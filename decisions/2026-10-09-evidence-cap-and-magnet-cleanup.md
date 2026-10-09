# 2026-10-09 — The evidence cap: clearing all 13 magnets at once

**Decision (Jeremy, 2026-10-09, attended session):** cap semantic evidence
attachment at **3 canonical edges per post** (`SEMANTIC_MAX_EVIDENCE_PER_POST`
in `db/concepts.py`), backfill the existing carpet by demoting each post's
over-cap evidence edges to `weak`, and keep the cap enforced on every future
run. This closes open-work item A (the magnet list), which had been
deliberately deferred since 2026-09-25.

## The problem, quantified

The magnet detector returned **13 hits** on 2026-10-08 — every large concept
in the graph, including #77 *applied decision-model routing*, which had gone
from 24 canonical / 19 homes to **370 canonical / 30 homes in ten days** by
absorbing the Jev conversation. It was the third concept to hold that material
and was repeating the #74 failure on the concept created to replace #74.

Root cause was never the geometry; it was the **uncapped evidence band**.
`SEMANTIC_MAX_WEAK_PER_POST` (3) caps weak edges; nothing capped evidence, so
every ≥0.82 match filed as load-bearing. Measured on 2026-10-08:

- 632 posts with canonical edges carried **6,211** of them — median **12 per
  post**, 201 posts with 15+.
- The seven long-documented magnets shared 82–94% of their members: the same
  posts under seven names.
- 191 of 1,128 centroid pairs sat above 0.99 cosine (16.9%).

## Options weighed

1. **Per-post evidence cap + backfill** (chosen). Fixes the root cause for
   every concept at once; symmetric with the weak cap; preserves the home
   layer by construction.
2. **Per-concept #74-style rollbacks.** Thirteen hand jobs, and new magnets
   keep forming from the same uncapped mechanism.
3. **Mark the magnets `[no-centroid-scoring]`.** Terminal per the #74
   epilogue — wrong for live homes (#77 had 30, #50 had 37).

Cap value was swept before deciding: **3** clears 11/13 magnets in projection
(demoting 4,683 edges); 4 clears 8/13; 5 clears 7/13. The two projected
stragglers (#51, #4) were left for re-measurement rather than hand-treated —
correctly, as it turned out.

## What was done

1. **Backfill.** For each post: keep protected edges (primary, `origin` role,
   and `curated`/`latent`/`cluster`-sourced — human and reader decisions are
   never machine-demoted), then keep its top-(3 − protected) remaining
   evidence edges by cosine to concept centroid; demote the rest to `weak`.
   4,683 edges demoted, **zero dismissed** (no-discard intact), all 630
   primaries untouched. Reversible via `_rollback_evidence_cap_20261009`.
2. **The flaw, found by spot check, and its fix.** The backfill ranked edges
   against the *old, diffuse* centroids — so a post whose true home had a
   drifted centroid could lose exactly that edge (Mark Ajzenstadt's FDE post
   landed in *Claude skills craft* because its #3 edge ranked low against
   #3's bloated centroid). One re-rank iteration against the **post-cap
   sharpened centroids**, selecting from each post's original canonical set,
   swapped 201 edges across 177 posts (rollback table updated to stay
   consistent). Homes re-derived; spot checks then filed correctly.
   **Lesson: a cleanup that changes the geometry must re-rank under the
   geometry it creates, not the one it found.**
3. **Ongoing cap.** Enforced in `auto_curate()`'s semantic-evidence branch:
   per-post TOTAL (counting existing canonical edges from any source),
   best-scored matches win the budget, overflow files as `weak` with an
   explanatory note — recorded, browseable, upgradeable by hand. Exempt:
   exemplar matches (provisional tier is inert and needs evidence to
   graduate) and mechanical `url:` co-citations (concrete and rare).
   Regression coverage: `EvidenceCapIsPerPostTotal` in `db/test_roles.py`
   (4 tests; suite now 37).

## Results

| measure | before | after |
|---|---|---|
| magnet detector hits | 13 | **0** |
| canonical edges | 6,211 | 1,541 |
| weak edges | 2,678 | 7,512 |
| centroid pairs >0.99 | 191/1,128 (16.9%) | **9/1,378 (0.7%)** |
| primary homes | 630 | 632 (necessarily reshuffled: ~190 moved under the sharper leave-one-out centroids) |
| dismissals since 2026-08-26 | 0 | 0 |

First live run of the cap: 32 above-floor matches, 13 filed evidence, 19
capped to weak.

**Filing recalibration** (required after any large re-home): every margin
band improved — 0.00–0.01 survival 32.3% → 48.3%, 0.03–0.05 61.7% → 76.7% —
and at the 80% target `calibrate` now recommends margin **0.00** (83.1% mean
stability over all 468 contested). `ABSTAIN_MARGIN` was left at 0.03 (the
don't-retune-from-a-session rule; lowering it is now a live option for
Jeremy).

## Limits and consequences

- **~190 primary homes moved.** Expected and necessary — the old homes were
  derived from coin-flip rankings against near-identical centroids (the 86%
  sub-0.01-margin finding). Spot checks look right, but this invalidates any
  external reference to a specific post's pre-cap home.
- **Evidence counts are no longer comparable across 2026-10-09**, the same
  way they weren't across the 2026-09-25 #74 rollback. The honest sizes are
  now much smaller everywhere; keep quoting primary-home counts.
- **A post's reachable homes are now its ≤3 best-fit concepts.** A genuinely
  cross-cutting post may have a defensible fourth home it can no longer win.
  The weak layer records those associations and `ai-links-filing`'s abstain
  queue remains the review surface; upgrade by hand where it matters.
- The gold-label plan (item B) is unchanged, but any gold set sampled before
  this date would have measured the old coin-flip homes — sample after.

## Rollback

`_rollback_evidence_cap_20261009` holds every currently-demoted edge with its
original role. To reverse: restore roles from the table, delete the table,
re-run `assign_primaries()` and rebuild. The 201 re-rank swap-ins were
removed from the table when restored, so it is exact.
