---
title: "Free Products"
excerpt: "Free product and universal property"

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/free_products
sidebar:
    nav: "algebraic_structures-en"

date: 2026-03-11
last_modified_at: 2026-03-11
weight: 9
translated_at: 2026-05-29T02:00:58+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-24T14:30:03+00:00
---
Unlike in the category of abelian groups, the weak direct product defined in the previous post does not satisfy the universal property for general groups.

<div class="example" markdown="1">

<ins id="ex1">**Example 1**</ins> Consider an arbitrary nonabelian group $$G$$, and let $$a,b\in G$$ satisfy $$ab\neq ba$$. Define group homomorphisms $$f_1, f_2: (\mathbb{Z},+)\rightarrow (G,\cdot)$$ by

$$f_1(1)=a, \qquad f_2(1)=b$$

Since the index set $$I=\{1,2\}$$ is finite, the weak direct product of two copies of $$(\mathbb{Z},+)$$ is $$\mathbb{Z}\times\mathbb{Z}$$.

However, we can see that there is no $$f:\mathbb{Z}\times\mathbb{Z}\rightarrow G$$ making the following diagram

![counterexample](/assets/images/Math/Algebraic_Structures/Free_Products-1.svg){:style="width:11.41em" class="invert" .align-center}

commute. If such an $$f$$ existed, then

$$\begin{aligned}ab&=f_1(1)f_2(1)=f(\iota_1(1))f(\iota_2(1))=f(\iota_1(1)+\iota_2(1))\\
&=f(\iota_2(1)+\iota_1(1))=f(\iota_2(1))f(\iota_1(1))=f_2(1)f_1(1)\\
&=ba\end{aligned}$$

contradicting the choice of $$a,b$$.

</div>

Therefore, to find an object satisfying the universal property for general groups, just as direct sums do, we must introduce a new construction. For this we first define free groups.

## Free Group

Any group $$G$$ may be viewed as a set equipped with a binary operation, an identity element, and inverses. Moreover, any group homomorphism can naturally be regarded as a function between sets. That is, there is a forgetful functor $$U: \Grp \rightarrow\Set$$. In this section we define the left adjoint $$F:\Set \rightarrow\Grp$$ of $$U$$. By the definition of a left adjoint functor, it is a functor satisfying the natural isomorphism

$$\Hom_\Set(X, U(G))\cong\Hom_\Grp(F(X), G)$$

