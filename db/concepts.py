#!/usr/bin/env python3
"""
Concept-graph layer for the ai-links collection.

This module implements Layer 2 of CURATION_DESIGN.md:

    * Concept lifecycle helpers — create / merge / archive / rename.
    * Observation lifecycle — record / promote / dismiss / supersede.
    * Mechanical discovery passes — shared external URLs, shared mentions.
      These are SQL-only, deterministic, run continuously. Semantic and
      latent passes come later (steps 6 and 9 in the design doc).
    * Query helpers for the viewer / morning surface.
    * CLI entry points for one-off curation ("promote N", "merge A into B",
      "list active concepts", etc.) while the full chat-mediated curate.py
      skill is still being built.

The candidate/canonical split is the structural decision the doc commits to:
discovery passes write to `concept_observations` (immutable history with full
provenance); curation writes to `post_concepts` (one row per (post, concept)
reflecting the human's truth). Never bypass that — even hand-curated concepts
should write an observation row and a post_concepts row together via
`record_observation` + `promote_observation`, so the provenance trail stays
honest.

CLI:
    python3 -m db.concepts list                  # active concepts + post counts
    python3 -m db.concepts pending [CONCEPT_ID]  # pending observations
    python3 -m db.concepts promote OBS_ID        # promote an observation
    python3 -m db.concepts dismiss OBS_ID        # dismiss an observation
    python3 -m db.concepts merge SRC_ID DST_ID   # merge one concept into another
    python3 -m db.concepts discover              # run mechanical discovery passes
    python3 -m db.concepts stats                 # corpus-level concept stats
"""

import sqlite3
import argparse
import datetime
import re
from pathlib import Path
from contextlib import contextmanager
from typing import Optional, Iterable, Sequence
from collections import defaultdict, Counter
from urllib.parse import urlparse

try:
    from .lock import writer_lock
except ImportError:
    import sys
    sys.path.insert(0, str(Path(__file__).parent))
    from lock import writer_lock

SCRIPT_DIR = Path(__file__).parent
DEFAULT_DB = SCRIPT_DIR / "ai_links.db"

# Status enums
CONCEPT_ACTIVE = "active"
CONCEPT_ARCHIVED = "archived"
CONCEPT_MERGED = "merged-into"

CONCEPT_SOURCE_DISCOVERED = "discovered"
CONCEPT_SOURCE_CURATED = "curated"
CONCEPT_SOURCE_MERGED = "merged"

OBS_PENDING = "pending"
OBS_PROMOTED = "promoted"
OBS_DISMISSED = "dismissed"
OBS_SUPERSEDED = "superseded"

ROLE_EVIDENCE = "evidence"
ROLE_COUNTER = "counter-example"
ROLE_TANGENTIAL = "tangential"
ROLE_ORIGIN = "origin"

SOURCE_MECHANICAL = "mechanical"
SOURCE_SEMANTIC = "semantic"
SOURCE_LATENT = "latent"

SCORE_MECHANICAL = "mechanical-overlap"
SCORE_SEMANTIC = "cosine-similarity"
SCORE_LATENT = "llm-self-report"


# ---- Connection helper -------------------------------------------------

@contextmanager
def _connect(db_path: Path = DEFAULT_DB):
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys=ON")
    try:
        yield conn
    finally:
        conn.close()


@contextmanager
def _maybe_lock(with_lock: bool):
    if with_lock:
        with writer_lock():
            yield
    else:
        yield


def _now() -> str:
    return datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")


# ---- Concept lifecycle ------------------------------------------------

def create_concept(name: str, description: str = "",
                   source: str = CONCEPT_SOURCE_CURATED,
                   db_path: Path = DEFAULT_DB,
                   with_lock: bool = True) -> int:
    """Create a new concept. Returns the new concept id."""
    with _maybe_lock(with_lock), _connect(db_path) as conn:
        cur = conn.execute("""
            INSERT INTO concepts (name, description, source, status, created_at, updated_at)
            VALUES (?, ?, ?, 'active', ?, ?)
        """, (name, description, source, _now(), _now()))
        conn.commit()
        return cur.lastrowid


