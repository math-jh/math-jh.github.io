---

title: "Order Relations Between Ordinals"
excerpt: "Order relations between ordinals and the rigorous definition of cardinals"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/order_relations_between_ordinals
header:
    overlay_image: /assets/images/Math/Set_Theory/Order_relations_between_ordinals.png
    overlay_filter: 0.5
sidebar: 
    nav: "set_theory-en"

date: 2026-03-07
last_modified_at: 2026-03-07
weight: 22

---

## Order Relations Between Ordinals

By definition, any ordinal is a well-ordered set. Moreover, the converse also holds.

<div class="proposition" markdown="1">

<ins id="prop1">**Proposition 1**</ins> Let $$A,B$$ be two well-ordered sets. Then at least one of the following holds:
1. There exists an order isomorphism from $$A$$ to a segment of $$B$$, or
2. There exists an order isomorphism from $$B$$ to a segment of $$A$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$\mathcal{F}$$ be the set of isomorphisms from segments of $$A$$ to segments of $$B$$. First, we show that $$\mathcal{F}$$ is inductive.

Suppose we are given a totally ordered subset $$\mathcal{G}$$ of $$\mathcal{F}$$. Then we can form the set $$S$$ by taking the union of the domains of all $$u\in\mathcal{G}$$. Since $$S$$ is a union of segments of $$A$$, it is again a segment of $$A$$. Now, let $$\fun(A,B)$$ be the collection of functions from subsets of $$A$$ to $$B$$. It is clear that this set is inductive with respect to function extension. Since $$\bigcup\mathcal{G}$$ consists of functions from subsets of $$A$$ to subsets of $$B$$, let $$v$$ be the least upper bound of $$\mathcal{G}$$ in $$\fun(A,B)$$. Then $$v(S)$$ is the union of the ranges of all $$u\in\mathcal{G}$$, so it becomes a segment of $$B$$, and for any $$x, y$$, choosing $$u\in \mathcal{G}$$ that contains both $$x$$ and $$y$$ yields

$$v(x)=u(x) < u(y)=v(y)$$

which shows that $$v$$ is an isomorphism from $$S$$ to $$v(S)$$. Therefore, $$\mathcal{F}$$ is inductive.

By Zorn's lemma, $$\mathcal{F}$$ has a maximal element. Let us call it $$u_0$$, and denote its domain by $$S_0$$. We need to show that either $$S_0=A$$ or $$u_0(S_0)=B$$.

If neither holds, then there exist $$a\in A$$ and $$b\in B$$ such that $$S_0=(-\infty, a)$$ and $$u_0(S_0)=(-\infty, b)$$. Now, adding $$(a,b)$$ to $$u_0$$ yields a new function that strictly extends $$u_0$$, which contradicts the maximality of $$u_0$$. Hence, either $$S_0=A$$ or $$u_0(S_0)=B$$.

</details>

As mentioned earlier, since every ordinal is a well-ordered set, the above proposition opens the way to view any well-ordered set as a segment that is order isomorphic to an initial segment of some ordinal. However, to achieve this, we need to introduce the following new axiom.

<div class="misc" markdown="1">

**The Axiom schema of Replacement.** Let $$P(x,y)$$ be a property satisfying

> For any $$x$$, there always exists a $$y$$ such that $$P(x,y)$$ holds.

Then for any set $$A$$, there exists another set $$B$$ such that

> For each $$x\in A$$, there exists a suitable $$y\in B$$ such that $$P(x,y)$$ holds.

</div>

Given a $$P$$ satisfying the above condition, we can regard it as a function $$F$$ that takes $$x$$ as input and produces $$y$$ as output. However, functions were originally defined with a specified target, whereas the correspondence created by this condition $$P$$ provides no information about the target whatsoever—this is why an axiom schema is needed rather than a single axiom. In any case, if the replacement schema is given, we can properly define the target $$B$$, and then by applying the comprehension schema to $$B$$ with the condition

> $$(x,y)\in F$$ for some $$x$$

we can equivalently define the *image* of $$A$$ under $$F$$.

<div class="proposition" markdown="1">

<ins id="thm2">**Theorem 2**</ins> Every well-ordered set is order isomorphic to a unique ordinal.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$A$$ be a well-ordered set, and let $$X$$ be the set of all $$x\in A$$ satisfying

> $$S_x$$ is order isomorphic to some ordinal.

