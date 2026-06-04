---
title: "Axiom of Choice"
description: "We introduce the Axiom of Choice and its equivalent formulations, prove the Well-Ordering Theorem and the Tarski-Bourbaki Fixed-Point Lemma, and define the order relations between ordinals."
excerpt: "The Axiom of Choice and its equivalents"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/axiom_of_choice
sidebar: 
    nav: "set_theory-en"

date: 2021-08-23
last_modified_at: 2022-04-14
weight: 21
translated_at: 2026-06-02T15:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-02T15:30:02+00:00
---
In this post we finally introduce the axiom of choice. We then define the order relation between ordinal numbers, which we discussed in the previous post.

## The Axiom of Choice and Its Equivalents

**The Axiom of Choice.** Every set has a choice function.
{: .misc}

Here, a choice function is a function defined on a collection of sets $$\mathcal{S}$$, such that $$f(X)\in X$$ holds for all $$X\in\mathcal{S}$$. That is, $$f$$ is a function that picks one element from each set $$X$$. In fact, we have been using this axiom implicitly all along; every time we pick an element from an arbitrary set, we are invoking it.

Next, we prove that

> Every well-ordered set is order-isomorphic to some ordinal.

As we saw in [§Ordinals and Well-Ordered Sets, ⁋Example 3](/en/math/set_theory/ordinals#ex3), many ordered sets are not well-ordered, so the condition in the above proposition may seem very restrictive. However, by a clever use of the axiom of choice, we can prove the following theorem.

<ins id="thm1">**Theorem 1. (Zermelo)**</ins> Every set $$A$$ can be well-ordered.
{: .proposition}

What this theorem means is that regardless of whether the set $$A$$ is an ordered set already equipped with an order, or merely a set with no additional structure, we can endow it with a new order relation. For example, $$(\mathbb{R},\leq)$$ is not a well-ordered set, but nevertheless we can define a suitable order relation $$\preceq$$ that makes the set $$\mathbb{R}$$ into a well-ordered set.

<div class="proposition" markdown="1">

<ins id="lem2">**Lemma 2 (Tarski-Bourbaki)**</ins> Let $$A$$ be a set, let $$\mathcal{S}\subset\mathcal{P}(A)$$, and let $$p:\mathcal{S}\rightarrow A$$ satisfy $$p(X)\not\in X$$. Then there exists a well-ordered subset $$(M,\leq)$$ satisfying the following conditions.

1. For every $$x\in X$$, we have $$S_x\in\mathcal{S}$$ and $$p(S_x)=x$$.
2. $$M\not\in\mathcal{S}$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$\mathcal{M}$$ be the collection of relations $$R\subseteq A\times A$$ satisfying the following conditions.

1. $$G$$ is a well-ordering on $$R=\pr_1R$$.
2. For each $$x\in U$$, we have $$S_x\in\mathcal{S}$$ and $$p(S_x)=x$$.

We will show that for each $$G\in\mathcal{M}$$, the set $$U=\pr_1G$$ satisfies the conditions of [§Properties of Well-Ordered Sets, ⁋Proposition 4](/en/math/set_theory/well_ordering#prop4). To this end, we show that for any $$U$$, $$U'$$, either $$U$$ is a segment of $$U'$$ or vice versa.

Let $$G$$, $$G'\in \mathcal{M}$$ be arbitrary, and let $$U$$, $$U'$$ be their domains, respectively. Let $$V$$ be the set of all $$x\in U\cap U'$$ such that (1) the segment with endpoint $$x$$ represents the same set in $$U$$ and in $$U'$$, and (2) the order on that segment agrees with $$G$$. If $$x\in V$$ and $$y\in U$$ satisfies $$y\leq x$$, then $$y\in S_x$$ in both $$U$$ and $$U'$$. Moreover, elements less than $$y$$ in $$U$$ are also less than $$y$$ in $$U'$$. Thus $$y\in V$$, and $$V$$ is a segment of $$U$$.

Now, to show that $$U$$ and $$U'$$ satisfy the desired condition, it suffices to show that either $$U=V$$ or $$U'=V$$. Assume $$V\neq U$$ and $$V\neq U'$$. Then for the least elements $$x$$ and $$x'$$ of $$U\setminus V$$ and $$U'\setminus V$$, we have $$V=S_x=S_{x'}$$ in $$U$$ and $$U'$$, respectively. However, by the second condition, $$V\in\mathcal{S}$$, so $$x=p(S_x)=p(V)=p(S_{x'})=x'$$, and thus $$x\in V$$.

