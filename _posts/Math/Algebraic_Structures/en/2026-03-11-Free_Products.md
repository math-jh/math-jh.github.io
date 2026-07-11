---
title: "Free Products"
description: "We prove the existence and universal property of free products, then explain their construction using the definition of free groups and adjoint functors."
excerpt: "Free product and universal property"

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/free_products
sidebar: 
    nav: "algebraic_structures-en"

date: 2022-12-07
weight: 9

drift_needed: true
translated_at: 2026-07-10T17:30:02+00:00
translation_source: kimi-cli
---
Unlike in the case of Abelian groups, the weak direct product defined in the previous post does not satisfy a universal property for general groups.

::: Example 1
Consider any nonabelian group $$G$$, and let $$a,b\in G$$ be such that $$ab\neq ba$$. Define group homomorphisms $$f_1, f_2: (\mathbb{Z},+)\rightarrow (G,\cdot)$$ by

$$f_1(1)=a, \qquad f_2(1)=b.$$

Since the index set $$I=\{1,2\}$$ is finite, the weak direct product of two copies of $$(\mathbb{Z},+)$$ equals $$\mathbb{Z}\times\mathbb{Z}$$.

However, we can see that there is no map $$f:\mathbb{Z}\times\mathbb{Z}\rightarrow G$$ making the following diagram commute:

![counterexample](/assets/images/Math/Algebraic_Structures/Free_Products-1.svg){:style="width:11.41em" class="invert" .align-center}

Indeed, if such an $$f$$ existed, we would have

$$\begin{aligned}ab&=f_1(1)f_2(1)=f(\iota_1(1))f(\iota_2(1))=f(\iota_1(1)+\iota_2(1))\\
&=f(\iota_2(1)+\iota_1(1))=f(\iota_2(1))f(\iota_1(1))=f_2(1)f_1(1)\\
&=ba\end{aligned}$$

contradicting our choice of $$a,b$$.
:::

Therefore, just as with direct sums for general groups, we need a new construction to find an object satisfying the universal property. To do this, we first define the free group.

## Free group

Any group $$G$$ can be thought of as a set equipped with a binary operation, an identity element, and inverses. Moreover, any group homomorphism can naturally be viewed as a function between sets. In other words, there is a forgetful functor $$U: \Grp \rightarrow\Set$$. In this section we define the left adjoint $$F:\Set \rightarrow\Grp$$ of $$U$$. By the definition of a left adjoint functor, this is a functor satisfying the natural isomorphism

$$\Hom_\Set(X, U(G))\cong\Hom_\Grp(F(X), G).$$

