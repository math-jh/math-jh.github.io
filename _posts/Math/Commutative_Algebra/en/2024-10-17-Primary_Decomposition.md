---
title: "Primary Decomposition"
description: "Covers primary decomposition of finitely generated modules over Noetherian rings in commutative algebra. Explains the definitions and properties of primary submodules and coprimary submodules with proofs."
excerpt: "Primary decomposition and uniqueness for modules over Noetherian rings"

categories: [Math / Commutative Algebra]
permalink: /en/math/commutative_algebra/primary_decomposition
sidebar: 
    nav: "commutative_algebra-en"

date: 2024-10-17
weight: 7
translated_at: 2026-08-27T13:15:05+00:00
translation_source: kimi-cli
---
In this post, we assume that $A$ is Noetherian and that $M$ is a finitely generated $A$-module.

## Primary Submodules

::: Definition 1
A submodule $N$ of $M$ is a *primary submodule* if $\Ass(M/N)$ consists of a single prime ideal. In this case, if $\Ass(M/N)=\{\mathfrak{p}\}$, we call $N$ a $\mathfrak{p}$-primary submodule. If $\Ass(M)$ consists of a single prime ideal, we call $M$ a *coprimary module*.
:::

That is, if $M/N$ is a coprimary module, then $N$ is a primary submodule. Also, by [§Associated Primes of Ideals, ⁋Lemma 5](/en/math/commutative_algebra/associated_primes#lem5), we know that any finite intersection of $\mathfrak{p}$-primary submodules is $\mathfrak{p}$-primary.

We now have the following.

::: Proposition 2
For a ring $A$, a prime ideal $\mathfrak{p}$, and a nonzero $A$-module $M$, the following are all equivalent.

1. The $A$-module $M$ is a $\mathfrak{p}$-coprimary module.
2. $\mathfrak{p}$ is minimal among the prime ideals containing $\ann(M)$, and no element outside $\mathfrak{p}$ is a zero divisor on $M$.
3. For some $k$, the power $\mathfrak{p}^k$ annihilates $M$, and no element outside $\mathfrak{p}$ is a zero divisor on $M$.
:::
::: Proof
First, suppose the first condition holds. Then by definition, $\mathfrak{p}$ is the unique associated prime ideal of $M$. By the first condition of [§Associated Primes of Ideals, ⁋Theorem 7](/en/math/commutative_algebra/associated_primes#thm7), $\mathfrak{p}$ must be minimal among the prime ideals containing $\ann(M)$, and by the second condition, the elements outside $\mathfrak{p}$ are not zero divisors on $M$.

Now suppose the second condition holds. Since the elements of $A\setminus \mathfrak{p}$ are not zero divisors on $M$, it suffices to prove the given claim in the localization $M_\mathfrak{p}$. That is, we may assume that $(A, \mathfrak{p})$ is a local ring, and now from the assumption that $\mathfrak{p}$ is minimal over $\ann(M)$ together with [§Properties of Localization, ⁋Corollary 8](/en/math/commutative_algebra/properties_of_localization#cor8), we obtain $\sqrt{\ann(M)}=\mathfrak{p}$. But since $A$ is Noetherian, $\mathfrak{p}$ is finitely generated, and since a suitable power of each generator lies in $\ann(M)$, taking $k$ larger than the sum of all these exponents gives $\mathfrak{p}^k\subseteq \ann(M)$.

Finally, if the third condition holds, it is obvious that $\mathfrak{p}$ is minimal among the prime ideals containing $\ann M$, so by the first condition of [§Associated Primes of Ideals, ⁋Theorem 7](/en/math/commutative_algebra/associated_primes#thm7), $\mathfrak{p}$ is an associated prime ideal of $M$. Moreover, since every element outside $\mathfrak{p}$ is not a zero divisor, by the second condition of [§Associated Primes of Ideals, ⁋Theorem 7](/en/math/commutative_algebra/associated_primes#thm7) we know that every associated prime is always contained in $\mathfrak{p}$. That is, $\mathfrak{p}$ is the unique associated prime ideal of $M$.
:::

## Primary Decomposition

The goal of this post is to prove the following theorem.

::: Theorem 3 (Primary decomposition)
Every proper submodule $M'$ of $M$ is an intersection of primary submodules. That is, for prime ideals $\mathfrak{p}_1,\ldots, \mathfrak{p}_n$ and $\mathfrak{p}_k$-primary submodules $M_k$, we can write $M'=\bigcap_{k=1}^n M_k$. We call this a *primary decomposition*, and then the following hold.

1. Every associated prime of $M/M'$ is one of the $\mathfrak{p}_k$.
2. If, when expressing $M'$, none of the $M_k$ is redundant, then the $\mathfrak{p}_i$ are exactly the associated primes of $M/M'$.
3. If there is no way of expressing $M'$ using fewer $M_k$, then the associated primes of $M/M'$ correspond to exactly one $\mathfrak{p}_k$ per index. If moreover $\mathfrak{p}_i$ is minimal among the prime ideals containing the annihilator ideal of $M/M'$, then $M_i/M'$ equals the kernel of $M/M' \rightarrow (M/M')_{\mathfrak{p}_i}$, and hence $M_i$ is determined solely by $M'$ and $\mathfrak{p}_i$.
4. Given a minimal primary decomposition, for any multiplicative subset $S$ of $A$, suppose that $\mathfrak{p}_1,\ldots, \mathfrak{p}_m$ are the prime ideals not meeting $S$. Then

    $$S^{-1}M'=\bigcap_{i=1}^m S^{-1}M_i$$

    is a minimal primary decomposition of $S^{-1}M'$ over $S^{-1}A$.
:::

In particular, when $M=A$ and $M'=\mathfrak a$ is an ideal of $A$, we call those prime ideals containing $\mathfrak a$ that are minimal with respect to inclusion, which appear in the third result of [Theorem 3](#thm3), the *minimal prime ideals* of $\mathfrak a$, and when $\mathfrak a=(0)$ we simply call them the minimal prime ideals of $A$.

To prove this, we first define the irreducible decomposition of a module.

::: Definition 4
A proper submodule $N$ of an $A$-module $M$ is *irreducible* if there do not exist $N_1,N_2\supsetneq N$ with $N=N_1\cap N_2$.
:::

Then the following holds.

::: Lemma 5 (Noether)
Every proper submodule of $M$ is expressed as an intersection of irreducible submodules.
:::
::: Proof
Let us use contradiction. Since $M$ is Noetherian, we can choose a maximal one among the proper submodules that are not expressed as an intersection of irreducible submodules. Call it $N$. Then since $N$ is not an irreducible submodule, there exist $N_1,N_2\supsetneq N$ such that $N=N_1\cap N_2$. If $N_1=M$ here, then $N=N_2$, contradicting $N_2\supsetneq N$, and likewise for the case $N_2=M$, so $N_1$ and $N_2$ are both proper submodules. But by the maximality of $N$, both $N_1$ and $N_2$ are expressed as intersections of irreducible submodules, and hence so is $N$, a contradiction.
:::

From this we know that for every proper submodule $M'$ of $M$, an *irreducible decomposition* of $M'$

$$M'=\bigcap_{k=1}^n M_k,\qquad \text{$M_k$ irreducible}$$

always exists.

::: Lemma 6
The irreducible decomposition above is a primary decomposition.
:::
::: Proof
For this it suffices to show that every irreducible submodule $P$ is a primary submodule, which is the same as showing that $M/P$ is a coprimary submodule. First, since $P$ is a proper submodule, $M/P\neq 0$, and by the first result of [§Associated Primes of Ideals, ⁋Theorem 7](/en/math/commutative_algebra/associated_primes#thm7), $\Ass(M/P)$ is nonempty. So, contrary to the conclusion, suppose $M/P$ has two distinct associated primes $\mathfrak{p},\mathfrak{q}$. Then $M/P$ has submodules isomorphic to $A/\mathfrak{p}$ and $A/\mathfrak{q}$, respectively. Now by definition, the annihilator of every nonzero element of $A/\mathfrak{p}$ is $\mathfrak{p}$, and the annihilator of every nonzero element of $A/\mathfrak{q}$ is $\mathfrak{q}$, so these two have only $0$ as a common element. That is, the zero submodule $0$ of $M/P$ is a reducible submodule. From this it follows that $P$ is a reducible submodule of $M$, yielding a contradiction.
:::

Therefore every proper submodule of $M$ always admits a primary decomposition. We must now prove the remaining parts of [Theorem 3](#thm3). As in the proof of the preceding lemma, when proving them it suffices to prove them for $M/M'$, so without loss of generality we may assume $M'=0$.

::: Proof (Theorem 3)
First, to show the first result, suppose a primary decomposition

$$0=\bigcap_{k=1}^n M_k$$

of the zero submodule $0$ of $M$ is given. Then from the generalization of the exact sequence in [\[Multilinear Algebra\] §Exact Sequences, ⁋Proposition 7](/en/math/multilinear_algebra/exact_sequences#prop7),

$$M\subseteq \bigoplus_{k=1}^n M/M_k,$$

so by [§Associated Primes of Ideals, ⁋Lemma 5](/en/math/commutative_algebra/associated_primes#lem5) we know that every prime in $\Ass M$ arises among the $\mathfrak{p}_k$.

Now let us show the second result. In particular, for each $j$,

$$\bigcap_{k\neq j} M_k\neq 0$$

holds. Since $M_j\cap \bigcap_{k\neq j}M_k=0$,

$$\bigcap_{k\neq j} M_k=\left(\bigcap_{k\neq j} M_k\right)\bigg/\left(M_j\cap \bigcap_{k\neq j}M_k\right)\cong \left(\bigcap_{k\neq j} M_k + M_j\right)\bigg/M_j\subseteq M/M_j,$$

so $\bigcap_{k\neq j} M_k$ is $\mathfrak{p}_j$-coprimary. From this we obtain the desired result.

Now let us show the third result. In general, an intersection of $\mathfrak{p}$-primary submodules is again $\mathfrak{p}$-primary, so to satisfy the given condition the $\mathfrak{p}_k$ must all be distinct prime ideals. Now suppose the $\mathfrak{p}_k$ are minimal among those containing the annihilator ideal. What we must show is that $M_k$ is determined solely by $M$ and $\mathfrak{p}_k$; by [§Localization, ⁋Proposition 5](/en/math/commutative_algebra/localization#prop5), the kernel of $\varepsilon: M \rightarrow M_{\mathfrak{p}_k}$ is the collection of those $x$ for which there exists $s\in A\setminus \mathfrak{p}_k$ with $sx=0$, so it is determined solely by $M$ and $\mathfrak{p}_k$, and therefore it suffices to show that the kernel of $\varepsilon$ is $M_k$.

Now consider the following commutative diagram

{% diagram Math/Commutative_Algebra/Primary_Decomposition-1.svg width="11.73em" alt="injective" %}

Since the kernel of $M \rightarrow M/M_k$ is $M_k$, to prove the desired claim it suffices to show that both $M_{\mathfrak{p}_k}\rightarrow (M/M_k)_{\mathfrak{p}_k}$ and $M/M_k \rightarrow (M/M_k)_{\mathfrak{p}_k}$ are injective. First, that $M/M_k \rightarrow (M/M_k)_{\mathfrak{p}_k}$ is injective is immediate from the fact that $M_k$ is $\mathfrak{p}_k$-primary. Now, as we examined at the very beginning,

$$M \rightarrow \bigoplus_{k=1}^n M/M_k$$

is injective, and hence its localization

$$M_{\mathfrak{p}_k} \rightarrow \left(\bigoplus_{k=1}^n M/M_k\right)_{\mathfrak{p}_k} $$

is also injective. Meanwhile, for each $j\neq k$, $M/M_j$ is $\mathfrak{p}_j$-coprimary, and by minimality $\mathfrak{p}_j$ must not be contained in $\mathfrak{p}_k$, so $(M/M_j)_{\mathfrak{p}_k}=0$ holds, and the resulting map is exactly $M_{\mathfrak{p}_k}\rightarrow (M/M_k)_{\mathfrak{p}_k}$, giving the desired result.

Finally, let us show the fourth result. First, since localization is an exact functor ([§Properties of Localization, ⁋Proposition 2](/en/math/commutative_algebra/properties_of_localization#prop2)), it commutes with finite intersections, so we obtain $0=\bigcap_{k=1}^n S^{-1}M_k$. Now, following the notation in the statement, suppose that only $\mathfrak{p}_1,\ldots, \mathfrak{p}_m$ are the prime ideals not meeting $S$. If $\mathfrak{p}_j\cap S\neq\emptyset$, then since $M/M_j$ is $\mathfrak{p}_j$-coprimary, by the third condition of [Proposition 2](#prop2) some $\mathfrak{p}_j^t$ annihilates $M/M_j$, and choosing $s\in \mathfrak{p}_j\cap S$, the element $s^t\in \mathfrak{p}_j^t$ also annihilates $M/M_j$, so again by [§Localization, ⁋Proposition 5](/en/math/commutative_algebra/localization#prop5) we know that $S^{-1}(M/M_j)=0$, i.e. $S^{-1}M_j=S^{-1}M$. That is, these components play no role in the intersection above, so

$$0=\bigcap_{i=1}^m S^{-1}M_i.$$

Now, for each $i$ appearing here, $\Ass(M/M_i)=\{\mathfrak{p}_i\}$ and $\mathfrak{p}_i\cap S=\emptyset$, so by the third result of [§Associated Primes of Ideals, ⁋Theorem 7](/en/math/commutative_algebra/associated_primes#thm7), $\Ass_{S^{-1}A}S^{-1}(M/M_i)=\{\mathfrak{p}_iS^{-1}A\}$, and hence $S^{-1}M_i$ is a $\mathfrak{p}_iS^{-1}A$-primary submodule.

Now let us show that this decomposition is minimal. By [§Localization, ⁋Proposition 8](/en/math/commutative_algebra/localization#prop8), the prime ideals of $A$ not meeting $S$ are in one-to-one correspondence with the prime ideals of $S^{-1}A$, so $\mathfrak{p}_1S^{-1}A,\ldots, \mathfrak{p}_mS^{-1}A$ are $m$ distinct prime ideals, and by the first result of the same proposition, every ideal $\mathfrak{b}$ of $S^{-1}A$ is generated by the image of the preimage of $\mathfrak{b}$ in $A$. Now, since $A$ is Noetherian, $S^{-1}A$ is also Noetherian, and since the images of the generators of $M$ generate $S^{-1}M$, the module $S^{-1}M$ is a finitely generated $S^{-1}A$-module. Then by the third result of [§Associated Primes of Ideals, ⁋Theorem 7](/en/math/commutative_algebra/associated_primes#thm7) and the second result already shown, $\Ass_{S^{-1}A}S^{-1}M$ consists of exactly these $m$ prime ideals, and applying the first result over $S^{-1}A$, any primary decomposition of the zero submodule of $S^{-1}M$ must have all of these among its prime ideals, hence must have at least $m$ components. That is, the decomposition above is minimal.
:::

## Primary Decomposition and Factorization

Meanwhile, the following theorem shows that primary decomposition generalizes the notion of factorization that we already knew.

::: Theorem 7
For a Noetherian domain $A$, the following hold.

1. Suppose $f\in A$ factors as $f=u p_1^{e_1}\cdots p_n^{e_n}$. Here $u$ is a unit, $e_i\geq 1$, and the $p_i$ are prime elements such that the $(p_i)$ are distinct prime ideals. Then $(f)=\bigcap(p_i^{e_i})$ is a minimal primary decomposition of $(f)$.
2. $A$ being a UFD is equivalent to all minimal prime ideals over principal ideals being principal.
:::
::: Proof
First let us prove the first claim. To begin with, we check that for each $i$, $(p_i^{e_i})$ is $(p_i)$-primary. Since it is clear that $(p_i)^{e_i}=(p_i^{e_i})$ annihilates $A/(p_i^{e_i})$, by the third condition of [Proposition 2](#prop2) it suffices to show that the elements outside $(p_i)$ are not zero divisors on $A/(p_i^{e_i})$. For this, we show by induction on $e_i$ that whenever $x\not\in (p_i)$ and $a\in A$ satisfy $xa\in (p_i^{e_i})$, then $a\in(p_i^{e_i})$. The case $e_i=0$ is trivial. If $e_i\geq 1$, then $xa\in(p_i^{e_i})\subseteq (p_i)$, and since $(p_i)$ is prime and $x\not\in(p_i)$, we have $a\in (p_i)$. That is, we can write $a=p_ib$, and writing $xa=p_i^{e_i}c$, we have $p_i(xb-p_i^{e_i-1}c)=0$, but since $A$ is a domain and $p_i\neq 0$, we get $xb=p_i^{e_i-1}c\in (p_i^{e_i-1})$. By the induction hypothesis $b\in (p_i^{e_i-1})$, and therefore $a=p_ib\in(p_i^{e_i})$.

We now show that $(f)=\bigcap_{i=1}^n (p_i^{e_i})$. Since $f\in (p_i^{e_i})$ for each $i$, one inclusion is trivial. Conversely, let $g\in\bigcap_{i=1}^n (p_i^{e_i})$, and let us show $g\in (p_1^{e_1}\cdots p_j^{e_j})$ by induction on $j$. The case $j=0$ is trivial. Now assume we can write $g=p_1^{e_1}\cdots p_j^{e_j}h$. First, we check that for two distinct indices $i\neq k$, $p_i\not\in (p_k)$: if $p_i=cp_k$, then since $p_i$ is a prime element it is irreducible ([\[Ring Theory\] §Integral Domains, ⁋Proposition 12](/en/math/ring_theory/integral_domains#prop12)), and since $p_k$ is not a unit, $c$ must be a unit, giving $(p_i)=(p_k)$, which contradicts the assumption that the $(p_i)$ are distinct. Therefore, since $(p_{j+1})$ is prime, $p_1^{e_1}\cdots p_j^{e_j}\not\in (p_{j+1})$, and since $p_1^{e_1}\cdots p_j^{e_j}h=g\in (p_{j+1}^{e_{j+1}})$, by what was shown in the previous paragraph $h\in (p_{j+1}^{e_{j+1}})$. That is, $g\in (p_1^{e_1}\cdots p_{j+1}^{e_{j+1}})$, and by induction we obtain $g\in (p_1^{e_1}\cdots p_n^{e_n})=(f)$. The last equality holds because $u$ is a unit.

To show that this decomposition is minimal, let us first check that no component can be omitted. For each $i$, the product $\prod_{j\neq i} p_j^{e_j}$ lies in $\bigcap_{j\neq i}(p_j^{e_j})$ but not in $(p_i^{e_i})$. For if it did, then in particular $\prod_{j\neq i}p_j^{e_j}\in (p_i)$, and since $(p_i)$ is prime, $p_j\in (p_i)$ for some $j\neq i$, contradicting what was checked in the previous paragraph. Therefore, by the second result of [Theorem 3](#thm3), $\Ass(A/(f))=\{(p_1),\ldots,(p_n)\}$, and in particular these are $n$ distinct prime ideals. Meanwhile, by the first result of [Theorem 3](#thm3), every primary decomposition of $(f)$ must have all the elements of $\Ass(A/(f))$ among its primes, so it must have at least $n$ components. That is, the decomposition above is minimal.

Now let us prove the second claim. First, suppose $A$ is a UFD, and let a principal ideal $(f)$ and a prime ideal $\mathfrak{p}$ minimal among those containing $(f)$ be given. If $f=0$, then since $A$ is a domain, $(0)$ is prime, and hence $\mathfrak{p}=(0)$ is principal. If $f$ is a unit, there is no prime ideal containing $(f)=A$, so there is nothing to consider. Now suppose $f$ is nonzero and a non-unit, and factor it as $f=up_1^{e_1}\cdots p_n^{e_n}$. Then $f\in\mathfrak{p}$ and since $\mathfrak{p}$ is prime, $p_i\in \mathfrak{p}$ for some $i$. That is, $(f)\subseteq (p_i)\subseteq \mathfrak{p}$, and since $(p_i)$ is prime, by the minimality of $\mathfrak{p}$ we have $\mathfrak{p}=(p_i)$, which is principal.

Conversely, suppose that all prime ideals minimal over principal ideals are principal. First, since $A$ is Noetherian, every nonzero, non-unit element is expressed as a product of irreducible elements. For if not, then the collection of principal ideals $(a)$ generated by nonzero, non-unit elements $a$ not expressible as products of irreducible elements is nonempty, so by the Noetherian condition we can choose a maximal element $(a)$ of this collection. Then $a$ is not irreducible, so we can write $a=bc$ for non-units $b,c$; if $(a)=(b)$, then $b=ad$ for some $d$ and $a=adc$, and since $A$ is a domain this makes $c$ a unit, a contradiction, so $(a)\subsetneq (b)$, and for the same reason $(a)\subsetneq(c)$. Then by the maximality of $(a)$, both $b$ and $c$ are expressed as products of irreducible elements, and hence so is $a=bc$, a contradiction.

Next, let us show that every irreducible element $p$ is prime. Since $A$ is Noetherian, there exists a prime ideal minimal among those containing $(p)$; calling it $\mathfrak{p}$, by assumption $\mathfrak{p}=(q)$ is principal. Then from $p\in (q)$ we can write $p=qc$, and since $p$ is irreducible and $q$ is a non-unit, $c$ is a unit, and therefore $(p)=(q)=\mathfrak{p}$ is a prime ideal. That is, $p$ is a prime element.

Finally, let us show uniqueness of factorization. Suppose $up_1\cdots p_m=vq_1\cdots q_k$ are products of irreducible elements with $u,v$ units; we use induction on $m$. If $m=0$, then the left-hand side is a unit, so we must have $k=0$. If $m\geq 1$, then since $p_m$ is prime, $p_m\mid q_j$ for some $j$, and since $q_j$ is irreducible and $p_m$ is a non-unit, there exists a unit $w$ such that $q_j=wp_m$. Then, since $A$ is a domain, we can cancel $p_m$ from both sides and apply the induction hypothesis to conclude that, after a suitable rearrangement, each $p_i$ and $q_i$ are associates. Therefore $A$ is a UFD. ([\[Ring Theory\] §Integral Domains, ⁋Definition 16](/en/math/ring_theory/integral_domains#def16))
:::

---

**References**

**[Eis]** David Eisenbud. *Commutative Algebra: with a view toward algebraic geometry*. Springer, 1995.

---
