---
title: "Intersection Product"
description: "This post covers the definition and properties of the Chow ring. It defines the intersection product on Chow groups and explores concrete calculation examples through intersection multiplicities and the Tor formula."
excerpt: "The intersection product on Chow groups"

categories: [Math / Algebraic Varieties]
permalink: /en/math/algebraic_varieties/intersection_product
sidebar: 
    nav: "algebraic_varieties-en"

date: 2026-05-11
weight: 19
translated_at: 2026-05-30T06:30:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-30T06:30:04+00:00
---
In [§Chow Groups](/en/math/algebraic_varieties/chow_groups) we defined the Chow group $$\CH^\ast(X)$$. At the end of that post we claimed that one can define an intersection product on it to give it a ring structure; in this post we define this product and examine its properties.

The following definition shows what the intersection of two varieties $$V, W$$ near a point $$p$$ is. By definition this is a local matter at $$p$$, so it suffices to pick an affine chart and take the ambient space to be $$\mathbb{A}^n$$.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> The *intersection multiplicity* $$i_p(V, W)$$ of two varieties $$V, W$$ at a point $$p$$ in affine space $$\mathbb{A}^n$$ is defined by the formula

$$i_p(V, W) = \dim_{\mathbb{K}} \mathcal{O}_{\mathbb{A}^n, p} / (I(V) + I(W))$$

</div>

By definition, near $$p$$ the varieties $$V$$ and $$W$$ are cut out by the elements of $$I(V)$$ and $$I(W)$$ respectively. Thus for $$p$$ to lie on both subvarieties it must be a common zero of all elements of both ideals, which leads us to consider the ideal sum $$I(V)+I(W)$$. In general, if $$V$$ and $$W$$ are too small relative to the ambient space they will not meet, so the above formula is not well defined. Hence we only use it when $$\dim V+\dim W=n$$. In general, when two arbitrary subvarieties meet, the expected dimension of their intersection is $$\dim V + \dim W - n$$, and this can be a point only if $$\dim V+\dim W=n$$.

In general this definition applies in the local complete intersection case, and in singular situations the following *Tor formula*

$$i_p(V, W) = \sum_{i \ge 0} (-1)^i \dim_{\mathbb{K}} \Tor_i^{R}\bigl(R/I(V),\ R/I(W)\bigr)$$

