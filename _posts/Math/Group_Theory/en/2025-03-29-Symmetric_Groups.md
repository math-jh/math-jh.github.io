---
title: "Symmetric Groups"
description: "We examine the definition of the symmetric group on a set, cycle notation, the computation of cycle compositions, and the concept of disjoint cycles."
excerpt: "Cycle decomposition and sign of the symmetric group, and the alternating group"

categories: [Math / Group Theory]
permalink: /en/math/group_theory/symmetric_groups
sidebar: 
    nav: "group_theory-en"

date: 2025-03-29
weight: 1
translated_at: 2026-05-31T10:00:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-10T07:15:05+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
In the [Algebraic Structures](/en/algebraic_structures) category we were interested in the common properties shared by various algebraic structures; while this approach is good for surveying how algebraic theories develop from an overall perspective, it is not well suited for examining details such as computing a specific group. Therefore, in the posts in this category we examine properties of groups not covered in the [Algebraic Structures](/en/algebraic_structures) category. 

## Symmetric Groups

The first objects we examine in the [Group Theory](/en/group_theory) category are specific groups. 

::: Definition 1
For the set $[n]=\{1,\ldots, n\}$, the automorphism group of $[n]$ in $\Set$, $\Aut([n])$, is called the *symmetric group* and written $S_n$. ([\[Category Theory\] §Category, ⁋Definition 9](/en/math/category_theory/categories#def9){: data-lid="394kx" })  
:::

That is, the elements of $S_n$ are bijections from the set $[n]$ to $[n]$, and the operation of $S_n$ is given by composition of functions. The elements of $S_n$ are called *permutations*.

Suppose given a permutation $\sigma: [n] \rightarrow [n]$, and consider, in the set $[n]$, the $n+1$ elements

$$1=\sigma^0(1), \quad\sigma(1)=\sigma^1(1),\quad\sigma^2(1),\quad\cdots, \quad\sigma^n(1)\tag{$\ast$}$$

By the pigeonhole principle there exist two distinct integers $0\leq k_1,k_2\leq n$ such that $\sigma^{k_1}(1)=\sigma^{k_2}(1)$, and assuming $k_1< k_2$ for convenience, we know from this that $\sigma^{k_2-k_1}(1)=1$. Furthermore, if we let the smallest positive integer satisfying $\sigma^k(1)=1$ be $k$, from the above result we have $k\leq n$, and based on this we can consider the notation

$$(1\quad \sigma(1)\quad \sigma^2(1)\quad\cdots\quad\sigma^{k-1}(1))$$

By definition this notation means the function sending $1$ to $\sigma(1)$, $\sigma(1)$ to $\sigma^2(1)$, $\ldots$, $\sigma^{k-2}(1)$ to $\sigma^{k-1}(1)$, and $\sigma^{k-1}(1)$ to $\sigma^k(1)=1$; and more generally

$$(a_1\quad a_2\quad\cdots\quad a_{k})$$

means the function sending $a_1$ to $a_2$, $\ldots$, $a_{k-1}$ to $a_{k}$, and $a_k$ to $a_1$ while leaving the remaining elements unchanged, which is called a *cycle* of length $k$. Then for two cycles $\sigma$, $\tau$, $\sigma\tau$ means the composition of the functions $\sigma$ and $\tau$, $\sigma\circ\tau$. 

::: Example 2
For example, consider in $S_3$ the element $\sigma=(1\quad 2\quad 3)$. This function sends $1$ to $2$, $2$ to $3$, and $3$ to $1$. Meanwhile, consider the following composition

$$\tau_1\tau_2=(2\quad 3)(1\quad 3)$$

Then first, under $\tau_2$, $1$ is moved to $3$, $2$ to $2$, and $3$ to $1$. Afterwards, under $\tau_1$, what was originally $1$, namely $3$, is moved to $2$, and $2$ is moved to $3$, so $\tau_1\tau_2$ sends $1$ to $2$, $2$ to $3$, and $3$ to $1$. That is, as functions, $\sigma=\tau_1\tau_2$. On the other hand, considering the composition

$$\tau_2\tau_1=(1\quad 3)(2\quad 3)$$

we see that $1$ is moved to $3$, $2$ to $1$, and $3$ to $2$. That is, $\tau_1\tau_2\neq\tau_2\tau_1$. 
:::

The composition of elements of $S_n$ is composition of functions, and since composition of functions generally does not satisfy commutativity, the above example is what was expected. However, in special cases, certain two functions may commute. 

::: Definition 3
Permutations $\sigma_1,\ldots,\sigma_r\in S_n$ are *disjoint* if whenever some $i$ satisfies $\sigma_i(k)\neq k$, then for all other $j\neq i$ we have $\sigma_j(k)=k$. 
:::

Then, if for some $k$ we have $\sigma_i(k)\neq k$, since $\sigma_i$ is injective we have $\sigma_i(\sigma_i(k))\neq \sigma_i(k)$, and thus by [Definition 3](#def3){: data-lid="1sjh6" }, other than $i$, for all $j$, $\sigma_j$ fixes both $k$ and $\sigma_i(k)$; hence the product of any disjoint permutations $\sigma_1,\ldots,\sigma_r\in S_n$ does not depend on their order. Moreover, the following holds.

::: Proposition 4
Any non-identity permutation of $S_n$ can be written as a product of disjoint cycles.
:::
::: Proof
On the set $[n]$, define an equivalence relation $\sim$ by

$$i\sim j\iff \sigma^m(i)=j\text{ for some $m$}$$

and let its quotient set be

$$[n]/{\sim}=\{C_1, \ldots, C_r\}$$

Now, for each $1\leq k\leq r$, if we define by the following formula

$$\sigma_k(x)=\begin{cases}\sigma(x)&\text{if $x\in C_k$}\\x&\text{otherwise}\end{cases}$$

then these are disjoint cycles and their product is $\sigma$.
:::

If we represent an arbitrary permutation as a product of disjoint cycles in this way, one of the advantages is that the order of the permutation $\sigma$ is easily seen. That is, if we write $\sigma=\sigma_1\cdots\sigma_r$, then the order of $\sigma$ equals the least common multiple of the orders of $\sigma_1,\ldots, \sigma_r$, and the orders of the cycles $\sigma_1,\ldots, \sigma_r$ are, of course, equal to their respective lengths.

Meanwhile, let us call a cycle of length $2$ a *transposition*. This is simply a function that swaps only the two numbers appearing in this cycle. Then by the above proposition, the following holds.

::: Corollary 5
Any permutation of $S_n$ can be written as a product of transpositions.
:::
::: Proof
By [Proposition 4](#prop4){: data-lid="rifbr" }, it suffices to prove that an arbitrary cycle can be written as a product of transpositions.

$$(k_1\quad k_2\quad \cdots\quad k_r)=(k_{r-1}\quad k_r)(k_{r-2}\quad k_r)\cdots(k_2\quad k_r)(k_1\quad k_r).$$
:::

Meanwhile, to represent all elements of $S_n$, just two elements suffice.

::: Proposition 6
Every element of $S_n$ can be written as a product of $(1\quad 2)$ and $(1\quad 2\quad \cdots\quad n)$.
:::

To prove this, let us first examine the following.

::: Lemma 7
Let $\sigma\in S_n$. Then $\sigma(1\quad 2)\sigma^{-1}=(\sigma(1)\quad \sigma(2))$ holds.
:::

Of course, $1$ and $2$ may be replaced by any other numbers.

::: Proof (Lemma 7)
First, for any $i\geq 3$, consider the value of $\sigma(1\quad 2)\sigma^{-1}(\sigma(i))$. Then $\sigma(i)$ is first mapped to $\sigma^{-1}(\sigma(i))=i$. Since $i\geq 3$, this value is unchanged by $(1\quad 2)$ and by the subsequent $\sigma$ returns to $\sigma(i)$. That is, for $i\geq 3$, all $\sigma(i)$ are invariant under this transformation, so we only need to examine the values of $\sigma(1)$ and $\sigma(2)$.

First, $\sigma(1)$ is mapped via $\sigma^{-1}$ to $1$. Then, in $(1\quad 2)$ this value becomes $2$ and finally in $\sigma$ it becomes $\sigma(2)$, so as a result $\sigma(1)$ is mapped to $\sigma(2)$. Similarly, one can show that $\sigma(2)$ is mapped to $\sigma(1)$.

Therefore, $\sigma(1\quad 2)\sigma^{-1}=(\sigma(1)\quad \sigma(2))$ holds.
:::

Substituting $\sigma=(1\quad 2\quad \cdots\quad n)$, $(1\quad 2\quad \cdots\quad n)^2$, $\ldots$ into [Lemma 7](#lem7){: data-lid="iq4mh" }, we obtain $(2\quad 3)$, $(3\quad 4)$, $\ldots$. On the other hand, for any $(a\quad b)$, assuming without loss of generality that $a<b$,

$$\begin{aligned}
    (a\quad b)&=(a\quad a+1)(a+1\quad b)(a\quad a+1)\\
    &=(a\quad a+1)(a+1\quad a+2)(a+2\quad b)(a+1\quad a+2)(a\quad a+1)\\
    &=\cdots\\
    &=(a\quad a+1)(a+1\quad a+2)\cdots(b-1\quad b)\cdots(a+1\quad a+2)(a\quad a+1)
\end{aligned}$$

as above, $(a\quad b)$ can be written as a product of cycles of the form $(i\quad i+1)$. Therefore, using $(1\quad 2)$ and $(1\quad 2\quad \cdots\quad n)$, we can generate any $(a\quad b)$. However, since for any cycle $(a_1\quad a_2\quad \cdots\quad a_k)$ the formula

$$(a_1\quad a_2\quad \cdots\quad a_k)=(a_1\quad a_2)(a_2\quad a_3)\cdots(a_{k-1}\quad a_k)$$

holds, $(1\quad 2)$ and $(1\quad 2\quad \cdots\quad n)$ can generate all cycles, and hence any element of $S_n$, so [Proposition 6](#prop6){: data-lid="w83dx" } holds.

::: Theorem 8 (Cayley)
For any finite group $G$, there exists a natural number $n$ such that $G$ can be made isomorphic to some subgroup of $S_n$.
:::
::: Proof
In other words, it suffices to find an $\iota:G\rightarrow S_n$ that is a suitable inclusion homomorphism $\iota$. For the group $G$, for each element $g$, define the following *left translation map*

$$L_g: G\rightarrow G,\qquad x\mapsto gx$$

Then by the cancellation law, $L_g$ is injective. Meanwhile, for any $x\in G$, since

$$x=g(g^{-1}x)=L_g(g^{-1}x)$$

$L_g$ is also surjective. That is, $L_g$ is a bijection on the set $G$. Let $\lvert G\rvert=n$. Then the $L_g$ may all be viewed as elements of $S_n$. Now, if we define $T:G\rightarrow S_n$ by the formula

$$T(g)=L_g$$ 

then for any $x\in G$,

$$T(gh)(x)=L_{gh}(x)=(gh)x=g(hx)=L_g(L_h(x))=\big(T(g)\circ T(h)\big)(x)$$

holds. That is, $T$ is a group homomorphism. Also, if $L_g=L_h$, substituting $x=e$ gives $g=h$, so $T$ is injective, and thus we obtain the desired result.  
:::

## Alternating Groups

::: Definition 9
For $S_n$, for each element $\sigma$, if $i<j$ but $\sigma(i)>\sigma(j)$, the pairs $(i,j)$ are called *inversions*. If the number of inversions is odd, $\sigma$ is called an *odd permutation*, and if the number of inversions is even, $\sigma$ is called an *even permutation*.
:::

For example, the identity permutation is an even permutation because the number of inversions is 0, and $(1\quad 2)$ is an odd permutation because $(1,2)$ is the only pair satisfying the condition. Many algebra books, including Dummit and Hungerford, define an even permutation instead as

> a permutation that can be expressed as a product of an even number of transpositions

The strength of this definition compared to our definition just now is that properties such as the product of an even permutation and an even permutation being even and the product of an odd permutation and an even permutation being odd appear more intuitive. However, unlike our definition just now, it is not obvious that the parity (i.e., whether $\sigma$ is even or odd) is well-defined. Therefore, it is convenient to carry both definitions. These books therefore show through the following lemma that this definition is equivalent to [Definition 9](#def9){: data-lid="uzrn8" } we just defined.

::: Lemma 10
That $\sigma$ is an even permutation is equivalent to $\sigma$ being expressible as a product of an even number of transpositions.
:::
::: Proof
For $n$ variables $x_1,\ldots, x_n$, let us define the *Vandermonde polynomial* $\Delta$ by the formula

$$\Delta=\prod_{1\leq i< j\leq n}(x_i-x_j)$$

One can easily observe that $\Delta$ is a polynomial consisting only of the product, for all $i< j$, over each pair $(i,j)$, of the corresponding term $(x_i-x_j)$. Now apply precomposition to $\Delta$ to form $\sigma(\Delta)$. That is,

$$\sigma(\Delta)=\prod_{1\leq i< j\leq n}(x_{\sigma(i)}-x_{\sigma(j)})$$

Then for each pair $(i,j)$, the term $(x_{\sigma(i)}-x_{\sigma(j)})$ can be rewritten according to the order relation between $\sigma(i)$ and $\sigma(j)$ as

$$(x_{\sigma(i)}-x_{\sigma(j)})=\begin{cases}(x_{\sigma(i)}-x_{\sigma(j)})&\text{if $\sigma(i)<\sigma(j)$}\\-(x_{\sigma(j)}-x_{\sigma(i)})&\text{if $\sigma(i)>\sigma(j)$}\end{cases}\tag{1}$$

Moreover, since $\sigma$ is a bijection, if we rewrite all terms in this way we see that $\sigma(\Delta)$ is exactly the same polynomial as $\Delta$ up to sign. Therefore, if we define $\sgn(\sigma)=\sigma(\Delta)/\Delta$, then $\sgn(\sigma)$ becomes exactly the parity of $\sigma$ defined in the sense of [Definition 9](#def9){: data-lid="x677c" }.

From [Definition 9](#def9){: data-lid="1lor1" }, if $\sigma$ is a transposition that, for $a<b$, interchanges two numbers $a$ and $b$, its inversions consist of: with $a<j<b$, the pairs $(a,j)$ numbering $b-a-1$; with $a<i<b$, the pairs $(i,b)$ numbering $b-a-1$; and one $(a,b)$, totaling $2(b-a)-1$, so $\sgn(\sigma)=-1$. Therefore, if we only show that $\sgn$ is multiplicative, then

$$\text{$\sigma$ odd}\iff\text{$\sgn(\sigma)=-1$}\iff\text{$\sigma$ is a product of odd number of transpositions}$$

holds, so we will obtain the desired result. Let two permutations $\sigma$ and $\tau$ be given. We must compute the value of $\sgn(\sigma\tau)$. Suppose that $\tau$ has $k$ inversions. That is, $\sgn(\tau)=(-1)^k$, and these $k$ factors of $-1$ all come from equation (1). Now, to compute the value of $\sgn(\sigma\tau)$, we first

$$\prod_{1\leq i< j\leq n}(x_{\tau(i)}-x_{\tau(j)})=(-1)^k\Delta$$

multiply both sides by $(-1)^k$ to restore each term on the left-hand side to its original form (that is, in this situation the left-hand side is $\Delta$ with only the order of multiplication changed), and then apply $\sigma$ to this restored polynomial. Therefore, if the number of inversions of $\sigma$ was $l$, the factor attached in front of $\Delta$ would be $(-1)^{k+l}$, and this guarantees the multiplicativity of $\sgn$.
:::

If we examine this proof carefully, the $\sgn$ we constructed is in fact not just a map, but a group homomorphism from $S_n$ to $\{\pm 1\}$. Then $\ker(\sgn)$ is a normal subgroup of $S_n$.

::: Definition 11
We call the kernel of the group homomorphism $\sgn$ defined above the *alternating group* of degree $n$, and denote it by $A_n$. In other words, $A_n$ is the set of all even permutations.
:::

Meanwhile, we define the following.

::: Definition 12
A group $G$ is called *simple* if $G$ has no normal subgroups other than $\{e\}$ and itself.
:::

One notable fact is that $A_5$ is simple.

::: Example 13
$A_5$ is simple. This can be shown in a slightly more elegant way using the Sylow theorem, but $A_5$ is not such a large group, so with a little effort we can show this using only our current knowledge.

First, the permutations in $A_5$ can be classified into the following types:

- 1 identity element
- 3-cycles (of the form $(123)=(2\quad 3)(1\quad 3)$): $20=\binom{5}{3}\cdot2$
- products of two disjoint 2-cycles (of the form $(12)(34)$): $15=\binom{5}{2}\cdot\binom{3}{2}\cdot\frac{1}{2}$
- 5-cycles (of the form $(12345)=(4\quad 5)(3\quad 5)(2\quad 5)(1\quad 5)$): $24=4!$

That these four types of permutations are mutually distinct can be seen by looking at the orders of the individual elements, and that the elements belonging to each type are distinct can be seen directly by looking at function values.

Meanwhile, in general, in a group $G$, for a subgroup $N$ to be a normal subgroup, precisely by definition, $N$ must be expressed as a union of conjugacy classes under inner automorphisms. However, using [Lemma 7](#lem7){: data-lid="au756" }, we can see that above, the 3-cycles and the products of two disjoint 2-cycles each form conjugacy classes, while the $5$-cycles split into two conjugacy classes each containing 12 elements. Now, the size of a normal subgroup of $A_5$ must divide the size of $A_5$, which is $60$, but since a non-trivial union of conjugacy classes that contains the identity and is not all of $A_5$ cannot produce a divisor of $60$, $A_5$ has no non-trivial normal subgroup.
:::

---
**References**

**[DF]** D.S. Dummit and R.M. Foote. Abstract Algebra. Wiley, 2003.

---