def rename_concept(concept_id: int, new_name: str,
                   description: Optional[str] = None,
                   db_path: Path = DEFAULT_DB, with_lock: bool = True) -> None:
    with _maybe_lock(with_lock), _connect(db_path) as conn:
        if description is None:
            conn.execute("UPDATE concepts SET name=?, updated_at=? WHERE id=?",
                         (new_name, _now(), concept_id))
        else:
            conn.execute("UPDATE concepts SET name=?, description=?, updated_at=? WHERE id=?",
                         (new_name, description, _now(), concept_id))
        conn.commit()


def archive_concept(concept_id: int, db_path: Path = DEFAULT_DB,
                    with_lock: bool = True) -> None:
    """Mark a concept archived. Posts attached to it remain attached; it
    just stops surfacing in active-concept views."""
    with _maybe_lock(with_lock), _connect(db_path) as conn:
        conn.execute("UPDATE concepts SET status=?, updated_at=? WHERE id=?",
                     (CONCEPT_ARCHIVED, _now(), concept_id))
        conn.commit()


def merge_concepts(source_id: int, dest_id: int,
                   db_path: Path = DEFAULT_DB, with_lock: bool = True) -> dict:
    """Merge `source_id` into `dest_id`. Flatten-on-merge in one transaction.

    Per design (CURATION_DESIGN.md Layer 2): reject cycles before write, then
    rewrite all post_concepts and concept_observations rows from source to
    dest, mark source as 'merged-into' with merged_into=dest_id. No recursive
    CTE at read time.

    Returns counts of what was moved.
    """
    if source_id == dest_id:
        raise ValueError("Cannot merge a concept into itself")

    with _maybe_lock(with_lock), _connect(db_path) as conn:
        # Cycle rejection — if dest has previously been merged into source
        # (directly or transitively), the merge would create a cycle.
        cycle_check = conn.execute("""
            WITH RECURSIVE chain(id) AS (
                SELECT merged_into FROM concepts WHERE id = ?
                UNION
                SELECT c.merged_into FROM concepts c JOIN chain ON c.id = chain.id
                WHERE c.merged_into IS NOT NULL
            )
            SELECT 1 FROM chain WHERE id = ?
        """, (dest_id, source_id)).fetchone()
        if cycle_check:
            raise ValueError(f"Refusing to merge: cycle detected ({source_id} ↔ {dest_id})")

        if not conn.execute("SELECT 1 FROM concepts WHERE id=? AND status='active'",
                            (dest_id,)).fetchone():
            raise ValueError(f"Destination concept {dest_id} doesn't exist or isn't active")

        conn.execute("BEGIN")
        try:
            obs_moved = conn.execute(
                "UPDATE concept_observations SET concept_id=? WHERE concept_id=?",
                (dest_id, source_id),
            ).rowcount

            # post_concepts has PK (post_id, concept_id) so a naive UPDATE could
            # violate uniqueness. INSERT OR IGNORE the source rows into dest first,
            # then delete source rows.
            conn.execute("""
                INSERT OR IGNORE INTO post_concepts
                    (post_id, concept_id, role, promoted_from_observation_id, notes, promoted_at)
                SELECT post_id, ?, role, promoted_from_observation_id, notes, promoted_at
                  FROM post_concepts WHERE concept_id = ?
            """, (dest_id, source_id))
            edges_moved = conn.execute(
                "DELETE FROM post_concepts WHERE concept_id=?", (source_id,)
            ).rowcount

            conn.execute("""
                UPDATE concepts
                   SET status=?, merged_into=?, updated_at=?
                 WHERE id=?
            """, (CONCEPT_MERGED, dest_id, _now(), source_id))

            conn.execute("UPDATE concepts SET updated_at=? WHERE id=?", (_now(), dest_id))
            conn.commit()
            return {"observations_moved": obs_moved, "canonical_edges_moved": edges_moved}
        except Exception:
            conn.rollback()
            raise


