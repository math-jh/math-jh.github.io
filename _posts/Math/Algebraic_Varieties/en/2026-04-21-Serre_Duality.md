---
title: "Serre Duality"
description: "We discuss the natural duality between line bundles and cohomology on projective spaces, and examine the cup product and the construction of Serre duality."
excerpt: "Serre duality theorem and its applications"

categories: [Math / Algebraic Varieties]
permalink: /en/math/algebraic_varieties/serre_duality
sidebar: 
    nav: "algebraic_varieties-en"

date: 2026-04-21
weight: 15
translated_at: 2026-08-19T00:45:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-09-27T19:15:05+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
Geometrically, in favorable cases there is a natural duality between dimension $k$ cohomology and codimension $k$ cohomology. To prove this we used the perfect pairing

$$H^k(M;R)\times H^{n-k}(M;R)\rightarrow R$$

and through it obtained results such as [\[Algebraic Topology\] §Poincaré Duality, ⁋Theorem 11](/en/math/algebraic_topology/Poincare_duality#thm11){: data-lid="c1nny" }. More concretely, since this pairing is constructed via the cap product and the fundamental class $[M] \in H_n(M;R)$, we may say that the source of duality in topology is the orientation class $[M]$.

In this post we examine Serre duality, the algebraic geometry version of duality.

## Serre Duality on Projective Space

We first examine rigorously only the case $X=\mathbb{P}^n$. We know that every line bundle defined on $\mathbb{P}^n$ is of the form $\mathcal{O}(d)$, and in particular we saw in [§Canonical Line Bundle, §§Canonical Bundle of $\mathbb{P}^n$](/en/math/algebraic_varieties/canonical_bundle#canonical-bundle-of-mathbbpn){: data-lid="0hq5l" } that this is $\mathcal{O}(-n-1)$. Then from [§Cohomology of Projective Space, ⁋Proposition 1](/en/math/algebraic_varieties/cohomology_of_projective_spaces#prop1){: data-lid="relbx" } we obtain the following.

::: Proposition 1
For the canonical line bundle $\omega_X$ on projective space $X=\mathbb{P}^n$, there exists an isomorphism

$$H^n(X, \omega_X)\cong \mathbb{K}$$

:::

In general this is understood as the isomorphism that explicitly takes $\x_0^{-1}\cdots\x_n^{-1}$ as a basis, but it is uniquely determined only up to scalar multiplication. Choosing such a normalization is concretely equivalent to choosing the *trace map* $\tr:H^n(\mathbb{P}^n, \omega_{\mathbb{P}^n}) \rightarrow \mathbb{K}$.

To obtain the duality pairing we now need to define the cup product. For convenience, let us work at the level of Čech cohomology. For any topological space $X$, an open cover of $X$, $\mathcal{U}$, and sheaves $\mathcal{F}$, $\mathcal{G}$ defined on $X$, the cup product of two Čech cochains $\alpha \in \check{C}^p(\mathcal{U}, \mathcal{F})$, $\beta \in \check{C}^q(\mathcal{U}, \mathcal{G})$ is defined by the formula

$$(\alpha \smile \beta)_{i_0, \ldots, i_{p+q}} = \alpha_{i_0,\ldots,i_p}\big\vert_{U_{i_0,\ldots,i_{p+q}}} \otimes \beta_{i_p,\ldots,i_{p+q}}\big\vert_{U_{i_0,\ldots,i_{p+q}}}\in \check{C}^{p+q}(\mathcal{U}, \mathcal{F}\otimes\mathcal{G})$$

We can explicitly compute that this descends to the cohomology level, and from this the map

$${\smile}:\check{H}^p(\mathcal{U}, \mathcal{F}) \times \check{H}^q(\mathcal{U}, \mathcal{G}) \rightarrow \check{H}^{p+q}(\mathcal{U}, \mathcal{F} \otimes \mathcal{G})$$

is defined. At the sheaf cohomology level as well, we can define this by taking, for $\mathcal{F}$ and $\mathcal{G}$, flat resolutions $\mathcal{I}^\bullet$, $\mathcal{J}^\bullet$ respectively, and then using their tensor product complex (that is, the total complex of the double complex with components $\mathcal{I}^p\otimes \mathcal{J}^q$).

In any case, by the cup product pairing, for cocycles of an arbitrary locally free sheaf $\mathcal{E}$ and $\omega_{\mathbb{P}^n}\otimes \mathcal{E}^\vee$ we obtain the bilinear map

$$H^k(\mathbb{P}^n, \mathcal{E})\times H^{n-k}(\mathbb{P}^n, \omega_{\mathbb{P}^n}\otimes \mathcal{E}^\vee)\rightarrow H^n(\mathbb{P}^n, \mathcal{E}\otimes \omega_{\mathbb{P}^n}\otimes \mathcal{E}^\vee)$$

and then, using the evaluation map $\mathcal{E}\otimes \mathcal{E}^\vee\rightarrow \mathcal{O}_{\mathbb{P}^n}$ and the trace map above, we obtain the bilinear form

$$H^k(\mathbb{P}^n, \mathcal{E})\times H^{n-k}(\mathbb{P}^n, \omega_{\mathbb{P}^n}\otimes\mathcal{E}^\vee)\rightarrow \mathbb{K}$$

We show non-degeneracy in the case of $\mathcal{O}(d)$ by direct computation in [§Cohomology of Projective Space, ⁋Proposition 1](/en/math/algebraic_varieties/cohomology_of_projective_spaces#prop1){: data-lid="yhtau" }, and using the syzygy theorem we can show this non-degeneracy for a general locally free sheaf $\mathcal{E}$.

From the discussion so far we obtain the following.

::: Proposition 2 (Serre duality pairing, projective case)
On $\mathbb{P}^n$, for a locally free sheaf $\mathcal{E}$, the bilinear form

$$H^k(\mathbb{P}^n, \mathcal{E}) \times H^{n-k}(\mathbb{P}^n, \omega_{\mathbb{P}^n} \otimes \mathcal{E}^\vee) \rightarrow \mathbb{K};\quad (\alpha, \beta) \mapsto \tr(\alpha \smile \beta)$$

is a perfect pairing.
:::

More explicitly, Serre duality generally means the following isomorphism obtained from this:

$$H^k(\mathbb{P}^n, \mathcal{E})\cong H^{n-k}(\mathbb{P}^n, \omega_{\mathbb{P}^n}\otimes\mathcal{E}^\vee)^\ast$$

More generally, by the Noether normalization theorem, for any $n$-dimensional smooth projective variety $X$ there exists a finite surjective morphism $f: X \rightarrow \mathbb{P}^n$. Then, via this finite morphism $f$, we can transfer Serre duality proved on $\mathbb{P}^n$ to $X$, and in this setting Serre duality means the following isomorphism:

$$H^i(X, \mathcal{E}) \cong H^{n-i}(X, \omega_X \otimes \mathcal{E}^\vee)^\ast$$

::: Example 3
Let us look concretely at [Proposition 2](#prop2){: data-lid="yyn3c" } on $\mathbb{P}^2$. Here $\omega_{\mathbb{P}^2} \cong \mathcal{O}(-3)$, so what Serre duality asserts is the isomorphism $H^k(\mathbb{P}^2, \mathcal{O}(d)) \cong H^{2-k}(\mathbb{P}^2, \mathcal{O}(-d-3))^\ast$.

First, for $d=0$, by [§Cohomology of Projective Space, ⁋Proposition 1](/en/math/algebraic_varieties/cohomology_of_projective_spaces#prop1){: data-lid="zktc0" } we have

$$H^0(\mathbb{P}^2, \mathcal{O}) = \mathbb{K},\qquad H^1(\mathbb{P}^2, \mathcal{O}) = 0, \qquad H^2(\mathbb{P}^2, \mathcal{O}) = 0$$

and the cohomology of $\mathcal{O}(-3)$ is

$$H^0(\mathbb{P}^2, \mathcal{O}(-3)) = 0, \qquad H^1(\mathbb{P}^2, \mathcal{O}(-3)) = 0,\qquad H^2(\mathbb{P}^2, \mathcal{O}(-3)) = \mathbb{K}$$

so we see that Serre duality holds. Similarly, for $d=1$, the only nonzero cohomology is

$$H^0(\mathbb{P}^2, \mathcal{O}(1)) = \mathbb{K}^3$$

and by Serre duality we must have $H^0(\mathcal{O}(1)) \cong H^2(\mathcal{O}(-4))^\ast$, so we should have $\dim H^2(\mathcal{O}(-4)) = 3$. Applying [§Cohomology of Projective Space, ⁋Proposition 1](/en/math/algebraic_varieties/cohomology_of_projective_spaces#prop1){: data-lid="7jkzc" } again, indeed for $\mathcal{O}(-4)$, $H^2$ has dimension

$$\binom{2+(-4)}{2}=\binom{-2}{2} = 3$$

so we can confirm that they match.
:::

## Generalizations of Serre Duality

We now generalize our discussion so far. The very first thing we can do is to extend from a locally free sheaf $\mathcal{E}$ to an arbitrary coherent sheaf $\mathcal{E}$. This is not as difficult as it might seem, because on a smooth variety any coherent sheaf has a finite length locally free resolution, so one can inductively transfer Serre duality, which holds on each term of the resolution, along the resolution. ([§Canonical Line Bundle](/en/math/algebraic_varieties/canonical_bundle){: data-lid="iptvt" }) However, the statement transferred in this way is not a duality between $H^i(X,\mathcal{E})$ and $H^{n-i}(X,\omega_X\otimes\mathcal{E}^\vee)$, but rather takes a form using $\Ext$ that we shall see below.

After that, we drop the smoothness condition on $X$. In this case there are two major problems: the first visible problem is the fact that $X$ does not have a canonical line bundle. Another problem is somewhat subtle: when obtaining the explicit isomorphism from the perfect pairing, we somewhat implicitly used the following isomorphism

$$\mathcal{H}om(\mathcal{E}, \mathcal{F})\cong \mathcal{E}^\vee\otimes \mathcal{F}$$

but in fact this is possible because $\mathcal{E}$ is locally free, and for a coherent sheaf $\mathcal{E}$ that is not locally free, this isomorphism does not generally hold even if $X$ is smooth. For example, on $X=\mathbb{A}^1$, the skyscraper sheaf $\mathcal{E}=\mathcal{O}_X/\mathfrak{m}_0$ at the origin satisfies $\mathcal{E}^\vee=0$, but $\mathcal{H}om(\mathcal{E},\mathcal{E})\cong\mathcal{E}$ is not $0$, and if $X$ is singular, we cannot even use the argument of transferring along a finite length locally free resolution as before. Therefore, we introduce derived functors again: on $X$, for every coherent sheaf $\mathcal{F}$ and every $i$, we call a sheaf satisfying the formula

$$\Ext^i_X(\mathcal{F},\omega_X)\cong H^{n-i}(X,\mathcal{F})^\ast$$

the *dualizing sheaf* $\omega_X$ of $X$. In general, its existence is guaranteed for Cohen-Macaulay varieties of pure dimension $n$, and although we will not give the definition, the Cohen-Macaulay condition can be thought of intuitively as a concept encompassing singular varieties that do not cause dimension problems.

A somewhat less intuitive version of the generalization is relative Serre duality. It is true that we have not paid attention to the underlying field $\mathbb{K}$ of the variety so far, but in this context it is helpful to make its role clear.

That an affine variety $X$ is defined over $\mathbb{K}$ means that its coordinate ring $A$ is a $\mathbb{K}$-algebra, so there exists a ring homomorphism $\mathbb{K}\rightarrow A$ encoding this structure. If we view this as a morphism between the coordinate rings of a point $\Spec\mathbb{K}$ and of $X$, respectively, this structure morphism is geometrically given by $X\rightarrow \Spec\mathbb{K}$, that is, a morphism to a point.

Relative Serre duality generalizes this setting by replacing the target point $\Spec\mathbb{K}$ with another variety. First, for arbitrary varieties $X,Y$, let us define a morphism $f:X\rightarrow Y$ to be a *smooth projective morphism* if $f$ is a flat proper morphism and, for each $y\in Y$, the fiber $f^{-1}(y)$ is a smooth projective variety. Then in this case, $f^{-1}(y)$, as a smooth projective variety, will have a canonical line bundle $\omega_{X_y}$, and consistently assembling these defines the *relative dualizing sheaf* $\omega_{X/Y}$ on $X$. That is, $\omega_{X/Y}$ is a sheaf satisfying, for each $y$, $\omega_{X/Y}\vert_{X_y}\cong\omega_{X_y}$. Then the generalization in this case is as follows.

::: Proposition 4 (Relative Serre duality)
For a smooth projective morphism $f \colon X \rightarrow Y$, let $n = \dim X - \dim Y$, and assume that $R^j f_\ast \mathcal{O}_X$ is locally free for all $j$.[^1] Then for all $i$ there exists an isomorphism

$$R^i f_\ast \omega_{X/Y} \cong (R^{n-i} f_\ast \mathcal{O}_X)^\vee$$

In particular, since each fiber is a variety, it is connected, and therefore $f_\ast \mathcal{O}_X \cong \mathcal{O}_Y$, so for $i = n$ we have $R^n f_\ast \omega_{X/Y} \cong \mathcal{O}_Y$.
:::

## Grothendieck duality

Let us retrace the steps of generalizing Serre duality earlier. We first proved Serre duality on $\mathbb{P}^n$ using the trace map and cup product ([Proposition 2](#prop2){: data-lid="dp6qq" }), and extended this to arbitrary smooth projective varieties via a finite morphism. Afterwards, the extension to coherent sheaves was handled by induction through locally free resolutions, and the extension to singular varieties was handled by introducing the dualizing sheaf. [Proposition 4](#prop4){: data-lid="rotdz" } was the generalization changing the target from a point to an arbitrary variety.

The most modern interpretation of Serre duality is Grothendieck duality, which is formulated in the language of derived categories. ([\[Homological Algebra\] §Derived Categories, ⁋Definition 2](/en/math/homological_algebra/derived_categories#def2){: data-lid="8eaod" }) Compared to its language, the motivation for this generalization is quite convincing: for example, even when defining sheaf cohomology we already had to think about injective resolutions, and above when generalizing Serre duality to arbitrary coherent sheaves we also had to think about locally free resolutions, so we know that the derived category is where everything actually happens. In particular, the key content is that the perfect pairing in Serre duality is in fact the same information as the choice of a concrete isomorphism

$$H^n(X, \omega_X) \cong \mathbb{K}$$

and the observation that, when lifted to the derived category, it is a special case of the adjunction between the derived pushforward $R f_\ast$ and its right adjoint. Concretely, the Serre duality isomorphism

$$H^i(X, \mathcal{E}) \cong H^{n-i}(X, \omega_X \otimes \mathcal{E}^\vee)^\ast$$

is derived from the following adjunction isomorphism in the derived category:

$$\operatorname{Hom}_{D(X)}(\mathcal{F}, f^! \mathcal{G}) \cong \operatorname{Hom}_{D(Y)}(R f_\ast \mathcal{F}, \mathcal{G})$$

Here the *exceptional inverse image* $f^!$ is the functor defined as the right adjoint of $R f_\ast$ in the derived category, and to define this properly one must necessarily formulate it in the derived category.

As mentioned earlier, Grothendieck duality is a result that includes relative Serre duality. To see this, consider the case of a smooth morphism $f:X\rightarrow Y$; then $f^! \mathcal{O}_Y \cong \omega_{X/Y}[n]$ holds, and from this we see that $\omega_{X/Y}$ placed in the correct dimension is precisely $f^!\mathcal{O}_Y$.

::: Proposition 5 (Grothendieck Duality)
For a proper morphism $f \colon X \rightarrow Y$ and a coherent sheaf $\mathcal{F}$ on $X$, the following isomorphism holds in the derived category:

$$R f_\ast R\mathcal{H}om_{\mathcal{O}_X}(\mathcal{F}, f^! \mathcal{G}) \cong R\mathcal{H}om_{\mathcal{O}_Y}(R f_\ast \mathcal{F}, \mathcal{G})$$

Here $R\mathcal{H}om$ is the derived Hom ([\[Homological Algebra\] §Derived Categories, ⁋Proposition 11](/en/math/homological_algebra/derived_categories#prop11){: data-lid="24lhg" }), and $\mathcal{G}$ is a bounded complex of coherent sheaves on $Y$.
:::

Intuitively, this theorem means that 'Hom after pushforward' and 'pushforward after Hom' are the same. That is, computing the Hom between $\mathcal{F}$ and $f^! \mathcal{G}$ on $X$ and then pushing down to $Y$ is the same as first pushing $\mathcal{F}$ down to $Y$ and then computing the Hom with $\mathcal{G}$.

---

**References**

**[Hart]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Ser]** J.-P. Serre, *Faisceaux algébriques cohérents*, Annals of Mathematics, 1955.

---

[^1]: This condition always holds by the degeneration of the Hodge-de Rham spectral sequence if $\operatorname{char}\mathbb{K}=0$. It can fail in characteristic $p$.
