---
title: "Surface Integrals and Flux"
description: "We introduce parametric surfaces described by two parameters and normal vectors given by the cross product of tangent vectors. We define surface area and scalar surface integrals, then define the orientation of a surface and the flux of a vector field, computing it on a sphere."
excerpt: "Parametric surfaces, normal vectors, surface area, scalar surface integrals, flux"

categories: [Math / Calculus]
permalink: /en/math/calculus/surface_integrals
sidebar: 
    nav: "calculus-en"

date: 2026-07-07
weight: 19
translated_at: 2026-08-19T13:15:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-01T23:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
We now define the integral over a surface by adding one variable to the line integral. 

## Parametrized Surfaces

::: Definition 1
On a planar region $D$, a $C^1$ map

$$\mathbf{r}\colon D \rightarrow \mathbb{R}^3$, $\mathbf{r}(u, v) = (x(u,v), y(u,v), z(u,v))$$

is called a *parametrized surface*.
:::

Fixing $u$ and varying only $v$ traces a curve on the surface whose tangent is $\mathbf{r}_v$; likewise, $\mathbf{r}_u$ is also the tangent to a curve on the surface. The plane spanned by these two tangent vectors is the tangent plane, and $\mathbf{r}_u \times \mathbf{r}_v$, being perpendicular to it, gives the normal direction. That is, the partial-derivative vectors $\mathbf{r}_u = \partial \mathbf{r}/\partial u$ and $\mathbf{r}_v = \partial \mathbf{r}/\partial v$ are tangent to the surface, and their cross product

$$\mathbf{N} = \mathbf{r}_u \times \mathbf{r}_v$$

is the normal vector of the surface. We call a parametrized surface *regular* if for all $(u,v) \in D$, $\mathbf{N}(u,v) \neq \mathbf{0}$.

## Surface Area

When the surface is divided into small rectangles in the parameter domain, each piece is approximated by a small parallelogram on the tangent plane, more specifically by the parallelogram formed by $\mathbf{r}_u\Delta u$ and $\mathbf{r}_v\Delta v$. Since this area is $\lvert \mathbf{r}_u \times \mathbf{r}_v\rvert\Delta u\Delta v$, summing these and taking the limit gives the surface area.

::: Definition 2
The *surface area* of a regular parametrized surface $\mathbf{r}\colon D \rightarrow \mathbb{R}^3$ is

$$\iint_D \lvert \mathbf{r}_u \times \mathbf{r}_v\rvert \dd{u}\dd{v}$$

and we write the area element as $\dd{S} = \lvert \mathbf{r}_u \times \mathbf{r}_v\rvert \dd{u}\dd{v}$.
:::

The parametrizations we shall deal with often do not satisfy the condition of being regular on all of $D$. Even if $\mathbf{N}$ becomes $\mathbf{0}$ at finitely many points and curves, or distinct parameters map to the same point, this exceptional set has area $0$ and therefore does not contribute to the value of the double integral above. Hence, when we speak of surface area and surface integrals hereafter, we allow parametrizations that are regular and injective except for finitely many points and curves, that is, parametrizations that cover the surface exactly once.

The area element $\dd{S}$ plays the same role as the Jacobian determinant in multiple integrals, and with the area element $\dd{S}$ defined in this way, we can integrate a scalar quantity distributed over the surface.

::: Definition 3
For a regular parametrized surface $\mathbf{r}\colon D \rightarrow \mathbb{R}^3$, the *surface integral* on the image $S = \mathbf{r}(D)$ of a continuous scalar field $f$ is

$$\iint_S f\dd{S} = \iint_D f(\mathbf{r}(u,v))\lvert \mathbf{r}_u \times \mathbf{r}_v\rvert \dd{u}\dd{v}$$
:::

