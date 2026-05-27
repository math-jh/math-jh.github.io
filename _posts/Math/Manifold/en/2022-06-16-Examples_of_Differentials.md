---
title: "Examples of Differentials"
excerpt: "Examples of smooth functions and differentials"

categories: [Math / Manifold]
permalink: /en/math/manifold/examples_of_differentials
header:
    overlay_image: /assets/images/Math/Manifold/Examples_of_Differentials.png
    overlay_filter: 0.5
sidebar: 
    nav: "manifold-en"

date: 2022-06-16
last_modified_at: 2022-06-16
weight: 6
translated_at: 2026-05-28T11:36:15+00:00
translation_source: kimi-cli
---
In the previous post we studied differentials in depth, and now we look at some examples.

## Curves and Velocity Vectors on Manifolds

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> For a manifold $$M$$, we call a $$C^\infty$$ function $$\gamma:(a,b)\rightarrow M$$ a $$C^\infty$$ curve defined on $$M$$, and for any $$t\in (a,b)$$ we call

$$d\gamma_t\left(\frac{d}{dr}\bigg|_t\right)$$

the *velocity vector* of this curve at the point $$\gamma(t)$$, and denote it by $$\gamma'(t)$$.

</div>

As an element of $$T_{\gamma(t)}M$$, the vector $$\gamma'(t)$$ acts on each element $$f$$ of $$\mathcal{C}^\infty_{M,\gamma(t)}$$, and writing out the definition of the differential we see that

$$\gamma'(t)f=d\gamma_p\left(\frac{d}{dr}\bigg|_t\right)f=\frac{d}{dr}\bigg|_t (f\circ\gamma)=\frac{d(f\circ \gamma)}{dr}(t)=(f\circ\gamma)'(t)$$

holds.

In fact, when defining $$T_pM$$, we may just as well think of it as the collection of $$C^\infty$$ curves passing through the point $$p$$[^1]. We give a proof of the following proposition, which is part of this claim and will be used frequently.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> Fix a manifold $$M$$ and a point $$p\in M$$. For any nonzero $$v\in T_pM$$, there exists a $$C^\infty$$ curve $$\gamma$$ passing through the point $$p$$ whose velocity vector at $$p$$ is $$v$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

We only need to find a coordinate system $$(U,\varphi)$$ centered at $$p$$ satisfying the equation

$$v=d\varphi^{-1}_{\varphi(p)}\left(\frac{\partial}{\partial r^1}\bigg|_0\right)$$

Then $$v$$ becomes the velocity vector at $$t=0$$ of the $$C^\infty$$ curve

$$\gamma: t\mapsto \varphi^{-1}(t, 0,\cdots, 0)$$

Incidentally, finding a coordinate system satisfying the above condition is very easy: choose an arbitrary coordinate system $$(U,\psi)$$, then construct a new basis of $$\mathbb{R}^n$$ containing the translated vector $$d\psi_p(v)$$, and compose the original $$\psi$$ with the resulting change of basis.

</details>

In the special case $$M=\mathbb{R}^m$$, a basis of $$T_{\gamma(t)}M$$ is given by

$$\frac{\partial}{\partial r^1}\bigg|_{\gamma(t)},\cdots,\frac{\partial}{\partial r^m}\bigg|_{\gamma(t)}$$

so

$$\gamma'(t)=\sum_{i=1}^m\frac{d(r^i\circ \gamma)}{dr}(t)\frac{\partial}{\partial r^i}\bigg|_{\gamma(t)}=\frac{d\gamma^1}{dr}\frac{\partial}{\partial r^1}\bigg|_{\gamma(t)}+\cdots+\frac{d\gamma^m}{dr}\frac{\partial}{\partial r^m}\bigg|_{\gamma(t)}$$

and since in Euclidean space these $$\partial/\partial r^i$$ coincide with the $$i$$th standard basis, we may think of this as

