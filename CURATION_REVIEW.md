# Adversarial Review — AI Links Curation Layer

> **Rev 3 verified (June 2026) — all follow-up items resolved, cleared for implementation.** The latent-gate floor, priority write-discipline, the `curate.py` shared-lock-and-push, and the `post_embeddings` staleness shape were all checked against the actual formula/schema and are correct. Revision 2's structural decisions (candidate/canonical split, chat write-path) are untouched. See "Revision 2 follow-up" and the Rev 3 confirmation below for detail.

**Date:** June 2026
**Reviews:** `CURATION_DESIGN.md` (June 2026), grounded against `ARCHITECTURE_PLAN.md`, `db/migrate.py`, `db/rebuild.py`, and the live `db/ai_links.db`.
**Method:** 5 independent adversarial reviewers run on the opposite model (Codex), each on a distinct lens. Reviewers challenged whether the design *achieves its intent*, not whether the intent is worthwhile. Synthesis + lead judgment by Claude.
**Reviewer lenses:** Skeptic (correctness/completeness), Architect (structural fitness), Minimalist (necessity/complexity), Product/Attention-ROI (value-per-effort for one user), Data-modeling/Migration (schema + migration safety).
**Raw per-lens reports:** `/tmp/adv-review-curation/{skeptic,architect,minimalist,product,data}.md` (regenerate if cleared).

---

## Corpus facts used by reviewers (live DB at review time)

These ground several findings — note they differ from the doc and from project context:

- **587 posts** total (doc says 548; project `CLAUDE.md` says 254 — both stale).
- **All 587 are `enriched=1`** — yet **328 have empty `content`**, ~**60-69** have failure-placeholder/short summaries (deleted, suspended, login-wall, image-only). The "everything is enriched" flag is not trustworthy.
- **Priority distribution:** 103 `now`, 315 `near-term`, 169 `long-term`.
- **Audience is many-to-many** (`post_audiences`, ~1030 rows for 587 posts; **402 posts have multiple audiences**), skewed heavily to `me`.
- **Topics overlap heavily:** `agent-design` 281, `claude-code` 143, `questionable` 75.
- **`post_relations` live PK** is `(post_id_a, post_id_b)` with `relation` outside the key.
- **`migrate.py`** is a rebuild-from-JSON script (deletes target DB, re-imports), **not** an incremental migration runner. **`rebuild.py`** reads `row['enriched']` and exports it to JSON/HTML/MD.

---

## Verdict: CONTESTED — sound direction, not implementable as written

The architectural instincts are right and the reviewers said so explicitly (see "What went well"). But there are **four high-severity, multi-reviewer-consensus items that must be resolved before any code**, plus **one genuine scope disagreement that is the author's call**. By strict spec standards the schema as written is a REJECT (the PK bug is verified, not theoretical); as a deliberately-loose intent doc it's CONTESTED — fix these and the frame is solid.

**Key synthesis insight:** the "cut scope" advice (Product/Minimalist) and the "add tables for correctness" advice (Architect/Data) are **not in conflict** — they operate on different axes. Ship *fewer features*, but give the features you keep a *cleaner schema*. Most schema pain comes from `post_concepts` trying to do too many jobs at once.

---

## Three headline takeaways

### 1. One root structural decision causes ~4 of the bugs
`post_concepts` stores raw discovery observations *and* curated truth in one table, multiple rows per (post, concept), "aggregate at query time." That single choice is the root of: the PK duplicate bug (H1), strength-incomparability (M), dismissed-candidates-regenerating-weekly (M), and merge-chain resolution (M).

