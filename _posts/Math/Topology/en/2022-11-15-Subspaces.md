---
title: "Subspaces"
excerpt: "Properties of subspaces"

categories: [Math / Topology]
permalink: /en/math/topology/subspaces
header:
    overlay_image: /assets/images/Math/Topology/Subspaces.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology-en"

date: 2022-11-15
last_modified_at: 2022-11-15
weight: 7
translated_at: 2026-05-29T02:00:58+00:00
translation_source: kimi-cli
---
## Definition of Subspaces

Just as when dealing with algebraic structures, after equipping a set $$X$$ with a topological structure it is natural to examine how this structure is restricted to a subset $$A\subseteq X$$. The first thought that comes to mind is to select, among the open sets of $$X$$, only those contained in $$A$$ and define them to be the open sets of the topological space $$A$$. However, this attempt is bound to fail, because if $$A$$ is not an open set in $$X$$ then the whole set $$A$$ itself does not belong to this collection.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Let a topological space $$(X,\mathcal{T})$$ and a subset $$A$$ of $$X$$ be given. Then the initial topology on $$A$$ defined by the inclusion $$\iota:A\hookrightarrow X$$ is called *the subspace topology on $$A$$*.

</div>

For any open set $$U$$ of $$X$$, we have $$\iota^{-1}(U)=U\cap A$$, and for any family of open sets $$(U_i)_{i\in I}$$,

$$\iota^{-1}\left(\bigcup_{i\in I} U_i\right)=\left(\bigcup_{i\in I} U_i\right)\cap A=\bigcup_{i\in I} (U_i\cap A)=\bigcup_{i\in I} \iota^{-1}(U)$$

and for any finite family of open sets $$(U_i)_{i\in I}$$,

$$\iota^{-1}\left(\bigcap_{i\in I} U_i\right)=\left(\bigcap_{i\in I} U_i\right)\cap A=\bigcap_{i\in I} (U_i\cap A)=\bigcap_{i\in I} \iota^{-1}(U)$$

