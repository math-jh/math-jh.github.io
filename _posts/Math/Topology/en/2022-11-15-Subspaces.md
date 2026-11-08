---
title: "Subspaces"
description: "This post introduces the definition of the subspace topology induced on a subset of a topological space and examines the properties of open and closed sets within a subspace."
excerpt: "Properties of subspaces"

categories: [Math / Topology]
permalink: /en/math/topology/subspaces
sidebar: 
    nav: "topology-en"

date: 2022-11-15
weight: 7
translated_at: 2026-06-03T04:00:01+00:00
translation_source: kimi-cli
last_polished_at: 2026-11-08T15:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
## Definition of Subspaces

Just as when dealing with algebraic structures, after equipping a set $X$ with a topological structure, it is natural to examine how this structure restricts to a subset $A\subseteq X$. The first idea that comes to mind is to select, among the open sets of $X$, only those contained in $A$ and define them to be the open sets of the topological space $A$. However, this attempt is bound to fail, because if $A$ is not an open set in $X$, then the whole set $A$ itself does not belong to this collection.

::: Definition 1
Let a topological space $(X,\mathcal{T})$ and a subset of $X$, $A$, be given. Then the initial topology defined by $\iota:A\hookrightarrow X$ on $A$ is called the *subspace topology on $A$*.
:::

For any open set of $X$, $U$, we have $\iota^{-1}(U)=U\cap A$, and for any family of open sets $(U_i)_{i\in I}$,

$$\iota^{-1}\left(\bigcup_{i\in I} U_i\right)=\left(\bigcup_{i\in I} U_i\right)\cap A=\bigcup_{i\in I} (U_i\cap A)=\bigcup_{i\in I} \iota^{-1}(U_i)$$

and for any finite family of open sets $(U_i)_{i\in I}$,

$$\iota^{-1}\left(\bigcap_{i\in I} U_i\right)=\left(\bigcap_{i\in I} U_i\right)\cap A=\bigcap_{i\in I} (U_i\cap A)=\bigcap_{i\in I} \iota^{-1}(U_i)$$

