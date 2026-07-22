---
name: ai-links-backfill
description: Weekday background re-enrichment of partial/failed AI Links posts at 10:30 AM, after the 9 AM sync settles. Also auto-recovers url-less posts (backfills the URL from Outlook + re-keys to the correct status ID). Chips at the recoverable-incompleteness backlog so the latent-discovery gate can open.
---

> **Versioned snapshot.** The *live* task runs from the Cowork app store at
> `~/Documents/Claude/Scheduled/ai-links-backfill/SKILL.md` (not this file).
> This copy exists so the automation trigger is reproducible on another machine
> or the CLI — see `SETUP.md`. Keep the two in sync. Semantic-stack deps
> (fastembed/numpy) are auto-ensured by the pipeline via `db/ensure_deps.py`.

Weekly background re-enrichment for the AI Links collection (step 8 of `CURATION_DESIGN.md`).

This task runs unattended on weekday mornings at 10:30 local time — about 90 minutes after the 9 AM `ai-links-sync` task. The buffer is intentional: the sync acquires the writer lock and may take 5–15 minutes when it has new emails to enrich. By 10:30 it's reliably done, so this task isn't racing it for Chrome time.

Process a small fixed batch of posts in `partial`, `failed`, or `unattempted` status — drives down the recoverable-incompleteness ratio so the latent-discovery gate (`(partial + failed) / (total − dead) < 0.05`) can eventually open. Different from the interactive `ai-links-catchup` skill — no chat-style back-and-forth, no asks for confirmation. Pick the batch, do the work, report.

Refer to `CLAUDE.md` for project context and `CURATION_DESIGN.md` for the architecture. Needs Claude in Chrome for scraping and the Microsoft 365 connector (Outlook) for the URL-backfill phase.

### Constants for this run

- BATCH_LIMIT = 15 (posts per week — sized to fit ~15 minutes wallclock with Chrome scraping + summarization)
- WALLCLOCK_BUDGET = 15 minutes — stop early if exceeded
- BACKFILL_STATUSES = ('partial', 'failed', 'unattempted')
- URL_BACKFILL_LIMIT = 10 (url-less posts to attempt to recover per run, before the Chrome batch)

Don't process `legacy-ok` posts in this task yet — they're at the previous `ENRICHMENT_VERSION` but they have usable content. Rolling-upgrade-to-current-version is a secondary concern; recovering the actively-broken partial/failed posts is what drives the gate.

### Step 0 — Locate Cowork folder, configure git

```python
import subprocess, pathlib, glob, sys, time
candidates = sorted(glob.glob('/sessions/*/mnt/cowork'))
cowork = next((c for c in candidates if (pathlib.Path(c) / 'CLAUDE.md').exists()), candidates[0] if candidates else None)
assert cowork, 'Cowork folder not found'
sys.path.insert(0, cowork)

# Ensure semantic-stack deps are importable (sandbox doesn't persist installs).
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

### Step 1 — Pull canonical state from GitHub

Same pattern as the daily sync (see `ai-links-sync` skill prompt). The morning sync usually pushed an hour ago, so the remote should match local — but a separate runner (cloud agent, curate session) may have pushed in between. Clone to `/tmp/lf-pull-{ts}`, compare local vs remote, restore if remote is fresher.

### Step 2 — Apply migrations

```python
subprocess.run(['python3', f'{cowork}/db/migrate_runner.py'], check=True)
```

Idempotent.

### Step 2.5 — URL backfill + re-key (auto-recovery for url-less posts)

Some posts get stranded with no usable URL — either `url IS NULL`/`''` or a placeholder sentinel like `'[not found]'` written when ingest failed to extract the link. These are invisible to Chrome enrichment (nothing to navigate to) and, worse, were historically minted with a *hash-derived* id (e.g. `sha256("[not found]")`) instead of the real X status id. They sit in `failed` forever because no other path repairs them. This phase closes that gap. It uses Outlook, not Chrome, so it runs before the Chrome preflight.

```python
from db.recover import url_backfill_candidates, rekey_post
from db.lock import writer_lock
import sqlite3

