---
title: "미적분의 기본정리"
description: "Riemann 적분 위에서 미적분의 기본정리를 엄밀하게 증명한다. 가변상한 적분이 연속이며 피적분함수가 연속인 점에서 미분가능함을 보이고, 원시함수를 통한 정적분의 평가정리를 확립한다."
excerpt: "가변상한 적분의 미분, 평가정리, 미분과 적분의 역관계"

categories: [Math / Analysis]
permalink: /ko/math/analysis/fundamental_theorem_of_calculus
sidebar: 
    nav: "analysis-ko"

header:
    overlay_image: /assets/images/Math/Analysis/Fundamental_Theorem_of_Calculus.png
    overlay_filter: 0.5

date: 2026-07-17
last_modified_at: 2026-07-17

weight: 15

published: false
---

[§Riemann 적분](/ko/math/analysis/riemann_integral)에서 적분을 엄밀하게 정초하고, [§미분](/ko/math/analysis/differentiation)에서 미분을 다시 세웠다. 미적분의 기본정리는 이 둘이 서로의 역연산임을 밝히며, [\[미적분학\] §미적분의 기본정리](/ko/math/calculus/fundamental_theorem_of_calculus)에서 다룬 내용을 이제 완비성 위에서 증명한다.

## 가변상한 적분

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1**</ins> $$f$$가 $$[a,b]$$에서 Riemann 적분가능하면 $$F(x) = \displaystyle\int_a^x f$$는 $$[a,b]$$에서 (립시츠) 연속이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$f$$는 유계이므로 $$\lvert f\rvert \leq M$$인 $$M$$이 있다. $$x < y$$에 대해 구간가법성과 단조성으로 $$\lvert F(y) - F(x)\rvert = \left\lvert\int_x^y f\right\rvert \leq M(y - x)$$이므로 $$F$$는 립시츠 연속, 따라서 연속이다.

</details>

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2 (제1형)**</ins> 위의 $$F$$에 대하여, $$f$$가 점 $$x_0$$에서 연속이면 $$F$$는 $$x_0$$에서 미분가능하고 $$F'(x_0) = f(x_0)$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\dfrac{F(x_0 + h) - F(x_0)}{h} = \dfrac1h\int_{x_0}^{x_0 + h} f$$이다. $$f$$가 $$x_0$$에서 연속이므로, 임의의 $$\varepsilon > 0$$에 대해 $$\lvert t - x_0\rvert < \delta$$이면 $$\lvert f(t) - f(x_0)\rvert < \varepsilon$$이다. $$0 < \lvert h\rvert < \delta$$이면

$$\left\lvert \frac1h\int_{x_0}^{x_0+h} f - f(x_0)\right\rvert = \left\lvert \frac1h\int_{x_0}^{x_0+h}\bigl(f(t) - f(x_0)\bigr)dt\right\rvert \leq \varepsilon$$

이므로 차분몫이 $$f(x_0)$$로 수렴한다.

</details>

특히 $$f$$가 $$[a,b]$$에서 연속이면 $$F$$는 $$f$$의 원시함수이다. 즉 연속함수는 언제나 원시함수를 가진다.

## 평가정리

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3 (제2형)**</ins> $$f$$가 $$[a,b]$$에서 적분가능하고 $$G$$가 $$[a,b]$$에서 연속이며 $$(a,b)$$에서 $$G' = f$$를 만족하는 함수이면

$$\int_a^b f = G(b) - G(a)$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

임의의 분할 $$P : a = x_0 < \cdots < x_n = b$$에 대해, 각 $$[x_{i-1}, x_i]$$에서 평균값 정리 ([§평균값 정리와 테일러 정리, ⁋정리 3](/ko/math/analysis/mean_value_theorem#thm3))를 $$G$$에 적용하면 $$G(x_i) - G(x_{i-1}) = f(t_i)\Delta x_i$$인 $$t_i$$가 있다. 합하면 $$G(b) - G(a) = \sum_i f(t_i)\Delta x_i$$로, 이는 $$f$$의 한 리만 합이며 $$L(P, f) \leq G(b) - G(a) \leq U(P, f)$$를 만족한다. $$f$$가 적분가능하므로 분할을 잘게 하면 양 끝이 $$\int_a^b f$$로 수렴하고, 따라서 $$\int_a^b f = G(b) - G(a)$$이다.

</details>

평가정리는 [\[미적분학\] §적분법](/ko/math/calculus/integration_techniques)의 치환·부분적분이 의존하던 토대이며, 이제 그 가정들이 모두 엄밀하게 증명되었다. 한 함수의 적분을 넘어 함수들의 열의 극한과 적분·미분이 어떻게 교환되는지는 다음 글 [§함수열과 점별수렴](/ko/math/analysis/sequences_of_functions)에서 다룬다.
