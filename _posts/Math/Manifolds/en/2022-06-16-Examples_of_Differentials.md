---
title: "Examples of Differentials"
description: "We define curves and velocity vectors on a manifold, and examine through concrete examples how the differential of a given function transforms tangent vectors. We show that in Euclidean space this concept coincides with ordinary differentiation."
excerpt: "Examples of smooth functions and differentials"

categories: [Math / Manifolds]
permalink: /en/math/manifolds/examples_of_differentials
sidebar: 
    nav: "manifolds-en"

date: 2022-06-16
weight: 6
translated_at: 2026-06-01T06:00:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-19T23:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
In the previous post we studied differentials in depth; now we examine examples of this.

## Curves and Velocity Vectors on Manifolds

::: Definition 1
For a manifold $M$, we call a $C^\infty$ function $\gamma:(a,b)\rightarrow M$ defined on $M$ a $C^\infty$ curve, and for any $t\in (a,b)$, we call

$$\dd{\gamma_t}\left(\frac{d}{\dd{r}}\bigg\vert_t\right)$$

the *velocity vector* of this curve at the point $\gamma(t)$, and denote it by $\gamma'(t)$.
:::

The vector $\gamma'(t)$, as an element of $T_{\gamma(t)}M$, acts on each element of $\mathcal{C}^\infty_{M,\gamma(t)}$, $f$; expanding the definition of the differential, one sees that

$$\gamma'(t)f=\dd{\gamma_t}\left(\frac{d}{\dd{r}}\bigg\vert_t\right)f=\frac{d}{\dd{r}}\bigg\vert_t (f\circ\gamma)=\frac{\dd{(f\circ \gamma)}}{\dd{r}}(t)=(f\circ\gamma)'(t)$$

holds.

In fact, when defining $T_pM$, there is no real problem in regarding it as the collection of curves passing through the point $p$ that are $C^\infty$[^1]. We prove the following proposition, which is part of this claim, as it will be used frequently.

::: Proposition 2
Fix a manifold $M$ and a point $p\in M$. For any nonzero $v\in T_pM$, there exists, passing through the point $p$ and having velocity vector at $p$ equal to $v$, a $C^\infty$ curve $\gamma$.
:::
::: Proof
It suffices to find, centered at the point $p$ and satisfying the equation

$$v=\dd{\varphi}^{-1}_{\varphi(p)}\left(\frac{\partial}{\partial r^1}\bigg\vert_0\right)$$

, a coordinate system $(U,\varphi)$. This is because $v$ then becomes the velocity vector of the $C^\infty$ curve

$$\gamma: t\mapsto \varphi^{-1}(t, 0,\cdots, 0)$$

at $t=0$. Note that finding a coordinate system satisfying the above condition is very easy: after choosing an arbitrary coordinate system $(U,\psi)$, one constructs, containing the vector to which $\dd{\psi_p}(v)$ is mapped, a new basis of $\mathbb{R}^n$, and then composes the original $\psi$ with the change of basis thus obtained.
:::

In the special case $M=\mathbb{R}^m$, a basis of $T_{\gamma(t)}M$ is given by

$$\frac{\partial}{\partial r^1}\bigg\vert_{\gamma(t)},\cdots,\frac{\partial}{\partial r^m}\bigg\vert_{\gamma(t)}$$

, so

$$\gamma'(t)=\sum_{i=1}^m\frac{\dd{(r^i\circ \gamma)}}{\dd{r}}(t)\frac{\partial}{\partial r^i}\bigg\vert_{\gamma(t)}=\frac{\dd{\gamma}^1}{\dd{r}}\frac{\partial}{\partial r^1}\bigg\vert_{\gamma(t)}+\cdots+\frac{\dd{\gamma}^m}{\dd{r}}\frac{\partial}{\partial r^m}\bigg\vert_{\gamma(t)}$$

, and since in Euclidean space these $\partial/\partial r^i$ are equal to the $i$th standard basis vectors, this can be regarded as

