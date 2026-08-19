---
title: "Interior, Closure, and Boundary"
description: "This post covers the definitions of closed sets, interior, closure, and boundary in a topological space, and explains how these determine the topology through the closure operation."
excerpt: "Basic concepts in topology"

categories: [Math / Topology]
permalink: /en/math/topology/other_concepts
sidebar: 
    nav: "topology-en"

date: 2022-11-09
weight: 3
translated_at: 2026-08-19T21:15:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-08-19T21:15:04+00:00
---
Before we begin treating continuous functions, sequences, and related notions in earnest, we introduce the remaining language of topology.

## Closed Sets

::: Definition 1
For a topological space $X$, a set $A$ is called a *closed set* if its complement $A^c = X \setminus A$ is an open set.
:::

In any topology $\mathcal{T}$ on $X$, both $\emptyset$ and $X$ are simultaneously open and closed, and if the discrete topology is given then every subset is simultaneously open and closed. Thus closed sets and open sets are not opposite concepts; rather, they are closer to being the same thing expressed in different ways. For instance, a topology $\mathcal{T}$ can in fact be defined using closed sets as follows.

::: Proposition 2
Suppose a collection $\mathcal{C}$ on a set $X$ is given satisfying the following conditions.

1. $\emptyset$, $X\in\mathcal{C}$
2. $\mathcal{C}$ is closed under arbitrary intersections.
3. $\mathcal{C}$ is closed under *finite* unions.

Then there exists a unique topology $\mathcal{T}$ whose open sets are exactly the complements of the elements of $\mathcal{C}$.
:::
::: Proof
From De Morgan's laws ([\[Set Theory\] §Union and Intersection, ⁋Proposition 8](/en/math/set_theory/union_and_intersection#prop8))

$$\left(\bigcap A_i\right)^c=\bigcup A_i^c,\quad\left(\bigcup A_i\right)^c=\bigcap A_i^c$$

the correspondence taking complements reverses inclusion and translates conditions 1, 2, and 3 into the three axioms for $\mathcal{T}=\{C^c\mid C\in\mathcal{C}\}$ to be a topology, and since the collection of open sets is determined by this $\mathcal{T}$, uniqueness follows as well.
:::

The third condition of the preceding proposition can be refined further.

::: Definition 3
Let a topological space $X$ be given, and let $(A_i)_{i\in I}$ be a family of subsets of $X$. Then $(A_i)$ is called *locally finite* if for every $x\in X$, there exists a neighborhood $V$ such that the set of indices $i$ with $V\cap A_i\neq\emptyset$ is finite.
:::

That any finite family is locally finite is obvious, so the above definition can be regarded as a generalization of finite families. The following holds.

::: Proposition 4
Let a topological space $X$ be given. If $(A_i)_{i\in I}$ is a locally finite collection of closed sets, then $A=\bigcup A_i$ is a closed set.
:::
::: Proof
To show this, it suffices to prove that $A^c$ is an open set. Let $x\in A^c$. Then $x\in A_i^c$ holds for all $i$. On the other hand, since $(A_i)$ is locally finite, there exists a neighborhood $V$ of $x$ such that the indices $i$ satisfying $V\cap A_i\neq\emptyset$ are only finitely many. Let $J$ be the subset of $I$ consisting of such indices. Then for every $j\in J$, each $A_j^c$ is an open set, and therefore the following set

$$V\cap\bigcap_{j\in J} A_j^c$$

is a neighborhood of $x$ and is a subset of $A^c$. From this we see that $A^c$ is an open set, and hence $A$ is a closed set.
:::

## Interior and Closure of a Set

Let a topological space $(X,\mathcal{T})$ be given. For any subset $A$ of $X$, there always exist <phrase>a closed set containing $A$</phrase> and <phrase>an open set contained in $A$</phrase>. ($X$ and $\emptyset$). On the other hand, since an arbitrary intersection of closed sets is closed and an arbitrary union of open sets is open, there exist both <phrase>the smallest closed set containing $A$</phrase> and <phrase>the largest open set contained in $A$</phrase>. We define them as follows.

::: Definition 5
For any subset $A$ of a topological space $X$, we call the smallest closed set containing $A$ the *closure* of $A$, and the largest open set contained in $A$ the *interior* of $A$, and denote them by $\cl(A)$ and $\interior(A)$, respectively.
:::

With this definition, it is obvious that the two operators $\cl$ and $\interior$ preserve inclusion.

Let us prove the identity

$$\interior(A^c)=(\cl(A))^c.$$

By definition, $\interior(A^c)$ is the largest open set contained in $A^c$, which is the same as saying the largest open set disjoint from $A$. On the other hand, $\cl(A)$ is the smallest closed set containing $A$, so $(\cl(A))^c$ is the largest open set disjoint from $A$; hence the two must be equal. We call this set the *exterior* of $A$.

