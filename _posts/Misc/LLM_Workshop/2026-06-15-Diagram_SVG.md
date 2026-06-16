---

title: "다이어그램을 SVG로"
excerpt: "345장의 PNG 다이어그램을, 카테고리 묶음에서 글 단위 벡터로"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/diagram_svg

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-06-15
weight: 21

---

관련 파일: [`scripts/diagrams/build.sh`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/diagrams/build.sh), [`assets/diagrams/.preamble/palette.sty`](https://github.com/math-jh/math-jh.github.io/blob/main/assets/diagrams/.preamble/palette.sty), [`assets/diagrams/.preamble/diagram-style.sty`](https://github.com/math-jh/math-jh.github.io/blob/main/assets/diagrams/.preamble/diagram-style.sty)
{: .notice--info}

이 블로그의 수학 그림들은 `assets/images/Math/{카테고리}/{글제목}-N.png` 형태의 PNG였고, 대부분 LaTeX(주로 tikz·tikzcd)로 그린 것이었다. 소스는 카테고리마다 하나의 큰 scratch `.tex`(`{카테고리}.tex`)에 뭉쳐 있었다. 두 가지가 거슬렸다 — PNG는 래스터라 KaTeX로 또렷하게 렌더되는 본문 수식 옆에서 흐릿하게 번지고, 소스가 글이 아니라 카테고리 단위라 어느 그림이 어느 글 것인지 추적이 어려웠다. 약 345장을 손보는 작업이 시작됐다. 방향은 둘이었다 — 그림은 PNG에서 SVG로, 소스는 카테고리 묶음에서 글 단위로.

## 투명 배경과 교차선

PNG 시절, 화살표나 선이 교차할 때는 위에 오는 선 둘레에 흰 halo를 깔아 아래 선을 가렸다. 배경이 흰색이었으니 자연스러웠지만, 다크모드에선 그 흰 사각형이 그대로 드러난다. 사용자가 처음 떠올린 해법은 직접적이었다.

> 네가 crossing 해서 png 만들고, 그럼 예를 들어 흰색 halo가 가린다 치면, 그 다음에 magick으로 halo를 transparent하게 만들면 되잖아.

여기서 한 가지가 갈렸다. **벡터(SVG)에서는** 흰 halo가 별도의 흰 채움 도형으로 남아 있어 그것만 골라 투명하게 만들 수 있다 — 대부분의 그림은 이 방법으로 흰 배경을 들어내고 SVG로 옮겼다. 그런데 halo가 *선의 교차를 가리려고* 깔린 경우는 다르다. 그 흰 도형을 투명하게 만들면 그 아래에서 가려져 있어야 할 선이 다시 드러난다 — 어느 선이 위인지 하는 정보가 사라지는 것이다. 그래서 **교차가 있는 소수의 그림은 SVG 대신 PNG로 남겼다**(대수기하 8·호몰로지대수 2·위상수학 1장). 나머지는 전부 벡터다.

## 빌드 파이프라인

`scripts/diagrams/build.sh`가 글 단위 `.tex` 하나를 받아 그 안의 그림들을 SVG로 뽑는다. LaTeX로 DVI를 만들고, `dvisvgm --no-fonts --bbox=preview`로 글자까지 path로 펼친 벡터를 얻고, 흰 채움을 투명으로 바꾸고, 가는 글자 획을 굵히고, 본문 기준의 `em` 폭을 계산해 출력한다.

글 단위 `.tex`는 `assets/diagrams/Math/{카테고리}/{글제목}.tex`에 둔다. `\documentclass[border=2pt]{standalone}` 하나에 그림들을 `%%FIG` 구분자로 나열하는데, **`%%FIG` 옆의 설명은 글의 `![alt](...)`와 정확히 일치**시킨다 — 그래야 어느 figure가 어느 자리에 들어가는지 소스만 봐도 분명하다.

```
%%FIG commuting_triangle (Functors-1.svg)
\begin{tikzcd} ... \end{tikzcd}
```

## 크기와 글자 보정

처음엔 그림이 본문 글자에 비해 작게 나왔다. 빌드식의 배율을 1.2배로 올렸다가, 1.1배에서 멈췄다(노드 글자가 본문의 1.1배). 화살표는 굵게 잘 나왔는데 글자가 여전히 얇아 작은 크기에서 subpixel로 사라지길래, 가는 Computer Modern 획에 가느다란 stroke를 덧대 굵혔다.

가장 어이없던 건 따로 있었다. 한 `.tex`에 여러 그림을 넣고 `standalone`의 multi-page 기능으로 페이지를 쪼개려 했더니, 그 기능이 tikzcd 내부의 tikzpicture까지 같이 쪼개는 통에 화살표 라벨들이 한 점에 뭉쳐 그림이 통째로 깨졌다.

> 지금 전혀 이상한 그림이 나왔어. node도 다 겹치고 난리도 아니야.

그래서 multi-page는 버리고, 빌드 스크립트가 figure를 `%%FIG` 단위로 하나씩 따로 컴파일하는 방식으로 갔다.

## 색

강조색은 사용자가 Claude Design에서 정해 왔다 — 검정 배경 위, 순서가 있는 모노 브래스 램프(`accent1`부터 `accent5`까지). 기존에 빨강(`red!45`)으로 강조하던 곳은 `accent`로, 회색이나 `black!`으로 연하게 깔던 요소는 일괄 `black!50`으로 통일했다. 본문 참고 블록에서 쓰던 오커 계열 색이 이 브래스와 부딪혀서, 그쪽은 보라로 옮겨 따뜻한 색조를 다이어그램 강조 전용으로 비웠다.

## 작업 방식

전체를 한 번에 바꾸지 않고 글 하나씩 간다. 카테고리는 abc 순, 카테고리 안에서는 weight 순. 다이어그램이 있는 글은 한글·영어 양쪽을 같은 SVG·같은 폭으로 갱신하고, 끝날 때마다 무엇을 했는지 보고한다. 보고를 생략해도 되는 것은 다이어그램이 아예 없는 글뿐이다.

> 한 글이 끝나면 문제가 있든 없든 보고해야지. 보고 안 해도 될 때는 diagram 없을 때 뿐이야.

하는 김에 어긋난 것들도 바로잡는다. 소스 디렉토리 이름이 글과 안 맞는 경우(대수기하 소스가 실은 대수다양체·스킴이론 글의 것이거나, `Manifold`/`Manifolds`·`Lie_theory`/`Lie_Theory` 같은 케이싱 중복) 디렉토리째 정리하고, 한 카테고리가 끝나면 옛 PNG와 큰 scratch `.tex`를 지운다.

아직 진행 중이다. 345장을 한 장씩 벡터로 다시 그리는 일은 지루하기 짝이 없지만, 다 끝나고 나면 어느 글에서 얼마를 확대하든 그림이 더는 번지지 않을 것이다. 그거면 됐다.
