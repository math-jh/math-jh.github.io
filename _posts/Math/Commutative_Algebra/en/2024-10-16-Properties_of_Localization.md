---
title: "Properties of Localization"
description: "We prove the close relationship between the localization of rings and the localization of modules, examine the relationship of localization with Hom and tensor products, and show that localization is a flat module."
excerpt: "Compatibility of localization with Hom and tensor, and local properties"

categories: [Math / Commutative Algebra]
permalink: /en/math/commutative_algebra/properties_of_localization
sidebar: 
    nav: "commutative_algebra-en"

date: 2024-10-16
weight: 3
translated_at: 2026-05-30T17:00:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-04T03:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
We now examine further properties of localization. The first goal of this post is to prove that there is a close relationship between the localization of modules and the localization of rings discussed in the previous post. In this post, we fix a ring $A$, a multiplicative subset of $A$, $S$, and an $A$-module $M$. 

## Localization and Hom, Tensor

We begin by proving a lemma. If we define a function $S^{-1}A\times M \rightarrow  S^{-1}M$ by $(r/u, x)\mapsto rx/u$, this is an $A$-bilinear map, and therefore induces an $A$-linear map $S^{-1}A\otimes_A M \rightarrow S^{-1}M$. ([\[Algebraic Structures\] §Direct Products, Direct Sums, and Tensor Products of Modules, ⁋Theorem 5](/en/math/algebraic_structures/operations_of_modules#thm5){: data-lid="t8y44" }) 

::: Lemma 1
The $A$-linear map defined above is an isomorphism.
:::
::: Proof
It suffices to construct an inverse. To this end, let us first define a function from $M\times S$ to $S^{-1}A\otimes_AM$ by

$$(x,s)\mapsto \frac{1}{s}\otimes x$$

Then this function defines a well-defined map from $S^{-1}M$ to $S^{-1}A\otimes_AM$ that is $A$-linear. To see this, it suffices to show that this function is well-behaved with respect to the equivalence relation defined on $M\times S$. Thus, suppose $(x,s)\sim (x',s')$ holds for two given elements of $M\times S$. Then there exists some $t\in S$ such that $tsx'=ts'x$ holds, and from this

$$\frac{1}{tss'}\otimes ts'x=\frac{1}{tss'}\otimes tsx'$$

holds. But since $ts',ts\in A$, moving $ts'$ and $ts$ on the left- and right-hand sides, respectively, to the left of $\otimes$ yields

$$\frac{1}{s}\otimes x=\frac{1}{s'}\otimes x'$$

It is clear that this function is an $A$-linear map and is the inverse of $S^{-1}A\otimes_A M \rightarrow S^{-1}M$ defined above.
:::

In particular, using this we can also show the functoriality of the localization of modules. This is because for any $u: M \rightarrow M'$, we can define $S^{-1}M \rightarrow S^{-1}M'$ by identifying both sides of the function

$$S^{-1}A\otimes_A u: S^{-1}A\otimes_AM \rightarrow S^{-1}A\otimes_AM'$$

with localizations. In general, the tensor product is right exact, but in this case it becomes an exact functor.

::: Proposition 2
$S^{-1}A$ is a flat $A$-module. ([\[Multilinear Algebra\] §Projective, Injective, and Flat Modules, ⁋Definition 7](/en/math/multilinear_algebra/various_modules#def7){: data-lid="4i7jv" })
:::
::: Proof
Suppose an injective $A$-linear map $u:M \rightarrow M'$ is given; we must show that $S^{-1}A\otimes_A u$ is injective. However, by [Lemma 1](#lem1){: data-lid="pirbk" }, it suffices to show that the linear map $S^{-1}M \rightarrow S^{-1}M'$ is injective. For some $x/s\in S^{-1}M$, suppose that the element sent to $S^{-1}M'$, namely $u(x)/s$, is in $S^{-1}M'$ equal to $0$. Then from $u(x)/s=0/1$, there exists some $t\in S$ such that 

$$tu(x)=u(tx)=0$$

holds, and since $u$ is injective, in $M$ we must have $tx=0$. Then in $S^{-1}M$,

$$\frac{x}{s}=\frac{tx}{ts}=\frac{0}{ts}=0$$

so we obtain the desired result. 
:::

## Properties Determined by Localization

By [Proposition 2](#prop2){: data-lid="432mt" } above and the right exactness of the tensor product, we know that if $u:M \rightarrow M'$ is injective (resp. surjective, bijective), then the map $S^{-1}M \rightarrow S^{-1}M'$ induced by this is also such. [Proposition 4](#prop4){: data-lid="urbx0" } can be regarded as a kind of (strong) converse to this. To this end, we first prove the following lemma.

::: Lemma 3
Consider an $A$-module $M$ and, at a maximal ideal of $A$, $\mathfrak{m}$, the localization $\epsilon_\mathfrak{m}:M \rightarrow M_\mathfrak{m}$. Then an element of $M$, $x$, is $0$ if and only if for *every* maximal ideal of $A$, $\mathfrak{m}$, the map $\epsilon_\mathfrak{m}$ defined above satisfies $\epsilon_\mathfrak{m}(x)=0$.
:::
::: Proof
One direction is obvious, so it suffices to prove the converse. Fix a maximal ideal $\mathfrak{m}$ and suppose $\epsilon_\mathfrak{m}(x)=0$. This is equivalent to $\ann(x)$ not being contained in $\mathfrak{m}$. Then by the given condition, $\ann(x)$ is an ideal not contained in *any* maximal ideal of $A$, and the only such ideal is $A$ itself. Thus $\ann(x)=A$, which completes the proof.
:::

Therefore, the following holds.

::: Proposition 4
An $A$-linear map $u:M \rightarrow N$ is a monomorphism (resp. epimorphism, isomorphism) if and only if for every maximal ideal $\mathfrak{m}$, $u_\mathfrak{m}: M_\mathfrak{m} \rightarrow N_\mathfrak{m}$ is such.
:::

To prove this, it suffices to apply [Lemma 3](#lem3){: data-lid="lsenz" } to the kernel and cokernel.

The following proposition will be used frequently hereafter, so even if one does not worry about the proof, it is good to remember the result.

::: Proposition 5
Fix a ring $A$ and an $A$-algebra $E$. Then for any $A$-modules $M,N$, the following $E$-module homomorphism

$$\alpha: E\otimes_A\Hom_A(M,N) \rightarrow\Hom_E(E\otimes_A M, E\otimes_AN);\qquad (1\otimes f)\mapsto \id_E\otimes_A f$$

is well-defined. In particular, if $E$ is a flat $A$-module and $M$ is finitely presented, then $\alpha$ is an isomorphism.
:::
::: Proof
That $\alpha$ is well-defined is obvious. Now suppose $E$ is a flat $A$-module and $M=A$. Then the given

$$\alpha: E\otimes_A\Hom_A(A, N) \rightarrow\Hom_E(E\otimes_AA, E\otimes_AN)$$

fits into the following commutative diagram

{% diagram Math/Commutative_Algebra/Properties_of_Localization-1.svg width="24.69em" alt="simplest_case" %}

so the given proposition holds. Here the vertical maps come from the respective isomorphisms

$$\Hom_A(A,N)\cong N,\qquad \Hom_E(E\otimes_AA,E\otimes_AN)\cong\Hom_E(E,E\otimes_AN)\cong E\otimes_AN$$

Next, since $\Hom$ and $\otimes$ commute with finite direct sums, this proposition also holds for any flat $A$-module $E$ and any finitely generated free $A$-module $M$. Finally, in the case where $M$ is finitely presented, after taking the following free presentation consisting of finitely generated free $A$-modules $F,G$

$$F \rightarrow G \rightarrow M \rightarrow 0$$

it suffices to apply the four lemma to the following commutative diagram

{% diagram Math/Commutative_Algebra/Properties_of_Localization-2.svg width="47.63em" alt="general_case" %}
:::

In particular, suppose the following short exact sequence

$$0 \rightarrow M \rightarrow L \rightarrow N \rightarrow 0$$

is given. Then this exact sequence is a split exact sequence if and only if for every $A$-module $K$,

$$0 \rightarrow \Hom_\rMod{A}(K,M) \rightarrow \Hom_\rMod{A}(K,L)\rightarrow \Hom_\rMod{A}(K,N) \rightarrow 0$$

is a split exact sequence; moreover, examining the proof of [\[Multilinear Algebra\] §Hom and the Tensor Product, ⁋Proposition 1](/en/math/multilinear_algebra/hom_and_tensor#prop1){: data-lid="2lt05" }, we see that in fact if the above sequence is exact when $K=N$, that is, if

$$\Hom_\rMod{A}(N,L) \rightarrow \Hom_\rMod{A}(N,N) \rightarrow 0$$

is surjective, then the original exact sequence $0 \rightarrow M \rightarrow L \rightarrow N \rightarrow 0$ is a split exact sequence. Thus we obtain the following.

::: Corollary 6
Suppose an arbitrary short exact sequence

$$0 \rightarrow M \rightarrow L \rightarrow N \rightarrow 0$$

is given. If $N$ is finitely presented and for every maximal ideal $\mathfrak{m}$,

$$0 \rightarrow M_\mathfrak{m} \rightarrow L_\mathfrak{m} \rightarrow N_\mathfrak{m} \rightarrow 0$$

is a splitting exact sequence, then the original exact sequence splits.
:::

## Radical of an Ideal

Strictly speaking, the following result is not related to localization, but because we use a multiplicative subset in stating it, we mention it here and move on.

::: Proposition 7
For a ring $A$ and a multiplicative subset $S$, suppose $\mathfrak{a}$ is maximal among ideals disjoint from $S$. Then $\mathfrak{a}$ is a prime ideal.
:::
::: Proof
First, since $1\in S$, from $\mathfrak{a}\cap S=\emptyset$ we have $1\not\in \mathfrak{a}$, that is, $\mathfrak{a}\neq A$. Now suppose two elements of $A$, $a_1,a_2$, are given, and let us show that if $a_1,a_2\not\in \mathfrak{a}$, then $a_1a_2\not\in \mathfrak{a}$. By the maximality of $\mathfrak{a}$, the two ideals $\mathfrak{a}+(a_1)$ and $\mathfrak{a}+(a_2)$ must intersect $S$, so for some $b_1,b_2\in A$ and $x_1,x_2\in \mathfrak{a}$ we must have $a_ib_i+x_i\in S$. But since $S$ is closed under multiplication, the following element

$$(a_1b_1+x_1)(a_2b_2+x_2)=a_1a_2b_1b_2+a_1b_1x_2+a_2b_2x_1+x_1x_2$$

must also belong to $S$. If, contrary to the conclusion, $a_1a_2\in \mathfrak{a}$, then all four terms on the right-hand side belong to $\mathfrak{a}$, which contradicts the assumption that $\mathfrak{a}$ and $S$ do not intersect.
:::

In a similar vein, we obtain the following.

::: Corollary 8
For a ring $A$ and an ideal $\mathfrak{a}$, define the *radical* of $\mathfrak{a}$, $\sqrt{\mathfrak{a}}$, by the formula

$$\sqrt{\mathfrak{a}}=\{a\mid a^k\in \mathfrak{a}\text{ for some $k\in \mathbb{N}$}\}$$

Then

$$\sqrt{\mathfrak{a}}=\bigcap_\text{\scriptsize$\mathfrak{p}$ prime containing $\mathfrak{a}$} \mathfrak{p}$$

holds.
:::
::: Proof
One direction is obvious. Conversely, if $a\not\in \sqrt{\mathfrak{a}}$, it suffices to set $S=\{a^k\mid k\geq 0\}$ and apply [§Localization, ⁋Proposition 8](/en/math/commutative_algebra/localization#prop8){: data-lid="4pvsb" }.
:::

---

**References**

**[Eis]** David Eisenbud. *Commutative Algebra: with a view toward algebraic geometry*. Springer, 1995.

---
