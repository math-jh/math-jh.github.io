---

title: "Elements in Ordered Sets"
excerpt: "Maximum, minimum, maximal, and minimal elements of ordered sets"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/elements_in_ordered_set
header: 
    overlay_image: /assets/images/Math/Set_Theory/Elements_in_ordered_set.png
    overlay_filter: 0.5
sidebar: 
    nav: "set_theory-en"

date: 2026-03-06
last_modified_at: 2026-03-06
weight: 16

---

Consider the following diagram

![diagram_representing_single_ordering](/assets/images/Math/Set_Theory/Elements_in_ordered_set-1.png){:style="width:1.4em" class="invert" .align-center}

to represent $$b\leq a$$. For instance, the diagram

![diagram_representing_two_orderings](/assets/images/Math/Set_Theory/Elements_in_ordered_set-2.png){:style="width:6em" class="invert" .align-center}

represents a situation where $$b\leq a$$ and $$c\leq a$$, but there is no particular relation between $$b$$ and $$c$$. Such a diagram is called a *Hasse diagram*.

## Maximal and Minimal Elements

<ins id="def1">**Definition 1**</ins> An element $$a$$ of an ordered set $$A$$ is a *minimal element* (resp. *maximal element*) of $$A$$ if for all $$x\in A$$, $$a\leq x$$ (resp. $$a\geq x$$) implies $$x=a$$.
{: .definition}

A minimal element need not be unique. For example, in

![diagram_representing_two_orderings](/assets/images/Math/Set_Theory/Elements_in_ordered_set-2.png){:style="width:6em" class="invert" .align-center}

both $$b$$ and $$c$$ are minimal elements of the set $$\{a,b,c\}$$. Mathematicians generally prefer such elements to be unique, so this situation is not particularly desirable.

## Least and Greatest Elements

<ins id="def2">**Definition 2**</ins> An element $$a$$ of an ordered set $$A$$ is a *least element* (resp. *greatest element*) of $$A$$ if $$a\leq x$$ (resp. $$x\leq a$$) for all $$x\in A$$.
{: .definition}

In the previous example, $$b$$ and $$c$$ cannot be least elements, since neither $$b\leq c$$ nor $$c\leq b$$ holds. By definition, a least element is unique. Moreover, the following holds.

<ins id="prop3">**Proposition 3**</ins> If $$A$$ has a least element $$a$$, then $$a$$ is the unique minimal element of $$A$$.
{: .proposition}

<details class="proof" markdown="1">
<summary>Proof</summary>

For any element $$x$$ of $$A$$, $$a\leq x$$ holds. Thus if there exists $$x\in A$$ such that $$x\leq a$$, then by antisymmetry of $$\leq$$, we must have $$x=a$$. From this we see that $$a$$ is a minimal element of $$A$$.

