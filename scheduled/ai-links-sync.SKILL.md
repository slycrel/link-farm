---
name: ai-links-sync
description: Pull-first daily AI Links sync from Outlook → SQLite via unified db/enrich.py helpers, structured thread capture, status-enum tracking, full post-enrichment pipeline (incl. orphan clustering, provisional growth + primaries), then push to GitHub.
---

> **Versioned snapshot.** The *live* task runs from the Cowork app store at
> `~/Documents/Claude/Scheduled/ai-links-sync/SKILL.md` (not this file). This
> copy exists so the automation trigger is reproducible on another machine or
> the CLI — see `SETUP.md`. **Keep the two in sync when you change either;**
> they drifted badly once (the live copy sat on a June vintage carrying a stale
> intake filter that suppressed `adjacent` / `solo-operator` tagging for weeks).
> Semantic-stack deps (fastembed/numpy) are auto-ensured by the pipeline via
> `db/ensure_deps.py`, so no manual install step is needed here.

Run the daily AI Links sync — pull-first + import + unified enrichment + post-enrichment pipeline + push.

Refer to `CLAUDE.md` for project background and `CURATION_DESIGN.md` for the curation-layer design. This task is unattended most days, so prefer reasonable defaults over asking. Needs the Microsoft 365 connector for Outlook search and Claude in Chrome for enrichment scraping.

The schema and helpers landed in June 2026 are the canonical write path. Do NOT write directly to `posts.enriched`, `posts.content`, or `posts.summary` from this skill — go through `db/enrich.py` so the schema layer can evolve underneath us without breaking sync runs.

The daily sync and the catch-up skill now run the same post-enrichment pipeline (`db/pipeline.py`) at the end. Capture differs (sync from Outlook, catch-up from the partial/failed queue), but what happens after — subject flags, embeddings, mechanical + semantic discovery, auto-curate, orphan clustering, provisional exemplar growth, assign-primaries, rebuild — is identical.

### Step 0 — Locate Cowork folder, configure git

```python
import subprocess, pathlib, glob, sys
candidates = sorted(glob.glob('/sessions/*/mnt/cowork'))
cowork = next((c for c in candidates if (pathlib.Path(c) / 'CLAUDE.md').exists()), candidates[0] if candidates else None)
assert cowork, 'Cowork folder not found'
sys.path.insert(0, cowork)  # so `import db.enrich` works

# Ensure semantic-stack deps are importable (sandbox doesn't persist installs).
# The pipeline also does this defensively; running it here is cheap when present.
subprocess.run(['python3', f'{cowork}/db/ensure_deps.py'], check=False)

token_path = pathlib.Path(cowork) / '.claude/github_token'
if token_path.exists():
    token = token_path.read_text().strip()
    creds = pathlib.Path.home() / '.git-credentials'
    creds.write_text(f'https://slycrel:{token}@github.com\n')
    creds.chmod(0o600)
    subprocess.run(['git', 'config', '--global', 'credential.helper', 'store'], check=True)
    subprocess.run(['git', 'config', '--global', 'user.name', 'Jeremy Stone'], check=True)
    subprocess.run(['git', 'config', '--global', 'user.email', 'jstone@taxhawk.com'], check=True)
```

Use `cowork` for every later file path.

**Writer lock.** All SQLite writes and the rebuild step run inside one `writer_lock()` context, acquired at Step 6 and held through Step 8. `curate.py` and any other writer take the same lock — they're allowed to interleave between batches but not inside one. If acquisition times out (60s default), the sync should bail out, log the contention, and let the next scheduled run try.

### Step 1 — Pull canonical state from GitHub first

(Unchanged from prior runs.) Another runner may have pushed since our last sync. Clone to `/tmp/lf-pull-{ts}`, compare local vs remote post counts and MAX(created_at). If remote is fresher, delete any local `db/ai_links.db-wal` / `-shm` / `-journal` (use `mcp__cowork__allow_cowork_file_delete` if needed), then copy `db/ai_links.db`, `posts_final_v3.json`, `ai_links_collection_v3.html`, `ai_links_collection_v3.md` from the clone back into `{cowork}/`.

### Step 2 — Apply pending migrations