# ---- Observation lifecycle ---------------------------------------------

def record_observation(post_id: int, concept_id: int, *,
                       source: str,
                       score_kind: str,
                       raw_score: float = 1.0,
                       role_suggestion: str = ROLE_EVIDENCE,
                       discovery_run_id: Optional[int] = None,
                       discovery_persona: Optional[str] = None,
                       discovery_model: Optional[str] = None,
                       notes: Optional[str] = None,
                       status: str = OBS_PENDING,
                       db_path: Path = DEFAULT_DB,
                       with_lock: bool = True) -> Optional[int]:
    """Record a discovery event. Returns the new observation id, or None
    if a `pending`/`promoted` observation already exists for this exact
    (post, concept, source, persona, model) — we don't regenerate dupes.
    Dismissed prior observations for the pair also block — that's the
    suppression semantic for the dismissal record (see design doc).
    """
    with _maybe_lock(with_lock), _connect(db_path) as conn:
        # Dedup against existing non-superseded observations for the same
        # discovery shape. The PK is auto-id so we check by content.
        existing = conn.execute("""
            SELECT id, status FROM concept_observations
             WHERE post_id=? AND concept_id=?
               AND source=?
               AND COALESCE(discovery_persona,'')=COALESCE(?, '')
               AND COALESCE(discovery_model,'')=COALESCE(?, '')
               AND status IN ('pending', 'promoted', 'dismissed')
        """, (post_id, concept_id, source, discovery_persona, discovery_model)).fetchone()
        if existing:
            return None

        cur = conn.execute("""
            INSERT INTO concept_observations (
                post_id, concept_id, role_suggestion, raw_score, score_kind,
                source, discovery_run_id, discovery_persona, discovery_model,
                status, observed_at, notes
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (post_id, concept_id, role_suggestion, raw_score, score_kind,
              source, discovery_run_id, discovery_persona, discovery_model,
              status, _now(), notes))
        conn.commit()
        return cur.lastrowid


def promote_observation(observation_id: int, *,
                         role: Optional[str] = None,
                         notes: Optional[str] = None,
                         db_path: Path = DEFAULT_DB,
                         with_lock: bool = True) -> None:
    """Promote a pending observation to a canonical post_concepts edge.

    Sets observation status to 'promoted' and inserts (or no-ops) the
    canonical row. If a canonical edge for (post, concept) already exists,
    leaves it in place — first promotion wins. Use `rename_concept` or
    direct UPDATE to change role on the canonical edge.
    """
    with _maybe_lock(with_lock), _connect(db_path) as conn:
        obs = conn.execute(
            "SELECT * FROM concept_observations WHERE id = ?", (observation_id,)
        ).fetchone()
        if not obs:
            raise ValueError(f"observation {observation_id} not found")

        chosen_role = role or obs["role_suggestion"] or ROLE_EVIDENCE
        conn.execute("BEGIN")
        try:
            conn.execute("""
                INSERT OR IGNORE INTO post_concepts
                    (post_id, concept_id, role, promoted_from_observation_id, notes, promoted_at)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (obs["post_id"], obs["concept_id"], chosen_role, observation_id,
                  notes, _now()))
            conn.execute(
                "UPDATE concept_observations SET status=? WHERE id=?",
                (OBS_PROMOTED, observation_id),
            )
            conn.execute(
                "UPDATE concepts SET updated_at=? WHERE id=?",
                (_now(), obs["concept_id"]),
            )
            conn.commit()
        except Exception:
            conn.rollback()
            raise


def dismiss_observation(observation_id: int, *,
                         notes: Optional[str] = None,
                         db_path: Path = DEFAULT_DB,
                         with_lock: bool = True) -> None:
    """Mark an observation dismissed. Future discovery passes skip it
    (dedup in record_observation checks against dismissed too)."""
    with _maybe_lock(with_lock), _connect(db_path) as conn:
        if notes is None:
            conn.execute("UPDATE concept_observations SET status=? WHERE id=?",
                         (OBS_DISMISSED, observation_id))
        else:
            conn.execute("UPDATE concept_observations SET status=?, notes=? WHERE id=?",
                         (OBS_DISMISSED, notes, observation_id))
        conn.commit()


