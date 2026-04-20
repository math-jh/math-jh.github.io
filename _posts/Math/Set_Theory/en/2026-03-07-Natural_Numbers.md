---

title: "Natural Numbers and Infinite Sets"
excerpt: "Definition of natural numbers and properties of infinite sets"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/natural_numbers
header:
    overlay_image: /assets/images/Math/Set_Theory/Natural_numbers.png
    overlay_filter: 0.5
sidebar: 
    nav: "set_theory-en"

date: 2026-03-07
last_modified_at: 2026-03-07
weight: 26

---

## An Alternative Definition of Natural Numbers

We now construct natural numbers using the cardinals we have already defined, rather than following the approach in [§Ordinals and Well-ordered Sets](/en/math/set_theory/ordinals). We then explore the structure of natural numbers using the operations and order relations previously defined on cardinal numbers.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A cardinal $$\mathfrak{a}$$ is said to be *finite* if $$\mathfrak{a}\neq\mathfrak{a}+\mathbf{1}$$. A finite cardinal is called a *natural number*. For a set $$E$$, if the cardinal $$\card E$$ is finite, then the set is said to be finite, and in this case $$\card E$$ is called the *number of elements* of the set $$E$$.

</div>

Since natural numbers form a subset of the set of cardinals, they are well-ordered. ([§Cardinals, ⁋Theorem 5](/en/math/set_theory/cardinals#thm5)) Thus, we can use induction on natural numbers. ([§Properties of Well-ordered Sets, ⁋Lemma 7](/en/math/set_theory/well_ordering#lem7))

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> A cardinal $$\mathfrak{a}$$ is finite if and only if $$\mathfrak{a}+\mathbf{1}$$ is finite.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

By [§Operations on Cardinals, ⁋Proposition 6](/en/math/set_theory/operation_of_cardinals#prop6), $$\mathfrak{a}=\mathfrak{b}$$ is equivalent to $$\mathfrak{a}+\mathbf{1}=\mathfrak{b}+\mathbf{1}$$. Now let $$\mathfrak{b}=\mathfrak{a}+\mathbf{1}$$. By assumption, $$\mathfrak{a}\neq\mathfrak{b}$$, and therefore

$$\mathfrak{b}=\mathfrak{a}+\mathbf{1}\neq\mathfrak{b}+\mathbf{1}$$

so $$\mathfrak{a}$$ is finite if and only if $$\mathfrak{b}=\mathfrak{a}+\mathbf{1}$$ is finite.

</details>

From now on, we will write natural numbers using ordinary letters such as $$m$$ and $$n$$ instead of blackletter $$\mathfrak{a}$$, $$\mathfrak{b}$$, and we will write the cardinal numbers $$\mathbf{0}$$ and $$\mathbf{1}$$ simply as $$0$$ and $$1$$.

## Order Relations Between Natural Numbers

<div class="proposition" markdown="1">

<ins id="lem3">**Lemma 3**</ins> Let $$\mathfrak{a}$$ and $$\mathfrak{b}$$ be cardinals. Then $$\mathfrak{a}\geq\mathfrak{b}$$ if and only if there exists a cardinal $$\mathfrak{c}$$ such that $$\mathfrak{a}=\mathfrak{b}+\mathfrak{c}$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

$$\mathfrak{a}\geq\mathfrak{b}$$ is equivalent to the existence of sets $$A$$ and $$B$$ with cardinals $$\mathfrak{a}$$ and $$\mathfrak{b}$$ respectively, such that $$A\supset B$$. Now, $$A=B\cup(A\setminus B)$$.

</details>

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> Let $$n$$ be a natural number. Then every cardinal $$\mathfrak{a}$$ satisfying $$\mathfrak{a}\leq n$$ is also a natural number. If $$n\neq 0$$, then there exists a unique natural number $$m$$ such that $$n=m+1$$. In this case, the unary relation $$a<n$$ is equivalent to $$a\leq m$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

To prove the first claim, let $$\mathfrak{a}$$ be a cardinal satisfying $$\mathfrak{a}\leq n$$. Then there exists a cardinal $$\mathfrak{b}$$ such that $$n=\mathfrak{a}+\mathfrak{b}$$. Now

$$(\mathfrak{a}+1)+\mathfrak{b}=(\mathfrak{a}+\mathfrak{b})+1=n+1\neq n$$

so $$(\mathfrak{a}+1)+\mathfrak{b}\neq\mathfrak{a}+\mathfrak{b}$$. Therefore $$\mathfrak{a}+1\neq\mathfrak{a}$$, and $$\mathfrak{a}$$ is a natural number.

If $$n\neq 0$$, then $$n\geq 1$$, so by the previous lemma, there exists a cardinal $$m$$ such that $$n=m+1$$, and by the same reasoning, $$m$$ is also a natural number. Thus we only need to show that $$a<n$$ is equivalent to $$a\leq m$$.

If $$a<n$$, then there exists a unique natural number $$b$$ such that $$n=a+b$$. Since $$b\neq 0$$, we have $$b=c+1$$ for some $$c$$. Then

$$m+1=n=a+b=a+(c+1)=(a+c)+1$$

so $$m=a+c$$. Therefore $$a\leq m$$. Conversely, if $$a\leq m$$, then

$$a\leq m+1=n$$

and $$a=n=m+1>m$$ is a contradiction, so $$a\neq n$$. Thus $$a<n$$.

</details>

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> Let $$a$$ and $$b$$ be natural numbers. Then $$a<b$$ is equivalent to the existence of a natural number $$c>0$$ such that $$b=a+c$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

This is a direct consequence of [Lemma 3](#lem3). Since $$a\leq b$$, such a $$c\geq 0$$ exists, and if $$c=0$$ then $$a=b$$, so we must have $$c\neq 0$$.

</details>

Summarizing what we have done so far, we obtain the following:

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> Let $$a$$ and $$b$$ be natural numbers. Then the function $$x\mapsto a+x$$ is a strictly increasing order isomorphism from the interval $$[0,b]$$ to $$[a,a+b]$$.

</div>

Therefore, any interval $$[a,b]$$ can be treated as a set with $$b-a+1$$ elements. A function with a finite domain is called a *finite sequence*. Since every finite set can be identified with $$[1,n]$$ by the theorem above, we can always regard finite sequences as functions defined on natural numbers from $$1$$ to $$n$$.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> Let $$(a_i)_{i\in I}$$ be a finite sequence taking values in natural numbers. Then both $$\sum a_i$$ and $$\prod a_i$$ are natural numbers.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Since $$I$$ is finite, it suffices to show that for any natural numbers $$a$$ and $$b$$, both $$a+b$$ and $$ab$$ are natural numbers. This can be shown by induction on $$b$$. First, $$a+0=a$$ is a natural number, and if $$a+k$$ is a natural number, then $$a+(k+1)=(a+k)+1$$ is also a natural number, which is straightforward to show. The case for multiplication is similar.

</details>

## Properties of the Set of Natural Numbers

<div class="definition" markdown="1">

<ins id="def8">**Definition 8**</ins> Let $$A$$ be a non-empty set and $$X$$ be a subset of $$A$$. The *characteristic function* of $$X$$ is the function $$\chi_X:E\rightarrow \{0,1\}$$ defined by the following formula:

$$\chi_X(x)=\begin{cases}1&\text{if $x\in X$}\\ 0&\text{if $x\in A\setminus X$}\end{cases}$$

</div>

The following theorem is obvious.

<div class="proposition" markdown="1">

<ins id="prop9">**Proposition 9**</ins> For two subsets $$X$$ and $$Y$$ of a set $$A$$, the following identities hold:

$$\begin{aligned}
\chi_{A\setminus X}(x)&=1-\chi_X(x)\\
\chi_{X\cap Y}(x)&=\chi_X(x)\chi_Y(x)\\
\chi_{X\cup Y}(x)+\chi_{X\cap Y}(x)&=\chi_X(x)+\chi_Y(x)
\end{aligned}$$

</div>


Let us now establish some properties of natural numbers that will be useful in contexts beyond set theory. First, we present the division algorithm, also known as the Euclidean algorithm.

<div class="proposition" markdown="1">

<ins id="thm10">**Theorem 10**</ins>  Let $$a$$ and $$b$$ be natural numbers with $$b>0$$. Then there exist unique natural numbers $$q$$ and $$r$$ such that $$a=bq+r$$ and $$r< b$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

If such a pair exists, then $$q$$ must be the smallest natural number satisfying $$a<b(q+1)$$. Otherwise,

$$r=a-bq<0\quad\text{or}\quad r=a-bq\geq b$$

To establish existence, let $$a<a+1<b(a+1)$$. Then the set of $$p$$ satisfying $$a<bp$$ is non-empty. By well-orderedness, there exists a least element $$m$$, and setting $$m=q+1$$, we obtain $$q$$ satisfying the given condition.

</details>

As demonstrated in the proof above, we can define concepts such as remainders, multiples, and divisors by properly using the operations on natural numbers that we have defined. The following corollary can also be easily proved in a similar manner, but since we have not yet defined integers, we will not provide the proof here.

<div class="proposition" markdown="1">

<ins id="cor11">**Corollary 11 (Bézout's lemma)**</ins> Let any two integers $$a$$ and $$b$$ have a greatest common divisor $$d$$. Then there exist integers $$x$$ and $$y$$ such that $$ax+by=d$$.

</div>

## Definition and Properties of Infinite Sets

<div class="definition" markdown="1">

<ins id="def11">**Definition 11**</ins> A set is *infinite* if it is not finite.

</div>

Let us now examine the properties of infinite cardinals. Earlier, we saw that a finite cardinal satisfies $$\mathfrak{a}\neq\mathfrak{a}+1$$. The following theorem presents a similar property that characterizes infinite cardinals.

<div class="proposition" markdown="1">

<ins id="prop12">**Proposition 12**</ins> For every infinite cardinal $$\mathfrak{a}$$, we have $$\mathfrak{a}^2=\mathfrak{a}$$.

</div>

To prove this, we first need to establish the following lemmas.

<div class="proposition" markdown="1">

<ins id="lem13">**Lemma 13**</ins> Every infinite set $$A$$ contains a subset that is equipotent to $$\mathbb{N}$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

There exists a well-ordering of $$A$$. Since every proper segment of $$\mathbb{N}$$ is finite, $$A$$ cannot be isomorphic to a segment of $$\mathbb{N}$$. Therefore, $$\mathbb{N}$$ is isomorphic to a segment of $$A$$. ([§Order Relations Between Ordinals, ⁋Proposition 1](/en/math/set_theory/order_relations_between_ordinals#prop1))

</details>
<div class="proposition" markdown="1">

<ins id="lem14">**Lemma 14**</ins> The set $$\mathbb{N}\times\mathbb{N}$$ is equipotent to $$\mathbb{N}$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

This follows from the following sequence:

$$(1,1),\;\; (1,2),(2,1),\;\; (1,3),(2,2),(3,1),\;\; \cdots$$

</details>

<details class="proof--alone" markdown="1">
<summary>Proof of Proposition 12</summary>

Let $$A$$ be a set with cardinal $$\mathfrak{a}$$. By the first lemma, there exists $$B\subseteq A$$ that is equipotent to $$\mathbb{N}$$, and thus by the second lemma, there exists a bijection between $$B\times B$$ and $$B$$. Let us call this bijection $$f$$.

Let $$\mathfrak{M}$$ be the collection of pairs $$(X,\psi)$$ where $$X$$ is a subset of $$A$$ containing $$B$$, and $$\psi:X\rightarrow X\times X$$ is an extension of $$f$$. For any chain in $$\mathfrak{M}$$, the pair with the largest domain serves as a maximal element, so $$\mathfrak{M}$$ is an inductive set. Therefore, by Zorn's lemma, there exists a maximal element $$(F, \tilde{f})$$ in $$\mathfrak{M}$$.

It now suffices to show that $$\card F=\mathfrak{a}$$. If $$\card F=\mathfrak{b}<\mathfrak{a}$$, then by the bijection $$\tilde{f}$$, we have $$\mathfrak{b}=\mathfrak{b}^2$$, so

$$\mathfrak{b}\leq 2\mathfrak{b}\leq 3\mathfrak{b}\leq \mathfrak{b}^2=\mathfrak{b}$$

and thus $$\mathfrak{b}=2\mathfrak{b}=3\mathfrak{b}$$. From $$\mathfrak{b}<\mathfrak{a}$$, we have $$\card(A\setminus F)>\mathfrak{b}$$. Otherwise,

$$\mathfrak{a}=\card A=\card(F\cup(A\setminus F))\leq\card F+\card(A\setminus F)\leq\mathfrak{b}+\mathfrak{b}=2\mathfrak{b}=\mathfrak{b}$$

which is a contradiction. Therefore, there exists $$Y\subseteq A\setminus F$$ such that $$\card Y=\mathfrak{b}$$. Let $$Z=F\cup Y$$. Then

$$Z\times Z=(F\times F)\cup(F\times Y)\cup(Y\times F)\cup (Y\times Y)$$

and the four sets on the right-hand side are pairwise disjoint. Since $$F$$ and $$Y$$ are equipotent,

$$\card(F\times Y)=\card(Y\times F)=\card(F\times F)=\mathfrak{b}^2=\mathfrak{b}$$

and therefore

$$\card((F\times Y)\cup(Y\times F)\cup(Y\times Y))=3\mathfrak{b}=\mathfrak{b}=\card Y$$

Thus there exists a bijection from $$Y$$ to the union of these sets, and consequently, there exists a bijection from $$Z=F\cup Y$$ to $$Z\times Z$$. This is because on $$F$$, we can use $$\tilde{f}:F\rightarrow F\times F$$, and on $$Y$$, we can use the bijection we just constructed. This contradicts the maximality of $$F$$, so we must have $$\card F=\mathfrak{a}$$.

</details>

Using this result, the following can be easily established.

<div class="proposition" markdown="1">

<ins id="cor15">**Corollary 15**</ins> If $$\mathfrak{a}$$ is an infinite cardinal, then $$\mathfrak{a}^n=\mathfrak{a}$$ for all $$n\geq 1$$. For a finite family of non-zero cardinals $$(\mathfrak{a}_i)_{i\in I}$$, if the largest cardinal among them is an infinite cardinal $$\mathfrak{a}$$, then both their product and sum equal $$\mathfrak{a}$$.

</div>

Among infinite sets, those that are equipotent to $$\mathbb{N}$$ are specially called *countable*.


---
**References**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
