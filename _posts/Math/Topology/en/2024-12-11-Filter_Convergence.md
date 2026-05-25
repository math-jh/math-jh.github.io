---
title: "Compactness and Filter Convergence"
excerpt: "A characterization of compactness through filter convergence"

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
translated_at: 2026-05-25T07:00:01+00:00
translation_source: kimi-cli
---
We first define the following.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A topological space $$X$$ is called *limit point compact* if every infinite subset of $$X$$ has a limit point. ([§Interior, Closure, and Boundary of Sets, ⁋Definition 8](/en/math/topology/other_concepts#def8))

</div>

In general, the following holds.

<div class="proposition" markdown="1">

<ins id="prop22">**Proposition 2**</ins> Every compact space is limit point compact.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Suppose for contradiction that $$X$$ is a compact space that is not limit point compact. Then there exists an infinite subset $$A$$ with no limit point, and thus by the argument following [§Interior, Closure, and Boundary of Sets, ⁋Definition 8](/en/math/topology/other_concepts#def8), we must have $$\cl(A)\setminus A=\emptyset$$. That is, $$A$$ is closed and therefore compact. On the other hand, since each $$a\in A$$ is not a limit point of $$A$$, there exists an open neighborhood $$U_a$$ of $$a$$ such that $$A\cap U_a=\{a\}$$. Then $$(U_a)_{a\in A}$$ is an open cover of $$A$$ with no finite subcover, which is a contradiction.

</details>

However, the converse does not hold in general.

<div class="example" markdown="1">

<ins id="ex3">**Example 3**</ins> Consider the two-point space $$X$$ with the trivial topology and an infinite set $$Y$$ with the discrete topology. Then $$X\times Y$$ is limit point compact but not compact.

</div>

We also define the following.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> A topological space $$X$$ is called *sequentially compact* if every sequence in $$X$$ has a convergent subsequence.

</div>

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> Every sequentially compact space is limit point compact.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$X$$ be a sequentially compact space, and suppose there exists an infinite subset $$A$$ with no limit point. Then we can choose a suitable countable subset $$A'$$ of $$A$$ and enumerate it as a sequence $$(x_n)_{n\geq k}$$. Since $$X$$ is sequentially compact, this sequence has a convergent subsequence; if this subsequence converges to $$x$$, then one can verify that $$x$$ is a limit point of $$A'$$ and hence of $$A$$.

</details>

## Convergence of Sequences

On the other hand, the converse of [Proposition 5](#prop5) does not hold either. This may seem somewhat surprising, because given any sequence $$(x_n)$$ in a limit point compact space, the set $$A=\{x_n\mid n\geq 1\}$$ is either finite, in which case it trivially has a convergent subsequence, or infinite, in which case it has a limit point. The problem is that there may not exist a subsequence converging to a limit point of $$A$$.

<div class="example" markdown="1">

<ins id="ex6">**Example 6**</ins> Consider the collection of subsets of $$\mathbb{R}$$

$$\mathcal{B}=\{(a,\infty)\mid a\in \mathbb{R}\}$$

This collection satisfies the conditions of [§Bases of Topological Spaces, ⁋Corollary 6](/en/math/topology/topological_bases#cor6), and thus defines a topology on $$\mathbb{R}$$.

Consider the sequence $$(x_n)_{n\geq 1}$$ in this topological space $$\mathbb{R}$$ defined by

$$x_n=-n$$

Then $$(x_n)$$ has no convergent subsequence. On the other hand, $$A=\{x_n\mid n\geq 1\}$$ does have a limit point; for instance, $$-2$$ is a limit point of $$A$$, because any open set containing $$-2$$ must also contain $$-1\in A$$.

</div>

The above example shows that convergence of sequences is not a very good concept for checking limit points. On the other hand, by [§Interior, Closure, and Boundary of Sets, ⁋Proposition 6](/en/math/topology/other_concepts#prop6), any limit point of a set $$A$$ belongs to the closure of $$A$$.

<div class="proposition" markdown="1">

<ins id="lem7">**Lemma 7**</ins> For a topological space $$X$$ and any subset $$A\subseteq X$$, if there exists a sequence in $$A$$ converging to $$x\in X$$, then $$x\in \cl(A)$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Choose any open neighborhood $$U$$ of $$x$$. Since there exists a sequence $$(x_n)$$ converging to $$x$$, there exists some $$N\in \mathbb{N}$$ such that $$x_n\in U$$ for all $$n\geq N$$. Then $$x_N\in U\cap A$$, so $$U\cap A\neq \emptyset$$, and therefore $$x\in \cl(A)$$.

</details>

Therefore, for a topological space $$X$$ and a subset $$A$$, if we define the *sequential closure* $$\scl(A)$$ of $$A$$ by

$$\scl(A)=\{x\in X\mid \text{there exists a sequence in $A$ that converges to $x$}\}$$

then it is clear that $$\scl(A)\subseteq \cl(A)$$.

<div class="example" markdown="1">

<ins id="ex8">**Example 8**</ins> Consider the uncountable product $$\mathbb{R}^J$$ with the usual product topology. Define the set $$A$$ by

$$A=\{(x_j)\in \mathbb{R}^J: x_j=1\text{ for all but finitely many $j$}\}$$

Then the origin of $$\mathbb{R}^J$$ belongs to the closure of $$A$$. This is because any basic open set containing the origin is $$\mathbb{R}$$ in all but finitely many coordinates, and the point that is $$0$$ in those finitely many indices and $$1$$ in all other indices lies in the intersection of this basic open set with $$A$$. However, no sequence in $$A$$ converges to the origin. Given any sequence in $$A$$, since $$J$$ is uncountable, one can show that there exists some $$j\in J$$ such that the $$j$$-th coordinate of every term in the sequence is $$1$$; then the open neighborhood of the origin whose $$j$$-th coordinate is $$(-1,1)$$ and whose other coordinates are all $$\mathbb{R}$$ contains no term of the sequence.

</div>

That is, the converse of [Lemma 7](#lem7) does not hold in general. Or, using the language above, for a topological space $$X$$ and a subset $$A$$, we have $$\scl(A)\subsetneq \cl(A)$$ in general. If $$\scl(A)=\cl(A)$$ holds for every subset $$A$$, then $$X$$ is called a *sequential space*.

On the other hand, the following proposition, although slightly generalized, is still familiar.

<div class="proposition" markdown="1">

<ins id="prop9">**Proposition 9**</ins> For a continuous function $$f:X \rightarrow Y$$ and any sequence $$(x_n)$$ in $$X$$, if $$(x_n)$$ converges to $$x\in X$$, then $$(f(x_n))$$ converges to $$f(x)$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Choose any open neighborhood $$V$$ of $$f(x)$$. Since $$f$$ is continuous, $$f^{-1}(V)$$ is an open neighborhood of $$x$$. Hence there exists some $$N\in \mathbb{N}$$ such that $$x_n\in f^{-1}(V)$$ for all $$n\geq N$$. Then $$f(x_n)\in V$$, so $$(f(x_n))$$ converges to $$f(x)$$.

</details>

On the other hand, if the converse of [Lemma 7](#lem7) holds in a space $$X$$, then using that result together with the second condition of [§Continuous Functions, ⁋Theorem 4](/en/math/topology/continuous_functions#thm4), one can also prove the converse of [Proposition 9](#prop9). That is, if for every sequence $$(x_n)$$ converging to any $$x\in A$$, the sequence $$f(x_n)$$ converges to $$f(x)$$, then $$f$$ is continuous at the point $$x$$.

Suppose $$X$$ is a space in which the converse of [Lemma 7](#lem7) holds. Then for any $$x\in \cl(A)$$, we can pick a sequence $$(x_n)$$ in $$X$$ converging to $$x$$. Then the sequence $$f(x_n)$$ in $$Y$$ converges to $$f(x)$$, so by [Lemma 7](#lem7) we have $$f(x)\in \cl(f(A))$$, and the desired result follows from [§Continuous Functions, ⁋Theorem 4](/en/math/topology/continuous_functions#thm4).

## Countability Axioms

The above discussion shows that convergence of sequences is not an adequate concept for capturing the notions we have studied so far. Looking at the proof of [Proposition 11](#prop11) suggests how we might generalize it.

<div class="definition" markdown="1">

<ins id="def10">**Definition 10**</ins> For a topological space $$X$$, we define the following.

1. $$X$$ is *first countable* if for every point $$x\in X$$, there exists a countable local base at $$x$$.
2. $$X$$ is *second countable* if there exists a countable base for $$X$$.

</div>

<div class="proposition" markdown="1">

<ins id="prop11">**Proposition 11**</ins> If $$X$$ is first countable and $$T_1$$, and limit point compact, then $$X$$ is sequentially compact.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

As mentioned earlier, given any sequence $$(x_n)$$, the set $$A=\{x_n\mid n\geq 1\}$$ is either finite, in which case it trivially has a convergent subsequence, or infinite, in which case it has a limit point $$x$$. If $$x=x_n$$ holds for infinitely many $$n$$, then again we trivially obtain a subsequence converging to $$x$$. Thus we may assume that there are only finitely many $$n$$ satisfying $$x_n=x$$, and since this does not affect convergence, we may assume without loss of generality that $$x_n\neq x$$ for all $$n$$.

Since $$X$$ is first countable, we can consider a countable local base $$\mathcal{B}(x)$$ at $$x$$. Writing the elements of $$\mathcal{B}(x)$$ as $$B_1,B_2,\ldots$$, we may replace $$B_n$$ by $$B_1\cap\cdots\cap B_n$$ so that $$B_{n+1}\subseteq B_n$$ holds for all $$n$$.

Now $$B_1$$ is an open set containing $$x$$, and since $$x$$ is a limit point of $$A$$, there exists some $$n_1$$ such that $$x_{n_1}\in B_1$$. Since $$X$$ is $$T_1$$, there exists an open set $$U_2$$ containing $$x$$ but not $$x_1,\ldots,x_{n_1}$$. Then $$U_2\cap B_2$$ is again an open set containing $$x$$, and since $$x$$ is a limit point of $$A$$, there exists some $$n_2$$ such that $$x_{n_2}\in U_2\cap B_2$$. Repeating this process, we obtain a subsequence of $$A$$ converging to $$x$$.

</details>

Moreover, one can easily show that every first countable space is a sequential space.

## Convergence of Filters

What played a key role in the proof of [Proposition 11](#prop11) was that $$x$$ has a decreasing sequence of open sets

$$B_1\supseteq B_2\supseteq\cdots$$

and by first countability, for any given open set $$U$$, we can arrange that $$B_n\subseteq U$$ for all sufficiently large $$n$$. In a sense, the open sets themselves can be regarded as converging to $$x$$. Motivated by this observation, we define the following.

<div class="definition" markdown="1">

<ins id="def12">**Definition 12**</ins> Consider a topological space $$X$$ and a filter $$\mathcal{F}$$ defined on it. ([§Equivalent Formulations of Topological Spaces, ⁋Definition 3](/en/math/topology/equivalent_formulations_of_topology#def3)) Then $$\mathcal{F}$$ is said to *converge* to $$x\in X$$ if $$\mathcal{N}(x)\subseteq \mathcal{F}$$. ([§Open Sets, §§Neighborhood filter](/en/math/topology/open_sets#neighborhood-filter)) In this case, $$x$$ is called a *limit point* of $$\mathcal{F}$$.

</div>

[Definition 12](#def12) generalizes the convergence of sequences. To verify this, we first need the following definition.

<div class="definition" markdown="1">

<ins id="def13">**Definition 13**</ins> Let a filter $$\mathcal{F}$$ be defined on a set $$X$$, and let $$X$$ be a topological space. For a function $$f:X \rightarrow Y$$, we say that $$y\in Y$$ is a *limit point* of $$f$$ with respect to $$\mathcal{F}$$ if $$y$$ is a limit point of the filter $${\uparrow}f(\mathcal{F})$$. ([§Equivalent Formulations of Topological Spaces, ⁋Proposition 7](/en/math/topology/equivalent_formulations_of_topology#prop7))

</div>

Then by definition, $$y\in Y$$ is a limit point of $$f$$ with respect to $$\mathcal{F}$$ if and only if for every neighborhood $$V$$ of $$y$$, there exists some $$F\in \mathcal{F}$$ such that $$f(F)\subseteq V$$. In particular, the following holds.

<div class="proposition" markdown="1">

<ins id="prop14">**Proposition 14**</ins> For a sequence $$(x_n)_{n\geq 1}$$ in a topological space $$X$$, the sequence converges to $$x\in X$$ if and only if the filter generated by the image of the Fréchet filter $$\mathcal{F}$$ on $$\mathbb{N}$$ under the map $$n\mapsto x_n$$ converges to $$x$$. ([§Equivalent Formulations of Topological Spaces, ⁋Example 4](/en/math/topology/equivalent_formulations_of_topology#ex4))

</div>

Thus we see that convergence of filters generalizes convergence of sequences. Moreover, using this concept we can prove the following proposition.

<div class="proposition" markdown="1">

<ins id="prop15">**Proposition 15**</ins> For a topological space $$X$$ and any subset $$A\subseteq X$$, the following are equivalent: $$x\in\cl(A)$$, and there exists a filter $$\mathcal{F}$$ on $$A$$ converging to $$x$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, suppose there exists a filter $$\mathcal{F}$$ on $$A$$ converging to $$x$$. That is, $$\mathcal{F}$$ contains the element $$A$$ and the collection $$\mathcal{N}(x)$$. Therefore, by the definition of a filter, for every neighborhood $$U\in \mathcal{N}(x)$$ we have $$U\cap A\neq\emptyset$$.

Conversely, suppose $$x\in \cl(A)$$. Then for every neighborhood $$U$$ of $$x$$, we have $$U\cap A\neq\emptyset$$, so the collection

$$\mathcal{N}(x)\vert_A=\{U\cap A\mid U\in \mathcal{N}(x)\}$$

defines a filter base. Now let $$\mathcal{F}$$ be the filter generated by $$\mathcal{N}(x)\vert_A$$; then we obtain the desired result.

</details>

Therefore, by the argument following [Lemma 8](#lem8), the following proposition is also clear.

<div class="proposition" markdown="1">

<ins id="prop16">**Proposition 16**</ins> For a function $$f:X \rightarrow Y$$ between topological spaces, $$f$$ is continuous at $$x\in X$$ if and only if for every filter $$\mathcal{F}$$ converging to $$x$$, the filter defined by the filter base $$f(\mathcal{F})$$ converges to $$f(x)$$.

</div>
