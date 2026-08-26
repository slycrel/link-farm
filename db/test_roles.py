#!/usr/bin/env python3
"""Regression tests for the role-aware concept graph.

The invariant these protect: **weak edges buy recall without costing
precision.** A `weak` edge records that a post is associated with a concept,
but must not influence what the concept *means* — so it may not feed centroids,
may not qualify a concept for semantic scoring, may not become a post's primary
home, and may not hide a post from orphan clustering. If any of those leak,
`auto_curate()`'s generous attachment silently degrades every downstream pass,
which is precisely the failure mode the old dismiss-everything policy avoided
by throwing information away.

Run:  python3 -m db.test_roles
"""
from __future__ import annotations

import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import numpy as np

from db import concepts as C
from db import embeddings as E


def _make_db() -> Path:
    """Minimal schema mirroring the real one for the tables under test."""
    tmp = Path(tempfile.mkdtemp()) / "t.db"
    conn = sqlite3.connect(tmp)
    conn.executescript("""
        CREATE TABLE posts (
            id INTEGER PRIMARY KEY, date TEXT, author TEXT, handle TEXT,
            subject TEXT, url TEXT, summary TEXT, content TEXT,
            enrichment_status TEXT DEFAULT 'ok', notes TEXT
        );
        CREATE TABLE concepts (
            id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL,
            description TEXT, source TEXT DEFAULT 'curated',
            status TEXT DEFAULT 'active', merged_into INTEGER,
            created_at TEXT DEFAULT (datetime('now')),
            updated_at TEXT DEFAULT (datetime('now'))
        );
        CREATE TABLE post_concepts (
            post_id INTEGER NOT NULL, concept_id INTEGER NOT NULL,
            role TEXT NOT NULL DEFAULT 'evidence',
            promoted_from_observation_id INTEGER, notes TEXT,
            promoted_at TEXT DEFAULT (datetime('now')),
            is_primary INTEGER NOT NULL DEFAULT 0,
            PRIMARY KEY (post_id, concept_id)
        );
        CREATE UNIQUE INDEX ux_primary ON post_concepts(post_id)
            WHERE is_primary = 1;
        CREATE TABLE concept_observations (
            id INTEGER PRIMARY KEY AUTOINCREMENT, post_id INTEGER NOT NULL,
            concept_id INTEGER NOT NULL,
            role_suggestion TEXT NOT NULL DEFAULT 'evidence',
            raw_score REAL NOT NULL DEFAULT 1.0, score_kind TEXT NOT NULL,
            source TEXT NOT NULL, discovery_run_id INTEGER,
            discovery_persona TEXT, discovery_model TEXT,
            status TEXT NOT NULL DEFAULT 'pending',
            observed_at TEXT DEFAULT (datetime('now')), notes TEXT
        );
        CREATE TABLE post_embeddings (
            post_id INTEGER PRIMARY KEY, model TEXT, dim INTEGER,
            vector BLOB, content_hash TEXT
        );
        CREATE TABLE discovery_runs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            started_at TEXT DEFAULT (datetime('now')), finished_at TEXT,
            source TEXT NOT NULL, persona TEXT, model TEXT,
            sampling_strategy TEXT, blinding_strategy TEXT,
            posts_examined INTEGER, observations_created INTEGER, notes TEXT
        );
    """)
    conn.commit()
    conn.close()
    return tmp


def _vec(*xs) -> np.ndarray:
    v = np.array(xs, dtype="float32")
    return v / (np.linalg.norm(v) or 1.0)


