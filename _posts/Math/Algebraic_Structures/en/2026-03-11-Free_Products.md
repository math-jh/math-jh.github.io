---
title: "Free Products"
description: "We prove the existence of free products and their universal property, then explain the construction of free products using the definition of free groups and adjoint functors."
excerpt: "Free products and the universal property"

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/free_products
sidebar: 
    nav: "algebraic_structures-en"

date: 2022-12-07
weight: 9
translated_at: 2026-08-16T12:45:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-08-16T12:45:04+00:00
---
Unlike the case of abelian groups, the weak direct product defined in the previous post does not satisfy the universal property for general groups.

::: Example 1
Consider an arbitrary nonabelian group $G$, and let $a,b\in G$ satisfy $ab\neq ba$. Define group homomorphisms $f_1, f_2: (\mathbb{Z},+)\rightarrow (G,\cdot)$ by

$$f_1(1)=a, \qquad f_2(1)=b.$$

Since the index set $I=\{1,2\}$ is finite, the weak direct product of two copies of $(\mathbb{Z},+)$ coincides with $\mathbb{Z}\times\mathbb{Z}$.

However, we see that there is no map $f:\mathbb{Z}\times\mathbb{Z}\rightarrow G$ making the following diagram

{% diagram Math/Algebraic_Structures/Free_Products-1.svg width="11.41em" alt="counterexample" %}

commute. Indeed, if such an $f$ existed then

$$\begin{aligned}ab&=f_1(1)f_2(1)=f(\iota_1(1))f(\iota_2(1))=f(\iota_1(1)+\iota_2(1))\\
&=f(\iota_2(1)+\iota_1(1))=f(\iota_2(1))f(\iota_1(1))=f_2(1)f_1(1)\\
&=ba\end{aligned}$$

which contradicts the choice of $a$ and $b$.
:::

Therefore, to find an object satisfying the universal property among general groups, just as the direct sum does, we must introduce a new construction. To this end, we first define the free group.

## Free group

Any group $G$ can be regarded as a set equipped with a binary operation, an identity element, and inverses. Moreover, any group homomorphism can naturally be viewed as a function between sets. That is, there is a forgetful functor $U: \Grp \rightarrow\Set$. In this section we define the left adjoint $F:\Set \rightarrow\Grp$ of $U$. By the definition of a left adjoint functor, this is a functor satisfying the natural isomorphism

$$\Hom_\Set(X, U(G))\cong\Hom_\Grp(F(X), G)$$

