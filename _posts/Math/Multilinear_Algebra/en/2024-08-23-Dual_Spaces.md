---
title: "Dual Spaces"
description: "This post covers the definition of dual modules over a given ring, Kronecker pairs, and the interplay between submodules."
excerpt: "Hom of modules, dual modules, and the bidual map"

categories: [Math / Multilinear Algebra]
permalink: /en/math/multilinear_algebra/dual_spaces
sidebar: 
    nav: "multilinear_algebra-en"

date: 2024-08-23
weight: 4
translated_at: 2026-06-01T15:30:03+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-01T15:30:03+00:00
---
## Module $$\Hom_\lMod{A}(M,N)$$

Fix arbitrary left $$A$$-modules $$M$$ and $$N$$. Then $$\Hom_\lMod{A}(M,N)$$ is an abelian group, but it does not generally carry the structure of a left $$A$$-module. That is, for arbitrary $$\alpha\in A$$ and $$u\in\Hom_\lMod{A}(M,N)$$, the map

$$x\mapsto \alpha u(x)$$

$$\alpha u: M \rightarrow N$$ defined by the above formula is not an $$A$$-linear map. This can be seen from the formula

$$(\alpha u)(\beta x)=\alpha u(\beta x)=\alpha \beta u(x)\neq \beta\alpha u(x)=\beta\cdot ((\alpha u)(x))$$

for arbitrary $$\beta\in A$$ and $$x\in M$$. However, from this formula we also see that if $$\alpha$$ lies in the center of $$A$$, then $$\alpha u$$ becomes an $$A$$-linear map. That is, with respect to the center $$Z(A)$$ of $$A$$, the set $$\Hom_\lMod{A}(M,N)$$ is a left $$Z(A)$$-module. By similar reasoning, for arbitrary right $$A$$-modules $$M,N$$, we see that $$\Hom_\rMod{A}(M,N)$$ is a right $$Z(A)$$-module.

Now suppose $$M$$ and $$N$$ are left $$A$$-modules, and in particular that $$N$$ carries a right $$B$$-module structure compatible with this, i.e., $$N$$ is an $$(A,B)$$-bimodule. Then for any $$\beta\in B$$ and $$u\in\Hom_\lMod{A}(M,N)$$, the map defined by

$$x\mapsto u(x)\beta$$

$$u\beta: M \rightarrow N$$ is an $$A$$-linear map, as can be seen from the formula

$$(u\beta)(\alpha x)=u(\alpha x)\beta=\alpha u(x)\beta=\alpha((u\beta)(x))$$

The same reasoning applies to a right $$A$$-module $$M$$ and a $$(B,A)$$-bimodule $$N$$.

## Definition of Dual Spaces

Any ring $$A$$ has a natural $$(A,A)$$-bimodule structure given by its multiplication. Therefore, by the preceding argument, we may regard $$\Hom_{\lMod{A}}(M, A)$$ as a right $$A$$-module.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> The right $$A$$-module $$\Hom_{\lMod{A}}(M, A)$$ defined above is called the *dual module* of $$M$$, and is denoted by $$M^\ast$$.

</div>

Similarly, given a right $$A$$-module $$M$$, we may view $$\Hom_{\rMod{A}}(M,A)$$ as a left $$A$$-module, and we call it the dual module of $$M$$. In the special case $$M=A$$, to avoid confusion we write $$A_l$$ for $$A$$ regarded as a left $$A$$-module and $$A_r$$ for $$A$$ regarded as a right $$A$$-module; then one can verify the two equalities $$A_l^\ast=A_r$$ and $$A_r^\ast=A_l$$.

By definition, for any $$x\in M$$ and $$\xi\in M^\ast$$, the pair assigns an element $$\xi(x)\in A$$. We write this as $$\langle x, \xi\rangle$$, and call this notation the *Kronecker pairing*.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> For any $$A$$-module $$M$$ and its dual $$M^\ast$$, elements $$x\in M$$ and $$\xi\in M^\ast$$ are said to be *orthogonal* if $$\langle x,\xi\rangle=0$$.

</div>

If every pair of elements from a subset of $$M$$ and a subset of $$M^\ast$$ is orthogonal, we say that the two subsets are orthogonal. Now fix an arbitrary $$x\in M$$, and let $$\xi,\xi_1,\xi_2\in M^\ast$$ and $$\alpha\in A$$. Then

$$\langle x, \xi_1+\xi_2\rangle=\langle x, \xi_1\rangle+\langle x,\xi_2\rangle=0,\qquad \langle x,\xi\cdot\alpha\rangle=\langle x,\xi\rangle\alpha=0$$

hence, for a fixed subset $$S$$ of $$M$$, the collection of elements of $$M^\ast$$ orthogonal to the elements of $$S$$ forms a submodule of $$M^\ast$$.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> The submodule of $$M^\ast$$ defined as above is called the submodule orthogonal to $$S$$, and is denoted by $$S^\perp$$.

</div>

For an arbitrary subset $$T\subseteq M^\ast$$, we can similarly define $$T^\perp$$ by the formula

$$T^\perp=\{x\in M\mid \langle x, \xi\rangle=0\text{ for all $\xi\in T$}\}$$

but note that here $$T^\perp$$ is defined as a submodule of $$M$$, not of $$M^{\ast\ast}$$.

