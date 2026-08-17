---
title: "Line Integrals"
description: "We define scalar line integrals of scalar fields and vector line integrals of vector fields along curves. We prove the fundamental theorem for line integrals, establish equivalent conditions for path independence, and examine the angle field as an example of a non-conservative irrotational field."
excerpt: "Scalar and vector line integrals, work, fundamental theorem, and conservative fields"

categories: [Math / Calculus]
permalink: /en/math/calculus/line_integrals
sidebar: 
    nav: "calculus-en"

date: 2026-07-06
weight: 17
translated_at: 2026-08-17T23:46:23+00:00
translation_source: kimi-cli
---
We now examine the integral of a vector function. The first step toward this is the line integral, which accumulates the contributions of the vector at each point as we travel along a curve defined in the space $\mathbb{R}^n$ where the vector field is defined. What is interesting is that if the vector field is conservative, this integral becomes *independent* of the path and depends only on the endpoints, which can be regarded as a higher-dimensional version of [§The Fundamental Theorem of Calculus](/en/math/calculus/fundamental_theorem_of_calculus).

## Line Integral

::: Definition 1
The *line integral* of a continuous scalar field $f$ over a $C^1$ curve $\mathbf{r}\colon [a, b] \rightarrow \mathbb{R}^n$ is

$$\int_C f\dd{s} = \int_a^b f(\mathbf{r}(t))\lvert \mathbf{r}'(t)\rvert \dd{t}.$$

Here, $\dd{s} = \lvert \mathbf{r}'(t)\rvert \dd{t}$ is the arc length element.
:::

The above integral is independent of the parametrization of the curve because its value is preserved under a change of $C^1$ parametrization by the change of variables formula. As a special case, if $f \equiv 1$, then $\int_C \dd{s}$ gives the length of the curve.

To lift this to the integral of a vector function, we must take the direction of the curve into account and define it as follows.

::: Definition 2
The *line integral* of a continuous vector field $\mathbf{F}$ over a $C^1$ curve $\mathbf{r}\colon [a, b] \rightarrow \mathbb{R}^n$ is

$$\int_C \mathbf{F} \cdot d\mathbf{r} = \int_a^b \mathbf{F}(\mathbf{r}(t)) \cdot \mathbf{r}'(t)\dd{t}.$$
:::

If $\mathbf{F}$ represents a force field, the above integral becomes the *work* done by that force on an object moving along the curve $C$. This definition arises from starting with the fact that the work done when the force is constant and the displacement is $\mathbf{d}$ is $\mathbf{F}\cdot \mathbf{d}$, then approximating the instantaneous displacement by $\mathbf{r}'(t)\dd{t}$ and summing the dot product with the force over the entire curve.

If $\mathbf{r}$ is a regular curve, writing it using the unit tangent vector as $\mathbf{T} = \mathbf{r}'/\lvert \mathbf{r}'\rvert$, we can verify that

$$\int_C \mathbf{F}\cdot d\mathbf{r} = \int_C (\mathbf{F}\cdot \mathbf{T})\dd{s}.$$

In particular, in the plane, if $\mathbf{F} = (P, Q)$ and $\mathbf{r}(t) = (x(t), y(t))$, the notation

$$\int_C \mathbf{F}\cdot d\mathbf{r} = \int_C P\dd{x} + Q\dd{y}$$

is also commonly used. Also, the symbol $\oint$ is sometimes used to denote the integral along a closed curve, but this is merely a matter of notation and no essentially new content is added.

## Fundamental Theorem for Line Integrals

Our main theorem is, as foreshadowed above, that the line integral of a conservative field reduces to the difference of the function values at the endpoints.

::: Theorem 3 (Fundamental theorem for line integrals)
If $f$ is $C^1$ and $C$ is a $C^1$ curve from $\mathbf{r}(a) = \mathbf{A}$ to $\mathbf{r}(b) = \mathbf{B}$, then

$$\int_C \nabla f \cdot d\mathbf{r} = f(\mathbf{B}) - f(\mathbf{A}).$$

In particular, the line integral of a conservative field depends only on the two endpoints.
:::