```python
subprocess.run(['python3', f'{cowork}/db/migrate_runner.py'], check=True)
```

Idempotent — no-op if everything is current. Surfaces failures early before any write attempt.

### Step 3 — Compute CUTOFF

`SELECT MAX(created_at) FROM posts` against `{cowork}/db/ai_links.db`. Call this CUTOFF.

### Step 4 — Search Outlook for new emails

Microsoft 365 MCP, sender `slycrel@gmail.com`, after CUTOFF. `limit: 25` (the connector caps at 25 — paginate with `offset` if a page is full). No recipient filter — it breaks pagination.

**Keep what Jeremy sends.** Anything pushed through the iPhone share sheet is deliberate and presumed intentional. Do NOT drop a link for being off-topic, non-technical, low-brow, or hype-packaged — that judgment happens later, with content in hand, via topic tags.

Drop only **true noise**: Sentry alerts, receipts, shipping and delivery notices, family mail, car listings — mail that isn't a link Jeremy is collecting at all. When genuinely unsure, keep it; a mis-tagged post is cheap and visible, a silently dropped one is neither.

Tangential material is wanted, not tolerated. Persuasion and sales, writing craft, creator-economy and indie-studio content, business logistics — these get the `adjacent` and/or `solo-operator` topics (see CLAUDE.md) alongside any technical tags that apply. Hype packaging earns `questionable`, which is a *credibility* label only and never a reason to drop, deprioritize, or suggest removing a post.

Note: some self-sent mail carries attachments and no URL at all (e.g. Jeremy moving a skill zip or a diff between his machines). That isn't noise and isn't a link — there's nothing to insert. Skip it and say so in the report rather than forcing a row.

### Step 5 — Extract URLs

For each email, read body via `mail:///messages/{messageId}` if needed (the summary is usually accurate for the iPhone share-sheet shape). Extract primary URL (x.com, twitter.com, github.com, arxiv.org, blog posts). Strip tracking params (`?s=`, `?t=`, `&utm_*`). Normalize x.com URLs to `https://x.com/{handle}/status/{id}`.

### Step 6 — Insert new posts (skeleton rows, acquire the lock here)

Acquire the writer lock NOW and hold it through enrichment, the pipeline, and rebuild:

```python
from db.lock import writer_lock
from db.enrich import (
    pending_enrichment_ids, record_enrichment, record_partial, record_dead,
    record_failed, status_breakdown, gate_ratio, ENRICHMENT_VERSION,
)
from db.pipeline import post_enrichment_pipeline

with writer_lock(timeout=60):
    # Steps 6, 7, 8 all happen inside this block
    ...
```

For each extracted URL:
- Derive deterministic post ID per CLAUDE.md (X status ID for x.com/twitter.com; SHA-256 of normalized URL truncated to 48 bits otherwise).
- Skip if ID already in `posts` table.
- INSERT a skeleton row: `date` (email date YYYY-MM-DD), `author` (from "Post by X on Y"), `handle` (lowercased with `@` if present), `subject`, `url`, `source='email'`, `priority='near-term'`, `enrichment_status='unattempted'`, `enrichment_version=0`. (The `enriched` legacy boolean defaults to 0 — leave it alone; `db/enrich.py` syncs both columns on successful enrichment.)
- Insert default-topic `post_topics` row (best-guess from subject keywords) and `post_audiences` row (`'me'`).

Track NEW_IDS for the enrichment pass.

### Step 7 — Chrome preflight + unified enrichment

Chrome runs on the user's Mac. Detect connectivity once:

1. `tabs_context_mcp` with `createIfEmpty: true`.
2. On "not connected", wait 10s, retry. **5 attempts total** (~50s wallclock).
3. Still not connected → call `db.enrich.record_failed(post_id, error="chrome-unreachable")` for every NEW_ID and jump to Step 7b.

Work list (newest-first):
- All NEW_IDS from Step 6.
- If `len(NEW_IDS) <= 5`, also append `pending_enrichment_ids(limit=25, statuses=('partial','failed'))` — light-day backlog. Cap total wallclock at ~15 minutes.
- If the work list comes out empty (no new posts and an empty backlog), skip Chrome entirely — don't open a tab just to prove there's nothing to scrape. Note it in the report and go straight to Step 8.

