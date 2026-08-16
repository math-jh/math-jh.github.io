---
title: "Chinese Remainder Theorem"
description: "Starting from congruences of integers, we prove the Chinese remainder theorem generalized to comaximal ideals. The key tool is that the intersection of pairwise comaximal ideals equals their product in a commutative ring, and we also cover the noncommutative case where the intersection becomes a sum of products in all orders."
excerpt: "Chinese remainder theorem for comaximal ideals"

categories: [Math / Ring Theory]
permalink: /en/math/ring_theory/chinese_remainder_theorem
sidebar: 
    nav: "ring_theory-en"

date: 2025-04-11
weight: 3
translated_at: 2026-08-16T07:47:14+00:00
translation_source: kimi-cli
---
The Chinese remainder theorem is a classical result in number theory, and its essence is the ring isomorphism

$$\mathbb{Z}/mn\mathbb{Z}\cong \mathbb{Z}/m\mathbb{Z}\times \mathbb{Z}/n\mathbb{Z},\qquad \text{$m,n$ coprime}$$

([[Number Theory] §Chinese Remainder Theorem, ⁋Theorem 1](/en/math/number_theory/chinese_remainder_theorem#thm1)). In other words, the remainder of an integer upon division by $mn$ is completely determined by its remainders upon division by $m$ and by $n$, and the goal of this post is to extend this to an arbitrary ring $A$.

Briefly speaking, this generalization first replaces $m\mathbb{Z}$ and $n\mathbb{Z}$ by ideals of the ring $A$, and understands $mn\mathbb{Z}$ as the intersection of these two ideals. However, this generalization does not work for arbitrary ideals; a condition corresponding to $m,n$ being coprime is also necessary. The corresponding condition on ideals is called *comaximal*, and then the generalized theorem in ring theory states that for pairwise comaximal ideals $\mathfrak{a}_i$, the ring isomorphism

$$A\Big/\Big(\bigcap_i \mathfrak{a}_i\Big)\cong \prod_i A/\mathfrak{a}_i$$

holds, and if $A$ is a commutative ring then the equality $\bigcap_i\mathfrak{a}_i=\mathfrak{a}_1\cdots\mathfrak{a}_n$ shown below allows us to write $A/\mathfrak{a}_1\cdots\mathfrak{a}_n\cong\prod_i A/\mathfrak{a}_i$ as well.

## Product of Ideals

::: Definition 1
For two two-sided ideals $\mathfrak{a},\mathfrak{b}$ of a ring $A$, their *product* $\mathfrak{a}\mathfrak{b}$ is the set

$$\mathfrak{a}\mathfrak{b}=\{x_1y_1+x_2y_2+\cdots+x_ny_n\mid x_i\in \mathfrak{a}, y_i\in \mathfrak{b}, n\geq 1\}.$$

:::

That $\mathfrak{a}\mathfrak{b}$ is a subgroup under addition in $A$ is obvious. On the other hand, for any element $x_1y_1+\cdots+x_ny_n$ of $\mathfrak{a}\mathfrak{b}$ and any element $x$ of $A$,

$$x(x_1y_1+\cdots+x_ny_n)=xx_1y_1+\cdots +xx_ny_n$$

and since $xx_i\in \mathfrak{a}$, we have $x(x_1y_1+\cdots+x_ny_n)\in \mathfrak{a}\mathfrak{b}$. A similar argument holds when multiplying by $x$ on the right, so we can verify that $\mathfrak{a}\mathfrak{b}$ is a two-sided ideal of $A$.

::: Proposition 2
With multiplication defined as above, the collection of two-sided ideals of $A$ forms a monoid with identity $A$ ([[Algebraic Structures] §Semigroups, Monoids, Groups, ⁋Definition 3](/en/math/algebraic_structures/groups#def3)). Moreover, the distributive laws

$$\mathfrak{a}(\mathfrak{b}+\mathfrak{c})=\mathfrak{a}\mathfrak{b}+\mathfrak{a}\mathfrak{c},\quad (\mathfrak{a}+\mathfrak{b})\mathfrak{c}=\mathfrak{a}\mathfrak{c}+\mathfrak{b}\mathfrak{c}$$

also hold.
:::

::: Proof
Let three two-sided ideals $\mathfrak{a},\mathfrak{b},\mathfrak{c}$ be given. Then any element of $(\mathfrak{a}\mathfrak{b})\mathfrak{c}$ can be written in the form

$$\left(\sum_{i=1}^{n_1} x_i^{(1)}y_i^{(1)}\right)z_1+\cdots+\left(\sum_{i=1}^{n_k}x_i^{(k)}y_i^{(k)}\right)z_k$$

and using the distributive law to expand everything and then grouping the rightmost two factors, we see that this element belongs to $\mathfrak{a}(\mathfrak{b}\mathfrak{c})$. The reverse inclusion can be proved in exactly the same way, so multiplication is associative. Also, for any two-sided ideal $\mathfrak{a}$, it is obvious that $A \mathfrak{a}=\mathfrak{a}A=\mathfrak{a}$.

Finally, for arbitrary $b_1+c_1,\ldots, b_n+c_n\in \mathfrak{b}+\mathfrak{c}$,

$$a_1(b_1+c_1)+\cdots +a_n(b_n+c_n)$$

can be expanded using the distributive law to easily show $\mathfrak{a}(\mathfrak{b}+\mathfrak{c})\subseteq \mathfrak{a}\mathfrak{b}+\mathfrak{a}\mathfrak{c}$. Conversely, for arbitrary

$$a_1b_1+\cdots +a_nb_n + a_1'c_1+\cdots +a_m'c_m\in \mathfrak{a}\mathfrak{b}+\mathfrak{a}\mathfrak{c}$$

since the $b_i$'s and $c_i$'s are all elements of $\mathfrak{b}+\mathfrak{c}$, the above element is an element of $\mathfrak{a}(\mathfrak{b}+\mathfrak{c})$. The right distributive law can be proved similarly.
:::

For any two two-sided ideals $\mathfrak{a},\mathfrak{b}$, the two inclusions

$$\mathfrak{a}\mathfrak{b}\subseteq \mathfrak{a}A\subseteq \mathfrak{a},\quad \mathfrak{a}\mathfrak{b}\subseteq A \mathfrak{b}\subseteq \mathfrak{b}$$

both hold, so $\mathfrak{a}\mathfrak{b}\subseteq \mathfrak{a}\cap \mathfrak{b}$ holds. In general equality need not hold.

::: Definition 3
Two two-sided ideals $\mathfrak{a},\mathfrak{b}$ of a ring $A$ are called *comaximal* if they satisfy $\mathfrak{a}+\mathfrak{b}=A$. Several ideals $\mathfrak{a}_1,\ldots,\mathfrak{a}_n$ are called *pairwise comaximal* if $\mathfrak{a}_i+\mathfrak{a}_j=A$ for all $i\ne j$.
:::

Here the condition $\mathfrak{a}+\mathfrak{b}=A$ is equivalent to the identity element $1$ being expressible in the form

$$1=u+v,\qquad\text{$u\in\mathfrak{a}$, $v\in\mathfrak{b}$}$$

which corresponds exactly to the existence of a Bézout identity $mu+nv=1$ for two coprime integers $m,n$ in number theory ([[Number Theory] §Euclidean Algorithm and Bézout's Identity, ⁋Theorem 3](/en/math/number_theory/euclidean_algorithm#thm3)). Thus in $\mathbb{Z}$, the ideals $m\mathbb{Z},n\mathbb{Z}$ of coprime integers $m,n$ are comaximal.

On the other hand, the equality $\mathfrak{a}\mathfrak{b}=\mathfrak{a}\cap\mathfrak{b}$, which does not hold in general, does hold when the two ideals are comaximal. The following result is what we need to show this.

::: Proposition 4
Let two-sided ideals $\mathfrak{a},\mathfrak{b}_1,\ldots, \mathfrak{b}_n$ of $A$ be given, and assume that $A=\mathfrak{a}+\mathfrak{b}_i$ holds for all $i$. Then

$$A=\mathfrak{a}+\mathfrak{b}_1\cdots \mathfrak{b}_n=\mathfrak{a}+(\mathfrak{b}_1\cap\cdots\cap \mathfrak{b}_n)$$

holds.
:::

::: Proof
Since $\mathfrak{b}_1\cdots \mathfrak{b}_n\subseteq \mathfrak{b}_1\cap \cdots\cap \mathfrak{b}_n$ anyway, it suffices to show the equality $A=\mathfrak{a}+\mathfrak{b}_1\cdots \mathfrak{b}_n$. Also, since the proof works inductively, it is enough to consider the case $n=2$. That is, assume $A=\mathfrak{a}+\mathfrak{b}_1=\mathfrak{a}+\mathfrak{b}_2$, and let us show $A=\mathfrak{a}+\mathfrak{b}_1 \mathfrak{b}_2$.

First, from $A=\mathfrak{a}+\mathfrak{b}_1=\mathfrak{a}+\mathfrak{b}_2$, we can choose $a,a'\in \mathfrak{a}, b_i\in \mathfrak{b}_i$ satisfying $1=a+b_1=a'+b_2$. Then

$$1=a'+b_2=a'+1b_2=a'+(a+b_1)b_2=(a'+ab_2)+b_1b_2\in \mathfrak{a}+\mathfrak{b}_1 \mathfrak{b}_2$$

holds.
:::

In the case of a commutative ring, we can use this to prove the following.

::: Proposition 5
Let the ideals $\mathfrak{b}_1,\ldots, \mathfrak{b}_n$ of a commutative ring $A$ be pairwise comaximal. That is, $\mathfrak{b}_i+\mathfrak{b}_j=A$ for $i\neq j$. Then

$$\mathfrak{b}_1\cap \cdots\cap \mathfrak{b}_n=\mathfrak{b}_1\cdots \mathfrak{b}_n$$

holds.
:::

::: Proof
We prove this by induction. Since $\mathfrak{b}_1\cdots\mathfrak{b}_n\subseteq \mathfrak{b}_1\cap\cdots\cap\mathfrak{b}_n$ always holds, we only need to show the reverse inclusion.

First let $n=2$ and $\mathfrak{b}_1+\mathfrak{b}_2=A$. Writing $1=u+v$ ($u\in\mathfrak{b}_1, v\in\mathfrak{b}_2$), for any $x\in\mathfrak{b}_1\cap\mathfrak{b}_2$, using the fact that $A$ is commutative,

$$x=x\cdot 1=x(u+v)=xu+xv\in \mathfrak{b}_2 \mathfrak{b}_1+\mathfrak{b}_1 \mathfrak{b}_2=\mathfrak{b}_1 \mathfrak{b}_2$$

holds. Therefore $\mathfrak{b}_1\cap\mathfrak{b}_2=\mathfrak{b}_1\mathfrak{b}_2$.

Now let $n>2$. It is obvious that the two ideals $\mathfrak{a}=\mathfrak{b}_n$ and $\mathfrak{b}_1,\ldots,\mathfrak{b}_{n-1}$ are pairwise comaximal, so applying [Proposition 4](#prop4) here gives

$$A=\mathfrak{b}_n+(\mathfrak{b}_1\cap\cdots\cap \mathfrak{b}_{n-1})$$

and by the induction hypothesis $\mathfrak{b}_1\cap\cdots\cap \mathfrak{b}_{n-1}=\mathfrak{b}_1\cdots \mathfrak{b}_{n-1}$. Now applying the $n=2$ result to the comaximal ideals $\mathfrak{b}_n$ and $\mathfrak{b}_1\cap\cdots\cap \mathfrak{b}_{n-1}$,

$$\mathfrak{b}_1\cap\cdots\cap \mathfrak{b}_n=(\mathfrak{b}_1\cap\cdots\cap \mathfrak{b}_{n-1})\cap \mathfrak{b}_n=(\mathfrak{b}_1\cap\cdots\cap \mathfrak{b}_{n-1})\mathfrak{b}_n=\mathfrak{b}_1\cdots \mathfrak{b}_n$$

as desired.
:::

## Chinese Remainder Theorem

Now we examine the main theorem of this post.

Let a ring $A$ and two-sided ideals $\mathfrak{a}_i$ of $A$ be given. Then the projections $\pi_i:A \rightarrow A/\mathfrak{a}_i$ to each quotient exist, and from these a ring homomorphism $\pi:A \rightarrow\prod A/\mathfrak{a}_i$ is defined. When this morphism becomes an isomorphism is the heart of the Chinese remainder theorem.

::: Proposition 6
Let a ring $A$ and pairwise comaximal two-sided ideals $\mathfrak{a}_1,\ldots, \mathfrak{a}_n$ of $A$ be given. Then the $\pi:A \rightarrow \prod_1^n A/\mathfrak{a}_i$ defined above is surjective, and the kernel of this map equals $\bigcap \mathfrak{a}_i$.
:::

::: Proof
That $\ker\pi=\bigcap_i \mathfrak{a}_i$ is almost obvious, so it suffices to show surjectivity. That is, for any element

$$(x_1+\mathfrak{a}_1,\ldots,x_n+\mathfrak{a}_n)\in\prod A/\mathfrak{a}_i$$

we must show that by choosing appropriate representatives, this lies in the image of $\pi$.

For this, it is enough to construct, for each index $i$, an element $e_i$ that acts as $1$ in the $i$-th place and $0$ in all other places:

$$e_i\equiv 1\pmod{\mathfrak{a}_i},\qquad e_i\equiv 0 \pmod{\mathfrak{a}_j}\quad(j\neq i)$$

and the condition guaranteeing this is the pairwise comaximal condition on the ideals. For fixed $i$, since $\mathfrak{a}_i+\mathfrak{a}_j=A$ for each $j\ne i$, we can choose elements $1=u_{ij}+v_{ij}$ ($u_{ij}\in\mathfrak{a}_i,\ v_{ij}\in\mathfrak{a}_j$). Now set

$$e_i=\prod_{j\ne i}v_{ij}.$$

Then first, for each $j\neq i$, since $e_i$ is the product of $v_{ij}\in \mathfrak{a}_j$ with other elements, it is obvious that $e_i\in \mathfrak{a}_j$. For the index $i$, since

$$v_{ij}=1-u_{ij}\equiv 1\pmod{\mathfrak{a}_i}$$

we have $e_i\equiv 1\pmod{\mathfrak{a}_i}$. Therefore setting $x=\sum_i x_ie_i$, we have $x_je_j\in \mathfrak{a}_i$ for each $j\neq i$, so $x\equiv x_ie_i\equiv x_i\pmod{\mathfrak{a}_i}$, which means $\pi(x)$ equals the given element.
:::

Thus, by the first isomorphism theorem, the following canonical isomorphism

$$A\Big/\left(\bigcap_{i=1}^n \mathfrak{a}_i\right)\cong \prod_{i=1}^n A/\mathfrak{a}_i$$

exists. If $A$ is commutative, then by [Proposition 5](#prop5) we can replace the intersection by a product, so

$$A/\mathfrak{a}_1\cdots \mathfrak{a}_n\cong\prod_{i=1}^n A/\mathfrak{a}_i$$

and in particular if $\bigcap \mathfrak{a}_i=0$ then we obtain the isomorphism $A\cong\prod A/\mathfrak{a}_i$.

The integer version mentioned in the introduction is the special case $A=\mathbb{Z}$. That is, for pairwise coprime $n_1,\ldots, n_r$, setting $\mathfrak{a}_i=n_i \mathbb{Z}$ and $n=n_1\cdots n_r$, the coprime condition becomes exactly the comaximal condition $\mathfrak{a}_i+\mathfrak{a}_j=\mathbb{Z}$, so the above proposition yields the isomorphism $\mathbb{Z}/n \mathbb{Z}\cong\prod \mathbb{Z}/n_i \mathbb{Z}$.

The isomorphism $A\cong\prod A/\mathfrak{a}_i$ obtained when $\bigcap\mathfrak{a}_i=0$ is a strong statement that the ring $A$ decomposes as a product of smaller rings. When $A$ is commutative, this condition is equivalent by [Proposition 5](#prop5) to $\mathfrak{a}_1\cdots\mathfrak{a}_n=0$.

## The Noncommutative Case

In [Proposition 5](#prop5), the commutativity assumption was used to guarantee that the intersection $\mathfrak{b}_1\cap\cdots\cap\mathfrak{b}_n$ collapses to a single product $\mathfrak{b}_1\cdots\mathfrak{b}_n$. Without this assumption, products in different orders can become different ideals, and the intersection is expressed as the symmetric sum of all such ordered products, with the following proposition giving the generalized version.

::: Proposition 7
Let two-sided ideals $\mathfrak{b}_1,\ldots, \mathfrak{b}_n$ of a ring $A$ be pairwise comaximal. Then

$$\mathfrak{b}_1\cap \cdots\cap \mathfrak{b}_n=\sum_{\sigma\in S_n} \mathfrak{b}_{\sigma(1)}\cdots \mathfrak{b}_{\sigma(n)}$$

holds. In particular, if $A$ is a commutative ring then all products in different orders coincide, so we recover [Proposition 5](#prop5).
:::

::: Proof
We prove this by induction, just as in [Proposition 5](#prop5). Since $\sum_{\sigma\in S_n}\mathfrak{b}_{\sigma(1)}\cdots\mathfrak{b}_{\sigma(n)}\subseteq\mathfrak{b}_1\cap\cdots\cap\mathfrak{b}_n$ always holds, we only need to show the reverse inclusion.

First let $n=2$. From the pairwise comaximal condition, choose elements $1=b_1+b_2$ ($b_i\in\mathfrak{b}_i$); then for any $x\in\mathfrak{b}_1\cap\mathfrak{b}_2$,

$$x=x\cdot 1=x(b_1+b_2)=xb_1+xb_2\in \mathfrak{b}_1\mathfrak{b}_2+\mathfrak{b}_2\mathfrak{b}_1$$

holds.

Now let $n>2$. Applying [Proposition 4](#prop4) to $\mathfrak{a}=\mathfrak{b}_n$ and $(\mathfrak{b}_1,\ldots,\mathfrak{b}_{n-1})$, we have $A=\mathfrak{b}_n+(\mathfrak{b}_1\cap\cdots\cap\mathfrak{b}_{n-1})$, so the two ideals $\mathfrak{b}_n$ and $\mathfrak{b}_1\cap\cdots\cap\mathfrak{b}_{n-1}$ are comaximal. Applying the $n=2$ result,

$$\mathfrak{b}_1\cap\cdots\cap\mathfrak{b}_n=(\mathfrak{b}_1\cap\cdots\cap\mathfrak{b}_{n-1})\mathfrak{b}_n+\mathfrak{b}_n(\mathfrak{b}_1\cap\cdots\cap\mathfrak{b}_{n-1})$$

holds. Substituting the induction hypothesis $\mathfrak{b}_1\cap\cdots\cap\mathfrak{b}_{n-1}=\sum_{\sigma\in S_{n-1}}\mathfrak{b}_{\sigma(1)}\cdots\mathfrak{b}_{\sigma(n-1)}$, the right-hand side becomes

$$\left(\sum_{\sigma\in S_{n-1}}\mathfrak{b}_{\sigma(1)}\cdots\mathfrak{b}_{\sigma(n-1)}\right)\mathfrak{b}_n+\mathfrak{b}_n\left(\sum_{\sigma\in S_{n-1}}\mathfrak{b}_{\sigma(1)}\cdots\mathfrak{b}_{\sigma(n-1)}\right)$$

and since each term on the right-hand side is contained in $\sum_{\sigma\in S_n}\mathfrak{b}_{\sigma(1)}\cdots\mathfrak{b}_{\sigma(n)}$, we obtain the desired reverse inclusion.
:::

Applying [Proposition 7](#prop7) to the kernel $\bigcap_i\mathfrak{a}_i$ in [Proposition 6](#prop6), the Chinese remainder theorem in the noncommutative case also holds in the form

$$A\Big/\left(\sum_{\sigma\in S_n}\mathfrak{a}_{\sigma(1)}\cdots\mathfrak{a}_{\sigma(n)}\right)\cong \prod_{i=1}^n A/\mathfrak{a}_i.$$

This essentially contains the same information as [Proposition 6](#prop6); the only difference is that in the commutative case this kernel collapses to a single product $\mathfrak{a}_1\cdots\mathfrak{a}_n$, simplifying the form.

---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  

---
