#!/usr/bin/env python3
"""Abstain-aware filing — a classifier for primary homes, not a model.

Borrowed wholesale from the Contrastive Language Model contract (Akshay
Pachaar's explainer, post 2103483160382386234, 2026-09-25), minus the trained
head. CLM's actual contribution is not speed, it is *shape*:

    the application supplies a finite candidate list;
    the scorer may not invent an option outside it;
    it returns a typed id **or abstains**.

`assign_primaries()` already does the first two. What it cannot do is the third
— it always names a winner — and on this corpus that turns out to be the whole
problem. Measured 2026-09-25 over 442 multi-candidate posts:

    geometry              median top1-top2 margin    margin < 0.02
    raw (what we ship)            0.0014                 95.9%
    mean-centered                 0.0222                 47.5%
    centered + bounded            0.0227                 46.7%

**86% of raw multi-candidate filing decisions land inside a 0.01 margin.** At
that spread the ranking is not measuring fit, it is measuring the shared "AI
stuff" direction that dominates every pairwise cosine on this corpus (pairwise
mean 0.61). The homes are coin flips with a confident-looking number attached.
This is the same pathology recorded for the lauren/pstack post, whose 20
candidates spanned 0.0095 end to end and whose correct home ranked last.

Two corrections, and the second is the one that is easy to get wrong:

1. **Mean-center before scoring.** Subtracting the corpus mean removes the
   shared direction; the median margin improves ~16x. This mirrors what
   `discover_orphan_clusters()` already does, and the 2026-09-15 dry run that
   moved centroid-pair similarity from median 0.826 to 0.029.

2. **Bound the candidate set to conceptual concepts.** Centering *alone*
   actively degrades filing: tiny `url:`/`mention:` groupings have 2-3 members,
   so their centered centroid is sharp and idiosyncratic and they start winning
   homes. Measured on the same run, homes landing on a mechanical grouping went
   raw 18 -> centered 25, but centered+bounded **4**. Naive centering is not a
   safe drop-in. Bounding is preference, not prohibition — a post whose *only*
   canonical edges are mechanical still homes there rather than nowhere, which
   matches `ConceptualPreferenceOnHomeAxis` in db/test_roles.py.

**Abstention is the point, and abstaining is not the same as un-homing.** A
thin margin means "these candidates are indistinguishable to the geometry", not
"this post belongs nowhere". So an abstention keeps whatever primary the post
already has (stability — never churn a home on a coin flip) and records the
post for human review. Only a post with no home at all and no confident
candidate ends up in the queue as genuinely unfiled.

Nothing here dismisses an observation, ever, and nothing writes unless the
caller passes dry_run=False. Consistent with the no-discard policy: automation
attaches and labels, humans discard.

CLI:
    python3 -m db.filing report            # distribution + what would change
    python3 -m db.filing review [--limit]  # the abstain queue, for a human
    python3 -m db.filing apply --confirm   # write confident decisions only
"""
from __future__ import annotations

import argparse
import sqlite3
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, Optional, Sequence

import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_DB = SCRIPT_DIR / "ai_links.db"

from db.concepts import (CANONICAL_ROLES, PRIMARY_PIN_MARKER,  # noqa: E402
                         _is_conceptual_name)
from db.lock import writer_lock  # noqa: E402

# --- calibration ------------------------------------------------------------
# Every threshold below is a *centered* cosine and is NOT comparable to
# SEMANTIC_CENTROID_THRESHOLD / AUTO_PROMOTE_MIN_COSINE, which are raw. Same
# trap the orphan-clustering and provisional-exemplar constants carry.

# Abstain when the top two candidates are closer than this. Swept against the
# live corpus 2026-09-25 (577 scored posts):
#
#     margin   confident   abstain   homes it would change
#      0.01        357        220            10
#      0.02        293        284             1
#      0.03        253        324             0
#      0.05        208        369             0
#
# 0.03 is the default because it is the point where the classifier stops
# *disagreeing* with the existing homes and becomes purely additive: it proposes
# no reassignments at all, it only separates the decisions it can stand behind
# from the ones it cannot. That makes it safe to run unattended and impossible
# to blame for churn.
#
# The single change proposed at 0.02 was also a good argument for 0.03: it moved
# an Anthropic agent-memory whitepaper summary from "vector / hybrid databases as
# agent-memory infrastructure" to "local model serving on consumer GPUs" on a
# margin of 0.0229. The old home was plainly better. Just above the floor is
# still the noise floor.
#
# Lower it to 0.02/0.01 only if you want an auto-filer rather than a review
# instrument, and read the proposed diff before confirming.
ABSTAIN_MARGIN = 0.03

