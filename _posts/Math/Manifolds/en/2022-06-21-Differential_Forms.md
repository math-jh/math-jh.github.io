---
title: "Differential Forms"
description: "Differential forms on manifolds are defined using tensor bundles and exterior algebra bundles. The wedge product introduces a graded algebra structure, followed by an explanation of pullbacks under smooth maps."
excerpt: "Differential forms on manifolds, wedge products, and pullbacks"

categories: [Math / Manifolds]
permalink: /en/math/manifolds/differential_forms
sidebar: 
    nav: "manifolds-en"

date: 2022-06-21
weight: 12
translated_at: 2026-09-25T11:15:05+00:00
translation_source: antigravity-gemini-3.8-flash-high
---
## Vector Bundles

Using [§Tangent and Cotangent Bundles, ⁋Example 5](/en/math/manifolds/tangent_and_cotangent_bundles#ex5){: data-lid="mqutq" } and [§Tangent and Cotangent Bundles, ⁋Theorem 6](/en/math/manifolds/tangent_and_cotangent_bundles#thm6){: data-lid="1qusz" }, we can define the following.

::: Definition 1
For a manifold $M$, 

$$\mathcal{T}^{r,s}(M)=\mathcal{T}^{r,s}(TM),\quad \bigwedge\nolimits^\ast(M)=\bigwedge(T^\ast M),\quad \bigwedge\nolimits^k(M)=\bigwedge\nolimits^k(T^\ast M)$$

are called the *$(r,s)$-tensor bundle*, *exterior algebra bundle*, and *exterior $k$-bundle* over $M$, respectively. The elements of their smooth sections

$$\Gamma\left(\mathcal{T}^{r,s}(M)\right),\quad\Omega^\ast(M):=\Gamma\left(\bigwedge\nolimits^\ast(M)\right),\quad\Omega^k(M):=\Gamma\left(\bigwedge\nolimits^k(M)\right)$$

are called a *tensor field*, a *differential form*, and a *differential $k$-form*, respectively. 
:::

For two simple tensors

$$\omega=\alpha^1\otimes\cdots\otimes \alpha^r\otimes u_{r+1}\otimes\cdots\otimes u_{r+s}\in\mathcal{T}^{r,s}(T_p^\ast M),\quad u=u_1\otimes\cdots\otimes u_r\otimes \alpha^{r+1}\otimes\cdots\otimes \alpha^{r+s}\in\mathcal{T}^{r,s}(T_pM)$$

define

$$(\omega,u)=\alpha^1(u_1)\alpha^2(u_2)\cdots \alpha^{r+s}(u_{r+s})$$

Then, since $(-,-)$ is a non-degenerate pairing, $\mathcal{T}^{r,s}(T_p^\ast M)\cong\mathcal{T}^{r,s}(T_pM)^\ast$ holds. ([\[Linear Algebra\] §Dual Space, ⁋Corollary 5](/en/math/linear_algebra/dual_space#cor5){: data-lid="bg40l" })

Similarly, for two elements

$$\omega=\alpha^1\wedge\cdots\wedge \alpha^k\in \bigwedge\nolimits^k(T_p^\ast M),\quad u=u_1\wedge\cdots\wedge u_k\in\bigwedge\nolimits^k(T_pM)$$

if we define the pairing $(-,-)$ by

$$(\omega, u)=\det\bigl(\alpha^i(u_j)\bigr)$$

we can verify that $\bigwedge\nolimits^k(T_pM)^\ast\cong\bigwedge\nolimits^k(T_p^\ast M)$. On the other hand, for a finite family of vector spaces $(V_i)_{1\leq i\leq n}$,

$$\bigoplus_{i=1}^n V_i^\ast\cong \left(\bigoplus_{i=1}^n V_i\right)^\ast$$

holds, and since $\bigwedge(V)$ is a direct sum of only finitely many $\bigwedge\nolimits^k(V)$,

$$\bigwedge(T_p^\ast M)=\bigoplus_{k\geq 0}\bigwedge\nolimits^k(T_p^\ast M)\cong\bigoplus_{k\geq 0}\bigwedge\nolimits^k(T_pM)^\ast\cong\left(\bigwedge(T_pM)\right)^\ast$$

holds.

## Differential Forms and Pullbacks

Among the objects in [Definition 1](#def1){: data-lid="lmvxa" } above, the elements of $\Omega^\ast(M)$ are of particular interest. By definition, any differential form $\omega\in\Omega^\ast(M)$ is a map $M\rightarrow\bigwedge\nolimits^\ast(M)$, and this value is written as

$$p\mapsto \omega_p\in\bigwedge(T_p^\ast M)$$

If we define the wedge product $\omega\wedge\eta$ of two differential forms by the formula

$$(\omega\wedge\eta)_p=\omega_p\wedge\eta_p\qquad\text{for all $p\in M$}$$

then, letting $n=\dim M$, we can regard $\Omega^\ast(M)$ as the $\mathbb{N}$-graded $\mathbb{R}$-algebra

$$\Omega^\ast(M)=\bigoplus_{k=0}^n\Omega^k(M)$$

Furthermore, because the scalar multiplication on $\Omega^\ast(M)$ by $\mathbb{R}$ can actually be performed at each point $p$, we may also view the coefficients of $\Omega^\ast(M)$ as $C^\infty(M)$. Algebraically, this can be viewed as changing the coefficient ring via the ring homomorphism $\mathbb{R}\rightarrow C^\infty(M)$, and henceforth we always regard $\Omega^\ast(M)$ as being endowed with this $\mathbb{N}$-graded $C^\infty(M)$-algebra structure.

Now suppose a $C^\infty$ map $F:M\rightarrow N$ is given. Then the linear map $\dd{F_p}:T_pM\rightarrow T_{F(p)}N$ is well-defined. Therefore, applying the functoriality of the exterior algebra to the dual map of $\dd{F_p}$, we obtain

$$\bigwedge({\dd{F}}_p^\ast):\bigwedge(T_{F(p)}^\ast N)\rightarrow\bigwedge(T_p^\ast M)$$

([\[Multilinear Algebra\] §Tensor Algebra, ⁋Proposition 11](/en/math/multilinear_algebra/tensor_algebras#prop11){: data-lid="hi83i" }) At each point $p$, assigning $\bigwedge({\dd{F}}_p^\ast)$ gives a linear map $\Omega^\ast(N)\rightarrow\Omega^\ast(M)$, which we denote by $F^\ast$. That is, for any $\omega\in\Omega^\ast(N)$,

$$(F^\ast\omega)_p=\bigwedge({\dd{F}}_p^\ast)(\omega_{F(p)})$$

The differential form $F^\ast\omega$ obtained in this way is called the *pullback* of $\omega$ by $F$. Furthermore, by definition $F^\ast$ is a graded algebra homomorphism, so it also preserves $\wedge$.

In particular, suppose $\omega$ is a $k$-form. At a point $p\in M$, to compute $(F^\ast\omega)_p$, substituting $k$ vectors $X_1(p),\ldots, X_k(p)$, we obtain

$$(F^\ast\omega)_p(X_1(p),\ldots, X_k(p))=(F^\ast_p\omega_{F(p)})\bigl(X_1(p),\ldots, X_k(p)\bigr)=\omega_{F(p)}\bigl(\dd{F_p}(X_1(p)), \ldots, \dd{F_p}(X_k(p))\bigr)$$

## Exterior Derivative and de Rham Cohomology

At each point $p$, since $\bigwedge\nolimits^0(T_p^\ast M)=\mathbb{R}$, $\Omega^0(M)$ in [Definition 1](#def1){: data-lid="s1j41" } is equal to $C^\infty(M)$. For any $f\in C^\infty(M)$, its differential $\dd{f}$ is the function that takes each point $p\in M$ and outputs $\dd{f_p}:T_pM\rightarrow\mathbb{R}$. ([§Examples of Differentials, ⁋Definition 6](/en/math/manifolds/examples_of_differentials#def6){: data-lid="fc98r" }) That is, $\dd{f}\in\Gamma(T^\ast M)=\Omega^1(M)$. This operator $d$ is also defined for general differential forms as follows.

::: Theorem 2
For a manifold $M$, there uniquely exists a degree $1$ anti-derivation $d:\Omega^\ast(M)\rightarrow\Omega^\ast(M)$ satisfying the following two conditions. (For the proof, see **[War]**.)

1. $d^2=0$,
2. For any $f\in\Omega^0(M)$, $\dd{f}$ is equal to the differential of $f$ as above.

Furthermore, $d$ defined in this way commutes with the pullback $F^\ast$.
:::

A graded algebra equipped with such a differential $d$ is called a *differential graded algebra*, or simply a *DG-algebra*. Meanwhile, by condition 1 above, the following sequence

$$0\longrightarrow\Omega^0(M)\overset{d}{\longrightarrow}\Omega^1(M)\overset{d}{\longrightarrow}\Omega^2(M)\overset{d}{\longrightarrow}\cdots\overset{d}{\longrightarrow}\Omega^n(M)\longrightarrow 0\tag{1}$$

becomes a cochain complex. In addition, since $d$ commutes with $F^\ast$ and $F^\ast$ is a graded algebra homomorphism, in the above language we can say that $F^\ast$ induces a chain map between the de Rham complexes.

{% diagram Math/Manifolds/Differential_Forms-1.svg width="26.08em" alt="Chain_map_in_dR" %}

We call the cohomology group corresponding to the cochain complex of (1) the *de Rham cohomology group* and denote it by $H^\ast_\text{dR}(M)$. The de Rham theorem shows that $H_\text{dR}^\ast(M)$ obtained in this way contains the same information as other topologically defined cohomology groups.

## Interior multiplication

::: Definition 3
Consider a manifold $M$ and a vector field $X$ given on it. Then $\iota_X:\Omega^\ast(M) \rightarrow\Omega^\ast(M)$ is the map that assigns to each $k$-form $\omega$ the $(k-1)$-form $\iota_X\omega$ defined by the formula

$$(\iota_X\omega)(X_1,\ldots, X_{k-1})=\omega(X,X_1,\ldots, X_{k-1})$$

where in the case $k=0$, we set $\iota_X\omega=0$. This is called the *interior multiplication* by $X$.
:::

::: Proposition 4
For a manifold $M$ and any vector field $X$ given on it, the interior multiplication $\iota_X$ is an antiderivation of degree $-1$.
:::


---

**References**

**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013  
**[Lee]** John M. Lee. *Introduction to Smooth Manifolds*, Graduate texts in mathematics, Springer, 2012

---
