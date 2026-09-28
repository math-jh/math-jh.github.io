---
title: "The Riemann-Roch Theorem on Surfaces"
description: "In the process of generalizing the Riemann-Roch theorem from curves to surfaces, we define intersection numbers, prove the Hodge index theorem and an inequality for multiple generators, and examine the geometric meaning of the intersection form."
excerpt: "Intersection theory on surfaces and its applications"

categories: [Math / Algebraic Varieties]
permalink: /en/math/algebraic_varieties/riemann_roch_surfaces
sidebar: 
    nav: "algebraic_varieties-en"

date: 2026-05-04
weight: 17
translated_at: 2026-08-19T01:45:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-09-28T07:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
We previously examined the Riemann–Roch theorem for curves. Essentially, the Riemann–Roch theorem computes the Euler characteristic in terms of other quantitative values, and although more generally we could generalize this to the arbitrary case, in this post we treat only the generalization to surfaces.

If we look again at the Riemann–Roch formula for a curve $C$ ([§The Riemann–Roch Theorem for Curves, ⁋Proposition 3](/en/math/algebraic_varieties/riemann_roch_theorem#prop3){: data-lid="surlk" })

$$\ell(D) - \ell(K_C - D) = \deg D + 1 - g$$

the left-hand side of this formula is essentially the Euler characteristic of $\mathcal{O}_C(D)$, and [§The Riemann–Roch Theorem for Curves, ⁋Lemma 2](/en/math/algebraic_varieties/riemann_roch_theorem#lem2){: data-lid="f4nkc" } guarantees that this part consists of only two terms. However, now to generalize this to surfaces, since the dimension of the base space increases by one, an additional term will appear, and correspondingly, an additional term will also appear in the expression on the right-hand side.

Intuitively, the term $\deg D$ appearing on the right-hand side of the above formula may be thought of as a kind of linear term, but in the process of generalizing to surfaces in this way, we come to consider additional *quadratic terms* such as $D\cdot D$, $D\cdot K_S$, and so on. These are quantities that capture how much two divisors on a surface intersect; they arise because, while divisors in the curve case, namely points, generally do not meet inside the curve, divisors on a surface, namely curves, generally meet at finitely many points inside this surface.

In this post, we discuss the definition and basic properties of the intersection number, rigorously derive the Riemann–Roch formula, and then use this to prove the Hodge index theorem.

## Intersection Number

Our starting point is a definition using the Euler characteristic, which may appear somewhat abstract. The advantage of this definition is that invariance under linear equivalence follows immediately, and right after the definition we will verify that it indeed counts the number of intersection points.

::: Definition 1
On a smooth projective surface $S$, for two divisors $C, D$, we define their *intersection number* $C \cdot D$ as follows:

$$C \cdot D = \rchi(\mathcal{O}_S(C + D)) - \rchi(\mathcal{O}_S(C)) - \rchi(\mathcal{O}_S(D)) + \rchi(\mathcal{O}_S)$$
:::

To examine their geometric meaning, suppose $C$ and $D$ are effective divisors defined by global sections $s \in H^0(\mathcal{O}(C))$ and $t \in H^0(\mathcal{O}(D))$, respectively. Then their common zero locus is $C \cap D$, and the following exact sequence holds:

$$0 \rightarrow \mathcal{O} \xrightarrow{(t,-s)} \mathcal{O}(D) \oplus \mathcal{O}(C) \xrightarrow{(s,t)} \mathcal{O}(C+D) \rightarrow \mathcal{O}_{C \cap D} \rightarrow 0$$

Here, the first arrow is $h \mapsto (ht, -hs)$, the second arrow is $(f, g) \mapsto fs + gt$, and the last arrow is the natural restriction map from $\mathcal{O}(C+D)$ onto $C \cap D$. Then, by the additivity of the Euler characteristic,

$$C \cdot D = \rchi(\mathcal{O}_{C \cap D})$$

where $C\cap D$ is the intersection of two curves, namely points, and therefore the Euler characteristic on the right-hand side precisely counts the number of points of $C\cap D$. A somewhat subtle point is that for this to be well-defined, $C$ and $D$ must be in general position; to this end, we define that two curves $C,D$ *transversally intersect* at a point $p$ by the condition

$$T_pC\oplus T_pD = T_pS$$

where $T_pC$ and $T_pD$ are viewed as subspaces of $T_pS$, and thus the above condition means an internal direct sum inside $T_pS$, that is, $T_pC + T_pD = T_pS$ and $T_pC\cap T_pD = 0$. For instance, in $\mathbb{A}^2$, $\x=0$ does not transversally intersect itself, and $\y=\x^3$ does not transversally intersect $\y=0$. On the other hand, $\y=\x$ and $\y=-\x$ meet transversally. Moreover, this example also provides intuition for intersection multiplicity: the intersection multiplicity of $\y=\x$ and $\y=-\x$ (at the origin) is $1$, but the intersection multiplicity of $\y=\x^3$ and $\y=0$ is $3$. Then, in the general case where $C$ and $D$ may not meet transversally,

$$\rchi(\mathcal{O}_{C \cap D}) = \sum_{p \in C \cap D} (C \cdot D)_p$$

holds, where $(C \cdot D)_p$ is the local intersection multiplicity at $p$. Here, to prevent the situation where $C\cap D$ in this formula becomes a curve instead of a finite set of points (for instance, to prevent the situation where $C=D$), we assume that $C,D$ share no common component.

::: Proposition 2
For divisors on a smooth projective surface $S$, the following hold. 

1. *Symmetry.* $C \cdot D = D \cdot C$ holds.
2. *Bilinearity.* $(aC_1 + bC_2) \cdot D = a(C_1 \cdot D) + b(C_2 \cdot D)$ holds. 
3. *Linear invariance.* For two linearly equivalent divisors $C \sim C'$, $C \cdot D = C' \cdot D$ always holds.
:::

Symmetry follows immediately from the fact that the formula in [Definition 1](#def1){: data-lid="uknj0" } is symmetric under exchanging $C$ and $D$, and linear invariance also follows because if $C\sim C'$, then $\mathcal{O}_S(C)\cong\mathcal{O}_S(C')$ and $\mathcal{O}_S(C+D)\cong\mathcal{O}_S(C'+D)$, so the four terms appearing in the definition match each other respectively. Surprisingly, the least trivial property is bilinearity, which can usually be explained by Snapper's theorem. According to Snapper's theorem, for any coherent sheaf $\mathcal{F}$ and line bundles $L_1, \ldots, L_k$ on a projective variety, the Euler characteristic 

$$\rchi(\mathcal{F} \otimes L_1^{\otimes n_1} \otimes \cdots \otimes L_k^{\otimes n_k})$$

is given by a polynomial in $n_1, \ldots, n_k$. Then in particular, in the definition of the intersection number, $\rchi(\mathcal{O}_S(aC_1 + bC_2 + D))$ is a polynomial in $a, b$, and comparing the quadratic coefficients of this polynomial yields bilinearity.

## Riemann–Roch Theorem for Surfaces

We now have all the language needed to extend the Riemann–Roch theorem to surfaces. Before that, it is necessary to examine how to read the intersection number as the degree of a line bundle on a curve. On $S$, for a smooth irreducible curve $D$ and any divisor $C$,

$$\deg(\mathcal{O}_S(C)\vert_D) = C \cdot D$$

holds; this follows because since $D$ is an effective divisor, multiplying by the section defining $D$ of $\mathcal{O}_S(D)$ yields the short exact sequence

$$0 \rightarrow \mathcal{O}_S(C) \rightarrow \mathcal{O}_S(C+D) \rightarrow \mathcal{O}_S(C+D)\vert_D \rightarrow 0$$

and by the additivity of the Euler characteristic, $\rchi(\mathcal{O}_S(C+D)\vert_D) = \rchi(\mathcal{O}_S(C+D)) - \rchi(\mathcal{O}_S(C))$. Indeed, subtracting the equality for the case $C=0$, the right-hand side becomes exactly $C \cdot D$ by [Definition 1](#def1){: data-lid="rsree" }, while applying [§The Riemann–Roch Theorem for Curves, ⁋Proposition 3](/en/math/algebraic_varieties/riemann_roch_theorem#prop3){: data-lid="qzitc" } to line bundles on $D$, the left-hand side becomes

$$\big(\deg(\mathcal{O}_S(C+D)\vert_D) + 1 - g(D)\big) - \big(\deg(\mathcal{O}_S(D)\vert_D) + 1 - g(D)\big) = \deg(\mathcal{O}_S(C)\vert_D)$$

so the desired equality follows. Now what we need is the following lemma. 

::: Lemma 3 (Genus formula)
On a smooth projective surface $S$, for a smooth irreducible curve $D$,

$$2g(D) - 2 = D^2 + D \cdot K_S$$

holds.
:::

::: Proof
By the adjunction formula in [§Canonical Line Bundle, ⁋Proposition 9](/en/math/algebraic_varieties/canonical_bundle#prop9){: data-lid="s254n" },

$$\omega_D \cong (\omega_S \otimes \mathcal{O}_S(D))\vert_D$$

Taking the degrees of both sides,

$$\deg(\omega_D) = \deg(\omega_S\vert_D) + \deg(\mathcal{O}_D(D))$$

We previously derived from [§The Riemann–Roch Theorem for Curves, ⁋Proposition 3](/en/math/algebraic_varieties/riemann_roch_theorem#prop3){: data-lid="i83nq" } that $\deg(\omega_D)=2g-2$, and it remains only to interpret the two terms on the right-hand side as intersection numbers. First, since the divisor corresponding to $\omega_S$ is the canonical divisor $K_S$, we have $\omega_S\vert_D = \mathcal{O}_S(K_S)\vert_D$, and therefore substituting $C=K_S$ into the equality established earlier gives $\deg(\omega_S\vert_D) = K_S \cdot D$. Similarly, since $\mathcal{O}_D(D) = \mathcal{O}_S(D)\vert_D$, substituting $C=D$ into the same equality yields $\deg(\mathcal{O}_D(D)) = D^2$. The latter is also the degree of the normal bundle of $D$, $\mathcal{N}_{D/S}$, and geometrically this is a quantity measuring how much $D$ meets itself inside $S$. Combining these,

$$2g(D) - 2 = D \cdot K_S + D^2$$

is obtained. 
:::

Then the Riemann–Roch theorem for surfaces is given as follows.

::: Proposition 4 (Riemann–Roch for surfaces)
On a smooth projective surface $S$, for a divisor $D$,

$$\rchi(\mathcal{O}_S(D)) = \frac{1}{2} D \cdot (D - K_S) + \rchi(\mathcal{O}_S)$$

holds. 
:::

::: Proof
First consider the case where $D$ is a smooth irreducible effective divisor. From the following short exact sequence

$$0 \rightarrow \mathcal{O}_S \rightarrow \mathcal{O}_S(D) \rightarrow \mathcal{O}_D(D) \rightarrow 0$$

by the additivity of the Euler characteristic,

$$\rchi(\mathcal{O}_S(D)) = \rchi(\mathcal{O}_S) + \rchi(\mathcal{O}_D(D))$$

holds. Here, since $\mathcal{O}_D(D)$ is a line bundle defined on $D$, by [§The Riemann–Roch Theorem for Curves, ⁋Proposition 3](/en/math/algebraic_varieties/riemann_roch_theorem#prop3){: data-lid="w854z" },

$$\rchi(\mathcal{O}_D(D)) = D^2 + 1 - g(D)$$

holds. Since from the preceding [Lemma 3](#lem3){: data-lid="ctg6o" },

$$g(D) = \frac{1}{2}(D^2 + D \cdot K_S) + 1$$

substituting this yields

$$\rchi(\mathcal{O}_D(D)) = D^2 + 1 - \frac{1}{2}(D^2 + D \cdot K_S) - 1 = \frac{1}{2}D \cdot (D - K_S)$$

Therefore,

$$\rchi(\mathcal{O}_S(D)) = \rchi(\mathcal{O}_S) + \frac{1}{2}D \cdot (D - K_S)$$

is obtained.

Now we must generalize this to an arbitrary divisor $D$. On $S$, let us first fix an ample divisor $H$. Then by [§Cohomology of Projective Space, ⁋Proposition 7](/en/math/algebraic_varieties/cohomology_of_projective_spaces#prop7){: data-lid="gmqk8" }, for sufficiently large $n$,

$$H^1(S, \mathcal{O}_S(D + nH)) = H^2(S, \mathcal{O}_S(D + nH)) = 0$$

holds. Therefore,

$$\rchi(\mathcal{O}_S(D + nH)) = h^0(\mathcal{O}_S(D + nH))$$

holds. On the other hand, if we increase $n$ further, by [§Cohomology of Projective Space, ⁋Proposition 13](/en/math/algebraic_varieties/cohomology_of_projective_spaces#prop13){: data-lid="z9uos" }, we can ensure that $D+nH$ is very ample, and then the linear system $\lvert D+nH\rvert$ is non-empty. However, by [§Linear Systems, ⁋Corollary 12](/en/math/algebraic_varieties/linear_systems#cor12){: data-lid="m1tx5" }, a general member $D'$ of this linear system is a smooth irreducible curve, and since $D' \sim D+nH$, the two divisors have the same Euler characteristic from $\mathcal{O}_S(D')\cong\mathcal{O}_S(D+nH)$, and by the linear invariance of [Proposition 2](#prop2){: data-lid="g2c1u" }, the intersection numbers they form are also equal. Therefore, applying the preceding argument to $D'$, the desired equality holds for $D+nH$ as well. Then, considering the two functions of $n$, $f(n) = \rchi(\mathcal{O}(D+nH))$ and $g(n) = \frac{1}{2}(D+nH)\cdot(D+nH-K_S) + \rchi(\mathcal{O}_S)$, they always agree for sufficiently large $n$. But by the aforementioned Snapper's theorem, $\rchi(\mathcal{O}_S(D+nH))$ is a polynomial in $n$, and since polynomials whose values agree on infinitely many points are equal to each other, $f$ and $g$ are in fact the same polynomial. That is, for all $n$, $f(n) = g(n)$, and in particular, substituting $n = 0$,

$$\rchi(\mathcal{O}(D)) = \frac{1}{2}D\cdot(D-K_S) + \rchi(\mathcal{O}_S)$$

is obtained.
:::

As in the case of curves, if $D$ is in a sufficiently "positive" direction, $h^1$ and $h^2$ vanish so that $\rchi(\mathcal{O}_S(D)) = h^0(S, \mathcal{O}_S(D))$. This is closely related to the concept of ampleness defined in [§Linear Systems, ⁋Definition 10](/en/math/algebraic_varieties/linear_systems#def10){: data-lid="19vsc" }.

::: Example 5 ($\mathbb{P}^2$)
On $\mathbb{P}^2$, we know that if we fix a hyperplane class $H$,

$$K_{\mathbb{P}^2} = -3H, \qquad \rchi(\mathcal{O}_{\mathbb{P}^2}) = 1$$

([§Canonical Line Bundle, §§Canonical Bundle of $\mathbb{P}^n$](/en/math/algebraic_varieties/canonical_bundle#canonical-bundle-of-mathbbpn){: data-lid="e71wa" }, [§Cohomology of Projective Space, ⁋Corollary 3](/en/math/algebraic_varieties/cohomology_of_projective_spaces#cor3){: data-lid="xg5w6" }). Since any two lines on $\mathbb{P}^2$ generally meet at one point, the self-intersection number of $H$ is 1, and therefore for any divisor $D = dH$,

$$\rchi(\mathcal{O}_{\mathbb{P}^2}(d)) = \frac{1}{2}dH \cdot (dH + 3H) + 1 = \frac{1}{2}d(d+3) + 1$$

holds. That this actually holds is the result of [§Cohomology of Projective Space, ⁋Corollary 3](/en/math/algebraic_varieties/cohomology_of_projective_spaces#cor3){: data-lid="37hxy" }. In particular, for $d \ge 0$, we know that $h^0 = \binom{d+2}{2}$ and $h^1 = h^2 = 0$, so this serves as a direct example of the vanishing of $h^1, h^2$ mentioned above. 
:::

::: Example 6 (Blow-up of $\mathbb{P}^2$)
Now we consider, on $\mathbb{P}^2$ at a point $p$, the blow-up $\pi: \widetilde{\mathbb{P}}^2 \rightarrow \mathbb{P}^2$. By [§Canonical Line Bundle, ⁋Proposition 12](/en/math/algebraic_varieties/canonical_bundle#prop12){: data-lid="pzmw0" }, the canonical bundle is given by

$$K_{\widetilde{\mathbb{P}}^2} = \pi^\ast K_{\mathbb{P}^2} + E = -3H + E$$

In $\mathbb{P}^2$, we can choose the hyperplane class $H$ to avoid the point $p$, so $H \cdot E = 0$. On the other hand, $E \cong \mathbb{P}^1$, and the normal bundle of $E$, $\mathcal{N}_{E/\widetilde{\mathbb{P}}^2}$, is isomorphic to $\mathcal{O}_{\mathbb{P}^1}(-1)$, from which the self-intersection number is $E^2 = \deg(\mathcal{N}_{E/\widetilde{\mathbb{P}}^2}) = -1$; geometrically, this means that as $E$ collapses to a point, it "folds inward" from the surroundings and acquires negativity. Therefore, for a general divisor $D = dH - kE$, we can compute that

$$\rchi(\mathcal{O}_{\widetilde{\mathbb{P}}^2}(dH - kE)) = \frac{1}{2}(dH - kE) \cdot (dH - kE + 3H - E) + 1 = \frac{1}{2}d(d+3) - \frac{1}{2}k(k+1) + 1$$
:::

Meanwhile, just as the Riemann–Roch theorem for curves applied [§Serre Duality](/en/math/algebraic_varieties/serre_duality){: data-lid="awlcy" } to the formula using the Euler characteristic to replace the $h^1$ part with $h^0$, on a surface we can also apply this to [Proposition 4](#prop4){: data-lid="koib0" } above to write $h^2(\mathcal{O}(D)) = h^0(\omega_S(-D))$, and the Riemann–Roch formula then turns into the following equation:

$$h^0(\mathcal{O}(D)) - h^1(\mathcal{O}(D)) + h^0(\omega_S(-D)) = \rchi(\mathcal{O}_S) + \frac{1}{2}(D^2 - D \cdot K_S)$$

In general, $h^1(\mathcal{O}(D))$ is a term that is difficult to compute directly, but if we can assume that this value is 0 or sufficiently small, then we can show that at least one of $h^0(\mathcal{O}(D))$ and $h^0(\omega_S(-D))$ is sufficiently large. One powerful tool for this is the following Kodaira vanishing theorem.

::: Proposition 7 (Kodaira Vanishing Theorem)
For a smooth projective variety $X$ and an ample line bundle $L$,

$$H^i(X, \omega_X \otimes L) = 0$$

holds for all $i > 0$.
:::

Serious applications of the Kodaira vanishing theorem will be treated in the next post. To understand the utility of this formula, let us consider two extreme cases. If $D$ is "sufficiently positive", that is, if $D \cdot H$ is sufficiently large with respect to an ample divisor $H$, then $K_S - D$ goes in the "negative" direction so that $h^0(\omega_S(-D)) = 0$, and Riemann–Roch gives a lower bound for $h^0$. Conversely, if $D$ is "sufficiently negative", then $h^0(\mathcal{O}(D)) = 0$ and we obtain information about $K_S - D$. This "symmetry between positive and negative" is a phenomenon created by Serre duality.

The Riemann–Roch computation for $\mathbb{P}^2$ was already treated in [Example 5](#ex5){: data-lid="2z7ju" }. Here we examine another fundamental example.

::: Example 8 ($\mathbb{P}^1 \times \mathbb{P}^1$)
Consider $\mathbb{P}^1 \times \mathbb{P}^1$. The divisor class group of this surface is $\mathbb{Z} \oplus \mathbb{Z}$, with the hyperplane classes $H_1, H_2$ of each factor as generators, which are obtained by fixing the first and second factors and attaching a copy of $\mathbb{P}^1$. That is, geometrically, $H_1$ is the "horizontal" fibers corresponding to points of the first factor, and $H_2$ is the "vertical" fibers corresponding to points of the second factor. Two horizontal fibers are parallel to each other and thus do not meet, so $H_1^2 = 0$, and similarly $H_2^2 = 0$. On the other hand, a horizontal fiber and a vertical fiber always meet at one point, so $H_1 \cdot H_2 = 1$.

The canonical divisor is $K = -2H_1 - 2H_2$, which comes from the canonical divisor of $\mathbb{P}^1$, $-2H$. Meanwhile, for the Euler characteristic of the structure sheaf, using the Künneth formula, one can verify that

$$\rchi(\mathcal{O}) = \rchi(\mathcal{O}_{\mathbb{P}^1}) \cdot \rchi(\mathcal{O}_{\mathbb{P}^1}) = 1 \cdot 1 = 1$$

holds. Although this is a result similar to [\[Algebraic Topology\] §Cohomology, ⁋Corollary 10](/en/math/algebraic_topology/cohomology#cor10){: data-lid="rnobz" }, its proof involves somewhat technical aspects, so we omit it. Now, using this, applying the Riemann–Roch formula to a divisor of bidegree $(a, b)$, $D = aH_1 + bH_2$, we obtain

$$\rchi(\mathcal{O}(D)) = 1 + \frac{1}{2}(D^2 - D \cdot K)$$

Here, $D^2 = (aH_1 + bH_2)^2 = 2ab$ and $D \cdot K =  -2a - 2b$, so we obtain

$$\rchi(\mathcal{O}(D)) = 1 + \frac{1}{2}(2ab + 2a + 2b) = (a+1)(b+1)$$

This agrees with the number of parameters of bihomogeneous polynomials of bidegree $(a, b)$. For example, $D = H_1 + H_2$ is a curve of bidegree $(1,1)$ with $\rchi = 4$, which is consistent with the fact that on $\mathbb{P}^1 \times \mathbb{P}^1$, a $(1,1)$-curve is equivalent to a conic.
:::

## Hodge Index Theorem

For a fixed smooth projective variety $X$, we know that the collection of divisors on $X$, $\Pic(X)$, corresponds to the cohomology of $\mathcal{O}_X^\times$ in degree $1$. ([§Sheaf Cohomology, ⁋Proposition 22](/en/math/algebraic_varieties/sheaf_cohomology#prop22){: data-lid="63yth" }) On the other hand, since a divisor is a cycle in $X$ of complex codimension $1$, that is, real codimension $2$, by Poincaré duality it gives a class in topological degree $2$ cohomology, and under this correspondence the cup product corresponds exactly to the intersection of two cycles. ([\[Algebraic Topology\] §Poincaré Duality, ⁋Example 16](/en/math/algebraic_topology/Poincare_duality#ex16){: data-lid="b5b31" }) However, since we are exploring the case of surfaces, $X$ is real $4$-dimensional, so the cup product of two degree $2$ classes given by divisors lands in the top degree $4$ and becomes a single number. That is, the multiplicative structure generated by divisors is entirely described by this intersection product alone.

Therefore, we can collect divisors and examine what their intersection product is to study the multiplicative structure of the cohomology ring. To this end, we first define the following.

::: Definition 9
Two divisors $D_1, D_2$ are said to be *numerically equivalent*, written $D_1 \equiv D_2$, if for every divisor $E$, $D_1 \cdot E = D_2 \cdot E$. The set of numerical equivalence classes is denoted

$$\Num(S) = \Div(S) / \{\text{numerical equivalence}\}$$

and the quadratic form on the real vector space $\Num(S) \otimes \mathbb{R}$ induced by the intersection product is called the *intersection form*.
:::

The above equivalence relation is nothing special; it is merely the equivalence relation that regards elements giving the same values under the intersection product of divisors as the same. In general, numerical equivalence is a weaker relation than linear equivalence, so two numerically equivalent divisors need not be linearly equivalent to each other.

Meanwhile, an ample divisor $H$ corresponding to an ample line bundle ([§Linear Systems, ⁋Definition 10](/en/math/algebraic_varieties/linear_systems#def10){: data-lid="2s3o4" }) plays a special role in the intersection product. This fundamentally stems from the fact that the intersection number of a (very) ample divisor with an effective divisor is necessarily positive, which can be proved by embedding the projective variety into projective space via a very ample divisor and considering the actual intersection of the effective divisor and the very ample divisor. Using this, we obtain the following.

::: Proposition 10 (Hodge Index Theorem)
Fix a smooth projective surface $S$ and an ample divisor $H$. If a divisor $D$ satisfies $D \cdot H = 0$ and $D \not\equiv 0$, then $D^2 < 0$.
:::

::: Proof
First assume $D^2>0$. Using [§Cohomology of Projective Space, ⁋Proposition 13](/en/math/algebraic_varieties/cohomology_of_projective_spaces#prop13){: data-lid="7en9r" }, we can arrange that $H_n=D+nH$ is very ample. Then

$$D \cdot H_n = D^2 + n(D \cdot H) = D^2 > 0$$

On the other hand, by Serre duality $h^2(\mathcal{O}(mD)) = h^0(\omega_S(-mD))$, and when $m \gg 0$,

$$(K_S - mD) \cdot H_n = K_S \cdot H_n - m(D \cdot H_n) = K_S \cdot H_n - mD^2 < 0$$

However, since we chose $H_n$ to be very ample, this inequality shows that $K_S-mD$ is not an effective divisor; that is, $h^0(\omega_S(-mD)) = 0$. Now, from $\rchi(\mathcal{O}(mD)) = h^0(\mathcal{O}(mD)) - h^1(\mathcal{O}(mD)) + h^2(\mathcal{O}(mD))$, since $h^2 = 0$, for $m \gg 0$

$$h^0(\mathcal{O}(mD)) \geq \rchi(\mathcal{O}(mD))$$

But by [Proposition 4](#prop4){: data-lid="pznui" },

$$\rchi(\mathcal{O}(mD)) = \rchi(\mathcal{O}_S) + \frac{m^2 D^2 - m D \cdot K_S}{2}$$

and since we are assuming $D^2 > 0$, we know that as $\lvert m\rvert$ increases, $\rchi(\mathcal{O}(mD))$ also grows arbitrarily large. That is, for sufficiently large $m > 0$, $mD$ is an effective divisor, and then by the above discussion, $mD \cdot H > 0$. But this contradicts $D \cdot H = 0$, and therefore $D^2 \leq 0$.

We now complete the proof by showing that $D^2\neq 0$. Suppose for contradiction that $D^2 = 0$, $D \cdot H = 0$, and $D \not\equiv 0$. Since $D \not\equiv 0$, we have $D \cdot E \ne 0$ for some divisor $E$. Now define

$$E' = (H^2)E - (E \cdot H)H$$

then $E' \cdot H = (H^2)(E \cdot H) - (E \cdot H)(H^2) = 0$, and because $D \cdot H = 0$,

$$D \cdot E' = (H^2)(D \cdot E) - (E \cdot H)(D \cdot H) = (H^2)(D \cdot E) \ne 0$$

Now, similarly to the previous argument, if we set $F_n := nD + E'$, then $F_n \cdot H = n(D \cdot H) + (E' \cdot H) = 0$ and

$$F_n^2 = n^2 D^2 + 2n(D \cdot E') + E'^2 = 2n(D \cdot E') + E'^2$$

Then, since $D \cdot E' \ne 0$, by suitably choosing the sign of $n$ and making $\lvert n \rvert$ large, we can arrange that $F_n^2 > 0$. However, since $F_n \cdot H = 0$, applying the previous argument to $D=F_n$ requires that $F_n^2 \le 0$, which is a contradiction.
:::

From this we obtain the following corollary.

::: Corollary 11
The intersection form on $\Num(S) \otimes \mathbb{R}$ has signature $(1, \rho - 1)$, where $\rho$ is the dimension of $\Num(S) \otimes \mathbb{R}$.
:::

::: Proof
For an ample divisor $H$, since $H^2 > 0$, the intersection form has at least one positive direction. But by [Proposition 10](#prop10){: data-lid="ce2n7" }, every nonzero direction orthogonal to $H$ has negative self-intersection, completing the proof.
:::

That is, on a surface there is essentially only one "positive" direction, and all other directions can be thought of as "negative" in some sense. This result leads to deep consequences such as the uniqueness of minimal models in the birational geometry of surfaces.

## Plurigenera

In the case of curves, the genus $g$ is the most basic birational invariant. For surfaces, the situation is more complicated, because birational equivalence does not preserve all cohomology dimensions. However, the dimensions of global sections of tensor powers of the canonical bundle are birational invariants, and these values provide essential information about the birational type of a surface.

::: Definition 12
The *$m$-th plurigenus* of a surface $S$ is

$$P_m(S) = h^0(S, \omega_S^{\otimes m})$$
:::

Here $\omega_S$ is the canonical bundle defined in [§Canonical Line Bundle, ⁋Definition 5](/en/math/algebraic_varieties/canonical_bundle#def5){: data-lid="wiw7d" }. In particular, for $m = 1$, $P_1(S) = h^0(\omega_S) = p_g(S)$ is the geometric genus, and the sequence $\{P_m(S)\}_{m \ge 1}$ of plurigenera can be regarded as an extension of this in some sense. This is an important invariant determining the birational equivalence class of a surface.

In the next post, we discuss the Kodaira vanishing theorem and examine how this theorem is utilized in computing plurigenera and in the classification of surfaces.

---

**References**

**[Hart]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[BHPV]** W. Barth, K. Hulek, C. Peters, A. Van de Ven, *Compact Complex Surfaces*, Springer, 2004.  
**[Huy]** D. Huybrechts, *Lectures on K3 Surfaces*, Cambridge University Press, 2016.
