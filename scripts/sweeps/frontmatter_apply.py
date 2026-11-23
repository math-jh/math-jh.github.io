#!/usr/bin/env python3
"""검수 끝난 excerpt·description 적용안을 글 front matter 에 써 넣는다.

입력은 frontmatter_rewrite.py 의 제안을 검수해 합친 JSON(글마다 excerpt·description 의
old / final / source). source 가 '제안'·'검수 수정'인 필드만 바꾸고, '그대로'·'되돌림'은
건드리지 않는다.

  frontmatter_apply.py <merged.json>...            바뀔 내용만 보고 (쓰지 않음)
  frontmatter_apply.py --apply <merged.json>...    실제로 씀

키가 없는 글(old 가 빈 문자열)에는 excerpt·description·title 중 먼저 있는 키 아래에 새 줄을 넣는다.

안전장치: 글의 지금 값이 검수 때 본 값(old)과 다르면 그 필드는 건너뛰고 보고한다.
쓰기 전에 새 front matter 를 다시 파싱해 두 키 말고는 아무것도 바뀌지 않았는지, 본문이
바이트 단위로 같은지 확인하고, 하나라도 어긋나면 아무 파일도 쓰지 않고 끝낸다.
원래 줄은 FM_BACKUP(기본 /var/tmp/blog-frontmatter-apply-backup.json)에 남긴다.
"""
import json
import os
import re
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
BACKUP = Path(os.environ.get("FM_BACKUP", "/var/tmp/blog-frontmatter-apply-backup.json"))
KEYS = ("excerpt", "description")
APPLY_SOURCES = ("제안", "검수 수정")


def split_front_matter(text):
    m = re.match(r"---\n(.*?\n)---\n", text, re.S)
    if not m:
        raise ValueError("front matter 없음")
    return m.group(1), text[m.end():]


def key_block(lines, key):
    """front matter 줄 목록에서 key 가 차지하는 줄 범위 [start, end)."""
    for i, line in enumerate(lines):
        if line.startswith(key + ":"):
            j = i + 1
            while j < len(lines) and (lines[j].startswith((" ", "\t")) or not lines[j].strip()):
                j += 1
            while j > i + 1 and not lines[j - 1].strip():
                j -= 1
            return i, j
    return None


def quoted(value):
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def norm(value):
    return re.sub(r"\s+", " ", str(value or "")).strip()


def plan(records):
    changes, skipped, problems = [], [], []
    for rec in records:
        path = REPO / rec["path"]
        text = path.read_text(encoding="utf-8")
        head, body = split_front_matter(text)
        before = yaml.safe_load(head)
        lines = head.split("\n")
        original = {}
        for key in KEYS:
            field = rec[key]
            if field["source"] not in APPLY_SOURCES:
                continue
            final = field["final"]
            current = norm(before.get(key))
            if current == norm(final):
                skipped.append((rec["path"], key, "이미 적용됨"))
                continue
            if current != norm(field["old"]):
                problems.append((rec["path"], key, f"지금 값이 검수 때와 다름: {current[:60]}"))
                continue
            block = key_block(lines, key)
            if block is None:
                # 키가 아예 없는 글: 다른 쪽 키(없으면 title) 바로 아래에 새 줄로 넣는다.
                anchor = next((b for b in (key_block(lines, k) for k in (*KEYS, "title")) if b), None)
                if anchor is None:
                    problems.append((rec["path"], key, "넣을 위치를 찾지 못함"))
                    continue
                start = end = anchor[1]
            else:
                start, end = block
            original[key] = lines[start:end]
            lines[start:end] = [f"{key}: {quoted(final)}"]
        if not original:
            continue
        new_head = "\n".join(lines)
        after = yaml.safe_load(new_head)
        for key in set(before) | set(after):
            if key in original:
                if after.get(key) != rec[key]["final"]:
                    raise SystemExit(f"중단: {rec['path']} {key} 가 적용안과 다르게 써짐")
            elif before.get(key) != after.get(key):
                raise SystemExit(f"중단: {rec['path']} 의 다른 키 {key} 가 바뀜")
        new_text = f"---\n{new_head}---\n{body}"
        if split_front_matter(new_text)[1] != body:
            raise SystemExit(f"중단: {rec['path']} 본문이 바뀜")
        changes.append((path, new_text, original))
    return changes, skipped, problems


def main():
    args = sys.argv[1:]
    apply = "--apply" in args
    sources = [a for a in args if a != "--apply"]
    if not sources:
        raise SystemExit(__doc__)
    records = [r for src in sources for r in json.load(open(src, encoding="utf-8"))]
    paths = [r["path"] for r in records]
    if len(paths) != len(set(paths)):
        raise SystemExit("중단: 같은 글이 두 번 들어 있음")
    changes, skipped, problems = plan(records)
    fields = sum(len(orig) for _, _, orig in changes)
    print(f"글 {len(records)}편 · 바뀌는 글 {len(changes)}편 · 바뀌는 필드 {fields}개 · "
          f"건너뜀 {len(skipped)} · 문제 {len(problems)}")
    for path, key, why in problems:
        print(f"  [문제] {path} {key}: {why}")
    for path, key, why in skipped:
        print(f"  [건너뜀] {path} {key}: {why}")
    if not apply:
        print("dry-run (쓰지 않음). 실제로 쓰려면 --apply")
        return
    backup = json.load(open(BACKUP, encoding="utf-8")) if BACKUP.exists() else {}
    for path, _, original in changes:
        backup.setdefault(str(path.relative_to(REPO)), {}).update(original)
    BACKUP.write_text(json.dumps(backup, ensure_ascii=False, indent=1), encoding="utf-8")
    for path, new_text, _ in changes:
        path.write_text(new_text, encoding="utf-8")
    print(f"적용 완료. 원래 줄 백업: {BACKUP}")


if __name__ == "__main__":
    main()
