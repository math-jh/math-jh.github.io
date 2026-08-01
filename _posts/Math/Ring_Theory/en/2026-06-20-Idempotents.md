---
title: "Central Idempotents and Ring Decomposition"
description: "We define idempotents and complete sets of orthogonal idempotents, then prove that central idempotents correspond bijectively to product decompositions of a ring. Finally, we connect this result to the Chinese remainder theorem for general rings."
excerpt: "Central idempotents, ring product decomposition, and the Chinese remainder theorem"

categories: [Math / Ring Theory]
permalink: /en/math/ring_theory/idempotents
sidebar: 
    nav: "ring_theory-en"

date: 2026-06-20
weight: 6
translated_at: 2026-08-01T12:15:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-08-01T12:15:04+00:00
---
Previously, in [§Chinese Remainder Theorem, ⁋Proposition 6](/en/math/ring_theory/chinese_remainder_theorem#prop6), we saw that pairwise comaximal two-sided ideals decompose a given ring into a product of quotient rings. In that decomposition, the elements selecting each factor were those whose $i$th component is $1$ and the rest are $0$, and such elements are characterized as *idempotents* lying in the center of the ring.

In this post, we formally define these idempotents, prove that a complete set of central orthogonal idempotents is in bijection with a direct product decomposition of the ring, and then examine how the general Chinese remainder theorem is recovered from this.

## Idempotents

We begin with the following definition.

::: Definition 1
An element $e\in A$ of a ring $A$ satisfying $e^2=e$ is called an *idempotent*. Two idempotents $e,f$ are said to be *orthogonal* if $ef=fe=0$. Moreover, an idempotent $e$ belonging to the center $Z(A)$ of $A$ is called a *central idempotent*.
:::

Any ring always has the two idempotents $0$ and $1$, and these are always central. We call them *trivial* idempotents. Given an idempotent $e$, the element $1-e$ is also an idempotent, because

$$(1-e)^2=1-2e+e^2=1-2e+e=1-e.$$

Moreover,

$$e(1-e)=e-e^2=0,\qquad (1-e)e=e-e^2=0$$

so $e$ and $1-e$ are orthogonal. We will treat $e$ paired with its *complementary idempotent* $1-e$, and $e$ being central is equivalent to $1-e$ being central.

::: Example 2
By a simple calculation, one can check that the idempotents of the ring $A=\mathbb{Z}/6\mathbb{Z}$ are $0,1,3,4$; here $3$ and $4$ are complementary, as are $0$ and $1$. Moreover, since $A$ is commutative, these four idempotents are automatically central. On the other hand, in $\mathbb{Z}/4\mathbb{Z}$ the only elements satisfying $x^2=x$ are $0,1$, so this ring has only trivial idempotents.
:::

## Complete set of orthogonal idempotents

We now introduce the following concept in order to handle several idempotents at once.

::: Definition 3
Idempotents $e_1,\ldots, e_n$ in a ring $A$ are called a *complete set of orthogonal idempotents* if they satisfy the two conditions

$$e_1+\cdots+e_n=1,\qquad e_ie_j=0\quad\text{for $i\neq j$}.$$

If each $e_i$ is central, we call this a *central* complete set.
:::

The simplest complete set is $\{1\}$ when $n=1$, and in [Example 2](#ex2) the sets $\{0,1\}$ and $\{3,4\}$ in $\mathbb{Z}/6\mathbb{Z}$ are examples of central complete sets with $n=2$. More generally, given a single idempotent $e$, the set $\{e,1-e\}$ is always a complete set of orthogonal idempotents. Thus a complete set can be viewed as a generalization of splitting an idempotent into several pieces. Let us now see how this splitting decomposes the ring.

::: Proposition 4
Let a ring $A$ and a complete set of orthogonal idempotents $\{e_1,\ldots, e_n\}$ in $A$ be given. Then the decomposition as left $A$-modules

$$A=Ae_1\oplus\cdots\oplus Ae_n$$

holds. Moreover, if each $e_i$ is central, then each $Ae_i$ is a two-sided ideal of $A$.
:::
::: Proof
For any $x\in A$, from $e_1+\cdots+e_n=1$ we have

$$x=x\cdot 1=xe_1+\cdots+xe_n$$

and since each $xe_i\in Ae_i$, we get $A=Ae_1+\cdots+Ae_n$. Hence what remains to be shown is that this sum is a direct sum.

To this end, suppose some element is expressed in two ways. That is, let $a_1e_1+\cdots+a_ne_n=0$. Then multiplying this equation on the right by $e_j$, since $e_ie_j=0$ for $i\neq j$ and $e_j^2=e_j$, we obtain

$$0=(a_1e_1+\cdots+a_ne_n)e_j=\sum_{i=1}^n a_i(e_ie_j)=a_je_j.$$

Thus the $j$th component $a_je_j$ is $0$, and since this holds for every $j$, the given sum is a direct sum.

Now to show the last part, assume each $e_i$ is central. That $Ae_i$ is a left ideal is trivial by definition, so it suffices to show it is a right ideal. For this we need to check that for any $ae_i\in Ae_i$ and $x\in A$, we have $(ae_i)x\in Ae_i$; but since $e_i$ is central,

$$(ae_i)x=a(e_ix)=a(xe_i)=(ax)e_i\in Ae_i$$

so $Ae_i$ is a two-sided ideal.
:::

When each $e_i$ is central, $Ae_i$ itself carries the structure of a ring. In particular $Ae_i$ always has an identity element, namely $e_i$. Indeed, for any $ae_i\in Ae_i$, since $e_i$ is idempotent and central,

$$e_i\cdot(ae_i)=(e_ia)e_i=(ae_i)e_i=ae_i^2=ae_i$$

and likewise $(ae_i)\cdot e_i=ae_i$.

## Central idempotents and product decomposition

From the argument above we know that each $Ae_i$ is a ring with identity $e_i$ and that $A$ is their direct sum. The following theorem shows that this direct sum is in fact a direct product of rings, and moreover that such a decomposition is in bijection with a central complete set.

::: Theorem 5
For a ring $A$, there is a bijection between the following two data:

1. A central complete set of orthogonal idempotents $\{e_1,\ldots, e_n\}$ in $A$.
2. A decomposition of $A$ as a direct product of $n$ two-sided ideals $A=\mathfrak{a}_1\times\cdots\times\mathfrak{a}_n$.

This correspondence is given by $\mathfrak{a}_i=Ae_i$.
:::
::: Proof
First, suppose the first datum is given. Setting $\mathfrak{a}_i:=Ae_i$ as indicated, [Proposition 4](#prop4) implies that each $\mathfrak{a}_i$ is a two-sided ideal and $A=\mathfrak{a}_1\oplus\cdots\oplus\mathfrak{a}_n$ is a direct sum of left modules. It remains to show that this direct sum is also a direct product of rings. Consider the morphism

$$\varphi:A\rightarrow \prod_{i=1}^n Ae_i;\quad x\mapsto (xe_1,\ldots, xe_n).$$

This preserves addition, and since the $e_i$ are central and orthogonal,

$$\varphi(x)\varphi(y)=(xe_1\cdot ye_1,\ldots, xe_n\cdot ye_n)=(xye_1,\ldots, xye_n)=\varphi(xy)$$

so it also preserves multiplication. Moreover $\varphi(1)=(e_1,\ldots, e_n)$ and each $e_i$ is the identity of $Ae_i$, so $\varphi$ is a ring homomorphism. That this is an isomorphism follows because the direct sum decomposition of [Proposition 4](#prop4) is an isomorphism.

Conversely, suppose the second datum is given. A direct product decomposition yields in particular a direct sum $A=\mathfrak{a}_1\oplus\cdots\oplus\mathfrak{a}_n$ with respect to addition, so the identity element can be written uniquely in this decomposition as

$$1=e_1+\cdots+e_n,\qquad e_i\in\mathfrak{a}_i.$$

For any $x\in\mathfrak{a}_j$, since $\mathfrak{a}_i$ is an ideal we have $xe_i\in\mathfrak{a}_i$, and from this we obtain the unique decomposition

$$x=x\cdot 1=xe_1+\cdots+xe_n.$$

But the decomposition of $x\in\mathfrak{a}_j$ is the one whose $j$th component is $x$ and the rest are $0$, so by this uniqueness we have $xe_j=x$ and $xe_i=0$ for $i\neq j$. In particular, substituting $x=e_j$ gives $e_j^2=e_j$ and $e_je_i=0$ for all $i\neq j$. Thus $\{e_1,\ldots, e_n\}$ is a complete set of orthogonal idempotents. What remains to be shown is only centrality. Writing any $y\in A$ as

$$y=y_1+\cdots+y_n,\qquad y_i\in\mathfrak{a}_i$$

we have from above that $y_ie_j$ is $y_i$ when $i=j$ and $0$ otherwise, and the same holds for $e_jy_i$, so $ye_j=y_j=e_jy$. Hence each $e_j$ commutes with every $y$ and is central.

Finally, let us verify that these two constructions are mutual inverses. Starting from the first datum and setting $\mathfrak{a}_i=Ae_i$, since $1=e_1+\cdots+e_n$ is the unique expression of $1$ in this decomposition, the second construction returns the idempotents $e_i$ again. Conversely, starting from the second datum, from $e_i\in\mathfrak{a}_i$ we have $Ae_i\subseteq\mathfrak{a}_i$, and the equation $x=xe_i$ obtained above for any $x\in\mathfrak{a}_i$ gives the reverse inclusion, so $\mathfrak{a}_i=Ae_i$. Therefore this correspondence is bijective.
:::

By [Theorem 5](#thm5), a ring having no nontrivial central idempotents is equivalent to it not decomposing as a product of two nonzero rings. Such a ring is called *connected* or *indecomposable*. For instance, a division ring $A$ is always indecomposable. If $A$ decomposed as a product of two nonzero rings, then the elements $(1,0)$ and $(0,1)$ corresponding to the identity elements of the factors would both be nonzero while their product is $0$, so $A$ would have zero divisors.

The next example shows in particular what happens when the centrality condition is dropped. In this case [Theorem 5](#thm5) does not apply as is, but the decomposition as modules is still guaranteed by [Proposition 4](#prop4).

::: Example 6
For a ring $A$, consider the $n\times n$ matrix ring $\Mat_n(A)$. Let $E_{ij}$ be the matrix unit whose $(i,j)$ entry is $1$ and the rest are $0$; then the diagonal entries $E_{11},\ldots, E_{nn}$ satisfy

$$E_{ii}^2=E_{ii},\qquad E_{ii}E_{jj}=0\ (i\neq j),\qquad E_{11}+\cdots+E_{nn}=I$$

so they form a complete set of orthogonal idempotents. Hence by [Proposition 4](#prop4) we obtain the left module decomposition

$$\Mat_n(A)=\Mat_n(A)E_{11}\oplus\cdots\oplus \Mat_n(A)E_{nn},$$

where $\Mat_n(A)E_{ii}$ is the set of matrices whose only nonzero entries are in the $i$th column.

What must be noted is that for $n\geq 2$, the $E_{ii}$ are not central. For example, when $n=2$,

$$E_{11}E_{12}=E_{12}\neq 0=E_{12}E_{11}$$

so $E_{11}$ does not commute with $E_{12}$. Therefore this decomposition does not give a direct product decomposition of the ring.

In fact, for any ring $A$ one can compute the center of $\Mat_n(A)$ directly. If a matrix $M$ commutes with all matrix units, we know that

$$(E_{kl}M)_{i,j}=\delta_{ik}M_{lj},\qquad (ME_{kl})_{i,j}=M_{ik}\delta_{lj}$$

must be equal. Now consider the case $i=k$. Then

$$M_{lj}=M_{kk}\delta_{lj}$$

so if $j\neq l$ then $M_{lj}=0$, and where $j=l$ we have $M_{ll}=M_{kk}$, hence $M$ must be of the form $cI$. On the other hand, such an $M$ must commute not only with the matrix units but also with matrices of the form $aI$, so this coefficient $c$ must belong to the center $Z(A)$ of $A$. Conversely, if $c\in Z(A)$ then for any $M$ we have $(cIM)_{i,j}=cM_{i,j}=M_{i,j}c=(McI)_{i,j}$, so $cI$ commutes with all matrices, and therefore

$$Z(\Mat_n(A))=\{cI\mid c\in Z(A)\}.$$

Now since $(cI)^2=c^2I$, the central idempotents of $\Mat_n(A)$ are the $cI$ for $c\in Z(A)$ with $c^2=c$, which is exactly the embedding of the central idempotents of $A$ into $\Mat_n(A)$. In particular, if $A$ is a division ring then the only central idempotents of $A$ are $0,1$, so the only central idempotents of $\Mat_n(A)$ are $0$ and $I$.
:::

On the other hand, whether an idempotent is central depends on which ring we view it inside. Partition $n=n_1+\cdots+n_r$ and consider the subring of block-diagonal matrices with blocks of sizes $n_1\times n_1$, $n_2\times n_2$, and so on along the diagonal:

$$B=\left\{\diag(M_1,\ldots, M_r)\mid M_k\in \Mat_{n_k}(A)\right\}\cong\prod_{k=1}^r \Mat_{n_k}(A).$$

Inside this ring, the element $P_k$ which places the identity matrix only in the $k$th block is central, and by the correspondence of [Theorem 5](#thm5) it yields this direct product decomposition. However, we have already verified that this $P_k$ is not central in the example ring $\Mat_n(A)$ above.

## Connection with the Chinese Remainder Theorem

Meanwhile, even before [Theorem 5](#thm5), we had already seen a method of decomposing a given ring as a direct product. ([§Chinese Remainder Theorem, ⁋Proposition 6](/en/math/ring_theory/chinese_remainder_theorem#prop6)) These two results are not independent, and in the remainder of this post we examine the relationship between them. The key point is that the pairwise comaximal condition pulls the natural idempotents of the product ring back into $A$, and in the following theorem $\pi:A\rightarrow\prod_{i=1}^n A/\mathfrak{a}_i$ denotes the morphism induced by the projections onto each quotient

$$x\mapsto (x+\mathfrak{a}_1,\ldots, x+\mathfrak{a}_n).$$

::: Theorem 7
Let a ring $A$ and its two-sided ideals $\mathfrak{a}_1,\ldots, \mathfrak{a}_n$ be given. The following are all equivalent.

1. $\pi:A\rightarrow\prod_{i=1}^n A/\mathfrak{a}_i$ is an isomorphism.
2. For all $i\neq j$, $\mathfrak{a}_i+\mathfrak{a}_j=A$ and $\bigcap_i\mathfrak{a}_i=0$.
3. There exists a central complete set of orthogonal idempotents $\{e_1,\ldots, e_n\}$ in $A$ such that $\mathfrak{a}_i=A(1-e_i)$ for all $i$.
:::
::: Proof
First assume the first condition and show the second. If $\pi$ is an isomorphism then $\bigcap_i\mathfrak{a}_i=\ker\pi=0$. Also, for a fixed pair $i\neq j$, let $e_i\in A$ be a preimage of the element whose $i$th component is $1+\mathfrak{a}_i$ and whose remaining components are all $0$. Then from the $j$th component we have $e_i\in\mathfrak{a}_j$ and from the $i$th component $1-e_i\in\mathfrak{a}_i$, so

$$1=(1-e_i)+e_i\in\mathfrak{a}_i+\mathfrak{a}_j$$

and hence $\mathfrak{a}_i+\mathfrak{a}_j=A$.

Now assume the second condition and show the third. From the pairwise comaximal condition and $\bigcap_i\mathfrak{a}_i=\ker\pi=0$, [§Chinese Remainder Theorem, ⁋Proposition 6](/en/math/ring_theory/chinese_remainder_theorem#prop6) implies that $\pi$ is an isomorphism. Consider the elements

$$\bar e_i=(0,\ldots, 0,1,0,\ldots, 0)$$

in the product ring $\prod_i A/\mathfrak{a}_i$ whose $i$th component is $1+\mathfrak{a}_i$ and the rest are $0$; by componentwise calculation one can see that these form a central complete set of orthogonal idempotents, and since $\pi$ is a ring isomorphism, $e_i:=\pi^{-1}(\bar e_i)$ is also a central complete set of orthogonal idempotents in $A$. It remains to show the equality $\mathfrak{a}_i=A(1-e_i)$; since the $i$th component of $\bar e_i$ is $1+\mathfrak{a}_i$, we have $1-e_i\in\mathfrak{a}_i$, and since $\mathfrak{a}_i$ is an ideal, $A(1-e_i)\subseteq\mathfrak{a}_i$ is trivial. Conversely, let $a\in\mathfrak{a}_i$; then the $i$th component of $\pi(a)$ is $0$ and $\bar e_i$ is $0$ in every component except the $i$th, so $\pi(ae_i)=\pi(a)\bar e_i=0$, and since $\pi$ is injective, $ae_i=0$. Therefore

$$a=ae_i+a(1-e_i)=a(1-e_i)\in A(1-e_i).$$

Finally, assume the third condition and show the first. By [Theorem 5](#thm5), a central complete set $\{e_1,\ldots, e_n\}$ yields a direct product decomposition $A\cong\prod_i Ae_i$ given by the ring isomorphism $x\mapsto (xe_1,\ldots, xe_n)$. On the other hand, for each $i$ the morphism

$$A\rightarrow Ae_i;\quad a\mapsto ae_i$$

is clearly surjective, and if $ae_i=0$ then $a=a(1-e_i)$ while conversely $a(1-e_i)e_i=0$, so its kernel is $A(1-e_i)=\mathfrak{a}_i$. Hence $A/\mathfrak{a}_i\cong Ae_i$, and since this isomorphism is given by $x+\mathfrak{a}_i\mapsto xe_i$, composing with the above direct product decomposition yields exactly $\pi$. Therefore $\pi$ is an isomorphism.
:::

Let us apply this to the most familiar case, the ring of integers.

::: Example 8
Let the prime factorization of $n\geq 2$ be $n=p_1^{a_1}\cdots p_r^{a_r}$ (distinct primes $p_k$), and consider the ideals $\mathfrak{a}_k=p_k^{a_k}\mathbb{Z}/n\mathbb{Z}$ of $A=\mathbb{Z}/n\mathbb{Z}$. In $\mathbb{Z}$, the ideals $p_k^{a_k}\mathbb{Z}$ are pairwise comaximal and their intersection is $n\mathbb{Z}$, so inside $A$ the $\mathfrak{a}_k$ are pairwise comaximal and $\bigcap_k\mathfrak{a}_k=0$. Hence [Theorem 7](#thm7) applies, yielding the classical Chinese remainder theorem

$$\mathbb{Z}/n\mathbb{Z}\cong\prod_{k=1}^r\mathbb{Z}/p_k^{a_k}\mathbb{Z}$$

together with the central complete set of orthogonal idempotents in $\mathbb{Z}/n\mathbb{Z}$ corresponding to this decomposition.

Concretely, for $n=6=2\cdot 3$ we have $\mathbb{Z}/6\mathbb{Z}\cong\mathbb{Z}/2\mathbb{Z}\times\mathbb{Z}/3\mathbb{Z}$. Pulling back the two idempotents $\bar e_1=(1,0)$, $\bar e_2=(0,1)$ of the product ring $\mathbb{Z}/2\mathbb{Z}\times\mathbb{Z}/3\mathbb{Z}$ along the isomorphism, the element of $\mathbb{Z}/6\mathbb{Z}$ corresponding to $(1,0)$ is $3$, and the one corresponding to $(0,1)$ is $4$. Indeed $3\equiv 1\ (\mathrm{mod}\ 2)$, $3\equiv 0\ (\mathrm{mod}\ 3)$ and $4\equiv 0\ (\mathrm{mod}\ 2)$, $4\equiv 1\ (\mathrm{mod}\ 3)$. This matches exactly the idempotents $3,4$ found by hand in [Example 2](#ex2).

On the other hand, for a prime $p$ and $a\geq 1$, the ring $\mathbb{Z}/p^a\mathbb{Z}$ has no idempotents other than $0,1$. This is because $x^2\equiv x\ (\mathrm{mod}\ p^a)$ is the same as $x(x-1)\equiv 0\ (\mathrm{mod}\ p^a)$, and since $x$ and $x-1$ are coprime, $p^a$ must divide exactly one of them. Hence each factor in the above decomposition is indecomposable in the sense of [Theorem 5](#thm5), and the direct product decomposition according to prime factorization is the finest decomposition that cannot be split any further. That $\mathbb{Z}/4\mathbb{Z}$ had only trivial idempotents in [Example 2](#ex2) is the special case of this.
:::

---

**References**

**[AM]** M. F. Atiyah and I. G. Macdonald, *Introduction to commutative algebra*, Addison–Wesley, 1969.  
**[DF]** D. S. Dummit and R. M. Foote, *Abstract algebra*, 3rd ed., Wiley, 2004.  
**[Lam]** T. Y. Lam, *A first course in noncommutative rings*, 2nd ed., Graduate Texts in Mathematics 131, Springer, 2001.
