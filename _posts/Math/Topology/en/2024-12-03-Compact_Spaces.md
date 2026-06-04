---
title: "Compact Spaces"
description: "This post covers the definition of compactness in topological spaces and the conditions for the existence of finite subcovers, along with criteria for determining the compactness of subspaces and a proof that closed subsets of compact spaces are compact."
excerpt: "Compact spaces, defined by the existence of a finite subcover for every open cover"

categories: [Math / Topology]
permalink: /en/math/topology/compact_spaces
sidebar: 
    nav: "topology-en"

date: 2024-12-03
last_modified_at: 2024-12-03
weight: 14
translated_at: 2026-06-03T07:00:01+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-03T07:00:01+00:00
---
We now define the notion of compactness.

## Compact Sets

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A topological space $$X$$ is *compact* if for every open covering $$(U_i)_{i\in I}$$ of $$X$$, there exists a finite subset $$J\subseteq I$$ such that $$(U_j)_{j\in J}$$ is still an open covering of $$X$$.

</div>

By definition, a finite union of compact spaces is again compact. Thus compactness is related to an appropriate kind of finiteness.

Consider a subspace $$Y$$ of a topological space $$X$$. Then $$Y$$ is itself a topological space, so we may ask whether it is compact. The following proposition shows that to verify the compactness of $$Y$$, it suffices to consider coverings by open sets in $$X$$.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> Let $$Y$$ be a subspace of a topological space $$X$$. Then the following are equivalent: $$Y$$ is compact, and for every family $$(U_i)_{i\in I}$$ of open sets in $$X$$ satisfying $$Y\subseteq\bigcup U_i$$, there exists a finite subset $$J\subseteq I$$ such that the union of $$(U_j)_{j\in J}$$ still contains $$Y$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, assume that $$Y$$ is compact, and let $$(U_i)_{i\in I}$$ be a family of open sets in $$X$$ satisfying $$Y\subseteq\bigcup U_i$$. Then the sets $$Y\cap U_i$$ are open in $$Y$$, so $$(U_i\cap Y)_{i\in I}$$ is an open covering of $$Y$$. Hence we can choose a finite subset $$J$$ such that $$(U_j\cap Y)_{j\in J}$$ is still an open covering of $$Y$$. It is then obvious that the union of the $$(U_j)$$ still contains $$Y$$.

Conversely, assume that the stated condition holds, and let $$(V_i)_{i\in I}$$ be an arbitrary open covering of $$Y$$. By the definition of the topology on $$Y$$, there exist open sets $$(U_i)$$ in $$X$$ such that $$V_i=U_i\cap Y$$, and $$\bigcup U_i$$ contains $$Y$$. Thus there exists a finite subset $$J$$ such that the union of $$(U_j)_{j\in J}$$ contains $$Y$$. Then $$(V_j)_{j\in J}$$ is the desired finite subcover of $$(V_i)_{i\in I}$$.

</details>

