---title: "Compact Spaces"
excerpt: "Compact spaces, defined by the existence of a finite subcover for every open cover"

categories: [Math / Topology]
permalink: /en/math/topology/compact_spaces
header:
    overlay_image: /assets/images/Math/Topology/Compact_Spaces.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology-en"

date: 2024-12-03
last_modified_at: 2024-12-03
weight: 14
translated_at: 2026-05-28T11:36:15+00:00
translation_source: kimi-cli
---
In this post we define the notion of compactness.

## Compact Sets

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A topological space $$X$$ is *compact* if for every open covering $$(U_i)_{i\in I}$$ of $$X$$, there exists a finite subset $$J\subseteq I$$ such that $$(U_j)_{j\in J}$$ is still an open covering of $$X$$.

</div>

By definition, a finite union of compact spaces is again compact. In this way, compactness is related to an appropriate kind of finiteness.

Consider a subspace $$Y$$ of a topological space $$X$$. Then $$Y$$ is also a topological space, so we can examine whether this topological space is compact. The following proposition shows that to check whether $$Y$$ is compact, it suffices to consider coverings consisting of open sets in $$X$$.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> Consider a subspace $$Y$$ of a topological space $$X$$. Then the following are equivalent: $$Y$$ is compact, and for every family $$(U_i)_{i\in I}$$ of open sets in $$X$$ satisfying $$Y\subseteq\bigcup U_i$$, there exists a finite subset $$J\subseteq I$$ such that the union of $$(U_j)_{j\in J}$$ still contains $$Y$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, assume that $$Y$$ is compact, and suppose a family $$(U_i)_{i\in I}$$ of open sets in $$X$$ satisfying $$Y\subseteq\bigcup U_i$$ is given. Then the $$Y\cap U_i$$ are open in $$Y$$, and thus $$(U_i\cap Y)_{i\in I}$$ is an open covering of $$Y$$, from which we can choose a finite subset $$J$$ such that $$(U_j\cap Y)_{i\in J}$$ is still an open covering of $$Y$$. Then it is obvious that the union of the $$(U_j)$$ still contains $$Y$$.

Conversely, assume that the given condition holds, and suppose an arbitrary open covering $$(V_i)_{i\in I}$$ of $$Y$$ is given. Then by the definition of the topology on $$Y$$, there exist open sets $$(U_i)$$ in $$X$$ such that $$V_i=U_i\cap Y$$, and $$\bigcup U_i$$ contains $$Y$$. Thus there exists a finite subset $$J$$ such that the union of the $$(U_j)_{j\in J}$$ contains $$Y$$. Then $$(V_j)_{j\in J}$$ is the desired finite subcover of $$(V_i)_{i\in I}$$.

</details>

