---
title: "Quotient Spaces"
description: "We construct the quotient space of a vector space by a subspace using cosets, and prove the well-definedness of operations and the dimension formula. Furthermore, we examine the natural projection, the universal property, and the first isomorphism theorem."
excerpt: "Quotient spaces by subspaces"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/quotient_space
sidebar: 
    nav: "linear_algebra-en"


date: 2026-06-19

weight: 8
translated_at: 2026-08-19T18:15:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-17T23:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
In this post, for a $\mathbb{K}$-vector space $V$ and its subspace $W$, we define its *quotient space* $V/W$. Intuitively, this is the space obtained inside $V$ by making all elements of $W$ equal to $0$; however, since we want the space remaining even after making all elements of $W$ equal to $0$ like this to still be a vector space, simply declaring all elements of $W$ to be $0$ cannot achieve this. 

## Cosets

The main problem, as pointed out above, is that merely setting all elements of $W$ to $0$ gives no guarantee that the remaining space will be a vector space. For instance, for this to be a vector space, it must first be closed under operations, but any element of $V$, $v$, can always be written, for a fixed $0\neq w\in W$, in the form $v=(v-w)+w$; thus if $v$ and $v-w$ do not belong to $W$, then even after treating all elements of $W$ as $0$, we have

$$v-(v-w)=w=0$$

so that even though $v$ and $v-w$ are not equal, their difference becomes $0$.

This shows two things. First, to define $V/W$, it is insufficient to simply set all elements of $W$ to $0$ and leave the remaining elements as they are. Second, and more importantly, the simple calculation above actually gives a hint as to how to construct $V/W$: namely, if the difference of two vectors $v,v'$ lies in $W$, then we must treat them inside $V/W$ as the *same* element. 

::: Definition 1
Let a $\mathbb{K}$-vector space $V$ and its subspace $W\leq V$ be given. For any $v\in V$, the following set

$$v+W=\{v+w\mid w\in W\}$$

is called the *coset* containing $v$ of $W$.
:::