For each post:
1. `navigate` to URL in Chrome.
2. **Jittered render wait** — `new Promise(r => setTimeout(()=>r(true), 1500 + Math.random()*4000))`. Range 1.5–5.5s, mean ~3.5s. Fixed-cadence waits are the loudest automation signature; human-shaped variance is the cheapest mitigation against X rate-limiting at sustained read volume.
3. Extract via `javascript_tool`: enumerate all `<article>` elements; for each, capture `(text, handle, urls)`. The first article is type `op`; subsequent articles whose handle matches the page handle are `self_reply`; others are `quote`. Detect external links (github/arxiv/huggingface/blog hosts) as their own `external_link` segments.
4. On timeout/empty extraction, retry once after 3s.
5. **If `javascript_tool` returns `[BLOCKED: Cookie/query string data]`, fall back to `get_page_text` immediately.** That string is the Chrome extension's own content guard redacting the payload — it is *not* a dead post and *not* a rate limit. The guard fires on the **tool**, not on what the tool returns, so reshaping the payload does not help: verified 2026-08-26 on post `2055064462844219603`, where scrubbing every URL and query-string pattern out of the returned JSON was blocked identically to the unscrubbed version. `get_page_text` reads the article element directly, is not subject to the same guard, and recovered the full 14K-char article in one call. It trades segment structure (no quote/link-card separation) for actually getting the text — so prefer `javascript_tool` when it works, and consider `get_page_text` the *first* move on X Article URLs, which is where this shape shows up. Never mark a `[BLOCKED: …]` post `dead`.
6. Still failing AND page text contains "post is unavailable" / "account suspended" / "page doesn't exist" / "this Tweet was deleted" → `record_dead(post_id, reason=<detected marker>, summary="[Post unavailable — {marker}]")`. Move on.
7. Still failing without a dead marker → `record_partial(post_id, error="empty capture")`. Move on; next sync will retry.
8. Otherwise, compose a 1–3 sentence summary capturing what it's about, why it matters, key details. Include notable URLs inline as plain text (no markdown linking). Skip generic x.com self-links. Prioritize GitHub repos, arxiv papers, product/tool homepages.
   - Good: `"NVIDIA open-sourced OpenShell (github.com/nvidia/openshell) — a sandbox for AI coding agents that locks filesystem, blocks network by default, and injects API keys at runtime only."`
   - Bad: `"Post about a security tool."`
9. Re-classify with content in hand:
   - **topics**: apply all relevant tags from CLAUDE.md. Add `questionable` alongside real topics when engagement-farmed-but-substantive — it flags packaging, not worth. Use `adjacent` for non-engineering material that's useful anyway, `solo-operator` for indie/side-hustle/business-of-one content, and `biohacking` for nootropics/peptides/supplements/sleep/longevity/biotech material; all three combine freely with technical tags and with each other. Never write a summary that recommends removing a post, and never call a post "off-topic," "not AI/dev," or "probably an accidental email" — that phrasing is the old aggressive intake filter talking, and it produced summaries that had to be rewritten in August 2026. If it's in the corpus, describe what value it might hold and let the tags carry the caveat.
   - **audiences**: upgrade `['me']` → `['me', 'dev-team']` for practical tools/patterns, `['me', 'leadership']` for strategy/industry signals.
   - **priority**: `now` for directly-actionable tools to evaluate; `near-term` for explore-soon; `long-term` for research/future.
   - **views**: extract from page if visible.
   - **author**: update to display name if it differs from email subject.
10. Persist via `record_enrichment(post_id, segments=[...], summary=..., topics=[...], audiences=[...], author=..., handle=..., views=..., priority=..., with_lock=False)` — `with_lock=False` because the batch already holds the writer lock.

**Rate-limit watch.** If 3+ posts in a row return empty articles or page-shell content (no text in the OP article element), stop the batch early — that's the most-likely shape of X rate-limiting. Persist already-scraped posts and report. Next run picks up where this one left off.

If Chrome rate-limits or persistently times out, stop early — don't burn budget retrying. Count what got done and move on.

### Step 7b — Chrome-unreachable fallback

