---
title: "Surface Integrals and Flux"
description: "We introduce parametric surfaces described by two parameters and the normal vector given by the cross product of tangent vectors. Surface area and scalar surface integrals are defined, and the orientation of a surface and the flux of a vector field are defined and computed on a sphere."
excerpt: "Parametric surfaces, normal vectors, surface area, scalar surface integrals, flux"

categories: [Math / Calculus]
permalink: /en/math/calculus/surface_integrals
sidebar: 
    nav: "calculus-en"

date: 2026-07-07
weight: 19
translated_at: 2026-07-13T12:30:02+00:00
translation_source: kimi-cli
---
Now we define the surface integral by adding one more variable to the line integral.

## Parametrized Surfaces

::: Definition 1
A $C^1$ map defined on a planar region $D$

$\mathbf{r}\colon D \to \mathbb{R}^3$, $\mathbf{r}(u, v) = (x(u,v), y(u,v), z(u,v))$

is called a *parametrized surface*.
:::


Fixing $u$ and varying $v$ traces a curve on the surface whose tangent is $\mathbf{r}_v$; likewise $\mathbf{r}_u$ is the tangent of another curve on the surface. The plane spanned by the two tangent vectors is the tangent plane, and $\mathbf{r}_u \times \mathbf{r}_v$, perpendicular to it, gives the normal direction. That is, the partial-derivative vectors $\mathbf{r}_u = \partial \mathbf{r}/\partial u$ and $\mathbf{r}_v = \partial \mathbf{r}/\partial v$ are tangent to the surface, and their cross product

$$\mathbf{N} = \mathbf{r}_u \times \mathbf{r}_v$$

is the normal vector of the surface. We call a surface with $\mathbf{N} \neq 0$ *regular*.

## Surface Area

If we chop the surface into small rectangles in the parameter domain, each piece is approximated by a small parallelogram on the tangent plane, specifically the parallelogram spanned by $\mathbf{r}_u\Delta u$ and $\mathbf{r}_v\Delta v$. Since its area is $\lvert \mathbf{r}_u \times \mathbf{r}_v\rvert\Delta u\Delta v$, taking the limit of the sum gives the surface area.

::: Definition 2
The *surface area* of a regular parametrized surface $\mathbf{r}\colon D \to \mathbb{R}^3$ is

$$\iint_D \lvert \mathbf{r}_u \times \mathbf{r}_v\rvert \mathop{du}\mathop{dv}$$

and we write the area element as $dS = \lvert \mathbf{r}_u \times \mathbf{r}_v\rvert \mathop{du}\mathop{dv}$.
:::

The area element $dS$ plays the same role as the Jacobian determinant in multiple integrals, and with this area element $dS$ we can integrate a scalar quantity distributed over the surface.

::: Definition 3
The *surface integral* of a continuous scalar field $f$ on a surface $S$ is

$$\iint_S f\mathop{dS} = \iint_D f(\mathbf{r}(u,v))\lvert \mathbf{r}_u \times \mathbf{r}_v\rvert \mathop{du}\mathop{dv}.$$
:::

Just as a line integral is independent of the curve's parametrization because we integrate with respect to arc length, a surface integral is independent of the surface's parametrization because we integrate with respect to the area element.

## Flux

On the other hand, we can also consider integrating a vector function, rather than a scalar function, over a surface. For this, just as in the previous post, we must decide which side of the surface is "outside." For a surface, an *orientation* is a continuous choice of one of the two unit normals $\pm \mathbf{N}/\lvert \mathbf{N}\rvert$ at each point.

::: Definition 4
The *flux* of a continuous vector field $\mathbf{F}$ on an oriented surface $S$ with unit normal $\mathbf{n}$ is

$$\iint_S \mathbf{F} \cdot d\mathbf{S} = \iint_S \mathbf{F} \cdot \mathbf{n}\mathop{dS} = \iint_D \mathbf{F}(\mathbf{r}(u,v)) \cdot (\mathbf{r}_u \times \mathbf{r}_v)\mathop{du}\mathop{dv}.$$

Here we take $\mathbf{n} = (\mathbf{r}_u \times \mathbf{r}_v)/\lvert \mathbf{r}_u \times \mathbf{r}_v\rvert$ to match the orientation of the surface.
:::

Flux is the amount flowing across the surface per unit time. For example, if $\mathbf{F}$ is the velocity of a fluid, then $\iint_S \mathbf{F}\cdot d\mathbf{S}$ can be thought of as the amount of fluid passing through the surface. It is intuitively obvious that only the normal component $\mathbf{F}\cdot \mathbf{n}$ contributes to the flow while the tangential component does not, and it is easy to check that reversing the orientation flips $\mathbf{n}$ and changes the sign of the flux.

Here are two examples of this integral.

::: Example 5 (Surface area of a sphere)
Parametrize a sphere of radius $R$ by spherical coordinates

$$\mathbf{r}(\phi, \theta) = (R\sin\phi\cos\theta, R\sin\phi\sin\theta, R\cos\phi),\qquad 0 \leq \phi \leq \pi,\quad 0 \leq \theta \leq 2\pi.$$

Computing the cross product of the tangent vectors gives magnitude

$$\lvert \mathbf{r}_\phi \times \mathbf{r}_\theta\rvert = R^2\sin\phi,$$

so the surface area is

$$\iint_S \mathop{dS} = \int_0^{2\pi} \int_0^\pi R^2\sin\phi \mathop{d\phi} \mathop{d\theta} = R^2 \cdot 2\pi \cdot 2 = 4\pi R^2,$$

the familiar value.
:::

Next is an example of integrating a vector function.

::: Example 6
On the sphere of [Example 5](#ex5), give the outward orientation. In this example our goal is to compute the flux of

$$\mathbf{F}(x,y,z) = (x,y,z).$$

Again, from the spherical parametrization

$$\mathbf{r}_\phi \times \mathbf{r}_\theta = R(\sin\phi) \mathbf{r}$$

and $\mathbf{F}(\mathbf{r}) = \mathbf{r}$, so

$$\mathbf{F}\cdot(\mathbf{r}_\phi\times \mathbf{r}_\theta) = \mathbf{r} \cdot R\sin\phi \mathbf{r} = R\sin\phi\lvert \mathbf{r}\rvert^2 = R^3\sin\phi.$$

Therefore

$$\iint_S \mathbf{F}\cdot d\mathbf{S} = \int_0^{2\pi} \int_0^\pi R^3\sin\phi \mathop{d\phi} \mathop{d\theta} = 4\pi R^3.$$
:::
