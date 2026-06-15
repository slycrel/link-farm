#!/usr/bin/env python3
"""
Semantic embeddings for the ai-links corpus.

Step 6 of CURATION_DESIGN.md. This module:

    * Picks an embedding model and dim (default BAAI/bge-small-en-v1.5, 384d).
    * Computes a content_hash for each post so re-enrichment can invalidate
      stale embeddings without re-embedding the whole corpus.
    * Embeds eligible posts (status in {ok, legacy-ok}) — never `partial` or
      `dead` (per design, embedding empty / placeholder content produces junk
      vectors that pollute the nearest-neighbor graph).
    * Stores vectors in the `post_embeddings` table from migration 006.
    * Provides nearest-neighbor + concept-centroid matching helpers used by
      `db/concepts.py` for the semantic discovery pass.

Why not sqlite-vec for queries (yet): the corpus is ~627 posts, well within
numpy-NN territory (< 1ms per query). The schema is forward-compatible —
when corpus crosses ~10k we can wire sqlite-vec virtual tables on top of
`post_embeddings` without changing the storage shape.

Dependencies (one-time install on the user's machine; sandbox already has them):
    pip install --break-system-packages fastembed sqlite-vec numpy

Usage:
    python3 -m db.embeddings status        # how much of the corpus is embedded?
    python3 -m db.embeddings embed         # embed eligible posts (skip already-embedded with matching content_hash)
    python3 -m db.embeddings neighbors POST_ID [--k 10]
    python3 -m db.embeddings centroids     # compute concept centroids and report
"""

import sqlite3
import hashlib
import argparse
import io
from pathlib import Path
from contextlib import contextmanager
from typing import Optional, Iterable

import numpy as np

try:
    from .lock import writer_lock
except ImportError:
    import sys as _sys
    _sys.path.insert(0, str(Path(__file__).parent))
    from lock import writer_lock

SCRIPT_DIR = Path(__file__).parent
DEFAULT_DB = SCRIPT_DIR / "ai_links.db"

# Default model. Local, lightweight (~133MB), 384-dim, ONNX-runtime backed.
# Held under `(post_id, model)` PK so we can hold multiple model versions
# simultaneously during a swap.
DEFAULT_MODEL = "BAAI/bge-small-en-v1.5"
DEFAULT_DIM = 384

# Statuses we embed. Excludes 'partial' (empty content), 'dead' (deleted),
# 'failed' (transient) — embedding junk just pollutes nearest-neighbor.
EMBEDDABLE_STATUSES = ("ok", "legacy-ok")

# Cache the model loaded once per process — embedding 600 posts otherwise
# pays the ONNX load cost twice.
_MODEL_CACHE: dict = {}


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


# ---- Content hash + embedding text -----------------------------------

def _compose_embedding_text(post: dict, segments: list[dict]) -> str:
    """Build the text we feed to the embedding model.

    Concatenates the summary and the captured thread segments. For
    legacy-ok posts where `post_thread_segments` is empty (segments only
    landed for posts re-enriched at ENRICHMENT_VERSION 1+), falls back to
    `posts.content` which holds the joined-blob form. Cap at 4000 chars
    so we don't blow context — bge-small handles 512 tokens (~2000 chars
    English) but truncation is more honest than chunking for a small post.
    """
    parts: list[str] = []
    if post.get("summary"):
        parts.append(post["summary"])
    if segments:
        for seg in segments:
            txt = (seg.get("text") or "").strip()
            if not txt:
                continue
            label = seg.get("type") or "op"
            parts.append(f"[{label}] {txt}")
    elif post.get("content"):
        # Legacy path — no structured segments yet, use the joined blob.
        parts.append(post["content"])
    blob = "\n\n".join(parts).strip()
    return blob[:4000]


def compute_content_hash(post: dict, segments: list[dict]) -> str:
    """SHA-256 hex digest of the text actually fed to the embedding model.
    Changing summary or segments → changes hash → invalidates embedding."""
    text = _compose_embedding_text(post, segments)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


# ---- Model loading + embedding -----------------------------------------

def _get_model(model_name: str = DEFAULT_MODEL):
    """Load (or return cached) embedding model."""
    if model_name in _MODEL_CACHE:
        return _MODEL_CACHE[model_name]
    from fastembed import TextEmbedding
    model = TextEmbedding(model_name=model_name)
    _MODEL_CACHE[model_name] = model
    return model


