---
title: "Operations on Cardinals"
description: "We define addition and multiplication operations between cardinal numbers that represent the size of sets, and examine how the properties of unions and Cartesian products extend to cardinal arithmetic."
excerpt: "Operations on cardinal numbers"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/operation_of_cardinals
sidebar: 
    nav: "set_theory-en"

date: 2021-09-04
weight: 24
translated_at: 2026-06-02T22:00:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-11-05T07:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
## Operations Between Cardinals

Now, as promised, let us define operations between cardinals.

::: Definition 1
Let $(\mathfrak{a}_i)_{i\in I}$ be a family of cardinals. The cardinal of the product (resp. sum) of the sets $\mathfrak{a}_i$ is called their *cardinal product* (resp. *cardinal sum*) and is denoted by $\prod_{i\in I}\mathfrak{a}_i$ (resp. $\sum_{i\in I}\mathfrak{a}_i$).
:::

This is why, when we first defined the sum of sets, we used the term "sum" instead of the intuitive name "disjoint union."

First, the above definitions are well-defined. This is because if $A_i$ and $\mathfrak{a}_i$ are equipotent, there also exists a bijection between $\prod_{i\in I} A_i$ and $\prod_{i\in I}\mathfrak{a}_i$. In the case of the sum, the sum itself is not uniquely determined, but by [§Sum of Sets, ⁋Corollary 9](/en/math/set_theory/sum_of_sets#cor9){: data-lid="haqzj" }, there always exists a bijection between such sums, so the cardinal is uniquely determined. With these operations, the properties of sums and products translate into properties of operations between cardinals as follows.

::: Proposition 2
Let $(\mathfrak{a}_i)_{i\in I}$ be a family of cardinals, and let $f$ be a bijection from $K$ to $I$. Then

$$\sum_{k\in K}\mathfrak{a}_{f(k)}=\sum_{i\in I}\mathfrak{a}_i,\quad \prod_{k\in K}\mathfrak{a}_{f(k)}=\prod_{i\in I}\mathfrak{a}_i$$ 

Also, if $(J_l)_{l\in L}$ is a partition of $I$, then

$$\sum_{i\in I}\mathfrak{a}_{i}=\sum_{l\in L}\sum_{i\in J_l}\mathfrak{a}_i,\quad \prod_{i\in I}\mathfrak{a}_{i}=\prod_{l\in L}\prod_{i\in J_l}\mathfrak{a}_i$$
:::
::: Proof
By [§Sum of Sets, ⁋Proposition 7](/en/math/set_theory/sum_of_sets#prop7){: data-lid="1u144" }, we may regard the sum of cardinals as the union of a pairwise disjoint family. Now, the first equations are consequences of [§Union and Intersection, ⁋Proposition 4](/en/math/set_theory/union_and_intersection#prop4){: data-lid="cx0l9" } and [§Product of Sets, ⁋Proposition 5](/en/math/set_theory/product_of_sets#prop5){: data-lid="udxxv" }, respectively, and the second equations are consequences of [§Union and Intersection, ⁋Proposition 5](/en/math/set_theory/union_and_intersection#prop5){: data-lid="gbo4a" } and [§Properties of Products, ⁋Proposition 3](/en/math/set_theory/property_of_products#prop3){: data-lid="c6f2y" }.
:::

::: Proposition 3
Let $(\mathfrak{a}_i)_{i\in I}$ be a family of cardinals, and let $J$ (resp. $K$) be a subset of $I$ satisfying $\mathfrak{a}_i=\mathbf{0}$ for all $i\not\in J$ (resp. $\mathfrak{a}_i=\mathbf{1}$ for all $i\not\in K$). Then

$$\sum_{i\in I}\mathfrak{a}_i=\sum_{i\in J}\mathfrak{a}_i,\quad \prod_{i\in I}\mathfrak{a}_i=\prod_{i\in K}\mathfrak{a}_i$$

hold.
:::
::: Proof
Taking the union with the empty set and taking the product with a singleton do not affect the cardinal. ($x\mapsto (x,i)$ defines a bijection from $A$ to $A\times\{i\}$.)
:::

In addition to these obvious results, applying the distributive law between product and union yields the following proposition ([§Properties of Products, ⁋Proposition 7](/en/math/set_theory/property_of_products#prop7){: data-lid="w8k31" }).

::: Proposition 4
For a family $((\mathfrak{a}_{k,j})_{j\in J_k})_{k\in K}$ of cardinals with double indices, if we let $I=\prod_{k\in K}J_k$, then 

$$\prod_{k\in K}\left(\sum_{j\in J_k}\mathfrak{a}_{k,j}\right)=\sum_{f\in I}\left(\prod_{k\in K}\mathfrak{a}_{k, f(k)}\right)$$

holds.
:::

In particular, if we consider the above propositions only in the finite case,

- Since the order in which we take the union of two sets $A$ and $B$ does not matter, $\mathfrak{a}+\mathfrak{b}=\mathfrak{b}+\mathfrak{a}$, and since there exists a natural bijection between $A\times B$ and $B\times A$, $\mathfrak{a}\mathfrak{b}=\mathfrak{b}\mathfrak{a}$.
- By the associativity of the sum and product of sets, $\mathfrak{a}+(\mathfrak{b}+\mathfrak{c})=(\mathfrak{a}+\mathfrak{b})+\mathfrak{c}$ and $\mathfrak{a}(\mathfrak{b}\mathfrak{c})=(\mathfrak{a}\mathfrak{b})\mathfrak{c}$
- Finally, rewriting the distributive law in the finite case, $\mathfrak{a}(\mathfrak{b}+\mathfrak{c})=\mathfrak{a}\mathfrak{b}+\mathfrak{a}\mathfrak{c}$.

we obtain such results. On the other hand, since any set can be written as a sum of singletons (that is, $B=\bigcup_{x\in B}\{x\}$ always holds), if $I$ is a set with cardinal $\mathfrak{b}$, we obtain

$$\mathfrak{b}=\sum_{i\in I} \mathfrak{c}_i,\qquad \mathfrak{c}_i=\mathbf{1}\text{ for all $i\in I$}$$

and multiplying both sides by $\mathfrak{a}$ and applying the earlier [Proposition 4](#prop4){: data-lid="hdhtc" }, we obtain

$$\mathfrak{a}\mathfrak{b}=\mathfrak{a}\left(\sum_{i\in I}\mathfrak{c}_i\right)=\sum_{i\in I}\mathfrak{a}\mathfrak{c}_i=\sum_{i\in I}\mathfrak{a}$$

::: Proposition 5
Let $(\mathfrak{a}_i)_{i\in I}$ be a family of cardinals. Then $\prod_{i\in I}\mathfrak{a}_i\neq \mathbf{0}$ is equivalent to $\mathfrak{a}_i\neq \mathbf{0}$ for all $i\in I$.
:::
::: Proof
An extension of [§Ordered Pairs, ⁋Proposition 10](/en/math/set_theory/ordered_pair#prop10){: data-lid="5h0nt" } to arbitrary products. The proof can be carried out in the same way, except that choosing an element from each $\mathfrak{a}_i$ simultaneously from an arbitrary family is done by the choice function $f$ given by [§Axiom of Choice, ⁋The Axiom of Choice.](/en/math/set_theory/axiom_of_choice#axiom-choice){: data-lid="7zjwo" }, where $f(i)\in\mathfrak{a}_i$ specifies an element of the product.
:::

::: Proposition 6
If $\mathfrak{a}$ and $\mathfrak{b}$ are cardinals satisfying $\mathfrak{a}+\mathbf{1}=\mathfrak{b}+\mathbf{1}$, then $\mathfrak{a}=\mathfrak{b}$.
:::
::: Proof
Let $X$ be a set of cardinal $\mathfrak{a}+\mathbf{1}=\mathfrak{b}+\mathbf{1}$. Then there exist subsets of the set $X$ of cardinal $\mathfrak{a}$ and $\mathfrak{b}$ such that $X\setminus A$ and $X\setminus B$ are singletons. Let $X\setminus A=\{a\}$ and $X\setminus B=\{b\}$; it suffices to define a bijection from $A$ to $B$ by

$$f(x)=\begin{cases}a&\text{if }x=b\\ x&\text{otherwise}\end{cases}$$
:::

We can even define exponentiation between cardinals. We just need to use the set of functions $B^A$.

::: Definition 7
Let $\mathfrak{a}$ and $\mathfrak{b}$ be cardinals. The cardinal of the set of functions from $\mathfrak{a}$ to $\mathfrak{b}$ is denoted by $\mathfrak{b}^\mathfrak{a}$.
:::

Strictly speaking, of course, the representative of the equivalence class of $\mathfrak{b}^\mathfrak{a}$ may differ from the above set of functions, so there is a slight abuse of notation,[^2] but since it is clear from the context, we choose to write it this way.

::: Proposition 8
Let $\mathfrak{a}$ and $\mathfrak{b}$ be cardinals, and let $I$ be a set satisfying $\card I=\mathfrak{b}$. If $\mathfrak{a}_i=\mathfrak{a}$ for all $i\in I$, then $\mathfrak{a}^\mathfrak{b}=\prod_{i\in I}\mathfrak{a}_i$.
:::
::: Proof
An element of the product $\prod_{i\in I}\mathfrak{a}_i$ specifies, for each $i\in I$, an element of $\mathfrak{a}_i=\mathfrak{a}$, that is, a function from $I$ to $\mathfrak{a}$; hence this product is equal to the set of functions $\mathfrak{a}^I$. Since $\card I=\mathfrak{b}$, by [Definition 7](#def7){: data-lid="3gfyp" }, the cardinal of this set is $\mathfrak{a}^\mathfrak{b}$.
:::

Properties concerning the cardinals $\mathbf{0}$ and $\mathbf{1}$, such as $\mathfrak{a}^\mathbf{0}=\mathbf{1}$, $\mathfrak{a}^\mathbf{1}=\mathfrak{a}$, $\mathbf{1}^\mathfrak{a}=\mathbf{1}$, and, when $\mathfrak{a}\neq\mathbf{0}$, $\mathbf{0}^\mathfrak{a}=\mathbf{0}$, can be easily proved. One of the most important theorems here is the following theorem.

::: Proposition 9
Let $A$ be a set and $\mathfrak{a}$ its cardinal. Then the cardinal of $\mathcal{P}(A)$ is $\mathbf{2}^\mathfrak{a}$.
:::
::: Proof
Let $\mathbf{2}=\{\alpha, \beta\}$ be a cardinal with $\alpha\neq\beta$. For any $X\in\mathcal{P}(A)$, there exists a function $f_X:A\rightarrow \mathbf{2}$ such that if $x\in X$ then $x\mapsto\alpha$, and otherwise $x\mapsto\beta$. Conversely, for any function $f:A\rightarrow \mathbf{2}$, $f^{-1}(\alpha)$ determines an element of $\mathcal{P}(A)$.
:::

The following is Cantor's famous theorem.

::: Proposition 10 (Cantor)
For any cardinal $\mathfrak{a}$, $\mathbf{2}^\mathfrak{a}>\mathfrak{a}$ always holds.
:::
::: Proof
Since $x\mapsto \{x\}$ is an injection from $\mathfrak{a}$ into the power set, $\mathfrak{a}\leq \mathbf{2}^\mathfrak{a}$ is obvious. Thus it suffices to show $\mathfrak{a}\neq\mathbf{2}^\mathfrak{a}$. That is, for any function $f:\mathfrak{a}\rightarrow\mathcal{P}(\mathfrak{a})$, we only need to show that there always exists some element outside the image of $\mathfrak{a}$.

Let $X$ be the set of elements satisfying $x\not\in f(x)$ among all $x\in\mathfrak{a}$. If $x\in X$, then $x\not\in f(x)$, so $f(x)\neq X$; conversely, if $x\not\in X$, then $x\in f(x)$, so again $f(x)\neq X$. Therefore $X\not\in f(\mathfrak{a})$, and the proof is complete.
:::

If $\mathfrak{a}$ is a finite set and $\mathfrak{a}\geq\mathbf{2}$, there always exists some cardinal between $\mathfrak{a}$ and $\mathbf{2}^\mathfrak{a}$. However, in the infinite case, this is not so obvious. For example, while it is obvious from the above proposition that the size of the power set of $\mathbb{N}$ is larger than the size of the set of natural numbers $\mathbb{N}$, it is not easy to predict whether any cardinal lies between the two.

To write more rigorously, we defined $\aleph_0,\aleph_1,\ldots$ as initial ordinals. If we construct a new sequence of cardinals by the equation

$$\beth_0=\aleph_0,\quad \beth_{\alpha+1}=\mathbf{2}^{\beth_\alpha}$$

then since $\beth_1$ is definitely larger than $\beth_0=\aleph_0$, by the definition of $\aleph$ it is greater than or equal to $\aleph_1$. That is, $\aleph_1\leq \beth_1$. Cantor proved that the size of the set of real numbers $\mathbb{R}$ equals $\beth_1$, and proposed the *continuum hypothesis* that in fact $\aleph_1=\beth_1$. If this hypothesis holds, the real numbers become a set having the size immediately following the natural numbers. More generally, that $\aleph_\alpha=\beth_\alpha$ holds is the generalized continuum hypothesis.

This hypothesis remained an open problem after its proposal, until Gödel and Cohen proved that this hypothesis can be neither proved nor disproved in the ZFC axiom system. Gödel proved relatively early that CH cannot be disproved in the ZFC axiom system, and later Cohen proved that CH cannot be proved in the ZFC axiom system.


---

**References**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
