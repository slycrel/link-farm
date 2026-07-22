# AI Links Curation Layer — Design

**Date:** June 2026
**Status:** Working design — pre-implementation (revised after adversarial review)
**Builds on:** `ARCHITECTURE_PLAN.md` (March 2026)
**See also:** `CURATION_REVIEW.md` — independent adversarial review whose accepted findings are folded in below.

This is an outline of intent, not a spec. The goal is a shared frame for the curation work — what we're trying to make true about the system after this round of changes — without locking us into implementation choices that will obviously want to shift as we build. Where something feels under-specified, that's on purpose; we'll let the building inform the design rather than the other way around.

**This revision incorporates the accepted findings from `CURATION_REVIEW.md`:** Layer 2 splits `concept_observations` (raw discovery events with full provenance) from `post_concepts` (curated canonical truth); Layer 1 adopts structured thread segments and `enrichment_version`; Layer 3 picks up a "morning lens" as the default daily surface; a new Write Path section pins curation to Cowork chat; the latent discovery pass is gated on enrichment quality rather than cut from scope; and several smaller corrections (PK fixes, lockfile + atomic rebuild, conservative backfill, audience-per-lens drop) are folded throughout. The scope-cut recommendations on lenses and latent are explicitly declined — the latent pass earns its keep behind the gate, and lens overlay is cheap.

**Revision 3 (June 2026) — fresh-reader explicitness.** A follow-up review caught that several nuances were *implied* in the doc but not *explicit* enough to survive a fresh implementer reading it in isolation. Four specific fixes folded in: the latent gate formula was structurally unreachable (`dead` is permanent and sat in both numerator and full corpus denominator) — corrected to exclude `dead` from both sides; `posts.priority` is explicitly read-only after migration so writes can't drift between it and the perspective row; the lockfile covers `curate.py` and any writer, not just sync; and `post_embeddings` shape is spec'd with `content_hash` invalidation so re-enrichment knows what to re-embed. The scope and structural decisions from Revision 2 are unchanged.

---

## North star

**Help me spend attention well in the AI/agents space — both moment-to-moment ("what's worth reading right now?") and conceptually ("what ideas are recurring, evolving, or worth tracking over time?").**

The link collection is the substrate. The point isn't the corpus; the point is what the corpus tells me about where to look. A good v1 of this system should be able to answer questions like:

- "What's worth my 15 minutes this morning?"
- "What ideas have been recurring across multiple authors I respect over the last month?"
- "Which posts from 3 months ago do I actually want to revisit, vs. which were noise?"
- "What conversation is the field having right now that I'm tangentially adjacent to?"
- "Is this post I just read part of a larger thread of thinking, or a one-off?"

The current system is good at "store and tag." It's not yet good at "surface connections" or "support multiple readings of the same post" — and it doesn't yet have a defined morning surface that actually answers the first question above. This design closes those gaps.

---

## Why this design, what changed since v2

`ARCHITECTURE_PLAN.md` (v2) anticipated some of this — the `post_relations` table is sketched, "concept clustering" appears under Edge Explorer, and sqlite-vec is named as a future direction. What's changed is that we've used the system for ~3 months and the v0.8 shortcomings have come into focus:

- **OP-only scraping misses substance.** Listicle-style authors put their content in self-replies; we capture only the hook. The "questionable" tag is doing double duty — sometimes "clickbait but real substance behind the link," sometimes "I literally didn't read past the hook."
- **The "everything is enriched" flag isn't trustworthy.** As of this revision the DB has **587 posts all flagged `enriched=1`, but 328 have empty `content` and ~60 have placeholder or near-empty summaries** (deleted, suspended, login-walled, image-only). The single boolean conflates "we tried" with "we got something useful."
- **Two enrichment implementations drift.** The daily sync and catch-up skills do similar work via different code paths. Every improvement has to be made twice and sometimes only gets made once.
- **Single-valued `priority` and `audience` flatten real nuance.** The same post might be `now` for someone thinking about hiring and `near-term` for someone thinking about implementation. We can't represent that.
- **No first-class relationships.** Posts are nodes; there are no edges. The "what ideas are recurring" question requires me to scroll and remember.
- **Curation is binary (in/out) rather than graduated.** A clickbait post that's evidence for a concept I care about should be able to live in the collection without polluting the daily-read surface.
- **No defined morning surface.** The current viewer is good for browse-and-search, but doesn't answer "what should I read right now?" — which is the system's reason to exist.

The design below is a direct response to these.

---

## The three layers

The system stops thinking of a post as a fully-classified atom and starts thinking of it as a piece of evidence that lives inside relationships. Three layers, each with a different job:

1. **Faithful capture** — every post in SQLite reflects what was actually said, including thread context.
2. **Concept graph** — discovered + curated relationships between posts, surfaced as named concepts/themes.
3. **Perspective lenses** — ways of viewing the graph (and the posts within it) depending on what I'm trying to do, including a dedicated "morning lens" that ships the default daily view.