Now, using [§Properties of Well-Ordered Sets, ⁋Proposition 4](/en/math/set_theory/well_ordering#prop4), we obtain the well-ordered set $$M=\bigcup_{G\in\mathcal{M}}\pr_1G$$. Trivially $$M\in\mathcal{M}$$, so $$M$$ satisfies condition 1 of the lemma. If $$M\in\mathcal{S}$$, then by the condition on $$\mathcal{S}$$ we have $$p(M)\not\in M$$. Adding a greatest element $$a=p(M)$$ to $$M$$, we obtain another well-ordered set $$M'=M\cup\{a\}$$ ($$S_a=M$$). Since $$S_a=M\in\mathcal{S}$$ and $$p(S_a)=a$$, we have $$M'\in\mathcal{M}$$, contradicting the maximality of $$M$$. Thus condition 2 of the lemma also holds.
</details>

<details class="proof--alone" markdown="1">
<summary>Proof of Theorem 1</summary>

Let $$\mathcal{S}=\mathcal{P}(A)\setminus\{A\}$$. Also, define the value $$P(X)$$ of the function $$p:\mathcal{S}\rightarrow A$$ to be some element of $$A\setminus X$$. (That is, $$P$$ is a choice function.) Then $$P(X)\not\in X$$. Now, by the preceding lemma, there exists a well-ordered subset $$M\subseteq A$$ satisfying conditions 1 and 2 of the lemma above. In particular, since $$M\not\in\mathcal{S}$$, the only $$M$$ that can satisfy this is $$A$$ itself.
</details>

Now it is time to introduce Zorn's lemma, the most widely used equivalent of the axiom of choice. First, we define the following.

<ins id="def3">**Definition 3**</ins> An ordered set $$A$$ is called *inductive* if every totally ordered subset has an upper bound.
{: .definition}

Caution is needed because the term *inductive set* can mean an entirely different concept depending on the author. A totally ordered subset is also called a *chain*.

<ins id="thm4">**Theorem 4 (Zorn's lemma)**</ins> Every inductive set has a maximal element.
{: .proposition}

Since every well-ordered set is also totally ordered, if we can prove the following proposition, the above theorem is immediate.

<ins id="prop5">**Proposition 5**</ins> An ordered set $$A$$ in which every well-ordered subset is bounded above has a maximal element.
{: .proposition}

<details class="proof" markdown="1">
<summary>Proof</summary>

If $$v$$ is an upper bound of $$X\subseteq A$$ and $$v\not\in X$$, then we call $$v\in A$$ a *strict upper bound* of $$X$$.

Now, let $$\mathcal{S}$$ be the collection of subsets of $$A$$ that have a strict upper bound, and let $$p:\mathcal{S}\rightarrow A$$ be a function picking out a strict upper bound. That is, for every $$S$$, $$p(S)$$ is a strict upper bound of $$S$$. Since $$p(S)\not\in S$$, by [§Properties of Well-Ordered Sets, ⁋Lemma 5](/en/math/set_theory/well_ordering#lem5) we obtain a well-ordered subset $$M$$. Moreover, this well-ordering coincides with the restriction of the order relation of $$A$$ to $$M$$. If $$x<y$$ holds in $$M$$, then this is equivalent to $$x\in S_y$$ (where $$S_y$$ is the segment in $$M$$), and if $$p(S_y)=y$$, then $$y$$ is a strict upper bound of $$S_y$$. (Here $$S_y$$ is a subset of $$M$$, so although it is not a segment, it has a strict upper bound $$y$$ simply as a subset.) In particular, from $$x\in S_y$$ we get that $$x<y$$ also holds in $$A$$. Since $$M$$ is now well-ordered, by hypothesis $$M$$ has an upper bound $$m$$. But by definition $$M$$ cannot have a strict upper bound, so $$m\in M$$, and if some $$m'$$ satisfies $$m\leq m'$$, then $$m=m'$$. Otherwise $$m'$$ would be a strict upper bound of $$M$$.
</details>

For completeness, let us briefly show that the three statements—the axiom of choice, Zermelo's theorem, and Zorn's lemma—are equivalent. Since we used the axiom of choice to prove Zermelo's theorem and Zorn's lemma, it now suffices to construct a choice function from each of Zermelo's theorem and Zorn's lemma.

First, assuming Zermelo's theorem, every set can be well-ordered, so for any $$S\in\mathcal{P}(A)\setminus \{\emptyset\}$$ there exists a least element. Defining $$p(S)$$ to be the least element of $$S$$ then gives the desired choice function.

Now assume Zorn's lemma and let us construct a choice function for the set $$A$$. First, collect all choice functions defined on some subset $$X$$ of $$A$$, and denote this collection by $$\mathcal{F}$$. At the very least, a choice function exists on $$X=\{a\}$$, so $$\mathcal{F}$$ is nonempty. Now, each element of $$\mathcal{F}$$ is a set, so they are ordered by inclusion $$\subseteq$$.

Now suppose a totally ordered subset $$\mathcal{C}$$ of $$\mathcal{F}$$ is given. Then $$\bigcup_{X\in\mathcal{C}} F_X$$ is a function with domain $$\mathcal{P}(\bigcup_{X\in\mathcal{C}} X)$$, so it becomes an upper bound for this collection of functions. Therefore, by Zorn's lemma there exists a maximal element. Denote it by $$F$$ and let its domain be $$\mathcal{P}(B)$$. If $$x\in A\setminus B$$, then by adding $$x$$ to $$B$$ and defining $$\tilde{f}$$ as

$$\tilde{f}(X)=\begin{cases}f(X)&\text{if }x\not\in X\\ x&\text{if }x\in X\end{cases}$$

we obtain a choice function $$\tilde{f}$$ extending $$F$$. This contradicts the maximality of $$F$$, so $$A\setminus B=\emptyset$$; that is, $$F$$ is a choice function on $$A$$.

---
**References**

**[HJJ]** K. Hrbacek, T.J. Jeck, and T. Jech. <i>Introduction to Set Theory</i>. Lecture Notes in Pure and Applied Mathematics. M. Dekker, 1978.  
**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
