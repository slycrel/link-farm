#!/usr/bin/env python3
"""
Rebuild all output artifacts from the SQLite database.

Generates:
  - posts_final_v3.json  (backward-compatible JSON export)
  - ai_links_collection_v3.html  (self-contained dark-mode viewer)
  - ai_links_collection_v3.md  (markdown companion)

Usage:
  python3 rebuild.py [--db path/to/ai_links.db] [--out path/to/output/dir]
"""

import json
import sqlite3
import re
import sys
from pathlib import Path
from collections import defaultdict
from datetime import datetime

SCRIPT_DIR = Path(__file__).parent
DEFAULT_DB = SCRIPT_DIR / "ai_links.db"
DEFAULT_OUT = SCRIPT_DIR.parent  # project root

TOPIC_ORDER = [
    'agent-design', 'claude-code', 'dev-practices', 'skills-mcp',
    'prompting', 'research', 'industry', 'management', 'questionable', 'general'
]

TOPIC_LABELS = {
    'agent-design': 'Agent Design',
    'claude-code': 'Claude Code',
    'dev-practices': 'Dev Practices',
    'skills-mcp': 'Skills & MCP',
    'prompting': 'Prompting',
    'research': 'Research',
    'industry': 'Industry',
    'management': 'Management',
    'general': 'General',
    'questionable': 'Questionable',
}


# --- Data access ---

def load_posts(db_path: Path) -> list[dict]:
    """Load all posts from SQLite with topics and audiences joined."""
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row

    posts = []
    rows = conn.execute("SELECT * FROM posts ORDER BY date DESC, id DESC").fetchall()

    for row in rows:
        post_id = row['id']

        topics = [r[0] for r in conn.execute(
            "SELECT topic FROM post_topics WHERE post_id = ? ORDER BY rowid", (post_id,)
        ).fetchall()]

        audiences = [r[0] for r in conn.execute(
            "SELECT audience FROM post_audiences WHERE post_id = ? ORDER BY rowid", (post_id,)
        ).fetchall()]

        posts.append({
            'id': post_id,
            'date': row['date'],
            'author': row['author'] or '',
            'handle': row['handle'] or '',
            'subject': row['subject'] or '',
            'url': row['url'] or '',
            'summary': row['summary'] or '',
            'content': row['content'] or '',
            'topics': topics,
            'audience': audiences,
            'priority': row['priority'] or 'near-term',
            'sourceType': row['source_type'] or 'tweet',
            'views': row['views'] or '',
            'notes': row['notes'] or '',
            'enriched': bool(row['enriched']),
            'image': row['image'] or '',
            'source': row['source'] or 'email',
        })

    conn.close()
    return posts


# --- JSON generation ---

def generate_json(posts: list[dict], out_path: Path):
    """Generate backward-compatible JSON export."""
    # Export format matches the original schema — only additive changes
    export = []
    for p in posts:
        entry = {
            'date': p['date'],
            'author': p['author'],
            'handle': p['handle'],
            'subject': p['subject'],
            'url': p['url'],
            'summary': p['summary'],
            'topics': p['topics'],
            'audience': p['audience'],
            'priority': p['priority'],
            'sourceType': p['sourceType'],
            'views': p['views'],
            'notes': p['notes'],
            'enriched': p['enriched'],
        }
        # Additive fields — only include if non-empty
        if p.get('content'):
            entry['content'] = p['content']
        if p.get('image'):
            entry['image'] = p['image']
        if p.get('source') and p['source'] != 'email':
            entry['source'] = p['source']

        export.append(entry)

    with open(out_path, 'w') as f:
        json.dump(export, f, indent=2, ensure_ascii=False)

    print(f"  JSON: {len(export)} posts → {out_path.name}")


# --- HTML generation ---

def js_escape(s: str) -> str:
    """Escape a string for embedding in a JS single-quoted string."""
    if not s:
        return ''
    return (s
        .replace('\\', '\\\\')
        .replace("'", "\\'")
        .replace('\n', '\\n')
        .replace('\r', '')
        .replace('\t', '\\t'))