The layers stack: concepts depend on faithful capture, lenses operate over both. The build order mostly follows the same shape, but the morning lens (a Layer 3 surface that doesn't strictly require concepts) ships right after Layer 1 so the system delivers daily value before the concept work is mature.

A separate **Write Path** section below pins the curation persistence boundary, which spans all three layers.

---

## Layer 1: Faithful capture (unified enrichment)

### Desired outcomes

- Every post in the DB reflects what the author actually communicated, not just the OP fragment X happened to show us first.
- One code path handles enrichment, whether the post is brand new (daily sync) or being re-processed (catch-up). No drift.
- Failures are visible and recoverable. I shouldn't have to wonder whether yesterday's sync silently dropped a post.
- The "thread" of an author's own contribution is captured as a structured set of segments — OP, self-replies, quoted content, and external links — not an inlined blob. Other people's replies are *not* part of the capture (they're discourse, not the author's content).
- The system never lies about enrichment quality. `enriched=1` is replaced by a status enum that distinguishes "actually has content" from "we tried."

### Shape

A single `enrich(post)` function that:

1. Navigates to the URL via Chrome.
2. Captures the OP article as an `op` segment.
3. Walks the author's self-reply chain, capturing each as a `self_reply` segment.
4. Captures quote-tweet context as a `quote` segment.
5. Captures GitHub/arxiv/paper links called out anywhere in the captured content as `external_link` segments.
6. Captures author display name, handle, view count, post timestamp.
7. Writes a summary, topics, and (later) a concept-tag candidate set based on the *combined* segmented content.
8. Records `enrichment_status` (`ok` / `partial` / `failed` / `dead` / `legacy-ok` / `unknown`), `enrichment_version` (integer), attempt count, last error, last attempt timestamp.

The thread itself is structured, not blob-inlined:

```
post_thread_segments (
    post_id     INTEGER REFERENCES posts(id)
    ordinal     INTEGER NOT NULL          -- order within the captured thread
    type        TEXT NOT NULL             -- 'op' | 'self_reply' | 'quote' | 'external_link'
    handle      TEXT
    text        TEXT
    url         TEXT
    captured_at TEXT
    PRIMARY KEY (post_id, ordinal)
)
```

This survives DOM fragility better than handle-matching ("stop when the handle changes" drops the reply with the GitHub link if a non-author reply got interleaved) and gives Layer 2 segment-level evidence — the GitHub URL in self-reply #3 can attach to a concept on its own.

Both the daily sync skill and the catch-up skill call the unified `enrich()` function. There is no separate "enrichment phase." The skeleton-insert-then-enrich-later pattern goes away — if Chrome is unreachable, the insert path stubs the row with `failed` status and the next sync retries it.

### What "done" looks like

- A single `db/enrich.py` module exists and is imported by both `sync` and `catch-up` skills.
- `enriched` boolean is replaced by `enrichment_status` enum + `enrichment_version` integer, with attempt tracking. **Backfill is conservative**: never to `ok`. Existing posts with non-empty content and a real summary become `legacy-ok` (worked once, version 0); posts with empty content become `partial`; posts with placeholder summaries become `partial` or `dead` depending on the marker. The targeted re-scrape uses status + version to find work, so calling the existing 587 posts all `ok` would defeat its own premise.
- 100% of new posts go through unified enrichment from the moment they're seen.
- `enrichment_version` lets rolling re-enrichment target rows where `version < current` regardless of status — every post eventually gets re-processed under the current capture logic.
- A targeted re-scrape pass over the **~388 visibly-incomplete posts** (328 empty-content + ~60 placeholder/short summaries) brings the existing corpus up to current standard. This is bigger than the original "50–80" estimate; the actual scope was hidden by the misleading `enriched=1` flag.
- Per-post failures surface as a "needs attention" badge in the viewer after the second consecutive failure.
- Systemic failures (Chrome unreachable, etc.) surface immediately as a viewer-header notice plus the existing scheduled-task retry fallback.
- A lockfile + atomic rebuild (temp-file + rename) prevents concurrent writers from racing on `rebuild.py` outputs or the git push. A solo local tool, not enterprise — a single PID file in the cowork folder is sufficient. **The lock covers every writer, not just sync.** `curate.py` (Write Path), the daily sync skill, the catch-up skill, and any future writer all acquire the same lock before touching SQLite or running `rebuild.py`. Without this, a curation action mid-sync would race the rebuild and produce inconsistent outputs.
- **Follow-on (background):** once unified enrichment is live and stable, queue the broader corpus for rolling background re-enrichment in weekly batches until `enrichment_version` is current across the board.

### Notes / open questions

- How aggressively to walk self-replies? Cap at 10? Stop on a non-author reply? Probably "cap at 10 and capture every author-handle-match in the conversation regardless of interleaving" — the structured-segment shape makes interleaving safe to handle without the brittle "stop when the handle changes" rule.
- For quote tweets: now a separate segment in `post_thread_segments`. The quoter is the curator; the quoted content's value is contextual.
- The `dead` status is for posts we've confirmed are 404 / login-walled / suspended. These stay in the DB (we never delete) but the viewer downweights them.
- Re-scrape can overwrite good data if a selector breaks. Snapshot the existing fields to a small audit table before replace; only promote the new enrichment if it's measurably better (non-error content length, author match, link count). Don't silently degrade.
- `migrate.py` is currently a rebuild-from-JSON script, not a versioned migration runner. The schema work in this layer is the right moment to introduce a real migration runner with a `schema_version` table — additive `ALTER TABLE` steps, transaction-per-migration, version advanced atomically. `rebuild.py` reads `row['enriched']`; the rename has to be done in the same change as the column update.

---

## Layer 2: Concept graph

### Desired outcomes

- A post can be evidence for a concept, and a concept can be evidence-driven (machine-discovered) or human-curated (named explicitly).
- "What ideas are recurring across my sources?" becomes a query, not a memory exercise.
- The `questionable` overload collapses cleanly: a clickbait post that's evidence for "let-it-cook" can live attached to that concept, and the viewer shows me the high-signal posts within a concept first.
- The graph grows organically over time — new posts attach to existing concepts when they fit, and new concepts emerge when posts cluster in ways that don't match anything yet.
- I (the human) can name, merge, split, and kill concepts. The system suggests; I curate. **Provenance is preserved**: which discovery pass (and which persona, model, run) surfaced a relationship is recorded and queryable.
- Some passes are blind to existing structure (topics, prior concepts) so we keep finding non-obvious threads instead of just reinforcing the categories we already drew.
- The most expensive discovery pass (latent) doesn't run against partial data, because clever threads found in noise are worse than no threads at all.

### Shape

Four tables structure the graph (one new, one renamed/restructured, two as before):

```
concepts (
    id          INTEGER PRIMARY KEY
    name        TEXT NOT NULL          -- short label, e.g. "routines as higher-order prompts"
    description TEXT                    -- 1-3 sentence explanation
    source      TEXT                    -- 'discovered' | 'curated' | 'merged'
    status      TEXT                    -- 'active' | 'archived' | 'merged-into'
    merged_into INTEGER REFERENCES concepts(id)
    created_at  TEXT
    updated_at  TEXT
)

-- Raw discovery events. Immutable history. One row per (post, concept) discovery event,
-- per source/persona/model. This is where every discovery pass writes.
concept_observations (
    id                   INTEGER PRIMARY KEY
    post_id              INTEGER REFERENCES posts(id)
    concept_id           INTEGER REFERENCES concepts(id)
    role_suggestion      TEXT             -- proposed 'evidence' | 'counter-example' | 'tangential' | 'origin'
    raw_score            REAL             -- discovery-time confidence; NOT comparable across kinds
    score_kind           TEXT             -- 'mechanical-overlap' | 'cosine-similarity' | 'llm-self-report'
    source               TEXT             -- 'mechanical' | 'semantic' | 'latent'
    discovery_run_id     INTEGER REFERENCES discovery_runs(id)
    discovery_persona    TEXT             -- null for mechanical
    discovery_model      TEXT             -- null for mechanical
    status               TEXT             -- 'pending' | 'promoted' | 'dismissed' | 'superseded'
    observed_at          TEXT
    notes                TEXT
)

-- Curated canonical truth. One row per (post, concept) reflecting the human's decision.
post_concepts (
    post_id     INTEGER REFERENCES posts(id)
    concept_id  INTEGER REFERENCES concepts(id)
    role        TEXT NOT NULL            -- 'evidence' | 'counter-example' | 'tangential' | 'origin'
    promoted_from_observation_id INTEGER REFERENCES concept_observations(id)
    notes       TEXT
    promoted_at TEXT
    PRIMARY KEY (post_id, concept_id)
)

-- Batch provenance for discovery runs. Helps with reproducibility, cost tracking,
-- debugging, and noticing when a persona/model is consistently producing noise.
discovery_runs (
    id                     INTEGER PRIMARY KEY
    started_at             TEXT
    finished_at            TEXT
    source                 TEXT          -- 'mechanical' | 'semantic' | 'latent'
    persona                TEXT
    model                  TEXT
    sampling_strategy      TEXT
    blinding_strategy      TEXT
    posts_examined         INTEGER
    observations_created   INTEGER
    notes                  TEXT
)

-- Embedding storage for the semantic discovery pass. NOT built in step 4 (concept schema);
-- the shape is spec'd here so step 6 (semantic) doesn't have to invent it. The content_hash
-- column is the staleness anchor: re-enrichment changes content, which changes the hash,
-- which invalidates the embedding and queues a re-embed.
post_embeddings (
    post_id      INTEGER REFERENCES posts(id)
    model        TEXT NOT NULL          -- e.g. 'voyage-3' or 'text-embedding-3-small'
    dim          INTEGER NOT NULL       -- vector dimension; reject inserts that don't match
    content_hash TEXT NOT NULL          -- SHA-256 of the (segmented) content used to embed
    vector       BLOB NOT NULL          -- via sqlite-vec
    embedded_at  TEXT
    PRIMARY KEY (post_id, model)
)
```

The `(post_id, model)` PK lets us hold embeddings under multiple models simultaneously (e.g., during a model swap), and the `content_hash` lets re-enrichment surface "this post's content changed; its embedding is stale" without re-embedding the whole corpus on every backfill batch.

The existing `post_relations` table from v2 stays for post-to-post edges (`quotes`, `extends`, etc.), but the PK gets fixed to `(post_id_a, post_id_b, relation)` so a pair can carry multiple relations.

### Primary vs secondary (Revision, July 2026)

Multi-label overlap is intentional and stays — a post is "evidence living in relationships," not an atom in one box, and single-valued fields were rejected earlier for flattening real nuance. But experience showed a calibration problem, not a model problem: auto-promotion at a flat cosine threshold made broad concepts act as attractors, and a split-review trigger that counted *total edges* kept firing on merely-popular concepts — so splitting multiplied overlapping edges instead of partitioning anything.

The fix adds one axis without abandoning overlap. `post_concepts.is_primary` (migration 8) marks exactly one edge per post as its **primary home** (partial unique index enforces at most one). Primary edges form a partition of the tagged corpus (one home per post); all other edges are **secondary** tags that keep cross-cutting discovery. `assign_primaries()` derives the primary as the best-fit concept by cosine against each candidate's leave-one-out centroid (so a small concept can't win by self-similarity); manual pins (`[primary-pin]` in `notes`) are respected. `split_candidates()` now measures primary-home count, so a concept that is a secondary tag on many posts but the home of few is not flagged. This is the axis the qualitative `role` column (evidence / counter-example / tangential / origin) is deliberately *not* — role describes the nature of a relationship; is_primary describes which one is the home.

