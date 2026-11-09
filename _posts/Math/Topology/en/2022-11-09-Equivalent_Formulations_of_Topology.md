---
title: "Other Definitions of Topological Spaces"
description: "A topological space can be defined without open sets using the Kuratowski closure operator axioms and interior operator axioms, and a topology defined this way produces the same topological structure as one defined by open sets."
excerpt: "Definitions of topology using closed sets, closure, and neighborhood filters"

categories: [Math / Topology]
permalink: /en/math/topology/equivalent_formulations_of_topology
sidebar: 
    nav: "topology-en"

date: 2022-11-09
weight: 4
translated_at: 2026-06-03T02:00:01+00:00
translation_source: kimi-cli
last_polished_at: 2026-11-07T23:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
We have covered the basics of topology so far. Historically, defining a topological space as a collection $\mathcal{T}$ of open sets is not that old, and various definitions have existed. Even today, depending on the field of study, these definitions can be useful. In this post, we examine how to define topology in different ways using the concepts we have explored so far.

## Closed Sets

By [§Interior, Closure, and Boundary, ⁋Proposition 2](/en/math/topology/other_concepts#prop2){: data-lid="6rdoy" }, on a set $X$, defining a collection $\mathcal{C}$ of sets that specifies *which sets are closed* allows one to endow $X$ with a topological structure. This is hardly different from the original definition, but it is particularly useful when defining the Zariski topology in algebraic geometry.

## Closure Axiom

::: Definition 1 (Kuratowski closure axiom)
For an arbitrary *set* $X$, suppose a function $\cl:\mathcal{P}(X)\rightarrow\mathcal{P}(X)$ satisfies all of the following conditions.

- $$A\subseteq\cl(A)$$
- $$\cl(\cl(A))=\cl(A)$$
- $$\cl(A\cup B)=\cl(A)\cup\cl(B)$$
- $$\cl(\emptyset)=\emptyset$$

A function satisfying these conditions is called a *closure operator*. ([\[Set Theory\] §Filters, Ideals, and Galois Connections, ⁋Definition 8](/en/math/set_theory/filter_and_ideal#def8){: data-lid="rqkh0" })
:::

From the third condition, if $A\subseteq B$, we see that

$$\cl(A)\subseteq\cl(A)\cup\cl(B)=\cl(A\cup B)=\cl(B)$$

.

For an arbitrary topological space $X$, it is obvious that the function sending each subset of $X$, $A$, to the closure of $A$, $\cl:\mathcal{P}(X)\rightarrow\mathcal{P}(X)$, satisfies the above conditions.

Conversely, suppose that on an arbitrary set $X$, a closure operator $\cl:\mathcal{P}(X)\rightarrow\mathcal{P}(X)$ satisfying the above conditions is given. Now, among the elements of $\mathcal{P}(X)$, let the collection of sets satisfying $\cl(C)=C$ be denoted by $\mathcal{C}$. Then

- Since $\cl(\emptyset)=\emptyset$, we have $\emptyset\in\mathcal{C}$. Meanwhile, since $X\subseteq\cl(X)$, we have $\cl(X)=X$ and therefore $X\in\mathcal{C}$.
- For arbitrary $A,B\in\mathcal{C}$, since $A\cup B=\cl(A)\cup\cl(B)=\cl(A\cup B)$ holds, we have $A\cup B\in\mathcal{C}$.
- For an arbitrary index set $I$ and $A_i\in\mathcal{C}$, we have $\bigcap A_i\subseteq\cl(\bigcap A_i)$, and from $\bigcap A_i\subseteq A_i$, since

  $$\cl(\bigcap A_i)\subseteq\cl(A_i)=A_i$$

  holds, $\cl(\bigcap A_i)\subseteq\bigcap A_i$ also holds.

From this we obtain the following theorem.

::: Theorem 2
Suppose a function $\cl:\mathcal{P}(X)\rightarrow\mathcal{P}(X)$ satisfying all the conditions of [Definition 1](#def1){: data-lid="es421" } is given. If we define $\mathcal{C}$ to be the collection of sets satisfying $\cl(C)=C$ over all $C$, then $\mathcal{C}$ satisfies all the conditions of [§Interior, Closure, and Boundary, ⁋Proposition 2](/en/math/topology/other_concepts#prop2){: data-lid="hnwpo" } and therefore defines a unique topological structure.
:::

Of course, one can define a topological structure without difficulty using the interior of a set as well. In this case, the axioms that the interior operator $\interior$ must satisfy are as follows.

::: misc Interior axiom. {#interior-axiom}
For an arbitrary set $X$, suppose a function $\interior:\mathcal{P}(X)\rightarrow\mathcal{P}(X)$ satisfies the following conditions.

- $$\interior(A)\subseteq A$$
- $$\interior(\interior(A))=\interior(A)$$
- $$\interior(A\cap B)=\interior(A)\cap\interior(B)$$
- $$\interior(X)=X$$

A function satisfying these conditions is called an *interior operator*.
:::

## Neighborhood Filter

We confirmed in [§Open Sets, ⁋Proposition 6](/en/math/topology/open_sets#prop6){: data-lid="pn9lb" } that for each point $x$, if we specify a *neighborhood filter* $\mathcal{N}(x)$, this information also gives $X$ a topological structure in a unique way. In that proposition, the first and second conditions that $\mathcal{N}(x)$ must satisfy are the conditions of a filter, and the third condition is that each element of $\mathcal{N}(x)$ contains $x$; although the following definition has also already been given, we retain it for later reference.

::: Definition 3
A *filter* defined on a set $X$ refers to a subset of $\mathcal{P}(X)$, $\mathcal{F}$, satisfying the following three conditions.

1. Whenever it contains an element of $\mathcal{F}$, a subset of $X$ belongs to $\mathcal{F}$.
2. Any finite intersection of elements of $\mathcal{F}$ belongs to $\mathcal{F}$.
3. $\emptyset\not\in\mathcal{F}$.
:::

::: Example 4
For an infinite set $X$, the collection of subsets such that $X\setminus A$ is a finite set, taken over all such $A$, is a filter. In particular, when $X=\mathbb{N}$, this filter is called the *Fréchet filter*.
:::

Considering the ordered set $(\mathcal{P}(X),\subseteq)$, the above definition is identical to the one defined in [\[Set Theory\] §Filters, Ideals, and Galois Connections, ⁋Definition 1](/en/math/set_theory/filter_and_ideal#def1){: data-lid="ufndh" }, but can be regarded as having the condition $\emptyset\not\in\mathcal{F}$ added. Similarly, an *ultrafilter* defined on $X$ is also understood to mean a maximal filter not containing $\emptyset$.

Then, among the four conditions that $\mathcal{N}(x)$ must satisfy, the first three can be summarized as saying that for every $x$, $\mathcal{N}(x)$ is a filter whose elements each contain $x$. The fourth condition has its own name.

::: misc Neighborhood axiom. {#neighborhood-axiom}
Suppose an arbitrary $z\in X$ and, with each of its elements containing $z$, a filter on $X$, $\mathcal{N}(z)$, are given. Then for every $S\in\mathcal{N}(z)$, there exists a suitable $S'\in\mathcal{N}(z)$ such that for every $x\in S'$, $S\in\mathcal{N}(x)$ holds.
:::

Moreover, regarding $\mathcal{N}(x)$ as playing a role similar to a local base, through this we were able to show that a topological space can also be defined via a base $\mathcal{B}$. ([§Bases of a Topological Space, ⁋Corollary 6](/en/math/topology/topological_bases#cor6){: data-lid="7k4j9" })

Meanwhile, more generally, one can define a base for a filter. 

::: Definition 5
Suppose that a subset of $\mathcal{P}(X)$, $\mathcal{B}$, satisfies the following two conditions.

1. The intersection of any two elements of $\mathcal{B}$ contains some element of $\mathcal{B}$.
2. $\mathcal{B}$ contains at least one element, and $\emptyset\not\in \mathcal{B}$.

Then $\uparrow \mathcal{B}$ defines a filter on $X$, and in this case we call $\mathcal{B}$ a *filter base* for $\uparrow \mathcal{B}$. 
:::

It is not difficult to verify the following.

::: Proposition 6
On $X$, for a filter $\mathcal{F}$, a subset $\mathcal{B}$ is a filter base for $\mathcal{F}$ if and only if every element of $\mathcal{F}$ contains some element of $\mathcal{B}$. 
:::

Furthermore, the following holds.

::: Proposition 7
On $X$, consider a filter $\mathcal{F}$. Then for any function $f:X \rightarrow Y$, 

$$f(\mathcal{F})=\{f(F)\mid F\in \mathcal{F}\}$$

is a filter base on $Y$.
:::
::: Proof
This follows from $f(F_1\cap F_2)\subseteq f(F_1)\cap f(F_2)$ and $\emptyset\not\in\mathcal{F}\implies \emptyset\not\in f(\mathcal{F})$.
:::

Meanwhile, on a set $X$, for a filter $\mathcal{F}$ and an arbitrary subset $A$, the following set

$$\mathcal{F}\vert_A=\{F\cap A\mid F\in \mathcal{F}\}$$

does not generally form a filter on $A$. Upon reflection, this is only because $\mathcal{F}\vert_A$ might contain the empty set. That is, if every element of $\mathcal{F}$ is not disjoint from $A$, then $\mathcal{F}\vert_A$ defines a filter on $A$. 

::: Definition 8
If in the above situation $\mathcal{F}\vert_A$ defines a filter on $A$, we say that the filter $\mathcal{F}$ induces the filter $\mathcal{F}\vert_A$ on $A$. 
:::

---

**References**

**[Bou]** N. Bourbaki, <i>General Topology</i>. Elements of mathematics. Springer, 1995.