def generate_posts_js_array(posts: list[dict]) -> str:
    """Generate the JS POSTS array content (without the const declaration)."""
    lines = []
    for i, p in enumerate(posts):
        topics_js = json.dumps(p['topics'])
        audience_js = json.dumps(p['audience'])

        line = (
            f"  {{ id: 'post-{i}', "
            f"date: '{js_escape(p['date'])}', "
            f"author: '{js_escape(p['author'])}', "
            f"handle: '{js_escape(p['handle'])}', "
            f"subject: '{js_escape(p['subject'])}', "
            f"url: '{js_escape(p['url'])}', "
            f"summary: '{js_escape(p['summary'])}', "
            f"topics: {topics_js}, "
            f"audience: {audience_js}, "
            f"priority: '{js_escape(p['priority'])}', "
            f"sourceType: '{js_escape(p['sourceType'])}', "
            f"views: '{js_escape(p['views'])}', "
            f"notes: '{js_escape(p['notes'])}', "
            f"enriched: {'true' if p['enriched'] else 'false'}, "
            f"content: '{js_escape(p.get('content', ''))}' }}"
        )
        if i < len(posts) - 1:
            line += ','
        lines.append(line)

    return '\n'.join(lines)


def generate_html(posts: list[dict], html_template_path: Path, out_path: Path):
    """Regenerate the HTML by replacing the POSTS array in the existing template."""
    with open(html_template_path) as f:
        html = f.read()

    # Find and replace the POSTS array
    # Pattern: from "const POSTS = [" to the matching "];"
    start_marker = 'const POSTS = ['
    end_marker = '];'

    start_idx = html.index(start_marker)
    # Find the end marker after the start
    # We need to find the "];" that closes the POSTS array
    # The array content is between the "[" and "];"
    bracket_start = start_idx + len(start_marker) - 1  # position of "["

    # Find the matching "];" — scan forward counting brackets
    depth = 1
    pos = bracket_start + 1
    while depth > 0 and pos < len(html):
        if html[pos] == '[':
            depth += 1
        elif html[pos] == ']':
            depth -= 1
        pos += 1
    # pos is now right after the closing "]"
    end_idx = pos  # should point to ";"

    new_array = generate_posts_js_array(posts)
    new_section = f'const POSTS = [\n{new_array}\n]'

    html = html[:start_idx] + new_section + html[end_idx:]

    with open(out_path, 'w') as f:
        f.write(html)

    print(f"  HTML: {len(posts)} posts → {out_path.name}")


# --- Markdown generation ---

def truncate(s: str, max_len: int = 70) -> str:
    """Truncate a string with ellipsis."""
    if not s or len(s) <= max_len:
        return s
    return s[:max_len].rstrip() + '...'


