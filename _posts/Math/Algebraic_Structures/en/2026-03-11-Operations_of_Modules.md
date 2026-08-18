---
title: "Direct Products, Direct Sums, and Tensor Products of Modules"
description: "We define direct products and direct sums of R-modules from a categorical perspective and examine their properties as products and coproducts. Direct products preserve kernels and cokernels, direct sums preserve kernels, and R-Mod forms an abelian category."
excerpt: "Products, coproducts, and tensor products in the module category"

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/operations_of_modules
sidebar: 
    nav: "algebraic_structures-en"

date: 2024-05-12
weight: 202
translated_at: 2026-08-18T08:15:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-08-18T08:15:04+00:00
---
## Direct Products and Direct Sums of Modules

The category $\lMod{A}$ is bicomplete. To show this, we must construct arbitrary products and coproducts in $\lMod{A}$, and for this it suffices to exhibit natural $A$-actions on the product and coproduct taken in $\Ab$.

Let $(M_i)_{i\in I}$ be a family of $A$-modules. Then the action on $\prod M_i$ is given by the formula

$$A\otimes\left(\prod_{i\in I}M_i\right)\overset{\id_A\otimes\pr_i}{\longrightarrow} A\otimes M_i \overset{\rho_i}{\longrightarrow} M_i $$

which defines $A\otimes\left(\prod M_i\right) \rightarrow M_i$, and then by the universal property of the product in $\Ab$ we obtain $A\otimes\left(\prod M_i\right) \rightarrow \prod M_i$ and verify that this satisfies the action axioms.

For the coproduct, since $A\otimes-$ is a left adjoint from $\Ab$ to $\Ab$, it preserves colimits, and therefore

$$A\otimes\left(\bigoplus_{i\in I} M_i\right)\cong\bigoplus_{i\in I}(A\otimes M_i)\overset{\bigoplus \rho_i}{\longrightarrow} \bigoplus_{i\in I}M_i$$

defines an action on $\bigoplus M_i$. For equalizers and coequalizers, given two module homomorphisms $u,v:M \rightarrow N$, we have

$$\Eq(u,v)=\{x\in M\mid u(x)=v(x)\}$$

and

$$\CoEq(u,v)=N/N',\qquad N'=\langle u(x)-v(x)\rangle$$

That is, the following holds.

::: Theorem 1
$\lMod{A}$ is a bicomplete category; in particular, the product of a family $(M_i)$ of $A$-modules is their direct product, and the coproduct is their direct sum.
:::

