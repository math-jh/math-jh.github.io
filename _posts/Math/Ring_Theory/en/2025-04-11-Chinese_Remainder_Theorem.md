---
title: "Chinese Remainder Theorem"
excerpt: "Chinese remainder theorem for products of ideals and comaximal ideals"

categories: [Math / Ring Theory]
permalink: /en/math/ring_theory/chinese_remainder_theorem
header:
    overlay_image: /assets/images/Math/Ring_Theory/Chinese_Remainder_Theorem.png
    overlay_filter: 0.5
sidebar: 
    nav: "ring_theory-en"

date: 2025-04-11
last_modified_at: 2025-04-11
weight: 2
translated_at: 2026-05-28T11:36:15+00:00
translation_source: kimi-cli
---
## Products of Ideals

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> For two two-sided ideals $$\mathfrak{a},\mathfrak{b}$$ of a ring $$A$$, their *product* $$\mathfrak{a}\mathfrak{b}$$ is defined as the set

$$\mathfrak{a}\mathfrak{b}=\{x_1y_1+x_2y_2+\cdots+x_ny_n: x_i\in \mathfrak{a}, y_i\in \mathfrak{b}, n\geq 1\}.$$

</div>

That $$\mathfrak{a}\mathfrak{b}$$ is a subgroup of $$A$$ under addition is clear. Moreover, for any element $$x_1y_1+\cdots+x_ny_n$$ of $$\mathfrak{a}\mathfrak{b}$$ and any element $$x$$ of $$A$$,

$$x(x_1y_1+\cdots+x_ny_n)=xx_1y_1+\cdots xx_ny_n$$

and since $$xx_i\in \mathfrak{a}$$, we have $$x(x_1y_1+\cdots+x_ny_n)\in \mathfrak{a}\mathfrak{b}$$. A similar argument holds for multiplication on the right, so we see that $$\mathfrak{a}\mathfrak{b}$$ is a two-sided ideal of $$A$$.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> With respect to the multiplication defined above, the collection of two-sided ideals of $$A$$ has a monoid structure with identity element $$A$$. Moreover, the distributive laws

$$\mathfrak{a}(\mathfrak{b}+\mathfrak{c})=\mathfrak{a}\mathfrak{b}+\mathfrak{a}\mathfrak{c},\quad (\mathfrak{a}+\mathfrak{b})\mathfrak{c}=\mathfrak{a}\mathfrak{c}+\mathfrak{b}\mathfrak{c}$$

also hold.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let three two-sided ideals $$\mathfrak{a},\mathfrak{b},\mathfrak{c}$$ be given. Then any element of $$(\mathfrak{a}\mathfrak{b})\mathfrak{c}$$ can be written in the form

$$\left(\sum_{i=1}^{n_1} x_i^{(1)}y_i^{(1)}\right)z_1+\cdots+\left(\sum_{i=1}^{n_k}x_i^{(k)}y_i^{(k)}\right)z_k$$

and expanding everything using the distributive law and then grouping the rightmost two factors, we see that this element belongs to $$\mathfrak{a}(\mathfrak{b}\mathfrak{c})$$. The reverse inclusion can be proved in the same way, so multiplication is associative. Also, it is clear that $$A \mathfrak{a}=\mathfrak{a}A=\mathfrak{a}$$ for any two-sided ideal $$\mathfrak{a}$$.

Finally, for any $$b_1+c_1,\ldots, b_n+c_n\in \mathfrak{b}+\mathfrak{c}$$, expanding

$$a_1(b_1+c_1)+\cdots a_n(b_n+c_n)$$

using the distributive law, one can easily show that $$\mathfrak{a}(\mathfrak{b}+\mathfrak{c})\subset \mathfrak{a}\mathfrak{b}+\mathfrak{a}\mathfrak{c}$$. Conversely, for any

$$a_1b_1+\cdots+a_nb_n + a_1'c_1+\cdots +a_m'c_m\in \mathfrak{a}\mathfrak{b}+\mathfrak{a}\mathfrak{c}$$

since the $$b_i$$ and $$c_i$$ all belong to $$\mathfrak{b}+\mathfrak{c}$$, the above element lies in $$\mathfrak{a}(\mathfrak{b}+\mathfrak{c})$$. Similarly, one can prove the right distributive law.

</details>

Thus the collection of two-sided ideals of $$A$$ has a structure identical to that of a ring except for additive inverses. Such a structure is called a semiring, though we will not have much use for it.

For any two two-sided ideals $$\mathfrak{a},\mathfrak{b}$$, the two inclusions

$$\mathfrak{a}\mathfrak{b}\subset \mathfrak{a}A\subset \mathfrak{a},\quad \mathfrak{a}\mathfrak{b}\subset A \mathfrak{b}\subset \mathfrak{b}$$

