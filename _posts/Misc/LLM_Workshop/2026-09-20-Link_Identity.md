---

title: "링크 출현에 이름 붙이기"
excerpt: "의존성 판정이 끝났다는 표시(reviewed), 갈린 판정을 남기는 값(requires-review), 그리고 KO 링크와 그 번역을 잇는 불투명 식별자 data-lid까지, 링크 한 개가 판정을 받고 EN으로 넘어가는 경로를 정리한 일"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/link_identity

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-09-20
last_modified_at: 2026-09-25
weight: 53

---

관련 파일: [`scripts/dependency-classifier/dependency_classifier.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/dependency-classifier/dependency_classifier.py), [`scripts/translation/translate_worker.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/translation/translate_worker.py), [`scripts/translation/section_anchor_gate.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/translation/section_anchor_gate.py), [`scripts/dashboard/server.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/dashboard/server.py), [`scripts/lib/link_relations.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/lib/link_relations.py), [`_plugins/graph_data.rb`](https://github.com/math-jh/math-jh.github.io/blob/main/_plugins/graph_data.rb)
{: .notice--info}

[링크에 선수 관계 붙이기](/ko/llm_workshop/semantic_dependencies)에서 분류기는 링크마다 `data-relation`을 달았고, 재검토 패스가 1차 판정을 의심하도록 만들었다. 거기까지는 링크 하나를 판정하는 이야기였다. 이 글은 그 판정이 **어느 링크의 것인가**에 관한 이야기다. 같은 링크가 KO 글에 한 번, EN 번역에 한 번 있고, 분류기는 둘을 따로 판정했다. 값이 갈린 쌍이 수백 개 쌓이고 나서야 그 둘이 같은 링크라는 것을 기계가 알 방법이 없다는 사실이 드러났다.

## 판정이 끝났다는 표시

처음 손본 것은 판정의 상태였다. 재검토 패스는 1차와 2차가 갈리면 태그를 떼고 보류 원장에 거는 방식이었는데, 태그가 사라지니 사용자가 그 링크를 에디터에서 찾을 길이 없었다.

> classifier가 재검토시 충돌하면 IAL 태그를 떼도록 되어 있잖아, 그 부분은 data relation을 ambiguous 혹은 requires-review 정도로 넣어줘 (내가 IDE에서 ctrl+f로 찾기 편하게)

그래서 `bd3b2307`부터 갈린 링크는 값이 `requires-review`가 된다. 소비자들(그래프 빌더, 본문 선수 블록)은 `required|weak|forward` 세 값만 받는 정규식을 쓰므로 이 링크는 무분류와 똑같이 취급되고, 분류기 1차·재검토 어느 쪽도 이 값을 다시 집지 않는다. 판정은 사람이 검색해서 내린다.

반대쪽 끝, 즉 "이 링크는 다 봤다"는 표시는 `83f6d1ec`에서 생겼다. IAL 안의 빈 속성 `reviewed=""`다.

```python
REVIEWED_RE = re.compile(r'\breviewed\s*=\s*["\']["\']')

def mark_reviewed(text: str, links: list[Link]) -> str:
    ...
        replacement = ial[:-1].rstrip() + ' reviewed="" }'
```
{: data-filename="scripts/dependency-classifier/dependency_classifier.py"}

1차와 재검토가 일치하면 분류기가 이 마커를 찍고, 사람이 대시보드에서 판정하면 서버가 찍는다(`43200fe9`). 대시보드 쪽은 보류 목록을 고르면 그 글을 dev 서버 렌더 그대로 iframe에 띄우고 해당 링크를 강조한 뒤, 판정 버튼이 `POST /api/linkaudit/resolve`로 IAL 하나에 값과 마커를 같이 쓴다. 속성만 바뀐 글은 같은 화면의 커밋 버튼이 한 커밋으로 묶는데, 두 속성을 걷어낸 본문이 `HEAD`와 같은 글만 고른다. 본문 수정이 섞인 글은 사람이 따로 커밋하라는 뜻이다.

이 구간의 사소한 사고 하나. 재검토 프롬프트는 태그를 뗀 본문을 모델에 보내는데, 발췌를 자르는 오프셋은 태그를 떼기 전 원본에서 잰 값이었다. 뗀 태그 길이만큼 위치가 밀려서 모델은 엉뚱한 문단을 받았고, 판정 근거에 "근거 자료가 주어지지 않았다"고 적었다. 사용자가 그 문장을 보고 짚었다. `6544bdfd`는 태그를 뗀 본문에서 링크를 다시 읽어 자른다. 발췌를 못 받은 판정자가 정직하게 그렇다고 말한 것은 칭찬할 일이지만, 그 정직함을 읽은 것은 사람이었다.

## 내용에서 복원되지 않는 대응

KO와 EN을 합치자는 이야기는 보류 목록에서 시작됐다. 같은 글의 KO 판본과 EN 판본이 목록에서 떨어져 보였고, 붙여 놓고 보니 같은 링크에 KO는 `required`, EN은 `weak`인 쌍이 흔했다. 한 출현을 두 번 판단했으니 두 번 다른 답이 나오는 것은 자연스럽다.

문제는 "같은 링크"를 어떻게 아느냐였다. 대상 경로와 앵커, 링크 텍스트, 글 안에서의 순번 같은 재료로 짝을 지으려 하면 번역이 전부 흔든다. 번역은 문장 순서를 바꾸고, 링크 두 개를 하나로 합치기도 하고, 섹션 앵커는 글자 자체가 영어로 바뀐다. 원장이 쓰던 식별자 `sha1(path:ordinal:target:label)`도 같은 이유로 약했다. 사용자가 링크 텍스트를 고치는 순간 식별자가 바뀌어서 보류 항목이 `gone`으로 사라졌다.

사용자의 제안은 복원을 포기하는 쪽이었다.

> 음... 아니면 음... 어떤 해시값을 IAL 태그로 링크에 넣어주고, 그걸 기반으로 identify하는거 어때?

이어서 길이와 충돌을 물었다.

> 전역 id 부여하고, 네 말대로 난수는 난수인데 그 난수가 다르다는 걸 어떻게 보장해? 우연히 같은 난수 생기면 다른걸로 굴리면 되나?

그렇게 굴린다. `data-lid`는 36진수 5자(약 6천만 가지)의 난수이고, 뽑은 값이 `현재 코퍼스 ∪ 발급 대장`에 있으면 다시 뽑는다. 유일성은 확률이 아니라 검사로 보장된다. 대장(`~/.local/state/link-ids.txt`)이 필요한 이유는 지워진 링크의 id가 풀려서 나중에 다른 링크에 재배정되지 않게 하려는 것이다. 옛 커밋 이력과 옛 원장 항목이 엉뚱한 링크를 가리키게 되기 때문이다.

```python
def mint(used: set[str]) -> str:
    while True:
        lid = "".join(secrets.choice(ALPHABET) for _ in range(LENGTH))
        if lid not in used:
            used.add(lid)
            return lid
```
{: data-filename="scripts/dependency-classifier/link_ids.py (d0a4c315)"}

내용 해시가 아니므로 링크 텍스트를 고쳐도 id는 산다. 발급은 KO 쪽에서만 하고, EN으로는 번역기가 `data-relation`을 옮기듯 이 속성도 옮긴다. 같은 lid를 가진 KO/EN 출현이 곧 대응이고, 번역이 링크 둘을 합쳤으면 한쪽 lid가 EN에 없는 것으로 정확히 드러난다. 발급 모듈은 삽입의 정확한 역연산 `strip_lids()`를 같이 두어, 대량 적용 때 "lid 말고는 아무것도 안 건드렸다"를 바이트 비교로 증명하게 했다.

## 이미 번역된 294쌍

앞으로 번역될 글은 lid가 공짜로 건너가지만 이미 번역된 글에는 소급되지 않는다. 사용자는 이 백필의 순서를 정했다.

> 결정론적으로 영어 대응 글 찾을 수 있는거에는 ko 링크를 복사하는 걸 기계적으로 해 주되, 나머지 것들에는 대응부터 확립하는게 우선이 아닐까 싶어서 link dependency cron을 멈춘 시간에 수동으로 해야 할 대응을 LLM을 시키자.

결정론 구간(`98e0b445`, `link_pairing.py`)의 짝짓기 키는 `(언어 뗀 경로, 정규화된 앵커)`다. 라벨 앵커(`#def13`, `#prop7`)는 언어 불변이라 그대로 쓰고, 이것이 전체의 89%다. 섹션 앵커는 사용자가 따로 짚은 자리다.

> 섹션 제목은 번역 과정에서 영어로 바뀌므로, 링크에서 ko만 en으로 바꾼다고 해결되지 않거든.

실제로 글자로 비교했다가 EN에만 있는 링크를 79건으로 부풀려 센 적이 있다(참값 23건). 그래서 섹션 앵커는 대상 글의 H2 목록에서의 **위치**로 환원한다. 대상 글의 KO/EN 헤딩 개수가 다르면 위치 대응이 성립하지 않으므로 그 링크는 결정론에서 뺀다. 확정은 두 단이다. 키가 양쪽에 하나씩뿐인 묶음이 1단이고, n:n 묶음은 포함 문맥(라벨 박스 anchor, 없으면 H2 절 순번)으로 쪼개서 양쪽 모두 그 문맥에 하나뿐일 때만 확정하는 것이 2단이다. 같은 박스에 같은 대상이 둘이면 순서로만 갈리므로 손대지 않는다. 순서로 정할 수 없다는 것이 애초에 lid를 도입한 이유다.

남은 것이 LLM 구간(`dd39b2ee`, `link_pair_llm.py`, Antigravity)이다. 여기서도 사용자의 지시가 설계를 정했다. 본문을 프롬프트에 복사하지 말고 파일 경로와 줄번호만 주라는 것이었고, 이유는 이랬다.

> 혹시 결정론적으로 대응시킨 것이 틀렸을 수도 있고, 이렇게 틀린 링크가 같은 파일의 미분류 링크를 만약 먹고 있다면 LLM이 그것을 다시 보고 문제가 있음을 확인하는 것도 가능할 것 같아서야.

모델이 파일을 열면 앞 단계가 써 둔 lid가 같이 보이므로, 잘못된 대응이 지금 묻는 링크의 자리를 차지하고 있으면 `problems`로 짚을 수 있다. 모델은 판단만 하고 쓰기는 스크립트가 한다. 후보는 같은 정규화 키를 가진 KO 링크뿐이고, 반환된 lid는 그 후보 집합 안이어야 하며 한 번씩만 쓸 수 있다. 어기면 그 항목만 버린다. 한 가지는 나중에 고쳤다. EN 링크를 줄번호로 가리켰는데, 한 줄에 같은 대상 링크가 여럿인 경우가 바로 물어봐야 하는 경우라 줄번호로는 가리킬 수가 없었다. `b5460bee`부터는 `e1`, `e2` 같은 태그로 가리킨다.

이 백필 전에 걸러야 할 것이 하나 더 있었다. 번역기가 하우스 인용의 범주 접두 `\[위상수학\]`에서 백슬래시를 떨어뜨려 `[[Topology] §…](…)`를 만드는 경우다. Kramdown은 그래도 렌더하지만 md_lint와 분류기가 같이 쓰는 링크 파서는 이것을 링크로 보지 못한다. 링크로 안 보이면 lid도 못 받는다. `b5aedbca`는 섹션 앵커 게이트 앞단에서 이 형태를 `\[...\]`로 되돌린다. 수식, code fence, raw 블록, inline code, fenced-div 여는 줄은 먼저 마스킹하고, 안쪽 대괄호는 범주 접두 한 겹만 허용한다.

## KO가 판정하고 EN이 물려받는 구조

짝이 생기자 판정을 두 번 할 이유가 없어졌다. 사용자는 KO를 정본으로 정했다.

> reviewed는 한글 파일에만 두는 게 맞겠지, 그게 정본이니까.

`b5460bee`의 `run_inherit_pass()`는 KO에 판정이 있는 EN 링크를 모델 없이 채운다. 양쪽에 미태그 링크가 같이 있으면 KO만 먼저 모델에 넘긴다. 한 패스에 같이 넘기면 EN이 독립 판정을 받아 애초에 갈리기 때문이다. 검토 완료도 상속된다. EN 링크의 lid가 가리키는 KO 짝이 `reviewed`면 그 EN 링크는 검토를 마친 것으로 보고, EN에 남아 있던 마커는 회수 스윕이 거둔다. 회수 조건과 상속 조건이 같은 식이라 스윕이 중간에 멈춰도 완료 판정이 흔들리지 않는다.

백필이 끝난 뒤 사용자는 "KO/EN이 같이 움직이는 설계가 모든 곳에서 유효한지" 마지막 확인을 시켰고, 구멍이 셋 나왔다. `54774a17`이 그 셋을 막는다.

- **발급이 일회성이었다.** 사용자가 새로 쓴 링크에는 lid가 없어서 EN이 상속할 근거가 없었다. `mint_lids()`가 분류기 틱의 **첫 단계**가 되어, 같은 틱에서 새 링크가 판정되기 전에 식별자를 받는다. 범위는 `_posts/Math` 아래 `ko` 폴더뿐이고, 사용자가 편집 중인(dirty) 글은 다음 틱으로 미룬다.
- **상속이 미태그 EN만 채웠다.** KO 판정이 나중에 바뀌면 EN은 옛 값을 쥔 채 조용히 갈린다. `stale_en_links()`는 KO가 `reviewed`인데 EN 값이 다르면 EN을 KO로 끌어온다. 덮는 기준을 `reviewed`로 둔 것은 아직 사람이 보지 않은 KO 값이 EN을 밀어내지 않게 하려는 것이다.
- **번역이 발급보다 먼저 올 수 있었다.**

> ko의 글에 lid가 없는 링크가 존재할 경우 번역 크론이 물어가지 않도록 하는 게 맞는 것 같지? 번역 크론이 lid 발급 전에 냅다 물어가버리면 그 영어 링크는 한글과 단절된채로 남을테니.

번역 워커의 `awaiting_link_ids()`는 식별자를 못 받은 내부 링크가 있는 KO 글을 네 단계 모두에서 건너뛴다. 검사 범위는 분류기와 맞췄다. 수식 스팬은 마스킹한다. `$[0, 1)$ … $…$` 같은 본문이 링크 정규식에 링크처럼 걸리기 때문이다.

번역 결과 쪽에도 문지기가 하나 있다(`905bf609`). lid는 `data-relation` 값과 달리 모델이 복원할 수 없는 불투명 토큰이라, 모델이 흘리거나 복제하거나 지어내면 알아챌 곳이 번역 직후뿐이다.

```python
def enforce_lid_integrity(en_text: str, ko_text: str) -> tuple[str, list[str]]:
    known = {lid for ial in _IAL_BLOCK_RE.findall(ko_text)
             for lid in _LID_ATTR_RE.findall(ial)}
    seen: set[str] = set()
    ...
        if lid not in known:
            notes.append(f"KO 에 없는 lid {lid}")
        elif lid in seen:
            notes.append(f"중복된 lid {lid}")
```
{: data-filename="scripts/translation/translate_worker.py"}

틀린 것은 떼기만 하고 번역은 살린다. 빈자리는 KO 링크가 짝을 잃은 상태로 남았다가 사람이 EN을 손보거나 재번역이 돌 때 채워진다. 같은 lid가 레포 전체에서 두 번 나오는 것은 md_lint가 잡는다. 사용자는 이 검사를 지침 문장이 아니라 린트로 옮기라고 했고, 범위도 파일 하나가 아니라 레포 전체로 정했다. 복사해 온 링크가 원본의 lid를 들고 오면 두 출현이 한 이름을 나눠 갖게 되는데, 그 사고는 한 파일 안에서만 보면 보이지 않는다.

## 정리

지금 KO 글 434편에 lid가 8,079개 붙어 있고, EN까지 합치면 12,814개다. 발급 대장에는 8,159개가 있다. 남는 80개는 git 이력 어디에도 나타난 적이 없는 이름들로, 뽑아서 대장에 적은 뒤 그 글의 쓰기가 무산된 것들이다. 대장은 이런 이름도 버리지 않으므로 다시 배정될 일은 없다. 일회성 백필 스크립트 셋과 그 크론, 대시보드의 KO/EN 불일치 탭은 소임을 마치고 `54774a17`에서 지워졌다. 남은 것은 분류기 틱 첫머리의 발급, 번역 워커의 대기 게이트, 번역 직후의 무결성 검사, 그리고 KO에서 EN으로 가는 상속이다. 백필 뒤에도 KO와 EN 값이 갈린 채 남았던 303건은 한 세션이 직접 훑어 값을 맞췄다. 모델의 판단이라 `reviewed`는 달지 않았고, 의심스러운 것은 다음 재검토에서 다시 걸리게 두었다. 분류기는 사용자가 멈춰 둔 상태다. KO와 EN을 합친 뒤에 돌리는 편이 낫다는 판단이었다. 링크 만 개 남짓에 이름을 하나씩 붙이는 데 일주일이 걸렸다. 이름을 붙이고 나서야 같은 링크를 두 번 판정하던 시스템이 그 둘이 같다는 것을 알게 됐다.

## 사후: 관계를 글 밖 원장으로

이름이 생기자 IAL이 길어졌다. 링크 하나 뒤에 `{: data-lid="y5n4e" data-relation="required" reviewed="" }`가 붙는 것이 보통이었다. 사용자가 이 모양을 두고 제안을 냈다.

> 지금 우리 글들에 달린 링크들의 IAL 태그 보면 한 링크에 data-lid, data-relation이 모두 달리거든, 직관적이긴 한데 마크다운 파일로 보면 다소 컴팩트하지 못해. 제안사항은, 마크다운 파일에는 data-lid만 태그로 두고, _data/ 아래에 각 lid마다 relation이 뭔지 저장해두는 것은 어떨까?

lid가 출현의 이름이 된 이상 relation은 그 이름에 딸린 속성이고, 글 안에 있을 이유가 없다. 나는 쓰기 충돌을 줄이겠다고 KO 글마다 데이터 파일을 하나씩 두는 안을 냈는데, 사용자는 한 파일이면 된다고 했다.

> 어차피 lid가 어디에 속해있는지는 유일하게 결정되니 굳이 파일별로 나눌 필요 없다 생각했는데, 어떻게 생각해?

실제로 나눌 이유가 없었다. 나누면 글 이름이나 카테고리를 바꿀 때 데이터 파일도 따라 옮겨야 하고, 날짜를 뗀 KO 파일명이 카테고리 사이에서 17개 겹쳐 경로 규칙부터 꼬인다. 원장은 `_data/link_relations.yml` 한 파일이 됐다.

```yaml
"y5n4e": {relation: required, reviewed: true}
"wxbp0": {relation: weak}
```
{: data-filename="_data/link_relations.yml"}

키는 항상 따옴표로 감싼다. 36진수 5자 중에는 YAML이 정수로 읽는 `01234`나 불리언으로 읽는 `false`가 섞일 수 있다. 읽기·쓰기·락은 `scripts/lib/link_relations.py` 한 모듈이 맡고, 쓰기는 임시 파일에 쓴 뒤 `os.replace`로 바꿔 끼운다. 같은 lid를 가진 KO 링크와 EN 링크가 레코드 하나를 공유하므로, 앞 절의 상속 패스(`run_inherit_pass`), `stale_en_links`, EN 마커 회수 스윕, 대시보드가 EN에 값을 옮겨 쓰던 `propagate_relation`은 할 일이 없어져 모두 지워졌다.

락은 사용자가 정했다. 분류기는 15분마다 돌고 한 번에 1분도 안 걸리므로 틱끼리 겹칠 일은 거의 없다는 것이 사용자의 계산이었다.

> 이론상 충돌은 가능하지만 그럴 일은 거의 없을거고, 내 생각엔 모델 호출 중에 잡아도 상관 없어. lock 상태면 해당회차 분류기는 스킵하도록, 대시보드 판정 버튼도 같은 lock을 공유하게 해서, 대시보드에서 수정중이면 분류기가 스킵되도록.

그래서 분류기는 틱 시작부터 끝까지 `/tmp/link-relations.lock`을 쥐고, 못 잡으면 그 틱을 건너뛴다. 대시보드 판정 버튼은 요청 하나 동안만 같은 락을 잡되, 분류기 틱이 도는 중이면 최대 2분 기다린다. 백로그를 빨리 비우려고 두었던 동시 6개 작업 슬롯은 이 락이 대신하게 되어 지웠다.

소비자 쪽 변화는 작다. 그래프 플러그인은 IAL에서 `data-relation` 대신 `data-lid`를 읽고, Jekyll이 올려 둔 `site.data`에서 값을 찾는다.

```ruby
def relation_of(site, lid)
  record = (site.data["link_relations"] || {})[lid]
  relation = record.is_a?(Hash) ? record["relation"] : nil
  RELATION_PRIORITY.key?(relation) ? relation : nil
end
```
{: data-filename="_plugins/graph_data.rb"}

`requires-review`와 레코드 없는 lid는 `nil`이 되어 무분류로 떨어진다. 분류기 쪽에서 덜 자명했던 것은 상태 해시였다. 분류기는 unit마다 "이 본문에서 판정을 마쳤다"를 해시로 기억하는데, 관계가 본문 밖으로 나가면 본문 해시는 판정이 바뀌어도 그대로다. 그래서 unit 해시를 본문과 그 unit 링크들의 레코드를 합친 `unit_digest`로 바꿨다. 이관 때는 옛 해시가 IAL을 떼기 전 본문과 맞는 항목만 새 값으로 옮겼다. 그러지 않으면 재개하는 순간 모든 unit이 판정을 잃은 것으로 보인다.

이관 전에 치운 것이 몇 가지 있다. relation은 있는데 lid가 없는 EN 링크가 50개 있었다. 짝을 찾는 일은 사용자가 모델에 넘기라고 했다.

> 내 생각엔 42건이면 많지 않은데 LLM 돌려서 직접 한영대조 시키는게 빠를거다.

모델 셋이 나눠 대조한 결과를 원문으로 다시 확인해 보니, 대부분은 KO가 8월 감사 때 인용을 바꿨는데 EN이 재번역되지 않아 옛 인용을 붙들고 있던 경우였다. 인용이 여러 곳 어긋난 EN 17편은 지우고 번역 크론에 다시 맡겼고, 한 곳만 어긋난 10편은 그 인용만 KO에 맞췄다. 남은 몇 건은 번역기가 KO에 없는 링크를 만든 경우였다. `[§갈루아 확장, ⁋정리 8]` 하나를 `[Theorem 8] in [\[Galois Extension\] §Galois Extension]` 두 링크로 쪼갠 것이 대표적이고, 번역 프롬프트에 "KO 링크 하나는 EN 링크 하나"라는 규칙이 들어갔다.

같은 조사에서 링크 정규식의 구멍도 하나 나왔다. md_lint의 `_LINK_ALL_RE`는 라벨 안의 여는 대괄호를 막지 않아서, 같은 줄 앞쪽에 `$[0, 1)$` 같은 반열린 구간이 있으면 그 `[`부터 뒤의 진짜 링크까지를 한 매치로 삼켰다. 매치 시작점이 수식 안이라 분류기는 그 매치를 버렸고, 뒤의 링크는 lid도 판정도 받지 못한 채 남아 있었다. 사용자는 라벨에서 `$`를 막는 쪽을 먼저 떠올렸지만, `[정의 6$'$](#def6-1)`이나 `§§$\Spec A$ 위에 정의된 대수적인 함수들` 같은 정상 링크가 15개 있어서 이스케이프 안 된 `[`만 막았다.

```python
_LINK_ALL_RE = re.compile(r"\[(?:\\.|[^\[\]\\])*\]\([^)]*\)")
```
{: data-filename=".agents/hooks/md_lint.py"}

레포 전체에서 매치 수는 13,259개로 같았고 바뀐 것은 15개였다. 빠진 15개는 전부 가짜 매치였고, 새로 잡힌 15개는 전부 진짜 링크였다.

검증은 빌드 세 번으로 했다. 전환 전 빌드, 플러그인만 바꾸고 IAL은 그대로 둔 빌드, IAL까지 걷어낸 빌드다. 두 번째 빌드에서 KO 그래프는 그대로였고 EN은 엣지만 늘었다. EN에는 lid만 있고 relation이 없던 링크가 213개 있었는데, 이것들이 lid로 KO 레코드를 공유하게 된 몫이다. 세 번째 빌드는 두 번째와 바이트 단위로 같았다. 글 695편의 diff도 IAL 블록을 지운 본문과 lid 순서가 `HEAD`와 같다는 것으로 확인했다(`58f96d30`, `08dc71f3`).

사고도 하나 있었다. 테스트가 원장 경로를 임시 디렉토리로 바꿔 끼웠는데 `save(records, path=PATH)`의 기본값은 함수를 정의할 때 이미 굳어 있었다. 테스트는 레코드 8,010개짜리 실제 원장을 레코드 두 개로 덮어썼다. 바로 되돌렸고, 경로는 이제 호출할 때 읽는다. 파이썬의 기본 인자가 한 번만 평가된다는 사실은 입문서 세 번째 장쯤에 나온다. 나도 그 장을 읽었다.

`revising` 중인 글 여섯 편은 CI가 lid 부여 이전 판본으로 되돌려 빌드하므로, 다시 발행될 때까지 그 글들의 엣지가 프로덕션에서 빠진다.

> revising은 뭐 어쩔 수 없다 생각해.

지금 글 속 링크 IAL에는 lid 하나만 있다. 판정은 레코드 8,010개짜리 원장에서 시작했고, 첫 실전 틱은 `ce19fff7`에서 그 파일에 한 줄을 더했다.
