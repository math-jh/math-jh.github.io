---
title: "Green's Theorem"
description: "We prove Green's theorem for simple regions, converting a line integral around a planar boundary into a double integral over the region. We also examine area formulas, the curl and divergence forms, and why irrotational vector fields are conservative on simply connected domains."
excerpt: "Green's theorem, area formulas, curl and divergence, simply connected and conservative fields"

categories: [Math / Calculus]
permalink: /en/math/calculus/greens_theorem
sidebar: 
    nav: "calculus-en"

date: 2026-07-07
weight: 18
translated_at: 2026-07-06T21:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-07-06T21:30:02+00:00
---
The fundamental theorem of calculus and the fundamental theorem of line integrals share a common spirit: what happens inside a region is expressed as an integral over its boundary. This can be seen as the prototype of later theorems such as the divergence theorem and Stokes' theorem, and Green's theorem, which we examine in this post, can be regarded as the two-dimensional version of this spirit.

## Green's Theorem

First, we define the *positive orientation* as the direction along which we traverse the boundary curve $\partial D$ of a planar region $D$ with the region on our left; in other words, the outer boundary is traversed counterclockwise. Then the following holds.

::: Theorem 1 (Green)
If $D$ is a planar region bounded by a piecewise smooth simple closed curve $C = \partial D$ and $P, Q$ are $C^1$ on an open set containing $D$, then when $C$ is taken with positive orientation,

$$\oint_C P\mathop{dx} + Q\mathop{dy} = \iint_D \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right)\mathop{dA}$$

holds.
:::

::: Proof
First, we show the identity

$$\oint_C P\mathop{dx} = -\iint_D \partial P/\partial y\mathop{dA}$$

when $D$ is a region simple with respect to $y$, i.e.,

$$D = \{(x,y) \mid a \leq x \leq b,\ g_1(x) \leq y \leq g_2(x)\}.$$

