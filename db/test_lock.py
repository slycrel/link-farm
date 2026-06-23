#!/usr/bin/env python3
"""
Regression tests for db/lock.py (flock-based writer lock).

Focus: the failure modes that motivated the flock rewrite —
    1. A lock held by a process that dies (without calling release) must be
       immediately acquirable by the next process. This is the "stale lock"
       bug the old PID/unlink design could not recover from on the FUSE mount.
    2. Two live holders are mutually excluded; the second times out.
    3. Acquire / release / context-manager round-trips work.
    4. Reusing a lockfile that already has leftover content (e.g. an old PID)
       just works — content is non-authoritative under flock.

Run:  python3 db/test_lock.py        (exits non-zero on failure)
"""

import os
import sys
import time
import tempfile
import textwrap
import subprocess
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPT_DIR.parent))

from db.lock import writer_lock, WriterLock, LockTimeout  # noqa: E402

_failures = []


def check(cond, msg):
    status = "PASS" if cond else "FAIL"
    print(f"  [{status}] {msg}")
    if not cond:
        _failures.append(msg)


def _hold_lock_in_child(lockpath: str, hold_seconds: float) -> subprocess.Popen:
    """Spawn a child that acquires the lock and holds it, printing READY."""
    code = textwrap.dedent(f"""
        import sys, time
        sys.path.insert(0, {str(SCRIPT_DIR.parent)!r})
        from db.lock import writer_lock
        with writer_lock({lockpath!r}, timeout=5):
            print("READY", flush=True)
            time.sleep({hold_seconds})
    """)
    p = subprocess.Popen([sys.executable, "-c", code],
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    # Wait for READY so we know the child holds the lock.
    line = p.stdout.readline().strip()
    assert line == "READY", f"child did not acquire lock, got: {line!r}"
    return p


def test_basic_roundtrip(lockpath):
    print("test_basic_roundtrip")
    lock = WriterLock(lockpath, timeout=2)
    lock.acquire()
    check(lock._fd is not None, "acquire sets fd")
    lock.release()
    check(lock._fd is None, "release clears fd")
    with writer_lock(lockpath, timeout=2):
        pass
    check(True, "context manager acquire/release ok")


def test_stale_lock_from_dead_process(lockpath):
    # The motivating bug: a holder dies WITHOUT releasing. flock must let the
    # next acquirer in immediately.
    print("test_stale_lock_from_dead_process")
    child = _hold_lock_in_child(lockpath, hold_seconds=30)
    try:
        # Lock is held — a short-timeout acquire here should time out.
        timed_out = False
        try:
            with writer_lock(lockpath, timeout=1):
                pass
        except LockTimeout:
            timed_out = True
        check(timed_out, "live holder excludes a second acquirer (times out)")

        # Kill the holder hard (simulates crash / namespace teardown). It never
        # gets to run release(); the lockfile stays on disk with its PID.
        child.kill()
        child.wait(timeout=5)

        # The next acquire must succeed promptly — kernel released the flock on
        # process death even though the file was never unlinked.
        t0 = time.time()
        got = False
        with writer_lock(lockpath, timeout=5):
            got = True
        check(got, "stale lock (dead holder) is acquirable")
        check(time.time() - t0 < 2.0, "stale lock acquired promptly (<2s, no full timeout wait)")
    finally:
        if child.poll() is None:
            child.kill()
            child.wait(timeout=5)


def test_leftover_content_is_ignored(lockpath):
    # Old design left arbitrary content (e.g. "0" or a stale PID). flock must
    # not care about file contents.
    print("test_leftover_content_is_ignored")
    Path(lockpath).write_text("2\n")  # mimic the stale PID-2 file we hit in prod
    got = False
    with writer_lock(lockpath, timeout=2):
        got = True
    check(got, "lockfile with leftover stale-PID content is still acquirable")


def main():
    with tempfile.TemporaryDirectory() as d:
        lockpath = os.path.join(d, ".writer.lock")
        test_basic_roundtrip(lockpath)
        test_stale_lock_from_dead_process(lockpath)
        test_leftover_content_is_ignored(lockpath)

    print()
    if _failures:
        print(f"{len(_failures)} FAILURE(S):")
        for f in _failures:
            print("   -", f)
        sys.exit(1)
    print("All lock tests passed.")
    sys.exit(0)


if __name__ == "__main__":
    main()
