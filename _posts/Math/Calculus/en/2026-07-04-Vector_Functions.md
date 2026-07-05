---
title: "Curves and Vector-Valued Functions"
description: "Introduce vector-valued functions that trace space curves with a single parameter, and define velocity, acceleration, and the unit tangent vector through component-wise differentiation. Covers arc length and the arc-length parameter, curvature and the unit normal vector, and the tangential-normal decomposition of acceleration."
excerpt: "Vector-valued functions, parametric curves, velocity and tangent, arc length, curvature and acceleration decomposition"

categories: [Math / Calculus]
permalink: /en/math/calculus/vector_functions
sidebar: 
    nav: "calculus-en"

date: 2026-07-04
weight: 13
translated_at: 2026-07-05T15:00:02+00:00
translation_source: kimi-cli
---
So far, the functions we have dealt with were only $$f:\mathbb{R}\to\mathbb{R}$$ sending real numbers to real numbers, and to be honest, apart from the fact that the concept of limits was rigorously defined using $$\epsilon$$-$$\delta$$, there was little difference from what we learned in high school. We now generalize this to actually explore new material. The direction of generalization is to increase dimension, which includes raising the dimension of the domain and raising the dimension of the codomain. In this post, we first deal with the latter, namely a function $$\mathbf{r}:\mathbb{R}\to\mathbb{R}^n$$ that sends one real number to several real numbers. This is a vector-valued function that draws a curve in space with a single parameter, and can be viewed as the locus of a point moving in time, so that differentiation acquires the physical meaning of velocity and acceleration, and integration measures the length of a curve.

## Vector Space

A curve is a function that takes one real number and outputs a point consisting of several real numbers, that is, a function into $$\mathbb{R}^n$$, so we first briefly review the structure of that space. $$\mathbb{R}^n$$ is a *vector space*, and the elements of this space are called *vectors*. A vector is written as an ordered tuple

$$\mathbf{a}=(a_1, \ldots, a_n)\qquad a_i\in\mathbb{R}$$

and there are two basic operations between vectors. One is *addition* of two vectors $$\mathbf{v}=(v_1,\ldots,v_n)$$ and $$\mathbf{w}=(w_1,\ldots,w_n)$$

$$\mathbf{v}+\mathbf{w}=(v_1+w_1,\ldots,v_n+w_n)$$

and the other is *scalar multiplication* by a real number $$c$$

$$c\mathbf{v}=(cv_1,\ldots,cv_n)$$

These operations are exactly the vector operations seen in the coordinate plane lifted to $$n$$ dimensions, and the commutative law, associative law, distributive law, etc. hold naturally. In particular, the following vectors

$$\mathbf{e}_1=(1,0,\ldots, 0,0),\ldots, \mathbf{e}_n=(0,0,\ldots, 0,1)$$

are called *standard basis vectors*, and using them any vector can be written as

$$\mathbf{v}=\sum_{i=1}^n v_i \mathbf{e}_i$$

The space we are dealing with is Euclidean space, so we also use the inner product and norm together. The *inner product* of two vectors $$\mathbf{v},\mathbf{w}\in\mathbb{R}^n$$ is defined as the sum of coordinate-wise products

$$\mathbf{v}\cdot \mathbf{w}=v_1w_1+\cdots+v_nw_n$$

and from this the *norm* of a vector, that is, its magnitude, is given by $$\lVert \mathbf{v}\rVert=\sqrt{\mathbf{v}\cdot \mathbf{v}}$$. The inner product is also used to measure the angle between two vectors, and in particular when $$\mathbf{v}\cdot \mathbf{w}=0$$ we say the two vectors are *orthogonal*.

On the other hand, in three-dimensional $$\mathbb{R}^3$$ the *cross product* is additionally defined. For two vectors $$\mathbf{v},\mathbf{w}\in\mathbb{R}^3$$, the cross product $$\mathbf{v}\times \mathbf{w}$$ is a vector that is perpendicular to both $$\mathbf{v}$$ and $$\mathbf{w}$$, whose direction follows the right-hand rule, and whose magnitude equals the area of the parallelogram formed by $$\mathbf{v}$$ and $$\mathbf{w}$$. In coordinates it is computed as

$$\mathbf{v}\times \mathbf{w}=(v_2w_3-v_3w_2,\ v_3w_1-v_1w_3,\ v_1w_2-v_2w_1)$$

In this post we mainly use the cross product as a tool to create perpendicular vectors.

## Vector-Valued Functions

Then we can first define the following.

::: Definition 1
A function $$\mathbf{r}\colon I \to \mathbb{R}^n$$ that assigns to each $$t$$ in an interval $$I \subseteq \mathbb{R}$$ the point $$\mathbf{r}(t) = (x_1(t), \ldots, x_n(t)) \in \mathbb{R}^n$$ is called a *vector-valued function* or a *parametrized curve*, and each $$x_i$$ is called its *component function*.
:::