### Why the candidate/canonical split

Four tables instead of one or two is real complexity, but it dissolves several bugs in a single move:

- **Provenance and corroboration are first-class.** Multiple discovery events for the same (post, concept) live as multiple `concept_observations` rows. Three personas independently surfacing the same connection is itself a strength signal — querying `COUNT(*) FROM concept_observations WHERE post_id=X AND concept_id=Y AND status != 'dismissed'` gives corroboration count.
- **Canonical edges are clean.** `post_concepts` is "what I, the human, decided about this pair." Single row per pair, no ambiguity, easy to display.
- **Strength isn't fake-normalized.** `raw_score` + `score_kind` keeps mechanical 1.0 and semantic 0.86 and latent self-reports in their native units. We never compute a misleading aggregate "strength." Ranking decisions look at corroboration count + promotion status, not a fake unified score.
- **Dismissed candidates stay dismissed.** `concept_observations.status='dismissed'` is persistent; discovery passes skip-or-dedupe against it so the same observation doesn't regenerate week after week.
- **Merge handling is local.** When concept B merges into concept A, we flatten in one transaction: rewrite all `post_concepts` and `concept_observations` rows from B to A, set B's `status='merged-into'` and `merged_into=A`. Reject cycles before write (`A→B + B→A` rejected). No recursive CTE at read time, no merge-chain resolution overhead.
- **The original H1 PK bug doesn't exist** — `concept_observations` uses an autoincrement `id` PK, not the composite that was vulnerable to NULL-distinct semantics.

