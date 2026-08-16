---
title: "Serre Duality"
description: "We discuss the natural duality between line bundles and cohomology on projective spaces, and examine the construction process of cup products and Serre duality."
excerpt: "Serre duality theorem and its applications"

categories: [Math / Algebraic Varieties]
permalink: /en/math/algebraic_varieties/serre_duality
sidebar: 
    nav: "algebraic_varieties-en"

date: 2026-04-21
weight: 15
translated_at: 2026-08-16T02:17:24+00:00
translation_source: kimi-cli
---
Geometrically, in favorable situations there is a natural duality between cohomology of dimension $k$ and cohomology of codimension $k$. To prove this we used the perfect pairing

$$H^k(M;R)\times H^{n-k}(M;R)\rightarrow R$$

and through it obtained results such as [[Algebraic Topology] §Poincaré Duality, ⁋Theorem 11](/en/math/algebraic_topology/Poincare_duality#thm11). More specifically, since this pairing is constructed via the cap product and the fundamental class $[M] \in H_n(M;R)$, we may say that the source of duality in topology is the orientation class $[M]$.

In this post we examine Serre duality, the algebraic geometry version of duality.

## Serre Duality on Projective Space

We first look carefully at the case $X=\mathbb{P}^n$. We know that every line bundle defined on $\mathbb{P}^n$ is of the form $\mathcal{O}(d)$, and in particular we saw in [§Canonical Line Bundle, §§The Canonical Bundle of $\mathbb{P}^n$](/en/math/algebraic_varieties/canonical_bundle#the-canonical-bundle-of-mathbbpn) that this is $\mathcal{O}(-n-1)$. Then from [§Cohomology of Projective Space, ⁋Proposition 1](/en/math/algebraic_varieties/cohomology_of_projective_spaces#prop1) we obtain the following.

::: Proposition 1
For the canonical line bundle $\omega_X$ on projective space $X=\mathbb{P}^n$, there exists an isomorphism

$$H^n(X, \omega_X)\cong \mathbb{K}.$$
:::

Generally this is understood as the isomorphism that explicitly takes $\x_0^{-1}\cdots\x_n^{-1}$ as its basis, but it is determined only up to scalar multiplication. Choosing such a normalization is the same as concretely choosing a *trace map* $\tr:H^n(\mathbb{P}^n, \omega_{\mathbb{P}^n}) \rightarrow \mathbb{K}$.

Now, to obtain the duality pairing we must define the cup product. For convenience let us work at the level of Čech cohomology. For any topological space $X$, an open cover $\mathcal{U}$ of $X$, and sheaves $\mathcal{F}$, $\mathcal{G}$ defined on $X$, the cup product of two Čech cochains $\alpha \in \check{C}^p(\mathcal{U}, \mathcal{F})$, $\beta \in \check{C}^q(\mathcal{U}, \mathcal{G})$ is defined by the formula

$$(\alpha \smile \beta)_{i_0, \ldots, i_{p+q}} = \alpha_{i_0,\ldots,i_p}\big\vert_{U_{i_0,\ldots,i_{p+q}}} \otimes \beta_{i_p,\ldots,i_{p+q}}\big\vert_{U_{i_0,\ldots,i_{p+q}}}\in \check{C}^{p+q}(\mathcal{U}, \mathcal{F}\otimes\mathcal{G}).$$

We can explicitly compute that this descends to the cohomology level, and from this the map

$$\smile:\check{H}^p(\mathcal{U}, \mathcal{F}) \times \check{H}^q(\mathcal{U}, \mathcal{G}) \rightarrow \check{H}^{p+q}(\mathcal{U}, \mathcal{F} \otimes \mathcal{G})$$

is defined. At the sheaf cohomology level one can also define this by taking flat resolutions $\mathcal{I}^\bullet$, $\mathcal{J}^\bullet$ of $\mathcal{F}$ and $\mathcal{G}$ respectively, and then using the tensor product complex (that is, the total complex of the double complex whose components are $\mathcal{I}^p\otimes \mathcal{J}^q$).

In any case, by the cup product pairing we obtain for any locally free sheaf $\mathcal{E}$ and any cocycle of $\omega_{\mathbb{P}^n}\otimes \mathcal{E}^\vee$ the bilinear map

$$H^k(\mathbb{P}^n, \mathcal{E})\times H^{n-k}(\mathbb{P}^n, \omega_{\mathbb{P}^n}\otimes \mathcal{E}^\vee)\rightarrow H^n(\mathbb{P}^n, \mathcal{E}\otimes \omega_{\mathbb{P}^n}\otimes \mathcal{E}^\vee)$$

and then, using the evaluation map $\mathcal{E}\otimes \mathcal{E}^\vee\rightarrow \mathcal{O}_{\mathbb{P}^n}$ together with the trace map above, we obtain the bilinear form

$$H^k(\mathbb{P}^n, \mathcal{E})\times H^{n-k}(\mathbb{P}^n, \omega_{\mathbb{P}^n}\otimes\mathcal{E}^\vee)\rightarrow \mathbb{K}.$$

We show non-degeneracy for the case of $\mathcal{O}(d)$ by direct computation in [§Cohomology of Projective Space, ⁋Proposition 1](/en/math/algebraic_varieties/cohomology_of_projective_spaces#prop1), and then extend this non-degeneracy to a general locally free sheaf $\mathcal{E}$ using the syzygy theorem.

From the discussion so far we obtain the following.

::: Proposition 2 (Serre duality pairing, projective case)
For a locally free sheaf $\mathcal{E}$ on $\mathbb{P}^n$, the bilinear form

$$H^k(\mathbb{P}^n, \mathcal{E}) \times H^{n-k}(\mathbb{P}^n, \omega_{\mathbb{P}^n} \otimes \mathcal{E}^\vee) \rightarrow \mathbb{K};\quad (\alpha, \beta) \mapsto \tr(\alpha \smile \beta)$$

is a perfect pairing.
:::

More explicitly, Serre duality generally means the following isomorphism obtained from this:

$$H^k(\mathbb{P}^n, \mathcal{E})\cong H^{n-k}(\mathbb{P}^n, \omega_{\mathbb{P}^n}\otimes\mathcal{E}^\vee)^\ast.$$

More generally, by the Noether normalization theorem, for any smooth projective variety $X$ of dimension $n$ there exists a finite surjective morphism $f: X \rightarrow \mathbb{P}^n$. Then we can pull back Serre duality, proved on $\mathbb{P}^n$, to $X$ via this finite morphism $f$, and in this setting Serre duality means the isomorphism

$$H^i(X, \mathcal{E}) \cong H^{n-i}(X, \omega_X \otimes \mathcal{E}^\vee)^\ast.$$

::: Example 3
Let us examine [Proposition 2](#prop2) concretely on $\mathbb{P}^2$. Here $\omega_{\mathbb{P}^2} \cong \mathcal{O}(-3)$, so what Serre duality asserts is the isomorphism $H^k(\mathbb{P}^2, \mathcal{O}(d)) \cong H^{2-k}(\mathbb{P}^2, \mathcal{O}(-d-3))^\ast$.

First, for $d=0$, by [§Cohomology of Projective Space, ⁋Proposition 1](/en/math/algebraic_varieties/cohomology_of_projective_spaces#prop1) we have

$$H^0(\mathbb{P}^2, \mathcal{O}) = \mathbb{K},\qquad H^1(\mathbb{P}^2, \mathcal{O}) = 0, \qquad H^2(\mathbb{P}^2, \mathcal{O}) = 0$$

and the cohomology of $\mathcal{O}(-3)$ is

$$H^0(\mathbb{P}^2, \mathcal{O}(-3)) = 0, \qquad H^1(\mathbb{P}^2, \mathcal{O}(-3)) = 0,\qquad H^2(\mathbb{P}^2, \mathcal{O}(-3)) = \mathbb{K},$$

so we see that Serre duality holds. Similarly for $d=1$, the only nonzero cohomology is

$$H^0(\mathbb{P}^2, \mathcal{O}(1)) = \mathbb{K}^3,$$

and by Serre duality we must have $H^0(\mathcal{O}(1)) \cong H^2(\mathcal{O}(-4))^\ast$, so $\dim H^2(\mathcal{O}(-4))$ should be $3$. Applying [§Cohomology of Projective Space, ⁋Proposition 1](/en/math/algebraic_varieties/cohomology_of_projective_spaces#prop1) again, the $H^2$ of $\mathcal{O}(-4)$ actually has dimension

$$\binom{2+(-4)}{2}=\binom{-2}{2} = 3,$$

so we can check that they agree.
:::

## Generalizations of Serre Duality

We now generalize the discussion so far. The first thing one can do is to extend from locally free sheaves $\mathcal{E}$ to arbitrary coherent sheaves $\mathcal{E}$. This is not as difficult as it might seem, because on a smooth variety any coherent sheaf has a finite length locally free resolution, so one simply carries Serre duality for each term of the resolution inductively along the resolution. ([§Canonical Line Bundle](/en/math/algebraic_varieties/canonical_bundle)) However, the statement obtained this way is not a duality between $H^i(X,\mathcal{E})$ and $H^{n-i}(X,\omega_X\otimes\mathcal{E}^\vee)$, but rather takes the form using $\Ext$ that we shall see below.

Next we drop the smoothness condition on $X$. In this case there are broadly two problems. The first problem that appears is the fact that $X$ does not have a canonical line bundle. Another problem is somewhat subtle: when we obtained the explicit isomorphism from the perfect pairing, we somewhat implicitly used the isomorphism

$$\mathcal{H}om(\mathcal{E}, \mathcal{F})\cong \mathcal{E}^\vee\otimes \mathcal{F},$$

but in reality this is possible only because $\mathcal{E}$ is locally free, and for a coherent sheaf $\mathcal{E}$ that is not locally free this isomorphism does not generally hold even if $X$ is smooth. For example, if we take the skyscraper sheaf $\mathcal{E}=\mathcal{O}_X/\mathfrak{m}_0$ at the origin on $X=\mathbb{A}^1$, then $\mathcal{E}^\vee=0$ but $\mathcal{H}om(\mathcal{E},\mathcal{E})\cong\mathcal{E}$ is not $0$. When $X$ is smooth, the argument of carrying over to the locally free case via a finite length locally free resolution remains as before, but if $X$ is singular there is not even any guarantee that such a resolution has finite length. Therefore we introduce derived functors again, and call $\omega_X$ the *dualizing sheaf* of $X$ if it satisfies

$$\Ext^i_X(\mathcal{F},\omega_X)\cong H^{n-i}(X,\mathcal{F})^\ast$$

for all coherent sheaves $\mathcal{F}$ on $X$ and all $i$. In general, its existence is guaranteed for Cohen-Macaulay varieties of pure dimension $n$, and although we will not give the definition, one may think of the Cohen-Macaulay condition intuitively as a notion that includes singular varieties which do not cause dimension problems.

A somewhat less intuitive generalization is relative Serre duality. In fact, we have not paid attention to the underlying field $\mathbb{K}$ of the variety, but in this context it helps to make its role explicit.

That an affine variety $X$ is defined over $\mathbb{K}$ means that its coordinate ring $A$ is a $\mathbb{K}$-algebra, so there exists a ring homomorphism $\mathbb{K}\rightarrow A$ encoding this structure. Viewing these respectively as morphisms between the one-point scheme $\Spec\mathbb{K}$ and the coordinate ring of $X$, this structure morphism is geometrically given as the map $X\rightarrow \Spec\mathbb{K}$, that is, the map to a point.

Relative Serre duality generalizes this setting by replacing the target one-point scheme $\Spec\mathbb{K}$ with another variety. First, for arbitrary varieties $X,Y$, let us define a morphism $f:X\rightarrow Y$ to be a *smooth projective morphism* if $f$ is a flat proper morphism and each fiber $f^{-1}(y)$ over $y\in Y$ is a smooth projective variety. Then in this case, each fiber $f^{-1}(y)$ is a smooth projective variety so it will have a canonical line bundle $\omega_{X_y}$, and these can be assembled consistently into a *relative dualizing sheaf* $\omega_{X/Y}$ defined on $X$. That is, $\omega_{X/Y}$ is a sheaf satisfying $\omega_{X/Y}\vert_{X_y}\cong\omega_{X_y}$ for each $y$. Then the generalization in this case is as follows.

::: Proposition 4 (Relative Serre duality)
Let $f \colon X \rightarrow Y$ be a smooth projective morphism with $n = \dim X - \dim Y$, and assume that $R^j f_\ast \mathcal{O}_X$ is locally free for all $j$.[^1] Then for all $i$ there exists an isomorphism

$$R^i f_\ast \omega_{X/Y} \cong (R^{n-i} f_\ast \mathcal{O}_X)^\vee.$$

In particular, since each fiber is a variety it is connected, and therefore $f_\ast \mathcal{O}_X \cong \mathcal{O}_Y$, so for $i = n$ we have $R^n f_\ast \omega_{X/Y} \cong \mathcal{O}_Y$.
:::

## Grothendieck Duality

Let us retrace the steps in generalizing Serre duality. We first proved Serre duality on $\mathbb{P}^n$ using the trace map and cup product ([Proposition 2](#prop2)), and extended this to an arbitrary smooth projective variety via a finite morphism. The extension to coherent sheaves was handled by induction via locally free resolutions, and the extension to singular varieties was handled by introducing the dualizing sheaf. [Proposition 4](#prop4) was the generalization replacing the target point by an arbitrary variety.

The most modern interpretation of Serre duality is Grothendieck duality, which is formulated in the language of derived categories. ([[Homological Algebra] §Derived Categories, ⁋Definition 2](/en/math/homological_algebra/derived_categories#def2)) This generalization is quite convincing in its motivation: for example, when we defined sheaf cohomology we had to think about injective resolutions, and when we generalized Serre duality to arbitrary coherent sheaves above we had to think about locally free resolutions, so we know that the derived category is where everything actually happens. In particular, the key point is that the perfect pairing in Serre duality is in fact the same information as the choice of a concrete isomorphism

$$H^n(X, \omega_X) \cong \mathbb{K},$$

and lifting this to the derived category yields the observation that it is a special case of the adjunction between the derived pushforward $R f_\ast$ and its right adjoint. Specifically, the Serre duality isomorphism

$$H^i(X, \mathcal{E}) \cong H^{n-i}(X, \omega_X \otimes \mathcal{E}^\vee)^\ast$$

is derived from the following adjunction isomorphism in the derived category:

$$\operatorname{Hom}_{D(X)}(\mathcal{F}, f^! \mathcal{G}) \cong \operatorname{Hom}_{D(Y)}(R f_\ast \mathcal{F}, \mathcal{G}).$$

Here the *exceptional inverse image* $f^!$ is the functor defined as the right adjoint of $R f_\ast$ in the derived category, and to define it properly one must necessarily work in the derived category.

As mentioned earlier, Grothendieck duality is a result that includes relative Serre duality. To see this, consider the case of a smooth morphism $f:X\rightarrow Y$; then $f^! \mathcal{O}_Y \cong \omega_{X/Y}[n]$ holds, and from this we can see that $\omega_{X/Y}$ in the correct dimension is exactly $f^!\mathcal{O}_Y$.

::: Proposition 5 (Grothendieck Duality)
For a proper morphism $f \colon X \rightarrow Y$ and a coherent sheaf $\mathcal{F}$ on $X$, the following isomorphism holds in the derived category:

$$R f_\ast R\mathcal{H}om_{\mathcal{O}_X}(\mathcal{F}, f^! \mathcal{G}) \cong R\mathcal{H}om_{\mathcal{O}_Y}(R f_\ast \mathcal{F}, \mathcal{G}).$$

Here $R\mathcal{H}om$ is derived Hom ([[Homological Algebra] §Derived Categories, ⁋Proposition 10](/en/math/homological_algebra/derived_categories#prop10)), and $\mathcal{G}$ is a bounded complex of coherent sheaves on $Y$.
:::

Intuitively, this theorem means that "pushforward then Hom" is the same as "Hom then pushforward." That is, computing the Hom between $\mathcal{F}$ and $f^! \mathcal{G}$ on $X$ and then pushing down to $Y$ is the same as first pushing $\mathcal{F}$ down to $Y$ and then computing the Hom with $\mathcal{G}$.

---

**References**

**[Hart]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Ser]** J.-P. Serre, *Faisceaux algébriques cohérents*, Annals of Mathematics, 1955.

---

[^1]: This condition always holds in characteristic $\operatorname{char}\mathbb{K}=0$ by the degeneration of the Hodge-de Rham spectral sequence. It can fail in characteristic $p$.
