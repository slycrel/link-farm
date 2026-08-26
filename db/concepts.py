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
ROLE_WEAK = "weak"

# Roles that count as *load-bearing* membership. Only these feed concept
# centroids, qualify a concept for semantic scoring, and are eligible to become
# a post's primary home. Everything else (weak / counter-example / tangential)
# is a recorded association that a reader can act on but that must not vote on
# what a concept *means* — otherwise recall improvements silently degrade the
# precision of every downstream pass.
#
# Rationale (Jeremy, Aug 2026): "low signal" was doing too much work as a
# reason to discard. A sub-threshold match is usually a real association that
# the 0.82 floor can't confirm, not noise — and this corpus is a personal
# research library where the cost of losing a thread is higher than the cost
# of carrying a weak one. So the recall band is now *attached and labelled*
# rather than dismissed, and the role vocabulary is what keeps that honest.
CANONICAL_ROLES = (ROLE_EVIDENCE, ROLE_ORIGIN)

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

    **Attach-and-label, never discard (Jeremy, Aug 2026).** This pass used to
    dismiss two large buckets: the sub-threshold semantic "recall band", and raw
    mechanical `mention:` / `url:` groupings. That was wrong for this corpus.
    Every post here is something Jeremy deliberately sent himself, so a match
    the 0.82 floor can't *confirm* is usually a real association rather than
    noise — and dismissing it meant nothing downstream would ever reconsider
    it. Measured cost of the old policy: `adjacent`-tagged posts were ~1.6x
    more likely than the corpus baseline to end up with no concept edge at all,
    i.e. the triage was biased against exactly the tangential material the
    taxonomy was extended to capture.

    So automation no longer decides that something isn't worth thinking about.
    It records what it found and how much to trust it; `role` carries the
    caveat. Only a human calls `dismiss_observation()`, for genuine junk
    (scams, content-free engagement bait).

    Rules:
      - EVIDENCE (load-bearing; feeds centroids, can become a primary home):
        semantic observations at/above `min_cosine` on an active *conceptual*
        concept, plus mechanical shared-external-URL groupings — two posts
        citing the same repo or article are concretely about the same thing.
      - WEAK (recorded association; excluded from centroids, never primary):
        semantic observations *below* `min_cosine` on a conceptual concept (the
        recall band), mechanical `mention:` groupings (a shared @handle is a
        much looser signal than a shared URL, and per-person grouping is
        deprioritised by preference — but not deleted), and non-conceptual
        observations whose post is already conceptually covered.
      - LEAVE PENDING: genuine structural decisions — e.g. a mechanical
        grouping on an archived concept. The human queue should only ever
        contain things a human actually has to decide.

    Because weak edges can't move centroids or primaries, attaching them
    generously is safe: recall goes up, precision of every downstream pass is
    unchanged. Returns per-run counts. Idempotent: a second run finds nothing.
    """
    result = {"promoted": 0, "dismissed": 0, "dismissed_lowscore": 0,
              "left_pending": 0, "weak": 0, "evidence": 0}

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

    # (observation_id, role, note) — nothing is dismissed here by design.
    to_attach: list[tuple[int, str, str]] = []
    for o in pend:
        conceptual = _is_conceptual_name(o["cname"])
        active = o["cstatus"] == CONCEPT_ACTIVE
        score = o["raw_score"] or 0.0
        name = o["cname"]
        if o["source"] == "semantic" and active and conceptual and score >= min_cosine:
            to_attach.append((o["id"], ROLE_EVIDENCE,
                              f"auto-curate: cosine {score:.3f} >= floor {min_cosine}"))
        elif o["source"] == "semantic" and conceptual and score < min_cosine:
            # The recall band. Previously dismissed; now kept as a labelled
            # association so it stays findable and can be upgraded by hand.
            to_attach.append((o["id"], ROLE_WEAK,
                              f"auto-curate: recall band, cosine {score:.3f} "
                              f"< floor {min_cosine} — association recorded, "
                              f"not load-bearing"))
        elif o["source"] == "mechanical" and name.startswith("url:") and active:
            # Shared external URL: concrete co-citation, treat as real evidence.
            to_attach.append((o["id"], ROLE_EVIDENCE,
                              "auto-curate: shared external URL (co-citation)"))
        elif o["source"] == "mechanical" and name.startswith("mention:") and active:
            # Shared @handle: much looser, and per-person grouping is
            # deprioritised by preference — kept weak rather than dropped.
            to_attach.append((o["id"], ROLE_WEAK,
                              "auto-curate: shared @mention — loose signal, "
                              "per-person grouping deprioritised"))
        elif not conceptual and active:
            # Non-conceptual concept (url:/mention:/per-person). Weak either
            # way: if the post is already conceptually covered this is a
            # duplicate association, and if it isn't, a raw grouping still
            # isn't the thematic home it needs — orphan clustering and the
            # latent pass should stay free to find that. Previously the
            # not-yet-covered case fell through to `left_pending` and sat in
            # the human queue forever (91 such rows accumulated in one run).
            covered = o["post_id"] in covered_posts
            to_attach.append((o["id"], ROLE_WEAK,
                              "auto-curate: non-conceptual grouping, post "
                              + ("already conceptually covered"
                                 if covered else "not yet conceptually homed")))
        else:
            result["left_pending"] += 1

    def _apply():
        for oid, role, note in to_attach:
            promote_observation(oid, role=role, notes=note,
                                db_path=db_path, with_lock=False)
            result["promoted"] += 1
            result["evidence" if role == ROLE_EVIDENCE else "weak"] += 1

    if with_lock:
        with writer_lock(timeout=120):
            _apply()
    else:
        _apply()

    if progress:
        print(f"[auto-curate] attached {result['promoted']} "
              f"({result['evidence']} evidence, {result['weak']} weak), "
              f"dismissed {result['dismissed']}, "
              f"left {result['left_pending']} pending")
    return result


# ---- Primary/secondary assignment --------------------------------------

# A concept whose description carries this marker is excluded from semantic
# centroid scoring: it keeps its edges and shows up everywhere else, but no
# post is ever matched *into* it by cosine.
#
# Why this is needed. A concept assembled by hand from a lexically DIFFUSE
# cluster gets a centroid that sits near the corpus mean — its members share a
# purpose, not a vocabulary, so averaging them points at "general AI writing"
# rather than at the theme. Such a centroid then matches almost everything, and
# because matches at/above AUTO_PROMOTE_MIN_COSINE become *evidence*, the
# concept feeds on its own diffuseness and grows without bound.
#
# Observed 2026-08-26: #65 "thinking tools & problem-solving method" was
# hand-created with 7 carefully chosen members (raw cohesion 0.840) and within
# two pipeline runs had absorbed 26 unrelated evidence edges — Markov-chain
# trading lectures, "Chain of Thought is dead", a Google/Meta agent paper — and
# hijacked 18 posts' primary homes. Marking it fixed that while keeping the
# hand-curated membership intact.
#
# Rule of thumb: if a concept only exists because a *reader* could see it, it
# should carry this marker. Membership is then curated deliberately (by hand or
# by the latent pass), which is the honest way to maintain a category that
# embeddings cannot represent.
NO_CENTROID_SCORING_MARKER = "[no-centroid-scoring]"

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
            # Only load-bearing edges are eligible to be a post's home. A weak
            # or counter-example edge is a recorded association, not a claim
            # about where the post belongs — so a post whose *only* edges are
            # weak is intentionally left unhomed and stays visible to orphan
            # clustering, which can still invent a real concept for it.
            rows = conn.execute(f"""
                SELECT pc.post_id, pc.concept_id, pc.is_primary, pc.notes,
                       c.name AS cname, pe.vector
                  FROM post_concepts pc
                  JOIN concepts c ON c.id = pc.concept_id AND c.status = ?
                  LEFT JOIN post_embeddings pe
                         ON pe.post_id = pc.post_id AND pe.model = ?
                 WHERE pc.role IN ({','.join('?' * len(CANONICAL_ROLES))})
            """, (CONCEPT_ACTIVE, model, *CANONICAL_ROLES)).fetchall()

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
                # Conceptual-preference on the *home* axis. A raw `url:` /
                # `mention:` grouping or a per-person concept is a legitimate
                # association but a poor answer to "what is this post about",
                # so it only wins a home when nothing thematic is available.
                # (Without this, making shared-URL edges load-bearing quietly
                # promoted url: groupings into homes for a handful of posts.)
                conceptual_edges = [e for e in edges
                                    if _is_conceptual_name(e["cname"])]
                candidates = conceptual_edges or edges
                if len(candidates) == 1:
                    chosen[pid] = candidates[0]["concept_id"]
                    result["single_edge"] += 1
                    continue
                # Score each candidate by leave-one-out centroid cosine.
                best_cid, best_score = None, -2.0
                for e in candidates:
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
                    # Drawn from `candidates`, so the conceptual preference
                    # still holds when nothing could be scored.
                    cur = next((e["concept_id"] for e in candidates if e["is_primary"]), None)
                    chosen[pid] = cur if cur is not None else min(e["concept_id"] for e in candidates)
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

# A flat absolute tripwire: flag a concept only once its PRIMARY-home count runs
# clearly *above* anything we'd expect, as a cheap "did a pool suddenly balloon?"
# signal — not a routine nag on merely-large homes. Big primary homes are fine
# and expected now that primary/secondary auto-promotion routes overlap into
# *secondary* edges, so a large *primary* home means legitimate size, not
# conflated threads (Jeremy, July 2026: "we're ok with appropriate bigger pools
# and looking for spikes to indicate we're doing it wrong").
#
# Set with headroom over the current max (~50, loop engineering) so it flags
# nothing today and only trips on a genuine spike past 60. A data-driven
# mean-based version was tried and reverted — the distribution is bimodal (a few
# real 20-50 homes over a long tail of 2-4-post singletons), so the mean drifts
# with the tail and it flagged *more*, not fewer. True rate-of-change spike
# detection would need per-run history tracking; deliberately not built — the
# corpus grows a few posts/day and this tripwire gets ~all the value for one
# line. Measured on primaries (a partition), never total edges. Only a *flag*,
# never an auto-split.
SPLIT_CANDIDATE_MIN_POSTS = 60


def split_candidates(db_path: Path = DEFAULT_DB,
                     min_posts: int = SPLIT_CANDIDATE_MIN_POSTS) -> list[dict]:
    """Active concepts whose PRIMARY-post count is large enough to be worth
    vetting for sub-categorization.

    Returns [{id, name, post_count}] where `post_count` is the number of posts
    for which this concept is the *primary* home (is_primary=1) — a partition,
    not a sum of overlapping tags. A concept can accrue many secondary tags
    without being an oversized home, so measuring primaries stops the split
    trigger from firing on merely-popular concepts. Purely advisory — surfaced
    in the pipeline report; splitting stays a human decision.
    """
    with _connect(db_path) as conn:
        rows = conn.execute("""
            SELECT c.id, c.name, COUNT(pc.post_id) AS post_count
              FROM concepts c
              JOIN post_concepts pc ON pc.concept_id = c.id AND pc.is_primary = 1
             WHERE c.status = ?
             GROUP BY c.id
            HAVING post_count >= ?
             ORDER BY post_count DESC
        """, (CONCEPT_ACTIVE, min_posts)).fetchall()
    return [dict(r) for r in rows]


# ---- Query helpers -----------------------------------------------------

def list_active_concepts(db_path: Path = DEFAULT_DB) -> list[dict]:
    """List active concepts with promoted-evidence counts.

    `post_count` is total edges (what the concept touches); `evidence_count` is
    the load-bearing subset (what it actually rests on) and `weak_count` the
    recorded-but-unconfirmed remainder. Report `evidence_count` when describing
    how big a concept is — quoting the total overstates it, which is the same
    mistake the old "49 active concepts" figure made by counting empty shells.
    """
    with _connect(db_path) as conn:
        rows = conn.execute("""
            SELECT
                c.id, c.name, c.description, c.source, c.created_at, c.updated_at,
                (SELECT COUNT(*) FROM post_concepts pc WHERE pc.concept_id = c.id) AS post_count,
                (SELECT COUNT(*) FROM post_concepts pc WHERE pc.concept_id = c.id
                   AND pc.role IN ('evidence', 'origin')) AS evidence_count,
                (SELECT COUNT(*) FROM post_concepts pc WHERE pc.concept_id = c.id
                   AND pc.role NOT IN ('evidence', 'origin')) AS weak_count,
                (SELECT COUNT(*) FROM concept_observations o
                  WHERE o.concept_id = c.id AND o.status = 'pending') AS pending_count
              FROM concepts c
             WHERE c.status = 'active'
             ORDER BY evidence_count DESC, post_count DESC, c.updated_at DESC
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
        # "Gained new evidence" means exactly that — load-bearing edges only.
        # Weak edges are attached generously, so counting them here would make
        # every concept look freshly active and drown the morning view.
        rows = conn.execute(f"""
            SELECT
                c.id, c.name, c.description,
                (SELECT COUNT(*) FROM post_concepts pc
                  WHERE pc.concept_id = c.id
                    AND pc.role IN ('evidence', 'origin')) AS post_count,
                (SELECT COUNT(DISTINCT pc.post_id)
                   FROM post_concepts pc
                   JOIN posts p ON p.id = pc.post_id
                  WHERE pc.concept_id = c.id
                    AND pc.role IN ('evidence', 'origin')
                    AND p.date >= date('now', ?)
                ) AS recent_post_count,
                (SELECT MAX(p.date)
                   FROM post_concepts pc
                   JOIN posts p ON p.id = pc.post_id
                  WHERE pc.concept_id = c.id
                    AND pc.role IN ('evidence', 'origin')) AS last_post_date
              FROM concepts c
             WHERE c.status = 'active'
               AND EXISTS (
                   SELECT 1 FROM post_concepts pc
                     JOIN posts p ON p.id = pc.post_id
                    WHERE pc.concept_id = c.id
                      AND pc.role IN ('evidence', 'origin')
                      AND p.date >= date('now', ?)
               )
             ORDER BY recent_post_count DESC, post_count DESC, last_post_date DESC
             LIMIT ?
        """, (f'-{days} days', f'-{days} days', limit)).fetchall()
    return [dict(r) for r in rows]


