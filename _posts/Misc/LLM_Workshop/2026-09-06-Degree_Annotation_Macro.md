---

title: "복합체 항 아래 degree를 적는 매크로"
excerpt: "여접 복합체 글이 요구한 매크로 다섯은 KaTeX와 다이어그램 sty 양쪽에 한 줄씩 늘었고, 여섯째 \\at은 사용자가 언더셋과 색을 두고 마음을 몇 번 바꾼 끝에 브래스색 degree 표시로 자리를 잡았다"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/degree_annotation_macro

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-09-06
last_modified_at: 2026-11-02
weight: 51

---

관련 파일: [`assets/js/katex-macros.js`](https://github.com/math-jh/math-jh.github.io/blob/main/assets/js/katex-macros.js), [`assets/diagrams/.preamble/Operators.sty`](https://github.com/math-jh/math-jh.github.io/blob/main/assets/diagrams/.preamble/Operators.sty), [`_sass/_diagram-colors.scss`](https://github.com/math-jh/math-jh.github.io/blob/main/_sass/_diagram-colors.scss), [커밋 cd136751](https://github.com/math-jh/math-jh.github.io/commit/cd136751), [커밋 cbb78517](https://github.com/math-jh/math-jh.github.io/commit/cbb78517)
{: .notice--info}

9월 초에 쓰던 여접 복합체(cotangent complex) 글이 며칠에 걸쳐 매크로 여섯 개를 새로 요구했다. naive cotangent complex $\NL$, full cotangent complex $\LL$, Lichtenbaum–Schlessinger complex에 쓰이는 $\Rel$·$\TrivRel$, obstruction class를 가리키는 $\ob$. 다섯은 여느 때처럼 KaTeX 쪽과 다이어그램 LaTeX 쪽에 한 줄씩 늘어나는 것으로 끝났다. 여섯째는 그렇지 않았다.

## 이름 하나에 두 정의

`katex-macros.js`와 `assets/diagrams/.preamble/Operators.sty`는 서로 파생할 수 없는 언어 경계를 사이에 두고 같은 어휘를 각자 정의한다. 두 파일 머리에 나란히 적힌 주석이 그 규칙을 명시한다.

```
의도된 이중 유지: 여기가 본문 수식 매크로의 정본이고, 다이어그램 LaTeX 쪽
assets/diagrams/.preamble/Operators.sty 가 겹치는 어휘를 같은 이름·같은 렌더로
재정의한다 (JS↔LaTeX 라 파생 불가). 겹치는 매크로를 고치면 저쪽도 맞출 것.
```
{: data-filename="assets/js/katex-macros.js"}

두 파일을 기계로 대조하는 게이트는 없다. 맞추는 일은 이 주석을 읽은 손의 몫이고, $\LL$·$\NL$·$\ob$·$\Rel$·$\TrivRel$은 그 규칙대로 양쪽에 한 줄씩 붙었다.

```js
// cotangent complexes
"\\LL":"\\mathbb{L}",
"\\NL":"\\LL^{\\mathrm{naive}}",
```
{: data-filename="assets/js/katex-macros.js"}

```
%% Cotangent complexes

\newcommand{\LL}{\mathbb{L}}
\newcommand{\NL}{\LL^{\mathrm{naive}}}
```
{: data-filename="assets/diagrams/.preamble/Operators.sty"}

$\Rel$·$\TrivRel$·$\ob$도 같은 모양이다. sty 쪽에 `\DeclareMathOperator` 세 줄, JS 쪽에 `\operatorname` 세 줄. 다섯 개를 합쳐도 diff는 열 몇 줄이다.

## 언더셋 degree 숫자의 브래스색

여섯째 `\at`은 글의 본문이 아니라 표기 방식을 두고 나왔다. naive cotangent complex를 두 항짜리 복합체로 적을 때, 어느 항이 degree 1이고 어느 항이 degree 0인지를 매번 산문으로 짚어야 했다.

> 언더브레이스 비슷한 건데, 언더브레이스에서 괄호만 없는 거 혹시 없을까? 그러니까 지금 코호몰로지 쓸 때, 거기 밑에다가 조그맣게 1,0 해가지고 어디 디그리가 어딘지 써주면 굳이 산문에서 디그리 얘기 꼬박꼬박 안 해줘도 될 것 같아서.

`\underset`으로 시작했지만 방향은 한 번 뒤집혔다. "다른 사람들이 이거 어떻게 처리해?"라고 관례를 물은 다음 나온 답은 "언더셋 하지 말고 그냥 산문으로 한 번 말하고 끝내기로 하자"였다. 몇 분 뒤 다시 뒤집혔다.

> 미안 마음이 또 바뀌었어. Underset으로 하되. 내가 지금 Underset 표기에서 약간 걸리는 거는 1이랑 0이 생각보다 좀 잘 보이게 돼 있어 가지고 그렇거든. 색을 바꿔볼까? 어차피 블로그니까. 약간 회색으로?

회색으로 죽이는 안은 곧바로 다시 뒤집혔다. 뮤티드 그레이로 넣어 보라고 해놓고는, 결과를 보고 마음을 바꿨다.

> 눈에 잘 띄게 그리고 다른 그래프에서도 맞게. 색깔을 브레스 골드색으로 하는 것도 나쁘지 않은 것 같은데 어떻게 생각하는지.

최종 색은 `#a56f14`다. `_sass/_diagram-colors.scss`의 `$diag-accent1`, `palette.sty`의 `accent1`(RGB 165,111,20)과 같은 값으로, 다이어그램에서 강조에 쓰는 브래스 톤이다. 색만 죽이는 게 아니라 숫자가 항에 붙는 느낌도 문제라는 걸 사용자가 짚었으므로, 첫 정의부터 색과 세로 간격을 같이 넣었다.

## `\vphantom`·`\smash[b]`로 맞춘 항의 depth

지금 정의는 이렇다.

```js
"\\at":"\\underset{\\rule{0pt}{0.8em}\\textcolor{##a56f14}{#1}}{\\mkern1mu\\vphantom{X_{X/X}}\\smash[b]{#2}\\mkern1mu}",
```
{: data-filename="assets/js/katex-macros.js"}

`#`이 KaTeX 매크로 인자 기호와 겹치므로 색의 리터럴 `#`은 TeX 관례대로 `##`로 두 번 적는다. 밑에 붙는 쪽의 `\rule{0pt}{0.8em}`은 폭 0짜리 strut으로, 항과 숫자 사이에 세로 간격을 준다.

항 쪽의 장치는 두 번째 커밋 cbb78517에서 들어왔다. 첫 정의는 `#2`를 그대로 받았는데, $\mathfrak{a}/\mathfrak{a}^2$처럼 아래첨자 없는 항과 $\Omega_{B/A}\otimes_BC$처럼 아래첨자가 있는 항을 나란히 두면 후자의 depth가 더 깊어 밑에 붙는 숫자의 높이가 어긋났다. 지금은 `\vphantom{X_{X/X}}`가 이중 아래첨자 깊이의 보이지 않는 버팀대를 세워 모든 항의 depth를 그 값으로 고정하고, `\smash[b]`가 실제 항의 depth를 무시하게 만든다. 양옆의 `\mkern1mu`는 항 주위에 좁은 수평 여백을 낸다. 그래서 $\NL_{C/A}=[\at{1}{\mathfrak{a}/\mathfrak{a}^2}\to\at{0}{\Omega_{B/A}\otimes_BC}]$처럼 써도 숫자 1과 0이 같은 높이에 나란히 놓인다.

## KaTeX에만 있는 `\at`

`\at`은 `katex-macros.js`에만 있고 `Operators.sty`에는 없다. 겹치는 매크로를 고치면 양쪽을 맞추라는 게 표준 규칙인데, 여기서는 겹칠 게 없다. $\LL$이나 $\Rel$은 그 자체로 수학적 대상을 가리키는 기호라 다이어그램에서도 같은 기호가 나오면 같은 이름으로 부를 이유가 있지만, `\at`은 대상이 아니라 렌더 방식이다. `assets/diagrams/` 아래의 다이어그램 소스 중에 `\at`을 쓰는 것은 지금도 없으니, 옮겨 적을 자리 자체가 없다.

지금 `\at{`는 여접 복합체 글 말고도 Gromov–Witten 시리즈의 마디 곡선 변형, 안정사상 모듈라이, perfect obstruction theory 글에서 쓰인다. 1과 0을 적으려고 나온 매크로인데, 안정사상과 perfect obstruction theory 글의 복합체는 degree $-1$과 $0$에 놓이고 여접 복합체 글의 Lichtenbaum–Schlessinger complex는 $2$까지 받는다.
