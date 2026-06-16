---
title: "Operations on Cardinals"
description: "We define addition and multiplication operations between cardinal numbers that represent the size of sets, and examine how the properties of unions and Cartesian products extend to cardinal arithmetic."
excerpt: "Operations on cardinal numbers"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/operation_of_cardinals
sidebar: 
    nav: "set_theory-en"

date: 2021-09-04
weight: 25
translated_at: 2026-06-02T22:00:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-02T22:00:02+00:00
---
## Operations Between Cardinals

We now define operations on cardinals as promised.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Let $$(\mathfrak{a}_i)_{i\in I}$$ be a family of cardinals. The cardinal of the product (resp. sum) of the sets $$\mathfrak{a}_i$$ is called their *cardinal product* (resp. *cardinal sum*) and is denoted by $$\prod_{i\in I}\mathfrak{a}_i$$ (resp. $$\sum_{i\in I}\mathfrak{a}_i$$).

</div>

This is why, when we first defined the sum of sets, we used the term "sum" instead of the more intuitive name "disjoint union."

First, the above definitions are well-defined. If each $$A_i$$ is equipotent to $$\mathfrak{a}_i$$, then there exists a bijection between $$\prod_{i\in I} A_i$$ and $$\prod_{i\in I}\mathfrak{a}_i$$. With these operations in hand, the properties of sums and products for sets translate into the following properties for operations between cardinals.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> Let $$(\mathfrak{a}_i)_{i\in I}$$ be a family of cardinals, and let $$f$$ be a bijection from $$K$$ to $$I$$. Then

$$\sum_{k\in K}\mathfrak{a}_{f(k)}=\sum_{i\in I}\mathfrak{a}_i,\quad \prod_{k\in K}\mathfrak{a}_{f(k)}=\prod_{i\in I}\mathfrak{a}_i$$

Also, if $$(J_l)_{l\in L}$$ is a partition of $$I$$, then

$$\sum_{i\in I}\mathfrak{a}_{i}=\sum_{l\in L}\sum_{i\in J_l}\mathfrak{a}_i,\quad \prod_{i\in I}\mathfrak{a}_{i}=\prod_{l\in L}\prod_{i\in J_l}\mathfrak{a}_i$$

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

