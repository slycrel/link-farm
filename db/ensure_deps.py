#!/usr/bin/env python3
"""
Ensure the semantic-stack Python deps are importable before the pipeline runs.

Why this exists: the sync / catch-up / backfill skills run in a sandbox that
does not persist installed packages between runs. Without a bootstrap, the
embedding → semantic-discovery → auto-file steps silently no-op whenever
`fastembed` happens to be absent (the pipeline catches the ImportError and
continues with mechanical + rebuild only). That means the concept automation
we rely on would run or not run depending on ambient environment state.

Call `ensure()` at the top of any automation that needs embeddings. It is:
  - Fast when deps are already present — a `find_spec` check, no pip call.
  - Idempotent — safe to call every run.
  - Quiet — installs with -q; returns a dict describing what it did.

CLI:  python3 db/ensure_deps.py        # ensure, print result
      python3 db/ensure_deps.py --check # report only, exit 1 if missing
"""

import importlib.util
import subprocess
import sys
from pathlib import Path

# Deps that gate the semantic layer. sqlite-vec is intentionally NOT here —
# it's declared in requirements.txt for the future but not yet imported by any
# code path, so its absence must not trigger an install or a failure.
REQUIRED = ["fastembed", "numpy"]

REPO_ROOT = Path(__file__).resolve().parent.parent
REQUIREMENTS = REPO_ROOT / "requirements.txt"


def missing() -> list[str]:
    """Return the subset of REQUIRED modules that aren't importable."""
    return [m for m in REQUIRED if importlib.util.find_spec(m) is None]


def ensure(quiet: bool = True) -> dict:
    """Install any missing REQUIRED deps. Returns {installed, already, ok}."""
    need = missing()
    if not need:
        return {"installed": [], "already": list(REQUIRED), "ok": True}

    cmd = [sys.executable, "-m", "pip", "install", "--break-system-packages"]
    if quiet:
        cmd.append("-q")
    # Prefer the pinned manifest; fall back to bare module names if it's absent.
    cmd += ["-r", str(REQUIREMENTS)] if REQUIREMENTS.exists() else need
    subprocess.run(cmd, check=True)

    still = missing()
    return {
        "installed": [m for m in need if m not in still],
        "already": [m for m in REQUIRED if m not in need],
        "ok": not still,
        "still_missing": still,
    }


if __name__ == "__main__":
    if "--check" in sys.argv:
        m = missing()
        print("missing:", m or "none")
        sys.exit(1 if m else 0)
    print(ensure())
