#!/usr/bin/env python3
"""
Persistence helpers for the unified enrichment path.

This module is the *persistence layer* for enrichment work. It is intentionally
NOT an orchestrator — Chrome scraping and LLM summarization happen at the
calling skill layer (where Claude has access to the MCP browser tools and is
itself the model doing the classification). The skill calls into these
helpers to persist results.

Concretely: both the daily sync skill and the catch-up skill share this
module. Each skill is responsible for:
    1. Selecting work (via `pending_enrichment_ids` or `recent_partial_ids`)
    2. Doing the Chrome scrape (MCP browser tools)
    3. Composing structured segments + a summary + topics
    4. Calling `record_enrichment` (or `record_partial` / `record_dead`) to
       persist with the correct enrichment_status + version

The current enrichment generation is ENRICHMENT_VERSION. Bump it whenever the
capture/classification logic changes meaningfully; rolling re-enrichment then
targets `enrichment_version < ENRICHMENT_VERSION`.

All write functions acquire the shared writer lock (db/lock.py) when called
in their default mode. Callers performing many writes in one batch should
acquire the lock once externally and pass `with_lock=False` for individual
calls to avoid lock churn.

Usage sketch (in a skill):

    from db.enrich import (
        pending_enrichment_ids, record_enrichment, record_partial,
        record_dead, ENRICHMENT_VERSION,
    )
    from db.lock import writer_lock

    with writer_lock():
        ids = pending_enrichment_ids(limit=10)
        for post_id in ids:
            try:
                segments, summary, topics, audiences, views, priority = scrape(post_id)
                if is_dead_signal(segments, summary):
                    record_dead(post_id, reason=summary, with_lock=False)
                elif not segments or not summary:
                    record_partial(post_id, error="empty capture", with_lock=False)
                else:
                    record_enrichment(
                        post_id, segments=segments, summary=summary,
                        topics=topics, audiences=audiences,
                        views=views, priority=priority,
                        with_lock=False,
                    )
            except Exception as e:
                record_partial(post_id, error=str(e), with_lock=False)
"""

import sqlite3
import datetime
from pathlib import Path
from contextlib import contextmanager
from typing import Optional, Sequence, Iterable

try:
    from .lock import writer_lock
except ImportError:
    # Run as a script (python3 db/enrich.py) rather than imported as a package.
    import sys
    sys.path.insert(0, str(Path(__file__).parent))
    from lock import writer_lock

SCRIPT_DIR = Path(__file__).parent
DEFAULT_DB = SCRIPT_DIR / "ai_links.db"

# The current generation of enrichment logic. Bump this in the same change
# that meaningfully alters capture or classification. Rolling background
# re-enrichment targets `enrichment_version < ENRICHMENT_VERSION`.
ENRICHMENT_VERSION = 1

# Status values used by the enrichment pipeline.
STATUS_OK = "ok"
STATUS_PARTIAL = "partial"
STATUS_FAILED = "failed"
STATUS_DEAD = "dead"
STATUS_LEGACY_OK = "legacy-ok"
STATUS_UNATTEMPTED = "unattempted"

VALID_STATUSES = {
    STATUS_OK, STATUS_PARTIAL, STATUS_FAILED,
    STATUS_DEAD, STATUS_LEGACY_OK, STATUS_UNATTEMPTED,
}

# Permanent-floor statuses — re-enrichment will not retry these.
DEAD_STATUSES = {STATUS_DEAD}

# Statuses that count as "needs work" for the re-scrape / catch-up queue.
# Excludes DEAD (permanent) and OK at the current version.
RECOVERABLE_STATUSES = {STATUS_PARTIAL, STATUS_FAILED, STATUS_UNATTEMPTED}


# ---- Connection helper -------------------------------------------------

@contextmanager
def _connect(db_path: Path = DEFAULT_DB):
    """Open a connection with sensible pragmas for short writer sessions."""
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys=ON")
    try:
        yield conn
    finally:
        conn.close()


@contextmanager
def _maybe_lock(with_lock: bool):
    """Acquire the writer lock if requested; otherwise no-op."""
    if with_lock:
        with writer_lock():
            yield
    else:
        yield


def _now() -> str:
    return datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")


# ---- Work-queue queries (read-only, no lock) ---------------------------

