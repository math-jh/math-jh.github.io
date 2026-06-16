---
title: "Resolutions"
description: "This post defines projective and injective objects in an Abelian category, and explains the concepts of left and right resolutions, including projective and injective resolutions."
excerpt: "Projective and injective resolutions in an abelian category"

categories: [Math / Homological Algebra]
permalink: /en/math/homological_algebra/resolutions
sidebar: 
    nav: "homological_algebra-en"

date: 2024-11-01
weight: 4
published: false
translated_at: 2026-05-31T13:30:03+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-31T13:30:03+00:00
---
## Projective and Injective Resolutions

We defined projective and injective modules in [\[Multilinear Algebra\] §Projective, Injective, and Flat Modules, ⁋Definition 3](/en/math/multilinear_algebra/various_modules#def3). Rephrasing this in the language of diagrams, we obtain the notions of projective object and injective object in a general abelian category.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Fix an abelian category $$\mathcal{A}$$.

1. An object $$P$$ of $$\mathcal{A}$$ is a *projective object* if, whenever a diagram
    
    ![Projective_object-1](/assets/images/Math/Homological_Algebra/Resolutions-1.svg){:style="width:9.44em" class="invert" .align-center}

    is given, there exists at least one morphism $$P \rightarrow B$$ making the following diagram
    
    ![Projective_object-2](/assets/images/Math/Homological_Algebra/Resolutions-2.svg){:style="width:9.44em" class="invert" .align-center}

    commute. If for every object $$A$$ in $$\mathcal{A}$$ there exists a projective object $$P$$ such that $$P \rightarrow A \rightarrow 0$$ can be made exact, we say that $$\mathcal{A}$$ has *enough projectives*.
2. An object $$I$$ of $$\mathcal{A}$$ is an *injective object* if, whenever a diagram
    
    ![Injective_object-1](/assets/images/Math/Homological_Algebra/Resolutions-3.svg){:style="width:9.40em" class="invert" .align-center}

    is given, there exists at least one morphism $$B \rightarrow I$$ making the following diagram
    
    ![Injective_object-2](/assets/images/Math/Homological_Algebra/Resolutions-4.svg){:style="width:9.40em" class="invert" .align-center}

    commute. If for every object $$A$$ in $$\mathcal{A}$$ there exists an injective object $$I$$ such that $$0 \rightarrow A \rightarrow I$$ can be made exact, we say that $$\mathcal{A}$$ has *enough injectives*. 

</div>

We also make the following definition.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> Let $$M$$ be an object of an abelian category $$\mathcal{A}$$.

1. A *left resolution* of $$M$$ is a chain complex $$P_\bullet$$ together with an *augmentation map* $$\epsilon: P_0 \rightarrow M$$ such that the chain complex
    
    $$\cdots \longrightarrow P_2 \longrightarrow P_1 \longrightarrow P_0 \overset{\epsilon}{\longrightarrow} M \longrightarrow 0$$

    is exact. If each $$P_i$$ is a projective object, we call this a *projective resolution*.
2. A *right resolution* of $$M$$ is a cochain complex $$I^\bullet$$ together with an *augmentation map* $$\eta: M \rightarrow I^0$$ such that the cochain complex
    
    $$0 \longrightarrow M \overset{\eta}{\longrightarrow} I^0 \longrightarrow I^1 \longrightarrow I^2 \longrightarrow \cdots$$

    is exact. If each $$I^i$$ is an injective object, we call this an *injective resolution*.

</div>

A projective object in $$\mathcal{A}$$ is an injective object in $$\mathcal{A}^\op$$. Likewise, if $$\mathcal{A}$$ has enough projectives then $$\mathcal{A}^\op$$ has enough injectives. Moreover, a projective resolution of $$M$$ in $$\mathcal{A}$$ coincides with an injective resolution of $$M$$ in $$\mathcal{A}^\op$$. Therefore, it suffices to prove the following proposition only for projective resolutions.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> If an abelian category $$\mathcal{A}$$ has enough projectives, then every object $$M$$ in $$\mathcal{A}$$ has a projective resolution. Likewise, if an abelian category $$\mathcal{A}$$ has enough injectives, then every object $$M$$ in $$\mathcal{A}$$ has an injective resolution.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, since $$\mathcal{A}$$ has enough projectives, we can choose a surjection $$\epsilon_0:P_0 \rightarrow M$$. Let $$M_0=\ker \epsilon_0$$. Then since $$\mathcal{A}$$ has enough projectives, we can choose a surjection $$\epsilon_1:P_1 \rightarrow M_0$$. Drawing the diagram up to the composite $$d_1=\iota_0\circ\epsilon_1$$ of $$\epsilon_1: P_1 \rightarrow M_0$$ and the inclusion $$\iota_0: M_0 \rightarrow P_0$$, we obtain the following.

![splicing-1](/assets/images/Math/Homological_Algebra/Resolutions-5.svg){:style="width:19.97em" class="invert" .align-center}

Proceeding in this way, whenever $$\epsilon_n:P_n \rightarrow M_{n-1}$$ is given we set $$M_n=\ker \epsilon_n$$ to obtain the following commutative diagram.

![splicing-2](/assets/images/Math/Homological_Algebra/Resolutions-6.svg){:style="width:39.85em" class="invert" .align-center}

Then the complex obtained in the middle,

$$\cdots \overset{d_3}{\longrightarrow} P_2 \overset{d_2}{\longrightarrow} P_1 \overset{d_1}{\longrightarrow} P_0 \overset{\epsilon_0}{\longrightarrow} M \longrightarrow 0$$

gives the following equalities:

$$\im(d_n)=\im(\iota_{n-1}\circ\epsilon_n)=\im(\iota_{n-1})=\ker(\epsilon_{n-1})=\ker(\iota_{n-2}\circ\epsilon_{n-1})=\ker(d_{n-1})$$

Here, the equality $$\im(\iota_{n-1}\circ\epsilon_n)=\im(\iota_{n-1})$$ uses the fact that $$\epsilon_n$$ is surjective, and the equality $$\ker(\epsilon_{n-1})=\ker(d_{n-1})$$ uses the fact that $$\iota_{n-2}$$ is injective. Therefore $$P_\bullet$$ is a projective resolution of $$M$$.

</details>

One of our goals in this post is to prove that every $$A$$-module always has a projective resolution and an injective resolution. Using [Proposition 3](#prop3), it suffices to prove that $$\lMod{A}$$ has enough projectives and enough injectives. That $$\lMod{A}$$ has enough projectives is obvious.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> The category $$\lMod{A}$$ has enough projectives.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

This is obvious by [\[Multilinear Algebra\] §Bases, ⁋Proposition 2](/en/math/multilinear_algebra/basis_of_free_modules#prop2) and [\[Multilinear Algebra\] §Projective, Injective, and Flat Modules, ⁋Proposition 4](/en/math/multilinear_algebra/various_modules#prop4).

</details>

However, since we know nothing about $$\lMod{A}^\op$$, the fact that $$\lMod{A}$$ has enough injectives does not follow from the above result. Therefore, the following proposition requires a separate proof.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> The category $$\lMod{A}$$ has enough injectives.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

It is not difficult to show that a right adjoint preserves injective objects. Then the coextension of scalars $$\Ab \rightarrow \lMod{A}$$ obtained from the ring homomorphism $$\mathbb{Z}\rightarrow A$$ is the right adjoint of restriction of scalars, so an injective object in $$\Ab$$ becomes an injective object in $$\lMod{A}$$. ([\[Algebraic Structures\] §Change of Base Ring, ⁋Proposition 7](/en/math/algebraic_structures/change_of_base_ring#prop7)) Thus, for the desired proof it suffices to prove that $$\Ab$$ has enough injectives. For any $$A\in\Ab$$, this is done by defining

$$I(A)=\prod_{f\in\Hom_\Ab(A, \mathbb{Q}/\mathbb{Z})} \mathbb{Q}/\mathbb{Z}$$

and $$e_A:A \rightarrow I(A)$$ by $$a\mapsto (f(a))_{f\in\Hom(A, \mathbb{Q}/\mathbb{Z})}$$.

</details>

## Uniqueness of Resolutions

Meanwhile, the uniqueness of projective and injective resolutions follows from the following stronger theorem.

<div class="proposition" markdown="1">

<ins id="thm6">**Theorem 6**</ins> Let a projective resolution $$P_\bullet \rightarrow M$$ and any $$u:M \rightarrow N$$ be given. Then for every left resolution $$Q_\bullet \rightarrow N$$, there exists a chain map $$f:P_\bullet \rightarrow Q_\bullet$$ making the following diagram

![comparison_proj](/assets/images/Math/Homological_Algebra/Resolutions-7.svg){:style="width:20.02em" class="invert" .align-center}

commute, uniquely up to homotopy.  
Similarly, let an injective resolution $$N \rightarrow I^\bullet$$ and any $$u: M \rightarrow N$$ be given. Then for every right resolution $$M \rightarrow J^\bullet$$, there exists a chain map $$f:J^\bullet \rightarrow I^\bullet$$ making the following diagram

![comparison_inj](/assets/images/Math/Homological_Algebra/Resolutions-8.svg){:style="width:19.71em" class="invert" .align-center}

commute.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>



</details>

Finally, we conclude by proving the following lemma, which will be used importantly in the next post.

<div class="proposition" markdown="1">

<ins id="lem7">**Lemma 7**</ins> Let the following short exact sequence

$$0 \longrightarrow A'\overset{i}{\longrightarrow}A\overset{p}{\longrightarrow}A'' \longrightarrow 0$$

be given, and let $$P_\bullet'$$, $$P_\bullet''$$ be projective resolutions of $$A'$$, $$A''$$. Then the chain complex $$P_\bullet$$ defined by $$P_n=P_n'\oplus P_n''$$ is a projective resolution of $$A$$, and there exists a short exact sequence of these complexes

$$0 \rightarrow P' \rightarrow P \rightarrow P'' \rightarrow 0$$

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, drawing the given situation as a diagram, we obtain the following.

![horseshoe-initial](/assets/images/Math/Homological_Algebra/Resolutions-9.svg){:style="width:20.34em" class="invert" .align-center}

Now from the condition that $$P_0''$$ is projective, we can define $$P_0'' \rightarrow A$$. On the other hand, $$P_0' \rightarrow A$$ is already given as the composite of $$i_A$$ and $$\epsilon'$$, so considering their direct sum we obtain $$\epsilon:P_0 \rightarrow A$$. Now from [§Diagram Chasing, ⁋Lemma 5](/en/math/homological_algebra/diagram_chasing#lem5) we obtain the following diagram

![horseshoe-induction](/assets/images/Math/Homological_Algebra/Resolutions-10.svg){:style="width:20.84em" class="invert" .align-center}

and in particular we obtain the following diagram

![horseshoe-finish](/assets/images/Math/Homological_Algebra/Resolutions-11.svg){:style="width:21.61em" class="invert" .align-center}

Repeating this process, we obtain $$P_\bullet$$.

</details>
