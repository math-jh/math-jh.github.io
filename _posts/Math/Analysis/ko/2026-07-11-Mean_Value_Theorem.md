---
title: "평균값 정리와 테일러 정리"
description: "엄밀하게 증명된 최대·최소 정리 위에서 페르마 정리·롤의 정리·평균값 정리를 다시 세우고, 도함수의 부호가 단조성을 결정함을 보인다. 라그랑주 나머지를 가진 테일러 정리를 코시 평균값 정리로 증명한다."
excerpt: "페르마·롤·평균값 정리, 단조성, 테일러 정리"

categories: [Math / Analysis]
permalink: /ko/math/analysis/mean_value_theorem
sidebar: 
    nav: "analysis-ko"

header:
    overlay_image: /assets/images/Math/Analysis/Mean_Value_Theorem.png
    overlay_filter: 0.5

date: 2026-07-11
last_modified_at: 2026-07-11

weight: 13

published: false
---

[§미분](/ko/math/analysis/differentiation)에서 미분을 엄밀하게 정초하고, [§연속함수의 성질](/ko/math/analysis/continuous_functions)에서 최대·최소 정리를 완비성으로부터 증명하였다. 이 둘을 결합하면 미적분학에서 도구로 받아들였던 평균값 정리와 테일러 정리를 빈틈없이 세울 수 있다.

## 페르마 정리와 롤의 정리

<div class="proposition" markdown="1">

<ins id="thm1">**정리 1 (페르마)**</ins> $$f$$가 내부의 점 $$c$$에서 극값을 가지고 $$c$$에서 미분가능하면 $$f'(c) = 0$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$c$$가 극댓값이면 $$c$$ 근방에서 $$\dfrac{f(x)-f(c)}{x-c}$$는 $$x > c$$에서 $$\leq 0$$, $$x < c$$에서 $$\geq 0$$이다. 미분가능성으로 양쪽 극한이 일치해야 하므로 $$f'(c) = 0$$이다.

</details>

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2 (롤)**</ins> $$f$$가 $$[a,b]$$에서 연속, $$(a,b)$$에서 미분가능하고 $$f(a) = f(b)$$이면 $$f'(c) = 0$$인 $$c \in (a,b)$$가 존재한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

최대·최소 정리 ([§연속함수의 성질, ⁋따름정리 2](/ko/math/analysis/continuous_functions#cor2))에 의해 $$f$$는 $$[a,b]$$에서 최댓값과 최솟값을 가진다. 둘 다 끝점에서만 일어나면 $$f(a) = f(b)$$이므로 $$f$$는 상수여서 모든 내부 점에서 $$f' = 0$$이다. 그렇지 않으면 극값이 내부 점 $$c$$에서 일어나고 페르마 정리에 의해 $$f'(c) = 0$$이다.

</details>

## 평균값 정리

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3 (평균값 정리)**</ins> $$f$$가 $$[a,b]$$에서 연속, $$(a,b)$$에서 미분가능하면 $$f'(c) = \dfrac{f(b)-f(a)}{b-a}$$인 $$c \in (a,b)$$가 존재한다. 더 일반적으로 $$f, g$$에 대해 $$\bigl(f(b)-f(a)\bigr)g'(c) = \bigl(g(b)-g(a)\bigr)f'(c)$$인 $$c$$가 존재한다 (코시 평균값 정리).

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

코시 형태만 보이면 충분하다 ($$g(x) = x$$로 두면 평균값 정리이다). 보조함수 $$h(x) = \bigl(f(b)-f(a)\bigr)g(x) - \bigl(g(b)-g(a)\bigr)f(x)$$는 $$h(a) = h(b)$$를 만족하므로, 롤의 정리에 의해 $$h'(c) = 0$$인 $$c$$가 있고 이것이 주장하는 등식이다.

</details>

평균값 정리의 가장 기본적인 귀결은 도함수가 함수의 단조성을 결정한다는 것이다.

<div class="proposition" markdown="1">

<ins id="cor4">**따름정리 4**</ins> $$f$$가 구간에서 미분가능할 때, 항상 $$f' = 0$$이면 $$f$$는 상수이고, $$f' > 0$$이면 순증가, $$f' < 0$$이면 순감소한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

두 점 $$x_1 < x_2$$에 평균값 정리를 적용하면 $$f(x_2) - f(x_1) = f'(c)(x_2 - x_1)$$이므로, 우변의 부호가 $$f'(c)$$로 결정된다.

</details>

## 테일러 정리

평균값 정리를 고계도함수로 끌어올린 것이 테일러 정리이다.

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5 (테일러 정리, 라그랑주 나머지)**</ins> $$f$$가 $$a$$를 포함하는 구간에서 $$n+1$$번 미분가능하면, 각 $$x$$에 대해 $$a$$와 $$x$$ 사이의 $$c$$가 존재하여

$$f(x) = \sum_{k=0}^{n}\frac{f^{(k)}(a)}{k!}(x-a)^k + \frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$x$$를 고정하고 $$g(t) = f(x) - \sum_{k=0}^n \dfrac{f^{(k)}(t)}{k!}(x-t)^k$$, $$h(t) = (x-t)^{n+1}$$로 두면 $$g'(t) = -\dfrac{f^{(n+1)}(t)}{n!}(x-t)^n$$로 망원합처럼 상쇄된다. $$a$$와 $$x$$ 사이에서 코시 평균값 정리 (정리 3)를 적용하면 $$\bigl(g(x)-g(a)\bigr)h'(c) = \bigl(h(x)-h(a)\bigr)g'(c)$$인 $$c$$가 있고, $$g(x) = h(x) = 0$$을 대입해 정리하면 나머지항 공식을 얻는다.

</details>

이 증명은 [\[미적분학\] §테일러 정리](/ko/math/calculus/taylor_theorem)에서와 같지만, 이제 그 토대인 최대·최소 정리와 미분의 성질이 모두 엄밀하게 증명되어 있다. 다음으로는 미분의 짝이 되는 적분을 엄밀하게 정초하는 [§Riemann 적분](/ko/math/analysis/riemann_integral)으로 나아간다.