### Three flavors of edge discovery

Each flavor writes rows to `concept_observations` with provenance. A curation step promotes, merges, or dismisses them.

**Mechanical** — Free SQL queries over existing structure:

- Same author posting on related topics.
- Same GitHub repo linked across posts.
- Same person quoted (by name or handle) across posts.
- Same paper or external URL cited.
- Same vocabulary phrase appearing across posts ("let it cook," "FDE," "SOUL.md," etc.).

Output: rows into `concept_observations` with `source='mechanical'`, `raw_score=1.0`, `score_kind='mechanical-overlap'`. Cheap. Deterministic. Runs continuously.

**Semantic** — Embedding-based nearest-neighbor (via sqlite-vec, already anticipated in v2):

- Embed `summary` + relevant slice of segmented content (skipping `partial` / empty-content posts; embedding nothing produces noise). Vectors land in `post_embeddings` (schema above) keyed by `(post_id, model)`, with `content_hash` recorded.
- Re-enrichment compares the new content's hash against `post_embeddings.content_hash`; mismatches mark the embedding stale and queue a re-embed before semantic discovery considers the post.
- For each new or recently re-embedded post, find its top-K nearest neighbors via sqlite-vec.
- Cluster the neighbors via simple proximity (or HDBSCAN if needed) to suggest "this post belongs to cluster Z."
- Existing concepts get embedding-centroids; a new post's distance to those centroids determines fit.

Output: rows into `concept_observations` with `source='semantic'`, `raw_score`=cosine similarity, `score_kind='cosine-similarity'`. Cheap-ish (one embedding call per new or re-embedded post). Deterministic. Finds the *obvious* connections — same topic, similar framing.

**Latent** — Random/blinded LLM passes for non-obvious connections:

- Sample small groups of N posts (5–7 feels right; tune empirically).
- Some sampling biased to draw across different existing topic clusters (maximize cross-category discovery).
- At least one pass is blind to existing topics/concepts/tags — only the post content is shown to the model — to anti-anchor against existing structure.
- Ask the model: "What thread or idea, if any, connects these posts? Name it if there is one. It's fine to say 'no real thread.'"
- Promote named threads to candidate concepts; track which posts the model cited as evidence.

Output: rows into `concept_observations` with `source='latent'`, `raw_score` from model self-report, `score_kind='llm-self-report'`. Expensive per call but the work is the *non-obvious* discovery — semantic similarity wouldn't have found these. Run on a budget (e.g., N batches per week).

**Latent gating.** The latent pass is the most expensive and the most easily misled by partial data — blinded LLM passes against the current 328 empty-content rows would produce clever-sounding hallucinations, not real connections. The latent pass is therefore **blocked from running** until enrichment quality crosses a threshold. The gate is a single SQL check at the start of any latent run.

The gate must be expressed carefully because `dead` is a permanent status. 404s, suspended accounts, login-walled posts, and deleted tweets never become recoverable — they form a permanent floor that re-enrichment work can't reduce. If `dead` rows sit in the numerator (or in the corpus-denominator), the gate becomes structurally unreachable: at current numbers ~10% of the corpus is permanently dead, so even with `partial` and `failed` driven to zero the ratio bottoms out above any reasonable threshold.