# ---- Query helpers -----------------------------------------------------

def list_active_concepts(db_path: Path = DEFAULT_DB) -> list[dict]:
    """List active concepts with promoted-evidence counts."""
    with _connect(db_path) as conn:
        rows = conn.execute("""
            SELECT
                c.id, c.name, c.description, c.source, c.created_at, c.updated_at,
                (SELECT COUNT(*) FROM post_concepts pc WHERE pc.concept_id = c.id) AS post_count,
                (SELECT COUNT(*) FROM concept_observations o
                  WHERE o.concept_id = c.id AND o.status = 'pending') AS pending_count
              FROM concepts c
             WHERE c.status = 'active'
             ORDER BY post_count DESC, c.updated_at DESC
        """).fetchall()
    return [dict(r) for r in rows]


def pending_observations(concept_id: Optional[int] = None,
                          db_path: Path = DEFAULT_DB, limit: int = 50) -> list[dict]:
    """Pending observations, optionally filtered to one concept.
    Joins post + concept so the curator sees what they're deciding on."""
    where = "o.status = 'pending'"
    params: list = []
    if concept_id is not None:
        where += " AND o.concept_id = ?"
        params.append(concept_id)
    sql = f"""
        SELECT
            o.id              AS observation_id,
            o.post_id, o.concept_id, o.source, o.score_kind, o.raw_score,
            o.discovery_persona, o.discovery_model, o.notes,
            c.name            AS concept_name,
            p.author          AS post_author,
            p.date            AS post_date,
            p.url             AS post_url,
            SUBSTR(COALESCE(p.summary,''), 1, 200) AS post_summary
          FROM concept_observations o
          JOIN concepts c ON c.id = o.concept_id
          JOIN posts    p ON p.id = o.post_id
         WHERE {where}
         ORDER BY o.observed_at DESC
         LIMIT ?
    """
    params.append(limit)
    with _connect(db_path) as conn:
        rows = conn.execute(sql, params).fetchall()
    return [dict(r) for r in rows]


def concept_post_ids(concept_id: int, db_path: Path = DEFAULT_DB) -> list[int]:
    """Canonical posts attached to a concept (promoted only)."""
    with _connect(db_path) as conn:
        rows = conn.execute(
            "SELECT post_id FROM post_concepts WHERE concept_id=? ORDER BY promoted_at",
            (concept_id,),
        ).fetchall()
    return [r[0] for r in rows]


def recent_active_concepts(days: int = 7, db_path: Path = DEFAULT_DB,
                            limit: int = 5) -> list[dict]:
    """Concepts that recently gained evidence — for the morning view's
    "Recurring this week" section.

    Ranks by **post-date recency**, not observation-date. The observation
    timestamp is when the system noticed the connection; the post date is
    when the idea actually appeared in Jeremy's feed. The morning view
    cares about the latter.

    Concepts with no recent evidence at all are excluded. Concepts that
    only have older evidence (long-term threads that aren't moving) won't
    surface here — they're still browseable via the concepts list.
    """
    with _connect(db_path) as conn:
        rows = conn.execute(f"""
            SELECT
                c.id, c.name, c.description,
                (SELECT COUNT(*) FROM post_concepts pc WHERE pc.concept_id = c.id) AS post_count,
                (SELECT COUNT(DISTINCT pc.post_id)
                   FROM post_concepts pc
                   JOIN posts p ON p.id = pc.post_id
                  WHERE pc.concept_id = c.id
                    AND p.date >= date('now', ?)
                ) AS recent_post_count,
                (SELECT MAX(p.date)
                   FROM post_concepts pc
                   JOIN posts p ON p.id = pc.post_id
                  WHERE pc.concept_id = c.id) AS last_post_date
              FROM concepts c
             WHERE c.status = 'active'
               AND EXISTS (
                   SELECT 1 FROM post_concepts pc
                     JOIN posts p ON p.id = pc.post_id
                    WHERE pc.concept_id = c.id
                      AND p.date >= date('now', ?)
               )
             ORDER BY recent_post_count DESC, post_count DESC, last_post_date DESC
             LIMIT ?
        """, (f'-{days} days', f'-{days} days', limit)).fetchall()
    return [dict(r) for r in rows]