# A candidate has to clear this in absolute terms too, or every candidate being
# equally bad still produces a "winner" whenever one is marginally less bad.
ABSTAIN_MIN_TOP = 0.05

# Prefer conceptual homes over url:/mention: groupings. Preference, not
# prohibition: a post with only mechanical edges still homes on one.
PREFER_CONCEPTUAL = True


@dataclass
class Decision:
    """One filing decision over a bounded candidate set."""
    post_id: int
    candidates: list[tuple[float, int]] = field(default_factory=list)
    chosen: Optional[int] = None
    current: Optional[int] = None
    top_score: Optional[float] = None
    margin: Optional[float] = None
    abstained: bool = False
    reason: str = ""
    pinned: bool = False

    @property
    def changes(self) -> bool:
        return (not self.abstained and self.chosen is not None
                and self.chosen != self.current)

    @property
    def unfiled(self) -> bool:
        """Abstained *and* has no existing home — genuinely needs a human."""
        return self.abstained and self.current is None


def _unit(v: np.ndarray) -> np.ndarray:
    n = float(np.linalg.norm(v))
    return v / n if n else v


def _load(db_path: Path):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row

    vecs = {r["post_id"]: np.frombuffer(r["vector"], dtype=np.float32)
            for r in conn.execute("SELECT post_id, vector FROM post_embeddings")}
    if not vecs:
        raise RuntimeError("no embeddings — run the embed step first")

    # Mean-center against the whole embedded corpus, then re-normalise. The
    # all-but-the-top trick: the corpus mean *is* the "AI stuff" direction.
    mu = np.mean(np.stack(list(vecs.values())), axis=0)
    cvecs = {k: _unit(v - mu) for k, v in vecs.items()}

    names = {r["id"]: r["name"] for r in conn.execute(
        "SELECT id, name FROM concepts WHERE status='active'")}

    placeholders = ",".join("?" * len(CANONICAL_ROLES))
    edges: dict[int, list[int]] = {}
    for r in conn.execute(f"""
            SELECT pc.post_id, pc.concept_id
              FROM post_concepts pc
              JOIN concepts co ON co.id = pc.concept_id
             WHERE pc.role IN ({placeholders}) AND co.status = 'active'
        """, tuple(CANONICAL_ROLES)):
        edges.setdefault(r["post_id"], []).append(r["concept_id"])

    members: dict[int, list[int]] = {}
    for pid, cids in edges.items():
        for cid in cids:
            members.setdefault(cid, []).append(pid)

    current = {r["post_id"]: r["concept_id"] for r in conn.execute(
        "SELECT post_id, concept_id FROM post_concepts WHERE is_primary=1")}

    pins = {r["post_id"] for r in conn.execute(
        "SELECT post_id FROM post_concepts WHERE COALESCE(notes,'') LIKE ?",
        (f"%{PRIMARY_PIN_MARKER}%",))}

    conn.close()
    return cvecs, names, edges, members, current, pins


def _candidate_ids(post_id: int, edges, names) -> list[int]:
    """The finite action list. Never invent an option outside a post's own
    canonical edges — that is the contract borrowed from CLM."""
    cids = edges.get(post_id, [])
    if not PREFER_CONCEPTUAL:
        return cids
    conceptual = [c for c in cids if _is_conceptual_name(names.get(c))]
    return conceptual if conceptual else cids


class _Scorer:
    """Loaded corpus state plus the one scoring routine everything shares.

    `score(pid)` is the real decision. `score(pid, rng=...)` resamples each
    candidate concept's membership with replacement before averaging, which is
    what `stability()` uses — a bootstrap over *who is in the concept*, since
    that is the quantity a filing decision is actually sensitive to.
    """

    def __init__(self, db_path: Path = DEFAULT_DB):
        (self.vecs, self.names, self.edges,
         self.members, self.current, self.pins) = _load(db_path)

    def candidates(self, pid: int) -> list[int]:
        return _candidate_ids(pid, self.edges, self.names)

    def score(self, pid: int, rng=None) -> list[tuple[float, int]]:
        out: list[tuple[float, int]] = []
        for cid in self.candidates(pid):
            # Leave-one-out: a post must not vote for its own home.
            peers = [q for q in self.members.get(cid, [])
                     if q != pid and q in self.vecs]
            if not peers:
                continue
            if rng is not None:
                peers = list(rng.choice(peers, size=len(peers), replace=True))
            centroid = _unit(np.mean([self.vecs[q] for q in peers], axis=0))
            out.append((float(self.vecs[pid] @ centroid), cid))
        out.sort(reverse=True)
        return out


