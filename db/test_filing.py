#!/usr/bin/env python3
"""Regression tests for abstain-aware filing (db/filing.py).

The invariant: **the classifier may decline.** Every other property here exists
to keep that meaningful — an abstention must be a no-op rather than an
un-homing, a thin margin must not become a confident answer, and the candidate
set must stay bounded so the scorer can never invent a home a post has no edge
to. If any of those leak, this degrades into assign_primaries with extra steps.

Run:  python3 -m db.test_filing
"""
from __future__ import annotations

import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import numpy as np

from db import filing as F


def _make_db(posts, concepts, edges, primaries=(), pins=()) -> Path:
    """posts: {id: vector}; concepts: {id: (name, status)}; edges: [(pid, cid)]"""
    tmp = Path(tempfile.mkdtemp()) / "t.db"
    conn = sqlite3.connect(tmp)
    conn.executescript("""
        CREATE TABLE posts (id INTEGER PRIMARY KEY, date TEXT, author TEXT,
                            summary TEXT, enrichment_status TEXT DEFAULT 'ok');
        CREATE TABLE concepts (id INTEGER PRIMARY KEY, name TEXT,
                               description TEXT DEFAULT '', status TEXT DEFAULT 'active');
        CREATE TABLE post_concepts (post_id INTEGER, concept_id INTEGER,
                                    role TEXT DEFAULT 'evidence', notes TEXT,
                                    is_primary INTEGER DEFAULT 0,
                                    PRIMARY KEY (post_id, concept_id));
        CREATE TABLE post_embeddings (post_id INTEGER PRIMARY KEY, model TEXT,
                                      dim INTEGER, content_hash TEXT, vector BLOB);
    """)
    for pid, vec in posts.items():
        conn.execute("INSERT INTO posts (id, date, author, summary) VALUES (?,?,?,?)",
                     (pid, "2026-01-01", f"a{pid}", "s"))
        conn.execute("INSERT INTO post_embeddings (post_id, vector) VALUES (?,?)",
                     (pid, np.asarray(vec, dtype=np.float32).tobytes()))
    for cid, (name, status) in concepts.items():
        conn.execute("INSERT INTO concepts (id, name, status) VALUES (?,?,?)",
                     (cid, name, status))
    for pid, cid in edges:
        note = F.PRIMARY_PIN_MARKER if (pid, cid) in set(pins) else None
        conn.execute("""INSERT INTO post_concepts (post_id, concept_id, role, notes, is_primary)
                        VALUES (?,?,'evidence',?,?)""",
                     (pid, cid, note, 1 if (pid, cid) in set(primaries) else 0))
    conn.commit()
    conn.close()
    return tmp


def _spread(base, jitter, n, dim=8, seed=0):
    """n vectors clustered around `base` with a given jitter."""
    rng = np.random.default_rng(seed)
    v = np.zeros(dim, dtype=np.float32)
    v[base] = 1.0
    return [v + jitter * rng.standard_normal(dim).astype(np.float32) for _ in range(n)]


