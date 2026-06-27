---
title: "Flat Morphisms"
description: "We begin with the definition of flat modules in commutative algebra, then introduce flat morphisms between schemes, their geometric meaning, criteria, and examples. Flatness is a fundamental property that ensures the fibers of a morphism retain uniform algebraic and geometric properties over the base."
excerpt: "Flat morphisms in algebraic geometry"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/flat_morphisms
sidebar: 
    nav: "scheme_theory-en"

date: 2025-02-21
weight: 10
translated_at: 2026-06-27T00:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-27T00:30:02+00:00
---
When dealing with families of shapes in algebraic geometry, we expect the fibers to vary "continuously" as the base point changes. However, mere continuity of the map is insufficient to capture this intuition. For instance, the dimension of a fiber may jump abruptly at a point of the base, or the number of singular points may change discontinuously. The notion that excludes such phenomena and ensures that the fibers maintain constant algebraic and geometric properties is precisely **flatness**. In this post, we first define flat modules in the context of commutative algebra, then introduce flat morphisms between [§Schemes](/en/math/scheme_theory/schemes), and examine their geometric meaning, criteria, and examples.

## Flat Modules

That a module $$M$$ over a commutative ring $$A$$ is flat is an algebraically natural condition. The tensor product functor $$-\otimes_A M$$ between $$A$$-modules does not generally preserve exact sequences. That is, for an injective module homomorphism $$N' \hookrightarrow N$$, the map $$N' \otimes_A M \rightarrow N \otimes_A M$$ need not be injective. The essence of a flat module is to prevent this phenomenon, where the tensor product "destroys" the relations among modules.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A module $$M$$ over a commutative ring $$A$$ is called **flat** if the tensor product functor $$-\otimes_A M$$ is an exact functor. That is, for any short exact sequence of $$A$$-modules

$$0 \longrightarrow N' \longrightarrow N \longrightarrow N'' \longrightarrow 0$$

the sequence

$$0 \longrightarrow N' \otimes_A M \longrightarrow N \otimes_A M \longrightarrow N'' \otimes_A M \longrightarrow 0$$

is also a short exact sequence.

</div>

Intuitively, a flat module $$M$$ preserves the linear relations that existed among the original modules even after taking the tensor product. For example, over $$A = \mathbb{Z}$$, the module $$\mathbb{Z}/2\mathbb{Z}$$ is not flat, because tensoring the injective map $$\mathbb{Z} \xrightarrow{\times 2} \mathbb{Z}$$ with $$\mathbb{Z}/2\mathbb{Z}$$ yields

$$\mathbb{Z}/2\mathbb{Z} \xrightarrow{\times 2} \mathbb{Z}/2\mathbb{Z}$$

which becomes the zero map, so injectivity fails. On the other hand, free modules are always flat. Conversely, over a local ring, a finitely presented flat module is known to be free.

## Definition of Flat Morphisms

Let us now move to the context of schemes. That a morphism $$f: X \to Y$$ is flat means, roughly speaking, that the structure sheaf of $$X$$ carries the structure of a flat module over the structure sheaf of $$Y$$.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> A morphism $$f: X \to Y$$ is called **flat** if for every $$x \in X$$, the local ring $$\mathcal{O}_{X,x}$$ is flat as an $$\mathcal{O}_{Y,f(x)}$$-module. Additionally, if the corresponding map of topological spaces is surjective, we call it **faithfully flat**.

</div>

Flatness is one of the most important algebraic properties of a [§Morphism of Schemes](/en/math/scheme_theory/morphism_of_schemes). In particular, the fibers of a flat morphism vary in a predictable manner as the base changes, which means that geometric properties are preserved along the family.

## Geometric Properties

The most geometrically intuitive feature of a flat morphism is that the [§Dimension](/en/math/scheme_theory/dimension) of the fiber is locally constant on the base. For a general morphism, Chevalley's theorem implies that the fiber dimension is upper semi-continuous, but when flatness is given, this semi-continuity becomes two-sided, so the fiber dimension becomes constant.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> If a flat morphism $$f: X \to Y$$ between locally Noetherian schemes is locally of finite type, then the function

$$y \longmapsto \dim f^{-1}(y)$$

is locally constant on $$Y$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

By Chevalley's theorem, for a morphism locally of finite type, the map $$y \mapsto \dim f^{-1}(y)$$ is upper semi-continuous. On the other hand, under the flatness assumption, it also holds that for any $$y \in Y$$, the dimension of $$f^{-1}(y)$$ does not drop at nearby points. This can be shown using the local criterion and the dimension formula from [\[Commutative Algebra\] §Flatness and Localization, ⁋Theorem 1](/en/math/commutative_algebra/local_criterion_for_flatness#thm1). Since a function that is both upper and lower semi-continuous is locally constant, we obtain the conclusion.

</details>

Another important geometric property of flat morphisms is that they send open sets to open sets. In fact, a stronger result holds.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> A flat morphism $$f: X \to Y$$ that is locally of finite type and dominant is an open map. That is, for any open set $$U \subseteq X$$, the image $$f(U)$$ is an open set of $$Y$$.