class RoleAwareCentroids(unittest.TestCase):
    def setUp(self):
        self.db = _make_db()
        conn = sqlite3.connect(self.db)
        # Concept 1 with two evidence posts pointing one way (+x) and one
        # weak post pointing the opposite way (-x). If the weak edge leaks
        # into the centroid it will drag it toward zero/negative.
        # NB the third vector is orthogonal (+y), not antiparallel. Centroids
        # are renormalized, so an antiparallel outlier barely moves the *unit*
        # direction when two aligned vectors dominate — an orthogonal one shifts
        # it measurably, which is what makes the leak detectable.
        conn.execute("INSERT INTO concepts (id, name) VALUES (1, 'thing')")
        for pid, vec, role in [(10, _vec(1, 0), 'evidence'),
                               (11, _vec(1, 0.1), 'evidence'),
                               (12, _vec(0, 1), 'weak')]:
            conn.execute("INSERT INTO posts (id, summary) VALUES (?, 's')", (pid,))
            conn.execute(
                "INSERT INTO post_embeddings (post_id, model, dim, vector) VALUES (?,?,?,?)",
                (pid, E.DEFAULT_MODEL, 2, E._vector_to_blob(vec)))
            conn.execute(
                "INSERT INTO post_concepts (post_id, concept_id, role) VALUES (?,1,?)",
                (pid, role))
        conn.commit()
        conn.close()

    def test_weak_edge_excluded_from_centroid(self):
        cents = E.concept_centroids(db_path=self.db)
        self.assertIn(1, cents)
        # Centroid should sit close to +x, not be cancelled by the weak -x post.
        self.assertGreater(float(cents[1][0]), 0.9,
                           "weak edge leaked into the centroid")

    def test_counter_example_also_excluded(self):
        conn = sqlite3.connect(self.db)
        conn.execute("UPDATE post_concepts SET role='counter-example' WHERE post_id=12")
        conn.commit(); conn.close()
        cents = E.concept_centroids(db_path=self.db)
        self.assertGreater(float(cents[1][0]), 0.9,
                           "counter-example leaked into the centroid")

    def test_origin_is_load_bearing(self):
        conn = sqlite3.connect(self.db)
        conn.execute("UPDATE post_concepts SET role='origin' WHERE post_id=12")
        conn.commit(); conn.close()
        cents = E.concept_centroids(db_path=self.db)
        # origin counts, so now the -x post DOES pull the centroid down.
        self.assertLess(float(cents[1][0]), 0.9,
                        "'origin' should be treated as load-bearing")


class WeakNeverPrimary(unittest.TestCase):
    def setUp(self):
        self.db = _make_db()
        conn = sqlite3.connect(self.db)
        # Post 10 has a weak edge to concept 1 and an evidence edge to 2.
        # Concept 1 is a much better vector fit — but weak must not win.
        conn.execute("INSERT INTO concepts (id, name) VALUES (1, 'near')")
        conn.execute("INSERT INTO concepts (id, name) VALUES (2, 'far')")
        rows = [(10, _vec(1, 0)), (11, _vec(1, 0)), (12, _vec(1, 0)),
                (20, _vec(0, 1)), (21, _vec(0, 1))]
        for pid, vec in rows:
            conn.execute("INSERT INTO posts (id, summary) VALUES (?, 's')", (pid,))
            conn.execute(
                "INSERT INTO post_embeddings (post_id, model, dim, vector) VALUES (?,?,?,?)",
                (pid, E.DEFAULT_MODEL, 2, E._vector_to_blob(vec)))
        # concept 1: posts 11,12 evidence (so it has a centroid at +x)
        for pid in (11, 12):
            conn.execute("INSERT INTO post_concepts (post_id, concept_id, role) VALUES (?,1,'evidence')", (pid,))
        # concept 2: posts 20,21 evidence (centroid at +y)
        for pid in (20, 21):
            conn.execute("INSERT INTO post_concepts (post_id, concept_id, role) VALUES (?,2,'evidence')", (pid,))
        # post 10 (vector +x): weak on concept 1, evidence on concept 2
        conn.execute("INSERT INTO post_concepts (post_id, concept_id, role) VALUES (10,1,'weak')")
        conn.execute("INSERT INTO post_concepts (post_id, concept_id, role) VALUES (10,2,'evidence')")
        conn.commit(); conn.close()

    def test_primary_ignores_weak_even_when_better_fit(self):
        C.assign_primaries(db_path=self.db, with_lock=False)
        conn = sqlite3.connect(self.db)
        prim = conn.execute(
            "SELECT concept_id FROM post_concepts WHERE post_id=10 AND is_primary=1"
        ).fetchone()
        conn.close()
        self.assertIsNotNone(prim, "post 10 should have a primary home")
        self.assertEqual(prim[0], 2,
                         "weak edge became primary despite being non-canonical")

    def test_weak_only_post_gets_no_primary(self):
        conn = sqlite3.connect(self.db)
        conn.execute("DELETE FROM post_concepts WHERE post_id=10 AND concept_id=2")
        conn.commit(); conn.close()
        C.assign_primaries(db_path=self.db, with_lock=False)
        conn = sqlite3.connect(self.db)
        prim = conn.execute(
            "SELECT COUNT(*) FROM post_concepts WHERE post_id=10 AND is_primary=1"
        ).fetchone()[0]
        conn.close()
        self.assertEqual(prim, 0,
                         "a post whose only edge is weak must stay unhomed")


