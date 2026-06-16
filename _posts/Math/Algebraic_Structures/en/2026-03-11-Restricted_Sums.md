---
title: "Restricted Sums"
description: "We define the restricted sum and weak direct product for families of groups, and show that the category of Abelian groups has coproducts given by restricted sums."
excerpt: "Restricted sums of groups"

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/restricted_sums
sidebar: 
    nav: "algebraic_structures-en"

date: 2023-01-09
weight: 8
translated_at: 2026-05-29T18:30:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-29T18:30:04+00:00
---
Previously, we verified in [§Direct Product of Groups](/en/math/algebraic_structures/direct_products) that arbitrary products exist in $$\Grp$$, and in [§Group Homomorphisms, ⁋Proposition 2](/en/math/algebraic_structures/group_homomorphisms#prop2) that every morphism in $$\Grp$$ has an equalizer. Therefore, by the argument following [\[Category Theory\] §Limits, ⁋Example 7](/en/math/category_theory/limits#ex7), $$\Grp$$ is a complete category.

On the other hand, every morphism in $$\Grp$$ has a coequalizer ([§Isomorphism Theorems, ⁋Proposition 8](/en/math/algebraic_structures/isomorphism_theorems#prop8)). Thus, if $$\Grp$$ has arbitrary coproducts, then $$\Grp$$ is a cocomplete category and hence a bicomplete category.

However, as observed in [§Direct Product of Groups, ⁋Lemma 1](/en/math/algebraic_structures/direct_products#lem1), it seems difficult to find an obvious way to impose a group structure on the coproduct $$\coprod G_i$$ in $$\Set$$ ([\[Set Theory\] §Sum of Sets, ⁋Proposition 5](/en/math/set_theory/sum_of_sets#prop5)).

In this post, we first show that the category of abelian groups has coproducts. In the next post, by a method different from the one used here, we show that for *arbitrary* groups there also exists a group satisfying the universal property of coproducts.

## Restricted sum

Let a family of groups $$(G_i)$$ and their product be given. Then each $$G_i$$ can be viewed as a subgroup of $$\prod G_i$$ via $$\iota_i$$. Naturally, one may ask whether the identity

$$\prod_{i\in I} G_i=\left\langle\bigcup \iota_i(G_i)\right\rangle$$

holds. This identity almost never holds when $$I$$ is infinite. As the simplest example, let $$I=\mathbb{N}$$ and $$G_i=\mathbb{Z}/2\mathbb{Z}=\{\bar{0}, \bar{1}\}$$. Then, for instance, the left-hand side contains the element

$$(\bar{1},\bar{1},\cdots)$$

but the right-hand side contains only elements obtained by *finite* operations on the $$\iota_i(\bar{1})$$, so it cannot contain the element above.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Let a family of groups $$(G_i)$$ be given, and fix subgroups $$H_i$$ of the $$G_i$$. Then the subgroup consisting of those $$x$$ such that $$\pr_ix\in H_i$$ for all but finitely many $$i$$ is called the *restricted sum* of the $$G_i$$ with respect to the $$H_i$$, and is denoted by $$\prod^H G_i$$.

In the special case where $$H_i=\{e\}$$ for all $$i$$, it is called the *weak direct product* of the $$G_i$$, and is denoted simply by

$${\prod_{i\in I}}^w G_i$$

</div>

The notation $$\prod^H$$ is not particularly good, but fortunately we are only interested in the weak direct product, so we will not use this notation again.

By definition,

$$\left\langle\bigcup \iota_i(G_i)\right\rangle={\prod_{i\in I}}^w G_i$$

holds. Also, if $$I$$ is finite, then the weak direct product coincides with the ordinary direct product.

Then $$\prod^wG_i$$ has the following universal property.

<div class="proposition" markdown="1">

<ins id="thm2">**Theorem 2**</ins> Let a family of groups $$(G_i)$$ and their weak direct product $$\prod^w G_i$$ be given. For another group $$H$$, suppose group homomorphisms $$f_i:G_i\rightarrow H$$ satisfy the following condition:

> For any $$i\neq j$$, if $$x\in G_i$$ and $$y\in G_j$$, then $$f_i(x)f_j(y)=f_j(y)f_i(x)$$.

Then there exists a unique group homomorphism $$f:\prod^w G_i\rightarrow H$$ such that $$f_i=f\circ\iota_i$$ for every $$i$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

We first show uniqueness. If $$f, f'$$ satisfy the above, they must agree on $$\bigcup\iota_i(G_i)$$, and hence also on $$\prod^w G_i$$; therefore $$f=f'$$.

Now we show existence. For any $$x\in \prod^w G_i$$, define $$f(x)$$ by

$$f(x)=\prod_{i\in I} f_i(\pr_ix)$$

Here $$\prod$$ denotes the product of elements in the usual sense. Since $$x$$ lies in $$\prod^w G_i$$, all but finitely many of the $$f_i(\pr_ix)$$ on the right-hand side are the identity, so this product is well defined.

That $$f_i=f\circ\iota_i$$ holds is obvious. To see that $$f$$ is a group homomorphism, take any $$x,y\in\prod^wG_i$$; then

$$f(xy)=\prod_{i\in I}f_i(\pr_i(xy))=\prod_{i\in I}f_i(\pr_ix)f_i(\pr_iy)$$

holds. Picking the finitely many indices for which $$\pr_i(xy)$$ is not $$e_i$$ and labeling them $$1,\ldots, n$$, we obtain

$$f_1(\pr_1x)f_1(\pr_1y)f_2(\pr_2x)f_2(\pr_2y)\cdots f_n(\pr_nx)f_n(\pr_ny)$$

and since $$f_i(\pr_ix)$$ and $$f_j(\pr_jy)$$ commute whenever $$i\neq j$$, this expression can be rewritten as

$$f_1(\pr_1x)f_2(\pr_2x)\cdots f_n(\pr_nx)f_1(\pr_1y)f_2(\pr_2y)\cdots f_n(\pr_ny)$$

Therefore $$f(xy)=f(x)f(y)$$, and $$f$$ is a group homomorphism. That $$f_i=f\circ\iota_i$$ is obvious.

</details>

The condition imposed on the $$f_i$$,

> For any $$i\neq j$$, if $$x\in G_i$$ and $$y\in G_j$$, then $$f_i(x)f_j(y)=f_j(y)f_i(x)$$

is one that necessarily arises, because these are exactly the conditions satisfied by the $$\iota_i$$. Consequently, [Theorem 2](#thm2) answers our question only for abelian groups.

Using the universal property of the weak direct product, one can establish several properties analogous to those of the direct product. For instance, the following holds.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> Let the $$G_i$$ be groups and let the $$H_i$$ be normal subgroups of the $$G_i$$. Then the $$\prod^w H_i$$ are also normal subgroups of $$\prod^w G_i$$, and the quotient group is $$\prod^w (G_i/H_i)$$.

</div>

## Internal weak product

Let $$G$$ be a group and let $$(H_i)$$ be a family of subgroups of $$G$$. If the elements of $$H_i$$ commute with those of $$H_j$$ whenever $$i\neq j$$, then the inclusion homomorphisms $$\iota_i:H_i\rightarrow G$$ induce a homomorphism $$\iota$$ from $$\prod^w H_i$$ to $$G$$.

Furthermore, we make the following definition.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> In the above situation, if $$\iota$$ is an isomorphism, then $$G$$ is called the *internal weak direct product* of the $$H_i$$.

</div>

Reflecting on the form of the homomorphism $$f$$ constructed in [Theorem 2](#thm2), one can verify that $$G$$ being the internal weak direct product of the $$H_i$$ is equivalent to the following condition:

> Every $$x\in G$$ can be expressed as a product $$\prod y_i$$ of a finitely supported family $$(y_i)_{i\in I}$$ with $$y_i\in H_i$$.

If the subgroups $$H_i$$ are all normal in $$G$$, then $$G$$ becomes the internal weak direct product of the $$H_i$$ provided the following additional conditions are met.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> Let $$(H_i)$$ be normal subgroups of a group $$G$$ satisfying the following two conditions:

1. $$G=\bigl\langle\bigcup_{i\in I} H_i\bigr\rangle$$,
2. $$H_k\cap \bigl\langle\bigcup_{i\neq k} H_i\bigr\rangle=\{e\}$$

Then $$G$$ is the internal weak direct product of the $$H_i$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, condition 2 implies in particular that $$H_i\cap H_j=\{e\}$$ for every pair $$i\neq j$$. Now take arbitrary $$x_i\in H_i$$ and $$x_j\in H_j$$; then

$$x_ix_jx_i^{-1}x_j^{-1}=x_i\bigl(x_jx_i^{-1}x_j^{-1}\bigr)=\bigl(x_ix_jx_i^{-1}\bigr)x_j^{-1}\in H_i\cap H_j=\{e\}$$

shows that the elements of $$H_i$$ and $$H_j$$ commute. Hence the inclusion homomorphisms $$\iota_i$$ induce $$\iota$$ as in [Theorem 2](#thm2).

To show that $$G$$ is the internal weak direct product of the $$H_i$$, we must show that this induced $$\iota$$ is an isomorphism. By condition 1, any $$a\in G$$ is obtained by *finite* operations on $$\bigcup H_i$$. Moreover, since the $$H_i$$ commute with one another, we can write $$a$$ as

$$a=\prod_{i\in I} h_i=\prod_{i\in I}\iota_i(h_i),\qquad\text{$\supp(h_i)$ finite and $h_i\in H_i$}$$

Setting $$h=\prod_{i\in I} \iota_i(h_i)\in\prod^w H_i$$, we have

$$a=\prod_{i\in I}\iota_i(h_i)=\iota\left(\prod_{i\in I}\iota_i(h_i)\right)=\iota(h)$$

so $$\iota$$ is surjective.

Now suppose $$\iota(a)=e$$. Then we can write $$a=(a_i)_{i\in I}$$ for a finitely supported family $$(a_i)$$ with each term in $$H_i$$. From the equation

$$\iota(a)=\prod_{i\in I}\iota_i(a_i)=\prod_{i\in I} a_i=e$$

if $$\supp(a_i)$$ contains at least one element and $$i\in\supp(a_i)$$, then

$$a_i^{-1}=\prod_{j\in I\setminus\{i\}}a_j\in H_i\cap \left\langle\bigcup_{j\neq i} H_i\right\rangle=\{e\}$$

which contradicts the assumption that $$i\in\supp(a_i)$$. Therefore $$\supp(a_i)$$ is empty and $$a$$ is the identity.

</details>


---

**References**

**[Hun]** Thomas W. Hungerford, *Algebra*, Graduate texts in mathematics, Springer, 2003.

---
