#!/usr/bin/env python3
"""같은 글이 정의하는 중복 표제어를 한 항목으로 합친다.

찾는 방법은 유사도다. 같은 정의 글을 공유하는 표제어 쌍마다 영어끼리·한국어끼리
따로 재고, 어느 한쪽이라도 임계를 넘으면 후보로 본다. 언어를 나눠 재는 것이 핵심이다
— `GCD`/`greatest common divisor` 는 영어 유사도가 0.27 이지만 한국어가 둘 다
'최대공약수'라 한국어 쪽에서만 걸린다.

합친다는 것은 지우는 것이 아니다. 진 쪽의 영어형은 `alias_en`, 한국어형은 `alias`
로 내려가 색인 검색과 md_lint 의 이형 검사에 그대로 남는다. 색인 화면에서 줄이
하나로 줄 뿐이다. `defs`·`refs`·`see` 는 합집합으로 옮긴다.

기계가 정하지 않는 것:

* 뜻이 다른데 한국어 라벨만 같은 쌍 (`coequalizer`/`cokernel` 이 둘 다 '여핵',
  `disjoint`/`relatively prime` 이 둘 다 '서로소'). 문자열로는 굴절 변형과 구별되지
  않으므로 전부 `--review` 목록으로 빠진다.
* 정의 글이 여럿인 껍데기. `closed` 는 `$\\bar\\partial$-closed` 와 한 글을 공유하지만
  다른 두 글에서도 정의되는 제 몫의 용어다. 지우면 그 두 정의가 사라진다.

`--dry-run` 이 기본이다. 쓰기는 `--apply` 를 명시할 때만 한다.
"""
from __future__ import annotations

import argparse
import collections
import difflib
import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import terms_common as tc  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
TERMS = ROOT / "_data" / "terms.yml"
THRESHOLD = 0.9


def strip_math(s: str) -> str:
    return re.sub(r"\$[^$]*\$", "", s or "")


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9가-힣]+", "", strip_math(s).lower())


def sim(a: str, b: str) -> float | None:
    """한쪽이 비어 있으면 그 언어로는 판단하지 않는다 (0 이 아니라 '모름')."""
    x, y = norm(a), norm(b)
    if not x or not y:
        return None
    return difflib.SequenceMatcher(None, x, y).ratio()


def initials(s: str) -> str:
    return "".join(w[0] for w in re.findall(r"[A-Za-z]+", s or "")).lower()


def load() -> dict:
    return yaml.safe_load(TERMS.read_text(encoding="utf-8"))


def def_urls(t: dict) -> list[str]:
    return [x["url"].rstrip("/") for x in (t.get("defs") or []) if x.get("url")]


def math_spans(s: str) -> list[str]:
    return re.findall(r"\$[^$]*\$", s or "")


# 붙으면 다른 것이 되는 형태소. 문자열로는 한두 글자 차이라 유사도가 0.9 를 넘는데
# 뜻은 다르거나 정반대다 (`topology`/`pretopology`, 정칙/반정칙).
MODIFIERS = {
    "anti", "pre", "post", "co", "non", "un", "in", "semi", "quasi", "sub", "super",
    "bi", "tri", "multi", "pseudo", "hyper", "infra", "ultra", "left", "right",
    "upper", "lower", "inner", "outer", "weak", "strong", "strict", "proper",
    "준", "반", "비", "여", "쌍대", "국소", "대역", "좌", "우", "상", "하", "약", "강",
}


def modifier_apart(a: str, b: str) -> bool:
    """두 표제어의 차이가 수식어 하나를 넣고 뺀 것뿐인가."""
    x, y = norm(a), norm(b)
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, x, y).get_opcodes():
        if tag == "equal":
            continue
        for chunk in (x[i1:i2], y[j1:j2]):
            if chunk and chunk in MODIFIERS:
                return True
    return False


