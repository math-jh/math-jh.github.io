---
title: "Algebraic Closures"
description: "An algebraically closed field is a field in which every non-constant polynomial has a root, which is equivalent to every algebraic extension having degree one. The definition and properties of relatively algebraically closed fields are also discussed."
excerpt: "The existence of algebraically closed fields and algebraic closures"

categories: [Math / Field Theory]
permalink: /en/math/field_theory/algebraically_closed_extensions
sidebar: 
    nav: "field_theory-en"

date: 2025-05-05
weight: 3
translated_at: 2026-05-31T04:30:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-31T04:30:04+00:00
---
In the previous post we defined what an algebraic extension is. First, consider the following proposition.

::: Proposition 1
For a field $$\mathbb{K}$$, the following are equivalent. 

1. Every non-constant polynomial in $$\mathbb{K}[\x]$$ is a product of linear polynomials. 
2. Every non-constant polynomial in $$\mathbb{K}[\x]$$ has at least one root. 
3. Every irreducible polynomial in $$\mathbb{K}[\x]$$ is linear. 
4. Every algebraic extension of $$\mathbb{K}$$ has degree $$1$$. 
:::
::: Proof
First, the equivalence of the first and second conditions is obvious. If the first condition holds, then the third condition is obvious. Also, by [\[Ring Theory\] §Polynomial Rings, ⁋Proposition 6](/en/math/ring_theory/polynomial_rings#prop6), any element of $$\mathbb{K}[\x]$$ can be written as a product of irreducible polynomials, and linear polynomials have roots in $$\mathbb{K}$$ for obvious reasons, so the third condition implies the second. Therefore the first three conditions are all equivalent.

Now let us show that the third and fourth conditions are equivalent. Assume that the third condition holds; then for any element $$x$$ of an algebraic extension $$\mathbb{L}/\mathbb{K}$$, its minimal polynomial is irreducible ([§Algebraic Extensions, ⁋Theorem 15](/en/math/field_theory/algebraic_extensions#thm15)), so from the third condition this minimal polynomial must be linear. 

Now assume the fourth condition. For an irreducible polynomial $$f$$ in $$\mathbb{K}[\x]$$, consider $$\mathbb{K}[\x]/(f)$$; this is an algebraic extension of $$\mathbb{K}$$ of degree $$n$$. Since we are assuming that every algebraic extension of $$\mathbb{K}$$ has degree $$1$$, the third condition follows. 
:::

::: Definition 2
A field $$\mathbb{K}$$ satisfying the above equivalent conditions is called an *algebraically closed field*. 
:::

If for a field extension $$\Omega/\mathbb{K}$$, every element of $$\Omega$$ that is algebraic over $$\mathbb{K}$$ belongs to $$\mathbb{K}$$, then $$\mathbb{K}$$ is said to be *relatively algebraically closed* in $$\Omega$$. In general, a relatively algebraically closed field need not be algebraically closed, but the following holds. 

::: Proposition 3
For an algebraically closed field $$\Omega$$ and a subfield $$\mathbb{K}$$, the relative algebraic closure $$\overline{\mathbb{K}}$$ of $$\mathbb{K}$$ in $$\Omega$$ is an algebraically closed field. 
:::

This is because given any $$f\in \overline{\mathbb{K}}[\x]$$, we may also regard $$f$$ as an element of $$\Omega[\x]$$; then by the assumption that $$\Omega$$ is algebraically closed we can find a root of $$f$$ in $$\Omega$$, and this root must belong to $$\overline{\mathbb{K}}$$. The following fact uses Euclid's proof that there are infinitely many primes. 

::: Proposition 4
Every algebraically closed field is infinite. 
:::
::: Proof
Suppose for contradiction that $$\Omega$$ is a finite algebraically closed field, and consider the polynomial

$$1+\prod_{a\in \Omega}(\x-a)$$

This polynomial has no root in $$\Omega$$. 
:::

::: Theorem 5
Let an algebraic extension $$\mathbb{L}/\mathbb{K}$$ be given, and let $$\Omega$$ be an algebraically closed extension of $$\mathbb{K}$$. Then there exists a morphism from $$\mathbb{L}/\mathbb{K}$$ to $$\Omega/\mathbb{K}$$. 
:::

The proof of this is immediate from [§Algebraic Extensions, ⁋Proposition 8](/en/math/field_theory/algebraic_extensions#prop8). 

## Splitting Extensions

If we try to obtain the algebraically closed extension examined above constructively, we see that we need the following definition. 

::: Definition 6
For a field $$\mathbb{K}$$ and polynomials $$f_i\in \mathbb{K}[\x]$$, a *splitting extension* of these polynomials is a field extension $$\mathbb{L}/\mathbb{K}$$ satisfying the following conditions. 

1. All the $$f_i$$ factor into products of linear polynomials in $$\mathbb{L}[\x]$$.  
2. For each $$i$$, letting $$R_i$$ be the set of all roots of $$f_i$$ in $$\mathbb{L}$$, we have $$\mathbb{L}=\mathbb{K}(\bigcup R_i)$$. 
:::

Then we must prove the existence of a splitting extension. 

::: Proposition 7
For a field $$\mathbb{K}$$ and polynomials $$f_i\in \mathbb{K}[\x]$$, a splitting extension of these polynomials exists. 
:::
::: Proof
When dealing with algebraic extensions, only the roots of the polynomials matter anyway, so we may assume that the given polynomials $$f_i$$ are all monic. Suppose each $$f_i$$ is a monic polynomial of degree $$d_i$$. Then by [\[Multilinear Algebra\] §Symmetric Tensors, ⁋Proposition 14](/en/math/multilinear_algebra/symmetric_tensors#prop14), for each $$i$$ we can choose a $$\mathbb{K}$$-algebra $$A_i$$ and elements $$\xi_{i,1},\ldots, \xi_{i, d_i}\in A_i$$ satisfying the following two conditions:

1. $$A_i$$ is generated as a $$\mathbb{K}$$-algebra by $$\xi_{i,1},\ldots, \xi_{i, d_i}$$. 
2. In $$A_i[\x]$$, the equality $$f_i(\x)=\prod_{k=1}^{d_i} (\x-\xi_{i,k})$$ holds. 

Now we must construct an extension of $$\mathbb{K}$$ using these. Let

$$A=\bigotimes_{i\in I} A_i$$

Then by Krull's theorem there exists a maximal ideal $$\mathfrak{m}$$ of $$A$$, so we can set $$\mathbb{L}=A/\mathfrak{m}$$, and this gives the desired splitting extension. 
:::

Moreover, a splitting extension is unique in the following sense. 

::: Proposition 8
Let a field $$\mathbb{K}$$ and polynomials $$f_i\in \mathbb{K}[\x]$$ be given, and fix an extension $$\Omega/\mathbb{K}$$. If two subextensions $$\mathbb{L}_1$$ and $$\mathbb{L}_2$$ are splitting extensions of these, then $$\mathbb{L}_1=\mathbb{L}_2$$. 
:::

## Algebraic Closures

We now make the following definition. 

::: Definition 9
An *algebraic closure* of a field $$\mathbb{K}$$ is an algebraic extension of $$\mathbb{K}$$ that is itself algebraically closed. 
:::

To show the existence of an algebraic closure, it would be natural to consider the splitting field $$\Omega$$ of all (non-constant) polynomials in $$\mathbb{K}[\x]$$. However, to show that $$\Omega$$ is algebraically closed, one must show that the roots of polynomials whose coefficients are the roots already adjoined from $$\mathbb{K}$$ also lie in $$\Omega$$, so this is not so simple. The following proposition shows that there is no need to worry about such a situation. 

::: Proposition 10
An algebraic extension $$\Omega/\mathbb{K}$$ is algebraically closed if and only if every non-constant polynomial in $$\mathbb{K}[\x]$$ factors into a product of linear polynomials in $$\Omega[\x]$$. 
:::
::: Proof
Of course, it suffices to show only one direction. For this, take any algebraic extension $$\Omega'$$ of $$\Omega$$, and let $$x\in\Omega'$$. We must show that $$x\in \Omega$$. First, $$x$$ is algebraic over $$\Omega$$, and since $$\Omega/\mathbb{K}$$ is algebraic, $$x$$ is also algebraic over $$\mathbb{K}$$. Now let $$u\in \mathbb{K}[\x]$$ be the minimal polynomial of $$x$$; then $$u$$ splits into a product of linear polynomials in $$\Omega[\x]$$, and therefore $$x\in \Omega$$. 
:::

Therefore, to find an algebraic closure of a given field $$\mathbb{K}$$, it suffices to consider the splitting field of all non-constant polynomials in $$\mathbb{K}[\x]$$. This is necessarily unique by [Proposition 8](#prop8). 

::: Proposition 11
For an algebraic extension $$\Omega/\mathbb{K}$$ of a field $$\mathbb{K}$$, the following hold.

1. If $$\Omega$$ is algebraically closed, then any algebraic extension of $$\mathbb{K}$$ is isomorphic to some subextension of $$\Omega/\mathbb{K}$$.
2. Conversely, if every finite-degree algebraic extension of $$\mathbb{K}$$ is isomorphic to a subextension of $$\Omega$$, then $$\Omega$$ is algebraically closed. 
:::

Therefore, the algebraic closure of $$\mathbb{K}$$ exists uniquely up to isomorphism. When one or more algebraic extensions of $$\mathbb{K}$$ are given, we can embed them into a (common) algebraic closure to compare them; in such a situation there is no need to choose a specific algebraic closure of $$\mathbb{K}$$, so we simply write $$\overline{\mathbb{K}}$$. After all, when dealing with fields we always treat isomorphic fields as the same, so by a slight abuse we shall think of all algebraic extensions of $$\mathbb{K}$$ as subextensions of $$\overline{\mathbb{K}}$$.
