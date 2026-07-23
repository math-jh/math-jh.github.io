---
title: "Serre Duality"
description: "We explore the natural duality between line bundles and cohomology on projective spaces, and examine the construction of cup products and Serre duality."
excerpt: "Serre duality theorem and its applications"

categories: [Math / Algebraic Varieties]
permalink: /en/math/algebraic_varieties/serre_duality
sidebar: 
    nav: "algebraic_varieties-en"

date: 2026-04-21
weight: 14
translated_at: 2026-07-11T08:00:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-07-11T08:00:02+00:00
---
Geometrically, in favorable situations there is a natural duality between dimension $k$ cohomology and codimension $k$ cohomology. To prove this we used the perfect pairing

$$H^k(M;R)\times H^{n-k}(M;R)\rightarrow R$$

and obtained results such as [[Algebraic Topology] §Poincaré Duality, ⁋Theorem 11](/en/math/algebraic_topology/Poincare_duality#thm11). More concretely, since this pairing is constructed via the cap product and the fundamental class $[M] \in H_n(M;R)$, we can say that the source of duality in topology is the orientation class $[M]$.

In this post we examine Serre duality, the algebraic-geometry version of duality.

## Serre Duality on Projective Space

We first look carefully at the case $X=\mathbb{P}^n$. We know that every line bundle on $\mathbb{P}^n$ is of the form $\mathcal{O}(d)$, and in particular we saw in [§Canonical Bundle, ⁋Proposition 7](/en/math/algebraic_varieties/canonical_bundle#prop7) that this is $\mathcal{O}(-n-1)$. Then from [§Cohomology of Projective Spaces, ⁋Proposition 1](/en/math/algebraic_varieties/cohomology_of_projective_spaces#prop1) we obtain the following.

::: Proposition 1
For the canonical line bundle $\omega_X$ on projective space $X=\mathbb{P}^n$, there exists an isomorphism

$$H^n(X, \omega_X)\cong \mathbb{K}$$
:::

In general this is understood as the isomorphism explicitly taking $\x_0^{-1}\cdots\x_n^{-1}$ as a basis, but it is determined only up to scalar multiplication. Choosing such a normalization is the same as concretely choosing a *trace map* $\tr:H^n(\mathbb{P}^n, \omega_{\mathbb{P}^n}) \rightarrow \mathbb{K}$.

To obtain the duality pairing we now need to define the cup product. For convenience let us work at the level of Čech cohomology. For any topological space $X$, an open cover $\mathcal{U}$ of $X$, and sheaves $\mathcal{F}$, $\mathcal{G}$ defined on $X$, we define the cup product of two Čech cochains $\alpha \in \check{C}^i(\mathcal{U}, \mathcal{F})$, $\beta \in \check{C}^j(\mathcal{U}, \mathcal{G})$ by the formula

$$(\alpha \smile \beta)_{i_0, \ldots, i_{i+j}} = \alpha_{i_0,\ldots,i_i}\big\vert_{U_{i_0,\ldots,i_{i+j}}} \otimes \beta_{i_i,\ldots,i_{i+j}}\big\vert_{U_{i_0,\ldots,i_{i+j}}}\in \check{C}^{i+j}(\mathcal{U}, \mathcal{F}\otimes\mathcal{G})$$

We can explicitly compute that this descends to the cohomology level, and from this the function

$$\smile:\check{H}^i(\mathcal{U}, \mathcal{F}) \times \check{H}^j(\mathcal{U}, \mathcal{G}) \rightarrow \check{H}^{i+j}(\mathcal{U}, \mathcal{F} \otimes \mathcal{G})$$

is defined. At the sheaf cohomology level we can also define this by taking injective resolutions $\mathcal{I}^\bullet$, $\mathcal{J}^\bullet$ of $\mathcal{F}$ and $\mathcal{G}$ respectively, and using the fact that their tensor product complex (that is, the total complex of the double complex whose components are $\mathcal{I}^p\otimes \mathcal{J}^q$) defines a resolution of $\mathcal{F}\otimes \mathcal{G}$.

In any case, by the cup product pairing we obtain the following bilinear map for cocycles of any locally free sheaf $\mathcal{E}$ and $\omega_{\mathbb{P}^n}\otimes \mathcal{E}^\vee$:

$$H^k(\mathbb{P}^n, \mathcal{E})\times H^{n-k}(\mathbb{P}^n, \omega_{\mathbb{P}^n}\otimes \mathcal{E}^\vee)\rightarrow H^n(\mathbb{P}^n, \mathcal{E}\otimes \omega_{\mathbb{P}^n}\otimes \mathcal{E}^\vee)$$

and then, using the isomorphism $\mathcal{E}\otimes \mathcal{E}^\vee\rightarrow \mathcal{O}_{\mathbb{P}^n}$ and the trace map above, we obtain the bilinear form

$$H^k(\mathbb{P}^n, \mathcal{E})\times H^{n-k}(\mathbb{P}^n, \omega_{\mathbb{P}^n}\otimes\mathcal{E}^\vee)\rightarrow \mathbb{K}$$

We show non-degeneracy for the case of $\mathcal{O}(d)$ by direct computation in [§Cohomology of Projective Spaces, ⁋Proposition 1](/en/math/algebraic_varieties/cohomology_of_projective_spaces#prop1), and we can extend this non-degeneracy to general locally free sheaves $\mathcal{E}$ using the syzygy theorem.

From the discussion so far we obtain the following.

::: Proposition 2 (Serre duality pairing, projective case)
For a locally free sheaf $\mathcal{E}$ on $\mathbb{P}^n$, the bilinear form

$$H^k(\mathbb{P}^n, \mathcal{E}) \times H^{n-k}(\mathbb{P}^n, \omega_{\mathbb{P}^n} \otimes \mathcal{E}^\vee) \rightarrow \mathbb{K};\quad (\alpha, \beta) \mapsto \tr(\alpha \smile \beta)$$

is a perfect pairing.
:::

More explicitly, Serre duality generally means the following isomorphism obtained from this:

$$H^k(\mathbb{P}^n, \mathcal{E})\cong H^{n-k}(\mathbb{P}^n, \omega_{\mathbb{P}^n}\otimes\mathcal{E}^\vee)^\ast$$

More generally, by the Noether normalization theorem for any $n$-dimensional smooth projective variety $X$ there exists a finite surjective morphism $f: X \rightarrow \mathbb{P}^n$. Then we can pull back Serre duality proved on $\mathbb{P}^n$ to $X$ via this finite morphism $f$, and in this setting Serre duality means the isomorphism

$$H^i(X, \mathcal{E}) \cong H^{n-i}(X, \omega_X \otimes \mathcal{E}^\vee)^\ast$$

::: Example 3
Let us look concretely at [Proposition 2](#prop2) on $\mathbb{P}^2$. Here $\omega_{\mathbb{P}^2} \cong \mathcal{O}(-3)$, so what Serre duality asserts is the isomorphism $H^k(\mathbb{P}^2, \mathcal{O}(d)) \cong H^{2-k}(\mathbb{P}^2, \mathcal{O}(-d-3))^\ast$.

First for the case $d=0$, by [§Cohomology of Projective Spaces, ⁋Proposition 1](/en/math/algebraic_varieties/cohomology_of_projective_spaces#prop1) we have

$$H^0(\mathbb{P}^2, \mathcal{O}) = \mathbb{K},\qquad H^1(\mathbb{P}^2, \mathcal{O}) = 0, \qquad H^2(\mathbb{P}^2, \mathcal{O}) = 0$$

and the cohomology of $\mathcal{O}(-3)$ is

$$H^0(\mathbb{P}^2, \mathcal{O}(-3)) = 0, \qquad H^1(\mathbb{P}^2, \mathcal{O}(-3)) = 0,\qquad H^2(\mathbb{P}^2, \mathcal{O}(-3)) = \mathbb{K}$$

so we can see that Serre duality holds. Similarly for the case $d=1$, the only nonzero cohomology is

$$H^0(\mathbb{P}^2, \mathcal{O}(1)) = \mathbb{K}^3$$

and by Serre duality we must have $H^0(\mathcal{O}(1)) \cong H^2(\mathcal{O}(-4))^\ast$, so $\dim H^2(\mathcal{O}(-4)) = 3$ should hold. Applying [§Cohomology of Projective Spaces, ⁋Proposition 1](/en/math/algebraic_varieties/cohomology_of_projective_spaces#prop1) again, the $H^2$ of $\mathcal{O}(-4)$ actually has dimension

$$\binom{2+(-4)}{2}=\binom{-2}{2} = 3$$

so we can check that they match.
:::

## Generalizations of Serre Duality

We generalize the discussion so far. The first thing we can do is to extend from locally free sheaves $\mathcal{E}$ to arbitrary coherent sheaves $\mathcal{E}$. This is not as difficult as one might think, because on a smooth variety any coherent sheaf has a finite length locally free resolution, so we can use the statement of Serre duality inductively. ([§Canonical Bundle](/en/math/algebraic_varieties/canonical_bundle))

After that we drop the smoothness condition on $X$. In this case there are two major problems: the first visible problem is that $X$ does not have a canonical line bundle. The other problem is slightly more subtle: when we obtained an explicit isomorphism from the perfect pairing, we rather implicitly used the isomorphism

$$\mathcal{H}om(\mathcal{E}, \mathcal{F})\cong \mathcal{E}^\vee\otimes \mathcal{F}$$

but this is actually possible only because $\mathcal{E}$ is locally free, and if $\mathcal{E}$ is a coherent sheaf and $X$ is singular then there is no guarantee that $\mathcal{E}$ has a finite length locally free resolution, so this isomorphism does not hold. Therefore we introduce derived functors again and call $\omega_X$ satisfying the formula

$$\Ext^i_X(\mathcal{F},\omega_X)\cong H^{n-i}(X,\mathcal{F})^\vee$$

the *dualizing sheaf* of $X$. In general its existence is guaranteed for Cohen-Macaulay varieties of pure dimension $n$; we will not give the definition, but the Cohen-Macaulay condition can be thought of intuitively as a notion including singular varieties that do not cause dimension problems.

A slightly less intuitive generalization is relative Serre duality. In fact, we have not paid attention to the underlying field $\mathbb{K}$ of the variety, but in this context it helps to make its role clear.

That an affine variety $X$ is defined over $\mathbb{K}$ means that its coordinate ring $A$ is a $\mathbb{K}$-algebra, so there exists a ring homomorphism $\mathbb{K}\rightarrow A$ containing this structure. Viewing these as morphisms between the coordinate rings of $\mathbb{A}^1_\mathbb{K}$ and $X$ respectively, this structure morphism is geometrically given as $X\rightarrow \mathbb{A}^1_\mathbb{K}$.

Relative Serre duality generalizes this setting by replacing the target $\mathbb{A}^1_\mathbb{K}$ with another variety. First, for arbitrary varieties $X,Y$, let us define that a morphism $f:X\rightarrow Y$ is a *smooth projective morphism* if the fiber $f^{-1}(y)$ over each $y\in Y$ is a smooth projective variety. Then in this case, since $f^{-1}(y)$ is a smooth projective variety, the canonical line bundle $\omega_{X_y}$ will exist, and the *relative dualizing sheaf* $\omega_{X/Y}$ on $X$ is defined by consistently collecting these. That is, $\omega_{X/Y}$ is a sheaf satisfying $\omega_{X/Y}\vert_{X_y}\cong\omega_{X_y}$ for each $y$. Then the generalization in this case is as follows.

::: Proposition 4 (Relative Serre duality)
For a smooth projective morphism $f \colon X \rightarrow Y$, let $n = \dim X - \dim Y$. Then

$$R^n f_\ast \omega_{X/Y} \cong \mathcal{O}_Y$$

and for $i \neq n$ we have $R^i f_\ast \omega_{X/Y} = 0$.
:::

## Grothendieck Duality

Let us retrace the process of generalizing Serre duality. We first proved Serre duality on $\mathbb{P}^n$ using the trace map and cup product ([Proposition 2](#prop2)), and extended this to arbitrary smooth projective varieties via a finite morphism. The extension to coherent sheaves was handled by induction using locally free resolutions, and the extension to singular varieties was handled by introducing the dualizing sheaf. [Proposition 4](#prop4) was the generalization replacing the target from a point to an arbitrary variety.

The most modern interpretation of Serre duality is Grothendieck duality, which is formulated in the language of derived categories. ([[Homological Algebra] §Derived Categories, ⁋Definition 2](/en/math/homological_algebra/derived_categories#def2)) This generalization is quite convincing in terms of motivation; for example, we already had to think about injective resolutions when defining sheaf cohomology, and we also had to think about locally free resolutions when generalizing Serre duality to arbitrary coherent sheaves above, so we know that the derived category is where everything actually happens. In particular, the key content is that the perfect pairing in Serre duality is in fact information equivalent to the choice of a concrete isomorphism

$$H^n(X, \omega_X) \cong \mathbb{K}$$

and lifting this to the derived category gives the observation that it is a special case of the adjunction between the derived pushforward $R f_\ast$ and its right adjoint. Concretely, the Serre duality isomorphism

$$H^i(X, \mathcal{E}) \cong H^{n-i}(X, \omega_X \otimes \mathcal{E}^\vee)^\ast$$

is derived from the following adjunction isomorphism in the derived category:

$$\operatorname{Hom}_{D(X)}(\mathcal{F}, f^! \mathcal{G}) \cong \operatorname{Hom}_{D(Y)}(R f_\ast \mathcal{F}, \mathcal{G})$$

Here the *exceptional inverse image* $f^!$ is the functor defined as the right adjoint of $R f_\ast$ in the derived category, and to define this well one must necessarily formulate it in the derived category.

As mentioned earlier, Grothendieck duality is a result containing relative Serre duality. To see this, consider the case of a smooth morphism $f:X\rightarrow Y$; then $f^! \mathcal{O}_Y \cong \omega_{X/Y}[n]$ holds, and from this we can see that $\omega_{X/Y}$ being in the correct dimension is exactly $f^!\mathcal{O}_Y$.

::: Proposition 5 (Grothendieck Duality)
For a proper morphism $f \colon X \rightarrow Y$ and a coherent sheaf $\mathcal{F}$ on $X$, the following isomorphism holds in the derived category:

$$R f_\ast R\mathcal{H}om_{\mathcal{O}_X}(\mathcal{F}, f^! \mathcal{G}) \cong R\mathcal{H}om_{\mathcal{O}_Y}(R f_\ast \mathcal{F}, \mathcal{G})$$

Here $R\mathcal{H}om$ is the derived Hom ([[Homological Algebra] §Derived Categories, ⁋Proposition 10](/en/math/homological_algebra/derived_categories#prop10)), and $\mathcal{G}$ is a bounded complex of coherent sheaves on $Y$.
:::

Intuitively this theorem means that "pushforward then Hom" and "Hom then pushforward" are the same. That is, computing the Hom between $\mathcal{F}$ and $f^! \mathcal{G}$ on $X$ and then pushing down to $Y$ is the same as first pushing $\mathcal{F}$ down to $Y$ and then computing the Hom with $\mathcal{G}$.

---

**References**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Ser]** J.-P. Serre, *Faisceaux algébriques cohérents*, Annals of Mathematics, 1955.

---