def pending_enrichment_ids(limit: int = 50,
                           db_path: Path = DEFAULT_DB,
                           statuses: Sequence[str] = None,
                           below_version: int = ENRICHMENT_VERSION) -> list[int]:
    """Return post IDs that need enrichment work.

    Includes posts whose `enrichment_status` is in `RECOVERABLE_STATUSES`
    OR whose `enrichment_version` is below the current generation.
    Excludes DEAD posts (permanent floor).

    Order: most-recent date first, then highest id. Newest work surfaces
    first, which is what both the daily sync and the catch-up skill want.

    Args:
        limit: max number of IDs to return.
        statuses: optional restriction to specific statuses. Defaults to
            RECOVERABLE_STATUSES (everything not OK and not DEAD).
        below_version: only consider rows with enrichment_version strictly
            below this number. Defaults to ENRICHMENT_VERSION so older
            generations get re-processed.
    """
    if statuses is None:
        statuses = tuple(RECOVERABLE_STATUSES)
    placeholders = ",".join(["?"] * len(statuses))
    sql = f"""
        SELECT id FROM posts
        WHERE enrichment_status IN ({placeholders})
           OR (enrichment_status NOT IN ('dead') AND enrichment_version < ?)
        ORDER BY date DESC, id DESC
        LIMIT ?
    """
    with _connect(db_path) as conn:
        rows = conn.execute(sql, (*statuses, below_version, limit)).fetchall()
    return [r[0] for r in rows]


def status_breakdown(db_path: Path = DEFAULT_DB) -> dict[str, int]:
    """Return a status -> count map. Useful for the gate computation and reporting."""
    with _connect(db_path) as conn:
        rows = conn.execute(
            "SELECT enrichment_status, COUNT(*) FROM posts GROUP BY enrichment_status"
        ).fetchall()
    return {r[0]: r[1] for r in rows}


def gate_ratio(db_path: Path = DEFAULT_DB) -> tuple[float, dict]:
    """Compute the latent-discovery gate ratio.

    Returns (ratio, breakdown) where ratio = (partial + failed) / (total - dead).
    Per CURATION_DESIGN.md: latent discovery activates when ratio < 0.05.
    `dead` is permanent and excluded from both numerator and denominator.
    """
    counts = status_breakdown(db_path)
    partial = counts.get(STATUS_PARTIAL, 0)
    failed = counts.get(STATUS_FAILED, 0)
    dead = counts.get(STATUS_DEAD, 0)
    total = sum(counts.values())
    denom = total - dead
    if denom <= 0:
        return 0.0, counts
    ratio = (partial + failed) / denom
    return ratio, counts


# ---- Status write helpers ---------------------------------------------

def _record_attempt(conn, post_id: int, error: Optional[str]) -> None:
    """Increment attempts counter and record last error/timestamp."""
    conn.execute("""
        UPDATE posts
           SET enrichment_attempts = enrichment_attempts + 1,
               enrichment_last_error = ?,
               enrichment_last_attempt_at = ?,
               updated_at = ?
         WHERE id = ?
    """, (error, _now(), _now(), post_id))