def top_posts_for_concept(concept_id: int, limit: int = 3,
                           db_path: Path = DEFAULT_DB) -> list[dict]:
    """Top promoted posts attached to a concept, newest first."""
    with _connect(db_path) as conn:
        rows = conn.execute("""
            SELECT p.id, p.date, p.author, p.handle, p.url,
                   SUBSTR(COALESCE(p.summary,''), 1, 200) AS summary
              FROM post_concepts pc
              JOIN posts p ON p.id = pc.post_id
             WHERE pc.concept_id = ?
             ORDER BY p.date DESC
             LIMIT ?
        """, (concept_id, limit)).fetchall()
    return [dict(r) for r in rows]


# ---- Mechanical discovery ---------------------------------------------

def _start_run(conn, source: str, sampling_strategy: str,
               persona: Optional[str] = None,
               model: Optional[str] = None) -> int:
    cur = conn.execute("""
        INSERT INTO discovery_runs
            (started_at, source, persona, model, sampling_strategy)
        VALUES (?, ?, ?, ?, ?)
    """, (_now(), source, persona, model, sampling_strategy))
    return cur.lastrowid


def _finish_run(conn, run_id: int, posts_examined: int, observations_created: int,
                 notes: Optional[str] = None) -> None:
    conn.execute("""
        UPDATE discovery_runs
           SET finished_at = ?, posts_examined = ?, observations_created = ?, notes = ?
         WHERE id = ?
    """, (_now(), posts_examined, observations_created, notes, run_id))


# URLs we ignore as "evidence" for a concept — too generic to mean anything.
_GENERIC_DOMAINS = {
    "x.com", "twitter.com", "t.co", "fxtwitter.com", "vxtwitter.com",
    "youtube.com", "youtu.be",
    "google.com", "google.co", "google.de", "google.fr",
}


def _interesting_external_urls(post: dict, conn) -> set[str]:
    """Extract external URLs that are concept-worthy.

    Looks at:
      - thread segments of type 'external_link'
      - URLs found in summary/content text via regex
    Filters out the post's own URL and generic hosts.
    """
    found: set[str] = set()

    # Segments
    seg_rows = conn.execute(
        "SELECT url FROM post_thread_segments WHERE post_id=? AND url IS NOT NULL AND url != ''",
        (post["id"],),
    ).fetchall()
    for r in seg_rows:
        url = (r[0] or "").strip()
        if url:
            found.add(url)

    # Regex over summary + content
    text_blob = (post.get("summary") or "") + " " + (post.get("content") or "")
    for m in re.finditer(r'https?://[^\s\)\]\}>"]+', text_blob):
        found.add(m.group(0).rstrip('.,;:'))
    # Also match bare host/path mentions like "github.com/user/repo" (no scheme)
    for m in re.finditer(r'\b(?:github\.com|arxiv\.org|huggingface\.co)/[A-Za-z0-9_./-]+', text_blob):
        found.add("https://" + m.group(0).rstrip('.,;:'))

    # Normalize + filter
    out: set[str] = set()
    own_url = (post.get("url") or "").strip()
    for url in found:
        url = url.rstrip('/')
        if not url or url == own_url:
            continue
        try:
            host = urlparse(url).netloc.lower()
        except Exception:
            continue
        host = host.lstrip("www.")
        if host in _GENERIC_DOMAINS or not host:
            continue
        # Strip tracking params crudely
        url = re.sub(r'\?(s|t|utm_[A-Za-z_]+)=[^&]*(&|$)', '?', url)
        url = url.rstrip('?&')
        out.add(url)
    return out


