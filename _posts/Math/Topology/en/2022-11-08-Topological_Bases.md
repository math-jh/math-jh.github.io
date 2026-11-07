---
title: "Bases of a Topological Space"
description: "This post introduces the definitions of a basis and subbasis for a topological space and proves three equivalent conditions for being a basis. It also examines how to construct a topology using a basis on an arbitrary set."
excerpt: "Bases, subbases, and local bases of a topological space"

categories: [Math / Topology]
permalink: /en/math/topology/topological_bases
sidebar: 
    nav: "topology-en"

date: 2022-11-08
weight: 2
translated_at: 2026-06-03T01:00:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-11-07T19:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
## Bases and Subbases of a Topological Space

The most definitive way to express a topological space is to give the topological structure $\mathcal{T}$ by listing all open sets, but the entirety of $\mathcal{T}$ is not required for this. For instance, if for some open set $U=\bigcup U_i$, it is known that for all $i$ we have $U\neq U_i$ and $U_i\in\mathcal{T}$, then the information that $U\in\mathcal{T}$ can be thought of as unnecessarily redundant information.

::: Definition 1
For a topological space $(X,\mathcal{T})$, that a subset $\mathcal{B}$ of $\mathcal{T}$ is a *base* for $\mathcal{T}$ means that for any $U\in\mathcal{T}$, there exists, satisfying $U=\bigcup_{i\in I} B_i$, a family of elements of $\mathcal{B}$, $(B_i)_{i\in I}$.
:::

