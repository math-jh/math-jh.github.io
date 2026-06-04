---
title: "Orientation"
description: "This post discusses orientation in vector spaces and manifolds. It explains how to determine the ordering of bases using the sign of the determinant, and describes orientable manifolds through coordinate systems with positive Jacobian and nonvanishing top-degree differential forms."
excerpt: "Orientation on a manifold"

categories: [Math / Manifolds]
permalink: /en/math/manifolds/orientation
sidebar: 
    nav: "manifolds-en"

date: 2023-02-13
last_modified_at: 2023-02-13
weight: 19
translated_at: 2026-06-01T11:30:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-01T11:30:04+00:00
---
## Orientation in Euclidean Space

Consider the standard basis $$(e_1,e_2,e_3)$$ in three-dimensional space. From calculus, we know that the order in which this basis is arranged matters. For example, the basis above satisfies $$e_1\times e_2=e_3$$, but if the order were changed to $$(e_2,e_1,e_3)$$, then we would have $$e_2\times e_1=-e_3$$.

There is no need to restrict this observation to the standard basis. In general, for any orthonormal basis $$(x_1,x_2,x_3)$$ of $$\mathbb{R}^3$$, we can tell whether this basis is arranged in the correct order according to whether $$x_1\times x_2$$ equals $$x_3$$ or $$-x_3$$. Writing this as a formula, the value of

$$x_3\cdot(x_1\times x_2)$$

being $$+1$$ or $$-1$$ determines the order. Yet this expression equals

$$x_3\cdot(x_1\times x_2)=\det[x_3\;x_1\;x_2]=\det[x_1\;x_2\;x_3]$$

so we can determine the order for a general basis, not necessarily orthonormal, by reading whether the value of the above determinant is positive or negative.

Once we define the order of a basis via the determinant in $$\mathbb{R}^3$$, we can naturally tell in $$\mathbb{R}^m$$ as well whether a basis $$(x_1,\ldots, x_m)$$ is arranged in the correct order or the opposite order. Namely, we investigate the sign of the determinant

$$\det[x_1\;x_2\;\cdots\;x_m]$$

## Determinant and Orientation

Let $$V,W$$ be $$n$$-dimensional $$\mathbb{R}$$-vector spaces and let $$L:V\rightarrow W$$ be a linear map. Then, by the universal property of [\[Multilinear Algebra\] §Tensor Algebras, ⁋Proposition 11](/en/math/multilinear_algebra/tensor_algebras#prop11), the following linear map

$$\bigwedge\nolimits^n(L):\bigwedge\nolimits^n(V)\rightarrow\bigwedge\nolimits^n(W)$$

is well-defined. On the other hand, since both $$V$$ and $$W$$ are $$n$$-dimensional, $$\bigwedge\nolimits^n(V)$$ and $$\bigwedge\nolimits^n(W)$$ are both one-dimensional vector spaces; therefore the above linear map is uniquely determined by where any nonzero vector is sent. In particular, if $$V=W$$, then any nonzero vector in $$\bigwedge\nolimits^n(V)$$ is always sent to a scalar multiple of itself, and this scalar equals the determinant of $$L$$. From this perspective, $$\bigwedge\nolimits^n(L)$$ is sometimes called the *determinant map*, and if $$E$$ is an $$n$$-dimensional vector bundle over a manifold $$M$$, then $$\bigwedge\nolimits^n(E)$$ is called the *determinant bundle* of $$E$$.

In particular, if $$E=T^\ast M$$, we define the following.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Let $$M$$ be an $$m$$-dimensional connected manifold. Then $$M$$ is said to be *orientable* if $$\bigwedge\nolimits^m(M)\setminus\{0\}$$ has two components, and choosing one of the two components is called an *orientation* of $$M$$.

</div>

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> Let $$M$$ be an $$m$$-dimensional connected manifold. Then the following are all equivalent.

1. $$M$$ is orientable.
2. There exists a suitable collection of coordinate systems covering $$M$$ such that the Jacobian is always positive on their overlaps.
3. There exists a non-vanishing $$m$$-form defined on $$M$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>



</details>

<div class="example" markdown="1">

<ins id="ex3">**Example 3**</ins>

Any Lie group is orientable. Indeed, if we choose any basis $$\omega_1,\ldots,\omega_n$$ in $$\Omega_\text{l.inv}^\ast(G)$$ and consider their wedge $$\omega_1\wedge\cdots\wedge\omega_n$$, this defines a nonvanishing $$n$$-form on $$G$$.

</div>

---

**References**

**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013  
**[Lee]** John M. Lee. *Introduction to Smooth Manifolds*, Graduate texts in mathematics, Springer, 2012

---