class AbstainBehaviour(unittest.TestCase):
    def test_thin_margin_abstains(self):
        """Two equally-good candidates must produce no answer, not a coin flip."""
        # One post sitting exactly between two tight, symmetric clusters.
        a = _spread(0, 0.01, 4, seed=1)
        b = _spread(1, 0.01, 4, seed=2)
        mid = (np.eye(8, dtype=np.float32)[0] + np.eye(8, dtype=np.float32)[1]) / 2
        posts = {i + 1: v for i, v in enumerate(a + b)}
        posts[99] = mid
        edges = [(i + 1, 1) for i in range(4)] + [(i + 5, 2) for i in range(4)]
        edges += [(99, 1), (99, 2)]
        db = _make_db(posts, {1: ("alpha", "active"), 2: ("beta", "active")}, edges)
        d = {x.post_id: x for x in F.classify(db_path=db)}[99]
        self.assertTrue(d.abstained, f"expected abstain, got {d.chosen} ({d.reason})")
        self.assertIsNone(d.chosen)

    def test_clear_winner_is_chosen(self):
        a = _spread(0, 0.01, 4, seed=1)
        b = _spread(4, 0.01, 4, seed=2)
        near_a = np.eye(8, dtype=np.float32)[0] + 0.01
        posts = {i + 1: v for i, v in enumerate(a + b)}
        posts[99] = near_a
        edges = [(i + 1, 1) for i in range(4)] + [(i + 5, 2) for i in range(4)]
        edges += [(99, 1), (99, 2)]
        db = _make_db(posts, {1: ("alpha", "active"), 2: ("beta", "active")}, edges)
        d = {x.post_id: x for x in F.classify(db_path=db)}[99]
        self.assertFalse(d.abstained, d.reason)
        self.assertEqual(d.chosen, 1)

    def test_abstention_never_unhomes(self):
        """A thin margin is 'I cannot tell', not 'this belongs nowhere'."""
        a = _spread(0, 0.01, 4, seed=1)
        b = _spread(1, 0.01, 4, seed=2)
        mid = (np.eye(8, dtype=np.float32)[0] + np.eye(8, dtype=np.float32)[1]) / 2
        posts = {i + 1: v for i, v in enumerate(a + b)}
        posts[99] = mid
        edges = [(i + 1, 1) for i in range(4)] + [(i + 5, 2) for i in range(4)]
        edges += [(99, 1), (99, 2)]
        db = _make_db(posts, {1: ("alpha", "active"), 2: ("beta", "active")},
                      edges, primaries=[(99, 1)])
        res = F.apply(db_path=db, dry_run=False, with_lock=False)
        still = sqlite3.connect(db).execute(
            "SELECT concept_id FROM post_concepts WHERE post_id=99 AND is_primary=1"
        ).fetchone()
        self.assertIsNotNone(still, "abstaining must not strip an existing home")
        self.assertEqual(still[0], 1)
        # Scoped to the abstaining post: other posts in the fixture have no home
        # at all, and filing those *is* wanted work — an abstention is a no-op
        # for the post it applies to, not a freeze on the whole run.
        touched = [d for d in res["decisions"] if d.post_id == 99 and d.changes]
        self.assertEqual(touched, [], "the abstaining post must not be rewritten")

    def test_absolute_floor_abstains_even_with_wide_margin(self):
        """Least-bad is not the same as good."""
        a = _spread(0, 0.01, 4, seed=1)
        b = _spread(1, 0.01, 4, seed=2)
        orthogonal = np.eye(8, dtype=np.float32)[7]
        posts = {i + 1: v for i, v in enumerate(a + b)}
        posts[99] = orthogonal
        edges = [(i + 1, 1) for i in range(4)] + [(i + 5, 2) for i in range(4)]
        edges += [(99, 1), (99, 2)]
        db = _make_db(posts, {1: ("alpha", "active"), 2: ("beta", "active")}, edges)
        d = {x.post_id: x for x in F.classify(db_path=db, abstain_min_top=0.9)}[99]
        self.assertTrue(d.abstained)
        self.assertIn("floor", d.reason)


class BoundedCandidateSet(unittest.TestCase):
    def test_never_chooses_a_concept_the_post_has_no_edge_to(self):
        """The CLM contract: score the supplied actions, never invent one."""
        a = _spread(0, 0.01, 4, seed=1)
        b = _spread(1, 0.01, 4, seed=2)
        posts = {i + 1: v for i, v in enumerate(a + b)}
        # post 99 sits right on cluster b but is only edged to concept 1
        posts[99] = np.eye(8, dtype=np.float32)[1]
        edges = [(i + 1, 1) for i in range(4)] + [(i + 5, 2) for i in range(4)]
        edges += [(99, 1)]
        db = _make_db(posts, {1: ("alpha", "active"), 2: ("beta", "active")}, edges)
        d = {x.post_id: x for x in F.classify(db_path=db)}[99]
        self.assertIn(d.chosen, (1, None))
        self.assertNotEqual(d.chosen, 2, "scored a concept outside the candidate set")

    def test_conceptual_preferred_over_mechanical(self):
        a = _spread(0, 0.01, 4, seed=1)
        posts = {i + 1: v for i, v in enumerate(a)}
        posts[99] = np.eye(8, dtype=np.float32)[0]
        edges = [(i + 1, 1) for i in range(4)] + [(i + 1, 2) for i in range(4)]
        edges += [(99, 1), (99, 2)]
        db = _make_db(posts, {1: ("real theme", "active"),
                              2: ("url:https://example.com", "active")}, edges)
        d = {x.post_id: x for x in F.classify(db_path=db)}[99]
        self.assertTrue(all(cid != 2 for _, cid in d.candidates),
                        "a url: grouping must be dropped when a conceptual home exists")

    def test_mechanical_allowed_when_it_is_all_there_is(self):
        """Preference, not prohibition — better a url: home than none."""
        a = _spread(0, 0.01, 4, seed=1)
        posts = {i + 1: v for i, v in enumerate(a)}
        posts[99] = np.eye(8, dtype=np.float32)[0]
        edges = [(i + 1, 2) for i in range(4)] + [(99, 2)]
        db = _make_db(posts, {2: ("url:https://example.com", "active")}, edges)
        d = {x.post_id: x for x in F.classify(db_path=db)}[99]
        self.assertEqual([cid for _, cid in d.candidates], [2])


