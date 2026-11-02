---
title: "Properties of Well-Ordered Sets"
description: "We analyze the segment structure of well-ordered sets and rigorously construct ordinals via von Neumann's definition. We prove properties from natural numbers to general ordinals and that successor ordinals are ordinals."
excerpt: "Definition of ordinals and properties of well-ordered sets"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/well_ordering
sidebar: 
    nav: "set_theory-en"

date: 2021-08-23
weight: 20
translated_at: 2026-06-02T16:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-11-02T23:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
## The Rigorous Definition of Ordinals

In the previous post we briefly introduced ordinals, but postponed defining them until after we had defined well-ordered sets. We are now ready to define ordinal numbers rigorously.

::: Proposition 1
For a well-ordered set $A$, let $A^\ast$ be the set of all its segments. Then $(A^\ast,\subseteq)$ is also a well-ordered set, and the function $x\mapsto S_x$ is an order isomorphism between $A$ and $A^\ast\setminus\{A\}$.
:::
::: Proof
We use [§Directed Sets, ⁋Proposition 6](/en/math/set_theory/directed_set#prop6){: data-lid="0gfvz" }. Let us show that $s\colon x\mapsto S_x$ is strictly increasing and that $s(A)=A^\ast\setminus\{A\}$.

It is obvious that $s$ is an increasing function: if $x\leq y$ and $a\in S_x$, then $a < x\leq y$, so $a\in S_y$. Moreover, this inclusion is strict, since if $x < y$, then $x\not< x$ and $x < y$, so $x\not\in S_x$ but $x\in S_y$. Hence the function $s$ is an isomorphism between $A$ and its image. Therefore, by [§Ordinals and Well-Ordered Sets, ⁋Proposition 5](/en/math/set_theory/ordinals#prop5){: data-lid="zd4js" }, we have $s(A)=A^\ast\setminus\{A\}$.

Finally, let us show that $A^\ast$ is well-ordered. Since $s(A)$ is well-ordered, adding to $s(A)=A^\ast\setminus\{A\}$ the greatest element $A$ ([§Elements of Ordered Sets, ⁋Proposition 4](/en/math/set_theory/elements_in_ordered_set#prop4){: data-lid="uda3l" }) yields $A^\ast$, and the set obtained in this way is again well-ordered.
:::

Via the isomorphism in the above proposition, we may treat a well-ordered set as in the following definition:

> Each well-ordered set is a set of well-ordered sets smaller than itself, given the inclusion relation by $\subseteq$.

::: Definition 2 (von Neumann)
A set $S$ is an *ordinal* if every element of $S$ is strictly well-ordered by $\in$, and every element of $S$ is also a subset of $S$.
:::

$\emptyset$ is vacuously an ordinal, and all natural numbers are also ordinals. This is because the set representing a natural number is obviously a well-ordered set (since it is a finite set and a totally ordered set), and moreover, for example, if $2\in 3=\{0,1,2\}$, then $2=\{0,1\}$ is also a subset of $3$. It is customary to denote general ordinals by lowercase Greek letters.

More generally, the following holds.

::: Proposition 3
If $\alpha$ is an ordinal number, then $\alpha$'s successor $S(\alpha)=\alpha\cup\{\alpha\}$ is also an ordinal.
:::
::: Proof
First, every element of $S(\alpha)=\alpha\cup\{\alpha\}$ is a subset of $S(\alpha)$. The elements that were in the set $\alpha$ will also be in the set containing $\alpha$, namely $S(\alpha)$, and the newly added *element* $\alpha$ is by definition also a subset of $S(\alpha)$.
:::

The next proposition shows a way to construct *larger* ordinals by an even more general method than introducing the successor function $S$ in this way.

::: Proposition 4
Let $(A_i)_{i\in I}$ be a family of well-ordered sets, and suppose that for any $i,j\in I$, one of $A_i$ and $A_j$ is a segment of the other. Then on the set $A=\bigcup_{i\in I}A_i$, there exists a unique order relation extending the order relation of each $A_i$. This is a well-ordering, any segment of $A_i$ is a segment of $A$, and every segment of $A$ other than $A$ itself is a segment of some $A_i$.
:::

Rather than directly showing the existence and uniqueness of the desired order relation, let us prove a more general result under a condition weaker than this.

::: Lemma 5
Let $(A_i)_{i\in I}$ be a family of ordered sets that is right directed under inclusion, and suppose that whenever $A_i\subseteq A_j$, the relation obtained by restricting the order relation of $A_j$ to $A_i$ coincides with the given order relation on $A_i$. Then there exists a unique order relation on $A=\bigcup_{i\in I} A_i$ extending all of the given order relations.
:::
::: Proof
For each $A_i$, let $R_i$ be its order relation. If there exists on $A$ an ordering $R$ extending each order relation, then $R_i\subseteq R$. Conversely, if $(x,y)\in R$, then since $x$ and $y$ are contained in some $A_i,A_j$, there exists some $A_k$ containing both $x$ and $y$ simultaneously. Meanwhile, since $(x,y)\in R_k$, we have $(x,y)\in\bigcup_{i\in I}R_i$. Therefore, if such a relation exists, it is unique and must be $\bigcup_{i\in I}R_i$.

Therefore, it suffices to show that $R=\bigcup_{i\in I}R_i$ actually satisfies these conditions. First, since it is obvious by definition that $R$ extends all $R_i$, let us show that $R$ is an order relation. For any $x\in A$, if $x\in A_i$, then $(x,x)\in R_i\subseteq R$, so $(x,x)\in R$. Similarly, if $(x,y)\in R$ and $(y,x)\in R$, there exists some $A_k$ containing both $x$ and $y$ simultaneously, and by the conditions on the order relations on this set, $(x,y),(y,x)\in R_k$, so by the antisymmetry of $R_k$, we have $x=y$. To show transitivity, after assuming $(x,y)\in R$ and $(y,z)\in R$, it suffices to find, containing all of $x$, $y$, and $z$, a set $A_l$, and conclude that $(x,z)\in R_l$.
:::

It now suffices to show that the order relation defined in this way satisfies all the given properties.

::: Proof (Proposition 4)
First, let us show that all $A_i$ and their segments become segments of $A$. For any $A_i$ and $x\in A_i$, suppose that some $y\in A$ is given. Then there exists some $A_j$ such that $y\in A_j$. Now let $y\leq x$. By assumption, either $A_i$ is a segment of $A_j$ or $A_j$ is a segment of $A_i$. If $A_i$ is a segment of $A_j$, then as elements of $A_j$, $y\leq x$ implies $y\in A_i$. If conversely $A_j$ was a segment of $A_i$, then $A_j\subseteq A_i$, and in particular $y\in A_i$. In either case, $y\in A_i$, and therefore $A_i$ is a segment of $A$. Similarly, one can show that segments of $A_i$ are also segments of $A$.

Now let us show that $A$ is well-ordered. Let $X$ be an arbitrary nonempty subset of $A$. Then there exists some $A_i$ such that $X\cap A_i\neq\emptyset$. As a subset of the well-ordered set $A_i$, $A_i\cap X$ has a least element. Call it $a$. We will now show that $a$ is the least element of $X$. For any $x\in X$, one has $x\in A_j$ for some $A_j$, which either is a segment of $A_i$ or contains $A_i$ as a segment. If $A_j$ is a segment of $A_i$, then $x\in A_i$, and thus $x\in A_i\cap X$ and $a\leq x$ (minimality of $a$). Conversely, if $A_i$ is a segment of $A_j$, then $x<a$ is impossible. If that were so, then $x\in A_i$, contradicting the minimality of $a$. In either case, for any $x\in X$ we have $a\leq x$, so $a$ is the least element of $X$.

Finally, any segment $S$ is of the form $(-\infty, x)$, so if we choose, with $x\in A_i$, some $A_i$, then $(-\infty, x)$ becomes a segment of $A_i$.
:::

The main reason mathematical induction works on the natural numbers is that each natural number is defined sequentially using the successor function $S$. However, extending this idea to general ordinals presents some difficulty. Looking at the order structure of the ordinal $\omega+1$,

$$0,1,2,\cdots; \omega$$

as one must pass through infinitely many natural numbers before $\omega$ as above, it is impossible to use induction sequentially. This is due to a particular property of $\omega$. That is, appearing before $\omega$, the elements $0,1,2,\cdots$ are elements of $\omega$, and they do not have a maximal element. We first define this situation as follows.

::: Definition 6
For an arbitrary ordinal $\alpha$, if $\alpha$ has a maximal element $\beta$, we define $\alpha$ to be a *successor ordinal*; otherwise, we call $\alpha$ a *limit ordinal*.
:::

If $\alpha$ is a successor ordinal and $\beta$ is the maximal element of $\alpha$, we have given it such a name because we can write $\alpha=S(\beta)=\beta+1$.  

However, despite the existence of limit ordinals, it is possible to use something resembling induction for ordinals as well. 

::: Lemma 7 (Transfinite induction)
Let $A$ be a well-ordered set, and let $\mathcal{S}$ be a collection of segments satisfying the following conditions.

1. $\mathcal{S}$ is closed under arbitrary unions (including the union of the empty family, that is, $\emptyset\in\mathcal{S}$).
2. If $S_a\in\mathcal{S}$, then $S_a\cup\{a\}\in\mathcal{S}$.

Then every segment of $A$ belongs to $\mathcal{S}$.
:::

::: Proof
To find a contradiction, let us negate the conclusion. Since $\mathcal{S}\subseteq A^\ast$, $A^\ast\setminus\mathcal{S}$ has a least element $S$. If $S$ has no greatest element, then $S=\bigcup_{x\in S}S_x$, and by minimality each $S_x$ is an element of $\mathcal{S}$, so by 1, $S\in\mathcal{S}$. If $S$ has a greatest element $a$, then $S=S_a\cup\{a\}$, and again by minimality $S_a\in\mathcal{S}$. Now by 2, we must have $S=S_a\cup\{a\}\in\mathcal{S}$. This is a contradiction, so $A^\ast\setminus\mathcal{S}$ has no least element, and therefore $\mathcal{S}=A^\ast$.
:::

Here, $A$ is some large ordinal (regardless of whether it is a limit ordinal or a successor ordinal), and thus the existence of limit ordinals, which was an obstacle when generalizing induction, is resolved through this lemma. What makes this possible is condition 1. For example, this is because $\omega$ can be formed as the infinite union of $1,2,\ldots$.

Similarly, we can also formulate a transfinite recursion theorem for ordinals and define operations on ordinals. However, since in most cases we are interested in the order relation given on a collection of ordinals, we will not cover this here.

---
**References**

**[HJJ]** K. Hrbacek, T.J. Jeck, and T. Jech. <i>Introduction to Set Theory</i>. Lecture Notes in Pure and Applied Mathematics. M. Dekker, 1978.  
**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
