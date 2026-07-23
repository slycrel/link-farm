#!/usr/bin/env python3
"""
Concept-graph layer for the ai-links collection.

This module implements Layer 2 of CURATION_DESIGN.md:

    * Concept lifecycle helpers — create / merge / archive / rename.
    * Observation lifecycle — record / promote / dismiss / supersede.
    * Mechanical discovery passes — shared external URLs, shared mentions.
      These are SQL-only, deterministic, run continuously. Semantic and
      latent passes come later (steps 6 and 9 in the design doc).
    * Query helpers for the viewer / morning surface.
    * CLI entry points for one-off curation ("promote N", "merge A into B",
      "list active concepts", etc.) while the full chat-mediated curate.py
      skill is still being built.

The candidate/canonical split is the structural decision the doc commits to:
discovery passes write to `concept_observations` (immutable history with full
provenance); curation writes to `post_concepts` (one row per (post, concept)
reflecting the human's truth). Never bypass that — even hand-curated concepts
should write an observation row and a post_concepts row together via
`record_observation` + `promote_observation`, so the provenance trail stays
honest.

CLI:
    python3 -m db.concepts list                  # active concepts + post counts
    python3 -m db.concepts pending [CONCEPT_ID]  # pending observations
    python3 -m db.concepts promote OBS_ID        # promote an observation
    python3 -m db.concepts dismiss OBS_ID        # dismiss an observation
    python3 -m db.concepts merge SRC_ID DST_ID   # merge one concept into another
    python3 -m db.concepts discover              # run mechanical discovery passes
    python3 -m db.concepts stats                 # corpus-level concept stats
"""

import sqlite3
import argparse
import datetime
import math
import re
from pathlib import Path
from contextlib import contextmanager
from typing import Optional, Iterable, Sequence
from collections import defaultdict, Counter
from urllib.parse import urlparse

try:
    from .lock import writer_lock
except ImportError:
    import sys
    sys.path.insert(0, str(Path(__file__).parent))
    from lock import writer_lock

SCRIPT_DIR = Path(__file__).parent
DEFAULT_DB = SCRIPT_DIR / "ai_links.db"

# Status enums
CONCEPT_ACTIVE = "active"
CONCEPT_ARCHIVED = "archived"
CONCEPT_MERGED = "merged-into"

CONCEPT_SOURCE_DISCOVERED = "discovered"
CONCEPT_SOURCE_CURATED = "curated"
CONCEPT_SOURCE_MERGED = "merged"

OBS_PENDING = "pending"
OBS_PROMOTED = "promoted"
OBS_DISMISSED = "dismissed"
OBS_SUPERSEDED = "superseded"

ROLE_EVIDENCE = "evidence"
ROLE_COUNTER = "counter-example"
ROLE_TANGENTIAL = "tangential"
ROLE_ORIGIN = "origin"

SOURCE_MECHANICAL = "mechanical"
SOURCE_SEMANTIC = "semantic"
SOURCE_LATENT = "latent"

SCORE_MECHANICAL = "mechanical-overlap"
SCORE_SEMANTIC = "cosine-similarity"
SCORE_LATENT = "llm-self-report"


# ---- Connection helper -------------------------------------------------

@contextmanager
def _connect(db_path: Path = DEFAULT_DB):
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys=ON")
    try:
        yield conn
    finally:
        conn.close()


@contextmanager
def _maybe_lock(with_lock: bool):
    if with_lock:
        with writer_lock():
            yield
    else:
        yield


def _now() -> str:
    return datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")


# ---- Concept lifecycle ------------------------------------------------

def create_concept(name: str, description: str = "",
                   source: str = CONCEPT_SOURCE_CURATED,
                   db_path: Path = DEFAULT_DB,
                   with_lock: bool = True) -> int:
    """Create a new concept. Returns the new concept id."""
    with _maybe_lock(with_lock), _connect(db_path) as conn:
        cur = conn.execute("""
            INSERT INTO concepts (name, description, source, status, created_at, updated_at)
            VALUES (?, ?, ?, 'active', ?, ?)
        """, (name, description, source, _now(), _now()))
        conn.commit()
        return cur.lastrowid


def rename_concept(concept_id: int, new_name: str,
                   description: Optional[str] = None,
                   db_path: Path = DEFAULT_DB, with_lock: bool = True) -> None:
    with _maybe_lock(with_lock), _connect(db_path) as conn:
        if description is None:
            conn.execute("UPDATE concepts SET name=?, updated_at=? WHERE id=?",
                         (new_name, _now(), concept_id))
        else:
            conn.execute("UPDATE concepts SET name=?, description=?, updated_at=? WHERE id=?",
                         (new_name, description, _now(), concept_id))
        conn.commit()


def archive_concept(concept_id: int, db_path: Path = DEFAULT_DB,
                    with_lock: bool = True) -> None:
    """Mark a concept archived. Posts attached to it remain attached; it
    just stops surfacing in active-concept views."""
    with _maybe_lock(with_lock), _connect(db_path) as conn:
        conn.execute("UPDATE concepts SET status=?, updated_at=? WHERE id=?",
                     (CONCEPT_ARCHIVED, _now(), concept_id))
        conn.commit()


def merge_concepts(source_id: int, dest_id: int,
                   db_path: Path = DEFAULT_DB, with_lock: bool = True) -> dict:
    """Merge `source_id` into `dest_id`. Flatten-on-merge in one transaction.

    Per design (CURATION_DESIGN.md Layer 2): reject cycles before write, then
    rewrite all post_concepts and concept_observations rows from source to
    dest, mark source as 'merged-into' with merged_into=dest_id. No recursive
    CTE at read time.

    Returns counts of what was moved.
    """
    if source_id == dest_id:
        raise ValueError("Cannot merge a concept into itself")

    with _maybe_lock(with_lock), _connect(db_path) as conn:
        # Cycle rejection — if dest has previously been merged into source
        # (directly or transitively), the merge would create a cycle.
        cycle_check = conn.execute("""
            WITH RECURSIVE chain(id) AS (
                SELECT merged_into FROM concepts WHERE id = ?
                UNION
                SELECT c.merged_into FROM concepts c JOIN chain ON c.id = chain.id
                WHERE c.merged_into IS NOT NULL
            )
            SELECT 1 FROM chain WHERE id = ?
        """, (dest_id, source_id)).fetchone()
        if cycle_check:
            raise ValueError(f"Refusing to merge: cycle detected ({source_id} ↔ {dest_id})")

        if not conn.execute("SELECT 1 FROM concepts WHERE id=? AND status='active'",
                            (dest_id,)).fetchone():
            raise ValueError(f"Destination concept {dest_id} doesn't exist or isn't active")

        conn.execute("BEGIN")
        try:
            obs_moved = conn.execute(
                "UPDATE concept_observations SET concept_id=? WHERE concept_id=?",
                (dest_id, source_id),
            ).rowcount

            # post_concepts has PK (post_id, concept_id) so a naive UPDATE could
            # violate uniqueness. INSERT OR IGNORE the source rows into dest first,
            # then delete source rows.
            conn.execute("""
                INSERT OR IGNORE INTO post_concepts
                    (post_id, concept_id, role, promoted_from_observation_id, notes, promoted_at)
                SELECT post_id, ?, role, promoted_from_observation_id, notes, promoted_at
                  FROM post_concepts WHERE concept_id = ?
            """, (dest_id, source_id))
            edges_moved = conn.execute(
                "DELETE FROM post_concepts WHERE concept_id=?", (source_id,)
            ).rowcount

            conn.execute("""
                UPDATE concepts
                   SET status=?, merged_into=?, updated_at=?
                 WHERE id=?
            """, (CONCEPT_MERGED, dest_id, _now(), source_id))

            conn.execute("UPDATE concepts SET updated_at=? WHERE id=?", (_now(), dest_id))
            conn.commit()
            return {"observations_moved": obs_moved, "canonical_edges_moved": edges_moved}
        except Exception:
            conn.rollback()
            raise