candidates = url_backfill_candidates()[:10]  # URL_BACKFILL_LIMIT; excludes `dead` tombstones
print(f"URL-backfill: {len(candidates)} url-less post(s) to attempt.")
recovered, rekeyed, still_missing = [], [], []
```

For each candidate, find the original email and recover the URL:
- Search the Microsoft 365 Outlook MCP by sender `slycrel@gmail.com` plus a keyword from the candidate's `author` or `subject` (e.g. the author name). Narrow by the candidate's `date` if multiple hits.
- Read the matching message body via `read_resource` with `mail:///messages/{messageId}`.
- Extract the primary URL from the body HTML (x.com/twitter.com/github.com/arxiv.org/blog hosts). The tweet-card markup wraps the whole card in an `<a href=...>` around a `.../status/{id}` link — pull that. Strip tracking params (`?s=`, `?t=`, `&utm_*`); convert `twitter.com` → `x.com`.
- If no email / no URL found, add to `still_missing` and move on (it'll be retried next run).

Persist recoveries inside the writer lock. `rekey_post` re-derives the correct deterministic id from the URL and migrates the row + all its foreign-key rows onto it; it raises `ValueError` on a merge clash (the canonical id already exists as a different row) — catch and log those for manual review rather than clobbering:

```python
with writer_lock(timeout=60):
    con = sqlite3.connect(f'{cowork}/db/ai_links.db')
    try:
        con.execute("BEGIN")
        for cand in candidates:
            url = recovered_url_for[cand['id']]  # from the Outlook step above; skip if None
            if not url:
                continue
            try:
                new_id = rekey_post(con, cand['id'], url)
                rekeyed.append((cand['id'], new_id))
            except ValueError as e:
                still_missing.append((cand['id'], f"needs manual review: {e}"))
        con.commit()
    except Exception:
        con.rollback(); raise
    finally:
        con.close()
print(f"URL-backfill: re-keyed {len(rekeyed)}, unresolved {len(still_missing)}.")
```

Re-keyed posts now carry a real URL and the correct id, still in `partial`/`failed`/`unattempted` — so Step 3's queue picks them up and Step 5 enriches them this same run. Report the re-keyed pairs and anything left unresolved.

### Step 3 — Check the queue

```python
from db.enrich import pending_enrichment_ids, status_breakdown, gate_ratio

counts = status_breakdown()
ratio, _ = gate_ratio()
print(f"Pre-run: {counts}, gate={ratio:.3f}")

queue = pending_enrichment_ids(limit=15, statuses=('partial', 'failed', 'unattempted'))
if not queue:
    print("Queue empty — gate is open or nothing recoverable left.")
    # If Step 2.5 re-keyed anything, still run the pipeline + push (data changed).
    # Otherwise report and exit cleanly without commit/push.
    return
```

### Step 4 — Chrome preflight

`tabs_context_mcp` with `createIfEmpty: true`. On "not connected", wait 10s and retry; 5 attempts total (~50s wallclock).

If Chrome is unreachable after the preflight attempts, mark every queued post `record_failed(post_id, error="chrome-unreachable", with_lock=False)` inside a lock, then schedule a one-time retry in 4 hours via `mcp__scheduled-tasks__create_scheduled_task`. Skip ahead to the report. Do not run the pipeline or push — nothing changed except attempt counters. (Note: if Step 2.5 re-keyed posts, that IS a real change — run the pipeline + push before exiting even if Chrome is down.)

### Step 5 — Acquire writer lock and process the batch

```python
from db.enrich import record_enrichment, record_partial, record_dead, record_failed, get_post

started_at = time.time()
budget_seconds = 15 * 60

with writer_lock(timeout=60):
    counts_this_run = {'ok': 0, 'partial': 0, 'dead': 0, 'failed': 0}
    for post_id in queue:
        if time.time() - started_at > budget_seconds:
            print(f"Budget exhausted after {counts_this_run}; stopping early.")
            break

        post = get_post(post_id)
        url = post['url']

        # Navigate, wait, extract structured segments (same pattern as ai-links-sync Step 7).
        # On timeout/empty extraction, retry once after 3s.
        # Detect dead markers: "post is unavailable", "account suspended",
        # "page doesn't exist", "this Tweet was deleted".
        # ...
        # Compose summary + topics + audiences + priority from captured content.
        # ...

        # Persist via the right helper
        if dead_marker_detected:
            record_dead(post_id, reason=marker, summary=f"[Post unavailable — {marker}]", with_lock=False)
            counts_this_run['dead'] += 1
        elif scrape_empty:
            record_partial(post_id, error="empty capture", with_lock=False)
            counts_this_run['partial'] += 1
        elif scrape_failed:
            record_failed(post_id, error=str(exc), with_lock=False)
            counts_this_run['failed'] += 1
        else:
            record_enrichment(
                post_id=post_id, segments=segments, summary=summary,
                topics=topics, audiences=audiences, author=author, handle=handle,
                views=views, priority=priority, with_lock=False,
            )
            counts_this_run['ok'] += 1

    # Step 6 — Post-enrichment pipeline (still in the lock)
    from db.pipeline import post_enrichment_pipeline
    pipeline_result = post_enrichment_pipeline(with_lock=False, progress=True)
    print(pipeline_result['summary'])
```

### Step 7 — Push to GitHub (still in the lock)

Same shape as the daily sync's push step. Include `db/ai_links.db`, all regenerated artifacts, `CLAUDE.md`, `CURATION_DESIGN.md`, `requirements.txt`, and the Python modules (`concepts.py`, `embeddings.py`, `pipeline.py`, `perspectives.py`, `enrich.py`, `lock.py`, `recover.py`, `subject_flags.py`, `ensure_deps.py`, `migrate_runner.py`, `rebuild.py`, `migrate.py`, `__init__.py`). Commit message: `Backfill {YYYY-MM-DD}`.

Skip the commit if `git diff --cached` is empty.

### Step 8 — Report

Tell Jeremy:
- URL-backfill results: url-less posts found, re-keyed (old id → new id) pairs, anything left unresolved or flagged for manual review.
- Posts processed this run, breakdown by outcome (ok/partial/dead/failed).
- Pipeline summary (`pipeline_result['summary']`).
- Pre-run vs post-run gate ratio — is the gate closer to opening?
- Remaining `partial` + `failed` count.
- At current rate, estimated weeks to gate-open.
- Any failures (Chrome unreachable, lock timeout, scrape exceptions).
- GitHub push status.

### Constraints

- Never write `posts.enriched`, `posts.content`, `posts.summary`, or `posts.priority` directly — always go through `db/enrich.py` helpers. For url-less repair, go through `db/recover.py` (`rekey_post` / `backfill_and_rekey`) — never hand-mutate `posts.id`.
- BATCH_LIMIT is intentionally small. Don't try to clear the backlog in one run; weekly cadence respects Chrome quota and gives Jeremy a chance to notice if something starts going wrong.
- URL_BACKFILL_LIMIT is also small on purpose — Outlook search per candidate is the slow part. Unresolved candidates persist and are retried next run.
- If a single post fails repeatedly across runs, the `enrichment_attempts` counter grows — the viewer will eventually surface a "needs attention" badge. This task doesn't need to handle that explicitly; just keep retrying within budget.
- If gate ratio already < 0.05 and `partial + failed + unattempted = 0` and Step 2.5 re-keyed nothing, exit cleanly with `"Gate already open — nothing to backfill."` Don't commit, don't push.
- Run the pipeline whenever the queue was non-empty OR Step 2.5 re-keyed something (data changed either way). Skip the pipeline only when there was genuinely nothing to do.
- If anything throws inside a writer-lock block, abort before pushing and report. Releasing the lock is automatic via the context manager.