In the definition, the coset $v+W$ is the set of all vectors whose difference from $v$ belongs to $W$, that is, the set of all vectors that we agreed in the introduction to treat inside $V/W$ as equal to $v$. This is an example of an equivalence class treated in set theory ([\[Set Theory\] §Equivalence Relations, ⁋Definition 4](/en/math/set_theory/equivalence_relations#def4){: data-lid="vzbna" }), but all we need is the following fact, claimed in the introduction above, that determines whether two cosets are equal by the difference of their representatives.

::: Lemma 2
For a $\mathbb{K}$-vector space $V$, its subspace $W\leq V$, and any two vectors $v,v'\in V$, the equivalence

$$v+W=v'+W\iff v-v'\in W$$

holds.
:::
::: Proof
First, if $v-v'\in W$, then for any representative $v+w\in v+W$ we have $v+w=v'+\bigl((v-v')+w\bigr)\in v'+W$, and the converse holds in the same way, so $v+W=v'+W$. 

Conversely, if $v+W=v'+W$, then since $v=v+0\in v'+W$, we have $v=v'+w$ for some $w\in W$, and therefore $v-v'=w\in W$.
:::

In particular, $v+W=W$ is equivalent to $v\in W$, and from this we see that two distinct cosets are always disjoint.

## Definition of the Quotient Space

Now we endow the cosets with a vector space structure. 

::: Definition 3
For a $\mathbb{K}$-vector space $V$ and its subspace $W\leq V$, we denote the set of all cosets of $W$ by $V/W$ and call it the *quotient space* by $W$ of $V$. Addition and scalar multiplication on $V/W$ are defined respectively by

$$(v+W)+(v'+W)=(v+v')+W,\qquad \alpha(v+W)=(\alpha v)+W$$

Here, the linear map sending any $v\in V$ to $v+W$, $p: V\rightarrow V/W$, is called the *natural projection*. 
:::

In the definition above, addition and scalar multiplication are described via a vector $v$ representing the coset, so we must check that they are well defined independently of the choice of representative. That is, if $v+W=v_1+W$ and $v'+W=v_1'+W$, then 

$$(v+v')+W=(v_1+v_1')+W,\qquad (\alpha v)+W=(\alpha v_1)+W$$

must hold. By assumption, $v-v_1\in W$ and $v'-v_1'\in W$, so from the fact that $W$ is closed under addition,

$$(v+v')-(v_1+v_1')=(v-v_1)+(v'-v_1')\in W$$

and from the fact that $W$ is closed under scalar multiplication,

$$(\alpha v)-(\alpha v_1)=\alpha(v-v_1)\in W$$

as well. By [Lemma 2](#lem2){: data-lid="sig9k" }, this is precisely the equality we wanted. Therefore, the two operations on $V/W$ are well defined.

::: Proposition 4
Equipped with the operations of [Definition 3](#def3){: data-lid="5wsju" }, $V/W$ is a $\mathbb{K}$-vector space. Here, the additive identity is $0+W=W$, and the additive inverse of $v+W$ is $(-v)+W$.
:::
::: Proof
All axioms of a vector space follow immediately from the fact that the operations on $V/W$ are induced coset-wise from the operations on $V$. For example, associativity of addition follows from the fact that for any $v,v',v''\in V$,

$$\bigl((v+W)+(v'+W)\bigr)+(v''+W)=\bigl((v+v')+v''\bigr)+W=\bigl(v+(v'+v'')\bigr)+W=(v+W)+\bigl((v'+W)+(v''+W)\bigr)$$

holds, which is a direct consequence of the associativity of addition in $V$. Commutativity, distributivity, and the axioms for scalar multiplication are also verified in the same way. On the other hand, since for any $v\in V$,

$$(v+W)+(0+W)=(v+0)+W=v+W,\qquad (v+W)+((-v)+W)=(v-v)+W=0+W$$

$0+W$ is the additive identity and $(-v)+W$ is the inverse of $v+W$.
:::

## Dimension of the Quotient Space

The only invariant of a vector space is its dimension. If $V$ is finite-dimensional, then in the case of $V/W$, its dimension is determined immediately from the dimensions of $V$ and $W$.

::: Theorem 5
For a finite-dimensional $\mathbb{K}$-vector space $V$ and its subspace $W\leq V$, the formula

$$\dim(V/W)=\dim V-\dim W$$

holds.
:::
::: Proof
Let $\dim W=k$, $\dim V=n$, and choose a basis of $W$, say $\{x_1,\ldots, x_k\}$. Since this is a linearly independent subset of $V$, by [§Dimension of Vector Spaces, ⁋Proposition 5](/en/math/linear_algebra/dimension#prop5){: data-lid="68z3f" } we can extend it to obtain a basis of $V$, $\{x_1,\ldots, x_k, x_{k+1},\ldots, x_n\}$. We show that the cosets

$$x_{k+1}+W,\quad\ldots,\quad x_n+W$$

form a basis of $V/W$.

First, they span $V/W$. For any $v\in V$, if $v=\sum_{i=1}^n\alpha_ix_i$, then

$$v+W=\sum_{i=1}^n\alpha_i(x_i+W)=\sum_{i=k+1}^n\alpha_i(x_i+W)$$

where the last equality holds because for $i\leq k$, $x_i\in W$ and so $x_i+W=W$ is the zero vector of $V/W$.

Next, to show that they are linearly independent, suppose that for scalars $\alpha_{k+1},\ldots,\alpha_n$,

$$\sum_{i=k+1}^n\alpha_i(x_i+W)=0+W$$

Then, as seen above, $\sum_{i=k+1}^n\alpha_ix_i+W=W=0+W$, so by [Lemma 2](#lem2){: data-lid="karqj" } we have $\sum_{i=k+1}^n\alpha_ix_i\in W$. Therefore, expressing this vector in terms of a basis of $W$, for suitable scalars $\beta_1,\ldots,\beta_k$ we can write

$$\sum_{i=k+1}^n\alpha_ix_i=\sum_{i=1}^k\beta_ix_i$$

which rearranges to

$$-\sum_{i=1}^k\beta_ix_i+\sum_{i=k+1}^n\alpha_ix_i=0$$

The left-hand side is a linear combination of $\{x_1,\ldots, x_n\}$, and since these form a basis of $V$ they are linearly independent, so all coefficients must be $0$; in particular, $\alpha_{k+1}=\cdots=\alpha_n=0$.

Therefore, $\{x_{k+1}+W,\ldots, x_n+W\}$ is a basis of $V/W$, and since it has $n-k$ elements, $\dim(V/W)=n-k=\dim V-\dim W$.
:::

## First Isomorphism Theorem

One reason this post exists as a separate article is to give a more essential meaning to [§Isomorphisms, ⁋Theorem 7](/en/math/linear_algebra/isomorphic_vector_spaces#thm7){: data-lid="xyiwg" }. In this final section we resolve this.

For any $\mathbb{K}$-vector space $V$ and subspace $W\leq V$, consider the formula

$$p(v)=v+W$$

which defines a function $p:V\rightarrow V/W$. Then the operations of [Definition 3](#def3){: data-lid="iuq5d" } are defined precisely so that $p$ satisfies the two identities

$$p(\alpha v)=(\alpha v)+W=\alpha(v+W)=\alpha  p(v),\qquad p(v+v')=(v+v')+W=(v+W)+(v'+W)=p(v)+p(v')$$

That is, $p$ is a linear map, called the *natural projection* from $V$ to $V/W$. By definition $p$ is surjective, and

$$\ker p=\{v\in V\mid v+W=W\}=W$$

holds. From this we see that any subspace can be realized as the kernel of a suitable linear map.

The most important property of the natural projection is the following universal property. This says that any linear map sending $W$ to $0$ factors uniquely through $V/W$.

::: Proposition 6
Let a $\mathbb{K}$-vector space $V$, a subspace $W\leq V$, and a linear map to another $\mathbb{K}$-vector space $U$, $L:V\rightarrow U$, satisfy $W\subseteq\ker L$. Then, defined by the equation

$$\bar{L}(v+W)=L(v)$$

there exists a unique linear map $\bar{L}:V/W\rightarrow U$ such that $L=\bar{L}\circ p$.
:::
::: Proof
First we show that $\bar{L}$ is well defined. If $v+W=v'+W$, then $v-v'\in W\subseteq\ker L$, so

$$L(v)-L(v')=L(v-v')=0$$

and hence $L(v)=L(v')$. Thus the value of $\bar{L}(v+W)$ is independent of the choice of representative. That $\bar{L}$ is linear follows from

$$\bar{L}\bigl(\alpha(v+W)+(v'+W)\bigr)=\bar{L}\bigl((\alpha v+v')+W\bigr)=L(\alpha v+v')=\alpha L(v)+L(v')=\alpha\bar{L}(v+W)+\bar{L}(v'+W)$$

Also, for any $v\in V$ we have $(\bar{L}\circ p)(v)=\bar{L}(v+W)=L(v)$, so $L=\bar{L}\circ p$. Finally, if $L=L'\circ p$ holds for a linear map $L':V/W\rightarrow U$, then since $p$ is surjective, for any $v+W\in V/W$ we have $L'(v+W)=L'(p(v))=L(v)=\bar{L}(v+W)$, and therefore $L'=\bar{L}$.
:::

In particular, applying the above universal property to the case $W=\ker L$ yields the following theorem, which is central to classifying vector spaces.

::: Theorem 7 (First Isomorphism Theorem)
For two $\mathbb{K}$-vector spaces $V,U$ and a linear map $L:V\rightarrow U$, defined by the equation

$$\bar{L}(v+\ker L)=L(v)$$

the linear map $\bar{L}:V/\ker L\rightarrow \im L$ is an isomorphism. That is, $V/\ker L\cong\im L$.
:::
::: Proof
Setting $W=\ker L$, by [Proposition 6](#prop6){: data-lid="hbvay" }, the linear map defined by $\bar{L}(v+\ker L)=L(v)$, namely $\bar{L}:V/\ker L\rightarrow U$, is well defined, and its image equals $\im L$. Restricting the codomain to $\im L$, we obtain that $\bar{L}:V/\ker L\rightarrow\im L$ is surjective. On the other hand, if $\bar{L}(v+\ker L)=0$, then $L(v)=0$, i.e. $v\in\ker L$, so $v+\ker L=\ker L$ is the zero vector of $V/\ker L$. Hence $\ker\bar{L}=\{0\}$, and therefore $\bar{L}$ is injective. ([§Linear Maps, ⁋Proposition 8](/en/math/linear_algebra/linear_map#prop8){: data-lid="o5uu6" }) Thus $\bar{L}$ is a bijective linear map, hence an isomorphism. ([§Isomorphisms, ⁋Lemma 2](/en/math/linear_algebra/isomorphic_vector_spaces#lem2){: data-lid="8qnn6" })
:::

Combining [Theorem 7](#thm7){: data-lid="3upyz" } and [Theorem 5](#thm5){: data-lid="10mfu" } above, we recover the rank-nullity theorem. Indeed, for finite-dimensional $V$,

$$\rank L=\dim\im L=\dim(V/\ker L)=\dim V-\dim\ker L=\dim V-\nullity L$$

holds, which is exactly the formula of [§Isomorphisms, ⁋Theorem 7](/en/math/linear_algebra/isomorphic_vector_spaces#thm7){: data-lid="nhl7t" }. In other words, the rank-nullity theorem is nothing more than the statement that $L$ becomes injective after "folding away" $\ker L$, expressed in the language of dimensions.

---

**References**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.

---
