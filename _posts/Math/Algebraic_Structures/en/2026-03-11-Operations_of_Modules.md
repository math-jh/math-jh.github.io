---
title: "Direct Products, Direct Sums, and Tensor Products of Modules"
excerpt: "Product, coproduct, and tensor product of the module category"

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/operations_of_modules
header:
    overlay_image: /assets/images/Math/Algebraic_Structures/Operations_of_Modules.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_structures-en"

date: 2026-03-11
last_modified_at: 2026-03-11
weight: 202
translated_at: 2026-05-24T21:00:03+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-24T21:00:03+00:00
---
## Direct Products and Direct Sums of Modules

The category $$\lMod{A}$$ is bicomplete. To see this, we construct arbitrary products and coproducts in $$\lMod{A}$$; for this, it suffices to exhibit natural $$A$$-actions on the product and coproduct in $$\Ab$$.

Let $$(M_i)_{i\in I}$$ be a family of $$A$$-modules. We first define the maps $$A\otimes\left(\prod M_i\right) \rightarrow M_i$$ through the composition

$$A\otimes\left(\prod_{i\in I}M_i\right)\overset{\id_A\otimes\pr_i}{\longrightarrow} A\otimes M_i \overset{\rho_i}{\longrightarrow} M_i $$

and then invoke the universal property of the product in $$\Ab$$ to obtain a map $$A\otimes\left(\prod M_i\right) \rightarrow \prod M_i$$. It remains to verify that this map satisfies the action axioms.

For the coproduct, since $$A\otimes-$$ is a left adjoint $$\Ab\to\Ab$$, it preserves colimits; hence the action on $$\bigoplus M_i$$ is given by

$$A\otimes\left(\bigoplus_{i\in I} M_i\right)\cong\bigoplus_{i\in I}(A\otimes M_i)\overset{\bigoplus \rho_i}{\longrightarrow} \bigoplus_{i\in I}M_i$$

For equalizers and coequalizers, given two module homomorphisms $$u,v:M \rightarrow N$$, we set

$$\Eq(u,v)=\{x\in M\mid u(x)=v(x)\}$$

and

$$\CoEq(u,v)=N/N',\qquad N'=\langle u(x)-v(x)\rangle\rangle$$

This yields the following.

<div class="proposition" markdown="1">

<ins id="thm1">**Theorem 1**</ins> $$\lMod{A}$$ is a bicomplete category, and in particular the product of a family $$(M_i)$$ of $$A$$-modules is their direct product and the coproduct is their direct sum.

</div>

