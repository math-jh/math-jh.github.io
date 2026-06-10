---
title: "Smooth Manifolds"
description: "We define a differential structure through the compatibility of coordinate charts on a topological manifold, and based on this, we discuss the concept of a smooth manifold."
excerpt: "Definition of smooth manifolds"

categories: [Math / Manifolds]
permalink: /en/math/manifolds/smooth_manifolds
sidebar: 
    nav: "manifolds-en"

date: 2022-06-06
last_modified_at: 2022-06-06
weight: 1
translated_at: 2026-06-01T04:00:03+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-01T04:00:03+00:00
---
We defined the notion of a topological manifold in topology; in this series of posts we deal with differentiable manifolds, and in particular smooth manifolds.

## Notation

Since we will frequently work with coordinate systems of dimension $$m$$, we fix the following notation. For $$\mathbb{R}^m$$, we denote the $$i$$-th projection $$\pr_i$$ by $$r^i$$. Similarly, for any set $$X$$ and function $$f:X\rightarrow\mathbb{R}^m$$, the $$i$$-th *component function* of $$f$$ is defined by the formula $$f^i=r^i\circ f$$.

Now let $$f$$ be a function from $$\mathbb{R}^m$$ to $$\mathbb{R}$$. Then we define the partial derivative of $$f$$ with respect to its $$i$$-th component by the formula

$$\frac{\partial}{\partial r^i}\bigg\vert_t f=\frac{\partial f}{\partial r^i}\bigg\vert_t=\lim_{h\rightarrow 0}\frac{f(t^1,\ldots, t^{i-1}, t^i+h, t^{i+1},\ldots, t^m)-f(t^1,\ldots, t^m)}{h}$$

As in the notation above, following **[Lee]** we write the $$i$$-th component as $$x^i$$ rather than $$x_i$$.

If each component function is $$k$$-times differentiable and the result is continuous, we say the function $$f$$ is $$C^k$$. For example, saying a function $$f:\mathbb{R}^2\rightarrow\mathbb{R}$$ is $$C^2$$ means that all the following partial derivatives

$$\frac{\partial^2 f}{\partial x^2},\quad\frac{\partial^2 f}{\partial x\partial y},\quad\frac{\partial^2 f}{\partial y\partial x},\quad\frac{\partial^2 f}{\partial y^2}$$

exist and are continuous. If a function $$f$$ is $$C^k$$ for every natural number $$k$$, we call it $$C^\infty$$.

## Differentiable Manifolds

Unlike general topological spaces, a topological manifold looks locally like $$\mathbb{R}^n$$, so we can import the notion of differentiation defined there to $$M$$. This is possible because differentiability is essentially a local property.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Let a topological manifold $$M$$ be given. For $$0\leq k\leq\infty$$, coordinate charts $$(U,\varphi)$$ and $$(V,\psi)$$ are *$$C^k$$-compatible* if both *transition maps*

$$\psi\circ\varphi^{-1}:\varphi(U\cap V)\rightarrow\psi(U\cap V),\qquad\varphi\circ\psi^{-1}:\psi(U\cap V)\rightarrow\varphi(U\cap V)$$

are $$C^k$$. A collection $$\mathcal{A}=\{(U_\lambda, \varphi_\lambda)\}_{\lambda\in\Lambda}$$ of $$C^k$$-compatible charts satisfying $$M=\bigcup U_\lambda$$ is called a *$$C^k$$-atlas*.

Among $$C^k$$-atlases defined on $$M$$, an atlas that is maximal with respect to inclusion is called a *$$C^k$$-differentiable structure*, and in this case $$M$$ is called a *$$C^k$$-differentiable manifold*. In the special case $$k=\infty$$, this structure is called a *smooth differentiable manifold* or more simply a *differentiable manifold*.

</div>

The reason we think of a *maximal* atlas as giving a differentiable structure in this definition is that it is entirely possible for two non-maximal atlases to give essentially the same differentiable structure. For example, $$\mathbb{R}$$ has the $$C^\infty$$-atlas

$$\mathcal{A}=\{(\mathbb{R}, \id_\mathbb{R})\}$$

but also another atlas

$$\mathcal{A}'=\{((-\infty, 1), \id_{(-\infty, 1)}), ((-1, \infty),\id_{(-1,\infty)})\}$$

