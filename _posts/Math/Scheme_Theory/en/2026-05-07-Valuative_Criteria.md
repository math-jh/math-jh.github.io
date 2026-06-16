---
title: "Valuation Rings"
description: "We define separated and proper morphisms, and examine how they generalize the topological notions of Hausdorff and compact conditions in algebraic geometry. The structure of discrete valuation rings is also discussed."
excerpt: "Valuative criteria for separatedness and properness"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/valuative_criteria
sidebar: 
    nav: "scheme_theory-en"

date: 2024-05-24
weight: 9
translated_at: 2026-06-02T09:00:01+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-02T09:00:01+00:00
---
In this post we define separated morphisms and proper morphisms. It is helpful to think of them as the algebraic-geometry analogues of the Hausdorff and compactness conditions in topology.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Let an arbitrary scheme $$X$$ be given.

1. For an open subset $$U$$ of $$X$$, we call the scheme $$(U, \mathcal{O}\_X\vert\_U)$$ an *open subscheme* of $$X$$. If $$f:X \rightarrow Y$$ induces an isomorphism between open subschemes of $$X$$ and $$Y$$, we call $$f$$ an *open immersion*.
2. A scheme morphism $$f:Y \rightarrow X$$ is called a *closed immersion* if $$\lvert Y\rvert$$ defines a homeomorphism onto a closed subset of $$\lvert X\rvert$$ via $$f$$, and $$f^\sharp: \mathcal{O}_X \rightarrow f_\ast \mathcal{O}_Y$$ is surjective.  
If for two closed immersions $$f:Y \rightarrow X$$ and $$f': Y' \rightarrow X$$, there exists an isomorphism $$i:Y' \rightarrow Y$$ such that $$f'=f\circ i$$, then we regard $$f$$ and $$f'$$ as equivalent closed immersions, and define the equivalence class as a *closed subscheme*. When such a closed subscheme is given, we call the kernel $$\mathcal{I}_Y$$ of $$f^\sharp$$ the *ideal sheaf*.
3. $$f:X \rightarrow Y$$ is called *projective* if for a suitable $$n$$, $$f$$ can be decomposed as a composition of a closed immersion and a projection in the form $$X\hookrightarrow \mathbb{P}^n_Y \rightarrow Y$$.
4. $$f:X \rightarrow Y$$ is called *quasi-projective* if it can be decomposed as a composition of a suitable open immersion $$X \rightarrow X'$$ and a projective morphism $$X' \rightarrow Y$$.

</div>

## Discrete Valuation Rings

Before starting the main story, it is good to look at the following example.

<div class="example" markdown="1">

<ins id="ex2">**Example 2**</ins> Let a ring $$A$$ be a discrete valuation ring. That is, $$A$$ is a principal ideal domain with exactly two prime ideals $$(0)$$ and $$\mathfrak{m}$$, of which $$\mathfrak{m}$$ is the unique maximal ideal consisting of the non-units.

From this, $$\Spec A$$ consists of the two points $$(0)$$ and $$\mathfrak{m}$$, and since

$$Z((0))=\{(0),\mathfrak{m}\},\quad Z(\mathfrak{m})=\{\mathfrak{m}\}$$

the only nontrivial open subset of $$\Spec A$$ is

$$D(\mathfrak{m})=\{(0)\}.$$

