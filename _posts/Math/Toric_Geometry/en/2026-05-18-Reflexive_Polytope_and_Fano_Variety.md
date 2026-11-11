---
title: "Fano Varieties"
description: "We examine the definition of reflexive polytopes and properties of dual polytopes, and explore how to understand the geometric structure of Fano varieties through the bipolar theorem."
excerpt: "Reflexive polytopes and the corresponding Gorenstein Fano toric varieties"

categories: [Math / Toric Geometry]
permalink: /en/math/toric_geometry/reflexive_polytope_fano

sidebar:
    nav: "toric_geometry-en"

date: 2026-05-18
weight: 4
translated_at: 2026-06-03T11:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-11-11T15:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
[§Definition of Toric Varieties](/en/math/toric_geometry/toric_varieties){: data-lid="9o805" } we saw how to construct, from a lattice polytope $P \subseteq M_{\mathbb{R}}$ via its normal fan $\Sigma_P$, a projective toric variety $X_P$. In this construction there are many pathways by which the geometric properties of $P$ translate into algebro-geometric properties of $X_P$, and among them *reflexive polytopes* occupy a special position.

## Reflexive Polytopes

First, fix a lattice $M$ and its dual lattice $N = \Hom(M, \mathbb{Z})$, and let $\langle -, - \rangle : M_{\mathbb{R}} \times N_{\mathbb{R}} \rightarrow \mathbb{R}$ be the natural dual pairing. Then, through this pairing, we can transport a given polytope to the opposite dual lattice. By definition, a *reflexive polytope* is one for which the result is also a lattice polytope.

::: Definition 1
In $M_{\mathbb{R}}$, a $d$-dimensional *lattice polytope* $\Delta$ is called a *reflexive polytope* if the following two conditions are satisfied:

1. The origin $0$ is contained in the interior of $\Delta$.
2. The *dual polytope* of $\Delta$,

$$\Delta^\circ = \{ v \in N_{\mathbb{R}} \mid \langle u, v \rangle \ge -1 \text{ for all } u \in \Delta \}$$

is again a lattice polytope. That is, every vertex of $\Delta^\circ$ belongs to the lattice $N$.
:::

While what the second condition means is quite transparent, the first condition may feel somewhat superfluous. Intuitively, if $\Delta$ does not contain the origin in its interior, then no vector in the *opposite direction* to some vector inside $\Delta$ exists; thus, after choosing a dual vector in a direction that is positive when paired with this vector, if we continue to scale it, the condition defining $\Delta^\circ$ is defined to be unbounded. For this reason, we necessarily require the two conditions above.

True to its name, the most basic property of a reflexive polytope is that the dual operation $\Delta \mapsto \Delta^\circ$ forms an involution on the collection of reflexive polytopes.

::: Proposition 2 (Bipolar theorem)
If $\Delta \subseteq M_{\mathbb{R}}$ is a reflexive polytope, then $\Delta^\circ \subseteq N_{\mathbb{R}}$ is also a reflexive polytope, and $(\Delta^\circ)^\circ = \Delta$ holds.
:::

::: Proof
Since $\Delta$ is reflexive, $\Delta^\circ$ is by definition a lattice polytope. Since for every element of $\Delta$, $u$, the inequality $\langle u, v \rangle \ge -1$ holds for all $v \in \Delta^\circ$, $\Delta \subseteq (\Delta^\circ)^\circ$ can be verified directly from the definition.

Now, to show the reverse direction, if we let $w \in (\Delta^\circ)^\circ$, then $w$ satisfies, for all $v \in \Delta^\circ$, $\langle w, v \rangle \ge -1$. Now consider each facet of $\Delta$, $\Theta$. Then $\Theta$ is, on the boundary of $\Delta$, a $(d-1)$-dimensional face, and by the definition of a reflexive polytope, $\Theta$ is given by the equation $\langle u, v_\Theta \rangle = -1$. Here $v_\Theta \in N$ is the primitive inner normal vector corresponding to $\Theta$. However, since $v_\Theta \in \Delta^\circ$ is a vertex, $\langle w, v_\Theta \rangle \ge -1$ holds. This means that $w$ is contained in the intersection of the half-spaces defining all facets of $\Delta$, and therefore $w \in \Delta$. From this, we obtain $(\Delta^\circ)^\circ = \Delta$. Finally, since $(\Delta^\circ)^\circ = \Delta$ is a lattice polytope, $\Delta^\circ$ is also reflexive.
:::

