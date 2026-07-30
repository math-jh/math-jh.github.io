---
title: "Intersection Product"
description: "This post covers the definition and properties of the intersection product. We define the intersection product on Chow groups and explore concrete computation examples through intersection multiplicities and the Tor formula."
excerpt: "The intersection product on Chow groups"

categories: [Math / Algebraic Varieties]
permalink: /en/math/algebraic_varieties/intersection_product
sidebar: 
    nav: "algebraic_varieties-en"

date: 2026-05-11
weight: 20
translated_at: 2026-07-11T09:00:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-07-11T09:00:02+00:00
---
In [§Chow Groups](/en/math/algebraic_varieties/chow_groups) we defined the Chow group $\CH^\ast(X)$. At the end of that post we claimed that one can define an intersection product on it to give it a ring structure; in this post we define this product and examine its properties.

The following definition shows what the intersection of two varieties $V,W$ near a point $p$ means. By definition this is a local matter at $p$, so it suffices to choose an affine chart and take the ambient space to be $\mathbb{A}^n$.

::: Definition 1
For two varieties $V, W$ in affine space $\mathbb{A}^n$ at a point $p$, we define their *intersection multiplicity* $i_p(V, W)$ by the formula

$$i_p(V, W) = \dim_{\mathbb{K}} \mathcal{O}_{\mathbb{A}^n, p} / (I(V) + I(W)).$$
:::

By definition, near $p$ the varieties $V$ and $W$ are represented as the common zero sets of the elements of $I(V)$ and $I(W)$ respectively. Then for $p$ to lie in both subvarieties it must be a common zero of all elements of both $I(V)$ and $I(W)$, which leads us to consider the ideal sum $I(V)+I(W)$. In general, if $V,W$ are too small compared with the ambient space they typically do not meet, so the above formula is not well defined. That is, we use the formula only when $\dim V+\dim W=n$. In general, the expected dimension of the intersection of two arbitrary subvarieties meeting each other is $\dim V + \dim W -n$, and for this to be a point we must have $\dim V+\dim W=n$.

In general this definition applies in the local complete intersection case, and in singular situations the following *Tor formula*

$$i_p(V, W) = \sum_{i \ge 0} (-1)^i \dim_{\mathbb{K}} \Tor_i^{R}\bigl(R/I(V),\ R/I(W)\bigr)$$

