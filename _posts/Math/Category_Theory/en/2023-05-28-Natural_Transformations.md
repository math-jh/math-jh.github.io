---
title: "Natural Transformations"
description: "We define natural transformations as morphisms between functors, and based on this, introduce functor categories and the notion of equivalence of categories."
excerpt: "Natural transformations and equivalence between categories"

categories: [Math / Category Theory]
permalink: /en/math/category_theory/natural_transformations
sidebar: 
    nav: "category_theory-en"

date: 2023-05-28
weight: 3
translated_at: 2026-08-19T14:15:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-02T11:15:05+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
## Definition of Natural Transformations

We have seen earlier that a category of categories exists. If we likewise hold the belief that everything is a category, we can also believe, to some extent, that given two categories $\mathcal{A},\mathcal{B}$, there exists a category $\Fun(\mathcal{A},\mathcal{B})$ of functors from $\mathcal{A}$ to $\mathcal{B}$. The question we must answer is: given two functors $F,G:\mathcal{A}\rightarrow \mathcal{B}$, what is a morphism from $F$ to $G$? That is precisely the natural transformation we define in this post.

::: Definition 1
Suppose two categories $\mathcal{A},\mathcal{B}$ are given, and let $F,G$ be two functors from $\mathcal{A}$ to $\mathcal{B}$. If a family of morphisms indexed by $\obj(\mathcal{A})$

$$\bigl(\alpha_A:F(A)\rightarrow G(A)\bigr)_{A\in\obj(\mathcal{A})}$$

makes the following diagram commute for each $A_1,A_2\in\obj(\mathcal{A})$ and every $f\in\Hom_\mathcal{A}(A_1,A_2)$

{% diagram Math/Category_Theory/Natural_Transformations-1.svg width="10.28em" alt="natural_transformation" %}

then we call $\alpha=(\alpha_A)_{A\in\obj(\mathcal{A})}$ a *natural transformation* and denote it by $\alpha:F\Rightarrow G$.

If each $\alpha_A$ is an isomorphism, we call this a *natural isomorphism*, and we say that the two functors $F,G$ are *naturally equivalent*. We write this as $F\simeq G$.
:::

Based on this, we can define the *functor category* $\Fun(\mathcal{A},\mathcal{B})$ from category $\mathcal{A}$ to $\mathcal{B}$. This is the category consisting of functors from $\mathcal{A}$ to $\mathcal{B}$, whose morphisms are natural transformations between functors. Composition is given componentwise by $(\beta\circ\alpha)_A=\beta_A\circ\alpha_A$, and the identity morphism of a functor $F$ is given by $(\id_F)_A=\id_{F(A)}$. The isomorphisms in this category are given by natural isomorphisms.

## Equivalent Categories

