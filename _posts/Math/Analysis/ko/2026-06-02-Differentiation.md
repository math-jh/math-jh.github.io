---
title: "미분"
description: "미분가능성을 Carathéodory의 연속인자 형태로 정식화하여, 미분이 연속을 함의함과 연쇄법칙을 깔끔하게 증명한다. 미적분학에서 다룬 미분을 실수의 완비성 위에서 엄밀하게 재정초한다."
excerpt: "Carathéodory 미분, 미분가능성과 연속, 연쇄법칙"

categories: [Math / Analysis]
permalink: /ko/math/analysis/differentiation
sidebar: 
    nav: "analysis-ko"

header:
    overlay_image: /assets/images/Math/Analysis/Differentiation.png
    overlay_filter: 0.5

date: 2026-06-02
last_modified_at: 2026-06-02
weight: 12

published: false
---

[\[미적분학\] §미분과 도함수](/ko/math/calculus/derivatives)에서 미분을 차분몫의 극한으로 정의하였다. 이제 극한과 연속의 엄밀한 이론을 갖추었으므로, 미분을 다시 정초하되 차분몫의 분모가 사라지는 번거로움을 피하는 Carathéodory의 동치 형태를 채택한다.

## Carathéodory 미분

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1**</ins> 구간 $$I$$에서 정의된 $$f$$가 $$a \in I$$에서 미분가능한 것은, $$a$$에서 연속인 함수 $$\varphi : I \to \mathbb{R}$$가 존재하여 모든 $$x \in I$$에 대해

$$f(x) - f(a) = \varphi(x)\,(x - a)$$

가 성립하는 것과 동치이다. 이때 $$\varphi(a) = f'(a)$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$f$$가 $$a$$에서 미분가능하면 $$\varphi(x) = \dfrac{f(x)-f(a)}{x-a}$$ ($$x \neq a$$), $$\varphi(a) = f'(a)$$로 두면 미분가능성의 정의가 곧 $$\varphi$$의 $$a$$에서의 연속이다. 거꾸로 그런 연속 $$\varphi$$가 있으면 $$x \neq a$$에서 $$\dfrac{f(x)-f(a)}{x-a} = \varphi(x) \to \varphi(a)$$이므로 $$f'(a) = \varphi(a)$$가 존재한다.

</details>

이 형태는 분모 $$x - a$$를 곱셈으로 옮겨 두어, 미분의 기본 정리들을 극한 조작 없이 함수의 연속성만으로 끌어낸다.

## 미분가능성과 연속

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> $$f$$가 $$a$$에서 미분가능하면 $$a$$에서 연속이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

명제 1의 $$\varphi$$를 쓰면 $$f(x) = f(a) + \varphi(x)(x-a)$$이다. 우변은 $$a$$에서 연속인 함수들의 곱과 합이므로 ([§함수의 극한과 연속](/ko/math/analysis/limits_and_continuity)), $$x \to a$$일 때 $$f(x) \to f(a) + \varphi(a)\cdot 0 = f(a)$$이다.

</details>

## 연쇄법칙

Carathéodory 형태의 진가는 연쇄법칙의 증명에서 드러난다.

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3 (연쇄법칙)**</ins> $$f$$가 $$a$$에서, $$g$$가 $$b = f(a)$$에서 미분가능하면 $$g \circ f$$가 $$a$$에서 미분가능하고 $$(g\circ f)'(a) = g'(f(a))f'(a)$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

명제 1로 $$a$$에서 연속인 $$\varphi$$와 $$b$$에서 연속인 $$\psi$$가 있어 $$f(x) - f(a) = \varphi(x)(x-a)$$, $$g(y) - g(b) = \psi(y)(y - b)$$이다. $$y = f(x)$$를 대입하면

$$g(f(x)) - g(f(a)) = \psi(f(x))\,\bigl(f(x) - f(a)\bigr) = \psi(f(x))\,\varphi(x)\,(x - a)$$

이다. $$f$$가 $$a$$에서 연속이고 $$\psi$$가 $$b = f(a)$$에서 연속이므로 $$x \mapsto \psi(f(x))\varphi(x)$$는 $$a$$에서 연속이고, 명제 1에 의해 $$g\circ f$$가 $$a$$에서 미분가능하며 그 미분계수는 $$\psi(f(a))\varphi(a) = g'(b)f'(a)$$이다.

</details>

차분몫을 직접 다룰 때 생기던 "$$f(x) - f(a) = 0$$일 때 0으로 나누는" 문제가 이 증명에는 전혀 나타나지 않는다. 같은 방식으로 합·곱·몫의 미분법도 엄밀하게 재현된다 ([\[미적분학\] §미분법](/ko/math/calculus/differentiation_rules)).

이렇게 엄밀한 토대 위에서, 미분이 함수의 거동을 통제하는 핵심 정리 — 평균값 정리와 그 고계 일반화인 테일러 정리 — 를 다음 글 [§평균값 정리와 테일러 정리](/ko/math/analysis/mean_value_theorem)에서 다룬다.
