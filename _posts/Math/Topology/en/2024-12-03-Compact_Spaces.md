---
title: "Compact Spaces"
description: "This post covers the definition of compactness in topological spaces and the conditions for the existence of finite subcovers, along with criteria for determining the compactness of subspaces and a proof that closed subsets of compact spaces are compact."
excerpt: "Compact spaces defined by finite subcovers of open covers"

categories: [Math / Topology]
permalink: /en/math/topology/compact_spaces
sidebar: 
    nav: "topology-en"

date: 2024-12-03
weight: 14
translated_at: 2026-06-03T07:00:01+00:00
translation_source: kimi-cli
last_polished_at: 2026-11-09T23:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
We now define the notion of compactness.

## Compact Sets

::: Definition 1
A topological space $X$ is *compact* if whenever an arbitrary open covering of $X$, $(U_i)_{i\in I}$, is given, there exists a finite subset $J\subseteq I$ such that $(U_j)_{j\in J}$ is still an open covering of $X$.
:::

By definition, we know that a finite union of compact subspaces of a topological space is again compact. In this way, compactness is related to an appropriate kind of finiteness.

In a topological space $X$, consider a subspace $Y$. Then since $Y$ is also a topological space, we can examine whether this topological space is compact. The following proposition shows that to verify whether $Y$ is compact, it suffices to consider a covering consisting of open sets in $X$.

::: Proposition 2
In a topological space $X$, consider a subspace $Y$. Then $Y$ is compact if and only if, whenever a family of open sets of $X$, $(U_i)_{i\in I}$, satisfies $Y\subseteq\bigcup U_i$, there exists a finite subset $J\subseteq I$ such that the union of $(U_j)_{j\in J}$ still contains $Y$.
:::
::: Proof
First, assume that $Y$ is compact, and suppose we are given, satisfying $Y\subseteq\bigcup U_i$, a family of open sets of $X$, $(U_i)_{i\in I}$. Then the sets $Y\cap U_i$ are open in $Y$, and therefore $(U_i\cap Y)_{i\in I}$ is an open covering of $Y$, from which we can choose a finite subset $J$ such that $(U_j\cap Y)_{j\in J}$ is still an open covering of $Y$. It is then obvious that the union of $(U_j)$ still contains $Y$.

Conversely, assume that the given condition holds, and suppose an arbitrary open covering of $Y$, $(V_i)_{i\in I}$, is given. Then by the definition of the topological structure on $Y$, there exist, such that $V_i=U_i\cap Y$, open sets in $X$, $(U_i)$, and $\bigcup U_i$ contains $Y$. Thus there exists a finite subset $J$ such that the union of $(U_j)_{j\in J}$ contains $Y$. Then $(V_j)_{j\in J}$ is the desired finite subcover of $(V_i)_{i\in I}$.
:::

