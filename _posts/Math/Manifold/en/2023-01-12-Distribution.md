---
title: "Distribution"
description: "This post defines distributions on manifolds and the concept of integral submanifolds, then explains how Frobenius's theorem characterizes integrable distributions through the involutivity condition."
excerpt: "The definition of a distribution and the Frobenius theorem"

categories: [Math / Manifold]
permalink: /en/math/manifold/distribution
header:
    overlay_image: /assets/images/Math/Manifold/Distribution.png
    overlay_filter: 0.5
sidebar: 
    nav: "manifold-en"

date: 2023-01-12
last_modified_at: 2023-01-12
weight: 14
translated_at: 2026-06-01T10:00:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-01T10:00:04+00:00
---
## Distribution and Integral Flow

Previously, in [§Vector Fields](/en/math/manifold/vector_fields), we saw that for any smooth vector field $$X$$ defined on a given manifold $$M$$, there exists a sufficiently small $$\epsilon>0$$ such that there is a curve $$\sigma:(-\epsilon,\epsilon)\rightarrow M$$ satisfying

$$\sigma'(t)=X(\sigma(t)),\qquad \sigma(0)=p\tag{1}$$

The image $$S$$ of such a curve $$\sigma$$ in $$M$$ can be viewed as a submanifold of $$M$$ containing the point $$p$$.

On the other hand, equation (1) determines not only the image of $$\sigma$$ but also its parametrization. In contrast, the submanifold $$S$$ is determined independently of the parametrization of $$\sigma$$, so it is determined solely by the 1-dimensional subspace $$\span(X_p)$$ of $$T_pM$$, rather than by the vector $$X_p$$ itself.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Let $$M$$ be an $$m$$-dimensional manifold, and let $$k$$ be an integer with $$1\leq k\leq m$$. A function assigning to each $$p\in M$$ a $$k$$-dimensional subspace $$\mathcal{D}(p)$$ of $$T_pM$$ is called a *$$k$$-dimensional distribution*.

A $$k$$-dimensional distribution $$\mathcal{D}$$ is said to be $$C^\infty$$ if for each $$p\in M$$ there exists a suitable open neighborhood $$U$$ and smooth vector fields $$X_1,\ldots, X_k$$ defined on it such that for each $$x\in U$$,

$$\mathcal{D}(x)=\span\{(X_1)_x,\ldots, (X_k)_x\}$$

holds.

</div>

As we saw above, a vector field $$X$$ defines a 1-dimensional distribution via the map $$p\mapsto\span(X_p)\subseteq T_pM$$. Then the submanifold $$S$$ is characterized by the condition

$$T_xS=\mathcal{D}(x)\qquad\text{for all $x$}$$

We therefore make the following definition.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> For a $$k$$-dimensional distribution $$\mathcal{D}$$ defined on $$M$$, a manifold $$S$$ satisfying

$$T_xS=\mathcal{D}(x)\qquad\text{for all $x$}$$

is called an *integral manifold* of $$\mathcal{D}$$.

</div>

If for each $$p\in M$$ there exists an integral manifold containing $$p$$, then $$\mathcal{D}$$ is called an *integrable* distribution.

## Frobenius Theorem

The following theorem is well known.

<div class="proposition" markdown="1">

<ins id="thm3">**Theorem 3 (Frobenius)**</ins> Let $$\mathcal{D}$$ be a $$k$$-dimensional distribution defined on a manifold $$M$$. Then $$\mathcal{D}$$ is integrable if and only if $$[X,Y]\in\mathcal{D}$$ holds for any $$X,Y\in\mathcal{D}$$.

Moreover, for any $$k$$-dimensional involutive distribution the following hold:

1. For each $$p\in M$$, there exists an integral manifold of $$\mathcal{D}$$ containing $$p$$.
2. Furthermore, by choosing a coordinate system $$(U,\varphi)$$ centered at $$p$$ appropriately, the slices defined by the equations
    
    $$x_i=\text{constant},\qquad i>k$$

   can be made to be integral manifolds of $$\mathcal{D}$$.
3. Finally, if $$\Phi:N\rightarrow M$$ is a connected integral manifold and $$\Phi(N)\subseteq U$$, then $$\Phi(N)$$ is contained in exactly one of the slices from (2).

</div>

A distribution satisfying the latter condition is called *involutive*. Therefore, the Frobenius theorem may be summarized by saying that a distribution $$\mathcal{D}$$ is integrable if and only if it is involutive.

One direction of this theorem can be proved quite easily.

<div class="proposition" markdown="1">

