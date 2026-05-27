---
title: "Fano Varieties"
excerpt: "Reflexive polytopes and the corresponding Gorenstein Fano toric varieties"

categories: [Math / Toric Geometry]
permalink: /en/math/toric_geometry/reflexive_polytope_fano

header:
    overlay_image: /assets/images/Math/Toric_Geometry/Reflexive_Polytope_and_Fano_Variety.png
    overlay_filter: 0.5

sidebar:
    nav: "toric_geometry-en"

date: 2026-05-18
last_modified_at: 2026-05-18
weight: 4
translated_at: 2026-05-28T11:36:15+00:00
translation_source: kimi-cli
---
In [§Definition of Toric Varieties](/en/math/toric_geometry/toric_varieties) we saw how to construct a projective toric variety $$X_P$$ from a lattice polytope $$P \subset M_{\mathbb{R}}$$ via its normal fan $$\Sigma_P$$. In this construction there are many pathways by which the geometric properties of $$P$$ are translated into algebro-geometric properties of $$X_P$$, and among them *reflexive polytopes* occupy a special position.

## Reflexive Polytopes

First, fix a lattice $$M$$ and its dual lattice $$N = \Hom(M, \mathbb{Z})$$, and let $$\langle -, - \rangle : M_{\mathbb{R}} \times N_{\mathbb{R}} \to \mathbb{R}$$ be the natural dual pairing. Then via this pairing we can transport a given polytope to the opposite dual lattice. By definition, a *reflexive polytope* is one for which the result is again a lattice polytope.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A $$d$$-dimensional *lattice polytope* $$\Delta$$ in $$M_{\mathbb{R}}$$ is called a *reflexive polytope* if the following two conditions are satisfied:

1. The origin $$0$$ lies in the interior of $$\Delta$$.
2. The *dual polytope*

$$\Delta^\circ = \{ v \in N_{\mathbb{R}} \mid \langle u, v \rangle \ge -1 \text{ for all } u \in \Delta \}$$

is again a lattice polytope. That is, every vertex of $$\Delta^\circ$$ belongs to the lattice $$N$$.

</div>

The second condition is quite transparent in meaning, but the first may feel somewhat useless at first glance. Intuitively, if $$\Delta$$ does not contain the origin, then for some vector inside $$\Delta$$ its opposite direction vector does not exist, so by pairing with this vector and then taking a dual vector in the positive direction and continuing to enlarge it, the condition defining $$\Delta^\circ$$ becomes unbounded. This is why we require the two conditions above.

True to its name, the most basic property of a reflexive polytope is that the dual operation $$\Delta \mapsto \Delta^\circ$$ forms an involution on the collection of reflexive polytopes.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2 (Bipolar theorem)**</ins> If $$\Delta \subset M_{\mathbb{R}}$$ is a reflexive polytope, then $$\Delta^\circ \subset N_{\mathbb{R}}$$ is also a reflexive polytope, and $$(\Delta^\circ)^\circ = \Delta$$ holds.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Since $$\Delta$$ is reflexive, $$\Delta^\circ$$ is a lattice polytope by definition. Since $$\langle u, v \rangle \ge -1$$ holds for all $$u \in \Delta$$ and all $$v \in \Delta^\circ$$, we can directly verify from the definition that $$\Delta \subseteq (\Delta^\circ)^\circ$$.

To show the reverse direction, let $$w \in (\Delta^\circ)^\circ$$. Then $$w$$ satisfies $$\langle w, v \rangle \ge -1$$ for all $$v \in \Delta^\circ$$. Now consider each facet $$\Theta$$ of $$\Delta$$. Then $$\Theta$$ is a $$(d-1)$$-dimensional face on the boundary of $$\Delta$$, and by the definition of a reflexive polytope, $$\Theta$$ is given by the equation $$\langle u, v_\Theta \rangle = -1$$. Here $$v_\Theta \in N$$ is the primitive inner normal vector corresponding to $$\Theta$$. Since $$v_\Theta$$ becomes a vertex of $$\Delta^\circ$$, we have $$\langle w, v_\Theta \rangle \ge -1$$. This means that $$w$$ is contained in the intersection of the half-spaces defining all facets of $$\Delta$$, and therefore $$w \in \Delta$$. From this we obtain $$(\Delta^\circ)^\circ = \Delta$$. Finally, since $$(\Delta^\circ)^\circ = \Delta$$ is a lattice polytope, $$\Delta^\circ$$ is also reflexive.

