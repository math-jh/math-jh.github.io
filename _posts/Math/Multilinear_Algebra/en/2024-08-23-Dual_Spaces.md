---
title: "Dual Spaces"
description: "This post covers the definition of dual modules for modules over a given ring, the Kronecker pairing, and the orthogonal relationship between submodules."
excerpt: "Hom of modules, dual modules, and bidual maps"

categories: [Math / Multilinear Algebra]
permalink: /en/math/multilinear_algebra/dual_spaces
sidebar: 
    nav: "multilinear_algebra-en"

date: 2024-08-23
weight: 4
translated_at: 2026-08-19T19:45:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-23T11:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
## Module $\Hom_\lMod{A}(M,N)$

Fix arbitrary left $A$-modules $M,N$. Then $\Hom_\lMod{A}(M,N)$ is an abelian group, but in general it does not have the structure of a left $A$-module. That is, in general, for arbitrary $\alpha\in A$ and $u\in\Hom_\lMod{A}(M,N)$, the function defined by the formula

$$x\mapsto \alpha u(x)$$

denoted $\alpha u: M \rightarrow N$, is not an $A$-linear map. This can be seen from the following computation for arbitrary $\beta\in A$ and $x\in M$:

$$(\alpha u)(\beta x)=\alpha u(\beta x)=\alpha \beta u(x)\neq \beta\alpha u(x)=\beta\cdot ((\alpha u)(x))$$

However, also from this equation, we see that if $\alpha$ belongs to the center of $A$, then $\alpha u$ is an $A$-linear map. That is, for the center of $A$, $Z(A)$, $\Hom_\lMod{A}(M,N)$ is a left $Z(A)$-module. By a similar argument, for arbitrary right $A$-modules $M,N$, we see that $\Hom_\rMod{A}(M,N)$ is a right $Z(A)$-module.

On the other hand, consider the case where left $A$-modules $M,N$ are given, and in particular $N$ carries a compatible right $B$-module structure, that is, the case where $N$ is an $(A,B)$-bimodule. Then for arbitrary $\beta\in B$ and $u\in\Hom_\lMod{A}(M,N)$, that the function defined by the formula

$$x\mapsto u(x)\beta$$

denoted $u\beta: M \rightarrow N$, is an $A$-linear map can be seen from the following computation:

$$(u\beta)(\alpha x)=u(\alpha x)\beta=\alpha u(x)\beta=\alpha((u\beta)(x))$$

A similar logic holds for a right $A$-module $M$ and a $(B,A)$-bimodule $N$.

## Definition of the Dual Space

Any ring $A$ has a natural $(A,A)$-bimodule structure via the multiplication defined on it. Therefore, by the preceding argument, $\Hom_{\lMod{A}}(M, A)$ can be regarded as a right $A$-module.

::: Definition 1
The right $A$-module $\Hom_{\lMod{A}}(M, A)$ defined above is called the *dual module* of $M$, and is denoted by $M^\ast$.
:::

Similarly, if a right $A$-module $M$ is given, $\Hom_{\rMod{A}}(M,A)$ can be viewed as a left $A$-module, and we call this the dual module of $M$. In particular, in the case where $M=A$, to avoid confusion, if we denote $A$ viewed as a left $A$-module by $A_l$, and viewed as a right $A$-module by $A_r$, we can verify the two equations $A_l^\ast=A_r$ and $A_r^\ast=A_l$.

By definition, if arbitrary $x\in M$ and $\xi\in M^\ast$ are given, this pair specifies $\xi(x)\in A$. We write this as $\langle x, \xi\rangle$, and call this notation the *Kronecker pairing*.

::: Definition 2
For an arbitrary $A$-module $M$ and its dual $M^\ast$, we say that $x\in M$ and $\xi\in M^\ast$ are *orthogonal* if $\langle x,\xi\rangle=0$.
:::

If every pair of elements from two subsets of $M$ and $M^\ast$ is orthogonal, we say that the two are orthogonal. Meanwhile, fix an arbitrary $x\in M$, and suppose that $\xi,\xi_1,\xi_2\in M^\ast$ orthogonal to $x$ and $\alpha\in A$ are given. Then, since

$$\langle x, \xi_1+\xi_2\rangle=\langle x, \xi_1\rangle+\langle x,\xi_2\rangle=0,\qquad \langle x,\xi\cdot\alpha\rangle=\langle x,\xi\rangle\alpha=0$$

for a fixed subset of $M$, denoted $S$, collecting the elements of $M^\ast$ orthogonal to the elements of $S$ forms a submodule of $M^\ast$.

::: Definition 3
The submodule of $M^\ast$ defined above is called the submodule orthogonal to $S$, and is denoted by $S^\perp$.
:::

Similarly, for an arbitrary subset $T\subseteq M^\ast$, one can define $T^\perp$ by the formula

$$T^\perp=\{x\in M\mid \langle x, \xi\rangle=0\text{ for all $\xi\in T$}\}$$

where one should note that $T^\perp$ is defined not as a submodule of $M^{\ast\ast}$, but as a submodule of $M$.

## Transpose of a Linear Map

