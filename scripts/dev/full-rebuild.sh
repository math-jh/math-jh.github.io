#!/usr/bin/env bash
# Force the local livereload server to do a FULL rebuild.
#
# Why this exists: the dev server runs `jekyll serve --incremental`, which only
# regenerates files whose own source (or a tracked layout/include) changed.
# Jekyll does NOT track `_data/*.yml` as a dependency — so editing
# `_data/navigation.yml` (the top menu + sidebar nav) leaves the nav stale on
# every post page until a full rebuild. A plain restart now usually suffices:
# the unit's ExecStartPre (`~/.local/bin/jekyll-data-rebuild-guard.py prepare`)
# clears metadata and cache when the `_data`/navigation digest changed.
#
# Run this when local output still looks stale. It clears the incremental
# metadata and cache and restarts the server, forcing one clean full build
# (~30s). Production is unaffected — CI always builds clean from scratch.

set -euo pipefail

BLOG=/home/junhyeok/math-jh.github.io
SVC=jekyll-blog.service

# .jekyll-cache is a symlink into ~/.cache/jekyll-mathjh (the unit's ExecStartPre
# creates it). `rm -rf` on the link would drop only the link and leave the real
# cache intact, so empty the resolved target and keep the link. Resolve and vet
# the target before stopping the server, so a refusal leaves it running.
CACHE="$BLOG/.jekyll-cache"
target=""
if [ -L "$CACHE" ]; then
  target=$(readlink -f "$CACHE" || true)
  case "$target" in
    "" | / | "$HOME" | "$BLOG")
      echo "Refusing to clear cache: suspicious symlink target '$target'" >&2
      exit 1
      ;;
  esac
fi

echo "Stopping $SVC ..."
systemctl --user stop "$SVC" || true

echo "Clearing incremental metadata + cache ..."
rm -f "$BLOG/.jekyll-metadata"
if [ -n "$target" ]; then
  if [ -d "$target" ]; then
    find "$target" -mindepth 1 -maxdepth 1 -exec rm -rf -- {} +
  fi
else
  rm -rf "$CACHE"
fi

echo "Starting $SVC (full rebuild) ..."
systemctl --user start "$SVC"

echo "Done. Watch progress: journalctl --user -fu $SVC  (or tail $BLOG/_site/jekyll.log)"
