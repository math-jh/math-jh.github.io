---
title: "Tangent Space"
excerpt: "Tangent Vectors and Tangent Space"

categories: [Math / Manifold]
permalink: /en/math/manifold/tangent_space
header:
    overlay_image: /assets/images/Math/Manifold/Tangent_Space.png
    overlay_filter: 0.5
sidebar: 
    nav: "manifold-en"

date: 2022-06-14
last_modified_at: 2022-12-09
weight: 3
translated_at: 2026-05-21T15:00:01+00:00
translation_source: kimi-cli
---
In this post we define tangent vectors on a manifold and the space they generate, the tangent space.

## Motivation

In **[Lee]**, a fairly lengthy portion of the beginning of Chapter 3 is devoted to justifying the definitions we will make; let us first briefly review this.

The simplest example of a manifold is $$\mathbb{R}^m$$, and a slightly more complicated example is a surface contained in $$\mathbb{R}^m$$. A tangent vector at a point $$p$$ on this surface literally means vectors that are tangent to the surface at the point $$p$$. If this surface is a two-dimensional surface in $$\mathbb{R}^3$$, then collecting these vectors yields exactly the tangent plane at the point $$p$$. However, generalizing this to a definition of tangent vectors on a manifold is not easy. In this definition, the existence of an ambient space $$\mathbb{R}^m$$ containing the surface is essential, because when we defined a manifold we did so in a purely intrinsic way.

Instead, in the situation above we can observe that whenever tangent vectors are given, directional derivatives arise. That is, given any tangent vector $$v$$, this vector assigns to each function $$f$$ defined in a neighborhood of the point $$p$$ the directional derivative in the $$v$$-direction

$$\lim_{t\rightarrow 0}\frac{f(p+tv)-f(p)}{t}$$

Our idea is to define this operator called <em-ko>directional derivative</em-ko> as the tangent vector.

## Sheaf of Differentiable Functions

Let $$C^\infty(U)$$ be the collection of $$C^\infty$$ functions defined on an open set $$U$$, and whenever $$V\subseteq U$$ define the map $$\rho_{UV}:C^\infty(U)\rightarrow C^\infty(V)$$ by

$$\rho_{UV}:f\mapsto f|_V$$

