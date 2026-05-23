---
title: "Compactness and Convergence of Filters"
excerpt: "Characterizing compactness through convergence of filters"

categories: [Math / Topology]
permalink: /en/math/topology/filter_convergence
header:
    overlay_image: /assets/images/Math/Topology/Filter_Convergence.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology-en"

date: 2024-12-11
last_modified_at: 2024-12-11
weight: 15
translated_at: 2026-05-23T06:30:02+00:00
translation_source: kimi-cli
---
We first define the following.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A topological space $$X$$ is *limit point compact* if every infinite subset of $$X$$ has a limit point. ([§Interior, Closure, and Boundary of Sets, ⁋Definition 8](/en/math/topology/other_concepts#def8))

</div>

In general, the following holds.

<div class="proposition" markdown="1">

<ins id="prop22">**Proposition 2**</ins> Every compact space is limit point compact.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Assume for contradiction that $$X$$ is a compact space that is not limit point compact. Then there exists an infinite subset $$A$$ with no limit point, so by the argument after [§Interior, Closure, and Boundary of Sets, ⁋Definition 8](/en/math/topology/other_concepts#def8) we must have $$\cl(A)\setminus A=\emptyset$$. That is, $$A$$ must be closed, and hence compact. Meanwhile, since each $$a\in A$$ is also not a limit point of $$A$$, there exists a suitable open neighborhood $$U_a$$ of $$a$$ such that $$A\cap U_a=\{a\}$$. Then $$(U_a)_{a\in A}$$ is an open cover of $$A$$ with no finite subcover, which is a contradiction.

</details>

However, the converse does not hold in general.

<div class="example" markdown="1">

<ins id="ex3">**Example 3**</ins> Consider a two-point space $$X$$ with the trivial topology and an infinite set $$Y$$ with the discrete topology. Then $$X\times Y$$ is limit point compact but not compact.

</div>

We also define the following.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> A topological space $$X$$ is *sequentially compact* if every sequence in $$X$$ has a convergent subsequence.

</div>

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> Every sequentially compact space is limit point compact.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$X$$ be a sequentially compact space, and assume there exists an infinite subset $$A$$ with no limit point. Then we can choose a suitable countable subset $$A'$$ of $$A$$ and make it into a sequence $$(x_n)_{n\geq k}$$. Since $$X$$ is sequentially compact, this sequence has a convergent subsequence; if this subsequence converges to $$x$$, one can verify that $$x$$ becomes a limit point of $$A'$$ and therefore a limit point of $$A$$.

</details>

## Convergence of Sequences

Meanwhile, the converse of [Proposition 5](#prop5) also does not hold. This may seem somewhat surprising, because given an arbitrary sequence $$(x_n)$$ in a limit point compact space, the set $$A=\{x_n\mid n\geq 1\}$$ is either finite, in which case it trivially has a convergent subsequence, or infinite, in which case it has a limit point. The problem is that there may not exist a subsequence converging to a limit point of $$A$$.

<div class="example" markdown="1">

<ins id="ex6">**Example 6**</ins> Consider the collection of subsets of $$\mathbb{R}$$

$$\mathcal{B}=\{(a,\infty)\mid a\in \mathbb{R}\}$$

This collection satisfies the conditions of [§Bases of Topological Spaces, ⁋Corollary 6](/en/math/topology/topological_bases#cor6) and therefore defines a topology on $$\mathbb{R}$$.

Define a sequence $$(x_n)_{n\geq 1}$$ in this topological space $$\mathbb{R}$$ by the formula

$$x_n=-n$$

Then $$(x_n)$$ has no convergent subsequence. On the other hand, $$A=\{x_n\mid n\geq 1\}$$ has a limit point; for example, $$-2$$ is a limit point of $$A$$. This is because any open set containing $$-2$$ must also contain $$-1\in A$$.

</div>

The above example shows that convergence of sequences is not such a good concept for checking limit points. Meanwhile, by [§Interior, Closure, and Boundary of Sets, ⁋Proposition 6](/en/math/topology/other_concepts#prop6), any limit point of $$A$$ belongs to the closure of $$A$$.

<div class="proposition" markdown="1">

<ins id="lem7">**Lemma 7**</ins> For a topological space $$X$$ and any subset $$A\subseteq X$$, if there exists a sequence in $$A$$ converging to $$x\in X$$, then $$x\in \cl(A)$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Pick an arbitrary open neighborhood $$U$$ of $$x$$. Since there exists a sequence $$(x_n)$$ converging to $$x$$, there exists a suitable $$N\in \mathbb{N}$$ such that $$x_n\in U$$ whenever $$n\geq N$$. Then $$x_N\in U\cap A$$, so $$U\cap A\neq \emptyset$$, and therefore $$x\in \cl(A)$$.

</details>

Therefore, for a topological space $$X$$ and a subset $$A$$, we define the *sequential closure* $$\scl(A)$$ of $$A$$ by

$$\scl(A)=\{x\in X\mid \text{there exists a sequence in $A$ that converges to $x$}\}$$

Then it is obvious that $$\scl(A)\subseteq \cl(A)$$.

<div class="example" markdown="1">

<ins id="ex8">**Example 8**</ins> Consider the uncountable product $$\mathbb{R}^J$$ with the product topology. Define the set $$A$$ by

$$A=\{(x_j)\in \mathbb{R}^J: x_j=1\text{ for all but finitely many $j$}\}$$

Then the origin of $$\mathbb{R}^J$$ belongs to the closure of $$A$$. This is because a basic open set in $$\mathbb{R}^J$$ containing the origin is $$\mathbb{R}$$ in all but finitely many indices, and the point whose coordinates at these finitely many indices are $$0$$ and whose coordinates at the remaining indices are $$1$$ lies in the intersection of this base element and $$A$$. However, no sequence in $$A$$ converges to the origin. This is because, given any sequence in $$A$$, using the fact that $$J$$ is uncountable we can show that there exists $$j\in J$$ such that the $$j$$-th coordinate of every term in the sequence is $$1$$, and then the open neighborhood of the origin whose $$j$$-th coordinate is $$(-1,1)$$ and whose other coordinates are $$\mathbb{R}$$ contains no element of this sequence.

</div>

That is, the converse of [Lemma 7](#lem7) also does not hold in general. Or, using the language above, for a topological space $$X$$ and a subset $$A$$ we have $$\scl(A)\subsetneq \cl(A)$$ in general. If $$\scl(A)=\cl(A)$$ holds for every subset $$A$$, we call $$X$$ a *sequential space*.

Meanwhile, the following proposition, though slightly generalized, is still familiar.

<div class="proposition" markdown="1">

<ins id="prop9">**Proposition 9**</ins> For a continuous function $$f:X \rightarrow Y$$ and any sequence $$(x_n)$$ in $$X$$, if $$(x_n)$$ converges to $$x\in X$$, then $$(f(x_n))$$ converges to $$f(x)$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Pick an arbitrary open neighborhood $$V$$ of $$f(x)$$. Since $$f$$ is continuous, $$f^{-1}(V)$$ is an open neighborhood of $$x$$. Hence there exists a suitable $$N\in \mathbb{N}$$ such that $$x_n\in f^{-1}(V)$$ whenever $$n\geq N$$. Then $$f(x_n)\in V$$, so $$(f(x_n))$$ converges to $$f(x)$$.

</details>

Meanwhile, if the converse of [Lemma 7](#lem7) holds in the space $$X$$, we can also show the converse of [Proposition 9](#prop9) using this result together with the second condition of [§Continuous Functions, ⁋Theorem 4](/en/math/topology/continuous_functions#thm4). That is, if for any sequence $$(x_n)$$ converging to any point $$x$$, $$f(x_n)$$ converges to $$f(x)$$, then $$f$$ is continuous at $$x$$.

Let $$X$$ be a space in which the converse of [Lemma 7](#lem7) holds. Then for any $$x\in \cl(A)$$, we can pick a sequence $$(x_n)$$ in $$X$$ converging to $$x$$. Then the sequence $$f(x_n)$$ in $$Y$$ converges to $$f(x)$$, so by [Lemma 7](#lem7) we have $$f(x)\in \cl(f(A))$$, and we obtain the desired result from [§Continuous Functions, ⁋Theorem 4](/en/math/topology/continuous_functions#thm4).

## Countability Axioms

The above shows that convergence of sequences is not an adequate concept for expressing the notions we have dealt with so far. Looking at the proof of [Proposition 11](#prop11), we can see in what way it is best to generalize this.

<div class="definition" markdown="1">

<ins id="def10">**Definition 10**</ins> We define the following for a topological space $$X$$.

1. $$X$$ is *first countable* if for every point $$x\in X$$, there exists a countable local base at $$x$$.
2. $$X$$ is *second countable* if there exists a countable base for $$X$$.

</div>

<div class="proposition" markdown="1">

<ins id="prop11">**Proposition 11**</ins> If $$X$$ is first countable, $$T_1$$, and limit point compact, then $$X$$ is sequentially compact.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

As mentioned before, given an arbitrary sequence $$(x_n)$$, the set $$A=\{x_n\mid n\geq 1\}$$ is either finite, in which case it trivially has a convergent subsequence, or infinite, in which case it has a limit point $$x$$. If $$x=x_n$$ holds for infinitely many $$n$$, then again for trivial reasons we can extract a subsequence converging to $$x$$; thus we may assume that there are only finitely many $$n$$ satisfying $$x_n=x$$, and since this does not affect the convergence of the sequence, we may assume without loss of generality that $$x_n\neq x$$ for all $$
