---
title: "정적분"
description: "정적분을 분할 위의 리만 합의 극한으로 정의하고, 연속함수가 적분가능함을 받아들인 뒤 선형성·구간가법성·단조성 등 기본 성질을 정리한다. 넓이로서의 기하학적 의미를 함께 본다."
excerpt: "분할과 리만 합, 정적분의 정의, 적분의 성질"

categories: [Math / Calculus]
permalink: /ko/math/calculus/definite_integral
sidebar: 
    nav: "calculus-ko"

header:
    overlay_image: /assets/images/Math/Calculus/Definite_Integral.png
    overlay_filter: 0.5

date: 2026-06-02
last_modified_at: 2026-06-02
weight: 9

published: false
---

[§부정적분](/ko/math/calculus/antiderivatives)은 미분의 역연산이었다. 정적분은 그와 전혀 다른 동기 — 곡선 아래의 넓이, 누적된 양 — 에서 출발하지만, 놀랍게도 다음 글의 미적분의 기본정리를 통해 둘이 하나로 묶인다. 이 글에서는 먼저 정적분을 넓이의 근사라는 직관에 충실하게 정의한다.

## 분할과 리만 합

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 닫힌구간 $$[a, b]$$의 *분할<sub>partition</sub>*은 유한개의 점 $$a = x_0 < x_1 < \cdots < x_n = b$$이다. 각 부분구간 $$[x_{i-1}, x_i]$$의 길이를 $$\Delta x_i = x_i - x_{i-1}$$, 가장 긴 부분구간의 길이를 분할의 *너비<sub>mesh</sub>* $$\lVert P\rVert = \max_i \Delta x_i$$라 한다. 각 부분구간에서 표본점 $$c_i \in [x_{i-1}, x_i]$$을 택했을 때

$$S(P, f) = \sum_{i=1}^{n} f(c_i)\,\Delta x_i$$

를 함수 $$f$$의 *리만 합<sub>Riemann sum</sub>*이라 한다.

</div>

리만 합은 곡선 아래 영역을 폭이 $$\Delta x_i$$인 직사각형들로 근사한 넓이이다. 분할을 한없이 잘게 하면 이 근사가 한 값으로 수렴하기를 기대한다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 어떤 실수 $$I$$가 존재하여, 임의의 $$\varepsilon > 0$$에 대해 $$\delta > 0$$이 있어 $$\lVert P\rVert < \delta$$인 모든 분할과 표본점의 선택에 대해 $$\lvert S(P, f) - I\rvert < \varepsilon$$이 성립하면, $$f$$가 $$[a,b]$$에서 *적분가능<sub>integrable</sub>*하다고 하고 $$I$$를 *정적분*이라 하여

$$\int_a^b f(x)\,dx = I$$

로 적는다.

</div>

모든 함수가 적분가능하지는 않지만, 우리가 다루는 함수 대부분은 적분가능하다.

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3**</ins> $$[a, b]$$에서 연속인 함수는 적분가능하다.

</div>

이 정리의 증명은 연속함수가 닫힌구간에서 균등연속이라는 사실에 기대며, 그 엄밀한 논증은 실수의 완비성을 본격적으로 사용하는 해석학 [\[해석학\] §Riemann 적분](/ko/math/analysis/riemann_integral)에서 다룬다. 여기서는 이를 도구로 받아들인다.

## 정적분의 성질

리만 합이 합과 극한으로 정의되므로, 정적분은 다음 성질들을 물려받는다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $$f, g$$가 $$[a,b]$$에서 적분가능하면 다음이 성립한다.

1. (선형성) 상수 $$\alpha, \beta$$에 대해 $$\displaystyle\int_a^b (\alpha f + \beta g) = \alpha\int_a^b f + \beta\int_a^b g$$.
2. (구간가법성) $$a < c < b$$에 대해 $$\displaystyle\int_a^b f = \int_a^c f + \int_c^b f$$.
3. (단조성) 모든 $$x$$에서 $$f(x) \leq g(x)$$이면 $$\displaystyle\int_a^b f \leq \int_a^b g$$.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

세 성질 모두 리만 합 수준에서 성립하고 극한으로 보존된다. 선형성은 $$S(P, \alpha f + \beta g) = \alpha S(P, f) + \beta S(P, g)$$에서, 단조성은 $$f(c_i) \leq g(c_i)$$이면 $$S(P, f) \leq S(P, g)$$에서 따른다. 구간가법성은 $$c$$를 분점으로 포함하는 분할들만 생각하면 두 구간의 리만 합으로 갈라짐에서 얻는다.

</details>

관례적으로 $$\int_a^a f = 0$$, 그리고 $$\int_b^a f = -\int_a^b f$$로 두면 구간가법성은 $$a, b, c$$의 대소에 무관하게 성립한다. 단조성으로부터 $$m \leq f \leq M$$이면 $$m(b-a) \leq \int_a^b f \leq M(b-a)$$라는 유용한 평가도 따른다.

이렇게 정의한 정적분은 원리적으로는 리만 합의 극한을 직접 계산해야 하지만, 다음 글 [§미적분의 기본정리](/ko/math/calculus/fundamental_theorem_of_calculus)는 이 계산을 부정적분, 즉 미분의 역연산으로 환원하여 정적분과 부정적분을 하나로 잇는다.