class ConceptualPreferenceOnHomeAxis(unittest.TestCase):
    """A url:/mention: grouping may be evidence, but shouldn't be a *home*."""

    def setUp(self):
        self.db = _make_db()
        conn = sqlite3.connect(self.db)
        conn.execute("INSERT INTO concepts (id, name) VALUES (1, 'a real theme')")
        conn.execute("INSERT INTO concepts (id, name) VALUES (2, 'url:https://example.com/repo')")
        for pid, vec in [(10, _vec(1, 0)), (11, _vec(1, 0)), (12, _vec(1, 0)),
                         (20, _vec(1, 0)), (21, _vec(1, 0))]:
            conn.execute("INSERT INTO posts (id, summary) VALUES (?, 's')", (pid,))
            conn.execute(
                "INSERT INTO post_embeddings (post_id, model, dim, vector) VALUES (?,?,?,?)",
                (pid, E.DEFAULT_MODEL, 2, E._vector_to_blob(vec)))
        for pid in (11, 12):
            conn.execute("INSERT INTO post_concepts (post_id, concept_id, role) VALUES (?,1,'evidence')", (pid,))
        for pid in (20, 21):
            conn.execute("INSERT INTO post_concepts (post_id, concept_id, role) VALUES (?,2,'evidence')", (pid,))
        # post 10 sits on both a real theme and a url: grouping, as evidence.
        conn.execute("INSERT INTO post_concepts (post_id, concept_id, role) VALUES (10,1,'evidence')")
        conn.execute("INSERT INTO post_concepts (post_id, concept_id, role) VALUES (10,2,'evidence')")
        conn.commit(); conn.close()

    def test_conceptual_concept_wins_the_home(self):
        C.assign_primaries(db_path=self.db, with_lock=False)
        conn = sqlite3.connect(self.db)
        prim = conn.execute(
            "SELECT concept_id FROM post_concepts WHERE post_id=10 AND is_primary=1"
        ).fetchone()[0]
        conn.close()
        self.assertEqual(prim, 1, "url: grouping should not win the home axis")

    def test_non_conceptual_still_homes_when_nothing_else(self):
        """Preference, not prohibition — better a url: home than none at all."""
        conn = sqlite3.connect(self.db)
        conn.execute("DELETE FROM post_concepts WHERE post_id=10 AND concept_id=1")
        conn.commit(); conn.close()
        C.assign_primaries(db_path=self.db, with_lock=False)
        conn = sqlite3.connect(self.db)
        prim = conn.execute(
            "SELECT concept_id FROM post_concepts WHERE post_id=10 AND is_primary=1"
        ).fetchone()
        conn.close()
        self.assertIsNotNone(prim)
        self.assertEqual(prim[0], 2)


class WeakDoesNotHideFromOrphanClustering(unittest.TestCase):
    def test_weak_only_post_is_still_an_orphan(self):
        db = _make_db()
        conn = sqlite3.connect(db)
        conn.execute("INSERT INTO concepts (id, name) VALUES (1, 'c')")
        # The pass bails out below 50 embeddings ("too few for a stable corpus
        # mean"), so pad with filler posts that all carry evidence edges and
        # are therefore NOT orphans. Without this the assertion passes/fails
        # for the wrong reason.
        for pid in range(100, 160):
            conn.execute(
                "INSERT INTO posts (id, summary, enrichment_status) VALUES (?,'s','ok')",
                (pid,))
            conn.execute(
                "INSERT INTO post_embeddings (post_id, model, dim, vector) VALUES (?,?,?,?)",
                (pid, E.DEFAULT_MODEL, 2, E._vector_to_blob(_vec(1, 0.01 * pid))))
            conn.execute(
                "INSERT INTO post_concepts (post_id, concept_id, role) VALUES (?,1,'evidence')",
                (pid,))
        for pid in (10, 11):
            conn.execute(
                "INSERT INTO posts (id, summary, enrichment_status) VALUES (?,'s','ok')",
                (pid,))
            conn.execute(
                "INSERT INTO post_embeddings (post_id, model, dim, vector) VALUES (?,?,?,?)",
                (pid, E.DEFAULT_MODEL, 2, E._vector_to_blob(_vec(1, 0))))
        conn.execute("INSERT INTO post_concepts (post_id, concept_id, role) VALUES (10,1,'weak')")
        conn.execute("INSERT INTO post_concepts (post_id, concept_id, role) VALUES (11,1,'evidence')")
        conn.commit(); conn.close()
        # min_size high enough that nothing is created; we only care which
        # posts the pass *considered*.
        stats = C.discover_orphan_clusters(db_path=db, dry_run=True,
                                          with_lock=False, min_size=99)
        self.assertNotIn("error", stats, f"pass bailed out: {stats.get('error')}")
        self.assertEqual(stats["orphans_examined"], 1,
                         "weak-only post should still be examined as an orphan; "
                         f"got {stats['orphans_examined']}")


