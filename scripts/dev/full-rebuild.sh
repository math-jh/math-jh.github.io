#!/usr/bin/env bash
# Force the local livereload server to do a FULL rebuild.
#
# Why this exists: the dev server runs `jekyll serve --incremental`, which only
# regenerates files whose own source (or a tracked layout/include) changed.
# Jekyll does NOT track `_data/*.yml` as a dependency — so editing
# `_data/navigation.yml` (the top menu + sidebar nav) leaves the nav stale on
# every post page until a full rebuild. Restarting the service alone does NOT
# help, because the persisted `.jekyll-metadata` still suppresses regeneration.
#
# Run this after editing anything under `_data/` (or whenever local output
# looks stale). It clears the incremental metadata and restarts the server,
# forcing one clean full build (~30s). Production is unaffected — CI always
# builds clean from scratch.

set -euo pipefail

BLOG=/home/junhyeok/math-jh.github.io
SVC=jekyll-blog.service

echo "Stopping $SVC ..."
systemctl --user stop "$SVC" || true

echo "Clearing incremental metadata + cache ..."
rm -f "$BLOG/.jekyll-metadata"
rm -rf "$BLOG/.jekyll-cache"

echo "Starting $SVC (full rebuild) ..."
systemctl --user start "$SVC"

echo "Done. Watch progress: journalctl --user -fu $SVC  (or tail $BLOG/_site/jekyll.log)"
