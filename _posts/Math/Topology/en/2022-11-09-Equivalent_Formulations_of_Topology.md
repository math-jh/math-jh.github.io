---
title: "Other Definitions of Topological Spaces"
excerpt: "Definitions of topology using closed sets, closure, and neighborhood filters"

categories: [Math / Topology]
permalink: /en/math/topology/equivalent_formulations_of_topology
header:
    overlay_image: /assets/images/Math/Topology/Equivalent_Formulations_of_Topology.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology-en"

date: 2022-11-09
last_modified_at: 2022-11-09
weight: 4
translated_at: 2026-05-23T00:00:01+00:00
translation_source: kimi-cli
---
We have covered the basics of topology so far. Historically, the definition of a topological space as a collection $$\mathcal{T}$$ of open sets is not very old, and various definitions have existed. Even today, depending on the field of study, these definitions can be useful. In this post, we explore how to define topology in different ways using the concepts we have studied.

## Closed Sets

By [§Interior, Closure, and Boundary, ⁋Proposition 2](/en/math/topology/other_concepts#prop2), by defining a collection $$\mathcal{C}$$ of subsets of $$X$$ that tells us *which sets are closed*, we can give $$X$$ a topological structure. This is not very different from the original definition, but it can be particularly useful when defining the Zariski topology in algebraic geometry.

## Closure Axiom

<div class="definition" markdown="1">

<ins id="def1">**Definition 1 (Kuratowski closure axiom)**</ins> For an arbitrary *set* $$X$$, suppose a function $$\cl:\mathcal{P}(X)\rightarrow\mathcal{P}(X)$$ satisfies all of the following conditions.

- $$A\subset\cl(A)$$
- $$\cl(\cl(A))=\cl(A)$$
- $$\cl(A\cup B)=\cl(A)\cup\cl(B)$$
- $$\cl(\emptyset)=\emptyset$$

A function satisfying these conditions is called a *closure operator*. ([\[Set Theory\] §Filters, Ideals, and Galois Correspondence, ⁋Definition 8](/en/math/set_theory/filter_and_ideal#def8))

</div>

From the third condition, if $$A\subseteq B$$, then we can see that

$$\cl(A)\subset\cl(A)\cup\cl(B)=\cl(A\cup B)=\cl(B)$$

holds.

For an arbitrary topological space $$X$$, it is obvious that the function $$\cl:\mathcal{P}(X)\rightarrow\mathcal{P}(X)$$ sending an arbitrary subset $$A$$ of $$X$$ to its closure satisfies the above conditions.

Conversely, suppose a closure operator $$\cl:\mathcal{P}(X)\rightarrow\mathcal{P}(X)$$ satisfying the above conditions is given on an arbitrary set $$X$$. Now let us denote by $$\mathcal{C}$$ the collection of elements of $$\mathcal{P}(X)$$ satisfying $$\cl(C)=C$$. Then

- Since $$\cl(\emptyset)=\emptyset$$, we have $$\emptyset\in\mathcal{C}$$. On the other hand, since $$X\subset\cl(X)$$, we have $$\cl(X)=X$$ and therefore $$X\in\mathcal{C}$$.
- For arbitrary $$A,B\in\mathcal{C}$$, since $$A\cup B=\cl(A)\cup\cl(B)=\cl(A\cup B)$$ holds, we have $$A\cup B\in\mathcal{C}$$.
- For an arbitrary index set $$I$$ and $$A_i\in\mathcal{C}$$, we have $$\bigcap A_i\subset\cl(\bigcap A_i)$$, and also from $$\bigcap A_i\subseteq A_i$$,

  $$\cl(\bigcap A_i)\subset\cl(A_i)=A_i$$

  holds, so $$\cl(\bigcap A_i)\subset\bigcap A_i$$ also holds.

From this, the following theorem is obtained.

<div class="proposition" markdown="1">

<ins id="thm2">**Theorem 2**</ins> Suppose a function $$\cl:\mathcal{P}(X)\rightarrow\mathcal{P}(X)$$ satisfying all the conditions of [Definition 1](#def1) is given. If we define $$\mathcal{C}$$ as <phrase>the collection of all $$C$$ satisfying $$\cl(C)=C$$</phrase>, then $$\mathcal{C}$$ satisfies all the conditions of [§Interior, Closure, and Boundary, ⁋Proposition 2](/en/math/topology/other_concepts#prop2) and thus defines a unique topological structure.

</div>

Of course, using the interior of a set, one can easily define a topological structure as well. In this case, the axioms that the interior operator $$\interior$$ must satisfy are as follows.

<div class="misc" markdown="1">

**Interior Axiom.** For an arbitrary set $$X$$, suppose a function $$\interior:\mathcal{P}(X)\rightarrow\mathcal{P}(X)$$ satisfies the following conditions.

- $$\interior(A)\subseteq A$$
- $$\interior(\interior(A))=\interior(A)$$
- $$\interior(A\cap B)=\interior(A)\cap\interior(B)$$
- $$\interior(X)=X$$

A function satisfying these conditions is called an *interior operator*.

</div>

## Neighborhood Filter

We verified in [§Open Sets, ⁋Proposition 6](/en/math/topology/open_sets#prop6) that giving a *neighborhood filter* $$\mathcal{N}(x)$$ for each point $$x$$ also gives $$X$$ a topological structure in a unique way. In that proposition, the first through third conditions that $$\mathcal{N}(x)$$ must satisfy are the conditions for a filter, and although the following definition has already been defined, we leave it for later reference.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> A *filter* defined on a set $$X$$ means a subset $$\mathcal{F}$$ of $$\mathcal{P}(X)$$ satisfying the following three conditions.

1. A subset of $$X$$ containing an element of $$\mathcal{F}$$ belongs to $$\mathcal{F}$$.
2. A finite intersection of elements of $$\mathcal{F}$$ belongs to $$\mathcal{F}$$.
3. $$\emptyset\not\in\mathcal{F}$$.

</div>

<div class="example" markdown="1">

<ins id="ex4">**Example 4**</ins> For an infinite set $$X$$, the collection of $$A$$ such that $$X\setminus A$$ is a finite set is a filter. Especially when $$X=\mathbb{N}$$, this filter is called the *Fréchet filter*.

</div>

Thinking of the ordered set $$(\mathcal{P}(X),\subseteq)$$, the above definition can be thought of as the same as that defined in [\[Set Theory\] §Filters, Ideals, and Galois Correspondence, ⁋Definition 1](/en/math/set_theory/filter_and_ideal#def1), except with the additional condition $$\emptyset\not\in\mathcal{F}$$. Similarly, an *ultrafilter* defined on $$X$$ is also thought of as a maximal filter not containing $$\emptyset$$.

Then among the four conditions that $$\mathcal{N}(x)$$ must satisfy, the first three can be summarized as $$\mathcal{N}(x)$$ having a filter structure for every $$x$$. The fourth condition has a separate name.

<div class="misc" markdown="1">

**Neighborhood Axiom.** For an arbitrary $$z\in X$$, suppose a filter $$\mathcal{N}(z)$$ on $$X$$ is given whose elements each contain $$z$$. Then for every $$S\in\mathcal{N}(z)$$, there exists a suitable $$S'\in\mathcal{N}(z)$$ such that <phrase>for every $$x\in S'$$, $$S\in\mathcal{N}(x)$$</phrase> holds.

</div>

Moreover, thinking of $$\mathcal{N}(x)$$ as playing a role similar to a local base, we were able to show that a topological space can also be defined through a base $$\mathcal{B}$$. ([§Topological Bases, ⁋Corollary 6](/en/math/topology/topological_bases#cor6))

Meanwhile, one can define the base of a filter more generally.

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> Suppose a subset $$\mathcal{B}$$ of $$\mathcal{P}(X)$$ satisfies the following two conditions.

1. The intersection of any two elements of $$\mathcal{B}$$ contains some element of $$\mathcal{B}$$.
2. $$\mathcal{B}$$ contains at least one element, and $$\emptyset\not\in \mathcal{B}$$.

Then $$\uparrow \mathcal{B}$$ defines a filter on $$X$$, and in this case we call $$\mathcal{B}$$ a *filter base* of $$\uparrow \mathcal{B}$$.

</div>

The following can be easily verified.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> A subset $$\mathcal{B}$$ of a filter $$\mathcal{F}$$ defined on $$X$$ is a filter base of $$\mathcal{F}$$ if and only if every element of $$\mathcal{F}$$ contains some element of $$\mathcal{B}$$.

</div>

Also, the following holds.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> Consider a filter $$\mathcal{F}$$ defined on $$X$$. Then for an arbitrary function $$f:X \rightarrow Y$$,

$$f(\mathcal{F})=\{f(F)\mid F\in \mathcal{F}\}$$

is a filter base on $$Y$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

This is obvious from $$f(F_1\cap F_2)\subseteq f(F_1)\cap f(F_2)$$, and $$\emptyset\not\in\mathcal{F}\implies \emptyset\not\in f(\mathcal{F})$$.

</details>

Meanwhile, for a filter $$\mathcal{F}$$ defined on a set $$X$$ and an arbitrary subset $$A$$, the following set

$$\mathcal{F}\vert_A=\{F\cap A\mid F\in \mathcal{F}\}$$

does not generally become a filter on $$A$$. Thinking about it, this is because $$\mathcal{F}\vert_A$$ may contain the empty set. That is, if every element of $$\mathcal{F}$$ intersects $$A$$, then $$\mathcal{F}\vert_A$$ defines a filter on $$A$$.

<div class="definition" markdown="1">

<ins id="def8">**Definition 8**</ins> If in the above situation $$\mathcal{F}\vert_A$$ defines a filter on $$A$$, we call the filter $$\mathcal{F}$$ a filter on $$A$$.

</div>
