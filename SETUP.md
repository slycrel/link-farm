# Setup / Portability — running the AI Links automation on a new machine

The repo carries the whole *brain* — all `db/*.py` code, the SQLite DB (source of
truth), the docs, and the skills. What it can't carry are the machine- and
account-level *reflexes*: secrets, connectors, the scheduled triggers, and the
Python deps. This is the checklist to reconstitute those on a fresh box or from
the Claude CLI.

## 1. Clone + Python deps

```bash
git clone https://github.com/slycrel/link-farm.git
cd link-farm
pip install --break-system-packages -r requirements.txt
python3 db/migrate_runner.py     # idempotent; brings schema to current
```

`requirements.txt` pins `fastembed` (embedding backbone, ~133 MB incl. the
bge-small-en-v1.5 ONNX model on first use), `numpy`, and `sqlite-vec`
(declared for the future; not yet imported). Without fastembed+numpy the
pipeline still does subject-flags + mechanical discovery + rebuild, but the
**semantic / auto-curate / primary layer silently no-ops**.

### Making fastembed *permanent* (so it survives across runs)

The Cowork sandbox is ephemeral — a `pip install` in one run may not be present
in the next, which is why `db/ensure_deps.py` re-checks and installs at the top
of every pipeline run. If you're on a **normal machine / CLI** and want it
installed once and for good, do any of:

- **User install (simplest):** `pip install --user fastembed numpy` — persists
  for your user across sessions (no sandbox reset). On externally-managed
  Pythons add `--break-system-packages`.
- **A virtualenv (cleanest, recommended for a real box):**
  ```bash
  python3 -m venv ~/.venvs/link-farm
  ~/.venvs/link-farm/bin/pip install -r requirements.txt
  # run the tools with that interpreter:
  ~/.venvs/link-farm/bin/python3 db/pipeline.py
  ```
- **pipx / conda** if you prefer — any environment that persists works; the code
  only needs `import fastembed, numpy` to succeed.

`db/ensure_deps.py` stays harmless in all of these: it's a `find_spec` check
first, so when the deps are already importable it does nothing. To verify:
`python3 db/ensure_deps.py --check` (exits 0 when present).

## 2. GitHub token (secret — not in the repo)

The push helpers read `.claude/github_token` (a GitHub token for the `slycrel`
account). It's gitignored on purpose. On a new box, create it:

```bash
mkdir -p .claude
printf '%s' 'YOUR_GITHUB_TOKEN' > .claude/github_token
chmod 600 .claude/github_token
```

## 3. Connectors (account-level, connected in the app)

- **Microsoft 365** — Outlook search for the daily sync + URL backfill (sender
  `slycrel@gmail.com`).
- **Claude in Chrome** — post scraping/enrichment.

Connect both in the Cowork/Claude app on the new machine. They are not, and
cannot be, in the repo.

## 4. Scheduled tasks (the automation triggers)

The live tasks live in the Cowork app store at
`~/Documents/Claude/Scheduled/<taskId>/SKILL.md` — **not** in the repo. Versioned
snapshots are kept here under `scheduled/`:

| snapshot | cron | state | recreate? |
|---|---|---|---|
| `scheduled/ai-links-sync.SKILL.md` | `0 9 * * 1-5` (weekdays 09:00) | **enabled** — the one that matters | yes |
| `scheduled/ai-links-backfill.SKILL.md` | `30 10 * * 1` (Mondays 10:30) | **disabled**, campaign complete | no — leave it off |

To recreate the sync, ask Claude to "create a scheduled task" with the cron above
and the prompt body from the snapshot (or paste the file). Keep the live copy and
the `scheduled/` snapshot in sync when either changes — they drifted for weeks
once, and the stale copy silently suppressed two topic tags.

**Don't schedule the backfill on a fresh box.** It existed to drain a backlog of
`partial`/`failed` posts so the latent-discovery gate could open. The gate opened
2026-08-14, the queue emptied 2026-08-26, and it has been dormant since (last run
2026-08-03). Recreate it *disabled*, or not at all, and wake it only if a real
queue reappears:

```bash
python3 -c "from db.enrich import gate_ratio, status_breakdown; print(gate_ratio(), status_breakdown())"
# gate above 0.05, or more than a couple dozen partial/failed -> re-enable it
```

Some older text in `CLAUDE.md` described it as a weekday task (`30 10 * * 1-5`).
That was the drain cadence and is no longer accurate.

## 5. Skills

- `ai-links-catchup.SKILL.md` and `ai-links-curate.SKILL.md` are in the repo
  root. Install them as skills in the app (or invoke their logic directly).
- `ai-links-catchup/SKILL.md` is the same catch-up skill in directory form —
  which is what the app installs. The flat `.SKILL.md` is the readable copy.
- `skills/` carries anything else that travels with the repo (e.g. `skills/ste`).

## 6. What actually gets pushed

`db/repo_sync.py` holds `PUSH_SPEC`, the single definition of which paths are
mirrored to the remote. It is glob-based on purpose: a new file in `db/`,
`scheduled/` or `skills/` propagates without anyone editing a list. `.claude/`
(the token), `__pycache__/`, `*.bak`, `db/_*` scratch and the SQLite `-wal`/`-shm`
sidecars are excluded.

Before trusting a push, check for drift:

```bash
git clone https://github.com/slycrel/link-farm.git /tmp/lf-check
python3 -m db.repo_sync --check . /tmp/lf-check   # exits 1 if anything is missing
python3 -m db.repo_sync --list .                  # what would be copied
```

This exists because the sync task previously pushed a hardcoded filename list,
so `SETUP.md`, `README.md`, `scheduled/`, `skills/` and `db/test_*.py` never
reached the remote except by hand.

## Sanity check

```bash
python3 db/ensure_deps.py                      # {'ok': True, ...}
python3 db/migrate_runner.py                   # schema current (expect "Nothing to do")
python3 -m db.stats                            # corpus + concept graph summary
python3 -m db.concepts stats                   # concept graph detail
python3 -m db.repo_sync --check . /tmp/lf-check # nothing missing from the remote
python3 -m unittest discover -s db -p 'test_*.py' -v
python3 -c "from db.pipeline import post_enrichment_pipeline as p; print(p()['summary'])"
```

If the pipeline line shows `embed:` and `semantic:` with real counts (not a
skip), the semantic layer is live and portable. `db/test_roles.py` is the one
worth caring about — it guards the four places where the canonical/weak edge
distinction is enforced, and every one of them is a *silent* failure if it
regresses.

`python3 -m db.stats --markdown` regenerates the Collection Stats block in
`CLAUDE.md`; paste over it rather than hand-editing, so the numbers and the
as-of date stay honest together.
