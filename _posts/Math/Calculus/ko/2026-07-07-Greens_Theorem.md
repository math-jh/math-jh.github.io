---
title: "그린 정리"
description: "평면 영역의 경계를 따라가는 선적분을 영역 위의 이중적분으로 바꾸는 그린 정리를 단순영역에서 증명한다. 넓이 공식, 회전형과 발산형(평면 발산정리), 그리고 단순연결 영역에서 무회전 벡터장이 보존장이 됨을 본다."
excerpt: "그린 정리, 넓이 공식, 회전형과 발산형, 단순연결과 보존장"

categories: [Math / Calculus]
permalink: /ko/math/calculus/greens_theorem
sidebar: 
    nav: "calculus-ko"

date: 2026-07-07
weight: 18

---

미적분의 기본정리와 선적분의 기본정리가 공통적으로 갖고 있는 정신은 영역 내부에서 일어나는 일이 경계의 적분으로 나타난다는 것이다. 이는 나중에 발산정리와 스토크스 정리 등의 원형으로 볼 수 있으며, 이번 글에서 살펴볼 그린 정리는 이 정신의 $$2$$차원 버전이라 할 수 있다.

## 그린 정리

우선 우리는 평면 영역 $$D$$의 경계곡선 $$\partial D$$에는 두 방향 중, 영역을 왼쪽에 두고 도는 방향, 곧 바깥 경계는 반시계방향으로 도는 것을 *양의 방향<sub>positive orientation</sub>*이라 정의한다. 그럼 다음이 성립한다.

::: 정리 1 (그린)
$$D$$가 조각마다 매끄러운 단순 닫힌 곡선 $$C = \partial D$$로 둘러싸인 평면 영역이고 $$P, Q$$가 $$D$$를 포함하는 열린집합에서 $$C^1$$이면, $$C$$를 양의 방향으로 잡을 때

$$\oint_C P\mathop{dx} + Q\mathop{dy} = \iint_D \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right)\mathop{dA}$$

이다.
:::

::: 증명
먼저 $$D$$가 $$y$$에 대해 단순한 영역, 곧 

$$D = \{(x,y) \mid a \leq x \leq b,\ g_1(x) \leq y \leq g_2(x)\}$$

인 경우에 다음의 식

$$\oint_C P\mathop{dx} = -\iint_D \partial P/\partial y\mathop{dA}$$

