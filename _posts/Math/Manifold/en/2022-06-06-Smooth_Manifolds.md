---
title: "Differentiable Manifolds"
excerpt: "Definition of smooth manifolds"

categories: [Math / Manifold]
permalink: /en/math/manifold/smooth_manifolds
header:
    overlay_image: /assets/images/Math/Manifold/Smooth_Manifolds.png
    overlay_filter: 0.5
sidebar: 
    nav: "manifold-en"

date: 2022-06-06
last_modified_at: 2022-06-06
weight: 1
translated_at: 2026-05-21T14:00:01+00:00
translation_source: kimi-cli
---
In topology we defined the notion of a topological manifold; in this series we study differentiable manifolds, and in particular smooth manifolds.

## Notation

We will frequently deal with $$m$$-dimensional coordinate systems, so we fix the following notation. For $$\mathbb{R}^m$$, we denote the $$i$$-th projection $$\pr_i$$ by $$r^i$$. Similarly, for any set $$X$$ and function $$f:X\rightarrow\mathbb{R}^m$$, the $$i$$-th *component function* of $$f$$ is defined by the formula $$f^i=r^i\circ f$$.

Now let $$f$$ be a function from $$\mathbb{R}^m$$ to $$\mathbb{R}$$. Then we define the partial derivative of $$f$$ with respect to the $$i$$-th coordinate by the formula

$$\frac{\partial}{\partial r^i}\bigg|_t f=\frac{\partial f}{\partial r^i}\bigg|_t=\lim_{h\rightarrow 0}\frac{f(t^1,\ldots, t^{i-1}, t^i+h, t^{i+1},\ldots, t^m)-f(t^1,\ldots, t^m)}{h}$$

As in the notation above, following **[Lee]** we write the $$i$$-th coordinate as $$x^i$$ rather than $$x_i$$.

If all the component functions are $$k$$ times differentiable and the resulting derivatives are continuous, we call $$f$$ a $$C^k$$ function. For example, saying that a function $$f:\mathbb{R}^2\rightarrow\mathbb{R}$$ is $$C^2$$ means that the following partial derivatives

$$\frac{\partial^2 f}{\partial x^2},\quad\frac{\partial^2 f}{\partial x\partial y},\quad\frac{\partial^2 f}{\partial y\partial x},\quad\frac{\partial^2 f}{\partial y^2}$$

all exist and are continuous. If $$f$$ is $$C^k$$ for every natural number $$k$$, we call it $$C^\infty$$.

## Differentiable Manifolds

Unlike a general topological space, a topological manifold looks locally like $$\mathbb{R}^n$$, so we can carry over the notion of differentiation defined there to $$M$$. The reason this is possible is that differentiability is essentially a local property.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Let a topological manifold $$M$$ be given. For $$0\leq k\leq\infty$$, we say that coordinate charts $$(U,\varphi)$$ and $$(V,\psi)$$ are *$$C^k$$-compatible* if the two *transition maps*

$$\psi\circ\varphi^{-1}:\varphi(U\cap V)\rightarrow\psi(U\cap V),\qquad\varphi\circ\psi^{-1}:\psi(U\cap V)\rightarrow\varphi(U\cap V)$$

are both $$C^k$$. A collection $$\mathcal{A}=\{(U_\lambda, \varphi_\lambda)\}_{\lambda\in\Lambda}$$ of $$C^k$$-compatible charts satisfying $$M=\bigcup U_\lambda$$ is called a *$$C^k$$-atlas*.

Among the $$C^k$$-atlases defined on $$M$$, one that is maximal with respect to inclusion is called a *$$C^k$$-differentiable structure*, and in this case $$M$$ is called a *$$C^k$$-differentiable manifold*. In the special case $$k=\infty$$, this structure is called a *smooth differentiable manifold*, or more simply a *differentiable manifold*.

</div>

The reason we think of a *maximal* atlas as giving a differentiable structure is that it is quite possible for two non-maximal atlases to define essentially the same differentiable structure. For example, $$\mathbb{R}$$ admits the following $$C^\infty$$-atlas

$$\mathcal{A}=\{(\mathbb{R}, \id_\mathbb{R})\}$$

but also another atlas

$$\mathcal{A}'=\{((-\infty, 1), \id_{(-\infty, 1)}), ((-1, \infty),\id_{(-1,\infty)})\}$$

