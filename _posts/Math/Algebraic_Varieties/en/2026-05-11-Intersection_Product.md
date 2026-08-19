---
title: "Intersection Product"
description: "We cover the definition and properties of the intersection product. We define the intersection product on Chow groups and explore concrete computational examples using intersection multiplicities and the Tor formula."
excerpt: "The intersection product on Chow groups"

categories: [Math / Algebraic Varieties]
permalink: /en/math/algebraic_varieties/intersection_product
sidebar: 
    nav: "algebraic_varieties-en"

date: 2026-05-11
weight: 20
translated_at: 2026-08-19T03:15:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-08-19T03:15:04+00:00
---
In [§Chow Groups](/en/math/algebraic_varieties/chow_groups) we defined the Chow group $\CH^\ast(X)$. At the end of that post we claimed that one can define an intersection product on it, thereby giving it a ring structure; in this post we construct this product and examine its properties.

The following definition shows what the intersection of two varieties $V,W$ near a point $p$ is. By definition this is a local matter at $p$, so it suffices to pick an affine chart and take the ambient space to be $\mathbb{A}^n$.

::: Definition 1
At a point $p$ of affine space $\mathbb{A}^n$, the *intersection multiplicity* $i_p(V, W)$ of two varieties $V, W$ is defined by the formula

$$i_p(V, W) = \dim_{\mathbb{K}} \mathcal{O}_{\mathbb{A}^n, p} / (I(V) + I(W)).$$
:::

By definition, near $p$ the varieties $V$ and $W$ are represented as the common zero loci of elements of $I(V)$ and $I(W)$ respectively. Thus for $p$ to lie in both subvarieties it must be a common zero of all elements of $I(V)$ and $I(W)$, which leads us to consider the ideal sum $I(V)+I(W)$. In general, if $V,W$ are too large relative to the ambient space then their intersection has positive dimension and the above quotient becomes infinite-dimensional, while if they are too small then a generic small perturbation of one will make them disjoint, so the formula fails to give a stable value. Hence we use the above formula only when $\dim V+\dim W=n$. In general, when two arbitrary subvarieties meet the expected dimension of their intersection is $\dim V + \dim W - n$, and for this to be a point we must have $\dim V+\dim W=n$.

In general this definition applies in the local complete intersection case; when this is not the case the following *Tor formula*

$$i_p(V, W) = \sum_{i \ge 0} (-1)^i \dim_{\mathbb{K}} \Tor_i^{R}\bigl(R/I(V),\ R/I(W)\bigr)$$

