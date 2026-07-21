#!/usr/bin/env python3
"""
Shared post-enrichment pipeline for the ai-links collection.

The daily sync skill and the catch-up skill have different work-sources
(new Outlook emails vs the partial/failed/unattempted queue) but the work
that happens *after* enrichment is identical: re-embed anything that changed
content, run mechanical + semantic discovery to grow the concept graph, then
rebuild outputs.

This module is that shared tail. Both skills call `post_enrichment_pipeline()`
at the end of their enrichment loop and get a consistent experience.

It's intentionally a thin orchestrator — every step delegates to a more
specialized module (`db.embeddings`, `db.concepts`, `db.rebuild`). The value
is keeping the order, the lock discipline, and the reporting shape uniform.

Usage (inside a skill that already holds the writer lock):

    from db.pipeline import post_enrichment_pipeline
    result = post_enrichment_pipeline(with_lock=False)
    print(result['summary'])

Standalone (e.g., manual catch-up rerun):

    python3 -m db.pipeline
"""

import argparse
import datetime
from pathlib import Path
from contextlib import contextmanager

try:
    from .lock import writer_lock
except ImportError:
    import sys as _sys
    _sys.path.insert(0, str(Path(__file__).parent))
    from lock import writer_lock

SCRIPT_DIR = Path(__file__).parent
DEFAULT_DB = SCRIPT_DIR / "ai_links.db"


@contextmanager
def _maybe_lock(with_lock: bool):
    if with_lock:
        with writer_lock(timeout=120):
            yield
    else:
        yield


def post_enrichment_pipeline(*,
                              db_path: Path = DEFAULT_DB,
                              with_lock: bool = True,
                              subject_flags: bool = True,
                              embed: bool = True,
                              mechanical_discovery: bool = True,
                              semantic_discovery: bool = True,
                              auto_curate: bool = True,
                              rebuild_outputs: bool = True,
                              progress: bool = True) -> dict:
    """Run every post-enrichment step that should happen after either a
    daily sync or a catch-up run.

    Steps (each independently skippable):
        0. Mirror trailing-parenthetical subject flags into notes.
        1. Embed any post whose embedding is missing or stale.
        2. Run mechanical discovery (shared external URLs, shared mentions).
        3. Run semantic discovery (concept-centroid matching).
        3.5 Auto-curate: conservative conceptual-preference triage of pending
            observations (promote high-confidence conceptual matches, dismiss
            low-signal mechanical/per-person duplicates, leave the rest).
        4. Rebuild outputs (JSON / HTML / Markdown).

    Each step is a no-op when there's nothing to do. The pipeline is
    idempotent — running it twice in a row produces the same final state
    as running it once.

    Returns a dict with per-step stats and a `summary` string suitable for
    pasting into the skill's report.
    """
    result = {
        "started_at": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "subject_flags": None,
        "embed": None,
        "mechanical": None,
        "semantic": None,
        "auto_curate": None,
        "rebuild": None,
        "split_candidates": None,
        "errors": [],
    }

    with _maybe_lock(with_lock):

        # Step 0: mirror trailing-parenthetical subject flags into notes.
        # Runs before rebuild so newly-captured flags land in the outputs.
        if subject_flags:
            try:
                try:
                    from .subject_flags import apply_subject_flags
                except ImportError:
                    import sys as _sys
                    _sys.path.insert(0, str(Path(__file__).parent))
                    from subject_flags import apply_subject_flags
                if progress:
                    print("[pipeline] subject flags…")
                result["subject_flags"] = apply_subject_flags(
                    db_path=db_path, with_lock=False, progress=progress,
                )
            except Exception as e:
                result["errors"].append(f"subject_flags: {e}")
                if progress:
                    print(f"[pipeline] subject_flags FAILED: {e}")

        # Step 1: embeddings
        if embed:
            try:
                # Lazy import — surfacing a clean error if fastembed isn't installed
                try:
                    from .embeddings import embed_corpus
                except ImportError:
                    import sys as _sys
                    _sys.path.insert(0, str(Path(__file__).parent))
                    from embeddings import embed_corpus
                if progress:
                    print("[pipeline] embedding…")
                result["embed"] = embed_corpus(
                    db_path=db_path, with_lock=False, progress=progress,
                )
            except Exception as e:
                result["errors"].append(f"embed: {e}")
                if progress:
                    print(f"[pipeline] embed FAILED: {e}")

        # Step 2: mechanical discovery
        if mechanical_discovery:
            try:
                try:
                    from .concepts import run_all_mechanical_passes
                except ImportError:
                    import sys as _sys
                    _sys.path.insert(0, str(Path(__file__).parent))
                    from concepts import run_all_mechanical_passes
                if progress:
                    print("[pipeline] mechanical discovery…")
                result["mechanical"] = run_all_mechanical_passes(
                    db_path=db_path, with_lock=False,
                )
            except Exception as e:
                result["errors"].append(f"mechanical: {e}")
                if progress:
                    print(f"[pipeline] mechanical FAILED: {e}")

        # Step 3: semantic discovery (depends on embeddings being current —
        # the embed step above ensures that)
        if semantic_discovery:
            try:
                try:
                    from .concepts import discover_semantic_neighbors
                except ImportError:
                    import sys as _sys
                    _sys.path.insert(0, str(Path(__file__).parent))
                    from concepts import discover_semantic_neighbors
                if progress:
                    print("[pipeline] semantic discovery…")
                result["semantic"] = discover_semantic_neighbors(
                    db_path=db_path, with_lock=False,
                )
            except Exception as e:
                result["errors"].append(f"semantic: {e}")
                if progress:
                    print(f"[pipeline] semantic FAILED: {e}")

        # Step 3.5: auto-curation (acts on observations discovery just produced).
        # Conservative, conceptual-preference triage — see db.concepts.auto_curate.
        if auto_curate:
            try:
                try:
                    from .concepts import auto_curate as _auto_curate
                except ImportError:
                    import sys as _sys
                    _sys.path.insert(0, str(Path(__file__).parent))
                    from concepts import auto_curate as _auto_curate
                if progress:
                    print("[pipeline] auto-curate…")
                result["auto_curate"] = _auto_curate(
                    db_path=db_path, with_lock=False, progress=progress,
                )
            except Exception as e:
                result["errors"].append(f"auto_curate: {e}")
                if progress:
                    print(f"[pipeline] auto_curate FAILED: {e}")

        # Step 4: rebuild outputs
        if rebuild_outputs:
            try:
                try:
                    from .rebuild import rebuild
                except ImportError:
                    import sys as _sys
                    _sys.path.insert(0, str(Path(__file__).parent))
                    from rebuild import rebuild
                if progress:
                    print("[pipeline] rebuild…")
                posts = rebuild(db_path=db_path, with_lock=False)
                result["rebuild"] = {"posts": len(posts) if posts else 0}
            except Exception as e:
                result["errors"].append(f"rebuild: {e}")
                if progress:
                    print(f"[pipeline] rebuild FAILED: {e}")

        # Advisory: flag oversized concepts as split-review candidates.
        # Read-only — never mutates; just surfaces buckets worth vetting.
        try:
            try:
                from .concepts import split_candidates
            except ImportError:
                import sys as _sys
                _sys.path.insert(0, str(Path(__file__).parent))
                from concepts import split_candidates
            result["split_candidates"] = split_candidates(db_path=db_path)
        except Exception as e:
            result["errors"].append(f"split_candidates: {e}")

    result["finished_at"] = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    result["summary"] = _format_summary(result)
    return result


