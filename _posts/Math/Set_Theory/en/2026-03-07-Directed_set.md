---

title: "Directed Sets"
excerpt: "Directed sets and lattices"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/directed_set
header: 
    overlay_image: /assets/images/Math/Set_Theory/Directed_set.png
    overlay_filter: 0.5
sidebar: 
    nav: "set_theory-en"

date: 2026-03-07
last_modified_at: 2026-03-07
weight: 17

---

For a preordered set $$A$$, a subset $$X\subseteq A$$ is *cofinal* (resp. *coinitial*) in $$A$$ if for any $$x\in A$$, there exists $$y\in X$$ such that $$x\leq y$$ (resp. $$y\leq x$$). For example, in the following diagram

![cofinal_sequence](/assets/images/Math/Set_Theory/Directed_set-1.png){:style="width:20em" class="invert" .align-center}

the sets $$\left\{a_{2n}\right\}_{n\in\mathbb{N}}$$ and $$\left\{a_{1000+n}\right\}_{n\in\mathbb{N}}$$ are both cofinal.

## Directed Set

In Hasse diagrams, it is conventional to place larger elements at the top, but sometimes larger elements are written on the right, as in the diagram above.

<ins id="def1">**Definition 1**</ins>  A preordered set $$A$$ is *right directed* if every two-element subset of $$A$$ is bounded above. Similarly, a preordered set $$A$$ is *left directed* if every two-element subset of $$A$$ is bounded below.
{: .definition}

For example, for any set $$A$$, the ordered set $$(\mathcal{P}(A),\subseteq)$$ is right directed. This is because for any $$X, Y\in\mathcal{P}(A)$$, $$X\cup Y$$ is an element of $$\mathcal{P}(A)$$ and is an upper bound of $$X$$ and $$Y$$. This can be represented as follows:

![directed_system](/assets/images/Math/Set_Theory/Directed_set-2.png){:style="width:24em" class="invert" .align-center}

<ins id="prop2">**Proposition 2**</ins>  If an ordered set $$A$$ is right directed, then every maximal element of $$A$$ is also a greatest element.
{: .proposition}

<details class="proof" markdown="1">
<summary>Proof</summary>

Since $$A$$ is right directed, for any $$x\in A$$ and maximal element $$a$$, there exists an upper bound $$y$$ of the set $$\{x,a\}$$. By the maximality of $$a$$, we must have $$a=y$$, so $$x\leq a$$ holds.
</details>

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> If $$(A_i)$$ is a family of right directed sets, then $$\prod A_i$$ is also right directed.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$(x_i),(y_i)\in\prod A_i$$. For each $$i$$, since $$x_i,y_i\in A_i$$ and $$A_i$$ is right directed, there exists $$z_i\in A_i$$ such that $$x_i,y_i\leq z_i$$. Now $$(x_i),(y_i)\leq(z_i)$$, so $$\prod A_i$$ is also right directed.

</details>

In general, a subset of a right directed set is not necessarily right directed. However, it is easy to verify that a cofinal subset is right directed.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> An ordered set $$A$$ is a *lattice* if every two-element subset of $$A$$ has a supremum and an infimum. In this case, the two elements $$\sup\{x,y\}$$ and $$\inf\{x,y\}$$ are called the *join* and *meet* of $$x$$ and $$y$$, respectively, and are written as $$x\vee y$$ and $$x\wedge y$$.

</div>

Every *finite* subset of a lattice $$A$$ has a supremum and an infimum. If *every* subset of $$A$$ has a supremum and an infimum, then $$A$$ is called a *complete lattice*.

## Totally Ordered Set

<ins id="def5">**Definition 5**</ins> Two elements $$x$$ and $$y$$ in a preordered set $$A$$ are *comparable* if the proposition "$$x\leq y$$ or $$y\leq x$$" holds. If every pair of elements in a set $$A$$ is comparable, then $$A$$ is called a *totally ordered set*.
{: .definition}

If $$A$$ is a totally ordered set, then trichotomy holds. That is, for any $$x, y\in A$$, exactly one of the following holds:

$$x=y,\qquad x < y,\qquad x > y$$

In this case, the negation of $$x\leq y$$ is $$x > y$$. However, without the condition that the set is totally ordered, this does not generally hold. ([§Definition of Order Relations, ⁋Remark](/en/math/set_theory/order_relations#rmk1))

<ins id="prop6">**Proposition 6**</ins> Every strictly monotone function $$f$$ from a totally ordered set $$A$$ to an ordered set $$B$$ is injective. If $$f$$ is strictly increasing, then $$f$$ is an isomorphism from $$A$$ to $$f(A)$$.
{: .proposition}
<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$f$$ be a strictly monotone function. For any $$x\neq y$$, either $$x > y$$ or $$x < y$$ holds, so $$f(x) > f(y)$$ or $$f(x) < f(y)$$, and therefore $$f(x)\neq f(y)$$, making $$f$$ injective. In particular, if $$f$$ is strictly increasing, we need to show that $$f(x)\leq f(y)\implies x\leq y$$, and its contrapositive is obvious.
</details>

The proposition above also did not hold for general ordered sets. ([§Monotone Functions, ⁋Remark](/en/math/set_theory/monotone_functions#rmk2))

<ins id="prop7">**Proposition 7**</ins> Let $$A$$ be a totally ordered set and $$X$$ be a subset of $$A$$. Then $$b\in A$$ is the supremum of $$X$$ if and only if $$b$$ is an upper bound of $$X$$, and for any $$c\in A$$ satisfying $$c < b$$, there exists $$x\in X$$ such that $$c < x\leq b$$.
{: .proposition}

<details class="proof" markdown="1">
<summary>Proof</summary>

Obvious.

</details>

Let $$A$$ be an ordered set, and suppose $$a\leq b$$. The subset $$X\subseteq A$$ consisting of all $$x$$ satisfying $$a\leq x\leq b$$ is called a *closed interval* and is denoted by $$[a,b]$$. The interval $$(a,b)$$ is called an *open interval*, which is the set of all $$x$$ satisfying $$a < x < b$$.

Additionally, the subset consisting of all $$x$$ satisfying $$x\leq a$$ is called an *unbounded* closed interval and is denoted by $$(-\infty, a]$$. The notations $$[a,\infty)$$, $$(-\infty, a)$$, and $$(a, \infty)$$ are defined similarly.


<ins id="prop8">**Proposition 8**</ins> In a lattice, the intersection of two intervals is also an interval.
{: .proposition}

---
**References**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
