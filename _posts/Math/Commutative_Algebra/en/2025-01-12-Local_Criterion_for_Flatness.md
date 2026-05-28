---
title: "Flatness and Localization"
excerpt: "A local criterion for flatness via checking at the maximal ideal"

categories: [Math / Commutative Algebra]
permalink: /en/math/commutative_algebra/local_criterion_for_flatness
header:
    overlay_image: /assets/images/Math/Commutative_Algebra/Local_Criterion_for_Flatness.png
    overlay_filter: 0.5
sidebar: 
    nav: "commutative_algebra-en"

date: 2025-01-12
last_modified_at: 2025-01-12
weight: 13

toc: false
translated_at: 2026-05-28T11:36:15+00:00
translation_source: kimi-cli
---
In the previous post we saw several criteria for determining when an $$A$$-module $$M$$ is flat, and in this post we examine a criterion for determining this specifically through localization. The following theorem shows that it suffices to check [§Flatness, ⁋Proposition 1](/en/math/commutative_algebra/flatness#prop1) only for the maximal ideal.

<div class="proposition" markdown="1">

<ins id="thm1">**Theorem 1**</ins> Fix a Noetherian local ring $$(A, \mathfrak{m})$$, and assume that $$(E, \mathfrak{n})$$ is a local Noetherian $$A$$-algebra satisfying $$\mathfrak{m}E\subseteq \mathfrak{n}$$. Then for a finitely generated $$E$$-module $$M$$, $$M$$ being a flat $$A$$-module is equivalent to $$\Tor_1^A(A/\mathfrak{m}, M)=0$$. 

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

If $$M$$ is a flat $$A$$-module then $$\Tor_1^A(A/\mathfrak{m}, M)=0$$ is exactly the content of [§Flatness, ⁋Proposition 1](/en/math/commutative_algebra/flatness#prop1), so it suffices to show the converse. 

To show the converse, we likewise use [§Flatness, ⁋Proposition 1](/en/math/commutative_algebra/flatness#prop1), assume the given condition, and show that for any ideal $$\mathfrak{a}$$ of $$A$$ the multiplication map $$m:\mathfrak{a}\otimes_AM \rightarrow M$$ is injective. To this end, assume $$x\in \mathfrak{a}\otimes_AM$$ lies in the kernel $$\ker m$$ of the multiplication map, and let us show $$x=0$$. First, from the $$E$$-module structure defined on $$M$$ we naturally obtain an $$E$$-module structure on $$\mathfrak{a}\otimes_AM$$ as well, and from the assumption $$\mathfrak{m}E\subseteq \mathfrak{n}$$ we know that for any $$n$$ the formula

$$\mathfrak{m}^n(\mathfrak{a}\otimes_AM )\subseteq \mathfrak{n}^n(\mathfrak{a}\otimes_AM)$$	 

holds. On the other hand, since these are finitely generated $$E$$-modules, [§Blowup Algebras, ⁋Corollary 8 (Krull intersection theorem)](/en/math/commutative_algebra/blowup_algebra#cor8) gives

$$\bigcap \mathfrak{m}^n(\mathfrak{a}\otimes_AM)=\bigcap \mathfrak{n}^n(\mathfrak{a}\otimes_AM)=0$$

Therefore, to show $$x=0$$ it suffices to show that $$x\in \mathfrak{m}^n(\mathfrak{a}\otimes_AM)$$ holds for all $$n$$. On the other hand, $$\mathfrak{m}^n(\mathfrak{a}\otimes_AM)$$ can be identified with $$(\mathfrak{m}^n \mathfrak{a})\otimes_AM$$, and applying [§Blowup Algebras, ⁋Lemma 7 (Artin-Rees)](/en/math/commutative_algebra/blowup_algebra#lem7) to the following $$\mathfrak{m}$$-stable filtration

$$\mathfrak{m}\supseteq \mathfrak{m}^2\supseteq\cdots$$

and $$M'=\mathfrak{a}$$, the following filtration

$$\mathfrak{m}\cap \mathfrak{a}\supseteq \mathfrak{m}^2 \cap\mathfrak{a}\supseteq\cdots$$

is also $$\mathfrak{m}$$-stable, so there exists a suitable $$N$$ such that whenever $$m>N$$,

$$\mathfrak{m}^{m+i}\cap \mathfrak{a}=\mathfrak{m}^i(\mathfrak{m}^m\cap \mathfrak{a})$$

holds for all $$i$$. Thus whenever any $$n$$ is given, if we choose $$t>N+n$$ then

$$\mathfrak{m}^t\cap \mathfrak{a}=\mathfrak{m}^n(\mathfrak{m}^{t-n}\cap \mathfrak{a})\subseteq \mathfrak{m}^n \mathfrak{a}$$

and instead of showing that $$x\in (\mathfrak{m}^na)\otimes_AM$$ holds for arbitrary $$n$$, we may show that $$x\in (\mathfrak{m}^t\cap \mathfrak{a})\otimes_AM$$ holds for arbitrary $$t$$. 

Now applying $$-\otimes_AM$$ to the following short exact sequence

$$0 \rightarrow \mathfrak{m}^t\cap \mathfrak{a} \rightarrow \mathfrak{a} \rightarrow \frac{\mathfrak{a}}{\mathfrak{m}^t\cap \mathfrak{a}} \rightarrow 0$$

we obtain the following exact sequence

$$(\mathfrak{m}^t\cap \mathfrak{a})\otimes_AM \rightarrow \mathfrak{a}\otimes_AM \rightarrow \frac{\mathfrak{a}}{\mathfrak{m}^t\cap \mathfrak{a}}\otimes_AM \rightarrow 0$$

and in this situation it suffices to show that $$x$$ becomes $$0$$ when mapped to $$(\mathfrak{a}/\mathfrak{m}^t\cap \mathfrak{a})\otimes_AM$$. On the other hand, considering the following commutative diagram

![inclusions](/assets/images/Math/Commutative_Algebra/Local_Criterion_for_Flatness-1.png){:style="width:10em" class="invert" .align-center}

and applying $$-\otimes_AM$$ to obtain the following commutative diagram

![trick](/assets/images/Math/Commutative_Algebra/Local_Criterion_for_Flatness-2.png){:style="width:16em" class="invert" .align-center}

the left map $$\mathfrak{a}\otimes_AM \rightarrow M$$ is the multiplication map $$m$$, and therefore $$x\in\ker m$$ is sent to $$0$$ through the composition in the $$\llcorner$$ direction. Thus it suffices to show that the right map $$(\mathfrak{a}/(\mathfrak{m}^t\cap I))\otimes_AM \rightarrow (A/\mathfrak{m}^t)\otimes_AM$$ is injective. Through the isomorphism

$$\frac{\mathfrak{a}}{\mathfrak{m}^t\cap \mathfrak{a}}\cong \frac{\mathfrak{a}+\mathfrak{m}^t}{\mathfrak{m}^t}$$

the map $$\mathfrak{a}/(\mathfrak{m}^t\cap \mathfrak{a}) \rightarrow A/\mathfrak{m}^t$$ giving this is exactly the left map of the following short exact sequence

$$0 \rightarrow \frac{\mathfrak{a}+\mathfrak{m}^t}{\mathfrak{m}^t} \rightarrow \frac{A}{\mathfrak{m}^t}\rightarrow \frac{A}{\mathfrak{a}+\mathfrak{m}^t} \rightarrow 0$$

Therefore, from the $$\Tor$$ long exact sequence

$$\cdots \Tor_1^A(A/(\mathfrak{a}+\mathfrak{m}^t), M) \rightarrow \frac{\mathfrak{a}+\mathfrak{m}^t}{\mathfrak{m}^t}\otimes_AM \rightarrow \frac{A}{\mathfrak{m}^t}\otimes_AM \rightarrow$$

what we must show is $$\Tor_1^A(A/(\mathfrak{a}+\mathfrak{m}^t), M)=0$$. 

Now $$A/(\mathfrak{a}+\mathfrak{m}^t)$$ is annihilated by $$\mathfrak{m}^t$$, and since $$\mathfrak{m}^t$$ is finitely generated, through this we know that $$A/(\mathfrak{a}+\mathfrak{m}^t)$$ has finite length. Therefore, if we show more generally that $$\Tor_1^A(N, M)=0$$ holds whenever any $$A$$-module $$N$$ of finite length is given, we obtain what we want.

We proceed by induction. If $$N$$ has length $$1$$ then by the discussion after [§The Jordan-Hölder Theorem, ⁋Definition 1](/en/math/commutative_algebra/Jordan-Holder_theorem#def1) we must have $$N=A/\mathfrak{m}$$, and thus $$\Tor_1^A(N, M)=0$$ coincides exactly with the hypothesis of the theorem. Choose an $$A$$-module $$N$$ of finite length and any proper submodule $$N'$$ of $$N$$. Then applying the $$\Tor$$ long exact sequence to the exact sequence

$$0 \rightarrow N' \rightarrow N \rightarrow N/N' \rightarrow 0$$

we obtain

$$\cdots \rightarrow\Tor_1^A(N', M) \rightarrow \Tor_1^A(N, M) \rightarrow \Tor_1^A(N/N', M) \rightarrow \cdots$$

Now by the inductive hypothesis $$\Tor_1^A(N', M)=\Tor_1^A(N/N',M)=0$$, so we obtain the desired result.

</details>

On the other hand, if $$M$$ is a flat $$A$$-module then for any $$A/(a)$$-module $$N$$,

$$(M/aM)\otimes_{A/(a)}N=(A/(x)\otimes_A M)\otimes_{A/(a)} N\cong M\otimes_AN$$

so $$M/aM$$ is a flat $$A/(a)$$-module without any additional conditions. In [Corollary 3](#cor3) we prove the converse of this claim assuming the conditions of [Theorem 1](#thm1). For this we first need the following lemma.

<div class="proposition" markdown="1">

<ins id="lem2">**Lemma 2**</ins> Let an $$A$$-module $$M$$ be given, and let $$a\in A$$ be a non-zerodivisor on both $$A$$ and $$M$$. Then for any $$A/(a)$$-module $$N$$,

$$\Tor_i^{A/(a)}(N, M/aM)=\Tor_i^A(N,M)$$

holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Considering a free resolution of the $$A$$-module $$M$$

$$\cdots \rightarrow F_2 \rightarrow F_1 \rightarrow F_0\tag{1}$$

by definition the $$i$$-th homology of the following chain complex

$$\cdots \rightarrow N\otimes_A F_2 \rightarrow N\otimes_AF_1 \rightarrow N\otimes_A F_0$$

is $$\Tor_i^A(M,N)$$. On the other hand, consider the following complex obtained by applying $$A/(a)\otimes_A-$$ to (1)

$$\cdots \rightarrow F_2/aF_2 \rightarrow F_1/aF_1 \rightarrow F_0/aF_0 \rightarrow M/aM \rightarrow 0\tag{2}$$

Then the homology of this complex is given by

$$\Tor_i^A(A/(a), M)=\begin{cases} M/aM&\text{if $i=0$}\\ 0&\text{otherwise}\end{cases}$$

so this becomes a free resolution of $$M/aM$$. Therefore, to compute $$\Tor_i^{A/(a)}(N, M/aM)$$ using (2), we obtain the desired result through the following isomorphism

$$N\otimes_{A/(a)} F_i/aF_i=N\otimes_{A/(a)} ((A/(a))\otimes_A F_i)\cong N\otimes_A F_i$$

</details>

Using this we can show the following.

<div class="proposition" markdown="1">

<ins id="cor3">**Corollary 3**</ins> Fix a Noetherian local ring $$(A, \mathfrak{m})$$, and assume that $$(E, \mathfrak{n})$$ is a local Noetherian $$A$$-algebra satisfying $$\mathfrak{m}E\subseteq \mathfrak{n}$$. If $$a\in \mathfrak{m}$$ is a non-zerodivisor in $$A$$ and simultaneously a zerodivisor on the finitely generated $$E$$-module $$M$$, then $$M$$ being a flat $$A$$-module is equivalent to $$M/aM$$ being a flat $$A/(a)$$-module. 

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Assume $$M/aM$$ is a flat $$A/(a)$$-module. For the residue field $$A/\mathfrak{m}$$ of $$A$$, from the assumption

$$\Tor_1^{A/(a)}(A/\mathfrak{m}, M/aM)=0$$

holds, and now applying [Lemma 2](#lem2) we know that $$\Tor_1^A(A/\mathfrak{m}, M)=0$$ holds. Therefore by [Theorem 1](#thm1), $$M$$ is a flat $$A$$-module.

</details>

## Rees algebra

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> For a ring $$A$$ and an ideal $$\mathfrak{a}$$, the *Rees algebra* is

$$A[\mathfrak{a}t]=\bigoplus_{n=0}^\infty \mathfrak{a}^n t^n\subseteq A[t]$$

Also, in the same situation the *extended Rees algebra* is defined as

$$A[\mathfrak{a}t, t^{-1}]=\bigoplus_{n=-\infty}^\infty \mathfrak{a}^nt^n\subseteq A[t, t^{-1}]$$

</div>

Then the following corollary is almost obvious.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> Fix a field $$\mathbb{K}$$ and a $$\mathbb{K}$$-algebra $$A$$. Then the Rees algebra $$A[\mathfrak{a}t, t^{-1}]$$ is a flat $$\mathbb{K}[t]$$-module. Also, if $$\bigcap \mathfrak{a}^i=0$$, then elements of the form $$1-t s$$ ($$s\in S$$) are all non-zerodivisors in $$A[\mathfrak{a}t, t^{-1}]$$. 

</div>
