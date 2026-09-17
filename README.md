# link-farm

Links I've sent myself — mostly X/Twitter posts and GitHub repos — captured from
my phone, enriched automatically, and organized into a concept graph so the
collection stays findable as it grows.

**890 posts** (June 2024 – September 2026), 817 fully enriched, 562 filed into
**54 concepts** derived from the content rather than a fixed taxonomy.

## Start here

| I want to… | Read |
|---|---|
| Browse the collection | `ai_links_collection_v3.html` — self-contained, no build step, just open it |
| Understand how it works | `CLAUDE.md` — the full project context, schema, and curation design decisions |
| Run it on another machine | **`SETUP.md`** — the reconstitution checklist |
| Know why curation works the way it does | `CURATION_DESIGN.md`, `CURATION_REVIEW.md` |
| See what's planned | `ARCHITECTURE_PLAN.md` |

## How it works, briefly

I email links to myself from the iPhone share sheet. A scheduled task runs each
weekday morning: it pulls the canonical state from this repo, checks Outlook for
new mail, extracts and normalizes the URLs, scrapes each post via Chrome,
summarizes and tags it, then runs a pipeline that embeds the content, grows a
concept graph from it, assigns each post a single primary home, regenerates the
HTML/JSON/Markdown artifacts, and pushes everything back here.

**SQLite is the source of truth** (`db/ai_links.db`). The JSON, HTML, and
Markdown files are generated — don't hand-edit them; run `python3 db/rebuild.py`.

Two design choices carry most of the weight, and both are explained at length in
`CLAUDE.md`:

- **Keep what I send.** Anything pushed through the share sheet was deliberate,
  so the intake filter drops only true noise (receipts, alerts). Hype-packaged
  or tangential material gets tagged honestly and kept — the bar is "would I be
  embarrassed by the *tagging*", not by the content.
- **Automation attaches and labels; it never discards.** Edges carry a role.
  `evidence`/`origin` are load-bearing and define what a concept means; `weak` is
  a recorded association that deliberately doesn't vote. Only a human dismisses
  anything.

## Layout

```
posts_final_v3.json            # generated dataset
ai_links_collection_v3.html    # generated viewer (open this)
ai_links_collection_v3.md      # generated markdown companion
db/
  ai_links.db                  # SQLite — source of truth
  pipeline.py                  # the post-enrichment pipeline
  enrich.py                    # canonical write path (never bypass it)
  concepts.py  embeddings.py   # the concept graph + semantic layer
  repo_sync.py                 # PUSH_SPEC — what gets mirrored here
  stats.py                     # regenerates the stats block in CLAUDE.md
  test_*.py                    # roles / lock / recover
scheduled/                     # snapshots of the live scheduled tasks
skills/                        # skills that travel with the repo
```

## Quick checks

```bash
pip install --break-system-packages -r requirements.txt
python3 db/migrate_runner.py      # schema up to date
python3 -m db.stats               # corpus + concept graph summary
python3 -m unittest discover -s db -p 'test_*.py'
```

`db/test_roles.py` is the one that matters most — it guards the four places
where the canonical/weak edge distinction is enforced, each of which fails
*silently* if it regresses.
