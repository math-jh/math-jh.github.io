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
translated_at: 2026-08-18T01:46:56+00:00
translation_source: kimi-cli
---
We now define the integral over a surface by adding one more variable to the line integral.

## Parametrized Surfaces

::: Definition 1
A $C^1$ map defined on a planar region $D$

$\mathbf{r}\colon D \rightarrow \mathbb{R}^3$, $\mathbf{r}(u, v) = (x(u,v), y(u,v), z(u,v))$

is called a *parametrized surface*.
:::

If we fix $u$ and vary only $v$, a curve is drawn on the surface and its tangent is $\mathbf{r}_v$; likewise, $\mathbf{r}_u$ is also the tangent of a curve on the surface. The plane spanned by the two tangent vectors is the tangent plane, and $\mathbf{r}_u \times \mathbf{r}_v$, which is perpendicular to it, gives the normal direction. That is, the partial derivative vectors $\mathbf{r}_u = \partial \mathbf{r}/\partial u$ and $\mathbf{r}_v = \partial \mathbf{r}/\partial v$ are tangent to the surface, and their cross product

$$\mathbf{N} = \mathbf{r}_u \times \mathbf{r}_v$$

is the normal vector of the surface. We call a parametrized surface *regular* if $\mathbf{N}(u,v) \neq \mathbf{0}$ for all $(u,v) \in D$.

## Surface Area

If we divide a surface into small rectangles in the parameter domain, each piece is approximated by a small parallelogram on the tangent plane, or more specifically by the parallelogram formed by $\mathbf{r}_u\Delta u$ and $\mathbf{r}_v\Delta v$. Since its area is $\lvert \mathbf{r}_u \times \mathbf{r}_v\rvert\Delta u\Delta v$, the surface area is obtained by summing these and taking the limit.

::: Definition 2
The *surface area* of a regular parametrized surface $\mathbf{r}\colon D \rightarrow \mathbb{R}^3$ is

$$\iint_D \lvert \mathbf{r}_u \times \mathbf{r}_v\rvert \dd{u}\dd{v}$$

and we write the area element as $\dd{S} = \lvert \mathbf{r}_u \times \mathbf{r}_v\rvert \dd{u}\dd{v}$.
:::

The parametrizations we deal with often do not satisfy the regularity condition on the whole of $D$. Even if $\mathbf{N}$ becomes $\mathbf{0}$ at finitely many points and curves, or if different parameters map to the same point, the exceptional set has area $0$ and thus does not contribute to the value of the above double integral. Therefore, when we speak of surface area and surface integrals from now on, we allow parametrizations that are regular and injective except for finitely many points and curves, that is, parametrizations that cover the surface exactly once.

The area element $\dd{S}$ plays the same role as the Jacobian determinant in multiple integrals, and with this definition of $\dd{S}$ we can integrate a scalar quantity distributed over the surface.

::: Definition 3
The *surface integral* of a continuous scalar field $f$ on the image $S = \mathbf{r}(D)$ of a regular parametrized surface $\mathbf{r}\colon D \rightarrow \mathbb{R}^3$ is

$$\iint_S f\dd{S} = \iint_D f(\mathbf{r}(u,v))\lvert \mathbf{r}_u \times \mathbf{r}_v\rvert \dd{u}\dd{v}$$

.
:::

