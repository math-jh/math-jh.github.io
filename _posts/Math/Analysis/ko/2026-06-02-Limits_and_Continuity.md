---
title: "함수의 극한과 연속"
description: "거리공간 사이의 함수의 극한과 연속을 ε-δ로 정의하고, 점열을 통한 특징화와 열린집합의 역상을 통한 위상적 특징화를 증명한다. 이로써 연속성을 거리·점열·위상의 세 관점에서 통합한다."
excerpt: "함수의 극한과 연속, 점열 특징화, 위상적 특징화"

categories: [Math / Analysis]
permalink: /ko/math/analysis/limits_and_continuity
sidebar: 
    nav: "analysis-ko"

header:
    overlay_image: /assets/images/Math/Analysis/Limits_and_Continuity.png
    overlay_filter: 0.5

date: 2026-06-02
last_modified_at: 2026-06-02
weight: 8

published: false
---

[\[미적분학\] §연속함수](/ko/math/calculus/continuity)에서 실함수의 연속을 다루었지만, [§거리공간](/ko/math/analysis/metric_spaces)과 [§열린집합과 닫힌집합](/ko/math/analysis/open_and_closed_sets)을 갖춘 지금은 연속을 훨씬 넓은 무대 위에서, 그리고 세 가지 동치인 관점에서 이해할 수 있다.

## 함수의 극한과 연속

$$(X, d_X)$$와 $$(Y, d_Y)$$를 거리공간이라 하자.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 함수 $$f : X \to Y$$가 점 $$a \in X$$에서 *연속<sub>continuous</sub>*이라는 것은, 임의의 $$\varepsilon > 0$$에 대하여 $$\delta > 0$$이 존재하여

$$d_X(x, a) < \delta \;\Longrightarrow\; d_Y(f(x), f(a)) < \varepsilon$$

이 성립하는 것이다. $$f$$가 $$X$$의 모든 점에서 연속이면 $$f$$를 *연속함수*라 한다.

</div>

거리 $$\lvert x - a\rvert$$를 $$d_X(x, a)$$로 바꾸었을 뿐, [\[미적분학\] §함수와 극한](/ko/math/calculus/functions_and_limits)의 정의와 형태가 같다. 같은 방식으로 $$x \to a$$일 때 $$f(x) \to L$$인 함수의 극한도 정의된다.

## 세 가지 특징화

연속은 점열의 언어로 다시 표현된다. 이는 연속함수를 다룰 때 가장 자주 쓰이는 형태이다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2 (점열 특징화)**</ins> $$f : X \to Y$$가 $$a$$에서 연속인 것은, $$a$$로 수렴하는 모든 점열 $$(x_n)$$에 대해 $$f(x_n) \to f(a)$$인 것과 동치이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$f$$가 $$a$$에서 연속이고 $$x_n \to a$$라 하자. 임의의 $$\varepsilon > 0$$에 대해 정의 1의 $$\delta$$를 잡고, $$x_n \to a$$이므로 큰 $$n$$에서 $$d_X(x_n, a) < \delta$$, 따라서 $$d_Y(f(x_n), f(a)) < \varepsilon$$이다. 즉 $$f(x_n) \to f(a)$$이다.

역으로 $$f$$가 $$a$$에서 연속이 아니라 하자. 그러면 어떤 $$\varepsilon > 0$$에 대해 모든 $$\delta$$가 실패하므로, $$\delta = 1/n$$에 대해 $$d_X(x_n, a) < 1/n$$이면서 $$d_Y(f(x_n), f(a)) \geq \varepsilon$$인 $$x_n$$이 있다. 이 $$(x_n)$$은 $$a$$로 수렴하지만 $$f(x_n) \not\to f(a)$$이므로 대우가 성립한다.

</details>

연속은 또한 열린집합의 역상이라는 순수히 위상적인 조건과 동치이다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3 (위상적 특징화)**</ins> $$f : X \to Y$$가 ($$X$$ 전체에서) 연속인 것은, $$Y$$의 모든 열린집합 $$V$$에 대해 그 역상 $$f^{-1}(V)$$가 $$X$$에서 열린집합인 것과 동치이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$f$$가 연속이고 $$V \subseteq Y$$가 열려 있다 하자. $$a \in f^{-1}(V)$$이면 $$f(a) \in V$$이고 $$V$$가 열려 있어 $$B(f(a), \varepsilon) \subseteq V$$인 $$\varepsilon$$이 있다. 연속성으로 이 $$\varepsilon$$에 대응하는 $$\delta$$를 잡으면 $$f(B(a, \delta)) \subseteq B(f(a), \varepsilon) \subseteq V$$, 즉 $$B(a, \delta) \subseteq f^{-1}(V)$$이므로 $$f^{-1}(V)$$가 열려 있다.

역으로 열린집합의 역상이 항상 열려 있다 하자. $$a \in X$$와 $$\varepsilon > 0$$에 대해 $$V = B(f(a), \varepsilon)$$은 열려 있으므로 $$f^{-1}(V)$$도 열려 있고 $$a$$를 포함하므로 $$B(a, \delta) \subseteq f^{-1}(V)$$인 $$\delta$$가 있다. 이는 정의 1의 연속 조건이다.

</details>

명제 3은 거리를 전혀 언급하지 않으므로, 연속의 개념이 본질적으로 위상적임을 드러낸다. 이것이 [\[위상수학\] §연속함수](/ko/math/topology/continuous_functions)에서 일반 위상공간 사이의 연속을 열린집합의 역상으로 *정의*하는 근거이다.

세 특징화 — $$\varepsilon$$-$$\delta$$, 점열, 열린집합 — 는 상황에 따라 골라 쓰인다. 다음 글들에서 연속함수가 [§컴팩트성](/ko/math/analysis/compactness)과 [§연결성과 중간값 정리](/ko/math/analysis/connectedness)를 어떻게 보존하는지, 그리고 그로부터 [§연속함수의 성질](/ko/math/analysis/continuous_functions)에서 최대·최소 정리와 중간값 정리가 어떻게 따라 나오는지를 본다.