class SafetyProperties(unittest.TestCase):
    def test_dry_run_is_the_default_and_writes_nothing(self):
        a = _spread(0, 0.01, 4, seed=1)
        b = _spread(4, 0.01, 4, seed=2)
        posts = {i + 1: v for i, v in enumerate(a + b)}
        posts[99] = np.eye(8, dtype=np.float32)[0] + 0.01
        edges = [(i + 1, 1) for i in range(4)] + [(i + 5, 2) for i in range(4)]
        edges += [(99, 1), (99, 2)]
        db = _make_db(posts, {1: ("alpha", "active"), 2: ("beta", "active")},
                      edges, primaries=[(99, 2)])
        res = F.apply(db_path=db, with_lock=False)          # no dry_run kwarg
        self.assertTrue(res["dry_run"])
        got = sqlite3.connect(db).execute(
            "SELECT concept_id FROM post_concepts WHERE post_id=99 AND is_primary=1"
        ).fetchone()[0]
        self.assertEqual(got, 2, "default call must not write")

    def test_pins_are_never_recomputed(self):
        a = _spread(0, 0.01, 4, seed=1)
        b = _spread(4, 0.01, 4, seed=2)
        posts = {i + 1: v for i, v in enumerate(a + b)}
        posts[99] = np.eye(8, dtype=np.float32)[0] + 0.01
        edges = [(i + 1, 1) for i in range(4)] + [(i + 5, 2) for i in range(4)]
        edges += [(99, 1), (99, 2)]
        db = _make_db(posts, {1: ("alpha", "active"), 2: ("beta", "active")},
                      edges, primaries=[(99, 2)], pins=[(99, 2)])
        d = {x.post_id: x for x in F.classify(db_path=db)}[99]
        self.assertTrue(d.pinned)
        self.assertTrue(d.abstained)

    def test_never_dismisses_an_observation(self):
        """No-discard policy: this module must not contain a dismissal path."""
        src = Path(F.__file__).read_text()
        self.assertNotIn("dismiss_observation", src)
        self.assertNotIn("DELETE FROM", src.upper().replace("DELETE  FROM", "DELETE FROM"))

    def test_archived_concepts_are_not_candidates(self):
        a = _spread(0, 0.01, 4, seed=1)
        posts = {i + 1: v for i, v in enumerate(a)}
        posts[99] = np.eye(8, dtype=np.float32)[0]
        edges = [(i + 1, 1) for i in range(4)] + [(99, 1)]
        db = _make_db(posts, {1: ("retired", "archived")}, edges)
        d = {x.post_id: x for x in F.classify(db_path=db)}.get(99)
        self.assertTrue(d is None or d.abstained,
                        "an archived concept must never be offered as a home")


class Centering(unittest.TestCase):
    def test_scoring_is_mean_centered(self):
        """Centered scores must separate clusters raw cosine cannot.

        Two clusters sharing a large common direction: raw cosine calls them
        nearly identical, centered cosine pulls them apart. This is the corpus
        condition ('everything is AI stuff') in miniature.
        """
        common = np.zeros(8, dtype=np.float32)
        common[0] = 3.0
        a = [common + np.eye(8, dtype=np.float32)[1] * 0.3 for _ in range(4)]
        b = [common + np.eye(8, dtype=np.float32)[2] * 0.3 for _ in range(4)]
        probe = common + np.eye(8, dtype=np.float32)[1] * 0.3

        def cos(x, y):
            return float(x @ y / (np.linalg.norm(x) * np.linalg.norm(y)))

        raw_gap = abs(cos(probe, np.mean(a, 0)) - cos(probe, np.mean(b, 0)))

        posts = {i + 1: v for i, v in enumerate(a + b)}
        posts[99] = probe
        edges = [(i + 1, 1) for i in range(4)] + [(i + 5, 2) for i in range(4)]
        edges += [(99, 1), (99, 2)]
        db = _make_db(posts, {1: ("alpha", "active"), 2: ("beta", "active")}, edges)
        d = {x.post_id: x for x in F.classify(db_path=db)}[99]
        self.assertEqual(d.chosen, 1, d.reason)
        self.assertGreater(d.margin, raw_gap,
                           "centering must widen the margin raw cosine reports")


