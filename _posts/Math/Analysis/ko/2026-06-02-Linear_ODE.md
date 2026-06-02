---
title: "선형 미분방정식계"
description: "선형 미분방정식계의 해가 구간 전체에서 전역적으로 존재하고 유일함을 보인다. 상수계수 선형계의 해를 행렬지수로 표현하고, 그 계산이 계수행렬의 고윳값 구조로 환원됨을 본다."
excerpt: "선형계의 전역 존재유일성, 행렬지수, 고윳값과 해"

categories: [Math / Analysis]
permalink: /ko/math/analysis/linear_ode
sidebar: 
    nav: "analysis-ko"

header:
    overlay_image: /assets/images/Math/Analysis/Linear_ODE.png
    overlay_filter: 0.5

date: 2026-06-02
last_modified_at: 2026-06-02
weight: 22

published: false
---

[§미분방정식의 존재성과 유일성](/ko/math/analysis/existence_uniqueness_ode)에서 립시츠 조건 아래 해가 국소적으로 존재함을 보았다. 미분방정식 가운데 가장 잘 이해된 부류가 선형계이며, 여기서는 해가 전역적으로 존재할 뿐 아니라 선형대수로 명시적으로 풀린다. 이로써 해석학의 미분방정식 이론이 선형대수와 만난다.

## 선형계의 전역 존재유일성

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $$n$$차 벡터값 함수 $$y(t) \in \mathbb{R}^n$$에 대한 *선형 미분방정식계*는

$$y'(t) = A(t)\,y(t) + b(t)$$

꼴이다. 여기서 $$A(t)$$는 $$n\times n$$ 행렬값, $$b(t)$$는 벡터값 연속함수이다. $$b \equiv 0$$이면 *제차*라 한다.

</div>

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2**</ins> $$A(t), b(t)$$가 구간 $$I$$에서 연속이면, 임의의 초기 조건 $$y(t_0) = y_0$$에 대한 해가 $$I$$ 전체에서 유일하게 존재한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$f(t, y) = A(t)y + b(t)$$는 $$\lvert f(t, y_1) - f(t, y_2)\rvert = \lvert A(t)(y_1 - y_2)\rvert \leq \lVert A(t)\rVert\,\lvert y_1 - y_2\rvert$$이므로, $$I$$의 임의의 컴팩트 부분구간에서 $$\lVert A(t)\rVert$$이 유계여서 ([§연속함수의 성질, ⁋따름정리 2](/ko/math/analysis/continuous_functions#cor2)) 립시츠 조건을 만족한다. 피카르–린델뢰프 정리 ([§미분방정식의 존재성과 유일성, ⁋정리 4](/ko/math/analysis/existence_uniqueness_ode#thm4))로 국소해가 존재하며, 립시츠 상수가 해의 크기에 무관하게 균일하므로 해가 폭발하지 않고 $$I$$ 전체로 확장된다.

</details>

비선형 방정식의 해가 유한 시간에 발산할 수 있는 것과 달리, 선형계의 해는 계수가 정의된 구간 전체에 걸쳐 존재한다.

## 행렬지수와 상수계수 해

$$A$$가 상수행렬인 제차계 $$y' = Ay$$는 한 변수 지수함수의 직접적 일반화로 풀린다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> $$n\times n$$ 행렬 $$A$$의 *행렬지수<sub>matrix exponential</sub>*를

$$e^{A} = \sum_{k=0}^{\infty}\frac{A^k}{k!} = I + A + \frac{A^2}{2!} + \cdots$$

으로 정의한다. 이 급수는 모든 $$A$$에 대해 (성분별로) 절대수렴한다.

</div>

급수의 수렴은 $$\lVert A^k/k!\rVert \leq \lVert A\rVert^k/k!$$에 바이어슈트라스 M-판정 ([§균등수렴, ⁋정리 4](/ko/math/analysis/uniform_convergence#thm4))을 적용하면 따른다. 행렬지수를 항별 미분하면 $$\dfrac{d}{dt}e^{tA} = A e^{tA}$$이므로 다음을 얻는다.

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4**</ins> 상수계수 제차계 $$y' = Ay$$, $$y(0) = y_0$$의 유일한 해는

$$y(t) = e^{tA}\,y_0$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$y(t) = e^{tA}y_0$$은 $$y(0) = e^0 y_0 = y_0$$이고 $$y'(t) = A e^{tA}y_0 = Ay(t)$$이므로 해이다. 정리 2의 유일성에 의해 이것이 유일한 해이다.

</details>

## 고윳값을 통한 계산

행렬지수의 실제 계산은 $$A$$의 고유구조로 환원된다. $$A$$가 고윳값 $$\lambda$$, 고유벡터 $$v$$를 가지면 $$A v = \lambda v$$이므로 $$e^{tA}v = e^{\lambda t} v$$이고, $$v e^{\lambda t}$$가 해가 된다. 따라서 $$A$$가 대각화되면 — 고유벡터들이 기저를 이루면 — 해는 $$e^{\lambda_i t}$$ 꼴의 항들의 결합으로 명시적으로 적힌다. 대각화되지 않는 경우에는 조르당 표준형을 써서 $$t^j e^{\lambda t}$$ 꼴의 항이 추가된다.

이렇게 선형 미분방정식의 풀이는 행렬의 고윳값·고유벡터 — 곧 선형사상의 스펙트럼 구조 ([\[다중선형대수학\] §행렬과 선형사상](/ko/math/multilinear_algebra/matrices_and_linear_maps)) — 로 완전히 귀착된다. 미분방정식의 해의 정성적 거동(평형의 안정성, 진동, 발산)이 고윳값의 실수부와 허수부로 읽힌다는 사실은 동역학계 이론의 출발점이며, 해석학·선형대수·기하가 만나는 지점이다.