both hold, so $$\mathfrak{a}\mathfrak{b}\subset \mathfrak{a}\cap \mathfrak{b}$$ holds. In general equality need not hold, but it may hold in special cases.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> Let $$\mathfrak{a},\mathfrak{b}_1,\ldots, \mathfrak{b}_n$$ be two-sided ideals of $$A$$, and assume that $$A=\mathfrak{a}+\mathfrak{b}_i$$ holds for all $$i$$. Then

$$A=\mathfrak{a}+\mathfrak{b}_1\cdots \mathfrak{b}_n=\mathfrak{a}+(\mathfrak{b}_1\cap\cdots\cap \mathfrak{b}_n)$$

holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Since $$\mathfrak{b}_1\cdots \mathfrak{b}_n\subset \mathfrak{b}_1\cap \cdots\cap \mathfrak{b}_n$$ in any case, it suffices to show the equality $$A=\mathfrak{a}+\mathfrak{b}_1\cdots \mathfrak{b}_n$$. Moreover, since the proof proceeds by induction, it is enough to consider the case $$n=2$$. That is, suppose $$A=\mathfrak{a}+\mathfrak{b}_1=\mathfrak{a}+\mathfrak{b}_2$$, and let us show that $$A=\mathfrak{a}+\mathfrak{b}_1 \mathfrak{b}_2$$.

First, from $$A=\mathfrak{a}+\mathfrak{b}_1=\mathfrak{a}+\mathfrak{b}_2$$, we can choose $$a,a'\in \mathfrak{a}, b_i\in \mathfrak{b}_i$$ satisfying $$1=a+b_1=a'+b_2$$. Then

$$1=a'+b_2=a'+1b_2=a'+(a+b_1)b_2=(a+a'b_2)+b_1b_2\in \mathfrak{a}+\mathfrak{b}_1 \mathfrak{b}_2$$

holds.

</details>

Using this we can prove the following proposition.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> Let $$\mathfrak{b}_1,\ldots, \mathfrak{b}_n$$ be two-sided ideals of $$A$$ such that $$\mathfrak{b}_i+\mathfrak{b}_j=A$$ ($$i\neq j$$) always holds. Then the equality

$$\mathfrak{b}_1\cap \cdots\cap \mathfrak{b}_n=\sum_{\sigma\in S_n} \mathfrak{b}_{\sigma(1)}\cdots \mathfrak{b}_{\sigma(n)}$$

holds, and therefore in particular if $$A$$ is commutative then

$$\mathfrak{b}_1\cap \cdots\cap \mathfrak{b}_n=\mathfrak{b}_1\cdots \mathfrak{b}_n$$

holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

We prove this by induction as well. First, in the case $$n=2$$, we can find $$b_i\in \mathfrak{b}_i$$ satisfying $$b_1+b_2=1$$. Now for any $$x\in \mathfrak{b}_1\cap \mathfrak{b}_2$$,

$$x=x\cdot 1=x(b_1+b_2)=xb_1+xb_2\in \mathfrak{b}_2 \mathfrak{b}_1+\mathfrak{b}_1 \mathfrak{b}_2$$

