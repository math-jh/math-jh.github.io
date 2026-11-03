---
title: "Natural Numbers and Infinite Sets"
description: "We define finite cardinals as natural numbers through the concept of cardinality, examine the well-ordered property of the set of natural numbers and the foundation of induction, and analyze the order relation between natural numbers."
excerpt: "Definition of natural numbers and properties of infinite sets"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/natural_numbers
sidebar: 
    nav: "set_theory-en"

date: 2021-09-04
weight: 25
translated_at: 2026-06-02T17:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-11-03T11:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
## An Alternative Definition of Natural Numbers

Now, instead of the method of [§Ordinals and Well-Ordered Sets](/en/math/set_theory/ordinals){: data-lid="wvue3" }, we construct the natural numbers using the cardinals we have already defined, and explore the structure of the natural numbers using the operations and order relations defined on cardinal numbers.

::: Definition 1
A cardinal $\mathfrak{a}$ is said to be *finite* if $\mathfrak{a}\neq\mathfrak{a}+\mathbf{1}$. A finite cardinal is called a *natural number*. For a set $E$, if the cardinal $\card E$ is finite, this set is called finite, and in this case $\card E$ is called the *number of elements* of the set $E$.
:::

Since natural numbers form a subset of the set of cardinals, they are well-ordered. ([§Cardinals, ⁋Theorem 5](/en/math/set_theory/cardinals#thm5){: data-lid="yfzlc" }) Thus, we can use induction on natural numbers. ([§Properties of Well-Ordered Sets, ⁋Lemma 7](/en/math/set_theory/well_ordering#lem7){: data-lid="01vqd" })

::: Proposition 2
A cardinal $\mathfrak{a}$ is finite if and only if $\mathfrak{a}+\mathbf{1}$ is finite.
:::

::: Proof
By [§Operations on Cardinals, ⁋Proposition 6](/en/math/set_theory/operation_of_cardinals#prop6){: data-lid="1bf64" }, $\mathfrak{a}=\mathfrak{b}$ is equivalent to $\mathfrak{a}+\mathbf{1}=\mathfrak{b}+\mathbf{1}$. Now let $\mathfrak{b}=\mathfrak{a}+\mathbf{1}$. By assumption, $\mathfrak{a}\neq\mathfrak{b}$, and therefore

$$\mathfrak{b}=\mathfrak{a}+\mathbf{1}\neq\mathfrak{b}+\mathbf{1}$$

so $\mathfrak{a}$ is finite if and only if $\mathfrak{b}=\mathfrak{a}+\mathbf{1}$ is finite.
:::

From now on, instead of the blackletter $\mathfrak{a}$, $\mathfrak{b}$, we will write natural numbers using ordinary letters such as $m$, $n$, etc., and write the cardinal numbers $\mathbf{0}$ and $\mathbf{1}$ simply as $0$ and $1$. Also, the set of all natural numbers is denoted by $\mathbb{N}$.

## Order Relations Between Natural Numbers

::: Lemma 3
Let $\mathfrak{a}$ and $\mathfrak{b}$ be cardinals. Then $\mathfrak{a}\geq\mathfrak{b}$ if and only if there exists a cardinal $\mathfrak{c}$ such that $\mathfrak{a}=\mathfrak{b}+\mathfrak{c}$.
:::
::: Proof
$\mathfrak{a}\geq\mathfrak{b}$ is equivalent to the condition that for the cardinals $\mathfrak{a}$ and $\mathfrak{b}$, there exist sets $A$ and $B$ respectively such that $A\supset B$. Now $A=B\cup(A\setminus B)$.
:::

::: Proposition 4
Let $n$ be a natural number. Then, for every cardinal satisfying $\mathfrak{a}\leq n$, $\mathfrak{a}$ is also a natural number. If $n\neq 0$, then there exists a unique natural number $m$ such that $n=m+1$. In this case, the unary relation in $a$, $a<n$, is equivalent to $a\leq m$.
:::
::: Proof
To prove the first claim, let $\mathfrak{a}$ be a cardinal satisfying $\mathfrak{a}\leq n$. Then there exists a cardinal $\mathfrak{b}$ such that $n=\mathfrak{a}+\mathfrak{b}$. Now

$$(\mathfrak{a}+1)+\mathfrak{b}=(\mathfrak{a}+\mathfrak{b})+1=n+1\neq n$$

so $(\mathfrak{a}+1)+\mathfrak{b}\neq\mathfrak{a}+\mathfrak{b}$. Therefore $\mathfrak{a}+1\neq\mathfrak{a}$, so $\mathfrak{a}$ is a natural number.

If $n\neq 0$, then $n\geq 1$, so by the previous lemma we have $n=m+1$ for some cardinal $m$, and by the preceding reasoning, $m$ is also a natural number. Thus it suffices to show that $a<n$ is equivalent to $a\leq m$.

First, if $a<n$, there exists a unique natural number $b$ such that $n=a+b$. Since $b\neq 0$, for some $c$ we have $b=c+1$. Then

$$m+1=n=a+b=a+(c+1)=(a+c)+1$$

so $m=a+c$. Therefore $a\leq m$. Conversely, if $a\leq m$, then

$$a\leq m+1=n$$

and since $a=n=m+1>m$ is a contradiction, $a\neq n$. Therefore $a<n$.
:::

::: Proposition 5
Let $a$ and $b$ be natural numbers. Then $a<b$ is equivalent to the existence of a natural number $c>0$ such that $b=a+c$.
:::
::: Proof
This is a direct consequence of [Lemma 3](#lem3){: data-lid="rldhh" }. Since $a\leq b$, such a $c\geq 0$ exists, and if $c=0$, then $a=b$, so $c\neq 0$.
:::

Summarizing what we have done so far, we obtain the following.

::: Proposition 6
Let $a$ and $b$ be natural numbers. Then the function $x\mapsto a+x$ is a strictly increasing order isomorphism from the interval $[0,b]$ to $[a,a+b]$.
:::

Therefore, any interval $[a,b]$ can be treated in the same way as a set with $b-a+1$ elements. A function with a finite domain is called a *finite sequence*; since every finite set can be identified with $[1,n]$ by the theorem above, we can always treat a finite sequence as being defined on the natural numbers from $1$ to $n$.

::: Proposition 7
Let $(a_i)_{i\in I}$ be a finite sequence taking values in the natural numbers. Then both $\sum a_i$ and $\prod a_i$ are natural numbers.
:::
::: Proof
Since $I$ is finite, it suffices to show that for any natural numbers $a$ and $b$, both $a+b$ and $ab$ are natural numbers. This can be shown by induction on $b$. First, $a+0=a$ is a natural number, and if $a+k$ is a natural number, then $a+(k+1)=(a+k)+1$ is also a natural number, so this is easily shown. The same applies to multiplication.
:::

## Properties of the Set of Natural Numbers

::: Definition 8
Let $A$ be a non-empty set and $X$ be a subset of $A$. The *characteristic function* of $X$ is the function $\chi_X:A\rightarrow \{0,1\}$, and its values are given by the formula

$$\chi_X(x)=\begin{cases}1&\text{if $x\in X$}\\ 0&\text{if $x\in A\setminus X$}\end{cases}$$

.
:::

The following theorem is obvious.

::: Proposition 9
For a set $A$ and two of its subsets $X$ and $Y$,

$$\begin{aligned}
\chi_{A\setminus X}(x)&=1-\chi_X(x)\\
\chi_{X\cap Y}(x)&=\chi_X(x)\chi_Y(x)\\
\chi_{X\cup Y}(x)+\chi_{X\cap Y}(x)&=\chi_X(x)+\chi_Y(x)
\end{aligned}$$

hold.
:::

Now, before moving on, let us summarize some properties of the natural numbers that will be used in various other places rather than set theory. First, the following is the division algorithm called Euclidean division.

::: Theorem 10
Let $a$ and $b$ be natural numbers satisfying $b>0$. Then there exist unique natural numbers $q$ and $r$ such that $a=bq+r$ and $r< b$.
:::

::: Proof
If such a pair exists, $q$ must be the smallest natural number satisfying $a<b(q+1)$, because otherwise we would have

$$r=a-bq<0\quad\text{or}\quad r=a-bq\geq b$$

. To show existence, let $a<a+1\leq b(a+1)$. Then the set satisfying $a<bp$ for $p$ is non-empty. Now, by well-orderedness, there exists a least element $m$, so setting $m=q+1$, $q$ satisfies the given conditions.
:::

As in the proof above, by properly using the operations on natural numbers we have defined, one can define concepts such as remainders, multiples, and divisors. The following corollary can also be easily proved in a similar manner, but since we have not yet defined integers, we do not give a proof here.

::: Corollary 11 (Bézout's lemma)
Suppose any two integers $a$, $b$ have a greatest common divisor $d$. Then there exist two integers $x$ and $y$ such that $ax+by=d$.
:::

## Definition and Properties of Infinite Sets

::: Definition 12
A set is *infinite* if it is not finite.
:::

Let us now examine the properties of infinite cardinals. Earlier, a finite cardinal satisfied $\mathfrak{a}\neq\mathfrak{a}+1$. The following theorem is a similar property of infinite cardinals.

::: Proposition 13
For every infinite cardinal $\mathfrak{a}$, $\mathfrak{a}^2=\mathfrak{a}$ holds.
:::

To show this, we must first prove the following lemmas.

::: Lemma 14
Every infinite set $A$ contains a subset equipotent to $\mathbb{N}$.
:::
::: Proof
There exists a well-ordering of $A$. Since every segment of $\mathbb{N}$ other than itself is always finite, $A$ cannot be isomorphic to a segment of $\mathbb{N}$. Therefore, $\mathbb{N}$ is isomorphic to a segment of $A$. ([§Order Relations Between Ordinals, ⁋Proposition 1](/en/math/set_theory/order_relations_between_ordinals#prop1){: data-lid="y55gn" })
:::
::: Lemma 15
The set $\mathbb{N}\times\mathbb{N}$ is equipotent to $\mathbb{N}$.
:::

::: Proof
From the following sequence,

$$(1,1),\quad (1,2),(2,1),\quad (1,3),(2,2),(3,1),\quad \cdots$$

this is clear.
:::

::: Proof (Proposition 13)
Let $A$ be a set with cardinal $\mathfrak{a}$. Then, by the first lemma, some $B\subseteq A$ is equipotent to $\mathbb{N}$, and thus by the second lemma, there exists a bijection between $B\times B$ and $B$. Let this be $f$. 

For a subset containing $B$ within $A$, $X$, and an extension of $f$ defined on it, $\psi:X\rightarrow X\times X$, let $\mathfrak{M}$ be the collection of such pairs $(X,\psi)$. Then, for any chain in $\mathfrak{M}$, the pair with the largest domain is a maximal element, so $\mathfrak{M}$ is an inductive set; therefore, by Zorn's lemma, $\mathfrak{M}$ has a maximal element $(F, \tilde{f})$.

It now suffices to show that $\card F=\mathfrak{a}$. If $\card F=\mathfrak{b}<\mathfrak{a}$, then by the bijection $\tilde{f}$, we have $\mathfrak{b}=\mathfrak{b}^2$, so 

$$\mathfrak{b}\leq 2\mathfrak{b}\leq 3\mathfrak{b}\leq \mathfrak{b}^2=\mathfrak{b}$$

we have $\mathfrak{b}=2\mathfrak{b}=3\mathfrak{b}$. Then, from $\mathfrak{b}<\mathfrak{a}$, we have $\card(A\setminus F)>\mathfrak{b}$. Otherwise,

$$\mathfrak{a}=\card A=\card(F\cup(A\setminus F))\leq\card F+\card(A\setminus F)\leq\mathfrak{b}+\mathfrak{b}=2\mathfrak{b}=\mathfrak{b}$$

which is a contradiction. Therefore, there exists $Y\subseteq A\setminus F$ such that $\card Y=\mathfrak{b}$. Let $Z=F\cup Y$. Then

$$Z\times Z=(F\times F)\cup(F\times Y)\cup(Y\times F)\cup (Y\times Y)$$

and the four terms on the right-hand side are pairwise disjoint sets. Since $F$ and $Y$ are equipotent, 

$$\card(F\times Y)=\card(Y\times F)=\card(F\times F)=\mathfrak{b}^2=\mathfrak{b}$$

and therefore

$$\card((F\times Y)\cup(Y\times F)\cup(Y\times Y))=3\mathfrak{b}=\mathfrak{b}=\card Y$$

Therefore, there exists a bijection from $Y$ to the union of these sets, and thus there exists a bijection from $Z=F\cup Y$ to $Z\times Z$. This is because on $F$, one can use $\tilde{f}:F\rightarrow F\times F$, and on $Y$, one can use the bijection just constructed. This contradicts the maximality of $F$, so we must have $\card F=\mathfrak{a}$.
:::

Using this, the following can be easily shown.

::: Corollary 16
If $\mathfrak{a}$ is an infinite cardinal, then for any $n\geq 1$, we have $\mathfrak{a}^n=\mathfrak{a}$. For a finite family $(\mathfrak{a}_i)_{i\in I}$ of non-zero cardinals, if the largest cardinal among them is an infinite cardinal $\mathfrak{a}$, then both their product and sum are $\mathfrak{a}$.
:::

Among infinite sets, we specifically call those equipotent to $\mathbb{N}$ *countable*.


---
**References**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