Suppose an arbitrary $A$-linear map $u:M \rightarrow N$ is given. Then the abelian group homomorphism from [\[Algebraic Structures\] §Modules, ⁋Proposition 8](/en/math/algebraic_structures/modules#prop8){: data-lid="6v0z6" },

$$\Hom(u,A):\Hom_{\lMod{A}}(N,A)\rightarrow\Hom_{\lMod{A}}(M,A)$$

is compatible with the right action of $A$. That is, $\Hom(u,A)$ is a right $A$-module homomorphism.

::: Definition 4
Between left $A$-modules, for an $A$-linear map $u:M \rightarrow N$, the right $A$-module homomorphism defined above is called the *transpose* of $u$, and is denoted $u^t$.
:::

The map $u^t$ is determined by its value at arbitrary $\xi\in N^\ast$, $u^t(\xi)\in M^\ast$, and in turn $u^t(\xi)\in M^\ast$ is determined by its value at arbitrary $x\in M$,

$$u^t(\xi)(x)=\langle x, u^t(\xi)\rangle$$

On the other hand, by the definition of $u^t=\Hom(u,A)$ we have $u^t(\xi)=\xi\circ u$. That is, the above equation can be written as

$$\langle u(x),\xi\rangle=\langle x, u^t\xi\rangle$$

and conversely, if this equation holds for all $x\in M$ and all $\xi\in N^\ast$, then $u^t$ is uniquely determined.

Also, for two $A$-linear maps $u,v:M \rightarrow N$ and arbitrary $\xi\in N^\ast$, $x\in M$, from the fact that $\xi((u+v)(x))=\xi(u(x))+\xi(v(x))$, the functoriality of $\Hom(-,A)$, and [\[Algebraic Structures\] §Modules, ⁋Proposition 8](/en/math/algebraic_structures/modules#prop8){: data-lid="uvnpc" }, we obtain the following proposition.

::: Proposition 5
The following hold.

1. For two $A$-linear maps $u,v:M \rightarrow N$, we have $(u+v)^t=u^t+v^t$.
2. For two $A$-linear maps $u:M \rightarrow N$ and $v:N \rightarrow L$, we have $(v\circ u)^t=u^t\circ v^t$.
3. For any $M$, we have $(\id_M)^t=\id_{M^\ast}$.
4. For any $A$-linear isomorphism $u:M \rightarrow N$, we have $(u^{-1})^t=(u^t)^{-1}$.
:::

## Dual Basis

Suppose that the $A$-module $M$ has a basis $(e_i)_{i\in I}$. ([§Bases, ⁋Definition 1](/en/math/multilinear_algebra/basis_of_free_modules#def1){: data-lid="xtbc7" }) That is, there exists an isomorphism

$$\varepsilon: A^{\oplus I} \rightarrow M$$

Then, taking the dual of this isomorphism, we obtain an isomorphism of right $A$-modules

$$\varepsilon^t: M^\ast \rightarrow (A_l^{\oplus I})^\ast=\Hom_{\lMod{A}}(A_l^{\oplus I}, A_l)\cong \prod_{i\in I}\left(\Hom_\lMod{A}(A_l,A_l)\right)\cong \prod_{i\in I} A_r$$

Now, among the elements of the right-hand side, consider the elements whose $i$-th component is $1$ and whose other components are $0$, and write their preimage under $\varepsilon^t$ as $e_i^\ast$. Then we know that

$$\langle e_i, e_j^\ast\rangle=\delta_{ij}$$

holds. The collection of these elements is linearly independent, but if $I$ is an infinite set, this does not become a basis of $M^\ast$. However, if $I$ is a finite set, then $\prod_{i\in I} A\cong \bigoplus_{i\in I}A$, so these elements do form a basis.

::: Definition 6
Fix an arbitrary free module $M$ and a basis $(e_i)_{i\in I}$. Then the family of elements of $M^\ast$ defined above, $(e_i^\ast)_{i\in I}$, is called the *coordinate form* corresponding to $(e_i)_{i\in I}$.  
If $M$ is a finitely generated free module, then this family $(e_i^\ast)_{i\in I}$ is a basis of $M^\ast$, and is called the *dual basis* of $(e_i)$.
:::

## Double Dual Space

For any left $A$-module $M$, the dual of $M$, $M^\ast$, is a right $A$-module, and the dual of $M^\ast$, $M^{\ast\ast}$, is again a left $A$-module. On the other hand, for arbitrary $x\in M$, one can check that the function defined by the following expression

$$\langle x,-\rangle: M^\ast \rightarrow A$$

is a right $A$-module homomorphism. That is, the above formula defines a function from $M$ to $M^{\ast\ast}$, and one can also check that this function is a linear map. In general, this function is neither injective nor surjective.

::: Definition 7
If the above function $M \rightarrow M^{\ast\ast}$ is bijective, we call $M$ *reflexive*.
:::

Then the following holds.

::: Proposition 8
For any free module $M$, the map $M \rightarrow M^{\ast\ast}$ defined above is injective. If, in addition, $M$ is finitely generated, then this map is bijective.
:::

---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.
