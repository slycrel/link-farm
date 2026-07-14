#!/usr/bin/env python3
"""
Recovery helpers for url-less / mis-keyed posts.

Background
----------
When ingest failed to extract a URL, the row was stored with `url = '[not found]'`
(or NULL/'') and, worse, its deterministic id was minted by hashing that
placeholder string. Such a row is invisible to enrichment (nothing to navigate
to) and to the catch-up skill's original backfill query (which only matched
`url IS NULL OR url = ''`, missing '[not found]'). It also carries the *wrong*
deterministic id: the canonical id for an X post is its status id, not a hash.

This module closes that gap with two pieces:

  * ``url_backfill_candidates`` — finds every row whose URL is missing OR a
    known placeholder sentinel (the superset the old query missed).
  * ``rekey_post`` / ``backfill_and_rekey`` — once a real URL is recovered,
    re-derives the correct deterministic id and migrates the row (and all of
    its foreign-key rows) onto it, so the deterministic-id invariant holds and
    future dedup works.

Callers (the sync + catch-up + backfill skills, or a manual repair) should run
these inside the shared writer lock; the ``*_and_rekey`` convenience wrappers
take the lock for you.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Optional

from db.migrate import (
    normalize_url, generate_id, is_missing_url, MISSING_URL_SENTINELS,
)

DEFAULT_DB = Path(__file__).parent / "ai_links.db"

# Tables with a single post_id foreign key that must follow a re-key.
_POST_FK_TABLES = (
    "link_checks", "post_audiences", "post_topics", "post_thread_segments",
    "concept_observations", "post_concepts", "post_embeddings",
    "post_perspectives",
)


def _sentinel_sql(col: str = "url") -> str:
    """SQL predicate matching a missing/placeholder URL column."""
    placeholders = ",".join("?" for _ in MISSING_URL_SENTINELS)
    # NULL, or trimmed-lowercased value in the sentinel set.
    return f"({col} IS NULL OR LOWER(TRIM({col})) IN ({placeholders}))"


def url_backfill_candidates(db_path: Path = DEFAULT_DB) -> list[dict]:
    """Rows whose URL is missing or a placeholder sentinel — need URL backfill.

    Superset of the old `url IS NULL OR url = ''` query: also catches
    '[not found]' and the other sentinels that stranded posts in `failed`.
    Excludes `dead` rows — those are permanent tombstones (including orphans
    already superseded by a re-key) and must never be re-processed.
    """
    con = sqlite3.connect(db_path)
    con.row_factory = sqlite3.Row
    try:
        rows = con.execute(
            f"""SELECT id, date, author, handle, subject, url, enrichment_status
                FROM posts
                WHERE {_sentinel_sql('url')}
                  AND COALESCE(enrichment_status, '') != 'dead'
                ORDER BY date DESC""",
            tuple(sorted(MISSING_URL_SENTINELS)),
        ).fetchall()
        return [dict(r) for r in rows]
    finally:
        con.close()


def rekey_post(conn: sqlite3.Connection, old_id: int, new_url: str) -> int:
    """Set a post's real URL and migrate it onto the correct deterministic id.

    Must be called inside an open transaction / writer lock. Returns the new id
    (== old id if the URL already hashed/resolved to the same value).

    Raises ValueError if `new_url` is missing/placeholder, or if the canonical
    id already exists on a *different* row (a merge — left for the caller/human
    to resolve so we never silently clobber real data).
    """
    if is_missing_url(new_url):
        raise ValueError(f"rekey_post needs a real URL, got {new_url!r}")

    url = normalize_url(new_url)
    new_id = generate_id(url)

    if new_id == old_id:
        conn.execute(
            "UPDATE posts SET url = ?, updated_at = datetime('now') WHERE id = ?",
            (url, old_id),
        )
        _rebuild_fts(conn)
        return new_id

    clash = conn.execute("SELECT 1 FROM posts WHERE id = ?", (new_id,)).fetchone()
    if clash:
        raise ValueError(
            f"canonical id {new_id} for {url} already exists — this is a merge, "
            f"not a re-key; resolve manually (old orphan id {old_id})."
        )

    # Move foreign-key rows first, then the post row itself.
    for table in _POST_FK_TABLES:
        if _table_exists(conn, table):
            conn.execute(
                f"UPDATE OR IGNORE {table} SET post_id = ? WHERE post_id = ?",
                (new_id, old_id),
            )
            conn.execute(f"DELETE FROM {table} WHERE post_id = ?", (old_id,))
    if _table_exists(conn, "post_relations"):
        conn.execute(
            "UPDATE OR IGNORE post_relations SET post_id_a = ? WHERE post_id_a = ?",
            (new_id, old_id))
        conn.execute(
            "UPDATE OR IGNORE post_relations SET post_id_b = ? WHERE post_id_b = ?",
            (new_id, old_id))
        conn.execute(
            "DELETE FROM post_relations WHERE post_id_a = ? OR post_id_b = ?",
            (old_id, old_id))

    conn.execute(
        "UPDATE posts SET id = ?, url = ?, updated_at = datetime('now') WHERE id = ?",
        (new_id, url, old_id),
    )
    _rebuild_fts(conn)
    return new_id


def backfill_and_rekey(old_id: int, new_url: str,
                       db_path: Path = DEFAULT_DB,
                       with_lock: bool = True) -> int:
    """Convenience wrapper: acquire the writer lock and re-key one post."""
    import contextlib
    lock_cm = _writer_lock() if with_lock else contextlib.nullcontext()
    with lock_cm:
        con = sqlite3.connect(db_path)
        try:
            con.execute("BEGIN")
            new_id = rekey_post(con, old_id, new_url)
            con.commit()
            return new_id
        except Exception:
            con.rollback()
            raise
        finally:
            con.close()


def _writer_lock():
    from db.lock import writer_lock
    return writer_lock(timeout=60)


def _table_exists(conn: sqlite3.Connection, name: str) -> bool:
    return conn.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name = ?", (name,)
    ).fetchone() is not None


def _rebuild_fts(conn: sqlite3.Connection) -> None:
    """Rebuild the external-content FTS index (no triggers keep it in sync)."""
    try:
        conn.execute("INSERT INTO posts_fts(posts_fts) VALUES('rebuild')")
    except sqlite3.Error:
        pass  # FTS optional; rebuild.py / migrate.py own full population


if __name__ == "__main__":
    import json
    cands = url_backfill_candidates()
    print(f"{len(cands)} post(s) need URL backfill:")
    print(json.dumps(cands, indent=2, default=str))
