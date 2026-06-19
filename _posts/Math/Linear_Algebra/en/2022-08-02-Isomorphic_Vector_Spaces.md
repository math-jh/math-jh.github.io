---
title: "Isomorphisms"
description: "An isomorphism between vector spaces is defined as a bijective linear map that preserves structure, and it is shown that its inverse is also linear, proving that isomorphism is an equivalence relation."
excerpt: "Equivalent vector spaces"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/isomorphic_vector_spaces
sidebar: 
    nav: "linear_algebra-en"


date: 2022-08-02

weight: 7
translated_at: 2026-05-31T22:30:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-31T22:30:05+00:00
---
In mathematics, after defining certain objects we usually proceed to group and classify them according to whether they are <em>the same</em>. For example, when dealing with sets, two sets $$A,B$$ of the same size are regarded as the same, which by definition means there exists a bijection between $$A$$ and $$B$$.

Of course, we cannot simply carry this over to vector spaces. If we were to regard two vector spaces of the same set-theoretic size as the same, then by [\[Set Theory\] §Natural Numbers and Infinite Sets, ⁋Corollary 16](/en/math/set_theory/natural_numbers#cor16), all finite-dimensional vector spaces over an infinite field $$\mathbb{K}$$ would have to be regarded as identical. Moreover, since functions in general do not preserve the addition and scalar multiplication of a vector space, this is clearly unsuitable for studying vector spaces.

## Isomorphic Vector Spaces

Therefore we define as follows.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Let two $$\mathbb{K}$$-vector spaces $$V,W$$ and a linear map $$L:V\rightarrow W$$ be given. Then $$L$$ is called an *isomorphism* if there exists another linear map $$L':W\rightarrow V$$ such that $$L\circ L'=\id_W$$ and $$L'\circ L=\id_V$$. When such an isomorphism between $$V$$ and $$W$$ exists, we say that $$V,W$$ are *isomorphic* and write $$V\cong W$$.

</div>

By definition, any isomorphism is a bijection between the two sets $$V,W$$. Moreover, the converse also holds by the following lemma.

<div class="proposition" markdown="1">

<ins id="lem2">**Lemma 2**</ins> Let $$L:V\rightarrow W$$ be an isomorphism between two $$\mathbb{K}$$-vector spaces $$V$$, $$W$$. Then the inverse function $$L^{-1}$$ exists, and $$L^{-1}$$ is linear.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

The existence of $$L^{-1}$$ is a result from set theory, and in this case $$L\circ L^{-1}=\id_W$$ and $$L^{-1}\circ L=\id_V$$.

Thus it suffices to show that $$L^{-1}$$ is linear. First, for any $$\alpha\in\mathbb{K}$$ and $$w\in W$$, we must show that $$L^{-1}(\alpha w)=\alpha L^{-1}(w)$$. For any $$w\in W$$ there exists a unique $$v\in V$$ such that $$L(v)=w$$, and then $$L(\alpha v)=\alpha L(v)=\alpha w$$. Now

$$L^{-1}(\alpha w)=L^{-1}(L(\alpha v))=\alpha v=\alpha L^{-1}(w).$$

Similarly, $$L^{-1}(w_1+w_2)=L^{-1}(w_1)+L^{-1}(w_2)$$ can also be shown.

</details>

The following proposition involves the same set-theoretic issue that was briefly mentioned after [\[Set Theory\] §Cardinals, ⁋Definition 1](/en/math/set_theory/cardinals#def1). Namely, it is uncertain whether <phrase>the collection of all $\mathbb{K}$-vector spaces</phrase> is actually a set, but we will pass over this without further comment.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> The relation $$\cong$$ of [Definition 1](#def1) is an equivalence relation.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

We must show that the relation $$\cong$$ is reflexive, symmetric, and transitive.

1. First, it is obvious that $$V\cong V$$ for any $$\mathbb{K}$$-vector space $$V$$, because $$\id_V:V\rightarrow V$$ is an isomorphism from $$V$$ to $$V$$.
2. By the preceding [Lemma 2](#lem2), it is obvious that $$\cong$$ is symmetric.    
3. Finally, suppose $$U\cong V$$ and $$V\cong W$$. Then there exist two isomorphisms $$L_1:U\rightarrow V$$, $$L_2: V\rightarrow W$$ such that

</details>

Although this proposition may seem obvious, it establishes the less obvious part of the classification of all finite-dimensional $$\mathbb{K}$$-vector spaces.

<div class="proposition" markdown="1">

<ins id="cor4">**Corollary 4**</ins> Any two $$n$$-dimensional $$\mathbb{K}$$-vector spaces are always isomorphic.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

[§Linear Maps, ⁋Example 14](/en/math/linear_algebra/linear_map#ex14) means that any $$n$$-dimensional $$\mathbb{K}$$-vector space $$V$$ satisfies $$V\cong \mathbb{K}^n$$. For another $$n$$-dimensional $$\mathbb{K}$$-vector space $$W$$ we also have $$W\cong \mathbb{K}^n$$, so from the fact that $$\cong$$ is an equivalence relation we know that $$V\cong W$$.

</details>

Of course the converse also holds, and therefore we see that the only invariant determining the structure of a finite-dimensional vector space is its dimension.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> Let two isomorphic $$\mathbb{K}$$-vector spaces $$V,W$$ and an isomorphism $$L:V\rightarrow W$$ be given. If $$\mathcal{B}$$ is a basis of $$V$$, then $$L(\mathcal{B})$$ is also a basis of $$W$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

[§Linear Maps, ⁋Corollary 9](/en/math/linear_algebra/linear_map#cor9).

</details>

## Rank-Nullity Theorem

Meanwhile, for a given linear map $$L$$, the spaces $$\ker L$$ and $$\im L$$ measure how far $$L$$ is from being injective and surjective, respectively. Since we have seen above that dimension is the only invariant determining a vector space, it is enough to look at the dimensions of $$\ker L$$ and $$\im L$$ rather than the spaces themselves.

<div class="definition" markdown="1">

<ins id="def6">**Definition 6**</ins> Let two $$\mathbb{K}$$-vector spaces $$V,W$$ and a linear map $$L:V\rightarrow W$$ be given. Then 

1. $$\dim\ker L$$ is called the *nullity* of $$L$$, and is denoted by $$\nullity L$$.
2. $$\dim\im L$$ is called the *rank* of $$L$$, and is denoted by $$\rank L$$.

</div>

The following two statements are hardly worth numbering separately.

1. $$L$$ is injective if and only if $$\nullity L=0$$.
2. $$L$$ is surjective if and only if $$\rank L=\dim W$$.

Moreover, the following theorem holds.

<div class="proposition" markdown="1">

<ins id="thm7">**Theorem 7 (Rank-nullity theorem)**</ins> Let two $$\mathbb{K}$$-vector spaces $$V,W$$ and a linear map $$L:V\rightarrow W$$ be given. Then the equation

$$\rank L+\nullity L=\dim V$$

always holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

For convenience, write $$\dim V=n$$ and $$\nullity L=k$$. The following two cases are obvious.

1. If $$n=k$$, then $$\ker L$$ is a subspace having the same dimension as $$V$$, so $$\ker L=V$$. Therefore $$L=0$$, and since $$\im L=0$$ we have $$\rank L=0$$, so the theorem holds.
2. Similarly, if $$k=0$$ then $$\ker L=0$$, so $$L$$ is injective. Hence, restricting the codomain of $$L$$ from $$W$$ to $$\im L$$, we obtain that $$L$$ is a bijective linear map between $$V$$ and $$\im L$$. Therefore $$\dim V=\dim\im L=\rank L$$.

Now it suffices to consider the case $$0 < k < n$$. Let $$\left\{x_1,x_2,\ldots,x_k\right\}$$ be a basis of $$\ker L$$. Since this set is a linearly independent subset of $$V$$, we can extend it to a basis $$\left\{x_1,x_2,\ldots,x_k,x_{k+1},\ldots,x_n\right\}$$ of $$V$$. Then we can show that the set $$\left\{L(x_{k+1}),L(x_{k+2}),\ldots,L(x_n)\right\}$$ is a basis of $$\im L$$ as follows.

First, this set is linearly independent: if

$$\alpha_{k+1}L(x_{k+1})+\alpha_{k+2}L(x_{k+2})+\cdots+\alpha_nL(x_n)=0$$

holds, then by linearity $$L(\sum_{i=k+1}^n \alpha_i x_i)=0$$, so $$\sum_{i=k+1}^n\alpha_ix_i\in\ker L$$, and therefore for some $$\alpha_1$$, $$\alpha_2$$, $$\ldots$$, $$\alpha_k$$ we have

$$\sum_{i=k+1}^n\alpha_ix_i=\alpha_1x_1+\alpha_2x_2+\cdots+\alpha_kx_k$$

or equivalently

$$\alpha_1x_1+\alpha_2x_2+\cdots+\alpha_kx_k-\alpha_{k+1}x_{k+1}-\cdots-\alpha_nx_n=0.$$

Since $$\left\{x_1,x_2,\ldots,x_k,x_{k+1},\ldots,x_n\right\}$$ is linearly independent, we must have $$\alpha_1=\alpha_2=\cdots=\alpha_n=0$$, and in particular $$\alpha_{k+1}=\alpha_{k+2}=\cdots=\alpha_n=0$$.

Also, this set spans $$\im L$$. Let any $$w\in \im L$$ be given. Then there exists $$v\in V$$ with $$L(v)=w$$. Writing $$v=\sum_{i=1}^n \alpha_ix_i$$, we have

$$w=L\left(\sum_{i=1}^n\alpha_ix_i\right)=L\left(\sum_{i=1}^k\alpha_ix_i\right)+L\left(\sum_{i=k+1}^n\alpha_i x_i\right)=\sum_{i=k+1}^n\alpha_i L(x_i)$$

because $$\sum_{i=1}^k\alpha_ix_i\in\ker L$$.

From the above, $$\rank L=\dim\im L=n-k=\dim V-\nullity L$$, so the equation of the theorem holds.

</details>

---

**References**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.

---
