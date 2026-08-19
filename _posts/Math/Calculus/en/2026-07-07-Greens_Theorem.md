---
title: "Green's Theorem"
description: "We prove Green's theorem for simple regions, converting line integrals around a planar boundary into double integrals over the region. We also examine area formulas, the circulation and divergence forms, and show that irrotational vector fields are conservative on simply connected domains."
excerpt: "Green's theorem, area formulas, circulation and flux forms, simply connected domains and conservative fields"

categories: [Math / Calculus]
permalink: /en/math/calculus/greens_theorem
sidebar: 
    nav: "calculus-en"

date: 2026-07-07
weight: 18
translated_at: 2026-08-19T12:45:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-08-19T12:45:04+00:00
---
The fundamental theorem of calculus and the fundamental theorem of line integrals share a common spirit: what happens in the interior of a domain is expressed as an integral over its boundary. This idea is the prototype of later theorems such as the divergence theorem and Stokes' theorem, and Green's theorem, which we examine in this post, can be regarded as the two-dimensional version of this spirit.

## Green's Theorem

First, for the boundary curve $\partial D$ of a planar region $D$, we define the *positive orientation* as the direction in which the region lies to the left; that is, the outer boundary is traversed counterclockwise. Then the following holds.

::: Theorem 1 (Green)
If $D$ is a planar region bounded by a piecewise smooth simple closed curve $C = \partial D$, and $P, Q$ are $C^1$ on an open set containing $D$, then with $C$ taken in the positive orientation,

$$\oint_C P\dd{x} + Q\dd{y} = \iint_D \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right)\dd{A}$$

holds.
:::

::: Proof
First, we prove the identity

$$\oint_C P\dd{x} = -\iint_D \partial P/\partial y\dd{A}$$

in the case where $D$ is simple with respect to $y$, that is,

$$D = \{(x,y) \mid a \leq x \leq b,\ g_1(x) \leq y \leq g_2(x)\}.$$

