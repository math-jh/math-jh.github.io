---
title: "Dual Spaces"
description: "This post covers the definition of dual modules over a commutative ring, the Kronecker pairing, and the orthogonal relationship between submodules."
excerpt: "Hom of modules, dual modules, and bidual maps"

categories: [Math / Multilinear Algebra]
permalink: /en/math/multilinear_algebra/dual_spaces
sidebar: 
    nav: "multilinear_algebra-en"

date: 2024-08-23
weight: 4
translated_at: 2026-08-16T07:17:05+00:00
translation_source: kimi-cli
---
## Module $\Hom_\lMod{A}(M,N)$

Fix arbitrary left $A$-modules $M$ and $N$. Then $\Hom_\lMod{A}(M,N)$ is an abelian group, but in general it does not carry the structure of a left $A$-module. That is, for arbitrary $\alpha\in A$ and $u\in\Hom_\lMod{A}(M,N)$, the function $\alpha u: M \rightarrow N$ defined by the formula

$$x\mapsto \alpha u(x)$$

is not an $A$-linear map. This can be checked from the following equation for arbitrary $\beta\in A$ and $x\in M$:

$$(\alpha u)(\beta x)=\alpha u(\beta x)=\alpha \beta u(x)\neq \beta\alpha u(x)=\beta\cdot ((\alpha u)(x)).$$

However, from this very equation we also see that if $\alpha$ lies in the center of $A$, then $\alpha u$ becomes an $A$-linear map. Thus, for the center $Z(A)$ of $A$, the abelian group $\Hom_\lMod{A}(M,N)$ is a left $Z(A)$-module. By the same reasoning, for arbitrary right $A$-modules $M$ and $N$, the abelian group $\Hom_\rMod{A}(M,N)$ is a right $Z(A)$-module.

On the other hand, suppose left $A$-modules $M$ and $N$ are given, and in particular $N$ carries a right $B$-module structure compatible with the given one, i.e. $N$ is an $(A,B)$-bimodule. Then for arbitrary $\beta\in B$ and $u\in\Hom_\lMod{A}(M,N)$, the function $u\beta: M \rightarrow N$ defined by the formula

$$x\mapsto u(x)\beta$$

is an $A$-linear map, as can be checked from the following equation:

$$(u\beta)(\alpha x)=u(\alpha x)\beta=\alpha u(x)\beta=\alpha((u\beta)(x)).$$

The same reasoning also holds for a right $A$-module $M$ and a $(B,A)$-bimodule $N$.

## Definition of Dual Spaces

Any ring $A$ carries a natural $(A,A)$-bimodule structure via the multiplication defined on it. Therefore, by the preceding argument we may regard $\Hom_{\lMod{A}}(M, A)$ as a right $A$-module.

::: Definition 1
The right $A$-module $\Hom_{\lMod{A}}(M, A)$ defined above is called the *dual module* of $M$, and is denoted $M^\ast$.
:::

Similarly, if a right $A$-module $M$ is given, then $\Hom_{\rMod{A}}(M,A)$ can be viewed as a left $A$-module, and we call this the dual module of $M$ as well. In the special case $M=A$, to avoid confusion we write $A_l$ for $A$ regarded as a left $A$-module and $A_r$ for $A$ regarded as a right $A$-module; then one can verify the two identities $A_l^\ast=A_r$ and $A_r^\ast=A_l$.

By definition, for arbitrary $x\in M$ and $\xi\in M^\ast$, the pair $(x,\xi)$ specifies an element $\xi(x)\in A$. We write this as $\langle x, \xi\rangle$, and call this notation the *Kronecker pairing*.

::: Definition 2
For any $A$-module $M$ and its dual $M^\ast$, we say that $x\in M$ and $\xi\in M^\ast$ are *orthogonal* if $\langle x,\xi\rangle=0$.
:::

If every pair of elements from two subsets of $M$ and $M^\ast$ is orthogonal, we say that the two subsets are orthogonal. Now fix an arbitrary element $x\in M$, and let $\xi,\xi_1,\xi_2\in M^\ast$ and $\alpha\in A$ be given. Then

$$\langle x, \xi_1+\xi_2\rangle=\langle x, \xi_1\rangle+\langle x,\xi_2\rangle=0,\qquad \langle x,\xi\cdot\alpha\rangle=\langle x,\xi\rangle\alpha=0,$$

so for a fixed subset $S$ of $M$, the collection of elements of $M^\ast$ orthogonal to every element of $S$ forms a submodule of $M^\ast$.

::: Definition 3
The submodule of $M^\ast$ defined as above is called the submodule orthogonal to $S$, and is denoted $S^\perp$.
:::

For an arbitrary subset $T\subseteq M^\ast$, we can similarly define $T^\perp$ by the formula

$$T^\perp=\{x\in M\mid \langle x, \xi\rangle=0\text{ for all $\xi\in T$}\};$$

note here that $T^\perp$ is defined as a submodule of $M$, not of $M^{\ast\ast}$.

