---
title: "Symmetric Groups"
description: "We examine the definition of the symmetric group on a set, cycle notation, composition of cycles, and the concept of disjoint cycles."
excerpt: "Cycle decomposition and sign of the symmetric group, and the alternating group"

categories: [Math / Group Theory]
permalink: /en/math/group_theory/symmetric_groups
sidebar: 
    nav: "group_theory-en"

date: 2025-03-29
last_modified_at: 2025-03-29
weight: 1
translated_at: 2026-05-31T10:00:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-31T10:00:04+00:00
---
In the [Algebraic Structures](/en/algebraic_structures) category we were interested in the common properties shared by various algebraic structures; however, while this approach is good for surveying how algebraic theories develop from an overall perspective, it is ill suited for examining details such as computing a specific group. Therefore, in the posts in this category we study properties of groups not covered in the [Algebraic Structures](/en/algebraic_structures) category.

## Symmetric Groups

The first objects we examine in the [Group Theory](/en/group_theory) category are specific groups.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> For the set $$[n]=\{1,\ldots, n\}$$, we call the automorphism group $$\Aut([n])$$ of $$[n]$$ in $$\Set$$ the *symmetric group* and write it as $$S_n$$.

</div>

That is, the elements of $$S_n$$ are bijections from the set $$[n]$$ to $$[n]$$, and the operation of $$S_n$$ is given by composition of functions. The elements of $$S_n$$ are called *permutations*.

Given a permutation $$\sigma: [n] \rightarrow [n]$$, consider the $$n+1$$ elements of the set $$[n]$$

$$1=\sigma^0(1), \quad\sigma(1)=\sigma^1(1),\quad\sigma^2(1),\quad\cdots, \quad\sigma^n(1)\tag{$\ast$}$$

By the pigeonhole principle there exist two distinct integers $$0\leq k_1,k_2\leq n$$ such that $$\sigma^{k_1}(1)=\sigma^{k_2}(1)$$, and assuming $$k_1< k_2$$ for convenience, we know from this that $$\sigma^{k_2-k_1}(1)=1$$. Moreover, letting $$k$$ be the smallest positive integer satisfying $$\sigma^k(1)=1$$, from the above result we have $$k\leq n$$, and based on this we can consider the notation

$$(1\quad \sigma(1)\quad \sigma^2(1)\quad\cdots\quad\sigma^{k-1}(1))$$

By definition this notation means the function sending $$1$$ to $$\sigma(1)$$, $$\sigma(1)$$ to $$\sigma^2(1)$$, $$\ldots$$, $$\sigma^{k-2}(1)$$ to $$\sigma^{k-1}(1)$$, and $$\sigma^{k-1}(1)$$ to $$\sigma^k(1)=1$$; and more generally

$$(a_1\quad a_2\quad\cdots\quad a_{k})$$

means the function sending $$a_1$$ to $$a_2$$, $$\ldots$$, $$a_{k-1}$$ to $$a_{k}$$, and $$a_k$$ to $$a_1$$ while leaving the remaining elements unchanged. We call this a *cycle* of length $$k$$. Then for two cycles $$\sigma$$, $$\tau$$, the product $$\sigma\tau$$ means the composition $$\sigma\circ\tau$$ of the functions $$\sigma$$ and $$\tau$$.

<div class="example" markdown="1">

<ins id="ex2">**Example 2**</ins> For example, consider the element $$\sigma=(1\;2\;3)$$ of $$S_3$$. This function sends $$1$$ to $$2$$, $$2$$ to $$3$$, and $$3$$ to $$1$$. On the other hand, consider the following composition

$$\tau_1\tau_2=(2\;3)(1\;3)$$

Then first, under $$\tau_2$$, $$1$$ is moved to $$3$$, $$2$$ stays at $$2$$, and $$3$$ is moved to $$1$$. Afterwards, under $$\tau_1$$, $$3$$ (which was originally $$1$$) is moved to $$2$$, and $$2$$ is moved to $$3$$, so $$\tau_1\tau_2$$ sends $$1$$ to $$2$$, $$2$$ to $$3$$, and $$3$$ to $$1$$. That is, as functions $$\sigma=\tau_1\tau_2$$. On the other hand, if we consider the composition

$$\tau_2\tau_1=(1\;3)(2\;3)$$

we see that $$1$$ is moved to $$3$$, $$2$$ to $$1$$, and $$3$$ to $$2$$. Hence $$\tau_1\tau_2\neq\tau_2\tau_1$$.

</div>

