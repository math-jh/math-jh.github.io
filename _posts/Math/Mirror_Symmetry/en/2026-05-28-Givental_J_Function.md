---
title: "Givental J-function and Mirror Theorem"
description: "Starting from the basic definitions, we prove its properties as a fundamental solution of the quantum differential equation and discuss the relationship between explicit hypergeometric functions for toric Fano varieties and the mirror theorem."
excerpt: "Fundamental solution of the quantum differential equation and the I=J theorem"

categories: [Math / Mirror Symmetry]
permalink: /en/math/mirror_symmetry/givental_j_function
sidebar: 
    nav: "mirror_symmetry-en"

date: 2026-05-28
weight: 6
translated_at: 2026-07-14T10:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-22T15:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
In [§Dubrovin Connection, §§D-module](/en/math/mirror_symmetry/dubrovin_connection#d-module){: data-lid="5xb2j" }, we showed that the quantum differential equation (QDE) on the quantum cohomology side has a $\dim_\mathbb{C} H^\ast(X)$-dimensional space of flat sections as its solution space, and announced that writing down its fundamental solution explicitly is *Givental's $J$-function*. Meanwhile, in [§Gauss-Manin Connection, ⁋Proposition 7](/en/math/mirror_symmetry/gauss-manin_connection#prop7){: data-lid="9t8qb" }, we saw that on the B-side, the period matrix $\mathcal{I}^a_p$ forms the fundamental solution matrix of the B-model connection $\nabla^z_B$. The mirror theorem we foreshadowed will ultimately be concretized as the statement that the A-side $J$-function and the B-side period matrix are fundamental solutions of the same $D$-module, and this post will fill the empty A-side slot in that claim.

## Descendant Gromov-Witten invariant

Before beginning the definition of the $J$-function, let us briefly summarize the *descendant* invariants used throughout this post ([\[Symplectic Geometry\] §Gromov-Witten Invariants, ⁋Definition 2](/en/math/symplectic_geometry/gromov_witten#def2)), adapted to the notation of this post. On the moduli space of genus $0$, $(n+1)$-marked, class $\beta$ stable maps

$$\overline{\mathcal{M}}_{0, n+1}(X, \beta)$$

the evaluation map $\ev_i: \overline{\mathcal{M}}_{0, n+1}(X, \beta) \rightarrow X$ at each marked point $i$ and the universal cotangent line bundle $\mathbb{L}_i$ are defined. Intuitively, $\mathbb{L}_i$ is obtained by gluing together the cotangent lines at the $i$-th marked points over the moduli space, and the first Chern class of this universal cotangent line bundle

$$\psi_i := c_1(\mathbb{L}_i) \in H^2(\overline{\mathcal{M}}_{0, n+1}(X, \beta))$$

is called the *$\psi$-class*.

::: Definition 1 (Descendant Gromov-Witten invariant)
For arbitrary cohomology classes $\gamma_i \in H^\ast(X)$ and $k_i \geq 0$, the *descendant Gromov-Witten invariant* is defined by

$$\left\langle \tau_{k_1}(\gamma_1), \ldots, \tau_{k_{n+1}}(\gamma_{n+1})\right\rangle_{0, n+1, \beta} := \int_{[\overline{\mathcal{M}}_{0, n+1}(X, \beta)]^{\mathrm{vir}}} \prod_{i=1}^{n+1} \psi_i^{k_i} \smile \ev_i^\ast \gamma_i$$

When $k_i = 0$, it is called a *primary* invariant; if at least one $k_i \geq 1$, it is called a *gravitational descendant*.
:::

Although dealing with moduli spaces involves a slight upgrade in language, essentially the intuitive meaning of the Chern class of a stack is also the same as the Chern class of an ordinary line bundle. That is, it is a quantity measuring how twisted $\mathbb{L}_i$ is over the moduli space. More concretely, given a $2$-cycle $\Sigma$ of the moduli base, the quantity given by $\psi_i$ through pairing with this cycle,

$$\int_\Sigma \psi_i\in \mathbb{Z}$$

is the same as looking at the monodromy action: that is, when going once along $\Sigma$, how much $\mathbb{L}_i$ is twisted and glued to the original fiber. In the simplest case, this value being $1$ means that the restriction to $\Sigma$ of $\mathbb{L}_i$ has degree $1$; more intuitively, we can interpret this as the phase factor, that is, the monodromy, being concentrated at that single point whenever passing through a virtual point on $\Sigma$. Of course, there is freedom in choosing this point, but this arises precisely from choosing a representative of the cohomology class of $\psi_i$, and thus more generally, $\int_\Sigma\psi_i$ being $n$ corresponds to arranging $n$ such points.

A well-known fact is that these $n$ points can actually be thought of as the intersections of $\Sigma$ with the boundary divisors of the moduli space, that is, the loci where the degeneration of the source curve occurs; thus $\psi_i$ can be thought of as carrying information about the degeneration of the source curve.

Then it is obvious that in [Definition 1](#def1){: data-lid="tlyw3" }, the $\psi_i^{k_i}$ components determine the degeneration of the source curve, while $\ev_i^\ast\gamma_i$ determines the incidence condition on the target. In particular, the latter condition is that the image of the $i$-th marked point $p_i$ passes through $\gamma_i$. However, the first condition is somewhat less intuitive, so let us examine its meaning in detail.

We have seen above that $\psi_i$ can essentially be represented as a sum of degenerations of the source curve. More concretely, suppose the source curve degenerates by splitting the marked points $1,\ldots, n$ into two components $S$ and $S^c$, and let $D_S$ be the corresponding boundary divisor. Here we assume $i\in S$, and call the component containing $i$ the *tail*. At this time, since three points are needed to make $\mathbb{P}^1$ stable, both $S$ and $S^c$ must contain at least two points.

Intuitively, $\psi_i$ can be thought of as the sum $\sum_{i\in S} D_S$ of boundary divisors arising in this manner, but if left as is, the same cohomology class would be counted multiple times, so a reference choice is needed to eliminate redundancy. That is, fixing $j,k$, on the component corresponding to $S^c$, we must use $j,k$ and the nodal point to kill the automorphism of this $\mathbb{P}^1$.

::: Proposition 2 (Genus 0 Topological Recursion Relation)
For three fixed distinct indices $i,j,k$ of $\{1, \ldots, n\}$ ($n\geq 4$), the $\psi$-class $\psi_i$ is represented as the sum of the following boundary divisors:

$$\psi_i=\sum_{\substack{S \subseteq \{1, \ldots, n\} \\ i \in S, j, k \notin S, \lvert S\rvert \geq 2}} D_S \in H^2(\overline{\mathcal{M}}_{0, n})$$

:::

::: Proof
When $n = 4$, $\overline{\mathcal{M}}_{0,4} \cong \mathbb{P}^1$ and $\psi_i$ is a point class of degree $1$, which is linearly equivalent to the unique boundary divisor $D_{\{i, l\}}$ separating $i$ from $j, k$ ($l$ is the fourth index), so it matches the right-hand side for $n = 4$. For general $n$, comparing cotangent line classes under the forgetful morphism $\pi: \overline{\mathcal{M}}_{0,n} \rightarrow \overline{\mathcal{M}}_{0,4}$ that leaves only $i, j, k$ and one point, we find that $\psi_i$ differs from $\pi^\ast \psi_i$ by the boundary where $i$ is separated from $j, k$; repeatedly applying this yields the boundary sum on the right-hand side. This is a standard fact for $\overline{\mathcal{M}}_{0,n}$ ([CK, §10]).
:::

Then, on the moduli space of stable maps $\overline{\mathcal{M}}_{0, n}(X, \beta)$ with a given target $X$, we can also transfer the above formula via the pullback under the forgetful morphism $\overline{\mathcal{M}}_{0, n}(X, \beta) \rightarrow \overline{\mathcal{M}}_{0, n}$.

Now we can understand $\psi_i^{k_i}$ more clearly. From the viewpoint above, $\psi_i^{k_i}$ simply means a degenerate cycle belonging to a tail where the part corresponding to the marked point $p_i$ degenerates $k_i$ times; putting this together, the descendant GW invariant can be thought of as the virtual counting of stable maps simultaneously satisfying the two conditions of *target incidence* and *source depth-$k_i$ tail degeneration*.

Now, in order to consider these gravitational invariants all at once, we consider the formal geometric series

$$\frac{1}{z - \psi} = \frac{1}{z}\cdot\frac{1}{1 - \psi/z} = \sum_{k \geq 0} z^{-k-1}\psi^k$$

For example, inserting the $\psi$ class only into the last factor gives

$$\begin{aligned}\left\langle \gamma_1, \ldots, \gamma_n, \frac{\gamma_{n+1}}{z - \psi}\right\rangle_{0, n+1, \beta}&=\left\langle \gamma_1, \ldots, \gamma_n, \sum_{k \geq 0} z^{-k-1}\psi^k\gamma_{n+1}\right\rangle_{0, n+1, \beta}=\sum_{k\geq 0}z^{-k-1}\left\langle \gamma_1, \ldots, \gamma_n, \psi^k\gamma_{n+1}\right\rangle_{0, n+1, \beta}\\&=\sum_{k \geq 0} z^{-k-1} \left\langle \gamma_1, \ldots, \gamma_n, \tau_k(\gamma_{n+1})\right\rangle_{0, n+1, \beta}\end{aligned}$$

so that the descendant invariant at each depth $k$ is separated as the coefficient of $z^{-k-1}$ and captured all at once. Primarily, this packages the infinite sum on the right-hand side, but once we introduce the $J$-function in the next section, we can confirm that even the $z$ on the right-hand side comes to carry a specific meaning.

## Introduction of the $J$-Function

Now we introduce the $J$-function using the gravitational invariants examined above. Consider a smooth projective variety $X$, a homogeneous basis $\{ T_a \}_{a=0,\ldots,s}$ of $H^\ast(X, \mathbb{C})$ ($T_0 = 1$), and the Poincaré dual basis $\{ T^a \}$ given by them. Taking the portion occupying the $H^2$ component as $\{ T_a \}_{a=1,\ldots,r}$ (to simplify notation), the flat coordinates $t^a$ and Novikov variables $q_a := e^{t^a}$ ($a = 1, \ldots, r$) introduced in [§Dubrovin Connection, §§D-module](/en/math/mirror_symmetry/dubrovin_connection#d-module){: data-lid="bn8vu" } are defined. For convenience, setting

$$t_{(2)} := \sum_{b=1}^r t^b T_b$$

we have $q^\beta = e^{t_{(2)} \cdot \beta}$. Meanwhile, the Dubrovin connection was defined by the formula

$$\nabla^z = \partial + z^{-1}\mathcal{C}$$

but in this post, to match signs with the oscillating integral side, we consider its *dual Dubrovin connection*

$$\nabla^{z, \vee} := \nabla^{-z} = \partial - z^{-1}\mathcal{C}$$

and the horizontal section equation of this connection

$$z q_a\partial_{q_a} s = T_a \qtimes s \qquad (a = 1, \ldots, r)\tag{$\ast$}$$

To find the solution to this equation, first consider the situation where $z\rightarrow \infty$. Then as $z\rightarrow\infty$, the $z^{-1}\mathcal{C}$ term vanishes and the connection degenerates to the standard differential $\partial$, so the leading-order horizontal section of ($\ast$) becomes a horizontal section of $\partial$, that is, a constant section independent of $q$. More generally, a solution whose correction terms vanish in the limit $z\rightarrow \infty$ will be of the form

$$s=s_0+\frac{s_1}{z}+\frac{s_2}{z^2}+\cdots$$

and since we have seen from the above computation that the $0$-th order term $s_0$ can be taken as a constant section, substituting the form

$$s=1+\frac{s_1}{z}+\frac{s_2}{z^2}+\cdots$$

directly into ($\ast$) allows us to find the $s_i$ recursively. Specifically, organizing both sides of ($\ast$) by powers of $z$, since $s_0$ is constant the left-hand side is

$$z \cdot \sum_k z^{-k} q_a\partial_{q_a} s_k = \sum_k z^{-k} q_a\partial_{q_a} s_{k+1}$$

and the right-hand side is $\sum_k z^{-k} T_a\qtimes s_k$, so comparing coefficients of each $z^{-k}$ yields the general recursion

$$q_a\partial_{q_a} s_{k+1} = T_a \qtimes s_k \qquad (a = 1, \ldots, r, k \geq 0)$$

At $k = 0$, corresponding to the first step of the recursion, we have $T_a \qtimes 1 = T_a$, so without any quantum correction, $q_a\partial_{q_a} s_1 = T_a$ holds. Integrating both sides with respect to $q_a$ gives

$$s_1=t_{(2)} + C_1,\qquad C_1\in H^\ast(X)$$

The interesting part is $k=1$, where quantum corrections first appear; considering the recursion formula

$$q_a\partial_{q_a} s_2 = T_a \qtimes t_{(2)}=T_a\qtimes \left(\sum_{b=1}^r t^b T_b\right)$$

the right-hand side now has, in addition to the classical cup product $T_a\smile t_{(2)}$, the quantum correction

$$\sum_{\beta \neq 0} q^\beta \sum_c \left(\sum_{b=1}^r t^b \langle T_a, T_b, T^c\rangle_{0, 3, \beta}\right) T_c$$

part. Meanwhile, since $T_b \in H^2$, applying the result of [\[Symplectic Geometry\] §Gromov-Witten Invariants, ⁋Proposition 4](/en/math/symplectic_geometry/gromov_witten#prop4){: data-lid="oad7k" }

$$\langle T_a, T_b, T^c\rangle_{0, 3, \beta} = (T_b \cdot \beta)\langle T_a, T^c\rangle_{0, 2, \beta}$$

we obtain the formula

$$T_a \qtimes t_{(2)} = T_a \smile t_{(2)} + \sum_{\beta \neq 0} q^\beta (t_{(2)} \cdot \beta) \sum_c \langle T_a, T^c\rangle_{0, 2, \beta} T_c$$

Now let us integrate this with respect to $q_a$. The antiderivative of the classical part $T_a \smile t_{(2)}$ is $(t_{(2)})^2/2$, which can be directly verified using $q_a\partial_{q_a} = \partial_{t^a}$:

$$\partial_{t^a}\bigl((t_{(2)})^2/2\bigr) = \partial_{t^a}\left(\frac{1}{2}\sum_{b, c} t^b t^c T_b \smile T_c\right) = \sum_c t^c T_a \smile T_c = T_a \smile t_{(2)}$$

The antiderivative of the quantum part is solved $\beta$-by-$\beta$ using the relation $q_a\partial_{q_a} q^\beta = (T_a \cdot \beta) q^\beta$ coming from $q^\beta = e^{t_{(2)}\cdot \beta}$, and for each $\beta$ it is organized as an $H^\ast(X)$-valued correction determined by the $q^\beta$ factor and the *primary* GW invariant (descendant invariant without $\psi$-class insertion) $\langle T_a, T^c\rangle_{0, 2, \beta}$. Thus $s_2$ becomes the sum of the classical $(t_{(2)})^2/2$ and this quantum correction. At higher $z^{-k}$ ($k \geq 2$) degrees, *gravitational descendants* of the form $\tau_{k-1}(T_a)$ accumulate successively along the same recursion, and the $J$-function is ultimately the explicit one-line expression for the fundamental solution forced in this manner.

::: Definition 3
The (small) *Givental $J$-function* $J_X: (\mathbb{C}^\ast)^r \times \mathbb{C}^\ast \rightarrow H^\ast(X)$ of $X$ is defined by

$$J_X(q, z) := e^{t_{(2)}/z}\left( 1 + \sum_{\substack{\beta \in H_2(X, \mathbb{Z})_{\mathrm{eff}} \\ \beta \neq 0}} \sum_{a=0}^s q^\beta \left\langle \frac{T_a}{z(z - \psi)} \right\rangle_{0, 1, \beta} T^a \right)$$
:::

Here $H_2(X, \mathbb{Z})_{\mathrm{eff}}$ is the set of effective curve classes (defined in [\[Symplectic Geometry\] §Quantum Cohomology, §§Novikov Ring](/en/math/symplectic_geometry/quantum_cohomology#novikov-ring){: data-lid="dzj23" }), over which $\beta$ ranges, and each $\beta \neq 0$ contributes to the instanton correction of degree $q^\beta$.

Since we have already verified the formula

$$\left\langle \gamma_1, \ldots, \gamma_n, \frac{\gamma_{n+1}}{z - \psi}\right\rangle_{0, n+1, \beta}=\sum_{k \geq 0} z^{-k-1} \left\langle \gamma_1, \ldots, \gamma_n, \tau_k(\gamma_{n+1})\right\rangle_{0, n+1, \beta}$$

the above $J$-function can be expanded in the form

$$J_X(q, z) = e^{t_{(2)}/z}\left(\mathbf{1} + \sum_{\substack{\beta \in H_2(X, \mathbb{Z})_{\mathrm{eff}} \\ \beta \neq 0}}\sum_{a = 0}^s \sum_{k \geq 0} q^\beta z^{-k-2} \langle\tau_k(T_a)\rangle_{0, 1, \beta} T^a\right)$$

Thus, this function can essentially be thought of as a generating function obtained by attaching the single marked point descendant invariants

$$\bigl\{\langle\tau_k(T_a)\rangle_{0, 1, \beta}\bigr\}_{\beta \in H_2(X, \mathbb{Z})_{\mathrm{eff}} \setminus \{0\}, a = 0, \ldots, s, k \geq 0}$$

to the Novikov parameter $q^\beta$, the spectral parameter $z^{-k-2}$, and the cohomology basis elements $T^a$.

Note that while the descendant invariants we defined above are generally of the multi-marked point form

$$\left\langle \tau_{k_1}(\gamma_1), \ldots, \tau_{k_{n+1}}(\gamma_{n+1})\right\rangle_{0, n+1, \beta}$$

above we have only included single marked points in the formula. This is possible because $\beta\neq 0$, so stability is guaranteed regardless of the stability of the source because the target is sufficiently large, and the reason it suffices to consider only these is essentially that we are primarily considering deformations in the $H^2$ direction, that is, small quantum cohomology.

More concretely, we already saw from [\[Symplectic Geometry\] §Gromov-Witten Invariants, ⁋Proposition 4](/en/math/symplectic_geometry/gromov_witten#prop4){: data-lid="0c0wa" } that inserting a divisor $D\in H^2(X)$ into a Gromov-Witten invariant has the effect of multiplying by $D\cdot \beta$, and we have seen that expanding this as a power series, looking at the $H^2$ direction is after all nothing more than multiplying by $e^{t_{(2)}\cdot \beta}$ in front, that is, reparametrizing the Novikov variable as $q^\beta \mapsto e^{t_{(2)}\cdot \beta}q^\beta$. In [Definition 3](#def3){: data-lid="j60mv" }, we additionally multiplied the $T_a/(z-\psi)$ term by $z^{-1}$ once more,[^1] so reflecting this $z$-shift as well, the overall factor attached in front of the $J$-function becomes $e^{t_{(2)}/z}$. Once all the dependence on the $H^2$ direction is put into $e^{t_{(2)}/z}$ and the Novikov variable, the Gromov-Witten information is condensed into the remaining single marked point, so it suffices to look at only single marked point invariants.

Meanwhile, let us recall that our motivation for introducing the $J$-function was to find the fundamental solution of the QDE ($\ast$). In [§Dubrovin Connection, §§D-module](/en/math/mirror_symmetry/dubrovin_connection#d-module){: data-lid="0sgqy" }, we saw that the A-model $D$-module is a bundle with fiber $H^\ast(X)$ at each point $(q, z)$ of the base $M_A = (\mathbb{C}^\ast)^r \times \mathbb{C}^\ast_z$, and the connection 1-form $\mathcal{C}_a = T_a \qtimes -$ on it was also an endomorphism of this fiber, whose solutions were precisely the horizontal sections of ($\ast$). These solutions are $\dim_\mathbb{C}H^\ast(X)$-dimensional, and if we solve this equation with the $T_a$ as initial values, we obtain precisely all of the solutions. Through this process, we obtain the following fundamental solution matrix.

::: Proposition 4 (A-side fundamental solution matrix)
Define the endomorphism $S(q, z) \in \End(H^\ast(X))$ by the matrix element

$$\eta\bigl(S(q,z)T_a, T_b\bigr) := \eta(T_a, T_b) + \sum_{\beta \neq 0} q^\beta \left\langle \frac{T_a}{z - \psi}, T_b \right\rangle_{0, 2, \beta}$$

where $\eta$ is the Poincaré pairing. Then $S$ satisfies the following. 

1. *(Flat section property)* Each column $S(q, z) T_b$ of $S(q, z)$ is a horizontal section of the dual small Dubrovin connection $\nabla^{z, \vee}$. That is,
   
   $$z q_a\partial_{q_a} \bigl(S(q,z)T_b\bigr) = T_a \qtimes \bigl(S(q,z)T_b\bigr)\qquad (a = 1, \ldots, r)$$

2. *($J$ = $T_0$ column)* $J_X(q, z) = e^{t_{(2)}/z} S(q, z) T_0$ holds. In particular, $J$ itself is also a horizontal section of ($\ast$), and
   
   $$z q_a\partial_{q_a} J_X = T_a \qtimes J_X \qquad (a = 1, \ldots, r)$$

:::

::: Proof
First, let us show that substituting $T_b = T_0 = 1$ into the second argument in the defining equation of $S$ yields the $J = T_0$ column. In this post, we consistently follow the convention $1/(z - \psi) = \sum_{k \geq 0} z^{-k-1}\psi^k$, and accordingly we also take the correction term in the divisor equation with a $+$ sign (in some literature $1/(z + \psi)$ is used with the opposite sign). Now, the 2-point descendant appearing in the definition is of the form with $T_0 = 1$ inserted, and expanding this as a geometric series,

$$\left\langle \frac{T_a}{z - \psi}, 1\right\rangle_{0, 2, \beta} = \sum_{k \geq 0} z^{-k-1}\langle \tau_k(T_a), 1\rangle_{0, 2, \beta}$$

Applying [\[Symplectic Geometry\] §Gromov-Witten Invariants, ⁋Proposition 3](/en/math/symplectic_geometry/gromov_witten#prop3) to each term,

$$\langle \tau_k(T_a), 1\rangle_{0, 2, \beta} = \langle \tau_{k-1}(T_a)\rangle_{0, 1, \beta}$$

holds for all $k\geq 1$. For the $k = 0$ term, since there is no $\psi$ to lower on the right-hand side of the string equation, it becomes an empty sum, and thus vanishes as $\langle T_a, 1\rangle_{0, 2, \beta} = 0$ ($\beta \neq 0$) (this is none other than the fact that a marked point evaluating the fundamental class does not contribute when $\beta \neq 0$). Thus the degree of the power series shifts down by one, giving the following expression:

$$\sum_{k \geq 1} z^{-k-1}\langle \tau_{k-1}(T_a)\rangle_{0, 1, \beta} = \sum_{m \geq 0} z^{-m-2}\langle \tau_m(T_a)\rangle_{0, 1, \beta} = \left\langle \frac{T_a}{z(z - \psi)}\right\rangle_{0, 1, \beta}$$

This is precisely the term appearing in the small $J$ formula of [Definition 3](#def3){: data-lid="rydx7" }, and multiplying this by the prefactor $e^{t_{(2)}/z}$ gives $J_X = e^{t_{(2)}/z} S(q, z) T_0$. This is the origin of the additional $z^{-1}$ that may have appeared somewhat awkward in [Definition 3](#def3){: data-lid="xcnad" }.

Now let us show that each column $S(q,z)T_b$ of $S$ is a horizontal section. For this, we directly apply $z q_a\partial_{q_a}$ to $S(q, z) T_b$. First, $S(q, z) T_b$ is expressed as a sum of terms with $q^\beta$ as a factor for each $\beta$; using the recursion relation examined before introducing the $J$-function and [\[Symplectic Geometry\] §Gromov-Witten Invariants, ⁋Proposition 4](/en/math/symplectic_geometry/gromov_witten#prop4), $z q_a\partial_{q_a}$ ultimately inserts $T_a$ at a point while, through the multiplied $z$, lowering the degree of $\psi$ in $1/(z - \psi)$ at the distinguished marked point by one.

Now this lowered $\psi$ can be decomposed into the sum of boundary divisors $\sum_S D_S$ using [Proposition 2](#prop2){: data-lid="86lym" } (more precisely, the version of [Proposition 2](#prop2){: data-lid="7czpj" } with the target retained). On each $D_S$, the source curve splits into two components whose effective class is divided as $\beta = \beta_1 + \beta_2$, and at the node between them the diagonal class $\sum_c T_c \otimes T^c$ is inserted. The component where the newly inserted $T_a$ lands gives the 3-point invariant $\langle T_a, T_c, T^d\rangle_{0, 3, \beta_1}$, namely the structure constant expressing the quantum product $T_a \qtimes$ in the basis, while the other component reconstructs the (lower-degree) $\beta_2$ part of $S(q, z) T_b$ having $T^c$ at the node. Thus, summing over all $c$ and splittings $\beta = \beta_1 + \beta_2$ reproduces exactly $T_a \qtimes$ applied to the vector $S(q, z) T_b$, that is, the right-hand side $T_a \qtimes \bigl(S(q, z) T_b\bigr)$ is precisely recovered.
:::

Therefore, since all $q^\beta$ terms vanish as $q\rightarrow 0$, the classical limit of $S$ is $\id$. On the A-side, this can be thought of as a consequence of the fact that the classical limit of the quantum cup product is the ordinary cup product.

[Proposition 4](#prop4){: data-lid="z6qjz" } shows that the $J$-function is more than a mere bundle of enumerative data: it forms a column of the fundamental solution matrix $S$ on the A-model side (specifically, the column corresponding to the normalization element $T_0 = 1$). This corresponds precisely to the period matrix $\mathcal{I}$ in [§Gauss-Manin Connection, ⁋Proposition 7](/en/math/mirror_symmetry/gauss-manin_connection#prop7){: data-lid="j6twp" } forming the fundamental solution matrix of $\nabla^z_B$ trivialized by the frame $\{e_a\}$.

In particular, when $H^\ast(X)$ is generated by $H^2(X)$, such as when $X = \mathbb{P}^n$ or for most toric Fano varieties, this single column $J$ in fact determines all of $S$. Indeed, repeatedly applying the flat section equation $z q_a\partial_{q_a} J = T_a \qtimes J$ from [Proposition 4](#prop4){: data-lid="tbw2f" } generates the quantum products $T_{a_1} \qtimes \cdots \qtimes T_{a_k} \qtimes J$ of $H^2$ classes in sequence; when $H^\ast(X)$ is generated by $H^2$, these quantum products sweep through all $T_b$ as a basis of cohomology, so the remaining columns $S(q, z) T_b$ are all reconstructed from derivatives of $J$ as well. This justifies why our "Mirror theorem" in [Claim 5](#conj5){: data-lid="bm9fg" } makes an assertion only about the first column.

Meanwhile, this calculation is also related to the handling of the integration constants obtained by repeatedly integrating from ($\ast$) earlier: namely, $S$ in [Proposition 4](#prop4){: data-lid="tp9qj" } is the solution where these integration constants are discarded as $0$ at all degrees. That is, it is the fundamental solution chosen so that, once the components coming from $t_{(2)}$ are separated off as the prefactor $e^{t_{(2)}/z}$, all remaining corrections have only instanton degrees $q^\beta$ with $\beta \neq 0$, and thus the classical limit emerges as above when $q \rightarrow 0$.

## Mirror theorem

We have previously constructed, independently, the A-side fundamental solution matrix $S$ ([Proposition 4](#prop4){: data-lid="91det" }) and the B-side period matrix $\mathcal{I}$ ([§Gauss-Manin Connection, ⁋Proposition 7](/en/math/mirror_symmetry/gauss-manin_connection#prop7){: data-lid="pmkrs" }). That the two matrices actually coincide is precisely one of the insights of the mirror theorem.

::: misc Conjecture 5 (Mirror theorem, $J$-function form) {#conj5}
For a mirror pair $(X, \check{X})$, the $J$-function of $X$ is written in terms of the cohomology basis $\{T^a\}$ components of the oscillating integral over a specific Lefschetz thimble $\Gamma_0$ corresponding to the $T_0 = 1$ normalization (the *distinguished* thimble determined in the neighborhood of the large radius limit). That is,

$$J_X(q, z) = \sum_a J^a(q, z) T^a,\qquad J^a(q, z) \propto \mathcal{I}^a_{\Gamma_0}(q, z) = \int_{\Gamma_0} T_a e^{W_q/z}\omega$$

holds up to normalization. Here the right-hand side is the $p = \Gamma_0$ column of the period matrix $\mathcal{I}^a_p$ introduced in [§Gauss-Manin Connection, ⁋Proposition 7](/en/math/mirror_symmetry/gauss-manin_connection#prop7){: data-lid="bsfx2" }.
:::

The above [Conjecture 5](#conj5){: data-lid="o1kl2" } is one of the strongest expressions of mirror symmetry: all A-side descendant Gromov-Witten invariants are reconstructed from B-side period integrals. Then, in particular, the classical version of ring-level mirror symmetry $QH^\ast(X) \cong \Jac(W_q)$ is recovered at leading order as $z\rightarrow 0$. Specifically, the $z \rightarrow 0$ stationary phase asymptotic ([§Gauss-Manin Connection, ⁋Proposition 3](/en/math/mirror_symmetry/gauss-manin_connection#prop3){: data-lid="57wes" }) expands into a sum over the critical points of $W_q$, and the leading-order critical values $\{W_q(p)\}$ recover the canonical coordinates of quantum cohomology.

This claim is not merely a repetition of [§Dubrovin Connection, ⁋Conjecture 4](/en/math/mirror_symmetry/dubrovin_connection#conj4){: data-lid="elv3y" }. To show this, we must first demonstrate that the QDE satisfied by the $J$-function ([Proposition 4](#prop4){: data-lid="nka6z" }) and the Gauss-Manin system satisfied by the period matrix ([§Gauss-Manin Connection, ⁋Proposition 7](/en/math/mirror_symmetry/gauss-manin_connection#prop7){: data-lid="bz0fa" }) define the same $D$-module; this is the content of [§Dubrovin Connection, ⁋Conjecture 4](/en/math/mirror_symmetry/dubrovin_connection#conj4){: data-lid="l6n5r" }. After that, we must verify that the $J$-function, i.e., the first column of the matrix $S$, is mapped under the isomorphism of [§Dubrovin Connection, ⁋Conjecture 4](/en/math/mirror_symmetry/dubrovin_connection#conj4){: data-lid="3rjq3" } not to an arbitrary linear combination of thimble periods, but specifically to the single oscillating integral over the distinguished thimble $\Gamma_0$. For this, an additional claim that the *integral structures* on both sides match is needed; on the A-side, the lattice defined by $K$-theory and the $\hat{\Gamma}$-class plays this role, and on the B-side, the lattice generated by Lefschetz thimbles does.

In the case of Calabi-Yau hypersurfaces in toric varieties, this was proven by Givental and Lian-Liu-Yau, and for our main object of interest, toric Fano varieties, the *$I = J$* theorem in the next section provides an explicit and computable form of this claim.

## Givental's Mirror Theorem

In the case of toric Fano varieties, the B-side oscillating integral is computed in an explicit *hypergeometric* form. The object defined through this is the *$I$-function*, which serves as the toric mirror counterpart of the $J$-function.

::: Definition 6 (Givental's $I$-function)
Let $X$ be a smooth projective toric Fano variety, $D_1, \ldots, D_m$ the toric divisors, and $\beta \in H_2(X, \mathbb{Z})$ an effective curve class. The *$I$-function* of $X$ is defined by

$$I_X(q, z) := e^{t_{(2)}/z} \sum_{\beta \in H_2(X, \mathbb{Z})_{\mathrm{eff}}} q^\beta \prod_{i=1}^m \frac{\prod_{k=-\infty}^{0} (D_i + kz)}{\prod_{k=-\infty}^{D_i \cdot \beta}(D_i + kz)}$$
:::

Here, the formally appearing infinite product to $-\infty$ precisely cancels between the numerator and denominator, so it is actually a well-defined expression that reduces to a finite product (or its inverse) depending on the sign of $D_i \cdot \beta$. The data determining this product is only the toric divisor $D_i$ and its intersection number $D_i \cdot \beta$, and the information contained in these two is the same as the information contained in the *charge matrix* of $X$, $Q = (Q_{ji}) \in \Mat_{r \times m}(\mathbb{Z})$, introduced in [§Mirror Symmetry: An Overview, ⁋Definition 1](/en/math/mirror_symmetry/overview#def1){: data-lid="e3y4h" }.

Let $X$ be a smooth projective toric variety. Then we can consider the following short exact sequence

$$0 \rightarrow H_2(X, \mathbb{Z}) \xrightarrow{\ \iota\ } \mathbb{Z}^m \xrightarrow{\ e_i \mapsto v_i\ } \mathbb{Z}^n \rightarrow 0$$

Here $m$ is the number of rays, and $\mathbb{Z}^n$ is the cocharacter lattice. That is, $H_2$ is identical to the set of relations among rays

$$\{(a_i)_i \in \mathbb{Z}^m \mid \sum_i a_i v_i = 0\}$$

Here, the charge matrix is by definition obtained by collecting these $r$ relations as rows, and thus it precisely contains the information about a basis of $H_2(X, \mathbb{Z})$. That is, for each row of $\mathbb{Z}^m$, $(Q_{j\bullet})$, the preimages $\beta_j=\iota^{-1}(Q_{j\bullet})$ form a basis of $H_2(X, \mathbb{Z})$, and in this setting the intersection with the toric divisor $D_i$ is merely reading from $\beta=(a_i)_i$ the $i$-th coordinate, so $D_i\cdot\beta_j=Q_{ji}$.

The origin of this formula is the oscillating integral on the Hori-Vafa mirror of $X$, $\check{X}$, or more precisely, expanding that integral over the distinguished thimble $\Gamma_0$ of [Claim 5](#conj5){: data-lid="la0me" } in terms of charge data gives exactly $I_X$. That is, $I_X$ is nothing more than explicitly writing the distinguished column of the period matrix $\mathcal{I}$ of [§Gauss-Manin Connection, ⁋Proposition 7](/en/math/mirror_symmetry/gauss-manin_connection#prop7){: data-lid="q9q6n" }. We defer the detailed expansion to [Example 8](#ex8){: data-lid="1uav0" }, and first translate this into a claim about the $J$-function.

::: Proposition 7 (Givental's mirror theorem)
When $X$ is a smooth projective toric Fano variety, $X$'s $I$-function and $J$-function satisfy the relation

$$J_X(\tau(q), z) = I_X(q, z)$$

Here, $\tau(q)$ is the mirror map defined from the asymptotic expansion of the $I$-function:

$$I_X(q, z) = 1 + \tau(q)/z + O(z^{-2})$$
:::

Looking at both sides for the proof, $J_X$ is, as seen in [Proposition 4](#prop4){: data-lid="hrtk6" }, the fundamental solution of the small QDE ($\ast$), and $I_X$ is the hypergeometric function explicitly given by the charge data in [Definition 6](#def6){: data-lid="gr46f" }. The key to the proof lies in directly verifying that this explicit $I_X$, like $J_X$, is also a solution of the same $D$-module, that is, a solution of the same QDE ($\ast$). If $X$ is toric Fano, then $H^\ast(X)$ is generated by $H^2(X)$, so ($\ast$) reduces to a differential equation for a single component of $I_X$, and at this point, directly applying to the hypergeometric product of $I_X$ the operator $z q_a\partial_{q_a}$ confirms that each factor of the product satisfies this equation term by term. Meanwhile, both $I_X$ and $J_X$, as $z \rightarrow \infty$, have the normalization $1 + O(z^{-1})$, and since for solutions of the QDE, once $s_0$ is determined, the remainder is uniquely determined in recurrence form from this leading asymptotic, we obtain $J_X(\tau(q), z) = I_X(q, z)$. We will see the concrete calculation for this in $X = \mathbb{P}^n$. ([Example 8](#ex8){: data-lid="0i1tk" })

Note that it is thanks to the Fano property of $X$ that the mirror map is well-defined. If $X$ is Fano, then for every non-zero effective curve class $\beta$ we have $-K_X \cdot \beta > 0$, so all $q^\beta$ corrections appear only in degrees $z^{-1}$ and below; thus the $z^0$ term of $I_X$ is exactly $1$ ($I_X = 1 + O(z^{-1})$), so from the $z^{-1}$ coefficient one can read off $\tau(q)$. More generally, in the *semi-positive* case where $-K_X$ is merely nef, directions with $-K_X \cdot \beta = 0$ produce in degree $z^0$ a correction $I_0(q) \neq 1$, so the relation is modified to $J_X(\tau(q), z) = I_X(q, z)/I_0(q)$.

In a similar vein, consider the case where the Fano index of $X$ is at least $2$. Here, the *Fano index* $r_X$ is the largest positive integer such that $-K_X = r_X H$ holds for some $H \in \Pic(X)$. Then in this case, $H = -K_X / r_X$ is also ample, so for any non-zero effective curve class $\beta$ we have $H \cdot \beta \geq 1$, and thus

$$-K_X \cdot \beta = r_X (H \cdot \beta) \geq 2$$

so that all $q$-dependent corrections are pushed to degrees $z^{-2}$ and below. As a result, in the mirror map $\tau(q)$ no $q$-correction remains, and in this case $J_X(q, z) = I_X(q, z)$ holds directly without coordinate change. The space $\mathbb{P}^n$ ($-K = (n+1)H$, Fano index $n+1 \geq 2$) in the following [Example 8](#ex8){: data-lid="n85pz" } is such a case.

::: Example 8 ($X = \mathbb{P}^n$)
The fan of $\mathbb{P}^n$ is the normal fan of the standard simplex, having $n+1$ rays

$$v_0 = -e_1 - \cdots - e_n,\qquad v_i = e_i\quad (i = 1, \ldots, n)$$

([\[Toric Geometry\] §Definition of Toric Varieties, ⁋Example 10](/en/math/toric_geometry/toric_varieties#ex10){: data-lid="lln8e" }). Here, the toric divisors are $D_0, \ldots, D_n$, corresponding to the respective coordinate hyperplanes; since they are all linearly equivalent, they defined a single hyperplane class $H\in H^2(\mathbb{P}^n)$. Furthermore, the cohomology computation of $\mathbb{P}^n$ showed that this hyperplane class generates the entire cohomology of $\mathbb{P}^n$.

Now let us unpack the data entering the $I$-function formula of [Definition 6](#def6){: data-lid="z1y4k" } for $\mathbb{P}^n$. First, since $H^2(\mathbb{P}^n)$ is generated by $H$ alone, we have $t_{(2)} = tH$, and the Novikov variable is given by $q = e^t$. That is, since $t = \ln q$, we can write $e^{t_{(2)}/z} = e^{H \ln q / z}$.

Next, an effective curve class is parameterized by a non-negative multiple $\beta = d H^\vee$ ($d \geq 0$) of the line class $H^\vee$, so $q^\beta = q^d$; furthermore, on $\mathbb{P}^n$, all $n+1$ toric divisors $D_0, \ldots, D_n$ ([\[Toric Geometry\] §Torus-Invariant Divisors and Line Bundles, ⁋Example 11](/en/math/toric_geometry/toric_divisors#ex11){: data-lid="wg0d3" }) satisfy $D_i \cdot \beta = H \cdot d H^\vee = d$, so upon substituting this, the infinite products toward $-\infty$ cancel in each factor, reducing to

$$\frac{\prod_{k=-\infty}^{0}(D_i + kz)}{\prod_{k=-\infty}^{D_i \cdot \beta}(D_i + kz)} = \frac{\prod_{k=-\infty}^{0}(H + kz)}{\prod_{k=-\infty}^{d}(H + kz)} = \frac{1}{\prod_{j=1}^{d}(H + jz)}$$

and since there are $n+1$ such factors, one for each toric divisor, raising this to the $n+1$-th power yields the $I$-function

$$I_{\mathbb{P}^n}(q, z) = e^{H \ln q /z} \sum_{d \geq 0} \frac{q^d}{\prod_{j=1}^d (H + jz)^{n+1}}$$

Since $H^{n+1} = 0$, expanding $(H + jz)^{-(n+1)}$ in the denominator as a power series in $z^{-1}$, Taylor-expanding $e^{H\ln q/z}$, and grouping by degree, we obtain the following expansion:

$$I_{\mathbb{P}^n}(q, z) = 1 + \frac{H \ln q}{z} + \frac{(H \ln q)^2}{2 z^2} + \cdots + q \frac{1}{(H+z)^{n+1}} + \cdots$$

Now, the Fano index of $\mathbb{P}^n$, from $-K_{\mathbb{P}^n} = (n+1) H$, is $n+1 \geq 2$. In the expansion above, the $q$-dependent corrections (for $d \geq 1$, the $q^d$ terms) appear only in degrees $z^{-(n+1)}$ and below, so in $I_{\mathbb{P}^n}$ the $z^{-1}$ coefficient is only $H \ln q$ (namely $t_{(2)}$) coming from the prefactor. Therefore, as discussed immediately after [Proposition 7](#prop7){: data-lid="1122m" }, the mirror map must be the identity, and

$$J_{\mathbb{P}^n}(q, z) = I_{\mathbb{P}^n}(q, z)$$

must hold. Let us verify this directly.

The B-side calculation is largely finished in [§Gauss-Manin Connection, ⁋Example 8](/en/math/mirror_symmetry/gauss-manin_connection#ex8){: data-lid="9ozqh" }. According to it, for $\mathbb{P}^n$, with respect to the fundamental solution matrix $\mathcal{I}_p^a(q,z)$, the vector corresponding to the Lefschetz thimble basis $\Gamma_p$ has its first component $\mathcal{I}_p^0(q,z)$ satisfy the following equation:

$$(z\partial_q)(qz\partial_q)^n\mathcal{I}_p^0=\mathcal{I}_p^0 \tag{$\ast\ast$}$$

Now we show that the above $I$-function with $H=0$ satisfies this equation. According to ($\ast$), taking $qz\partial_q$ is equivalent to taking the quantum product with $H$, and on the B-side this is exactly the same as starting from $\mathcal{I}_p^0$ and inductively computing the $\mathcal{I}_p^a$; thus, showing that these are solutions to the same ODE when $H=0$ completes the verification of [Proposition 7](#prop7){: data-lid="kughb" }.

Then, in the product formula of [Definition 6](#def6){: data-lid="8ebju" }, the prefactor becomes $e^0 = 1$ and each factor becomes $(H + jz) \mapsto jz$, so we obtain the expression

$$\Phi_0(q, z) := I_{\mathbb{P}^n}(q, z)\big\vert_{H=0} = \sum_{d \geq 0} \frac{q^d}{(d!)^{n+1}z^{(n+1)d}}$$

Let us verify directly that this $\Phi_0$ satisfies ($\ast\ast$). By direct computation, the action of $qz\partial_q$ pulls down $d$ term by term and attaches a $z^{-1}$ factor, so

$$(qz\partial_q)^n\Phi_0 = \sum_{d\geq 0}\frac{d^n q^d}{(d!)^{n+1}z^{(n+1)d - n}},$$

and applying $z\partial_q$ again pulls down $d$ once more and shifts $d$ to $d - 1$, giving

$$(z\partial_q)(qz\partial_q)^n\Phi_0 = \sum_{d \geq 1}\frac{d^{n+1}q^{d-1}}{(d!)^{n+1}z^{(n+1)d - n - 1}} = \sum_{d' \geq 0}\frac{(d'+1)^{n+1}q^{d'}}{((d'+1)!)^{n+1}z^{(n+1)d'}} = \Phi_0$$

which is seen to hold exactly.

The stationary phase aspect of [Claim 5](#conj5){: data-lid="f93ro" } was also already computed in [§Gauss-Manin Connection, ⁋Example 8](/en/math/mirror_symmetry/gauss-manin_connection#ex8){: data-lid="ahx9a" }, but since this is slightly outside our primary focus in this post, we omit it.
:::

This example shows that mirror symmetry is realized not as an abstract isomorphism, but as the concrete coincidence of two hypergeometric series. For a general toric Fano variety, a similar explicit calculation proceeds from the charge matrix, and in all such cases the $I = J$ theorem of [Proposition 7](#prop7){: data-lid="ou3u9" } provides a practical verification of mirror symmetry.

## Extension to Big Quantum Cohomology

The small $J$-function treated so far, over the base of deformations only in the $H^2$ directions from [§Dubrovin Connection, §§D-module](/en/math/mirror_symmetry/dubrovin_connection#d-module){: data-lid="vmh1u" }, was the fundamental solution for the small quantum $D$-module. As seen in the earlier part of the same post, the Dubrovin connection itself was actually defined on big quantum cohomology based on deformations of the entire $H^\ast(X)$, and the small version looking only at the $H^2$ direction was a specialization of this. The same upgrade is possible for the $J$-function as well, and this is the *big $J$-function*.

To move to the setup of the big version, we must introduce for $H^\ast(X)$ the general deformation parameter $t = \sum_{a=0}^s t^a T_a$. For an arbitrary $t \in H^\ast(X)$, the big quantum product $\star_t$, as seen in [§Dubrovin Connection, §§D-module](/en/math/mirror_symmetry/dubrovin_connection#d-module){: data-lid="i1yoq" }, determines via $\mathcal{C}_\alpha = T_\alpha \star_t -$ the connection $1$-form of the Dubrovin connection. Its dual horizontal section equation is

$$z\partial_{t^a} s = T_a \star_t s\qquad (a = 0, 1, \ldots, \dim_\mathbb{C} H^\ast(X) - 1)$$

and this is the *big QDE*, extending ($\ast$) of the small case to all directions of $H^\ast$.

::: Definition 9 (Big $J$-function)
For $X$, the *big Givental $J$-function* $J_X^{\mathrm{big}}: H^\ast(X) \times \mathbb{C}^\ast \rightarrow H^\ast(X)$ is defined by

$$J_X^{\mathrm{big}}(t, z) := e^{t_{(2)}/z}\left( 1 + \sum_{\substack{\beta \in H_2(X, \mathbb{Z})_{\mathrm{eff}}, n \geq 0 \\ (\beta, n) \neq (0, 0)}} \sum_{a=0}^s \frac{q^\beta}{n!} \left\langle \frac{T_a}{z - \psi}, t, \ldots, t \right\rangle_{0, n+1, \beta} T^a \right)$$

Here, $T_a/(z-\psi)$ is inserted at the first marked point (i.e., the pullback of $T_a$ with $\psi^k$ of all degrees in generating function form), and at all the remaining $n$ marked points, $t \in H^\ast(X)$ is inserted, making a total of $n+1$ marked points.
:::

The fact that the big $J$-function forms a horizontal section of the big QDE follows from the same argument as in the small version of [Proposition 4](#prop4){: data-lid="ah3k7" }. The small $J$-function is recovered as the specialization of the big $J$-function to $t = t_{(2)} \in H^2(X)$: if one applies the divisor equation (with descendant correction term) to the $H^2$ insertions $n$ times, the $t_{(2)}$ insertions come out as the factor $(t_{(2)} \cdot \beta)^n$ and $\psi$-shift corrections, and these sum to $\sum_n (t_{(2)}\cdot \beta)^n/n! = q^\beta$ while the $\psi$-shift correction produces an additional $z^{-1}$ factor, so that, with the marked points reduced to $1$, the small $J$-function form of [Definition 3](#def3){: data-lid="fm5qj" } is recovered as is.

The additional information contained in the big $J$-function is all descendant invariants determined by arbitrary cohomology classes. Based on this, [Conjecture 5](#conj5){: data-lid="6vh4q" } is also elevated to the big version, becoming a stronger statement asserting the coincidence of the *full* $S$-matrix and the *full* period matrix, and $I = J$ ([Proposition 7](#prop7){: data-lid="7kav7" }) also has richer content in the big version where the mirror map $\tau(q)$ is generally non-trivial.

---

**References**

**[CK]** D. A. Cox, S. Katz, *Mirror Symmetry and Algebraic Geometry*, Mathematical Surveys and Monographs **68**, AMS, 1999.  
**[MS]** K. Hori, S. Katz, A. Klemm, R. Pandharipande, R. Thomas, C. Vafa, R. Vakil, E. Zaslow, *Mirror Symmetry*, Clay Mathematics Monographs **1**, AMS, 2003.

---

[^1]: Its origin is examined in the proof of [Proposition 4](#prop4){: data-lid="os9n8" }.
