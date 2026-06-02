---
title: "미분방정식의 존재성과 유일성"
description: "완비 거리공간 위의 축약사상 원리를 증명하고, 미분방정식의 초기값 문제를 적분방정식으로 바꾸어 그 해의 존재와 유일성을 보이는 피카르–린델뢰프 정리를 확립한다."
excerpt: "축약사상 원리, 립시츠 조건, 피카르–린델뢰프 정리"

categories: [Math / Analysis]
permalink: /ko/math/analysis/existence_uniqueness_ode
sidebar: 
    nav: "analysis-ko"

header:
    overlay_image: /assets/images/Math/Analysis/Existence_Uniqueness_ODE.png
    overlay_filter: 0.5

date: 2026-06-02
last_modified_at: 2026-06-02
weight: 21

published: false
---

미분방정식은 함수와 그 도함수의 관계로 함수를 규정한다. 가장 기본적인 물음은 주어진 초기 조건 아래 해가 존재하는가, 그리고 유일한가이다. 이 글에서는 해석학의 존재 정리를 떠받치는 축약사상 원리를 증명하고, 이를 미분방정식에 적용한다.

## 축약사상 원리

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 거리공간 $$(X, d)$$의 사상 $$T : X \to X$$가 *축약사상<sub>contraction</sub>*이라는 것은, 어떤 상수 $$0 \leq \lambda < 1$$에 대하여 모든 $$x, y$$에서 $$d(T x, T y) \leq \lambda\, d(x, y)$$인 것이다.

</div>

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2 (바나흐 고정점 정리)**</ins> 완비 거리공간 위의 축약사상 $$T$$는 유일한 고정점 $$x^\ast = T x^\ast$$를 가지며, 임의의 출발점 $$x_0$$에서 시작한 반복 $$x_{n+1} = T x_n$$이 그 고정점으로 수렴한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$d(x_{n+1}, x_n) = d(Tx_n, Tx_{n-1}) \leq \lambda\, d(x_n, x_{n-1})$$이므로 $$d(x_{n+1}, x_n) \leq \lambda^n d(x_1, x_0)$$이다. $$m > n$$에 대해 삼각부등식과 등비급수로

$$d(x_m, x_n) \leq \sum_{k=n}^{m-1}\lambda^k d(x_1, x_0) \leq \frac{\lambda^n}{1 - \lambda}d(x_1, x_0)$$

이고 우변이 $$0$$으로 가므로 $$(x_n)$$은 Cauchy이다. 공간이 완비이므로 ([§거리공간, ⁋정의 4](/ko/math/analysis/metric_spaces#def4)) $$x_n \to x^\ast$$이 존재하고, $$T$$가 연속이므로 $$x^\ast = \lim x_{n+1} = \lim T x_n = T x^\ast$$이다. 유일성은 $$x^\ast, y^\ast$$가 둘 다 고정점이면 $$d(x^\ast, y^\ast) = d(Tx^\ast, Ty^\ast) \leq \lambda d(x^\ast, y^\ast)$$이고 $$\lambda < 1$$이므로 $$d(x^\ast, y^\ast) = 0$$임에서 따른다.

</details>

## 피카르–린델뢰프 정리

이제 초기값 문제

$$y'(t) = f(t, y(t)), \qquad y(t_0) = y_0$$

를 생각한다. 해의 존재·유일성은 $$f$$가 둘째 변수에 대해 다음 조건을 만족할 때 보장된다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> $$f(t, y)$$가 $$y$$에 대해 *립시츠 조건<sub>Lipschitz condition</sub>*을 만족한다는 것은, 상수 $$L$$이 존재하여 $$\lvert f(t, y_1) - f(t, y_2)\rvert \leq L\lvert y_1 - y_2\rvert$$이 성립하는 것이다.

</div>

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4 (피카르–린델뢰프)**</ins> $$f$$가 $$(t_0, y_0)$$ 근방에서 연속이고 $$y$$에 대해 립시츠 조건을 만족하면, $$t_0$$의 어떤 닫힌구간 $$I$$ 위에서 초기값 문제의 해가 유일하게 존재한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

미분방정식과 초기 조건을 적분하면, 미적분의 기본정리 ([§미적분의 기본정리, ⁋정리 2](/ko/math/analysis/fundamental_theorem_of_calculus#thm2))에 의해 문제는 적분방정식

$$y(t) = y_0 + \int_{t_0}^t f(s, y(s))\,ds$$

와 동치이다. 우변을 연속함수 $$y$$에 대응시키는 *피카르 작용소* $$(Ty)(t) = y_0 + \int_{t_0}^t f(s, y(s))\,ds$$를 생각하자. 충분히 짧은 구간 $$I$$에서 연속함수들의 공간 $$C(I)$$에 상한노름을 주면 이는 완비 거리공간이고, 립시츠 조건에 의해

$$\lVert Ty_1 - Ty_2\rVert_\infty \leq L\,\lvert I\rvert\,\lVert y_1 - y_2\rVert_\infty$$

이다. $$\lvert I\rvert$$를 $$L\lvert I\rvert < 1$$이 되도록 잡으면 $$T$$가 축약사상이므로, 바나흐 고정점 정리에 의해 유일한 고정점 $$y$$가 존재한다. 이 $$y$$가 초기값 문제의 유일한 해이다.

</details>

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> $$y' = y$$, $$y(0) = 1$$에서 피카르 반복을 $$y_0 \equiv 1$$에서 시작하면 $$y_1(t) = 1 + t$$, $$y_2(t) = 1 + t + \tfrac{t^2}{2}$$, $$\ldots$$로, $$y_n(t) = \sum_{k=0}^n \tfrac{t^k}{k!}$$이 지수함수 $$e^t$$로 수렴한다. 이는 알려진 해 $$y = e^t$$와 일치한다.

</div>

립시츠 조건이 없으면 유일성이 깨질 수 있다: $$y' = \sqrt{\lvert y\rvert}$$, $$y(0) = 0$$은 $$y \equiv 0$$ 외에 $$y = t^2/4$$ ($$t \geq 0$$) 도 해로 가진다. 한편 $$f$$가 $$y$$에 대해 선형이면 립시츠 조건이 전역적으로 성립하여 해가 구간 전체로 확장되는데, 이 중요한 경우를 다음 글 [§선형 미분방정식계](/ko/math/analysis/linear_ode)에서 다룬다.
