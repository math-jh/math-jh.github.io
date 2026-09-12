---
title: "Free Product"
description: "We prove the existence and universal property of the free product, and explain the construction of the free product using the definition of free groups and adjoint functors."
excerpt: "Free product and universal property"

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/free_products
sidebar: 
    nav: "algebraic_structures-en"

date: 2022-12-07
weight: 9
translated_at: 2026-08-16T12:45:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-09-08T03:15:04+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
Unlike in abelian groups, the weak direct product defined in the previous post does not satisfy the universal property for general groups.

::: Example 1
Consider an arbitrary nonabelian group $G$, and let $a,b\in G$ satisfy $ab\neq ba$. Define group homomorphisms $f_1, f_2: (\mathbb{Z},+)\rightarrow (G,\cdot)$ by

$$f_1(1)=a, \qquad f_2(1)=b$$

Since the index set $I=\{1,2\}$ is a finite set, the weak direct product of two copies of $(\mathbb{Z},+)$ is equal to $\mathbb{Z}\times\mathbb{Z}$.

However, we can see that there does not exist $f:\mathbb{Z}\times\mathbb{Z}\rightarrow G$ making the following diagram

{% diagram Math/Algebraic_Structures/Free_Products-1.svg width="11.41em" alt="counterexample" %}

commute. Indeed, if such an $f$ exists, then

$$\begin{aligned}ab&=f_1(1)f_2(1)=f(\iota_1(1))f(\iota_2(1))=f(\iota_1(1)+\iota_2(1))\\
&=f(\iota_2(1)+\iota_1(1))=f(\iota_2(1))f(\iota_1(1))=f_2(1)f_1(1)\\
&=ba\end{aligned}$$

which contradicts the choice of $a,b$.
:::

Therefore, to find an object satisfying the universal property among general groups, just like the direct sum, we must introduce a new method. To this end, we must first define the free group.

## Free group

Any group $G$ can be thought of as adding the notions of a binary operation, an identity element, and inverses onto an appropriate set. Not only that, but any group homomorphism can naturally be viewed as a function between sets. That is, there exists a forgetful functor $U: \Grp \rightarrow\Set$. In this section, we define the left adjoint $F:\Set \rightarrow\Grp$ of $U$. By the definition of a left adjoint functor, this is a functor satisfying the natural isomorphism

$$\Hom_\Set(X, U(G))\cong\Hom_\Grp(F(X), G)$$

