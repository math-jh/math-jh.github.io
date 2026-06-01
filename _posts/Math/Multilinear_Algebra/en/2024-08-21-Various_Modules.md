---
title: "Projective, Injective, and Flat Modules"
description: "This post covers the definitions and properties of projective, injective, and flat modules. It examines kernels, cokernels, direct products, and direct sums of modules through the adjunction between the Hom functor and the tensor product functor."
excerpt: "Definitions and equivalent conditions for projective, injective, and flat modules"

categories: [Math / Multilinear Algebra]
permalink: /en/math/multilinear_algebra/various_modules
header:
    overlay_image: /assets/images/Math/Multilinear_Algebra/Various_Modules.png
    overlay_filter: 0.5
sidebar: 
    nav: "multilinear_algebra-en"

date: 2024-08-21
last_modified_at: 2024-09-23
weight: 2
translated_at: 2026-06-01T15:00:06+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-01T15:00:06+00:00
---
In [\[Algebraic Structures\]](/en/algebraic_structures/) we defined $$A$$-modules over an arbitrary ring $$A$$ and examined their basic properties. In this post we study further properties of (left) $$A$$-modules.

## Kernel and Cokernel

For any $$A$$-linear map $$u:M \rightarrow N$$, injectivity of $$u$$ is equivalent to $$\ker u=0$$, and surjectivity of $$u$$ is equivalent to $$\coker u=0$$. On the other hand, the category $$\lMod{A}$$ is bicomplete; the product of a family of $$A$$-modules is the direct product, and the coproduct is the direct sum. ([\[Algebraic Structures\] §Direct Products, Direct Sums, and Tensor Products of Modules, ⁋Theorem 1](/en/math/algebraic_structures/operations_of_modules#thm1)) Therefore, by [\[Category Theory\] §Limits, ⁋Proposition 10](/en/math/category_theory/limits#prop10),

$$\ker \prod u_i=\prod \ker u_i,\qquad \coker \bigoplus u_i=\bigoplus \coker u_i $$

and applying the same reasoning to rewrite [\[Algebraic Structures\] §Direct Products, Direct Sums, and Tensor Products of Modules, ⁋Proposition 2](/en/math/algebraic_structures/operations_of_modules#prop2) yields the two further identities

$$\ker \bigoplus u_i=\bigoplus \ker u_i,\qquad \coker \prod u_i=\prod \coker u_i$$

as well.

In a similar vein we revisit properties of the $$\Hom$$ and $$\otimes$$ functors, making use of the adjunction between them. ([\[Algebraic Structures\] §Direct Products, Direct Sums, and Tensor Products of Modules, ⁋Theorem 6](/en/math/algebraic_structures/operations_of_modules#thm6) and [\[Algebraic Structures\] §Direct Products, Direct Sums, and Tensor Products of Modules, ⁋Theorem 9](/en/math/algebraic_structures/operations_of_modules#thm9))

## Direct Products and Direct Sums

To see how the above adjunction is used, we begin with the most basic example. First, consider the relationship between $$\Hom$$, $$\bigoplus$$, and $$\prod$$. Fix left $$A$$-modules $$M,N$$ and families of left $$A$$-modules $$(M_i)_{i\in I}$$, $$(N_j)_{j\in J}$$. Since $$\Hom$$ is a right adjoint, it preserves limits. ([\[Category Theory\] §Adjoint Functors, ⁋Theorem 9](/en/math/category_theory/adjoints#thm9)) Hence, by [\[Category Theory\] §Limits, ⁋Proposition 10](/en/math/category_theory/limits#prop10), we obtain isomorphisms of abelian groups

$$\Hom_{\lMod{A}}\left(M, \prod_{j\in J} N_j \right)\cong\prod_{j\in J} \Hom_{\lMod{A}}(M, N_j),\qquad \Hom_{\lMod{A}}\left(\bigoplus_{i\in I} M_i, N\right)\cong\prod_{i\in I}\Hom_{\lMod{A}}(M_i, N)$$

Applying [\[Category Theory\] §Limits, ⁋Proposition 10](/en/math/category_theory/limits#prop10) once more yields

$$\Hom_{\lMod{A}}\left(\bigoplus_{i\in I} M_i, \prod_{j\in J} N_j\right)\cong\prod_{(i,j)\in I\times J}\Hom_{\lMod{A}}(M_i, N_j)\tag{1}$$

Similarly, consider the relationship between $$\otimes$$ and $$\bigoplus$$. This time we take a right $$A$$-module $$M$$, a family of right $$A$$-modules $$(M_i)_{i\in I}$$, a left $$A$$-module $$N$$, and a family of left $$A$$-modules $$(N_j)_{j\in J}$$. Since $$\otimes$$ preserves colimits, we have abelian group isomorphisms

$$M\otimes_A \left(\bigoplus_{j\in J}N_j\right)\cong\bigoplus_{j\in J} (M\otimes_AN_j),\qquad \left(\bigoplus_{i\in I} M_i\right)\otimes_A N\cong \bigoplus_{i\in I} M_i\otimes_AN)$$

and combining these gives

$$\left(\bigoplus_{i\in I} M_i\right)\otimes_A\left(\bigoplus_{j\in J} N_j\right)\cong\bigoplus_{(i,j)\in I\times J}M_i\otimes_AN_j$$

If $$A$$ were a commutative ring, we could use [\[Algebraic Structures\] §Direct Products, Direct Sums, and Tensor Products of Modules, ⁋Theorem 9](/en/math/algebraic_structures/operations_of_modules#thm9) in place of [\[Algebraic Structures\] §Direct Products, Direct Sums, and Tensor Products of Modules, ⁋Theorem 6](/en/math/algebraic_structures/operations_of_modules#thm6) to make the above isomorphisms into isomorphisms of $$A$$-modules.

## Projective and Injective Modules

Now let an arbitrary $$A$$-linear map $$u:M \rightarrow M'$$ and an $$A$$-module $$N$$ be given. Then we have the abelian group homomorphism

$$\Hom_{\lMod{A}}(u,N):\Hom_{\lMod{A}}(M', N) \rightarrow \Hom_{\lMod{A}}(M,N)$$

and since $$\Hom$$ is a right adjoint,

$$\ker(\Hom_{\lMod{A}}(u,N))\cong\Hom_{\lMod{A}}(\coker u, N)\tag{2}$$

holds. Likewise, for the abelian group homomorphism

$$\Hom_{\lMod{A}}(N, u):\Hom_{\lMod{A}}(M, N) \rightarrow\Hom_{\lMod{A}}(M', N)$$

we have

$$\ker(\Hom_{\lMod{A}}(N, u))\cong\Hom_{\lMod{A}}(N, \ker u)\tag{3}$$

Therefore the following holds.

<div class="proposition" markdown="1">

<ins id="prop1">**Proposition 1**</ins> Let an $$A$$-linear map $$u:M \rightarrow M'$$ be given.

1. $$u$$ is injective if and only if $$\Hom(N, u)$$ is injective for every $$A$$-module $$N$$.
2. $$u$$ is surjective if and only if $$\Hom(u, N)$$ is injective for every $$A$$-module $$N$$.

</div>

However, in general, even if $$u$$ is surjective, $$\Hom(u, N)$$ need not be surjective; and even if $$u$$ is injective, $$\Hom(N, u)$$ need not be surjective.

On the other hand, since $$\lMod{A}$$ is an abelian category, the isomorphism (2) is essentially the statement that when a short exact sequence

$$M_1 \rightarrow M_2 \rightarrow M_3 \rightarrow 0$$

is given, the sequence obtained by applying the (contravariant) additive functor $$\Hom_{\lMod{A}}(-, N):\lMod{A} \rightarrow\lMod{\mathbb{Z}}$$,

$$0 \rightarrow \Hom_\lMod{A}(M_3, N) \rightarrow \Hom_\lMod{A}(M_2, N)\rightarrow\Hom_\lMod{A}(M_1,A)$$

is exact. Similarly, the isomorphism (3) says that when a short exact sequence

$$0 \rightarrow M_1 \rightarrow M_2 \rightarrow M_3$$

is given, the sequence obtained by applying the additive functor $$\Hom_\lMod{A}(N,-):\lMod{A} \rightarrow \lMod{\mathbb{Z}}$$,

$$0 \rightarrow \Hom_\lMod{A}(N, M_1)\rightarrow\Hom_\lMod{A}(N, M_2) \rightarrow\Hom_\lMod{A}(N, M_3)$$

is exact. In other words, the following holds.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> For any $$N\in\lMod{A}$$, the functors $$\Hom_\lMod{A}(-,N)$$ and $$\Hom_\lMod{A}(N,-)$$ are left exact.

</div>

However, in general $$\Hom_\lMod{A}(-,N)$$ and $$\Hom_{\lMod{A}}(N,-)$$ need not be right exact. We define $$A$$-modules satisfying these conditions as follows.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> We define the following.

1. If $$\Hom(-, I)$$ is right exact, we call $$I$$ an *injective module*.
2. If $$\Hom(P, -)$$ is right exact, we call $$P$$ a *projective module*.

</div>

Then from (1) we know that a direct product of modules is injective if and only if each factor is injective, and a direct sum of modules is projective if and only if each direct summand is projective. In particular, from the fact that the homomorphism

$$\Hom(A, u):\Hom_{\lMod{A}}(A, M) \rightarrow \Hom_{\lMod{A}}(A, M')$$

is an isomorphism, we see that $$A$$ itself is projective, and hence any free module is a projective module.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> A left $$A$$-module is projective if and only if it is a direct summand of a free $$A$$-module.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

That any direct summand of a free module is projective is clear from the argument above. Thus assume that $$P$$ is projective. By [§Bases, ⁋Proposition 2](/en/math/multilinear_algebra/basis_of_free_modules#prop2) we can choose a free $$A$$-module $$F$$ and a surjection $$p:F \rightarrow P$$. Now $$P$$ being projective means that the map

$$\Hom_{\lMod{A}}(P, p):\Hom_{\lMod{A}}(P,F) \rightarrow \Hom_{\lMod{A}}(P,P)$$

is surjective, so there exists $$i\in \Hom_{\lMod{A}}(P,F)$$ such that

$$\id_P=\Hom_{\lMod{A}}(P,p)(i)=p\circ i$$

This equation shows that $$i$$ is injective, so we may identify $$P$$ with $$\im i$$, and then one verifies that $$F\cong\ker p\oplus\im i$$.

</details>

## Flat Modules

Now let a right $$A$$-module $$M$$ and an $$A$$-linear map $$v:N \rightarrow N'$$ between left $$A$$-modules be given. Then there is the abelian group homomorphism

$$M\otimes_A v:M\otimes_AN \rightarrow M\otimes_AN'$$

Since $$\otimes$$ is a left adjoint, it preserves colimits, and therefore there is an isomorphism of abelian groups

$$\coker(M\otimes_Av)\cong M\otimes_A(\coker v)$$

Likewise, for an $$A$$-linear map $$u:M \rightarrow M'$$ between right $$A$$-modules and a fixed left $$A$$-module $$N$$, there is an isomorphism

$$\coker(u\otimes_AN)\cong (\coker u)\otimes_A N$$

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> The following hold.

1. A linear map $$u:M \rightarrow M'$$ between right $$A$$-modules is surjective if and only if $$u\otimes_A N$$ is surjective for every left $$A$$-module $$N$$.
2. A linear map $$v:N \rightarrow N'$$ between left $$A$$-modules is surjective if and only if $$M\otimes_A v$$ is surjective for every right $$A$$-module $$M$$.

</div>

Then, just as before, the above property means that when an exact sequence of right $$A$$-modules

$$M_1 \rightarrow M_2 \rightarrow M_3 \rightarrow 0$$

is given, for any left $$A$$-module $$N$$ the sequence

$$M_1\otimes_AN \rightarrow M_2\otimes_AN \rightarrow M_3\otimes_AN \rightarrow 0$$

is also exact. Likewise, when an exact sequence of left $$A$$-modules

$$N_1 \rightarrow N_2 \rightarrow N_3 \rightarrow 0$$

is given, for any right $$A$$-module $$M$$ the sequence

$$M\otimes_AN_1 \rightarrow M\otimes_AN_2 \rightarrow M\otimes_AN_3 \rightarrow 0$$

is also exact. In other words, the following holds.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> For any $$M\in\rMod{A}$$ and $$N\in \lMod{A}$$, the functors $$-\otimes_AN$$ and $$M\otimes_A-$$ are right exact.

</div>

Then, in the same spirit as [Definition 3](#def3), we can make the following definition.

<div class="definition" markdown="1">

<ins id="def7">**Definition 7**</ins> A left $$A$$-module $$N$$ is called a *flat module* if for every injective $$A$$-linear map $$u:M \rightarrow M'$$ between right $$A$$-modules, $$u\otimes_A N$$ is injective. Similarly one defines flat right $$A$$-modules.

</div>

Any free module is flat. Also, it is obvious that a direct sum of modules is flat if and only if each summand is flat. Therefore, by [Proposition 4](#prop4), every projective module is flat. However, the converse does not hold in general.
