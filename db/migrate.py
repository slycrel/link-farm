#!/usr/bin/env python3
"""
Migrate posts_final_v3.json → SQLite database (ai_links.db).

Deterministic ID scheme:
  - X/Twitter URLs: extract the status ID from the URL (snowflake ID)
  - Other URLs: SHA-256 hash of the normalized URL, truncated to 48-bit integer

This ensures the same URL always produces the same ID regardless of import order.
"""

import json
import sqlite3
import hashlib
import re
import sys
from pathlib import Path

# Paths
SCRIPT_DIR = Path(__file__).parent
PROJECT_DIR = SCRIPT_DIR.parent
JSON_PATH = PROJECT_DIR / "posts_final_v3.json"
# Default DB path; can be overridden via CLI arg
DB_PATH = SCRIPT_DIR / "ai_links.db"

# --- ID generation ---

def extract_x_status_id(url: str) -> int | None:
    """Extract the numeric status ID from an X/Twitter URL."""
    match = re.search(r'(?:twitter\.com|x\.com)/\w+/status/(\d+)', url or '')
    if match:
        return int(match.group(1))
    return None


def url_to_hash_id(url: str) -> int:
    """Generate a deterministic integer ID from a URL hash."""
    normalized = normalize_url(url)
    h = hashlib.sha256(normalized.encode()).hexdigest()
    return int(h[:12], 16)  # 48-bit integer, ~281 trillion range


def normalize_url(url: str) -> str:
    """Normalize a URL for deduplication and ID generation."""
    if not url:
        return ""
    url = url.strip().rstrip('/')
    # twitter.com → x.com
    url = url.replace('twitter.com', 'x.com')
    # Strip tracking params
    url = re.sub(r'[?&](s|t|utm_\w+)=[^&]*', '', url)
    # Clean up leftover ? or &
    url = re.sub(r'\?$', '', url)
    url = re.sub(r'\?&', '?', url)
    # Lowercase the domain portion
    parts = url.split('/', 3)
    if len(parts) >= 3:
        parts[2] = parts[2].lower()
    return '/'.join(parts)


def generate_id(url: str) -> int:
    """Generate a deterministic post ID from the URL."""
    status_id = extract_x_status_id(url)
    if status_id:
        return status_id
    return url_to_hash_id(url)


# --- Schema ---

SCHEMA_SQL = """
-- Schema version tracking
CREATE TABLE IF NOT EXISTS schema_version (
    version     INTEGER PRIMARY KEY,
    applied_at  TEXT DEFAULT (datetime('now'))
);

-- Main posts table
CREATE TABLE IF NOT EXISTS posts (
    id          INTEGER PRIMARY KEY,
    date        TEXT NOT NULL,
    author      TEXT,
    handle      TEXT,
    subject     TEXT,
    url         TEXT,
    summary     TEXT,
    content     TEXT,
    source_type TEXT DEFAULT 'tweet',
    views       TEXT,
    notes       TEXT,
    enriched    INTEGER DEFAULT 0,
    image       TEXT,
    priority    TEXT DEFAULT 'near-term',
    source      TEXT DEFAULT 'email',
    bookmarked_at TEXT,
    created_at  TEXT DEFAULT (datetime('now')),
    updated_at  TEXT DEFAULT (datetime('now'))
);

-- Topic junction table (many-to-many)
CREATE TABLE IF NOT EXISTS post_topics (
    post_id     INTEGER REFERENCES posts(id) ON DELETE CASCADE,
    topic       TEXT NOT NULL,
    PRIMARY KEY (post_id, topic)
);

-- Audience junction table (many-to-many)
CREATE TABLE IF NOT EXISTS post_audiences (
    post_id     INTEGER REFERENCES posts(id) ON DELETE CASCADE,
    audience    TEXT NOT NULL,
    PRIMARY KEY (post_id, audience)
);

-- For future concept clustering
CREATE TABLE IF NOT EXISTS post_relations (
    post_id_a   INTEGER REFERENCES posts(id) ON DELETE CASCADE,
    post_id_b   INTEGER REFERENCES posts(id) ON DELETE CASCADE,
    relation    TEXT,
    notes       TEXT,
    PRIMARY KEY (post_id_a, post_id_b)
);

-- Track link health
CREATE TABLE IF NOT EXISTS link_checks (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    post_id     INTEGER REFERENCES posts(id) ON DELETE CASCADE,
    checked_at  TEXT,
    status      INTEGER,
    notes       TEXT
);

-- Full-text search (external content mode)
CREATE VIRTUAL TABLE IF NOT EXISTS posts_fts USING fts5(
    author, handle, subject, summary, content, notes,
    content=posts,
    content_rowid=id
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_posts_date ON posts(date);
CREATE INDEX IF NOT EXISTS idx_posts_url ON posts(url);
CREATE INDEX IF NOT EXISTS idx_posts_source ON posts(source);
CREATE INDEX IF NOT EXISTS idx_posts_enriched ON posts(enriched);
CREATE INDEX IF NOT EXISTS idx_post_topics_topic ON post_topics(topic);
CREATE INDEX IF NOT EXISTS idx_post_audiences_audience ON post_audiences(audience);
"""


def create_db(db_path: Path) -> sqlite3.Connection:
    """Create the database and schema."""
    conn = sqlite3.connect(str(db_path))
    conn.execute("PRAGMA journal_mode=DELETE")
    conn.execute("PRAGMA foreign_keys=ON")
    conn.executescript(SCHEMA_SQL)
    conn.execute("INSERT OR IGNORE INTO schema_version (version) VALUES (1)")
    conn.commit()
    return conn


