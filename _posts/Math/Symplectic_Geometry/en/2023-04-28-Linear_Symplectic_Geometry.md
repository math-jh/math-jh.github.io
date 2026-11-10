---
title: "Symplectic Vector Spaces"
description: "This post defines symplectic vector spaces and symplectic forms, the foundations of symplectic geometry, and proves that every symplectic vector space has even dimension using antisymmetry and nondegeneracy conditions."
excerpt: "Definition of symplectic forms"

categories: [Math / Symplectic Geometry]
permalink: /en/math/symplectic_geometry/linear_symplectic_geometry
sidebar: 
    nav: "symplectic_geometry-en"

date: 2023-04-28
weight: 2
translated_at: 2026-06-02T23:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-11-07T07:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
Since momentum is treated as a covector in physics, when describing phase space mathematically, for a manifold $M$, it is natural to consider the cotangent bundle $T^\ast M$.

Even aside from physical reasons, when describing a symplectic manifold, rather than the tangent bundle $TM$, $T^\ast M$ is far more natural, because $T^\ast M$ carries a natural symplectic form. Before examining what a symplectic form is, we first look at symplectic geometry in the linear algebra setting.

## Symplectic form

::: Definition 1
A finite-dimensional vector space $(V,\omega)$ is called a *symplectic vector space* if the bilinear map $\omega:V\times V\rightarrow \mathbb{R}$ satisfies the following two conditions.

- (Skew-symmetry) For any $v,w\in V$, we have $\omega(v,w)=-\omega(w,v)$.
- (Nondegeneracy) If $\omega(v,w)=0$ holds for all $w\in V$, the only such $v$ is $v=0$.

In this case, $\omega$ is called a *symplectic form*.
:::

It is not difficult to see that every symplectic vector space must be even-dimensional.

::: Lemma 2
Let a finite-dimensional vector space $V$ and an arbitrary skew-symmetric bilinear map $\omega:V\times V\rightarrow \mathbb{R}$ on it be given. Then there exists a basis $u_1,\ldots, u_k, e_1, \ldots,e_n,f_1,\ldots, f_n$ of $V$ such that the following conditions are all satisfied.

- For all $v\in V$, we have $\omega(u_i,v)=0$.
- For all $i,j$, we have $\omega(e_i,e_j)=\omega(f_i,f_j)=0$.
- For all $i,j$, we have $\omega(e_i,f_j)=\delta_{ij}$.
:::
::: Proof
First, one can easily check that the set

$$\{u\in V\mid \omega(u,v)=0\text{ for all $v\in V$}\}$$

is a subspace of $V$. Thus, choosing a basis of this subspace, we obtain $u_1,\ldots, u_k$. Now let $V=U\oplus W$. Then, for $W$, we can find a basis $e_1,\ldots, e_n,f_1,\ldots, f_n$ as follows. 

If $W=\{0\}$, there is nothing more to do, so assume $W\neq\{0\}$ and choose a nonzero vector $e_1\in W$. Then, since $\omega$ is non-degenerate on $W$, there exists, satisfying $\omega(e_1,f_1)\neq 0$, a vector $f_1\in W$, and by multiplying by a scalar as needed, we may assume $\omega(e_1,f_1)=1$. Since $\omega$ is skew-symmetric, it is clear that $\omega(e_1,e_1)=\omega(f_1,f_1)=0$.

Repeating this process, with the two conditions

- For all $i,j$, we have $\omega(e_i,e_j)=\omega(f_i,f_j)=0$.
- For all $i,j$, we have $\omega(e_i,f_j)=\delta_{ij}$.

satisfied, suppose vectors $e_1,\ldots, e_k, f_1,\ldots, f_k\in W$ are given, and choose an arbitrary vector $e_{k+1}$ not belonging to $\span\{e_1,\ldots, e_k,f_1,\ldots, f_k\}\leq W$. If for any $i=1,\ldots, k$,

$$\omega(e_{k+1}, e_i)=\lambda_i,\qquad\omega(e_{k+1},f_i)=\eta_i$$

then, instead of $e_{k+1}$, by considering the vector

$$e_{k+1}-\sum_{i=1}^k(\eta_i e_i-\lambda_i f_i)$$

we may assume that $e_{k+1}$ was a vector satisfying the following conditions:

$$\omega(e_{k+1},e_i)=\omega(e_{k+1},f_i)=0\qquad\text{for all $i=1,\ldots, k$}$$