The correct gate is therefore expressed against *recoverable* incompleteness only:

```
(partial + failed) / (total − dead) < 5%
```

Numerator: rows that *could* be brought to `ok` with more enrichment work. Denominator: the corpus that *could* theoretically reach full coverage. `dead` is excluded from both sides; it's a fact about the world, not a quality problem we can drive down.

Until the gate opens, mechanical + semantic do the discovery work, and we don't burn budget on threads-from-noise. The gate becomes naturally reachable as the rolling re-enrichment backfill (Layer 1 step 8) chips away at `partial` and `failed`.

### Discovery dimensions

Any discovery pass — but especially latent — has four independent dimensions worth treating as first-class parameters in the function signature, even if v1 defaults each to a single value:

- **Sampling** — which posts the pass looks at this batch. Strategies include random, biased-cross-category (draw from posts in different existing topic clusters to maximize the chance of a non-obvious connection), recency-weighted, concept-adjacent (sample around an existing concept to refine its boundary), etc.
- **Blinding** — what context is *hidden* from the discoverer. The default latent pass blinds existing topic/concept tags to force fresh framing. Other blinding strategies might hide author identity (anti-author-anchoring) or hide post dates (anti-recency-bias).
- **Persona** — the lens the discoverer wears while looking. A `tool-eval`-persona pass surfaces different candidates than a `strategy`-persona pass on the same batch. Personas mirror the reading lenses from Layer 3 — same vocabulary, used at discovery time instead of viewing time. The symmetry is useful: concepts found under persona X tend to be most useful when read through lens X.
- **Model** — which model is doing the looking. Different models bring different priors. Haiku for high-volume cheap sampling, Sonnet for the default discovery, Opus for deep review of high-promise candidates. Treating model as a parameter lets us mix cost tiers without restructuring code.

v1 defaults all four to a single value (random sampling, blind-to-existing-tags, no explicit persona, single model). The `discovery_persona`, `discovery_model`, and `discovery_run_id` columns on `concept_observations` record the values used, so when v1.1 activates diversity the historical data already speaks the same vocabulary. Concretely, the foundation for v1.1 lives in four places: the discovery function signature takes the dimensions as parameters, the schema records them, the curation surface can filter by them, and any LLM prompts used for discovery are templated to accept persona injection. None of that has runtime cost in v1 — it's just shape that doesn't have to be retrofitted later.

### Curation flow

The viewer surfaces `concept_observations` candidates grouped by concept, with their corroboration count, the post they're attached to, and the (source, persona, model) provenance. Curation is three actions, **executed via Cowork chat** (see Write Path below):

- **Promote** — sets the observation's `status='promoted'` and writes a canonical `post_concepts` row.
- **Merge** — merges two concepts; flattens both their observation and canonical rows under the surviving concept; sets `status='merged-into'` on the absorbed concept; rejects cycles.
- **Dismiss** — sets the observation's `status='dismissed'`. Future discovery passes check this to avoid regenerating identical dismissed observations.

Concepts I promote can be renamed and given descriptions during curation. Discovered concepts (`source='discovered'`) get auto-named by the model; human curation often renames.

### What "done" looks like

- `concepts`, `concept_observations`, `discovery_runs`, and `post_concepts` (canonical) tables exist; existing posts have at least one mechanical pass producing initial observations.
- The mechanical pass runs continuously; the semantic pass runs on every new/re-enriched post.
- The latent pass is implemented but gated; remains dormant until enrichment quality clears the threshold.
- The viewer has a "Concepts" view listing active concepts with promoted-evidence counts, corroboration counts on pending observations, descriptions, and quick-jump.
- A post's detail view shows both its canonical concept attachments (curated) and pending observations (suggestions, with provenance).
- Curation works via the chat-mediated write path (see Write Path section).

### Notes / open questions

- How many concepts is "too many"? At some point we stop reading them all. Probably want a "show top N most-active concepts" default with an archive.
- Can a concept "expire"? If no new observation attached to it in 6 months, auto-archive? Lean yes but make it visible — archived concepts are still searchable.
- Suppression scope: when I dismiss an observation, do I dismiss just that observation, or the (post, concept) pair across all future observations from any pass? Probably the latter via a `(post_id, concept_id)` suppression record — but worth thinking through whether that's too aggressive (a future-better-model might surface the same pair with better evidence).

---

## Layer 3: Perspective lenses

### Desired outcomes

- The same post can carry multiple urgencies depending on the lens I'm looking through. The Levie/FDE post being `now` from the hiring lens and `near-term` from the engineering-management lens is the canonical example.
- Switching lenses changes what I see (which posts surface, in what order, with what emphasis) without re-tagging anything.
- The starting vocabulary is small and expected to evolve. I add a lens when I notice myself filtering for one repeatedly.
- One special lens — the **morning lens** — defines the default daily view: "what should I read right now?" answered with a small, fixed-size surface.

### Shape

A `post_perspectives` overlay table:

```
post_perspectives (
    post_id     INTEGER REFERENCES posts(id)
    lens        TEXT NOT NULL           -- 'tool-eval' | 'theme' | 'routing' | 'strategy' | 'zeitgeist' | ...
    priority    TEXT                    -- 'now' | 'near-term' | 'long-term' | null
    notes       TEXT
    PRIMARY KEY (post_id, lens)
)
```

