---
name: ai-links-catchup
description: "Bulk enrichment and catch-up tool for Jeremy's AI Links Collection. Use this skill whenever Jeremy says 'catch up on links', 'enrich my links', 'deep dive on posts', 'scrape my bookmarks', 'process missed links', 'update link summaries', or any variation of wanting to fill in missing URLs, scrape X/Twitter content, summarize posts, or re-categorize the AI links collection. Also trigger when Jeremy mentions he's been away (vacation, long weekend, laptop closed) and wants to get his link collection up to date. Even if he just says 'catch up' or 'what did I miss' in the context of his AI links, use this skill."
---

# AI Links Catch-Up & Deep Dive

You are enriching Jeremy's AI Links Collection — a curated set of X/Twitter posts and articles about AI, coding agents, and developer tools that he emails to himself from his personal account (slycrel@gmail.com).

Refer to `CLAUDE.md` in Jeremy's Cowork folder for full project context (schema, topic definitions, status semantics, GitHub recipe) and `CURATION_DESIGN.md` for the architecture this skill operates within. The most important thing to internalize before doing any work: **never write directly to `posts.enriched`, `posts.content`, or `posts.summary`. Always go through `db/enrich.py` helpers** so the persistence semantics stay consistent and provenance is preserved.

## Overview

This skill handles three jobs, run in sequence (Jeremy can ask for all or a subset):

1. **Backfill missing URLs** — read Outlook email bodies to extract URLs for posts whose `url` column is empty
2. **Re-enrich posts** — query the `partial` / `failed` / `unattempted` work queue, scrape each via Chrome through structured-segment capture, persist via `db/enrich.py`
3. **Rebuild outputs** — regenerate the JSON / HTML / Markdown deliverables (one Python call)

The default invocation ("catch up on links") runs all three. Jeremy may scope it: "just get the URLs," "just re-scrape the partial ones," "deep dive on the last month."

## Data files

Look for these in Jeremy's Cowork folder (the selected/mounted folder):

- **SQLite (source of truth):** `db/ai_links.db`
- **Persistence module:** `db/enrich.py` — all write paths go through this
- **Migration runner:** `db/migrate_runner.py` — run first, idempotent
- **Lock module:** `db/lock.py` — shared writer lock; acquire before any mutation
- **Outputs (generated):** `posts_final_v3.json`, `ai_links_collection_v3.html`, `ai_links_collection_v3.md`

Never edit the generated outputs directly. They are regenerated from SQLite by `db.rebuild.rebuild()`.

## Setup at the start of every run

Always do these first, in order:

```python
import subprocess, pathlib, glob, sys
candidates = sorted(glob.glob('/sessions/*/mnt/cowork'))
cowork = next((c for c in candidates if (pathlib.Path(c) / 'CLAUDE.md').exists()), candidates[0] if candidates else None)
assert cowork, 'Cowork folder not found'
sys.path.insert(0, cowork)  # so `import db.enrich` resolves

# Idempotent — picks up any pending schema changes before we touch the DB.
subprocess.run(['python3', f'{cowork}/db/migrate_runner.py'], check=True)
```

Use the `cowork` variable for every later file path.

## Phase 1 — Backfill missing URLs

Query SQLite for posts whose `url` column is empty/NULL:

```python
import sqlite3
con = sqlite3.connect(f'{cowork}/db/ai_links.db')
con.row_factory = sqlite3.Row
need_urls = con.execute("""
    SELECT id, date, author, handle, subject
    FROM posts
    WHERE url IS NULL OR url = ''
    ORDER BY date DESC
""").fetchall()
```

For each, use the Microsoft 365 Outlook MCP to find the original email:
- Search by sender `slycrel@gmail.com` and a keyword from the author name or subject.
- Use `read_resource` with URI `mail:///messages/{messageId}` to read the full body HTML.
- Extract the URL (look for x.com, twitter.com, github.com, arxiv.org, blog hosts).
- Normalize: strip tracking params (`?s=`, `?t=`, `?utm_*`). Convert `twitter.com` → `x.com`.

