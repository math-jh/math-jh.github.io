---

title: "감사 규약과 audit.json"
excerpt: "감사 산출물을 블록 하나당 항목 하나라는 규칙의 audit.json으로 고정하고, 8월 노트를 옮기는 변환기와 넘기기 전에 돌리는 검증기를 붙인 일"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/audit_protocol

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-08-17

weight: 41
group: admin

---

관련 파일: [`scripts/audit/AUDIT-PROTOCOL.md`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/audit/AUDIT-PROTOCOL.md), [`scripts/audit/export_audit_json.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/audit/export_audit_json.py), [`scripts/audit/validate_audit_json.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/audit/validate_audit_json.py)
{: .notice--info}

[판본 비교기](/ko/llm_workshop/version_comparator)가 호버 카드로 붙이는 감사 지적은, 8월 감사 때는 카테고리별 표와 두 벌의 반영 기록으로 흩어져 있었다. 비교기가 그 노트를 읽으려면 전용 파서가 필요했다. 다음 감사도 노트 형식이 다르면 파서를 또 짜야 한다는 뜻이고, 사용자는 그 반복을 여기서 끊자고 했다.

> 감사 과정을 우리가 하나의 워크플로우로, 고정된 워크플로우로 만들자는 건데 지금 사실 감사 노트가, 결과 노트가 어느 정도 포맷팅이 돼 있긴 한데 그게 사실 지금은 ad-hoc인거잖아. 그걸 형식을 고정하자는거야. 그리고 그 고정된 형식으로 출력된 json을 compare 페이지에서 선택하면 (혹은 슬러그로 매치해도 좋고) 지금처럼 hover가 되어 나타나도록. 이거를 별도 문서로 만들어야 다음 감사 돌릴 때 그걸 참고할 수 있겠지.

같은 자리에서 워킹트리 얘기도 나왔다. 8월 감사는 main 워킹트리에서 그대로 진행했다. 전후 스냅샷을 구워 비교했으므로 결과에는 문제가 없었지만, 그 사이 크론 워커의 커밋이 감사 변경과 섞여 비교기가 보는 "이후" 판본이 검토 중에도 계속 움직였다. `AUDIT-PROTOCOL.md`는 `git switch -c audit/<slug>`로 브랜치를 만들고 main은 건드리지 않는 것을 1번 규칙으로 적었다. 비교기는 `main ↔ audit/<slug>`로 보면 된다.

## 감사를 돌리는 모델에게 주는 지침

형식의 핵심은 **항목 하나가 블록 하나에 대응한다**는 것이다. "블록"은 조작적으로 정의된다. base 판본 그 파일에서 빈 줄로 끊긴 덩이 하나다. 문단·정리 박스·display 수식·목록·도식 태그·제목 줄이 각각 블록 하나이고, 정리 박스나 목록은 안의 문단·항목을 쪼개지 않고 통째로 하나로 센다. 한 블록에서 세 군데를 고쳤어도 항목은 하나이고, `summary` 안에 나열한다. 반대로 한 지적이 두 블록에 걸치면 항목을 둘로 쪼개고 같은 `group` 키로 묶는다.

이 단위는 비교기의 "미반영 의심" 판정이 기대는 곳이다. 비교기는 항목의 인용문으로 base 판본의 블록을 찾아 그 블록의 변경에 카드를 붙이고, `status`가 `applied`인데 그 블록에 변경이 하나도 없으면 반영되지 않은 지적으로 표시한다. 한 항목이 고친 줄과 함께 맥락으로 인용한 줄까지 가리키면, 고칠 필요가 없던 그 줄의 블록도 "안 고쳐졌다"고 잡힌다. 규약 문서의 실측으로는 8월 노트를 변환한 본에서 나온 의심 511건 중 307건이 여러 블록으로 쪼개진 항목에서 나왔다.

이 규칙을 지켜야 하는 쪽은 비교기가 아니라 **감사를 수행하는 모델**이라, 문서는 리뷰어용 형식 설명과 별개로 "6. 감사를 돌리는 쪽에 주는 지침" 절을 따로 뒀다. 이 절이 생긴 이유도 사용자 질문이었다.

