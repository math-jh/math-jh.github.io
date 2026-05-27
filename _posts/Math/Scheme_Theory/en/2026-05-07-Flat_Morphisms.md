---
title: "Flat Morphisms"
excerpt: "Flat morphisms in algebraic geometry"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/flat_morphisms
header:
    overlay_image: /assets/images/Math/Scheme_Theory/Flat_morphisms.png
    overlay_filter: 0.5
sidebar: 
    nav: "scheme_theory-en"

date: 2025-02-21
last_modified_at: 2025-02-21
weight: 10
translated_at: 2026-05-22T17:30:02+00:00
translation_source: kimi-cli
---
When dealing with families of varieties in algebraic geometry, we expect the fibers to vary "continuously" as the point in the base changes. However, mere continuity of the morphism is insufficient to capture this intuition. For example, the dimension of a fiber may suddenly jump at a point of the base, or the number of singularities may change, leading to discontinuous behavior. The notion that excludes such phenomena and ensures that the fibers maintain constant algebraic and geometric properties is precisely **flatness**. In this post, we first define flat modules in the context of commutative algebra, and then introduce flat morphisms between [§Schemes](/en/math/scheme_theory/schemes) and examine their geometric meaning, criteria, and examples.

## Flat Modules

For a module $$M$$ over a commutative ring $$A$$, being flat is an algebraically natural condition. The tensor product functor $$-\otimes_A M$$ between $$A$$-modules does not generally preserve exact sequences. That is, for an injective module homomorphism $$N' \hookrightarrow N$$, the map $$N' \otimes_A M \rightarrow N \otimes_A M$$ may fail to be injective. The essence of a flat module is to prevent this phenomenon where the tensor product "destroys" the relations between modules.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A module $$M$$ over a commutative ring $$A$$ is said to be **flat** if the tensor product functor $$-\otimes_A M$$ is an exact functor. That is, for any short exact sequence of $$A$$-modules

$$0 \longrightarrow N' \longrightarrow N \longrightarrow N'' \longrightarrow 0$$

the sequence

$$0 \longrightarrow N' \otimes_A M \longrightarrow N \otimes_A M \longrightarrow N'' \otimes_A M \longrightarrow 0$$

is also a short exact sequence.

</div>

Intuitively, a flat module $$M$$ preserves the linear relations already present in modules after taking the tensor product. For example, over $$A = \mathbb{Z}$$, the module $$\mathbb{Z}/2\mathbb{Z}$$ is not flat, because tensoring the injection $$\mathbb{Z} \xrightarrow{\times 2} \mathbb{Z}$$ with $$\mathbb{Z}/2\mathbb{Z}$$ yields

$$\mathbb{Z}/2\mathbb{Z} \xrightarrow{\times 2} \mathbb{Z}/2\mathbb{Z}$$