If Step 7 preflight failed entirely, the import work from Steps 4–6 is still valuable. Don't lose it:

1. Use `mcp__scheduled-tasks__create_scheduled_task` to schedule a one-time follow-up in 2 hours. `taskId`: `ai-links-enrich-retry-YYYYMMDD-HHMM`. `fireAt`: now+2h ISO with local offset. Prompt: "Run the ai-links-catchup skill — Chrome was unreachable on the morning sync, finish enriching any posts in `partial` or `failed` status."
2. Skip to Step 8.

### Step 8 — Post-enrichment pipeline (still inside the lock)

```python
pipeline_result = post_enrichment_pipeline(with_lock=False, progress=True)
print(pipeline_result['summary'])
```

This single call does, in pipeline order:
0. **Subject flags** — lifts the trailing-parenthetical importance flag from email subjects into `posts.notes` as a searchable `flag: <text>` fragment. Idempotent; never clobbers existing curation notes.
1. **Embed** any post whose content_hash changed (or is missing an embedding) using fastembed + bge-small-en-v1.5 (384d). Skips partial/dead posts. (Deps auto-ensured via `db/ensure_deps.py`.)
2. **Mechanical discovery** — shared external URLs (min 2 co-citing posts) + shared @mentions (min 3) → new `concept_observations` rows.
3. **Semantic discovery** — concept-centroid matching. Two bands, and the gap between them is the point: propose at `SEMANTIC_CENTROID_THRESHOLD` (**0.75**), auto-file as evidence at `AUTO_PROMOTE_MIN_COSINE` (**0.82**) — both measured on *raw* cosines. Anything landing in between is recorded as a `weak` edge. `SEMANTIC_MAX_WEAK_PER_POST` (3) caps weak edges as a **per-post total, not per-run**, so a weak edge means "one of this post's closest concepts"; the evidence band is uncapped. A concept needs at least `SEMANTIC_MIN_CONCEPT_EDGES` (2) *canonical* edges to be scoreable at all.
4. **Auto-curate** (step 3.5) — **attaches and labels; it no longer discards anything.** Every post here is something Jeremy deliberately sent himself, so "low signal" is not a high enough bar to decide we never think about it again. Automation records what it found and how much to trust it; only a human calls `dismiss_observation()`, and only for genuine junk (scams, content-free bait). Do not "clean up" weak edges in an unattended run.
5. **Orphan clustering** (step 3.55) — the only pass that invents a *new* concept from theme, clustering edge-less posts on **mean-centered** embeddings (`ORPHAN_CLUSTER_THRESHOLD` = 0.40 is a centered cosine and is *not* comparable to the semantic threshold). Guards: min size 4, min cohesion 0.55, max 6 per run, max 55% single-author share, min 3 distinct authors. "Orphan" means *no canonical home* — a weak-only post stays eligible.
6. **Provisional exemplar growth** (step 3.56) — grows the nursery tier. A `provisional` concept holds edges and is fully browseable but is inert by construction: it is not a candidate primary home, and it does not feed centroids or semantic scoring. It graduates to `active` automatically at `PROVISIONAL_GRADUATION_MIN_EDGES` (4) **canonical** edges — weak edges don't buy graduation. Centroid matching structurally can't grow a 1–2 member concept, so this pass scores candidates by **max similarity to any single existing member** on **mean-centered** vectors at `PROVISIONAL_EXEMPLAR_THRESHOLD` (0.40, centered — *not* comparable to the semantic threshold), capped at `PROVISIONAL_EXEMPLAR_MAX_PER_RUN` (3).
7. **Assign primaries** (step 3.6) — derives each post's single primary home (exactly one per post) by cosine against each candidate concept's leave-one-out centroid. Only `active` concepts and only **canonical** (`evidence`/`origin`) edges can be a home. Split-review counts *primaries*, not total edges.
8. **Rebuild** — regenerates `posts_final_v3.json`, `ai_links_collection_v3.html`, `ai_links_collection_v3.md`.

