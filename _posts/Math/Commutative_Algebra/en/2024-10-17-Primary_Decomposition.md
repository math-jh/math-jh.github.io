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
last_polished_at: 2026-08-27T14:45:05+00:00
---
In this post, we assume that $A$ is Noetherian and that $M$ is a finitely generated $A$-module.

## Primary Submodules

::: Definition 1
A submodule $N$ of $M$ is a *primary submodule* if $\Ass(M/N)$ consists of a single prime ideal. In this case, if $\Ass(M/N)=\{\mathfrak{p}\}$, we call $N$ a $\mathfrak{p}$-primary submodule. If $\Ass(M)$ consists of a single prime ideal, we call $M$ a *coprimary module*.
:::

In other words, if $M/N$ is a coprimary module, then $N$ is a primary submodule. Also, by [§Associated Primes, ⁋Lemma 5](/en/math/commutative_algebra/associated_primes#lem5), any finite intersection of $\mathfrak{p}$-primary submodules is again $\mathfrak{p}$-primary.

We now have the following.

::: Proposition 2
For a ring $A$, a prime ideal $\mathfrak{p}$, and a nonzero $A$-module $M$, the following are all equivalent.

1. The $A$-module $M$ is a $\mathfrak{p}$-coprimary module.
2. $\mathfrak{p}$ is minimal among the prime ideals containing $\ann(M)$, and no element outside $\mathfrak{p}$ is a zero divisor on $M$.
3. For some $k$, the power $\mathfrak{p}^k$ annihilates $M$, and no element outside $\mathfrak{p}$ is a zero divisor on $M$.
:::
::: Proof
First, suppose the first condition holds. Then by definition, $\mathfrak{p}$ is the unique associated prime ideal of $M$. By the first condition of [§Associated Primes, ⁋Theorem 7](/en/math/commutative_algebra/associated_primes#thm7), $\mathfrak{p}$ must be minimal among the prime ideals containing $\ann(M)$, and by the second condition, the elements outside $\mathfrak{p}$ are not zero divisors on $M$.

Now suppose the second condition holds. Since the elements of $A\setminus \mathfrak{p}$ are not zero divisors on $M$, it suffices to prove the claim after passing to the localization $M_\mathfrak{p}$. That is, we may assume that $(A, \mathfrak{p})$ is a local ring; then the assumption that $\mathfrak{p}$ is minimal over $\ann(M)$, together with [§Properties of Localization, ⁋Corollary 8](/en/math/commutative_algebra/properties_of_localization#cor8), gives $\sqrt{\ann(M)}=\mathfrak{p}$. But since $A$ is Noetherian, $\mathfrak{p}$ is finitely generated, and since a suitable power of each generator lies in $\ann(M)$, taking $k$ larger than the sum of all these exponents yields $\mathfrak{p}^k\subseteq \ann(M)$.

Finally, if the third condition holds, it is clear that $\mathfrak{p}$ is minimal among the prime ideals containing $\ann M$, so by the first condition of [§Associated Primes, ⁋Theorem 7](/en/math/commutative_algebra/associated_primes#thm7), $\mathfrak{p}$ is an associated prime ideal of $M$. Moreover, since no element outside $\mathfrak{p}$ is a zero divisor, the second condition of [§Associated Primes, ⁋Theorem 7](/en/math/commutative_algebra/associated_primes#thm7) tells us that every associated prime of $M$ is contained in $\mathfrak{p}$. Hence $\mathfrak{p}$ is the unique associated prime ideal of $M$.
:::

## Primary Decomposition

The goal of this post is to prove the following theorem.

::: Theorem 3 (Primary decomposition)
Every proper submodule $M'$ of $M$ is an intersection of primary submodules. That is, for prime ideals $\mathfrak{p}_1,\ldots, \mathfrak{p}_n$ and $\mathfrak{p}_k$-primary submodules $M_k$, we can write $M'=\bigcap_{k=1}^n M_k$. We call this a *primary decomposition*, and the following hold.

1. Every associated prime of $M/M'$ is one of the $\mathfrak{p}_k$.
2. If no $M_k$ is redundant in this expression for $M'$, then the $\mathfrak{p}_i$ are exactly the associated primes of $M/M'$.
3. If $M'$ cannot be expressed using fewer of the $M_k$, then the associated primes of $M/M'$ are exactly the $\mathfrak{p}_k$, one for each index. If moreover $\mathfrak{p}_i$ is minimal among the prime ideals containing the annihilator ideal of $M/M'$, then $M_i/M'$ equals the kernel of $M/M' \rightarrow (M/M')_{\mathfrak{p}_i}$, and hence $M_i$ is determined by $M'$ and $\mathfrak{p}_i$ alone.
4. Given a minimal primary decomposition, for any multiplicative subset $S$ of $A$, let $\mathfrak{p}_1,\ldots, \mathfrak{p}_m$ be the prime ideals that do not meet $S$. Then

    $$S^{-1}M'=\bigcap_{i=1}^m S^{-1}M_i$$

    is a minimal primary decomposition of $S^{-1}M'$ over $S^{-1}A$.
:::

In particular, when $M=A$ and $M'=\mathfrak a$ is an ideal of $A$, the prime ideals containing $\mathfrak a$ that are minimal with respect to inclusion, as in the third part of [Theorem 3](#thm3), are called the *minimal prime ideals* of $\mathfrak a$; when $\mathfrak a=(0)$, we simply call them the minimal prime ideals of $A$.

To prove this, we first define the irreducible decomposition of a module.

::: Definition 4
A proper submodule $N$ of an $A$-module $M$ is *irreducible* if there do not exist $N_1,N_2\supsetneq N$ with $N=N_1\cap N_2$.
:::

Then the following holds.

::: Lemma 5 (Noether)
Every proper submodule of $M$ is an intersection of irreducible submodules.
:::
::: Proof
We argue by contradiction. Since $M$ is Noetherian, we may choose a maximal element among the proper submodules that are not intersections of irreducible submodules; call it $N$. Since $N$ is not an irreducible submodule, there exist $N_1,N_2\supsetneq N$ such that $N=N_1\cap N_2$. If $N_1=M$ here, then $N=N_2$, contradicting $N_2\supsetneq N$, and the case $N_2=M$ is similar; hence $N_1$ and $N_2$ are both proper submodules. But by the maximality of $N$, both $N_1$ and $N_2$ are intersections of irreducible submodules, and therefore so is $N$ — a contradiction.
:::

It follows that for every proper submodule $M'$ of $M$, an *irreducible decomposition* of $M'$

$$M'=\bigcap_{k=1}^n M_k,\qquad \text{$M_k$ irreducible}$$

always exists.

::: Lemma 6
The irreducible decomposition above is a primary decomposition.
:::
::: Proof
For this it suffices to show that every irreducible submodule $P$ is a primary submodule, which amounts to showing that $M/P$ is a coprimary module. First, since $P$ is a proper submodule, $M/P\neq 0$, and by the first part of [§Associated Primes, ⁋Theorem 7](/en/math/commutative_algebra/associated_primes#thm7), $\Ass(M/P)$ is nonempty. Toward a contradiction, suppose that $M/P$ has two distinct associated primes $\mathfrak{p},\mathfrak{q}$. Then $M/P$ has submodules isomorphic to $A/\mathfrak{p}$ and $A/\mathfrak{q}$, respectively. By definition, the annihilator of every nonzero element of $A/\mathfrak{p}$ is $\mathfrak{p}$, and the annihilator of every nonzero element of $A/\mathfrak{q}$ is $\mathfrak{q}$, so these two submodules have only $0$ as a common element. That is, the zero submodule $0$ of $M/P$ is a reducible submodule, from which it follows that $P$ is a reducible submodule of $M$ — a contradiction.
:::

Thus every proper submodule of $M$ admits a primary decomposition. It remains to prove the other parts of [Theorem 3](#thm3). As in the proof of the preceding lemma, it suffices to prove them for $M/M'$, so without loss of generality we may assume $M'=0$.

::: Proof (Theorem 3)
First, to show the first part, suppose we are given a primary decomposition

$$0=\bigcap_{k=1}^n M_k$$

of the zero submodule $0$ of $M$. Then, generalizing the exact sequence of [\[Multilinear Algebra\] §Exact Sequences, ⁋Proposition 7](/en/math/multilinear_algebra/exact_sequences#prop7), we have

$$M\subseteq \bigoplus_{k=1}^n M/M_k,$$

so by [§Associated Primes, ⁋Lemma 5](/en/math/commutative_algebra/associated_primes#lem5), every prime in $\Ass M$ arises among the $\mathfrak{p}_k$.

Next, let us show the second part. The hypothesis gives, for each $j$,

$$\bigcap_{k\neq j} M_k\neq 0.$$

Since $M_j\cap \bigcap_{k\neq j}M_k=0$,

$$\bigcap_{k\neq j} M_k=\left(\bigcap_{k\neq j} M_k\right)\bigg/\left(M_j\cap \bigcap_{k\neq j}M_k\right)\cong \left(\bigcap_{k\neq j} M_k + M_j\right)\bigg/M_j\subseteq M/M_j,$$

so $\bigcap_{k\neq j} M_k$ is $\mathfrak{p}_j$-coprimary. The desired result follows.

Now let us show the third part. Since an intersection of $\mathfrak{p}$-primary submodules is again $\mathfrak{p}$-primary, the given condition forces the $\mathfrak{p}_k$ to all be distinct prime ideals. Now suppose $\mathfrak{p}_k$ is minimal among the prime ideals containing the annihilator ideal. What we must show is that $M_k$ is determined by $M$ and $\mathfrak{p}_k$ alone; by [§Localization, ⁋Proposition 5](/en/math/commutative_algebra/localization#prop5), the kernel of $\varepsilon: M \rightarrow M_{\mathfrak{p}_k}$ consists of those $x$ for which there exists $s\in A\setminus \mathfrak{p}_k$ with $sx=0$, so it is determined by $M$ and $\mathfrak{p}_k$ alone. It therefore suffices to show that the kernel of $\varepsilon$ is $M_k$.

Consider the commutative diagram

{% diagram Math/Commutative_Algebra/Primary_Decomposition-1.svg width="11.73em" alt="injective" %}

Since the kernel of $M \rightarrow M/M_k$ is $M_k$, proving the claim reduces to showing that both $M_{\mathfrak{p}_k}\rightarrow (M/M_k)_{\mathfrak{p}_k}$ and $M/M_k \rightarrow (M/M_k)_{\mathfrak{p}_k}$ are injective. First, the injectivity of $M/M_k \rightarrow (M/M_k)_{\mathfrak{p}_k}$ is immediate from the fact that $M_k$ is $\mathfrak{p}_k$-primary. Next, as we saw at the very beginning,

$$M \rightarrow \bigoplus_{k=1}^n M/M_k$$

is injective, and hence its localization

$$M_{\mathfrak{p}_k} \rightarrow \left(\bigoplus_{k=1}^n M/M_k\right)_{\mathfrak{p}_k} $$

is also injective. Meanwhile, for each $j\neq k$, the module $M/M_j$ is $\mathfrak{p}_j$-coprimary, and by minimality $\mathfrak{p}_j$ is not contained in $\mathfrak{p}_k$, so $(M/M_j)_{\mathfrak{p}_k}=0$; the map thus obtained is exactly $M_{\mathfrak{p}_k}\rightarrow (M/M_k)_{\mathfrak{p}_k}$, which gives the desired result.

Finally, let us show the fourth part. Since localization is an exact functor ([§Properties of Localization, ⁋Proposition 2](/en/math/commutative_algebra/properties_of_localization#prop2)), it commutes with finite intersections, and we obtain $0=\bigcap_{k=1}^n S^{-1}M_k$. Following the notation of the statement, let $\mathfrak{p}_1,\ldots, \mathfrak{p}_m$ be the prime ideals that do not meet $S$. If $\mathfrak{p}_j\cap S\neq\emptyset$, then since $M/M_j$ is $\mathfrak{p}_j$-coprimary, the third condition of [Proposition 2](#prop2) shows that $\mathfrak{p}_j^t$ annihilates $M/M_j$ for some $t$; choosing $s\in \mathfrak{p}_j\cap S$, the element $s^t\in \mathfrak{p}_j^t$ also annihilates $M/M_j$, so again by [§Localization, ⁋Proposition 5](/en/math/commutative_algebra/localization#prop5) we have $S^{-1}(M/M_j)=0$, i.e. $S^{-1}M_j=S^{-1}M$. In other words, these components play no role in the intersection above, so

$$0=\bigcap_{i=1}^m S^{-1}M_i.$$

Now, for each $i$ appearing here, $\Ass(M/M_i)=\{\mathfrak{p}_i\}$ and $\mathfrak{p}_i\cap S=\emptyset$, so by the third part of [§Associated Primes, ⁋Theorem 7](/en/math/commutative_algebra/associated_primes#thm7), $\Ass_{S^{-1}A}S^{-1}(M/M_i)=\{\mathfrak{p}_iS^{-1}A\}$; hence $S^{-1}M_i$ is a $\mathfrak{p}_iS^{-1}A$-primary submodule.

It remains to show that this decomposition is minimal. By [§Localization, ⁋Proposition 8](/en/math/commutative_algebra/localization#prop8), the prime ideals of $A$ not meeting $S$ are in one-to-one correspondence with the prime ideals of $S^{-1}A$, so $\mathfrak{p}_1S^{-1}A,\ldots, \mathfrak{p}_mS^{-1}A$ are $m$ distinct prime ideals; moreover, by the first part of the same proposition, every ideal $\mathfrak{b}$ of $S^{-1}A$ is generated by the image of the preimage of $\mathfrak{b}$ in $A$. Since $A$ is Noetherian, $S^{-1}A$ is also Noetherian, and since the images of the generators of $M$ generate $S^{-1}M$, the module $S^{-1}M$ is a finitely generated $S^{-1}A$-module. Then, by the third part of [§Associated Primes, ⁋Theorem 7](/en/math/commutative_algebra/associated_primes#thm7) together with the second part already proven, $\Ass_{S^{-1}A}S^{-1}M$ consists of exactly these $m$ prime ideals. Applying the first part over $S^{-1}A$, any primary decomposition of the zero submodule of $S^{-1}M$ must have all of these among its prime ideals, and hence must have at least $m$ components. That is, the decomposition above is minimal.
:::

## Primary Decomposition and Factorization

The following theorem shows that primary decomposition generalizes the familiar notion of factorization.

::: Theorem 7
For a Noetherian domain $A$, the following hold.

1. Suppose $f\in A$ factors as $f=u p_1^{e_1}\cdots p_n^{e_n}$, where $u$ is a unit, $e_i\geq 1$, and the $p_i$ are prime elements such that the $(p_i)$ are distinct prime ideals. Then $(f)=\bigcap(p_i^{e_i})$ is a minimal primary decomposition of $(f)$.
2. $A$ is a UFD if and only if every prime ideal minimal over a principal ideal is principal.
:::
::: Proof
We first prove the first claim. To begin with, we check that $(p_i^{e_i})$ is $(p_i)$-primary for each $i$. Since it is clear that $(p_i)^{e_i}=(p_i^{e_i})$ annihilates $A/(p_i^{e_i})$, by the third condition of [Proposition 2](#prop2) it suffices to show that the elements outside $(p_i)$ are not zero divisors on $A/(p_i^{e_i})$. For this, we show by induction on $e_i$ that whenever $x\not\in (p_i)$ and $a\in A$ satisfy $xa\in (p_i^{e_i})$, then $a\in(p_i^{e_i})$. The case $e_i=0$ is trivial. If $e_i\geq 1$, then $xa\in(p_i^{e_i})\subseteq (p_i)$, and since $(p_i)$ is prime and $x\not\in(p_i)$, we have $a\in (p_i)$. Thus we can write $a=p_ib$, and writing $xa=p_i^{e_i}c$, we have $p_i(xb-p_i^{e_i-1}c)=0$; since $A$ is a domain and $p_i\neq 0$, this gives $xb=p_i^{e_i-1}c\in (p_i^{e_i-1})$. By the induction hypothesis $b\in (p_i^{e_i-1})$, and therefore $a=p_ib\in(p_i^{e_i})$.

We now show that $(f)=\bigcap_{i=1}^n (p_i^{e_i})$. Since $f\in (p_i^{e_i})$ for each $i$, one inclusion is trivial. Conversely, let $g\in\bigcap_{i=1}^n (p_i^{e_i})$; we show $g\in (p_1^{e_1}\cdots p_j^{e_j})$ by induction on $j$. The case $j=0$ is trivial. Now assume we can write $g=p_1^{e_1}\cdots p_j^{e_j}h$. First, we check that $p_i\not\in (p_k)$ for any two distinct indices $i\neq k$: if $p_i=cp_k$, then since the prime element $p_i$ is irreducible ([\[Ring Theory\] §Integral Domains, ⁋Proposition 12](/en/math/ring_theory/integral_domains#prop12)) and $p_k$ is not a unit, $c$ must be a unit, giving $(p_i)=(p_k)$ and contradicting the assumption that the $(p_i)$ are distinct. Therefore, since $(p_{j+1})$ is prime, $p_1^{e_1}\cdots p_j^{e_j}\not\in (p_{j+1})$, and since $p_1^{e_1}\cdots p_j^{e_j}h=g\in (p_{j+1}^{e_{j+1}})$, what we showed in the previous paragraph gives $h\in (p_{j+1}^{e_{j+1}})$. That is, $g\in (p_1^{e_1}\cdots p_{j+1}^{e_{j+1}})$, and by induction we obtain $g\in (p_1^{e_1}\cdots p_n^{e_n})=(f)$. The last equality holds because $u$ is a unit.

To show that this decomposition is minimal, we first check that no component can be omitted. For each $i$, the product $\prod_{j\neq i} p_j^{e_j}$ lies in $\bigcap_{j\neq i}(p_j^{e_j})$ but not in $(p_i^{e_i})$: if it did, then in particular $\prod_{j\neq i}p_j^{e_j}\in (p_i)$, and since $(p_i)$ is prime, we would have $p_j\in (p_i)$ for some $j\neq i$, contradicting what we checked in the previous paragraph. Therefore, by the second part of [Theorem 3](#thm3), $\Ass(A/(f))=\{(p_1),\ldots,(p_n)\}$, and in particular these are $n$ distinct prime ideals. Meanwhile, by the first part of [Theorem 3](#thm3), every primary decomposition of $(f)$ must have all the elements of $\Ass(A/(f))$ among its primes, so it must have at least $n$ components. Hence the decomposition above is minimal.

We now prove the second claim. First, suppose $A$ is a UFD, and let a principal ideal $(f)$ and a prime ideal $\mathfrak{p}$ minimal among those containing $(f)$ be given. If $f=0$, then since $A$ is a domain, $(0)$ is prime, and hence $\mathfrak{p}=(0)$ is principal. If $f$ is a unit, there is no prime ideal containing $(f)=A$, so there is nothing to prove. Now suppose $f$ is a nonzero non-unit, and factor it as $f=up_1^{e_1}\cdots p_n^{e_n}$. Then $f\in\mathfrak{p}$, and since $\mathfrak{p}$ is prime, $p_i\in \mathfrak{p}$ for some $i$. That is, $(f)\subseteq (p_i)\subseteq \mathfrak{p}$, and since $(p_i)$ is prime, the minimality of $\mathfrak{p}$ forces $\mathfrak{p}=(p_i)$, which is principal.

Conversely, suppose that every prime ideal minimal over a principal ideal is principal. First, since $A$ is Noetherian, every nonzero non-unit element is a product of irreducible elements. Indeed, if not, the collection of principal ideals $(a)$ generated by nonzero non-unit elements $a$ that are not products of irreducible elements would be nonempty, so by the Noetherian condition we could choose a maximal element $(a)$ of this collection. Then $a$ is not irreducible, so we can write $a=bc$ for non-units $b,c$; if $(a)=(b)$, then $b=ad$ for some $d$ and $a=adc$, and since $A$ is a domain this would make $c$ a unit — a contradiction. Hence $(a)\subsetneq (b)$, and for the same reason $(a)\subsetneq(c)$. But then the maximality of $(a)$ implies that both $b$ and $c$ are products of irreducible elements, and hence so is $a=bc$ — a contradiction.

Next, we show that every irreducible element $p$ is prime. Since $A$ is Noetherian, there exists a prime ideal minimal among those containing $(p)$; calling it $\mathfrak{p}$, our assumption says that $\mathfrak{p}=(q)$ is principal. From $p\in (q)$ we can write $p=qc$, and since $p$ is irreducible and $q$ is a non-unit, $c$ must be a unit; therefore $(p)=(q)=\mathfrak{p}$ is a prime ideal. That is, $p$ is a prime element.

Finally, we show the uniqueness of factorization. Suppose $up_1\cdots p_m=vq_1\cdots q_k$ are products of irreducible elements with $u,v$ units; we induct on $m$. If $m=0$, then the left-hand side is a unit, so we must have $k=0$. If $m\geq 1$, then since $p_m$ is prime, $p_m\mid q_j$ for some $j$, and since $q_j$ is irreducible and $p_m$ is a non-unit, there exists a unit $w$ such that $q_j=wp_m$. Since $A$ is a domain, we can cancel $p_m$ from both sides and apply the induction hypothesis to conclude that, after a suitable rearrangement, each $p_i$ is an associate of $q_i$. Therefore $A$ is a UFD. ([\[Ring Theory\] §Integral Domains, ⁋Definition 16](/en/math/ring_theory/integral_domains#def16))
:::

---

**References**

**[Eis]** David Eisenbud. *Commutative Algebra: with a view toward algebraic geometry*. Springer, 1995.

---