def generate_markdown(posts: list[dict], out_path: Path):
    """Generate the markdown companion file."""
    total = len(posts)
    enriched_count = sum(1 for p in posts if p['enriched'])
    dates = [p['date'] for p in posts if p['date']]
    date_min = min(dates) if dates else 'N/A'
    date_max = max(dates) if dates else 'N/A'

    lines = []

    # Header
    lines.append('# AI Links Collection')
    lines.append(f'**Total Posts**: {total}  ')
    lines.append(f'**Date Range**: {date_min} – {date_max}  ')
    lines.append(f'**Enriched**: {enriched_count}/{total} ({100*enriched_count//total if total else 0}%)')
    lines.append('')

    # Topic distribution
    topic_counts = defaultdict(int)
    for p in posts:
        for t in p['topics']:
            topic_counts[t] += 1

    lines.append('---')
    lines.append('## Topic Distribution')
    lines.append('| Topic | Count | % |')
    lines.append('|-------|-------|---|')
    for topic in TOPIC_ORDER:
        count = topic_counts.get(topic, 0)
        pct = f'{100*count/total:.1f}%' if total else '0%'
        lines.append(f'| {topic} | {count} | {pct} |')
    lines.append('')

    # Quick Reference (50 most recent)
    lines.append('---')
    lines.append('## Quick Reference (50 Most Recent)')
    lines.append('| Date | Author | Topic | Summary |')
    lines.append('|------|--------|-------|--------|')
    for p in posts[:50]:
        primary_topic = p['topics'][0] if p['topics'] else 'general'
        summary_trunc = truncate(p['summary'])
        lines.append(f"| {p['date']} | {p['author']} | {primary_topic} | {summary_trunc} |")
    lines.append('')

    # Posts by Topic
    lines.append('---')
    lines.append('## Posts by Topic')
    lines.append('')

    posts_by_topic = defaultdict(list)
    for p in posts:
        if not p['topics']:
            posts_by_topic['general'].append(p)
        else:
            for t in p['topics']:
                posts_by_topic[t].append(p)

    for topic in TOPIC_ORDER:
        topic_posts = posts_by_topic.get(topic, [])
        if not topic_posts:
            continue
        label = TOPIC_LABELS.get(topic, topic)
        lines.append(f'### {label} ({len(topic_posts)})')
        lines.append('')
        for p in topic_posts:
            url_part = f'[{p["author"]}]({p["url"]})' if p['url'] else p['author']
            lines.append(f'- {url_part} — {p["date"]}: {p["summary"]}')
            lines.append('')

    # Full Chronological List
    lines.append('---')
    lines.append('## Full Chronological List')
    lines.append('')

    # Group by month
    posts_by_month = defaultdict(list)
    for p in posts:
        if p['date']:
            month_key = p['date'][:7]  # YYYY-MM
        else:
            month_key = 'unknown'
        posts_by_month[month_key].append(p)

    for month_key in sorted(posts_by_month.keys(), reverse=True):
        month_posts = posts_by_month[month_key]
        # Format month header
        if month_key != 'unknown':
            try:
                dt = datetime.strptime(month_key, '%Y-%m')
                header = dt.strftime('%b %Y')
            except ValueError:
                header = month_key
        else:
            header = 'Unknown Date'

        lines.append(f'### {header}')
        lines.append('')
        for p in month_posts:
            topics_str = ', '.join(p['topics']) if p['topics'] else 'general'
            url_part = f'[{p["author"]}]({p["url"]})' if p['url'] else p['author']
            lines.append(f'- **{p["date"]}** | {url_part} | {topics_str}')
            lines.append(f'  {p["summary"]}')
            lines.append('')

    with open(out_path, 'w') as f:
        f.write('\n'.join(lines))

    print(f"  Markdown: {total} posts → {out_path.name}")


# --- Main ---

def rebuild(db_path: Path = None, out_dir: Path = None):
    """Main rebuild function — can be called from other scripts."""
    db_path = db_path or DEFAULT_DB
    out_dir = out_dir or DEFAULT_OUT

    print(f"Rebuilding from: {db_path}")
    print(f"Output dir: {out_dir}")

    posts = load_posts(db_path)
    print(f"Loaded {len(posts)} posts from SQLite")

    generate_json(posts, out_dir / 'posts_final_v3.json')
    generate_html(posts, out_dir / 'ai_links_collection_v3.html', out_dir / 'ai_links_collection_v3.html')
    generate_markdown(posts, out_dir / 'ai_links_collection_v3.md')

    print(f"\n✓ Rebuild complete ({len(posts)} posts)")
    return posts


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Rebuild output artifacts from SQLite')
    parser.add_argument('--db', type=Path, default=DEFAULT_DB, help='Path to SQLite database')
    parser.add_argument('--out', type=Path, default=DEFAULT_OUT, help='Output directory')
    args = parser.parse_args()

    rebuild(args.db, args.out)


if __name__ == "__main__":
    main()
