#!/usr/bin/env bash
# Cron entry point for Marvin (blogdev-bot). Fires once per tick (weekly).
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=lib.sh
source "$HERE/lib.sh"

ensure_session
git_sync
prep_marvin
send_line "Read $HERE/marvin.md and execute it now."
log "injected blogdev-bot marvin prompt"