# ---- Observation lifecycle ---------------------------------------------

def record_observation(post_id: int, concept_id: int, *,
                       source: str,
                       score_kind: str,
                       raw_score: float = 1.0,
                       role_suggestion: str = ROLE_EVIDENCE,
                       discovery_run_id: Optional[int] = None,
                       discovery_persona: Optional[str] = None,
                       discovery_model: Optional[str] = None,
                       notes: Optional[str] = None,
                       status: str = OBS_PENDING,
                       db_path: Path = DEFAULT_DB,
                       with_lock: bool = True) -> Optional[int]:
    """Record a discovery event. Returns the new observation id, or None
    if a `pending`/`promoted` observation already exists for this exact
    (post, concept, source, persona, model) — we don't regenerate dupes.
    Dismissed prior observations for the pair also block — that's the
    suppression semantic for the dismissal record (see design doc).
    """
    with _maybe_lock(with_lock), _connect(db_path) as conn:
        # Dedup against existing non-superseded observations for the same
        # discovery shape. The PK is auto-id so we check by content.
        existing = conn.execute("""
            SELECT id, status FROM concept_observations
             WHERE post_id=? AND concept_id=?
               AND source=?
               AND COALESCE(discovery_persona,'')=COALESCE(?, '')
               AND COALESCE(discovery_model,'')=COALESCE(?, '')
               AND status IN ('pending', 'promoted', 'dismissed')
        """, (post_id, concept_id, source, discovery_persona, discovery_model)).fetchone()
        if existing:
            return None

        cur = conn.execute("""
            INSERT INTO concept_observations (
                post_id, concept_id, role_suggestion, raw_score, score_kind,
                source, discovery_run_id, discovery_persona, discovery_model,
                status, observed_at, notes
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (post_id, concept_id, role_suggestion, raw_score, score_kind,
              source, discovery_run_id, discovery_persona, discovery_model,
              status, _now(), notes))
        conn.commit()
        return cur.lastrowid


def promote_observation(observation_id: int, *,
                         role: Optional[str] = None,
                         notes: Optional[str] = None,
                         db_path: Path = DEFAULT_DB,
                         with_lock: bool = True) -> None:
    """Promote a pending observation to a canonical post_concepts edge.

    Sets observation status to 'promoted' and inserts (or no-ops) the
    canonical row. If a canonical edge for (post, concept) already exists,
    leaves it in place — first promotion wins. Use `rename_concept` or
    direct UPDATE to change role on the canonical edge.
    """
    with _maybe_lock(with_lock), _connect(db_path) as conn:
        obs = conn.execute(
            "SELECT * FROM concept_observations WHERE id = ?", (observation_id,)
        ).fetchone()
        if not obs:
            raise ValueError(f"observation {observation_id} not found")

        chosen_role = role or obs["role_suggestion"] or ROLE_EVIDENCE
        conn.execute("BEGIN")
        try:
            conn.execute("""
                INSERT OR IGNORE INTO post_concepts
                    (post_id, concept_id, role, promoted_from_observation_id, notes, promoted_at)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (obs["post_id"], obs["concept_id"], chosen_role, observation_id,
                  notes, _now()))
            conn.execute(
                "UPDATE concept_observations SET status=? WHERE id=?",
                (OBS_PROMOTED, observation_id),
            )
            conn.execute(
                "UPDATE concepts SET updated_at=? WHERE id=?",
                (_now(), obs["concept_id"]),
            )
            conn.commit()
        except Exception:
            conn.rollback()
            raise


def dismiss_observation(observation_id: int, *,
                         notes: Optional[str] = None,
                         db_path: Path = DEFAULT_DB,
                         with_lock: bool = True) -> None:
    """Mark an observation dismissed. Future discovery passes skip it
    (dedup in record_observation checks against dismissed too)."""
    with _maybe_lock(with_lock), _connect(db_path) as conn:
        if notes is None:
            conn.execute("UPDATE concept_observations SET status=? WHERE id=?",
                         (OBS_DISMISSED, observation_id))
        else:
            conn.execute("UPDATE concept_observations SET status=?, notes=? WHERE id=?",
                         (OBS_DISMISSED, notes, observation_id))
        conn.commit()


# ---- Auto-curation -----------------------------------------------------

# Confidence floor for auto-filing a semantic observation as a SECONDARY tag.
# Cosine at/above this against a conceptual concept's centroid is trusted
# enough to attach without human review; below it is dismissed as noise.
#
# 2026-07-22: lowered 0.83 → 0.82 and repurposed as the secondary auto-file
# floor. This is safe now that (a) primary is derived separately by
# assign_primaries — auto-filed edges are always secondary, never a home — and
# (b) split-review measures primary count, so denser secondary tagging can't
# retrigger the split churn. 0.82 is the corpus's observed true-positive floor:
# the design notes on SEMANTIC_CENTROID_THRESHOLD record genuine matches as low
# as 0.821, and warn 0.83 silently drops them. Auto-filing at 0.82 keeps the
# curate queue empty of routine semantic matches — the human queue is now for
# structural decisions (merges, naming, per-person groupings), not "is this
# post also about X."
AUTO_PROMOTE_MIN_COSINE = 0.82


def _is_conceptual_name(name: Optional[str]) -> bool:
    """Heuristic: is this a *conceptual* concept (a theme/idea) rather than a
    per-person or raw-mechanical grouping?

    Jeremy's stated preference is to curate conceptual categories and leave
    per-person ones un-grown (kept, but not actively maintained). So:
      - "mention:@handle" and "url:https://…" mechanical concepts → not conceptual
      - names carrying a "(@handle)" person tag → not conceptual
      - everything else → conceptual
    """
    if not name:
        return False
    if name.startswith("mention:") or name.startswith("url:"):
        return False
    if re.search(r"\(@\w+\)", name):
        return False
    return True


