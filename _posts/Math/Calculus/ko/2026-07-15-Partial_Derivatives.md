---
title: "다변수함수와 편미분"
description: "여러 변수의 함수에 대해 편미분과 기울기를 정의하고, 미분가능성을 일차 근사로 정식화한다. 다변수 연쇄법칙과 혼합편미분의 교환에 관한 클레로 정리를 다룬다."
excerpt: "편미분과 기울기, 미분가능성, 다변수 연쇄법칙"

categories: [Math / Calculus]
permalink: /ko/math/calculus/partial_derivatives
sidebar: 
    nav: "calculus-ko"

header:
    overlay_image: /assets/images/Math/Calculus/Partial_Derivatives.png
    overlay_filter: 0.5

date: 2026-07-15
last_modified_at: 2026-07-15

weight: 16

published: false
---

지금까지의 미분은 한 변수 함수에 관한 것이었다. [§미분과 도함수](/ko/math/calculus/derivatives)에서 미분이 일차 근사 $$f(a+h) \approx f(a) + f'(a)h$$임을 강조했는데, 이 관점이 여러 변수로의 확장에서 핵심이 된다. 이 글에서는 $$\mathbb{R}^n$$에서 $$\mathbb{R}$$로 가는 함수의 미분을 다룬다.

## 편미분과 기울기

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 함수 $$f(x_1, \ldots, x_n)$$의 점 $$a$$에서 변수 $$x_i$$에 대한 *편미분<sub>partial derivative</sub>*은 나머지 변수를 고정한 채 $$x_i$$로만 미분한 것이다.

$$\frac{\partial f}{\partial x_i}(a) = \lim_{h\to 0}\frac{f(a + h e_i) - f(a)}{h}$$

여기서 $$e_i$$는 $$i$$번째 표준기저벡터이다. 모든 편미분을 모은 벡터 $$\nabla f(a) = \left(\dfrac{\partial f}{\partial x_1}(a), \ldots, \dfrac{\partial f}{\partial x_n}(a)\right)$$를 $$f$$의 *기울기<sub>gradient</sub>*라 한다.

</div>

## 미분가능성

편미분은 좌표축 방향의 변화율만 보므로, 함수의 진정한 "일차 근사 가능성"을 담기에는 부족하다. 일차 근사를 직접 요구하는 것이 옳은 미분 개념이다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> $$f$$가 점 $$a$$에서 *미분가능<sub>differentiable</sub>*하다는 것은, 벡터 $$L$$이 존재하여

$$\lim_{h \to 0}\frac{f(a + h) - f(a) - L\cdot h}{\lVert h\rVert} = 0$$

이 성립하는 것이다. 이 경우 $$L = \nabla f(a)$$이고, $$f(a+h) \approx f(a) + \nabla f(a)\cdot h$$가 최선의 일차 근사이다.

</div>

편미분이 존재해도 미분가능하지 않을 수 있으나, 편미분이 연속이면 미분가능하다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> $$f$$의 모든 편미분이 $$a$$ 근방에서 존재하고 $$a$$에서 연속이면, $$f$$는 $$a$$에서 미분가능하다.

</div>

기울기는 함수가 가장 빠르게 증가하는 방향을 가리키며, 그 크기가 그 방향의 변화율이다. 임의의 단위벡터 $$u$$ 방향의 변화율인 *방향도함수*는 $$\nabla f(a)\cdot u$$로 주어진다.

## 연쇄법칙과 혼합편미분

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4 (다변수 연쇄법칙)**</ins> $$f$$가 미분가능하고 $$x(t) = (x_1(t), \ldots, x_n(t))$$가 미분가능한 곡선이면, 합성 $$t \mapsto f(x(t))$$도 미분가능하고

$$\frac{d}{dt} f(x(t)) = \nabla f(x(t)) \cdot x'(t) = \sum_{i=1}^n \frac{\partial f}{\partial x_i}\,\frac{dx_i}{dt}$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

미분가능성에 의해 $$f(x(t+\Delta t)) - f(x(t)) = \nabla f(x(t))\cdot \Delta x + o(\lVert\Delta x\rVert)$$이고, $$\Delta x = x'(t)\Delta t + o(\Delta t)$$이다. 양변을 $$\Delta t$$로 나누고 $$\Delta t \to 0$$을 취하면 오차항이 사라져 공식을 얻는다.

</details>

이계편미분에 대해서는 미분의 순서가 (적절한 연속성 아래) 문제되지 않는다.

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5 (클레로)**</ins> 두 혼합편미분 $$\dfrac{\partial^2 f}{\partial x\,\partial y}$$와 $$\dfrac{\partial^2 f}{\partial y\,\partial x}$$가 모두 존재하고 한 점 근방에서 연속이면, 그 점에서 둘이 같다.

</div>

한 변수 미분에서 적분으로 넘어갔듯, 다변수에서도 편미분의 짝으로 여러 변수에 걸친 적분이 있다. 이는 다음 글 [§다중적분](/ko/math/calculus/multiple_integrals)에서 다룬다. 다변수 미분의 엄밀한 이론 — 미분을 선형사상으로 보는 관점과 역함수·음함수 정리 — 은 해석학 [\[해석학\] §다변수 미분](/ko/math/analysis/multivariable_differentiation)에서 전개된다.
