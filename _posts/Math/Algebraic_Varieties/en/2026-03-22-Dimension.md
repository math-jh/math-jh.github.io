---
title: "Dimension"
excerpt: "Dimension of algebraic varieties"

categories: [Math / Algebraic Varieties]
permalink: /en/math/algebraic_varieties/dimension
sidebar: 
    nav: "algebraic_varieties-en"

header:
    overlay_image: /assets/images/Math/Algebraic_Varieties/Dimension.png
    overlay_filter: 0.5

date: 2026-03-22
last_modified_at: 2026-03-22
weight: 5
translated_at: 2026-05-28T11:36:15+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-25T21:00:04+00:00
---
In geometry, dimension is among the most fundamental invariants. In algebraic geometry it is equally important, and there are several equivalent ways to define it. In this post we examine various definitions of the dimension of a variety.

## Dimension as a Topological Space

An algebraic variety is already a topological space, so by [\[Topology\] §Dimension, ⁋Definition 10](/en/math/topology/dimension#def10) we may define the dimension of $$X$$ as the supremum of the lengths of strictly descending chains of irreducible closed subsets.

<div class="example" markdown="1">

<ins id="ex1">**Example 1**</ins> In $$\mathbb{A}^1$$ the only closed sets are $$\mathbb{A}^1$$ itself and finite sets. Hence the longest chain is $$\mathbb{A}^1 \supsetneq \{p\} \supsetneq \emptyset$$, a chain of length $$2$$, so $$\mathbb{A}^1$$ is $$1$$-dimensional under this definition.

</div>

This definition has the virtue of being purely topological. However, it is not very efficient in practice, because one must know all chains of irreducible closed subsets.

## Dimension of an Affine Variety

We already know that an algebraic variety and the functions defined on it are intimately related. It is therefore not surprising that the algebraic structure of these functions encodes information about the dimension. To pursue this viewpoint, it is natural to begin with the case of an *affine* variety, whose coordinate ring $$\mathbb{K}[X]$$ is given explicitly.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> The dimension of an affine variety $$X$$ equals the Krull dimension of its coordinate ring $$\mathbb{K}[X]$$. ([\[Commutative Algebra\] §Dimension, ⁋Definition 1](/en/math/commutative_algebra/Krull_dimension#def1))

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

By [§Affine Varieties, ⁋Proposition 12](/en/math/algebraic_varieties/affine_varieties#prop12), irreducible closed subsets of an affine variety correspond bijectively to prime ideals of $$\mathbb{K}[X]$$.

</details>
<div class="proposition" markdown="1">

<ins id="cor3">**Corollary 3**</ins> $$\dim \mathbb{A}^n = n$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

[\[Commutative Algebra\] §System of Parameters, ⁋Theorem 10](/en/math/commutative_algebra/system_of_parameters#cor10)

</details>

Meanwhile, for any prime ideal $$\mathfrak{p}\subset \mathbb{K}[\x_1,\ldots, \x_n]$$ we know that

$$\dim \mathbb{K}[\x_1,\ldots, \x_n]/\mathfrak{p}+\codim \mathfrak{p}=\dim \mathbb{K}[\x_1,\ldots, \x_n]=n\tag{$\ast$}$$

holds. ([\[Commutative Algebra\] §Regular Local Rings, ⁋Proposition 4](/en/math/commutative_algebra/regular_local_rings#prop4)) Here the codimension of $$\mathfrak{p}$$ is defined in [\[Commutative Algebra\] §Dimension, ⁋Definition 2](/en/math/commutative_algebra/Krull_dimension#def2) as the supremum of the lengths of chains of prime ideals contained in $$\mathfrak{p}$$; geometrically it is the supremum of the lengths of chains of closed subvarieties of $$\mathbb{A}^n$$ containing $$X=Z(\mathfrak{p})$$. Since $$\dim \mathbb{K}[\x_1,\ldots, \x_n]/\mathfrak{p}$$ is the dimension of $$Z(\mathfrak{p})$$, equation ($\ast$) acquires a geometric meaning.

## Dimension of a Projective Variety

The difficulty appears when we pass to projective varieties. Recall that global functions on $$\mathbb{P}^n$$ are only the constants. In this situation one might try to define the dimension of a projective variety by choosing an affine chart: given $$X\subset \mathbb{P}^n$$, pick an affine open chart $$U_i$$ of $$\mathbb{P}^n$$ and consider the dimension of $$X_i=X\cap U_i$$ as an affine variety. But this would require proving first that the dimension of any open subset equals that of the original variety, so we cannot adopt it as a definition yet. Instead we use the *affine cone* $$C(X)$$ of $$X$$.

For a projective variety $$X\subseteq \mathbb{P}^n$$, the affine cone $$C(X)\subseteq \mathbb{A}^{n+1}$$ is the affine variety in $$\mathbb{A}^{n+1}$$ defined by the homogeneous ideal defining $$X$$, regarded as an ideal in $$\mathbb{K}[\x_0,\ldots, \x_n]$$. That is, for the homogeneous ideal $$I(X)$$ defining $$X$$, the ring

$$S(X)=\mathbb{K}[\x_0,\ldots, \x_n]/I(X)$$

is the coordinate ring of the affine cone. The following result is the key to computing the dimension of a projective variety.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> For a projective variety $$X \subseteq \mathbb{P}^n$$, $$\dim X = \dim S(X) - 1$$.

</div>

This follows from a computation in graded rings. In particular $$\dim C(X) = \dim X + 1$$, and from this we obtain:

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> $$\dim \mathbb{P}^n = n$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

The cone of $$\mathbb{P}^n$$ is $$\mathbb{A}^{n+1}$$ and $$\dim \mathbb{A}^{n+1} = n+1$$, so $$\dim \mathbb{P}^n = (n+1) - 1 = n$$.

</details>

## Dimension of a Hypersurface

A hypersurface is a variety defined as the zero set of a single polynomial. Intuitively, adding one equation imposes one constraint and should reduce the dimension by one.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> For an irreducible polynomial $$f \in \mathbb{K}[\x_1, \ldots, \x_n]$$, the irreducible hypersurface $$Z(f) \subset \mathbb{A}^n$$ has dimension $$n - 1$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Since $$f$$ is irreducible, $$(f)$$ is prime, and the coordinate ring of $$Z(f)$$ is $$\mathbb{K}[\x_1, \ldots, \x_n]/(f)$$. We show that the codimension of $$(f)$$ in $$\mathbb{K}[\x_1, \ldots, \x_n]$$ is $$1$$. The chain $$(0) \subsetneq (f)$$ has length $$1$$, so $$\codim(f) \ge 1$$. On the other hand, in the UFD $$\mathbb{K}[\x_1, \ldots, \x_n]$$ every prime ideal of codimension $$1$$ is principal, so no prime ideal can lie strictly between $$(0)$$ and $$(f)$$. Hence $$\codim(f) = 1$$, and

$$\dim \mathbb{K}[\x_1, \ldots, \x_n]/(f) = \dim \mathbb{K}[\x_1, \ldots, \x_n] - \codim(f) = n - 1$$

In general, for a regular local ring $$R$$ and a prime ideal $$\mathfrak{p}$$, we have $$\dim R/\mathfrak{p} = \dim R - \codim(\mathfrak{p})$$. ([\[Commutative Algebra\] §Regular Local Rings, ⁋Proposition 4](/en/math/commutative_algebra/regular_local_rings#prop4))

</details>

## Dimension via Function Fields

Another way to define dimension is through the function field. The function field $$\mathbb{K}(X)$$ carries information about the generic point of the variety and is a birational invariant. The following proposition is also deduced from an algebraic fact.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> The dimension of a variety $$X$$ equals the transcendence degree of its function field $$\mathbb{K}(X)$$ over $$\mathbb{K}$$.

</div>

<div class="example" markdown="1">

<ins id="ex8">**Example 8**</ins> The following are examples of dimension computations via function fields.

1. $$\mathbb{K}(\mathbb{A}^n) = \mathbb{K}(x_1, \ldots, x_n)$$, and $$x_1, \ldots, x_n$$ are algebraically independent over $$\mathbb{K}$$, so $$\dim \mathbb{A}^n = n$$.
2. $$\mathbb{K}(V(\y - \x^2)) = \mathbb{K}(x)$$, and $$x$$ is algebraically independent over $$\mathbb{K}$$, so $$\dim V(\y - \x^2) = 1$$. This agrees with the intuition that a parabola is a curve.
3. $$\mathbb{K}(\mathbb{P}^n) = \mathbb{K}(\x_1/\x_0, \ldots, \x_n/\x_0)$$, and $$\x_1/\x_0, \ldots, \x_n/\x_0$$ are algebraically independent over $$\mathbb{K}$$, so $$\dim \mathbb{P}^n = n$$. This reflects the fact that projective space is birationally equivalent to affine space.

</div>

## Basic Properties of Dimension

The most basic property of dimension is that a proper closed subvariety has smaller dimension. This is geometrically evident.

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

This may be regarded as a generalization of [Proposition 6](#prop6). We now turn to the relationship between regular maps and dimension.

<div class="proposition" markdown="1">

<ins id="prop10">**Proposition 10**</ins> For varieties $$X, Y$$ and a regular map $$\varphi: X \to Y$$, the following hold.

1. $$\dim \varphi(X) \le \dim X$$.
2. If $$\varphi$$ is dominant, then $$\dim Y \le \dim X$$. ([§Rational Maps, ⁋Definition 8](/en/math/algebraic_varieties/rational_maps#def8))

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

1. Given a chain of closed subsets of $$\varphi(X)$$
    
    $$Z_0 \supsetneq Z_1 \supsetneq \cdots \supsetneq Z_n$$

    their preimages

    $$\varphi^{-1}(Z_0) \supsetneq \varphi^{-1}(Z_1) \supsetneq \cdots \supsetneq \varphi^{-1}(Z_n)$$

    form a chain of closed subsets in $$X$$.
2. If $$\varphi$$ is dominant, the pullback $$\varphi^\ast: \mathbb{K}(Y)\rightarrow \mathbb{K}(X)$$ is injective, and the desired result follows from [Proposition 7](#prop7).

</details>

The first statement supports the intuition that a geometric map cannot increase dimension. The second says, roughly, that if $$\varphi$$ is surjective (up to birational equivalence), then the dimension of the target cannot exceed that of the source.

<div class="definition" markdown="1">

<ins id="def11">**Definition 11**</ins> A regular map $$\varphi: X \to Y$$ between irreducible varieties is called *finite* if for every affine open $$U \subseteq Y$$, the preimage $$\varphi^{-1}(U)$$ is affine and $$\mathbb{K}[\varphi^{-1}(U)]$$ is a finitely generated module over $$\mathbb{K}[U]$$.

</div>

A finite morphism has finite fibers. From this the next result is immediate.

<div class="proposition" markdown="1">

<ins id="prop12">**Proposition 12**</ins> For varieties $$X, Y$$ and a finite map $$\varphi: X \to Y$$, we have $$\dim X = \dim Y$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

If $$\varphi$$ is finite, then at the level of coordinate rings $$\mathbb{K}[X]$$ is finitely generated as a $$\mathbb{K}[Y]$$-module. Hence $$\mathbb{K}(X)$$ is a finite extension of $$\mathbb{K}(Y)$$, and the transcendence degrees are equal. Thus $$\dim X = \dim Y$$.

</details>

<div class="example" markdown="1">

<ins id="ex13">**Example 13**</ins> A $$k$$-dimensional linear subspace $$L$$ of $$\mathbb{A}^n$$ satisfies $$\dim L = k$$, because $$L \cong \mathbb{A}^k$$. Likewise, a $$k$$-dimensional linear subspace $$L$$ of $$\mathbb{P}^n$$ satisfies $$\dim L = k$$.

</div>

<div class="example" markdown="1">

<ins id="ex14">**Example 14**</ins> For varieties $$X, Y \subseteq \mathbb{A}^n$$, in general

$$\dim(X \cap Y) \ge \dim X + \dim Y - n$$

This is called the *dimension inequality*. It is an inequality because in extreme cases, such as $$X=Y$$, equality may fail. When equality does hold, we call the intersection *proper*.

</div>

---

**References**

**[Har]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.  
**[Hart]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.  
**[AM]** M. F. Atiyah and I. G. Macdonald, *Introduction to Commutative Algebra*, Addison-Wesley, 1969.
