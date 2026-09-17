"""Canonical definition of what gets mirrored to the link-farm remote.

Why this file exists
--------------------
The daily sync used to push a hand-written list of filenames. Anything outside
that list -- SETUP.md, README.md, scheduled/, skills/, db/test_*.py,
ARCHITECTURE_PLAN.md -- never reached the remote, and only matched because a
human occasionally pushed it by hand. That is the same silent-drift class that
let the live scheduled task sit on a stale June vintage for weeks.

The fix is to sync by *path pattern* rather than by filename, so a new file
dropped into db/, scheduled/ or skills/ propagates on the next sync with nobody
editing a list. Both the scheduled task and any ad-hoc push import from here, so
there is exactly one definition.

Usage
-----
    from db.repo_sync import mirror_to_clone
    copied = mirror_to_clone(cowork_dir, push_dir)

CLI:
    python3 -m db.repo_sync --check <cowork_dir> <clone_dir>
"""

from __future__ import annotations

import argparse
import fnmatch
import os
import shutil
import sys
from pathlib import Path

# Glob patterns, relative to the repo root. Directory globs are the point:
# they pick up new files automatically.
PUSH_SPEC: tuple[str, ...] = (
    # --- docs -------------------------------------------------------------
    "README.md",
    "CLAUDE.md",
    "SETUP.md",
    "ARCHITECTURE_PLAN.md",
    "CURATION_DESIGN.md",
    "CURATION_REVIEW.md",
    "requirements.txt",
    ".gitignore",
    # --- generated artifacts ---------------------------------------------
    "posts_final_v3.json",
    "ai_links_collection_v3.html",
    "ai_links_collection_v3.md",
    # --- skills -----------------------------------------------------------
    "ai-links-*.SKILL.md",
    "ai-links-catchup/**",
    "skills/**",
    "scheduled/**",
    # --- code + source of truth ------------------------------------------
    "db/*.py",
    "db/ai_links.db",
)

# Excluded even when a pattern above would otherwise match. The token is the
# one that actually matters; the rest is local scratch that would bloat history.
EXCLUDE_SPEC: tuple[str, ...] = (
    ".claude/**",          # GitHub token -- gitignored, must never be pushed
    "**/__pycache__/**",
    "**/*.pyc",
    "*.bak",
    "**/*.bak",
    "db/_*",               # local scratch scripts (_backfill_run.py etc.)
    "**/.fuse_hidden*",    # cowork mount denies unlink; these accumulate
    "**/ai_links.db-wal",  # checkpoint the WAL instead of shipping sidecars
    "**/ai_links.db-shm",
    "**/ai_links.db-journal",
)


def _matches(rel: str, patterns: tuple[str, ...]) -> bool:
    """True if `rel` matches any glob in `patterns`.

    Handles `dir/**` as "anything at or under dir/", which fnmatch does not do
    natively for a single path segment.
    """
    for pat in patterns:
        if fnmatch.fnmatch(rel, pat):
            return True
        if pat.endswith("/**"):
            prefix = pat[:-3]
            if rel == prefix or rel.startswith(prefix + "/"):
                return True
        # allow **/x to match a bare x at the root
        if pat.startswith("**/") and fnmatch.fnmatch(rel, pat[3:]):
            return True
    return False


def is_excluded(rel: str) -> bool:
    return _matches(rel, EXCLUDE_SPEC)


def is_included(rel: str) -> bool:
    return _matches(rel, PUSH_SPEC) and not is_excluded(rel)


def enumerate_files(src_dir: str | Path) -> list[str]:
    """Every repo-relative path under `src_dir` that PUSH_SPEC selects."""
    src = Path(src_dir)
    out: list[str] = []
    for dirpath, dirnames, filenames in os.walk(src):
        rel_dir = os.path.relpath(dirpath, src)
        rel_dir = "" if rel_dir == "." else rel_dir
        # prune obviously-dead directories early (big win on __pycache__ and
        # the .fuse_hidden pile in db/)
        dirnames[:] = [
            d for d in dirnames
            if d not in {".git", "__pycache__", ".deps", ".model-cache", ".claude"}
        ]
        for fn in filenames:
            rel = f"{rel_dir}/{fn}" if rel_dir else fn
            if is_included(rel):
                out.append(rel)
    return sorted(out)


def mirror_to_clone(src_dir: str | Path, dest_dir: str | Path,
                    verbose: bool = False) -> list[str]:
    """Copy every PUSH_SPEC-selected file from `src_dir` into `dest_dir`.

    Creates intermediate directories. Does not delete anything in the clone --
    `git add -A` plus review is the safety net, and an accidental mass-delete
    is far worse than a stale file.
    """
    src, dest = Path(src_dir), Path(dest_dir)
    copied: list[str] = []
    for rel in enumerate_files(src):
        s, d = src / rel, dest / rel
        d.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(s, d)
        copied.append(rel)
        if verbose:
            print(f"  + {rel}")
    return copied


def check(src_dir: str | Path, clone_dir: str | Path) -> dict:
    """Report drift between what PUSH_SPEC selects and what the clone tracks.

    `missing_from_remote` is the one that bites: files the spec covers that the
    remote has never seen.
    """
    src = Path(src_dir)
    selected = set(enumerate_files(src))
    tracked = set()
    clone = Path(clone_dir)
    for dirpath, dirnames, filenames in os.walk(clone):
        dirnames[:] = [d for d in dirnames if d != ".git"]
        rel_dir = os.path.relpath(dirpath, clone)
        rel_dir = "" if rel_dir == "." else rel_dir
        for fn in filenames:
            tracked.add(f"{rel_dir}/{fn}" if rel_dir else fn)
    return {
        "selected": len(selected),
        "tracked_in_clone": len(tracked),
        "missing_from_remote": sorted(selected - tracked),
        "remote_only": sorted(t for t in tracked - selected if not is_excluded(t)),
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", nargs=2, metavar=("SRC", "CLONE"),
                    help="report drift instead of copying")
    ap.add_argument("--list", metavar="SRC", help="list selected files")
    args = ap.parse_args(argv)

    if args.list:
        for rel in enumerate_files(args.list):
            print(rel)
        return 0
    if args.check:
        result = check(*args.check)
        print(f"selected by PUSH_SPEC : {result['selected']}")
        print(f"present in clone      : {result['tracked_in_clone']}")
        if result["missing_from_remote"]:
            print("\nMISSING FROM REMOTE (would silently drift):")
            for r in result["missing_from_remote"]:
                print(f"  ! {r}")
        else:
            print("\nNothing missing from the remote.")
        if result["remote_only"]:
            print("\nIn the remote but not selected locally:")
            for r in result["remote_only"]:
                print(f"  ? {r}")
        return 1 if result["missing_from_remote"] else 0

    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
