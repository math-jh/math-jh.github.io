---
title: "Proper Maps"
description: "This post covers the definition and properties of universally closed maps. It proves equivalence conditions between universally closed maps, closed maps, and homeomorphisms for continuous injective functions, and examines properties related to subsets and covers."
excerpt: "The relationship between proper maps as universally closed maps and compactness"

categories: [Math / Topology]
permalink: /en/math/topology/proper_maps
sidebar: 
    nav: "topology-en"

date: 2024-12-15
weight: 17
translated_at: 2026-06-03T10:00:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-03T10:00:02+00:00
---
## Universally Closed Maps

In general, the fact that continuous functions $$f_1:X_1 \rightarrow Y_1$$ and $$f_2: X_2 \rightarrow Y_2$$ are closed does not imply that their product $$f_1\times f_2: X_1\times X_2 \rightarrow Y_1\times Y_2$$ is closed.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A continuous function $$f:X \rightarrow Y$$ is called *universally closed* if for every topological space $$Z$$, the map $$f\times\id_Z: X\times Z \rightarrow Y\times Z$$ is closed.

</div>

Taking $$Z=\{\ast\}$$, one can show that any universally closed map is a closed map, but the converse does not hold. Nevertheless, the following does hold.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> If $$f:X \rightarrow Y$$ is a continuous injective map, then the following are equivalent.

1. $$f$$ is universally closed.
2. $$f$$ is closed.
3. $$f$$ is a homeomorphism between $$X$$ and $$f(X)$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