def auto_curate(*, db_path: Path = DEFAULT_DB, with_lock: bool = True,
                min_cosine: float = AUTO_PROMOTE_MIN_COSINE,
                progress: bool = False) -> dict:
    """Unattended triage of pending observations, safe to run every sync.

    Rules (post-2026-07-22: semantic matches are fully automated — with primary
    derived separately and split-review measuring primaries, a semantic edge is
    only ever a low-stakes *secondary* tag, so there's no reason to park it for
    a human):
      - AUTO-FILE (promote as secondary): semantic observations at/above
        `min_cosine` on an active *conceptual* concept.
      - DISMISS: semantic observations *below* `min_cosine` on a conceptual
        concept (the recall band — too weak to tag without review, and we no
        longer review them); raw mechanical `mention:` / `url:` groupings; and
        per-person / non-conceptual observations whose post is already attached
        to some conceptual concept (lossless de-duplication).
      - LEAVE PENDING: only genuine structural decisions — e.g. a per-person /
        mechanical grouping whose post is *not* yet covered conceptually. These
        are the things the human curate queue should actually contain.

    Returns per-run counts. Idempotent: a second run finds nothing to do.
    """
    result = {"promoted": 0, "dismissed": 0, "dismissed_lowscore": 0, "left_pending": 0}

    with _connect(db_path) as conn:
        pend = conn.execute("""
            SELECT o.id, o.source, o.raw_score, o.post_id, o.concept_id,
                   c.name AS cname, c.status AS cstatus
              FROM concept_observations o
              JOIN concepts c ON c.id = o.concept_id
             WHERE o.status = 'pending'
        """).fetchall()
        # Posts already attached to at least one conceptual concept.
        conceptual_ids = {
            r["id"] for r in conn.execute(
                "SELECT id, name FROM concepts").fetchall()
            if _is_conceptual_name(r["name"])
        }
        covered_posts = set()
        if conceptual_ids:
            qmarks = ",".join("?" * len(conceptual_ids))
            covered_posts = {
                r["post_id"] for r in conn.execute(
                    f"SELECT DISTINCT post_id FROM post_concepts "
                    f"WHERE concept_id IN ({qmarks})", tuple(conceptual_ids)
                ).fetchall()
            }

    promote_ids, dismiss_ids, dismiss_lowscore_ids = [], [], []
    for o in pend:
        conceptual = _is_conceptual_name(o["cname"])
        active = o["cstatus"] == CONCEPT_ACTIVE
        score = o["raw_score"] or 0.0
        if o["source"] == "semantic" and active and conceptual and score >= min_cosine:
            promote_ids.append(o["id"])
        elif o["source"] == "semantic" and conceptual and score < min_cosine:
            # Recall band below the auto-file floor — too weak to tag, and we
            # no longer review it by hand. Dismiss so it can't accumulate.
            dismiss_lowscore_ids.append(o["id"])
        elif o["source"] == "mechanical" and (
                o["cname"].startswith("mention:") or o["cname"].startswith("url:")):
            dismiss_ids.append(o["id"])
        elif not conceptual and o["post_id"] in covered_posts:
            dismiss_ids.append(o["id"])
        else:
            result["left_pending"] += 1

    def _apply():
        for oid in promote_ids:
            promote_observation(oid, db_path=db_path, with_lock=False)
            result["promoted"] += 1
        for oid in dismiss_ids:
            dismiss_observation(
                oid, notes="auto-curate: conceptual-preference triage",
                db_path=db_path, with_lock=False)
            result["dismissed"] += 1
        for oid in dismiss_lowscore_ids:
            dismiss_observation(
                oid, notes=f"auto-curate: below secondary-tag floor ({min_cosine})",
                db_path=db_path, with_lock=False)
            result["dismissed_lowscore"] += 1

    if with_lock:
        with writer_lock(timeout=120):
            _apply()
    else:
        _apply()

    if progress:
        print(f"[auto-curate] promoted {result['promoted']} (secondary), "
              f"dismissed {result['dismissed']} + {result['dismissed_lowscore']} low-score, "
              f"left {result['left_pending']} pending")
    return result


# ---- Primary/secondary assignment --------------------------------------

# Manual pins: a post_concepts row whose notes contain this marker is a
# human-locked primary — assign_primaries() will not recompute that post.
PRIMARY_PIN_MARKER = "[primary-pin]"


def assign_primaries(*, db_path: Path = DEFAULT_DB, with_lock: bool = True,
                     respect_pins: bool = True, progress: bool = False) -> dict:
    """Designate exactly one PRIMARY concept per concept-tagged post.

    The primary/secondary axis (migration 8): multi-label overlap is kept —
    a post can carry many concept edges — but exactly one edge is its primary
    *home*. Primary edges partition the tagged corpus (one home per post);
    everything else is a secondary tag that preserves cross-cutting discovery.

    Primary = the post's best-fitting concept, by cosine of the post's
    embedding against each candidate concept's *leave-one-out* centroid (the
    post is excluded from its own concept's centroid so small concepts don't
    trivially win by self-similarity). Deterministic fallbacks:
      - single-edge post            → that edge is primary.
      - no embedding / no centroid  → keep current primary if any, else the
                                       lowest concept_id (stable).
      - manual pin (respect_pins)   → left untouched.

    Idempotent: primary is derived, so re-running reproduces the same state
    (modulo pins and centroid drift). Returns per-run counts.
    """
    result = {"tagged_posts": 0, "single_edge": 0, "scored": 0,
              "pinned_skipped": 0, "fallback": 0, "changed": 0}

    # Lazy import — keep concepts.py usable without numpy/fastembed installed.
    try:
        import numpy as np
        try:
            from .embeddings import _blob_to_vector, DEFAULT_MODEL
        except ImportError:
            from embeddings import _blob_to_vector, DEFAULT_MODEL
    except Exception as e:
        result["error"] = f"embeddings unavailable: {e}"
        if progress:
            print(f"[assign-primaries] skipped — {result['error']}")
        return result

    def _apply():
        with _connect(db_path) as conn:
            model = DEFAULT_MODEL
            # All edges on active concepts, with vectors where available.
            rows = conn.execute("""
                SELECT pc.post_id, pc.concept_id, pc.is_primary, pc.notes,
                       pe.vector
                  FROM post_concepts pc
                  JOIN concepts c ON c.id = pc.concept_id AND c.status = ?
                  LEFT JOIN post_embeddings pe
                         ON pe.post_id = pc.post_id AND pe.model = ?
            """, (CONCEPT_ACTIVE, model)).fetchall()

            # Group edges by post; collect per-concept vector sums for LOO.
            by_post: dict[int, list[dict]] = defaultdict(list)
            csum: dict[int, np.ndarray] = {}
            ccount: dict[int, int] = defaultdict(int)
            vecs: dict[tuple, "np.ndarray"] = {}
            for r in rows:
                by_post[r["post_id"]].append(dict(r))
                if r["vector"] is not None:
                    v = _blob_to_vector(r["vector"])
                    v = v / (np.linalg.norm(v) or 1.0)
                    vecs[(r["post_id"], r["concept_id"])] = v
                    csum[r["concept_id"]] = csum.get(r["concept_id"], 0) + v
                    ccount[r["concept_id"]] += 1

            chosen: dict[int, int] = {}   # post_id -> concept_id
            for pid, edges in by_post.items():
                result["tagged_posts"] += 1
                pinned = [e for e in edges
                          if respect_pins and (e["notes"] or "").find(PRIMARY_PIN_MARKER) >= 0]
                if pinned:
                    result["pinned_skipped"] += 1
                    continue
                if len(edges) == 1:
                    chosen[pid] = edges[0]["concept_id"]
                    result["single_edge"] += 1
                    continue
                # Score each candidate by leave-one-out centroid cosine.
                best_cid, best_score = None, -2.0
                for e in edges:
                    cid = e["concept_id"]
                    v = vecs.get((pid, cid))
                    if v is None or ccount.get(cid, 0) < 2:
                        continue  # can't score this candidate reliably
                    loo = (csum[cid] - v) / (ccount[cid] - 1)
                    loo = loo / (np.linalg.norm(loo) or 1.0)
                    score = float(np.dot(v, loo))
                    if score > best_score:
                        best_score, best_cid = score, cid
                if best_cid is not None:
                    chosen[pid] = best_cid
                    result["scored"] += 1
                else:
                    # Fallback: keep existing primary, else lowest concept_id.
                    cur = next((e["concept_id"] for e in edges if e["is_primary"]), None)
                    chosen[pid] = cur if cur is not None else min(e["concept_id"] for e in edges)
                    result["fallback"] += 1

            # Write: clear all, then set the chosen edge per post. Clearing
            # first keeps the one-primary-per-post partial unique index happy.
            conn.execute("BEGIN")
            try:
                # Count how many will actually change (for reporting).
                for pid, cid in chosen.items():
                    was = next((e["is_primary"] for e in by_post[pid]
                                if e["concept_id"] == cid), 0)
                    if not was:
                        result["changed"] += 1
                conn.execute("UPDATE post_concepts SET is_primary = 0 WHERE is_primary = 1")
                conn.executemany(
                    "UPDATE post_concepts SET is_primary = 1 WHERE post_id = ? AND concept_id = ?",
                    [(pid, cid) for pid, cid in chosen.items()],
                )
                conn.commit()
            except Exception:
                conn.rollback()
                raise

    if with_lock:
        with writer_lock(timeout=120):
            _apply()
    else:
        _apply()

    if progress:
        print(f"[assign-primaries] {result['tagged_posts']} tagged posts "
              f"({result['single_edge']} single, {result['scored']} scored, "
              f"{result['fallback']} fallback, {result['pinned_skipped']} pinned) "
              f"→ {result['changed']} primaries changed")
    return result