Meanwhile, on $W$, since $\omega$ is non-degenerate, there exists, satisfying $\omega(e_{k+1},f_{k+1})\neq 0$, a vector $f_{k+1}\in W$. Similarly, if $f_{k+1}$ satisfies

$$\omega(f_{k+1}, e_i)=\lambda_i',\qquad\omega(f_{k+1},f_i)=\eta_i'$$

then, instead of $f_{k+1}$, by considering the vector

$$f_{k+1}-\sum_{i=1}^k(\eta_i' e_i-\lambda_i' f_i)$$

we may assume that $f_{k+1}$ satisfies the following conditions:

$$\omega(f_{k+1},e_i)=\omega(f_{k+1},f_i)=0\qquad\text{for all $i=1,\ldots, k$}$$

and then, by an appropriate scalar multiplication, we may assume $\omega(e_{k+1},f_{k+1})=1$. 
:::

In the above lemma, the subspace $U=\span\{u_1,\ldots, u_k\}$ is the space where $\omega$ is identically zero, and thus on the complement $W$ of this subspace, $\omega$ becomes a symplectic form. Conversely, if a symplectic form is given on an arbitrary vector space, then since $\omega$ is non-degenerate we must have $U=0$, and therefore any symplectic vector space must be even-dimensional. In this case, the basis

$$e_1,\ldots, e_n, f_1,\ldots, f_n$$

obtained from the above lemma is called a *symplectic basis*. If a linear map preserving the symplectic form is called a *(linear) symplectomorphism*, then by the choice of a symplectic basis, one can verify that any symplectic vector space is symplectomorphic to the space $(\mathbb{R}^{2n},\omega_0)$ examined in [§Classical Mechanics](/en/math/symplectic_geometry/classical_mechanics){: data-lid="a4c7o" }.

::: Definition 3
Let $(V,\omega)$ be a symplectic vector space and let $W\leq V$ be an arbitrary subspace. Then the *symplectic complement* of $W$ is the space defined by

$$W^\omega=\{v\in V\mid\omega(v,w)=0\text{ for all $w\in W$}\}$$

1. If $W\subseteq W^\omega$, then $W$ is called an *isotropic subspace*.
2. If $W^\omega\subseteq W$, then $W$ is called a *coisotropic subspace*.
3. If $W\cap W^\omega=\{0\}$, then $W$ is called a *symplectic subspace*.
4. If $W=W^\omega$, then $W$ is called a *Lagrangian subspace*.
:::

::: Lemma 4
For a symplectic vector space $(V,\omega)$ and its subspace $W$, the following hold.

