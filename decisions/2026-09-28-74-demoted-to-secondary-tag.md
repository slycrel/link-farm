# 2026-09-28 — #74 demoted to a secondary-only grouping tag

**Decision (Jeremy, in-session).** Demote concept #74 *System One models — bounded
decisions as a primitive* from a primary home to a **secondary-only grouping tag**,
and let the theme re-seed its own home organically.

## What prompted it

The 2026-09-28 sync imported 24 posts, **ten of them squarely about Jev** — TypeSafe
AI's non-generative decision model. #74 was hand-seeded on 2026-09-24 for exactly this
conversation. It took **zero** of the ten.

That is a direct consequence of the 2026-09-25 magnet rollback, which applied the
centroid-scoring opt-out marker to #74. The marker works: nothing is matched into a
marked concept by cosine. But the flip side had not been seen before — the *live*
conversation could no longer reach the concept built for it, so orphan clustering
formed a new concept (#77) from the same material. The corpus ended up with two homes
for one idea, and the hand-made one was the one nothing could find.

## Options considered

1. **Merge #77 into #74.** Rejected: it would move the live thread into a concept that
   is permanently unscoreable, guaranteeing the same problem again with the next batch.
2. **Remove the marker from #74.** Rejected: #74 went from 9 seeds to 328 evidence
   edges in 48 hours. The marker is the only thing holding that back.
3. **`status=provisional`.** Rejected on mechanics: the nursery tier auto-graduates at
   `PROVISIONAL_GRADUATION_MIN_EDGES` (4) canonical edges and #74 had 11, so it would
   flip straight back to `active` on the next run.
4. **Demote the canonical edges (chosen).** `assign_primaries` filters on
   `role IN CANONICAL_ROLES`, so demoting `evidence → weak` makes a concept structurally
   ineligible as a home while leaving every edge in place and fully browseable.

## What was done

- Recorded all 11 canonical edges (role + `is_primary`) in `_rollback_74_20260928`.
- `UPDATE post_concepts SET role='weak', is_primary=0` for those 11.
- Rewrote #74's description to say what it now is.
- **No observation was dismissed.** Last dismissal is still 2026-08-26; the no-discard
  policy is intact. This is the same demote-not-dismiss shape as the 09-25 rollback.

## Outcome

| | before | after |
|---|---:|---:|
| #74 canonical / homes | 11 / 11 | **0 / 0** (338 weak) |
| #77 canonical / homes | 6 / 6 | **24 / 19** |

**Ten of the 11 released posts re-homed onto #77 in a single pipeline pass**, at raw
cosines of 0.82–0.91 against its centroid — including the Jev launch announcement, the
CLM mechanism explainer and two model cards, all of which had been stranded at #74. The
eleventh (a Qwen-2.5-1B-RLCD model card, 0.7716) is honestly unhomed and stays visible
to orphan clustering.

#77 at 24 canonical / 19 homes is a ~1.3:1 ratio — the magnet detector needs
`canonical > 40 AND canonical > homes * 10`, so it is not remotely close. Worth
re-checking on the next few runs anyway, since this is the same *kind* of concept that
became a magnet twice; the difference is that #77 was derived from the embedding
geometry and cohesion-guarded, not hand-seeded from a purpose.

## The bug this surfaced

The first attempt produced **zero** re-homing, and the reason is worth keeping. #77's
rewritten description *mentioned* the centroid-scoring opt-out marker in prose, while
explaining that #74 carried it. Eligibility is a plain substring match over the whole
description, so #77 silently excluded **itself** from centroid scoring. The symptom is
quiet: `observations_created: 0` with a plausible-looking `concepts_considered`, while
twelve posts at 0.82–0.91 are never proposed. Never write the marker as a literal string
in a description that is not opting out. See CLAUDE.md for the detector.

## Generalized

**The marker is a terminal state, not a pause.** A marked concept can only lose
relevance over time, because the material that would refresh it accumulates elsewhere.
When marking one, decide whether you are freezing an *archive* or crippling a *home* —
and if it is a live thread, demote it to a secondary tag so a scoreable concept can form.
