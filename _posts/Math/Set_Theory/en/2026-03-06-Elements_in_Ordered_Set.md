---
title: "Elements of Ordered Sets"
description: "This post introduces Hasse diagram notation for ordered sets, covers the definitions of minimal and maximal elements, and presents the concepts of least and greatest elements and proves their uniqueness."
excerpt: "Greatest, least, maximal, and minimal elements of ordered sets"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/elements_in_ordered_set
sidebar: 
    nav: "set_theory-en"

date: 2021-08-22
weight: 16
translated_at: 2026-06-02T13:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-11-02T03:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
Let the following diagram

{% diagram Math/Set_Theory/Elements_in_Ordered_Set-1.svg width="0.58em" alt="diagram_representing_single_ordering" %}

represent $b\leq a$. For example, the following diagram

{% diagram Math/Set_Theory/Elements_in_Ordered_Set-2.svg width="6.04em" alt="diagram_representing_two_orderings" %}

represents the situation where $b\leq a$ and $c\leq a$, but there is no particular relation between $b$ and $c$. Such a diagram is called a *Hasse diagram*.

## Maximal and Minimal Elements

::: Definition 1
For an ordered set $A$, an element $a$ is called a *minimal element* (resp. *maximal element*) of $A$ if for all $x\in A$, $x\leq a$ (resp. $x\geq a$) implies $x=a$.
:::

A minimal element need not be unique. For instance, in
    
{% diagram Math/Set_Theory/Elements_in_Ordered_Set-2.svg width="6.04em" alt="diagram_representing_two_orderings" %}

both $b$ and $c$ are minimal elements of the set $\{a,b,c\}$. Mathematicians generally prefer such elements to be unique, so this situation is not particularly desirable.

## Greatest and Least Elements

::: Definition 2
For an ordered set $A$, an element $a$ is called a *least element* (resp. *greatest element*) of $A$ if for all $x\in A$, we have $a\leq x$ (resp. $x\leq a$).
:::

In the preceding example, neither $b$ nor $c$ can be a least element, since neither $b\leq c$ nor $c\leq b$ holds. By definition, a least element is unique. Moreover, the following holds.

::: Proposition 3
If $A$ has a least element $a$, then $a$ is the unique minimal element of $A$.
:::

::: Proof
In $A$, for any element $x$, we have $a\leq x$. Thus, if $x\leq a$ holds for some $x\in A$, then by the antisymmetry of $\leq$, we must have $x=a$. From this, we see that $a$ is a minimal element of $A$.

