---
title: "Quotient Spaces"
description: "We construct quotient spaces of a vector space by a subspace using cosets, and prove well-definedness of operations and the dimension formula. We also examine the natural projection, universal property, and the first isomorphism theorem."
excerpt: "Quotient spaces of vector spaces by subspaces"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/quotient_space
sidebar: 
    nav: "linear_algebra-en"


date: 2026-06-19

weight: 8
translated_at: 2026-08-16T05:47:06+00:00
translation_source: kimi-cli
---
In this post, we define the *quotient space* $V/W$ for a $\mathbb{K}$-vector space $V$ and its subspace $W$. Intuitively, this is the space obtained from $V$ by making every element of $W$ equal to $0$; however, since we want the remaining space to still be a vector space, simply declaring all elements of $W$ to be $0$ is not enough to achieve this.

## Cosets

The biggest problem, as pointed out above, is that merely setting all elements of $W$ to $0$ gives no guarantee that the remaining space will be a vector space. For this to be a vector space, it must first be closed under operations: for any element $v$ of $V$ and any fixed $0\neq w\in W$, we can always write $v=(v-w)+w$, so if $v$ and $v-w$ do not belong to $W$, then even after treating all elements of $W$ as $0$ we get

$$v-(v-w)=w=0,$$

so the difference of $v$ and $v-w$ becomes $0$ even though they are not equal.

This shows two things. First, to define $V/W$ it is insufficient to simply set all elements of $W$ to $0$ and leave the rest unchanged. Second, and more importantly, the simple calculation above actually gives a hint as to how to construct $V/W$: namely, if the difference of two vectors $v,v'$ lies in $W$, then we must regard them as the *same* element inside $V/W$.

::: Definition 1
Let a $\mathbb{K}$-vector space $V$ and its subspace $W\leq V$ be given. For any $v\in V$, the set

$$v+W=\{v+w\mid w\in W\}$$

is called the *coset* of $W$ containing $v$.
:::

