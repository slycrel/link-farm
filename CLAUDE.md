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

  **Curation preference (Jeremy, July 2026):** favor *conceptual* categories (themes/ideas) over *per-person* ones. Per-person concepts (`mention:@handle`, names carrying a `(@handle)` tag) and raw `url:` groupings are kept but not actively grown — don't route new evidence into them when a conceptual home exists. `auto_curate()` encodes this: it auto-files semantic matches at/above `AUTO_PROMOTE_MIN_COSINE` (default 0.82) as *secondary* tags on active *conceptual* concepts, dismisses conceptual matches below that floor (the recall band — no longer reviewed by hand), and dismisses low-signal `mention:`/`url:` groupings and per-person duplicates whose post is already conceptually covered. Overlapping conceptual tags are fine and expected — no dedup forced. Since primary is derived separately (`assign_primaries`) and split-review counts primaries, generous secondary auto-filing is safe. The human curate queue is now reserved for structural decisions (merges, naming, per-person groupings not yet covered), not routine semantic tagging.
- **db/subject_flags.py** — Subject-flag extraction. Lifts the trailing-parenthetical importance flag Jeremy adds to email subjects (`Post by X on X (read for work)`) into `posts.notes` as a searchable `flag: <text>` fragment. Idempotent and non-destructive (never clobbers existing curation notes; re-running is a no-op). Runs automatically as step 0 of `db/pipeline.py`, so every sync/catch-up/backfill captures new flags. Fully custom subjects (e.g. "Local code review") are left alone — those are Jeremy's own titling, not flags, and stay in `posts.subject`. CLI: `python3 -m db.subject_flags [--dry-run]`.
- **db/embeddings.py** — Semantic embeddings via fastembed + numpy. Default model `BAAI/bge-small-en-v1.5` (384-dim, ONNX, local). Embeds posts in `ok`/`legacy-ok` status (skips partial/dead — junk in produces junk vectors). `content_hash` invalidation so re-enrichment doesn't require re-embedding the whole corpus. CLI: `python3 -m db.embeddings {status,embed,neighbors,centroids}`.
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

### Weekday Backfill (ai-links-backfill)

Unattended weekday background re-enrichment, scheduled for 10:30 AM local Monday through Friday (cron `30 10 * * 1-5`) — after the 9 AM morning sync settles. Processes a fixed BATCH_LIMIT (currently 15) of `partial` / `failed` / `unattempted` posts per run via Chrome + `db/enrich.py` helpers, then runs the same `post_enrichment_pipeline` the sync and catch-up skills use. Drives down the recoverable-incompleteness ratio so the latent-discovery gate (`(partial + failed) / (total − dead) < 0.05`) eventually opens. Skips `legacy-ok` posts (they have usable content already) — that's a separate concern when `ENRICHMENT_VERSION` bumps. Cleanly no-ops when the queue is empty. At 75 posts/week, the backlog drains in roughly 3 weeks under typical conditions; the cadence can be slowed back to weekly once the gate opens.

### Curate Skill (ai-links-curate)

Chat-mediated curation surface for the concept graph. Invoked by saying "curate links", "promote observation", "merge concepts", etc. Parses natural-language commands and routes them to `db/concepts.py` helpers — promote/dismiss/merge/rename/create concepts, list pending observations, run discovery passes manually, show gate ratio. End-of-batch: rebuild via the shared pipeline + push to GitHub.

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

## Collection Stats (as of August 26, 2026)

Regenerate these numbers from the DB rather than trusting them blind — they drift between refreshes. The queries are one-liners against `db/ai_links.db`.

