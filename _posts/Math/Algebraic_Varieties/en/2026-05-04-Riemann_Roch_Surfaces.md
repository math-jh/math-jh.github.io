---
title: "The Riemann–Roch Theorem for Surfaces"
description: "We define intersection numbers while generalizing the Riemann-Roch theorem from curves to surfaces, prove Hodge's index theorem and inequalities for plurigenera, and examine the geometric meaning of intersection forms."
excerpt: "Intersection theory on surfaces and its applications"

categories: [Math / Algebraic Varieties]
permalink: /en/math/algebraic_varieties/riemann_roch_surfaces
sidebar: 
    nav: "algebraic_varieties-en"

date: 2026-05-04
weight: 16
translated_at: 2026-07-14T10:00:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-07-14T10:00:02+00:00
---
We previously examined the Riemann–Roch theorem for curves. In essence, the Riemann–Roch theorem computes the Euler characteristic in terms of other numerical quantities, and although we could generalize it to arbitrary dimension, in this post we shall only discuss the generalization to surfaces.

Revisiting the Riemann–Roch formula on a curve $C$ ([§Riemann–Roch Theorem for Curves, ⁋Proposition 3](/en/math/algebraic_varieties/riemann_roch_theorem#prop3))

$$\ell(D) - \ell(K_C - D) = \deg D + 1 - g$$

we see that the left-hand side is essentially the Euler characteristic of $\mathcal{O}_C(D)$, and [§Riemann–Roch Theorem for Curves, ⁋Lemma 2](/en/math/algebraic_varieties/riemann_roch_theorem#lem2) guarantees that this side consists of only two terms. However, when we now generalize this to surfaces, the dimension of the base space increases by one, so additional terms will appear; correspondingly, the right-hand side will also acquire additional terms.

Intuitively, the term $\deg D$ appearing on the right-hand side of the above formula can be thought of as a linear term, but in the process of generalizing to surfaces we must also consider additional *quadratic terms* $D\cdot D$, $D\cdot K_S$, and so on. These quantities encode how two divisors intersect on a surface, and they arise because divisors on a curve—namely points—generally do not meet inside the curve, whereas divisors on a surface—namely curves—typically intersect in finitely many points inside the surface.

In this post we introduce the definition of the intersection number and its basic properties, rigorously derive the Riemann–Roch formula, and then use it to prove the Hodge index theorem and inequalities for plurigenera. We also examine the significance of the intersection form in the birational geometry of surfaces.

## Intersection Number

Our starting point is a definition that may appear somewhat abstract, using the Euler characteristic. The advantage of this definition is that invariance under linear equivalence follows immediately, and right after the definition we shall verify that it indeed counts intersection points.

::: Definition 1
We define the *intersection number* $C \cdot D$ of two divisors $C, D$ on a smooth surface $S$ as follows.

$$C \cdot D = \rchi(\mathcal{O}_S(C + D)) - \rchi(\mathcal{O}_S(C)) - \rchi(\mathcal{O}_S(D)) + \rchi(\mathcal{O}_S)$$
:::

To examine the geometric meaning of this, suppose $C$ and $D$ are effective divisors defined by global sections $s \in H^0(\mathcal{O}(C))$ and $t \in H^0(\mathcal{O}(D))$, respectively. Then their common zero locus is $C \cap D$, and the following exact sequence holds.

$$0 \rightarrow \mathcal{O} \xrightarrow{(t,-s)} \mathcal{O}(C) \oplus \mathcal{O}(D) \xrightarrow{(s,t)} \mathcal{O}(C+D) \rightarrow \mathcal{O}_{C \cap D} \rightarrow 0$$

Here the first arrow is $h \mapsto (ht, -hs)$, the second arrow is $(f, g) \mapsto fs + gt$, and the last arrow is the natural restriction map from $\mathcal{O}(C+D)$ to $C \cap D$. Then by additivity of the Euler characteristic,

$$C \cdot D = \rchi(\mathcal{O}_{C \cap D})$$

and in this case $C \cap D$ is the intersection of two curves, i.e., points, so the right-hand side exactly counts the number of points in $C \cap D$. A somewhat subtle point is that for this to be well defined, $C$ and $D$ must be in general position; to this end we say that two curves $C, D$ *transversally intersect* at a point $p$ if the following condition holds:

$$T_pC\oplus T_pD\cong T_pS$$

For example, in $\mathbb{A}^2$, the line $\x=0$ does not intersect itself transversally, and $\y=\x^3$ does not intersect $\y=0$ transversally. On the other hand, $\y=\x$ and $\y=-\x$ meet transversally. Moreover, this example also provides intuition for intersection multiplicity: the intersection multiplicity of $\y=\x$ and $\y=-\x$ (at the origin) is $1$, but that of $\y=\x^3$ and $\y=0$ is $3$. Then in the general case where $C$ and $D$ may not meet transversally,

$$\rchi(\mathcal{O}_{C \cap D}) = \sum_{p \in C \cap D} (C \cdot D)_p$$

holds, where $(C \cdot D)_p$ is the local intersection multiplicity at $p$. To prevent $C \cap D$ from being a curve rather than a finite set of points in this formula (for instance, to rule out the case $C = D$), we assume that $C$ and $D$ have no common component.

::: Proposition 2
The following are properties of the intersection number.

1. *Symmetry.* $C \cdot D = D \cdot C$ holds.
2. *Bilinearity.* $(aC_1 + bC_2) \cdot D = a(C_1 \cdot D) + b(C_2 \cdot D)$ holds.
3. *Linear invariance.* For two linearly equivalent divisors $C \sim C'$, $C \cdot D = C' \cdot D$ always holds.
:::

Symmetry is obvious from the intuition shown above, and linear invariance is also almost obvious. Surprisingly, the least obvious is bilinearity, which is usually explained by Snapper's theorem. By Snapper's theorem, for any coherent sheaf $\mathcal{F}$ on a projective variety and line bundles $L_1, \ldots, L_k$, the Euler characteristic

$$\rchi(\mathcal{F} \otimes L_1^{\otimes n_1} \otimes \cdots \otimes L_k^{\otimes n_k})$$

is given by a polynomial in $n_1, \ldots, n_k$. Then in particular, from the definition of the intersection number, $\rchi(\mathcal{O}_S(aC_1 + bC_2 + D))$ becomes a polynomial in $a, b$, and comparing the quadratic coefficients of this polynomial gives bilinearity.

## Riemann–Roch for Surfaces

We now have all the language needed to extend the Riemann–Roch theorem to surfaces. What we need next is the following lemma.

::: Lemma 3 (Genus formula)
For a smooth irreducible curve $D$ on a smooth projective surface $S$,

$$2g(D) - 2 = D^2 + D \cdot K_S$$

holds.
:::

::: Proof
By the adjunction formula from [§Canonical Bundle, ⁋Proposition 9](/en/math/algebraic_varieties/canonical_bundle#prop9),

$$\omega_D \cong (\omega_S \otimes \mathcal{O}_S(D))\vert_D$$

holds. Taking degrees of both sides gives

$$\deg(\omega_D) = \deg(\omega_S\vert_D) + \deg(\mathcal{O}_D(D))$$

We previously derived from the result of [§Riemann–Roch Theorem for Curves, ⁋Proposition 3](/en/math/algebraic_varieties/riemann_roch_theorem#prop3) that $\deg(\omega_D)=2g-2$, and it remains only to interpret the two terms on the right-hand side as intersection numbers. First, $\omega_S\vert_D$ is the canonical bundle restricted to $D$, which measures the intersection number of $D$ with the canonical divisor $K_S$. Specifically, since $K_S$ is the divisor corresponding to $\omega_S$, the degree of $\omega_S\vert_D$ equals the number of points that $K_S$ occupies on $D$, namely $D \cdot K_S$. Similarly, $\mathcal{O}_D(D)$ corresponds to the normal bundle $\mathcal{N}_{D/S}$, which measures the extent to which $D$ meets itself inside $S$. The degree of this bundle coincides with the self-intersection number $D^2$ of $D$. Combining these yields

$$2g(D) - 2 = D \cdot K_S + D^2$$

as desired.
:::

Then the Riemann–Roch theorem on a surface is given as follows.

::: Proposition 4 (Riemann–Roch for surfaces)
For a divisor $D$ on a smooth projective surface $S$, we have

$$\rchi(\mathcal{O}_S(D)) = \frac{1}{2} D \cdot (D - K_S) + \rchi(\mathcal{O}_S)$$

:::

::: Proof
First, consider the case where $D$ is a smooth irreducible effective divisor. From the short exact sequence

$$0 \rightarrow \mathcal{O}_S \rightarrow \mathcal{O}_S(D) \rightarrow \mathcal{O}_D(D) \rightarrow 0$$

and the additivity of the Euler characteristic, we obtain

$$\rchi(\mathcal{O}_S(D)) = \rchi(\mathcal{O}_S) + \rchi(\mathcal{O}_D(D)).$$

Now, since $\mathcal{O}_D(D)$ is a line bundle defined on $D$, by [§Riemann–Roch Theorem for Curves, ⁋Proposition 3](/en/math/algebraic_varieties/riemann_roch_theorem#prop3),

$$\rchi(\mathcal{O}_D(D)) = D^2 + 1 - g(D).$$

From the preceding [Lemma 3](#lem3),

$$g(D) = \frac{1}{2}(D^2 + D \cdot K_S) + 1,$$

so substituting this gives

$$\rchi(\mathcal{O}_D(D)) = D^2 + 1 - \frac{1}{2}(D^2 + D \cdot K_S) - 1 = \frac{1}{2}D \cdot (D - K_S).$$

Therefore, we obtain

$$\rchi(\mathcal{O}_S(D)) = \rchi(\mathcal{O}_S) + \frac{1}{2}D \cdot (D - K_S).$$

Now we must generalize this to an arbitrary divisor $D$. First, fix an ample divisor $H$ on $S$. Then by [§Cohomology of Projective Spaces, ⁋Proposition 4](/en/math/algebraic_varieties/cohomology_of_projective_spaces#prop4), for sufficiently large $n$,

$$H^1(S, \mathcal{O}_S(D + nH)) = H^2(S, \mathcal{O}_S(D + nH)) = 0.$$

Hence,

$$\rchi(\mathcal{O}_S(D + nH)) = h^0(\mathcal{O}_S(D + nH)).$$

On the other hand, since $D + nH$ is an effective divisor, the desired equality holds for $D + nH$ by the preceding argument. Therefore, considering the two functions of $n$, $f(n) = \rchi(\mathcal{O}(D+nH))$ and $g(n) = \frac{1}{2}(D+nH)\cdot(D+nH-K_S) + \rchi(\mathcal{O}_S)$, they agree for all sufficiently large $n$. However, by Snapper's theorem mentioned earlier, $\rchi(\mathcal{O}_S(D+nH))$ is a polynomial in $n$, and two polynomials that agree at infinitely many points are equal; thus $f$ and $g$ are in fact the same polynomial. That is, $f(n) = g(n)$ for all $n$, and in particular substituting $n = 0$ yields

$$\rchi(\mathcal{O}(D)) = \frac{1}{2}D\cdot(D-K_S) + \rchi(\mathcal{O}_S).$$

:::

As in the case of curves, if $D$ is sufficiently "positive," then $h^1$ and $h^2$ vanish and $\rchi(\mathcal{O}_S(D)) = h^0(S, \mathcal{O}_S(D))$. This is closely related to the notion of ampleness defined in [§Linear Systems, ⁋Definition 10](/en/math/algebraic_varieties/linear_systems#def10).

::: Example 5 ($\mathbb{P}^2$)
Fixing the hyperplane class $H$ on $\mathbb{P}^2$, we know that

$$K_{\mathbb{P}^2} = -3H, \qquad \rchi(\mathcal{O}_{\mathbb{P}^2}) = 1$$

([§Canonical Bundle, ⁋Proposition 7](/en/math/algebraic_varieties/canonical_bundle#prop7), [§Cohomology of Projective Spaces, ⁋Corollary 3](/en/math/algebraic_varieties/cohomology_of_projective_spaces#cor3)). Since any two lines in $\mathbb{P}^2$ generally meet at a single point, the self-intersection number of $H$ is $1$, and therefore for any divisor $D = dH$ we have

$$\rchi(\mathcal{O}_{\mathbb{P}^2}(d)) = \frac{1}{2}dH \cdot (dH + 3H) + 1 = \frac{1}{2}d(d+3) + 1$$

This identity is indeed a consequence of [§Cohomology of Projective Spaces, ⁋Corollary 3](/en/math/algebraic_varieties/cohomology_of_projective_spaces#cor3). In particular, for $d \ge 0$ we know that $h^0 = \binom{d+2}{2}$ and $h^1 = h^2 = 0$, which provides a direct example of the vanishing of $h^1, h^2$ mentioned above.
:::

::: Example 6 (Blow-up of $\mathbb{P}^2$)
Now we consider the blow-up $\pi: \widetilde{\mathbb{P}}^2 \rightarrow \mathbb{P}^2$ of $\mathbb{P}^2$ at a point $p$. By [§Canonical Bundle, ⁋Proposition 12](/en/math/algebraic_varieties/canonical_bundle#prop12), the canonical bundle is given by the formula

$$K_{\widetilde{\mathbb{P}}^2} = \pi^\ast K_{\mathbb{P}^2} + E = -3H + E$$

In $\mathbb{P}^2$, the hyperplane class $H$ can be chosen to avoid the point $p$, so $H \cdot E = 0$. On the other hand, $E \cong \mathbb{P}^1$, and the normal bundle $\mathcal{N}_{E/\widetilde{\mathbb{P}}^2}$ of $E$ is isomorphic to $\mathcal{O}_{\mathbb{P}^1}(-1)$, from which the self-intersection number $E^2 = \deg(\mathcal{N}_{E/\widetilde{\mathbb{P}}^2}) = -1$ follows; geometrically, this means that as $E$ collapses to a point, it "folds inward" in its neighborhood, acquiring negativity. Thus for a general divisor $D = dH - kE$, we can compute

$$\rchi(\mathcal{O}_{\widetilde{\mathbb{P}}^2}(dH - kE)) = \frac{1}{2}(dH - kE) \cdot (dH - kE + 3H - E) + 1 = \frac{1}{2}d(d+3) - \frac{1}{2}k(k+1) + 1$$

:::

Meanwhile, the Riemann–Roch theorem for curves is obtained by applying [§Serre Duality](/en/math/algebraic_varieties/serre_duality) to the $h^1$ term in [Proposition 4](#prop4) above and replacing it with $h^0$. In the surface case, we can likewise use this to write $h^2(\mathcal{O}(D)) = h^0(\omega_S(-D))$, so the Riemann–Roch formula becomes

$$h^0(\mathcal{O}(D)) - h^1(\mathcal{O}(D)) + h^0(\omega_S(-D)) = \rchi(\mathcal{O}_S) + \frac{1}{2}(D^2 - D \cdot K_S)$$

In general, $h^1(\mathcal{O}(D))$ is a term that is difficult to compute directly; however, if we can assume that this value is zero or sufficiently small, we can show that at least one of $h^0(\mathcal{O}(D))$ and $h^0(\omega_S(-D))$ is sufficiently large. One of the powerful tools for this is the following Kodaira vanishing theorem.

::: Proposition 7 (Kodaira Vanishing Theorem)
For a smooth projective variety $X$ and an ample line bundle $L$,

$$H^i(X, \omega_X \otimes L) = 0$$

holds for all $i > 0$.
:::

The full-fledged applications of the Kodaira vanishing theorem will be discussed in the next post. To understand the usefulness of this formula, let us consider two extreme cases. If $D$ is "sufficiently positive," that is, $D \cdot H$ is large enough for an ample divisor $H$, then $K_S - D$ becomes "negative" and we have $h^0(\omega_S(-D)) = 0$, so Riemann–Roch gives a lower bound for $h^0$. Conversely, if $D$ is "sufficiently negative," then $h^0(\mathcal{O}(D)) = 0$ and we obtain information about $K_S - D$. This "symmetry between positive and negative" is a phenomenon created by Serre duality.

The Riemann–Roch computation for $\mathbb{P}^2$ was already covered in [Example 5](#ex5). Here we examine another fundamental example.

::: Example 8 ($\mathbb{P}^1 \times \mathbb{P}^1$)
Consider $\mathbb{P}^1 \times \mathbb{P}^1$. The divisor class group of this surface is $\mathbb{Z} \oplus \mathbb{Z}$, and the hyperplane classes $H_1, H_2$ from each factor are generators; geometrically, these correspond to attaching copies of $\mathbb{P}^1$ while fixing the first and second factors respectively. That is, $H_1$ consists of "horizontal" fibers corresponding to points of the first factor, and $H_2$ consists of "vertical" fibers corresponding to points of the second factor. Two horizontal fibers are parallel and hence do not meet, so $H_1^2 = 0$, and similarly $H_2^2 = 0$. On the other hand, a horizontal fiber and a vertical fiber always meet at a single point, so $H_1 \cdot H_2 = 1$.

The canonical divisor is $K = -2H_1 - 2H_2$, which comes from the canonical divisor $-2H$ on $\mathbb{P}^1$. For the Euler characteristic of the structure sheaf, using the Künneth formula we can verify that

$$\rchi(\mathcal{O}) = \rchi(\mathcal{O}_{\mathbb{P}^1}) \cdot \rchi(\mathcal{O}_{\mathbb{P}^1}) = 1 \cdot 1 = 1.$$

This is analogous to a result in [[Algebraic Topology] §Cohomology, ⁋Corollary 10](/en/math/algebraic_topology/cohomology#cor10), but its proof involves somewhat technical details, so we omit it. Now applying the Riemann–Roch formula to a divisor $D = aH_1 + bH_2$ of bidegree $(a, b)$, we obtain

$$\rchi(\mathcal{O}(D)) = 1 + \frac{1}{2}(D^2 - D \cdot K).$$

Here $D^2 = (aH_1 + bH_2)^2 = 2ab$ and $D \cdot K = -2a - 2b$, so we get

$$\rchi(\mathcal{O}(D)) = 1 + \frac{1}{2}(2ab + 2a + 2b) = (a+1)(b+1).$$

This agrees with the number of parameters of a bihomogeneous polynomial of bidegree $(a, b)$. For example, $D = H_1 + H_2$ is a curve of $(1,1)$-bidegree with $\rchi = 4$, which is consistent with the fact that a $(1,1)$-curve on $\mathbb{P}^1 \times \mathbb{P}^1$ is equivalent to a conic.
:::

## Hodge Index Theorem

For a fixed smooth variety $X$, we know that the collection of divisors $\Pic(X)$ corresponds to $1$-dimensional cohomology. ([§Sheaf Cohomology, ⁋Proposition 22](/en/math/algebraic_varieties/sheaf_cohomology#prop22)) On the other hand, the cup product defined on cohomology is generally dual to the intersection product ([[Algebraic Topology] §Poincaré Duality, ⁋Example 16](/en/math/algebraic_topology/Poincare_duality#ex16)), so to understand cohomology as an algebra it suffices to understand the intersection product. Since we are investigating the case of surfaces, nontrivial elements appear only in the three dimensions $H^0, H^1, H^2$, and because the cup product is a graded multiplication, the only case where their product has nontrivial meaning is when $1$-dimensional elements are multiplied with each other, that is, the case corresponding to the intersection product of divisors.

Therefore, we may collect the divisors and examine their intersection product to study the multiplicative structure of the cohomology ring. To this end, we first define the following.

::: Definition 9
Two divisors $D_1, D_2$ are *numerically equivalent*, written $D_1 \equiv D_2$, if $D_1 \cdot E = D_2 \cdot E$ for every divisor $E$. We denote the set of numerical equivalence classes by

$$\Num(S) = \Div(S) / \{\text{numerical equivalence}\}$$

and call the quadratic form induced by the intersection product on the real vector space $\Num(S) \otimes \mathbb{R}$ the *intersection form*.
:::

The above equivalence relation is nothing deep: it is merely the equivalence class that regards elements giving the same value when taking intersection products of divisors as the same. In general, numerical equivalence is a weaker relation than linear equivalence, so two numerically equivalent divisors need not be linearly equivalent.

On the other hand, an ample divisor $H$ corresponding to an ample line bundle ([§Linear Systems, ⁋Definition 10](/en/math/algebraic_varieties/linear_systems#def10)) plays a special role in the intersection product. This ultimately stems from the fact that the intersection number of a (very) ample divisor with an effective divisor is always positive, which can be proved by thinking of the actual intersection of an effective divisor with a very ample divisor after embedding the projective variety into projective space via the very ample divisor. Using this, we obtain the following.

::: Proposition 10 (Hodge Index Theorem)
Fix a smooth projective surface $S$ and an ample divisor $H$. If a divisor $D$ satisfies $D \cdot H = 0$ and $D \not\equiv 0$, then $D^2 < 0$.
:::

::: Proof
First assume $D^2 > 0$. Using [§Cohomology of Projective Spaces, ⁋Proposition 10](/en/math/algebraic_varieties/cohomology_of_projective_spaces#prop10), we can arrange that $H_n = D + nH$ is very ample. Then

$$D \cdot H_n = D^2 + n(D \cdot H) = D^2 > 0$$

On the other hand, by Serre duality $h^2(\mathcal{O}(mD)) = h^0(\omega_S(-mD))$, and for $m \gg 0$

$$(K_S - mD) \cdot H_n = K_S \cdot H_n - m(D \cdot H_n) = K_S \cdot H_n - mD^2 < 0$$

Since we chose $H_n$ to be very ample, this inequality shows that $K_S - mD$ is not an effective divisor. That is, $h^0(\omega_S(-mD)) = 0$. Now from $\rchi(\mathcal{O}(mD)) = h^0(\mathcal{O}(mD)) - h^1(\mathcal{O}(mD)) + h^2(\mathcal{O}(mD))$ and $h^2 = 0$, for $m \gg 0$

$$h^0(\mathcal{O}(mD)) \geq \rchi(\mathcal{O}(mD))$$

But by [Proposition 4](#prop4)

$$\rchi(\mathcal{O}(mD)) = \rchi(\mathcal{O}_S) + \frac{m^2 D^2 - m D \cdot K_S}{2}$$

and since we assumed $D^2 > 0$, we know that $\rchi(\mathcal{O}(mD))$ grows without bound as $\lvert m\rvert$ becomes large. Thus for sufficiently large $m > 0$, the divisor $mD$ becomes effective, and then by the above discussion $mD \cdot H > 0$. However, this contradicts $D \cdot H = 0$, and therefore $D^2 \leq 0$.

We now finish the proof by showing $D^2 \neq 0$. Suppose, to the contrary, that $D^2 = 0$, $D \cdot H = 0$, and $D \not\equiv 0$. Since $D \not\equiv 0$, there exists some divisor $E$ with $D \cdot E \ne 0$. Define

$$E' = (H^2)\,E - (E \cdot H)\,H$$

Then $E' \cdot H = (H^2)(E \cdot H) - (E \cdot H)(H^2) = 0$, and since $D \cdot H = 0$

$$D \cdot E' = (H^2)(D \cdot E) - (E \cdot H)(D \cdot H) = (H^2)(D \cdot E) \ne 0$$

Now similarly to the previous argument, set $F_n := nD + E'$. Then $F_n \cdot H = n(D \cdot H) + (E' \cdot H) = 0$ and

$$F_n^2 = n^2 D^2 + 2n(D \cdot E') + E'^2 = 2n(D \cdot E') + E'^2$$

Since $D \cdot E' \ne 0$, by choosing the sign of $n$ appropriately and making $\lvert n \rvert$ large, we can arrange $F_n^2 > 0$. But $F_n \cdot H = 0$, so applying the previous argument with $D = F_n$ would require $F_n^2 \le 0$, a contradiction.
:::

From this we obtain the following corollary.

::: Corollary 11
The intersection form on $\Num(S) \otimes \mathbb{R}$ has signature $(1, \rho - 1)$.
:::

::: Proof
For an ample divisor $H$ we have $H^2 > 0$, so the intersection form has at least one positive direction. But by [Proposition 10](#prop10), every nonzero direction orthogonal to $H$ has negative self-intersection, which completes the proof.
:::

Thus there is essentially only one "positive" direction on a surface, and every other direction can be thought of as "negative" in a certain sense. This result leads to deep consequences in the birational geometry of surfaces, such as the uniqueness of the minimal model.

## Plurigenera

In the case of curves, the genus $g$ completely determines the birational equivalence class of a curve. For surfaces the situation is more complicated, because birational equivalence does not preserve all cohomological dimensions. However, the dimensions of global sections of tensor powers of the canonical bundle are birational invariants, and these values provide essential information about the birational type of a surface.

::: Definition 12
The *$m$-th plurigenus* of a surface $S$ is

$$P_m(S) = h^0(S, \omega_S^{\otimes m})$$

:::

Here $\omega_S$ is the canonical bundle defined in [§Canonical Bundle, ⁋Definition 5](/en/math/algebraic_varieties/canonical_bundle#def5). In particular, when $m = 1$, we have $P_1(S) = h^0(\omega_S) = p_g(S)$, the geometric genus; the sequence of plurigenera $\{P_m(S)\}_{m \ge 1}$ can be thought of as an extension of this in a certain sense. It is an important invariant that determines the birational equivalence class of a surface.

In the next post we will discuss the Kodaira vanishing theorem and see how this theorem is used in the computation of plurigenera and the classification of surfaces.

---

**References**

**[Hart]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[BHPV]** W. Barth, K. Hulek, C. Peters, A. Van de Ven, *Compact Complex Surfaces*, Springer, 2004.  
**[Huyb]** D. Huybrechts, *Lectures on K3 Surfaces*, Cambridge University Press, 2016.