For the double integral, applying the iterated integral formula from [§Multiple Integrals, §§Fubini's Theorem](/en/math/calculus/multiple_integrals#fubinis-theorem) and integrating the inner integral first yields

$$\iint_D \frac{\partial P}{\partial y}\dd{A} = \int_a^b \bigl(P(x, g_2(x)) - P(x, g_1(x))\bigr)\dd{x}.$$

On the other hand, the boundary $C$ consists of two pieces: the lower curve $y = g_1(x)$ traversed with $x\colon a \rightarrow b$, and the upper curve $y = g_2(x)$ traversed with $x\colon b \rightarrow a$, while on the two vertical sides $x$ is constant so $\dd{x} = 0$. Therefore,

$$\oint_C P\dd{x} = \int_a^b P(x, g_1(x))\dd{x} + \int_b^a P(x, g_2(x))\dd{x} = -\int_a^b \bigl(P(x,g_2) - P(x,g_1)\bigr)\dd{x},$$

and comparing the two identities gives

$$\oint_C P\dd{x} = -\iint_D \partial P/\partial y\dd{A}.$$

Symmetrically, if $D$ is simple with respect to $x$, then

$$\oint_C Q\dd{y} = \iint_D \partial Q/\partial x\dd{A}.$$

For a general region, cutting it into such pieces and summing causes the integrals over interior boundaries to cancel as two integrals with opposite directions, so the theorem holds.
:::

In particular, choosing $P, Q$ so that the integrand of the double integral becomes $1$ allows us to compute the area of the region as a line integral over the boundary.

::: Corollary 2
The area of $D$ is given by the boundary integral

$$\area(D) = \oint_C x\dd{y} = -\oint_C y\dd{x} = \frac{1}{2}\oint_C (x\dd{y} - y\dd{x}).$$
:::

::: Proof
In [Theorem 1](#thm1), taking $(P, Q) = (0, x)$ gives $Q_x - P_y = 1$, so

$$\oint_C x\dd{y} = \iint_D 1\dd{A} = \area(D),$$

and taking $(P, Q) = (-y, 0)$ gives

$$\oint_C -y\dd{x} = \area(D).$$

The third identity is the average of these two.
:::

Meanwhile, Green's theorem can be rewritten in two forms that interpret two differential quantities of the planar vector field $\mathbf{F} = (P, Q)$ as boundary integrals. Here, the divergence of a planar vector field is obtained by viewing $\mathbf{F}$ as $(P, Q, 0)$ independent of $z$, giving $\divergence \mathbf{F} = \partial P/\partial x + \partial Q/\partial y$, just as in the case of curl. ([§Vector Fields, ⁋Definition 3](/en/math/calculus/vector_fields#def3))

::: Proposition 3
If the boundary $C$ of $D$ is positively oriented and $\mathbf{F} = (P, Q)$ is $C^1$, then for the unit tangent $\mathbf{T}$ and the outward unit normal $\mathbf{n}$,

$$\oint_C \mathbf{F} \cdot \mathbf{T}\dd{s} = \iint_D \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right)\dd{A}, \qquad \oint_C \mathbf{F} \cdot \mathbf{n}\dd{s} = \iint_D \divergence \mathbf{F}\dd{A}$$

hold.
:::

::: Proof
For the first identity,

$$\oint_C \mathbf{F}\cdot \mathbf{T}\dd{s} = \oint_C P\dd{x} + Q\dd{y}$$

is precisely the left-hand side of [Theorem 1](#thm1), and the integrand $Q_x - P_y$ on the right-hand side is the curl of the planar vector field. ([§Vector Fields, ⁋Definition 3](/en/math/calculus/vector_fields#def3))

For the second identity, using that on the positively oriented boundary the outward unit normal $\mathbf{n}$ satisfies $\mathbf{n}\dd{s} = (\dd{y}, -\dd{x})$, we have

$$\oint_C \mathbf{F}\cdot \mathbf{n}\dd{s} = \oint_C P\dd{y} - Q\dd{x},$$

and applying [Theorem 1](#thm1) to $(P, Q) \mapsto (-Q, P)$ shows that this equals

$$\iint_D (P_x + Q_y)\dd{A} = \iint_D \divergence \mathbf{F}\dd{A}.$$
:::

The first identity is exactly Green's theorem, and only the second is new, but its intuitive meaning is clear: integrating the function $\mathbf{F}$ along the boundary in the direction <em>outward</em> from the boundary captures precisely the divergence. On the other hand, we have already seen in [§Line Integrals, ⁋Example 6](/en/math/calculus/line_integrals#ex6) that even when curl vanishes, a vector field may fail to be conservative if the region has holes; this can be written rigorously as follows.

A region being *simply connected* means that any closed curve inside it can be continuously shrunk to a point without leaving the region; intuitively, one may think of this as a region without holes. For instance, a disk is simply connected, but a disk with its center removed is not, because to shrink a circle surrounding the center to a point one must necessarily pass through the missing center.

::: Corollary 4
In a simply connected open region, if a $C^1$ vector field $\mathbf{F} = (P, Q)$ satisfies $\partial Q/\partial x = \partial P/\partial y$, then $\mathbf{F}$ is conservative.
:::

::: Proof
Since the region is simply connected, the entire region $D$ enclosed by any simple closed curve $C$ inside it again lies within the region. Now

$$\oint_C \mathbf{F}\cdot d\mathbf{r} = \iint_D (Q_x - P_y)\dd{A} = 0,$$

and since the integral vanishes over every closed curve, [§Line Integrals, ⁋Theorem 4](/en/math/calculus/line_integrals#thm4) implies that $\mathbf{F}$ is conservative.
:::

::: Example 5 (Simple connectedness)
The vector field

$$\mathbf{F} = (-y, x)/(x^2+y^2)$$

from [§Line Integrals, ⁋Example 6](/en/math/calculus/line_integrals#ex6) is irrotational, but its integral over the unit circle around the origin was $2\pi$. By [Corollary 4](#cor4), this only makes sense if the domain on which this vector field is defined is not simply connected, and indeed the domain $\mathbb{R}^2\setminus\{0\}$ is not simply connected. Moreover, over any closed curve not enclosing the origin the integral of $\mathbf{F}$ is $0$, so we can also verify that the only problematic point is the origin where the vector field is undefined.
:::

---

**References**

**[Ste]** J. Stewart, *Calculus*, 8th ed., Cengage Learning, 2016.  
**[Kim]** 김홍종, *미적분학 1·2*, 제3개정판, 서울대학교출판문화원, 2020.