By the argument above, it is obvious that the first condition implies the second. On the other hand, since $$f$$ is injective, its canonical decomposition shows that it is a homeomorphism between $$X$$ and $$f(X)$$. ([§Open Mappings and Closed Mappings, ⁋Proposition 5](/en/math/topology/open_mappings_and_closed_mappings#prop5)) Now assume that the third condition holds. Then for any $$Z$$, the map $$f\times\id_Z$$ is a homeomorphism from $$X\times Z$$ onto the closed subset $$f(X)\times Z$$ of $$Y\times Z$$, which yields the desired result.

</details>

However, in general one must check directly whether a function $$f$$ is universally closed. The second result of the following proposition shows that this can be examined on the target $$Y$$.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> Let a continuous function $$f:X \rightarrow Y$$ be given. Then the following hold.

1. If $$f$$ is universally closed, then for any subset $$A$$ of $$Y$$, the restriction $$f\vert_{f^{-1}(A)}: f^{-1}(A) \rightarrow A$$ is also universally closed.
2. Let $$(A_i)_{i\in I}$$ be a covering of $$Y$$ that is either (1) a locally finite closed covering, or (2) such that $$(\interior A_i)_{i\in I}$$ is an open covering of $$Y$$. If each restriction $$f\vert_{f^{-1}(A_i)}$$ is universally closed, then so is $$f$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, to prove the first statement, let an arbitrary topological space $$Z$$ be given. Then for any subset $$A$$ of $$Y$$,

$$(f\vert_{f^{-1}(A)})\times \id_Z=(f\times\id_Z)\vert_{f^{-1}(A\times Z)}$$

holds. Since $$f$$ is universally closed, the map $$f\times\id_Z$$ is closed, and therefore so is $$(f\times\id_Z)\vert_{f^{-1}(A\times Z)}$$.

Now let us prove the second statement. If $$(A_i)$$ satisfies the given condition, then $$(A_i\times Z)$$ satisfies the same condition. If the $$f\vert_{f^{-1}(A_i)}$$ are universally closed, then the maps

$$(f\times\id_Z)\vert_{f^{-1}(A_i\times Z)}$$

are closed, and thus $$f\times\id_Z$$ is also closed. ([§Open Mappings and Closed Mappings, ⁋Proposition 3](/en/math/topology/open_mappings_and_closed_mappings#prop3))

</details>

Moreover, the following holds.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> For two continuous functions $$f:X \rightarrow Y$$ and $$g:Y \rightarrow Z$$, the following hold.

1. If both $$f$$ and $$g$$ are universally closed, then so is $$g\circ f$$.
2. If $$g\circ f$$ is universally closed and $$f$$ is surjective, then $$g$$ is universally closed.
3. If $$g\circ f$$ is universally closed and $$g$$ is injective, then $$f$$ is universally closed.
4. If $$g\circ f$$ is universally closed and $$Y$$ is Hausdorff, then $$f$$ is universally closed.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

The first three statements are all immediate from the identity

$$(g\circ f)\times\id_Z=(g\times\id_Z)\circ(f\times\id_Z)$$

and the results of [§Open Mappings and Closed Mappings, ⁋Proposition 2](/en/math/topology/open_mappings_and_closed_mappings#prop2).

For the last statement, define two functions $$\Gamma_f: X \rightarrow X\times Y$$ and $$\Gamma_g: Y \rightarrow Z\times Y$$ respectively by

$$\Gamma_f(x)=(x,f(x)),\qquad \Gamma_g(y)=(g(y), y)$$

Then one easily verifies the identity

$$((g\circ f)\times\id_Y)\circ\Gamma_f=\Gamma_g\circ f$$

Here $$\Gamma_f$$ and $$\Gamma_g$$ are homeomorphisms from $$X$$ and $$Y$$ onto the graphs of $$f$$ and $$g$$, respectively. ([§Product Spaces, ⁋Corollary 4](/en/math/topology/product_spaces#cor4)) Moreover, since $$Y$$ is Hausdorff, we know that $$\Gamma(f)\subseteq X\times Y$$ is a closed set. ([§Hausdorff Spaces, ⁋Corollary 7](/en/math/topology/Hausdorff_spaces#cor7)) Hence, by [Proposition 2](#prop2), we know that $$\Gamma_f$$ is universally closed. On the other hand, one can show without difficulty that the product of universally closed maps is universally closed; combining this with [Proposition 4](#prop4), we know that $$(g\circ f)\times\id_Y$$ is universally closed. Therefore the right-hand side $$\Gamma_g\circ f$$ of the above identity is also universally closed, and since $$\Gamma_g$$ is injective, $$f$$ is universally closed.

</details>

## Compactness and Universally Closed Maps

So far, it is not apparent how this definition is related to compactness; in this section we examine the relationship between them. Before doing so, we need to say a little about filters in order to use [§Compactness, ⁋Lemma 1](/en/math/topology/compactness#lem1).

Let an arbitrary topological space $$X$$ and an arbitrary filter $$\mathcal{F}$$ on it be given. Consider the set $$X'=X\cup \{\ast_X\}$$ obtained by adjoining one point to $$X$$, and the filter

$$\mathcal{F}'=\{F\cup\{\ast_X\}: F\in \mathcal{F}\}$$

on it. Now define $$\mathcal{N}(x)=\uparrow\{x\}$$ for any $$x\in X'$$ other than $$\ast_X$$, and $$\mathcal{N}(\ast_X)=\mathcal{F}'$$. Then this satisfies all four conditions of [§Open Sets, ⁋Proposition 6](/en/math/topology/open_sets#prop6), and thus defines a topology on $$X'$$. In this topological space $$X'$$, the point $$\ast_X$$ lies in the closure of $$X$$, and it is obvious that $$\mathcal{F}=\mathcal{F}'\vert_X=\mathcal{N}(\ast_X)\vert_X$$.

Then we can prove the following lemma.

<div class="proposition" markdown="1">

<ins id="lem5">**Lemma 5**</ins> For a topological space $$X$$, suppose $$f: X \rightarrow \{\ast\}$$ is universally closed. Then $$X$$ is compact.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

For an arbitrary filter $$\mathcal{F}$$ on $$X$$, consider the space $$X'$$ obtained from the above construction. Also, define the subset $$\Delta$$ of $$X\times X'$$ by

$$\Delta=\{(x,x)\mid x\in X\}$$

Then we may consider the closure $$\cl\Delta$$ of $$\Delta$$, and from the assumption that $$f$$ is universally closed, we know that the image of $$\cl\Delta$$ under $$f\times\id_{X'}:X\times X'\rightarrow \{\ast\}\times X'\cong X'$$ is a closed set. Since this image contains $$x$$, and since $$\ast_X$$ lies in the closure, we know that there exists a suitable $$x\in X$$ such that $$(x,\ast_X)\in \cl\Delta$$. Then $$x$$ is a cluster point of $$\mathcal{F}$$, and therefore, considering an ultrafilter containing $$\mathcal{F}$$, we know that $$x$$ is the limit point of that filter.

</details>

The converse of the above lemma also holds. More generally, the following holds.

<div class="proposition" markdown="1">

<ins id="thm6">**Theorem 6**</ins> For a continuous function $$f:X \rightarrow Y$$, the following are equivalent.

1. $$f$$ is universally closed.
2. $$f$$ is closed, and for each $$y\in Y$$, the fiber $$f^{-1}(y)$$ is compact.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

If the first condition holds, then for any $$y\in Y$$, we know that $$f\vert_{f^{-1}(y)}$$ is universally closed, and from the preceding lemma we know that $$f^{-1}(y)$$ is compact. The converse can be proved using the fact that the product of universally closed maps is universally closed.

</details>

Thus, we could equally well have defined a compact space by requiring that $$f:X \rightarrow \{\ast\}$$ be universally closed. In particular, the following holds.

<div class="proposition" markdown="1">

<ins id="cor7">**Corollary 7**</ins> If a continuous function $$f:X \rightarrow Y$$ is universally closed, then for any compact subset $$C\subseteq Y$$, the preimage $$f^{-1}(C)$$ is also compact.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Since $$f$$ is universally closed, $$f\vert_{f^{-1}(C)}$$ is universally closed. On the other hand, $$C \rightarrow\{\ast\}$$ is universally closed because $$C$$ is compact, and therefore the composition $$f^{-1}(C) \rightarrow C \rightarrow \{\ast\}$$ is universally closed; hence $$f^{-1}(C)$$ is also compact.

</details>

## Proper Maps

A function $$f$$ satisfying the conclusion of [Corollary 7](#cor7) is called a *proper map*. The following proposition shows that the converse of the above corollary also holds in a special case.

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8**</ins> Let a continuous function $$f:X \rightarrow Y$$ between Hausdorff spaces be given, and additionally assume that $$Y$$ is locally compact. Then $$f$$ being universally closed and $$f$$ being proper are equivalent.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

As noted earlier, that $$f$$ being universally closed implies $$f$$ is proper is the content of [Corollary 7](#cor7). Thus the heart of this proposition is the reverse direction. Since $$Y$$ is locally compact, there exists an open covering $$(U_i)$$ of $$Y$$ consisting of open sets each contained in some compact set. Then the $$f^{-1}(\cl U_i)$$ are compact in $$X$$ and each $$f\vert_{f^{-1}(\cl U_i)}$$ is universally closed. Hence by [Proposition 3](#prop3), we obtain the desired result.

</details>

In particular, applying this to the one-point compactification examined earlier yields the following result.

<div class="proposition" markdown="1">

<ins id="cor9">**Corollary 9**</ins> Let two locally compact Hausdorff spaces $$X_1, X_2$$ be given, and let their one-point compactifications be $$\overline{X}_i=X_i\cup \{\ast_i\}$$. Then $$f:X_1 \rightarrow X_2$$ being universally closed is equivalent to $$\overline{f}:\overline{X}_1 \rightarrow \overline{X}_2$$ defined by

$$\overline{f}(x)=\begin{cases}\ast_2&\text{if $x=\ast_1$}\\f(x)&\text{otherwise}\end{cases}$$

being continuous.

</div>