## Transpose of a Linear Map

Let an arbitrary $A$-linear map $u:M \rightarrow N$ be given. Then the abelian group homomorphism

$$\Hom(u,A):\Hom_{\lMod{A}}(N,A)\rightarrow\Hom_{\lMod{A}}(M,A)$$

from [[Algebraic Structures] §Modules, ⁋Proposition 8](/en/math/algebraic_structures/modules#prop8) is compatible with the right action of $A$. That is, $\Hom(u,A)$ is a right $A$-module homomorphism.

::: Definition 4
For an $A$-linear map $u:M \rightarrow N$ between left $A$-modules, the right $A$-module homomorphism defined above is called the *transpose* of $u$, and is denoted $u^t$.
:::

The map $u^t$ is determined by its value $u^t(\xi)\in M^\ast$ at arbitrary $\xi\in N^\ast$, and in turn $u^t(\xi)\in M^\ast$ is determined by its value at arbitrary $x\in M$,

$$u^t(\xi)(x)=\langle x, u^t(\xi)\rangle.$$

On the other hand, by the definition of $u^t=\Hom(u,A)$ we have $u^t(\xi)=\xi\circ u$. Hence the above equation can be written as

$$\langle u(x),\xi\rangle=\langle x, u^t\xi\rangle,$$

and conversely, if this equation holds for all $x\in M$ and all $\xi\in N^\ast$, then $u^t$ is uniquely determined.

Moreover, for two $A$-linear maps $u,v:M \rightarrow N$ and arbitrary $\xi\in N^\ast$, $x\in M$, the equality $\xi((u+v)(x))=\xi(u(x))+\xi(v(x))$, together with the functoriality of $\Hom(-,A)$ and [[Algebraic Structures] §Modules, ⁋Proposition 8](/en/math/algebraic_structures/modules#prop8), yields the following proposition.

::: Proposition 5
The following hold.

1. For two $A$-linear maps $u,v:M \rightarrow N$, we have $(u+v)^t=u^t+v^t$.
2. For two $A$-linear maps $u:M \rightarrow N$ and $v:N \rightarrow L$, we have $(v\circ u)^t=u^t\circ v^t$.
3. For any $M$, we have $(\id_M)^t=\id_{M^\ast}$.
4. For any $A$-linear isomorphism $u:M \rightarrow N$, we have $(u^{-1})^t=(u^t)^{-1}$.
:::

## Dual Basis

Suppose that the $A$-module $M$ has a basis $(e_i)_{i\in I}$. ([§Bases, ⁋Definition 1](/en/math/multilinear_algebra/basis_of_free_modules#def1)) That is, there exists an isomorphism

$$\varepsilon: A^{\oplus I} \rightarrow M.$$

Then considering the dual of this isomorphism, we obtain an isomorphism of right $A$-modules

$$\varepsilon^t: M^\ast \rightarrow (A_l^{\oplus I})^\ast=\Hom_{\lMod{A}}(A_l^{\oplus I}, A_l)\cong \prod_{i\in I}\left(\Hom_\lMod{A}(A_l,A_l)\right)\cong \prod_{i\in I} A_r.$$

Now among the elements of the right-hand side, consider those whose $i$-th component is $1$ and all other components are $0$, and write $e_i^\ast$ for the preimage of such an element under $\varepsilon^t$. Then we know that the formula

$$\langle e_i, e_j^\ast\rangle=\delta_{ij}$$

holds. The collection of these elements is linearly independent, but if $I$ is infinite then it does not form a basis of $M^\ast$. However, if $I$ is finite then $\prod_{i\in I} A\cong \bigoplus_{i\in I}A$, so these elements form a basis exactly.

::: Definition 6
Fix an arbitrary free module $M$ and a basis $(e_i)_{i\in I}$. Then the family $(e_i^\ast)_{i\in I}$ of elements of $M^\ast$ defined above is called the *coordinate form* corresponding to $(e_i)_{i\in I}$.  
If $M$ is a finitely generated free module, then this family $(e_i^\ast)_{i\in I}$ is a basis of $M^\ast$, and is called the *dual basis* of $(e_i)$.
:::

## Double Dual Space

For any left $A$-module $M$, the dual $M^\ast$ is a right $A$-module, and the dual $M^{\ast\ast}$ of $M^\ast$ is again a left $A$-module. On the other hand, for arbitrary $x\in M$, one can check that the function

$$\langle x,-\rangle: M^\ast \rightarrow A$$

defined by the above formula is a right $A$-module homomorphism. That is, the above formula defines a function from $M$ to $M^{\ast\ast}$, and one can also check that this function is a linear map. In general this function is neither injective nor surjective.

::: Definition 7
If the above function $M \rightarrow M^{\ast\ast}$ is bijective, we call $M$ *reflexive*.
:::

Then the following holds.

::: Proposition 8
For any free module $M$, the map $M \rightarrow M^{\ast\ast}$ defined above is injective. If in addition $M$ is finitely generated, then this map is bijective.
:::

---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.