> 응 그건 그렇고, 감사때 모델이 참고할 스펙에는 어떻게 작성하라 되어 있어?

당시엔 그런 스펙이 없었다. §6.2는 항목 하나를 쓰는 순서를 여섯 단계로 정한다. 블록을 고르고, 그 블록의 문장 하나를 원문 그대로 `quote`로 삼는 것이 앞의 두 단계다. 그 문장은 `:::`·`#`·`-`·`>`·Liquid 태그로 시작하는 줄에서는 고르지 말고, 글 안에서 유일할 만큼 길게(짧으면 두 문장까지) 잡는다. 마커로 시작하는 줄을 인용문으로 쓰지 말라는 제약은 취향이 아니라 실측에서 나왔다. 렌더된 본문에는 그런 마커가 남지 않으므로, 인용문에 섞이면 그 항목은 어느 블록에도 안 붙는다.

## 옛 노트를 규약으로 옮기는 변환기

규약을 문서로 남기는 것과, 이미 쌓인 8월 감사 노트를 그 규약에 맞게 바꾸는 것은 별개 작업이다.

> ㅇㅋ 지금 감사 결과들을 audit.json 형태로 돌려보는 작업은 좀... 힘들겠지? 그리고 audit.json은 여러 파일도 포함할 수 있을 것 같은데 그것도 지원해?

여러 파일은 지원한다. 글 여러 편은 `posts` 배열에 담고, 한 감사를 `audit.<무엇이든>.json` 여러 개로 나눠 내면 비교기가 폴더 이름을 slug로 삼아 합친다.

변환은 `export_audit_json.py`가 맡는다. 옛 노트는 `findings/<key>.md`(절 머리에 줄번호), `by-category/*.md`(카테고리별 정리 표), `applied/`·`applied2/`(1·2차 반영 기록) 세 갈래로 흩어져 있었는데, 여기엔 인용문이 없고 줄번호만 있다. 그래서 변환의 핵심은 base 판본의 그 줄을 `git show`로 실제로 읽어 인용문을 만드는 일이다.

```python
def paragraphs(lines: list[str]) -> list[tuple[int, int]]:
    out, start = [], None
    for i, ln in enumerate(lines, 1):
        if ln.strip():
            start = start or i
        elif start:
            out.append((start, i - 1))
            start = None
    if start:
        out.append((start, len(lines)))
    return out
```
{: data-filename="scripts/audit/export_audit_json.py · 일부 발췌, 문서 문자열 생략"}

`paragraphs()`는 base 판본의 줄을 위에서부터 읽으며, 비어 있지 않은 줄에서 덩이를 열고 빈 줄을 만나면 닫아 (시작 줄, 끝 줄)을 남긴다. 옛 노트의 줄번호들을 `block_of()`로 이 문단 목록에 매핑해, 같은 문단에 떨어지는 줄은 한 항목으로 합치고 다른 문단이면 `BUG-1.1`·`BUG-1.2`로 쪼개 `group`을 공유시킨다. §6.1의 "블록 하나당 항목 하나" 규칙을 사람이 아니라 이 스크립트가 강제하는 곳이다.

인용문 자체는 `quote_for()`가 뽑는다. 그 줄부터 아래로 네 줄까지 내려가며 첫 "내용" 줄을 찾고, 목록·인용·제목·각주 마커를 정규식으로 벗겨낸다.

{% raw %}
```python
_MARKER = re.compile(r"^(?:>\s*|[-*+]\s+|\d+[.)]\s+|#{1,6}\s+|\[\^[^\]]+\]:\s*)+")

def quote_for(lines: list[str], line_no: int) -> str:
    for i in range(line_no, min(line_no + 4, len(lines)) + 1):
        if not (1 <= i <= len(lines)):
            break
        raw = lines[i - 1].strip()
        if not raw or raw.startswith(":::") or raw.startswith("{%"):
            continue          # 여는 줄·Liquid 태그는 본문이 아니다
        text = _MARKER.sub("", raw).strip()
        if text:
            return text
    return ""
```
{: data-filename="scripts/audit/export_audit_json.py · 일부 발췌, 문서 문자열 생략"}
{% endraw %}

