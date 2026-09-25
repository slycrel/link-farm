# AI Links Collection — Project Context

This folder contains Jeremy's curated collection of AI-related links, sourced from emails he sends himself (X/Twitter posts, articles, tools) and organized with rich metadata.

## ⏳ Open work queue (resume here — as of 2026-08-26)

**The queue is EMPTY.** Both known-bad data populations are closed, and the last stray capture (item 1a) landed on 2026-08-26. Every post in the corpus is now `ok` (763) or `dead` (73) — **zero `partial` / `failed` / `unattempted` / `legacy-ok`**, so `ai-links-backfill` no-ops until new mail arrives. Everything below is *detected by query*, so nothing depends on remembering a list.

**1. Legacy description-blob content — ✅ CLOSED 2026-08-24.** All 236 are done; the detector below now returns **0**. A capture-logic vintage from roughly March–May 2026 wrote an editorial *description* into the `op` segment instead of the post's actual text, shaped `Author @handle. <description>. 7.4M views. topic1, topic2.` All were marked `v1`/`ok`, so they were invisible to `pending_enrichment_ids()`, and all were embedded — meaning a large slice of the semantic layer was voting on concept assignment using paraphrase rather than source text. The detector, kept for regression use:

```python
import sqlite3, re
con = sqlite3.connect('db/ai_links.db')
pat = re.compile(r'\b[\d.,KM]+\s+views\.\s*[a-z][a-z-]*(?:,\s*[a-z][a-z-]*)*\.?\s*$', re.I)
hits = [pid for pid, t in con.execute("SELECT post_id, text FROM post_thread_segments WHERE type='op'")
        if t and pat.search(t)]
```

The fix, for reference if this shape ever recurs: re-scrape with the `ai-links-catchup` extractor (which captures quoted posts and link cards — essential here, since roughly half these were endorsement posts whose whole meaning lived in the quoted article) and re-persist via `record_enrichment` with **existing topics/audiences passed back unchanged**; the goal is content fidelity, not re-tagging. Expect a large `semantic → auto-curate` surge afterwards — that is real content displacing paraphrase, not churn.

Batch log: 2026-08-21 (a) 50 posts → +144 obs, 32 primaries moved. 2026-08-21 (b) 50 posts (2026-03-24 → 2026-04-10) → **+337 obs, 336 auto-promoted, 61 primaries moved**. 2026-08-21 (c) 50 posts (2026-04-11 → 2026-05-05) → **+351 obs, 349 auto-promoted, 68 primaries moved**, plus 5 new mechanical concepts. 2026-08-24 (d) **final batch — 86 posts** (2026-05-10 → 2026-05-22), 85 re-enriched + 1 partial → **+318 obs, 318 auto-promoted, 65 primaries moved**, plus 1 new mechanical `url:` concept. Verified each time: 0 topic/audience drift. Quote-segment recovery was 26/50 in (b), 17/50 in (c), 35/85 in (d).

**Batch-size calibration, revised after (d).** Batches (b) and (c) landed within 5% of each other, which suggested ~340 obs / ~65 primary moves was the fixed cost of a *50-post* batch. Batch (d) ran **86 posts and produced the same ~320 obs / 65 moves** — so the cost scales with how much *new conceptual ground* the batch covers, not with post count. By May the corpus already had dense concept coverage, so most re-enriched posts landed on existing centroids. Don't extrapolate obs-per-post linearly.

**1a. Blocked capture — ✅ CLOSED 2026-08-26. The fix generalizes; read this before fighting a `[BLOCKED: …]` again.** Post `2055064462844219603` (Sam Hogan, *HALO: Using RLMs to build self-improving agents*, X Article, 23.9K views) had resisted five scrape attempts across three runs, every one returning `[BLOCKED: Cookie/query string data]` instead of page text. The earlier diagnosis was right that the post was alive and this was a capture failure, but wrong about the trigger: it is **not** payload-shape dependent. Two more `javascript_tool` attempts on 2026-08-26 were blocked identically — first with URLs in the returned JSON, then with every URL and query-string pattern scrubbed out of the payload. The guard fires on the *tool*, not on what the tool returns.

**What worked: `get_page_text` instead of `javascript_tool`.** One call returned the entire 14K-char article cleanly — full body text, view count, and the inline `github.com/context-labs/halo` + original-post links. Re-persisted via `record_enrichment` with topics/audiences passed back unchanged (`agent-design`, `dev-practices`, `research` / `me`, `dev-team`), views corrected 15K → 23.9K, and three segments (op + two `external_link`). It homed on concept #19 *agent harness engineering* on the next pass — the correct home, and a clean confirmation that the recovered text displaced the paraphrase rather than just adding noise.

**Generalized rule:** when `javascript_tool` returns `[BLOCKED: Cookie/query string data]`, do not retry it with a reshaped payload and do not conclude the post is dead — **fall back to `get_page_text`.** It reads the article element directly and is not subject to the same guard. Worth trying as the *first* move on X Article URLs, which is where this shape has shown up. The `ai-links-catchup` extractor's richer segment capture (quotes, link cards) is still preferable when `javascript_tool` works; `get_page_text` is the fallback that trades segment structure for actually getting the text.

