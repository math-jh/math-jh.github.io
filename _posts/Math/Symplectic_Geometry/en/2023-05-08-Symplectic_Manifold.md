---
title: "Symplectic Manifolds"
description: "This post covers the definition of symplectic manifolds using symplectic forms on manifolds. It introduces the fundamental properties and structures of symplectic manifolds, which exist only in even dimensions."
excerpt: "Definition and properties of symplectic manifolds"

categories: [Math / Symplectic Geometry]
permalink: /en/math/symplectic_geometry/symplectic_manifold
sidebar: 
    nav: "symplectic_geometry-en"

date: 2023-05-08
weight: 3
translated_at: 2026-09-06T19:15:05+00:00
translation_source: antigravity-gemini-3.8-flash-high
---
In **[MS]**, after introducing symplectic vector spaces, the authors spend some more time introducing the Maslov class and related topics. We postpone these until we need them later when discussing Floer theory, and follow **[CdS]** to first define symplectic manifolds.

::: Definition 1
A *symplectic form* $\omega$ defined on a manifold $M$ is a differential $2$-form such that $\dd{\omega}=0$ and, for every $p\in M$, the map $\omega_p:T_pM\times T_pM\rightarrow \mathbb{R}$ is a linear symplectic form. In this case, $(M,\omega)$ is called a *symplectic manifold*. 
:::

