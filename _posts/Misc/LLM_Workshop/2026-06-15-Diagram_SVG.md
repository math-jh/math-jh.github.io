---

title: "TikZ 다이어그램의 SVG 빌드와 색 체계"
excerpt: "글 단위 tex에서 그림마다 SVG를 뽑아 본문에 인라인하고, 테마별 색은 CSS가 다시 입힌다"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/diagram_svg

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-06-15
last_modified_at: 2026-11-02
weight: 20

---

관련 파일: [`scripts/diagrams/build.sh`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/diagrams/build.sh), [`scripts/diagrams/check_diagram_colors.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/diagrams/check_diagram_colors.py), [`assets/diagrams/.preamble/palette.sty`](https://github.com/math-jh/math-jh.github.io/blob/main/assets/diagrams/.preamble/palette.sty), [`assets/diagrams/.preamble/diagram-style.sty`](https://github.com/math-jh/math-jh.github.io/blob/main/assets/diagrams/.preamble/diagram-style.sty), [`_plugins/diagram_tag.rb`](https://github.com/math-jh/math-jh.github.io/blob/main/_plugins/diagram_tag.rb), [`_sass/_diagram-colors.scss`](https://github.com/math-jh/math-jh.github.io/blob/main/_sass/_diagram-colors.scss)
{: .notice--info}

이 블로그의 수학 그림은 TikZ·tikz-cd로 그린다. 소스는 글 하나에 `.tex` 하나씩 두고, `scripts/diagrams/build.sh`가 그림마다 SVG를 뽑고, 본문의 `diagram` 태그가 그 SVG를 페이지에 인라인한다. 색은 CSS가 테마에 맞춰 다시 입힌다. 원래 그림들은 카테고리마다 하나씩 있는 큰 scratch `.tex`(`{카테고리}.tex`)에서 뽑은 PNG였다. 래스터라서 KaTeX로 또렷하게 렌더되는 본문 수식 옆에서 흐릿하게 번졌고, 소스가 카테고리 단위라 어느 그림이 어느 글 것인지 추적하기 어려웠다. 약 345장을 글 단위 벡터로 옮긴 것은 그 두 가지 때문이다.

## 글 단위 소스와 `%%FIG` 분할

글 단위 `.tex`는 `assets/diagrams/Math/{카테고리}/{글제목}.tex`에 있다. `\documentclass[border=2pt]{standalone}` 프리앰블 하나 아래에 그림들을 `%%FIG` 줄로 구분해 나열한다. 공용 패키지(`palette`·`diagram-style`·`Operators`·`quiver`)는 `assets/diagrams/.preamble/`에 있고, 빌드가 `TEXINPUTS`에 이 경로를 넣는다.

```latex
%%FIG commuting_triangle (Functors-1.svg)
\begin{tikzcd} ... \end{tikzcd}
```

`%%FIG` 옆의 설명은 본문 태그의 `alt`와 글자까지 같게 쓴다. 그래야 소스만 보고도 어느 그림이 글의 어디에 들어가는지 알 수 있다. 괄호 안은 출력 파일명이고, 그 확장자가 출력 형식이다.

가장 어이없던 실패는 여러 그림을 한 번에 컴파일하려던 때 나왔다. `standalone`의 multi-page 기능으로 그림마다 페이지를 쪼개려 했더니, 그 기능이 tikz-cd 내부의 tikzpicture까지 같이 쪼개서 화살표 라벨이 한 점에 뭉쳤다.

> 지금 전혀 이상한 그림이 나왔어. node도 다 겹치고 난리도 아니야.

그래서 `build.sh`는 그림을 하나씩 따로 컴파일한다. 스크립트 안의 짧은 Python이 `\begin{document}` 앞의 프리앰블을 떼어 두고, 본문을 `%%FIG` 줄에서 잘라 조각마다 프리앰블을 붙인 한 쪽짜리 `fig-N.tex`를 만든다. 같은 단계에서 마커의 괄호를 읽어 `manifest.tsv`(번호, 출력 이름, 확장자)를 쓰고, 뒤의 루프가 이 목록대로 컴파일과 변환을 돌린다.

## `build.sh`의 변환 단계

그림 하나는 `latex` → DVI → `dvisvgm --no-fonts --bbox=preview` → 글자 획 굵히기 → 색 검사를 거쳐 SVG가 된다. `--no-fonts`는 글자를 폰트 대신 path로 펼친다. 글리프 path는 `<defs>`에 한 번 정의되고 본문에서 `<use>`로 참조되므로, 보는 쪽에 Computer Modern이 없어도 같은 모양이 나온다.

가는 Computer Modern 획은 본문 크기에서 subpixel로 사라진다. 그래서 `<use>`마다 0.20pt의 stroke를 덧대는데, stroke 색은 그 글리프의 fill 색이다. 검정으로 고정하면 accent 색 라벨에 검정 테두리가 둘러져 색이 탁해진다. 태그를 앞에서부터 훑으면서 `<g fill=...>`의 스택을 유지하고, `<use>`에 자기 `fill`이 없으면 가장 가까운 조상의 것을, 그것도 없으면 검정을 쓴다.

```python
elif re.match(r'<use\s', tag):
    fm = fill_re.search(tag)
    fill = fm.group(1) if fm else (stack[-1] if stack else '#000')
    if fill != 'none':
        out.append(s[pos:m.start()])
        out.append(tag.replace('<use ', f"<use stroke='{fill}' stroke-width='{bold}' stroke-linejoin='round' ", 1))
        pos = m.end()
```
{: data-filename="scripts/diagrams/build.sh"}

굵기는 `--bold PT`로 바꾼다. 마지막으로 SVG의 고유 폭(pt)에서 본문에 쓸 폭을 계산해 출력한다. `width_em = SCALE × pt / BASEFONT`이고 `BASEFONT=10`, `SCALE=1.1`이라 노드 글자가 본문 글자의 1.1배가 된다. `diagram-style.sty`는 그림 안의 글꼴을 줄이지 않고, 선 굵기 0.7pt와 Stealth 화살촉을 기본으로 둬서 이 배율에서 선이 흐려지지 않게 한다. 타겟은 여러 개를 받아 순서대로 빌드하므로 카테고리 하나를 다시 뽑는 것도 한 줄이다.

## 흰 지우개 페인트와 교차선

TikZ는 무언가를 가려야 하는 곳에 흰색을 칠한다. 교차하는 화살표에서 위쪽 선 둘레의 halo, 이중선 화살표와 등호의 심, 라벨 뒤의 white-out 상자, puncture 표시가 다 그렇다. 흰 배경에서는 보이지 않지만 다크 모드처럼 순백이 아닌 배경에서는 흰 띠와 얼룩으로 드러난다. 사용자가 처음 떠올린 해법은 이랬다.

> 네가 crossing 해서 png 만들고, 그럼 예를 들어 흰색 halo가 가린다 치면, 그 다음에 magick으로 halo를 transparent하게 만들면 되잖아.

래스터에서는 흰 픽셀을 투명으로 바꾸면 된다 (`--png` 경로의 `magick -fill none -opaque white`가 지금도 그 일을 한다). 벡터에서는 다르다. 흰 halo는 별도의 흰 채움 도형으로 남아 있어서, 그것을 투명하게 만들면 그 아래에서 가려져 있어야 할 선이 다시 보이고 어느 선이 위인지가 사라진다.

`white_eraser_to_mask.py`는 이것을 벡터 절개로 푼다. 흰 요소를 지우고, 그보다 먼저 그려진 것 전부를 luminance `<mask>`로 감싼다. mask에는 전체를 살리는 흰 사각형과 지우개 실루엣을 검정으로 바꾼 복사본이 들어가므로, 실루엣과 겹치는 부분에만 진짜 구멍이 뚫린다. 스크립트는 추측하지 않는다. 흰 페인트가 변환 없는 `<g id='page1'>` 바로 아래의 self-closed 요소가 아니거나, 결과가 XML로 파싱되지 않거나, mask 밖에 흰 페인트가 남거나, 원본의 path 데이터가 하나라도 사라지면 그 파일은 쓰지 않고 중단한다.

그런데 SVG가 본문에 인라인되자 절개 경계에서 안티앨리어싱이 남기는 반투명 잔흔이 눈에 띄었다. 그래서 지금은 흰 지우개를 실제 흰 도형으로 두고, CSS가 `#fff`를 페이지 배경색으로 불투명하게 덧칠한다. 덧칠된 halo는 여전히 아래 선을 가리므로 교차의 위아래가 유지된다. mask로 바꿨던 31장은 역변환 결과가 mask 이전 SVG와 바이트 단위로 같은 것만 되돌렸고, `build.sh`의 `STRIP` 기본값은 0이다. `--strip`은 `<img>`로 렌더되어 CSS가 닿지 않는 파일에 한해 mask 변환을 켠다. 지우개를 구멍으로 바꾸는 스크립트를 짜고 이틀 뒤에 그 구멍들을 도로 메웠는데, 스크립트는 그 옵션 하나 뒤에서 아직 쓸 날을 기다리고 있다.

## `diagram` 태그의 인라인 SVG와 가로 스크롤

본문은 `{% raw %}{% diagram Math/카테고리/글제목-N.svg width="20em" alt="..." %}{% endraw %}` 한 줄로 그림을 넣는다. `_plugins/diagram_tag.rb`는 SVG 파일을 읽어 `<figure class="diagram">` 안에 그대로 인라인한다. `<img>`로 참조한 SVG는 자기 완결된 별도 문서라 페이지의 CSS가 내부 요소에 닿지 않는다. 인라인하면 `stroke`·`fill` 속성이 페이지 DOM의 일부가 되어 속성 선택자로 색을 바꿀 수 있다.

인라인에는 손질이 두 가지 따른다. dvisvgm이 매기는 글리프 id(`g1-101` 같은)는 한 페이지에 그림이 여럿 실리면 충돌하므로, 태그가 경로의 MD5 앞 6자리와 같은 파일의 재등장 순번으로 접두를 만들어 `id`·`href`·`url(#…)`를 모두 바꾼다. 그리고 출력을 한 줄로 눌러서 인용 블록(`>`) 안의 임베드가 kramdown에서 깨지지 않게 한다. PNG와, 색을 열거할 수 없는 green-ramp 예외 4장은 인라인하지 않고 `<img class="invert">`로 렌더해 다크 모드에서 `invert(1) hue-rotate(180deg)` 필터를 받는다.

폭은 figure와 svg 양쪽에 건다. 본문보다 넓은 그림에 대한 사용자의 요청은 이랬다.

> 지금 폭 긴 diagram들이 기본적으로 삐져나가게 되어 있거든? svg로 구운거 말하는거야. 이게 삐져나가는 대신, x방향 스크롤하게 해 줄래? 지금 참고로 POT 글의 5번째 diagram이 그렇게 되어 있어서, 지금은 수동으로 폭을 줄여놨어.

폭이 figure의 `style`에만 있고 SVG가 `width:100%`로 figure를 따라가면, figure가 본문보다 넓을 때 둘이 같이 본문 밖으로 나간다. 그래서 SVG가 지정 폭을 직접 갖고, figure는 본문 폭에서 멈춰 그 안에서 가로로 스크롤된다.

```ruby
svg = svg.sub('<svg ', %(<svg style="width:#{width || '100%'};height:auto" ))
```
{: data-filename="_plugins/diagram_tag.rb"}

```scss
figure.diagram {
  max-width: 100%;
  overflow-x: auto;
  overflow-y: hidden;

  svg { max-width: none; }
}
```
{: data-filename="_sass/_diagram-colors.scss"}

`width`가 없는 그림은 `100%`라서 본문 폭을 따른다. 스크롤바는 [스크롤바 리팩토링](/ko/llm_workshop/scrollbar_refactor)에서 `.katex-display`용으로 만든 4px 직각, 트랙 없는 모양이다. `_base.scss`의 선택자 목록과 두 스킨의 thumb 색(`#bfa46a`, `#8f7434`)에 `figure.diagram`이 같이 들어 있어서, 수식과 그림이 넘칠 때 같은 스크롤바가 뜬다.

## 의미 기반 색 체계

tex 쪽 색은 `palette.sty`의 세 단계 브래스 램프다. accent1 브래스(`#a56f14`), accent2 브론즈, accent3 코코아이고, 강조는 accent1부터 쓴다. 이 색들은 사용자가 Claude Design에서 정해 왔다. 옛 그림의 빨강(`red!45`) 강조는 accent로, 회색이나 `black!`으로 연하게 깔던 요소는 `black!50`으로 통일했다. 공리·추측에 쓰는 `misc` 박스는 오커 색이 이 브래스와 부딪혀서 보라로 옮겼고, 따뜻한 색조는 다이어그램 강조 전용으로 남았다.

tex가 찍은 색값(`#333`, `#906b40` 같은 16진수)을 그대로 두면 라이트와 다크가 같은 색이 된다. `_sass/_diagram-colors.scss`는 이 값들을 속성 선택자로 하나씩 잡아 역할별로 다시 정의한다. 잉크(`#000`과 fill 속성이 없는 글리프)는 `currentColor`로 본문 글자색을 따른다. 회색은 tex의 `black!N` 비율 그대로 `mix($text-color, $background-color, N%)`다. 음영과 연한 accent fill은 tex가 흰색과 섞은 `accentN!K`를 배경색과의 `mix`로 바꾼 것이다. 흰 지우개는 배경색이다.

```scss
[stroke='#000'] { stroke: currentColor; }
[stroke='#333'] { stroke: mix($text-color, $background-color, 80%); }
[fill='#bb934f'] { fill: mix($diag-accent1, $background-color, 75%); }
[fill='#fff'] { fill: $background-color; }
```
{: data-filename="_sass/_diagram-colors.scss"}

라이트와 다크 엔트리(`main.scss`·`main_dark.scss`)가 이 파일을 스킨 변수만 달리 컴파일하므로 같은 규칙이 테마마다 다른 값이 된다. accent 원색은 다크에서 따로 다뤄야 했다. 라이트의 대비 사다리(accent1 3.6:1 < accent2 7.8:1 < accent3 12.6:1)를 다크에서는 순서만 뒤집어 재현해야 하는데, accent1과 accent3을 그대로 맞바꾸면 코코아가 다크 배경에서 1.3:1로 묻힌다. 그래서 `main_dark.scss`의 다크 전용 램프는 브래스를 글자색 쪽으로 끌어올려 만든다.

```scss
$diag-dark1: $diag-accent1;                          // ≈4.5:1
$diag-dark2: mix($diag-accent1, $text-color, 55%);   // ≈8:1
$diag-dark3: mix($diag-accent1, $text-color, 25%);   // ≈12:1
```
{: data-filename="assets/css/main_dark.scss"}

이 규칙 목록은 유한하다. 새 그림이 목록에 없는 색을 쓰면 다크 모드에서 라이트와 같은 색으로 남는다. `check_diagram_colors.py`는 두 CSS 소스의 속성 선택자에서 색을 파싱해 allowlist를 만들고, SVG에 그 밖의 색이 있으면 stderr에 경고한다. `build.sh`가 SVG를 하나 뽑을 때마다 부르지만 빌드를 막지는 않는다. allowlist가 CSS에서 유도되므로 규칙을 추가하면 경고도 따라 사라진다.

## 345장 전환의 작업 순서

전환은 한 번에 하지 않고 글 하나씩 했다. 카테고리는 abc 순, 카테고리 안에서는 weight 순이다. 다이어그램이 있는 글은 한국어·영어 양쪽을 같은 SVG·같은 폭으로 바꾸고, 글 하나가 끝날 때마다 보고했다.

> 한 글이 끝나면 문제가 있든 없든 보고해야지. 보고 안 해도 될 때는 diagram 없을 때 뿐이야.

하는 김에 어긋난 것도 바로잡았다. 대수기하 소스가 실은 대수다양체·스킴이론 글의 것이거나, `Manifold`/`Manifolds`·`Lie_theory`/`Lie_Theory`처럼 케이싱만 다른 디렉토리가 겹쳐 있으면 디렉토리째 정리했다. 카테고리 하나가 끝나면 옛 PNG와 큰 scratch `.tex`를 지웠다.

교차가 있는 그림은 전환 중에 PNG로 남겨 두었다가, 흰 지우개를 벡터에서 다룰 수 있게 된 뒤 SVG로 옮겼다. 이제 LaTeX에서 나오는 래스터는 없고, 본문의 그림 임베드는 전부 `diagram` 태그다. `assets/images/Math/`에 남은 PNG 9장은 tex 소스가 없는 손그림과 외부 래스터다.
