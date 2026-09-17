"""Print the Collection Stats block for CLAUDE.md, straight from the DB.

CLAUDE.md's stats section drifts every time anyone trusts it blind -- it sat on
August 26 numbers for three weeks while the corpus grew by 54 posts. Rather than
hand-editing, run:

    python3 -m db.stats            # human-readable
    python3 -m db.stats --markdown # paste-ready bullets for CLAUDE.md

and paste the result over the block. The queries live here so they stay
consistent with how the docs claim to measure things -- in particular, concept
size is reported by **primary-home count**, never by evidence or total edges.
"""

from __future__ import annotations

import argparse
import sqlite3
import sys
from pathlib import Path

DB_PATH = Path(__file__).with_name("ai_links.db")


def collect(db_path: Path = DB_PATH) -> dict:
    con = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    q1 = lambda s: con.execute(s).fetchone()[0]

    d: dict = {}
    d["total"] = q1("SELECT COUNT(*) FROM posts")
    d["date_min"], d["date_max"] = con.execute(
        "SELECT MIN(date), MAX(date) FROM posts").fetchone()
    d["status"] = dict(con.execute(
        "SELECT enrichment_status, COUNT(*) FROM posts GROUP BY 1").fetchall())
    d["topics"] = con.execute(
        "SELECT topic, COUNT(*) c FROM post_topics GROUP BY 1 ORDER BY c DESC").fetchall()
    d["priority"] = dict(con.execute(
        "SELECT priority, COUNT(*) FROM posts GROUP BY 1").fetchall())
    d["audiences"] = dict(con.execute(
        "SELECT audience, COUNT(*) FROM post_audiences GROUP BY 1").fetchall())
    d["concepts"] = dict(con.execute(
        "SELECT status, COUNT(*) FROM concepts GROUP BY 1").fetchall())
    d["roles"] = dict(con.execute(
        "SELECT role, COUNT(*) FROM post_concepts GROUP BY 1").fetchall())
    d["primaries"] = q1("SELECT COUNT(*) FROM post_concepts WHERE is_primary=1")
    d["primary_concepts"] = q1(
        "SELECT COUNT(DISTINCT concept_id) FROM post_concepts WHERE is_primary=1")
    d["largest_homes"] = con.execute("""
        SELECT c.name, COUNT(*) n FROM post_concepts pc
        JOIN concepts c ON c.id = pc.concept_id
        WHERE pc.is_primary = 1 GROUP BY 1 ORDER BY n DESC LIMIT 3""").fetchall()
    d["pending_obs"] = q1(
        "SELECT COUNT(*) FROM concept_observations WHERE status='pending'")
    d["provenance"] = con.execute(
        "SELECT source, status, COUNT(*) FROM concept_observations GROUP BY 1,2").fetchall()
    d["recent_dismissals"] = con.execute("""
        SELECT substr(observed_at,1,10) d, COUNT(*) FROM concept_observations
        WHERE status='dismissed' GROUP BY d ORDER BY d DESC LIMIT 3""").fetchall()
    d["flags"] = q1("SELECT COUNT(*) FROM posts WHERE notes LIKE '%flag:%'")
    d["orphans"] = q1("""SELECT COUNT(*) FROM posts p WHERE p.enrichment_status != 'dead'
        AND NOT EXISTS(SELECT 1 FROM post_concepts pc
                       WHERE pc.post_id = p.id AND pc.role IN ('evidence','origin'))""")
    d["zero_edge"] = q1("""SELECT COUNT(*) FROM posts p WHERE p.enrichment_status != 'dead'
        AND NOT EXISTS(SELECT 1 FROM post_concepts pc WHERE pc.post_id = p.id)""")
    d["zero_home_concepts"] = q1("""SELECT COUNT(*) FROM concepts c WHERE c.status='active'
        AND NOT EXISTS(SELECT 1 FROM post_concepts pc
                       WHERE pc.concept_id = c.id AND pc.is_primary = 1)""")
    d["zero_edge_concepts"] = q1("""SELECT COUNT(*) FROM concepts c WHERE c.status='active'
        AND NOT EXISTS(SELECT 1 FROM post_concepts pc WHERE pc.concept_id = c.id)""")
    con.close()
    return d


