---
title: "Flatness and Localization"
description: "We discuss criteria for deciding whether a finitely generated module over a Noetherian local ring is flat, showing that it suffices to verify flatness at the maximal ideal alone."
excerpt: "A local criterion for flatness via checking at the maximal ideal"

categories: [Math / Commutative Algebra]
permalink: /en/math/commutative_algebra/local_criterion_for_flatness
sidebar: 
    nav: "commutative_algebra-en"

date: 2025-01-12
weight: 13

toc: false
translated_at: 2026-09-01T20:15:05+00:00
translation_source: kimi-cli
---
In the previous post, we looked at several criteria for determining when an $A$-module $M$ is flat; in this post, we examine a criterion for determining flatness specifically over a Noetherian local ring $(A, \mathfrak{m})$. The following theorem shows that, for a finitely generated module over a local Noetherian $A$-algebra $(E, \mathfrak{n})$ satisfying $\mathfrak{m}E\subseteq \mathfrak{n}$, it suffices to check [§Flatness, ⁋Proposition 1](/en/math/commutative_algebra/flatness#prop1) only for the maximal ideal.

::: Theorem 1
Fix a Noetherian local ring $(A, \mathfrak{m})$, and suppose that $(E, \mathfrak{n})$ is a local Noetherian $A$-algebra satisfying $\mathfrak{m}E\subseteq \mathfrak{n}$. Then for a finitely generated $E$-module $M$, $M$ is a flat $A$-module if and only if $\Tor_1^A(A/\mathfrak{m}, M)=0$.
:::
::: Proof
If $M$ is a flat $A$-module, then $\Tor_1^A(A/\mathfrak{m}, M)=0$ is exactly the content of [§Flatness, ⁋Proposition 1](/en/math/commutative_algebra/flatness#prop1), so it suffices to prove the converse.

For the converse, we again use [§Flatness, ⁋Proposition 1](/en/math/commutative_algebra/flatness#prop1): after assuming the given condition, it suffices to show that for an arbitrary ideal $\mathfrak{a}$ of $A$, the multiplication map $m:\mathfrak{a}\otimes_AM \rightarrow M$ is injective. To this end, suppose $x\in \mathfrak{a}\otimes_AM$ belongs to the kernel $\ker m$ of the multiplication map, and let us show that $x=0$. First, the $E$-module structure on $M$ naturally induces an $E$-module structure on $\mathfrak{a}\otimes_AM$, and from the assumption $\mathfrak{m}E\subseteq \mathfrak{n}$, we know that for every $n$ the following

$$\mathfrak{m}^n(\mathfrak{a}\otimes_AM )\subseteq \mathfrak{n}^n(\mathfrak{a}\otimes_AM)$$	 

holds. On the other hand, since these are finitely generated $E$-modules, by part 1 of [§Blowup Algebras, ⁋Corollary 8](/en/math/commutative_algebra/blowup_algebra#cor8) there exists $a\in \mathfrak{n}$ such that $(1-a)(\bigcap \mathfrak{n}^n(\mathfrak{a}\otimes_AM))=0$, and since $E$ is a local ring, $1-a$ is a unit, so

$$\bigcap \mathfrak{m}^n(\mathfrak{a}\otimes_AM)=\bigcap \mathfrak{n}^n(\mathfrak{a}\otimes_AM)=0$$

holds. Therefore, to show that $x=0$, it suffices to show that $x\in \mathfrak{m}^n(\mathfrak{a}\otimes_AM)$ holds for every $n$. Meanwhile, $\mathfrak{m}^n(\mathfrak{a}\otimes_AM)$ can be identified with $(\mathfrak{m}^n \mathfrak{a})\otimes_AM$, and applying [§Blowup Algebras, ⁋Lemma 7](/en/math/commutative_algebra/blowup_algebra#lem7) to the following $\mathfrak{m}$-stable filtration

$$\mathfrak{m}\supseteq \mathfrak{m}^2\supseteq\cdots$$

with $M'=\mathfrak{a}$, the following filtration

$$\mathfrak{m}\cap \mathfrak{a}\supseteq \mathfrak{m}^2 \cap\mathfrak{a}\supseteq\cdots$$

is also $\mathfrak{m}$-stable, so we can choose a suitable $N$ such that whenever $m>N$, for all $i$

$$\mathfrak{m}^{m+i}\cap \mathfrak{a}=\mathfrak{m}^i(\mathfrak{m}^m\cap \mathfrak{a})$$

holds. Therefore, whenever an arbitrary $n$ is given, taking $t>N+n$ gives

$$\mathfrak{m}^t\cap \mathfrak{a}=\mathfrak{m}^n(\mathfrak{m}^{t-n}\cap \mathfrak{a})\subseteq \mathfrak{m}^n \mathfrak{a}$$

so instead of showing that $x\in (\mathfrak{m}^n\mathfrak{a})\otimes_AM$ holds for every $n$, we may show that $x\in (\mathfrak{m}^t\cap \mathfrak{a})\otimes_AM$ holds for every $t$.

Now, applying $-\otimes_AM$ to the short exact sequence

$$0 \rightarrow \mathfrak{m}^t\cap \mathfrak{a} \rightarrow \mathfrak{a} \rightarrow \frac{\mathfrak{a}}{\mathfrak{m}^t\cap \mathfrak{a}} \rightarrow 0$$

yields the exact sequence

$$(\mathfrak{m}^t\cap \mathfrak{a})\otimes_AM \rightarrow \mathfrak{a}\otimes_AM \rightarrow \frac{\mathfrak{a}}{\mathfrak{m}^t\cap \mathfrak{a}}\otimes_AM \rightarrow 0$$

and in this situation, it suffices to show that $x$ becomes $0$ when carried over to $(\mathfrak{a}/\mathfrak{m}^t\cap \mathfrak{a})\otimes_AM$. Meanwhile, consider the commutative diagram

{% diagram Math/Commutative_Algebra/Local_Criterion_for_Flatness-1.svg width="9.34em" alt="inclusions" %}

and the commutative diagram obtained by applying $-\otimes_AM$ to it:

{% diagram Math/Commutative_Algebra/Local_Criterion_for_Flatness-2.svg width="16.39em" alt="trick" %}

The left-hand map $\mathfrak{a}\otimes_AM \rightarrow M$ is the multiplication map $m$, so $x\in\ker m$ is carried to $0$ via the composition in the $\llcorner$ direction. Therefore, it suffices to show that the right-hand map $(\mathfrak{a}/(\mathfrak{m}^t\cap \mathfrak{a}))\otimes_AM \rightarrow (A/\mathfrak{m}^t)\otimes_AM$ is injective. Through the isomorphism

$$\frac{\mathfrak{a}}{\mathfrak{m}^t\cap \mathfrak{a}}\cong \frac{\mathfrak{a}+\mathfrak{m}^t}{\mathfrak{m}^t}$$

the map $\mathfrak{a}/(\mathfrak{m}^t\cap \mathfrak{a}) \rightarrow A/\mathfrak{m}^t$ inducing it is exactly the left-hand map of the short exact sequence

$$0 \rightarrow \frac{\mathfrak{a}+\mathfrak{m}^t}{\mathfrak{m}^t} \rightarrow \frac{A}{\mathfrak{m}^t}\rightarrow \frac{A}{\mathfrak{a}+\mathfrak{m}^t} \rightarrow 0$$

Therefore, from the $\Tor$ long exact sequence

$$\cdots \Tor_1^A(A/(\mathfrak{a}+\mathfrak{m}^t), M) \rightarrow \frac{\mathfrak{a}+\mathfrak{m}^t}{\mathfrak{m}^t}\otimes_AM \rightarrow \frac{A}{\mathfrak{m}^t}\otimes_AM \rightarrow$$

what we must show is that $\Tor_1^A(A/(\mathfrak{a}+\mathfrak{m}^t), M)=0$.

Now, $A/(\mathfrak{a}+\mathfrak{m}^t)$ is annihilated by $\mathfrak{m}^t$, and since $\mathfrak{m}^t$ is finitely generated, this implies that $A/(\mathfrak{a}+\mathfrak{m}^t)$ has finite length. Therefore, we obtain the desired result once we show, more generally, that $\Tor_1^A(N, M)=0$ holds for any $A$-module $N$ of finite length.

We proceed by induction. If $N$ has length $1$, then by the argument following [§The Jordan-Hölder Theorem, ⁋Definition 1](/en/math/commutative_algebra/Jordan-Holder_theorem#def1), we must have $N=A/\mathfrak{m}$, and hence $\Tor_1^A(N, M)=0$ agrees exactly with the hypothesis of the theorem. Let $N$ be an $A$-module of finite length, and choose any nonzero proper submodule $N'$ of $N$. Applying the $\Tor$ long exact sequence to the exact sequence

$$0 \rightarrow N' \rightarrow N \rightarrow N/N' \rightarrow 0$$

yields

$$\cdots \rightarrow\Tor_1^A(N', M) \rightarrow \Tor_1^A(N, M) \rightarrow \Tor_1^A(N/N', M) \rightarrow \cdots$$

Now by the inductive hypothesis, $\Tor_1^A(N', M)=\Tor_1^A(N/N',M)=0$, so we obtain the desired result.
:::

Meanwhile, if $M$ is a flat $A$-module, then for any $A/(a)$-module $N$,

$$(M/aM)\otimes_{A/(a)}N=(A/(a)\otimes_A M)\otimes_{A/(a)} N\cong M\otimes_AN$$

so $M/aM$ is a flat $A/(a)$-module with no further conditions. In [Corollary 3](#cor3), we prove the converse of this claim under the hypotheses of [Theorem 1](#thm1). For this, we first need the following lemma.

::: Lemma 2
Let an $A$-module $M$ be given, and suppose $a\in A$ is a non-zerodivisor on both $A$ and $M$. Then for any $A/(a)$-module $N$,

$$\Tor_i^{A/(a)}(N, M/aM)=\Tor_i^A(N,M)$$

holds.
:::
::: Proof
Consider a free resolution

$$\cdots \rightarrow F_2 \rightarrow F_1 \rightarrow F_0\tag{1}$$

of the $A$-module $M$. By definition, the $i$-th homology of the chain complex

$$\cdots \rightarrow N\otimes_A F_2 \rightarrow N\otimes_AF_1 \rightarrow N\otimes_A F_0$$

is $\Tor_i^A(M,N)$. Meanwhile, consider the complex

$$\cdots \rightarrow F_2/aF_2 \rightarrow F_1/aF_1 \rightarrow F_0/aF_0 \rightarrow M/aM \rightarrow 0\tag{2}$$

obtained by applying $A/(a)\otimes_A-$ to (1). Since its homology is given by

$$\Tor_i^A(A/(a), M)=\begin{cases} M/aM&\text{if $i=0$}\\ 0&\text{otherwise}\end{cases}$$

this is a free resolution of $M/aM$. Therefore, using (2) to compute $\Tor_i^{A/(a)}(N, M/aM)$, we obtain the desired result through the isomorphism

$$N\otimes_{A/(a)} F_i/aF_i=N\otimes_{A/(a)} ((A/(a))\otimes_A F_i)\cong N\otimes_A F_i$$

:::
Using this, we can prove the following.

::: Corollary 3
Fix a Noetherian local ring $(A, \mathfrak{m})$, and suppose that $(E, \mathfrak{n})$ is a local Noetherian $A$-algebra satisfying $\mathfrak{m}E\subseteq \mathfrak{n}$. If $a\in \mathfrak{m}$ is simultaneously a non-zerodivisor of $A$ and a non-zerodivisor of a finitely generated $E$-module $M$, then $M$ is a flat $A$-module if and only if $M/aM$ is a flat $A/(a)$-module.
:::
::: Proof
Suppose $M/aM$ is a flat $A/(a)$-module. Since the residue field of $A/(a)$ is $A/\mathfrak{m}$, by assumption

$$\Tor_1^{A/(a)}(A/\mathfrak{m}, M/aM)=0$$

holds, and now applying [Lemma 2](#lem2), we know that $\Tor_1^A(A/\mathfrak{m}, M)=0$ holds. Therefore, by [Theorem 1](#thm1), $M$ is a flat $A$-module.
:::

While the theorem above, in the form of [Corollary 3](#cor3), essentially cuts by an element on the base side, the following form, cutting by an element on the fiber side, is used to lift flatness from the fiber to the base.

::: Corollary 4
Fix a Noetherian local ring $(A, \mathfrak{m})$, and suppose that $(E, \mathfrak{n})$ is a local Noetherian $A$-algebra satisfying $\mathfrak{m}E\subseteq \mathfrak{n}$. Let $M$ be a finitely generated $E$-module that is a flat $A$-module, and suppose that for an element $f\in \mathfrak{n}$, the image of $f$ is a non-zerodivisor on $M/\mathfrak{m}M$. Then $f$ is a non-zerodivisor on $M$, and $M/fM$ is a flat $A$-module. In particular, if the images of $f_1,\ldots, f_r\in \mathfrak{n}$ form a regular sequence of $M/\mathfrak{m}M$, then $f_1,\ldots, f_r$ is a regular sequence of $M$, and $M/(f_1,\ldots, f_r)M$ is a flat $A$-module.
:::
::: Proof
For convenience of the proof, write $\kappa=A/\mathfrak{m}$, and let $K$ be the kernel and $C=M/fM$ the cokernel of $\times f:M \rightarrow M$.

First, applying $-\otimes_A\kappa$ to the exact sequence

$$0 \rightarrow K \rightarrow M \rightarrow fM \rightarrow 0$$

shows that $M\otimes_A\kappa \rightarrow fM\otimes_A\kappa$ is surjective. Composing this with the map $fM\otimes_A\kappa \rightarrow M\otimes_A\kappa$ induced by the inclusion $fM\hookrightarrow M$, we obtain exactly multiplication by $f$ on $M\otimes_A\kappa=M/\mathfrak{m}M$, and since this is injective by assumption, $M\otimes_A\kappa \rightarrow fM\otimes_A\kappa$ is also injective, giving an isomorphism. In particular, $fM\otimes_A\kappa \rightarrow M\otimes_A\kappa$ is injective as well.

Now apply the long exact sequence of $\Tor^A_\bullet(\kappa, -)$ to the exact sequence

$$0 \rightarrow fM \rightarrow M \rightarrow C \rightarrow 0$$

Since $M$ is flat, $\Tor_1^A(\kappa, M)=0$ ([§Flatness, ⁋Proposition 1](/en/math/commutative_algebra/flatness#prop1)), and hence

$$0 \rightarrow \Tor_1^A(\kappa, C) \rightarrow fM\otimes_A\kappa \rightarrow M\otimes_A\kappa$$

is exact. Since we saw above that the right-hand morphism is injective, $\Tor_1^A(\kappa, C)=0$, and since $C$ is a finitely generated $E$-module, by [Theorem 1](#thm1), $C=M/fM$ is a flat $A$-module.

We must now show that $K=0$. Since $C$ is flat, computing $\Tor_i^A(N, C)$ for any $A$-module $N$ via a projective resolution of $N$, it vanishes for $i\geq 1$ because $-\otimes_AC$ is exact; likewise $\Tor_1^A(N,M)=0$. Then from the long exact sequence of $0 \rightarrow fM \rightarrow M \rightarrow C \rightarrow 0$,

$$0=\Tor_2^A(N,C) \rightarrow \Tor_1^A(N, fM) \rightarrow \Tor_1^A(N,M)=0$$

so $\Tor_1^A(N, fM)=0$, and by [§Flatness, ⁋Proposition 1](/en/math/commutative_algebra/flatness#prop1), $fM$ is also a flat $A$-module. Therefore, the sequence obtained by applying $-\otimes_A\kappa$ to $0 \rightarrow K \rightarrow M \rightarrow fM \rightarrow 0$ is exact on the left as well, so $K\otimes_A\kappa \rightarrow M\otimes_A\kappa$ is injective; but its image is the kernel of $M\otimes_A\kappa \rightarrow fM\otimes_A\kappa$, and since this morphism is an isomorphism, the image is zero. That is, $K\otimes_A\kappa=K/\mathfrak{m}K=0$, and since $K$ is a finitely generated $E$-module with $\mathfrak{m}K\subseteq \mathfrak{n}K$, Nakayama's lemma ([§Integral Extensions, ⁋Lemma 8](/en/math/commutative_algebra/integral_extension#lem8)) gives $K=0$.

The final claim follows by induction on $r$. We saw above that $M/f_1M$ is a flat $A$-module, and since

$$(M/f_1M)/\mathfrak{m}(M/f_1M)=(M/\mathfrak{m}M)/f_1(M/\mathfrak{m}M)$$

the images of $f_2,\ldots, f_r$ form a regular sequence of this quotient, so the same argument can be repeated.
:::

## Rees algebra

::: Definition 5
For a ring $A$ and an ideal $\mathfrak{a}$, the *Rees algebra* is

$$A[\mathfrak{a}t]=\bigoplus_{n=0}^\infty \mathfrak{a}^n t^n\subseteq A[t]$$

Also, in the same situation, we define the *extended Rees algebra* by

$$A[\mathfrak{a}t, t^{-1}]=\bigoplus_{n=-\infty}^\infty \mathfrak{a}^nt^n\subseteq A[t, t^{-1}]$$

where we adopt the convention $\mathfrak{a}^n=A$ for $n\leq 0$.
:::

If $A$ is an algebra over a field $\mathbb{K}$, then the extended Rees algebra contains $t^{-1}$, so it is a $\mathbb{K}[t^{-1}]$-algebra, and in this case the following holds.

::: Proposition 6
Fix a field $\mathbb{K}$, a $\mathbb{K}$-algebra $A$, and an ideal $\mathfrak{a}$ of $A$, and write $R=A[\mathfrak{a}t, t^{-1}]$. Then the extended Rees algebra $R$ is a flat $\mathbb{K}[t^{-1}]$-module. Moreover, if $\bigcap \mathfrak{a}^i=0$, then all elements of the form $1-t^{-1}s$ ($s\in R$) are non-zerodivisors on $R$.
:::

---

**References**

**[Eis]** David Eisenbud. *Commutative Algebra: with a view toward algebraic geometry*. Springer, 1995.
