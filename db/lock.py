#!/usr/bin/env python3
"""
Shared writer lock for the ai-links database.

Every process that mutates ai_links.db or regenerates output artifacts via
rebuild.py must acquire this lock first. That includes:

    - The daily sync skill (new posts from email)
    - The catch-up skill (re-enrichment, backfill)
    - curate.py (chat-mediated curation: promote, merge, dismiss)
    - Any future writer

Without the shared lock, a sync run and a curation run can race on rebuild.py
outputs — A rebuilds state A, B writes B, A overwrites and pushes stale.

Implementation: advisory whole-file lock via ``fcntl.flock`` on a persistent
lockfile (``db/.writer.lock``). The kernel ties the lock to the open file
description, so it is **released automatically when the holding process exits**
— even on a crash, a SIGKILL, or a sandbox/namespace teardown. That removes the
entire class of "stale lock left behind by a dead writer" bugs without any PID
heuristics.

Why not the previous O_CREAT|O_EXCL + PID-file design? Two failure modes bit us:

    1. The cowork folder is a virtiofs/FUSE mount where ``unlink`` is denied
       (EPERM), so ``release()`` could never delete the lockfile and stale-lock
       cleanup could never run. The very first writer left a permanent file and
       every later writer hit EEXIST forever.
    2. PID liveness (``os.kill(pid, 0)``) false-positives across the
       PID-namespaced sandbox shells, which reuse low PIDs — a dead holder's
       PID 2 looks "alive" because the current shell is also PID 2.

flock sidesteps both: the lockfile is created once and never unlinked (its mere
existence is harmless), and liveness is the kernel's problem, not ours.

Reentrancy note: flock is per open file description, so each ``WriterLock``
opens its own fd and a *second* acquisition in the same process will block.
Writers that already hold the lock must pass ``with_lock=False`` to nested
helpers (the enrich/pipeline/rebuild APIs already do this).

Usage:
    from db.lock import writer_lock

    with writer_lock():
        # mutate SQLite, run rebuild, push to GitHub
        ...
"""

import os
import time
import errno
import fcntl
from contextlib import contextmanager
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
DEFAULT_LOCK_PATH = SCRIPT_DIR / ".writer.lock"

# errnos that mean "lock is held by someone else, try again later"
_WOULDBLOCK = {errno.EACCES, errno.EAGAIN, errno.EWOULDBLOCK}


class LockTimeout(Exception):
    """Raised when the lock cannot be acquired within the timeout window."""


class WriterLock:
    """Advisory whole-file mutex (flock) for ai-links writers.

    Attributes:
        path: lockfile location (default: db/.writer.lock)
        timeout: max seconds to wait when acquiring (default 60)
        poll: seconds between retries (default 0.5)
    """

    def __init__(self, path: Path = DEFAULT_LOCK_PATH, timeout: float = 60.0,
                 poll: float = 0.5):
        self.path = Path(path)
        self.timeout = timeout
        self.poll = poll
        self._fd = None

    def acquire(self) -> None:
        """Block until the lock is acquired or timeout expires.

        Raises LockTimeout if the lock is held by another live process for the
        full timeout window. The lockfile is created if missing and is *never*
        unlinked — flock state lives in the kernel, not in the file's presence.
        """
        # Open (creating if needed) a long-lived fd we hold for the lock's life.
        fd = os.open(str(self.path), os.O_CREAT | os.O_RDWR, 0o644)
        deadline = time.time() + self.timeout
        while True:
            try:
                fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
                self._fd = fd
                self._stamp_pid()  # best-effort diagnostic breadcrumb
                return
            except OSError as e:
                if e.errno not in _WOULDBLOCK:
                    os.close(fd)
                    raise
            if time.time() >= deadline:
                os.close(fd)
                raise LockTimeout(
                    f"Could not acquire {self.path} within {self.timeout}s"
                )
            time.sleep(self.poll)

    def _stamp_pid(self) -> None:
        """Write the holder PID into the file for human debugging only.

        Purely informational — acquisition correctness comes from flock, not
        from this content. Best-effort: never fail the lock over it (the mount
        forbids unlink but does allow truncate+write).
        """
        if self._fd is None:
            return
        try:
            os.lseek(self._fd, 0, os.SEEK_SET)
            os.ftruncate(self._fd, 0)
            os.write(self._fd, f"{os.getpid()}\n".encode())
            os.fsync(self._fd)
        except OSError:
            pass

    def release(self) -> None:
        """Release the lock. Safe to call if not held.

        Unlocks and closes the fd; the kernel would also release on close or on
        process exit. The lockfile itself is intentionally left in place (the
        mount forbids unlink, and a persistent flock target is correct anyway).
        """
        if self._fd is not None:
            try:
                fcntl.flock(self._fd, fcntl.LOCK_UN)
            except OSError:
                pass
            try:
                os.close(self._fd)
            except OSError:
                pass
            self._fd = None

    def __enter__(self):
        self.acquire()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.release()
        return False


@contextmanager
def writer_lock(path: Path = DEFAULT_LOCK_PATH, timeout: float = 60.0,
                poll: float = 0.5):
    """Context manager wrapper. The canonical way to use the lock.

        with writer_lock():
            ...

    Raises LockTimeout if the lock can't be acquired within `timeout` seconds.
    """
    lock = WriterLock(path, timeout, poll)
    lock.acquire()
    try:
        yield lock
    finally:
        lock.release()


if __name__ == "__main__":
    # Smoke test: acquire, hold for a second, release.
    import sys
    print(f"Acquiring lock at {DEFAULT_LOCK_PATH}...")
    with writer_lock(timeout=5):
        print(f"  Held by PID {os.getpid()}. Sleeping 1s.")
        time.sleep(1)
    print("Released.")
    sys.exit(0)
