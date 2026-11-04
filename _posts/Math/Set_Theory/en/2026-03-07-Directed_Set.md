---
title: "Directed Sets"
description: "This post covers the definition and properties of directed sets. It defines sets directed to the right and left in a partially ordered set, shows that the greatest element of a directed set is the greatest element, and proves that a family of directed sets is also a directed set."
excerpt: "Directed sets and lattices"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/directed_set
sidebar: 
    nav: "set_theory-en"

date: 2022-11-27
weight: 17
translated_at: 2026-06-02T21:00:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-11-04T23:15:07+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
For a preordered set $A$, a subset $X\subseteq A$ is *cofinal* (resp. *coinitial*) in $A$ if for any $x\in A$ there exists $y\in X$ such that $x\leq y$ (resp. $y\leq x$). For example, in the following diagram

{% diagram Math/Set_Theory/Directed_Set-1.svg width="20.75em" alt="cofinal_sequence" %}

the sets $\left\{a_{2n}\right\}_{n\in\mathbb{N}}$, $\left\{a_{1000+n}\right\}_{n\in\mathbb{N}}$, etc., are all cofinal.

## Directed Set

In Hasse diagrams it is conventional to place larger elements toward the top, but larger elements are sometimes placed toward the right, as in the diagram above.

::: Definition 1
 A preordered set $A$ is *right directed* if every two-element subset of $A$ is bounded above. Similarly, a preordered set $A$ is *left directed* if every two-element subset of $A$ is bounded below.
:::

For example, for any set $A$, the ordered set $(\mathcal{P}(A),\subseteq)$ is right directed. This is because for any $X, Y\in\mathcal{P}(A)$, $X\cup Y$ is an element of $\mathcal{P}(A)$ and is an upper bound of $X$ and $Y$. Representing this as a diagram gives the following.

{% diagram Math/Set_Theory/Directed_Set-2.png width="24em" alt="directed_system" %}

::: Proposition 2
 If an ordered set $A$ is right directed, then a maximal element of $A$ is also a greatest element.
:::

::: Proof
Since $A$ is right directed, for any $x\in A$ and a maximal element $a$, the set $\{x,a\}$ has an upper bound $y$. Now by the maximality of $a$, we must have $a=y$, so $x\leq a$ holds.
:::

::: Proposition 3
If $(A_i)$ is a family of right directed sets, then $\prod A_i$ is also right directed.
:::
::: Proof
Let $(x_i),(y_i)\in\prod A_i$. Then for each $i$, since $x_i,y_i\in A_i$ and $A_i$ is right directed, there exists, such that $x_i,y_i\leq z_i$, an element $z_i\in A_i$. Now since $(x_i),(y_i)\leq(z_i)$, $\prod A_i$ is also right directed.
:::

In general, a subset of a right directed set is of course not right directed. However, one can easily verify that a cofinal subset is right directed.

::: Definition 4
An ordered set $A$ is a *lattice* if every two-element subset of $A$ has a supremum and an infimum. In this case, the two elements $\sup\{x,y\}$ and $\inf\{x,y\}$ are called the *join* and *meet* of $x,y$, respectively, and are written $x\vee y$ and $x\wedge y$.
:::

Any *nonempty finite* subset of a lattice $A$ has a supremum and an infimum. If *every* subset of $A$ has a supremum and an infimum, then $A$ is called a *complete lattice*.

## Totally Ordered Set

::: Definition 5
In a preordered set $A$, two elements $x$ and $y$ are *comparable* if $x\leq y$ or $y\leq x$ holds. If any two elements of an ordered set $A$ are comparable, it is called a *totally ordered set*.
:::

If $A$ is a totally ordered set, then trichotomy holds: for any $x, y\in A$, exactly one of

$$x=y,\qquad x < y,\qquad x > y$$

holds. In this case, the negation of $x\leq y$ is $x > y$. However, without the condition of being a totally ordered set, this does not hold in general. ([§Definition of Order Relations, ⁋Remark 11](/en/math/set_theory/order_relations#rmk11){: data-lid="mlqdv" })

::: Proposition 6
From a totally ordered set $A$ to an ordered set $B$, every strictly monotone function $f$ is injective. If $f$ is strictly increasing, then $f$ is an isomorphism from $A$ onto $f(A)$.
:::
::: Proof
Let $f$ be a strictly monotone function. Then for any $x\neq y$, we have $x > y$ or $x < y$, so $f(x) > f(y)$ or $f(x) < f(y)$, and thus $f(x)\neq f(y)$, so that $f$ is injective. In particular, if $f$ is strictly increasing, we must show $f(x)\leq f(y)\implies x\leq y$, whose contrapositive is obvious.
:::

The proposition above also did not hold for general ordered sets. ([§Monotone Functions, ⁋Remark 6](/en/math/set_theory/monotone_functions#rmk6){: data-lid="5iy57" })

::: Proposition 7
Let $A$ be a totally ordered set and let $X$ be a subset of it. Then $b\in A$ is the supremum of $X$ if and only if $b$ is an upper bound of $X$ and, for every $c < b$ with $c\in A$, there exists $x\in X$ such that $c < x\leq b$.
:::

::: Proof
Obvious.
:::

Let $A$ be an ordered set, and suppose $a\leq b$. Then, the subset that, satisfying $a\leq x\leq b$, collects all $x$, $X\subseteq A$, is called a *closed interval* and is denoted $[a,b]$. The interval $(a,b)$ is called an *open interval*; this is the set that, satisfying $a < x < b$, collects all $x$.  
Additionally, the subset that, satisfying $x\leq a$, collects all $x$ is called an *unbounded* closed interval and is denoted $(-\infty, a]$. $[a,\infty)$, $(-\infty, a)$, and $(a, \infty)$ are defined similarly.


::: Proposition 8
In a lattice, the intersection of two intervals is also an interval.
:::

---
**References**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