gives the definition. The preceding formula corresponds to the $$i = 0$$ term. In this post we only consider simple cases, so [Definition 1](#def1) above suffices.

<div class="example" markdown="1">

<ins id="ex2">**Example 2**</ins> In $$\mathbb{A}^2$$, $$V=\{ \y = 0\}$$ and $$W=\{\y = \x^2\}$$ meet at the origin. The ideals defining the two curves are $$I(V) = (\y)$$, $$I(W) = (\y - \x^2)$$. Computing the quotient of the local ring at the origin according to the definition, we obtain

$$\mathcal{O}_{\mathbb{A}^2, 0} / (\y, \y - \x^2) = \mathcal{O}_{\mathbb{A}^2, 0} / (\y, \x^2)$$

and this quotient is a 2-dimensional $$\mathbb{K}$$-vector space with basis $$\{1, \x\}$$. Hence $$i_0(V, W) = 2$$. This agrees with the fact that the curve $$W$$ is tangent to $$V$$ at $$\x=0$$ with order 2. More generally, for $$V=\{ \y = 0\}$$ and $$W=\{\y = \x^n\}$$ we have $$i_0(V, W) = n$$.

</div>

The above is an example of two 1-dimensional subvarieties meeting in dimension 2, which we already introduced briefly in [§The Riemann–Roch Theorem for Surfaces, ⁋Definition 1](/en/math/algebraic_varieties/riemann_roch_surfaces#def1). In that post we introduced the notion of a transversal intersection, so let us define it formally.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> Two varieties $$V, W \subseteq \mathbb{A}^n$$ *intersect transversely* at a point $$p \in V \cap W$$ if the sum of their tangent spaces is the whole space.

</div>

Then the following two propositions are natural generalizations of [§The Riemann–Roch Theorem for Surfaces, ⁋Proposition 2](/en/math/algebraic_varieties/riemann_roch_surfaces#prop2).

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> Intersection multiplicity satisfies the following properties.

1. For any $$p$$ and $$V, W$$, we always have $$0 \leq i_p(V,W) < \infty$$, and $$i_p(V,W)=0$$ holds precisely when $$p \notin V \cap W$$.
2. $$V$$ and $$W$$ intersect transversely at $$p$$ if and only if $$i_p(V,W)=1$$.
3. $$i_p$$ satisfies all the conditions of [§The Riemann–Roch Theorem for Surfaces, ⁋Proposition 2](/en/math/algebraic_varieties/riemann_roch_surfaces#prop2).

</div>

## Definition of the Intersection Product

Strictly speaking, the definitions given so far do not yet allow us to use all the properties of the intersection product on the Chow group. For example, in 3-dimensional space two planes generally meet in a line, but we have only treated the case where the intersection of two subspaces is 0-dimensional, so we cannot account for this. Therefore we first make the following definition.

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> For two subvarieties $$V, W$$ of a variety $$X$$, if the equality

$$\codim(V \cap W) = \codim V + \codim W$$

holds, then we say that $$V$$ and $$W$$ *intersect properly*.

</div>

In particular, [Definition 1](#def1) is the special case where $$\codim(V \cap W) = n$$. Now, if the above equality holds for every component of $$V \cap W$$, then we can use it to define

$$V \cdot W = \sum_{T \subseteq V \cap W} i_T(V, W) \, [T]$$

Here $$i_T(V, W)$$ is the intersection multiplicity along the component $$T$$, obtained by naturally extending the pointwise multiplicity of [Definition 1](#def1) to the component $$T$$. If $$T$$ is a point $$p$$, then $$i_T(V, W) = i_p(V, W)$$; in general it is the number measuring how the two varieties meet at a general point of $$T$$, and can be defined rigorously as the intersection multiplicity at the generic point. The following proposition lifts the properties of intersection multiplicity to the intersection product.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> For two cycles $$Z, W$$ of codimensions $$k$$ and $$l$$ on a smooth irreducible variety $$X$$, the *intersection product*

$$Z \cdot W \in \CH^{k+l}(X)$$

is well defined. Moreover, it satisfies the following properties:

1. *Symmetry.* $$Z \cdot W = W \cdot Z$$.
2. *Bilinearity.* $$(aZ_1 + bZ_2) \cdot W = a(Z_1 \cdot W) + b(Z_2 \cdot W)$$.
3. *Associativity.* $$(Z_1 \cdot Z_2) \cdot Z_3 = Z_1 \cdot (Z_2 \cdot Z_3)$$.

</div>

Then the following definition has been anticipated since the previous post.

<div class="definition" markdown="1">

<ins id="def7">**Definition 7**</ins> The intersection product makes $$\CH^\ast(X) = \bigoplus_k \CH^k(X)$$ into a *graded ring*. This is called the *Chow ring*.

</div>

## Moving Lemma

Now our only problem is that, given two arbitrary classes, even if they satisfy the dimension condition we do not know whether the two cycles actually meet nicely. For example, in the present state we cannot define the self-intersection of a given class. To remedy this, we must more generally be able to move one of two arbitrary cycles within its rational equivalence class so that it intersects $$W$$ properly. The theorem guaranteeing this is the following *moving lemma*.

<div class="proposition" markdown="1">

<ins id="lem8">**Lemma 8 (Moving Lemma)**</ins> For a smooth quasi-projective variety $$X$$, a cycle $$Z \in \CH^k(X)$$, and any cycle $$W \in \CH^l(X)$$, there exists a cycle $$Z'$$ such that $$Z' \sim_{\text{rat}} Z$$ and $$Z'$$ intersects $$W$$ properly.

</div>

The key idea is as follows. For each irreducible component $$V_i$$ of $$Z$$, cut it by a sufficiently "general" hypersurface $$H_i$$ containing $$V_i$$, and take a cycle of the form $$V_i \cap H_1 \cap \cdots \cap H_s$$. Here "general" means that $$H_i$$ is chosen so as to meet $$W$$ in generic position; then the dimension drops appropriately to achieve a proper intersection. As we saw in [§Linear Systems, ⁋Definition 5](/en/math/algebraic_varieties/linear_systems#def5), using a basepoint-free linear system one can realize such a "general" move by a regular map, and the heart of the proof is to show that this process preserves rational equivalence.

Then, using the above lemma to move $$Z$$ to $$Z'$$, we define the intersection by

$$Z \cdot W := Z' \cdot W = \sum_{T \subset Z' \cap W} i_T(Z', W) [T]$$

## Deformation to the Normal Cone

The moving lemma realizes our intuition that, given two classes, one can perturb them to compute the intersection. However, this approach depends on the hypothesis of quasi-projectivity, and to extend it to the general setting one must use the *deformation to the normal cone*.

The key observation is as follows. First, recall that in [§Tangent Spaces and Smoothness, ⁋Definition 13](/en/math/algebraic_varieties/tangent_spaces_and_smoothness#def13) we defined the tangent cone. This was a tool for understanding the local structure at a singular point, and generalizing it we can define the *normal cone* $$C_{Y/X}$$ of $$Y$$ inside $$X$$ for a closed embedding $$i: Y \hookrightarrow X$$. If $$X$$ is smooth along $$Y$$ then the normal cone becomes the normal bundle $$N_{Y/X}$$, but in general it has a cone structure.

<div class="proposition" markdown="1">

<ins id="prop9">**Proposition 9 (Deformation to the Normal Cone)**</ins> For a closed embedding $$i: Y \hookrightarrow X$$, one can construct a family $$M \to \mathbb{A}^1$$ parametrized by $$\mathbb{A}^1$$. Specifically, the fiber $$M_t$$ for $$t \neq 0$$ is $$X$$ itself, and the fiber $$M_0$$ at $$t = 0$$ is the normal cone $$C_{Y/X}$$. The existence of this family reduces the well-definedness of the intersection product to the compatibility of pushforward and pullback for this family.

</div>

<details class="proof" markdown="1">
<summary>Proof (Sketch)</summary>

The construction uses a blow-up. First blow up $$X \times \mathbb{A}^1$$ along $$Y \times \{0\}$$ to obtain $$\widetilde{M} = \Bl_{Y \times \{0\}}(X \times \mathbb{A}^1)$$, and then remove the proper transform of $$X \times \{0\}$$ to define $$M = \widetilde{M} \setminus \widetilde{X \times \{0\}}$$. The exceptional divisor of this blow-up is $$\mathbb{P}(C_{Y/X} \oplus \mathcal{O}_Y)$$, and removing the proper transform leaves exactly the normal cone $$C_{Y/X}$$ in the $$t=0$$ fiber. For $$t \neq 0$$ the blow-up is an isomorphism, so the fiber is just $$X$$. Thus $$M \to \mathbb{A}^1$$ provides a deformation connecting $$X$$ at $$t=1$$ to $$C_{Y/X}$$ at $$t=0$$. One can define a specialization map $$\sigma: \CH^\ast(X) \to \CH^\ast(C_{Y/X})$$ on Chow groups, and when the normal cone has a vector bundle structure (i.e. when the embedding is regular) the Thom isomorphism gives $$\CH^\ast(C_{Y/X}) \cong \CH^\ast(Y)$$, establishing the well-definedness of the intersection product.

</details>

The idea of this method is to deform $$X$$ continuously and contract it onto the normal cone of $$Y$$. Geometrically, at $$t=1$$ we see the original space $$X$$, and as $$t$$ goes to $$0$$ the space $$X$$ is "flattened out" more and more along $$Y$$, eventually becoming the normal cone opened up along $$Y$$ at $$t=0$$. Just as the blow-up in [§Rational Maps, ⁋Example 12](/en/math/algebraic_varieties/rational_maps#ex12) was a deformation that expanded a point into $$\mathbb{P}^1$$, the deformation to the normal cone does this for a more general embedding.

## Examples

Let us verify the properties of the intersection product through concrete examples.

<div class="example" markdown="1">

<ins id="ex10">**Example 10 ($$\mathbb{P}^n$$)**</ins> We have $$\CH^\ast(\mathbb{P}^n) \cong \mathbb{Z}[H] / (H^{n+1})$$. Here $$H$$ is the hyperplane class, and adding the intersection product to $$\Pic(\mathbb{P}^n) \cong \CH^1(\mathbb{P}^n) \cong \mathbb{Z}$$, which we have already computed, completes the Chow ring by adjoining the multiplications $$H \cdot H = H^2$$, $$H \cdot H^2 = H^3$$, ...

</div>

<div class="example" markdown="1">

<ins id="ex11">**Example 11 (Surface)**</ins> In a previous post we saw that for two curves $$C, D$$ on a surface $$S$$:

$$[C] \cdot [D] = \sum_{p \in C \cap D} i_p(C, D) [p] \in \CH^2(S)$$

In general, for an arbitrary surface the structure of $$\CH^2(S)$$ is very complicated; although the intersection number $$C \cdot D = \sum_{p \in C \cap D} i_p(C, D)$$ gives an integer as the image of the degree map, its kernel may be nontrivial, so $$\CH^2(S)$$ need not be $$\mathbb{Z}$$.

However, the situation in $$\mathbb{P}^2$$ is simple. Since $$\CH^\ast(\mathbb{P}^2) = \mathbb{Z}[H]/(H^3)$$, we have $$\CH^2(\mathbb{P}^2) \cong \mathbb{Z}$$, and the intersection number is completely determined. In the Chow ring the class of a conic is $$[X] = 2H$$ and the class of a line is $$[L] = H$$, so $$[X] \cdot [L] = 2H \cdot H = 2H^2 = 2[\text{point}]$$.

</div>

<div class="example" markdown="1">

<ins id="ex12">**Example 12 ($$\mathbb{P}^1 \times \mathbb{P}^1$$)**</ins> As a slightly more complicated example, we saw in [§Rational Maps, ⁋Example 11](/en/math/algebraic_varieties/rational_maps#ex11) that $$\mathbb{P}^1 \times \mathbb{P}^1$$ is isomorphic to the quadric surface $$Q = V(\x\y - \z\w)$$. The Chow ring of $$\mathbb{P}^1 \times \mathbb{P}^1$$ is

$$\CH^\ast(\mathbb{P}^1 \times \mathbb{P}^1) \cong \mathbb{Z}[H_1, H_2] / (H_1^2, H_2^2)$$

and here $$H_1 = [\mathbb{P}^1 \times \{p\}]$$, $$H_2 = [\{p\} \times \mathbb{P}^1]$$. For a curve $$C$$ of bidegree $$(a, b)$$ we have $$[C] = aH_1 + bH_2$$, and therefore the intersection product of two curves $$C = aH_1 + bH_2$$ and $$C' = a'H_1 + b'H_2$$ is

$$C \cdot C' = (aH_1 + bH_2)(a'H_1 + b'H_2) = ab' H_1 H_2 + a'b H_1 H_2 = (ab' + a'b) H_1 H_2$$

</div>

<div class="example" markdown="1">

<ins id="ex13">**Example 13**</ins> Consider the Segre embedding $$\sigma: \mathbb{P}^1 \times \mathbb{P}^1 \to \mathbb{P}^3$$. ([§Projective Varieties, ⁋Example 16](/en/math/algebraic_varieties/projective_varieties#ex16)) The image of this embedding is the quadric surface $$Q = V(\x\y - \z\w)$$. By [§Line Bundles and Vector Bundles, ⁋Proposition 20](/en/math/algebraic_varieties/line_bundles#prop20), the pullback $$\sigma^\ast \mathcal{O}_{\mathbb{P}^3}(1)$$ is a line bundle on $$\mathbb{P}^1 \times \mathbb{P}^1$$, and indeed $$\sigma^\ast \mathcal{O}_{\mathbb{P}^3}(1) \cong \mathcal{O}_{\mathbb{P}^1 \times \mathbb{P}^1}(1,1)$$. This can also be checked at the level of Chow rings: pulling back the hyperplane class $$H_{\mathbb{P}^3}$$ from $$\mathbb{P}^3$$ gives $$H_1 + H_2$$, which corresponds to bidegree $$(1,1)$$.

Using this, intersection calculations in $$\mathbb{P}^3$$ can be transferred to $$\mathbb{P}^1 \times \mathbb{P}^1$$. For example, the intersection in $$\mathbb{P}^3$$ of two hyperplanes $$H, H'$$ with the quadric surface $$Q$$, i.e. the intersection of $$(H \cap Q)$$ and $$(H' \cap Q)$$, is computed in $$\mathbb{P}^1 \times \mathbb{P}^1$$ as $$(H_1 + H_2)^2 = 2H_1 H_2$$. In other words, the intersection of two hyperplanes with the quadric surface is two points, which is the same as two curves of bidegree $$(1,1)$$ meeting in $$Q \cong \mathbb{P}^1 \times \mathbb{P}^1$$.

</div>

## Projection Formula

Finally, we close this post by introducing the following useful formula.

<div class="proposition" markdown="1">

<ins id="prop14">**Proposition 14 (Projection Formula)**</ins> For a proper morphism $$f: X \to Y$$ and classes $$\alpha \in \CH^\ast(X)$$, $$\beta \in \CH^\ast(Y)$$, we have

$$f_\ast(\alpha \cdot f^\ast \beta) = f_\ast(\alpha) \cdot \beta$$

</div>

---

**References**

**[Ful]** W. Fulton, *Intersection Theory*, Springer, 1984.
**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.