</div>
<details class="proof" markdown="1">

By Chevalley's theorem, the image of a morphism locally of finite type is a constructible set. In a Noetherian space, a constructible set is open if and only if it is closed under generization. Since $$f$$ is flat, one can show via a faithfully flat localization that $$f(U)$$ is closed under generization. Specifically, suppose $$y' \in \overline{\{y\}}$$ and $$y \in f(U)$$. By flatness, a generization over $$U$$ lifts to a generization over $$f(U)$$, and therefore $$y' \in f(U)$$.

</details>

Flatness is a weaker condition than being a smooth morphism. In fact, smoothness is a relative version of regularity, and it implies flatness.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> A smooth morphism is flat.

</div>
<details class="proof" markdown="1">

Let $$f: X \to Y$$ be a smooth morphism. Smoothness is locally of finite presentation, and for any $$x \in X$$, the local ring $$\mathcal{O}_{X,x}$$ is a regular local ring over $$\mathcal{O}_{Y,f(x)}$$ of relative dimension $$d$$. That is, the maximal ideal $$\mathfrak{m}_x$$ is generated by $$d$$ elements $$f_1, \dots, f_d$$ and $$\mathfrak{m}_{f(x)}$$, and $$\mathcal{O}_{X,x}/(f_1, \dots, f_d)$$ is flat over $$\mathcal{O}_{Y,f(x)}$$. From the definition of a regular local ring and the local criterion, one sees that $$\mathcal{O}_{X,x}$$ itself is a flat $$\mathcal{O}_{Y,f(x)}$$-module.

</details>

## Criteria for Flatness

Since verifying flatness directly can be difficult, various criteria have been developed. The most basic one is the local criterion for flatness.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> (Local criterion for flatness). Let $$(A, \mathfrak{m})$$ be a Noetherian local ring and $$M$$ a finitely generated $$A$$-module. If for every ideal $$I$$ of $$A$$, $$M/IM$$ is flat over $$A/I$$, and moreover $$\operatorname{Tor}_1^A(M, A/I) = 0$$, then $$M$$ is flat over $$A$$. In particular, for $$I = \mathfrak{m}$$, if $$M/\mathfrak{m}M$$ is flat over $$A/\mathfrak{m}$$ (that is, free) and $$\operatorname{Tor}_1^A(M, A/\mathfrak{m}) = 0$$, then $$M$$ is flat.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

