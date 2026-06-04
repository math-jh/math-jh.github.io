---
title: "Differential Forms"
description: "We define differential forms on a manifold using the tensor bundle and exterior algebra bundle, endow them with a graded algebraic structure via the wedge product, and explain the pullback operation induced by smooth functions."
excerpt: "Differential form"

categories: [Math / Manifolds]
permalink: /en/math/manifolds/differential_forms
sidebar: 
    nav: "manifolds-en"

date: 2022-06-21
last_modified_at: 2022-06-21
weight: 12
translated_at: 2026-06-01T08:30:06+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-01T08:30:06+00:00
---
## Vector Bundles

Using [§Tangent and Cotangent Bundles, ⁋Example 5](/en/math/manifolds/tangent_and_cotangent_bundles#ex5) and [§Tangent and Cotangent Bundles, ⁋Theorem 6](/en/math/manifolds/tangent_and_cotangent_bundles#thm6), we can make the following definitions.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> For a manifold $$M$$, we define

$$\mathcal{T}^{r,s}(M)=\mathcal{T}^{r,s}(TM),\quad \bigwedge\nolimits^\ast(M)=\bigwedge(T^\ast M),\quad \bigwedge\nolimits^k(M)=\bigwedge\nolimits^k(T^\ast M)$$

and call them the *$$(r,s)$$-tensor bundle*, *exterior algebra bundle*, and *exterior $$k$$-bundle* on $$M$$, respectively. The smooth sections of these bundles,

$$\Gamma\left(\mathcal{T}^{r,s}(M)\right),\quad\Omega^\ast(M):=\Gamma\left(\bigwedge\nolimits^\ast(M)\right),\quad\Omega^k(M):=\Gamma\left(\bigwedge\nolimits^k(M)\right)$$

are called *tensor fields*, *differential forms*, and *differential $$k$$-forms*, respectively.

</div>

For two simple tensors

$$\omega=\alpha^1\otimes\cdots\otimes \alpha^r\otimes u_{r+1}\otimes\cdots\otimes u_{r+s}\in\mathcal{T}^{r,s}(T_p^\ast M),\quad u=u_1\otimes\cdots\otimes u_r\otimes \alpha^{r+1}\otimes\cdots\otimes \alpha^{r+s}\in\mathcal{T}^{r,s}(T_pM)$$

we define

$$(\omega,u)=\alpha^1(u_1)\alpha^2(u_2)\cdots \alpha^{r+s}(u_{r+s}).$$

Then $$(-,-)$$ is a non-degenerate pairing, so $$\mathcal{T}^{r,s}(T_p^\ast M)\cong\mathcal{T}^{r,s}(T_pM)^\ast$$. ([\[Linear Algebra\] §Dual Space, ⁋Corollary 5](/en/math/linear_algebra/dual_space#cor5))

Similarly, for two elements

$$\omega=\alpha^1\wedge\cdots\wedge \alpha^k\in \bigwedge\nolimits^k(T_p^\ast M),\quad u=u_1\wedge\cdots\wedge u_k\in\bigwedge\nolimits^k(T_pM)$$

if we define the pairing $$(-,-)$$ by

$$(\omega, u)=\det\bigl(\alpha^i(u_j)\bigr)$$

then we can verify that $$\bigwedge\nolimits^k(T_pM)^\ast\cong\bigwedge\nolimits^k(T_p^\ast M)$$. On the other hand, for a finite family of vector spaces $$(V_i)_{1\leq i\leq n}$$,

$$\bigoplus_{i=1}^n V_i^\ast\cong \left(\bigoplus_{i=1}^n V_i\right)^\ast$$

holds, and since $$\bigwedge(V)$$ is the direct sum of only finitely many $$\bigwedge\nolimits^k(V)$$,

$$\bigwedge(T_p^\ast M)=\bigoplus_{k\geq 0}\bigwedge\nolimits^k(T_p^\ast M)=\bigoplus_{k\geq 0}\bigwedge\nolimits^k(T_pM)^\ast\cong\left(\bigwedge(T_pM)\right)^\ast$$

holds.

## Differential Forms and Pullback

Among the objects introduced in [Definition 1](#def1), the elements of $$\Omega^\ast(M)$$ are of particular interest. By definition, any differential form $$\omega\in\Omega^\ast(M)$$ is a function $$M\rightarrow\bigwedge\nolimits^\ast(M)$$, and we write its values as

$$p\mapsto \omega_p\in\bigwedge\nolimits^\ast(T_pM).$$

If we define the wedge product of two differential forms $$\omega\wedge\eta$$ by the formula

$$(\omega\wedge\eta)_p=\omega_p\wedge\eta_p\qquad\text{for all $p\in M$}$$

then $$\Omega^\ast(M)$$ can be regarded as an $$\mathbb{N}$$-graded $$\mathbb{R}$$-algebra

$$\Omega^\ast(M)=\bigoplus_{k=0}^n\Omega^k(M).$$

Moreover, since scalar multiplication in $$\Omega^\ast(M)$$ by $$\mathbb{R}$$ can in fact be performed at each point $$p$$, we may also regard the coefficients of $$\Omega^\ast(M)$$ as $$C^\infty(M)$$. Algebraically, this can be thought of as changing the coefficient ring via the ring homomorphism $$\mathbb{R}\rightarrow C^\infty(M)$$, and henceforth we always consider $$\Omega^\ast(M)$$ as an $$\mathbb{N}$$-graded $$C^\infty(M)$$-algebra in this manner.

Now suppose a $$C^\infty$$ function $$F:M\rightarrow N$$ is given. Then the linear map $$dF_p:T_pM\rightarrow T_{F(p)}N$$ is well defined. Therefore, applying the functoriality of the exterior algebra to the dual map of $$dF_p$$, we obtain

$$\bigwedge({dF}_p^\ast):\bigwedge(T_{F(p)}^\ast N)\rightarrow\bigwedge(T_p^\ast M).$$

([\[Multilinear Algebra\] §Tensor Algebras, ⁋Definition 10](/en/math/multilinear_algebra/tensor_algebras#def10)) Let $$F^\ast$$ denote the linear map $$\Omega^\ast(N)\rightarrow\Omega^\ast(M)$$ obtained by assigning $$\bigwedge({dF}_p^\ast)$$ to each point $$p$$. That is, for any $$\omega\in\Omega^\ast(N)$$,

$$(F^\ast\omega)_p=\bigwedge({dF}_p^\ast)(\omega_{F(p)}).$$

The differential form $$F^\ast\omega$$ obtained in this way is called the *pullback* of $$\omega$$ by $$F$$. Moreover, since $$F^\ast$$ is a graded algebra homomorphism by definition, it also preserves $$\wedge$$.

In particular, suppose $$\omega$$ is a $$k$$-form. To compute $$(F^\ast\omega)_p$$ at a point $$p\in M$$, we evaluate it on $$k$$ vectors $$X_1(p),\ldots, X_k(p)$$ to obtain

$$(F^\ast\omega)_p(X_1(p),\ldots, X_k(p))=(F^\ast_p\omega_{F(p)})\bigl(X_1(p),\ldots, X_k(p)\bigr)=\omega_{F(p)}\bigl(dF_p(X_1(p)), \ldots, dF_p(X_k(p))\bigr).$$

## Exterior Derivative and de Rham Cohomology

Earlier we verified that $$\Omega^0(M)=C^\infty(M)$$. For any $$f\in C^\infty(M)$$, its differential $$df$$ is the function that takes each point $$p\in M$$ and outputs $$df_p:T_pM\rightarrow\mathbb{R}$$. ([§Examples of Differentials, ⁋Definition 6](/en/math/manifolds/examples_of_differentials#def6)) That is, $$df\in T^\ast M=\Omega^1(M)$$. This operator $$d$$ is defined for general differential forms as follows.

<div class="proposition" markdown="1">

<ins id="thm2">**Theorem 2**</ins> For a manifold $$M$$, there exists a unique degree $$1$$ anti-derivation $$d:\Omega^\ast(M)\rightarrow\Omega^\ast(M)$$ satisfying the following two conditions. ([##ref##]())

1. $$d^2=0$$,
2. For any $$f\in\Omega^0(M)$$, $$df$$ coincides with the differential of $$f$$ as above.

Moreover, this $$d$$ commutes with pullback $$F^\ast$$.

</div>

A graded algebra equipped with such a differential $$d$$ is called a *differential graded algebra*, or simply a *DG-algebra*. Meanwhile, by condition 1 above, the sequence

$$0\longrightarrow\Omega^0(M)\overset{d}{\longrightarrow}\Omega^1(M)\overset{d}{\longrightarrow}\Omega^2(M)\overset{d}{\longrightarrow}\cdots\overset{d}{\longrightarrow}\Omega^n(M)\longrightarrow 0\tag{2}$$

becomes a cochain complex. Also, since $$d$$ commutes with $$F^\ast$$ and $$F^\ast$$ is a graded algebra homomorphism, in the language above we can say that $$F^\ast$$ induces a chain map between de Rham complexes.

![Chain_map_in_dR](/assets/images/Math/Manifolds/Differential_Forms-1.png){:style="width:23.2em" class="invert" .align-center}

We call the cohomology group of the cochain complex (2) the *de Rham cohomology group* and denote it by $$H^\ast_\text{dR}(M)$$. de Rham's theorem shows that $$H_\text{dR}^\ast(M)$$ obtained in this way carries the same information as other cohomology groups defined topologically.

## Interior Multiplication

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> Consider a vector field $$X$$ on a manifold $$M$$. Then $$\iota_X:\Omega^\ast(M) \rightarrow\Omega^\ast(M)$$ is the map that assigns to any $$k$$-form $$\omega$$ the $$(k-1)$$-form $$\iota_X\omega$$ defined by the formula

$$(\iota_X\omega)(X_1,\ldots, X_{k-1})=\omega(X,X_1,\ldots, X_{k-1}).$$

This is called *interior multiplication* by $$X$$.

</div>

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> For a manifold $$M$$ and any vector field $$X$$ on it, the interior multiplication $$\iota_X$$ is an antiderivation of degree $$-1$$.

</div>


---

**References**

**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013  
**[Lee]** John M. Lee. *Introduction to Smooth Manifolds*, Graduate texts in mathematics, Springer, 2012  

---
