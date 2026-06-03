---
title: "Other Definitions of Topological Spaces"
description: "A topological space can be defined using only the Kuratowski closure axioms or interior operator axioms, without any reference to open sets, and the resulting topology is identical to the one defined by open sets."
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
translated_at: 2026-06-03T02:00:01+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-03T02:00:01+00:00
---
We have covered the basics of topology so far. Historically, defining a topological space as a collection $$\mathcal{T}$$ of open sets is not very old, and various definitions have been used. Even today, depending on the area of study, these definitions can still be useful. In this post, we explore how to define topology in different ways using the concepts we have examined so far.

## Closed Sets

By [§Interior, Closure, and Boundary, ⁋Proposition 2](/en/math/topology/other_concepts#prop2), defining a collection $$\mathcal{C}$$ of subsets of $$X$$ that tells us *which sets are closed* suffices to give $$X$$ a topological structure. This is hardly different from the original definition, but it is particularly useful when defining the Zariski topology in algebraic geometry.

## Closure Axiom

<div class="definition" markdown="1">

<ins id="def1">**Definition 1 (Kuratowski closure axiom)**</ins> For an arbitrary *set* $$X$$, suppose a function $$\cl:\mathcal{P}(X)\rightarrow\mathcal{P}(X)$$ satisfies all of the following conditions.

- $$A\subset\cl(A)$$
- $$\cl(\cl(A))=\cl(A)$$
- $$\cl(A\cup B)=\cl(A)\cup\cl(B)$$
- $$\cl(\emptyset)=\emptyset$$

A function satisfying these conditions is called a *closure operator*. ([\[Set Theory\] §Filters, Ideals, and Galois Connections, ⁋Definition 8](/en/math/set_theory/filter_and_ideal#def8))

</div>

From the third condition, if $$A\subseteq B$$ then

$$\cl(A)\subset\cl(A)\cup\cl(B)=\cl(A\cup B)=\cl(B)$$

follows.

For any topological space $$X$$, it is obvious that the function $$\cl:\mathcal{P}(X)\rightarrow\mathcal{P}(X)$$ sending each subset $$A$$ of $$X$$ to its closure satisfies the above conditions.

Conversely, suppose a closure operator $$\cl:\mathcal{P}(X)\rightarrow\mathcal{P}(X)$$ satisfying the above conditions is given on a set $$X$$. Let $$\mathcal{C}$$ denote the collection of those elements $$C$$ of $$\mathcal{P}(X)$$ for which $$\cl(C)=C$$. Then

- Since $$\cl(\emptyset)=\emptyset$$, we have $$\emptyset\in\mathcal{C}$$. On the other hand, since $$X\subset\cl(X)$$, we have $$\cl(X)=X$$ and therefore $$X\in\mathcal{C}$$.
- For arbitrary $$A,B\in\mathcal{C}$$, since $$A\cup B=\cl(A)\cup\cl(B)=\cl(A\cup B)$$, we have $$A\cup B\in\mathcal{C}$$.
- For an arbitrary index set $$I$$ and $$A_i\in\mathcal{C}$$, we have $$\bigcap A_i\subset\cl(\bigcap A_i)$$, and since $$\bigcap A_i\subseteq A_i$$,

  $$\cl(\bigcap A_i)\subset\cl(A_i)=A_i$$

  holds, so $$\cl(\bigcap A_i)\subset\bigcap A_i$$ also holds.

From this we obtain the following theorem.

<div class="proposition" markdown="1">

<ins id="thm2">**Theorem 2**</ins> Suppose a function $$\cl:\mathcal{P}(X)\rightarrow\mathcal{P}(X)$$ satisfying all the conditions of [Definition 1](#def1) is given. Define $$\mathcal{C}$$ to be <phrase>the collection of all $C$ satisfying $\cl(C)=C$</phrase>. Then $$\mathcal{C}$$ satisfies all the conditions of [§Interior, Closure, and Boundary, ⁋Proposition 2](/en/math/topology/other_concepts#prop2), and therefore defines a unique topological structure.

</div>

Of course, one can just as easily define a topological structure using the interior of a set. In this case, the axioms that the interior operator $$\interior$$ must satisfy are as follows.

<div class="misc" markdown="1">

**Interior Axiom.** For an arbitrary set $$X$$, suppose a function $$\interior:\mathcal{P}(X)\rightarrow\mathcal{P}(X)$$ satisfies the following conditions.

- $$\interior(A)\subseteq A$$
- $$\interior(\interior(A))=\interior(A)$$
- $$\interior(A\cap B)=\interior(A)\cap\interior(B)$$
- $$\interior(X)=X$$

A function satisfying these conditions is called an *interior operator*.

</div>

## Neighborhood Filter

We verified in [§Open Sets, ⁋Proposition 6](/en/math/topology/open_sets#prop6) that giving a *neighborhood filter* $$\mathcal{N}(x)$$ for each point $$x$$ also endows $$X$$ with a topological structure in a unique way. In that proposition, the first three conditions that $$\mathcal{N}(x)$$ must satisfy are precisely the filter axioms. Although the following definition has already been introduced, we record it here for later reference.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> A *filter* on a set $$X$$ is a subset $$\mathcal{F}$$ of $$\mathcal{P}(X)$$ satisfying the following three conditions.

1. Any subset of $$X$$ containing an element of $$\mathcal{F}$$ belongs to $$\mathcal{F}$$.
2. Any finite intersection of elements of $$\mathcal{F}$$ belongs to $$\mathcal{F}$$.
3. $$\emptyset\not\in\mathcal{F}$$.

</div>

<div class="example" markdown="1">

<ins id="ex4">**Example 4**</ins> For an infinite set $$X$$, the collection of all $$A$$ such that $$X\setminus A$$ is finite forms a filter. In particular, when $$X=\mathbb{N}$$, this filter is called the *Fréchet filter*.

</div>

Regarding the ordered set $$(\mathcal{P}(X),\subseteq)$$, the above definition coincides with that given in [\[Set Theory\] §Filters, Ideals, and Galois Connections, ⁋Definition 1](/en/math/set_theory/filter_and_ideal#def1), except for the additional condition $$\emptyset\not\in\mathcal{F}$$. Likewise, an *ultrafilter* on $$X$$ is understood as a maximal filter not containing $$\emptyset$$.

Thus, among the four conditions that $$\mathcal{N}(x)$$ must satisfy, the first three can be summarized as the requirement that $$\mathcal{N}(x)$$ be a filter for every $$x$$. The fourth condition has its own name.

<div class="misc" markdown="1">

**Neighborhood Axiom.** For an arbitrary $$z\in X$$, suppose a filter $$\mathcal{N}(z)$$ on $$X$$ is given whose elements each contain $$z$$. Then for every $$S\in\mathcal{N}(z)$$, there exists a suitable $$S'\in\mathcal{N}(z)$$ such that <phrase>for every $x\in S'$, $S\in\mathcal{N}(x)$</phrase>.

</div>

Moreover, regarding $$\mathcal{N}(x)$$ as playing a role similar to a local base, we showed that a topological space can also be defined via a base $$\mathcal{B}$$. ([§Bases of a Topological Space, ⁋Corollary 6](/en/math/topology/topological_bases#cor6))

More generally, one can define a base for a filter.

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> Suppose a subset $$\mathcal{B}$$ of $$\mathcal{P}(X)$$ satisfies the following two conditions.

1. The intersection of any two elements of $$\mathcal{B}$$ contains some element of $$\mathcal{B}$$.
2. $$\mathcal{B}$$ contains at least one element, and $$\emptyset\not\in \mathcal{B}$$.

Then $$\uparrow \mathcal{B}$$ defines a filter on $$X$$, and in this case we call $$\mathcal{B}$$ a *filter base* for $$\uparrow \mathcal{B}$$.

</div>

The following is easily verified.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> A subset $$\mathcal{B}$$ of a filter $$\mathcal{F}$$ on $$X$$ is a filter base for $$\mathcal{F}$$ if and only if every element of $$\mathcal{F}$$ contains some element of $$\mathcal{B}$$.

</div>

Furthermore, the following holds.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> Let $$\mathcal{F}$$ be a filter on $$X$$. Then for any function $$f:X \rightarrow Y$$,

$$f(\mathcal{F})=\{f(F)\mid F\in \mathcal{F}\}$$

is a filter base on $$Y$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

This is obvious from $$f(F_1\cap F_2)\subseteq f(F_1)\cap f(F_2)$$ and $$\emptyset\not\in\mathcal{F}\implies \emptyset\not\in f(\mathcal{F})$$.

</details>

Meanwhile, for a filter $$\mathcal{F}$$ on a set $$X$$ and an arbitrary subset $$A$$, the set

$$\mathcal{F}\vert_A=\{F\cap A\mid F\in \mathcal{F}\}$$

does not generally form a filter on $$A$$. Upon reflection, this is solely because $$\mathcal{F}\vert_A$$ might contain the empty set. That is, if every element of $$\mathcal{F}$$ meets $$A$$, then $$\mathcal{F}\vert_A$$ defines a filter on $$A$$.

<div class="definition" markdown="1">

<ins id="def8">**Definition 8**</ins> If in the above situation $$\mathcal{F}\vert_A$$ defines a filter on $$A$$, we call the filter $$\mathcal{F}$$ a filter on $$A$$.

</div>
