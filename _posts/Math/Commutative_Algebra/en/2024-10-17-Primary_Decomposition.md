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
translated_at: 2026-08-27T14:45:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-04T11:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
In this post, we assume that $A$ is Noetherian and that $M$ is a finitely generated $A$-module.

## Primary Submodules

::: Definition 1
In $M$, a submodule $N$ is a *primary submodule* if $\Ass(M/N)$ consists of only a single prime ideal. In this case, if $\Ass(M/N)=\{\mathfrak{p}\}$, we call $N$ a $\mathfrak{p}$-primary submodule. If $\Ass(M)$ consists of only a single prime ideal, we call $M$ a *coprimary submodule*.
:::

That is, if $M/N$ is a coprimary module, then $N$ is a primary submodule. Also, from [§Associated Primes, ⁋Lemma 5](/en/math/commutative_algebra/associated_primes#lem5){: data-lid="vg2nc" }, we know that any finite intersection of $\mathfrak{p}$-primary submodules is $\mathfrak{p}$-primary.

Now the following holds.

::: Proposition 2
For a ring $A$, a prime ideal $\mathfrak{p}$, and a non-$0$ $A$-module $M$, the following are all equivalent.

1. The $A$-module $M$ is a $\mathfrak{p}$-coprimary module.
2. $\mathfrak{p}$ is minimal among the prime ideals containing $\ann(M)$, and elements not in $\mathfrak{p}$ are not zero divisors on $M$.
3. For some $k$, $\mathfrak{p}^k$ annihilates $M$, and elements not in $\mathfrak{p}$ are not zero divisors on $M$.
:::
::: Proof
First, suppose the first condition holds. Then by definition, $\mathfrak{p}$ is the unique associated prime ideal of $M$. Now, by the first condition of [§Associated Primes, ⁋Theorem 7](/en/math/commutative_algebra/associated_primes#thm7){: data-lid="l2d21" }, $\mathfrak{p}$ must be minimal among the prime ideals containing $\ann(M)$, and by the second condition, elements outside $\mathfrak{p}$ are not zero divisors on $M$.

Now suppose the second condition holds. Since elements of $A\setminus \mathfrak{p}$ are not zero divisors on $M$, it suffices to prove the given claim in the localization $M_\mathfrak{p}$. That is, we may assume that $(A, \mathfrak{p})$ is a local ring, and now from the assumption that $\mathfrak{p}$ is minimal over $\ann(M)$ and [§Properties of Localization, ⁋Corollary 8](/en/math/commutative_algebra/properties_of_localization#cor8){: data-lid="z8jwb" }, we obtain $\sqrt{\ann(M)}=\mathfrak{p}$. But since $A$ is Noetherian, $\mathfrak{p}$ is finitely generated, and since a suitable power of each generator belongs to $\ann(M)$, choosing $k$ larger than the sum of all these exponents yields $\mathfrak{p}^k\subseteq \ann(M)$.

Finally, suppose the third condition holds. Then it is clear that $\mathfrak{p}$ is minimal among the prime ideals containing $\ann M$, and therefore, by the first condition of [§Associated Primes, ⁋Theorem 7](/en/math/commutative_algebra/associated_primes#thm7){: data-lid="kplxr" }, $\mathfrak{p}$ is an associated prime ideal of $M$. Moreover, since elements outside $\mathfrak{p}$ are all not zero divisors, we know again by the second condition of [§Associated Primes, ⁋Theorem 7](/en/math/commutative_algebra/associated_primes#thm7){: data-lid="j3wu6" } that any associated prime is always contained in $\mathfrak{p}$. That is, $\mathfrak{p}$ is the unique associated prime ideal of $M$.
:::

## Primary Decomposition

In this post, our goal is to show the following theorem.

::: Theorem 3 (Primary decomposition)
In $M$, every proper submodule $M'$ is an intersection of primary submodules. That is, for prime ideals $\mathfrak{p}_1,\ldots, \mathfrak{p}_n$ and $\mathfrak{p}_k$-primary submodules $M_k$, we can write $M'=\bigcap_{k=1}^n M_k$. We call this a *primary decomposition*, and then the following hold.

1. Every associated prime of $M/M'$ is one of the $\mathfrak{p}_k$.
2. If, in expressing $M'$, no $M_k$ is redundant, then the $\mathfrak{p}_i$ are precisely the associated primes of $M/M'$.
3. If there is no way to express $M'$ using fewer $M_k$, then the associated primes of $M/M'$ are precisely the $\mathfrak{p}_k$, one for each index. If moreover $\mathfrak{p}_i$ is minimal among the prime ideals containing the annihilator ideal of $M/M'$, then $M_i/M'$ equals the kernel of $M/M' \rightarrow (M/M')_{\mathfrak{p}_i}$, and hence $M_i$ is determined by $M'$ and $\mathfrak{p}_i$ alone.
4. Given a minimal primary decomposition, for any of $A$'s multiplicative subsets $S$, let $\mathfrak{p}_1,\ldots, \mathfrak{p}_m$ be the prime ideals that do not meet $S$. Then
    
    $$S^{-1}M'=\bigcap_{i=1}^m S^{-1}M_i$$

    is, over $S^{-1}A$, a minimal primary decomposition of $S^{-1}M'$.
:::

In particular, when $M=A$ and $M'=\mathfrak{a}$ is an ideal of $A$, in the third result of [Theorem 3](#thm3){: data-lid="m1mg4" }, those prime ideals containing $\mathfrak{a}$ that are minimal with respect to inclusion are called the *minimal prime ideals* of $\mathfrak{a}$; when $\mathfrak{a}=(0)$, we simply call them the minimal prime ideals of $A$.

To prove this, we first define the irreducible decomposition of a module.

::: Definition 4
For an $A$-module $M$, a proper submodule $N$ is *irreducible* if $N=N_1\cap N_2$ holds for no $N_1,N_2\supsetneq N$.
:::

Then the following holds.

::: Lemma 5 (Noether)
Every proper submodule of $M$ is an intersection of irreducible submodules.
:::
::: Proof
We argue by contradiction. Since $M$ is Noetherian, we can choose a maximal element among the proper submodules that are not intersections of irreducible submodules; call it $N$. Since $N$ is not an irreducible submodule, $N=N_1\cap N_2$ holds for some $N_1,N_2\supsetneq N$. Here, if $N_1=M$, then $N=N_2$, contradicting $N_2\supsetneq N$, and the case $N_2=M$ is similar; hence $N_1,N_2$ are both proper submodules. But by the maximality of $N$, $N_1,N_2$ are both intersections of irreducible submodules, and therefore so is $N$, which is a contradiction.
:::

From this, we see that in $M$, for any proper submodule $M'$, an *irreducible decomposition* of $M'$

$$M'=\bigcap_{k=1}^n M_k,\qquad \text{$M_k$ irreducible}$$

always exists.

::: Lemma 6
The irreducible decomposition above is a primary decomposition.
:::
::: Proof
For this, it suffices to show that any irreducible submodule $P$ is a primary submodule, which is equivalent to showing that $M/P$ is a coprimary submodule. First, since $P$ is a proper submodule, $M/P\neq 0$, and by the first result of [§Associated Primes, ⁋Theorem 7](/en/math/commutative_algebra/associated_primes#thm7){: data-lid="ff37b" }, $\Ass(M/P)$ is nonempty. Therefore, contrary to the conclusion, suppose that $M/P$ has two distinct associated primes $\mathfrak{p},\mathfrak{q}$. Then $M/P$ has submodules isomorphic to $A/\mathfrak{p}$ and $A/\mathfrak{q}$, respectively. Then by definition, the annihilator of any element of $A/\mathfrak{p}$ other than $0$ is $\mathfrak{p}$, and the annihilator of any element of $A/\mathfrak{q}$ other than $0$ is $\mathfrak{q}$, so they have only $0$ as a common element. That is, in $M/P$, the zero submodule $0$ is a reducible submodule. From this, in $M$, $P$ is a reducible submodule, which yields a contradiction.
:::

Therefore, every proper submodule of $M$ always has a primary decomposition. Now the remaining parts of [Theorem 3](#thm3){: data-lid="wdw5i" } must be proved. As in the proof of the preceding lemma, in proving them it suffices to prove them for $M/M'$, so without loss of generality we may assume $M'=0$.

::: Proof (Theorem 3)
First, to show the first result, suppose that for $M$, a primary decomposition of the zero submodule $0$

$$0=\bigcap_{k=1}^n M_k$$

is given. Then, since from generalizing the exact sequence of [\[Multilinear Algebra\] §Exact Sequences, ⁋Proposition 7](/en/math/multilinear_algebra/exact_sequences#prop7){: data-lid="alqlt" } we have

$$M\subseteq \bigoplus_{k=1}^n M/M_k$$

we know from [§Associated Primes, ⁋Lemma 5](/en/math/commutative_algebra/associated_primes#lem5){: data-lid="9djk7" } that any primes in $\Ass M$ are obtained from among the $\mathfrak{p}_k$.

Now let us show the second result. Then, in particular, for each $j$,

$$\bigcap_{k\neq j} M_k\neq 0$$

holds. Then, since $M_j\cap \bigcap_{k\neq j}M_k=0$,

$$\bigcap_{k\neq j} M_k=\left(\bigcap_{k\neq j} M_k\right)\bigg/\left(M_j\cap \bigcap_{k\neq j}M_k\right)\cong \left(\bigcap_{k\neq j} M_k + M_j\right)\bigg/M_j\subseteq M/M_j$$

so $\bigcap_{k\neq j} M_k$ is $\mathfrak{p}_j$-coprimary. From this, we obtain the desired result.

Now let us show the third result. In general, since an intersection of $\mathfrak{p}$-primary submodules is also $\mathfrak{p}$-primary, to satisfy the given condition the $\mathfrak{p}_k$ must all be distinct prime ideals. Now suppose that the $\mathfrak{p}_k$ are minimal among those containing the annihilator ideal. What we must show here is that $M_k$ is determined by $M$ and $\mathfrak{p}_k$ alone; since by [§Localization, ⁋Proposition 5](/en/math/commutative_algebra/localization#prop5){: data-lid="ezwzm" } the kernel of $\varepsilon: M \rightarrow M_{\mathfrak{p}_k}$ is the collection of elements for which $sx=0$ holds for some $s\in A\setminus \mathfrak{p}_k$, that is, of such $x$, it is determined by $M$ and $\mathfrak{p}_k$ alone, and therefore it suffices to show that the kernel of $\varepsilon$ is $M_k$.

Now consider the following commutative diagram:

{% diagram Math/Commutative_Algebra/Primary_Decomposition-1.svg width="11.73em" alt="injective" %}

Then, since the kernel of $M \rightarrow M/M_k$ is $M_k$, to show the desired claim it suffices to show that both $M_{\mathfrak{p}_k}\rightarrow (M/M_k)_{\mathfrak{p}_k}$ and $M/M_k \rightarrow (M/M_k)_{\mathfrak{p}_k}$ are injective. First, that $M/M_k \rightarrow (M/M_k)_{\mathfrak{p}_k}$ is injective is immediate from the fact that $M_k$ is $\mathfrak{p}_k$-primary. Then, as we observed at the very beginning,

$$M \rightarrow \bigoplus_{k=1}^n M/M_k$$

is injective, and therefore the localization of this map

$$M_{\mathfrak{p}_k} \rightarrow \left(\bigoplus_{k=1}^n M/M_k\right)_{\mathfrak{p}_k} $$

is also injective. Meanwhile, for each $j\neq k$, $M/M_j$ is $\mathfrak{p}_j$-coprimary, and by minimality $\mathfrak{p}_j$ cannot be contained in $\mathfrak{p}_k$, so $(M/M_j)_{\mathfrak{p}_k}=0$ holds; since the map thus obtained is precisely $M_{\mathfrak{p}_k}\rightarrow (M/M_k)_{\mathfrak{p}_k}$, we obtain the desired result.

Finally, let us show the fourth result. First, since localization is an exact functor ([§Properties of Localization, ⁋Proposition 2](/en/math/commutative_algebra/properties_of_localization#prop2){: data-lid="fktau" }), it commutes with finite intersections, and therefore we obtain $0=\bigcap_{k=1}^n S^{-1}M_k$. Now, following the notation of the statement, let $\mathfrak{p}_1,\ldots, \mathfrak{p}_m$ be the only prime ideals that do not meet $S$. If $\mathfrak{p}_j\cap S\neq\emptyset$, then since $M/M_j$ is $\mathfrak{p}_j$-coprimary, by the third condition of [Proposition 2](#prop2){: data-lid="c0xi4" }, for some $t$, $\mathfrak{p}_j^t$ annihilates $M/M_j$, and choosing $s\in \mathfrak{p}_j\cap S$, the element $s^t\in \mathfrak{p}_j^t$ also annihilates $M/M_j$, so again by [§Localization, ⁋Proposition 5](/en/math/commutative_algebra/localization#prop5){: data-lid="bv6d6" } we know that $S^{-1}(M/M_j)=0$, that is, $S^{-1}M_j=S^{-1}M$. In other words, these components play no role in the intersection above, so

$$0=\bigcap_{i=1}^m S^{-1}M_i$$

holds. Now, for each $i$ appearing here, $\Ass(M/M_i)=\{\mathfrak{p}_i\}$ and $\mathfrak{p}_i\cap S=\emptyset$, so by the third result of [§Associated Primes, ⁋Theorem 7](/en/math/commutative_algebra/associated_primes#thm7){: data-lid="ms995" }, $\Ass_{S^{-1}A}S^{-1}(M/M_i)=\{\mathfrak{p}_iS^{-1}A\}$, and thus $S^{-1}M_i$ is a $\mathfrak{p}_iS^{-1}A$-primary submodule.

Now let us show that this decomposition is minimal. By [§Localization, ⁋Proposition 8](/en/math/commutative_algebra/localization#prop8){: data-lid="u2w6f" }, since prime ideals not meeting $S$ in $A$ are in one-to-one correspondence with the prime ideals of $S^{-1}A$, the ideals $\mathfrak{p}_1S^{-1}A,\ldots, \mathfrak{p}_mS^{-1}A$ are $m$ distinct prime ideals, and by the first result of the same proposition, in $S^{-1}A$, any ideal $\mathfrak{b}$ is generated by the image of the preimage of $\mathfrak{b}$ in $A$. Now, from the fact that $A$ is Noetherian, $S^{-1}A$ is also Noetherian, and since the images of the generators of $M$ generate $S^{-1}M$, the module $S^{-1}M$ is a finitely generated $S^{-1}A$-module. Then, from the third result of [§Associated Primes, ⁋Theorem 7](/en/math/commutative_algebra/associated_primes#thm7){: data-lid="0ybta" } and the second result already proven, $\Ass_{S^{-1}A}S^{-1}M$ consists of precisely these $m$ prime ideals, and applying the first result over $S^{-1}A$, any primary decomposition of the zero submodule of $S^{-1}M$ must have all of them among its prime ideals, so it has at least $m$ components. That is, the decomposition above is minimal.
:::

## Primary Decomposition and Factorization

Meanwhile, the following theorem shows that primary decomposition generalizes the familiar notion of factorization.

::: Theorem 7
For a Noetherian domain $A$, the following hold.

1. Suppose $f\in A$ factors as $f=u p_1^{e_1}\cdots p_n^{e_n}$, where $u$ is a unit, $e_i\geq 1$, and the $p_i$ are prime elements such that the $(p_i)$ are distinct prime ideals. Then $(f)=\bigcap(p_i^{e_i})$ is a minimal primary decomposition of $(f)$.
2. $A$ is a UFD if and only if every prime ideal minimal over a principal ideal is principal.
:::
::: Proof
We first prove the first claim. To begin with, we check that $(p_i^{e_i})$ is $(p_i)$-primary for each $i$. Since it is clear that $(p_i)^{e_i}=(p_i^{e_i})$ annihilates $A/(p_i^{e_i})$, by the third condition of [Proposition 2](#prop2){: data-lid="z73ba" } it suffices to show that the elements outside $(p_i)$ are not zero divisors on $A/(p_i^{e_i})$. For this, we show by induction on $e_i$ that whenever $x\not\in (p_i)$ and $a\in A$ satisfy $xa\in (p_i^{e_i})$, then $a\in(p_i^{e_i})$. The case $e_i=0$ is trivial. If $e_i\geq 1$, then $xa\in(p_i^{e_i})\subseteq (p_i)$, and since $(p_i)$ is prime and $x\not\in(p_i)$, we have $a\in (p_i)$. Thus we can write $a=p_ib$, and setting $xa=p_i^{e_i}c$, we have $p_i(xb-p_i^{e_i-1}c)=0$; since $A$ is a domain and $p_i\neq 0$, this gives $xb=p_i^{e_i-1}c\in (p_i^{e_i-1})$. By the induction hypothesis $b\in (p_i^{e_i-1})$, and therefore $a=p_ib\in(p_i^{e_i})$.

We now show that $(f)=\bigcap_{i=1}^n (p_i^{e_i})$. Since $f\in (p_i^{e_i})$ for each $i$, one inclusion is trivial. Conversely, let $g\in\bigcap_{i=1}^n (p_i^{e_i})$; we show $g\in (p_1^{e_1}\cdots p_j^{e_j})$ by induction on $j$. The case $j=0$ is trivial. Now assume we can write $g=p_1^{e_1}\cdots p_j^{e_j}h$. First, we check that $p_i\not\in (p_k)$ for any two distinct indices $i\neq k$: if $p_i=cp_k$, then since the prime element $p_i$ is irreducible ([\[Ring Theory\] §Integral Domains, ⁋Proposition 12](/en/math/ring_theory/integral_domains#prop12){: data-lid="69ht2" }) and $p_k$ is not a unit, $c$ must be a unit, giving $(p_i)=(p_k)$ and contradicting the assumption that the $(p_i)$ are distinct. Therefore, since $(p_{j+1})$ is prime, $p_1^{e_1}\cdots p_j^{e_j}\not\in (p_{j+1})$, and since $p_1^{e_1}\cdots p_j^{e_j}h=g\in (p_{j+1}^{e_{j+1}})$, what we showed in the previous paragraph gives $h\in (p_{j+1}^{e_{j+1}})$. That is, $g\in (p_1^{e_1}\cdots p_{j+1}^{e_{j+1}})$, and by induction we obtain $g\in (p_1^{e_1}\cdots p_n^{e_n})=(f)$. The last equality holds because $u$ is a unit.

To show that this decomposition is minimal, we first check that no component can be omitted. For each $i$, the product $\prod_{j\neq i} p_j^{e_j}$ lies in $\bigcap_{j\neq i}(p_j^{e_j})$ but not in $(p_i^{e_i})$: if it did, then in particular $\prod_{j\neq i}p_j^{e_j}\in (p_i)$, and since $(p_i)$ is prime, we would have $p_j\in (p_i)$ for some $j\neq i$, contradicting what we checked in the previous paragraph. Therefore, by the second part of [Theorem 3](#thm3){: data-lid="mph6k" }, $\Ass(A/(f))=\{(p_1),\ldots,(p_n)\}$, and in particular these are $n$ distinct prime ideals. Meanwhile, by the first part of [Theorem 3](#thm3){: data-lid="8400g" }, every primary decomposition of $(f)$ must have all the elements of $\Ass(A/(f))$ among its primes, so it must have at least $n$ components. That is, the decomposition above is minimal.

We now prove the second claim. First, suppose $A$ is a UFD, and let a principal ideal $(f)$ and a prime ideal $\mathfrak{p}$ minimal among those containing $(f)$ be given. If $f=0$, then since $A$ is a domain, $(0)$ is prime, and hence $\mathfrak{p}=(0)$ is principal. If $f$ is a unit, there is no prime ideal containing $(f)=A$, so there is nothing to prove. Now suppose $f$ is a nonzero non-unit, and factor it as $f=up_1^{e_1}\cdots p_n^{e_n}$. Then $f\in\mathfrak{p}$, and since $\mathfrak{p}$ is prime, $p_i\in \mathfrak{p}$ for some $i$. That is, $(f)\subseteq (p_i)\subseteq \mathfrak{p}$, and since $(p_i)$ is prime, the minimality of $\mathfrak{p}$ forces $\mathfrak{p}=(p_i)$, which is principal.

Conversely, suppose that every prime ideal minimal over a principal ideal is principal. First, since $A$ is Noetherian, every nonzero non-unit element is expressed as a product of irreducible elements. Supposing otherwise, the collection of principal ideals $(a)$ formed by nonzero non-unit elements $a$ that cannot be expressed as products of irreducible elements is nonempty, so by the Noetherian condition we can choose a maximal element $(a)$ of this collection. Then $a$ is not irreducible, so we can write $a=bc$ for non-units $b,c$; if $(a)=(b)$, then $b=ad$ for some $d$ and $a=adc$, and since $A$ is a domain this makes $c$ a unit, a contradiction; hence $(a)\subsetneq (b)$, and for the same reason $(a)\subsetneq(c)$. Then by the maximality of $(a)$, $b,c$ are both expressed as products of irreducible elements, and therefore so is $a=bc$, a contradiction.

Next, we show that every irreducible element $p$ is prime. Since $A$ is Noetherian, there exists a prime ideal minimal among those containing $(p)$; letting it be $\mathfrak{p}$, by assumption $\mathfrak{p}=(q)$ is principal. From $p\in (q)$ we can write $p=qc$, and since $p$ is irreducible and $q$ is a non-unit, $c$ must be a unit; therefore $(p)=(q)=\mathfrak{p}$ is a prime ideal. That is, $p$ is a prime element.

Finally, we show the uniqueness of factorization. Suppose $up_1\cdots p_m=vq_1\cdots q_k$ are products of irreducible elements and $u,v$ are units; we use induction on $m$. If $m=0$, then the left-hand side is a unit, so we must have $k=0$. If $m\geq 1$, then since $p_m$ is prime, $p_m\mid q_j$ for some $j$, and since $q_j$ is irreducible and $p_m$ is a non-unit, there exists a unit $w$ such that $q_j=wp_m$. Since $A$ is a domain, canceling $p_m$ from both sides and applying the induction hypothesis yields that, after a suitable rearrangement, each $p_i$ and $q_i$ are associates. Therefore $A$ is a UFD. ([\[Ring Theory\] §Integral Domains, ⁋Definition 16](/en/math/ring_theory/integral_domains#def16){: data-lid="oay8k" })
:::

---

**References**

**[Eis]** David Eisenbud. *Commutative Algebra: with a view toward algebraic geometry*. Springer, 1995.

---
