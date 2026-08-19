---
title: "Curves and Vector-Valued Functions"
description: "We introduce vector-valued functions that trace space curves with a single parameter, and define velocity, acceleration, and the unit tangent vector by differentiating component-wise. Arc length and the arc-length parameter, curvature and the unit normal vector, and the tangential-normal decomposition of acceleration are also covered."
excerpt: "Vector-valued functions, parametric curves, velocity and tangent, arc length, curvature and acceleration decomposition"

categories: [Math / Calculus]
permalink: /en/math/calculus/vector_functions
sidebar: 
    nav: "calculus-en"

date: 2026-07-04
weight: 13
translated_at: 2026-08-19T10:45:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-08-19T10:45:04+00:00
---
So far, the only functions we have dealt with are $f:\mathbb{R}\rightarrow\mathbb{R}$, sending real numbers to real numbers; to be blunt, apart from the fact that limits were rigorously defined via $\epsilon$-$\delta$, there was little difference from what we learned in high school. We now generalize this and turn to genuinely new content. The direction of generalization is to increase dimension, and there are two ways to do so: raising the dimension of the domain or raising the dimension of the codomain. In this post we first treat the latter, namely functions $\mathbf{r}:\mathbb{R}\rightarrow\mathbb{R}^n$ that send one real number to several real numbers. These are vector-valued functions that trace a curve in space with a single parameter, and can be viewed as the locus of a point moving in time; consequently, differentiation acquires the physical meaning of velocity and acceleration, and integration measures the length of a curve.

## Vector Spaces

A curve is a function that takes one real number and returns a point consisting of several real numbers, that is, a function into $\mathbb{R}^n$, so we first briefly review the structure of this space. $\mathbb{R}^n$ is a *vector space*, and its elements are called *vectors*. A vector is written as an ordered tuple

$$\mathbf{a}=(a_1, \ldots, a_n)\qquad a_i\in\mathbb{R}$$

and there are two basic operations on vectors. One is *addition* of two vectors $\mathbf{v}=(v_1,\ldots,v_n)$ and $\mathbf{w}=(w_1,\ldots,w_n)$,

$$\mathbf{v}+\mathbf{w}=(v_1+w_1,\ldots,v_n+w_n)$$

and the other is *scalar multiplication* by a real number $c$,

$$c\mathbf{v}=(cv_1,\ldots,cv_n).$$

These operations are exactly the vector operations seen in the coordinate plane, lifted to $n$ dimensions, and the commutative, associative, and distributive laws hold naturally. In particular, the vectors

$$\mathbf{e}_1=(1,0,\ldots, 0,0),\ldots, \mathbf{e}_n=(0,0,\ldots, 0,1)$$

are called the *standard basis vectors*, and using them any vector can be written as

$$\mathbf{v}=\sum_{i=1}^n v_i \mathbf{e}_i.$$

Since the space we deal with is Euclidean, we also employ the inner product and norm. The *inner product* of two vectors $\mathbf{v},\mathbf{w}\in\mathbb{R}^n$ is defined as the sum of coordinate-wise products,

$$\mathbf{v}\cdot \mathbf{w}=v_1w_1+\cdots+v_nw_n$$

and from this the *norm*, i.e., the magnitude of a vector, is given by $\lVert \mathbf{v}\rVert=\sqrt{\mathbf{v}\cdot \mathbf{v}}$. The inner product is also used to measure the angle between two vectors, and in particular when $\mathbf{v}\cdot \mathbf{w}=0$ we say the two vectors are *orthogonal*.

Meanwhile, in three dimensions $\mathbb{R}^3$, the *cross product* is additionally defined. For two vectors $\mathbf{v},\mathbf{w}\in\mathbb{R}^3$, the cross product $\mathbf{v}\times \mathbf{w}$ is the vector that is orthogonal to both $\mathbf{v}$ and $\mathbf{w}$, whose direction follows the right-hand rule, and whose magnitude equals the area of the parallelogram formed by $\mathbf{v}$ and $\mathbf{w}$. In coordinates it is computed as

$$\mathbf{v}\times \mathbf{w}=(v_2w_3-v_3w_2,\ v_3w_1-v_1w_3,\ v_1w_2-v_2w_1).$$

In this post we mainly use the cross product as a tool for producing orthogonal vectors.

## Vector-Valued Functions

We may now define the following.

::: Definition 1
A function $\mathbf{r}\colon I \rightarrow \mathbb{R}^n$ assigning to each $t$ in an interval $I \subseteq \mathbb{R}$ the point $\mathbf{r}(t) = (x_1(t), \ldots, x_n(t)) \in \mathbb{R}^n$ is called a *vector-valued function* or *parametrized curve*, and each $x_i$ is called its *component function*.
:::