def classify(a: dict, b: dict, en: float | None, ko: float | None) -> str:
    ae, be = a.get("en") or "", b.get("en") or ""
    # 유사도는 수식을 지우고 잰다. 그래서 둘 다 수식을 달고 있고 그 수식만 다른
    # 쌍은 1.00 으로 올라온다 — `$R_0$-space` 와 `$T_1$-space` 가 그렇다. 지워진
    # 그 부분이 바로 두 용어를 가르는 내용이므로 기계가 손대서는 안 된다.
    ma, mb = math_spans(ae), math_spans(be)
    if ma and mb and ma != mb:
        return "review"
    if modifier_apart(ae, be) or modifier_apart(a.get("ko"), b.get("ko")):
        return "review"
    if ("$" in ae) != ("$" in be) and norm(ae) == norm(be):
        bare = b if "$" in ae else a
        # 장식 없는 쪽이 한 낱말이면 추출기가 남긴 껍데기다 (`$A$-algebra` → `algebra`).
        # 여러 낱말이면 그쪽이 오히려 본래 용어이고 장식 붙은 쪽이 특수한 경우다
        # (`differentiable manifold` 와 `$C^k$-differentiable manifold`) — 어느 쪽을
        # 표제어로 둘지는 편집 판단이라 기계가 정하지 않는다.
        if len(re.findall(r"[A-Za-z가-힣]+", strip_math(bare.get("en") or ""))) > 1:
            return "review"
        return "shell" if len(def_urls(bare)) <= 1 else "review"
    if (re.fullmatch(r"[A-Z]{2,6}", ae) and initials(be) == ae.lower()) or \
       (re.fullmatch(r"[A-Z]{2,6}", be) and initials(ae) == be.lower()):
        return "abbrev"
    # 굴절·표기 변형으로 자동 합치는 조건은 하나다: **저자가 두 항목에 같은 한국어
    # 라벨을 달았을 것.** 그건 문자열의 우연이 아니라 저자가 같은 용어로 본다는 표시다.
    # 영어 유사도만 보면 `cap product`/`cup product`(0.90), `perfect`/`imperfect
    # field`(0.92), `rational`/`irrational number`(0.93) 가 전부 통과한다 — 형태소
    # 목록을 아무리 늘려도 다음 반례가 나온다. 반대로 한국어가 같아도 영어가 멀면
    # 동의어이거나 라벨만 겹친 다른 개념이다 (`disjoint`/`relatively prime` 이 둘 다
    # '서로소', `coequalizer`/`cokernel` 이 둘 다 '여핵') — 그래서 둘 다 요구한다.
    ka, kb = norm(a.get("ko")), norm(b.get("ko"))
    if ka and ka == kb and en is not None and en >= 0.85:
        return "variant"
    return "review"


def winner(kind: str, a: dict, b: dict) -> tuple[dict, dict]:
    """남길 쪽과 접을 쪽. 규칙을 고정해 두 번 돌려도 같은 답이 나오게 한다."""
    if kind == "shell":
        # 장식이 붙은 쪽이 제 용어이고, 맨 낱말이 껍데기다.
        return (a, b) if "$" in (a.get("en") or "") else (b, a)
    if kind == "abbrev":
        # 풀네임이 표제어, 약어는 검색어.
        return (a, b) if not re.fullmatch(r"[A-Z]{2,6}", a.get("en") or "") else (b, a)
    # 굴절·표기 변형: 더 많이 정의된 쪽 → 짧은 쪽 → 사전순.
    key = lambda t: (-len(def_urls(t)), len(t.get("en") or ""), t.get("en") or "")
    ranked = sorted([a, b], key=key)
    return ranked[0], ranked[1]


