---
title: "Hausdorff Spaces"
description: "We define the convergence of sequences in topological spaces and examine the space structure where the uniqueness of limits is guaranteed by the Hausdorff separation axiom."
excerpt: "Convergence of sequences and the Hausdorff axiom"

categories: [Math / Topology]
permalink: /en/math/topology/Hausdorff_spaces
sidebar: 
    nav: "topology-en"

date: 2024-12-03
last_modified_at: 2024-12-03
weight: 13
translated_at: 2026-06-03T07:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-03T07:30:02+00:00
---
Now we define Hausdorff spaces. Before doing so, we first introduce the following.

## Convergence of Sequences

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> For a topological space $$X$$, a function $$\mathbb{N} \rightarrow X$$ is called a *sequence* of points in $$X$$, and is denoted by $$(x_n)_{n\geq 1}$$. We say that a sequence $$(x_n)_{n\geq 1}$$ *converges* to $$x\in X$$ if for every neighborhood $$U$$ of $$x$$, there exists an $$N\in \mathbb{N}$$ such that

$$n\geq N\implies x_n\in U$$

holds.

</div>

This differs from the usual $$\epsilon$$-$$N$$ definition of convergence in calculus only in that an open set $$U$$ is used in place of an $$\epsilon$$-ball to represent points close to $$x$$. Naturally, if a sequence $$(x_n)$$ converges to $$x$$, one would like to write $$\lim_{n \rightarrow\infty}x_n$$, but the following example shows that this notation need not even be well-defined.

<div class="example" markdown="1">

<ins id="ex2">**Example 2**</ins> Let $$X$$ be any set endowed with the trivial topology, considered as a topological space. Then any sequence in $$X$$ converges to every point of $$X$$.

</div>

## Separation Axioms

