# AI Links Collection — Architecture Plan v2

**Date**: March 20, 2026
**Status**: Approved — ready to build

---

## Vision

Two capture paths (Chrome extension for desktop, email relay for mobile) feed into a shared enrichment pipeline that produces fully-formed, screenshot-annotated posts. A separate analytical layer surfaces patterns and recovers edge cases. HTML viewers stay simple and standalone — read-only outputs of the pipeline, not platforms.

The datasets grow over time (email links today, X bookmarks next, potentially other sources later), but the schema, enrichment pipeline, and storage are shared infrastructure. SQLite backs everything; JSON and HTML are generated artifacts.

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│                    CAPTURE LAYER                        │
│                                                         │
│  ┌──────────────────┐      ┌──────────────────────┐    │
│  │ Chrome Extension  │      │ Email Relay Skill     │    │
│  │ (desktop capture) │      │ (phone → Outlook)     │    │
│  │                   │      │                       │    │
│  │ • Click to save   │      │ • Scheduled 9am M-F   │    │
│  │ • DOM access      │      │ • slycrel → jstone    │    │
│  │ • Screenshot on   │      │ • Extract URL from    │    │
│  │   capture         │      │   email body          │    │
│  │ • Bookmark import │      │ • Immediate enrich    │    │
│  └────────┬─────────┘      └──────────┬───────────┘    │
│           │                            │                │
│           └──────────┬─────────────────┘                │
│                      ▼                                  │
│         ┌────────────────────────┐                      │
│         │  SQLite (source of     │                      │
│         │  truth for all posts)  │                      │
│         └────────────┬───────────┘                      │
└──────────────────────┼──────────────────────────────────┘
                       │
┌──────────────────────┼──────────────────────────────────┐
│                      ▼                                  │
│               ENRICHMENT LAYER                          │
│                                                         │
│  ┌──────────────────────────────────────────────────┐   │
│  │ Enrichment Pipeline (shared logic)                │   │
│  │                                                   │   │
│  │ For posts arriving via email (no DOM access):     │   │
│  │ • Scrape URL via Chrome → text, views, threads    │   │
│  │ • Summarize (1-3 sentences)                       │   │
│  │ • Classify topics, audience, priority             │   │
│  │ • Screenshot key passage                          │   │
│  │                                                   │   │
│  │ For posts arriving via extension (already rich):  │   │
│  │ • Validate/normalize extracted data               │   │
│  │ • Summarize if not done at capture                │   │
│  │ • Classify topics, audience, priority             │   │
│  │ • Screenshot already captured at extension time   │   │
│  └──────────────────────────────────────────────────┘   │
│                                                         │
│  ┌──────────────────────────────────────────────────┐   │
│  │ Edge Explorer Skill (depth work)                  │   │
│  │                                                   │   │
│  │ • Dead link recovery (Wayback, repost detection)  │   │
│  │ • Video post review (title, description, context) │   │
│  │ • Quote tweet expansion (capture quoted content)  │   │
│  │ • Thread mining (follow-up replies, GitHub links) │   │
│  │ • Concept clustering (surface thematic groups)    │   │
│  │ • Cross-dataset linking (email posts ↔ bookmarks) │   │
│  └──────────────────────────────────────────────────┘   │
│                                                         │
│  ┌──────────────────────────────────────────────────┐   │
│  │ Screenshot & Re-Enrichment Skill                  │   │
│  │ (repurposed catch-up)                             │   │
│  │                                                   │   │
│  │ • Backlog screenshot capture (254 existing posts) │   │
│  │ • Reclassify general → specific topics            │   │
│  │ • Re-scrape posts with thin summaries             │   │
│  └──────────────────────────────────────────────────┘   │
│                                                         │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│                   OUTPUT LAYER                          │
│                                                         │
│  Generated from SQLite via rebuild scripts.             │
│  Each output is a standalone artifact, not a platform.  │
│                                                         │
│  ┌─────────────────┐  ┌─────────────────┐              │
│  │ Email Links      │  │ Bookmarks       │              │
│  │ Viewer (.html)   │  │ Viewer (.html)  │              │
│  └─────────────────┘  └─────────────────┘              │
│  ┌─────────────────┐  ┌──────────────────┐             │
│  │ Markdown (.md)   │  │ Screenshots/     │             │
│  │ companions       │  │ (PNGs)           │             │
│  └─────────────────┘  └──────────────────┘             │
│  ┌─────────────────┐                                   │
│  │ JSON exports     │  ← for backward compat &         │
│  │ (.json)          │    portability                    │
│  └─────────────────┘                                   │
│                                                         │
│  Rebuild triggered after any data change.               │
└─────────────────────────────────────────────────────────┘
```

---

## Data Layer: SQLite

### Why SQLite

At 254 posts, JSON works fine. At 1200+ (once bookmarks arrive), the pain points multiply: deduplication across datasets requires loading everything into memory, generating different filtered views means JS gymnastics, and schema drift between `posts_final_v3.json` and `bookmarks_v1.json` becomes a real risk. SQLite gives us:

- **One source of truth** for all posts regardless of source
- **Real queries**: "all agent-design posts from the last 3 months that I bookmarked AND emailed" is just SQL
- **Schema enforcement** built in — no drift between datasets
- **Portable**: single file, no server, works everywhere
- **Future-friendly**: concept clustering, cross-referencing, analytics all become SQL queries
- **Concurrent-safe**: multiple processes (extension host, skills) can write without corrupting JSON

### Schema

```sql
CREATE TABLE posts (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    date        TEXT NOT NULL,               -- ISO date (2026-03-16)
    author      TEXT,
    handle      TEXT,
    subject     TEXT,
    url         TEXT,
    summary     TEXT,
    content     TEXT,                        -- full scraped text (for embeddings, re-summarization, search)
    source_type TEXT DEFAULT 'tweet',        -- tweet, article, video, thread
    views       TEXT,
    notes       TEXT,
    enriched    INTEGER DEFAULT 0,           -- boolean
    image       TEXT,                        -- path to screenshot PNG
    source      TEXT DEFAULT 'email',        -- email, bookmark, both
    bookmarked_at TEXT,                      -- ISO timestamp, if from bookmarks
    created_at  TEXT DEFAULT (datetime('now')),
    updated_at  TEXT DEFAULT (datetime('now'))
);

