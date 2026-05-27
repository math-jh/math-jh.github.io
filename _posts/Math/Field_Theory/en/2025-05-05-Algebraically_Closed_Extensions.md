---
title: "Algebraic Closures"
excerpt: "The existence of algebraically closed fields and algebraic closures"

categories: [Math / Field Theory]
permalink: /en/math/field_theory/algebraically_closed_extensions
header:
    overlay_image: /assets/images/Math/Field_Theory/Algebraically_Closed_Extensions.png
    overlay_filter: 0.5
sidebar: 
    nav: "field_theory-en"

date: 2025-05-05
last_modified_at: 2025-05-05
weight: 3
translated_at: 2026-05-28T11:36:15+00:00
translation_source: kimi-cli
---
In the previous post we defined what an algebraic extension is. First, let us look at the following proposition.

<div class="proposition" markdown="1">

<ins id="prop1">**Proposition 1**</ins> For a field $$\mathbb{K}$$, the following are all equivalent. 

1. Every non-constant polynomial in $$\mathbb{K}[\x]$$ is always a product of linear polynomials. 
2. Every non-constant polynomial in $$\mathbb{K}[\x]$$ always has at least one root. 
3. Irreducible polynomials in $$\mathbb{K}[\x]$$ are all linear. 
4. Every algebraic extension of $$\mathbb{K}$$ always has degree $$1$$. 

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, the equivalence of the first and second conditions is obvious. If the first condition holds, then it is obvious that the third condition holds. Also, by [\[Ring Theory\] §Polynomial Rings, ⁋Proposition 6](/en/math/ring_theory/polynomial_rings#prop6), any element of $$\mathbb{K}[\x]$$ can be written as a product of irreducible polynomials, and linear polynomials have roots in $$\mathbb{K}$$ for obvious reasons, so the third condition implies the second. Therefore the first through third conditions are all equivalent.

Now let us show that the third and fourth conditions are equivalent. First, assume that the third condition holds; then for any element $$x$$ of an algebraic extension $$\mathbb{L}/\matbb{K}$$, its minimal polynomial is irreducible ([§Algebraic Extensions, ⁋Theorem 15](/en/math/field_theory/algebraic_extensions#thm15)), so from the third condition we know that this minimal polynomial must be linear. 

Now assume the fourth condition. For an irreducible polynomial $$f$$ in $$\mathbb{K}[\x]$$, consider $$\mathbb{K}[\x]/(f)$$; this is an algebraic extension of $$\mathbb{K}$$ of degree $$n$$. Since we are assuming that this extension must have degree $$1$$, the third condition follows. 

</details>

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> A field $$\mathbb{K}$$ satisfying the above equivalent conditions is called an *algebraically closed field*. 

</div>

If for a field extension $$\Omega/\mathbb{K}$$, every element of $$\Omega$$ that is algebraic over $$\mathbb{K}$$ belongs to $$\mathbb{K}$$, then $$\mathbb{K}$$ is called a *relatively algebraically closed field* in $$\Omega$$. In general, a relatively algebraically closed field need not be algebraically closed, but the following holds. 

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> For an algebraically closed field $$\Omega$$ and a subfield $$\mathbb{K}$$, the relative algebraic closure $$\overline{\mathbb{K}}$$ of $$\mathbb{K}$$ in $$\Omega$$ is an algebraically closed field. 

</div>

This is because given any $$f\in \overline{\mathbb{K}}[\x]$$, we can also regard $$f$$ as an element of $$\Omega[\x]$$, so by the assumption that $$\Omega$$ is algebraically closed we can find a root of $$f$$ in $$\Omega$$, and this root must belong to $$\overline{\mathbb{K}}$$. The following fact uses Euclid's proof that there are infinitely many primes. 

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> Every algebraically closed field is infinite. 

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Suppose for contradiction that $$\Omega$$ is a finite algebraically closed field, and consider the following polynomial

$$1+\prod_{a\in \Omega}(\x-a)$$

This polynomial does not have any $$a$$ as a root. 

</details>

<div class="proposition" markdown="1">

<ins id="thm5">**Theorem 5**</ins> Let an algebraic extension $$\mathbb{L}/\mathbb{K}$$ be given, and let $$\Omega$$ be an algebraically closed extension of $$\mathbb{K}$$. Then there exists a morphism from $$\mathbb{L}/\mathbb{K}$$ to $$\Omega/\mathbb{K}$$. 

</div>

The proof of this is obvious from [§Algebraic Extensions, ⁋Proposition 8](/en/math/field_theory/algebraic_extensions#prop8). 

## Splitting Extensions

If we try to obtain the algebraically closed extension examined above constructively, we see that we need to make the following definition. 

<div class="definition" markdown="1">

<ins id="def6">**Definition 6**</ins> For a field $$\mathbb{K}$$ and polynomials $$f_i\in \mathbb{K}[\x]$$, a *splitting extension* of these polynomials is a field extension $$\mathbb{L}/\mathbb{K}$$ satisfying the following conditions. 

1. All the $$f_i$$ factor into products of linear polynomials in $$\mathbb{L}[\x]$$.  
2. For each $$i$$, letting $$R_i$$ be the set of roots of $$f_i$$ in $$\mathbb{L}$$, we have $$\mathbb{L}=\mathbb{K}(\bigcup R_i)$$. 

</div>

Then we must prove the existence of a splitting extension. 

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> For a field $$\mathbb{K}$$ and polynomials $$f_i\in \mathbb{K}[\x]$$, a splitting extension of these polynomials exists. 

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

When dealing with algebraic extensions, only the roots of the polynomials matter anyway, so we may assume that the given polynomials $$f_i$$ are all monic. Suppose each $$f_i$$ is a monic polynomial of degree $$d_i$$. Then by [\[Multilinear Algebra\] §Symmetric Tensors, ⁋Proposition 13](/en/math/multilinear_algebra/symmetric_tensors#prop13), for each $$i$$ we can choose a $$\mathbb{K}$$-algebra $$A_i$$ and elements $$\xi_{i,1},\ldots, \xi_{i, d_i}\in A_i$$ satisfying the following two conditions:

1. $$A_i$$ is generated as a $$\mathbb{K}$$-algebra by $$\xi_{i,1},\ldots, \xi_{i, d_i}$$. 
2. In $$A_i[\x]$$, the equality $$f_i(\x)=\prod_{k=1}^{d_i} (\x-\xi_{i,k})$$ holds. 

Now we must construct an extension of $$\mathbb{K}$$ using them. Let

$$A=\bigotimes_{i\in I} A_i$$

Then by Krull's theorem there exists a maximal ideal $$\mathfrak{m}$$ of $$A$$, so we can set $$\mathbb{L}=A/\mathfrak{m}$$, and this gives the desired splitting extension. 

</details>

Moreover, a splitting extension is unique in the following sense. 

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8**</ins> Let a field $$\mathbb{K}$$ and polynomials $$f_i\in \mathbb{K}[\x]$$ be given, and fix an extension $$\Omega/\mathbb{K}$$. If two subextensions $$\mathbb{L}_1$$ and $$\mathbb{L}_2$$ are splitting extensions of these, then $$\mathbb{L}_1=\mathbb{L}_2$$. 

</div>

## Algebraic Closures

We now define the following. 

<div class="definition" markdown="1">

<ins id="def9">**Definition 9**</ins> The *algebraic closure* of a field $$\mathbb{K}$$ is an algebraic extension of $$\mathbb{K}$$ that is itself algebraically closed. 

</div>

To show the existence of an algebraic closure, it would be natural to consider the splitting field $$\Omega$$ of all (non-constant) polynomials in $$\mathbb{K}[\x]$$. However, to show that $$\Omega$$ is algebraically closed, one must show that the roots of polynomials whose coefficients are the roots adjoined from $$\mathbb{K}$$ also lie in $$\Omega$$ again, so this is not so simple. The following proposition shows that there is no need to worry about such a situation. 

<div class="proposition" markdown="1">

<ins id="prop10">**Proposition 10**</ins> An algebraic extension $$\Omega/\mathbb{K}$$ is algebraically closed if and only if every non-constant polynomial in $$\mathbb{K}[\x]$$ factors into a product of linear polynomials in $$\Omega[\x]$$. 

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Of course, it suffices to show only one direction. For this, take any algebraic extension $$\Omega'$$ of $$\Omega$$, and let $$x\in\Omega'$$. We must show that $$x\in \Omega$$. First, $$x$$ is algebraic over $$\Omega$$, and since $$\Omega/\mathbb{K}$$ is algebraic, $$x$$ is also algebraic over $$\mathbb{K}$$. Now let $$u\in \mathbb{K}[\x]$$ be the minimal polynomial of $$x$$; then $$u$$ splits into a product of linear polynomials in $$\Omega[\x]$$, and therefore $$x\in \Omega$$. 

</details>

Therefore, to find an algebraic closure of a given field $$\mathbb{K}$$, it suffices to consider the splitting field of all non-constant polynomials in $$\mathbb{K}[\x]$$. This is necessarily unique by [Proposition 8](#prop8). 

<div class="proposition" markdown="1">

<ins id="prop11">**Proposition 11**</ins> For an algebraic extension $$\Omega/\mathbb{K}$$ of a field $$\mathbb{K}$$, the following hold.

1. If $$\Omega$$ is algebraically closed, then any algebraic extension of $$\mathbb{K}$$ is isomorphic to some subextension of $$\Omega/\mathbb{K}$$.
2. Conversely, if every finite degree algebraic extension of $$\mathbb{K}$$ is isomorphic to a subextension of $$\Omega$$, then $$\Omega$$ is algebraically closed. 

</div>

Therefore, the algebraic closure of $$\mathbb{K}$$ exists uniquely up to isomorphism. When one or more algebraic extensions of $$\mathbb{K}$$ are given, we can embed them into a (common) algebraic closure to compare them; in such a situation there is no need to choose a specific algebraic closure of $$\mathbb{K}$$, so we simply write $$\overline{\mathbb{K}}$$. After all, when dealing with fields we always treat isomorphic fields as the same, so by a slight abuse we shall think of all algebraic extensions of $$\mathbb{2}$$ as subextensions of $$\overline{\mathbb{K}}$$.
