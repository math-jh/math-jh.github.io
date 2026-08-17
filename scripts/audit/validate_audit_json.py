#!/usr/bin/env python3
"""audit.json 자체 점검 — 감사를 낸 쪽이 넘기기 전에 돌린다.

비교기가 항목을 못 붙이는 사고는 전부 **에러 없이** 일어난다 (그냥 카드가 안 뜬다).
그래서 규약을 기계로 확인한다. 제일 중요한 검사는 하나다:

    인용문이 base 판본의 그 파일에 **정말로 그대로 있는가**

사용법:
    validate_audit_json.py notes/audit-<slug>/            # 폴더 안 audit*.json 전부
    validate_audit_json.py notes/audit-<slug>/audit.json
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATUSES = {"open", "applied", "dismissed"}
MARKERS = (":::", "#", ">", "- ", "* ", "{%", "|")
MIN_QUOTE = 12          # 이보다 짧으면 글 안에서 유일하지 않기 쉽다
_WS = re.compile(r"\s+")


def norm(s: str) -> str:
    return _WS.sub("", s or "")


def git_show(ref: str, path: str) -> str | None:
    p = subprocess.run(["git", "-C", str(ROOT), "show", f"{ref}:{path}"],
                       capture_output=True, text=True)
    return p.stdout if p.returncode == 0 else None


def check(files: list[Path]) -> int:
    errors: list[str] = []
    warns: list[str] = []
    n_posts = n_items = 0
    base_refs: set[str] = set()
    cache: dict[str, str | None] = {}

    for f in files:
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
        except ValueError as e:
            errors.append(f"{f.name}: JSON 파싱 실패 — {e}")
            continue
        if d.get("schema", "").split("/")[0] != "blog-audit":
            errors.append(f"{f.name}: schema 가 blog-audit/… 이 아니다")
            continue
        base = d.get("base_ref", "")
        if not base:
            errors.append(f"{f.name}: base_ref 없음")
            continue
        base_refs.add(base)

        for post in d.get("posts", []):
            n_posts += 1
            path = post.get("path", "")
            if path not in cache:
                cache[path] = git_show(base, path)
            src = cache[path]
            if src is None:
                # 버전 관리 밖 글(로컬 전용 카테고리)은 base 판본 자체가 없다 —
                # 인용문을 확인할 방법이 없을 뿐 감사 자체는 유효하다.
                tracked = subprocess.run(["git", "-C", str(ROOT), "ls-files", "--error-unmatch",
                                          path], capture_output=True).returncode == 0
                (warns if not tracked else errors).append(
                    f"{f.name}: {'버전 관리 밖 글 — 인용문 확인 불가' if not tracked else 'base 판본에 없는 파일'} — {path}")
                continue
            flat = norm(src)
            seen: set[str] = set()
            for it in post.get("items", []):
                n_items += 1
                iid = it.get("id", "")
                where = f"{path} {iid or '(id 없음)'}"
                if not iid:
                    errors.append(f"{where}: id 없음")
                elif iid in seen:
                    errors.append(f"{where}: 글 안에서 id 중복")
                seen.add(iid)
                if not it.get("summary"):
                    errors.append(f"{where}: summary 없음")
                if it.get("status") not in STATUSES:
                    errors.append(f"{where}: status 가 {sorted(STATUSES)} 중 하나가 아니다"
                                  f" ({it.get('status')!r})")

                q = it.get("quote", "")
                if not q:
                    warns.append(f"{where}: 인용문 없음 — 이 항목은 본문에 안 붙는다")
                    continue
                if q.lstrip().startswith(MARKERS):
                    errors.append(f"{where}: 인용문이 블록 마커로 시작한다 "
                                  f"({q[:20]!r}) — 본문 내용만 적을 것")
                if len(norm(q)) < MIN_QUOTE:
                    warns.append(f"{where}: 인용문이 짧다({len(norm(q))}자) — 유일하지 않을 수 있다")
                hits = flat.count(norm(q))
                if hits == 0:
                    errors.append(f"{where}: 인용문이 base 파일에 없다 — {q[:60]!r}")
                elif hits > 1 and not it.get("base_lines"):
                    warns.append(f"{where}: 인용문이 {hits}번 나온다 — base_lines 로 가릴 것")

                for k in ("was", "now"):
                    v = it.get(k)
                    if v and k == "was" and norm(v) not in flat:
                        warns.append(f"{where}: was 가 base 파일에 없다 — {v[:40]!r}")

    if len(base_refs) > 1:
        errors.append(f"base_ref 가 여럿이다 {sorted(b[:12] for b in base_refs)} — "
                      "한 감사는 한 판본을 본다")

    print(f"파일 {len(files)} · 글 {n_posts} · 항목 {n_items}")
    for e in errors[:40]:
        print(f"  [오류] {e}")
    for w in warns[:20]:
        print(f"  [경고] {w}")
    if len(errors) > 40:
        print(f"  … 오류 {len(errors) - 40}건 더")
    if len(warns) > 20:
        print(f"  … 경고 {len(warns) - 20}건 더")
    print(f"오류 {len(errors)} · 경고 {len(warns)}")
    return 1 if errors else 0


def main() -> None:
    if len(sys.argv) < 2:
        print(__doc__)
        raise SystemExit(2)
    target = Path(sys.argv[1])
    files = sorted(target.glob("audit*.json")) if target.is_dir() else [target]
    if not files:
        print(f"audit*.json 을 못 찾았다: {target}")
        raise SystemExit(2)
    raise SystemExit(check(files))


if __name__ == "__main__":
    main()
