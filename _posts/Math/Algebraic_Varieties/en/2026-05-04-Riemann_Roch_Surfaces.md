---
title: "The Riemann–Roch Theorem for Surfaces"
excerpt: "Intersection theory on surfaces and its applications"

categories: [Math / Algebraic Varieties]
permalink: /en/math/algebraic_varieties/riemann_roch_surfaces
sidebar: 
    nav: "algebraic_varieties-en"

header:
    overlay_image: /assets/images/Math/Algebraic_Varieties/Riemann_Roch_Surfaces.png
    overlay_filter: 0.5

date: 2026-05-04
last_modified_at: 2026-05-09
weight: 16
---

We examined the Riemann–Roch theorem for curves in the previous post. Essentially, the Riemann–Roch theorem computes the Euler characteristic in terms of other quantitative invariants, and although we could generalize it to arbitrary cases, in this post we only discuss its generalization to surfaces.

Recall the Riemann–Roch formula for a curve $$C$$ ([§The Riemann–Roch Theorem for Curves, ⁋Proposition 3](/en/math/algebraic_varieties/riemann_roch_theorem#prop3))

$$\ell(D) - \ell(K_C - D) = \deg D + 1 - g$$

Observing this formula, the left-hand side is essentially the Euler characteristic of $$\mathcal{O}_C(D)$$, and [§The Riemann–Roch Theorem for Curves, ⁋Lemma 2](/en/math/algebraic_varieties/riemann_roch_theorem#lem2) guarantees that this part consists of only two terms. However, when we generalize this to a surface, the dimension of the base space increases by one, so additional terms will appear, and correspondingly the right-hand side will also acquire additional terms.

Intuitively, the term $$\deg D$$ appearing on the right-hand side can be thought of as a linear term, but in the process of generalizing to surfaces we must consider additional *quadratic terms* such as $$D \cdot D$$, $$D \cdot K_S$$, etc. These quantities encode how two divisors on a surface intersect each other, arising from the fact that while divisors on a curve, i.e., points, generally do not meet inside the curve, divisors on a surface, i.e., curves, generally meet at finitely many points inside the surface.

In this post, we treat the definition of intersection numbers and their basic properties, rigorously derive the Riemann–Roch formula, and then apply it to prove the Hodge index theorem and an inequality for plurigenera. We also examine the meaning of the intersection form in the birational geometry of surfaces.

## Intersection numbers

Our starting point is a definition using the Euler characteristic, which may appear somewhat abstract. The advantage of this definition is that invariance under linear equivalence follows immediately, and we will verify right after the definition that it actually counts intersection points.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> For two divisors $$C, D$$ on a smooth surface $$S$$, the *intersection number* $$C \cdot D$$ is defined as follows.

$$C \cdot D = \rchi(\mathcal{O}_S(C + D)) - \rchi(\mathcal{O}_S(C)) - \rchi(\mathcal{O}_S(D)) + \rchi(\mathcal{O}_S)$$

</div>

To examine the geometric meaning of this, suppose $$C$$ and $$D$$ are effective divisors defined by global sections $$s \in H^0(\mathcal{O}(C))$$, $$t \in H^0(\mathcal{O}(D))$$, respectively. Then their common zero locus is $$C \cap D$$, and the following exact sequence holds.

$$0 \to \mathcal{O} \xrightarrow{(t,-s)} \mathcal{O}(C) \oplus \mathcal{O}(D) \xrightarrow{(s,t)} \mathcal{O}(C+D) \to \mathcal{O}_{C \cap D} \to 0$$

Here the first arrow is $$h \mapsto (ht, -hs)$$, the second arrow is $$(f, g) \mapsto fs + gt$$, and the last arrow is the natural restriction map from $$\mathcal{O}(C+D)$$ to $$C \cap D$$. Then by additivity of the Euler characteristic,

$$C \cdot D = \rchi(\mathcal{O}_{C \cap D})$$

and in this case $$C \cap D$$ is the intersection of two curves, i.e., points, so the Euler characteristic on the right-hand side exactly counts the number of points in $$C \cap D$$. A somewhat subtle point is that for this to be well defined, $$C$$ and $$D$$ must be in general position; for this purpose we define two curves $$C, D$$ to *transversally intersect* at a point $$p$$ by the condition

$$T_pC \oplus T_pD \cong T_pS$$

For example, in $$\mathbb{A}^2$$, $$\x=0$$ does not transversally intersect itself, and $$\y=\x^3$$ does not transversally intersect $$\y=0$$. On the other hand, $$\y=\x$$ and $$\y=-\x$$ meet transversally. Moreover, these examples also provide intuition for intersection multiplicity: the intersection multiplicity of $$\y=\x$$ and $$\y=-\x$$ (at the origin) is $$1$$, but that of $$\y=\x^3$$ and $$\y=0$$ is $$3$$. Then in the general case where $$C$$ and $$D$$ may not meet transversally,

$$\rchi(\mathcal{O}_{C \cap D}) = \sum_{p \in C \cap D} (C \cdot D)_p$$

holds, where $$(C \cdot D)_p$$ is the local intersection multiplicity at $$p$$. To prevent $$C \cap D$$ from being a curve instead of a finite set of points in this formula (for instance, in the situation $$C=D$$), we assume that $$C$$ and $$D$$ have no common component.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> The following are properties of the intersection number.

1. *Symmetry.* $$C \cdot D = D \cdot C$$ holds.
2. *Bilinearity.* $$(aC_1 + bC_2) \cdot D = a(C_1 \cdot D) + b(C_2 \cdot D)$$ holds.
3. *Linear invariance.* For two linearly equivalent divisors $$C \sim C'$$, we always have $$C \cdot D = C' \cdot D$$.

</div>

Symmetry is obvious from the intuition shown above, and linear invariance is also almost obvious. What is perhaps least obvious is bilinearity, which is usually explained by Snapper's theorem. By Snapper's theorem, for any coherent sheaf $$\mathcal{F}$$ on a projective variety and line bundles $$L_1, \ldots, L_k$$, the Euler characteristic

$$\rchi(\mathcal{F} \otimes L_1^{\otimes n_1} \otimes \cdots \otimes L_k^{\otimes n_k})$$

is given by a polynomial in $$n_1, \ldots, n_k$$. Then in particular $$\rchi(\mathcal{O}_S(aC_1 + bC_2 + D))$$ is a polynomial in $$a, b$$, and comparing the quadratic coefficients of this polynomial yields bilinearity.

## The Riemann–Roch theorem for surfaces

We now have all the language needed to extend the Riemann–Roch theorem to surfaces. What we need is the following lemma.

<div class="proposition" markdown="1">

<ins id="lem3">**Lemma 3 (Genus formula)**</ins> For a smooth irreducible curve $$D$$ on a smooth projective surface $$S$$,

$$2g(D) - 2 = D^2 + D \cdot K_S$$

holds.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

By the adjunction formula ([§The Canonical Bundle, ⁋Proposition 9](/en/math/algebraic_varieties/canonical_bundle#prop9)),

$$\omega_D \cong (\omega_S \otimes \mathcal{O}_S(D))\vert_D$$

holds. Taking degrees of both sides,

$$\deg(\omega_D) = \deg(\omega_S\vert_D) + \deg(\mathcal{O}_D(D))$$

holds. We previously derived from [§The Riemann–Roch Theorem for Curves, ⁋Proposition 3](/en/math/algebraic_varieties/riemann_roch_theorem#prop3) that $$\deg(\omega_D)=2g-2$$, and it remains to interpret the two terms on the right-hand side as intersection numbers. First, $$\omega_S\vert_D$$ is the canonical bundle restricted to $$D$$, which measures the intersection number of $$D$$ with the canonical divisor $$K_S$$. Specifically, since $$K_S$$ is the divisor corresponding to $$\omega_S$$, the degree of $$\omega_S\vert_D$$ equals the number of points that $$K_S$$ occupies on $$D$$, i.e., $$D \cdot K_S$$. Similarly, $$\mathcal{O}_D(D)$$ corresponds to the normal bundle $$\mathcal{N}_{D/S}$$ of $$D$$, which measures the degree to which $$D$$ meets itself inside $$S$$. The degree of this bundle coincides with the self-intersection number $$D^2$$ of $$D$$. Combining these,

$$2g(D) - 2 = D \cdot K_S + D^2$$

is obtained.

</details>

Then the Riemann–Roch theorem on a surface is given as follows.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4 (Riemann–Roch for surfaces)**</ins> For a divisor $$D$$ on a smooth projective surface $$S$$,

$$\rchi(\mathcal{O}_S(D)) = \frac{1}{2} D \cdot (D - K_S) + \rchi(\mathcal{O}_S)$$

holds.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

First consider the case where $$D$$ is a smooth irreducible effective divisor. From the short exact sequence

$$0 \to \mathcal{O}_S \to \mathcal{O}_S(D) \to \mathcal{O}_D(D) \to 0$$

additivity of the Euler characteristic gives

$$\rchi(\mathcal{O}_S(D)) = \rchi(\mathcal{O}_S) + \rchi(\mathcal{O}_D(D))$$

Here, since $$\mathcal{O}_D(D)$$ is a line bundle defined on $$D$$, by the Riemann–Roch for curves ([§The Riemann–Roch Theorem for Curves, ⁋Proposition 3](/en/math/algebraic_varieties/riemann_roch_theorem#prop3)),

$$\rchi(\mathcal{O}_D(D)) = D^2 + 1 - g(D)$$

holds. From the preceding [Lemma 3](#lem3),

$$g(D) = \frac{1}{2}(D^2 + D \cdot K_S) + 1$$

so substituting this gives

$$\rchi(\mathcal{O}_D(D)) = D^2 + 1 - \frac{1}{2}(D^2 + D \cdot K_S) - 1 = \frac{1}{2}D \cdot (D - K_S)$$

Therefore

$$\rchi(\mathcal{O}_S(D)) = \rchi(\mathcal{O}_S) + \frac{1}{2}D \cdot (D - K_S)$$

is obtained.

We now need to generalize this to an arbitrary divisor $$D$$. First fix an ample divisor $$H$$ on $$S$$. Then by Serre vanishing ([§Cohomology of Projective Spaces, ⁋Proposition 4](/en/math/algebraic_varieties/cohomology_of_projective_spaces#prop4)), for sufficiently large $$n$$,

$$H^1(S, \mathcal{O}_S(D + nH)) = H^2(S, \mathcal{O}_S(D + nH)) = 0$$

holds. Therefore

$$\rchi(\mathcal{O}_S(D + nH)) = h^0(\mathcal{O}_S(D + nH))$$

holds. On the other hand, since $$D+nH$$ is an effective divisor, the desired equality holds for $$D+nH$$ by the preceding argument. Thus, considering the two functions of $$n$$, $$f(n) = \rchi(\mathcal{O}(D+nH))$$ and $$g(n) = \frac{1}{2}(D+nH)\cdot(D+nH-K_S) + \rchi(\mathcal{O}_S)$$, they agree for all sufficiently large $$n$$. But by Snapper's theorem mentioned earlier, $$\rchi(\mathcal{O}_S(D+nH))$$ is a polynomial in $$n$$, and two polynomials that agree at infinitely many points are identical. Hence $$f$$ and $$g$$ are in fact the same polynomial, i.e., $$f(n) = g(n)$$ for all $$n$$, and in particular substituting $$n = 0$$ gives

$$\rchi(\mathcal{O}(D)) = \frac{1}{2}D\cdot(D-K_S) + \rchi(\mathcal{O}_S)$$

is obtained.

</details>

As in the case of curves, if $$D$$ is sufficiently "positive" then $$h^1$$ and $$h^2$$ vanish and $$\rchi(\mathcal{O}_S(D)) = h^0(S, \mathcal{O}_S(D))$$. This is closely related to the notion of ampleness defined in ([§Linear Systems, ⁋Definition 10](/en/math/algebraic_varieties/linear_systems#def10)).

<div class="example" markdown="1">

<ins id="ex5">**Example 5 ($$\mathbb{P}^2$$)**</ins> Fixing the hyperplane class $$H$$ in $$\mathbb{P}^2$$, we know

$$K_{\mathbb{P}^2} = -3H, \qquad \rchi(\mathcal{O}_{\mathbb{P}^2}) = 1$$

([§The Canonical Bundle, ⁋Proposition 7](/en/math/algebraic_varieties/canonical_bundle#prop7), [§Cohomology of Projective Spaces, ⁋Corollary 3](/en/math/algebraic_varieties/cohomology_of_projective_spaces#cor3)). Since any two lines in $$\mathbb{P}^2$$ generally meet at one point, the self-intersection number of $$H$$ is $$1$$, and thus for an arbitrary divisor $$D = dH$$,

$$\rchi(\mathcal{O}_{\mathbb{P}^2}(d)) = \frac{1}{2}dH \cdot (dH + 3H) + 1 = \frac{1}{2}d(d+3) + 1$$

holds. That this actually holds is the result of [§Cohomology of Projective Spaces, ⁋Corollary 3](/en/math/algebraic_varieties/cohomology_of_projective_spaces#cor3). In particular, for $$d \ge 0$$ we know $$h^0 = \binom{d+2}{2}$$ and $$h^1 = h^2 = 0$$, so this provides a direct example of the vanishing of $$h^1, h^2$$ mentioned above.

</div>

<div class="example" markdown="1">

<ins id="ex6">**Example 6 (Blow-up of $$\mathbb{P}^2$$)**</ins> We now consider the blow-up $$\pi: \widetilde{\mathbb{P}}^2 \to \mathbb{P}^2$$ of $$\mathbb{P}^2$$ at a point $$p$$. By [§The Canonical Bundle, ⁋Proposition 12](/en/math/algebraic_varieties/canonical_bundle#prop12), the canonical bundle is given by the formula

$$K_{\widetilde{\mathbb{P}}^2} = \pi^\ast K_{\mathbb{P}^2} + E = -3H + E$$

In $$\mathbb{P}^2$$ the hyperplane class $$H$$ can be chosen to avoid the point $$p$$, so $$H \cdot E = 0$$. On the other hand, $$E \cong \mathbb{P}^1$$, and the normal bundle $$\mathcal{N}_{E/\widetilde{\mathbb{P}}^2}$$ of $$E$$ is isomorphic to $$\mathcal{O}_{\mathbb{P}^1}(-1)$$, from which the self-intersection number $$E^2 = \deg(\mathcal{N}_{E/\widetilde{\mathbb{P}}^2}) = -1$$ follows. Geometrically this means that $$E$$ collapses to a point and "folds inward" from its surroundings, acquiring negativity. Therefore for a general divisor $$D = dH - kE$$,

$$\rchi(\mathcal{O}_{\widetilde{\mathbb{P}}^2}(dH - kE)) = \frac{1}{2}(dH - kE) \cdot (dH - kE + 3H - E) + 1 = \frac{1}{2}d(d+3) - \frac{1}{2}k(k+1) + 1$$

can be computed.

</div>

On the other hand, the Riemann–Roch theorem for curves was obtained from the above [Proposition 4](#prop4) by applying [§Serre Duality, ⁋Proposition 4](/en/math/algebraic_varieties/serre_duality#prop4) to replace the $$h^1$$ term with $$h^0$$. In the surface case as well, we can use this to write $$h^2(\mathcal{O}(D)) = h^0(\omega_S(-D))$$, and then the Riemann–Roch formula becomes

$$h^0(\mathcal{O}(D)) - h^1(\mathcal{O}(D)) + h^0(\omega_S(-D)) = \rchi(\mathcal{O}_S) + \frac{1}{2}(D^2 - D \cdot K_S)$$

In general $$h^1(\mathcal{O}(D))$$ is a term that is difficult to compute directly, but if we can assume that this value is zero or sufficiently small, we can show that at least one of $$h^0(\mathcal{O}(D))$$ and $$h^0(\omega_S(-D))$$ is sufficiently large. One powerful tool for this is the following Kodaira vanishing theorem.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7 (Kodaira Vanishing Theorem)**</ins> For a smooth projective variety $$X$$ and an ample line bundle $$L$$,

$$H^i(X, \omega_X \otimes L) = 0$$

holds for all $$i > 0$$.

</div>

The full application of the Kodaira vanishing theorem is treated in the next post. To understand the utility of this formula, let us consider two extreme cases. If $$D$$ is sufficiently "positive", i.e., $$D \cdot H$$ is sufficiently large for an ample divisor $$H$$, then $$K_S - D$$ becomes "negative" so that $$h^0(\omega_S(-D)) = 0$$ and Riemann–Roch gives a lower bound for $$h^0$$. Conversely, if $$D$$ is "sufficiently negative" then $$h^0(\mathcal{O}(D)) = 0$$ and we obtain information about $$K_S - D$$. This "symmetry between positive and negative" is a phenomenon created by Serre duality.

The Riemann–Roch calculation for $$\mathbb{P}^2$$ was already covered in [Example 5](#ex5). Here we examine another fundamental example.

<div class="example" markdown="1">

<ins id="ex8">**Example 8 ($$\mathbb{P}^1 \times \mathbb{P}^1$$)**</ins> Consider $$\mathbb{P}^1 \times \mathbb{P}^1$$. The divisor class group of this surface is $$\mathbb{Z} \oplus \mathbb{Z}$$, with the hyperplane classes $$H_1, H_2$$ of each factor as generators. Geometrically, $$H_1$$ is the "horizontal" fibers corresponding to points of the first factor, and $$H_2$$ is the "vertical" fibers corresponding to points of the second factor. Two horizontal fibers are parallel so they do not meet, hence $$H_1^2 = 0$$, and similarly $$H_2^2 = 0$$. On the other hand, a horizontal fiber and a vertical fiber always meet at one point, so $$H_1 \cdot H_2 = 1$$.

The canonical divisor is $$K = -2H_1 - 2H_2$$, which comes from the canonical divisor $$-2H$$ of $$\mathbb{P}^1$$. Meanwhile, for the Euler characteristic of the structure sheaf, using the Künneth formula,

$$\rchi(\mathcal{O}) = \rchi(\mathcal{O}_{\mathbb{P}^1}) \cdot \rchi(\mathcal{O}_{\mathbb{P}^1}) = 1 \cdot 1 = 1$$

can be verified. Although this is a result similar to [\[Algebraic Topology\] §Cohomology, ⁋Corollary 10](/en/math/algebraic_topology/cohomology#cor10), its proof involves somewhat technical aspects so we omit it. Using this, applying the Riemann–Roch formula to a divisor $$D = aH_1 + bH_2$$ of bidegree $$(a, b)$$ gives

$$\rchi(\mathcal{O}(D)) = 1 + \frac{1}{2}(D^2 - D \cdot K)$$

Here $$D^2 = (aH_1 + bH_2)^2 = 2ab$$, and $$D \cdot K = -2a - 2b$$, so

$$\rchi(\mathcal{O}(D)) = 1 + \frac{1}{2}(2ab + 2a + 2b) = (a+1)(b+1)$$

is obtained. This coincides with the number of parameters of bihomogeneous polynomials of bidegree $$(a, b)$$. For example, $$D = H_1 + H_2$$ is a curve of $$(1,1)$$-bidegree, with $$\rchi = 4$$, which is consistent with the fact that a $$(1,1)$$-curve on $$\mathbb{P}^1 \times \mathbb{P}^1$$ is equivalent to a conic.

</div>

## The Hodge index theorem

For a fixed smooth variety $$X$$, we know that the collection of divisors $$\Pic(X)$$ corresponds to $$1$$-dimensional cohomology. ([\[Algebraic Varieties\] §Sheaf Cohomology, ⁋Proposition 22](/en/math/algebraic_varieties/sheaf_cohomology#prop22)) On the other hand, since the cup product defined on cohomology is generally dual to the intersection product ([\[Algebraic Topology\] §Poincaré Duality, ⁋Example 15](/en/math/algebraic_topology/Poincare_duality#ex15)), to understand cohomology as an algebra it suffices to understand the intersection product. However, since we are investigating the case of surfaces, nontrivial elements appear only in the three dimensions $$H^0, H^1, H^2$$, and since the cup product is a graded multiplication, the only case where their product has nontrivial meaning is when $$1$$-dimensional elements are multiplied with each other, i.e., the case corresponding to the intersection product of divisors.

Therefore, by collecting divisors and examining their intersection product, we can investigate the multiplicative structure of the cohomology ring. For this purpose, we first define the following.

<div class="definition" markdown="1">

<ins id="def9">**Definition 9**</ins> Two divisors $$D_1, D_2$$ are *numerically equivalent*, written $$D_1 \equiv D_2$$, if for every divisor $$E$$ we have $$D_1 \cdot E = D_2 \cdot E$$. The set of numerical equivalence classes is denoted

$$\Num(S) = \Div(S) / \{\text{numerical equivalence}\}$$

and the quadratic form on the real vector space $$\Num(S) \otimes \mathbb{R}$$ induced by the intersection product is called the *intersection form*.

</div>

The above equivalence relation is nothing other than an equivalence class that regards elements giving the same value when taking intersection products of divisors as the same. In general, numerical equivalence is a weaker relation than linear equivalence, so two numerically equivalent divisors may not be linearly equivalent to each other.

On the other hand, the ample divisor $$H$$ corresponding to an ample line bundle ([§Linear Systems, ⁋Definition 10](/en/math/algebraic_varieties/linear_systems#def10)) plays a special role in the intersection product. This fundamentally stems from the fact that the intersection number of a (very) ample divisor and an effective divisor must be positive, which can be proved by considering the actual intersection of an effective divisor and a very ample divisor when the projective variety is embedded into projective space using the very ample divisor. Using this, we obtain the following.

<div class="proposition" markdown="1">

<ins id="prop10">**Proposition 10 (Hodge Index Theorem)**</ins> Fix a smooth projective surface $$S$$ and an ample divisor $$H$$. If a divisor $$D$$ satisfies $$D \cdot H = 0$$ and $$D \not\equiv 0$$, then $$D^2 < 0$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

First assume $$D^2 > 0$$. Using [§Cohomology of Projective Spaces, ⁋Proposition 10](/en/math/algebraic_varieties/cohomology_of_projective_spaces#prop10), we can arrange that $$H_n = D + nH$$ is very ample. Then

$$D \cdot H_n = D^2 + n(D \cdot H) = D^2 > 0$$

holds. On the other hand, by Serre duality $$h^2(\mathcal{O}(mD)) = h^0(\omega_S(-mD))$$, and for $$m \gg 0$$

$$(K_S - mD) \cdot H_n = K_S \cdot H_n - m(D \cdot H_n) = K_S \cdot H_n - mD^2 < 0$$

holds. Since we chose $$H_n$$ to be very ample, this inequality shows that $$K_S - mD$$ is not an effective divisor, i.e., $$h^0(\omega_S(-mD)) = 0$$. Now from $$\rchi(\mathcal{O}(mD)) = h^0(\mathcal{O}(mD)) - h^1(\mathcal{O}(mD)) + h^2(\mathcal{O}(mD))$$ and $$h^2 = 0$$, for $$m \gg 0$$

$$h^0(\mathcal{O}(mD)) \geq \rchi(\mathcal{O}(mD))$$

holds. But by [Proposition 4](#prop4),

$$\rchi(\mathcal{O}(mD)) = \rchi(\mathcal{O}_S) + \frac{m^2 D^2 - m D \cdot K_S}{2}$$

and since we assumed $$D^2 > 0$$, we know that $$\rchi(\mathcal{O}(mD))$$ grows without bound as $$\lvert m\rvert$$ increases. That is, for sufficiently large $$m > 0$$, $$mD$$ becomes an effective divisor, and then by the above argument $$mD \cdot H > 0$$. However, this contradicts $$D \cdot H = 0$$, so $$D^2 \leq 0$$.

We now finish the proof by showing $$D^2 \neq 0$$. Suppose to the contrary that $$D^2 = 0$$, $$D \cdot H = 0$$, and $$D \not\equiv 0$$. Since $$D \not\equiv 0$$, there exists a divisor $$E$$ with $$D \cdot E \ne 0$$. Define

$$E' = (H^2)\,E - (E \cdot H)\,H$$

Then $$E' \cdot H = (H^2)(E \cdot H) - (E \cdot H)(H^2) = 0$$, and since $$D \cdot H = 0$$,

$$D \cdot E' = (H^2)(D \cdot E) - (E \cdot H)(D \cdot H) = (H^2)(D \cdot E) \ne 0$$

holds. Now similarly to the preceding argument, set $$F_n := nD + E'$$; then $$F_n \cdot H = n(D \cdot H) + (E' \cdot H) = 0$$ and

$$F_n^2 = n^2 D^2 + 2n(D \cdot E') + E'^2 = 2n(D \cdot E') + E'^2$$

holds. Since $$D \cdot E' \ne 0$$, by choosing the sign of $$n$$ appropriately and making $$\lvert n \rvert$$ large, we can arrange $$F_n^2 > 0$$. However, since $$F_n \cdot H = 0$$, applying the preceding argument with $$D = F_n$$ would require $$F_n^2 \le 0$$, a contradiction.

</details>

From this we obtain the following corollary.

<div class="proposition" markdown="1">

<ins id="cor11">**Corollary 11**</ins> The intersection form on $$\Num(S) \otimes \mathbb{R}$$ has signature $$(1, \rho - 1)$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

For an ample divisor $$H$$ we have $$H^2 > 0$$, so the intersection form has at least one positive direction. But by [Proposition 10](#prop10), every nonzero direction orthogonal to $$H$$ has negative self-intersection, which completes the proof.

</details>

That is, there is essentially only one "positive" direction on a surface, and all other directions can be thought of as "negative" in some sense. This result leads to deep consequences in the birational geometry of surfaces, such as the uniqueness of minimal models.

## Plurigenera

In the case of curves, the genus $$g$$ completely determines the birational equivalence class of the curve. For surfaces the situation is more complicated, because birational equivalence does not preserve all dimensions of cohomology. However, the dimensions of global sections of tensor powers of the canonical bundle are birational invariants, and these values provide essential information about the birational type of the surface.

<div class="definition" markdown="1">

<ins id="def12">**Definition 12**</ins> The *$$m$$-th plurigenus* of a surface $$S$$ is

$$P_m(S) = h^0(S, \omega_S^{\otimes m})$$

</div>

Here $$\omega_S$$ is the canonical bundle defined in ([§The Canonical Bundle, ⁋Definition 5](/en/math/algebraic_varieties/canonical_bundle#def5)). In particular, for $$m = 1$$, $$P_1(S) = h^0(\omega_S) = p_g(S)$$ is the geometric genus, and the sequence of plurigenera $$\{P_m(S)\}_{m \ge 1}$$ can be said to extend this in some sense. This is an important invariant that determines the birational equivalence class of the surface.

In the next post we treat the Kodaira vanishing theorem and examine how this theorem is utilized in the computation of plurigenera and the classification of surfaces.

---

**References**

**[Hart]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[BHPV]** W. Barth, K. Hulek, C. Peters, A. Van de Ven, *Compact Complex Surfaces*, Springer, 2004.  
**[Huyb]** D. Huybrechts, *Lectures on K3 Surfaces*, Cambridge University Press, 2016.
