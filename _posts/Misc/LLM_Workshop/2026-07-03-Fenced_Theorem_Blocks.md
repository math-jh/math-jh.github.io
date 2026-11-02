---

title: "정리 박스를 fenced-div로"
excerpt: "손으로 쓰던 정리 박스 HTML 9,460개를 콜론 세 개짜리 펜스로 옮기고, 빌드 때 그 펜스를 같은 HTML로 되돌리는 전처리 플러그인"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/fenced_theorem_blocks

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-07-03
last_modified_at: 2026-11-02
weight: 24

---

관련 파일: [`_plugins/fenced_theorem_blocks.rb`](https://github.com/math-jh/math-jh.github.io/blob/main/_plugins/fenced_theorem_blocks.rb), [`_data/theorem_vocab.yml`](https://github.com/math-jh/math-jh.github.io/blob/main/_data/theorem_vocab.yml), [`scripts/translation/translate_worker.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/translation/translate_worker.py)
{: .notice--info}

이 블로그의 수학 글에는 정의·명제·정리·증명이 박스로 뜬다. 그 박스는 원래 소스 마크다운에 HTML로 직접 적었고, 코퍼스 전체에 9,460개가 있었다. 사용자가 정한 방향은 이것을 pandoc식 `:::` 펜스로 바꾸는 것이었다. 여는 줄에 라벨만 적으면 class도 id도 번호도 거기서 유도되는 문법이다. 조건이 하나 붙었다. 렌더된 화면은 한 글자도 바뀌면 안 되고, 바뀌는 것은 소스뿐이어야 했다.

## 손으로 쓰던 박스 HTML

옛 소스는 이렇게 생겼다.

```html
<div class="proposition" markdown="1">

<ins id="thm2">**정리 2 (Thom isomorphism)**</ins> 본문 첫 문단…

</div>
```

내용 한 문단을 감싸는 비계가 다섯 줄이고, 같은 정보가 여러 자리에 흩어져 있다. 종류가 "정리"라는 사실은 class(`proposition`)와 id 접두사(`thm`)에 한 번씩, 번호 2는 id(`thm2`)와 라벨(`정리 2`)에 한 번씩 나온다. class를 `proposition`이라 적고 라벨에 "정의"라 적어도 빌드는 아무 말을 하지 않고, 틀어진 박스가 그대로 렌더된다.

다른 글이 `[정리 2](#thm2)`로 이 박스를 가리키면 `thm2`는 그 글들과의 계약이 된다. 그래서 정리 하나를 끼워 넣어 번호를 밀 때마다 id와 라벨을 나란히 다시 세어야 했다. 증명은 `<summary>증명</summary>`을 단 접히는 `<details class="proof">`였다.

## `:::` 여는 줄에서 유도되는 class·id·라벨

같은 박스를 펜스로 적으면 이렇다.

```markdown
::: 정리 2 (Thom isomorphism)
본문 첫 문단…
:::
```

여는 줄의 "정리 2 (Thom isomorphism)"에서 나머지가 전부 나온다. 종류어 "정리"가 class `proposition`과 접두사 `thm`을 정하고, 번호 2가 붙어 id `thm2`가 되고, 괄호 안 이름은 라벨에 그대로 실린다. 종류어 대응표는 `_data/theorem_vocab.yml`에 있다.

```yaml
kinds:
  - { ko: 정의,     en: Definition,  class: definition,  prefix: def }
  - { ko: 명제,     en: Proposition, class: proposition, prefix: prop }
  - { ko: 정리,     en: Theorem,     class: proposition, prefix: thm }
  - { ko: 보조정리, en: Lemma,       class: proposition, prefix: lem }
  - { ko: 따름정리, en: Corollary,   class: proposition, prefix: cor }
  - { ko: 예시,     en: Example,     class: example,     prefix: ex }
  - { ko: 참고,     en: Remark,      class: remark,      prefix: rmk }
explicit_classes: [definition, proposition, example, remark, misc]
```
{: data-filename="_data/theorem_vocab.yml"}

한 행이 한국어 종류어와 영어 키워드를 같이 들고 있어서, 영어 글의 `::: Theorem 2`도 같은 행을 거쳐 `thm2`가 된다. 플러그인·번역 워커·JS가 모두 이 파일에서 표를 파생한다 ([단일 출처 글](/ko/llm_workshop/single_source)).

증명은 라벨만 적는다. `::: 증명`은 바로 앞 박스에 붙는 증명이고, `::: 증명 (정리 4)`로 적으면 단독형(`proof--alone`)이 되어 `<summary>`가 "정리 4의 증명"으로 붙는다. 영어는 `::: Proof`와 `::: Proof (Theorem 4)`다.

표에 없는 종류("주장" 같은)이거나 inbound 참조를 지키려고 유도 규칙 밖의 id를 써야 하는 박스는 명시형으로 class와 `{#id}`를 직접 준다.

```markdown
::: misc 주장 4 (Mirror theorem) {#conj4}
내용…
:::
```

명시형은 라벨과 id를 verbatim으로 받고 아무것도 유도하지 않는다. 유도할 수 있는 라벨은 유도형이 정본이다.

## 펜스를 옛 HTML로 되돌리는 전처리

`_plugins/fenced_theorem_blocks.rb`가 이 문법을 손으로 쓰던 것과 같은 HTML로 펼친다. 출력이 옛 소스와 같으니 kramdown, 라벨을 쪼개는 `theorem-label-splitter.rb`, CSS, 링크 정규화기, hover 미리보기 카드는 하나도 고치지 않았고, 화면이 안 바뀐다는 조건은 그렇게 지켜졌다.

```ruby
def parse_header(label, raw_line)
  if (m = label.match(EXPLICIT_RE))     # misc 주장 4 (…) {#conj4}
    return { type: :box, cls: m[1], id: m[3], label: m[2], raw: raw_line }
  end
  # … 증명 / 증명 (정리 4) / Proof / Proof (Theorem 4)
  if (m = label.match(DERIVED_RE))      # 정리 2 (Thom isomorphism)
    cls, prefix = KIND_MAP[m[1]]        # proposition, thm
    return { type: :box, cls: cls, id: "#{prefix}#{m[2]}", label: label, raw: raw_line }
  end
  nil
end
```
{: data-filename="_plugins/fenced_theorem_blocks.rb"}

파서는 줄 단위로 스캔하면서 백틱·물결 코드펜스와 Liquid raw 구간을 추적하고, 그 안의 `:::`는 건드리지 않는다. 정규식 일괄 치환이었다면 코드 예시 속 `:::`까지 박스가 된다. 인식하지 못한 `:::` 줄은 원본 그대로 두고 경고를 찍어 마이그레이션 실수가 소스에 드러나게 한다.

순서도 맞춰야 했다. 링크 정규화기는 변환된 `<ins id>`를 읽어 교차참조 표시명을 만든다. 그래서 이 플러그인은 `:site, :pre_render`에 priority 30(high)으로 걸려, priority 20인 링크 정규화기의 훅보다 먼저 돈다.

지금 Math 코퍼스에는 손으로 쓴 박스 HTML이 하나도 남아 있지 않다(`<ins id=` 0건). 이 HTML은 이제 플러그인만 만드는 중간 형식이고, 마크업을 바꿀 때는 플러그인의 출력 함수를 고친다. 증명 `<summary>` 안의 라벨 칩 `<span class="thm-tag">`가 그렇게 들어갔다.

## 9,460개 일괄 변환과 린트

코퍼스의 옛 HTML이 완전히 한 모양은 아니어서, 먼저 변형들을 플러그인이 내는 정본 형태로 정규화하고 나서 9,460개를 일괄 변환했다. 1차 변환에서 대부분이 유도형으로 떨어졌고, 표에 없는 종류거나 커스텀 id가 필요한 302개가 남아 2차 정리에서 명시형으로 손봤다. 앵커가 없던 자리에는 새 slug id 43개를 배정했다 ([b07d82dc](https://github.com/math-jh/math-jh.github.io/commit/b07d82dcc76a6a2333c93c80beb0c47bd90ef5f7)).

화면에 아무 변화가 없어야 성공인 작업을 9,460번 반복했다. 잘 됐는지 확인하는 방법도 아무 일도 일어나지 않았음을 확인하는 것뿐이었다.

규칙도 같이 옮겼다. 작성 가이드라인은 `:::`를 정본으로 두고 정리 박스 HTML 직접 작성을 금지한다. 편집 때 도는 md_lint 훅은 `:::` 여는 줄과 닫는 줄의 개수가 맞는지, `theorem`·`lemma`·`corollary` 같은 금지 class의 div가 없는지, 유도형 라벨의 번호가 1..N으로 이어지는지를 검사한다.

## 번역 워커가 읽는 `:::`

한국어 글은 [번역 워커](/ko/llm_workshop/translation_worker)가 영어로 옮긴다. 워커는 정리 박스를 HTML 구조로 알고 있었으니 새 문법을 가르쳐야 했다. 프롬프트의 규칙은 `:::` 줄의 개수와 순서를 그대로 두고 여는 줄의 라벨만 번역하라는 것이다.

```text
::: 정리 2 (Thom isomorphism)   →  ::: Theorem 2 (Thom isomorphism)
::: 증명 (정리 4)               →  ::: Proof (Theorem 4)
::: misc 주장 4 (…) {#conj4}    →  ::: misc Conjecture 4 (…) {#conj4}
```

번호 N과 `{#id}`는 바꾸지 않는다. 그게 바뀌면 유도 id(`thm2`)나 명시 id(`conj4`)가 어긋나 교차참조가 끊긴다. 워커는 이것을 검사도 한다. 같은 `theorem_vocab.yml`에서 종류어→접두사 표를 만들어 플러그인의 유도를 그대로 흉내 내고, KO와 EN의 박스 id 집합을 대조한다.

```python
def _fenced_block_id(label: str) -> Optional[str]:
    m = _MISC_LABEL_RE.match(label)
    if m:
        return m.group(2)
    m = _DERIVED_LABEL_RE.match(label)
    if m:
        return _KIND_PREFIX[m.group(1)] + m.group(2)
    return None
```
{: data-filename="scripts/translation/translate_worker.py"}

KO 여는 줄과 번역이 덜 된 EN 여는 줄은 같은 id를 유도하므로 id 대조로는 안 잡힌다. 그래서 EN 여는 줄의 라벨에 한글이 남았는지를 따로 본다. 프롬프트에는 `:::`로 안 옮겨진 HTML 박스를 보존하라는 조항이 아직 남아 있지만, 그런 박스는 이제 Math 코퍼스에 없다.

## dev 빌드에서 펼쳐 두는 증명

[스킴 매끄러움 글](/ko/math/scheme_theory/smooth_and_etale_morphisms)처럼 증명이 여러 단계로 중첩된 글을 고칠 때는 접힌 `<details>`를 매번 손으로 열어야 했다.

> 좋아, 그리고 dev 서버에서는 증명 블럭이 항상 펼쳐진 상태이도록 해 줄 수 있어?

`render_proof`가 여는 `<details>` 태그에 조건부 속성 하나를 넣었다.

```ruby
PROOF_OPEN_ATTR = Jekyll.env == "production" ? "" : " open"
# …
lines << %(<details class="#{block[:cls]}"#{PROOF_OPEN_ATTR} markdown="1">)
lines << %(<summary><span class="thm-tag">#{block[:summary]}</span></summary>)
```
{: data-filename="_plugins/fenced_theorem_blocks.rb"}

새 플래그는 두지 않았다. dev 서버(포트 4001)는 `JEKYLL_ENV`를 주지 않아 기본값 development로 돌고, [판본 스냅샷](/ko/llm_workshop/version_comparator) 빌드는 `JEKYLL_ENV=development`를 명시한다. 토글은 그대로라 펼쳐진 증명도 클릭 한 번이면 접힌다. `JEKYLL_ENV=production`으로 도는 CI 빌드만 증명을 접은 채로 배포한다.
