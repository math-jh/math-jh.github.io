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
last_polished_at: 2026-11-08T03:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
Before we begin treating concepts such as continuous functions and sequences in earnest, we introduce the remaining language used in topology.

## Closed Sets

::: Definition 1
For a topological space $X$, that a set $A$ is a *closed set* means that the complement of $A$, $A^c=X\setminus A$, is an open set.
:::

On $X$, in any topology $\mathcal{T}$, both $\emptyset$ and $X$ are simultaneously open and closed, and if the discrete topology is given, any subset is simultaneously open and closed. Thus closed sets and open sets are not opposite concepts; rather, they are closer to being the same thing expressed in different ways. For instance, a topology $\mathcal{T}$ can in fact be defined using closed sets as follows.

::: Proposition 2
Suppose that on a set $X$, a collection $\mathcal{C}$ satisfying the following conditions is given.

1. $\emptyset$, $X\in\mathcal{C}$
2. $\mathcal{C}$ is closed under arbitrary intersections.
3. $\mathcal{C}$ is closed under *finite* unions.

Then, with precisely the complements of the elements of $\mathcal{C}$ as its open sets, there exists a unique topology $\mathcal{T}$.
:::
::: Proof
From De Morgan's laws ([\[Set Theory\] §Union and Intersection, ⁋Proposition 8](/en/math/set_theory/union_and_intersection#prop8){: data-lid="zn8cs" })

$$\left(\bigcap A_i\right)^c=\bigcup A_i^c,\quad\left(\bigcup A_i\right)^c=\bigcap A_i^c$$

the correspondence taking complements reverses inclusion and translates conditions 1, 2, and 3 into the three axioms for $\mathcal{T}=\{C^c\mid C\in\mathcal{C}\}$ to be a topology, and since the collection of open sets is determined by this $\mathcal{T}$, uniqueness follows as well.
:::

The third condition of the preceding proposition can be refined further.

::: Definition 3
Let a topological space $X$ be given, and let a family of subsets of $X$, $(A_i)_{i\in I}$, be given. Then $(A_i)$ is called *locally finite* if for every $x\in X$, there exists a neighborhood $V$ such that $V\cap A_i\neq\emptyset$ holds for only finitely many $i$.
:::

That any finite family is locally finite is obvious, so the above definition can be regarded as a generalization of finite families. The following holds.

::: Proposition 4
Let a topological space $X$ be given. If $(A_i)_{i\in I}$ is a locally finite collection of closed sets, then $A=\bigcup A_i$ is a closed set.
:::
::: Proof
To show this, it suffices to prove that $A^c$ is an open set. Let $x\in A^c$. Then $x\in A_i^c$ holds for all $i$. On the other hand, since $(A_i)$ is locally finite, $x$ has a neighborhood $V$ such that $V\cap A_i\neq\emptyset$ holds for only finitely many $i$. Let the set of such $i$, which is a subset of $I$, be $J$. Then for every $j\in J$, each $A_j^c$ is an open set, and therefore the following set

$$V\cap\bigcap_{j\in J} A_j^c$$

is a neighborhood of $x$ and is a subset of $A^c$. From this we see that $A^c$ is an open set, and hence $A$ is a closed set.
:::

## Interior and Closure of a Set

Let a topological space $(X,\mathcal{T})$ be given. For any subset of $X$, $A$, there always exist a closed set containing $A$ and an open set contained in $A$. ($X$ and $\emptyset$). On the other hand, since an arbitrary intersection of closed sets is closed and an arbitrary union of open sets is open, there exist both the smallest closed set containing $A$ and the largest open set contained in $A$. We define them as follows.

::: Definition 5
For a topological space $X$ and any subset $A$, we call the smallest closed set containing $A$ the *closure* of $A$, and the largest open set contained in $A$ the *interior* of $A$, and denote them by $\cl(A)$ and $\interior(A)$, respectively.
:::

With this definition, it is obvious that the two operators $\cl$ and $\interior$ preserve inclusion.

Let us prove the identity

$$\interior(A^c)=(\cl(A))^c$$

By definition, $\interior(A^c)$ is the largest open set contained in $A^c$, which is equivalent to saying that it is the largest open set disjoint from $A$. Meanwhile, $\cl(A)$ is the smallest closed set containing $A$, and thus $(\cl(A))^c$ is the largest open set disjoint from $A$, so the two must be identical. We call this set the *exterior* of $A$.

Through the argument above, we know that given any one of interior, closure, or exterior, we can construct the other two.

