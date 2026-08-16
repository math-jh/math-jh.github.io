---
title: "The Riemann–Roch Theorem for Surfaces"
description: "We define intersection numbers while generalizing the Riemann–Roch theorem from curves to surfaces, prove the Hodge index theorem and an inequality for plurigenera, and examine the geometric meaning of the intersection form."
excerpt: "Intersection theory on surfaces and its applications"

categories: [Math / Algebraic Varieties]
permalink: /en/math/algebraic_varieties/riemann_roch_surfaces
sidebar: 
    nav: "algebraic_varieties-en"

date: 2026-05-04
weight: 17
translated_at: 2026-08-16T03:18:56+00:00
translation_source: kimi-cli
---
We previously examined the Riemann-Roch theorem for curves. In essence, the Riemann-Roch theorem computes the Euler characteristic in terms of other quantitative invariants, and although we could generalize it to arbitrary dimensions, in this post we shall only treat the generalization to surfaces.

Revisiting the Riemann-Roch formula for a curve $C$ ([§The Riemann–Roch Theorem for Curves, ⁋Proposition 3](/en/math/algebraic_varieties/riemann_roch_theorem#prop3))

$$\ell(D) - \ell(K_C - D) = \deg D + 1 - g$$

we see that the left-hand side is essentially the Euler characteristic of $\mathcal{O}_C(D)$, and [§The Riemann–Roch Theorem for Curves, ⁋Lemma 2](/en/math/algebraic_varieties/riemann_roch_theorem#lem2) guarantees that this part consists of only two terms. However, when we generalize this to surfaces, the dimension of the base space increases by one, so additional terms will appear, and correspondingly the right-hand side will also acquire extra terms.

Intuitively, the term $\deg D$ appearing on the right-hand side of the above formula may be thought of as a linear term, but in the process of generalizing to surfaces we must consider additional *quadratic terms* such as $D\cdot D$, $D\cdot K_S$, etc. These encode how much two divisors on a surface intersect each other, and they arise because divisors on a curve, namely points, generally do not meet inside the curve, whereas divisors on a surface, namely curves, generally intersect in finitely many points inside the surface.

In this post we cover the definition of intersection number and its basic properties, then rigorously derive the Riemann–Roch formula and use it to prove the Hodge index theorem. We also examine the meaning of the intersection form in the birational geometry of surfaces, and define the birational invariant plurigenera.

## Intersection Number

Our starting point is a definition that may appear somewhat abstract, using the Euler characteristic. The advantage of this definition is that invariance under linear equivalence follows immediately, and right after the definition we shall verify that it indeed counts intersection points.

::: Definition 1
For two divisors $C, D$ on a smooth projective surface $S$, we define the *intersection number* $C \cdot D$ as follows.

$$C \cdot D = \rchi(\mathcal{O}_S(C + D)) - \rchi(\mathcal{O}_S(C)) - \rchi(\mathcal{O}_S(D)) + \rchi(\mathcal{O}_S)$$
:::

To examine their geometric meaning, suppose that $C$ and $D$ are effective divisors defined by global sections $s \in H^0(\mathcal{O}(C))$, $t \in H^0(\mathcal{O}(D))$ respectively. Then their common zero locus is $C \cap D$, and the following exact sequence holds.

$$0 \rightarrow \mathcal{O} \xrightarrow{(t,-s)} \mathcal{O}(D) \oplus \mathcal{O}(C) \xrightarrow{(s,t)} \mathcal{O}(C+D) \rightarrow \mathcal{O}_{C \cap D} \rightarrow 0$$

Here the first arrow is $h \mapsto (ht, -hs)$, the second arrow is $(f, g) \mapsto fs + gt$, and the last arrow is the natural restriction map from $\mathcal{O}(C+D)$ onto $C \cap D$. Then by additivity of the Euler characteristic

$$C \cdot D = \rchi(\mathcal{O}_{C \cap D})$$

and in this case $C\cap D$ is the intersection of two curves, namely points, so the Euler characteristic on the right-hand side exactly counts the number of points of $C\cap D$. A somewhat subtle point is that for this to be well defined, $C$ and $D$ must be in general position; for this purpose we define that two curves $C, D$ *transversally intersect* at a point $p$ by the condition

$$T_pC\oplus T_pD = T_pS$$

where $T_pC$ and $T_pD$ are regarded as subspaces of $T_pS$, so the above condition means the internal direct sum inside $T_pS$, that is, $T_pC + T_pD = T_pS$ while $T_pC\cap T_pD = 0$. For example, in $\mathbb{A}^2$, the line $\x=0$ does not intersect itself transversally, and $\y=\x^3$ does not intersect $\y=0$ transversally. On the other hand, $\y=\x$ and $\y=-\x$ meet transversally. Moreover, this example also provides intuition for intersection multiplicity: the intersection multiplicity of $\y=\x$ and $\y=-\x$ (at the origin) is $1$, but that of $\y=\x^3$ and $\y=0$ is $3$. Then in the general case where $C$ and $D$ may not meet transversally,

$$\rchi(\mathcal{O}_{C \cap D}) = \sum_{p \in C \cap D} (C \cdot D)_p$$

holds, where $(C \cdot D)_p$ is the local intersection multiplicity at $p$. To prevent $C\cap D$ from being a curve instead of a finite set of points in this formula (for instance, to avoid the situation $C=D$), we assume that $C$ and $D$ share no common component.

::: Proposition 2
For divisors on a smooth projective surface $S$, the following are properties of the intersection number.

1. *Symmetry.* $C \cdot D = D \cdot C$ holds.
2. *Bilinearity.* $(aC_1 + bC_2) \cdot D = a(C_1 \cdot D) + b(C_2 \cdot D)$ holds.
3. *Linear invariance.* For two linearly equivalent divisors $C \sim C'$, we always have $C \cdot D = C' \cdot D$.
:::

Symmetry follows immediately from the fact that the formula in [Definition 1](#def1) is symmetric under exchanging $C$ and $D$, and linear invariance also follows because if $C\sim C'$ then $\mathcal{O}_S(C)\cong\mathcal{O}_S(C')$ and $\mathcal{O}_S(C+D)\cong\mathcal{O}_S(C'+D)$, so the four terms appearing in the definition match respectively. Perhaps the least trivial is bilinearity, which is usually explained by Snapper's theorem. By Snapper's theorem, for any coherent sheaf $\mathcal{F}$ on a projective variety and line bundles $L_1, \ldots, L_k$, the Euler characteristic

$$\rchi(\mathcal{F} \otimes L_1^{\otimes n_1} \otimes \cdots \otimes L_k^{\otimes n_k})$$

is given by a polynomial in $n_1, \ldots, n_k$. Then in particular $\rchi(\mathcal{O}_S(aC_1 + bC_2 + D))$ becomes a polynomial in $a, b$, and bilinearity is obtained by comparing the quadratic coefficients of this polynomial.

## Riemann–Roch Theorem for Surfaces

We now have all the language needed to extend the Riemann-Roch theorem to surfaces. Before that, let us establish the following identity which interprets the intersection number as the degree of a line bundle on a curve. For a smooth irreducible curve $D$ on $S$ and any divisor $C$,

$$\deg(\mathcal{O}_S(C)\vert_D) = C \cdot D$$

holds. Indeed, since $D$ is an effective divisor, multiplying by a section of $\mathcal{O}_S(D)$ defining $D$ yields the short exact sequence

$$0 \rightarrow \mathcal{O}_S(C) \rightarrow \mathcal{O}_S(C+D) \rightarrow \mathcal{O}_S(C+D)\vert_D \rightarrow 0$$

and by additivity of the Euler characteristic $\rchi(\mathcal{O}_S(C+D)\vert_D) = \rchi(\mathcal{O}_S(C+D)) - \rchi(\mathcal{O}_S(C))$. Subtracting the case $C=0$, the right-hand side becomes exactly $C \cdot D$ by [Definition 1](#def1), and applying [§The Riemann–Roch Theorem for Curves, ⁋Proposition 3](/en/math/algebraic_varieties/riemann_roch_theorem#prop3) to line bundles on $D$, the left-hand side becomes

$$\big(\deg(\mathcal{O}_S(C+D)\vert_D) + 1 - g(D)\big) - \big(\deg(\mathcal{O}_S(D)\vert_D) + 1 - g(D)\big) = \deg(\mathcal{O}_S(C)\vert_D)$$

so the desired identity follows. What we need next is the following lemma.

::: Lemma 3 (Genus formula)
For a smooth irreducible curve $D$ on a smooth projective surface $S$,

$$2g(D) - 2 = D^2 + D \cdot K_S$$

holds.
:::

::: Proof
By the adjunction formula of [§Canonical Line Bundle, ⁋Proposition 9](/en/math/algebraic_varieties/canonical_bundle#prop9),

$$\omega_D \cong (\omega_S \otimes \mathcal{O}_S(D))\vert_D$$

Taking degrees of both sides,

$$\deg(\omega_D) = \deg(\omega_S\vert_D) + \deg(\mathcal{O}_D(D))$$

We previously derived $\deg(\omega_D)=2g-2$ as a consequence of [§The Riemann–Roch Theorem for Curves, ⁋Proposition 3](/en/math/algebraic_varieties/riemann_roch_theorem#prop3), and we only need to interpret the two terms on the right-hand side as intersection numbers. First, since the divisor corresponding to $\omega_S$ is the canonical divisor $K_S$, we have $\omega_S\vert_D = \mathcal{O}_S(K_S)\vert_D$, so substituting $C=K_S$ into the previously established identity gives $\deg(\omega_S\vert_D) = K_S \cdot D$. Similarly, since $\mathcal{O}_D(D) = \mathcal{O}_S(D)\vert_D$, substituting $C=D$ into the same identity yields $\deg(\mathcal{O}_D(D)) = D^2$. The latter is also the degree of the normal bundle $\mathcal{N}_{D/S}$ of $D$, and geometrically this measures how much $D$ meets itself inside $S$. Combining these,

$$2g(D) - 2 = D \cdot K_S + D^2$$

is obtained.
:::

Then the Riemann-Roch theorem on a surface is given as follows.

::: Proposition 4 (Riemann–Roch for surfaces)
For a divisor $D$ on a smooth projective surface $S$,

$$\rchi(\mathcal{O}_S(D)) = \frac{1}{2} D \cdot (D - K_S) + \rchi(\mathcal{O}_S)$$

holds.
:::

::: Proof
First consider the case where $D$ is a smooth irreducible effective divisor. From the short exact sequence

$$0 \rightarrow \mathcal{O}_S \rightarrow \mathcal{O}_S(D) \rightarrow \mathcal{O}_D(D) \rightarrow 0$$

additivity of the Euler characteristic gives

$$\rchi(\mathcal{O}_S(D)) = \rchi(\mathcal{O}_S) + \rchi(\mathcal{O}_D(D))$$

Now, since $\mathcal{O}_D(D)$ is a line bundle on $D$, by [§The Riemann–Roch Theorem for Curves, ⁋Proposition 3](/en/math/algebraic_varieties/riemann_roch_theorem#prop3),

$$\rchi(\mathcal{O}_D(D)) = D^2 + 1 - g(D)$$

From the preceding [Lemma 3](#lem3),

$$g(D) = \frac{1}{2}(D^2 + D \cdot K_S) + 1$$

so substituting this gives

$$\rchi(\mathcal{O}_D(D)) = D^2 + 1 - \frac{1}{2}(D^2 + D \cdot K_S) - 1 = \frac{1}{2}D \cdot (D - K_S)$$

Therefore

$$\rchi(\mathcal{O}_S(D)) = \rchi(\mathcal{O}_S) + \frac{1}{2}D \cdot (D - K_S)$$

is obtained.

We now need to generalize this to a general divisor $D$. First fix an ample divisor $H$ on $S$. Then by [§Cohomology of Projective Space, ⁋Proposition 7](/en/math/algebraic_varieties/cohomology_of_projective_spaces#prop7), for sufficiently large $n$,

$$H^1(S, \mathcal{O}_S(D + nH)) = H^2(S, \mathcal{O}_S(D + nH)) = 0$$

Hence

$$\rchi(\mathcal{O}_S(D + nH)) = h^0(\mathcal{O}_S(D + nH))$$

holds. On the other hand, by taking $n$ even larger, [§Cohomology of Projective Space, ⁋Proposition 13](/en/math/algebraic_varieties/cohomology_of_projective_spaces#prop13) allows us to make $D+nH$ very ample, so the linear system $\lvert D+nH\rvert$ is non-empty. Then by Bertini's theorem, a general element $D'$ of this linear system is a smooth irreducible curve, and since $D' \sim D+nH$, we have $\mathcal{O}_S(D')\cong\mathcal{O}_S(D+nH)$, so the Euler characteristics of the two divisors are equal, and by linear invariance from [Proposition 2](#prop2) their intersection numbers are also equal. Thus applying the previous argument to $D'$, the desired identity also holds for $D+nH$. Now consider the two functions in $n$, $f(n) = \rchi(\mathcal{O}(D+nH))$ and $g(n) = \frac{1}{2}(D+nH)\cdot(D+nH-K_S) + \rchi(\mathcal{O}_S)$; these agree for all sufficiently large $n$. But by Snapper's theorem mentioned earlier, $\rchi(\mathcal{O}_S(D+nH))$ is a polynomial in $n$, and polynomials that agree at infinitely many points are identical. That is, $f(n) = g(n)$ for all $n$, and in particular substituting $n = 0$ gives

$$\rchi(\mathcal{O}(D)) = \frac{1}{2}D\cdot(D-K_S) + \rchi(\mathcal{O}_S)$$
:::

As in the curve case, if $D$ is sufficiently "positive" then $h^1$ and $h^2$ vanish and $\rchi(\mathcal{O}_S(D)) = h^0(S, \mathcal{O}_S(D))$. This is closely related to the notion of ampleness defined in [§Linear Systems, ⁋Definition 10](/en/math/algebraic_varieties/linear_systems#def10).

::: Example 5 ($\mathbb{P}^2$)
Fix the hyperplane class $H$ in $\mathbb{P}^2$; we know

$$K_{\mathbb{P}^2} = -3H, \qquad \rchi(\mathcal{O}_{\mathbb{P}^2}) = 1$$

([§Canonical Line Bundle, §§The Canonical Bundle of $\mathbb{P}^n$](/en/math/algebraic_varieties/canonical_bundle#the-canonical-bundle-of-mathbbpn), [§Cohomology of Projective Space, ⁋Corollary 3](/en/math/algebraic_varieties/cohomology_of_projective_spaces#cor3)) Since any two lines in $\mathbb{P}^2$ generally meet at one point, the self-intersection number of $H$ is $1$, and thus for any divisor $D = dH$,

$$\rchi(\mathcal{O}_{\mathbb{P}^2}(d)) = \frac{1}{2}dH \cdot (dH + 3H) + 1 = \frac{1}{2}d(d+3) + 1$$

holds. That this actually holds is a consequence of [§Cohomology of Projective Space, ⁋Corollary 3](/en/math/algebraic_varieties/cohomology_of_projective_spaces#cor3). In particular, for $d \ge 0$ we know $h^0 = \binom{d+2}{2}$ and $h^1 = h^2 = 0$, so this provides a direct example of the vanishing of $h^1, h^2$ mentioned above.
:::

::: Example 6 (Blow-up of $\mathbb{P}^2$)
Now consider the blow-up $\pi: \widetilde{\mathbb{P}}^2 \rightarrow \mathbb{P}^2$ at a point $p$ of $\mathbb{P}^2$. By [§Canonical Line Bundle, ⁋Proposition 12](/en/math/algebraic_varieties/canonical_bundle#prop12), the canonical bundle is given by the formula

$$K_{\widetilde{\mathbb{P}}^2} = \pi^\ast K_{\mathbb{P}^2} + E = -3H + E$$

In $\mathbb{P}^2$ we can choose the hyperplane class $H$ to avoid the point $p$, so $H \cdot E = 0$. On the other hand $E \cong \mathbb{P}^1$, and the normal bundle $\mathcal{N}_{E/\widetilde{\mathbb{P}}^2}$ of $E$ is isomorphic to $\mathcal{O}_{\mathbb{P}^1}(-1)$, from which the self-intersection number $E^2 = \deg(\mathcal{N}_{E/\widetilde{\mathbb{P}}^2}) = -1$ follows; geometrically this means that as $E$ collapses to a point, it "folds inward" from its surroundings and acquires negativity. Therefore for a general divisor $D = dH - kE$,

$$\rchi(\mathcal{O}_{\widetilde{\mathbb{P}}^2}(dH - kE)) = \frac{1}{2}(dH - kE) \cdot (dH - kE + 3H - E) + 1 = \frac{1}{2}d(d+3) - \frac{1}{2}k(k+1) + 1$$

can be computed.
:::

Meanwhile, just as the Riemann-Roch theorem for curves was an expression using the Euler characteristic to which [§Serre Duality](/en/math/algebraic_varieties/serre_duality) was applied to replace the $h^1$ term by $h^0$, on a surface we can also apply this to the above [Proposition 4](#prop4) to write $h^2(\mathcal{O}(D)) = h^0(\omega_S(-D))$, and then the Riemann–Roch formula becomes

$$h^0(\mathcal{O}(D)) - h^1(\mathcal{O}(D)) + h^0(\omega_S(-D)) = \rchi(\mathcal{O}_S) + \frac{1}{2}(D^2 - D \cdot K_S)$$

In general $h^1(\mathcal{O}(D))$ is a term that is difficult to compute directly, but if we can assume that this value is $0$ or sufficiently small, then we can show that at least one of $h^0(\mathcal{O}(D))$ and $h^0(\omega_S(-D))$ is sufficiently large. One powerful tool for this is the following Kodaira vanishing theorem.

::: Proposition 7 (Kodaira Vanishing Theorem)
For a smooth projective variety $X$ and an ample line bundle $L$,

$$H^i(X, \omega_X \otimes L) = 0$$

holds for all $i > 0$.
:::

The serious applications of the Kodaira vanishing theorem are treated in the next post. To understand the usefulness of this formula, let us consider two extreme cases. If $D$ is "sufficiently positive", that is, if $D \cdot H$ is sufficiently large for an ample divisor $H$, then $K_S - D$ becomes "negative" and $h^0(\omega_S(-D)) = 0$, so Riemann–Roch gives a lower bound for $h^0$. Conversely, if $D$ is "sufficiently negative" then $h^0(\mathcal{O}(D)) = 0$ and we obtain information about $K_S - D$. This "symmetry between positive and negative" is a phenomenon created by Serre duality.

The Riemann–Roch computation for $\mathbb{P}^2$ was already treated in [Example 5](#ex5). Here we examine another fundamental example.

::: Example 8 ($\mathbb{P}^1 \times \mathbb{P}^1$)
Consider $\mathbb{P}^1 \times \mathbb{P}^1$. The divisor class group of this surface is $\mathbb{Z} \oplus \mathbb{Z}$, with the hyperplane classes $H_1, H_2$ of each factor as generators; geometrically these are copies of $\mathbb{P}^1$ attached by fixing the first and second factors respectively. That is, geometrically $H_1$ consists of "horizontal" fibers corresponding to points of the first factor, and $H_2$ consists of "vertical" fibers corresponding to points of the second factor. Two horizontal fibers are parallel so they do not meet, hence $H_1^2 = 0$, and similarly $H_2^2 = 0$. On the other hand, a horizontal fiber and a vertical fiber always meet at one point, so $H_1 \cdot H_2 = 1$.

The canonical divisor is $K = -2H_1 - 2H_2$, which comes from the canonical divisor $-2H$ of $\mathbb{P}^1$. For the Euler characteristic of the structure sheaf, using the Künneth formula,

$$\rchi(\mathcal{O}) = \rchi(\mathcal{O}_{\mathbb{P}^1}) \cdot \rchi(\mathcal{O}_{\mathbb{P}^1}) = 1 \cdot 1 = 1$$

can be verified. This is a result similar to [\[Algebraic Topology\] §Cohomology, ⁋Corollary 10](/en/math/algebraic_topology/cohomology#cor10), but its proof involves somewhat technical aspects so we omit it. Now applying the Riemann–Roch formula to a divisor $D = aH_1 + bH_2$ of bidegree $(a, b)$,

$$\rchi(\mathcal{O}(D)) = 1 + \frac{1}{2}(D^2 - D \cdot K)$$

is obtained. Here $D^2 = (aH_1 + bH_2)^2 = 2ab$, and $D \cdot K =  -2a - 2b$, so

$$\rchi(\mathcal{O}(D)) = 1 + \frac{1}{2}(2ab + 2a + 2b) = (a+1)(b+1)$$

is obtained. This coincides with the number of parameters of bihomogeneous polynomials of bidegree $(a, b)$. For example, $D = H_1 + H_2$ is a $(1,1)$-bidegree curve, with $\rchi = 4$, which is consistent with the fact that a $(1,1)$-curve on $\mathbb{P}^1 \times \mathbb{P}^1$ is equivalent to a conic.
:::

## Hodge Index Theorem

For a fixed smooth projective variety $X$, we know that the collection of divisors $\Pic(X)$ corresponds to the first cohomology of $\mathcal{O}_X^\times$. ([§Sheaf Cohomology, ⁋Proposition 22](/en/math/algebraic_varieties/sheaf_cohomology#prop22)) On the other hand, a divisor is a cycle of complex codimension $1$, that is, real codimension $2$ inside $X$, so by Poincaré duality it gives a class in topological second cohomology, and under this correspondence the cup product exactly corresponds to the intersection of two cycles. ([\[Algebraic Topology\] §Poincaré Duality, ⁋Example 16](/en/math/algebraic_topology/Poincare_duality#ex16)) However, since we are investigating the case of surfaces, $X$ is real $4$-dimensional, so the cup product of two second classes given by divisors falls into top degree $4$ and becomes a single number. That is, the multiplicative structure created by divisors is entirely described by this intersection product alone.

Therefore we can gather divisors and examine their intersection product to study the multiplicative structure of the cohomology ring. For this purpose we first define the following.

::: Definition 9
Two divisors $D_1, D_2$ are *numerically equivalent*, written $D_1 \equiv D_2$, if $D_1 \cdot E = D_2 \cdot E$ for every divisor $E$. The set of numerical equivalence classes is denoted

$$\Num(S) = \Div(S) / \{\text{numerical equivalence}\}$$

and the quadratic form on the real vector space $\Num(S) \otimes \mathbb{R}$ induced by the intersection product is called the *intersection form*.
:::

The above equivalence relation is nothing special; it is merely an equivalence class that regards elements giving the same value when we think about the intersection product of divisors as the same. In general numerical equivalence is a weaker relation than linear equivalence, so two numerically equivalent divisors need not be linearly equivalent to each other.

Meanwhile, an ample divisor $H$ corresponding to an ample line bundle ([§Linear Systems, ⁋Definition 10](/en/math/algebraic_varieties/linear_systems#def10)) plays a special role in the intersection product. This fundamentally stems from the fact that the intersection number of a (very) ample divisor and an effective divisor is necessarily positive, which can be proved by thinking of the actual intersection of an effective divisor and a very ample divisor when we embed the projective variety into projective space using the very ample divisor. Using this, we obtain the following.

::: Proposition 10 (Hodge Index Theorem)
Fix a smooth projective surface $S$ and an ample divisor $H$. If a divisor $D$ satisfies $D \cdot H = 0$ and $D \not\equiv 0$, then $D^2 < 0$.
:::

::: Proof
First assume $D^2>0$. Using [§Cohomology of Projective Space, ⁋Proposition 13](/en/math/algebraic_varieties/cohomology_of_projective_spaces#prop13), we can make $H_n=D+nH$ very ample. Then

$$D \cdot H_n = D^2 + n(D \cdot H) = D^2 > 0$$

On the other hand, by Serre duality $h^2(\mathcal{O}(mD)) = h^0(\omega_S(-mD))$, and for $m \gg 0$,

$$(K_S - mD) \cdot H_n = K_S \cdot H_n - m(D \cdot H_n) = K_S \cdot H_n - mD^2 < 0$$

Since we chose $H_n$ to be very ample, this inequality shows that $K_S-mD$ is not an effective divisor. That is, $h^0(\omega_S(-mD)) = 0$. Now from $\rchi(\mathcal{O}(mD)) = h^0(\mathcal{O}(mD)) - h^1(\mathcal{O}(mD)) + h^2(\mathcal{O}(mD))$ and $h^2 = 0$, for $m \gg 0$,

$$h^0(\mathcal{O}(mD)) \geq \rchi(\mathcal{O}(mD))$$

But by [Proposition 4](#prop4),

$$\rchi(\mathcal{O}(mD)) = \rchi(\mathcal{O}_S) + \frac{m^2 D^2 - m D \cdot K_S}{2}$$

and since we assumed $D^2 > 0$, we know that $\rchi(\mathcal{O}(mD))$ also grows without bound as $\lvert m\rvert$ becomes large. That is, for sufficiently large $m > 0$, $mD$ becomes an effective divisor, and then by the above discussion $mD \cdot H > 0$. However, this contradicts $D \cdot H = 0$, so $D^2 \leq 0$.

Now we finish the proof by showing $D^2\neq 0$. Suppose to the contrary that $D^2 = 0$, $D \cdot H = 0$, and $D \not\equiv 0$. Since $D \not\equiv 0$, there exists some divisor $E$ with $D \cdot E \ne 0$. Define

$$E' = (H^2)E - (E \cdot H)H$$

then $E' \cdot H = (H^2)(E \cdot H) - (E \cdot H)(H^2) = 0$, and since $D \cdot H = 0$,

$$D \cdot E' = (H^2)(D \cdot E) - (E \cdot H)(D \cdot H) = (H^2)(D \cdot E) \ne 0$$

Now similarly to the previous argument, let $F_n := nD + E'$; then $F_n \cdot H = n(D \cdot H) + (E' \cdot H) = 0$ and

$$F_n^2 = n^2 D^2 + 2n(D \cdot E') + E'^2 = 2n(D \cdot E') + E'^2$$

Since $D \cdot E' \ne 0$, by choosing the sign of $n$ appropriately and making $\lvert n \rvert$ large, we can arrange $F_n^2 > 0$. However, $F_n \cdot H = 0$, so applying the previous argument with $D=F_n$ would require $F_n^2 \le 0$, a contradiction.
:::

From this we obtain the following corollary.

::: Corollary 11
The intersection form on $\Num(S) \otimes \mathbb{R}$ has signature $(1, \rho - 1)$, where $\rho$ is the dimension of $\Num(S) \otimes \mathbb{R}$.
:::

::: Proof
For an ample divisor $H$, we have $H^2 > 0$, so the intersection form has at least one positive direction. But by [Proposition 10](#prop10), every nonzero direction orthogonal to $H$ has negative self-intersection, so the proof is complete.
:::

That is, on a surface there is essentially only one "positive" direction, and all other directions can be thought of as "negative" in some sense. This result leads to deep consequences in the birational geometry of surfaces, such as the uniqueness of minimal models.

## Plurigenera

In the case of curves, the genus $g$ is the most basic birational invariant. For surfaces the situation is more complicated, because birational equivalence does not preserve all dimensions of cohomology. However, the dimensions of global sections of tensor powers of the canonical bundle are birational invariants, and these values provide essential information about the birational type of a surface.

::: Definition 12
The *$m$-th plurigenus* of a surface $S$ is

$$P_m(S) = h^0(S, \omega_S^{\otimes m})$$
:::

Here $\omega_S$ is the canonical bundle defined in [§Canonical Line Bundle, ⁋Definition 5](/en/math/algebraic_varieties/canonical_bundle#def5). In particular, for $m = 1$, $P_1(S) = h^0(\omega_S) = p_g(S)$ is the geometric genus, and the sequence of plurigenera $\{P_m(S)\}_{m \ge 1}$ can be said to extend this in some sense. This is an important invariant that determines the birational equivalence class of a surface.

In the next post we treat the Kodaira vanishing theorem and examine how this theorem is utilized in the computation of plurigenera and the classification of surfaces.

---

**References**

**[Hart]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[BHPV]** W. Barth, K. Hulek, C. Peters, A. Van de Ven, *Compact Complex Surfaces*, Springer, 2004.  
**[Huy]** D. Huybrechts, *Lectures on K3 Surfaces*, Cambridge University Press, 2016.
