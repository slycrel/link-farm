#!/usr/bin/env python3
"""Search the link collection from the command line.

    python3 -m db.search "supply chain"                       # keyword, best match first
    python3 -m db.search litellm --since 2026-03-01           # posted on/after (falls back to capture date)
    python3 -m db.search mcp --handle karpathy --topic claude-code
    python3 -m db.search "github.com/mattpocock" --links      # show every extracted link
    python3 -m db.search --concept "dependency risk" --limit 50   # members of a concept (name substring)

Reads the `post_search` index that db/rebuild.py refreshes on every run (covers
summary, captured text, topics, ALL concept names, external links, URL and posted
date). Keyword syntax is FTS5: quoted phrases, AND/OR/NOT, prefix*, column:term
(e.g. `links:arxiv`, `concepts:harness`). Read-only.
"""
import argparse
import sqlite3
import sys
from pathlib import Path

DB = Path(__file__).parent / "ai_links.db"


def search(query=None, since=None, until=None, handle=None, topic=None,
           concept=None, limit=20, db=DB):
    conn = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    where, params = [], []
    if query:
        where.append("post_search MATCH ?")
        params.append(query)
    if since:
        where.append("COALESCE(NULLIF(substr(p.posted_at,1,10),''), p.date) >= ?")
        params.append(since)
    if until:
        where.append("COALESCE(NULLIF(substr(p.posted_at,1,10),''), p.date) <= ?")
        params.append(until)
    if handle:
        where.append("lower(p.handle) LIKE ?")
        params.append("%" + handle.lower().lstrip("@") + "%")
    if topic:
        where.append("EXISTS (SELECT 1 FROM post_topics t WHERE t.post_id=p.id AND t.topic=?)")
        params.append(topic)
    if concept:
        where.append("p.id IN (SELECT pc.post_id FROM post_concepts pc JOIN concepts c ON c.id=pc.concept_id"
                     " WHERE lower(c.name) LIKE ? AND pc.role IN ('evidence','origin'))")
        params.append("%" + concept.lower() + "%")
    order = "ORDER BY bm25(post_search)" if query else "ORDER BY COALESCE(p.posted_at, p.date) DESC"
    sql = (f"SELECT p.id, p.date, p.posted_at, p.author, p.handle, p.url, p.summary "
           f"FROM post_search s JOIN posts p ON p.id = s.rowid " if query else
           f"SELECT p.id, p.date, p.posted_at, p.author, p.handle, p.url, p.summary FROM posts p ")
    if where:
        sql += "WHERE " + " AND ".join(where) + " "
    sql += order + " LIMIT ?"
    params.append(limit)
    return conn.execute(sql, params).fetchall(), conn


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("query", nargs="?", help="FTS5 query")
    ap.add_argument("--since"); ap.add_argument("--until")
    ap.add_argument("--handle"); ap.add_argument("--topic"); ap.add_argument("--concept")
    ap.add_argument("--limit", type=int, default=20)
    ap.add_argument("--links", action="store_true", help="print extracted links for each hit")
    a = ap.parse_args(argv)
    if not any([a.query, a.concept, a.handle, a.topic, a.since, a.until]):
        ap.error("give a query or at least one filter")
    rows, conn = search(a.query, a.since, a.until, a.handle, a.topic, a.concept, a.limit)
    for r in rows:
        posted = (r["posted_at"] or "")[:10] or "?"
        print(f"{posted} (added {r['date']}) {r['handle'] or r['author']}  {r['url']}")
        print(f"    {(r['summary'] or '')[:200]}")
        if a.links:
            ln = conn.execute("SELECT links FROM post_search WHERE rowid=?", (r["id"],)).fetchone()
            if ln and ln[0]:
                print(f"    links: {ln[0]}")
    print(f"-- {len(rows)} result(s)", file=sys.stderr)


if __name__ == "__main__":
    main()