defines it. The above formula corresponds to the $i = 0$ term. In this post we only look at simple cases, so [Definition 1](#def1) is sufficient.

::: Example 2
In $\mathbb{A}^2$ let $V=\{ \y = 0\}$ and $W=\{\y = \x^2\}$ meet at the origin. The ideals defining the two curves are $I(V) = (\y)$, $I(W) = (\y - \x^2)$. Following the definition we compute the quotient of the local ring at the origin:

$$\mathcal{O}_{\mathbb{A}^2, 0} / (\y, \y - \x^2) = \mathcal{O}_{\mathbb{A}^2, 0} / (\y, \x^2)$$

and this quotient is a 2-dimensional $\mathbb{K}$-vector space with basis $\{1, \x\}$. Hence $i_0(V, W) = 2$. This agrees with the fact that the curve $W$ is tangent to $V$ with order 2 at $\x=0$. More generally, for $V=\{ \y = 0\}$ and $W=\{\y = \x^n\}$ we have $i_0(V, W) = n$.
:::

The above is an example of two 1-dimensional subvarieties meeting in dimension 2, which we already briefly introduced in [§The Riemann–Roch Theorem for Surfaces, ⁋Definition 1](/en/math/algebraic_varieties/riemann_roch_surfaces#def1). In that post we introduced the notion of transversal intersection, which we now define formally.

::: Definition 3
Two varieties $V, W \subseteq \mathbb{A}^n$ *intersect transversely* at a point $p \in V \cap W$ if the sum of their tangent spaces fills the whole space.
:::

Then the following two propositions are natural generalizations of [§The Riemann–Roch Theorem for Surfaces, ⁋Proposition 2](/en/math/algebraic_varieties/riemann_roch_surfaces#prop2).

::: Proposition 4
Intersection multiplicity satisfies the following conditions.

1. For any $p$ and $V,W$, we always have $0\leq i_p(V,W)<\infty$, and $i_p(V,W)=0$ holds exactly when $p\not\in V\cap W$.
2. $V,W$ intersect transversely at $p$ if and only if $i_p(V,W)=1$.
3. $i_p$ satisfies all the conditions of [§The Riemann–Roch Theorem for Surfaces, ⁋Proposition 2](/en/math/algebraic_varieties/riemann_roch_surfaces#prop2).
:::

## Definition of Intersection Product

The definitions so far are, strictly speaking, not enough to make all properties of the intersection product in the Chow group available. For instance, in 3-dimensional space two planes typically meet along a line, but we have only treated the case where the intersection of two subspaces is 0-dimensional, so we cannot explain this. Therefore we first define the following.

::: Definition 5
For two subvarieties $V,W$ of a variety $X$, we say that $V,W$ *intersect properly* if

$$\codim(V \cap W) = \codim V + \codim W$$

holds.
:::

In particular [Definition 1](#def1) is the special case with $\codim (V\cap W)=n$. Now, if the above equality holds for every component of $V,W$, we can use it to define the following formula

$$V \cdot W = \sum_{T \subseteq V \cap W} i_T(V, W) \, [T]$$

where $i_T(V, W)$ is the intersection multiplicity at the component $T$, a natural extension of the point multiplicity in [Definition 1](#def1) to the component $T$. If $T$ is a point $p$ then $i_T(V, W) = i_p(V, W)$, and in general it is the value measuring how the two varieties meet at a general point of $T$, which can be defined rigorously as the intersection multiplicity at the generic point. Then the following lifts the properties of intersection multiplicity to the intersection product.

::: Proposition 6
For two cycles $Z, W$ of codimension $k$, $l$ on a smooth irreducible variety $X$, the *intersection product*

$$Z \cdot W \in \CH^{k+l}(X)$$

is well defined by the above formula. Moreover, it satisfies the following properties.

1. *Symmetry.* $Z \cdot W = W \cdot Z$.
2. *Bilinearity.* $(aZ_1 + bZ_2) \cdot W = a(Z_1 \cdot W) + b(Z_2 \cdot W)$.
3. *Associativity.* $(Z_1 \cdot Z_2) \cdot Z_3 = Z_1 \cdot (Z_2 \cdot Z_3)$.
:::

Then the following definition is what was anticipated from the previous posts.

::: Definition 7
By the intersection product $\CH^\ast(X) = \bigoplus_k \CH^k(X)$ becomes a *graded ring*. We call this the *Chow ring*.
:::

## Moving Lemma

Now our only problem is that, given two arbitrary classes, even if they satisfy the dimension condition we do not know whether the two cycles actually meet nicely. For example, in the current state we cannot define the self-intersection of a given class. For this we need, more generally, that given two arbitrary cycles we can move one within its rational equivalence so that it intersects properly with $W$. The theorem guaranteeing this is the following *moving lemma*.

::: Lemma 8 (Moving Lemma)
For a smooth quasi-projective variety $X$, a cycle $Z \in \CH^k(X)$, and any cycle $W \in \CH^l(X)$, there exists $Z' \sim_{\text{rat}} Z$ such that $Z'$ and $W$ intersect properly.
:::

The key idea is as follows. For each irreducible component $V_i$ of $Z$, we cut $V_i$ by a sufficiently "general" hypersurface $H_i$ containing it, and take a cycle of the form $V_i \cap H_1 \cap \cdots \cap H_s$. Here "general" means that the $H_i$ are chosen to meet $W$ in generic position, which makes the dimensions drop appropriately to achieve a proper intersection. As we saw in [§Linear Systems, ⁋Definition 5](/en/math/algebraic_varieties/linear_systems#def5), using a basepoint-free linear system one can realize such a "general" move by a regular map, and the heart of the proof is showing that this process preserves rational equivalence.

Then using the above lemma we move $Z$ to $Z'$ and define the intersection by the formula

$$Z \cdot W := Z' \cdot W = \sum_{T \subseteq Z' \cap W} i_T(Z', W) [T].$$

## Deformation to Normal Cone

The moving lemma realizes our intuition that, given two classes, we perturb them to compute the intersection. However, this approach depends on the quasi-projectivity assumption, and to extend it to a general setting one needs the *deformation to normal cone*.

The key observation is as follows. First recall that in [§Tangent Spaces and Smoothness, ⁋Definition 13](/en/math/algebraic_varieties/tangent_spaces_and_smoothness#def13) we defined the tangent cone. This was a tool for understanding the local structure at a singular point, and generalizing this we can define the *normal cone* $C_{Y/X}$ of $Y$ inside $X$ for a closed embedding $i: Y \hookrightarrow X$. If $X$ is smooth along $Y$ then the normal cone becomes the normal bundle $N_{Y/X}$, but in general it has a cone structure.

::: Proposition 9 (Deformation to Normal Cone)
For a closed embedding $i: Y \hookrightarrow X$, one can construct a family $M \rightarrow \mathbb{A}^1$ parameterized by $\mathbb{A}^1$. Specifically, the fiber $M_t$ for $t \neq 0$ is $X$ itself, and the fiber $M_0$ at $t = 0$ is the normal cone $C_{Y/X}$. The existence of this family reduces the well-definedness of the intersection product to the compatibility of pushforward and pullback for this family.
:::

::: Proof
The construction uses blow-up. First blow up $X \times \mathbb{A}^1$ along $Y \times \{0\}$ to obtain $\widetilde{M} = \Bl_{Y \times \{0\}}(X \times \mathbb{A}^1)$, then remove the proper transform of $X \times \{0\}$ to define $M = \widetilde{M} \setminus \widetilde{X \times \{0\}}$. The exceptional divisor of this blow-up is $\mathbb{P}(C_{Y/X} \oplus \mathcal{O}_Y)$, and removing the proper transform leaves exactly the normal cone $C_{Y/X}$ in the $t=0$ fiber. For $t \neq 0$ the blow-up is an isomorphism, so the fiber is just $X$. Thus $M \rightarrow \mathbb{A}^1$ provides a deformation connecting $X$ at $t=1$ to $C_{Y/X}$ at $t=0$. In the Chow group one can define a specialization map $\sigma: \CH^\ast(X) \rightarrow \CH^\ast(C_{Y/X})$ on $M$, and when the normal cone has a vector bundle structure (i.e. for a regular embedding) the Thom isomorphism gives $\CH^\ast(C_{Y/X}) \cong \CH^\ast(Y)$, establishing the well-definedness of the intersection product.
:::

The idea of this method is to deform $X$ continuously and shrink it onto the normal cone of $Y$. Geometrically, at $t=1$ we see the original space $X$, and as $t$ goes to $0$ the space $X$ is "flattened" more and more along $Y$ until at $t=0$ it becomes the normal cone opened up along $Y$. If the blow-up in [§Rational Maps, ⁋Example 12](/en/math/algebraic_varieties/rational_maps#ex12) was a deformation that expands a point into $\mathbb{P}^1$, the deformation to normal cone performs this for a more general embedding.

## Examples

Let us verify the properties of the intersection product through concrete examples.

::: Example 10 ($\mathbb{P}^n$)
$\CH^\ast(\mathbb{P}^n) \cong \mathbb{Z}[H] / (H^{n+1})$. Here $H$ is the hyperplane class, and adding the intersection product to the $\Pic(\mathbb{P}^n) \cong \CH^1(\mathbb{P}^n) \cong \mathbb{Z}$ we already computed gives the multiplication $H \cdot H = H^2$, $H \cdot H^2 = H^3$, ... and completes the Chow ring.
:::

::: Example 11 (Surface)
In the previous post we saw that for two curves $C, D$ on a surface $S$:

$$[C] \cdot [D] = \sum_{p \in C \cap D} i_p(C, D) [p] \in \CH^2(S).$$

For a general surface the structure of $\CH^2(S)$ is very complicated, and in general the intersection multiplicity $C \cdot D = \sum_{p \in C \cap D} i_p(C, D)$ gives an integer value as the image of the degree map, but its kernel may be nontrivial so $\CH^2(S)$ need not be $\mathbb{Z}$.

However, the situation is simple for $\mathbb{P}^2$. Since $\CH^\ast(\mathbb{P}^2) = \mathbb{Z}[H]/(H^3)$ we have $\CH^2(\mathbb{P}^2) \cong \mathbb{Z}$, and the intersection number is completely determined. In the Chow ring the class of a conic is $[X] = 2H$ and the class of a line is $[L] = H$, so $[X] \cdot [L] = 2H \cdot H = 2H^2 = 2[\text{point}]$.
:::

::: Example 12 ($\mathbb{P}^1 \times \mathbb{P}^1$)
As a slightly more complicated example, we saw in [§Rational Maps, ⁋Example 11](/en/math/algebraic_varieties/rational_maps#ex11) that $\mathbb{P}^1 \times \mathbb{P}^1$ and the quadric surface $Q = V(\x\y - \z\w)$ are isomorphic. The Chow ring of $\mathbb{P}^1 \times \mathbb{P}^1$ is

$$\CH^\ast(\mathbb{P}^1 \times \mathbb{P}^1) \cong \mathbb{Z}[H_1, H_2] / (H_1^2, H_2^2)$$

where $H_1 = [\mathbb{P}^1 \times \{p\}]$, $H_2 = [\{p\} \times \mathbb{P}^1]$. For a curve $C$ of bidegree $(a, b)$ we have $[C] = aH_1 + bH_2$, and thus the intersection product of two curves $C = aH_1 + bH_2$, $C' = a'H_1 + b'H_2$ is computed as

$$C \cdot C' = (aH_1 + bH_2)(a'H_1 + b'H_2) = ab' H_1 H_2 + a'b H_1 H_2 = (ab' + a'b) H_1 H_2.$$
:::

::: Example 13
Consider the Segre embedding $\sigma: \mathbb{P}^1 \times \mathbb{P}^1 \rightarrow \mathbb{P}^3$. ([§Projective Varieties, ⁋Example 16](/en/math/algebraic_varieties/projective_varieties#ex16)) The image of this embedding is the quadric surface $Q = V(\x\y - \z\w)$. By [§Line Bundles and Vector Bundles, ⁋Proposition 20](/en/math/algebraic_varieties/line_bundles#prop20) the pullback $\sigma^\ast \mathcal{O}_{\mathbb{P}^3}(1)$ is a line bundle on $\mathbb{P}^1 \times \mathbb{P}^1$, and in fact $\sigma^\ast \mathcal{O}_{\mathbb{P}^3}(1) \cong \mathcal{O}_{\mathbb{P}^1 \times \mathbb{P}^1}(1,1)$. This can also be seen at the Chow ring level: pulling back the hyperplane class $H_{\mathbb{P}^3}$ from $\mathbb{P}^3$ gives $H_1 + H_2$, which corresponds to bidegree $(1,1)$.

Through this we can transfer intersection calculations in $\mathbb{P}^3$ to $\mathbb{P}^1 \times \mathbb{P}^1$. For instance, the intersection of two hyperplanes $H, H'$ in $\mathbb{P}^3$ each with the quadric surface $Q$, i.e. the intersection of $(H \cap Q)$ and $(H' \cap Q)$, is computed in $\mathbb{P}^1 \times \mathbb{P}^1$ as $(H_1 + H_2)^2 = 2H_1 H_2$. That is, the intersection of two hyperplanes with a quadric surface is 2 points, which is the same as two curves of bidegree $(1,1)$ meeting in $Q \cong \mathbb{P}^1 \times \mathbb{P}^1$.
:::

## Projection Formula

We close this post by introducing the following useful formula.

::: Proposition 14 (Projection Formula)
For a proper morphism $f: X \rightarrow Y$ and $\alpha \in \CH^\ast(X)$, $\beta \in \CH^\ast(Y)$,

$$f_\ast(\alpha \cdot f^\ast \beta) = f_\ast(\alpha) \cdot \beta$$

holds.
:::


---

**References**

**[Ful]** W. Fulton, *Intersection Theory*, Springer, 1984.  
**[Hart]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.