`:::` 여는 줄과 Liquid 태그로 시작하는 줄은 줄 전체가 표기라 벗길 것이 없으므로 건너뛰고 다음 줄로 내려간다. 내용이 있는 줄에서는 `_MARKER`가 줄 첫머리(`^`)의 마커만 지운다. `>\s*`는 인용, `[-*+]\s+`는 글머리표, `\d+[.)]\s+`는 `1.`·`1)` 같은 번호, `#{1,6}\s+`는 제목, `\[\^[^\]]+\]:\s*`는 `[^1]:` 꼴의 각주 정의다. 묶음 전체에 `+`가 붙어 있어 `> - `처럼 겹친 마커도 한 번에 벗겨진다.

규약 문서에 남은 실측으로는, 이 걸러내기 전 미매칭 803건 중 71%가 정의 박스나 정리 박스의 여는 줄(`:::`)이었고, 걷어내고 나니 91건으로 줄었다. `was`/`now`(실제로 바뀐 짧은 조각)는 옛 요약의 "A → B" 꼴에서만 건지는데, 화살표로 갈라 뽑은 왼쪽 조각이 40자 이하이고 base 파일에 실제로 있을 때만 채택한다. 산문에서 화살표 패턴이 우연히 걸리면 고치지도 않은 엉뚱한 조각이 `was`로 들어오고, 비교기는 그 조각이 수정 뒤에도 그대로 남아 있는 것을 보고 "미반영 의심"을 띄운다. 이 가드를 넣기 전 검증기 경고가 1,400건이었다.

## 인용문을 base 판본에 대 보는 검증기

`validate_audit_json.py`가 확인하는 것은 하나로 요약된다. **인용문이 base 판본의 그 파일에 정말로 그대로 있는가.** 비교기가 항목을 못 붙이는 사고는 전부 에러 없이 일어난다. 카드가 그냥 안 뜰 뿐이다. 그래서 넘기기 전에 기계로 확인한다. 대조는 base 원문과 인용문의 공백만 지우고 한다. §6.2가 인용문의 줄바꿈을 공백으로 접는 것은 허용하고 글자를 바꾸는 것은 금하므로, 공백을 지운 비교는 접힌 줄바꿈은 통과시키고 바뀐 글자는 잡는다.

```python
flat = norm(src)
...
hits = flat.count(norm(q))
if hits == 0:
    errors.append(...)
elif hits > 1 and not it.get("base_lines"):
    warns.append(...)
```
{: data-filename="scripts/audit/validate_audit_json.py · 일부 생략"}

인용문이 base에 없으면 오류, 여러 번 나오는데 `base_lines`가 없으면 경고다. 그 밖의 오류는 마커로 시작하는 인용문(§6.2가 금지한 그 패턴), `summary` 누락, `id` 중복, `status` 값 오타, 파일들 사이에서 `base_ref`가 갈리는 경우다. 마지막 것은 서로 다른 판본을 한 감사로 합치는 사고다. 파일 자체를 base 판본에서 못 찾을 때는 두 갈래로 나눈다. git이 추적하는 파일인데 그 판본에 없으면 오류, 애초에 버전 관리 밖(로컬 전용 카테고리)이면 경고로만 낮춘다. 인용문을 확인할 방법이 없을 뿐 감사 자체는 무효가 아니기 때문이다.

두 스크립트의 수명은 다르다. 변환기는 docstring에 적었듯 8월 노트만 겨눈 것이라 다음 감사가 처음부터 이 형식으로 나오면 필요 없고, 검증기는 규약 §6.5가 감사마다 넘기기 전에 돌려 오류 0을 만들라고 요구한다. 다음에 감사를 맡을 모델은 그게 나든 아니든 §6을 읽고 항목을 쓴 뒤, 검증기가 오류 0을 낼 때까지 인용문을 고치면 된다. 그 모델에게 설계할 일은 남아 있지 않다.