However, as we will see in [Proposition 3](#prop3), since a maximal atlas containing any given atlas is uniquely determined, in an essential sense this is not such a big difference.

On the other hand, to understand an object in mathematics it suffices to know the functions defined on it. Henceforth we assume all manifolds are smooth differentiable manifolds.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> Consider a manifold $$M$$ and a point $$p\in M$$. A function $$f$$ defined on a suitable open neighborhood of $$p$$ is $$C^\infty$$ at $$p$$ if for some coordinate chart $$(U,\varphi)$$ containing $$p$$, the function $$f\circ\varphi^{-1}:U'\rightarrow \mathbb{R}$$ is $$C^\infty$$ at the point $$\varphi(p)$$.

</div>

Suppose another coordinate chart $$(V,\psi)$$ is defined on another open neighborhood of $$p$$. If $$f\circ\varphi^{-1}$$ is $$C^\infty$$ at $$\varphi(p)$$ but $$f\circ\psi^{-1}$$ is not at $$\psi(p)$$, then this definition would not be well-defined. However, on $$\psi(U\cap V)$$ we have

$$f\circ\psi^{-1}=(f\circ\varphi^{-1})\circ(\varphi\circ\psi^{-1})$$

so $$f\circ\psi^{-1}$$ is $$C^\infty$$ at $$\psi(p)$$. By a similar argument one can show the following.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> Let a $$C^k$$-atlas $$\mathcal{A}$$ on a topological manifold $$M$$ be given. Then there exists a unique maximal $$C^k$$-atlas containing $$\mathcal{A}$$. Therefore any $$C^k$$-atlas $$\mathcal{A}$$ defines a unique $$C^k$$-differentiable structure on $$M$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Define $$\mathcal{A}'$$ by the formula

$$\mathcal{A}'=\{(V,\psi)\mid\psi\circ\varphi_\lambda^{-1}, \varphi_\lambda\circ\psi^{-1}\text{ are $C^k$ for all $\varphi_\lambda\in\mathcal{A}$}\}$$

Then $$\mathcal{A}'$$ contains $$\mathcal{A}$$, and thus covers $$M$$ with coordinate charts. On the other hand, if $$(V,\psi)$$ and $$(V',\psi')$$ are elements of $$\mathcal{A}'$$ and $$V\cap V'\neq\emptyset$$, then the transition map

$$\psi'\circ\psi^{-1}:\psi(V\cap V')\rightarrow\psi'(V\cap V')$$

is $$C^k$$. For any $$p\in\psi(V\cap V')$$, choosing $$(U,\varphi)\in\mathcal{A}$$ with $$p\in U$$, on $$U\cap V\cap V'$$ we have

$$\psi'\circ\psi^{-1}=(\psi'\circ\varphi^{-1})\circ(\varphi\circ\psi^{-1})$$

so $$\psi'\circ\psi^{-1}$$ is $$C^k$$ at $$p$$. Since $$p$$ was arbitrary, this shows that $$\psi'\circ\psi^{-1}$$ is $$C^k$$. Of course, reversing the roles of $$(V,\psi)$$ and $$(V',\psi')$$ shows that the reverse transition map is also $$C^k$$.

By definition $$\mathcal{A}'$$ is clearly a maximal $$C^k$$-atlas, and its uniqueness is easily verified.

</details>

<div class="example" markdown="1">

<ins id="ex4">**Example 4**</ins> On the real numbers $$\mathbb{R}$$, consider the two atlases

$$\mathcal{A}_1=\{(\mathbb{R},\id_\mathbb{R})\},\qquad \mathcal{A}_2=\{(\mathbb{R}, x\mapsto x^3)\}$$

These are atlases consisting of a single chart, so they are trivially $$C^\infty$$. By the preceding [Proposition 3](#prop3), there exists a differentiable structure containing each of them. However, they are not equal, because the two charts $$(\mathbb{R},\id_\mathbb{R})$$ and $$(\mathbb{R}, x\mapsto x^3)$$ are not $$C^\infty$$-compatible. (While $$x\mapsto x^3$$ is a $$C^\infty$$ function, its inverse $$x\mapsto x^{1/3}$$ is not.)

</div>

However, although the two atlases in [Example 4](#ex4) do not give the *same* differentiable structure, they give differentiable structures that are *diffeomorphic* to each other.

## Smooth Partition of Unity

We showed that a continuous partition of unity exists on any topological manifold, but when dealing with differentiable manifolds a merely continuous partition of unity is of little help. For example, if we multiply an arbitrary $$C^\infty$$ function by a partition of unity that is only continuous, the degree of differentiability of this function would immediately deteriorate.

Therefore we need to construct a smooth partition of unity, and for this it suffices to prove the following lemma.

<div class="proposition" markdown="1">

<ins id="lem5">**Lemma 5 ($$C^\infty$$ Urysohn Lemma)**</ins> Let real numbers $$a'<a<b<b'$$ be given. Then there exists a $$C^\infty$$ function $$\psi:\mathbb{R}\rightarrow[0,1]$$ that equals $$1$$ on $$[a,b]$$ and $$0$$ outside $$(a',b')$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

We may assume without loss of generality that $$a'=-2,a=-1,b=1,b'=2$$. First define a function $$f$$ by

$$f(t)=\begin{cases}e^{-1/t}&t>0\\0&t\leq 0\end{cases}$$

Then in particular $$f$$ is always non-negative and is $$C^\infty$$. Now define

$$g(t)=\frac{f(t)}{f(t)+f(1-t)}$$

Then $$g$$ is likewise always non-negative, its value is always less than or equal to $$1$$, and in particular it is identically $$1$$ when $$t\geq 1$$ and identically $$0$$ when $$t\leq 0$$. Therefore it suffices to define $$\psi$$ by the formula

$$\psi(t)=g(t+2)g(2-t)$$

</details>

Using the above $$C^\infty$$ Urysohn lemma in place of the general Urysohn lemma, we can construct a smooth partition of unity on a differentiable manifold.

---

**References**

**[Lee]** John M. Lee. *Introduction to Smooth Manifolds*, Graduate texts in mathematics, Springer, 2012  
**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013    

---
