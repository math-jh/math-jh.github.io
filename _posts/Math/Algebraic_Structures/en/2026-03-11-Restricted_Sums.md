---
title: "Restricted Sums"
description: "We define the restricted sum and weak direct product of a family of groups, and show that the category of abelian groups has coproducts via restricted sums."
excerpt: "Restricted sums of groups"

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/restricted_sums
sidebar: 
    nav: "algebraic_structures-en"

date: 2023-01-09
weight: 8
translated_at: 2026-06-24T00:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-24T00:30:02+00:00
---
Previously, we verified in [§Direct Products of Groups](/en/math/algebraic_structures/direct_products) that arbitrary products exist in $$\Grp$$, and in [§Group Homomorphisms](/en/math/algebraic_structures/group_homomorphisms) that every morphism in $$\Grp$$ has an equalizer. Thus, by the argument following [[Category Theory] §Limits, ⁋Example 7](/en/math/category_theory/limits#ex7), $$\Grp$$ is a complete category.

On the other hand, every morphism in $$\Grp$$ has a coequalizer ([§Isomorphism Theorems, ⁋Proposition 8](/en/math/algebraic_structures/isomorphism_theorems#prop8)). Therefore, if $$\Grp$$ has arbitrary coproducts, it is a cocomplete category, and hence a bicomplete category.

However, as in [§Direct Products of Groups, ⁋Lemma 1](/en/math/algebraic_structures/direct_products#lem1), it is not at all obvious how to put a group structure on the coproduct $$\coprod G_i$$ in $$\Set$$ ([[Set Theory] §Sum of Sets, ⁋Proposition 5](/en/math/set_theory/sum_of_sets#prop5)).

In this post, we first show that the category of abelian groups has coproducts. In the next post, by a different method, we show that a group satisfying the universal property of the coproduct exists for <em>arbitrary</em> groups as well.

## Restricted sum

Let $$(G_i)$$ be a family of groups, and suppose their product is given. Then each $$G_i$$ can be viewed as a subgroup of $$\prod G_i$$ via $$\iota_i$$. Naturally, one may ask whether the equality

$$\prod_{i\in I} G_i=\left\langle\bigcup \iota_i(G_i)\right\rangle$$

holds. This equality almost never holds when $$I$$ is infinite. The simplest example is to take $$I=\mathbb{N}$$ and $$G_i=\mathbb{Z}/2\mathbb{Z}=\{\bar{0}, \bar{1}\}$$. Then, for instance, the left-hand side contains the element

$$(\bar{1},\bar{1},\cdots)$$

but the right-hand side contains only elements obtained by *finite* operations on the $$\iota_i(\bar{1})$$, so it cannot contain the element above.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Let a family of groups $$(G_i)$$ be given, and fix subgroups $$H_i$$ of the $$G_i$$. Then the subgroup consisting of those $$x$$ such that $$\pr_ix\in H_i$$ for all but finitely many $$i$$ is called the *restricted sum* of the $$G_i$$ with respect to the $$H_i$$, and is denoted $$\prod^H G_i$$.

In the special case where $$H_i=\{e\}$$ for all $$i$$, it is called the *weak direct product* of the $$G_i$$, and is simply denoted

$${\prod_{i\in I}}^w G_i.$$

</div>

The notation $$\prod^H$$ is not particularly good, but fortunately we are only interested in the weak direct product, so we will never use this notation again.

By definition,

$$\left\langle\bigcup \iota_i(G_i)\right\rangle={\prod_{i\in I}}^w G_i$$

holds. Also, if $$I$$ is a finite set, the weak direct product coincides with the ordinary direct product.

Then $$\prod^wG_i$$ has the following universal property.

<div class="proposition" markdown="1">

<ins id="thm2">**Theorem 2**</ins> Let a family of groups $$(G_i)$$ and their weak direct product $$\prod^w G_i$$ be given. For another group $$H$$, suppose that group homomorphisms $$f_i:G_i\rightarrow H$$ satisfy the condition

> For any $$i\neq j$$, if $$x\in G_i$$ and $$y\in G_j$$, then $$f_i(x)f_j(y)=f_j(y)f_i(x)$$.

Then there exists a unique group homomorphism $$f:\prod^w G_i\rightarrow H$$ such that $$f_i=f\circ\iota_i$$ holds for every $$i$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, we show uniqueness. If $$f, f'$$ satisfy the above, then they must agree on $$\bigcup\iota_i(G_i)$$, hence also on $$\prod^w G_i$$, and therefore $$f=f'$$.

Now we show the existence of $$f$$. For any $$x\in \prod^w G_i$$, define $$f(x)$$ by the formula

$$f(x)=\prod_{i\in I} f_i(\pr_ix).$$

Here $$\prod$$ denotes the ordinary product of elements. Since $$x$$ is an element of $$\prod^w G_i$$, all but finitely many of the $$f_i(\pr_ix)$$ on the right-hand side are the identity, so this product is well-defined.

That the equation $$f_i=f\circ\iota_i$$ holds is obvious, and that $$f$$ is a group homomorphism follows because for any $$x,y\in\prod^wG_i$$,

$$f(xy)=\prod_{i\in I}f_i(\pr_i(xy))=\prod_{i\in I}f_i(\pr_ix)f_i(\pr_iy)$$

holds, so choosing only the finitely many indices for which $$\pr_i(xy)$$ is not $$e_i$$ and calling them $$1,\ldots, n$$, we obtain

$$f_1(\pr_1x)f_1(\pr_1y)f_2(\pr_2x)f_2(\pr_2y)\cdots f_n(\pr_nx)f_n(\pr_ny)$$

and since $$f_i(\pr_ix)$$ and $$f_j(\pr_jy)$$ always commute when $$i\neq j$$, this expression can be rewritten as

$$f_1(\pr_1x)f_2(\pr_2x)\cdots f_n(\pr_nx)f_1(\pr_1y)f_2(\pr_2y)\cdots f_n(\pr_ny).$$

Thus $$f(xy)=f(x)f(y)$$ and $$f$$ is a group homomorphism. That $$f_i=f\circ\iota_i$$ is obvious.

</details>

The condition imposed on the $$f_i$$,

> For any $$i\neq j$$, if $$x\in G_i$$ and $$y\in G_j$$, then $$f_i(x)f_j(y)=f_j(y)f_i(x)$$

is necessarily satisfied, because these are exactly the conditions satisfied by the $$\iota_i$$. Consequently, [Theorem 2](#thm2) answers our question only for abelian groups.

Using the universal property of the weak direct product, one can prove several properties analogous to those for the direct product. For example, the following holds.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> Let the $$G_i$$ be groups and the $$H_i$$ be normal subgroups of the $$G_i$$. Then $$\prod^w H_i$$ is also a normal subgroup of $$\prod^w G_i$$, and its quotient group is $$\prod^w (G_i/H_i)$$.

</div>

## Internal weak product

Let $$G$$ be a group, and let $$(H_i)$$ be a family of subgroups of $$G$$. If the elements of $$H_i$$ commute with the elements of $$H_j$$ whenever $$i\neq j$$, then the inclusion homomorphisms $$\iota_i:H_i\rightarrow G$$ induce a homomorphism $$\iota$$ from $$\prod^w H_i$$ to $$G$$.

We also make the following definition.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> In the above situation, if $$\iota$$ is an isomorphism, then $$G$$ is called the *internal weak direct product* of the $$H_i$$.

</div>

Thinking about the form of the homomorphism $$f$$ constructed in [Theorem 2](#thm2), one can verify that $$G$$ being the internal weak direct product of the $$H_i$$ is equivalent to the condition

> Every $$x\in G$$ can be represented as a product $$\prod y_i$$ of finitely supported families $$(y_i)_{i\in I}$$ with $$y_i\in H_i$$.

If the subgroups $$H_i$$ are all normal in $$G$$, then the following additional condition guarantees that $$G$$ is the internal weak direct product of the $$H_i$$.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> Let $$(H_i)$$ be normal subgroups of a group $$G$$ satisfying the two conditions

1. $$G=\bigl\langle\bigcup_{i\in I} H_i\bigr\rangle$$,
2. $$H_k\cap \bigl\langle\bigcup_{i\neq k} H_i\bigr\rangle=\{e\}$$

Then $$G$$ is the internal weak direct product of the $$H_i$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, condition 2 shows in particular that $$H_i\cap H_j=\{e\}$$ for every pair $$i\neq j$$. Now choose arbitrary $$x_i\in H_i, x_j\in H_j$$; then from

$$x_ix_jx_i^{-1}x_j^{-1}=x_i\bigl(x_jx_i^{-1}x_j^{-1}\bigr)=\bigl(x_ix_jx_i^{-1}\bigr)x_j^{-1}\in H_i\cap H_j=\{e\}$$

we know that the elements of $$H_i$$ and $$H_j$$ commute. Thus the inclusion homomorphisms $$\iota_i$$ induce $$\iota$$ as in [Theorem 2](#thm2).

To show that $$G$$ is the internal weak direct product of the $$H_i$$, we must show that this induced $$\iota$$ is an isomorphism. First, by condition 1, every $$a\in G$$ is obtained by *finite* operations on the $$\bigcup H_i$$. Also, since the $$H_i$$ commute with each other, we can write $$a$$ as

$$a=\prod_{i\in I} h_i=\prod_{i\in I}\iota_i(h_i),\qquad\text{$\supp(h_i)$ finite and $h_i\in H_i$}.$$

Letting $$h=\prod_{i\in I} \iota_i(h_i)\in\prod^w H_i$$, we have

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
