---
title: "선적분"
description: "곡선을 따라 스칼라장을 적분하는 스칼라 선적분과 벡터장을 적분하는 벡터 선적분(일)을 정의한다. 보존장에 대한 선적분의 기본정리와 경로독립성의 동치 조건을 보이고, 무회전이지만 보존장이 아닌 각도장을 본다."
excerpt: "스칼라·벡터 선적분과 일, 선적분의 기본정리, 경로독립과 보존장"

categories: [Math / Calculus]
permalink: /ko/math/calculus/line_integrals
sidebar: 
    nav: "calculus-ko"

date: 2026-07-08
weight: 17
published: false
---

이제 우리는 벡터함수의 적분을 살펴본다. 이를 위한 첫째 단계는 선적분으로, 이는 벡터장이 정의된 공간 $$\mathbb{R}^n$$ 안에서 정의된 곡선을 따라가며, 각각의 점에서의 벡터를 모두 더해 누적시키는 것이다. 흥미로운 것은 벡터장이 보존장이었다면 이 적분이 경로에 <em-ko>무관</em-ko>해져서 오직 끝점에만 의존한다는 것으로, 이는 [§미적분의 기본정리](/ko/math/calculus/fundamental_theorem_of_calculus)의 고차원 버전이라 할 수 있다. 

## 선적분

::: 정의 1
$$C^1$$ 곡선 $$\mathbf{r}\colon [a, b] \to \mathbb{R}^n$$ 위에서 연속인 스칼라장 $$f$$의 *선적분<sub>line integral</sub>*은

$$\int_C f\mathop{ds} = \int_a^b f(\mathbf{r}(t))\lvert \mathbf{r}'(t)\rvert \mathop{dt}$$

이다. 여기서 $$ds = \lvert \mathbf{r}'(t)\rvert \mathop{dt}$$는 호의 길이 원소이다.
:::

정의에 의해 위의 적분은 arc-length parametriztion을 사용한 적분값이므로 이는 곡선의 매개화에 의존하지 않는다. 특수한 경우로 $$f \equiv 1$$이면 $$\int_C \mathop{ds}$$가 곡선의 길이를 줄 것이다. 

이제 이를 벡터함수의 적분으로 올려주기 위해서는 

::: 정의 2
$$C^1$$ 곡선 $$\mathbf{r}\colon [a, b] \to \mathbb{R}^n$$ 위의 연속 벡터장 $$\mathbf{F}$$의 *선적분*은

$$\int_C \mathbf{F} \cdot d\mathbf{r} = \int_a^b \mathbf{F}(\mathbf{r}(t)) \cdot \mathbf{r}'(t)dt$$

이다. 단위접선벡터 $$\mathbf{T} = \mathbf{r}'/\lvert \mathbf{r}'\rvert$$로 쓰면 $$\int_C \mathbf{F}\cdot d\mathbf{r} = \int_C (\mathbf{F}\cdot \mathbf{T})ds$$이고, $$\mathbf{F}$$가 힘이면 이 값을 곡선 $$C$$를 따라 $$\mathbf{F}$$가 한 *일<sub>work</sub>*이라 한다.
:::

스칼라 선적분과 달리 벡터 선적분은 곡선의 방향에 의존한다. 곡선을 거꾸로 ($$-C$$로) 가면 $$\mathbf{T}$$가 뒤집혀 부호가 바뀌어 $$\int_{-C} \mathbf{F}\cdot d\mathbf{r} = -\int_C \mathbf{F}\cdot d\mathbf{r}$$이다. 평면에서 $$\mathbf{F} = (P, Q)$$이고 $$\mathbf{r}(t) = (x(t), y(t))$$이면 $$\int_C \mathbf{F}\cdot d\mathbf{r} = \int_C Pdx + Qdy$$로 쓰는 미분형식 표기도 흔히 쓰인다.

## 선적분의 기본정리

보존장의 선적분은 퍼텐셜의 양 끝 값 차이로 환원된다. 한 변수의 미적분의 기본정리에서 원시함수의 차로 정적분이 계산되던 것이 그대로 곡선으로 옮겨진다.

::: 정리 3 (선적분의 기본정리)
$$f$$가 $$C^1$$이고 $$C$$가 $$\mathbf{r}(a) = \mathbf{A}$$에서 $$\mathbf{r}(b) = \mathbf{B}$$로 가는 $$C^1$$ 곡선이면

$$\int_C \nabla f \cdot d\mathbf{r} = f(\mathbf{B}) - f(\mathbf{A})$$

이다. 특히 보존장의 선적분은 양 끝점에만 의존한다.
:::

