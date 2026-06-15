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
import os
import sqlite3
import re
import sys
import tempfile
from pathlib import Path
from collections import defaultdict
from datetime import datetime

# Writer lock is shared across all writers (sync, catch-up, curate, rebuild).
try:
    from .lock import writer_lock
except ImportError:
    sys.path.insert(0, str(Path(__file__).parent))
    from lock import writer_lock

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

# Hard caps on the morning view. Per CURATION_DESIGN.md these are guesses to
# tune by use; the *shape* of fixed-size sections matters more than the exact
# numbers. Infinite-scroll surfaces violate the attention budget the system
# exists to protect.
MORNING_READ_NOW_CAP = 5
MORNING_RECURRING_CAP = 5
MORNING_REVISIT_CAP = 2

# Days of grace before a `now`/`near-term` post counts as "revisit" material.
MORNING_REVISIT_MIN_AGE_DAYS = 30
MORNING_READ_NOW_RECENT_DAYS = 7
# Recurring window is the design doc's "this week" loosely — 14 days gives a
# meaningful set at current corpus density. Tune as concept count grows.
MORNING_RECURRING_WINDOW_DAYS = 14


# --- Morning view computation ---

def _parse_date(date_str: str):
    """Return a datetime.date or None for malformed inputs."""
    try:
        return datetime.strptime(date_str, '%Y-%m-%d').date()
    except (TypeError, ValueError):
        return None


def _topic_label(topic: str) -> str:
    return TOPIC_LABELS.get(topic, topic)


def _one_line_reason(p: dict) -> str:
    """Compose a short 'why this surfaced' tag for a morning-view post."""
    parts = []
    if p.get('priority'):
        parts.append(p['priority'])
    primary_topic = (p.get('topics') or ['general'])[0]
    parts.append(_topic_label(primary_topic))
    if p.get('views'):
        parts.append(f"{p['views']} views")
    # Quality / status hints — useful given the legacy-ok vs ok distinction.
    status = p.get('enrichment_status') or ''
    if status == 'ok':
        parts.append('v1 enriched')
    elif status == 'legacy-ok':
        parts.append('legacy enrichment')
    elif status == 'partial':
        parts.append('partial capture')
    return ' • '.join(parts)


def compute_morning_view(posts: list[dict], today=None) -> dict:
    """Compute the daily morning surface from the full post list.

    Returns a dict with three lists ('read_now', 'recurring', 'revisit') and
    a meta header. Each section is hard-capped; passing in 50K posts will
    produce the same shape as passing in 50.

    `read_now`     — high-confidence near-term-actionable posts captured
                     in the last MORNING_READ_NOW_RECENT_DAYS. Priority 'now'
                     ranks above 'near-term'. Excludes `dead` and `partial`.
    `recurring`    — placeholder until Layer 2 (concept graph) lands. The
                     viewer renders a "Concept tracking activates with Layer 2"
                     message for this section.
    `revisit`      — posts marked 'now' or 'near-term' that are
                     MORNING_REVISIT_MIN_AGE_DAYS+ old. The "did I actually
                     pay attention to what I said was urgent" check.
    """
    today = today or datetime.utcnow().date()
    recent_cutoff = today.toordinal() - MORNING_READ_NOW_RECENT_DAYS
    revisit_cutoff = today.toordinal() - MORNING_REVISIT_MIN_AGE_DAYS

    read_now: list[dict] = []
    revisit: list[dict] = []
    for p in posts:
        d = _parse_date(p.get('date'))
        if d is None:
            continue
        status = p.get('enrichment_status') or ''
        if status == 'dead':
            continue  # don't surface dead posts in the daily view
        priority = p.get('priority') or ''

        # Read now: recent + priority is now/near-term + meaningfully enriched.
        if d.toordinal() >= recent_cutoff and priority in ('now', 'near-term') \
                and status in ('ok', 'legacy-ok'):
            read_now.append(p)

        # Revisit: older actionable posts that should have been acted on.
        elif d.toordinal() <= revisit_cutoff and priority in ('now', 'near-term') \
                and status in ('ok', 'legacy-ok'):
            revisit.append(p)

    # Rank read_now: `now` > `near-term`, then by date desc.
    priority_rank = {'now': 0, 'near-term': 1, 'long-term': 2}
    read_now.sort(key=lambda p: (
        priority_rank.get(p.get('priority') or '', 9),
        -(_parse_date(p.get('date')).toordinal() if _parse_date(p.get('date')) else 0),
    ))
    read_now = read_now[:MORNING_READ_NOW_CAP]

    # Revisit: oldest "still on the list" goes first — they're the most-stale.
    revisit.sort(key=lambda p: _parse_date(p.get('date')).toordinal() if _parse_date(p.get('date')) else 0)
    revisit = revisit[:MORNING_REVISIT_CAP]

    def _slim(p: dict) -> dict:
        return {
            'id': p.get('id'),
            'date': p.get('date'),
            'author': p.get('author'),
            'handle': p.get('handle'),
            'url': p.get('url'),
            'summary': p.get('summary'),
            'topics': p.get('topics') or [],
            'priority': p.get('priority'),
            'views': p.get('views'),
            'reason': _one_line_reason(p),
        }

    return {
        'generated_at': datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
        'read_now': [_slim(p) for p in read_now],
        'recurring': _compute_recurring_section(),
        'revisit': [_slim(p) for p in revisit],
    }


