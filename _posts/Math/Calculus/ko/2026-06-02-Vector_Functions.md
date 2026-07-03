---
title: "곡선과 벡터함수"
description: "한 매개변수로 공간곡선을 그리는 벡터값 함수를 도입하고, 성분별 미분으로 속도·가속도·단위접선벡터를 정의한다. 호의 길이와 호장 매개변수, 곡률과 단위법선벡터, 가속도의 접선·법선 분해를 다룬다."
excerpt: "벡터값 함수와 매개곡선, 속도와 접선, 호의 길이, 곡률과 가속도의 분해"

categories: [Math / Calculus]
permalink: /ko/math/calculus/vector_functions
sidebar: 
    nav: "calculus-ko"

date: 2026-06-02
weight: 13
published: false
---

지금까지 다룬 함수는 실수를 실수로 보내는 $$f:\mathbb{R}\to\mathbb{R}$$에 국한되었다. 이제 함수를 더 일반적으로 택하여 새로운 내용을 시작한다. 일반화의 방향은 차원을 늘리는 것인데, 정의역의 차원을 올리는 방향과 공역의 차원을 올리는 방향이 있다. 이 글에서는 후자, 곧 한 실수를 여러 실수로 보내는 함수 $$\mathbf{r}:\mathbb{R}\to\mathbb{R}^n$$을 다룬다. 이는 매개변수 하나로 공간 속의 곡선을 그리는 벡터값 함수로, 시간에 따라 움직이는 점의 자취로 볼 수 있어 미분이 속도와 가속도라는 물리적 의미를 얻고 적분이 곡선의 길이를 잰다.

## 벡터값 함수

::: 정의 1
구간 $$I \subseteq \mathbb{R}$$의 각 $$t$$에 점 $$\mathbf{r}(t) = (x_1(t), \ldots, x_n(t)) \in \mathbb{R}^n$$을 대응시키는 함수 $$\mathbf{r}\colon I \to \mathbb{R}^n$$을 *벡터값 함수<sub>vector-valued function</sub>* 또는 *매개곡선<sub>parametrized curve</sub>*이라 하고, 각 $$x_i$$를 그 *성분함수*라 한다.
:::

벡터값 함수의 극한·연속·미분은 모두 성분별로 정의된다. $$\mathbf{r}$$의 극한 $$\lim_{t \to t_0} \mathbf{r}(t)$$는 각 성분의 극한을 모은 벡터이고, $$\mathbf{r}$$이 $$t_0$$에서 연속이라는 것은 모든 성분함수가 $$t_0$$에서 연속이라는 것이다. 미분도 차분몫

$$\mathbf{r}'(t) = \lim_{h \to 0} \frac{\mathbf{r}(t+h) - \mathbf{r}(t)}{h}$$

으로 정의하되, 벡터의 극한이 성분별 극한이므로 다음이 성립한다.

::: 명제 2
$$\mathbf{r}(t) = (x_1(t), \ldots, x_n(t))$$의 각 성분함수가 $$t$$에서 미분가능하면 $$\mathbf{r}$$도 $$t$$에서 미분가능하고 $$\mathbf{r}'(t) = (x_1'(t), \ldots, x_n'(t))$$이다.
:::

::: 증명
차분몫 $$(\mathbf{r}(t+h) - \mathbf{r}(t))/h$$의 $$i$$번째 성분은 정확히 $$(x_i(t+h) - x_i(t))/h$$이다. 각 성분의 극한이 $$x_i'(t)$$로 존재하므로, 벡터의 극한이 성분별 극한과 같다는 사실에 의해 $$\mathbf{r}'(t) = (x_1'(t), \ldots, x_n'(t))$$이다.
:::

스칼라함수의 곱미분과 같은 규칙이 벡터의 곱셈들로 옮겨진다.

::: 명제 3 (미분 법칙)
$$\mathbf{u}, \mathbf{v}\colon I \to \mathbb{R}^n$$이 미분가능하고 $$f\colon I \to \mathbb{R}$$가 미분가능하며 $$\varphi\colon J \to I$$가 미분가능한 실함수이면