def _mentioned_handles(post: dict) -> set[str]:
    """@handle mentions in the post body, lowercased. Excludes the post's own handle."""
    text_blob = (post.get("summary") or "") + " " + (post.get("content") or "")
    own = (post.get("handle") or "").lower().lstrip("@")
    out: set[str] = set()
    for m in re.finditer(r'@([A-Za-z0-9_]{2,30})', text_blob):
        h = m.group(1).lower()
        if h != own and h not in {"every"}:  # exclude common stopwords
            out.add(h)
    return out


def discover_shared_external_urls(db_path: Path = DEFAULT_DB,
                                   min_evidence: int = 2,
                                   with_lock: bool = True) -> dict:
    """Mechanical pass: find external URLs that appear across multiple posts.

    For each unique URL referenced by `min_evidence` or more posts, create a
    discovered concept (named after the URL) and observation rows linking
    those posts to it. If a discovered concept with the same name already
    exists, attach new observations to it.

    Returns stats: {urls_seen, urls_promoted, concepts_created, observations_created}.
    """
    stats = {"urls_seen": 0, "urls_promoted": 0,
             "concepts_created": 0, "observations_created": 0}

    with _maybe_lock(with_lock), _connect(db_path) as conn:
        run_id = _start_run(conn, SOURCE_MECHANICAL, "shared-external-url")

        # Pull enriched-enough posts only (skip empty / dead so we don't
        # build concepts on noise).
        posts = conn.execute("""
            SELECT id, url, handle, summary, content
              FROM posts
             WHERE enrichment_status IN ('ok', 'legacy-ok')
        """).fetchall()

        url_to_posts: dict[str, list[int]] = defaultdict(list)
        posts_examined = 0
        for row in posts:
            posts_examined += 1
            urls = _interesting_external_urls(dict(row), conn)
            for u in urls:
                url_to_posts[u].append(row["id"])

        stats["urls_seen"] = len(url_to_posts)

        # For each URL with enough evidence, create or find a concept.
        for url, post_ids in url_to_posts.items():
            unique_posts = list(set(post_ids))
            if len(unique_posts) < min_evidence:
                continue
            stats["urls_promoted"] += 1

            concept_name = f"url:{url}"
            existing = conn.execute(
                "SELECT id FROM concepts WHERE name = ? AND status = 'active'",
                (concept_name,),
            ).fetchone()
            if existing:
                concept_id = existing[0]
            else:
                cur = conn.execute("""
                    INSERT INTO concepts (name, description, source, status, created_at, updated_at)
                    VALUES (?, ?, ?, 'active', ?, ?)
                """, (concept_name, f"Posts referencing {url}",
                      CONCEPT_SOURCE_DISCOVERED, _now(), _now()))
                concept_id = cur.lastrowid
                stats["concepts_created"] += 1

            # Strength = number of co-citing posts (cap at 5).
            strength = min(len(unique_posts) / 5.0, 1.0)
            for post_id in unique_posts:
                obs_id = _record_obs_in_txn(
                    conn,
                    post_id=post_id, concept_id=concept_id,
                    source=SOURCE_MECHANICAL,
                    score_kind=SCORE_MECHANICAL,
                    raw_score=strength,
                    discovery_run_id=run_id,
                    notes=f"co-cites {url}",
                )
                if obs_id is not None:
                    stats["observations_created"] += 1

        _finish_run(conn, run_id, posts_examined, stats["observations_created"],
                    notes=f"min_evidence={min_evidence}")
        conn.commit()

    return stats


