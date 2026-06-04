---
title: "The Givental J-Function and the Mirror Theorem"
description: "Starting from basic definitions, we prove the Givental J-function as a fundamental solution of the quantum differential equation and discuss its relation to explicit hypergeometric functions and the mirror theorem for toric Fano varieties."
excerpt: "Fundamental solutions of quantum differential equations and the I equals J theorem"

categories: [Math / Mirror Symmetry]
permalink: /en/math/mirror_symmetry/givental_j_function
sidebar: 
    nav: "mirror_symmetry-en"

date: 2026-05-28
last_modified_at: 2026-06-02
weight: 6
translated_at: 2026-06-02T08:30:01+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-02T08:30:01+00:00
---
In [§Dubrovin Connection, §§D-module](/en/math/mirror_symmetry/dubrovin_connection#d-module) we showed that the quantum differential equation (QDE) on the quantum cohomology side admits a space of solutions of dimension $$\dim_\mathbb{C} H^\ast(X)$$ consisting of flat sections, and we foreshadowed that the explicit formula for its fundamental solution is *Givental's $$J$$-function*. Meanwhile, in [§Gauss–Manin Connection, ⁋Proposition 7](/en/math/mirror_symmetry/gauss-manin_connection#prop7) we examined how the period matrix $$\mathcal{I}^a_p$$ on the B-side forms the fundamental solution matrix of the B-model connection $$\nabla^z_B$$. The mirror theorem we foreshadowed will ultimately crystallize into the statement that the A-side $$J$$-function and the B-side period matrix are fundamental solutions of the same $$D$$-module, and this post fills in the missing A-side slot in that claim.

## Descendant Gromov–Witten invariant

Before defining the $$J$$-function, let us briefly summarize the *descendant* invariant ([\[Symplectic Geometry\] §Gromov–Witten Invariants, ⁋Definition 2](/en/math/symplectic_geometry/gromov_witten#def2)) in the notation of this post. On the moduli space of stable maps of genus $$0$$, with $$(n+1)$$ marked points and class $$\beta$$,

$$\overline{\mathcal{M}}_{0, n+1}(X, \beta)$$

there are evaluation maps $$\ev_i: \overline{\mathcal{M}}_{0, n+1}(X, \beta) \to X$$ at each marked point $$i$$ and universal cotangent line bundles $$\mathbb{L}_i$$. Intuitively, $$\mathbb{L}_i$$ is the family of cotangent lines at the $$i$$-th marked point parametrized over the moduli space, and the first Chern class of this universal cotangent line bundle

$$\psi_i := c_1(\mathbb{L}_i) \in H^2(\overline{\mathcal{M}}_{0, n+1}(X, \beta))$$

is called the *$$\psi$$-class*.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1 (Descendant Gromov–Witten invariant)**</ins> For any cohomology classes $$\gamma_i \in H^\ast(X)$$ and integers $$k_i \geq 0$$, the *descendant Gromov–Witten invariant* is defined by

$$\left\langle \tau_{k_1}(\gamma_1), \ldots, \tau_{k_{n+1}}(\gamma_{n+1})\right\rangle_{0, n+1, \beta} := \int_{[\overline{\mathcal{M}}_{0, n+1}(X, \beta)]^{\mathrm{vir}}} \prod_{i=1}^{n+1} \psi_i^{k_i} \smile \ev_i^\ast \gamma_i$$

When all $$k_i = 0$$ it is called a *primary* invariant; if at least one $$k_i \geq 1$$ it is called a *gravitational descendant*.

</div>

Although working with moduli spaces requires a slight upgrade in language, the Chern class of a stack carries essentially the same intuitive meaning as that of an ordinary line bundle. That is, $$\psi_i$$ measures how much $$\mathbb{L}_i$$ is twisted over the moduli space. More concretely, given a $$2$$-cycle $$\Sigma$$ in the moduli base, the pairing

$$\int_\Sigma \psi_i\in \mathbb{Z}$$

is the same as observing the monodromy action: it records how much the fiber twists back onto itself when $$\mathbb{L}_i$$ is carried once around $$\Sigma$$. In the simplest case where this value is $$1$$, it means that the degree of $$\mathbb{L}_i$$ restricted to $$\Sigma$$ is $$1$$, and more intuitively we may interpret this as the monodromy being concentrated at a virtual point on $$\Sigma$$—a phase factor. Of course there is freedom in choosing this point, but this freedom comes exactly from choosing a representative of the cohomology class $$\psi_i$$; therefore, more generally, $$\int_\Sigma\psi_i = n$$ corresponds to arranging $$n$$ such points.

A well-known fact is that these $$n$$ points can actually be thought of as the intersections of $$\Sigma$$ with the boundary divisors of the moduli space, i.e., the loci where the source curve degenerates. Thus $$\psi_i$$ can be regarded as carrying information about the degeneration of the source curve.

It is then clear that the $$\psi_i^{k_i}$$ factors in [Definition 1](#def1) govern the degeneration of the source curve, while the $$\ev_i^\ast\gamma_i$$ impose incidence conditions on the target. In particular, the latter condition requires that the image of the $$i$$-th marked point $$p_i$$ pass through $$\gamma_i$$. However, the first condition is somewhat less intuitive, so let us unpack its meaning.

We saw earlier that $$\psi_i$$ can essentially be expressed as a sum of degenerations of the source curve. More concretely, suppose the source curve degenerates by splitting the marked points $$1,\ldots, n$$ into two components $$S$$ and $$S^c$$, and let $$D_S$$ denote the corresponding boundary divisor. Here we assume $$i\in S$$, and call the component containing $$i$$ the *tail*. Since three points are needed to stabilize $$\mathbb{P}^1$$, both $$S$$ and $$S^c$$ must contain at least two points.

Intuitively, $$\psi_i$$ can be thought of as a sum of boundary divisors arising in this manner, $$\sum_{i\in S} D_S$$, but if left as is the same cohomology class would be counted multiple times, so a reference choice is needed to remove the redundancy. That is, fixing $$j,k$$, the component corresponding to $$S^c$$ must be pinned down by $$j,k$$ and the nodal point to kill the automorphism of this $$\mathbb{P}^1$$.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2 (Genus 0 Topological Recursion Relation)**</ins> For fixed three indices $$i,j,k$$ of $$\{1, \ldots, n\}$$ ($$n\geq 4$$), the $$\psi$$-class $$\psi_i$$ is expressed as the following sum of boundary divisors:

$$\psi_i=\sum_{\substack{S \subset \{1, \ldots, n\} \\ i \in S, j, k \notin S, \lvert S\rvert \geq 2}} D_S \in H^2(\overline{\mathcal{M}}_{0, n})$$

</div>

Then for the moduli space of stable maps to a given target $$X$$, namely $$\overline{\mathcal{M}}_{0, n}(X, \beta)$$, the above formula can be pulled back via the forgetful morphism $$\overline{\mathcal{M}}_{0, n}(X, \beta) \to \overline{\mathcal{M}}_{0, n}$$.

We can now understand $$\psi_i^{k_i}$$ more clearly. From this perspective, $$\psi_i^{k_i}$$ simply means that the part corresponding to marked point $$p_i$$ degenerates $$k_i$$ times into a tail degeneration, and putting this together, the descendant GW invariant can be thought of as a virtual count of stable maps simultaneously satisfying *target incidence* and *source depth-$$k_i$$ tail degeneration* conditions.

To collect all these gravitational invariants at once, we consider the formal geometric series

$$\frac{1}{z - \psi} = \frac{1}{z}\cdot\frac{1}{1 - \psi/z} = \sum_{k \geq 0} z^{-k-1}\psi^k$$

For example, inserting the $$\psi$$-class only in the last factor gives

$$\begin{aligned}\left\langle \gamma_1, \ldots, \gamma_n, \frac{\gamma_{n+1}}{z - \psi}\right\rangle_{0, n+1, \beta}&=\left\langle \gamma_1, \ldots, \gamma_n, \sum_{k \geq 0} z^{-k-1}\psi^k\gamma_{n+1}\right\rangle_{0, n+1, \beta}=\sum_{k\geq 0}z^{-k-1}\left\langle \gamma_1, \ldots, \gamma_n, \psi^k\gamma_{n+1}\right\rangle_{0, n+1, \beta}\\&=\sum_{k \geq 0} z^{-k-1} \left\langle \gamma_1, \ldots, \gamma_n, \tau_k(\gamma_{n+1})\right\rangle_{0, n+1, \beta}\end{aligned}$$

so that each descendant invariant of depth $$k$$ is separated as the $$z^{-k-1}$$ coefficient and captured all at once. At first glance this merely packages the infinite sum on the right-hand side, but in the next section we will see that when the $$J$$-function is introduced, even the $$z$$ on the right-hand side acquires a specific meaning.

## Introduction of the $$J$$-function

We now introduce the $$J$$-function using the gravitational invariants examined above. Consider a smooth projective variety $$X$$, a homogeneous basis $$\{ T_a \}_{a=0,\ldots,s}$$ of $$H^\ast(X, \mathbb{C})$$ ($$T_0 = 1$$), and the Poincaré dual basis $$\{ T^a \}$$ they induce. Taking the $$H^2$$ components as $$\{ T_a \}_{a=1,\ldots,r}$$ (for notational simplicity), the flat coordinates $$t^a$$ and Novikov variables $$q_a := e^{t^a}$$ ($$a = 1, \ldots, r$$) introduced in [§Dubrovin Connection, §§D-module](/en/math/mirror_symmetry/dubrovin_connection#d-module) are defined. For convenience, setting

$$t_{(2)} := \sum_{b=1}^r t^b T_b$$

we have $$q^\beta = e^{t_{(2)} \cdot \beta}$$. Meanwhile, the Dubrovin connection was defined by the formula

$$\nabla^z = \partial + z^{-1}\mathcal{C}$$

but in this post, to match signs with the oscillating-integral side, we consider its *dual Dubrovin connection*

$$\nabla^{z, \vee} := -\nabla^{-z} = \partial - z^{-1}\mathcal{C}$$

and the horizontal section equation of this connection

$$z q_a\partial_{q_a} s = T_a \qtimes s \qquad (a = 1, \ldots, r)\tag{$\ast$}$$

To find a solution to this equation, let us first examine the situation where $$z\rightarrow \infty$$. Then as $$z\rightarrow\infty$$ the $$z^{-1}\mathcal{C}$$ term disappears and the connection degenerates to the standard differential $$\partial$$, so the leading-order horizontal section of ($$\ast$$) becomes a horizontal section of $$\partial$$, i.e., a constant section independent of $$q$$. More generally, a solution vanishing in the $$z\rightarrow \infty$$ limit would be of the form

$$s=s_0+\frac{s_1}{z}+\frac{s_2}{z^2}+\cdots$$

and from the above computation we saw that the zeroth-order term $$s_0$$ can be taken as a constant section, so substituting the form

$$s=1+\frac{s_1}{z}+\frac{s_2}{z^2}+\cdots$$

into ($$\ast$$) allows us to determine the $$s_i$$ recursively. Concretely, organizing both sides of ($$\ast$$) by powers of $$z$$, the left-hand side is

$$z \cdot \sum_k z^{-k} q_a\partial_{q_a} s_k = \sum_k z^{-k} q_a\partial_{q_a} s_{k+1}$$

since $$s_0$$ is constant, and the right-hand side is $$\sum_k z^{-k} T_a\qtimes s_k$$, so comparing the $$z^{-k}$$ coefficients yields the general recursion

$$q_a\partial_{q_a} s_{k+1} = T_a \qtimes s_k \qquad (a = 1, \ldots, r, k \geq 0)$$

At the first step of the recursion, $$k = 0$$, we have $$T_a \qtimes 1 = T_a$$, so without any quantum correction $$q_a\partial_{q_a} s_1 = T_a$$ holds. Integrating both sides with respect to $$q_a$$ gives

$$s_1=t_{(2)} + C_1,\qquad C_1\in H^\ast(X)$$

The interesting part is $$k=1$$, where quantum correction first appears; considering the recursion formula

$$q_a\partial_{q_a} s_2 = T_a \qtimes t_{(2)}=T_a\qtimes \left(\sum_{b=1}^r t^b T_b\right)$$

the right-hand side now carries, in addition to the classical cup product $$T_a\smile t_{(2)}$$, the quantum correction term

$$\sum_{\beta \neq 0} q^\beta \sum_c \left(\sum_{b=1}^r t^b \langle T_a, T_b, T^c\rangle_{0, 3, \beta}\right) T_c$$

Since $$T_b \in H^2$$, applying the result of [\[Symplectic Geometry\] §Gromov–Witten Invariants, ⁋Proposition 4](/en/math/symplectic_geometry/gromov_witten#prop4)

$$\langle T_a, T_b, T^c\rangle_{0, 3, \beta} = (T_b \cdot \beta)\langle T_a, T^c\rangle_{0, 2, \beta}$$

yields the formula

$$T_a \qtimes t_{(2)} = T_a \smile t_{(2)} + \sum_{\beta \neq 0} q^\beta (t_{(2)} \cdot \beta) \sum_c \langle T_a, T^c\rangle_{0, 2, \beta} T_c$$

Let us integrate this with respect to $$q_a$$. The antiderivative of the classical part $$T_a \smile t_{(2)}$$ is $$(t_{(2)})^2/2$$, which can be verified directly using $$q_a\partial_{q_a} = \partial_{t^a}$$:

$$\partial_{t^a}\bigl((t_{(2)})^2/2\bigr) = \partial_{t^a}\!\left(\frac{1}{2}\sum_{b, c} t^b t^c T_b \smile T_c\right) = \sum_c t^c T_a \smile T_c = T_a \smile t_{(2)}$$

The antiderivative of the quantum part is resolved $$\beta$$-by-$$\beta$$ using the relation $$q_a\partial_{q_a} q^\beta = (T_a \cdot \beta) q^\beta$$ coming from $$q^\beta = e^{t_{(2)}\cdot \beta}$$, and for each $$\beta$$ it organizes into an $$H^\ast(X)$$-valued correction determined by the $$q^\beta$$ factor and *primary* GW invariants (descendant invariants without $$\psi$$-class insertions) $$\langle T_a, T^c\rangle_{0, 2, \beta}$$. Therefore $$s_2$$ becomes the sum of the classical $$(t_{(2)})^2/2$$ and this quantum correction. At higher orders $$z^{-k}$$ ($$k \geq 2$$), following the same recursion, *gravitational descendants* of the form $$\tau_{k-1}(T_a)$$ accumulate in turn, and the $$J$$-function is ultimately the explicit one-line formula for the fundamental solution forced by this process.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> The (small) *Givental $$J$$-function* $$J_X: (\mathbb{C}^\ast)^r \times \mathbb{C}^\ast \to H^\ast(X)$$ of $$X$$ is defined by

$$J_X(q, z) := e^{t_{(2)}/z}\left( 1 + \sum_{\substack{\beta \in H_2(X, \mathbb{Z})_{\mathrm{eff}} \\ \beta \neq 0}} \sum_{a=0}^s q^\beta \left\langle \frac{T_a}{z(z - \psi)} \right\rangle_{0, 1, \beta} T^a \right)$$

</div>

Here $$H_2(X, \mathbb{Z})_{\mathrm{eff}}$$ is the set of effective curve classes (defined in [\[Symplectic Geometry\] §Quantum Cohomology, §§Novikov Ring](/en/math/symplectic_geometry/quantum_cohomology#novikov-ring)), and as $$\beta$$ ranges over this set, each $$\beta \neq 0$$ contributes to the instanton correction of degree $$q^\beta$$.

Since we have already verified the formula

$$\left\langle \gamma_1, \ldots, \gamma_n, \frac{\gamma_{n+1}}{z - \psi}\right\rangle_{0, n+1, \beta}=\sum_{k \geq 0} z^{-k-1} \left\langle \gamma_1, \ldots, \gamma_n, \tau_k(\gamma_{n+1})\right\rangle_{0, n+1, \beta}$$

the above $$J$$-function can be expanded as

$$J_X(q, z) = e^{t_{(2)}/z}\left(\mathbf{1} + \sum_{\substack{\beta \in H_2(X, \mathbb{Z})_{\mathrm{eff}} \\ \beta \neq 0}}\sum_{a = 0}^s \sum_{k \geq 0} q^\beta z^{-k-2} \langle\tau_k(T_a)\rangle_{0, 1, \beta} T^a\right)$$

Thus, this function can be thought of essentially as a generating function obtained by attaching the single-marked-point descendant invariants

$$\bigl\{\langle\tau_k(T_a)\rangle_{0, 1, \beta}\bigr\}_{\beta \in H_2(X, \mathbb{Z})_{\mathrm{eff}} \setminus \{0\}, a = 0, \ldots, s, k \geq 0}$$

to the Novikov parameter $$q^\beta$$, the spectral parameter $$z^{-k-2}$$, and the basis elements $$T^a$$ of cohomology.

Note that while the descendant invariants we defined above are generally of the multi-marked-point form

$$\left\langle \tau_{k_1}(\gamma_1), \ldots, \tau_{k_{n+1}}(\gamma_{n+1})\right\rangle_{0, n+1, \beta}$$

we have only put single marked points into the formula. This is possible because $$\beta\neq 0$$, so the target is sufficiently large that stability is guaranteed regardless of source stability, and the reason it suffices to look at only these is essentially that we are primarily considering the $$H^2$$-direction deformation, i.e., small quantum cohomology.

More concretely, we have already seen from [\[Symplectic Geometry\] §Gromov–Witten Invariants, ⁋Proposition 4](/en/math/symplectic_geometry/gromov_witten#prop4) that inserting a divisor $$D\in H^2(X)$$ into a Gromov–Witten invariant has the effect of multiplying by $$D\cdot \beta$$, and expanding this as a power series shows that looking at the $$H^2$$ direction is nothing more than multiplying by $$e^{t_{(2)}\cdot \beta}$$ in front, i.e., reparametrizing the Novikov variable as $$q^\beta \mapsto e^{t_{(2)}\cdot \beta}q^\beta$$. In [Definition 3](#def3) we have further multiplied the $$T_a/(z-\psi)$$ term by an additional factor of $$z^{-1}$$,[^1] so reflecting this $$z$$-shift as well, the overall prefactor attached to the $$J$$-function becomes $$e^{t_{(2)}/z}$$. Once all $$H^2$$-direction dependence is packed into $$e^{t_{(2)}/z}$$ and the Novikov variable, the Gromov–Witten information condenses into the remaining single marked point, so it suffices to look at single-marked-point invariants.

Meanwhile, recall that our motivation for introducing the $$J$$-function was to find the fundamental solution of the QDE ($$\ast$$). In [§Dubrovin Connection, §§D-module](/en/math/mirror_symmetry/dubrovin_connection#d-module) we saw that the A-model $$D$$-module is the bundle with fiber $$H^\ast(X)$$ over each point $$(q, z)$$ of the base $$M_A = (\mathbb{C}^\ast)^r \times \mathbb{C}^\ast_z$$, and the connection 1-form $$\mathcal{C}_a = T_a \qtimes -$$ on it was an endomorphism of this fiber, whose solutions were exactly the horizontal sections of ($$\ast$$). These solutions are $$\dim_\mathbb{C}H^\ast(X)$$-dimensional, and if we solve this equation with the $$T_a$$ as initial values, we obtain exactly all the solutions. Through this process we obtain the following fundamental solution matrix.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4 (A-side fundamental solution matrix)**</ins> Define the endomorphism $$S(q, z) \in \End(H^\ast(X))$$ by the matrix elements

$$\eta\bigl(S(q,z)T_a, T_b\bigr) := \eta(T_a, T_b) + \sum_{\beta \neq 0} q^\beta \left\langle \frac{T_a}{z - \psi}, T_b \right\rangle_{0, 2, \beta}$$

where $$\eta$$ is the Poincaré pairing. Then $$S$$ satisfies the following.

1. *(Flat section property)* Each column $$S(q, z) T_b$$ of $$S(q, z)$$ is a horizontal section of the dual small Dubrovin connection $$\nabla^{z, \vee}$$. That is,
   
   $$z q_a\partial_{q_a} \bigl(S(q,z)T_b\bigr) = T_a \qtimes \bigl(S(q,z)T_b\bigr)\qquad (a = 1, \ldots, r)$$

2. *($$J$$ = $$T_0$$ column)* $$J_X(q, z) = e^{t_{(2)}/z} S(q, z) T_0$$ holds. In particular $$J$$ itself is also a horizontal section of ($$\ast$$), and
   
   $$z q_a\partial_{q_a} J_X = T_a \qtimes J_X \qquad (a = 1, \ldots, r)$$

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

First, let us show that substituting $$T_b = T_0 = 1$$ in the second slot of the defining equation for $$S$$ gives the $$J = T_0$$ column. Throughout this post we consistently follow the convention $$1/(z - \psi) = \sum_{k \geq 0} z^{-k-1}\psi^k$$, and accordingly we keep the divisor-equation correction term with a $$+$$ sign (some literature uses $$1/(z + \psi)$$ with the opposite sign). Now the 2-point descendant in the definition involves $$T_0 = 1$$, and expanding this as a geometric series gives

$$\left\langle \frac{T_a}{z - \psi}, 1\right\rangle_{0, 2, \beta} = \sum_{k \geq 0} z^{-k-1}\langle \tau_k(T_a), 1\rangle_{0, 2, \beta}$$

Applying [\[Symplectic Geometry\] §Gromov–Witten Invariants, ⁋Proposition 3](/en/math/symplectic_geometry/gromov_witten#prop3) to each term gives

$$\langle \tau_k(T_a), 1\rangle_{0, 2, \beta} = \langle \tau_{k-1}(T_a)\rangle_{0, 1, \beta}$$

for all $$k\geq 1$$. The $$k = 0$$ term vanishes as an empty sum because there is no $$\psi$$ to pull down from the string-equation right-hand side, so $$\langle T_a, 1\rangle_{0, 2, \beta} = 0$$ ($$\beta \neq 0$$) (this is none other than the fact that a marked point evaluating the fundamental class contributes nothing when $$\beta \neq 0$$). Therefore the power-series degrees shift down by one, giving the formula

$$\sum_{k \geq 1} z^{-k-1}\langle \tau_{k-1}(T_a)\rangle_{0, 1, \beta} = \sum_{m \geq 0} z^{-m-2}\langle \tau_m(T_a)\rangle_{0, 1, \beta} = \left\langle \frac{T_a}{z(z - \psi)}\right\rangle_{0, 1, \beta}$$

This is exactly the term appearing inside the small $$J$$ formula of [Definition 3](#def3), and multiplying by the prefactor $$e^{t_{(2)}/z}$$ gives $$J_X = e^{t_{(2)}/z} S(q, z) T_0$$. This is the origin of the additional $$z^{-1}$$ that may have looked somewhat awkward in [Definition 3](#def3).

Now let us show that each column $$S(q,z)T_b$$ of $$S$$ is a horizontal section. For this, we directly apply $$z q_a\partial_{q_a}$$ to $$S(q, z) T_b$$. First, $$S(q, z) T_b$$ is expressed as a sum of terms with $$q^\beta$$ as a factor for each $$\beta$$, and using the recursion relation examined before introducing the $$J$$-function and [\[Symplectic Geometry\] §Gromov–Witten Invariants, ⁋Proposition 4](/en/math/symplectic_geometry/gromov_witten#prop4), $$z q_a\partial_{q_a}$$ ultimately inserts $$T_a$$ at a point while lowering the degree of $$\psi$$ by one in the $$1/(z - \psi)$$ of the distinguished marked point, multiplied by the attached $$z$$.

Now this lowered-degree $$\psi$$ can be decomposed into a sum of boundary divisors $$\sum_S D_S$$ using [Proposition 2](#prop2) (more precisely, the version with target lifted from [Proposition 2](#prop2)). On each $$D_S$$, the source curve splits into two components with effective class $$\beta = \beta_1 + \beta_2$$, and the diagonal class $$\sum_c T_c \otimes T^c$$ appears at the node between them. The component where the newly inserted $$T_a$$ gathers gives a 3-point invariant $$\langle T_a, T_c, T_d\rangle_{0, 3, \beta_1}$$, i.e., the structure constant expressing the quantum product $$T_a \qtimes$$ in a basis, and the other component reconstructs the (lower-degree) $$\beta_2$$ part of $$S(q, z) T_b$$ having $$T^c$$ at the node. Therefore summing over all $$c$$ and splittings $$\beta = \beta_1 + \beta_2$$ exactly reconstructs applying $$T_a \qtimes$$ to the vector $$S(q, z) T_b$$, i.e., the right-hand side $$T_a \qtimes \bigl(S(q, z) T_b\bigr)$$.

</details>

Therefore as $$q\rightarrow 0$$ all $$q^\beta$$ terms vanish, so the classical limit of $$S$$ is $$\id$$. On the A-side this can be thought of as a consequence of the fact that the classical limit of the quantum cup product is the ordinary cup product.

[Proposition 4](#prop4) shows that the $$J$$-function is more than a mere package of enumerative data: it forms a column of the A-model fundamental solution matrix $$S$$, specifically the column corresponding to the normalization element $$T_0 = 1$$. This is exactly the counterpart to the period matrix $$\mathcal{I}$$ in [§Gauss–Manin Connection, ⁋Proposition 7](/en/math/mirror_symmetry/gauss-manin_connection#prop7) forming the fundamental solution matrix of $$\nabla^z_B$$ trivialized by the frame $$\{e_a\}$$.

In particular, when $$H^\ast(X)$$ is generated by $$H^2(X)$$—for instance when $$X = \mathbb{P}^n$$ or for most toric Fano varieties—this single column $$J$$ in fact determines all of $$S$$. Indeed, repeatedly applying the flat-section equation $$z q_a\partial_{q_a} J = T_a \qtimes J$$ from [Proposition 4](#prop4) generates $$T_{a_1} \qtimes \cdots \qtimes T_{a_k} \qtimes J$$ in turn, and since $$H^\ast(X)$$ is generated by $$H^2$$ these quantum products sweep through all $$T_b$$ as a cohomology basis, so the remaining columns $$S(q, z) T_b$$ are also reconstructed from derivatives of $$J$$. This justifies in [Conjecture 5](#conj5) why our "mirror theorem" makes a claim only about the first column.

Meanwhile, this calculation is also related to the treatment of integration constants obtained by computing from ($$\ast$$) and performing repeated integrations, namely that the $$S$$ in [Proposition 4](#prop4) is the solution where these integration constants are set to zero at all orders. That is, after peeling off the components coming from $$t_{(2)}$$ as the prefactor $$e^{t_{(2)}/z}$$, all remaining corrections carry only instanton degrees $$q^\beta$$ for $$\beta \neq 0$$, so that as above the classical limit emerges as $$q \to 0$$.

## Mirror theorem

We have independently constructed the A-side fundamental solution matrix $$S$$ ([Proposition 4](#prop4)) and the B-side period matrix $$\mathcal{I}$$ ([§Gauss–Manin Connection, ⁋Proposition 7](/en/math/mirror_symmetry/gauss-manin_connection#prop7)). One of the insights of mirror symmetry is that these two matrices actually coincide.

<div class="proposition" markdown="1">

<ins id="conj5">**Conjecture 5 (Mirror theorem, $$J$$-function form)**</ins> For a mirror pair $$(X, \check{X})$$, the $$J$$-function of $$X$$ is written in terms of the cohomology basis $$\{T^a\}$$ components of the oscillating integral over a certain Lefschetz thimble $$\Gamma_0$$ (the *distinguished* thimble determined in a neighborhood of the large radius limit) corresponding to the $$T_0 = 1$$ normalization. That is,

$$J_X(q, z) = \sum_a J^a(q, z) T^a,\qquad J^a(q, z) \;\propto\; \mathcal{I}^a_{\Gamma_0}(q, z) = \int_{\Gamma_0} T_a\, e^{W_q/z}\,\omega$$

holds up to normalization. Here the right-hand side is the $$p = \Gamma_0$$ column of the period matrix $$\mathcal{I}^a_p$$ introduced in [§Gauss–Manin Connection, ⁋Proposition 7](/en/math/mirror_symmetry/gauss-manin_connection#prop7).

</div>

The above [Conjecture 5](#conj5) is one of the strongest formulations of mirror symmetry: all A-side descendant Gromov–Witten invariants are reconstructed from B-side period integrals. Then in particular, the classical ring-level mirror symmetry $$QH^\ast(X) \cong \Jac(W_q)$$ is recovered as the leading order as $$z\rightarrow 0$$. Concretely, the $$z \to 0$$ stationary-phase asymptotic ([§Gauss–Manin Connection, ⁋Proposition 3](/en/math/mirror_symmetry/gauss-manin_connection#prop3)) expands as a sum over critical points of $$W_q$$, and the leading-order critical values $$\{W_q(p)\}$$ recover the canonical coordinates of quantum cohomology.

This claim is not merely a repetition of [§Dubrovin Connection, ⁋Conjecture 4](/en/math/mirror_symmetry/dubrovin_connection#conj4). To see this, we must first show that the QDE satisfied by the $$J$$-function ([Proposition 4](#prop4)) and the Gauss–Manin system satisfied by the period matrix ([§Gauss–Manin Connection, ⁋Proposition 7](/en/math/mirror_symmetry/gauss-manin_connection#prop7)) define the same $$D$$-module, which is the content of [§Dubrovin Connection, ⁋Conjecture 4](/en/math/mirror_symmetry/dubrovin_connection#conj4). After that, we must verify that the $$J$$-function, i.e., the first column of the matrix $$S$$, maps under the isomorphism of [§Dubrovin Connection, ⁋Conjecture 4](/en/math/mirror_symmetry/dubrovin_connection#conj4) not to an arbitrary linear combination of thimble periods, but precisely to the oscillating integral over the distinguished thimble $$\Gamma_0$$. For this, an additional claim that the *integral structures* on both sides match is needed; on the A-side the lattice is defined by $$K$$-theory and the $$\hat{\Gamma}$$-class, and on the B-side the lattice generated by Lefschetz thimbles plays this role.

In the case of Calabi–Yau hypersurfaces in toric varieties, this was proven by Givental and Lian–Liu–Yau, and for our main object of interest, toric Fano varieties, the *$$I = J$$* theorem in the next section provides an explicit and computable form of this claim.

## Givental's Mirror Theorem

In the case of toric Fano varieties, the B-side oscillating integral is computed in an explicit *hypergeometric* form. The object defined through this is the *$$I$$-function*, which serves as the toric mirror counterpart of the $$J$$-function.

<div class="definition" markdown="1">

<ins id="def6">**Definition 6 (Givental's $$I$$-function)**</ins> Let $$X$$ be a smooth projective toric Fano variety, $$D_1, \ldots, D_m$$ the toric divisors, and $$\beta \in H_2(X, \mathbb{Z})$$ an effective curve class. The *$$I$$-function* of $$X$$ is defined by

$$I_X(q, z) := e^{t_{(2)}/z} \sum_{\beta \in H_2(X, \mathbb{Z})_{\mathrm{eff}}} q^\beta \prod_{i=1}^m \frac{\prod_{k=-\infty}^{0} (D_i + kz)}{\prod_{k=-\infty}^{D_i \cdot \beta}(D_i + kz)}$$

</div>

Here the formally appearing infinite products to $$-\infty$$ cancel exactly between numerator and denominator, so this is in fact a well-defined expression reducing to a finite product (or its inverse) depending on the sign of $$D_i \cdot \beta$$. The data determining this product are only the toric divisor $$D_i$$ and its intersection number $$D_i \cdot \beta$$, and the information these two carry is the same as that contained in the *charge matrix* $$Q = (Q_{ji}) \in \Mat_{r \times m}(\mathbb{Z})$$ introduced in [§Overview of Mirror Symmetry, ⁋Definition 1](/en/math/mirror_symmetry/overview#def1).

Let $$X$$ be a smooth projective toric variety. Then we have the short exact sequence

$$0 \longrightarrow H_2(X, \mathbb{Z}) \xrightarrow{\ \iota\ } \mathbb{Z}^m \xrightarrow{\ e_i \mapsto v_i\ } \mathbb{Z}^n \longrightarrow 0$$

Here $$m$$ is the number of rays, and $$\mathbb{Z}^n$$ is the cocharacter lattice. That is, $$H_2$$ is identified with the set of relations among rays

$$\{(a_i)_i \in \mathbb{Z}^m : \sum_i a_i v_i = 0\}$$

The charge matrix is by definition the matrix whose rows are these $$r$$ relations, and therefore it carries precisely the information about a basis of $$H_2(X, \mathbb{Z})$$. That is, the preimage $$\beta_j=\iota^{-1}(Q_{j\bullet})$$ of each row $$(Q_{j\bullet})$$ of $$\mathbb{Z}^m$$ forms a basis of $$H_2(X, \mathbb{Z})$$, and in this setting the intersection with toric divisor $$D_i$$ is nothing but reading the $$i$$-th coordinate of $$\beta=(a_i)_i$$, so $$D_i\cdots\beta_j=Q_{ji}$$.

The origin of this formula is the oscillating integral on the Hori–Vafa mirror $$\check{X}$$ of $$X$$, or more precisely, the expansion of this integral over charge data for the distinguished thimble $$\Gamma_0$$ of [Conjecture 5](#conj5) is exactly $$I_X$$. That is, $$I_X$$ is nothing more than the explicit formula for the distinguished column of the period matrix $$\mathcal{I}$$ in [§Gauss–Manin Connection, ⁋Proposition 7](/en/math/mirror_symmetry/gauss-manin_connection#prop7). We postpone the detailed expansion of this to [Example 8](#ex8), and first translate this into a statement about the $$J$$-function.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7 (Givental's mirror theorem)**</ins> When $$X$$ is a smooth projective toric Fano variety, the $$I$$-function and $$J$$-function of $$X$$ satisfy the relation

$$J_X(\tau(q), z) = I_X(q, z)$$

where $$\tau(q)$$ is the mirror map defined from the asymptotic expansion of the $$I$$-function

$$I_X(q, z) = 1 + \tau(q)/z + O(z^{-2})$$

</div>

Examining both sides for the proof, $$J_X$$ is as seen in [Proposition 4](#prop4) the fundamental solution of the small QDE ($$\ast$$), and $$I_X$$ is the hypergeometric function explicitly given by charge data in [Definition 6](#def6). The key to the proof is to directly verify that this explicit $$I_X$$ is also a solution of the same $$D$$-module as $$J_X$$, i.e., of the same QDE ($$\ast$$). If $$X$$ is toric Fano then $$H^\ast(X)$$ is generated by $$H^2(X)$$, so ($$\ast$$) reduces to a differential equation for a single component of $$I_X$$, and at this point feeding $$z q_a\partial_{q_a}$$ into the hypergeometric product of $$I_X$$ verifies that each factor of the product satisfies this equation term by term. Meanwhile both $$I_X$$ and $$J_X$$ have the normalization $$1 + O(z^{-1})$$ as $$z \to \infty$$, and since the solution of the QDE is uniquely determined from its leading asymptotic once $$a_0$$ is fixed, we obtain $$J_X(\tau(q), z) = I_X(q, z)$$. We will verify this with a concrete calculation for $$X = \mathbb{P}^n$$. ([Example 8](#ex8))

Note that the mirror map being well-defined is thanks to the Fano property of $$X$$. If $$X$$ is Fano then for all non-zero effective curve classes $$\beta$$ we have $$-K_X \cdot \beta > 0$$, so the $$q^\beta$$ corrections appear only at orders $$z^{-1}$$ and below, and therefore the $$z^0$$ term of $$I_X$$ is exactly $$1$$ ($$I_X = 1 + O(z^{-1})$$), allowing us to read off $$\tau(q)$$ as the $$z^{-1}$$ coefficient. More generally, in the *semi-positive* case where $$-K_X$$ is merely nef, directions with $$-K_X \cdot \beta = 0$$ produce a correction $$I_0(q) \neq 1$$ in the $$z^0$$ degree, and the relation is modified to $$J_X(\tau(q), z) = I_X(q, z)/I_0(q)$$.

Similarly, consider the case where the Fano index of $$X$$ is at least $$2$$. Here the *Fano index* $$r_X$$ is the largest positive integer such that there exists $$H \in \Pic(X)$$ with $$-K_X = r_X H$$. In this case $$H = -K_X / r_X$$ is also ample, so for non-zero effective curve classes $$\beta$$ we have $$H \cdot \beta \geq 1$$, and therefore

$$-K_X \cdot \beta = r_X (H \cdot \beta) \geq 2$$

so the $$q$$-dependent corrections are pushed to orders $$z^{-2}$$ and below. As a result no $$q$$-corrections remain in the mirror map $$\tau(q)$$, and in this case $$J_X(q, z) = I_X(q, z)$$ holds without any coordinate change. The $$\mathbb{P}^n$$ in the following [Example 8](#ex8) ($$-K = (n+1)H$$, Fano index $$n+1 \geq 2$$) is such a case.

<div class="example" markdown="1">

<ins id="ex8">**Example 8** ($$X = \mathbb{P}^n$$)</ins> The fan of $$\mathbb{P}^n$$ is the normal fan of the standard simplex, with $$n+1$$ rays

$$v_0 = -e_1 - \cdots - e_n,\qquad v_i = e_i\quad (i = 1, \ldots, n)$$

([\[Toric Geometry\] §Definition of Toric Varieties, ⁋Example 10](/en/math/toric_geometry/toric_varieties#ex10)) The toric divisors are $$D_0, \ldots, D_n$$ corresponding to the respective coordinate hyperplanes, and since these are all linearly equivalent they define a single hyperplane class $$H\in H^2(\mathbb{P}^n)$$. Moreover, the cohomology computation of $$\mathbb{P}^n$$ tells us that this hyperplane class generates the entire cohomology of $$\mathbb{P}^n$$.

Let us now unpack the data entering the $$I$$-function formula of [Definition 6](#def6) for $$\mathbb{P}^n$$. First, since $$H^2(\mathbb{P}^n)$$ is generated by a single $$H$$, we have $$t_{(2)} = tH$$ and the Novikov variable is given by $$q = e^t$$. That is, since $$t = \ln q$$, we can write $$e^{t_{(2)}/z} = e^{H \ln q / z}$$.

Next, effective curve classes are parametrized by non-negative multiples of the line class $$H^\vee$$, namely $$\beta = d H^\vee$$ ($$d \geq 0$$), so $$q^\beta = q^d$$, and the $$n+1$$ toric divisors $$D_0, \ldots, D_n$$ of $$\mathbb{P}^n$$ ([\[Toric Geometry\] §Torus Invariants and Line Bundles, ⁋Example 11](/en/math/toric_geometry/toric_divisors#ex11)) all satisfy $$D_i \cdot \beta = H \cdot d H^\vee = d$$, so substituting this, the infinite products to $$-\infty$$ cancel and each factor reduces to

$$\frac{\prod_{k=-\infty}^{0}(D_i + kz)}{\prod_{k=-\infty}^{D_i \cdot \beta}(D_i + kz)} = \frac{\prod_{k=-\infty}^{0}(H + kz)}{\prod_{k=-\infty}^{d}(H + kz)} = \frac{1}{\prod_{j=1}^{d}(H + jz)}$$

and since there is such a factor for each of the $$n+1$$ toric divisors, raising to the $$(n+1)$$-st power gives the $$I$$-function

$$I_{\mathbb{P}^n}(q, z) = e^{H \ln q /z} \sum_{d \geq 0} \frac{q^d}{\prod_{j=1}^d (H + jz)^{n+1}}$$

Since $$H^{n+1} = 0$$, expanding $$(H + jz)^{-(n+1)}$$ in the denominator as a power series in $$z^{-1}$$ and Taylor-expanding $$e^{H\ln q/z}$$, then collecting by degrees, gives the following expansion:

$$I_{\mathbb{P}^n}(q, z) = 1 + \frac{H \ln q}{z} + \frac{(H \ln q)^2}{2 z^2} + \cdots + q \frac{1}{(H+z)^{n+1}} + \cdots$$

Now the Fano index of $$\mathbb{P}^n$$ is $$n+1 \geq 2$$ from $$-K_{\mathbb{P}^n} = (n+1) H$$. In the above expansion, the $$q$$-dependent corrections (the $$q^d$$ terms for $$d \geq 1$$) appear only at orders $$z^{-(n+1)}$$ and below, so the $$z^{-1}$$ coefficient of $$I_{\mathbb{P}^n}$$ is only $$H \ln q$$ (i.e., $$t_{(2)}$$) coming from the prefactor. Therefore, as discussed right after [Proposition 7](#prop7), the mirror map is the identity and

$$J_{\mathbb{P}^n}(q, z) = I_{\mathbb{P}^n}(q, z)$$

must hold. Let us verify this directly.

The B-side calculation is more or less finished in [§Gauss–Manin Connection, ⁋Example 8](/en/math/mirror_symmetry/gauss-manin_connection#ex8). According to it, for the fundamental solution matrix $$\mathcal{I}_p^a(q,z)$$ of $$\mathbb{P}^n$$, the first component $$\mathcal{I}_p^0(q,z)$$ of the vector corresponding to the Lefschetz thimble base $$\Gamma_p$$ must satisfy the equation

$$(z\partial_q)(qz\partial_q)^n\mathcal{I}_p^0=\mathcal{I}_p^0 \tag{$\ast\ast$}$$

We now show that setting $$H=0$$ in the above $$I$$-function satisfies this equation. By ($$\ast$$), applying $$qz\partial_q$$ is the same as taking the quantum product with $$H$$, which is exactly the same as inductively computing the $$\mathcal{I}_p^a$$ from $$\mathcal{I}_p^0$$ on the B-side, and therefore showing that these are solutions of the same ODE when $$H=0$$ completes the verification of [Proposition 7](#prop7).

Then from the product formula of [Definition 6](#def6), the prefactor becomes $$e^0 = 1$$ and each factor becomes $$(H + jz) \mapsto jz$$, so we obtain the formula

$$\Phi_0(q, z) := I_{\mathbb{P}^n}(q, z)\big\vert_{H=0} = \sum_{d \geq 0} \frac{q^d}{(d!)^{n+1}z^{(n+1)d}}$$

Let us directly verify that this $$\Phi_0$$ satisfies ($$\ast\ast$$). A direct computation shows that the action of $$qz\partial_q$$ pulls out $$d$$ term by term and attaches a $$z^{-1}$$ factor, so

$$(qz\partial_q)^n\Phi_0 = \sum_{d\geq 0}\frac{d^n q^d}{(d!)^{n+1}z^{(n+1)d - n}},$$

and applying $$z\partial_q$$ once more pulls out another $$d$$ and shifts $$d$$ to $$d - 1$$, giving

$$(z\partial_q)(qz\partial_q)^n\Phi_0 = \sum_{d \geq 1}\frac{d^{n+1}q^{d-1}}{(d!)^{n+1}z^{(n+1)d - n - 1}} = \sum_{d' \geq 0}\frac{(d'+1)^{n+1}q^{d'}}{((d'+1)!)^{n+1}z^{(n+1)d'}} = \Phi_0$$

which is exactly verified.

The stationary-phase aspect of [Conjecture 5](#conj5) was also already computed in [§Gauss–Manin Connection, ⁋Example 8](/en/math/mirror_symmetry/gauss-manin_connection#ex8), but this falls somewhat outside our core concerns in this post, so we omit it.

</div>

This example shows that mirror symmetry is realized not as an abstract isomorphism but as a concrete coincidence of two hypergeometric series. In the case of general toric Fano varieties, similar explicit calculations proceed from the charge matrix, and in all such cases the $$I = J$$ theorem of [Proposition 7](#prop7) provides a practical verification of mirror symmetry.

## Extension to big quantum cohomology

The small $$J$$-function we have treated so far was the fundamental solution for the small quantum $$D$$-module based on the $$H^2$$-direction deformation from [§Dubrovin Connection, §§D-module](/en/math/mirror_symmetry/dubrovin_connection#d-module). As seen in the earlier part of the same post, the Dubrovin connection itself was defined on big quantum cohomology based on the full $$H^\ast(X)$$ deformation, and the small version looking only at the $$H^2$$ direction was a specialization of this. The same upgrade is possible for the $$J$$-function, and that is the *big $$J$$-function*.

To go to the big version setup, we must introduce the general deformation parameter $$t = \sum_{a=0}^s t^a T_a$$ of $$H^\ast(X)$$. The big quantum product $$\star_t$$ for arbitrary $$t \in H^\ast(X)$$ determines the connection $$1$$-form of the Dubrovin connection as $$\mathcal{C}_\alpha = T_\alpha \star_t -$$, as seen in [§Dubrovin Connection, §§D-module](/en/math/mirror_symmetry/dubrovin_connection#d-module). Its dual horizontal section equation is

$$z\partial_{t^a} s = T_a \star_t s\qquad (a = 0, 1, \ldots, \dim_\mathbb{C} H^\ast(X) - 1)$$

which is the *big QDE* extending ($$\ast$$) to the full $$H^\ast$$ direction.

<div class="definition" markdown="1">

<ins id="def9">**Definition 9 (Big $$J$$-function)**</ins> The *big Givental $$J$$-function* $$J_X^{\mathrm{big}}: H^\ast(X) \times \mathbb{C}^\ast \to H^\ast(X)$$ of $$X$$ is defined by

$$J_X^{\mathrm{big}}(t, z) := e^{t_{(2)}/z}\left( 1 + \sum_{\substack{\beta \in H_2(X, \mathbb{Z})_{\mathrm{eff}}, n \geq 0 \\ (\beta, n) \neq (0, 0)}} \sum_{a=0}^s \frac{q^\beta}{n!} \left\langle \frac{T_a}{z - \psi}, t, \ldots, t \right\rangle_{0, n+1, \beta} T^a \right)$$

Here the first marked point carries $$T_a/(z-\psi)$$ (i.e., the pullback of $$T_a$$ with all degree $$\psi^k$$ inserted in generating-function form), and the remaining $$n$$ marked points all carry $$t \in H^\ast(X)$$, making a total of $$n+1$$ marked points.

</div>

That the big $$J$$-function forms a horizontal section of the big QDE follows by the same argument as the small version of [Proposition 4](#prop4). The small $$J$$-function is recovered as the $$t = t_{(2)} \in H^2(X)$$ specialization of the big $$J$$-function; applying the divisor equation (with descendant correction term) $$n$$ times to $$H^2$$ insertions makes the $$t_{(2)}$$ insertions come out as $$(t_{(2)} \cdot \beta)^n$$ factors and $$\psi$$-shift corrections, these sum to $$\sum_n (t_{(2)}\cdot \beta)^n/n! = q^\beta$$, and the $$\psi$$-shift correction produces an additional $$z^{-1}$$ factor, so that the small $$J$$-function form of [Definition 3](#def3) with a single marked point is directly recovered.

The additional information carried by the big $$J$$-function is all descendant invariants determined by arbitrary cohomology classes. On this basis the mirror theorem ([Conjecture 5](#conj5)) also upgrades to a big version making the stronger claim of coincidence of the *full* $$S$$-matrix and the *full* period matrix, and $$I = J$$ ([Proposition 7](#prop7)) also has richer content in the generally non-trivial big version where the mirror map $$\tau(q)$$ is concerned.

---

**References**

**[CK]** D. A. Cox, S. Katz, *Mirror Symmetry and Algebraic Geometry*, Mathematical Surveys and Monographs **68**, AMS, 1999.

**[MS]** K. Hori, S. Katz, A. Klemm, R. Pandharipande, R. Thomas, C. Vafa, R. Vakil, E. Zaslow, *Mirror Symmetry*, Clay Mathematics Monographs **1**, AMS, 2003.

---

[^1]: Its origin is examined in the proof of [Proposition 4](#prop4).