CREATE TABLE post_topics (
    post_id     INTEGER REFERENCES posts(id),
    topic       TEXT NOT NULL,
    PRIMARY KEY (post_id, topic)
);

CREATE TABLE post_audiences (
    post_id     INTEGER REFERENCES posts(id),
    audience    TEXT NOT NULL,
    PRIMARY KEY (post_id, audience)
);

-- Priority stays on the post (single-valued)
-- ALTER TABLE posts ADD COLUMN priority TEXT DEFAULT 'near-term';

CREATE TABLE post_priority (
    -- Actually, keep priority as a column on posts. It's single-valued.
    -- This table is not needed.
);

-- For concept clustering later
CREATE TABLE post_relations (
    post_id_a   INTEGER REFERENCES posts(id),
    post_id_b   INTEGER REFERENCES posts(id),
    relation    TEXT,                        -- 'related', 'contradicts', 'extends', 'quotes'
    notes       TEXT,
    PRIMARY KEY (post_id_a, post_id_b)
);

-- Track link health
CREATE TABLE link_checks (
    post_id     INTEGER REFERENCES posts(id),
    checked_at  TEXT,
    status      INTEGER,                    -- HTTP status code
    notes       TEXT                         -- 'deleted', 'login_wall', 'ok', 'redirected'
);