For a symplectic manifold $(M,\omega)$, since the vector space $T_pM$ is equipped with the linear symplectic form $\omega_p$ ([§Symplectic Vector Spaces, ⁋Definition 1](/en/math/symplectic_geometry/linear_symplectic_geometry#def1)), $\dim T_pM$ is even, and therefore $M$ must also be even-dimensional. 

## Examples

::: Example 2
1. Endowing Euclidean space $\mathbb{R}^{2n}$ with coordinates $(x_1,\ldots, x_n,y_1,\ldots, y_n)$, if we define 

	$$\omega_0=\sum_{i=1}^n \dd{x_i}\wedge \dd{y_i}$$

	then since this is a $2$-form with constant coefficients, $\dd{\omega_0}=0$, and since it gives the standard linear symplectic form at each point, it is nondegenerate. We call this the *canonical symplectic form* on $\mathbb{R}^{2n}$, which is precisely the form that appeared on the phase space in [§Classical Mechanics](/en/math/symplectic_geometry/classical_mechanics).

2. Consider the cotangent bundle $M=T^\ast Q$ of an arbitrary manifold $Q$. With respect to the projection $\pi:T^\ast Q\rightarrow Q$, define the *tautological $1$-form* $\lambda$ at a point $(q,p)\in T^\ast Q$ (that is, $p\in T_q^\ast Q$) by 

	$$\lambda_{(q,p)}(\xi)=p\bigl(\dd{\pi_{(q,p)}}(\xi)\bigr),\qquad \xi\in T_{(q,p)}(T^\ast Q)$$

	and set $\omega=-\dd{\lambda}$. In local coordinates $(q_1,\ldots, q_n)$ on $Q$ and the corresponding fiber coordinates $(p_1,\ldots, p_n)$, we have $\lambda=\sum_i p_i\dd{q_i}$, so 

	$$\omega=-\dd{\lambda}=\sum_{i=1}^n \dd{q_i}\wedge \dd{p_i}$$

	which has the same form as in (1) and is therefore nondegenerate, and $\omega=-\dd{\lambda}$ is closed because it is exact. In this way, the cotangent bundle always carries a canonical symplectic structure, which is the phase space of classical mechanics. 

3. Consider a nowhere-vanishing $2$-form (i.e., an area form) $\sigma$ on an orientable surface $\Sigma$. Since $\Sigma$ is $2$-dimensional, $\dd{\sigma}$ is a $3$-form, hence $0$, and since $\sigma$ is nonzero at each point, it is nondegenerate. Therefore, every orientable surface equipped with an area form becomes a symplectic manifold.
:::

Kähler manifolds, especially $\mathbb{CP}^n$ equipped with the Fubini--Study form, are also important examples, but since these require the language of complex geometry, we will treat them later. 

## Volume Form and Orientation

Nondegeneracy ensures that the top power of $\omega$ does not vanish, endowing a symplectic manifold with a natural orientation. 

::: Proposition 3
For a $2n$-dimensional symplectic manifold $(M,\omega)$, the wedge product of $n$ copies of $\omega$,

$$\omega^n=\underbrace{\omega\wedge\cdots\wedge\omega}_{n}$$

is a nowhere-vanishing $2n$-form, that is, a volume form. Consequently, $M$ is orientable.
:::
::: Proof
At each point $p\in M$, since $\omega_p$ is a linear symplectic form on $T_pM$, by [§Symplectic Vector Spaces, ⁋Lemma 2](/en/math/symplectic_geometry/linear_symplectic_geometry#lem2) there exists a basis $e_1,\ldots, e_n,f_1,\ldots, f_n$ of $T_pM$ such that with respect to the dual basis $e_1^\ast,\ldots, f_n^\ast$,

$$\omega_p=\sum_{i=1}^n e_i^\ast\wedge f_i^\ast$$

holds. (By nondegeneracy, the degenerate components $u_j$ in the lemma do not appear.) Then 

$$\omega_p^n=n!e_1^\ast\wedge f_1^\ast\wedge\cdots\wedge e_n^\ast\wedge f_n^\ast\neq 0$$

holds. Therefore, $\omega^n$ is a nowhere-vanishing $2n$-form, and since a nowhere-vanishing top-degree form is a volume form, it defines an orientation on $M$. ([\[Smooth Manifolds\] §Orientation](/en/math/manifolds/orientation)) 
:::

::: Remark 4
If $M$ is a compact symplectic manifold without boundary, $\omega$ can never be exact. Indeed, if $\omega=\dd{\alpha}$, then since $\omega$ is closed, 

$$\omega^n=\dd{\alpha}\wedge\omega^{n-1}=\dd{(\alpha\wedge\omega^{n-1})}$$

would be exact, so by Stokes' theorem ([\[Smooth Manifolds\] §Stokes' Theorem, ⁋Corollary 2](/en/math/manifolds/stokes_theorem#cor2)), $\int_M\omega^n=0$. However, by [Proposition 3](#prop3), $\omega^n$ is a volume form, so its integral cannot be $0$, which is a contradiction. From this, we see that a closed manifold whose second cohomology vanishes, such as, for $n\geq 2$, $S^{2n}$, cannot admit a symplectic structure. 
:::

## Symplectomorphisms

A morphism preserving the structure between symplectic manifolds is given as follows. 

::: Definition 5
Between two symplectic manifolds $(M,\omega)$ and $(M',\omega')$, a diffeomorphism $\varphi:M\rightarrow M'$ is called a *symplectomorphism* if $\varphi^\ast\omega'=\omega$. 
:::

Unlike isometries in Riemannian geometry, as seen in the next section and [Remark 8](#rmk8), symplectomorphisms always exist abundantly on a local level. This is the fundamental point where symplectic geometry differs from Riemannian geometry. 

## Hamiltonian Vector Fields and Poisson Brackets

The most important application of nondegeneracy is converting the differential of a function into a vector field. For each vector field $X$, if we define the $1$-form $\iota_X\omega$ by $(\iota_X\omega)(Y)=\omega(X,Y)$, then since $\omega$ is nondegenerate, the correspondence $X\mapsto\iota_X\omega$ is an isomorphism between vector fields and $1$-forms (as $C^\infty(M)$-modules). 

::: Definition 6
For a symplectic manifold $(M,\omega)$ and a function $H\in C^\infty(M)$, we define the *Hamiltonian vector field* of $H$, denoted $X_H$, to be the unique vector field satisfying 

$$\iota_{X_H}\omega=\dd{H}.$$
:::

Since the correspondence seen above is an isomorphism, such an $X_H$ indeed exists uniquely. When $M=\mathbb{R}^{2n}$ is equipped with the canonical form $\omega_0$, this definition reduces to the very vector field defined by Hamilton's equations in [§Classical Mechanics, ⁋Proposition 1](/en/math/symplectic_geometry/classical_mechanics#prop1); thus the integral flow of $X_H$ describes the motion of a system under the energy $H$. 

This flow preserves $\omega$. Indeed, from Cartan's formula in [\[Smooth Manifolds\] §Lie Derivative, ⁋Proposition 4](/en/math/manifolds/Lie_derivative#prop4) and $\dd{\omega}=0$, we have 

$$\mathcal{L}_{X_H}\omega=\iota_{X_H}\dd{\omega}+\dd{(\iota_{X_H}\omega)}=\dd{(\dd{H})}=0$$

and for the flow of $X_H$, denoted $\varphi^t$, the derivative of $(\varphi^t)^\ast\omega$ with respect to $t$ is $(\varphi^t)^\ast(\mathcal{L}_{X_H}\omega)$, so $(\varphi^t)^\ast\omega=\omega$ holds wherever the flow is defined. In other words, for each function $H\in C^\infty(M)$, one obtains a $1$-parameter family of symplectomorphisms. 

::: Definition 7
For a symplectic manifold $(M,\omega)$ and two functions $f,g\in C^\infty(M)$, we define their *Poisson bracket* $\{f,g\}$ by 

$$\{f,g\}=\omega(X_f,X_g).$$
:::

From the definition, $\{f,g\}=(\iota_{X_f}\omega)(X_g)=\dd{f}(X_g)=X_g f$, so along the flow of $g$, the Poisson bracket is the rate of change of $f$. Since $\omega$ is antisymmetric, $\{f,g\}=-\{g,f\}$, and since $X_f$ is a derivation, the Leibniz rule $\{f,gh\}=\{f,g\}h+g\{f,h\}$ holds in each argument. Furthermore, one can show that the condition $\dd{\omega}=0$ is precisely equivalent to the Jacobi identity $\{f,\{g,h\}\}+\{g,\{h,f\}\}+\{h,\{f,g\}\}=0$, and therefore $(C^\infty(M),\{-,-\})$ forms a Lie algebra. 

::: Remark 8
Item 1 of [Example 2](#ex2) is not merely a local model. *Darboux's theorem*, which we will discuss in the next post, shows that any symplectic manifold $(M,\omega)$ is symplectomorphic to $(\mathbb{R}^{2n},\omega_0)$ in a neighborhood of each point. That is, symplectic manifolds have no local invariants like curvature, and all symplectic manifolds look locally identical. This is the precise meaning of the "local abundance" mentioned after [Definition 5](#def5). 
:::

## Lagrangian Submanifolds

Elevating the role played by Lagrangian subspaces in linear symplectic geometry ([§Symplectic Vector Spaces, ⁋Definition 3](/en/math/symplectic_geometry/linear_symplectic_geometry#def3)) to the manifold level gives Lagrangian submanifolds. This is the most important class of submanifolds in symplectic geometry.

::: Definition 9
For a $2n$-dimensional symplectic manifold $(M,\omega)$, a submanifold $L\subseteq M$ is called a *Lagrangian submanifold* if for the inclusion map $\iota:L\hookrightarrow M$, $\iota^\ast\omega=0$ and $\dim L=n=(\dim M)/2$.
:::

The condition $\iota^\ast\omega=0$ means that at each point $p\in L$, on the tangent space $T_pL\subseteq T_pM$, $\omega_p$ is identically $0$, that is, $T_pL$ is an isotropic subspace. When the dimension condition is added, [§Symplectic Vector Spaces, ⁋Lemma 4](/en/math/symplectic_geometry/linear_symplectic_geometry#lem4) implies that $T_pL$ is a Lagrangian subspace at each point. In short, a Lagrangian submanifold is a submanifold whose tangent spaces are Lagrangian subspaces at each point.

::: Example 10
1. On a surface, that is, a $2$-dimensional symplectic manifold, any smooth curve (1-dimensional submanifold) is Lagrangian. This is because on a $1$-dimensional space, an alternating $2$-form is always $0$, so $\iota^\ast\omega=0$ is automatic, and $\dim=1=(1/2)\cdot 2$.

2. For the cotangent bundle $T^\ast Q$ ([Example 2](#ex2)), each fiber $T_q^\ast Q$ is Lagrangian. In local coordinates, the fiber is $\{q=\text{const}\}$ and its tangent space is spanned by the $\partial/\partial p_i$; restricting $\omega=\sum_i \dd{q_i}\wedge \dd{p_i}$ to it, every $\dd{q_i}$ vanishes and it becomes $0$. The dimension is also $n=(\dim T^\ast Q)/2$.
:::

In the cotangent bundle, submanifolds lying along the direction of the base $Q$ correspond precisely to $1$-forms, and among these, only closed forms are Lagrangian.

::: Proposition 11
On a manifold $Q$, for a $1$-form $\alpha$, its graph

$$\Gamma_\alpha=\{(q,\alpha_q)\mid q\in Q\}\subseteq T^\ast Q$$

is a Lagrangian submanifold with respect to the standard symplectic form $\omega=-\dd{\lambda}$ ([Example 2](#ex2)) if and only if $\alpha$ is a closed form ($\dd{\alpha}=0$). In particular, the zero section is always Lagrangian.
:::
::: Proof
Viewing the $1$-form $\alpha$ as a section $s_\alpha:Q\rightarrow T^\ast Q$, $q\mapsto(q,\alpha_q)$, we have $\Gamma_\alpha=s_\alpha(Q)$, and $s_\alpha$ is a diffeomorphism between $Q$ and $\Gamma_\alpha$. The key point is that the pullback of the tautological $1$-form $\lambda$ ([Example 2](#ex2)) is $s_\alpha^\ast\lambda=\alpha$. Indeed, for any $\xi\in T_qQ$,

$$(s_\alpha^\ast\lambda)(\xi)=\lambda_{(q,\alpha_q)}\bigl(\dd{s_\alpha}(\xi)\bigr)=\alpha_q\bigl(\dd{\pi}(\dd{s_\alpha}(\xi))\bigr)=\alpha_q\bigl(\dd{(\pi\circ s_\alpha)}(\xi)\bigr)=\alpha_q(\xi)$$

where the last equality follows because $\pi\circ s_\alpha=\id_Q$. Therefore,

$$s_\alpha^\ast\omega=s_\alpha^\ast(-\dd{\lambda})=-\dd{(s_\alpha^\ast\lambda)}=-\dd{\alpha}.$$

Since $s_\alpha$ is a diffeomorphism between $Q$ and $\Gamma_\alpha$, on $\Gamma_\alpha$, the restriction of $\omega$ being $0$ is equivalent to $s_\alpha^\ast\omega=0$, that is, $\dd{\alpha}=0$. Meanwhile, $\dim\Gamma_\alpha=\dim Q=n=(\dim T^\ast Q)/2$ always holds, so $\Gamma_\alpha$ being Lagrangian is precisely equivalent to $\alpha$ being a closed form. If $\alpha=0$, then $\dd{\alpha}=0$, and hence the zero section $\Gamma_0\cong Q$ is Lagrangian.
:::

::: Remark 12
Lagrangian submanifolds even subsume morphisms between symplectic manifolds. Given two symplectic manifolds $(M,\omega)$ and $(M',\omega')$, if we endow their product $M\times M'$ with the symplectic form $\Omega=\pi^\ast\omega-\pi'^\ast\omega'$ ($\pi,\pi'$ being the projections onto each factor), then a diffeomorphism $\varphi:M\rightarrow M'$ is a symplectomorphism ([Definition 5](#def5)) if and only if its graph $\Gamma_\varphi=\{(m,\varphi(m))\}$ is a Lagrangian submanifold of $(M\times M',\Omega)$. Indeed, for $j:M\rightarrow M\times M'$, $m\mapsto(m,\varphi(m))$, we have $j^\ast\Omega=j^\ast\pi^\ast\omega-j^\ast\pi'^\ast\omega'=\omega-\varphi^\ast\omega'$ and $\dim\Gamma_\varphi=\dim M=(\dim(M\times M'))/2$, so $\Gamma_\varphi$ being Lagrangian is equivalent to $\varphi^\ast\omega'=\omega$. This phenomenon, where even symplectic morphisms reduce to Lagrangians, is summarized by Weinstein's motto that "a morphism in the symplectic category is a Lagrangian."
:::

---

**References**

**[CdS]** A. Cannas da Silva, *Lectures on Symplectic Geometry*, Lecture Notes in Mathematics 1764, Springer, 2008.  
**[MS]** D. Mcduff and D. Salamon. *Introduction to symplectic topology*. Oxford graduate texts in mathematics. Oxford University Press, 2017.
