---
title: "면적분과 선속"
description: "두 매개변수로 곡면을 기술하는 매개곡면과 접벡터의 교차곱으로 주어지는 법선벡터를 도입한다. 곡면넓이와 스칼라 면적분을 정의하고, 곡면의 방향과 벡터장의 선속(flux)을 정의하여 구 위에서 계산한다."
excerpt: "매개곡면과 법선벡터, 곡면넓이, 스칼라 면적분, 선속(flux)"

categories: [Math / Calculus]
permalink: /ko/math/calculus/surface_integrals
sidebar: 
    nav: "calculus-ko"

date: 2026-06-02
weight: 19
published: false
---

곡선이 한 매개변수로 그려졌듯, 곡면은 두 매개변수로 그려진다. 곡선의 선적분에 대응하여, 곡면 위에 분포한 양을 더하면 스칼라 면적분이, 곡면을 가로질러 흐르는 벡터장의 양을 재면 선속이 된다. 선속은 발산정리와 스토크스 정리에서 적분정리의 한 변을 이루는 핵심량이다.

## 매개곡면

::: 정의 1
평면 영역 $$D$$에서 정의된 $$C^1$$ 사상 $$\mathbf{r}\colon D \to \mathbb{R}^3$$, $$\mathbf{r}(u, v) = (x(u,v), y(u,v), z(u,v))$$를 *매개곡면<sub>parametrized surface</sub>*이라 한다. 편도함수 벡터 $$\mathbf{r}_u = \partial \mathbf{r}/\partial u$$와 $$\mathbf{r}_v = \partial \mathbf{r}/\partial v$$는 곡면에 접하며, 그 교차곱

$$\mathbf{N} = \mathbf{r}_u \times \mathbf{r}_v$$

가 곡면의 법선벡터이다. $$\mathbf{N} \neq 0$$인 곡면을 *정칙<sub>regular</sub>*이라 한다.
:::

$$u$$를 고정하고 $$v$$만 움직이면 곡면 위의 곡선이 그려지고 그 접선이 $$\mathbf{r}_v$$이며, 마찬가지로 $$\mathbf{r}_u$$도 곡면 위의 한 곡선의 접선이다. 두 접벡터가 펼치는 평면이 접평면이고, 그에 수직인 $$\mathbf{r}_u \times \mathbf{r}_v$$가 법선 방향을 준다. 가령 그래프 $$z = g(x,y)$$는 $$\mathbf{r}(x,y) = (x, y, g(x,y))$$로 매개화되어 $$\mathbf{r}_x = (1, 0, g_x)$$, $$\mathbf{r}_y = (0, 1, g_y)$$, $$\mathbf{N} = (-g_x, -g_y, 1)$$이다.

## 곡면넓이

곡면을 매개변수 영역의 작은 직사각형들로 쪼개면, 각 조각은 접평면 위의 작은 평행사변형 $$\mathbf{r}_u\Delta u$$와 $$\mathbf{r}_v\Delta v$$로 근사된다. 그 넓이가 $$\lvert \mathbf{r}_u \times \mathbf{r}_v\rvert\Delta u\Delta v$$이므로, 이를 모아 극한을 취한 것이 곡면넓이이다.

::: 정의 2
정칙 매개곡면 $$\mathbf{r}\colon D \to \mathbb{R}^3$$의 *곡면넓이<sub>surface area</sub>*는

$$\iint_D \lvert \mathbf{r}_u \times \mathbf{r}_v\rvert dudv$$

이고, 면적원소를 $$dS = \lvert \mathbf{r}_u \times \mathbf{r}_v\rvert dudv$$로 적는다.
:::

면적원소 $$dS$$는 다중적분의 야코비 행렬식이 넓이의 국소 확대율이던 것과 같은 역할을 하되, 평면에서 평면이 아니라 평면에서 곡면으로 가므로 행렬식 대신 교차곱의 크기가 들어간다. 이 $$dS$$로 곡면 위에 분포한 스칼라량을 적분한다.

::: 정의 3
곡면 $$S$$ 위에서 연속인 스칼라장 $$f$$의 *면적분*은

