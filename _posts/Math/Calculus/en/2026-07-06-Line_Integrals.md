---
title: "Line Integrals"
description: "We define scalar line integrals of scalar fields and vector line integrals (work) of vector fields along curves. We show the fundamental theorem of line integrals for conservative fields and equivalent conditions for path independence, and examine the angle field, which is irrotational but not conservative."
excerpt: "Scalar and vector line integrals, work, fundamental theorem, path independence, conservative fields"

categories: [Math / Calculus]
permalink: /en/math/calculus/line_integrals
sidebar: 
    nav: "calculus-en"

date: 2026-07-06
weight: 17
translated_at: 2026-08-19T11:15:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-01T07:15:05+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
We now examine the integral of a vector function. The first step for this is the line integral, which follows a curve defined in the space $\mathbb{R}^n$ where the vector field is defined and sums and accumulates all the forces contributed by the vector at each point. What is interesting is that if the vector field is conservative, this integral becomes *independent* of the path and depends only on the endpoints; this can be regarded as a higher-dimensional version of [§The Fundamental Theorem of Calculus](/en/math/calculus/fundamental_theorem_of_calculus){: data-lid="rz832" }.

## Line Integrals

::: Definition 1
Over a $C^1$ curve $\mathbf{r}\colon [a, b] \rightarrow \mathbb{R}^n$, the *line integral* of a continuous scalar field $f$ is

$$\int_C f\dd{s} = \int_a^b f(\mathbf{r}(t))\lvert \mathbf{r}'(t)\rvert \dd{t}$$

Here, $\dd{s} = \lvert \mathbf{r}'(t)\rvert \dd{t}$ is the arc length element.
:::

The above integral does not depend on the parametrization of the curve, since its value is preserved under a change of $C^1$ parametrization by substitution. As a special case, if $f \equiv 1$, then $\int_C \dd{s}$ gives the length of the curve.

Now, to lift this to the integral of a vector function, we must take into account the direction of the curve and define it as follows.

::: Definition 2
Over a $C^1$ curve $\mathbf{r}\colon [a, b] \rightarrow \mathbb{R}^n$, the *line integral* of a continuous vector field $\mathbf{F}$ is

$$\int_C \mathbf{F} \cdot d\mathbf{r} = \int_a^b \mathbf{F}(\mathbf{r}(t)) \cdot \mathbf{r}'(t)\dd{t}$$
:::

When $\mathbf{F}$ is a vector field representing a force, the above integral is the *work* done by that force on an object moving along the curve $C$. This is because, starting from the fact that the work when the force is constant and the displacement is $\mathbf{d}$ is $\mathbf{F}\cdot \mathbf{d}$, the above definition approximates the displacement at each instant by $\mathbf{r}'(t)\dd{t}$ and sums the dot product with the force over the entire curve.

When $\mathbf{r}$ is a continuously differentiable regular curve, using the unit tangent vector to write $\mathbf{T} = \mathbf{r}'/\lvert \mathbf{r}'\rvert$, one can verify that

$$\int_C \mathbf{F}\cdot d\mathbf{r} = \int_C (\mathbf{F}\cdot \mathbf{T})\dd{s}$$

In particular, in the plane, if $\mathbf{F} = (P, Q)$ and $\mathbf{r}(t) = (x(t), y(t))$, the notation

$$\int_C \mathbf{F}\cdot d\mathbf{r} = \int_C P\dd{x} + Q\dd{y}$$

is also commonly used. In addition, $\oint$ is sometimes used to denote the result of integrating along a closed curve, but this is a matter of notation and adds essentially no new content.

## Fundamental Theorem for Line Integrals

Our key theorem is, as foreshadowed above, that the line integral of a conservative field reduces to the difference of the function values at the endpoints.

::: Theorem 3 (Fundamental theorem for line integrals)
If $f$ is $C^1$ and $C$, from $\mathbf{r}(a) = \mathbf{A}$ to $\mathbf{r}(b) = \mathbf{B}$, is a $C^1$ curve, then

$$\int_C \nabla f \cdot d\mathbf{r} = f(\mathbf{B}) - f(\mathbf{A})$$

In particular, the line integral of a conservative field depends only on its endpoints.
:::

