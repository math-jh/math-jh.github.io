#!/usr/bin/env python3
"""For every KO post that has `description:`, bump the EN counterpart's
`translated_at` frontmatter to (now + 24h), so the translation worker's
git-based drift check doesn't flag description-only KO changes as drift.

Idempotent: only bumps if KO actually has description AND EN's current
translated_at is in the past.
"""
import glob
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]


def parse_frontmatter(text):
    if not text.startswith("---"):
        return None, text
    end = text.find("---", 4)
    if end == -1:
        return None, text
    return text[4:end], text[end + 3:]


def get_field(fm, name):
    m = re.search(rf'^{name}:\s*"?(.+?)"?\s*$', fm, re.M)
    return m.group(1) if m else None


def set_field(fm, name, value):
    line = f"{name}: {value}"
    if re.search(rf"^{name}:", fm, re.M):
        return re.sub(rf"^{name}:.*$", line, fm, count=1, flags=re.M)
    # Append at end of frontmatter
    return fm.rstrip() + f"\n{line}\n"


def main():
    new_ts = (datetime.now(timezone.utc) + timedelta(hours=24)).isoformat(timespec="seconds")
    ko_files = sorted(glob.glob(str(REPO / "_posts/Math/*/ko/*.md")))
    bumped = skipped_no_desc = skipped_no_en = skipped_already_future = 0

    for ko_path in ko_files:
        ko_txt = Path(ko_path).read_text()
        ko_fm, _ = parse_frontmatter(ko_txt)
        if ko_fm is None or not get_field(ko_fm, "description"):
            skipped_no_desc += 1
            continue
        en_path = ko_path.replace("/ko/", "/en/")
        if not Path(en_path).exists():
            skipped_no_en += 1
            continue
        en_txt = Path(en_path).read_text()
        en_fm, en_body = parse_frontmatter(en_txt)
        if en_fm is None:
            continue
        existing = get_field(en_fm, "translated_at")
        if existing:
            try:
                existing_dt = datetime.fromisoformat(existing)
                if existing_dt.timestamp() > datetime.now(timezone.utc).timestamp():
                    skipped_already_future += 1
                    continue
            except ValueError:
                pass
        new_fm = set_field(en_fm, "translated_at", new_ts)
        Path(en_path).write_text("---" + new_fm + "---" + en_body)
        bumped += 1
        print(f"  bumped: {Path(en_path).name}")

    print(f"\nbumped={bumped} skipped_no_desc={skipped_no_desc} "
          f"skipped_no_en={skipped_no_en} skipped_already_future={skipped_already_future}")


if __name__ == "__main__":
    main()