Just as the line integral was independent of the parametrization of the curve because it was integrated with respect to arc length, the surface integral is also independent of the parametrization of the surface because it is integrated using the area element. Indeed, if two parametrized surfaces $\mathbf{r}(u,v)$ and $\tilde{\mathbf{r}}(s,t)$ give the same image and are related by a $C^1$ change of variables $(u,v) \mapsto (s,t)$, then by the chain rule $\mathbf{r}_u \times \mathbf{r}_v = (\partial(s,t)/\partial(u,v))(\tilde{\mathbf{r}}_s \times \tilde{\mathbf{r}}_t)$, so taking absolute values and applying [§Multiple Integrals, ⁋Theorem 4](/en/math/calculus/multiple_integrals#thm4) shows that the double integrals given by the two parametrizations are equal.

## Flux

On the other hand, we can also consider integrating a vector function, rather than a scalar function, over a surface. For this, just as in the previous post, we must decide which side of the surface is "outside." In the case of a surface, an *orientation* is a continuous choice of one of the two unit normals $\pm \mathbf{N}/\lvert \mathbf{N}\rvert$ at each point.

::: Definition 4
The *flux* of a continuous vector field $\mathbf{F}$ on a surface $S$ with orientation given by the unit normal $\mathbf{n}$ is

$$\iint_S \mathbf{F} \cdot d\mathbf{S} = \iint_S \mathbf{F} \cdot \mathbf{n}\dd{S} = \iint_D \mathbf{F}(\mathbf{r}(u,v)) \cdot (\mathbf{r}_u \times \mathbf{r}_v)\dd{u}\dd{v}$$

. Here we assume that $\mathbf{n} = (\mathbf{r}_u \times \mathbf{r}_v)/\lvert \mathbf{r}_u \times \mathbf{r}_v\rvert$ matches the orientation of the surface.
:::

Flux is the amount flowing across the surface per unit time. For example, if $\mathbf{F}$ is the velocity of a fluid, then $\iint_S \mathbf{F}\cdot d\mathbf{S}$ can be thought of as the amount of fluid passing through the surface. It is then intuitively clear that only the normal component $\mathbf{F}\cdot \mathbf{n}$ contributes to the flow, while the component tangent to the surface does not, and it is also easy to check that if the orientation is reversed, $\mathbf{n}$ is flipped and the sign of the flux changes.

Here are two examples of surface integrals.

::: Example 5 (Surface area of a sphere)
Parametrize a sphere of radius $R$ by spherical coordinates

$$\mathbf{r}(\phi, \theta) = (R\sin\phi\cos\theta, R\sin\phi\sin\theta, R\cos\phi),\qquad 0 \leq \phi \leq \pi,\quad 0 \leq \theta \leq 2\pi$$

. Computing the cross product of the tangent vectors, its magnitude is

$$\lvert \mathbf{r}_\phi \times \mathbf{r}_\theta\rvert = R^2\sin\phi$$

and therefore the surface area is

$$\iint_S \dd{S} = \int_0^{2\pi} \int_0^\pi R^2\sin\phi \dd{\phi} \dd{\theta} = R^2 \cdot 2\pi \cdot 2 = 4\pi R^2$$

which gives the familiar value.
:::

The next is an example of the integral of a vector function.

::: Example 6
On the sphere of [Example 5](#ex5), give the outward orientation. Our goal in this example is to find the flux of

$$\mathbf{F}(x,y,z) = (x,y,z)$$

. Similarly, in the spherical parametrization,

$$\mathbf{r}_\phi \times \mathbf{r}_\theta = R(\sin\phi) \mathbf{r}$$

and since $\mathbf{F}(\mathbf{r}) = \mathbf{r}$,

$$\mathbf{F}\cdot(\mathbf{r}_\phi\times \mathbf{r}_\theta) = \mathbf{r} \cdot R\sin\phi \mathbf{r} = R\sin\phi\lvert \mathbf{r}\rvert^2 = R^3\sin\phi$$

. Therefore,

$$\iint_S \mathbf{F}\cdot d\mathbf{S} = \int_0^{2\pi} \int_0^\pi R^3\sin\phi \dd{\phi} \dd{\theta} = 4\pi R^3$$

.
:::

---

**References**

**[Ste]** J. Stewart, *Calculus*, 8th ed., Cengage Learning, 2016.  
**[Kim]** 김홍종, *미적분학 1·2*, 제3개정판, 서울대학교출판문화원, 2020.