Thus the direct product preserves kernels, and the direct sum preserves cokernels. ([[Category Theory] §Limits, ⁋Proposition 10](/en/math/category_theory/limits#prop10)) Moreover, they satisfy the following further property.

::: Proposition 2
Let $(M_i)_{i\in I},(N_i)_{i\in I}$ be two families of $A$-modules and let $u_i: M_i \rightarrow N_i$ be linear maps between them; consider the induced maps $\bigoplus u_i:\bigoplus M_i \rightarrow \bigoplus N_i$ and $\prod u_i: \prod M_i \rightarrow \prod N_i$. Then the following hold.

1. If each $u_i$ is surjective, then $\prod u_i$ is also surjective, and conversely.
2. If each $u_i$ is injective, then $\bigoplus u_i$ is also injective, and conversely.
:::

The proof follows by writing out $\prod u_i$ and $\bigoplus u_i$ coordinatewise. In particular, from this proposition we see that the direct product also preserves cokernels, and the direct sum also preserves kernels.

We have already observed that for arbitrary $M,N\in\lMod{A}$, the set $\Hom_{\lMod{A}}(M,N)$ is an abelian group. It is easy to check that this addition is compatible with composition, and that the category $\lMod{A}$ is an additive category with the zero module $0$ as zero object. ([[Category Theory] §Abelian Categories, ⁋Definition 1](/en/math/category_theory/abelian_categories#def1))

Moreover, $\lMod{A}$ is an abelian category. ([[Category Theory] §Abelian Categories, ⁋Definition 3](/en/math/category_theory/abelian_categories#def3)) To verify this, one checks that any monomorphism $u:M \rightarrow N$ is the kernel of its cokernel $N \rightarrow N/M$, and any epimorphism $v:M \rightarrow N$ is the cokernel of its kernel $\ker v$, namely $M \rightarrow M/\ker v$.

## Free Modules

In [[§Modules, ⁋Example 5](/en/math/algebraic_structures/modules#ex5)] we observed that a ring $A$ carries the structure of an $A$-module. Hence any $A$-module homomorphism $u:A \rightarrow M$ is uniquely determined by $u(1)$. For any $\alpha\in A$,

$$u(\alpha)=u(\alpha\cdot 1)=\alpha\cdot u(1)$$

In other words, the following isomorphism

$$\Hom_A(A, M)\cong\Hom_\Set(\ast, U(M))$$

holds. Here $U:\lMod{A} \rightarrow \Set$ is the forgetful functor. That is, $A$ is a representation of the forgetful functor $U$.

On the other hand, since we have verified that $\lMod{A}$ has coproducts $\bigoplus$, if the left adjoint $F: \Set \rightarrow \lMod{A}$ of $U$ exists then the formula

$$F(X)=F\left(\coprod_{x\in X} \{x\}\right)\cong\bigoplus_{x\in X} F(\{x\})$$

must hold, and using the representation above we know that we must define $F(X)=\bigoplus_{x\in X}Ax$. Conversely, defining $F(X)$ in this way and, for a function $u:X\rightarrow Y$, defining $F(u)$ to be the linear map sending each generator to its image, the universal property of the coproduct together with the representation above yield, for any $A$-module $M$, the isomorphism

$$\Hom_A\biggl(\bigoplus_{x\in X}Ax,M\biggr)\cong\prod_{x\in X}\Hom_A(A,M)\cong\prod_{x\in X}U(M)\cong\Hom_\Set(X,U(M))$$

Since each correspondence here is given only by composition of linear maps and of functions, it is natural in both $X$ and $M$, and therefore we obtain the following.

::: Proposition 3
For the forgetful functor $U:\lMod{A} \rightarrow\Set$ and the free functor $F:\Set \rightarrow\lMod{A}$ defined above, the adjunction $F\dashv U$ exists.
:::

For any set $X$, an $A$-module isomorphic to $F(X)$ is called a *free $A$-module*.

## Tensor Products of Modules

Meanwhile, we can also define the tensor product of $A$-modules. We begin with the following definition.

::: Definition 4
Let a ring $A$, a right $A$-module $M$, and a left $A$-module $N$ be given. Then a function $f:M\times N \rightarrow L$ is called *$A$-balanced* if $f$ is bilinear as a map of abelian groups and additionally satisfies

$$f(x\alpha, y)=f(x,\alpha y)$$
:::

For fixed $M\in\obj(\rMod{A}),N\in\obj(\lMod{A})$, define the set $\Balan_A(M,N;L)$ by

$$\Balan_A(M,N;L)=\{\text{$A$-balanced maps from $M\times N$ to $L$}\}$$

Then the following theorem holds.

::: Theorem 5
The functor $\Balan_A(M,N;-):\lMod{\mathbb{Z}}=\Ab\rightarrow\Set$ is a representable functor.
:::
::: Proof
Define the subgroup $M'$ of the free abelian group $F(M\times N)$ by

$$M'=\left\langle (x, y_1+y_2)-(x,y_1)-(x,y_2), (x_1+x_2,y)-(x_1,y)-(x_2,y), (x\alpha,y)-(x,\alpha y)\right\rangle$$

Then by the universal property of the free abelian group, for any function $f:M\times N \rightarrow L$ there exists a group homomorphism $\hat{f}:F(M\times N)\rightarrow L$, and if $f$ is $A$-balanced then the kernel of this $\hat{f}$ contains $M'$, so $\hat{f}$ defines a group homomorphism from $F(M\times N)/M'$ to $L$.

The naturality of the isomorphism $\Balan_A(M,N;L)\cong\Hom_\Ab(F(M\times N)/M',L)$ still needs to be checked, but this is a straightforward computation so we omit it.
:::

We write the representation thus obtained as $M\otimes_AN$. Then the following holds.

::: Theorem 6 ($\otimes\dashv\Hom$)
The adjunction

$$\Hom_\mathbb{Z}(M\otimes_A N, L)\cong\Hom_{\rMod{A}}(M,\Hom_\mathbb{Z}(N, L))\cong\Hom_{\lMod{A}}(N,\Hom_\mathbb{Z}(M, L))$$

exists.
:::

The proof is obtained by associating to an $A$-balanced map $f:M\times N\rightarrow L$ the map $x\mapsto f(x,-)$, which gives $\tilde{f}(x\alpha)=\tilde{f}(x)\alpha$ and hence $\Balan_A(M,N;L)\cong\Hom_{\rMod{A}}(M,\Hom_\mathbb{Z}(N,L))$; fixing the second variable similarly yields $\Hom_{\lMod{A}}(N,\Hom_\mathbb{Z}(M,L))$.

Therefore $\otimes$ commutes with colimits, and $\Hom$ commutes with limits. In particular, we obtain the following isomorphisms of abelian groups

$$M\otimes_A\left(\bigoplus_{i\in I} N_i\right)\cong \bigoplus_{i\in I} M\otimes_AN_i,\qquad \left(\bigoplus_{i\in I} M_i\right)\otimes_A N\cong\bigoplus_{i\in I} M_i\otimes_AN\tag{1}$$

and

$$\Hom_{\lMod{A}}\left(M,\prod_{i\in I} N_i\right)\cong\prod_{i\in I}\Hom_{\lMod{A}}(M, N_i),\qquad \Hom_{\lMod{A}}\left(\bigoplus_{i\in I} M_i, N\right)\cong \prod_{i\in I}\Hom_{\lMod{A}}(M_i,N)\tag{2}$$

In the special case $A=\mathbb{Z}$, this recovers the contents of [[§Abelian Groups, §§Tensor Products](/en/math/algebraic_structures/abelian_groups#tensor-products)]; the isomorphisms above were omitted in that article for reasons of length.

## Tensor Products of Modules over Commutative Rings

The $M\otimes_A N$ defined above does not carry an $A$-module structure. If we try to define an action of $A$ on $M\otimes_A N$, it would be natural to set

$$(x\alpha)\otimes_A y=x\otimes_A(\alpha y)$$

equal to $\alpha(x\otimes_Ay)$, but computing $(\alpha\beta)(x\otimes_Ay)$ and $\alpha(\beta(x\otimes_Ay))$ yields

$$(x\alpha\beta)\otimes_A y,\qquad (x\beta\alpha)\otimes_A y$$

which would be different elements. The reason $M$ is taken as a right module and $N$ as a left module in the definition of the tensor product is similar.

If $M$ has not only a right $A$-module structure but also a compatible left $B$-module structure, we call $M$ a $(B,A)$-bimodule. That is, for any $\alpha\in A$, $\beta\in B$, $x\in M$ the equation

$$(\beta\cdot_B x)\cdot_A\alpha=\beta\cdot_B(x\cdot_A\alpha)$$

must hold. Then the formula

$$\beta(x\otimes_A y)=(\beta x)\otimes_Ay$$

gives $M\otimes_AN$ a left $B$-module structure.

We are mostly interested in the case where $A$ is a commutative ring. Then any left $A$-module is also a right $A$-module, and vice versa. Moreover, viewing any left $A$-module as a right $A$-module in this way, these two structures form an $(A,A)$-bimodule structure. Therefore there is a natural $A$-action on $M\otimes_AN$

$$\alpha(x\otimes_Ay)=(\alpha x)\otimes_Ay=x\otimes_A(\alpha y)$$

This is again a representation of an appropriate functor.

::: Definition 7
Let a commutative ring $A$ and three $A$-modules $M,N,L$ be given. Then a function $f:M\times N \rightarrow L$ is called *$A$-bilinear* if $f$ is bilinear as a map of abelian groups and additionally satisfies

$$\alpha f(x,y)=f(\alpha x,y)=f(x,\alpha y)$$
:::

Define the set $\Bilin_A(M,N;L)$ by

$$\Bilin_A(M,N;L)=\{\text{$A$-bilinear maps from $M\times N$ to $L$}\}$$

::: Proposition 8
The functor $\Bilin_A(M,N;-):\lMod{A}\rightarrow\Set$ is a representable functor, and its representation is the *$A$-module* $M\otimes_AN$ defined above.
:::

Since an $A$-bilinear map is in particular $A$-balanced, the correspondence of [Theorem 5](#thm5) applies directly, and under this correspondence $f$ being $A$-bilinear is equivalent to $\hat{f}$ being $A$-linear. Indeed,

$$\hat{f}(\alpha(x\otimes_Ay))=\hat{f}((\alpha x)\otimes_Ay)=f(\alpha x,y)=\alpha f(x,y)=\alpha\hat{f}(x\otimes_Ay)$$

and since $M\otimes_AN$ is generated by elements of the form $x\otimes_Ay$, the converse also holds. That is, $\Bilin_A(M,N;L)\cong\Hom_A(M\otimes_AN,L)$.

On the other hand, if $A$ is a general ring then $\Hom_{\lMod{A}}(M,M')$ does not have an $A$-module structure, but if $A$ is a commutative ring then $\Hom_{\lMod{A}}(M,M')$ does carry an $A$-module structure. That is, $\Hom_A$ is an internal $\Hom$, and therefore we can refine the adjunction of [Theorem 6](#thm6) to prove the following.

::: Theorem 9
For a commutative ring $A$, the adjunction

$$\Hom_A(M\otimes_AN, L)\cong\Hom_A(M,\Hom_A(N,L))\cong\Hom_A(N,\Hom_A(M,L))$$

exists.
:::

In particular, the formulas (1), (2) above become isomorphisms of $A$-modules. Also, one can verify that $(\lMod{A},\otimes_A,A)$ is a symmetric monoidal category.

---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.