# ---- Split-candidate trigger -------------------------------------------

# The split trigger fires on a *proportional* threshold, not a flat count.
# A concept is worth a human glance when its PRIMARY-home count runs well
# above the typical home size for the current corpus — i.e. it's
# disproportionately large, whatever the corpus size — so the bar auto-scales
# as the collection grows instead of needing a magic number re-tuned by hand.
# (This replaced the old flat SPLIT_CANDIDATE_MIN_POSTS=40, which had started
# cutting through the natural head of the distribution once primary/secondary
# auto-promotion made a big primary home a sign of legitimate size rather than
# of conflated threads — Jeremy, July 2026.)
#
# Threshold = SPLIT_CANDIDATE_MEAN_MULTIPLE × (mean primary-home size across
# concepts that are a primary home for ≥1 post), floored at
# SPLIT_CANDIDATE_FLOOR so a tiny corpus doesn't flag 3-post homes. Measured on
# primaries (a partition), never total edges — a concept can carry many
# secondary tags without being an oversized *home*. Only a *flag*, never an
# auto-split.
SPLIT_CANDIDATE_MEAN_MULTIPLE = 2.0
SPLIT_CANDIDATE_FLOOR = 20  # never flag a home smaller than this, whatever the mean

# Back-compat alias: some callers/tests referenced the old flat constant. Kept
# so `min_posts=SPLIT_CANDIDATE_MIN_POSTS` still forces the pre-July behaviour.
SPLIT_CANDIDATE_MIN_POSTS = 40


def split_candidates(db_path: Path = DEFAULT_DB,
                     mean_multiple: float = SPLIT_CANDIDATE_MEAN_MULTIPLE,
                     min_posts: Optional[int] = None) -> list[dict]:
    """Active concepts whose PRIMARY-post count is disproportionately large for
    the current corpus — worth vetting for sub-categorization.

    The threshold scales with the corpus: it's `mean_multiple` times the mean
    primary-home size across active concepts that home ≥1 post, floored at
    SPLIT_CANDIDATE_FLOOR. Pass an explicit `min_posts` to override with a flat
    threshold instead (e.g. the legacy SPLIT_CANDIDATE_MIN_POSTS).

    Returns [{id, name, post_count}] where `post_count` is the number of posts
    for which this concept is the *primary* home (is_primary=1) — a partition,
    not a sum of overlapping tags. A concept can accrue many secondary tags
    without being an oversized home, so measuring primaries stops the trigger
    from firing on merely-popular concepts. Purely advisory — surfaced in the
    pipeline report; splitting stays a human decision.
    """
    with _connect(db_path) as conn:
        rows = conn.execute("""
            SELECT c.id, c.name, COUNT(pc.post_id) AS post_count
              FROM concepts c
              JOIN post_concepts pc ON pc.concept_id = c.id AND pc.is_primary = 1
             WHERE c.status = ?
             GROUP BY c.id
             ORDER BY post_count DESC
        """, (CONCEPT_ACTIVE,)).fetchall()
    counts = [r["post_count"] for r in rows]
    if not counts:
        return []
    if min_posts is not None:
        threshold = min_posts
    else:
        mean = sum(counts) / len(counts)
        threshold = max(SPLIT_CANDIDATE_FLOOR, math.ceil(mean_multiple * mean))
    return [dict(r) for r in rows if r["post_count"] >= threshold]


# ---- Query helpers -----------------------------------------------------

def list_active_concepts(db_path: Path = DEFAULT_DB) -> list[dict]:
    """List active concepts with promoted-evidence counts."""
    with _connect(db_path) as conn:
        rows = conn.execute("""
            SELECT
                c.id, c.name, c.description, c.source, c.created_at, c.updated_at,
                (SELECT COUNT(*) FROM post_concepts pc WHERE pc.concept_id = c.id) AS post_count,
                (SELECT COUNT(*) FROM concept_observations o
                  WHERE o.concept_id = c.id AND o.status = 'pending') AS pending_count
              FROM concepts c
             WHERE c.status = 'active'
             ORDER BY post_count DESC, c.updated_at DESC
        """).fetchall()
    return [dict(r) for r in rows]


def pending_observations(concept_id: Optional[int] = None,
                          db_path: Path = DEFAULT_DB, limit: int = 50) -> list[dict]:
    """Pending observations, optionally filtered to one concept.
    Joins post + concept so the curator sees what they're deciding on."""
    where = "o.status = 'pending'"
    params: list = []
    if concept_id is not None:
        where += " AND o.concept_id = ?"
        params.append(concept_id)
    sql = f"""
        SELECT
            o.id              AS observation_id,
            o.post_id, o.concept_id, o.source, o.score_kind, o.raw_score,
            o.discovery_persona, o.discovery_model, o.notes,
            c.name            AS concept_name,
            p.author          AS post_author,
            p.date            AS post_date,
            p.url             AS post_url,
            SUBSTR(COALESCE(p.summary,''), 1, 200) AS post_summary
          FROM concept_observations o
          JOIN concepts c ON c.id = o.concept_id
          JOIN posts    p ON p.id = o.post_id
         WHERE {where}
         ORDER BY o.observed_at DESC
         LIMIT ?
    """
    params.append(limit)
    with _connect(db_path) as conn:
        rows = conn.execute(sql, params).fetchall()
    return [dict(r) for r in rows]


def concept_post_ids(concept_id: int, db_path: Path = DEFAULT_DB) -> list[int]:
    """Canonical posts attached to a concept (promoted only)."""
    with _connect(db_path) as conn:
        rows = conn.execute(
            "SELECT post_id FROM post_concepts WHERE concept_id=? ORDER BY promoted_at",
            (concept_id,),
        ).fetchall()
    return [r[0] for r in rows]