The notion of being *equivalent*, frequently used between categories, is not given by isomorphism in $\Cat$. ([§Functor, ⁋Definition 9](/en/math/category_theory/functors#def9){: data-lid="234ka" }) This is because isomorphism between categories is too strong a condition, so that even two categories that appear sufficiently similar are treated as different.

::: Definition 2
A functor $F$ from a category $\mathcal{A}$ to $\mathcal{B}$ is called an *equivalence of categories* if there exists a functor $G:\mathcal{B}\rightarrow \mathcal{A}$ such that $\id_\mathcal{A}\simeq G\circ F$ and $\id_\mathcal{B}\simeq F\circ G$. If there exists an equivalence from $\mathcal{A}$ to $\mathcal{B}$, we say that these two categories are *equivalent* and write $\mathcal{A}\simeq\mathcal{B}$.
:::

Let us examine in what sense this notion of equivalence between categories gives a sufficiently good notion of *sameness*. For this, we must first define the following.

::: Definition 3
A category $\mathcal{A}$ is a *skeletal category* if, for any $A\in\obj(\mathcal{A})$, the only object isomorphic to $A$ in $\mathcal{A}$ is itself.
:::

Let $\mathcal{A}$ be a small category. Then, after viewing mutually isomorphic objects in the set $\obj(\mathcal{A})$ as the same, we can pick out only distinct ones to form a subset of $\obj(\mathcal{A})$, namely $\mathcal{S}$. For any $S_1,S_2\in\mathcal{S}$, set $\Hom_\mathcal{S}(S_1,S_2)=\Hom_\mathcal{A}(S_1,S_2)$. By definition, $\mathcal{S}$ is a subcategory of $\mathcal{A}$, and the trivially defined inclusion functor $\mathcal{S}\hookrightarrow\mathcal{A}$ is a faithful functor. ([§Category, ⁋Definition 5](/en/math/category_theory/categories#def5){: data-lid="iz7hy" }) If this functor is also full, we call $\mathcal{S}$ a *full subcategory*. ([§Functor, ⁋Definition 10](/en/math/category_theory/functors#def10){: data-lid="ark4w" })

When constructing from a small category $\mathcal{A}$ a subcategory $\mathcal{S}$ as in the preceding argument, it is a natural question whether $\mathcal{S}$ has enough information to describe $\mathcal{A}$. For instance, if in $\mathcal{A}$ a morphism $f:A_1\rightarrow A_2$ exists, but when choosing objects isomorphic to $A_1,A_2$, say $A_1',A_2'$, no morphism $A_1'\rightarrow A_2'$ exists, then one could say that $\mathcal{S}$ has lost the information that $\mathcal{A}$ holds. However, a moment's thought shows that this never happens. This is because whenever a morphism $f:A_1\rightarrow A_2$ is given, we can compose the isomorphisms $A_1'\rightarrow A_1$, $A_2\rightarrow A_2'$ and $f$ to produce $A_1'\rightarrow A_2'$.

From this perspective, the category $\mathcal{S}$ constructed above can be thought of as essentially containing all the information of $\mathcal{A}$. Of course, $\mathcal{S}$ itself will vary depending on which of the isomorphic objects we choose, but it is easy to prove that a category obtained from a different choice is also necessarily isomorphic to $\mathcal{S}$.

::: Definition 4
A *skeleton* of a category $\mathcal{A}$ is a full subcategory of $\mathcal{A}$ that is a skeletal category such that every $A\in\obj(\mathcal{A})$ is isomorphic to some object of that subcategory. We denote this by $\sk(\mathcal{A})$.
:::

The proof of the following theorem is long and tedious, so we do not write it down separately. However, a moment's thought shows that no special idea is needed for this proof, and it is even quite obvious. In many cases, one takes this itself as the definition of an equivalence.

::: Theorem 5
A functor $F:\mathcal{A}\rightarrow\mathcal{B}$ is an equivalence between categories if and only if $F$ is a fully faithful functor and is *essentially surjective* in the following sense.

> For every $B\in\obj(\mathcal{B})$, there exists some $A\in\obj(\mathcal{A})$ such that $F(A)\cong B$.
:::

Considering a skeleton of $\mathcal{A}$, the inclusion functor $\sk(\mathcal{A})\hookrightarrow\mathcal{A}$ is fully faithful because it is the inclusion of a full subcategory, and the last condition of [Definition 4](#def4){: data-lid="a37tm" } is precisely that this functor is essentially surjective. Therefore, by [Theorem 5](#thm5){: data-lid="mrj0j" }, this inclusion is an equivalence, and $\mathcal{A}\simeq\sk(\mathcal{A})$ holds. From this we obtain the following.

::: Corollary 6
Two small categories $\mathcal{A}$ and $\mathcal{B}$ are equivalent if and only if their skeletal subcategories $\sk(\mathcal{A})$ and $\sk(\mathcal{B})$ are isomorphic.
:::

---

**References**

**[Rie]** Emily Riehl. *Category Theory in Context*. Dover Publications, 2016.

---
