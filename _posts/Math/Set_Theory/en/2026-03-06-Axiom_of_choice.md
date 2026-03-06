---

title: "Axiom of Choice"
excerpt: "The axiom of choice and its equivalents"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/axiom_of_choice
header:
    overlay_image: /assets/images/Math/Set_Theory/Axiom_of_choice.png
    overlay_filter: 0.5
sidebar: 
    nav: "set_theory-en"

date: 2026-03-06
last_modified_at: 2026-03-06
weight: 21

---

In this post, we finally introduce the axiom of choice. Afterwards, we will define the order relation between ordinal numbers discussed in the previous post.


## The Axiom of Choice and Its Equivalents

**The Axiom of Choice.** Every set has a choice function.
{: .misc}

Here, a choice function is a function defined on a collection of sets $\mathcal{S}$ such that $f(X)\in X$ holds for all $X\in\mathcal{S}$. In other words, $f$ is a function that picks one element from each set $X$. We have actually been using this axiom implicitly all along—whenever we picked an element from an arbitrary set, we were doing so.

Next, we prove that

> every well-ordered set is order isomorphic to some ordinal.

As seen in [§Ordinals and Well-Ordered Sets, ⁋Example 3](/en/math/set_theory/ordinals#ex3), many ordered sets are not well-ordered, so the condition in the above proposition may seem quite restrictive. However, by using the axiom of choice properly, we can prove the following theorem.

<ins id="thm1">**Theorem 1. (Zermelo)**</ins> Every set $A$ can be well-ordered.
{: .proposition}

This theorem means that regardless of whether a set $A$ is an ordered set with a pre-existing order or just a set with no information whatsoever, we can define a new order relation on it. For example, $(\mathbb{R},\leq)$ is not a well-ordered set, but nevertheless, there exists an order relation $\preceq$ that makes the set $\mathbb{R}$ well-ordered.

<div class="proposition" markdown="1">

<ins id="lem2">**Lemma 2 (Tarski-Bourbaki)**</ins> Let $A$ be a set, $\mathcal{S}\subset\mathcal{P}(A)$, and $p:\mathcal{S}\rightarrow A$ satisfy $p(X)\not\in X$. Then there exists a well-ordered subset $(M,\leq)$ satisfying the following conditions:

1. For all $x\in X$, $S_x\in\mathcal{S}$ and $p(S_x)=x$.
2. $M\not\in\mathcal{S}$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Let $\mathcal{M}$ be the collection of relations $R\subseteq A\times A$ satisfying the following conditions:

1. $G$ is a well-ordering on $R=\pr\_1R$.
2. For each $x\in U$, $S_x\in\mathcal{S}$ and $p(S_x)=x$.

We will show that $U=\pr\_1G$ defined for each element $G$ of $\mathcal{M}$ satisfies the conditions of [§Properties of Well-Ordered Sets, ⁋Proposition 4](/en/math/set_theory/well_ordering#prop4). To do this, we show that for any $U$ and $U'$, either $U$ is a segment of $U'$ or vice versa.

Let $G$, $G'\in \mathcal{M}$ be arbitrary and let $U$, $U'$ be their domains. Let $V$ be the set of all $x\in U\cap U'$ such that (1) the segment with endpoint $x$ represents the same set in $U$ and $U'$, and (2) the order on that segment is the same as in $G$. If $x\in V$ and $y\in U$ satisfies $y\leq x$, then $y\in S_x$ in both $U$ and $U'$. Also, elements smaller than $y$ in $U$ are also smaller than $y$ in $U'$. Thus $y\in V$, and $V$ is a segment of $U$.

Now to show that $U$ and $U'$ satisfy the desired condition, it suffices to show that either $U=V$ or $U'=V$. Assume $V\neq U$ and $V\neq U'$. Then for the least elements $x$ and $x'$ of $U\setminus V$ and $U'\setminus V$, respectively, $V=S_x=S\_{x'}$ holds in both $U$ and $U'$. But by the second condition, $V\in\mathcal{S}$, so $x=p(S_x)=p(V)=p(S\_{x'})=x'$, and thus $x\in V$.

