---
title: "Valuation Rings"
excerpt: "Valuative criteria for separatedness and properness"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/valuative_criteria
header:
    overlay_image: /assets/images/Math/Algebraic_Varieties/Valuative_criteria.png
    overlay_filter: 0.5
sidebar: 
    nav: "scheme_theory-en"

date: 2024-05-24
last_modified_at: 2024-05-24
weight: 9
translated_at: 2026-05-22T21:00:01+00:00
translation_source: kimi-cli
---
In this post we define separated morphisms and proper morphisms. It is helpful to think of them as the algebraic geometry analogues of the Hausdorff and compactness conditions in topology.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Let an arbitrary scheme $X$ be given.

1. For an open subset $U$ of $X$, we call the scheme $(U, \mathcal{O}\_X\vert\_U)$ an *open subscheme* of $X$. If $f:X \rightarrow Y$ induces an isomorphism between $X$ and an open subscheme of $Y$, we call $f$ an *open immersion*.
2. A scheme morphism $f:Y \rightarrow X$ is a *closed immersion* if $\lvert Y\rvert$ defines a homeomorphism onto a closed subset of $\lvert X\rvert$ via $f$, and $f^\sharp: \mathcal{O}\_X \rightarrow f\_\ast \mathcal{O}_Y$ is surjective.  
If for two closed immersions $f:Y \rightarrow X$ and $f': Y' \rightarrow X$, there exists an isomorphism $i:Y' \rightarrow Y$ such that $f'=f\circ i$, then we consider $f$ and $f'$ to be equivalent closed immersions, and in this case we define the equivalence class as a *closed subscheme*. When such a closed subscheme is given, we call the kernel $\mathcal{I}_Y$ of $f^\sharp$ the *ideal sheaf*. 
3. $f:X \rightarrow Y$ is *projective* if for a suitable $n$, $f$ can be decomposed in the form of a composition of a closed immersion and a projection $X\hookrightarrow \mathbb{P}^n_Y \rightarrow Y$. 
4. $f:X \rightarrow Y$ is *quasi-projective* if it can be decomposed as a composition of a suitable open immersion $X \rightarrow X'$ and a projective morphism $X' \rightarrow Y$. 

</div>

## Discrete Valuation Rings

Before beginning the main discussion, it is good to look at the following example.

<div class="example" markdown="1">

<ins id="ex2">**Example 2**</ins> Let $A$ be a discrete valuation ring. That is, $A$ is a principal ideal domain with two prime ideals $(0)$, $\mathfrak{m}$, of which $\mathfrak{m}$ is the unique maximal ideal of $A$ consisting of the non-units. 

From this, $\Spec A$ consists of the two points $(0)$, $\mathfrak{m}$, and since

$$Z((0))=\{(0),\mathfrak{m}\},\quad Z(\mathfrak{m})=\{\mathfrak{m}\}$$

the only nontrivial open subset of $\Spec A$ is

$$D(\mathfrak{m})=\{(0)\}$$

