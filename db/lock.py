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

File-based mutex via O_CREAT|O_EXCL. Solo-local-tool sized: handles stale
locks (holder PID died) by checking liveness; times out rather than blocking
forever; context-manager friendly. Not designed for many-writer or multi-host
scenarios — a single PID file in the cowork folder is sufficient.

Usage:
    from db.lock import writer_lock

    with writer_lock():
        # mutate SQLite, run rebuild, push to GitHub
        ...
"""

import os
import time
import errno
from contextlib import contextmanager
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
DEFAULT_LOCK_PATH = SCRIPT_DIR / ".writer.lock"


class LockTimeout(Exception):
    """Raised when the lock cannot be acquired within the timeout window."""


class WriterLock:
    """File-based mutex for ai-links writers.

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
        """Block until the lock is acquired or timeout expires."""
        deadline = time.time() + self.timeout
        while True:
            try:
                fd = os.open(str(self.path), os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o644)
                os.write(fd, f"{os.getpid()}\n".encode())
                self._fd = fd
                return
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise

            # Lockfile exists — check if the holder is still alive.
            if self._holder_dead():
                # Stale lock — clean up and retry immediately.
                try:
                    self.path.unlink()
                except FileNotFoundError:
                    pass
                continue

            if time.time() >= deadline:
                raise LockTimeout(
                    f"Could not acquire {self.path} within {self.timeout}s"
                )
            time.sleep(self.poll)

    def release(self) -> None:
        """Release the lock. Safe to call if not held."""
        if self._fd is not None:
            try:
                os.close(self._fd)
            except OSError:
                pass
            self._fd = None
        try:
            self.path.unlink()
        except FileNotFoundError:
            pass

    def _holder_dead(self) -> bool:
        """Return True if the recorded PID is no longer alive."""
        try:
            pid_str = self.path.read_text().strip()
        except FileNotFoundError:
            # Lock vanished between EEXIST and read — treat as available.
            return True
        try:
            pid = int(pid_str)
        except (ValueError, TypeError):
            # Garbage in lockfile — treat as stale.
            return True
        if pid == 0:
            return True
        try:
            os.kill(pid, 0)  # 0 signal = liveness probe, doesn't actually signal
            return False
        except OSError:
            return True

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
