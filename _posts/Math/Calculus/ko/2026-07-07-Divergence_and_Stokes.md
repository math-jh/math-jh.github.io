---
title: "발산정리와 스토크스 정리"
description: "그린 정리를 공간으로 일반화하는 두 적분정리를 다룬다. 닫힌 곡면의 선속을 입체의 발산적분과 잇는 발산정리, 경계곡선의 순환을 곡면의 회전적분과 잇는 스토크스 정리를 증명하고, 무회전 벡터장의 보존성과 미분형식으로의 통일을 본다."
excerpt: "발산정리, 스토크스 정리, 무회전과 보존장, 적분정리의 통일"

categories: [Math / Calculus]
permalink: /ko/math/calculus/divergence_and_stokes
sidebar: 
    nav: "calculus-ko"

date: 2026-07-07
weight: 20
published: false
revising: true
drift_needed: true
---

우리는 그린 정리를 소개하며 이것이 미적분학의 기본정리의 2차원 analogue라는 것을 보았다. 미적분학의 마지막은 이를 고차원으로 확대하는 것으로, 역시 이들이 공유하는 정신은 영역 interior의 적분과 boundary의 적분이 이어진다는 것이다. 

## 발산정리

우선 우리는 발산정리를 보인다. 이는 $2$차원 boundary로 둘러싸인 $3$차원 공간의 적분에 대한 정리이다. 

::: 정리 1 (발산정리)
$E$가 조각마다 smooth한 closed 곡면 $\partial E$로 둘러싸인 공간의 입체이고 $\mathbf{F}$가 $E$를 포함하는 열린집합에서 $C^1$ 벡터장이면, $\partial E$를 outward로 잡을 때

$$\iint_{\partial E} \mathbf{F} \cdot d\mathbf{S} = \iiint_E \divergence \mathbf{F}\dd{V}$$

이다.
:::

::: 증명
$\mathbf{F} = (P, Q, R)$로 적고 $z$성분에 대해 

$$\iint_{\partial E} (0,0,R)\cdot d\mathbf{S} = \iiint_E \partial R/\partial z\dd{V}$$

를 보이면 $P, Q$도 symmetric하게 처리되어 셋을 더해 정리가 나온다. 

