---
title: "다변수 미분"
description: "다변수함수의 미분을 일차근사를 주는 선형사상으로 정의하고, 야코비 행렬로 표현한다. 연쇄법칙을 선형사상의 합성으로 깔끔하게 증명하고, 편미분이 연속이면 미분가능함을 보인다."
excerpt: "선형사상으로서의 미분, 야코비 행렬, 연쇄법칙"

categories: [Math / Analysis]
permalink: /ko/math/analysis/multivariable_differentiation
sidebar: 
    nav: "analysis-ko"

header:
    overlay_image: /assets/images/Math/Analysis/Multivariable_Differentiation.png
    overlay_filter: 0.5

date: 2026-06-02
last_modified_at: 2026-06-02
weight: 19

published: false
---

[\[미적분학\] §다변수함수와 편미분](/ko/math/calculus/partial_derivatives)에서 편미분과 기울기를 다루었다. 다변수 미분의 본질을 가장 잘 드러내는 관점은 미분을 하나의 *선형사상* — 함수를 한 점 근방에서 가장 잘 근사하는 일차사상 — 으로 보는 것이며, 이것이 한 변수의 "$$f(a+h)\approx f(a)+f'(a)h$$"를 곧바로 일반화한다.

## 선형사상으로서의 미분

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $$f : \mathbb{R}^n \to \mathbb{R}^m$$이 점 $$a$$에서 *미분가능<sub>differentiable</sub>*하다는 것은, 선형사상 $$Df(a) : \mathbb{R}^n \to \mathbb{R}^m$$이 존재하여

$$\lim_{h \to 0}\frac{\lVert f(a + h) - f(a) - Df(a)h\rVert}{\lVert h\rVert} = 0$$

이 성립하는 것이다. 이 $$Df(a)$$를 $$f$$의 $$a$$에서의 *(전)미분*이라 한다.

</div>

미분이 선형사상이라는 점이 한 변수와의 본질적 차이이다. 한 변수에서는 그 선형사상이 수 $$f'(a)$$를 곱하는 것이었다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> $$f$$가 $$a$$에서 미분가능하면 모든 편미분이 존재하고, $$Df(a)$$를 표준기저로 나타낸 행렬은 야코비 행렬

$$J_f(a) = \left(\frac{\partial f_i}{\partial x_j}(a)\right)_{i,j}$$

이다. 특히 $$Df(a)$$는 유일하다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

정의 1에서 $$h = t e_j$$ ($$t \to 0$$) 로 두면 $$\dfrac{f(a + te_j) - f(a)}{t} \to Df(a)e_j$$이고, 좌변의 극한은 $$j$$번째 편미분 벡터 $$\left(\dfrac{\partial f_i}{\partial x_j}(a)\right)_i$$이다. 따라서 $$Df(a)$$의 $$j$$번째 열이 그 편미분 벡터이다.

</details>

## 연쇄법칙

선형사상 관점의 진가는 연쇄법칙이 사상의 합성으로 깔끔하게 표현되는 데 있다.

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3 (연쇄법칙)**</ins> $$f$$가 $$a$$에서, $$g$$가 $$b = f(a)$$에서 미분가능하면 $$g \circ f$$가 $$a$$에서 미분가능하고

$$D(g \circ f)(a) = Dg(f(a)) \circ Df(a)$$

이다. 행렬로는 야코비 행렬의 곱 $$J_{g\circ f}(a) = J_g(b)\,J_f(a)$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$A = Df(a)$$, $$B = Dg(b)$$로 두자. 미분가능성에서 $$f(a+h) = b + Ah + r(h)$$, $$g(b+k) = g(b) + Bk + s(k)$$이고 $$r, s$$는 각각 $$\lVert h\rVert, \lVert k\rVert$$에 비해 무시할 만하다. $$k = Ah + r(h)$$를 대입하면

$$g(f(a+h)) = g(b) + B(Ah + r(h)) + s(k) = g(b) + BA\,h + \bigl(B\,r(h) + s(k)\bigr)$$

이고, 괄호 안의 오차가 $$\lVert h\rVert$$에 비해 $$0$$으로 감을 확인하면 $$D(g\circ f)(a) = BA$$이다.

</details>

## 연속미분가능성

편미분의 존재만으로는 미분가능성이 보장되지 않지만, 편미분이 연속이면 충분하다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $$f$$의 모든 편미분이 $$a$$ 근방에서 존재하고 $$a$$에서 연속이면 ($$f$$가 $$C^1$$이면), $$f$$는 $$a$$에서 미분가능하다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

한 좌표씩 변화시키며 각 단계에 한 변수 평균값 정리 ([§평균값 정리와 테일러 정리, ⁋정리 3](/ko/math/analysis/mean_value_theorem#thm3))를 적용하면 $$f(a+h) - f(a) = \sum_j \dfrac{\partial f}{\partial x_j}(\xi_j) h_j$$로 쓰이고, 편미분의 연속성으로 각 $$\dfrac{\partial f}{\partial x_j}(\xi_j)$$가 $$\dfrac{\partial f}{\partial x_j}(a)$$에 가까우므로 오차가 $$o(\lVert h\rVert)$$임이 따른다.

</details>

미분을 선형사상으로 보는 이 관점은 미분이 가역일 때 함수 자신이 국소적으로 가역이라는 강력한 결론으로 이어진다. 이것이 다음 글 [§역함수 정리와 음함수 정리](/ko/math/analysis/inverse_function_theorem)의 주제이다.