$$\left(\frac{\dd{\gamma}^1}{\dd{r}},\ldots, \frac{\dd{\gamma}^m}{\dd{r}}\right)$$

. Since this equation is identical to the usual derivative

$$\gamma'(t)=\lim_{h\rightarrow 0}\frac{\gamma(t+h)-\gamma(t)}{h}$$

, we can verify that our defined notions of tangent vector and velocity vector coincide in Euclidean space with the (already familiar) velocity vector of a curve.

Between two manifolds $M,N$, suppose we are given a $C^\infty$ function $F:M\rightarrow N$, and consider a $C^\infty$ function $\gamma:(a,b)\rightarrow M$. Computing the differential of $F\circ\gamma$ at $t$ gives

$$\dd{(F\circ\gamma)_t}=\dd{F_{\gamma(t)}}\circ \dd{\gamma_t}$$

, and therefore

$$\dd{(F\circ\gamma)_t}\left(\frac{d}{\dd{r}}\bigg\vert_t\right)=(\dd{F_{\gamma(t)}}\circ \dd{\gamma_t})\left(\frac{d}{\dd{r}}\bigg\vert_t\right)=\dd{F_{\gamma(t)}}(\gamma'(t))$$

. Since the left-hand side can be regarded, in $N$, as the velocity vector of the $C^\infty$ curve $F\circ\gamma$ at time $t$, the above equation can be written as

$$(F\circ\gamma)'(t)=\dd{F_{\gamma(t)}}(\gamma'(t))$$

.

Modifying this slightly, we see that for a given $C^\infty$ function $F:M\rightarrow N$, in order to determine, for any $v\in T_pM$, the value of the differential $\dd{F_p}(v)$, one only needs to choose any curve having at the point $p$ a velocity vector in the direction of $v$[^2], and for this curve $\gamma$, find the velocity vector of $F\circ\gamma$ at time $t$. That is,

::: Proposition 3
Consider two manifolds $M,N$ and a $C^\infty$ function $F:M\rightarrow N$. For any $v\in T_pM$, satisfying $\gamma(0)=p$ and $\gamma'(0)=v$, a $C^\infty$ curve $\gamma:(a,b)\rightarrow M$ also satisfies the equation

$$\dd{F_p}(v)=(F\circ\gamma)'(0)$$
:::

## Tangent Spaces of Vector Spaces