([\[Category Theory\] §Adjoint Functors, ⁋Definition 1](/en/math/category_theory/adjoints#def1){: data-relation="required" }). That is, for any set $X$ and any group $G$, the functor $F$ is given by a bijection that uniquely associates to each $f\in\Hom_\Set(X, U(G))$ an element of $\Hom_\Grp(F(X),G)$. Rewriting this, we obtain the following.

::: Definition 2
For a set $X$, the *free group* $F(X)$ defined by $X$ is determined by the solution $(F(X), \eta_X\in\Hom_\Set(X,UF(X)))$ to the following universal mapping problem.

> For any group $G$, if a function $f:X\rightarrow U(G)$ is given, then there exists a unique group homomorphism $\hat{f}:F(X)\rightarrow G$ satisfying $U(\hat{f})\circ\eta_X=f$.
:::

Here, $\eta_X$ is nothing but the unit of the adjunction $F\dashv U$. Of course, for this we must actually construct $F(X)$.

We outline the general flow. First, consider a set $X^{-1}$ disjoint from $X$ and having the same cardinality. There is no reason for $X^{-1}$ to be any special set, but we choose a bijection $X\rightarrow X^{-1}$ and denote the image of $x\in X$ in $X^{-1}$ by $x^{-1}$. Also, choose a singleton set disjoint from $X\cup X^{-1}$ and let the element of this set be $e$.

Then the elements of the group $F$ are the collection of *reduced words* defined by the set $X\cup X^{-1}\cup \{e\}$. Here, a *word* is simply a sequence of elements of the set $X\cup X^{-1}\cup \{e\}$; if the same element is listed twice in succession as in $xx$, or two mutually inverse elements are listed in succession as in $xx^{-1}$ or $x^{-1}x$, or if $e$ is between two terms or at the front or back end of a word as in $xey$, then these can be reduced to $x^2$, $e$, and $xy$, respectively. However, if for example $y\neq x^{-1}$, there is no way to reduce $xyx$. A word reduced in this way is called a *reduced word*.

We can reduce every word to a reduced word.[^1] Let us define the operation and identity element between them. The identity element is of course the reduced word $e$. The operation is simply defined by concatenating two words and then reducing the result to a reduced word. For example, the operation of the words $x_1x_2$ and $x_3x_4$ is given by $x_1x_2x_3x_4$. Then $e$ can also be viewed as the *empty word* under this operation. That this operation is associative follows from the fact that the reduced form of each word is unique regardless of the order of reduction. The inverse is obtained by taking the inverse of each term of the originally given element and then listing them in reverse order. For example, the inverse of the following word

$$x_1x_2^{-1}x_3^2$$

is

$$x_3^{-2}x_2x_1^{-1}$$

and one can verify that actually computing the operation of these two yields $e$.

Now we have constructed the group $F$, and by identifying the elements of length 1 consisting of elements of $X$ with the elements of $X$, we also obtain $\eta_X:X\rightarrow F$. Then one can easily show that these satisfy the universal property of [Definition 2](#def2){: data-relation="required" }. To this end, one defines $\hat{f}$ as the function that replaces all elements $x\in X$ appearing in $F$ with $f(x)$, and then checks that this is a group homomorphism.

::: Corollary 3
Any group $G$ is a homomorphic image of a free group.
:::
::: Proof
Consider the collection $X$ of generators of $G$, and then consider the free group $F$ on $X$. There exists a group homomorphism from $F$ to $G$ defined by the function $X\hookrightarrow G$, and since the image of this homomorphism contains all generators of $G$, it is surjective.
:::

## Free product

Applying the above idea, we can similarly define the free product as well, which becomes the coproduct we have been looking for. Likewise, we introduce the construction only briefly.

Let a family of groups $(G_i)$ be given. For convenience, assume that they are all pairwise disjoint, and let $X=\coprod G_i$. That is, for any element $x\in X$, one can uniquely find $i$ such that $x\in G_i$. Since the $G_i$ already contain inverses, it is sufficient to consider only $X\cup\{e\}$ as the collection of generators.

The *free product* $\prod^\ast  G_i$ of $(G_i)$ is the collection of reduced words formed from this set $X\cup\{e\}$. The general flow is the same as when defining the free group, but this time, since the elements of $G_i$ can be operated with each other, we must be a little more careful when defining reduced words. The term reduced word used when defining the free product means that a word formed from elements of the set $X\cup\{e\}$,

$$x_1x_2\cdots x_n$$

satisfies the following three conditions:

1. If $n>1$, none of the $x_k$ is equal to $e$.
2. If $x_k\in X$, then $x_k$ is not the identity element in the group $G_i$ containing this element.
3. Two adjacent elements $x_k, x_{k+1}$ must belong to different groups.

Given any word, the method to make it into a reduced word is simple. After checking whether adjacent elements belong to the same group, combine elements belonging to the same group into a single element via the operation in that group. If the identity element of some group appears in this process (or was there from the beginning), that element can simply be deleted.

Then the operation on $\prod^\ast G_i$ is, identically to when defining the free group, the *concatenation* operation, and it is not difficult to verify that this collection carries a group structure. Moreover, a situation like [Example 1](#ex1){: data-relation="required" } no longer occurs, because even if two nontrivial groups $G_1,G_2$ are abelian, their free product $G_1\ast G_2$ is no longer an abelian group.

::: Example 4
Consider the same situation as in [Example 1](#ex1){: data-relation="required" }. Instead, for notational convenience, let $G_1=\langle a\rangle\cong\mathbb{Z}$ and $G_2=\langle b\rangle\cong\mathbb{Z}$. Then the elements of $G_1\ast G_2$ are the collection of elements such as

$$ab, a^2b, a^{-1}ba^3, bab^2, \cdots$$

For example, if we operate on the two elements $a^2b$ and $bab^2$, we obtain

$$(a^2b)(bab^2)=a^2bbab^2=a^2b^2ab^2$$

Here, $\langle a\rangle$ and $\langle b\rangle$ are cyclic subgroups of $G_1\ast G_2$, and therefore defining homomorphisms from $G_1$ and $G_2$ to $G_1\ast G_2$ by $a\mapsto a$ and $b\mapsto b$ yields the natural inclusion maps $\iota_1$ and $\iota_2$.

Of course, a problem like [Example 1](#ex1){: data-relation="required" } does not occur either. This is because $\iota_1(a)\iota_2(b)=ab$ and $\iota_2(b)\iota_1(a)=ba$, and these two elements are distinct elements of $\prod^\ast G_i$.
:::

::: Proposition 5
The free product $\prod^\ast G_i$ is the coproduct in $\Grp$.
:::
::: Proof
Let an arbitrary group $H$ and group homomorphisms $f_i:G_i\rightarrow H$ be given. Then by the universal property of $X=\coprod U(G_i)$, there exists a unique function $f:X\rightarrow U(H)$ satisfying $U(f_i)=f\circ \iota_i$ for the inclusion maps $\iota_i:U(G_i)\rightarrow X$. Now from the universal property of [Definition 2](#def2){: data-relation="required" } we obtain a group homomorphism $\hat{f}:F(X)\rightarrow H$, and using the fact that the $f_i$ were group homomorphisms, we know that $\hat{f}$ factors through the above reduction process and therefore defines $\prod^\ast G_i\rightarrow H$.
:::

Meanwhile, for any group $G$, a group homomorphism $\mathbb{Z}\rightarrow G$ is uniquely determined by which element of $G$ the element $1\in \mathbb{Z}$ is sent to. That is, the isomorphism

$$\Hom_\Grp(\mathbb{Z},G)\cong U(G)$$

exists, and by an argument similar to [\[Category Theory\] §Representable Functors, ⁋Example 2](/en/math/category_theory/representable_functors#ex2){: data-relation="weak" } one can see that the above isomorphism is a representation of $U$; furthermore, if we think of it as

$$\Hom_\Grp(\mathbb{Z},G)\cong \Hom_\Set(\ast, U(G))$$

it can be interpreted as $\mathbb{Z}=F(\ast)$. Therefore, for any set $X$, by using [\[Category Theory\] §Adjoint Functors, ⁋Theorem 9](/en/math/category_theory/adjoints#thm9){: data-relation="required" }, we can express the free group $F(X)$ as the free product of copies of $\mathbb{Z}$:

$$F(X)=F\left(\coprod_{x\in X} \{x\}\right)\cong \coprod_{x\in X} F(\ast)={\prod_{x\in X}}^\ast \mathbb{Z}$$

---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  

---

[^1]: It is not strictly necessary to introduce reduced words in order to define an operation on words, but it is preferable to introduce reduced words for the uniqueness of representation.
