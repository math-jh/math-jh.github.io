---
title: "Elements of Ordered Sets"
description: "This post introduces Hasse diagrams for ordered sets, defines minimal and maximal elements, and proves the uniqueness of minimum and maximum elements."
excerpt: "Greatest, least, maximal, and minimal elements of ordered sets"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/elements_in_ordered_set
sidebar: 
    nav: "set_theory-en"

date: 2021-08-22
last_modified_at: 2022-11-27
weight: 16
translated_at: 2026-06-02T13:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-02T13:30:02+00:00
---
Consider the following diagram

![diagram_representing_single_ordering](/assets/images/Math/Set_Theory/Elements_in_Ordered_Set-1.png){:style="width:1.4em" class="invert" .align-center}

and let it represent $$b\leq a$$. For example, the following diagram

![diagram_representing_two_orderings](/assets/images/Math/Set_Theory/Elements_in_Ordered_Set-2.png){:style="width:6em" class="invert" .align-center}

represents the situation where $$b\leq a$$ and $$c\leq a$$, but there is no particular relation between $$b$$ and $$c$$. Such a diagram is called a *Hasse diagram*.

## Maximal and Minimal Elements

<ins id="def1">**Definition 1**</ins> An element $$a$$ of an ordered set $$A$$ is called a *minimal element* (resp. *maximal element*) of $$A$$ if for all $$x\in A$$, whenever $$a\leq x$$ (resp. $$a\geq x$$), we have $$x=a$$.
{: .definition}

A minimal element need not be unique. For instance, in

![diagram_representing_two_orderings](/assets/images/Math/Set_Theory/Elements_in_Ordered_Set-2.png){:style="width:6em" class="invert" .align-center}

both $$b$$ and $$c$$ are minimal elements of the set $$\{a,b,c\}$$. Mathematicians generally prefer such elements to be unique, so this situation is not entirely satisfactory.

## Greatest and Least Elements

<ins id="def2">**Definition 2**</ins> An element $$a$$ of an ordered set $$A$$ is called a *least element* (resp. *greatest element*) of $$A$$ if for all $$x\in A$$, we have $$a\leq x$$ (resp. $$x\leq a$$).
{: .definition}

In the preceding example, neither $$b$$ nor $$c$$ can be a least element, since neither $$b\leq c$$ nor $$c\leq b$$ holds. By definition, a least element is unique. Moreover, the following holds.

<ins id="prop3">**Proposition 3**</ins> If $$A$$ has a least element $$a$$, then $$a$$ is the unique minimal element of $$A$$.
{: .proposition}

<details class="proof" markdown="1">
<summary>Proof</summary>

For any element $$x$$ of $$A$$, we have $$a\leq x$$. Thus, if there exists $$x\in A$$ such that $$x\leq a$$, then antisymmetry of $$\leq$$ implies $$x=a$$. Hence $$a$$ is a minimal element of $$A$$.