By the above proposition, to prove the compactness of $$Y$$ it suffices to cover $$Y$$ by open sets in the ambient space $$X$$ containing $$Y$$, and then show that these satisfy the condition of [Definition 1](#def1). Therefore, by a slight abuse of terminology, we call open sets $$U_i$$ in $$X$$ satisfying $$Y\subseteq \bigcup U_i$$ an open cover of $$Y$$, and we will only make this distinction explicit when there is a risk of confusion. 

<div class="proposition" markdown="1">

<ins id="prop3">**Lemma 3**</ins> A closed subset of a compact space is compact.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Suppose a compact space $$X$$ and a closed subset $$Y$$ of $$X$$ are given, and suppose an open covering $$(U_i)$$ of $$Y$$ is given. Then $$X\setminus Y$$ is an open set, and adding this set to the open covering $$(U_i)$$ of $$Y$$ gives an open covering of $$X$$. Since $$X$$ is compact, a finite subcover of this new covering exists, and removing $$X\setminus Y$$ from this finite subcover again yields a covering of $$Y$$, which is a finite subcover of the original $$(U_i)$$.

</details>

## Compact Hausdorff Spaces

In the case of a Hausdorff space, defined in the previous post, adding the compact condition yields better separation properties. To see this, we first prove the following lemma.

<div class="proposition" markdown="1">

<ins id="lem4">**Lemma 4**</ins> Suppose a Hausdorff space $$X$$ is given, a point $$x$$ of $$X$$, and a compact subspace $$Y$$ of $$X$$ not containing $$x$$. Then the two sets $$\{x\}$$ and $$Y$$ can be separated by neighborhoods.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Since $$X$$ is a Hausdorff space, for each $$y\in A$$ there exist an open neighborhood $$U_{xy}$$ of $$x$$ and an open neighborhood $$V_y$$ of $$y$$ such that $$U_{xy}\cap V_y=\emptyset$$. Now by [Lemma 3](#lem3) there exists a finite subcover $$V_{y_1},\ldots,V_{y_n}$$ of $$(V_y)_{y\in Y}$$ such that still

$$Y\subseteq V_{y_1}\cup\cdots\cup V_{y_n}$$

holds. Now

$$U_{xy_1}\cap \cdots\cap U_{xy_n}$$

is an open neighborhood of $$\{x\}$$ disjoint from $$\bigcup_{i=1}^n V_{y_i}$$.

</details>

In particular, the following holds.

<div class="proposition" markdown="1">

<ins id="cor5">**Corollary 5**</ins> A compact subset $$Y$$ of a Hausdorff space $$X$$ is closed.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

From the proof of [Lemma 4](#lem4), setting

$$U_x=U_{xy_1}\cap \cdots\cap U_{xy_n}$$

we have $$X\setminus Y=\bigcup_{x\not\in Y} U_x$$.

</details>

As mentioned above, a compact Hausdorff space satisfies the following additional separation axiom. ([§Hausdorff Spaces, ⁋Definition 3](/en/math/topology/Hausdorff_spaces#def3))

<div class="proposition" markdown="1">

<ins id="lem6">**Lemma 6**</ins> A compact Hausdorff space is a regular space.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Fix a compact Hausdorff space $$X$$, and suppose a point $$x\in X$$ and a closed subset $$Y$$ of $$X$$ not containing $$x$$ are given. Then $$Y$$ is compact by [Lemma 3](#lem3), and thus the desired result follows immediately from [Lemma 4](#lem4). 

</details>

Moreover, applying this once more yields the following proposition.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> A compact Hausdorff space is a normal space.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Suppose any two disjoint closed subsets $$A,B$$ of a compact Hausdorff space are given. Then for each $$a\in A$$, by [Lemma 6](#lem6) there exist an open neighborhood $$U_a$$ of $$a$$ and an open neighborhood $$V_{a}$$ of $$B$$ such that $$U_a\cap V_a=\emptyset$$. Now, in the same way as in [Lemma 4](#lem4), $$(U_a)_{a\in A}$$ becomes an open covering of $$A$$, so again by [Lemma 3](#lem3) we can take a finite subcover $$U_{a_1},\ldots, U_{a_n}$$ of $$(U_a)$$, and now the two open sets

$$U_{a_1}\cup\cdots \cup U_{a_n},\qquad V_{a_1}\cap\cdots\cap V_{a_n}$$

are open neighborhoods separating these two closed subsets $$A,B$$.

</details>

## Compact Spaces and Continuous Functions

Compactness also behaves well with respect to continuous functions.

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8**</ins> For a continuous function $$f:X \rightarrow Y$$ and any compact subspace $$A$$ of $$X$$, $$f(A)$$ is also compact.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

For any open covering $$(U_i)$$ of $$f(A)$$, $$(f^{-1}(U_i))$$ is a covering of $$A$$, and since $$A$$ is compact, a finite subcover exists. The corresponding $$U_i$$ form a finite open subcover of $$f(A)$$.

</details>

Meanwhile, we saw that a bijective continuous function $$f:X \rightarrow Y$$ need not be a homeomorphism; however, if $$X$$ is compact and $$Y$$ is Hausdorff, then this does hold.

<div class="proposition" markdown="1">

<ins id="prop9">**Proposition 9**</ins> If $$X$$ is compact and $$Y$$ is Hausdorff, then any bijective continuous function $$f:X \rightarrow Y$$ is a homeomorphism.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

To show this, we must prove that $$f^{-1}$$ is continuous. Let us use the third condition of [§Continuous Functions, ⁋Theorem 4](/en/math/topology/continuous_functions#thm4). That is, we must show that $$f$$ is a closed map. But this follows by applying [Lemma 3](#lem3), [Proposition 8](#prop8), and [Corollary 5](#cor5) in order, given a closed subset $$A$$ of $$X$$.

</details>

## Finite Intersection Property

<div class="definition" markdown="1">

<ins id="def10">**Definition 10**</ins> A family $$\mathcal{A}$$ of subsets of a set $$X$$ has the *finite intersection property* if for any finitely many elements $$A_1,\ldots, A_n$$ of $$\mathcal{A}$$,

$$A_1\cap\cdots\cap A_n$$

is nonempty.

</div>

Then in particular $$\emptyset\not\in \mathcal{A}$$ holds. Also, if a family $$\mathcal{A}$$ satisfying this condition is given, we can add all finite intersections of elements of $$\mathcal{A}$$ to obtain a filter base $$\mathcal{B}$$ on $$X$$. ([§Equivalent Formulations of Topology, ⁋Definition 6](/en/math/topology/equivalent_formulations_of_topology#def6)) For this reason $$\mathcal{A}$$ is sometimes called a *subbase* of $$\uparrow \mathcal{B}$$.

Then the following proposition is an alternative formulation of compactness.

<div class="proposition" markdown="1">

<ins id="prop11">**Proposition 11**</ins> A topological space $$X$$ is compact if and only if for every family $$\mathcal{A}$$ of closed sets satisfying the finite intersection property, $$\bigcap \mathcal{A}\neq\emptyset$$. 

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

It suffices to take complements.

</details>