class AutoCurateAttachesInsteadOfDismissing(unittest.TestCase):
    def setUp(self):
        self.db = _make_db()
        conn = sqlite3.connect(self.db)
        conn.execute("INSERT INTO concepts (id, name) VALUES (1, 'real concept')")
        conn.execute("INSERT INTO concepts (id, name) VALUES (2, 'url:https://example.com/x')")
        conn.execute("INSERT INTO concepts (id, name) VALUES (3, 'mention:@someone')")
        for pid in (10, 11, 12):
            conn.execute("INSERT INTO posts (id, summary) VALUES (?, 's')", (pid,))
        # below-floor semantic match on a conceptual concept
        conn.execute("""INSERT INTO concept_observations
            (id, post_id, concept_id, raw_score, score_kind, source, status)
            VALUES (1, 10, 1, 0.70, 'cosine-similarity', 'semantic', 'pending')""")
        # above-floor semantic match
        conn.execute("""INSERT INTO concept_observations
            (id, post_id, concept_id, raw_score, score_kind, source, status)
            VALUES (2, 11, 1, 0.91, 'cosine-similarity', 'semantic', 'pending')""")
        # mechanical url: grouping
        conn.execute("""INSERT INTO concept_observations
            (id, post_id, concept_id, raw_score, score_kind, source, status)
            VALUES (3, 12, 2, 1.0, 'mechanical-overlap', 'mechanical', 'pending')""")
        # mechanical mention: grouping
        conn.execute("""INSERT INTO concept_observations
            (id, post_id, concept_id, raw_score, score_kind, source, status)
            VALUES (4, 12, 3, 1.0, 'mechanical-overlap', 'mechanical', 'pending')""")
        conn.commit(); conn.close()

    def test_nothing_is_dismissed(self):
        r = C.auto_curate(db_path=self.db, with_lock=False)
        self.assertEqual(r["dismissed"], 0, "auto_curate should no longer dismiss")
        self.assertEqual(r["dismissed_lowscore"], 0)
        conn = sqlite3.connect(self.db)
        n = conn.execute(
            "SELECT COUNT(*) FROM concept_observations WHERE status='dismissed'"
        ).fetchone()[0]
        conn.close()
        self.assertEqual(n, 0)

    def test_roles_assigned_by_evidence_quality(self):
        C.auto_curate(db_path=self.db, with_lock=False)
        conn = sqlite3.connect(self.db)
        roles = dict(conn.execute(
            "SELECT concept_id || ':' || post_id, role FROM post_concepts"))
        conn.close()
        self.assertEqual(roles.get("1:10"), C.ROLE_WEAK, "recall band should be weak")
        self.assertEqual(roles.get("1:11"), C.ROLE_EVIDENCE, "above-floor should be evidence")
        self.assertEqual(roles.get("2:12"), C.ROLE_EVIDENCE, "shared url should be evidence")
        self.assertEqual(roles.get("3:12"), C.ROLE_WEAK, "shared mention should be weak")

    def test_idempotent(self):
        first = C.auto_curate(db_path=self.db, with_lock=False)
        second = C.auto_curate(db_path=self.db, with_lock=False)
        self.assertGreater(first["promoted"], 0)
        self.assertEqual(second["promoted"], 0, "second run should be a no-op")

    def test_existing_evidence_edge_not_downgraded(self):
        conn = sqlite3.connect(self.db)
        conn.execute(
            "INSERT INTO post_concepts (post_id, concept_id, role) VALUES (10,1,'evidence')")
        conn.commit(); conn.close()
        C.auto_curate(db_path=self.db, with_lock=False)
        conn = sqlite3.connect(self.db)
        role = conn.execute(
            "SELECT role FROM post_concepts WHERE post_id=10 AND concept_id=1"
        ).fetchone()[0]
        conn.close()
        self.assertEqual(role, "evidence",
                         "a pre-existing evidence edge must never be downgraded to weak")