class StabilityHarness(unittest.TestCase):
    """The label-free eval. Ground truth doesn't exist on this corpus — of 577
    homes, 139 are forced and 380 of the rest were sub-0.01 coin flips — so the
    classifier is validated by asking whether a decision survives resampling
    the concept membership it depended on, not by scoring it against homes that
    are themselves noise.
    """

    def _two_clusters(self, probe, jitter=0.01):
        a = _spread(0, jitter, 5, seed=1)
        b = _spread(4, jitter, 5, seed=2)
        posts = {i + 1: v for i, v in enumerate(a + b)}
        posts[99] = probe
        edges = [(i + 1, 1) for i in range(5)] + [(i + 6, 2) for i in range(5)]
        edges += [(99, 1), (99, 2)]
        return _make_db(posts, {1: ("alpha", "active"), 2: ("beta", "active")}, edges)

    def test_stability_is_deterministic(self):
        """A threshold derived from a number that moves each run isn't a
        calibration."""
        db = self._two_clusters(np.eye(8, dtype=np.float32)[0] + 0.05)
        a = F.stability(db_path=db, resamples=10)
        b = F.stability(db_path=db, resamples=10)
        self.assertEqual(a, b)

    def test_single_candidate_is_trivially_stable(self):
        a = _spread(0, 0.01, 4, seed=1)
        posts = {i + 1: v for i, v in enumerate(a)}
        posts[99] = np.eye(8, dtype=np.float32)[0]
        edges = [(i + 1, 1) for i in range(4)] + [(99, 1)]
        db = _make_db(posts, {1: ("alpha", "active")}, edges)
        self.assertEqual(F.stability(db_path=db, resamples=5)[99], 1.0)

    def test_clear_winner_more_stable_than_ambiguous(self):
        """The property the whole margin design rests on.

        The ambiguous fixture needs *overlapping* clusters, not merely a probe
        placed between two tight ones: with tight clusters the midpoint still
        lands on the same side under every resample, which is correct behaviour
        and precisely why it isn't a test of instability.
        """
        clear = F.stability(
            db_path=self._two_clusters(np.eye(8, dtype=np.float32)[0]),
            resamples=20)[99]
        mid = (np.eye(8, dtype=np.float32)[0] + np.eye(8, dtype=np.float32)[4]) / 2
        ambiguous = F.stability(
            db_path=self._two_clusters(mid, jitter=0.8), resamples=20)[99]
        self.assertEqual(clear, 1.0)
        self.assertLess(ambiguous, clear,
                        "overlapping clusters must not yield a stable home")

    def test_calibrate_respects_the_target(self):
        db = self._two_clusters(np.eye(8, dtype=np.float32)[0] + 0.05)
        r = F.calibrate(db_path=db, target_stability=0.8, resamples=10)
        self.assertIn("curve", r)
        self.assertEqual(r["current_margin"], F.ABSTAIN_MARGIN)
        if r["recommended_margin"] is not None:
            self.assertGreaterEqual(r["stability_at_recommended"], 0.8)

    def test_calibrate_reports_no_threshold_when_target_unreachable(self):
        """Honest failure: if the geometry can't support the confidence asked
        for, say so rather than returning the least-bad number."""
        mid = (np.eye(8, dtype=np.float32)[0] + np.eye(8, dtype=np.float32)[4]) / 2
        db = self._two_clusters(mid)
        r = F.calibrate(db_path=db, target_stability=1.01, resamples=10)
        self.assertIsNone(r["recommended_margin"])

    def test_scorer_bootstrap_only_perturbs_membership(self):
        """Without an rng the scorer must be exact — bootstrap is opt-in."""
        db = self._two_clusters(np.eye(8, dtype=np.float32)[0] + 0.05)
        sc = F._Scorer(db)
        self.assertEqual(sc.score(99), sc.score(99))


if __name__ == "__main__":
    unittest.main(verbosity=2)
