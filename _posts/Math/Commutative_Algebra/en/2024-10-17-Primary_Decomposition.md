---title: "Primary Decomposition"
excerpt: "Primary decomposition and uniqueness for modules over Noetherian rings"

categories: [Math / Commutative Algebra]
permalink: /en/math/commutative_algebra/primary_decomposition
header:
    overlay_image: /assets/images/Math/Commutative_Algebra/Primary_Decomposition.png
    overlay_filter: 0.5
sidebar: 
    nav: "commutative_algebra-en"

date: 2024-10-17
last_modified_at: 2024-10-17
weight: 7
translated_at: 2026-05-28T11:36:15+00:00
translation_source: kimi-cli
---
<div class="remark" markdown="1">

In this post we assume that $$A$$ is Noetherian and $$M$$ is a finitely generated $$A$$-module.

</div>

## Primary Submodules

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A submodule $$N$$ of $$M$$ is *primary* if $$\Ass(M/N)$$ consists of a single prime ideal. In this case, if $$\Ass(M/N)=\{\mathfrak{p}\}$$, we call $$N$$ a $$\mathfrak{p}$$-primary submodule. If $$\Ass(M)$$ consists of a single prime ideal, we call $$M$$ *coprimary*.

</div>

That is, if $$M/N$$ is coprimary then $$N$$ is primary. Also, from [§Associated Primes, ⁋Lemma 5](/en/math/commutative_algebra/associated_primes#lem5) we know that any finite intersection of $$\mathfrak{p}$$-primary submodules is $$\mathfrak{p}$$-primary.

Now the following holds.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> For a ring $$A$$ and a prime ideal $$\mathfrak{p}$$, the following are equivalent.

1. The $$A$$-module $$M$$ is $$\mathfrak{p}$$-coprimary.
2. $$\mathfrak{p}$$ is minimal among prime ideals containing $$\ann(M)$$, and elements not in $$\mathfrak{p}$$ are not zero divisors on $$M$$.
3. For some $$k$$, $$\mathfrak{p}^k$$ annihilates $$M$$, and elements not in $$\mathfrak{p}$$ are not zero divisors on $$M$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, suppose the first condition holds. Then by definition $$\mathfrak{p}$$ is the unique associated prime of $$M$$. Now by condition 1 of [§Associated Primes, ⁋Theorem 7](/en/math/commutative_algebra/associated_primes#thm7), $$\mathfrak{p}$$ must be minimal among prime ideals containing $$\ann(M)$$, and by condition 2, elements outside $$\mathfrak{p}$$ are not zero divisors on $$M$$.

Now assume the second condition holds. Then since elements of $$A\setminus \mathfrak{p}$$ are not zero divisors on $$M$$, it suffices to prove the claim after localizing at $$\mathfrak{p}$$. That is, we may assume $$(A, \mathfrak{p})$$ is a local ring, and now the desired result follows from the assumption that $$\mathfrak{p}$$ is minimal over $$\ann(M)$$ and [§Properties of Localization, ⁋Corollary 8](/en/math/commutative_algebra/properties_of_localization#cor8).

Finally, suppose the third condition holds. Then it is obvious that $$\mathfrak{p}$$ is minimal among prime ideals containing $$\ann M$$, and therefore by the first condition of [§Associated Primes, ⁋Theorem 7](/en/math/commutative_algebra/associated_primes#thm7), $$\mathfrak{p}$$ is an associated prime of $$M$$. Also, since elements outside $$\mathfrak{p}$$ are all not zero divisors, by the second condition of [§Associated Primes, ⁋Theorem 7](/en/math/commutative_algebra/associated_primes#thm7) we know that any associated prime is always contained in $$\mathfrak{p}$$. That is, $$\mathfrak{p}$$ is the unique associated prime of $$M$$.

</details>

## Primary Decomposition

Our goal in this post is to prove the following theorem.

<div class="proposition" markdown="1">

<ins id="thm3">**Theorem 3 (Primary decomposition)**</ins> Any submodule $$M'$$ of $$M$$ is an intersection of primary submodules. That is, for prime ideals $$\mathfrak{p}_1,\ldots, \mathfrak{p}_n$$ and $$\mathfrak{p}_k$$-primary submodules $$M_k$$, we can write $$M'=\bigcap_{k=1}^n M_k$$. We call this a *primary decomposition*, and then the following hold.

1. The associated primes of $$M/M'$$ are among the $$\mathfrak{p}_k$$.
2. If there are no redundant $$M_k$$ in the expression for $$M'$$, then the $$\mathfrak{p}_i$$ are exactly the associated primes of $$M/M'$$.
3. If there is no way to express $$M'$$ using fewer $$M_k$$, then the associated primes of $$M/M'$$ correspond exactly to one $$\mathfrak{p}_k$$ per index. If in addition $$\mathfrak{p}_i$$ is minimal among prime ideals containing the annihilator ideal of $$M/M'$$, then $$M_i$$ is the $$\mathfrak{p}_i$$-primary component of $$M'$$.
4. For a given minimal primary decomposition and any multiplicative subset $$S$$ of $$A$$, let $$\mathfrak{p}_1,\ldots, \mathfrak{p}_m$$ be the prime ideals not meeting $$S$$. Then

    $$S^{-1}M'=\bigcap_{i=1}^m S^{-1}M_i$$

    is a minimal primary decomposition of $$S^{-1}M$$ over $$S^{-1}A$$.

</div>

To prove this, we first define the irreducible decomposition of a module.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> A submodule $$N$$ of an $$A$$-module $$M$$ is *irreducible* if there do not exist $$N_1,N_2\supsetneq N$$ with $$N=N_1\cap N_2$$.

</div>

Then the following holds.

<div class="proposition" markdown="1">

<ins id="lem5">**Lemma 5 (Noether)**</ins> Any submodule of $$M$$ can be expressed as an intersection of irreducible submodules.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

We use proof by contradiction. Since $$M$$ is Noetherian, we can choose a maximal submodule among those that cannot be expressed as an intersection of irreducible submodules. Call this $$N$$. Then $$N$$ is not irreducible, so there exist $$N_1,N_2\supsetneq N$$ with $$N=N_1\cap N_2$$. But by maximality of $$N$$, both $$N_1$$ and $$N_2$$ are intersections of irreducible submodules, and therefore so is $$N$$, which is a contradiction.

</details>

From this we know that for any submodule $$M'$$ of $$M$$, an *irreducible decomposition*

$$M'=\bigcap_{k=1}^n M_k,\qquad \text{$M_k$ irreducible}$$

always exists.

<div class="proposition" markdown="1">

<ins id="lem6">**Lemma 6**</ins> The above irreducible decomposition is a primary decomposition.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

For this it suffices to show that any irreducible submodule $$P$$ is primary, which is the same as showing that $$M/P$$ is coprimary. Suppose for contradiction that $$M/P$$ has two associated primes $$\mathfrak{p},\mathfrak{q}$$. Then $$M/P$$ has submodules isomorphic to $$A/\mathfrak{p}$$ and $$A/\mathfrak{q}$$ respectively. Then by definition the annihilator of any nonzero element of $$A/\mathfrak{p}$$ is $$\mathfrak{p}$$, and the annihilator of any nonzero element of $$A/\mathfrak{q}$$ is $$\mathfrak{q}$$, so they have only $$0$$ in common. That is, the zero submodule of $$M/P$$ is reducible. From this we obtain that $$P$$ is reducible in $$M$$, a contradiction.

</details>

Therefore any submodule of $$M$$ always has a primary decomposition. We now need to prove the remaining parts of [Theorem 3](#thm3). As in the proof of the preceding lemma, when proving these it suffices to work with $$M/M'$$, so without loss of generality we may assume $$M'=0$$.

<details class="proof--alone" markdown="1">
<summary>Proof of Theorem 3</summary>

First, to prove the first result, suppose a primary decomposition of the zero submodule of $$M$$ is given:

$$0=\bigcap_{k=1}^n M_k$$

Then from a generalization of the exact sequence of [\[Multilinear Algebra\] §Exact Sequences, ⁋Proposition 7](/en/math/multilinear_algebra/exact_sequences#prop7#prop7),

$$M\subseteq \bigoplus_{k=1}^n M/M_k$$

so by [§Associated Primes, ⁋Lemma 5](/en/math/commutative_algebra/associated_primes#lem5) we know that any prime of $$\Ass M$$ is obtained among the $$\mathfrak{p}_k$$.

Now we prove the second result. Then in particular, for each $$j$$,

$$\bigcap_{k\neq j} M_k\neq 0$$

holds. Then since $$M_j\cap \bigcap_{k\neq j}M_k=0$$,

$$\bigcap_{k\neq j} M_k=\left(\bigcap_{k\neq j} M_k\right)\bigg/\left(M_k\cap \bigcap_{k\neq j}M_k\right)\cong \left(\bigcap_{k\neq j} M_k + M_j\right)\bigg/M_j\subseteq M/M_j$$

so $$\bigcap_{k\neq j} M_k$$ is $$\mathfrak{p}_j$$-coprimary. From this we obtain the desired result.

Now we prove the third result. In general, since the intersection of $$\mathfrak{p}$$-primary submodules is also $$\mathfrak{p}$$-primary, to satisfy the given condition the $$\mathfrak{p}_k$$ must all be distinct prime ideals. Now assume the $$\mathfrak{p}_k$$ are minimal among those containing the annihilator ideal, and let us show that $$\Ass(M/M_k)=\{\mathfrak{p}_k\}$$. For this we need to show that for any nonzero $$x+M_k\in M/M_k$$, $$\ann(x)=\mathfrak{p}_k$$ holds, so by [§Localization, ⁋Proposition 5](/en/math/commutative_algebra/localization#prop5) it suffices to show that the kernel of $$\varepsilon: M \rightarrow M_{\mathfrak{p}_k}$$ is $$M_k$$.

Now consider the following commutative diagram

![injective](/assets/images/Math/Commutative_Algebra/Primary_Decomposition-1.png){:style="width:12em" class="invert" .align-center}

Then since the kernel of $$M \rightarrow M/M_k$$ is $$M_k$$, to prove the desired claim it suffices to show that both $$M_{\mathfrak{p}_k}\rightarrow (M/M_k)_{\mathfrak{p}_k}$$ and $$M/M_k \rightarrow (M/M_k)_{\mathfrak{p}_k}$$ are injective. First, the injectivity of $$M/M_k \rightarrow (M/M_k)_{\mathfrak{p}_k}$$ is obvious from the fact that $$M_k$$ is $$\mathfrak{p}_k$$-primary. Then as we saw at the beginning,

$$M \rightarrow \bigoplus_{k=1}^n M/M_k$$

is injective, and therefore its localization

$$M_{\mathfrak{p}_k} \rightarrow \left(\bigoplus_{k=1}^n M/M_k\right)_{\mathfrak{p}_k} $$

is also injective. On the other hand, for each $$j\neq k$$, $$M/M_j$$ is $$\mathfrak{p}_j$$-coprimary, and by minimality $$\mathfrak{p}_j$$ must not be contained in $$\mathfrak{p}_i$$, so $$(M/M_j)_{\mathfrak{p}_k}=0$$ holds, and the resulting map is exactly $$M_{\mathfrak{p}_k}\rightarrow (M/M_k)_{\mathfrak{p}_k}$$, so we obtain the desired result.

The last claim is almost obvious.

</details>

## Primary Decomposition and Factorization

Meanwhile, the following theorem shows that primary decomposition generalizes the notion of factorization we already know.

<div class="proposition" markdown="1">

<ins id="thm7">**Theorem 7**</ins> For a Noetherian domain $$A$$, the following hold.

1. Suppose $$f\in A$$ factors as $$f=u p_1^{e_1}\cdots p_n^{e_n}$$. Here $$u$$ is a unit and the $$p_i$$ are elements such that the $$(p_i)$$ are pairwise distinct prime ideals. Then $$(f)=\bigcap(p_i^{e_i})$$ is a minimal primary decomposition of $$(f)$$.
2. $$A$$ is a UFD if and only if all minimal prime ideals over principal ideals are principal.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>



</details>

---

**References**

**[Eis]** David Eisenbud. *Commutative Algebra: with a view toward algebraic geometry*. Springer, 1995.

---
