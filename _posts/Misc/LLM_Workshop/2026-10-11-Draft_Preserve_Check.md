---

title: "개정 초안이 원문을 건드렸는지 블록 단위로 세기"
excerpt: "개정 초안이 원본 글의 문단을 글자 단위로 보존했는지 에이전트에게 묻지 않고, 빈 줄 단위 블록 집합 차로 세는 스크립트와, relabel을 먼저 적용하는 두 단계 치환"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/draft_preserve_check

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-10-11
weight: 58

---

관련 파일: [`scripts/dev/draft_preserve_check.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/dev/draft_preserve_check.py), [`커밋 a8dede59`](https://github.com/math-jh/math-jh.github.io/commit/a8dede59), [`_posts/Math/Gromov_Witten_Theory/CLAUDE.md`](https://github.com/math-jh/math-jh.github.io/blob/main/_posts/Math/Gromov_Witten_Theory/CLAUDE.md)
{: .notice--info}

Gromov–Witten 스트림에는 새 개념을 배우는 글을 개정하는 절차가 생겼다. 초안을 쓰는 에이전트가 사용자의 기존 문단을 어디까지 건드렸는지가 그 절차의 마지막 관문이고, 이 스크립트는 그 관문이다. 기존 글을 통째로 다시 쓴 초안이 나오면 사용자는 어디가 새 글이고 어디가 옛 글인지 알 수 없다. 그러면 검토할 범위가 글 전체로 늘어난다.

개정 절차를 정리한 `brief.md`에는 이 관문이 한 줄로만 있었다.

> 기존 부분이 글자 단위로 보존됐는지는 에이전트에게 맡기지 않고 diff 스크립트로 확인한다.

이 절차의 다른 단계를 보면 이 줄이 왜 에이전트 밖에 있는지 알 수 있다. 핵심 목록을 세우는 쪽도, 초안을 검증하는 쪽도 에이전트이고, 그 에이전트에게 "원문이 그대로인지 봐 달라"고 하면 읽고 그럴듯하다고 답한다. 글자가 같은지는 읽어서 아는 것이 아니라 비교해서 아는 것이므로, 이 한 단계만 비교 연산으로 꺼냈다. 이 `brief.md`는 Raspberry Pi에만 제한적으로 접근하는 Claude Opus가 사용자의 문제의식을 받아 쓴 것이어서 사용자가 실제와 맞지 않는 데가 있을 수 있다고 미리 적어 두었는데, 이 줄은 스크립트가 생긴 뒤 `CLAUDE.md`의 7번 항목에서 스크립트 경로를 얻었다.

## 줄 단위가 아니라 빈 줄 단위

원본과 초안을 줄 단위 `diff`로 비교하면 개정에서 단락이 하나 늘어날 때마다 뒤쪽 전체가 밀려서 다르게 보인다. 이 글 형식에서는 정리 박스가 `:::` 펜스로 이어진 여러 줄이고, 디스플레이 수식도 앞뒤에 빈 줄을 둔 독립 단락이어서, 변경의 단위는 줄이 아니라 빈 줄로 끊긴 덩어리다. 그래서 양쪽을 블록으로 자르고 집합 차를 낸다.

```python
def blocks(text: str) -> list[tuple[int, str]]:
    out, cur, start = [], [], 0
    lines = text.split("\n")
    for i, line in enumerate(lines + [""]):
        if line.strip() == "":
            if cur:
                out.append((start, "\n".join(l.rstrip() for l in cur)))
                cur = []
        else:
            if not cur:
                start = i + 1
            cur.append(line)
    return out
```
{: data-filename="scripts/dev/draft_preserve_check.py"}

`lines + [""]`는 파일이 빈 줄 없이 끝나도 마지막 블록을 내보내기 위한 것이다. 블록의 내용은 행 끝 공백만 지운 문자열이고, 줄번호는 목록에서 블록을 찾아가는 용도로만 들고 간다. 비교는 이렇게 한다.

```python
oset, dset = {b for _, b in ob}, {b for _, b in db}
only_o = [(n, b) for n, b in ob if b not in dset]
only_d = [(n, b) for n, b in db if b not in oset]
```
{: data-filename="scripts/dev/draft_preserve_check.py"}

출력은 두 목록이다. 원본에만 있는 블록은 초안이 지우거나 다시 쓴 문단이고, 초안에만 있는 블록은 새로 쓴 문단이거나 원본 문단을 고친 결과다. CLAUDE.md는 후자를 "곧 검증 범위"라고 부른다. 검증 에이전트에게 맡기는 범위를 사람이 기억에 의존해 적지 않고, 이 목록으로 못 박기 위해서다.

## 초안은 본문만, 생략 주석은 걷고

초안 파일(`notes/pot-revision/draft.md`)은 머리말과 포팅 순서, 본문, 끝의 생략 장부 표로 이루어져 있다. 비교 대상은 본문뿐이므로 `<!-- ==== 본문 시작 ==== -->`와 `본문 끝` 마커 사이만 잘라 낸다. 마커 정규식은 `=`의 개수에 무관하게 걸리도록 `=+`로 썼다. 마커가 없으면 조용히 전체를 비교하지 않고 `sys.exit`으로 멈춘다.

본문 안에는 `<!-- 생략 L3: … -->` 주석이 흩어져 있다. 생략 장부의 번호와 이어지는 표식이고 렌더되지 않지만, 원본에는 없으므로 그대로 두면 그 주석이 붙은 블록이 전부 "새 블록"이 된다. 그래서 비교 전에 주석을 지운다.

```python
OMIT = re.compile(r"\s*<!--\s*생략.*?-->", re.S)
draft = OMIT.sub("", draft_body(Path(a.draft).read_text()))
```
{: data-filename="scripts/dev/draft_preserve_check.py"}

앞의 `\s*`까지 같이 지우는 것은 주석이 줄 끝에 붙어 있을 때 남는 공백이 블록 내용을 달라지게 하기 때문이다. 이 정규식은 주석 제거로 두 블록이 하나로 붙는 경우를 따로 다루지 않는다. 주석이 빈 줄 사이에 홀로 놓인 보통의 경우에는 그 줄이 사라져도 단락 경계는 유지된다.

## relabel을 원본 쪽에 먼저 적용하기

개정 초안은 새 박스를 끼워 넣으므로 기존 박스의 번호가 밀린다. 이 글이 그랬다. 정의 2는 3으로, 명제 3·4는 11·12로, 예시 5·6은 13·14로 바뀐다. 내용은 그대로여도 `::: 명제 3`이 `::: 명제 11`로 바뀐 블록은 글자가 다르다. 번호 이동을 그대로 두면 원문을 한 글자도 안 고친 박스가 전부 "바뀐 블록"으로 나와서 신호가 번호 변동에 묻힌다.

해결은 원본 쪽에 같은 번호 이동을 미리 적용하는 것이다. 포팅 순서가 실제로는 `relabel.py shift`를 두 번 돌리므로, 그 결과와 같은 상태로 원본을 옮겨 놓고 비교하는 셈이다. 대응은 `--map prop3=prop11,def2=def3,...`로 준다.

```python
def apply_map(text: str, mapping: dict[str, str]) -> str:
    # 두 단계 치환으로 prop3→prop11, prop11→prop12 같은 연쇄 충돌을 피한다.
    tokens = {}
    for i, (old, new) in enumerate(mapping.items()):
        ...
        tok = f"\x00{i}\x00"
        tokens[tok] = (new, ko_new)
        # 글 안 링크: [명제 3](#prop3)
        text = re.sub(rf"\[{re.escape(ko_old)}\]\(#{old}\)", f"[{tok}K](#{tok}A)", text)
        # 정리 박스 머리: ::: 명제 3 ...
        text = re.sub(rf"(?m)^(:::\s+){re.escape(ko_old)}(?=\s|$)", rf"\g<1>{tok}K", text)
    for tok, (new, ko_new) in tokens.items():
        text = text.replace(f"{tok}K", ko_new).replace(f"{tok}A", new)
    return text
```
{: data-filename="scripts/dev/draft_preserve_check.py"}

두 단계로 나눈 이유는 주석에 있다. 이 글에서는 `prop4=prop12`와 `prop3=prop11`이 같은 map에 있지만, 일반적으로 이동의 이전 값과 새 값이 서로 겹칠 수 있다. 앞에서부터 바로 치환하면 방금 바꾼 `prop11`을 다음 규칙이 다시 집어 간다. 그래서 먼저 임시 토큰(`\x00`로 감싼 번호)으로 바꿔 두고, 전부 끝난 뒤에 토큰을 최종 값으로 푼다.

치환 대상은 일부러 두 자리뿐이다. 글 안의 링크 `[명제 3](#prop3)`와 정리 박스 머리 `::: 명제 3`. 다른 글을 가리키는 링크는 `[...](/ko/.../moduli_of_stable_maps#prop4)`처럼 앵커 앞에 경로가 있어서 첫 패턴에 걸리지 않는다. 그 앵커는 그 글의 번호이므로 이 글의 relabel과 무관하다. `kind` 접두어는 `def`·`prop`·`thm`·`lem`·`cor`·`ex`·`rmk` 일곱 개를 알며, 모르는 접두어가 오면 map을 해석하지 못한다고 하고 멈춘다.

## 신고 목록과 종료 코드

초안을 쓴 쪽이 "이 블록은 내가 새로 쓴 것"이라고 신고한 목록이 있으면 `--declared`로 넘긴다. 한 줄에 블록 첫머리 문자열 하나씩이다. 초안에만 있는 블록 중 어느 줄로도 시작하지 않는 것은 `← 신고 없음`을 달고, 하나라도 있으면 종료 코드 1을 돌려준다. 신고 목록이 없을 때는 항상 0이다. 이 모드는 자기 보고와 실제 변경을 교차시키려는 것이지만, 이 글을 쓰는 시점의 `CLAUDE.md`는 이 옵션을 부르지 않는다.

## 실제 글에 돌려 보기

개정 전 판본(`774bae44`)을 풀어 놓고, 지금 `notes/pot-revision/draft.md`와 대조했다.

```
python3 scripts/dev/draft_preserve_check.py orig.md notes/pot-revision/draft.md \
    --map def2=def3,prop3=prop11,prop4=prop12,ex5=ex13,ex6=ex14,prop7=prop15,ex8=ex16

원본 블록 123개 중 보존 115개, 초안 블록 193개 중 새 블록 78개
```

`--map` 없이 돌리면 보존이 101개, 새 블록이 92개다. 둘의 차이 14블록이 번호만 달라진 박스와 그 박스를 가리키는 링크 문단이다. 원본에만 있는 8블록은 정의 뒤 한 문단과 가상 기본류를 정의하던 구간 여섯 블록, 그리고 참고문헌 블록이다.

이 마지막 항목은 이 스크립트의 한계를 보여 준다. 참고문헌 블록은 빈 줄 없이 이어진 한 덩어리인데, 초안이 거기에 `[KKP]` 한 줄을 덧붙여서 블록 전체가 "원본에만 있음"과 "초안에만 있음"에 한 번씩 올랐다. 블록 단위 비교는 한 줄 추가를 한 덩어리의 교체로 보고한다. 그 덕에 참고문헌처럼 손대지 말아야 할 자리가 건드려진 것은 바로 드러나지만, 어디가 바뀌었는지는 따로 `diff`로 열어 봐야 한다.

반대편의 한계도 있다. 비교가 집합 연산이라 블록의 **순서**와 **중복 횟수**는 보지 않는다. 원본의 두 단락을 맞바꿔도, 같은 문단을 두 번 붙여 넣어도 이 스크립트는 "전부 보존"이라고 한다. 이 관문이 잡으려는 것은 원문 문단의 조용한 변형이므로 지금은 이 정도로 두었고, 순서가 문제 되는 개정이 생기면 그때 블록 번호열의 최장 공통 부분수열 같은 것을 얹을 일이다.
