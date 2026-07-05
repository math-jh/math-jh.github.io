---
title: "Quotient Spaces"
description: "We construct the quotient space of a vector space by a subspace using cosets, and prove the well-definedness of operations and the dimension formula. We also examine the natural projection, the universal property, and the first isomorphism theorem."
excerpt: "Quotient spaces formed by modding out a subspace"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/quotient_space
sidebar: 
    nav: "linear_algebra-en"


date: 2026-06-19

weight: 8
drift_needed: true
translated_at: 2026-07-05T15:32:00+00:00
translation_source: kimi-cli
---
In this post, we define the *quotient space* $$V/W$$ for a $$\mathbb{K}$$-vector space $$V$$ and its subspace $$W$$. Intuitively, this is the space obtained from $$V$$ by making all elements of $$W$$ equal to $$0$$; however, since we want the remaining space to still be a vector space, simply declaring all elements of $$W$$ to be $$0$$ is not enough to achieve this.

## Cosets

The biggest problem, as pointed out above, is that merely setting all elements of $$W$$ to $$0$$ does not guarantee that the remaining space will be a vector space. For this to be a vector space, it must first be closed under operations: any element $$v$$ of $$V$$ can always be written in the form $$v=(v-w)+w$$ for a fixed $$w\in W$$, and thus if $$v$$ and $$v-w$$ do not belong to $$W$$, then even if we treat every element of $$W$$ as $$0$$,

$$v-(v-w)=w=0$$

so the difference of $$v$$ and $$v-w$$ becomes $$0$$ even though they are not equal.

This shows two things. First, to define $$V/W$$ it is insufficient to simply set all elements of $$W$$ to $$0$$ and leave the remaining elements unchanged. Second, and more importantly, the simple computation above actually gives a hint as to how to construct $$V/W$$. Namely, if the difference of two vectors $$v,v'$$ lies in $$W$$, then we must treat them as <em-ko>the same</em-ko> element inside $$V/W$$.

::: Definition 1
Let a $$\mathbb{K}$$-vector space $$V$$ and its subspace $$W\leq V$$ be given. For any $$v\in V$$, the set

$$v+W=\{v+w\mid w\in W\}$$

is called the *coset* of $$W$$ containing $$v$$.
:::