def recent_active_concepts(days: int = 7, db_path: Path = DEFAULT_DB,
                            limit: int = 5) -> list[dict]:
    """Concepts that recently gained evidence — for the morning view's
    "Recurring this week" section.

    Ranks by **post-date recency**, not observation-date. The observation
    timestamp is when the system noticed the connection; the post date is
    when the idea actually appeared in Jeremy's feed. The morning view
    cares about the latter.

    Concepts with no recent evidence at all are excluded. Concepts that
    only have older evidence (long-term threads that aren't moving) won't
    surface here — they're still browseable via the concepts list.
    """
    with _connect(db_path) as conn:
        rows = conn.execute(f"""
            SELECT
                c.id, c.name, c.description,
                (SELECT COUNT(*) FROM post_concepts pc WHERE pc.concept_id = c.id) AS post_count,
                (SELECT COUNT(DISTINCT pc.post_id)
                   FROM post_concepts pc
                   JOIN posts p ON p.id = pc.post_id
                  WHERE pc.concept_id = c.id
                    AND p.date >= date('now', ?)
                ) AS recent_post_count,
                (SELECT MAX(p.date)
                   FROM post_concepts pc
                   JOIN posts p ON p.id = pc.post_id
                  WHERE pc.concept_id = c.id) AS last_post_date
              FROM concepts c
             WHERE c.status = 'active'
               AND EXISTS (
                   SELECT 1 FROM post_concepts pc
                     JOIN posts p ON p.id = pc.post_id
                    WHERE pc.concept_id = c.id
                      AND p.date >= date('now', ?)
               )
             ORDER BY recent_post_count DESC, post_count DESC, last_post_date DESC
             LIMIT ?
        """, (f'-{days} days', f'-{days} days', limit)).fetchall()
    return [dict(r) for r in rows]


def top_posts_for_concept(concept_id: int, limit: int = 3,
                           db_path: Path = DEFAULT_DB) -> list[dict]:
    """Top promoted posts attached to a concept, newest first."""
    with _connect(db_path) as conn:
        rows = conn.execute("""
            SELECT p.id, p.date, p.author, p.handle, p.url,
                   SUBSTR(COALESCE(p.summary,''), 1, 200) AS summary
              FROM post_concepts pc
              JOIN posts p ON p.id = pc.post_id
             WHERE pc.concept_id = ?
             ORDER BY p.date DESC
             LIMIT ?
        """, (concept_id, limit)).fetchall()
    return [dict(r) for r in rows]


def get_concept(concept_id: int, db_path: Path = DEFAULT_DB) -> Optional[dict]:
    """Fetch a concept by id, or None if not found."""
    with _connect(db_path) as conn:
        row = conn.execute(
            "SELECT * FROM concepts WHERE id = ?", (concept_id,)
        ).fetchone()
    return dict(row) if row else None


def find_concept_by_name(name: str, db_path: Path = DEFAULT_DB) -> Optional[dict]:
    """Find an active concept by exact name match (case-insensitive)."""
    with _connect(db_path) as conn:
        row = conn.execute(
            "SELECT * FROM concepts WHERE LOWER(name) = LOWER(?) AND status='active'",
            (name,),
        ).fetchone()
    return dict(row) if row else None


def list_discovery_runs(limit: int = 20, db_path: Path = DEFAULT_DB) -> list[dict]:
    """Recent discovery runs with summary counts."""
    with _connect(db_path) as conn:
        rows = conn.execute("""
            SELECT id, started_at, finished_at, source, persona, model,
                   sampling_strategy, posts_examined, observations_created, notes
              FROM discovery_runs
             ORDER BY id DESC LIMIT ?
        """, (limit,)).fetchall()
    return [dict(r) for r in rows]


def filter_observations(*,
                         status: Optional[str] = None,
                         source: Optional[str] = None,
                         discovery_run_id: Optional[int] = None,
                         concept_id: Optional[int] = None,
                         min_raw_score: Optional[float] = None,
                         min_corroboration: Optional[int] = None,
                         limit: int = 200,
                         db_path: Path = DEFAULT_DB) -> list[dict]:
    """Flexible observation filter for bulk-curation commands.

    `min_corroboration` counts non-superseded observations for the
    (post_id, concept_id) pair across ALL sources — useful for "promote
    everything that 3+ independent passes have surfaced."

    Returns enriched rows (joined with post + concept) for display.
    """
    clauses = []
    params: list = []
    if status is not None:
        clauses.append("o.status = ?")
        params.append(status)
    if source is not None:
        clauses.append("o.source = ?")
        params.append(source)
    if discovery_run_id is not None:
        clauses.append("o.discovery_run_id = ?")
        params.append(discovery_run_id)
    if concept_id is not None:
        clauses.append("o.concept_id = ?")
        params.append(concept_id)
    if min_raw_score is not None:
        clauses.append("o.raw_score >= ?")
        params.append(min_raw_score)
    if min_corroboration is not None:
        # Count concurrent non-superseded observations for the same pair.
        clauses.append("""(
            SELECT COUNT(*) FROM concept_observations o2
             WHERE o2.post_id = o.post_id
               AND o2.concept_id = o.concept_id
               AND o2.status != 'superseded'
        ) >= ?""")
        params.append(min_corroboration)

    where = (" WHERE " + " AND ".join(clauses)) if clauses else ""
    sql = f"""
        SELECT
            o.id AS observation_id,
            o.post_id, o.concept_id,
            o.source, o.score_kind, o.raw_score,
            o.discovery_persona, o.discovery_model, o.discovery_run_id,
            o.status, o.notes,
            c.name            AS concept_name,
            p.author          AS post_author,
            p.date            AS post_date,
            p.url             AS post_url,
            SUBSTR(COALESCE(p.summary,''), 1, 160) AS post_summary
          FROM concept_observations o
          JOIN concepts c ON c.id = o.concept_id
          JOIN posts    p ON p.id = o.post_id
          {where}
         ORDER BY o.id ASC
         LIMIT ?
    """
    params.append(limit)
    with _connect(db_path) as conn:
        rows = conn.execute(sql, params).fetchall()
    return [dict(r) for r in rows]


def bulk_promote(observation_ids: Sequence[int],
                  role: Optional[str] = None,
                  db_path: Path = DEFAULT_DB,
                  with_lock: bool = True) -> dict:
    """Promote multiple observations under a single lock acquisition.
    Returns counts: {promoted, skipped, not_found}."""
    counts = {"promoted": 0, "skipped": 0, "not_found": 0}
    with _maybe_lock(with_lock):
        for oid in observation_ids:
            try:
                obs = None
                with _connect(db_path) as conn:
                    obs = conn.execute(
                        "SELECT status FROM concept_observations WHERE id = ?", (oid,)
                    ).fetchone()
                if not obs:
                    counts["not_found"] += 1
                    continue
                if obs[0] == OBS_PROMOTED:
                    counts["skipped"] += 1
                    continue
                promote_observation(oid, role=role, db_path=db_path, with_lock=False)
                counts["promoted"] += 1
            except Exception:
                # Skip on per-row failure; bulk operations don't abort whole batch
                counts["skipped"] += 1
    return counts


def bulk_dismiss(observation_ids: Sequence[int],
                  notes: Optional[str] = None,
                  db_path: Path = DEFAULT_DB,
                  with_lock: bool = True) -> dict:
    """Dismiss multiple observations under a single lock acquisition."""
    counts = {"dismissed": 0, "skipped": 0, "not_found": 0}
    with _maybe_lock(with_lock):
        for oid in observation_ids:
            try:
                with _connect(db_path) as conn:
                    obs = conn.execute(
                        "SELECT status FROM concept_observations WHERE id = ?", (oid,)
                    ).fetchone()
                if not obs:
                    counts["not_found"] += 1
                    continue
                if obs[0] == OBS_DISMISSED:
                    counts["skipped"] += 1
                    continue
                dismiss_observation(oid, notes=notes, db_path=db_path, with_lock=False)
                counts["dismissed"] += 1
            except Exception:
                counts["skipped"] += 1
    return counts


