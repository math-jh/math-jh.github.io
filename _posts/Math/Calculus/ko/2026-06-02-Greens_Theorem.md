---
title: "그린 정리"
description: "평면 영역의 경계를 따라가는 선적분을 영역 위의 이중적분으로 바꾸는 그린 정리를 단순영역에서 증명한다. 넓이 공식, 회전형과 발산형(평면 발산정리), 그리고 단순연결 영역에서 무회전 벡터장이 보존장이 됨을 본다."
excerpt: "그린 정리, 넓이 공식, 회전형과 발산형, 단순연결과 보존장"

categories: [Math / Calculus]
permalink: /ko/math/calculus/greens_theorem
sidebar: 
    nav: "calculus-ko"

date: 2026-06-02
weight: 18
published: false
---

선적분의 기본정리가 보존장의 선적분을 끝점만으로 환원했다면, 그린 정리는 일반 벡터장에 대해 평면 영역의 *경계*를 따르는 선적분을 그 *영역* 위의 이중적분과 잇는다. 경계에서의 적분과 내부에서의 적분을 맞바꾸는 이 원리는 발산정리와 스토크스 정리로 일반화되는, 적분정리들의 평면 원형이다.

## 그린 정리

평면 영역 $$D$$의 경계곡선 $$\partial D$$에는 두 방향이 있다. 영역을 왼쪽에 두고 도는 방향, 곧 바깥 경계는 반시계방향으로 도는 것을 *양의 방향<sub>positive orientation</sub>*이라 한다.

<div class="proposition" markdown="1">

<ins id="thm1">**정리 1 (그린)**</ins> $$D$$가 조각마다 매끄러운 단순 닫힌 곡선 $$C = \partial D$$로 둘러싸인 평면 영역이고 $$P, Q$$가 $$D$$를 포함하는 열린집합에서 $$C^1$$이면, $$C$$를 양의 방향으로 잡을 때

$$\oint_C Pdx + Qdy = \iint_D \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right)dA$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