def classify(db_path: Path = DEFAULT_DB,
             post_ids: Optional[Iterable[int]] = None,
             abstain_margin: float = ABSTAIN_MARGIN,
             abstain_min_top: float = ABSTAIN_MIN_TOP,
             respect_pins: bool = True,
             _scorer: "Optional[_Scorer]" = None) -> list[Decision]:
    """Score every post against its bounded candidate set; abstain when thin.

    `_scorer` lets a caller reuse loaded corpus state across many calls (the
    calibration sweep does this); it is otherwise an implementation detail.
    """
    sc = _scorer if _scorer is not None else _Scorer(db_path)
    targets = list(post_ids) if post_ids is not None else list(sc.edges)

    out: list[Decision] = []
    for pid in targets:
        d = Decision(post_id=pid, current=sc.current.get(pid))
        if respect_pins and pid in sc.pins:
            d.pinned = True
            d.abstained = True
            d.reason = "hand-pinned primary; never recomputed"
            out.append(d)
            continue
        if pid not in sc.vecs:
            d.abstained = True
            d.reason = "no embedding"
            out.append(d)
            continue

        scored = sc.score(pid)
        d.candidates = scored

        if not scored:
            d.abstained = True
            d.reason = "no scoreable candidate (every candidate is this post alone)"
        elif scored[0][0] < abstain_min_top:
            d.abstained = True
            d.top_score = scored[0][0]
            d.margin = (scored[0][0] - scored[1][0]) if len(scored) > 1 else None
            d.reason = (f"best candidate only {scored[0][0]:.4f} "
                        f"(floor {abstain_min_top})")
        elif len(scored) == 1:
            d.chosen, d.top_score = scored[0][1], scored[0][0]
            d.reason = "single candidate"
        else:
            margin = scored[0][0] - scored[1][0]
            d.top_score, d.margin = scored[0][0], margin
            if margin < abstain_margin:
                d.abstained = True
                d.reason = (f"margin {margin:.4f} < {abstain_margin} — "
                            f"top candidates indistinguishable")
            else:
                d.chosen = scored[0][1]
                d.reason = f"margin {margin:.4f}"
        out.append(d)
    return out


def report(db_path: Path = DEFAULT_DB, **kw) -> dict:
    """Summarise what abstain-aware filing would do. Writes nothing."""
    ds = classify(db_path=db_path, **kw)
    multi = [d for d in ds if len(d.candidates) > 1]
    margins = np.array([d.margin for d in multi if d.margin is not None])
    confident = [d for d in ds if not d.abstained]
    return {
        "posts": len(ds),
        "confident": len(confident),
        "abstained": sum(1 for d in ds if d.abstained),
        "pinned": sum(1 for d in ds if d.pinned),
        "would_change": sum(1 for d in ds if d.changes),
        "unfiled": sum(1 for d in ds if d.unfiled),
        "median_margin": float(np.median(margins)) if margins.size else None,
        "decisions": ds,
    }


# --- stability: the label-free eval ----------------------------------------
# The obvious eval — score the classifier against the existing primary homes —
# is invalid on this corpus and it is worth being explicit about why. Of 577
# homes, 139 are single-candidate (forced, so they carry no information about
# discrimination) and 380 of the remaining 442 were decided on a sub-0.01 raw
# margin. That leaves ~62 homes that represent a defensible decision. An
# accuracy number measured against the rest would *rise* as the classifier got
# better at reproducing coin flips.
#
# So: measure stability instead, which needs no labels. Resample each candidate
# concept's membership with replacement and ask whether the same home wins. A
# decision that does not survive resampling was never a decision — the centroid
# it depended on was an artifact of which posts happened to be attached.
#
# Measured 2026-09-25, 15 resamples per post:
#
#     centered margin     n     home survives
#         < 0.01         131        29.4%
#       0.01 - 0.03      119        44.2%
#       0.03 - 0.08       95        70.8%
#         > 0.08          92        97.8%
#
# Monotonic, which is the result that justifies the whole margin-based design:
# margin is measuring something real, and it can be checked without ground
# truth. Note the 0.03-0.08 band is only ~71% stable, so the default threshold
# buys "usually reproducible", not "settled".