Now using [§Properties of Well-Ordered Sets, ⁋Proposition 4](/en/math/set_theory/well_ordering#prop4), we obtain a well-ordered set $M=\bigcup\_{G\in\mathcal{M}}\pr\_1G$. Clearly $M\in\mathcal{M}$, so $M$ satisfies property 1 of the proposition. If $M\in\mathcal{S}$, then by the condition on $\mathcal{S}$, $p(M)\not\in M$. Now adding $a=p(M)$ as a greatest element to $M$, we obtain another well-ordered set $M'=M\cup\{a\}$ ($S_a=M$). Since $S_a=M\in\mathcal{S}$ and $p(S_a)=a$, $M'$ becomes an element of $\mathcal{M}$, contradicting the maximality of $M$. Thus property 2 also holds.
</details>

<details class="proof--alone" markdown="1">
<summary>Proof of Theorem 1</summary>

Let $\mathcal{S}=\mathcal{P}(A)\setminus\{A\}$. Also, define the value $P(X)$ of the function $p:\mathcal{S}\rightarrow A$ to be some element of $A\setminus X$. (That is, $P$ is a choice function.) Then $P(X)\not\in X$. Now by the previous lemma, there exists a well-ordered subset $M\subseteq A$ satisfying conditions 1 and 2 of the lemma. In particular, $M\not\in\mathcal{S}$, and the only $M$ that can satisfy this is $A$.
</details>

Now it is time to introduce Zorn's lemma, the most widely used equivalent of the axiom of choice. First, we define the following.

<ins id="def3">**Definition 3**</ins> An ordered set $A$ is *inductive* if every totally ordered subset has an upper bound.
{: .definition}

Note that an inductive set may mean something entirely different depending on the author, so caution is needed. A totally ordered subset is also sometimes called a *chain*.

<ins id="thm4">**Theorem 4 (Zorn's lemma)**</ins> Every inductive set has a maximal element.
{: .proposition}

Since every well-ordered set is also a totally ordered set, if we can prove the following theorem, the above theorem becomes immediate.

<ins id="prop5">**Proposition 5**</ins> An ordered set $A$ in which every well-ordered subset is bounded above has a maximal element.
{: .proposition}

<details class="proof" markdown="1">
<summary>Proof</summary>

If $v$ is an upper bound of $X\subseteq A$ and $v\not\in X$, let us call $v\in A$ a *strict upper bound* of $X$.

Now let $\mathcal{S}$ be the collection of subsets of $A$ that have strict upper bounds, and let $p:\mathcal{S}\rightarrow A$ be a function that picks a strict upper bound. That is, for all $S$, $p(S)$ is a strict upper bound of $S$. Since $p(S)\not\in S$, by [§Properties of Well-Ordered Sets, ⁋Lemma 5](/en/math/set_theory/well_ordering#lem5), we obtain a well-ordered subset $M$. Also, this well-ordering is the same as the restriction of $A$'s order relation to $M$. If $x&lt;y$ holds in $M$, this is equivalent to $x\in S_y$ ($S_y$ is a segment in $M$), and if $p(S_y)=y$, then $y$ becomes a strict upper bound of $S_y$. (Here $S_y$ is a subset of $M$, so while not a segment, it has a strict upper bound $y$ simply as a subset.) In particular, from $x\in S_y$, $x&lt;y$ also holds in $A$. Since $M$ is well-ordered, by assumption $M$ has an upper bound $m$. But by definition, $M$ has no strict upper bound, so $m\in M$, and if some $m'$ satisfies $m\leq m'$, then $m=m'$. Otherwise, $m'$ would become a strict upper bound of $M$.
</details>

For completeness, let us briefly show that the three propositions—the axiom of choice, Zermelo's theorem, and Zorn's lemma—are equivalent. We used the axiom of choice to prove Zermelo's theorem and Zorn's lemma, so now we need to construct a choice function using each of Zermelo's theorem and Zorn's lemma.

First, assuming Zermelo's theorem, every set can be well-ordered, so every $S\in\mathcal{P}(A)\setminus \{\emptyset\}$ has a least element. Now defining $p(S)$ as the least element of $S$, $p$ is the desired choice function.

Now assume Zorn's lemma and construct a choice function for a set $A$. First, let $\mathcal{F}$ be the collection of choice functions defined on some subset $X$ of $A$. At least for $X=\{a\}$, a choice function exists, so $\mathcal{F}$ is non-empty. Now each element of $\mathcal{C}$ is a set, so they are ordered by $\subseteq$.

Now let $\mathcal{C}$ be a totally ordered subset of $\mathcal{F}$. Then $\bigcup\_{X\in\mathcal{C}} F_X$ is a function with domain $\mathcal{P}(\bigcup\_{X\in\mathcal{C}} X)$, so it becomes an upper bound of this collection of functions. Thus by Zorn's lemma, there exists a maximal element. Call it $F$ and let $\mathcal{P}(B)$ be its domain. If $x\in A\setminus B$, then adding $x$ to $B$ and defining $\tilde{f}$ by

$$\tilde{f}(X)=\begin{cases}f(X)&\text{if }x\not\in X\\ x&\text{if }x\in X\end{cases}$$

we obtain a choice function $\tilde{f}$ extending $F$. This contradicts the maximality of $F$, so $A\setminus B=\emptyset$, i.e., $F$ is a choice function for $A$.

---
**References** 

**[HJJ]** K. Hrbacek, T.J. Jeck, and T. Jech. <i>Introduction to Set Theory</i>. Lecture Notes in Pure and Applied Mathematics. M. Dekker, 1978.  
**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
