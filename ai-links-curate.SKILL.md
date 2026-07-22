---
name: ai-links-curate
description: "Chat-mediated curation surface for Jeremy's AI Links Collection concept graph. Use whenever Jeremy says 'curate links', 'curate concepts', 'merge concepts', 'rename concept', 'split concept', 'review pending', 'show me pending observations', 'set the primary for', 'clean up the concept graph', or wants to act on the discovery output. Even a bare 'curate' or 'review concepts' in the AI-links context should trigger this."
---

# AI Links Curation Layer

You operate the curation surface for Jeremy's AI Links Collection concept graph (Layer 2 of `CURATION_DESIGN.md`). This skill is the **write path** for the concept layer: parse Jeremy's natural-language commands and route them to the helpers in `db/concepts.py`.

Read `CLAUDE.md` for project background and `CURATION_DESIGN.md` for the architecture. The rule that never bends: **the candidate/canonical split is sacred.** Discovery writes to `concept_observations` (immutable history + provenance); curation promotes observations into `post_concepts` (canonical truth). Go through the helpers — never hand-write those tables. (The one sanctioned exception is a *split*, which re-homes canonical edges in bulk; see that section.)

## What changed (July 2026) — read this first

Two revisions reshaped what curation is *for*:

1. **Semantic triage is automated.** The pipeline's `auto_curate()` auto-files conceptual semantic matches ≥ `AUTO_PROMOTE_MIN_COSINE` (0.82) as **secondary** tags and dismisses the sub-floor band every run, so **`pending` stays ~0 in steady state.** You will rarely be promoting routine semantic matches by hand. The human queue is now for **structural decisions**: merges, renames, splits, naming discovered `url:`/`mention:` concepts, and pinning primaries.
2. **Primary vs secondary.** Membership is many-to-many (overlap is fine), but exactly one edge per post is its **primary home** (`post_concepts.is_primary=1`, one-per-post enforced by index). `assign_primaries()` derives the primary as the best-fit concept by leave-one-out centroid cosine; split-review counts **primary** homes, not total edges. So don't panic at a concept with a large *total* edge count — check its primary-home count (that's its real size).

## Setup at the start of every run

```python
import subprocess, pathlib, glob, sys
candidates = sorted(glob.glob('/sessions/*/mnt/cowork'))
cowork = next((c for c in candidates if (pathlib.Path(c) / 'CLAUDE.md').exists()), candidates[0] if candidates else None)
assert cowork, 'Cowork folder not found'
sys.path.insert(0, cowork)  # so `import db.concepts` resolves

subprocess.run(['python3', f'{cowork}/db/ensure_deps.py'], check=False)   # embeddings need fastembed/numpy
subprocess.run(['python3', f'{cowork}/db/migrate_runner.py'], check=True) # idempotent
```

Use `cowork` for every later path.

## Mental model

- **Observation** (`concept_observations`) — one discovery event: "post X is evidence for concept Y," with provenance (source/persona/model/run/score). Statuses: `pending` / `promoted` / `dismissed` / `superseded`.
- **Canonical edge** (`post_concepts`) — curated truth that post X belongs to concept Y. Carries `is_primary` (0/1) and a qualitative `role` (evidence / counter-example / tangential / origin — a *different* axis from primary/secondary).
- **Concept** (`concepts`) — a named thread. Source `curated` / `discovered` / `merged`; status `active` / `archived` / `merged-into`.
- **Primary home** — the single concept a post is filed under. Derived by `assign_primaries()`; pinnable by hand (see below).

## Commands Jeremy may say

### "Show me what needs attention" / "show pending"

```python
from db.concepts import filter_observations, split_candidates
pend = filter_observations(status='pending', limit=100)
print(f"{len(pend)} pending (expect near 0 — semantic triage is automated).")
for o in pend[:50]:
    print(f"  #{o['observation_id']}  {o['concept_name'][:38]:38s}  {o['source']}  {o.get('raw_score')}  ← {o['post_author']}")
# The genuinely actionable queue is structural:
print("Split-review candidates (by PRIMARY home count):")
for c in split_candidates():
    print(f"  #{c['id']} {c['name'][:44]}  home={c['post_count']}")
```

Anything still pending is usually a `mention:`/`url:` grouping or a per-person concept whose post isn't yet conceptually covered — decide whether it deserves a real conceptual home.

### "List active concepts"

```python
from db.concepts import list_active_concepts
for c in list_active_concepts():
    print(f"  #{c['id']:<4} {c['name'][:56]:56s} total={c['post_count']:>3} pending={c['pending_count']}")
```