def _format_summary(result: dict) -> str:
    """Compact summary line suitable for the skill's end-of-run report."""
    parts = []
    if result.get("subject_flags"):
        f = result["subject_flags"]
        parts.append(f"flags: +{f.get('updated', 0)} ({f.get('flagged', 0)} flagged, {f.get('already_present', 0)} already present)")
    if result.get("embed"):
        s = result["embed"]
        parts.append(f"embed: +{s.get('embedded', 0)} ({s.get('skipped_unchanged', 0)} unchanged, {s.get('errors', 0)} errors)")
    if result.get("mechanical"):
        m = result["mechanical"]
        urls = m.get("shared_external_urls", {})
        mentions = m.get("shared_mentions", {})
        parts.append(
            f"mechanical: urls(+{urls.get('observations_created', 0)} obs / +{urls.get('concepts_created', 0)} concepts), "
            f"mentions(+{mentions.get('observations_created', 0)} obs / +{mentions.get('concepts_created', 0)} concepts)"
        )
    if result.get("semantic"):
        s = result["semantic"]
        if "error" in s:
            parts.append(f"semantic: skipped ({s['error']})")
        else:
            parts.append(f"semantic: {s.get('concepts_considered', 0)} concepts × {s.get('posts_considered', 0)} posts → +{s.get('observations_created', 0)} obs")
    if result.get("auto_curate"):
        a = result["auto_curate"]
        parts.append(f"auto-curate: +{a.get('promoted', 0)} promoted / -{a.get('dismissed', 0)} dismissed ({a.get('left_pending', 0)} left)")
    if result.get("rebuild"):
        parts.append(f"rebuild: {result['rebuild'].get('posts', 0)} posts → JSON/HTML/MD")
    if result.get("split_candidates"):
        cands = ", ".join(f"#{c['id']} '{c['name'][:32]}' ({c['post_count']})"
                          for c in result["split_candidates"])
        parts.append(f"⚑ split-review candidates: {cands}")
    if result.get("errors"):
        parts.append(f"errors: {len(result['errors'])}")
    return " | ".join(parts) if parts else "(no work)"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", type=Path, default=DEFAULT_DB)
    parser.add_argument("--no-subject-flags", dest="subject_flags", action="store_false")
    parser.add_argument("--no-embed", dest="embed", action="store_false")
    parser.add_argument("--no-mechanical", dest="mechanical", action="store_false")
    parser.add_argument("--no-semantic", dest="semantic", action="store_false")
    parser.add_argument("--no-auto-curate", dest="auto_curate", action="store_false")
    parser.add_argument("--no-rebuild", dest="rebuild", action="store_false")
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    result = post_enrichment_pipeline(
        db_path=args.db,
        subject_flags=args.subject_flags,
        embed=args.embed,
        mechanical_discovery=args.mechanical,
        semantic_discovery=args.semantic,
        auto_curate=args.auto_curate,
        rebuild_outputs=args.rebuild,
        progress=not args.quiet,
    )
    print()
    print("Pipeline summary:")
    print(f"  {result['summary']}")
    if result.get("errors"):
        print()
        print("Errors:")
        for e in result["errors"]:
            print(f"  - {e}")


if __name__ == "__main__":
    main()