The same argument shows that if we have any one of interior, closure, or exterior, we can construct the other two.

Consider the interior of a set $A$. The statement $x\in\interior(A)$ means that there exists an open set $U$ containing $x$ and contained in $A$, which is equivalent to saying that $A$ is a neighborhood of $x$. Therefore, for any two sets $A,B$, the condition $x\in\interior(A\cap B)$ is equivalent to $x\in\interior(A)\cap\interior(B)$. (The second condition of [§Open Sets, ⁋Proposition 6](/en/math/topology/open_sets#prop6).) Translating this into a proposition about closure via the method explained above, we obtain the equality

$$\cl(A\cup B)=\cl(A)\cup\cl(B).$$

::: Proposition 6
For a topological space $X$ and a subset $A$, the following two conditions are equivalent:

1. $x\in\cl A$,
2. every neighborhood $U$ of $x$ meets $A$.

:::
::: Proof
It is convenient to prove the contrapositive. Suppose $x\not\in\cl A$. Then $(\cl A)^c=\ext A$ contains $x$, is an open set disjoint from $\cl A$, and hence also disjoint from $A$. That is, the statement <phrase>there exists a neighborhood of $x$ that does not meet $A$</phrase> is true.

Conversely, suppose there exists a neighborhood of $x$ that does not meet $A$. Then there is an open neighborhood $U$ of $x$ contained in this neighborhood such that $U$ does not meet $A$, so $U\cap A=\emptyset$. Now $U^c\cap A=A$, so $U^c$ is a closed set containing $A$, and by the minimality of the closure, $U^c$ also contains $\cl A$. Hence, if $x\not\in U^c$ then $x\not\in\cl A$, and therefore the reverse direction also holds.  
:::

::: Corollary 7
Let a topological space $X$ be given. For an open set $A$ and an arbitrary set $B$, the following identity

$$A\cap\cl(B)\subseteq\cl(A\cap B)$$

holds.
:::
::: Proof
Suppose $x\in A\cap\cl(B)$. Since $A$ is an open neighborhood of $x$, for any neighborhood $V$ of $x$, the intersection $V\cap A$ is also a neighborhood of $x$. Thus, from the fact that $x\in\cl(B)$ and [Proposition 6](#prop6), we know that $(V\cap A)\cap B\neq\emptyset$. However, this can also be interpreted as saying that the intersection of $A\cap B$ and $V$ is nonempty, and since $V$ is an arbitrary neighborhood of $x$, we again have $x\in\cl(A\cap B)$ by [Proposition 6](#prop6).
:::

::: Definition 8
For a topological space $X$ and any subset $A$ of $X$, a point $x\in X$ is called a *limit point* of $A$ if every neighborhood of $x$ meets $A$ at some point other than $x$ itself.
:::

Then $\cl(A)$ is the union of $A$ and the limit points of $A$. If $x\in\cl(A)\setminus A$, then by [Proposition 6](#prop6) the point $x$ must be a limit point of $A$; conversely, any limit point of $A$ belongs to $\cl(A)$ by [Proposition 6](#prop6) again, because every neighborhood of it meets $A$. On the other hand, if $x\in A$ this need not hold. If, for $x\in A$, there exists a neighborhood $V$ such that $V\cap A=\{x\}$, then we call $x$ an *isolated point* of $A$. A closed set with no isolated points is called a *perfect set*.

## Boundary of a Set

::: Definition 9
For any subset $A$ of a topological space $X$, the *boundary* of $A$ is the set $\partial A$ defined by the equation

$$\partial A=\cl A\setminus\interior A$$

:::

Thus $\partial A$ is a closed set.

## Dense Sets

::: Definition 10
A subset $A$ of a topological space $X$ is called a *dense subset* if $\cl(A)=X$.
:::

By [Proposition 6](#prop6), the condition that $A$ is dense in $X$ means that every nonempty open subset of $X$ must intersect $A$. Intuitively, one may think that if we find a dense subset of $X$, then we can recover all of $X$ with only a slight perturbation. In more everyday language, a dense subset of $X$ can be thought of as containing "almost all" of $X$.

On the other hand, in topology the notion of size is also given by the cardinality of a base, as shown in the following proposition.

::: Proposition 11
For a base $\mathcal{B}$ of a topological space $X$, there exists a dense subset $D$ of $X$ such that $\card(D)\leq\card(\mathcal{B})$.
:::
::: Proof
For each nonempty $U\in\mathcal{B}$, choose an element $x_U\in U$, and let $D$ be the collection of these elements. That $D$ is dense follows because for any nonempty open set $V$, we can express $V$ as a union of elements of $\mathcal{B}$, and this union must contain some $x_U$, so $V\cap D\neq\emptyset$.
:::

---

**References**

**[Bou]** N. Bourbaki, <i>General Topology</i>. Elements of mathematics. Springer, 1995.