Intuitively, this is a rule by which a different point in the vector space corresponds as $$t$$ varies, and can be thought of as expressing the locus of a point moving in time.

The limit of a vector-valued function is defined in the same way as the limit of a function in one dimension. That is, whenever any $$\epsilon$$ is given, if there always exists an appropriate $$\delta>0$$ such that

$$0<\lvert t-t_0\rvert<\delta\implies \lVert \mathbf{r}(t)-\mathbf{v}\rVert<\epsilon$$

is satisfied, we say this vector function $$\mathbf{r}$$ converges to the vector $$\mathbf{v}$$ as $$t\rightarrow t_0$$. Then by the Cauchy–Schwarz inequality

$$\lvert\mathbf{a}\cdot\mathbf{b}\rvert\leq\lVert\mathbf{a}\rVert\lVert\mathbf{b}\rVert$$

we have

$$\lvert x_i(t)-v_i\rvert=\lvert(\mathbf{r}(t)-\mathbf{v})\cdot\mathbf{e}_i\rvert\leq\lVert\mathbf{r}(t)-\mathbf{v}\rVert$$

so if $$\mathbf{r}(t)\to\mathbf{v}$$ then each component also converges $$x_i(t)\to v_i$$. Conversely, if all components converge then

$$\lVert\mathbf{r}(t)-\mathbf{v}\rVert^2=\sum_i(x_i(t)-v_i)^2\to 0$$

so $$\mathbf{r}(t)\to\mathbf{v}$$. That is, the convergence of a vector function is the same as the convergence of each component function, and in particular the continuity and differentiability of a vector function are both well defined component-wise.

::: Proposition 2
If each component function of $$\mathbf{r}(t) = (x_1(t), \ldots, x_n(t))$$ is differentiable at $$t$$, then $$\mathbf{r}$$ is also differentiable at $$t$$ and $$\mathbf{r}'(t) = (x_1'(t), \ldots, x_n'(t))$$.
:::

::: Proof
The $$i$$th component of the difference quotient $$(\mathbf{r}(t+h) - \mathbf{r}(t))/h$$ is exactly $$(x_i(t+h) - x_i(t))/h$$. Since the limit of each component exists as $$x_i'(t)$$, we have $$\mathbf{r}'(t) = (x_1'(t), \ldots, x_n'(t))$$.
:::

Also, by a similar argument the product rule for scalar functions carries over to vector products.

::: Proposition 3 (Differentiation Rules)
If $$\mathbf{u}, \mathbf{v}\colon I \to \mathbb{R}^n$$ are differentiable and $$f\colon I \to \mathbb{R}$$ is differentiable and $$\varphi\colon J \to I$$ is a differentiable real function, then

$$(f \mathbf{u})' = f' \mathbf{u} + f \mathbf{u}', \qquad (\mathbf{u} \cdot \mathbf{v})' = \mathbf{u}' \cdot \mathbf{v} + \mathbf{u} \cdot \mathbf{v}', \qquad (\mathbf{u} \circ \varphi)'(t) = \varphi'(t) \mathbf{u}'(\varphi(t))$$

and when $$n = 3$$ for the cross product $$(\mathbf{u} \times \mathbf{v})' = \mathbf{u}' \times \mathbf{v} + \mathbf{u} \times \mathbf{v}'$$.
:::

::: Proof
Writing everything out component-wise reduces to the product rule and chain rule for scalar functions. For example, the inner product is $$\mathbf{u} \cdot \mathbf{v} = \sum_i u_i v_i$$, so $$(\mathbf{u} \cdot \mathbf{v})' = \sum_i (u_i' v_i + u_i v_i') = \mathbf{u}' \cdot \mathbf{v} + \mathbf{u} \cdot \mathbf{v}'$$, and the cross product and scalar multiplication can be shown in the same way since each component is a sum of products of the form $$u_i v_j$$. The composition is applying [§Differentiation Rules, ⁋Theorem 4](/en/math/calculus/differentiation_rules#thm4) to each component.
:::

One useful corollary of this proposition is that if $$\lVert \mathbf{u}(t)\rVert$$ is constant then $$\mathbf{u} \cdot \mathbf{u} = \lVert \mathbf{u}\rVert^2$$ is also constant, so $$(\mathbf{u} \cdot \mathbf{u})' = 2 \mathbf{u} \cdot \mathbf{u}' = 0$$, that is, $$\mathbf{u} \perp \mathbf{u}'$$. In other words, the rate of change of a vector of constant length is always perpendicular to that vector, and the fact that in circular motion the position vector and velocity are perpendicular is a special case of this fact.

