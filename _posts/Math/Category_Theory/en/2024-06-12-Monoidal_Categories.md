---
title: "Monoidal Categories"
description: "We review the definition of an algebraic monoid and translate it into the language of category theory, expressing associativity and identity as commutative diagrams to introduce the notions of monoidal categories and monoid objects."
excerpt: "Definition and coherence conditions of monoidal categories"

categories: [Math / Category Theory]
permalink: /en/math/category_theory/monoidal_categories
sidebar: 
    nav: "category_theory-en"

date: 2024-06-12
weight: 6
translated_at: 2026-08-19T16:45:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-08-19T16:45:05+00:00
---
Posts in the category theory category are basically readable with only the posts from the [\[Set Theory\]](/en/set_theory/) category, and although the monoidal category covered in this post could have been written in the same way, the first part of this post specifically brings in posts from the [\[Algebraic Structures\]](/en/algebraic_structures) category to aid understanding.

In this post and the next, we examine monoidal categories and monoid objects defined within them. Roughly speaking, a monoid object is an object in some category that has properties similar to the monoid defined algebraically, and to say that it has properties similar to a monoid, this category must be a monoidal category. Therefore, we first briefly review what a monoid was algebraically, and then think about how this story can be rewritten in the language of categories.

## Monoid

We decided to call an associative unital magma a *monoid*. ([\[Algebraic Structures\] §Semigroups, Monoids, and Groups, ⁋Definition 3](/en/math/algebraic_structures/groups#def3)) Unpacking this, the statement that $M$ is a monoid means the following.

> There exists a binary operation $\mu:M\times M \rightarrow M$ defined on $M$, and an element $e\in M$ of $M$, such that
>
> 1. (Associativity) For any $a,b,c\in M$, $\mu(\mu(a,b),c)=\mu(a,\mu(b, c))$ holds.
> 2. (Unit element) $e\in M$ satisfies $a\cdot e=e\cdot a=a$ for any $a\in M$.

However, each of these conditions can be expressed as a commutative diagram. First, for associativity, it is equivalent to the following diagram commuting.

{% diagram Math/Category_Theory/Monoidal_Categories-1.svg width="13.51em" alt="Associativity" %}

This is obvious because if we pick an arbitrary element $(a,b,c)$ from the set in the upper left, proceeding in the $\llcorner$ direction yields

$$\mu(\mu(a,b),c)=\mu(a\cdot b,c)=(a\cdot b)\cdot c$$

and similarly, proceeding in the $\urcorner$ direction yields

$$\mu(a,\mu(b,c))=\mu(a,b\cdot c)=a\cdot(b\cdot c)$$

and the fact that this diagram commutes means exactly that these two elements of $M$ are equal to each other.

Similarly, for the identity element $e$, using the set $I=\{e\}$ and the inclusion $i:I\hookrightarrow M$, we can write this as the following diagram commuting.

{% diagram Math/Category_Theory/Monoidal_Categories-2.svg width="17.03em" alt="Unit_element" %}

In category theory, it is impossible to pick out elements from an object. Therefore, the definition of a monoid examined at the very beginning is unsuitable for explanation using category theory. However, if everything is represented as a diagram as above, it can be appropriately lifted into the language of category theory. To do this, we must first define what $M\times M$, which we naturally used, is.[^1]

## Monoidal Category

Briefly put, a monoidal category is a category equipped with a monoid operation between objects, that is, an associative operation with an identity element. For example, we will soon see that the $\times$ used when defining a monoid at the very beginning makes $\Set$ a monoidal category.

Before giving the definition, recall that when defining a monoid, $M\times(M\times M)$ and $(M\times M)\times M$ are different sets, and $M$, $I\times M$, and $M\times I$ are also different sets. They are certainly different sets; it is just that there exist natural isomorphisms between them.

::: Definition 1 (Monoidal category)
A *monoidal category* is data $(\mathcal{A},\otimes, I)$. Here $\mathcal{A}$ is a category, $I\in\obj(\mathcal{A})$, and $\otimes:\mathcal{A}\times \mathcal{A}\rightarrow \mathcal{A}$ is a bifunctor. These satisfy the following conditions.

1. There exists a natural isomorphism between the two functors $-\otimes(-\otimes-)$ and $(-\otimes-)\otimes-$ from $\mathcal{A}\times \mathcal{A}\times \mathcal{A}$ to $\mathcal{A}$

    $$\alpha_{A,B,C}:A\otimes(B\otimes C)\rightarrow (A\otimes B)\otimes C$$

    This is called the *associator*.
2. There exist natural isomorphisms between the three functors $I\otimes-$, $-\otimes I$, and $\id_\mathcal{A}$ from $\mathcal{A}$ to $\mathcal{A}$

    $$\lambda_A:I\otimes A\rightarrow A,\qquad \rho_A:A\otimes I\rightarrow A$$

    $\lambda$ and $\rho$ are called the *left unitor* and *right unitor*, respectively.
3. (Coherence condition) The following two diagrams both commute.

- (Associator)
  {% diagram Math/Category_Theory/Monoidal_Categories-3.svg width="33.05em" alt="Pentagon_identity" %}
- (Unitor)
  {% diagram Math/Category_Theory/Monoidal_Categories-4.svg width="21.81em" alt="unitor_diagram" %}

If a symmetric condition on $\otimes$ is additionally imposed on a monoidal category $(\mathcal{A},\otimes,I)$, we call it a *symmetric monoidal category*. This is expressed by a natural isomorphism (*symmetor*) $\gamma_{A,B}:A\otimes B \rightarrow B\otimes A$ and the following additional coherence conditions

- (Associativity coherence)
  {% diagram Math/Category_Theory/Monoidal_Categories-5.svg width="26.70em" alt="associativity_coherence" %}
- (Unit coherence)
  {% diagram Math/Category_Theory/Monoidal_Categories-6.svg width="13.43em" alt="symmetor" %}
- (Inverse law)
  {% diagram Math/Category_Theory/Monoidal_Categories-7.svg width="16.29em" alt="inverse" %}

:::

For a monoidal category $(\mathcal{A},\otimes,I)$ and a natural isomorphism $\gamma_{A,B}:A\otimes B\rightarrow B\otimes A$, if together with the above (Associativity coherence) the hexagon decomposing $\gamma_{A,B\otimes C}$ into $\gamma_{A,B}$ and $\gamma_{A,C}$

$$\gamma_{A,B\otimes C}=\alpha_{B,C,A}\circ(\id_B\otimes\gamma_{A,C})\circ\alpha_{B,A,C}^{-1}\circ(\gamma_{A,B}\otimes\id_C)\circ\alpha_{A,B,C}$$

holds, we call this data a *braided monoidal category*. The two hexagons are generally independent conditions, so one alone does not imply the other, but if the inverse law holds, one implies the other. This is why [Definition 1](#def1) only required one hexagon for a symmetric monoidal category, and therefore a symmetric monoidal category is a braided monoidal category satisfying the inverse law.

The coherence conditions for the associator and unitors are used when proving Mac Lane's coherence theorem. Roughly speaking, this states that given a product $A_1\otimes\cdots\otimes A_n$ of $n$ objects, no matter which order we compute in or (in the case of a symmetric monoidal category) which order we rearrange them in, the results are naturally isomorphic, and this is uniquely expressed as a composition of associators, unitors, and (in the case of a symmetric monoidal category) symmetors. However, in a symmetric monoidal category, uniqueness only holds among compositions inducing the same permutation of the objects. For example, when $A_1=A_2=A$, both $\id_{A\otimes A}$ and $\gamma_{A,A}$ appear as compositions from $A\otimes A$ to itself.

Anyway, thanks to the coherence theorem, we know that the monoidal product does not depend on the order of computation or the order in which they are listed, so we now need to worry less about these natural isomorphisms.

::: Example 2
The following are all examples of monoidal categories.

- Equipping $\Set$ with the usual product ([§Limits, ⁋Example 6](/en/math/category_theory/limits#ex6)) and taking $I$ to be any singleton makes $\Set$ a symmetric monoidal category.
- Equipping $\Grp$ with the usual product and taking $I$ to be the trivial group $\{e\}$ makes $\Grp$ a symmetric monoidal category.
- Giving $\Top$ the product structure as the product topology and taking $I$ to be any singleton makes $\Top$ a symmetric monoidal category.
- For any commutative ring $R$, the category $\lMod{R}$ of $R$-modules is a symmetric monoidal category with respect to the tensor product $\otimes$.
- In particular, when $R=k$, the above example shows that $\Vect_k$ is a symmetric monoidal category, and when $R=\mathbb{Z}$, we see that $\Ab$ is a symmetric monoidal category.
:::

The first two examples of [Example 2](#ex2) can be generalized. Let us first define the following.

::: Definition 3
If every finite family of objects in a category $\mathcal{A}$ always has a categorical product, we call this category a *cartesian category*.
:::

Then in the preceding examples, $\Set$ and $\Grp$ become cartesian categories. Likewise, $\Top$ and $\Man^\infty$ are also all cartesian categories.

::: Proposition 4
Any cartesian category has the structure of a monoidal category.
:::

Although quite a bit needs to be added for the proof of this proposition, essentially it amounts to recalling how $(A\times B)\times C\cong A\times(B\times C)$ and $I\times M\cong M\cong M\times I$ came about, and then repeating the computations. A monoidal category whose monoidal product is given by the product is called a *cartesian monoidal category* in this way.

One of the ways in which a cartesian monoidal category differs from a general monoidal category is that several natural morphisms are well-defined. For example, the diagonal morphism $\Delta_X:X \rightarrow X\times X$ and the augmentation morphism $\epsilon_X:X \rightarrow I$, which are not well-defined in a general monoidal category, are well-defined here. $\epsilon_X$ is naturally defined because $I$ is a terminal object, and $\Delta_X$ is obtained through the following diagram.

{% diagram Math/Category_Theory/Monoidal_Categories-8.svg width="12.46em" alt="diagonal_morphism" %}

This will be used when dealing with group objects in the next post.

---

**References**

**[nLab]** nLab. *Monoidal category*. ([Link](https://ncatlab.org/nlab/show/monoidal+category))  
**[Rie]** Emily Riehl. *Category Theory in Context*. Dover Publications, 2016.

---

[^1]: Although the product of two objects inside a category itself was defined as a limit in [§Limits, ⁋Example 6](/en/math/category_theory/limits#ex6), the $\otimes$ of a monoidal category defined below need not be such a categorical product.
