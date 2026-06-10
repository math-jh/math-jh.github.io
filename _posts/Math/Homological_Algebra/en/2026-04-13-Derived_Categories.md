---
title: "Derived Categories"
description: "We discuss the structure of the derived category, which is defined by formally inverting quasi-isomorphisms and identifying chain homotopic maps in the homotopy category."
excerpt: "Construction of derived categories via chain complexes and quasi-isomorphisms"

categories: [Math / Homological Algebra]
permalink: /en/math/homological_algebra/derived_categories
sidebar: 
    nav: "homological_algebra-en"

date: 2026-04-13
last_modified_at: 2026-04-13
weight: 8
translated_at: 2026-05-31T15:30:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-31T15:30:05+00:00
---
In [§Derived Functors](/en/math/homological_algebra/derived_functors) we saw how to address the issue when a functor is not exact. Specifically, given a left (resp. right) exact functor $$F$$, we chose an injective (resp. projective) resolution of an object $$A$$ and took the cohomology (resp. homology) of that resolution to define the right (resp. left) derived functor.

What deserves attention is that while the choice of injective or projective resolution does not affect the (co)homology, at the level of concrete chain complexes these choices are not natural. We now refine the framework conceptually. Specifically, we take chain complexes as our objects and regard quasi-isomorphic chain complexes as identical from the outset, thereby resolving this issue. That is, the category $$\Ch(\mathcal{A})$$ of chain complexes in $$\mathcal{A}$$, rather than the abelian category $$\mathcal{A}$$ itself, becomes our primary object of study.

## Definition of the Derived Category

However, $$\Ch(\mathcal{A})$$ itself is not our ultimate object of interest. As explained above, we must regard all quasi-isomorphisms in $$\Ch(\mathcal{A})$$ as identical, so we must also take the corresponding quotient. Moreover, since chain maps that are chain homotopic are already identified, we make the following definition.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> The *homotopy category* $$K(\mathcal{A})$$ of an abelian category $$\mathcal{A}$$ is the quotient category of $$\Ch(\mathcal{A})$$ obtained by identifying chain homotopic maps. That is, with respect to the chain homotopy relation $$\sim$$,

$$\Hom_{K(\mathcal{A})}(A^\bullet, B^\bullet) = \Hom_{\Ch(\mathcal{A})}(A^\bullet, B^\bullet) /{\sim}$$

.

</div>