Remember `post_count` here is *total* edges. For split decisions, use `split_candidates()` (primary homes) or the SQL in the split section.

### "Merge concepts 'A' into 'B'" / "merge 8 into 2"

```python
from db.concepts import find_concept_by_name, merge_concepts
# by name:
src = find_concept_by_name("SOUL.md as identity scaffold")
dst = find_concept_by_name("agent identity files (SOUL.md, CLAUDE.md, persona scaffolds)")
result = merge_concepts(src['id'], dst['id'])   # or merge_concepts(8, 2) by id
print(result)
```

Flatten-on-merge in one transaction; cycles rejected. **After a merge, re-derive primaries** (see "finishing a batch").

### "Rename concept 8 to '…'"

```python
from db.concepts import rename_concept
rename_concept(8, "loop engineering", description="optional new description")
```

Always rename discovered `url:…` / `mention:@…` concepts to a human-readable conceptual name when you keep them.

### "Split concept N" — the structural heavy-lift

Only split when a concept's **primary home** conflates genuinely distinct threads (like #29 did with skills / setup / config / teams) — *not* just because it's popular. Confirm the sub-concepts with Jeremy first. Prefer re-homing into **existing** concepts over minting new ones.

1. Inspect the members and cluster them (read `subject`/`summary`; keyword-histogram helps).
2. Create any new sub-concepts (`create_concept`). Reuse existing homes where they fit.
3. Re-home canonical edges in bulk, mirroring `merge_concepts`' edge move but scoped to a post set — this is the sanctioned direct-table exception:

```python
from db.concepts import create_concept, archive_concept, _now
from db.lock import writer_lock
import sqlite3
with writer_lock(timeout=90):
    conn = sqlite3.connect(f'{cowork}/db/ai_links.db'); conn.execute("BEGIN")
    def move(src, dest, post_ids):
        q = ",".join("?"*len(post_ids))
        conn.execute(f"""INSERT OR IGNORE INTO post_concepts
            (post_id,concept_id,role,promoted_from_observation_id,notes,promoted_at,is_primary)
            SELECT post_id,?,role,promoted_from_observation_id,notes,promoted_at,0
            FROM post_concepts WHERE concept_id=? AND post_id IN ({q})""", (dest,src,*post_ids))
        conn.execute(f"""UPDATE concept_observations SET concept_id=?
            WHERE concept_id=? AND status='promoted' AND post_id IN ({q})""", (dest,src,*post_ids))
        conn.execute(f"DELETE FROM post_concepts WHERE concept_id=? AND post_id IN ({q})", (src,*post_ids))
    # move(...) each cluster to its destination concept...
    # dismiss the source's stale pending, then archive it:
    conn.execute("UPDATE concept_observations SET status='dismissed' WHERE concept_id=? AND status='pending'", (N,))
    conn.execute("UPDATE concepts SET status='archived', updated_at=? WHERE id=?", (_now(), N))
    conn.commit(); conn.close()
```

Set moved edges `is_primary=0`; the primary re-derivation in "finishing a batch" assigns homes cleanly. Expect a one-time **convergence surge** on the next pipeline run (discovery re-fires against the new centroids, auto-files as secondary, settles to a trickle over 1–2 runs). That's normal — don't chase it with more splits.

### "Set / pin the primary for post P to concept C"

`assign_primaries()` derives primaries automatically, but Jeremy can override. Pin by adding the `[primary-pin]` marker to the edge's `notes` — `assign_primaries` respects pins and won't recompute that post.

```python
from db.concepts import PRIMARY_PIN_MARKER
from db.lock import writer_lock
import sqlite3
with writer_lock(timeout=60):
    conn = sqlite3.connect(f'{cowork}/db/ai_links.db'); conn.execute("BEGIN")
    conn.execute("UPDATE post_concepts SET is_primary=0 WHERE post_id=?", (P,))
    conn.execute("UPDATE post_concepts SET is_primary=1, notes=COALESCE(notes,'')||? WHERE post_id=? AND concept_id=?",
                 (' '+PRIMARY_PIN_MARKER, P, C))
    conn.commit(); conn.close()
```

### "Create a concept 'X' from posts P1, P2, P3"

```python
from db.concepts import create_concept, record_observation, promote_observation
from db.lock import writer_lock
with writer_lock(timeout=60):
    cid = create_concept("X", description="Jeremy's framing of X.", source='curated', with_lock=False)
    for pid in [P1, P2, P3]:
        oid = record_observation(post_id=pid, concept_id=cid, source='mechanical',
                                  score_kind='mechanical-overlap', raw_score=1.0,
                                  notes='curator seed', with_lock=False)
        if oid:
            promote_observation(oid, with_lock=False)   # lands as secondary; primary derived later
```

