---
title: "Dimension"
description: "This post introduces the definition of Krull dimension in commutative algebra, defines the concepts of ideals and codimension, and discusses dimension calculations in Noetherian rings."
excerpt: "Krull dimension, defined by prime chains, and its basic properties"

categories: [Math / Commutative Algebra]
permalink: /en/math/commutative_algebra/Krull_dimension
header:
    overlay_image: /assets/images/Math/Commutative_Algebra/Krull_Dimension.png
    overlay_filter: 0.5
sidebar: 
    nav: "commutative_algebra-en"

date: 2025-01-16
last_modified_at: 2025-01-16
weight: 16
translated_at: 2026-05-31T00:00:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-31T00:00:04+00:00
---
## Definition of Dimension

In the next few posts we define the dimension of a ring and study its properties. The definition itself is not difficult.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> The *Krull dimension* of a ring $$A$$ is defined as the supremum of the lengths $$r$$ of descending chains of prime ideals of $$A$$

$$\mathfrak{p}_r\supseteq \mathfrak{p}_{r-1}\supseteq\cdots\supseteq \mathfrak{p}_1\supseteq \mathfrak{p}_0$$

and is denoted by $$\dim A$$. If no such $$r$$ exists, we define $$\dim A=\infty$$.

</div>

For short, we call the Krull dimension of a ring $$A$$ simply the dimension of $$A$$. For example, a field $$\mathbb{K}$$ has only the prime ideal $$(0)$$, so $$\mathbb{K}$$ is always $$0$$-dimensional.

More generally, we make the following definition.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> For an ideal $$\mathfrak{a}$$ of a ring $$A$$, the dimension of $$\mathfrak{a}$$ is defined by

$$\dim \mathfrak{a}=\dim A/\mathfrak{a}$$

For a prime ideal $$\mathfrak{p}$$ of $$A$$, the *codimension* $$\codim \mathfrak{p}$$ of $$\mathfrak{p}$$ is defined as the dimension of $$A_\mathfrak{p}$$; for a general ideal $$\mathfrak{a}$$, $$\codim \mathfrak{a}$$ is defined as the minimum of the codimensions of the prime ideals containing $$\mathfrak{a}$$.

Finally, for any $$A$$-module $$M$$, the dimension and codimension of $$M$$ are defined respectively as the dimension and codimension of $$\ann(M)$$.

</div>