In particular, since $X\in\mathcal{T}$, $\mathcal{B}$ is also a covering of $X$. ([\[Set Theory\] §Sum of Sets, ⁋Definition 1](/en/math/set_theory/sum_of_sets#def1){: data-lid="y9yup" }) By definition, the elements of $\mathcal{B}$ are all open sets, so it is appropriate to say that $\mathcal{B}$ is an *open covering* of $X$.

::: Proposition 2
For a topological space $(X,\mathcal{T})$, that $\mathcal{B}$ is a base for $\mathcal{T}$ is equivalent to satisfying the three conditions:

1. For each $x\in X$, there exists at least one $B\in \mathcal{B}$ such that $x\in B$;
2. For any two elements containing $x$ from $\mathcal{B}$, $B_1$, $B_2$, there exists another $B_3\in\mathcal{B}$ such that $x\in B_3$ and $B_3\subseteq B_1\cap B_2$;
3. For each $U\in\mathcal{T}$ and $x\in U$, there exists, satisfying $x\in B\subseteq U$, a $B\in\mathcal{B}$.
:::
::: Proof
First, assume that $\mathcal{B}$ is a base for $\mathcal{T}$. Then, since $\mathcal{B}$ is an open covering of $X$, condition 1 holds trivially.

Meanwhile, if $B_1$, $B_2$ are given as in condition 2, then $B_1\cap B_2$ is also an open set, so there exists, satisfying $B_1\cap B_2=\bigcup_{i\in I} B_i$, a family of elements of $\mathcal{B}$, $(B_i)_{i\in I}$. Here, since $(B_i)_{i\in I}$ is an open covering of $B_1\cap B_2$, condition 2 holds trivially, just as condition 1. Replacing $B_1\cap B_2$ here with an arbitrary open set $U$ yields condition 3.

Conversely, assume that the three conditions are satisfied, and choose an arbitrary open set $U$. Then for $x\in U$, by condition 3 there exists, satisfying $x\in B_x\subseteq U$, some $B_x\in\mathcal{B}$. Now since $U=\bigcup_{x\in U} B_x$, the proof is complete.  
:::

From the above proposition, the following question arises naturally.

> Suppose that for an arbitrary *set* $X$, a subset of $\mathcal{P}(X)$, $\mathcal{B}$, satisfying the preceding conditions is given. Then, by endowing $X$ with a topology $\mathcal{T}$, can $(X,\mathcal{T})$ be regarded as a topological space with base $\mathcal{B}$?

The answer to this question is affirmative; although **[Mun]** proved this directly, we will prove it in a simpler way after defining a local base.

Meanwhile, by further refining [Definition 1](#def1){: data-lid="v70fw" }, we can define a *subbase* as follows.

::: Definition 3
For a topological space $(X,\mathcal{T})$, a *subbase* $\mathcal{S}$ means, for any $U\in\mathcal{T}$, that $S\subseteq U$ holds for some $S\in\mathcal{S}$, forming an open covering of $X$.
:::

By collecting finite intersections of elements of $\mathcal{S}$, we can form a new collection $\mathcal{B}$. To check whether this collection is a base, only condition 2 is needed; in any case, the elements of $\mathcal{B}$ are obtained as finite intersections of elements of $\mathcal{S}$, and therefore $B_1\cap B_2$ is still a finite intersection of elements of $\mathcal{S}$, so $\mathcal{B}$ is a base.

## Local Bases of a Topological Space

[§Open Sets, ⁋Proposition 6](/en/math/topology/open_sets#prop6){: data-lid="11lvo" } shows that for a topological space $X$ and a point $x$, if we can describe the neighborhood filter centered at $x$, $\mathcal{N}(x)$, then we can completely recover the topological structure of $X$. On the other hand, since $\mathcal{N}(x)$ satisfies the conditions of [§Open Sets, ⁋Proposition 6](/en/math/topology/open_sets#prop6){: data-lid="lengf" }, in particular the first condition, we do not need all of $\mathcal{N}(x)$ to describe this set.

::: Definition 4
For a topological space $X$ and a subset $A$, a *local base* at $A$ means a coinitial subset of $(\mathcal{N}(A),\subseteq)$ consisting of open sets. ([\[Set Theory\] §Elements of Ordered Sets](/en/math/set_theory/elements_in_ordered_set){: data-lid="7aqun" })
:::

As in [§Open Sets, ⁋Definition 4](/en/math/topology/open_sets#def4){: data-lid="3m9t1" }, when $A$ is a singleton $\{x\}$, a local base at $A$ is called a local base at the point $x$. Then the following holds.

::: Proposition 5
Let a topological space $(X,\mathcal{T})$ be given. Then a subset of $\mathcal{T}$, $\mathcal{B}$, is a base for $\mathcal{T}$ if and only if for each $x\in X$, the elements containing $x$ in $\mathcal{B}$ define a local base at $x$.
:::
::: Proof
For convenience, let us collect all elements of $\mathcal{B}$ containing $x$ and denote them by $\mathcal{B}(x)$.

First, suppose that $\mathcal{B}$ is a base for $\mathcal{T}$, and choose an arbitrary point $x\in X$ and a neighborhood $V$. Then there exists, satisfying $x\in U\subseteq V$, an open set $U$. Now, since $\mathcal{B}$ is a base for $\mathcal{T}$, there exist, satisfying $U=\bigcup U_i$, elements $U_i\in\mathcal{B}$. Since $x\in U$, for some $i$ we have $x\in U_i$, and therefore $U_i\in\mathcal{B}(x)$ and $U_i\subseteq U\subseteq V$.

Conversely, suppose that $\mathcal{B}$ satisfying the given condition is given, and let an arbitrary open set $U$ be given. Then for any $x\in U$, since $U\in\mathcal{N}(x)$, from the given condition there exists a suitable $V(x)\in\mathcal{B}(x)$ such that $x\in V(x)\subseteq U$. Now since $U=\bigcup V(x)$, we obtain the desired result.
:::

Earlier we asked whether, given an arbitrary collection satisfying the first and second conditions of [Proposition 2](#prop2){: data-lid="5uxv2" }, there exists a topology on $X$ having it as a base. This becomes an easy corollary of the above proposition.

::: Corollary 6
Let a set $X$ be given, and suppose that a subset of $\mathcal{P}(X)$, $\mathcal{B}$, satisfies the following two conditions.

1. For each $x$, there exists at least one $B\in\mathcal{B}$ such that $x\in B$.
2. For $x$ contained in any $B_1,B_2\in\mathcal{B}$, there exists another $B_3\in\mathcal{B}$ such that $x\in B_3\subseteq B_1\cap B_2$.

Then on $X$ there exists a unique topology $\mathcal{T}$ such that $\mathcal{B}$ is a base for this topology $\mathcal{T}$.
:::
::: Proof
Define $\mathcal{B}(x)$, as in the proof of the previous proposition, to be the collection of elements of $\mathcal{B}$ containing $x$. Also define

$$\mathcal{N}(x)=\mathop{\uparrow}\mathcal{B}(x):=\bigcup_{B\in\mathcal{B}(x)}\mathop{\uparrow}B$$

That is, $\mathcal{N}(x)$ is the collection containing, for the given $x\in X$, all elements of $\mathcal{B}$ containing it, as well as all elements of $\mathcal{P}(X)$ larger than these elements. ([\[Set Theory\] §Filters, Ideals, and Galois Connections, ⁋Example 2](/en/math/set_theory/filter_and_ideal#ex2){: data-lid="nd1nv" })

- For any $V\in\mathcal{N}(x)$, let $V\subseteq V'$. By the definition of $\mathcal{N}(x)$, we have $U\subseteq V$ for some $U\in\mathcal{B}(x)$, and for such $U$, since $U\subseteq V'$, we have $V'\in\mathcal{N}(x)$.
- Suppose elements of $\mathcal{N}(x)$, $V_1,\ldots, V_n$, are given. Then we have $U_i\subseteq V_i$ for some $U_i\in\mathcal{B}(x)$. Using the second assumption inductively, we see that there exists a suitable $U\in\mathcal{B}(x)$ such that $U\subseteq U_1\cap\cdots\cap U_n$. In particular, since $U\subseteq V_1\cap\cdots\cap V_n$, we have $V_1\cap\cdots\cap V_n\in\mathcal{N}(x)$.
- For any element of $\mathcal{N}(x)$, $V$, since we have $W\subseteq V$ for some $W\in\mathcal{B}(x)$, it follows that $x\in V$.
- For any element of $\mathcal{N}(x)$, $V$, choose an element satisfying $W\subseteq V$ with $W\in\mathcal{B}(x)$. Then $W\in\mathcal{B}$, and therefore for any $y\in W$ we have $W\in\mathcal{B}(y)$. Since $W\subseteq V$, from this we see that $V\in\mathcal{N}(y)$ holds for all $y\in W$.

Now we can apply [§Open Sets, ⁋Proposition 6](/en/math/topology/open_sets#prop6){: data-lid="tytud" } to obtain a topology $\mathcal{T}$, and since $\mathcal{B}(x)$ is a local base at $x$ in this topological space, by [Proposition 5](#prop5){: data-lid="r8rkd" }, $\mathcal{B}$ is a base for $\mathcal{T}$.
:::

The topology obtained from $\mathcal{B}$ through this process is called the topology generated by $\mathcal{B}$, and similarly, we form a base from a subbase $\mathcal{S}$, and the topology generated by this base is called the topology obtained from $\mathcal{S}$.

---

**References**

**[Bou]** N. Bourbaki, <i>General Topology</i>. Elements of mathematics. Springer, 1995.  
**[Mun]** J.R. Munkres, <i>Topology</i>. Featured Titles for Topology. Prentice Hall, Incorporated, 2000.

---
