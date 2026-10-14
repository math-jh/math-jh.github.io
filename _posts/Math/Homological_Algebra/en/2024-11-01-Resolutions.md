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
translated_at: 2026-07-14T00:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-11T03:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
## Projective and Injective Resolutions

We defined projective and injective modules in [\[Multilinear Algebra\] §Projective, Injective, and Flat Modules, ⁋Definition 3](/en/math/multilinear_algebra/various_modules#def3){: data-lid="r6nwy" }. Rephrasing this in the language of diagrams, we obtain the notions of projective object and injective object in a general abelian category.

::: Definition 1
Fix an abelian category $\mathcal{A}$.

1. In $\mathcal{A}$, an object $P$ is called a *projective object* if whenever the following diagram
    
    {% diagram Math/Homological_Algebra/Resolutions-1.svg width="9.44em" alt="Projective_object-1" %}

    is given, there exists at least one $P \rightarrow B$ making the following diagram

    {% diagram Math/Homological_Algebra/Resolutions-2.svg width="9.44em" alt="Projective_object-2" %}

    commute.  
    If in $\mathcal{A}$, for every object $A$, there exists a suitable projective object $P$ such that $P \rightarrow A \rightarrow 0$ is exact, we say that $\mathcal{A}$ has *enough projectives*. 
2. In $\mathcal{A}$, an object $I$ is called an *injective object* if whenever the following diagram
    
    {% diagram Math/Homological_Algebra/Resolutions-3.svg width="9.40em" alt="Injective_object-1" %}

    is given, there exists at least one $B \rightarrow I$ making the following diagram

    {% diagram Math/Homological_Algebra/Resolutions-4.svg width="9.40em" alt="Injective_object-2" %}

    commute.  
    If in $\mathcal{A}$, for every object $A$, there exists a suitable injective object $I$ such that $0 \rightarrow A \rightarrow I$ is exact, we say that $\mathcal{A}$ has *enough injectives*. 
:::

We also define the following.

::: Definition 2
In an abelian category $\mathcal{A}$, for an object $M$, we define the following.

1. A *left resolution* of $M$ is, such that the following chain complex
    
    $$\cdots \rightarrow P_2 \rightarrow P_1 \rightarrow P_0 \overset{\epsilon}{\rightarrow} M \rightarrow 0$$

    is exact, a chain complex $P_\bullet$ and an *augmentation map* $\epsilon: P_0 \rightarrow M$. If all the $P_i$ are projective objects, we call this a *projective resolution*.
2. A *right resolution* of $M$ is, such that the following cochain complex
    
    $$0 \rightarrow M \overset{\eta}{\rightarrow} I^0 \rightarrow I^1 \rightarrow I^2 \rightarrow \cdots$$

    is exact, a cochain complex $I^\bullet$ and an *augmentation map* $\eta: M \rightarrow I^0$. If all the $I^i$ are injective objects, we call this an *injective resolution*.
:::

A projective object in $\mathcal{A}$ is an injective object in $\mathcal{A}^\op$. Similarly, if $\mathcal{A}$ has enough projectives, then $\mathcal{A}^\op$ has enough injectives. Also, a projective resolution of $M$ in $\mathcal{A}$ is the same as an injective resolution of $M$ in $\mathcal{A}^\op$. Therefore, it suffices to prove the following proposition only for projective resolutions.

::: Proposition 3
If an abelian category $\mathcal{A}$ has enough projectives, then in $\mathcal{A}$, every object $M$ has a projective resolution. Similarly, if an abelian category $\mathcal{A}$ has enough injectives, then in $\mathcal{A}$, every object $M$ has an injective resolution.
:::
::: Proof
First, since $\mathcal{A}$ has enough projectives, we can choose a suitable surjection $\epsilon_0:P_0 \rightarrow M$. Let $M_0=\ker \epsilon_0$. Then since $\mathcal{A}$ has enough projectives, we can choose a suitable surjection $\epsilon_1:P_1 \rightarrow M_0$. Now, drawing the composition of $\epsilon_1: P_1 \rightarrow M_0$ and the inclusion $\iota_0: M_0 \rightarrow P_0$ as $d_1=\iota_0\circ\epsilon_1$ in a diagram, we obtain the following.

{% diagram Math/Homological_Algebra/Resolutions-5.svg width="19.97em" alt="splicing-1" %}

Continuing in this way, whenever $\epsilon_n:P_n \rightarrow M_{n-1}$ is given, we set $M_n=\ker \epsilon_n$ to obtain the following commutative diagram

{% diagram frozen/635a8f80/Math/Homological_Algebra/Resolutions-6.svg width="39.85em" alt="splicing-2" %}

Then looking at

$$\cdots \overset{d_3}{\rightarrow} P_2 \overset{d_2}{\rightarrow} P_1 \overset{d_1}{\rightarrow} P_0 \overset{\epsilon_0}{\rightarrow} M \rightarrow 0$$

obtained in the middle, for $n\geq 2$ we obtain the following equation

$$\im(d_n)=\im(\iota_{n-1}\circ\epsilon_n)=\im(\iota_{n-1})=\ker(\epsilon_{n-1})=\ker(\iota_{n-2}\circ\epsilon_{n-1})=\ker(d_{n-1})$$

and for $n=1$ we also have $\im(d_1)=\im(\iota_0\circ\epsilon_1)=\im(\iota_0)=\ker(\epsilon_0)$. Here, the equation $\im(\iota_{n-1}\circ\epsilon_n)=\im(\iota_{n-1})$ uses the fact that $\epsilon_n$ is surjective, and the equation $\ker(\epsilon_{n-1})=\ker(d_{n-1})$ uses the fact that $\iota_{n-2}$ is injective, respectively. Therefore $P_\bullet$ is a projective resolution of $M$.
:::

One of our goals in this post is to prove that every $A$-module always has a projective resolution and an injective resolution. Using [Proposition 3](#prop3){: data-lid="f3ivp" }, it suffices to prove that $\lMod{A}$ has enough projectives and enough injectives. That $\lMod{A}$ has enough projectives is trivial.

::: Proposition 4
The category $\lMod{A}$ has enough projectives.
:::
::: Proof
For any $M\in\lMod{A}$, from [\[Multilinear Algebra\] §Bases, ⁋Proposition 2](/en/math/multilinear_algebra/basis_of_free_modules#prop2){: data-lid="39ptc" } we obtain a free module $F$ and a surjection $F \rightarrow M$, and from [\[Multilinear Algebra\] §Projective, Injective, and Flat Modules, ⁋Proposition 4](/en/math/multilinear_algebra/various_modules#prop4){: data-lid="vumg5" }, $F$ is projective.
:::

However, since we know nothing about $\lMod{A}^\op$, it does not follow from the above result that $\lMod{A}$ has enough injectives. Therefore, the following proposition requires a separate proof.

::: Proposition 5
The category $\lMod{A}$ has enough injectives.
:::
::: Proof
One can easily show that a functor with an exact left adjoint preserves injective objects. Then, from the ring homomorphism $\mathbb{Z}\rightarrow A$, the resulting coextension of scalars $\Ab \rightarrow \lMod{A}$ is a right adjoint of restriction of scalars, which is an exact functor, so an injective object of $\Ab$ becomes an injective object when sent to $\lMod{A}$. ([\[Algebraic Structures\] §Change of Scalars, ⁋Proposition 7](/en/math/algebraic_structures/change_of_base_ring#prop7){: data-lid="r62ex" }) Also, if we view any $A$-module $M$ as an abelian group and choose an injection $j:M\rightarrow I$ into an injective object $I$ of $\Ab$, the $A$-module homomorphism $M\rightarrow\Hom_\mathbb{Z}(A,I)$ obtained by adjunction is given by $m\mapsto(a\mapsto j(am))$, and evaluating this at $a=1$ yields $j$, so this is also an injection. Therefore, for the desired proof, it suffices to prove that $\Ab$ has enough injectives. This is done by defining, for any $G\in\Ab$,

$$I(G)=\prod_{f\in\Hom_\Ab(G, \mathbb{Q}/\mathbb{Z})} \mathbb{Q}/\mathbb{Z}$$

and $e_G:G \rightarrow I(G)$ by $g\mapsto (f(g))_{f\in\Hom(G, \mathbb{Q}/\mathbb{Z})}$.
:::

## Uniqueness of Resolutions

Meanwhile, the uniqueness of projective resolutions and injective resolutions is obtained from the following stronger theorem.

::: Theorem 6
Let a projective resolution $P_\bullet \rightarrow M$ and any $u:M \rightarrow N$ be given. Then for any left resolution $Q_\bullet \rightarrow N$, there exists a chain map $f:P_\bullet \rightarrow Q_\bullet$ making the following diagram

{% diagram Math/Homological_Algebra/Resolutions-7.svg width="20.02em" alt="comparison_proj" %}

commute, uniquely up to homotopy.  
Similarly, let an injective resolution $N \rightarrow I^\bullet$ and any $u: M \rightarrow N$ be given. Then for any right resolution $M \rightarrow J^\bullet$, there exists a chain map $f:J^\bullet \rightarrow I^\bullet$ making the following diagram

{% diagram Math/Homological_Algebra/Resolutions-8.svg width="19.71em" alt="comparison_inj" %}

commute, uniquely up to homotopy.
:::
::: Proof
First we prove the first claim. Write the augmentations of the two resolutions as $\varepsilon:P_0 \rightarrow M$ and $\varepsilon':Q_0 \rightarrow N$, respectively.

**(Existence of a chain map)** We construct the $f_n$ inductively. Since $\varepsilon'$ is surjective and $P_0$ is projective, for $u\circ\varepsilon:P_0 \rightarrow N$ we have $\varepsilon'\circ f_0=u\circ \varepsilon$ for some $f_0:P_0 \rightarrow Q_0$. Now suppose $f_0,\ldots,f_{n-1}$ have been constructed to make the given diagram commute, and consider the composition $\varphi=f_{n-1}\circ d_n^P:P_n \rightarrow Q_{n-1}$. Then for $n\geq 2$,

$$d_{n-1}^Q\circ\varphi=d_{n-1}^Q\circ f_{n-1}\circ d_n^P=f_{n-2}\circ d_{n-1}^P\circ d_n^P=0$$

and for $n=1$ we also have $\varepsilon'\circ f_0\circ d_1^P=u\circ\varepsilon\circ d_1^P=0$. Therefore $\im\varphi$ is contained in $\ker d_{n-1}^Q$ (or $\ker\varepsilon'$ when $n=1$), which equals $\im d_n^Q$ since $Q_\bullet \rightarrow N$ is a resolution. Then since $P_n$ is projective and $d_n^Q:Q_n \rightarrow \im d_n^Q$ is surjective, we have $d_n^Q\circ f_n=\varphi$ for some $f_n:P_n \rightarrow Q_n$.

**(Uniqueness up to homotopy)** Suppose $f,f'$ are both chain maps making the given diagram commute, and let $g=f-f'$. Then $g$ is a chain map satisfying $\varepsilon'\circ g_0=u\circ\varepsilon-u\circ\varepsilon=0$. For $g_n=d_{n+1}^Q\circ s_n+s_{n-1}\circ d_n^P$ to hold for all $n$, we construct a homotopy $s_n:P_n \rightarrow Q_{n+1}$ inductively. Here $s_{-1}=0$.

First, from $\varepsilon'\circ g_0=0$ we have $\im g_0\subseteq \ker\varepsilon'=\im d_1^Q$, so by the projectivity of $P_0$, we have $d_1^Q\circ s_0=g_0$ for some $s_0:P_0 \rightarrow Q_1$. Now suppose $s_0,\ldots,s_{n-1}$ have been constructed and let $\psi=g_n-s_{n-1}\circ d_n^P$. Then

$$d_n^Q\circ\psi=d_n^Q\circ g_n-(d_n^Q\circ s_{n-1})\circ d_n^P=g_{n-1}\circ d_n^P-(g_{n-1}-s_{n-2}\circ d_{n-1}^P)\circ d_n^P=s_{n-2}\circ d_{n-1}^P\circ d_n^P=0$$

so $\im\psi\subseteq\ker d_n^Q=\im d_{n+1}^Q$, and again by the projectivity of $P_n$, we have $d_{n+1}^Q\circ s_n=\psi$ for some $s_n:P_n \rightarrow Q_{n+1}$. Then by definition $g_n=d_{n+1}^Q\circ s_n+s_{n-1}\circ d_n^P$.

Now we prove the second claim. This is obtained by dualizing the proof of the first claim verbatim. Let the augmentations of the two resolutions be $\eta:M \rightarrow J^0$ and $\eta':N \rightarrow I^0$. Since $\eta$ is injective and $I^0$ is an injective object, for $\eta'\circ u:M \rightarrow I^0$ we have $f^0\circ\eta=\eta'\circ u$ for some $f^0:J^0 \rightarrow I^0$. Suppose $f^0,\ldots,f^{n-1}$ have been constructed inductively, and consider the composition $d_I^{n-1}\circ f^{n-1}:J^{n-1} \rightarrow I^n$. By the same computation as above, on $\im d_J^{n-2}=\ker d_J^{n-1}$ this map is $0$, and therefore, via the injective morphism $J^{n-1}/\ker d_J^{n-1}\hookrightarrow J^n$, it induces a morphism to $I^n$. Since $I^n$ is an injective object, we extend this to all of $J^n$ to obtain $f^n:J^n \rightarrow I^n$, and by this construction $f^n\circ d_J^{n-1}=d_I^{n-1}\circ f^{n-1}$ holds.
:::

Finally, we conclude by proving the following lemma, which will play an important role in the next post.

::: Lemma 7
Suppose we are given the following short exact sequence

$$0 \rightarrow A'\overset{i}{\rightarrow}A\overset{p}{\rightarrow}A'' \rightarrow 0$$

and projective resolutions $P_\bullet'$, $P_\bullet''$ of $A'$, $A''$. Then the chain complex $P_\bullet$ defined by $P_n=P_n'\oplus P_n''$ is a projective resolution of $A$, and there exists an exact sequence

$$0 \rightarrow P' \rightarrow P \rightarrow P'' \rightarrow 0$$

between these complexes.
:::
::: Proof
First, drawing the given situation in a diagram, we obtain the following.

{% diagram Math/Homological_Algebra/Resolutions-9.svg width="20.34em" alt="horseshoe-initial" %}

Now from the condition that $P_0''$ is projective, we can define $P_0'' \rightarrow A$. On the other hand, $P_0' \rightarrow A$ is already given as the composition of $i$ and $\epsilon'$, so taking their direct sum we obtain $\epsilon:P_0 \rightarrow A$. Now from [§Diagram chasing, ⁋Theorem 6](/en/math/homological_algebra/diagram_chasing#thm6){: data-lid="4wu4j" } we obtain the following diagram

{% diagram Math/Homological_Algebra/Resolutions-10.svg width="20.84em" alt="horseshoe-induction" %}

and in particular the following diagram

{% diagram frozen/635a8f80/Math/Homological_Algebra/Resolutions-11.svg width="21.61em" alt="horseshoe-finish" %}

Repeating this process, we obtain $P_\bullet$.
:::

---

**References**

**[Wei]** C.A. Weibel. *An Introduction to Homological Algebra*. Cambridge Studies in Advanced Mathematics. Cambridge University Press, 1995.