By the proposition above, to prove the compactness of $Y$, it suffices to take open sets in the space containing $Y$, namely $X$, cover $Y$ with them, and then show that these satisfy the condition of [Definition 1](#def1){: data-lid="8ix8i" }. Therefore, by a slight abuse of terminology, we call open sets satisfying $Y\subseteq \bigcup U_i$ in $X$, $U_i$, an open cover of $Y$, and we shall make this distinction clearly only when there is room for confusion.

::: Lemma 3
A closed subset of a compact space is compact.
:::
::: Proof
Suppose we are given a compact space $X$, a closed subset of $X$, $Y$, and an open covering of $Y$, $(U_i)$. Then $X\setminus Y$ is an open set, and adding this set to the open covering of $Y$, $(U_i)$, yields an open covering of $X$. Since $X$ is compact, this new covering has a finite subcover; removing $X\setminus Y$ from that finite subcover again gives a covering of $Y$, which is a finite subcover of the original $(U_i)$.
:::

## Compact Hausdorff Spaces

For a Hausdorff space defined in the previous post, adding the compact condition makes it satisfy even better conditions. To this end, let us first prove the following lemma.

::: Lemma 4
Suppose given a Hausdorff space $X$, a point of $X$, $x$, and, not containing $x$, a compact subspace of $X$, $Y$. Then the two sets $\{x\}$ and $Y$ can be separated by neighborhoods.
:::
::: Proof
Since $X$ is a Hausdorff space, for each $y\in Y$, there exist an open neighborhood of $x$, $U_{xy}$, and an open neighborhood of $y$, $V_y$, such that $U_{xy}\cap V_y=\emptyset$. Now by [Proposition 2](#prop2){: data-lid="0vonz" }, there exists a finite subcover of $(V_y)_{y\in Y}$, $V_{y_1},\ldots,V_{y_n}$, such that

$$Y\subseteq V_{y_1}\cup\cdots\cup V_{y_n}$$

still holds. Now

$$U_{xy_1}\cap \cdots\cap U_{xy_n}$$

is disjoint from $\bigcup_{i=1}^n V_{y_i}$ and is an open neighborhood of $\{x\}$.
:::

In particular, the following holds.

::: Corollary 5
In a Hausdorff space $X$, a compact subset $Y$ is closed.
:::
::: Proof
In the proof of [Lemma 4](#lem4){: data-lid="3pxrl" }, if we set 

$$U_x=U_{xy_1}\cap \cdots\cap U_{xy_n}$$

then $X\setminus Y=\bigcup_{x\not\in Y} U_x$.
:::

As mentioned above, a compact Hausdorff space satisfies the following additional separation axiom. ([§Hausdorff Spaces, ⁋Definition 3](/en/math/topology/Hausdorff_spaces#def3){: data-lid="unkff" })

::: Lemma 6
A compact Hausdorff space is a regular space.
:::
::: Proof
Fix a compact Hausdorff space $X$, and suppose given a point $x\in X$ and, not containing $x$, a closed subset of $X$, $Y$. Then $Y$ is compact by [Lemma 3](#lem3){: data-lid="svb53" }, and thus the desired result is immediate from [Lemma 4](#lem4){: data-lid="mrfyt" }. 
:::

Moreover, applying this once more yields the following proposition.

::: Proposition 7
A compact Hausdorff space is a normal space.
:::
::: Proof
Let any two disjoint closed subsets $A,B$ of a compact Hausdorff space be given. Then for each $a\in A$, by [Lemma 6](#lem6){: data-lid="40yv7" } there exist an open neighborhood of $a$, $U_a$, and an open neighborhood of $B$, $V_{a}$, such that $U_a\cap V_a=\emptyset$. Now, in the same manner as in [Lemma 4](#lem4){: data-lid="aexi2" }, since $(U_a)_{a\in A}$ is an open covering of $A$, by [Lemma 3](#lem3){: data-lid="xa9oq" } again we can choose from $(U_a)$ a finite subcover $U_{a_1},\ldots, U_{a_n}$, and now the two open sets

$$U_{a_1}\cup\cdots \cup U_{a_n},\qquad V_{a_1}\cap\cdots\cap V_{a_n}$$

are open neighborhoods separating the two closed subsets $A,B$.
:::

## Compact Spaces and Continuous Functions

Compactness also behaves well with respect to continuous functions.

::: Proposition 8
For a continuous function $f:X \rightarrow Y$ and any compact subspace of $X$, $A$, the set $f(A)$ is also compact.
:::
::: Proof
For any open covering of $f(A)$, $(U_i)$, the family $(f^{-1}(U_i))$ is a covering of $A$, and since $A$ is compact, a finite subcover exists. The corresponding $U_i$ form a finite open subcover covering $f(A)$.
:::

Meanwhile, we have seen that a bijective continuous function $f:X \rightarrow Y$ need not be a homeomorphism; however, if $X$ is compact and $Y$ is Hausdorff, then this holds.

::: Proposition 9
If $X$ is compact and $Y$ is Hausdorff, then any bijective continuous function $f:X \rightarrow Y$ is a homeomorphism.
:::
::: Proof
To this end, we must show that $f^{-1}$ is continuous. Let us use the third condition of [§Continuous Functions, ⁋Theorem 4](/en/math/topology/continuous_functions#thm4){: data-lid="44eko" }: that is, we must show that $f$ is a closed map. However, assuming that a closed subset of $X$, $A$, is given, it suffices to apply [Lemma 3](#lem3){: data-lid="m5ssk" }, [Proposition 8](#prop8){: data-lid="sdibz" }, and [Corollary 5](#cor5){: data-lid="d5sv9" } in order.
:::

## Finite Intersection Property

::: Definition 10
For a set $X$, a family $\mathcal{A}$ of subsets has the *finite intersection property* if for any finitely many elements of $\mathcal{A}$, $A_1,\ldots, A_n$,

$$A_1\cap\cdots\cap A_n$$

is nonempty.
:::

Then in particular $\emptyset\not\in \mathcal{A}$ holds. Also, given a family $\mathcal{A}$ satisfying this condition, by adding all finite intersections of elements of $\mathcal{A}$ we can obtain on $X$ a filter base $\mathcal{B}$. ([§Other Definitions of Topological Spaces, ⁋Definition 5](/en/math/topology/equivalent_formulations_of_topology#def5){: data-lid="83o2l" }) For this reason, $\mathcal{A}$ is also called a *subbase* of $\uparrow \mathcal{B}$.

Then the following proposition states compactness in another way.

::: Proposition 11
A topological space $X$ is compact if and only if for every family $\mathcal{A}$ of closed sets satisfying the finite intersection property, $\bigcap \mathcal{A}\neq\emptyset$.
:::
::: Proof
It suffices to take complements.
:::

---

**References**

**[Bou]** N. Bourbaki, <i>General Topology</i>. Elements of mathematics. Springer, 1995.