# ---- Mechanical discovery ---------------------------------------------

def _start_run(conn, source: str, sampling_strategy: str,
               persona: Optional[str] = None,
               model: Optional[str] = None) -> int:
    cur = conn.execute("""
        INSERT INTO discovery_runs
            (started_at, source, persona, model, sampling_strategy)
        VALUES (?, ?, ?, ?, ?)
    """, (_now(), source, persona, model, sampling_strategy))
    return cur.lastrowid


def _finish_run(conn, run_id: int, posts_examined: int, observations_created: int,
                 notes: Optional[str] = None) -> None:
    conn.execute("""
        UPDATE discovery_runs
           SET finished_at = ?, posts_examined = ?, observations_created = ?, notes = ?
         WHERE id = ?
    """, (_now(), posts_examined, observations_created, notes, run_id))


# URLs we ignore as "evidence" for a concept — too generic to mean anything.
_GENERIC_DOMAINS = {
    "x.com", "twitter.com", "t.co", "fxtwitter.com", "vxtwitter.com",
    "youtube.com", "youtu.be",
    "google.com", "google.co", "google.de", "google.fr",
}


def _interesting_external_urls(post: dict, conn) -> set[str]:
    """Extract external URLs that are concept-worthy.

    Looks at:
      - thread segments of type 'external_link'
      - URLs found in summary/content text via regex
    Filters out the post's own URL and generic hosts.
    """
    found: set[str] = set()

    # Segments
    seg_rows = conn.execute(
        "SELECT url FROM post_thread_segments WHERE post_id=? AND url IS NOT NULL AND url != ''",
        (post["id"],),
    ).fetchall()
    for r in seg_rows:
        url = (r[0] or "").strip()
        if url:
            found.add(url)

    # Regex over summary + content
    text_blob = (post.get("summary") or "") + " " + (post.get("content") or "")
    for m in re.finditer(r'https?://[^\s\)\]\}>"]+', text_blob):
        found.add(m.group(0).rstrip('.,;:'))
    # Also match bare host/path mentions like "github.com/user/repo" (no scheme)
    for m in re.finditer(r'\b(?:github\.com|arxiv\.org|huggingface\.co)/[A-Za-z0-9_./-]+', text_blob):
        found.add("https://" + m.group(0).rstrip('.,;:'))

    # Normalize + filter
    out: set[str] = set()
    own_url = (post.get("url") or "").strip()
    for url in found:
        url = url.rstrip('/')
        if not url or url == own_url:
            continue
        try:
            host = urlparse(url).netloc.lower()
        except Exception:
            continue
        host = host.lstrip("www.")
        if host in _GENERIC_DOMAINS or not host:
            continue
        # Strip tracking params crudely
        url = re.sub(r'\?(s|t|utm_[A-Za-z_]+)=[^&]*(&|$)', '?', url)
        url = url.rstrip('?&')
        out.add(url)
    return out


def _mentioned_handles(post: dict) -> set[str]:
    """@handle mentions in the post body, lowercased. Excludes the post's own handle."""
    text_blob = (post.get("summary") or "") + " " + (post.get("content") or "")
    own = (post.get("handle") or "").lower().lstrip("@")
    out: set[str] = set()
    for m in re.finditer(r'@([A-Za-z0-9_]{2,30})', text_blob):
        h = m.group(1).lower()
        if h != own and h not in {"every"}:  # exclude common stopwords
            out.add(h)
    return out


def discover_shared_external_urls(db_path: Path = DEFAULT_DB,
                                   min_evidence: int = 2,
                                   with_lock: bool = True) -> dict:
    """Mechanical pass: find external URLs that appear across multiple posts.

    For each unique URL referenced by `min_evidence` or more posts, create a
    discovered concept (named after the URL) and observation rows linking
    those posts to it. If a discovered concept with the same name already
    exists, attach new observations to it.

    Returns stats: {urls_seen, urls_promoted, concepts_created, observations_created}.
    """
    stats = {"urls_seen": 0, "urls_promoted": 0,
             "concepts_created": 0, "observations_created": 0}

    with _maybe_lock(with_lock), _connect(db_path) as conn:
        run_id = _start_run(conn, SOURCE_MECHANICAL, "shared-external-url")

        # Pull enriched-enough posts only (skip empty / dead so we don't
        # build concepts on noise).
        posts = conn.execute("""
            SELECT id, url, handle, summary, content
              FROM posts
             WHERE enrichment_status IN ('ok', 'legacy-ok')
        """).fetchall()

        url_to_posts: dict[str, list[int]] = defaultdict(list)
        posts_examined = 0
        for row in posts:
            posts_examined += 1
            urls = _interesting_external_urls(dict(row), conn)
            for u in urls:
                url_to_posts[u].append(row["id"])

        stats["urls_seen"] = len(url_to_posts)

        # For each URL with enough evidence, create or find a concept.
        for url, post_ids in url_to_posts.items():
            unique_posts = list(set(post_ids))
            if len(unique_posts) < min_evidence:
                continue
            stats["urls_promoted"] += 1

            concept_name = f"url:{url}"
            existing = conn.execute(
                "SELECT id FROM concepts WHERE name = ? AND status = 'active'",
                (concept_name,),
            ).fetchone()
            if existing:
                concept_id = existing[0]
            else:
                cur = conn.execute("""
                    INSERT INTO concepts (name, description, source, status, created_at, updated_at)
                    VALUES (?, ?, ?, 'active', ?, ?)
                """, (concept_name, f"Posts referencing {url}",
                      CONCEPT_SOURCE_DISCOVERED, _now(), _now()))
                concept_id = cur.lastrowid
                stats["concepts_created"] += 1

            # Strength = number of co-citing posts (cap at 5).
            strength = min(len(unique_posts) / 5.0, 1.0)
            for post_id in unique_posts:
                obs_id = _record_obs_in_txn(
                    conn,
                    post_id=post_id, concept_id=concept_id,
                    source=SOURCE_MECHANICAL,
                    score_kind=SCORE_MECHANICAL,
                    raw_score=strength,
                    discovery_run_id=run_id,
                    notes=f"co-cites {url}",
                )
                if obs_id is not None:
                    stats["observations_created"] += 1

        _finish_run(conn, run_id, posts_examined, stats["observations_created"],
                    notes=f"min_evidence={min_evidence}")
        conn.commit()

    return stats


