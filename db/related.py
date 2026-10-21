"""'See also' neighbours from post embeddings.

Ranking uses MEAN-CENTERED cosine. Raw cosine in this corpus is dominated by a
shared 'agent-ish' component (pairwise mean ~0.61), so raw neighbours are
topically vague and lean on author names (every Karpathy post neighbours every
other Karpathy post); centered neighbours are the actually-related posts (e.g.
the litellm attack post's top neighbours are the axios npm compromise and the
CA-key compromise). Derived data — never stored; computed at rebuild time for
the HTML viewer and on demand by `python3 -m db.search --similar`.
"""
from pathlib import Path
import sqlite3

DEFAULT_DB = Path(__file__).parent / "ai_links.db"
RELATED_FLOOR = 0.35   # centered cosine; ~2.2 neighbours/post on average, noise-free
RELATED_K = 5


def _load(db_path):
    import numpy as np
    try:
        from .embeddings import _blob_to_vector, DEFAULT_MODEL
    except ImportError:
        from embeddings import _blob_to_vector, DEFAULT_MODEL
    conn = sqlite3.connect(str(db_path))
    rows = conn.execute("SELECT post_id, vector FROM post_embeddings WHERE model=?", (DEFAULT_MODEL,)).fetchall()
    conn.close()
    ids = [r[0] for r in rows]
    V = np.array([_blob_to_vector(r[1]) for r in rows], dtype=np.float32)
    V /= np.linalg.norm(V, axis=1, keepdims=True)
    V -= V.mean(0)
    V /= np.linalg.norm(V, axis=1, keepdims=True)
    return np, ids, V


def related_for_all(db_path=DEFAULT_DB, k=RELATED_K, floor=RELATED_FLOOR) -> dict:
    """{post_id: [(neighbour_id, score), ...]} best first, only scores >= floor."""
    try:
        np, ids, V = _load(db_path)
    except Exception:
        return {}
    S = V @ V.T
    np.fill_diagonal(S, -1)
    out = {}
    for i, pid in enumerate(ids):
        order = np.argsort(-S[i])[:k]
        pairs = [(ids[j], float(S[i][j])) for j in order if S[i][j] >= floor]
        if pairs:
            out[pid] = pairs
    return out


def related_to(post_id: int, db_path=DEFAULT_DB, k=10, floor=0.0):
    """Neighbours of one post with no floor by default (for interactive use)."""
    np, ids, V = _load(db_path)
    if post_id not in ids:
        return []
    i = ids.index(post_id)
    s = V @ V[i]
    s[i] = -1
    return [(ids[j], float(s[j])) for j in np.argsort(-s)[:k] if s[j] >= floor]
