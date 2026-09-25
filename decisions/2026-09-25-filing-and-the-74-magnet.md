# 2026-09-25 — The #74 magnet, the marker default, and an abstain-aware filing classifier

**Status:** implemented and pushed (`fc72deb`, `a2a3f27`, `b0f2af2`, `25f58c1`).
**Scope:** `db/concepts.py`, `db/filing.py` (new), `db/test_filing.py` (new), `db/test_roles.py`, `ai-links-filing.SKILL.md` (new), `CLAUDE.md`, `scheduled/ai-links-sync.SKILL.md`.

A record of what changed today and — more importantly — *why*, including the things that were measured and rejected. The running reference is `CLAUDE.md`; this file exists because the reasoning behind a decision compresses away fast once it becomes a one-line rule.

---

## How this started

The daily sync ran clean and found nothing (no new mail, empty enrichment queue). Jeremy then pasted one link by hand — Akshay Pachaar's explainer on the **Contrastive Language Model (CLM)**, post `2103483160382386234` — and asked for it to be filed so it "rhymes with some of yesterday's links."

It didn't rhyme. It landed with three `weak` edges and no home at all, despite being the single most on-topic post in the corpus for a concept that had been hand-created **the previous evening** for exactly that conversation. Chasing that is what produced everything below.

**Worth noting as a working pattern:** nothing here was found by auditing. It surfaced because a routine task produced a result that didn't make sense, and the anomaly was followed instead of worked around. The cheapest bug detector available is a small task whose output you can already predict.

---

## 1. The #74 magnet

### What happened

Concept #74 *System One models — bounded decisions as a primitive* was hand-seeded 2026-09-24 23:28 with 9 Jev posts, precisely because the semantic layer was scattering that conversation across five unrelated homes. It graduated the same day (bar is 4 canonical edges) and within 48 hours held **328 evidence edges, of which only 10 concerned Jev / CLM / RLCD.** The rest reached back to 2025-01-04: agent memory, agent factories, eval pipelines, harness recipes.

*Edge accounting, since the numbers are easy to garble:* `concept_observations` records **93 promoted edges on 2026-09-24 and 245 on 2026-09-25** (338 total), but the 09-25 figure includes the one hand-curated CLM edge added *after* the rollback. Peak evidence was **328** = 318 rolled back + 11 held now − 1 curated. An earlier draft of this record said "93 + 244", which doesn't sum to 328; the reconciling term is the curated edge.

### The diagnostic that mattered

Scoring the new CLM explainer against two versions of the same concept:

| scored against | cosine | outcome |
|---|---:|---|
| the original 9 hand-seeded members | **0.8397** | clears the 0.82 floor, homes correctly |
| #74's centroid after absorption | **0.8036** | below floor, rank **6 of 55** |

**A magnet does not merely over-recruit. It eventually stops recognising its own subject.** The concept ate enough unrelated material that the post it was created for could no longer reach it.

That asymmetry is the whole argument for a default rather than vigilance: by the time a concept is *visibly* too big, it is already rejecting its own core material — so the obvious symptom (size) appears after the damaging one (drift), and "keep an eye out for diffuse concepts" is advice that arrives too late by construction.

### Why the existing guards missed it

This is the part worth remembering. The nursery tier and the marker are **orthogonal**, and #74 fell through the gap between them:

- `status=provisional` gates whether a concept can be a home or feed centroids — #74 **graduated legitimately**, on 9 real hand-chosen edges.
- `[no-centroid-scoring]` gates whether a concept recruits by cosine — #74 didn't carry it, because marking was opt-in and nobody opted in.

Graduation was never going to catch this. A concept becomes a magnet *after* it earns a centroid, which is exactly the moment graduation stops paying attention.

### Remediation, and why demote rather than dismiss

318 edges moved `evidence → weak`; **nothing was dismissed**. That keeps the no-discard policy intact (last dismissal is still 2026-08-26) and is reversible — the exact set is in table `_rollback_74_20260925`. The keep/demote split was decided by a content test (does the post mention Jev / CLM / RLCD / System One / tev1 / TypeSafe), not by score, so it is reproducible and auditable rather than a judgement call dressed as a threshold.

Demotion works because `weak` is non-canonical: the edges stay recorded and browseable, they just stop voting on what the concept *means*. That is the role layer doing precisely the job it was built for.