$$\iint_S fdS = \iint_D f(\mathbf{r}(u,v))\lvert \mathbf{r}_u \times \mathbf{r}_v\rvert dudv$$

이다.
:::

선적분이 호장 원소로 적분하여 곡선의 매개화에 무관했듯, 면적분도 면적원소로 적분하여 곡면의 매개화에 무관하다. $$f \equiv 1$$이면 곡면넓이이고, $$f$$가 면밀도이면 곡면의 질량이다.

## 선속

곡면을 가로지르는 흐름을 재려면 곡면의 어느 쪽이 "바깥"인지를 정해야 한다. 곡면의 각 점에서 두 단위법선 $$\pm \mathbf{N}/\lvert \mathbf{N}\rvert$$ 중 하나를 연속적으로 고르는 것을 곡면의 *방향<sub>orientation</sub>*이라 한다.

::: 정의 4
단위법선 $$\mathbf{n}$$으로 방향지은 곡면 $$S$$ 위의 연속 벡터장 $$\mathbf{F}$$의 *선속<sub>flux</sub>*은

$$\iint_S \mathbf{F} \cdot d\mathbf{S} = \iint_S \mathbf{F} \cdot \mathbf{n}dS = \iint_D \mathbf{F}(\mathbf{r}(u,v)) \cdot (\mathbf{r}_u \times \mathbf{r}_v)dudv$$

이다. 여기서 $$\mathbf{n} = (\mathbf{r}_u \times \mathbf{r}_v)/\lvert \mathbf{r}_u \times \mathbf{r}_v\rvert$$가 곡면의 방향과 맞는다고 본다.
:::

선속은 단위시간에 곡면을 가로질러 흐르는 양이다. $$\mathbf{F}$$가 유체의 (밀도 곱하기) 속도이면 $$\iint_S \mathbf{F}\cdot d\mathbf{S}$$는 곡면을 통과하는 질량유량이고, 법선 성분 $$\mathbf{F}\cdot \mathbf{n}$$만이 흐름에 기여하며 곡면에 접하는 성분은 가로지르지 않는다. 방향을 반대로 잡으면 $$\mathbf{n}$$이 뒤집혀 선속의 부호가 바뀐다.

::: 예시 5 (구의 넓이)
반지름 $$R$$인 구를 구면좌표로 $$\mathbf{r}(\phi, \theta) = (R\sin\phi\cos\theta, R\sin\phi\sin\theta, R\cos\phi)$$ ($$0 \leq \phi \leq \pi$$, $$0 \leq \theta \leq 2\pi$$)로 매개화한다. 접벡터의 교차곱을 계산하면 그 크기는 $$\lvert \mathbf{r}_\phi \times \mathbf{r}_\theta\rvert = R^2\sin\phi$$이다. 따라서 곡면넓이는

$$\iint_S dS = \int_0^{2\pi} \int_0^\pi R^2\sin\phi d\phi d\theta = R^2 \cdot 2\pi \cdot 2 = 4\pi R^2$$

으로 익숙한 값이 나온다.
:::

::: 예시 6 (지름장의 선속)
위 구의 바깥 방향에 대해 $$\mathbf{F}(x,y,z) = (x,y,z)$$의 선속을 구하자. 구면 매개화에서 $$\mathbf{r}_\phi \times \mathbf{r}_\theta = R\sin\phi \mathbf{r}$$ (바깥 지름 방향)이고 $$\mathbf{F}(\mathbf{r}) = \mathbf{r}$$이므로 $$\mathbf{F}\cdot(\mathbf{r}_\phi\times \mathbf{r}_\theta) = \mathbf{r} \cdot R\sin\phi \mathbf{r} = R\sin\phi\lvert \mathbf{r}\rvert^2 = R^3\sin\phi$$이다. 그러므로

$$\iint_S \mathbf{F}\cdot d\mathbf{S} = \int_0^{2\pi} \int_0^\pi R^3\sin\phi d\phi d\theta = 4\pi R^3$$

이다. 이 값이 공의 부피 $$4\pi R^3/3$$의 세 배인 것은 우연이 아니다. $$\operatorname{div} \mathbf{F} = 3$$이라 부피에 $$3$$을 곱한 것이 흘러나가는 총량이라는 발산정리의 예고이다.
:::