Note: audience-per-lens is **not** in v1. The existing `post_audiences` junction (many-to-many, ~1030 rows for 587 posts) stays exactly where it is — folding it into `post_perspectives` as a scalar would silently destroy the m2m structure. If/when team sharing happens, add a separate `post_perspective_audiences(post_id, lens, audience)` junction at that point.

The existing `priority` column on `posts` becomes the post's "default read" priority — the lens-agnostic answer. `post_perspectives` rows override per-lens. Migration: every existing post gets a single `tool-eval` perspective row using its current priority, and the original `priority` column stays as legacy fallback. We treat this as "overlay" rather than "replace" — the existing structure stays valid, and perspectives layer on top. Cleaner conceptually than a full migration, lower risk during the transition.

**`posts.priority` becomes read-only after migration.** All priority writes — from the enrichment classifier, from `curate.py`, from anywhere — go to `post_perspectives` rows. The legacy column is a read-time fallback only; if it ever gets written again, the two sources drift and `get_effective_priority` silently picks one without flagging the inconsistency. The write-discipline is the thing that keeps the overlay sound; without it, "overlay" quietly becomes "two competing truths."

Drift between `posts.priority` and `post_perspectives.priority` is addressed at the read path: a single helper `get_effective_priority(post_id, lens)` does the COALESCE once, and downstream code never thinks about which column to read.

The framing here is **composition, not inheritance**: a lens doesn't replace what a post is, it adds a way of reading it. Same property applies one level up — personas at discovery time and lenses at reading time share the same vocabulary, so we can grow either side independently. (One caveat the review was right about: with n=1 user, "adding a lens is just config" is a small operational convenience, not the central virtue. The principle still matters — composition keeps the lens system from contaminating post records — but the rhetoric was inflated. We're not optimizing for 100 lenses; we're trying to keep adding the next lens cheap.)

### Starting vocabulary (5 reading lenses + 1 surface lens, expected to drift)

- **`tool-eval`** — "Is this a concrete tool, technique, or repo I should evaluate this week?" Priority skews `now`/`near-term`. Filters to actionable posts.
- **`theme`** — "What concept is this part of?" Used with the concept graph for tracking ideas over time. Priority less central here; concepts matter more.
- **`routing`** — "Who on my team should see this?" Used in tandem with the existing `post_audiences` junction.
- **`strategy`** — "What does this say about where the industry is going, what we should be planning for?" Skews `long-term`.
- **`zeitgeist`** — "What's the field talking about right now, even if I don't personally need it?" Captures momentum and signal-tracking distinct from actionability.

Plus one special lens that defines the daily output:

- **`morning`** — The default daily surface. Not a category posts get tagged into manually; the morning view is *computed* from the other lenses and the concept graph. See "The morning lens" below.

Posts can carry multiple perspective rows. Posts without a relevant row in a given lens simply don't show in that lens's view (or show in a "uncategorized for this lens" bucket).

### The morning lens

The system's reason to exist is answering "what should I read right now?" with a small, fixed-size surface. The morning view ships **right after Layer 1** (it doesn't strictly require concepts yet) and gets richer as Layer 2 lands.

The default morning view has three sections, hard-capped:

- **Read now (3–5 posts)** — High-confidence near-term-actionable posts captured since I last opened the system. Computed from `tool-eval` lens at `now` priority + unread fresh items with high faithful-capture quality. One-line reason per post ("Tool eval • GitHub repo linked • 524K views").
- **Recurring this week (3–5 active concepts)** — Concepts with the most new observation activity in the last 7 days. Each shows the top 2–3 posts attached. Empty until Layer 2 lands; placeholder copy until then.
- **Revisit from last month (1–2 posts)** — Posts I marked `now` or `near-term` 30+ days ago that I haven't acted on. The "did I actually pay attention to what I said was urgent" check.

Hard caps matter. Attention budgets are violated by infinite-scroll surfaces. If a post earns its way into "Read now" today, something else falls out. The viewer's existing browse/search affordances stay for going deeper — but the morning view is fixed-size on purpose.

Computation lives in `rebuild.py` — generate a small `morning.json` artifact during rebuild, viewer renders it as the landing surface. No runtime computation in the browser.

### What "done" looks like

- `post_perspectives` table exists; existing posts seeded with `tool-eval` rows reflecting current priority.
- Viewer has a lens-switcher in the header. Switching lens re-sorts and re-filters the main view.
- The morning view is the default landing surface when the viewer opens. Hard caps enforced. "Recurring this week" reads from the concept graph once Layer 2 is live; before that it's empty/placeholder.
- Each post's detail view shows all the perspectives it carries with their priorities/notes.
- `get_effective_priority(post_id, lens)` helper exists and is the single read path for priority.

### Notes / open questions

- Lens vocabulary is global for now. If sharing happens, lens overlay per person via a junction table.
- "Read now" cap of 3–5 is a guess. Tune by use; might want different shapes on different days (Sundays heavier on `theme`, weekdays heavier on `tool-eval`).
- How do new posts get auto-tagged into lenses on first capture? Probably: the enrichment pass classifies into all applicable lenses with default priorities; I edit during curation. Worth thinking through what the classifier prompt looks like.

---

## Write path (curation persistence)

The viewer is a static HTML artifact generated by `rebuild.py`. It has no write affordances and shouldn't grow any. **Curation actions persist via Cowork chat.**

