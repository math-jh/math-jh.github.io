---
title: "Restricted Sum"
description: "This post covers the definitions of the restricted sum and weak direct product for a family of groups and shows that abelian groups form a category with coproducts through restricted sums."
excerpt: "Restricted sums of groups"

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/restricted_sums
sidebar: 
    nav: "algebraic_structures-en"

date: 2023-01-09
weight: 8
translated_at: 2026-08-16T13:15:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-09-08T07:15:04+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
Previously, we verified in [§Direct Product of Groups](/en/math/algebraic_structures/direct_products){: data-relation="required" } that arbitrary products exist in $\Grp$, and in [§Group Homomorphisms](/en/math/algebraic_structures/group_homomorphisms){: data-relation="weak" } that every pair of parallel morphisms in $\Grp$ has an equalizer. Hence, by the argument following [[Category Theory] §Limits, ⁋Example 7](/en/math/category_theory/limits#ex7), $\Grp$ is a complete category. 

On the other hand, every pair of parallel morphisms in $\Grp$ also has a coequalizer. ([§Group Isomorphisms, ⁋Proposition 8](/en/math/algebraic_structures/isomorphism_theorems#prop8){: data-relation="weak" }) Therefore, if $\Grp$ has arbitrary coproducts, $\Grp$ would be a cocomplete category, and hence a bicomplete category. 

However, as in [§Direct Product of Groups, ⁋Lemma 1](/en/math/algebraic_structures/direct_products#lem1), finding an obvious way to endow the coproduct in $\Set$, $\coprod G_i$, with a group structure seems difficult. ([\[Set Theory\] §Sum of Sets, ⁋Proposition 5](/en/math/set_theory/sum_of_sets#prop5){: data-relation="weak" }) 

Instead, we look for the answer inside the product $\prod G_i$, whose existence is already known. By viewing each $G_i$ as a subgroup of $\prod G_i$ and considering the subgroup they generate together, in this post we call the group obtained in this way the weak direct product and verify its universal property.

However, this universal property carries the condition that the images of homomorphisms coming from distinct $G_i$ must commute; consequently, the weak direct product becomes the construction we were looking for at least for abelian groups, but fails to be so for general groups. In the next post, by a method different from that of this post, we show that a group satisfying the universal property of the coproduct exists for *arbitrary* groups as well.

## Restricted sum

Let a family of groups $(G_i)$ and their product be given. For each $i$, since the map sending $g\in G_i$ to the element whose $i$-th component is $g$ and remaining components are the identity, $\iota_i:G_i\rightarrow\prod G_i$, is an injective group homomorphism, each $G_i$ can be viewed via $\iota_i$ as a subgroup of $\prod G_i$. Naturally, one can consider whether the following identity

$$\prod_{i\in I} G_i=\left\langle\bigcup \iota_i(G_i)\right\rangle$$

holds. This identity almost never holds if $I$ is an infinite set. As the simplest example, take $I=\mathbb{N}$ and let $G_i=\mathbb{Z}/2\mathbb{Z}=\{\bar{0}, \bar{1}\}$. Then, for example, the left-hand side contains the element

$$(\bar{1},\bar{1},\cdots)$$

but the right-hand side contains only elements obtained by *finite* operations on the $\iota_i(\bar{1})$, so it cannot contain the element above.

::: Definition 1
Let a family of groups $(G_i)$ be given, and for the $G_i$, fix subgroups $H_i$. Then, for all but finitely many $i$, the subgroup of elements satisfying $\pr_ix\in H_i$, consisting of all such $x$, is called, with respect to the $H_i$, the *restricted sum* of the $G_i$, and is denoted $\prod^H G_i$.

In particular, if for all $i$ we have $H_i=\{e\}$, it is called the *weak direct product* of the $G_i$, and is denoted simply by

$${\prod_{i\in I}}^w G_i$$
:::

The notation $\prod^H$ is not particularly good, but fortunately we are only interested in the weak direct product, so there will be no occasion to use this notation again. 

By definition,

$$\left\langle\bigcup \iota_i(G_i)\right\rangle={\prod_{i\in I}}^w G_i$$

holds. In particular, since the image of $\iota_i$ is contained in $\prod^w G_i$, from now on we regard $\iota_i$ as an injective homomorphism into $\prod^w G_i$. Also, if $I$ is a finite set, the weak direct product coincides with the ordinary direct product.

Then $\prod^wG_i$ has the following universal property.

::: Theorem 2
Let a family of groups $(G_i)$ and their weak direct product $\prod^w G_i$ be given. For another group $H$, if group homomorphisms $f_i:G_i\rightarrow H$ satisfy the condition

> for any $i\neq j$, if $x\in G_i$ and $y\in G_j$, then $f_i(x)f_j(y)=f_j(y)f_i(x)$
 
then there exists a unique group homomorphism $f:\prod^w G_i\rightarrow H$ such that $f_i=f\circ\iota_i$ holds for every $i$. 
:::
::: Proof
First, let us show uniqueness. If $f, f'$ satisfy the equation above, they must take the same values on $\bigcup\iota_i(G_i)$, and hence they must also take the same values on $\prod^w G_i$; therefore $f=f'$.

Now we must show the existence of $f$. For any $x\in \prod^w G_i$, let us define $f(x)$ by the formula

$$f(x)=\prod_{i\in I} f_i(\pr_ix)$$

Here $\prod$ denotes the ordinary product of elements. Since $x$ is an element of $\prod^w G_i$, the $f_i(\pr_ix)$ on the right-hand side are all the identity except for finitely many $i$. In addition, the non-identity factors of the element on the right-hand side come from distinct indices and hence commute with each other by hypothesis; thus this product is well-defined regardless of the order of multiplication. 

That the equation $f_i=f\circ\iota_i$ holds is obtained from $f(\iota_i(g))=\prod_{j\in I}f_j(\pr_j\iota_i(g))=f_i(g)$, and that $f$ is a group homomorphism follows because for any $x,y\in\prod^wG_i$,

$$f(xy)=\prod_{i\in I}f_i(\pr_i(xy))=\prod_{i\in I}f_i(\pr_ix)f_i(\pr_iy)$$

holds; choosing only the finitely many values such that at least one of $\pr_ix$ and $\pr_iy$ is not $e_i$, and letting these indices be $1,\ldots, n$, this expression becomes

$$f_1(\pr_1x)f_1(\pr_1y)f_2(\pr_2x)f_2(\pr_2y)\cdots f_n(\pr_nx)f_n(\pr_ny)$$

and since $f_i(\pr_ix)$ and $f_j(\pr_jy)$ always commute whenever $i\neq j$, this expression can be rewritten as

$$f_1(\pr_1x)f_2(\pr_2x)\cdots f_n(\pr_nx)f_1(\pr_1y)f_2(\pr_2y)\cdots f_n(\pr_ny)$$

Therefore, $f(xy)=f(x)f(y)$ and $f$ is a group homomorphism.
:::

The condition imposed on the $f_i$,

> for any $i\neq j$, if $x\in G_i$ and $y\in G_j$, then $f_i(x)f_j(y)=f_j(y)f_i(x)$

is a condition that inevitably had to arise, because these conditions are precisely those satisfied by the $\iota_i$. Because of this, [Theorem 2](#thm2){: data-relation="required" } is the answer to our question only for abelian groups.

Using the universal property of the weak direct product, one can show several properties similar to those for the direct product. For example, the following holds.

::: Proposition 3
If the $G_i$ are groups and the $H_i$ are normal subgroups of the $G_i$, then $\prod^w H_i$ is also a normal subgroup of $\prod^w G_i$, and its quotient group is equal to $\prod^w (G_i/H_i)$.
:::
::: Proof
Consider the canonical homomorphisms $p_i:G_i\rightarrow G_i/H_i$. For any $x\in\prod^wG_i$, the element $\bigl(p_i(\pr_ix)\bigr)_{i\in I}$ is the identity except for finitely many $i$, so it is an element of $\prod^w(G_i/H_i)$, and the map $p:\prod^wG_i\rightarrow\prod^w(G_i/H_i)$ obtained in this way is a homomorphism since each $p_i$ is a homomorphism on each component.

Given an element of $\prod^w(G_i/H_i)$, $y$, at indices where $\pr_iy$ is the identity, for such $i$ we choose $e$ as the representative, and for the remaining finitely many $i$ we choose arbitrary representatives to obtain an element of $\prod^wG_i$; hence $p$ is surjective. Also, $p(x)$ being the identity is equivalent to having for every $i$ that $\pr_ix\in H_i$, so $\ker p=\prod^wH_i$. Therefore, by [§Group Isomorphisms, ⁋Lemma 1](/en/math/algebraic_structures/isomorphism_theorems#lem1){: data-relation="required" }, $\prod^wH_i$ is a normal subgroup of $\prod^wG_i$, and by [§Group Isomorphisms, ⁋Theorem 2](/en/math/algebraic_structures/isomorphism_theorems#thm2){: data-relation="required" }, the identity

$$\biggl({\prod_{i\in I}}^wG_i\biggr)\bigg/\biggl({\prod_{i\in I}}^wH_i\biggr)\cong{\prod_{i\in I}}^w(G_i/H_i)$$

holds.
:::

## Internal weak product

Let $G$ be a group, and let $(H_i)$ be a family of subgroups of $G$. If whenever $i\neq j$ the elements of $H_i$ commute with the elements of $H_j$, then induced by the inclusion homomorphisms $\iota_i:H_i\rightarrow G$, there exists from $\prod^w H_i$ to $G$ a homomorphism $\iota$. Here, writing the inclusion homomorphism from $H_i$ to $\prod^wH_i$ as $\iota^w_i$, we have $\iota\circ\iota^w_i=\iota_i$.

We also define the following.

::: Definition 4
In the situation above, if $\iota$ is an isomorphism, we say that $G$ is the *internal weak direct product* of the $H_i$. 
:::

Considering the form of the homomorphism $f$ constructed in [Theorem 2](#thm2){: data-relation="required" }, one can verify that $G$ being the internal weak direct product of the $H_i$ is equivalent to the condition

> any $x\in G$ can be uniquely expressed, with $y_i\in H_i$, as the product of a finitely supported family $(y_i)_{i\in I}$, $\prod y_i$.

If the subgroups $H_i$ are all normal subgroups of $G$, then with the following additional conditions satisfied, $G$ becomes the internal weak direct product of the $H_i$.

::: Proposition 5
If for a group $G$, normal subgroups $(H_i)$ satisfy the two conditions

1. $G=\bigl\langle\bigcup_{i\in I} H_i\bigr\rangle$,
2. for each $k$, $H_k\cap \bigl\langle\bigcup_{i\neq k} H_i\bigr\rangle=\{e\}$

then $G$ is the internal weak direct product of the $H_i$.
:::
::: Proof
First, condition 2 shows in particular that $H_i\cap H_j=\{e\}$ holds for every pair $i\neq j$. Now choosing arbitrary $x_i\in H_i,x_j\in H_j$, from

$$x_ix_jx_i^{-1}x_j^{-1}=x_i\bigl(x_jx_i^{-1}x_j^{-1}\bigr)=\bigl(x_ix_jx_i^{-1}\bigr)x_j^{-1}\in H_i\cap H_j=\{e\}$$

we see that the elements of $H_i$ and $H_j$ commute. Hence the inclusion homomorphisms $\iota_i$ induce $\iota$ properly as in [Theorem 2](#thm2){: data-relation="required" }.

To show that $G$ is the internal weak direct product of the $H_i$, we must show that the $\iota$ induced in this way is an isomorphism. First, by condition 1, any $a\in G$ is obtained through *finite* operations of $\bigcup H_i$. Moreover, since the $H_i$ commute with each other, we can write $a$ as

$$a=\prod_{i\in I} h_i,\qquad\text{$\supp(h_i)$ finite and $h_i\in H_i$}$$

Setting $h=\prod_{i\in I} \iota^w_i(h_i)\in\prod^w H_i$, since

$$\iota(h)=\prod_{i\in I}\iota\bigl(\iota^w_i(h_i)\bigr)=\prod_{i\in I}\iota_i(h_i)=\prod_{i\in I}h_i=a$$

$\iota$ is surjective.

Now suppose $\iota(a)=e$. Then, with each term belonging to $H_i$, for a finitely supported family $(a_i)$, we can write $a=(a_i)_{i\in I}$. From the formula  

$$\iota(a)=\prod_{i\in I}\iota_i(a_i)=\prod_{i\in I} a_i=e$$
  
if $\supp(a_i)$ has at least one element and $i\in\supp(a_i)$, then

$$a_i^{-1}=\prod_{j\in I\setminus\{i\}}a_j\in H_i\cap \left\langle\bigcup_{j\neq i} H_j\right\rangle=\{e\}$$

which contradicts the assumption that $i\in\supp(a_i)$. Therefore, $\supp(a_i)$ is the empty set and $a$ is the identity. 
:::


---

**References**

**[Hun]** Thomas W. Hungerford, *Algebra*, Graduate texts in mathematics, Springer, 2003.

---
