---
title: "Axiom of Choice"
description: "Introduces the definition and equivalent statements of the axiom of choice, proves the well-ordering theorem and the Tarski-Bourbaki lemma, and defines order relations on ordinals."
excerpt: "Axiom of choice and its equivalents"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/axiom_of_choice
sidebar: 
    nav: "set_theory-en"

date: 2021-08-23
weight: 21
translated_at: 2026-09-26T23:15:05+00:00
translation_source: antigravity-gemini-3.8-flash-high
---
In this post, we finally introduce the Axiom of Choice. Afterward, we define the order relation between ordinal numbers discussed in the previous post.


## The Axiom of Choice and Its Equivalents

::: misc The Axiom of Choice. {#axiom-choice}
Every set has a choice function.
:::

Here, a choice function is a function defined on a collection $\mathcal{S}$ of non-empty sets such that $f(X)\in X$ holds for all $X\in\mathcal{S}$. That is, $f$ is a function that selects an element from each set $X$. In fact, we have been using this axiom all along without realizing it, whenever we chose an element from an arbitrary set. 

Next, we prove that

> any well-ordered set is order isomorphic to some ordinal.

As seen in [§Ordinals and Well-Ordered Sets, ⁋Example 3](/en/math/set_theory/ordinals#ex3){: data-lid="yg6uq" }, many ordered sets are not well-ordered sets, so the condition of the above proposition might seem very restrictive; however, using the Axiom of Choice properly, we can prove the following theorem.

::: Theorem 1. (Zermelo)
Every set $A$ can be endowed with a well-ordering.
:::

What this theorem means is that regardless of whether the set $A$ was originally an ordered set endowed with an order or just a bare set without any structure, we can endow it with a new order relation. For example, $(\mathbb{R},\leq)$ is not a well-ordered set, but on this set $\mathbb{R}$ one can nevertheless define a suitable order relation $\preceq$ that makes it a well-ordered set.

::: Lemma 2 (Tarski-Bourbaki)
Let $A$ be a set, $\mathcal{S}\subseteq\mathcal{P}(A)$, and suppose $p:\mathcal{S}\rightarrow A$ satisfies $p(X)\not\in X$. Then there exists a well-ordered subset $M\subseteq A$ satisfying the following conditions:

1. For every $x\in M$, $S_x\in\mathcal{S}$ and $p(S_x)=x$.
2. $M\not\in\mathcal{S}$.
:::

::: Proof
Let $\mathcal{M}$ be the collection of relations $G\subseteq A\times A$ satisfying the following conditions:

1. $G$ is a well-ordering on $U=\pr_1G$.
2. For each $x\in U$, $S_x\in\mathcal{S}$ and $p(S_x)=x$.

We will show that for each element of $\mathcal{M}$, say $G$, the set $U=\pr_1G$ satisfies the condition of [§Properties of Well-Ordered Sets, ⁋Proposition 4](/en/math/set_theory/well_ordering#prop4){: data-lid="5049s" }. To this end, let us show that for any $U$ and $U'$, either $U$ is a segment of $U'$ or vice versa.

Let $G$ and $G'\in \mathcal{M}$ be given arbitrarily, and let $U$ and $U'$ be their domains. Here, for elements such that (1) the segment with endpoint $x$ represents the same set in $U$ and $U'$, and (2) the order on that segment is the same in $G$ and $G'$, let the collection of such $x\in U\cap U'$ be $V$. If $x\in V$ and $y\in U$ satisfies $y\leq x$, then in both $U$ and $U'$, we have $y\in S_x$. Moreover, in $U$, any element smaller than $y$ is in $U'$ also smaller than $y$. Therefore, $y\in V$, and $V$ is a segment of $U$.

Now, for $U$ and $U'$ to satisfy the desired condition, it suffices to show that either $U=V$ or conversely $U'=V$. Suppose that $V\neq U$ and $V\neq U'$. Then, for $U\setminus V$ and $U'\setminus V$, their least elements $x$ and $x'$ satisfy $V=S_x=S_{x'}$ in $U$ and $U'$, respectively. However, by the second condition, we have $V\in\mathcal{S}$, so $x=p(S_x)=p(V)=p(S_{x'})=x'$, and thus $x\in V$. On the other hand, since $x$ is the least element of $U\setminus V$, we have $x\not\in V$, which is a contradiction.

