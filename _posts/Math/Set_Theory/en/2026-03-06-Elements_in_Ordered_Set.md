---
title: "Elements of Ordered Sets"
description: "This post introduces Hasse diagrams for ordered sets, defines minimal and maximal elements, and proves the uniqueness of minimum and maximum elements."
excerpt: "Greatest, least, maximal, and minimal elements of ordered sets"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/elements_in_ordered_set
sidebar: 
    nav: "set_theory-en"

date: 2021-08-22
weight: 16
translated_at: 2026-06-02T13:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-02T13:30:02+00:00
---
Consider the following diagram

{% diagram Math/Set_Theory/Elements_in_Ordered_Set-1.svg width="0.58em" alt="diagram_representing_single_ordering" %}

and let it represent $b\leq a$. For example, the following diagram

{% diagram Math/Set_Theory/Elements_in_Ordered_Set-2.svg width="6.04em" alt="diagram_representing_two_orderings" %}

represents the situation where $b\leq a$ and $c\leq a$, but there is no particular relation between $b$ and $c$. Such a diagram is called a *Hasse diagram*.

## Maximal and Minimal Elements

::: Definition 1
An element $a$ of an ordered set $A$ is called a *minimal element* (resp. *maximal element*) of $A$ if for all $x\in A$, whenever $a\leq x$ (resp. $a\geq x$), we have $x=a$.
:::

A minimal element need not be unique. For instance, in

{% diagram Math/Set_Theory/Elements_in_Ordered_Set-2.svg width="6.04em" alt="diagram_representing_two_orderings" %}

both $b$ and $c$ are minimal elements of the set $\{a,b,c\}$. Mathematicians generally prefer such elements to be unique, so this situation is not entirely satisfactory.

## Greatest and Least Elements

::: Definition 2
An element $a$ of an ordered set $A$ is called a *least element* (resp. *greatest element*) of $A$ if for all $x\in A$, we have $a\leq x$ (resp. $x\leq a$).
:::

In the preceding example, neither $b$ nor $c$ can be a least element, since neither $b\leq c$ nor $c\leq b$ holds. By definition, a least element is unique. Moreover, the following holds.

::: Proposition 3
If $A$ has a least element $a$, then $a$ is the unique minimal element of $A$.
:::

::: Proof
For any element $x$ of $A$, we have $a\leq x$. Thus, if there exists $x\in A$ such that $x\leq a$, then antisymmetry of $\leq$ implies $x=a$. Hence $a$ is a minimal element of $A$.

