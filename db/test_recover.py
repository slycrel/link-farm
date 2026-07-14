#!/usr/bin/env python3
"""Regression tests for the url-less-orphan guard + recovery path.

Run: python3 -m db.test_recover   (from the cowork root)
"""
import sqlite3
import tempfile
import unittest
from pathlib import Path

from db.migrate import generate_id, url_to_hash_id, is_missing_url
from db import recover


class TestMissingUrlGuard(unittest.TestCase):
    def test_placeholder_detected(self):
        for bad in ["[not found]", "", None, "  N/A ", "none", "NULL"]:
            self.assertTrue(is_missing_url(bad), bad)

    def test_real_url_not_missing(self):
        self.assertFalse(is_missing_url("https://x.com/a/status/1"))

    def test_generate_id_refuses_placeholder(self):
        # This is the exact bug: sha256("[not found]") used to be minted as an id.
        for bad in ["[not found]", "", "n/a"]:
            with self.assertRaises(ValueError):
                generate_id(bad)
            with self.assertRaises(ValueError):
                url_to_hash_id(bad)

    def test_status_id_still_works(self):
        self.assertEqual(
            generate_id("https://x.com/dickson_tsai/status/2029235808235078095?s=43"),
            2029235808235078095,
        )


class TestRekey(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
        self.db = Path(self.tmp.name)
        con = sqlite3.connect(self.db)
        con.executescript(
            """
            CREATE TABLE posts (id INTEGER PRIMARY KEY, url TEXT, updated_at TEXT);
            CREATE TABLE post_topics (post_id INTEGER, topic TEXT);
            CREATE TABLE post_audiences (post_id INTEGER, audience TEXT);
            CREATE TABLE post_relations (post_id_a INTEGER, post_id_b INTEGER, relation TEXT);
            CREATE VIRTUAL TABLE posts_fts USING fts5(url, content=posts, content_rowid=id);
            """
        )
        con.commit()
        con.close()

    def tearDown(self):
        self.db.unlink(missing_ok=True)

    def _con(self):
        return sqlite3.connect(self.db)

    def test_rekey_migrates_fk_rows(self):
        old = url_to_hash_id("[placeholder-was-here]") if False else 262554158365753
        con = self._con()
        con.execute("INSERT INTO posts (id, url) VALUES (?, '[not found]')", (old,))
        con.execute("INSERT INTO post_topics VALUES (?, 'claude-code')", (old,))
        con.execute("INSERT INTO post_audiences VALUES (?, 'me')", (old,))
        con.commit()

        con.execute("BEGIN")
        new_id = recover.rekey_post(
            con, old, "https://x.com/dickson_tsai/status/2029235808235078095")
        con.commit()

        self.assertEqual(new_id, 2029235808235078095)
        # post row moved
        self.assertIsNone(con.execute("SELECT 1 FROM posts WHERE id=?", (old,)).fetchone())
        row = con.execute("SELECT url FROM posts WHERE id=?", (new_id,)).fetchone()
        self.assertEqual(row[0], "https://x.com/dickson_tsai/status/2029235808235078095")
        # fk rows followed
        self.assertEqual(
            con.execute("SELECT topic FROM post_topics WHERE post_id=?", (new_id,)).fetchone()[0],
            "claude-code")
        self.assertEqual(
            con.execute("SELECT COUNT(*) FROM post_topics WHERE post_id=?", (old,)).fetchone()[0],
            0)
        con.close()

    def test_rekey_refuses_missing_url(self):
        con = self._con()
        con.execute("INSERT INTO posts (id, url) VALUES (1, '[not found]')")
        con.commit()
        con.execute("BEGIN")
        with self.assertRaises(ValueError):
            recover.rekey_post(con, 1, "[not found]")
        con.close()

    def test_rekey_refuses_merge_clash(self):
        con = self._con()
        con.execute("INSERT INTO posts (id, url) VALUES (?, '[not found]')", (999,))
        con.execute("INSERT INTO posts (id, url) VALUES (2029235808235078095, 'x')")
        con.commit()
        con.execute("BEGIN")
        with self.assertRaises(ValueError):
            recover.rekey_post(
                con, 999, "https://x.com/dickson_tsai/status/2029235808235078095")
        con.close()

    def test_candidate_query_catches_not_found(self):
        con = self._con()
        con.execute("INSERT INTO posts (id, url) VALUES (1, '[not found]')")
        con.execute("INSERT INTO posts (id, url) VALUES (2, '')")
        con.execute("INSERT INTO posts (id, url) VALUES (3, NULL)")
        con.execute("INSERT INTO posts (id, url) VALUES (4, 'https://x.com/a/status/9')")
        con.commit()
        con.close()
        # candidate query needs enrichment_status col; add it for the shape
        con = self._con()
        con.execute("ALTER TABLE posts ADD COLUMN enrichment_status TEXT")
        con.execute("ALTER TABLE posts ADD COLUMN author TEXT")
        con.execute("ALTER TABLE posts ADD COLUMN handle TEXT")
        con.execute("ALTER TABLE posts ADD COLUMN subject TEXT")
        con.execute("ALTER TABLE posts ADD COLUMN date TEXT")
        con.commit()
        con.close()
        cands = recover.url_backfill_candidates(self.db)
        ids = {c["id"] for c in cands}
        self.assertEqual(ids, {1, 2, 3})


if __name__ == "__main__":
    unittest.main(verbosity=2)
