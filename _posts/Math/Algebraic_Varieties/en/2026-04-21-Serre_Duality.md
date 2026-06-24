---
title: "Serre Duality"
description: "We explore the natural duality between line bundles and cohomology on projective space, and examine the construction of the cup product and Serre duality."
excerpt: "Serre duality theorem and its applications"

categories: [Math / Algebraic Varieties]
permalink: /en/math/algebraic_varieties/serre_duality
sidebar: 
    nav: "algebraic_varieties-en"

date: 2026-04-21
weight: 14
translated_at: 2026-06-24T07:00:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-24T07:00:02+00:00
---
In geometrically favorable situations, there is a natural duality between cohomology in dimension $$k$$ and cohomology in codimension $$k$$. To prove this, we used the perfect pairing

$$H^k(M;R)\times H^{n-k}(M;R)\rightarrow R$$

and obtained results such as [\[Algebraic Topology\] §Poincaré Duality, ⁋Theorem 11](/en/math/algebraic_topology/Poincare_duality#thm11). More specifically, since this pairing is constructed via the cap product and the fundamental class $$[M] \in H_n(M;R)$$, the source of duality in topology can be identified with the orientation class $$[M]$$.

In this post, we examine Serre duality, the algebraic-geometry analogue of this phenomenon.

## Serre Duality on Projective Space

We first examine the case $$X=\mathbb{P}^n$$ in detail. We know that every line bundle on $$\mathbb{P}^n$$ is of the form $$\mathcal{O}(d)$$, and in particular we saw in [§Canonical Bundle, ⁋Proposition 7](/en/math/algebraic_varieties/canonical_bundle#prop7) that the canonical bundle is $$\mathcal{O}(-n-1)$$. Then from [§Cohomology of Projective Space, ⁋Proposition 1 (Bott)](/en/math/algebraic_varieties/cohomology_of_projective_spaces#prop1) we obtain the following.

<div class="proposition" markdown="1">

<ins id="prop1">**Proposition 1**</ins> For the canonical line bundle $$\omega_X$$ on projective space $$X=\mathbb{P}^n$$, there is an isomorphism

$$H^n(X, \omega_X)\cong \mathbb{K}$$

</div>

In general, this is understood as the isomorphism that explicitly takes $$\x_0^{-1}\cdots\x_n^{-1}$$ as its basis, but it is only uniquely determined up to scalar multiplication. Choosing such a normalization is tantamount to choosing a *trace map* $$\tr:H^n(\mathbb{P}^n, \omega_{\mathbb{P}^n}) \to \mathbb{K}$$.

To obtain the duality pairing, we must define the cup product. For convenience, we work at the level of Čech cohomology. For any topological space $$X$$, an open cover $$\mathcal{U}$$ of $$X$$, and sheaves $$\mathcal{F}$$, $$\mathcal{G}$$ on $$X$$, the cup product of two Čech cochains $$\alpha \in \check{C}^i(\mathcal{U}, \mathcal{F})$$ and $$\beta \in \check{C}^j(\mathcal{U}, \mathcal{G})$$ is given by the formula

$$(\alpha \smile \beta)_{i_0, \ldots, i_{i+j}} = \alpha_{i_0,\ldots,i_i}\big\vert_{U_{i_0,\ldots,i_{i+j}}} \otimes \beta_{i_i,\ldots,i_{i+j}}\big\vert_{U_{i_0,\ldots,i_{i+j}}}\in \check{C}^{i+j}(\mathcal{U}, \mathcal{F}\otimes\mathcal{G})$$

We can verify explicitly that this descends to cohomology, yielding the map

$$\smile:\check{H}^i(\mathcal{U}, \mathcal{F}) \times \check{H}^j(\mathcal{U}, \mathcal{G}) \to \check{H}^{i+j}(\mathcal{U}, \mathcal{F} \otimes \mathcal{G})$$

At the sheaf cohomology level, one can also define this by taking injective resolutions $$\mathcal{I}^\bullet$$ and $$\mathcal{J}^\bullet$$ of $$\mathcal{F}$$ and $$\mathcal{G}$$ respectively, and using the fact that their tensor product complex (that is, the total complex of the double complex whose components are $$\mathcal{I}^p\otimes \mathcal{J}^q$$) defines a resolution of $$\mathcal{F}\otimes\mathcal{G}$$.

In any case, by the cup product pairing we obtain the following bilinear map for any locally free sheaf $$\mathcal{E}$$:

$$H^k(\mathbb{P}^n, \mathcal{E})\times H^{n-k}(\mathbb{P}^n, \omega_{\mathbb{P}^n}\otimes \mathcal{E}^\vee)\rightarrow H^n(\mathbb{P}^n, \mathcal{E}\otimes \omega_{\mathbb{P}^n}\otimes \mathcal{E}^\vee)$$

then, using the isomorphism $$\mathcal{E}\otimes \mathcal{E}^\vee\rightarrow \mathcal{O}_{\mathbb{P}^n}$$ and the trace map above, we obtain a bilinear form

$$H^k(\mathbb{P}^n, \mathcal{E})\times H^{n-k}(\mathbb{P}^n, \omega_{\mathbb{P}^n}\otimes\mathcal{E}^\vee)\rightarrow \mathbb{K}$$

For the case of $$\mathcal{O}(d)$$, we establish non-degeneracy by direct computation in [§Cohomology of Projective Space, ⁋Proposition 1 (Bott)](/en/math/algebraic_varieties/cohomology_of_projective_spaces#prop1), and then use the syzygy theorem to extend this non-degeneracy to a general locally free sheaf $$\mathcal{E}$$.

From the discussion so far, we obtain the following.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2 (Serre duality pairing, projective case)**</ins> For a locally free sheaf $$\mathcal{E}$$ on $$\mathbb{P}^n$$, the bilinear form

$$H^k(\mathbb{P}^n, \mathcal{E}) \times H^{n-k}(\mathbb{P}^n, \omega_{\mathbb{P}^n} \otimes \mathcal{E}^\vee) \to \mathbb{K};\quad (\alpha, \beta) \mapsto \tr(\alpha \smile \beta)$$

is a perfect pairing.

</div>

More explicitly, Serre duality generally refers to the following isomorphism obtained from this:

$$H^k(\mathbb{P}^n, \mathcal{E})\cong H^{n-k}(\mathbb{P}^n, \omega_{\mathbb{P}^n}\otimes\mathcal{E}^\vee)^\ast$$

More generally, by the Noether normalization theorem, for any $$n$$-dimensional smooth projective variety $$X$$ there exists a finite surjective morphism $$f: X \to \mathbb{P}^n$$. Then we can pull back Serre duality proved on $$\mathbb{P}^n$$ to $$X$$ via this finite morphism $$f$$, and in this setting Serre duality means the following isomorphism:

$$H^i(X, \mathcal{E}) \cong H^{n-i}(X, \omega_X \otimes \mathcal{E}^\vee)^\ast$$

<div class="example" markdown="1">

<ins id="ex3">**Example 3**</ins> Let us examine [Proposition 2](#prop2) concretely in $$\mathbb{P}^2$$. Here $$\omega_{\mathbb{P}^2} \cong \mathcal{O}(-3)$$, so what Serre duality asserts is the isomorphism $$H^k(\mathbb{P}^2, \mathcal{O}(d)) \cong H^{2-k}(\mathbb{P}^2, \mathcal{O}(-d-3))^\ast$$.

First, for $$d=0$$, by [§Cohomology of Projective Spaces, ⁋Proposition 1](/en/math/algebraic_varieties/cohomology_of_projective_spaces#prop1) we have

$$H^0(\mathbb{P}^2, \mathcal{O}) = \mathbb{K},\qquad H^1(\mathbb{P}^2, \mathcal{O}) = 0, \qquad H^2(\mathbb{P}^2, \mathcal{O}) = 0$$

and the cohomology of $$\mathcal{O}(-3)$$ is

$$H^0(\mathbb{P}^2, \mathcal{O}(-3)) = 0, \qquad H^1(\mathbb{P}^2, \mathcal{O}(-3)) = 0,\qquad H^2(\mathbb{P}^2, \mathcal{O}(-3)) = \mathbb{K}$$

so we see that Serre duality holds. Similarly, for $$d=1$$, the only nonzero cohomology is

$$H^0(\mathbb{P}^2, \mathcal{O}(1)) = \mathbb{K}^3$$

and by Serre duality we must have $$H^0(\mathcal{O}(1)) \cong H^2(\mathcal{O}(-4))^\ast$$, so $$\dim H^2(\mathcal{O}(-4))$$ should be $$3$$. Applying [§Cohomology of Projective Spaces, ⁋Proposition 1](/en/math/algebraic_varieties/cohomology_of_projective_spaces#prop1) again, the $$H^2$$ of $$\mathcal{O}(-4)$$ actually has dimension

$$\binom{2+(-4)}{2}=\binom{-2}{2} = 3$$

so we can verify that they agree.

</div>

## Generalization of Serre Duality

We generalize the discussion so far. The first thing we can do is to extend from a locally free sheaf $$\mathcal{E}$$ to an arbitrary coherent sheaf $$\mathcal{E}$$. This is not as difficult as one might think, because on a smooth variety any coherent sheaf has a finite locally free resolution, so we may apply the statement of Serre duality inductively. ([§Canonical Bundle](/en/math/algebraic_varieties/canonical_bundle))

Next we drop the smoothness condition on $$X$$. In this case there are two major problems. The first visible problem is that $$X$$ does not have a canonical line bundle. The other problem is slightly more subtle: when we obtained an explicit isomorphism from the perfect pairing, we somewhat implicitly used the isomorphism

$$\mathcal{H}om(\mathcal{E}, \mathcal{F})\cong \mathcal{E}^\vee\otimes \mathcal{F}$$

but this is only possible because $$\mathcal{E}$$ is locally free; if $$\mathcal{E}$$ is a coherent sheaf and $$X$$ is singular, there is no guarantee that $$\mathcal{E}$$ has a finite locally free resolution, so this isomorphism fails. Therefore we introduce derived functors again, and call a sheaf $$\omega_X$$ satisfying

$$\Ext^i_X(\mathcal{F},\omega_X)\cong H^{n-i}(X,\mathcal{F})^\vee$$

the *dualizing sheaf* of $$X$$. In general, its existence is guaranteed for a Cohen-Macaulay variety of pure dimension $$n$$; we will not give the definition, but intuitively the Cohen-Macaulay condition is a notion that includes singular varieties which do not cause dimension-theoretic problems.

A somewhat less intuitive generalization is relative Serre duality. In fact, we have not paid much attention to the underlying field $$\mathbb{K}$$ of the variety, but in this context it helps to make its role explicit.

That an affine variety $$X$$ is defined over $$\mathbb{K}$$ means that its coordinate ring $$A$$ is a $$\mathbb{K}$$-algebra, so there exists a ring homomorphism $$\mathbb{K}\rightarrow A$$ encoding this structure. Viewing these as the coordinate rings of $$\mathbb{A}^1_\mathbb{K}$$ and $$X$$ respectively, this structure morphism is geometrically given as $$X\rightarrow \mathbb{A}^1_\mathbb{K}$$.

Relative Serre duality generalizes this setup by replacing the target $$\mathbb{A}^1_\mathbb{K}$$ with another variety. First, for arbitrary varieties $$X,Y$$, let us define that a morphism $$f:X\rightarrow Y$$ is a *smooth projective morphism* if for each $$y\in Y$$ the fiber $$f^{-1}(y)$$ is a smooth projective variety. Then in this case, each $$f^{-1}(y)$$ is a smooth projective variety so it will have a canonical line bundle $$\omega_{X_y}$$, and these can be assembled consistently into a *relative dualizing sheaf* $$\omega_{X/Y}$$ defined on $$X$$. That is, $$\omega_{X/Y}$$ is a sheaf satisfying $$\omega_{X/Y}\vert_{X_y}\cong\omega_{X_y}$$ for each $$y$$. Then the generalization in this setting is as follows.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4 (Relative Serre duality)**</ins> Let $$f \colon X \to Y$$ be a smooth projective morphism and let $$n = \dim X - \dim Y$$. Then

$$R^n f_\ast \omega_{X/Y} \cong \mathcal{O}_Y$$

and for $$i \neq n$$ we have $$R^i f_\ast \omega_{X/Y} = 0$$.

</div>

## Grothendieck Duality

Let us review the process of generalizing Serre duality. We first proved Serre duality on $$\mathbb{P}^n$$ using the trace map and cup product ([Proposition 2](#prop2)), and extended this to an arbitrary smooth projective variety via a finite morphism. The extension to coherent sheaves was handled by induction using locally free resolutions, and the extension to singular varieties was handled by introducing the dualizing sheaf. Relative Serre duality ([Proposition 4](#prop4)) was the generalization that replaced the target from a point to an arbitrary variety.

The most modern interpretation of Serre duality is Grothendieck duality, which is formulated in the language of derived categories. ([\[Homological Algebra\] §Derived Categories, ⁋Definition 2](/en/math/homological_algebra/derived_categories#def2)) This generalization has a rather convincing motivation compared to its language: for example, we had to think about injective resolutions just to define sheaf cohomology, and we also had to think about locally free resolutions when generalizing Serre duality to arbitrary coherent sheaves above, so we know that the derived category is where everything actually happens. In particular, the key point is that the perfect pairing in Serre duality is actually equivalent to the information of choosing a specific isomorphism

$$H^n(X, \omega_X) \cong \mathbb{K}$$

and lifting this to the derived category reveals the observation that it is a special case of an adjunction between the derived pushforward $$R f_\ast$$ and its right adjoint. Specifically, the isomorphism of Serre duality

$$H^i(X, \mathcal{E}) \cong H^{n-i}(X, \omega_X \otimes \mathcal{E}^\vee)^\ast$$

is derived in the derived category from the following adjunction isomorphism:

$$\operatorname{Hom}_{D(X)}(\mathcal{F}, f^! \mathcal{G}) \cong \operatorname{Hom}_{D(Y)}(R f_\ast \mathcal{F}, \mathcal{G})$$

Here the *exceptional inverse image* $$f^!$$ is the functor defined as the right adjoint of $$R f_\ast$$ in the derived category, and to define it properly one must necessarily work in the derived category.

As mentioned earlier, Grothendieck duality is a result that encompasses relative Serre duality. To see this, consider the case of a smooth morphism $$f:X\rightarrow Y$$; then $$f^! \mathcal{O}_Y \cong \omega_{X/Y}[n]$$ holds, and from this we can see that $$\omega_{X/Y}$$ placed in the correct dimension is exactly $$f^!\mathcal{O}_Y$$.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5 (Grothendieck Duality)**</ins> For a proper morphism $$f \colon X \to Y$$ and a coherent sheaf $$\mathcal{F}$$ on $$X$$, the following isomorphism holds in the derived category:

$$R f_\ast R\mathcal{H}om_{\mathcal{O}_X}(\mathcal{F}, f^! \mathcal{G}) \cong R\mathcal{H}om_{\mathcal{O}_Y}(R f_\ast \mathcal{F}, \mathcal{G})$$

Here $$R\mathcal{H}om$$ is derived Hom ([\[Homological Algebra\] §Derived Categories, ⁋Proposition 10](/en/math/homological_algebra/derived_categories#prop10)), and $$\mathcal{G}$$ is a bounded complex of coherent sheaves on $$Y$$.

</div>

Intuitively, this theorem means that "Hom after pushforward" and "pushforward after Hom" are the same. That is, computing the Hom between $$\mathcal{F}$$ and $$f^! \mathcal{G}$$ on $$X$$ and then pushing down to $$Y$$ is the same as first pushing $$\mathcal{F}$$ down to $$Y$$ and then computing the Hom with $$\mathcal{G}$$.

---

**References**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Ser]** J.-P. Serre, *Faisceaux algébriques cohérents*, Annals of Mathematics, 1955.

---
