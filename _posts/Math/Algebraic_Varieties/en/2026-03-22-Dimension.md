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
translated_at: 2026-08-18T20:15:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-08-18T20:15:05+00:00
---
Dimension is one of the most fundamental invariants in geometry. In algebraic geometry, it is equally important, and there are several equivalent ways to define it. In this post, we examine various definitions of the dimension of a variety.

## Dimension as a Topological Space

Since an algebraic variety is already a topological space, we may use [[Topology] §Dimension, ⁋Definition 10](/en/math/topology/dimension#def10) to define the dimension of $X$ as the supremum of the lengths of strictly descending chains of irreducible closed subsets.

::: Example 1
For an infinite field $\mathbb{K}$, the closed subsets of $\mathbb{A}^1$ are $\mathbb{A}^1$ itself and the finite sets. Hence the longest chain is $\mathbb{A}^1 \supsetneq \{p\}$, which has length $1$, so $\mathbb{A}^1$ has dimension $1$ under this definition.
:::

This definition has the virtue of being purely topological. However, it is not very efficient for actual computation, since one would need to know all chains of irreducible closed subsets.

## Dimension of an Affine Variety

On the other hand, we already know that an algebraic variety and the functions defined on it are intimately related. Thus it should come as no surprise that the algebraic structure of these functions carries information about the dimension. To pursue this viewpoint, it is best to begin with the case of *affine* varieties, where the coordinate ring $\mathbb{K}[X]$ is given explicitly.

::: Proposition 2
For an affine variety $X$ over an algebraically closed field $\mathbb{K}$, the dimension of $X$ equals the Krull dimension of its coordinate ring $\mathbb{K}[X]$. ([[Commutative Algebra] §Dimension, ⁋Definition 1](/en/math/commutative_algebra/Krull_dimension#def1))
:::

::: Proof
By [§Affine Varieties, ⁋Proposition 12](/en/math/algebraic_varieties/affine_varieties#prop12), irreducible closed subsets of an affine variety correspond bijectively to prime ideals of $\mathbb{K}[X]$.
:::
::: Corollary 3
For an infinite field $\mathbb{K}$, we have $\dim \mathbb{A}^n = n$.
:::

::: Proof
[[Commutative Algebra] §System of Parameters, ⁋Corollary 11](/en/math/commutative_algebra/system_of_parameters#cor11)
:::

On the other hand, for any prime ideal $\mathfrak{p}\subseteq \mathbb{K}[\x_1,\ldots, \x_n]$, we know that the identity

$$\dim \mathbb{K}[\x_1,\ldots, \x_n]/\mathfrak{p}+\codim \mathfrak{p}=\dim \mathbb{K}[\x_1,\ldots, \x_n]=n\tag{$\ast$}$$

holds. ([[Commutative Algebra] §Noether Normalization, ⁋Theorem 4](/en/math/commutative_algebra/noether_normalization#thm4)) Here the codimension of $\mathfrak{p}$ is defined in [[Commutative Algebra] §Dimension, ⁋Definition 2](/en/math/commutative_algebra/Krull_dimension#def2) as the supremum of the lengths of chains of prime ideals contained in $\mathfrak{p}$; geometrically, it is the supremum of the lengths of chains of closed subvarieties of $\mathbb{A}^n$ containing $X=Z(\mathfrak{p})$. Since $\dim \mathbb{K}[\x_1,\ldots, \x_n]/\mathfrak{p}$ is the dimension of $Z(\mathfrak{p})$, this allows us to interpret ($\ast$) geometrically.

## Dimension of a Projective Variety

The difficulty begins when we pass to projective varieties. Recall that the only global regular functions on $\mathbb{P}^n$ are the constants. The dimension of a projective variety $X\subseteq \mathbb{P}^n$ is already defined as that of the underlying topological space, so the remaining task is to compute it. The first idea that comes to mind is to use an affine chart: choose an affine open chart $U_i$ of $\mathbb{P}^n$ and consider the dimension of $X_i=X\cap U_i$ as an affine variety. But to justify this method one must know that the dimension of any open subset equals that of the original variety, which we do not yet have. Instead, we use the *affine cone* $C(X)$ of $X$.

For a projective variety $X\subseteq \mathbb{P}^n$, the affine cone $C(X)\subseteq \mathbb{A}^{n+1}$ is the affine variety in $\mathbb{A}^{n+1}$ defined by the homogeneous ideal of $X$, viewed as an ideal in $\mathbb{K}[\x_0,\ldots, \x_n]$. That is, for the homogeneous ideal $I(X)$ defining $X$, the ring

$$S(X)=\mathbb{K}[\x_0,\ldots, \x_n]/I(X)$$

is the coordinate ring of the affine cone. The key result for computing the dimension of a projective variety is the following.

::: Proposition 4
For a projective variety $X \subseteq \mathbb{P}^n$, we have $\dim X = \dim S(X) - 1$.
:::

This follows from computations in graded rings. In particular, $\dim C(X) = \dim X + 1$, and from this we obtain:

::: Proposition 5
We have $\dim \mathbb{P}^n = n$.
:::

::: Proof
The cone of $\mathbb{P}^n$ is $\mathbb{A}^{n+1}$, and $\dim \mathbb{A}^{n+1} = n+1$, so $\dim \mathbb{P}^n = (n+1) - 1 = n$.
:::

## Dimension of a Hypersurface

A hypersurface is a variety defined as the zero set of a single polynomial. Intuitively, imposing one equation means imposing one constraint, so the dimension should drop by one.

::: Proposition 6
For an algebraically closed field $\mathbb{K}$ and an irreducible polynomial $f \in \mathbb{K}[\x_1, \ldots, \x_n]$, the irreducible hypersurface $Z(f) \subseteq \mathbb{A}^n$ has dimension $n - 1$.
:::

::: Proof
Since $f$ is irreducible, $(f)$ is a prime ideal, and hence the coordinate ring of $Z(f)$ is $\mathbb{K}[\x_1, \ldots, \x_n]/(f)$. Let us show that the codimension of $(f)$ in $\mathbb{K}[\x_1, \ldots, \x_n]$ is $1$. The chain $(0) \subsetneq (f)$ has length $1$, so $\codim(f) \ge 1$. Conversely, let $\mathfrak{q}$ be a prime ideal with $(0) \subsetneq \mathfrak{q} \subseteq (f)$. Take any nonzero $g \in \mathfrak{q}$ and factor it in the UFD $\mathbb{K}[\x_1, \ldots, \x_n]$; some irreducible factor $p$ lies in $\mathfrak{q}$. From $(p) \subseteq (f)$ we get $f \mid p$, hence $(f) = (p) \subseteq \mathfrak{q}$, so $\mathfrak{q} = (f)$. Thus there is no prime ideal strictly between $(0)$ and $(f)$, and $\codim(f) = 1$. Therefore

$$\dim \mathbb{K}[\x_1, \ldots, \x_n]/(f) = \dim \mathbb{K}[\x_1, \ldots, \x_n] - \codim(f) = n - 1$$

where the first equality follows from [[Commutative Algebra] §Noether Normalization, ⁋Theorem 4](/en/math/commutative_algebra/noether_normalization#thm4).
:::

## Dimension via Function Fields

Another way to define dimension is through the function field. The function field $\mathbb{K}(X)$ captures information about the generic point of the variety and is a birational invariant. The following proposition is also deduced from an algebraic fact. ([[Commutative Algebra] §Noether Normalization, ⁋Theorem 3](/en/math/commutative_algebra/noether_normalization#thm3))

::: Proposition 7
The dimension of a variety $X$ equals the transcendence degree of its function field $\mathbb{K}(X)$ over $\mathbb{K}$.
:::

::: Example 8
The following are examples of dimension computations using function fields.

1. $\mathbb{K}(\mathbb{A}^n) = \mathbb{K}(\x_1, \ldots, \x_n)$, and since $\x_1, \ldots, \x_n$ are algebraically independent over $\mathbb{K}$, we have $\dim \mathbb{A}^n = n$.
2. $\mathbb{K}(V(\y - \x^2)) = \mathbb{K}(\x)$, and since $\x$ is algebraically independent over $\mathbb{K}$, we have $\dim V(\y - \x^2) = 1$. This agrees with the intuition that a parabola is a curve.
3. $\mathbb{K}(\mathbb{P}^n) = \mathbb{K}(\x_1/\x_0, \ldots, \x_n/\x_0)$, and since $\x_1/\x_0, \ldots, \x_n/\x_0$ are algebraically independent over $\mathbb{K}$, we have $\dim \mathbb{P}^n = n$. This reflects the fact that projective space is birationally equivalent to affine space.
:::

## Basic Properties of Dimension

The most basic property of dimension is that a proper closed subvariety has smaller dimension. This is geometrically obvious.

::: Proposition 9
For a closed subvariety $Y \subsetneq X$, we have $\dim Y < \dim X$.
:::

::: Proof
Consider a maximal chain of closed subvarieties of $Y$

$$Y = Y_0 \supsetneq Y_1 \supsetneq \cdots \supsetneq Y_n \neq \emptyset$$

Since $X$ is irreducible,

$$X \supsetneq Y = Y_0 \supsetneq Y_1 \supsetneq \cdots \supsetneq Y_n$$

is a chain of closed subvarieties of $X$ of length $n+1$.
:::

This may be viewed as a weak generalization of [Proposition 6](#prop6). Applied to a hypersurface $Z(f)\subsetneq \mathbb{A}^n$, it yields only $\dim Z(f)\leq n-1$, so it does not suffice to show that a single equation drops the dimension by exactly one. We now turn to the relationship between regular maps and dimension.

::: Proposition 10
For two varieties $X, Y$ and a regular map $\varphi: X \rightarrow Y$, the following hold.

1. We have $\dim \varphi(X) \le \dim X$.
2. If $\varphi$ is dominant, then $\dim Y \le \dim X$.  ([§Rational Maps, ⁋Definition 8](/en/math/algebraic_varieties/rational_maps#def8))
:::

::: Proof
Let us prove the second statement first. If $\varphi$ is dominant, the pullback $\varphi^\ast: \mathbb{K}(Y)\rightarrow \mathbb{K}(X)$ is injective, and the desired result follows from [Proposition 7](#prop7).

The first statement follows from this. Since $X$ is irreducible and $\varphi$ is continuous, $\varphi(X)$ is also irreducible; hence its closure $\overline{\varphi(X)}$ in $Y$ is a closed subvariety. The regular map obtained by restricting the codomain of $\varphi$ to $\overline{\varphi(X)}$ is dominant by definition, so the second result gives $\dim \overline{\varphi(X)}\leq \dim X$. On the other hand, given a chain of irreducible closed subsets of $\varphi(X)$

$$Z_0 \supsetneq Z_1 \supsetneq \cdots \supsetneq Z_n$$

each $Z_i$ is closed in $\varphi(X)$, so for its closure $\overline{Z_i}$ in $Y$ we have $\overline{Z_i}\cap \varphi(X)=Z_i$, and strict inclusions are preserved. Thus

$$\overline{Z_0} \supsetneq \overline{Z_1} \supsetneq \cdots \supsetneq \overline{Z_n}$$

is a chain of irreducible closed subsets of $\overline{\varphi(X)}$. Hence $\dim \varphi(X)\leq \dim \overline{\varphi(X)}$, which yields the desired result.
:::

The first statement supports the general intuition that a geometric map cannot increase dimension. The second statement shows, roughly speaking, that if $\varphi$ is surjective (up to birational equivalence), then the dimension of the target cannot exceed that of the source.

::: Definition 11
A regular map $\varphi: X \rightarrow Y$ between irreducible varieties $X, Y$ is called *finite* if for every affine open $U \subseteq Y$, the preimage $\varphi^{-1}(U)$ is affine and $\mathbb{K}[\varphi^{-1}(U)]$ is a finitely generated module over $\mathbb{K}[U]$.
:::

One can show that a finite morphism has finite fibers. Concerning dimension, we have the following.

::: Proposition 12
For two varieties $X, Y$ and a finite surjective map $\varphi: X \rightarrow Y$, we have $\dim X = \dim Y$.
:::

::: Proof
If $\varphi$ is finite, then at the level of coordinate rings $\mathbb{K}[X]$ is finitely generated as a module over $\mathbb{K}[Y]$. Hence $\mathbb{K}(X)$ is a finite extension of $\mathbb{K}(Y)$, and the transcendence degrees are equal. That is, $\dim X = \dim Y$.
:::

::: Example 13
A $k$-dimensional linear subspace $L$ of $\mathbb{A}^n$ satisfies $\dim L = k$, because $L \cong \mathbb{A}^k$. Likewise, a $k$-dimensional linear subspace $L$ of $\mathbb{P}^n$ satisfies $\dim L = k$.
:::

::: Example 14
For two varieties $X, Y \subseteq \mathbb{A}^n$ with $X \cap Y \neq \emptyset$, we generally have

$$\dim(X \cap Y) \ge \dim X + \dim Y - n$$

This is called the *dimension inequality*. The inequality is strict in extreme situations such as $X=Y$, where the desired equality can fail. The case of equality is called a *proper intersection*.
:::

---

**References**

**[Har]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.  
**[Hart]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.  
**[AM]** M. F. Atiyah and I. G. Macdonald, *Introduction to Commutative Algebra*, Addison-Wesley, 1969.