def _compute_recurring_section() -> dict:
    """Build the 'Recurring this week' section from the concept graph.

    Imports db.concepts lazily so a stale DB without migration 6 still
    produces a sensible (empty) section instead of erroring on import.
    """
    try:
        try:
            from .concepts import recent_active_concepts, top_posts_for_concept
        except ImportError:
            # Run as `python3 db/rebuild.py` — package context not set up.
            import sys as _sys
            _sys.path.insert(0, str(Path(__file__).parent))
            from concepts import recent_active_concepts, top_posts_for_concept
    except Exception as e:
        return {
            'placeholder': True,
            'message': f'Concept graph unavailable: {e}',
        }

    try:
        concepts = recent_active_concepts(
            days=MORNING_RECURRING_WINDOW_DAYS,
            limit=MORNING_RECURRING_CAP,
        )
    except Exception as e:
        # Tables might not exist yet on a fresh-from-old-snapshot DB.
        return {
            'placeholder': True,
            'message': f'Concept graph not yet initialized: {e}',
        }

    if not concepts:
        return {
            'placeholder': True,
            'message': (
                f'No concepts gained new evidence in the last '
                f'{MORNING_RECURRING_WINDOW_DAYS} days. Run mechanical discovery '
                f'or seed curated concepts to populate this section.'
            ),
        }

    items = []
    for c in concepts:
        posts = top_posts_for_concept(c['id'], limit=3)
        items.append({
            'id': c['id'],
            'name': c['name'],
            'description': c.get('description') or '',
            'count': c.get('post_count') or 0,
            'recent_count': c.get('recent_post_count') or 0,
            'last_post_date': c.get('last_post_date') or '',
            'top_posts': [{
                'id': p['id'],
                'date': p.get('date') or '',
                'author': p.get('author') or '',
                'url': p.get('url') or '',
                'summary': (p.get('summary') or '')[:160],
            } for p in posts],
        })
    return {
        'placeholder': False,
        'window_days': MORNING_RECURRING_WINDOW_DAYS,
        'items': items,
    }


# --- Data access ---

def load_posts(db_path: Path) -> list[dict]:
    """Load all posts from SQLite with topics, audiences, and perspectives joined.

    `priority` is the *effective* priority under the default `tool-eval` lens
    (perspective row wins, falls back to legacy `posts.priority`). A separate
    `perspectives` dict on each post carries `{lens: priority}` for every lens
    the post has rows under — the viewer's lens-switcher reads this.
    """
    # Pre-compute effective priorities under tool-eval in a single query
    # (avoids N+1 over all posts).
    try:
        try:
            from .perspectives import load_priorities_by_lens, DEFAULT_LENS
        except ImportError:
            import sys as _sys
            _sys.path.insert(0, str(Path(__file__).parent))
            from perspectives import load_priorities_by_lens, DEFAULT_LENS
        eff_priorities = load_priorities_by_lens(DEFAULT_LENS, db_path)
    except Exception:
        # Pre-migration-7 fallback — just use whatever posts.priority says.
        eff_priorities = {}

    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row

    # Pre-fetch all perspective rows so we can hand each post its full overlay.
    perspectives_by_post: dict[int, dict[str, str]] = {}
    try:
        for r in conn.execute(
            "SELECT post_id, lens, priority FROM post_perspectives WHERE priority IS NOT NULL"
        ):
            perspectives_by_post.setdefault(r['post_id'], {})[r['lens']] = r['priority']
    except sqlite3.OperationalError:
        # Table doesn't exist yet — pre-migration-7
        pass

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

        # Effective priority: tool-eval perspective wins, fall back to posts.priority.
        effective_priority = eff_priorities.get(post_id) or row['priority'] or 'near-term'

        # New enrichment columns; older DBs without these migrations applied
        # surface as None via dict.get, so callers degrade gracefully.
        row_dict = dict(row)
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
            'priority': effective_priority,
            'sourceType': row['source_type'] or 'tweet',
            'views': row['views'] or '',
            'notes': row['notes'] or '',
            'enriched': bool(row['enriched']),
            'image': row['image'] or '',
            'source': row['source'] or 'email',
            # Additive — present once migration 2 has run.
            'enrichment_status': row_dict.get('enrichment_status') or '',
            'enrichment_version': row_dict.get('enrichment_version') or 0,
            'enrichment_attempts': row_dict.get('enrichment_attempts') or 0,
            'enrichment_last_error': row_dict.get('enrichment_last_error') or '',
            # Layer 3 — per-lens priorities. Empty for pre-migration-7 DBs.
            'perspectives': perspectives_by_post.get(post_id, {}),
        })

    conn.close()
    return posts


