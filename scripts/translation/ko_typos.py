#!/usr/bin/env python3
"""KO-TYPOS 파싱 — 검증 verdict 에서 "KO 원문이 틀렸다"는 지적만 뽑는 규칙.

translate_worker(워커)와 scripts/dashboard/server.py(대시보드)가 **같은 모듈을**
쓴다. 규칙을 양쪽에 복제하면 두 목록이 조용히 갈라진다 — 2026-08-15 실측으로
대시보드판에는 legacy fallback 이 없어 워커가 보는 8건 중 1건만 보였다(나머지 7건은
어디에도 안 뜬 채 묻혀 있었고, 그중 다수가 진짜 KO 오타였다).

대시보드는 venv 없이 /usr/bin/python3 로 도므로 이 모듈은 **표준 라이브러리만**
쓴다 (index_ranking 과 같은 제약). yaml·md_lint 같은 워커 전용 의존성을 여기에
들이면 대시보드 쪽 import 가 조용히 실패하고(try/except) 지적이 빈 목록이 된다.
"""
import re

# The verifier is asked (VERIFY_SEM_INSTRUCTIONS) to list errors it found in the
# *Korean* under a KO-TYPOS heading. Those reports used to be thrown away: they
# arrive attached to a SAFE verdict (the EN is fine — it is the KO that is wrong),
# and the telegram policy suppresses SAFE. On 2026-07-13 a sweep of the stored
# verdicts found 19 posts with such reports, 16 of them never surfaced, and
# source-checking them turned up 13 real KO errors (\cap for \cup in Seifert-van
# Kampen, \mathbb{2} for \mathbb{K}, varprojlim for varinjlim, "infumum", …).
# So parse them out and always report, independently of the verdict.
_KO_TYPO_HEAD_RE = re.compile(r"^\s*KO-TYPOS\s*:?\s*$", re.M)
# Fallback for verdicts written before the KO-TYPOS section existed, where the
# report is buried in a FINDINGS line.
_KO_TYPO_INLINE_RE = re.compile(
    r"\b(typos?"                                    # plural too: "apparent typos in ..."
    r"|corrects?\s+(?:an?\s+)?(?:evident\s+|apparent\s+|minor\s+)?(?:typos?|errors?)"
    r"|errors?\s+in\s+the\s+Korean"
    r"|Korean\s+(?:source\s+)?(?:has|contains)\s+(?:a\s+)?"
    r"(?:genuine\s+)?(?:mathematical\s+)?(?:errors?|typos?))\b", re.I)

# "(none detected)" / "(none found)" / "None detected." 류의 빈 목록 마커.
_KO_TYPO_NONE_RE = re.compile(r"^\(?\s*none\b[^()]*\)?\s*\.?$", re.I)


def extract_ko_typos(verdict_text: str) -> list:
    """Errors the verifier spotted in the KO source. Reported whether the verdict
    was safe or lossy — a KO typo is not an EN defect, so it never shows up as
    'lossy', which is exactly why these went unnoticed for so long.

    KO-TYPOS 섹션 헤더가 있으면 그 섹션만 믿는다 — 비어 있어도 legacy
    fallback 으로 넘어가지 않는다. 예전엔 빈 섹션이 fallback 을 타면서
    `\\btypos?\\b` 가 "KO-TYPOS:" 헤더 자체에 매치돼, 오타 0건이
    "FLAGGED — 1 ko-typo"(내용은 헤더 문자열)로 둔갑했다 (2026-07-22
    로그 리뷰에서 확인 — 최근 플래그 8건 중 7건이 이 오탐)."""
    if not verdict_text:
        return []
    m = _KO_TYPO_HEAD_RE.search(verdict_text)
    if m:
        out = []
        for line in verdict_text[m.end():].splitlines():
            s = line.strip()
            if not s:
                continue
            if not s.startswith("-"):      # next section began
                break
            item = s.lstrip("- ").strip()
            if item and not _KO_TYPO_NONE_RE.match(item):
                out.append(item)
        return out
    # Legacy / narrated form (KO-TYPOS 섹션이 아예 없던 옛 verdict 전용).
    return [ln.strip().lstrip("- ").strip()
            for ln in verdict_text.splitlines() if _KO_TYPO_INLINE_RE.search(ln)]