We can verify that $$K(\mathcal{A})$$ is an additive category. On the other hand, we already observed in [§The Long Exact Sequence, ⁋Definition 4](/en/math/homological_algebra/long_exact_sequence#def4) that a quasi-isomorphism is generally not an isomorphism in $$K(\mathcal{A})$$. Therefore, in order to regard quasi-isomorphic chain complexes (up to chain homotopy) as the same, we must forcibly adjoin inverses for quasi-isomorphisms.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> The *derived category* $$D(\mathcal{A})$$ of an abelian category $$\mathcal{A}$$ is the Verdier quotient $$K(\mathcal{A})/S$$ of the homotopy category $$K(\mathcal{A})$$ by the class $$S$$ of quasi-isomorphisms.

</div>

We will not treat this definition with full rigor, but it is essentially the same construction as in [[Algebraic Structures] §Field of Fractions, ⁋Definition 2](/en/math/algebraic_structures/field_of_fractions#def2). The only difference is that the objects are non-commutative; with this caveat alone we can obtain the "localization" $$D(\mathcal{A})$$ of $$K(\mathcal{A})$$.

More concretely, when describing morphisms in $$D(\mathcal{A})$$ we often use roof diagrams. A morphism in $$D(\mathcal{A})$$ from $$X$$ to $$Y$$ is represented by a diagram

$$X\overset{s}{\longleftarrow} X'\overset{f}{\longrightarrow}Y$$

where $$s$$ is a quasi-isomorphism and $$f$$ is a chain map. In other words, inside $$D(\mathcal{A})$$, a map from $$X$$ to $$Y$$ is not an actual map but rather a chain map (precisely, up to chain homotopy) from some $$X'$$ in the quasi-isomorphism class of $$X$$ to $$Y$$. In this process we adjoin $$s^{-1}$$, which may not exist as an actual chain map, thereby producing the "localization" analogue described above.

From this perspective, we can also examine when two roofs define equivalent ones. In the localization setup this is expressed by an equivalence of the form

$$\frac{a}{b}=\frac{ca}{cb}$$

. Consider two roofs

$$X\overset{s}{\longleftarrow} A\overset{f}{\longrightarrow}Y,\qquad X\overset{t}{\longleftarrow} B\overset{g}{\longrightarrow}Y$$

. They are equivalent if there exists another object $$C$$ and a roof

$$A\overset{u}{\longleftarrow} C\overset{h}B$$

such that

$$su=th,\qquad fu=gh$$

hold and $$su=th$$ is a quasi-isomorphism. In a similar way one can define the composition of two roofs (on the level of roof diagrams this corresponds to finding a common roof), and thus one can fully understand the morphisms in $$D(\mathcal{A})$$.

To see how this language furnishes a good framework, let an object $$A$$ of $$\mathcal{A}$$ be given. Then we consider the chain complex

$$A[0]:\qquad \cdots\rightarrow 0\rightarrow A\rightarrow 0\rightarrow \cdots$$

. What we know is that an injective resolution or a projective resolution of $$A$$ is quasi-isomorphic to $$A[0]$$; at the level of the derived category, resolutions of $$A$$ become nothing but $$A$$ itself.

On the other hand, since injective and projective resolutions point in opposite directions, we can refine $$D(\mathcal{A})$$ further.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> We define subcategories of the derived category $$D(\mathcal{A})$$.

1. Complexes for which $$H^n(A^\bullet)=0$$ holds for all sufficiently small $$n$$ are called *bounded below*, and the full subcategory of $$D(\mathcal{A})$$ consisting of these is denoted $$D^+(\mathcal{A})$$.
2. Complexes for which $$H^n(A^\bullet)=0$$ holds for all sufficiently large $$n$$ are called *bounded above*, and the full subcategory of $$D(\mathcal{A})$$ consisting of these is denoted $$D^-(\mathcal{A})$$.
3. Complexes that are both bounded below and bounded above are called *bounded*, and the full subcategory of $$D(\mathcal{A})$$ consisting of these is denoted $$D^b(\mathcal{A})$$.

</div>

The range of indices in which a given complex has non-zero (co)homology is often called its *amplitude*. As mentioned above, $$D^+(\mathcal{A})$$ is the natural setting for working with injective resolutions, and $$D^-(\mathcal{A})$$ is natural for projective resolutions. In most applications the bounded derived category $$D^b(\mathcal{A})$$ is the main stage.

We also formally make the following definition.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> The *shift functor* $$[n]: D(\mathcal{A}) \rightarrow D(\mathcal{A})$$ on $$D(\mathcal{A})$$ shifts a complex $$A^\bullet$$ by $$n$$ places. Specifically, $$(A[n])^i = A^{i+n}$$, and the differential is defined by $$(d_{A[n]})^i = (-1)^n d_A^{i+n}$$.

</div>

The sign convention for the differential has already been explained after [§Homology, ⁋Definition 5](/en/math/homological_algebra/homology#def5). However, the sign change does not affect the (co)homology at all, so for example we have

$$H^i(A[n]) = H^{i+n}(A)$$

. As a concrete example, when we view an object $$A$$ of an abelian category as $$A[0]$$, the complex $$A[n]$$ is the one with $$A$$ in degree $$-n$$ and $$0$$ elsewhere; hence $$H^{-n}(A[n]) = A$$ and the cohomology in all other degrees is $$0$$.

## Derived Functors

We mentioned earlier that the derived category helps us view derived functors correctly. To do so, we must introduce the notion of resolution at the level of complexes.

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> A complex $$P \in K(\mathcal{A})$$ is called *$$K$$-projective* if for every quasi-isomorphism $$s: A \rightarrow B$$ in $$K(\mathcal{A})$$, the induced map

$$\Hom(s, P):\Hom_{K(\mathcal{A})}(B, P)\rightarrow\Hom_{K(\mathcal{A})}(A, P)$$

is an isomorphism.

</div>

In other words, $$P$$ is a complex that makes the Hom functor $$\Hom(-, P)$$ invariant under quasi-isomorphisms in $$K(\mathcal{A})$$; it is obvious that only such objects descend well to the derived category. Of course we must also define the following.

<div class="definition" markdown="1">

<ins id="def6">**Definition 6**</ins> A complex $$I \in K(\mathcal{A})$$ is called *$$K$$-injective* if for every quasi-isomorphism $$s : A \rightarrow B$$, the induced map

$$\Hom_{K(\mathcal{A})}(I, A) \xrightarrow{s_\ast} \Hom_{K(\mathcal{A})}(I, B)$$

is an isomorphism.

</div>

In general, a resolution of an object $$A$$ becomes a $$K$$-resolution of $$A[0]$$. Moreover, one can easily verify the following proposition.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> The following hold.

1. A chain complex whose terms are injective and which is bounded below is $$K$$-injective.
2. A chain complex whose terms are projective and which is bounded above is $$K$$-projective.

</div>

More generally, the homotopy category of any abelian category with enough injectives has enough $$K$$-injective resolutions, and the same holds for the projective case. We are now ready to make the following definition.

<div class="definition" markdown="1">

<ins id="def8">**Definition 8**</ins> Let an additive functor $$F : \mathcal{A} \rightarrow \mathcal{B}$$ be given.

1. Suppose $$F$$ is left exact and $$\mathcal{A}$$ has enough injectives. The *right derived functor* of $$A^\bullet \in D^+(\mathcal{A})$$ is defined by $$R F(A^\bullet) = F(I^\bullet)$$, where $$A^\bullet \rightarrow I^\bullet$$ is a $$K$$-injective resolution.
2. Suppose $$F$$ is right exact and $$\mathcal{A}$$ has enough projectives. The *left derived functor* of $$A^\bullet \in D^-(\mathcal{A})$$ is defined by $$L F(A^\bullet) = F(P_\bullet)$$, where $$P_\bullet \rightarrow A^\bullet$$ is a $$K$$-projective resolution.

</div>

We required $$A^\bullet$$ to lie in $$D^+(\mathcal{A})$$ or $$D^-(\mathcal{A})$$ in order to use the existence of $$K$$-resolutions, but if a $$K$$-resolution is given explicitly there is no need to assume this. However, in most cases that arise in practice, $$A^\bullet$$ is given with the desired boundedness.

In particular, viewing $$A \in \mathcal{A}$$ as $$A[0] \in D(\mathcal{A})$$,

$$H^i(R F(A[0])) = (R^i F)(A)$$

holds, so we see that $$RF$$ correctly recovers the classical right derived functors. More intuitively, all the information of these right derived functors is contained not in the individual $$R^iF$$ but in the single derived functor $$RF$$; cohomology is merely the tool that brings it back to the "classical" world. Similarly, it is clear that $$H_i(L F(A[0])) = (L_i F)(A)$$.

<div class="proposition" markdown="1">

<ins id="prop9">**Proposition 9**</ins> $$R F$$ and $$L F$$ are functors on the derived category; that is, they send quasi-isomorphisms to quasi-isomorphisms.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let a quasi-isomorphism $$s : A^\bullet \rightarrow B^\bullet$$ be given, and let $$A^\bullet \rightarrow I^\bullet$$ and $$B^\bullet \rightarrow J^\bullet$$ be $$K$$-injective resolutions. By the lifting property of $$K$$-injective resolutions ([Definition 6](#def6)), the quasi-isomorphism $$s$$ extends uniquely (up to homotopy) to a map $$\tilde{s} : I^\bullet \rightarrow J^\bullet$$. Thus we obtain $$F(\tilde{s}) : F(I^\bullet) \rightarrow F(J^\bullet)$$. Since we have applied $$F$$ over a $$K$$-injective resolution, $$F(\tilde{s})$$ is a quasi-isomorphism, and hence $$R F(A^\bullet) \cong R F(B^\bullet)$$ in $$D(\mathcal{B})$$. The argument for the left derived functor is similar.

</details>

As a concrete example, the Hom functor $$\Hom(-, B)$$ on $$\mathcal{A}$$ is a contravariant left exact functor; deriving it yields the derived Hom $$R\Hom$$ at the complex level, and the cohomology of $$R\Hom(A, B)$$ coincides with $$\Ext^i(A, B)$$.

<div class="proposition" markdown="1">

<ins id="prop10">**Proposition 10**</ins> Let $$\mathcal{A}$$ be an abelian category with enough injectives. Then for all $$A, B \in \mathcal{A}$$,

$$H^{i}(R\Hom(A, B)) \cong \Ext^i(A, B)$$

holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let us define $$R\Hom(A, B)$$ precisely. View $$A$$ as $$A[0] \in D(\mathcal{A})$$ and choose a projective resolution $$P_\bullet \rightarrow A$$. By [Proposition 7](#prop7), $$P_\bullet$$ is a $$K$$-projective complex, so

$$R\Hom(A, B) = \Hom(P_\bullet, B)$$

is the definition. Here the right-hand side denotes the complex $$\Hom(P_\bullet, B)$$. Since $$P_\bullet \rightarrow A$$ is a projective resolution, the definition in [§Ext and Tor](/en/math/homological_algebra/ext_and_tor) gives $$H^i(\Hom(P_\bullet, B)) = \Ext^i(A, B)$$.

</details>

Similarly, one can define the left derived functor of the tensor product as $$L(A \otimes B) = A \otimes^L B$$, and $$\Tor_i(A, B) = H^{-i}(A \otimes^L B)$$ holds.

## Triangulated Categories

The derived category $$D(\mathcal{A})$$ is not merely a category; it carries the structure of a *triangulated category*. This structure plays the role in the derived category that short exact sequences play in an abelian category.

<div class="definition" markdown="1">

<ins id="def11">**Definition 11**</ins> A *triangulated category* is an additive category $$(\mathcal{T}, [1], \mathcal{S})$$ equipped with the following structure.

1. A *shift functor* $$[1] : \mathcal{T} \rightarrow \mathcal{T}$$, where $$[0] = \id$$ and $$[n+1] = [1] \circ [n]$$.
2. A collection $$\mathcal{S}$$ of *distinguished triangles*. Each distinguished triangle has the form

$$A \overset{f}{\rightarrow} B \overset{g}{\rightarrow} C \overset{h}{\rightarrow} A[1]$$

. This collection satisfies the following axioms.
- (TR1) For every morphism $$f : A \rightarrow B$$ there exists a distinguished triangle $$A \rightarrow B \rightarrow C \rightarrow A[1]$$. Also, $$A \overset{\id}{\rightarrow} A \rightarrow 0 \rightarrow A[1]$$ is a distinguished triangle.
- (TR2) If $$A \rightarrow B \rightarrow C \rightarrow A[1]$$ is a distinguished triangle, then so is $$B \rightarrow C \rightarrow A[1] \rightarrow B[1]$$.
- (TR3) Given two distinguished triangles, if maps $$(u, v)$$ make the diagram commute, then there exists a map $$w$$ completing the morphism of triangles.
- (TR4) Octahedral axiom: Given a composition $$B \overset{g}{\longrightarrow} C \overset{h}{\longrightarrow} D$$, there exist three distinguished triangles forming the associated octahedron.

</div>

The intuition behind a distinguished triangle is that it is the "derived version" of a short exact sequence. In an abelian category, given a short exact sequence $$0 \rightarrow A' \overset{f}{\longrightarrow} A \overset{g}{\longrightarrow} A'' \rightarrow 0$$, we can view $$f$$ as a map of complexes $$A'[0] \rightarrow A[0]$$, and then the mapping cone $$C(f)$$ is quasi-isomorphic to $$A''[0]$$. ([§The Long Exact Sequence, ⁋Definition 8](/en/math/homological_algebra/long_exact_sequence#def8)) In other words, a short exact sequence becomes a distinguished triangle in the derived category

$$A'[0] \overset{f}{\rightarrow} A[0] \rightarrow A''[0] \rightarrow A'[1]$$

. For a general map $$f$$, the extent to which $$f$$ deviates from an isomorphism is measured by the cohomology of $$C(f)$$, and the cohomology long exact sequence arises naturally.

In the derived category $$D(\mathcal{A})$$, distinguished triangles are triangles obtained from a map of complexes $$f$$ and its mapping cone $$C(f)$$: 

$$A \overset{f}{\rightarrow} B \overset{g}{\rightarrow} C(f) \overset{h}{\rightarrow} A[1]$$

. Here $$g : B^i \rightarrow C(f)^i = B^i \oplus A^{i+1}$$ is given by $$b \mapsto (b, 0)$$, and $$h : C(f)^i \rightarrow A[1]^i = A^{i+1}$$ is given by $$(b, a) \mapsto a$$.

<div class="proposition" markdown="1">

<ins id="prop12">**Proposition 12**</ins> $$R F : D^+(\mathcal{A}) \rightarrow D^+(\mathcal{B})$$ is a triangulated functor; that is, given a distinguished triangle

$$A \rightarrow B \rightarrow C \rightarrow A[1]$$

,

$$R F(A) \rightarrow R F(B) \rightarrow R F(C) \rightarrow R F(A)[1]$$

is also a distinguished triangle.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

View $$A \rightarrow B$$ as a map and let $$I_A^\bullet$$ and $$I_B^\bullet$$ be their $$K$$-injective resolutions. By the lifting property of $$K$$-injective resolutions, the map $$A \rightarrow B$$ extends to $$I_A^\bullet \rightarrow I_B^\bullet$$. Taking a $$K$$-injective resolution $$I_C^\bullet$$ of $$C = C(f)$$, the sequence $$I_A^\bullet \rightarrow I_B^\bullet \rightarrow I_C^\bullet \rightarrow I_A^\bullet[1]$$ is a distinguished triangle among $$K$$-injective complexes, and applying $$F$$ and viewing the result in $$D(\mathcal{B})$$ yields the desired distinguished triangle. Since bounded below $$K$$-injective complexes form a triangulated subcategory of $$K(\mathcal{A})$$, the mapping cone is also $$K$$-injective and the diagram commutes.

</details>

## Derived Adjunction

In category theory, adjunction is one of the most important relationships between two functors. Adjunction also holds in the derived category, and is called *derived adjunction*.

Derived adjunction $$L F \dashv R G$$ lifts an ordinary adjoint relationship to the derived category; even when $$F$$ and $$G$$ are not exact, the correctly computed results via resolutions still form an adjoint pair. Naively applying $$F$$ or $$G$$ may break exactness and produce incorrect homology, but using the derived version resolves this problem while preserving the original adjoint structure.

<div class="proposition" markdown="1">

<ins id="prop13">**Proposition 13**</ins> Let additive functors $$F : \mathcal{A} \rightarrow \mathcal{B}$$ (right exact) and $$G : \mathcal{B} \rightarrow \mathcal{A}$$ (left exact) between abelian categories $$\mathcal{A}, \mathcal{B}$$ form an adjoint pair $$F \dashv G$$. Then in the derived category

$$L F : D^-(\mathcal{A}) \rightarrow D^-(\mathcal{B}), \qquad R G : D^+(\mathcal{B}) \rightarrow D^+(\mathcal{A})$$

form an adjoint pair $$L F \dashv R G$$. That is, for all $$A^\bullet \in D^-(\mathcal{A})$$ and $$B^\bullet \in D^+(\mathcal{B})$$,

$$\Hom_{D(\mathcal{B})}(L F(A^\bullet), B^\bullet) \cong \Hom_{D(\mathcal{A})}(A^\bullet, R G(B^\bullet))$$

holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Choose a $$K$$-projective resolution $$P_\bullet$$ of $$A^\bullet$$ and a $$K$$-injective resolution $$I^\bullet$$ of $$B^\bullet$$. Since $$P_\bullet$$ is $$K$$-projective, in computing $$\Hom_{D(\mathcal{B})}(F(P_\bullet), I^\bullet)$$ we can replace $$F(P_\bullet)$$ by a resolution. By the original adjunction $$F \dashv G$$, at the complex level we have

$$\Hom_{\Ch(\mathcal{B})}(F(P_\bullet), I^\bullet) \cong \Hom_{\Ch(\mathcal{A})}(P_\bullet, G(I^\bullet))$$

. This isomorphism is obtained by assembling the degree-wise adjunctions $$\Hom_\mathcal{B}(F(P^n), I^m) \cong \Hom_\mathcal{A}(P^n, G(I^m))$$ to the complex level. Since $$P_\bullet$$ is $$K$$-projective and $$I^\bullet$$ is $$K$$-injective, the left-hand side reduces to $$\Hom_{K(\mathcal{B})}(F(P_\bullet), I^\bullet) = \Hom_{D(\mathcal{B})}(L F(A^\bullet), B^\bullet)$$, and the right-hand side reduces to $$\Hom_{K(\mathcal{A})}(P_\bullet, G(I^\bullet)) = \Hom_{D(\mathcal{A})}(A^\bullet, R G(B^\bullet))$$.

</details>

The most representative example is the adjunction between tensor product and Hom. The tensor-Hom adjunction on an abelian category $$\mathcal{A}$$ seen in [[Multilinear Algebra] §Hom and Tensor Products](/en/math/multilinear_algebra/hom_and_tensor)

$$\Hom(A \otimes B, C) \cong \Hom(A, \Hom(B, C))$$

is one where we might wish to obtain an isomorphism of the same form for complexes $$X, Y, Z$$ in the derived category as well. However, the raw functors $$-\otimes B$$ and $$\Hom(B,-)$$ do not preserve quasi-isomorphisms, so this adjunction does not descend naively to the derived category. We verified earlier that when defining derived functors one must take a projective or injective resolution in order to descend well from $$K(\mathcal{A})$$ to $$D(\mathcal{A})$$; this is precisely because $$-\otimes B$$ is right exact and $$\Hom(B,-)$$ is left exact. Since localization with respect to quasi-isomorphisms does not automatically preserve the classical adjoint, a derived version that compensates for this lack of exactness is needed.

To see this concretely, consider $$R = \mathbb{Z}$$ and $$M = \mathbb{Z}/n\mathbb{Z}$$. Since $$M$$ is not flat, tensoring is not exact. Applying $$-\otimes M$$ to $$0 \to \mathbb{Z} \xrightarrow{\times n} \mathbb{Z} \to \mathbb{Z}/n\mathbb{Z} \to 0$$ breaks exactness; specifically, since $$\Tor_1^\mathbb{Z}(\mathbb{Z}/n\mathbb{Z}, \mathbb{Z}/n\mathbb{Z}) \cong \mathbb{Z}/n\mathbb{Z}$$ exists, the naive adjunction does not work as expected. ([§Ext and Tor](/en/math/homological_algebra/ext_and_tor))

To resolve this exactness failure we construct $$\otimes^L$$ and $$R\Hom$$ using projective resolutions, and by [Proposition 13](#prop13) the adjunction is restored. Specifically, $$A \otimes^L B$$ is obtained by applying $$-\otimes B$$ to a projective resolution of $$A$$, and $$R\Hom(B, C)$$ is obtained by applying $$\Hom(-, C)$$ to a projective resolution of $$B$$. This yields

$$\Hom_{D(\mathcal{A})}(A \otimes^L B, C) \cong \Hom_{D(\mathcal{A})}(A, R\Hom(B, C))$$

. In the process of taking a projective resolution, the $$\Tor$$ information lost by $$-\otimes B$$ and the $$\Ext$$ information lost by $$\Hom(B,-)$$ are preserved in the higher degrees of the complex, and one can verify that the two sides agree by computing chain maps.

In summary, the classical adjunction in an abelian category exists at the underived level, but it does not automatically survive localization with respect to quasi-isomorphisms. Because $$-\otimes B$$ is right exact and $$\Hom(B,-)$$ is left exact, quasi-isomorphisms are not preserved, and consequently the naive adjunction breaks. This failure of exactness is resolved by constructing $$\otimes^L$$ and $$R\Hom$$ via resolutions, and the derived adjunction guaranteed by [Proposition 13](#prop13) precisely replaces the classical adjunction.

---

**References**

**[GM]** S. I. Gelfand, Y. I. Manin, *Methods of homological algebra*, Springer, 2003.  
**[Ver]** J.-L. Verdier, *Des catégories dérivées des catégories abéliennes*, Astérisque **239** (1996).  
**[Wei]** C. A. Weibel, *An introduction to homological algebra*, Cambridge University Press, 1994.