The reason phenomena like [Example 2](#ex2) occur is, intuitively, that the topology on $$X$$ is not strong enough to separate the points of $$X$$. We may define various *separation axioms* according to the degree to which points are separated in a topological space, and classify spaces satisfying each of them. To this end, let us fix some terminology.

- Two points $$x,y$$ of a topological space $$X$$ are distinct if $$x\neq y$$. 
- Two points $$x,y$$ of a topological space $$X$$ are *topologically distinguishable* if $$\mathcal{N}(x)\neq \mathcal{N}(y)$$.[^1] ([§Open Sets, §§Neighborhood filter](/en/math/topology/open_sets#neighborhood-filter))
- Two subsets $$A,B$$ of a topological space $$X$$ are *separated* if each has a neighborhood not containing the other.
- Two subsets $$A,B$$ of a topological space $$X$$ are *separated by neighborhoods* if they have disjoint neighborhoods.
- Two subsets $$A,B$$ of a topological space $$X$$ are *separated by closed neighborhoods* if they have disjoint closed neighborhoods.
- Two subsets $$A,B$$ of a topological space $$X$$ are *separated by continuous functions* if there exists a continuous function $$f:X \rightarrow \mathbb{R}$$ such that $$A\subseteq f^{-1}(\{0\})$$ and $$B\subseteq f^{-1}(\{1\})$$. 
- Two subsets $$A,B$$ of a topological space $$X$$ are *precisely separated by continuous functions* if there exists a continuous function $$f:X \rightarrow \mathbb{R}$$ such that $$A= f^{-1}(\{0\})$$ and $$B= f^{-1}(\{1\})$$. 

The conditions above are listed in order of increasing strength. That is, two subsets precisely separated by continuous functions are separated by continuous functions; two subsets separated by continuous functions are separated by closed neighborhoods; two subsets separated by closed neighborhoods are separated by neighborhoods; two subsets separated by neighborhoods are separated; two separated points are topologically distinguishable; and all topologically distinguishable points are distinct.

Now we define the following.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> For a topological space $$X$$, we define the following.

1. $$X$$ is a *$$T_0$$-space*, or a *Kolmogorov space*, if any two distinct points are topologically distinguishable.
2. $$X$$ is an *$$R_0$$-space* if any two topologically distinguishable points are separated.
3. $$X$$ is a *$$T_1$$-space*, or a *Fréchet space*, if any two distinct points are separated. Thus, $$X$$ is $$T_1$$ if and only if $$X$$ is $$T_0$$ and $$R_0$$.
4. $$X$$ is an *$$R_1$$-space* if any two topologically distinguishable points are separated by neighborhoods. Hence every $$R_1$$-space is an $$R_0$$-space.
5. $$X$$ is a *$$T_2$$-space*, or a *Hausdorff space*, if any two distinct points are separated by neighborhoods. Thus, $$X$$ is $$T_2$$ if and only if $$X$$ is $$T_0$$ and $$R_1$$, and every $$T_2$$-space is $$T_1$$. 
6. $$X$$ is a *$$T_{2\frac{1}{2}}$$-space*, or a *Urysohn space*, if any two topologically distinguishable points are separated by closed neighborhoods. Hence every $$T_{2\frac{1}{2}}$$-space is $$T_2$$. 
7. $$X$$ is a *completely $$T_2$$-space*, or a *completely Hausdorff space*, if any two distinct points are separated by continuous functions.
8. $$X$$ is a *regular space* if any point $$x\in X$$ and any closed set $$A\subseteq X$$ not containing $$x$$ are always separated by neighborhoods.
9. $$X$$ is a *$$T_3$$-space*, or a *regular Hausdorff space*, if $$X$$ is $$T_0$$ and regular. Every $$T_3$$-space is $$T_{2\frac{1}{2}}$$. 
10. $$X$$ is a *completely regular space* if any point $$x\in X$$ and any closed set $$A\subseteq X$$ not containing $$x$$ are always separated by continuous functions.
11. $$X$$ is a *completely $$T_3$$-space*, or a *Tychonoff space*, if $$X$$ is $$T_0$$ and completely regular. Thus if $$X$$ is completely $$T_3$$, then it is completely Hausdorff and regular Hausdorff; it is therefore also called a *completely regular Hausdorff space*.
12. $$X$$ is a *normal space* if any two disjoint closed subsets are separated by neighborhoods. 
13. $$X$$ is a *normal regular space* if $$X$$ is normal and $$R_0$$. Thus if $$X$$ is normal regular, then $$X$$ is completely regular. 
14. $$X$$ is a *$$T_4$$-space*, or a *normal Hausdorff space*, if $$X$$ is $$T_1$$ and normal. Every $$T_1$$-space is $$R_0$$, so every $$T_4$$-space is normal regular, and hence completely regular. Moreover, every $$T_1$$-space is a $$T_0$$-space, so every $$T_4$$-space is completely $$T_3$$.
15. $$X$$ is a *completely normal space* if any two separated subsets are separated by neighborhoods. Then every completely normal space is normal.
16. $$X$$ is a *completely $$T_4$$-space* if $$X$$ is completely normal and $$T_1$$. Hence every completely $$T_4$$-space is $$T_4$$.
17. $$X$$ is a *perfectly normal space* if any two disjoint closed subsets are precisely separated by continuous functions.
18. $$X$$ is a *perfectly $$T_4$$-space* if $$X$$ is perfectly normal and $$T_0$$. 

</div>

## Hausdorff Spaces

One of the notions of particular importance in [Definition 3](#def3) is that of a Hausdorff space. Here our intuition is well-founded.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> In a Hausdorff space $$X$$, any sequence $$(x_n)$$ converges to at most one point.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Suppose for contradiction that $$(x_n)$$ converges to two distinct points $$x,y$$. Then we can choose disjoint open neighborhoods $$U,V$$ of $$x$$ and $$y$$, respectively. From the assumption that $$(x_n)$$ converges to both $$x$$ and $$y$$, there exist $$M,N$$ such that

$$m\geq M \implies x_m\in U,\qquad n\geq N\implies x_n\in V$$

so letting $$K=\max(M,N)$$, the term $$x_K$$ must belong to both $$U$$ and $$V$$, a contradiction.

</details>

Meanwhile, the following lemma is also useful for showing that $$X$$ is Hausdorff.

<div class="proposition" markdown="1">

<ins id="lem5">**Lemma 5**</ins> A topological space $$X$$ is Hausdorff if and only if the subset

$$\Delta_X=\{(x,x)\mid x\in X\}$$

of $$X\times X$$ is closed.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, assume $$X$$ is Hausdorff. Then for any $$(x,y)\not\in\Delta_X$$, we have $$x\neq y$$, so we can choose disjoint neighborhoods $$U,V$$ of $$x$$ and $$y$$. Then $$U\times V$$ is an open set containing $$(x,y)$$ and disjoint from $$\Delta_X$$.

Conversely, if $$\Delta_X$$ is a closed subset of $$X\times X$$, then for any $$x,y\in X$$ with $$x\neq y$$, we have $$(x,y)\not\in\Delta_X$$, so there exists an open neighborhood of $$(x,y)$$ disjoint from $$\Delta_X$$, and by considering the base for the product topology, there is a basic open set of the form $$U\times V$$ contained in it.

</details>

More generally, by the same argument one can show that $$X$$ is Hausdorff if and only if, for any index set $$I$$, the diagonal

$$\Delta_X=\{(x_i)_{i\in I}:\text{$x_i=x$ for all $i$, where $x\in X$}\}$$

in $$X^I=\prod_{i\in I}X$$ is closed. From [Lemma 5](#lem5) we obtain the following.

<div class="proposition" markdown="1">

<ins id="cor6">**Corollary 6**</ins> For continuous functions $$f,g:X \rightarrow Y$$, if $$Y$$ is Hausdorff then the set

$$E=\{x\in X\mid f(x)=g(x)\}$$

is a closed subset of $$X$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Consider the continuous function $$x\mapsto (f(x), g(x))$$ from $$X$$ to $$Y\times Y$$; the given set is the preimage of the closed set $$\Delta_Y$$ under this map.

</details>

<div class="proposition" markdown="1">

<ins id="cor7">**Corollary 7**</ins> For a continuous function $$f:X \rightarrow Y$$, if $$Y$$ is Hausdorff then the set

$$\Gamma(f)=\{(x,f(x))\mid x\in X\}$$

is a closed subset of $$X\times Y$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Apply [Corollary 6](#cor6) to the two continuous functions

$$(x,y)\mapsto f(x),\quad (x,y)\mapsto y$$

from $$X\times Y$$ to $$Y$$.

</details>

## Subspaces and Products of Hausdorff Spaces

For any Hausdorff space $$X$$, it is easy to verify that any subspace $$A$$ of $$X$$ is also Hausdorff. Indeed, given any $$x,y\in A$$, if we choose disjoint open neighborhoods $$U,V$$ of them in $$X$$, then $$U\cap A$$ and $$V\cap A$$ are disjoint open neighborhoods of $$x,y$$ in $$A$$. On the other hand, the product of Hausdorff spaces is also Hausdorff.

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8**</ins> For nonempty spaces $$X_i$$, the product $$X=\prod_{i\in I}X_i$$ is Hausdorff if and only if each $$X_i$$ is Hausdorff.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, suppose the $$X_i$$ are Hausdorff and let $$x,y\in X$$ be given. Then there exists an index $$i$$ such that $$x_i\neq y_i$$, and in this $$X_i$$ we choose open neighborhoods $$U,V$$ separating $$x_i$$ and $$y_i$$. Considering the base for $$X=\prod X_i$$, the sets whose $$i$$th factor is $$U$$ or $$V$$ and whose remaining $$j$$th factors are $$X_j$$ separate $$x$$ and $$y$$.

Conversely, if $$X$$ is Hausdorff, then for arbitrarily chosen elements $$x_j\in X_j$$, the set

$$\prod_{j\in I} A_j,\qquad A_j=\begin{cases}A_i&i=j\\\{x_j\}&\text{otherwise}\end{cases}$$

is a subset of $$X$$ homeomorphic to $$X_i$$.

</details>

## Quotient Spaces of Hausdorff Spaces

In general, the quotient space $$X/R$$ of a Hausdorff space $$X$$ need not be Hausdorff. Moreover, a necessary and sufficient condition for $$X/R$$ to be Hausdorff is not hard to obtain: since open sets in $$X/R$$ correspond bijectively to $$R$$-saturated open sets in $$X$$, the quotient $$X/R$$ is Hausdorff if and only if for any $$x,y\in X$$ belonging to different equivalence classes, there exists an $$R$$-saturated open set separating them. In particular, the following holds.

<div class="proposition" markdown="1">

<ins id="prop9">**Proposition 9**</ins> For a continuous function $$f:X \rightarrow Y$$, if $$Y$$ is Hausdorff then the quotient space $$X/{\sim}$$ with respect to the equivalence relation

$$x\sim y\iff f(x)=f(y)$$

is Hausdorff.

</div>



[^1]: This is equivalent to saying that the collections of open sets containing $$x$$ and $$y$$ are not the same.
