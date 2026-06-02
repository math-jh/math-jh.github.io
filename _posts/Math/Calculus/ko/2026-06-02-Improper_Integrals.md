---
title: "이상적분"
description: "적분 구간이 무한하거나 피적분함수가 발산하는 이상적분을 극한으로 정의하고, 수렴과 발산을 판정한다. 기준이 되는 p-적분과 비교판정을 다루고, 무한급수의 적분판정과의 연관을 본다."
excerpt: "무한구간 이상적분, 특이적분, 비교판정"

categories: [Math / Calculus]
permalink: /ko/math/calculus/improper_integrals
sidebar: 
    nav: "calculus-ko"

header:
    overlay_image: /assets/images/Math/Calculus/Improper_Integrals.png
    overlay_filter: 0.5

date: 2026-06-02
last_modified_at: 2026-06-02
weight: 12

published: false
---

[§정적분](/ko/math/calculus/definite_integral)은 유한한 구간에서 유계인 함수에 대해 정의되었다. 그러나 구간이 무한히 뻗거나 피적분함수가 한 점에서 무한히 커지는 경우에도 "넓이"를 논하고 싶을 때가 많다. 이를 극한을 통해 정의하는 것이 이상적분이다.

## 이상적분의 정의

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $$f$$가 모든 $$t > a$$에서 $$[a, t]$$에서 적분가능할 때, *무한구간 이상적분*을

$$\int_a^{\infty} f(x)\,dx = \lim_{t \to \infty}\int_a^t f(x)\,dx$$

으로 정의하고, 이 극한이 존재하면 이상적분이 *수렴*한다고 한다. $$\int_{-\infty}^b$$도 대칭적으로 정의하며, $$\int_{-\infty}^{\infty} f = \int_{-\infty}^c f + \int_c^{\infty} f$$로 둔다.

</div>

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> $$f$$가 $$b$$에서 발산하지만 모든 $$t < b$$에서 $$[a, t]$$에서 적분가능할 때, *특이적분*을

$$\int_a^{b} f(x)\,dx = \lim_{t \to b^-}\int_a^t f(x)\,dx$$

으로 정의한다.

</div>

## 기준 적분과 비교판정

수렴·발산의 경계를 보여 주는 기준 예가 거듭제곱함수의 적분이다.

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> $$\displaystyle\int_1^{\infty}\frac{dx}{x^p}$$는 $$p > 1$$일 때 수렴하고 $$p \leq 1$$일 때 발산한다. 실제로 $$p \neq 1$$이면 $$\int_1^t x^{-p}\,dx = \dfrac{t^{1-p} - 1}{1 - p}$$인데, $$t \to \infty$$일 때 $$t^{1-p}$$는 $$p > 1$$이면 $$0$$으로, $$p < 1$$이면 무한으로 간다. $$p = 1$$이면 $$\int_1^t \tfrac1x\,dx = \ln t \to \infty$$로 발산한다. 따라서 $$p > 1$$에서만 수렴하며, 그 값은 $$\dfrac{1}{p-1}$$이다.

</div>

피적분함수가 음이 아니면, 적분값이 단조증가하므로 급수에서와 같은 비교판정이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4 (비교판정)**</ins> $$x \geq a$$에서 $$0 \leq f(x) \leq g(x)$$라 하자. $$\int_a^\infty g$$가 수렴하면 $$\int_a^\infty f$$도 수렴하고, $$\int_a^\infty f$$가 발산하면 $$\int_a^\infty g$$도 발산한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$F(t) = \int_a^t f$$는 $$f \geq 0$$이므로 $$t$$에 대해 증가하고, 단조성 ([§정적분, ⁋명제 4](/ko/math/calculus/definite_integral#prop4))에 의해 $$F(t) \leq \int_a^t g \leq \int_a^\infty g$$로 위로 유계이다. 위로 유계인 증가함수는 $$t \to \infty$$에서 극한을 가지므로 $$\int_a^\infty f$$가 수렴한다. 둘째 주장은 대우이다.

</details>

예를 들어 $$\int_1^\infty e^{-x^2}\,dx$$는 $$x \geq 1$$에서 $$e^{-x^2} \leq e^{-x}$$이고 $$\int_1^\infty e^{-x}\,dx$$가 수렴하므로 수렴한다.

이상적분의 수렴 이론은 무한급수의 그것과 평행하다. 실제로 양의 감소함수 $$f$$에 대해 $$\sum_{n} f(n)$$과 $$\int_1^\infty f$$는 동시에 수렴하거나 발산하며 (적분판정), 이는 [\[해석학\] §무한급수](/ko/math/analysis/series)의 수렴 판정과 직접 이어진다. 함수를 무한히 더하거나 적분하는 이런 극한 과정 전반의 엄밀한 취급은 해석학에서 이루어진다.
