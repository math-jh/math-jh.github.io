---
title: "Projective, Injective, and Flat Modules"
description: "This post covers the definitions and properties of projective, injective, and flat modules. It examines kernels, cokernels, direct products, and direct sums of modules through the adjunction between the Hom functor and the tensor product functor."
excerpt: "Definitions and equivalent conditions for projective, injective, and flat modules"

categories: [Math / Multilinear Algebra]
permalink: /en/math/multilinear_algebra/various_modules
sidebar: 
    nav: "multilinear_algebra-en"

date: 2024-08-21
weight: 2
translated_at: 2026-06-01T15:00:06+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-23T07:15:07+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
In [\[Algebraic Structures\]](/en/algebraic_structures/), we defined $A$-modules over an arbitrary ring $A$ and examined their basic properties. Now we further examine the properties of (left) $A$-modules.

## Kernel and Cokernel

For any $A$-linear map $u:M \rightarrow N$, that $u$ is injective is equivalent to $\ker u=0$, and that $u$ is surjective is equivalent to $\coker u=0$. On the other hand, the category $\lMod{A}$ is a bicomplete category, where the product of a family of $A$-modules was given by the direct product, and the coproduct by the direct sum. ([\[Algebraic Structures\] §Direct Products, Direct Sums, and Tensor Products of Modules, ⁋Theorem 1](/en/math/algebraic_structures/operations_of_modules#thm1){: data-lid="143lh" }) Therefore, by [\[Category Theory\] §Limits, ⁋Proposition 10](/en/math/category_theory/limits#prop10){: data-lid="0cs6t" }, the equation

$$\ker \prod u_i=\prod \ker u_i,\qquad \coker \bigoplus u_i=\bigoplus \coker u_i $$

holds, and rewriting [\[Algebraic Structures\] §Direct Products, Direct Sums, and Tensor Products of Modules, ⁋Proposition 2](/en/math/algebraic_structures/operations_of_modules#prop2){: data-lid="i5v2c" } through the above discussion, we also obtain the two equations

$$\ker \bigoplus u_i=\bigoplus \ker u_i,\qquad \coker \prod u_i=\prod \coker u_i$$

as well.

In a similar vein, we can revisit the properties of the $\Hom$ functor and the $\otimes$ functor, and here we use the adjoints of $\Hom$ and $\otimes$. ([\[Algebraic Structures\] §Direct Products, Direct Sums, and Tensor Products of Modules, ⁋Theorem 6](/en/math/algebraic_structures/operations_of_modules#thm6){: data-lid="h0wor" } and [\[Algebraic Structures\] §Direct Products, Direct Sums, and Tensor Products of Modules, ⁋Theorem 9](/en/math/algebraic_structures/operations_of_modules#thm9){: data-lid="yc3xx" })

## Direct Products and Direct Sums

To see how to use the above adjunction, we consider the most basic example. First, let us examine the relationship between $\Hom$, $\bigoplus$, and $\prod$. For this, we fix left $A$-modules $M,N$ and families of left $A$-modules $(M_i)_{i\in I}$, $(N_j)_{j\in J}$. Then, since $\Hom$ is a right adjoint, it preserves limits. ([\[Category Theory\] §Adjoint Functors, ⁋Theorem 9](/en/math/category_theory/adjoints#thm9){: data-lid="p4a1u" }) Therefore, by [\[Category Theory\] §Limits, ⁋Theorem 9](/en/math/category_theory/limits#thm9){: data-lid="ejjiz" }, we obtain the isomorphisms of abelian groups

$$\Hom_{\lMod{A}}\left(M, \prod_{j\in J} N_j \right)\cong\prod_{j\in J} \Hom_{\lMod{A}}(M, N_j),\qquad \Hom_{\lMod{A}}\left(\bigoplus_{i\in I} M_i, N\right)\cong\prod_{i\in I}\Hom_{\lMod{A}}(M_i, N)$$

Applying [\[Category Theory\] §Limits, ⁋Proposition 10](/en/math/category_theory/limits#prop10){: data-lid="8s0di" } to this again yields the following equation:

$$\Hom_{\lMod{A}}\left(\bigoplus_{i\in I} M_i, \prod_{j\in J} N_j\right)\cong\prod_{(i,j)\in I\times J}\Hom_{\lMod{A}}(M_i, N_j)\tag{1}$$

Similarly, let us examine the relationship between $\otimes$ and $\bigoplus$. This time, we consider a right $A$-module $M$, a family of right $A$-modules $(M_i)_{i\in I}$, a left $A$-module $N$, and a family of left $A$-modules $(N_j)_{j\in J}$. Then, since $\otimes$ preserves colimits, we obtain the abelian group isomorphisms

$$M\otimes_A \left(\bigoplus_{j\in J}N_j\right)\cong\bigoplus_{j\in J} (M\otimes_AN_j),\qquad \left(\bigoplus_{i\in I} M_i\right)\otimes_A N\cong \bigoplus_{i\in I} (M_i\otimes_AN)$$

and combining these, we obtain

$$\left(\bigoplus_{i\in I} M_i\right)\otimes_A\left(\bigoplus_{j\in J} N_j\right)\cong\bigoplus_{(i,j)\in I\times J}M_i\otimes_AN_j$$

If $A$ were a commutative ring, instead of [\[Algebraic Structures\] §Direct Products, Direct Sums, and Tensor Products of Modules, ⁋Theorem 6](/en/math/algebraic_structures/operations_of_modules#thm6){: data-lid="93303" }, we could use [\[Algebraic Structures\] §Direct Products, Direct Sums, and Tensor Products of Modules, ⁋Theorem 9](/en/math/algebraic_structures/operations_of_modules#thm9){: data-lid="rb8jh" } to make the above isomorphisms into isomorphisms between $A$-modules.

## Projective and Injective Modules

Now let an arbitrary $A$-linear map $u:M \rightarrow M'$ and an $A$-module $N$ be given. Then, for the abelian group homomorphism

$$\Hom_{\lMod{A}}(u,N):\Hom_{\lMod{A}}(M', N) \rightarrow \Hom_{\lMod{A}}(M,N)$$

since $\Hom$ is a right adjoint,

$$\ker(\Hom_{\lMod{A}}(u,N))\cong\Hom_{\lMod{A}}(\coker u, N)\tag{2}$$

holds. Similarly, for the abelian group homomorphism

$$\Hom_{\lMod{A}}(N, u):\Hom_{\lMod{A}}(N, M) \rightarrow\Hom_{\lMod{A}}(N, M')$$

we have

$$\ker(\Hom_{\lMod{A}}(N, u))\cong\Hom_{\lMod{A}}(N, \ ker u)\tag{3}$$

holds. Therefore the following holds.

::: Proposition 1
Let an $A$-linear map $u:M \rightarrow M'$ be given.

1. $u$ is injective if and only if for any $A$-module $N$, $\Hom(N, u)$ is injective.
2. $u$ is surjective if and only if for any $A$-module $N$, $\Hom(u, N)$ is injective.
:::

However, in general, even if $u$ is surjective, $\Hom(u, N)$ need not be surjective, and even if $u$ is injective, $\Hom(N, u)$ need not be surjective.

On the other hand, since $\lMod{A}$ is an abelian category, the isomorphism of (2) is essentially the statement that when the following exact sequence

$$M_1 \rightarrow M_2 \rightarrow M_3 \rightarrow 0$$

is given, the following sequence obtained by applying the (contravariant) additive functor $\Hom_{\lMod{A}}(-, N):\lMod{A} \rightarrow\lMod{\mathbb{Z}}$ to it,

$$0 \rightarrow \Hom_\lMod{A}(M_3, N) \rightarrow \Hom_\lMod{A}(M_2, N)\rightarrow\Hom_\lMod{A}(M_1,N)$$

is exact. Similarly, the isomorphism of (3) is essentially the statement that when the following exact sequence

$$0 \rightarrow M_1 \rightarrow M_2 \rightarrow M_3$$

is given, the following sequence obtained by applying the additive functor $\Hom_\lMod{A}(N,-):\lMod{A} \rightarrow \lMod{\mathbb{Z}}$ to it,

$$0 \rightarrow \Hom_\lMod{A}(N, M_1)\rightarrow\Hom_\lMod{A}(N, M_2) \rightarrow\Hom_\lMod{A}(N, M_3)$$

is exact. That is, the following holds.

::: Proposition 2
For any $N\in\lMod{A}$, $\Hom_\lMod{A}(-,N)$ and $\Hom_\lMod{A}(N,-)$ are left exact functors.
:::

However, in general $\Hom_\lMod{A}(-,N)$ and $\Hom_{\lMod{A}}(N,-)$ need not be right exact. We define $A$-modules satisfying these conditions as follows.

::: Definition 3
We define the following.

1. If $\Hom(-, I)$ is right exact, we call $I$ an *injective module*.
2. If $\Hom(P, -)$ is right exact, we call $P$ a *projective module*.
:::

Then from (1), we know that a direct product of modules is injective if and only if each component is injective, and that a direct sum of modules is projective if and only if each component is projective. In particular, from the fact that under the natural isomorphism $\Hom_{\lMod{A}}(A, M)\cong M$, the following homomorphism

$$\Hom(A, u):\Hom_{\lMod{A}}(A, M) \rightarrow \Hom_{\lMod{A}}(A, M')$$

equals $u$, we know that $A$ itself is projective, and therefore any free module is a projective module.

::: Proposition 4
A left $A$-module $P$ is projective if and only if $P$ is a direct summand of a free $A$-module.
:::
::: Proof
That any direct summand of a free module is projective is clear from the argument above. Thus assume that $P$ is projective. By [§Bases, ⁋Proposition 2](/en/math/multilinear_algebra/basis_of_free_modules#prop2){: data-lid="e0rww" } we can choose a free $A$-module $F$ and a surjection $p:F \rightarrow P$. Now, $P$ being projective means that the following map

$$\Hom_{\lMod{A}}(P, p):\Hom_{\lMod{A}}(P,F) \rightarrow \Hom_{\lMod{A}}(P,P)$$

is surjective, so there exists $i\in \Hom_{\lMod{A}}(P,F)$ such that

$$\id_P=\Hom_{\lMod{A}}(P,p)(i)=p\circ i$$

holds. From this equation, since $i$ is injective, we can identify $P$ with $\im i$, and then verify that $F\cong\ker p\oplus\im i$.
:::

## Flat Modules

This time, let a right $A$-module $M$ and, between left $A$-modules, an $A$-linear map $v:N \rightarrow N'$ be given. Then the following abelian group homomorphism

$$M\otimes_A v:M\otimes_AN \rightarrow M\otimes_AN'$$

exists. Then, since $\otimes$ is a left adjoint, it preserves colimits, and therefore the following isomorphism between abelian groups

$$\coker(M\otimes_Av)\cong M\otimes_A(\coker v)$$

exists. Similarly, between right $A$-modules, for an $A$-linear map $u:M \rightarrow M'$ and a fixed left $A$-module $N$, the following isomorphism

$$\coker(u\otimes_AN)\cong (\coker u)\otimes_A N$$

exists.

::: Proposition 5
The following hold.

1. Between right $A$-modules, a linear map $u:M \rightarrow M'$ is surjective if and only if for every left $A$-module $N$, $u\otimes_A N$ is surjective.
2. Between left $A$-modules, a linear map $v:N \rightarrow N'$ is surjective if and only if for every right $A$-module $M$, $M\otimes_A v$ is surjective.
:::

Then, just as before, the above property can be written as saying that when an exact sequence of right $A$-modules

$$M_1 \rightarrow M_2 \rightarrow M_3 \rightarrow 0$$

is given, for any left $A$-module $N$,

$$M_1\otimes_AN \rightarrow M_2\otimes_AN \rightarrow M_3\otimes_AN \rightarrow 0$$

is also exact. Similarly, when an exact sequence of left $A$-modules

$$N_1 \rightarrow N_2 \rightarrow N_3 \rightarrow 0$$

is given, for any right $A$-module $M$,

$$M\otimes_AN_1 \rightarrow M\otimes_AN_2 \rightarrow M\otimes_AN_3 \rightarrow 0$$

also becomes exact. That is, the following holds.

::: Proposition 6
For any $M\in\rMod{A}$ and $N\in \lMod{A}$, $-\otimes_AN$ and $M\otimes_A-$ are each right exact functors.
:::

Then, in a similar vein to [Definition 3](#def3){: data-lid="fxj4j" }, we can define the following.

::: Definition 7
A left $A$-module $N$ is called a *flat module* if for any right $A$-modules and any injective $A$-linear map $u:M \rightarrow M'$ between them, $u\otimes_A N$ is injective. Similarly, one can define a flat right $A$-module.
:::

Any free module is flat. Also, it is obvious that a direct sum of modules is flat if and only if each summand is flat. Therefore, by [Proposition 4](#prop4){: data-lid="twtgh" }, a projective module is always flat. However, the converse does not always hold.

---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.