The composition of elements of $$S_n$$ is composition of functions, and since composition of functions is generally not commutative, the above example is what we expected. However, in special cases two functions may commute.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> Permutations $$\sigma_1,\ldots,\sigma_r\in S_n$$ are called *disjoint* if whenever some $$i$$ satisfies $$\sigma_i(k)\neq k$$, then for all other $$j\neq i$$ we have $$\sigma_j(k)=k$$.

</div>

Then it is obvious that the product of arbitrary disjoint permutations $$\sigma_1,\ldots,\sigma_r\in S_n$$ does not depend on their order. Moreover, the following holds.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> Any non-identity permutation of $$S_n$$ can be written as a product of disjoint cycles.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Define an equivalence relation $$\sim$$ on the set $$[n]$$ by

$$i\sim j\iff \sigma^m(i)=j\text{ for some $m$}$$

and let its quotient set be

$$[n]/{\sim}=\{C_1, \ldots, C_r\}$$

Now for each $$1\leq k\leq r$$ define by the following formula

$$\sigma_k(i)=\begin{cases}\sigma(x)&\text{if $x\in C_k$}\\x&\text{otherwise}\end{cases}$$

Then these are disjoint cycles and their product is $$\sigma$$.

</details>

If we represent an arbitrary permutation as a product of disjoint cycles in this way, one of the advantages is that the order of a permutation $$\sigma$$ is easily seen. That is, if we write $$\sigma=\sigma_1\cdots\sigma_r$$, then the order of $$\sigma$$ equals the least common multiple of the orders of $$\sigma_1,\ldots, \sigma_r$$, and the orders of the cycles $$\sigma_1,\ldots, \sigma_r$$ are, of course, equal to their respective lengths.

Meanwhile, let us call a cycle of length $$2$$ a *transposition*. This is simply the function that swaps the two numbers appearing in this cycle. Then by the above proposition the following holds.

<div class="proposition" markdown="1">

<ins id="cor5">**Corollary 5**</ins> Any permutation of $$S_n$$ can be written as a product of transpositions.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