holds. Now assume the desired equality holds for all integers less than $$n$$. First, applying [Proposition 3](#prop3) to $$\mathfrak{b}_n=\mathfrak{a}$$ and $$\mathfrak{b}_1,\ldots, \mathfrak{b}_{n-1}$$, we obtain

$$A=\mathfrak{b}_n+(\mathfrak{b}_1\cap\cdots\cap \mathfrak{b}_{n-1})=\mathfrak{b}_n+\mathfrak{b}_1\cdots \mathfrak{b}_{n-1}$$

so for the two ideals $$\mathfrak{b}_n$$ and $$\mathfrak{b}_1\cap\cdots\cap\mathfrak{b}_{n-1}$$,

$$\mathfrak{b}_n\cap(\mathfrak{b}_1\cap\cdots\cap\mathfrak{b}_{n-1})=(\mathfrak{b}_1\cap\cdots\cap\mathfrak{b}_{n-1})\mathfrak{b}_n+\mathfrak{b}_n(\mathfrak{b}_1\cap\cdots\cap\mathfrak{b}_{n-1})$$

holds. By the induction hypothesis $$\mathfrak{b}_1\cap\cdots\cap\mathfrak{b}_{n-1}=\sum_{\sigma\in S_{n-1}}\mathfrak{b}_{\sigma(1)}\cdots\mathfrak{b}_{\sigma(n-1)}$$ holds, so from this

$$\mathfrak{b}_n\cap(\mathfrak{b}_1\cap\cdots\cap\mathfrak{b}_{n-1})=\left(\sum_{\sigma\in S_{n-1}}\mathfrak{b}_{\sigma(1)}\cdots\mathfrak{b}_{\sigma(n-1)}\right)\mathfrak{b}_n+\mathfrak{b}_n\left(\sum_{\sigma\in S_{n-1}}\mathfrak{b}_{\sigma(1)}\cdots \mathfrak{b}_{\sigma(n-1)}\right)$$

and here the right-hand side is a partial sum of $$\sum_{\sigma\in S_n}\mathfrak{b}_{\sigma(1)}\cdots \mathfrak{b}_{\sigma(n)}$$, so we obtain the desired conclusion.

</details>

## Chinese Remainder Theorem

Let $$A$$ be a ring, and let $$\mathfrak{a}_i$$ be two-sided ideals of $$A$$. Then there exist projections $$\pi_i:A \rightarrow A/\mathfrak{a}_i$$, and from these a ring homomorphism $$\pi:A \rightarrow\prod A/\mathfrak{a}_i$$ is defined.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> Let $$A$$ be a ring, and let $$\mathfrak{a}_1,\ldots, \mathfrak{a}_n$$ be two-sided ideals of $$A$$. If $$\mathfrak{a}_i+\mathfrak{a}_j=A$$ always holds for $$i\neq j$$, then the $$\pi:A \rightarrow \prod_1^n A/\mathfrak{a}_i$$ defined above is surjective, and the kernel of this map equals $$\bigcap \mathfrak{a}_i$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, $$\ker\pi=\bigcap \mathfrak{a}_i$$ is clear, so it suffices to show that $$\pi$$ is surjective. This can be shown by induction as follows.

First, the case $$n=1$$ is clear from the properties of the quotient ring. Now suppose there exists some $$y\in A$$ such that $$\pi_i(y)=x_i+\mathfrak{a}_i$$ holds for all $$i=1,\ldots, n-1$$. If there exists $$x\in A$$ satisfying $$\pi_i(x)=x_i+\mathfrak{a}_i$$ for all $$i=1,\ldots, n$$, then we can write $$x=y+z$$ for some $$z\in A$$, and then the conditions on $$x$$ and $$y$$ require that $$z\in\bigcap_{i=1}^{n-1} \mathfrak{a}_i$$. Also, $$z+\mathfrak{a}_n=x_n-y \mathfrak{a}_n$$ must hold, and conversely, if such $$z$$ exists then $$x=y+z$$ is the desired $$x$$. But by [Proposition 3](#prop3), $$\mathfrak{a}_n+\bigcap_1^{n-1} \mathfrak{a}_i=A$$ holds, so we can always find such $$z$$.

</details>

Therefore, by the first isomorphism theorem there exists the canonical isomorphism

$$\frac{A}{\bigcap_{i=1}^n \mathfrak{a}_i}\cong \prod_{i=1}^n A/\mathfrak{a}_i$$

and if $$A$$ is commutative then by [Proposition 4](#prop4) it can be written as

$$A/\mathfrak{a}_1\cdots \mathfrak{a}_n\cong\prod_{i=1}^n A/\mathfrak{a}_i.$$

In particular, if $$\bigcap \mathfrak{a}_i=0$$ then we obtain an isomorphism $$A\cong\prod A/\mathfrak{a}_i$$.

In particular, consider the case $$A=\mathbb{Z}$$, and for pairwise coprime $$n_1,\ldots, n_r$$ let $$\mathfrak{a}_i=n_i \mathbb{Z}$$. Letting $$n=n_1\cdots n_r$$, by the above proposition and the first isomorphism theorem we obtain an isomorphism $$\mathbb{Z}/n \mathbb{Z}\cong\prod \mathbb{Z}/n_i \mathbb{Z}$$. That is, from the above proposition we recover the classical Chinese remainder theorem.

More generally, the following are all equivalent.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> Let $$A$$ be a ring, let $$C(A)$$ be its center, and let $$\mathfrak{a}_1,\ldots, \mathfrak{a}_n$$ be two-sided ideals of $$A$$. The following are all equivalent.

1. The $$A \rightarrow \prod A/\mathfrak{a}_i$$ defined above is an isomorphism.
2. For all $$i\neq j$$, $$\mathfrak{a}_i+\mathfrak{a}_j=A$$ and $$\bigcap \mathfrak{a}_i=0$$.
3. For all $$i\neq j$$, $$\mathfrak{a}_i+\mathfrak{a}_j=A$$ and $$\prod \mathfrak{a}_i=0$$.
4. There exist elements $$e_1,\ldots, e_n$$ of $$C(A)$$ such that $$\sum e_i=1$$, $$e_i^2=e_i$$ for all $$i$$, $$e_ie_j=0$$ for all $$i\neq j$$, and $$\mathfrak{a}_i=A(1-e_i)$$ for all $$i$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

The $$e_i$$ in the last condition denote the elements of $$\prod A/\mathfrak{a}_i$$ whose $$i$$th component is $$1$$ and whose remaining components are all $$0$$. With this in mind, one can easily show that the four conditions are all equivalent.

</details>