# --- JSON generation ---

def _atomic_write(path: Path, content: str) -> None:
    """Write content to path via temp-file + rename for crash safety.

    A reader that opens `path` during the write either sees the old content
    or the new content — never a partial write. Important when the lock has
    been acquired but a crash mid-write could still leave outputs torn.
    """
    path = Path(path)
    # tempfile in the same directory so rename is atomic (same filesystem).
    fd, tmp = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w") as f:
            f.write(content)
        os.replace(tmp, path)
    except Exception:
        # Best-effort cleanup of the temp file if rename failed.
        try:
            Path(tmp).unlink()
        except FileNotFoundError:
            pass
        raise


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
        # Additive (post-migration 2) — only emit when meaningfully populated
        # so old consumers reading the JSON keep their expected shape.
        if p.get('enrichment_status'):
            entry['enrichment_status'] = p['enrichment_status']
        if p.get('enrichment_version'):
            entry['enrichment_version'] = p['enrichment_version']
        if p.get('enrichment_attempts'):
            entry['enrichment_attempts'] = p['enrichment_attempts']
        if p.get('enrichment_last_error'):
            entry['enrichment_last_error'] = p['enrichment_last_error']

        export.append(entry)

    _atomic_write(out_path, json.dumps(export, indent=2, ensure_ascii=False))

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
        # Compact JSON for perspectives — usually empty or 1-2 keys.
        perspectives_js = json.dumps(p.get('perspectives') or {})

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
            f"perspectives: {perspectives_js}, "
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


def _replace_js_const(html: str, marker_start: str, open_bracket: str, close_bracket: str,
                       new_body: str) -> str:
    """Replace a balanced JS literal (array `[]` or object `{}`) bound to a const.

    Scans from `marker_start` forward, finds the matching `close_bracket` by
    counting nested `open_bracket`/`close_bracket` pairs, and replaces the body
    between (and including) the outermost pair.
    """
    start_idx = html.index(marker_start)
    bracket_start = start_idx + len(marker_start) - 1  # position of opening bracket
    assert html[bracket_start] == open_bracket, \
        f"Expected '{open_bracket}' at marker boundary in {marker_start!r}"
    depth = 1
    pos = bracket_start + 1
    while depth > 0 and pos < len(html):
        c = html[pos]
        if c == open_bracket:
            depth += 1
        elif c == close_bracket:
            depth -= 1
        pos += 1
    # pos is now right after the closing bracket
    end_idx = pos
    replacement = marker_start + new_body + close_bracket
    return html[:start_idx] + replacement + html[end_idx:]


def generate_html(posts: list[dict], html_template_path: Path, out_path: Path,
                  morning_view: dict = None):
    """Regenerate the HTML by replacing the POSTS array and MORNING_VIEW object."""
    with open(html_template_path) as f:
        html = f.read()

    # Replace POSTS array.
    new_array = generate_posts_js_array(posts)
    html = _replace_js_const(html, 'const POSTS = [', '[', ']', f'\n{new_array}\n')

    # Replace MORNING_VIEW object if the template has it. Older templates that
    # predate the morning surface don't carry the marker — silently skip in
    # that case so the rebuild still works during the template migration.
    if morning_view is not None and 'const MORNING_VIEW = {' in html:
        morning_body = json.dumps(morning_view, indent=2, ensure_ascii=False)
        # Strip the outermost braces from json.dumps output to match how
        # _replace_js_const reassembles around them.
        inner = morning_body.strip()
        assert inner.startswith('{') and inner.endswith('}'), 'unexpected json shape'
        inner = inner[1:-1]
        html = _replace_js_const(html, 'const MORNING_VIEW = {', '{', '}', inner)

    _atomic_write(out_path, html)

    print(f"  HTML: {len(posts)} posts → {out_path.name}")


# --- Markdown generation ---

def truncate(s: str, max_len: int = 70) -> str:
    """Truncate a string with ellipsis."""
    if not s or len(s) <= max_len:
        return s
    return s[:max_len].rstrip() + '...'


