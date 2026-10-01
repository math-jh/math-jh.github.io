---
title: "The Divergence Theorem and Stokes' Theorem"
description: "We cover two integral theorems that generalize Green's theorem to space. We prove the divergence theorem, which relates the flux of a closed surface to the divergence integral of a solid, and Stokes' theorem, which relates the circulation of a boundary curve to the curl integral of a surface, and examine the conservativeness of irrotational vector fields and unification into differential forms."
excerpt: "Divergence theorem, Stokes' theorem, irrotational and conservative fields, unification of integral theorems"

categories: [Math / Calculus]
permalink: /en/math/calculus/divergence_and_stokes
sidebar: 
    nav: "calculus-en"

date: 2026-07-07
weight: 20
translated_at: 2026-08-19T12:15:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-01T15:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
We introduced Green's theorem and observed that it is a two-dimensional analogue of the fundamental theorem of calculus. The culmination of calculus is to extend this to higher dimensions; the spirit they share is again that the integral over the interior of a region is linked to the integral over its boundary.

## Divergence Theorem

We first present the divergence theorem. This is a theorem on integrals over a region bounded by a $2$-dimensional boundary in $3$-dimensional space.

::: Theorem 1 (Divergence theorem)
If $E$ is a solid region in space bounded by a piecewise smooth closed surface $\partial E$, and $\mathbf{F}$ is, on an open set containing $E$, a $C^1$ vector field, then with $\partial E$ oriented outward,

$$\iint_{\partial E} \mathbf{F} \cdot d\mathbf{S} = \iiint_E \divergence \mathbf{F}\dd{V}$$

holds.
:::

::: Proof
Write $\mathbf{F} = (P, Q, R)$. If for the $z$-component we show

$$\iint_{\partial E} (0,0,R)\cdot d\mathbf{S} = \iiint_E \partial R/\partial z\dd{V}$$

then $P, Q$ are also treated symmetrically, and adding the three yields the theorem.