hold, so by [§Initial and Final Topology, ⁋Proposition 2](/en/math/topology/initial_and_final_topology#prop2) we see that the subspace topology $$\mathcal{T}_A$$ is given by the formula

$$\mathcal{T}_A=\{U\cap A\mid U\in\mathcal{T}\}$$

In books such as **[Mun]**, this is sometimes taken as the definition of a subspace. From this we see that if $$A\subseteq B\subseteq X$$, then whether we regard $$A$$ as a subspace of $$X$$ or as a subspace of $$B$$ (with the subspace topology), we obtain the same space.

One must be careful when dealing with subspaces: a set may be open in $$\mathcal{T}_A$$ without being open in $$\mathcal{T}$$.

![open_in_subspace_but_not_in_whole](/assets/images/Math/Topology/Subspaces-1.png){:style="width:12em"  class="invert" .align-center}

This situation is easily resolved if $$A$$ is an open set.

<div class="proposition" markdown="1">

<ins id="lem2" markdown="1">**Lemma 2**</ins> For a subspace $$A$$ of a topological space $$X$$, a necessary and sufficient condition for every open set of $$A$$ to be open in $$X$$ is that $$A$$ be an open set in $$X$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Since $$A$$ is an open set in $$A$$, one direction is trivial.

For the converse, given any open set of $$A$$, there exists an open set $$U$$ of $$X$$ such that it can be written as $$U\cap A$$; since $$A$$ is also open, $$U\cap A$$ is open.

</details>

It is not difficult to see that the closed sets in the subspace $$A$$ are precisely the sets of the form $$A\cap C$$ for closed sets $$C$$ of $$X$$. A similar situation can arise for closed sets, and the remedy is likewise simple.

<div class="proposition" markdown="1">

<ins id="lem3">**Lemma 3**</ins> For a subspace $$A$$ of a topological space $$X$$, a necessary and sufficient condition for every closed set of $$A$$ to be closed in $$X$$ is that $$A$$ be a closed set in $$X$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Since $$A$$ is a closed set in $$A$$, one direction is trivial.

For the converse, given any closed set of $$A$$, there exists a closed set $$U$$ of $$X$$ such that it can be written as $$U\cap A$$; since $$A$$ is also closed, $$U\cap A$$ is closed.

</details>

We have defined all topological properties in terms of neighborhoods up to now, and this too can be adjusted just as in the lemmas above.

<div class="proposition" markdown="1">

<ins id="lem4">**Lemma 4**</ins> For a subspace $$A$$ of a topological space $$X$$ and any point $$x\in A$$, a necessary and sufficient condition for every neighborhood of $$x$$ in $$A$$ to be a neighborhood of $$x$$ in $$X$$ is that $$A$$ be a neighborhood of $$x$$ in $$X$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Since $$A$$ is a neighborhood of $$x$$ in $$A$$, one direction is trivial.

For the converse, let $$U$$ be an arbitrary neighborhood of $$x$$ in $$A$$. Then there exists an open neighborhood $$U'$$ of $$x$$ (in $$A$$) contained in $$U$$. On the other hand, if $$A$$ is a neighborhood of $$x$$ in $$X$$, then there exists an open neighborhood $$V$$ of $$x$$ (in $$X$$) contained in $$A$$. Now $$U'\cap V$$ is a nonempty subset, $$U'\cap V\subseteq U$$, and since $$U'\cap V$$ is an open neighborhood of $$x$$ in $$X$$, it follows that $$U$$ is a neighborhood of $$x$$ in $$X$$.

</details>

Using these lemmas, we can restrict the concepts we have examined so far to subspaces.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> Let $$X$$ be a topological space and let $$A\subseteq B\subseteq X$$ be subsets. Then the closure of $$A$$ in $$B$$, denoted $$\cl_BA$$, is equal to

$$\cl_BA=B\cap\cl_XA$$

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

For any $$x\in B$$, a neighborhood of $$x$$ in $$B$$ is always of the form $$V\cap B$$ for some suitable neighborhood $$V$$ of $$x$$ in $$X$$. Now using $$V\cap A=(V\cap B)\cap A$$ and [§Interior, Closure, and Boundary, ⁋Proposition 6](/en/math/topology/other_concepts#prop6), we obtain the desired result.

</details>

Therefore, for $$A\subseteq B\subseteq X$$, the condition that $$A$$ be a dense subset of $$B$$ is equivalent to

$$B=\cl_BA=B\cap\cl_XA$$

and from this in turn we see that it is equivalent to $$B\subseteq\cl_XA$$.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> Let $$X$$ be a topological space and let $$(A_i)_{i\in I}$$ be a collection of subsets of $$X$$, and suppose that one of the following two conditions holds.

1. $$X=\bigcup_{i\in I}\interior(A_i)$$, or
2. $$(A_i)_{i\in I}$$ is a locally finite closed covering of $$X$$.

Then an arbitrary subset $$B$$ of $$X$$ is open (resp. closed) in $$X$$ if and only if $$B\cap A_i$$ is open (resp. closed) in $$A_i$$ for every $$i$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, from the identity

$$X\setminus B\cap A_i=A_i\setminus (B\cap A_i)$$

it suffices to prove the proposition for either open sets or closed sets. Also, if $$B$$ is open in $$X$$ then $$B\cap A_i$$ is open in $$A_i$$ by definition, so the heart of the proposition is the converse.

1. Assume that $$(A_i)$$ satisfies the first condition, and suppose that $$B\cap A_i$$ is open in $$A_i$$. Regarding $$A_i$$ as the whole set and $$\interior A_i$$ as a subspace, we know from this that $$B\cap\interior A_i$$ is open in $$\interior A_i$$. Since $$\interior A_i$$ is an open set, applying [Lemma 2](#lem2) we see that $$B\cap\interior A_i$$ is open in $$X$$. Therefore, from

    $$B=B\cap X=B\cap\left(\bigcup_{i\in I} \interior A_i\right)=\bigcup_{i\in I}(B\cap\interior A_i)$$

    we see that $$B$$ is open.
2. Now suppose that $$(A_i)$$ satisfies the second condition. This time we assume that all the $$B\cap A_i$$ are closed in $$A_i$$. Then by [Lemma 3](#lem3), each $$B\cap A_i$$ is a closed set in $$X$$. Now $$(B\cap A_i)$$ is a collection of locally finite closed sets, and since $$B=\bigcup (B\cap A_i)$$, by [§Interior, Closure, and Boundary, ⁋Proposition 4](/en/math/topology/other_concepts#prop4) we conclude that $$B$$ is closed.

</details>

## Subspaces and Continuous Functions

Let $$X$$ and $$Y$$ be topological spaces and let $$f:X\rightarrow Y$$ be a map. Then for a set $$Y$$ satisfying $$f(X)\subseteq B\subseteq Y$$, the function obtained by restricting the codomain of $$f$$ to $$B$$ is continuous. This is trivial by [Definition 1](#def1) and [§Initial and Final Topology, ⁋Proposition 3](/en/math/topology/initial_and_final_topology#prop3).

Now, in the same situation, suppose a subset $$A$$ of $$X$$ is given. Then the function $$f:X\rightarrow Y$$ restricted to $$A$$, denoted $$f\vert_A$$, equals $$f\circ\iota$$ for the inclusion $$\iota:A\hookrightarrow X$$. Since this is a composition of two continuous functions, we immediately see that $$f\vert_A$$ is also continuous. However, the converse does not hold in general.

<div class="example" markdown="1">

<ins id="ex7">**Example 7**</ins> Let $$f:X\rightarrow Y$$ be a function between two topological spaces that is not continuous. For any $$x\in X$$, if we set $$A=\{x\}$$, then $$f\vert_A$$ is continuous. This is because for any open set $$U$$ of $$Y$$, the preimage $$f^{-1}(U)$$ is always either empty or $$\{x\}$$.

</div>

Instead, if the set $$A$$ is a neighborhood of $$x$$, then the continuity of $$f\vert_A$$ at the point $$x\in X$$ implies that $$f$$ is continuous at $$x$$. This is because by [Lemma 4](#lem4), a neighborhood of $$x$$ in $$A$$ can always be viewed as a neighborhood in $$X$$. To use this argument to show that $$f$$ is continuous at every point, one would have to prove that for each $$x\in X$$ there is a neighborhood $$N(x)$$ such that $$f\vert_{N(x)}$$ is continuous; however, by the following proposition we can prove that $$f$$ is continuous using even weaker information.

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8**</ins> Let $$X$$ be a topological space and let $$(A_i)_{i\in I}$$ be a collection of subsets satisfying one of the conditions of [Proposition 6](#prop6). Then an arbitrary function $$f:X\rightarrow Y$$ into a topological space $$Y$$ is continuous if and only if all the restrictions $$f\vert_{A_i}$$ are continuous.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

It suffices to assume that all the $$f\vert_{A_i}$$ are continuous and show that $$f$$ is continuous. Let $$B$$ be an arbitrary closed set of $$Y$$ and set $$A=f^{-1}(B)$$. Since all the $$f\vert_{A_i}$$ are continuous, $$(f\vert_{A_i})^{-1}(B)=A\cap A_i$$ are all closed sets. Applying [Proposition 6](#prop6), we see that $$A$$ is closed, and therefore $$f$$ is continuous.

</details>
