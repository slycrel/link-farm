---
name: ai-links-filing
description: "Abstain-aware filing review for Jeremy's AI Links Collection. Use whenever Jeremy says 'review filing', 'check the filing', 'what's badly filed', 'which posts are in the wrong concept', 'run the classifier', 'filing report', 'abstain queue', 'what can't you classify', 'which homes are coin flips', or wants to know how confident the primary-home assignments actually are. Also trigger when he asks whether a specific post is filed correctly, or after a large re-home / merge / split when he wants to know what moved and what the geometry can't decide."
---

# Abstain-Aware Filing Review

You operate the **filing classifier** for Jeremy's AI Links Collection: `db/filing.py`. Read `CLAUDE.md` for project background.

This skill answers one question — *which primary homes do we actually believe?* — and it is deliberately a **review instrument, not an auto-filer**. At its default calibration it proposes zero reassignments; its whole output is the separation between decisions it can stand behind and decisions it cannot.

## Why this exists

`assign_primaries()` always names a winner. Measured on the live corpus (2026-09-25, 442 multi-candidate posts), **86% of its decisions land inside a 0.01 cosine margin** — at that spread the ranking measures the shared "AI stuff" direction, not fit. The homes are coin flips wearing a confident number.

The fix borrows the contract from the Contrastive Language Model (the Akshay Pachaar explainer Jeremy added 2026-09-25, post `2103483160382386234`) without borrowing a trained model. **We don't need a model; we need a classifier.** CLM's real contribution is the shape:

- the application supplies a **finite candidate list**
- the scorer may **not invent** an option outside it
- it returns a typed id **or abstains**

`assign_primaries` already does the first two. The third is what was missing, and it is the one that matters here.

Two corrections underneath it, and the second is easy to get wrong:

1. **Mean-center before scoring.** Removes the shared corpus direction; median margin improves ~16x (0.0014 → 0.0222). Same geometry `discover_orphan_clusters()` already uses.
2. **Bound candidates to conceptual concepts.** Centering *alone* makes things worse — tiny `url:`/`mention:` groupings have sharp idiosyncratic centroids and start stealing homes (mechanical homes went raw 18 → centered 25 → centered+bounded **4**). Preference, not prohibition: a post whose only canonical edges are mechanical still homes there.

**All thresholds in `db/filing.py` are CENTERED cosines** and are not comparable to `SEMANTIC_CENTROID_THRESHOLD` / `AUTO_PROMOTE_MIN_COSINE`, which are raw. Same trap the orphan-clustering constants carry.

## Running it

```bash
python3 -m db.filing report              # distribution + what would change
python3 -m db.filing review --limit 25   # the abstain queue, unfiled first
python3 -m db.filing apply --confirm     # write confident decisions only
```

Or in-process, which is what you usually want so you can read summaries alongside scores:

```python
import sys; sys.path.insert(0, cowork)
from db import filing
r = filing.report()                       # writes nothing, ever
queue = [d for d in r["decisions"] if d.abstained and not d.pinned]
```

## How to run a review session

1. **Start with `report()`.** Give Jeremy the headline: how many confident, how many abstained, how many would change, median margin. If `would_change` is non-zero at the default margin, that is notable — the default is calibrated to the point where the classifier stops disagreeing with existing homes.

2. **Work the abstain queue, unfiled first.** `d.unfiled` (abstained *and* no existing home) is the sharp end — those posts have no home at all and the geometry can't pick one. Read the actual summaries; don't triage on scores.

3. **A negative top score is the most interesting signal in the queue.** It means the post is *anti-correlated* with the concept it currently sits in — raw cosine would have shown ~0.8 and told you nothing. Treat those as likely mis-files worth a human decision.

4. **Propose, don't act.** Structural changes (re-home, merge, rename, pin) go through the `ai-links-curate` skill and `db/concepts.py` helpers. This skill's job is to produce the shortlist and the evidence.

5. **Pin what you resolve by hand.** If Jeremy decides a home, set the `[primary-pin]` marker so `assign_primaries()` stops recomputing it. Pinned posts are reported as abstentions here by design (`d.pinned`) — that is the pin working, not a failure.

## What this skill must not do

- **Never dismiss an observation.** The no-discard policy holds: automation attaches and labels, humans discard. `db/filing.py` contains no dismissal path and a regression test enforces that.
- **Never un-home a post on a thin margin.** An abstention is a no-op, not an un-filing. A post keeps whatever home it has; the classifier just declines to defend it.
- **Never retune the thresholds to make the output look better.** They were swept against the real corpus (the table is in `db/filing.py`). If a number looks wrong, say so and show the sweep — don't quietly move it.
- **Don't run `apply --confirm` unattended.** Read the proposed diff first. The one change proposed at margin 0.02 during calibration was wrong (an agent-memory whitepaper moved to "local model serving" on a 0.0229 margin), which is exactly why the default is 0.03.

## Known limits, worth saying out loud

- **Abstention rate is high by design** (~324 of 577 at the default). That is not the classifier failing; it is the honest version of a number that was previously 100% confident and 86% coin flips.
- **It inherits bge-small's geometry.** It learns nothing about how *Jeremy* files. A trained head over the ~578 existing primary-home decisions is the real CLM-shaped upgrade and has not been attempted.
- **It cannot fix a magnet**, only reveal one. A concept that absorbed hundreds of unrelated edges has a drifted centroid, and every post scored against it is scored against that drift. Check the magnet detector in `CLAUDE.md` first; as of 2026-09-25 **11 active concepts** trip it.
- **Margin is not calibrated probability.** A 0.05 margin is not "95% sure". It is only "further apart than the median decision on this corpus".