-- Full-text search
CREATE VIRTUAL TABLE posts_fts USING fts5(
    author, handle, subject, summary, content, notes,
    content=posts,
    content_rowid=id
);
```

### Migration Path

The existing `posts_final_v3.json` (254 posts) gets imported into the SQLite DB as the initial dataset. The JSON file continues to be generated as an export artifact (backward compatibility), but the DB is the source of truth going forward. A simple Python script handles the import:

1. Read JSON, insert into `posts` table
2. Normalize topics/audiences into junction tables
3. Populate FTS index
4. Verify row count matches

### JSON & HTML Generation

After any data change, a rebuild script queries SQLite and generates:

- `posts_final_v3.json` — full export for backward compatibility
- `ai_links_collection_v3.html` — email links viewer
- `ai_links_collection_v3.md` — email links markdown
- `bookmarks_v1.json` — bookmarks export (when ready)
- `bookmarks_v1.html` — bookmarks viewer (separate, when ready)

This is the **single rebuild function** that every skill calls. One place to maintain, one place to update when the schema evolves.

---

## Workstream 1: Chrome Extension

### Purpose
Primary capture path for desktop browsing. Replaces the "email myself" pattern when at a computer, and handles screenshots natively since it's already on the page.

### Core Features

**One-click capture** while browsing X/Twitter:
- Grab URL, author, handle, post text from the DOM
- Screenshot the visible content area (or a user-selected region)
- Quick-classify: present topic pills for one-tap tagging (pre-filled by keyword match)
- Write to SQLite via Native Messaging host

**Bookmark import mode:**
- Navigate to `x.com/i/bookmarks`
- Intercept GraphQL responses as the user scrolls (same approach as twitter-web-exporter)
- Extract bookmark data (URL, author, text, timestamp) from the API responses
- Batch-insert into SQLite with `source: "bookmark"`
- This is the primary mechanism for the 5x bookmark dataset

**Overlay on X/Twitter pages:**
- Subtle indicator if a post is already in the collection
- Quick view of existing metadata (topics, priority)

### Technical Shape

- **Manifest V3** Chrome extension
- **Content script** for DOM extraction and overlay on x.com
- **Background service worker** for GraphQL interception and data persistence
- **Popup UI** for capture confirmation, quick-tag, and import controls
- **Self-hosted**: load unpacked during development, host .crx on internal server for distribution

### File Access: Native Messaging Host

Chrome extensions can't write to the filesystem directly. The **Native Messaging** approach is the cleanest fit for Jeremy's constraints (no background server, no persistent process, self-contained):

- A small Python script registered as a Chrome Native Messaging host
- Chrome launches the script on-demand when the extension sends a message
- The script receives the post data, writes to SQLite, triggers a rebuild, and exits
- No daemon, no server, no port to manage — Chrome handles the process lifecycle
- Registration is a one-time setup: a JSON manifest file pointing to the script

```
Extension                    Chrome                     Native Host (Python)
   │                          │                              │
   ├─── sendNativeMessage ───►│                              │
   │                          ├─── launches process ────────►│
   │                          │                              ├── write to SQLite
   │                          │                              ├── trigger rebuild
   │                          │◄── response ─────────────────┤
   │◄── callback ─────────────┤                              │
   │                          │                              X (process exits)
