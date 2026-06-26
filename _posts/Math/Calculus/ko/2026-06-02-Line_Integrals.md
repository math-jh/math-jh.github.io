---
title: "선적분"
description: "곡선을 따라 스칼라장을 적분하는 스칼라 선적분과 벡터장을 적분하는 벡터 선적분(일)을 정의한다. 보존장에 대한 선적분의 기본정리와 경로독립성의 동치 조건을 보이고, 무회전이지만 보존장이 아닌 각도장을 본다."
excerpt: "스칼라·벡터 선적분과 일, 선적분의 기본정리, 경로독립과 보존장"

categories: [Math / Calculus]
permalink: /ko/math/calculus/line_integrals
sidebar: 
    nav: "calculus-ko"

date: 2026-06-02
weight: 17
published: false
---

정적분이 구간 위에서의 누적이었다면, 선적분은 곡선을 따라가며 누적한다. 곡선을 따라 분포한 양을 더하면 스칼라 선적분이, 벡터장을 곡선의 진행 방향으로 누적하면 벡터 선적분, 곧 물리에서의 일이 된다. 보존장에서는 이 적분이 경로에 무관해지며, 그것이 [§미적분의 기본정리](/ko/math/calculus/fundamental_theorem_of_calculus)에 이은 또 하나의 기본정리를 이룬다.

## 스칼라 선적분

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $$C^1$$ 곡선 $$r\colon [a, b] \to \mathbb{R}^n$$ 위에서 연속인 스칼라장 $$f$$의 *선적분<sub>line integral</sub>*은

$$\int_C fds = \int_a^b f(r(t))\lvert r'(t)\rvert dt$$

이다. 여기서 $$ds = \lvert r'(t)\rvert dt$$는 호의 길이 원소이다.

</div>