Then this structure becomes a sheaf of rings $$\mathcal{C}^\infty_M$$ on $$M$$. ([\[Topology\] §Sheaves, ⁋Definition 1](/en/math/topology/sheaves#def1)) The stalk of $$\mathcal{C}^\infty$$ at any $$p\in M$$ is written $$\mathcal{C}^\infty_{M,p}$$, or simply $$\mathcal{C}^\infty_p$$ when there is no danger of confusion. ([\[Topology\] §Presheaves, ⁋Definition 9](/en/math/topology/presheaves#def9))

<div class="proposition" markdown="1">

<ins id="prop1">**Proposition 1**</ins> For any manifold $$M$$, $$\mathcal{C}^\infty_p$$ has the structure of an $$\mathbb{R}$$-algebra.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

To show this, it suffices to define operations on $$\mathcal{C}^\infty_p$$. Choose two elements $$\mathbf{f},\mathbf{g}$$ of $$\mathcal{C}^\infty_p$$. Then there exist suitable open neighborhoods $$U,V$$ of $$p$$ such that we may think of $$\mathbf{f}$$ and $$\mathbf{g}$$ as the germs of $$(f,U)$$ and $$(g,V)$$, respectively. Now define $$\mathbf{f}+\mathbf{g}$$ as the equivalence class of the function

$$(f|_{U\cap V}+g|_{U\cap V}, U\cap V)$$

In other words, to compute the sum of two germs $$\mathbf{f}$$ and $$\mathbf{g}$$, we find an open neighborhood of $$p$$ on which both functions $$f,g$$ are commonly defined, and then compute the sum of $$f$$ and $$g$$ on this open neighborhood. Of course, it is easy to see that this definition does not depend on the choice of representative.

Similarly, one can define multiplication of functions and scalar multiplication.

</details>

In fact, for scalar multiplication defined on $$\mathcal{C}^\infty_p$$, since this can simply be thought of as multiplication by constant functions, we may regard $$\mathcal{C}^\infty_p$$ as a ring rather than an algebra. Thus $$(M,\mathcal{C}^\infty_M)$$ becomes a ringed space. The next proposition shows that this space is a *locally ringed space*.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> The ring $$\mathcal{C}^\infty_p$$ is a local ring, and its maximal ideal is given by the formula

$$\mathfrak{m}_p=\{\mathbf{f}\in \mathcal{C}^\infty_p\mid \mathbf{f}(p)=0\}$$

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, the condition $$\mathbf{f}(p)=0$$ is well defined. This is because all functions belonging to $$\mathbf{f}$$ must have the same value at the point $$p$$. It is not difficult to see that $$\mathfrak{m}_p$$ is indeed an ideal.

Moreover, that $$\mathfrak{m}_p$$ is maximal follows from the following diagram being exact when the *evaluation map* $$\ev_p:\mathcal{C}^\infty_p\rightarrow\mathbb{R}$$ is defined by $$\mathbf{f}\mapsto\mathbf{f}(p)$$:

$$0\longrightarrow \mathfrak{m}_p\longrightarrow \mathcal{C}^\infty_p\overset{\ev_p}{\longrightarrow}\mathbb{R}\longrightarrow 0$$

This is because $$\mathcal{C}^\infty_p/\mathfrak{m}_p$$ becomes the field $$\mathbb{R}$$.

</details>

## Tangent Vectors

Summarizing the preceding content without the language of sheaves is as follows.

We have decided to define a tangent vector at the point $$p$$ as a <em-ko>directional derivative at the point $$p$$</em-ko>. This directional derivative is of course well defined for any function differentiable on all of $$M$$, but differentiability is essentially a local property, so in fact the directional derivative of a function defined only on a suitable open neighborhood $$U$$ of the point $$p$$ can also be defined.[^1] 

Moreover, if two functions $$f,g$$ define the same function on some open neighborhood $$U$$ of the point $$p$$, then their derivatives at the point $$p$$ also coincide, so when dealing with directional derivatives they may be treated as the same. Then the objects of our interest are no longer functions but equivalence classes of functions, which explicitly is as follows.

$$\mathcal{C}^\infty_p=\{(f,U)\mid f\in C^\infty(U)\}\big/{\sim},\qquad (f,U)\sim (g,V)\iff f\vert_W=g\vert_W\text{ for some $W\subseteq U\cap V$ open}$$

Let us write the equivalence class of $$f$$ as $$\mathbf{f}$$. Then the content of [Proposition 1](#prop1) is that scalar multiplication and addition, and even multiplication, are well defined on $$\mathcal{C}^\infty$$, as in $$\mathbf{f}\mathbf{g},\mathbf{f}+\mathbf{g}$$.

Now a tangent vector is a directional derivative that assigns a real number to each element of $$\mathcal{C}^\infty_p$$. Here the derivative is defined as a linear map satisfying the Leibniz rule.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> Let $$M$$ be a manifold and $$p\in M$$ a point. An $$\mathbb{R}$$-linear map $$v:\mathcal{C}^\infty_p\rightarrow\mathbb{R}$$ satisfying the Leibniz rule

$$v(\mathbf{f}\mathbf{g})=\mathbf{f}(p)v(\mathbf{g})+\mathbf{g}(p)v(\mathbf{f})$$

is called a *tangent vector* of $$M$$ at the point $$p$$. The collection of tangent vectors of $$M$$ at the point $$p$$ is called the *tangent space* of $$M$$ at the point $$p$$, and is written $$T_pM$$.

</div>

The next proposition states a fact that is already easy to guess.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> The $$T_pM$$ defined in [Definition 3](#def3) is an $$\mathbb{R}$$-vector space.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Since both $$\mathcal{C}^\infty_p$$ and $$\mathbb{R}$$ are $$\mathbb{R}$$-vector spaces, $$\Hom_\mathbb{R}(\mathcal{C}^\infty_p,\mathbb{R})$$ is also an $$\mathbb{R}$$-vector space. Therefore, to show that the tangent space $$T_pM$$ is indeed an $$\mathbb{R}$$-vector space as its name suggests, it suffices to show that $$T_pM$$ is closed under addition and scalar multiplication. For example, since $$v+w$$ is the linear map defined by the formula

$$(v+w)(\mathbf{f})=v(\mathbf{f})+w(\mathbf{f})$$

to show that $$T_pM$$ is closed under addition we compute

$$\begin{aligned}(v+w)(\mathbf{fg})&=v(\mathbf{fg})+w(\mathbf{fg})=\mathbf{f}(p)v(\mathbf{g})+\mathbf{g}(p)v(\mathbf{f})+\mathbf{f}(p)w(\mathbf{g})+\mathbf{g}(p)w(\mathbf{f})\\
&=\mathbf{f}(p)(v+w)(\mathbf{g})+\mathbf{g}(p)(v+w)(\mathbf{f})\end{aligned}$$

and confirm that $$v+w$$ is also an element of $$T_pM$$.

</details>

Moreover, for any tangent vector $$v$$ and the constant function $$\mathbf{c}$$ having the value $$c$$ at every point, $$v(\mathbf{c})=0$$ always holds. If we denote by $$\mathbf{1}$$ the constant function with function value $$1$$, then since $$\mathbf{c}=c\cdot\mathbf{1}$$ it suffices to show the following:

<div class="proposition" markdown="1">

<ins id="lem6">**Lemma 6**</ins> For any tangent vector $$v$$, we have $$v(\mathbf{1})=0$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

$$v(\mathbf{1})=v(\mathbf{1}\cdot\mathbf{1})=\mathbf{1}(p)v(\mathbf{1})+\mathbf{1}(p)v(\mathbf{1})=v(\mathbf{1})+v(\mathbf{1})=2v(\mathbf{1}).$$

</details>

However, we still do not know what kind of space $$T_pM$$ is. In particular, we do not yet know the dimension of $$T_pM$$. We will examine this in the next post.

---

**References**

**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013  
**[Lee]** John M. Lee. *Introduction to Smooth Manifolds*, Graduate texts in mathematics, Springer, 2012  

---

[^1]: Functions defined only on $$U$$ can be extended to all of $$M$$ via a partition of unity, so in the present situation we need not distinguish the two.