If $$a'$$ is another minimal element of $$A$$ and $$a'\neq a$$, then the contrapositive of [Definition 1](#def1) implies $$a'\not\leq a$$, which contradicts the fact that $$a$$ is a least element. Therefore $$a'=a$$.

</details>

Occasionally we must consider a new element larger than every element of an ordered set, or smaller than every element. It is common to denote such hypothetical elements by $$\pm\infty$$.

<ins id="prop4">**Proposition 4**</ins> Let $$A$$ be an ordered set and let $$A'=A\sqcup\{+\infty\}$$. Then there exists an order relation on $$A'$$ extending the order relation defined on $$A$$ and having $$+\infty$$ as its greatest element.
{: .proposition}

<details class="proof" markdown="1">
<summary>Proof</summary>

It suffices to adjoin to the original order relation the elements of $$\bigcup_{x\in A}\left\{(x, +\infty)\right\}$$.

</details>

## Suprema and Infima

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> Let $$A$$ be a preordered set and let $$X$$ be a subset of $$A$$. If $$a\in A$$ satisfies $$a\leq x$$ (resp. $$a\geq x$$) for all $$x\in X$$, we call it a *lower bound* (resp. *upper bound*) of $$X$$ in $$A$$.

A set possessing a lower bound (resp. upper bound) is called *bounded below* (resp. *bounded above*), and a set that is both bounded below and bounded above is simply called *bounded*.

</div>

Consider the ordered set $$A=\{a,b,c,d,e\}$$ shown below.

![upper_and_lower_bounds](/assets/images/Math/Set_Theory/Elements_in_Ordered_Set-3.png){:style="width:7em" class="invert" .align-center}

Then $$a$$ is an upper bound of the set $$X=\left\{c,d,e\right\}$$, but $$b$$ is not. If we consider the set $$X'=\left\{d,e\right\}$$, both $$a$$ and $$b$$ are upper bounds of this set. From the above example we see that a lower bound of a set $$X$$ need not belong to $$X$$; however, if it does, then that element is a least element of $$X$$.

<div class="definition" markdown="1">

<ins id="def6">**Definition 6**</ins> Let $$A$$ be an ordered set and let $$X\subseteq A$$. An element $$a$$ of $$A$$ is called the *greatest lower bound* (or *infimum*) of $$X$$ if it is the greatest element among the lower bounds of $$X$$. Similarly, the *least upper bound* (or *supremum*) is defined.

</div>

If the supremum of $$X\subseteq A$$ exists, we denote it by $$\sup_AX$$, and the infimum by $$\inf_AX$$. By definition, one easily checks that if $$X\subseteq A$$ has a greatest element $$a$$, then $$a=\sup_AX$$.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> Let $$A$$ be an ordered set and suppose $$X\subset A$$ has both a supremum and an infimum.

1. If $$X\neq\emptyset$$, then $$\inf_A X\leq\sup_A X$$.
2. If $$X=\emptyset$$, then $$\sup_AX$$ and $$\inf_AX$$ are the least and greatest elements of $$A$$, respectively.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

1. If $$X\neq\emptyset$$, then there exists at least one element; let this be $$a$$. Then by definition $$\inf X\leq a$$ and $$a\leq\sup X$$, and by transitivity $$\inf_AX \leq\sup_AX$$.
2. If $$X=\emptyset$$, then every element $$a$$ of $$A$$ satisfies $$a\leq x$$ and $$x\leq a$$ for all $$x\in X$$. Therefore every element of $$A$$ is both a lower bound and an upper bound of $$X$$, and $$\sup_AX$$ and $$\inf_AX$$ are the least and greatest elements of $$A$$.

</details>

## Suprema, Infima, and Set Operations

We now examine the relationship between the set operations we have seen and suprema and infima.

<ins id="prop8">**Proposition 8**</ins> For two subsets $$X,X'$$ of an ordered set $$A$$, if $$\sup_AX$$ and $$\sup_AX'$$ are defined and $$X'\subseteq X$$, then $$\sup X'\leq\sup X$$.
{: .proposition}

<details class="proof" markdown="1">
<summary>Proof</summary>
Choose an arbitrary $$x\in X'$$. Since $$X'\subseteq X$$, we have $$x\in X$$. On the other hand, for any $$x\in X$$ we have $$x\leq \sup X$$, and therefore $$\sup X$$ is an upper bound of $$X'$$. Hence by definition $$\sup X'\leq \sup X$$. 
</details>

<ins id="prop9">**Proposition 9**</ins> For an ordered set $$A$$, consider families $$(x_i)_{i\in I}$$ and $$(y_i)_{i\in I}$$ satisfying $$x_i\leq y_i$$ for all $$i\in I$$. If both have suprema in $$A$$, then $$\sup_{i\in I} x_i\leq \sup_{i\in I} y_i$$.
{: .proposition}

<details class="proof" markdown="1">
<summary>Proof</summary>

For any $$i\in I$$, we have $$x_i\leq y_i$$ and $$y_i\leq \sup y_i$$, so $$x_i\leq \sup y_i$$ for all $$i$$. Therefore, by the minimality of $$\sup x_i$$, we have $$\sup x_i\leq\sup y_i$$.
</details>

<ins id="prop10">**Proposition 10**</ins> Let $$A$$ be an ordered set, $$I$$ an index set, and $$(J_k)_{k\in K}$$ a covering of $$I$$, and suppose that $$(x_i)_{i\in J_k}$$ has a supremum in $$A$$ for each $$k$$. Then $$\sup_{i\in I} x_i$$ exists if and only if $$\sup_{k\in K}(\sup_{j\in J_k}x_j)$$ exists, and the two values are equal.
{: .proposition}

<details class="proof" markdown="1">
<summary>Proof</summary>

Write $$b_k=\sup_{i\in J_k} x_i$$. First suppose that $$(x_i)_{i\in I}$$ has a supremum, and denote it by $$a$$. Then $$a\leq b_k$$ holds for all $$k$$. Also, if $$c\geq b_k$$ holds for all $$k$$, then for any $$x_i$$ there is a $$k'$$ with $$i\in J_{k'}$$, which satisfies $$b_{k'}\geq x_i$$; hence $$c\geq x_i$$ for any $$i$$. Now by the minimality of $$a$$ we must have $$c\geq a$$, and therefore $$a$$ is the supremum and $$\sup_{i\in I}x_i=\sup_{k\in K}(\sup_{j\in J_k} x_j)$$.

Conversely, if $$(b_k)_{k\in K}$$ has a supremum $$a'$$, the proof can be completed in the same way.

</details>

<ins id="prop11">**Proposition 11**</ins> For the product $$A=\prod A_i$$ of ordered sets $$(A_i)_{i\in I}$$ and a subset $$X$$ thereof, let $$X_i=\pr_i X$$. Then $$\sup_AX$$ exists if and only if each $$\sup_{A_i}X_i$$ exists, and $$\sup_AX=(\sup_{A_i}X_i)$$.
{: .proposition}
<details class="proof" markdown="1">
<summary>Proof</summary>

First suppose that $$\sup_{A_i} X_i$$ exists for each $$i$$. Then it is obvious that $$(\sup_{A_i} X_i)_{i\in I}$$ is an upper bound of $$X$$. If $$(c_i)$$ were another upper bound of $$X$$, then each $$c_i$$ would be an upper bound of $$X_i$$, so by the minimality of $$\sup_{A_i}X_i$$ we have $$c_i\geq\sup X_i$$, and therefore $$(c_i)\geq(\sup X_i)_{i\in I}$$.

Conversely, suppose $$\sup X=(a_i)$$ exists. For all $$i$$, $$a_i$$ is an upper bound of $$X_i$$. Indeed, if $$x_i\in X_i$$, then there exists $$x\in X$$ whose $$i$$-th component is $$x_i$$ and which satisfies $$x\leq (a_i)$$. Now for any other upper bound $$a_i'$$, define a new element $$(c_i)$$ by replacing the $$i$$-th component of $$(a_i)$$ with $$a_i'$$; then $$c\geq a$$, so $$a_i'\geq a_i$$.

</details>

<div class="remark" markdown="1">

**Remark**</ins> For an ordered set $$A$$ and $$X'\subseteq X\subseteq A$$, it may happen that only one of $$\sup_AX'$$ and $$\sup_XX'$$ exists, or that both exist but take different values. For instance, let us compare $$X'=\{x\in\mathbb{Q}\mid x < \sqrt{2}\}$$ in various sets.

1. As a subset of $$X_1=\mathbb{Q}$$, this set has no supremum, but it does in $$A=\mathbb{R}$$. That is, even if $$\sup_AX'$$ exists, $$\sup_{X_1}X'$$ may not exist.
2. On the other hand, consider the set $$X_2=X'\cup \left\{2\right\}$$. Then $$X'\subseteq X_2\subseteq X_1$$ and $$\sup_{X_2}X'=2$$, but $$\sup_{X_1}X'$$ does not exist.
3. Finally, in $$X'\subseteq X_2\subseteq A$$, both $$\sup_{X_2}X'$$ and $$\sup_AX'$$ exist but the two values differ.

</div>

Nevertheless, we can still prove the following.

<div class="proposition" markdown="1">

<ins id="prop12">**Proposition 12**</ins> Let $$A$$ be an ordered set and let $$X'\subseteq X\subseteq A$$. If both $$\sup_AX'$$ and $$\sup_XX'$$ exist, then $$\sup_AX'\leq\sup_XX'$$. If $$\sup_AX'$$ exists and belongs to $$X$$, then $$\sup_XX'$$ also exists and equals $$\sup_AX'$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>
The set of upper bounds of $$X'$$ in $$X$$ is contained in the set of upper bounds of $$X'$$ in $$A$$; hence the supremum in $$X$$ is larger. If $$\sup_AX'$$ exists and belongs to $$X$$, then it is evidently the supremum of $$X'$$ in $$X$$.
</details>




---
**References**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