호장 원소 $$ds$$로 적분하므로 선적분은 곡선의 매개화에 무관하다 ([§곡선과 벡터함수, ⁋정의 5](/ko/math/calculus/vector_functions#def5)에서 호의 길이가 매개화에 무관했던 것과 같은 이유이다). $$f \equiv 1$$이면 $$\int_C ds$$가 곡선의 길이이고, $$f$$가 가는 철사의 선밀도이면 $$\int_C fds$$는 철사의 질량이다. 곡선 위에 분포한 양을 곡선을 따라 더한다는 것이 스칼라 선적분의 뜻이다.

## 벡터 선적분과 일

힘을 받으며 곡선을 따라 움직일 때 한 일은, 각 점에서 힘의 진행 방향 성분에 이동거리를 곱해 누적한 것이다. 진행 방향은 단위접선벡터 $$T$$이므로, 일은 $$\int_C (F \cdot T)ds$$이다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> $$C^1$$ 곡선 $$r\colon [a, b] \to \mathbb{R}^n$$ 위의 연속 벡터장 $$F$$의 *선적분*은

$$\int_C F \cdot dr = \int_a^b F(r(t)) \cdot r'(t)dt$$

이다. 단위접선벡터 $$T = r'/\lvert r'\rvert$$로 쓰면 $$\int_C F\cdot dr = \int_C (F\cdot T)ds$$이고, $$F$$가 힘이면 이 값을 곡선 $$C$$를 따라 $$F$$가 한 *일<sub>work</sub>*이라 한다.

</div>

스칼라 선적분과 달리 벡터 선적분은 곡선의 방향에 의존한다. 곡선을 거꾸로 ($$-C$$로) 가면 $$T$$가 뒤집혀 부호가 바뀌어 $$\int_{-C} F\cdot dr = -\int_C F\cdot dr$$이다. 평면에서 $$F = (P, Q)$$이고 $$r(t) = (x(t), y(t))$$이면 $$\int_C F\cdot dr = \int_C Pdx + Qdy$$로 쓰는 미분형식 표기도 흔히 쓰인다.

## 선적분의 기본정리

보존장의 선적분은 퍼텐셜의 양 끝 값 차이로 환원된다. 한 변수의 미적분의 기본정리에서 원시함수의 차로 정적분이 계산되던 것이 그대로 곡선으로 옮겨진다.

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3 (선적분의 기본정리)**</ins> $$f$$가 $$C^1$$이고 $$C$$가 $$r(a) = A$$에서 $$r(b) = B$$로 가는 $$C^1$$ 곡선이면

$$\int_C \nabla f \cdot dr = f(B) - f(A)$$

이다. 특히 보존장의 선적분은 양 끝점에만 의존한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

다변수 연쇄법칙 ([§다변수함수와 편미분, ⁋정리 4](/ko/math/calculus/partial_derivatives#thm4))으로 $$\frac{d}{dt} f(r(t)) = \nabla f(r(t)) \cdot r'(t)$$이다. 따라서

$$\int_C \nabla f \cdot dr = \int_a^b \nabla f(r(t)) \cdot r'(t)dt = \int_a^b \frac{d}{dt} f(r(t))dt = f(r(b)) - f(r(a))$$

인데, 마지막 등호가 미적분의 기본정리 ([§미적분의 기본정리](/ko/math/calculus/fundamental_theorem_of_calculus))이다.

</details>

## 경로독립과 보존장

[정리 3](#thm3)은 보존장의 선적분이 경로에 무관함을 말한다. 놀랍게도 그 역도 성립하여, 경로독립성은 보존장임을 특징짓는다.

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4**</ins> $$F$$가 연결된 열린 영역 $$D$$에서 연속일 때, 다음은 동치이다.

1. $$F$$는 $$D$$에서 보존장이다.
2. $$D$$ 안의 모든 닫힌 곡선 $$C$$에 대해 $$\oint_C F \cdot dr = 0$$이다.
3. $$\int_C F\cdot dr$$는 $$C$$의 양 끝점에만 의존하고 경로에는 무관하다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$(1 \Rightarrow 3)$$은 [정리 3](#thm3)이다. $$(3 \Leftrightarrow 2)$$는 닫힌 곡선을 한 점에서 끊어 두 경로로 보고, 한 경로를 거꾸로 이으면 닫힌 곡선이 됨에서 따른다. 곧 두 경로 $$C_1, C_2$$가 같은 끝점을 가지면 $$C_1$$과 $$-C_2$$를 이은 것이 닫힌 곡선이고 $$\int_{C_1} - \int_{C_2} = \oint$$이므로, 경로독립과 닫힌 곡선 적분이 $$0$$인 것이 같다. $$(3 \Rightarrow 1)$$은 퍼텐셜을 직접 짓는다. 기준점 $$x_0 \in D$$를 고정하고 $$f(x) = \int_{x_0}^{x} F\cdot dr$$로 정의하면 (경로독립이라 잘 정의된다), 한 좌표방향 $$e_i$$로의 차분몫 $$(f(x + h e_i) - f(x))/h$$는 $$x$$에서 $$x + h e_i$$로 가는 직선 선분 위의 적분을 $$h$$로 나눈 것이라 $$h \to 0$$에서 $$F_i(x)$$로 수렴한다. 따라서 $$\partial f/\partial x_i = F_i$$, 곧 $$\nabla f = F$$이다.

</details>

[벡터장, ⁋명제 6](/ko/math/calculus/vector_fields#prop6)의 무회전 조건은 보존장의 필요조건이었다. 그것이 충분조건이 되지 못하는 까닭이 경로독립성의 관점에서 분명해진다. 무회전이라도 영역에 구멍이 있으면 그 구멍을 도는 닫힌 곡선의 적분이 $$0$$이 아닐 수 있기 때문이다.

<div class="example" markdown="1">

<ins id="ex5">**예시 5 (일의 계산)**</ins> 힘 $$F = (y, x)$$가 점 $$(0,0)$$에서 $$(1,1)$$로 가는 포물선 $$r(t) = (t, t^2)$$ ($$0 \leq t \leq 1$$)을 따라 한 일을 구하자. $$F(r(t)) = (t^2, t)$$, $$r'(t) = (1, 2t)$$이므로 $$F\cdot r' = t^2 + 2t^2 = 3t^2$$이고 $$\int_C F\cdot dr = \int_0^1 3t^2dt = 1$$이다. 실은 $$F = \nabla(xy)$$인 보존장이라, [정리 3](#thm3)으로 $$xy$$의 양 끝 값 차이 $$1\cdot 1 - 0\cdot 0 = 1$$로 곧장 같은 답이 나온다. 경로를 직선으로 바꾸어도 답은 변하지 않는다.

</div>

<div class="example" markdown="1">

<ins id="ex6">**예시 6 (무회전이나 비보존인 각도장)**</ins> 원점을 뺀 평면 $$\mathbb{R}^2 \setminus \{0\}$$에서

$$F = \left(\frac{-y}{x^2 + y^2},\ \frac{x}{x^2 + y^2}\right)$$

를 보자. 직접 미분하면 $$\partial Q/\partial x = \partial P/\partial y = (y^2 - x^2)/(x^2+y^2)^2$$이라 [벡터장, ⁋명제 6](/ko/math/calculus/vector_fields#prop6)의 무회전 조건을 만족한다. 그런데 단위원 $$r(t) = (\cos t, \sin t)$$를 따라 한 바퀴 돌면 $$F(r(t)) = (-\sin t, \cos t) = r'(t)$$라

$$\oint_C F\cdot dr = \int_0^{2\pi} (\sin^2 t + \cos^2 t)dt = 2\pi \neq 0$$

이다. [정리 4](#thm4)에 의해 $$F$$는 이 영역에서 보존장이 아니다. 국소적으로는 편각 $$\theta = \arctan(y/x)$$의 기울기이지만, 편각이 원점을 돌 때 $$2\pi$$만큼 불어나 한 값으로 정의되지 못하는 것이 그 원인이다. 무회전이 보존으로 이어지려면 정의역에 구멍이 없어야 한다는 [벡터장](/ko/math/calculus/vector_fields)의 단서가 여기서 구체적인 반례로 확인된다.

</div>
