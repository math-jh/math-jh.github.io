---
title: "Compactness and Convergence of Filters"
description: "This post covers the definitions of limit point compactness, compactness, and sequential compactness in topological spaces, and explains the inclusion relationships among them."
excerpt: "Characterizing compactness via filter convergence"

categories: [Math / Topology]
permalink: /en/math/topology/filter_convergence
sidebar: 
    nav: "topology-en"

date: 2024-12-11
weight: 15
translated_at: 2026-06-27T01:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-27T01:30:02+00:00
---
We first define the following.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A topological space $$X$$ is called *limit point compact* if every infinite subset of $$X$$ has a limit point. ([§Interior, Closure, Boundary of Sets, ⁋Definition 8](/en/math/topology/other_concepts#def8))

</div>

In general, the following holds.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> Every compact space is limit point compact.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Suppose, for the sake of contradiction, that $$X$$ is a compact space that is not limit point compact. Then there exists an infinite subset $$A$$ having no limit point, and therefore by the argument after [§Interior, Closure, Boundary of Sets, ⁋Definition 8](/en/math/topology/other_concepts#def8) we must have $$\cl(A)\setminus A=\emptyset$$. That is, $$A$$ must be closed, and hence compact. On the other hand, since each $$a\in A$$ is also not a limit point of $$A$$, there exists a suitable open neighborhood $$U_a$$ of $$a$$ such that $$A\cap U_a=\{a\}$$. Then $$(U_a)_{a\in A}$$ is an open cover of $$A$$ with no finite subcover, which is a contradiction.

</details>

However, the converse does not hold in general.

<div class="example" markdown="1">

<ins id="ex3">**Example 3**</ins> Consider a two-point space $$X$$ with the trivial topology, and an infinite set $$Y$$ with the discrete topology. Then $$X\times Y$$ is limit point compact but not compact.

</div>

We also define the following.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> A topological space $$X$$ is called *sequentially compact* if every sequence of points in $$X$$ has a convergent subsequence.

</div>

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> Every sequentially compact space is limit point compact.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$X$$ be a sequentially compact space, and suppose there exists an infinite subset $$A$$ having no limit point. Then we can choose a suitable countable subset $$A'$$ of $$A$$ and regard it as a sequence $$(x_n)_{n\geq k}$$. Since $$X$$ is sequentially compact, this sequence has a convergent subsequence; if this subsequence converges to $$x$$, then one can verify that $$x$$ is a limit point of $$A'$$, and hence of $$A$$.

</details>

## Convergence of Sequences

Meanwhile, the converse of [Proposition 5](#prop5) also fails. This may seem somewhat surprising, because if an arbitrary sequence $$(x_n)$$ in a limit point compact space is given, the set $$A=\{x_n\mid n\geq 1\}$$ is either finite, in which case it trivially has a convergent subsequence, or infinite, in which case it has a limit point. The problem is that there may not exist a subsequence converging to a limit point of the set $$A$$.

<div class="example" markdown="1">

<ins id="ex6">**Example 6**</ins> Consider the collection of subsets of $$\mathbb{R}$$

$$\mathcal{B}=\{(a,\infty)\mid a\in \mathbb{R}\}$$

This collection satisfies the conditions of [§Topological Bases, ⁋Corollary 6](/en/math/topology/topological_bases#cor6), and thus defines a topology on $$\mathbb{R}$$.

For the topological space $$\mathbb{R}$$ defined in this way, define a sequence $$(x_n)_{n\geq 1}$$ by the formula

$$x_n=-n$$

Then $$(x_n)$$ has no convergent subsequence. On the other hand, the set $$A=\{x_n\mid n\geq 1\}$$ does have a limit point; for instance, $$-2$$ is a limit point of $$A$$, because any open set containing $$-2$$ must also contain $$-1\in A$$.

</div>

The above example shows that convergence of sequences is not a very good notion for detecting limit points. On the other hand, by [§Interior, Closure, Boundary of Sets, ⁋Proposition 6](/en/math/topology/other_concepts#prop6), any limit point of a set $$A$$ belongs to the closure of $$A$$.

<div class="proposition" markdown="1">

<ins id="lem7">**Lemma 7**</ins> Let $$X$$ be a topological space and $$A\subseteq X$$ an arbitrary subset. If there exists a sequence in $$A$$ converging to $$x\in X$$, then $$x\in \cl(A)$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Choose an arbitrary open neighborhood $$U$$ of $$x$$. Since there exists a sequence $$(x_n)$$ converging to $$x$$, there exists a suitable $$N\in \mathbb{N}$$ such that $$x_n\in U$$ for all $$n\geq N$$. Then $$x_N\in U\cap A$$, so $$U\cap A\neq \emptyset$$, and therefore $$x\in \cl(A)$$.

</details>

Therefore, for a topological space $$X$$ and a subset $$A$$, if we define the *sequential closure* $$\scl(A)$$ of $$A$$ by

$$\scl(A)=\{x\in X\mid \text{there exists a sequence in $A$ that converges to $x$}\}$$

then it is clear that $$\scl(A)\subseteq \cl(A)$$.

<div class="example" markdown="1">

<ins id="ex8">**Example 8**</ins> Consider the uncountable product $$\mathbb{R}^J$$ of copies of $$\mathbb{R}$$, equipped with the product topology. Define the set $$A$$ by

$$A=\{(x_j)\in \mathbb{R}^J: x_j=1\text{ for all but finitely many $j$}\}$$

Then the origin of $$\mathbb{R}^J$$ belongs to the closure of $$A$$. This is because any basic open set containing the origin has all but finitely many coordinates equal to $$\mathbb{R}$$, and by setting those finitely many coordinates to $$0$$ and the remaining coordinates to $$1$$, we obtain a point lying in the intersection of this basic open set with $$A$$. However, no sequence in $$A$$ converges to the origin. Indeed, given any sequence in $$A$$, since $$J$$ is uncountable one can show that there exists $$j\in J$$ such that the $$j$$th coordinate of every term of the sequence is $$1$$; then the open neighborhood of the origin whose $$j$$th coordinate is $$(-1,1)$$ and whose remaining coordinates are $$\mathbb{R}$$ contains no term of the sequence.

</div>

That is, the converse of [Lemma 7](#lem7) also fails in general. Or, using the language above, for a topological space $$X$$ and a subset $$A$$ we have $$\scl(A)\subsetneq \cl(A)$$ in general. If $$\scl(A)=\cl(A)$$ holds for every subset $$A$$, then $$X$$ is called a *sequential space*.

Meanwhile, the following proposition, although slightly generalized, is still familiar.

<div class="proposition" markdown="1">

<ins id="prop9">**Proposition 9**</ins> Let $$f:X \rightarrow Y$$ be a continuous function and $$(x_n)$$ an arbitrary sequence in $$X$$. If $$(x_n)$$ converges to $$x\in X$$, then $$(f(x_n))$$ converges to $$f(x)$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Choose an arbitrary open neighborhood $$V$$ of $$f(x)$$. Since $$f$$ is continuous, $$f^{-1}(V)$$ is an open neighborhood of $$x$$. Hence there exists a suitable $$N\in \mathbb{N}$$ such that $$x_n\in f^{-1}(V)$$ for all $$n\geq N$$. Then $$f(x_n)\in V$$, so $$(f(x_n))$$ converges to $$f(x)$$.

</details>

On the other hand, if the converse of [Lemma 7](#lem7) holds in the space $$X$$, then using that result together with the second condition of [§Continuous Functions, ⁋Theorem 4](/en/math/topology/continuous_functions#thm4), we can also prove the converse of [Proposition 9](#prop9). That is, if for every sequence $$(x_n)$$ converging to any $$x\in A$$, the sequence $$f(x_n)$$ converges to $$f(x)$$, then $$f$$ is continuous at the point $$x$$.

Suppose $$X$$ is a space in which the converse of [Lemma 7](#lem7) holds. Then for any $$x\in \cl(A)$$ we can choose a sequence $$(x_n)$$ in $$X$$ converging to $$x$$. Since the sequence $$f(x_n)$$ in $$Y$$ converges to $$f(x)$$, by [Lemma 7](#lem7) we have $$f(x)\in \cl(f(A))$$, and the desired result follows from [§Continuous Functions, ⁋Theorem 4](/en/math/topology/continuous_functions#thm4).

## Countability Axioms

The above contents show that convergence of sequences is not an appropriate notion for expressing the concepts we have dealt with so far. Looking at the proof of [Proposition 11](#prop11), one can see in what direction it is good to generalize this.

<div class="definition" markdown="1">

<ins id="def10">**Definition 10**</ins> For a topological space $$X$$, we define the following.

1. $$X$$ is called *first countable* if for every point $$x\in X$$ there exists a countable local base at $$x$$.
2. $$X$$ is called *second countable* if there exists a countable base for $$X$$.

</div>

<div class="proposition" markdown="1">

<ins id="prop11">**Proposition 11**</ins> If $$X$$ is first countable and $$T_1$$, and limit point compact, then $$X$$ is sequentially compact.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

As mentioned before, given an arbitrary sequence $$(x_n)$$, the set $$A=\{x_n\mid n\geq 1\}$$ is either finite, in which case it trivially has a convergent subsequence, or infinite, in which case it has a limit point $$x$$. If $$x=x_n$$ holds for infinitely many $$n$$, then again for trivial reasons we can extract a subsequence converging to $$x$$; thus we may assume that there are only finitely many $$n$$ satisfying $$x_n=x$$, and since this does not affect convergence of the sequence we may assume without loss of generality that $$x_n\neq x$$ for all $$n$$.

Since $$X$$ is first countable, we can consider a countable local base $$\mathcal{B}(x)$$ at $$x$$. Writing the elements of $$\mathcal{B}(x)$$ as $$B_1,B_2,\ldots$$, we may replace $$B_n$$ by $$B_1\cap\cdots\cap B_n$$ so that $$B_{n+1}\subseteq B_n$$ holds for all $$n$$.

Now $$B_1$$ is an open set containing $$x$$, and since $$x$$ is a limit point of $$A$$, there exists a suitable $$n_1$$ such that $$x_{n_1}\in B_1$$. Since $$X$$ is $$T_1$$, there exists an open set $$U_2$$ containing $$x$$ but not containing $$x_1,\ldots,x_{n_1}$$. Then $$U_2\cap B_2$$ is again an open set containing $$x$$, and since $$x$$ is a limit point of $$A$$, there exists a suitable $$n_2$$ such that $$x_{n_2}\in U_2\cap B_2$$. Repeating this process, we can extract a subsequence of $$A$$ converging to $$x$$.

</details>

Moreover, one can easily show that every first countable space is a sequential space.

<div class="proposition" markdown="1">

<ins id="prop12">**Proposition 12**</ins> Every second countable space $$X$$ is *Lindelöf*. That is, every open cover of $$X$$ has a countable subcover.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Fix a countable base $$\mathcal{B}=\{B_1, B_2, \ldots\}$$ of $$X$$, and let $$(U_\alpha)_{\alpha\in A}$$ be an arbitrary open cover of $$X$$. For each point $$x\in X$$ there exists $$\alpha$$ with $$x\in U_\alpha$$, and by the definition of a base there exists $$B_n\in\mathcal{B}$$ such that $$x\in B_n\subseteq U_\alpha$$. Collecting all such $$B_n$$'s, we obtain a countable subcollection $$\{B_{n_1}, B_{n_2}, \ldots\}$$ of $$\mathcal{B}$$ covering $$X$$. Now for each $$k$$ choose one $$\alpha_k$$ with $$B_{n_k}\subseteq U_{\alpha_k}$$; then $$(U_{\alpha_k})_{k\geq 1}$$ is a countable subcover of $$(U_\alpha)_{\alpha\in A}$$.

</details>

## Convergence of Filters

What played the essential role in the proof of [Proposition 11](#prop11) was that $$x$$ possesses a decreasing sequence of open sets

$$B_1\supseteq B_2\supseteq\cdots$$

and by first countability, for any given open set $$U$$, one can arrange that $$B_n\subseteq U$$ for all sufficiently large $$n$$. That is, in a certain sense, the above open sets themselves can be regarded as converging to $$x$$. Based on this observation, we define the following.

<div class="definition" markdown="1">

<ins id="def13">**Definition 13**</ins> Consider a topological space $$X$$ and a filter $$\mathcal{F}$$ defined on it. ([§Equivalent Definitions of Topological Spaces, ⁋Definition 3](/en/math/topology/equivalent_formulations_of_topology#def3)) Then $$\mathcal{F}$$ is said to *converge* to $$x\in X$$ if $$\mathcal{N}(x)\subseteq \mathcal{F}$$ holds. ([§Open Sets, §§Neighborhood filter](/en/math/topology/open_sets#neighborhood-filter)) In this case, $$x$$ is called a *limit point* of $$\mathcal{F}$$.

</div>

[Definition 13](#def13) generalizes the convergence of sequences. To verify this, we first need to define the following.

<div class="definition" markdown="1">

<ins id="def14">**Definition 14**</ins> Let a filter $$\mathcal{F}$$ be defined on a set $$X$$, and let $$X$$ be a topological space. For a function $$f:X \rightarrow Y$$, we say that $$y\in Y$$ is a *limit point* of $$f$$ with respect to $$\mathcal{F}$$ if $$y$$ is a limit point of the filter $${\uparrow}f(\mathcal{F})$$. ([§Equivalent Definitions of Topological Spaces, ⁋Proposition 7](/en/math/topology/equivalent_formulations_of_topology#prop7))

</div>

Then by definition, $$y\in Y$$ being a limit point of $$f$$ with respect to $$\mathcal{F}$$ means that for every neighborhood $$V$$ of $$y$$, there exists $$F\in \mathcal{F}$$ such that $$f(F)\subseteq V$$. In particular, the following holds.

<div class="proposition" markdown="1">

<ins id="prop15">**Proposition 15**</ins> For a sequence $$(x_n)_{n\geq 1}$$ in a topological space $$X$$, the sequence $$(x_n)_{n\geq 1}$$ converging to $$x\in X$$ is equivalent to the filter generated by the image of the Fréchet filter $$\mathcal{F}$$ on $$\mathbb{N}$$ under the map $$n\mapsto x_n$$ converging to $$x$$. ([§Equivalent Definitions of Topological Spaces, ⁋Example 4](/en/math/topology/equivalent_formulations_of_topology#ex4))

</div>

Thus we see that convergence of filters generalizes convergence of sequences. Moreover, through this notion we can prove the following proposition.

<div class="proposition" markdown="1">

<ins id="prop16">**Proposition 16**</ins> For a topological space $$X$$ and an arbitrary subset $$A\subseteq X$$, the following are equivalent: $$x\in\cl(A)$$, and there exists a filter $$\mathcal{F}$$ on $$A$$ converging to $$x$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, suppose there exists a filter $$\mathcal{F}$$ on $$A$$ converging to $$x$$. That is, $$\mathcal{F}$$ contains the element $$A$$ and the collection of subsets $$\mathcal{N}(x)$$. Hence by the definition of a filter, for every neighborhood $$U\in \mathcal{N}(x)$$ we have $$U\cap A\neq\emptyset$$.

Conversely, suppose $$x\in \cl(A)$$. Then for every neighborhood $$U$$ of $$x$$ we have $$U\cap A\neq\emptyset$$, so the following expression

$$\mathcal{N}(x)\vert_A=\{U\cap A\mid U\in \mathcal{N}(x)\}$$

defines a filter base. Now letting $$\mathcal{F}$$ be the filter defined by $$\mathcal{N}(x)\vert_A$$, we obtain the desired result.

</details>

Therefore, by the argument after [Lemma 7](#lem7), the following proposition is also obvious.

<div class="proposition" markdown="1">

<ins id="prop17">**Proposition 17**</ins> For a function $$f:X \rightarrow Y$$ between topological spaces, $$f$$ is continuous at $$x\in X$$ if and only if for every filter $$\mathcal{F}$$ converging to $$x$$, the filter defined by the filter base $$f(\mathcal{F})$$ converges to $$f(x)$$.

</div>
