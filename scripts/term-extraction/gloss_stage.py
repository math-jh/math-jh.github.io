#!/usr/bin/env python3
"""gloss_stage — 정의 박스 안 병기 없는 영어 이탤릭에 한국어 병기를 붙이는 상시 단계.

term_extract_worker의 stage 1.5로 호출된다 (2026-07-21 배선, 일회성 백필은
gloss_backfill.py). 정책 (사용자 룰링 확정):

- terms.yml에 이미 있는 용어의 무병기 이탤릭 = **의도적 재사용** → 건드리지 않음.
- 색인에 없는 신규 용어만 병기 대상. 병기는 신뢰 소스에서만 가져온다:
  KMS 수학용어집 exact 단일 → 자동, exact 복수 → 워커가 haiku로 후보 안에서 선택,
  위키(langlink)만 있거나 무소스 → 리뷰 큐 (임의 번역 절대 금지 — '양근' 사고 전례).
- 생략 확정 용어는 gloss_skip.yml, 리뷰 제안 이력은 gloss_pending.json에 기록해
  같은 용어를 매 틱 재제안하지 않는다.

캐시(kms_cache.json/wiki_cache.json)는 gloss_backfill.py와 공유하며 포맷 계약:
  kms:  {"<용어소문자>": {"ts": iso, "candidates": [ko, ...]}}   (부정 캐시 포함)
  wiki: {"<용어소문자>": {"ts": iso, "title_en": str|null, "ko_title": str|null}}
쓰기는 항상 read-merge-write (백필과 동시 실행 대비).
"""
from __future__ import annotations

import json
import os
import re
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
# 테스트용 오버라이드 — 실환경에선 미설정 (캐시·pending은 SCRIPT_DIR에)
_STATE_DIR = Path(os.environ.get("GLOSS_STATE_DIR", str(SCRIPT_DIR)))
KMS_CACHE = _STATE_DIR / "kms_cache.json"
WIKI_CACHE = _STATE_DIR / "wiki_cache.json"
PENDING_PATH = _STATE_DIR / "gloss_pending.json"
SKIP_PATH = SCRIPT_DIR / "gloss_skip.yml"  # 사용자 편집 파일 — 항상 repo 고정

_UA = {"User-Agent": "Mozilla/5.0 (math-jh blog term tooling)"}
_BOX_RE = re.compile(r"^(::: (?:정의|[Dd]efinition)\b[^\n]*)\n(.*?)^:::[ \t]*$",
                     re.M | re.S)
_ITALIC_RE = re.compile(r"(?<!\*)\*([A-Za-z][^*<\n]{1,60}?)\*(?!\*)")
_DERIVED_BOX_RE = re.compile(r"^::: 정의[ \t]+(\d+)")
_EXPLICIT_ID_RE = re.compile(r"\{#([^}]+)\}")


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ── 탐지 ────────────────────────────────────────────────────────────────────

def _mask(s: str) -> str:
    s = re.sub(r"\$\$.*?\$\$", lambda m: " " * len(m.group(0)), s, flags=re.S)
    s = re.sub(r"(?<!\\)\$[^$\n]*(?<!\\)\$", lambda m: " " * len(m.group(0)), s)
    return re.sub(r"`[^`\n]*`", lambda m: " " * len(m.group(0)), s)


def detect_unglossed(text: str) -> list[dict]:
    """raw 파일 텍스트에서 (용어, 박스 span, 박스 anchor) 목록.

    같은 용어가 한 글에 여러 번이면 첫 박스만. `<sub>`가 이미 붙은 이탤릭과
    수식·코드 안은 제외."""
    out, seen = [], set()
    for bm in _BOX_RE.finditer(text):
        opener, inner = bm.group(1), bm.group(2)
        anchor = None
        me = _EXPLICIT_ID_RE.search(opener)
        md = _DERIVED_BOX_RE.match(opener)
        if me:
            anchor = me.group(1)
        elif md:
            anchor = "def" + md.group(1)
        masked = _mask(inner)
        for im in _ITALIC_RE.finditer(masked):
            term = im.group(1).strip()
            if not term or "<sub>" in inner[im.start():im.end() + 20]:
                continue
            key = term.lower()
            if key in seen:
                continue
            # 원문에 정확히 *term*<sub>… 형태로 이미 병기됐으면 제외
            if f"*{term}<sub>" in inner:
                continue
            seen.add(key)
            out.append({"term": term, "box_start": bm.start(),
                        "box_end": bm.end(), "anchor": anchor})
    return out


# ── 캐시 (read-merge-write) ─────────────────────────────────────────────────

def _load(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def _merge_save(path: Path, key: str, value: dict) -> None:
    cur = _load(path)
    cur[key] = value
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(cur, ensure_ascii=False, indent=1),
                   encoding="utf-8")
    tmp.replace(path)


# ── 소스 조회 ───────────────────────────────────────────────────────────────