```

The host script also handles:
- **Offline queue**: if SQLite is locked or unavailable, queue to a temp JSON and flush on next call
- **Rebuild trigger**: after writing, regenerate HTML/Markdown/JSON exports
- **Deduplication**: check URL against existing posts before inserting

---

## Workstream 2: Email Relay Skill (Refactored Sync)

### Purpose
Keeps the phone workflow alive. Jeremy emails himself a link from his phone → the sync skill picks it up, extracts the URL, and pushes it through the full enrichment pipeline. Writes to the same SQLite database.

### What Changes from Current Design

The sync skill (currently specced in CLAUDE.md but never built) gets implemented with **immediate enrichment** — no more two-phase "capture skeleton now, enrich later":

1. Check Outlook for new emails from `slycrel@gmail.com` (since last run)
2. Extract & normalize URLs from email bodies
3. Deduplicate against existing posts in SQLite
4. **Immediately scrape via Chrome** — text, author, handle, views, thread context
5. Summarize, classify topics/audience/priority
6. **Screenshot the key passage** (since we're already on the page)
7. Insert fully-formed post into SQLite
8. Trigger rebuild (HTML + Markdown + JSON)

### Schedule
- **Automated**: weekday mornings at 9 AM (`0 9 * * 1-5`)
- **Manual trigger**: "sync my links" or "check for new emails"

### Relationship to Catch-Up Skill
The current catch-up skill's Phase 1 (URL backfill) and Phase 2 (scrape/enrich) are absorbed into this skill for new posts. The catch-up skill gets repurposed (see Workstream 3).

---

## Workstream 3: Repurposed Catch-Up Skill → Screenshot & Re-Enrichment Pass

### Purpose
The catch-up skill sheds its original responsibilities (now handled at capture time) and becomes the **editorial/screenshot pass** for the existing backlog, plus a re-enrichment tool for posts whose content or classification could improve.

### Screenshot Capture (Primary Mode)
- Query SQLite: `SELECT * FROM posts WHERE enriched = 1 AND image IS NULL`
- Open each URL in Chrome
- AI identifies the most impactful passage (semi-automated v2 from the spec)
- Screenshot that region, crop to content area (no tweet chrome — just the words)
- Save to `screenshots/post-{id}.png`
- Update post's `image` field in SQLite
- Batch-friendly: "screenshot the agent-design posts" or "screenshot the last 50"

### Re-Enrichment (Secondary Mode)
- Re-scrape posts that have changed (author edited, thread grew)
- Reclassify posts that were tagged `general` but might deserve better topics now that we have more context
- Update summaries that are thin or were written from email subjects only

### Trigger Phrases (Updated)
- "catch up on screenshots" / "screenshot my links"
- "re-enrich the [topic] posts"
- "reclassify the general posts"
- Still responds to "catch up on links" but now focuses on screenshots rather than URL backfill

---

## Workstream 4: Edge Explorer Skill (New)

### Purpose
Investigative subagent for deeper work on the collection. This is the "kick the tires" skill — invoked when Jeremy wants to go deeper on a subset of posts or recover edge cases.

### Capabilities

**Dead Link Recovery**
- Query: `SELECT * FROM link_checks WHERE notes IN ('deleted', 'login_wall') ORDER BY checked_at`
- Check Wayback Machine for cached versions
- Search for reposted content (author may have deleted and reposted — two confirmed cases already: James Cowling, fintechjunkie)
- Search X for the author + keywords to find replacement URLs
- Special focus on the Jan 3–16 2026 dead zone

**Video Post Review**
- Query: `SELECT * FROM posts WHERE source_type = 'video' AND summary LIKE '%bookmark%'`
- Open the video page, extract title, description, visible comments/context
- If the video has a companion blog post or GitHub repo, find and link it
- Write a useful summary even without watching the video

**Quote Tweet & Thread Expansion**
- For posts that quote other tweets, follow the quoted content and capture that context
- Mine threads for same-author follow-ups with GitHub links, papers, tools
- For posts that ARE quoted by others, surface the discourse (what are people saying about this?)
- Record relationships in `post_relations` table

**Concept Clustering**
- Surface posts that rhyme conceptually — e.g., all the RAG-related posts across different topics
- Use `post_relations` table to record and query clusters
- Suggest new topic tags or sub-topics when clusters emerge
- Identify contradictions or evolution in thinking (post A says X, post B from 3 months later says the opposite)
- Cross-reference between email links and bookmarks: `SELECT ... WHERE source IN ('email', 'bookmark') AND ...`

**Invocation**
- "dig into the dead links"
- "explore the agent-design posts"
- "find related content for the RAG cluster"
- "what patterns do you see in the last month?"

---

## Workstream 5: X Bookmarks Pipeline

### Purpose
Import and process Jeremy's X bookmarks (estimated 5x+ the size of the email collection) into the same SQLite database with `source: "bookmark"`.

### Approach

**Phase 1: Initial Export**
The Chrome extension's bookmark import mode is the primary mechanism (Workstream 1). As a fallback/bootstrap, a browser extension like X Bookmarks Exporter can do a one-shot CSV/JSON dump that gets imported via script.

**Phase 2: Normalize & Deduplicate**
- Map exported bookmark data to the posts schema
- Insert with `source: "bookmark"`
- Deduplicate against existing posts: if a URL already exists with `source: "email"`, update to `source: "both"` rather than creating a duplicate
- Preserve `bookmarked_at` timestamp if available from the export

**Phase 3: Enrichment**
Run through the same enrichment pipeline — scrape, summarize, classify. This is a large batch job (potentially 1000+ posts), so it needs:
- Batching with progress tracking (update `enriched` flag per-row)
- Graceful failure handling (transaction per post — don't lose progress on crash)
- Incremental saves: SQLite handles this naturally (each INSERT/UPDATE commits)
- Progress query: `SELECT COUNT(*) FROM posts WHERE source = 'bookmark' AND enriched = 0`

**Phase 4: Output**
- Separate bookmarks HTML viewer (generated from SQLite query: `WHERE source IN ('bookmark', 'both')`)
- Separate bookmarks JSON export
- Separate bookmarks Markdown
- Can revisit unification later once we see the volume and overlap

---

## Workstream 6: HTML Viewer Refinements

### Purpose
Polish the viewer(s) for usability before sharing internally. Separate track from the pipeline work.

### Priority Fixes
1. **Screenshot display** — expandable thumbnails in card detail view, lightbox on click, dark-mode friendly
2. **URL state** — encode filters/search/view in the URL hash so links are shareable and back-button works
3. **Post deep-linking** — `#post-42` scrolls to and highlights a specific post
4. **Filter UX** — post count badges on filter pills, "clear all" button, active filter summary
5. **Sort options** — by date (default), by views, by topic, by priority
6. **Performance** — virtual scrolling or pagination if the dataset grows past ~500 posts
7. **Concept clusters** — if `post_relations` data exists, show "Related posts" in the detail view