hold, so by [§Initial and Final Topology, ⁋Proposition 2](/en/math/topology/initial_and_final_topology#prop2){: data-lid="8i8pq" } we see that the subspace topology $\mathcal{T}_A$ is given by the formula

$$\mathcal{T}_A=\{U\cap A\mid U\in\mathcal{T}\}$$

In books such as **[Mun]**, this is even taken as the definition of a subspace. From this, we see that if $A\subseteq B\subseteq X$, then whether we regard $A$ as a subspace of $X$ or as a subspace of $B\subseteq X$ equipped with the subspace topology, we obtain the same space.

When dealing with subspaces, one must be careful that even if a set is open in $\mathcal{T}_A$, it may not be open in $\mathcal{T}$.

{% diagram Math/Topology/Subspaces-1.svg width="27.83em" alt="open_in_subspace_but_not_in_whole" %}

This situation is easily resolved if $A$ is an open set.

::: Lemma 2
For a topological space $X$ and a subspace $A$, a necessary and sufficient condition for every open set of $A$ to be open in $X$ is that $A$ be an open set in $X$.
:::
::: Proof
Since $A$ is an open set in $A$, one direction is trivial.

For the converse, if we choose any open set of $A$, it can be written as $U\cap A$ for some open set of $X$, $U$; since $A$ is also an open set, $U\cap A$ is also an open set.
:::

It is not difficult to see that the closed sets in the subspace $A$ are precisely the sets that, for a closed set of $X$, $C$, appear in the form $A\cap C$. In the case of closed sets as well, a situation like the example above can arise, and the way to resolve this is likewise simple.

::: Lemma 3
For a topological space $X$ and a subspace $A$, a necessary and sufficient condition for every closed set of $A$ to be closed in $X$ is that $A$ be a closed set in $X$.
:::
::: Proof
Since $A$ is a closed set in $A$, one direction is trivial.

For the converse, if we choose any closed set of $A$, it can be written as $U\cap A$ for some closed set of $X$, $U$; since $A$ is also a closed set, $U\cap A$ is also a closed set.
:::

Up to now, we have defined all topological properties through the notion of neighborhoods, and this too can be properly modified just as in the lemmas above.

::: Lemma 4
For a topological space $X$, given a subspace $A$ and any $x\in A$, a necessary and sufficient condition for every neighborhood in $A$ of $x$ to be a neighborhood in $X$ of $x$ is that $A$ be a neighborhood in $X$ of $x$.
:::
::: Proof
Since $A$ is a neighborhood in $A$ of $x$, one direction is trivial.

For the converse, choose an arbitrary neighborhood of $x$ in $A$, $U$. Then there exists, contained in $U$, an open neighborhood of $x$ (in $A$), $U'$. On the other hand, if $A$ is a neighborhood in $X$ of $x$, there exists, contained in $A$, an open neighborhood (in $X$) of $x$, $V$. At this point, choosing to satisfy $U'=W\cap A$ an open set of $X$, $W$, since $V\subseteq A$, $U'\cap V=W\cap A\cap V=W\cap V$ is an open set in $X$. Now $U'\cap V$ is a nonempty subset, $U'\cap V\subseteq U$, and since $U'\cap V$ is an open neighborhood in $X$ of $x$, $U$ is a neighborhood in $X$ of $x$.
:::

Through these lemmas, we can restrict the concepts we have examined so far to subspaces.

::: Proposition 5
Consider a topological space $X$ and subsets $A\subseteq B\subseteq X$. Then the closure $\cl_BA$ of $A$ in $B$ is equal to

$$\cl_BA=B\cap\cl_XA$$
:::
::: Proof
For any $x\in B$, a neighborhood of $x$ in $B$ can always be written, for a suitable neighborhood of $x$ in $X$, $V$, in the form $V\cap B$. Now using $V\cap A=(V\cap B)\cap A$ and [§Interior, Closure, and Boundary, ⁋Proposition 6](/en/math/topology/other_concepts#prop6){: data-lid="30tit" }, we obtain the desired result.
:::

Therefore, for $A\subseteq B\subseteq X$, the condition that $A$ be a dense subset of $B$ is equivalent to

$$B=\cl_BA=B\cap\cl_XA$$

and from this in turn we see that it is equivalent to $B\subseteq\cl_XA$.

::: Proposition 6
Let a topological space $X$ and a family of subsets of $X$, $(A_i)_{i\in I}$, be given, and suppose that one of the following two conditions holds.

1. $X=\bigcup_{i\in I}\interior(A_i)$ holds, or
2. $(A_i)_{i\in I}$ is a locally finite, closed covering of $X$.

Then, an arbitrary subset of $X$, $B$, is open (resp. closed) in $X$ if and only if for every $A_i$, $B\cap A_i$ is open (resp. closed) in $A_i$.
:::
::: Proof
First, from 

$$(X\setminus B)\cap A_i=A_i\setminus (B\cap A_i)$$

it suffices to prove this proposition for either open sets or closed sets. Also, if $B$ is open in $X$, then $B\cap A_i$ being open in $A_i$ is by definition, so the heart of the proposition is the converse.

1. Suppose that the $(A_i)$ satisfy the first condition, and assume that $B\cap A_i$ is open in $A_i$. Regarding $A_i$ as the whole set and $\interior A_i$ as a subspace, we know from this that $B\cap\interior A_i$ is open in $\interior A_i$. Now since $\interior A_i$ is an open set, applying [Lemma 2](#lem2){: data-lid="ckhze" } shows that $B\cap\interior A_i$ is open in $X$. Therefore, from
    
    $$B=B\cap X=B\cap\left(\bigcup_{i\in I} \interior A_i\right)=\bigcup_{i\in I}(B\cap\interior A_i)$$
    
    we see that $B$ is an open set.
2. Now suppose that $(A_i)$ satisfies the second condition. This time, we assume that the $B\cap A_i$ are all closed in $A_i$. Then $B\cap A_i$ is a closed set in $X$ by [Lemma 3](#lem3){: data-lid="bypay" }. Now $(B\cap A_i)$ is a locally finite collection of closed sets, and since $B=\bigcup (B\cap A_i)$, by [§Interior, Closure, and Boundary, ⁋Proposition 4](/en/math/topology/other_concepts#prop4){: data-lid="2iewu" }, $B$ is a closed set.
:::

## Subspaces and Continuous Functions

Let topological spaces $X,Y$ and a continuous function $f:X\rightarrow Y$ be given. Then for any set satisfying $f(X)\subseteq B\subseteq Y$, denoted $B$, the function obtained by restricting the codomain of $f$ to $B$ is continuous. This is trivial by [Definition 1](#def1){: data-lid="gjyvh" } and [§Initial and Final Topology, ⁋Proposition 3](/en/math/topology/initial_and_final_topology#prop3){: data-lid="8cb8m" }.

Now suppose, in the same setting as above, that a subset of $X$, $A$, is given. Then the restriction of $f:X\rightarrow Y$ to $A$, denoted $f\vert_A$, is, with respect to $\iota:A\hookrightarrow X$, equal to $f\circ\iota$. Since this is the composition of two continuous functions, we clearly see that $f\vert_A$ is also continuous. However, the converse does not hold in general.

::: Example 7
Suppose that a function between two topological spaces $f:X\rightarrow Y$ is not continuous. For any $x\in X$, if we set $A=\{x\}$, then $f\vert_A$ is continuous. This is because for any open set in $Y$, $U$, $(f\vert_A)^{-1}(U)$ is always either the empty set or $\{x\}$.
:::

Instead, if the set $A$ is a neighborhood of $x$, then the continuity of $f\vert_A$ at the point $x\in X$ implies that $f$ is continuous at $x$. This is because by [Lemma 4](#lem4){: data-lid="z1sia" }, a neighborhood of $x$ in $A$ can always be viewed as a neighborhood in $X$. To use this argument to show that the function $f$ is continuous at all points, one would have to choose for each $x\in X$ a neighborhood $N(x)$ and prove that $f\vert_{N(x)}$ is necessarily continuous; however, by the following proposition, we can prove that $f$ is continuous using even weaker information.

::: Proposition 8
Let $X$ be a topological space and let $(A_i)_{i\in I}$ be a collection of subsets satisfying one of the conditions of [Proposition 6](#prop6){: data-lid="fysbg" }. Then, for any topological space $Y$, an arbitrary function $f:X\rightarrow Y$ is continuous if and only if all $f\vert_{A_i}$ are continuous.
:::
::: Proof
It suffices to assume that all $f\vert_{A_i}$ are continuous and show that $f$ is continuous. In $Y$, choose an arbitrary closed set $B$, and let $A=f^{-1}(B)$. Since all $f\vert_{A_i}$ are continuous, $(f\vert_{A_i})^{-1}(B)=A\cap A_i$ are all closed sets in $A_i$. From this, applying [Proposition 6](#prop6){: data-lid="i9fpp" }, we see that $A$ is closed, and therefore $f$ is continuous.
:::

---

**References**

**[Bou]** N. Bourbaki, <i>General Topology</i>. Elements of mathematics. Springer, 1995.
