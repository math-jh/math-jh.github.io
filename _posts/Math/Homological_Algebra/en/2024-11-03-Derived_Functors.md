---
title: "Derived Functors"
description: "This post covers the basic concepts of derived functors in homological algebra. It explains the definitions of homology and cohomology delta-functors, long exact sequences, and naturality conditions, and examines the properties of morphisms between functors."
excerpt: "Definition of right/left derived functors via δ-functors"

categories: [Math / Homological Algebra]
permalink: /en/math/homological_algebra/derived_functors
header:
    overlay_image: /assets/images/Math/Homological_Algebra/Derived_Functors.png
    overlay_filter: 0.5
sidebar: 
    nav: "homological_algebra-en"

date: 2024-11-03
last_modified_at: 2024-11-03
weight: 5
translated_at: 2026-05-31T14:00:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-31T14:00:05+00:00
---
## $$\delta$$-functor

We previously proved that, given any short exact sequence in $$\Ch(\mathcal{A})$$

$$0\longrightarrow A_\bullet\longrightarrow B_\bullet\longrightarrow C_\bullet\longrightarrow 0$$

we can construct the long exact sequence

$$\cdots\rightarrow H_n(A)\rightarrow H_n(B)\rightarrow H_n(C)\rightarrow H_{n-1}(A)\rightarrow \cdots$$

The most essential part of this proof was the definition of the connecting map $$\delta$$, and we generalize this process as follows.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Let two abelian categories $$\mathcal{A},\mathcal{B}$$ be given. Then a *homological $$\delta$$-functor* from $$\mathcal{A}$$ to $$\mathcal{B}$$ consists of a collection of additive functors $$T_n:\mathcal{A}\rightarrow\mathcal{B}$$ ($$n\geq 0$$), together with morphisms $$\delta_n:T_n(C)\rightarrow T_{n-1}(A)$$ defined for every short exact sequence

$$0\longrightarrow A\longrightarrow B\longrightarrow C\longrightarrow 0$$

For $$n<0$$, we regard all $$T_n$$ as zero. These satisfy the following conditions.

1. (Long exact sequence) The sequence

    $$\cdots\longrightarrow T_{n+1}(C)\overset{\delta}{\longrightarrow}T_n(A)\longrightarrow T_n(B)\longrightarrow T_n(C)\overset{\delta}{\longrightarrow}T_{n-1}(A)\longrightarrow \cdots$$

    is exact.
2. (Naturality) Given a homomorphism between short exact sequences

    ![morphism_of_short_exact_sequence](/assets/images/Math/Homological_Algebra/Derived_Functors-1.png){:style="width:18em" class="invert" .align-center}

    the following diagram

    ![naturality_of_delta_functor](/assets/images/Math/Homological_Algebra/Derived_Functors-2.png){:style="width:32em" class="invert" .align-center}

    commutes.

</div>

Rewriting the above definition with $$T^n$$ and $$\delta^n:T^n(C)\rightarrow T^{n+1}(A)$$, we obtain the definition of a *cohomological $$\delta$$-functor*. Since we have agreed to regard both $$T_n$$ and $$T^n$$ as zero when $$n<0$$, the first condition for a homological $$\delta$$-functor means in particular that

$$\cdots\longrightarrow T_0(A)\longrightarrow T_0(B)\longrightarrow T_0(C)\longrightarrow0\longrightarrow 0\longrightarrow\cdots, $$

that is, $$T_0$$ is a right exact functor. Similarly, the first condition for a cohomological $$\delta$$-functor makes $$T^0$$ a left exact functor.

Also, the second condition of a $$\delta$$-functor, naturality, means that when we regard $$T_i(C)$$ and $$T_{i-1}(A)$$ as functors from the category of short exact sequences $$\mathbf{S}(\mathcal{A})$$ to $$\mathcal{A}$$, each $$\delta_i$$ is a natural transformation between them.

As always, the cohomological case can be easily derived from the homological one, so we shall consider only homological $$\delta$$-functors from now on.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> Let two $$\delta$$-functors $$S,T$$ be given. Then a *morphism* $$S\rightarrow T$$ is a collection of natural transformations from $$S_n$$ to $$T_n$$ that commute with $$\delta$$.

</div>

In other words, it is a collection of natural transformations $$\alpha_n:S_n\Rightarrow T_n$$ making the following diagram commute for every short exact sequence

$$0\longrightarrow A\longrightarrow B\longrightarrow C\longrightarrow 0$$

![morphism_of_delta_functor](/assets/images/Math/Homological_Algebra/Derived_Functors-3.png){:style="width:36em" class="invert" .align-center}

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> A $$\delta$$-functor $$T$$ is called a *universal $$\delta$$-functor* if, whenever a $$\delta$$-functor $$S$$ and a natural transformation $$\alpha_0:S_0\rightarrow T_0$$ are given, there exists a unique morphism $$(\alpha_n:S_n\Rightarrow T_n)$$ of $$\delta$$-functors extending it.

</div>

## Derived Functors

Consider a right exact functor $$F: \mathcal{A}\rightarrow \mathcal{B}$$ between two abelian categories $$\mathcal{A}$$ and $$\mathcal{B}$$. Then $$F$$ does not preserve left exactness. For example, if $$F$$ is covariant, then even when the short exact sequence

$$0 \rightarrow A_1 \rightarrow A_2 \rightarrow A_3 \rightarrow 0$$

is given, only the exactness of the sequence

