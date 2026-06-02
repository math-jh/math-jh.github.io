---
title: "함수열과 점별수렴"
description: "함수들의 열이 수렴하는 가장 단순한 방식인 점별수렴을 정의하고, 그것이 연속성·적분·미분을 보존하지 못함을 구체적 반례로 보인다. 이로써 더 강한 균등수렴의 필요성을 드러낸다."
excerpt: "점별수렴, 연속성·적분의 비보존, 균등수렴의 동기"

categories: [Math / Analysis]
permalink: /ko/math/analysis/sequences_of_functions
sidebar: 
    nav: "analysis-ko"

header:
    overlay_image: /assets/images/Math/Analysis/Sequences_of_Functions.png
    overlay_filter: 0.5

date: 2026-07-18
last_modified_at: 2026-07-18

weight: 16

published: false
---

지금까지 수렴은 수들의 열에 관한 것이었다. 그러나 멱급수의 부분합처럼, 함수들의 열 $$(f_n)$$이 어떤 함수 $$f$$로 수렴한다는 것을 다루어야 할 때가 많다. 함수열의 수렴에는 여러 강도가 있으며, 가장 약한 점별수렴은 우리가 보존되기를 바라는 성질들을 의외로 잘 지키지 못한다.

## 점별수렴

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 함수열 $$(f_n)$$이 함수 $$f$$로 *점별수렴<sub>pointwise convergence</sub>*한다는 것은, 정의역의 각 점 $$x$$마다 수열 $$(f_n(x))$$이 $$f(x)$$로 수렴하는 것이다. 즉 각 $$x$$와 각 $$\varepsilon > 0$$에 대해 $$N$$ (이때 $$N$$은 $$x$$에 따라 달라질 수 있다) 이 있어 $$n \geq N$$이면 $$\lvert f_n(x) - f(x)\rvert < \varepsilon$$이다.

</div>

핵심은 $$N$$이 점 $$x$$마다 다를 수 있다는 데 있다. 이 자유 때문에 극한함수가 원래 함수들의 좋은 성질을 잃을 수 있다.

## 점별수렴이 보존하지 못하는 것

<div class="example" markdown="1">

<ins id="ex2">**예시 2 (연속성의 상실)**</ins> $$[0,1]$$에서 $$f_n(x) = x^n$$을 보자. $$0 \leq x < 1$$이면 $$x^n \to 0$$이고 $$x = 1$$이면 $$x^n \to 1$$이므로, 극한함수는

$$f(x) = \begin{cases} 0, & 0 \leq x < 1,\\ 1, & x = 1 \end{cases}$$

이다. 각 $$f_n$$은 연속이지만 극한 $$f$$는 $$x = 1$$에서 불연속이다. 즉 점별수렴은 연속성을 보존하지 않는다.

</div>

<div class="example" markdown="1">

<ins id="ex3">**예시 3 (적분의 비교환)**</ins> $$[0,1]$$에서 $$g_n$$을 밑변 $$[0, 1/n]$$, 높이 $$n$$인 삼각형꼴 함수 (나머지에서 $$0$$) 로 두면, 각 점에서 $$g_n(x) \to 0$$이므로 점별극한은 $$0$$이다. 그러나 모든 $$n$$에서 $$\int_0^1 g_n = \tfrac12$$이므로

$$\lim_{n\to\infty}\int_0^1 g_n = \tfrac12 \neq 0 = \int_0^1 \lim_{n\to\infty} g_n$$

이다. 즉 극한과 적분을 바꿔 쓸 수 없다.

</div>

미분에 대해서도 사정은 마찬가지여서, 점별수렴하는 함수열의 도함수가 극한함수의 도함수로 수렴하지 않는 예가 흔하다.

## 균등수렴의 필요

예시들의 공통된 병폐는, 수렴의 빠르기가 점마다 제각각이어서 — 예시 2에서 $$x$$가 $$1$$에 가까울수록 $$x^n$$이 $$0$$으로 가는 속도가 한없이 느려진다 — 극한이 "고르게" 일어나지 않는다는 데 있다. 이를 막으려면 $$N$$을 모든 점에 대해 *동시에* 잡을 수 있어야 한다.

이렇게 점에 무관하게 일정한 수렴을 요구하는 것이 *균등수렴*이며, 다음 글 [§균등수렴](/ko/math/analysis/uniform_convergence)에서 정의한다. 균등수렴 아래에서는 연속성이 보존되고 극한과 적분이 교환되며, 그 결과로 [§멱급수와 해석함수](/ko/math/analysis/power_series)에서 멱급수의 항별 미분·적분이 정당화된다.
