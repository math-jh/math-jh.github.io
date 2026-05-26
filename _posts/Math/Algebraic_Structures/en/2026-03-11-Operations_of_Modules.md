---
title: "Direct Products, Direct Sums, and Tensor Products of Modules"
excerpt: "Products, coproducts, and tensor products in the module category"

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/operations_of_modules
header:
    overlay_image: /assets/images/Math/Algebraic_Structures/Operations_of_Modules.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_structures-en"

date: 2024-05-12
last_modified_at: 2024-05-12
weight: 202
translated_at: 2026-05-26T08:00:01+00:00
translation_source: kimi-cli
---
## Direct Products and Direct Sums of Modules

The category $$\lMod{A}$$ is a bicomplete category. To show this, we need to construct arbitrary products and coproducts in $$\lMod{A}$$, and for this it suffices to show that there are natural $$A$$-actions on the products and coproducts in $$\Ab$$.

Let a family of $$A$$-modules $$(M_i)_{i\in I}$$ be given. Then the action on $$\prod M_i$$ is defined by first defining $$A\otimes\left(\prod M_i\right) \rightarrow M_i$$ through the formula

$$A\otimes\left(\prod_{i\in I}M_i\right)\overset{\id_A\otimes\pr_i}{\longrightarrow} A\otimes M_i \overset{\rho_i}{\longrightarrow} M_i $$

and then using the universal property of the product in $$\Ab$$ to obtain $$A\otimes\left(\prod M_i\right) \rightarrow \prod M_i$$, and verifying that this satisfies the action axioms.

For the coproduct, since $$A\otimes-$$ is a left adjoint from $$\Ab$$ to $$\Ab$$, it preserves colimits, and thus through

$$A\otimes\left(\bigoplus_{i\in I} M_i\right)\cong\bigoplus_{i\in I}(A\otimes M_i)\overset{\bigoplus \rho_i}{\longrightarrow} \bigoplus_{i\in I}M_i$$

an action on $$\bigoplus M_i$$ is defined. For equalizers and coequalizers, given two module homomorphisms $$u,v:M \rightarrow N$$, we can define

$$\Eq(u,v)=\{x\in M\mid u(x)=v(x)\}$$

and

$$\CoEq(u,v)=N/N',\qquad N'=\langle u(x)-v(x)\rangle\rangle$$

That is, the following holds.

<div class="proposition" markdown="1">

<ins id="thm1">**Theorem 1**</ins> $$\lMod{A}$$ is a bicomplete category; in particular, the product of a family $$(M_i)$$ of $$A$$-modules is their direct product, and the coproduct is their direct sum.

</div>