gives the definition. Here $R = \mathcal{O}_{\mathbb{A}^n, p}$. The formula above corresponds to the $i = 0$ term. In this post we only consider simple cases, so [Definition 1](#def1) suffices.

::: Example 2
In $\mathbb{A}^2$ the varieties $V=\{ \y = 0\}$ and $W=\{\y = \x^2\}$ meet at the origin. The ideals defining the respective curves are $I(V) = (\y)$, $I(W) = (\y - \x^2)$. Computing the quotient by the local ring at the origin according to the definition gives

$$\mathcal{O}_{\mathbb{A}^2, 0} / (\y, \y - \x^2) = \mathcal{O}_{\mathbb{A}^2, 0} / (\y, \x^2),$$

and this quotient is a 2-dimensional $\mathbb{K}$-vector space with basis $\{1, \x\}$. Hence $i_0(V, W) = 2$. This agrees with the fact that the curve $W$ is tangent to $V$ at $\x=0$ with order 2. More generally, for $V=\{ \y = 0\}$ and $W=\{\y = \x^n\}$ we have $i_0(V, W) = n$.
:::

The above is an example of two 1-dimensional subvarieties meeting in dimension 2, which we already briefly introduced in [§The Riemann–Roch Theorem for Surfaces, ⁋Definition 1](/en/math/algebraic_varieties/riemann_roch_surfaces#def1). In that post we introduced the notion of transversal intersection; let us define it formally.

::: Definition 3
Two varieties $V, W \subseteq \mathbb{A}^n$ are said to *intersect transversely* at a point $p \in V \cap W$ which is a smooth point of both if the sum of their tangent spaces fills the whole space.
:::

Then the following two propositions are natural generalizations of [§The Riemann–Roch Theorem for Surfaces, ⁋Proposition 2](/en/math/algebraic_varieties/riemann_roch_surfaces#prop2).

::: Proposition 4
Intersection multiplicity satisfies the following conditions.

1. For any $p$ which is an isolated point of $V\cap W$ and any $V,W$, we have $0\leq i_p(V,W)<\infty$, and if $p\not\in V\cap W$ then $i_p(V,W)=0$.
2. $V,W$ intersect transversally at $p$ if and only if $i_p(V,W)=1$.
3. $i_p$ satisfies the symmetry and bilinearity of [§The Riemann–Roch Theorem for Surfaces, ⁋Proposition 2](/en/math/algebraic_varieties/riemann_roch_surfaces#prop2).
:::

## Definition of the Intersection Product

Strictly speaking, the definitions so far do not yet allow us to use all the properties of the intersection product in the Chow group. For example, in 3-dimensional space two planes will generally meet in a line, but we have only treated the case where the intersection of two subspaces is 0-dimensional, so we cannot explain this. Hence we first make the following definition.

::: Definition 5
For two subvarieties $V,W$ of a variety $X$, we say that $V,W$ *intersect properly* if

$$\codim(V \cap W) = \codim V + \codim W$$

holds.
:::

In particular [Definition 1](#def1) is the special case where $\codim (V\cap W)=n$. Now, if the above equality holds for every irreducible component of $V\cap W$, we can use it to define

$$V \cdot W = \sum_{T \subseteq V \cap W} i_T(V, W) [T].$$

Here $i_T(V, W)$ is the intersection multiplicity along the component $T$, the natural extension of the pointwise multiplicity of [Definition 1](#def1) to a component $T$. If $T$ is a point $p$ then $i_T(V, W) = i_p(V, W)$, and in general it is the value measuring how the two varieties meet at a general point of $T$, which can be defined rigorously as the intersection multiplicity at the generic point. The following proposition lifts the properties of intersection multiplicity to the intersection product.

::: Proposition 6
On a smooth irreducible quasi-projective variety $X$, if two cycles $Z, W$ of codimension $k$, $l$ respectively intersect properly, the above formula well-defines the *intersection product*

$$Z \cdot W \in \CH^{k+l}(X).$$

Moreover, it satisfies the following properties.

1. *Symmetry.* $Z \cdot W = W \cdot Z$.
2. *Bilinearity.* $(aZ_1 + bZ_2) \cdot W = a(Z_1 \cdot W) + b(Z_2 \cdot W)$.
3. *Associativity.* $(Z_1 \cdot Z_2) \cdot Z_3 = Z_1 \cdot (Z_2 \cdot Z_3)$.
:::

Then the following definition is what was anticipated from the previous post.

::: Definition 7
For a smooth quasi-projective variety $X$, the intersection product makes $\CH^\ast(X) = \bigoplus_k \CH^k(X)$ a *graded ring*. This is called the *Chow ring*.
:::

## Moving Lemma

Our only remaining problem is that, given two arbitrary classes, even if they satisfy the dimension condition we do not know whether the two cycles actually meet nicely. For example, in the present state we cannot define the self-intersection of a given class. To do this, we need more generally, given two arbitrary cycles, to move one within its rational equivalence class so that it intersects $W$ properly. The theorem guaranteeing this is the following *moving lemma*.

::: Lemma 8 (Moving Lemma)
For a smooth quasi-projective variety $X$, a cycle $Z \in Z^k(X)$, and any cycle $W \in Z^l(X)$, there exists $Z' \sim_{\text{rat}} Z$ such that $Z'$ and $W$ intersect properly.
:::

The key idea is that, rather than moving the irreducible components $V_i$ constituting $Z$ directly, we represent them by cutting them out from a larger cycle. Embedding $X$ in $\mathbb{P}^n$ and taking the cone $C_L(V_i)$ over $V_i$ with a general linear subspace $L$ as vertex, the dimensions match so that $C_L(V_i)$ and $X$ intersect properly and at the cycle level we obtain $C_L(V_i) \cdot X = V_i + R_i$ with a residual cycle $R_i$ left over. Then from the rational equivalence moving $C_L(V_i)$ to a cycle $C$ in general position in $\mathbb{P}^n$ we obtain $V_i \sim_{\text{rat}} C \cdot X - R_i$, and the first term on the right already intersects $W$ properly. For the remaining $R_i$, when $L$ is chosen generally the excess that $R_i$ has with respect to $W$ (that is, the amount by which the dimension of the intersection exceeds the expected dimension) becomes strictly smaller than that of $V_i$, so by induction on this excess we obtain the desired $Z'$. As we saw in [§Linear Systems, ⁋Definition 5](/en/math/algebraic_varieties/linear_systems#def5), using a basepoint-free linear system one can realize such a *general* move by a regular map, and the heart of the proof is showing that this process preserves rational equivalence.

Then using the above lemma we move $Z$ to $Z'$ and define the intersection by the formula

$$Z \cdot W := Z' \cdot W = \sum_{T \subseteq Z' \cap W} i_T(Z', W) [T].$$

## Deformation to Normal Cone

The moving lemma realizes our intuition that, given two classes, we perturb them to compute the intersection. However, this approach relies on the quasi-projectivity assumption, and to extend it to a general setting one needs the *deformation to normal cone*.

The key observation is as follows. First recall that in [§Tangent Spaces and Smoothness, ⁋Definition 13](/en/math/algebraic_varieties/tangent_spaces_and_smoothness#def13) we defined the tangent cone. This was a tool for understanding the local structure at a singular point, and generalizing this we can define the *normal cone* $C_{Y/X}$ of a closed embedding $i: Y \hookrightarrow X$ inside $X$. If $i$ is a regular embedding (for instance if both $X$ and $Y$ are smooth) the normal cone becomes the normal bundle $N_{Y/X}$, but in general it has a cone structure.

::: Proposition 9 (Deformation to Normal Cone)
For a closed embedding $i: Y \hookrightarrow X$, one can construct a family $M \rightarrow \mathbb{A}^1$ parameterized by $\mathbb{A}^1$. Specifically, the fiber $M_t$ for $t \neq 0$ is $X$ itself, and the fiber $M_0$ at $t = 0$ is the normal cone $C_{Y/X}$. The existence of this family reduces the well-definedness of the intersection product to the compatibility of pushforward and pullback for this family.
:::

::: Proof
The construction uses blow-up. First blow up $X \times \mathbb{A}^1$ along $Y \times \{0\}$ to obtain $\widetilde{M} = \Bl_{Y \times \{0\}}(X \times \mathbb{A}^1)$, then remove the proper transform of $X \times \{0\}$ to define $M = \widetilde{M} \setminus \widetilde{X \times \{0\}}$. The exceptional divisor of this blow-up is $\mathbb{P}(C_{Y/X} \oplus \mathcal{O}_Y)$, and removing the proper transform leaves exactly the normal cone $C_{Y/X}$ in the $t=0$ fiber. For $t \neq 0$ the blow-up is an isomorphism so the fiber is just $X$. Hence $M \rightarrow \mathbb{A}^1$ provides a deformation connecting $X$ at $t=1$ to $C_{Y/X}$ at $t=0$. In the Chow group one can define a specialization map $\sigma: \CH^\ast(X) \rightarrow \CH^\ast(C_{Y/X})$ on $M$, and when the normal cone has a vector bundle structure (that is, in the regular embedding case) the Thom isomorphism gives $\CH^\ast(C_{Y/X}) \cong \CH^\ast(Y)$, establishing the well-definedness of the intersection product.
:::

The idea of this method is to deform $X$ continuously and shrink it onto the normal cone of $Y$. Geometrically, at $t=1$ we see the original space $X$, and as $t$ goes to $0$ the space $X$ becomes increasingly *flattened* along $Y$ until at $t=0$ it becomes the normal cone opened up along $Y$. If the blow-up in [§Rational Maps, ⁋Example 12](/en/math/algebraic_varieties/rational_maps#ex12) was the deformation that blows up a point to a $\mathbb{P}^1$, then deformation to normal cone performs this for a more general embedding.

## Examples

Let us verify the properties of the intersection product through concrete examples.

::: Example 10 ($\mathbb{P}^n$)
$\CH^\ast(\mathbb{P}^n) \cong \mathbb{Z}[H] / (H^{n+1})$. Here $H$ is the hyperplane class, and adding the intersection product to the $\Pic(\mathbb{P}^n) \cong \CH^1(\mathbb{P}^n) \cong \mathbb{Z}$ that we already computed gives the additional multiplications $H \cdot H = H^2$, $H \cdot H^2 = H^3$, ... completing the Chow ring.
:::

::: Example 11 (Surface)
In the previous post we saw that for two curves $C, D$ on a surface $S$:

$$[C] \cdot [D] = \sum_{p \in C \cap D} i_p(C, D) [p] \in \CH^2(S).$$

For a general surface the structure of $\CH^2(S)$ is very complicated, and although the intersection multiplicity $C \cdot D = \sum_{p \in C \cap D} i_p(C, D)$ yields an integer value as the image of the degree map, its kernel can be nontrivial so that $\CH^2(S)$ need not be $\mathbb{Z}$.

However, the situation in $\mathbb{P}^2$ is simple. Since $\CH^\ast(\mathbb{P}^2) = \mathbb{Z}[H]/(H^3)$ we have $\CH^2(\mathbb{P}^2) \cong \mathbb{Z}$, and the intersection number is completely determined. In the Chow ring the class of a conic is $[C] = 2H$ and the class of a line is $[L] = H$, so $[C] \cdot [L] = 2H \cdot H = 2H^2 = 2[\text{pt}]$.
:::

::: Example 12 ($\mathbb{P}^1 \times \mathbb{P}^1$)
As a slightly more complicated example, we saw in [§Rational Maps, ⁋Example 11](/en/math/algebraic_varieties/rational_maps#ex11) that $\mathbb{P}^1 \times \mathbb{P}^1$ and the quadric surface $Q = V(\x\y - \z\w)$ are isomorphic. The Chow ring of $\mathbb{P}^1 \times \mathbb{P}^1$ is

$$\CH^\ast(\mathbb{P}^1 \times \mathbb{P}^1) \cong \mathbb{Z}[H_1, H_2] / (H_1^2, H_2^2),$$

where $H_1 = [\mathbb{P}^1 \times \{p\}]$, $H_2 = [\{p\} \times \mathbb{P}^1]$. For a curve $C$ of bidegree $(a, b)$ we have $[C] = aH_1 + bH_2$, and hence the intersection product of two curves $C = aH_1 + bH_2$, $C' = a'H_1 + b'H_2$ is computed as

$$C \cdot C' = (aH_1 + bH_2)(a'H_1 + b'H_2) = ab' H_1 H_2 + a'b H_1 H_2 = (ab' + a'b) H_1 H_2.$$
:::

::: Example 13
Consider the Segre embedding $\sigma: \mathbb{P}^1 \times \mathbb{P}^1 \rightarrow \mathbb{P}^3$. ([§Projective Varieties, ⁋Example 16](/en/math/algebraic_varieties/projective_varieties#ex16)) The image of this embedding is the quadric surface $Q = V(\x\y - \z\w)$. By [§Line Bundles and Vector Bundles, ⁋Proposition 20](/en/math/algebraic_varieties/line_bundles#prop20) the pullback $\sigma^\ast \mathcal{O}_{\mathbb{P}^3}(1)$ is a line bundle on $\mathbb{P}^1 \times \mathbb{P}^1$, and indeed $\sigma^\ast \mathcal{O}_{\mathbb{P}^3}(1) \cong \mathcal{O}_{\mathbb{P}^1 \times \mathbb{P}^1}(1,1)$. This can also be checked at the level of Chow rings: pulling back the hyperplane class $H_{\mathbb{P}^3}$ in $\mathbb{P}^3$ gives $H_1 + H_2$, which corresponds to bidegree $(1,1)$.

Through this we can transfer intersection computations in $\mathbb{P}^3$ to $\mathbb{P}^1 \times \mathbb{P}^1$. For example, the intersection of the two hyperplanes $H, H'$ in $\mathbb{P}^3$ each with the quadric surface $Q$, that is the intersection of $(H \cap Q)$ and $(H' \cap Q)$, is computed in $\mathbb{P}^1 \times \mathbb{P}^1$ as $(H_1 + H_2)^2 = 2H_1 H_2$. That is, the intersection of two hyperplanes with a quadric surface is 2 points, which is the same as two curves of bidegree $(1,1)$ meeting in $Q \cong \mathbb{P}^1 \times \mathbb{P}^1$.
:::

## Projection Formula

We close this post by introducing the following useful formula.

::: Proposition 14 (Projection Formula)
For a proper morphism $f: X \rightarrow Y$ between smooth varieties and $\alpha \in \CH^\ast(X)$, $\beta \in \CH^\ast(Y)$,

$$f_\ast(\alpha \cdot f^\ast \beta) = f_\ast(\alpha) \cdot \beta$$

holds.
:::


---

**References**

**[Ful]** W. Fulton, *Intersection Theory*, Springer, 1984.  
**[Hart]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.
