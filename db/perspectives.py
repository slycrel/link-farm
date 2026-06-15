#!/usr/bin/env python3
"""
Perspective lens layer for the ai-links collection.

Layer 3 of CURATION_DESIGN.md. The composition-not-inheritance shape:
`post_perspectives` is an overlay over `posts.priority`. A post can carry
a different priority under different lenses (`tool-eval`, `theme`, `routing`,
`strategy`, `zeitgeist`, ...). Reads go through `get_effective_priority(...)`,
which honors the lens row first and falls back to `posts.priority`.

After migration 7, `posts.priority` is read-only — all priority writes go
to `post_perspectives` rows. This module is the only sanctioned writer for
that table; never INSERT/UPDATE directly elsewhere.

Lens vocabulary (starter set, expected to drift):

    tool-eval  — "is this a concrete tool/technique I should evaluate this week?"
    theme      — "what concept is this part of?"
    routing    — "who on my team should see this?"
    strategy   — "what does this say about where the industry is going?"
    zeitgeist  — "what's the field talking about right now?"
    morning    — special, computed surface; not a hand-tagged lens

Usage:

    from db.perspectives import get_effective_priority, set_priority
    eff = get_effective_priority(post_id, lens='tool-eval')  # 'now' | 'near-term' | 'long-term' | None
    set_priority(post_id, 'tool-eval', 'now', notes='shipping tool')
"""

import argparse
import sqlite3
from pathlib import Path
from contextlib import contextmanager
from typing import Optional

try:
    from .lock import writer_lock
except ImportError:
    import sys as _sys
    _sys.path.insert(0, str(Path(__file__).parent))
    from lock import writer_lock

SCRIPT_DIR = Path(__file__).parent
DEFAULT_DB = SCRIPT_DIR / "ai_links.db"

# Default lens used for the lens-agnostic priority answer. Backfilled in
# migration 7 from `posts.priority`. New posts that haven't been enriched
# yet have no perspective row; reads fall back to `posts.priority`.
DEFAULT_LENS = "tool-eval"

# Lenses the system understands. Adding a new one is a config change here
# (plus seeding rows for posts that should carry it).
KNOWN_LENSES = (
    "tool-eval",
    "theme",
    "routing",
    "strategy",
    "zeitgeist",
)

# Special lens: not a hand-tagged lens, computed by rebuild.py from other lenses
# + concept activity. Don't write rows under this lens.
COMPUTED_LENSES = ("morning",)

VALID_PRIORITIES = ("now", "near-term", "long-term")


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
        with writer_lock(timeout=60):
            yield
    else:
        yield


# ---- Read path --------------------------------------------------------

def get_effective_priority(post_id: int,
                            lens: str = DEFAULT_LENS,
                            db_path: Path = DEFAULT_DB) -> Optional[str]:
    """Return the effective priority for a post under the given lens.

    Lookup order:
      1. `post_perspectives` row for (post_id, lens) — the authoritative source
      2. For lens == DEFAULT_LENS only: fall back to `posts.priority` (the
         legacy column the backfill migrated into tool-eval rows).
      3. For other lenses: return None — a post without a row in a given
         lens has no priority under that lens. Conflating them would defeat
         the point of having multiple lenses.

    Returns None if no value is found.
    """
    with _connect(db_path) as conn:
        row = conn.execute(
            "SELECT priority FROM post_perspectives WHERE post_id=? AND lens=?",
            (post_id, lens),
        ).fetchone()
        if row and row[0]:
            return row[0]
        if lens != DEFAULT_LENS:
            return None
        # Legacy fallback only applies to the default lens.
        row = conn.execute("SELECT priority FROM posts WHERE id=?", (post_id,)).fetchone()
        return row[0] if row and row[0] else None


def get_perspectives_for_post(post_id: int,
                               db_path: Path = DEFAULT_DB) -> list[dict]:
    """All lens rows for a post, ordered by lens name. Excludes the legacy
    `posts.priority` fallback — call `get_effective_priority` if you need it."""
    with _connect(db_path) as conn:
        rows = conn.execute("""
            SELECT lens, priority, notes, updated_at
              FROM post_perspectives
             WHERE post_id = ?
             ORDER BY lens
        """, (post_id,)).fetchall()
    return [dict(r) for r in rows]