Consider the interior of a set $A$. That $x\in\interior(A)$ means that containing $x$ and contained in $A$, there exists an open set $U$, which is therefore equivalent to $A$ being a neighborhood of $x$. Therefore, for any two sets $A,B$, the condition $x\in\interior(A\cap B)$ is equivalent to $x\in\interior(A)\cap\interior(B)$. (The second condition of [§Open Sets, ⁋Proposition 6](/en/math/topology/open_sets#prop6){: data-lid="k6cox" }.) Translating this into a proposition about closure following the method explained above, we obtain the equality

$$\cl(A\cup B)=\cl(A)\cup\cl(B)$$

::: Proposition 6
For a topological space $X$ and a subset $A$, the two conditions

1. $x\in\cl A$,
2. for $x$, every neighborhood $U$ meets $A$

are equivalent.
:::
::: Proof
It is convenient to prove the contrapositive. Suppose $x\not\in\cl A$. Then $(\cl A)^c=\ext A$ contains $x$, is an open set disjoint from $\cl A$, and hence is an open set disjoint from $A$ as well. That is, the proposition "there exists, disjoint from $A$, some neighborhood of $x$" is true.

Conversely, suppose there exists, disjoint from $A$, some neighborhood of $x$. Then an open neighborhood of $x$, $U$, contained in this neighborhood does not meet $A$, so $U\cap A=\emptyset$. Now $U^c\cap A=A$, so $U^c$ is a closed set containing $A$, and by the minimality of the closure, $U^c$ also contains $\cl A$. That is, if $x\not\in U^c$, then $x\not\in\cl A$, and therefore the reverse direction also holds.  
:::

::: Corollary 7
Let a topological space $X$ be given. For an open set $A$ and an arbitrary set $B$, the following inclusion

$$A\cap\cl(B)\subseteq\cl(A\cap B)$$

holds.
:::
::: Proof
Suppose $x\in A\cap\cl(B)$. Since $A$ is an open neighborhood of $x$, for any neighborhood of $x$, $V$, the intersection $V\cap A$ is also a neighborhood of $x$. Thus, from $x\in\cl(B)$ and [Proposition 6](#prop6){: data-lid="wqi0e" }, we know that $(V\cap A)\cap B\neq\emptyset$. However, this can also be interpreted as saying that the intersection of $A\cap B$ and $V$ is nonempty, and since $V$ is an arbitrary neighborhood of $x$, we again have $x\in\cl(A\cap B)$ by [Proposition 6](#prop6){: data-lid="l47zu" }.
:::

::: Definition 8
For a topological space $X$ and any subset of $X$, $A$, we say that $x\in X$ is a *limit point* of $A$ if every neighborhood of $x$, at a point other than $x$ itself, meets $A$.
:::

Then $\cl(A)$ is the union of the limit points of $A$ and $A$. If $x\in\cl(A)\setminus A$, then by [Proposition 6](#prop6){: data-lid="dt0j8" } the point $x$ must be a limit point of $A$; conversely, since every neighborhood of a limit point of $A$ meets $A$, we know by [Proposition 6](#prop6){: data-lid="o8n4l" } again that it belongs to $\cl(A)$. On the other hand, if $x\in A$, this need not be true. As such, if for $x\in A$ there exists a neighborhood $V$ such that $V\cap A=\{x\}$, we call $x$ an *isolated point* of $A$. A closed set having no isolated points is called a *perfect set*.

## Boundary of a Set

::: Definition 9
For a topological space $X$ and any subset $A$, the *boundary* of $A$ is defined by the following equation

$$\partial A=\cl A\setminus\interior A$$

to be the set $\partial A$.
:::

Thus $\partial A$ is a closed set.

## Dense Sets

::: Definition 10
For a topological space $X$, a subset $A$ is called a *dense subset* if $\cl(A)=X$.
:::

By [Proposition 6](#prop6){: data-lid="yleva" }, the condition that $A$ is dense in $X$ means that every nonempty open subset of $X$ must intersect $A$. Intuitively, one may think that if we find a dense subset of $X$, then we can recover all of $X$ with only a slight perturbation. In more everyday language, a dense subset of $X$ can be thought of as containing "almost all" of $X$.

On the other hand, in topology the notion of size is also given by the cardinality of a base, as shown in the following proposition.

::: Proposition 11
For a topological space $X$ and a base $\mathcal{B}$, there exists, satisfying $\card(D)\leq\card(\mathcal{B})$, a dense subset of $X$, $D$.
:::
::: Proof
For each nonempty $U\in\mathcal{B}$, choose an element $x_U\in U$, and let $D$ be the collection of these elements. That the set $D$ is dense follows because for any nonempty open set $V$, we can express it as a union of elements of $\mathcal{B}$, and this union must contain some $x_U$, so $V\cap D\neq\emptyset$.
:::

---

**References**

**[Bou]** N. Bourbaki, <i>General Topology</i>. Elements of mathematics. Springer, 1995.