## Velocity and Acceleration

As we saw above, vector functions are a good tool for representing physical phenomena. We now explain that physical intuition.

::: Definition 4
For a curve $$\mathbf{r}(t)$$, we call $$\mathbf{r}'(t)$$ the *velocity*, its magnitude $$\lVert \mathbf{r}'(t)\rVert$$ the *speed*, and $$\mathbf{r}''(t)$$ the *acceleration*. At a point where $$\mathbf{r}'(t) \neq 0$$,

$$\mathbf{T}(t) = \frac{\mathbf{r}'(t)}{\lVert \mathbf{r}'(t)\rVert}$$

is called the *unit tangent vector*.
:::

Velocity points in the direction of the curve's progression and its magnitude is how fast the point is moving, and the unit tangent vector is what remains after keeping only the direction of the velocity. The condition for this to be well defined is that the parametrized curve $$\mathbf{r}$$ is a *$$C^1$$-regular curve*, which means a curve satisfying both of the following two conditions.

1. $$\mathbf{r}$$ is *$$C^1$$*. That is, the velocity vector $$\mathbf{r}'(t)$$ exists continuously.
2. $$\mathbf{r}$$ is *regular*. That is, there is no point where $$\mathbf{r}'(t)$$ becomes $$0$$.

Then in particular by the second condition the unit tangent vector $$\mathbf{T}$$ is well defined everywhere, and by the first condition $$\mathbf{T}(t)$$ is continuous. In this post, unless otherwise stated, we treat $$C^1$$-regular curves as the default.

Given a moving object, one of the things we are curious about is the distance traveled during a time interval. This can be obtained, as in one dimension, by integrating the velocity vector, and more rigorously by approximating the curve with a polygon connecting points on the curve, creating for a partition

$$a = t_0 < \cdots < t_m = b$$

the sum of line segment lengths

$$\sum_k \lVert \mathbf{r}(t_k) - \mathbf{r}(t_{k-1})\rVert$$

and showing that as the partition is refined this converges to a Riemann sum for $$\lVert \mathbf{r}'(t)\rVert$$; compressing this process yields the following definition.

::: Definition 5
The *arc length* of a $$C^1$$ curve $$\mathbf{r}\colon [a, b] \to \mathbb{R}^n$$ is

$$L = \int_a^b \lVert \mathbf{r}'(t)\rVert \mathop{dt}$$
:::

The integrand $$\lVert \mathbf{r}'(t)\rVert$$ is continuous so it is integrable ([§Integration, ⁋Theorem 10](/en/math/calculus/integration#thm10)). We now call the arc length measured from the starting point

$$s(t) = \int_a^t \lVert \mathbf{r}'(\tau)\rVert \mathop{d\tau}$$

the *arc length*, and by the fundamental theorem of calculus $$s'(t) = \lVert \mathbf{r}'(t)\rVert > 0$$, so $$s$$ is an increasing function and we can solve for $$t$$ in terms of $$s$$ to reparametrize the curve by arc length.

::: Proposition 6
When a curve is parametrized by arc length $$s$$, it has unit speed. That is, $$\lVert d\mathbf{r}/ds\rVert = 1$$.
:::

::: Proof
By the chain rule $$d\mathbf{r}/\mathop{dt} = (d\mathbf{r}/ds)(ds/\mathop{dt})$$ and $$ds/\mathop{dt} = \lVert \mathbf{r}'(t)\rVert = \lVert d\mathbf{r}/\mathop{dt}\rVert$$, so $$\lVert d\mathbf{r}/ds\rVert = \lVert d\mathbf{r}/\mathop{dt}\rVert / (ds/\mathop{dt}) = 1$$.
:::

The parametrization obtained in this way is called an *arc length parametrization*.

## Curvature

How much a curve bends is measured by how quickly the direction of the unit tangent vector changes as the curve progresses. However, if the curve moves quickly then the rate of change will also increase, so to examine how much the shape of the curve is bent we must normalize this rate equally. Also, intuitively this is obtained by differentiating the unit tangent vector obtained from differentiating the original curve once more, so we now need to consider a *$$C^2$$* curve. That is, the acceleration vector $$\mathbf{r}''(t)$$ must also exist continuously.

::: Definition 7
The *curvature* of a $$C^2$$-regular curve is the magnitude of the rate at which the unit tangent vector changes with respect to arc length

$$\kappa = \left\lVert \frac{d\mathbf{T}}{ds}\right\rVert$$

When $$d\mathbf{T}/ds \neq 0$$, the unit vector in that direction

$$\mathbf{N} = \frac{d\mathbf{T}/ds}{\lVert d\mathbf{T}/ds\rVert}$$

is called the *unit normal vector*.
:::

