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

Moved here 2026-07-17 (dead-device sweep):

- `triage_overrides.py` + `anchor-*.json` + `anchor-review.md` — one-time anchor
  triage snapshot from the 2026-05-28 link-normalizer work (see the
  Link_Normalizer workshop post). Frozen since; nothing calls them.

Live tooling stays under `scripts/` (translation, comments, audit, diagrams/build.sh,
index-monitor, dev, favicons, generate-thumbnails.js, reindex-pagefind.sh).