def discover_shared_mentions(db_path: Path = DEFAULT_DB,
                              min_evidence: int = 3,
                              with_lock: bool = True) -> dict:
    """Mechanical pass: find @handles mentioned across multiple posts.

    Threshold default is 3 (vs 2 for URLs) because mentions are noisier —
    a person can be cited in passing.
    """
    stats = {"handles_seen": 0, "handles_promoted": 0,
             "concepts_created": 0, "observations_created": 0}

    with _maybe_lock(with_lock), _connect(db_path) as conn:
        run_id = _start_run(conn, SOURCE_MECHANICAL, "shared-mention")

        posts = conn.execute("""
            SELECT id, handle, summary, content
              FROM posts
             WHERE enrichment_status IN ('ok', 'legacy-ok')
        """).fetchall()

        handle_to_posts: dict[str, list[int]] = defaultdict(list)
        posts_examined = 0
        for row in posts:
            posts_examined += 1
            for h in _mentioned_handles(dict(row)):
                handle_to_posts[h].append(row["id"])

        stats["handles_seen"] = len(handle_to_posts)

        for handle, post_ids in handle_to_posts.items():
            unique_posts = list(set(post_ids))
            if len(unique_posts) < min_evidence:
                continue
            stats["handles_promoted"] += 1

            concept_name = f"mention:@{handle}"
            existing = conn.execute(
                "SELECT id FROM concepts WHERE name = ? AND status = 'active'",
                (concept_name,),
            ).fetchone()
            if existing:
                concept_id = existing[0]
            else:
                cur = conn.execute("""
                    INSERT INTO concepts (name, description, source, status, created_at, updated_at)
                    VALUES (?, ?, ?, 'active', ?, ?)
                """, (concept_name,
                      f"Posts mentioning @{handle} as a recurring reference point",
                      CONCEPT_SOURCE_DISCOVERED, _now(), _now()))
                concept_id = cur.lastrowid
                stats["concepts_created"] += 1

            strength = min(len(unique_posts) / 8.0, 1.0)
            for post_id in unique_posts:
                obs_id = _record_obs_in_txn(
                    conn,
                    post_id=post_id, concept_id=concept_id,
                    source=SOURCE_MECHANICAL,
                    score_kind=SCORE_MECHANICAL,
                    raw_score=strength,
                    discovery_run_id=run_id,
                    notes=f"mentions @{handle}",
                )
                if obs_id is not None:
                    stats["observations_created"] += 1

        _finish_run(conn, run_id, posts_examined, stats["observations_created"],
                    notes=f"min_evidence={min_evidence}")
        conn.commit()

    return stats


def _record_obs_in_txn(conn, *, post_id: int, concept_id: int, source: str,
                        score_kind: str, raw_score: float = 1.0,
                        discovery_run_id: Optional[int] = None,
                        discovery_persona: Optional[str] = None,
                        discovery_model: Optional[str] = None,
                        notes: Optional[str] = None,
                        role_suggestion: str = ROLE_EVIDENCE) -> Optional[int]:
    """Like record_observation, but uses the open connection (no nested
    lock / connect). Used inside discovery passes that already hold both."""
    existing = conn.execute("""
        SELECT id FROM concept_observations
         WHERE post_id=? AND concept_id=?
           AND source=?
           AND COALESCE(discovery_persona,'')=COALESCE(?, '')
           AND COALESCE(discovery_model,'')=COALESCE(?, '')
           AND status IN ('pending', 'promoted', 'dismissed')
    """, (post_id, concept_id, source, discovery_persona, discovery_model)).fetchone()
    if existing:
        return None
    cur = conn.execute("""
        INSERT INTO concept_observations (
            post_id, concept_id, role_suggestion, raw_score, score_kind,
            source, discovery_run_id, discovery_persona, discovery_model,
            status, observed_at, notes
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'pending', ?, ?)
    """, (post_id, concept_id, role_suggestion, raw_score, score_kind,
          source, discovery_run_id, discovery_persona, discovery_model,
          _now(), notes))
    return cur.lastrowid


def run_all_mechanical_passes(db_path: Path = DEFAULT_DB,
                               with_lock: bool = True) -> dict:
    """Run every mechanical-discovery flavor under a single lock acquisition."""
    out = {}
    with _maybe_lock(with_lock):
        out["shared_external_urls"] = discover_shared_external_urls(
            db_path=db_path, with_lock=False,
        )
        out["shared_mentions"] = discover_shared_mentions(
            db_path=db_path, with_lock=False,
        )
    return out


