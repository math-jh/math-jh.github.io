---
title: "Dimension"
description: "We examine several equivalent ways to define dimension in algebraic geometry. The discussion ranges from the topological definition to the Krull dimension of the coordinate ring of an affine variety."
excerpt: "Dimensions of algebraic varieties"

categories: [Math / Algebraic Varieties]
permalink: /en/math/algebraic_varieties/dimension
sidebar: 
    nav: "algebraic_varieties-en"


date: 2026-03-22
weight: 5
translated_at: 2026-06-24T04:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-24T04:30:02+00:00
---
In geometry, dimension is one of the most basic invariants. In algebraic geometry it is equally important, and there are several equivalent ways to define it. In this post we examine various ways to define the dimension of a variety.

## Dimension as a topological space

Since an algebraic variety is already a topological space, we may use [[Topology] §Dimension, ⁋Definition 10](/en/math/topology/dimension#def10) to define the dimension of $$X$$ as the supremum of the lengths of strictly descending chains of irreducible closed subsets.

<div class="example" markdown="1">

<ins id="ex1">**Example 1**</ins> In $$\mathbb{A}^1$$ the closed sets are $$\mathbb{A}^1$$ itself and the finite sets. Thus the longest chain is $$\mathbb{A}^1 \supsetneq \{p\} \supsetneq \emptyset$$, which has length $$2$$; hence $$\mathbb{A}^1$$ has dimension $$1$$ under this definition.

</div>

The advantage of this definition is that it gives a purely topological notion of dimension. However, it is not very efficient in practice, because one must know all chains of irreducible closed subsets.

## Dimension of an affine variety

On the other hand, we already know that the relationship between an algebraic variety and the functions defined on it is very close. Therefore it should not be surprising that the algebraic structure of functions on a variety carries information about its dimension. To approach this point of view, it is best to look at the case of *affine* varieties, for which the coordinate ring $$\mathbb{K}[X]$$ is given cleanly.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> The dimension of an affine variety $$X$$ equals the Krull dimension of its coordinate ring $$\mathbb{K}[X]$$. ([[Commutative Algebra] §Dimension, ⁋Definition 1](/en/math/commutative_algebra/Krull_dimension#def1))

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

From [§Affine Varieties, ⁋Proposition 12](/en/math/algebraic_varieties/affine_varieties#prop12) there is a one-to-one correspondence between irreducible closed subsets of an affine variety and prime ideals of $$\mathbb{K}[X]$$.

</details>
<div class="proposition" markdown="1">

<ins id="cor3">**Corollary 3**</ins> $$\dim \mathbb{A}^n = n$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

[[Commutative Algebra] §System of Parameters, ⁋Corollary 11](/en/math/commutative_algebra/system_of_parameters#cor11)

</details>

On the other hand, for any prime ideal $$\mathfrak{p}\subset \mathbb{K}[\x_1,\ldots, \x_n]$$ we know that the following formula holds:

$$\dim \mathbb{K}[\x_1,\ldots, \x_n]/\mathfrak{p}+\codim \mathfrak{p}=\dim \mathbb{K}[\x_1,\ldots, \x_n]=n\tag{$\ast$}$$

([[Commutative Algebra] §Regular Local Rings, ⁋Proposition 4](/en/math/commutative_algebra/regular_local_rings#prop4)) Here the codimension of $$\mathfrak{p}$$ is as defined in [[Commutative Algebra] §Dimension, ⁋Definition 2](/en/math/commutative_algebra/Krull_dimension#def2): it is the supremum of the lengths of chains of prime ideals contained in $$\mathfrak{p}$$, and geometrically it is the supremum of the lengths of chains of closed subvarieties of $$\mathbb{A}^n$$ containing $$X=Z(\mathfrak{p})$$. Since geometrically $$\dim \mathbb{K}[\x_1,\ldots, \x_n]/\mathfrak{p}$$ is the dimension of $$Z(\mathfrak{p})$$, we can give ($$\ast$$) a geometric meaning through this.

## Dimension of a projective variety

The problem arises when we move to projective varieties. Recall that the only global functions on $$\mathbb{P}^n$$ are the constant functions. In this situation, to define the dimension of a projective variety we might try to take an affine chart. That is, given $$X\subset \mathbb{P}^n$$, we choose an affine open chart $$U_i$$ of $$\mathbb{P}^n$$ and consider the dimension of $$X_i=X\cap U_i$$ as an affine variety. However, to make this a definition we would first have to show that the dimension of any open set equals that of the original variety, so we cannot yet adopt this as a definition. Instead we use the *affine cone* $$C(X)$$ of $$X$$.

For a projective variety $$X\subseteq \mathbb{P}^n$$, the affine cone $$C(X)\subseteq \mathbb{A}^{n+1}$$ is the affine variety in $$\mathbb{A}^{n+1}$$ defined by the homogeneous ideal defining $$X$$, regarded as an ideal in $$\mathbb{K}[\x_0,\ldots, \x_n]$$. That is, for the homogeneous ideal $$I(X)$$ defining $$X$$, if we define the ring $$S(X)$$ by

$$S(X)=\mathbb{K}[\x_0,\ldots, \x_n]/I(X)$$

then this becomes the coordinate ring of the affine cone. The following result is key for computing the dimension of a projective variety.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> For a projective variety $$X \subseteq \mathbb{P}^n$$, we have $$\dim X = \dim S(X) - 1$$.

</div>

This can be shown through calculations in graded rings. In particular $$\dim C(X) = \dim X + 1$$, and from this we obtain the following.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> $$\dim \mathbb{P}^n = n$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

The cone of $$\mathbb{P}^n$$ is $$\mathbb{A}^{n+1}$$ and $$\dim \mathbb{A}^{n+1} = n+1$$, so $$\dim \mathbb{P}^n = (n+1) - 1 = n$$.

</details>

## Dimension of a hypersurface

A hypersurface is a variety defined as the zero set of a single polynomial. Intuitively, adding one equation imposes one constraint, so it should reduce the dimension by one.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> For an irreducible polynomial $$f \in \mathbb{K}[\x_1, \ldots, \x_n]$$, the irreducible hypersurface $$Z(f) \subset \mathbb{A}^n$$ has dimension $$n - 1$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Since $$f$$ is irreducible, $$(f)$$ is a prime ideal, and hence the coordinate ring of $$Z(f)$$ is $$\mathbb{K}[\x_1, \ldots, \x_n]/(f)$$. We now show that the codimension of $$(f)$$ in $$\mathbb{K}[\x_1, \ldots, \x_n]$$ is $$1$$. The chain $$(0) \subsetneq (f)$$ has length $$1$$, so $$\codim(f) \ge 1$$. On the other hand, in the UFD $$\mathbb{K}[\x_1, \ldots, \x_n]$$ every prime ideal of codimension $$1$$ is principal, so no other prime ideal can lie strictly between $$(0)$$ and $$(f)$$. Therefore $$\codim(f) = 1$$, and

$$\dim \mathbb{K}[\x_1, \ldots, \x_n]/(f) = \dim \mathbb{K}[\x_1, \ldots, \x_n] - \codim(f) = n - 1$$

In general, for a regular local ring $$R$$ and a prime ideal $$\mathfrak{p}$$, we have $$\dim R/\mathfrak{p} = \dim R - \codim(\mathfrak{p})$$. ([[Commutative Algebra] §Regular Local Rings, ⁋Proposition 4](/en/math/commutative_algebra/regular_local_rings#prop4))

</details>

## Dimension via the function field

Another way to define dimension is to use the function field. The function field $$\mathbb{K}(X)$$ contains information about the generic point of the variety, and it is also a birational invariant. The following proposition is also derived from an algebraic fact.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> The dimension of a variety $$X$$ equals the transcendence degree of its function field $$\mathbb{K}(X)$$ over $$\mathbb{K}$$.

</div>

<div class="example" markdown="1">

<ins id="ex8">**Example 8**</ins> The following are examples of dimension computations via function fields.

1. $$\mathbb{K}(\mathbb{A}^n) = \mathbb{K}(x_1, \ldots, x_n)$$, and $$x_1, \ldots, x_n$$ are algebraically independent over $$\mathbb{K}$$, so $$\dim \mathbb{A}^n = n$$.
2. $$\mathbb{K}(V(\y - \x^2)) = \mathbb{K}(x)$$, and $$x$$ is algebraically independent over $$\mathbb{K}$$, so $$\dim V(\y - \x^2) = 1$$. This agrees with the intuition that a parabola is a curve.
3. $$\mathbb{K}(\mathbb{P}^n) = \mathbb{K}(\x_1/\x_0, \ldots, \x_n/\x_0)$$, and $$\x_1/\x_0, \ldots, \x_n/\x_0$$ are algebraically independent over $$\mathbb{K}$$, so $$\dim \mathbb{P}^n = n$$. This reflects the fact that projective space is birationally equivalent to affine space.

</div>

## Basic properties of dimension

The most basic property of dimension is that a proper closed subset has smaller dimension. This is geometrically obvious.

<div class="proposition" markdown="1">

<ins id="prop9">**Proposition 9**</ins> For a closed subvariety $$Y \subsetneq X$$, we have $$\dim Y < \dim X$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Consider a maximal chain of closed subsets of $$Y$$

$$Y = Y_0 \supsetneq Y_1 \supsetneq \cdots \supsetneq Y_n \neq \emptyset$$

Then

$$X \supsetneq Y = Y_0 \supsetneq Y_1 \supsetneq \cdots \supsetneq Y_n$$

is a chain in $$X$$ of length $$n+1$$.

</details>

This can be regarded as a generalization of [Proposition 6](#prop6). We now examine the relationship between regular maps and dimension.

<div class="proposition" markdown="1">

<ins id="prop10">**Proposition 10**</ins> For two varieties $$X, Y$$ and a regular map $$\varphi: X \to Y$$, the following hold.

1. $$\dim \varphi(X) \le \dim X$$.
2. If $$\varphi$$ is dominant then $$\dim Y \le \dim X$$. ([§Rational Maps, ⁋Definition 8](/en/math/algebraic_varieties/rational_maps#def8))

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

1. For a chain of closed subsets of $$\varphi(X)$$

    $$Z_0 \supsetneq Z_1 \supsetneq \cdots \supsetneq Z_n$$

    their preimages

    $$\varphi^{-1}(Z_0) \supsetneq \varphi^{-1}(Z_1) \supsetneq \cdots \supsetneq \varphi^{-1}(Z_n)$$

    form a chain of closed subsets of $$X$$.
2. If $$\varphi$$ is dominant, then the pullback $$\varphi^\ast: \mathbb{K}(Y)\rightarrow \mathbb{K}(X)$$ is injective, and the desired result follows from [Proposition 7](#prop7).

</details>

The first result supports our general intuition that a geometric map cannot increase dimension. The second result roughly shows that if $$\varphi$$ is (up to birational equivalence) surjective, then the dimension of the target cannot exceed that of the domain.

<div class="definition" markdown="1">

<ins id="def11">**Definition 11**</ins> A regular map $$\varphi: X \to Y$$ between irreducible varieties is called *finite* if for every affine open $$U \subseteq Y$$, the preimage $$\varphi^{-1}(U)$$ is affine and $$\mathbb{K}[\varphi^{-1}(U)]$$ is a finitely generated module over $$\mathbb{K}[U]$$.

</div>

One can show that a finite morphism has finite fibers. Then the following is clear.

<div class="proposition" markdown="1">

<ins id="prop12">**Proposition 12**</ins> For two varieties $$X, Y$$ and a finite map $$\varphi: X \to Y$$, we have $$\dim X = \dim Y$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

If $$\varphi$$ is finite, then at the coordinate ring level $$\mathbb{K}[X]$$ is finitely generated as a $$\mathbb{K}[Y]$$-module. Hence $$\mathbb{K}(X)$$ is a finite-degree extension of $$\mathbb{K}(Y)$$, and the transcendence degrees are equal. Thus $$\dim X = \dim Y$$.

</details>

<div class="example" markdown="1">

<ins id="ex13">**Example 13**</ins> A $$k$$-dimensional linear subspace $$L$$ of $$\mathbb{A}^n$$ satisfies $$\dim L = k$$. This is because $$L \cong \mathbb{A}^k$$. Likewise, a $$k$$-dimensional linear subspace $$L$$ of $$\mathbb{P}^n$$ satisfies $$\dim L = k$$.

</div>

<div class="example" markdown="1">

<ins id="ex14">**Example 14**</ins> For two varieties $$X, Y \subseteq \mathbb{A}^n$$, we generally have

$$\dim(X \cap Y) \ge \dim X + \dim Y - n$$

This is called the *dimension inequality*. The reason this is an inequality is that in extreme situations, such as $$X=Y$$, the desired equality may fail. The case where equality holds is called a *proper intersection*.

</div>

---

**References**

**[Har]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.  
**[Hart]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.  
**[AM]** M. F. Atiyah and I. G. Macdonald, *Introduction to Commutative Algebra*, Addison-Wesley, 1969.
