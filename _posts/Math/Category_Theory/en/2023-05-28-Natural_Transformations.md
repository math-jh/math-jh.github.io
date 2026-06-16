---
title: "Natural Transformations"
description: "We define natural transformations as morphisms between functors, and based on this, introduce the functor category and the notion of equivalence of categories."
excerpt: "Natural transformations and equivalence between categories"

categories: [Math / Category Theory]
permalink: /en/math/category_theory/natural_transformations
sidebar: 
    nav: "category_theory-en"

date: 2023-05-28
last_modified_at: 2023-05-28
weight: 3
translated_at: 2026-05-30T12:00:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-30T12:00:04+00:00
---
## Definition of Natural Transformations

We have previously seen that a category of categories exists. Likewise, if we adopt the belief that everything is a category, we can more or less believe that for two categories $$\mathcal{A},\mathcal{B}$$, the category $$\Fun(\mathcal{A},\mathcal{B})$$ of functors from $$\mathcal{A}$$ to $$\mathcal{B}$$ also exists. The question we must answer is then: given two functors $$F,G:\mathcal{A}\rightarrow \mathcal{B}$$, what is a morphism from $$F$$ to $$G$$? This is precisely the natural transformation that we define in this post.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Let two categories $$\mathcal{A},\mathcal{B}$$ be given, and let $$F,G$$ be two functors from $$\mathcal{A}$$ to $$\mathcal{B}$$. If the family of morphisms indexed by $$\obj(\mathcal{A})$$

$$\bigl(\alpha_A:F(A)\rightarrow G(A)\bigr)_{A\in\obj(\mathcal{A})}$$

makes the following diagram commute for each $$A_1,A_2\in\obj(\mathcal{A})$$,

![natural_transformation](/assets/images/Math/Category_Theory/Natural_Transformations-1.svg){:style="width:10.28em" class="invert" .align-center}

then we call $$\alpha=(\alpha_A)_{A\in\obj(\mathcal{A})}$$ a *natural transformation* and denote it by $$\alpha:F\Rightarrow G$$.

If each $$\alpha_A$$ is an isomorphism, then we call this a *natural isomorphism*, and say that the two functors $$F,G$$ are *naturally equivalent*. We denote this by $$F\simeq G$$.

</div>

Based on this, we can define the *functor category* $$\Fun(\mathcal{A},\mathcal{B})$$ from $$\mathcal{A}$$ to $$\mathcal{B}$$. This is the category consisting of functors from $$\mathcal{A}$$ to $$\mathcal{B}$$, whose morphisms are natural transformations between functors. Isomorphisms in this category are given by natural isomorphisms.

## Equivalent Categories

The notion of *equivalence* frequently used between categories is not given by isomorphism in $$\Cat$$. This is because isomorphism between categories is too strong a condition: two categories that appear sufficiently similar may still be regarded as different.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> A functor $$F$$ from $$\mathcal{A}$$ to $$\mathcal{B}$$ is called an *equivalence of categories* if there exists a functor $$G:\mathcal{B}\rightarrow \mathcal{A}$$ such that $$\id_\mathcal{A}\simeq G\circ F$$ and $$\id_\mathcal{B}\simeq F\circ G$$. If an equivalence from $$\mathcal{A}$$ to $$\mathcal{B}$$ exists, then these two categories are said to be *equivalent*, and we write $$\mathcal{A}\simeq\mathcal{B}$$.

</div>

Let us examine in what sense this notion of equivalence between categories gives a sufficiently good notion of being the *same*. For this, we must first define the following.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> A category $$\mathcal{A}$$ is called a *skeletal category* if for any $$A\in\obj(\mathcal{A})$$, the only object of $$\mathcal{A}$$ isomorphic to $$A$$ is $$A$$ itself.

</div>

Let $$\mathcal{A}$$ be a small category. Then we can take the set $$\obj(\mathcal{A})$$, regard isomorphic objects as the same, and pick out only the distinct ones to form a subset $$\mathcal{S}$$ of $$\obj(\mathcal{A})$$. For any $$S_1,S_2\in\mathcal{S}$$, set $$\Hom_\mathcal{S}(S_1,S_2)=\Hom_\mathcal{A}(S_1,S_2)$$. By definition $$\mathcal{S}$$ is a subcategory of $$\mathcal{A}$$, and the inclusion functor $$\mathcal{S}\hookrightarrow\mathcal{A}$$ defined in the obvious way is a faithful functor. If this functor is also full, then we call $$\mathcal{S}$$ a *full subcategory*.

As in the preceding argument, when we construct a subcategory $$\mathcal{S}$$ from a small category $$\mathcal{A}$$, it is natural to question whether $$\mathcal{S}$$ retains enough information to describe $$\mathcal{A}$$. For instance, if a morphism $$f:A_1\rightarrow A_2$$ exists in $$\mathcal{A}$$, but no morphism $$A_1'\rightarrow A_2'$$ exists when we choose objects $$A_1',A_2'$$ isomorphic to $$A_1,A_2$$, then we could say that $$\mathcal{S}$$ has lost information possessed by $$\mathcal{A}$$. However, a moment's thought shows that this can never happen: whenever a morphism $$f:A_1\rightarrow A_2$$ is given, we can compose it with isomorphisms $$A_1'\rightarrow A_1$$ and $$A_2\rightarrow A_2'$$ to produce a morphism $$A_1'\rightarrow A_2'$$.

From this point of view, the category $$\mathcal{S}$$ constructed above can be thought of as essentially containing all the information of $$\mathcal{A}$$. Of course, $$\mathcal{S}$$ itself may differ depending on which object is chosen from each isomorphism class, but it is easy to prove that a category obtained from a different choice is necessarily isomorphic to $$\mathcal{S}$$.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> The *skeleton* of a category $$\mathcal{A}$$ is a full subcategory of $$\mathcal{A}$$ that is a skeletal category. We write this as $$\sk(\mathcal{A})$$.

</div>

The proof of the following theorem is long and tedious, so we do not write it out separately. However, a little thought reveals that no new idea is needed for this proof, and it is even quite obvious. In many cases, one adopts this as the definition of equivalence outright.

<div class="proposition" markdown="1">

<ins id="thm5">**Theorem 5**</ins> A functor $$F:\mathcal{A}\rightarrow\mathcal{B}$$ is an equivalence between categories if and only if $$F$$ is a fully faithful functor and *essentially surjective* in the following sense:

> For each $$B\in\obj(\mathcal{B})$$ there exists a suitable $$A\in\mathcal{A}$$ such that $$F(A)\cong B$$.

</div>

Accepting this, the following corollary is also obvious.

<div class="proposition" markdown="1">

<ins id="cor6">**Corollary 6**</ins> Two small categories $$\mathcal{A}$$ and $$\mathcal{B}$$ are equivalent if and only if their skeletal subcategories $$\sk(\mathcal{A})$$ and $$\sk(\mathcal{B})$$ are isomorphic.

</div>

---

**References**

**[Rie]** Emily Riehl. *Category Theory in Context*. Dover Publications, 2016.

---
