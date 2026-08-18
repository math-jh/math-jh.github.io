---
title: "The Divergence Theorem and Stokes' Theorem"
description: "This post covers the two integral theorems that generalize Green's theorem to three dimensions. We prove the divergence theorem, which relates flux through a closed surface to a volume integral, and Stokes' theorem, which relates circulation along a boundary curve to a surface integral of curl, and examine the conservativity of irrotational vector fields and their unification via differential forms."
excerpt: "Divergence theorem, Stokes' theorem, irrotational and conservative fields, unification of integral theorems"

categories: [Math / Calculus]
permalink: /en/math/calculus/divergence_and_stokes
sidebar: 
    nav: "calculus-en"

date: 2026-07-07
weight: 20
translated_at: 2026-08-18T00:46:41+00:00
translation_source: kimi-cli
---
We introduced Green's theorem and saw that it is a two-dimensional analogue of the fundamental theorem of calculus. The culmination of calculus is to extend this to higher dimensions, and again the shared spirit is that the integral over the interior of a region is linked to the integral over its boundary.

## Divergence Theorem

First we prove the divergence theorem. This is a theorem about integrals over three-dimensional space bounded by a two-dimensional boundary.

::: Theorem 1 (Divergence theorem)
If $E$ is a solid region in space bounded by a piecewise smooth closed surface $\partial E$, and $\mathbf{F}$ is a $C^1$ vector field on an open set containing $E$, then with $\partial E$ oriented outward,

$$\iint_{\partial E} \mathbf{F} \cdot d\mathbf{S} = \iiint_E \divergence \mathbf{F}\dd{V}$$

holds.
:::

::: Proof
Write $\mathbf{F} = (P, Q, R)$. If we show

$$\iint_{\partial E} (0,0,R)\cdot d\mathbf{S} = \iiint_E \partial R/\partial z\dd{V}$$

for the $z$-component, then $P$ and $Q$ are handled symmetrically, and adding the three gives the theorem.