def import_posts(conn: sqlite3.Connection, json_path: Path) -> dict:
    """Import posts from JSON into SQLite. Returns stats dict."""
    with open(json_path) as f:
        posts = json.load(f)

    stats = {
        "total": len(posts),
        "imported": 0,
        "skipped_duplicate_url": 0,
        "skipped_duplicate_id": 0,
        "id_collisions": [],
    }

    seen_urls = set()
    seen_ids = set()

    for i, post in enumerate(posts):
        url = post.get("url", "")
        normalized = normalize_url(url)

        # Deduplicate by normalized URL
        if normalized and normalized in seen_urls:
            stats["skipped_duplicate_url"] += 1
            print(f"  Skipping duplicate URL at index {i}: {url}")
            continue
        if normalized:
            seen_urls.add(normalized)

        # Generate deterministic ID
        post_id = generate_id(url)

        # Handle ID collision (shouldn't happen, but safety check)
        if post_id in seen_ids:
            # Append index to differentiate
            original_id = post_id
            post_id = post_id + i
            stats["id_collisions"].append((original_id, post_id, url))
            print(f"  ID collision resolved: {original_id} → {post_id} for {url}")

        seen_ids.add(post_id)

        # Insert post
        conn.execute("""
            INSERT INTO posts (id, date, author, handle, subject, url, summary, content,
                             source_type, views, notes, enriched, priority, source)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            post_id,
            post.get("date", ""),
            post.get("author", ""),
            post.get("handle", ""),
            post.get("subject", ""),
            url,
            post.get("summary", ""),
            post.get("content", ""),
            post.get("sourceType", "tweet"),
            post.get("views", ""),
            post.get("notes", ""),
            1 if post.get("enriched") else 0,
            post.get("priority", "near-term"),
            "email",
        ))

        # Insert topics
        for topic in post.get("topics", []):
            conn.execute(
                "INSERT OR IGNORE INTO post_topics (post_id, topic) VALUES (?, ?)",
                (post_id, topic)
            )

        # Insert audiences
        for audience in post.get("audience", []):
            conn.execute(
                "INSERT OR IGNORE INTO post_audiences (post_id, audience) VALUES (?, ?)",
                (post_id, audience)
            )

        stats["imported"] += 1

    # Populate FTS index
    conn.execute("""
        INSERT INTO posts_fts (rowid, author, handle, subject, summary, content, notes)
        SELECT id, author, handle, subject, summary, content, notes FROM posts
    """)

    conn.commit()
    return stats


def verify(conn: sqlite3.Connection, json_path: Path) -> bool:
    """Verify the import produced correct data."""
    with open(json_path) as f:
        posts = json.load(f)

    # Deduplicate expected count (matching migration logic)
    seen_urls = set()
    expected = 0
    for post in posts:
        normalized = normalize_url(post.get("url", ""))
        if normalized and normalized in seen_urls:
            continue
        if normalized:
            seen_urls.add(normalized)
        expected += 1

    # Check counts
    row_count = conn.execute("SELECT COUNT(*) FROM posts").fetchone()[0]
    topic_count = conn.execute("SELECT COUNT(*) FROM post_topics").fetchone()[0]
    audience_count = conn.execute("SELECT COUNT(*) FROM post_audiences").fetchone()[0]
    fts_count = conn.execute("SELECT COUNT(*) FROM posts_fts").fetchone()[0]

    print(f"\nVerification:")
    print(f"  Expected posts: {expected}")
    print(f"  Posts in DB:    {row_count}")
    print(f"  Topic links:    {topic_count}")
    print(f"  Audience links: {audience_count}")
    print(f"  FTS entries:    {fts_count}")

    ok = row_count == expected and fts_count == expected
    if ok:
        print("  ✓ Row counts match")
    else:
        print("  ✗ Row count mismatch!")

    # Spot-check: verify topics round-trip
    sample = conn.execute("""
        SELECT p.id, p.author, GROUP_CONCAT(pt.topic, ',') as topics
        FROM posts p
        LEFT JOIN post_topics pt ON p.id = pt.post_id
        GROUP BY p.id
        ORDER BY p.date DESC
        LIMIT 5
    """).fetchall()
    print(f"\n  Sample posts (5 most recent):")
    for row in sample:
        print(f"    ID {row[0]}: {row[1]} → topics: {row[2]}")

    # Check date range
    date_range = conn.execute("SELECT MIN(date), MAX(date) FROM posts").fetchone()
    print(f"\n  Date range: {date_range[0]} to {date_range[1]}")

    return ok


def main():
    global DB_PATH
    if len(sys.argv) > 1:
        DB_PATH = Path(sys.argv[1])
    print(f"Source: {JSON_PATH}")
    print(f"Target: {DB_PATH}")

    if DB_PATH.exists():
        print(f"\nRemoving existing database...")
        DB_PATH.unlink()

    print(f"\nCreating database and schema...")
    conn = create_db(DB_PATH)

    print(f"\nImporting posts...")
    stats = import_posts(conn, JSON_PATH)

    print(f"\nImport stats:")
    print(f"  Total in JSON:          {stats['total']}")
    print(f"  Imported:               {stats['imported']}")
    print(f"  Skipped (dup URL):      {stats['skipped_duplicate_url']}")
    print(f"  Skipped (dup ID):       {stats['skipped_duplicate_id']}")
    if stats['id_collisions']:
        print(f"  ID collisions resolved: {len(stats['id_collisions'])}")

    ok = verify(conn, JSON_PATH)
    conn.close()

    if ok:
        print(f"\n✓ Migration complete: {DB_PATH}")
        print(f"  Size: {DB_PATH.stat().st_size / 1024:.1f} KB")
    else:
        print(f"\n✗ Migration had issues — review above")
        sys.exit(1)


if __name__ == "__main__":
    main()
