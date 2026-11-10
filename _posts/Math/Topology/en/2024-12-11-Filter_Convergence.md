---
title: "Compactness and Convergence of Filters"
description: "This post covers the definitions of limit point compactness, compactness, and sequential compactness in topological spaces, and the inclusion relationships among them."
excerpt: "Characterizing compactness via filter convergence"

categories: [Math / Topology]
permalink: /en/math/topology/filter_convergence
sidebar: 
    nav: "topology-en"

date: 2024-12-11
weight: 15
translated_at: 2026-06-27T01:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-11-10T15:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
We first define the following.

::: Definition 1
A topological space $X$ is called *limit point compact* if every infinite subset of $X$ has a limit point. ([§Interior, Closure, and Boundary, ⁋Definition 8](/en/math/topology/other_concepts#def8){: data-lid="hg2d1" })
:::

In general, the following holds.

::: Proposition 2
Every compact space is limit point compact.
:::
::: Proof
Suppose, for the sake of contradiction, that $X$ is a compact space that is not limit point compact. Then there exists an infinite subset $A$ having no limit point, and therefore by the argument following [§Interior, Closure, and Boundary, ⁋Definition 8](/en/math/topology/other_concepts#def8){: data-lid="kw5hd" }, we must have $\cl(A)\setminus A=\emptyset$. That is, $A$ must be closed, and hence compact. ([§Compact Spaces, ⁋Lemma 3](/en/math/topology/compact_spaces#lem3){: data-lid="0ak2t" }) On the other hand, since each $a\in A$ is also not a limit point of $A$, there exists for $a$ a suitable open neighborhood $U_a$ such that $A\cap U_a=\{a\}$. Then $(U_a)_{a\in A}$ is an open covering of $A$ having no finite subcover, which is a contradiction.
:::

However, the converse does not hold in general.

::: Example 3
Consider a two-point space $X$ with the trivial topology, and an infinite set $Y$ with the discrete topology. Then $X\times Y$ is limit point compact but not compact. Indeed, let $X=\{a,b\}$, and suppose an infinite subset of $X\times Y$, $S$, contains $(a,y)$ as an element. Since the smallest open set containing $(b,y)$ is $X\times \{y\}$ and this contains $(a,y)$, the point $(b,y)$ is a limit point of $S$, and the same holds if the roles of $a$ and $b$ are interchanged. On the other hand, $(X\times \{y\})_{y\in Y}$ is an open covering of $X\times Y$ having no finite subcover.
:::

We also define the following.

::: Definition 4
A topological space $X$ is called *sequentially compact* if every sequence in $X$ has a convergent subsequence.
:::

::: Proposition 5
Every sequentially compact space is limit point compact.
:::
::: Proof
Let $X$ be a sequentially compact space, and suppose there exists an infinite subset $A$ having no limit point. Then, choosing from $A$ a suitable countable subset $A'$, we can form a sequence $(x_n)_{n\geq 1}$. Since $X$ is sequentially compact, this sequence has a convergent subsequence; if this subsequence converges to $x$, then one can verify that $x$ is a limit point of $A'$, and hence of $A$.
:::

## Convergence of Sequences

Meanwhile, the converse of [Proposition 5](#prop5){: data-lid="xr3cw" } also fails. This may seem somewhat surprising, because if an arbitrary sequence $(x_n)$ in a limit point compact space is given, the set $A=\{x_n\mid n\geq 1\}$ is either finite, in which case it trivially has a convergent subsequence, or infinite, in which case it has a limit point. The problem is that there may not exist a subsequence converging to a limit point of the set $A$.

::: Example 6
Consider the collection of subsets of $\mathbb{R}$

$$\mathcal{B}=\{(a,\infty)\mid a\in \mathbb{R}\}$$

This collection satisfies the conditions of [§Bases of a Topological Space, ⁋Corollary 6](/en/math/topology/topological_bases#cor6){: data-lid="ipoaw" }, and thus defines a topology on $\mathbb{R}$.

For the topological space $\mathbb{R}$ defined in this way, define a sequence $(x_n)_{n\geq 1}$ by the formula

$$x_n=-n$$

Then $(x_n)$ has no convergent subsequence. On the other hand, $A=\{x_n\mid n\geq 1\}$ has a limit point; for instance, $-2$ is a limit point of $A$, because any open set containing $-2$ must also contain $-1\in A$.
:::

The above example shows that convergence of sequences is not a very good notion for detecting limit points. On the other hand, by [§Interior, Closure, and Boundary, ⁋Proposition 6](/en/math/topology/other_concepts#prop6){: data-lid="1ie7y" }, any limit point of a set $A$ belongs to the closure of $A$.

::: Lemma 7
For a topological space $X$ and an arbitrary subset $A\subseteq X$, if there exists a sequence converging to $x\in X$ in $A$, then $x\in \cl(A)$.
:::
::: Proof
For $x$, choose an arbitrary open neighborhood $U$. Then, since there exists a sequence converging to $x$, $(x_n)$, there exists an appropriate $N\in \mathbb{N}$ such that if $n\geq N$, then $x_n\in U$. Then since $x_N\in U\cap A$, we have $U\cap A\neq \emptyset$, and therefore $x\in \cl(A)$.
:::

Therefore, for a topological space $X$ and a subset $A$, if we define the *sequential closure* of $A$, $\scl(A)$, by

$$\scl(A)=\{x\in X\mid \text{there exists a sequence in $A$ that converges to $x$}\}$$

it is natural that $\scl(A)\subseteq \cl(A)$ holds.

::: Example 8
For $\mathbb{R}$ given the usual topology, consider the uncountable product $\mathbb{R}^J$. Define the set $A$ by

$$A=\{(x_j)\in \mathbb{R}^J\mid x_j=1\text{ for all but finitely many $j$}\}$$

Then the origin of $\mathbb{R}^J$ belongs to the closure of $A$. This is because a basis element of $\mathbb{R}^J$ containing the origin has all coordinates equal to $\mathbb{R}$ except for finitely many indices, and the point whose components at these finite indices are defined to be $0$ and whose components at the remaining indices are $1$ is contained in the intersection of this basis element and $A$. However, no sequence in $A$ converges to the origin. This is because, given any sequence in $A$, using that $J$ is uncountable one can show that having the $j$th component of all terms of this sequence be $1$ holds for some $j\in J$, and then the open neighborhood of the origin whose $j$th component is $(-1,1)$ and whose remaining components are $\mathbb{R}$ contains no element of this sequence.
:::

That is, the converse of [Lemma 7](#lem7){: data-lid="7bwnr" } also does not hold in general. Or, using the language above, one can say that for a topological space $X$ and a subset $A$, in general it may be that $\scl(A)\neq \cl(A)$. If $\scl(A)=\cl(A)$ holds for every subset $A$, then $X$ is called a *Fréchet–Urysohn space*.

Meanwhile, the following proposition, although slightly generalized, is still familiar.

::: Proposition 9
For a continuous function $f:X \rightarrow Y$ and an arbitrary sequence in $X$, $(x_n)$, if $(x_n)$ converges to $x\in X$, then $(f(x_n))$ converges to $f(x)$.
:::
::: Proof
For $f(x)$, choose an arbitrary open neighborhood $V$. Then since $f$ is a continuous function, $f^{-1}(V)$ is an open neighborhood of $x$. Therefore, there exists an appropriate $N\in \mathbb{N}$ such that if $n\geq N$, then $x_n\in f^{-1}(V)$. Then since $f(x_n)\in V$, $(f(x_n))$ converges to $f(x)$.
:::

Meanwhile, if in the space $X$ the converse of [Lemma 7](#lem7){: data-lid="4oyes" } holds, then using that result and the second condition of [§Continuous Functions, ⁋Theorem 4](/en/math/topology/continuous_functions#thm4){: data-lid="9lx73" }, one can also show the converse of [Proposition 9](#prop9){: data-lid="sj54x" }. That is, if for any sequence converging to an arbitrary $x\in X$, $(x_n)$, we have that $f(x_n)$ converges to $f(x)$, then $f$ is continuous at the point $x$.

Suppose $X$ is a space in which the converse of [Lemma 7](#lem7){: data-lid="i6oy0" } holds. Then, for any $x\in \cl(A)$, we can choose a sequence converging to $x$ in $A$, $(x_n)$. Then since in $Y$ the sequence $f(x_n)$ converges to $f(x)$, by [Lemma 7](#lem7){: data-lid="y5ayz" } we have $f(x)\in \cl(f(A))$, and from [§Continuous Functions, ⁋Theorem 4](/en/math/topology/continuous_functions#thm4){: data-lid="38979" } we obtain the desired result.

## Countability Axioms

The above contents show that convergence of sequences is not an appropriate notion for representing the concepts dealt with so far. Examining the proof of [Proposition 11](#prop11){: data-lid="73s9b" }, one can see in what manner it is desirable to generalize this.

::: Definition 10
For a topological space $X$, we define the following.

1. That $X$ is *first countable* means that for every point of $X$, $x\in X$, there exists a countable local base at $x$. ([§Bases of a Topological Space, ⁋Definition 4](/en/math/topology/topological_bases#def4){: data-lid="1kuh9" })
2. That $X$ is *second countable* means that there exists a countable base for $X$. ([§Bases of a Topological Space, ⁋Definition 1](/en/math/topology/topological_bases#def1){: data-lid="ou5pu" })
:::

::: Proposition 11
If $X$ is first countable, $T_1$, and limit point compact, then $X$ is sequentially compact.
:::
::: Proof
As mentioned before, given an arbitrary sequence $(x_n)$, the set $A=\{x_n\mid n\geq 1\}$ is either a finite set and for trivial reasons has a convergent subsequence, or an infinite set and has a limit point $x$. If $x=x_n$ holds for infinitely many $n$, then again for trivial reasons we can choose a subsequence converging to $x$, so we may assume that $x_n=x$ holds for only finitely many $n$; since this does not affect convergence of the sequence, we may assume without loss of generality that $x_n\neq x$ holds for all $n$.

Meanwhile, since $X$ is first countable, we can consider a countable local base at $x$, $\mathcal{B}(x)$. Writing the elements of $\mathcal{B}(x)$ as $B_1,B_2,\ldots$, we may replace $B_n$ by $B_1\cap\cdots\cap B_n$ so that $B_{n+1}\subseteq B_n$ holds for all $n$.

Now $B_1$ is an open set containing $x$, and since $x$ is a limit point of $A$, there exists a suitable $n_1$ such that $x_{n_1}\in B_1$. Now since $X$ is $T_1$, there exists, containing $x$ but not containing $x_1,\ldots,x_{n_1}$, an open set $U_2$. Then $U_2\cap B_2$ is again an open set containing $x$, and since $x$ is a limit point of $A$, there exists a suitable $n_2$ such that $x_{n_2}\in U_2\cap B_2$. Repeating this process, we can obtain a subsequence converging to $x$ of $(x_n)$.
:::

Furthermore, one can easily show that a first countable space is a Fréchet–Urysohn space.

::: Proposition 12
Every second countable space $X$ is *Lindelöf*. That is, every open cover of $X$ has a countable subcover.
:::
::: Proof
Fix for $X$ a countable base $\mathcal{B}=\{B_1, B_2, \ldots\}$, and let an arbitrary open cover of $X$, $(U_\alpha)_{\alpha\in A}$, be given. For each point $x\in X$, we have $x\in U_\alpha$ for some $\alpha$, and by the definition of a base, $x\in B_n\subseteq U_\alpha$ for some $B_n\in\mathcal{B}$. Collecting all such $B_n$, covering $X$, we obtain a countable subcollection of $\mathcal{B}$, $\{B_{n_1}, B_{n_2}, \ldots\}$. Now for each $k$, if we choose, satisfying $B_{n_k}\subseteq U_{\alpha_k}$, one $\alpha_k$, then $(U_{\alpha_k})_{k\geq 1}$ is a countable subcover of $(U_\alpha)_{\alpha\in A}$.
:::

## Convergence of Filters

What played an essential role in the proof of [Proposition 11](#prop11){: data-lid="o924j" } was that $x$ possesses a decreasing sequence of open sets

$$B_1\supseteq B_2\supseteq\cdots$$

and by first countability, given any open neighborhood of $x$, $U$, for sufficiently large $n$, one can arrange that $B_n\subseteq U$. That is, in a certain sense, the above open sets themselves can be regarded as converging to $x$. Based on this observation, we define the following.

::: Definition 13
Consider a topological space $X$ and a filter $\mathcal{F}$ defined on it. ([§Other Definitions of Topological Spaces, ⁋Definition 3](/en/math/topology/equivalent_formulations_of_topology#def3){: data-lid="55frh" }) Then $\mathcal{F}$ is said to *converge* to $x\in X$ if $\mathcal{N}(x)\subseteq \mathcal{F}$ holds. ([§Open Sets, §§Neighborhood filter](/en/math/topology/open_sets#neighborhood-filter){: data-lid="twg84" }) In this case, $x$ is called a *limit point* of $\mathcal{F}$.
:::

[Definition 13](#def13){: data-lid="y6olx" } generalizes the convergence of sequences. To verify this, we first need to define the following.

::: Definition 14
On a set $X$, let a filter $\mathcal{F}$ be defined, and let a topological space $Y$ be given. For a function $f:X \rightarrow Y$, we say that $y\in Y$ is, with respect to $\mathcal{F}$, a *limit point* of $f$ if $y$ is a limit point of the filter ${\uparrow}f(\mathcal{F})$. ([§Other Definitions of Topological Spaces, ⁋Proposition 7](/en/math/topology/equivalent_formulations_of_topology#prop7){: data-lid="jrvu7" })
:::

Then by definition, that $y\in Y$ is, with respect to $\mathcal{F}$, a limit point of $f$ means that for $y$, whenever any of its neighborhoods $V$ is given, there exists $F\in \mathcal{F}$ such that $f(F)\subseteq V$. In particular, the following holds.

::: Proposition 15
In a topological space $X$, for a sequence $(x_n)_{n\geq 1}$, $(x_n)_{n\geq 1}$ converging to $x\in X$ is equivalent to the filter generated by the image of the Fréchet filter on $\mathbb{N}$, $\mathcal{F}$, under the map $n\mapsto x_n$ converging to $x$. ([§Other Definitions of Topological Spaces, ⁋Example 4](/en/math/topology/equivalent_formulations_of_topology#ex4){: data-lid="3f216" })
:::

Thus we see that convergence of filters generalizes convergence of sequences. Moreover, through this notion we can prove the following proposition.

::: Proposition 16
For a topological space $X$ and an arbitrary subset $A\subseteq X$, that $x\in\cl(A)$ is equivalent to the existence of a filter converging to $x$ on $A$, $\mathcal{F}$.
:::
::: Proof
First, suppose there exists a filter converging to $x$ on $A$, $\mathcal{F}$. That is, every element of $\mathcal{F}$ meets $A$ and $\mathcal{N}(x)\subseteq \mathcal{F}$. Therefore, by the definition of a filter, for every neighborhood $U\in \mathcal{N}(x)$ we have $U\cap A\neq\emptyset$.

Conversely, suppose $x\in \cl(A)$. Then for $x$, since for every neighborhood $U$ we have $U\cap A\neq\emptyset$, the following expression

$$\mathcal{N}(x)\vert_A=\{U\cap A\mid U\in \mathcal{N}(x)\}$$

defines a filter base. Now letting $\mathcal{F}$ be the filter defined by $\mathcal{N}(x)\vert_A$, we obtain the desired result.
:::

Therefore, by the argument after [Lemma 7](#lem7){: data-lid="7930i" }, the following proposition is also obvious.

::: Proposition 17
For a function $f:X \rightarrow Y$ between topological spaces, the function $f$ is continuous at $x\in X$ if and only if for every filter converging to $x$, $\mathcal{F}$, the filter defined by the filter base $f(\mathcal{F})$ converges to $f(x)$.
:::

## Tychonoff theorem

An arbitrary product of compact spaces is again a compact space. If this product is finite, this result can be shown in a more intuitive manner, but if this product is infinite, the following lemma is needed for this. This generalizes [Proposition 5](#prop5){: data-lid="yf0r0" } to the language of filters.

::: Lemma 18
A topological space $X$ is compact if and only if every ultrafilter converges.
:::
::: Proof
First, assume $X$ is compact and let an arbitrary ultrafilter $\mathcal{F}$ be given. Suppose for contradiction that $\mathcal{F}$ has no limit point. That is, for every $x\in X$, there exists an open neighborhood $U_x$ such that $U_x\not\in \mathcal{F}$. Then by the compactness of $X$, there exists a finite subcover $U_{x_1},\ldots, U_{x_n}$ of $X$. 

On the other hand, by [\[Set Theory\] §Filters, Ideals, and Galois Connections, ⁋Proposition 5](/en/math/set_theory/filter_and_ideal#prop5){: data-lid="p9nwn" }, $\mathcal{F}$ is prime. That is, for any subset $A\subseteq X$, exactly one of $A\in \mathcal{F}$ or $X\setminus A\in \mathcal{F}$ holds. Now for any $A\in \mathcal{F}$,

$$A=A\cap X=(A\cap U_{x_1})\cup \cdots\cup (A\cap U_{x_n})\in \mathcal{F}$$

and since $U_{x_i}\not\in \mathcal{F}$ by assumption, each $A\cap U_{x_i}$ also does not belong to $\mathcal{F}$, and since $\mathcal{F}$ is maximal, we must have $X\setminus (A\cap U_{x_i})\in \mathcal{F}$. Then their finite intersection

$$X\setminus A=(X\setminus (A\cap U_{x_1}))\cap\cdots\cap (X\setminus (A\cap U_{x_n}))$$

must also belong to $\mathcal{F}$, which contradicts the fact that exactly one of $A$ and $X\setminus A$ belongs to $\mathcal{F}$. 

Conversely, suppose that whenever an arbitrary ultrafilter $\mathcal{F}$ is given, a limit point $x$ can be found, and let a family $\mathcal{A}$ of closed subsets of $X$ satisfying the finite intersection property be given. Then we can consider an ultrafilter $\mathcal{F}$ containing the filter generated by $\mathcal{A}$, and by assumption $\mathcal{F}$ has a limit point $x$. That is, $\mathcal{N}(x)\subseteq \mathcal{F}$, and therefore for any $F\in \mathcal{F}$ and any neighborhood $U$ of $x$, $U\cap F\neq\emptyset$. In particular, since $A\cap U\neq\emptyset$ for any $A\in \mathcal{A}$ and any neighborhood $U$ of $x$, $x\in \cl(A)=A$ always holds. From this we know that $x\in\bigcap_{A\in \mathcal{A}}A$, and therefore by [§Compact Spaces, ⁋Proposition 11](/en/math/topology/compact_spaces#prop11){: data-lid="q3oy1" } we obtain the desired result.
:::

Then the following holds.

::: Theorem 19 (Tychonoff)
The product $X=\prod_{i\in I} X_i$ of compact spaces $(X_i)_{i\in I}$ is compact. Conversely, if $X\neq\emptyset$ and the product space $X$ is compact, then each $X_i$ is compact.
:::
::: Proof
If $X$ is compact, that each $X_i$ is compact is trivial by the continuity of $\pr_i$ and [§Compact Spaces, ⁋Proposition 8](/en/math/topology/compact_spaces#prop8){: data-lid="sr8n2" }.

For the converse, for any ultrafilter $\mathcal{F}$ defined on $X$, after verifying that $\pr_i(\mathcal{F})$ defines an ultrafilter base on $X_i$, from the assumption that $X_i$ is compact and [Lemma 18](#lem18){: data-lid="qltnq" } we obtain a limit point $x_i$ of this ultrafilter; since we can show that $x=(x_i)_{i\in I}$ is a limit point of $\mathcal{F}$, the proof is completed again by [Lemma 18](#lem18){: data-lid="ydh22" }. 
:::

---

**References**

**[Bou]** N. Bourbaki, <i>General Topology</i>. Elements of mathematics. Springer, 1995.
