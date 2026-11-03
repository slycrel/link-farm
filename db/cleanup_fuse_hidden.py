#!/usr/bin/env python3
"""Remove orphaned `.fuse_hidden*` files from db/.

The cowork mount denies unlink, so deleted-but-still-open files pile up as
`.fuse_hidden*` orphans (reached ~5,200 files / 284 MB once and made db/
unlistable). This only ever removes files whose names start with
`.fuse_hidden` directly inside db/ - never the SQLite DB, its -wal/-shm/-journal
files, backups, or anything else.

Usage:
    python3 db/cleanup_fuse_hidden.py              # dry run: count + size
    python3 db/cleanup_fuse_hidden.py --delete     # delete
    python3 db/cleanup_fuse_hidden.py --delete --min 500   # only if > 500 files

Deleting needs delete permission on the mount (in Cowork: the
device_request_delete_permission tool). Without it unlink fails with
"Operation not permitted"; this script reports that and exits 2.
"""
import argparse, os, sys
from pathlib import Path

PREFIX = '.fuse_hidden'


def find_orphans(db_dir: Path):
    out = []
    for e in os.scandir(db_dir):
        if e.name.startswith(PREFIX) and e.is_file(follow_symlinks=False):
            out.append(Path(e.path))
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--db-dir', default=str(Path(__file__).resolve().parent))
    ap.add_argument('--delete', action='store_true', help='actually delete (default: dry run)')
    ap.add_argument('--min', type=int, default=0, help='only delete if more than N orphans exist')
    a = ap.parse_args(argv)

    files = find_orphans(Path(a.db_dir))
    size = sum(f.stat().st_size for f in files if f.exists())
    print(f'{len(files)} {PREFIX}* files, {size/1e6:.1f} MB in {a.db_dir}')
    if not a.delete:
        print('dry run; pass --delete to remove')
        return 0
    if len(files) <= a.min:
        print(f'at or below --min {a.min}; nothing to do')
        return 0
    removed = failed = 0
    for f in files:
        try:
            f.unlink(); removed += 1
        except PermissionError:
            failed += 1
        except FileNotFoundError:
            pass
    print(f'removed {removed}, failed {failed}')
    if failed:
        print('unlink denied: request delete permission for the cowork folder and rerun', file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    sys.exit(main())
