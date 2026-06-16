---
title: "Flatness and Localization"
description: "We discuss a criterion for determining whether finitely generated modules over a Noetherian local ring are flat, and show that it suffices to check flatness at the maximal ideal."
excerpt: "A local criterion for flatness via checking at the maximal ideal"

categories: [Math / Commutative Algebra]
permalink: /en/math/commutative_algebra/local_criterion_for_flatness
sidebar: 
    nav: "commutative_algebra-en"

date: 2025-01-12
weight: 13

toc: false
translated_at: 2026-05-30T23:00:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-30T23:00:05+00:00
---
In the previous post we examined several criteria for determining when an $$A$$-module $$M$$ is flat, and in this post we turn to a criterion using localization. The following theorem shows that it suffices to verify [§Flatness, ⁋Proposition 1](/en/math/commutative_algebra/flatness#prop1) only for the maximal ideal.

<div class="proposition" markdown="1">

<ins id="thm1">**Theorem 1**</ins> Fix a Noetherian local ring $$(A, \mathfrak{m})$$, and assume that $$(E, \mathfrak{n})$$ is a local Noetherian $$A$$-algebra satisfying $$\mathfrak{m}E\subseteq \mathfrak{n}$$. Then for a finitely generated $$E$$-module $$M$$, $$M$$ is a flat $$A$$-module if and only if $$\Tor_1^A(A/\mathfrak{m}, M)=0$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

If $$M$$ is a flat $$A$$-module then $$\Tor_1^A(A/\mathfrak{m}, M)=0$$ is precisely the content of [§Flatness, ⁋Proposition 1](/en/math/commutative_algebra/flatness#prop1), so it suffices to prove the converse.

To prove the converse, we again invoke [§Flatness, ⁋Proposition 1](/en/math/commutative_algebra/flatness#prop1): assuming the given condition, we show that for any ideal $$\mathfrak{a}$$ of $$A$$ the multiplication map $$m:\mathfrak{a}\otimes_AM \rightarrow M$$ is injective. To this end, suppose $$x\in \mathfrak{a}\otimes_AM$$ lies in the kernel $$\ker m$$, and let us show that $$x=0$$. First, the $$E$$-module structure on $$M$$ induces a natural $$E$$-module structure on $$\mathfrak{a}\otimes_AM$$ as well, and from the assumption $$\mathfrak{m}E\subseteq \mathfrak{n}$$ we know that for every $$n$$,

$$\mathfrak{m}^n(\mathfrak{a}\otimes_AM )\subseteq \mathfrak{n}^n(\mathfrak{a}\otimes_AM)$$	 

holds. On the other hand, since these are finitely generated $$E$$-modules, [§Blowup Algebras, ⁋Corollary 8](/en/math/commutative_algebra/blowup_algebra#cor8) yields

$$\bigcap \mathfrak{m}^n(\mathfrak{a}\otimes_AM)=\bigcap \mathfrak{n}^n(\mathfrak{a}\otimes_AM)=0.$$

Thus, to show $$x=0$$ it suffices to show that $$x\in \mathfrak{m}^n(\mathfrak{a}\otimes_AM)$$ for all $$n$$. Now $$\mathfrak{m}^n(\mathfrak{a}\otimes_AM)$$ can be identified with $$(\mathfrak{m}^n \mathfrak{a})\otimes_AM$$, and applying [§Blowup Algebras, ⁋Lemma 7](/en/math/commutative_algebra/blowup_algebra#lem7) to the $$\mathfrak{m}$$-stable filtration

$$\mathfrak{m}\supseteq \mathfrak{m}^2\supseteq\cdots$$

and $$M'=\mathfrak{a}$$, the induced filtration

$$\mathfrak{m}\cap \mathfrak{a}\supseteq \mathfrak{m}^2 \cap\mathfrak{a}\supseteq\cdots$$

is also $$\mathfrak{m}$$-stable; hence there exists $$N$$ such that whenever $$m>N$$,

$$\mathfrak{m}^{m+i}\cap \mathfrak{a}=\mathfrak{m}^i(\mathfrak{m}^m\cap \mathfrak{a})$$

holds for all $$i$$. Thus, given any $$n$$, choosing $$t>N+n$$ gives

$$\mathfrak{m}^t\cap \mathfrak{a}=\mathfrak{m}^n(\mathfrak{m}^{t-n}\cap \mathfrak{a})\subseteq \mathfrak{m}^n \mathfrak{a},$$

and so instead of showing that $$x\in (\mathfrak{m}^n\mathfrak{a})\otimes_AM$$ for arbitrary $$n$$, we may show that $$x\in (\mathfrak{m}^t\cap \mathfrak{a})\otimes_AM$$ for arbitrary $$t$$.

Now apply $$-\otimes_AM$$ to the short exact sequence

$$0 \rightarrow \mathfrak{m}^t\cap \mathfrak{a} \rightarrow \mathfrak{a} \rightarrow \frac{\mathfrak{a}}{\mathfrak{m}^t\cap \mathfrak{a}} \rightarrow 0$$

to obtain the exact sequence

$$(\mathfrak{m}^t\cap \mathfrak{a})\otimes_AM \rightarrow \mathfrak{a}\otimes_AM \rightarrow \frac{\mathfrak{a}}{\mathfrak{m}^t\cap \mathfrak{a}}\otimes_AM \rightarrow 0;$$

in this situation it suffices to show that the image of $$x$$ in $$(\mathfrak{a}/\mathfrak{m}^t\cap \mathfrak{a})\otimes_AM$$ is zero. On the other hand, consider the commutative diagram

![inclusions](/assets/images/Math/Commutative_Algebra/Local_Criterion_for_Flatness-1.svg){:style="width:9.34em" class="invert" .align-center}

and apply $$-\otimes_AM$$ to obtain the commutative diagram

![trick](/assets/images/Math/Commutative_Algebra/Local_Criterion_for_Flatness-2.svg){:style="width:16.39em" class="invert" .align-center}

The left-hand map $$\mathfrak{a}\otimes_AM \rightarrow M$$ is the multiplication map $$m$$, so $$x\in\ker m$$ is sent to $$0$$ along the $$\llcorner$$ composite. Hence it suffices to show that the right-hand map $$(\mathfrak{a}/(\mathfrak{m}^t\cap \mathfrak{a}))\otimes_AM \rightarrow (A/\mathfrak{m}^t)\otimes_AM$$ is injective. Via the isomorphism

$$\frac{\mathfrak{a}}{\mathfrak{m}^t\cap \mathfrak{a}}\cong \frac{\mathfrak{a}+\mathfrak{m}^t}{\mathfrak{m}^t}$$

the map $$\mathfrak{a}/(\mathfrak{m}^t\cap \mathfrak{a}) \rightarrow A/\mathfrak{m}^t$$ inducing it is exactly the left-hand map in the short exact sequence

$$0 \rightarrow \frac{\mathfrak{a}+\mathfrak{m}^t}{\mathfrak{m}^t} \rightarrow \frac{A}{\mathfrak{m}^t}\rightarrow \frac{A}{\mathfrak{a}+\mathfrak{m}^t} \rightarrow 0.$$

Therefore, from the $$\Tor$$ long exact sequence

$$\cdots \Tor_1^A(A/(\mathfrak{a}+\mathfrak{m}^t), M) \rightarrow \frac{\mathfrak{a}+\mathfrak{m}^t}{\mathfrak{m}^t}\otimes_AM \rightarrow \frac{A}{\mathfrak{m}^t}\otimes_AM \rightarrow$$

we see that what we must show is $$\Tor_1^A(A/(\mathfrak{a}+\mathfrak{m}^t), M)=0$$.

Now $$A/(\mathfrak{a}+\mathfrak{m}^t)$$ is annihilated by $$\mathfrak{m}^t$$, and since $$\mathfrak{m}^t$$ is finitely generated, it follows that $$A/(\mathfrak{a}+\mathfrak{m}^t)$$ has finite length. Hence, if we show more generally that $$\Tor_1^A(N, M)=0$$ for every $$A$$-module $$N$$ of finite length, we obtain the desired conclusion.

We proceed by induction on length. If $$N$$ has length $$1$$, then by the discussion after [§The Jordan–Hölder Theorem, ⁋Definition 1](/en/math/commutative_algebra/Jordan-Holder_theorem#def1) we must have $$N=A/\mathfrak{m}$$, and thus $$\Tor_1^A(N, M)=0$$ is exactly the hypothesis of the theorem. Choose an $$A$$-module $$N$$ of finite length and any proper submodule $$N'$$ of $$N$$. Applying the $$\Tor$$ long exact sequence to

$$0 \rightarrow N' \rightarrow N \rightarrow N/N' \rightarrow 0$$

we obtain

$$\cdots \rightarrow\Tor_1^A(N', M) \rightarrow \Tor_1^A(N, M) \rightarrow \Tor_1^A(N/N', M) \rightarrow \cdots$$

By the inductive hypothesis $$\Tor_1^A(N', M)=\Tor_1^A(N/N',M)=0$$, whence the desired result.

</details>

On the other hand, if $$M$$ is a flat $$A$$-module then for any $$A/(a)$$-module $$N$$,

$$(M/aM)\otimes_{A/(a)}N=(A/(a)\otimes_A M)\otimes_{A/(a)} N\cong M\otimes_AN$$

so $$M/aM$$ is a flat $$A/(a)$$-module without any additional hypotheses. In [Corollary 3](#cor3) we establish the converse of this assertion under the hypotheses of [Theorem 1](#thm1). For this we require the following lemma.

<div class="proposition" markdown="1">

<ins id="lem2">**Lemma 2**</ins> Let $$M$$ be an $$A$$-module, and let $$a\in A$$ be a non-zerodivisor on both $$A$$ and $$M$$. Then for any $$A/(a)$$-module $$N$$,

$$\Tor_i^{A/(a)}(N, M/aM)=\Tor_i^A(N,M)$$

holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Consider a free resolution of the $$A$$-module $$M$$

$$\cdots \rightarrow F_2 \rightarrow F_1 \rightarrow F_0\tag{1}$$

By definition, the $$i$$-th homology of the chain complex

$$\cdots \rightarrow N\otimes_A F_2 \rightarrow N\otimes_AF_1 \rightarrow N\otimes_A F_0$$

is $$\Tor_i^A(M,N)$$. On the other hand, consider the complex obtained by applying $$A/(a)\otimes_A-$$ to (1):

$$\cdots \rightarrow F_2/aF_2 \rightarrow F_1/aF_1 \rightarrow F_0/aF_0 \rightarrow M/aM \rightarrow 0\tag{2}$$

The homology of this complex is given by

$$\Tor_i^A(A/(a), M)=\begin{cases} M/aM&\text{if $i=0$}\\ 0&\text{otherwise}\end{cases}$$

so (2) is a free resolution of $$M/aM$$. Therefore, computing $$\Tor_i^{A/(a)}(N, M/aM)$$ using (2), we obtain the desired result from the isomorphism

$$N\otimes_{A/(a)} F_i/aF_i=N\otimes_{A/(a)} ((A/(a))\otimes_A F_i)\cong N\otimes_A F_i.$$

</details>

Using this we can prove the following.

<div class="proposition" markdown="1">

<ins id="cor3">**Corollary 3**</ins> Fix a Noetherian local ring $$(A, \mathfrak{m})$$, and assume that $$(E, \mathfrak{n})$$ is a local Noetherian $$A$$-algebra satisfying $$\mathfrak{m}E\subseteq \mathfrak{n}$$. If $$a\in \mathfrak{m}$$ is a non-zerodivisor in $$A$$ and simultaneously a zerodivisor on the finitely generated $$E$$-module $$M$$, then $$M$$ is a flat $$A$$-module if and only if $$M/aM$$ is a flat $$A/(a)$$-module.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Assume that $$M/aM$$ is a flat $$A/(a)$$-module. For the residue field $$A/\mathfrak{m}$$ of $$A$$, the assumption gives

$$\Tor_1^{A/(a)}(A/\mathfrak{m}, M/aM)=0,$$

and applying [Lemma 2](#lem2) we deduce that $$\Tor_1^A(A/\mathfrak{m}, M)=0$$. Hence by [Theorem 1](#thm1), $$M$$ is a flat $$A$$-module.

</details>

## Rees algebra

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> For a ring $$A$$ and an ideal $$\mathfrak{a}$$, the *Rees algebra* is

$$A[\mathfrak{a}t]=\bigoplus_{n=0}^\infty \mathfrak{a}^n t^n\subseteq A[t].$$

In the same setting, the *extended Rees algebra* is defined by

$$A[\mathfrak{a}t, t^{-1}]=\bigoplus_{n=-\infty}^\infty \mathfrak{a}^nt^n\subseteq A[t, t^{-1}].$$

</div>

Then the following corollary is almost obvious.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> Fix a field $$\mathbb{K}$$ and a $$\mathbb{K}$$-algebra $$A$$. Then the Rees algebra $$A[\mathfrak{a}t, t^{-1}]$$ is a flat $$\mathbb{K}[t]$$-module. Moreover, if $$\bigcap \mathfrak{a}^i=0$$, then every element of the form $$1-t s$$ ($$s\in S$$) is a non-zerodivisor in $$A[\mathfrak{a}t, t^{-1}]$$.

</div>
