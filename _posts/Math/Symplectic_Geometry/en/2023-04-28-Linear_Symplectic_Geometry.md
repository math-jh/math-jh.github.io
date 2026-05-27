---title: "Symplectic Vector Spaces"
excerpt: "Definition of symplectic forms"

categories: [Math / Symplectic Geometry]
permalink: /en/math/symplectic_geometry/linear_symplectic_geometry
header:
    overlay_image: /assets/images/Math/Symplectic_Geometry/Linear_Symplectic_Geometry.png
    overlay_filter: 0.5
sidebar: 
    nav: "symplectic_geometry-en"

date: 2023-04-28
last_modified_at: 2023-04-28
weight: 2
translated_at: 2026-05-28T11:36:15+00:00
translation_source: kimi-cli
---
Since momentum is treated as a covector in physics, it is natural to consider the cotangent bundle $$T^\ast M$$ of a manifold $$M$$ when describing phase space mathematically.

Even aside from physical reasons, $$T^\ast M$$ is far more natural than the tangent bundle $$TM$$ when describing a symplectic manifold, because $$T^\ast M$$ carries a natural symplectic form. Before examining what a symplectic form is, we first study symplectic geometry in a linear algebra setting.

## Symplectic form

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A vector space $$(V,\omega)$$ is called a *symplectic vector space* if $$\omega:V\times V\rightarrow \mathbb{R}$$ satisfies the following two conditions.

- (Skew-symmetry) For any $$v,w\in V$$, we have $$\omega(v,w)=-\omega(w,v)$$.
- (Nondegeneracy) If $$\omega(v,w)=0$$ for all $$w\in V$$, then $$v=0$$.

In this case, $$\omega$$ is called a *symplectic form*.

</div>

It is not difficult to see that every symplectic vector space must have even dimension.

<div class="proposition" markdown="1">

<ins id="lem2">**Lemma 2**</ins> Let a skew-symmetric bilinear map $$\omega:V\times V\rightarrow \mathbb{R}$$ be given. Then there exists a basis $$u_1,\ldots, u_k, e_1, \ldots,e_n,f_1,\ldots, f_n$$ of $$V$$ such that the following conditions are all satisfied.

- For all $$v\in V$$, we have $$\omega(u_i,v)=0$$.
- For all $$i,j$$, we have $$\omega(e_i,e_j)=\omega(f_i,f_j)=0$$.
- For all $$i,j$$, we have $$\omega(e_i,f_j)=\delta_{ij}$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, one can easily check that the set

$$\{u\in V\mid \omega(u,v)=0\text{ for all $v\in V$}\}$$

is a subspace of $$V$$. Thus, choosing a basis of this subspace, we obtain $$u_1,\ldots, u_k$$. Now, write $$V=U\oplus W$$. Then we can find a basis $$e_1,\ldots, e_n,f_1,\ldots, f_n$$ of $$W$$ as follows.

Choose an arbitrary vector $$e_1\in W$$. Since $$\omega$$ is non-degenerate on $$W$$, there exists $$f_1\in W$$ such that $$\omega(e_1,f_1)\neq 0$$, and by an appropriate scalar multiplication we may assume $$\omega(e_1,f_1)=1$$. Since $$\omega$$ is skew-symmetric, it is obvious that $$\omega(e_1,e_1)=\omega(f_1,f_1)=0$$.

Repeating this process, suppose vectors $$e_1,\ldots, e_k, f_1,\ldots, f_k\in W$$ satisfying the two conditions

- For all $$i,j$$, we have $$\omega(e_i,e_j)=\omega(f_i,f_j)=0$$.
- For all $$i,j$$, we have $$\omega(e_i,f_j)=\delta_{ij}$$.

are given, and choose an arbitrary vector $$e_{k+1}$$ not belonging to $$\span\{e_1,\ldots, e_k,f_1,\ldots, f_k\}\leq W$$. If for all $$i=1,\ldots, k$$,

$$\omega(e_{k+1}, e_i)=\lambda_i,\qquad\omega(e_{k+1},f_i)=\eta_i$$

then by considering the vector

$$e_{k+1}-\sum_{i=1}^k(\lambda_i f_i+\eta_i e_i)$$

instead of $$e_{k+1}$$, we may assume that $$e_{k+1}$$ satisfies

$$\omega(e_{k+1},e_i)=\omega(e_{k+1},f_i)=0\qquad\text{for all $i=1,\ldots, k$}$$