1. $\dim W+\dim W^\omega=\dim V$, and $(W^\omega)^\omega=W$.
2. $W$ is a symplectic subspace if and only if $W^\omega$ is a symplectic subspace.
3. $W$ is isotropic if and only if $W^\omega$ is coisotropic. Also, $W$ is coisotropic if and only if $W^\omega$ is isotropic.
4. $W$ is Lagrangian if and only if $W$ is isotropic and $\dim W=\frac{1}{2}\dim V$.
:::
::: Proof
1. Since $\omega$ is a non-degenerate pairing, $v\mapsto \omega(v,-)$ defines an injective linear map from $V$ to $V^\ast$ ([\[Linear Algebra\] §Dual Space, ⁋Proposition 4](/en/math/linear_algebra/dual_space#prop4){: data-lid="70m05" }), and since $\dim V=\dim V^\ast$, this is an isomorphism. 
    
    Let the annihilator of $W$ be $W^\perp\subseteq V^\ast$. ([\[Linear Algebra\] §Dual Space, ⁋Definition 7](/en/math/linear_algebra/dual_space#def7){: data-lid="pp42c" }) For any $u\in W^\omega$,
    
    $$\omega(u,w)=0\qquad\text{for all $w\in W$}$$
    
    holds, and therefore $\omega(u,-)$ always belongs to $W^\perp$. Conversely, whenever an arbitrary $\varphi\in V^\ast$ is given, there exists a unique $u\in V$ such that $\varphi=\omega(u,-)$, and if $\varphi\in W^\perp$, then
    
    $$0=\varphi(w)=\omega(u,w)\qquad\text{for all $w\in W$}$$
    
    holds, so $u\in W^\omega$. That is, via the above isomorphism we know that the two spaces $W^\perp$ and $W^\omega$ are isomorphic. Now the first equality of 1 is obvious from

    $$\dim V=\dim W+\dim W^\perp=\dim W+\dim W^\omega$$

    and the equality $(W^\omega)^\omega=W$ is obtained because $W\subseteq(W^\omega)^\omega$ holds and $\dim (W^\omega)^\omega=\dim W$ must hold by the first equality.

2. Since $(W^\omega)^\omega=W$, we have $W\cap W^\omega=(W^\omega)^\omega\cap W^\omega$.
3. If $W\subseteq W^\omega$, then $(W^\omega)^\omega\subseteq W^\omega$, so $W^\omega$ is coisotropic.
4. If $W$ is Lagrangian, then $W=W^\omega$, so from $\dim W+\dim W^\omega=\dim V$ we have $\dim W=\frac{1}{2}\dim V$ and $W$ is an isotropic subspace. Conversely, if $\dim W=\frac{1}{2}\dim V$, then $\dim W^\omega$ is also $\frac{1}{2}\dim V$, and therefore an isotropic subspace satisfying such a dimension condition is Lagrangian.
:::

## Symplectic quotient

Meanwhile, for an $\mathbb{R}$-vector space $V$ and any subspace $W$, the quotient space $V/W$ is always well defined. However, even if $V$ is a symplectic vector space, $V/W$ need not carry the structure of a symplectic vector space in general. For example, if $W$ is an odd-dimensional subspace, then $V/W$ also becomes odd-dimensional, so it certainly cannot have the structure of a symplectic vector space.

Even if $W$ is an even-dimensional subspace, the same is true: we may attempt to define a symplectic form on the quotient space $V/W$ by

$$\overline{\omega}([v_1],[v_2])=\omega(v_1,v_2)$$

but for this to be well defined, the value of

$$\omega(v_1+w_1,v_2+w_2)=\omega(v_1,v_2)+\omega(v_1,w_2)+\omega(w_1,v_2)+\omega(w_1,w_2)$$

must coincide with $\omega(v_1,v_2)$. If no condition is imposed on $W$, there is no reason for the last three terms on the right-hand side to be $0$, so a symplectic form on $V/W$ is not generally well defined. Moreover, even if $W$ is an isotropic subspace, only the last term on the right-hand side, namely $\omega(w_1,w_2)$, vanishes, so the condition is still insufficient.

To make this work, one can define the quotient space in the following manner.

::: Lemma 5
Let $(V,\omega)$ be a symplectic vector space and let $W$ be a coisotropic subspace. Then there exists a unique symplectic structure $\overline{\omega}$ on $W/W^\omega$ such that the pullback of $\overline{\omega}$ by the projection $W\rightarrow W/W^\omega$ coincides with the restriction of $\omega$ to $W$.
:::
::: Proof
For arbitrary $[w_1],[w_2]\in W/W^\omega$, define $\overline{\omega}([w_1],[w_2])=\omega(w_1,w_2)$. It is obvious that if this formula yields a well-defined symplectic form, then the desired property holds. First, for any $u_1,u_2\in W^\omega$,

$$\omega(w_1+u_1,w_2+u_2)=\omega(w_1,w_2)+\omega(w_1,u_2)+\omega(u_1,w_2)+\omega(u_1,u_2)$$

holds, and since $w_1,w_2,u_1,u_2$ are all elements of $W$ and $u_1,u_2$ are elements of $W^\omega$, the last three terms on the right-hand side all become 0. Therefore $\overline{\omega}$ is well defined. That $\overline{\omega}$ is skew-symmetric is obvious by definition, so it suffices to show that $\overline{\omega}$ is non-degenerate. If $[w]\in W/W^\omega$ satisfies $\overline{\omega}([w],[w'])=0$ for all $[w']\in W/W^\omega$, then

$$0=\overline{\omega}([w],[w'])=\omega(w,w')\qquad\text{for all $w'\in W$}$$

so by definition $w\in W^\omega$ and therefore $[w]=0$. That is, $\overline{\omega}$ is non-degenerate.
:::

Since every 1-dimensional subspace of a symplectic vector space is an isotropic subspace, by [Lemma 4](#lem4){: data-lid="v63xr" } every codimension-1 subspace $W$ is a coisotropic subspace. Applying [Lemma 5](#lem5){: data-lid="kunuo" } to this space, we obtain a new symplectic vector space with dimension reduced by 2 from the original vector space.

---

**References**

**[CdS]** A. Cannas da Silva, *Lectures on Symplectic Geometry*, Lecture Notes in Mathematics 1764, Springer, 2008.  
**[MS]** D. Mcduff and D. Salamon. *Introduction to symplectic topology*. Oxford graduate texts in mathematics. Oxford University Press, 2017.
