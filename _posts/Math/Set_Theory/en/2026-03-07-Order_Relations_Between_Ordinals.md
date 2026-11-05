---
title: "Order Relations Between Ordinals"
description: "We show that any well-ordered set can be viewed as an initial segment of some ordinal by using the properties of ordinals, and to achieve this we introduce the Axiom Schema of Replacement."
excerpt: "Order relations between ordinals and the rigorous definition of cardinals"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/order_relations_between_ordinals
sidebar: 
    nav: "set_theory-en"

date: 2022-11-29
weight: 22
translated_at: 2026-06-02T22:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-11-05T15:15:07+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
## Order Relations Between Ordinals

By definition, every ordinal is a well-ordered set. Moreover, it can also be said that the converse holds.

::: Proposition 1
Let $A,B$ be two well-ordered sets. Then at least one of the following holds:
1. There exists an order isomorphism from $A$ to a segment of $B$, or
2. There exists an order isomorphism from $B$ to a segment of $A$.
:::
::: Proof
Let $\mathcal{F}$ be the set of isomorphisms from a segment of $A$ to a segment of $B$. First, we show that $\mathcal{F}$ is inductive.

Suppose a totally ordered subset of $\mathcal{F}$, denoted $\mathcal{G}$, is given. Then, by taking the union of the domains of all $u\in\mathcal{G}$, we can form the set $S$. Since this set $S$ is a union of segments of $A$, it is again a segment of $A$. Meanwhile, let $\fun(A,B)$ be the collection of functions from subsets of $A$ to $B$. Then it is clear that this collection is inductive with respect to function extension. Now, since $\bigcup\mathcal{G}$ consists of functions from subsets of $A$ to subsets of $B$, let the least upper bound of $\mathcal{G}$ in $\fun(A,B)$ be $v$. Then $v(S)$ is the union of the ranges of all $u\in\mathcal{G}$, hence a segment of $B$; and for any $x<y$, choosing, to contain both $x$ and $y$, some $u\in \mathcal{G}$,

$$v(x)=u(x) < u(y)=v(y)$$
  
shows that $v$ is an isomorphism from $S$ to $v(S)$. Therefore, $\mathcal{F}$ is inductive.