Then the direct product preserves kernels, and the direct sum preserves cokernels. ([\[Category Theory\] §Limits, ⁋Proposition 10](/en/math/category_theory/limits#prop10)) Additionally, they also satisfy the following proposition.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> Let two families of $$A$$-modules $$(M_i)_{i\in I},(N_i)_{i\in I}$$ and linear maps $$u_i: M_i \rightarrow N_i$$ between them be given, and consider the induced maps $$\bigoplus u_i:\bigoplus M_i \rightarrow \bigoplus N_i$$ and $$\prod u_i: \prod M_i \rightarrow \prod N_i$$. Then the following hold.

1. If each $$u_i$$ is surjective, then $$\prod u_i$$ is also surjective, and the converse holds as well.
2. If each $$u_i$$ is injective, then $$\bigoplus u_i$$ is also injective, and the converse holds as well.

</div>

The proof of this is obtained by writing out $$\prod u_i$$ and $$\bigoplus u_i$$ explicitly coordinatewise. In particular, from this proposition we see that the direct product also preserves cokernels, and the direct sum also preserves kernels.

Earlier we saw that for any $$M,N\in\lMod{A}$$, the set $$\Hom_{\lMod{A}}(M,N)$$ becomes an abelian group. It is not difficult to verify that this addition behaves well under composition, and that the category $$\lMod{A}$$ is an additive category with the zero module $$0$$ as a zero object. ([\[Category Theory\] §Abelian Categories, ⁋Definition 1](/en/math/category_theory/abelian_categories#def1))

Moreover, $$\lMod{A}$$ is an abelian category. ([\[Category Theory\] §Abelian Categories, ⁋Definition 7](/en/math/category_theory/abelian_categories#def7)) To verify this, one checks that any monomorphism $$u:M \rightarrow N$$ is the kernel of its cokernel $$N \rightarrow N/M$$, and any epimorphism $$v:M \rightarrow N$$ is the cokernel of its kernel $$\ker v$$, namely $$M \rightarrow M/\ker v$$.

## Free Modules

In [§Modules, ⁋Example 5](/en/math/algebraic_structures/modules#ex5) we saw that a ring $$A$$ carries the structure of an $$A$$-module. Then any $$A$$-module homomorphism $$u:A \rightarrow M$$ is uniquely determined by $$u(1)$$, since for any $$\alpha\in A$$,

$$u(\alpha)=u(\alpha\cdot 1)=\alpha\cdot u(1)$$

In other words, the following isomorphism holds:

$$\Hom_A(A, M)\cong\Hom_\Set(\ast, U(M))$$

where $$U:\lMod{A} \rightarrow \Set$$ is the forgetful functor. That is, $$A$$ can be said to be a representation of the forgetful functor $$U$$.

On the other hand, since we have verified that $$\lMod{R}$$ has coproducts $$\bigoplus$$, if the left adjoint $$F: \Set \rightarrow \lMod{A}$$ of $$U$$ exists then the formula

$$F(X)=F\left(\coprod_{x\in X} \{x\}\right)\cong\bigoplus_{x\in X} F(\{x\})$$

must hold, and using the above representation we know that we must define $$F(X)=\bigoplus_{x\in X}Ax$$. That is, the following holds.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> For the forgetful functor $$U:\lMod{A} \rightarrow\Set$$ and the free functor $$F:\Set \rightarrow\lMod{A}$$ defined above, an adjunction $$F\dashv U$$ exists.

</div>

For any set $$X$$, $$A$$-modules isomorphic to $$F(X)$$ are called *free $$A$$-modules*.

## Tensor Products of Modules

On the other hand, we can also define the tensor product of $$A$$-modules. We begin with the following definition.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> Let a ring $$A$$, a right $$A$$-module $$M$$, and a left $$A$$-module $$N$$ be given. Then for any abelian group $$L$$, a function $$f:M\times N \rightarrow L$$ is called *$$A$$-balanced* if $$f$$ is bilinear as a map of abelian groups and additionally the following identity

$$f(x\alpha, y)=f(x,\alpha y)$$

holds.

</div>

For fixed $$M\in\obj(\rMod{A}),N\in\obj(\lMod{A})$$, define the set $$\Balan_A(M,N;L)$$ by

$$\Balan_A(M,N;L)=\{\text{$A$-balanced maps from $M\times N$ to $L$}\}$$

Then the following theorem holds.

<div class="proposition" markdown="1">

<ins id="thm5">**Theorem 5**</ins> The functor $$\Balan_A(M,N;-):\lMod{\mathbb{Z}}=\Ab\rightarrow\Set$$ is a representable functor.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Define the subgroup $$M'$$ of the free abelian group $$F(M\times N)$$ by

$$M'=\left\langle (x, y_1+y_2)-(x,y_1)-(x,y_2), (x_1+x_2,y)-(x_1,y)-(x_2,y), (\alpha x,y)-(x,\alpha y)\right\rangle$$

Then by the universal property of the free group, for any function $$f:M\times N \rightarrow L$$ there exists a group homomorphism $$\hat{f}:F(M\times N)\rightarrow L$$, and if $$f$$ is $$A$$-balanced then the kernel of this $$\hat{f}$$ contains $$M'$$, so $$\hat{f}$$ defines a group homomorphism from $$F(M\times N)/M'$$ to $$L$$.

The naturality of the isomorphism $$\Balan_A(M,N;L)\cong\Hom_\Ab(F(M\times N)/M',L)$$ still needs to be verified, but it is a straightforward computation so we omit it.

</details>

We denote the representation thus obtained by $$M\otimes_AN$$. Then the following holds.

<div class="proposition" markdown="1">

<ins id="thm6">**Theorem 6 ($$\otimes\dashv\Hom$$)**</ins> An adjunction

$$\Hom_\mathbb{Z}(M\otimes_A N, L)\cong\Hom_{\rMod{A}}(M,\Hom_\mathbb{Z}(N, L))\cong\Hom_{\lMod{A}}(N,\Hom_\mathbb{Z}(M, L))$$

exists.

</div>

Therefore $$\otimes$$ commutes with colimits, and $$\Hom$$ commutes with limits. In particular, we obtain the following isomorphisms of abelian groups:

$$M\otimes_A\left(\bigoplus_{i\in I} N_i\right)\cong \bigoplus_{i\in I} M\otimes_AN_i,\qquad \left(\bigoplus_{i\in I} M_i\right)\otimes_A N\cong\bigoplus_{i\in I} M_i\otimes_AN\tag{1}$$

and

$$\Hom_{\lMod{A}}\left(M,\prod_{i\in I} N_i\right)\cong\prod_{i\in I}\Hom_{\lMod{A}}(M, N_i),\qquad \Hom_{\lMod{A}}\left(\bigoplus_{i\in I} M_i, N\right)\cong \prod_{i\in I}\Hom_{\lMod{A}}(M_i,N)\tag{2}$$

In the special case where $$A=\mathbb{Z}$$, we recover the contents of [§Abelian Groups, §§Tensor Product](/en/math/algebraic_structures/abelian_groups#텐서곱); the above isomorphisms are ones that were omitted in that post for reasons of length.

## Tensor Products of Modules over Commutative Rings

The $$M\otimes_A N$$ defined above does not carry an $$A$$-module structure. If we try to define an action of $$A$$ on $$M\otimes_A N$$, it would be natural to set the element

$$(x\alpha)\otimes_A y=x\otimes_A(\alpha y)$$

equal to $$\alpha(x\otimes_Ay)$$, but the two elements

$$(x\alpha\beta)\otimes_A y,\qquad x\otimes_A(\alpha\beta y)$$

that arise when computing $$(\alpha\beta)(x\otimes_Ay)$$ would become different elements. In the definition of the tensor product, taking $$M$$ as a right module and $$N$$ as a left module is also for a similar reason.

If $$M$$ has not only a right $$A$$-module structure but also a compatible left $$B$$-module structure, we call $$M$$ a $$(B,A)$$-bimodule. That is, for any $$\alpha\in A$$, $$\beta\in B$$, $$x\in M$$ the identity

$$(\alpha\cdot_A x)\cdot_B\beta=\alpha\cdot_A(x\cdot_B\beta)$$

must hold. Then one can verify that the formula

$$\beta(x\otimes_A y)=(\beta x)\otimes_Ay$$

gives a left $$B$$-module structure on $$M\otimes_AN$$.

We are mostly interested in the case where $$A$$ is a commutative ring. Then any left $$A$$-module is also a right $$A$$-module, and vice versa. Moreover, viewing any left $$A$$-module as a right $$A$$-module in this way, these two structures form an $$(A,A)$$-bimodule structure. Therefore there is a natural $$A$$-action on $$M\otimes_AN$$ given by

$$\alpha(x\otimes_Ay)=(\alpha x)\otimes_Ay=x\otimes_A(\alpha y)$$

This is again a representation of an appropriate functor.

<div class="definition" markdown="1">

<ins id="def7">**Definition 7**</ins> Let a commutative ring $$A$$ and three $$A$$-modules $$M,N,L$$ be given. Then a function $$f:M\times N \rightarrow L$$ is called *$$A$$-bilinear* if $$f$$ is bilinear as a map of abelian groups and additionally the identity

$$\alpha f(x,y)=f(\alpha x,y)=f(x,\alpha y)$$

holds.

</div>

Define the set $$\Bilin_A(M,N;L)$$ by

$$\Bilin_A(M,N;L)=\{\text{$A$-bilinear maps from $M\times N$ to $L$}\}$$

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8**</ins> The functor $$\Bilin_A(M,N;-):\lMod{A}\rightarrow\Set$$ is a representable functor, and its representation is the *$$A$$-module* $$M\otimes_AN$$ defined above.

</div>

On the other hand, if $$A$$ is a general ring then $$\Hom_{\lMod{A}}(M,M')$$ does not have an $$A$$-module structure, but if $$A$$ is a commutative ring then $$\Hom_{\lMod{A}}(M,M')$$ does have an $$A$$-module structure. That is, $$\Hom_A$$ is an internal $$\Hom$$, and thus we can refine the adjunction of [Theorem 6](#thm6) to prove the following.

<div class="proposition" markdown="1">

<ins id="thm9">**Theorem 9**</ins> For a commutative ring $$A$$, the adjunction

$$\Hom_A(M\otimes_AN, L)\cong\Hom_A(M,\Hom_A(N,L))\cong\Hom_A(N,\Hom_A(M,L))$$

exists.

</div>

In particular, the formulas (1) and (2) above become isomorphisms of $$A$$-modules. Also, one can verify that $$(\lMod{A},\otimes_A,A)$$ is a symmetric monoidal category.