## Transpose of Linear Maps

Let $$u:M \rightarrow N$$ be an arbitrary $$A$$-linear map. Then the abelian group homomorphism given in [[Algebraic Structures] §Modules, ⁋Proposition 8](/en/math/algebraic_structures/modules#prop8)

$$\Hom(u,A):\Hom_{\lMod{A}}(N,A)\rightarrow\Hom_{\lMod{A}}(M,A)$$

is compatible with the right action of $$A$$. That is, $$\Hom(u,A)$$ is a right $$A$$-module homomorphism.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> For an $$A$$-linear map $$u:M \rightarrow N$$ between left $$A$$-modules, the right $$A$$-module homomorphism defined above is called the *transpose* of $$u$$, and is denoted by $$u^\ast$$.

</div>

$$u^\ast$$ is determined by its values $$u^\ast(\xi)\in M^\ast$$ at any $$\xi\in N^\ast$$, and in turn each $$u^\ast(\xi)\in M^\ast$$ is determined by its values at any $$x\in M$$

$$u^\ast(\xi)(x)=\langle x, u^\ast(\xi)\rangle$$

By definition of $$u^\ast=\Hom(u,A)$$, we have $$u^\ast(\xi)=\xi\circ u$$. Thus the above formula can be written as

$$\langle u(x),\xi\rangle=\langle x, u^\ast\xi\rangle$$

and conversely, if this formula holds for all $$x\in M$$ and all $$\xi\in N^\ast$$, then $$u^\ast$$ is uniquely determined.

Moreover, by the functoriality of $$\Hom(-,A)$$ and [[Algebraic Structures] §Modules, ⁋Proposition 8](/en/math/algebraic_structures/modules#prop8), we obtain the following proposition.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> The following hold.

1. For any two $$A$$-linear maps $$u,v:M \rightarrow N$$, we have $$(u+v)^\ast=u^\ast+v^\ast$$.
2. For any two $$A$$-linear maps $$u:M \rightarrow N$$ and $$v:N \rightarrow L$$, we have $$(v\circ u)^\ast=u^\ast\circ v^\ast$$.
3. For any $$M$$, we have $$(\id_M)^\ast=\id_{M^\ast}$$.
4. For any $$A$$-linear isomorphism $$u:M \rightarrow N$$, we have $$(u^{-1})^\ast=(u^\ast)^{-1}$$. 

</div>

## Dual Basis

Suppose the $$A$$-module $$M$$ has a basis $$(x_i)_{i\in I}$$. ([§Basis, ⁋Definition 1](/en/math/multilinear_algebra/basis_of_free_modules#def1)) That is, there exists an isomorphism

$$\varepsilon: A^{\oplus I} \rightarrow M$$

Taking the dual of this isomorphism yields an isomorphism of right $$A$$-modules

$$\varepsilon^\ast: M^\ast \rightarrow (A_l^{\oplus I})^\ast=\Hom_{\lMod{A}}(A_l^{\oplus I}, A_l)\cong \prod_{i\in I}\left(\Hom_\lMod{A}(A_l,A_l)\right)\cong \prod_{i\in I} A_r$$

Now consider the elements on the right-hand side whose $$i$$th component is $$1$$ and whose remaining components are $$0$$, and denote the preimage of each such element under $$\varepsilon^\ast$$ by $$e_i^\ast$$. Then we see that the formula

$$\langle e_i, e_j^\ast\rangle=\delta_{ij}$$

holds. The collection of these elements is linearly independent, but if $$I$$ is infinite it does not form a basis of $$M^\ast$$. However, if $$I$$ is finite then $$\prod_{i\in I} A\cong \bigoplus_{i\in I}A$$, so they constitute a basis.

<div class="definition" markdown="1">

<ins id="def6">**Definition 6**</ins> Fix an arbitrary free module $$M$$ and a basis $$(e_i)_{i\in I}$$. Then the family $$(e_i^\ast)_{i\in I}$$ of elements of $$M^\ast$$ defined above is called the *coordinate form* corresponding to $$(e_i)_{i\in I}$$.  
If $$M$$ is a finitely generated free module, then this family $$(e_i^\ast)_{i\in I}$$ is a basis of $$M^\ast$$, and is called the *dual basis* of $$(e_i)$$.

</div>


## Bidual Space

For any left $$A$$-module $$M$$, the dual $$M^\ast$$ of $$M$$ is a right $$A$$-module, and the dual $$M^{\ast\ast}$$ of $$M^\ast$$ is again a left $$A$$-module. Now, for any $$x\in M$$, one can verify that the map defined by the formula

$$\langle x,-\rangle: M^\ast \rightarrow A$$

is a right $$A$$-module homomorphism. Thus the above formula defines a map from $$M$$ to $$M^{\ast\ast}$$, and one can verify that this map is also linear. In general, this map is neither injective nor surjective.

<div class="definition" markdown="1">

<ins id="def7">**Definition 7**</ins> If the above map $$M \rightarrow M^{\ast\ast}$$ is bijective, then $$M$$ is called *reflexive*.

</div>

Then the following holds.

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8**</ins> For any free module $$M$$, the map $$M \rightarrow M^{\ast\ast}$$ defined above is injective. If in addition $$M$$ is finitely generated, then this map is bijective.

</div>
