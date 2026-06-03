---
title: "Interior, Closure, and Boundary"
description: "This post covers the definitions of closed sets, interior, closure, and boundary in a topological space, and explains how these determine the topology through the closure operation."
excerpt: "Basic concepts in topology"

categories: [Math / Topology]
permalink: /en/math/topology/other_concepts
header:
    overlay_image: /assets/images/Math/Topology/Other_Concepts.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology-en"

date: 2022-11-09
last_modified_at: 2022-11-09
weight: 3
translated_at: 2026-06-03T02:30:01+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-03T02:30:01+00:00
---
Before we take up continuous functions, sequences, and related notions in earnest, we complete the introduction of the language used in topology.

## Closed Sets

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> For a topological space $$X$$, a set $$A$$ is called a *closed set* if its complement $$A^c=X\setminus A$$ is an open set.

</div>

In any topology $$\mathcal{T}$$ on $$X$$, the sets $$\emptyset$$ and $$X$$ are simultaneously open and closed, and under the discrete topology every subset is both open and closed. Thus, closed sets and open sets are not opposite concepts; rather, they are nearly the same thing expressed in a different way. For instance, a topology $$\mathcal{T}$$ can in fact be defined using closed sets as follows.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> Let $$\mathcal{C}$$ be a collection of subsets of a set $$X$$ satisfying the following conditions.

1. $$\emptyset$$, $$X\in\mathcal{C}$$
2. $$\mathcal{C}$$ is closed under arbitrary intersections.
3. $$\mathcal{C}$$ is closed under <em>finite</em> unions.

Then there exists a unique topology $$\mathcal{T}$$ whose open sets are the complements of the elements of $$\mathcal{C}$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