def discover_shared_mentions(db_path: Path = DEFAULT_DB,
                              min_evidence: int = 3,
                              with_lock: bool = True) -> dict:
    """Mechanical pass: find @handles mentioned across multiple posts.

    Threshold default is 3 (vs 2 for URLs) because mentions are noisier —
    a person can be cited in passing.
    """
    stats = {"handles_seen": 0, "handles_promoted": 0,
             "concepts_created": 0, "observations_created": 0}

    with _maybe_lock(with_lock), _connect(db_path) as conn:
        run_id = _start_run(conn, SOURCE_MECHANICAL, "shared-mention")

        posts = conn.execute("""
            SELECT id, handle, summary, content
              FROM posts
             WHERE enrichment_status IN ('ok', 'legacy-ok')
        """).fetchall()

        handle_to_posts: dict[str, list[int]] = defaultdict(list)
        posts_examined = 0
        for row in posts:
            posts_examined += 1
            for h in _mentioned_handles(dict(row)):
                handle_to_posts[h].append(row["id"])

        stats["handles_seen"] = len(handle_to_posts)

        for handle, post_ids in handle_to_posts.items():
            unique_posts = list(set(post_ids))
            if len(unique_posts) < min_evidence:
                continue
            stats["handles_promoted"] += 1

            concept_name = f"mention:@{handle}"
            existing = conn.execute(
                "SELECT id FROM concepts WHERE name = ? AND status = 'active'",
                (concept_name,),
            ).fetchone()
            if existing:
                concept_id = existing[0]
            else:
                cur = conn.execute("""
                    INSERT INTO concepts (name, description, source, status, created_at, updated_at)
                    VALUES (?, ?, ?, 'active', ?, ?)
                """, (concept_name,
                      f"Posts mentioning @{handle} as a recurring reference point",
                      CONCEPT_SOURCE_DISCOVERED, _now(), _now()))
                concept_id = cur.lastrowid
                stats["concepts_created"] += 1

            strength = min(len(unique_posts) / 8.0, 1.0)
            for post_id in unique_posts:
                obs_id = _record_obs_in_txn(
                    conn,
                    post_id=post_id, concept_id=concept_id,
                    source=SOURCE_MECHANICAL,
                    score_kind=SCORE_MECHANICAL,
                    raw_score=strength,
                    discovery_run_id=run_id,
                    notes=f"mentions @{handle}",
                )
                if obs_id is not None:
                    stats["observations_created"] += 1

        _finish_run(conn, run_id, posts_examined, stats["observations_created"],
                    notes=f"min_evidence={min_evidence}")
        conn.commit()

    return stats


def _record_obs_in_txn(conn, *, post_id: int, concept_id: int, source: str,
                        score_kind: str, raw_score: float = 1.0,
                        discovery_run_id: Optional[int] = None,
                        discovery_persona: Optional[str] = None,
                        discovery_model: Optional[str] = None,
                        notes: Optional[str] = None,
                        role_suggestion: str = ROLE_EVIDENCE) -> Optional[int]:
    """Like record_observation, but uses the open connection (no nested
    lock / connect). Used inside discovery passes that already hold both."""
    existing = conn.execute("""
        SELECT id FROM concept_observations
         WHERE post_id=? AND concept_id=?
           AND source=?
           AND COALESCE(discovery_persona,'')=COALESCE(?, '')
           AND COALESCE(discovery_model,'')=COALESCE(?, '')
           AND status IN ('pending', 'promoted', 'dismissed')
    """, (post_id, concept_id, source, discovery_persona, discovery_model)).fetchone()
    if existing:
        return None
    cur = conn.execute("""
        INSERT INTO concept_observations (
            post_id, concept_id, role_suggestion, raw_score, score_kind,
            source, discovery_run_id, discovery_persona, discovery_model,
            status, observed_at, notes
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'pending', ?, ?)
    """, (post_id, concept_id, role_suggestion, raw_score, score_kind,
          source, discovery_run_id, discovery_persona, discovery_model,
          _now(), notes))
    return cur.lastrowid


def run_all_mechanical_passes(db_path: Path = DEFAULT_DB,
                               with_lock: bool = True) -> dict:
    """Run every mechanical-discovery flavor under a single lock acquisition."""
    out = {}
    with _maybe_lock(with_lock):
        out["shared_external_urls"] = discover_shared_external_urls(
            db_path=db_path, with_lock=False,
        )
        out["shared_mentions"] = discover_shared_mentions(
            db_path=db_path, with_lock=False,
        )
    return out


# ---- Semantic discovery (step 6) -------------------------------------

# Concept-centroid match threshold. Cosine similarity >= this counts as
# "close enough to the concept's average meaning to suggest as evidence."
# bge-small-en-v1.5's score distribution on this corpus (mostly AI/agents
# content) clusters tightly — pairs of unrelated AI posts often score 0.65-
# 0.75 because the topic vocabulary overlaps. 0.78 is a measured threshold:
# at 0.80 we get ~150 candidates across active concepts, at 0.65 we get
# ~1500 (mostly noise). 0.78 sits at the elbow of the score distribution.
# Tune by use — the latent gate paragraph applies here too.
#
# 2026-07-17: settled on 0.80 after a curate pass. Once the latent gate
# opened, 0.78 produced ~15:1 noise (592 semantic candidates, only ~34 worth
# reviewing). Briefly tried 0.83, but that was too aggressive: genuine
# matches promoted that day ran as low as 0.821 (e.g. a "Loop Engineering"
# post, a CLAUDE.md-as-control-layer post), so 0.83 would have silently
# dropped real evidence.
#
# 2026-07-22: raised 0.80 → 0.82 to match the auto-file floor
# (AUTO_PROMOTE_MIN_COSINE). The old 0.80 was deliberately recall-biased on
# the assumption a human would review the 0.80–0.82 band in curation. That
# review never happened at scale (the band just accumulated as hundreds of
# stale pending rows), and semantic triage is now fully automated: matches
# ≥0.82 auto-file as secondary, below that we don't tag. Generating sub-0.82
# candidates only to auto-dismiss them is wasted churn, so we stop generating
# them. 0.82 is the observed true-positive floor (matches as low as 0.821),
# so recall loss is minimal. auto_curate still defensively dismisses anything
# below the floor that pre-dates this change.
SEMANTIC_CENTROID_THRESHOLD = 0.82

# Don't centroid-match concepts with too few canonical edges — a single-post
# concept's centroid is just that post's embedding, which collapses to a
# raw nearest-neighbor query and loses the "what does this concept mean
# across multiple examples" signal.
SEMANTIC_MIN_CONCEPT_EDGES = 2