::: Proof
By [§Functions of Several Variables and Partial Derivatives, ⁋Theorem 6](/en/math/calculus/partial_derivatives#thm6){: data-lid="vuire" }, we have $\frac{d}{\dd{t}} f(\mathbf{r}(t)) = \nabla f(\mathbf{r}(t)) \cdot \mathbf{r}'(t)$. Therefore, applying [§The Fundamental Theorem of Calculus, ⁋Theorem 4](/en/math/calculus/fundamental_theorem_of_calculus#thm4){: data-lid="59ek9" }, we obtain

$$\int_C \nabla f \cdot d\mathbf{r} = \int_a^b \nabla f(\mathbf{r}(t)) \cdot \mathbf{r}'(t)\dd{t} = \int_a^b \frac{d}{\dd{t}} f(\mathbf{r}(t))\dd{t} = f(\mathbf{r}(b)) - f(\mathbf{r}(a))$$
:::

[Theorem 3](#thm3){: data-lid="p22mi" } states that the line integral of a conservative field is independent of the path. Surprisingly, the converse also holds.

::: Theorem 4
When $\mathbf{F}$ is continuous on a connected open region $D$, the following are equivalent.

1. $\mathbf{F}$ is a conservative field on $D$.
2. In $D$, for every closed curve $C$, $\oint_C \mathbf{F} \cdot d\mathbf{r} = 0$.
3. $\int_C \mathbf{F}\cdot d\mathbf{r}$ depends only on the endpoints of $C$ and is independent of the path.
:::

::: Proof
$(1 \Rightarrow 3)$ is [Theorem 3](#thm3){: data-lid="pxo9x" }. Here, since $\mathbf{F} = \nabla f$ is continuous, the potential $f$ is automatically $C^1$. $(3 \Leftrightarrow 2)$ follows from viewing a closed curve as two paths by cutting it at a point, and noting that joining one path in reverse yields a closed curve. This is because the integral over this path is the negative of the original integral by the substitution $t \mapsto a + b - t$, so that the integral over the closed curve being $0$ and the integrals over the two paths being equal mean the same thing.

Thus the key claim is $(3 \Rightarrow 1)$. For this, we must construct the potential directly. Fix a base point $\mathbf{x}_0 \in D$, and for any $\mathbf{x}\in D$, define $f(\mathbf{x})$ as the line integral from $\mathbf{x}_0$ to $\mathbf{x}$ of $\mathbf{F}$. In joining $\mathbf{x}_0$ and $\mathbf{x}$, this would normally depend on the choice of curve $\mathbf{r}$, but since we are assuming the third condition, this definition is justified. Now the average rate of change in a coordinate direction $\mathbf{e}_i$

$$\frac{f(\mathbf{x} + h \mathbf{e}_i) - f(\mathbf{x})}{h}$$

is the integral over the straight line segment from $\mathbf{x}$ to $\mathbf{x} + h \mathbf{e}_i$ divided by $h$, so as $h \rightarrow 0$ it converges to $F_i(\mathbf{x})$, and therefore $\partial f/\partial x_i = F_i$, that is, $\nabla f = \mathbf{F}$.
:::

For instance, let us verify this in the following example.

::: Example 5 (Example of a conservative field)
Let us integrate $\mathbf{F} = (y, x)$ from the point $(0,0)$ to $(1,1)$ along the parabola $\mathbf{r}(t) = (t, t^2)$ ($0 \leq t \leq 1$).

$$\mathbf{F}(\mathbf{r}(t)) = (t^2, t),\qquad \mathbf{r}'(t) = (1, 2t)$$

so

$$\mathbf{F}\cdot \mathbf{r}' = t^2 + 2t^2 = 3t^2$$

and therefore, integrating this gives

$$\int_C \mathbf{F}\cdot d\mathbf{r} = \int_0^1 3t^2\dd{t} = 1$$

Indeed, since $\mathbf{F} = \nabla(xy)$, by [Theorem 3](#thm3){: data-lid="r0jnd" } calculating the difference between the endpoint values of $xy$, namely $1\cdot 1 - 0\cdot 0 = 1$, allows us to recover the above computation. This depends only on the endpoints; for instance, if we set $\mathbf{r}(t)=(t,t)$ ($0 \leq t \leq 1$), then

$$\mathbf{F}(\mathbf{r}(t))=(t,t),\qquad \mathbf{r}'(t)=(1,1)$$

so $\mathbf{F}\cdot \mathbf{r}'=2t$, and we can confirm that

$$\int_C \mathbf{F}\cdot d\mathbf{r} = \int_0^1 2t\dd{t} = 1$$

:::

Meanwhile, in [§Vector Fields, ⁋Proposition 6](/en/math/calculus/vector_fields#prop6){: data-lid="7o9p2" } we saw that a conservative field has the necessary condition of being irrotational. [Theorem 4](#thm4){: data-lid="oq6bx" } reveals why this is not a sufficient condition in the language of path independence. Since being a conservative field is equivalent to the integral over every closed curve being $0$, if there is even one example where the integral over a closed curve is not $0$ despite the field being irrotational, it is not a conservative field. Such examples actually arise when the domain has a hole, and the very next example is precisely that.

::: Example 6
Consider the vector field defined on the plane with the origin removed, $\mathbb{R}^2 \setminus \{0\}$,

$$\mathbf{F} = \left(\frac{-y}{x^2 + y^2}, \frac{x}{x^2 + y^2}\right)$$

Differentiating this directly, we have

$$\frac{\partial Q}{\partial x} = \frac{\partial P}{\partial y} = \frac{y^2 - x^2}{(x^2+y^2)^2}$$

so this vector field is irrotational. However, traversing the unit circle $\mathbf{r}(t) = (\cos t, \sin t)$ once, we have $\mathbf{F}(\mathbf{r}(t)) = (-\sin t, \cos t) = \mathbf{r}'(t)$, so

$$\oint_C \mathbf{F}\cdot d\mathbf{r} = \int_0^{2\pi} (\sin^2 t + \cos^2 t)\dd{t} = 2\pi \neq 0$$

By [Theorem 4](#thm4){: data-lid="hqwyz" }, $\mathbf{F}$ is not a conservative field on this region. The reason is that although this vector field can locally be expressed as the gradient of the polar angle $\theta = \arctan(y/x)$, the polar angle increases by $2\pi$ upon encircling the origin and thus cannot be defined as a single-valued function.
:::

---

**References**

**[Ste]** J. Stewart, *Calculus*, 8th ed., Cengage Learning, 2016.  
**[Kim]** 김홍종, *미적분학 1·2*, 제3개정판, 서울대학교출판문화원, 2020.
