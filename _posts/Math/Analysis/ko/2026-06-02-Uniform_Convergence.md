---
title: "균등수렴"
description: "함수열의 균등수렴을 상한노름으로 정의하고, 균등극한이 연속성을 보존하며 극한과 적분이 교환됨을 증명한다. 함수항급수의 균등수렴을 보장하는 바이어슈트라스 M-판정법을 다룬다."
excerpt: "균등수렴, 연속성과 적분의 보존, 바이어슈트라스 M-판정"

categories: [Math / Analysis]
permalink: /ko/math/analysis/uniform_convergence
sidebar: 
    nav: "analysis-ko"

header:
    overlay_image: /assets/images/Math/Analysis/Uniform_Convergence.png
    overlay_filter: 0.5

date: 2026-06-02
last_modified_at: 2026-06-02
weight: 17

published: false
---

[§함수열과 점별수렴](/ko/math/analysis/sequences_of_functions)에서 점별수렴이 연속성과 적분을 보존하지 못함을 보았다. 그 병폐의 원인은 수렴 속도가 점마다 다른 데 있었다. 이를 막아 수렴이 정의역 전체에서 고르게 일어나도록 요구하는 것이 균등수렴이다.

## 균등수렴

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 함수열 $$(f_n)$$이 $$f$$로 *균등수렴<sub>uniform convergence</sub>*한다는 것은, 임의의 $$\varepsilon > 0$$에 대하여 ($$x$$에 무관한) $$N$$이 존재하여 모든 $$n \geq N$$과 모든 $$x$$에 대해

$$\lvert f_n(x) - f(x)\rvert < \varepsilon$$

이 성립하는 것이다. 상한노름 $$\lVert g\rVert_\infty = \sup_x \lvert g(x)\rvert$$을 쓰면, 균등수렴은 $$\lVert f_n - f\rVert_\infty \to 0$$과 같다.

</div>

점별수렴과의 결정적 차이는 $$N$$이 점에 무관하다는 것이다. $$[0,1]$$에서 $$f_n(x) = x^n$$은 $$\lVert f_n - f\rVert_\infty = 1$$ ($$x$$를 $$1$$ 가까이 잡으면 $$f_n$$이 $$1$$에 가까우므로) 이어서 균등수렴하지 않으며, 이것이 그 극한이 불연속이었던 이유이다.

## 연속성과 적분의 보존

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2**</ins> 연속함수들의 열 $$(f_n)$$이 $$f$$로 균등수렴하면 $$f$$도 연속이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

점 $$a$$와 $$\varepsilon > 0$$에 대해, 균등수렴으로 $$\lVert f_n - f\rVert_\infty < \varepsilon/3$$인 $$n$$을 잡는다. $$f_n$$이 $$a$$에서 연속이므로 $$\lvert x - a\rvert < \delta$$이면 $$\lvert f_n(x) - f_n(a)\rvert < \varepsilon/3$$이다. 그러면

$$\lvert f(x) - f(a)\rvert \leq \lvert f(x) - f_n(x)\rvert + \lvert f_n(x) - f_n(a)\rvert + \lvert f_n(a) - f(a)\rvert < \varepsilon$$

이므로 $$f$$가 $$a$$에서 연속이다. 이 "$$\varepsilon/3$$ 논법"에서 첫째·셋째 항을 동시에 통제하는 데 균등성이 필수적이다.

</details>

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3**</ins> 연속함수들의 열 $$(f_n)$$이 $$[a,b]$$에서 $$f$$로 균등수렴하면

$$\lim_{n\to\infty}\int_a^b f_n = \int_a^b f = \int_a^b \lim_{n\to\infty} f_n$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$f$$는 정리 2로 연속이므로 적분가능하다 ([§Riemann 적분, ⁋정리 4](/ko/math/analysis/riemann_integral#thm4)). 단조성에 의해

$$\left\lvert\int_a^b f_n - \int_a^b f\right\rvert \leq \int_a^b \lvert f_n - f\rvert \leq \lVert f_n - f\rVert_\infty\,(b - a) \to 0$$

이다.

</details>

[§함수열과 점별수렴, ⁋예시 3](/ko/math/analysis/sequences_of_functions#ex3)의 반례에서 적분이 교환되지 않았던 것은 그 수렴이 균등하지 않았기 때문이다. (미분에 대해서는 더 강하게, $$f_n'$$ 자체의 균등수렴을 요구해야 극한과 미분이 교환된다.)

## 바이어슈트라스 M-판정

함수항급수 $$\sum f_n$$의 균등수렴을 보장하는 실용적 기준이다.

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4 (바이어슈트라스 M-판정)**</ins> 모든 $$x$$에서 $$\lvert f_n(x)\rvert \leq M_n$$이고 수치급수 $$\sum M_n$$이 수렴하면, 함수항급수 $$\sum f_n$$은 균등수렴(이며 절대수렴)한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

부분합 $$s_N = \sum_{n=1}^N f_n$$을 생각하자. $$M > N$$에 대해 $$\lVert s_M - s_N\rVert_\infty \leq \sum_{n=N+1}^M M_n$$인데, $$\sum M_n$$이 수렴하므로 우변은 $$N \to \infty$$에서 $$0$$으로 간다. 즉 $$(s_N)$$이 상한노름에 대해 Cauchy이고, 따라서 극한함수로 균등수렴한다 ([§Cauchy 수열과 완비성](/ko/math/analysis/cauchy_sequences)의 완비성 논법을 상한노름 공간에 적용).

</details>

균등수렴은 극한 연산과 미적분 연산을 교환할 수 있게 해 주는 핵심 조건이다. 그 가장 중요한 응용으로, 다음 글 [§멱급수와 해석함수](/ko/math/analysis/power_series)에서 멱급수가 수렴반경 안에서 균등수렴하여 항별 미분·적분이 정당화됨을 본다.