If $$a'$$ is another minimal element of $$A$$ and $$a'\neq a$$, then by the contrapositive of [Definition 1](#def1), we must have $$a'\not\leq a$$, which contradicts the fact that $$a$$ is a least element. Therefore $$a'=a$$.

</details>

Sometimes we need to consider a new element greater than all elements of an ordered set, or an element smaller than all elements. Such imaginary elements are conventionally denoted by $$\pm\infty$$.

<ins id="prop4">**Proposition 4**</ins> Let $$A$$ be an ordered set and $$A'=A\sqcup\{+\infty\}$$. Then there exists an order relation on $$A'$$ that extends the order relation defined on $$A$$ and has $$a$$ as its greatest element.
{: .proposition}

<details class="proof" markdown="1">
<summary>Proof</summary>

It suffices to add the elements of $$\bigcup\_{x\in A}\left\{(x, +\infty)\right\}$$ to the existing order relation.

</details>

## Upper and Lower Bounds

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> Let $$A$$ be a preordered set and $$X$$ a subset of $$A$$. If $$a\in A$$ satisfies $$a\leq x$$ (resp. $$a\geq x$$) for all $$x\in X$$, then $$a$$ is called a *lower bound* (resp. *upper bound*) of $$X$$ in $$A$$.

A set that has a lower bound (resp. upper bound) is called *bounded below* (resp. *bounded above*), and a set that is both bounded below and bounded above is simply called *bounded*.

</div>

Consider the following ordered set $$A=\{a,b,c,d,e\}$$.

![upper_and_lower_bounds](/assets/images/Math/Set_Theory/Elements_in_ordered_set-3.png){:style="width:7em" class="invert" .align-center}

Then $$a$$ is an upper bound of the set $$X=\left\{c,d,e\right\}$$ but $$b$$ is not. If we consider the set $$X'=\left\{d,e\right\}$$, then both $$a$$ and $$b$$ are upper bounds of this set. From the above example, we see that a lower bound of a set $$X$$ need not belong to $$X$$, but if it does, then that element is the least element of $$X$$.

<div class="definition" markdown="1">

<ins id="def6">**Definition 6**</ins> Let $$A$$ be an ordered set and $$X\subseteq A$$. An element $$a$$ of $$A$$ is a *greatest lower bound* (or *infimum*) of $$X$$ if it is the greatest element among the lower bounds of $$X$$. Similarly, the *least upper bound* (or *supremum*) is defined.

</div>

If the supremum of $$X\subseteq A$$ exists, we denote it by $$\sup_AX$$, and the infimum by $$\inf_AX$$. By definition, it is easy to verify that if $$X\subseteq A$$ has a greatest element $$a$$, then $$a=\sup_AX$$.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> Let $$A$$ be an ordered set and $$X\subset A$$ have both a supremum and an infimum.

1. If $$X\neq\emptyset$$, then $$\inf_A X\leq\sup_A X$$.
2. If $$X=\emptyset$$, then $$\sup_AX$$ and $$\inf_AX$$ become the least and greatest elements of $$A$$, respectively.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

1. If $$X\neq\emptyset$$, then there exists at least one element. Call it $$a$$. By definition, $$\inf X\leq a$$ and $$a\leq\sup X$$, so by transitivity, $$\inf_AX \leq\sup_AX$$.
2. If $$X=\emptyset$$, then for any element $$a$$ of $$A$$, both $$a\leq x$$ and $$x\leq a$$ hold for all $$x\in X$$. Thus every element of $$A$$ is both a lower bound and an upper bound of $$X$$, and $$\sup_AX$$ and $$\inf_AX$$ become the least and greatest elements of $$A$$, respectively.

</details>

## Operations on Sets and Bounds

Now we examine the relationship between set operations and bounds.

<ins id="prop8">**Proposition 8**</ins> For two subsets $$X,X'$$ of an ordered set $$A$$, if $$\sup_AX,\sup_AX'$$ are both defined and $$X'\subseteq X$$, then $$\sup X'\leq\sup X$$.
{: .proposition}

<details class="proof" markdown="1">
<summary>Proof</summary>
Let $$x\in X'$$ be arbitrary. Since $$X'\subseteq X$$, $$x\in X$$. On the other hand, $$x\leq \sup X$$ holds for any $$x\in X$$, and thus $$\sup X$$ is an upper bound of $$X'$$. By definition, $$\sup X'\leq \sup X$$.
</details>

<ins id="prop9">**Proposition 9**</ins> For an ordered set $$A$$, consider families $$(x_i)\_{i\in I}$$, $$(y_i)\_{i\in I}$$ satisfying $$x_i\leq y_i$$ for all $$i\in I$$. If they all have suprema in $$A$$, then $$\sup_{i\in I} x_i\leq \sup_{i\in I} y_i$$.
{: .proposition}

<details class="proof" markdown="1">
<summary>Proof</summary>

For any $$i\in I$$, $$x_i\leq y_i$$ and $$y_i\leq \sup y_i$$, so $$x_i\leq \sup y_i$$ for all $$i$$. By the minimality of $$\sup x_i$$, we have $$\sup x_i\leq\sup y_i$$.
</details>

<ins id="prop10">**Proposition 10**</ins>  For an ordered set $$A$$, an index set $$I$$, and a covering $$(J_k)_{i\in I}$$ of $$I$$, suppose $$(x_i)\_{i\in J_k}$$ has a supremum in $$A$$. Then $$\sup\_{i\in I} x_i$$ exists if and only if $$\sup\_{k\in K}(\sup\_{j\in J_k}x_j)$$ exists, and the two values are equal.
{: .proposition}

<details class="proof" markdown="1">
<summary>Proof</summary>

Write $$b_k=\sup\_{i\in J_k} x_i$$. First suppose $$(x_i)\_{i\in I}$$ has a supremum, call it $$a$$. Then $$a\leq b_k$$ holds for all $$k$$. Also, if $$c\geq b_k$$ holds for all $$k$$, then for any $$x_i$$, if $$i\in J\_{k'}$$, then $$b\_{k'}\geq x_i$$, and thus $$c\geq x_i$$ for all $$i$$. By minimality of $$a$$, we must have $$c\geq a$$, so $$a$$ is the supremum and $$\sup\_{i\in I}x_i=\sup\_{k\in K}(\sup\_{i\in J_k} x_j)$$.

Conversely, if $$(b_k)\_{k\in K}$$ has a supremum $$a'$$, the proof can be completed in the same way.

</details>

<ins id="prop11">**Proposition 11**</ins>  For the product $$A=\prod A_i$$ of ordered sets $$(A_i)\_{i\in I}$$ and a subset $$X$$ of $$A$$, let $$X_i=\pr\_i X$$. Then $$\sup_AX$$ exists if and only if $$\sup\_{A_i}X_i$$ exists for each $$i$$, and $$\sup_AX=(\sup\_{A_i}X_i)$$.
{: .proposition}
<details class="proof" markdown="1">
<summary>Proof</summary>

First suppose $$\sup\_{A_i} X_i$$ exists for each $$i$$. It is clear that $$(\sup\_{A_i} X_i)\_{i\in I}$$ is an upper bound of $$X$$. If $$(c_i)$$ were another upper bound of $$X$$, then each $$c_i$$ would be an upper bound of $$X_i$$, so by minimality of $$\sup\_{A_i}X_i$$, we have $$c_i\geq\sup X_i$$, and thus $$(c_i)\geq(\sup X_i)\_{i\in I}$$.

Conversely, suppose $$\sup X=(a_i)$$ exists. For all $$i$$, $$a_i$$ is an upper bound of $$X_i$$. For if $$x_i\in X_i$$, then there exists $$x\in X$$ with $$x_i$$ as its $$i$$th component such that $$x\leq (a_i)$$. Now for any other upper bound $$a_i'$$, define a new element $$(c_i)$$ by replacing the $$i$$th component of $$(a_i)$$ with $$a_i'$$. Then $$c\geq a$$, so $$a_i'\geq a_i$$.

</details>

<div class="remark" markdown="1">

<ins id="rmk4">**Remark**</ins>  For an ordered set $$A$$ and $$X'\subseteq X\subseteq A$$, only one of $$\sup_AX'$$ and $$\sup_XX'$$ may exist, or both may exist but with different values. For example, compare $$X'=\{x\in\mathbb{Q}\mid x < \sqrt{2}\}$$ in each of the following sets:

1. As a subset of $$X_1=\mathbb{Q}$$, the supremum of this set does not exist, but it does exist in $$A=\mathbb{R}$$. Thus even if $$\sup_AX'$$ exists, $$\sup_{X_1}X'$$ may not exist.
2. Consider the set $$X_2=X'\cup \left\{2\right\}$$. Then $$X'\subseteq X_2\subseteq X_1$$ and $$\sup\_{X_2}X'=2$$, but $$\sup_{X_1}A$$ does not exist.
3. Finally, for $$X'\subseteq X_2\subseteq A$$, both $$\sup\_{X_2}X'$$ and $$\sup\_AX'$$ exist but have different values.

</div>

Nevertheless, we can still prove the following.

<div class="proposition" markdown="1">

<ins id="prop12">**Proposition 12**</ins>  Let $$A$$ be an ordered set and $$X'\subseteq X\subseteq A$$. If both $$\sup_AX'$$ and $$\sup_XX'$$ exist, then $$\sup_AX'\leq\sup_XX'$$. If $$\sup_AX'$$ exists and belongs to $$X$$, then $$\sup_XX'$$ also exists and equals $$\sup_AX'$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>
The set of upper bounds of $$X'$$ in $$X$$ is contained in the set of upper bounds in $$A$$, and thus the supremum is larger. If $$\sup_AX'$$ exists and belongs to $$X$$, then it is clearly the supremum of $$X'$$ in $$X$$.
</details>




---
**References**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