Suppose $E$ is a solid simple in all three coordinate directions; in particular, in the $z$-direction let $E = \{(x,y,z) \mid (x,y) \in D,\ u_1(x,y) \leq z \leq u_2(x,y)\}$. For the right-hand triple integral, integrating $z$ first by [§Multiple Integrals, ⁋Theorem 2](/en/math/calculus/multiple_integrals#thm2){: data-lid="sybwn" } gives

$$\iiint_E \frac{\partial R}{\partial z}\dd{V} = \iint_D \bigl(R(x,y,u_2) - R(x,y,u_1)\bigr)\dd{A}$$

On the other hand, $\partial E$ consists of the top face $z = u_2$, the bottom face $z = u_1$, and the side faces. On the side faces, the outward normal is horizontal, so $(0,0,R)\cdot \mathbf{n} = 0$ and there is no contribution. The top face has its outward normal pointing upward, giving flux $+\iint_D R(x,y,u_2)\dd{A}$, and the bottom face points downward, giving $-\iint_D R(x,y,u_1)\dd{A}$; their sum equals the double integral above. For a general solid, cutting it into such pieces and adding them causes the flux across interior boundary faces to cancel, since they appear twice with opposite orientations, so the theorem holds.
:::

The divergence theorem states that the amount flowing out through a closed surface equals the total amount $\divergence \mathbf{F}$ welling up inside. Thus the intuition that divergence is "outflow per unit volume" is established as a theorem. It is also practical in that flux over a closed surface can be computed by a volume integral instead of integrating over the surface directly.

::: Example 2 (Reduction of flux to a volume integral)
In [§Surface Integrals and Flux, ⁋Example 6](/en/math/calculus/surface_integrals#ex6){: data-lid="1di1u" }, for a sphere of radius $R$, we directly computed the flux of $\mathbf{F} = (x,y,z)$ by a surface integral and obtained $4\pi R^3$. By the divergence theorem, since $\divergence \mathbf{F} = 3$,

$$\iint_{\partial E} \mathbf{F}\cdot d\mathbf{S} = \iiint_E 3\dd{V} = 3\cdot\frac{4}{3}\pi R^3 = 4\pi R^3$$

which gives the same value.
:::

## Stokes' Theorem

Stokes' theorem is almost the same as Green's theorem; as this is in fact essentially a theorem about integrals where a $1$-dimensional boundary encloses a $2$-dimensional region, it is merely a modification of Green's theorem so that it works even when the region of integration is *curved* inside $3$-dimensional space.

::: Theorem 3 (Stokes)
If $S$ is a piecewise smooth oriented surface, its boundary $\partial S$ is a piecewise smooth simple closed curve, and $\mathbf{F}$ on an open set containing $S$ is $C^1$, then when choosing $\partial S$ compatibly with the orientation of $S$ (with the surface to the left),

$$\oint_{\partial S} \mathbf{F} \cdot d\mathbf{r} = \iint_S \curl \mathbf{F} \cdot d\mathbf{S}$$

holds.
:::

::: Proof
If we show the case where $S$ is the upward-oriented graph of a $C^2$ function $g$, $z = g(x,y)$, a general surface can then be handled by cutting it into such pieces and verifying that interior boundaries cancel. Therefore, let us treat only this special case. First, on the boundary, since $z = g(x,y)$, we have $\dd{z} = g_x\dd{x} + g_y\dd{y}$, so

$$\oint_{\partial S} \mathbf{F}\cdot d\mathbf{r} = \oint_{\partial D} P\dd{x} + Q\dd{y} + R\dd{z} = \oint_{\partial D} (P + R g_x)\dd{x} + (Q + R g_y)\dd{y}$$

and applying [§Green's Theorem, ⁋Theorem 1](/en/math/calculus/greens_theorem#thm1){: data-lid="yxboh" } to the planar region $D$, this is equal to

$$\iint_D \bigl[\partial_x(Q + R g_y) - \partial_y(P + R g_x)\bigr]\dd{A}$$

Taking care only that $P, Q, R$ are evaluated at $(x, y, g(x,y))$ and differentiating by the chain rule, the terms $R g_{xy}$ and $R g_{yx}$ cancel by [§Functions of Several Variables and Partial Derivatives, ⁋Theorem 7](/en/math/calculus/partial_derivatives#thm7){: data-lid="f0u7b" }, and simplifying using this yields the integrand

$$(Q_x - P_y) + (Q_z - R_y)g_x + (R_x - P_z)g_y$$

On the other hand, the upward normal of the graph is $\mathbf{N} = (-g_x, -g_y, 1)$ and $\curl \mathbf{F} = (R_y - Q_z,\ P_z - R_x,\ Q_x - P_y)$, so $\curl \mathbf{F} \cdot \mathbf{N}$ is exactly this expression. Hence the above double integral equals

$$\iint_D \curl \mathbf{F}\cdot \mathbf{N}\dd{A} = \iint_S \curl \mathbf{F}\cdot d\mathbf{S}$$
:::

As in the plane, the following also holds.

::: Corollary 4
In a simply connected open region $D \subseteq \mathbb{R}^3$, if a $C^1$ vector field $\mathbf{F}$ is irrotational ($\curl \mathbf{F} = 0$), then $\mathbf{F}$ is conservative.
:::

::: Proof
Since $D$ is simply connected, in $D$, any closed curve $C$ can be filled by a surface in $D$, $S$, as its boundary. By Stokes' theorem,

$$\oint_C \mathbf{F}\cdot d\mathbf{r} = \iint_S \curl \mathbf{F}\cdot d\mathbf{S} = 0$$

and since the integral over every closed curve is $0$, $\mathbf{F}$ is conservative by [§Line Integrals, ⁋Theorem 4](/en/math/calculus/line_integrals#thm4){: data-lid="r4tpr" }.
:::

::: Example 5
Let us find the circulation of the vector field $\mathbf{F} = (-y, x, z)$ along the unit circle

$$C\colon \mathbf{r}(t) = (\cos t, \sin t, 0)$$

We have $\curl \mathbf{F} = (0, 0, 2)$, and if we choose, as a surface with boundary $C$, the unit disk in the $xy$-plane, $S$ (with upward normal $\mathbf{k}$), Stokes' theorem gives

$$\oint_C \mathbf{F}\cdot d\mathbf{r} = \iint_S \curl \mathbf{F}\cdot d\mathbf{S} = \iint_S 2\dd{A} = 2\pi$$

Even calculating directly without using Stokes' theorem,

$$\mathbf{F}(\mathbf{r}(t))\cdot \mathbf{r}'(t) = (-\sin t, \cos t, 0)\cdot(-\sin t, \cos t, 0) = 1$$

so the value of the integral agrees at $\oint_C = \int_0^{2\pi} \dd{t} = 2\pi$, and one can also verify that choosing another surface sharing the boundary, say a hemisphere, does not change the value of the integral.
:::

---

**References**

**[Ste]** J. Stewart, *Calculus*, 8th ed., Cengage Learning, 2016.  
**[Kim]** 김홍종, *미적분학 1·2*, 제3개정판, 서울대학교출판문화원, 2020.