This proposition shows the symmetry of reflexive polytopes. Although $\Delta$ and $\Delta^\circ$ lie in different vector spaces $M_{\mathbb{R}}$ and $N_{\mathbb{R}}$, they provide two aspects of the same combinatorial object.

## Fano Varieties

In algebraic geometry, a *Fano variety* means, with an ample anticanonical divisor $-K_X$, a normal projective variety $X$. Here the canonical divisor $K_X$ is the divisor class corresponding to the canonical bundle ([\[Algebraic Varieties\] §Canonical Line Bundle, ⁋Definition 6](/en/math/algebraic_varieties/canonical_bundle#def6){: data-lid="llhbq" }), and $-K_X$ is its inverse. If $-K_X$ is additionally a Cartier divisor, then $X$ is called a *Gorenstein Fano variety*. In the context of toric varieties, this condition translates into a very explicit combinatorial condition.

As we saw in [§Definition of Toric Varieties, ⁋Proposition 8](/en/math/toric_geometry/toric_varieties#prop8){: data-lid="b7hh1" }, given a lattice polytope $P \subseteq M_{\mathbb{R}}$, via the normal fan $\Sigma_P$ it defines, we can construct the projective toric variety $X_P = X_{\Sigma_P}$. Now assume that $P = \Delta$ is a reflexive polytope.

::: Proposition 3
For a toric variety $X_\Sigma$, the anticanonical divisor $-K_{X_\Sigma}$, that is, the inverse of the canonical divisor, is given by the sum of all boundary divisors:

$$-K_{X_\Sigma} = \sum_{\rho \in \Sigma(1)} D_\rho.$$

Here $\Sigma(1)$ is the set of 1-dimensional cones of $\Sigma$, and each $D_\rho$ is the torus-invariant prime divisor corresponding to $\rho$.
:::

::: Proof
In [\[Algebraic Varieties\] §Canonical Line Bundle, ⁋Definition 6](/en/math/algebraic_varieties/canonical_bundle#def6){: data-lid="xd579" }, the canonical divisor $K_X$ was defined as the divisor class corresponding to the canonical bundle $\omega_X = \det \Omega^1_X$. We show that $K_{X_\Sigma} = -\sum_\rho D_\rho$, thereby proving that its inverse takes the form above.

On the open dense torus $T_N = \Spec \mathbb{C}[M] \subseteq X_\Sigma$, if we choose for $M$ a basis $m_1, \ldots, m_n$, the characters $\rchi^{m_i}$ become coordinates on the torus, and the top form

$$\omega = \frac{d\rchi^{m_1}}{\rchi^{m_1}} \wedge \cdots \wedge \frac{d\rchi^{m_n}}{\rchi^{m_n}}$$

trivializes $\Omega^n_{T_N}$. Independent of the choice of basis of $M$, this is a $T_N$-invariant top form, and it extends naturally to $X_\Sigma$ as a rational $n$-form.

Now, along each boundary divisor $D_\rho$, let us compute the vanishing degree of $\omega$. For a ray $\rho \in \Sigma(1)$, taking its primitive generator $v_\rho \in N$ as the first basis vector of a suitable basis of $N$ and taking for $M$ the dual basis $m_1, \ldots, m_n$, in an affine chart having $\rho$ as a face, $U_\sigma$, the local equation of $D_\rho$ is $\rchi^{m_1} = 0$. Then, in the expression above, the term $d\rchi^{m_1}/\rchi^{m_1}$ creates exactly a simple pole along $D_\rho$, and since the other factors are regular near $D_\rho$, the form $\omega$ has exactly a simple pole along $D_\rho$. Therefore

$$\divisor(\omega) = -\sum_{\rho \in \Sigma(1)} D_\rho$$

and since $K_{X_\Sigma}$ is the class of this divisor, $-K_{X_\Sigma} = \sum_\rho D_\rho$.
:::

Although this equality itself is well-defined for any fan, the *ample* condition that we are interested in (and the Fano condition) only makes sense when $X_\Sigma$ is complete, so hereafter we assume that $\Sigma$ is a complete fan.

When the anticanonical divisor $-K_{X_\Sigma}$ is a Cartier divisor, the corresponding piecewise linear function $\psi_{-K} \in \PL(\Sigma, M)$ is precisely the function satisfying $\psi_{-K}(v_\rho) = -1$ for all $\rho \in \Sigma(1)$. Moreover, in [§Torus-Invariant Divisors and Line Bundles, ⁋Proposition 6](/en/math/toric_geometry/toric_divisors#prop6){: data-lid="xz57e" } we saw that it suffices to check this condition only on maximal cones, and that this condition exactly coincides with the condition for the given divisor to be Cartier. Now, the key point of the following proposition is that this condition matches precisely the vertex condition of the dual $\Delta^\circ$ of a reflexive polytope.

::: Proposition 4
For a reflexive polytope $\Delta \subseteq M_{\mathbb{R}}$, let the normal fan of $\Delta$ be $\Sigma_\Delta$ and write the corresponding toric variety as $X_\Delta = X_{\Sigma_\Delta}$. Then $X_\Delta$ is a Gorenstein Fano variety. Conversely, if a complete toric variety $X_\Sigma$ is Gorenstein Fano, then $\Sigma$ is the normal fan of some reflexive polytope.
:::

::: Proof
Suppose $\Delta$ is a reflexive polytope. In $\Sigma_\Delta$, each maximal cone $\sigma$ corresponds by [§Definition of Toric Varieties, ⁋Definition 6](/en/math/toric_geometry/toric_varieties#def6){: data-lid="qi0g8" } to some vertex of $\Delta$, $u_\sigma$, and for $\sigma$, the ray generators $v_\rho$ are precisely the inner primitive normals of the facets containing $u_\sigma$. Since the facet equation of $\Delta$ is $\langle u, v_\Theta \rangle = -1$, $u_\sigma$ achieves on $\Delta$ the minimum of $\langle -, v_\rho\rangle$ as precisely $-1$. That is,

$$\langle u_\sigma, v_\rho\rangle = -1 \le \langle u, v_\rho\rangle \quad \text{for all } u \in \Delta, \rho \in \sigma(1)$$

and equality holds only when $u \in F_\rho$ (facet). Therefore $m_\sigma = u_\sigma \in M$ satisfies the Cartier compatibility of [§Torus-Invariant Divisors and Line Bundles, ⁋Proposition 6](/en/math/toric_geometry/toric_divisors#prop6){: data-lid="jqygk" }, and $-K_{X_\Delta}$ is Cartier.

On the other hand, to show the ampleness of $-K_{X_\Delta}$, it suffices to verify that the piecewise linear function $\psi_{-K}$ is strictly convex ([§Torus-Invariant Divisors and Line Bundles, ⁋Proposition 9](/en/math/toric_geometry/toric_divisors#prop9){: data-lid="oeakt" }). That is, for two distinct maximal cones $\sigma, \sigma'$ and the corresponding $u_\sigma, u_{\sigma'}$, it suffices to show that $\langle u_{\sigma'}, v\rangle$ is, on $v \in \sigma$, an upper bound for $\psi_{-K}(v) = \langle u_\sigma, v\rangle$, and that equality holds precisely when $v \in \sigma \cap \sigma'$.

Decompose $v \in \sigma$ as $v = \sum_{\rho \in \sigma(1)} c_\rho v_\rho$ ($c_\rho \ge 0$). For each $\rho \in \sigma(1)$, since $u_{\sigma'} \in \Delta$, we have $\langle u_{\sigma'}, v_\rho \rangle \ge -1$, and also since $u_\sigma \in F_\rho$, we have $\langle u_\sigma, v_\rho\rangle = -1$. Therefore

$$\langle u_{\sigma'}, v\rangle = \sum_{\rho \in \sigma(1)} c_\rho \langle u_{\sigma'}, v_\rho\rangle \ge -\sum_{\rho \in \sigma(1)} c_\rho = \langle u_\sigma, v\rangle$$

and equality holds precisely when, for every $c_\rho > 0$, the ray $\rho$ satisfies $\langle u_{\sigma'}, v_\rho\rangle = -1$, that is, $u_{\sigma'} \in F_\rho$. However, since by the vertex structure of facets "$u_{\sigma'} \in F_\rho$" is equivalent to "$\rho \in \sigma'(1)$", the condition for equality to hold is that $v$ is a combination of only the rays of $\sigma \cap \sigma'$, which is precisely $v \in \sigma \cap \sigma'$. This proves strict convexity.

Conversely, assume that $X_\Sigma$ is Gorenstein Fano. Since $-K_{X_\Sigma}$ is Cartier, for each maximal cone $\sigma$ there exists $m_\sigma \in M$ such that $\langle m_\sigma, v_\rho \rangle = -1$ for all $\rho \in \sigma(1)$. Now, if we define

$$\Delta = \{ u \in M_{\mathbb{R}} \mid \langle u, v_\rho \rangle \ge -1 \text{ for all } \rho \in \Sigma(1) \}$$

then $\Delta$ is a lattice polytope and $0 \in \interior(\Delta)$. The dual of $\Delta$ is $\Delta^\circ = \operatorname{conv}\{v_\rho \mid \rho \in \Sigma(1)\}$, and since this is a lattice polytope, $\Delta$ is reflexive. That $\Sigma$ is the normal fan of $\Delta$ can be verified from the definition.
:::

Meanwhile, the correspondence between a reflexive polytope $\Delta$ and the Gorenstein Fano variety $X_\Delta$ extends beyond the mere existence of the variety, to a correspondence between solutions of the line bundles on it. Specifically, corresponding to the anticanonical divisor $-K_{X_\Delta}$, the global sections of the line bundle $\mathcal{O}_{X_\Delta}(-K_{X_\Delta})$ are in one-to-one correspondence with the lattice points of the reflexive polytope $\Delta$.

::: Proposition 5
For a reflexive polytope $\Delta \subseteq M_{\mathbb{R}}$ and the corresponding toric variety $X_\Delta$, the following $\mathbb{C}$-vector space isomorphism holds:

$$H^0\bigl(X_\Delta, \mathcal{O}_{X_\Delta}(-K_{X_\Delta})\bigr) \cong \bigoplus_{u \in \Delta \cap M} \mathbb{C} \cdot \rchi^u.$$
:::

::: Proof
On a toric variety, the polytope $P_D$ corresponding to a $T_N$-invariant Cartier divisor $D$ is defined by

$$P_D = \{ u \in M_{\mathbb{R}} \mid \langle u, v_\rho \rangle \ge -a_\rho \text{ for all } \rho \in \Sigma(1) \}$$

and as shown in [§Torus-Invariant Divisors and Line Bundles, ⁋Proposition 7](/en/math/toric_geometry/toric_divisors#prop7){: data-lid="718q1" }, a basis of $H^0(X_\Sigma, \mathcal{O}_{X_\Sigma}(D))$ is given by the characters $\rchi^u$ corresponding to the elements of $P_D \cap M$. For the anticanonical divisor $-K_{X_\Delta}$, since $a_\rho = 1$ for all $\rho$, we have

$$P_{-K} = \{ u \in M_{\mathbb{R}} \mid \langle u, v_\rho \rangle \ge -1 \text{ for all } \rho \in \Sigma_\Delta(1) \}$$

However, since $\Sigma_\Delta$ is the normal fan of $\Delta$, the polytope defined by the above inequalities coincides exactly with $\Delta$. Therefore, $P_{-K} = \Delta$, and the desired isomorphism holds.
:::

This result means that the number of lattice points of a reflexive polytope determines the dimension of the solutions of the anticanonical line bundle of the Gorenstein Fano variety. In particular, the number of elements of $\Delta \cap M$ equals $h^0(X_\Delta, \mathcal{O}(-K_{X_\Delta}))$.

Again, the most basic example of a reflexive polytope is the simplex corresponding to projective space $\mathbb{P}^n$. In [§Definition of Toric Varieties, ⁋Example 10](/en/math/toric_geometry/toric_varieties#ex10){: data-lid="vtm2m" }, we saw that the normal fan of the standard simplex $\Delta_n$ is the standard fan of $\mathbb{P}^n$. However, since one of the vertices of $\Delta_n$ is the origin, we have $0 \notin \interior(\Delta_n)$. Thus $\Delta_n$ itself is not a reflexive polytope. Instead, we can consider a (similar) polytope obtained by appropriately extending each edge of this polytope to move the origin into the interior.

::: Example 6
In the lattice $M = \mathbb{Z}^n$, define the polytope

$$\Delta = \{ (x_1, \ldots, x_n) \in \mathbb{R}^n \mid x_i \ge -1 \text{ for all } i, \quad x_1 + x_2 + \cdots + x_n \le 1 \}$$

This polytope is obtained by expanding the standard simplex toward the origin; its vertices are $(-1, -1, \ldots, -1)$ and $(n, -1, \ldots, -1), \ldots, (-1, \ldots, -1, n)$. Each facet is given by the equation $x_i = -1$ or $x_1 + \cdots + x_n = 1$, and the corresponding primitive inner normal vectors are $e_i \in N$ and $-(e_1 + \cdots + e_n) \in N$, respectively. Therefore the dual polytope of $\Delta$ is

$$\Delta^\circ = \operatorname{conv}\{ e_1, e_2, \ldots, e_n, -(e_1 + e_2 + \cdots + e_n) \}$$

which is again a lattice polytope. That is, $\Delta$ is a reflexive polytope. Meanwhile, since the normal fan of $\Delta$ coincides with the standard fan of $\mathbb{P}^n$ verified in [§Definition of Toric Varieties, ⁋Example 10](/en/math/toric_geometry/toric_varieties#ex10){: data-lid="y3bwq" }, we have $X_\Delta \cong \mathbb{P}^n$.

In this example, because we enlarged the size of $\Delta$, now $\Delta$ can have multiple lattice points on its boundary and interior in addition to its vertices. For instance, when $n=2$, the lattice points of $\Delta = \operatorname{conv}\{(-1,-1), (2,-1), (-1,2)\}$ are

$$(-1,-1), (-1,0), (-1,1), (-1,2), (0,-1), (0,0), (0,1), (1,-1), (1,0), (2,-1)$$

for a total of $10$ points, and one can verify that this coincides with $h^0(\mathbb{P}^2, \mathcal{O}_{\mathbb{P}^2}(3)) = 10$.
:::

## Mirror Symmetry

If we look again at [Example 6](#ex6){: data-lid="8srko" } above, an interesting phenomenon appears: although $\Delta$ and $\Delta^\circ$ are two aspects of the same reflexive data, the toric varieties $X_\Delta$ and $X_{\Delta^\circ}$ constructed from them are generally very different from each other. For example, in the case of the modified standard simplex with $n=2$, we have $X_\Delta \cong \mathbb{P}^2$, whereas for $\Delta^\circ = \mathrm{conv}\{(1,0), (0,1), (-1,-1)\}$, computing the determinants of adjacent rays in its normal fan gives values of $\pm3$, so it is not even a smooth variety. ([§Definition of Toric Varieties, ⁋Proposition 11](/en/math/toric_geometry/toric_varieties#prop11){: data-lid="8id7w" }) In fact, $X_{\Delta^\circ}$ is the singular Gorenstein Fano surface $\mathbb{P}^2/(\mathbb{Z}/3)$, with a $\mathbb{Z}/3$ quotient singularity in each of its three maximal cones.

A natural question is whether there is a geometric relationship between these two varieties $X_\Delta$ and $X_{\Delta^\circ}$. As we saw in the simple example above, in general there is no direct morphism or birational isomorphism between $X_\Delta$ and $X_{\Delta^\circ}$. Instead, the true connection between the two is revealed through anticanonical hypersurfaces. The starting point is the following classical adjunction result.

::: Proposition 7
For a smooth Fano variety $X$, in the anticanonical linear system $\lvert -K_X \rvert$, a smooth divisor $V \subseteq X$ has a trivial canonical bundle. That is, $K_V = 0$.
:::

::: Proof
We use the adjunction formula $K_V = (K_X + V)\vert_V$ from [\[Algebraic Varieties\] §Canonical Line Bundle](/en/math/algebraic_varieties/canonical_bundle){: data-lid="qj8gk" }. Since $V \in \lvert -K_X \rvert$, we have $V \sim -K_X$, and therefore

$$K_V = (K_X + V)\vert_V = (K_X - K_X)\vert_V = 0$$

holds.
:::

As mentioned above, the relationship between $X_\Delta$ and $X_{\Delta^\circ}$ is not of an easily visible kind, and it is also impossible to explain it rigorously in the remainder of this post. The two are related through mirror symmetry, which is, in a word, the conjecture that two (usually non-isomorphic) Calabi-Yau varieties are *paired* through a certain symmetry of Hodge data.

The conclusion $K_V = 0$ of [Proposition 7](#prop7){: data-lid="cmxaq" } gives room for $V$ to enter the stage of this mirror symmetry, in that it is (almost) exactly the algebraic condition characterizing a *Calabi-Yau variety*. Likewise, if we repeat the same construction for $X_{\Delta^\circ}$ as well, we will also be able to define for this $V$ its "mirror pair" $V^\circ$.

However, in general, for a reflexive polytope $\Delta$, $X_\Delta$ constructed from it is singular, and this gives rise to two subtle problems.

1. When the codimension $1$ $V$ meets the singular locus of $X_\Delta$, $V$ itself becomes singular at those points. In our example $\mathbb{P}^2/(\mathbb{Z}/3)$, the singular locus consists of three isolated points, so a generic cubic curve $V$ can avoid them and be chosen to be smooth; but as the dimension grows, the singular locus becomes positive-dimensional, and the phenomenon appears where $V$ necessarily crosses it. Therefore, the conclusion of [Proposition 7](#prop7){: data-lid="cmlt1" } cannot be applied directly to a *singular* $V$.
2. Therefore, to obtain a genuine smooth Calabi-Yau from a singular $V$, an appropriate resolution $\pi: \widetilde{V} \rightarrow V$ is needed, but a general resolution does not preserve the canonical class. Specifically, it is known that an arbitrary resolution of a normal Gorenstein variety $V$ satisfies the following *discrepancy formula*:
    
    $$K_{\tilde{V}} = \pi^\ast K_V + \sum_i a_i E_i$$
    
    Here the $E_i$ are the exceptional divisors of $\pi$, and $a_i \in \mathbb{Q}$ are rational numbers called the *discrepancies*. In this formula, the part where $\pi^\ast K_V$ fails to accurately capture the vanishing/pole structure of differential forms on $\tilde{V}$ is corrected by $a_i E_i$, and the sign and magnitude of $a_i$ become standard invariants classifying the types of singular points of $V$.
    
    Now even if $V$ satisfies $K_V \sim 0$ by adjunction, for an arbitrary resolution we have
    
    $$K_{\tilde{V}} = \pi^\ast \cdot 0 + \sum_i a_i E_i = \sum_i a_i E_i$$
    
    and generically there exist terms with $a_i > 0$, so $K_{\tilde{V}} \not\sim 0$, that is, $\tilde{V}$ loses the Calabi-Yau property.

Therefore, the only kind of resolution that *preserves* the Calabi-Yau property is one where all $a_i = 0$, and such a resolution is defined as follows.

::: Definition 8
For a normal Gorenstein variety $X$, when a resolution of singularities $\pi: \tilde{X} \rightarrow X$ (that is, $\tilde{X}$ is smooth and $\pi$ is a proper birational morphism) satisfies

$$K_{\tilde{X}} = \pi^\ast K_X$$

it is called a *crepant resolution*.
:::

That is, a crepant resolution is a resolution with no discrepancy. Then we can immediately verify that this condition is exactly what is needed to carry the conclusion of [Proposition 7](#prop7){: data-lid="5ftqb" } into the singular setting, and from this $\widetilde{V}$ becomes a genuine (smooth) Calabi-Yau.

In the toric setting, crepant resolutions translate into very explicit lattice data. We already saw in the discussion following [§Definition of Toric Varieties, ⁋Proposition 11](/en/math/toric_geometry/toric_varieties#prop11){: data-lid="wj05d" } that a general toric resolution is given by a refinement of a fan (that is, a finer fan on the same support). Then the real question would be when this resolution is crepant, and this too can be expressed in terms of combinatorial properties of the fan. Specifically, a birational morphism $\pi: X_{\Sigma'} \rightarrow X_\Delta$ is crepant if and only if the newly added rays $v$ are all lattice points lying on the *boundary* of $\Delta^\circ$.

Intuitively, this can be understood as saying that the anticanonical piecewise linear function $\psi_{-K}$ introduced right after [Proposition 3](#prop3){: data-lid="illur" } must, for a new ray $v$ as well, still satisfy $\psi_{-K}(v) = -1$. This is because if $v$ lies in the interior of a cone $\sigma$ (vertex $u_\sigma$), $\psi_{-K}(v) = \langle u_\sigma, v\rangle = -1$ is precisely equivalent to $v$ lying on the $\Delta^\circ$ facet $F_{u_\sigma}$. For example, in the fan of $\mathbb{P}^2/(\mathbb{Z}/3)$, if we add the boundary lattice points of $\Delta$ other than its vertices, $(0,-1), (1,-1), (1,0), (0,1), (-1,0), (-1,1)$, as new rays, the three $\mathbb{Z}/3$ singular points are resolved simultaneously, and the result is a smooth fan with nine rays.

However, crepant resolutions do not always exist. In the case of toric Gorenstein varieties, it is known that a crepant resolution always exists for $n \le 3$, but for $n \ge 4$ it is generally impossible to resolve all singular points simultaneously. Now, what was introduced to absorb the cohomology contributions of the remaining quotient singular points is the *stringy* Hodge numbers appearing in the mirror statement below, and thanks to this correction, mirror symmetry is cleanly expressed as a function of reflexive data, regardless of the singular remnants.

Batyrev's key insight is that the two Calabi-Yau families $V, V^\circ$ are *mirror dual* to each other. More specifically, for the two families constructed from a reflexive pair $(\Delta, \Delta^\circ)$,

$$\bigl\{ V \subseteq X_\Delta : V \in \lvert -K_{X_\Delta}\rvert \bigr\}, \qquad \bigl\{ V^\circ \subseteq X_{\Delta^\circ} : V^\circ \in \lvert -K_{X_{\Delta^\circ}}\rvert \bigr\}$$

the stringy Hodge numbers of their generic members satisfy the following mirror symmetry when $n \ge 4$:

$$h^{p,q}_{\mathrm{st}}(V) = h^{n-1-p, q}_{\mathrm{st}}(V^\circ)$$

That is, this does not mean that $X_\Delta$ and $X_{\Delta^\circ}$ themselves are equivalent, but rather that the Calabi-Yau hypersurface families on them are paired through mirror symmetry. This is the geometric content of reflexive duality.

---

**References**

**[Bat]** V. V. Batyrev, *Dual polyhedra and mirror symmetry for Calabi-Yau hypersurfaces in toric varieties*, J. Algebraic Geom. 3 (1994), 493--535.  
**[CLS]** David Cox, John Little, Hal Schenck, *Toric Varieties*, Graduate Studies in Mathematics, American Mathematical Society, 2011.  
**[Ful]** William Fulton, *Introduction to Toric Varieties*, Annals of Mathematics Studies, Princeton University Press, 1993.