def _embed_texts(texts: list[str], model_name: str = DEFAULT_MODEL) -> np.ndarray:
    """Embed a list of texts. Returns (N, dim) numpy float32 array."""
    if not texts:
        return np.zeros((0, DEFAULT_DIM), dtype=np.float32)
    model = _get_model(model_name)
    vectors = list(model.embed(texts))
    arr = np.array(vectors, dtype=np.float32)
    return arr


# ---- BLOB encoding (sqlite_vec-compatible little-endian float32) ------

def _vector_to_blob(vec: np.ndarray) -> bytes:
    """Serialize a 1-D float32 array to bytes."""
    return np.asarray(vec, dtype=np.float32).tobytes()


def _blob_to_vector(blob: bytes) -> np.ndarray:
    """Deserialize bytes to a 1-D float32 numpy array."""
    return np.frombuffer(blob, dtype=np.float32)


# ---- Status + queries --------------------------------------------------

def status_breakdown(db_path: Path = DEFAULT_DB, model: str = DEFAULT_MODEL) -> dict:
    """Counts of embeddable / embedded / stale posts."""
    with _connect(db_path) as conn:
        eligible = conn.execute(f"""
            SELECT COUNT(*) FROM posts
             WHERE enrichment_status IN ({','.join(['?']*len(EMBEDDABLE_STATUSES))})
        """, EMBEDDABLE_STATUSES).fetchone()[0]
        embedded = conn.execute(
            "SELECT COUNT(*) FROM post_embeddings WHERE model = ?", (model,)
        ).fetchone()[0]
        # Stale = embedded but content_hash doesn't match the current post text.
        stale = conn.execute("""
            SELECT COUNT(*) FROM post_embeddings pe
              JOIN posts p ON p.id = pe.post_id
             WHERE pe.model = ?
               AND p.enrichment_status IN ('ok', 'legacy-ok')
        """, (model,)).fetchone()[0]
    return {
        "eligible": eligible,
        "embedded": embedded,
        "missing": eligible - embedded,
        "model": model,
    }


def _fetch_segments(conn, post_id: int) -> list[dict]:
    rows = conn.execute(
        "SELECT type, handle, text, url FROM post_thread_segments "
        "WHERE post_id = ? ORDER BY ordinal", (post_id,),
    ).fetchall()
    return [dict(r) for r in rows]


def _fetch_existing_hash(conn, post_id: int, model: str) -> Optional[str]:
    row = conn.execute(
        "SELECT content_hash FROM post_embeddings WHERE post_id=? AND model=?",
        (post_id, model),
    ).fetchone()
    return row[0] if row else None


# ---- Embed corpus ------------------------------------------------------

def embed_corpus(model_name: str = DEFAULT_MODEL,
                  batch_size: int = 32,
                  force: bool = False,
                  db_path: Path = DEFAULT_DB,
                  with_lock: bool = True,
                  progress: bool = True) -> dict:
    """Embed all eligible posts whose embedding is missing or stale.

    `force=True` re-embeds everything regardless of hash. Use after a model
    swap or a content-format change.
    """
    stats = {"considered": 0, "skipped_unchanged": 0, "embedded": 0, "errors": 0}

    with _connect(db_path) as conn:
        rows = conn.execute(f"""
            SELECT id, summary, content, enrichment_status, enrichment_version
              FROM posts
             WHERE enrichment_status IN ({','.join(['?']*len(EMBEDDABLE_STATUSES))})
             ORDER BY date DESC, id DESC
        """, EMBEDDABLE_STATUSES).fetchall()
        candidates = []
        for row in rows:
            post = dict(row)
            segments = _fetch_segments(conn, post["id"])
            text = _compose_embedding_text(post, segments)
            if not text:
                continue
            content_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
            existing = _fetch_existing_hash(conn, post["id"], model_name)
            stats["considered"] += 1
            if not force and existing == content_hash:
                stats["skipped_unchanged"] += 1
                continue
            candidates.append({
                "post_id": post["id"],
                "text": text,
                "content_hash": content_hash,
            })

    if not candidates:
        return stats

    if progress:
        print(f"Embedding {len(candidates)} posts (model={model_name}, dim={DEFAULT_DIM}, batch={batch_size})...")

    # Embed in batches, write under one lock acquisition.
    with (writer_lock(timeout=120) if with_lock else _nullctx()):
        for start in range(0, len(candidates), batch_size):
            batch = candidates[start:start + batch_size]
            texts = [c["text"] for c in batch]
            try:
                vectors = _embed_texts(texts, model_name=model_name)
            except Exception as e:
                stats["errors"] += len(batch)
                if progress:
                    print(f"  batch {start}-{start+len(batch)} failed: {e}")
                continue
            with _connect(db_path) as conn:
                for c, vec in zip(batch, vectors):
                    if vec.shape[0] != DEFAULT_DIM:
                        stats["errors"] += 1
                        continue
                    conn.execute("""
                        INSERT INTO post_embeddings
                            (post_id, model, dim, content_hash, vector, embedded_at)
                        VALUES (?, ?, ?, ?, ?, datetime('now'))
                        ON CONFLICT(post_id, model) DO UPDATE SET
                            content_hash = excluded.content_hash,
                            vector       = excluded.vector,
                            embedded_at  = excluded.embedded_at
                    """, (c["post_id"], model_name, DEFAULT_DIM,
                          c["content_hash"], _vector_to_blob(vec)))
                    stats["embedded"] += 1
                conn.commit()
            if progress:
                done = start + len(batch)
                print(f"  ...{done}/{len(candidates)} ({100*done//len(candidates)}%)")

    return stats