The viewer surfaces observations and concepts with their numeric IDs — e.g., "Observation #4823 attaches Post #2057476020454949201 to Concept 'SOUL.md as identity scaffold' with corroboration count 3, from latent run #17 (persona=tool-eval, model=sonnet)." In a Cowork session, I (the human) say things like:

- "promote 4823"
- "dismiss 4824, 4825, 4826"
- "merge concepts 'SOUL.md as identity scaffold' into 'agent identity files'"
- "rename concept #42 to 'agent identity files'"
- "promote all observations from run #17 with corroboration ≥ 2"

A small `curate.py` skill parses these commands, acquires the shared writer lock (see Layer 1), mutates SQLite (updating `concept_observations.status`, inserting `post_concepts` canonical rows, handling concept merges with cycle rejection, etc.), runs `rebuild.py` once at the end of the batch, then commits and pushes the changed files to GitHub before releasing the lock. The push happens inside the batch — not as a separate step — so the canonical state in the repo always matches what's on disk locally. The weekday pull-first sync therefore sees the curation work as part of the canonical state rather than as a divergent local change to reconcile.

This keeps the persistence boundary clean:

- No browser-local state.
- No separate writer service or local API.
- No in-viewer write affordances (no buttons, no form, no JS state machine to fork from the SQLite truth).
- Leverages how I already use the system — curation happens in the same chat where I'm working with the corpus.

The cost is needing Cowork open to curate, which matches reality.

Bulk curation works the same way — higher-level commands ("promote everything from this run with corroboration ≥ 2 that attaches to a curated concept") parse into the same primitives.

---

## What we're explicitly not building (this round)

- **Chrome extension capture path (v2 Workstream 1).** Email relay is fine for now. The extension is a separate effort that doesn't block the curation work.
- **X bookmark import (v2 Workstream 5).** Same — separate effort. Curation should work on the existing email-sourced corpus.
- **Screenshot capture (v2 Workstream 3).** Schema is in place; this design doesn't change anything there. Continue as planned but separately.
- **In-viewer write affordances.** Curation is chat-mediated. See Write Path.
- **A writer service or local API for curation.** Same reason.
- **Semantic embeddings on `partial` / empty-content posts.** Junk vectors in produces junk vectors out. The semantic pass runs only after the targeted re-scrape brings content quality up.
- **Team annotation layer.** Comments, reactions, multi-user lenses. Out of scope until I'm actually sharing this with people.
- **Hosted viewer.** The HTML output stays self-contained and local for now.
- **Cross-corpus federation** (multiple link collections from different sources merged). Out of scope.

---

## Sequencing (rough, not gantt)

Re-sequenced to land the morning surface as soon as Layer 1 makes it possible, so daily value ships before the concept work is mature. Within a step, order is looser.

1. **Unified enrichment + structured thread segments + status overhaul** (Layer 1). Foundation. Build `db/enrich.py` as the shared module. Add `enrichment_status` + `enrichment_version`, conservative backfill (no false `ok`s). Add `post_thread_segments` table and structured thread capture. Add a real migration runner with `schema_version`. Add lockfile + atomic rebuild. Cut daily-sync and catch-up over to the shared module. Update `rebuild.py` to read the new fields (otherwise renaming `enriched` breaks export).
2. **Targeted re-scrape** (Layer 1 finish). Process the ~388 visibly-incomplete posts. Snapshot-before-replace audit; promote new enrichment only if measurably better.
3. **Morning surface** (Layer 3 partial). Ships now because it depends only on Layer 1 + existing topic/priority structure. Define `get_effective_priority`, generate `morning.json` in `rebuild.py`, viewer renders the three sections. "Recurring this week" is placeholder copy until Layer 2 lands.
4. **Concept graph schema + mechanical discovery** (Layer 2 first flavor). Create `concepts`, `concept_observations`, `discovery_runs`, `post_concepts` (canonical), fix `post_relations` PK. Build mechanical discovery queries. Seed concepts I already know I want by hand.
5. **Curation chat skill** (Write Path). `curate.py` for promote/merge/dismiss. Viewer surfaces observations with IDs. The morning view's "Recurring this week" comes alive in this step.
6. **Semantic discovery** (Layer 2 second flavor). sqlite-vec setup, embeddings for posts with usable content (skipping `partial` rows), nearest-neighbor → `concept_observations` writes.
7. **Perspective lenses overlay** (Layer 3 full). `post_perspectives` table, seed `tool-eval` from existing priority, lens-switcher in viewer.
8. **Rolling background re-enrichment.** Weekly batch processing `enrichment_version < current` until corpus catches up. Drives the gate from step 9.
9. **Latent discovery, gated** (Layer 2 third flavor). Activates once `(partial + failed) / (total − dead) < 5%` — recoverable incompleteness only; `dead` is permanent and excluded from both sides of the ratio so the gate stays reachable. Single-persona / single-model to start. See Layer 2 "Latent gating" for the rationale.
10. **Refinement.** Once everything is live for a few weeks, lens vocabulary, discovery cadences, morning-view caps, gate threshold, and curation UX all get revised based on actual use.

### v1.1: Activating persona and model diversity in discovery

Not a question of *whether* to do this — we already know multi-persona / multi-model discovery improves the latent pass. The question is *when*, and the answer is "after v1 has been running long enough that we have a felt sense of where the basic discovery is leaving gaps."

The plan:

