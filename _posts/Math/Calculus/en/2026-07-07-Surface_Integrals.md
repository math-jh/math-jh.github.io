---
title: "Surface Integrals and Flux"
description: "This post introduces parametric surfaces described by two parameters and the normal vector given by the cross product of tangent vectors. It defines surface area and scalar surface integrals, then introduces the orientation of a surface and the flux of a vector field, with an explicit calculation over a sphere."
excerpt: "Parametric surfaces, normal vectors, surface area, scalar surface integrals, flux"

categories: [Math / Calculus]
permalink: /en/math/calculus/surface_integrals
sidebar: 
    nav: "calculus-en"

date: 2026-07-07
weight: 19
translated_at: 2026-07-07T10:00:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-07-07T10:00:02+00:00
---
Now we define the integral over a surface by adding one more variable to the line integral.

## Parametrized Surface

::: Definition 1
A $$C^1$$ map defined on a planar region $$D$$

$$\mathbf{r}\colon D \to \mathbb{R}^3$$, $$\mathbf{r}(u, v) = (x(u,v), y(u,v), z(u,v))$$

is called a *parametrized surface*.
:::


If we fix $$u$$ and vary only $$v$$, a curve is traced on the surface and its tangent is $$\mathbf{r}_v$$; likewise $$\mathbf{r}_u$$ is the tangent of a curve on the surface. The plane spanned by the two tangent vectors is the tangent plane, and $$\mathbf{r}_u \times \mathbf{r}_v$$, which is perpendicular to it, gives the normal direction. That is, the partial derivative vectors $$\mathbf{r}_u = \partial \mathbf{r}/\partial u$$ and $$\mathbf{r}_v = \partial \mathbf{r}/\partial v$$ are tangent to the surface, and their cross product

$$\mathbf{N} = \mathbf{r}_u \times \mathbf{r}_v$$

is the normal vector of the surface. We call a surface with $$\mathbf{N} \neq 0$$ *regular*.

## Surface Area

If we divide the surface into small rectangles of the parameter domain, each piece is approximated by a small parallelogram on the tangent plane, or more specifically, the parallelogram formed by $$\mathbf{r}_u\Delta u$$ and $$\mathbf{r}_v\Delta v$$. Since its area is $$\lvert \mathbf{r}_u \times \mathbf{r}_v\rvert\Delta u\Delta v$$, taking the limit of the sum of these gives the surface area.

::: Definition 2
The *surface area* of a regular parametrized surface $$\mathbf{r}\colon D \to \mathbb{R}^3$$ is

$$\iint_D \lvert \mathbf{r}_u \times \mathbf{r}_v\rvert \mathop{du}\mathop{dv}$$

and we write the area element as $$dS = \lvert \mathbf{r}_u \times \mathbf{r}_v\rvert \mathop{du}\mathop{dv}$$.
:::

The area element $$dS$$ plays the same role as the Jacobian determinant in multiple integrals, and with this area element $$dS$$ we can integrate a scalar quantity distributed over the surface.

::: Definition 3
The *surface integral* of a continuous scalar field $$f$$ on a surface $$S$$ is

$$\iint_S f\mathop{dS} = \iint_D f(\mathbf{r}(u,v))\lvert \mathbf{r}_u \times \mathbf{r}_v\rvert \mathop{du}\mathop{dv}$$

.

Just as the line integral was independent of the parametrization of the curve by integrating with respect to arc length, the surface integral is also independent of the parametrization of the surface by integrating with respect to the area element.

## Flux

On the other hand, we can also consider integrating a vector function over a surface, rather than a scalar function. For this, as in the previous post, we must decide which side of the surface is the "outside." In the case of a surface, a continuous choice of one of the two unit normals $$\pm \mathbf{N}/\lvert \mathbf{N}\rvert$$ at each point is called an *orientation* of the surface.

::: Definition 4
The *flux* of a continuous vector field $$\mathbf{F}$$ on a surface $$S$$ with orientation given by a unit normal $$\mathbf{n}$$ is

$$\iint_S \mathbf{F} \cdot d\mathbf{S} = \iint_S \mathbf{F} \cdot \mathbf{n}\mathop{dS} = \iint_D \mathbf{F}(\mathbf{r}(u,v)) \cdot (\mathbf{r}_u \times \mathbf{r}_v)\mathop{du}\mathop{dv}$$

. Here we assume that $$\mathbf{n} = (\mathbf{r}_u \times \mathbf{r}_v)/\lvert \mathbf{r}_u \times \mathbf{r}_v\rvert$$ matches the orientation of the surface.
:::

Flux is the amount flowing across the surface per unit time. For example, if $$\mathbf{F}$$ is the velocity of a fluid, then $$\iint_S \mathbf{F}\cdot d\mathbf{S}$$ can be thought of as the amount of fluid passing through the surface. Then it is intuitively obvious that only the normal component $$\mathbf{F}\cdot \mathbf{n}$$ contributes to the flow while the component tangent to the surface does not contribute to this quantity, and it is also easy to check that if the direction is reversed, $$\mathbf{n}$$ is flipped and the sign of the flux changes.

The following are two examples of this integral.

::: Example 5 (Surface area of a sphere)
Parametrize a sphere of radius $$R$$ by spherical coordinates

$$\mathbf{r}(\phi, \theta) = (R\sin\phi\cos\theta, R\sin\phi\sin\theta, R\cos\phi),\qquad 0 \leq \phi \leq \pi,\quad 0 \leq \theta \leq 2\pi$$

. Computing the cross product of the tangent vectors, its magnitude is

$$\lvert \mathbf{r}_\phi \times \mathbf{r}_\theta\rvert = R^2\sin\phi$$

and therefore the surface area is

$$\iint_S \mathop{dS} = \int_0^{2\pi} \int_0^\pi R^2\sin\phi \mathop{d\phi} \mathop{d\theta} = R^2 \cdot 2\pi \cdot 2 = 4\pi R^2$$

which gives the familiar value.
:::

The following is an example of the integral of a vector function.

::: Example 6
On the sphere of [Example 5](#ex5), give the outward orientation. In this example our goal is to find the flux of

$$\mathbf{F}(x,y,z) = (x,y,z)$$

. Similarly, from the spherical parametrization

$$\mathbf{r}_\phi \times \mathbf{r}_\theta = R(\sin\phi) \mathbf{r}$$

and since $$\mathbf{F}(\mathbf{r}) = \mathbf{r}$$,

$$\mathbf{F}\cdot(\mathbf{r}_\phi\times \mathbf{r}_\theta) = \mathbf{r} \cdot R\sin\phi \mathbf{r} = R\sin\phi\lvert \mathbf{r}\rvert^2 = R^3\sin\phi$$

. Therefore

$$\iint_S \mathbf{F}\cdot d\mathbf{S} = \int_0^{2\pi} \int_0^\pi R^3\sin\phi \mathop{d\phi} \mathop{d\theta} = 4\pi R^3$$

.
:::