를 보인다. 이중적분 쪽은 [§다중적분, ⁋정리 2](/ko/math/calculus/multiple_integrals#thm2)로 안쪽을 먼저 적분하면

$$\iint_D \frac{\partial P}{\partial y}\mathop{dA} = \int_a^b \bigl(P(x, g_2(x)) - P(x, g_1(x))\bigr)\mathop{dx}$$

이다. 한편 경계 $$C$$는 아래 곡선 $$y = g_1(x)$$를 $$x\colon a \to b$$로, 위 곡선 $$y = g_2(x)$$를 $$x\colon b \to a$$로 도는 두 조각으로 이루어지고, 양 옆 수직변에서는 $$x$$가 상수라 $$dx = 0$$이다. 따라서

$$\oint_C P\mathop{dx} = \int_a^b P(x, g_1(x))\mathop{dx} + \int_b^a P(x, g_2(x))\mathop{dx} = -\int_a^b \bigl(P(x,g_2) - P(x,g_1)\bigr)\mathop{dx}$$

이라 두 식을 비교하면 

$$\oint_C P\mathop{dx} = -\iint_D \partial P/\partial y\mathop{dA}$$

이다. 대칭적으로, $$D$$가 $$x$$에 대해 단순한 영역이면 

$$\oint_C Q\mathop{dy} = \iint_D \partial Q/\partial x\mathop{dA}$$

이다. 일반 영역은 이러한 조각들로 잘라 합치면 내부 경계들의 적분이 방향이 반대인 두 번의 적분으로 상쇄되어 정리가 성립한다.
:::

특히 이중적분의 피적분함수가 $$1$$이 되도록 $$P, Q$$를 고르면, 영역의 넓이를 경계에서의 선적분으로 계산할 수 있다.

::: 따름정리 2
$$D$$의 넓이는 경계 적분으로

$$\area(D) = \oint_C x\mathop{dy} = -\oint_C y\mathop{dx} = \frac{1}{2}\oint_C (x\mathop{dy} - y\mathop{dx})$$

로 주어진다.
:::

::: 증명
[정리 1](#thm1)에서 $$(P, Q) = (0, x)$$로 두면 $$Q_x - P_y = 1$$이라 

$$\oint_C x\mathop{dy} = \iint_D 1\mathop{dA} = \area(D)$$

이고, $$(P, Q) = (-y, 0)$$으로 두면 

$$\oint_C -y\mathop{dx} = \area(D)$$

이다. 셋째 식은 이 둘을 평균낸 것이다.
:::

한편, 그린 정리는 평면벡터장 $$\mathbf{F} = (P, Q)$$의 두 미분량을 각각 경계 적분으로 해석하는 두 형태로 다시 적힌다.

::: 명제 3
$$D$$의 경계 $$C$$가 양의 방향이고 $$\mathbf{F} = (P, Q)$$가 $$C^1$$이면, 단위접선 $$\mathbf{T}$$와 바깥 단위법선 $$\mathbf{n}$$에 대해

$$\oint_C \mathbf{F} \cdot \mathbf{T}\mathop{ds} = \iint_D \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right)\mathop{dA}, \qquad \oint_C \mathbf{F} \cdot \mathbf{n}\mathop{ds} = \iint_D \divergence \mathbf{F}\mathop{dA}$$

이다. 
:::

::: 증명
첫째 등식은 

$$\oint_C \mathbf{F}\cdot \mathbf{T}\mathop{ds} = \oint_C P\mathop{dx} + Q\mathop{dy}$$

가 바로 [정리 1](#thm1)의 좌변이고, 우변의 피적분함수 $$Q_x - P_y$$가 평면벡터장의 회전이다. ([§벡터장, ⁋정의 3](/ko/math/calculus/vector_fields#def3)) 

둘째 등식의 경우, 양의 방향 경계에서 바깥 단위법선이 $$\mathbf{n}ds = (dy, -dx)$$임을 쓰면 

$$\oint_C \mathbf{F}\cdot \mathbf{n}\mathop{ds} = \oint_C P\mathop{dy} - Q\mathop{dx}$$

인데, [정리 1](#thm1)을 $$(P, Q) \mapsto (-Q, P)$$에 적용하면 이것이 

$$\iint_D (P_x + Q_y)\mathop{dA} = \iint_D \divergence \mathbf{F}\mathop{dA}$$

와 같다.
:::

첫째 등식은 그린 정리와 정확히 동일한 것이며, 오직 둘째 등식만이 새로운 것이나 이 또한 직관적 의미가 명확하다. 즉, 함수 $$\mathbf{F}$$를 경계에서 <em-ko>나가는</em-ko> 방향으로 경계를 따라 모두 적분하면, 이것이 곧 divergence에 담겨있다는 것이다. 한편 우리는 앞서 [§선적분, ⁋예시 6](/ko/math/calculus/line_integrals#ex6)에서 이미 영역에 구멍이 뚫려있으면 curl이 없어도 보존장이 되지 않을 수 있다는 것을 살펴보았는데, 이는 다음과 같이 엄밀하게 적을 수 있다. 

영역이 *단순연결<sub>simply connected</sub>*이라는 것은 그 안의 임의의 닫힌 곡선을 영역 밖으로 나가지 않고 한 점까지 연속적으로 수축시킬 수 있다는 뜻으로, 직관적으로는 구멍이 없는 영역이라 생각하면 된다. 가령 원반은 단순연결이지만 중심을 뺀 원반은 그렇지 않은데, 중심을 감싸는 원을 한 점으로 줄이려면 반드시 빠진 중심을 지나야 하기 때문이다.

::: 따름정리 4
단순연결 열린 영역에서 $$C^1$$ 벡터장 $$\mathbf{F} = (P, Q)$$가 $$\partial Q/\partial x = \partial P/\partial y$$을 만족하면 $$\mathbf{F}$$는 보존장이다.
:::

::: 증명
영역이 단순연결이므로 그 안의 임의의 단순닫힌곡선 $$C$$가 둘러싸는 영역 $$D$$ 전체가 다시 영역 안에 들어간다. 이제 

$$\oint_C \mathbf{F}\cdot d\mathbf{r} = \iint_D (Q_x - P_y)\mathop{dA} = 0$$

이고, 모든 닫힌 곡선에서 적분이 $$0$$이므로 [§선적분, ⁋정리 4](/ko/math/calculus/line_integrals#thm4)에 의해 $$\mathbf{F}$$는 보존장이다.
:::

::: 예시 5 (단순연결성)
[§선적분, ⁋예시 6](/ko/math/calculus/line_integrals#ex6)의 

$$\mathbf{F} = (-y, x)/(x^2+y^2)$$

은 무회전이지만 원점을 도는 단위원에서 적분이 $$2\pi$$였다. [따름정리 4](#cor4)에 의하면 이는 오직 이 벡터장이 정의된 영역이 단순연결이 아니어야만 말이 되며, 실제로 정의역 $$\mathbb{R}^2\setminus\{0\}$$이 단순연결이 아니다. 뿐만 아니라, 원점을 품지 않는 닫힌 곡선에서는 $$\mathbf{F}$$의 적분이 모두 $$0$$이므로, 문제가 되는 것은 오직 벡터장이 정의되지 않는 원점 뿐인 것도 확인할 수 있다. 
:::
