---
title: "발산정리와 스토크스 정리"
description: "그린 정리를 공간으로 일반화하는 두 적분정리를 다룬다. 닫힌 곡면의 선속을 입체의 발산적분과 잇는 발산정리, 경계곡선의 순환을 곡면의 회전적분과 잇는 스토크스 정리를 증명하고, 무회전 벡터장의 보존성과 미분형식으로의 통일을 본다."
excerpt: "발산정리, 스토크스 정리, 무회전과 보존장, 적분정리의 통일"

categories: [Math / Calculus]
permalink: /ko/math/calculus/divergence_and_stokes
sidebar: 
    nav: "calculus-ko"

date: 2026-06-02
weight: 20
published: false
---

그린 정리는 평면 영역의 경계 선적분을 내부 이중적분과 이었다. 공간으로 올라가면 이것이 두 갈래로 갈라진다. 그린의 발산형은 닫힌 곡면의 선속을 입체의 발산적분과 잇는 발산정리로, 회전형은 경계곡선의 순환을 곡면의 회전적분과 잇는 스토크스 정리로 일반화된다. 두 정리는 미적분학의 정점이자, 더 높은 곳에서는 하나의 정리이다.

## 발산정리

<div class="proposition" markdown="1">

<ins id="thm1">**정리 1 (발산정리)**</ins> $$E$$가 조각마다 매끄러운 닫힌 곡면 $$\partial E$$로 둘러싸인 공간의 입체이고 $$F$$가 $$E$$를 포함하는 열린집합에서 $$C^1$$ 벡터장이면, $$\partial E$$를 바깥 방향으로 잡을 때

