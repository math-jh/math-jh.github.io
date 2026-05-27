---title: "Properties of Localization"
excerpt: "Compatibility of localization with Hom and tensor, and local properties"

categories: [Math / Commutative Algebra]
permalink: /en/math/commutative_algebra/properties_of_localization
header:
    overlay_image: /assets/images/Math/Commutative_Algebra/Properties_of_Localization.png
    overlay_filter: 0.5
sidebar: 
    nav: "commutative_algebra-en"

date: 2024-10-16
last_modified_at: 2024-10-16
weight: 3
translated_at: 2026-05-28T11:36:15+00:00
translation_source: kimi-cli
---
We now examine additional properties of localization. The first goal of this post is to prove the close relationship between the localization of modules and the localization of rings that we studied in the previous post. Throughout this post, we fix a ring $$A$$, a multiplicative subset $$S$$ of $$A$$, and an $$A$$-module $$M$$.

## Localization and Hom, Tensor

We begin by proving a lemma. Defining an $$A$$-module homomorphism $$S^{-1}A\times_A M \rightarrow  S^{-1}M$$ by $$(r/u, x)\mapsto rx/u$$ gives an $$A$$-bilinear map, and therefore induces an $$A$$-linear map $$S^{-1}A\otimes_A M \rightarrow S^{-1}M$$. ([\[Algebraic Structures\] §Direct Products, Direct Sums, and Tensor Products of Modules, ⁋Theorem 5](/en/math/algebraic_structures/operations_of_modules#def5))

<div class="proposition" markdown="1">

<ins id="lem1">**Lemma 1**</ins> The $$A$$-linear map defined above is an isomorphism.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

It suffices to construct an inverse map. To this end, we first define a function from $$M\times S$$ to $$S^{-1}A\otimes_AM$$ by

$$(x,s)\mapsto \frac{1}{s}\otimes x$$

Then this function defines a well-defined $$A$$-linear map from $$S^{-1}M$$ to $$S^{-1}A\otimes_AM$$. To verify this, it is enough to show that this function respects the equivalence relation defined on $$M\times S$$. Thus, suppose two elements of $$M\times S$$ satisfy $$(x,s)\sim (x',s')$$. Then there exists some $$t\in S$$ such that $$tsx'=ts'x$$ holds, and from this we obtain

$$\frac{1}{tss'}\otimes ts'x=\frac{1}{tss'}\otimes tsx'$$

Since $$ts',ts\in A$$, moving $$ts'$$ and $$ts$$ to the left of $$\otimes$$ on each side yields

$$\frac{1}{s}\otimes x=\frac{1}{s'}\otimes x'$$

That this function is an $$A$$-linear map and is the inverse of the $$S^{-1}A\otimes_A M \rightarrow S^{-1}M$$ defined above is now clear.

</details>

In particular, using this we can also show the functoriality of module localization. For any $$u: M \rightarrow M'$$, we define $$S^{-1}M \rightarrow S^{-1}M'$$ by identifying both sides with localization via the map

$$S^{-1}\otimes_A u: S^{-1}\otimes_AM \rightarrow S^{-1}\otimes_AM'$$

In general, tensor products are right exact, but in this case it becomes an exact functor.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> $$S^{-1}A$$ is a flat $$A$$-module. ([\[Multilinear Algebra\] §Projective, Injective, and Flat Modules, ⁋Definition 7](/en/math/multilinear_algebra/various_modules#def7))

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Suppose an injective $$A$$-linear map $$u:M \rightarrow M'$$ is given; we must show that $$S^{-1}A\otimes_A u$$ is injective. By [Lemma 1](#lem1), it suffices to show that the linear map $$S^{-1}M \rightarrow S^{-1}M'$$ is injective. For any $$x/s\in S^{-1}M$$, suppose its image $$u(x)/s$$ in $$S^{-1}M'$$ is zero. Then from $$u(x)/s=0/1$$ there exists some $$t\in S$$ such that

$$tu(x)=u(tx)=0$$

holds, and since $$u$$ is injective we must have $$tx=0$$ in $$M$$. Then in $$S^{-1}M$$,

$$\frac{x}{s}=\frac{tx}{ts}=\frac{0}{ts}=0$$

so we obtain the desired result.

</details>

## Properties Determined by Localization

By [Proposition 2](#prop2) above, if $$u:M \rightarrow M'$$ is injective (resp. surjective, bijective), then the induced map $$S^{-1}M \rightarrow S^{-1}M'$$ is also such. [Proposition 4](#prop4) can be thought of as a sort of (strong) converse to this. To prove it, we first establish the following lemma.

<div class="proposition" markdown="1">

<ins id="lem3">**Lemma 3**</ins> Let $$M$$ be an $$A$$-module and consider the localization $$\epsilon_\mathfrak{m}:M \rightarrow M_\mathfrak{m}$$ at a maximal ideal $$\mathfrak{m}$$ of $$A$$. Then an element $$x$$ of $$M$$ is zero if and only if for *every* maximal ideal $$\mathfrak{m}$$ of $$A$$, the map $$\epsilon_\mathfrak{m}$$ defined above satisfies $$\epsilon_\mathfrak{m}(x)=0$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

One direction is obvious, so it suffices to show the converse. Fix a maximal ideal $$\mathfrak{m}$$ and suppose $$\epsilon_\mathfrak{m}(x)=0$$ holds. This is equivalent to $$\ann(x)$$ not being contained in $$\mathfrak{m}$$. Then by the given condition, $$\ann(x)$$ is an ideal not contained in *any* maximal ideal of $$A$$, and the only such ideal is $$A$$ itself. That is, $$\ann(x)=A$$, which completes the proof.

</details>

Therefore, the following holds.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> An $$A$$-linear map $$u:M \rightarrow N$$ is a monomorphism (resp. epimorphism, isomorphism) if and only if for every maximal ideal $$\mathfrak{m}$$, the map $$u_\mathfrak{m}: M_\mathfrak{m} \rightarrow N_\mathfrak{m}$$ is such.

</div>

The proof of this follows by applying [Lemma 3](#lem3) to the kernel and cokernel.

The following proposition will be used frequently hereafter, so it is worth remembering the statement even if one does not worry about the proof.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> Fix a ring $$A$$ and an $$A$$-algebra $$E$$. Then for any $$A$$-modules $$M,N$$, the following $$E$$-module homomorphism

$$\alpha: E\otimes_A\Hom_A(M,N) \rightarrow\Hom_E(E\otimes_A M, E\otimes_AN);\qquad (1\otimes f)\mapsto \id_E\otimes_A f$$

is well-defined. In particular, if $$E$$ is a flat $$A$$-module and $$M$$ is finitely presented, then $$\alpha$$ is an isomorphism.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

That $$\alpha$$ is well-defined is obvious. Now suppose $$E$$ is a flat $$A$$-module and $$M=A$$. Then the given

$$\alpha: E\otimes_A\Hom_A(A, N) \rightarrow\Hom_E(E\otimes_AM, E\otimes_AN)$$

fits into the following commutative diagram

![simplest_case](/assets/images/Math/Commutative_Algebra/Properties_of_Localization-1.png){:style="width:23em" class="invert" .align-center}

so the proposition holds. Here the vertical maps come from the isomorphisms

$$\Hom_A(A,N)\cong N,\qquad \Hom_E(E\otimes_A,E\otimes_AN)\cong\Hom_E(E,E\otimes_AN)\cong E\otimes_AN$$

Then, since $$\Hom$$ and $$\otimes$$ commute with finite direct sums, this proposition also holds for a flat $$A$$-module $$E$$ and any finitely generated free $$A$$-module $$M$$. Finally, for the case where $$M$$ is finitely presented, take a free presentation

$$F \rightarrow G \rightarrow M \rightarrow 0$$

and then apply the four lemma to the following commutative diagram

![general_case](/assets/images/Math/Commutative_Algebra/Properties_of_Localization-2.png){:style="width:44em" class="invert" .align-center}

</details>

In particular, suppose the following short exact sequence

$$0 \rightarrow M \rightarrow L \rightarrow N \rightarrow 0$$

is given. Then this exact sequence is a splitting exact sequence if and only if for every $$A$$-module $$K$$,

$$0 \rightarrow \Hom_\rMod{A}(K,M) \rightarrow \Hom_\rMod{A}(K,L)\rightarrow \Hom_\rMod{A}(K,N) \rightarrow 0$$

is a splitting exact sequence, and looking at the proof of [\[Multilinear Algebra\] §Hom and Tensor Products, ⁋Proposition 1](/en/math/multilinear_algebra/hom_and_tensor#prop1), in fact if the above sequence is exact when $$K=N$$, that is, if

$$\Hom_\rMod{A}(N,L) \rightarrow \Hom_\rMod{A}(N,N) \rightarrow 0$$

is surjective, then the original exact sequence $$0 \rightarrow M \rightarrow L \rightarrow N \rightarrow 0$$ is a splitting exact sequence. Thus we obtain the following.

<div class="proposition" markdown="1">

<ins id="cor6">**Corollary 6**</ins> Suppose an arbitrary short exact sequence

$$0 \rightarrow M \rightarrow L \rightarrow N \rightarrow 0$$

is given. If $$N$$ is finitely presented and for every maximal ideal $$\mathfrak{m}$$,

$$0 \rightarrow M_\mathfrak{m} \rightarrow L_\mathfrak{m} \rightarrow N_\mathfrak{m} \rightarrow 0$$

is a splitting exact sequence, then the original exact sequence splits.

</div>

## Radical of an Ideal

The following result is not strictly related to localization, but we mention it here because the proof uses a multiplicative subset.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> For a ring $$A$$ and a multiplicative subset $$S$$, suppose $$\mathfrak{a}$$ is maximal among ideals not meeting $$S$$. Then $$\mathfrak{a}$$ is a prime ideal.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$a_1,a_2$$ be two elements of $$A$$; we show that if $$a_1,a_2\not\in \mathfrak{a}$$ then $$a_1a_2\not\in \mathfrak{a}$$. By the maximality of $$\mathfrak{a}$$, the two ideals $$\mathfrak{a}+(a_1)$$ and $$\mathfrak{a}+(a_2)$$ must both meet $$S$$, so there exist suitable $$b_1,b_2\in A$$ and $$x_1,x_2\in \mathfrak{a}$$ such that $$a_ib_i+x_i\in S$$. Since $$S$$ is closed under multiplication, the element

$$(a_1b_1+x_1)(a_2b_2+x_2)=a_1a_2b_1b_2+a_1b_1x_2+a_2b_2x_1+x_1x_2$$

must also belong to $$S$$. If contrary to the conclusion $$a_1a_2\in \mathfrak{a}$$, then all four terms on the right-hand side lie in $$\mathfrak{a}$$, contradicting the assumption that $$\mathfrak{a}$$ and $$S$$ do not meet.

</details>

In a similar vein we obtain the following.

<div class="proposition" markdown="1">

<ins id="cor8">**Corollary 8**</ins> For an ideal $$\mathfrak{a}$$ of a ring $$A$$, define the *radical* $$\sqrt{\mathfrak{a}}$$ by the formula

$$\sqrt{\mathfrak{a}}=\{a\mid a^k\in \mathfrak{a}\text{ for some $k\in \mathbb{N}$}\}$$

Then

$$\sqrt{\mathfrak{a}}=\bigcap_\text{\scriptsize$\mathfrak{p}$ prime containing $\mathfrak{a}$} \mathfrak{p}$$

holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

One direction is obvious. For the converse, if $$a\not\in \sqrt{\mathfrak{a}}$$ then set $$S=\{a^k\mid k\geq 1\}$$ and apply [§Localization, ⁋Proposition 8](/en/math/commutative_algebra/localization#prop8).

</details>

---

**References**

**[Eis]** David Eisenbud. *Commutative Algebra: with a view toward algebraic geometry*. Springer, 1995.

---
