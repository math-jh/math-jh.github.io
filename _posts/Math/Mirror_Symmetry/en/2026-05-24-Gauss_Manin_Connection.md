---
title: "Gauss-Manin Connection"
description: "This post examines the module isomorphism arising in the Dubrovin connection of mirror symmetry. It covers the construction of holomorphic volume forms in Landau-Ginzburg models, focusing on B-side oscillating integrals and the Gauss-Manin system."
excerpt: "B-model D-module structures, oscillating integrals, and Gauss-Manin connections on cohomology"

categories: [Math / Mirror Symmetry]
permalink: /en/math/mirror_symmetry/gauss-manin_connection
sidebar: 
    nav: "mirror_symmetry-en"

date: 2026-05-24
weight: 5
translated_at: 2026-10-03T15:15:05+00:00
translation_source: antigravity-gemini-3.8-flash-high
---
In this post, we examine in detail the $D$-module isomorphism asserted in [§Dubrovin Connection, ⁋Conjecture 4](/en/math/mirror_symmetry/dubrovin_connection#conj4){: data-lid="qcy8y" }. To this end, we must look at both the A-side and the B-side. Since the A-side was already covered to some extent in [\[Symplectic Geometry\] §Quantum Cohomology, ⁋Definition 7](/en/math/symplectic_geometry/quantum_cohomology#def7){: data-lid="9rb24" }, we first examine the B-side, namely oscillating integrals and the Gauss-Manin system. 

## Landau-Ginzburg Model and Volume Form

First, we need to set the stage for the B-model. As seen in [§Mirror Symmetry: An Overview, ⁋Definition 4](/en/math/mirror_symmetry/overview#def4){: data-lid="wafnp" }, in a Landau-Ginzburg model $(\check{X}, W_q)$, $\check{X}$ is usually an algebraic torus $(\mathbb{C}^\ast)^N$ or a subvariety inside it, and $W_q$ is a holomorphic function parametrized by the *quantum parameter* $q = (q_1, \ldots, q_r) \in (\mathbb{C}^\ast)^r$. Here, $r$ was the dimension of the *complexified Kähler moduli* of the A-side mirror $X$, which for a Fano variety was given by

$$r = \rank \operatorname{Pic}(X) = \dim_\mathbb{C} H^2(X; \mathbb{C})$$

To define oscillating integrals on this, we first define a holomorphic volume form $\omega$.

In general, on a compact (or complete, in algebraic geometry) space whose canonical bundle is not trivial, a holomorphic top form cannot be nowhere-vanishing; thus, to obtain a volume form, we must deliberately remove such points. That is, we view $\check{X}$ as an open subset $\check{X} = Y \setminus D$ of some smooth projective variety $Y$, and then choose the divisor $D$ on $Y$ so that it precisely absorbs the bad locus of a rational section of $\mathcal{K}_Y$. Specifically, if we take an effective representative $D \geq 0$ of the anti-canonical class $-K_Y$ (that is, $D \sim -K_Y$), then $\mathcal{K}_Y \otimes \mathcal{O}_Y(D) \cong \mathcal{O}_Y$ becomes trivial, so there exists a nowhere-vanishing global section

$$\Omega\in H^0(Y, \mathcal{K}_Y\otimes \mathcal{O}_Y(D))$$

and viewing $\Omega$ as a rational section of $\mathcal{K}_Y$, we have $\divisor(\Omega)=-D$, so that $\omega=\Omega\vert_{\check{X}}$ serves precisely as the volume form we want. This is a generalization of the construction[^1] where, on a smooth complete toric variety, one removes the boundary divisor $D=\sum_\rho D_\rho$ corresponding to the anti-canonical divisor and then forms the canonical volume form

$$\omega = d\log \rchi^{m_1} \wedge \cdots \wedge d\log \rchi^{m_N}$$

there. Meanwhile, abstracting the ambient data $(Y, D)$ on which this construction operates leads to the log Calabi-Yau pair of the following definition.

::: Definition 1
When a pair $(Y, D)$ of a smooth projective variety $Y$ and a reduced SNC divisor ([\[Toric Geometry\] §Logarithmic Differential Forms on Toric Varieties, ⁋Definition 5](/en/math/toric_geometry/logarithmic_differentials#def5){: data-lid="gqq7g" }) $D \subseteq Y$ satisfies $K_Y + D \sim 0$, we call it a *log Calabi-Yau pair*. In this case, the non-vanishing volume form $\omega=\Omega\vert_{\check{X}}$ obtained via the construction above is called the *canonical holomorphic volume form* of the log CY pair. 
:::

Geometrically, choosing $\omega$ via a nowhere-vanishing global section of $\mathcal{K}_Y\otimes \mathcal{O}_Y(D)\cong \mathcal{O}_Y$ in the previous construction is equivalent to choosing a trivialization $\Omega^N_Y(\log D)\cong\mathcal{O}_Y$. In particular, when $\check{X}=(\mathbb{C}^\ast)^N$, the canonical volume form with respect to the standard affine coordinates $\x_i$ is

$$\omega = \frac{\dd{\x_1} \wedge \cdots \wedge \dd{\x_N}}{\x_1 \cdots \x_N} = d\log \x_1 \wedge \cdots \wedge d\log \x_N$$

## Lefschetz thimble

An oscillating integral is a bona fide integral, obtained by integrating an actual function along an actual integration path. Specifically, for a superpotential $W_q$, the *oscillating integral* along a path $\Gamma$ called a *Lefschetz thimble* is defined by

$$\mathcal{I}_\Gamma(q,z)=\int_\Gamma e^{W_q/z}\omega$$

Here, $\omega$ is the volume form on $\check{X}$ defined above, $q$ is the quantum parameter parametrizing $W_q$, and $z$ is the spectral parameter connecting the region where $z\rightarrow 0$ and where it does not, just as in the Dubrovin connection. For now, if we consider $z$ as suitably fixed, for the integral above to be well-defined, $W_q/z$ in the exponent must tend to $-\infty$ and vanish as we follow the integration path $\Gamma$.

To this end, for each point $p\in \Crit(W_q)$, we call the cycle of the form

$$\Gamma_p := \left\{ x(0) \in \check{X} \middle\vert \lim_{t \rightarrow -\infty} x(t) = p, \lim_{t \rightarrow +\infty} \Real\left(\frac{W_q(x(t))}{z}\right) = -\infty \right\}$$

a *Lefschetz thimble*. Here, $x(t)$ is a negative gradient flow line of $\Real(W_q/z)$, and thus $\Gamma_p$ is the unstable manifold of $p$. ([\[Symplectic Geometry\] §Morse Theory and Stationary Phase Approximation, ⁋Definition 14](/en/math/symplectic_geometry/morse_stationary_phase#def14){: data-lid="mn6r9" }) It is known that if $W_q$ is of Morse type, $\Gamma_p$ forms a cycle of real dimension $N$ ([\[Symplectic Geometry\] §Morse Theory and Stationary Phase Approximation, ⁋Proposition 15](/en/math/symplectic_geometry/morse_stationary_phase#prop15){: data-lid="uty75" }). Meanwhile, from the ring isomorphism $\Jac(W_q) \cong QH^\ast(X)$ examined in [§Mirror Symmetry: An Overview](/en/math/mirror_symmetry/overview){: data-lid="cevbm" }, the number of critical points coincides precisely with $\dim_\mathbb{C} H^\ast(X, \mathbb{C})$. The Lefschetz thimbles $\{\Gamma_p\}_{p \in \Crit(W_q)}$ corresponding to these critical points form a $\mathbb{C}$-basis of the *$N$th rapid decay homology*

$$H_N(\check{X}, \{\Real(W_q/z) \ll 0\}; \mathbb{C})$$

Here, the rapid decay homology $H_\ast(\check{X}, \{\Real(W_q/z) \ll 0\}; \mathbb{C})$ is formed by collecting $n$-chains $\sigma$ whose boundary $\partial \sigma$ lies in the *rapid decay zone*

$$S_z=\{x \in \check{X} \mid \Real(W_q(x)/z) \ll 0\}$$

consisting of points with sufficiently negative $\Real(W_q/z)$, and quotienting out chains that lie entirely within $S_z$ by zero. More rigorously, we set

$$S_z^M=\{x \in \check{X} \mid \Real(W_q(x)/z) <-M\}$$

and consider the relative singular homology $H_n(\check{X}, S_z^M; \mathbb{C})$; while $S_z^M$ of course depends on the value of $M$, it is known that this relative homology itself stabilizes as $M$ becomes large. We define this stabilized value to be the rapid decay homology.

From this expression, the role of $z$ also becomes somewhat visible: when $z\rightarrow 0$, $e^{W_q/z}$ oscillates rapidly according to the phase of $W_q$, so the dominant contribution to the integral appears only near the stationary phase, that is, near $p$. Since we know that on the B-side the mirror symmetry statement is about the critical points of $W_q$, the role of $z$ is clear.

However, one must note that $z$ is actually not a real parameter, but a complex parameter. Indeed, if the argument of $z$ changes, $W_q$ must also be aligned in that direction to become the real part, so the definition of $\Gamma_p$ above will change slightly. When varying $z$ in this way, the basis defined by the Lefschetz thimbles itself changes, and this is also the case for the Dubrovin connection on the A-side (even though not explicitly mentioned in that post). That is, the values of $\nabla^z$ will also vary as $z$ changes, but we simply had not paid attention to this; viewing it on $\mathbb{C}^\ast$ reveals a richer structure. In short, looking at the stationary phase asymptote as $z \rightarrow 0^+$ is merely one section of this structure, and we will preserve the data they contain over all of $\mathbb{C}^\ast$.

Summarizing the discussion so far, we have the following.

::: Definition 2
Consider a Landau-Ginzburg model $(\check{X}, W_q)$ and a holomorphic volume form $\omega$ defined on it. For a fixed Lefschetz thimble $\Gamma_p$, we define the *oscillating integral* along it by

$$\mathcal{I}_{\Gamma_p}(q, z) := \int_{\Gamma_p} e^{W_q / z} \omega$$

where $\Gamma_p$ is chosen as a Lefschetz thimble that can be continuously isotoped as $q$ and $z$ vary.
:::

Here, choosing $\Gamma_p$ so that it can be continuously isotoped as $(q,z)$ varies ensures that, as the critical point varies with $(q,z)$ and the thimble is consequently deformed, this deformation is continuous. That is, it parallel transports the cycle as the parameters $(q,z)$ vary, and this will provide the basis for the Gauss-Manin connection to be defined shortly. 

As mentioned above, since $e^{W_q/z}$ oscillates rapidly depending on the phase of $W_q$, the dominant contribution to the integral arises only near the points where the phase is stationary, that is, near the critical points. The following proposition restates [\[Symplectic Geometry\] §Morse Theory and Stationary Phase Approximation, ⁋Proposition 16](/en/math/symplectic_geometry/morse_stationary_phase#prop16){: data-lid="jbsvn" } adapted to our setting. 

::: Proposition 3 (Stationary phase asymptotic)
For a non-degenerate critical point $p$ of $W_q$ and the Lefschetz thimble $\Gamma_p$ passing through it, as $z \rightarrow 0^+$,

$$\mathcal{I}_{\Gamma_p}(q, z) \sim (2\pi z)^{N/2} \frac{e^{W_q(p)/z}}{\sqrt{\det\Hess_p(W_q)}} \big(1 + O(z)\big)$$

holds. Here $N = \dim_\mathbb{C} \check{X}$, $\Hess_p$ is the Hessian at $p$ with respect to holomorphic coordinates $y$ near $p$ in which $\omega$ becomes the standard volume form $\dd{y_1}\wedge\cdots\wedge\dd{y_N}$, and the branch of $\sqrt{}$ is determined by the orientation of $\Gamma_p$.
:::

The core of the proof is to reduce $W_q$ to a quadratic form near $p$ using [\[Symplectic Geometry\] §Morse Theory and Stationary Phase Approximation, ⁋Theorem 6](/en/math/symplectic_geometry/morse_stationary_phase#thm6){: data-lid="ts49d" } and then apply Gaussian integration. In any case, what is important in our setting is the fact that as $z \rightarrow 0^+$, the oscillating integral is completely determined by the *local data at each critical point*, namely the critical value $W_q(p)$ and the Hessian determinant. In particular, from the viewpoint of the mirror symmetry isomorphism $\Jac(W_q) \cong QH^\ast(X_\Sigma)$, the critical values $\{ W_q(p) \}$ are interpreted on the A-side as the *canonical coordinates* of quantum cohomology.

## Gauss-Manin Connection

To track the $(q, z)$-dependence of oscillating integrals, we introduce the *Gauss-Manin connection* $\nabla^{GM}$. In order to define this, we must first set up the vector bundle that serves as its setting. Taking the parameter space of $(q,z)$, $B=(\mathbb{C}^\ast)^r\times \mathbb{C}^\ast$, as the base manifold, for each base point $(q, z) \in B$ we consider the *rapid decay relative cohomology* (the dual of the rapid decay homology defined above)

$$\mathcal{H}_{(q, z)} := H^N(\check{X}, \{ \Real(W_q/z) \ll 0 \}; \mathbb{C})$$

and consider the family

$$\{\mathcal{H}_{(q, z)}\}_{(q, z) \in B}$$

assigning this as the fiber. At each point $(q,z)$, elements of this cohomology are inherently paired with elements of rapid decay homology to yield values. Since rapid decay homology has the Lefschetz thimbles as its basis, in view of [Definition 2](#def2){: data-lid="j8afh" }, it is natural to take $[e^{W_q/z}\omega]$ as a representative for elements of this cohomology. 

It is known that if $W_q$ is of Morse type, this family defines a vector bundle $\mathcal{H}$ over $B$. In particular, the fact that these fibers patch together nicely is possible precisely because, when choosing the Lefschetz thimbles earlier, we selected those that can be continuously isotoped with respect to $(q,z)$. That is, when a cycle $\Gamma$ varies continuously with $(q, z)$, the cohomology class paired with it can also be parallel transported to "follow along", and formulating this parallel transport in the form of a connection gives the *Gauss-Manin connection*.

::: Definition 4 (Gauss-Manin connection)
The *Gauss-Manin connection* $\nabla^{GM}$ on the vector bundle $\mathcal{H} \rightarrow (\mathbb{C}^\ast)^r \times \mathbb{C}^\ast$ is the flat connection uniquely determined by the following condition:

> A section $\mathbf{s}: (q, z) \mapsto [\alpha(q, z)] \in \mathcal{H}_{(q,z)}$ is *$\nabla^{GM}$-flat* if and only if, for *any* family of cycles $\{\Gamma(q, z)\}$ continuously isotoped in the sense immediately following [Definition 2](#def2){: data-lid="ojmda" }, the *period*
> 
> $\Pi_\Gamma(q, z) := \int_{\Gamma(q, z)} \alpha(q, z)$
> 
> is a locally constant function of $(q, z)$.
:::

As mentioned above, an element of the cohomology fiber $\mathcal{H}_{(q,z)}$ is completely determined by its integral pairing with cycles in the dual rapid decay homology. Here, the canonical identification between fibers in the local system structure above was determined precisely as the dual of the parallel transport of cycles. Therefore, to check whether sections of the bundle above are locally constant via this identification, it suffices to see whether the pairing values with all parallel-transported cycles are locally constant, and these values are precisely the periods. After a brief calculation, one sees that $\nabla^{GM}$ defined this way is uniquely determined, and the flatness of $\nabla^{GM}$ can also be verified.

The computation of $\nabla^{GM}$ at the level of representative forms is as follows.

::: Proposition 5
For a class $[e^{W_q/z} \omega] \in \mathcal{H}_{(q,z)}$, the Gauss-Manin connection acts by

$$\nabla^{GM}_{\partial_{q_i}} [e^{W_q/z} \omega] = \left[\frac{\partial_{q_i} W_q}{z} e^{W_q/z} \omega\right],\qquad \nabla^{GM}_{z \partial_z}[e^{W_q/z} \omega] = \left[-\frac{W_q}{z} e^{W_q/z} \omega\right]$$
:::

::: Proof
Computing by the chain rule at the cochain level gives

$$\partial_{q_i}\left(e^{W_q/z} \omega\right) = \frac{\partial_{q_i} W_q}{z} e^{W_q/z} \omega,\qquad z\partial_z\left(e^{W_q/z} \omega\right) = -\frac{W_q}{z} e^{W_q/z} \omega$$

(where $\omega$ is independent of $q, z$). The well-definedness of $\nabla^{GM}$ follows from the fact that cocycle variations drop into coboundaries, namely that for any $(N-1)$-form $\beta$, $\dd{(e^{W_q/z}\beta)} = e^{W_q/z}(\dd{\beta} + z^{-1} \dd{W_q} \wedge \beta)$ is exact, and the flatness $[\nabla^{GM}_{\partial_{q_i}}, \nabla^{GM}_{\partial_{q_j}}] = 0$ is immediately obtained from the commutativity of partial derivatives.
:::

## B-model connection

To allow a direct comparison with the A-model Dubrovin connection $\nabla^z$ in [§Dubrovin Connection, ⁋Definition 1](/en/math/mirror_symmetry/dubrovin_connection#def1){: data-lid="9zxab" }, we define the *B-model connection* by rescaling the Gauss-Manin connection by $z$.

::: Definition 6 (B-model connection)
On $\mathcal{H}$, we define the *B-model connection* $\nabla^z_B$ by

$$\nabla^z_B := z\nabla^{GM}$$

. 
:::

Explicitly, applying the B-model connection to the frame $[e^{W_q/z}\omega]$, by [Proposition 5](#prop5){: data-lid="1w2bv" } we have

$$\nabla^z_{B, \partial_{q_i}}[e^{W_q/z}\omega] = \partial_{q_i} W_q \cdot [e^{W_q/z}\omega],\qquad \nabla^z_{B, z\partial_z}[e^{W_q/z}\omega] = -W_q \cdot [e^{W_q/z}\omega]$$

. Since this rescaling absorbs the $1/z$ factor from [Proposition 5](#prop5){: data-lid="7ptbo" }, in the limit $z \rightarrow 0$ the connection 1-form of the B-model connection becomes precisely multiplication by $\partial_{q_i} W_q$ on the cohomology class. This is in the same context as what we saw earlier in [§Dubrovin Connection, ⁋Conjecture 4](/en/math/mirror_symmetry/dubrovin_connection#conj4){: data-lid="oi5ma" }, and is identical to the situation where sending $z$ to $0$ on the Frobenius manifold $M\times \mathbb{C}^\ast$ in the setting $z\rightarrow 0$ recovers the product structure of the Frobenius algebra.

Since the above formulas are statements at the level of cohomology classes, to compute them concretely we can pair them with an arbitrary Lefschetz thimble (that is, a basis of rapid decay homology) to evaluate the actual integral. The result is the following:

$$z \partial_{q_i}\mathcal{I}_\Gamma = \int_\Gamma \partial_{q_i}W_q\cdot e^{W_q/z} \omega,\qquad z^2 \partial_z\mathcal{I}_\Gamma = -\int_\Gamma W_q\cdot e^{W_q/z} \omega \tag{$\ast$}$$

. However, the right-hand side of ($\ast$) differs from the form in [Definition 2](#def2){: data-lid="ukqwy" } that we know; to resolve this, we need to broaden the integrand to the form $f e^{W_q/z}\omega$, provided that $f$ does not violate the decaying condition of rapid decay homology. Since $\lvert e^{W_q/z}\rvert = e^{\Real(W_q/z)}$ vanishes exponentially to $0$ near the boundary of the thimble $\Gamma$, as long as $f$ has at most polynomial growth it can be controlled sufficiently, so the natural function space is the space of regular functions $\mathcal{O}(\check{X})$.

The problem is that if defined this way, the collection of regular functions is infinite-dimensional (as a vector space), making it impossible to add all of them. To resolve this, we observe that when we define the pairing using period integrals, the value depends only on the cohomology class. Indeed, if $f, g \in \mathcal{O}(\check{X})$ define the same cohomology class (that is, if for some rapid decay form $\alpha$ the identity $(f-g)\cdot e^{W_q/z}\omega = \dd{\alpha}$ holds), then from Stokes' theorem,

$$\int_\Gamma (f-g)\cdot e^{W_q/z}\omega = \int_\Gamma \dd{\alpha} = \int_{\partial\Gamma}\alpha = 0$$

, and it follows that the value of $\mathcal{I}^f_\Gamma$ depends only on the cohomology class $[f\cdot e^{W_q/z}\omega] \in \mathcal{H}_{(q,z)}$ of $f$. That is, the space of unknowns we need to deal with is not actually $\mathcal{O}(\check{X})$ but $\mathcal{H}_{(q,z)}$, and this problem is resolved as long as $\mathcal{H}_{(q,z)}$ is finite-dimensional. And this indeed holds: if $W_q$ is of Morse type, the rapid decay homology $H_N(\check{X},指示 S_z;\mathbb{C})$ has a thimble basis $\{[\Gamma_p]\}_{p\in\Crit(W_q)}$, and since this is the dual of $\mathcal{H}_{(q,z)}$, we have

$$\dim_\mathbb{C}\mathcal{H}_{(q,z)} = \lvert\Crit(W_q)\rvert$$

.

Meanwhile, $\mathcal{H}_{(q,z)}$ has another natural basis, namely the one coming from $\Jac(W_q)$. Considering the natural map

$$\Jac(W_q) \longrightarrow \mathcal{H}_{(q,z)},\qquad T \longmapsto [T\cdot e^{W_q/z}\omega]$$

, a dimension count shows that this is an isomorphism, and from this, given a basis $\{T_a\}$ of $\Jac(W_q)$, we can choose a basis

$$\bigl\{e_a := [T_a e^{W_q/z}\omega] \bigr\}_{a=0,\ldots,\mu-1}$$

of $\mathcal{H}_{(q,z)}$. That is, we currently have a basis $\{e_a\}$ on the rapid decay cohomology side and a basis $\{[\Gamma_p]\}_{p=0,\ldots,\mu-1}$ on the rapid decay homology side (indexing thimbles by critical points), and using these we can define the *period matrix*

$$\mathcal{I}^a_p(q, z) := \langle e_a, [\Gamma_p]\rangle = \int_{\Gamma_p} T_a e^{W_q/z} \omega$$

. Now, ($\ast$) above is written on this matrix as follows.

::: Proposition 7 (Fundamental solution matrix)
In the setup above, if we define the multiplication matrices in $\Jac(W_q)$ by

$$T_a\cdot \partial_{q_i}W_q = \sum_b (M_i)^a_b T_b,\qquad T_a\cdot W_q = \sum_b E^a_b T_b\quad\text{in }\Jac(W_q)$$

then the period matrix $\mathcal{I} = (\mathcal{I}^a_p)$ satisfies the closed ODE system

$$z \partial_{q_i}\mathcal{I}^a_p = \sum_b (M_i)^a_b \mathcal{I}^b_p,\qquad z^2 \partial_z\mathcal{I}^a_p = -\sum_b E^a_b \mathcal{I}^b_p$$

In particular, $\mathcal{I}$ is an invertible matrix-valued function, and forms a *fundamental solution matrix* of the B-model connection $\nabla^z_B$ trivialized by the frame $\{e_a\}_a$.
:::

Specifically, dual to $\{[\Gamma_p]\}$, the basis $\{f^p\}\subseteq\mathcal{H}_{(q,z)}$ consists of *horizontal sections* of $\nabla^z_B$ by [Definition 4](#def4){: data-lid="l69xc" }, and within $\mathcal{H}$, the change-of-basis between the non-flat frame $\{e_a\}$ and the flat frame $\{f^p\}$ is precisely

$$e_a = \sum_p \mathcal{I}^a_p f^p,\qquad f^p = \sum_a (\mathcal{I}^{-1})^p_a e_a$$

Therefore, the rows of $\mathcal{I}^{-1}$ are, in the frame $\{e_a\}$, the horizontal sections of $\nabla^z_B$, so that $\mathcal{I}$ itself encodes all data of $\nabla^z_B$. That this fundamental solution matrix $\mathcal{I}$ coincides on the A-side with the fundamental solution of the quantum cohomology $D$-module ($J$-function) is the assertion of the mirror theorem, which we treat in the next post.

## Example: Oscillating Integrals of $\mathbb{P}^n$

::: Example 8 ($X = \mathbb{P}^n$)
From [§Mirror Symmetry: An Overview, ⁋Definition 4](/en/math/mirror_symmetry/overview#def4){: data-lid="cqgb3" }, the Hori-Vafa mirror of $\mathbb{P}^n$ is given in the form

$$\check{X} = (\mathbb{C}^\ast)^n,\qquad W_q = \x_1 + \cdots + \x_n + \frac{q}{\x_1 \cdots \x_n},\qquad \omega = \frac{\dd{\x_1} \wedge \cdots \wedge \dd{\x_n}}{\x_1 \cdots \x_n}$$

Computing the derivatives to find the critical points, we have

$$\partial_{\x_i}W_q =1 - \frac{1}{\x_i}\frac{q}{\x_1\cdots \x_n} = 0$$

and since this must hold for all $i$, all $\x_i$ must take the same value; thus for an $(n+1)$th root of unity $\zeta$, the points given by $x_i = \zeta q^{1/(n+1)}$ ($i=1,\ldots,n$) are the critical points $x_\zeta$. From the viewpoint of the Jacobi ring, the equations for the critical points above yield

$$\Jac(W_q) \cong \mathbb{C}[\x, \x^{-1}] / (\x^{n+1} - q)$$

and from the calculation of $x$ above, we can choose a basis for $\Jac(W_q)$ consisting of the $\x^a$. Meanwhile, in the Jacobi ring,

$$\partial_qW_q = \x^{-n} = \x/q,\qquad W_q = n\x + q\cdot\x/q = (n+1)\x$$

so the multiplication matrices are

$$M_q = \begin{pmatrix} 0 & 1/q & & & \\ & 0 & 1/q & & \\ & & \ddots & \ddots & \\ & & & 0 & 1/q \\ 1 & & & & 0\end{pmatrix},\qquad E = (n+1)qM_q$$

Now, according to [Proposition 7](#prop7){: data-lid="lnpcd" }, the period matrix $\mathcal{I}^a_p(q,z)$ satisfies

$$z\partial_q\mathcal{I}^a_p = \sum_b (M_q)^a_b\mathcal{I}^b_p$$

so for $a<n$, the component $a$ satisfies

$$z\partial_q\mathcal{I}_p^a=\frac{1}{q}\mathcal{I}_p^{a+1}$$

which implies $\mathcal{I}_p^n=(qz\partial_q)^n \mathcal{I}_p^0$; combining this with the equation obtained from the first column,

$$z\partial_q\mathcal{I}_p^n=\mathcal{I}_p^0$$

we obtain for $\mathcal{I}_p^0$ the $(n+1)$-th order ODE

$$(z\partial_q)\bigl(qz\partial_q\bigr)^n \mathcal{I}^0_p = \mathcal{I}^0_p$$

which is the quantum differential equation of $\mathbb{P}^n$, identical to the hypergeometric ODE satisfied by the A-side $J$-function. In the case of the stationary phase asymptotic, the coordinates in which $\omega$ becomes the standard volume form are $u_i = \log\x_i$, so the Hessian in [Proposition 3](#prop3){: data-lid="7757y" } must be computed with respect to $u$. Since at $x_\zeta$, the derivatives $\partial_{u_i}\partial_{u_j} W_q$ have diagonal entries $2x_\zeta$ and off-diagonal entries $x_\zeta$ ($\mathbf{1} := (1,\ldots,1)^\top$),

$$\Hess_{x_\zeta}(W_q) = x_\zeta\bigl(I_n + \mathbf{1}\mathbf{1}^\top\bigr),\qquad \det \Hess_{x_\zeta}(W_q) = (n+1) (\zeta q^{1/(n+1)})^{n}$$

and the critical value is $W_q(x_\zeta) = (n+1) \zeta q^{1/(n+1)}$, it follows from [Proposition 3](#prop3){: data-lid="8s6tr" } that

$$\mathcal{I}_{\Gamma_{x_\zeta}}(q, z) \sim (2\pi z)^{n/2} \frac{\exp\bigl((n+1) \zeta q^{1/(n+1)}/z\bigr)}{\sqrt{(n+1)(\zeta q^{1/(n+1)})^{n}}} (1 + O(z))$$

holds.
:::

---

**References**

**[CK]** D. A. Cox, S. Katz, *Mirror Symmetry and Algebraic Geometry*, Mathematical Surveys and Monographs **68**, AMS, 1999.  
**[MS]** K. Hori, S. Katz, A. Klemm, R. Pandharipande, R. Thomas, C. Vafa, R. Vakil, E. Zaslow, *Mirror Symmetry*, Clay Mathematics Monographs **1**, AMS, 2003.

---

[^1]: Here, $m_1, \ldots, m_N$ is a basis for the character lattice $M$ over $\mathbb{Z}$ ([\[Toric Geometry\] §Logarithmic Differential Forms on Toric Varieties, ⁋Proposition 13](/en/math/toric_geometry/logarithmic_differentials#prop13){: data-lid="c34qh" }).