# ---- CLI --------------------------------------------------------------

def _cmd_list(args):
    rows = list_active_concepts(args.db)
    if not rows:
        print("No active concepts.")
        return
    print(f"{'id':>5}  {'name':40s}  {'posts':>6}  {'pending':>8}  source")
    print("-" * 80)
    for r in rows:
        name = (r["name"] or "")[:40]
        print(f"{r['id']:>5}  {name:40s}  {r['post_count']:>6}  {r['pending_count']:>8}  {r['source']}")


def _cmd_pending(args):
    rows = pending_observations(args.concept_id, args.db, args.limit)
    if not rows:
        print("No pending observations.")
        return
    for r in rows:
        print(f"#{r['observation_id']}  concept={r['concept_id']} ({r['concept_name']})  "
              f"post={r['post_id']} ({r['post_author']} {r['post_date']})  "
              f"src={r['source']}  notes={r['notes'] or ''}")
        if r.get("post_summary"):
            print(f"      {r['post_summary']}")


def _cmd_promote(args):
    promote_observation(args.observation_id)
    print(f"Promoted observation #{args.observation_id}")


def _cmd_dismiss(args):
    dismiss_observation(args.observation_id, notes=args.notes)
    print(f"Dismissed observation #{args.observation_id}")


def _cmd_merge(args):
    out = merge_concepts(args.source_id, args.dest_id)
    print(f"Merged {args.source_id} → {args.dest_id}: {out}")


def _cmd_discover(args):
    stats = run_all_mechanical_passes(args.db)
    for pass_name, s in stats.items():
        print(f"{pass_name}:")
        for k, v in s.items():
            print(f"    {k:25s} {v}")


def _cmd_stats(args):
    with _connect(args.db) as conn:
        for name in ("concepts", "concept_observations", "post_concepts", "discovery_runs"):
            n = conn.execute(f"SELECT COUNT(*) FROM {name}").fetchone()[0]
            print(f"  {name:25s} {n}")
        print()
        print("Observations by status:")
        for r in conn.execute(
            "SELECT status, COUNT(*) FROM concept_observations GROUP BY status"
        ):
            print(f"  {r[0]:15s} {r[1]}")
        print()
        print("Top concepts by promoted edges:")
        for r in conn.execute("""
            SELECT c.id, c.name, COUNT(pc.post_id) AS n
              FROM concepts c
              LEFT JOIN post_concepts pc ON pc.concept_id = c.id
             WHERE c.status='active'
             GROUP BY c.id ORDER BY n DESC LIMIT 10
        """):
            print(f"  #{r[0]:<5} {r[1][:50]:50s}  {r[2]:>4} promoted")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", type=Path, default=DEFAULT_DB)
    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("list").set_defaults(func=_cmd_list)

    p = sub.add_parser("pending")
    p.add_argument("concept_id", type=int, nargs="?", default=None)
    p.add_argument("--limit", type=int, default=50)
    p.set_defaults(func=_cmd_pending)

    p = sub.add_parser("promote")
    p.add_argument("observation_id", type=int)
    p.set_defaults(func=_cmd_promote)

    p = sub.add_parser("dismiss")
    p.add_argument("observation_id", type=int)
    p.add_argument("--notes", type=str, default=None)
    p.set_defaults(func=_cmd_dismiss)

    p = sub.add_parser("merge")
    p.add_argument("source_id", type=int)
    p.add_argument("dest_id", type=int)
    p.set_defaults(func=_cmd_merge)

    sub.add_parser("discover").set_defaults(func=_cmd_discover)
    sub.add_parser("stats").set_defaults(func=_cmd_stats)

    args = parser.parse_args()
    if not getattr(args, "func", None):
        parser.print_help()
        return
    args.func(args)


if __name__ == "__main__":
    main()
