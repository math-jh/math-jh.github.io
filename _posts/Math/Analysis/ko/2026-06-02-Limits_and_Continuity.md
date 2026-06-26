---
title: "함수의 극한과 연속"
description: "거리공간 사이의 함수의 극한과 연속을 ε-δ로 정의하고, 점열을 통한 특징화와 열린집합의 역상을 통한 위상적 특징화를 증명한다. 이로써 연속성을 거리·점열·위상의 세 관점에서 통합한다."
excerpt: "함수의 극한과 연속, 점열 특징화, 위상적 특징화"

categories: [Math / Analysis]
permalink: /ko/math/analysis/limits_and_continuity
sidebar: 
    nav: "analysis-ko"

date: 2026-06-02
weight: 8

drift_needed: true

published: false
---

[\[미적분학\] §연속함수](/ko/math/calculus/continuity)에서 실함수의 연속을 다루었지만, [§거리공간](/ko/math/analysis/metric_spaces)과 [§열린집합과 닫힌집합](/ko/math/analysis/open_and_closed_sets)을 갖춘 지금은 연속을 훨씬 넓은 무대 위에서, 그리고 세 가지 동치인 관점에서 이해할 수 있다.

## 함수의 극한과 연속

$$(X, d_X)$$와 $$(Y, d_Y)$$를 거리공간이라 하자.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 함수 $$f : X \to Y$$가 점 $$a \in X$$에서 *연속<sub>continuous</sub>*이라는 것은, 임의의 $$\varepsilon > 0$$에 대하여 $$\delta > 0$$이 존재하여

$$d_X(x, a) < \delta  \Longrightarrow  d_Y(f(x), f(a)) < \varepsilon$$

이 성립하는 것이다. $$f$$가 $$X$$의 모든 점에서 연속이면 $$f$$를 *연속함수*라 한다.

</div>

거리 $$\lvert x - a\rvert$$를 $$d_X(x, a)$$로 바꾸었을 뿐, [\[미적분학\] §함수의 극한](/ko/math/calculus/functions_and_limits)의 정의와 형태가 같다. 같은 방식으로 $$x \to a$$일 때 $$f(x) \to L$$인 함수의 극한도 정의된다.

## 세 가지 특징화