class WeakCapIsPerPostTotal(unittest.TestCase):
    """The weak-band cap must bound a post's TOTAL weak edges, not per-run.

    A per-run cap looks fine for one run and then quietly converges on
    everything-attached-to-everything, because `already_attached` excludes what
    a post already has and hands it the next-best N every time.
    """

    def test_second_run_does_not_add_more_weak_edges(self):
        db = _make_db()
        conn = sqlite3.connect(db)
        # 6 concepts, each with 2 evidence members, all near +x so every
        # concept is a plausible sub-floor match for the probe post.
        for cid in range(1, 7):
            conn.execute("INSERT INTO concepts (id, name) VALUES (?, ?)",
                         (cid, f'theme {cid}'))
            for k in range(2):
                pid = 1000 + cid * 10 + k
                conn.execute("INSERT INTO posts (id, summary) VALUES (?, 's')", (pid,))
                conn.execute(
                    "INSERT INTO post_embeddings (post_id, model, dim, vector) VALUES (?,?,?,?)",
                    (pid, E.DEFAULT_MODEL, 2, E._vector_to_blob(_vec(1, 0.02 * cid))))
                conn.execute(
                    "INSERT INTO post_concepts (post_id, concept_id, role) VALUES (?,?,'evidence')",
                    (pid, cid))
        # Probe post, unattached, sits near all of them.
        conn.execute("INSERT INTO posts (id, summary) VALUES (500, 's')")
        conn.execute(
            "INSERT INTO post_embeddings (post_id, model, dim, vector) VALUES (500,?,2,?)",
            (E.DEFAULT_MODEL, E._vector_to_blob(_vec(1, 0.07))))
        conn.commit(); conn.close()

        def weak_count():
            c = sqlite3.connect(db)
            n = c.execute(
                "SELECT COUNT(*) FROM post_concepts WHERE post_id=500 AND role='weak'"
            ).fetchone()[0]
            c.close()
            return n

        # threshold well below the floor so everything lands in the weak band
        for _ in range(3):
            C.discover_semantic_neighbors(db_path=db, threshold=0.10,
                                          max_weak_per_post=3, with_lock=False)
            C.auto_curate(db_path=db, with_lock=False)
        self.assertLessEqual(weak_count(), 3,
                             f"weak edges exceeded the per-post cap across runs: "
                             f"{weak_count()}")


class ReviveGuards(unittest.TestCase):
    def test_revive_refuses_without_role_filters(self):
        """The revive script must abort if centroids aren't role-filtered."""
        from db import revive_dismissed as R
        self.assertEqual(R._check_guards(), [],
                         "guards should pass on the current tree")

    def test_revive_skips_retired_concepts(self):
        from db import revive_dismissed as R
        db = _make_db()
        conn = sqlite3.connect(db)
        conn.execute("INSERT INTO concepts (id, name, status) VALUES (1,'live','active')")
        conn.execute("INSERT INTO concepts (id, name, status) VALUES (2,'gone','archived')")
        for pid in (10, 11):
            conn.execute("INSERT INTO posts (id, summary) VALUES (?, 's')", (pid,))
        conn.execute("""INSERT INTO concept_observations
            (id, post_id, concept_id, raw_score, score_kind, source, status, notes)
            VALUES (1, 10, 1, 0.7, 'cosine-similarity', 'semantic', 'dismissed', 'x')""")
        conn.execute("""INSERT INTO concept_observations
            (id, post_id, concept_id, raw_score, score_kind, source, status, notes)
            VALUES (2, 11, 2, 0.7, 'cosine-similarity', 'semantic', 'dismissed', 'x')""")
        conn.commit(); conn.close()
        r = R.revive(db_path=db, dry_run=True, progress=False)
        self.assertEqual(r["weak"], 1)
        self.assertEqual(r["skipped_retired_concept"], 1,
                         "observations on archived concepts must not be revived")


if __name__ == "__main__":
    unittest.main(verbosity=2)
