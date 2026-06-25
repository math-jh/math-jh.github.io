---
title: "Localization"
description: "We cover the localization of rings and the properties of local rings, which have a unique maximal ideal. We also extend this to the localization of modules and the notion of multiplicatively closed subsets."
excerpt: "Localization of rings and modules, and local ring construction"

categories: [Math / Commutative Algebra]
permalink: /en/math/commutative_algebra/localization
drift_needed: true
sidebar: 
    nav: "commutative_algebra-en"

date: 2024-09-05
weight: 2
translated_at: 2026-06-25T15:30:34+00:00
translation_source: kimi-cli
---
## Local Ring

In this post, we define localization. Briefly speaking, localization can be thought of as the process of making a ring $$A$$ into a local ring.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A ring $$A$$ is called a *local ring* if it has a unique maximal ideal.

</div>

Then we can show the following equivalence.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> For a ring $$A$$, the following are equivalent.

1. $$A$$ is a local ring.
2. Every non-unit of $$A$$ lies in some ideal $$\mathfrak{m}\subsetneq A$$ of $$A$$.
3. The set of all non-units of $$A$$ forms an ideal.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, assume 1, and let $$a\in A$$ be an arbitrary non-unit. Then $$(a)$$ is an ideal of $$A$$, so by [[Algebraic Structures] §Definition of Rings, ⁋Theorem 9](/en/math/algebraic_structures/rings#thm9) it is contained in some maximal ideal. But since $$A$$ has a unique maximal ideal $$\mathfrak{m}$$, we must have $$(a)\subseteq \mathfrak{m}$$, and thus $$a\in \mathfrak{m}$$.

Now assume 2 and show 3. For this, it suffices to show that the set of non-units of $$A$$ is closed under addition. First, from $$\mathfrak{m}\neq A$$ we know that $$\mathfrak{m}$$ does not contain any unit of $$A$$. From this we know that if we collect all non-units of $$A$$, this must equal $$\mathfrak{m}$$.

Finally, assume 3 and show 1. For any ideal $$\mathfrak{a}\subsetneq A$$, from the previous observation we know that $$\mathfrak{a}$$ consists only of non-units, and thus $$\mathfrak{a}$$ is contained in the ideal $$\mathfrak{m}$$ consisting of all non-units of $$A$$. On the other hand, $$\mathfrak{m}$$ is a maximal ideal because any element of $$A\setminus \mathfrak{m}$$ is a unit of $$A$$, so the only ideal containing $$\mathfrak{m}$$ is $$A$$ itself.

</details>

## Localization of Modules

As explained in the previous post, to look at localization of rings we more generally define localization of modules.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> A subset $$S$$ of a ring $$A$$ is *multiplicatively closed* if any product of elements of $$S$$ again belongs to $$S$$.

</div>

In particular, since $$1$$ can be thought of as the product of the empty family, we have $$1\in S$$ by definition.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> For a ring $$A$$, an $$A$$-module $$M$$, and a multiplicative subset $$S$$ of $$A$$, the *localization* of $$M$$ at $$S$$ is the $$A$$-module $$S^{-1}M$$ defined as follows.

1. As a set, $$S^{-1}M$$ is the quotient set of $$M\times S$$ by the equivalence relation

    $$(x,s)\sim (x',s')\iff \text{there exists $t\in S$ such that $t(s'x-sx')=0$}$$

    We write the representative of $$(x,s)$$ as $$x/s$$.
2. The $$A$$-module structure on $$S^{-1}M$$ is defined by

  $$\frac{x}{s}+\frac{x'}{s'}=\frac{s'x+sx'}{ss'},\qquad a\cdot \frac{x}{s}=\frac{ax}{s}.$$

</div>

We should verify that the operations defined in condition 2 actually give an $$A$$-module structure, but this is not difficult. Instead, we add a few observations. First, for any $$t\in S$$ and $$x/s\in S^{-1}M$$,

$$\frac{tx}{ts}=\frac{x}{s}$$

holds. This is simply because $$1(txs-tsx)=0$$. Also, we can examine the identity and inverse for addition in $$S^{-1}M$$. First, for any $$s,s'\in S$$ we can check that

$$\frac{0}{s}=\frac{0}{s'}$$

and from the equation

$$\frac{0}{s'}+\frac{x}{s}=\frac{x}{s}+\frac{0}{s'}=\frac{0s+s'x}{ss'}=\frac{s'x}{s's}=\frac{x}{s}$$

we see that this is the identity for addition in $$S^{-1}M$$. By a similar calculation, we can check that the inverse of any $$x/s$$ is $$(-x)/s$$.

The above calculations are no different from the addition and multiplication of fractions we have done since middle school. Taking this as intuition, we can define the canonical map $$\epsilon: M \rightarrow S^{-1}M$$ by $$x\mapsto x/1$$. Unfortunately, $$\epsilon$$ may not be an inclusion in general; the reason is obvious and is contained in the following proposition.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> In the above situation, $$\epsilon(x)=0$$ is equivalent to the existence of some $$s\in S$$ such that $$sx=0$$. In particular, if $$M$$ is finitely generated, then $$S^{-1}M=0$$ is equivalent to $$M$$ being annihilated by $$S$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

If

$$\epsilon(x)=x/1=0=0/1$$

then there exists some $$s\in S$$ such that

$$s(1x-0\cdot1)=sx=0$$

holds. The above logic also works in the opposite direction.

</details>

## Localization of Rings

The simplest example of localization is the ring of fractions examined in [[Algebraic Structures] §Field of Fractions, ⁋Definition 2](/en/math/algebraic_structures/field_of_fractions#def2). Here we took $$M=A$$. In particular, we also saw that if $$A$$ is an integral domain, then its ring of fractions $$\Frac(A)$$ becomes a field. ([[Algebraic Structures] §Field of Fractions, ⁋Proposition 6](/en/math/algebraic_structures/field_of_fractions#prop6))

As another example, again taking $$M=A$$ and letting $$S=A\setminus \mathfrak{p}$$ for a prime ideal $$\mathfrak{p}$$ of $$A$$, we could consider $$A_\mathfrak{p}=S^{-1}A$$. Using [Definition 4](#def4), this can be applied to any $$A$$-module $$M$$ as well, and the resulting $$A$$-module is written as $$M_\mathfrak{p}$$.

Both of the above examples have a multiplication structure in addition to the addition structure and scalar multiplication by $$A$$ defined in [Definition 4](#def4). Explicitly, this structure is given by

$$\frac{x}{s}\frac{x'}{s'}=\frac{xx'}{ss'}$$

so we can think of $$S^{-1}A$$ as an $$A$$-algebra.

Localization of rings has the following universal property.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> Fix rings $$A,B$$ and a multiplicative subset $$S$$ of $$A$$. If the image $$f(S)\subseteq B$$ of $$S$$ under a ring homomorphism $$f:A \rightarrow B$$ satisfies $$f(S)\subseteq B^\times$$, then there exists a unique ring homomorphism $$\overline{f}: S^{-1}A \rightarrow B$$ such that $$\overline{f}\circ\epsilon=f$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Suppose $$f$$ satisfying the given condition is given. If $$\overline{f}: S^{-1}A \rightarrow B$$ satisfying the given condition exists, then for any $$a/s\in S^{-1}A$$,

$$\overline{f}\left(\frac{a}{s}\right)=\overline{f}\left(\frac{a}{1}\frac{1}{s}\right)=\overline{f}(\epsilon(a)\epsilon(s)^{-1})=\overline{f}(\epsilon(a))\overline{f}(\epsilon(s)^{-1})=f(a)f(s)^{-1}$$

must hold, so if $$\overline{f}$$ exists it is uniquely determined by the above formula. Now it suffices to show that $$\overline{f}: S^{-1}A \rightarrow B$$ defined by $$\overline{f}(a/s)=f(a)f(s)^{-1}$$ is a ring homomorphism, which is a straightforward calculation.

</details>

From this, the functoriality of localization can also be shown.

## Localization and Ideals

On the other hand, there is a specific relationship between localization and ideals. First, let us define the following.

<div class="definition" markdown="1">

<ins id="def7">**Definition 7**</ins> For a ring homomorphism $$f:A \rightarrow B$$, an ideal $$\mathfrak{a}$$ of $$A$$, and an ideal $$\mathfrak{b}$$ of $$B$$, we define the following.

1. The *contraction* of $$\mathfrak{b}$$ under $$f$$ is the ideal $$f^{-1}(\mathfrak{b})$$ of $$A$$, written $$\mathfrak{b}^c$$.
2. The *extension* of $$\mathfrak{a}$$ under $$f$$ is the ideal of $$B$$ generated by the image $$f(\mathfrak{a})$$, written $$\mathfrak{a}^e$$.

</div>

To make the first definition, we need to prove that $$f^{-1}(\mathfrak{b})$$ is an ideal, but this proof is easy. Although the above notation is useful, it is relatively less intuitive, so after this post we will write $$f^{-1}(\mathfrak{b})$$ and $$f(\mathfrak{a})B$$ instead of the above notation.

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8**</ins> For any ring $$A$$, multiplicative subset $$S$$, localization $$S^{-1}A$$, and canonical map $$\epsilon:A \rightarrow S^{-1}A$$, the following hold.

1. For any ideal $$\mathfrak{b}\subset S^{-1}A$$, we have $$\mathfrak{b}=\mathfrak{b}^{ce}$$.
2. For any ideal $$\mathfrak{a}\subset A$$,

    $$\mathfrak{a}^{ec}=\{a\in A\mid\text{there exists $s\in S$ satisfying $sa\in \mathfrak{a}$}\}$$

    holds. In particular, $$\mathfrak{a}^e=S^{-1}A$$ is equivalent to $$\mathfrak{a}\cap S\neq\emptyset$$.

Therefore, there exists an inclusion-preserving bijection between the prime ideals of $$S^{-1}A$$ and the prime ideals of $$A$$ that do not meet $$S$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

1. First, $$\mathfrak{b}^{ce}\subseteq \mathfrak{b}$$ always holds in general. For the reverse direction, let $$a/s\in \mathfrak{b}$$. Then $$s(a/s)=a/1$$ must belong to $$\mathfrak{b}$$, so $$a\in \mathfrak{b}^c$$ holds. Thus $$a/1\in \mathfrak{b}^{ce}$$ and from this we know $$a/s=(1/s)(a/1)\in \mathfrak{b}^{ce}$$.
2. Let us write the right-hand side of the given formula as $$\mathfrak{a}'$$ for convenience. Then first, for any $$a'\in \mathfrak{a}'$$, there exists $$s$$ such that $$sa'\in \mathfrak{a}$$. From $$a'/1=sa'/s\in \mathfrak{a}^e$$ we know $$a'\in \mathfrak{a}^{ec}$$. Conversely, for any $$a\in \mathfrak{a}^{ec}$$, we can find $$a\in \mathfrak{a}$$ and $$s\in S$$ satisfying $$a/1=a'/s$$. Then there exists appropriate $$t\in S$$ such that $$tsa=ta'\in \mathfrak{a}$$, and since $$ts\in S$$, by definition $$a\in \mathfrak{a}'$$ holds. Also

  $$\mathfrak{a}^e=S^{-1}A\iff 1/1\in \mathfrak{a}^e\iff 1\in \mathfrak{a}^{ec}\iff \text{there exists $s\in S$ s.t. $s1\in \mathfrak{a}$}\iff \mathfrak{a}\cap S\neq \emptyset$$

  holds.

Now from the result of 2, we know that for any $$\mathfrak{b}\subseteq S^{-1}A$$, $$\mathfrak{b}^c$$ is a prime ideal of $$A$$ not meeting $$S$$. ([[Algebraic Structures] §Field of Fractions, ⁋Proposition 9](/en/math/algebraic_structures/field_of_fractions#prop9)) Conversely, let $$\mathfrak{a}\subseteq A$$ be a prime ideal of $$A$$ not meeting $$S$$. Then $$\mathfrak{a}^e$$ is a prime ideal of $$S^{-1}A$$. Suppose for arbitrary $$b/t,b'/t'$$ that $$(b/t)(b'/t')\in \mathfrak{a}^e$$. Then there exist appropriate $$a\in \mathfrak{a}$$ and $$s\in S$$ such that $$(bb')/(tt')=a/s$$, and thus there exists appropriate $$u\in S$$ such that $$utt'a=usbb'\in \mathfrak{a}$$. Now from $$\mathfrak{a}\cap S=\emptyset$$ we know $$us\not\in \mathfrak{a}$$, and since $$\mathfrak{a}$$ is a prime ideal, $$bb'\in \mathfrak{a}$$ holds. Therefore $$b\in \mathfrak{a}$$ or $$b'\in \mathfrak{a}$$, and $$\mathfrak{a}^e$$ is a prime ideal. That these correspondences are inverses of each other follows naturally from the result of 2.

</details>

The following is obvious from the above proposition.

<div class="proposition" markdown="1">

<ins id="cor9">**Corollary 9**</ins> The localization of a Noetherian ring is noetherian.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Given an ascending chain of ideals of $$S^{-1}A$$

$$\mathfrak{b}_0\subseteq \mathfrak{b}_1\subseteq\cdots$$

$$\mathfrak{b}_0^c\subseteq \mathfrak{b}_1^c\subseteq\cdots$$

is an ascending chain of ideals of the noetherian ring $$A$$, so there exists appropriate $$N$$ such that for all $$n>N$$, $$\mathfrak{b}_n^c=\mathfrak{b}_{n+1}^c$$. Now for such $$n$$,

$$\mathfrak{b}_n=\mathfrak{b}_n^{ce}=\mathfrak{b}_{n+1}^{ce}=\mathfrak{b}_{n+1}$$

holds.

</details>

On the other hand, from [Proposition 8](#prop8), for any prime ideal $$\mathfrak{p}$$ of $$A$$, $$\mathfrak{p}^e=\mathfrak{p}A_\mathfrak{p}$$ is the unique *maximal* ideal of $$A_\mathfrak{p}$$. That is, $$A_\mathfrak{p}$$ is a local ring, and its quotient field $$A_\mathfrak{p}/\mathfrak{p}A_\mathfrak{p}$$ is well-defined.

<div class="definition" markdown="1">

<ins id="def10">**Definition 10**</ins> For a ring $$A$$ and a prime ideal $$\mathfrak{p}$$, we call the field $$A_\mathfrak{p}/\mathfrak{p}A_\mathfrak{p}$$ the *residue field* of $$A$$ at $$\mathfrak{p}$$ and write it as $$\kappa(\mathfrak{p})$$.

</div>

---

**References**

**[Eis]** David Eisenbud. *Commutative Algebra: with a view toward algebraic geometry*. Springer, 1995.

---