def fold(keep: dict, drop: dict) -> tuple[list[str], set[str]]:
    """진 쪽을 이긴 쪽 안으로 접는다.

    사람이 읽을 줄과 **실제로 바뀐 필드 이름**을 돌려준다. 안 바뀐 필드까지 다시
    쓰면 원래 인용 스타일이 바뀌어 diff 에 잡음이 낀다.
    """
    notes: list[str] = []
    touched: set[str] = set()
    de, dk = (drop.get("en") or "").strip(), (drop.get("ko") or "").strip()
    if de and de.lower() != (keep.get("en") or "").lower():
        cur = list(keep.get("alias_en") or [])
        if de not in cur:
            keep["alias_en"] = cur + [de]
            notes.append(f"alias_en += {de!r}")
            touched.add("alias_en")
    if dk and dk != (keep.get("ko") or ""):
        cur = list(keep.get("alias") or [])
        if dk not in cur:
            keep["alias"] = cur + [dk]
            notes.append(f"alias += {dk!r}")
            touched.add("alias")
    for field in ("defs", "refs", "see"):
        extra = [x for x in (drop.get(field) or []) if x not in (keep.get(field) or [])]
        if extra:
            keep[field] = (keep.get(field) or []) + extra
            notes.append(f"{field} += {len(extra)}건")
            touched.add(field)
    return notes, touched


def _drop_field(lines: list[str], field: str) -> list[str]:
    """엔트리 깊이(2칸)의 `field:` 블록을 통째로 뺀다."""
    out, skipping = [], False
    for line in lines:
        if re.match(rf"^  {field}:", line):
            skipping = True
            continue
        if skipping and re.match(r"^  [A-Za-z_]+:", line):
            skipping = False
        if not skipping:
            out.append(line)
    return out


# 흐름열 `[a, b]` 안에서는 `{ } [ ] ,` 가 구조 문자다. tc.yaml_quote 는 블록 문맥
# 기준이라 `$\mathbb{K}$-벡터공간` 을 맨몸으로 내보내고, 그러면 YAML 이 깨진다.
_FLOW_UNSAFE = set("{}[],:#&*!|>'\"%@`")


def flow_quote(s: str) -> str:
    if any(ch in _FLOW_UNSAFE for ch in s) or s != s.strip():
        return "'" + s.replace("'", "''") + "'"
    return tc.yaml_quote(s)


def _render(field: str, value) -> list[str]:
    """집 스타일 그대로: 스칼라 목록은 흐름열 한 줄, 매핑 목록은 블록."""
    if all(isinstance(x, str) for x in value):
        return [f"  {field}: [" + ", ".join(flow_quote(x) for x in value) + "]"]
    out = [f"  {field}:"]
    for item in value:
        keys = list(item)
        out.append(f"  - {keys[0]}: {tc.yaml_quote(str(item[keys[0]]))}")
        for k in keys[1:]:
            out.append(f"    {k}: {tc.yaml_quote(str(item[k]))}")
    return out


