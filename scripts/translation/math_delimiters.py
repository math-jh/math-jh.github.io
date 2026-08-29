"""수식 구분자 프로필 — KO/EN 번역쌍의 수식 구조가 같은지 재는 자.

**2026-07-13 이전과 정반대다.** 예전에는 이 모듈이 `$...$` → `$$...$$` 로 **승격**
시켰다. 블로그가 인라인 수식까지 전부 `$$...$$` 로 적었기 때문인데, 그 이유는
kramdown 이 `$...$` 를 수식으로 인식하지 못해 그 안의 `_`/`*`/`|`/`\\{` 를 마크다운으로
먹어치웠기 때문이다. 이제 `_plugins/kramdown_inline_math.rb` 가 kramdown 에게 single
`$...$` 도 수식으로 가르치므로, 인라인은 표준대로 `$...$`, 디스플레이는 `$$...$$` 다.

따라서 kimi 가 원래 하던 짓(인라인을 `$...$` 로 적는 것)이 이제 **정답**이고, 승격은
오히려 해가 된다. 남은 위험은 하나뿐이다: kimi 가 KO 의 **디스플레이** `$$...$$` 를
인라인 `$...$` 로 낮추는 것 (가운데 정렬 수식이 문장 속으로 들어가 버린다).

`math_profile` 은 그걸 잡기 위한 결정적 지표다. 수식 내용은 verbatim 보존이 원칙이므로
KO 와 EN 의 (`$$` 스팬 수, `$` 스팬 수) 는 정확히 같아야 한다. 어긋나면 구분자가
바뀐 것이다.
"""
import re

# 세지 않고 통째로 가리는 구간. `\1` 은 보호 태그 이름을 묶는다.
# `$$...$$` 를 통째로 가리므로 그 내부의 single `$` (\text{$k$}, \tag{$\ast$}) 는
# 인라인으로 오인되지 않는다.
#
# 주의(이중 SoT 감사 [3], 2026-07-22): 아래 _DISPLAY/_INLINE 은
# .agents/hooks/md_lint.py 의 _MATH_SPAN_RE 사본이 **아니다** — 저쪽은 "스팬
# 하나"를 훑는 스캐너(치환·마스킹용), 이쪽은 KO/EN 쌍의 구분자 **계수**용이라
# 의미론이 다르다(예: _INLINE 은 개행 허용). 같아 보여도 통합하지 말 것.
_CODE = re.compile(
    r"```.*?```"      # fenced code block
    r"|`[^`\n]*`",    # inline code
    re.DOTALL,
)
_DISPLAY = re.compile(r"\$\$.*?\$\$", re.DOTALL)
# 균형 잡힌 top-level 인라인 스팬. `(?!\$)` 로 `$$` 잔재를 물지 않는다.
_INLINE = re.compile(r"(?<!\\)\$(?!\$)[^$]*?(?<!\\)\$")


def math_profile(text: str) -> tuple[int, int]:
    """(디스플레이 `$$...$$` 스팬 수, 인라인 `$...$` 스팬 수).

    코드 블록·코드 스팬은 제외한다. `$$` 안의 single `$` 도 제외된다.
    """
    masked = _CODE.sub(lambda m: " " * len(m.group(0)), text)
    n_display = len(_DISPLAY.findall(masked))
    without_display = _DISPLAY.sub(lambda m: " " * len(m.group(0)), masked)
    n_inline = len(_INLINE.findall(without_display))
    return n_display, n_inline


def unbalanced_dollars(text: str) -> bool:
    """이스케이프 안 된 `$` 의 개수가 홀수면 수식 마크업이 깨진 것이다."""
    masked = _CODE.sub(lambda m: " " * len(m.group(0)), text)
    return len(re.findall(r"(?<!\\)\$", masked)) % 2 == 1


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == "--selftest":
        cases = [
            (r"a $x$ b", (0, 1)),
            (r"$$D$$ alone", (1, 0)),
            (r"map $$f\colon X\to Y$$ mix $g$", (1, 1)),
            # `$$` 안의 single `$` 는 인라인으로 세지 않는다 (문서화된 예외)
            (r"$$\Omega=\{\text{$k$-forms on $\mathbb{R}^n$}\}$$", (1, 0)),
            (r"$$0\to A\to B\to 0\tag{$\ast$}$$", (1, 0)),
            (r"see <cap>$x$</cap> then $z$", (0, 2)),
            (r"costs \$5 and $q$", (0, 1)),
            ("code `$x$` and $y$", (0, 1)),
            (r"$$A$$$$B$$", (2, 0)),
        ]
        ok = True
        for src, exp in cases:
            got = math_profile(src)
            if got != exp:
                ok = False
                print(f"FAIL\n  in : {src}\n  exp: {exp}\n  got: {got}")
            else:
                print(f"ok   profile {got}  {src}")
        for src, exp_bad in [(r"$$D$$ stray $ here", True), (r"clean $a$ and $$B$$", False)]:
            got = unbalanced_dollars(src)
            if got != exp_bad:
                ok = False
                print(f"FAIL unbalanced: {src!r} -> {got} (exp {exp_bad})")
            else:
                print(f"ok   unbal={got}  {src}")
        sys.exit(0 if ok else 1)

    print(math_profile(sys.stdin.read()))