**Verification that it worked:** the next pipeline run scored 45 concepts instead of 46 and proposed **+0** observations, down from +244 earlier the same day. #74 is now 11 evidence edges, all 11 homed, spanning Sep 16 → Sep 25 — the actual conversation.

### Then: how many more?

Generalising the shape into a detector (canonical > 40 **and** canonical > 10 × homes) returned **11 active concepts**, not one. These are the seven already documented under the set-identity finding (82–94% Jaccard overlap as re-measured today) plus four more.

So #74 was not an anomaly; it was a fast, visible instance of the corpus's general condition. **Deferred deliberately** (Jeremy: "we're well into hand-tooling territory, revisit on the next redesign"). The reason deferring is defensible: the *home* layer is unaffected — primaries remain a clean partition with disjoint sets — so this is a secondary-edge problem, not a filing problem.

---

## 2. The marker became the default

`create_concept()` and `record_latent_findings()` now stamp `[no-centroid-scoring]` unless the caller passes `centroid_scoring=True`.

**Why those two and not the third.** The rule of thumb already in `CLAUDE.md` — *if a concept exists only because a reader could see it, mark it* — turns out to name exactly the two reader-seeded paths. Both #65 and #74 came from a human or a model reading posts and perceiving a category. Members of such a category share a **purpose** but not a **vocabulary**, and averaging them yields a centroid near the corpus mean, which matches everything.

`discover_orphan_clusters()` is deliberately **exempt**. Those concepts are derived *from* the embedding geometry and are cohesion-guarded (`ORPHAN_CLUSTER_MIN_COHESION`), so they are vocabulary-coherent by construction. Marking them would freeze the only pass that grows vocabulary from theme — a real cost with no corresponding risk.

Regression coverage: `CentroidScoringDefault` in `db/test_roles.py` (7 tests). **3 were verified failing against the old default before the change**, per the convention this repo already follows for the `[primary-pin]` fix.

---

## 3. `db/filing.py` — an abstain-aware classifier

Jeremy's framing, which turned out to be the right one: *"We don't need a model, but we do need a classifier."*

CLM's contribution is not speed, it is **shape**:

- the application supplies a **finite candidate list**
- the scorer may **not invent** an option outside it
- it returns a typed id **or abstains**

`assign_primaries()` already did the first two. The third was missing, and on this corpus that omission is the whole problem.

### The measurement that justified building it

Over the contested posts (442 on the unbounded candidate set used for this comparison, so the three geometries are measured on identical populations):

| geometry | median top1–top2 margin | margin < 0.02 |
|---|---:|---:|
| raw (what ships) | 0.0014 | **95.9%** |
| mean-centered | 0.0222 | 47.5% |
| centered + bounded | 0.0227 | 46.7% |

**86% of raw multi-candidate filing decisions land inside a 0.01 margin.** At that spread the ranking measures the shared "AI stuff" direction, not fit. The homes were coin flips with a confident number attached.

### The correction that was nearly missed

Mean-centering is the obvious fix and it is **not sufficient — alone it makes filing worse**. Homes landing on tiny `url:`/`mention:` groupings, measured as *argmax is a mechanical concept* over all 577 edged posts:

| | mechanical homes |
|---|---:|
| raw | 21 |
| centered, unbounded | **29** |
| centered + bounded | **4** |

*(An earlier draft quoted 18 / 25 / 4, which mixed two different post populations — the first two figures were measured over multi-candidate posts only. The direction holds under every variant tried; the table above is one consistent basis. Worth the correction because a table that silently changes denominators between rows is exactly the kind of thing this record exists to prevent.)*

A 2-member centroid is sharp and idiosyncratic; removing the shared direction lets it win. So the tempting one-line version ("just mean-center it") would have quietly handed homes to exactly the groupings the curation preference says not to grow. **Bounding is load-bearing, not a refinement.** Preference not prohibition, though: a post whose only canonical edges are mechanical still homes there.

### Threshold, chosen twice by different arguments

`ABSTAIN_MARGIN = 0.03`, arrived at independently two ways:

1. **Sweep:** 0.03 is where the classifier stops *disagreeing* with existing homes (zero proposed reassignments) and becomes purely additive — impossible to blame for churn.
2. **Stability calibration** (below): at an 80% target, 0.03 is what `calibrate` recommends.

The single change proposed at 0.02 was itself an argument for 0.03: it moved an Anthropic agent-memory whitepaper summary into *local model serving on consumer GPUs* on a 0.0229 margin. The old home was plainly better. **Just above the floor is still the noise floor.**

---