$$\iint_{\partial E} F \cdot dS = \iiint_E \operatorname{div} FdV$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$F = (P, Q, R)$$로 적고 $$z$$성분에 대해 $$\iint_{\partial E} (0,0,R)\cdot dS = \iiint_E \partial R/\partial zdV$$를 보이면, $$P, Q$$도 대칭적으로 처리되어 셋을 더해 정리가 나온다. $$E$$가 $$z$$방향으로 단순한 입체, 곧 $$E = \{(x,y) \in D,\ u_1(x,y) \leq z \leq u_2(x,y)\}$$라 하자. 오른쪽 삼중적분은 [§다중적분, ⁋정리 2](/ko/math/calculus/multiple_integrals#thm2)로 $$z$$를 먼저 적분하면

$$\iiint_E \frac{\partial R}{\partial z}dV = \iint_D \bigl(R(x,y,u_2) - R(x,y,u_1)\bigr)dA$$

이다. 한편 $$\partial E$$는 윗면 $$z = u_2$$, 아랫면 $$z = u_1$$, 옆면으로 이루어지는데, 옆면에서는 바깥 법선이 수평이라 $$(0,0,R)\cdot n = 0$$이라 기여가 없다. 윗면은 바깥 법선이 위를 향해 선속이 $$+\iint_D R(x,y,u_2)dA$$, 아랫면은 아래를 향해 $$-\iint_D R(x,y,u_1)dA$$를 주므로, 합이 위 이중적분과 같다. 일반 입체는 이런 조각들로 잘라 합치면 내부 경계면의 선속이 방향이 반대인 두 번으로 상쇄되어 정리가 성립한다.

</details>

발산정리는 닫힌 곡면을 통해 흘러나가는 알짜 유량이 내부에서 솟아나는 양($$\operatorname{div} F$$)을 모두 모은 것과 같음을 말한다. 이로써 발산이 "단위부피당 흘러나가는 양"이라는 [§벡터장](/ko/math/calculus/vector_fields)에서의 직관이 정리로 확정된다. 닫힌 곡면 위의 선속을, 곡면을 직접 적분하는 대신 부피적분으로 바꾸어 계산할 수 있다는 점에서 실용적이기도 하다.

<div class="example" markdown="1">

<ins id="ex2">**예시 2 (선속의 부피적분 환원)**</ins> [§면적분과 선속, ⁋예시 6](/ko/math/calculus/surface_integrals#ex6)에서 반지름 $$R$$인 구를 통한 $$F = (x,y,z)$$의 선속을 곡면적분으로 직접 계산해 $$4\pi R^3$$을 얻었다. 발산정리로는 $$\operatorname{div} F = 3$$이라

$$\iint_{\partial E} F\cdot dS = \iiint_E 3dV = 3\cdot\frac{4}{3}\pi R^3 = 4\pi R^3$$

으로 곧장 같은 값이 나온다. 곡면 위의 적분이 부피의 상수배 적분으로 환원되어 계산이 단숨에 끝난다.

</div>

## 스토크스 정리

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3 (스토크스)**</ins> $$S$$가 조각마다 매끄러운 경계곡선 $$\partial S$$를 갖는 방향지어진 곡면이고 $$F$$가 $$S$$를 포함하는 열린집합에서 $$C^1$$이면, $$\partial S$$를 $$S$$의 방향과 맞게 (곡면을 왼쪽에 두고) 잡을 때

$$\oint_{\partial S} F \cdot dr = \iint_S \operatorname{curl} F \cdot dS$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$S$$가 위로 방향지어진 그래프 $$z = g(x,y)$$ ($$(x,y) \in D$$) 인 경우를 보이면, 일반 곡면은 그런 조각들로 잘라 합쳐 내부 경계가 상쇄됨에서 따른다. 경계 위에서 $$z = g(x,y)$$이라 $$dz = g_xdx + g_ydy$$이므로

$$\oint_{\partial S} F\cdot dr = \oint_{\partial D} Pdx + Qdy + Rdz = \oint_{\partial D} (P + R g_x)dx + (Q + R g_y)dy$$

이고, 평면 영역 $$D$$에 [§그린 정리, ⁋정리 1](/ko/math/calculus/greens_theorem#thm1)을 적용하면 이는 $$\iint_D \bigl[\partial_x(Q + R g_y) - \partial_y(P + R g_x)\bigr]dA$$와 같다. $$P, Q, R$$가 $$(x, y, g(x,y))$$에서 평가됨에 유의해 연쇄법칙으로 미분하면, $$R g_{xy}$$와 $$R g_{yx}$$ 항이 클레로 정리로 상쇄되고 정리하면 피적분함수가

$$(Q_x - P_y) + (Q_z - R_y)g_x + (R_x - P_z)g_y$$

가 된다. 한편 그래프의 위쪽 법선은 $$N = (-g_x, -g_y, 1)$$이고 $$\operatorname{curl} F = (R_y - Q_z,\ P_z - R_x,\ Q_x - P_y)$$이므로 $$\operatorname{curl} F \cdot N$$이 정확히 같은 식이다. 따라서 위 이중적분은 $$\iint_D \operatorname{curl} F\cdot NdA = \iint_S \operatorname{curl} F\cdot dS$$이다.

</details>

스토크스 정리는 경계를 도는 순환이 곡면을 꿰뚫는 회전의 총합과 같음을 말한다. 같은 경계곡선을 가지는 곡면이라면 어느 것으로 적분해도 값이 같다는 사실도 여기서 따른다. 평면곡면에 적용하면 회전적분이 $$\iint_S (Q_x - P_y)dA$$로 줄어 그린 정리의 회전형 ([§그린 정리, ⁋명제 3](/ko/math/calculus/greens_theorem#prop3))을 회복하므로, 스토크스 정리는 그린 정리의 공간판이다. 평면에서 미뤄 둔 보존장 판정의 역방향도 공간에서 그대로 성립한다.

<div class="proposition" markdown="1">

<ins id="cor4">**따름정리 4**</ins> 단순연결 열린 영역 $$D \subseteq \mathbb{R}^3$$에서 $$C^1$$ 벡터장 $$F$$가 무회전($$\operatorname{curl} F = 0$$)이면 $$F$$는 보존장이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$D$$가 단순연결이므로 $$D$$ 안의 임의의 닫힌 곡선 $$C$$는 $$D$$ 안에 놓인 곡면 $$S$$의 경계로 채울 수 있다. 스토크스 정리로 $$\oint_C F\cdot dr = \iint_S \operatorname{curl} F\cdot dS = 0$$이고, 모든 닫힌 곡선에서 적분이 $$0$$이므로 [§선적분, ⁋정리 4](/ko/math/calculus/line_integrals#thm4)에 의해 $$F$$는 보존장이다.

</details>

<div class="example" markdown="1">

<ins id="ex5">**예시 5 (순환의 회전적분 환원)**</ins> $$F = (-y, x, z)$$의 단위원 $$C\colon r(t) = (\cos t, \sin t, 0)$$ 위 순환을 구하자. $$\operatorname{curl} F = (0, 0, 2)$$이고 $$C$$를 경계로 갖는 곡면으로 $$xy$$평면의 단위원판 $$S$$ (위 방향 법선 $$k$$) 를 택하면 스토크스 정리로

$$\oint_C F\cdot dr = \iint_S \operatorname{curl} F\cdot dS = \iint_S 2dA = 2\pi$$

이다. 직접 계산해도 $$F(r(t))\cdot r'(t) = (-\sin t, \cos t, 0)\cdot(-\sin t, \cos t, 0) = 1$$이라 $$\oint_C = \int_0^{2\pi} dt = 2\pi$$로 일치한다. 곡면을 반구로 바꾸어도 경계가 같으니 값은 변하지 않는다.

</div>

<div class="remark" markdown="1">

<ins id="rmk6">**참고 6**</ins> 미적분의 기본정리, 그린 정리, 발산정리, 스토크스 정리는 모두 "경계에서의 적분 = 내부에서 한 번 미분한 것의 적분"이라는 한 형태이다. 미분형식 $$\omega$$와 그 외미분 $$d\omega$$의 언어로 쓰면 이 넷이 하나의 일반화된 스토크스 정리 $$\int_{\partial M}\omega = \int_M d\omega$$의 특수한 경우들이다. 발산·회전·기울기는 차원과 차수에 따라 외미분 $$d$$가 드러나는 서로 다른 모습이며, 이 통일된 관점은 다양체 위의 미분형식 이론에서 본격적으로 다루어진다.

</div>