::: Proof
By [§Functions of Several Variables and Partial Derivatives, ⁋Theorem 6](/en/math/calculus/partial_derivatives#thm6), we have $\frac{d}{\dd{t}} f(\mathbf{r}(t)) = \nabla f(\mathbf{r}(t)) \cdot \mathbf{r}'(t)$. Therefore, applying [§The Fundamental Theorem of Calculus, ⁋Theorem 4](/en/math/calculus/fundamental_theorem_of_calculus#thm4),

$$\int_C \nabla f \cdot d\mathbf{r} = \int_a^b \nabla f(\mathbf{r}(t)) \cdot \mathbf{r}'(t)\dd{t} = \int_a^b \frac{d}{\dd{t}} f(\mathbf{r}(t))\dd{t} = f(\mathbf{r}(b)) - f(\mathbf{r}(a)).$$

:::

[Theorem 3](#thm3) says that the line integral of a conservative field is independent of the path. Surprisingly, the converse also holds.

::: Theorem 4
Let $\mathbf{F}$ be continuous on a connected open region $D$. Then the following are equivalent.

1. $\mathbf{F}$ is a conservative field on $D$.
2. For every closed curve $C$ in $D$, $\oint_C \mathbf{F} \cdot d\mathbf{r} = 0$.
3. $\int_C \mathbf{F}\cdot d\mathbf{r}$ depends only on the two endpoints of $C$ and is independent of the path.
:::

::: Proof
$(1 \Rightarrow 3)$ is [Theorem 3](#thm3). Here, since $\mathbf{F} = \nabla f$ is continuous, the potential $f$ is automatically $C^1$. $(3 \Leftrightarrow 2)$ follows from cutting a closed curve at one point into two paths, and noting that reversing one path yields a closed curve. The integral over this reversed path is the negative of the original integral by the change of variables $t \mapsto a + b - t$, so the integral over a closed curve being zero is the same as the integrals over the two paths being equal.

Thus the key claim is $(3 \Rightarrow 1)$. For this, we must construct the potential directly. Fix a base point $\mathbf{x}_0 \in D$, and for any $\mathbf{x}\in D$, define $f(\mathbf{x})$ to be the line integral of $\mathbf{F}$ from $\mathbf{x}_0$ to $\mathbf{x}$. This would normally depend on the choice of curve $\mathbf{r}$ joining $\mathbf{x}_0$ and $\mathbf{x}$, but since we are assuming the third condition, this definition is well-defined. Now the average rate of change in the coordinate direction $\mathbf{e}_i$

$$\frac{f(\mathbf{x} + h \mathbf{e}_i) - f(\mathbf{x})}{h}$$

is the integral over the straight line segment from $\mathbf{x}$ to $\mathbf{x} + h \mathbf{e}_i$ divided by $h$, so as $h \rightarrow 0$ it converges to $F_i(\mathbf{x})$, and therefore $\partial f/\partial x_i = F_i$, that is, $\nabla f = \mathbf{F}$.
:::

Let us verify this in the following example.

::: Example 5 (Example of a conservative field)
Let us integrate $\mathbf{F} = (y, x)$ along the parabola $\mathbf{r}(t) = (t, t^2)$ ($0 \leq t \leq 1$) from the point $(0,0)$ to $(1,1)$.

$$\mathbf{F}(\mathbf{r}(t)) = (t^2, t),\qquad \mathbf{r}'(t) = (1, 2t)$$

so

$$\mathbf{F}\cdot \mathbf{r}' = t^2 + 2t^2 = 3t^2$$

and therefore integrating this gives

$$\int_C \mathbf{F}\cdot d\mathbf{r} = \int_0^1 3t^2\dd{t} = 1.$$

Indeed, since $\mathbf{F} = \nabla(xy)$, by [Theorem 3](#thm3) we can recover the above computation by calculating the difference of endpoint values of $xy$, namely $1\cdot 1 - 0\cdot 0 = 1$. This depends only on the endpoints; for instance, if we take $\mathbf{r}(t)=(t,t)$ ($0 \leq t \leq 1$), then

$$\mathbf{F}(\mathbf{r}(t))=(t,t),\qquad \mathbf{r}'(t)=(1,1)$$

so $\mathbf{F}\cdot \mathbf{r}'=2t$, and we can verify that

$$\int_C \mathbf{F}\cdot d\mathbf{r} = \int_0^1 2t\dd{t} = 1.$$

:::

Meanwhile, in [§Vector Fields, ⁋Proposition 6](/en/math/calculus/vector_fields#prop6) we saw that a conservative field necessarily satisfies the irrotational condition. [Theorem 4](#thm4) reveals why this is not sufficient, in the language of path independence. Since being a conservative field is equivalent to the integral over every closed curve being zero, if there is even one example where the closed curve integral is not zero despite being irrotational, then the field is not conservative. Such examples actually arise when the domain has a hole, and the following example is precisely that.

::: Example 6
Consider the vector field defined on the plane with the origin removed, $\mathbb{R}^2 \setminus \{0\}$,

$$\mathbf{F} = \left(\frac{-y}{x^2 + y^2}, \frac{x}{x^2 + y^2}\right).$$

Differentiating this directly,

$$\frac{\partial Q}{\partial x} = \frac{\partial P}{\partial y} = \frac{y^2 - x^2}{(x^2+y^2)^2}$$

so this vector field is irrotational. However, going once around the unit circle $\mathbf{r}(t) = (\cos t, \sin t)$, we have $\mathbf{F}(\mathbf{r}(t)) = (-\sin t, \cos t) = \mathbf{r}'(t)$, so

$$\oint_C \mathbf{F}\cdot d\mathbf{r} = \int_0^{2\pi} (\sin^2 t + \cos^2 t)\dd{t} = 2\pi \neq 0.$$

By [Theorem 4](#thm4), $\mathbf{F}$ is not a conservative field on this region. The cause is that although this vector field can locally be expressed as the gradient of the polar angle $\theta = \arctan(y/x)$, the polar angle increases by $2\pi$ upon encircling the origin and thus cannot be defined as a single-valued function.

:::

---

**References**

**[Ste]** J. Stewart, *Calculus*, 8th ed., Cengage Learning, 2016.  
**[Kim]** 김홍종, *미적분학 1·2*, 제3개정판, 서울대학교출판문화원, 2020.