**Edge roles are load-bearing — don't let generous attachment corrupt the graph.** `CANONICAL_ROLES = ('evidence', 'origin')` vote on what a concept *means*; `weak`, `counter-example` and `tangential` are recorded associations that must not. That distinction is enforced in four separate places (centroids, semantic scoring, primary assignment, orphan eligibility) and each is a *silent* failure if it regresses — `db/test_roles.py` (15 tests) exists for exactly this reason. If you touch role handling, run it.

**If orphan clustering created concepts, rename them before finishing.** Unattended runs auto-name from crude TF-IDF and mark the description `[auto-named]`; this task has a model in the loop, so do better. Find and fix them:

```python
import sqlite3
con = sqlite3.connect(f'{cowork}/db/ai_links.db')
fresh = con.execute("SELECT id, name FROM concepts WHERE description LIKE '%[auto-named]%'").fetchall()
```

Read a few member posts of each, then use `db.concepts.rename_concept()` to give it a name that names the *idea*, not the loudest author (author and handle tokens are already excluded from the naming vocabulary, but auto-names are still crude). `archive_concept(id)` retires a cluster that isn't a real theme; `merge_concepts()` folds a duplicate into an existing home. Both are reversible.

**While you're there, check whether the fresh cluster is lexically diffuse** — members that share a *purpose* but not a *vocabulary*. Averaging those yields a centroid near the corpus mean, which matches everything, and matches ≥0.82 become evidence, so the concept feeds on its own diffuseness and becomes a magnet. Concept #65 absorbed 26 unrelated evidence edges and 18 primaries within two runs this way. The fix is to put `NO_CENTROID_SCORING_MARKER` (`[no-centroid-scoring]`) in the description: the concept keeps its edges and stays fully browseable, but nothing is ever matched *into* it by cosine. Rule of thumb — **if a concept exists only because a reader could see it, mark it.** Note the interaction with the nursery: a provisional concept that graduates while still lexically diffuse becomes a magnet the moment it earns a centroid.

Each step is idempotent; running the pipeline twice is a no-op the second time. Errors in one step don't abort the others — the result dict has `errors` listing what went wrong.

If deps can't be installed for some reason, the embed + semantic steps surface a clean error and the pipeline still runs mechanical + rebuild. Tell Jeremy in the report.

**A large jump in new semantic observations is expected, not alarming,** if a manual restructure, an orphan-clustering run, or a latent pass recently reshaped centroids. Those auto-file as *secondary* edges and settle to a trickle over the next 1–2 runs (the convergence surge — e.g. 134 → 4 → ~0). Report the number and move on.

### Step 9 — Push to GitHub (still inside the lock)

```python
push_dir = f'/tmp/lf-sync-{int(time.time())}'
subprocess.run(['git', 'clone', 'https://github.com/slycrel/link-farm.git', push_dir], check=True)
subprocess.run(['git', 'config', '--global', '--add', 'safe.directory', push_dir], check=True)
for fname in ['posts_final_v3.json', 'ai_links_collection_v3.html', 'ai_links_collection_v3.md',
              'CLAUDE.md', 'CURATION_DESIGN.md', 'requirements.txt']:
    src = f'{cowork}/{fname}'
    if os.path.exists(src):
        shutil.copy(src, f'{push_dir}/{fname}')
os.makedirs(f'{push_dir}/db', exist_ok=True)
for fname in ['ai_links.db', 'migrate.py', 'migrate_runner.py', 'rebuild.py', 'enrich.py',
              'lock.py', '__init__.py', 'concepts.py', 'embeddings.py', 'pipeline.py',
              'perspectives.py', 'subject_flags.py', 'recover.py', 'ensure_deps.py']:
    src = f'{cowork}/db/{fname}'
    if os.path.exists(src):
        shutil.copy(src, f'{push_dir}/db/{fname}')

today = datetime.date.today().isoformat()
subprocess.run(['git', '-C', push_dir, 'add', '-A'], check=True)
diff = subprocess.run(['git', '-C', push_dir, 'diff', '--cached', '--stat'], capture_output=True, text=True)
if diff.stdout.strip():
    subprocess.run(['git', '-C', push_dir, 'commit', '-m', f'Sync {today}'], check=True)
    subprocess.run(['git', '-C', push_dir, 'push', 'origin', 'main'], check=True)
```

Release the writer lock by exiting the `with` block.

