---
title: "Directed Sets"
description: "This post covers the definition and properties of directed sets. It defines sets directed to the right and left in a partially ordered set, shows that the greatest element of a directed set is a maximal element, and proves that any family of directed sets is also a directed set."
excerpt: "Directed sets and lattices"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/directed_set
sidebar: 
    nav: "set_theory-en"

date: 2022-11-27
weight: 17
translated_at: 2026-06-02T21:00:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-02T21:00:02+00:00
---
For a preordered set $A$, a subset $X\subseteq A$ is *cofinal* (resp. *coinitial*) in $A$ if for any $x\in A$ there exists $y\in X$ such that $x\leq y$ (resp. $y\leq x$). For example, in the following diagram

{% diagram Math/Set_Theory/Directed_Set-1.svg width="20.75em" alt="cofinal_sequence" %}

the sets $\left\{a_{2n}\right\}_{n\in\mathbb{N}}$ and $\left\{a_{1000+n}\right\}_{n\in\mathbb{N}}$ are both cofinal.

## Directed Set

In Hasse diagrams it is conventional to place larger elements toward the top, but larger elements are sometimes placed toward the right, as in the diagram above.

::: Definition 1
 A preordered set $A$ is *right directed* if every two-element subset of $A$ is bounded above. Similarly, a preordered set $A$ is *left directed* if every two-element subset of $A$ is bounded below.
:::

For example, for any set $A$, the ordered set $(\mathcal{P}(A),\subseteq)$ is right directed: for any $X, Y\in\mathcal{P}(A)$, the union $X\cup Y$ belongs to $\mathcal{P}(A)$ and is an upper bound of both $X$ and $Y$. This is illustrated by the following diagram.

{% diagram Math/Set_Theory/Directed_Set-2.png width="24em" alt="directed_system" %}

::: Proposition 2
 If an ordered set $A$ is right directed, then every maximal element of $A$ is also a greatest element.
:::

::: Proof
Since $A$ is right directed, for any $x\in A$ and any maximal element $a$, the set $\{x,a\}$ has an upper bound $y$. By maximality of $a$ we must have $a=y$, and therefore $x\leq a$.
:::

::: Proposition 3
If $(A_i)$ is a family of right directed sets, then $\prod A_i$ is also right directed.
:::
::: Proof
Let $(x_i),(y_i)\in\prod A_i$. For each $i$, since $x_i,y_i\in A_i$ and $A_i$ is right directed, there exists $z_i\in A_i$ with $x_i,y_i\leq z_i$. Then $(x_i),(y_i)\leq(z_i)$, so $\prod A_i$ is right directed.
:::

In general, a subset of a right directed set need not be right directed. However, one easily verifies that every cofinal subset is right directed.

::: Definition 4
An ordered set $A$ is a *lattice* if every two-element subset of $A$ has a supremum and an infimum. In this case, $\sup\{x,y\}$ and $\inf\{x,y\}$ are called the *join* and *meet* of $x$ and $y$, respectively, and are written $x\vee y$ and $x\wedge y$.
:::

Every *finite* subset of a lattice $A$ has a supremum and an infimum. If *every* subset of $A$ has a supremum and an infimum, then $A$ is called a *complete lattice*.

## Totally Ordered Set

::: Definition 5
Two elements $x$ and $y$ in a preordered set $A$ are *comparable* if $x\leq y$ or $y\leq x$. If every two elements of $A$ are comparable, then $A$ is called a *totally ordered set*.
:::

If $A$ is a totally ordered set, then trichotomy holds: for any $x, y\in A$, exactly one of

$$x=y,\qquad x < y,\qquad x > y$$

holds. In this case the negation of $x\leq y$ is $x > y$; without the totally ordered hypothesis this is generally false. ([§Definition of Order Relations, ⁋Remark 11](/en/math/set_theory/order_relations#rmk11))

::: Proposition 6
Every strictly monotone function $f$ from a totally ordered set $A$ to an ordered set $B$ is injective. If $f$ is strictly increasing, then $f$ is an isomorphism from $A$ onto $f(A)$.
:::
::: Proof
Let $f$ be strictly monotone. For any $x\neq y$, either $x > y$ or $x < y$, so $f(x) > f(y)$ or $f(x) < f(y)$; hence $f(x)\neq f(y)$, and $f$ is injective. In particular, if $f$ is strictly increasing, we must show $f(x)\leq f(y)\implies x\leq y$, whose contrapositive is obvious.
:::

The preceding proposition also fails for general ordered sets. ([§Monotone Functions, ⁋Remark 6](/en/math/set_theory/monotone_functions#rmk6))

::: Proposition 7
Let $A$ be a totally ordered set and let $X\subseteq A$. Then $b\in A$ is the supremum of $X$ if and only if $b$ is an upper bound of $X$ and, for every $c\in A$ with $c < b$, there exists $x\in X$ such that $c < x\leq b$.
:::

::: Proof
Obvious.
:::

Let $A$ be an ordered set, and suppose $a\leq b$. The subset $X\subseteq A$ consisting of all $x$ satisfying $a\leq x\leq b$ is called a *closed interval* and is denoted $[a,b]$. The interval $(a,b)$ is called an *open interval*; it is the set of all $x$ satisfying $a < x < b$.

Likewise, the subset of all $x$ satisfying $x\leq a$ is called an *unbounded* closed interval and is denoted $(-\infty, a]$. The notations $[a,\infty)$, $(-\infty, a)$, and $(a, \infty)$ are defined analogously.


::: Proposition 8
In a lattice, the intersection of two intervals is again an interval.
:::

---
**References**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
