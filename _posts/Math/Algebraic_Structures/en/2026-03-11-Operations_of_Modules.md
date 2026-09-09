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
last_polished_at: 2026-09-09T07:15:05+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
## Direct Products and Direct Sums of Modules

The category $\lMod{A}$ is a bicomplete category. To show this, we must construct arbitrary products and coproducts in $\lMod{A}$, and to do so, it suffices to show that natural $A$-actions exist on the product and coproduct in $\Ab$.

Let $(M_i)_{i\in I}$ be a family of $A$-modules. Then, for the action on $\prod M_i$, it suffices to define $A\otimes\left(\prod M_i\right) \rightarrow M_i$ via the formula

$$A\otimes\left(\prod_{i\in I}M_i\right)\overset{\id_A\otimes\pr_i}{\longrightarrow} A\otimes M_i \overset{\rho_i}{\longrightarrow} M_i $$

and then use the universal property of the product in $\Ab$ to construct $A\otimes\left(\prod M_i\right) \rightarrow \prod M_i$ and show that this satisfies the conditions for an action.

For the coproduct, since $A\otimes-$ is a left adjoint from $\Ab$ to $\Ab$, it preserves colimits, and therefore

$$A\otimes\left(\bigoplus_{i\in I} M_i\right)\cong\bigoplus_{i\in I}(A\otimes M_i)\overset{\bigoplus \rho_i}{\longrightarrow} \bigoplus_{i\in I}M_i$$

defines the action on $\bigoplus M_i$. For equalizers and coequalizers, given two module homomorphisms $u,v:M \rightarrow N$, they can be defined by

$$\Eq(u,v)=\{x\in M\mid u(x)=v(x)\}$$

and

$$\CoEq(u,v)=N/N',\qquad N'=\langle u(x)-v(x)\rangle$$

That is, the following holds.

::: Theorem 1
$\lMod{A}$ is a bicomplete category; in particular, the product of a family $(M_i)$ of $A$-modules is their direct product, and the coproduct is their direct sum.
:::

