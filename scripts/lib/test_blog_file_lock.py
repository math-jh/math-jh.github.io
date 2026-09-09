#!/usr/bin/env python3
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from blog_file_lock import try_acquire_file_locks


class BlogFileLockTest(unittest.TestCase):
    def test_overlap_conflicts_but_disjoint_paths_do_not(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            lock_dir = root / "locks"
            first = try_acquire_file_locks([root / "ko.md", root / "en.md"], lock_dir=lock_dir)
            self.assertIsNotNone(first)
            try:
                self.assertIsNone(
                    try_acquire_file_locks([root / "en.md"], lock_dir=lock_dir)
                )
                other = try_acquire_file_locks([root / "other.md"], lock_dir=lock_dir)
                self.assertIsNotNone(other)
                other.release()
            finally:
                first.release()

            again = try_acquire_file_locks([root / "ko.md"], lock_dir=lock_dir)
            self.assertIsNotNone(again)
            again.release()

    def test_partial_set_is_released_after_conflict(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            lock_dir = root / "locks"
            held = try_acquire_file_locks([root / "z.md"], lock_dir=lock_dir)
            self.assertIsNotNone(held)
            try:
                self.assertIsNone(
                    try_acquire_file_locks(
                        [root / "a.md", root / "z.md"], lock_dir=lock_dir
                    )
                )
                a_only = try_acquire_file_locks([root / "a.md"], lock_dir=lock_dir)
                self.assertIsNotNone(a_only)
                a_only.release()
            finally:
                held.release()


if __name__ == "__main__":
    unittest.main()
