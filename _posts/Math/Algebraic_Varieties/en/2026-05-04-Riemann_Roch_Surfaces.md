---
title: "The Riemann–Roch Theorem for Surfaces"
description: "We generalize the Riemann–Roch theorem from curves to surfaces by defining intersection numbers, proving the Hodge index theorem and an inequality for plurigenera, and examining the geometric meaning of the intersection form."
excerpt: "Intersection theory on surfaces and its applications"

categories: [Math / Algebraic Varieties]
permalink: /en/math/algebraic_varieties/riemann_roch_surfaces
sidebar: 
    nav: "algebraic_varieties-en"

date: 2026-05-04
weight: 17
translated_at: 2026-08-19T01:45:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-08-19T01:45:04+00:00
---
We previously examined the Riemann–Roch theorem for curves. Essentially, the Riemann–Roch theorem computes the Euler characteristic in terms of other quantitative invariants, and although one could generalize it to arbitrary dimension, in this post we restrict ourselves to the case of surfaces.

Revisiting the Riemann–Roch formula for a curve $C$ ([§The Riemann–Roch Theorem for Curves, ⁋Proposition 3](/en/math/algebraic_varieties/riemann_roch_theorem#prop3))

$$\ell(D) - \ell(K_C - D) = \deg D + 1 - g$$

the left-hand side is essentially the Euler characteristic of $\mathcal{O}_C(D)$, and [§The Riemann–Roch Theorem for Curves, ⁋Lemma 2](/en/math/algebraic_varieties/riemann_roch_theorem#lem2) guarantees that it consists of only two terms. However, when we generalize to surfaces the dimension of the base space increases by one, so additional terms appear on the left-hand side, and correspondingly the right-hand side acquires extra terms as well.

Intuitively, the term $\deg D$ on the right-hand side may be thought of as a linear term, but in generalizing to surfaces we must also consider additional *quadratic terms* such as $D\cdot D$, $D\cdot K_S$, and so on. These encode how two divisors on a surface intersect: whereas divisors on a curve, i.e. points, generally do not meet inside the curve, divisors on a surface, i.e. curves, generally intersect in finitely many points.

In this post we discuss the definition and basic properties of intersection numbers, rigorously derive the Riemann–Roch formula for surfaces, and use it to prove the Hodge index theorem.

## Intersection Number

Our starting point is a definition that may appear somewhat abstract, using the Euler characteristic. Its advantage is that invariance under linear equivalence follows immediately; we will verify shortly that it indeed counts intersection points.

::: Definition 1
For two divisors $C, D$ on a smooth projective surface $S$, we define their *intersection number* $C \cdot D$ by

$$C \cdot D = \rchi(\mathcal{O}_S(C + D)) - \rchi(\mathcal{O}_S(C)) - \rchi(\mathcal{O}_S(D)) + \rchi(\mathcal{O}_S)$$
:::

To understand the geometric meaning, suppose $C$ and $D$ are effective divisors defined by global sections $s \in H^0(\mathcal{O}(C))$, $t \in H^0(\mathcal{O}(D))$. Then their common zero locus is $C \cap D$, and we have the exact sequence

$$0 \rightarrow \mathcal{O} \xrightarrow{(t,-s)} \mathcal{O}(D) \oplus \mathcal{O}(C) \xrightarrow{(s,t)} \mathcal{O}(C+D) \rightarrow \mathcal{O}_{C \cap D} \rightarrow 0$$

where the first arrow is $h \mapsto (ht, -hs)$, the second is $(f, g) \mapsto fs + gt$, and the last is the natural restriction map from $\mathcal{O}(C+D)$ to $C \cap D$. By additivity of the Euler characteristic,

$$C \cdot D = \rchi(\mathcal{O}_{C \cap D})$$

and since $C\cap D$ consists of points, the right-hand side simply counts the number of points in $C\cap D$. A subtle point is that for this to be well defined the curves $C$ and $D$ must be in general position; for this purpose we say that two curves $C, D$ *transversally intersect* at a point $p$ if

$$T_pC\oplus T_pD = T_pS$$

where $T_pC$ and $T_pD$ are viewed as subspaces of $T_pS$, so the condition means an internal direct sum inside $T_pS$, i.e. $T_pC + T_pD = T_pS$ and $T_pC\cap T_pD = 0$. For example, in $\mathbb{A}^2$ the line $x=0$ does not intersect itself transversally, and $y=x^3$ does not intersect $y=0$ transversally, whereas $y=x$ and $y=-x$ do intersect transversally. Moreover, these examples also provide intuition for intersection multiplicity: the intersection multiplicity of $y=x$ and $y=-x$ (at the origin) is $1$, while that of $y=x^3$ and $y=0$ is $3$. In the general case where $C$ and $D$ may not meet transversally,

$$\rchi(\mathcal{O}_{C \cap D}) = \sum_{p \in C \cap D} (C \cdot D)_p$$

holds, where $(C \cdot D)_p$ is the local intersection multiplicity at $p$. To prevent $C\cap D$ from being a curve rather than a finite set of points (for instance when $C=D$), we assume that $C$ and $D$ share no common component.

::: Proposition 2
For divisors on a smooth projective surface $S$, the following hold.

1. *Symmetry.* $C \cdot D = D \cdot C$.
2. *Bilinearity.* $(aC_1 + bC_2) \cdot D = a(C_1 \cdot D) + b(C_2 \cdot D)$.
3. *Linear invariance.* If $C \sim C'$ are linearly equivalent, then $C \cdot D = C' \cdot D$ always holds.
:::

Symmetry follows immediately because the formula in [Definition 1](#def1) is symmetric under exchanging $C$ and $D$, and linear invariance also follows because if $C\sim C'$ then $\mathcal{O}_S(C)\cong\mathcal{O}_S(C')$ and $\mathcal{O}_S(C+D)\cong\mathcal{O}_S(C'+D)$, so the four terms appearing in the definition match pairwise. Perhaps the least trivial property is bilinearity, which is usually explained via Snapper's theorem. By Snapper's theorem, for any coherent sheaf $\mathcal{F}$ on a projective variety and line bundles $L_1, \ldots, L_k$, the Euler characteristic

$$\rchi(\mathcal{F} \otimes L_1^{\otimes n_1} \otimes \cdots \otimes L_k^{\otimes n_k})$$

is given by a polynomial in $n_1, \ldots, n_k$. In particular, $\rchi(\mathcal{O}_S(aC_1 + bC_2 + D))$ is a polynomial in $a, b$, and comparing the quadratic coefficients yields bilinearity.

## Riemann–Roch Theorem for Surfaces

We now have all the language needed to extend the Riemann–Roch theorem to surfaces. Before proceeding, it is useful to observe how intersection numbers can be read as the degree of a line bundle restricted to a curve. For a smooth irreducible curve $D$ on $S$ and any divisor $C$,

$$\deg(\mathcal{O}_S(C)\vert_D) = C \cdot D$$

holds. This follows because $D$ being effective gives a short exact sequence by multiplying with the section defining $\mathcal{O}_S(D)$:

$$0 \rightarrow \mathcal{O}_S(C) \rightarrow \mathcal{O}_S(C+D) \rightarrow \mathcal{O}_S(C+D)\vert_D \rightarrow 0$$

and additivity of the Euler characteristic yields $\rchi(\mathcal{O}_S(C+D)\vert_D) = \rchi(\mathcal{O}_S(C+D)) - \rchi(\mathcal{O}_S(C))$. Indeed, subtracting the case $C=0$ makes the right-hand side exactly $C \cdot D$ by [Definition 1](#def1), while applying [§The Riemann–Roch Theorem for Curves, ⁋Proposition 3](/en/math/algebraic_varieties/riemann_roch_theorem#prop3) to line bundles on $D$ gives

$$\big(\deg(\mathcal{O}_S(C+D)\vert_D) + 1 - g(D)\big) - \big(\deg(\mathcal{O}_S(D)\vert_D) + 1 - g(D)\big) = \deg(\mathcal{O}_S(C)\vert_D)$$

so the desired equality follows. What we need next is the following lemma.

::: Lemma 3 (Genus formula)
For a smooth irreducible curve $D$ on a smooth projective surface $S$,

$$2g(D) - 2 = D^2 + D \cdot K_S$$

holds.
:::

::: Proof
By the adjunction formula in [§Canonical Line Bundle, ⁋Proposition 9](/en/math/algebraic_varieties/canonical_bundle#prop9),

$$\omega_D \cong (\omega_S \otimes \mathcal{O}_S(D))\vert_D$$

Taking degrees of both sides,

$$\deg(\omega_D) = \deg(\omega_S\vert_D) + \deg(\mathcal{O}_D(D))$$

We previously derived from [§The Riemann–Roch Theorem for Curves, ⁋Proposition 3](/en/math/algebraic_varieties/riemann_roch_theorem#prop3) that $\deg(\omega_D)=2g-2$, and it remains only to interpret the two terms on the right as intersection numbers. First, since the divisor corresponding to $\omega_S$ is the canonical divisor $K_S$, we have $\omega_S\vert_D = \mathcal{O}_S(K_S)\vert_D$, and substituting $C=K_S$ into the earlier equality gives $\deg(\omega_S\vert_D) = K_S \cdot D$. Similarly $\mathcal{O}_D(D) = \mathcal{O}_S(D)\vert_D$, so substituting $C=D$ yields $\deg(\mathcal{O}_D(D)) = D^2$. The latter is also the degree of the normal bundle $\mathcal{N}_{D/S}$, which geometrically measures how much $D$ meets itself inside $S$. Combining these,

$$2g(D) - 2 = D \cdot K_S + D^2$$

is obtained.
:::

The Riemann–Roch theorem for surfaces is then given as follows.

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

Since $\mathcal{O}_D(D)$ is a line bundle on $D$, by [§The Riemann–Roch Theorem for Curves, ⁋Proposition 3](/en/math/algebraic_varieties/riemann_roch_theorem#prop3),

$$\rchi(\mathcal{O}_D(D)) = D^2 + 1 - g(D)$$

From the preceding [Lemma 3](#lem3),

$$g(D) = \frac{1}{2}(D^2 + D \cdot K_S) + 1$$

so substituting,

$$\rchi(\mathcal{O}_D(D)) = D^2 + 1 - \frac{1}{2}(D^2 + D \cdot K_S) - 1 = \frac{1}{2}D \cdot (D - K_S)$$

Therefore,

$$\rchi(\mathcal{O}_S(D)) = \rchi(\mathcal{O}_S) + \frac{1}{2}D \cdot (D - K_S)$$

is obtained.

We must now generalize this to an arbitrary divisor $D$. Fix an ample divisor $H$ on $S$. Then by [§Cohomology of Projective Space, ⁋Proposition 7](/en/math/algebraic_varieties/cohomology_of_projective_spaces#prop7), for sufficiently large $n$,

$$H^1(S, \mathcal{O}_S(D + nH)) = H^2(S, \mathcal{O}_S(D + nH)) = 0$$

Hence,

$$\rchi(\mathcal{O}_S(D + nH)) = h^0(\mathcal{O}_S(D + nH))$$

On the other hand, by taking $n$ even larger, [§Cohomology of Projective Space, ⁋Proposition 13](/en/math/algebraic_varieties/cohomology_of_projective_spaces#prop13) ensures that $D+nH$ becomes very ample, so the linear system $\lvert D+nH\rvert$ is non-empty. Moreover, by [§Linear Systems, ⁋Corollary 12](/en/math/algebraic_varieties/linear_systems#cor12), a general member $D'$ of this linear system is a smooth irreducible curve, and $D' \sim D+nH$ implies $\mathcal{O}_S(D')\cong\mathcal{O}_S(D+nH)$, so the two divisors have the same Euler characteristic and, by linear invariance from [Proposition 2](#prop2), the same intersection numbers. Applying the previous argument to $D'$ yields the desired equality for $D+nH$. Now consider the two functions of $n$, $f(n) = \rchi(\mathcal{O}(D+nH))$ and $g(n) = \frac{1}{2}(D+nH)\cdot(D+nH-K_S) + \rchi(\mathcal{O}_S)$; they agree for all sufficiently large $n$. But by Snapper's theorem, $\rchi(\mathcal{O}_S(D+nH))$ is a polynomial in $n$, and two polynomials agreeing at infinitely many points are identical. Thus $f=g$ for all $n$, and in particular substituting $n=0$ gives

$$\rchi(\mathcal{O}(D)) = \frac{1}{2}D\cdot(D-K_S) + \rchi(\mathcal{O}_S)$$
:::

As in the curve case, if $D$ is sufficiently "positive" then $h^1$ and $h^2$ vanish and $\rchi(\mathcal{O}_S(D)) = h^0(S, \mathcal{O}_S(D))$. This is closely related to the notion of ampleness defined in [§Linear Systems, ⁋Definition 10](/en/math/algebraic_varieties/linear_systems#def10).

::: Example 5 ($\mathbb{P}^2$)
Fix the hyperplane class $H$ in $\mathbb{P}^2$; we know

$$K_{\mathbb{P}^2} = -3H, \qquad \rchi(\mathcal{O}_{\mathbb{P}^2}) = 1$$

([§Canonical Line Bundle, §§Canonical Bundle of $\mathbb{P}^n$](/en/math/algebraic_varieties/canonical_bundle#canonical-bundle-of-mathbbpn), [§Cohomology of Projective Space, ⁋Corollary 3](/en/math/algebraic_varieties/cohomology_of_projective_spaces#cor3)). Since any two lines in $\mathbb{P}^2$ generally meet at one point, the self-intersection number of $H$ is $1$, and thus for any divisor $D = dH$,

$$\rchi(\mathcal{O}_{\mathbb{P}^2}(d)) = \frac{1}{2}dH \cdot (dH + 3H) + 1 = \frac{1}{2}d(d+3) + 1$$

holds. That this is indeed true follows from [§Cohomology of Projective Space, ⁋Corollary 3](/en/math/algebraic_varieties/cohomology_of_projective_spaces#cor3). In particular, for $d \ge 0$ we know $h^0 = \binom{d+2}{2}$ and $h^1 = h^2 = 0$, which gives a direct illustration of the vanishing of $h^1, h^2$ mentioned above.
:::

::: Example 6 (Blow-up of $\mathbb{P}^2$)
Now consider the blow-up $\pi: \widetilde{\mathbb{P}}^2 \rightarrow \mathbb{P}^2$ of $\mathbb{P}^2$ at a point $p$. By [§Canonical Line Bundle, ⁋Proposition 12](/en/math/algebraic_varieties/canonical_bundle#prop12), the canonical bundle is given by

$$K_{\widetilde{\mathbb{P}}^2} = \pi^\ast K_{\mathbb{P}^2} + E = -3H + E$$

In $\mathbb{P}^2$ we may choose the hyperplane class $H$ to avoid $p$, so $H \cdot E = 0$. On the other hand, $E \cong \mathbb{P}^1$ and the normal bundle $\mathcal{N}_{E/\widetilde{\mathbb{P}}^2}$ is isomorphic to $\mathcal{O}_{\mathbb{P}^1}(-1)$, giving the self-intersection number $E^2 = \deg(\mathcal{N}_{E/\widetilde{\mathbb{P}}^2}) = -1$; geometrically this means $E$ acquires negativity by "folding inward" as it collapses to a point. Hence for a general divisor $D = dH - kE$,

$$\rchi(\mathcal{O}_{\widetilde{\mathbb{P}}^2}(dH - kE)) = \frac{1}{2}(dH - kE) \cdot (dH - kE + 3H - E) + 1 = \frac{1}{2}d(d+3) - \frac{1}{2}k(k+1) + 1$$

can be computed.
:::

Just as the Riemann–Roch theorem for curves could be rewritten by applying [§Serre Duality](/en/math/algebraic_varieties/serre_duality) to replace the $h^1$ term with $h^0$, on a surface we can apply the same to [Proposition 4](#prop4) to write $h^2(\mathcal{O}(D)) = h^0(\omega_S(-D))$, transforming the Riemann–Roch formula into

$$h^0(\mathcal{O}(D)) - h^1(\mathcal{O}(D)) + h^0(\omega_S(-D)) = \rchi(\mathcal{O}_S) + \frac{1}{2}(D^2 - D \cdot K_S)$$

In general $h^1(\mathcal{O}(D))$ is difficult to compute directly, but if this term is zero or sufficiently small then we can show that at least one of $h^0(\mathcal{O}(D))$ and $h^0(\omega_S(-D))$ is large. One powerful tool for this is the following Kodaira vanishing theorem.

::: Proposition 7 (Kodaira Vanishing Theorem)
For a smooth projective variety $X$ and an ample line bundle $L$,

$$H^i(X, \omega_X \otimes L) = 0$$

holds for all $i > 0$.
:::

Serious applications of the Kodaira vanishing theorem will be treated in the next post. To appreciate the utility of this formula, consider two extreme cases. If $D$ is "sufficiently positive", i.e. $D \cdot H$ is large enough for an ample divisor $H$, then $K_S - D$ becomes "negative" and $h^0(\omega_S(-D)) = 0$, so Riemann–Roch gives a lower bound for $h^0$. Conversely, if $D$ is "sufficiently negative" then $h^0(\mathcal{O}(D)) = 0$ and we obtain information about $K_S - D$. This "symmetry between positive and negative" is a phenomenon created by Serre duality.

The Riemann–Roch computation for $\mathbb{P}^2$ was already covered in [Example 5](#ex5). Here we examine another fundamental example.

::: Example 8 ($\mathbb{P}^1 \times \mathbb{P}^1$)
Consider $\mathbb{P}^1 \times \mathbb{P}^1$. The divisor class group of this surface is $\mathbb{Z} \oplus \mathbb{Z}$, generated by the hyperplane classes $H_1, H_2$ of the two factors, which geometrically are the "horizontal" and "vertical" fibers fixing a point in the first and second factor respectively. That is, $H_1$ consists of copies of $\mathbb{P}^1$ parametrized by the first factor, and $H_2$ by the second. Two horizontal fibers are parallel and do not meet, so $H_1^2 = 0$, and likewise $H_2^2 = 0$. On the other hand, a horizontal fiber and a vertical fiber always meet at one point, so $H_1 \cdot H_2 = 1$.

The canonical divisor is $K = -2H_1 - 2H_2$, coming from the canonical divisor $-2H$ on $\mathbb{P}^1$. As for the Euler characteristic of the structure sheaf, using the Künneth formula,

$$\rchi(\mathcal{O}) = \rchi(\mathcal{O}_{\mathbb{P}^1}) \cdot \rchi(\mathcal{O}_{\mathbb{P}^1}) = 1 \cdot 1 = 1$$

This is analogous to a result in [\[Algebraic Topology\] §Cohomology, ⁋Corollary 10](/en/math/algebraic_topology/cohomology#cor10), though its proof involves somewhat technical details that we omit. Applying the Riemann–Roch formula to a divisor $D = aH_1 + bH_2$ of bidegree $(a, b)$ gives

$$\rchi(\mathcal{O}(D)) = 1 + \frac{1}{2}(D^2 - D \cdot K)$$

Here $D^2 = (aH_1 + bH_2)^2 = 2ab$ and $D \cdot K =  -2a - 2b$, so

$$\rchi(\mathcal{O}(D)) = 1 + \frac{1}{2}(2ab + 2a + 2b) = (a+1)(b+1)$$

This agrees with the number of parameters of bihomogeneous polynomials of bidegree $(a, b)$. For example, $D = H_1 + H_2$ is a $(1,1)$-curve with $\rchi = 4$, consistent with the fact that a $(1,1)$-curve on $\mathbb{P}^1 \times \mathbb{P}^1$ is equivalent to a conic.
:::

## Hodge Index Theorem

For a fixed smooth projective variety $X$, we know that the collection of divisors $\Pic(X)$ corresponds to the first cohomology of $\mathcal{O}_X^\times$. ([§Sheaf Cohomology, ⁋Proposition 22](/en/math/algebraic_varieties/sheaf_cohomology#prop22)) On the other hand, a divisor is a cycle of complex codimension $1$, i.e. real codimension $2$, so by Poincaré duality it gives a class in topological second cohomology, and under this correspondence the cup product corresponds exactly to the intersection of two cycles. ([\[Algebraic Topology\] §Poincaré Duality, ⁋Example 16](/en/math/algebraic_topology/Poincare_duality#ex16)) Since we are exploring the case of surfaces, $X$ is real $4$-dimensional, so the cup product of two second cohomology classes given by divisors lands in top degree $4$ and becomes a single number. Thus the multiplicative structure generated by divisors is entirely described by this intersection product.

Therefore we can collect divisors and examine their intersection product to study the multiplicative structure of the cohomology ring. For this we first make the following definition.

::: Definition 9
Two divisors $D_1, D_2$ are *numerically equivalent*, written $D_1 \equiv D_2$, if $D_1 \cdot E = D_2 \cdot E$ for every divisor $E$. The set of numerical equivalence classes is denoted

$$\Num(S) = \Div(S) / \{\text{numerical equivalence}\}$$

and the quadratic form on the real vector space $\Num(S) \otimes \mathbb{R}$ induced by the intersection product is called the *intersection form*.
:::

The above equivalence relation is nothing more than grouping together elements that give the same values under intersection product. In general numerical equivalence is weaker than linear equivalence, so two numerically equivalent divisors need not be linearly equivalent.

Meanwhile, an ample divisor $H$ corresponding to an ample line bundle ([§Linear Systems, ⁋Definition 10](/en/math/algebraic_varieties/linear_systems#def10)) plays a special role in the intersection product. This ultimately stems from the fact that the intersection number of a (very) ample divisor with an effective divisor is necessarily positive, which can be proved by embedding the projective variety into projective space via a very ample divisor and considering the actual intersection of the effective divisor with it. Using this we obtain the following.

::: Proposition 10 (Hodge Index Theorem)
Fix a smooth projective surface $S$ and an ample divisor $H$. If a divisor $D$ satisfies $D \cdot H = 0$ and $D \not\equiv 0$, then $D^2 < 0$.
:::

::: Proof
First assume $D^2>0$. By [§Cohomology of Projective Space, ⁋Proposition 13](/en/math/algebraic_varieties/cohomology_of_projective_spaces#prop13) we can arrange that $H_n=D+nH$ is very ample. Then

$$D \cdot H_n = D^2 + n(D \cdot H) = D^2 > 0$$

On the other hand, by Serre duality $h^2(\mathcal{O}(mD)) = h^0(\omega_S(-mD))$, and for $m \gg 0$,

$$(K_S - mD) \cdot H_n = K_S \cdot H_n - m(D \cdot H_n) = K_S \cdot H_n - mD^2 < 0$$

Since we chose $H_n$ to be very ample, this inequality shows that $K_S-mD$ is not an effective divisor; i.e. $h^0(\omega_S(-mD)) = 0$. Now from $\rchi(\mathcal{O}(mD)) = h^0(\mathcal{O}(mD)) - h^1(\mathcal{O}(mD)) + h^2(\mathcal{O}(mD))$ and $h^2 = 0$, for $m \gg 0$,

$$h^0(\mathcal{O}(mD)) \geq \rchi(\mathcal{O}(mD))$$

But by [Proposition 4](#prop4),

$$\rchi(\mathcal{O}(mD)) = \rchi(\mathcal{O}_S) + \frac{m^2 D^2 - m D \cdot K_S}{2}$$

and since we assumed $D^2 > 0$, $\rchi(\mathcal{O}(mD))$ grows without bound as $\lvert m\rvert$ becomes large. Thus for sufficiently large $m > 0$, $mD$ is an effective divisor, and by the above discussion $mD \cdot H > 0$. But this contradicts $D \cdot H = 0$, so $D^2 \leq 0$.

It remains to rule out $D^2 = 0$. Suppose for contradiction that $D^2 = 0$, $D \cdot H = 0$, and $D \not\equiv 0$. Since $D \not\equiv 0$, there exists some divisor $E$ with $D \cdot E \ne 0$. Define

$$E' = (H^2)E - (E \cdot H)H$$

Then $E' \cdot H = (H^2)(E \cdot H) - (E \cdot H)(H^2) = 0$, and because $D \cdot H = 0$,

$$D \cdot E' = (H^2)(D \cdot E) - (E \cdot H)(D \cdot H) = (H^2)(D \cdot E) \ne 0$$

Now set $F_n := nD + E'$; then $F_n \cdot H = n(D \cdot H) + (E' \cdot H) = 0$ and

$$F_n^2 = n^2 D^2 + 2n(D \cdot E') + E'^2 = 2n(D \cdot E') + E'^2$$

Since $D \cdot E' \ne 0$, by choosing the sign of $n$ and making $\lvert n \rvert$ large we can ensure $F_n^2 > 0$. However, $F_n \cdot H = 0$, so applying the previous argument with $D=F_n$ would require $F_n^2 \le 0$, a contradiction.
:::

From this we obtain the following corollary.

::: Corollary 11
The intersection form on $\Num(S) \otimes \mathbb{R}$ has signature $(1, \rho - 1)$, where $\rho$ is the dimension of $\Num(S) \otimes \mathbb{R}$.
:::

::: Proof
For an ample divisor $H$, $H^2 > 0$, so the intersection form has at least one positive direction. But by [Proposition 10](#prop10), every non-zero direction orthogonal to $H$ has negative self-intersection, completing the proof.
:::

That is, on a surface there is essentially only one "positive" direction, and all other directions can be thought of as "negative" in some sense. This result leads to deep consequences such as the uniqueness of minimal models in the birational geometry of surfaces.

## Plurigenera

In the case of curves, the genus $g$ is the most basic birational invariant. For surfaces the situation is more complicated, because birational equivalence does not preserve all cohomology dimensions. However, the dimensions of global sections of tensor powers of the canonical bundle are birational invariants, and these values provide essential information about the birational type of a surface.

::: Definition 12
The *$m$-th plurigenus* of a surface $S$ is

$$P_m(S) = h^0(S, \omega_S^{\otimes m})$$
:::

Here $\omega_S$ is the canonical bundle defined in [§Canonical Line Bundle, ⁋Definition 5](/en/math/algebraic_varieties/canonical_bundle#def5). In particular, for $m = 1$, $P_1(S) = h^0(\omega_S) = p_g(S)$ is the geometric genus, and the sequence $\{P_m(S)\}_{m \ge 1}$ of plurigenera can be regarded as an extension of this in some sense. It is an important invariant determining the birational equivalence class of a surface.

In the next post we discuss the Kodaira vanishing theorem and examine how this theorem is utilized in computing plurigenera and in the classification of surfaces.

---

**References**

**[Hart]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[BHPV]** W. Barth, K. Hulek, C. Peters, A. Van de Ven, *Compact Complex Surfaces*, Springer, 2004.  
**[Huy]** D. Huybrechts, *Lectures on K3 Surfaces*, Cambridge University Press, 2016.
