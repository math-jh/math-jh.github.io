---
title: "Localization"
description: "We discuss the localization of rings and the properties of local rings, which possess a unique maximal ideal. We also extend this to the localization of modules and the notion of multiplicatively closed subsets."
excerpt: "Localization of rings and modules, and local ring construction"

categories: [Math / Commutative Algebra]
permalink: /en/math/commutative_algebra/localization
sidebar: 
    nav: "commutative_algebra-en"

date: 2024-09-05
weight: 2
translated_at: 2026-06-26T14:00:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-26T14:00:02+00:00
---
## Local Rings

In this post we define localization. Briefly speaking, localization can be thought of as the process of making a ring $$A$$ into a local ring.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A ring $$A$$ is called a *local ring* if it has a unique maximal ideal.

</div>

Then we can show the following equivalence.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> For a ring $$A$$, the following are equivalent.

1. $$A$$ is a local ring.
2. Every non-unit of $$A$$ lies in some proper ideal $$\mathfrak{m}\subsetneq A$$.
3. The set of all non-units of $$A$$ forms an ideal.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First assume (1), and let $$a\in A$$ be an arbitrary non-unit. Then $$(a)$$ is an ideal of $$A$$, so by [[Algebraic Structures] §Definition of Rings, ⁋Theorem 9](/en/math/algebraic_structures/rings#thm9) it is contained in some maximal ideal. But since $$A$$ has a unique maximal ideal $$\mathfrak{m}$$, we must have $$(a)\subseteq \mathfrak{m}$$, and hence $$a\in \mathfrak{m}$$.

Now assume (2) and show (3). For this, it suffices to show that the set of non-units of $$A$$ is closed under addition. First, from $$\mathfrak{m}\neq A$$ we know that $$\mathfrak{m}$$ contains no unit of $$A$$. From this we see that the set of all non-units of $$A$$ must equal $$\mathfrak{m}$$.

Finally, assume (3) and show (1). For any ideal $$\mathfrak{a}\subsetneq A$$, by the preceding observation we know that $$\mathfrak{a}$$ consists only of non-units, and therefore $$\mathfrak{a}$$ is contained in the ideal $$\mathfrak{m}$$ consisting of all non-units of $$A$$. On the other hand, $$\mathfrak{m}$$ is a maximal ideal because any element of $$A\setminus \mathfrak{m}$$ is a unit of $$A$$, so the only ideal containing $$\mathfrak{m}$$ is $$A$$ itself.

</details>

## Localization of Modules

As explained in the previous post, to study localization of rings we define localization of modules in greater generality.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> A subset $$S$$ of a ring $$A$$ is *multiplicatively closed* if the product of any elements of $$S$$ again belongs to $$S$$.

</div>

In particular, since $$1$$ can be regarded as the product of a family indexed by the empty set, we have $$1\in S$$ by definition.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> For a ring $$A$$, an $$A$$-module $$M$$, and a multiplicative subset $$S$$ of $$A$$, the *localization* of $$M$$ at $$S$$ is the $$A$$-module $$S^{-1}M$$ defined as follows.

1. As a set, $$S^{-1}M$$ is the quotient of $$M\times S$$ by the equivalence relation
    
    $$(x,s)\sim (x',s')\iff \text{there exists $t\in S$ such that $t(s'x-sx')=0$}$$
  
    We write the equivalence class of $$(x,s)$$ as $$x/s$$.
2. The $$A$$-module structure on $$S^{-1}M$$ is defined by
  
  $$\frac{x}{s}+\frac{x'}{s'}=\frac{s'x+sx'}{ss'},\qquad a\cdot \frac{x}{s}=\frac{ax}{s}.$$

</div>

We should verify that the operations defined in (2) actually yield an $$A$$-module structure, but this is not difficult. Instead we add a few observations. First, for any $$t\in S$$ and $$x/s\in S^{-1}M$$, we have

$$\frac{tx}{ts}=\frac{x}{s}$$

This holds simply because $$1(txs-tsx)=0$$. Also, we can examine the additive identity and inverses in $$S^{-1}M$$: for any $$s,s'\in S$$ we can verify that

$$\frac{0}{s}=\frac{0}{s'}$$

and from the equation

$$\frac{0}{s'}+\frac{x}{s}=\frac{x}{s}+\frac{0}{s'}=\frac{0s+s'x}{ss'}=\frac{s'x}{s's}=\frac{x}{s}$$

we see that this is the additive identity in $$S^{-1}M$$. By a similar calculation one can verify that the inverse of any $$x/s$$ is $$(-x)/s$$.

The above calculations are no different from the addition and multiplication of fractions we have done since middle school. Taking this as intuition, we define the canonical map $$\epsilon: M \rightarrow S^{-1}M$$ by $$x\mapsto x/1$$. Unfortunately, $$\epsilon$$ need not be injective in general; the reason is obvious and is captured in the following proposition.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> In the above situation, $$\epsilon(x)=0$$ if and only if there exists $$s\in S$$ such that $$sx=0$$. In particular, if $$M$$ is finitely generated, then $$S^{-1}M=0$$ if and only if $$M$$ is annihilated by $$S$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

If

$$\epsilon(x)=x/1=0=0/1$$

then there exists $$s\in S$$ such that

$$s(1x-0\cdot1)=sx=0$$

The above argument also works in the reverse direction.

</details>

## Localization of Rings

The simplest example of localization is the ring of fractions examined in [[Algebraic Structures] §Field of Fractions, ⁋Definition 2](/en/math/algebraic_structures/field_of_fractions#def2). Here we take $$M=A$$. In particular, we also saw that if $$A$$ is an integral domain, then its ring of fractions $$\Frac(A)$$ is a field. ([[Algebraic Structures] §Field of Fractions, ⁋Proposition 6](/en/math/algebraic_structures/field_of_fractions#prop6))

As another example, again taking $$M=A$$ and letting $$S=A\setminus \mathfrak{p}$$ for a prime ideal $$\mathfrak{p}$$ of $$A$$, we can consider $$A_\mathfrak{p}=S^{-1}A$$. Using [Definition 4](#def4) we can apply this to any $$A$$-module $$M$$, and the resulting $$A$$-module is denoted $$M_\mathfrak{p}$$.

Both of the above examples carry a multiplication structure in addition to the addition and scalar multiplication by $$A$$ defined in [Definition 4](#def4). Explicitly, this structure is given by

$$\frac{x}{s}\frac{x'}{s'}=\frac{xx'}{ss'}$$

so we can regard $$S^{-1}A$$ as an $$A$$-algebra.

The localization of a ring has the following universal property.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> Fix rings $$A,B$$ and a multiplicative subset $$S$$ of $$A$$. If the image $$f(S)\subseteq B$$ of a ring homomorphism $$f:A \rightarrow B$$ satisfies $$f(S)\subseteq B^\times$$, then there exists a unique ring homomorphism $$\overline{f}: S^{-1}A \rightarrow B$$ such that $$\overline{f}\circ\epsilon=f$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Suppose $$f$$ satisfying the given condition is given. If $$\overline{f}: S^{-1}A \rightarrow B$$ satisfying the given condition exists, then for any $$a/s\in S^{-1}A$$ we must have

$$\overline{f}\left(\frac{a}{s}\right)=\overline{f}\left(\frac{a}{1}\frac{1}{s}\right)=\overline{f}(\epsilon(a)\epsilon(s)^{-1})=\overline{f}(\epsilon(a))\overline{f}(\epsilon(s)^{-1})=f(a)f(s)^{-1}$$

so if $$\overline{f}$$ exists it is uniquely determined by the above formula. It remains to show that $$\overline{f}: S^{-1}A \rightarrow B$$ defined by $$\overline{f}(a/s)=f(a)f(s)^{-1}$$ is a ring homomorphism, which is a straightforward calculation.

</details>

From this the functoriality of localization can also be shown.

## Localization and Ideals

Meanwhile, there is a specific relationship between localization and ideals. First we define the following.

<div class="definition" markdown="1">

<ins id="def7">**Definition 7**</ins> For a ring homomorphism $$f:A \rightarrow B$$, an ideal $$\mathfrak{a}$$ of $$A$$, and an ideal $$\mathfrak{b}$$ of $$B$$, we define the following.

1. The *contraction* of $$\mathfrak{b}$$ under $$f$$ is the ideal $$f^{-1}(\mathfrak{b})$$ of $$A$$, denoted $$\mathfrak{b}^c$$.
2. The *extension* of $$\mathfrak{a}$$ under $$f$$ is the ideal of $$B$$ generated by the image $$f(\mathfrak{a})$$, denoted $$\mathfrak{a}^e$$.

</div>

To make the first definition we should prove that $$f^{-1}(\mathfrak{b})$$ is an ideal, but this proof is easy. While the above notation is useful, it is relatively less intuitive, so after this post we will write $$f^{-1}(\mathfrak{b})$$ and $$f(\mathfrak{a})B$$ instead.

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8**</ins> For any ring $$A$$, multiplicative subset $$S$$, localization $$S^{-1}A$$, and canonical map $$\epsilon:A \rightarrow S^{-1}A$$, the following hold.

1. For any ideal $$\mathfrak{b}\subset S^{-1}A$$, we have $$\mathfrak{b}=\mathfrak{b}^{ce}$$.
2. For any ideal $$\mathfrak{a}\subset A$$,
  
    $$\mathfrak{a}^{ec}=\{a\in A\mid\text{there exists $s\in S$ satisfying $sa\in \mathfrak{a}$}\}$$
  
    holds. In particular, $$\mathfrak{a}^e=S^{-1}A$$ if and only if $$\mathfrak{a}\cap S\neq\emptyset$$.

Therefore, there is an inclusion-preserving bijection between the prime ideals of $$S^{-1}A$$ and the prime ideals of $$A$$ that do not meet $$S$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

1. First, $$\mathfrak{b}^{ce}\subseteq \mathfrak{b}$$ always holds in general. For the reverse direction, let $$a/s\in \mathfrak{b}$$. Then $$s(a/s)=a/1$$ must belong to $$\mathfrak{b}$$, so $$a\in \mathfrak{b}^c$$. Hence $$a/1\in \mathfrak{b}^{ce}$$, and from this we see $$a/s=(1/s)(a/1)\in \mathfrak{b}^{ce}$$.
2. Let us denote the right-hand side of the given equation by $$\mathfrak{a}'$$ for convenience. Then first, for any $$a'\in \mathfrak{a}'$$, there exists $$s$$ such that $$sa'\in \mathfrak{a}$$. From $$a'/1=sa'/s\in \mathfrak{a}^e$$ we see that $$a'\in \mathfrak{a}^{ec}$$. Conversely, for any $$a\in \mathfrak{a}^{ec}$$, we can find $$a\in \mathfrak{a}$$ and $$s\in S$$ satisfying $$a/1=a'/s$$. Then there exists suitable $$t\in S$$ such that $$tsa=ta'\in \mathfrak{a}$$, and since $$ts\in S$$ we have $$a\in \mathfrak{a}'$$ by definition. Also
  
  $$\mathfrak{a}^e=S^{-1}A\iff 1/1\in \mathfrak{a}^e\iff 1\in \mathfrak{a}^{ec}\iff \text{there exists $s\in S$ s.t. $s1\in \mathfrak{a}$}\iff \mathfrak{a}\cap S\neq \emptyset$$

Now from (2), given any $$\mathfrak{b}\subseteq S^{-1}A$$ we know that $$\mathfrak{b}^c$$ is a prime ideal of $$A$$ not meeting $$S$$. ([[Algebraic Structures] §Field of Fractions, ⁋Proposition 9](/en/math/algebraic_structures/field_of_fractions#prop9)) Conversely, let $$\mathfrak{a}\subseteq A$$ be a prime ideal of $$A$$ not meeting $$S$$. Then $$\mathfrak{a}^e$$ is a prime ideal of $$S^{-1}A$$. Suppose $$(b/t)(b'/t')\in \mathfrak{a}^e$$ for arbitrary $$b/t,b'/t'$$. Then there exist $$a\in \mathfrak{a}$$ and $$s\in S$$ such that $$(bb')/(tt')=a/s$$, and hence there exists $$u\in S$$ such that $$utt'a=usbb'\in \mathfrak{a}$$. Since $$\mathfrak{a}\cap S=\emptyset$$ we know $$us\not\in \mathfrak{a}$$, and since $$\mathfrak{a}$$ is a prime ideal we have $$bb'\in \mathfrak{a}$$. Therefore $$b\in \mathfrak{a}$$ or $$b'\in \mathfrak{a}$$, and $$\mathfrak{a}^e$$ is a prime ideal. That these correspondences are mutual inverses follows naturally from the result of (2).

</details>

The following is immediate from the above proposition.

<div class="proposition" markdown="1">

<ins id="cor9">**Corollary 9**</ins> The localization of a Noetherian ring is Noetherian.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Given an ascending chain of ideals of $$S^{-1}A$$

$$\mathfrak{b}_0\subseteq \mathfrak{b}_1\subseteq\cdots$$

we have

$$\mathfrak{b}_0^c\subseteq \mathfrak{b}_1^c\subseteq\cdots$$

which is an ascending chain of ideals in the Noetherian ring $$A$$, so there exists $$N$$ such that for all $$n>N$$ we have $$\mathfrak{b}_n^c=\mathfrak{b}_{n+1}^c$$. Now for such $$n$$,

$$\mathfrak{b}_n=\mathfrak{b}_n^{ce}=\mathfrak{b}_{n+1}^{ce}=\mathfrak{b}_{n+1}$$

</details>

Meanwhile, from [Proposition 8](#prop8), for any prime ideal $$\mathfrak{p}$$ of $$A$$ it is immediate that $$\mathfrak{p}^e=\mathfrak{p}A_\mathfrak{p}$$ is the unique *maximal* ideal of $$A_\mathfrak{p}$$. That is, $$A_\mathfrak{p}$$ is a local ring, and its quotient field $$A_\mathfrak{p}/\mathfrak{p}A_\mathfrak{p}$$ is well-defined.

<div class="definition" markdown="1">

<ins id="def10">**Definition 10**</ins> For a ring $$A$$ and a prime ideal $$\mathfrak{p}$$, we call the field $$A_\mathfrak{p}/\mathfrak{p}A_\mathfrak{p}$$ the *residue field* of $$A$$ at $$\mathfrak{p}$$ and denote it by $$\kappa(\mathfrak{p})$$.

</div>

---

**References**

**[Eis]** David Eisenbud. *Commutative Algebra: with a view toward algebraic geometry*. Springer, 1995.

---