Intuitively, this is a rule by which a different point in the vector space corresponds to each value of $t$, and can be thought of as expressing the locus of a point moving in time.

The limit of a vector-valued function is defined in the same way as the limit of a one-dimensional function. That is, whenever any $\epsilon>0$ is given, there exists a suitable $\delta>0$ such that

$$0<\lvert t-t_0\rvert<\delta\implies \lVert \mathbf{r}(t)-\mathbf{v}\rVert<\epsilon$$

holds, we say this vector function $\mathbf{r}$ converges to the vector $\mathbf{v}$ as $t\rightarrow t_0$. Then by the Cauchy–Schwarz inequality

$$\lvert\mathbf{a}\cdot\mathbf{b}\rvert\leq\lVert\mathbf{a}\rVert\lVert\mathbf{b}\rVert$$

we have

$$\lvert x_i(t)-v_i\rvert=\lvert(\mathbf{r}(t)-\mathbf{v})\cdot\mathbf{e}_i\rvert\leq\lVert\mathbf{r}(t)-\mathbf{v}\rVert$$

so if $\mathbf{r}(t)\rightarrow\mathbf{v}$ then each component also converges, $x_i(t)\rightarrow v_i$. Conversely, if all components converge then

$$\lVert\mathbf{r}(t)-\mathbf{v}\rVert^2=\sum_i(x_i(t)-v_i)^2\rightarrow 0$$

so $\mathbf{r}(t)\rightarrow\mathbf{v}$. Thus convergence of a vector function is equivalent to convergence of each component function, and in particular continuity and differentiability of a vector function are both well defined component-wise.

::: Proposition 2
If each component function of $\mathbf{r}(t) = (x_1(t), \ldots, x_n(t))$ is differentiable at $t$, then $\mathbf{r}$ is also differentiable at $t$ and $\mathbf{r}'(t) = (x_1'(t), \ldots, x_n'(t))$.
:::

::: Proof
The $i$-th component of the difference quotient $(\mathbf{r}(t+h) - \mathbf{r}(t))/h$ is exactly $(x_i(t+h) - x_i(t))/h$. Since the limit of each component exists and equals $x_i'(t)$, we have $\mathbf{r}'(t) = (x_1'(t), \ldots, x_n'(t))$.
:::

Moreover, by a similar argument the product rule for scalar functions carries over to vector products.

::: Proposition 3 (Differentiation Rules)
If $\mathbf{u}, \mathbf{v}\colon I \rightarrow \mathbb{R}^n$ are differentiable, $f\colon I \rightarrow \mathbb{R}$ is differentiable, and $\varphi\colon J \rightarrow I$ is a differentiable real function, then

$$(f \mathbf{u})' = f' \mathbf{u} + f \mathbf{u}', \qquad (\mathbf{u} \cdot \mathbf{v})' = \mathbf{u}' \cdot \mathbf{v} + \mathbf{u} \cdot \mathbf{v}', \qquad (\mathbf{u} \circ \varphi)'(t) = \varphi'(t) \mathbf{u}'(\varphi(t))$$

and when $n = 3$, for the cross product $(\mathbf{u} \times \mathbf{v})' = \mathbf{u}' \times \mathbf{v} + \mathbf{u} \times \mathbf{v}'$.
:::

::: Proof
Writing everything out component-wise reduces each identity to the product rule and chain rule for scalar functions. For example, the inner product is $\mathbf{u} \cdot \mathbf{v} = \sum_i u_i v_i$, so $(\mathbf{u} \cdot \mathbf{v})' = \sum_i (u_i' v_i + u_i v_i') = \mathbf{u}' \cdot \mathbf{v} + \mathbf{u} \cdot \mathbf{v}'$; the cross product and scalar multiplication can be shown in the same way since each component is a sum of products of the form $u_i v_j$. The composition rule follows by applying [§Differentiation, ⁋Theorem 4](/en/math/calculus/differentiation_rules#thm4) to each component.
:::

One useful corollary of this proposition is that if $\lVert \mathbf{u}(t)\rVert$ is constant then $\mathbf{u} \cdot \mathbf{u} = \lVert \mathbf{u}\rVert^2$ is also constant, so $(\mathbf{u} \cdot \mathbf{u})' = 2 \mathbf{u} \cdot \mathbf{u}' = 0$, i.e., $\mathbf{u} \perp \mathbf{u}'$. Hence the derivative of a vector of constant length is always perpendicular to that vector, and the fact that in circular motion the position vector and velocity are perpendicular is a special case of this.

## Velocity and Acceleration

As we saw above, vector functions are a good tool for representing physical phenomena. We now explain that physical intuition.

::: Definition 4
For a curve $\mathbf{r}(t)$, we call $\mathbf{r}'(t)$ the *velocity*, its magnitude $\lVert \mathbf{r}'(t)\rVert$ the *speed*, and $\mathbf{r}''(t)$ the *acceleration*. At points where $\mathbf{r}'(t) \neq 0$,