Earlier, in [§Examples of Differentiable Manifolds, ⁋Example 2](/en/math/manifolds/examples_of_manifolds#ex2){: data-lid="bxjdg" }, we saw that any $m$-dimensional $\mathbb{R}$-vector space $V$ carries an $m$-dimensional manifold structure. Then for any point $x\in V$, the tangent space at the point $x$, $T_xV$, also has the same dimension as the manifold $V$, so $\dim T_xV=m$ holds. Therefore, $V\cong T_xV$ must hold. 

This can essentially be shown by using the fact that in Euclidean space, the standard basis vectors of $\mathbb{R}^m$ and the basis vectors of $T_x\mathbb{R}^m$,

$$\frac{\partial}{\partial r^1}\bigg\vert_x,\cdots,\frac{\partial}{\partial r^m}\bigg\vert_x$$

are the same. In fact, this isomorphism does not depend on the choice of basis, because it is given by associating to each $v\in V$ the directional derivative defined by

$$D_v\vert_x: f\mapsto \lim_{t\rightarrow 0}\frac{f(x+tv)-f(x)}{t}$$

::: Proposition 4
Consider an $m$-dimensional $\mathbb{R}$-vector space $V$ equipped with a manifold structure. For any point of $V$, $x\in V$, there exists an isomorphism $V\cong T_xV$ independent of the choice of basis. Moreover, if $V,W$ are two $\mathbb{R}$-vector spaces and $L:V\rightarrow W$ is a linear map, then the following diagram commutes.

{% diagram Math/Manifolds/Examples_of_Differentials-1.svg width="9.31em" alt="tangent_space_of_vector_space" %}
:::
::: Proof
For the first part, we can use the formula for the directional derivative shown above:

$$(D_v\vert_x)f=\lim_{t\rightarrow 0}\frac{f(x+tv)-f(x)}{t}$$

Under the correspondence $v\mapsto D_v\vert_x$, the vector $v+w$ is sent to

$$\begin{aligned}(D_{v+w}\vert_x)f&=\lim_{t\rightarrow 0}\frac{f(x+t(v+w))-f(x)}{t}\\
&=\lim_{t\rightarrow 0}\left(\frac{f((x+tw)+tv)-f(x+tw)}{t}+\frac{f(x+tw)-f(x)}{t}\right)\\
&=(D_v\vert_x)f+(D_w\vert_x)f
\end{aligned}$$

and similarly $\alpha v$ is obtained from

$$(D_{\alpha v}\vert_x)f=\lim_{t\rightarrow 0}\frac{f(x+t\alpha v)-f(x)}{t}=\alpha\lim_{t\rightarrow 0}\frac{f(x+t\alpha v)-f(x)}{\alpha t}=\alpha(D_v\vert_x)f$$

Therefore, $v\mapsto D_v\vert_x$ is linear. 

That this correspondence is injective can be seen by substituting for the function $f$ each of $x^1,\ldots, x^m$, and since the two vector spaces have the same dimension, this correspondence must be an isomorphism. From the above, we obtain the isomorphism $V\cong T_xV$. 

We now show the second part. Any $v\in V$, following $V\rightarrow W\rightarrow T_{L(x)}W$, is sent to

$$v\mapsto L(v)\mapsto D_{L(v)}\vert_{L(x)}$$

On the other hand, following $V\rightarrow T_xV\rightarrow T_{L(x)}W$, we first obtain from $V\rightarrow T_xV$

$$v\mapsto D_v\vert_x$$

and after that, using $\gamma(t)=x+tv$ and applying [Proposition 3](#prop3){: data-lid="j3yl9" }, we obtain

$$\dd{L_x}(D_v\vert_x)=(L\circ \gamma)'(0)$$

However, since

$$(L\circ\gamma)(t)=L(x+tv)=L(x)+tL(v)$$

$(L\circ\gamma)'(0)$ satisfies, for any $f$,

$$(L\circ\gamma)'(0)f=\lim_{t\rightarrow 0}\frac{f(L(x)+tL(v))-f(L(x))}{t}=(D_{L(v)}\vert_{L(x)})f$$

Therefore, the given diagram commutes.
:::

The isomorphism $V\cong T_xV$ constructed in the proposition above does not depend on the choice of basis, but if, for $V$, some basis $e_1,\ldots, e_m$ and its dual basis $r^1,\ldots, r^m$ are given, one can verify that this isomorphism is given by

$$\sum a_ie_i\leftrightarrow\sum a_i\frac{\partial}{\partial r^i}\bigg\vert_x$$

::: Example 5
The collection of $n\times n$ matrices $\Mat_n(\mathbb{R})$ is an $n^2$-dimensional $\mathbb{R}$-vector space. Therefore, the tangent space at any point of $\Mat_n(\mathbb{R})$ is the same as $\Mat_n(\mathbb{R})$. 

In particular, considering an open submanifold of $\Mat_n(\mathbb{R})$, namely $\GL(n;\mathbb{R})$, the tangent space at any element of $\GL(n;\mathbb{R})$ coincides with the tangent space of that element viewed as an element of $\Mat_n(\mathbb{R})$, and therefore equals $\Mat_n(\mathbb{R})$. 
:::

## Tangent covector

Let an arbitrary manifold $M$ and a $C^\infty$ function $f:M\rightarrow\mathbb{R}$ be given. Then for every point $p\in M$, the differential $\dd{f_p}:T_pM\rightarrow T_{f(p)}\mathbb{R}$ is well-defined. By the preceding [Proposition 4](#prop4){: data-lid="sjvhv" }, as 1-dimensional $\mathbb{R}$-vector spaces, there exists an isomorphism between $\mathbb{R}$ and its tangent space $T_{f(p)}\mathbb{R}$. Then now, via

$$T_pM\overset{\dd{f_p}}{\rightarrow}T_{f(p)}\mathbb{R}\overset{\sim}{\rightarrow}\mathbb{R}$$

we can view $\dd{f_p}$ as an element of $(T_pM)^\ast$.

::: Definition 6
For a manifold $M$ and a point $p\in M$, the dual space of the $\mathbb{R}$-vector space $T_pM$, $(T_pM)^\ast$, is called the *cotangent space*, written simply as $T_p^\ast M$. The elements of $T_p^\ast M$ are called *tangent covectors*, or simply *covectors*.
:::

Therefore, the preceding discussion can be summarized as saying that any $C^\infty$ function $f:M\rightarrow\mathbb{R}$ determines a tangent covector.

Meanwhile, $T_p^\ast M$ is the dual space of the vector space $T_pM$, and since $T_pM$ is a finite-dimensional $\mathbb{R}$-vector space, bases of $T_pM$ define a *dual basis* of $T_p^\ast M$. 

Let $(U,\varphi)$ be a coordinate system containing the point $p$, and let $\varphi=(x^i)_{i=1}^m$. Then the following $m$ tangent vectors

$$\frac{\partial}{\partial x^1}\bigg\vert_p,\cdots\frac{\partial}{\partial x^m}\bigg\vert_p$$

form a basis of $T_pM$. Let us temporarily denote their dual basis by $\xi^i \vert_p$. That is, $\xi^i \vert_p$ is a linear map from $T_pM$ to $\mathbb{R}$, uniquely defined by the formula

$$(\xi^i \vert_p)\left(\frac{\partial}{\partial x^j}\bigg\vert_p\right)=\delta_{ij}\tag{1}$$

where $\delta_{ij}$ denotes the Kronecker delta. 

::: Proposition 7
In the above situation, $\xi^i\vert_p=\dd{x}^i\vert_p$. That is, arising from $(U,\varphi)$, the dual basis elements of $T_pM$, $(\xi^i \vert_p)$, are in fact equal to the differentials of the coordinate functions $x^i$ at the point $p$.
:::
::: Proof
It suffices to show that the $\dd{x}^i$ satisfy equation (1) above. By definition,

$$\dd{x}^i\vert_p\left(\frac{\partial}{\partial x^j}\bigg\vert_p\right)=\frac{\partial}{\partial x^j}\bigg\vert_p x^i=\delta_{ij}$$

holds. 
:::

The above proof becomes more plausible if we recall [§Cotangent Space, ⁋Lemma 1](/en/math/manifolds/cotangent_space#lem1){: data-lid="urxro" }, which we proved when we first introduced the tangent space. That is, passing from the first equality to the second expression is the definition of the differential $\dd{x}^i\vert_p$, but at the same time, via

$$T_p^\ast M\cong (\mathfrak{m}_p/\mathfrak{m}_p^2)^{\ast\ast}\cong\mathfrak{m}_p/\mathfrak{m}^2_p$$

it is also the process of naturally identifying the double dual of the finite-dimensional $\mathbb{R}$-vector space $\mathfrak{m}_p/\mathfrak{m}^2_p$ with itself.

---

**References**

**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013  
**[Lee]** John M. Lee. *Introduction to Smooth Manifolds*, Graduate texts in mathematics, Springer, 2012

---

[^1]: More precisely, curves having the same velocity vector at the point $p$ should be treated as identical to give an equivalence relation.
[^2]: By [Proposition 2](#prop2){: data-lid="ywv6h" }, at least one such curve exists.