$$\left(\frac{d\gamma^1}{dr},\ldots, \frac{d\gamma^m}{dr}\right)$$

This is identical to the usual derivative

$$\gamma'(t)=\lim_{h\rightarrow 0}\frac{\gamma(t+h)-\gamma(t)}{h}$$

so we can verify that the notions of tangent vector and velocity vector we defined agree in Euclidean space with the (previously known) velocity vector of a curve.

Suppose we are given a $$C^\infty$$ function $$F:M\rightarrow N$$ between two manifolds $$M,N$$, and consider a $$C^\infty$$ function $$\gamma:(a,b)\rightarrow M$$. Then computing the differential of $$F\circ\gamma$$ at $$t$$ gives

$$d(F\circ\gamma)_t=dF_{\gamma(t)}\circ d\gamma_t$$

and therefore

$$d(F\circ\gamma)_t\left(\frac{d}{dr}\bigg|_t\right)=(dF_{\gamma(t)}\circ d\gamma_t)\left(\frac{d}{dr}\bigg|_t\right)=dF_{\gamma(t)}(\gamma'(t))$$

Since the left-hand side can be regarded as the velocity vector at time $$t$$ of the $$C^\infty$$ curve $$F\circ\gamma$$ in $$N$$, the above equation can be written as

$$(F\circ\gamma)'(t)=dF_{\gamma(t)}(\gamma'(t))$$

Modifying this slightly, for a given $$C^\infty$$ function $$F:M\rightarrow N$$, we can see that in order to know the value $$dF_p(v)$$ of the differential at any $$v\in T_pM$$, we may simply choose any curve having velocity vector in the $$v$$ direction at the point $$p$$[^2], and then compute the velocity vector of $$F\circ\gamma$$ at time $$t$$ for this curve $$\gamma$$. That is,

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> Consider two manifolds $$M,N$$ and a $$C^\infty$$ function $$F:M\rightarrow N$$. For any $$v\in T_pM$$, any $$C^\infty$$ curve $$\gamma:(a,b)\rightarrow M$$ satisfying $$\gamma(0)=p$$ and $$\gamma'(0)=v$$ also satisfies the equation

$$dF_p(v)=(F\circ\gamma)'(0)$$

</div>

## Tangent Spaces of Vector Spaces