Just as the line integral was independent of the curve's parametrization because it integrated with respect to the arc length parametrization, the surface integral is independent of the surface's parametrization because it integrates with respect to the area element. Indeed, if two parametrized surfaces $\mathbf{r}(u,v)$ and $\tilde{\mathbf{r}}(s,t)$ give the same image and are connected by a $C^1$ change of variables $(u,v) \mapsto (s,t)$, then by the chain rule $\mathbf{r}_u \times \mathbf{r}_v = (\partial(s,t)/\partial(u,v))(\tilde{\mathbf{r}}_s \times \tilde{\mathbf{r}}_t)$; taking magnitudes and applying [§Multiple Integrals, ⁋Theorem 4](/en/math/calculus/multiple_integrals#thm4){: data-lid="b0fw2" } shows that the two parametrizations yield the same double integral. 

## Flux

Meanwhile, we may also consider the situation where we integrate a vector function, rather than a scalar function, along a surface. For this, just as in the previous post, we must determine which side of the surface is the "outside." In the case of a surface, continuously choosing one of the two unit normals $\pm \mathbf{N}/\lvert \mathbf{N}\rvert$ at each point is called an *orientation* of the surface.

::: Definition 4
Given a unit normal $\mathbf{n}$ orienting a surface $S$, the *flux* of a continuous vector field $\mathbf{F}$ across the surface is

$$\iint_S \mathbf{F} \cdot d\mathbf{S} = \iint_S \mathbf{F} \cdot \mathbf{n}\dd{S} = \iint_D \mathbf{F}(\mathbf{r}(u,v)) \cdot (\mathbf{r}_u \times \mathbf{r}_v)\dd{u}\dd{v}$$

Here, we take $\mathbf{n} = (\mathbf{r}_u \times \mathbf{r}_v)/\lvert \mathbf{r}_u \times \mathbf{r}_v\rvert$ to match the orientation of the surface.
:::

Flux is the amount of flow across a surface per unit time. For instance, if $\mathbf{F}$ is the velocity of a fluid, then $\iint_S \mathbf{F}\cdot d\mathbf{S}$ can be thought of as the amount of fluid passing through the surface. It is then intuitively clear that only the normal component $\mathbf{F}\cdot \mathbf{n}$ contributes to the flow, while the component tangent to the surface does not contribute to this quantity; it is also easy to see that reversing the orientation flips $\mathbf{n}$ and changes the sign of the flux.

The following are two examples of surface integrals.

::: Example 5 (Surface area of a sphere)
Let us parametrize a sphere of radius $R$ by spherical coordinates

$$\mathbf{r}(\phi, \theta) = (R\sin\phi\cos\theta, R\sin\phi\sin\theta, R\cos\phi),\qquad 0 \leq \phi \leq \pi,\quad 0 \leq \theta \leq 2\pi$$

Computing the cross product of the tangent vectors, its magnitude is

$$\lvert \mathbf{r}_\phi \times \mathbf{r}_\theta\rvert = R^2\sin\phi$$

and therefore the surface area is

$$\iint_S \dd{S} = \int_0^{2\pi} \int_0^\pi R^2\sin\phi \dd{\phi} \dd{\theta} = R^2 \cdot 2\pi \cdot 2 = 4\pi R^2$$

which gives the familiar value.
:::

The following is an example of an integral of a vector function.

::: Example 6
Let us give the sphere in [Example 5](#ex5){: data-lid="o78pm" } the outward orientation. In this example, our goal is to compute the flux of

$$\mathbf{F}(x,y,z) = (x,y,z)$$

Similarly, in the spherical parametrization,

$$\mathbf{r}_\phi \times \mathbf{r}_\theta = R(\sin\phi) \mathbf{r}$$

and since $\mathbf{F}(\mathbf{r}) = \mathbf{r}$,

$$\mathbf{F}\cdot(\mathbf{r}_\phi\times \mathbf{r}_\theta) = \mathbf{r} \cdot R\sin\phi \mathbf{r} = R\sin\phi\lvert \mathbf{r}\rvert^2 = R^3\sin\phi$$

Therefore,

$$\iint_S \mathbf{F}\cdot d\mathbf{S} = \int_0^{2\pi} \int_0^\pi R^3\sin\phi \dd{\phi} \dd{\theta} = 4\pi R^3$$
:::

---

**References**

**[Ste]** J. Stewart, *Calculus*, 8th ed., Cengage Learning, 2016.  
**[Kim]** 김홍종, *미적분학 1·2*, 제3개정판, 서울대학교출판문화원, 2020.
