---

title: "정리 박스를 fenced-div로"
excerpt: "손으로 쓰던 정리 박스 HTML 9,460개를 콜론 세 개짜리 펜스로 줄이고, 렌더 결과는 한 글자도 바꾸지 않은 일"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/fenced_theorem_blocks

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-07-03
weight: 24

---

관련 파일: [`_plugins/fenced_theorem_blocks.rb`](https://github.com/math-jh/math-jh.github.io/blob/main/_plugins/fenced_theorem_blocks.rb), [`scripts/translation/translate_worker.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/translation/translate_worker.py)
{: .notice--info}

이 블로그의 수학 글에는 정의·명제·정리·증명이 박스로 뜬다. 그 박스를 그동안은 소스 마크다운에 HTML로 직접 적었다. 정리 하나를 쓰려면 여는 `<div class="proposition" markdown="1">`, 앵커를 단 `<ins id="thm2">`, 볼드 라벨 `**정리 2**`, 닫는 `</div>`까지 — 내용 한 문단을 감싸는 비계가 대여섯 줄이었다. 게다가 같은 정보가 여러 자리에 흩어졌다. 종류가 "정리"라는 사실은 class(`proposition`)로 한 번, id 접두사(`thm`)로 또 한 번 옮겨 적어야 했고, 번호 2는 id(`thm2`)와 라벨(`정리 2`)에 두 번 나타났다. 넷 중 하나만 어긋나도 박스는 조용히 틀어진다.

코퍼스 전체에 그런 박스가 9,460개 있었다. 사용자가 정한 방향은 이걸 pandoc식 `:::` 펜스로 바꾸는 것이었다 — 여는 한 줄에 라벨만 적으면 class도 id도 번호도 거기서 유도되게. 조건이 하나 붙었다. 화면은 한 글자도 바뀌면 안 된다. 렌더된 박스는 지금과 완전히 같고, 바뀌는 건 소스뿐이어야 했다.

## 손으로 쓰던 박스

옛 소스는 이렇게 생겼다.

```html
<div class="proposition" markdown="1">

<ins id="thm2">**정리 2 (Thom isomorphism)**</ins> 본문 첫 문단…

</div>
```

class는 종류에서 나오고(정리 → `proposition`), id는 접두사에 번호를 붙인 것이고(`thm` + `2`), 라벨은 종류·번호·이름을 다시 적은 것이다. 쓰는 자리마다 이 셋을 손으로 맞춰야 했고, 종류를 `proposition`이라 적고 라벨엔 "정의"라 적는 어긋남은 빌드가 잡아주지 않는다. 그냥 틀어진 박스가 렌더될 뿐이다.

앵커는 특히 못 건드린다. 다른 글이 `[정리 2](#thm2)`로 이 박스를 가리키고 있으면 `thm2`라는 id는 그 글들과의 계약이다. 그래서 이 비계는 지우기도 옮기기도 조심스러웠고, 정리 하나를 끼워 넣어 번호를 밀 때마다 id와 라벨을 나란히 다시 세어야 했다.

증명은 접히는 별도 박스였다.

```html
<details class="proof" markdown="1">
<summary>증명</summary>

증명 본문…

</details>
```

## `:::` 한 줄

바꾼 뒤의 같은 박스다.

```markdown
::: 정리 2 (Thom isomorphism)
본문 첫 문단…
:::
```

여는 줄의 "정리 2 (Thom isomorphism)" 하나에서 나머지가 전부 나온다. 종류어 "정리"가 class `proposition`과 id 접두사 `thm`을 정하고, 번호 2가 붙어 `thm2`가 되고, 괄호 안 이름은 라벨에 그대로 실린다. 종류어와 class·접두사의 대응은 한 곳에 표로 있다 — 정의는 definition/def, 명제는 proposition/prop, 정리는 proposition/thm, 보조정리는 lem, 따름정리는 cor, 예시는 example/ex, 참고는 remark/rmk. 영어 글은 Definition·Theorem 같은 키워드를 같은 표로 받는다.

증명은 라벨만 적는다. 부착형은 `::: 증명`으로 바로 앞 박스의 증명이 되고, 단독형은 `::: 증명 (정리 4)`로 적으면 `<summary>`가 "정리 4의 증명"으로 자동으로 붙는다.

유도가 안 되는 라벨도 있다. "주장"(Conjecture)처럼 표에 없는 종류거나, inbound 참조를 지키려고 유도 규칙 밖의 커스텀 id를 써야 하는 박스다. 이건 명시형으로, class와 `{#id}`를 직접 준다.

```markdown
::: misc 주장 4 (Mirror theorem) {#conj4}
내용…
:::
```

유도할 수 있는 라벨은 유도형이 정본이고, 명시형은 이 예외들만 받는다.

## 바이트가 같은 출력

이 문법을 HTML로 되돌리는 게 `_plugins/fenced_theorem_blocks.rb`다. 핵심은 이 플러그인이 **손으로 쓰던 그 HTML과 바이트 단위로 같은 출력**을 낸다는 것이다.

```ruby
KIND_MAP = {
  "정의" => %w[definition def],  "명제" => %w[proposition prop],
  "정리" => %w[proposition thm], "예시" => %w[example ex], # …
}

# ::: 정리 2 (Thom isomorphism)  →  유도형
cls, prefix = KIND_MAP[kind]          # proposition, thm
id          = "#{prefix}#{number}"    # thm2
# 아래 세 줄은 옛 소스와 글자 하나 다르지 않다
%(<div class="#{cls}" markdown="1">)
%(<ins id="#{id}">**#{label}**</ins> #{body_first})
%(</div>)
```
{: data-filename="_plugins/fenced_theorem_blocks.rb"}

출력이 옛것과 같으니 그 뒤 파이프라인은 아무것도 모른다. kramdown도, 라벨을 종류·이름으로 쪼개는 기존 플러그인(`theorem-label-splitter.rb`)도, CSS도, 교차참조 표시명을 만드는 링크 정규화기도, hover 미리보기 카드도 전부 무변경이다. 플러그인은 소스 앞단에 설탕을 한 겹 발랐을 뿐이고, 렌더 경로는 예전 그대로다. 그래서 "화면이 안 바뀐다"는 조건이 지켜진다.

두 가지를 조심했다. 하나는 `:::`가 코드블록이나 Liquid raw 블록 안에 있을 때다. 정규식으로 일괄 치환하면 코드 예시 속 `:::`까지 박스로 바꿔버린다. 그래서 파서는 줄 단위로 스캔하며 코드펜스와 raw 구간을 추적해 그 안은 건드리지 않는다. 다른 하나는 순서다. 링크 정규화기가 변환된 `<ins id>`를 읽어야 교차참조 표시명이 나오므로, 이 플러그인을 그보다 먼저(pre_render, 높은 priority) 돌게 걸었다. 인식 못 하는 `:::`는 바꾸지 않고 원본 그대로 두면서 경고를 찍는다 — 마이그레이션 실수를 소스에 드러내, 조용히 사라지지 않게.

## 9,460개를 옮기기

문법과 플러그인이 준비돼도 옮길 박스가 9,460개였다. 코퍼스의 옛 HTML이 완전히 한 모양은 아니어서, 먼저 변형들을 플러그인이 내는 정본 형태로 정규화한 뒤 일괄 변환했다. 1차로 대부분이 유도형으로 떨어졌고, 유도 규칙에 안 맞는 302개가 2차 정리로 남았다 — 표에 없는 종류거나 커스텀 id가 필요한 박스들로, 명시형으로 손봤다. 이 과정에서 앵커가 없던 자리에 새 slug id 43개를 배정했다.

여기까지 하고 나면 소스에 정리 박스 HTML을 다시 손으로 적을 일이 없어야 한다. 그래서 규칙도 같이 옮겼다. 작성 가이드라인은 이제 `:::`를 정본으로 두고 정리 박스 HTML 직접 작성을 금지하며, 저장 전 린트가 `:::` 펜스의 짝이 맞는지, 금지된 박스 태그가 없는지, 유도 라벨의 번호가 1..N으로 이어지는지를 검사한다.

## 번역 워커에 가르치기

이 블로그는 한국어 글을 [자동 번역 워커](/ko/llm_workshop/translation_worker)가 영어로 옮긴다. 워커는 그동안 정리 박스를 HTML 구조로 알고 있었으니, 새 문법을 가르쳐야 했다. 규칙은 단순하다 — `:::` 줄은 개수도 순서도 그대로 두고, 여는 줄의 라벨만 번역한다.

```text
::: 정리 2 (Thom isomorphism)   →   ::: Theorem 2 (Thom isomorphism)
    종류어만 번역(정리 → Theorem), 번호 2 유지, 괄호 이름 번역
::: 증명                        →   ::: Proof
::: misc 주장 4 (…) {#conj4}    →   ::: misc Conjecture 4 (…) {#conj4}
```
{: data-filename="scripts/translation/translate_worker.py"}

번호 N과 `{#id}` 앵커는 절대 바꾸지 않는다 — 그게 바뀌면 유도되는 id(`thm2`)나 명시 id(`conj4`)가 어긋나 교차참조가 끊긴다. 아직 `:::`로 안 옮겨진 잔여 HTML 박스가 섞여 들어와도 그대로 보존하도록, 두 형태를 다 아는 프롬프트로 맞췄다.

## 정리

9,460개를 옮겼고, 화면에서는 아무 일도 일어나지 않았다. 박스는 예전과 똑같은 자리에 똑같은 모양으로 뜨고, 교차참조도 hover 카드도 그대로다. 바뀐 건 소스뿐이다 — 정리 하나가 대여섯 줄의 HTML 비계에서 `:::` 두 줄 사이로 줄었고, 종류·번호·앵커를 손으로 맞추던 일이 여는 줄 한 줄에서 유도된다. 눈에 보이는 성과가 정확히 0인 작업을 9,460번 반복했다. 다음에 정의를 적을 사람이 `<div>`를 세지 않아도 된다는 것, 그게 이번 작업의 전부다.