For the double integral, integrating the inner integral first by [§Multiple Integrals, ⁋Theorem 2](/en/math/calculus/multiple_integrals#thm2) gives

$$\iint_D \frac{\partial P}{\partial y}\mathop{dA} = \int_a^b \bigl(P(x, g_2(x)) - P(x, g_1(x))\bigr)\mathop{dx}.$$

On the other hand, the boundary $C$ consists of two pieces: the lower curve $y = g_1(x)$ traversed with $x\colon a \rightarrow b$, and the upper curve $y = g_2(x)$ traversed with $x\colon b \rightarrow a$, and on the two vertical sides $x$ is constant so $dx = 0$. Hence

$$\oint_C P\mathop{dx} = \int_a^b P(x, g_1(x))\mathop{dx} + \int_b^a P(x, g_2(x))\mathop{dx} = -\int_a^b \bigl(P(x,g_2) - P(x,g_1)\bigr)\mathop{dx},$$

and comparing the two identities yields

$$\oint_C P\mathop{dx} = -\iint_D \partial P/\partial y\mathop{dA}.$$

Symmetrically, if $D$ is a region simple with respect to $x$, then

$$\oint_C Q\mathop{dy} = \iint_D \partial Q/\partial x\mathop{dA}.$$

For a general region, cutting it into such pieces and combining them causes the integrals over interior boundaries to cancel as two integrals in opposite directions, so the theorem holds.
:::

In particular, choosing $P, Q$ so that the integrand of the double integral becomes $1$, we can compute the area of a region by a line integral over its boundary.

::: Corollary 2
The area of $D$ is given by the boundary integral

$$\area(D) = \oint_C x\mathop{dy} = -\oint_C y\mathop{dx} = \frac{1}{2}\oint_C (x\mathop{dy} - y\mathop{dx}).$$
:::

::: Proof
In [Theorem 1](#thm1), taking $(P, Q) = (0, x)$ gives $Q_x - P_y = 1$, so

$$\oint_C x\mathop{dy} = \iint_D 1\mathop{dA} = \area(D),$$

and taking $(P, Q) = (-y, 0)$ gives

$$\oint_C -y\mathop{dx} = \area(D).$$

The third formula is the average of these two.
:::

Meanwhile, Green's theorem can be rewritten in two forms that interpret the two differential quantities of a planar vector field $\mathbf{F} = (P, Q)$ as boundary integrals.

::: Proposition 3
If the boundary $C$ of $D$ is positively oriented and $\mathbf{F} = (P, Q)$ is $C^1$, then for the unit tangent $\mathbf{T}$ and the outward unit normal $\mathbf{n}$,

$$\oint_C \mathbf{F} \cdot \mathbf{T}\mathop{ds} = \iint_D \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right)\mathop{dA}, \qquad \oint_C \mathbf{F} \cdot \mathbf{n}\mathop{ds} = \iint_D \divergence F\mathop{dA}$$

hold.
:::

::: Proof
The first equality follows because

$$\oint_C \mathbf{F}\cdot \mathbf{T}\mathop{ds} = \oint_C P\mathop{dx} + Q\mathop{dy}$$

is exactly the left-hand side of [Theorem 1](#thm1), and the integrand $Q_x - P_y$ on the right-hand side is the curl of the planar vector field ([§Vector Fields, ⁋Definition 3](/en/math/calculus/vector_fields#def3)).

For the second equality, using that on a positively oriented boundary the outward unit normal satisfies $\mathbf{n}ds = (dy, -dx)$, we have

$$\oint_C \mathbf{F}\cdot \mathbf{n}\mathop{ds} = \oint_C P\mathop{dy} - Q\mathop{dx},$$

and applying [Theorem 1](#thm1) to $(P, Q) \mapsto (-Q, P)$ shows this equals

$$\iint_D (P_x + Q_y)\mathop{dA} = \iint_D \divergence F\mathop{dA}.$$
:::

The first equality is exactly Green's theorem itself, and only the second equality is new, but its intuitive meaning is clear. Namely, if we integrate the function $\mathbf{F}$ along the boundary in the *outward* direction, this is precisely captured by the divergence. On the other hand, we already saw in [§Line Integrals, ⁋Example 6](/en/math/calculus/line_integrals#ex6) that if a region has a hole, the field may fail to be conservative even when the curl vanishes; this can be written rigorously as follows.

A region being *simply connected* means that any closed curve inside it can be continuously shrunk to a point without leaving the region; intuitively, one may think of it as a region without holes. For example, a disk is simply connected, but a disk with its center removed is not, because to shrink a circle surrounding the center to a point one must pass through the missing center.

::: Corollary 4
On a simply connected open region, a $C^1$ vector field $\mathbf{F} = (P, Q)$ satisfying $\partial Q/\partial x = \partial P/\partial y$ is conservative.
:::

::: Proof
Since the region is simply connected, any simple closed curve $C$ inside it bounds a region $D$ entirely contained in the region. Now

$$\oint_C \mathbf{F}\cdot d\mathbf{r} = \iint_D (Q_x - P_y)\mathop{dA} = 0,$$

and since the integral vanishes over every closed curve, [§Line Integrals, ⁋Theorem 4](/en/math/calculus/line_integrals#thm4) implies that $\mathbf{F}$ is conservative.
:::

::: Example 5 (Simple connectedness)
The vector field

$$\mathbf{F} = (-y, x)/(x^2+y^2)$$

from [§Line Integrals, ⁋Example 6](/en/math/calculus/line_integrals#ex6) is irrotational, but its integral around the unit circle centered at the origin was $2\pi$. By [Corollary 4](#cor4), this makes sense only if the domain on which this vector field is defined is not simply connected, and indeed the domain $\mathbb{R}^2\setminus\{0\}$ is not simply connected. Moreover, on any closed curve not enclosing the origin the integral of $\mathbf{F}$ is $0$, so we can also confirm that the only problematic point is the origin where the vector field is undefined.
:::