$$(f \mathbf{u})' = f' \mathbf{u} + f \mathbf{u}', \qquad (\mathbf{u} \cdot \mathbf{v})' = \mathbf{u}' \cdot \mathbf{v} + \mathbf{u} \cdot \mathbf{v}', \qquad (\mathbf{u} \circ \varphi)'(t) = \varphi'(t) \mathbf{u}'(\varphi(t))$$

이고, $$n = 3$$일 때 교차곱에 대해 $$(\mathbf{u} \times \mathbf{v})' = \mathbf{u}' \times \mathbf{v} + \mathbf{u} \times \mathbf{v}'$$이다.
:::

::: 증명
모두 성분별로 적으면 스칼라함수의 곱미분과 연쇄법칙으로 환원된다. 가령 점곱은 $$\mathbf{u} \cdot \mathbf{v} = \sum_i u_i v_i$$이므로 $$(\mathbf{u} \cdot \mathbf{v})' = \sum_i (u_i' v_i + u_i v_i') = \mathbf{u}' \cdot \mathbf{v} + \mathbf{u} \cdot \mathbf{v}'$$이고, 교차곱과 스칼라곱도 각 성분이 $$u_i v_j$$ 꼴의 곱들의 합이라 같은 방식으로 따른다. 합성은 [§미분법, ⁋정리 4](/ko/math/calculus/differentiation_rules#thm4)의 연쇄법칙을 각 성분에 적용한 것이다.
:::

점곱의 미분에서 곧바로 유용한 따름정리가 나온다. $$\lvert \mathbf{u}(t)\rvert$$가 상수이면 $$\mathbf{u} \cdot \mathbf{u} = \lvert \mathbf{u}\rvert^2$$도 상수이므로 $$(\mathbf{u} \cdot \mathbf{u})' = 2 \mathbf{u} \cdot \mathbf{u}' = 0$$, 곧 $$\mathbf{u} \perp \mathbf{u}'$$이다. 길이가 일정한 벡터의 변화율은 항상 그 벡터에 수직이다. 원운동에서 위치벡터와 속도가 수직인 것이 이 사실의 특수한 경우이다.

## 속도와 가속도

::: 정의 4
매개곡선 $$\mathbf{r}(t)$$에 대해 $$\mathbf{r}'(t)$$를 *속도<sub>velocity</sub>*, 그 크기 $$\lvert \mathbf{r}'(t)\rvert$$를 *속력<sub>speed</sub>*, $$\mathbf{r}''(t)$$를 *가속도<sub>acceleration</sub>*라 한다. $$\mathbf{r}'(t) \neq 0$$인 점에서

$$\mathbf{T}(t) = \frac{\mathbf{r}'(t)}{\lvert \mathbf{r}'(t)\rvert}$$

을 *단위접선벡터<sub>unit tangent vector</sub>*라 한다.
:::

속도는 곡선의 진행 방향을 가리키고 그 크기가 점이 움직이는 빠르기이며, 단위접선벡터는 방향만 남긴 것이다. 가령 나선 $$\mathbf{r}(t) = (\cos t, \sin t, t)$$는 $$\mathbf{r}'(t) = (-\sin t, \cos t, 1)$$로 속력이 $$\lvert \mathbf{r}'(t)\rvert = \sqrt{2}$$로 일정하고, 단위접선벡터는 $$\mathbf{T}(t) = (-\sin t, \cos t, 1)/\sqrt{2}$$이다.

## 호의 길이

곡선의 길이는 곡선 위의 점들을 잇는 다각형으로 근사한다. 분할 $$a = t_0 < \cdots < t_m = b$$에 대해 선분 길이의 합 $$\sum_k \lvert \mathbf{r}(t_k) - \mathbf{r}(t_{k-1})\rvert$$을 만들고 분할을 잘게 하는 것이다. 각 선분에 평균값 정리를 성분별로 적용하면 $$\mathbf{r}(t_k) - \mathbf{r}(t_{k-1}) \approx \mathbf{r}'(t_k^\ast)\Delta t_k$$이고, 이 합은 $$\lvert \mathbf{r}'(t)\rvert$$의 리만 합으로 수렴한다. 이 극한을 곡선의 길이로 삼는다.

::: 정의 5
$$C^1$$ 매개곡선 $$\mathbf{r}\colon [a, b] \to \mathbb{R}^n$$의 *호의 길이<sub>arc length</sub>*는

