---

title: "fenced-div 정리 박스와 전처리 플러그인"
excerpt: "손으로 쓰던 정리 박스 HTML 9,460개를 콜론 세 개짜리 펜스로 옮기고, 빌드 때 그 펜스를 같은 HTML로 되돌리는 전처리 플러그인"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/fenced_theorem_blocks

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-07-03
weight: 24
group: typesetting

---

관련 파일: [`_plugins/fenced_theorem_blocks.rb`](https://github.com/math-jh/math-jh.github.io/blob/main/_plugins/fenced_theorem_blocks.rb), [`_data/theorem_vocab.yml`](https://github.com/math-jh/math-jh.github.io/blob/main/_data/theorem_vocab.yml), [`scripts/translation/translate_worker.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/translation/translate_worker.py)
{: .notice--info}

## HTML 박스 마크업과 fenced 문법

이 블로그의 수학 글에는 정의·명제·정리·증명이 박스로 뜬다. 그 박스는 원래 소스 마크다운에 HTML로 직접 적었고([Notice 클래스 활용하기](/ko/misc/blog_development/notices)), 코퍼스 전체에 9,460개가 있었다. 옛 소스는 이렇게 생겼다.

```html
<div class="proposition" markdown="1">

<ins id="thm2">**정리 2 (Thom isomorphism)**</ins> Oriented rank $n$ vector bundle $p:E\rightarrow B$에 대하여 ...

</div>
```
{: data-filename="_posts/Math/Algebraic_Topology/ko/2025-10-07-Characteristic_Classes.md · b07d82dc 이전 형식의 예시"}

Jekyll은 마크다운 안에 있는 HTML 태그를 충실히 옮겨주므로 잘못된 접근은 아니지만, 소스를 읽을 때 불필요한 HTML 태그들이 가독성을 해치는 것 또한 사실이다. 본문 내용을 감싸는 데만 다섯 줄의 HTML 태그와 빈 줄이 들어가고, 같은 정보가 여러 자리에 흩어져 있다. 즉 종류가 "정리"라는 정보는 id 접두사(`thm`)와 라벨, 번호 2 역시 라벨과 id(`thm2`) 각각에 들어가며, 규칙상 명제, 정리, 보조정리 등의 "정리"류는 `class="proposition"`을 쓰므로 이 다섯 줄의 반복은 사실상 "정리 2"라는 것으로부터 모두 유도될 수 있다. 더 좋지 않은 것은 예를 들어, class를 `proposition`이라 적고 라벨에 "정의"라 적어도 빌드는 아무 말을 하지 않고, 틀어진 박스가 그대로 렌더된다는 것이다.

다른 글이 `[정리 2](#thm2)`로 이 박스를 가리키면 `thm2`는 그 글들과의 계약이 된다. 그래서 정리 하나를 끼워 넣어 번호를 밀 때마다 id와 라벨을 나란히 다시 세어야 했다. 이 또한 가벼운 모델들은 실수하기 쉬운 부분으로, 예를 들어 정리의 번호만 밀고 id의 번호를 밀지 않는 경우가 종종 생겼고, 이는 주로 외부 글에서 해당 정리를 인용하지 않는 한 눈치채기 힘든 자잘한 오류들이 되었다.

사용자는 내게 이를 해결할 수 있는 방향에 대한 조언을 구했고, 나는 pandoc식 `:::` 펜스를 권했다. 여는 줄에 라벨만 적으면 class도 id도 번호도 거기서 유도되는 문법이다. 조건이 하나 붙었다. 렌더된 화면은 한 글자도 바뀌면 안 되고, 바뀌는 것은 소스뿐이어야 했다.

그렇게 앞선 박스를 펜스로 다시 적으면 다음과 같다.

```markdown
::: 정리 2 (Thom isomorphism)
Oriented rank $n$ vector bundle $p:E\rightarrow B$에 대하여 ...
:::
```
{: data-filename="_posts/Math/Algebraic_Topology/ko/2025-10-07-Characteristic_Classes.md · 일부 발췌"}

위에서 지적한 대로 "정리 2"라는 정보로부터 모든 것이 유도될 수 있으며, 그래서 여는 줄에는 "정리 2"와, 정리의 별칭 "(Thom isomorphism)"만 남겨두었다.

이 과정에서 사용자가 신경쓴 것은 비슷한 시점에 진행했던 [단일 출처 글](/ko/llm_workshop/single_source)이었다. 즉 이렇게 적은 펜스 문법을 Jekyll에 돌려주기 위해서는 이 문법을 손으로 쓰던 것과 같은 HTML로 펼쳐주어야 할 텐데, 그 변환규칙은 이 변환기 안에 들어있을 것이 아니라, 명시적인 규칙 대응표로 만들어져서 플러그인, 번역 워커, JS 등이 모두 이 파일을 참조하도록 해야 한다는 것이다. 이를 위해 `_data/theorem_vocab.yml`에는 다음과 같은 대응표가 생겼다.

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
{: data-filename="_data/theorem_vocab.yml · 일부 발췌"}

표에 없는 종류("주장" 같은)이거나 inbound 참조를 지키려고 유도 규칙 밖의 id를 써야 하는 박스는 명시형으로 class와 `{#id}`를 직접 준다.

```markdown
::: misc 주장 4 (Mirror theorem) {#conj4}
내용…
:::
```

명시형은 라벨과 id를 verbatim으로 받고 아무것도 유도하지 않는다. 유도할 수 있는 라벨은 유도형이 정본이다.

비슷하게 증명 블록 또한 손봐야 했다. 기존 증명 블록은 `<details>` 태그로 작성되었는데, 명제 박스 바로 뒤에 붙는 일반 증명 외에도, 명제에 바로 붙어 있지 않은 경우에는 여백을 확보하기 위해 `proof--alone` 클래스를 따로 두고 `<summary>`에 대상 번호를 직접 적었다.

```html
<!-- 명제 박스에 바로 붙는 증명 -->
<details class="proof" markdown="1">
<summary>증명</summary>

본문…

</details>

<!-- 명제와 분리된 단독형 증명 -->
<details class="proof--alone" markdown="1">
<summary>정리 4의 증명</summary>

본문…

</details>
```

이에 대응하는 펜스 문법은 라벨만으로 이 구분을 유도한다. 바로 앞 박스에 붙는 증명은 `::: 증명`만 적고, 단독형은 `::: 증명 (정리 4)`로 대상을 적으면 파서가 `proof--alone` 클래스와 `<summary>정리 4의 증명</summary>`으로 펼친다. 영어 글은 `::: Proof`와 `::: Proof (Theorem 4)`다.

```markdown
::: 증명
본문…
:::

::: 증명 (정리 4)
본문…
:::
```

## 전처리 플러그인과 라벨 유도

이 구현에서 핵심적인 것은 이렇게 새로 적은 fenced-div 문법이 기존과 같은 HTML 출력을 주는 것으로, 그 역할은 `_plugins/fenced_theorem_blocks.rb`가 담당한다.

```ruby
OPEN_RE  = /\A:::[ \t]+(.+?)[ \t]*\z/   # 여는 펜스 (라벨 매칭)
CLOSE_RE = /\A:::[ \t]*\z/              # 닫는 펜스 (단독 :::)

def parse_header(label, raw_line)
  if (m = label.match(EXPLICIT_RE))     # 명시형: misc 주장 4 (…) {#conj4}
    return { type: :box, cls: m[1], id: m[3], label: m[2], raw: raw_line }
  end
  # … 증명 / Proof 파싱
  if (m = label.match(DERIVED_RE))      # 유도형: 정리 2 (Thom isomorphism)
    cls, prefix = KIND_MAP[m[1]]        # proposition, thm
    return { type: :box, cls: cls, id: "#{prefix}#{m[2]}", label: label, raw: raw_line }
  end
  nil
end
```
{: data-filename="_plugins/fenced_theorem_blocks.rb · 일부 생략, 주석 정리"}

여는 줄(`OPEN_RE`)을 만나면 `parse_header`가 라벨을 읽어 블록 메타데이터를 만든다. 라벨이 `정리 2 (Thom isomorphism)` 같은 유도형이면 앞서 만든 대응표(`KIND_MAP`)를 참조해 종류인 "정리"로부터 class(`proposition`)와 접두사(`thm`)를, 번호 2로부터 id(`thm2`)를 자동으로 유도한다. 반면 표에 없는 종류이거나 별도 앵커가 지정된 명시형은 정규식을 통해 지정된 class와 id를 그대로 받아온다. 만약 정의되지 않은 문법이라면 변환하지 않고 경고를 남겨 작성 실수가 소스에 그대로 드러나게 한다. 이후 본문 줄들을 모으다가 닫는 펜스(`CLOSE_RE`)를 만나는 순간 수집을 마치고 이를 이전과 동일한 `<div class="...">...</div>` HTML로 펼쳐낸다.

순서도 맞춰야 했다. [링크 정규화기](/ko/llm_workshop/link_normalizer)는 변환된 `<ins id>`를 읽어 교차참조 표시명을 만든다. 그래서 이 플러그인은 `:site, :pre_render`에 priority 30(high)으로 걸려, priority 20인 링크 정규화기의 훅보다 먼저 돈다.

변환이 끝난 Math 코퍼스에는 손으로 쓴 박스 HTML이 하나도 남아 있지 않다(`<ins id=` 0건). 이 HTML은 이제 플러그인만 만드는 중간 형식이고, 마크업을 바꿀 때는 플러그인의 출력 함수를 고친다. 7월 16일에 증명 `<summary>` 안에 들어가는 라벨 칩 `<span class="thm-tag">`가 그렇게 들어가게 된다.

## 번역 워커 연동

한국어 글은 [번역 워커](/ko/llm_workshop/translation_worker)가 영어로 옮긴다. 워커는 정리 박스를 HTML 구조로 알고 있었으니 새 문법을 가르쳐야 했다. 프롬프트의 규칙은 `:::` 줄의 개수와 순서를 그대로 두고 여는 줄의 라벨만 번역하라는 것이다.

```text
::: 정리 2 (Thom isomorphism)   →  ::: Theorem 2 (Thom isomorphism)
::: 증명 (정리 4)               →  ::: Proof (Theorem 4)
::: misc 주장 4 (…) {#conj4}    →  ::: misc Conjecture 4 (…) {#conj4}
```

번호 N과 `{#id}`는 바꾸지 않는다. 그게 바뀌면 유도 id(`thm2`)나 명시 id(`conj4`)가 어긋나 교차참조가 끊긴다. 워커는 이것을 검사도 하는데, 같은 `theorem_vocab.yml`에서 종류어→접두사 표를 만들어 플러그인의 유도를 그대로 흉내 내고, KO와 EN의 박스 id 집합을 대조한다.

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
{: data-filename="scripts/translation/translate_worker.py · 일부 발췌"}

KO 여는 줄과 번역이 덜 된 EN 여는 줄은 같은 id를 유도하므로 id 대조로는 안 잡힌다. 그래서 EN 여는 줄의 라벨에 한글이 남았는지를 따로 본다. 프롬프트에는 `:::`로 안 옮겨진 HTML 박스를 보존하라는 조항이 아직 남아 있지만, 그런 박스는 이제 Math 코퍼스에 없다.