$$F(A_1) \rightarrow F(A_2) \rightarrow F(A_3)\rightarrow 0$$

is preserved. Likewise, a left exact functor does not preserve right exactness.

The philosophy of derived functors is to recover the information lost on one side by introducing infinitely many additional terms. Thus, for a right exact functor $$F$$, our goal is to find a homological $$\delta$$-functor with $$T_0=F$$, and similarly for a left exact functor, our goal is to find a cohomological $$\delta$$-functor.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> Let a right exact functor $$F:\mathcal{A}\rightarrow \mathcal{B}$$ be given, and suppose $$\mathcal{A}$$ has enough projectives. Then the *left derived functors* $$L_iF$$ of $$F$$ are defined by the formula

$$(L_iF)(A)=H_i(F(P_\bullet)),\qquad\text{$P_\bullet$ a projective resolution of $A$}$$

</div>

For this definition to make sense, $$L_iF(A)$$ must not depend on the choice of $$P_\bullet$$ above.

<div class="proposition" markdown="1">

<ins id="lem5">**Lemma 5**</ins> $$L_iF(A)$$ does not depend on the choice of $$P_\bullet$$ above.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Take two projective resolutions and apply [§Resolutions, ⁋Theorem 6](/en/math/homological_algebra/resolutions#thm6) to the identity map.

</details>

Now let us examine left derived functors in more detail. First, since $$F$$ is right exact, we know that the sequence

$$F(P_1) \overset{Fd_1}{\longrightarrow} F(P_0) \overset{F\epsilon_0}{\longrightarrow} F(A) \longrightarrow 0$$

is exact. Therefore, we obtain

$$L_0F(A)=H_i(F(P))=\frac{F(P_0)}{\im Fd_1}=\frac{F(P_0)}{\ker F\epsilon_0}\cong F(A)$$

To show that the $$L_\bullet F$$ form a homological $$\delta$$-functor, we must first show that they are additive functors, and then construct the connecting maps $$\delta$$. We divide this into two steps.

<div class="proposition" markdown="1">

<ins id="lem6">**Lemma 6**</ins> The $$L_iF$$ are additive functors.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, given any $$f: A' \rightarrow A$$ and projective resolutions of $$A'$$ and $$A$$ respectively, we can apply [§Resolutions, ⁋Theorem 6](/en/math/homological_algebra/resolutions#thm6) to obtain $$L_nF(f)$$. That this satisfies functoriality and additivity is obvious from the universal property.

</details>

<div class="proposition" markdown="1">

<ins id="lem7">**Lemma 7**</ins> The $$L_iF$$ form a homological $$\delta$$-functor.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, suppose a short exact sequence

$$0 \rightarrow A \rightarrow B \rightarrow C \rightarrow 0$$

is given. If projective resolutions $$P_\bullet$$ of $$A$$ and $$R_\bullet$$ of $$C$$ are given, then using [§Resolutions, ⁋Lemma 7](/en/math/homological_algebra/resolutions#lem7) we obtain a projective resolution $$Q_\bullet \rightarrow B$$. On the other hand, since each $$R_n$$ is projective, the sequence

$$0 \rightarrow P_n \rightarrow Q_n \rightarrow R_n \rightarrow 0$$

is split exact. From this,

$$0 \rightarrow F(P_\bullet) \rightarrow F(Q_\bullet) \rightarrow F(R_\bullet) \rightarrow 0$$

is also a short exact sequence ([\[Multilinear Algebra\] §Hom and the Tensor Product, ⁋Proposition 1](/en/math/multilinear_algebra/hom_and_tensor#prop1)), and considering the homology sequence here, we obtain the desired connecting maps and the long exact sequence of left derived functors

$$\cdots\overset{\partial}{\longrightarrow}L_iF(A')\longrightarrow L_iF(A)\longrightarrow L_iF(A'')\overset{\partial}{\longrightarrow}L_{i-1}F(A')\longrightarrow L_{i-1}F(A)\longrightarrow L_iF(A'')\overset{\partial}{\longrightarrow}\cdots$$

That the information thus obtained satisfies the second condition of [Definition 1](#def1) follows from [§Resolutions, ⁋Theorem 6](/en/math/homological_algebra/resolutions#thm6).

</details>

Moreover, they define a *universal* homological $$\delta$$-functor in the sense of [Definition 3](#def3). We omit the proof of this.

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8**</ins> Consider an abelian category $$\mathcal{A}$$ with enough projectives and any right exact functor $$F: \mathcal{A}\rightarrow \mathcal{B}$$. Then the derived functors $$L_nF$$ are universal $$\delta$$-functors.

</div>

Just as in the discussion above, we can also define right derived functors for a left exact functor. Its definition is the "dual" of [Definition 4](#def4).

<div class="definition" markdown="1">

<ins id="def9">**Definition 9**</ins> Let a left exact functor $$F:\mathcal{A}\rightarrow \mathcal{B}$$ be given, and suppose $$\mathcal{A}$$ has enough injectives. Then the *right derived functors* $$R^i F$$ of $$F$$ are defined by the formula

$$(R^iF)(A)=H_i(F(I^\bullet)),\qquad\text{$I^\bullet$ an injective resolution of $A$}$$

</div>

Then one can also show that these are universal cohomological $$\delta$$-functors. The reason we use superscripts, unlike in [Definition 4](#def4), is that these are literally *cohomological* $$\delta$$-functors, and they arise mainly when dealing with matters related to cohomology.
