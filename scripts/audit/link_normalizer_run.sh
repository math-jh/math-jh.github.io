#!/usr/bin/env bash
# Refresh scripts/audit/link-overrides.log by doing a one-shot production
# Jekyll build. Output goes to a disk-backed throwaway dir (NOT /tmp, which is
# tmpfs/RAM on this Pi — a full _site is ~700M and would spike memory) so the
# livereload daemon's _site is untouched. The tracker log itself lives in the
# source tree and gets rewritten by the link_normalizer plugin during this build.

set -euo pipefail

BLOG=/home/junhyeok/math-jh.github.io
DEST="/var/tmp/jekyll-link-audit-$$"

cd "$BLOG"

JEKYLL_ENV=production /usr/local/bin/bundle exec jekyll build \
  --destination "$DEST" --quiet >/dev/null 2>&1

# Print summary so the cron log captures it.
SUMMARY=$(tail -n1 scripts/audit/link-overrides.log 2>/dev/null || true)
printf '[%s] %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$SUMMARY"

rm -rf "$DEST"