One point requiring some care: according to the definition above, $$\mathfrak{a}$$ acquires two notions of dimension—the dimension as an ideal defined first, and the dimension when regarded as an $$A$$-module—and these two may give different values. Therefore, when we use the notation $$\dim \mathfrak{a}$$, we agree that it refers only to the dimension as an ideal of $$A$$, as defined first in [Definition 2](#def2).

Then by [§Localization, ⁋Proposition 8](/en/math/commutative_algebra/localization#prop8), $$\codim \mathfrak{p}$$ equals the supremum of the lengths of decreasing chains starting from the prime ideal $$\mathfrak{p}$$

$$\mathfrak{p}=\mathfrak{p}_r\supseteq \mathfrak{p}_{r-1}\supseteq\cdots\supseteq \mathfrak{p}_1\supseteq \mathfrak{p}_0$$

Hence the inequality

$$\dim \mathfrak{a}+\codim \mathfrak{a}\leq \dim A$$

holds. Despite its name, the reverse inequality does not hold in general.

On the other hand, for a local ring $$(A, \mathfrak{m})$$, we can always prepend $$\mathfrak{m}$$ to the beginning of any chain of prime ideals giving $$\dim A$$, so necessarily $$\dim A=\codim \mathfrak{m}$$.

## Computation of Dimension

In general, when we treat dimension we mainly consider the case where the ring $$A$$ is noetherian. One of the principal reasons is that [Theorem 7](#thm7) holds only for noetherian rings. Before computing dimensions in earnest, let us first look at a simple example.

First, through the equivalence between the first and third conditions of [§The Jordan-Hölder Theorem, ⁋Theorem 4](/en/math/commutative_algebra/Jordan-Holder_theorem#thm4), we know exactly what $$0$$-dimensional noetherian rings are.

<div class="proposition" markdown="1">

<ins id="cor3">**Corollary 3**</ins> For a noetherian ring $$A$$, $$\dim A =0$$ is equivalent to $$A$$ being artinian.

</div>

On the other hand, by the following proposition we know that in general, if $$\phi:A \rightarrow B$$ is integral, then dimension does not change.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> Let $$\phi: A \rightarrow B$$ be integral. Then for any prime ideal $$\mathfrak{p}$$ of $$A$$ containing $$\ker\phi$$, there exists a prime ideal $$\mathfrak{q}$$ of $$B$$ such that $$\mathfrak{p}=\phi^{-1} \mathfrak{q}$$. Moreover, for any ideal $$\mathfrak{b}$$ of $$B$$, $$\dim \mathfrak{b}=\dim \phi^{-1} \mathfrak{b}$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

The first statement is simply [§Integral Extensions and Ideals, ⁋Proposition 1](/en/math/commutative_algebra/lying_over_and_going_up#prop1). For the second, $$\dim \mathfrak{b}\geq \dim \phi^{-1}\mathfrak{b}$$ holds by the second statement of [§Integral Extensions and Ideals, ⁋Proposition 1](/en/math/commutative_algebra/lying_over_and_going_up#prop1), and the reverse inequality holds by [§Integral Extensions and Ideals, ⁋Corollary 4](/en/math/commutative_algebra/lying_over_and_going_up#cor4).

</details>

Now we turn our attention to what happens in dimension one. Before that, we give the following somewhat technical definition.

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> For a prime ideal $$\mathfrak{p}\subseteq A$$, we define the *$$n$$th symbolic power* $$\mathfrak{p}^{(n)}$$ of $$\mathfrak{p}$$ by the formula

$$\mathfrak{p}^{(n)}=\{a\in A\mid\text{$ba\in \mathfrak{p}^n$ for some $b\in A\setminus \mathfrak{p}$}\}$$

</div>

By definition, $$\mathfrak{p}^{(n)}$$ is the inverse image in $$A$$ of the ideal $$(\mathfrak{p}A_\mathfrak{p})^n$$ under the localization $$A \rightarrow A_\mathfrak{p}$$. Then elements outside $$\mathfrak{p}$$ become non-zerodivisors modulo $$\mathfrak{p}^({n})$$, and it is clear that $$\mathfrak{p}^{(n)}A_\mathfrak{p}=(\mathfrak{p}A_\mathfrak{p})^n$$. Moreover, there is a descending chain of symbolic powers

$$A=\mathfrak{p}^{(0)}\supseteq \mathfrak{p}=\mathfrak{p}^{(1)}\supseteq \mathfrak{p}^{(2)}\supseteq \mathfrak{p}^{(3)}\supseteq\cdots$$

Now we can prove the following theorem.

<div class="proposition" markdown="1">

<ins id="thm6">**Theorem 6 (Codimension one Principal Ideal Theorem)**</ins> Let $$A$$ be a noetherian ring and let $$a\in A$$ be arbitrary. Let $$\mathfrak{p}$$ be minimal among the prime ideals containing the principal ideal $$\mathfrak{a}=(a)$$. Then $$\codim \mathfrak{p}\leq 1$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

It suffices to show that $$\codim \mathfrak{q}=0$$ for any prime ideal $$\mathfrak{q}\subsetneq \mathfrak{p}$$, and by [§Localization, ⁋Proposition 8](/en/math/commutative_algebra/localization#prop8) this is equivalent to showing that $$\dim A_\mathfrak{q}=0$$.

Now in $$A_\mathfrak{p}$$, $$\mathfrak{p}A_\mathfrak{p}$$ is the unique maximal ideal, so $$\mathfrak{p}$$ contains the ideals $$\mathfrak{q}A_\mathfrak{p}$$, $$(\mathfrak{q}A_\mathfrak{p})^{(n)}$$, and $$\mathfrak{a}A_\mathfrak{p}$$. In particular, we obtain the two chains

$$\mathfrak{a}A_\mathfrak{p}\subseteq (\mathfrak{q}A_\mathfrak{p})^{(n)}+\mathfrak{a}A_\mathfrak{p}\subseteq \mathfrak{p}A_\mathfrak{p},\qquad \mathfrak{q}A_\mathfrak{p}\subseteq \mathfrak{p}A_\mathfrak{p}$$

On the other hand, since $$\mathfrak{p}A_\mathfrak{p}$$ is minimal among prime ideals containing $$\mathfrak{a}A_\mathfrak{p}$$, by [§The Jordan-Hölder Theorem, ⁋Corollary 8](/en/math/commutative_algebra/Jordan-Holder_theorem#cor8) the quotient $$A_\mathfrak{p}/\mathfrak{a}A_\mathfrak{p}$$ is artinian. Hence the descending chain of symbolic powers

$$(\mathfrak{q}A_\mathfrak{p})^{(1)}+\mathfrak{a}A_\mathfrak{p}\supseteq (\mathfrak{q}A_\mathfrak{p})^{(2)}+\mathfrak{a}A_\mathfrak{p}\supseteq\cdots $$

must terminate. Suppose that $$(\mathfrak{q}A_\mathfrak{p})^{(n)}+\mathfrak{a}A_\mathfrak{p}= (\mathfrak{q}A_\mathfrak{p})^{(n+1)}+\mathfrak{a}A_\mathfrak{p}$$. Then

$$(\mathfrak{q}A_\mathfrak{p})^{(n)}\subseteq (\mathfrak{q}A_\mathfrak{p})^{(n)}+\mathfrak{a}A_\mathfrak{p}= (\mathfrak{q}A_\mathfrak{p})^{(n+1)}+\mathfrak{a}A_\mathfrak{p}$$

so any $$f\in (\mathfrak{q}A_\mathfrak{p})^{(n)}$$ can be written in the form

$$f=\alpha a+g,\qquad g\in (\mathfrak{q}A_\mathfrak{p})^{(n+1)}=(\mathfrak{q}A_\mathfrak{p})^{(n)}$$

and from this $$\alpha a\in (\mathfrak{q}A_\mathfrak{p})^{(n)}$$. But in this expression, since $$\mathfrak{p}$$ is minimal among primes containing $$\mathfrak{a}$$, we have $$a\not\in \mathfrak{q}$$ and therefore $$\alpha\in (\mathfrak{q}A_\mathfrak{p})^{(n)}$$. That is,

$$(\mathfrak{q}A_\mathfrak{p})^{(n)}=\mathfrak{a}(\mathfrak{q}A_\mathfrak{p})^{(n)}+(\mathfrak{q}A_\mathfrak{p})^{(n+1)}$$

holds. Now passing to $$A_\mathfrak{p}/(\mathfrak{q}A_\mathfrak{p})^{(n+1)}$$,

$$(\mathfrak{q}A_\mathfrak{p})^{(n)}=\mathfrak{a}(\mathfrak{q}A_\mathfrak{p})^{(n)}\pmod{\mathfrak{q}^{(n+1)}}$$

and since $$a\in \mathfrak{p}A_\mathfrak{p}=J(A_\mathfrak{p})$$, by [§Integral Extensions, ⁋Lemma 8](/en/math/commutative_algebra/integral_extension#lem8) we have $$(\mathfrak{q}A_\mathfrak{p})^{(n)}=0\pmod{(\mathfrak{q}A_\mathfrak{p})^{(n+1)}}$$. That is, $$(\mathfrak{q}A_\mathfrak{p})^{(n)}=(\mathfrak{q}A_\mathfrak{p})^{(n+1)}$$. Localizing this equation at $$\mathfrak{q}$$,

$$(\mathfrak{q}A_\mathfrak{q})^{n+1}=(\mathfrak{q}A_\mathfrak{q})^{n}$$

and since $$\mathfrak{q}A_\mathfrak{q}=J(A_\mathfrak{q})$$, we have $$(\mathfrak{q}A_\mathfrak{q})^{n}=0$$. From the equivalence of the second and third conditions of [§The Jordan-Hölder Theorem, ⁋Corollary 8](/en/math/commutative_algebra/Jordan-Holder_theorem#cor8), $$A_\mathfrak{q}=A_\mathfrak{q}/(0)$$ is artinian, and therefore by [Corollary 3](#cor3) we know that $$\dim A_\mathfrak{q}=0$$.

</details>

Now using this, we can inductively prove the following.

<div class="proposition" markdown="1">

<ins id="thm7">**Theorem 7 (Principal Ideal Theorem)**</ins> Let $$A$$ be a noetherian ring and let $$a_1,\ldots, a_c\in A$$ be arbitrary. Let $$\mathfrak{p}$$ be minimal among the prime ideals containing $$a_1,\ldots, a_c$$. Then $$\codim \mathfrak{p}\leq c$$.

</div>

That is, in a noetherian ring any prime ideal satisfies the descending chain condition, and the length of a chain starting from $$\mathfrak{p}$$ is at most the number of generators of the ideal it minimally contains. Nevertheless, there exist noetherian rings of infinite dimension. (**[Nag, Appendix, Example 1]**)

On the other hand, [Theorem 7](#thm7) also admits the following converse.

<div class="proposition" markdown="1">

<ins id="cor8">**Corollary 8**</ins> In a noetherian ring $$A$$, a prime ideal $$\mathfrak{p}$$ of codimension $$c$$ is minimal among the prime ideals containing some ideal generated by $$c$$ elements.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Suppose that $$\mathfrak{p}$$ has codimension $$c$$, as claimed. We will construct the desired ideal by inductively choosing elements $$x_1,\ldots, x_r$$, starting from the zero ideal $$(0)$$ (generated by $$0$$ elements). Now suppose that for some $$r$$ satisfying $$0\leq r< c$$, we have constructed the ideal generated by $$x_1,\ldots, x_r$$. Then we must choose a suitable $$x_{r+1}\in \mathfrak{p}$$ not belonging to any of the prime ideals containing the ideal $$(x_1,\ldots, x_r)$$.

Now let $$\mathfrak{q}_1,\ldots, \mathfrak{q}_s$$ be the minimal prime ideals containing $$(x_1,\ldots, x_r)$$. By [Theorem 7](#thm7), the codimension of each $$\mathfrak{q}_i$$ is at most $$r$$, and since $$r< c$$, their codimensions are all strictly less than $$c$$. Therefore $$\mathfrak{p}$$ cannot equal any of them, and in particular $$\mathfrak{p}\not\subseteq \bigcup_{i=1}^s \mathfrak{q}_i$$. Thus we can choose $$x_{r+1}\in \mathfrak{p}\setminus \bigcup_{i=1}^s \mathfrak{q}_i$$.

By induction we now obtain $$c$$ elements $$x_1,\ldots, x_c$$ belonging to $$\mathfrak{p}$$. Then choosing a minimal prime ideal $$\mathfrak{q}$$ containing the ideal $$(x_1,\ldots, x_c)$$, by [Theorem 7](#thm7) we have $$\codim \mathfrak{q}\leq c$$. On the other hand, since $$\mathfrak{q}\subseteq \mathfrak{p}$$ and $$\codim \mathfrak{p}=c$$, we must have $$\mathfrak{q}=\mathfrak{p}$$.

</details>

If in the above corollary $$\codim \mathfrak{p}=0$$, then $$\mathfrak{p}$$ is a minimal prime containing the ideal generated by $$0$$ elements, that is, the zero ideal. Now by [§Associated Primes, ⁋Theorem 7](/en/math/commutative_algebra/associated_primes#thm7), such a prime ideal consists entirely of zerodivisors. Combining this with [Theorem 6](#thm6), we see that if $$\mathfrak{p}$$ is a minimal prime ideal containing a non-zerodivisor $$a$$, then necessarily $$\codim \mathfrak{p}=1$$.

In particular, for a minimal prime $$\mathfrak{p}$$ containing a non-zerodivisor $$a$$,

$$\dim A/\mathfrak{p}A+\codim \mathfrak{p}=\dim \mathfrak{p}+\codim \mathfrak{p}\leq \dim A$$

and since $$\codim \mathfrak{p}=1$$,

$$\dim A/\mathfrak{p}A\leq\dim A-1$$

holds.

In particular, we have seen that for a noetherian local ring $$(A, \mathfrak{m})$$, $$\dim A=\codim \mathfrak{m}$$ holds. Therefore, since $$\codim \mathfrak{m}=d$$, by [Corollary 8](#cor8) the maximal ideal $$\mathfrak{m}$$ must be generated by at least $$d$$ elements.

## Dimension in Graded Rings

Let us examine some useful properties for computing dimension in a graded ring $$R = \bigoplus_{d \ge 0} R_d$$. First, recall the following. ([§Localization of Graded Rings](/en/math/commutative_algebra/localization_of_graded_rings))

<div class="definition" markdown="1">

<ins id="def9">**Definition 9**</ins> An ideal $$\mathfrak{a}$$ of a graded ring $$R$$ is called *homogeneous* if it is generated by homogeneous elements. A prime ideal $$\mathfrak{p}$$ is called a *homogeneous prime ideal* if it is a homogeneous ideal and is prime.

</div>

The key observation in a graded ring is that prime ideals containing the irrelevant ideal $$\mathfrak{m} = \bigoplus_{d > 0} R_d$$ are always homogeneous.

<div class="proposition" markdown="1">

<ins id="prop10">**Proposition 10**</ins> In a graded ring $$R$$, any prime ideal $$\mathfrak{p}$$ containing the irrelevant ideal $$\mathfrak{m} = \bigoplus_{d > 0} R_d$$ is homogeneous.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$\mathfrak{p}$$ be a prime ideal with $$\mathfrak{m} \subseteq \mathfrak{p}$$. Consider the *homogenization* of $$\mathfrak{p}$$

$$\mathfrak{p}^* = \{x \in \mathfrak{p} \mid x \text{ homogeneous}\}$$

That this is a graded prime ideal follows immediately from the definition. The key point is that $$\mathfrak{p} = \mathfrak{p}^*$$. First, $$\mathfrak{m} \subseteq \mathfrak{p}^* \subseteq \mathfrak{p}$$ is obvious, so assume $$x \in \mathfrak{p}$$ and let us show that $$x\in \mathfrak{p}^\ast$$.

Write $$x$$ in its homogeneous decomposition $$x = \sum_{d} x_d$$. Since $$x_+ = \sum_{d > 0} x_d \in \mathfrak{m} \subseteq \mathfrak{p}$$, we have $$x_0 = x - x_+ \in \mathfrak{p}$$. Now $$x' = x - x_0 = x_+ \in \mathfrak{p}$$, and in the same way we can show that $$x_1 \in \mathfrak{p}$$. By induction each $$x_d \in \mathfrak{p}$$, and therefore $$x \in \mathfrak{p}^*$$.

</details>

From Proposition 10 we know that prime ideals containing the irrelevant ideal $$\mathfrak{m}$$ are homogeneous. Conversely, homogeneous prime ideals not containing $$\mathfrak{m}$$ correspond to the points of $$\operatorname{Proj} R$$. Now we will show that any prime ideal chain can be refined to a homogeneous prime ideal chain.

<div class="proposition" markdown="1">

<ins id="prop11">**Proposition 11 (Refinement by graded prime ideals)**</ins> Any prime ideal chain in a graded ring $$R$$ can be refined to a homogeneous prime ideal chain. That is, for a prime ideal chain $$\mathfrak{p}_0 \supsetneq \cdots \supsetneq \mathfrak{p}_s$$, there exists a homogeneous prime ideal chain $$\mathfrak{p}_0^* \supsetneq \mathfrak{p}_1^* \supsetneq \cdots \supsetneq \mathfrak{p}_s^*$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Consider a prime ideal chain $$\mathfrak{p}_0 \supsetneq \mathfrak{p}_1 \supsetneq \cdots \supsetneq \mathfrak{p}_s$$. For each $$\mathfrak{p}_i$$, define the ideal generated by its homogeneous elements

$$\mathfrak{p}_i^* = \langle f \in \mathfrak{p}_i : f \text{ is homogeneous} \rangle$$

Each $$\mathfrak{p}_i^*$$ is a homogeneous prime ideal. Also, if $$\mathfrak{p}_i \supsetneq \mathfrak{p}_{i+1}$$ then $$\mathfrak{p}_i^* \supseteq \mathfrak{p}_{i+1}^*$$.

Now let us show that $$\mathfrak{p}_i^* \supseteq \mathfrak{p}_{i+1}^*$$ is a strict inclusion. Since $$\mathfrak{p}_i \supsetneq \mathfrak{p}_{i+1}$$, there exists an element $$f$$ belonging to $$\mathfrak{p}_i \setminus \mathfrak{p}_{i+1}$$. Writing $$f$$ as the sum of homogeneous components $$f = f_{d_1} + \cdots + f_{d_k}$$, at least one of the $$f_{d_j}$$ does not belong to $$\mathfrak{p}_{i+1}$$ (otherwise $$f \in \mathfrak{p}_{i+1}$$). Hence this $$f_{d_j} \in \mathfrak{p}_i^* \setminus \mathfrak{p}_{i+1}^*$$.

Consequently, $$\mathfrak{p}_0^* \supsetneq \mathfrak{p}_1^* \supsetneq \cdots \supsetneq \mathfrak{p}_s^*$$ is a homogeneous prime ideal chain.

</details>

## Regular Local Rings

<div class="definition" markdown="1">

<ins id="def12">**Definition 12**</ins> A noetherian local ring $$(A, \mathfrak{m})$$ is called a *regular local ring* if $$\mathfrak{m}$$ can be generated by exactly $$d$$ elements.

</div>

Then by [§Integral Extensions, ⁋Lemma 8](/en/math/commutative_algebra/integral_extension#lem8), for $$a_1,\ldots, a_d\in \mathfrak{m}$$, their images in $$\mathfrak{m}/\mathfrak{m}^2$$ generate $$\mathfrak{m}/\mathfrak{m}^2$$ as an $$A/\mathfrak{m}$$-vector space if and only if $$a_1,\ldots, a_d$$ generate $$\mathfrak{m}$$ as an $$A$$-module. We will examine further properties of these at the end of the next post.

---

**References**

**[Eis]** David Eisenbud. *Commutative Algebra: with a view toward algebraic geometry*. Springer, 1995.  
**[Nag]** Masayoshi Nagata. *Local Rings*. Interscience publishers, 1962.

---
