---
title: "Connected Spaces"
description: "This post covers the definition and properties of connected spaces in topology. It proves that connectedness is preserved under continuous functions and that the union of intersecting connected sets is also connected."
excerpt: "Connected spaces, path-connectedness, and connected components"

categories: [Math / Topology]
permalink: /en/math/topology/connected_spaces
sidebar: 
    nav: "topology-en"

date: 2024-12-15
last_modified_at: 2025-02-08
weight: 18
translated_at: 2026-06-03T09:00:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-03T09:00:02+00:00
---
We now examine connectedness, one of the fundamental concepts in topology.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A topological space $$X$$ is called a *connected space* if it cannot be written as the union of two disjoint nonempty open sets. More generally, a subset $$A$$ of $$X$$ is connected if $$A$$ with the subspace topology is connected.

</div>

In other words, a topological space is disconnected if and only if

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> For a connected set $$A\subseteq X$$, any set $$B$$ satisfying $$A\subseteq B \subseteq \cl(A)$$ is connected.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

In the given situation,

$$\cl_B(A)=B\cap \cl_X(A)=B$$

so $$A$$ is a dense subset of $$B$$. ([§Subspaces, ⁋Proposition 4](/en/math/topology/subspaces#prop4)) Now, toward a contradiction, suppose there exist two disjoint open sets $$U,V$$ in $$B$$ with $$U\cup V=B$$. Since $$A$$ is dense in $$B$$, both $$U\cap A$$ and $$V\cap A$$ are nonempty and $$U\cap V\cap A=\emptyset$$. This contradicts the assumption that $$A$$ is connected.

</details>

The following proposition is also intuitively plausible.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> For a family $$(A_i)$$ of connected sets, if $$A_i\cap A_j\neq\emptyset$$ for all $$i,j$$, then $$A=\bigcup A_i$$ is also connected.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Toward a contradiction, assume there exist two open sets $$U,V$$ such that

$$A=(U\cap A)\cup (V\cap A),\qquad U\cap V\cap A=\emptyset$$

First, for each $$i$$, since $$A_i$$ is connected, exactly one of the two inclusions $$A_i\subseteq U$$ or $$A_i\subseteq V$$ must hold. On the other hand, if $$A_i\subseteq U$$ and $$A_j\subseteq V$$, then

$$A_i\cap A_j\subseteq (U\cap A)\cap (V\cap A)=U\cap V\cap A=\emptyset$$

which is a contradiction; thus all the $$A_i$$ must be contained in $$U$$, or all must be contained in $$V$$. Hence either $$U\cap A=\emptyset$$ or $$V\cap A=\emptyset$$.

</details>

## Properties of Connected Sets

Connectedness is preserved by continuous functions.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> For any continuous function $$f:X \rightarrow Y$$ and any connected subset $$A\subseteq X$$, the image $$f(A)$$ is also connected.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Suppose toward a contradiction that $$f(A)$$ is not connected, and choose open sets $$V_1,V_2$$ in $$Y$$ such that

$$f(A)=(V_1\cap f(A))\cup (V_2\cap f(A)), \qquad V_1\cap V_2\cap f(A)=\emptyset$$

Then $$f^{-1}(V_1)$$ and $$f^{-1}(V_2)$$ are open in $$X$$, and

$$A=(A\cap f^{-1}(V_1))\cup (A\cap f^{-1}(V_2)),\qquad f^{-1}(V_1)\cap f^{-1}(V_2)\cap A=\emptyset$$

From the assumption that $$A$$ is connected, we know that either $$V_1\cap f(A)=\emptyset$$ or $$V_2\cap f(A)=\emptyset$$.

</details>

From this the following corollary is immediate.

<div class="proposition" markdown="1">

<ins id="cor5">**Corollary 5**</ins> The quotient space of a connected space is connected.

</div>

Also, the following holds.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> The product of connected spaces is connected. Conversely, if a product is connected then each factor is connected.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

The reverse direction follows immediately from [Proposition 4](#prop4) applied to the projections $$\pr_i$$, so there is nothing to prove.

Thus, assuming each $$X_i$$ is connected, suppose toward a contradiction that $$X=\prod X_i$$ is not connected. If $$X=U\cup V$$ with $$U\cap V=\emptyset$$ and $$U,V\neq\emptyset$$, then the function $$f:X \rightarrow \{0,1\}$$ defined by

$$f(x)=\begin{cases}1&\text{if $x\in U$}\\0&\text{if $x\in V$}\end{cases}$$

is continuous. (Here $$\{0,1\}$$ is given the discrete topology.)

Now fix an element $$a=(a_i)\in X$$, and define $$\iota_i: X_i \rightarrow X$$ to be the map whose $$i$$th coordinate is $$x$$ and whose remaining coordinates are taken from $$a$$. Then $$f\circ\iota_i$$ is a continuous function from $$X_i$$ to $$\{0,1\}$$, and since $$X_i$$ is connected we know that $$f\circ\iota_i$$ must be constant. Thus, by induction, points $$x$$ in $$X$$ all of whose coordinates except finitely many are equal to $$a$$ must satisfy $$f(x)=f(a)$$. Since such points form a dense subset of $$X$$, $$f$$ must be constant on all of $$X$$, which is a contradiction.

</details>

## Connected Components

Meanwhile, for a fixed $$x\in X$$, the collection of connected sets containing $$x$$ satisfies the hypothesis of [Proposition 3](#prop3), so the largest connected set containing $$x$$ is well defined.

<div class="definition" markdown="1">

<ins id="def7">**Definition 7**</ins> The *connected component* containing a point $$x\in X$$ is the largest connected subset of $$X$$ containing $$x$$. If the connected component containing every point $$x\in X$$ is always $$\{x\}$$ itself, then $$X$$ is called *totally disconnected*.

</div>

By definition, if $$X$$ is connected then $$X$$ has a unique connected component. More generally, any $$X$$ can be written as a union of connected components

$$X=\bigcup_{i\in I} U_i$$

Meanwhile, by [Proposition 2](#prop2) each $$U_i$$ must be closed. If $$I$$ is finite, we know that the $$U_i$$ must be simultaneously open and closed. Of course this does not apply to infinitely many connected components, but any clopen set in an arbitrary topological space must be a union of connected components. For if not, and some connected component $$C$$ met a clopen set $$A$$ while also meeting its complement, then $$C\cap A$$ and $$C\setminus A$$ would be two open sets partitioning $$C$$.

Moreover, the following holds.

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8**</ins> Define an equivalence relation $$\sim$$ on a topological space $$X$$ by

$$x\sim y\iff \text{$x$ and $y$ lie in the same component}$$

Then $$X/{\sim}$$ is totally disconnected.

</div>

The proof of this is immediate.

## Locally Connected Spaces

<div class="definition" markdown="1">

<ins id="def9">**Definition 9**</ins> A topological space $$X$$ is *locally connected* at a point $$x\in X$$ if, whenever a neighborhood $$U$$ of $$x$$ is given, there exists a connected neighborhood of $$x$$ contained in $$U$$. A space that is locally connected at every point is simply called a locally connected space.

</div>

Then the following holds.

<div class="proposition" markdown="1">

<ins id="prop10">**Proposition 10**</ins> $$X$$ is locally connected if and only if every component of every open set in $$X$$ is open.

</div>

## Path-Connected Spaces

Meanwhile, we