Now, applying [§Properties of Well-Ordered Sets, ⁋Proposition 4](/en/math/set_theory/well_ordering#prop4){: data-lid="dddqx" }, we obtain the well-ordered set $M=\bigcup_{G\in\mathcal{M}}\pr_1G$. Since the well-ordering on $M$ is clearly an element of $\mathcal{M}$, $M$ satisfies condition 1 of the lemma. If $M\in\mathcal{S}$, then by the condition on $\mathcal{S}$, we have $p(M)\not\in M$. Now, adding to $M$ the greatest element $a=p(M)$, we obtain another well-ordered set $M'=M\cup\{a\}$ ($S_a=M$). Since $S_a=M\in\mathcal{S}$ and $p(S_a)=a$, the well-ordering on $M'$ is an element of $\mathcal{M}$, contradicting the maximality of $M$. Therefore, condition 2 of the lemma also holds.
:::

::: Proof (Theorem 1)
Let $\mathcal{S}=\mathcal{P}(A)\setminus\{A\}$. Also, for the function $p:\mathcal{S}\rightarrow A$, define its value $p(X)$ to be an element of $A\setminus X$. (That is, $p$ is a choice function.) Then $p(X)\not\in X$. Now, by the preceding lemma, there exists a well-ordered subset $M\subseteq A$ satisfying conditions 1 and 2 of the lemma above. In particular, $M\not\in\mathcal{S}$, and the only $M$ that can satisfy this is $A$.
:::

Now it is time to introduce Zorn's lemma, the most widely used equivalent of the Axiom of Choice. First, let us make the following definition.

::: Definition 3
An ordered set $A$ is said to be *inductive* if every totally ordered subset has an upper bound.
:::

Note that an inductive set may refer to a completely different concept depending on the author, so caution is needed. A totally ordered subset is also called a *chain*. 

::: Theorem 4 (Zorn's lemma)
Every inductive set has a maximal element.
:::

Since every well-ordered set is also a totally ordered set, if we can prove the following theorem, the above theorem is immediate.

::: Proposition 5
An ordered set $A$ in which every well-ordered subset is bounded above has a maximal element.
:::

::: Proof
If $v$ is an upper bound of $X\subseteq A$ and $v\not\in X$, we call $v\in A$ a *strict upper bound* of $X$. 

Now let $\mathcal{S}$ be the set of subsets of $A$ that have a strict upper bound, and let $p:\mathcal{S}\rightarrow A$ be a function that chooses a strict upper bound. That is, for every $S$, $p(S)$ is a strict upper bound of $S$. Since $p(S)\not\in S$, by [Lemma 2](#lem2){: data-lid="vd8zn" } we obtain a well-ordered subset $M$. Moreover, this well-ordering is the same as the restriction of the order relation of $A$ to $M$. If $x<y$ holds in $M$, this is equivalent to $x\in S_y$ (where $S_y$ is the segment in $M$), and if $p(S_y)=y$, then $y$ is a strict upper bound of $S_y$. (Here $S_y$ is a subset of $M$, so although it is not a segment, as a mere subset it has the strict upper bound $y$.) In particular, from $x\in S_y$, $x<y$ holds in $A$ as well. Since $M$ is now well-ordered, by assumption $M$ has an upper bound $m$. However, by definition $M$ cannot have a strict upper bound, so $m\in M$, and if some $m'$ satisfies $m\leq m'$, then $m=m'$, since otherwise $m'$ would be a strict upper bound of $M$.
:::

For completeness, let us briefly show that the three propositions (namely, the Axiom of Choice, Zermelo's theorem, and Zorn's lemma) are equivalent. Since we used the Axiom of Choice when proving Zermelo's theorem and Zorn's lemma, it now suffices to construct a choice function using Zermelo's theorem and Zorn's lemma, respectively. 

First, if we assume Zermelo's theorem, every set can be well-ordered, so for any $S\in\mathcal{P}(A)\setminus \{\emptyset\}$ there exists a least element. Defining $p(S)$ to be the least element of $S$, $p$ is the desired choice function.

Now assume Zorn's lemma, and let us construct a choice function for a set $A$. First, for subsets of $A$, say $X$, let us collect the choice functions defined on $\mathcal{P}(X)\setminus\{\emptyset\}$ and denote this set by $\mathcal{F}$. Since there exists a choice function at least on $X=\{a\}$, $\mathcal{F}$ is non-empty. Now, since each element of $\mathcal{F}$ is a set, it is ordered by $\subseteq$. 

Now suppose that in $\mathcal{F}$ a totally ordered subset $\mathcal{C}$ is given. Then $\bigcup_{X\in\mathcal{C}} F_X$ is a function with domain $\mathcal{P}(\bigcup_{X\in\mathcal{C}} X)\setminus\{\emptyset\}$, so it is an upper bound of $\mathcal{C}$. Therefore, by Zorn's lemma, there exists a maximal element. Let this be $F$ and let $\mathcal{P}(B)\setminus\{\emptyset\}$ be its domain. If $x\in A\setminus B$, by adding to $B$ the element $x$ and defining $\tilde{F}$ by

$$\tilde{F}(X)=\begin{cases}F(X)&\text{if }x\not\in X\\ x&\text{if }x\in X\end{cases}$$

we obtain an extension of $F$ to a choice function $\tilde{F}$. This contradicts the maximality of $F$, so $A\setminus B=\emptyset$; that is, $F$ is a choice function for $A$.

---
**References**

**[HJJ]** K. Hrbacek, T.J. Jeck, and T. Jech. <i>Introduction to Set Theory</i>. Lecture Notes in Pure and Applied Mathematics. M. Dekker, 1978.  
**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
