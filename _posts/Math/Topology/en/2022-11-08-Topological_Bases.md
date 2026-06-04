---
title: "Bases of a Topological Space"
description: "This post introduces the definition of a basis and subbasis for a topological space, proves three equivalent conditions for a collection to be a basis, and explains how to construct a topology from a basis on an arbitrary set."
excerpt: "Bases, subbases, and local bases of a topological space"

categories: [Math / Topology]
permalink: /en/math/topology/topological_bases
sidebar: 
    nav: "topology-en"

date: 2022-11-08
last_modified_at: 2022-11-08
weight: 2
translated_at: 2026-06-03T01:00:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-03T01:00:02+00:00
---
## Bases and Subbases of a Topological Space

The most straightforward way to specify a topological space is to list all open sets and thereby give the topology $$\mathcal{T}$$, but the entire collection $$\mathcal{T}$$ is not needed for this. For instance, if an open set $$U=\bigcup U_i$$ is given, and for every $$i$$ we have $$U\neq U_i$$ and $$U_i\in\mathcal{T}$$, then the information that $$U\in\mathcal{T}$$ may be regarded as redundant.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Let $$(X,\mathcal{T})$$ be a topological space. A subset $$\mathcal{B}$$ of $$\mathcal{T}$$ is called a *base* for $$\mathcal{T}$$ if for every $$U\in\mathcal{T}$$, there exists a family $$(B_i)_{i\in I}$$ of elements of $$\mathcal{B}$$ such that $$U=\bigcup_{i\in I} B_i$$.

</div>