STABILITY_RESAMPLES = 15
STABILITY_SEED = 20260925


def stability(db_path: Path = DEFAULT_DB,
              post_ids: Optional[Iterable[int]] = None,
              resamples: int = STABILITY_RESAMPLES,
              seed: int = STABILITY_SEED,
              _scorer: "Optional[_Scorer]" = None) -> dict[int, float]:
    """Fraction of bootstrap resamples that reproduce each post's chosen home.

    Seeded, so a calibration run is reproducible — a threshold derived from a
    number that moves every invocation is not a calibration.
    """
    sc = _scorer if _scorer is not None else _Scorer(db_path)
    rng = np.random.default_rng(seed)
    targets = list(post_ids) if post_ids is not None else list(sc.edges)

    out: dict[int, float] = {}
    for pid in targets:
        if pid not in sc.vecs:
            continue
        base = sc.score(pid)
        if not base:
            continue
        if len(base) == 1:
            out[pid] = 1.0          # nothing to be unstable between
            continue
        hits = sum(1 for _ in range(resamples)
                   if (b := sc.score(pid, rng=rng)) and b[0][1] == base[0][1])
        out[pid] = hits / resamples
    return out


def calibrate(db_path: Path = DEFAULT_DB,
              target_stability: float = 0.80,
              bands: Sequence[float] = (0.0, 0.01, 0.02, 0.03, 0.05, 0.08, 0.12),
              resamples: int = STABILITY_RESAMPLES,
              seed: int = STABILITY_SEED) -> dict:
    """Derive ABSTAIN_MARGIN from measured stability rather than from a sweep.

    Returns the per-band stability curve and the lowest margin threshold whose
    *retained* decisions clear `target_stability` on average. That is a real
    calibration: pick the confidence you want, read off the threshold.
    """
    sc = _Scorer(db_path)
    contested = [p for p in sc.edges if p in sc.vecs and len(sc.candidates(p)) > 1]
    stab = stability(db_path, post_ids=contested, resamples=resamples,
                     seed=seed, _scorer=sc)

    margins: dict[int, float] = {}
    for pid in contested:
        s = sc.score(pid)
        if len(s) > 1:
            margins[pid] = s[0][0] - s[1][0]

    curve = []
    for lo, hi in zip(bands, list(bands[1:]) + [float("inf")]):
        ids = [p for p, m in margins.items() if lo <= m < hi and p in stab]
        if ids:
            curve.append({"lo": lo, "hi": hi, "n": len(ids),
                          "stability": float(np.mean([stab[p] for p in ids]))})

    recommended = None
    for t in bands:
        kept = [p for p, m in margins.items() if m >= t and p in stab]
        if kept and float(np.mean([stab[p] for p in kept])) >= target_stability:
            recommended = t
            break

    kept = [p for p, m in margins.items()
            if recommended is not None and m >= recommended and p in stab]
    return {
        "contested": len(contested),
        "curve": curve,
        "target_stability": target_stability,
        "recommended_margin": recommended,
        "current_margin": ABSTAIN_MARGIN,
        "retained_at_recommended": len(kept),
        "stability_at_recommended": (
            float(np.mean([stab[p] for p in kept])) if kept else None),
        "resamples": resamples,
        "seed": seed,
    }


def apply(db_path: Path = DEFAULT_DB, dry_run: bool = True,
          with_lock: bool = True, **kw) -> dict:
    """Write only the confident decisions. Abstentions leave the graph alone.

    An abstention is deliberately a *no-op*, not an un-homing: a thin margin
    means the geometry cannot tell the candidates apart, which is no reason to
    strip a home a previous run or a human already established.
    """
    res = report(db_path=db_path, **kw)
    changes = [d for d in res["decisions"] if d.changes]
    res["applied"] = 0
    if dry_run or not changes:
        res["dry_run"] = True
        return res

    lock = writer_lock() if with_lock else _nullctx()
    with lock:
        conn = sqlite3.connect(db_path)
        for d in changes:
            conn.execute("UPDATE post_concepts SET is_primary=0 WHERE post_id=?",
                         (d.post_id,))
            conn.execute("""UPDATE post_concepts SET is_primary=1
                             WHERE post_id=? AND concept_id=?""",
                         (d.post_id, d.chosen))
        conn.commit()
        conn.close()
    res["applied"] = len(changes)
    res["dry_run"] = False
    return res