**Fix:** split candidate/observation rows (provenance, raw score, discovery run) from canonical curated edges (one row = the human's truth). Fixing this one thing collapses four findings.

### 2. The design has no write path (Architect, high)
Curation = promote/merge/dismiss + per-lens editing = **writes**. But the viewer is read-only generated HTML (`rebuild.py` emits a static artifact). Click "promote" and either nothing persists, state forks into browser-local storage, or the design quietly grows an unplanned backend.

**Fix:** decide the persistence boundary *now* — a small CLI/local command that mutates SQLite and re-runs rebuild, or an explicit tiny local writer service. Do not describe any viewer curation action until this path exists.

### 3. The scope question is the author's to make (Product + Minimalist, high)
Both reviewers independently recommend **cutting the latent LLM pass and the entire v1.1 persona/model machinery from v1, and trimming 5 lenses to 2-3 modes.** Grounded in the corpus facts: until capture is actually faithful (328 empty-content rows), blinded LLM discovery is finding clever threads in partial data, and it creates a permanent weekly triage chore (~1,000 human decisions/year) with no evidence it beats mechanical + semantic. This contradicts the doc's "it's basically free shape" framing.

**Lead lean:** defer latent + v1.1; gate them behind "mechanical+semantic ran for a month and I can name 5 non-obvious connections they missed." But the author explicitly values non-obvious discovery — so this is a **taste call, not a bug.** Decide it explicitly rather than drift into building everything.

---

## Findings by severity (deduplicated across 5 reviewers)

### High

**H1 — `post_concepts` primary key is broken.** *(Data [verified], Architect, Minimalist, Skeptic)*
PK `(post_id, concept_id, source, discovery_persona, discovery_model)` with persona/model NULL for mechanical/curated rows. SQLite treats NULLs in a PK as distinct, so identical mechanical edges duplicate. **Verified:** inserting `(1,2,'mechanical',NULL,NULL)` twice yields count=2. Breaks dedup, corroboration, and idempotency.
**Judgment: ACCEPT.** Fix = `NOT NULL DEFAULT ''` sentinels + UNIQUE, or better a `discovery_runs` table + `run_id` (also relocates v1.1 provenance off every edge — see H6).

**H2 — No persistence boundary for curation.** *(Architect)* — see Takeaway 2.
**Judgment: ACCEPT — top priority.** The workflow is unbuildable until this is answered.

**H3 — `enriched → enrichment_status` backfill would lie.** *(Data, Skeptic, Product)*
All 587 `enriched=1` but 328 empty-content + ~60 placeholders. Naive `enriched=1 → 'ok'` makes the targeted re-scrape unable to find incomplete rows by status — defeating its own premise.
**Judgment: ACCEPT.** Backfill to `legacy-ok`/`unknown`, never `ok`; add `enrichment_version` so rolling re-enrichment targets `version < current`. Conservative backfill: empty content → `partial`; placeholder summary → `partial`/`dead`.

**H4 — `post_perspectives.audience TEXT` silently destroys data.** *(Skeptic, Data)*
Audience is m2m (1030 rows; 402 multi-audience posts). One scalar column can't seed that without lossy comma-joining.
**Judgment: ACCEPT.** Use `post_perspective_audiences(post_id, lens, audience)` junction, or drop audience-per-lens for v1.

**H5 — Two sources of truth for priority.** *(Data, Minimalist)*
`posts.priority` (default) + `post_perspectives.priority` (overlay) drift permanently; every morning query needs COALESCE/join.
**Judgment: ACCEPT the problem.** Fix = *replace not overlay*: a `lens='default'` row, `posts.priority` becomes read-only legacy. Dissolves entirely if lenses are cut for v1 (H6).

**H6 (scope) — Cut latent pass + v1.1 + trim lenses from v1.** *(Product, Minimalist)* — see Takeaway 3.
**Judgment: LEAN ACCEPT — author's call.** Data-grounded and matches attention-ROI, but trades away the prized non-obvious discovery. Decide explicitly.

**H7 — Concurrency race.** *(Skeptic)*
Daily sync vs manual catch-up vs Sunday batch all mutate shared DB + `rebuild.py` outputs + git push. SQLite avoids corruption but generated artifacts and the push can race (A rebuilds state A, B writes state B, A overwrites/pushes stale).
**Judgment: ACCEPT, right-sized.** A lockfile + atomic rebuild (temp-file + rename) is enough for a solo local tool. Don't build a lock service.

**H8 — Self-reply capture by handle is fragile.** *(Skeptic, Architect)*
X interleaves non-author replies, virtualizes DOM, hides "show more"; "stop when handle changes" drops the reply holding the GitHub link. Handle matching fails in compact/display-name-only views or after handle changes.
**Judgment: ACCEPT.** Store structured thread segments (`op`/`self_reply`/`quote`/`external_link`, ordinal, handle, text, url) rather than an inlined blob — also gives Layer 2 segment-level evidence provenance. Test against real forked/interleaved/self-quote cases before trusting the DOM walk.

### Medium

- **strength not comparable across provenance** *(Data, Architect)*: mechanical 1.0 vs semantic 0.86 vs latent self-report aren't one scale; `MAX`/`SUM`/`AVG` all misbehave (`SUM` worsened by H1 dup bug). **ACCEPT** — store `raw_score` + `score_kind`; defer any materialized "belief" computation until cross-source ranking is actually needed. (A versioned `post_concept_beliefs` table is premature for a lean v1.)
- **No candidate lifecycle in `post_concepts`** *(Architect, Minimalist, Skeptic)*: dismissed latent candidates regenerate weekly; merged concepts keep receiving rows on the old id. **ACCEPT** — falls out of Takeaway 1 (split candidate/canonical) + a dismissal/suppression record.
- **`migrate.py` is rebuild-from-JSON, not incremental; `rebuild.py` reads `row['enriched']`** *(Data, verified)*: renaming the column breaks export immediately. **ACCEPT** — additive `ALTER TABLE` + update `rebuild.py` in the same change, or add a real versioned migration runner first (transaction per migration, `schema_version` advanced atomically).
- **Concept merge chains** *(Data, Skeptic)*: A→B→C needs recursive CTE on every read or goes stale; nothing prevents A→B + B→A. **ACCEPT** — flatten-on-merge in one transaction; reject cycles before write.
- **sqlite-vec underspecified** *(Data)*: no embedding dimension, storage shape, model identity, or staleness rule; 328 empty-content rows produce junk vectors. **ACCEPT** — but specify when building the semantic phase, not now. Add `content_hash`-based invalidation; store model + dim and reject mismatches.
- **Morning surface never defined** *(Product, Architect, Minimalist)*: the doc specifies graph infrastructure but never the actual "here are your 3-5 posts" output, and sequences felt value too late. **ACCEPT — high-value despite medium tag.** Define the default morning view (`Read now` / `Recurring` / `Revisit`, hard-capped, with one-line reasons) and re-sequence to ship it right after Layer 1.
- **Re-scrape can overwrite good data** *(Skeptic)*: broken selector → thin/wrong summary replaces a good one; candidate set isn't really "~50-80" (already 75 `questionable` + 328 empty). **ACCEPT** — snapshot old fields to an audit table; promote new enrichment only if measurably better (non-error content length, author match, link count).
- **Faithful capture underweighted vs ROI** *(Product)*: make enrichment quality a first-class score and ranking gate. **ACCEPT.**

### Low

- **`post_relations` PK too narrow** *(Data, verified)*: `(post_id_a, post_id_b)` can't hold both `quotes` and `extends` for a pair. Add `relation` to the key; decide if `(A,B)`/`(B,A)` are distinct.
- **Stale corpus counts** *(Skeptic)*: 548 (doc) vs 587 (DB) vs 254 (`CLAUDE.md`). Generate live stats as an implementation-checklist command.
- **"Adding a lens is config not migration" is premature flexibility** *(Minimalist)* for n=1. Accept migrations; keep schema boring until a second lens proves durable.

---

## Where the lead pushed back on the reviewers

- **Don't over-build tables in response.** Reviewers collectively proposed `concept_observations`, `post_concept_evidence`, `post_concept_beliefs`, `discovery_runs`, `post_thread_items`, `post_perspective_audiences`, `post_embeddings`, `concept_embeddings`. Adopt the *split* (candidate/observation vs canonical) and the *junctions* (audience, thread segments) — but the versioned belief table is premature for a lean v1.
- **The "global lock covering GitHub sync"** is enterprise-shaped; a lockfile is the right size for a personal tool.
- **"Record cost/token metadata now"** only pays off if latent is kept — and the H6 scope decision may delete it.

---

## What went well (reviewer consensus)

- Unifying daily-sync + catch-up onto one `enrich()` path fixes a real drift root-cause.
- Self-reply capture targets a genuine, measurable data-quality failure (the 328 empty-content rows confirm it).
- Curated-concepts-as-suggestions (human decides) is the right posture for a single-user attention tool.
- Keeping generated HTML as an output artifact rather than a platform.
- Separating post-to-post edges from post-to-concept evidence is the right modeling boundary — *once the identity is fixed*.

---

## Suggested integration order

1. **Make the H6 scope call first** — it determines how much schema (lenses, latent provenance) even exists in v1.
2. **Resolve H2 (write path)** — it's a precondition for any curation feature.
3. **Apply the Takeaway-1 split** to `post_concepts` — collapses H1 + several mediums.
4. **Fix the migration honesty** — H3 backfill, H4 audience junction, `migrate.py`/`rebuild.py` reality.
5. **Define the morning surface + re-sequence** so felt value lands right after Layer 1.

A natural follow-on is `/plan-eng-review` to fold the accepted findings directly into a revised `CURATION_DESIGN.md`.

---

# Revision 2 follow-up (June 2026)

Reviewed `CURATION_DESIGN.md` after the revision that incorporated the findings above. **Verdict: green-light implementation after one structural fix (gate floor, below).** The revision didn't just patch findings — it made real structural decisions and defended the ones it declined.

## What landed well

- **Candidate/canonical split adopted cleanly.** `concept_observations` (autoincrement `id`, immutable history + provenance) vs `post_concepts` (one row per pair = human truth). This one move dissolved H1 (PK bug), strength-incomparability, dismissed-regeneration, and merge-chain resolution as predicted. The "Why the candidate/canonical split" section is the strongest part of the doc.
- **Write path (H2) — better than recommended.** The chat-mediated `curate.py` ("promote 4823", "merge concepts…") avoids a backend entirely and matches how the tool is actually used. No browser state, no writer service.
- **Backfill honesty (H3).** Conservative `legacy-ok`/`partial`/`dead` + `enrichment_version`; re-scrape scope corrected from "50-80" to "~388."
- **Audience (H4):** scalar dropped, `post_audiences` m2m preserved.
- **Morning surface:** went from absent to a fully specified, hard-capped 3-section `morning.json` shipping right after Layer 1. Re-sequencing is correct.
- **post_relations PK, merge cycles, snapshot-before-rescrape, real migration runner** all folded in.
- **Declined scope (H6) defended, not ignored.** Keeping latent discovery but gating it on data quality is the right way to honor both the "no clever threads from noise" objection and the author's preference for non-obvious discovery.

## Must-fix: the latent gate can never open (NEW issue introduced by the revision)

The gate is written as `(partial + failed + dead) / total < 5%`. **`dead` is permanent** (404s, suspended accounts, login-walls never become recoverable). Live DB check (593 posts at review time):

- 328 empty-content
- ~60 carry permanent-death markers (deleted / suspended / "page doesn't exist" / login-walled)
- 56 are both — almost certainly permanently dead

So the `dead` floor alone is **~9-10% of the corpus**, against a 5% threshold. Even with every recoverable post re-enriched perfectly (`partial + failed → 0`), the ratio bottoms out at `dead/total ≈ 10% > 5%`. **The latent pass would be built and then never run.**

The doc lists "too strict (never opens)" as a threshold-tuning open question, but this is structural, not a knob: no threshold between 0 and ~10% works while `dead` is in the numerator.

**Fix (one-line SQL change):** gate on *recoverable* incompleteness — `(partial + failed) / (total − dead) < 5%`. Excludes the permanent floor; becomes reachable as re-enrichment does its job.

## Smaller residuals (none blocking)

1. **Priority overlay write-discipline (H5).** The revision chose overlay + `get_effective_priority()` instead of full replace (defensible). But `posts.priority` is called "legacy fallback" without forbidding *writes* to it — if both it and the `tool-eval` row keep getting written, they diverge and the helper silently picks one. Close it: after migration, `posts.priority` is read-only; all writes go to perspective rows.
2. **`curate.py` and the sync lock (H7).** The lockfile is described as covering concurrent *sync* runs, but `curate.py` also writes SQLite and triggers `rebuild.py` — it must take the same lock. Also unclear whether curation pushes to GitHub or only writes locally; if local-only, the weekday pull-first sync must reconcile rather than clobber local curation. Needs one explicit sentence.
3. **sqlite-vec staleness (deferred).** Skipping `partial`/empty posts is correct, but the schema still has no `content_hash`/model/dim shape, so re-enrichment won't know which embeddings went stale. Fine to defer the table — but decide it before step 6 (semantic), since re-enrichment (step 8) and semantic (step 6) interleave.

## Net

Green-light after the gate fix (#1 of the residuals is the only other one worth doing up front). The candidate/canonical split and chat write-path are the decisions that make the rest of the build straightforward. The scope calls are the author's and were made defensibly — the gate *is* the answer to the latent-on-noise critique; it just needs to be reachable.

---

# Revision 3 confirmation (June 2026)

Verified the Rev 3 changes against the actual formula and schema (not just presence of the words). **All four follow-up items resolved correctly; cleared for implementation.**

1. **Latent gate floor — fixed.** Now `(partial + failed) / (total − dead) < 5%`, with `dead` excluded from both numerator and denominator and the rationale spelled out ("a fact about the world, not a quality problem we can drive down"). Propagated to the sequencing step and open-questions note, which correctly states any future tightening should be a minimum-N clause, not re-adding `dead`. Reachable as re-enrichment drives `partial`/`failed` down.
2. **Priority write-discipline — fixed.** `posts.priority` is explicitly read-only after migration; all writes go to `post_perspectives`. Closes the overlay drift hole.
3. **`curate.py` lock + push — fixed, went further than asked.** The lock covers every writer, not just sync. `curate.py` acquires the shared lock, mutates, rebuilds once, then commits+pushes inside the batch before releasing — so the repo's canonical state matches local and the weekday pull-first sync sees curation as canonical, not a divergent change. Resolves both the lock race and the pull-first-clobber question.
4. **sqlite-vec staleness — fixed.** `post_embeddings` table spec'd with `(post_id, model)` PK, `dim` (reject-on-mismatch), `content_hash` staleness anchor, and the re-embed-on-mismatch flow. Decided before the semantic step, as recommended.

No new problems introduced by the tightening changes; Revision 2's structural decisions are untouched.

**Optional micro-note (not worth a revision):** `unknown`-status rows sit in the gate denominator but not the numerator, making the ratio slightly optimistic. Non-issue in practice — the conservative backfill assigns `legacy-ok`/`partial`/`dead` and rarely leaves anything `unknown`.