By [Proposition 4](#prop4) it suffices to prove that an arbitrary cycle can be written as a product of transpositions.

$$(k_1\;k_2\;\cdots\;k_r)=(k_{r-1}\;k_r)(k_{r-2}\;k_r)\cdots(k_2\;k_r)(k_1\;k_r).$$

</details>

Meanwhile, to represent all elements of $$S_n$$, just two elements suffice.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> Every element of $$S_n$$ can be written as a product of $$(1\;2)$$ and $$(1\;2\;\cdots\;n)$$.

</div>

To prove this we first examine the following.

<div class="proposition" markdown="1">

<ins id="lem7">**Lemma 7**</ins> Let $$\sigma\in S_n$$. Then $$\sigma(1\;2)\sigma^{-1}=(\sigma(1)\;\sigma(2))$$ holds.

</div>

Of course, $$1$$ and $$2$$ may be replaced by any other numbers.

<details class="proof--alone" markdown="1">
<summary>Proof</summary>

First, for any $$i\geq 3$$, consider the value of $$\sigma(1\;2)\sigma^{-1}(\sigma(i))$$. Then $$\sigma(i)$$ is first moved to $$\sigma^{-1}(\sigma(i))=i$$. Since $$i\geq 3$$, this value is unchanged by $$(1\;2)$$ and returns to $$\sigma(i)$$ by the next $$\sigma$$. That is, the $$\sigma(i)$$ with $$i\geq 3$$ are all invariant under this transformation, so we only need to examine the values of $$\sigma(1)$$ and $$\sigma(2)$$.

$$\sigma(1)$$ is first moved to $$1$$ via $$\sigma^{-1}$$. Then, in $$(1\;2)$$ this value becomes $$2$$ and finally in $$\sigma$$ it becomes $$\sigma(2)$$, so as a result $$\sigma(1)$$ is moved to $$\sigma(2)$$. Likewise one can show that $$\sigma(2)$$ is moved to $$\sigma(1)$$.

Therefore $$\sigma(1\;2)\sigma^{-1}=(\sigma(1)\;\sigma(2))$$ holds.

</details>

Substituting $$\sigma=(1\;2\;\cdots\;n)$$, $$(1\;2\;\cdots\;n)^2$$, $$\ldots$$ into [Lemma 7](#lem7), we obtain $$(2\;3)$$, $$(3\;4)$$, $$\ldots$$. On the other hand, for any $$(a\;b)$$, assuming without loss of generality that $$a<b$$,

$$\begin{aligned}
    (a\;b)&=(a\;a+1)(a+1\;b)(a\;a+1)\\
    &=(a\;a+1)(a+1\;a+2)(a+2\;b)(a+1\;a+2)(a\;a+1)\\
    &=\cdots\\
    &=(a\;a+1)(a+1\;a+2)\cdots(b-1\;b)\cdots(a+1\;a+2)(a\;a+1)
\end{aligned}$$

thus $$(a\;b)$$ can be written as a product of cycles of the form $$(i\;i+1)$$. Therefore using $$(1\;2)$$ and $$(1\;2\;\cdots\;n)$$ we can generate any $$(a\;b)$$. But for any cycle $$(a_1\;a_2\;\cdots\;a_k)$$ the formula

$$(a_1\;a_2\;\cdots\;a_k)=(a_1\;a_2)(a_2\;a_3)\cdots(a_{k-1}\;a_k)$$

holds, so $$(1\;2)$$ and $$(1\;2\;\cdots\;n)$$ can generate all cycles, and hence any element of $$S_n$$, so [Proposition 6](#prop6) holds.

<div class="proposition" markdown="1">

<ins id="thm8">**Theorem 8 (Cayley)**</ins> For any finite group $$G$$, there exists a natural number $$n$$ such that $$G$$ can be made isomorphic to some subgroup of $$S_n$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

In other words, it suffices to find a suitable inclusion homomorphism $$\iota:G\rightarrow S_n$$. For each element $$g$$ of the group $$G$$, define the following *left translation map*

$$L_g: G\rightarrow G,\qquad x\mapsto gx$$

Then by the cancellation law $$L_g$$ is an injective homomorphism. Moreover, for any $$x\in G$$,

$$x=g(g^{-1}x)=L_g(g^{-1}x)$$

so $$L_g$$ is also a surjective homomorphism. That is, $$L_g$$ becomes an automorphism defined on $$G$$. Let $$\lvert G\rvert=n$$. Then an automorphism defined on $$G$$ is also a bijection defined on the set $$G$$, so the $$L_g$$ may all be regarded as elements of $$S_n$$. Now define $$T:G\rightarrow S_n$$ by the formula

$$T(g)=L_g$$

Then for any $$x\in G$$,

$$T(gh)(x)=L_{gh}(x)=(gh)x=g(h(x))=(T_g\circ T_h)(x)$$

holds. That is, $$T$$ is a group homomorphism. One can also easily verify that $$T$$ is injective, so we obtain the desired result.

</details>

## Alternating Groups

<div class="definition" markdown="1">

<ins id="def9">**Definition 9**</ins> For each element $$\sigma$$ of $$S_n$$, pairs $$(i,j)$$ with $$i<j$$ but $$\sigma(i)>\sigma(j)$$ are called *inversions*. If the number of inversions is odd, we call $$\sigma$$ an *odd permutation*, and if the number of inversions is even we call $$\sigma$$ an *even permutation*.

</div>

For example, the identity permutation has 0 inversions so is an even permutation, and $$(1\;2)$$ has only the pair $$(1,2)$$ satisfying that condition so is an odd permutation. Many algebra books, including Dummit and Hungerford, define an even permutation instead as

> a permutation that can be expressed as a product of an even number of transpositions

The strength of this definition compared to ours just now is that properties such as the product of two even permutations being even and the product of an odd and an even permutation being odd are more intuitively obvious. But unlike our definition just now, it is not obvious that the parity (i.e., whether $$\sigma$$ is even or odd) is well defined. Therefore it is convenient to carry both definitions along. These books therefore show through the following lemma that this definition is the same as [Definition 9](#def9) we just defined.

<div class="proposition" markdown="1">

<ins id="lem10">**Lemma 10**</ins> That $$\sigma$$ is an even permutation is equivalent to $$\sigma$$ being expressible as a product of an even number of transpositions.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

For $$n$$ variables $$x_1,\ldots, x_n$$, define the *Vandermonde polynomial* $$\Delta$$ by the formula

$$\Delta=\prod_{1\leq i< j\leq n}(x_i-x_j)$$

One can easily observe that $$\Delta$$ is a polynomial consisting only of the product of terms $$(x_i-x_j)$$ corresponding to all pairs $$(i,j)$$ satisfying $$i< j$$. Now apply precomposition to $$\Delta$$ to make $$\sigma(\Delta)$$. That is,

$$\sigma(\Delta)=\prod_{1\leq i< j\leq n}(x_{\sigma(i)}-x_{\sigma(j)})$$

Then for each pair $$(i,j)$$, the term $$(x_{\sigma(i)}-x_{\sigma(j)})$$ can be rewritten according to the order relation between $$\sigma(i)$$ and $$\sigma(j)$$ as

$$(x_{\sigma(i)}-x_{\sigma(j)})=\begin{cases}(x_{\sigma(i)}-x_{\sigma(j)})&\text{if $\sigma(i)<\sigma(j)$}\\-(x_{\sigma(j)}-x_{\sigma(i)})&\text{if $\sigma(i)>\sigma(j)$}\end{cases}\tag{1}$$

Moreover, since $$\sigma$$ is a bijection, if we rewrite all terms in this way we see that $$\sigma(\Delta)$$ is exactly the same polynomial as $$\Delta$$ up to sign. Therefore, defining $$\sgn(\sigma)=\sigma(\Delta)/\Delta$$, the quantity $$\sgn(\sigma)$$ becomes exactly the parity of $$\sigma$$ defined in the sense of [Definition 9](#def9).

From the definition, it is obvious that if $$\sigma$$ is a transposition then $$\sgn(\sigma)=-1$$. Therefore, if we can only show that $$\sgn$$ is multiplicative,

$$\text{$\sigma$ odd}\iff\text{$\sgn(\sigma)=-1$}\iff\text{$\sigma$ is a product of odd number of permutations}$$

will hold, so we will obtain the desired result. Let two permutations $$\sigma$$, $$\tau$$ be given. We must compute the value of $$\sgn(\sigma\tau)$$. Suppose $$\tau$$ has $$k$$ inversions. That is, $$\sgn(\tau)=(-1)^k$$, and these $$k$$ copies of $$-1$$ all come from factors in equation (1). To compute the value of $$\sgn(\sigma\tau)$$ we first multiply both sides of

$$\prod_{1\leq i< j\leq n}(x_{\tau(i)}-x_{\tau(j)})=(-1)^k\Delta$$

by $$(-1)^k$$, restoring the terms on the left-hand side to their original form (that is, in this situation the left-hand side is just $$\Delta$$ with the order of multiplication changed), and then apply $$\sigma$$ to this restored polynomial. Therefore, if the number of inversions of $$\sigma$$ was $$l$$, the factor attached in front of $$\Delta$$ would be $$(-1)^{k+l}$$, and this guarantees the multiplicativity of $$\sgn$$.

</details>

If we examine this proof carefully, the $$\sgn$$ we constructed is in fact not just a map but a group homomorphism from $$S_n$$ to $$\{\pm 1\}$$. Then $$\ker(\sgn)$$ is a normal subgroup of $$S_n$$.

<div class="definition" markdown="1">

<ins id="def11">**Definition 11**</ins> We call the kernel of the group homomorphism $$\sgn$$ defined above the *alternating group* of degree $$n$$, and denote it by $$A_n$$. In other words, $$A_n$$ is the set of all even permutations.

</div>

We also make the following definition.

<div class="definition" markdown="1">

<ins id="def12">**Definition 12**</ins> A group $$G$$ is called *simple* if it has no normal subgroups other than $$\{e\}$$ and itself.

</div>

One notable fact is that $$A_5$$ is simple.

<div class="example" markdown="1">

<ins id="ex13">**Example 13**</ins> $$A_5$$ is simple. This can be shown in a more elegant way using Sylow theorems, but $$A_5$$ is not such a large group, so with a little effort we can show this with only our current knowledge.

First, the permutations inside $$A_5$$ can be classified into the following types:

- 1 identity element
- 3-cycles (of the form $$(123)=(2\;3)(1\;3)$$): $$20=\binom{5}{3}\cdot2$$
- products of two disjoint 2-cycles (of the form $$(12)(34)$$): $$15=\binom{5}{2}\cdot\binom{3}{2}\cdot\frac{1}{2}$$
- 5-cycles (of the form $$(12345)=(4\;5)(3\;5)(2\;5)(1\;5)$$): $$24=4!$$

That these four types of permutations are mutually distinct can be seen by looking at the orders of the individual elements, and that elements belonging to the same type are distinct from one another can be seen directly by looking at function values.

In general, for a subgroup $$N$$ of a group $$G$$ to be a normal subgroup, by definition $$N$$ must be expressible as a union of conjugacy classes under inner automorphisms. Now using [Lemma 7](#lem7), we can see that the 3-cycles and the products of two disjoint 2-cycles each form single conjugacy classes, while the 5-cycles split into two conjugacy classes each containing 12 elements. The size of a normal subgroup of $$A_5$$ must divide the size of $$A_5$$, which is 60, but no union of non-trivial conjugacy classes containing the identity can produce a divisor of 60, so $$A_5$$ has no non-trivial normal subgroup.

</div>

---
**References**

**[DF]** D.S. Dummit and R.M. Foote. Abstract Algebra. Wiley, 2003.

---
