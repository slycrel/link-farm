#!/usr/bin/env python3
"""Revive historically-dismissed observations as labelled `weak` edges.

Background (Jeremy, Aug 2026)
-----------------------------
`auto_curate()` used to dismiss two large buckets outright: the sub-threshold
semantic "recall band" (cosine below `AUTO_PROMOTE_MIN_COSINE`), and raw
mechanical `mention:` / `url:` groupings. Two July hand-curation passes did the
same thing at larger scale. Net effect: ~1,900 observations were thrown away on
a "low signal" judgement, and nothing downstream could ever reconsider them.

That bar was too low for this corpus. Every post here is something Jeremy chose
to send himself, so a match the 0.82 floor can't *confirm* is usually a real
association rather than noise. Measured bias: `adjacent`-tagged posts were
~1.6x more likely than baseline to end up with no concept edge at all — the
triage was cutting hardest against exactly the tangential material the taxonomy
had been extended to capture. It also left 20 `url:`/`mention:` concepts as
empty shells, created by discovery and then stripped of every observation.

What this script does
---------------------
Re-attaches those dismissed observations as `post_concepts` edges carrying a
non-canonical role, so they are findable and upgradeable but cannot vote on
what a concept means:

  * mechanical `url:` groupings  → `evidence` (shared external URL is concrete
    co-citation: two posts citing the same repo really are about the same thing)
  * mechanical `mention:` groupings → `weak` (a shared @handle is much looser,
    and per-person grouping is deprioritised by standing preference)
  * everything else (semantic recall band, non-conceptual duplicates) → `weak`

Safety properties
-----------------
  * Additive only. Never deletes, never downgrades: `promote_observation()` uses
    INSERT OR IGNORE, so an existing `evidence` edge is left untouched.
  * Skips observations on archived / merged-into concepts — reviving an edge to
    a retired concept would resurrect structure that was deliberately retired.
  * Idempotent. Reviving flips observation status `dismissed` → `promoted`, so a
    second run finds nothing. `--dry-run` reports without writing.
  * Depends on the role-aware filters in `concept_centroids()`,
    `assign_primaries()`, `discover_semantic()` and `discover_orphan_clusters()`.
    Running this against a build that lacks them WILL corrupt centroids —
    `--check-guards` verifies they are present and aborts if not.

Usage
-----
    python3 -m db.revive_dismissed --dry-run
    python3 -m db.revive_dismissed
    python3 -m db.revive_dismissed --only-auto-curate   # machine-made only
"""
from __future__ import annotations

import argparse
import sqlite3
import sys
from pathlib import Path

try:
    from .concepts import (ROLE_EVIDENCE, ROLE_WEAK, CANONICAL_ROLES,
                           promote_observation, CONCEPT_ACTIVE)
    from .lock import writer_lock
except ImportError:  # direct-script invocation
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from db.concepts import (ROLE_EVIDENCE, ROLE_WEAK, CANONICAL_ROLES,
                             promote_observation, CONCEPT_ACTIVE)
    from db.lock import writer_lock

DEFAULT_DB = Path(__file__).parent / "ai_links.db"

# Dismissal-note prefixes written by the unattended pass, as opposed to the
# July hand passes. `--only-auto-curate` restricts to these.
AUTO_CURATE_MARKERS = ("auto-curate:",)


def _check_guards() -> list[str]:
    """Verify the role-aware filters are in place before we write weak edges."""
    problems = []
    here = Path(__file__).parent
    emb = (here / "embeddings.py").read_text()
    con = (here / "concepts.py").read_text()
    if "pc.role IN ('evidence', 'origin')" not in emb:
        problems.append("embeddings.concept_centroids() is not role-filtered")
    if "ROLE_WEAK" not in con:
        problems.append("concepts.ROLE_WEAK missing")
    if "CANONICAL_ROLES" not in con:
        problems.append("concepts.CANONICAL_ROLES missing")
    return problems


def revive(*, db_path: Path = DEFAULT_DB, dry_run: bool = False,
           only_auto_curate: bool = False, check_guards: bool = True,
           progress: bool = True) -> dict:
    if check_guards:
        problems = _check_guards()
        if problems:
            raise RuntimeError(
                "refusing to revive: role-aware guards missing — "
                + "; ".join(problems))

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    rows = conn.execute("""
        SELECT o.id, o.post_id, o.concept_id, o.source, o.raw_score, o.notes,
               c.name AS cname, c.status AS cstatus
          FROM concept_observations o
          JOIN concepts c ON c.id = o.concept_id
         WHERE o.status = 'dismissed'
         ORDER BY o.id
    """).fetchall()

    result = {"examined": len(rows), "evidence": 0, "weak": 0,
              "skipped_retired_concept": 0, "skipped_not_auto_curate": 0,
              "skipped_edge_exists": 0}

    existing = {(r["post_id"], r["concept_id"]) for r in
                conn.execute("SELECT post_id, concept_id FROM post_concepts")}
    conn.close()

    plan: list[tuple[int, str, str]] = []
    for o in rows:
        if o["cstatus"] != CONCEPT_ACTIVE:
            result["skipped_retired_concept"] += 1
            continue
        note = o["notes"] or ""
        if only_auto_curate and not note.startswith(AUTO_CURATE_MARKERS):
            result["skipped_not_auto_curate"] += 1
            continue
        if (o["post_id"], o["concept_id"]) in existing:
            # Already attached by some other path — nothing to add. (The
            # observation status stays 'dismissed', which is accurate: this
            # particular observation wasn't what created the edge.)
            result["skipped_edge_exists"] += 1
            continue

        name = o["cname"] or ""
        if o["source"] == "mechanical" and name.startswith("url:"):
            role = ROLE_EVIDENCE
            why = "revived 2026-08-24: shared external URL (co-citation)"
        elif o["source"] == "mechanical" and name.startswith("mention:"):
            role = ROLE_WEAK
            why = "revived 2026-08-24: shared @mention, loose per-person signal"
        else:
            score = o["raw_score"]
            score_s = f", cosine {score:.3f}" if isinstance(score, float) else ""
            role = ROLE_WEAK
            why = (f"revived 2026-08-24: previously dismissed as low-signal"
                   f"{score_s} — association recorded, not load-bearing")
        plan.append((o["id"], role, why))
        result["evidence" if role == ROLE_EVIDENCE else "weak"] += 1

    if dry_run:
        result["dry_run"] = True
        if progress:
            _report(result)
        return result

    with writer_lock(timeout=180):
        for oid, role, why in plan:
            promote_observation(oid, role=role, notes=why,
                                db_path=db_path, with_lock=False)
    if progress:
        _report(result)
    return result


def _report(r: dict) -> None:
    tag = "[revive DRY RUN]" if r.get("dry_run") else "[revive]"
    print(f"{tag} examined {r['examined']} dismissed observations → "
          f"{r['evidence']} evidence + {r['weak']} weak "
          f"({r['skipped_retired_concept']} on retired concepts, "
          f"{r['skipped_edge_exists']} already attached, "
          f"{r['skipped_not_auto_curate']} not auto-curate)")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--db", type=Path, default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--only-auto-curate", action="store_true",
                    help="restrict to machine-made dismissals (skip July hand passes)")
    ap.add_argument("--no-check-guards", action="store_true",
                    help="skip the role-aware-filter precondition check (unsafe)")
    a = ap.parse_args(argv)
    revive(db_path=a.db, dry_run=a.dry_run, only_auto_curate=a.only_auto_curate,
           check_guards=not a.no_check_guards)


if __name__ == "__main__":
    main()