## 4. Calibration is label-free, because it has to be

The obvious eval — score the classifier against existing primary homes — is **invalid here**, and this is the most transferable finding of the day.

Of 577 homes, on the **bounded** candidate basis throughout (139 + 435 + 3 pinned/no-vector = 577):

- **139** are single-candidate — forced, so they carry no information about discrimination
- of the **435** contested, **373 (86%)** were decided on a sub-0.01 raw margin

That leaves roughly **62** defensible decisions. An accuracy number measured against the rest would *rise* as the classifier got better at reproducing coin flips. **A dataset can look like ground truth and be noise wearing its clothes.**

*(Earlier drafts quoted "380 of 442", which is the same 86% measured on the *unbounded* candidate set. Both are true on their own basis, but presenting 139 and 442 together implies they partition the same 577, and they don't — 577 − 139 = 438. Fixed to one basis. The 86% is unaffected.)*

So `calibrate` measures **stability** instead: bootstrap-resample each candidate concept's membership and ask whether the same home still wins. A decision that doesn't survive resampling was an artifact of which posts happened to be attached. Seeded, so it is reproducible — a threshold derived from a number that moves every run is not a calibration.

| centered margin | n | home survives resampling |
|---|---:|---:|
| 0.00–0.01 | 131 | 32.3% |
| 0.01–0.02 | 73 | 38.7% |
| 0.02–0.03 | 46 | 54.2% |
| 0.03–0.05 | 54 | 61.7% |
| 0.05–0.08 | 41 | 78.9% |
| 0.08–0.12 | 18 | 92.2% |
| > 0.12 | 73 | 99.5% |

Monotonic — which is the result that justifies the margin-based design at all, with no labels required.

**Quote it honestly.** 0.03 clears 80% *on average* (83.3% over 186 retained), but the 0.03–0.05 band inside it is only 61.7%. The mean is carried by the high-margin tail. `--target 0.9` gives 0.05, retaining 132 at 92.1%. Left at 0.03 because raising it costs a third of the confident set for a guarantee that may not be needed — revisit after real use.

---

## What was considered and rejected

- **A conventional accuracy eval against existing homes.** Rejected: the labels are the noise (§4).
- **Training the CLM-shaped head now.** Rejected for the same reason — it would learn to imitate coin flips. Blocked on a gold set, which must be **stratified across margin bands**; a random sample is dominated by easy cases and would flatter any classifier.
- **Mean-centering `assign_primaries` directly.** Rejected: unbounded centering increases mechanical homes (§3), and changing the live filing path is a bigger commitment than adding a review instrument beside it.
- **Remediating all 11 magnets today.** Deferred by Jeremy; the home layer is unaffected, so the cost of waiting is bounded.
- **Dismissing the 318 over-attached edges.** Rejected in favour of demotion — no-discard policy, and demotion is reversible.
- **Marking orphan-cluster concepts too.** Rejected: they are cohesion-guarded and vocabulary-coherent, and marking them would freeze vocabulary growth (§2).

---

## Honest limits of what was built

- `db/filing.py` inherits bge-small's geometry and **learns nothing about how Jeremy actually files**.
- It **cannot fix a magnet, only reveal one.** A drifted centroid poisons every post scored against it, so run the magnet detector first.
- **Margin is not calibrated probability.** 0.05 is not "95% sure"; it is "further apart than the median decision on this corpus."
- The abstention rate (~324 of 577) is high **by design** — the honest version of a number that was previously 100% confident and 86% coin flips.
- Two tests caught two of my own errors while writing this (an over-strict assertion scoped to the whole run instead of the post under test, and a "ambiguous" fixture built from tight clusters that were in fact perfectly stable). Both are noted in the test files, since a fixture that cannot fail is worse than no test.

---

## Follow-ups

1. **Paste `scheduled/ai-links-sync.SKILL.md` over the live task by hand.** A sandbox session cannot write to `~/Documents/Claude/Scheduled/<id>/SKILL.md`, and this is the exact drift that went unnoticed for weeks in August.
2. Use `review filing` for a few weeks before investing in gold labels — real usage should decide whether the abstain queue surfaces genuine mis-files.
3. Re-run `python3 -m db.filing calibrate` after any large merge, split or re-home; those reshape the centroids the threshold was derived from.
4. The 11 magnets, at the next redesign. The untried lever is capping **evidence** attachment per post — `SEMANTIC_MAX_WEAK_PER_POST` caps weak edges, nothing caps evidence.