class _nullctx:
    def __enter__(self): return self
    def __exit__(self, *a): return False


def main(argv: Optional[Sequence[str]] = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("command", choices=["report", "review", "apply", "calibrate"])
    ap.add_argument("--db", type=Path, default=DEFAULT_DB)
    ap.add_argument("--limit", type=int, default=25)
    ap.add_argument("--margin", type=float, default=ABSTAIN_MARGIN)
    ap.add_argument("--confirm", action="store_true",
                    help="actually write (apply only)")
    ap.add_argument("--target", type=float, default=0.80,
                    help="target bootstrap stability (calibrate only)")
    ap.add_argument("--resamples", type=int, default=STABILITY_RESAMPLES,
                    help="bootstrap resamples per post (calibrate only)")
    a = ap.parse_args(argv)

    conn = sqlite3.connect(a.db)
    names = {r[0]: r[1] for r in conn.execute("SELECT id, name FROM concepts")}

    if a.command == "calibrate":
        r = calibrate(db_path=a.db, target_stability=a.target,
                      resamples=a.resamples)
        print(f"contested posts   : {r['contested']}")
        print(f"resamples / seed  : {r['resamples']} / {r['seed']}")
        print(f"\n{'margin band':>14} {'n':>5} {'home survives resampling':>26}")
        for b in r["curve"]:
            hi = "inf" if b["hi"] == float("inf") else f"{b['hi']:.2f}"
            print(f"{b['lo']:>7.2f}-{hi:<6} {b['n']:>5} {b['stability']:>25.1%}")
        print(f"\ntarget stability  : {r['target_stability']:.0%}")
        if r["recommended_margin"] is None:
            print("recommended margin: none of the swept thresholds reach the "
                  "target — the geometry cannot support that confidence here")
        else:
            print(f"recommended margin: {r['recommended_margin']:.2f}  "
                  f"(currently {r['current_margin']:.2f})")
            print(f"  retains {r['retained_at_recommended']} contested decisions "
                  f"at {r['stability_at_recommended']:.1%} mean stability")
        conn.close()
        return 0

    if a.command == "apply":
        r = apply(db_path=a.db, dry_run=not a.confirm, abstain_margin=a.margin)
        print(f"{'APPLIED' if not r['dry_run'] else 'DRY RUN'}: "
              f"{r['would_change']} home(s) would change, "
              f"{r['abstained']} abstained, {r['unfiled']} unfiled")
        if r["dry_run"]:
            print("  (pass --confirm to write)")
        return 0

    r = report(db_path=a.db, abstain_margin=a.margin)
    print(f"posts scored     : {r['posts']}")
    print(f"confident        : {r['confident']}")
    print(f"abstained        : {r['abstained']}  (pinned {r['pinned']})")
    print(f"  of which unfiled (abstained, no existing home): {r['unfiled']}")
    print(f"would change home: {r['would_change']}")
    if r["median_margin"] is not None:
        print(f"median margin    : {r['median_margin']:.4f} (centered cosine)")

    if a.command == "review":
        q = [d for d in r["decisions"] if d.abstained and not d.pinned]
        q.sort(key=lambda d: (d.current is not None, -(d.margin or 0)))
        print(f"\n--- abstain queue ({len(q)}), unfiled first ---")
        for d in q[:a.limit]:
            row = conn.execute(
                "SELECT date, author, substr(summary,1,64) FROM posts WHERE id=?",
                (d.post_id,)).fetchone()
            head = f"{row[0]} {row[1][:18]:<18}" if row else str(d.post_id)
            cur = names.get(d.current, "—") if d.current else "NO HOME"
            print(f"\n  {head} | now: {cur[:44]}")
            print(f"     {d.reason}")
            for s, cid in d.candidates[:3]:
                print(f"       {s:+.4f}  {names.get(cid,'?')[:56]}")
    conn.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