By definition, the coset $$v+W$$ is the set of all vectors whose difference from $$v$$ lies in $$W$$, that is, the vectors that we agreed to treat as equal to $$v$$ inside $$V/W$$. This is an example of an equivalence class from set theory ([\[Set Theory\] §Equivalence Relations, ⁋Definition 4](/en/math/set_theory/equivalence_relations#def4)), but all we need is the following fact, claimed in the introduction, that two cosets are equal if and only if the difference of their representatives lies in $$W$$.

::: Lemma 2
For a $$\mathbb{K}$$-vector space $$V$$ and its subspace $$W\leq V$$, and for any two vectors $$v,v'\in V$$, the following equivalence holds:

$$v+W=v'+W\iff v-v'\in W$$
:::
::: Proof
First, if $$v-v'\in W$$, then for any representative $$v+w\in v+W$$ we have $$v+w=v'+\bigl((v-v')+w\bigr)\in v'+W$$, and the converse holds in the same way, so $$v+W=v'+W$$.

Conversely, if $$v+W=v'+W$$, then since $$v=v+0\in v'+W$$ there exists $$w\in W$$ such that $$v=v'+w$$, and therefore $$v-v'=w\in W$$.
:::

In particular, $$v+W=W$$ is equivalent to $$v\in W$$, and from this we know that any two distinct cosets are always disjoint.

## Definition of the Quotient Space

Now we endow the cosets with a vector space structure.

::: Definition 3
For a $$\mathbb{K}$$-vector space $$V$$ and its subspace $$W\leq V$$, we denote by $$V/W$$ the set of all cosets of $$W$$ and call it the *quotient space* of $$V$$ by $$W$$. Addition and scalar multiplication on $$V/W$$ are defined respectively by the formulas

$$(v+W)+(v'+W)=(v+v')+W,\qquad \alpha(v+W)=(\alpha v)+W$$

In this case, the linear map $$p: V\rightarrow V/W$$ sending any $$v\in V$$ to $$v+W$$ is called the *natural projection*.
:::

In the above definition, addition and scalar multiplication are described via a representative vector $$v$$ of the coset, so we must check that they are well defined independent of the choice of representative. That is, if $$v+W=v_1+W$$ and $$v'+W=v_1'+W$$, then

$$(v+v')+W=(v_1+v_1')+W,\qquad (\alpha v)+W=(\alpha v_1)+W$$

must hold. By assumption $$v-v_1\in W$$ and $$v'-v_1'\in W$$, so from the fact that $$W$$ is closed under addition,

$$(v+v')-(v_1+v_1')=(v-v_1)+(v'-v_1')\in W$$

and from the fact that $$W$$ is closed under scalar multiplication,

$$(\alpha v)-(\alpha v_1)=\alpha(v-v_1)\in W$$

By [Lemma 2](#lem2) this is exactly the equation we wanted. Therefore the two operations on $$V/W$$ are well defined.

::: Proposition 4
The set $$V/W$$ equipped with the operations from [Definition 3](#def3) is a $$\mathbb{K}$$-vector space. The additive identity is $$0+W=W$$, and the additive inverse of $$v+W$$ is $$(-v)+W$$.
:::
::: Proof
All vector space axioms follow immediately from the fact that the operations on $$V/W$$ are induced from those on $$V$$ coset-wise. For example, the associativity of addition follows from the fact that for any $$v,v',v''\in V$$,

$$\bigl((v+W)+(v'+W)\bigr)+(v''+W)=\bigl((v+v')+v''\bigr)+W=\bigl(v+(v'+v'')\bigr)+W=(v+W)+\bigl((v'+W)+(v''+W)\bigr)$$

which is a direct consequence of the associativity of addition in $$V$$. Commutativity, distributivity, and the scalar multiplication axioms are verified in the same way. On the other hand, for any $$v\in V$$,

$$(v+W)+(0+W)=(v+0)+W=v+W,\qquad (v+W)+((-v)+W)=(v-v)+W=0+W$$

so $$0+W$$ is the additive identity and $$(-v)+W$$ is the inverse of $$v+W$$.
:::

## Dimension of the Quotient Space

The only invariant of a vector space is its dimension. In the case of $$V/W$$, its dimension is determined immediately from the dimensions of $$V$$ and $$W$$.

::: Theorem 5
For a finite-dimensional $$\mathbb{K}$$-vector space $$V$$ and its subspace $$W\leq V$$, the formula

$$\dim(V/W)=\dim V-\dim W$$

holds.
:::
::: Proof
Let $$\dim W=k$$, $$\dim V=n$$, and choose a basis $$\{x_1,\ldots, x_k\}$$ of $$W$$. This is a linearly independent subset of $$V$$, so by [§Dimension of Vector Spaces, ⁋Proposition 5](/en/math/linear_algebra/dimension#prop5) we can extend it to a basis $$\{x_1,\ldots, x_k, x_{k+1},\ldots, x_n\}$$ of $$V$$. We show that the following cosets

$$x_{k+1}+W,\quad\ldots,\quad x_n+W$$

form a basis of $$V/W$$.

First, they span $$V/W$$. For any $$v\in V$$, if $$v=\sum_{i=1}^n\alpha_ix_i$$ then

$$v+W=\sum_{i=1}^n\alpha_i(x_i+W)=\sum_{i=k+1}^n\alpha_i(x_i+W)$$

where the last equality holds because for $$i\leq k$$ we have $$x_i\in W$$, so $$x_i+W=W$$ is the zero vector of $$V/W$$.

Next, to show they are linearly independent, suppose for scalars $$\alpha_{k+1},\ldots,\alpha_n$$ that

$$\sum_{i=k+1}^n\alpha_i(x_i+W)=0+W$$

Then as seen before, $$\sum_{i=k+1}^n\alpha_ix_i+W=W=0+W$$, so by [Lemma 2](#lem2) we have $$\sum_{i=k+1}^n\alpha_ix_i\in W$$. Hence we can express this vector in terms of the basis of $$W$$, so for suitable scalars $$\beta_1,\ldots,\beta_k$$,

$$\sum_{i=k+1}^n\alpha_ix_i=\sum_{i=1}^k\beta_ix_i$$

and rearranging gives

$$-\sum_{i=1}^k\beta_ix_i+\sum_{i=k+1}^n\alpha_ix_i=0$$

But the left-hand side is a linear combination of $$\{x_1,\ldots, x_n\}$$, and since these form a basis of $$V$$ they are linearly independent, so all coefficients must be $$0$$; in particular $$\alpha_{k+1}=\cdots=\alpha_n=0$$.

Therefore $$\{x_{k+1}+W,\ldots, x_n+W\}$$ is a basis of $$V/W$$, and since it has $$n-k$$ elements, $$\dim(V/W)=n-k=\dim V-\dim W$$.
:::

## First Isomorphism Theorem

One reason this post exists as a separate article is to give a more essential meaning to [§Isomorphisms, ⁋Theorem 7](/en/math/linear_algebra/isomorphic_vector_spaces#thm7). In this final section we resolve this.

For any $$\mathbb{K}$$-vector space $$V$$ and subspace $$W\leq V$$, consider the function $$p:V\rightarrow V/W$$ defined by the formula

$$p(v)=v+W$$

Then the operations in [Definition 3](#def3) are defined precisely so that $$p$$ satisfies the two equations

$$p(\alpha v)=(\alpha v)+W=\alpha(v+W)=\alpha  p(v),\qquad p(v+v')=(v+v')+W=(v+W)+(v'+W)=p(v)+p(v')$$

That is, $$p$$ is a linear map, and we call it the *natural projection* from $$V$$ to $$V/W$$. By definition $$p$$ is surjective, and

$$\ker p=\{v\in V\mid v+W=W\}=W$$

From this we see that any subspace can be realized as the kernel of a suitable linear map.

The most important property of the natural projection is the following universal property. It says that any linear map sending $$W$$ to $$0$$ factors uniquely through $$V/W$$.

::: Proposition 6
Let a $$\mathbb{K}$$-vector space $$V$$ and a subspace $$W\leq V$$ be given, and let $$L:V\rightarrow U$$ be a linear map to another $$\mathbb{K}$$-vector space $$U$$ satisfying $$W\subseteq\ker L$$. Then the linear map $$\bar L:V/W\rightarrow U$$ defined by the formula

$$\bar L(v+W)=L(v)$$

exists uniquely and satisfies $$L=\bar L\circ p$$.
:::
::: Proof
First we show that $$\bar L$$ is well defined. If $$v+W=v'+W$$, then $$v-v'\in W\subseteq\ker L$$, so

$$L(v)-L(v')=L(v-v')=0$$

and therefore $$L(v)=L(v')$$. That is, the value of $$\bar L(v+W)$$ is independent of the choice of representative. That $$\bar L$$ is linear follows from

$$\bar L\bigl(\alpha(v+W)+(v'+W)\bigr)=\bar L\bigl((\alpha v+v')+W\bigr)=L(\alpha v+v')=\alpha L(v)+L(v')=\alpha\bar L(v+W)+\bar L(v'+W)$$

Also, for any $$v\in V$$ we have $$(\bar L\circ p)(v)=\bar L(v+W)=L(v)$$, so $$L=\bar L\circ p$$. Finally, if a linear map $$L':V/W\rightarrow U$$ satisfying $$L=L'\circ p$$ is given, then since $$p$$ is surjective, for any $$v+W\in V/W$$ we have $$L'(v+W)=L'(p(v))=L(v)=\bar L(v+W)$$, and therefore $$L'=\bar L$$.
:::

In particular, applying the above universal property to the case $$W=\ker L$$ yields the following theorem, which is central to classifying vector spaces.

::: Theorem 7 (First Isomorphism Theorem)
For two $$\mathbb{K}$$-vector spaces $$V,U$$ and a linear map $$L:V\rightarrow U$$, the linear map $$\bar L:V/\ker L\rightarrow \im L$$ defined by the formula

$$\bar L(v+\ker L)=L(v)$$

is an isomorphism. That is, $$V/\ker L\cong\im L$$.
:::
::: Proof
Setting $$W=\ker L$$, by [Proposition 6](#prop6) the linear map $$\bar L:V/\ker L\rightarrow U$$ defined by $$\bar L(v+\ker L)=L(v)$$ is well defined, and its image equals $$\im L$$. Therefore, restricting the codomain to $$\im L$$, the map $$\bar L:V/\ker L\rightarrow\im L$$ is surjective. On the other hand, if $$\bar L(v+\ker L)=0$$, then $$L(v)=0$$, i.e. $$v\in\ker L$$, so $$v+\ker L=\ker L$$ is the zero vector of $$V/\ker L$$. Hence $$\ker\bar L=\{0\}$$, and therefore $$\bar L$$ is injective. ([§Linear Maps, ⁋Proposition 8](/en/math/linear_algebra/linear_map#prop8)) That is, $$\bar L$$ is a bijective linear map, and thus an isomorphism. ([§Isomorphisms, ⁋Lemma 2](/en/math/linear_algebra/isomorphic_vector_spaces#lem2))
:::

Combining [Theorem 7](#thm7) and [Theorem 5](#thm5) above, we recover the rank-nullity theorem. Indeed, for finite-dimensional $$V$$,

$$\rank L=\dim\im L=\dim(V/\ker L)=\dim V-\dim\ker L=\dim V-\nullity L$$

holds, which is exactly the formula of [§Isomorphisms, ⁋Theorem 7](/en/math/linear_algebra/isomorphic_vector_spaces#thm7). That is, the rank-nullity theorem is nothing more than the statement that after "collapsing" $$\ker L$$, $$L$$ becomes injective, expressed in the language of dimensions.

---

**References**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.

---
