#!/usr/bin/env bash
# Re-index the local _site/ with Pagefind (cargo-built native binary).
# Use after content changes when you want search to reflect them locally.
# CI rebuilds the index on every push, so this is local-only.
set -euo pipefail
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
"$HOME/.cargo/bin/pagefind" --site "$REPO/_site" --quiet
echo "Pagefind index refreshed at $REPO/_site/pagefind/"