This is immediate from the following De Morgan laws ([\[Set Theory\] §Unions and Intersections, ⁋Proposition 8](/en/math/set_theory/union_and_intersection#prop8))

$$\left(\bigcap A_i\right)^c=\bigcup A_i^c,\quad\left(\bigcup A_i\right)^c=\bigcap A_i^c$$

</details>

We can refine the third condition of the preceding proposition further.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> Let a topological space $$X$$ be given, and let $$(A_i)_{i\in I}$$ be a family of subsets of $$X$$. Then $$(A_i)$$ is called *locally finite* if for every $$x\in X$$ there exists a neighborhood $$V$$ such that the set of indices $$i$$ with $$V\cap A_i\neq\emptyset$$ is finite.

</div>

That any finite family is locally finite is obvious, so the above definition may be regarded as a generalization of finite families. The following holds.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> Let a topological space $$X$$ be given. If $$(A_i)_{i\in I}$$ is a locally finite collection of closed sets, then $$A=\bigcup A_i$$ is a closed set.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

To show this, it suffices to prove that $$A^c$$ is an open set. Let $$x\in A^c$$. Then $$x\in A_i^c$$ holds for all $$i$$. On the other hand, since $$(A_i)$$ is locally finite, there exists a neighborhood $$V$$ of $$x$$ such that the set of indices $$i$$ satisfying $$V\cap A_i\neq\emptyset$$ is finite. Let $$J$$ be the subset of $$I$$ consisting of such indices. Then for every $$j\in J$$, the set $$A_j^c$$ is open, and therefore the set

$$V\cap\bigcap_{j\in J} A_j^c$$

is a neighborhood of $$x$$ contained in $$A^c$$. Hence $$A^c$$ is open, and so $$A$$ is closed.

</details>

## Interior and Closure

Let a topological space $$(X,\mathcal{T})$$ be given. For any subset $$A$$ of $$X$$, there always exist <phrase>a closed set containing $A$</phrase> and <phrase>an open set contained in $A$</phrase> (namely $$X$$ and $$\emptyset$$). On the other hand, since arbitrary intersections of closed sets are closed and arbitrary unions of open sets are open, both <phrase>the smallest closed set containing $A$</phrase> and <phrase>the largest open set contained in $A$</phrase> exist. We define them as follows.

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> For any subset $$A$$ of a topological space $$X$$, the smallest closed set containing $$A$$ is called the *closure* of $$A$$, and the largest open set contained in $$A$$ is called the *interior* of $$A$$; we denote them by $$\cl(A)$$ and $$\interior(A)$$, respectively.

</div>

Defined in this way, it is obvious that the two operators $$\cl$$ and $$\interior$$ preserve inclusion.

Let us prove the identity

$$\interior(A^c)=(\cl(A))^c$$

By definition, $$\interior(A^c)$$ is the largest open set contained in $$A^c$$, which is the same as saying the largest open set not containing $$A$$. On the other hand, $$\cl(A)$$ is the smallest closed set containing $$A$$, so $$(\cl(A))^c$$ is the largest open set not containing $$A$$; hence the two must coincide. We call this set the *exterior* of $$A$$.

Through the above argument, we see that having any one of interior, closure, or exterior allows us to construct the other two.

Consider the interior of a set $$A$$. The statement $$x\in\interior(A)$$ means that there exists an open set $$U$$ containing $$x$$ and contained in $$A$$, which is equivalent to saying that $$A$$ is a neighborhood of $$x$$. Therefore, for any two sets $$A$$ and $$B$$, the statement $$x\in\interior(A\cap B)$$ is equivalent to $$x\in\interior(A)\cap\interior(B)$$. (The second condition of [§Open Sets, ⁋Proposition 6](/en/math/topology/open_sets#prop6)) Rewriting this as a statement about closures in the manner described above yields the identity

$$\cl(A\cup B)=\cl(A)\cup\cl(B)$$

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> For a topological space $$X$$ and a subset $$A$$, the following two conditions are equivalent:

1. $$x\in\cl A$$;
2. every neighborhood $$U$$ of $$x$$ meets $$A$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

It is convenient to prove the contrapositive. Suppose $$x\not\in\cl A$$. Then $$x\in(\cl A)^c=\ext A$$ is an open set containing $$x$$ and disjoint from $$\cl A$$, hence also disjoint from $$A$$. That is, the statement <phrase>there exists some neighborhood of $x$ disjoint from $A$</phrase> is true.

Conversely, suppose there exists some neighborhood of $$x$$ disjoint from $$A$$. Then there is an open neighborhood $$U$$ of $$x$$ contained in this neighborhood that does not meet $$A$$, so $$U\cap A=\emptyset$$. Now since $$U^c\cap A=A$$, the set $$U^c$$ is a closed set containing $$A$$, and by minimality of the closure, $$U^c$$ also contains $$\cl A$$. Hence if $$x\not\in U^c$$ then $$x\not\in\cl A$$, and the reverse direction also holds.

</details>

<div class="proposition" markdown="1">

<ins id="cor7">**Corollary 7**</ins> Let a topological space $$X$$ be given. For an open set $$A$$ and any set $$B$$, the following inclusion holds:

$$A\cap\cl(B)\subseteq\cl(A\cap B)$$

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$x\in A\cap\cl(B)$$. Since $$A$$ is an open neighborhood of $$x$$, for any neighborhood $$V$$ of $$x$$, the intersection $$V\cap A$$ is also a neighborhood of $$x$$. Therefore, from $$x\in\cl(B)$$ and [Proposition 6](#prop6), we know that $$(V\cap A)\cap B\neq\emptyset$$. But this can be interpreted as saying that the intersection of $$A\cap B$$ with $$V$$ is nonempty, and since $$V$$ is an arbitrary neighborhood of $$x$$, [Proposition 6](#prop6) again gives $$x\in\cl(A\cap B)$$.

</details>

<div class="definition" markdown="1">

<ins id="def8">**Definition 8**</ins> For a topological space $$X$$ and any subset $$A$$ of $$X$$, a point $$x\in X$$ is called a *limit point* of $$A$$ if every neighborhood of $$x$$ meets $$A$$ at some point other than $$x$$ itself.

</div>

Then by definition, $$\cl(A)$$ is the union of $$A$$ and its limit points. If $$x\in\cl(A)\setminus A$$, then by [Proposition 6](#prop6), $$x$$ must be a limit point of $$A$$. On the other hand, if $$x\in A$$, this need not hold. If for $$x\in A$$ there exists a neighborhood $$V$$ such that $$V\cap A=\{x\}$$, then $$x$$ is called an *isolated point* of $$A$$. A closed set with no isolated points is called a *perfect set*.

## Boundary

<div class="definition" markdown="1">

<ins id="def9">**Definition 9**</ins> For any subset $$A$$ of a topological space $$X$$, the *boundary* of $$A$$ is the set $$\partial A$$ defined by the formula

$$\partial A=\cl A\setminus\interior A$$

</div>

Hence $$\partial A$$ is a closed set.

## Dense Sets

<div class="definition" markdown="1">

<ins id="def10">**Definition 10**</ins> For any subset $$A$$ of a topological space $$X$$, $$A$$ is called a *dense subset* if $$\cl(A)=X$$.

</div>

By [Proposition 6](#prop6), saying that $$A$$ is dense in $$X$$ means that every nonempty open set in $$X$$ meets $$A$$. Intuitively, finding a dense subset of $$X$$ means that with only a slight perturbation we can recover all of $$X$$. In more everyday language, a dense subset of $$X$$ can be thought of as containing "almost all" of $$X$$.

Meanwhile, the notion of size in topology is also given by the size of a base, as the following proposition shows.

<div class="proposition" markdown="1">

<ins id="prop11">**Proposition 11**</ins> For a base $$\mathcal{B}$$ of a topological space $$X$$, there exists a dense subset $$D$$ of $$X$$ such that $$\card(D)\leq\card(\mathcal{B})$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

For each $$U\in\mathcal{B}$$, choose an element $$x_U\in U$$, and let $$D$$ be the set of these. That $$D$$ is dense follows because for any open set $$V$$, we can express it as a union of elements of $$\mathcal{B}$$, and this union must contain some $$x_U$$, so $$V\cap D\neq\emptyset$$.

</details>
