---
title: "Divergence Theorem and Stokes' Theorem"
description: "This post covers two integral theorems that generalize Green's theorem to three dimensions. It proves the divergence theorem, which relates flux through a closed surface to a volume integral of divergence, and Stokes' theorem, which connects circulation around a boundary curve to a surface integral of curl. It also examines the conservative property of irrotational vector fields and their unification through differential forms."
excerpt: "Divergence theorem, Stokes' theorem, irrotational and conservative fields, unification of integral theorems"

categories: [Math / Calculus]
permalink: /en/math/calculus/divergence_and_stokes
sidebar: 
    nav: "calculus-en"

date: 2026-07-07
weight: 20
translated_at: 2026-07-12T00:00:01+00:00
translation_source: kimi-cli
last_polished_at: 2026-07-12T00:00:01+00:00
---
We introduced Green's theorem and saw that it is a two-dimensional analogue of the fundamental theorem of calculus. The culmination of calculus is to generalize this to higher dimensions, and the spirit shared by all of them is the connection between the integral over a region and the integral over its boundary.

## Divergence Theorem

First we prove the divergence theorem. This is a theorem about the integral over a three-dimensional space bounded by a two-dimensional boundary.

::: Theorem 1 (Divergence theorem)
If $$E$$ is a solid in space bounded by a piecewise smooth closed surface $$\partial E$$ and $$\mathbf{F}$$ is a $$C^1$$ vector field on an open set containing $$E$$, then taking $$\partial E$$ with the outward orientation,

$$\iint_{\partial E} \mathbf{F} \cdot d\mathbf{S} = \iiint_E \divergence \mathbf{F}\mathop{dV}$$

holds.
:::

::: Proof
Write $$\mathbf{F} = (P, Q, R)$$ and show for the $$z$$-component that

$$\iint_{\partial E} (0,0,R)\cdot d\mathbf{S} = \iiint_E \partial R/\partial z\mathop{dV}$$

then $$P$$ and $$Q$$ are handled symmetrically and adding the three gives the theorem.