$$L = \int_a^b \lvert \mathbf{r}'(t)\rvert dt$$

이다.
:::

피적분함수 $$\lvert \mathbf{r}'(t)\rvert$$는 연속이므로 적분가능하다 ([§적분, ⁋정리 10](/ko/math/calculus/integration#thm10)). 가령 위 나선의 $$0 \leq t \leq 2\pi$$ 부분은 $$L = \int_0^{2\pi} \sqrt{2}dt = 2\sqrt{2}\pi$$이다. 이제 시작점에서 잰 호의 길이

$$s(t) = \int_a^t \lvert \mathbf{r}'(\tau)\rvert d\tau$$

를 *호장 매개변수<sub>arc length parameter</sub>*라 한다. 미적분의 기본정리로 $$s'(t) = \lvert \mathbf{r}'(t)\rvert > 0$$이므로 (정칙곡선, 곧 $$\mathbf{r}' \neq 0$$인 경우) $$s$$는 증가함수이고, $$t$$를 $$s$$로 풀어 곡선을 호장으로 다시 매개화할 수 있다.

::: 명제 6
곡선을 호장 매개변수 $$s$$로 매개화하면 단위속력이다. 즉 $$\lvert d\mathbf{r}/ds\rvert = 1$$이다.
:::

::: 증명
연쇄법칙으로 $$d\mathbf{r}/dt = (d\mathbf{r}/ds)(ds/dt)$$이고 $$ds/dt = \lvert \mathbf{r}'(t)\rvert = \lvert d\mathbf{r}/dt\rvert$$이므로, $$\lvert d\mathbf{r}/ds\rvert = \lvert d\mathbf{r}/dt\rvert / (ds/dt) = 1$$이다.
:::

## 곡률

곡선이 얼마나 휘는지는 단위접선벡터의 방향이 진행에 따라 얼마나 빨리 바뀌는가로 잰다. 빠르기에 휘둘리지 않으려면 시간이 아니라 호장에 대한 변화율을 본다.

::: 정의 7
정칙곡선의 *곡률<sub>curvature</sub>*은 단위접선벡터가 호장에 대해 변하는 비율의 크기

$$\kappa = \left\lvert \frac{d\mathbf{T}}{ds}\right\rvert$$

이다. $$d\mathbf{T}/ds \neq 0$$일 때 그 방향의 단위벡터 $$\mathbf{N} = (d\mathbf{T}/ds)/\lvert d\mathbf{T}/ds\rvert$$를 *단위법선벡터<sub>unit normal vector</sub>*라 한다.
:::

[명제 6](#prop6)의 따름으로 $$\mathbf{T} = d\mathbf{r}/ds$$는 단위벡터이므로, 길이가 일정한 벡터의 변화율은 그 벡터에 수직이라는 앞의 관찰에 의해 $$d\mathbf{T}/ds \perp \mathbf{T}$$이다. 곧 단위법선벡터 $$\mathbf{N}$$은 항상 접선에 수직이며, 곡선이 휘어 들어가는 안쪽을 가리킨다. 정의는 호장 매개변수를 쓰지만, 실제 계산에는 임의의 매개변수로 적은 다음 공식이 편하다.

::: 명제 8 (곡률 공식)
임의의 정칙 매개변수 $$t$$에 대해 공간곡선의 곡률은

$$\kappa = \frac{\lvert \mathbf{r}' \times \mathbf{r}''\rvert}{\lvert \mathbf{r}'\rvert^3}$$

이고, 특히 평면곡선 $$y = f(x)$$의 곡률은 $$\kappa = \lvert f''\rvert / (1 + f'^2)^{3/2}$$이다.
:::

::: 증명
$$v = \lvert \mathbf{r}'\rvert = ds/dt$$로 두면 $$\mathbf{r}' = v\mathbf{T}$$이다. 곱미분으로 $$\mathbf{r}'' = v'\mathbf{T} + v\mathbf{T}'(t)$$이고, 연쇄법칙 $$\mathbf{T}'(t) = (d\mathbf{T}/ds)v$$와 $$\lvert d\mathbf{T}/ds\rvert = \kappa$$에서 $$\mathbf{T}'(t) = \kappa v\mathbf{N}$$이다. 따라서

$$\mathbf{r}' \times \mathbf{r}'' = (v\mathbf{T}) \times (v'\mathbf{T} + \kappa v^2\mathbf{N}) = v^3 \kappa(\mathbf{T} \times \mathbf{N})$$

인데 ($$\mathbf{T} \times \mathbf{T} = 0$$) $$\mathbf{T} \perp \mathbf{N}$$이고 둘 다 단위벡터라 $$\lvert \mathbf{T} \times \mathbf{N}\rvert = 1$$이므로 $$\lvert \mathbf{r}' \times \mathbf{r}''\rvert = v^3 \kappa = \lvert \mathbf{r}'\rvert^3 \kappa$$, 곧 주장이 따른다. 평면곡선 $$y = f(x)$$는 $$\mathbf{r}(x) = (x, f(x))$$로 매개화하면 $$\mathbf{r}' = (1, f')$$, $$\mathbf{r}'' = (0, f'')$$이고 평면에서의 교차곱 크기 $$\lvert \mathbf{r}' \times \mathbf{r}''\rvert = \lvert f''\rvert$$, $$\lvert \mathbf{r}'\rvert = (1 + f'^2)^{1/2}$$이라 위 공식에서 곧바로 나온다.
:::

증명에 등장한 $$\mathbf{r}' = v\mathbf{T}$$를 한 번 더 미분한 $$\mathbf{r}'' = v'\mathbf{T} + \kappa v^2\mathbf{N}$$은 그 자체로 의미가 깊다. 가속도가 접선 방향 성분과 법선 방향 성분으로 갈라지는 것이다.

::: 명제 9 (가속도의 분해)
정칙곡선의 가속도는 $$\mathbf{r}'' = \frac{dv}{dt}\mathbf{T} + \kappa v^2\mathbf{N}$$으로 분해된다. 여기서 $$v = \lvert \mathbf{r}'\rvert$$는 속력이다.
:::

접선 성분 $$dv/dt$$는 속력이 변하는 정도, 법선 성분 $$\kappa v^2$$은 방향이 휘는 정도이다. 등속운동이면 $$dv/dt = 0$$이라 가속도는 순전히 법선 방향, 곧 구심가속도뿐이고 그 크기는 $$\kappa v^2$$이다. 반지름 $$\rho$$인 원을 속력 $$v$$로 도는 운동은 $$\kappa = 1/\rho$$이므로 익숙한 $$v^2/\rho$$를 회복한다.

::: 예시 10 (나선)
나선 $$\mathbf{r}(t) = (\cos t, \sin t, t)$$에 대해 $$\mathbf{r}'(t) = (-\sin t, \cos t, 1)$$, $$\mathbf{r}''(t) = (-\cos t, -\sin t, 0)$$이다. 교차곱은

$$\mathbf{r}' \times \mathbf{r}'' = (\sin t,\ -\cos t,\ 1), \qquad \lvert \mathbf{r}' \times \mathbf{r}''\rvert = \sqrt{2}$$

이고 $$\lvert \mathbf{r}'\rvert = \sqrt{2}$$이므로 곡률은 $$\kappa = \sqrt{2}/(\sqrt{2})^3 = 1/2$$로 일정하다. 속력 $$v = \sqrt{2}$$가 일정하므로 [명제 9](#prop9)에서 가속도는 법선 성분뿐이고 그 크기는 $$\kappa v^2 = (1/2)\cdot 2 = 1$$인데, 실제로 $$\lvert \mathbf{r}''(t)\rvert = \lvert(-\cos t, -\sin t, 0)\rvert = 1$$로 일치한다.
:::

::: 예시 11 (포물선의 곡률)
포물선 $$y = x^2$$은 $$f' = 2x$$, $$f'' = 2$$이므로 $$\kappa(x) = 2/(1 + 4x^2)^{3/2}$$이다. 꼭짓점 $$x = 0$$에서 $$\kappa = 2$$로 가장 크고, $$\lvert x\rvert \to \infty$$에서 $$\kappa \to 0$$으로 점점 직선에 가까워진다. 곡률이 최대인 꼭짓점은 곡선이 가장 급하게 휘는 점이다.
:::
