---
title: "Restricted Sum"
excerpt: "Restricted sum of groups"

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/restricted_sums
header:
    overlay_image: /assets/images/Math/Algebraic_Structures/Restricted_Sums.png
    overlay_filter: 0.5
sidebar:
    nav: "algebraic_structures-en"

date: 2026-03-11
last_modified_at: 2026-03-11
weight: 8
translated_at: 2026-05-24T15:30:03+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-24T15:30:03+00:00
---
Previously, we verified in [§Direct Products of Groups](/en/math/algebraic_structures/direct_products) that arbitrary products exist in $$\Grp$$, and in [§Group Homomorphisms, ⁋Proposition 2](/en/math/algebraic_structures/group_homomorphisms#prop2) that every morphism in $$\Grp$$ has an equalizer. Thus, by the argument following [\[Category Theory\] §Limits, ⁋Example 7](/en/math/category_theory/limits#ex7), $$\Grp$$ is a complete category.

On the other hand, every morphism in $$\Grp$$ has a coequalizer. ([§Isomorphism Theorems, ⁋Proposition 8](/en/math/algebraic_structures/isomorphism_theorems#prop8)) Hence, if $$\Grp$$ has arbitrary coproducts, it is cocomplete, and therefore bicomplete.

However, unlike in [§Direct Products of Groups, ⁋Lemma 1](/en/math/algebraic_structures/direct_products#lem1), there is no obvious way to equip the coproduct $$\coprod G_i$$ in $$\Set$$ with a group structure. ([\[Set Theory\], §Sum of Sets, ⁋Proposition 5](/en/math/set_theory/sum_of_sets#prop5))

In this post, we first show that the category of abelian groups has coproducts. In the next post, we will show, by a different approach, that for *arbitrary* groups there exists a group satisfying the universal property of coproducts.

## Restricted Sum

Let $$(G_i)$$ be a family of groups and consider their product. Then each $$G_i$$ can be viewed as a subgroup of $$\prod G_i$$ via $$\iota_i$$. Naturally, we may ask whether the equation

$$\prod_{i\in I} G_i=\left\langle\bigcup \iota_i(G_i)\right\rangle$$

holds. This equation almost never holds when $$I$$ is infinite. As the simplest example, take $$I=\mathbb{N}$$ and $$G_i=\mathbb{Z}/2\mathbb{Z}=\{\bar{0}, \bar{1}\}$$. Then the left-hand side contains the element

$$(\bar{1},\bar{1},\cdots)$$

but the right-hand side only contains elements obtained from *finite* operations among the $$\iota_i(\bar{1})$$, and hence cannot contain the element above.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Let $$(G_i)$$ be a family of groups and fix subgroups $$H_i$$ of $$G_i$$. The subgroup consisting of all $$x$$ such that $$\pr_ix\in H_i$$ for all but finitely many $$i$$ is called the *restricted sum* of the $$G_i$$ with respect to the $$H_i$$, denoted $$\prod^H G_i$$.

In particular, if $$H_i=\{e\}$$ for all $$i$$, it is called the *weak direct product* of the $$G_i$$, denoted simply by

$${\prod_{i\in I}}^w G_i$$

</div>

The notation $$\prod^H$$ is not particularly convenient, but fortunately we are only interested in weak direct products, so we shall not need it again.

By definition,

$$\left\langle\bigcup \iota_i(G_i)\right\rangle={\prod_{i\in I}}^w G_i$$

holds. Moreover, if $$I$$ is finite, the weak direct product coincides with the usual direct product.

Then $$\prod^wG_i$$ satisfies the following universal property.

<div class="proposition" markdown="1">

<ins id="thm2">**Theorem 2**</ins> Let $$(G_i)$$ be a family of groups and let $$\prod^w G_i$$ be their weak direct product. Given another group $$H$$, suppose that group homomorphisms $$f_i:G_i\rightarrow H$$ satisfy the condition

> for any $$i\neq j$$, if $$x\in G_i$$ and $$y\in G_j$$, then $$f_i(x)f_j(y)=f_j(y)f_i(x)$$
 
Then there exists a unique group homomorphism $$f:\prod^w G_i\rightarrow H$$ such that $$f_i=f\circ\iota_i$$ for all $$i$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, we prove uniqueness. If $$f,f':\prod^w G_i\rightarrow H$$ both satisfy the above condition, they agree on $$\bigcup\iota_i(G_i)$$, hence on $$\prod^w G_i$$, and thus $$f=f'$$.

We now show existence. For any $$x\in \prod^w G_i$$, define $$f(x)$$ by

$$f(x)=\prod_{i\in I} f_i(\pr_ix)$$

Here $$\prod$$ denotes the product of elements in the usual multiplicative sense. Since $$x\in\prod^w G_i$$, the factors $$f_i(\pr_ix)$$ are the identity for all but finitely many $$i$$, so this product is well defined.

The identity $$f_i=f\circ\iota_i$$ is immediate, and to verify that $$f$$ is a group homomorphism, observe that for any $$x,y\in\prod^wG_i$$,

$$f(xy)=\prod_{i\in I}f_i(\pr_i(xy))=\prod_{i\in I}f_i(\pr_ix)f_i(\pr_iy)$$

holds; selecting the finitely many indices for which $$\pr_i(xy)\neq e_i$$ and denoting them by $$1,\ldots, n$$, we obtain

$$f_1(\pr_1x)f_1(\pr_1y)f_2(\pr_2x)f_2(\pr_2y)\cdots f_n(\pr_nx)f_n(\pr_ny)$$

and since $$f_i(\pr_ix)$$ and $$f_j(\pr_jy)$$ commute whenever $$i\neq j$$, this can be rewritten as

$$f_1(\pr_1x)f_2(\pr_2x)\cdots f_n(\pr_nx)f_1(\pr_1y)f_2(\pr_2y)\cdots f_n(\pr_ny)$$

Thus $$f(xy)=f(x)f(y)$$, so $$f$$ is a group homomorphism. That $$f_i=f\circ\iota_i$$ is immediate.

</details>

The condition imposed on the $$f_i$$

> for any $$i\neq j$$, if $$x\in G_i$$ and $$y\in G_j$$, then $$f_i(x)f_j(y)=f_j(y)f_i(x)$$

is inevitable, for it is precisely the condition satisfied by the $$\iota_i$$. Consequently, [Theorem 6](#thm6) answers our question only for abelian groups.

Using the universal property of weak direct products, one can establish several properties analogous to those of direct products. For instance, the following holds.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> Given groups $$G_i$$ and normal subgroups $$H_i$$ of $$G_i$$, the weak direct product $$\prod^w H_i$$ is a normal subgroup of $$\prod^w G_i$$, and the quotient group is $$\prod^w (G_i/H_i)$$.

</div>

## Internal Weak Product

Let $$G$$ be a group and let $$(H_i)$$ be a family of subgroups of $$G$$. If elements of $$H_i$$ commute with those of $$H_j$$ whenever $$i\neq j$$, then the inclusion homomorphisms $$\iota_i:H_i\rightarrow G$$ induce a homomorphism $$\iota$$ from $$\prod^w H_i$$ to $$G$$.

We now make the following definition.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> In this situation, if $$\iota$$ is an isomorphism, we say that $$G$$ is the *internal weak direct product* of the $$H_i$$.

</div>

From the explicit description of the homomorphism $$f$$ constructed in [Theorem 2](#thm2), one sees that $$G$$ being the internal weak direct product of the $$H_i$$ is equivalent to the condition

> every $$x\in G$$ can be written as a product $$\prod y_i$$ of a finitely supported family $$(y_i)_{i\in I}$$ with $$y_i\in H_i$$.

If the subgroups $$H_i$$ are all normal in $$G$$, then the following additional condition ensures that $$G$$ is the internal weak direct product of the $$H_i$$.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> Let $$(H_i)$$ be normal subgroups of a group $$G$$ satisfying the following two conditions:

1. $$G=\bigl\langle\bigcup_{i\in I} H_i\bigr\rangle$$,
2. $$H_k\cap \bigl\langle\bigcup_{i\neq k} H_i\bigr\rangle=\{e\}$$

Then $$G$$ is the internal weak direct product of the $$H_i$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, condition 2 implies that $$H_i\cap H_j=\{e\}$$ whenever $$i\neq j$$. Choosing arbitrary $$x_i\in H_i$$ and $$x_j\in H_j$$, from

$$x_ix_jx_i^{-1}x_j^{-1}=x_i\bigl(x_jx_i^{-1}x_j^{-1}\bigr)=\bigl(x_ix_jx_i^{-1}\bigr)x_j^{-1}\in H_i\cap H_j=\{e\}$$

we see that elements of $$H_i$$ commute with those of $$H_j$$. Thus the inclusion homomorphisms $$\iota_i$$ induce a homomorphism $$\iota$$ as in [Theorem 2](#thm2).

To show that $$G$$ is the internal weak direct product of the $$H_i$$, we must show that the induced $$\iota$$ is an isomorphism. By condition 1, any $$a\in G$$ is obtained from the $$H_i$$ by a finite sequence of group operations. Since the $$H_i$$ commute pairwise, $$a$$ can be written as

$$a=\prod_{i\in I} h_i=\prod_{i\in I}\iota_i(h_i),\qquad\text{$\supp(h_i)$ finite and $h_i\in H_i$}$$

Setting $$h=\prod_{i\in I} \iota_i(h_i)\in\prod^w H_i$$, we have

$$a=\prod_{i\in I}\iota_i(h_i)=\iota_i\left(\prod_{i\in I}h_i\right)=\iota_i(h)$$

so $$\iota$$ is surjective.

Now suppose $$\iota(a)=e$$. Then we can write $$a=(a_i)_{i\in I}$$ for a finitely supported family $$(a_i)$$ with each $$a_i\in H_i$$. From the equation

$$\iota(a)=\prod_{i\in I}\iota_i(a_i)=\prod_{i\in I} a_i=e$$
  
if $$\supp(a_i)$$ has at least one element, and if $$i\in\supp(a_i)$$, then

$$a_i^{-1}=\prod_{j\in I\setminus\{i\}}a_j\in H_i\cap \left\langle\bigcup_{j\neq i} H_i\right\rangle=\{e\}$$

contradicting the assumption that $$i\in\supp(a_i)$$. Therefore $$\supp(a_i)$$ is empty and $$a$$ is the identity element.

</details>


---

**References**

**[Hun]** Thomas W. Hungerford, *Algebra*, Graduate texts in mathematics, Springer, 2003.

---
