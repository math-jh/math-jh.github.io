---

title: "Restricted Sums"
excerpt: "Restricted sum of groups"

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/restricted_sums
header:
    overlay_image: /assets/images/Math/Algebraic_Structures/Restricted_sums.png
    overlay_filter: 0.5
sidebar:
    nav: "algebraic_structures-en"

date: 2026-03-11
last_modified_at: 2026-03-11
weight: 8

---

Previously, we verified in [§Direct Products of Groups](/en/math/algebraic_structures/direct_products) that any product exists in $$\Grp$$, and in [§Group Homomorphisms, ⁋Proposition 2](/en/math/algebraic_structures/group_homomorphisms#prop2) that any morphism in $$\Grp$$ has an equalizer. Therefore, by the argument after [\[Category Theory\] §Limits, ⁋Example 7](/en/math/category_theory/limits#ex7), $$\Grp$$ is a complete category.

On the other hand, any morphism in $$\Grp$$ has a coequalizer. ([§Isomorphism Theorems, ⁋Proposition 8](/en/math/algebraic_structures/isomorphism_theorems#prop8)) Therefore, if $$\Grp$$ has any coproduct, $$\Grp$$ becomes a cocomplete category, and hence a bicomplete category.

However, unlike in [§Direct Products of Groups, ⁋Lemma 1](/en/math/algebraic_structures/direct_products#lem1), it seems difficult to trivially find a way to equip the coproduct $$\coprod G_i$$ in $$\Set$$ with a group structure. ([\[Set Theory\], §Sum of Sets, ⁋Proposition 5](/en/math/set_theory/sum_of_sets#prop5))

In this post, we first show that abelian groups form a category with coproducts. In the next post, we will show through a different approach that for *arbitrary* groups, there exists a group satisfying the universal property of coproducts.

## Restricted Sum

Let a family of groups $$(G_i)$$ and their product be given. Then each $$G_i$$ can be viewed as a subgroup of $$\prod G_i$$ through $$\iota_i$$. Naturally, we can consider whether the equation

$$\prod_{i\in I} G_i=\left\langle\bigcup \iota_i(G_i)\right\rangle$$

holds. This equation almost never holds when $$I$$ is an infinite set. As the simplest example, let $$I=\mathbb{N}$$ and $$G_i=\mathbb{Z}/2\mathbb{Z}=\{\bar{0}, \bar{1}\}$$. Then, for instance, the left-hand side contains the element

$$(\bar{1},\bar{1},\cdots)$$

but the right-hand side only contains elements obtained through *finite* operations of $$\iota_i(\bar{1})$$, so it cannot contain the above element.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Let a family of groups $$(G_i)$$ be given, and fix subgroups $$H_i$$ of $$G_i$$. The subgroup consisting of $$x$$ such that $$\pr_ix\in H_i$$ for all but finitely many $$i$$ is called the *restricted sum* of $$G_i$$ with respect to $$H_i$$, denoted by $$\prod^H G_i$$.

In particular, when $$H_i=\{e\}$$ for all $$i$$, it is called the *weak direct product* of $$G_i$$, denoted simply by

$${\prod_{i\in I}}^w G_i$$

</div>

The notation $$\prod^H$$ is not particularly good notation, but fortunately we are only interested in weak direct products, so we will not use this notation again.

By definition,

$$\left\langle\bigcup \iota_i(G_i)\right\rangle={\prod_{i\in I}}^w G_i$$

holds. Also, if $$I$$ is finite, the weak direct product equals the usual direct product.

Then $$\prod^wG_i$$ has the following universal property.

<div class="proposition" markdown="1">

<ins id="thm2">**Theorem 2**</ins> Let a family of groups $$(G_i)$$ and their weak direct product $$\prod^w G_i$$ be given. For another group $$H$$, if group homomorphisms $$f_i:G_i\rightarrow H$$ satisfy the condition

> For any $$i\neq j$$, if $$x\in G_i$$ and $$y\in G_j$$, then $$f_i(x)f_j(y)=f_j(y)f_i(x)$$

then there exists a unique group homomorphism $$f:\prod^w G_i\rightarrow H$$ such that $$f_i=f\circ\iota_i$$ for all $$i$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, we show uniqueness. If $$f$$ and $$f'$$ satisfy the above equation, they must have the same values on $$\bigcup\iota_i(G_i)$$, so they must have the same values on $$\prod^w G_i$$, and therefore $$f=f'$$.

Now we show existence of $$f$$. For any $$x\in \prod^w G_i$$, define $$f(x)$$ by

$$f(x)=\prod_{i\in I} f_i(\pr_ix)$$

Here $$\prod$$ denotes the product of general elements. Since $$x$$ is an element of $$\prod^w G_i$$, $$f_i(\pr_ix)$$ is the identity element for all but finitely many $$i$$, so this product is well-defined.

That the equation $$f_i=f\circ\iota_i$$ holds is trivial, and that $$f$$ is a group homomorphism follows from: for any $$x,y\in\prod^wG_i$$,

$$f(xy)=\prod_{i\in I}f_i(\pr_i(xy))=\prod_{i\in I}f_i(\pr_ix)f_i(\pr_iy)$$

holds, so selecting only the finitely many values for which $$\pr_i(xy)$$ is not $$e_i$$ and denoting these indices by $$1,\ldots, n$$,

$$f_1(\pr_1x)f_1(\pr_1y)f_2(\pr_2x)f_2(\pr_2y)\cdots f_n(\pr_nx)f_n(\pr_ny)$$

and since $$f_i(\pr_ix)$$ and $$f_j(\pr_jy)$$ always commute when $$i\neq j$$, this can be rewritten as

$$f_1(\pr_1x)f_2(\pr_2x)\cdots f_n(\pr_nx)f_1(\pr_1y)f_2(\pr_2y)\cdots f_n(\pr_ny)$$

Thus $$f(xy)=f(x)f(y)$$ and $$f$$ is a group homomorphism. That $$f_i=f\circ\iota_i$$ is trivial.

</details>

The condition on $$f_i$$

> For any $$i\neq j$$, if $$x\in G_i$$ and $$y\in G_j$$, then $$f_i(x)f_j(y)=f_j(y)f_i(x)$$

is an inevitably arising condition, because this condition is exactly what $$\iota_i$$ satisfy. Because of this, [Theorem 6](#thm6) becomes the answer to our question only for abelian groups.

Using the universal property of weak direct products, we can prove several properties similar to those of direct products. For example, the following holds.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> If $$G_i$$ are groups and $$H_i$$ are normal subgroups of $$G_i$$, then $$\prod^w H_i$$ are also normal subgroups of $$\prod^w G_i$$, and their quotient group equals $$\prod^w (G_i/H_i)$$.

</div>

## Internal Weak Product

Let $$G$$ be a group and $$(H_i)$$ a family of subgroups of $$G$$. If whenever $$i\neq j$$, elements of $$H_i$$ commute with elements of $$H_j$$, then the inclusion homomorphisms $$\iota_i:H_i\rightarrow G$$ induce a homomorphism $$\iota$$ from $$\prod^w H_i$$ to $$G$$.

Also, we define the following.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> In the above situation, if $$\iota$$ is an isomorphism, we say that $$G$$ is the *internal weak direct product* of $$H_i$$.

</div>

Considering the form of the homomorphism $$f$$ constructed in [Theorem 2](#thm2), we can verify that $$G$$ being the internal weak direct product of $$H_i$$ is equivalent to the condition

> Any $$x\in G$$ can be expressed as a product $$\prod y_i$$ of a finitely supported family $$(y_i)_{i\in I}$$ with $$y_i\in H_i$$.

If the subgroups $$H_i$$ are all normal subgroups of $$G$$, then additionally, the following condition makes $$G$$ the internal weak direct product of $$H_i$$.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> If normal subgroups $$(H_i)$$ of a group $$G$$ satisfy the following two conditions

1. $$G=\bigl\langle\bigcup_{i\in I} H_i\bigr\rangle$$,
2. $$H_k\cap \bigl\langle\bigcup_{i\neq k} H_i\bigr\rangle=\{e\}$$

then $$G$$ is the internal weak direct product of $$H_i$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, condition 2 shows that $$H_i\cap H_j=\{e\}$$ holds for all pairs $$i\neq j$$. Now choosing arbitrary $$x_i\in H_i,x_j\in H_j$$, from

$$x_ix_jx_i^{-1}x_j^{-1}=x_i\bigl(x_jx_i^{-1}x_j^{-1}\bigr)=\bigl(x_ix_jx_i^{-1}\bigr)x_j^{-1}\in H_i\cap H_j=\{e\}$$

we see that elements of $$H_i$$ and $$H_j$$ commute. Therefore, the inclusion homomorphisms $$\iota_i$$ induce $$\iota$$ as in [Theorem 2](#thm2).

To show that $$G$$ is the internal weak direct product of $$H_i$$, we need to show that this induced $$\iota$$ is an isomorphism. First, by condition 1, any $$a\in G$$ is obtained through *finite* operations on $$\bigcup H_i$$. Also, since $$H_i$$ commute with each other, $$a$$ can be written as

$$a=\prod_{i\in I} h_i=\prod_{i\in I}\iota_i(h_i),\qquad\text{$\supp(h_i)$ finite and $h_i\in H_i$}$$

Letting $$h=\prod_{i\in I} \iota_i(h_i)\in\prod^w H_i$$,

$$a=\prod_{i\in I}\iota_i(h_i)=\iota_i\left(\prod_{i\in I}h_i\right)=\iota_i(h)$$

so $$\iota$$ is surjective.

Now suppose $$\iota(a)=e$$. Then we can write $$a=(a_i)_{i\in I}$$ for a finitely supported family $$(a_i)$$ with each term belonging to $$H_i$$. From the equation

$$\iota(a)=\prod_{i\in I}\iota_i(a_i)=\prod_{i\in I} a_i=e$$

if $$\supp(a_i)$$ has more than one element, and if $$i\in\supp(a_i)$$, then

$$a_i^{-1}=\prod_{j\in I\setminus\{i\}}a_j\in H_i\cap \left\langle\bigcup_{j\neq i} H_i\right\rangle=\{e\}$$

contradicting the assumption that $$i\in\supp(a_i)$$. Therefore, $$\supp(a_i)$$ is empty and $$a$$ is the identity element.

</details>


---

**References**

**[Hun]** Thomas W. Hungerford, *Algebra*, Graduate texts in mathematics, Springer, 2003.

---