### Deferred (Post-Sharing)
- Mobile layout improvements
- Keyboard navigation / accessibility
- Internal hosting (serve from a TaxHawk URL)
- RSS/Atom feed generation
- Team annotation layer (comments, reactions)
- Unified cross-dataset viewer (revisit after seeing bookmark volume)

---

## Build Order

### Phase A — Data Foundation
| # | What | Effort | Notes |
|---|------|--------|-------|
| 0 | **SQLite setup + migration** | Small | Create DB, import existing 254 posts from JSON, write the rebuild script. Everything else depends on this. |
| 1 | **Email Relay Skill** | Medium | Implements the missing sync automation. Now writes to SQLite, triggers rebuild. Gets the daily workflow running hands-free with immediate enrichment. |
| 2 | **Repurpose Catch-Up Skill** | Small | Strip Phases 1-2, add screenshot logic. Queries SQLite for un-screenshotted posts. Can start running against the existing 254 posts immediately. |

### Phase B — Chrome Extension
| # | What | Effort | Notes |
|---|------|--------|-------|
| 3 | **Extension MVP** | Medium-Large | One-click capture + screenshot on x.com. Native Messaging host writes to SQLite. No bookmark import yet — just the single-post capture flow. |
| 4 | **Bookmark import mode** | Medium | Add GraphQL interception to the extension. Run the initial bookmark export. Batch-insert into SQLite. |

### Phase C — Depth & Enrichment
| # | What | Effort | Notes |
|---|------|--------|-------|
| 5 | **Bookmark batch enrichment** | Medium | Process 1000+ bookmarks through the shared pipeline. Batched, incremental, crash-safe. |
| 6 | **Edge Explorer Skill** | Medium | Dead link recovery, concept clustering, thread mining. More powerful with both datasets in place. |

### Phase D — Polish & Share
| # | What | Effort | Notes |
|---|------|--------|-------|
| 7 | **Viewer refinements** | Medium | Screenshot display, URL state, sort, filter badges. Both viewers. |
| 8 | **Bookmarks viewer** | Small | Generate from SQLite, reuse viewer template with bookmark-specific defaults. |
| 9 | **Internal sharing** | TBD | Host the viewer(s), add any team-facing features. |

---

## Shared Infrastructure

Things that multiple workstreams depend on, built in Phase A:

- **SQLite database** (`ai_links.db`): Single source of truth. All capture paths write here, all outputs generate from here.
- **Rebuild script** (`rebuild.py` or similar): Queries SQLite, generates JSON + HTML + Markdown. Called by every skill and the Native Messaging host after writes. One place to maintain.
- **URL normalization**: Stripping tracking params, handling x.com vs twitter.com, normalizing mobile URLs. Shared utility function.
- **Schema migrations**: As the schema grows, a simple migration mechanism (version table + SQL scripts) keeps the DB up to date.

---

## Future: Vector Search & Embeddings

When concept clustering and semantic search outgrow keyword matching, the path forward is straightforward:

- **sqlite-vec** (SQLite extension) adds vector search to the existing DB — same single-file, no-server philosophy. No new infrastructure.
- Generate embeddings from the `content` column (full scraped text gives much better embeddings than 2-sentence summaries alone).
- Store in a `post_embeddings` table keyed by `post_id`, or use sqlite-vec's virtual table syntax.
- Semantic search: "find posts similar to this one" becomes a vector distance query.
- The `post_relations` table can be auto-populated by finding posts with high cosine similarity.

Nothing in the current architecture needs to change to support this — the `content` column is the key prerequisite, and it's already in the schema.

---

## Updated CLAUDE.md Changes Needed

When we start building, the CLAUDE.md project context should be updated to reflect:
- SQLite as the source of truth (with JSON/HTML as generated artifacts)
- The two-path capture architecture (extension + email)
- The repurposed catch-up skill (screenshots + re-enrichment)
- The new Edge Explorer skill
- The bookmarks dataset (same DB, `source` column distinguishes)
- The `screenshots/` directory convention
- The Native Messaging host setup for the extension
- Updated collection stats as they change