([\[Category Theory\] §Adjoint Functors, ⁋Definition 1](/en/math/category_theory/adjoints#def1)) That is, the functor $$F$$ gives, for any set $$X$$ and any group $$G$$, a bijection that uniquely assigns to each $$f\in\Hom_\Set(X, U(G))$$ an element of $$\Hom_\Grp(F(X),G)$$. Rewriting this, we obtain the following.

::: Definition 2
For a nonempty set $$X$$, the *free group* $$F(X)$$ defined by $$X$$ is determined as the solution $$(F(X), \eta_X\in\Hom_\Set(X,UF(X)))$$ of the following universal mapping problem.

> For any group $$G$$, if any function $$f:X\rightarrow U(G)$$ is given, then there exists a unique group homomorphism $$\hat{f}:F(X)\rightarrow G$$ satisfying $$U(\hat{f})\circ\eta_X=f$$.
:::

Here $$\eta_X$$ is nothing but the unit of the adjunction $$F\dashv U$$. Of course, to do this we must actually construct $$F(X)$$.

We outline the rough idea. First, consider a set $$X^{-1}$$ that is disjoint from $$X$$ and has the same cardinality. There is no reason for $$X^{-1}$$ to be any special set, but we choose a bijection $$X\rightarrow X^{-1}$$ and denote the image of $$x\in X$$ in $$X^{-1}$$ by $$x^{-1}$$. Also, choose a singleton set disjoint from $$X\cup X^{-1}$$ and let its element be $$e$$.

Then the elements of the group $$F$$ are the collection of *reduced words* defined by the set $$X\cup X^{-1}\cup \{e\}$$. Here a *word* is simply a list of elements of the set $$X\cup X^{-1}\cup \{e\}$$; if the same element appears twice in a row as in $$xx$$, or if $$x^{-1}$$ appears immediately after $$x$$ as in $$xx^{-1}$$, or if $$e$$ lies between two terms as in $$xey$$, then these can be abbreviated as $$x^2$$, $$e$$, and $$xy$$ respectively. However, if for example $$y\neq x^{-1}$$, there is no way to abbreviate $$xyx$$. We call a word abbreviated in this way a *reduced word*.

We can reduce every word to a reduced word.[^1] Let us define the operation and identity element among these. The identity element is of course the reduced word $$e$$. The operation is defined by simply concatenating two words and then reducing the result to a reduced word. For example, the operation of the words $$x_1x_2$$ and $$x_3x_4$$ is given by $$x_1x_2x_3x_4$$. Then $$e$$ can also be viewed as the *empty word* under this operation. This operation is obviously associative. The inverse is obtained by taking the inverse of each term of the given element and then listing them in reverse order. For example, the inverse of the word

$$x_1x_2^{-1}x_3^2$$

is

$$x_3^{-2}x_2x_1^{-1}$$

and indeed one can verify that operating these two yields $$e$$.

Now we have constructed the group $$F$$, and if we identify the length-1 elements consisting of elements of $$X$$ with the elements of $$X$$ themselves, we also obtain $$\iota:X\rightarrow F$$. Then one can easily show that these satisfy the universal property of [Definition 2](#def2). For this, we define $$\bar{f}$$ as the function that replaces every element $$x\in X$$ appearing in $$F$$ with $$g(x)$$, and then verify that this is a group homomorphism.

::: Corollary 3
Any group $$G$$ is a homomorphic image of a free group.
:::
::: Proof
Consider the set of generators $$X$$ of $$G$$, and then consider the free group $$F$$ on $$X$$. The function $$X\hookrightarrow G$$ defines a group homomorphism from $$F$$ to $$G$$, and since the image of this homomorphism contains all the generators of $$G$$, it is surjective.
:::

## Free product

Applying the above idea similarly, we can also define the free product, which turns out to be the coproduct we have been looking for. Again, we only briefly introduce the construction.

Suppose a family of groups $$(G_i)$$ is given. For convenience, assume they are all pairwise disjoint, and let $$X=\coprod G_i$$. That is, for any element $$x\in X$$, we can uniquely find an $$i$$ such that $$x\in G_i$$. Since the $$G_i$$ already contain inverses, it suffices to take $$X\cup\{e\}$$ as the set of generators.

The *free product* $$\prod^\ast G_i$$ of $$(G_i)$$ is the set of reduced words formed from this set $$X\cup\{e\}$$. The overall flow is the same as when defining a free group, but this time the elements of $$G_i$$ can be multiplied among themselves, so we need to be a bit more careful when defining reduced words. By a reduced word used in defining the free product, we mean a word

$$x_1x_2\cdots x_n$$

formed from elements of the set $$X\cup\{e\}$$ satisfying the following three conditions.

1. If $$n>1$$, none of the $$x_k$$ is equal to $$e$$.
2. If $$x_k\in X$$, then $$x_k$$ is not the identity element in the group $$G_i$$ containing this element.
3. Any two adjacent elements $$x_i, x_{i+1}$$ must belong to different groups.

When an arbitrary word is given, the way to make it a reduced word is simple. Check whether adjacent elements belong to the same group, and if they do, combine them into a single element by the operation in that group. If an identity element in some group appears during this process (or from the beginning), simply erase that element.

Then the operation on $$\prod^\ast G_i$$ is the same <em-ko>concatenation</em-ko> operation as when defining a free group, and it is not difficult to verify that this set carries a group structure. Also, a situation like [Example 1](#ex1) no longer occurs, because even if two groups $$G_1, G_2$$ are abelian, their free product $$G_1\ast G_2$$ is no longer an abelian group.

::: Example 4
Consider the same situation as [Example 1](#ex1). Instead, for notational convenience, let $$G_1=\langle a\rangle\cong\mathbb{Z}$$, $$G_2=\langle b\rangle\cong\mathbb{Z}$$. Then the elements of $$G_1\ast G_2$$ are the collection of elements of the form

$$ab, a^2b, a^{-1}ba^3, bab^2, \cdots$$

For example, if we multiply the two elements $$a^2b$$ and $$bab^2$$, we obtain

$$(a^2b)(bab^2)=a^2bbab^2=a^2b^2ab^2$$

Here, $$\langle a\rangle$$ and $$\langle b\rangle$$ are cyclic subgroups of $$G_1\ast G_2$$, so by defining homomorphisms from $$G_1$$ and $$G_2$$ into $$G_1\ast G_2$$ via $$a\mapsto a$$ and $$b\mapsto b$$, we obtain natural inclusion maps $$\iota_1$$ and $$\iota_2$$.

Of course, the same issue as in [Example 1](#ex1) does not occur. We have $$\iota_1(a)\iota_2(b)=ab$$ and $$\iota_2(b)\iota_1(a)=ba$$, and these two elements are distinct elements of $$\prod^\ast G_i$$.
:::

::: Proposition 5
Free product $$\prod^\ast G_i$$ is the coproduct in $$\Grp$$.
:::
::: Proof
Suppose we are given an arbitrary group $$H$$ and group homomorphisms $$f_i:G_i\rightarrow H$$. Then by the universal property of $$X=\coprod U(G_i)$$, there exists a unique function $$f:X\rightarrow U(H)$$ satisfying $$U(f_i)=f\circ \iota_i$$ for the inclusion maps $$\iota_i:U(G_i)\rightarrow X$$. Now from the universal property in [Definition 2](#def2), we obtain a group homomorphism $$\hat{f}:F(X)\rightarrow H$$, and using the fact that the $$f_i$$ were group homomorphisms, we see that $$f$$ factors through the above reduction process, and thus defines a map $$\prod^\ast G_i\rightarrow H$$.
:::

On the other hand, for an arbitrary group $$G$$, a group homomorphism $$\mathbb{Z}\rightarrow G$$ is uniquely determined by where $$1\in \mathbb{Z}$$ is sent in $$G$$. That is, we have the isomorphism

$$\Hom_\Grp(\mathbb{Z},G)\cong U(G)$$

and by an argument similar to [[Category Theory] §Representable Functors](/en/math/category_theory/representable_functors#ex2), we know that this isomorphism is a representation of $$U$$; moreover, thinking of it as

$$\Hom_\Grp(\mathbb{Z},G)\cong \Hom_\Set(\ast, U(G))$$

we can interpret this as saying $$\mathbb{Z}=F(\ast)$$. Therefore, for an arbitrary set $$X$$, using [[Category Theory] §Adjoints, ⁋Theorem 9](/en/math/category_theory/adjoints#thm9), we can express the free group $$F(X)$$ as a free product of copies of $$\mathbb{Z}$$:

$$F(X)=F\left(\coprod_{x\in X} \{x\}\right)\cong \coprod_{x\in X} F(\ast)={\prod_{x\in X}}^\ast \mathbb{Z}$$.

---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  

---

[^1]: It is not strictly necessary to introduce reduced words in order to define the operation between words, but it is convenient to introduce reduced words for the sake of uniqueness of representation.