Meanwhile, since $$\omega$$ is non-degenerate on $$W$$, there exists a vector $$f_{k+1}\in W$$ such that $$\omega(e_{k+1},f_{k+1})\neq 0$$. Likewise, if $$f_{k+1}$$ satisfies

$$\omega(f_{k+1}, e_i)=\lambda_i',\qquad\omega(f_{k+1},f_i)=\eta_i'$$

then by considering the vector

$$f_{k+1}-\sum_{i=1}^k(\lambda_i' f_i+\eta_i' e_i)$$

instead of $$f_{k+1}$$, we may assume that $$f_{k+1}$$ satisfies

$$\omega(f_{k+1},e_i)=\omega(f_{k+1},f_i)=0\qquad\text{for all $i=1,\ldots, k$}$$

and then by an appropriate scalar multiplication we may assume $$\omega(e_{k+1},f_{k+1})=1$$.

</details>

In the above lemma, the subspace $$U=\span\{u_1,\ldots, u_k\}$$ is the space where $$\omega$$ vanishes identically, and thus on the complement $$W$$ of this subspace, $$\omega$$ becomes a symplectic form. Conversely, if a symplectic form is given on an arbitrary vector space, then since $$\omega$$ is non-degenerate we must have $$U=0$$, and therefore any symplectic vector space must have even dimension. In this case, the basis

$$e_1,\ldots, e_n, f_1,\ldots, f_n$$

obtained from the above lemma is called a *symplectic basis*. If a linear map preserving the symplectic form is called a *(linear) symplectomorphism*, then by choosing a symplectic basis one can verify that any symplectic vector space is symplectomorphic to the space $$(\mathbb{R}^{2n},\omega_0)$$ that we studied in the previous post.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> Let $$(V,\omega)$$ be a symplectic vector space and let $$W\leq V$$ be an arbitrary subspace. Then the *symplectic complement* of $$W$$ is the space defined by

$$W^\omega=\{v\in V\mid\omega(v,w)=0\text{ for all $w\in W$}\}$$

1. If $$W\subseteq W^\omega$$, then $$W$$ is called an *isotropic subspace*.
2. If $$W^\omega\subseteq W$$, then $$W$$ is called a *coisotropic subspace*.
3. If $$W\cap W^\omega=\{0\}$$, then $$W$$ is called a *symplectic subspace*.
4. If $$W=W^\omega$$, then $$W$$ is called a *Lagrangian subspace*.

</div>

<div class="proposition" markdown="1">

<ins id="lem4">**Lemma 4**</ins> For a symplectic vector space $$(V,\omega)$$ and its subspace $$W$$, the following hold.

1. We have $$\dim W+\dim W^\omega=\dim V$$, and $$(W^\omega)^\omega=W$$.
2. $$W$$ is a symplectic subspace if and only if $$W^\omega$$ is a symplectic subspace.
3. $$W$$ is isotropic if and only if $$W^\omega$$ is coisotropic. Also, $$W$$ is coisotropic if and only if $$W^\omega$$ is isotropic.
4. $$W$$ is Lagrangian if and only if $$W$$ is isotropic and $$\dim W=\frac{1}{2}\dim V$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