$$\mathbf{T}(t) = \frac{\mathbf{r}'(t)}{\lVert \mathbf{r}'(t)\rVert}$$

is called the *unit tangent vector*.
:::

Velocity points in the direction of the curve's progression and its magnitude is the speed of the point, while the unit tangent vector retains only the direction of the velocity. For this to be well defined, the parametrized curve $\mathbf{r}$ must be a *$C^1$-regular curve*, meaning a curve satisfying both of the following conditions.

1. $\mathbf{r}$ is *$C^1$*. That is, the velocity vector $\mathbf{r}'(t)$ exists continuously.
2. $\mathbf{r}$ is *regular*. That is, there is no point where $\mathbf{r}'(t)$ vanishes.

Then by the second condition the unit tangent vector $\mathbf{T}$ is well defined everywhere, and by the first condition $\mathbf{T}(t)$ is continuous. In this post, unless stated otherwise, we take $C^1$-regular curves as the default.

Given a moving object, one of the quantities we wish to know is the distance traveled over time. This is obtained, just as in one dimension, by integrating the speed; rigorously, one approximates the curve by a polygon connecting points on it, forms for a partition

$$a = t_0 < \cdots < t_m = b$$

the sum of line-segment lengths

$$\sum_k \lVert \mathbf{r}(t_k) - \mathbf{r}(t_{k-1})\rVert$$

and refines the partition to show that this converges to a Riemann sum of $\lVert \mathbf{r}'(t)\rVert$. This process compresses to the following definition.

::: Definition 5
The *arc length* of a $C^1$ curve $\mathbf{r}\colon [a, b] \rightarrow \mathbb{R}^n$ is

$$L = \int_a^b \lVert \mathbf{r}'(t)\rVert \dd{t}.$$
:::

The integrand $\lVert \mathbf{r}'(t)\rVert$ is continuous, hence integrable ([§Integration, ⁋Theorem 10](/en/math/calculus/integration#thm10)). We call

$$s(t) = \int_a^t \lVert \mathbf{r}'(\tau)\rVert \dd{\tau}$$

the *arc length* measured from the starting point; by the fundamental theorem of calculus $s'(t) = \lVert \mathbf{r}'(t)\rVert > 0$, so $s$ is an increasing function, and we can solve for $t$ in terms of $s$ to reparametrize the curve by arc length.

::: Proposition 6
If a curve is parametrized by arc length $s$, then it has unit speed. That is, $\lVert d\mathbf{r}/\dd{s}\rVert = 1$.
:::

::: Proof
By the chain rule $d\mathbf{r}/\dd{t} = (d\mathbf{r}/\dd{s})(\dd{s}/\dd{t})$ and $\dd{s}/\dd{t} = \lVert \mathbf{r}'(t)\rVert = \lVert d\mathbf{r}/\dd{t}\rVert$, so $\lVert d\mathbf{r}/\dd{s}\rVert = \lVert d\mathbf{r}/\dd{t}\rVert / (\dd{s}/\dd{t}) = 1$.
:::

The parametrization obtained in this way is called *arc length parametrization*.

## Curvature

How much a curve bends is measured by how quickly the direction of the unit tangent vector changes as we proceed along the curve. However, if the curve moves quickly then the rate of change will also increase, so to examine how much the shape of the curve is bent we must normalize this rate. Moreover, intuitively this quantity is obtained by differentiating the unit tangent vector (already the derivative of the original curve) once more, so we must now consider *second-order* curves. That is, the acceleration vector $\mathbf{r}''(t)$ must exist continuously.

::: Definition 7
The *curvature* of a second-order regular curve is the magnitude of the rate at which the unit tangent vector changes with respect to arc length,

$$\kappa = \left\lVert \frac{d\mathbf{T}}{\dd{s}}\right\rVert.$$

When $d\mathbf{T}/\dd{s} \neq 0$, the unit vector in that direction

$$\mathbf{N} = \frac{d\mathbf{T}/\dd{s}}{\lVert d\mathbf{T}/\dd{s}\rVert}$$

is called the *unit normal vector*.
:::