def as_markdown(d: dict) -> str:
    st = d["status"]
    total_edges = sum(d["roles"].values())
    topics = ", ".join(f"{t} ({n})" for t, n in d["topics"])
    homes = ", ".join(f"*{n}* ({c})" for n, c in d["largest_homes"])
    prov = ", ".join(f"{s} {p}/{q}" for (s, q, p) in
                     [(s, st_, n) for s, st_, n in d["provenance"]][:0]) or None

    lines = [
        f"- **{d['total']} total posts** in SQLite (live count). "
        f"Date range: {d['date_min']} – {d['date_max']}.",
        f"- Enrichment status: **{st.get('ok', 0)} `ok`**, {st.get('dead', 0)} `dead`. "
        + ("**Zero `partial` / `failed` / `unattempted` / `legacy-ok`.**"
           if not any(st.get(k) for k in ('partial', 'failed', 'unattempted', 'legacy-ok'))
           else "Queue NOT empty: "
                + ", ".join(f"{k} {st[k]}" for k in
                            ('partial', 'failed', 'unattempted', 'legacy-ok') if st.get(k))),
        f"- Top topics: {topics}.",
        "- Priority breakdown: " + ", ".join(
            f"{k} ({v})" for k, v in sorted(d["priority"].items(), key=lambda x: -x[1])) + ".",
        "- Audiences: " + ", ".join(
            f"{k} ({v})" for k, v in sorted(d["audiences"].items(), key=lambda x: -x[1])) + ".",
        f"- Concept graph: **{d['concepts'].get('active', 0)} active + "
        f"{d['concepts'].get('provisional', 0)} provisional** "
        f"({d['concepts'].get('archived', 0)} archived, "
        f"{d['concepts'].get('merged-into', 0)} merged-into). "
        f"{total_edges:,} edges — " + " + ".join(
            f"{v:,} `{k}`" for k, v in sorted(d["roles"].items(), key=lambda x: -x[1]))
        + f". **{d['primaries']} primary homes across {d['primary_concepts']} concepts**, "
          f"{d['pending_obs']} pending observations. Largest homes: {homes}.",
        f"- Orphans (no canonical home): **{d['orphans']} live posts**, of which "
        f"{d['zero_edge']} have no edge at all.",
        f"- Zero-home active concepts: {d['zero_home_concepts']}; "
        f"zero-edge active concepts: {d['zero_edge_concepts']}.",
        f"- {d['flags']} posts carry a subject `flag:` in `notes`.",
    ]
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--markdown", action="store_true",
                    help="emit paste-ready CLAUDE.md bullets")
    ap.add_argument("--db", default=str(DB_PATH))
    args = ap.parse_args(argv)

    d = collect(Path(args.db))
    if args.markdown:
        print(as_markdown(d))
        return 0

    print(f"posts            : {d['total']}  ({d['date_min']} .. {d['date_max']})")
    print(f"status           : {d['status']}")
    print(f"concepts         : {d['concepts']}")
    print(f"edges by role    : {d['roles']}")
    print(f"primary homes    : {d['primaries']} across {d['primary_concepts']} concepts")
    print(f"largest homes    : {d['largest_homes']}")
    print(f"pending obs      : {d['pending_obs']}")
    print(f"orphans          : {d['orphans']} (no edge at all: {d['zero_edge']})")
    print(f"zero-home concepts: {d['zero_home_concepts']}  zero-edge: {d['zero_edge_concepts']}")
    print(f"subject flags    : {d['flags']}")
    print(f"recent dismissals: {d['recent_dismissals']}  "
          "(expect nothing after 2026-08-26 — automation must not discard)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