1. Since $$\omega$$ is a non-degenerate pairing, the map $$v\mapsto \omega(v,-)$$ defines an isomorphism from $$V$$ to $$V^\ast$$. ([\[Linear Algebra\], §Dual Spaces, ⁋Proposition 4](/en/math/linear_algebra/dual_space#prop4))
    
    Let $$W^\perp\subseteq V^\ast$$ be the annihilator of $$W$$. ([\[Linear Algebra\], §Dual Spaces, ⁋Definition 7](/en/math/linear_algebra/dual_space#def7)) For any $$u\in W^\omega$$,
    
    $$\omega(u,w)=0\qquad\text{for all $w\in W$}$$
    
    holds, and therefore $$\omega(u,-)$$ always lies in $$W^\perp$$. Conversely, whenever an arbitrary $$\varphi\in V^\ast$$ is given, there exists a unique $$u\in V$$ such that $$\varphi=\omega(u,-)$$, and if $$\varphi\in W^\perp$$ then
    
    $$0=\varphi(w)=\omega(u,w)\qquad\text{for all $w\in W$}$$
    
    holds, so $$u\in W^\omega$$. That is, via the above isomorphism we know that the two spaces $$W^\perp$$ and $$W^\omega$$ are isomorphic. Now the first equality of 1 is obvious from

    $$\dim V=\dim W+\dim W^\perp=\dim W+\dim W^\omega$$

    and the equality $$(W^\omega)^\omega=W$$ follows from $$W\subseteq(W^\omega)^\omega$$ and the fact that we must have $$\dim (W^\omega)^\omega=\dim W$$ by the first equality.

2. Since $$(W^\omega)^\omega=W$$, we have $$W\cap W^\omega=(W^\omega)^\omega\cap W^\omega$$.
3. If $$W\subseteq W^\omega$$, then $$(W^\omega)^\omega\subseteq W^\omega$$, so $$W^\omega$$ is coisotropic.
4. If $$W$$ is Lagrangian, then $$W=W^\omega$$, so from $$\dim W+\dim W^\omega$$ we obtain $$\dim W=\frac{1}{2}\dim V$$ and $$W$$ is an isotropic subspace. Conversely, if $$\dim W=\frac{1}{2}\dim V$$, then $$\dim W^\omega$$ is also $$\frac{1}{2}\dim V$$, and therefore an isotropic subspace satisfying such a dimension condition is Lagrangian.

</details>

## Symplectic quotient

Meanwhile, for an $$\mathbb{R}$$-vector space $$V$$ and any subspace $$W$$, the quotient space $$V/W$$ is always well defined. However, even if $$V$$ is a symplectic vector space, $$V/W$$ need not carry the structure of a symplectic vector space in general. For example, if $$W$$ is an odd-dimensional subspace, then $$V/W$$ also becomes odd-dimensional, so it certainly cannot have the structure of a symplectic vector space.

Even if $$W$$ is an even-dimensional subspace, the same is true: we may attempt to define a symplectic form on the quotient space $$V/W$$ by

$$\overline{\omega}([v_1],[v_2])=\omega(v_1,v_2)$$

but for this to be well defined, the value of

$$\omega(v_1+w_1,v_2+w_2)=\omega(v_1,v_2)+\omega(v_1,w_2)+\omega(w_1,v_2)+\omega(w_1,w_2)$$

must coincide with $$\omega(v_1,v_2)$$. If no condition is imposed on $$W$$, there is no reason for the last three terms on the right-hand side to be $$0$$, so a symplectic form on $$V/W$$ is not generally well defined. Moreover, even if $$W$$ is a symplectic subspace, only the last term on the right-hand side, namely $$\omega(w_1,w_2)$$, vanishes, so the condition is still insufficient.

To make this work, one can define the quotient space in the following manner.

<div class="proposition" markdown="1">

<ins id="lem5">**Lemma 5**</ins> Let $$(V,\omega)$$ be a symplectic vector space and let $$W$$ be a coisotropic subspace. Then there exists a unique symplectic structure $$\overline{\omega}$$ on $$W/W^\omega$$ such that the pullback of $$\overline{\omega}$$ by the projection $$W\rightarrow W/W^\omega$$ coincides with the restriction of $$\omega$$ to $$W$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

For arbitrary $$[w_1],[w_2]\in W$$, define $$\overline{\omega}([w_1],[w_2])=\omega(w_1,w_2)$$. It is obvious that if this formula yields a well-defined symplectic form, then the desired property holds. First, for any $$u_1,u_2\in W^\omega$$,

$$\omega(w_1+u_1,w_2+u_2)=\omega(w_1,w_2)+\omega(w_1,u_2)+\omega(u_1,w_2)+\omega(u_1,u_2)$$

holds, and since $$w_1,w_2,u_1,u_2$$ are all elements of $$W$$ and $$u_1,u_2$$ are elements of $$W^\omega$$, the last three terms on the right-hand side all become 0. Therefore $$\overline{\omega}$$ is well defined. That $$\overline{\omega}$$ is skew-symmetric is obvious by definition, so it suffices to show that $$\overline{\omega}$$ is non-degenerate. If $$[w]\in W$$ satisfies $$\overline{\omega}([w],[w'])=0$$ for all $$[w']\in W$$, then

$$0=\overline{\omega}([w],[w'])=\omega(w,w')\qquad\text{for all $w'\in W$}$$

so by definition $$w\in W^\omega$$ and therefore $$[w]=0$$. That is, $$\overline{\omega}$$ is non-degenerate.

</details>

Since every 1-dimensional subspace of a symplectic vector space is an isotropic subspace, by [Lemma 4](#lem4) every codimension-1 subspace $$W$$ is a coisotropic subspace. Applying [Lemma 5](#lem5) to this space, we obtain a new symplectic vector space with dimension reduced by 2 from the original vector space.