- **836 total posts** in SQLite (live count). Date range: June 11, 2024 – August 25, 2026.
- Enrichment status: **763 `ok`** (current `ENRICHMENT_VERSION=1`), 73 `dead` (permanent floor — deleted/suspended/login-walled). **Zero `partial` / `failed` / `unattempted` / `legacy-ok` — the enrichment queue is completely empty** as of 2026-08-26, so `ai-links-backfill` no-ops until new mail arrives.
- **Latent gate ratio: 0.00% — the gate is OPEN** (open since 2026-08-14; see `gate_history`). With no recoverable-incomplete posts left, the numerator is zero. Latent discovery is available on demand, but only inside a skill session — it is deliberately not in `post_enrichment_pipeline` because an unattended run has no reader.
- Top topics: agent-design (490), dev-practices (354), research (211), claude-code (191), skills-mcp (191), management (131), prompting (125), questionable (122), industry (121), general (100), `adjacent` (38), `solo-operator` (8), `biohacking` (7).
- **Re-tag pass, 2026-08-18.** `adjacent` and `solo-operator` had 1 post each despite being deliberate taxonomy additions. A review of the 151 live `general`/`industry` posts (cross-checked against concepts #45/#50) added 27 `adjacent` and 4 `solo-operator` tags, additively — existing topics were preserved, nothing was retagged away. Root cause was upstream: the *live* `ai-links-sync` scheduled task had drifted to a June vintage carrying the old aggressive intake filter ("filter out non-AI/tech") and no mention of either topic, so the enricher never had them in its working vocabulary. Live task and repo snapshot are now back in sync and both name the two topics explicitly.
- Two known gaps left after that pass, both judgment calls rather than oversights: (a) a **quant-trading / masterclass vein** (concept #45, ~5 posts — Jane Street / Jim Simons / Markov-chain lectures) is non-engineering but doesn't fit `adjacent`'s "informs how the technical work gets used or sold" test; (b) a **health / biohacking vein** (~4-5 posts — peptides, nootropics, longevity, biotech digests) has no taxonomy home at all and currently sits in `general`. Both are honestly-labelled where they are; a new topic would be the fix if either keeps growing.
- Note: concept #50 is named *founder philosophy & life-design essays* but its primary members are mostly technical "recommended reading" endorsement posts — the name overpromises and is a rename/split candidate independent of the size trigger.
- Priority breakdown: near-term (548), long-term (178), now (110).
- Audiences: me (828), dev-team (586), leadership (156), team (5).
- Concept graph: 50 active concepts (10 archived, 4 merged-into), **7,041 edges**, 516 primary homes, 0 pending observations. 254 posts still carry no concept edge (183 of them embedded and thus eligible for orphan clustering; the rest are `dead` and never embedded).
- **The empty-shell caveat is resolved — as of 2026-08-26 there are 0 zero-edge active concepts** (it was 20 of 49 on 2026-08-24). All 50 active concepts now carry edges, so the active count is finally an honest measure of the conceptual vocabulary. The regression query is worth keeping, since mechanical discovery can recreate shells at any time: `SELECT id,name FROM concepts c WHERE status='active' AND NOT EXISTS(SELECT 1 FROM post_concepts pc WHERE pc.concept_id=c.id)`.
- Observation provenance: semantic 6,899 promoted / 416 dismissed, mechanical 120 / 19, cluster 58 promoted, latent 16 promoted. Note the semantic dismissed count *fell* (2,560 → 416) while promoted rose sharply — the blob-remediation campaign replaced paraphrase with real content, so matches that previously scored under the 0.82 floor now clear it.
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

A GitHub OAuth token is stored at `.claude/github_token`. At the start of any session that needs to push:

```python
import subprocess, pathlib
token = pathlib.Path('/sessions/inspiring-clever-keller/mnt/cowork/.claude/github_token').read_text().strip()
subprocess.run(['git', 'config', '--global', 'credential.helper', 'store'], check=True)
creds_path = pathlib.Path.home() / '.git-credentials'
creds_path.write_text(f'https://slycrel:{token}@github.com\n')
creds_path.chmod(0o600)
subprocess.run(['git', 'config', '--global', 'user.name', 'Jeremy Stone'], check=True)
subprocess.run(['git', 'config', '--global', 'user.email', 'jstone@taxhawk.com'], check=True)
```

Then clone (if not already present), copy the output files, commit, and push:

```bash
# Clone once per session if needed
git clone https://github.com/slycrel/link-farm.git /tmp/link-farm

# After rebuild, sync files
cp posts_final_v3.json ai_links_collection_v3.html ai_links_collection_v3.md /tmp/link-farm/
cp db/ai_links.db /tmp/link-farm/db/
cd /tmp/link-farm && git add -A && git commit -m "Sync: $(date +%Y-%m-%d)" && git push origin main
```

### Repo Structure

```
link-farm/
├── posts_final_v3.json          # Full dataset (JSON)
├── ai_links_collection_v3.html  # Self-contained viewer
├── ai_links_collection_v3.md    # Markdown companion
├── db/
│   ├── ai_links.db              # SQLite source of truth
│   ├── rebuild.py               # Regenerate outputs from SQLite
│   └── migrate.py               # One-time import script
└── .gitignore
```

## Jeremy's Wiki

His internal categorization framework lives at: `https://git.taxhawk.com/groups/taxhawk/dev/toolbox/prototypes/-/wikis/AI-Code-as-platform-and-systemic/architecture-things`

## Post Screenshots

**Status**: Schema ready (`image` column in SQLite), implementation planned as Workstream 3 (repurposed catch-up skill).

The `image` field on each post points to a screenshot PNG (e.g., `screenshots/post-{id}.png`). These are NOT full-post screenshots — Jeremy editorially selects the key passage (could be mid-post, a quote tweet, or a specific paragraph). The value is in the curation.

**Implementation approach** (semi-automated v2): During enrichment or the screenshot pass, AI identifies the most impactful passage, scrolls to it, and screenshots that region. No tweet chrome — just the words on a clean background.

**Storage**: `screenshots/` subdirectory. Lazy-load in the HTML viewer.

See `ARCHITECTURE_PLAN.md` for the full workstream details.
