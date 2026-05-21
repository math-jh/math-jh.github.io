---
title: "Nullstellensatz"
excerpt: "Proofs of Jacobson rings and Hilbert's Nullstellensatz"

categories: [Math / Commutative Algebra]
permalink: /en/math/commutative_algebra/nullstellensatz
header:
    overlay_image: /assets/images/Math/Commutative_Algebra/Nullstellensatz.png
    overlay_filter: 0.5
sidebar: 
    nav: "commutative_algebra-en"

date: 2024-10-20
last_modified_at: 2024-10-20
weight: 10
translated_at: 2026-05-19T21:00:02+00:00
translation_source: kimi-cli
---
## Jacobson Rings

For a ring $$A$$ and an ideal $$\mathfrak{a}$$, we saw that the following formula holds:

$$\sqrt{\mathfrak{a}}=\bigcap_\text{\scriptsize$\mathfrak{p}$ prime containing $\mathfrak{a}$} \mathfrak{p}$$

([§Properties of Localization, ⁋Corollary 8](/en/math/commutative_algebra/properties_of_localization#cor8)) In particular, if $$\mathfrak{a}$$ is a prime ideal, it is clear that $$\mathfrak{p}=\sqrt{\mathfrak{p}}$$ must hold. More generally, we make the following definition.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> An ideal $$\mathfrak{a}$$ of a ring $$A$$ is called a *radical ideal* if $$\mathfrak{a}=\sqrt{\mathfrak{a}}$$ holds.

</div>

Thus, the above observation says in short that any prime ideal is radical. The proof of this observation is somewhat trivial, but if we had considered the intersection of *maximal* ideals containing $$\mathfrak{p}$$ instead of prime ideals containing $$\mathfrak{p}$$, in a manner similar to [§Integral Extension, §§Nakayama's Lemma](/en/math/commutative_algebra/integral_extension#나카야마-보조정리), then this observation would not have been so obvious, and in fact it would not hold. For example, any local ring containing a prime ideal that is not maximal, such as $$\mathbb{Z}_{(2)}$$, is a counterexample.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> A ring $$A$$ is called a *Jacobson ring* if every prime ideal can be expressed as an intersection of maximal ideals.

</div>

Then the following holds.

<div class="proposition" markdown="1">

<ins id="lem3">**Lemma 3 (Rabinowitch)**</ins> For a ring $$A$$, the following are equivalent.

1. $$A$$ is a Jacobson ring.
2. For a prime ideal $$\mathfrak{p}$$ of $$A$$, if there exists $$a\in A/\mathfrak{p}$$ such that $$(A/\mathfrak{p})[a^{-1}]$$ is a field, then $$A/\mathfrak{p}$$ is a field.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, suppose $$A$$ is Jacobson. Then it is obvious from the definition that its quotient $$A/\mathfrak{p}$$ is also Jacobson. Meanwhile, by [\[Algebraic Structures\] §Field of Fractions, ⁋Proposition 8](/en/math/algebraic_structures/field_of_fractions#prop8), $$A/\mathfrak{p}$$ is an integral domain, and since $$(0)$$ is a prime ideal in an integral domain, we can write $$(0)$$ as an intersection of maximal ideals. However, by [§Localization, ⁋Proposition 8](/en/math/commutative_algebra/localization#prop8), there is a one-to-one correspondence between prime ideals of $$(A/\mathfrak{p})[a^{-1}]$$ and prime ideals of $$A/\mathfrak{p}$$ not containing $$a$$, and by assumption the only prime ideal of $$(A/\mathfrak{p})[a^{-1}]$$ is $$0$$, so the only prime ideal of $$A/\mathfrak{p}$$ not containing $$a$$ is also $$0$$. That is, any nonzero prime ideal of $$A/\mathfrak{p}$$ must contain $$a$$. But if such a prime ideal exists, then since $$A/\mathfrak{p}$$ is an integral domain,

$$(0)=\sqrt{(0)}=\bigcap_\text{\scriptsize$\mathfrak{p}$ a prime} \mathfrak{p}$$

and thus $$a=0$$, which is a contradiction.

Conversely, assume the second condition and let us show the first. Fix a prime ideal $$\mathfrak{p}$$ of $$A$$, and let $$\mathfrak{P}$$ be the intersection of all maximal ideals containing $$\mathfrak{p}$$; we must show that $$\mathfrak{p}=\mathfrak{P}$$. Suppose, for contradiction, that there exists an element $$a\in \mathfrak{P}\setminus \mathfrak{p}$$. Then by [\[Set Theory\] §Axiom of Choice, ⁋Theorem 4](/en/math/set_theory/axiom_of_choice#thm4), there exists a prime ideal $$\mathfrak{q}$$ containing $$\mathfrak{p}$$ but not containing $$a$$ that is maximal with respect to this property. By definition $$a\not\in \mathfrak{q}$$, so $$\mathfrak{q}$$ is not a maximal ideal, and hence $$A/\mathfrak{q}$$ is not a field. However, in $$A[a^{-1}]$$, $$\mathfrak{q}$$ must be a maximal ideal by definition, and this contradicts the second condition; therefore $$\mathfrak{p}=\mathfrak{P}$$.

</details>

## Nullstellensatz

We can now state the Nullstellensatz as follows.

<div class="proposition" markdown="1">

<ins id="thm4">**Theorem 4**</ins> Let $$A$$ be a Jacobson ring and let $$E$$ be a finitely generated $$A$$-algebra. Then $$E$$ is also a Jacobson ring. Moreover, if $$\mathfrak{n}$$ is a maximal ideal of $$E$$, then $$\mathfrak{m}=\mathfrak{n}\cap A$$ is a maximal ideal of $$A$$, and $$E/\mathfrak{n}$$ is a finite field extension of $$A/\mathfrak{m}$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

We divide the proof into three steps.

1. First, consider the case where $$A=\mathbb{K}$$ and $$E=\mathbb{K}[\x]$$. Then $$E$$ is a principal ideal domain, and in particular any prime ideal of $$E$$ is generated by an irreducible monic polynomial. From this we see that no prime ideal can be contained in another prime ideal, so any prime ideal of $$E$$ is maximal, and since such an ideal cannot contain $$1\in \mathbb{K}$$, its intersection with $$A=\mathbb{K}$$ must be $$(0)$$. In this case, $$E/\mathfrak{n}$$ becomes a $$\mathbb{K}$$-vector space of dimension equal to the degree of the irreducible polynomial defining $$\mathfrak{n}$$. Finally, to show that $$(0)$$ is an intersection of maximal ideals, we use the argument that $$E=\mathbb{K}[\x]$$ has infinitely many irreducible polynomials, and since the degree of a polynomial must be finite, the only polynomial having all of them as factors is $$0$$. Here the infinitude of irreducible polynomials in $$E$$ follows exactly from Euclid's proof of the infinitude of primes.
2. Next, for an arbitrary Jacobson ring $$A$$ and an $$A$$-algebra $$E$$ generated by one element, we show that $$E$$ is Jacobson by verifying the second condition of [Lemma 3](#lem3). That is, our goal in this step is to prove the following proposition.
    > Let $$A$$ be a Jacobson ring and let $$E$$ be an $$A$$-algebra generated by one element. If for a fixed prime ideal $$\mathfrak{q}\subseteq E$$, there exists a nonzero $$x\in E/\mathfrak{q}$$ such that $$(E/\mathfrak{q})[x^{-1}]$$ is a field, then $$E/\mathfrak{q}$$ is also a field.

    Now since $$E'=E/\mathfrak{q}$$ is also an $$A$$-algebra generated by one element, showing the above proposition is equivalent to showing the following.
    > Let $$A$$ be a Jacobson ring and let $$E'$$ be an $$A$$-algebra generated by one element that is an integral domain. If there exists a nonzero $$x\in E'$$ such that $$E'[x^{-1}]$$ is a field, then $$E'$$ is also a field.

    In this process of taking the quotient, $$A$$ is replaced by $$A'=A/(A\cap \mathfrak{q})$$, which is also a Jacobson ring; consequently, what we must show is the following proposition.
    > Let $$A'$$ be a Jacobson integral domain and let $$E'$$ be an integral domain that is an $$A'$$-algebra generated by one element and contains $$A'$$. If there exists a nonzero $$x\in E'$$ such that $$E'[x^{-1}]$$ is a field, then $$E'$$ is also a field.

    For this, we show that under the above assumptions $$A'$$ must be a field and $$E'$$ is a finite extension of $$A'$$. Since $$E'$$ in the above proposition is an $$A'$$-algebra generated by one element, we can write $$E'=A'[\x]/\mathfrak{q}$$. First let us show that $$\mathfrak{q}\neq 0$$. Suppose, for contradiction, that $$\mathfrak{q}=0$$ and that there exists a suitable $$x\in E'/(0)=A'[\x]$$ such that $$E'[x^{-1}]=A'[\x][x^{-1}]$$ is a field. Let $$K'=\Frac(A')$$; then by this assumption $$K'[\x][x^{-1}]$$ is also a field. But $$K'[\x]$$ is Jacobson by the first result, so $$K'[\x]$$ must be a field, which is a contradiction. Therefore $$\mathfrak{q}\neq 0$$, and $$E'[x^{-1}]=K'[\x]/\mathfrak{q}K'[\x]$$ is a finite dimensional extension of $$K'$$.  
    Now suppose $$p(x)\in \mathfrak{q}$$ satisfies the following equation in $$E'$$:

    $$p(\alpha)=p_n\alpha^n+\cdots+p_0=0$$

    where $$\alpha$$ is the generator of $$E'$$ as an $$A'$$-algebra. Then from the above equation we see that $$E'[p_n^{-1}]$$ is an integral $$A'[p_n^{-1}]$$-algebra. On the other hand, the $$x$$ defined above must also satisfy a suitable polynomial equation

    $$q(x)=q_mx^m+\cdots+q_0=0$$

    and since $$E'$$ is an integral domain, we may assume without loss of generality that $$q_0\neq 0$$. Then from the monic polynomial

    $$\left(\frac{1}{x}\right)^m+\frac{q_1}{q_0}\left(\frac{1}{x}\right)^{m-1}+\cdots+\frac{q_m}{q_0}=0$$

    we see that $$E'[x^{-1}]$$ is an integral $$A'[(p_nq_0)^{-1}]$$-algebra. Now by [§Integral Extensions and Ideals, ⁋Corollary 3](/en/math/commutative_algebra/lying_over_and_going_up#cor3), $$A'[(p_nq_0)^{-1}]$$ is a field, and since $$A'$$ is Jacobson by assumption, [Lemma 3](#lem3) implies that $$A'$$ is a field. Therefore $$E'$$ is an integral $$A'$$-algebra, and again by [§Integral Extensions and Ideals, ⁋Corollary 3](/en/math/commutative_algebra/lying_over_and_going_up#cor3), we see that $$E'$$ is a field.
3. The final case now follows by induction using the second result.

</details>

In particular, consider the case where $$A=\mathbb{K}$$ and $$E=\mathbb{K}[\x_1,\ldots, \x_n]$$. Then for any

$$a=(a_1,\ldots, a_n)\in \mathbb{K}^n$$

if we define the ideal $$\mathfrak{m}_a$$ by the formula

$$\mathfrak{m}_a=(\x_1-a_1,\ldots, \x_n-a_n)$$

then from the isomorphism

$$\ev_a:\mathbb{K}[\x_1,\ldots, \x_n]/\mathfrak{m}_a\rightarrow \mathbb{K}$$

given by evaluation, we see that $$\mathfrak{m}_a$$ is a maximal ideal.

Moreover, if $$\mathbb{K}$$ is an algebraically closed field, then every maximal ideal of $$E$$ is of this form. First, for any maximal ideal $$\mathfrak{n}$$ of $$E$$, $$E/\mathfrak{n}$$ is an algebraic extension of $$\mathbb{K}/(\mathfrak{n}\cap \mathbb{K})=\mathbb{K}$$, and if $$\mathbb{K}$$ is algebraically closed then such an extension can only be itself, so we must have $$E/\mathfrak{n}\cong \mathbb{K}$$. On the other hand, letting $$a_i$$ be the element of $$\mathbb{K}$$ to which each $$\x_i$$ is mapped under the canonical surjection $$E \rightarrow E/\mathfrak{n}\cong \mathbb{K}$$, we have $$\mathfrak{m}_a\subseteq \mathfrak{n}$$, and the desired result follows from the maximality of $$\mathfrak{m}_a$$.

Therefore, from [§Basic Notions, ⁋Proposition 11](/en/math/commutative_algebra/basic_notions#prop11) we obtain the following.

<div class="proposition" markdown="1">

<ins id="lem5">**Lemma 5**</ins> Let $$\mathbb{K}$$ be a field. Then $$\mathfrak{m}_a=(\x_1-a_1,\ldots, \x_n-a_n)$$ is a maximal ideal of $$\mathbb{K}[\x_1,\ldots, \x_n]$$. Also, if $$\mathbb{K}$$ is algebraically closed, there is a one-to-one correspondence between maximal ideals of $$\mathbb{K}[\x_1,\ldots,\x_n]/(f_1,\ldots, f_r)$$ and the solutions $$(x_1,\ldots, x_n)$$ of the system of equations

$$f_1(x_1,\ldots, x_n)=\cdots=f_r(x_1,\ldots, x_n)=0$$

</div>

A slightly more traditional version of the Nullstellensatz also follows from this. To state it, consider the function $$Z$$ that takes an ideal $$\mathfrak{a}$$ of $$\mathbb{K}[\x_1,\ldots, \x_n]$$ and returns the subset $$Z(\mathfrak{a})$$ of $$\mathbb{K}^n$$

$$Z(\mathfrak{a})=\{(a_1,\ldots, a_n)\in \mathbb{K}^n: \text{$f(a_1,\ldots, a_n)=0$ for all $f\in \mathfrak{a}$}\}$$

and the function $$I$$ that takes a subset $$S$$ of $$\mathbb{K}^n$$ and returns the subset

$$I(S)=\{f\in \mathbb{K}[\x_1,\ldots, \x_n]:\text{$f(a_1,\ldots, a_n)=0$ for all $(a_1,\ldots, a_n)\in S$}\}$$

of $$\mathbb{K}[\x_1,\ldots, \x_n]$$.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> Let $$\mathbb{K}$$ be an algebraically closed field and let $$\mathfrak{a}\subseteq \mathbb{K}[\x_1,\ldots, \x_n]$$ be an ideal. Then

$$I(Z(\mathfrak{a}))=\sqrt{\mathfrak{a}}$$

holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

From [Lemma 5](#lem5), we see that the elements of $$Z(\mathfrak{a})$$ correspond one-to-one with the maximal ideals of $$\mathbb{K}[\x_1,\ldots, \x_n]$$ containing $$\mathfrak{a}$$. Therefore $$I(Z(\mathfrak{a}))$$ is the intersection of the maximal ideals of $$\mathbb{K}[\x_1,\ldots, \x_n]$$ containing $$\mathfrak{a}$$, and since $$\mathbb{K}[\x_1,\ldots, \x_n]$$ is Jacobson by [Theorem 4](#thm4), this equals the intersection of the prime ideals of $$\mathbb{K}[\x_1,\ldots, \x_n]$$ containing $$\mathfrak{a}$$, which is exactly the right-hand side.

</details>

---

**References**

**[Eis]** David Eisenbud. *Commutative Algebra: with a view toward algebraic geometry*. Springer, 1995.

---