Then the direct product preserves kernels, and the direct sum preserves cokernels. ([\[Category Theory\] §Limits, ⁋Proposition 10](/en/math/category_theory/limits#prop10){: data-relation="required" }) In addition, they also satisfy the following proposition.

::: Proposition 2
Suppose that two families of $A$-modules $(M_i)_{i\in I},(N_i)_{i\in I}$ and linear maps $u_i: M_i \rightarrow N_i$ between them are given, and consider the functions $\bigoplus u_i:\bigoplus M_i \rightarrow \bigoplus N_i$ and $\prod u_i: \prod M_i \rightarrow \prod N_i$ induced by them. Then the following hold.

1. If each $u_i$ is surjective, then $\prod u_i$ is also surjective, and conversely.
2. If each $u_i$ is injective, then $\bigoplus u_i$ is also injective, and conversely.
:::

The proof of this is obtained by writing out $\prod u_i$ and $\bigoplus u_i$ directly coordinatewise. In particular, from this proposition we see that the direct product also preserves cokernels, and the direct sum also preserves kernels.

Previously, we observed that for any $M,N\in\lMod{A}$, $\Hom_{\lMod{A}}(M,N)$ is an abelian group. It is easy to check that this addition behaves well with respect to composition, and that the category $\lMod{A}$ is an additive category with the zero module $0$ as a zero object. ([\[Category Theory\] §Abelian Categories, ⁋Definition 1](/en/math/category_theory/abelian_categories#def1){: data-relation="weak" })

Moreover, $\lMod{A}$ is an abelian category. ([\[Category Theory\] §Abelian Categories, ⁋Definition 3](/en/math/category_theory/abelian_categories#def3){: data-relation="required" }) To verify this, one only needs to check that any monomorphism $u:M \rightarrow N$ is equal to the kernel of its cokernel $N \rightarrow N/M$, and any epimorphism $v:M \rightarrow N$ is equal to the cokernel of its kernel $\ker v$, namely $M \rightarrow M/\ker v$.

## Free module

In [§Modules, ⁋Example 5](/en/math/algebraic_structures/modules#ex5){: data-relation="required" }, we observed that the ring $A$ has the structure of an $A$-module. Then any $A$-module homomorphism $u:A \rightarrow M$ is uniquely determined by $u(1)$. This is because for any $\alpha\in A$,

$$u(\alpha)=u(\alpha\cdot 1)=\alpha\cdot u(1)$$

holds. In other words, the following isomorphism

$$\Hom_A(A, M)\cong\Hom_\Set(\ast, U(M))$$

holds. Here, $U:\lMod{A} \rightarrow \Set$ is the forgetful functor. That is, $A$ can be said to be a representation of the forgetful functor $U$.

On the other hand, since we previously verified that $\lMod{A}$ has the coproduct $\bigoplus$, if $U$ has a left adjoint $F: \Set \rightarrow \lMod{A}$, then the equation

$$F(X)=F\left(\coprod_{x\in X} \{x\}\right)\cong\bigoplus_{x\in X} F(\{x\})$$

must hold, and using the representation above we see that we must define $F(X)=\bigoplus_{x\in X}Ax$. Conversely, defining $F(X)$ in this way and, for a function $u:X\rightarrow Y$, setting $F(u)$ to be the linear map that maps each generator, from the universal property of the coproduct and the representation above we obtain, for any $A$-module $M$, the following isomorphism

$$\Hom_A\biggl(\bigoplus_{x\in X}Ax,M\biggr)\cong\prod_{x\in X}\Hom_A(A,M)\cong\prod_{x\in X}U(M)\cong\Hom_\Set(X,U(M))$$

Since each correspondence here is given only by the composition of linear maps and the composition of functions, it is natural in both $X$ and $M$, and therefore we obtain the following.

::: Proposition 3
For the forgetful functor $U:\lMod{A} \rightarrow\Set$ and the free functor $F:\Set \rightarrow\lMod{A}$ defined above, there exists an adjunction $F\dashv U$.
:::

For any set $X$, if isomorphic to $F(X)$, an $A$-module is called a *free $A$-module*.

## Tensor Product of Modules

Meanwhile, we can also define the tensor product of $A$-modules. First, we begin with the following definition.

::: Definition 4
Suppose that a ring $A$, a right $A$-module $M$, and a left $A$-module $N$ are given. Then, for any abelian group $L$, a function $f:M\times N \rightarrow L$ is said to be *$A$-balanced* if $f$ is bilinear as a function between abelian groups, and additionally the equation

$$f(x\alpha, y)=f(x,\alpha y)$$

holds.
:::

For fixed $M\in\obj(\rMod{A}),N\in\obj(\lMod{A})$, define the set $\Balan_A(M,N;L)$ by

$$\Balan_A(M,N;L)=\{\text{$A$-balanced maps from $M\times N$ to $L$}\}$$

Then the following theorem holds.

::: Theorem 5
The functor $\Balan_A(M,N;-):\lMod{\mathbb{Z}}=\Ab\rightarrow\Set$ is a representable functor.
:::
::: Proof
Let us define the subgroup $M'$ of the free abelian group $F(M\times N)$ by

$$M'=\left\langle (x, y_1+y_2)-(x,y_1)-(x,y_2), (x_1+x_2,y)-(x_1,y)-(x_2,y), (x\alpha,y)-(x,\alpha y)\right\rangle$$

Then by the universal property of the free abelian group, whenever a function $f:M\times N \rightarrow L$ is given, there exists a group homomorphism $\hat{f}:F(M\times N)\rightarrow L$, and if $f$ is $A$-balanced, the kernel of this $\hat{f}$ contains $M'$, so $\hat{f}$ defines a group homomorphism from $F(M\times N)/M'$ to $L$.

The naturality of the isomorphism $\Balan_A(M,N;L)\cong\Hom_\Ab(F(M\times N)/M',L)$ still needs to be shown, but as it is a straightforward calculation, we omit it.
:::

We write the representation obtained in this way as $M\otimes_AN$. Then the following holds.

::: Theorem 6 ($\otimes\dashv\Hom$)
There exists an adjunction

$$\Hom_\mathbb{Z}(M\otimes_A N, L)\cong\Hom_{\rMod{A}}(M,\Hom_\mathbb{Z}(N, L))\cong\Hom_{\lMod{A}}(N,\Hom_\mathbb{Z}(M, L))$$
:::

The proof of this is obtained by associating to an $A$-balanced map $f:M\times N\rightarrow L$ the map $x\mapsto f(x,-)$, which gives $\tilde{f}(x\alpha)=\tilde{f}(x)\alpha$ and hence yields $\Balan_A(M,N;L)\cong\Hom_{\rMod{A}}(M,\Hom_\mathbb{Z}(N,L))$; fixing the second variable similarly yields $\Hom_{\lMod{A}}(N,\Hom_\mathbb{Z}(M,L))$.

Therefore $\otimes$ commutes with colimits, and $\Hom$ commutes with limits. In particular, we obtain the following isomorphisms of abelian groups:

$$M\otimes_A\left(\bigoplus_{i\in I} N_i\right)\cong \bigoplus_{i\in I} M\otimes_AN_i,\qquad \left(\bigoplus_{i\in I} M_i\right)\otimes_A N\cong\bigoplus_{i\in I} M_i\otimes_AN\tag{1}$$

and

$$\Hom_{\lMod{A}}\left(M,\prod_{i\in I} N_i\right)\cong\prod_{i\in I}\Hom_{\lMod{A}}(M, N_i),\qquad \Hom_{\lMod{A}}\left(\bigoplus_{i\in I} M_i, N\right)\cong \prod_{i\in I}\Hom_{\lMod{A}}(M_i,N)\tag{2}$$

In the special case where $A=\mathbb{Z}$, this recovers the contents of [§Abelian Groups, §§Tensor Products](/en/math/algebraic_structures/abelian_groups#tensor-products){: data-relation="weak" }; the above isomorphisms are ones that were omitted in that article for reasons of length.

## Tensor Products of Modules over Commutative Rings

The $M\otimes_A N$ defined above does not have an $A$-module structure. This is because, if we think about defining an action of $A$ on $M\otimes_A N$, it would be natural to define the element

$$(x\alpha)\otimes_A y=x\otimes_A(\alpha y)$$

as $\alpha(x\otimes_Ay)$, but the elements

$$(x\alpha\beta)\otimes_A y,\qquad (x\beta\alpha)\otimes_A y$$

obtained by computing $(\alpha\beta)(x\otimes_Ay)$ and $\alpha(\beta(x\otimes_Ay))$ will be different elements. It is also for a similar reason that in the definition of the tensor product, $M$ is taken as a right module and $N$ as a left module.

If $M$ has not only a right $A$-module structure but also a compatible left $B$-module structure, we call $M$ a $(B,A)$-bimodule. That is, for any $\alpha\in A$, $\beta\in B$, $x\in M$, the equation

$$(\beta\cdot_B x)\cdot_A\alpha=\beta\cdot_B(x\cdot_A\alpha)$$

must hold. Then one can verify that the formula

$$\beta(x\otimes_A y)=(\beta x)\otimes_Ay$$

gives a left $B$-module structure on $M\otimes_AN$.

We are mostly interested in the case where $A$ is a commutative ring. Then any left $A$-module is also a right $A$-module, and vice versa. Moreover, viewing any left $A$-module as a right $A$-module in this way, these two structures form an $(A,A)$-bimodule structure. Therefore, there is a natural $A$-action on $M\otimes_AN$:

$$\alpha(x\otimes_Ay)=(\alpha x)\otimes_Ay=x\otimes_A(\alpha y)$$

This is also a representation of an appropriate functor.

::: Definition 7
Let a commutative ring $A$ and three $A$-modules $M,N,L$ be given. Then a function $f:M\times N \rightarrow L$ is called *$A$-bilinear* if $f$ is bilinear as a function between abelian groups and, additionally, the following equation

$$\alpha f(x,y)=f(\alpha x,y)=f(x,\alpha y)$$

holds.
:::

Define the set $\Bilin_A(M,N;L)$ by the following equation:

$$\Bilin_A(M,N;L)=\{\text{$A$-bilinear maps from $M\times N$ to $L$}\}$$

::: Proposition 8
The functor $\Bilin_A(M,N;-):\lMod{A}\rightarrow\Set$ is a representable functor, and its representation is the *$A$-module* $M\otimes_AN$ defined above.
:::

Since an $A$-bilinear map is in particular $A$-balanced, the correspondence of [Theorem 5](#thm5){: data-relation="required" } applies directly, and under this correspondence $f$ being $A$-bilinear is equivalent to $\hat{f}$ being $A$-linear. Indeed,

$$\hat{f}(\alpha(x\otimes_Ay))=\hat{f}((\alpha x)\otimes_Ay)=f(\alpha x,y)=\alpha f(x,y)=\alpha\hat{f}(x\otimes_Ay)$$

and since $M\otimes_AN$ is generated by elements of the form $x\otimes_Ay$, the converse also holds. That is, $\Bilin_A(M,N;L)\cong\Hom_A(M\otimes_AN,L)$.

On the other hand, if $A$ is a general ring then $\Hom_{\lMod{A}}(M,M')$ did not have an $A$-module structure, but if $A$ is a commutative ring then an $A$-module structure also exists on $\Hom_{\lMod{A}}(M,M')$. That is, $\Hom_A$ is an internal $\Hom$, and therefore we can further refine the adjunction of [Theorem 6](#thm6){: data-relation="required" } to prove the following.

::: Theorem 9
For a commutative ring $A$, the adjunction

$$\Hom_A(M\otimes_AN, L)\cong\Hom_A(M,\Hom_A(N,L))\cong\Hom_A(N,\Hom_A(M,L))$$

exists.
:::

In particular, the formulas (1), (2) above both become isomorphisms between $A$-modules. Also, one can verify that $(\lMod{A},\otimes_A,A)$ is a symmetric monoidal category.

---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.
