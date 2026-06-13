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


# ---- Migration list -----------------------------------------------------

# (version_number, short_name, function). Ordered by version.
MIGRATIONS = [
    (2, "Add enrichment_status columns", migrate_002_enrichment_status_columns),
    (3, "Add post_thread_segments table", migrate_003_thread_segments),
    (4, "Fix post_relations PK to include relation", migrate_004_post_relations_pk),
    (5, "Conservative backfill of enrichment_status", migrate_005_backfill_enrichment_status),
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