By definition, the coset $v+W$ is the set of all vectors whose difference from $v$ lies in $W$, i.e. the vectors that we agreed to treat as equal to $v$ in $V/W$. This is an example of an equivalence class from set theory ([\[Set Theory\] §Equivalence Relations, ⁋Definition 4](/en/math/set_theory/equivalence_relations#def4)), but all we need is the following fact, claimed in the introduction, that two cosets are equal precisely when the difference of their representatives lies in $W$.

::: Lemma 2
For a $\mathbb{K}$-vector space $V$, its subspace $W\leq V$, and any two vectors $v,v'\in V$, the equivalence

$$v+W=v'+W\iff v-v'\in W$$

holds.
:::
::: Proof
First, if $v-v'\in W$, then for any representative $v+w\in v+W$ we have $v+w=v'+\bigl((v-v')+w\bigr)\in v'+W$, and the converse holds in the same way, so $v+W=v'+W$.

Conversely, if $v+W=v'+W$, then $v=v+0\in v'+W$, so there exists $w\in W$ with $v=v'+w$, and therefore $v-v'=w\in W$.
:::

In particular, $v+W=W$ is equivalent to $v\in W$, and from this we know that two distinct cosets are always disjoint.

## Definition of the Quotient Space

Now we endow the cosets with a vector space structure.

::: Definition 3
For a $\mathbb{K}$-vector space $V$ and its subspace $W\leq V$, we write the set of all cosets of $W$ as $V/W$ and call it the *quotient space* of $V$ by $W$. Addition and scalar multiplication on $V/W$ are defined respectively by

$$(v+W)+(v'+W)=(v+v')+W,\qquad \alpha(v+W)=(\alpha v)+W.$$

The linear map $p: V\rightarrow V/W$ sending any $v\in V$ to $v+W$ is called the *natural projection*.
:::

In the above definition, addition and scalar multiplication are described via a representing vector $v$, so we must check that they are well defined independent of the choice of representative. That is, if $v+W=v_1+W$ and $v'+W=v_1'+W$, then

$$(v+v')+W=(v_1+v_1')+W,\qquad (\alpha v)+W=(\alpha v_1)+W$$

must hold. By assumption $v-v_1\in W$ and $v'-v_1'\in W$, so since $W$ is closed under addition,

$$(v+v')-(v_1+v_1')=(v-v_1)+(v'-v_1')\in W,$$

and since $W$ is closed under scalar multiplication,

$$(\alpha v)-(\alpha v_1)=\alpha(v-v_1)\in W.$$

By [Lemma 2](#lem2) this is exactly the equality we wanted. Hence the two operations on $V/W$ are well defined.

::: Proposition 4
The set $V/W$ equipped with the operations of [Definition 3](#def3) is a $\mathbb{K}$-vector space. The additive identity is $0+W=W$, and the additive inverse of $v+W$ is $(-v)+W$.
:::
::: Proof
All vector space axioms follow immediately from the fact that the operations on $V/W$ are induced coset-wise from those on $V$. For example, associativity of addition follows from

$$\bigl((v+W)+(v'+W)\bigr)+(v''+W)=\bigl((v+v')+v''\bigr)+W=\bigl(v+(v'+v'')\bigr)+W=(v+W)+\bigl((v'+W)+(v''+W)\bigr)$$

for any $v,v',v''\in V$, which is a direct consequence of associativity of addition in $V$. Commutativity, distributivity, and the scalar multiplication axioms are verified in the same way. On the other hand, for any $v\in V$,

$$(v+W)+(0+W)=(v+0)+W=v+W,\qquad (v+W)+((-v)+W)=(v-v)+W=0+W,$$

so $0+W$ is the additive identity and $(-v)+W$ is the inverse of $v+W$.
:::

## Dimension of the Quotient Space

The only invariant of a vector space is its dimension. If $V$ is finite-dimensional, then the dimension of $V/W$ is determined immediately from the dimensions of $V$ and $W$.

::: Theorem 5
For a finite-dimensional $\mathbb{K}$-vector space $V$ and its subspace $W\leq V$, the identity

$$\dim(V/W)=\dim V-\dim W$$

holds.
:::
::: Proof
Let $\dim W=k$, $\dim V=n$, and choose a basis $\{x_1,\ldots, x_k\}$ of $W$. Since this is a linearly independent subset of $V$, by [§Dimension of Vector Spaces, ⁋Proposition 5](/en/math/linear_algebra/dimension#prop5) we can extend it to a basis $\{x_1,\ldots, x_k, x_{k+1},\ldots, x_n\}$ of $V$. We show that the cosets

$$x_{k+1}+W,\quad\ldots,\quad x_n+W$$

form a basis of $V/W$.

First, they span $V/W$. For any $v\in V$, if $v=\sum_{i=1}^n\alpha_ix_i$ then

$$v+W=\sum_{i=1}^n\alpha_i(x_i+W)=\sum_{i=k+1}^n\alpha_i(x_i+W),$$

where the last equality holds because $x_i\in W$ for $i\leq k$, so $x_i+W=W$ is the zero vector of $V/W$.

Next, to show linear independence, let scalars $\alpha_{k+1},\ldots,\alpha_n$ satisfy

$$\sum_{i=k+1}^n\alpha_i(x_i+W)=0+W.$$

Then, as seen above, $\sum_{i=k+1}^n\alpha_ix_i+W=W=0+W$, so by [Lemma 2](#lem2) we have $\sum_{i=k+1}^n\alpha_ix_i\in W$. Hence we can express this vector in the basis of $W$ to obtain scalars $\beta_1,\ldots,\beta_k$ such that

$$\sum_{i=k+1}^n\alpha_ix_i=\sum_{i=1}^k\beta_ix_i,$$

which rearranges to

$$-\sum_{i=1}^k\beta_ix_i+\sum_{i=k+1}^n\alpha_ix_i=0.$$

The left-hand side is a linear combination of $\{x_1,\ldots, x_n\}$, and since these form a basis of $V$ they are linearly independent, so all coefficients must be $0$; in particular $\alpha_{k+1}=\cdots=\alpha_n=0$.

Therefore $\{x_{k+1}+W,\ldots, x_n+W\}$ is a basis of $V/W$, and since it has $n-k$ elements, $\dim(V/W)=n-k=\dim V-\dim W$.
:::

## First Isomorphism Theorem

One reason this post exists as a separate article is to give a more essential meaning to [§Isomorphisms, ⁋Theorem 7](/en/math/linear_algebra/isomorphic_vector_spaces#thm7). In this final section we resolve this.

For any $\mathbb{K}$-vector space $V$ and subspace $W\leq V$, consider the function $p:V\rightarrow V/W$ defined by

$$p(v)=v+W.$$

Then the operations of [Definition 3](#def3) are defined precisely so that $p$ satisfies the two identities

$$p(\alpha v)=(\alpha v)+W=\alpha(v+W)=\alpha  p(v),\qquad p(v+v')=(v+v')+W=(v+W)+(v'+W)=p(v)+p(v').$$

That is, $p$ is a linear map, called the *natural projection* from $V$ to $V/W$. By definition $p$ is surjective, and

$$\ker p=\{v\in V\mid v+W=W\}=W$$

holds. From this we see that any subspace can be realized as the kernel of a suitable linear map.

The most important property of the natural projection is the following universal property. It says that any linear map sending $W$ to $0$ factors uniquely through $V/W$.

::: Proposition 6
Let $V$ be a $\mathbb{K}$-vector space, $W\leq V$ a subspace, and $L:V\rightarrow U$ a linear map to another $\mathbb{K}$-vector space $U$ satisfying $W\subseteq\ker L$. Then there exists a unique linear map $\bar L:V/W\rightarrow U$ defined by

$$\bar L(v+W)=L(v)$$

such that $L=\bar L\circ p$.
:::
::: Proof
First we show that $\bar L$ is well defined. If $v+W=v'+W$, then $v-v'\in W\subseteq\ker L$, so

$$L(v)-L(v')=L(v-v')=0$$

and hence $L(v)=L(v')$. Thus the value of $\bar L(v+W)$ is independent of the choice of representative. That $\bar L$ is linear follows from

$$\bar L\bigl(\alpha(v+W)+(v'+W)\bigr)=\bar L\bigl((\alpha v+v')+W\bigr)=L(\alpha v+v')=\alpha L(v)+L(v')=\alpha\bar L(v+W)+\bar L(v'+W).$$

Also, for any $v\in V$ we have $(\bar L\circ p)(v)=\bar L(v+W)=L(v)$, so $L=\bar L\circ p$. Finally, if a linear map $L':V/W\rightarrow U$ satisfies $L=L'\circ p$, then since $p$ is surjective, for any $v+W\in V/W$ we have $L'(v+W)=L'(p(v))=L(v)=\bar L(v+W)$, and therefore $L'=\bar L$.
:::

Applying the above universal property to the case $W=\ker L$ yields the following theorem, which is central to classifying vector spaces.

::: Theorem 7 (First Isomorphism Theorem)
For two $\mathbb{K}$-vector spaces $V,U$ and a linear map $L:V\rightarrow U$, the linear map $\bar L:V/\ker L\rightarrow \im L$ defined by

$$\bar L(v+\ker L)=L(v)$$

is an isomorphism. That is, $V/\ker L\cong\im L$.
:::
::: Proof
Setting $W=\ker L$, [Proposition 6](#prop6) gives that the linear map $\bar L:V/\ker L\rightarrow U$ defined by $\bar L(v+\ker L)=L(v)$ is well defined, and its image equals $\im L$. Restricting the codomain to $\im L$, we obtain that $\bar L:V/\ker L\rightarrow\im L$ is surjective. On the other hand, if $\bar L(v+\ker L)=0$, then $L(v)=0$, i.e. $v\in\ker L$, so $v+\ker L=\ker L$ is the zero vector of $V/\ker L$. Hence $\ker\bar L=\{0\}$, and therefore $\bar L$ is injective. ([§Linear Maps, ⁋Proposition 8](/en/math/linear_algebra/linear_map#prop8)) Thus $\bar L$ is a bijective linear map, hence an isomorphism. ([§Isomorphisms, ⁋Lemma 2](/en/math/linear_algebra/isomorphic_vector_spaces#lem2))
:::

Combining [Theorem 7](#thm7) and [Theorem 5](#thm5) above, we recover the rank-nullity theorem. Indeed, for finite-dimensional $V$,

$$\rank L=\dim\im L=\dim(V/\ker L)=\dim V-\dim\ker L=\dim V-\nullity L$$

holds, which is exactly the formula of [§Isomorphisms, ⁋Theorem 7](/en/math/linear_algebra/isomorphic_vector_spaces#thm7). In other words, the rank-nullity theorem is nothing more than the statement that after "folding away" $\ker L$, $L$ becomes injective, expressed in the language of dimensions.

---

**References**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.

---