@contextmanager
def _nullctx():
    yield


# ---- Nearest neighbor + concept centroids -----------------------------

def _load_all_vectors(model: str, db_path: Path) -> tuple[list[int], np.ndarray]:
    """Load all embeddings for the given model into a (N, dim) matrix."""
    with _connect(db_path) as conn:
        rows = conn.execute(
            "SELECT post_id, vector FROM post_embeddings WHERE model = ? ORDER BY post_id",
            (model,),
        ).fetchall()
    ids = [r["post_id"] for r in rows]
    if not rows:
        return ids, np.zeros((0, DEFAULT_DIM), dtype=np.float32)
    matrix = np.stack([_blob_to_vector(r["vector"]) for r in rows], axis=0)
    return ids, matrix


def _normalize(matrix: np.ndarray) -> np.ndarray:
    """Row-normalize so dot product = cosine similarity."""
    norms = np.linalg.norm(matrix, axis=1, keepdims=True)
    norms = np.where(norms == 0, 1.0, norms)
    return matrix / norms


def find_neighbors(post_id: int, k: int = 10,
                    model: str = DEFAULT_MODEL,
                    db_path: Path = DEFAULT_DB) -> list[dict]:
    """Return the top-k nearest posts by cosine similarity, excluding the
    query post itself. Each item: {post_id, similarity, author, date,
    summary}."""
    with _connect(db_path) as conn:
        row = conn.execute(
            "SELECT vector FROM post_embeddings WHERE post_id=? AND model=?",
            (post_id, model),
        ).fetchone()
        if not row:
            return []
        query_vec = _blob_to_vector(row["vector"])

    ids, matrix = _load_all_vectors(model, db_path)
    if matrix.shape[0] == 0:
        return []
    normed = _normalize(matrix)
    q = query_vec / (np.linalg.norm(query_vec) or 1.0)
    sims = normed @ q  # (N,) cosine similarities

    # Build index → post_id map, drop the query post, take top-k.
    pairs = list(zip(ids, sims.tolist()))
    pairs = [(pid, s) for pid, s in pairs if pid != post_id]
    pairs.sort(key=lambda x: x[1], reverse=True)
    top = pairs[:k]

    if not top:
        return []
    top_ids = [pid for pid, _ in top]
    placeholders = ",".join("?" * len(top_ids))
    with _connect(db_path) as conn:
        post_rows = conn.execute(
            f"SELECT id, author, date, url, "
            f"       SUBSTR(COALESCE(summary,''),1,200) AS summary "
            f"FROM posts WHERE id IN ({placeholders})", top_ids,
        ).fetchall()
    by_id = {r["id"]: dict(r) for r in post_rows}
    out = []
    for pid, sim in top:
        info = by_id.get(pid, {})
        out.append({
            "post_id": pid,
            "similarity": float(sim),
            "author": info.get("author") or "?",
            "date": info.get("date") or "",
            "url": info.get("url") or "",
            "summary": info.get("summary") or "",
        })
    return out


