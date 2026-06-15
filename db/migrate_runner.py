#!/usr/bin/env python3
"""
Incremental schema migration runner for ai_links.db.

Distinct from migrate.py, which is a one-shot rebuild-from-JSON script
(deletes the DB, recreates from posts_final_v3.json). This runner applies
versioned, incremental schema changes against the live DB — each migration
runs in its own transaction, advancing the schema_version row only on success.

Idempotent: re-running this script after all migrations have applied is a no-op.

Usage:
    python3 db/migrate_runner.py [--db path/to/ai_links.db] [--dry-run]
"""

import sqlite3
import argparse
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
DEFAULT_DB = SCRIPT_DIR / "ai_links.db"


# ---- Migrations ---------------------------------------------------------

def migrate_002_enrichment_status_columns(conn):
    """Add enrichment_status, enrichment_version, attempts/error tracking.

    Does NOT remove the existing `enriched` boolean — that stays in place
    until callers (sync skill, rebuild.py) have been cut over. Both columns
    coexist during the transition.
    """
    conn.executescript("""
        ALTER TABLE posts ADD COLUMN enrichment_status TEXT DEFAULT 'unattempted';
        ALTER TABLE posts ADD COLUMN enrichment_version INTEGER DEFAULT 0;
        ALTER TABLE posts ADD COLUMN enrichment_attempts INTEGER DEFAULT 0;
        ALTER TABLE posts ADD COLUMN enrichment_last_error TEXT;
        ALTER TABLE posts ADD COLUMN enrichment_last_attempt_at TEXT;
        CREATE INDEX IF NOT EXISTS idx_posts_enrichment_status ON posts(enrichment_status);
        CREATE INDEX IF NOT EXISTS idx_posts_enrichment_version ON posts(enrichment_version);
    """)