1. **Define a starter persona set** matching the reading lenses. Each persona is a small system-prompt fragment — "you are reading these posts as someone who's evaluating tools to ship this week," etc. Start with the same 5 names as the reading lenses; expect drift.
2. **Define model targets.** Probably three tiers: Haiku for high-volume sampling, Sonnet as the default discovery model, Opus for "deep review" runs on the highest-strength candidates. Tier assignment is a config, not code.
3. **Update the latent pass to vary `(persona, model)` across batches.** Same sampling, same blinding — just multiple (persona, model) combinations producing rows that all land in `concept_observations` with provenance recorded against `discovery_runs`.
4. **Add a promotion pass.** Opus reviews high-strength or high-corroboration candidates across recent runs and proposes promotions for human review. This is itself a discovery dimension — "model=Opus, persona=curator" — using the same machinery as everything else.
5. **Add curation-surface filters by persona/model.** Useful for noticing if certain personas always produce noise, or if model X consistently surfaces threads model Y misses.

The reason this is "plan" not "question": every piece above is additive. The schema already records persona/model. The function signature already takes them as parameters. The curation surface already shows provenance. v1.1 is essentially "stop defaulting; start varying." That's a config change supported by deliberate v1 choices, not a refactor.

---

## Glossary

- **Capture** — moment a post enters the DB (via email relay today, eventually extension too).
- **Enrichment** — fetching content, walking thread segments, summarizing, classifying. One code path.
- **Enrichment version** — integer marking which generation of enrichment logic processed a post. Rolling background re-enrichment targets `version < current`.
- **Topic** — the existing taxonomy (`agent-design`, `claude-code`, etc.). Stays as-is. Coarse-grained.
- **Concept / Theme / Thread** — a discovered or curated idea spanning multiple posts. Finer-grained, often emergent. (Settled on "concept" in code; "theme" and "thread" are aliases in conversation.)
- **Observation** — a single discovery event proposing a (post, concept) relationship. Lives in `concept_observations`. Immutable history with provenance.
- **Canonical edge** — the human-curated post-to-concept relationship. Lives in `post_concepts`. One row per (post, concept).
- **Lens / Perspective** — a way of viewing posts. Determines what surfaces, in what priority.
- **Morning lens** — the special lens that defines the default daily surface. Computed from the other lenses + concept activity rather than tagged by hand.
- **Persona** — the lens a discoverer wears while looking. Same vocabulary as reading lenses.
- **Discovery pass** — a process that produces observation rows. Three flavors: mechanical, semantic, latent.
- **Discovery run** — a single execution of a discovery pass. Recorded in `discovery_runs` for batch provenance.
- **Curation** — human review of observations via Cowork chat → `curate.py` skill. Promote, merge, dismiss.
- **Raw score** + **score kind** — discovery-time confidence + what kind of score it is. Not normalized across kinds.
- **Gate (latent)** — the enrichment-quality threshold that blocks latent runs until met.

---

## Open questions / things to evolve as we go

These are not blockers — they're things to revisit once we have data:

- **Lens vocabulary.** Start with 5 (+ morning), expect drift. After 2 months of use, which lenses do I actually switch between?
- **Concept naming convention.** Short labels vs sentence-like? Auto-generated names vs human-edited? Probably model proposes, I edit.
- **Embedding model.** Local (sentence-transformers via Python) vs API (Voyage, OpenAI, etc.). Trade-off is cost vs offline availability. Affects sqlite-vec dimension choice.
- **Cost budget.** What's an acceptable monthly token spend on latent discovery (once the gate opens)? Probably want a soft cap with a warning.
- **Latent gating threshold.** Picked `(partial + failed) / (total − dead) < 5%` — recoverable-incompleteness ratio, with `dead` excluded from both sides (it's a permanent floor, not a quality problem). The 5% number itself might need tuning by use; the *shape* of the formula is the thing that has to stay right. If it ever felt too loose, the right adjustment is "and ≥ N posts total under each persona" or similar, not putting `dead` back into the calculation.
- **Morning view caps.** 3–5 / 3–5 / 1–2 are guesses. Tune by use; might want different shapes on different days.
- **Suppression scope.** When I dismiss an observation, do I dismiss just that observation, or the (post, concept) pair across all future observations from any pass? Probably the latter via a `(post_id, concept_id)` suppression record, but worth thinking through whether that's too aggressive.
- **Concept lifecycle.** Auto-archive after N months of no new observations? Or just leave them and let the viewer hide low-activity ones by default?
- **Cross-lens conflicts.** If `tool-eval` says `now` and `strategy` says `long-term`, the default-read shows what? Lean "current viewer mode dominates" via `get_effective_priority`.
- **Sharing.** If/when I share this with the team, do lenses fork per-person, or shared default with personal overlays? Out of scope for now but worth keeping in mind.

---

## Closing

The thing this design is reaching for, more than anything specific to threading or concepts or lenses, is **organic growth without locked-in taxonomy, with honest representation of what we actually know vs what we've decided.** The current system is rigid: posts get topics, topics are fixed, priority is one number, `enriched=1` lies about quality. This version lets the structure emerge from the corpus and from how I actually use it, separates raw observations from curated truth so provenance is preserved, gates expensive discovery on data quality so we don't fabricate connections from noise, and pins the persistence boundary at the chat-as-write-surface so curation doesn't accidentally grow a backend.

If something below turns out to be wrong, that's fine — it should be wrong in ways we can see and fix, not in ways the spec forces us to live with.