Direct products preserve kernels and direct sums preserve cokernels. ([\[Category Theory\] §Limits, ⁋Proposition 10](/en/math/category_theory/limits#prop10)) Moreover, we have the following proposition.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> Given two families $$(M_i)_{i\in I},(N_i)_{i\in I}$$ of $$A$$-modules and linear maps $$u_i: M_i \rightarrow N_i$$ between them, consider the induced maps $$\bigoplus u_i:\bigoplus M_i \rightarrow \bigoplus N_i$$ and $$\prod u_i: \prod M_i \rightarrow \prod N_i$$. Then the following holds:

1. If each $$u_i$$ is surjective, then $$\prod u_i$$ is surjective, and conversely.
2. If each $$u_i$$ is injective, then $$\bigoplus u_i$$ is injective, and conversely.

</div>

The proof follows by writing out $$\prod u_i$$ and $$\bigoplus u_i$$ coordinatewise. In particular, this proposition shows that direct products also preserve cokernels and direct sums also preserve kernels.

Earlier, we saw that for any $$M,N\in\lMod{A}$$, the set $$\Hom_{\lMod{A}}(M,N)$$ is an abelian group. It is easy to verify that this addition is compatible with composition, and that the category $$\lMod{A}$$ is an additive category with the zero module $$0$$ as zero object. ([\[Category Theory\] §Abelian Categories, ⁋Definition 1](/en/math/category_theory/abelian_categories#def1))

Moreover, $$\lMod{A}$$ is an abelian category. ([\[Category Theory\] §Abelian Categories, ⁋Definition 7](/en/math/category_theory/abelian_categories#def7)) To verify this, we check that every monomorphism $$u:M \rightarrow N$$ is the kernel of its cokernel $$N \rightarrow N/M$$, and every epimorphism $$v:M \rightarrow N$$ is the cokernel of its kernel $$M \rightarrow M/\ker v$$.

## Free Modules

In [§Modules, ⁋Example 5](/en/math/algebraic_structures/modules#ex5), we saw that a ring $$A$$ carries an $$A$$-module structure. Thus every $$A$$-module homomorphism $$u:A \rightarrow M$$ is uniquely determined by $$u(1)$$. Indeed, for any $$\alpha\in A$$,

$$u(\alpha)=u(\alpha\cdot 1)=\alpha\cdot u(1)$$

In other words, we have an isomorphism

$$\Hom_A(A, M)\cong\Hom_\Set(\ast, U(M))$$

where $$U:\lMod{A} \rightarrow \Set$$ is the forgetful functor. Thus $$A$$ may be called a representation of the forgetful functor $$U$$.

On the other hand, since we have verified that $$\lMod{R}$$ has coproducts $$\bigoplus$$, if the left adjoint $$F: \Set \rightarrow \lMod{A}$$ of $$U$$ exists, then the formula

$$F(X)=F\left(\coprod_{x\in X} \{x\}\right)\cong\bigoplus_{x\in X} F(\{x\})$$

must hold; the above representation shows that we should define $$F(X)=\bigoplus_{x\in X}Ax$$. Hence we have the following.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> For the forgetful functor $$U:\lMod{A} \rightarrow\Set$$ and the free functor $$F:\Set \rightarrow\lMod{A}$$ defined above, an adjunction $$F\dashv U$$ exists.

</div>

For any set $$X$$, $$A$$-modules isomorphic to $$F(X)$$ are called *free $$A$$-modules<sub>자유 $$A$$-가군</sub>*.

## Tensor Products of Modules

On the other hand, we can also define the tensor product of $$A$$-modules. We begin with the following definition.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> Let $$A$$ be a ring, $$M$$ a right $$A$$-module, and $$N$$ a left $$A$$-module. For any abelian group $$L$$, a map $$f:M\times N \rightarrow L$$ is called *$$A$$-balanced* if it is bilinear as a map of abelian groups and additionally satisfies

$$f(x\alpha, y)=f(x,\alpha y)$$

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

Then, by the universal property of the free abelian group, any function $$f:M\times N \rightarrow L$$ induces a group homomorphism $$\hat{f}:F(M\times N)\rightarrow L$$, and if $$f$$ is $$A$$-balanced, then $$\hat{f}$$ vanishes on $$M'$$ and therefore descends to a group homomorphism $$F(M\times N)/M' \rightarrow L$$.

The naturality of the isomorphism $$\Balan_A(M,N;L)\cong\Hom_\Ab(F(M\times N)/M',L)$$ requires additional verification, but it is a straightforward computation, which we omit.

</details>

The representation thus obtained is denoted by $$M\otimes_AN$$. Then the following holds.

<div class="proposition" markdown="1">

<ins id="thm6">**Theorem 6 ($$\otimes\dashv\Hom$$)**</ins> There is an adjunction

$$\Hom_\mathbb{Z}(M\otimes_A N, L)\cong\Hom_{\rMod{A}}(M,\Hom_\mathbb{Z}(N, L))\cong\Hom_{\lMod{A}}(N,\Hom_\mathbb{Z}(M, L))$$

</div>

Therefore $$\otimes$$ commutes with colimits and $$\Hom$$ commutes with limits. In particular, we obtain the following isomorphisms of abelian groups:

$$M\otimes_A\left(\bigoplus_{i\in I} N_i\right)\cong \bigoplus_{i\in I} M\otimes_AN_i,\qquad \left(\bigoplus_{i\in I} M_i\right)\otimes_A N\cong\bigoplus_{i\in I} M_i\otimes_AN\tag{1}$$

and

$$\Hom_{\lMod{A}}\left(M,\prod_{i\in I} N_i\right)\cong\prod_{i\in I}\Hom_{\lMod{A}}(M, N_i),\qquad \Hom_{\lMod{A}}\left(\bigoplus_{i\in I} M_i, N\right)\cong \prod_{i\in I}\Hom_{\lMod{A}}(M_i,N)\tag{2}$$

In the special case $$A=\mathbb{Z}$$, we recover the contents of [§Abelian Groups, §§Tensor Products](/en/math/algebraic_structures/abelian_groups#텐서곱); the isomorphisms above were omitted from that article for reasons of space.

## Tensor Products of Modules over Commutative Rings

The $$M\otimes_A N$$ defined above does not admit an $$A$$-module structure. If we attempt to define an $$A$$-action on $$M\otimes_A N$$ by setting

$$(x\alpha)\otimes_A y=x\otimes_A(\alpha y)$$

as $$\alpha(x\otimes_Ay)$$, then computing $$(\alpha\beta)(x\otimes_Ay)$$ yields

$$(x\alpha\beta)\otimes_A y,\qquad x\otimes_A(\alpha\beta y)$$

which are distinct elements. This is also why, in the definition of the tensor product, $$M$$ is taken as a right module and $$N$$ as a left module.

If $$M$$ has not only a right $$A$$-module structure but also a compatible left $$B$$-module structure, then $$M$$ is called a $$(B,A)$$-bimodule. That is, for any $$\alpha\in A$$, $$\beta\in B$$, and $$x\in M$$, the equation

$$(\alpha\cdot_A x)\cdot_B\beta=\alpha\cdot_A(x\cdot_B\beta)$$

must hold. Then one can verify that the formula

$$\beta(x\otimes_A y)=(\beta x)\otimes_Ay$$

defines a left $$B$$-module structure on $$M\otimes_AN$$.

We are primarily interested in the case where $$A$$ is a commutative ring. Then any left $$A$$-module is also a right $$A$$-module, and vice versa. Moreover, regarding any left $$A$$-module as a right $$A$$-module in this way, the two structures constitute an $$(A,A)$$-bimodule structure. Therefore there is a natural $$A$$-action on $$M\otimes_AN$$:

$$\alpha(x\otimes_Ay)=(\alpha x)\otimes_Ay=x\otimes_A(\alpha y)$$

This is likewise a representation of a suitable functor.

<div class="definition" markdown="1">

<ins id="def7">**Definition 7**</ins> Let $$A$$ be a commutative ring and let $$M$$, $$N$$, and $$L$$ be $$A$$-modules. A map $$f:M\times N \rightarrow L$$ is called *$$A$$-bilinear* if it is bilinear as a map of abelian groups and additionally satisfies

$$\alpha f(x,y)=f(\alpha x,y)=f(x,\alpha y)$$

</div>

Define the set $$\Bilin_A(M,N;L)$$ by

$$\Bilin_A(M,N;L)=\{\text{$A$-bilinear maps from $M\times N$ to $L$}\}$$

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8**</ins> The functor $$\Bilin_A(M,N;-):\lMod{A}\rightarrow\Set$$ is a representable functor, and its representation is the *$$A$$-module* $$M\otimes_AN$$ defined above.

</div>

On the other hand, if $$A$$ is an arbitrary ring, then $$\Hom_{\lMod{A}}(M,M')$$ does not admit an $$A$$-module structure; however, if $$A$$ is commutative, then $$\Hom_{\lMod{A}}(M,M')$$ does admit an $$A$$-module structure. That is, $$\Hom_A$$ is an internal $$\Hom$$, and thus we can refine the adjunction in [Theorem 6](#thm6) to prove the following.

<div class="proposition" markdown="1">

<ins id="thm9">**Theorem 9**</ins> For a commutative ring $$A$$, there is an adjunction

$$\Hom_A(M\otimes_AN, L)\cong\Hom_A(M,\Hom_A(N,L))\cong\Hom_A(N,\Hom_A(M,L))$$

</div>

In particular, the isomorphisms (1) and (2) above are isomorphisms of $$A$$-modules. Moreover, one can verify that $$(\lMod{A},\otimes_A,A)$$ is a symmetric monoidal category.