<ins id="lem4">**Lemma 4**</ins> Let $$\mathcal{D}$$ be a smooth distribution defined on a manifold $$M$$. If $$\mathcal{D}$$ is integrable, then $$\mathcal{D}$$ is an involutive distribution.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$X,Y\in\mathcal{D}$$ and pick a point $$p\in M$$. We must show that $$[X,Y]_p\in\mathcal{D}(p)$$.

Since $$\mathcal{D}$$ is an integrable distribution, there exists an integral submanifold $$\Phi:S\rightarrow M$$ of $$\mathcal{D}$$ containing $$p$$. Let $$s\in S$$ be a point satisfying $$\Phi(s)=p$$. For any $$x\in S$$,

$$d\Phi_x:T_xS\rightarrow\mathcal{D}(\Phi(x))$$

is an isomorphism, so we can find two vector fields $$\tilde{X},\tilde{Y}$$ satisfying

$$d\Phi_s(\tilde{X}_s)=X_p,\qquad d\Phi_s(\tilde{Y}_s)=Y_p.$$

Then these vector fields are $$\Phi$$-related to $$X$$ and $$Y$$ respectively, so by [§Lie Derivative, ⁋Proposition 9](/en/math/manifold/Lie_derivative#prop9), $$[\tilde{X},\tilde{Y}]$$ is $$\Phi$$-related to $$[X,Y]$$. Therefore

$$[X,Y]_p=d\Phi_s([\tilde{X},\tilde{Y}]_s)\in\mathcal{D}(p)$$

holds.

</details>

Thus, the difficult part of the proof of [Theorem 3](#thm3) is the converse direction. This proceeds by induction on the dimension $$k$$ of the distribution.

<div class="proposition" markdown="1">

<ins id="lem5">**Lemma 5**</ins> Let $$M$$ be an $$m$$-dimensional manifold, $$p\in M$$ a point, and $$X$$ a vector field satisfying $$X_p\neq 0$$. Then there exists a suitable coordinate system $$(U,\varphi)$$ containing $$p$$, with $$\varphi=(x^1,\ldots, x^m)$$, such that

$$X|_U=\frac{\partial}{\partial x^1}\bigg|_U$$

holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Choose a coordinate system $$(V,\tau)$$ centered at $$p$$, with $$\tau=(y^1,\ldots, y^m)$$, such that

$$X_p=\frac{\partial}{\partial y^1}\bigg|_p$$

holds. Without loss of generality, we may assume that $$V$$ is sufficiently small so that for a suitable $$\epsilon>0$$ the map

$$(-\epsilon,\epsilon)\times V\rightarrow M;\qquad(t,q)\mapsto X_t(q)$$

is a well-defined $$C^\infty$$ map. ([§Vector Fields, ⁋Theorem 6](/en/math/manifold/vector_fields#thm6)) Moreover, if we choose $$\epsilon>0$$ small enough that the inclusion

$$(-\epsilon,\epsilon)\times W\subseteq V,\qquad \text{$W$ is an open neighborhood of the origin in $\mathbb{R}^{d-1}$}$$

holds, then the map

$$\sigma: (-\epsilon,\epsilon)\times W;\qquad (t,a^2,\ldots, a^d)\mapsto \phi^t(\tau^{-1}(0,a^2,\ldots, a^d))$$

is well-defined. Now,

$$d\sigma\left(\frac{\partial}{\partial r^1}\bigg|_0\right)=\frac{\partial}{\partial y^1}\bigg|_p=X_p\neq 0,\qquad d\sigma\left(\frac{\partial}{\partial r^i}\bigg|_0\right)=\frac{\partial}{\partial y^i}\bigg|_p$$

so $$\sigma$$ is nonsingular at the origin, and hence $$\sigma^{-1}$$ defines a coordinate map.

</details>

<details class="proof--alone" markdown="1">
<summary>Proof of Theorem 3</summary>

Assume the theorem holds for all $$(k-1)$$-dimensional distributions, and let $$\mathcal{D}$$ be a $$k$$-dimensional distribution. For a point $$p\in M$$, we may assume that $$\mathcal{D}$$ is spanned by $$k$$ vector fields $$X_1,\ldots, X_k$$ in a neighborhood of $$p$$. Now apply [Lemma 5](#lem5) to find a coordinate system $$(V,\tau)$$ centered at $$p$$, with $$\tau=(y^1,\ldots, y^k)$$, such that

$$X_1|_V=\frac{\partial}{\partial y^1}$$

holds.

Define $$k$$ vector fields $$Y_1,\ldots, Y_k$$ by the formulas

$$Y_1=X_1,\qquad Y_i=X_i-(X_i(y^1))X_1\quad(i\geq 2).$$

Since the $$X_i$$ are independent, so are the $$Y_i$$.

Now let $$S$$ be the slice defined by $$y_1=0$$. Then by restricting $$Y_2,\ldots, Y_k$$ to $$S$$ we obtain vector fields

$$Z_i=Y_i|_S \qquad (i\geq 2).$$

Since

$$Z_i(y^1)=Y_i(y^1)=0$$

holds, the $$Z_i$$ are independent vector fields contained in the tangent space of $$S$$. Hence they span a $$(k-1)$$-dimensional distribution on $$S$$.

To use the induction hypothesis, let us show that this distribution is involutive. That is, we must show that $$[Z_i,Z_j]\in\span(Z_2,\ldots, Z_k)$$ for any $$i,j$$.

Consider the inclusion $$\iota:S\rightarrow M$$. Then the $$Z_i$$ are $$\iota$$-related to the $$Y_i$$, so it suffices to show that $$[Y_i,Y_j]\in\span(Y_2,\ldots, Y_k)$$. Now

$$Y_i(y^1)=X_i(y^1)-X_i(y^1)X_1(y^1)=X_i(y^1)-X_i(y^1)=0$$

holds for all $$i$$, and therefore $$[Y_i,Y_j]y^1=0$$. From this we see that the $$[Y_i,Y_j]$$ actually belong to $$\span(Y_2,\ldots, Y_k)$$.

Applying the second assertion of the theorem to the involutive distribution $$\span(Z_2,\ldots, Z_k)$$ on $$S$$, we can choose a coordinate system $$(w^2,\ldots, w^d)$$ centered at $$p\in S$$ so that the slices obtained from the equations

$$w^i=\text{constant},\qquad i>k$$

are integral submanifolds of $$\span(Z_2,\ldots, Z_k)$$.

To complete the proofs of the first and second assertions, define $$k$$ functions

$$x^1=y^1,\quad x^j=w^j\circ\pi$$

where $$\pi:V\rightarrow S$$ is the projection eliminating the $$y_1$$ component. Then the $$(x^i)$$ are independent functions, so we know there exists a coordinate system $$(U,\varphi)$$ having them as component functions. This coordinate system then satisfies the second assertion: the slices defined by

$$x^i=\text{constant},\qquad i>k$$

are integral manifolds of $$\mathcal{D}$$. To see this, it suffices to show that $$Y_i(x^{k+j})=0$$ for all $$x^{k+1},\ldots, x^m$$.

First, from the definition of the $$x^i$$ we know that $$\partial x^j/\partial y^1=\delta_{j1}$$ holds, and therefore on $$U$$ we have

$$Y_1=\frac{\partial}{\partial x^1}.$$

For the remaining $$Y_2,\ldots, Y_k$$, using the formula

$$\frac{\partial}{\partial x^1}Y_i(x^{k+j})=Y_1(Y_i(x^{k+j})=[Y_1,Y_i]x^{k+j}$$

and applying

$$[Y_1,Y_i]=\sum_{l=1}^k c_{il}Y_l$$

to the right-hand side from the involutivity condition on $$\mathcal{D}$$, we find

$$\frac{\partial}{\partial x^1}(Y_i(x^{k+j}))=\sum_{l=2}^k c_{il}Y_l(x^{k+j}).$$

Now for a fixed slice $$W$$, the $$Y_i(x^{k+j})$$ are functions of the single variable $$x^1$$, so the above is a system of $$k-1$$ linear ODEs and we can solve it.

The slices thus obtained meet $$S\cap U$$ at exactly one point, and there

$$Y_i(x^{k+j})=Z_i(w^{k+j})=0$$

holds, so the proofs of the first and second assertions are complete.

Finally, we must prove the third assertion. This time let $$\pi$$ be the projection from $$\mathbb{R}^m$$ onto the last $$m-k$$ coordinates. Then the image of $$\mathcal{D}$$ under $$d(\pi\circ\varphi)$$ is $$0$$, so

$$d(\pi\circ\varphi\circ\Phi)\equiv 0$$

holds for any $$y\in N$$. But since $$N$$ is connected, $$\pi\circ\varphi\circ\Phi$$ is constant, and hence $$\Phi(N)$$ is contained in a single slice.

</details>

---

**References**

**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013  
**[Lee]** John M. Lee. *Introduction to Smooth Manifolds*, Graduate texts in mathematics, Springer, 2012  

---
