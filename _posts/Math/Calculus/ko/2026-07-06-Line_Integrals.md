---
title: "선적분"
description: "곡선을 따라 스칼라장을 적분하는 스칼라 선적분과 벡터장을 적분하는 벡터 선적분(일)을 정의한다. 보존장에 대한 선적분의 기본정리와 경로독립성의 동치 조건을 보이고, 무회전이지만 보존장이 아닌 각도장을 본다."
excerpt: "스칼라·벡터 선적분과 일, 선적분의 기본정리, 경로독립과 보존장"

categories: [Math / Calculus]
permalink: /ko/math/calculus/line_integrals
sidebar: 
    nav: "calculus-ko"

date: 2026-07-06
weight: 17

---

이제 우리는 벡터함수의 적분을 살펴본다. 이를 위한 첫째 단계는 선적분으로, 이는 벡터장이 정의된 공간 $\mathbb{R}^n$ 안에서 정의된 곡선을 따라가며, 각각의 점에서의 벡터가 기여하는 힘들을 모두 더해 누적시키는 것이다. 흥미로운 것은 벡터장이 보존장이었다면 이 적분이 경로에 <em-ko>무관</em-ko>해져서 오직 끝점에만 의존한다는 것으로, 이는 [§미적분의 기본정리](/ko/math/calculus/fundamental_theorem_of_calculus)의 고차원 버전이라 할 수 있다. 

## 선적분

::: 정의 1
$C^1$ 곡선 $\mathbf{r}\colon [a, b] \rightarrow \mathbb{R}^n$ 위에서 연속인 scalar field $f$의 *선적분<sub>line integral</sub>*은

$$\int_C f\dd{s} = \int_a^b f(\mathbf{r}(t))\lvert \mathbf{r}'(t)\rvert \dd{t}$$

이다. 여기서 $\dd{s} = \lvert \mathbf{r}'(t)\rvert \dd{t}$는 arc length 원소이다.
:::

정의에 의해 위의 적분은 arc-length parametrization을 사용한 적분값이므로 이는 곡선의 매개화에 의존하지 않는다. 특수한 경우로 $f \equiv 1$이면 $\int_C \dd{s}$가 곡선의 길이를 줄 것이다. 

이제 이를 벡터함수의 적분으로 올려주기 위해서는 곡선의 방향을 고려하여 다음과 같이 정의해야 한다. 

::: 정의 2
$C^1$ 곡선 $\mathbf{r}\colon [a, b] \rightarrow \mathbb{R}^n$ 위의 연속 벡터장 $\mathbf{F}$의 *선적분*은

$$\int_C \mathbf{F} \cdot d\mathbf{r} = \int_a^b \mathbf{F}(\mathbf{r}(t)) \cdot \mathbf{r}'(t)\dd{t}$$

이다. 
:::

이를 단위접선벡터를 활용하여 $\mathbf{T} = \mathbf{r}'/\lvert \mathbf{r}'\rvert$로 쓰면 

$$\int_C \mathbf{F}\cdot d\mathbf{r} = \int_C (\mathbf{F}\cdot \mathbf{T})\dd{s}$$

이 되는 것을 확인할 수 있다. 특별히 평면에서 $\mathbf{F} = (P, Q)$이고 $\mathbf{r}(t) = (x(t), y(t))$이면 

$$\int_C \mathbf{F}\cdot d\mathbf{r} = \int_C P\dd{x} + Q\dd{y}$$

로 쓰는 표기도 흔히 쓰인다. 또, closed curve를 따라 적분한 결과를 나타내기 위해 $\oint$를 사용하기도 하지만, 이는 기호의 문제이고 본질적으로 새로운 내용이 더해지는 것은 없다. 

## 선적분의 기본정리

우리의 핵심 정리는 위에서 예고했듯 보존장의 선적분이 끝점에서의 함숫값 차이로 환원된다는 것이다. 

::: 정리 3 (선적분의 기본정리)
$f$가 $C^1$이고 $C$가 $\mathbf{r}(a) = \mathbf{A}$에서 $\mathbf{r}(b) = \mathbf{B}$로 가는 $C^1$ 곡선이면

$$\int_C \nabla f \cdot d\mathbf{r} = f(\mathbf{B}) - f(\mathbf{A})$$

이다. 특히 보존장의 선적분은 양 끝점에만 의존한다.
:::