In particular, since $$X\in\mathcal{T}$$, the collection $$\mathcal{B}$$ is also a covering of $$X$$. ([[Set Theory] §Sum of Sets, ⁋Definition 1](/en/math/set_theory/sum_of_sets#def1)) Since the elements of $$\mathcal{B}$$ are all open sets by definition, it is appropriate to say that $$\mathcal{B}$$ is an *open covering* of $$X$$.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> Let $$(X,\mathcal{T})$$ be a topological space. Then $$\mathcal{B}$$ is a base for $$\mathcal{T}$$ if and only if the following three conditions are satisfied:

1. For each $$x\in X$$, there exists at least one $$B\in\mathcal{B}$$ such that $$x\in B$$;
2. If there exist two elements $$B_1,B_2\in\mathcal{B}$$ containing $$x$$, then there exists another $$B_3\in\mathcal{B}$$ such that $$x\in B_3$$ and $$B_3\subseteq B_1\cap B_2$$;
3. For each $$U\in\mathcal{T}$$ and $$x\in U$$, there exists $$B\in\mathcal{B}$$ such that $$x\in B\subseteq U$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, assume that $$\mathcal{B}$$ is a base for $$\mathcal{T}$$. Then $$\mathcal{B}$$ is an open covering of $$X$$, so condition 1 is trivially satisfied.

On the other hand, if $$B_1$$ and $$B_2$$ are given as in condition 2, then $$B_1\cap B_2$$ is also an open set, so there exists a family $$(B_i)_{i\in I}$$ of elements of $$\mathcal{B}$$ such that $$B_1\cap B_2=\bigcup_{i\in I} B_i$$. Since $$(B_i)_{i\in I}$$ is an open covering of $$B_1\cap B_2$$, condition 2 is also trivially satisfied, just as condition 1. Replacing $$B_1\cap B_2$$ with an arbitrary open set $$U$$ yields condition 3.

Conversely, assume that the three conditions are satisfied and pick an arbitrary open set $$U$$. Then for each $$x\in U$$, condition 3 implies that there exists $$B_x\in\mathcal{B}$$ such that $$x\in B_x\subseteq U$$. Now $$U=\bigcup_{x\in U} B_x$$, which completes the proof.

</details>

From the above proposition, the following question arises naturally.

> Let $$X$$ be an arbitrary set, and let $$\mathcal{B}$$ be a subset of $$\mathcal{P}(X)$$ satisfying the above conditions. Can we endow $$X$$ with a topology $$\mathcal{T}$$ so that $$(X,\mathcal{T})$$ is a topological space having $$\mathcal{B}$$ as a base?

The answer to this question is affirmative. **[Mun]** gives a direct proof of this, but we will first define a local base and then prove it in a simpler way.

Meanwhile, by refining [Definition 1](#def1), we can define a *subbase* as follows.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> A *subbase* for a topological space $$(X,\mathcal{T})$$ is an open covering $$\mathcal{S}$$ of $$X$$ such that for every $$U\in\mathcal{T}$$, there exists $$S\in\mathcal{S}$$ with $$S\subseteq U$$.

</div>

Collecting all finite intersections of elements of $$\mathcal{S}$$, we obtain a new collection $$\mathcal{B}$$. To check whether this collection is a base, we only need condition 2; but since the elements of $$\mathcal{B}$$ are obtained as finite intersections of elements of $$\mathcal{S}$$, the intersection $$B_1\cap B_2$$ is again a finite intersection of elements of $$\mathcal{S}$$, and hence $$\mathcal{B}$$ is a base.

## Local Bases of a Topological Space

[§Open Sets, ⁋Proposition 6](/en/math/topology/open_sets#prop6) shows that if we can describe the neighborhood filter $$\mathcal{N}(x)$$ centered at a point $$x$$ in a topological space $$X$$, then we can completely recover the topology of $$X$$. On the other hand, since $$\mathcal{N}(x)$$ satisfies the conditions of [§Open Sets, ⁋Proposition 6](/en/math/topology/open_sets#prop6), in particular the first condition, we do not need all of $$\mathcal{N}(x)$$ to describe it.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> Let $$X$$ be a topological space and let $$A$$ be a subset of $$X$$. A *local base* at $$A$$ is a coinitial subset of $$(\mathcal{N}(A),\subseteq)$$ consisting of open sets. ([[Set Theory] §Elements of Ordered Sets](/en/math/set_theory/elements_in_ordered_set))

</div>

As in [§Open Sets, ⁋Definition 4](/en/math/topology/open_sets#def4), when $$A$$ is a singleton $$\{x\}$$, we call a local base at $$A$$ a local base at the point $$x$$. Then the following holds.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> Let $$(X,\mathcal{T})$$ be a topological space. Then a subset $$\mathcal{B}$$ of $$\mathcal{T}$$ is a base for $$X$$ if and only if for each $$x\in X$$, the <phrase>elements of $\mathcal{B}$ containing $x$</phrase> form a local base at $$x$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

For convenience, let us denote by $$\mathcal{B}(x)$$ the <phrase>collection of elements of $\mathcal{B}$ containing $x$</phrase>.

First, suppose that $$\mathcal{B}$$ is a base for $$X$$, and pick an arbitrary point $$x\in X$$ and a neighborhood $$V$$. Then there exists an open set $$U$$ such that $$x\in U\subseteq V$$. Since $$\mathcal{B}$$ is a base for $$X$$, there exist $$U_i\in\mathcal{B}$$ such that $$U=\bigcup U_i$$. Since $$x\in U$$, we have $$x\in U_i$$ for some $$i$$, and therefore $$U_i\in\mathcal{B}(x)$$.

Conversely, suppose that $$\mathcal{B}$$ satisfies the given condition and let $$U$$ be an arbitrary open set. Then for any $$x\in U$$, we have $$U\in\mathcal{N}(x)$$, so the given condition yields a suitable $$V(x)\in\mathcal{B}(x)$$ such that $$x\in V(x)\subseteq U$$. Now $$U=\bigcup V(x)$$, which gives the desired result.

</details>

Earlier we asked whether, given an arbitrary collection satisfying the first and second conditions of [Proposition 2](#prop2), there exists a topology on $$X$$ having it as a base. This becomes an easy corollary of the above proposition.

<div class="proposition" markdown="1">

<ins id="cor6">**Corollary 6**</ins> Let $$X$$ be a set, and let $$\mathcal{B}$$ be a subset of $$\mathcal{P}(X)$$ satisfying the following two conditions.

1. For each $$x$$, there exists at least one $$B\in\mathcal{B}$$ such that $$x\in B$$.
2. If there exist $$B_1,B_2\in\mathcal{B}$$ containing $$x$$, then there exists another $$B_3\in\mathcal{B}$$ such that $$x\in B_3\subseteq B_1\cap B_2$$.

Then there exists a unique topology $$\mathcal{T}$$ on $$X$$ such that $$\mathcal{B}$$ is a base for this topology $$\mathcal{T}$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Define $$\mathcal{B}(x)$$ to be the <phrase>collection of elements of $\mathcal{B}$ containing $x$</phrase>, just as in the proof of the previous proposition. Also define

$$\mathcal{N}(x)=\mathop{\uparrow}\mathcal{B}(x):=\bigcup_{B\in\mathcal{B}}\mathop{\uparrow}B$$

That is, $$\mathcal{N}(x)$$ is the collection containing every element of $$\mathcal{B}$$ that contains the given $$x\in X$$, together with all elements of $$\mathcal{P}(X)$$ larger than it.

- For any $$V\in\mathcal{N}(x)$$, suppose $$V\subseteq V'$$. By the definition of $$\mathcal{N}(x)$$, there exists $$U\in\mathcal{B}(x)$$ such that $$U\subseteq V$$, and for such $$U$$ we have $$U\subseteq V'$$, so $$V'\in\mathcal{N}(x)$$.
- Suppose that elements $$V_1,\ldots,V_n$$ of $$\mathcal{N}(x)$$ are given. Then there exist $$U_i\in\mathcal{B}(x)$$ such that $$U_i\subseteq V_i$$. Using the second condition of [Proposition 2](#prop2) inductively, we can find a suitable $$U\in\mathcal{B}(x)$$ such that $$U\subseteq U_1\cap\cdots\cap U_n$$. In particular, $$U\subseteq V_1\cap\cdots\cap V_n$$, so $$V_1\cap\cdots\cap V_n\in\mathcal{N}(x)$$.
- For any element $$V$$ of $$\mathcal{N}(x)$$, there exists $$W\in\mathcal{B}(x)$$ such that $$W\subseteq V$$, so $$x\in V$$.
- For any element $$V$$ of $$\mathcal{N}(x)$$, pick $$W\in\mathcal{B}(x)$$ such that $$W\subseteq V$$. Then $$W\in\mathcal{B}$$, and therefore $$W\in\mathcal{B}(y)$$ for any $$y\in W$$. Since $$W\subseteq V$$, it follows that $$V\in\mathcal{N}(y)$$ for all $$y$$.

Now we can apply [§Open Sets, ⁋Proposition 6](/en/math/topology/open_sets#prop6) to obtain a topology $$\mathcal{T}$$, and in this topological space $$\mathcal{B}(x)$$ is a local base at $$x$$, so by [Proposition 5](#prop5), $$\mathcal{B}$$ is a base for $$\mathcal{T}$$.

</details>

The topology obtained from $$\mathcal{B}$$ through this process is called the topology generated by $$\mathcal{B}$$. Similarly, we make a base from a subbase $$\mathcal{S}$$, and the topology generated by this base is called the topology obtained from $$\mathcal{S}$$.

---

**References**

**[Bou]** N. Bourbaki, <i>General Topology</i>. Elements of mathematics. Springer, 1995.  
**[Mun]** J.R. Munkres, <i>Topology</i>. Featured Titles for Topology. Prentice Hall, Incorporated, 2000.

---