Note that by [Proposition 6](#prop6), $$\mathbf{T} = d\mathbf{r}/ds$$ is a unit vector. Then by the observation made just after [Proposition 3](#prop3), that the rate of change of a vector of constant length is perpendicular to that vector, we have $$d\mathbf{T}/ds \perp \mathbf{T}$$. That is, the unit normal vector $$\mathbf{N}$$ is always perpendicular to the tangent, and points to the inside where the curve is bending.

The above definition is for curves in general $$n$$-dimensional space, but in three-dimensional space the cross product allows us to compute this more conveniently. In particular, the following formula can be applied directly without arc length parametrization, which is much more convenient.

::: Proposition 8 (Curvature Formula)
The curvature of a $$C^2$$-regular curve $$\mathbf{r}(t)$$ in three-dimensional space is

$$\kappa = \frac{\lVert \mathbf{r}' \times \mathbf{r}''\rVert}{\lVert \mathbf{r}'\rVert^3}$$

and in particular the curvature of a plane curve $$y = f(x)$$ is

$$\kappa = \frac{\lvert f''\rvert}{(1 + f'^2)^{3/2}}$$
:::

::: Proof
Let $$v = \lVert \mathbf{r}'\rVert = ds/\mathop{dt}$$, then $$\mathbf{r}' = v\mathbf{T}$$. By the product rule

$$\mathbf{r}'' = v'\mathbf{T} + v\mathbf{T}'(t)$$

and by the chain rule $$\mathbf{T}'(t) = (d\mathbf{T}/ds)v$$ and $$\lVert d\mathbf{T}/ds\rVert = \kappa$$ we have $$\mathbf{T}'(t) = \kappa v\mathbf{N}$$. Therefore

$$\mathbf{r}' \times \mathbf{r}'' = (v\mathbf{T}) \times (v'\mathbf{T} + \kappa v^2\mathbf{N}) = v^3 \kappa(\mathbf{T} \times \mathbf{N})$$

Here the second equality is obtained from $$\mathbf{T}\times \mathbf{T}=0$$. Now since $$\mathbf{T} \perp \mathbf{N}$$ and both are unit vectors, $$\lVert \mathbf{T} \times \mathbf{N}\rVert = 1$$, so

$$\lVert \mathbf{r}' \times \mathbf{r}''\rVert = v^3 \kappa = \lVert \mathbf{r}'\rVert^3 \kappa$$

giving the desired equality. The formula for a plane curve $$y = f(x)$$ is obtained by setting $$\mathbf{r}(x) = (x, f(x),0)$$ and applying the three-dimensional formula directly.
:::

The expression $$\mathbf{r}'' = v'\mathbf{T} + \kappa v^2\mathbf{N}$$, obtained by differentiating $$\mathbf{r}' = v\mathbf{T}$$ once more as it appeared in the proof, is itself deeply meaningful. It is the decomposition of acceleration into tangential and normal components. Let us record this as a separate proposition.

::: Proposition 9 (Decomposition of Acceleration)
The acceleration of a $$C^2$$-regular curve decomposes as

$$\mathbf{r}'' = \frac{dv}{\mathop{dt}}\mathbf{T} + \kappa v^2\mathbf{N}$$

where $$v = \lVert \mathbf{r}'\rVert$$ is the speed.
:::

The tangential component $$dv/\mathop{dt}$$ tells us how much the speed is changing, and the normal component $$\kappa v^2$$ tells us how much the direction is bending. If the motion is uniform then $$dv/\mathop{dt} = 0$$, so the acceleration is purely in the normal direction, that is, purely centripetal acceleration, and its magnitude is $$\kappa v^2$$.

::: Example 10 (Helix)
For the helix $$\mathbf{r}(t) = (\cos t, \sin t, t)$$, we have $$\mathbf{r}'(t) = (-\sin t, \cos t, 1)$$ and $$\mathbf{r}''(t) = (-\cos t, -\sin t, 0)$$. The cross product is

$$\mathbf{r}' \times \mathbf{r}'' = (\sin t,\ -\cos t,\ 1), \qquad \lVert \mathbf{r}' \times \mathbf{r}''\rVert = \sqrt{2}$$

and since $$\lVert \mathbf{r}'\rVert = \sqrt{2}$$, the curvature is $$\kappa = \sqrt{2}/(\sqrt{2})^3 = 1/2$$, which is constant. Since the speed $$v = \sqrt{2}$$ is constant, by [Proposition 9](#prop9) the acceleration is purely normal and its magnitude is $$\kappa v^2 = (1/2)\cdot 2 = 1$$, and indeed $$\lVert \mathbf{r}''(t)\rVert = \lVert(-\cos t, -\sin t, 0)\rVert = 1$$, which matches.
:::
