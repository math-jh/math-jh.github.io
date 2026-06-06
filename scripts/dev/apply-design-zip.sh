#!/usr/bin/env bash
# Apply the latest Claude Design export to the blog.
#
# Picks the most-recently-modified "math-jh.github.io (*).zip" in
# ~/Documents/Temporary, extracts it, and overwrites the repo with every file
# under its changed_files/ folder (preserving relative paths). The livereload
# dev server (jekyll-blog.service) recompiles automatically — no commit, no push
# (autopush stays as you left it).
#
# Usage:
#   scripts/dev/apply-design-zip.sh            # newest zip
#   scripts/dev/apply-design-zip.sh "/path/to/specific (4).zip"
set -euo pipefail

REPO=/home/junhyeok/math-jh.github.io
SRCDIR="$HOME/Documents/Temporary"

ZIP="${1:-}"
if [ -z "$ZIP" ]; then
  ZIP=$(ls -t "$SRCDIR"/math-jh.github.io*.zip 2>/dev/null | head -1)
fi
[ -n "${ZIP:-}" ] && [ -f "$ZIP" ] || { echo "❌ no zip found (looked in $SRCDIR)"; exit 1; }

TMP=$(mktemp -d /var/tmp/design-zip.XXXXXX)
trap 'rm -rf "$TMP"' EXIT

echo "→ $ZIP"
unzip -q "$ZIP" -d "$TMP"

CF=$(find "$TMP" -type d -name changed_files | head -1)
[ -n "${CF:-}" ] || { echo "❌ no changed_files/ folder inside the zip"; exit 1; }

n=0
while IFS= read -r f; do
  rel="${f#"$CF"/}"
  dest="$REPO/$rel"
  mkdir -p "$(dirname "$dest")"
  cp "$f" "$dest"
  echo "  ✓ $rel"
  n=$((n + 1))
done < <(find "$CF" -type f | sort)

echo "✅ applied $n file(s). livereload will recompile (~5-10s)."
