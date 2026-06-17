# archived scripts

One-off / migration scripts that have served their purpose. Kept for reference
(not deleted), but referenced by nothing — no cron, CI, systemd unit, or other
script calls them. Moved here 2026-06-17 during a codebase cleanup.

- `fix_dollar_downgrades.py` — one-time fix of `$..$` → `$$..$$` downgrades in EN translations.
- `math_block_audit.py` — one-time analysis of math-block counts (translation loss check).
- `translation_loss_audit.py` — one-time translation-semantics audit.
- `extract_set.py` — one-time Set-Theory diagram figure extraction.
- `remove_description.py` — one-time image-description cleanup.
- `update_set_posts.py` — one-time batch update of Set-Theory posts.

Live tooling stays under `scripts/` (translation, comments, audit, diagrams/build.sh,
index-monitor, dev, favicons, generate-thumbnails.js, reindex-pagefind.sh).