However, as we shall verify in [Proposition 3](#prop3), given any atlas there is a uniquely determined maximal atlas containing it, so in an essential sense this is not a serious difference.

Meanwhile, to understand an object in mathematics it suffices to understand the functions defined on it. Henceforth, all manifolds are understood to be smooth differentiable manifolds.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> Consider a manifold $$M$$ and a point $$p\in M$$. A function $$f$$ defined on some open neighborhood of $$p$$ is said to be $$C^\infty$$ at $$p$$ if there exists a coordinate chart $$(U,\varphi)$$ containing $$p$$ such that the function $$f\circ\varphi^{-1}:U'\rightarrow\mathbb{R}$$ is $$C^\infty$$ at the point $$\varphi(p)$$.

</div>

Suppose another coordinate chart $$(V,\psi)$$ is defined on another open neighborhood of $$p$$. If $$f\circ\varphi^{-1}$$ were $$C^\infty$$ at $$\varphi(p)$$ but $$f\circ\psi^{-1}$$ were not $$C^\infty$$ at $$\psi(p)$$, this definition would be ill-defined. However, on $$\psi(U\cap V)$$ we have

$$f\circ\psi^{-1}=(f\circ\varphi^{-1})\circ(\varphi\circ\psi^{-1})$$

and therefore $$f\circ\psi^{-1}$$ is $$C^\infty$$ at $$\psi(p)$$. By a similar argument one can prove the following.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> Let a $$C^k$$-atlas $$\mathcal{A}$$ be given on a topological manifold $$M$$. Then there exists a unique maximal $$C^k$$-atlas containing $$\mathcal{A}$$. Hence any $$C^k$$-atlas $$\mathcal{A}$$ defines a unique $$C^k$$-differentiable structure on $$M$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Define $$\mathcal{A}'$$ by the formula

$$\mathcal{A}'=\{(V,\psi)\mid\psi\circ\varphi_\lambda^{-1}, \varphi_\lambda\circ\psi^{-1}\text{ are $C^k$ for all $\varphi_\lambda\in\mathcal{A}$}\}$$

Then $$\mathcal{A}'$$ contains $$\mathcal{A}$$, and therefore covers $$M$$ by coordinate charts. Moreover, if $$(V,\psi)$$ and $$(V',\psi')$$ are elements of $$\mathcal{A}'$$ and $$V\cap V'\neq\emptyset$$, then the transition map

$$\psi'\circ\psi^{-1}:\psi(V\cap V')\rightarrow\psi'(V\cap V')$$

is $$C^k$$. For any $$p\in\psi(V\cap V')$$, pick $$(U,\varphi)\in\mathcal{A}$$ with $$p\in U$$; then on $$U\cap V\cap V'$$ we have

$$\psi'\circ\psi^{-1}=(\psi'\circ\varphi^{-1})\circ(\varphi\circ\psi^{-1})$$

so that $$\psi'\circ\psi^{-1}$$ is $$C^k$$ at the point $$p$$. Since $$p$$ was chosen arbitrarily, this shows that $$\psi'\circ\psi^{-1}$$ is $$C^k$$. Of course, by interchanging the roles of $$(V,\psi)$$ and $$(V',\psi')$$ one can show that the transition map in the opposite direction is also $$C^k$$.

Obviously $$\mathcal{A}'$$ is a maximal $$C^k$$-atlas by definition, and its uniqueness is easily verified.

</details>

<div class="example" markdown="1">

<ins id="ex4">**Example 4**</ins> Consider two atlases on the set of real numbers $$\mathbb{R}$$:

$$\mathcal{A}_1=\{(\mathbb{R},\id_\mathbb{R})\},\qquad \mathcal{A}_2=\{(\mathbb{R}, x\mapsto x^3)\}$$

Since these consist of a single chart, they are obviously $$C^\infty$$. By the preceding [Proposition 3](#prop3), there exists a differentiable structure containing each of them. But they are not equal. This is because the two charts $$(\mathbb{R},\id_\mathbb{R})$$ and $$(\mathbb{R}, x\mapsto x^3)$$ are not $$C^\infty$$-compatible. ($$x\mapsto x^3$$ is a $$C^\infty$$ function, but its inverse $$x\mapsto x^{1/3}$$ is not.)

</div>

Nevertheless, although the two atlases in [Example 4](#ex4) do not give the <em>same</em> differentiable structure, they give *diffeomorphic* differentiable structures.

## Smooth partition of unity

We showed that a continuous partition of unity exists on any topological manifold; however, when dealing with differentiable manifolds a merely continuous partition of unity is of little use. For example, if we multiply an arbitrary $$C^\infty$$ function by a partition of unity that is merely continuous, the differentiability of the function is immediately weakened.

Therefore we need to construct a smooth partition of unity, and for this it suffices to prove the following lemma.

<div class="proposition" markdown="1">

<ins id="lem5">**Lemma 5 ($$C^\infty$$ Urysohn lemma)**</ins> Let real numbers $$a'<a<b<b'$$ be given. Then there exists a $$C^\infty$$ function $$\psi:\mathbb{R}\rightarrow[0,1]$$ that is equal to $$1$$ on $$[a,b]$$ and equal to $$0$$ outside $$(a',b')$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

We may assume without loss of generality that $$a'=-2$$, $$a=-1$$, $$b=1$$, and $$b'=2$$. First define a function $$f$$ by

$$f(t)=\begin{cases}e^{-1/t}&t>0\\0&t\leq 0\end{cases}$$

In particular, $$f$$ is always non-negative and is $$C^\infty$$. Now define

$$g(t)=\frac{f(t)}{f(t)+f(1-t)}$$

Then $$g$$ is likewise always non-negative, its values are always at most $$1$$, and in particular $$g(t)\equiv 1$$ for $$t\geq 1$$ and $$g(t)\equiv 0$$ for $$t\leq 0$$. Therefore, defining $$\psi$$ by the formula

$$\psi(t)=g(t+2)g(2-t)$$

gives the desired function.

</details>

Using the above $$C^\infty$$ Urysohn lemma instead of the ordinary Urysohn lemma, one can construct a smooth partition of unity on a differentiable manifold.

---

**References**

**[Lee]** John M. Lee. *Introduction to Smooth Manifolds*, Graduate texts in mathematics, Springer, 2012  
**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013    

---