def rewrite_chunk(chunk: str, entry: dict, touched: set[str]) -> str:
    """이긴 항목의 청크에 바뀐 필드만 다시 쓴다.

    나머지 줄은 손대지 않는다. alias·alias_en 은 `ko:` 바로 뒤에 놓고(집 스타일),
    defs·refs·see 는 청크 끝에 둔다 — 원래 그 자리에 있다.
    """
    lines = chunk.split("\n")
    for field in ("alias", "alias_en", "defs", "refs", "see"):
        if field in touched:
            lines = _drop_field(lines, field)

    for field in ("alias_en", "alias"):          # 역순으로 넣어야 alias 가 앞에 온다
        if field not in touched:
            continue
        rendered = _render(field, entry[field])
        at = next((i for i, l in enumerate(lines) if re.match(r"^  ko:", l)), None)
        if at is None:
            at = next((i for i, l in enumerate(lines) if re.match(r"^  en:", l)), 0)
        lines[at + 1:at + 1] = rendered

    while lines and not lines[-1].strip():
        lines.pop()
    for field in ("defs", "refs", "see"):
        if field in touched:
            lines += _render(field, entry[field])
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="실제로 쓴다 (기본은 dry-run)")
    ap.add_argument("--threshold", type=float, default=THRESHOLD)
    ap.add_argument("--review", type=Path, help="판단이 필요한 쌍을 이 파일에 쓴다")
    ap.add_argument("--force-merge", type=Path,
                    help="`keep_id<TAB>drop_id` 목록을 후보 여부와 무관하게 합친다. "
                         "정의 글이 서로 달라 유사도 후보에 안 잡히는 이형용")
    ap.add_argument("--decisions", type=Path,
                    help="`keep_id<TAB>drop_id` 목록. 규칙이 review 로 미룬 쌍을 "
                         "사람(또는 모델)이 읽고 내린 판정이며, 규칙보다 우선한다")
    args = ap.parse_args()

    data = load()
    terms = [t for group in data.values() for t in group]
    # 한 항목이 같은 글을 defs 에 두 번 적어 두면 그 묶음에 두 번 들어가고,
    # 자기 자신과 짝이 되어 제가 저를 접어 삼킨다. 묶음마다 한 번씩만 담는다.
    by_url = collections.defaultdict(list)
    for t in terms:
        for url in set(def_urls(t)):
            by_url[url].append(t)

    pairs, seen = [], set()
    for group in by_url.values():
        for i in range(len(group)):
            for j in range(i + 1, len(group)):
                a, b = group[i], group[j]
                if a is b:
                    continue
                key = tuple(sorted([a.get("id", ""), b.get("id", "")]))
                if key in seen:
                    continue
                en, ko = sim(a.get("en"), b.get("en")), sim(a.get("ko"), b.get("ko"))
                best = max([x for x in (en, ko) if x is not None], default=None)
                if best is None or best < args.threshold:
                    continue
                seen.add(key)
                pairs.append((classify(a, b, en, ko), best, en, ko, a, b))

    # 명시 판정은 규칙을 덮는다. 규칙이 자동으로 정한 쌍은 그대로 두고, review 로
    # 미뤄 둔 쌍 중 목록에 있는 것만 끌어올린다.
    decided: dict[tuple[str, str], tuple[str, str]] = {}
    if args.decisions:
        for line in args.decisions.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            keep_id, drop_id = [x.strip() for x in line.split("\t")]
            decided[tuple(sorted([keep_id, drop_id]))] = (keep_id, drop_id)
    if decided:
        promoted = []
        for idx, (kind, best, en, ko, a_, b_) in enumerate(pairs):
            key = tuple(sorted([a_.get("id", ""), b_.get("id", "")]))
            if kind == "review" and key in decided:
                pairs[idx] = ("decided", best, en, ko, a_, b_)
                promoted.append(key)
        missing = set(decided) - set(promoted)
        if missing:
            print(f"판정 목록에 있으나 후보에 없는 쌍 {len(missing)}건: "
                  + ", ".join("/".join(k) for k in sorted(missing)[:5]))

    if args.force_merge:
        index = {t.get("id"): t for t in terms}
        for line in args.force_merge.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            keep_id, drop_id = [x.strip() for x in line.split("\t")]
            keep, drop = index.get(keep_id), index.get(drop_id)
            if keep is None or drop is None:
                print(f"없는 id: {keep_id if keep is None else drop_id}")
                continue
            pairs.append(("decided", 1.0, None, None, keep, drop))
            decided[tuple(sorted([keep_id, drop_id]))] = (keep_id, drop_id)

    buckets = collections.Counter(p[0] for p in pairs)
    print(f"유사도 ≥ {args.threshold} 쌍 {len(pairs)}건 — "
          + " · ".join(f"{k} {v}" for k, v in sorted(buckets.items())))

    # 한 항목이 여러 쌍에 걸릴 수 있다. 접힌 항목은 다시 접지 않는다.
    dropped: set[int] = set()
    changes = []
    for kind, best, en, ko, a, b in pairs:
        if kind == "review":
            continue
        if id(a) in dropped or id(b) in dropped:
            continue
        if kind == "decided":
            keep_id, _ = decided[tuple(sorted([a.get("id", ""), b.get("id", "")]))]
            keep, drop = (a, b) if a.get("id") == keep_id else (b, a)
        else:
            keep, drop = winner(kind, a, b)
        notes, touched = fold(keep, drop)
        dropped.add(id(drop))
        changes.append((kind, best, keep, drop, notes, touched))

    for kind, best, keep, drop, notes, _ in sorted(changes, key=lambda c: (c[0], c[3].get("en") or "")):
        print(f"\n[{kind}] {best:.2f}  남김 {keep.get('en')!r} / {keep.get('ko')!r}")
        print(f"          접음 {drop.get('en')!r} / {drop.get('ko')!r}")
        for n in notes:
            print(f"            → {n}")
    print(f"\n항목 {len(terms)} → {len(terms) - len(dropped)} ({len(dropped)}건 접힘)")

    if args.review:
        lines = ["# 판단이 필요한 중복 후보",
                 "",
                 "문자열로는 굴절 변형과 구별되지 않지만 뜻이 다를 수 있는 쌍이다.",
                 "한국어 라벨만 같고 실제로는 다른 개념인 경우가 여기 섞여 있다",
                 "(`coequalizer`/`cokernel` 이 둘 다 '여핵', `disjoint`/`relatively prime`",
                 "이 둘 다 '서로소'). 합칠 것만 골라 표시해 주면 그대로 반영한다.",
                 ""]
        for kind, best, en, ko, a, b in sorted(
                [p for p in pairs if p[0] == "review"], key=lambda p: -p[1]):
            f = lambda v: f"{v:.2f}" if v is not None else "  — "
            lines.append(f"- [ ] en {f(en)} · ko {f(ko)}")
            lines.append(f"      {a.get('en')!r} / {a.get('ko')!r}")
            lines.append(f"      {b.get('en')!r} / {b.get('ko')!r}")
            lines.append(f"      정의: {', '.join(sorted(set(def_urls(a)) | set(def_urls(b))))}")
            lines.append("")
        args.review.write_text("\n".join(lines), encoding="utf-8")
        print(f"판단 필요 {buckets['review']}건 → {args.review}")

    if not args.apply:
        print("\n(dry-run — 쓰지 않았다. 반영하려면 --apply)")
        return 0

    # 쓰기는 terms_common 의 포맷 보존 수술기로 한다. yaml.dump 재직렬화는 헤더
    # 주석과 기존 인용 스타일을 통째로 날린다 (terms_common 의 같은 주석 참조).
    text = TERMS.read_text(encoding="utf-8")
    header, groups = tc.split_file(text)
    drop_ids = {t.get("id") for t in terms if id(t) in dropped}
    # 접힌 항목을 가리키던 `see:` 참조를 남은 쪽으로 돌린다. 안 하면 terms_lint 가
    # "see → 항목이 없음" 으로 잡는다 — 실제로 색인에서 끊긴 링크가 된다.
    remap = {drop.get("id"): keep.get("id") for _, _, keep, drop, _, _ in changes}
    edits = {t.get("id"): (t, touched) for _, _, t, _, _, touched in changes}

    removed = 0
    for letter, chunks in groups.items():
        kept = []
        for chunk in chunks:
            cid = tc.chunk_id(chunk)
            if cid in drop_ids:
                removed += 1
                continue
            edit = edits.get(cid)
            chunk = rewrite_chunk(chunk, *edit) if edit else chunk
            for old, new in remap.items():
                if old and new:
                    chunk = re.sub(rf"^(\s+id: ){re.escape(old)}$", rf"\g<1>{new}",
                                   chunk, flags=re.M)
            kept.append(chunk)
        groups[letter] = kept

    TERMS.write_text(tc.join_file(header, groups), encoding="utf-8")
    print(f"\n{TERMS} 갱신 — 항목 {removed}건 접힘")
    return 0


if __name__ == "__main__":
    sys.exit(main())
