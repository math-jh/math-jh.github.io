---
title: "Properties of Well-Ordered Sets"
excerpt: "Definition of ordinals and properties of well-ordered sets"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/well_ordering
header:
    overlay_image: /assets/images/Math/Set_Theory/Well_Ordering.png
    overlay_filter: 0.5
sidebar: 
    nav: "set_theory-en"

date: 2021-08-23
last_modified_at: 2022-11-29
weight: 20
translated_at: 2026-05-29T16:03:58+00:00
translation_source: kimi-cli
---
## The Rigorous Definition of Ordinals

In the previous post we briefly introduced ordinals, but postponed their definition until after we had defined well-ordered sets. We are now ready to define ordinal numbers rigorously.

<div class="proposition" markdown="1">

<ins id="prop1">**Proposition 1**</ins> Let $$A^\ast$$ be the set of all segments of a well-ordered set $$A$$. Then $$(A^\ast,\subseteq)$$ is also a well-ordered set, and the map $$x\mapsto S_x$$ is an order isomorphism between $$A$$ and $$A^\ast\setminus\{A\}$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

We use [§Directed Sets, ⁋Proposition 6](/en/math/set_theory/directed_set#prop6). We show that $$S$$ is strictly increasing and that $$s(A)=A^\ast\setminus\{A\}$$.

That $$s$$ is an increasing function is obvious: if $$x\leq y$$ and $$a\in S_x$$, then $$a < x\leq y$$, so $$a\in S_y$$. Moreover, this inclusion is strict, since if $$x < y$$, then $$x\not< x$$ and $$x < y$$, so $$x\not\in S_x$$ but $$x\in S_y$$. Hence the function $$s$$ is an isomorphism between $$A$$ and its image. Therefore, by [§Ordinals and Well-Ordered Sets, ⁋Proposition 5](/en/math/set_theory/ordinals#prop5), we have $$s(A)=A^\ast\setminus\{A\}$$.

Finally, we show that $$A^\ast$$ is well-ordered. Since $$s(A)$$ is well-ordered, adding the maximum element $$A$$ to $$s(A)=A^\ast\setminus\{A\}$$ ([§Elements of Ordered Sets, ⁋Proposition 4](/en/math/set_theory/elements_in_ordered_set#prop4)) yields $$A^\ast$$, and the resulting set is again well-ordered.

</details>

Via the isomorphism in the above proposition, we may regard each well-ordered set as

> a set of well-ordered sets smaller than itself, ordered by $$\subset$$.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2 (von Neumann)**</ins> A set $$S$$ is an *ordinal* if every element of $$S$$ is strictly well-ordered by $$\in$$, and every element of $$S$$ is also a subset of $$S$$.

</div>

$$\emptyset$$ is vacuously an ordinal, and all natural numbers are ordinals. The sets representing natural numbers are obviously well-ordered sets (since they are finite and totally ordered), and for example, if $$2\in 3=\{0,1,2\}$$, then $$2=\{0,1\}$$ is also a subset of $$3$$. It is customary to denote general ordinals by Greek lowercase letters.

More generally, the following holds.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> If $$\alpha$$ is an ordinal number, then its successor $$S(\alpha)=\alpha\cup\{\alpha\}$$ is also an ordinal.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, every element of $$S(\alpha)=\alpha\cup\{\alpha\}$$ is a subset of $$S(\alpha)$$. The elements that were in the set $$\alpha$$ will also be in $$S(\alpha)$$, which contains $$\alpha$$, and the new *element* $$\alpha$$ that we added is by definition also a subset of $$S(\alpha)$$.

</details>

The next proposition shows a way to construct *larger* ordinals that is even more general than introducing the successor function $$S$$.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> Let $$(A_i)_{i\in I}$$ be a family of well-ordered sets such that for any $$i,j\in I$$, one of $$A_i$$ or $$A_j$$ is a segment of the other. Then there exists a unique order relation on the set $$A=\bigcup_{i\in I}A_i$$. This is a well-ordering, segments of $$A_i$$ become segments of $$A$$, and every segment of $$A$$ other than $$A$$ itself is a segment of some $$A_i$$.

</div>

Rather than directly proving the existence and uniqueness of the desired order relation, let us show a more general result under a weaker condition.

<div class="proposition" markdown="1">

<ins id="lem5">**Lemma 5**</ins> Let $$(A_i)_{i\in I}$$ be a family of ordered sets that is right directed under inclusion, and suppose that whenever $$A_i\subseteq A_j$$, the relation obtained by restricting the order relation of $$A_j$$ to $$A_i$$ coincides with the given order relation on $$A_i$$. Then there exists a unique order relation on $$A=\bigcup_{i\in I} A_i$$ extending all of the given order relations.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

For each $$A_i$$, let $$R_i$$ be its order relation. If there exists an ordering $$R$$ on $$A$$ extending each order relation, then $$R_i\subseteq R$$. Conversely, if $$(x,y)\in R$$, then there exist $$A_i,A_j$$ containing $$x$$ and $$y$$ respectively, so there exists some $$A_k$$ containing both $$x$$ and $$y$$. Since $$(x,y)\in R_k$$, we have $$(x,y)\in\bigcup_{i\in I}R_i$$. Hence, if such a relation exists, it is unique and must be $$\bigcup_{i\in I}R_i$$.

Thus it suffices to show that $$R=\bigcup_{\alpha\in A}R_\alpha$$ actually satisfies these conditions. By definition it is obvious that $$R$$ extends all $$R_i$$, so we show that $$R$$ is an order relation. For any $$x\in A$$, if $$x\in X_i$$ then $$(x,x)\in R_i\subseteq R$$, so $$(x,x)\in R$$. Similarly, if $$(x,y)\in R$$, then there exists some $$X_k$$ containing both $$x$$ and $$y$$, and by the conditions on the order relations in this set, $$(y,x)\in R_k\subseteq R$$. To show transitivity, assume $$(x,y)\in R$$ and $$(y,z)\in R$$, then find a set $$X_l$$ containing $$x$$, $$y$$, and $$z$$, and conclude that $$(x,z)\in R_l$$.

</details>

We now show that the order relation defined in this way satisfies all the stated properties.

<details class="proof--alone" markdown="1">
<summary>Proof of Proposition 4</summary>

First we show that all $$A_i$$ and their segments become segments of $$A$$. For any $$A_i$$ and $$x\in A_i$$, suppose some $$y\in A$$ is given. Then there exists $$A_j$$ with $$y\in A_j$$. Now suppose $$y\leq x$$. By assumption, either $$A_i$$ is a segment of $$A_j$$ or $$A_j$$ is a segment of $$A_i$$. If $$A_i$$ is a segment of $$A_j$$, then $$y\leq x$$ as an element of $$A_j$$ implies $$y\in A_i$$. If conversely $$A_j$$ was a segment of $$A_i$$, then $$A_j\subseteq A_i$$, and in particular $$y\in A_i$$. In any case $$y\in A_i$$, and therefore $$A_i$$ is a segment of $$A$$. That segments of $$A_i$$ are also segments of $$A$$ can be shown similarly.

Now we show that $$A$$ is well-ordered. Let $$X$$ be an arbitrary subset of $$A$$. Then there exists some $$A_i$$ such that $$X\cap A_i\neq\emptyset$$. As a subset of the well-ordered set $$A_i$$, $$A_i\cap X$$ has a least element. Call it $$a$$. We now show that $$a$$ is the least element of $$X$$. For any $$x\in X$$, there exists $$A_j$$ with $$x\in A_j$$, which is either a segment of $$A_i$$ or contains $$A_i$$ as a segment. If $$A_j$$ is a segment of $$A_i$$, then $$x\in A_i$$, and thus $$x\in A_i\cap X$$ and $$a\leq x$$ (minimality of $$a$$). Conversely, if $$A_i$$ is a segment of $$A_j$$, then $$x<a$$ is impossible. If it were, then $$x\in A_i$$, contradicting the minimality of $$a$$. In any case, $$a\leq x$$ for every $$x\in X$$, so $$a$$ is the least element of $$X$$.

Finally, any segment $$S$$ is of the form $$(-\infty, x)$$, so choosing $$A_i$$ with $$x\in A_i$$ makes $$(-\infty, x)$$ a segment of $$A_i$$.

</details>

The main reason mathematical induction works on the natural numbers is that each natural number is defined sequentially using the successor function $$S$$. However, extending this idea to general ordinals presents some difficulty. Looking at the order structure of the ordinal $$\omega+1$$,

$$0,1,2,\cdots; \omega$$

we see that one must pass through infinitely many natural numbers before reaching $$\omega$$, making it impossible to use induction sequentially. This is due to a particular property of $$\omega$$: namely, the elements $$0,1,2,\cdots$$ that appear before $$\omega$$ are elements of $$\omega$$, and they have no maximal element. We first define this situation as follows.

<div class="definition" markdown="1">

<ins id="def6">**Definition 6**</ins> For an arbitrary ordinal $$\alpha$$, if a maximal element $$\beta$$ of $$\alpha$$ exists, we define $$\alpha$$ to be a *successor ordinal*; otherwise, we call $$\alpha$$ a *limit ordinal*.

</div>

If $$\alpha$$ is a successor ordinal and $$\beta$$ is the maximal element of $$\alpha$$, then we can write $$\alpha=S(\beta)=\beta+1$$, which justifies the name.

Nevertheless, despite the existence of limit ordinals, it is possible to use something resembling induction for ordinals.

<div class="proposition" markdown="1">

<ins id="lem7">**Lemma 7 (Transfinite Induction)**</ins> Let $$A$$ be a well-ordered set, and let $$\mathcal{S}$$ be a collection of segments satisfying the following conditions.

1. $$\mathcal{S}$$ is closed under arbitrary unions.
2. If $$S_a\in\mathcal{S}$$, then $$S_a\cup\{a\}\in\mathcal{S}$$.

Then every segment of $$A$$ belongs to $$\mathcal{S}$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

We argue by contradiction. Since $$\mathcal{S}\subseteq A^\ast$$, there exists a least element $$S$$ of $$A^\ast\setminus\mathcal{S}$$. If $$S$$ has no greatest element, then $$S=\bigcup_{x\in S}S_x$$, and by minimality each $$S_x$$ is an element of $$\mathcal{S}$$, so by (1), $$S\in\mathcal{S}$$. If $$S$$ has a greatest element $$a$$, then $$S=S_a\cup\{a\}$$, and again by minimality $$S_a\in\mathcal{S}$$. Then by (ii), $$S=S_a\cup\{a\}\in\mathcal{S}$$. This is a contradiction, so $$A^\ast\setminus\mathcal{S}$$ has no least element, and therefore $$\mathcal{S}=A^\ast$$.
</details>

Here, $$A$$ is some large ordinal (whether limit or successor), and thus the obstacle of the existence of limit ordinals that troubled us when generalizing induction is resolved by this lemma. What makes this possible is condition (1). For example, $$\omega$$ can be formed as the infinite union of $$1,2,\ldots$$.

Similarly, we could formulate a transfinite recursion theorem for ordinals and define operations on ordinals. However, since in most cases we are interested in the order relation given on a collection of ordinals, we will not pursue this here.

---
**References**

**[HJJ]** K. Hrbacek, T.J. Jeck, and T. Jech. <i>Introduction to Set Theory</i>. Lecture Notes in Pure and Applied Mathematics. M. Dekker, 1978.  
**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
