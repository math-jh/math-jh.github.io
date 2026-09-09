#!/usr/bin/env python3
"""Non-blocking locks for blog files shared by cron workers.

Long-running model calls may overlap as long as they do not touch the same
post.  Git commits and worker-owned aggregate state still use their own short
or resource-specific locks; this module protects only the concrete content
files passed to it.
"""
from __future__ import annotations

import fcntl
import hashlib
import os
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


LOCK_DIR = Path("/tmp/blog-file-locks")


@dataclass
class FileLockSet:
    """A successfully acquired set of file locks."""

    fds: list[int]
    paths: tuple[Path, ...]

    def release(self) -> None:
        while self.fds:
            os.close(self.fds.pop())

    def __enter__(self) -> "FileLockSet":
        return self

    def __exit__(self, *_exc: object) -> None:
        self.release()


def _canonical(paths: Iterable[Path | str]) -> tuple[Path, ...]:
    # All callers acquire in the same order, so a future blocking caller cannot
    # introduce an AB/BA deadlock.  resolve(strict=False) also gives prospective
    # translation output paths a stable identity before the EN file exists.
    return tuple(sorted({Path(p).resolve(strict=False) for p in paths}, key=str))


def try_acquire_file_locks(
    paths: Iterable[Path | str], *, lock_dir: Path = LOCK_DIR,
) -> FileLockSet | None:
    """Atomically-ish acquire every path lock, or release all and return None.

    The set acquisition is non-blocking.  Persistent empty lock files are only
    rendezvous points; closing the returned descriptors releases the locks.
    """
    canonical = _canonical(paths)
    lock_dir.mkdir(parents=True, exist_ok=True)
    fds: list[int] = []
    try:
        for path in canonical:
            name = hashlib.sha256(str(path).encode("utf-8")).hexdigest() + ".lock"
            fd = os.open(lock_dir / name, os.O_CREAT | os.O_RDWR, 0o664)
            try:
                fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except OSError:
                os.close(fd)
                raise
            fds.append(fd)
        return FileLockSet(fds=fds, paths=canonical)
    except OSError:
        while fds:
            os.close(fds.pop())
        return None


def acquire_file_locks(
    paths: Iterable[Path | str], *, wait_sec: float, lock_dir: Path = LOCK_DIR,
    poll_sec: float = 0.25,
) -> FileLockSet | None:
    """Acquire a path set within ``wait_sec`` without holding partial sets."""
    deadline = time.monotonic() + max(0.0, wait_sec)
    while True:
        lease = try_acquire_file_locks(paths, lock_dir=lock_dir)
        if lease is not None:
            return lease
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            return None
        time.sleep(min(poll_sec, remaining))