Suppose $$E$$ is a solid simple in the $$z$$-direction, that is, $$E = \{(x,y) \in D,\ u_1(x,y) \leq z \leq u_2(x,y)\}$$. The right-hand triple integral, integrating $$z$$ first by [§Multiple Integrals, ⁋Theorem 2](/en/math/calculus/multiple_integrals#thm2), is

$$\iiint_E \frac{\partial R}{\partial z}dV = \iint_D \bigl(R(x,y,u_2) - R(x,y,u_1)\bigr)\mathop{dA}$$

On the other hand, $$\partial E$$ consists of the top face $$z = u_2$$, the bottom face $$z = u_1$$, and the side faces; on the side faces the outward normal is horizontal, so $$(0,0,R)\cdot \mathbf{n} = 0$$ and there is no contribution. The top face has outward normal pointing upward, giving flux $$+\iint_D R(x,y,u_2)\mathop{dA}$$, and the bottom face points downward, giving $$-\iint_D R(x,y,u_1)\mathop{dA}$$, so their sum equals the double integral above. For a general solid, cutting it into such pieces and summing causes the fluxes over internal boundary faces to cancel because they appear twice with opposite orientations, so the theorem holds.
:::

The divergence theorem says that the amount flowing out through a closed surface equals the total amount produced inside by $$\divergence \mathbf{F}$$. This confirms rigorously the intuition that divergence is "the amount flowing out per unit volume." It is also practical in that flux over a closed surface can be computed by a volume integral instead of integrating over the surface directly.

::: Example 2 (Reducing flux to a volume integral)
In [§Surface Integrals and Flux, ⁋Example 6](/en/math/calculus/surface_integrals#ex6) we directly computed the flux of $$\mathbf{F} = (x,y,z)$$ through a sphere of radius $$R$$ by a surface integral and obtained $$4\pi R^3$$. By the divergence theorem, since $$\divergence \mathbf{F} = 3$$,

$$\iint_{\partial E} \mathbf{F}\cdot d\mathbf{S} = \iiint_E 3\mathop{dV} = 3\cdot\frac{4}{3}\pi R^3 = 4\pi R^3$$

gives the same value.
:::

## Stokes' Theorem

Stokes' theorem is almost the same thing as Green's theorem; in fact, since it is essentially a theorem about the integral over a two-dimensional region bounded by a one-dimensional boundary, it is merely a modification of Green's theorem so that it still works when the region of integration is <em-ko>curved</em-ko> inside three-dimensional space.

::: Theorem 3 (Stokes)
If $$S$$ is an oriented piecewise smooth surface with boundary curve $$\partial S$$ and $$\mathbf{F}$$ is $$C^1$$ on an open set containing $$S$$, then taking $$\partial S$$ oriented consistently with $$S$$ (with the surface on the left),

$$\oint_{\partial S} \mathbf{F} \cdot d\mathbf{r} = \iint_S \curl \mathbf{F} \cdot d\mathbf{S}$$

holds.
:::

::: Proof
It suffices to show the case where $$S$$ is an upward-oriented graph $$z = g(x,y)$$; a general surface is then handled by cutting it into such pieces and verifying that internal boundaries cancel. So let us consider only this special case. First, on the boundary we have $$z = g(x,y)$$, so $$dz = g_x\mathop{dx} + g_y\mathop{dy}$$, hence

$$\oint_{\partial S} \mathbf{F}\cdot d\mathbf{r} = \oint_{\partial D} P\mathop{dx} + Q\mathop{dy} + R\mathop{dz} = \oint_{\partial D} (P + R g_x)\mathop{dx} + (Q + R g_y)\mathop{dy}$$

and applying [§Green's Theorem, ⁋Theorem 1](/en/math/calculus/greens_theorem#thm1) to the planar region $$D$$, this equals

$$\iint_D \bigl[\partial_x(Q + R g_y) - \partial_y(P + R g_x)\bigr]\mathop{dA}$$

Noting only that $$P, Q, R$$ are evaluated at $$(x, y, g(x,y))$$ and differentiating by the chain rule, the $$R g_{xy}$$ and $$R g_{yx}$$ terms cancel by [§Multivariable Functions and Partial Derivatives, ⁋Theorem 7](/en/math/calculus/partial_derivatives#thm7), and simplifying using this, the integrand becomes

$$(Q_x - P_y) + (Q_z - R_y)g_x + (R_x - P_z)g_y$$

On the other hand, the upward normal of the graph is $$\mathbf{N} = (-g_x, -g_y, 1)$$ and $$\curl \mathbf{F} = (R_y - Q_z,\ P_z - R_x,\ Q_x - P_y)$$, so $$\curl \mathbf{F} \cdot \mathbf{N}$$ is exactly this same expression. Therefore the double integral above is

$$\iint_D \curl \mathbf{F}\cdot \mathbf{N}\mathop{dA} = \iint_S \curl \mathbf{F}\cdot d\mathbf{S}$$

as claimed.
:::

The following also holds, just as in the plane.

::: Corollary 4
In a simply connected open region $$D \subseteq \mathbb{R}^3$$, if a $$C^1$$ vector field $$\mathbf{F}$$ is irrotational ($$\curl \mathbf{F} = 0$$), then $$\mathbf{F}$$ is conservative.
:::

::: Proof
Since $$D$$ is simply connected, any closed curve $$C$$ in $$D$$ can be filled by a surface $$S$$ in $$D$$ having $$C$$ as its boundary. By Stokes' theorem,

$$\oint_C \mathbf{F}\cdot d\mathbf{r} = \iint_S \curl \mathbf{F}\cdot d\mathbf{S} = 0$$

and since the integral is zero over every closed curve, $$\mathbf{F}$$ is conservative by [§Line Integrals, ⁋Theorem 4](/en/math/calculus/line_integrals#thm4).
:::

::: Example 5
Let us find the circulation of the vector field $$\mathbf{F} = (-y, x, z)$$ around the unit circle

$$C\colon \mathbf{r}(t) = (\cos t, \sin t, 0)$$

We have $$\curl \mathbf{F} = (0, 0, 2)$$, and choosing as the surface with boundary $$C$$ the unit disk $$S$$ in the $$xy$$-plane (with upward normal $$\mathbf{k}$$), Stokes' theorem gives

$$\oint_C \mathbf{F}\cdot d\mathbf{r} = \iint_S \curl \mathbf{F}\cdot d\mathbf{S} = \iint_S 2\mathop{dA} = 2\pi$$

Even without using Stokes' theorem, direct computation yields

$$\mathbf{F}(\mathbf{r}(t))\cdot \mathbf{r}'(t) = (-\sin t, \cos t, 0)\cdot(-\sin t, \cos t, 0) = 1$$

so the integral is $$\oint_C = \int_0^{2\pi} dt = 2\pi$$, agreeing with the above, and one can check that choosing a different surface sharing the same boundary, such as a hemisphere, does not change the value.

:::
