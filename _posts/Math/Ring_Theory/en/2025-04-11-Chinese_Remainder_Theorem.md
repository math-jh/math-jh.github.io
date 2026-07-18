---
title: "The Chinese Remainder Theorem"
description: "Starting from congruences of integers, we prove the Chinese remainder theorem generalized to comaximal ideals. The key tool is that pairwise comaximal ideals in a commutative ring have intersection equal to their product, and we also cover the correspondence between product decompositions and central idempotent decompositions."
excerpt: "The Chinese remainder theorem for comaximal ideals and central idempotent decompositions"

categories: [Math / Ring Theory]
permalink: /en/math/ring_theory/chinese_remainder_theorem
sidebar: 
    nav: "ring_theory-en"

date: 2025-04-11
weight: 3
translated_at: 2026-07-18T10:30:02+00:00
translation_source: kimi-cli
---
The Chinese remainder theorem is a classical result in number theory, and its essence is the ring isomorphism

$$\mathbb{Z}/mn\mathbb{Z}\cong \mathbb{Z}/m\mathbb{Z}\times \mathbb{Z}/n\mathbb{Z},\qquad \text{$m,n$ coprime})$$

([\[Number Theory\] §Chinese Remainder Theorem, ⁋Theorem 1](/en/math/number_theory/chinese_remainder_theorem#thm1)). In other words, knowing the remainders of an integer upon division by $m$ and by $n$ separately determines the remainder upon division by $mn$ perfectly, and the goal of this post is to extend this to an arbitrary ring $A$.

Briefly, this generalization first replaces $m\mathbb{Z}$ and $n\mathbb{Z}$ by ideals of a ring $A$, and understands $mn\mathbb{Z}$ as the intersection of these two ideals. However, this generalization does not work for arbitrary ideals; a condition corresponding to the coprimality of $m$ and $n$ above is also required.

The goal of this post is to generalize this to ideals of an arbitrary ring $A$. Here, the condition on ideals corresponding to "coprime" is *comaximal*. Two ideals $\mathfrak{a},\mathfrak{b}$ are called comaximal when they satisfy $\mathfrak{a}+\mathfrak{b}=A$, which means that an expression of the form $1=u+v$ ($u\in\mathfrak{a}, v\in\mathfrak{b}$) exists, and this corresponds exactly to the Bézout representation $1=\gcd(m,n)$ for integers. The generalized theorem states that for pairwise comaximal ideals $\mathfrak{a}_i$, the ring isomorphism

$$A/\Big(\bigcap_i \mathfrak{a}_i\Big)\cong \prod_i A/\mathfrak{a}_i$$

holds, and if $A$ is commutative, the intersection–product equality $\bigcap_i\mathfrak{a}_i=\mathfrak{a}_1\cdots\mathfrak{a}_n$ shown later allows us to write this also as $A/\mathfrak{a}_1\cdots\mathfrak{a}_n\cong\prod_i A/\mathfrak{a}_i$.

This equality is a subtle fact that requires both the comaximal condition and commutativity. In the next section we define the product of ideals and secure this first.

## Product of Ideals

::: Definition 1
For two two-sided ideals $\mathfrak{a},\mathfrak{b}$ of a ring $A$, their *product* $\mathfrak{a}\mathfrak{b}$ is the set

$$\mathfrak{a}\mathfrak{b}=\{x_1y_1+x_2y_2+\cdots+x_ny_n: x_i\in \mathfrak{a}, y_i\in \mathfrak{b}, n\geq 1\}.$$

:::

That $\mathfrak{a}\mathfrak{b}$ is a subgroup under addition of $A$ is obvious. On the other hand, for any element $x_1y_1+\cdots+x_ny_n$ of $\mathfrak{a}\mathfrak{b}$ and any element $x$ of $A$,

$$x(x_1y_1+\cdots+x_ny_n)=xx_1y_1+\cdots xx_ny_n$$

and since $xx_i\in \mathfrak{a}$, we have $x(x_1y_1+\cdots+x_ny_n)\in \mathfrak{a}\mathfrak{b}$. A similar argument works when multiplying by $x$ on the right, so we can verify that $\mathfrak{a}\mathfrak{b}$ is a two-sided ideal of $A$.

::: Proposition 2
With multiplication defined as above, the collection of two-sided ideals of $A$ forms a monoid with identity $A$. Moreover, the distributive laws

$$\mathfrak{a}(\mathfrak{b}+\mathfrak{c})=\mathfrak{a}\mathfrak{b}+\mathfrak{a}\mathfrak{c},\quad (\mathfrak{a}+\mathfrak{b})\mathfrak{c}=\mathfrak{a}\mathfrak{c}+\mathfrak{b}\mathfrak{c}$$

also hold.
:::
::: Proof
Let three two-sided ideals $\mathfrak{a},\mathfrak{b},\mathfrak{c}$ be given. Then any element of $(\mathfrak{a}\mathfrak{b})\mathfrak{c}$ can be written in the form

$$\left(\sum_{i=1}^{n_1} x_i^{(1)}y_i^{(1)}\right)z_1+\cdots+\left(\sum_{i=1}^{n_k}x_i^{(k)}y_i^{(k)}\right)z_k$$

and using the distributive law to expand everything and then grouping the rightmost two terms, we see that this element belongs to $\mathfrak{a}(\mathfrak{b}\mathfrak{c})$. The reverse inclusion can be proved in exactly the same way, so multiplication is associative. Also, for any two-sided ideal $\mathfrak{a}$ it is obvious that $A \mathfrak{a}=\mathfrak{a}A=\mathfrak{a}$.

Finally, for arbitrary $b_1+c_1,\ldots, b_n+c_n\in \mathfrak{b}+\mathfrak{c}$,

$$a_1(b_1+c_1)+\cdots a_n(b_n+c_n)$$

can be expanded using the distributive law, and $\mathfrak{a}(\mathfrak{b}+\mathfrak{c})\subset \mathfrak{a}\mathfrak{b}+\mathfrak{a}\mathfrak{c}$ follows easily. Conversely, for any

$$a_1b_1+\cdots a_nb_n + a_1'c_1+\cdots +a_m'c_m\in \mathfrak{a}\mathfrak{b}+\mathfrak{a}\mathfrak{c}$$

since the $b_i$ and $c_i$ are all elements of $\mathfrak{b}+\mathfrak{c}$, the above element is an element of $\mathfrak{a}(\mathfrak{b}+\mathfrak{c})$. The right distributive law can be proved similarly.
:::

For any two two-sided ideals $\mathfrak{a},\mathfrak{b}$, since the two inclusions

$$\mathfrak{a}\mathfrak{b}\subset \mathfrak{a}A\subset \mathfrak{a},\quad \mathfrak{a}\mathfrak{b}\subset A \mathfrak{b}\subset \mathfrak{b}$$

both hold, we have $\mathfrak{a}\mathfrak{b}\subset \mathfrak{a}\cap \mathfrak{b}$. In general equality need not hold.

::: Definition 3 (Comaximal ideals)
Two two-sided ideals $\mathfrak{a},\mathfrak{b}$ of a ring $A$ are called *comaximal* when they satisfy $\mathfrak{a}+\mathfrak{b}=A$. This means that the identity $1$ can be expressed in the form $1=u+v$ ($u\in\mathfrak{a}, v\in\mathfrak{b}$), which corresponds exactly to the existence of the Bézout identity $mu+nv=1$ for two coprime integers $m,n$ in number theory. The ideals $m\mathbb{Z},n\mathbb{Z}$ for coprime $m,n$ being comaximal in $\mathbb{Z}$ is an example. Several ideals $\mathfrak{a}_1,\ldots,\mathfrak{a}_n$ are called *pairwise comaximal* if $\mathfrak{a}_i+\mathfrak{a}_j=A$ for all $i\ne j$.
:::

However, when two ideals are comaximal, surprisingly equality does hold, and to show this we first prove the following auxiliary result.

::: Proposition 4
Let two-sided ideals $\mathfrak{a},\mathfrak{b}_1,\ldots, \mathfrak{b}_n$ of $A$ be given, and assume that $A=\mathfrak{a}+\mathfrak{b}_i$ holds for every $i$. Then

$$A=\mathfrak{a}+\mathfrak{b}_1\cdots \mathfrak{b}_n=\mathfrak{a}+(\mathfrak{b}_1\cap\cdots\cap \mathfrak{b}_n)$$

holds.
:::
::: Proof
Since $\mathfrak{b}_1\cdots \mathfrak{b}_n\subset \mathfrak{b}_1\cap \cdots\cap \mathfrak{b}_n$ anyway, it suffices to show the equality $A=\mathfrak{a}+\mathfrak{b}_1\cdots \mathfrak{b}_n$. Moreover, because the proof proceeds by induction, it suffices to consider the case $n=2$. That is, assume $A=\mathfrak{a}+\mathfrak{b}_1=\mathfrak{a}+\mathfrak{b}_2$, and let us show $A=\mathfrak{a}+\mathfrak{b}_1 \mathfrak{b}_2$.

First, from $A=\mathfrak{a}+\mathfrak{b}_1=\mathfrak{a}+\mathfrak{b}_2$ we can choose $a,a'\in \mathfrak{a}, b_i\in \mathfrak{b}_i$ satisfying $1=a+b_1=a'+b_2$. Then

$$1=a'+b_2=a'+1b_2=a'+(a+b_1)b_2=(a+a'b_2)+b_1b_2\in \mathfrak{a}+\mathfrak{b}_1 \mathfrak{b}_2$$

holds.
:::

We now obtain the key tool used in the commutative case.

::: Proposition 5
Let ideals $\mathfrak{b}_1,\ldots, \mathfrak{b}_n$ of a commutative ring $A$ be pairwise comaximal, i.e. assume $\mathfrak{b}_i+\mathfrak{b}_j=A$ for $i\neq j$. Then

$$\mathfrak{b}_1\cap \cdots\cap \mathfrak{b}_n=\mathfrak{b}_1\cdots \mathfrak{b}_n$$

holds.
:::
::: Proof
We prove this by induction. Since $\mathfrak{b}_1\cdots\mathfrak{b}_n\subseteq \mathfrak{b}_1\cap\cdots\cap\mathfrak{b}_n$ always holds, it suffices to show the reverse inclusion.

First let $n=2$ and assume $\mathfrak{b}_1+\mathfrak{b}_2=A$. Writing $1=u+v$ ($u\in\mathfrak{b}_1, v\in\mathfrak{b}_2$), for any $x\in\mathfrak{b}_1\cap\mathfrak{b}_2$ we use the fact that $A$ is commutative to obtain

$$x=x\cdot 1=x(u+v)=xu+xv\in \mathfrak{b}_2 \mathfrak{b}_1+\mathfrak{b}_1 \mathfrak{b}_2=\mathfrak{b}_1 \mathfrak{b}_2.$$

Hence $\mathfrak{b}_1\cap\mathfrak{b}_2=\mathfrak{b}_1\mathfrak{b}_2$.

Now let $n>2$. Applying [Proposition 4](#prop4) to $\mathfrak{a}=\mathfrak{b}_n$ and $\mathfrak{b}_1,\ldots,\mathfrak{b}_{n-1}$ (that these are pairwise comaximal is obvious),

$$A=\mathfrak{b}_n+(\mathfrak{b}_1\cap\cdots\cap \mathfrak{b}_{n-1})$$

and by the induction hypothesis $\mathfrak{b}_1\cap\cdots\cap \mathfrak{b}_{n-1}=\mathfrak{b}_1\cdots \mathfrak{b}_{n-1}$. Applying the $n=2$ result to the comaximal ideals $\mathfrak{b}_n$ and $\mathfrak{b}_1\cap\cdots\cap \mathfrak{b}_{n-1}$,

$$\mathfrak{b}_1\cap\cdots\cap \mathfrak{b}_n=(\mathfrak{b}_1\cap\cdots\cap \mathfrak{b}_{n-1})\cap \mathfrak{b}_n=(\mathfrak{b}_1\cap\cdots\cap \mathfrak{b}_{n-1})\mathfrak{b}_n=\mathfrak{b}_1\cdots \mathfrak{b}_n$$

follows.
:::

(As a remark, when $A$ is not commutative the intersection becomes the symmetric sum of products in all orders, $\sum_{\sigma\in S_n}\mathfrak{b}_{\sigma(1)}\cdots\mathfrak{b}_{\sigma(n)}$, rather than the single product $\mathfrak{b}_1\cdots\mathfrak{b}_n$, and only in the commutative case does this collapse to a single product. For the commutative case that is the main subject of this post, the equality above suffices.)

## Chinese Remainder Theorem

Let a ring $A$ and two-sided ideals $\mathfrak{a}_i$ of $A$ be given. Then projections $\pi_i:A \rightarrow A/\mathfrak{a}_i$ to each quotient ring exist, and from these a ring homomorphism $\pi:A \rightarrow\prod A/\mathfrak{a}_i$ is defined. The question of when this map is an isomorphism is the heart of the Chinese remainder theorem.

::: Proposition 6
Let a ring $A$ and two-sided ideals $\mathfrak{a}_1,\ldots, \mathfrak{a}_n$ of $A$ be given. If $\mathfrak{a}_i+\mathfrak{a}_j=A$ always holds for $i\neq j$, then the $\pi:A \rightarrow \prod_1^n A/\mathfrak{a}_i$ defined above is surjective, and the kernel of this map equals $\bigcap \mathfrak{a}_i$.
:::
::: Proof
Clearly $\ker\pi=\bigcap_i \mathfrak{a}_i$, so it suffices to show surjectivity. Let us directly construct an element realizing an arbitrary target $(x_1+\mathfrak{a}_1,\ldots,x_n+\mathfrak{a}_n)\in\prod A/\mathfrak{a}_i$ in the image of $\pi$.

If for each $i$ we can find an element $e_i\in A$ that plays the role of being $1$ in the $i$-th position and $0$ elsewhere, i.e. satisfying $e_i\equiv 1\pmod{\mathfrak{a}_i}$ and $e_i\equiv 0\pmod{\mathfrak{a}_j}$ ($j\ne i$), then $x=\sum_i x_i e_i$ hits the target in every position simultaneously. Let us construct such $e_i$ explicitly from the pairwise comaximal condition. For a fixed $i$, since $\mathfrak{a}_i+\mathfrak{a}_j=A$ for each $j\ne i$, we can choose elements $1=u_{ij}+v_{ij}$ ($u_{ij}\in\mathfrak{a}_i,\ v_{ij}\in\mathfrak{a}_j$), and set

$$e_i=\prod_{j\ne i}v_{ij}.$$

For each $j\ne i$, since $v_{ij}\in\mathfrak{a}_j$ appears among the factors of $e_i$, we have $e_i\in\mathfrak{a}_j$, while for $\mathfrak{a}_i$ we have $v_{ij}=1-u_{ij}\equiv 1\pmod{\mathfrak{a}_i}$, so $e_i\equiv 1\pmod{\mathfrak{a}_i}$. Therefore $x=\sum_i x_i e_i$ satisfies $\pi_i(x)=x_i+\mathfrak{a}_i$, and $\pi$ is surjective.
:::

Therefore, by the first isomorphism theorem, the following canonical isomorphism

$$\frac{A}{\bigcap_{i=1}^n \mathfrak{a}_i}\cong \prod_{i=1}^n A/\mathfrak{a}_i$$

exists. If $A$ is commutative, [Proposition 5](#prop5) allows us to replace the intersection by a product, giving

$$A/\mathfrak{a}_1\cdots \mathfrak{a}_n\cong\prod_{i=1}^n A/\mathfrak{a}_i$$

and in particular if $\bigcap \mathfrak{a}_i=0$ we obtain the isomorphism $A\cong\prod A/\mathfrak{a}_i$.

The original integer version is the special case $A=\mathbb{Z}$. For pairwise coprime integers $n_1,\ldots, n_r$, setting $\mathfrak{a}_i=n_i \mathbb{Z}$ and $n=n_1\cdots n_r$, the coprime condition becomes precisely the comaximal condition $\mathfrak{a}_i+\mathfrak{a}_j=\mathbb{Z}$, so the above proposition yields the isomorphism $\mathbb{Z}/n \mathbb{Z}\cong\prod \mathbb{Z}/n_i \mathbb{Z}$. In other words, for any tuple of remainders $(a_i \bmod n_i)_i$ there exists a unique integer simultaneously realizing them modulo $n$, and this is the classical Chinese remainder theorem.

The isomorphism $A\cong\prod A/\mathfrak{a}_i$ of Proposition 6 is a strong fact that the ring $A$ splits into a product of smaller rings. Such a product decomposition is neatly described by *idempotents lying in the center* of the ring, and this is the content of the following equivalent statement. (A serious treatment of idempotents is the subject of the next post, so we only mention it briefly here.)

::: Proposition 7
Let a ring $A$, its center $C(A)$, and two-sided ideals $\mathfrak{a}_1,\ldots, \mathfrak{a}_n$ be given. The following are all equivalent.

1. The $\pi:A \rightarrow \prod A/\mathfrak{a}_i$ defined above is an isomorphism.
2. For all $i\neq j$, $\mathfrak{a}_i+\mathfrak{a}_j=A$ and $\bigcap \mathfrak{a}_i=0$.
3. There exist elements $e_1,\ldots, e_n$ of $C(A)$ such that $\sum e_i=1$, $e_i^2=e_i$ for all $i$, $e_ie_j=0$ for all $i\neq j$, and $\mathfrak{a}_i=A(1-e_i)$ for all $i$.
:::
::: Proof
We show that the three conditions are equivalent in the cycle (1)$\Leftrightarrow$(2)$\Rightarrow$(3)$\Rightarrow$(1).

(1)$\Leftrightarrow$(2): By [Proposition 6](#prop6), $\pi$ being surjective is equivalent to the pairwise comaximal condition, and since $\ker\pi=\bigcap\mathfrak{a}_i$ always holds, $\pi$ being an isomorphism is equivalent to (2).

(2)$\Rightarrow$(3): By (2), $\pi$ is an isomorphism. In $\prod A/\mathfrak{a}_i$, let $\bar{e}_i$ be the element whose $i$-th component is $1+\mathfrak{a}_i$ and all others are $0$. Then $\sum\bar{e}_i=\bar{1}$, $\bar{e}_i^2=\bar{e}_i$, $\bar{e}_i\bar{e}_j=0$ hold, and since each component is either the identity or $0$ of a quotient ring, $\bar{e}_i$ lies in the center of $\prod A/\mathfrak{a}_i$. Setting $e_i:=\pi^{-1}(\bar{e}_i)$, because $\pi$ is an isomorphism we have $e_i\in C(A)$ and the $e_i$ inherit the idempotent and orthogonality relations above. Moreover, since the $i$-th component of $\bar{e}_i$ is $1$, $1-e_i$ goes to $0$ under $\pi_i$, and hence $1-e_i\in\ker\pi_i=\mathfrak{a}_i$. Therefore $A(1-e_i)\subseteq \mathfrak{a}_i$. Conversely, let $a\in\mathfrak{a}_i$; then $a=ae_i+a(1-e_i)$, but all components of $ae_i$ become $0$ (the $i$-th is $\pi_i(a)\pi_i(e_i)=0\cdot 1=0$, and in the remaining components $\bar{e}_i$ is $0$), so $ae_i\in\bigcap\mathfrak{a}_i=0$ and thus $a=a(1-e_i)\in A(1-e_i)$. That is, $\mathfrak{a}_i=A(1-e_i)$.

(3)$\Rightarrow$(1): Since $e_i\in C(A)$ and these are orthogonal idempotents with $\sum e_i=1$, we have $A=\bigoplus_i Ae_i$. The map $A\to Ae_i$, $a\mapsto ae_i$ is surjective and its kernel is $A(1-e_i)=\mathfrak{a}_i$, so $A/\mathfrak{a}_i\cong Ae_i$. Combining these, $\prod A/\mathfrak{a}_i\cong\prod Ae_i\cong A$, and since this composition coincides with the original map $\pi$, $\pi$ is an isomorphism.
:::

If $A$ is commutative, [Proposition 5](#prop5) gives $\bigcap\mathfrak{a}_i=\mathfrak{a}_1\cdots\mathfrak{a}_n$, so the condition $\bigcap\mathfrak{a}_i=0$ in condition 2 can also be written as $\mathfrak{a}_1\cdots\mathfrak{a}_n=0$.