For an ideal $$I$$, to show that $$M$$ is flat over $$A$$, we show that $$\operatorname{Tor}_1^A(M, N) = 0$$ for every finitely generated $$A$$-module $$N$$. Using a filtration of $$N$$, it suffices inductively to check the case $$N = A/\mathfrak{p}$$ for a prime ideal $$\mathfrak{p}$$. The standard proof of the local criterion uses $$I$$-adic completion and the Artin–Rees lemma to show that the completion of $$M$$ is flat, and from this derives the flatness of $$M$$ itself. For details, see [\[Commutative Algebra\] §Flatness and Localization, ⁋Definition 4](/en/math/commutative_algebra/local_criterion_for_flatness#def4).

</details>

From the perspective of homological algebra, one can test flatness using [§Ext and Tor](/en/math/homological_algebra/ext_and_tor).

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> ($$\operatorname{Tor}$$ criterion). An $$A$$-module $$M$$ is flat if and only if $$\operatorname{Tor}_1^A(M, A/I) = 0$$ for every ideal $$I \subseteq A$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

To show that $$-\otimes_A M$$ is an exact functor, it suffices to check that when an injective map $$N' \hookrightarrow N$$ is given, the map $$N' \otimes_A M \rightarrow N \otimes_A M$$ is injective. Under the assumption that $$\operatorname{Tor}_1^A(M, -)$$ vanishes for all cyclic modules $$A/I$$, the long exact sequence implies that this holds for every finitely generated module, and indeed for every module. Therefore $$-\otimes_A M$$ is exact, and $$M$$ is flat. The converse follows from the definition of a flat module: since $$-\otimes_A M$$ is an exact functor, the tensor product with any injective map is injective, so $$\operatorname{Tor}_1^A(M, A/I) = 0$$ holds.

</details>

Finally, generic flatness is an important theorem stating that the flat locus forms a dense open subset of the base.

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8**</ins> (Generic flatness). Let $$f: X \to Y$$ be a dominant morphism of finite type from an integral scheme $$X$$ to a Noetherian scheme $$Y$$. Then there exists a dense open subset $$U$$ of $$Y$$ such that the restriction $$f\rvert_{f^{-1}(U)}: f^{-1}(U) \to U$$ is flat.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

The problem can be reduced to the affine case. That is, we set $$Y = \operatorname{Spec} A$$ and $$X = \operatorname{Spec} B$$, assume that $$A$$ is a Noetherian integral domain, that $$B$$ is an algebra of finite type over $$A$$, and that $$A \to B$$ is injective. By the algebraic version of generic flatness, there exists a nonzero element $$f \neq 0$$ in $$A$$ such that $$B_f$$ is flat over $$A_f$$. This means precisely that $$f$$ is flat over $$D(f) \subseteq Y$$. The proof of this theorem proceeds by viewing $$B$$ as a finitely generated $$A$$-algebra, securing flatness over its fraction field, and then propagating this to a suitable localization.

</details>

## Examples

Let us examine typical examples of flat and non-flat morphisms.

<div class="example" markdown="1">

<ins id="ex9">**Example 9**</ins>

(1) An open immersion is flat. This corresponds locally to localization, and localization is always flat.

(2) The projection morphism between affine spaces $$\mathbb{A}_k^{n+m} \to \mathbb{A}_k^n$$, that is, $$k[x_1, \dots, x_n] \to k[x_1, \dots, x_n, y_1, \dots, y_m]$$, is flat. This follows immediately from the free module structure of a multivariate polynomial ring.

</div>

<div class="example" markdown="1">

<ins id="ex10">**Example 10**</ins> As a representative non-flat example, consider a family of cusps. Let $$k$$ be a field, and consider the family over $$\mathbb{A}_k^1 = \operatorname{Spec} k[t]$$

$$X = \operatorname{Spec} k[t, x, y]/(y^2 - x^3 - t) \longrightarrow \mathbb{A}_k^1$$

At points with $$t \neq 0$$, the fiber is a non-singular elliptic curve (genus 1), but at $$t = 0$$, the fiber becomes the cusp $$y^2 = x^3$$ and is singular. This morphism is not flat at $$t = 0$$. In fact, considering $$k[t, x, y]/(y^2 - x^3 - t)_{(t)}$$ over $$k[t]_{(t)}$$, this module has elements annihilated by $$t$$, so $$t$$-torsion exists and flatness fails. Intuitively, flatness is lost because the topological type of the fiber changes abruptly.

Similarly, the family of nodes

$$\operatorname{Spec} k[t, x, y]/(xy - t) \longrightarrow \mathbb{A}_k^1$$

is also not flat at $$t = 0$$. When $$t \neq 0$$, the fiber is two intersecting lines, but at $$t = 0$$ it becomes the node $$xy = 0$$ and takes a topologically different form.

</div>

<div class="example" markdown="1">

<ins id="ex11">**Example 11**</ins> For a scheme $$X$$ over a field $$k$$ of positive characteristic $$p > 0$$, the **Frobenius morphism**

$$F: X \longrightarrow X$$

induces the $$p$$th power map $$a \mapsto a^p$$ on the structure sheaf. This morphism is generally not flat. By Kunz's theorem, $$X$$ being regular is equivalent to $$F$$ being flat. Therefore, if $$X$$ has a singular point, the Frobenius morphism is not flat. For example, $$X = \operatorname{Spec} k[x, y]/(xy)$$ is a node, and at this point the Frobenius is not flat.

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

(1) Base change is locally of the form $$B \otimes_A C$$. If $$B$$ is flat over $$A$$, then $$-\otimes_A (B \otimes_A C) \cong (-\otimes_A B) \otimes_B (B \otimes_A C)$$, so exactness is preserved. Therefore $$B \otimes_A C$$ is flat over $$C$$.

(2) For a composition, the pushforward of the structure sheaf with respect to $$(g \circ f)^{-1}$$ is $$g_\ast f_\ast \mathcal{O}_X$$. Since $$f_\ast \mathcal{O}_X$$ is a flat $$\mathcal{O}_Y$$-module and flatness is preserved by $$g_\ast$$, the composite morphism is also flat. Algebraically, if $$A \to B$$ and $$B \to C$$ are both flat, then for any $$A$$-module $$N$$ we have $$N \otimes_A C \cong (N \otimes_A B) \otimes_B C$$, and exactness is preserved at each step, so $$-\otimes_A C$$ is also exact.

</details>

It is also important that the set of points where a morphism fails to be flat forms a closed set.

<div class="proposition" markdown="1">

<ins id="prop13">**Proposition 13**</ins> For a morphism $$f: X \to Y$$ locally of finite presentation, the set of points of $$X$$ at which $$f$$ is not flat is a closed set. Equivalently, the flat locus is an open subset of $$X$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

The problem is local, so we may assume $$Y = \operatorname{Spec} A$$ and $$X = \operatorname{Spec} B$$. Let $$B$$ be of finite presentation over $$A$$. Flatness is checked locally by the vanishing of a $$\operatorname{Tor}$$ functor, and the vanishing of $$\operatorname{Tor}_1^A(B, -)$$ is described by the non-vanishing condition of certain determinants. Since such conditions are open conditions, the set of flat points is an open set. In the Noetherian case, this can be described more explicitly via the heights of ideals.

</details>

---

**References**

**[Har]** R. Hartshorne, *Algebraic geometry*, Springer, 1977.

**[Stacks]** The Stacks Project Authors, *Stacks Project*, https://stacks.math.columbia.edu, Tag 00MD, Tag 00R3, Tag 01UA.

**[EGA]** A. Grothendieck, *Éléments de géométrie algébrique*, IHES, 1960–1967.

**[Mats]** H. Matsumura, *Commutative ring theory*, Cambridge University Press, 1986.
