# AI Links Collection — Project Context

This folder contains Jeremy's curated collection of AI-related links, sourced from emails he sends himself (X/Twitter posts, articles, tools) and organized with rich metadata for sharing with his team at TaxHawk.

## How It Works

Jeremy emails himself links from his phone (slycrel@gmail.com → jstone@taxhawk.com) using iPhone's share sheet. The subject line is typically "Post by [Author] on X" with the URL in the email body. Sometimes he modifies the subject to flag importance — treat modified subjects as a signal worth noting.

## Files

- **db/ai_links.db** — SQLite database. Single source of truth for all posts. All capture paths write here; all output artifacts are generated from it.
- **db/migrate.py** — One-shot rebuild-from-JSON bootstrap script. Used only when rebuilding the DB from `posts_final_v3.json` from scratch. **Not** the runner for incremental schema changes.
- **db/migrate_runner.py** — Incremental schema migration runner. Transactional per-migration, idempotent, advances `schema_version`. Add a new migration here whenever the schema needs to change. Currently at version 8 (v8 added `post_concepts.is_primary` — the primary/secondary axis).
- **db/enrich.py** — Canonical persistence layer for enrichment work. All writers (sync, catch-up, curate) go through these helpers — never write directly to `posts.enriched`, `posts.content`, or `posts.summary`. Exposes `record_enrichment` / `record_partial` / `record_failed` / `record_dead`, work-queue queries (`pending_enrichment_ids`), and `gate_ratio` for the latent-discovery threshold.
- **db/concepts.py** — Concept-graph layer (Layer 2). Concept lifecycle (create/merge/archive/rename), observation lifecycle (record/promote/dismiss/bulk_promote/bulk_dismiss/filter), mechanical discovery passes (shared external URLs, shared @mentions), semantic discovery (concept-centroid matching via embeddings). Also holds `auto_curate()` (unattended conceptual-preference triage — see below), `assign_primaries()` (derives each post's single primary concept — see the primary/secondary note below), and `split_candidates()` (advisory large-*home* flag, threshold `SPLIT_CANDIDATE_MIN_POSTS`, default 40, measured on primary posts). CLI: `python3 -m db.concepts {list,pending,promote,dismiss,merge,discover,semantic,stats}`. Curation surface: chat-mediated via the `ai-links-curate` skill.

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
- **questionable** — Engagement farming (ALL CAPS hype, "BREAKING", listicles with fire emojis). Some may still have good content behind the clickbait — if so, keep relevant topic tags alongside "questionable"
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

### Split-review trigger

`db/concepts.split_candidates()` flags active concepts at/above `SPLIT_CANDIDATE_MIN_POSTS` (default 40) as candidates worth vetting for sub-categorization. **Measured on primary-home count, not total edges** (see the primary/secondary note above) — a concept can be a secondary tag on many posts without being an oversized home. Advisory only — surfaced in the pipeline summary (`⚑ split-review candidates: …`), never an auto-split. Overlapping/broad concepts are acceptable; the trigger just keeps a big *home* from quietly accumulating unnoticed. Splitting a merely-popular concept (large total, small home) won't reduce the flag and isn't the intent — split when a *home* conflates distinct threads, as #29 did.

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

## Collection Stats (as of June 13, 2026)

- **619 total posts** in SQLite (live count). Date range: June 11, 2024 – June 11, 2026.
- Enrichment status: 5 `ok` (current `ENRICHMENT_VERSION=1`), 289 `legacy-ok` (worked at pre-migration generation), 267 `partial` (recoverable — empty content waiting for re-enrichment), 58 `dead` (permanent floor — deleted/suspended/login-walled).
- Latent gate ratio: ~47% — far above the 5% threshold. Re-enrichment work needs to drive `partial` count down to ~28 (5% of total - dead) before latent discovery activates.
- Top topics: agent-design (300), dev-practices (167), claude-code (155), research (114), management (96), skills-mcp (87), prompting (84), questionable (84), general (78), industry (70).
- Priority breakdown: near-term (333), long-term (177), now (109).
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