If $a'$ is another minimal element of $A$ and $a'\neq a$, then the contrapositive of [Definition 1](#def1) implies $a'\not\leq a$, which contradicts the fact that $a$ is a least element. Therefore $a'=a$.
:::

Occasionally we must consider a new element larger than every element of an ordered set, or smaller than every element. It is common to denote such hypothetical elements by $\pm\infty$.

::: Proposition 4
Let $A$ be an ordered set and let $A'=A\sqcup\{+\infty\}$. Then there exists an order relation on $A'$ extending the order relation defined on $A$ and having $+\infty$ as its greatest element.
:::

::: Proof
It suffices to adjoin to the original order relation the elements of $\bigcup_{x\in A}\left\{(x, +\infty)\right\}$.
:::

## Suprema and Infima

::: Definition 5
Let $A$ be a preordered set and let $X$ be a subset of $A$. If $a\in A$ satisfies $a\leq x$ (resp. $a\geq x$) for all $x\in X$, we call it a *lower bound* (resp. *upper bound*) of $X$ in $A$.

A set possessing a lower bound (resp. upper bound) is called *bounded below* (resp. *bounded above*), and a set that is both bounded below and bounded above is simply called *bounded*.
:::

Consider the ordered set $A=\{a,b,c,d,e\}$ shown below.

{% diagram frozen/81b7e8af/Math/Set_Theory/Elements_in_Ordered_Set-3.svg width="20.75em" alt="upper_and_lower_bounds" %}

Then $a$ is an upper bound of the set $X=\left\{c,d,e\right\}$, but $b$ is not. If we consider the set $X'=\left\{d,e\right\}$, both $a$ and $b$ are upper bounds of this set. From the above example we see that a lower bound of a set $X$ need not belong to $X$; however, if it does, then that element is a least element of $X$.

::: Definition 6
Let $A$ be an ordered set and let $X\subseteq A$. An element $a$ of $A$ is called the *greatest lower bound* (or *infimum*) of $X$ if it is the greatest element among the lower bounds of $X$. Similarly, the *least upper bound* (or *supremum*) is defined.
:::

If the supremum of $X\subseteq A$ exists, we denote it by $\sup_AX$, and the infimum by $\inf_AX$. By definition, one easily checks that if $X\subseteq A$ has a greatest element $a$, then $a=\sup_AX$.

::: Proposition 7
Let $A$ be an ordered set and suppose $X\subseteq A$ has both a supremum and an infimum.

1. If $X\neq\emptyset$, then $\inf_A X\leq\sup_A X$.
2. If $X=\emptyset$, then $\sup_AX$ and $\inf_AX$ are the least and greatest elements of $A$, respectively.
:::

::: Proof
1. If $X\neq\emptyset$, then there exists at least one element; let this be $a$. Then by definition $\inf X\leq a$ and $a\leq\sup X$, and by transitivity $\inf_AX \leq\sup_AX$.
2. If $X=\emptyset$, then every element $a$ of $A$ satisfies $a\leq x$ and $x\leq a$ for all $x\in X$. Therefore every element of $A$ is both a lower bound and an upper bound of $X$, and $\sup_AX$ and $\inf_AX$ are the least and greatest elements of $A$.
:::

## Suprema, Infima, and Set Operations

We now examine the relationship between the set operations we have seen and suprema and infima.

::: Proposition 8
For two subsets $X,X'$ of an ordered set $A$, if $\sup_AX$ and $\sup_AX'$ are defined and $X'\subseteq X$, then $\sup X'\leq\sup X$.
:::

::: Proof
Choose an arbitrary $x\in X'$. Since $X'\subseteq X$, we have $x\in X$. On the other hand, for any $x\in X$ we have $x\leq \sup X$, and therefore $\sup X$ is an upper bound of $X'$. Hence by definition $\sup X'\leq \sup X$. 
:::

::: Proposition 9
For an ordered set $A$, consider families $(x_i)_{i\in I}$ and $(y_i)_{i\in I}$ satisfying $x_i\leq y_i$ for all $i\in I$. If both have suprema in $A$, then $\sup_{i\in I} x_i\leq \sup_{i\in I} y_i$.
:::

::: Proof
For any $i\in I$, we have $x_i\leq y_i$ and $y_i\leq \sup y_i$, so $x_i\leq \sup y_i$ for all $i$. Therefore, by the minimality of $\sup x_i$, we have $\sup x_i\leq\sup y_i$.
:::

::: Proposition 10
Let $A$ be an ordered set, $I$ an index set, and $(J_k)_{k\in K}$ a covering of $I$, and suppose that $(x_i)_{i\in J_k}$ has a supremum in $A$ for each $k$. Then $\sup_{i\in I} x_i$ exists if and only if $\sup_{k\in K}(\sup_{j\in J_k}x_j)$ exists, and the two values are equal.
:::

::: Proof
Write $b_k=\sup_{i\in J_k} x_i$. First suppose that $(x_i)_{i\in I}$ has a supremum, and denote it by $a$. Then $a\leq b_k$ holds for all $k$. Also, if $c\geq b_k$ holds for all $k$, then for any $x_i$ there is a $k'$ with $i\in J_{k'}$, which satisfies $b_{k'}\geq x_i$; hence $c\geq x_i$ for any $i$. Now by the minimality of $a$ we must have $c\geq a$, and therefore $a$ is the supremum and $\sup_{i\in I}x_i=\sup_{k\in K}(\sup_{j\in J_k} x_j)$.

Conversely, if $(b_k)_{k\in K}$ has a supremum $a'$, the proof can be completed in the same way.
:::

::: Proposition 11
For the product $A=\prod A_i$ of ordered sets $(A_i)_{i\in I}$ and a subset $X$ thereof, let $X_i=\pr_i X$. Then $\sup_AX$ exists if and only if each $\sup_{A_i}X_i$ exists, and $\sup_AX=(\sup_{A_i}X_i)$.
:::
::: Proof
First suppose that $\sup_{A_i} X_i$ exists for each $i$. Then it is obvious that $(\sup_{A_i} X_i)_{i\in I}$ is an upper bound of $X$. If $(c_i)$ were another upper bound of $X$, then each $c_i$ would be an upper bound of $X_i$, so by the minimality of $\sup_{A_i}X_i$ we have $c_i\geq\sup X_i$, and therefore $(c_i)\geq(\sup X_i)_{i\in I}$.

Conversely, suppose $\sup X=(a_i)$ exists. For all $i$, $a_i$ is an upper bound of $X_i$. Indeed, if $x_i\in X_i$, then there exists $x\in X$ whose $i$-th component is $x_i$ and which satisfies $x\leq (a_i)$. Now for any other upper bound $a_i'$, define a new element $(c_i)$ by replacing the $i$-th component of $(a_i)$ with $a_i'$; then $c\geq a$, so $a_i'\geq a_i$.
:::

::: remark Remark {#rmk}
For an ordered set $A$ and $X'\subseteq X\subseteq A$, it may happen that only one of $\sup_AX'$ and $\sup_XX'$ exists, or that both exist but take different values. For instance, let us compare $X'=\{x\in\mathbb{Q}\mid x < \sqrt{2}\}$ in various sets.

1. As a subset of $X_1=\mathbb{Q}$, this set has no supremum, but it does in $A=\mathbb{R}$. That is, even if $\sup_AX'$ exists, $\sup_{X_1}X'$ may not exist.
2. On the other hand, consider the set $X_2=X'\cup \left\{2\right\}$. Then $X'\subseteq X_2\subseteq X_1$ and $\sup_{X_2}X'=2$, but $\sup_{X_1}X'$ does not exist.
3. Finally, in $X'\subseteq X_2\subseteq A$, both $\sup_{X_2}X'$ and $\sup_AX'$ exist but the two values differ.
:::

Nevertheless, we can still prove the following.

::: Proposition 12
Let $A$ be an ordered set and let $X'\subseteq X\subseteq A$. If both $\sup_AX'$ and $\sup_XX'$ exist, then $\sup_AX'\leq\sup_XX'$. If $\sup_AX'$ exists and belongs to $X$, then $\sup_XX'$ also exists and equals $\sup_AX'$.
:::
::: Proof
The set of upper bounds of $X'$ in $X$ is contained in the set of upper bounds of $X'$ in $A$; hence the supremum in $X$ is larger. If $\sup_AX'$ exists and belongs to $X$, then it is evidently the supremum of $X'$ in $X$.
:::




---
**References**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