Note that by [Proposition 6](#prop6), $\mathbf{T} = d\mathbf{r}/\dd{s}$ is a unit vector. Then by the observation examined right after [Proposition 3](#prop3), that the derivative of a vector of constant length is perpendicular to that vector, we have $d\mathbf{T}/\dd{s} \perp \mathbf{T}$. Thus the unit normal vector $\mathbf{N}$ is always perpendicular to the tangent, and points to the inside into which the curve is bending.

The above definition applies to curves in general $n$-dimensional space, but in $3$-dimensional space the cross product allows us to compute curvature more conveniently. In particular, the following formula can be applied directly without arc length parametrization, which is far more practical.

::: Proposition 8 (Curvature Formula)
The curvature of a second-order regular curve $\mathbf{r}(t)$ in $3$-dimensional space is

$$\kappa = \frac{\lVert \mathbf{r}' \times \mathbf{r}''\rVert}{\lVert \mathbf{r}'\rVert^3}$$

and in particular the curvature of a plane curve $y = f(x)$ is

$$\kappa = \frac{\lvert f''\rvert}{(1 + f'^2)^{3/2}}.$$
:::

::: Proof
Let $v = \lVert \mathbf{r}'\rVert = \dd{s}/\dd{t}$; then $\mathbf{r}' = v\mathbf{T}$. By the product rule,

$$\mathbf{r}'' = v'\mathbf{T} + v\mathbf{T}'(t)$$

and by the chain rule $\mathbf{T}'(t) = (d\mathbf{T}/\dd{s})v$ and $\lVert d\mathbf{T}/\dd{s}\rVert = \kappa$, so $\lVert \mathbf{T}'(t)\rVert = \kappa v$. Therefore

$$\mathbf{r}' \times \mathbf{r}'' = (v\mathbf{T}) \times (v'\mathbf{T} + v\mathbf{T}'(t)) = v^2(\mathbf{T} \times \mathbf{T}'(t)).$$

Here the second equality follows from $\mathbf{T}\times \mathbf{T}=0$. Now $\mathbf{T}$ is a unit vector, and by the observation right after [Proposition 3](#prop3) that the derivative of a vector of constant length is perpendicular to that vector, we have $\mathbf{T} \perp \mathbf{T}'(t)$, so $\lVert \mathbf{T} \times \mathbf{T}'(t)\rVert = \lVert \mathbf{T}'(t)\rVert = \kappa v$, and

$$\lVert \mathbf{r}' \times \mathbf{r}''\rVert = v^3 \kappa = \lVert \mathbf{r}'\rVert^3 \kappa$$

yielding the desired equality. The formula for a plane curve $y = f(x)$ follows by setting $\mathbf{r}(x) = (x, f(x),0)$ and applying the $3$-dimensional formula directly.
:::

Differentiating $\mathbf{r}' = v\mathbf{T}$, which appeared in the proof, once more gives $\mathbf{r}'' = v'\mathbf{T} + v\mathbf{T}'(t)$, and at points where $\kappa \neq 0$ we have $d\mathbf{T}/\dd{s} = \kappa\mathbf{N}$ so $\mathbf{T}'(t) = \kappa v\mathbf{N}$; therefore there $\mathbf{r}'' = v'\mathbf{T} + \kappa v^2\mathbf{N}$. This equation is meaningful in itself: the acceleration splits into a tangential component and a normal component. Let us record this as a separate proposition.

::: Proposition 9 (Decomposition of Acceleration)
At points of a second-order regular curve where $\kappa \neq 0$, the acceleration decomposes as

$$\mathbf{r}'' = \frac{\dd{v}}{\dd{t}}\mathbf{T} + \kappa v^2\mathbf{N}.$$

Here $v = \lVert \mathbf{r}'\rVert$ is the speed.
:::

The tangential component $\dd{v}/\dd{t}$ tells us how much the speed is changing, and the normal component $\kappa v^2$ tells us how much the direction is bending. If the motion is uniform then $\dd{v}/\dd{t} = 0$, so the acceleration is purely in the normal direction (namely centripetal acceleration) and its magnitude is $\kappa v^2$.

::: Example 10 (Helix)
For the helix $\mathbf{r}(t) = (\cos t, \sin t, t)$, we have $\mathbf{r}'(t) = (-\sin t, \cos t, 1)$ and $\mathbf{r}''(t) = (-\cos t, -\sin t, 0)$. The cross product is

$$\mathbf{r}' \times \mathbf{r}'' = (\sin t,\ -\cos t,\ 1), \qquad \lVert \mathbf{r}' \times \mathbf{r}''\rVert = \sqrt{2}$$

and $\lVert \mathbf{r}'\rVert = \sqrt{2}$, so the curvature is $\kappa = \sqrt{2}/(\sqrt{2})^3 = 1/2$, which is constant. Since the speed $v = \sqrt{2}$ is constant, by [Proposition 9](#prop9) the acceleration is purely normal and its magnitude is $\kappa v^2 = (1/2)\cdot 2 = 1$, which indeed matches $\lVert \mathbf{r}''(t)\rVert = \lVert(-\cos t, -\sin t, 0)\rVert = 1$.
:::

---

**References**

**[Ste]** J. Stewart, *Calculus*, 8th ed., Cengage Learning, 2016.  
**[Kim]** 김홍종, *미적분학 1·2*, 제3개정판, 서울대학교출판문화원, 2020.