::: 증명
다변수 연쇄법칙 ([§다변수함수와 편미분, ⁋정리 6](/ko/math/calculus/partial_derivatives#thm6))으로 $$\frac{d}{dt} f(\mathbf{r}(t)) = \nabla f(\mathbf{r}(t)) \cdot \mathbf{r}'(t)$$이다. 따라서

$$\int_C \nabla f \cdot d\mathbf{r} = \int_a^b \nabla f(\mathbf{r}(t)) \cdot \mathbf{r}'(t)dt = \int_a^b \frac{d}{dt} f(\mathbf{r}(t))dt = f(\mathbf{r}(b)) - f(\mathbf{r}(a))$$

인데, 마지막 등호가 미적분의 기본정리 ([§미적분의 기본정리](/ko/math/calculus/fundamental_theorem_of_calculus))이다.
:::

## 경로독립과 보존장

[정리 3](#thm3)은 보존장의 선적분이 경로에 무관함을 말한다. 놀랍게도 그 역도 성립하여, 경로독립성은 보존장임을 특징짓는다.

::: 정리 4
$$\mathbf{F}$$가 연결된 열린 영역 $$D$$에서 연속일 때, 다음은 동치이다.

1. $$\mathbf{F}$$는 $$D$$에서 보존장이다.
2. $$D$$ 안의 모든 닫힌 곡선 $$C$$에 대해 $$\oint_C \mathbf{F} \cdot d\mathbf{r} = 0$$이다.
3. $$\int_C \mathbf{F}\cdot d\mathbf{r}$$는 $$C$$의 양 끝점에만 의존하고 경로에는 무관하다.
:::

::: 증명
$$(1 \Rightarrow 3)$$은 [정리 3](#thm3)이다. $$(3 \Leftrightarrow 2)$$는 닫힌 곡선을 한 점에서 끊어 두 경로로 보고, 한 경로를 거꾸로 이으면 닫힌 곡선이 됨에서 따른다. 곧 두 경로 $$C_1, C_2$$가 같은 끝점을 가지면 $$C_1$$과 $$-C_2$$를 이은 것이 닫힌 곡선이고 $$\int_{C_1} - \int_{C_2} = \oint$$이므로, 경로독립과 닫힌 곡선 적분이 $$0$$인 것이 같다. $$(3 \Rightarrow 1)$$은 퍼텐셜을 직접 짓는다. 기준점 $$\mathbf{x}_0 \in D$$를 고정하고 $$f(\mathbf{x}) = \int_{\mathbf{x}_0}^{\mathbf{x}} \mathbf{F}\cdot d\mathbf{r}$$로 정의하면 (경로독립이라 잘 정의된다), 한 좌표방향 $$\mathbf{e}_i$$로의 차분몫 $$(f(\mathbf{x} + h \mathbf{e}_i) - f(\mathbf{x}))/h$$는 $$\mathbf{x}$$에서 $$\mathbf{x} + h \mathbf{e}_i$$로 가는 직선 선분 위의 적분을 $$h$$로 나눈 것이라 $$h \to 0$$에서 $$F_i(\mathbf{x})$$로 수렴한다. 따라서 $$\partial f/\partial x_i = F_i$$, 곧 $$\nabla f = \mathbf{F}$$이다.
:::

[벡터장, ⁋명제 6](/ko/math/calculus/vector_fields#prop6)의 무회전 조건은 보존장의 필요조건이었다. 그것이 충분조건이 되지 못하는 까닭이 경로독립성의 관점에서 분명해진다. 무회전이라도 영역에 구멍이 있으면 그 구멍을 도는 닫힌 곡선의 적분이 $$0$$이 아닐 수 있기 때문이다.

::: 예시 5 (일의 계산)
힘 $$\mathbf{F} = (y, x)$$가 점 $$(0,0)$$에서 $$(1,1)$$로 가는 포물선 $$\mathbf{r}(t) = (t, t^2)$$ ($$0 \leq t \leq 1$$)을 따라 한 일을 구하자. $$\mathbf{F}(\mathbf{r}(t)) = (t^2, t)$$, $$\mathbf{r}'(t) = (1, 2t)$$이므로 $$\mathbf{F}\cdot \mathbf{r}' = t^2 + 2t^2 = 3t^2$$이고 $$\int_C \mathbf{F}\cdot d\mathbf{r} = \int_0^1 3t^2dt = 1$$이다. 실은 $$\mathbf{F} = \nabla(xy)$$인 보존장이라, [정리 3](#thm3)으로 $$xy$$의 양 끝 값 차이 $$1\cdot 1 - 0\cdot 0 = 1$$로 곧장 같은 답이 나온다. 경로를 직선으로 바꾸어도 답은 변하지 않는다.
:::

::: 예시 6 (무회전이나 비보존인 각도장)
원점을 뺀 평면 $$\mathbb{R}^2 \setminus \{0\}$$에서

$$\mathbf{F} = \left(\frac{-y}{x^2 + y^2},\ \frac{x}{x^2 + y^2}\right)$$

를 보자. 직접 미분하면 $$\partial Q/\partial x = \partial P/\partial y = (y^2 - x^2)/(x^2+y^2)^2$$이라 [벡터장, ⁋명제 6](/ko/math/calculus/vector_fields#prop6)의 무회전 조건을 만족한다. 그런데 단위원 $$\mathbf{r}(t) = (\cos t, \sin t)$$를 따라 한 바퀴 돌면 $$\mathbf{F}(\mathbf{r}(t)) = (-\sin t, \cos t) = \mathbf{r}'(t)$$라

$$\oint_C \mathbf{F}\cdot d\mathbf{r} = \int_0^{2\pi} (\sin^2 t + \cos^2 t)dt = 2\pi \neq 0$$

이다. [정리 4](#thm4)에 의해 $$\mathbf{F}$$는 이 영역에서 보존장이 아니다. 국소적으로는 편각 $$\theta = \arctan(y/x)$$의 기울기이지만, 편각이 원점을 돌 때 $$2\pi$$만큼 불어나 한 값으로 정의되지 못하는 것이 그 원인이다. 무회전이 보존으로 이어지려면 정의역에 구멍이 없어야 한다는 [벡터장](/ko/math/calculus/vector_fields)의 단서가 여기서 구체적인 반례로 확인된다.
:::