def generate_markdown(posts: list[dict], out_path: Path, morning_view: dict = None):
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

    # Morning view (at the top, hard-capped — this is the "what should I read now" surface)
    if morning_view:
        lines.append('---')
        lines.append('## Morning view')
        lines.append('')
        lines.append(f"*Generated {morning_view.get('generated_at', '')}. Hard-capped surface — see CURATION_DESIGN.md.*")
        lines.append('')

        lines.append('### Read now')
        rn = morning_view.get('read_now') or []
        if not rn:
            lines.append('*Nothing fresh in the last week marked actionable.*')
        else:
            for p in rn:
                url_part = f'[{p["author"]}]({p["url"]})' if p.get('url') else (p.get('author') or '?')
                lines.append(f"- **{p.get('date')}** — {url_part} — *{p.get('reason','')}*  ")
                if p.get('summary'):
                    lines.append(f"  {p['summary']}")
        lines.append('')

        lines.append('### Recurring this week')
        rec = morning_view.get('recurring') or {}
        if rec.get('placeholder'):
            lines.append(f"*{rec.get('message','')}*")
        else:
            window = rec.get('window_days', '?')
            lines.append(f"*Concepts with new evidence in the last {window} days. "
                         f"Ranked by recent post count.*")
            lines.append('')
            for c in rec.get('items', []):
                recent_part = f"+{c.get('recent_count', 0)} this week" if c.get('recent_count') else ''
                lines.append(f"- **{c.get('name')}** "
                             f"({c.get('count', 0)} posts" +
                             (f", {recent_part}" if recent_part else '') + ")  ")
                if c.get('description'):
                    lines.append(f"  {c['description']}")
                for p in (c.get('top_posts') or [])[:2]:
                    url_part = f"[{p.get('author','?')}]({p['url']})" if p.get('url') else (p.get('author') or '?')
                    lines.append(f"    - {p.get('date','')} — {url_part}: "
                                 f"{(p.get('summary') or '')[:140]}{'…' if len(p.get('summary') or '') > 140 else ''}")
                lines.append('')
        lines.append('')

        lines.append('### Revisit from last month')
        rv = morning_view.get('revisit') or []
        if not rv:
            lines.append('*No stale actionable posts in the revisit window.*')
        else:
            for p in rv:
                url_part = f'[{p["author"]}]({p["url"]})' if p.get('url') else (p.get('author') or '?')
                lines.append(f"- **{p.get('date')}** — {url_part} — *{p.get('reason','')}*  ")
                if p.get('summary'):
                    lines.append(f"  {p['summary']}")
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

    _atomic_write(out_path, '\n'.join(lines))

    print(f"  Markdown: {total} posts → {out_path.name}")


# --- Main ---

def rebuild(db_path: Path = None, out_dir: Path = None, with_lock: bool = True):
    """Main rebuild function — can be called from other scripts.

    Acquires the shared writer lock by default so concurrent sync / catch-up /
    curate runs don't race on the generated artifacts. Callers already holding
    the lock for a batch can pass with_lock=False to skip the nested acquire.
    """
    db_path = db_path or DEFAULT_DB
    out_dir = out_dir or DEFAULT_OUT

    def _do_rebuild():
        print(f"Rebuilding from: {db_path}")
        print(f"Output dir: {out_dir}")

        posts = load_posts(db_path)
        print(f"Loaded {len(posts)} posts from SQLite")

        morning_view = compute_morning_view(posts)
        rn = len(morning_view.get('read_now') or [])
        rv = len(morning_view.get('revisit') or [])
        rec = morning_view.get('recurring') or {}
        rec_count = 0 if rec.get('placeholder') else len(rec.get('items') or [])
        rec_tag = '(placeholder)' if rec.get('placeholder') else f'{rec_count} concepts'
        print(f"Morning view: Read now {rn}, Recurring {rec_tag}, Revisit {rv}")

        generate_json(posts, out_dir / 'posts_final_v3.json')
        generate_html(posts, out_dir / 'ai_links_collection_v3.html',
                      out_dir / 'ai_links_collection_v3.html',
                      morning_view=morning_view)
        generate_markdown(posts, out_dir / 'ai_links_collection_v3.md',
                          morning_view=morning_view)

        print(f"\n✓ Rebuild complete ({len(posts)} posts)")
        return posts

    if with_lock:
        with writer_lock():
            return _do_rebuild()
    return _do_rebuild()


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Rebuild output artifacts from SQLite')
    parser.add_argument('--db', type=Path, default=DEFAULT_DB, help='Path to SQLite database')
    parser.add_argument('--out', type=Path, default=DEFAULT_OUT, help='Output directory')
    args = parser.parse_args()

    rebuild(args.db, args.out)


if __name__ == "__main__":
    main()