alone. Meanwhile, writing $\mathfrak{m}=(\pi)$, by [§Spectrum, ⁋Proposition 5](/en/math/scheme_theory/spectrums#prop5) we have

$$\mathscr{O}(D(\mathfrak{m}))=\mathscr{O}(D(\pi))\cong A_\pi\cong \Frac(A)$$

Of course $\mathscr{O}(\Spec A)\cong A$. 

Meanwhile, the two points of $\\Spec A$ can be examined geometrically as follows: each point is determined by a ring homomorphism from $A$ to its residue field, namely $\\kappa((0))$ and $\\kappa(\\mathfrak{m})$. Using [§Spectrum, ⁋Proposition 5](/en/math/scheme_theory/spectrums#prop5) again we obtain

$$\mathscr{O}_{(0)}\cong A_{(0)}\cong \Frac(A),\qquad \mathscr{O}_\mathfrak{m}\cong A_\mathfrak{m}$$

and from this

$$\kappa((0))=\Frac(A), \qquad \kappa(\mathfrak{m})=A_\mathfrak{m}/\mathfrak{m}A_\mathfrak{m}\cong \Frac(A/\mathfrak{m})\cong A/\mathfrak{m}$$

</div>

## Separated Morphisms

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> For a scheme morphism $f:X \rightarrow Y$, we define the *diagonal morphism* as $\Delta: X \rightarrow X \times_Y X$. 

![diagonal_morphism](/assets/images/Math/Algebraic_Varieties/Valuative_criteria-1.png){:style="width:12em" class="invert" .align-center}

If $\Delta$ is a closed immersion, we call $f$ *separated* and say that $X$ is *separated* over $Y$. If $X$ is separated over $\Spec \mathbb{Z}$, we simply call $X$ a *separated* scheme.

</div>

In algebraic geometry, separatedness is thought of as the property replacing Hausdorffness, because of the following proposition.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> For $f:X \rightarrow Y$ to be separated is equivalent to the image of $X$ under the diagonal morphism $\Delta: X \rightarrow X\times_YX$ being a closed subset.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

It is obvious from the definition that if $f$ is separated then $\Delta(X)$ is closed. Thus, assuming that $\Delta(X)$ is closed, we must show that $\Delta$ is a closed immersion. Since it is obvious that $\Delta(X)$ is a closed subset of $X\times_YX$, it suffices to show that $\mathcal{O}\_{X\times\_YX} \rightarrow \Delta_\ast \mathcal{O}_X$ is surjective. Meanwhile, the surjectivity of a sheaf morphism can be checked on stalks. Choose an arbitrary $p\in X$. Then we can first choose an open affine subset $U$ containing $p$, and if necessary restrict $U$ so that $f(U)$ is contained in some open affine subset $V$ of $Y$. Then $U\times_VU$ is an open neighborhood of $\Delta(p)$, and on this $\Delta: U \rightarrow U\times_VU$ is a closed immersion by [Lemma 4](#lem4) below, completing the proof.

</details>

<div class="proposition" markdown="1">

<ins id="lem5">**Lemma 5**</ins> Any morphism $f:X \rightarrow Y$ between affine schemes is always separated.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Writing $X=\Spec A, Y=\Spec B$, the diagonal morphism $\Delta$ is induced by the ring homomorphism 

$$A\otimes_BA \rightarrow A;\quad a\otimes a'\mapsto aa'$$

and this is obvious since it is surjective. 

</details>

An example of a non-separated scheme is the line with double origin constructed in [§Schemes, ⁋Example 6](/en/math/scheme_theory/schemes#ex6). For convenience, let us denote this scheme by $X$. Then outside the axes, $X\times X$ will be the same as the usual coordinate plane, but on the axes, especially at the origin, there will be four origins. Intuitively, if we consider how $\Delta$ sits inside $X\times X$, outside the coordinate axes it will have the shape of the usual diagonal, but when the two origins of $X$ are mapped into $X\times X$ via $\Delta$, it is impossible to know which two of these four origins they go into. In fact, since all four of these origins lie in the closure of $\Delta(X)$, we see that it is not separated. This space was also an example of a non-Hausdorff space in topology.

<div class="proposition" markdown="1">

<ins id="thm6">**Theorem 6**</ins> For a Noetherian scheme $X$ and a scheme morphism $f:X \rightarrow Y$, $f$ is separated if and only if for every valuation ring $A$ with quotient field $K=\Frac(A)$, and for any scheme morphisms $\Spec A \rightarrow Y$ and $\Spec K \rightarrow X$ forming the outer square of the following commutative diagram, there is at most one morphism $\Spec A \rightarrow X$ making the entire diagram commute.

![valuative_criterion_for_separatedness](/assets/images/Math/Algebraic_Varieties/Valuative_criteria-2.png){:style="width:8em" class="invert" .align-center}

</div>

We do not prove this proposition separately, but it is known that if $Y$ is Noetherian and $f$ is a finite type morphism, then in the above theorem one may replace arbitrary valuation rings with arbitrary discrete valuation rings. Once this change is made, it becomes easy to explain the theorem using geometric intuition: thinking of $\Spec A$ as representing the germ of a smooth curve and $\Spec K$ as that curve with one point missing, the above theorem tells us that there is at most one way to extend such a $\Spec K\hookrightarrow \Spec A$.

From this we obtain the following.

<div class="proposition" markdown="1">

<ins id="cor7">**Corollary 7**</ins> For Noetherian schemes,

1. Open immersions and closed immersions are separated.
2. The composition of two separated morphisms is separated.
3. Separated morphisms are preserved under base change.
4. Separated morphisms are preserved under fiber products.
5. If $f:X \rightarrow Y$ and $g:Y \rightarrow Z$ are scheme morphisms and $g\circ f$ is a separated morphism, then $f$ is also a separated morphism.

</div>

## Proper Morphisms

<div class="definition" markdown="1">

<ins id="def8">**Definition 8**</ins> $f:X \rightarrow Y$ is said to be *universally closed* if $f$ is a closed map and for any $Y' \rightarrow Y$, the morphism $X\times_Y Y' \rightarrow Y'$ is also closed. A finite type morphism that is separated and universally closed is called a *proper morphism*. 

</div>

Just as in [Theorem 9](#thm9), there is also a valuative criterion for proper morphisms.

<div class="proposition" markdown="1">

<ins id="thm9">**Theorem 9**</ins> For a Noetherian scheme $X$ and a scheme morphism $f:X \rightarrow Y$, $f$ is proper if and only if for every valuation ring $A$ with quotient field $K=\Frac(A)$, and for any scheme morphisms $\Spec A \rightarrow Y$ and $\Spec K \rightarrow X$ forming the outer square of the following commutative diagram, there exists exactly one morphism $\Spec A \rightarrow X$ making the entire diagram commute.

![valuative_criterion_for_separatedness](/assets/images/Math/Algebraic_Varieties/Valuative_criteria-2.png){:style="width:8em" class="invert" .align-center}

</div>

Likewise, the following corollary holds.

<div class="proposition" markdown="1">

<ins id="cor9">**Corollary 9**</ins> For Noetherian schemes,

1. A closed immersion is proper.
2. The composition of proper morphisms is proper.
3. Proper morphisms are preserved under base change.
4. Proper morphisms are preserved under fiber products.
5. If $f:X \rightarrow Y$ and $g:Y \rightarrow Z$ are scheme morphisms and $g\circ f$ is a proper morphism, then $f$ is also a proper morphism.

</div>

<div class="proposition" markdown="1">

<ins id="thm10">**Theorem 10**</ins> A projective morphism between Noetherian schemes is a proper morphism, and a quasi-projective morphism is separated and of finite type. 

</div>