def record_enrichment(post_id: int, *,
                       segments: Sequence[dict] = (),
                       summary: Optional[str] = None,
                       topics: Sequence[str] = (),
                       audiences: Sequence[str] = (),
                       author: Optional[str] = None,
                       handle: Optional[str] = None,
                       views: Optional[str] = None,
                       priority: Optional[str] = None,
                       db_path: Path = DEFAULT_DB,
                       with_lock: bool = True) -> None:
    """Persist a successful enrichment.

    Marks the post `ok` at the current ENRICHMENT_VERSION. Writes:
        - posts.summary, content (joined segment text), enrichment_status,
          enrichment_version, attempts counter, last_attempt_at, optionally
          author/handle/views/priority.
        - post_thread_segments rows (replaces any prior segments for this post).
        - post_topics rows (replaces).
        - post_audiences rows (replaces).

    Args:
        segments: ordered list of dicts with keys
            {type, handle, text, url}. Ordinals are assigned by position.
        summary: 1-3 sentence summary of the post.
        topics, audiences: replace the post's topic and audience tags.
        author/handle/views: optional updates to those columns (skip if None).
        priority: optional priority update (skip if None).
        with_lock: acquire the writer lock for this call. Set False if
            caller already holds the lock for a batch.
    """
    with _maybe_lock(with_lock), _connect(db_path) as conn:
        conn.execute("BEGIN")
        try:
            # Build content blob from segment text (backward compat for code
            # still reading posts.content as a single blob). Segment table
            # remains the structured source.
            content_blob = "\n\n".join(
                (s.get("text") or "").strip() for s in segments
                if (s.get("text") or "").strip()
            )

            # Update post row.
            #
            # Note: per CURATION_DESIGN.md Layer 3, `posts.priority` is
            # read-only after migration 7 — all priority writes go to
            # `post_perspectives`. We DO NOT include `priority` in the
            # posts UPDATE below. The perspective write happens after the
            # row update, under the same transaction.
            updates = [
                "summary = ?",
                "content = ?",
                "enrichment_status = ?",
                "enrichment_version = ?",
                "enrichment_attempts = enrichment_attempts + 1",
                "enrichment_last_error = NULL",
                "enrichment_last_attempt_at = ?",
                "updated_at = ?",
                "enriched = 1",   # legacy boolean stays in sync during transition
            ]
            params: list = [
                summary or "",
                content_blob,
                STATUS_OK,
                ENRICHMENT_VERSION,
                _now(),
                _now(),
            ]
            if author is not None:
                updates.append("author = ?")
                params.append(author)
            if handle is not None:
                updates.append("handle = ?")
                params.append(handle)
            if views is not None:
                updates.append("views = ?")
                params.append(views)
            params.append(post_id)
            conn.execute(f"UPDATE posts SET {', '.join(updates)} WHERE id = ?", params)

            # Priority write: goes to post_perspectives, NOT posts.priority.
            # We do this inline (not via db.perspectives.set_priority) to keep
            # the whole enrichment write in one transaction. Mirrors the upsert
            # semantics there.
            if priority is not None:
                conn.execute("""
                    INSERT INTO post_perspectives (post_id, lens, priority, updated_at)
                    VALUES (?, 'tool-eval', ?, datetime('now'))
                    ON CONFLICT(post_id, lens) DO UPDATE SET
                        priority   = excluded.priority,
                        updated_at = excluded.updated_at
                """, (post_id, priority))

            # Replace thread segments.
            conn.execute("DELETE FROM post_thread_segments WHERE post_id = ?", (post_id,))
            for ordinal, seg in enumerate(segments):
                conn.execute("""
                    INSERT INTO post_thread_segments
                        (post_id, ordinal, type, handle, text, url, captured_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (
                    post_id, ordinal,
                    seg.get("type", "op"),
                    seg.get("handle"),
                    seg.get("text"),
                    seg.get("url"),
                    _now(),
                ))

            # Replace topics and audiences.
            if topics is not None:
                conn.execute("DELETE FROM post_topics WHERE post_id = ?", (post_id,))
                for topic in topics:
                    conn.execute(
                        "INSERT OR IGNORE INTO post_topics (post_id, topic) VALUES (?, ?)",
                        (post_id, topic),
                    )
            if audiences is not None:
                conn.execute("DELETE FROM post_audiences WHERE post_id = ?", (post_id,))
                for aud in audiences:
                    conn.execute(
                        "INSERT OR IGNORE INTO post_audiences (post_id, audience) VALUES (?, ?)",
                        (post_id, aud),
                    )

            conn.commit()
        except Exception:
            conn.rollback()
            raise


def record_partial(post_id: int, *,
                   error: Optional[str] = None,
                   segments: Sequence[dict] = (),
                   db_path: Path = DEFAULT_DB,
                   with_lock: bool = True) -> None:
    """Record a partial-success enrichment.

    Used when capture worked enough to know the post exists but didn't
    produce usable content/summary. Increments attempts; status becomes
    `partial`. Segments are written if provided (e.g., we got the OP but
    not the self-replies).
    """
    with _maybe_lock(with_lock), _connect(db_path) as conn:
        conn.execute("BEGIN")
        try:
            conn.execute("""
                UPDATE posts
                   SET enrichment_status = ?,
                       enrichment_attempts = enrichment_attempts + 1,
                       enrichment_last_error = ?,
                       enrichment_last_attempt_at = ?,
                       updated_at = ?
                 WHERE id = ?
            """, (STATUS_PARTIAL, error, _now(), _now(), post_id))

            if segments:
                conn.execute("DELETE FROM post_thread_segments WHERE post_id = ?", (post_id,))
                for ordinal, seg in enumerate(segments):
                    conn.execute("""
                        INSERT INTO post_thread_segments
                            (post_id, ordinal, type, handle, text, url, captured_at)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                    """, (
                        post_id, ordinal,
                        seg.get("type", "op"),
                        seg.get("handle"),
                        seg.get("text"),
                        seg.get("url"),
                        _now(),
                    ))
            conn.commit()
        except Exception:
            conn.rollback()
            raise


def record_failed(post_id: int, *,
                  error: str,
                  db_path: Path = DEFAULT_DB,
                  with_lock: bool = True) -> None:
    """Record an outright failure (Chrome unreachable, scrape exception, etc.).

    Status becomes `failed`. Used for transient errors that are expected to
    succeed on retry. Persistent failure after multiple attempts is the
    signal to surface a "needs attention" badge.
    """
    with _maybe_lock(with_lock), _connect(db_path) as conn:
        conn.execute("BEGIN")
        try:
            conn.execute("""
                UPDATE posts
                   SET enrichment_status = ?,
                       enrichment_attempts = enrichment_attempts + 1,
                       enrichment_last_error = ?,
                       enrichment_last_attempt_at = ?,
                       updated_at = ?
                 WHERE id = ?
            """, (STATUS_FAILED, error, _now(), _now(), post_id))
            conn.commit()
        except Exception:
            conn.rollback()
            raise


def record_dead(post_id: int, *,
                reason: str,
                summary: Optional[str] = None,
                db_path: Path = DEFAULT_DB,
                with_lock: bool = True) -> None:
    """Mark a post as permanently dead.

    Status becomes `dead` — the permanent floor. Re-enrichment will not retry.
    Used for 404s, suspended accounts, deleted tweets, login walls that have
    persisted past confirmation.
    """
    with _maybe_lock(with_lock), _connect(db_path) as conn:
        conn.execute("BEGIN")
        try:
            updates = [
                "enrichment_status = ?",
                "enrichment_attempts = enrichment_attempts + 1",
                "enrichment_last_error = ?",
                "enrichment_last_attempt_at = ?",
                "updated_at = ?",
            ]
            params: list = [STATUS_DEAD, reason, _now(), _now()]
            if summary is not None:
                updates.append("summary = ?")
                params.append(summary)
            params.append(post_id)
            conn.execute(
                f"UPDATE posts SET {', '.join(updates)} WHERE id = ?", params,
            )
            conn.commit()
        except Exception:
            conn.rollback()
            raise


def attempts_for(post_id: int, db_path: Path = DEFAULT_DB) -> int:
    """Return the current attempts counter for a post."""
    with _connect(db_path) as conn:
        row = conn.execute(
            "SELECT enrichment_attempts FROM posts WHERE id = ?", (post_id,)
        ).fetchone()
    return row[0] if row else 0


def get_post(post_id: int, db_path: Path = DEFAULT_DB) -> Optional[dict]:
    """Fetch a post row as a dict (or None if not found). Convenience for callers."""
    with _connect(db_path) as conn:
        row = conn.execute(
            "SELECT * FROM posts WHERE id = ?", (post_id,)
        ).fetchone()
    return dict(row) if row else None


def get_thread_segments(post_id: int, db_path: Path = DEFAULT_DB) -> list[dict]:
    """Fetch all segments for a post in order. Returns [] if none."""
    with _connect(db_path) as conn:
        rows = conn.execute("""
            SELECT ordinal, type, handle, text, url, captured_at
              FROM post_thread_segments
             WHERE post_id = ?
             ORDER BY ordinal
        """, (post_id,)).fetchall()
    return [dict(r) for r in rows]


# ---- CLI: status + gate report ----------------------------------------

def main():
    """Report current enrichment state and gate ratio. Diagnostic only."""
    import argparse
    parser = argparse.ArgumentParser(description="Enrichment state report")
    parser.add_argument("--db", type=Path, default=DEFAULT_DB)
    parser.add_argument("--limit", type=int, default=10,
                        help="Sample IDs to show from pending queue")
    args = parser.parse_args()

    ratio, counts = gate_ratio(args.db)
    total = sum(counts.values())
    dead = counts.get(STATUS_DEAD, 0)
    print(f"Enrichment status (total {total}, current ENRICHMENT_VERSION={ENRICHMENT_VERSION}):")
    for status in sorted(counts):
        print(f"  {status:15s} {counts[status]:4d}")
    print()
    print(f"Latent gate: (partial + failed) / (total - dead) = "
          f"{counts.get(STATUS_PARTIAL,0) + counts.get(STATUS_FAILED,0)} / "
          f"{total - dead} = {ratio:.3f}  "
          f"({'OPEN' if ratio < 0.05 else 'CLOSED (need <0.05)'})")
    print()
    pending = pending_enrichment_ids(limit=args.limit, db_path=args.db)
    print(f"Next {len(pending)} pending IDs:")
    for pid in pending:
        print(f"  {pid}")


if __name__ == "__main__":
    main()
