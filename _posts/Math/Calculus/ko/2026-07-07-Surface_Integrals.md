---
title: "면적분과 선속"
description: "두 매개변수로 곡면을 기술하는 매개곡면과 접벡터의 교차곱으로 주어지는 법선벡터를 도입한다. 곡면넓이와 스칼라 면적분을 정의하고, 곡면의 방향과 벡터장의 선속(flux)을 정의하여 구 위에서 계산한다."
excerpt: "매개곡면과 법선벡터, 곡면넓이, 스칼라 면적분, 선속(flux)"

categories: [Math / Calculus]
permalink: /ko/math/calculus/surface_integrals
sidebar: 
    nav: "calculus-ko"

date: 2026-07-07
weight: 19
---

이제 우리는 선적분에서 변수를 하나 추가하여 곡면의 적분을 정의한다. 

## 매개곡면

::: 정의 1
평면 영역 $D$에서 정의된 $C^1$ 사상 

$\mathbf{r}\colon D \rightarrow \mathbb{R}^3$, $\mathbf{r}(u, v) = (x(u,v), y(u,v), z(u,v))$

를 *매개곡면<sub>parametrized surface</sub>*이라 한다. 
:::


$u$를 고정하고 $v$만 움직이면 곡면 위의 곡선이 그려지고 그 접선이 $\mathbf{r}_v$이며, 마찬가지로 $\mathbf{r}_u$도 곡면 위의 한 곡선의 접선이다. 두 접벡터가 펼치는 평면이 접평면이고, 그에 수직인 $\mathbf{r}_u \times \mathbf{r}_v$가 법선 방향을 준다. 즉, 편도함수 벡터 $\mathbf{r}_u = \partial \mathbf{r}/\partial u$와 $\mathbf{r}_v = \partial \mathbf{r}/\partial v$는 곡면에 접하며, 그 교차곱

$$\mathbf{N} = \mathbf{r}_u \times \mathbf{r}_v$$

가 곡면의 법선벡터이다. 우리는 $\mathbf{N} \neq 0$인 곡면을 *regular<sub>정칙</sub>*이라 한다.

## 곡면넓이

곡면을 매개변수 영역의 작은 직사각형들로 쪼개면, 각 조각은 접평면 위의 작은 평행사변형, 더 구체적으로는 $\mathbf{r}_u\Delta u$와 $\mathbf{r}_v\Delta v$가 만드는 평행사변형으로 근사된다. 이 넓이가 $\lvert \mathbf{r}_u \times \mathbf{r}_v\rvert\Delta u\Delta v$이므로, 이를 모아 극한을 취한 것이 곡면넓이이다.

::: 정의 2
regular 매개곡면 $\mathbf{r}\colon D \rightarrow \mathbb{R}^3$의 *곡면넓이<sub>surface area</sub>*는

$$\iint_D \lvert \mathbf{r}_u \times \mathbf{r}_v\rvert \mathop{du}\mathop{dv}$$

이고, 면적원소를 $dS = \lvert \mathbf{r}_u \times \mathbf{r}_v\rvert \mathop{du}\mathop{dv}$로 적는다.
:::

면적원소 $dS$는 다중적분의 야코비 행렬식과 같은 역할을 하는 것으로, 이렇게 정의한 면적원소 $dS$로 곡면 위에 분포한 스칼라량을 적분할 수 있다.

::: 정의 3
곡면 $S$ 위에서 연속인 스칼라장 $f$의 *면적분<sub>surface integral</sub>*은

$$\iint_S f\mathop{dS} = \iint_D f(\mathbf{r}(u,v))\lvert \mathbf{r}_u \times \mathbf{r}_v\rvert \mathop{du}\mathop{dv}$$

이다.
:::

선적분이 arc length parametrization으로 적분하여 곡선의 매개화에 무관했듯, 면적분도 면적원소로 적분하여 곡면의 매개화에 무관하다. 

## 선속

