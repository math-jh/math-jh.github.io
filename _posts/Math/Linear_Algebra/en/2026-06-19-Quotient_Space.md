---
title: "Quotient Spaces"
description: "We construct the quotient of a vector space by a subspace using cosets, prove that the operations are well-defined, and verify the dimension formula. We also discuss the natural projection, the universal property, and the first isomorphism theorem."
excerpt: "Quotient spaces of vector spaces by subspaces"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/quotient_space
sidebar: 
    nav: "linear_algebra-en"


date: 2026-06-19

weight: 8
translated_at: 2026-06-21T05:00:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-21T05:00:02+00:00
---
In this post, we define the *quotient space* $$V/W$$ for a $$\mathbb{K}$$-vector space $$V$$ and its subspace $$W$$. Intuitively, this is the space obtained by making all elements of $$W$$ equal to $$0$$ inside $$V$$; however, simply declaring all elements of $$W$$ to be $$0$$ is not enough, because we want the remaining space to still be a vector space.

## Cosets

The biggest problem, as pointed out above, is that merely setting all elements of $$W$$ to $$0$$ gives no guarantee that the remaining space will be a vector space. For instance, for this to be a vector space it must first be closed under addition, but any element $$v$$ of $$V$$ can always be written as $$v=(v-w)+w$$ for a fixed $$w\in W$$, so if $$v$$ and $$v-w$$ do not belong to $$W$$, then even after treating all elements of $$W$$ as $$0$$ we would have

$$v-(v-w)=w=0$$

so that the difference of $$v$$ and $$v-w$$ becomes $$0$$ even though they are not equal.

This shows two things. First, to define $$V/W$$ it is insufficient to simply set all elements of $$W$$ to $$0$$ and leave the rest untouched. Second, and more importantly, the simple calculation above actually gives a hint as to how $$V/W$$ should be constructed. Namely, if the difference of two vectors $$v,v'$$ lies in $$W$$, then we must treat them as <em-ko>the same</em-ko> element inside $$V/W$$.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Let a $$\mathbb{K}$$-vector space $$V$$ and its subspace $$W\leq V$$ be given. For any $$v\in V$$, the set

$$v+W=\{v+w\mid w\in W\}$$

is called the *coset* of $$W$$ containing $$v$$.

</div>