$E$가 세 좌표방향 모두로 단순한 입체, 특히 $z$방향으로는 $E = \{(x,y,z) \mid (x,y) \in D,\ u_1(x,y) \leq z \leq u_2(x,y)\}$라 하자. 오른쪽 삼중적분은 [§다중적분, ⁋정리 2](/ko/math/calculus/multiple_integrals#thm2)로 $z$를 먼저 적분하면

$$\iiint_E \frac{\partial R}{\partial z}\dd{V} = \iint_D \bigl(R(x,y,u_2) - R(x,y,u_1)\bigr)\dd{A}$$

이다. 한편 $\partial E$는 윗면 $z = u_2$, 아랫면 $z = u_1$, 옆면으로 이루어지는데, 옆면에서는 바깥 법선이 수평이라 $(0,0,R)\cdot \mathbf{n} = 0$이라 기여가 없다. 윗면은 바깥 법선이 위를 향해 선속이 $+\iint_D R(x,y,u_2)\dd{A}$, 아랫면은 아래를 향해 $-\iint_D R(x,y,u_1)\dd{A}$를 주므로, 합이 위 이중적분과 같다. 일반 입체는 이런 조각들로 잘라 합치면 내부 경계면의 선속이 방향이 반대인 두 번으로 상쇄되어 정리가 성립한다.
:::

발산정리는 closed 곡면을 통해 흘러나가는 양이 interior에서 솟아나는 양 $\divergence \mathbf{F}$를 모두 모은 것과 같음을 말한다. 이로써 발산이 "단위부피당 흘러나가는 양"이라는 직관이 정리로 확정된다. Closed 곡면 위의 선속을, 곡면을 직접 적분하는 대신 부피적분으로 바꾸어 계산할 수 있다는 점에서 실용적이기도 하다.

::: 예시 2 (선속의 부피적분 환원)
[§면적분과 선속, ⁋예시 6](/ko/math/calculus/surface_integrals#ex6)에서 반지름 $R$인 구를 통한 $\mathbf{F} = (x,y,z)$의 선속을 곡면적분으로 직접 계산해 $4\pi R^3$을 얻었다. 발산정리로는 $\divergence \mathbf{F} = 3$이라

$$\iint_{\partial E} \mathbf{F}\cdot d\mathbf{S} = \iiint_E 3\dd{V} = 3\cdot\frac{4}{3}\pi R^3 = 4\pi R^3$$

으로 같은 값이 나온다. 
:::

## 스토크스 정리

스토크스 정리는 거의 그린 정리와 같은 것으로, 이는 사실 본질적으로는 $1$차원 boundary로 둘러싸인 $2$차원 영역의 적분에 대한 정리이므로 그린 정리의 적분 영역이 $3$차원 안에서 <em-ko>휘어져서</em-ko> 들어있을 때에도 작동하도록 바꾼 것에 불과하다. 

::: 정리 3 (스토크스)
$S$가 조각마다 smooth한 방향지어진 곡면이고 그 boundary $\partial S$가 조각마다 smooth한 simple closed 곡선이며 $\mathbf{F}$가 $S$를 포함하는 열린집합에서 $C^1$이면, $\partial S$를 $S$의 방향과 맞게 (곡면을 왼쪽에 두고) 잡을 때

$$\oint_{\partial S} \mathbf{F} \cdot d\mathbf{r} = \iint_S \curl \mathbf{F} \cdot d\mathbf{S}$$

이다.
:::

::: 증명
$S$가 $C^2$ 함수 $g$의 위로 방향지어진 그래프 $z = g(x,y)$인 경우를 보이면, 일반 곡면은 그런 조각들로 잘라 합쳐 내부 boundary가 상쇄되는 것을 확인하면 된다. 따라서 이 특정 경우만 보자. 우선 boundary 위에서 $z = g(x,y)$이라 $\dd{z} = g_x\dd{x} + g_y\dd{y}$이므로

$$\oint_{\partial S} \mathbf{F}\cdot d\mathbf{r} = \oint_{\partial D} P\dd{x} + Q\dd{y} + R\dd{z} = \oint_{\partial D} (P + R g_x)\dd{x} + (Q + R g_y)\dd{y}$$

이고, 평면 영역 $D$에 [§그린 정리, ⁋정리 1](/ko/math/calculus/greens_theorem#thm1)을 적용하면 이는 

$$\iint_D \bigl[\partial_x(Q + R g_y) - \partial_y(P + R g_x)\bigr]\dd{A}$$

와 같다. $P, Q, R$가 $(x, y, g(x,y))$에서 계산된다는 것만 주의하며 연쇄법칙으로 미분하면, $R g_{xy}$와 $R g_{yx}$ 항이 [§다변수함수와 편미분, ⁋정리 7](/ko/math/calculus/partial_derivatives#thm7)로 상쇄되고, 이를 사용하여 정리하면 피적분함수가

$$(Q_x - P_y) + (Q_z - R_y)g_x + (R_x - P_z)g_y$$

가 된다. 한편 그래프의 위쪽 법선은 $\mathbf{N} = (-g_x, -g_y, 1)$이고 $\curl \mathbf{F} = (R_y - Q_z,\ P_z - R_x,\ Q_x - P_y)$이므로 $\curl \mathbf{F} \cdot \mathbf{N}$이 정확히 이와 같은 식이다. 따라서 위 이중적분은 

$$\iint_D \curl \mathbf{F}\cdot \mathbf{N}\dd{A} = \iint_S \curl \mathbf{F}\cdot d\mathbf{S}$$

이다.
:::

평면에서와 마찬가지로 다음도 성립한다. 

::: 따름정리 4
단순연결 열린 영역 $D \subseteq \mathbb{R}^3$에서 $C^1$ 벡터장 $\mathbf{F}$가 무회전($\curl \mathbf{F} = 0$)이면 $\mathbf{F}$는 보존장이다.
:::

::: 증명
$D$가 단순연결이므로 $D$ 안의 임의의 closed curve $C$는 $D$ 안에 놓인 곡면 $S$의 boundary로 채울 수 있다. 스토크스 정리로 

$$\oint_C \mathbf{F}\cdot d\mathbf{r} = \iint_S \curl \mathbf{F}\cdot d\mathbf{S} = 0$$

이고, 모든 closed 곡선에서 적분이 $0$이므로 [§선적분, ⁋정리 4](/ko/math/calculus/line_integrals#thm4)에 의해 $\mathbf{F}$는 보존장이다.
:::

::: 예시 5
벡터장 $\mathbf{F} = (-y, x, z)$의 단위원 

$$C\colon \mathbf{r}(t) = (\cos t, \sin t, 0)$$

위에서의 순환을 구하자. $\curl \mathbf{F} = (0, 0, 2)$이고, $C$를 boundary로 갖는 곡면으로 $xy$평면의 단위원판 $S$ (위 방향 법선 $\mathbf{k}$) 를 택하면 스토크스 정리로

$$\oint_C \mathbf{F}\cdot d\mathbf{r} = \iint_S \curl \mathbf{F}\cdot d\mathbf{S} = \iint_S 2\dd{A} = 2\pi$$

이다. 

스토크스 정리를 사용하지 않고 직접 계산해도 

$$\mathbf{F}(\mathbf{r}(t))\cdot \mathbf{r}'(t) = (-\sin t, \cos t, 0)\cdot(-\sin t, \cos t, 0) = 1$$

이므로 적분값이 $\oint_C = \int_0^{2\pi} \dd{t} = 2\pi$로 일치하며, boundary를 공유하는 다른 곡면, 가령 반구를 택하여 계산해도 적분값은 변하지 않는다는 것을 확인할 수 있다.
:::

---

**참고문헌**

**[Ste]** J. Stewart, *Calculus*, 8th ed., Cengage Learning, 2016.  
**[Kim]** 김홍종, *미적분학 1·2*, 제3개정판, 서울대학교출판문화원, 2020.