먼저 $$D$$가 $$y$$에 대해 단순한 영역, 곧 $$D = \{(x,y) \mid a \leq x \leq b,\ g_1(x) \leq y \leq g_2(x)\}$$인 경우에 $$\oint_C Pdx = -\iint_D \partial P/\partial ydA$$를 보인다. 이중적분 쪽은 [§다중적분, ⁋정리 2](/ko/math/calculus/multiple_integrals#thm2)로 안쪽을 먼저 적분하면

$$\iint_D \frac{\partial P}{\partial y}dA = \int_a^b \bigl(P(x, g_2(x)) - P(x, g_1(x))\bigr)dx$$

이다. 한편 경계 $$C$$는 아래 곡선 $$y = g_1(x)$$를 $$x\colon a \to b$$로, 위 곡선 $$y = g_2(x)$$를 $$x\colon b \to a$$로 도는 두 조각으로 이루어지고 (양 옆 수직변에서는 $$x$$가 상수라 $$dx = 0$$), 따라서

$$\oint_C Pdx = \int_a^b P(x, g_1(x))dx + \int_b^a P(x, g_2(x))dx = -\int_a^b \bigl(P(x,g_2) - P(x,g_1)\bigr)dx$$

이라 두 식을 비교하면 $$\oint_C Pdx = -\iint_D \partial P/\partial ydA$$이다. 대칭적으로 $$D$$가 $$x$$에 대해 단순한 영역이면 $$\oint_C Qdy = \iint_D \partial Q/\partial xdA$$이다. 두 종류로 동시에 단순한 영역에서 두 식을 더하면 정리가 나오고, 일반 영역은 그런 조각들로 잘라 합치면 내부 경계들의 적분이 방향이 반대인 두 번의 적분으로 상쇄되어 정리가 성립한다.

</details>

## 넓이 공식

피적분 이중적분이 $$1$$이 되도록 $$P, Q$$를 고르면, 영역의 넓이가 경계 선적분으로 계산된다.

<div class="proposition" markdown="1">

<ins id="cor2">**따름정리 2**</ins> $$D$$의 넓이는 경계 적분으로

$$\operatorname{area}(D) = \oint_C xdy = -\oint_C ydx = \frac12\oint_C (xdy - ydx)$$

로 주어진다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

[정리 1](#thm1)에서 $$(P, Q) = (0, x)$$로 두면 $$Q_x - P_y = 1$$이라 $$\oint_C xdy = \iint_D 1dA = \operatorname{area}(D)$$이고, $$(P, Q) = (-y, 0)$$으로 두면 $$\oint_C -ydx = \operatorname{area}(D)$$이다. 둘을 평균하면 셋째 식이 나온다.

</details>

## 회전형과 발산형

그린 정리는 평면벡터장 $$F = (P, Q)$$의 두 미분량을 각각 경계 적분으로 해석하는 두 형태로 다시 적힌다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> $$D$$의 경계 $$C$$가 양의 방향이고 $$F = (P, Q)$$가 $$C^1$$이면, 단위접선 $$T$$와 바깥 단위법선 $$n$$에 대해

$$\oint_C F \cdot Tds = \iint_D \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right)dA, \qquad \oint_C F \cdot nds = \iint_D \operatorname{div} FdA$$

이다. 앞을 *회전형<sub>circulation form</sub>*, 뒤를 *발산형<sub>flux form</sub>*이라 한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

회전형은 $$\oint_C F\cdot Tds = \oint_C Pdx + Qdy$$가 바로 [정리 1](#thm1)의 좌변이고, 우변의 피적분함수 $$Q_x - P_y$$가 평면벡터장의 회전 ([§벡터장, ⁋정의 3](/ko/math/calculus/vector_fields#def3))이다. 발산형은 양의 방향 경계에서 바깥 단위법선이 $$nds = (dy, -dx)$$임을 쓰면 $$\oint_C F\cdot nds = \oint_C Pdy - Qdx$$인데, [정리 1](#thm1)을 $$(P, Q) \mapsto (-Q, P)$$에 적용하면 이것이 $$\iint_D (P_x + Q_y)dA = \iint_D \operatorname{div} FdA$$와 같다.

</details>

발산형은 평면에서의 발산정리로, 경계를 통해 흘러나가는 알짜 유량이 내부의 발산을 모은 것과 같음을 말한다. 회전형은 경계를 도는 순환이 내부 회전의 총합임을 말하며, 둘은 각각 공간의 발산정리와 스토크스 정리로 일반화된다. 회전형으로부터 앞서 미뤄 둔 보존장 판정의 역방향이 곧바로 따른다.

<div class="proposition" markdown="1">

<ins id="cor4">**따름정리 4**</ins> 단순연결 열린 영역에서 $$C^1$$ 벡터장 $$F = (P, Q)$$가 무회전($$\partial Q/\partial x = \partial P/\partial y$$)이면 $$F$$는 보존장이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

영역이 단순연결이므로 그 안의 임의의 단순 닫힌 곡선 $$C$$가 둘러싸는 영역 $$D$$ 전체가 다시 영역 안에 들어간다. 회전형으로 $$\oint_C F\cdot dr = \iint_D (Q_x - P_y)dA = 0$$이고, 모든 닫힌 곡선에서 적분이 $$0$$이므로 [§선적분, ⁋정리 4](/ko/math/calculus/line_integrals#thm4)에 의해 $$F$$는 보존장이다.

</details>

<div class="example" markdown="1">

<ins id="ex5">**예시 5 (타원의 넓이)**</ins> 타원 $$x^2/a^2 + y^2/b^2 = 1$$을 $$r(t) = (a\cos t, b\sin t)$$ ($$0 \leq t \leq 2\pi$$)로 매개화하면 [따름정리 2](#cor2)로

$$\operatorname{area} = \frac12\oint (xdy - ydx) = \frac12\int_0^{2\pi}\bigl(a\cos t \cdot b\cos t - b\sin t\cdot(-a\sin t)\bigr)dt = \frac12\int_0^{2\pi} abdt = \pi ab$$

이다. 경계만 알면 넓이가 나오는 이 공식이 평면측정기의 원리이다.

</div>

<div class="example" markdown="1">

<ins id="ex6">**예시 6 (각도장과 단순연결성)**</ins> [§선적분, ⁋예시 6](/ko/math/calculus/line_integrals#ex6)의 각도장 $$F = (-y, x)/(x^2+y^2)$$은 무회전이지만 원점을 도는 단위원에서 적분이 $$2\pi$$였다. [따름정리 4](#cor4)와 모순처럼 보이나, 단위원이 둘러싸는 원판은 $$F$$가 정의되지 않는 원점을 품으므로 그 위에서 그린 정리를 적용할 수 없다. 정의역 $$\mathbb{R}^2\setminus\{0\}$$이 단순연결이 아닌 것이 핵심이며, 정리의 단순연결 가정이 빠질 수 없음을 보여 준다. 실제로 원점을 품지 않는 닫힌 곡선에서는 $$F$$의 적분이 모두 $$0$$이다.

</div>
