---
title: "Resolutions"
description: "This post defines projective and injective objects in an Abelian category, and explains the concepts of left and right resolutions, including projective and injective resolutions."
excerpt: "Projective and injective resolutions in an Abelian category"

categories: [Math / Homological Algebra]
permalink: /en/math/homological_algebra/resolutions
sidebar: 
    nav: "homological_algebra-en"

date: 2024-11-01
weight: 4
translated_at: 2026-07-13T13:00:02+00:00
translation_source: kimi-cli
---
## Projective and Injective Resolutions

We defined projective and injective modules in [[Multilinear Algebra] §Projective, Injective, and Flat Modules, ⁋Definition 3](/en/math/multilinear_algebra/various_modules#def3). Rephrasing this in the language of diagrams, we obtain the notions of projective object and injective object in a general abelian category.

::: Definition 1
Fix an abelian category $\mathcal{A}$.

1. An object $P$ of $\mathcal{A}$ is called a *projective object* if whenever the following diagram is given

    ![Projective_object-1](/assets/images/Math/Homological_Algebra/Resolutions-1.svg){:style="width:9.44em" class="invert" .align-center}

    there exists at least one morphism $P \rightarrow B$ making the following diagram

    ![Projective_object-2](/assets/images/Math/Homological_Algebra/Resolutions-2.svg){:style="width:9.44em" class="invert" .align-center}

    commute.  
    If for every object $A$ of $\mathcal{A}$ there exists a suitable projective object $P$ such that $P \rightarrow A \rightarrow 0$ is exact, we say that $\mathcal{A}$ has *enough projectives*.
2. An object $I$ of $\mathcal{A}$ is called an *injective object* if whenever the following diagram is given

    ![Injective_object-1](/assets/images/Math/Homological_Algebra/Resolutions-3.svg){:style="width:9.40em" class="invert" .align-center}

    there exists at least one morphism $B \rightarrow I$ making the following diagram

    ![Injective_object-2](/assets/images/Math/Homological_Algebra/Resolutions-4.svg){:style="width:9.40em" class="invert" .align-center}

    commute.  
    If for every object $A$ of $\mathcal{A}$ there exists a suitable injective object $I$ such that $0 \rightarrow A \rightarrow I$ is exact, we say that $\mathcal{A}$ has *enough injectives*.
:::

We also define the following.

::: Definition 2
For an object $M$ of an abelian category $\mathcal{A}$, we define the following.

1. A *left resolution* of $M$ is a chain complex $P_\bullet$ and an *augmentation map* $\epsilon: P_0 \rightarrow M$ such that the chain complex

    $$\cdots \longrightarrow P_2 \longrightarrow P_1 \longrightarrow P_0 \overset{\epsilon}{\longrightarrow} M \longrightarrow 0$$

    is exact. If all the $P_i$ are projective objects, we call this a *projective resolution*.
2. A *right resolution* of $M$ is a cochain complex $I^\bullet$ and an *augmentation map* $\eta: M \rightarrow I^0$ such that the cochain complex

    $$0 \longrightarrow M \overset{\eta}{\longrightarrow} I^0 \longrightarrow I^1 \longrightarrow I^2 \longrightarrow \cdots$$

    is exact. If all the $I^i$ are injective objects, we call this an *injective resolution*.
:::

A projective object in $\mathcal{A}$ is an injective object in $\mathcal{A}^\op$. Similarly, if $\mathcal{A}$ has enough projectives then $\mathcal{A}^\op$ has enough injectives. Also, a projective resolution of $M$ in $\mathcal{A}$ is the same as an injective resolution of $M$ in $\mathcal{A}^\op$. Therefore, it suffices to prove the following proposition only for projective resolutions.

::: Proposition 3
If an abelian category $\mathcal{A}$ has enough projectives, then every object $M$ of $\mathcal{A}$ has a projective resolution. Similarly, if an abelian category $\mathcal{A}$ has enough injectives, then every object $M$ of $\mathcal{A}$ has an injective resolution.
:::
::: Proof
First, since $\mathcal{A}$ has enough projectives, we can choose a suitable surjection $\epsilon_0:P_0 \rightarrow M$. Let $M_0=\ker \epsilon_0$. Then since $\mathcal{A}$ has enough projectives, we can choose a suitable surjection $\epsilon_1:P_1 \rightarrow M_0$. Drawing the composition of $\epsilon_1: P_1 \rightarrow M_0$ and the inclusion $\iota_0: M_0 \rightarrow P_0$ as $d_1=\iota_0\circ\epsilon_1$ in a diagram, we obtain the following.

![splicing-1](/assets/images/Math/Homological_Algebra/Resolutions-5.svg){:style="width:19.97em" class="invert" .align-center}

Continuing in this way, whenever $\epsilon_n:P_n \rightarrow M_{n-1}$ is given we set $M_n=\ker \epsilon_n$ and obtain the following commutative diagram

![splicing-2](/assets/images/Math/Homological_Algebra/Resolutions-6.svg){:style="width:39.85em" class="invert" .align-center}

Then looking at the complex obtained in the middle,

$$\cdots \overset{d_3}{\longrightarrow} P_2 \overset{d_2}{\longrightarrow} P_1 \overset{d_1}{\longrightarrow} P_0 \overset{\epsilon_0}{\longrightarrow} M \longrightarrow 0$$

we obtain the identity

$$\im(d_n)=\im(\iota_{n-1}\circ\epsilon_n)=\im(\iota_{n-1})=\ker(\epsilon_{n-1})=\ker(\iota_{n-2}\circ\epsilon_{n-1})=\ker(d_{n-1}).$$

Here, the identity $\im(\iota_{n-1}\circ\epsilon_n)=\im(\iota_{n-1})$ uses the fact that $\epsilon_n$ is surjective, and the identity $\ker(\epsilon_{n-1})=\ker(d_{n-1})$ uses the fact that $\iota_{n-2}$ is injective. Therefore $P_\bullet$ is a projective resolution of $M$.
:::

One of our goals in this post is to prove that every $A$-module always has both a projective resolution and an injective resolution. Using [Proposition 3](#prop3), it suffices to prove that $\lMod{A}$ has enough projectives and enough injectives. That $\lMod{A}$ has enough projectives is trivial.

::: Proposition 4
The category $\lMod{A}$ has enough projectives.
:::
::: Proof
This follows immediately from [[Multilinear Algebra] §Bases, ⁋Proposition 2](/en/math/multilinear_algebra/basis_of_free_modules#prop2) and [[Multilinear Algebra] §Projective, Injective, and Flat Modules, ⁋Proposition 4](/en/math/multilinear_algebra/various_modules#prop4).
:::

However, since we know nothing about $\lMod{A}^\op$, it does not follow from the above result that $\lMod{A}$ has enough injectives. Therefore the following proposition requires a separate proof.

::: Proposition 5
The category $\lMod{A}$ has enough injectives.
:::
::: Proof
One can easily show that right adjoints preserve injective objects. Then the coextension of scalars $\Ab \rightarrow \lMod{A}$ obtained from the ring homomorphism $\mathbb{Z}\rightarrow A$ is a right adjoint of restriction of scalars, so injective objects in $\Ab$ become injective objects in $\lMod{A}$. ([[Algebraic Structures] §Change of Base Ring, ⁋Proposition 7](/en/math/algebraic_structures/change_of_base_ring#prop7)) Thus it suffices to prove that $\Ab$ has enough injectives. For any $A\in\Ab$, this is achieved by setting

$$I(A)=\prod_{f\in\Hom_\Ab(A, \mathbb{Q}/\mathbb{Z})} \mathbb{Q}/\mathbb{Z}$$

and defining $e_A:A \rightarrow I(A)$ by $a\mapsto (f(a))_{f\in\Hom(A, \mathbb{Q}/\mathbb{Z})}$.
:::

## Uniqueness of Resolutions

Meanwhile, the uniqueness of projective and injective resolutions follows from the following stronger theorem.

::: Theorem 6
Given a projective resolution $P_\bullet \rightarrow M$ and any $u:M \rightarrow N$. Then for any left resolution $Q_\bullet \rightarrow N$, there exists a chain map $f:P_\bullet \rightarrow Q_\bullet$ making the following diagram

![comparison_proj](/assets/images/Math/Homological_Algebra/Resolutions-7.svg){:style="width:20.02em" class="invert" .align-center}

commute, uniquely up to homotopy.  
Similarly, given an injective resolution $N \rightarrow I^\bullet$ and any $u: M \rightarrow N$, for any right resolution $M \rightarrow J^\bullet$ there exists a chain map $f:J^\bullet \rightarrow I^\bullet$ making the following diagram

![comparison_inj](/assets/images/Math/Homological_Algebra/Resolutions-8.svg){:style="width:19.71em" class="invert" .align-center}

commute.
:::
::: Proof
First we prove the first claim. Write the augmentations of the two resolutions as $\varepsilon:P_0 \rightarrow M$ and $\varepsilon':Q_0 \rightarrow N$ respectively.

**(Existence of chain map)** We construct the $f_n$ inductively. Since $\varepsilon'$ is surjective and $P_0$ is projective, for $u\circ\varepsilon:P_0 \rightarrow N$ there exists $f_0:P_0 \rightarrow Q_0$ such that $\varepsilon'\circ f_0=u\circ \varepsilon$. Now suppose $f_0,\ldots,f_{n-1}$ have been constructed to make the given diagram commute, and consider the composition $\varphi=f_{n-1}\circ d_n^P:P_n \rightarrow Q_{n-1}$. Then for $n\geq 2$,

$$d_{n-1}^Q\circ\varphi=d_{n-1}^Q\circ f_{n-1}\circ d_n^P=f_{n-2}\circ d_{n-1}^P\circ d_n^P=0$$

and for $n=1$ we also have $\varepsilon'\circ f_0\circ d_1^P=u\circ\varepsilon\circ d_1^P=0$. Therefore $\im\varphi$ is contained in $\ker d_{n-1}^Q$ (or $\ker\varepsilon'$ when $n=1$), which equals $\im d_n^Q$ since $Q_\bullet \rightarrow N$ is a resolution. Then since $P_n$ is projective and $d_n^Q:Q_n \rightarrow \im d_n^Q$ is surjective, there exists $f_n:P_n \rightarrow Q_n$ such that $d_n^Q\circ f_n=\varphi$.

**(Uniqueness up to homotopy)** Suppose $f,f'$ are both chain maps making the given diagram commute, and let $g=f-f'$. Then $g$ is a chain map satisfying $\varepsilon'\circ g_0=u\circ\varepsilon-u\circ\varepsilon=0$. We construct a homotopy $s_n:P_n \rightarrow Q_{n+1}$ inductively such that $g_n=d_{n+1}^Q\circ s_n+s_{n-1}\circ d_n^P$ holds for all $n$. Here $s_{-1}=0$.

First, from $\varepsilon'\circ g_0=0$ we have $\im g_0\subseteq \ker\varepsilon'=\im d_1^Q$, so by projectivity of $P_0$ there exists $s_0:P_0 \rightarrow Q_1$ such that $d_1^Q\circ s_0=g_0$. Now suppose $s_0,\ldots,s_{n-1}$ have been constructed and let $\psi=g_n-s_{n-1}\circ d_n^P$. Then

$$d_n^Q\circ\psi=d_n^Q\circ g_n-(d_n^Q\circ s_{n-1})\circ d_n^P=g_{n-1}\circ d_n^P-(g_{n-1}-s_{n-2}\circ d_{n-1}^P)\circ d_n^P=s_{n-2}\circ d_{n-1}^P\circ d_n^P=0$$

so $\im\psi\subseteq\ker d_n^Q=\im d_{n+1}^Q$, and again by projectivity of $P_n$ there exists $s_n:P_n \rightarrow Q_{n+1}$ such that $d_{n+1}^Q\circ s_n=\psi$. Then by definition $g_n=d_{n+1}^Q\circ s_n+s_{n-1}\circ d_n^P$.

Now we prove the second claim. This is obtained by dualizing the proof of the first claim verbatim. Let the augmentations of the two resolutions be $\eta:M \rightarrow J^0$ and $\eta':N \rightarrow I^0$. Since $\eta$ is injective and $I^0$ is an injective object, for $\eta'\circ u:M \rightarrow I^0$ there exists $f^0:J^0 \rightarrow I^0$ such that $f^0\circ\eta=\eta'\circ u$. Suppose $f^0,\ldots,f^{n-1}$ have been constructed inductively and consider the composition $d_I^{n-1}\circ f^{n-1}:J^{n-1} \rightarrow I^n$; by the same computation as above this map is zero on $\im d_J^{n-2}=\ker d_J^{n-1}$, and therefore induces a morphism to $I^n$ via the injective morphism $J^{n-1}/\ker d_J^{n-1}\hookrightarrow J^n$. Since $I^n$ is an injective object, we extend this to all of $J^n$ to obtain $f^n:J^n \rightarrow I^n$, and by this construction $f^n\circ d_J^{n-1}=d_I^{n-1}\circ f^{n-1}$ holds.
:::

Finally, we conclude by proving the following lemma, which will be used importantly in the next post.

::: Lemma 7
Given the following short exact sequence

$$0 \longrightarrow A'\overset{i}{\longrightarrow}A\overset{p}{\longrightarrow}A'' \longrightarrow 0$$

and projective resolutions $P_\bullet'$, $P_\bullet''$ of $A'$, $A''$ respectively. Then the chain complex $P_\bullet$ defined by $P_n=P_n'\oplus P_n''$ is a projective resolution of $A$, and there exists an exact sequence of these complexes

$$0 \rightarrow P' \rightarrow P \rightarrow P'' \rightarrow 0.$$
:::
::: Proof
First, drawing the given situation in a diagram, we obtain the following.

![horseshoe-initial](/assets/images/Math/Homological_Algebra/Resolutions-9.svg){:style="width:20.34em" class="invert" .align-center}

Now from the condition that $P_0''$ is projective, we can define $P_0'' \rightarrow A$. On the other hand, $P_0' \rightarrow A$ is already given as the composition of $i_A$ and $\epsilon'$, so taking their direct sum we obtain $\epsilon:P_0 \rightarrow A$. Then from [§Diagram Chasing, ⁋Lemma 5](/en/math/homological_algebra/diagram_chasing#lem5) we obtain the following diagram

![horseshoe-induction](/assets/images/Math/Homological_Algebra/Resolutions-10.svg){:style="width:20.84em" class="invert" .align-center}

and in particular the following diagram

![horseshoe-finish](/assets/images/Math/Homological_Algebra/Resolutions-11.svg){:style="width:21.61em" class="invert" .align-center}

Repeating this process, we obtain $P_\bullet$.
:::