**Content note from batch (b):** roughly a dozen of those 50 turned out to be the same conversation — *harness engineering* (Rohit's 8,000-word piece, Viv/LangChain's "Better Harness" eval hill-climbing recipe and its three separate endorsers, Akshay's vendor-by-vendor "Anatomy of an Agent Harness", Ramp's "the models are good enough, the harness isn't", Alpha Batcher's principles extracted from the Claude Code leak, AutoAgent). The blobs had flattened all of these into generic paraphrase, so the cluster was invisible to the semantic layer. Concept #19 *agent harness engineering* picked up 17 edges on the very next run. This is the clearest evidence so far that the blob population isn't just cosmetically wrong — it was actively suppressing real structure.

**Content note from batch (d), the May cohort.** May's blobs were dominated by two veins the paraphrase had flattened. First, an **agent-harness / context-economy** cluster that continues the batch (b) finding: OpenAI's harness-engineering writeup on building a ~1M-line internal product with Codex, elvis's 100+ page *Code as Agent Harness* survey (arxiv 2605.18747, four required properties — executable, inspectable, stateful, governed), Amar Singh's *Model-Bound versus Harness-Bound* ("the smarter the models become, the more expensive it becomes to waste their intelligence"), Vasilije's *Memory isn't a plugin. Skills aren't a plugin. They're the same harness*, Mike Piccolo's month-six failure taxonomy via Rohit Ghumare, and a `walkinglabs` harness-engineering course. Second, an **agent-memory / continual-learning** cluster: Tencent's open-sourced memory system (61% token cut, persona consistency 48%→76%), Neo4j `agent-memory`, Garry Tan's GBrain 8-layer knowledge OS, NanoResearch's three co-evolving layers, fast-slow training, On-Policy Self Distillation, and Google's *Nested Learning*. Both were largely invisible before this batch. Also of note: the May cohort is where **`questionable`-packaged posts most often carried real primary sources** — Boris Cherny's Claude Code session, Anthropic's own large-codebases blog post (cited independently by @charmaine_klee and @claudedevs), the GitHub GH-600 certification, and Airbnb's agentic-coding lecture all arrived wrapped in ALL-CAPS hooks.

**2. Unverified `dead` tombstones — ✅ CLOSED 2026-08-21.** All 73 `dead` posts are now individually scrape-verified; `SELECT COUNT(*) FROM posts WHERE enrichment_status='dead' AND enrichment_attempts=0` returns **0**, and every one carries a real marker in `enrichment_last_error`.

History: an audit on 2026-08-21 found 58 of 78 `dead` posts at `enrichment_attempts=0` with no recorded error — bulk-tombstoned, never scrape-tested. Of the 10 outside January, **5 were fully alive** (Kpaxs 521.7K views, Josh Kale 285.8K, hunvreus 95K, ericksky 47.6K, 0xSero 18K) and were resurrected. That 50% false-positive rate is what motivated probing the rest.

The January sweep found the opposite result: **48 of 48 genuinely gone** (46 "page doesn't exist", plus the pre-noted Daniel San handle-mismatch case). Five non-January stragglers were also closed out — 2 deleted, 3 suspended accounts. Net: **0 resurrections in January, 5 outside it.**

Three findings worth keeping:

- **`enrichment_attempts=0` overcounted the problem.** 10 of the 48 January posts already carried hand-written "confirmed deleted as of 2026-03-19" notes — verified in March, just never run through `db/enrich.py`. The audit metric measures *whether the write path was used*, not *whether anyone looked*. Both cohorts have now been re-recorded through `record_dead()` so the metric and reality agree.
- **The Jan 3–16 dead zone is real and total, not a scraping artifact.** Its 100% death rate is a genuine property of that window, and is qualitatively different from the scattered non-January tombstones where half were false. Do not generalize the 50% false-positive rate to it.
- **A mismatched handle in a status URL is harmless.** Several January rows have a URL handle disagreeing with the stored handle (`@tom_doerr` vs `tom_dorr`, `@svpino` vs `santiagoemeli`, `@omarsar0` vs `elvisnguyen`). Verified directly: `x.com/wronghandle12345/status/<valid-id>` 302s to the correct handle and renders. X ignores the handle segment — only the status ID matters, so a mangled handle is never the cause of a 404 and is not worth chasing as a repair path.

**Verification method, for whoever reruns this.** Interleave known-live control posts through the sweep (before, during, after). X rate-limiting and genuine deletion both produce empty `<article>` lists, and the controls are what separate them — all three controls here rendered full content, which is why 53 consecutive failures could be trusted rather than treated as throttling. Also retry a sample using the *stored* handle, not just the URL handle.

The remaining remediation follows this tail: `post_enrichment_pipeline()` → rename any `[auto-named]` concepts → pull-rebase → push per the GitHub Backup section below.

## What This Collection Is For

**Primarily Jeremy's own research corpus, secondarily a sharing artifact** (Jeremy, August 2026). It began as a curation project to share with the TaxHawk team, but in practice only a few people have read it a couple of times. The working assumption is now: this is Jeremy's personal research library, and the `audience` tags are a convenience for the occasional share rather than the organizing principle.

**Consequence for intake — keep what he sends.** Anything Jeremy pushes through the iPhone share sheet is a deliberate act and is presumed intentional. Do not drop a link for being off-topic, low-brow, or hype-packaged. Tangential material earns its place: persuasion and sales content, creator-economy and indie-studio material, writing craft, business logistics. Jeremy's example — a Tony Robbins sales tape is genuinely useful to a friend weighing whether an AI-enabled solo game studio is viable, and dismissing it as marketing throws away the insight with the packaging.

The intake filter should therefore drop only **true noise**: Sentry alerts, receipts, shipping notifications, family mail, car listings — things that are not links Jeremy is collecting at all. Everything else gets enriched and tagged, then judged with full content in hand. The bar is "would I be embarrassed by the *tagging*," not "would I be embarrassed by the *content*" — a hype-farmed post tagged `questionable` is honestly labeled and fine to keep; an unlabeled one is the actual problem.

## How It Works

Jeremy emails himself links from his phone (slycrel@gmail.com → jstone@taxhawk.com) using iPhone's share sheet. The subject line is typically "Post by [Author] on X" with the URL in the email body. Sometimes he modifies the subject to flag importance — treat modified subjects as a signal worth noting.

## Files

- **db/ai_links.db** — SQLite database. Single source of truth for all posts. All capture paths write here; all output artifacts are generated from it.
- **db/migrate.py** — One-shot rebuild-from-JSON bootstrap script. Used only when rebuilding the DB from `posts_final_v3.json` from scratch. **Not** the runner for incremental schema changes.
- **db/migrate_runner.py** — Incremental schema migration runner. Transactional per-migration, idempotent, advances `schema_version`. Add a new migration here whenever the schema needs to change. Currently at version 9 (v8 added `post_concepts.is_primary` — the primary/secondary axis; v9 added `gate_history`, a per-run snapshot of the latent-gate ratio).
- **db/enrich.py** — Canonical persistence layer for enrichment work. All writers (sync, catch-up, curate) go through these helpers — never write directly to `posts.enriched`, `posts.content`, or `posts.summary`. Exposes `record_enrichment` / `record_partial` / `record_failed` / `record_dead`, work-queue queries (`pending_enrichment_ids`), and `gate_ratio` for the latent-discovery threshold.
- **db/concepts.py** — Concept-graph layer (Layer 2). Concept lifecycle (create/merge/archive/rename), observation lifecycle (record/promote/dismiss/bulk_promote/bulk_dismiss/filter), mechanical discovery passes (shared external URLs, shared @mentions), semantic discovery (concept-centroid matching via embeddings). Also holds `auto_curate()` (unattended conceptual-preference triage — see below), `discover_orphan_clusters()` (the only pass that creates *new* concepts from theme — see the orphan-clustering section below), `assign_primaries()` (derives each post's single primary concept — see the primary/secondary note below), and `split_candidates()` (advisory large-*home* flag, threshold `SPLIT_CANDIDATE_MIN_POSTS`, default 60, measured on primary posts). CLI: `python3 -m db.concepts {list,pending,promote,dismiss,merge,discover,semantic,stats}`. Curation surface: chat-mediated via the `ai-links-curate` skill.

  **Primary vs secondary (Jeremy, July 2026).** Concept membership is intentionally many-to-many — a post can carry several concept edges (overlapping *secondary* tags aid cross-cutting discovery, and are explicitly fine). But exactly one edge per post is its **primary** home (`post_concepts.is_primary=1`, enforced by a partial unique index). Primary edges form a partition of the concept-tagged corpus (one home per post); everything else is secondary. `assign_primaries()` derives the primary as the post's best-fit concept by cosine against each candidate's *leave-one-out* centroid (single-edge posts trivially home there; manual pins via the `[primary-pin]` marker in `notes` are respected). It runs as pipeline step 3.6 (after auto-curate, before rebuild). Consequence for split-review: concept "size" is measured on **primary** count, not total edges — so a broad-but-popular concept that's a secondary tag on many posts (e.g. "Claude Code setup & usage": 33 homes but 95 total edges) is not flagged as oversized. This resolves the earlier churn where splitting a merely-popular concept just multiplied overlapping edges.

  **`[primary-pin]` was broken until 2026-09-01 — a pin deleted the home it was meant to protect.** Pinned posts were `continue`d out of the scoring loop *before* being added to `chosen`, but the write step does `UPDATE post_concepts SET is_primary=0 WHERE is_primary=1` and then re-sets only what's in `chosen`. So every run silently stripped the primary off exactly the posts a human had hand-filed. It stayed latent because the corpus had **zero** pinned posts until the first one was created that day (`pinned_skipped` was 0 in every prior run). Fixed by carrying the pinned concept into `chosen`; regression coverage is `PrimaryPinIsHonoured` in `db/test_roles.py` (4 tests — pin keeps *a* primary, pin beats the better-scoring candidate, pin survives repeated runs, and `respect_pins=False` still falls back to cosine). Verified the tests fail against the old behaviour before re-applying the fix.

  **Why the first pin was needed — the discriminative-centroid problem, in the sharpest form seen so far.** Adding a 14K-char X Article (lauren/@poteto, *The Complete Guide to pstack Pt. 1*, post `2094457600259842065`) produced **20 evidence edges in one pass**, and the leave-one-out scores across all 20 candidates spanned **0.8680 → 0.8585 — a total spread of 0.0095**. The winner (#2 *agent identity files*) beat #55 *local model serving on consumer GPUs* by **0.0012**, and the topically correct home, #19 *agent harness engineering*, ranked **dead last**. At that spread the ranking is numerically meaningless — it is measuring the shared "AI stuff" direction, not fit. This is the same pathology CLAUDE.md already flags (175 of 946 centroid pairs above 0.99 cosine) and is strong support for the proposed experiment: **mean-center the semantic pass the way orphan clustering already does.** Long documents look like the worst case, since more text pulls a post closer to the corpus mean and flattens the ranking further.

  **Curation preference (Jeremy, July 2026):** favor *conceptual* categories (themes/ideas) over *per-person* ones. Per-person concepts (`mention:@handle`, names carrying a `(@handle)` tag) and raw `url:` groupings are kept but not actively grown — don't route new evidence into them when a conceptual home exists. `auto_curate()` encodes this: it auto-files semantic matches at/above `AUTO_PROMOTE_MIN_COSINE` (default 0.82) as *secondary* tags on active *conceptual* concepts, dismisses conceptual matches below that floor (the recall band — no longer reviewed by hand), and dismisses low-signal `mention:`/`url:` groupings and per-person duplicates whose post is already conceptually covered. Overlapping conceptual tags are fine and expected — no dedup forced. Since primary is derived separately (`assign_primaries`) and split-review counts primaries, generous secondary auto-filing is safe. The human curate queue is now reserved for structural decisions (merges, naming, per-person groupings not yet covered), not routine semantic tagging.
- **db/subject_flags.py** — Subject-flag extraction. Lifts the trailing-parenthetical importance flag Jeremy adds to email subjects (`Post by X on X (read for work)`) into `posts.notes` as a searchable `flag: <text>` fragment. Idempotent and non-destructive (never clobbers existing curation notes; re-running is a no-op). Runs automatically as step 0 of `db/pipeline.py`, so every sync/catch-up/backfill captures new flags. Fully custom subjects (e.g. "Local code review") are left alone — those are Jeremy's own titling, not flags, and stay in `posts.subject`. CLI: `python3 -m db.subject_flags [--dry-run]`.
- **db/embeddings.py** — Semantic embeddings via fastembed + numpy. Default model `BAAI/bge-small-en-v1.5` (384-dim, ONNX, local). Embeds posts in `ok`/`legacy-ok` status (skips partial/dead — junk in produces junk vectors). `content_hash` invalidation so re-enrichment doesn't require re-embedding the whole corpus. CLI: `python3 -m db.embeddings {status,embed,neighbors,centroids}`.
- **db/filing.py** — Abstain-aware filing classifier (Sept 2026). A *review instrument*, not an auto-filer: it scores each post against a bounded candidate set on **mean-centered** vectors and **abstains** when the top-two margin is thin, instead of always naming a winner the way `assign_primaries()` must. Motivated by a measurement — on 442 multi-candidate posts, **86% of raw filing decisions land inside a 0.01 cosine margin**, i.e. most primary homes are coin flips with a confident number attached. Centering lifts the median margin ~16x (0.0014 → 0.0222). **Bounding matters as much as centering:** centered-but-unbounded scoring *increases* homes landing on tiny `url:`/`mention:` groupings (raw 18 → 25), because a 2-member centroid is sharp and idiosyncratic; bounding to conceptual concepts drops it to 4. All thresholds are **centered** cosines, not comparable to the raw `SEMANTIC_*` constants. `ABSTAIN_MARGIN` defaults to 0.03, the swept point where the classifier proposes *zero* reassignments and becomes purely additive. An abstention is a **no-op, never an un-homing**. Contains no dismissal path (enforced by test). CLI: `python3 -m db.filing {report,review,apply}`; `apply` is dry-run unless `--confirm`. Tests: `db/test_filing.py` (12). Surface: the `ai-links-filing` skill.
- **db/lock.py** — Shared writer lock. Advisory whole-file lock via `fcntl.flock` on a persistent lockfile (`db/.writer.lock`); the kernel auto-releases on process exit/crash, so stale locks can't accumulate (this matters because the cowork mount denies `unlink`). Every writer (sync, catch-up, curate, rebuild) acquires this before mutating SQLite or running rebuild. Regression tests in `db/test_lock.py`.
- **db/rebuild.py** — Rebuild script. Queries SQLite and regenerates all output artifacts below. Atomic temp-file-and-rename writes. Acquires the writer lock by default; pass `with_lock=False` when calling from inside another writer that already holds the lock.
- **posts_final_v3.json** — Generated JSON export (backward-compatible). Array of post objects. No longer the source of truth — generated from SQLite.
- **ai_links_collection_v3.html** — Generated self-contained dark-mode HTML viewer. Inline CSS/JS, no external dependencies. Has search, topic/priority/audience filter pills, list view with expandable cards, card grid view, and topic grouping. The `const POSTS = [...]` array in the `<script>` tag is regenerated by the rebuild script.
- **ai_links_collection_v3.md** — Generated markdown companion with topic distribution table, quick reference (50 most recent), by-topic sections, and full chronological list.

## Data Architecture

**SQLite is the source of truth.** JSON, HTML, and Markdown are generated artifacts. The rebuild script (`db/rebuild.py`) regenerates all outputs from SQLite after any data change.

### SQLite Schema (db/ai_links.db)

```sql
posts (
    id                          INTEGER PRIMARY KEY,  -- deterministic: X status ID or URL hash
    date                        TEXT NOT NULL,
    author                      TEXT,
    handle                      TEXT,
    subject                     TEXT,
    url                         TEXT,
    summary                     TEXT,
    content                     TEXT,                 -- joined segment text (segments are the structured source)
    source_type                 TEXT DEFAULT 'tweet',
    views                       TEXT,
    notes                       TEXT,
    enriched                    INTEGER DEFAULT 0,    -- legacy boolean; superseded by enrichment_status
    image                       TEXT,                 -- path to screenshot PNG
    priority                    TEXT DEFAULT 'near-term',  -- legacy; read-only post-migration, writes go to post_perspectives
    source                      TEXT DEFAULT 'email', -- email, bookmark, both
    bookmarked_at               TEXT,
    created_at                  TEXT,
    updated_at                  TEXT,
    -- Enrichment status (migration 002, June 2026)
    enrichment_status           TEXT DEFAULT 'unattempted',  -- ok | partial | failed | dead | legacy-ok | unattempted
    enrichment_version          INTEGER DEFAULT 0,           -- generation of capture logic; bump in db/enrich.py when shape changes
    enrichment_attempts         INTEGER DEFAULT 0,
    enrichment_last_error       TEXT,
    enrichment_last_attempt_at  TEXT
)
post_topics    (post_id, topic)                                 -- many-to-many
post_audiences (post_id, audience)                              -- many-to-many
post_relations (post_id_a, post_id_b, relation, notes)          -- PK is (a, b, relation) so a pair can carry multiple relations
post_thread_segments (post_id, ordinal, type, handle, text, url, captured_at)  -- structured thread capture; type in {op, self_reply, quote, external_link}
link_checks    (post_id, checked_at, status, notes)             -- future: link health
posts_fts      (FTS5 virtual table over posts)
schema_version (version PK, applied_at)                         -- incremental migration tracking
```

**Enrichment status semantics:**
- `ok` — fully enriched at the current `ENRICHMENT_VERSION` (in `db/enrich.py`).
- `partial` — capture tried, no usable content (empty article). Recoverable: re-enrichment will retry.
- `failed` — outright scrape failure (Chrome unreachable, exception). Recoverable.
- `dead` — confirmed permanent (404, suspended, deleted, login-walled). Never retried; forms the permanent floor in the latent gate calculation.
- `legacy-ok` — pre-migration enriched posts with real content + reasonable summary. Treated as `ok` for reading but eligible for rolling re-enrichment at the next `ENRICHMENT_VERSION`.
- `unattempted` — never tried (default for newly-inserted rows).

**Latent gate formula** (in `db/enrich.py` as `gate_ratio()`): `(partial + failed) / (total - dead) < 0.05`. `dead` is permanent and excluded from both numerator and denominator so the gate stays reachable.

### JSON Export Schema (backward-compatible)

```json
{
  "date": "2026-03-16",
  "author": "Author Name",
  "handle": "@handle",
  "subject": "Post by Author Name on X",
  "url": "https://x.com/handle/status/1234567890",
  "summary": "1-3 sentence summary of the content",
  "topics": ["agent-design", "claude-code"],
  "audience": ["me", "dev-team"],
  "priority": "near-term",
  "sourceType": "tweet",
  "views": "188.8K",
  "notes": "",
  "enriched": true
}
```

Additive fields (included when non-empty): `content`, `image`, `source`.

### Deterministic IDs

Post IDs are derived from the URL — not autoincrement. For X/Twitter posts, the status ID from the URL is used directly (e.g., `2034717504505823728`). For non-X URLs, a SHA-256 hash of the normalized URL is truncated to a 48-bit integer. This ensures the same URL always produces the same ID regardless of import order.

## Topics

- **agent-design** — AI agents, agentic workflows, multi-agent systems, orchestration, tool use, A2A
- **claude-code** — Claude Code CLI, Anthropic products, Claude models, Cowork, Claude-specific tips
- **dev-practices** — Testing, CI/CD, code review, refactoring, debugging, git, deployment
- **skills-mcp** — MCP protocol, skills/plugins, tool integration, MCP server development
- **prompting** — Prompt engineering, system prompts, chain of thought, reasoning techniques
- **research** — Papers, benchmarks, training methods, fine-tuning, alignment, academic work
- **industry** — Startups, funding, acquisitions, product launches, market analysis
- **management** — Team leadership, hiring, productivity, engineering culture, AI adoption strategy
- **adjacent** — Not about engineering, useful anyway. Persuasion and sales, writing and communication, negotiation, pricing, creative craft, career and life-logistics material that informs how the technical work gets used or sold. The test is "would I want to find this again," not "is this about code."
- **solo-operator** — The business and craft of building alone or very small: indie studios, side hustles, one-person-does-what-took-a-team, the practical realities of going independent. Frequently overlaps `adjacent` and `industry`; tag all that apply.
- **biohacking** — Health, cognition, and longevity as things you deliberately intervene in: nootropics and cognitive enhancement, peptides and compound protocols, supplements, sleep and recovery, longevity and biotech progress. Added August 2026 to give a real home to a vein that had been accumulating in `general` — the material is not about engineering and does not need to be. Note that much of it is self-reported, vendor-adjacent, or compiled from forums rather than trials; pair with `questionable` when the *evidence* is thin or the post is a funnel to a paid product, and say so in the summary. Some of these compounds are prescription-only or legally grey depending on jurisdiction — describe what a post claims, attribute the claim to its author, and don't restate dosing guidance as fact.
- **questionable** — **A credibility signal, not a relevance signal.** Engagement farming: ALL CAPS hype, "BREAKING", scarcity hooks ("save this before it's gone"), listicles with fire emojis, engineered outrage. It marks *how the content is packaged*, and says nothing about whether the post belongs in the collection. Hype-packaged posts frequently contain real substance — keep every relevant topic tag alongside `questionable`, and never let the tag alone drive a post to `long-term` or imply it should be removed.
- **general** — Fallback when no strong topic signal

## Audience & Priority

Audience: `me` (Jeremy), `dev-team` (engineering), `leadership` (strategy), `team` (general sharing).

Priority: `now` (directly actionable), `near-term` (explore soon), `long-term` (research/future).

## Automation

### Scheduled Sync (ai-links-sync)

Runs weekday mornings at 9 AM (Cowork scheduled task `ai-links-sync`). Pulls the canonical link-farm clone from GitHub first to absorb anything another runner pushed, then checks Outlook for new emails from slycrel@gmail.com, extracts URLs from email bodies, classifies topics using keyword matching, deduplicates, inserts into SQLite, rebuilds outputs, and pushes to GitHub. Can also be triggered manually.

**Pull-first is mandatory.** A separate headless/cloud runner has historically pushed `Sync YYYY-MM-DD` commits to link-farm at ~15:00 UTC on weekdays. Without the pull-first step, Cowork would re-process the same emails against a stale local DB and clobber the cloud runner's topic classifications. With pull-first, both runners converge on the same canonical state — whichever fires first wins, and the other becomes a no-op.

### Catch-Up Skill (ai-links-catchup)

Bulk enrichment tool invoked by saying things like "catch up on links" or "enrich my links." Three phases: (1) backfill missing URLs from Outlook email bodies, (2) scrape post content via Chrome and summarize/reclassify, (3) post-enrichment pipeline (embed + mechanical/semantic discovery + rebuild via `db/pipeline.post_enrichment_pipeline`). Handles all content types: direct posts, quote tweets (unified context), X articles, videos (bookmark only), and follow-up posts with thread awareness for GitHub links.

### Backfill (ai-links-backfill) — campaign complete, task dormant

**The backfill campaign is finished.** It existed to drain a recoverable-incompleteness backlog so the latent-discovery gate (`(partial + failed) / (total − dead) < 0.05`) could open. The gate opened on 2026-08-14 and the queue hit zero on 2026-08-26; every post has been `ok` or `dead` ever since. The task is **disabled** in the Cowork app store (last run 2026-08-03, cron `30 10 * * 1`) and is kept as a dormant tool, not a standing cadence — there is nothing for it to do, and the 9 AM sync already picks up any stray `partial`/`failed` post on the next light day via its own backlog append.

Earlier vintages of this file described it as running weekdays (`30 10 * * 1-5`). That was the drain-the-backlog cadence and is no longer accurate; don't recreate it on a schedule from that description.

**When to wake it up.** If a run of bad scrapes ever rebuilds a real queue — say `pending_enrichment_ids(statuses=('partial','failed'))` returns more than a couple dozen, or `gate_ratio()` climbs back above 0.05 — re-enable the existing task rather than writing a new one. It processes a fixed BATCH_LIMIT (currently 15) of `partial` / `failed` / `unattempted` posts per run via Chrome + `db/enrich.py` helpers, then runs the same `post_enrichment_pipeline` the sync and catch-up skills use. It skips `legacy-ok` posts (they have usable content already — that's a separate concern when `ENRICHMENT_VERSION` bumps) and cleanly no-ops on an empty queue. At 75 posts/week a backlog drains in roughly 3 weeks; slow the cadence back down or disable it again once the gate reopens. The prompt body is snapshotted at `scheduled/ai-links-backfill.SKILL.md`.

### Curate Skill (ai-links-curate)

Chat-mediated curation surface for the concept graph. Invoked by saying "curate links", "promote observation", "merge concepts", etc. Parses natural-language commands and routes them to `db/concepts.py` helpers — promote/dismiss/merge/rename/create concepts, list pending observations, run discovery passes manually, show gate ratio. End-of-batch: rebuild via the shared pipeline + push to GitHub.

### Filing Skill (ai-links-filing)

Chat surface over `db/filing.py`. Invoked by "review filing", "what's badly filed", "run the classifier", "abstain queue". Reports the confident/abstained split, works the abstain queue (unfiled first), and hands structural changes off to `ai-links-curate` — it proposes, it doesn't re-home.

Borrowed from the Contrastive Language Model contract (Akshay Pachaar's explainer, post `2103483160382386234`, added 2026-09-25) **without a trained model** — the useful part was never the speed, it was the shape: supply a finite candidate list, never invent an option outside it, return a typed id *or abstain*. `assign_primaries()` already did the first two.

The signal to look for in the queue is a **negative top score**: the post is anti-correlated with the concept it currently sits in. Raw cosine would report ~0.8 for the same pair and tell you nothing.

Two honest limits: it inherits bge-small's geometry and learns nothing about how Jeremy actually files (a trained head over the ~578 existing home decisions is the untried upgrade), and it **cannot fix a magnet, only reveal one** — a drifted centroid poisons every post scored against it, so run the magnet detector first.

### Edge roles — the weak layer (Aug 2026)

**`auto_curate()` no longer discards anything.** It used to dismiss two large buckets: the sub-threshold semantic "recall band", and raw mechanical `mention:` / `url:` groupings. Jeremy's objection (2026-08-26) is the governing principle now: *every post here is something he deliberately sent himself, so "low signal" is not a high enough bar to decide we never need to think about it again.* Automation records what it found and how much to trust it; only a human calls `dismiss_observation()`, for genuine junk (scams, content-free bait).

`post_concepts.role` carries the caveat. **`CANONICAL_ROLES = ('evidence', 'origin')` are load-bearing**; `weak`, `counter-example` and `tangential` are recorded associations that must not vote on what a concept *means*. Load-bearing is enforced in four places, and all four must stay in sync or generous attachment silently corrupts the graph:

1. `embeddings.concept_centroids()` — only canonical roles feed the mean.
2. `discover_semantic_neighbors()` — a concept needs canonical edges to be scoreable.
3. `assign_primaries()` — only canonical edges can be a post's home.
4. `discover_orphan_clusters()` — "orphan" means *no canonical home*, so a weak-only post stays eligible for a real concept.

Regression tests: **`db/test_roles.py`** (15 tests). It exists because every one of those four is a silent failure if it regresses.

**Measured effect.** Edge-less posts fell from 33% to 8% of the corpus; `adjacent` from 52% to 16%. The old policy was biased — `adjacent` material was ~1.6x likelier than baseline to have no concept edge at all, i.e. the triage cut hardest against exactly the tangential vein the taxonomy was extended to capture. `db/revive_dismissed.py` recovered the history (2,195 edges from 2,630 dismissed observations; 411 correctly skipped as belonging to retired concepts). Verified at the time: all 29 pre-existing centroids **byte-identical** and all 498 primaries **unchanged** — recall rose, nothing downstream moved.

**Three traps, all hit for real on 2026-08-26. Read before touching the thresholds.**

- **The recall band had zero width.** `SEMANTIC_CENTROID_THRESHOLD` (propose at) had been raised to *equal* `AUTO_PROMOTE_MIN_COSINE` (auto-file at) = 0.82, so nothing could ever land between them and no pass could surface an association it wasn't already confident about. Now 0.75 vs 0.82. 0.75 is chosen because this corpus's *pairwise* cosine distribution is mean 0.61 / p99 0.73 — so 0.75 clears the 99th percentile of ordinary similarity. Below ~0.73 that stops being true.
- **An absolute threshold is the wrong instrument for the weak band.** Uncapped, 0.75 proposed **8,825 observations in one run** — ~26% of every possible (post, concept) pair. "Almost everything is weakly related to almost everything" is true and useless. `SEMANTIC_MAX_WEAK_PER_POST = 3` makes a weak edge mean *"one of this post's closest concepts"*. **The cap must be a per-post TOTAL, not per-run** — `already_attached` excludes what a post already has, so a per-run cap just hands out the next-best 3 every time and converges on the same carpet slowly (observed 2024 → 1910 → 1444 before the fix). The evidence band stays uncapped.
- **A hand-created concept from a lexically diffuse cluster becomes a magnet.** #65 was created with 7 chosen members and absorbed 26 unrelated evidence edges and 18 primaries within two runs, because averaging members that share a *purpose* but not a *vocabulary* yields a centroid near the corpus mean, which matches everything — and matches ≥0.82 become evidence, so it feeds on its own diffuseness. Fix: `NO_CENTROID_SCORING_MARKER` (`[no-centroid-scoring]`) in the description. The concept keeps its edges and stays fully browseable; nothing is ever matched *into* it by cosine. **If a concept exists only because a reader could see it, mark it.** — **as of 2026-09-25 this is the default and no longer something to remember; see below.**

**The marker is now opt-out, not opt-in (2026-09-25).** #74 repeated #65 one month later and worse, which settled the question. `create_concept()` (the hand path) and `record_latent_findings()` (the blinded reader pass) both stamp the marker unless the caller passes `centroid_scoring=True`. `discover_orphan_clusters()` is deliberately **not** defaulted — those concepts are derived *from* the embedding geometry and are cohesion-guarded (`ORPHAN_CLUSTER_MIN_COHESION`), so they are vocabulary-coherent by construction and their centroids are trustworthy; marking them would freeze the only pass that grows vocabulary from theme. Regression coverage is `CentroidScoringDefault` in `db/test_roles.py` (7 tests; 3 verified failing against the old default before the change). Helper is `_apply_centroid_scoring_default()`, which is a no-op when the description already carries the marker, so a caller writing its own richer rationale isn't double-stamped.

**The #74 incident, 2026-09-25 — the sharpest version of this failure yet, because it became self-defeating.** #74 *System One models — bounded decisions as a primitive* was hand-seeded 2026-09-24 23:28 with 9 Jev posts, precisely because the semantic layer was scattering that conversation across five unrelated homes. It graduated the same day and within 48 hours held **328 evidence edges (93 on 09-24, 244 on 09-25), of which only 10 concerned Jev / CLM / RLCD.** The rest reached back to 2025-01-04: agent memory, agent factories, eval pipelines, harness recipes. The diagnostic that matters:

| a squarely on-topic CLM explainer scored against | cosine | outcome |
|---|---:|---|
| the original 9 hand-seeded members | **0.8397** | clears the 0.82 floor |
| #74's centroid after absorption | **0.8036** | below floor, rank **6 of 55** |

**A magnet doesn't just over-recruit — it eventually stops recognising its own subject.** That asymmetry is the reason to default the marker rather than rely on spotting diffuseness by eye: by the time the concept is visibly too big, it is already rejecting the posts it was created for. Note also that neither the nursery tier nor graduation caught this; `status`/`is_primary` gating and the marker are **orthogonal**, and #74 fell through the gap between them (graduated on 9 real edges, *then* became a magnet). Remediation was a demote-not-dismiss rollback: 318 edges `evidence → weak` (recorded, reversible via table `_rollback_74_20260925`, no-discard policy intact — last dismissal is still 2026-08-26), marker applied, and the CLM post attached by hand as `source='curated'`. Verification that it worked: the next pipeline run scored 45 concepts instead of 46 and proposed **+0** observations, down from +244 that same day. #74 is now 11 evidence edges, all 11 homed, Sep 16 → Sep 25.

**Detector, if this shape recurs.** A concept whose evidence count vastly exceeds its primary-home count, and whose members' date range far exceeds the span of the conversation it was created for:

```sql
SELECT c.id, c.name,
       SUM(pc.role IN ('evidence','origin'))       AS canonical,
       SUM(pc.is_primary)                          AS homes,
       MIN(p.date) || ' -> ' || MAX(p.date)        AS span
  FROM concepts c
  JOIN post_concepts pc ON pc.concept_id = c.id
  JOIN posts p          ON p.id = pc.post_id
 WHERE c.status = 'active'
   AND COALESCE(c.description,'') NOT LIKE '%[no-centroid-scoring]%'
 GROUP BY c.id HAVING canonical > 40 AND canonical > homes * 10
 ORDER BY canonical DESC;
```

**Known pre-existing issue: concept centroids are barely discriminative.** 185 of 990 centroid pairs sit above 0.99 cosine — several large concepts have effectively converged on the same direction. This predates the role work (141 of 378 pairs were already >0.99 on 2026-08-24, i.e. 37% vs 18.7% now) and is the raw-cosine problem the orphan-clustering note describes: on this corpus everything is "AI stuff", so un-centered centroid similarity is dominated by that shared direction.

**Mean-centering was dry-run on 2026-09-15. It works — but it is not the cause of the big-concept problem.** Recomputing every centroid on mean-centered vectors moves the pair distribution from median 0.826 / 18.7% >0.99 to **median 0.029 / 0.9% >0.99** — a ~20x reduction in spurious similarity, and a strong argument for making the semantic pass centered the way orphan clustering already is. *But* the seven big concepts (#3, #22, #45, #47, #48, #51, #52) survive centering at 0.986–0.993, because the real problem is not geometry:

**They share 84–93% of their members (Jaccard).** They are substantially the same set of posts under seven names, and no reweighting separates sets that are genuinely identical. Root cause is that the evidence band is **uncapped** — `SEMANTIC_MAX_WEAK_PER_POST` (3) caps weak edges per post, nothing caps evidence — so every large concept has slowly accreted most of the corpus as secondary tags. Measured 2026-09-15:

| concept | total edges | evidence | **is home to** |
|---|---:|---:|---:|
| #48 prediction-market & crypto bots | 393 | 346 | **4** |
| #51 context economy | 370 | 334 | **4** |
| #3 Forward Deployed Engineers | 356 | 321 | **6** |
| #47 self-improving skills | 382 | 341 | **20** |

The same seven have **Jaccard 0.00 on their primary sets** — the home layer is a clean partition and was never affected. So the corpus has a healthy organizing layer (541 homes, one per post, largest 61) wrapped in a secondary web that is mostly noise. **Prefer primary-home count whenever you describe or rank a concept.** Capping evidence attachment per post is the untried lever; it needs a backfill decision for the ~4,900 existing evidence edges and has not been attempted.

**Views report homes, not edges (changed 2026-09-15).** `recent_active_concepts()` and `top_posts_for_concept()` in `db/concepts.py` now measure and order on `is_primary`, not on `role IN ('evidence','origin')`. Before this the morning view listed four "different" concepts at 341–346 posts whose recent evidence was *literally the same two posts*; after, it lists five distinct concepts at 52/50/45/44/33 with disjoint shortlists. This is a presentation change only — no edges were altered.

**Source-aggregation was measured and is thin.** Prompted by the idea of grouping posts under a shared source rather than relating them to each other: mining every summary and content blob for GitHub repos, arXiv IDs and HF models finds 124 distinct sources, of which **only 12 are cited by more than one post, covering 24 posts (3.1% of the live corpus)**; 112 appear exactly once. The `external_link` segments agree (12 shared URLs / 23 posts). Jeremy sends one link per thing, so mechanical `url:` grouping has very little material by construction — which is also why the `url:` concepts are the emptiest objects in the graph (#60 `cognee` had 3 evidence edges and 56 total, the other 53 being semantic noise matched *into* a pure source-grouping). Don't invest in growing this axis; do keep cosine from polluting it.

### The provisional tier — a nursery for small concepts (Aug 2026)

**The problem it solves.** The concept graph was bimodal: 26 concepts at 2–3 evidence edges, 4 at 4–9, **zero between 10 and 99**, then 20 concepts at 100+. There was no way to be small and legitimate. The guards (orphan clustering: 4 posts / 3 authors; semantic scoring: 2 canonical edges) meant a theme either arrived fully formed or never — while anything that *did* exist could immediately become a primary home and, if lexically diffuse, a magnet.

`CONCEPT_PROVISIONAL` decouples the two things that were fused: **naming a category** and **being a home for posts**. A provisional concept holds edges and is fully browseable, but:

- it is **not** a candidate primary home (`assign_primaries` filters on `active`)
- it does **not** feed centroids or semantic scoring (both filter on `active`)
- it graduates to `active` automatically at `PROVISIONAL_GRADUATION_MIN_EDGES` (4) **canonical** edges — weak edges don't buy graduation

So a nursery concept is *inert by construction*. That's what makes it safe to name something speculatively: a bad seed can't distort discovery or steal homes, and costs a handful of edges to undo.

**Growth: `discover_provisional_exemplar_matches()`, pipeline step 3.56.** Centroid matching structurally cannot grow a 1–2 member concept — a centroid of one post is just that post's vector, which is exactly why `SEMANTIC_MIN_CONCEPT_EDGES = 2` exists. Two choices carry the weight:

- **Mean-centered vectors.** Raw cosines here have pairwise mean 0.61; a raw neighbourhood around one exemplar matches nearly everything. `PROVISIONAL_EXEMPLAR_THRESHOLD = 0.40` is a *centered* cosine, deliberately equal to `ORPHAN_CLUSTER_THRESHOLD` since both passes work the same geometry. **Not comparable to `SEMANTIC_CENTROID_THRESHOLD`, which is raw.**
- **Max similarity to any single member, not to their mean.** Averaging re-introduces the diffuseness that made #65 a magnet. Scoring against the nearest exemplar keeps a purpose-coherent category workable — a post joins because it resembles *one* thing already there. Capped at `PROVISIONAL_EXEMPLAR_MAX_PER_RUN = 3`.

**Seeded 2026-08-26, and what each demonstrates:**

- **#66 `cognitive enhancement & longevity protocols`** — 5 unhomed `biohacking` posts. Orphan clustering could never form it: 3 of 5 are one author, tripping `ORPHAN_CLUSTER_MAX_AUTHOR_SHARE=0.55`. The nursery has no such guard and doesn't need one. **Graduated on the first pipeline run** (5→6 edges) and now homes 6 posts.
- **#67 `organizational agency — authority taken vs authority granted`** — 2 posts, same author, deliberately below the bar. Still provisional after three runs; exemplar matching found nothing at 0.40. Its nearest candidate is **0.393** — a Dave Kline management post, a near-miss. That's the threshold doing real work: the vein is *adjacent* to management content, not identical, and the tier is holding it honestly at 2 rather than either discarding it or inflating it.

**When to reach for it.** Prefer `status=CONCEPT_PROVISIONAL` for anything you're naming speculatively; it is the low-risk way to add vocabulary. Promote to `active` by hand only if you're confident it should start competing for homes immediately. And note the interaction with `NO_CENTROID_SCORING_MARKER`: a concept that graduates while still being *lexically* diffuse will become a magnet the moment it earns a centroid — #65 is the worked example.

### Auto-curation (daily)

`db/concepts.auto_curate()` runs as step 3.5 of the pipeline (after discovery, before rebuild), so every sync/catch-up/backfill triages the observations discovery just produced. Encodes the conceptual-over-per-person preference (see the `db/concepts.py` note above): auto-file semantic matches ≥ `AUTO_PROMOTE_MIN_COSINE` (0.82) as *secondary* tags on conceptual concepts, dismiss conceptual matches below that floor, dismiss low-signal `mention:`/`url:` groupings and per-person duplicates already covered conceptually. **Semantic triage is fully automated** — the queue self-clears each run, so pending stays ~0 in steady state (as of 2026-07-22; previously the un-reviewed mid-confidence band accumulated into hundreds of stale pending rows). This is safe because auto-filed edges are always *secondary* (primary is derived by `assign_primaries`) and split-review counts primaries, so denser secondary tagging can't retrigger split churn. Manual `ai-links-curate` now handles only structural decisions (merges, naming, uncovered per-person groupings). Note: a large *manual* restructure reshapes centroids and makes the next run's discovery surface a burst of new matches, which auto-file as secondary and settle to a trickle over the next 1–2 runs (a self-resolving convergence surge — e.g. 134 → 4 → ~0).

### Orphan clustering — how the vocabulary grows (Aug 2026)

`db/concepts.discover_orphan_clusters()` runs as pipeline step 3.55 and is **the only pass that can invent a new concept from theme.** It closes a real structural gap: mechanical discovery creates concepts only from *structural coincidence* (a shared external URL, a shared @mention), and semantic discovery scores posts against the centroids of concepts that **already exist**. Neither can propose a category that isn't there yet, so before this the vocabulary could only grow by hand — and 367 of 715 live posts (51%) sat with no concept edge at all. That orphan pile is what produced the `questionable + general` failure mode: the enricher had to pick from a closed list and fell back to `general`, and nothing downstream ever revisited it.

**How it works.** Posts with no `post_concepts` edge are clustered on their embeddings; each tight, multi-author group becomes a new **active** concept with its members attached as *secondary* edges (primary homes are left to `assign_primaries()`, exactly as with `auto_curate()`).

**Why the vectors are mean-centered first.** This matters and is easy to get wrong. Raw bge-small cosines on this corpus have mean 0.61 / p99 0.73 — every post is "AI stuff", so the shared topical direction swamps the differences and absolute-threshold clustering returns *one blob of 366*. Subtracting the corpus mean (the all-but-the-top trick) removes that common direction: mean pairwise drops to 0.008 and real structure separates. **`ORPHAN_CLUSTER_THRESHOLD` is therefore a cosine on centered vectors and is not comparable to `SEMANTIC_CENTROID_THRESHOLD`, which is measured on raw ones.** Don't reuse one number for the other.

**Guards** (all tunable constants in `db/concepts.py`):

- `ORPHAN_CLUSTER_THRESHOLD` (0.40, centered) — tuned against 367 orphans; yields ~7 clusters over ~15% of the pool. Lower to widen the net.
- `ORPHAN_CLUSTER_MIN_SIZE` (4) — below this a "theme" is usually coincidence.
- `ORPHAN_CLUSTER_MIN_COHESION` (0.55) — mean cosine of members to their own centroid; rejects large-but-loose blobs.
- `ORPHAN_CLUSTER_MAX_PER_RUN` (6) — keeps a big first run from creating a dozen concepts at once.
- `ORPHAN_CLUSTER_MAX_AUTHOR_SHARE` (0.55) + `ORPHAN_CLUSTER_MIN_AUTHORS` (3) — enforces the conceptual-over-per-person preference. A 15-post cluster that was 60% one management writer sailed through an earlier 0.70 setting *and named itself after him*; author and handle tokens are now also excluded from the naming vocabulary, since a prolific writer's name is by construction the most distinctive token in their own cluster.

**Naming is deliberately two-stage.** Unattended runs auto-name from crude TF-IDF and mark the description `[auto-named]`. When the pass runs inside a Cowork skill there's a model in the loop, so **rename fresh clusters before finishing** — find them with:

```sql
SELECT id, name FROM concepts WHERE description LIKE '%[auto-named]%';
```

Everything created here is reversible: `archive_concept(id)` retires a cluster that isn't a real theme, and `merge_concepts()` folds a duplicate into an existing home.

**First run (2026-08-14)** created six concepts over 41 posts — *document parsing & extraction tooling*, *self-improving skills (autoresearch pattern)*, *Fable 5 access & usage*, *prediction-market & crypto trading bots*, *elite-skill masterclass content*, *founder philosophy & life-design essays* — and correctly skipped the Dave Kline management cluster on author concentration. None of those six existed in the fixed topic taxonomy; all would have been `general`.

**Relationship to the latent pass.** Orphan clustering is the cheap half of what `CURATION_DESIGN.md` calls latent discovery — it finds themes in the material that fit *nowhere*. The blinded pass (below) is the expensive half, and finds threads that cut *across* categories that already exist.

### Latent discovery — the blinded pass (Aug 2026)

The pass `CURATION_DESIGN.md` specced and nothing implemented for months. Where orphan clustering finds themes in material that fits *nowhere*, latent finds threads that cut *across* categories that already exist.

**It is split in two around the model.** The pipeline is plain Python with no LLM available to it, so rather than calling out to one:

```python
b  = prepare_latent_batch(batch_size=48, sampling='biased-cross-category',
                          blinding='blind-tags-author', model='claude-opus-5')
# ... a Cowork skill run reads b['items'] and proposes threads ...
st = record_latent_findings(b['run_id'], findings, b['key'], model='claude-opus-5')
```

Sampling, blinding, gating and provenance stay deterministic and testable in Python; the expensive judgement happens where a model actually exists. **This pass only runs inside a skill session — it is deliberately NOT in `post_enrichment_pipeline`,** because an unattended pipeline has no reader.

**Blinding is the whole point.** Semantic discovery already tells you what resembles what you have named. Latent exists to find threads that cross those boundaries, so the reader must not see them — otherwise it re-derives your existing taxonomy and reports it back as insight. Strategies: `blind-tags` (hide topics + concept membership), `blind-tags-author`, `blind-tags-author-date`. Posts are handed over as opaque refs (`P001`…) with the ref→post_id map held server-side, so the reader can't look one up and re-acquire the context just hidden.

**Known blinding leak:** summaries frequently name their author inline ("Ole Lehmann shares…"), so `blind-tags-author` is partial at best. Fixing it means either author-stripped summaries or a scrub pass at batch time. Not yet done — treat author-blinding as best-effort.

**Guards.** The gate (`< 0.05`) is enforced at batch time unless `enforce_gate=False`. A finding that proposes a *new* concept must cite at least `auto_create_min_posts` (3) posts; findings that attach to an existing concept have no floor, since corroborating a known idea with two posts is legitimate. Every edge lands secondary; `assign_primaries()` decides homes. Observations carry `source='latent'`, `score_kind='llm-self-report'`, plus run/persona/model, so latent-derived structure stays separable and auditable — `SELECT * FROM concept_observations WHERE source='latent'`.

**Roles.** A finding may set `role` (`counter-example`, `tangential`, `origin`). This is how a reader says "these belong with that concept because they argue the opposite" — e.g. filesystem-as-memory papers attached to *vector / hybrid databases as agent-memory infrastructure* as counter-examples, so the concept carries its own dissent. If the edge already exists with the default `evidence` role, the more specific role is applied; a deliberately-chosen non-default role is never clobbered.

**First run (2026-08-14, run 252, 48 posts, cross-category, blind-tags-author)** produced two new concepts — *context economy — routing tables beat big context* and *agents as constrained software — making bad shapes unexpressible* — grew *Forward Deployed Engineers* and *self-improving skills*, and attached the two counter-examples above. One single-post finding was correctly rejected by the floor. Both new concepts then attracted substantially more evidence on the next semantic run (4→14 and 3→26 posts), which is the convergence surge documented under auto-curation and a decent signal the threads were real.

### Split-review trigger

`db/concepts.split_candidates()` flags active concepts at/above `SPLIT_CANDIDATE_MIN_POSTS` (default 60) as candidates worth vetting for sub-categorization. **Measured on primary-home count, not total edges** (see the primary/secondary note above) — a concept can be a secondary tag on many posts without being an oversized home. Advisory only — surfaced in the pipeline summary (`⚑ split-review candidates: …`), never an auto-split. Overlapping/broad concepts are acceptable; the trigger just keeps a big *home* from quietly accumulating unnoticed. Splitting a merely-popular concept (large total, small home) won't reduce the flag and isn't the intent — split when a *home* conflates distinct threads, as #29 did.

## Rebuilding Outputs

Subject flags: when Jeremy edits an email subject to add a trailing parenthetical (e.g. `(implement!)`, `(read this today)`, `(mgmt)`), that's an importance signal. `db/subject_flags.py` mirrors it into `posts.notes` as a searchable `flag: <text>` fragment, run automatically as step 0 of the pipeline — so it's captured on every sync/catch-up/backfill with no manual step. Search `flag:` in notes to find everything Jeremy has flagged.

Run `python3 db/rebuild.py` (or `from db.rebuild import rebuild; rebuild()`) after any data change. This single script:

1. Queries SQLite for all posts (with topics and audiences joined)
2. Generates `posts_final_v3.json` (backward-compatible export)
3. Replaces the `const POSTS = [...]` array in the HTML viewer (preserving all CSS/JS)
4. Generates the Markdown companion (header, topic distribution, quick reference, by-topic sections, chronological list)

The HTML stats line (date range, counts) is computed dynamically by the viewer JS — no manual update needed.

## Outlook Email Search Notes

- Search by sender `slycrel@gmail.com` only — adding a recipient filter causes older emails to not appear
- Paginate with `limit: 50` and `beforeDateTime` for older results
- Read email bodies with `read_resource` URI: `mail:///messages/{messageId}`
- URLs are in the HTML body, often wrapped in anchor tags
- Strip tracking params (?s=, &t=, ?utm_*) when normalizing URLs
- Deduplicate by normalized URL and by date+author

## Content Types for Scraping

1. **Direct posts** — Standard tweets. Extract text, author, views, linked content.
2. **Quote tweets** — Single context split across elements. Same scraper as direct posts since all content is on one page.
3. **X articles** — Long-form. Follow article link for full text, capture author's introductory commentary.
4. **Videos** — Low priority. Mark as sourceType "video" and bookmark for manual review.
5. **Follow-up posts** — Authors often reply to their own tweets with GitHub links or additional context. Check thread for same-author replies.

## Collection Stats (as of September 17, 2026)

Regenerate these numbers from the DB rather than trusting them blind — they drift between refreshes. The queries are one-liners against `db/ai_links.db`. **`db/stats.py` prints this whole block** (`python3 -m db.stats`) — use it rather than hand-editing, so the numbers and the date stay honest together.

- **890 total posts** in SQLite (live count). Date range: June 11, 2024 – September 16, 2026.
- Enrichment status: **817 `ok`** (current `ENRICHMENT_VERSION=1`), 73 `dead` (permanent floor — deleted/suspended/login-walled). **Zero `partial` / `failed` / `unattempted` / `legacy-ok` — the enrichment queue has been completely empty since 2026-08-26**, which is why the backfill task is dormant (see the Automation section).
- **Latent gate ratio: 0.00% — the gate is OPEN** (open since 2026-08-14; see `gate_history`). With no recoverable-incomplete posts left, the numerator is zero. Latent discovery is available on demand, but only inside a skill session — it is deliberately not in `post_enrichment_pipeline` because an unattended run has no reader.
- Top topics: agent-design (530), dev-practices (383), research (235), skills-mcp (201), claude-code (197), management (139), questionable (136), industry (134), prompting (131), general (100), `adjacent` (45), `biohacking` (8), `solo-operator` (8).
- **Re-tag pass, 2026-08-18.** `adjacent` and `solo-operator` had 1 post each despite being deliberate taxonomy additions. A review of the 151 live `general`/`industry` posts (cross-checked against concepts #45/#50) added 27 `adjacent` and 4 `solo-operator` tags, additively — existing topics were preserved, nothing was retagged away. Root cause was upstream: the *live* `ai-links-sync` scheduled task had drifted to a June vintage carrying the old aggressive intake filter ("filter out non-AI/tech") and no mention of either topic, so the enricher never had them in its working vocabulary. Live task and repo snapshot are now back in sync and both name the two topics explicitly.
- Two known gaps left after that pass, both judgment calls rather than oversights: (a) a **quant-trading / masterclass vein** (concept #45, ~5 posts — Jane Street / Jim Simons / Markov-chain lectures) is non-engineering but doesn't fit `adjacent`'s "informs how the technical work gets used or sold" test; (b) a **health / biohacking vein** (~4-5 posts — peptides, nootropics, longevity, biotech digests) has no taxonomy home at all and currently sits in `general`. Both are honestly-labelled where they are; a new topic would be the fix if either keeps growing.
- Note: concept #50 is named *founder philosophy & life-design essays* but its primary members are mostly technical "recommended reading" endorsement posts — the name overpromises and is a rename/split candidate independent of the size trigger.
- Priority breakdown: near-term (602), long-term (178), now (110).
- Audiences: me (882), dev-team (632), leadership (168), team (5).
- Concept graph (2026-09-17): **54 active + 1 provisional** (10 archived, 8 merged-into). 7,540 edges — 5,317 `evidence` + 2,221 `weak` + 2 `counter-example`. **Quote the primary-home count, not the evidence count and not the total** — see the set-identity finding above; evidence overstates a concept by 10–60x and the totals include the generous weak layer. **562 primary homes across 33 concepts**, 0 pending observations. Largest homes: #41 *Claude Code setup & usage* (65), *vector / hybrid databases as agent-memory infrastructure* (54), #19 *agent harness engineering* (54).
- **21 of the 54 active concepts are home to zero posts** (2026-09-17; was 20 of 52 on 2026-09-15) — they exist only as secondary tags, and many are `url:` groupings. This is the empty-shell problem in a second form: the regression query in the bullet below checks for concepts with *no edges*, which these pass. The sharper query is `SELECT id,name FROM concepts c WHERE status='active' AND NOT EXISTS(SELECT 1 FROM post_concepts pc WHERE pc.concept_id=c.id AND pc.is_primary=1)`.
- **Merged 2026-09-15:** four `url:` concepts that were exact duplicates of their named twins (identical member sets) — #30→#21 `awesome-claude-skills`, #33→#24 `Feynman`, #35→#26 `turbovec`, #34→#25 `learn-harness-engineering`. 541 primaries unchanged by the merge.
- Orphans (no canonical home): **253 live posts** (2026-09-17), of which only 53 have *no edge at all* — **200 have edges that are all `weak`**. 63 sit at a best-candidate cosine of 0.80–0.81, just under the 0.82 floor. The topic bias the role work fixed has stayed fixed (`adjacent` is 1.06x baseline, was 1.6x). Known narrow gap: a post whose *only* edges came from `revive_dismissed.py` can never be homed, since that script deliberately attaches recovered history as `weak` regardless of cosine — this strands exactly 3 posts whose best revived edge cleared 0.82 (Garry Tan 0.824/#19, Phil Chen 0.825/#5, Avid 0.827/#2). Not a bug; a policy edge case.
- **#41 `Claude Code setup & usage` was vetted for splitting on 2026-09-15 and should NOT be split.** Sub-clustering its 61 homes on mean-centered embeddings at 0.30 (deliberately *below* the 0.40 orphan threshold) yields a largest sub-cluster of 3 and 46 singleton/pair groups. It is broad-and-popular, not conflated — exactly the case the trigger is documented not to act on. Treat the recurring advisory flag on #41 as noise.
- **The empty-shell caveat is resolved — as of 2026-08-26 there are 0 zero-edge active concepts** (it was 20 of 49 on 2026-08-24). All 50 active concepts now carry edges, so the active count is finally an honest measure of the conceptual vocabulary. The regression query is worth keeping, since mechanical discovery can recreate shells at any time: `SELECT id,name FROM concepts c WHERE status='active' AND NOT EXISTS(SELECT 1 FROM post_concepts pc WHERE pc.concept_id=c.id)`.
- Observation provenance (2026-09-17): semantic 7,383 promoted / 6,017 dismissed, mechanical 134 / 19, cluster 58 promoted, latent 16 promoted, curated 14 promoted.
- **The no-discard policy is holding, and the dismissed count is a historical archive — not a live behaviour.** Earlier vintages of this file quoted a much smaller dismissed figure (416) measured a different way; the honest number is 6,017, essentially all of it predating the policy. Grouping dismissals by date makes this unambiguous: **4,119 on 2026-08-26, then zero on every run since.** That date is exactly when `auto_curate()` stopped discarding. If a future audit ever shows a nonzero dismissal on a recent date, something regressed — automation is supposed to attach and label only. The check:

```sql
SELECT substr(observed_at,1,10) d, source, COUNT(*) FROM concept_observations
WHERE status='dismissed' GROUP BY d, source ORDER BY d DESC LIMIT 5;
```
- 36 posts carry a subject `flag:` in `notes`.
- Known dead zone: Jan 3–16, 2026 — many X posts return "page doesn't exist." Some have replacement URLs (authors may have deleted and reposted). Two confirmed replacements found so far (James Cowling, fintechjunkie).

## Python Dependencies

Most of the stack runs on the standard library. The semantic-discovery and curation pipelines need a few extras, pinned in **`requirements.txt`**:

```bash
pip install --break-system-packages -r requirements.txt
```

`fastembed` (~133MB including the bge-small-en-v1.5 ONNX model on first use) is the embedding backbone. `sqlite-vec` is declared but not yet imported by any code path — kept for when the corpus crosses ~10k posts and numpy nearest-neighbor becomes slow. `numpy` is used by `db/embeddings.py` for cosine similarity.

**Auto-bootstrap.** Because the sandbox doesn't persist installs between runs, `db/pipeline.py` calls `db/ensure_deps.py` at the top of its embed step — a `find_spec` check that pip-installs `fastembed`/`numpy` only if missing (fast no-op when present). This is why the sync/catch-up/backfill skills no longer silently skip the semantic layer when the environment is fresh. The sync/backfill skill snapshots also run `db/ensure_deps.py` in Step 0 for good measure. For a permanent install on a real machine (venv / `pip --user`), see **`SETUP.md`**.

**Portability.** The repo carries all code, the DB, docs, and skills. Machine/account-specific pieces — the GitHub token (`.claude/github_token`, gitignored), the M365 + Chrome connectors, and the scheduled-task triggers — are reconstituted per the checklist in `SETUP.md`. Versioned snapshots of the scheduled tasks live in `scheduled/` (`ai-links-sync.SKILL.md`, `ai-links-backfill.SKILL.md`); the live copies are in the Cowork app store at `~/Documents/Claude/Scheduled/<id>/SKILL.md`. The `ai-links-catchup` and `ai-links-curate` skills are in the repo root.

## GitHub Backup

The collection is mirrored to **https://github.com/slycrel/link-farm** after each sync.

### Pushing to GitHub

A GitHub OAuth token is stored at `.claude/github_token` (gitignored — see `SETUP.md` §2 to recreate it on a new box). At the start of any session that needs to push:

```python
import subprocess, pathlib, glob

# Never hardcode the session path — the sandbox mount name changes every session.
# Discover the folder by looking for the one that actually has CLAUDE.md in it.
candidates = sorted(glob.glob('/sessions/*/mnt/cowork'))
cowork = next((c for c in candidates if (pathlib.Path(c) / 'CLAUDE.md').exists()), candidates[0])

token = (pathlib.Path(cowork) / '.claude/github_token').read_text().strip()
creds_path = pathlib.Path.home() / '.git-credentials'
creds_path.write_text(f'https://slycrel:{token}@github.com\n')
creds_path.chmod(0o600)
subprocess.run(['git', 'config', '--global', 'credential.helper', 'store'], check=True)
subprocess.run(['git', 'config', '--global', 'user.name', 'Jeremy Stone'], check=True)
subprocess.run(['git', 'config', '--global', 'user.email', 'jstone@taxhawk.com'], check=True)
```

On a normal machine (not the Cowork sandbox) `cowork` is just the clone directory — drop the glob.

Then clone, mirror the tracked tree into it, commit, and push. **Sync by path pattern, not by a hand-listed set of filenames.** The sync task used an explicit filename allowlist for months, and everything outside it — `SETUP.md`, `README.md`, `scheduled/`, `skills/`, `db/test_*.py`, `ARCHITECTURE_PLAN.md` — silently never reached the remote. They only matched because somebody pushed them by hand. The canonical spec now lives in **`db/repo_sync.py`** (`PUSH_SPEC`), so both the sync task and any ad-hoc push use the same definition:

```python
from db.repo_sync import mirror_to_clone
mirror_to_clone(cowork, push_dir)   # returns the list of copied paths
```

The spec is directory-glob based, which is the part that matters: a new file dropped into `db/`, `scheduled/`, or `skills/` propagates on the next sync without anyone editing a list. Excluded on purpose: `.claude/` (the token), `__pycache__/`, `*.bak` and `db/_*` (local scratch and DB backups), `.fuse_hidden*`, and the SQLite `-wal`/`-shm` sidecars.

```bash
cd ~/work/link-farm && git add -A && git commit -m "Sync: $(date +%Y-%m-%d)" && git push origin main
```

Checkpoint the WAL (`PRAGMA wal_checkpoint(TRUNCATE)`) before copying `db/ai_links.db` so the committed file is self-contained.

### Repo Structure

```
link-farm/
├── README.md                    # Repo front door
├── CLAUDE.md                    # This file — project context
├── SETUP.md                     # Reconstitute on a new machine
├── ARCHITECTURE_PLAN.md         # Workstream plan (screenshots etc.)
├── CURATION_DESIGN.md           # Curation-layer design
├── CURATION_REVIEW.md           # Curation review notes
├── requirements.txt
├── posts_final_v3.json          # Full dataset (JSON, generated)
├── ai_links_collection_v3.html  # Self-contained viewer (generated)
├── ai_links_collection_v3.md    # Markdown companion (generated)
├── ai-links-catchup.SKILL.md    # Skills (also ai-links-catchup/SKILL.md)
├── ai-links-curate.SKILL.md
├── scheduled/                   # Snapshots of the live scheduled tasks
│   ├── ai-links-sync.SKILL.md
│   └── ai-links-backfill.SKILL.md
├── skills/                      # Other skills carried with the repo
├── db/
│   ├── ai_links.db              # SQLite source of truth
│   ├── rebuild.py               # Regenerate outputs from SQLite
│   ├── pipeline.py              # post_enrichment_pipeline
│   ├── enrich.py concepts.py embeddings.py lock.py subject_flags.py
│   ├── perspectives.py recover.py revive_dismissed.py ensure_deps.py
│   ├── repo_sync.py             # PUSH_SPEC — what gets mirrored to the remote
│   ├── migrate.py               # One-time JSON→SQLite bootstrap
│   ├── migrate_runner.py        # Incremental migration runner
│   └── test_*.py                # test_roles / test_lock / test_recover
└── .gitignore                   # .claude/ (token), backups, __pycache__
```

## Jeremy's Wiki

His internal categorization framework lives at: `https://git.taxhawk.com/groups/taxhawk/dev/toolbox/prototypes/-/wikis/AI-Code-as-platform-and-systemic/architecture-things`

## Post Screenshots

**Status**: Schema ready (`image` column in SQLite), implementation planned as Workstream 3 (repurposed catch-up skill).

The `image` field on each post points to a screenshot PNG (e.g., `screenshots/post-{id}.png`). These are NOT full-post screenshots — Jeremy editorially selects the key passage (could be mid-post, a quote tweet, or a specific paragraph). The value is in the curation.

**Implementation approach** (semi-automated v2): During enrichment or the screenshot pass, AI identifies the most impactful passage, scrolls to it, and screenshots that region. No tweet chrome — just the words on a clean background.

**Storage**: `screenshots/` subdirectory. Lazy-load in the HTML viewer.

See `ARCHITECTURE_PLAN.md` for the full workstream details.