연속은 점열의 언어로 다시 표현된다. 이는 연속함수를 다룰 때 가장 자주 쓰이는 형태이다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2 (점열 특징화)**</ins> $$f : X \to Y$$가 $$a$$에서 연속인 것은, $$a$$로 수렴하는 모든 점열 $$(x_n)$$에 대해 $$f(x_n) \to f(a)$$인 것과 동치이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$f$$가 $$a$$에서 연속이고 $$x_n \to a$$라 하자. 임의의 $$\varepsilon > 0$$에 대해 [정의 1](#def1)의 $$\delta$$를 잡고, $$x_n \to a$$이므로 큰 $$n$$에서 $$d_X(x_n, a) < \delta$$, 따라서 $$d_Y(f(x_n), f(a)) < \varepsilon$$이다. 즉 $$f(x_n) \to f(a)$$이다.

역으로 $$f$$가 $$a$$에서 연속이 아니라 하자. 그러면 어떤 $$\varepsilon > 0$$에 대해 모든 $$\delta$$가 실패하므로, $$\delta = 1/n$$에 대해 $$d_X(x_n, a) < 1/n$$이면서 $$d_Y(f(x_n), f(a)) \geq \varepsilon$$인 $$x_n$$이 있다. 이 $$(x_n)$$은 $$a$$로 수렴하지만 $$f(x_n) \not\to f(a)$$이므로 대우가 성립한다.

</details>

연속은 또한 열린집합의 역상이라는 순수히 위상적인 조건과 동치이다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3 (위상적 특징화)**</ins> $$f : X \to Y$$가 ($$X$$ 전체에서) 연속인 것은, $$Y$$의 모든 열린집합 $$V$$에 대해 그 역상 $$f^{-1}(V)$$가 $$X$$에서 열린집합인 것과 동치이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$f$$가 연속이고 $$V \subseteq Y$$가 열려 있다 하자. $$a \in f^{-1}(V)$$이면 $$f(a) \in V$$이고 $$V$$가 열려 있어 $$B(f(a), \varepsilon) \subseteq V$$인 $$\varepsilon$$이 있다. 연속성으로 이 $$\varepsilon$$에 대응하는 $$\delta$$를 잡으면 $$f(B(a, \delta)) \subseteq B(f(a), \varepsilon) \subseteq V$$, 즉 $$B(a, \delta) \subseteq f^{-1}(V)$$이므로 $$f^{-1}(V)$$가 열려 있다.

역으로 열린집합의 역상이 항상 열려 있다 하자. $$a \in X$$와 $$\varepsilon > 0$$에 대해 $$V = B(f(a), \varepsilon)$$은 열려 있으므로 $$f^{-1}(V)$$도 열려 있고 $$a$$를 포함하므로 $$B(a, \delta) \subseteq f^{-1}(V)$$인 $$\delta$$가 있다. 이는 [정의 1](#def1)의 연속 조건이다.

</details>

[명제 3](#prop3)은 거리를 전혀 언급하지 않으므로, 연속의 개념이 본질적으로 위상적임을 드러낸다. 이것이 [\[위상수학\] §연속함수](/ko/math/topology/continuous_functions)에서 일반 위상공간 사이의 연속을 열린집합의 역상으로 *정의*하는 근거이다.

세 특징화 — $$\varepsilon$$-$$\delta$$, 점열, 열린집합 — 는 상황에 따라 골라 쓰인다. 점별 평가가 자연스러운 곳에서는 $$\varepsilon$$-$$\delta$$를, 수렴하는 점열이 주어진 곳에서는 [명제 2](#prop2)를, 그리고 공간 전체의 위상적 성질을 다룰 때는 [명제 3](#prop3)을 택하는 것이 보통이다. 아래에서 이 세 관점을 구체적인 함수에 적용해 보고, 연속함수가 합·곱·합성에 대해 닫혀 있음을 확인한다.

## 함수의 극한

[정의 1](#def1)은 점 $$a$$에서의 *함숫값* $$f(a)$$와 그 근방에서의 거동을 한꺼번에 비교한다. 그러나 많은 경우 우리는 $$f$$가 $$a$$에서 정의되어 있는지와 무관하게 $$x$$를 $$a$$에 가까이 보낼 때 $$f(x)$$가 어디로 다가가는지만을 묻는다. 이를 위해 함수의 극한을 따로 정의한다. 여기서 $$a$$는 정의역 $$X$$의 *집적점<sub>limit point</sub>*, 즉 임의의 $$\delta > 0$$에 대해 $$0 < d_X(x, a) < \delta$$인 $$x \in X$$가 존재하는 점이라 가정한다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> 함수 $$f : X \to Y$$에 대하여 $$x \to a$$일 때 $$f(x)$$의 *극한<sub>limit</sub>*이 $$L \in Y$$이라는 것은, 임의의 $$\varepsilon > 0$$에 대하여 $$\delta > 0$$이 존재하여

$$0 < d_X(x, a) < \delta  \Longrightarrow  d_Y(f(x), L) < \varepsilon$$

이 성립하는 것이며, 이때 $$\lim_{x \to a} f(x) = L$$로 적는다.

</div>

[정의 1](#def1)과의 차이는 두 가지뿐이다. 첫째, 비교 대상이 $$f(a)$$가 아니라 임의의 후보 값 $$L$$이다. 둘째, $$x = a$$ 자체는 $$0 < d_X(x, a)$$라는 조건으로 배제된다. 이로부터 $$f$$가 $$a$$에서 연속인 것은 $$a$$가 집적점일 때 $$\lim_{x \to a} f(x) = f(a)$$인 것과 동치임이 즉시 따른다. 즉 연속은 극한이 존재하고 그 값이 함숫값과 같다는 조건의 다른 이름이다.

## 연속함수의 연산

연속함수는 가장 기본적인 연산들에 대해 닫혀 있다. 먼저 합성을 보자.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5 (합성의 연속)**</ins> $$f : X \to Y$$가 $$a$$에서 연속이고 $$g : Y \to Z$$가 $$f(a)$$에서 연속이면, 합성 $$g \circ f : X \to Z$$는 $$a$$에서 연속이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $$\varepsilon > 0$$이 주어졌다고 하자. $$g$$가 $$b := f(a)$$에서 연속이므로 $$\eta > 0$$이 존재하여

$$d_Y(y, b) < \eta  \Longrightarrow  d_Z(g(y), g(b)) < \varepsilon$$

이 성립한다. 이제 이 $$\eta$$를 $$f$$의 연속에 대한 도전값으로 삼으면, $$f$$가 $$a$$에서 연속이므로 $$\delta > 0$$이 존재하여

$$d_X(x, a) < \delta  \Longrightarrow  d_Y(f(x), b) < \eta$$

이다. 두 함의를 이어 붙이면 $$d_X(x, a) < \delta$$일 때

$$d_Z\bigl(g(f(x)), g(f(a))\bigr) < \varepsilon$$

이므로 $$g \circ f$$는 $$a$$에서 연속이다.

</details>

[명제 2](#prop2)의 [명제 2](#prop2)를 쓰면 같은 사실이 한층 짧게 나온다. $$x_n \to a$$이면 $$f$$의 연속으로 $$f(x_n) \to f(a)$$이고, 다시 $$g$$의 연속으로 $$g(f(x_n)) \to g(f(a))$$이므로 $$(g \circ f)(x_n) \to (g \circ f)(a)$$이다. 두 증명은 본질적으로 같은 내용을 $$\varepsilon$$-$$\delta$$의 언어와 점열의 언어로 각각 옮긴 것이다.

치역이 $$\mathbb{R}$$인 경우, 연속함수의 합·곱·몫도 연속이다. 이는 실수열의 극한이 대수 연산과 교환한다는 사실 ([§수열의 수렴, ⁋정리 4](/ko/math/analysis/convergence_of_sequences#thm4))을 [명제 2](#prop2)를 통해 함수에 옮긴 것이다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6 (합과 곱의 연속)**</ins> $$f, g : X \to \mathbb{R}$$가 $$a$$에서 연속이면 $$f + g$$와 $$fg$$도 $$a$$에서 연속이며, $$g(a) \neq 0$$이면 $$f/g$$도 $$a$$에서 연속이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$a$$로 수렴하는 임의의 점열 $$(x_n)$$을 잡자. [명제 2](#prop2)에 의해 $$f(x_n) \to f(a)$$이고 $$g(x_n) \to g(a)$$이다. 실수열의 [§수열의 수렴, ⁋정리 4](/ko/math/analysis/convergence_of_sequences#thm4)에 의해

$$\begin{aligned}
(f + g)(x_n) &= f(x_n) + g(x_n) \to f(a) + g(a) = (f + g)(a), \\
(fg)(x_n) &= f(x_n)  g(x_n) \to f(a)  g(a) = (fg)(a)
\end{aligned}$$

이다. $$g(a) \neq 0$$이면 같은 정리의 몫에 관한 부분으로

$$\frac{f}{g}(x_n) = \frac{f(x_n)}{g(x_n)} \to \frac{f(a)}{g(a)} = \frac{f}{g}(a)$$

이다. 세 경우 모두 $$a$$로 가는 임의의 점열에서 함숫값이 올바른 극한으로 가므로, 다시 [명제 2](#prop2)에 의해 $$f + g$$, $$fg$$, $$f/g$$가 $$a$$에서 연속이다.

</details>

상수함수와 항등함수 $$x \mapsto x$$가 연속임은 정의에서 곧바로 나오므로, [명제 6](#prop6)을 반복 적용하면 모든 다항식 $$p(x) = c_0 + c_1 x + \cdots + c_n x^n$$이 $$\mathbb{R}$$ 전체에서 연속이고, 유리함수 $$p/q$$는 $$q$$가 $$0$$이 되지 않는 모든 점에서 연속임을 얻는다.

## 예시와 계산

위상적 특징화([명제 3](#prop3))가 가장 잘 드러나는 함수는 거리 그 자체이다.

<div class="example" markdown="1">

<ins id="ex7">**예시 7 (거리함수의 연속)**</ins> 거리공간 $$(X, d)$$에서 한 점 $$p$$를 고정하고 $$f(x) = d(x, p)$$로 두자. 삼각부등식 ([§거리공간, ⁋정의 1](/ko/math/analysis/metric_spaces#def1))에서 임의의 $$x, y$$에 대해

$$d(x, p) \leq d(x, y) + d(y, p), \qquad d(y, p) \leq d(y, x) + d(x, p)$$

이므로, 두 부등식을 합치면

$$\lvert f(x) - f(y)\rvert = \lvert d(x, p) - d(y, p)\rvert \leq d(x, y)$$

를 얻는다. 따라서 임의의 $$\varepsilon > 0$$에 대해 $$\delta = \varepsilon$$으로 두면 $$d(x, y) < \delta$$일 때 $$\lvert f(x) - f(y)\rvert < \varepsilon$$이므로 $$f$$는 연속이다. 이렇게 $$\delta$$를 점에 무관하게 잡을 수 있는 함수를 *균등연속<sub>uniformly continuous</sub>*이라 하며, $$d(x, y)$$가 그대로 상계가 되는 특수한 경우를 *Lipschitz 함수*라 한다.

</div>

연속이 점열을 보존한다는 [명제 2](#prop2)는 극한을 계산하는 실용적 도구이기도 하다. $$g$$가 연속이고 $$x_n \to a$$이면

$$\lim_{n \to \infty} g(x_n) = g \left(\lim_{n \to \infty} x_n\right) = g(a)$$

이므로, 연속함수에 한해서는 극한과 함수를 자유롭게 교환할 수 있다. 연속성이 없으면 이러한 교환은 일반적으로 성립하지 않는다.

마지막으로, 연속이 깨지는 전형적인 예를 점열 특징화로 진단해 보자.

<div class="example" markdown="1">

<ins id="ex8">**예시 8 (불연속의 진단)**</ins> $$f : \mathbb{R} \to \mathbb{R}$$를 $$x > 0$$이면 $$f(x) = 1$$, $$x \leq 0$$이면 $$f(x) = 0$$인 계단함수라 하자. $$a = 0$$에서의 연속을 점열로 검사한다. 양의 점열 $$x_n = 1/n$$은 $$0$$으로 수렴하지만

$$f(x_n) = 1 \to 1 \neq 0 = f(0)$$

이므로, [명제 2](#prop2)에 의해 $$f$$는 $$0$$에서 연속이 아니다. 같은 사실을 [명제 3](#prop3)으로도 볼 수 있다. $$f(0) = 0$$을 품는 열린집합 $$V = (-1/2,  1/2)$$의 역상은

$$f^{-1}(V) = \{x : f(x) \in V\} = (-\infty, 0]$$

이고, 이는 점 $$0$$을 내부점으로 갖지 못하므로 열린집합이 아니다. 즉 어떤 열린집합의 역상이 열려 있지 않으므로 $$f$$는 ($$\mathbb{R}$$ 전체에서) 연속이 아니다.

</div>