한편 우리는 스칼라함수가 아니라 벡터함수를 곡면을 따라 적분하는 상황 또한 생각할 수 있다. 이를 위해서는 앞선 글과 마찬가지로 곡면의 어느 쪽이 "바깥"인지를 정해야 한다. 곡면의 경우, 각 점에서 두 단위법선 $\pm \mathbf{N}/\lvert \mathbf{N}\rvert$ 중 하나를 연속적으로 고르는 것을 곡면의 *방향<sub>orientation</sub>*이라 한다.

::: 정의 4
단위법선 $\mathbf{n}$으로 방향이 주어진 곡면 $S$ 위의 연속 벡터장 $\mathbf{F}$의 *선속<sub>flux</sub>*은

$$\iint_S \mathbf{F} \cdot d\mathbf{S} = \iint_S \mathbf{F} \cdot \mathbf{n}\mathop{dS} = \iint_D \mathbf{F}(\mathbf{r}(u,v)) \cdot (\mathbf{r}_u \times \mathbf{r}_v)\mathop{du}\mathop{dv}$$

이다. 여기서 $\mathbf{n} = (\mathbf{r}_u \times \mathbf{r}_v)/\lvert \mathbf{r}_u \times \mathbf{r}_v\rvert$가 곡면의 방향과 맞는다고 본다.
:::

선속은 단위시간에 곡면을 가로질러 흐르는 양이다. 가령 $\mathbf{F}$가 유체의 속도이면 $\iint_S \mathbf{F}\cdot d\mathbf{S}$는 곡면을 통과하는 유체의 양으로 생각할 수 있다. 그럼 법선 성분 $\mathbf{F}\cdot \mathbf{n}$만이 흐름에 기여하며 곡면에 접하는 성분은 이 양에 기여하지 않는다는 것이 직관적으로 자명하며, 방향을 반대로 잡으면 $\mathbf{n}$이 뒤집혀 선속의 부호가 바뀐다는 것 또한 쉽게 확인할 수 있다.

다음은 이 적분의 두 예시들이다.

::: 예시 5 (구의 겉넓이)
반지름 $R$인 구를 구면좌표

$$\mathbf{r}(\phi, \theta) = (R\sin\phi\cos\theta, R\sin\phi\sin\theta, R\cos\phi),\qquad 0 \leq \phi \leq \pi,\quad 0 \leq \theta \leq 2\pi$$

로 매개화하자. 접벡터의 교차곱을 계산하면 그 크기는 

$$\lvert \mathbf{r}_\phi \times \mathbf{r}_\theta\rvert = R^2\sin\phi$$

이며, 따라서 곡면의 넓이는

$$\iint_S \mathop{dS} = \int_0^{2\pi} \int_0^\pi R^2\sin\phi \mathop{d\phi} \mathop{d\theta} = R^2 \cdot 2\pi \cdot 2 = 4\pi R^2$$

으로 익숙한 값이 나온다.
:::

다음은 벡터함수의 적분의 예시이다. 

::: 예시 6
[예시 5](#ex5)의 구에, 바깥 방향을 주자. 이 예시에서 우리의 목표는 

$$\mathbf{F}(x,y,z) = (x,y,z)$$

의 선속을 구하는 것이다. 마찬가지로 구면 매개화에서 

$$\mathbf{r}_\phi \times \mathbf{r}_\theta = R(\sin\phi) \mathbf{r}$$

이고 $\mathbf{F}(\mathbf{r}) = \mathbf{r}$이므로 

$$\mathbf{F}\cdot(\mathbf{r}_\phi\times \mathbf{r}_\theta) = \mathbf{r} \cdot R\sin\phi \mathbf{r} = R\sin\phi\lvert \mathbf{r}\rvert^2 = R^3\sin\phi$$

이다. 그러므로

$$\iint_S \mathbf{F}\cdot d\mathbf{S} = \int_0^{2\pi} \int_0^\pi R^3\sin\phi \mathop{d\phi} \mathop{d\theta} = 4\pi R^3$$

이다.
:::