Since no ordinal is order isomorphic to any ordinal other than itself, we can assign a unique ordinal $$\alpha_x$$ to each $$x\in A$$ belonging to $$X$$. Our goal is to show that the set $$B$$ collecting all such ordinals becomes an ordinal that is order isomorphic to $$A$$, but first we need to show that such a set exists.

To this end, let us define the property $$P(x,y)$$ as follows:

> (i) $$x\in X$$ and $$y$$ is an ordinal order isomorphic to $$S_x$$, or
> (ii) $$x\not\in X$$ and $$y=\emptyset$$.

This property assigns either a unique ordinal $$y$$ or (equally uniquely) the empty set $$\emptyset$$, so we can apply the axiom schema of replacement. By doing so, for the function $$F$$ defined by $$P$$, we know that the set $$F(A)$$ exists. Let us call this set $$B$$.

1. Since $$B$$ is a set of ordinals, it is well-ordered by $$\in$$.
2. For any $$\alpha_x\in B$$, if $$\gamma\in\alpha_x$$, then we can consider the inverse image $$\varphi^{-1}(\gamma)\in S_x$$ under the order isomorphism $$\varphi$$ between $$\alpha_x$$ and $$S_x$$. Denoting this by $$c$$, the restriction of $$\varphi$$ to $$S_c$$ defines an order isomorphism between $$S_c$$ and $$\gamma$$, so by the definition of $$B$$, we have $$\gamma\in B$$.

From the above, we conclude that $$B$$ is an ordinal number. Moreover, applying the proof of step 2 verbatim, we can show that for any $$x\in X$$, if $$y<x$$, then $$y\in X$$. That is, $$X$$ is a segment of $$A$$, and thus either $$X=S_x$$ or $$X=A$$.

Now, to show that $$X=A$$, let us proceed by contradiction. First, we can define $$f:X\rightarrow B$$ by $$f(x)=\alpha_x$$, and in this case, one can verify that $$f$$ becomes an order isomorphism between $$B$$ and $$X$$. However, if $$X=S_x$$, then since $$B$$ is an ordinal, this would mean that $$S_x$$ is isomorphic to the ordinal $$B$$, and by definition, we must have $$x\in X$$. This is a contradiction, so $$X=A$$.

</details>

## Definition of Cardinal Numbers

We now introduce the rigorous definition of cardinality. However, our full treatment of cardinals will be in the next article (using the non-rigorous definition), and our present focus is solely on *defining the size of a set in a rigorous manner*. For example, defining operations between cardinals will use the definition from the next article; readers interested in a rigorous treatment of these should consult Chapters 7 and 9 of **[HJJ]**.

The definition of cardinality that we will consider in the next article defines the size of a set using bijections between sets. For example, since there exists a bijection between any two sets with two elements, we would consider them to have the same size. This definition does not align well with ordinals in some sense; for instance, $$\omega$$ and $$\omega+1$$ are certainly different sets from the ordinal perspective, but there exists a bijection between them (ignoring the order). To reconcile these, we can define the following.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> For any set $$A$$, the smallest ordinal number that does not admit a bijection with any subset of $$A$$ is called the *Hartogs number* of $$A$$ and is denoted by $$h(A)$$.

</div>

Successor ordinals admit bijections with their *preceding* ordinals, so they cannot be the Hartogs number of any set. Even looking at limit ordinals, $$\omega$$ and $$\omega\cdot 2$$ should have the same cardinality. For this reason, we introduce the following new concept.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> An ordinal $$\alpha$$ is called an *initial ordinal* if for all $$\beta<\alpha$$, there is no bijection between $$\beta$$ and $$\alpha$$.

</div>

Then the size of any set can be expressed as the size of an initial ordinal. Given a set $$X$$, we can equip it with a well-ordering to select an ordinal $$\alpha$$, and then choose the smallest among all ordinals of the same cardinality (using well-ordering).

We can define cardinal numbers using ordinal numbers. Consider collecting all infinite initial ordinals and labeling them in order as the 0th, 1st, ... That is, $$\omega_0$$ equals the 0th initial ordinal, namely $$\omega$$, and then we define $$\omega_1,\omega_2,\ldots$$ with strictly increasing cardinalities. When defining cardinals, it is customary to write these as $$\aleph_\alpha$$ (rather than using $$\omega$$, which denotes ordinals).

---
**References**

**[HJJ]** K. Hrbacek, T.J. Jeck, and T. Jech. *Introduction to Set Theory*. Lecture Notes in Pure and Applied Mathematics. M. Dekker, 1978.

---