def concept_centroids(model: str = DEFAULT_MODEL,
                       db_path: Path = DEFAULT_DB) -> dict[int, np.ndarray]:
    """Average embedding of the canonical posts attached to each active
    concept. Used to score a new post's fit to existing concepts."""
    with _connect(db_path) as conn:
        rows = conn.execute("""
            SELECT pc.concept_id, pe.vector
              FROM post_concepts pc
              JOIN post_embeddings pe ON pe.post_id = pc.post_id
              JOIN concepts c ON c.id = pc.concept_id
             WHERE pe.model = ? AND c.status = 'active'
        """, (model,)).fetchall()
    by_concept: dict[int, list[np.ndarray]] = {}
    for r in rows:
        cid = r["concept_id"]
        by_concept.setdefault(cid, []).append(_blob_to_vector(r["vector"]))
    centroids = {}
    for cid, vecs in by_concept.items():
        m = np.stack(vecs, axis=0)
        centroid = m.mean(axis=0)
        centroids[cid] = centroid / (np.linalg.norm(centroid) or 1.0)
    return centroids


def score_post_against_concepts(post_id: int,
                                  model: str = DEFAULT_MODEL,
                                  db_path: Path = DEFAULT_DB) -> list[tuple[int, float]]:
    """Cosine sim of a post against every active concept's centroid.
    Returns sorted descending list of (concept_id, score)."""
    with _connect(db_path) as conn:
        row = conn.execute(
            "SELECT vector FROM post_embeddings WHERE post_id=? AND model=?",
            (post_id, model),
        ).fetchone()
        if not row:
            return []
        q = _blob_to_vector(row["vector"])
        q = q / (np.linalg.norm(q) or 1.0)

    centroids = concept_centroids(model=model, db_path=db_path)
    scored = [(cid, float(np.dot(q, c))) for cid, c in centroids.items()]
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored


# ---- CLI --------------------------------------------------------------

def _cmd_status(args):
    s = status_breakdown(args.db, args.model)
    print(f"Embeddings (model={s['model']}, dim={DEFAULT_DIM}):")
    print(f"  eligible posts (ok/legacy-ok):  {s['eligible']}")
    print(f"  embedded:                       {s['embedded']}")
    print(f"  missing:                        {s['missing']}")


def _cmd_embed(args):
    stats = embed_corpus(
        model_name=args.model, batch_size=args.batch_size,
        force=args.force, db_path=args.db, progress=True,
    )
    print()
    print("Done.")
    for k, v in stats.items():
        print(f"  {k:25s} {v}")


def _cmd_neighbors(args):
    rows = find_neighbors(args.post_id, k=args.k, model=args.model, db_path=args.db)
    if not rows:
        print(f"No embedding for post {args.post_id} (or empty corpus).")
        return
    print(f"Top {len(rows)} neighbors for post {args.post_id}:")
    for r in rows:
        print(f"  {r['similarity']:.3f}  {r['post_id']}  {r['author'][:25]:25s}  {r['date']}")
        if r["summary"]:
            print(f"         {r['summary'][:140]}")


def _cmd_centroids(args):
    centroids = concept_centroids(model=args.model, db_path=args.db)
    print(f"{len(centroids)} concept centroids computed (model={args.model})")
    with _connect(args.db) as conn:
        for cid, c in list(centroids.items())[:20]:
            name_row = conn.execute(
                "SELECT name FROM concepts WHERE id = ?", (cid,)
            ).fetchone()
            name = (name_row[0] if name_row else "?")[:60]
            print(f"  #{cid:<4} {name}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", type=Path, default=DEFAULT_DB)
    parser.add_argument("--model", type=str, default=DEFAULT_MODEL)
    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("status").set_defaults(func=_cmd_status)

    p = sub.add_parser("embed")
    p.add_argument("--batch-size", type=int, default=32)
    p.add_argument("--force", action="store_true",
                    help="Re-embed everything regardless of hash")
    p.set_defaults(func=_cmd_embed)

    p = sub.add_parser("neighbors")
    p.add_argument("post_id", type=int)
    p.add_argument("--k", type=int, default=10)
    p.set_defaults(func=_cmd_neighbors)

    sub.add_parser("centroids").set_defaults(func=_cmd_centroids)

    args = parser.parse_args()
    if not getattr(args, "func", None):
        parser.print_help()
        return
    args.func(args)


if __name__ == "__main__":
    main()
