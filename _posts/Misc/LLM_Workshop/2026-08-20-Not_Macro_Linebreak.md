---

title: "슬래시만 남고 줄이 바뀔 때"
excerpt: "KaTeX의 \\not이 그 자체로 독립된 관계기호 atom이라 뒤따르는 기호와 다른 줄로 갈릴 수 있다는 것을, 인자를 통째로 삼키는 매크로로 막은 이야기"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/not_macro_linebreak

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-08-20
weight: 42

---

관련 파일: [`assets/js/katex-macros.js`](https://github.com/math-jh/math-jh.github.io/blob/main/assets/js/katex-macros.js), [`_posts/Math/Set_Theory/ko/2021-08-22-Order_Relations.md`](https://github.com/math-jh/math-jh.github.io/blob/main/_posts/Math/Set_Theory/ko/2021-08-22-Order_Relations.md), [커밋 4f107bf2](https://github.com/math-jh/math-jh.github.io/commit/4f107bf2)
{: .notice--info}

사용자가 가환대수 글을 감사하던 중 짚은 것은 한 줄이었다.

> 지금 감사 페이지에 보면 "우선 $j\geq 2$인 각각에 대하여 $x_j\not\in \mathfrak{a}_1$이고 $\mathfrak{a}_1$이 prime i" 여기에서, \not과 \in 사이에 줄바꿈이 들어갔거든? 문단 폭이 달라서 정확히 이게 프로덕션 사이트 혹은 데브 사이트에서 반영되는 것은 아닌데 혹시 비슷한 문제가 프로덕션 혹은 데브 사이트에서 생길 수 있는지만 확인해줘. 꼭 여기가 아니더라도.

출처는 [Associated Primes](/ko/math/commutative_algebra/associated_primes) 글의 prime avoidance 증명, `$x_j\not\in \mathfrak{a}_1$` 자리였다. 좁은 폭에서 사선(`/`)만 윗줄에 남고 `\in`은 다음 줄로 넘어간다. 사용자는 이 글 하나를 지목했지만 질문은 "다른 데도 이럴 수 있냐"였다. 답은 그렇다였다. `\not`이 코퍼스 전역에서 같은 방식으로 쓰이고 있었으므로 어디서든 재현될 수 있는 문제였다.

## mrel마다 끊기는 base

KaTeX가 수식 줄바꿈을 허용하는 자리는 아무 데나가 아니다. `buildHTML`에는 TeXbook 173쪽을 그대로 인용한 주석이 있다.

```js
// The TeXBook [p.173] says "A formula will be broken only after a
// relation symbol like $=$ or $<$ or $\rightarrow$, or after a binary
// operation symbol like $+$ or $-$ or $\times$, where the relation or
// binary operation is on the ``outer level'' of the formula (i.e., not
// enclosed in {...} and not part of an \over construction)."
```
{: data-filename="assets/katex/katex.js"}

구현은 최상위 수식을 관계(`mrel`)·이항연산(`mbin`) 기호 뒤에서 끊어 각 조각을 `.base`라는, 그 안에서는 절대 쪼개지지 않는 span으로 감싼다. 여기까지는 TeX의 관례를 그대로 재현한 것이라 딱히 버그가 아니다. 문제는 `\not`이 그 자체로 하나의 관계 atom이라는 데 있다. 이 레포가 물고 있는 KaTeX 사본의 정의는 이렇다.

```js
defineMacro("\\not", '\\html@mathml{\\mathrel{\\mathrlap\\@not}}{\\char"338}');
```
{: data-filename="assets/katex/katex.js"}

`\@not`은 사선 하나짜리 심볼이고, `\mathrlap{\@not}`이 그 사선의 advance width를 0으로 만들어 오른쪽 글자와 겹쳐 그리게 한다. 그리고 그 전체를 감싼 `\mathrel{...}`가 독립된 관계 atom이 된다. 즉 `\not\in`을 쓰면 실제로는 관계 atom이 두 개 연달아 있는 셈이다(사선 하나, 그리고 `\in` 하나). `buildHTML`의 끊기 로직은 관계 atom 하나가 끝날 때마다 그 뒤를 줄바꿈 후보로 등록하므로, 사선 바로 뒤가 후보 자리가 된다. `\nobreak` 공백이 바로 뒤따르면 그 후보를 취소하는 장치가 있지만, 이 `\not` 정의에는 그게 없다.

## 인자를 통째로 삼키기

새 매크로는 `\not`에 인자를 받게 만들어, 사선과 그 뒤에 오는 것을 애초에 한 atom으로 묶어 버린다.

```js
"\\not":"\\html@mathml{\\mathrel{\\mathrlap{\\@not}#1}}{\\mathrel{\\char\"338 #1}}",
```
{: data-filename="assets/js/katex-macros.js"}

HTML 쪽은 `\mathrlap{\@not}` 뒤에 `#1`을 이어 붙여, 사선이 여전히 인자 위에 겹쳐 그려지되 그 둘이 같은 `\mathrel{...}` 안에 들어간다. `buildHTML`이 볼 때는 처음부터 쪼갤 자리가 없는 단일 atom이다. `\nobreak`에 기대는 대신, 끊을 수 있는 경계 자체를 지운 셈이다. MathML 사본도 함께 고쳤다. 원래는 combining 문자 U+0338(`\char"338`) 하나만 얹었는데, 그 뒤에 `#1`을 붙여서 스크린리더 등이 읽는 접근성 트리에서도 부정 기호와 대상이 한 덩어리로 묶이게 했다.

## 검증과 남겨둔 34개

이 정도 매크로 교체는 코퍼스 전체의 `\not` 용례를 건드리는 일이다. 커밋 메시지는 검증 결과를 이렇게 적어 뒀다. 코퍼스의 `\not` 포함 수식 482개를 구·신 매크로로 대조해 448개에서 base 수가 줄었고 신규 파싱 실패는 0건, 나머지 34개는 `cases` 셀·`\text`·아래첨자 안이라 애초에 안전했다는 것이다. 이 검증을 돌린 스크립트 자체는 커밋에 남지 않았으므로, 그 숫자들은 diff가 아니라 메시지에만 있는 사실이다.

diff에서 직접 확인되는 것은 인자 문법이 바뀌면서 깨진 네 곳이다. 매크로 인자 `#1`은 토큰 하나를 받는데, `\mathrel`은 그 자체로 제어열 토큰 하나이고 `{R}`은 별개다. `\not\mathrel{R}`이라 쓰면 `#1`엔 `\mathrel` 딱 하나만 들어가고 뒤의 `{R}`은 인자 바깥에 남아 파싱이 깨진다. 묶으려면 전체를 중괄호로 싸서 한 그룹, 곧 하나의 토큰으로 만들어야 한다.

```diff
- $y\not\mathrel{R}x$
+ $y\not{\mathrel{R}}x$
```

Order_Relations 글 두 언어판(en·ko)에서 asymmetric 정의와 그 증명, 총 네 곳이 이 형태로 쓰이고 있었다. 렌더 결과는 전과 같다. 사선 뒤에 `R`이 붙는 글리프 자체는 그대로이고, 인자를 묶는 중괄호 위치만 바뀌었다.

넓은 화면에서는 애초에 재현되지 않던 버그였다. 사용자가 좁은 창에서 감사 페이지를 열어보다 우연히 걸렸고, 고친 뒤로는 사선이 다음 줄로 넘어가는 일 자체가 구조적으로 사라졌다. `\not` 뒤에 무엇이 오든, 그 사이엔 이제 끊을 자리가 없다.