By [§Sum of Sets, ⁋Proposition 7](/en/math/set_theory/sum_of_sets#prop7), we may regard the sum of cardinals as the union of a mutually disjoint family. The first equations are consequences of [§Union and Intersection, ⁋Proposition 4](/en/math/set_theory/union_and_intersection#prop4) and [§Product of Sets, ⁋Proposition 5](/en/math/set_theory/product_of_sets#prop5), respectively, and the second equations follow from [§Union and Intersection, ⁋Proposition 5](/en/math/set_theory/union_and_intersection#prop5) and [§Properties of Products, ⁋Proposition 3](/en/math/set_theory/property_of_products#prop3).

</details>

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> Let $$(\mathfrak{a}_i)_{i\in I}$$ be a family of cardinals, and let $$J$$ (resp. $$K$$) be a subset of $$I$$ satisfying $$\mathfrak{a}_i=\mathbf{0}$$ for all $$i\not\in J$$ (resp. $$\mathfrak{a}_i=\mathbf{1}$$ for all $$i\not\in K$$). Then

$$\sum_{i\in I}\mathfrak{a}_i=\sum_{i\in J}\mathfrak{a}_i,\quad \prod_{i\in I}\mathfrak{a}_i=\prod_{i\in K}\mathfrak{a}_i$$

hold.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Taking the union with the empty set and taking the product with a singleton do not affect the cardinal. (The map $$x\mapsto (x,i)$$ defines a bijection from $$A$$ to $$A\times\{i\}$$.)

</details>

Beyond these obvious facts, applying the distributive law between product and union ([§Properties of Products, ⁋Proposition 7](/en/math/set_theory/property_of_products#prop7)) yields the following proposition.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> For a doubly-indexed family $$((\mathfrak{a}_{j,k})_{j\in J_k})_{k\in K}$$ of cardinals, letting $$I=\prod_{k\in K}J_k$$,

$$\prod_{k\in K}\left(\sum_{j\in J_k}\mathfrak{a}_{j,k}\right)=\sum_{f\in I}\left(\prod_{k\in K}\mathfrak{a}_{k, f(k)}\right)$$

holds.
</div>

In particular, restricting the above propositions to the finite case, we obtain:

- The order in which we take the union of two sets $$A$$ and $$B$$ does not matter, so $$\mathfrak{a}+\mathfrak{b}=\mathfrak{b}+\mathfrak{a}$$; and since there is a natural bijection between $$A\times B$$ and $$B\times A$$, we have $$\mathfrak{a}\mathfrak{b}=\mathfrak{b}\mathfrak{a}$$.
- By the associativity of sum and product for sets, $$\mathfrak{a}+(\mathfrak{b}+\mathfrak{c})=(\mathfrak{a}+\mathfrak{b})+\mathfrak{c}$$ and $$\mathfrak{a}(\mathfrak{b}\mathfrak{c})=(\mathfrak{a}\mathfrak{b})\mathfrak{c}$$.
- Finally, rewriting the distributive law in the finite case gives $$\mathfrak{a}(\mathfrak{b}+\mathfrak{c})=\mathfrak{a}\mathfrak{c}+\mathfrak{a}\mathfrak{b}$$.

On the other hand, since any set can be written as a sum of singletons (that is, $$B=\bigcup_{x\in B}\{x\}$$ always holds), if $$I$$ is a set with cardinal $$\mathfrak{b}$$, then

$$\mathfrak{b}=\sum_{i\in I} \mathfrak{c}_i,\qquad \mathfrak{c}_i=1\text{ for all $i\in I$}$$

Multiplying both sides by $$\mathfrak{a}$$ and applying [Proposition 4](#prop4) above, we obtain

$$\mathfrak{a}\mathfrak{b}=\mathfrak{a}\left(\sum_{i\in I}\mathfrak{c}_i\right)=\sum_{i\in I}\mathfrak{a}\mathfrak{c}_i=\sum_{i\in I}\mathfrak{a}$$

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> Let $$(\mathfrak{a}_i)_{i\in I}$$ be a family of cardinals. Then $$\prod_{i\in I}\mathfrak{a}_i\neq \mathbf{0}$$ if and only if $$\mathfrak{a}_i\neq \mathbf{0}$$ for all $$i\in I$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

This is the extension of [§Ordered Pairs, ⁋Proposition 10](/en/math/set_theory/ordered_pair#prop10) to arbitrary products. The proof is identical.

</details>

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> If $$\mathfrak{a}$$ and $$\mathfrak{b}$$ are cardinals satisfying $$\mathfrak{a}+\mathbf{1}=\mathfrak{b}+\mathbf{1}$$, then $$\mathfrak{a}=\mathfrak{b}$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$X$$ be a set with cardinal $$\mathfrak{a}+\mathbf{1}=\mathfrak{b}+\mathbf{1}$$. Then there exist subsets of $$X$$ with cardinals $$\mathfrak{a}$$ and $$\mathfrak{b}$$ such that $$X\setminus A$$ and $$X\setminus B$$ are singletons. Let $$X\setminus A=\{a\}$$ and $$X\setminus B=\{b\}$$. We define a bijection from $$A$$ to $$B$$ by

$$f(x)=\begin{cases}a&\text{if }x=b\\ x&\text{otherwise}\end{cases}$$

</details>

We can even define exponentiation for cardinals. We use the set of functions $$B^A$$.

<div class="definition" markdown="1">

<ins id="def7">**Definition 7**</ins> Let $$\mathfrak{a}$$ and $$\mathfrak{b}$$ be cardinals. The cardinal of the set of functions from $$\mathfrak{b}$$ to $$\mathfrak{a}$$ is denoted by $$\mathfrak{b}^\mathfrak{a}$$.

</div>

Strictly speaking, since the representative of the equivalence class for $$\mathfrak{b}^\mathfrak{a}$$ may differ from the above set of functions, this involves a slight abuse of notation[^2]; but the meaning is clear from context, so we adopt this convention.

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8**</ins> Let $$\mathfrak{a}$$ and $$\mathfrak{b}$$ be cardinals, and let $$I$$ be a set with $$\card I=\mathfrak{b}$$. If $$\mathfrak{a}_i=\mathfrak{a}$$ for all $$i\in I$$, then $$\mathfrak{a}^\mathfrak{b}=\prod_{i\in I}\mathfrak{a}_i$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

This is immediate from the bijection between $$B^A$$ and $$\Fun(A,B)$$.

</details>

Properties of the cardinals $$\mathbf{0}$$ and $$\mathbf{1}$$, such as $$\mathfrak{a}^\mathbf{0}=\mathbf{1}$$, $$\mathfrak{a}^\mathbf{1}=\mathfrak{a}$$, $$\mathbf{1}^\mathfrak{a}=\mathbf{1}$$, and $$\mathbf{0}^\mathfrak{a}=\mathbf{0}$$, are easily proved. One of the most important theorems here is the following.

<div class="proposition" markdown="1">

<ins id="prop9">**Proposition 9**</ins> Let $$A$$ be a set and $$\mathfrak{a}$$ its cardinal. Then the cardinal of $$\mathcal{P}(A)$$ is $$\mathbf{2}^\mathfrak{a}$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$\mathbf{2}=\{\alpha, \beta\}$$ be a cardinal. For any $$X\in\mathcal{P}(A)$$, there exists a function $$f_X:A\rightarrow \mathbf{2}$$ such that if $$x\in X$$ then $$x\mapsto\alpha$$, and otherwise $$x\mapsto\beta$$. Conversely, for any function $$f:A\rightarrow \mathbf{2}$$, the preimage $$f^{-1}(\alpha)$$ determines an element of $$\mathcal{P}(A)$$.

</details>

Next is Cantor's famous theorem.

<div class="proposition" markdown="1">

<ins id="prop10">**Proposition 10 (Cantor)**</ins> For any cardinal $$\mathfrak{a}$$, we always have $$\mathbf{2}^\mathfrak{a}>\mathfrak{a}$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Since $$x\mapsto \{x\}$$ is an injection from $$\mathfrak{a}$$ into the power set, $$\mathfrak{a}\leq \mathbf{2}^\mathfrak{a}$$ is obvious. Thus it suffices to show $$\mathfrak{a}\neq\mathbf{2}^\mathfrak{a}$$. In other words, for any function $$f:\mathfrak{a}\rightarrow\mathcal{P}(\mathfrak{a})$$, we must show that there is always some element outside the image of $$\mathfrak{a}$$.

Let $$X$$ be the set of all $$x\in\mathfrak{a}$$ such that $$x\not\in f(x)$$. If $$x\in X$$, then $$x\not\in f(x)$$, so $$f(x)\neq X$$. Conversely, if $$x\not\in X$$, then $$x\in f(x)$$, so again $$f(x)\neq X$$. Therefore $$X\not\in f(\mathfrak{a})$$, and the proof is complete.

</details>

If $$\mathfrak{a}$$ is finite, there is always some cardinal strictly between $$\mathfrak{a}$$ and $$\mathbf{2}^\mathfrak{a}$$. In the infinite case, however, this is far from obvious. For example, while the above proposition makes it clear that the power set of $$\mathbb{N}$$ is strictly larger than $$\mathbb{N}$$ itself, it is not easy to predict whether any cardinal lies between them.

To state this more precisely, recall that we defined $$\aleph_0,\aleph_1,\ldots$$ as initial ordinals. If we define a new sequence of ordinals by

$$\beth_0=\aleph_0,\quad \beth_{\alpha+1}=\mathbf{2}^{\beth_\alpha}$$

then $$\beth_1$$ is certainly larger than $$\beth_0=\aleph_0$$, so by the definition of the $$\aleph$$ sequence we have $$\aleph_1\leq \beth_1$$. Cantor proved that the cardinality of the real numbers $$\mathbb{R}$$ equals $$\beth_1$$, and proposed the *continuum hypothesis* that $$\aleph_1=\beth_1$$. If this hypothesis holds, then the real numbers constitute the set of cardinality immediately succeeding that of the natural numbers. More generally, the statement that $$\aleph_\alpha=\beth_\alpha$$ for all $$\alpha$$ is the generalized continuum hypothesis.

This hypothesis remained open after its proposal, until Gödel and Cohen proved that it can be neither proved nor disproved within the ZFC axiom system. Gödel showed relatively early that CH cannot be disproved in ZFC, and Cohen later proved that CH cannot be proved in ZFC.


---

**References** 

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
