---

title: "Properties of Well-Ordered Sets"
excerpt: "Rigorous definition of ordinals and properties of well-ordered sets"

categories: [Math / Set Theory]
permalink: math/set_theory/well_ordering
header:
    overlay_image: /assets/images/Math/Set_Theory/Well_ordering.png
    overlay_filter: 0.5
sidebar: 
    nav: "set_theory-en"

date: 2026-03-06
last_modified_at: 2026-03-06
weight: 20

---

## Rigorous Definition of Ordinals

In the previous post, we briefly introduced ordinals and postponed their definition until after defining well-ordered sets. We are now ready to define ordinal numbers rigorously.

<div class="proposition" markdown="1">

<ins id="prop1">**Proposition 1**</ins> Let $$A^\ast$$ be the set of all segments of a well-ordered set $$A$$. Then $$(A^\ast,\subseteq)$$ is also a well-ordered set, and the function $$x\mapsto S_x$$ is an order isomorphism between $$A$$ and $$A^\ast\setminus\{A\}$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

We use [§Directed Sets, ⁋Proposition 6](math/set_theory/directed_set#prop16). Let us show that $$S$$ is strictly increasing and $$s(A)=A^\ast\setminus\{A\}$$.

It is clear that $$s$$ is an increasing function. For if $$x\leq y$$ and $$a\in S_x$$, then $$a < x\leq y$$, so $$a\in S_y$$. Moreover, this inclusion is strict: if $$x < y$$, then $$x\not< x$$ and $$x < y$$, so $$x\not\in S_x$$ but $$x\in S_y$$. Thus the function $$s$$ is an isomorphism between $$A$$ and its image. Therefore by [§Ordinals and Well-Ordered Sets, ⁋Proposition 5](math/set_theory/ordinals#prop5), $$s(A)=A^\ast\setminus\{A\}$$.

Finally, let us show that $$A^\ast$$ is well-ordered. Since $$s(A)$$ is well-ordered, adding the greatest element $$A$$ to $$s(A)=A^\ast\setminus\{A\}$$ ([§Elements in Ordered Sets, ⁋Proposition 4](math/set_theory/elements_in_ordered_set#prop4)) yields $$A^\ast$$, and the resulting set is again well-ordered.

</details>

Through the isomorphism of the above proposition, we may treat a well-ordered set according to the following definition:

> Each well-ordered set is a set with an inclusion relation $$\subset$$ given to well-ordered sets smaller than itself.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2 (von Neumann)**</ins> A set $$S$$ is an *ordinal* if each element of $$S$$ is strictly well-ordered by $$\in$$, and each element of $$S$$ is also a subset of $$S$$.

</div>

$$\emptyset$$ is vacuously an ordinal, and all natural numbers are also ordinals. It is clear that a set representing a natural number is a well-ordered set (since it is finite and totally ordered), and for example, if $$2\in 3=\{0,1,2\}$$, then $$2=\{0,1\}$$ is also a subset of $$3$$. It is conventional to denote general ordinals with lowercase Greek letters.

More generally, the following holds.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> If $$\alpha$$ is an ordinal number, then its successor $$S(\alpha)=\alpha\cup\{\alpha\}$$ is also an ordinal.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, every element of $$S(\alpha)=\alpha\cup\{\alpha\}$$ is a subset of $$S(\alpha)$$. Elements in the set $$\alpha$$ will be in $$S(\alpha)$$, which contains $$\alpha$$, and the *element* $$\alpha$$ that we newly added is, by definition, also a subset of $$S(\alpha)$$.

</details>

The following proposition shows an even more general method of creating *larger* ordinals than simply introducing the successor function $$S$$.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> Let $$(A_i)_{i\in I}$$ be a family of well-ordered sets such that for any $$i,j\in I$$, one of $$A_i$$ and $$A_j$$ is a segment of the other. Then there exists a unique order relation on the set $$A=\bigcup_{i\in I}A_i$$. This is a well-ordering, and segments of $$A_i$$ become segments of $$A$$, and every segment of $$A$$ other than $$A$$ itself becomes a segment of some $$A_i$$.

</div>

Rather than directly proving the existence and uniqueness of the desired order relation, let us prove a more general result under weaker conditions.

<div class="proposition" markdown="1">

<ins id="lem5">**Lemma 5**</ins> Let $$(A_i)_{i\in I})$$ be a family of ordered sets that is right directed with respect to inclusion, and suppose that whenever $$A_i\subseteq A_j$$, <phrase>the restriction of the order relation on $A_j$ to $A_i$</phrase> coincides with the order relation given on $$A_i$$. Then there exists a unique order relation on $$A=\bigcup_{i\in I} A_i$$ that extends each of the order relations.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

For each $$A_i$$, let $$R_i$$ be the order relation. If an ordering $$R$$ on $$A$$ extending each order relation exists, then $$R_i\subseteq R$$. Conversely, if $$(x,y)\in R$$, then there exist $$A_i$$ and $$A_j$$ containing $$x$$ and $$y$$, so there exists some $$A_k$$ containing both $$x$$ and $$y$$. Since $$(x,y)\in R_k$$, we have $$(x,y)\in\bigcup_{i\in I}R_i$$. Thus if such a relation exists, it is unique and must be $$\bigcup_{i\in I}R_i$$.

Therefore, we only need to show that $$R=\bigcup_{\alpha\in A}R_\alpha$$ actually satisfies these conditions. First, by definition, it is clear that $$R$$ extends all $$R_i$$, so let us show that $$R$$ is an order relation. For any $$x\in A$$, if $$x\in X_i$$, then $$(x,x)\in R_i\subseteq R$$, so $$(x,x)\in R$$. Similarly, if $$(x,y)\in R$$, then there exists some $$X_k$$ containing both $$x$$ and $$y$$, and by the conditions on the order relations in this set, $$(y,x)\in R_k\subseteq R$$. To show transitivity, assume $$(x,y)\in R$$ and $$(y,z)\in R$$, find a set $$X_l$$ containing $$x$$, $$y$$, and $$z$$, and conclude $$(x,z)\in R_l$$.

</details>

Now we only need to show that the order relation defined in this way satisfies all the given properties.

<details class="proof--alone" markdown="1">
<summary>Proof of Proposition 4</summary>

First, let us show that all $$A_i$$ and their segments become segments of $$A$$. For any $$A_i$$ and $$x\in A_i$$, suppose some $$y\in A$$ is given. Then there exists $$A_j$$ such that $$y\in A_j$$. Now let $$y\leq x$$. By assumption, either $$A_i$$ is a segment of $$A_j$$ or $$A_j$$ is a segment of $$A_i$$. If $$A_i$$ is a segment of $$A_j$$, then $$y\leq x$$ as an element of $$A_j$$ means $$y\in A_i$$. Conversely, if $$A_j$$ was a segment of $$A_i$$, then $$A_j\subseteq A_i$$, and in particular $$y\in A_i$$. In any case, $$y\in A_i$$, and thus $$A_i$$ is a segment of $$A$$. Segments of $$A_i$$ can similarly be shown to be segments of $$A$$.

Now let us show that $$A$$ is well-ordered. Let $$X$$ be an arbitrary subset of $$A$$. Then there exists $$A_i$$ such that $$X\cap A_i\neq\emptyset$$. As a subset of the well-ordered set $$A_i$$, $$A_i\cap X$$ has a least element. Call it $$a$$. We will show that $$a$$ is the least element of $$X$$. For any $$x\in X$$, there exists $$A_j$$ such that $$x\in A_j$$, and this is either a segment of $$A_i$$ or contains $$A_i$$ as a segment. If $$A_j$$ is a segment of $$A_i$$, then $$x\in A_i$$, so $$x\in A_i\cap X$$ and $$a\leq x$$ (by minimality of $$a$$). Conversely, if $$A_i$$ is a segment of $$A_j$$, then $$x<a$$ is impossible. If that were the case, $$x\in A_i$$, contradicting the minimality of $$a$$. In any case, for any $$x\in X$$, we have $$a\leq x$$, so $$a$$ is the least element of $$X$$.

Finally, since any segment $$S$$ is of the form $$(-\infty, x)$$, choosing $$A_i$$ such that $$x\in A_i$$ makes $$(-\infty, x)$$ a segment of $$A_i$$.

</details>

The main reason induction holds for natural numbers is that each natural number is defined sequentially using the successor function $$S$$. However, extending this idea to general ordinals presents some difficulties. Examining the order structure of the ordinal $$\omega+1$$:

$$0,1,2,\cdots; \omega$$

we see that there are infinitely many natural numbers before $$\omega$$, making it impossible to apply induction sequentially. This is due to a specific property of $$\omega$$. That is, the $$0,1,2,\cdots$$ appearing before $$\omega$$ are elements of $$\omega$$, and they have no maximal element. First, we define this situation as follows.

<div class="definition" markdown="1">

<ins id="def6">**Definition 6**</ins> For any ordinal $$\alpha$$, if $$\alpha$$ has a maximal element $$\beta$$, then $$\alpha$$ is defined to be a *successor ordinal*; otherwise, $$\alpha$$ is called a *limit ordinal*.

</div>

If $$\alpha$$ is a successor ordinal and $$\beta$$ is the maximal element of $$\alpha$$, then we can write $$\alpha=S(\beta)=\beta+1$$, which is why such a name was given.

However, despite the existence of limit ordinals, it is possible to use something similar to induction for ordinals as well.

<div class="proposition" markdown="1">

<ins id="lem7">**Lemma 7 (Transfinite induction)**</ins> Let $$A$$ be a well-ordered set and $$\mathcal{S}$$ be a collection of segments satisfying the following conditions:

1. $$\mathcal{S}$$ is closed under arbitrary unions.
2. If $$S_a\in\mathcal{S}$$, then $$S_a\cup\{a\}\in\mathcal{S}$$.

Then every segment of $$A$$ belongs to $$\mathcal{S}$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Assume the conclusion is false and derive a contradiction. Since $$\mathcal{S}\subseteq A^\ast$$, there exists a least element $$S$$ of $$A^\ast\setminus\mathcal{S}$$. If $$S$$ has no greatest element, then $$S=\bigcup_{x\in S}S_x$$, and by minimality, each $$S_x$$ is an element of $$\mathcal{S}$$, so by condition 1, $$S\in\mathcal{S}$$. If $$S$$ has a greatest element $$a$$, then $$S=S_a\cup\{a\}$$, and again by minimality, $$S_a\in\mathcal{S}$$. Now by condition (ii), $$S=S_a\cup\{a\}\in\mathcal{S}$$ must hold. This is a contradiction, so the least element of $$A^\ast\setminus\mathcal{S}$$ does not exist, and thus $$\mathcal{S}=A^\ast$$.
</details>

Here, $$A$$ can be some large ordinal (whether a limit ordinal or a successor ordinal), and thus the existence of limit ordinals that was an obstacle when generalizing induction is resolved through this lemma. What makes this possible is condition 1. For example, $$\omega$$ can be created as an infinite union of $$1,2,\ldots$$.

Similarly, we can formulate a transfinite recursion theorem for ordinals to define operations on ordinals. However, since in most cases we are interested in the order relation given on a collection of ordinals, we will not cover this here.

---
**References** 

**[HJJ]** K. Hrbacek, T.J. Jeck, and T. Jech. <i>Introduction to Set Theory</i>. Lecture Notes in Pure and Applied Mathematics. M. Dekker, 1978.  
**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---