which becomes the zero map, violating injectivity. On the other hand, free modules are always flat. More generally, as shown in [\[Commutative Algebra\] §Flatness, ⁋Proposition 1](/en/math/commutative_algebra/flatness#prop1), finitely generated flat modules over a local ring are free.

## Definition of Flat Morphisms

Let us now pass to the context of schemes. To say that a morphism $$f: X \to Y$$ is flat means, broadly speaking, that the structure sheaf of $$X$$ has the structure of a flat module over the structure sheaf of $$Y$$.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> A morphism $$f: X \to Y$$ is said to be **flat** if for every $$x \in X$$, the local ring $$\mathcal{O}_{X,x}$$ is flat as an $$\mathcal{O}_{Y,f(x)}$$-module. Additionally, if the corresponding map of topological spaces is surjective, we say $$f$$ is **faithfully flat**.

</div>

Flatness is one of the most important algebraic properties of [§Morphisms of Schemes](/en/math/scheme_theory/morphism_of_schemes). In particular, the fibers of a flat morphism vary in a predictable manner as the base changes, which means that geometric properties remain constant along the family.

## Geometric Properties

The most geometrically intuitive feature of a flat morphism is that the [§Dimension (Schemes)](/en/math/scheme_theory/dimension) of its fibers is locally constant over the base. For a general morphism, Chevalley's theorem implies that the fiber dimension is upper semi-continuous, but given flatness, this semi-continuity becomes two-sided, so the fiber dimension becomes constant.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> If a flat morphism $$f: X \to Y$$ between locally Noetherian schemes is locally of finite type, then the function

$$y \longmapsto \dim f^{-1}(y)$$

is locally constant on $$Y$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

By Chevalley's theorem, for a morphism locally of finite type, $$y \mapsto \dim f^{-1}(y)$$ is upper semi-continuous. On the other hand, under the flatness assumption, it also holds that for any $$y \in Y$$, the dimension of $$f^{-1}(y)$$ does not drop at nearby points. This can be shown using the local criterion and dimension formula from [\[Commutative Algebra\] §Flatness and Localization, ⁋Theorem 1](/en/math/commutative_algebra/local_criterion_for_flatness#thm1). Since a function that is both upper and lower semi-continuous is locally constant, we obtain the conclusion.

</details>

Another important geometric property of flat morphisms is that they map open sets to open sets. In fact, a stronger result holds.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> A morphism $$f: X \to Y$$ that is flat, locally of finite type, and dominant is an open map. That is, for any open set $$U \subseteq X$$, the image $$f(U)$$ is an open set in $$Y$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

By Chevalley's theorem, the image of a morphism locally of finite type is a constructible set. In a Noetherian space, a constructible set is open if and only if it is closed under generization. If $$f$$ is flat, one can show that $$f(U)$$ is closed under generization by passing to a faithfully flat localization. Specifically, suppose $$y' \in \overline{\{y\}}$$ and $$y \in f(U)$$. By flatness, generizations in $$U$$ map up to $$f(U)$$, and therefore $$y' \in f(U)$$.

</details>

Flatness is a weaker condition than smoothness. In fact, smoothness is a relative version of regularity, which implies flatness.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> A smooth morphism is flat.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$f: X \to Y$$ be a smooth morphism. Smoothness is locally of finite presentation, and for any $$x \in X$$, the local ring $$\mathcal{O}_{X,x}$$ is a regular local ring of relative dimension $$d$$ over $$\mathcal{O}_{Y,f(x)}$$. That is, the maximal ideal $$\mathfrak{m}_x$$ is generated by $$d$$ elements $$f_1, \dots, f_d$$ together with $$\mathfrak{m}_{f(x)}$$, and $$\mathcal{O}_{X,x}/(f_1, \dots, f_d)$$ is flat over $$\mathcal{O}_{Y,f(x)}$$. From the definition of a regular local ring and the local criterion, one sees that $$\mathcal{O}_{X,x}$$ itself is a flat $$\mathcal{O}_{Y,f(x)}$$-module.

</details>

## Criteria for Flatness

Since verifying flatness directly can be difficult, several criteria have been developed. The most basic one is the local criterion for flatness.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> (Local Criterion for Flatness). Let $$(A, \mathfrak{m})$$ be a Noetherian local ring and $$M$$ a finitely generated $$A$$-module. If for some ideal $$I$$ of $$A$$, $$M/IM$$ is $$A/I$$-flat and additionally $$\operatorname{Tor}_1^A(M, A/I) = 0$$, then $$M$$ is $$A$$-flat. In particular, for $$I = \mathfrak{m}$$, if $$M/\mathfrak{m}M$$ is flat (i.e., free) over $$A/\mathfrak{m}$$ and $$\operatorname{Tor}_1^A(M, A/\mathfrak{m}) = 0$$, then $$M$$ is flat.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

To show that $$M$$ is $$A$$-flat for the ideal $$I$$, we show that $$\operatorname{Tor}_1^A(M, N) = 0$$ for every finitely generated $$A$$-module $$N$$. Using a filtration on $$N$$, it suffices inductively to check the case $$N = A/\mathfrak{p}$$ for a prime ideal $$\mathfrak{p}$$. The standard proof of the local criterion uses $$I$$-adic completion and the Artin-Rees lemma to show that the completion of $$M$$ is flat, and from this derives the flatness of $$M$$ itself. For details, see [\[Commutative Algebra\] §Flatness and Localization, ⁋Definition 4](/en/math/commutative_algebra/local_criterion_for_flatness#def4).

</details>

From the viewpoint of homological algebra, one can test flatness using [§Ext and Tor](/en/math/homological_algebra/ext_and_tor).

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> ($$\operatorname{Tor}$$ Criterion). An $$A$$-module $$M$$ is flat if and only if $$\operatorname{Tor}_1^A(M, A/I) = 0$$ for every ideal $$I \subseteq A$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

To show that $$-\otimes_A M$$ is an exact functor, it suffices to verify that whenever $$N' \hookrightarrow N$$ is injective, the map $$N' \otimes_A M \rightarrow N \otimes_A M$$ is injective. Under the assumption that $$\operatorname{Tor}_1^A(M, -)$$ vanishes for all cyclic modules $$A/I$$, the long exact sequence implies that this holds for any finitely generated module, and hence for any module. Therefore $$-\otimes_A M$$ is exact and $$M$$ is flat. The converse follows from the definition of a flat module: since $$-\otimes_A M$$ is an exact functor, the tensor product with any injection is injective, so $$\operatorname{Tor}_1^A(M, A/I) = 0$$ holds.

</details>

Finally, generic flatness is an important theorem stating that the flat locus forms a dense open subset of the base.

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8**</ins> (Generic Flatness). Let $$f: X \to Y$$ be a dominant morphism of finite type from an integral scheme $$X$$ to a Noetherian scheme $$Y$$. Then there exists a dense open set $$U \subseteq Y$$ such that the restriction $$f\rvert_{f^{-1}(U)}: f^{-1}(U) \to U$$ is flat.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

The problem can be reduced to the affine case. That is, set $$Y = \operatorname{Spec} A$$ and $$X = \operatorname{Spec} B$$, and assume that $$A$$ is a Noetherian domain, $$B$$ is an algebra of finite type over $$A$$, and $$A \to B$$ is injective. By the algebraic version of generic flatness, there exists a nonzero element $$f \in A$$ such that $$B_f$$ is $$A_f$$-flat. This means that $$f$$ is flat over $$D(f) \subseteq Y$$. The proof of this theorem proceeds by viewing $$B$$ as a finitely generated $$A$$-algebra, securing flatness over its fraction field, and then propagating this to a suitable localization.

</details>

## Examples

Let us look at typical examples of flat and non-flat morphisms.

<div class="example" markdown="1">

<ins id="ex9">**Example 9**</ins>

(1) An open immersion into an open subscheme is flat. This corresponds locally to localization, and localization is always flat.

(2) The projection $$\mathbb{A}_k^{n+m} \to \mathbb{A}_k^n$$ between affine spaces, i.e., $$k[x_1, \dots, x_n] \to k[x_1, \dots, x_n, y_1, \dots, y_m]$$, is flat. This follows immediately from the free module structure of the multivariate polynomial ring.

</div>

<div class="example" markdown="1">

<ins id="ex10">**Example 10**</ins> As a typical non-flat example, consider the family of cusps. Let $$k$$ be a field, and consider the family over $$\mathbb{A}_k^1 = \operatorname{Spec} k[t]$$

$$X = \operatorname{Spec} k[t, x, y]/(y^2 - x^3 - t) \longrightarrow \mathbb{A}_k^1.$$

At points where $$t \neq 0$$, the fiber is a non-singular elliptic curve (genus 1), but at $$t = 0$$ the fiber becomes the cusp $$y^2 = x^3$$ and is singular. This morphism is not flat at $$t = 0$$. Indeed, if we consider $$k[t, x, y]/(y^2 - x^3 - t)_{(t)}$$ over $$k[t]_{(t)}$$, this module has elements annihilated by $$t$$, so $$t$$-torsion exists and flatness fails. Intuitively, flatness is lost because the topological shape of the fiber changes suddenly.

Similarly, the family of nodes

$$\operatorname{Spec} k[t, x, y]/(xy - t) \longrightarrow \mathbb{A}_k^1$$

is also not flat at $$t = 0$$. When $$t \neq 0$$, the fiber is two intersecting lines, but at $$t = 0$$ it becomes the node $$xy = 0$$, taking on a topologically different form.

</div>

<div class="example" markdown="1">

<ins id="ex11">**Example 11**</ins> For a scheme $$X$$ over a field $$k$$ of positive characteristic $$p > 0$$, the **Frobenius morphism**

$$F: X \longrightarrow X$$

induces the $$p$$th power map $$a \mapsto a^p$$ on the structure sheaf. This morphism is generally not flat. By Kunz's theorem, $$X$$ is regular if and only if $$F$$ is flat. Therefore, if $$X$$ has a singularity, the Frobenius morphism is not flat. For example, $$X = \operatorname{Spec} k[x, y]/(xy)$$ is a node, and Frobenius is not flat on this scheme.

</div>

## Properties of Flat Morphisms

Flatness behaves well under basic operations.

<div class="proposition" markdown="1">

<ins id="prop12">**Proposition 12**</ins>

(1) Base change of a flat morphism ([§Fiber Products](/en/math/scheme_theory/fiber_products)) is flat. That is, if $$f: X \to Y$$ is flat and $$Z \to Y$$ is any morphism, then the projection $$X \times_Y Z \to Z$$ is flat.

(2) The composition of flat morphisms is flat. That is, if $$f: X \to Y$$ and $$g: Y \to Z$$ are both flat, then $$g \circ f: X \to Z$$ is also flat.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

(1) Base change takes the local form of a tensor product $$B \otimes_A C$$. If $$B$$ is $$A$$-flat, then $$-\otimes_A (B \otimes_A C) \cong (-\otimes_A B) \otimes_B (B \otimes_A C)$$, so exactness is preserved. Hence $$B \otimes_A C$$ is $$C$$-flat.

(2) For the composition, the pushforward of the structure sheaf for $$(g \circ f)^{-1}$$ is $$g_* f_* \mathcal{O}_X$$. Since $$f_* \mathcal{O}_X$$ is a flat $$\mathcal{O}_Y$$-module and flatness is preserved by $$g_*$$, the composite morphism is also flat. Algebraically, if $$A \to B$$ and $$B \to C$$ are both flat, then for any $$A$$-module $$N$$ we have $$N \otimes_A C \cong (N \otimes_A B) \otimes_B C$$, and exactness is preserved at each step, so $$-\otimes_A C$$ is also exact.

</details>

It is also important that the points where a morphism fails to be flat form a closed set.

<div class="proposition" markdown="1">

<ins id="prop13">**Proposition 13**</ins> For a morphism $$f: X \to Y$$ locally of finite presentation, the set of points of $$X$$ where $$f$$ is not flat is closed. Equivalently, the flat locus is an open subset of $$X$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

The problem is local, so we may assume $$Y = \operatorname{Spec} A$$ and $$X = \operatorname{Spec} B$$. Suppose $$B$$ is of finite presentation over $$A$$. Flatness is determined locally by the vanishing of $$\operatorname{Tor}$$ functors, and the vanishing of $$\operatorname{Tor}_1^A(B, -)$$ is described by the non-vanishing condition of certain determinants. Since such conditions are open conditions, the set of flat points is open. In the Noetherian case, this can be described more explicitly in terms of the heights of ideals.

</details>

---

**References**

**[Har]** R. Hartshorne, *Algebraic geometry*, Springer, 1977.

**[Stacks]** The Stacks Project Authors, *Stacks Project*, https://stacks.math.columbia.edu, Tag 00MD, Tag 00R3, Tag 01UA.

**[EGA]** A. Grothendieck, *Éléments de géométrie algébrique*, IHES, 1960–1967.

**[Mats]** H. Matsumura, *Commutative ring theory*, Cambridge University Press, 1986.