Now, by [§Axiom of Choice, ⁋Theorem 4](/en/math/set_theory/axiom_of_choice#thm4){: data-lid="ahhe6" }, $\mathcal{F}$ has a maximal element. Let this be $u_0$, and let its domain be $S_0$. We must show that either $S_0=A$ or $u_0(S_0)=B$.

If not, by [§Ordinals and Well-Ordered Sets, ⁋Proposition 5](/en/math/set_theory/ordinals#prop5){: data-lid="hz792" }, there exist some $a\in A$ and $b\in B$ such that $S_0=(-\infty, a)$ and $u_0(S_0)=(-\infty, b)$. Now, adjoining to $u_0$ the pair $(a,b)$ produces a new function that strictly extends $u_0$, and since this contradicts the maximality of $u_0$, either $S_0=A$ or $u_0(S_0)=B$.
:::

As mentioned earlier, since every ordinal is a well-ordered set, according to the proposition above, the way is open to viewing any well-ordered set as a segment order isomorphic to an initial segment of some ordinal. However, for this we must introduce the following new axiom.

::: misc The Axiom schema of Replacement. {#axiom-replacement}
Let $P(x,y)$ be a property satisfying

> for any $x$, for $P(x,y)$ to hold, there exists a unique $y$

Then for any set $A$, another set $B$ can be found such that

> for each $x\in A$, there exists a suitable $y\in B$ such that $P(x,y)$ holds
:::

Given $P$ satisfying the above condition, we can also think of it as taking $x$ as input and producing $y$ as output, yielding a function $F$. However, functions were originally defined in a state where a target was specified, whereas the correspondence created by this condition $P$ provides no information about the target whatsoever. This is why an axiom schema is needed rather than a single axiom. In any case, if the replacement schema is given, we can properly define the target $B$, and by applying the comprehension schema to $B$ with the condition

> $(x,y)\in F$ for some $x$

we can define the *image* of $A$ under $F$ in the same way.

::: Theorem 2
Every well-ordered set is order isomorphic to a unique ordinal.
:::
::: Proof
Let $A$ be a well-ordered set, and let $X$ be the set of elements satisfying

> $S_x$ is order isomorphic to some ordinal

among all $x\in A$. Since no ordinal is order isomorphic to any ordinal other than itself, for each element of $X$ given by $x\in A$, we can assign a unique ordinal $\alpha_x$. Our goal is to show that the set $B$ collecting all such ordinals becomes an ordinal order isomorphic to $A$, but to do so, we must first show that this set exists.

To this end, let us define the property $P(x,y)$ as follows:

> (i) $x\in X$ and $y$ is an ordinal order isomorphic to $S_x$, or
> (ii) $x\not\in X$ and $y=\emptyset$.

As mentioned above, this property specifies either a unique ordinal $y$ or the (likewise unique) empty set $\emptyset$, so we can apply the axiom schema of replacement. Applying this, for the function defined by $P$, denoted $F$, we know that the set $F(A)$ exists. Call this set $B$.

1. Since $B$ is a set of ordinals, it is well-ordered by $\in$.
2. For any $\alpha_x\in B$, if $\gamma\in\alpha_x$, then for the order isomorphism between $\alpha_x$ and $S_x$, say $\varphi$, we can consider the inverse image $\varphi^{-1}(\gamma)\in S_x$ under it. Letting this be $c$, the function obtained by restricting $\varphi$ to $S_c$ defines an order isomorphism between $S_c$ and $\gamma$, so by the definition of $B$ we have $\gamma\in B$.

From the above, we see that $B$ is an ordinal number. Moreover, applying the argument of step 2 in the same way, we can show that for any $x\in X$, if $y<x$ then $y\in X$. That is, $X$ is a segment of $A$, and thus either $X=S_x$ or $X=A$. ([§Ordinals and Well-Ordered Sets, ⁋Proposition 5](/en/math/set_theory/ordinals#prop5){: data-lid="vu5x3" })

Now, to show that $X=A$, let us negate the conclusion to obtain a contradiction. First, we can define $f:X\rightarrow B$ by $f(x)=\alpha_x$, and in this case one can verify that $f$ is an order isomorphism between $B$ and $X$. However, if $X=S_x$, then since $B$ is an ordinal, this means that $S_x$ is isomorphic to the ordinal $B$, so by definition we must have $x\in X$. This is a contradiction, so $X=A$.
:::

## Definition of Cardinal Numbers

We now introduce the rigorous definition of cardinality. However, our full treatment of cardinals will appear in the next article (which uses the non-rigorous definition), and what we do now is strictly focused on *defining the size of a set in a rigorous manner*. For example, defining operations between them will use the definition from the next article, which is not rigorous; if one wishes to define them rigorously, refer to Chapters 7 and 9 of **[HJJ]**.

The definition of cardinality that we will consider in the next article defines the size of a set using bijections between sets. For example, since a bijection exists between two-element sets, we will consider them to have the same size. In a sense, this definition does not fit well with ordinals, because, for example, $\omega$ and $\omega+1$ are clearly different sets from the ordinal perspective, yet there exists a bijection between them (ignoring order). To reconcile these, we may define as follows.

::: Definition 3
For any set $A$, the smallest ordinal number for which no bijection exists with any subset of $A$ is called the *Hartogs number* of $A$ and is denoted by $h(A)$.
:::

Since infinite successor ordinals admit a bijection with their *preceding* ordinal, they cannot be the Hartogs number of any set. Even if we examine limit ordinals, $\omega$ and $\omega\cdot 2$ must have the same size itself. For this reason, we newly define the following concept.

::: Definition 4
An ordinal $\alpha$ is called an *initial ordinal* if, for $\beta<\alpha$, for all such $\beta$, there is no bijection between $\beta$ and $\alpha$.
:::

Then the size of any set can be expressed as the size of an initial ordinal. Given a set $X$, we can equip it with a well-ordering by [§Axiom of Choice, ⁋Theorem 1](/en/math/set_theory/axiom_of_choice#thm1){: data-lid="5t6u4" } to select an ordinal $\alpha$, and then choose the smallest among all ordinals of the same size (by well-ordering).

We can define cardinal numbers using ordinal numbers. Consider collecting all infinite initial ordinals and labeling them in order as the $0, 1, \ldots$-th. That is, $\omega_0$ is the 0th initial ordinal, namely $\omega$, and thereafter we define $\omega_1,\omega_2,\ldots$ with strictly increasing set sizes. When defining cardinals, it is customary to write these (rather than using $\omega$, the letter defining ordinals) as $\aleph_\alpha$.

---
**References**

**[HJJ]** K. Hrbacek, T.J. Jeck, and T. Jech. *Introduction to Set Theory*. Lecture Notes in Pure and Applied Mathematics. M. Dekker, 1978. 

---