::: 증명
[§다변수함수와 편미분, ⁋정리 6](/ko/math/calculus/partial_derivatives#thm6)으로 $\frac{d}{\dd{t}} f(\mathbf{r}(t)) = \nabla f(\mathbf{r}(t)) \cdot \mathbf{r}'(t)$이다. 따라서 [§미적분의 기본정리, ⁋정리 4](/ko/math/calculus/fundamental_theorem_of_calculus#thm4)를 적용하면 

$$\int_C \nabla f \cdot d\mathbf{r} = \int_a^b \nabla f(\mathbf{r}(t)) \cdot \mathbf{r}'(t)\dd{t} = \int_a^b \frac{d}{\dd{t}} f(\mathbf{r}(t))\dd{t} = f(\mathbf{r}(b)) - f(\mathbf{r}(a))$$

를 얻는다.
:::

[정리 3](#thm3)은 보존장의 선적분이 경로에 무관함을 말한다. 놀랍게도 그 역도 성립한다.

::: 정리 4
$\mathbf{F}$가 연결된 열린 영역 $D$에서 연속일 때, 다음은 동치이다.

1. $\mathbf{F}$는 $D$에서 보존장이다.
2. $D$ 안의 모든 closed curve $C$에 대해 $\oint_C \mathbf{F} \cdot d\mathbf{r} = 0$이다.
3. $\int_C \mathbf{F}\cdot d\mathbf{r}$는 $C$의 양 끝점에만 의존하고 경로에는 무관하다.
:::

::: 증명
$(1 \Rightarrow 3)$은 [정리 3](#thm3)이다. $(3 \Leftrightarrow 2)$는 closed curve를 한 점에서 끊어 두 경로로 보고, 한 경로를 거꾸로 이으면 closed curve가 되므로 자명하다. 

따라서 핵심 주장은 $(3 \Rightarrow 1)$이다. 이를 위해 potential을 직접 만들어야 한다. 기준점 $\mathbf{x}_0 \in D$를 고정하고, 임의의 $\mathbf{x}\in D$에 대해서 $f(\mathbf{x})$를 $\mathbf{x}_0$에서 $\mathbf{x}$를 따라 $\mathbf{F}$를 선적분한 값으로 두자. 이는 원래대로라면 $\mathbf{x}_0$과 $\mathbf{x}$를 잇는 곡선 $\mathbf{r}$의 선택에 의존하지만, 우리는 셋째 조건을 가정하고 있으므로 이 정의가 정당하다. 이제 한 좌표방향 $\mathbf{e}_i$로의 평균변화율 

$$\frac{f(\mathbf{x} + h \mathbf{e}_i) - f(\mathbf{x})}{h}$$

은 $\mathbf{x}$에서 $\mathbf{x} + h \mathbf{e}_i$로 가는 직선 선분 위의 적분을 $h$로 나눈 것이므로, $h \rightarrow 0$일 때 $F_i(\mathbf{x})$로 수렴하며, 따라서 $\partial f/\partial x_i = F_i$, 곧 $\nabla f = \mathbf{F}$이다.
:::

가령 다음 예시에서 이를 확인해보자.

::: 예시 5 (보존장의 예시)
$\mathbf{F} = (y, x)$를 점 $(0,0)$에서 $(1,1)$로 가는 포물선 $\mathbf{r}(t) = (t, t^2)$ ($0 \leq t \leq 1$)을 따라 적분해보자.

$$\mathbf{F}(\mathbf{r}(t)) = (t^2, t),\qquad \mathbf{r}'(t) = (1, 2t)$$

이므로 

$$\mathbf{F}\cdot \mathbf{r}' = t^2 + 2t^2 = 3t^2$$

이고 따라서 이를 적분하면 

$$\int_C \mathbf{F}\cdot d\mathbf{r} = \int_0^1 3t^2\dd{t} = 1$$

이다. 실제로, $\mathbf{F} = \nabla(xy)$이므로 [정리 3](#thm3)으로 $xy$의 양 끝 값 차이 $1\cdot 1 - 0\cdot 0 = 1$을 계산해보면 위의 계산을 복원할 수 있다. 이는 오직 끝점에만 의존하는 것으로, 가령 $\mathbf{r}(t)=(t,t)$ ($0 \leq t \leq 1$)로 주면

$$\mathbf{F}(\mathbf{r}(t))=(t,t),\qquad \mathbf{r}'(t)=(1,1)$$

이므로 $\mathbf{F}\cdot \mathbf{r}'=2t$가 되어 

$$\int_C \mathbf{F}\cdot d\mathbf{r} = \int_0^1 2t\dd{t} = 1$$

임을 확인할 수 있다.
:::

한편 [§벡터장, ⁋명제 6](/ko/math/calculus/vector_fields#prop6)에서 보존장은 무회전이라는 필요조건을 가짐을 보았다. [정리 4](#thm4)는 이것이 충분조건이 못 되는 까닭을 경로독립성의 언어로 드러낸다. 보존장은 모든 closed curve에서의 적분이 $0$이라는 것과 동치이므로, 무회전이라도 closed curve 적분이 $0$이 아닌 예가 하나라도 있으면 보존장이 아니다. 그런 예는 정의역에 구멍이 있을 때 실제로 생기는데, 바로 다음 예시가 그것이다.

::: 예시 6
원점을 뺀 평면 $\mathbb{R}^2 \setminus \{0\}$에서 정의된 벡터장

$$\mathbf{F} = \left(\frac{-y}{x^2 + y^2}, \frac{x}{x^2 + y^2}\right)$$

를 보자. 이를 직접 미분하면 

$$\frac{\partial Q}{\partial x} = \frac{\partial P}{\partial y} = \frac{y^2 - x^2}{(x^2+y^2)^2}$$

이므로, 이 벡터장은 무회전이다. 그런데 단위원 $\mathbf{r}(t) = (\cos t, \sin t)$를 따라 한 바퀴 돌면 $\mathbf{F}(\mathbf{r}(t)) = (-\sin t, \cos t) = \mathbf{r}'(t)$라

$$\oint_C \mathbf{F}\cdot d\mathbf{r} = \int_0^{2\pi} (\sin^2 t + \cos^2 t)\dd{t} = 2\pi \neq 0$$

이다. [정리 4](#thm4)에 의해 $\mathbf{F}$는 이 영역에서 보존장이 아니다. 이는 국소적으로는 이 벡터장이 편각 $\theta = \arctan(y/x)$의 기울기로 나타낼 수 있지만, 편각이 원점을 돌 때 $2\pi$만큼 불어나 한 값으로 정의되지 못하는 것이 그 원인이다. 
:::

---

**참고문헌**

**[Ste]** J. Stewart, *Calculus*, 8th ed., Cengage Learning, 2016.  
**[Kim]** 김홍종, *미적분학 1·2*, 제3개정판, 서울대학교출판문화원, 2020.
