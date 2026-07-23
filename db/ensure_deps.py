#!/usr/bin/env python3
"""
Ensure the semantic-stack Python deps are importable before the pipeline runs.

Why this exists: the sync / catch-up / backfill skills run in a sandbox that
does not persist installed packages between runs. Without a bootstrap, the
embedding → semantic-discovery → auto-file steps silently no-op whenever
`fastembed` happens to be absent (the pipeline catches the ImportError and
continues with mechanical + rebuild only). That means the concept automation
we rely on would run or not run depending on ambient environment state.

Persistence (Jeremy, July 2026): the plain `pip install` re-downloaded
fastembed + onnxruntime + the ONNX model (~130MB+) on *every* sandbox run,
because the sandbox wipes site-packages between runs. The repo/cowork folder,
however, *is* persistent. So we install into a repo-local target dir
(`.deps/`) and point fastembed/HuggingFace at a repo-local model cache
(`.model-cache/`). Both survive across sandbox runs, so after the first run
`ensure()` is a no-op and no download happens.

IMPORTANT — these caches hold Linux-native binaries (onnxruntime). They are
for the ephemeral Cowork sandbox, NOT for a Mac / local CLI. On a real machine
use a venv or `pip --user` per SETUP.md; there `ensure()` still works but has
nothing to do because the deps are already importable. Both dirs are gitignored
and the sync push copies named files only, so they never leave the machine.

Call `ensure()` at the top of any automation that needs embeddings. It is:
  - Fast when deps are already present — a `find_spec` check, no pip call.
  - Idempotent — safe to call every run.
  - Quiet — installs with -q; returns a dict describing what it did.

CLI:  python3 db/ensure_deps.py        # ensure, print result
      python3 db/ensure_deps.py --check # report only, exit 1 if missing
"""

import importlib.util
import os
import subprocess
import sys
from pathlib import Path

# Deps that gate the semantic layer. sqlite-vec is intentionally NOT here —
# it's declared in requirements.txt for the future but not yet imported by any
# code path, so its absence must not trigger an install or a failure.
REQUIRED = ["fastembed", "numpy"]

REPO_ROOT = Path(__file__).resolve().parent.parent
REQUIREMENTS = REPO_ROOT / "requirements.txt"

# Persistent, repo-local caches (survive the ephemeral sandbox — see module
# docstring). DEPS_DIR is a `pip install --target` prefix; MODEL_CACHE_DIR is
# where fastembed/HF store the downloaded ONNX model.
DEPS_DIR = REPO_ROOT / ".deps"
MODEL_CACHE_DIR = REPO_ROOT / ".model-cache"

# Wire the caches in at import time — BEFORE any find_spec check or model load:
#   * DEPS_DIR on sys.path so a cached `--target` install is importable.
#   * FASTEMBED_CACHE_PATH / HF_HOME so the model downloads to (and is read
#     from) the persistent cache. setdefault: never clobber an env the host
#     has already set on purpose.
if str(DEPS_DIR) not in sys.path:
    sys.path.insert(0, str(DEPS_DIR))
os.environ.setdefault("FASTEMBED_CACHE_PATH", str(MODEL_CACHE_DIR))
os.environ.setdefault("HF_HOME", str(MODEL_CACHE_DIR))


def missing() -> list[str]:
    """Return the subset of REQUIRED modules that aren't importable (this
    already accounts for DEPS_DIR, which was put on sys.path at import)."""
    return [m for m in REQUIRED if importlib.util.find_spec(m) is None]


def ensure(quiet: bool = True) -> dict:
    """Install any missing REQUIRED deps into the persistent DEPS_DIR.
    Returns {installed, already, ok, deps_dir, model_cache}."""
    need = missing()
    if not need:
        return {
            "installed": [],
            "already": list(REQUIRED),
            "ok": True,
            "deps_dir": str(DEPS_DIR),
            "model_cache": str(MODEL_CACHE_DIR),
        }

    DEPS_DIR.mkdir(parents=True, exist_ok=True)
    MODEL_CACHE_DIR.mkdir(parents=True, exist_ok=True)

    # Install into the persistent target dir. No --upgrade: the cowork mount
    # denies unlink, and once .deps is populated `missing()` short-circuits
    # this whole branch, so we never need to overwrite an existing install.
    cmd = [sys.executable, "-m", "pip", "install", "--target", str(DEPS_DIR)]
    if quiet:
        cmd.append("-q")
    # Prefer the pinned manifest; fall back to bare module names if it's absent.
    cmd += ["-r", str(REQUIREMENTS)] if REQUIREMENTS.exists() else need
    subprocess.run(cmd, check=True)

    importlib.invalidate_caches()  # make the fresh --target install visible now
    still = missing()
    return {
        "installed": [m for m in need if m not in still],
        "already": [m for m in REQUIRED if m not in need],
        "ok": not still,
        "still_missing": still,
        "deps_dir": str(DEPS_DIR),
        "model_cache": str(MODEL_CACHE_DIR),
    }


if __name__ == "__main__":
    if "--check" in sys.argv:
        m = missing()
        print("missing:", m or "none")
        sys.exit(1 if m else 0)
    print(ensure())