**Housekeeping.** The cowork mount denies `unlink`, so deleted-but-open files accumulate in `db/` as `.fuse_hidden*` orphans (they reached ~5,200 files / 284 MB once and made the directory unlistable). If `find {cowork}/db -maxdepth 1 -name '.fuse_hidden*' | wc -l` exceeds ~500, delete them — never touching `ai_links.db`, `ai_links.db-wal`, or `ai_links.db-shm` — and mention it in the report. Use `mcp__cowork__allow_cowork_file_delete` if `rm` returns "Operation not permitted". Also checkpoint the WAL (`PRAGMA wal_checkpoint(TRUNCATE)`) before the push so the committed `.db` file is self-contained.

### Step 10 — Report

Tell Jeremy:
- Pull-first result (was the remote ahead? did we restore local?)
- Migration runner — were any pending? Final schema version.
- Emails found, posts inserted (after dedup), topic breakdown of new posts. Note any mail skipped as noise or as attachment-only-with-no-URL.
- Enrichment counts: `ok` / `partial` / `dead` / `failed` for this run — or that Chrome was skipped because the work list was empty.
- Status breakdown for the whole corpus (`status_breakdown()`).
- Latent gate ratio (`gate_ratio()`): is it open?
- **Pipeline summary** (from `pipeline_result['summary']`) — flags, embed counts, new mechanical/semantic observations, auto-curate, orphan clusters, provisional growth, primaries, rebuild post count.
- Pending observation count (should be ~0 in steady state — semantic triage is automated).
- **Any concepts created by orphan clustering this run, and what you renamed them to** (or that none were created). Flag any left `[auto-named]`, and say whether you marked any `[no-centroid-scoring]`.
- **Any provisional concepts that graduated to `active` this run** (4+ canonical edges), and any still sitting below the bar. A nursery concept holding at 2 for several runs is the threshold doing its job, not a failure.
- When you quote how big a concept is, **quote the `evidence` count, not total edges** — the total includes the deliberately-generous weak layer and overstates it by roughly 40%.
- Split-review candidates from `pipeline_result['split_candidates']` (advisory only — never auto-split).
- Modified subject lines (Jeremy's importance flags — `(implement!)`, `(read this today)`, `(mgmt)`).
- GitHub push status.
- Any failures (Chrome unreachable, lock timeout, unparseable subjects, dedup hits, pipeline errors).
- **Whether the rate-limit watch fired** — if it did, what got captured and what didn't.

### Constraints

- Never write `posts.enriched`, `posts.content`, or `posts.summary` directly — always go through `db/enrich.py` so the persistence semantics stay consistent.
- The post-enrichment pipeline call is idempotent — safe to run even if Step 7 found nothing to enrich. The mechanical pass will re-scan the corpus cheaply; the semantic pass will surface new candidates as concepts gain evidence.
- If pull-first revealed the remote was ahead and we restored from it, that alone is not a reason to commit. We commit only when local has changes the remote doesn't have.
- If no new emails since CUTOFF AND no backlog of `partial`/`failed`, still run the pipeline (it's cheap and may surface new concept evidence as the graph evolves) — but skip commit/push if `git diff --cached` is empty.
- If the DB is locked or anything goes wrong inside the writer-lock block, abort before pushing and report.
- Never delete posts; only insert and update. `dead` status is the closest we get to a tombstone.
- Never call `dismiss_observation()` from this task. Automation attaches and labels; discarding is a human decision. A weak edge is a recorded association, not a mistake to clean up.
- Don't retune `SEMANTIC_CENTROID_THRESHOLD`, `AUTO_PROMOTE_MIN_COSINE`, `SEMANTIC_MAX_WEAK_PER_POST` or the orphan/provisional constants from a sync run. They were calibrated against this corpus's actual cosine distribution (pairwise mean 0.61 / p99 0.73), and the failure modes are non-obvious — an uncapped 0.75 proposed 8,825 observations in a single run, ~26% of every possible (post, concept) pair. Surface a concern in the report instead.
- If you change this task, mirror the change into `scheduled/ai-links-sync.SKILL.md` in the repo and push it, so the live copy and the snapshot don't drift again.