On the other hand, if $$\mathfrak{m}=(\pi)$$, then by [§Spectra, ⁋Proposition 5](/en/math/scheme_theory/spectrums#prop5),

$$\mathcal{O}(D(\mathfrak{m}))=\mathcal{O}(D(\pi))\cong A_\pi\cong \Frac(A).$$

Of course $$\mathcal{O}(\Spec A)\cong A$$.

Meanwhile, the two points of $$\Spec A$$ can be viewed geometrically as follows: each point is determined by a ring homomorphism from $$A$$ to its residue field, namely $$\kappa((0))$$ and $$\kappa(\mathfrak{m})$$. Using [§Spectra, ⁋Proposition 5](/en/math/scheme_theory/spectrums#prop5) again,

$$\mathcal{O}_{(0)}\cong A_{(0)}\cong \Frac(A),\qquad \mathcal{O}_\mathfrak{m}\cong A_\mathfrak{m}$$

from which we obtain

$$\kappa((0))=\Frac(A), \qquad \kappa(\mathfrak{m})=A_\mathfrak{m}/\mathfrak{m}A_\mathfrak{m}\cong \Frac(A/\mathfrak{m})\cong A/\mathfrak{m}.$$

</div>

## Separated Morphisms

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> For a scheme morphism $$f:X \rightarrow Y$$, we define the *diagonal morphism* as $$\Delta: X \rightarrow X \times_Y X$$.

![diagonal_morphism](/assets/images/Math/Scheme_Theory/Valuative_Criteria-1.svg){:style="width:13.51em" class="invert" .align-center}

If $$\Delta$$ is a closed immersion, we call $$f$$ *separated*, and say $$X$$ is *separated* over $$Y$$. If $$X$$ is separated over $$\Spec \mathbb{Z}$$, we simply call $$X$$ a *separated* scheme.

</div>

In algebraic geometry, separatedness is regarded as the property replacing Hausdorffness, and this is because of the following proposition.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> For $$f:X \rightarrow Y$$, $$f$$ being separated is equivalent to the image of $$X$$ under the diagonal morphism $$\Delta: X \rightarrow X\times_YX$$ being a closed set.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

By definition, if $$f$$ is separated then it is obvious that $$\Delta(X)$$ is closed. Thus we assume $$\Delta(X)$$ is closed and show that $$\Delta$$ is a closed immersion. It is obvious that $$\Delta(X)$$ becomes a closed subset of $$X\times_YX$$, so it suffices to show that $$\mathcal{O}_{X\times_YX} \rightarrow \Delta_\ast \mathcal{O}_X$$ is surjective. On the other hand, surjectivity of a sheaf morphism can be checked on stalks. Choose an arbitrary $$p\in X$$. Then we can first choose an open affine subset $$U$$ of $$p$$, and if necessary restrict $$U$$ so that $$f(U)$$ lies in some open affine subset $$V$$ of $$Y$$. Then $$U\times_VU$$ is an open neighborhood of $$\Delta(p)$$, and on this $$\Delta: U \rightarrow U\times_VU$$ is a closed immersion by the following [Lemma 5](#lem5), and the proof is complete.

</details>

<div class="proposition" markdown="1">

<ins id="lem5">**Lemma 5**</ins> An arbitrary morphism $$f:X \rightarrow Y$$ between affine schemes is always separated.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

If $$X=\Spec A, Y=\Spec B$$, then $$\Delta$$ is induced from the ring homomorphism

$$A\otimes_BA \rightarrow A;\quad a\otimes a'\mapsto aa'$$

and this is surjective, so it is obvious.

</details>

An example of a non-separated scheme is the line with double origin constructed in [§Schemes, ⁋Example 10](/en/math/scheme_theory/schemes#ex10). For convenience, let us call this scheme $$X$$. Then $$X\times X$$ will look like the ordinary coordinate plane away from the axes, but on the coordinate axes, especially at the origin, four origins will appear. Intuitively, if we think about how $$\Delta$$ sits inside $$X\times X$$, away from the coordinate axes it will take the shape of an ordinary diagonal line, but when the two origins of $$X$$ are mapped into $$X\times X$$ via $$\Delta$$, it is unclear which two of these four origins they land in. In fact, all four of these origins lie in the closure of $$\Delta(X)$$, so we see that it is not separated. Again, in topology this space was an example of a non-Hausdorff space.

<div class="proposition" markdown="1">

<ins id="thm6">**Theorem 6**</ins> For a Noetherian scheme $$X$$ and a scheme morphism $$f:X \rightarrow Y$$, $$f$$ being separated is equivalent to the following: for any valuation ring $$A$$ and its quotient field $$K=\Frac(A)$$, for any scheme morphisms $$\Spec A \rightarrow Y$$, $$\Spec K \rightarrow X$$ and the following commutative diagram

![valuative_criterion_for_separatedness](/assets/images/Math/Scheme_Theory/Valuative_Criteria-2.svg){:style="width:8.27em" class="invert" .align-center}

whenever the outer square is given, there is at most one $$\Spec A \rightarrow X$$ making the whole diagram commute.

</div>

We do not prove this proposition separately, but it is known that if $$Y$$ is Noetherian and $$f$$ is a finite type morphism, then in the above theorem one may replace arbitrary valuation rings by arbitrary discrete valuation rings. Once this is done, it becomes easier to explain the theorem using geometric intuition: think of $$\Spec A$$ as representing the germ of a smooth curve and $$\Spec K$$ as that curve with one point removed; then the theorem says that there is only one way to embed such a $$\Spec K\hookrightarrow \Spec A$$.

From this we obtain the following.

<div class="proposition" markdown="1">

<ins id="cor7">**Corollary 7**</ins> For Noetherian schemes,

1. Open immersions and closed immersions are both separated.
2. The composition of two separated morphisms is separated.
3. Separated morphisms are preserved under base change.
4. Separated morphisms are preserved under fiber products.
5. If $$f:X \rightarrow Y$$, $$g:Y \rightarrow Z$$ are scheme morphisms and $$g\circ f$$ is a separated morphism, then $$f$$ is also a separated morphism.

</div>

## Proper Morphisms

<div class="definition" markdown="1">

<ins id="def8">**Definition 8**</ins> $$f:X \rightarrow Y$$ is called *universally closed* if $$f$$ is a closed map and for any $$Y' \rightarrow Y$$, the morphism $$X\times_Y Y' \rightarrow Y'$$ is also closed. A finite type morphism that is separated and universally closed is called a *proper morphism*.

</div>

Just as for [Theorem 6](#thm6), there is also a valuative criterion for proper morphisms.

<div class="proposition" markdown="1">

<ins id="thm9">**Theorem 9**</ins> For a Noetherian scheme $$X$$ and a scheme morphism $$f:X \rightarrow Y$$, $$f$$ being proper is equivalent to the following: for any valuation ring $$A$$ and its quotient field $$K=\Frac(A)$$, for any scheme morphisms $$\Spec A \rightarrow Y$$, $$\Spec K \rightarrow X$$ and the following commutative diagram

![valuative_criterion_for_separatedness](/assets/images/Math/Scheme_Theory/Valuative_Criteria-2.svg){:style="width:8.27em" class="invert" .align-center}

whenever the outer square is given, there exists exactly one $$\Spec A \rightarrow X$$ making the whole diagram commute.

</div>

Likewise, the following corollary holds.

<div class="proposition" markdown="1">

<ins id="cor10">**Corollary 10**</ins> For Noetherian schemes,

1. A closed immersion is proper.
2. The composition of proper morphisms is proper.
3. Proper morphisms are preserved under base change.
4. Proper morphisms are preserved under fiber products.
5. If $$f:X \rightarrow Y$$, $$g:Y \rightarrow Z$$ are scheme morphisms and $$g\circ f$$ is a proper morphism, then $$f$$ is also a proper morphism.

</div>

<div class="proposition" markdown="1">

<ins id="thm11">**Theorem 11**</ins> A projective morphism between Noetherian schemes is a proper morphism, and a quasi-projective morphism is a separated, finite type morphism.

</div>