def top_posts_for_concept(concept_id: int, limit: int = 3,
                           db_path: Path = DEFAULT_DB) -> list[dict]:
    """Top promoted posts attached to a concept, newest first.

    Load-bearing edges are surfaced ahead of weak ones so a concept's shortlist
    shows what it actually rests on; weak associations still appear once the
    evidence is exhausted, which is the point of keeping them.
    """
    with _connect(db_path) as conn:
        rows = conn.execute("""
            SELECT p.id, p.date, p.author, p.handle, p.url, pc.role,
                   SUBSTR(COALESCE(p.summary,''), 1, 200) AS summary
              FROM post_concepts pc
              JOIN posts p ON p.id = pc.post_id
             WHERE pc.concept_id = ?
             ORDER BY (pc.role IN ('evidence', 'origin')) DESC, p.date DESC
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
#
# 2026-08-26: lowered 0.82 → 0.75, reopening the recall band deliberately.
# The 2026-07-22 reasoning was locally sound but had a structural side effect:
# setting the *proposal* threshold equal to the *auto-file* floor made the band
# ZERO WIDTH, so nothing could ever land in it and no pass could surface an
# association it wasn't already confident about. Measured consequence:
# `adjacent`-tagged posts were ~1.6x more likely than the corpus baseline to
# carry no concept edge at all (52% vs 33%), and the 16 edge-less `adjacent`
# posts all scored 0.67–0.80 against their nearest conceptual centroid — real
# associations sitting just under a floor that had been closed to them.
# Munger's inversion method, Pólya's *How to Solve It*, first-principles
# thinking: material Jeremy deliberately sent himself, invisible to the graph.
#
# Why 0.75 specifically: this corpus's *pairwise* post-post cosine distribution
# has mean 0.61 and p99 0.73 (see the orphan-clustering note in CLAUDE.md), so
# 0.75 sits above the 99th percentile of ordinary similarity. A 0.75 hit on a
# concept centroid is therefore distinctive rather than generic "this is all AI
# content" overlap. Below ~0.73 that stops being true and the weak layer starts
# carrying noise instead of signal — 0.70 would attach 162 of 173 edge-less
# posts, which is close enough to "everything" that the label stops informing.
#
# This is only safe because the 0.75–0.82 band lands as `weak` edges, which are
# excluded from centroids, semantic eligibility and primary assignment (see
# CANONICAL_ROLES). Recall rises; nothing downstream is distorted. If you raise
# this back toward the floor, understand you are re-closing the band, not just
# tightening a knob.
SEMANTIC_CENTROID_THRESHOLD = 0.75

# Max sub-floor ("weak band") matches proposed per post, per run. The evidence
# band (>= AUTO_PROMOTE_MIN_COSINE) is uncapped; only the weak band is ranked
# and truncated. See the rationale in discover_semantic_neighbors(): an
# absolute threshold on raw cosines is far too permissive on this corpus —
# uncapped, 0.75 proposed 8,825 observations in one run (~26% of every possible
# post/concept pair). Capping makes a weak edge mean "one of this post's
# closest concepts" instead of "cleared a bar everything clears". 3 is enough
# to give an otherwise-homeless post a few real leads without carpet-bombing;
# raise it if weak edges start feeling too sparse to be useful.
SEMANTIC_MAX_WEAK_PER_POST = 3

# Don't centroid-match concepts with too few canonical edges — a single-post
# concept's centroid is just that post's embedding, which collapses to a
# raw nearest-neighbor query and loses the "what does this concept mean
# across multiple examples" signal.
SEMANTIC_MIN_CONCEPT_EDGES = 2


def discover_semantic_neighbors(db_path: Path = DEFAULT_DB,
                                 model: Optional[str] = None,
                                 threshold: float = SEMANTIC_CENTROID_THRESHOLD,
                                 min_concept_edges: int = SEMANTIC_MIN_CONCEPT_EDGES,
                                 max_weak_per_post: int = SEMANTIC_MAX_WEAK_PER_POST,
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
        # Counted on load-bearing roles only, to match concept_centroids():
        # a concept held up entirely by weak edges has no trustworthy centroid
        # and must not be scored against.
        active_with_enough = conn.execute(f"""
            SELECT c.id, c.name, COUNT(pc.post_id) AS n
              FROM concepts c
              JOIN post_concepts pc ON pc.concept_id = c.id
             WHERE c.status = 'active'
               AND pc.role IN ({','.join('?' * len(CANONICAL_ROLES))})
               AND COALESCE(c.description, '') NOT LIKE ?
             GROUP BY c.id
            HAVING n >= ?
        """, (*CANONICAL_ROLES, f'%{NO_CENTROID_SCORING_MARKER}%',
              min_concept_edges)).fetchall()
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

        # Weak edges a post ALREADY carries from a previous semantic run. The
        # cap has to be a per-post *total*, not per-run: `already_attached`
        # excludes existing edges, so a per-run cap just hands each post its
        # next-best 3 every time and converges on the same everything-attached
        # carpet, only slowly (observed: 2024 → 1910 → 1444 edges per run).
        weak_held = defaultdict(int)
        for r in conn.execute(f"""
            SELECT post_id, COUNT(*) AS n FROM post_concepts
             WHERE role = ? AND promoted_from_observation_id IN
                   (SELECT id FROM concept_observations WHERE source = ?)
             GROUP BY post_id
        """, (ROLE_WEAK, SOURCE_SEMANTIC)):
            weak_held[r["post_id"]] = r["n"]

        # Collect candidates first, then apply a PER-POST CAP to the sub-floor
        # band before writing anything.
        #
        # Why the cap exists: an absolute threshold is the wrong instrument for
        # the weak band. Raw bge cosines on this corpus are high and concept
        # centroids are denoised, so post-to-centroid similarity clears 0.75 for
        # a large fraction of ALL (post, concept) pairs — the first run at 0.75
        # proposed 8,825 observations, ~26% of every possible pair, i.e. "almost
        # everything is weakly related to almost everything". True in a trivial
        # sense, useless as information, and it buries the handful of weak edges
        # that actually mean something.
        #
        # So a weak edge means "among this post's closest concepts", not "above
        # a bar". The evidence band (>= AUTO_PROMOTE_MIN_COSINE) is left
        # UNCAPPED — a confident match should always be recorded, and genuine
        # cross-cutting membership is the whole point of the secondary axis.
        candidates: dict[int, list[tuple[float, int]]] = defaultdict(list)
        for cid, centroid in centroids.items():
            sims = post_matrix_normed @ centroid  # already normalized
            for pid, sim in zip(post_ids, sims.tolist()):
                if sim < threshold:
                    continue
                if pid in already_attached.get(cid, set()):
                    continue
                candidates[pid].append((float(sim), cid))

        floor = AUTO_PROMOTE_MIN_COSINE
        for pid, cands in candidates.items():
            cands.sort(reverse=True)  # best first
            strong = [c for c in cands if c[0] >= floor]
            budget = max(0, max_weak_per_post - weak_held.get(pid, 0))
            weakish = [c for c in cands if c[0] < floor][:budget]
            skipped = len(cands) - len(strong) - len(weakish)
            stats["weak_capped"] = stats.get("weak_capped", 0) + skipped
            for sim, cid in strong + weakish:
                band = "evidence" if sim >= floor else "weak-band"
                obs_id = _record_obs_in_txn(
                    conn,
                    post_id=pid, concept_id=cid,
                    source=SOURCE_SEMANTIC,
                    score_kind=SCORE_SEMANTIC,
                    raw_score=float(sim),
                    discovery_run_id=run_id,
                    discovery_model=model,
                    notes=f"cosine={sim:.3f} vs centroid ({band})",
                )
                if obs_id is not None:
                    stats["observations_created"] += 1

        _finish_run(conn, run_id, stats["posts_considered"],
                    stats["observations_created"],
                    notes=f"threshold={threshold} min_concept_edges={min_concept_edges}")
        conn.commit()

    return stats


# ---- Orphan clustering (new-concept discovery) ------------------------
#
# The gap this closes: mechanical passes create concepts only from structural
# coincidence (shared URL, shared @mention), and the semantic pass scores posts
# against centroids of concepts that ALREADY EXIST. Neither can propose a new
# category, so the vocabulary could only ever grow by hand. Roughly half the
# live corpus sat with no concept edge at all as a result.
#
# Why the vectors are centered first. Raw bge-small cosines on this corpus have
# mean 0.61 / p99 0.73 — every post is "AI stuff", so the shared topical
# direction swamps the differences and absolute-threshold clustering returns one
# blob of 366. Subtracting the corpus mean (the classic all-but-the-top trick)
# removes that common direction: mean pairwise drops to 0.008 and real structure
# separates. THRESHOLD below is therefore a cosine on CENTERED vectors and is not
# comparable to SEMANTIC_CENTROID_THRESHOLD, which is measured on raw ones.
#
# Tuned 2026-08-14 against 367 orphans: 0.40 yields ~7 clusters over ~15% of the
# orphan pool, which is the conservative end. Lower it to widen the net.
ORPHAN_CLUSTER_THRESHOLD = 0.40

# Below 4 posts a "theme" is usually a coincidence or one author's crossposts.
ORPHAN_CLUSTER_MIN_SIZE = 4

# Mean cosine of members to their own centroid. Guards against a technically
# large but semantically loose blob.
ORPHAN_CLUSTER_MIN_COHESION = 0.55

# Concepts created per run. The first run over a large orphan backlog would
# otherwise create a dozen at once; a cap turns that into a trickle that can be
# judged (and archived) a few at a time.
ORPHAN_CLUSTER_MAX_PER_RUN = 6

# CLAUDE.md: favour conceptual categories over per-person ones. A cluster that is
# mostly one prolific author is a per-person grouping wearing a theme's clothes,
# so skip it rather than grow one automatically. 0.55 rather than something
# looser because a 15-post cluster that was 60% one management writer sailed
# through the first 0.70 pass and even named itself after him.
ORPHAN_CLUSTER_MAX_AUTHOR_SHARE = 0.55

# A theme that three different people independently posted about is a theme; two
# people is usually a conversation.
ORPHAN_CLUSTER_MIN_AUTHORS = 3

SOURCE_CLUSTER = "cluster"
SCORE_CLUSTER = "centroid-cohesion"
CONCEPT_SOURCE_CLUSTER = "discovered-cluster"

_NAME_STOPWORDS = {
    'the','a','an','and','or','but','if','then','than','that','this','these','those',
    'is','are','was','were','be','been','being','have','has','had','do','does','did',
    'to','of','in','on','at','by','for','with','from','into','about','as','it','its',
    'you','your','he','she','they','them','their','his','her','we','our','us','i',
    'not','no','so','can','will','just','more','most','other','some','such','only',
    'own','same','too','very','s','t','don','now','one','two','three','post','posts',
    'thread','x','via','how','what','why','when','where','which','who','whom',
    'new','use','using','used','make','makes','get','gets','also','out','up','down',
    'over','under','after','before','because','while','all','any','each','both',
    'shares','share','claims','claim','says','said','notes','note','argues','points',
    'ai','llm','llms','model','models','agent','agents',   # corpus-universal, carry no signal
}


def _cluster_name_terms(texts: Sequence[str], corpus_df: dict, n_docs: int,
                        top_n: int = 3, banned: Optional[set] = None) -> list[str]:
    """Pick the most distinctive terms for a cluster (crude TF-IDF).

    Scores a term by how concentrated it is inside the cluster relative to how
    common it is across the whole corpus, so generic vocabulary loses to the
    handful of words that actually mark this group out.

    `banned` carries the cluster's own author names and handles. Without it a
    single prolific writer's name is by construction the most distinctive token
    in the group, and the concept ends up named after the person rather than the
    idea — which is the per-person grouping CLAUDE.md tells us not to grow.
    """
    import math
    from collections import Counter
    banned = banned or set()
    tf = Counter()
    for t in texts:
        seen = {w for w in re.findall(r"[a-z][a-z0-9+/.-]{2,}", (t or "").lower())
                if w not in _NAME_STOPWORDS and w not in banned and not w.isdigit()}
        tf.update(seen)
    if not tf:
        return []
    scored = []
    for term, count in tf.items():
        if count < 2:
            continue
        idf = math.log(n_docs / (1 + corpus_df.get(term, 0)))
        scored.append((count / len(texts) * idf, count, term))
    scored.sort(reverse=True)
    out, seen_stems = [], set()
    for _, _, term in scored:
        stem = term[:5]
        if stem in seen_stems:
            continue
        seen_stems.add(stem)
        out.append(term)
        if len(out) >= top_n:
            break
    return out


def discover_orphan_clusters(db_path: Path = DEFAULT_DB,
                             model: Optional[str] = None,
                             threshold: float = ORPHAN_CLUSTER_THRESHOLD,
                             min_size: int = ORPHAN_CLUSTER_MIN_SIZE,
                             min_cohesion: float = ORPHAN_CLUSTER_MIN_COHESION,
                             max_per_run: int = ORPHAN_CLUSTER_MAX_PER_RUN,
                             max_author_share: float = ORPHAN_CLUSTER_MAX_AUTHOR_SHARE,
                             min_authors: int = ORPHAN_CLUSTER_MIN_AUTHORS,
                             dry_run: bool = False,
                             with_lock: bool = True) -> dict:
    """Cluster concept-less posts and create a concept for each tight group.

    This is the pass that lets the vocabulary grow on its own. Posts with no
    `post_concepts` edge are clustered on their (mean-centered) embeddings; any
    group that clears the size, cohesion and author-diversity bars becomes a new
    active concept, with its members attached as SECONDARY edges. Primary homes
    are left to `assign_primaries()`, exactly as with `auto_curate()`.

    New concepts are auto-named from distinctive terms and marked `[auto-named]`
    in their description, so a rename sweep can find them:
        SELECT * FROM concepts WHERE description LIKE '%[auto-named]%'
    Any concept created here is reversible with `archive_concept(id)`.

    Set dry_run=True to get the same report with nothing written.

    Returns {orphans_examined, clusters_found, concepts_created, posts_attached,
             skipped_low_cohesion, skipped_author_concentration, clusters:[...]}.
    """
    try:
        try:
            from .embeddings import _blob_to_vector, DEFAULT_MODEL
        except ImportError:
            import sys as _sys
            _sys.path.insert(0, str(Path(__file__).parent))
            from embeddings import _blob_to_vector, DEFAULT_MODEL
        import numpy as np
    except ImportError as e:
        return {"error": f"orphan clustering requires fastembed + numpy: {e}",
                "orphans_examined": 0, "clusters_found": 0,
                "concepts_created": 0, "posts_attached": 0, "clusters": []}

    if model is None:
        model = DEFAULT_MODEL

    stats = {"orphans_examined": 0, "clusters_found": 0, "concepts_created": 0,
             "posts_attached": 0, "skipped_low_cohesion": 0,
             "skipped_author_concentration": 0, "clusters": []}

    with _maybe_lock(with_lock), _connect(db_path) as conn:
        # The corpus mean is the "AI content" direction we subtract out. Take it
        # over every embedded post, not just orphans, so it stays stable as the
        # orphan pool drains.
        all_rows = conn.execute(
            "SELECT vector FROM post_embeddings WHERE model=?", (model,)).fetchall()
        if len(all_rows) < 50:
            return {**stats, "error": "too few embeddings for a stable corpus mean"}
        A = np.vstack([_blob_to_vector(r["vector"]) for r in all_rows]).astype("float32")
        A /= (np.linalg.norm(A, axis=1, keepdims=True) + 1e-9)
        mu = A.mean(0)

        # "Orphan" means *no load-bearing home*, not "no edges at all". A post
        # carrying only weak edges has an association recorded but nowhere it
        # belongs, so it stays eligible here — otherwise generous weak-edge
        # attachment would quietly starve the one pass that can invent the
        # concept such a post actually needs.
        rows = conn.execute(f"""
            SELECT e.post_id, e.vector, p.author, p.handle, p.summary, p.content
              FROM post_embeddings e
              JOIN posts p ON p.id = e.post_id
             WHERE e.model = ?
               AND p.enrichment_status IN ('ok', 'legacy-ok')
               AND NOT EXISTS (
                   SELECT 1 FROM post_concepts pc
                    WHERE pc.post_id = p.id
                      AND pc.role IN ({','.join('?' * len(CANONICAL_ROLES))})
               )
        """, (model, *CANONICAL_ROLES)).fetchall()
        stats["orphans_examined"] = len(rows)
        if len(rows) < min_size:
            return stats

        M = np.vstack([_blob_to_vector(r["vector"]) for r in rows]).astype("float32")
        M /= (np.linalg.norm(M, axis=1, keepdims=True) + 1e-9)
        M = M - mu
        M /= (np.linalg.norm(M, axis=1, keepdims=True) + 1e-9)
        S = M @ M.T
        np.fill_diagonal(S, -1.0)

        # Greedy leader clustering: seed on the densest unassigned post, then
        # refine the membership against a recomputed centroid a few times.
        assigned: set = set()
        found = []
        degree = (S >= threshold).sum(1)
        for seed in np.argsort(-degree):
            seed = int(seed)
            if seed in assigned or degree[seed] < min_size - 1:
                continue
            members = [int(i) for i in np.where(S[seed] >= threshold)[0]
                       if int(i) not in assigned] + [seed]
            for _ in range(3):
                if not members:
                    break
                cen = M[members].mean(0)
                cen /= (np.linalg.norm(cen) + 1e-9)
                sims = M @ cen
                members = [int(i) for i in np.argsort(-sims)
                           if sims[i] >= threshold and int(i) not in assigned]
            if len(members) < min_size:
                continue
            cen = M[members].mean(0)
            cen /= (np.linalg.norm(cen) + 1e-9)
            cohesion = float((M[members] @ cen).mean())
            found.append({"members": members, "cohesion": cohesion})
            assigned |= set(members)
        stats["clusters_found"] = len(found)

        # Corpus document frequencies, for naming.
        from collections import Counter
        corpus_df: Counter = Counter()
        df_rows = conn.execute(
            "SELECT summary FROM posts WHERE enrichment_status IN ('ok','legacy-ok')"
        ).fetchall()
        for r in df_rows:
            corpus_df.update({w for w in re.findall(
                r"[a-z][a-z0-9+/.-]{2,}", (r["summary"] or "").lower())})
        n_docs = max(len(df_rows), 1)

        found.sort(key=lambda c: -c["cohesion"])
        run_id = None
        if not dry_run:
            run_id = _start_run(conn, SOURCE_CLUSTER, "orphan-cluster", model=model)

        for cl in found:
            if stats["concepts_created"] >= max_per_run:
                break
            members = cl["members"]
            if cl["cohesion"] < min_cohesion:
                stats["skipped_low_cohesion"] += 1
                continue

            authors = [(rows[i]["author"] or "?") for i in members]
            top_author, top_count = Counter(authors).most_common(1)[0]
            share = top_count / len(members)
            n_authors = len(set(authors))
            if share > max_author_share or n_authors < min_authors:
                stats["skipped_author_concentration"] += 1
                stats["clusters"].append({
                    "skipped": "author-concentration", "size": len(members),
                    "cohesion": round(cl["cohesion"], 3),
                    "dominant_author": top_author,
                    "author_share": round(share, 2),
                    "distinct_authors": n_authors})
                continue

            # Keep the authors' own names out of the running for the label.
            banned = set()
            for i in members:
                for field in (rows[i]["author"], rows[i]["handle"]):
                    for w in re.findall(r"[a-z][a-z0-9+/.-]{2,}", (field or "").lower()):
                        banned.add(w)

            terms = _cluster_name_terms(
                [f'{rows[i]["summary"] or ""} {(rows[i]["content"] or "")[:400]}'
                 for i in members], corpus_df, n_docs, banned=banned)
            name = " / ".join(terms) if terms else f"unnamed cluster ({len(members)} posts)"
            cen = M[members].mean(0)
            cen /= (np.linalg.norm(cen) + 1e-9)
            ordered = sorted(members, key=lambda i: -float(M[i] @ cen))
            post_ids = [int(rows[i]["post_id"]) for i in ordered]

            entry = {"name": name, "size": len(members),
                     "cohesion": round(cl["cohesion"], 3),
                     "dominant_author": top_author,
                     "author_share": round(share, 2),
                     "post_ids": post_ids,
                     "sample": [(rows[i]["summary"] or "")[:110] for i in ordered[:3]]}

            if dry_run:
                entry["concept_id"] = None
                stats["clusters"].append(entry)
                stats["concepts_created"] += 1
                stats["posts_attached"] += len(members)
                continue

            desc = (f"[auto-named] Discovered by orphan clustering on "
                    f"{_now()[:10]} from {len(members)} posts with no prior concept "
                    f"(cohesion {cl['cohesion']:.2f}). Rename or archive if this "
                    f"isn't a real theme.")
            cur = conn.execute("""
                INSERT INTO concepts (name, description, source, status, created_at, updated_at)
                VALUES (?, ?, ?, 'active', ?, ?)
            """, (name, desc, CONCEPT_SOURCE_CLUSTER, _now(), _now()))
            concept_id = cur.lastrowid

            for i in ordered:
                pid = int(rows[i]["post_id"])
                obs_id = _record_obs_in_txn(
                    conn, post_id=pid, concept_id=concept_id,
                    source=SOURCE_CLUSTER, score_kind=SCORE_CLUSTER,
                    raw_score=float(M[i] @ cen), discovery_run_id=run_id,
                    discovery_model=model,
                    notes=f"orphan cluster seed (cohesion {cl['cohesion']:.2f})")
                conn.execute("""
                    INSERT OR IGNORE INTO post_concepts
                        (post_id, concept_id, role, promoted_from_observation_id,
                         notes, promoted_at, is_primary)
                    VALUES (?, ?, 'evidence', ?, 'auto-filed by orphan clustering', ?, 0)
                """, (pid, concept_id, obs_id, _now()))
                if obs_id is not None:
                    conn.execute(
                        "UPDATE concept_observations SET status='promoted' WHERE id=?",
                        (obs_id,))
                stats["posts_attached"] += 1

            entry["concept_id"] = concept_id
            stats["clusters"].append(entry)
            stats["concepts_created"] += 1

        if not dry_run:
            _finish_run(conn, run_id, stats["orphans_examined"],
                        stats["posts_attached"],
                        notes=(f"threshold={threshold} min_size={min_size} "
                               f"min_cohesion={min_cohesion} created={stats['concepts_created']}"))
            conn.commit()

    return stats


# ---- Latent discovery (blinded, model-in-the-loop) --------------------
#
# The design doc specs latent as "a blinded LLM pass". The pipeline is plain
# Python with no model available to it, so the pass is split in two around the
# model rather than trying to call one from inside the pipeline:
#
#     prepare_latent_batch()   -> a blinded payload + an open discovery_run
#     ... a Cowork skill run (or a human) reads it and proposes threads ...
#     record_latent_findings() -> concepts + observations, full provenance
#
# This keeps the expensive judgement where a model actually exists, while the
# sampling, blinding, gating and provenance stay deterministic and testable.
#
# BLINDING IS THE POINT. Semantic discovery already tells us what looks like
# what we've already named. The latent pass exists to find threads that cut
# ACROSS the categories we drew, so the reader must not see those categories —
# otherwise it just re-derives them and reports them back as insight.

LATENT_DEFAULT_BATCH = 45
LATENT_GATE_THRESHOLD = 0.05

SAMPLING_RANDOM = "random"
SAMPLING_CROSS_CATEGORY = "biased-cross-category"
SAMPLING_ORPHAN_HEAVY = "orphan-heavy"

BLIND_TAGS = "blind-tags"                # hide topics + concept membership
BLIND_TAGS_AUTHOR = "blind-tags-author"  # also hide author/handle
BLIND_ALL = "blind-tags-author-date"     # also hide dates


def prepare_latent_batch(db_path: Path = DEFAULT_DB,
                         batch_size: int = LATENT_DEFAULT_BATCH,
                         sampling: str = SAMPLING_CROSS_CATEGORY,
                         blinding: str = BLIND_TAGS,
                         persona: Optional[str] = None,
                         model: Optional[str] = None,
                         seed: Optional[int] = None,
                         enforce_gate: bool = True,
                         with_lock: bool = True) -> dict:
    """Assemble a blinded batch of posts for a latent discovery pass.

    Opens a `discovery_runs` row and returns the run id alongside the blinded
    items. Nothing is written to the graph here — call `record_latent_findings`
    with the same run_id once the reader has proposed threads.

    Sampling strategies:
      - `biased-cross-category` (default): round-robin across primary concept
        homes, plus a slice of unhomed posts. Maximises the chance that any
        thread the reader spots genuinely crosses an existing boundary rather
        than restating one concept.
      - `orphan-heavy`: draw mostly from posts with no concept edge.
      - `random`: uniform over live posts.

    Blinding removes the fields named by the strategy from the returned items.
    The mapping from opaque `ref` back to post_id is kept server-side in the
    returned `key` dict — the reader works only with refs, so it cannot
    accidentally look a post up and re-acquire the context we just hid.

    Gate: refuses to run while recoverable incompleteness is above 5% unless
    `enforce_gate=False`. Clever threads found in noise are worse than none.
    """
    import random as _random
    try:
        from .enrich import gate_ratio
    except ImportError:
        import sys as _sys
        _sys.path.insert(0, str(Path(__file__).parent))
        from enrich import gate_ratio

    ratio, breakdown = gate_ratio(db_path=db_path) if _gr_takes_db() else gate_ratio()
    if enforce_gate and ratio >= LATENT_GATE_THRESHOLD:
        return {"error": f"latent gate closed: ratio {ratio:.4f} >= {LATENT_GATE_THRESHOLD}",
                "gate_ratio": ratio, "items": [], "run_id": None}

    rng = _random.Random(seed)

    with _maybe_lock(with_lock), _connect(db_path) as conn:
        rows = conn.execute("""
            SELECT p.id, p.date, p.author, p.handle, p.summary, p.content, p.url,
                   (SELECT c.name FROM post_concepts pc JOIN concepts c ON c.id = pc.concept_id
                     WHERE pc.post_id = p.id AND pc.is_primary = 1) AS home
              FROM posts p
             WHERE p.enrichment_status IN ('ok', 'legacy-ok')
               AND COALESCE(p.summary, '') <> ''
        """).fetchall()
        if not rows:
            return {"error": "no live posts", "items": [], "run_id": None}

        by_home: dict = {}
        for r in rows:
            by_home.setdefault(r["home"], []).append(r)
        for bucket in by_home.values():
            rng.shuffle(bucket)

        picked = []
        if sampling == SAMPLING_RANDOM:
            picked = rng.sample(rows, min(batch_size, len(rows)))
        elif sampling == SAMPLING_ORPHAN_HEAVY:
            orphans = by_home.get(None, [])
            picked = orphans[:batch_size]
            if len(picked) < batch_size:
                rest = [r for r in rows if r["home"] is not None]
                rng.shuffle(rest)
                picked += rest[:batch_size - len(picked)]
        else:
            # Round-robin across homes so no single concept dominates the batch.
            homes = sorted(by_home.keys(), key=lambda h: (h is None, str(h)))
            i = 0
            while len(picked) < batch_size and any(by_home[h] for h in homes):
                h = homes[i % len(homes)]
                if by_home[h]:
                    picked.append(by_home[h].pop())
                i += 1

        run_id = _start_run(conn, SOURCE_LATENT, sampling,
                            persona=persona, model=model)
        conn.execute("UPDATE discovery_runs SET blinding_strategy=? WHERE id=?",
                     (blinding, run_id))

        items, key = [], {}
        for n, r in enumerate(picked, 1):
            ref = f"P{n:03d}"
            key[ref] = int(r["id"])
            item = {"ref": ref,
                    "text": (r["summary"] or "").strip(),
                    "excerpt": (r["content"] or "")[:500].strip()}
            if blinding == BLIND_TAGS:
                item["author"] = r["author"]
                item["date"] = r["date"]
            elif blinding == BLIND_TAGS_AUTHOR:
                item["date"] = r["date"]
            # BLIND_ALL adds neither.
            items.append(item)

        conn.commit()

    return {"run_id": run_id, "items": items, "key": key,
            "sampling": sampling, "blinding": blinding,
            "persona": persona, "model": model,
            "gate_ratio": ratio, "batch_size": len(items)}


def _gr_takes_db() -> bool:
    """gate_ratio's signature has varied; probe once rather than guess."""
    import inspect
    try:
        from .enrich import gate_ratio
    except ImportError:
        from enrich import gate_ratio
    return "db_path" in inspect.signature(gate_ratio).parameters


def record_latent_findings(run_id: int,
                           findings: Sequence[dict],
                           key: dict,
                           db_path: Path = DEFAULT_DB,
                           persona: Optional[str] = None,
                           model: Optional[str] = None,
                           auto_create_min_posts: int = 3,
                           attach_to_existing: bool = True,
                           with_lock: bool = True) -> dict:
    """Write the threads a latent reader proposed back into the graph.

    Each finding is a dict:
        {"name": str,
         "description": str,
         "refs": ["P003", "P017", ...],      # opaque refs from the batch
         "confidence": float,                 # 0-1, the reader's own estimate
         "existing_concept_id": int | None}   # set to attach to a known concept

    A finding with `existing_concept_id` attaches evidence to that concept. One
    without creates a new concept, provided it cites at least
    `auto_create_min_posts` posts — a "thread" of two is usually a coincidence.

    Every edge lands as SECONDARY (is_primary=0); `assign_primaries()` decides
    homes afterwards, same contract as auto_curate and orphan clustering. All
    observations carry source='latent', score_kind='llm-self-report', and the
    run/persona/model provenance, so latent-derived structure stays auditable
    and separable from mechanical and semantic work.
    """
    stats = {"concepts_created": 0, "concepts_attached": 0, "edges": 0,
             "skipped_too_small": 0, "skipped_bad_refs": 0, "details": []}

    with _maybe_lock(with_lock), _connect(db_path) as conn:
        for f in findings:
            refs = [r for r in f.get("refs", []) if r in key]
            if len(refs) != len(f.get("refs", [])):
                stats["skipped_bad_refs"] += 1
            post_ids = [key[r] for r in refs]
            # A post can be cited once per finding, no more.
            post_ids = list(dict.fromkeys(post_ids))

            existing_id = f.get("existing_concept_id")
            if existing_id is None and len(post_ids) < auto_create_min_posts:
                stats["skipped_too_small"] += 1
                stats["details"].append(
                    {"name": f.get("name"), "skipped": "too-few-posts",
                     "n": len(post_ids)})
                continue
            if existing_id is not None and not attach_to_existing:
                continue
            if not post_ids:
                continue

            if existing_id is not None:
                concept_id = int(existing_id)
                stats["concepts_attached"] += 1
            else:
                desc = (f.get("description") or "").strip()
                desc += (f"\n\n[latent] Proposed by a blinded latent pass "
                         f"(run {run_id}) from {len(post_ids)} posts read without "
                         f"their existing topic or concept tags.")
                cur = conn.execute("""
                    INSERT INTO concepts (name, description, source, status, created_at, updated_at)
                    VALUES (?, ?, ?, 'active', ?, ?)
                """, (f["name"].strip(), desc, CONCEPT_SOURCE_DISCOVERED, _now(), _now()))
                concept_id = cur.lastrowid
                stats["concepts_created"] += 1

            conf = float(f.get("confidence", 0.6))
            # A latent reader can legitimately say "these posts belong with that
            # concept because they argue the opposite" — the role vocabulary
            # already exists for exactly this, so honour it.
            role = f.get("role", ROLE_EVIDENCE)
            for pid in post_ids:
                obs_id = _record_obs_in_txn(
                    conn, post_id=pid, concept_id=concept_id,
                    source=SOURCE_LATENT, score_kind=SCORE_LATENT,
                    raw_score=conf, discovery_run_id=run_id,
                    discovery_persona=persona, discovery_model=model,
                    notes=f.get("why"), role_suggestion=role)
                conn.execute("""
                    INSERT OR IGNORE INTO post_concepts
                        (post_id, concept_id, role, promoted_from_observation_id,
                         notes, promoted_at, is_primary)
                    VALUES (?, ?, ?, ?, 'latent pass', ?, 0)
                """, (pid, concept_id, role, obs_id, _now()))
                # If the edge already existed, INSERT OR IGNORE just dropped the
                # role on the floor. 'evidence' is the schema default and so
                # carries no information; anything more specific does. Upgrade
                # in that one direction only — never clobber a role someone
                # already chose deliberately.
                if role != ROLE_EVIDENCE:
                    upd = conn.execute("""
                        UPDATE post_concepts
                           SET role = ?, notes = COALESCE(notes || ' | ', '') || 'role refined by latent pass'
                         WHERE post_id = ? AND concept_id = ? AND role = ?
                    """, (role, pid, concept_id, ROLE_EVIDENCE))
                    if upd.rowcount:
                        stats["roles_refined"] = stats.get("roles_refined", 0) + 1
                if obs_id is not None:
                    conn.execute(
                        "UPDATE concept_observations SET status='promoted' WHERE id=?",
                        (obs_id,))
                stats["edges"] += 1

            stats["details"].append({"concept_id": concept_id,
                                     "name": f.get("name"),
                                     "posts": len(post_ids),
                                     "new": existing_id is None})

        _finish_run(conn, run_id, len(key), stats["edges"],
                    notes=(f"latent: +{stats['concepts_created']} concepts, "
                           f"{stats['concepts_attached']} attached, "
                           f"{stats['edges']} edges"))
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