def load_priorities_by_lens(lens: str = DEFAULT_LENS,
                             db_path: Path = DEFAULT_DB) -> dict[int, str]:
    """Return {post_id: effective_priority} for every post, under the given lens.

    Used by rebuild.py to avoid N+1 queries when computing the morning view
    and JSON export. Mirrors `get_effective_priority`'s fallback rule:
    posts.priority is consulted only when lens == DEFAULT_LENS.
    """
    if lens == DEFAULT_LENS:
        sql = """
            SELECT p.id,
                   COALESCE(pp.priority, p.priority) AS effective_priority
              FROM posts p
              LEFT JOIN post_perspectives pp
                     ON pp.post_id = p.id AND pp.lens = ?
        """
    else:
        # Only return entries for posts that actually have a row under this lens.
        sql = """
            SELECT post_id, priority
              FROM post_perspectives
             WHERE lens = ? AND priority IS NOT NULL
        """
    with _connect(db_path) as conn:
        rows = conn.execute(sql, (lens,)).fetchall()
    return {r[0]: r[1] for r in rows if r[1]}


def list_active_lenses(db_path: Path = DEFAULT_DB) -> list[dict]:
    """Distinct lens values currently in use, with counts."""
    with _connect(db_path) as conn:
        rows = conn.execute("""
            SELECT lens, COUNT(*) AS posts_with_row,
                   SUM(CASE WHEN priority IS NOT NULL THEN 1 ELSE 0 END) AS posts_with_priority
              FROM post_perspectives
             GROUP BY lens
             ORDER BY posts_with_row DESC
        """).fetchall()
    return [dict(r) for r in rows]


# ---- Write path -------------------------------------------------------

def set_priority(post_id: int, lens: str, priority: Optional[str],
                  notes: Optional[str] = None,
                  db_path: Path = DEFAULT_DB,
                  with_lock: bool = True) -> None:
    """Upsert a perspective row for (post_id, lens).

    Passing `priority=None` clears the priority for that lens (the row stays;
    set_priority is the only way to add notes for a lens without a priority).
    """
    if lens in COMPUTED_LENSES:
        raise ValueError(f"Lens '{lens}' is computed — don't write to it directly")
    if priority is not None and priority not in VALID_PRIORITIES:
        raise ValueError(f"priority {priority!r} not in {VALID_PRIORITIES}")
    with _maybe_lock(with_lock), _connect(db_path) as conn:
        conn.execute("""
            INSERT INTO post_perspectives (post_id, lens, priority, notes, updated_at)
            VALUES (?, ?, ?, ?, datetime('now'))
            ON CONFLICT(post_id, lens) DO UPDATE SET
                priority   = excluded.priority,
                notes      = COALESCE(excluded.notes, post_perspectives.notes),
                updated_at = excluded.updated_at
        """, (post_id, lens, priority, notes))
        conn.commit()


def clear_perspective(post_id: int, lens: str,
                       db_path: Path = DEFAULT_DB,
                       with_lock: bool = True) -> None:
    """Delete a perspective row entirely. Read path falls back to `posts.priority`
    after this."""
    with _maybe_lock(with_lock), _connect(db_path) as conn:
        conn.execute(
            "DELETE FROM post_perspectives WHERE post_id=? AND lens=?",
            (post_id, lens),
        )
        conn.commit()


# ---- CLI --------------------------------------------------------------

def _cmd_lenses(args):
    rows = list_active_lenses(args.db)
    if not rows:
        print("No perspective rows.")
        return
    print(f"{'lens':15s}  {'rows':>6s}  {'with priority':>14s}")
    print('-' * 40)
    for r in rows:
        print(f"  {r['lens']:13s}  {r['posts_with_row']:>6d}  {r['posts_with_priority']:>14d}")


def _cmd_show(args):
    eff = get_effective_priority(args.post_id, args.lens, args.db)
    rows = get_perspectives_for_post(args.post_id, args.db)
    print(f"Post {args.post_id}:")
    print(f"  effective priority ({args.lens}): {eff}")
    print(f"  perspective rows: {len(rows)}")
    for r in rows:
        print(f"    {r['lens']:12s}  priority={r['priority']}  notes={r['notes'] or ''}")


def _cmd_set(args):
    set_priority(args.post_id, args.lens, args.priority, notes=args.notes,
                  db_path=args.db)
    print(f"Set post {args.post_id} lens={args.lens} priority={args.priority}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", type=Path, default=DEFAULT_DB)
    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("lenses").set_defaults(func=_cmd_lenses)

    p = sub.add_parser("show")
    p.add_argument("post_id", type=int)
    p.add_argument("--lens", default=DEFAULT_LENS)
    p.set_defaults(func=_cmd_show)

    p = sub.add_parser("set")
    p.add_argument("post_id", type=int)
    p.add_argument("lens")
    p.add_argument("priority", choices=list(VALID_PRIORITIES) + [""])
    p.add_argument("--notes", default=None)
    p.set_defaults(func=_cmd_set)

    args = parser.parse_args()
    if not getattr(args, "func", None):
        parser.print_help()
        return
    args.func(args)


if __name__ == "__main__":
    main()