</details>

This proposition exhibits the symmetry of reflexive polytopes. Although $$\Delta$$ and $$\Delta^\circ$$ lie in different vector spaces $$M_{\mathbb{R}}$$ and $$N_{\mathbb{R}}$$, they provide two aspects of the same combinatorial object.

## Fano Varieties

In algebraic geometry, a *Fano variety* is a normal projective variety $$X$$ whose anticanonical divisor $$-K_X$$ is ample. Here the canonical divisor $$K_X$$ is the divisor class corresponding to the canonical bundle ([\[Algebraic Varieties\] §Canonical Bundles, ⁋Definition 6](/en/math/algebraic_varieties/canonical_bundle#def6)), and $$-K_X$$ is its inverse. If $$-K_X$$ is additionally a Cartier divisor, then $$X$$ is called a *Gorenstein Fano variety*. In the context of toric varieties, this condition translates into a very explicit combinatorial condition.

As we saw in [§Definition of Toric Varieties, ⁋Proposition 8](/en/math/toric_geometry/toric_varieties#prop8), given a lattice polytope $$P \subset M_{\mathbb{R}}$$, we can construct the projective toric variety $$X_P = X_{\Sigma_P}$$ via the normal fan $$\Sigma_P$$ it defines. Now assume that $$P = \Delta$$ is a reflexive polytope.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> The anticanonical divisor $$-K_{X_\Sigma}$$ of a toric variety $$X_\Sigma$$, i.e. the inverse of the canonical divisor, is given by the sum of all boundary divisors:

$$-K_{X_\Sigma} = \sum_{\rho \in \Sigma(1)} D_\rho.$$

Here $$\Sigma(1)$$ is the set of 1-dimensional cones of $$\Sigma$$, and each $$D_\rho$$ is the torus-invariant prime divisor corresponding to $$\rho$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

In [\[Algebraic Varieties\] §Canonical Bundles, ⁋Definition 6](/en/math/algebraic_varieties/canonical_bundle#def6), the canonical divisor $$K_X$$ was defined as the divisor class corresponding to the canonical bundle $$\omega_X = \det \Omega^1_X$$. We show that $$K_{X_\Sigma} = -\sum_\rho D_\rho$$, so that its inverse takes the form above.

On the open dense torus $$T_N = \operatorname{Spec} \mathbb{C}[M] \subset X_\Sigma$$, if we choose a basis $$m_1, \ldots, m_n$$ of $$M$$, then the characters $$\chi^{m_i}$$ become coordinates on the torus, and the top form

$$\omega = \frac{d\chi^{m_1}}{\chi^{m_1}} \wedge \cdots \wedge \frac{d\chi^{m_n}}{\chi^{m_n}}$$

trivializes $$\Omega^n_{T_N}$$. This is a $$T_N$$-invariant top form independent of the choice of basis of $$M$$, and it extends naturally to a rational $$n$$-form on $$X_\Sigma$$.

Now let us compute the vanishing degree of $$\omega$$ along each boundary divisor $$D_\rho$$. Choose a suitable basis of $$N$$ with the primitive generator $$v_\rho \in N$$ of the ray $$\rho \in \Sigma(1)$$ as the first basis vector, and take the dual basis $$m_1, \ldots, m_n$$ of $$M$$. Then in the affine chart $$U_\sigma$$ having $$\rho$$ as a face, the local equation of $$D_\rho$$ is $$\chi^{m_1} = 0$$. In the above expression, the term $$d\chi^{m_1}/\chi^{m_1}$$ creates exactly a first-order pole along $$D_\rho$$, while the other factors are regular near $$D_\rho$$, so $$\omega$$ has exactly a first-order pole along $$D_\rho$$. Therefore

$$\operatorname{div}(\omega) = -\sum_{\rho \in \Sigma(1)} D_\rho$$

and since $$K_{X_\Sigma}$$ is the class of this divisor, we have $$-K_{X_\Sigma} = \sum_\rho D_\rho$$.

</details>

Although this equality itself is well-defined for any fan, the *ample* condition that we are interested in (and the Fano condition) only makes sense when $$X_\Sigma$$ is complete, so hereafter we assume that $$\Sigma$$ is a complete fan.

When the anticanonical divisor $$-K_{X_\Sigma}$$ is a Cartier divisor, the corresponding piecewise linear function $$\psi_{-K} \in \PL(\Sigma, M)$$ is precisely the function satisfying $$\psi_{-K}(v_\rho) = -1$$ for all $$\rho \in \Sigma(1)$$. Moreover, in [§Torus-Invariant Divisors and Line Bundles, ⁋Proposition 6](/en/math/toric_geometry/toric_divisors#prop6) we saw that it suffices to check this condition only on maximal cones, and that this condition exactly coincides with the condition for the given divisor to be Cartier. The following proposition is the key observation that this condition exactly matches the vertex condition of the dual $$\Delta^\circ$$ of a reflexive polytope.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> For a reflexive polytope $$\Delta \subset M_{\mathbb{R}}$$, let $$\Sigma_\Delta$$ be the normal fan of $$\Delta$$ and write the corresponding toric variety as $$X_\Delta = X_{\Sigma_\Delta}$$. Then $$X_\Delta$$ is a Gorenstein Fano variety. Conversely, if a complete toric variety $$X_\Sigma$$ is Gorenstein Fano, then $$\Sigma$$ is the normal fan of some reflexive polytope.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Suppose $$\Delta$$ is a reflexive polytope. Each maximal cone $$\sigma$$ of $$\Sigma_\Delta$$ corresponds to some vertex $$u_\sigma$$ of $$\Delta$$ by [§Definition of Toric Varieties, ⁋Definition 6](/en/math/toric_geometry/toric_varieties#def6), and the ray generators $$v_\rho$$ of $$\sigma$$ are exactly the inner primitive normals of the facets containing $$u_\sigma$$. Since the facet equation of $$\Delta$$ is $$\langle u, v_\Theta \rangle = -1$$, the vertex $$u_\sigma$$ achieves the minimum of $$\langle -, v_\rho\rangle$$ on $$\Delta$$ exactly at $$-1$$. That is,

$$\langle u_\sigma, v_\rho\rangle = -1 \le \langle u, v_\rho\rangle \quad \text{for all } u \in \Delta, \rho \in \sigma(1)$$

and equality holds only when $$u \in F_\rho$$ (the facet). Therefore $$m_\sigma = u_\sigma \in M$$ satisfies the Cartier compatibility of [§Torus-Invariant Divisors and Line Bundles, ⁋Proposition 6](/en/math/toric_geometry/toric_divisors#prop6), and $$-K_{X_\Delta}$$ is Cartier.

On the other hand, to show the ampleness of $$-K_{X_\Delta}$$, it suffices to verify that the piecewise linear function $$\psi_{-K}$$ is strictly convex ([§Torus-Invariant Divisors and Line Bundles, ⁋Proposition 9](/en/math/toric_geometry/toric_divisors#prop9)). That is, for two distinct maximal cones $$\sigma, \sigma'$$ and their corresponding $$u_\sigma, u_{\sigma'}$$, we need to show that $$\langle u_{\sigma'}, v\rangle$$ is an upper bound for $$\psi_{-K}(v) = \langle u_\sigma, v\rangle$$ on $$v \in \sigma$$, with equality exactly when $$v \in \sigma \cap \sigma'$$.

Decompose $$v \in \sigma$$ as $$v = \sum_{\rho \in \sigma(1)} c_\rho v_\rho$$ ($$c_\rho \ge 0$$). For each $$\rho \in \sigma(1)$$, since $$u_{\sigma'} \in \Delta$$ we have $$\langle u_{\sigma'}, v_\rho \rangle \ge -1$$, and since $$u_\sigma \in F_\rho$$ we have $$\langle u_\sigma, v_\rho\rangle = -1$$. Therefore

$$\langle u_{\sigma'}, v\rangle = \sum_{\rho \in \sigma(1)} c_\rho \langle u_{\sigma'}, v_\rho\rangle \ge -\sum_{\rho \in \sigma(1)} c_\rho = \langle u_\sigma, v\rangle$$

and equality holds exactly when $$\langle u_{\sigma'}, v_\rho\rangle = -1$$ for all $$\rho$$ with $$c_\rho > 0$$, i.e. when $$u_{\sigma'} \in F_\rho$$. However, by the vertex structure of facets, "$$u_{\sigma'} \in F_\rho$$" is equivalent to "$$\rho \in \sigma'(1)$$", so the equality condition means that $$v$$ is combined only from rays of $$\sigma \cap \sigma'$$, which is exactly $$v \in \sigma \cap \sigma'$$. This proves strict convexity.

Conversely, assume that $$X_\Sigma$$ is Gorenstein Fano. Since $$-K_{X_\Sigma}$$ is Cartier, for each maximal cone $$\sigma$$ there exists $$m_\sigma \in M$$ such that $$\langle m_\sigma, v_\rho \rangle = -1$$ for all $$\rho \in \sigma(1)$$. Now define

$$\Delta = \{ u \in M_{\mathbb{R}} \mid \langle u, v_\rho \rangle \ge -1 \text{ for all } \rho \in \Sigma(1) \}.$$

Then $$\Delta$$ is a lattice polytope and $$0 \in \operatorname{int}(\Delta)$$. The dual of $$\Delta$$ is $$\Delta^\circ = \operatorname{conv}\{v_\rho \mid \rho \in \Sigma(1)\}$$, which is a lattice polytope, so $$\Delta$$ is reflexive. That $$\Sigma$$ is the normal fan of $$\Delta$$ follows from the definition.

</details>

Moreover, the correspondence between a reflexive polytope $$\Delta$$ and the Gorenstein Fano variety $$X_\Delta$$ extends beyond the mere existence of the variety, to a correspondence between sections of line bundles on it. Specifically, the global sections of the line bundle $$\mathcal{O}_{X_\Delta}(-K_{X_\Delta})$$ corresponding to the anticanonical divisor $$-K_{X_\Delta}$$ are in one-to-one correspondence with the lattice points inside the reflexive polytope $$\Delta$$.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> For a reflexive polytope $$\Delta \subset M_{\mathbb{R}}$$ and the corresponding toric variety $$X_\Delta$$, the following $$\mathbb{C}$$-vector space isomorphism holds:

$$H^0\bigl(X_\Delta, \mathcal{O}_{X_\Delta}(-K_{X_\Delta})\bigr) \cong \bigoplus_{u \in \Delta \cap M} \mathbb{C} \cdot \chi^u.$$

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

For a toric variety, the polytope $$P_D$$ corresponding to a $$T_N$$-invariant Cartier divisor $$D$$ is defined by

$$P_D = \{ u \in M_{\mathbb{R}} \mid \langle u, v_\rho \rangle \ge -a_\rho \text{ for all } \rho \in \Sigma(1) \},$$

and as shown in [§Torus-Invariant Divisors and Line Bundles, ⁋Proposition 7](/en/math/toric_geometry/toric_divisors#prop7), a basis of $$H^0(X_\Sigma, \mathcal{O}_{X_\Sigma}(D))$$ is given by the characters $$\chi^u$$ corresponding to the elements of $$P_D \cap M$$. For the anticanonical divisor $$-K_{X_\Delta}$$, we have $$a_\rho = 1$$ for all $$\rho$$, so

$$P_{-K} = \{ u \in M_{\mathbb{R}} \mid \langle u, v_\rho \rangle \ge -1 \text{ for all } \rho \in \Sigma_\Delta(1) \}.$$

Since $$\Sigma_\Delta$$ is the normal fan of $$\Delta$$, the polytope defined by the above inequalities coincides exactly with $$\Delta$$. Therefore $$P_{-K} = \Delta$$, and the desired isomorphism follows.

</details>

This result means that the number of lattice points of a reflexive polytope determines the dimension of the sections of the anticanonical line bundle of the Gorenstein Fano variety, i.e. the *anticanonical degree*. In particular, the number of elements of $$\Delta \cap M$$ equals $$h^0(X_\Delta, \mathcal{O}(-K_{X_\Delta}))$$.

The most basic example of a reflexive polytope is the simplex corresponding to projective space $$\mathbb{P}^n$$. In [§Definition of Toric Varieties, ⁋Example 10](/en/math/toric_geometry/toric_varieties#ex10) we saw that the normal fan of the standard simplex $$\Delta_n$$ is the standard fan of $$\mathbb{P}^n$$. However, since one of the vertices of $$\Delta_n$$ is the origin, we have $$0 \notin \operatorname{int}(\Delta_n)$$. Thus $$\Delta_n$$ itself is not a reflexive polytope. Instead, we can consider a (similar) polytope obtained by appropriately extending each edge of this polytope to move the origin into the interior.

<div class="example" markdown="1">

<ins id="ex6">**Example 6**</ins> In the lattice $$M = \mathbb{Z}^n$$, define the following polytope:

$$\Delta = \{ (x_1, \ldots, x_n) \in \mathbb{R}^n \mid x_i \ge -1 \;\text{for all}\; i,\; x_1 + x_2 + \cdots + x_n \le 1 \}.$$

This polytope is obtained by expanding the standard simplex in the direction of the origin, and its vertices are $$(-1, -1, \ldots, -1)$$ and $$(n, -1, \ldots, -1), \ldots, (-1, \ldots, -1, n)$$. Each facet is given by the equation $$x_i = -1$$ or $$x_1 + \cdots + x_n = 1$$, and the corresponding primitive inner normal vectors are $$e_i \in N$$ and $$-(e_1 + \cdots + e_n) \in N$$, respectively. Therefore the dual polytope of $$\Delta$$ is

$$\Delta^\circ = \operatorname{conv}\{ e_1, e_2, \ldots, e_n, -(e_1 + e_2 + \cdots + e_n) \},$$

which is again a lattice polytope. That is, $$\Delta$$ is a reflexive polytope. On the other hand, since the normal fan of $$\Delta$$ coincides with the standard fan of $$\mathbb{P}^n$$ that we checked in [§Definition of Toric Varieties, ⁋Example 10](/en/math/toric_geometry/toric_varieties#ex10), we have $$X_\Delta \cong \mathbb{P}^n$$.

In this example, since we enlarged $$\Delta$$, it can now have several lattice points on its boundary and interior in addition to its vertices. For example, when $$n=2$$, the lattice points of $$\Delta = \operatorname{conv}\{(-1,-1), (2,-1), (-1,2)\}$$ are

$$(-1,-1), (-1,0), (-1,1), (-1,2), (0,-1), (0,0), (0,1), (1,-1), (1,0), (2,-1),$$

for a total of $$10$$ points, and we can verify that this coincides with $$h^0(\mathbb{P}^2, \mathcal{O}_{\mathbb{P}^2}(3)) = 10$$.

</div>

## Mirror Symmetry

If we look again at [Example 6](#ex6) above, an interesting phenomenon appears: although $$\Delta$$ and $$\Delta^\circ$$ are two aspects of the same reflexive data, the toric varieties $$X_\Delta$$ and $$X_{\Delta^\circ}$$ constructed from them are generally very different from each other. For example, in the case of the modified standard simplex with $$n=2$$, we have $$X_\Delta \cong \mathbb{P}^2$$, whereas for $$\Delta^\circ = \mathrm{conv}\{(1,0), (0,1), (-1,-1)\}$$, computing the determinants of adjacent rays in its normal fan gives values of $$\pm 3$$, so it is not even a smooth variety. ([§Definition of Toric Varieties, ⁋Proposition 11](/en/math/toric_geometry/toric_varieties#prop11)) In fact, $$X_{\Delta^\circ}$$ is the singular Gorenstein Fano surface $$\mathbb{P}^2/(\mathbb{Z}/3)$$ with a $$\mathbb{Z}/3$$ quotient singularity in each of its three maximal cones.

A natural question is whether there is a geometric relationship between these two varieties $$X_\Delta$$ and $$X_{\Delta^\circ}$$. As we saw in the simple example above, in general there is no direct morphism or birational isomorphism between $$X_\Delta$$ and $$X_{\Delta^\circ}$$. Instead, the true connection between them is revealed through anticanonical hypersurfaces. The starting point is the following classical adjunction result.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> A smooth divisor $$V \subset X$$ in the anticanonical linear system $$\lvert -K_X \rvert$$ of a smooth Fano variety $$X$$ has trivial canonical bundle. That is, $$K_V = 0$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

We use the adjunction formula $$K_V = (K_X + V)\vert_V$$ from [\[Algebraic Varieties\] §Canonical Bundles](/en/math/algebraic_varieties/canonical_bundle). Since $$V \in \lvert -K_X \rvert$$, we have $$V \sim -K_X$$, and therefore

$$K_V = (K_X + V)\vert_V = (K_X - K_X)\vert_V = 0$$

holds.

</details>

As mentioned above, the relationship between $$X_\Delta$$ and $$X_{\Delta^\circ}$$ is not of an easily visible kind, and it is impossible to explain it rigorously in the remainder of this post. These two are related through mirror symmetry, which is, in a word, the conjecture that two (usually non-isomorphic) Calabi-Yau varieties are *paired* through a certain symmetry of Hodge data.

The conclusion $$K_V = 0$$ of [Proposition 7](#prop7) gives $$V$$ a chance to step onto the stage of this mirror symmetry, since it is (almost) exactly the algebraic condition characterizing a *Calabi-Yau variety*. Likewise, if we repeat the same construction for $$X_{\Delta^\circ}$$, we should be able to define the "mirror pair" $$V^\circ$$ of this $$V$$.

However, in general the variety $$X_\Delta$$ constructed from a reflexive polytope $$\Delta$$ is singular, and this creates two subtle problems.

1. If the codimension-$$1$$ subvariety $$V$$ meets the singular locus of $$X_\Delta$$, then $$V$$ itself becomes singular at that point. In our example of $$\mathbb{P}^2/(\mathbb{Z}/3)$$, the singular locus consists of three isolated points, so a generic cubic curve $$V$$ can avoid them and remain smooth; but as the dimension grows, the singular locus can have positive dimension, causing $$V$$ to necessarily intersect it. Therefore we cannot directly apply the conclusion of [Proposition 7](#prop7) to a *singular* $$V$$.
2. Thus, to obtain a genuine smooth Calabi-Yau from a singular $$V$$, an appropriate resolution $$\pi: \widetilde{V} \to V$$ is needed, but a general resolution does not preserve the canonical class. Specifically, it is known that an arbitrary resolution of a normal Gorenstein variety $$V$$ satisfies the following *discrepancy formula*:

    $$K_{\tilde V} = \pi^\ast K_V + \sum_i a_i E_i.$$

    Here $$E_i$$ are the exceptional divisors of $$\pi$$, and $$a_i \in \mathbb{Q}$$ are rational numbers called the *discrepancies*. This formula expresses that $$\pi^\ast K_V$$ does not exactly capture the vanishing/pole structure of differential forms on $$\tilde V$$, and the terms $$a_i E_i$$ correct for this; the sign and magnitude of $$a_i$$ become standard invariants classifying the type of singularities of $$V$$.

    Now even if $$V$$ satisfies $$K_V \sim 0$$ by adjunction, for an arbitrary resolution we have

    $$K_{\tilde V} = \pi^\ast \cdot 0 + \sum_i a_i E_i = \sum_i a_i E_i$$

    and generically there exist terms with $$a_i > 0$$, so $$K_{\tilde V} \not\sim 0$$, i.e. $$\tilde V$$ loses the Calabi-Yau property.

Therefore the only kind of resolution that *preserves* the Calabi-Yau property is one where all $$a_i = 0$$, and such a resolution is defined as follows.

<div class="definition" markdown="1">

<ins id="def8">**Definition 8**</ins> A resolution of singularities $$\pi: \tilde{X} \to X$$ of a normal Gorenstein variety $$X$$ — that is, $$\tilde{X}$$ is smooth and $$\pi$$ is a proper birational morphism — satisfying

$$K_{\tilde{X}} = \pi^* K_X$$

is called a *crepant resolution*.

</div>

That is, a crepant resolution is a resolution with no discrepancy. Then we can immediately verify that this condition is exactly what is needed to carry the conclusion of [Proposition 7](#prop7) to the singular setting, and from this $$\widetilde{V}$$ becomes a genuine (smooth) Calabi-Yau.

In the toric setting, crepant resolutions translate into very explicit lattice data. We already saw in the discussion after [§Definition of Toric Varieties, ⁋Proposition 11](/en/math/toric_geometry/toric_varieties#prop11) that a general toric resolution is given by a refinement of a fan (i.e. a finer fan on the same support). Then the real question is when this resolution is crepant, and this too can be expressed in terms of combinatorial properties of the fan. Specifically, a birational morphism $$\pi: X_{\Sigma'} \to X_\Delta$$ is crepant if and only if all newly added rays $$v$$ lie on lattice points on the *boundary* of $$\Delta^\circ$$.

Intuitively, this can be thought of as the anticanonical piecewise linear function $$\psi_{-K}$$ from the proof of [Proposition 3](#prop3) still satisfying $$\psi_{-K}(v) = -1$$ for the new ray $$v$$. This is because if $$v$$ falls inside a cone $$\sigma$$ (with vertex $$u_\sigma$$), then $$\psi_{-K}(v) = \langle u_\sigma, v\rangle = -1$$ is exactly equivalent to $$v$$ lying on the facet $$F_{u_\sigma}$$ of $$\Delta^\circ$$. For example, if we add the lattice points $$(1,0), (0,1), (-1,-1)$$ between adjacent rays in the fan of $$\mathbb{P}^2/(\mathbb{Z}/3)$$ as new rays, all three $$\mathbb{Z}/3$$ singularities are resolved simultaneously, and the result becomes the fan of smooth $$\mathbb{P}^2$$.

However, crepant resolutions do not always exist. For toric Gorenstein varieties, it is known that crepant resolutions always exist for $$n \le 3$$, but for $$n \ge 4$$ it is generally impossible to resolve all singularities simultaneously. To absorb the remaining cohomological contributions of quotient singularities, *stringy* Hodge numbers were introduced, which appear in the mirror statement below; thanks to this correction, mirror symmetry is cleanly expressed as a function of reflexive data regardless of singular remnants.

Batyrev's key insight is that the two Calabi-Yau families $$V, V^\circ$$ form a *mirror dual* pair. More specifically, for the two families constructed from a reflexive pair $$(\Delta, \Delta^\circ)$$,

$$\bigl\{ V \subset X_\Delta : V \in \lvert -K_{X_\Delta}\rvert \bigr\}, \qquad \bigl\{ V^\circ \subset X_{\Delta^\circ} : V^\circ \in \lvert -K_{X_{\Delta^\circ}}\rvert \bigr\}$$

the stringy Hodge numbers of their generic members satisfy the following mirror symmetry for $$n \ge 4$$:

$$h^{p,q}_{\mathrm{st}}(V) = h^{n-1-p,\, q}_{\mathrm{st}}(V^\circ).$$

That is, it does not mean that $$X_\Delta$$ and $$X_{\Delta^\circ}$$ themselves are equivalent, but rather that the Calabi-Yau hypersurface families on them are paired through mirror symmetry — this is the geometric content of reflexive duality.

---

**References**

**[Bat]** V. V. Batyrev, *Dual polyhedra and mirror symmetry for Calabi-Yau hypersurfaces in toric varieties*, J. Algebraic Geom. 3 (1994), 493--535.

**[CLS]** David Cox, John Little, Hal Schenck, *Toric Varieties*, Graduate Studies in Mathematics, American Mathematical Society, 2011.

**[Ful]** William Fulton, *Introduction to Toric Varieties*, Annals of Mathematics Studies, Princeton University Press, 1993.
