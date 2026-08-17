---
title: "Dimension"
description: "We examine several equivalent ways to define dimension in algebraic geometry. This covers the definition as a topological space as well as the Krull dimension of the coordinate ring of an affine variety."
excerpt: "Equivalent definitions of dimension for algebraic varieties"

categories: [Math / Algebraic Varieties]
permalink: /en/math/algebraic_varieties/dimension
sidebar: 
    nav: "algebraic_varieties-en"


date: 2026-03-22
weight: 5
translated_at: 2026-08-17T09:17:17+00:00
translation_source: kimi-cli
---
Dimension is one of the most fundamental invariants in geometry. In algebraic geometry, dimension is equally important, and there are several equivalent ways to define it. In this post, we review various ways to define the dimension of a variety.

## Dimension as a Topological Space

Since an algebraic variety is already a topological space, we can use [[Topology] §Dimension, ⁋Definition 10](/en/math/topology/dimension#def10) to define the dimension of $X$ as the supremum of the lengths of strictly descending chains of irreducible closed subsets.

::: Example 1
For an infinite field $\mathbb{K}$, the closed subsets of $\mathbb{A}^1$ are $\mathbb{A}^1$ itself and finite sets. Thus the longest chain is $\mathbb{A}^1 \supsetneq \{p\}$, which is a chain of length $1$, so $\mathbb{A}^1$ has dimension $1$ under this definition.
:::

This definition has the advantage of defining dimension from a purely topological perspective. However, it is not very efficient for actual computations, because we would need to know all chains of irreducible closed subsets.

## Dimension of an Affine Variety

On the other hand, we already know that the relationship between an algebraic variety and the functions defined on it is very close. Therefore, it should not be surprising that the algebraic structure of functions on an algebraic variety carries information about its dimension. To approach this perspective, it is best to look at the case of *affine* varieties, where the coordinate ring $\mathbb{K}[X]$ is given neatly.

::: Proposition 2
For an affine variety $X$ defined over an algebraically closed field $\mathbb{K}$, the dimension of $X$ equals the Krull dimension of the coordinate ring $\mathbb{K}[X]$. ([[Commutative Algebra] §Dimension, ⁋Definition 1](/en/math/commutative_algebra/Krull_dimension#def1))
:::

::: Proof
From [§Affine Varieties, ⁋Proposition 12](/en/math/algebraic_varieties/affine_varieties#prop12), there is a one-to-one correspondence between irreducible closed subsets of an affine variety and prime ideals of $\mathbb{K}[X]$.
:::
::: Corollary 3
For an infinite field $\mathbb{K}$, we have $\dim \mathbb{A}^n = n$.
:::

::: Proof
[[Commutative Algebra] §System of Parameters, ⁋Corollary 11](/en/math/commutative_algebra/system_of_parameters#cor11)
:::

On the other hand, for any prime ideal $\mathfrak{p}\subseteq \mathbb{K}[\x_1,\ldots, \x_n]$, we know that the following identity

$$\dim \mathbb{K}[\x_1,\ldots, \x_n]/\mathfrak{p}+\codim \mathfrak{p}=\dim \mathbb{K}[\x_1,\ldots, \x_n]=n\tag{$\ast$}$$

holds. ([[Commutative Algebra] §Noether Normalization, ⁋Theorem 4](/en/math/commutative_algebra/noether_normalization#thm4)) Here, the codimension of $\mathfrak{p}$ is defined in [[Commutative Algebra] §Dimension, ⁋Definition 2](/en/math/commutative_algebra/Krull_dimension#def2) as the supremum of the lengths of chains of prime ideals contained in $\mathfrak{p}$, and geometrically it is the supremum of the lengths of chains of closed subvarieties of $\mathbb{A}^n$ containing $X=Z(\mathfrak{p})$. Geometrically, we know that $\dim \mathbb{K}[\x_1,\ldots, \x_n]/\mathfrak{p}$ is the dimension of $Z(\mathfrak{p})$, so through this we can give a geometric meaning to ($\ast$).

## Dimension of a Projective Variety

The problem arises when we move to projective varieties. Recall that the only global functions on $\mathbb{P}^n$ are constant functions. The dimension of a projective variety $X\subseteq \mathbb{P}^n$ is already defined as the dimension of the underlying topological space, so the remaining problem is how to compute it. The first thing that comes to mind in this situation is to take an affine chart. That is, after choosing an affine open chart $U_i$ of $\mathbb{P}^n$, we can consider the dimension of $X_i=X\cap U_i$ as an affine variety. However, to show that this method is correct, we need to show that the dimension of any open subset equals the dimension of the original variety, so we cannot use this yet. Instead, we use the *affine cone* $C(X)$ of $X$.

For a projective variety $X\subseteq \mathbb{P}^n$, the affine cone $C(X)\subseteq \mathbb{A}^{n+1}$ is the affine variety in $\mathbb{A}^{n+1}$ defined by viewing the homogeneous ideal defining $X$ as an ideal in $\mathbb{K}[\x_0,\ldots, \x_n]$. That is, for the homogeneous ideal $I(X)$ defining $X$, if we define the ring $S(X)$ as

$$S(X)=\mathbb{K}[\x_0,\ldots, \x_n]/I(X)$$

then this becomes the coordinate ring of the affine cone. The key result for computing the dimension of a projective variety is the following.

::: Proposition 4
For a projective variety $X \subseteq \mathbb{P}^n$, we have $\dim X = \dim S(X) - 1$.
:::

This can be shown through computations in graded rings. In particular, $\dim C(X) = \dim X + 1$, and from this we obtain the following.

::: Proposition 5
We have $\dim \mathbb{P}^n = n$.
:::

::: Proof
The cone of $\mathbb{P}^n$ is $\mathbb{A}^{n+1}$ and $\dim \mathbb{A}^{n+1} = n+1$, so $\dim \mathbb{P}^n = (n+1) - 1 = n$.
:::

## Dimension of a Hypersurface

A hypersurface is a variety defined as the zero set of a single polynomial. Intuitively, adding one equation is the same as imposing one constraint, so it should reduce the dimension by one.

::: Proposition 6
For an algebraically closed field $\mathbb{K}$ and an irreducible polynomial $f \in \mathbb{K}[\x_1, \ldots, \x_n]$ over it, the dimension of the irreducible hypersurface $Z(f) \subseteq \mathbb{A}^n$ is $n - 1$.
:::

::: Proof
Since $f$ is irreducible, $(f)$ is a prime ideal, and thus the coordinate ring of $Z(f)$ is $\mathbb{K}[\x_1, \ldots, \x_n]/(f)$. Now let us show that the codimension of $(f)$ in $\mathbb{K}[\x_1, \ldots, \x_n]$ is $1$. The chain $(0) \subsetneq (f)$ is a chain of length $1$, so $\codim(f) \ge 1$. On the other hand, given a prime ideal $\mathfrak{q}$ with $(0) \subsetneq \mathfrak{q} \subseteq (f)$, if we factor $0 \neq g \in \mathfrak{q}$ in the UFD $\mathbb{K}[\x_1, \ldots, \x_n]$, some irreducible factor $p$ belongs to $\mathfrak{q}$, and from $(p) \subseteq (f)$ we get $f \mid p$, that is, $(f) = (p) \subseteq \mathfrak{q}$, so $\mathfrak{q} = (f)$. Then there can be no other prime ideal between $(0)$ and $(f)$. Therefore $\codim(f) = 1$, and

$$\dim \mathbb{K}[\x_1, \ldots, \x_n]/(f) = \dim \mathbb{K}[\x_1, \ldots, \x_n] - \codim(f) = n - 1$$

The first equality here follows from [[Commutative Algebra] §Noether Normalization, ⁋Theorem 4](/en/math/commutative_algebra/noether_normalization#thm4).
:::

## Dimension via Function Fields

Another way to define dimension is to use the function field. The function field $\mathbb{K}(X)$ carries information about the generic point of the variety, and it is also a birational invariant. The following proposition is also derived from an algebraic fact. ([[Commutative Algebra] §Noether Normalization, ⁋Theorem 3](/en/math/commutative_algebra/noether_normalization#thm3))

::: Proposition 7
The dimension of a variety $X$ equals the transcendence degree of the function field $\mathbb{K}(X)$ over $\mathbb{K}$.
:::

::: Example 8
The following are examples of dimension computations via function fields.

1. $\mathbb{K}(\mathbb{A}^n) = \mathbb{K}(\x_1, \ldots, \x_n)$, and since $\x_1, \ldots, \x_n$ are algebraically independent over $\mathbb{K}$, we have $\dim \mathbb{A}^n = n$.
2. $\mathbb{K}(V(\y - \x^2)) = \mathbb{K}(\x)$, and since $\x$ is algebraically independent over $\mathbb{K}$, we have $\dim V(\y - \x^2) = 1$. This is consistent with the intuition that a parabola is a curve.
3. $\mathbb{K}(\mathbb{P}^n) = \mathbb{K}(\x_1/\x_0, \ldots, \x_n/\x_0)$, and since $\x_1/\x_0, \ldots, \x_n/\x_0$ are algebraically independent over $\mathbb{K}$, we have $\dim \mathbb{P}^n = n$. This reflects the fact that projective space is birationally equivalent to affine space.
:::

## Basic Properties of Dimension

The most basic property of dimension is that a proper subset has smaller dimension. This is a geometrically obvious fact.

::: Proposition 9
For a closed subvariety $Y \subsetneq X$ of a variety $X$, we have $\dim Y < \dim X$.
:::

::: Proof
Considering a maximal chain of closed subvarieties of $Y$

$$Y = Y_0 \supsetneq Y_1 \supsetneq \cdots \supsetneq Y_n \neq \emptyset$$

since $X$ is irreducible,

$$X \supsetneq Y = Y_0 \supsetneq Y_1 \supsetneq \cdots \supsetneq Y_n$$

is a chain of closed subvarieties of $X$ of length $n+1$.
:::

This can be thought of as a weak generalization of [Proposition 6](#prop6). Applying it to a hypersurface $Z(f)\subsetneq \mathbb{A}^n$ only yields $\dim Z(f)\leq n-1$, so we cannot obtain from this that a single equation drops the dimension by exactly one. Now let us examine the relationship between regular maps and dimension.

::: Proposition 10
For two varieties $X, Y$ and a regular map $\varphi: X \rightarrow Y$, the following hold.

1. We have $\dim \varphi(X) \le \dim X$.
2. If $\varphi$ is dominant, then $\dim Y \le \dim X$ holds. ([§Rational Maps, ⁋Definition 8](/en/math/algebraic_varieties/rational_maps#def8))
:::

::: Proof
Let us show the second result first. If $\varphi$ is dominant, the pullback $\varphi^\ast: \mathbb{K}(Y)\rightarrow \mathbb{K}(X)$ is injective, and thus the desired result follows from [Proposition 7](#prop7).

The first result follows from this. Since $X$ is irreducible and $\varphi$ is continuous, $\varphi(X)$ is also irreducible, and therefore the closure $\overline{\varphi(X)}$ in $Y$ is a closed subvariety of $Y$. The regular map obtained by restricting the codomain of $\varphi$ to $\overline{\varphi(X)}$ is dominant by definition, so from the second result just shown we obtain $\dim \overline{\varphi(X)}\leq \dim X$. On the other hand, given a chain of irreducible closed subsets of $\varphi(X)$

$$Z_0 \supsetneq Z_1 \supsetneq \cdots \supsetneq Z_n$$

since each $Z_i$ is a closed subset of $\varphi(X)$, for the closure $\overline{Z_i}$ in $Y$ we have $\overline{Z_i}\cap \varphi(X)=Z_i$, and thus strict inclusion is preserved, so

$$\overline{Z_0} \supsetneq \overline{Z_1} \supsetneq \cdots \supsetneq \overline{Z_n}$$

is a chain of irreducible closed subsets of $\overline{\varphi(X)}$. Then $\dim \varphi(X)\leq \dim \overline{\varphi(X)}$, so we obtain the desired result.
:::

The first result supports our general intuition that a geometric function cannot increase dimension. The second result roughly shows that if $\varphi$ is surjective (up to birational equivalence), then the dimension of the target cannot exceed that of the domain.

::: Definition 11
A regular map $\varphi: X \rightarrow Y$ between irreducible varieties $X, Y$ is called *finite* if for every affine open $U \subseteq Y$, the preimage $\varphi^{-1}(U)$ is affine, and $\mathbb{K}[\varphi^{-1}(U)]$ is a finitely generated module over $\mathbb{K}[U]$.
:::

It can be shown that a finite morphism has finite fibers. For dimension, the following holds.

::: Proposition 12
For two varieties $X, Y$ and a finite surjective map $\varphi: X \rightarrow Y$, we have $\dim X = \dim Y$.
:::

::: Proof
If $\varphi$ is finite, at the coordinate ring level $\mathbb{K}[X]$ is finitely generated as a $\mathbb{K}[Y]$-module. Therefore $\mathbb{K}(X)$ is a finite degree extension of $\mathbb{K}(Y)$, and the transcendence degrees are equal. That is, $\dim X = \dim Y$.
:::

::: Example 13
A $k$-dimensional linear subspace $L$ of $\mathbb{A}^n$ has $\dim L = k$. This is because $L \cong \mathbb{A}^k$. Similarly, a $k$-dimensional linear subspace $L$ of $\mathbb{P}^n$ has $\dim L = k$.
:::

::: Example 14
When two varieties $X, Y \subseteq \mathbb{A}^n$ satisfy $X \cap Y \neq \emptyset$, we generally have

$$\dim(X \cap Y) \ge \dim X + \dim Y - n$$

This is called the *dimension inequality*. The reason this is an inequality is that in extreme situations such as $X=Y$, the desired equality may not hold. The case where equality holds is called a *proper intersection*.
:::

---

**References**

**[Har]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.  
**[Hart]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.  
**[AM]** M. F. Atiyah and I. G. Macdonald, *Introduction to Commutative Algebra*, Addison-Wesley, 1969.
