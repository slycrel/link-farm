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

- `scheduled/ai-links-sync.SKILL.md` — weekdays 09:00, cron `0 9 * * 1-5`
- `scheduled/ai-links-backfill.SKILL.md` — Mondays 10:30, cron `30 10 * * 1`

To recreate them, ask Claude to "create a scheduled task" with the cron above and
the prompt body from the matching snapshot (or paste the file). Keep the live
copy and the `scheduled/` snapshot in sync when either changes.

## 5. Skills

- `ai-links-catchup.SKILL.md` and `ai-links-curate.SKILL.md` are in the repo.
  Install them as skills in the app (or invoke their logic directly).

## Sanity check

```bash
python3 db/ensure_deps.py                      # {'ok': True, ...}
python3 -m db.concepts stats                   # concept graph summary
python3 -c "from db.pipeline import post_enrichment_pipeline as p; print(p()['summary'])"
```

If the last line shows `embed:` and `semantic:` with real counts (not a skip),
the semantic layer is live and portable.