In [§Examples of Differentiable Manifolds, ⁋Example 2](/en/math/manifold/examples_of_manifolds#ex2), we saw that any $$m$$-dimensional $$\mathbb{R}$$-vector space $$V$$ has the structure of an $$m$$-dimensional manifold. Then for any point $$x\in V$$, the tangent space $$T_xV$$ at $$x$$ has the same dimension as the manifold $$V$$, so $$\dim T_xV=m$$ holds. Therefore we must have $$V\cong T_xV$$.

This can be shown using the fact that in Euclidean space, the standard vectors of $$\mathbb{R}^m$$ and the bases

$$\frac{\partial}{\partial r^1}\bigg|_x,\cdots,\frac{\partial}{\partial r^m}\bigg|_x$$

of $$T_x\mathbb{R}^m$$ are essentially the same. In fact, this isomorphism does not depend on the choice of basis: for any $$v\in\mathbb{R}^m$$, it is the correspondence with the directional derivative

$$D_v|_x: f\mapsto \lim_{h\rightarrow 0}\frac{f(x+tv)-f(x)}{t}$$

that gives this isomorphism.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> Consider an $$m$$-dimensional $$\mathbb{R}$$-vector space $$V$$ equipped with a manifold structure. For any point $$x\in V$$, there exists an isomorphism $$V\cong T_xV$$ that is independent of the choice of basis. Moreover, if $$V,W$$ are two $$\mathbb{R}$$-vector spaces and $$L:V\rightarrow W$$ is a linear map, then the following diagram commutes.

![tangent_space_of_vector_space](/assets/images/Math/Manifold/Examples_of_Differentials-1.png){:width="198.9px" class="invert" .align-center}

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

For the first part, we use the directional derivative formula shown above,

$$(D_v|_x)f=\lim_{t\rightarrow 0}\frac{f(x+tv)-f(x)}{t}$$

Under the correspondence $$v\mapsto D_v\vert_x$$, the vector $$v+w$$ is sent to

$$\begin{aligned}(D_{v+w}|_x)f&=\lim_{t\rightarrow 0}\frac{f(x+t(v+w))-f(x)}{t}\\
&=\lim_{t\rightarrow 0}\left(\frac{f((x+tw)+tv)-f(x+tw)}{t}+\frac{f(x+tv)-f(x)}{t}\right)\\
&=(D_v|_x)f+(D_w|_x)f
\end{aligned}$$

and similarly $$\alpha v$$ yields

$$(D_{\alpha v}|_x)f=\lim_{t\rightarrow 0}\frac{f(x+t\alpha v)-f(x)}{t}=\alpha\lim_{t\rightarrow 0}\frac{f(x+t\alpha v)-f(x)}{\alpha t}=\alpha(D_v|_x)f$$

Therefore $$v\mapsto D_v\vert_x$$ is linear.

That this correspondence is injective can be seen by plugging in $$x^1,\ldots, x^m$$ for $$f$$, and since the two vector spaces have the same dimension, this correspondence must be an isomorphism. Thus we obtain the isomorphism $$V\cong T_xV$$.

We must show the second part. Following $$V\rightarrow W\rightarrow T_{L(x)}W$$, any $$v\in V$$ is sent to

$$v\mapsto L(v)\mapsto D_{L(v)}|_{L(x)}$$

On the other hand, following $$V\rightarrow T_xV\rightarrow T_{L(x)}W$$, we first obtain

$$v\mapsto D_v|_x$$

via $$V\rightarrow T_xV$$, and then using $$\gamma(t)=x+tv$$ and [Proposition 3](#prop3) we get

$$dL_x(D_v|_x)=(L\circ \gamma)'(0)$$

But

$$(L\circ\gamma)(t)=L(x+tv)=L(x)+tL(v)$$

so for any $$f$$, $$(L\circ\gamma)'(0)$$ satisfies

$$(L\circ\gamma)'(0)f=\lim_{t\rightarrow 0}\frac{f(L(x)+tL(v))-f(L(x))}{t}=(D_{L(v)}|_{L(x)})f$$

Therefore the given diagram commutes.

</details>

The isomorphism $$V\cong T_xV$$ constructed in the above proposition does not depend on the choice of basis, but if a basis $$e_1,\ldots, e_n$$ of $$V$$ and its dual basis $$r^1,\ldots, r^n$$ are given, then one can check that this isomorphism is given by

$$\sum a_ie_i\leftrightarrow\sum a_i\frac{\partial}{\partial r^i}$$

<div class="example" markdown="1">

<ins id="ex5">**Example 5**</ins> The collection $$\Mat_n(\mathbb{R})$$ of $$n\times n$$ matrices is an $$n^2$$-dimensional $$\mathbb{R}$$-vector space. Therefore, the tangent space at any point of $$\Mat_n(\mathbb{R})$$ is the same as $$\Mat_n(\mathbb{R})$$.

In particular, considering the open submanifold $$\GL(n,\mathbb{R})$$ of $$\Mat_n(\mathbb{R})$$, the tangent space at any element of $$\GL(n,\mathbb{R})$$ is the same as the tangent space of that element viewed as an element of $$\Mat_n(\mathbb{R})$$, and hence equals $$\Mat_n(\mathbb{R})$$.

</div>

## Tangent Covectors

Suppose we are given an arbitrary manifold $$M$$ and a $$C^\infty$$ function $$f:M\rightarrow\mathbb{R}$$. Then for every point $$p\in M$$, the differential $$df_p:T_pM\rightarrow T_{f(p)}\mathbb{R}$$ is well defined. By [Proposition 4](#prop4), there exists an isomorphism between $$\mathbb{R}$$ and its tangent space $$T_{f(p)}\mathbb{R}$$ as 1-dimensional $$\mathbb{R}$$-vector spaces. Thus, via

$$T_pM\overset{df_p}{\longrightarrow}T_{f(p)}\mathbb{R}\overset{\sim}{\longrightarrow}\mathbb{R}$$

we may regard $$df_p$$ as an element of $$(T_pM)^\ast$$.

<div class="definition" markdown="1">

<ins id="def6">**Definition 6**</ins> For a manifold $$M$$ and a point $$p\in M$$, the dual space $$(T_pM)^\ast$$ of the $$\mathbb{R}$$-vector space $$T_pM$$ is called the *cotangent space*, and is written simply as $$T_p^\ast M$$. The elements of $$T_p^\ast M$$ are called *tangent covectors*, or simply *covectors*.

</div>

Therefore, the preceding discussion can be summarized as saying that any $$C^\infty$$ function $$f:M\rightarrow\mathbb{R}$$ determines a tangent covector.

Meanwhile, $$T_p^\ast M$$ is the dual space of the vector space $$T_pM$$, and since $$T_pM$$ is a finite-dimensional $$\mathbb{R}$$-vector space, any basis of $$T_pM$$ defines a *dual basis* of $$T_p^\ast M$$.

Let $$(U,\varphi)$$ be a coordinate system containing the point $$p$$, and write $$\varphi=(x^i)_{i=1}^m$$. Then the following $$m$$ tangent vectors

$$\frac{\partial}{\partial x^1}\bigg|_p,\cdots\frac{\partial}{\partial x^m}\bigg|_p$$

form a basis of $$T_pM$$. Let us temporarily denote their dual basis by $$\xi^i \vert_p$$. That is, $$\xi^i \vert_p$$ is a linear map from $$T_pM$$ to $$\mathbb{R}$$, uniquely defined by the formula

$$(\xi^i |_p)\left(\frac{\partial}{\partial x^j}\bigg|_p\right)=\delta_{ij}\tag{1}$$

Here $$\delta_{ij}$$ denotes the Kronecker delta.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> In the situation above, $$\xi^i\vert_p=dx^i\vert_p$$. In other words, the dual bases $$(\xi^i \vert_p)$$ of $$T_pM$$ arising from $$(U,\varphi)$$ are in fact the differentials at the point $$p$$ of the coordinate functions $$x^i$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

It suffices to show that the $$dx^i$$ satisfy equation (1) above. By definition,

$$dx^i|_p\left(\frac{\partial}{\partial x^j}\bigg|_p\right)=\frac{\partial}{\partial x^j}\bigg|_p x^i=\delta_{ij}$$

holds.

</details>

This proof becomes more convincing if we recall [§Cotangent Space, ⁋Lemma 1](/en/math/manifold/cotangent_space#lem1), which we proved when we first introduced the tangent space. That is, passing from the first equality to the second is by definition of the differential $$dx^i\vert_p$$, but at the same time it is the process of naturally identifying the double dual of the finite-dimensional $$\mathbb{R}$$-vector space $$\mathfrak{m}_p/\mathfrak{m}^2_p$$ with itself via

$$T_p^\ast M\cong (\mathfrak{m}_p/\mathfrak{m}_p^2)^{\ast\ast}\cong\mathfrak{m}_p/\mathfrak{m}^2_p$$

---

**References**

**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013  
**[Lee]** John M. Lee. *Introduction to Smooth Manifolds*, Graduate texts in mathematics, Springer, 2012  

---

[^1]: More precisely, we must give an equivalence relation by treating curves having the same velocity vector at the point $$p$$ as identical.
[^2]: By [Proposition 2](#prop2), at least one such curve exists.