def kms_lookup(term: str, timeout: int = 10) -> list[str]:
    """KMS 수학용어집 exact-match 한글 후보. 실패는 예외가 아니라 [] — 단
    네트워크 실패는 캐시하지 않는다 (다음 틱 재시도)."""
    key = term.lower()
    cache = _load(KMS_CACHE)
    if key in cache:
        return cache[key].get("candidates", [])
    cands: list[str] = []
    try:
        for start in (0, 30, 60):
            url = ("https://www.kms.or.kr/mathdict/list.html"
                   f"?start={start}&sort=ename&key=ename&keyword="
                   + urllib.parse.quote(term))
            req = urllib.request.Request(url, headers=_UA)
            h = urllib.request.urlopen(req, timeout=timeout).read().decode(
                "utf-8", "replace")
            rows = re.findall(r"<tr[^>]*>(.*?)</tr>", h, re.S)
            page = []
            for r in rows:
                cells = [re.sub(r"<[^>]+>", "", c).strip()
                         for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", r, re.S)]
                if len(cells) == 2 and cells[0] != "영문명":
                    page.append(cells)
            if not page:
                break
            for en, ko in page:
                if en.lower() == key:
                    cands += [c.strip() for c in ko.split(",") if c.strip()]
            time.sleep(0.4)
    except OSError:
        return []  # 네트워크 실패 — 캐시 없이 빈손 (재시도 여지)
    _merge_save(KMS_CACHE, key, {"ts": _now(), "candidates": cands})
    return cands


def wiki_ko_title(term: str, timeout: int = 10) -> str | None:
    key = term.lower()
    cache = _load(WIKI_CACHE)
    if key in cache:
        return cache[key].get("ko_title")

    def _api(params: dict) -> dict:
        url = "https://en.wikipedia.org/w/api.php?" + urllib.parse.urlencode(
            {**params, "format": "json"})
        req = urllib.request.Request(url, headers=_UA)
        return json.loads(urllib.request.urlopen(req, timeout=timeout).read())

    try:
        title_en, ko = None, None
        d = _api({"action": "query", "titles": term,
                  "prop": "langlinks", "lllang": "ko", "redirects": 1})
        pages = (d.get("query") or {}).get("pages") or {}
        for pid, p in pages.items():
            if pid != "-1":
                title_en = p.get("title")
                for ll in p.get("langlinks") or []:
                    ko = ll.get("*")
        if title_en is None:
            s = _api({"action": "query", "list": "search",
                      "srsearch": term, "srlimit": 1})
            hits = ((s.get("query") or {}).get("search")) or []
            if hits:
                d = _api({"action": "query", "titles": hits[0]["title"],
                          "prop": "langlinks", "lllang": "ko", "redirects": 1})
                for pid, p in ((d.get("query") or {}).get("pages") or {}).items():
                    if pid != "-1":
                        title_en = p.get("title")
                        for ll in p.get("langlinks") or []:
                            ko = ll.get("*")
    except OSError:
        return None  # 네트워크 실패 — 캐시하지 않음
    _merge_save(WIKI_CACHE, key, {"ts": _now(), "title_en": title_en,
                                  "ko_title": ko})
    return ko


# ── skip/pending ────────────────────────────────────────────────────────────

def skip_terms() -> set[str]:
    """gloss_skip.yml — `- 용어` 목록 (사용자가 '병기 생략 확정'한 것)."""
    try:
        import yaml
        d = yaml.safe_load(SKIP_PATH.read_text(encoding="utf-8")) or {}
        return {str(t).lower() for t in (d.get("skip") or [])}
    except (OSError, ValueError):
        return set()


def pending() -> dict:
    return _load(PENDING_PATH)


def mark_pending(term: str, reason: str) -> None:
    _merge_save(PENDING_PATH, term.lower(), {"ts": _now(), "reason": reason})


# ── 판정 + 적용 ─────────────────────────────────────────────────────────────

def decide(term: str) -> tuple[str, object]:
    """('auto', gloss) | ('pick', [후보…]) | ('review', 사유문자열)."""
    cands = kms_lookup(term)
    if len(cands) == 1:
        return "auto", cands[0]
    if len(cands) > 1:
        return "pick", cands
    ko = wiki_ko_title(term)
    if ko:
        return "review", f"위키 ko 문서 '{ko}' — 병기형 도출 필요"
    return "review", "소스 없음 (KMS exact ✗, 위키 ko ✗)"


def apply_gloss(text: str, occ: dict, gloss: str) -> str | None:
    """occ의 박스 span 안 첫 `*term*`에 <sub> 병기. 실패·불변이면 None.

    membership 강제는 호출자 몫이 아니라 여기서도 방어: gloss에 한글이
    없으면 거부한다 (임의 영문/빈 병기 방지)."""
    if not re.search(r"[가-힣]", gloss):
        return None
    box = text[occ["box_start"]:occ["box_end"]]
    needle = f"*{occ['term']}*"
    if needle not in box or f"*{occ['term']}<sub>" in box:
        return None
    new_box = box.replace(needle, f"*{occ['term']}<sub>{gloss}</sub>*", 1)
    new_text = text[:occ["box_start"]] + new_box + text[occ["box_end"]:]
    # 안전 검증: $ 개수 불변, 길이 증가량 = 병기 문자열 길이
    if new_text.count("$") != text.count("$"):
        return None
    if len(new_text) - len(text) != len(f"<sub>{gloss}</sub>"):
        return None
    return new_text