([\[Category Theory\] §Adjoint Functors, ⁋Definition 1](/en/math/category_theory/adjoints#def1)). In other words, for any set $$X$$ and any group $$G$$, the functor $$F$$ is given by a bijection assigning to each $$f\in\Hom_\Set(X, U(G))$$ a unique element of $$\Hom_\Grp(F(X),G)$$. This may be rewritten as follows.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> For a nonempty set $$X$$, the *free group* $$F(X)$$ on $$X$$ is defined as the solution $$(F(X), \eta_X\in\Hom_\Set(X,UF(X)))$$ to the following universal mapping problem.

> For any group $$G$$, given any function $$f:X\rightarrow U(G)$$, there exists a unique group homomorphism $$\hat{f}:F(X)\rightarrow G$$ satisfying $$U(\hat{f})\circ\eta_X=f$$.

</div>

Here $$\eta_X$$ is merely the unit of the adjunction $$F\dashv U$$. Of course, to this end we must actually construct $$F(X)$$.

We outline the general approach. First, consider a set $$X^{-1}$$ disjoint from $$X$$ and having the same cardinality. There is nothing special about the set $$X^{-1}$$ itself; we simply choose a bijection $$X\rightarrow X^{-1}$$ and denote the image of $$x\in X$$ in $$X^{-1}$$ by $$x^{-1}$$. Also, choose a singleton set disjoint from $$X\cup X^{-1}$$ and denote its element by $$e$$.

Then the elements of the group $$F$$ are the reduced words on the set $$X\cup X^{-1}\cup \{e\}$$. Here a *word* is simply a sequence of elements from $$X\cup X^{-1}\cup \{e\}$$; if the same element appears twice in succession, as in $$xx$$, or if $$x^{-1}$$ follows immediately after $$x$$, as in $$xx^{-1}$$, or if $$e$$ lies between two symbols, as in $$xey$$, then these may be shortened to $$x^2$$, $$e$$, and $$xy$$, respectively. For instance, if $$y\neq x^{-1}$$, there is no way to reduce $$xyx$$. A word that has been shortened in this manner is called a *reduced word*.

We can reduce every word to a reduced word.[^1] Let us define an operation and an identity element on these. The identity element is of course the reduced word $$e$$. The operation is defined by concatenating two words and then reducing the result to a reduced word. For example, the product of the words $$x_1x_2$$ and $$x_3x_4$$ is $$x_1x_2x_3x_4$$. Thus $$e$$ may also be regarded as the *empty word* under this operation. This operation is obviously associative. The inverse of a word is obtained by taking the inverse of each term in the original word and reversing their order. For example, the inverse of the word

$$x_1x_2^{-1}x_3^2$$

is

$$x_3^{-2}x_2x_1^{-1}$$;

indeed, their product is $$e$$.

Now we have constructed the group $$F$$. By identifying each element of $$X$$ with the corresponding word of length 1, we obtain $$\iota:X\rightarrow F$$. Then it is easy to verify that these satisfy the universal property of [Definition 2](#def2). For this, it suffices to define $$\bar{f}$$ as the map sending each $$x\in X$$ (regarded as an element of $$F$$) to $$g(x)$$, and to check that this defines a group homomorphism.

<div class="proposition" markdown="1">

<ins id="cor3">**Corollary 3**</ins> Any group $$G$$ is a homomorphic image of a free group.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Take a set $$X$$ of generators of $$G$$, and let $$F$$ be the free group on $$X$$. The inclusion $$X\hookrightarrow G$$ induces a group homomorphism $$F\rightarrow G$$, and since its image contains all generators of $$G$$, it is surjective.

</details>

## Free Product

Applying the above idea, we can define the free product in a similar manner; this is precisely the coproduct we have been seeking. As before, we give only a brief sketch of the construction.

Let $$(G_i)$$ be a family of groups. For convenience, assume that they are pairwise disjoint, and set $$X=\coprod G_i$$. Thus each element $$x\in X$$ belongs to a unique $$G_i$$. Since the $$G_i$$ already contain inverses, it suffices to take $$X\cup\{e\}$$ as the set of generators.

The *free product* $$\prod^\ast  G_i$$ of $$(G_i)$$ is the set of reduced words constructed from this set $$X\cup\{e\}$$. The overall idea is the same as for free groups, but since elements from the same $$G_i$$ can be multiplied together, we must take a little more care in defining reduced words. By a reduced word in the free product, we mean a word

$$x_1x_2\cdots x_n$$

formed from elements of $$X\cup\{e\}$$ satisfying the following three conditions.

1. If $$n>1$$, none of the $$x_k$$ equals $$e$$.
2. If $$x_k\in X$$, then $$x_k$$ is not the identity element of the group $$G_i$$ to which it belongs.
3. Two adjacent elements $$x_i, x_{i+1}$$ must belong to different groups.

Given any word, the reduction procedure is simple. Check whether adjacent elements belong to the same group, and merge consecutive elements from the same group into a single element using the group operation. If an identity element arises during this process (or was present from the start), simply delete it.

Then the operation on $$\prod^\ast G_i$$ is, as with free groups, the *concatenation* operation, and one easily verifies that this set forms a group. Moreover, a situation like that of [Example 1](#ex1) no longer arises, because even if two groups $$G_1,G_2$$ are abelian, their free product $$G_1\ast G_2$$ is not an abelian group.

<div class="example" markdown="1">

<ins id="ex4">**Example 4**</ins> Consider the same situation as in [Example 1](#ex1). For notational convenience, let $$G_1=\langle a\rangle\cong\mathbb{Z}$$ and $$G_2=\langle b\rangle\cong\mathbb{Z}$$. Then the elements of $$G_1\ast G_2$$ are words such as

$$ab, a^2b, a^{-1}ba^3, bab^2, \cdots$$

For example, multiplying the two elements $$a^2b$$ and $$bab^2$$ yields

$$(a^2b)(bab^2)=a^2bbab^2=a^2b^2ab^2$$

Here $$\langle a\rangle$$ and $$\langle b\rangle$$ are cyclic subgroups of $$G_1\ast G_2$$. Defining homomorphisms $$G_1\rightarrow G_1\ast G_2$$ and $$G_2\rightarrow G_1\ast G_2$$ by $$a\mapsto a$$ and $$b\mapsto b$$, we obtain the natural inclusion maps $$\iota_1$$ and $$\iota_2$$.

Of course, the problem of [Example 1](#ex1) does not arise here either: $$\iota_1(a)\iota_2(b)=ab$$ and $$\iota_2(b)\iota_1(a)=ba$$, but these are distinct elements of $$\prod^\ast G_i$$.

</div>

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> The free product $$\prod^\ast G_i$$ is the coproduct in $$\Grp$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$H$$ be an arbitrary group, and let $$f_i:G_i\rightarrow H$$ be group homomorphisms. By the universal property of the disjoint union $$X=\coprod U(G_i)$$, there exists a unique function $$f:X\rightarrow U(H)$$ such that $$U(f_i)=f\circ \iota_i$$ for the inclusion maps $$\iota_i:U(G_i)\rightarrow X$$. Now from the universal property of the free product ([Definition 2](#def2)), we obtain a group homomorphism $$\hat{f}:F(X)\rightarrow H$$. Using the fact that the $$f_i$$ are group homomorphisms, we see that $$f$$ factors through the reduction process described above, thereby defining a homomorphism $$\prod^\ast G_i\rightarrow H$$.

</details>

On the other hand, for any group $$G$$, a group homomorphism $$\mathbb{Z}\rightarrow G$$ is uniquely determined by the image of $$1\in \mathbb{Z}$$. That is, there is an isomorphism

$$\Hom_\Grp(\mathbb{Z},G)\cong U(G)$$

and by an argument similar to [\[Category Theory\] §Representable Functors](/en/math/category_theory/representable_functors#ex2), we see that this isomorphism gives a representation of $$U$$. Moreover, viewing it as

$$\Hom_\Grp(\mathbb{Z},G)\cong \Hom_\Set(\ast, U(G))$$

we may interpret $$\mathbb{Z}$$ as $$F(\ast)$$. Therefore, for any set $$X$$, applying [\[Category Theory\] §Adjoint Functors, ⁋Theorem 9](/en/math/category_theory/adjoints#thm9), we may write the free group $$F(X)$$ as the free product of copies of $$\mathbb{Z}$$:

$$F(X)=F\left(\coprod_{x\in X} \{x\}\right)\cong \coprod_{x\in X} F(\ast)={\prod_{x\in X}}^\ast \mathbb{Z}$$

---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.

---

[^1]: While reduced words are not strictly necessary to define the operation on words, it is preferable to introduce them for uniqueness of representation.