If $a'$ is another minimal element of $A$ and $a'\neq a$, then by the contrapositive of [Definition 1](#def1){: data-lid="2qjgc" }, we must have $a\not\leq a'$, which contradicts the fact that $a$ is a least element; hence $a'=a$.
:::

Occasionally it is necessary to consider a new element larger than every element of an ordered set, or smaller than every element. It is standard to write such hypothetical elements as $\pm\infty$.

::: Proposition 4
Let $A$ be an ordered set and let $A'=A\sqcup\{+\infty\}$. Then, extending the order relation defined on $A$ and having $+\infty$ as its greatest element, there exists an order relation on $A'$.
:::

::: Proof
It suffices to add the elements of $\bigcup_{x\in A'}\left\{(x, +\infty)\right\}$ to the original order relation.
:::

## Suprema and Infima

::: Definition 5
Let a preordered set $A$ and its subset $X$ be given. If $a\in A$ satisfies, for all $x\in X$, that $a\leq x$ (resp. $a\geq x$), then this is called a *lower bound* (resp. *upper bound*) in $A$ of $X$.

A set having a lower bound (resp. upper bound) is called *bounded below* (resp. *bounded above*), and a set that is both bounded below and bounded above is simply called *bounded*.
:::

Consider the following ordered set $A=\{a,b,c,d,e\}$.

{% diagram frozen/635a8f80/Math/Set_Theory/Elements_in_Ordered_Set-3.svg width="20.75em" alt="upper_and_lower_bounds" %}

Then $a$ is an upper bound of the set $X=\left\{c,d,e\right\}$, but $b$ is not. If we consider the set $X'=\left\{d,e\right\}$, both $a$ and $b$ are upper bounds of this set. From the example above, a lower bound of the set $X$ need not be contained in $X$, but if this holds, that element is a least element of $X$.

::: Definition 6
Let $A$ be an ordered set and let $X\subseteq A$. An element of $A$, $a$, is called the *greatest lower bound* (or *infimum*) of $X$ if this element is the greatest element among the lower bounds of $X$. Similarly, the *least upper bound* (or *supremum*) is also defined.
:::

If the supremum of $X\subseteq A$ exists, it is denoted by $\sup_AX$, and the infimum by $\inf_AX$. By definition, one easily checks that if $X\subseteq A$ has a greatest element $a$, then $a=\sup_AX$.

::: Proposition 7
Let $A$ be an ordered set and suppose $X\subseteq A$ has both a supremum and an infimum.

1. If $X\neq\emptyset$, then $\inf_A X\leq\sup_A X$.
2. If $X=\emptyset$, then $\sup_AX$ and $\inf_AX$ are respectively the least and greatest elements of $A$.
:::

::: Proof
1. If $X\neq\emptyset$, there exists at least one element; let this be $a$. Then by definition $\inf X\leq a$ and $a\leq\sup X$, and by transitivity $\inf_AX \leq\sup_AX$. 
2. If $X=\emptyset$, every element of $A$, $a$, satisfies, for all $x\in X$, $a\leq x$ and $x\leq a$. Therefore, every element of $A$ is both a lower bound and an upper bound of $X$, and $\sup_AX$ and $\inf_AX$ are the least and greatest elements of $A$.
:::

## Suprema, Infima, and Set Operations

We now examine the relationship between the set operations examined so far and the supremum and infimum.

::: Proposition 8
For an ordered set $A$ and two subsets $X,X'$, if $\sup_AX,\sup_AX'$ are each defined and $X'\subseteq X$, then $\sup X'\leq\sup X$.
:::

::: Proof
Choose an arbitrary $x\in X'$. Since $X'\subseteq X$, we have $x\in X$. On the other hand, for any $x\in X$, $x\leq \sup X$ holds, and therefore $\sup X$ is an upper bound of $X'$. Now by definition, $\sup X'\leq \sup X$. 
:::

::: Proposition 9
For an ordered set $A$, suppose that for all $i\in I$ we have $x_i\leq y_i$, and consider families $(x_i)_{i\in I}$, $(y_i)_{i\in I}$. If both have a supremum in $A$, then $\sup_{i\in I} x_i\leq \sup_{i\in I} y_i$.
:::

::: Proof
For any $i\in I$, we have $x_i\leq y_i$ and $y_i\leq \sup y_i$, so for all $i$, $x_i\leq \sup y_i$; therefore, by the minimality of $\sup x_i$, we have $\sup x_i\leq\sup y_i$.
:::

::: Proposition 10
For an ordered set $A$, an index set $I$, and a covering of $I$, $(J_k)_{k\in K}$, suppose that $(x_i)_{i\in J_k}$ has a supremum in $A$. Then $\sup_{i\in I} x_i$ exists if and only if $\sup_{k\in K}(\sup_{j\in J_k}x_j)$ exists, and the two values are equal.
:::

::: Proof
Write $b_k=\sup_{i\in J_k} x_i$. First suppose that $(x_i)_{i\in I}$ has a supremum, and let this be $a$. Then $a\geq b_k$ holds for all $k$. Also, if $c\geq b_k$ holds for all $k$, then for any $x_i$, with $i\in J_{k'}$, $k'$ satisfies $b_{k'}\geq x_i$, and therefore for any $i$, $c\geq x_i$. Now by the minimality of $a$ we must have $c\geq a$, and therefore $a$ is the supremum and $\sup_{i\in I}x_i=\sup_{k\in K}(\sup_{j\in J_k} x_j)$.  

Conversely, even if $(b_k)_{k\in K}$ has a supremum $a'$, the proof can be completed in the same way.
:::

::: Proposition 11
For the product of ordered sets $(A_i)_{i\in I}$, $A=\prod A_i$, and its subset $X$, let $X_i=\pr_i X$. Then $\sup_AX$ exists if and only if each $\sup_{A_i}X_i$ exists, and $\sup_AX=(\sup_{A_i}X_i)$.
:::
::: Proof
First suppose that $\sup_{A_i} X_i$ exists for each $i$. Then for any $x=(x_i)_{i\in I}\in X$, since $x_i\in X_i$, we have $x_i\leq\sup_{A_i}X_i$, and therefore $(\sup_{A_i} X_i)_{i\in I}$ is an upper bound of $X$. If $(c_i)$ were another upper bound of $X$, then each $c_i$ would be an upper bound of $X_i$, so by the minimality of $\sup_{A_i}X_i$ we have $c_i\geq\sup X_i$, and therefore $(c_i)\geq(\sup X_i)_{i\in I}$.  

Conversely, suppose that $\sup X=(a_i)$ exists. For all $i$, $a_i$ is an upper bound of $X_i$. This is because if $x_i\in X_i$, there exists, with $i$-th component $x_i$, an element $x\in X$, and this $x$ satisfies $x\leq (a_i)$. Now for any other upper bound $a_i'$, if we define a new element $(c_i)$ by replacing in $(a_i)$ the $i$-th component with $a_i'$, then since $c\geq a$, we have $a_i'\geq a_i$. 
:::

::: remark Remark {#rmk}
For an ordered set $A$ and $X'\subseteq X\subseteq A$, only one of $\sup_AX'$ and $\sup_XX'$ may exist, or both may exist but have different values. For example, let us compare $X'=\{x\in\mathbb{Q}\mid x < \sqrt{2}\}$ in each of these sets. 

1. As a subset of $X_1=\mathbb{Q}$, the supremum of this set does not exist, but it exists in $A=\mathbb{R}$. That is, even if $\sup_AX'$ exists, $\sup_{X_1}X'$ may not exist.
2. On the other hand, consider the set $X_2=X'\cup \left\{2\right\}$. Then $X'\subseteq X_2\subseteq X_1$ and $\sup_{X_2}X'=2$, but $\sup_{X_1}X'$ does not exist.
3. Finally, in $X'\subseteq X_2\subseteq A$, $\sup_{X_2}X'$ and $\sup_AX'$ each exist, but the two values differ.   
:::

Nevertheless, we can still prove the following.

::: Proposition 12
Let $A$ be an ordered set, and let $X'\subseteq X\subseteq A$. If both $\sup_AX'$ and $\sup_XX'$ exist, then $\sup_AX'\leq\sup_XX'$. If $\sup_AX'$ exists and belongs to $X$, then $\sup_XX'$ also exists and this value equals $\sup_AX'$.
:::
::: Proof
The set of upper bounds of $X'$ in $X$ is contained in the set of upper bounds in $A$, and therefore the supremum is larger. If $\sup_AX'$ exists and belongs to $X$, then this is an upper bound of $X'$ in $X$, and by its minimality in $A$, it also has minimality among the upper bounds in $X$, so in $X$, it becomes the supremum of $X'$.
:::




---
**References**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