By the proposition above, to prove that $$Y$$ is compact it suffices to cover $$Y$$ by open sets in the ambient space $$X$$ and then show that these satisfy the condition of [Definition 1](#def1). Therefore, by a slight abuse of terminology, we call open sets $$U_i$$ in $$X$$ satisfying $$Y\subseteq \bigcup U_i$$ an open cover of $$Y$$, and we shall make this distinction explicit only when there is a risk of confusion.

<div class="proposition" markdown="1">

<ins id="prop3">**Lemma 3**</ins> A closed subset of a compact space is compact.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$X$$ be a compact space, let $$Y$$ be a closed subset of $$X$$, and let $$(U_i)$$ be an open covering of $$Y$$. Then $$X\setminus Y$$ is open, and adding this set to the covering $$(U_i)$$ yields an open covering of $$X$$. Since $$X$$ is compact, this new covering has a finite subcover; removing $$X\setminus Y$$ from it again gives a covering of $$Y$$, which is a finite subcover of the original $$(U_i)$$.

</details>

## Compact Hausdorff Spaces

For a Hausdorff space, defined in the previous post, imposing the compact condition yields stronger separation properties. To see this, we first establish the following lemma.

<div class="proposition" markdown="1">

<ins id="lem4">**Lemma 4**</ins> Let $$X$$ be a Hausdorff space, let $$x$$ be a point of $$X$$, and let $$Y$$ be a compact subspace of $$X$$ not containing $$x$$. Then the two sets $$\{x\}$$ and $$Y$$ can be separated by neighborhoods.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Since $$X$$ is a Hausdorff space, for each $$y\in Y$$ there exist an open neighborhood $$U_{xy}$$ of $$x$$ and an open neighborhood $$V_y$$ of $$y$$ such that $$U_{xy}\cap V_y=\emptyset$$. Now by [Lemma 3](#lem3) there exists a finite subcover $$V_{y_1},\ldots,V_{y_n}$$ of $$(V_y)_{y\in Y}$$ such that

$$Y\subseteq V_{y_1}\cup\cdots\cup V_{y_n}$$

still holds. Then

$$U_{xy_1}\cap \cdots\cap U_{xy_n}$$

is an open neighborhood of $$\{x\}$$ disjoint from $$\bigcup_{i=1}^n V_{y_i}$$.

</details>

In particular, the following holds.

<div class="proposition" markdown="1">

<ins id="cor5">**Corollary 5**</ins> A compact subset of a Hausdorff space is closed.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

From the proof of [Lemma 4](#lem4), setting

$$U_x=U_{xy_1}\cap \cdots\cap U_{xy_n}$$

we have $$X\setminus Y=\bigcup_{x\not\in Y} U_x$$.

</details>

As mentioned above, a compact Hausdorff space satisfies the following additional separation axiom. ([§Hausdorff Spaces, ⁋Definition 3](/en/math/topology/Hausdorff_spaces#def3))

<div class="proposition" markdown="1">

<ins id="lem6">**Lemma 6**</ins> A compact Hausdorff space is regular.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Fix a compact Hausdorff space $$X$$, and let $$x\in X$$ be a point and $$Y$$ a closed subset of $$X$$ not containing $$x$$. Then $$Y$$ is compact by [Lemma 3](#lem3), and the desired result follows immediately from [Lemma 4](#lem4).

</details>

Moreover, applying this once more yields the following proposition.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> A compact Hausdorff space is normal.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$A$$ and $$B$$ be any two disjoint closed subsets of a compact Hausdorff space. Then for each $$a\in A$$, by [Lemma 6](#lem6) there exist an open neighborhood $$U_a$$ of $$a$$ and an open neighborhood $$V_a$$ of $$B$$ such that $$U_a\cap V_a=\emptyset$$. Now, in the same way as in [Lemma 4](#lem4), $$(U_a)_{a\in A}$$ is an open covering of $$A$$, so again by [Lemma 3](#lem3) we can take a finite subcover $$U_{a_1},\ldots, U_{a_n}$$ of $$(U_a)$$. Then the two open sets

$$U_{a_1}\cup\cdots \cup U_{a_n},\qquad V_{a_1}\cap\cdots\cap V_{a_n}$$

are open neighborhoods separating the two closed subsets $$A$$ and $$B$$.

</details>

## Compact Spaces and Continuous Functions

Compactness also behaves well with respect to continuous functions.

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8**</ins> For a continuous function $$f:X \rightarrow Y$$ and any compact subspace $$A$$ of $$X$$, the image $$f(A)$$ is also compact.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

For any open covering $$(U_i)$$ of $$f(A)$$, the family $$(f^{-1}(U_i))$$ covers $$A$$, and since $$A$$ is compact, a finite subcover exists. The corresponding $$U_i$$ then form a finite open subcover of $$f(A)$$.

</details>

Meanwhile, we have seen that a bijective continuous function $$f:X \rightarrow Y$$ need not be a homeomorphism; however, if $$X$$ is compact and $$Y$$ is Hausdorff, then this is indeed the case.

<div class="proposition" markdown="1">

<ins id="prop9">**Proposition 9**</ins> If $$X$$ is compact and $$Y$$ is Hausdorff, then any bijective continuous function $$f:X \rightarrow Y$$ is a homeomorphism.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

To show this, we must prove that $$f^{-1}$$ is continuous. We use the third condition of [§Continuous Functions, ⁋Theorem 4](/en/math/topology/continuous_functions#thm4): namely, we show that $$f$$ is a closed map. Given a closed subset $$A$$ of $$X$$, this follows by applying [Lemma 3](#lem3), [Proposition 8](#prop8), and [Corollary 5](#cor5) in order.

</details>

## Finite Intersection Property

<div class="definition" markdown="1">

<ins id="def10">**Definition 10**</ins> A family $$\mathcal{A}$$ of subsets of a set $$X$$ has the *finite intersection property* if for any finitely many elements $$A_1,\ldots, A_n$$ of $$\mathcal{A}$$,

$$A_1\cap\cdots\cap A_n$$

is nonempty.

</div>

Then in particular $$\emptyset\not\in \mathcal{A}$$. Moreover, given a family $$\mathcal{A}$$ satisfying this condition, we may add all finite intersections of elements of $$\mathcal{A}$$ to obtain a filter base $$\mathcal{B}$$ on $$X$$. ([§Other Definitions of Topological Spaces, ⁋Definition 5](/en/math/topology/equivalent_formulations_of_topology#def5)) For this reason $$\mathcal{A}$$ is sometimes called a *subbase* of $$\uparrow \mathcal{B}$$.

The following proposition gives an alternative characterization of compactness.

<div class="proposition" markdown="1">

<ins id="prop11">**Proposition 11**</ins> A topological space $$X$$ is compact if and only if for every family $$\mathcal{A}$$ of closed sets satisfying the finite intersection property, $$\bigcap \mathcal{A}\neq\emptyset$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

It suffices to take complements.

</details>