([\[Category Theory\] §Adjoint Functors, ⁋Definition 1](/en/math/category_theory/adjoints#def1)). In other words, for any set $X$ and any group $G$, the functor $F$ yields a bijection that uniquely assigns to each $f\in\Hom_\Set(X, U(G))$ an element of $\Hom_\Grp(F(X),G)$. Rewriting this, we obtain the following.

::: Definition 2
For a set $X$, the *free group* $F(X)$ defined by $X$ is the solution $(F(X), \eta_X\in\Hom_\Set(X,UF(X)))$ of the following universal mapping problem.

> For any group $G$, if a function $f:X\rightarrow U(G)$ is given, then there exists a unique group homomorphism $\hat{f}:F(X)\rightarrow G$ satisfying $U(\hat{f})\circ\eta_X=f$.
:::

Here $\eta_X$ is nothing but the unit of the adjunction $F\dashv U$. Of course, to make this work we must actually construct $F(X)$.

We outline the general idea. First, consider a set $X^{-1}$ disjoint from $X$ and having the same cardinality. There is no reason for $X^{-1}$ to be any special set, but we choose a bijection $X\rightarrow X^{-1}$ and denote the image of $x\in X$ in $X^{-1}$ by $x^{-1}$. Also, choose a singleton set disjoint from $X\cup X^{-1}$ and denote its element by $e$.

Then the elements of the group $F$ are the collection of *reduced words* defined by the set $X\cup X^{-1}\cup \{e\}$. Here a *word* is simply a sequence of elements of $X\cup X^{-1}\cup \{e\}$; if the same element appears twice in a row as in $xx$, or if two inverse elements appear consecutively as in $xx^{-1}$ or $x^{-1}x$, or if $e$ appears between two letters or at either end of a word as in $xey$, then these can be reduced to $x^2$, $e$, and $xy$ respectively. However, if for instance $y\neq x^{-1}$, there is no way to reduce $xyx$. Such a reduced expression is called a *reduced word*.

Every word can be reduced to a reduced word.[^1] Let us define the operation and identity element on these. The identity is of course the reduced word $e$. The operation is defined by concatenating two words and then reducing the result. For example, the product of the words $x_1x_2$ and $x_3x_4$ is $x_1x_2x_3x_4$. Then $e$ can be regarded as the *empty word* under this operation. That this operation is associative follows from the fact that the reduced form of each word is unique regardless of the order of cancellation. The inverse is obtained by taking the inverse of each letter of the given element and then reversing the order. For example, the inverse of the word

$$x_1x_2^{-1}x_3^2$$

is

$$x_3^{-2}x_2x_1^{-1},$$

and one can check that the product of these two is indeed $e$.

Now we have constructed the group $F$, and by identifying the length-one elements consisting of elements of $X$ with the elements of $X$ themselves, we also obtain $\eta_X:X\rightarrow F$. Then it is easy to see that these satisfy the universal property of [Definition 2](#def2). To verify this, one defines $\hat{f}$ as the map sending every element $x\in X$ appearing in $F$ to $f(x)$, and then checks that this is a group homomorphism.

::: Corollary 3
Any group $G$ is a homomorphic image of a free group.
:::
::: Proof
Take the set $X$ of generators of $G$, and consider the free group $F$ on $X$. The function $X\hookrightarrow G$ determines a group homomorphism from $F$ to $G$, and since the image of this homomorphism contains all generators of $G$, it is surjective.
:::

## Free product

Applying the above idea similarly, we can define the free product, which turns out to be the coproduct we have been looking for. Again, we only sketch the construction.

Let a family of groups $(G_i)$ be given. For convenience assume they are pairwise disjoint, and let $X=\coprod G_i$. That is, for any element $x\in X$ there is a unique $i$ such that $x\in G_i$. Since the $G_i$ already contain inverses, it suffices to take $X\cup\{e\}$ as the set of generators.

The *free product* $\prod^\ast G_i$ of $(G_i)$ is the collection of reduced words formed from this set $X\cup\{e\}$. The overall idea is the same as when defining the free group, but since elements of $G_i$ can now be multiplied among themselves, we must be a bit more careful in defining reduced words. By a reduced word used in defining the free product we mean a word

$$x_1x_2\cdots x_n$$

formed from elements of $X\cup\{e\}$ satisfying the following three conditions.

1. If $n>1$, none of the $x_k$ equals $e$.
2. If $x_k\in X$, then $x_k$ is not the identity element in the group $G_i$ containing this element.
3. Any two adjacent elements $x_k, x_{k+1}$ belong to different groups.

Given any word, the method to reduce it to a reduced word is simple. Check whether adjacent elements belong to the same group; if they do, combine them into a single element via the group operation. If during this process (or from the start) an identity element from some group appears, simply delete it.

Then the operation on $\prod^\ast G_i$ is the same *concatenation* as when defining the free group, and it is not difficult to verify that this collection carries a group structure. Moreover, a situation like [Example 1](#ex1) no longer occurs, because even if two nontrivial groups $G_1,G_2$ are abelian, their free product $G_1\ast G_2$ is no longer an abelian group.

::: Example 4
Consider the same situation as in [Example 1](#ex1). For notational convenience, let $G_1=\langle a\rangle\cong\mathbb{Z}$ and $G_2=\langle b\rangle\cong\mathbb{Z}$. Then the elements of $G_1\ast G_2$ are the collection of elements such as

$$ab, a^2b, a^{-1}ba^3, bab^2, \cdots$$

For example, multiplying the two elements $a^2b$ and $bab^2$ we obtain

$$(a^2b)(bab^2)=a^2bbab^2=a^2b^2ab^2.$$

Here $\langle a\rangle$ and $\langle b\rangle$ are cyclic subgroups of $G_1\ast G_2$, so defining homomorphisms from $G_1$ and $G_2$ into $G_1\ast G_2$ by $a\mapsto a$ and $b\mapsto b$ yields the natural inclusion maps $\iota_1$ and $\iota_2$.

Of course, the same problem as in [Example 1](#ex1) does not occur either. We have $\iota_1(a)\iota_2(b)=ab$ and $\iota_2(b)\iota_1(a)=ba$, and these two elements are distinct in $\prod^\ast G_i$.
:::

::: Proposition 5
The free product $\prod^\ast G_i$ is the coproduct in $\Grp$.
:::
::: Proof
Let an arbitrary group $H$ and group homomorphisms $f_i:G_i\rightarrow H$ be given. Then by the universal property of $X=\coprod U(G_i)$, there exists a unique function $f:X\rightarrow U(H)$ such that $U(f_i)=f\circ \iota_i$ for the inclusion maps $\iota_i:U(G_i)\rightarrow X$. Now from the universal property of [Definition 2](#def2) we obtain a group homomorphism $\hat{f}:F(X)\rightarrow H$, and using the fact that the $f_i$ are group homomorphisms one sees that $\hat{f}$ factors through the above reduction process, thereby defining $\prod^\ast G_i\rightarrow H$.
:::

On the other hand, for any group $G$, a group homomorphism $\mathbb{Z}\rightarrow G$ is uniquely determined by which element of $G$ the element $1\in \mathbb{Z}$ is sent to. That is, there is an isomorphism

$$\Hom_\Grp(\mathbb{Z},G)\cong U(G)$$

and by an argument similar to [\[Category Theory\] §Representable Functors, ⁋Example 2](/en/math/category_theory/representable_functors#ex2) one can see that this isomorphism is a representation of $U$. Moreover, thinking of it as

$$\Hom_\Grp(\mathbb{Z},G)\cong \Hom_\Set(\ast, U(G))$$

we can interpret $\mathbb{Z}=F(\ast)$. Hence for any set $X$, using [\[Category Theory\] §Adjoint Functors, ⁋Theorem 9](/en/math/category_theory/adjoints#thm9) we can express the free group $F(X)$ as the free product of copies of $\mathbb{Z}$:

$$F(X)=F\left(\coprod_{x\in X} \{x\}\right)\cong \coprod_{x\in X} F(\ast)={\prod_{x\in X}}^\ast \mathbb{Z}.$$

---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  

---

[^1]: It is not strictly necessary to introduce reduced words in order to define an operation on words, but doing so is convenient for the sake of uniqueness of representation.