def discover_semantic_neighbors(db_path: Path = DEFAULT_DB,
                                 model: Optional[str] = None,
                                 threshold: float = SEMANTIC_CENTROID_THRESHOLD,
                                 min_concept_edges: int = SEMANTIC_MIN_CONCEPT_EDGES,
                                 with_lock: bool = True) -> dict:
    """Mechanical semantic pass: match embedded posts against existing
    active concepts' centroids; propose new observations for posts that
    cluster close to a concept but aren't yet attached.

    This is the cleanest semantic signal for the current data scale —
    concept-relative matching rather than blind clustering. Embedding-based
    clustering (HDBSCAN, etc.) to discover *new* concepts comes later as
    the corpus grows.

    Returns stats: {concepts_considered, posts_considered, observations_created}.
    """
    # Lazy-import so a missing embeddings module / dep doesn't break the
    # rest of db.concepts.
    try:
        try:
            from .embeddings import (
                concept_centroids, _connect as _emb_connect,
                _blob_to_vector, DEFAULT_MODEL,
            )
        except ImportError:
            import sys as _sys
            _sys.path.insert(0, str(Path(__file__).parent))
            from embeddings import (
                concept_centroids, _blob_to_vector, DEFAULT_MODEL,
            )
        import numpy as np
    except ImportError as e:
        return {"error": f"semantic discovery requires fastembed + numpy: {e}",
                "concepts_considered": 0, "posts_considered": 0,
                "observations_created": 0}

    if model is None:
        model = DEFAULT_MODEL

    stats = {"concepts_considered": 0, "posts_considered": 0,
             "observations_created": 0}

    with _maybe_lock(with_lock), _connect(db_path) as conn:
        run_id = _start_run(conn, SOURCE_SEMANTIC,
                             "concept-centroid",
                             model=model)

        # Concepts with enough canonical edges to have a meaningful centroid.
        active_with_enough = conn.execute(f"""
            SELECT c.id, c.name, COUNT(pc.post_id) AS n
              FROM concepts c
              JOIN post_concepts pc ON pc.concept_id = c.id
             WHERE c.status = 'active'
             GROUP BY c.id
            HAVING n >= ?
        """, (min_concept_edges,)).fetchall()
        eligible_concept_ids = {r["id"] for r in active_with_enough}
        if not eligible_concept_ids:
            _finish_run(conn, run_id, 0, 0,
                        notes=f"no concepts with >= {min_concept_edges} edges")
            conn.commit()
            return stats

        # Compute centroids using the open connection's data — call into
        # embeddings.concept_centroids, then filter to eligible_concept_ids.
        all_centroids = concept_centroids(model=model, db_path=db_path)
        centroids = {cid: vec for cid, vec in all_centroids.items()
                     if cid in eligible_concept_ids}
        stats["concepts_considered"] = len(centroids)

        # Load all post embeddings.
        emb_rows = conn.execute(
            "SELECT post_id, vector FROM post_embeddings WHERE model = ?",
            (model,),
        ).fetchall()
        if not emb_rows:
            _finish_run(conn, run_id, 0, 0, notes="no embeddings")
            conn.commit()
            return stats

        post_ids = [r["post_id"] for r in emb_rows]
        post_matrix = np.stack(
            [_blob_to_vector(r["vector"]) for r in emb_rows], axis=0,
        )
        # Normalize for cosine.
        norms = np.linalg.norm(post_matrix, axis=1, keepdims=True)
        norms = np.where(norms == 0, 1.0, norms)
        post_matrix_normed = post_matrix / norms
        stats["posts_considered"] = len(post_ids)

        # For each concept, score all posts; propose for those that exceed
        # threshold AND aren't already canonically attached.
        already_attached = defaultdict(set)
        for r in conn.execute(
            "SELECT concept_id, post_id FROM post_concepts"
        ):
            already_attached[r["concept_id"]].add(r["post_id"])

        for cid, centroid in centroids.items():
            sims = post_matrix_normed @ centroid  # already normalized
            for pid, sim in zip(post_ids, sims.tolist()):
                if sim < threshold:
                    continue
                if pid in already_attached.get(cid, set()):
                    continue
                obs_id = _record_obs_in_txn(
                    conn,
                    post_id=pid, concept_id=cid,
                    source=SOURCE_SEMANTIC,
                    score_kind=SCORE_SEMANTIC,
                    raw_score=float(sim),
                    discovery_run_id=run_id,
                    discovery_model=model,
                    notes=f"cosine={sim:.3f} vs centroid",
                )
                if obs_id is not None:
                    stats["observations_created"] += 1

        _finish_run(conn, run_id, stats["posts_considered"],
                    stats["observations_created"],
                    notes=f"threshold={threshold} min_concept_edges={min_concept_edges}")
        conn.commit()

    return stats


# ---- CLI --------------------------------------------------------------

def _cmd_list(args):
    rows = list_active_concepts(args.db)
    if not rows:
        print("No active concepts.")
        return
    print(f"{'id':>5}  {'name':40s}  {'posts':>6}  {'pending':>8}  source")
    print("-" * 80)
    for r in rows:
        name = (r["name"] or "")[:40]
        print(f"{r['id']:>5}  {name:40s}  {r['post_count']:>6}  {r['pending_count']:>8}  {r['source']}")


def _cmd_pending(args):
    rows = pending_observations(args.concept_id, args.db, args.limit)
    if not rows:
        print("No pending observations.")
        return
    for r in rows:
        print(f"#{r['observation_id']}  concept={r['concept_id']} ({r['concept_name']})  "
              f"post={r['post_id']} ({r['post_author']} {r['post_date']})  "
              f"src={r['source']}  notes={r['notes'] or ''}")
        if r.get("post_summary"):
            print(f"      {r['post_summary']}")


def _cmd_promote(args):
    promote_observation(args.observation_id)
    print(f"Promoted observation #{args.observation_id}")


def _cmd_dismiss(args):
    dismiss_observation(args.observation_id, notes=args.notes)
    print(f"Dismissed observation #{args.observation_id}")


def _cmd_merge(args):
    out = merge_concepts(args.source_id, args.dest_id)
    print(f"Merged {args.source_id} → {args.dest_id}: {out}")


def _cmd_discover(args):
    stats = run_all_mechanical_passes(args.db)
    for pass_name, s in stats.items():
        print(f"{pass_name}:")
        for k, v in s.items():
            print(f"    {k:25s} {v}")


def _cmd_semantic(args):
    stats = discover_semantic_neighbors(
        db_path=args.db, threshold=args.threshold,
        min_concept_edges=args.min_concept_edges,
    )
    print("semantic concept-centroid pass:")
    for k, v in stats.items():
        print(f"    {k:25s} {v}")


def _cmd_stats(args):
    with _connect(args.db) as conn:
        for name in ("concepts", "concept_observations", "post_concepts", "discovery_runs"):
            n = conn.execute(f"SELECT COUNT(*) FROM {name}").fetchone()[0]
            print(f"  {name:25s} {n}")
        print()
        print("Observations by status:")
        for r in conn.execute(
            "SELECT status, COUNT(*) FROM concept_observations GROUP BY status"
        ):
            print(f"  {r[0]:15s} {r[1]}")
        print()
        print("Top concepts by promoted edges:")
        for r in conn.execute("""
            SELECT c.id, c.name, COUNT(pc.post_id) AS n
              FROM concepts c
              LEFT JOIN post_concepts pc ON pc.concept_id = c.id
             WHERE c.status='active'
             GROUP BY c.id ORDER BY n DESC LIMIT 10
        """):
            print(f"  #{r[0]:<5} {r[1][:50]:50s}  {r[2]:>4} promoted")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", type=Path, default=DEFAULT_DB)
    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("list").set_defaults(func=_cmd_list)

    p = sub.add_parser("pending")
    p.add_argument("concept_id", type=int, nargs="?", default=None)
    p.add_argument("--limit", type=int, default=50)
    p.set_defaults(func=_cmd_pending)

    p = sub.add_parser("promote")
    p.add_argument("observation_id", type=int)
    p.set_defaults(func=_cmd_promote)

    p = sub.add_parser("dismiss")
    p.add_argument("observation_id", type=int)
    p.add_argument("--notes", type=str, default=None)
    p.set_defaults(func=_cmd_dismiss)

    p = sub.add_parser("merge")
    p.add_argument("source_id", type=int)
    p.add_argument("dest_id", type=int)
    p.set_defaults(func=_cmd_merge)

    sub.add_parser("discover").set_defaults(func=_cmd_discover)

    p = sub.add_parser("semantic")
    p.add_argument("--threshold", type=float, default=SEMANTIC_CENTROID_THRESHOLD)
    p.add_argument("--min-concept-edges", type=int, default=SEMANTIC_MIN_CONCEPT_EDGES)
    p.set_defaults(func=_cmd_semantic)

    sub.add_parser("stats").set_defaults(func=_cmd_stats)

    args = parser.parse_args()
    if not getattr(args, "func", None):
        parser.print_help()
        return
    args.func(args)


if __name__ == "__main__":
    main()