def migrate_003_thread_segments(conn):
    """Add post_thread_segments table for structured thread capture.

    Replaces the implicit inlined-blob shape of `content`. Each row is one
    segment of the captured thread: OP, self-reply, quote, or external link.
    """
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS post_thread_segments (
            post_id     INTEGER REFERENCES posts(id) ON DELETE CASCADE,
            ordinal     INTEGER NOT NULL,
            type        TEXT NOT NULL,        -- 'op' | 'self_reply' | 'quote' | 'external_link'
            handle      TEXT,
            text        TEXT,
            url         TEXT,
            captured_at TEXT DEFAULT (datetime('now')),
            PRIMARY KEY (post_id, ordinal)
        );
        CREATE INDEX IF NOT EXISTS idx_thread_segments_type ON post_thread_segments(type);
        CREATE INDEX IF NOT EXISTS idx_thread_segments_url ON post_thread_segments(url);
    """)


def migrate_004_post_relations_pk(conn):
    """Fix post_relations PK to include the relation column.

    Original PK was (post_id_a, post_id_b), which prevented a pair from
    carrying multiple relations (e.g., both 'quotes' and 'extends').
    Recreates the table with the corrected PK and copies existing rows.
    """
    conn.executescript("""
        CREATE TABLE post_relations_new (
            post_id_a   INTEGER REFERENCES posts(id) ON DELETE CASCADE,
            post_id_b   INTEGER REFERENCES posts(id) ON DELETE CASCADE,
            relation    TEXT NOT NULL,
            notes       TEXT,
            PRIMARY KEY (post_id_a, post_id_b, relation)
        );

        INSERT INTO post_relations_new (post_id_a, post_id_b, relation, notes)
            SELECT post_id_a, post_id_b, COALESCE(relation, 'related'), notes
            FROM post_relations;

        DROP TABLE post_relations;
        ALTER TABLE post_relations_new RENAME TO post_relations;
    """)


def migrate_005_backfill_enrichment_status(conn):
    """Conservatively backfill enrichment_status from existing data.

    Per design (CURATION_DESIGN.md, Layer 1): NEVER claim 'ok' from the
    legacy `enriched=1` boolean. Map honestly:

      - has real content + non-placeholder summary  → 'legacy-ok' (version 0)
      - enriched=1 but empty content                → 'partial'
      - placeholder/dead-marker summary             → 'dead'
      - enriched=0                                  → 'unattempted' (default)
    """
    cur = conn.cursor()

    # Posts with real content + reasonable summary → 'legacy-ok' (worked at version 0).
    cur.execute("""
        UPDATE posts SET enrichment_status = 'legacy-ok'
        WHERE enriched = 1
          AND content IS NOT NULL AND content != ''
          AND summary IS NOT NULL AND LENGTH(summary) >= 60
          AND summary NOT LIKE '%unavailable%'
          AND summary NOT LIKE '%login wall%'
          AND summary NOT LIKE '%deleted%'
          AND summary NOT LIKE '%suspended%'
          AND summary NOT LIKE '%page doesn''t exist%'
          AND summary NOT LIKE '%no longer available%'
    """)

    # Dead markers in summary → 'dead' (permanent floor, never recovers).
    cur.execute("""
        UPDATE posts SET enrichment_status = 'dead'
        WHERE enriched = 1
          AND (
              summary LIKE '%unavailable%'
              OR summary LIKE '%login wall%'
              OR summary LIKE '%deleted%'
              OR summary LIKE '%suspended%'
              OR summary LIKE '%page doesn''t exist%'
              OR summary LIKE '%no longer available%'
          )
          AND enrichment_status = 'unattempted'
    """)

    # Anything else still flagged enriched=1 but missing content → 'partial'.
    cur.execute("""
        UPDATE posts SET enrichment_status = 'partial'
        WHERE enriched = 1
          AND enrichment_status = 'unattempted'
    """)

    # enriched=0 rows keep the default 'unattempted'. No action needed.


def migrate_007_post_perspectives(conn):
    """Layer 3 perspective lenses: `post_perspectives` overlay table.

    Per CURATION_DESIGN.md Layer 3. The composition-not-inheritance shape:
    `posts.priority` becomes a read-only legacy fallback after this migration;
    all priority writes go to `post_perspectives` rows under the relevant lens.

    Backfill: every existing post gets one `tool-eval` perspective row with
    its current `posts.priority` value, so reads through
    `get_effective_priority(post_id, 'tool-eval')` keep working.

    The `audience` column is intentionally NOT in this schema — per design
    (H4 in the review), `post_audiences` stays as the m2m source of truth.
    If team sharing ever needs per-lens audiences, add a separate
    `post_perspective_audiences(post_id, lens, audience)` junction.
    """
    conn.executescript("""
        CREATE TABLE post_perspectives (
            post_id     INTEGER NOT NULL REFERENCES posts(id) ON DELETE CASCADE,
            lens        TEXT NOT NULL,         -- 'tool-eval' | 'theme' | 'routing' | 'strategy' | 'zeitgeist' | ...
            priority    TEXT,                  -- 'now' | 'near-term' | 'long-term' | NULL
            notes       TEXT,
            updated_at  TEXT DEFAULT (datetime('now')),
            PRIMARY KEY (post_id, lens)
        );
        CREATE INDEX idx_perspectives_lens ON post_perspectives(lens);
        CREATE INDEX idx_perspectives_priority ON post_perspectives(lens, priority);

        -- Seed tool-eval rows from existing posts.priority. tool-eval is the
        -- default lens — the lens-agnostic priority value lives here now.
        INSERT INTO post_perspectives (post_id, lens, priority)
            SELECT id, 'tool-eval', priority FROM posts
             WHERE priority IS NOT NULL;
    """)


def migrate_006_concept_graph(conn):
    """Layer 2 concept graph: concepts, concept_observations, post_concepts
    (canonical), discovery_runs, post_embeddings.

    Per CURATION_DESIGN.md Layer 2. The candidate/canonical split is the
    architectural decision the adversarial review's Takeaway 1 endorsed:
    concept_observations is the immutable provenance log; post_concepts is
    the curator's truth (one row per (post, concept) reflecting Jeremy's
    promote/merge decisions).

    post_embeddings is spec'd here (per Revision 3 of the design doc) so the
    semantic discovery step doesn't have to invent the shape. NOT populated
    by this migration — built in step 6.
    """
    conn.executescript("""
        -- Curated/discovered concepts. A concept is a thread of thinking
        -- that spans multiple posts.
        CREATE TABLE concepts (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            name        TEXT NOT NULL,
            description TEXT,
            source      TEXT NOT NULL DEFAULT 'curated',  -- 'discovered' | 'curated' | 'merged'
            status      TEXT NOT NULL DEFAULT 'active',    -- 'active' | 'archived' | 'merged-into'
            merged_into INTEGER REFERENCES concepts(id),
            created_at  TEXT DEFAULT (datetime('now')),
            updated_at  TEXT DEFAULT (datetime('now'))
        );
        CREATE INDEX idx_concepts_status ON concepts(status);
        CREATE INDEX idx_concepts_source ON concepts(source);

        -- Batch provenance for discovery passes. Helps with reproducibility,
        -- cost tracking, and noticing when a persona/model produces noise.
        CREATE TABLE discovery_runs (
            id                     INTEGER PRIMARY KEY AUTOINCREMENT,
            started_at             TEXT DEFAULT (datetime('now')),
            finished_at            TEXT,
            source                 TEXT NOT NULL,        -- 'mechanical' | 'semantic' | 'latent'
            persona                TEXT,                  -- null for mechanical
            model                  TEXT,                  -- null for mechanical
            sampling_strategy      TEXT,                  -- free-form: 'shared-external-url', 'shared-mention', etc.
            blinding_strategy      TEXT,
            posts_examined         INTEGER,
            observations_created   INTEGER,
            notes                  TEXT
        );
        CREATE INDEX idx_runs_source ON discovery_runs(source);
        CREATE INDEX idx_runs_started_at ON discovery_runs(started_at);

        -- Immutable history. One row per (post, concept) discovery event,
        -- per source/persona/model. Aggregation across rows is a query
        -- concern; multiple rows for the same pair indicate corroboration.
        CREATE TABLE concept_observations (
            id                   INTEGER PRIMARY KEY AUTOINCREMENT,
            post_id              INTEGER NOT NULL REFERENCES posts(id) ON DELETE CASCADE,
            concept_id           INTEGER NOT NULL REFERENCES concepts(id) ON DELETE CASCADE,
            role_suggestion      TEXT NOT NULL DEFAULT 'evidence',  -- 'evidence' | 'counter-example' | 'tangential' | 'origin'
            raw_score            REAL NOT NULL DEFAULT 1.0,         -- NOT comparable across kinds
            score_kind           TEXT NOT NULL,                      -- 'mechanical-overlap' | 'cosine-similarity' | 'llm-self-report'
            source               TEXT NOT NULL,                      -- 'mechanical' | 'semantic' | 'latent'
            discovery_run_id     INTEGER REFERENCES discovery_runs(id),
            discovery_persona    TEXT,
            discovery_model      TEXT,
            status               TEXT NOT NULL DEFAULT 'pending',    -- 'pending' | 'promoted' | 'dismissed' | 'superseded'
            observed_at          TEXT DEFAULT (datetime('now')),
            notes                TEXT
        );
        CREATE INDEX idx_observations_post ON concept_observations(post_id);
        CREATE INDEX idx_observations_concept ON concept_observations(concept_id);
        CREATE INDEX idx_observations_status ON concept_observations(status);
        CREATE INDEX idx_observations_run ON concept_observations(discovery_run_id);

        -- Curator's truth. One row per (post, concept) reflecting the
        -- human's promote decision. Read this when displaying the graph;
        -- query concept_observations for provenance and corroboration.
        CREATE TABLE post_concepts (
            post_id     INTEGER NOT NULL REFERENCES posts(id) ON DELETE CASCADE,
            concept_id  INTEGER NOT NULL REFERENCES concepts(id) ON DELETE CASCADE,
            role        TEXT NOT NULL DEFAULT 'evidence',
            promoted_from_observation_id INTEGER REFERENCES concept_observations(id),
            notes       TEXT,
            promoted_at TEXT DEFAULT (datetime('now')),
            PRIMARY KEY (post_id, concept_id)
        );
        CREATE INDEX idx_post_concepts_concept ON post_concepts(concept_id);

        -- Embedding storage for semantic discovery (step 6). content_hash is
        -- the staleness anchor: re-enrichment changes content → hash mismatch
        -- → invalidate and re-embed.
        CREATE TABLE post_embeddings (
            post_id      INTEGER NOT NULL REFERENCES posts(id) ON DELETE CASCADE,
            model        TEXT NOT NULL,
            dim          INTEGER NOT NULL,
            content_hash TEXT NOT NULL,
            vector       BLOB NOT NULL,
            embedded_at  TEXT DEFAULT (datetime('now')),
            PRIMARY KEY (post_id, model)
        );
        CREATE INDEX idx_embeddings_hash ON post_embeddings(content_hash);
    """)


# ---- Migration list -----------------------------------------------------

# (version_number, short_name, function). Ordered by version.
MIGRATIONS = [
    (2, "Add enrichment_status columns", migrate_002_enrichment_status_columns),
    (3, "Add post_thread_segments table", migrate_003_thread_segments),
    (4, "Fix post_relations PK to include relation", migrate_004_post_relations_pk),
    (5, "Conservative backfill of enrichment_status", migrate_005_backfill_enrichment_status),
    (6, "Concept graph (Layer 2): concepts, observations, post_concepts, discovery_runs, post_embeddings",
     migrate_006_concept_graph),
    (7, "Perspective lenses (Layer 3): post_perspectives overlay + backfill tool-eval rows",
     migrate_007_post_perspectives),
]


# ---- Runner -------------------------------------------------------------

def current_version(conn) -> int:
    """Return the highest applied schema version, or 0 if none."""
    row = conn.execute("SELECT MAX(version) FROM schema_version").fetchone()
    return row[0] or 0 if row else 0


def run_migrations(db_path: Path, dry_run: bool = False) -> int:
    """Apply all pending migrations. Returns final schema version."""
    conn = sqlite3.connect(str(db_path))
    conn.execute("PRAGMA foreign_keys=ON")
    try:
        v = current_version(conn)
        pending = [m for m in MIGRATIONS if m[0] > v]
        print(f"Current schema version: {v}")
        print(f"Pending migrations: {len(pending)}")
        if not pending:
            print("Nothing to do.")
            return v

        for version, name, fn in pending:
            if dry_run:
                print(f"  [dry-run] would apply {version}: {name}")
                continue
            print(f"Applying migration {version}: {name}")
            try:
                conn.execute("BEGIN")
                fn(conn)
                conn.execute(
                    "INSERT INTO schema_version (version) VALUES (?)", (version,)
                )
                conn.commit()
                print(f"  ✓ migration {version} applied")
            except Exception as e:
                conn.rollback()
                print(f"  ✗ migration {version} FAILED — rolled back")
                print(f"    error: {e}")
                raise

        final = current_version(conn)
        print(f"\nFinal schema version: {final}")
        return final
    finally:
        conn.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", type=Path, default=DEFAULT_DB,
                        help="Path to ai_links.db")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show which migrations would apply, don't run them")
    args = parser.parse_args()

    if not args.db.exists():
        raise SystemExit(f"DB not found: {args.db}")

    run_migrations(args.db, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