### "Archive concept 5" / "dismiss 4824, 4825"

```python
from db.concepts import archive_concept, bulk_dismiss
archive_concept(5)                                  # keeps edges, hides from active views
bulk_dismiss([4824, 4825], notes="off-topic")       # notes help future passes
```

### "Run discovery" / "show the gate" / "show stats"

```python
from db.concepts import run_all_mechanical_passes, discover_semantic_neighbors
run_all_mechanical_passes(); discover_semantic_neighbors()
from db.enrich import gate_ratio
ratio, breakdown = gate_ratio(); print(f"gate {ratio:.3f} ({'OPEN' if ratio<0.05 else 'CLOSED'}) {breakdown}")
subprocess.run(['python3', '-m', 'db.concepts', 'stats'], cwd=cowork, check=True)
```

## Finishing a batch — re-derive primaries, rebuild, push

Any structural change (merge / split / create / manual promote) shifts centroids and edge sets, so **re-derive primaries and rebuild**. The simplest correct move is to run the whole pipeline (it embeds, discovers, auto-curates, assigns primaries, rebuilds):

```python
from db.lock import writer_lock
from db.pipeline import post_enrichment_pipeline
with writer_lock(timeout=120):
    print(post_enrichment_pipeline(with_lock=False, progress=True)['summary'])
```

(If you only touched names/archives and want a lighter touch: `assign_primaries(with_lock=False)` then `rebuild(with_lock=False)` inside the lock.)

Then push (only if something changed):

```python
import subprocess, shutil, os, datetime, time, pathlib
token = (pathlib.Path(cowork)/'.claude/github_token').read_text().strip()
creds = pathlib.Path.home()/'.git-credentials'; creds.write_text(f'https://slycrel:{token}@github.com\n'); creds.chmod(0o600)
for k,v in [('credential.helper','store'),('user.name','Jeremy Stone'),('user.email','jstone@taxhawk.com')]:
    subprocess.run(['git','config','--global',k,v], check=True)
pd = f'/tmp/lf-curate-{int(time.time())}'
subprocess.run(['git','clone','https://github.com/slycrel/link-farm.git',pd], check=True)
subprocess.run(['git','config','--global','--add','safe.directory',pd], check=True)
for f in ['posts_final_v3.json','ai_links_collection_v3.html','ai_links_collection_v3.md','CLAUDE.md','CURATION_DESIGN.md','requirements.txt']:
    if os.path.exists(f'{cowork}/{f}'): shutil.copy(f'{cowork}/{f}', f'{pd}/{f}')
os.makedirs(f'{pd}/db', exist_ok=True)
for f in ['ai_links.db','migrate.py','migrate_runner.py','rebuild.py','enrich.py','lock.py','__init__.py','concepts.py','embeddings.py','pipeline.py','perspectives.py','subject_flags.py','recover.py','ensure_deps.py']:
    if os.path.exists(f'{cowork}/db/{f}'): shutil.copy(f'{cowork}/db/{f}', f'{pd}/db/{f}')
subprocess.run(['git','-C',pd,'add','-A'], check=True)
if subprocess.run(['git','-C',pd,'diff','--cached','--stat'],capture_output=True,text=True).stdout.strip():
    subprocess.run(['git','-C',pd,'commit','-m',f'Curate {datetime.date.today().isoformat()}'], check=True)
    subprocess.run(['git','-C',pd,'push','origin','main'], check=True); print('Pushed')
else:
    print('No changes to push')
```

## Reporting

- **Merge**: "Merged #X into #Y — N observations + K edges moved."
- **Split**: "Dissolved #N into A/B/C; re-homed K edges; archived #N. Convergence surge expected next run."
- **Primary**: "Pinned post P's primary to #C." / "Re-derived primaries: Δ changed."
- **End**: "Rebuilt (X posts, Y active concepts). Pending now Z. Pushed as commit ####."

## Constraints

- Go through `db/concepts.py` helpers; the only sanctioned direct-table write is the scoped edge-move in a *split*.
- Hold one `writer_lock()` per batch; pass `with_lock=False` to inner calls.
- **Don't reflexively split.** Split only when a *primary home* conflates distinct threads; a large *total* edge count on a broad-but-coherent concept is fine (overlap is intentional). Splitting a merely-popular concept just multiplies secondary edges.
- After any structural change, re-derive primaries + rebuild before reporting done.
- Merge cycles raise `ValueError` — surface clearly.
- Don't run discovery unprompted — the scheduled sync/backfill handle it; pending stays ~0 on its own.
