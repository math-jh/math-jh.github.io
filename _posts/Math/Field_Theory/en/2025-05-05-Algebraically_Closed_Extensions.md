---
title: "Algebraic Closure"
description: "An algebraically closed field is a field in which every nonconstant polynomial has a root, which is equivalent to every algebraic extension having degree one. The definition and properties of relatively algebraically closed fields are also covered."
excerpt: "Algebraically closed fields and the existence of algebraic closures"

categories: [Math / Field Theory]
permalink: /en/math/field_theory/algebraically_closed_extensions
sidebar: 
    nav: "field_theory-en"

date: 2025-05-05
weight: 3
translated_at: 2026-09-24T18:20:46+00:00
translation_source: antigravity-gemini-3.8-flash-high
---
In the previous post, we defined what an algebraic extension is. First, let us look at the following proposition.

::: Proposition 1
For a field $\mathbb{K}$, the following are all equivalent. 

1. Any non-constant polynomial in $\mathbb{K}[\x]$ can always be expressed as a product of linear polynomials. 
2. Any non-constant polynomial in $\mathbb{K}[\x]$ always has at least one root. 
3. The only irreducible polynomials in $\mathbb{K}[\x]$ are linear polynomials. 
4. Any algebraic extension of $\mathbb{K}$ always has degree $1$. 
:::
::: Proof
First, it is clear that the first and second conditions are equivalent. If the first condition holds, it is clear that the third condition holds. In addition, by [\[Ring Theory\] §Polynomial Rings, ⁋Proposition 6](/en/math/ring_theory/polynomial_rings#prop6){: data-lid="9tk6w" }, any element of $\mathbb{K}[\x]$ can be factored into a product of irreducible polynomials, and since linear polynomials have roots in $\mathbb{K}$ for obvious reasons, the third condition implies the second condition. Therefore, the first through third conditions are all equivalent.

Now let us show that the third and fourth conditions are equivalent. First, assuming that the third condition holds, for an algebraic extension $\mathbb{L}/\mathbb{K}$, the minimal polynomial of any element $x$ is irreducible ([§Algebraic Extensions, ⁋Theorem 15](/en/math/field_theory/algebraic_extensions#thm15){: data-lid="a70tu" }), so we know from the third condition that this minimal polynomial must be a linear polynomial. 

Now assume the fourth condition. In $\mathbb{K}[\x]$, for an irreducible polynomial $f$, if we consider $\mathbb{K}[\x]/(f)$, this is an algebraic extension of $\mathbb{K}$ of degree $\deg f$. Since we assume that the degree of this extension must be $1$, the third condition is obtained. 
:::

::: Definition 2
A field $\mathbb{K}$ satisfying the above equivalent conditions is called an *algebraically closed field*. 
:::

If, for a field extension $\Omega/\mathbb{K}$, every element of $\Omega$ that is algebraic over $\mathbb{K}$ belongs to $\mathbb{K}$, we say that $\mathbb{K}$ is a *relatively algebraically closed field* in $\Omega$. In general, a relatively algebraically closed field does not have to be algebraically closed, but the following holds. 

::: Proposition 3
For an algebraically closed field $\Omega$ and a subfield $\mathbb{K}$, the relative algebraic closure of $\mathbb{K}$ in $\Omega$, $\overline{\mathbb{K}}$, is an algebraically closed field. 
:::

This is because, given any non-constant $f\in \overline{\mathbb{K}}[\x]$, we may also view $f$ as an element of $\Omega[\x]$, so from the assumption that $\Omega$ is algebraically closed, we can find a root of $f$ in $\Omega$, and this root must belong to $\overline{\mathbb{K}}$. The following fact makes use of Euclid's proof that there are infinitely many primes. 

::: Proposition 4
Any algebraically closed field is infinite. 
:::
::: Proof
Suppose to the contrary that $\Omega$ is a finite algebraically closed field, and consider the polynomial

$$1+\prod_{a\in \Omega}(\x-a)$$

This polynomial does not have any $a$ as a root. 
:::

::: Theorem 5
Suppose an algebraic extension $\mathbb{L}/\mathbb{K}$ is given, and let $\Omega$ be an algebraically closed extension of $\mathbb{K}$. Then there exists a morphism from $\mathbb{L}/\mathbb{K}$ to $\Omega/\mathbb{K}$. 
:::

The proof of this is obtained from [§Algebraic Extensions, ⁋Proposition 8](/en/math/field_theory/algebraic_extensions#prop8){: data-lid="cuvhf" }. Indeed, from this we obtain, for $\mathbb{L}$ and $\Omega$, a composite field $\mathbb{M}$ and extensions $u_1: \mathbb{L}\rightarrow \mathbb{M}$, $u_2: \Omega\rightarrow \mathbb{M}$. Since $\mathbb{L}/\mathbb{K}$ is algebraic, $\mathbb{M}/u_2(\Omega)$ is also algebraic, and since $u_2(\Omega)\cong\Omega$ is algebraically closed, by the fourth condition of [Proposition 1](#prop1){: data-lid="w5aet" } we have $\mathbb{M}=u_2(\Omega)$, and hence $u_2^{-1}\circ u_1$ gives the desired morphism. 

## Splitting Extensions

If we consider constructively obtaining the algebraically closed extensions discussed above, we see that we must make the following definition. 

::: Definition 6
For a field $\mathbb{K}$ and non-constant polynomials $f_i\in \mathbb{K}[\x]$, a *splitting extension* of these polynomials is a field extension $\mathbb{L}/\mathbb{K}$ satisfying the following conditions: 

1. Every $f_i$ factors into a product of linear polynomials in $\mathbb{L}[\x]$.  
2. For each $i$, if $R_i$ is the collection in $\mathbb{L}$ of roots of $f_i$, then $\mathbb{L}=\mathbb{K}(\bigcup_{i\in I} R_i)$. 
:::

Then we must prove the existence of a splitting extension.

::: Proposition 7
For a field $\mathbb{K}$ and non-constant polynomials $f_i\in \mathbb{K}[\x]$, there exists a splitting extension of these polynomials. 
:::
::: Proof
When forming an algebraic extension, only the roots of the polynomials matter anyway, so we may assume that the given polynomials $f_i$ are all monic polynomials. Suppose each $f_i$ is a monic polynomial of degree $d_i$. Then by the construction of [\[Multilinear Algebra\] §Symmetric Tensors, §§Symmetric Functions](/en/math/multilinear_algebra/symmetric_tensors#symmetric-functions){: data-lid="c7n2q" }, for each $i$, we can satisfy the following two conditions:

1. $A_i$ is generated as a $\mathbb{K}$-algebra by $\xi_{i,1},\ldots, \xi_{i, d_i}$. 
2. In $A_i[\x]$, $f_i(\x)=\prod_{k=1}^{d_i} (\x-\xi_{i,k})$ holds. 

by choosing a $\mathbb{K}$-algebra $A_i$ and elements $\xi_{i,1},\ldots, \xi_{i, d_i}\in A_i$. 

Now, using these, we must construct an extension of $\mathbb{K}$. If we let

$$A=\bigotimes_{i\in I} A_i$$

then by Krull's theorem $A$ has a maximal ideal $\mathfrak{m}$ ([\[Algebraic Structures\] §Definition of a Ring, ⁋Theorem 10](/en/math/algebraic_structures/rings#thm10){: data-lid="4v96p" }), so we may set $\mathbb{L}=A/\mathfrak{m}$, which gives the desired splitting extension. 
:::

Moreover, the splitting extension is unique in the following sense. 

::: Proposition 8
Let a field $\mathbb{K}$ and polynomials $f_i\in \mathbb{K}[\x]$ be given, and fix an extension $\Omega/\mathbb{K}$. If two subextensions $\mathbb{L}_1$ and $\mathbb{L}_2$ are splitting extensions of these polynomials, then $\mathbb{L}_1=\mathbb{L}_2$. 
:::

## Algebraic Closure

Now we define the following. 

::: Definition 9
An *algebraic closure* of a field $\mathbb{K}$ refers to an algebraic extension of $\mathbb{K}$ that is itself algebraically closed. 
:::

To show the existence of an algebraic closure, it would be natural to consider, for all (non-constant) polynomials in $\mathbb{K}[\x]$, their splitting extension $\Omega$. However, to show that $\Omega$ is algebraically closed, one must show that the roots of polynomials with coefficients in the roots added from $\mathbb{K}$ also belong again to $\Omega$, which is not so simple. The following proposition shows that we do not need to worry about such a situation. 

::: Proposition 10
An algebraic extension $\Omega/\mathbb{K}$ is algebraically closed if and only if every non-constant polynomial in $\mathbb{K}[\x]$ factors into a product of linear polynomials in $\Omega[\x]$. 
:::
::: Proof
Naturally, it suffices to show only one direction. For this, fix an algebraic extension of $\Omega$, denoted $\Omega'$, and let $x\in\Omega'$. We must show that $x\in \Omega$. First, $x$ is algebraic over $\Omega$, and since $\Omega/\mathbb{K}$ is algebraic, by [§Algebraic Extensions, ⁋Proposition 19](/en/math/field_theory/algebraic_extensions#prop19){: data-lid="l04wy" }, $x$ is also algebraic over $\mathbb{K}$. Now, letting $u\in \mathbb{K}[\x]$ be the minimal polynomial of $x$, $u$ splits into a product of linear polynomials in $\Omega[\x]$, and hence $x\in \Omega$. 
:::

Therefore, to find an algebraic closure of a given field $\mathbb{K}$, it suffices to consider a splitting extension of all non-constant polynomials of $\mathbb{K}$. 

::: Proposition 11
For a field $\mathbb{K}$ and an algebraic extension $\Omega/\mathbb{K}$, the following hold:

1. If $\Omega$ is algebraically closed, any algebraic extension of $\mathbb{K}$ is isomorphic to some subextension of $\Omega/\mathbb{K}$.
2. Conversely, if any finite-degree algebraic extension of $\mathbb{K}$ is isomorphic to a subextension of $\Omega$, then $\Omega$ is algebraically closed. 
:::

Therefore, an algebraic closure of $\mathbb{K}$ is unique up to isomorphism. When one or more algebraic extensions of $\mathbb{K}$ are given, we can compare them by embedding them into a (any) common algebraic closure; in such situations, since there is no need to choose a specific algebraic closure of $\mathbb{K}$, we simply denote it by $\overline{\mathbb{K}}$. In any case, when dealing with fields, as always, we regard isomorphic fields as identical, so by a slight abuse of notation we agree to view all algebraic extensions of $\mathbb{K}$ as subextensions of $\overline{\mathbb{K}}$.

---

**References**

**[Bou]** N. Bourbaki. *Algebra II: Chapters 4–7*. Springer, 2003.