From the definition, the coset $$v+W$$ is the set of all vectors whose difference from $$v$$ lies in $$W$$, i.e. the vectors that we agreed to identify with $$v$$ inside $$V/W$$. This is an example of an equivalence class treated in set theory ([\[Set Theory\] §Equivalence Relations, ⁋Definition 4](/en/math/set_theory/equivalence_relations#def4)), but all we need is the following fact, claimed in the introduction, that two cosets are equal precisely when the difference of their representatives lies in $$W$$.

<div class="proposition" markdown="1">

<ins id="lem2">**Lemma 2**</ins> For a $$\mathbb{K}$$-vector space $$V$$ and its subspace $$W\leq V$$, and for any two vectors $$v,v'\in V$$, the following equivalence holds:

$$v+W=v'+W\iff v-v'\in W$$

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, if $$v-v'\in W$$, then for any representative $$v+w\in v+W$$ we have $$v+w=v'+\bigl((v-v')+w\bigr)\in v'+W$$, and the converse holds in the same way, so $$v+W=v'+W$$.

Conversely, if $$v+W=v'+W$$, then since $$v=v+0\in v'+W$$ there exists $$w\in W$$ such that $$v=v'+w$$, and therefore $$v-v'=w\in W$$.

</details>

In particular, $$v+W=W$$ is equivalent to $$v\in W$$, and from this we see that two distinct cosets are always disjoint.

## Definition of the Quotient Space

Now let us endow the cosets with a vector space structure.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> For a $$\mathbb{K}$$-vector space $$V$$ and its subspace $$W\leq V$$, we write $$V/W$$ for the set of all cosets of $$W$$ and call it the *quotient space* of $$V$$ by $$W$$. Addition and scalar multiplication on $$V/W$$ are defined by the formulas

$$(v+W)+(v'+W)=(v+v')+W,\qquad \alpha(v+W)=(\alpha v)+W$$

respectively.

</div>

In the above definition, addition and scalar multiplication are described through a representative vector $$v$$ of the coset, so we must check that they are well defined independently of the choice of representative. That is, if $$v+W=v_1+W$$ and $$v'+W=v_1'+W$$, then we must have

$$(v+v')+W=(v_1+v_1')+W,\qquad (\alpha v)+W=(\alpha v_1)+W$$

By assumption $$v-v_1\in W$$ and $$v'-v_1'\in W$$, so from the fact that $$W$$ is closed under addition we obtain

$$(v+v')-(v_1+v_1')=(v-v_1)+(v'-v_1')\in W$$

and from the fact that $$W$$ is closed under scalar multiplication we obtain

$$(\alpha v)-(\alpha v_1)=\alpha(v-v_1)\in W$$

By [Lemma 2](#lem2) this is exactly the equality we wanted. Hence the two operations on $$V/W$$ are well defined.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> With the operations of [Definition 3](#def3), $$V/W$$ is a $$\mathbb{K}$$-vector space. The additive identity is $$0+W=W$$, and the additive inverse of $$v+W$$ is $$(-v)+W$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

All vector space axioms follow immediately from the fact that the operations on $$V/W$$ are induced coset-wise from those on $$V$$. For example, associativity of addition follows from the fact that for any $$v,v',v''\in V$$ we have

$$\bigl((v+W)+(v'+W)\bigr)+(v''+W)=\bigl((v+v')+v''\bigr)+W=\bigl(v+(v'+v'')\bigr)+W=(v+W)+\bigl((v'+W)+(v''+W)\bigr)$$

which is a direct consequence of associativity of addition in $$V$$. Commutativity, distributivity, and the scalar multiplication axioms are verified in the same way. Moreover, for any $$v\in V$$ we have

$$(v+W)+(0+W)=(v+0)+W=v+W,\qquad (v+W)+((-v)+W)=(v-v)+W=0+W$$

so $$0+W$$ is the additive identity and $$(-v)+W$$ is the additive inverse of $$v+W$$.

</details>

## Dimension of the Quotient Space

The only invariant of a vector space is its dimension. In the case of $$V/W$$, its dimension is determined directly from the dimensions of $$V$$ and $$W$$.

<div class="proposition" markdown="1">

<ins id="thm5">**Theorem 5**</ins> For a finite-dimensional $$\mathbb{K}$$-vector space $$V$$ and its subspace $$W\leq V$$, the formula

$$\dim(V/W)=\dim V-\dim W$$

holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$\dim W=k$$ and $$\dim V=n$$, and choose a basis $$\{x_1,\ldots, x_k\}$$ of $$W$$. Since this is a linearly independent subset of $$V$$, by [§Dimension of Vector Spaces, ⁋Proposition 5](/en/math/linear_algebra/dimension#prop5) we can extend it to a basis $$\{x_1,\ldots, x_k, x_{k+1},\ldots, x_n\}$$ of $$V$$. We show that the cosets

$$x_{k+1}+W,\quad\ldots,\quad x_n+W$$

form a basis of $$V/W$$.

First, they span $$V/W$$. For any $$v\in V$$, if $$v=\sum_{i=1}^n\alpha_ix_i$$ then

$$v+W=\sum_{i=1}^n\alpha_i(x_i+W)=\sum_{i=k+1}^n\alpha_i(x_i+W)$$

where the last equality holds because for $$i\leq k$$ we have $$x_i\in W$$, so $$x_i+W=W$$ is the zero vector of $$V/W$$.

Next, to show linear independence, let scalars $$\alpha_{k+1},\ldots,\alpha_n$$ be such that

$$\sum_{i=k+1}^n\alpha_i(x_i+W)=0+W$$

Then, as seen before, $$\sum_{i=k+1}^n\alpha_ix_i+W=W=0+W$$, so by [Lemma 2](#lem2) we have $$\sum_{i=k+1}^n\alpha_ix_i\in W$$. Hence we can express this vector in terms of the basis of $$W$$, so there exist scalars $$\beta_1,\ldots,\beta_k$$ with

$$\sum_{i=k+1}^n\alpha_ix_i=\sum_{i=1}^k\beta_ix_i$$

which rearranges to

$$-\sum_{i=1}^k\beta_ix_i+\sum_{i=k+1}^n\alpha_ix_i=0$$

The left-hand side is a linear combination of $$\{x_1,\ldots, x_n\}$$, and since these form a basis of $$V$$ they are linearly independent, so all coefficients must be $$0$$; in particular $$\alpha_{k+1}=\cdots=\alpha_n=0$$.

Therefore $$\{x_{k+1}+W,\ldots, x_n+W\}$$ is a basis of $$V/W$$, and since it has $$n-k$$ elements we have $$\dim(V/W)=n-k=\dim V-\dim W$$.

</details>

## First Isomorphism Theorem

One reason this post exists as a separate article is to give deeper meaning to [§Isomorphisms, ⁋Theorem 7](/en/math/linear_algebra/isomorphic_vector_spaces#thm7). In this final section we resolve this.

For any $$\mathbb{K}$$-vector space $$V$$ and subspace $$W\leq V$$, consider the function $$p:V\rightarrow V/W$$ defined by the formula

$$p(v)=v+W$$

Then the operations of [Definition 3](#def3) are precisely defined so that $$p$$ satisfies the two identities

$$p(\alpha v)=(\alpha v)+W=\alpha(v+W)=\alpha  p(v),\qquad p(v+v')=(v+v')+W=(v+W)+(v'+W)=p(v)+p(v')$$

Thus $$p$$ is a linear map, called the *natural projection* from $$V$$ to $$V/W$$. By definition $$p$$ is surjective, and

$$\ker p=\{v\in V\mid v+W=W\}=W$$

Hence we see that every subspace can be realized as the kernel of a suitable linear map.

The most important property of the natural projection is the following universal property. It says that any linear map sending $$W$$ to $$0$$ factors uniquely through $$V/W$$.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> Let a $$\mathbb{K}$$-vector space $$V$$ and a subspace $$W\leq V$$ be given, and let $$L:V\rightarrow U$$ be a linear map to another $$\mathbb{K}$$-vector space $$U$$ satisfying $$W\subseteq\ker L$$. Then there exists a unique linear map $$\bar L:V/W\rightarrow U$$ defined by the formula

$$\bar L(v+W)=L(v)$$

such that $$L=\bar L\circ p$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First we show that $$\bar L$$ is well defined. If $$v+W=v'+W$$, then $$v-v'\in W\subseteq\ker L$$, so

$$L(v)-L(v')=L(v-v')=0$$

and therefore $$L(v)=L(v')$$. That is, the value of $$\bar L(v+W)$$ is independent of the choice of representative. That $$\bar L$$ is linear follows from

$$\bar L\bigl(\alpha(v+W)+(v'+W)\bigr)=\bar L\bigl((\alpha v+v')+W\bigr)=L(\alpha v+v')=\alpha L(v)+L(v')=\alpha\bar L(v+W)+\bar L(v'+W)$$

Also, for any $$v\in V$$ we have $$(\bar L\circ p)(v)=\bar L(v+W)=L(v)$$, so $$L=\bar L\circ p$$. Finally, if a linear map $$L':V/W\rightarrow U$$ satisfies $$L=L'\circ p$$, then since $$p$$ is surjective, for any $$v+W\in V/W$$ we have $$L'(v+W)=L'(p(v))=L(v)=\bar L(v+W)$$, and therefore $$L'=\bar L$$.

</details>

Applying the above universal property to the case $$W=\ker L$$, we obtain the following theorem, which is fundamental for classifying vector spaces.

<div class="proposition" markdown="1">

<ins id="thm7">**Theorem 7 (First Isomorphism Theorem)**</ins> For two $$\mathbb{K}$$-vector spaces $$V,U$$ and a linear map $$L:V\rightarrow U$$, the linear map $$\bar L:V/\ker L\rightarrow \im L$$ defined by the formula

$$\bar L(v+\ker L)=L(v)$$

is an isomorphism. That is, $$V/\ker L\cong\im L$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Setting $$W=\ker L$$, by [Proposition 6](#prop6) the linear map $$\bar L:V/\ker L\rightarrow U$$ defined by $$\bar L(v+\ker L)=L(v)$$ is well defined, and its image equals $$\im L$$. Thus restricting the codomain to $$\im L$$ gives a surjective map $$\bar L:V/\ker L\rightarrow\im L$$. On the other hand, if $$\bar L(v+\ker L)=0$$ then $$L(v)=0$$, i.e. $$v\in\ker L$$, so $$v+\ker L=\ker L$$ is the zero vector of $$V/\ker L$$. Hence $$\ker\bar L=\{0\}$$, and therefore $$\bar L$$ is injective. ([§Linear Maps, ⁋Proposition 8](/en/math/linear_algebra/linear_map#prop8)) That is, $$\bar L$$ is a bijective linear map, hence an isomorphism. ([§Isomorphisms, ⁋Lemma 2](/en/math/linear_algebra/isomorphic_vector_spaces#lem2))

</details>

Combining [Theorem 7](#thm7) and [Theorem 5](#thm5), we recover the rank-nullity theorem. Indeed, for finite-dimensional $$V$$ we have

$$\rank L=\dim\im L=\dim(V/\ker L)=\dim V-\dim\ker L=\dim V-\nullity L$$

which is exactly the formula of [§Isomorphisms, ⁋Theorem 7](/en/math/linear_algebra/isomorphic_vector_spaces#thm7). That is, the rank-nullity theorem is nothing more than the statement that after "folding away" $$\ker L$$, $$L$$ becomes injective, expressed in the language of dimensions.

---

**References**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.  
**[Rom]** S. Roman, *Advanced linear algebra*, 3rd ed., Graduate Texts in Mathematics 135, Springer, 2008.

---