Suppose $E$ is a solid simple in all three coordinate directions; in particular, in the $z$-direction it is $E = \{(x,y,z) \mid (x,y) \in D,\ u_1(x,y) \leq z \leq u_2(x,y)\}$. The right-hand triple integral, integrating $z$ first by [§Multiple Integrals, ⁋Theorem 2](/en/math/calculus/multiple_integrals#thm2), is

$$\iiint_E \frac{\partial R}{\partial z}\dd{V} = \iint_D \bigl(R(x,y,u_2) - R(x,y,u_1)\bigr)\dd{A}.$$

On the other hand, $\partial E$ consists of the top face $z = u_2$, the bottom face $z = u_1$, and the side faces. On the side faces the outward normal is horizontal, so $(0,0,R)\cdot \mathbf{n} = 0$ and there is no contribution. The top face has outward normal pointing upward, giving flux $+\iint_D R(x,y,u_2)\dd{A}$, and the bottom face points downward, giving $-\iint_D R(x,y,u_1)\dd{A}$; their sum equals the double integral above. For a general solid, cutting it into such pieces and adding them causes the flux across interior boundary faces to cancel, since they appear twice with opposite orientations, so the theorem holds.
:::

The divergence theorem says that the amount flowing out through a closed surface equals the total amount produced inside by $\divergence \mathbf{F}$. Thus the intuition that divergence is "outflow per unit volume" is established as a theorem. It is also practical in that flux over a closed surface can be computed by a volume integral instead of integrating over the surface directly.

::: Example 2 (Reducing flux to a volume integral)
In [§Surface Integrals and Flux, ⁋Example 6](/en/math/calculus/surface_integrals#ex6), we directly computed the flux of $\mathbf{F} = (x,y,z)$ through a sphere of radius $R$ by a surface integral and obtained $4\pi R^3$. By the divergence theorem, since $\divergence \mathbf{F} = 3$,

$$\iint_{\partial E} \mathbf{F}\cdot d\mathbf{S} = \iiint_E 3\dd{V} = 3\cdot\frac{4}{3}\pi R^3 = 4\pi R^3,$$

giving the same value.
:::

## Stokes' Theorem

Stokes' theorem is almost the same as Green's theorem. In essence it is a theorem about integrals over two-dimensional regions bounded by one-dimensional boundaries, so it is merely a modification of Green's theorem to work even when the region of integration is *curved* inside three-dimensional space.

::: Theorem 3 (Stokes)
If $S$ is an oriented piecewise smooth surface whose boundary $\partial S$ is a piecewise smooth simple closed curve, and $\mathbf{F}$ is $C^1$ on an open set containing $S$, then with $\partial S$ oriented compatibly with $S$ (so that the surface lies to the left),

$$\oint_{\partial S} \mathbf{F} \cdot d\mathbf{r} = \iint_S \curl \mathbf{F} \cdot d\mathbf{S}$$

holds.
:::

::: Proof
It suffices to prove the case where $S$ is the graph $z = g(x,y)$ of a $C^2$ function $g$, oriented upward; a general surface is then handled by cutting it into such pieces and verifying that interior boundaries cancel. So let us treat only this special case. First, on the boundary we have $z = g(x,y)$, so $\dd{z} = g_x\dd{x} + g_y\dd{y}$, and therefore

$$\oint_{\partial S} \mathbf{F}\cdot d\mathbf{r} = \oint_{\partial D} P\dd{x} + Q\dd{y} + R\dd{z} = \oint_{\partial D} (P + R g_x)\dd{x} + (Q + R g_y)\dd{y},$$

and applying [§Green's Theorem, ⁋Theorem 1](/en/math/calculus/greens_theorem#thm1) to the planar region $D$ gives

$$\iint_D \bigl[\partial_x(Q + R g_y) - \partial_y(P + R g_x)\bigr]\dd{A}.$$

Noting that $P, Q, R$ are evaluated at $(x, y, g(x,y))$ and differentiating by the chain rule, the terms $R g_{xy}$ and $R g_{yx}$ cancel by [§Functions of Several Variables and Partial Derivatives, ⁋Theorem 7](/en/math/calculus/partial_derivatives#thm7), and simplifying yields the integrand

$$(Q_x - P_y) + (Q_z - R_y)g_x + (R_x - P_z)g_y.$$

On the other hand, the upward normal of the graph is $\mathbf{N} = (-g_x, -g_y, 1)$ and $\curl \mathbf{F} = (R_y - Q_z,\ P_z - R_x,\ Q_x - P_y)$, so $\curl \mathbf{F} \cdot \mathbf{N}$ is exactly this expression. Hence the above double integral equals

$$\iint_D \curl \mathbf{F}\cdot \mathbf{N}\dd{A} = \iint_S \curl \mathbf{F}\cdot d\mathbf{S}.$$
:::

As in the plane, the following also holds.

::: Corollary 4
In a simply connected open region $D \subseteq \mathbb{R}^3$, a $C^1$ vector field $\mathbf{F}$ that is irrotational ($\curl \mathbf{F} = 0$) is conservative.
:::

::: Proof
Since $D$ is simply connected, any closed curve $C$ in $D$ can be filled by a surface $S$ in $D$ whose boundary is $C$. By Stokes' theorem,

$$\oint_C \mathbf{F}\cdot d\mathbf{r} = \iint_S \curl \mathbf{F}\cdot d\mathbf{S} = 0,$$

and since the integral vanishes over every closed curve, $\mathbf{F}$ is conservative by [§Line Integrals, ⁋Theorem 4](/en/math/calculus/line_integrals#thm4).
:::

::: Example 5
Let us compute the circulation of the vector field $\mathbf{F} = (-y, x, z)$ around the unit circle

$$C\colon \mathbf{r}(t) = (\cos t, \sin t, 0).$$

We have $\curl \mathbf{F} = (0, 0, 2)$. Choosing the unit disk $S$ in the $xy$-plane (with upward normal $\mathbf{k}$) as the surface with boundary $C$, Stokes' theorem gives

$$\oint_C \mathbf{F}\cdot d\mathbf{r} = \iint_S \curl \mathbf{F}\cdot d\mathbf{S} = \iint_S 2\dd{A} = 2\pi.$$

Even without using Stokes' theorem, direct computation yields

$$\mathbf{F}(\mathbf{r}(t))\cdot \mathbf{r}'(t) = (-\sin t, \cos t, 0)\cdot(-\sin t, \cos t, 0) = 1,$$

so the integral is $\oint_C = \int_0^{2\pi} \dd{t} = 2\pi$, agreeing with the above. One can also verify that choosing another surface with the same boundary, such as a hemisphere, does not change the value of the integral.
:::

---

**References**

**[Ste]** J. Stewart, *Calculus*, 8th ed., Cengage Learning, 2016.  
**[Kim]** 김홍종, *미적분학 1·2*, 제3개정판, 서울대학교출판문화원, 2020.
