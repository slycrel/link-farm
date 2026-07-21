#!/usr/bin/env python3
"""
Subject-flag extraction for the ai-links collection.

Jeremy emails himself links from his phone. The default subject shape is
"Post by {Author} on X". Sometimes he edits the subject to flag importance or
intent — almost always as a trailing parenthetical, e.g.:

    "Post by ℏεsam on X (read for work)"
    "Post by Nyk on X (note as urgent for orchestration)"
    "Post by Shenyang Deng on X (please read)"

That parenthetical is an editorial signal worth preserving in a searchable
field. The raw subject already lives in `posts.subject`, but it's buried in a
noisy string. This module lifts the flag out and mirrors it into `posts.notes`
so it can be searched, filtered, and surfaced alongside other curation notes.

Design:
  - Only the trailing parenthetical after "... on X" is treated as a flag.
    Fully custom subjects (e.g. "Local code review", "RAG with Llama") are
    left alone — those are Jeremy's own titling, not importance flags, and
    they remain preserved in `posts.subject`.
  - Flags are stored in `notes` with a "flag: " prefix so they are easy to
    grep for and easy to keep idempotent.
  - Existing curation notes are never clobbered — a new flag is appended with
    a " | " separator, and re-running is a no-op once the flag is present.

`notes` is not part of the restricted enrichment column set (enriched /
content / summary), so writing to it directly here is fine; we still take the
writer lock like every other writer.

CLI:
    python3 -m db.subject_flags            # apply flags across the corpus
    python3 -m db.subject_flags --dry-run  # show what would change
"""

import argparse
import re
import sqlite3
from pathlib import Path

try:
    from .lock import writer_lock
except ImportError:
    import sys as _sys
    _sys.path.insert(0, str(Path(__file__).parent))
    from lock import writer_lock

SCRIPT_DIR = Path(__file__).parent
DEFAULT_DB = SCRIPT_DIR / "ai_links.db"

FLAG_PREFIX = "flag: "

# "Post by <anything> on X (<flag>)" — capture the trailing parenthetical only.
# Tolerates trailing whitespace and a trailing period after the closing paren.
_FLAG_RE = re.compile(r"^Post by .+ on X\s*\((?P<flag>.+)\)\s*\.?\s*$", re.IGNORECASE)


def derive_subject_flag(subject: str | None) -> str | None:
    """Return the trailing-parenthetical importance flag from a subject, or None.

    Only matches the canonical "Post by ... on X (flag)" shape. Custom subjects
    without that shape return None by design (see module docstring).
    """
    if not subject:
        return None
    m = _FLAG_RE.match(subject.strip())
    if not m:
        return None
    flag = m.group("flag").strip()
    return flag or None


def _merge_flag_into_notes(notes: str | None, flag: str) -> str | None:
    """Return updated notes with `flag: <flag>` present, or None if no change.

    Idempotent: if the exact flag fragment is already present (case-insensitive),
    returns None so the caller can skip the write.
    """
    fragment = f"{FLAG_PREFIX}{flag}"
    existing = (notes or "").strip()
    if fragment.lower() in existing.lower():
        return None
    if not existing:
        return fragment
    return f"{existing} | {fragment}"


def apply_subject_flags(*,
                        db_path: Path = DEFAULT_DB,
                        with_lock: bool = True,
                        dry_run: bool = False,
                        progress: bool = False) -> dict:
    """Mirror trailing-parenthetical subject flags into `posts.notes`.

    Idempotent and non-destructive: existing notes are preserved, and a flag
    already captured is left untouched. Returns per-run stats.
    """
    result = {"scanned": 0, "flagged": 0, "updated": 0, "already_present": 0, "changes": []}

    def _run(conn):
        rows = conn.execute(
            "SELECT id, subject, notes FROM posts WHERE subject IS NOT NULL"
        ).fetchall()
        result["scanned"] = len(rows)
        for pid, subject, notes in rows:
            flag = derive_subject_flag(subject)
            if not flag:
                continue
            result["flagged"] += 1
            new_notes = _merge_flag_into_notes(notes, flag)
            if new_notes is None:
                result["already_present"] += 1
                continue
            result["updated"] += 1
            result["changes"].append({"id": pid, "flag": flag, "notes": new_notes})
            if not dry_run:
                conn.execute(
                    "UPDATE posts SET notes = ?, updated_at = datetime('now') WHERE id = ?",
                    (new_notes, pid),
                )
        if not dry_run:
            conn.commit()

    if with_lock and not dry_run:
        with writer_lock(timeout=120):
            conn = sqlite3.connect(db_path)
            try:
                _run(conn)
            finally:
                conn.close()
    else:
        conn = sqlite3.connect(db_path)
        try:
            _run(conn)
        finally:
            conn.close()

    if progress:
        verb = "would update" if dry_run else "updated"
        print(f"[subject_flags] scanned {result['scanned']}, "
              f"{result['flagged']} flagged, {verb} {result['updated']}, "
              f"{result['already_present']} already present")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--db", type=Path, default=DEFAULT_DB)
    parser.add_argument("--dry-run", action="store_true",
                        help="show what would change without writing")
    args = parser.parse_args()

    res = apply_subject_flags(db_path=args.db, dry_run=args.dry_run, progress=True)
    if args.dry_run and res["changes"]:
        print()
        for ch in res["changes"]:
            print(f"  [{ch['id']}] flag={ch['flag']!r}")
            print(f"        notes -> {ch['notes']!r}")


if __name__ == "__main__":
    main()