**Deduplication:** before persisting a URL, check no other post already has the same normalized URL (other than the row you're updating).

**Persist updates inside the writer lock**:

```python
from db.lock import writer_lock

with writer_lock(timeout=60):
    con = sqlite3.connect(f'{cowork}/db/ai_links.db')
    for post_id, url in url_mapping.items():
        con.execute("UPDATE posts SET url = ?, updated_at = datetime('now') WHERE id = ? AND (url IS NULL OR url = '')", (url, post_id))
    con.commit()
    con.close()
```

If Jeremy invokes only this phase ("just get the URLs"), skip ahead to the rebuild step at the end (still inside the lock).

## Phase 2 — Re-enrich the work queue

Use the canonical helpers to find work and persist results. Status semantics (read `CLAUDE.md` if any are unclear):

- `unattempted` — never tried
- `partial` — capture tried, no usable content (empty article)
- `failed` — outright scrape failure (Chrome unreachable, exception)
- `dead` — confirmed permanent (404, suspended, deleted, login-walled) — **never retried**
- `legacy-ok` — pre-migration enriched; treat as `ok` for reading but eligible for re-enrichment when `ENRICHMENT_VERSION` bumps
- `ok` — fully enriched at the current `ENRICHMENT_VERSION`

### Acquire the writer lock for the batch

```python
from db.lock import writer_lock
from db.enrich import (
    pending_enrichment_ids, record_enrichment, record_partial,
    record_dead, record_failed, status_breakdown, gate_ratio,
    get_post, ENRICHMENT_VERSION,
)

# 60s default timeout is fine for solo use. If acquisition fails, another
# writer (daily sync, curate) is active — wait a minute and try again, or
# tell Jeremy to retry shortly.
with writer_lock(timeout=60):
    # ... all enrichment + rebuild happen inside this block ...
```

### Pick the work list

Default: posts in `partial` / `failed` / `unattempted`, newest first:

```python
ids = pending_enrichment_ids(limit=25)  # tune by request shape
```

For "deep dive on the last month": further restrict by date in your own SQL query. For "just re-scrape the partials": pass `statuses=('partial',)`. For "process everything below the current ENRICHMENT_VERSION" (rolling re-enrichment): also include `legacy-ok` and use the `below_version` parameter.

### Chrome preflight

Chrome runs on Jeremy's Mac. Confirm connectivity once:

1. `tabs_context_mcp` with `createIfEmpty: true`.
2. On "not connected", wait 10s and retry. 5 attempts total (~50s wallclock).
3. Still not connected → for each ID in the work list, call `record_failed(post_id, error="chrome-unreachable", with_lock=False)` (we already hold the lock). Skip to Phase 3.

### Per-post enrichment loop

For each `post_id`:

1. Get the post: `post = get_post(post_id)`. Use `post['url']`.
2. `navigate` to the URL in Chrome.
3. Wait a jittered interval for JS rendering — `setTimeout(()=>r(true), 1500 + Math.random()*4000)` (1.5–5.5s, mean ~3.5s). The variance matters more than the duration: a fixed cadence is the loudest automation signature; the wait being human-shaped is the cheapest mitigation against rate-limiting.
4. Extract structured segments via `javascript_tool`: enumerate `<article>` elements; for each, capture `(text, handle, urls)`. The first article is type `op`; subsequent articles whose handle matches the page handle are `self_reply`; others are `quote`. Detect external links (github / arxiv / huggingface / blog hosts) as their own `external_link` segments.
5. On timeout/empty extraction, retry once after 3s.
6. **Dead detection.** Still failing AND page text contains "post is unavailable" / "account suspended" / "page doesn't exist" / "this Tweet was deleted":
   ```python
   record_dead(post_id, reason=detected_marker,
               summary=f"[Post unavailable — {detected_marker}]",
               with_lock=False)
   ```
   Move on. `dead` posts are permanent and never retried.
7. **Partial.** Still failing without a dead marker:
   ```python
   record_partial(post_id, error="empty capture", with_lock=False)
   ```
   Next catch-up run will retry.
8. **Success.** Compose a concise 1-3 sentence summary capturing what it's about, why it matters, key details (repo links, paper links, specific numbers/benchmarks). Include notable URLs inline as plain text (no markdown linking). Skip generic x.com self-links; prioritize GitHub repos, arxiv papers, product/tool homepages.
   - Good: `"NVIDIA open-sourced OpenShell (github.com/nvidia/openshell) — a sandbox for AI coding agents that locks filesystem, blocks network by default, and injects API keys at runtime only."`
   - Bad: `"Post about a security tool."`

   Re-classify with content in hand. Topic definitions, audience targeting, and priority semantics are in `CLAUDE.md`. With full content you may discover the initial classification (made from the email subject alone) was off — fix it.

   ```python
   record_enrichment(
       post_id=post_id,
       segments=[
           {"type": "op", "handle": author_handle, "text": op_text, "url": post['url']},
           # plus self_reply / quote / external_link segments as captured
       ],
       summary=summary,
       topics=topics,        # list of topic strings — replaces existing
       audiences=audiences,  # list of audience strings — replaces existing
       author=display_name,  # update if email subject's was approximate
       handle=actual_handle,
       views=views_str,
       priority=priority,
       with_lock=False,      # batch already holds the lock
   )
   ```

If Chrome starts rate-limiting or persistently timing out, stop the loop early and report what got done. Don't burn budget retrying — the next catch-up run will pick up where this left off.

### Failures and dead detection — recap

- Transient (timeout, Chrome lost connection mid-batch): `record_failed`. Retries next run.
- Empty capture (page loads but content extraction returns nothing): `record_partial`. Retries next run.
- Permanent (deleted / suspended / login-walled / 404): `record_dead`. **Never retried** — these form the permanent floor in the latent gate.

A post stuck in `partial` after multiple attempts isn't a problem to solve here — the surfacing happens via the `enrichment_attempts` counter, which the viewer will eventually show as a "needs attention" badge.

## Phase 3 — Post-enrichment pipeline (still inside the lock)

The catch-up skill and the daily sync skill run the same tail. After the enrichment loop, call the shared pipeline:

```python
from db.pipeline import post_enrichment_pipeline
pipeline_result = post_enrichment_pipeline(with_lock=False, progress=True)
print(pipeline_result['summary'])
```

This single call does, in order:

1. **Embed** any post whose content changed (or is missing an embedding) using fastembed + bge-small-en-v1.5 (384d). Skips partial/dead posts.
2. **Mechanical discovery** — shared external URLs + shared @mentions → new `concept_observations` rows.
3. **Semantic discovery** — concept-centroid matching at threshold 0.78. Surfaces new candidate evidence for existing concepts.
4. **Rebuild** — regenerates `posts_final_v3.json`, `ai_links_collection_v3.html`, `ai_links_collection_v3.md`.

Each step is idempotent; running the pipeline twice in a row produces the same result as running it once. The pipeline is cheap when there's nothing to do — running it even on a no-enrichment day still cycles mechanical discovery (which may catch newly-correlated URLs as the corpus grows) at trivial cost.

Errors in one step don't abort the others — `pipeline_result['errors']` lists what went wrong. If fastembed isn't installed on the host, the embed + semantic steps surface a clean error and the pipeline still does mechanical + rebuild.

## Phase 4 — Push to GitHub (optional, still inside the lock)

If the catch-up was substantial (more than a handful of enrichments), push to GitHub so the next daily sync sees the work as canonical state:

```python
import subprocess, shutil, os, datetime, time, pathlib

token_path = pathlib.Path(cowork) / '.claude/github_token'
if token_path.exists():
    token = token_path.read_text().strip()
    creds = pathlib.Path.home() / '.git-credentials'
    creds.write_text(f'https://slycrel:{token}@github.com\n')
    creds.chmod(0o600)
    subprocess.run(['git', 'config', '--global', 'credential.helper', 'store'], check=True)
    subprocess.run(['git', 'config', '--global', 'user.name', 'Jeremy Stone'], check=True)
    subprocess.run(['git', 'config', '--global', 'user.email', 'jstone@taxhawk.com'], check=True)

push_dir = f'/tmp/lf-catchup-{int(time.time())}'
subprocess.run(['git', 'clone', 'https://github.com/slycrel/link-farm.git', push_dir], check=True)
subprocess.run(['git', 'config', '--global', '--add', 'safe.directory', push_dir], check=True)
for fname in ['posts_final_v3.json', 'ai_links_collection_v3.html', 'ai_links_collection_v3.md']:
    shutil.copy(f'{cowork}/{fname}', f'{push_dir}/{fname}')
os.makedirs(f'{push_dir}/db', exist_ok=True)
for fname in ['ai_links.db', 'migrate.py', 'migrate_runner.py', 'rebuild.py', 'enrich.py', 'lock.py', '__init__.py']:
    src = f'{cowork}/db/{fname}'
    if os.path.exists(src):
        shutil.copy(src, f'{push_dir}/db/{fname}')

today = datetime.date.today().isoformat()
subprocess.run(['git', '-C', push_dir, 'add', '-A'], check=True)
diff = subprocess.run(['git', '-C', push_dir, 'diff', '--cached', '--stat'], capture_output=True, text=True)
if diff.stdout.strip():
    subprocess.run(['git', '-C', push_dir, 'commit', '-m', f'Catch-up {today}'], check=True)
    subprocess.run(['git', '-C', push_dir, 'push', 'origin', 'main'], check=True)
```

For small invocations (a handful of enrichments), pushing is optional — Monday morning's sync will pick up the local state and push as part of its own run.

## Reporting

After each phase, give Jeremy a clear progress report:

- **Phase 1** (URLs): "Extracted X URLs from Y emails. Z posts still missing URLs."
- **Phase 2** (enrichment): "Re-enriched X posts to `ok`. Y new `partial` (empty capture, will retry next run). Z confirmed `dead` (deleted/suspended). Status breakdown of the corpus: ..."
- **Phase 3** (rebuild + gate): "Rebuilt outputs. Total: N posts. Latent gate ratio: $(partial+failed)/(total-dead) = X.XXX$ — {open|closed} (need <0.05)."
- **Phase 4** (push, if done): "Pushed to GitHub as commit Y."

If Jeremy asked for a specific subset, honor that and skip irrelevant phases. If anything failed, report what failed and what to do next.

## Content types — quick reference

Jeremy categorizes X posts into four content types; the structured-segment scraping handles all of them naturally:

- **Direct posts** — most common. Single `op` segment.
- **Quote tweets** — `op` segment for the quoting tweet plus a `quote` segment for the quoted content. Both visible on the page; the JS extractor surfaces them as separate `<article>` elements.
- **X articles** — long-form. Capture the article body as the `op` segment text (extend the truncation limit if needed) plus any commentary from the author's introducing tweet.
- **Videos** — low priority. Record summary as "Video post by [Author] — bookmarked for manual review", set `sourceType='video'`, persist via `record_partial` (not `ok`) — we know we didn't capture the substance, and a future approach (transcription) might do better.

## Constraints

- Never write `posts.enriched`, `posts.content`, or `posts.summary` directly.
- Never delete posts. Use `record_dead` for tombstones.
- Always acquire `writer_lock()` before mutating SQLite or running rebuild.
- Always call `db.migrate_runner` first — idempotent, picks up any pending schema work.
- For long batches, hold one lock for the whole batch (`with_lock=False` on individual helper calls). For one-off updates, the default `with_lock=True` is fine.
- If the gate ratio is already < 0.05 and Jeremy is asking for catch-up, the work queue is mostly empty — say so and confirm what he wants to do next rather than burning Chrome calls on nothing.
