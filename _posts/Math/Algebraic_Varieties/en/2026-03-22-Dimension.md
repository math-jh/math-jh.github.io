---
title: "Dimension"
description: "We examine several equivalent ways to define dimension in algebraic geometry. This covers from the definition as a topological space to the Krull dimension of the coordinate ring of an affine variety."
excerpt: "Dimension of algebraic varieties"

categories: [Math / Algebraic Varieties]
permalink: /en/math/algebraic_varieties/dimension
sidebar: 
    nav: "algebraic_varieties-en"


date: 2026-03-22
weight: 5
translated_at: 2026-08-18T20:15:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-09-23T11:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
Dimension is one of the most fundamental invariants in geometry. In algebraic geometry, dimension is likewise important, and there are several equivalent ways to define it. In this post, we examine various ways to define the dimension of a variety.

## Dimension as a Topological Space

Since an algebraic variety is already a topological space, we can use [\[Topology\] §Dimension, ⁋Definition 10](/en/math/topology/dimension#def10){: data-lid="nsmdr" } to define the dimension of $X$ as the supremum of the lengths of strictly descending chains of irreducible closed subsets.

::: Example 1
For an infinite field $\mathbb{K}$, the only closed subsets in $\mathbb{A}^1$ are all of $\mathbb{A}^1$ and finite sets. Therefore, the longest chain is $\mathbb{A}^1 \supsetneq \{p\}$, and since this is a length $1$ chain, $\mathbb{A}^1$ is $1$-dimensional according to this definition.
:::

This definition has the advantage of defining dimension from a purely topological viewpoint. However, it is not very efficient for actual computation, since one must know all chains of irreducible closed subsets.

## Dimension of an Affine Variety

On the other hand, we already know that an algebraic variety and the functions defined on it are very closely related. Then, it would not be so surprising if the algebraic structure of functions on an algebraic variety contains information about dimension. To approach from this perspective, it would be good to look at the case of *affine* varieties, whose coordinate ring $\mathbb{K}[X]$ is cleanly given.

::: Proposition 2
Over an algebraically closed field $\mathbb{K}$, the dimension of an affine variety $X$ is equal to the Krull dimension of the coordinate ring $\mathbb{K}[X]$. ([\[Commutative Algebra\] §Krull Dimension, ⁋Definition 1](/en/math/commutative_algebra/Krull_dimension#def1){: data-lid="2sksi" })
:::

::: Proof
By [§Affine Varieties, ⁋Proposition 12](/en/math/algebraic_varieties/affine_varieties#prop12){: data-lid="6kcrj" }, there is a one-to-one correspondence between irreducible closed subsets of an affine variety and prime ideals of $\mathbb{K}[X]$.
:::

::: Corollary 3
For an infinite field $\mathbb{K}$, $\dim \mathbb{A}^n = n$.
:::

::: Proof
[\[Commutative Algebra\] §System of Parameters, ⁋Corollary 11](/en/math/commutative_algebra/system_of_parameters#cor11){: data-lid="icc6f" }
:::

Meanwhile, we know that for any prime ideal $\mathfrak{p}\subseteq \mathbb{K}[\x_1,\ldots, \x_n]$, the equation

$$\dim \mathbb{K}[\x_1,\ldots, \x_n]/\mathfrak{p}+\codim \mathfrak{p}=\dim \mathbb{K}[\x_1,\ldots, \x_n]=n\tag{$\ast$}$$

holds. ([\[Commutative Algebra\] §Noether Normalization, ⁋Theorem 4](/en/math/commutative_algebra/noether_normalization#thm4){: data-lid="8xxpv" }) Here, codimension $\mathfrak{p}$ is defined in [\[Commutative Algebra\] §Krull Dimension, ⁋Definition 2](/en/math/commutative_algebra/Krull_dimension#def2){: data-lid="hvv85" } as the supremum of the lengths of chains of prime ideals contained in $\mathfrak{p}$, and geometrically it is the supremum of the lengths of chains of closed subvarieties containing $X=Z(\mathfrak{p})$ in $\mathbb{A}^n$. Geometrically, we know that $\dim \mathbb{K}[\x_1,\ldots, \x_n]/\mathfrak{p}$ is the dimension of $Z(\mathfrak{p})$, so through this we can give a geometric meaning to ($\ast$).

## Dimension of a Projective Variety

The problem arises when passing to projective varieties. Recall that the only global functions on $\mathbb{P}^n$ were constant functions. Since the dimension of a projective variety $X\subseteq \mathbb{P}^n$ is already defined as the dimension of a topological space, the remaining problem is how to compute it, and what comes to mind first in this situation is to take an affine chart. That is, after choosing an affine open chart of $\mathbb{P}^n$, $U_i$, we can consider the dimension of $X_i=X\cap U_i$ as an affine variety. However, to show that this method is valid, one must show that the dimension of any open set is equal to the dimension of the original variety, so we cannot use this yet. Instead, for $X$, we use its *affine cone* $C(X)$.

For a projective variety $X\subseteq \mathbb{P}^n$, the affine cone $C(X)\subseteq \mathbb{A}^{n+1}$ is, when the homogeneous ideal defining $X$ is viewed as an ideal of $\mathbb{K}[\x_0,\ldots, \x_n]$, the affine variety in $\mathbb{A}^{n+1}$ that it defines. That is, for the homogeneous ideal defining $X$, $I(X)$, if we define the ring $S(X)$ by

$$S(X)=\mathbb{K}[\x_0,\ldots, \x_n]/I(X)$$

this becomes the coordinate ring of the affine cone. The key result for computing the dimension of a projective variety is the following.

::: Proposition 4
For a projective variety $X \subseteq \mathbb{P}^n$, $\dim X = \dim S(X) - 1$.
:::

This can be shown through computations in graded rings. In particular, $\dim C(X) = \dim X + 1$, and from this we obtain the following.

::: Proposition 5
$\dim \mathbb{P}^n = n$.
:::

::: Proof
The cone of $\mathbb{P}^n$ is $\mathbb{A}^{n+1}$, and since $\dim \mathbb{A}^{n+1} = n+1$, $\dim \mathbb{P}^n = (n+1) - 1 = n$.
:::

## Dimension of a Hypersurface

A hypersurface is a variety defined as the zero set of a single polynomial. Intuitively, adding one equation is equivalent to imposing one constraint, so it will reduce the dimension by one.

::: Proposition 6
For an algebraically closed field $\mathbb{K}$ and an irreducible polynomial $f \in \mathbb{K}[\x_1, \ldots, \x_n]$ over it, the irreducible hypersurface $Z(f) \subseteq \mathbb{A}^n$ has dimension $n - 1$.
:::

::: Proof
Since $f$ is irreducible, $(f)$ is a prime ideal, and thus the coordinate ring of $Z(f)$ is $\mathbb{K}[\x_1, \ldots, \x_n]/(f)$. Let us now show that the codimension of $(f)$ in $\mathbb{K}[\x_1, \ldots, \x_n]$ is 1. Since $(0) \subsetneq (f)$ is a chain of length 1, we have $\codim(f) \ge 1$. On the other hand, given a prime ideal $\mathfrak{q}$ such that $(0) \subsetneq \mathfrak{q} \subseteq (f)$, when we factor $0 \neq g \in \mathfrak{q}$ in the UFD $\mathbb{K}[\x_1, \ldots, \x_n]$, some irreducible factor $p$ belongs to $\mathfrak{q}$, and from $(p) \subseteq (f)$ we have $f \mid p$, that is, $(f) = (p) \subseteq \mathfrak{q}$, so $\mathfrak{q} = (f)$. Then no other prime ideal can exist between $(0)$ and $(f)$. Therefore $\codim(f) = 1$, and

$$\dim \mathbb{K}[\x_1, \ldots, \x_n]/(f) = \dim \mathbb{K}[\x_1, \ldots, \x_n] - \codim(f) = n - 1$$

holds. Here the first equality follows from [\[Commutative Algebra\] §Noether Normalization, ⁋Theorem 4](/en/math/commutative_algebra/noether_normalization#thm4){: data-lid="cjjne" }.
:::

## Dimension via Function Fields

Another way to define dimension is through the function field. The function field $K(X)$ contains information at the generic point of the variety and is also a birational invariant. The following proposition is also deduced from an algebraic fact. ([\[Commutative Algebra\] §Noether Normalization, ⁋Theorem 3](/en/math/commutative_algebra/noether_normalization#thm3){: data-lid="5a9n3" })

::: Proposition 7
The dimension of a variety $X$ equals the transcendence degree of its function field $K(X)$ over $\mathbb{K}$.
:::

::: Example 8
The following are examples of dimension computations using function fields.

1. $K(\mathbb{A}^n) = \mathbb{K}(\x_1, \ldots, \x_n)$, and since $\x_1, \ldots, \x_n$ are algebraically independent over $\mathbb{K}$, we have $\dim \mathbb{A}^n = n$.
2. $K(V(\y - \x^2)) = \mathbb{K}(\x)$, and since $\x$ is algebraically independent over $\mathbb{K}$, we have $\dim V(\y - \x^2) = 1$. This agrees with the intuition that a parabola is a curve.
3. $K(\mathbb{P}^n) = \mathbb{K}(\x_1/\x_0, \ldots, \x_n/\x_0)$, and since $\x_1/\x_0, \ldots, \x_n/\x_0$ are algebraically independent over $\mathbb{K}$, we have $\dim \mathbb{P}^n = n$. This reflects the fact that projective space is birationally equivalent to affine space.
:::

## Basic Properties of Dimension

The most basic property of dimension is that a proper subset has smaller dimension. This is a geometrically obvious fact.

::: Proposition 9
For a closed subvariety $Y \subsetneq X$ of a variety $X$, we have $\dim Y < \dim X$.
:::

::: Proof
If we consider a maximal chain of closed subvarieties of $Y$

$$Y = Y_0 \supsetneq Y_1 \supsetneq \cdots \supsetneq Y_n \neq \emptyset$$

then, since $X$ is irreducible,

$$X \supsetneq Y = Y_0 \supsetneq Y_1 \supsetneq \cdots \supsetneq Y_n$$

is a chain of closed subvarieties of $X$ of length $n+1$.
:::

This can be thought of as a weak generalization of [Proposition 6](#prop6){: data-lid="6a5ru" }. Applied to a hypersurface $Z(f)\subsetneq \mathbb{A}^n$, it yields only $\dim Z(f)\leq n-1$, so we cannot obtain from this that a single equation drops the dimension by exactly one. Now let us examine the relationship between regular maps and dimension.

::: Proposition 10
For two varieties $X, Y$ and a regular map $\varphi: X \rightarrow Y$, the following hold.

1. $\dim \varphi(X) \le \dim X$ holds.
2. If $\varphi$ is dominant, then $\dim Y \le \dim X$ holds.  ([§Rational Maps, ⁋Definition 8](/en/math/algebraic_varieties/rational_maps#def8){: data-lid="veb7w" })
:::

::: Proof
Let us show the second result first. If $\varphi$ is dominant, the pullback $\varphi^\ast: K(Y)\rightarrow K(X)$ is injective, and therefore we obtain the desired result from [Proposition 7](#prop7){: data-lid="umr3o" }.

The first result follows from this. Since $X$ is irreducible and $\varphi$ is continuous, $\varphi(X)$ is also irreducible; therefore, its closure in $Y$, $\overline{\varphi(X)}$, is a closed subvariety of $Y$. The regular map obtained by restricting the codomain of $\varphi$ to $\overline{\varphi(X)}$ is dominant by definition, so from the second result just shown, we obtain $\dim \overline{\varphi(X)}\leq \dim X$. On the other hand, given a chain of irreducible closed subsets of $\varphi(X)$

$$Z_0 \supsetneq Z_1 \supsetneq \cdots \supsetneq Z_n$$

since each $Z_i$ is a closed subset of $\varphi(X)$, for its closure in $Y$, $\overline{Z_i}$, we have $\overline{Z_i}\cap \varphi(X)=Z_i$, and thus strict inclusions are preserved, so that

$$\overline{Z_0} \supsetneq \overline{Z_1} \supsetneq \cdots \supsetneq \overline{Z_n}$$

is a chain of irreducible closed subsets of $\overline{\varphi(X)}$. Then, since $\dim \varphi(X)\leq \dim \overline{\varphi(X)}$, we obtain the desired result.
:::

The first result supports our intuition that in general, a geometric function cannot increase dimension. The second result shows, roughly speaking, that if $\varphi$ is (up to birational equivalence) surjective, the dimension of the target cannot be higher than the dimension of the domain.

::: Definition 11
For irreducible varieties $X, Y$, a regular map $\varphi: X \rightarrow Y$ is said to be *finite* if for every affine open $U \subseteq Y$, $\varphi^{-1}(U)$ is affine, and $\mathbb{K}[\varphi^{-1}(U)]$ is a finitely generated module over $\mathbb{K}[U]$.
:::

It can be shown that a finite morphism has finite fibers. Concerning dimension, the following holds.

::: Proposition 12
For two varieties $X, Y$ and a finite surjective map $\varphi: X \rightarrow Y$, we have $\dim X = \dim Y$.
:::

::: Proof
If $\varphi$ is finite, at the coordinate ring level $\mathbb{K}[X]$ is finitely generated as a $\mathbb{K}[Y]$-module. Therefore, $K(X)$ is a finite degree extension of $K(Y)$, and their transcendence degrees are equal. That is, $\dim X = \dim Y$.
:::

::: Example 13
In $\mathbb{A}^n$, a $k$-dimensional linear subspace $L$ satisfies $\dim L = k$. This is because $L \cong \mathbb{A}^k$. Likewise, in $\mathbb{P}^n$, a $k$-dimensional linear subspace $L$ satisfies $\dim L = k$.
:::

::: Example 14
When two varieties $X, Y \subseteq \mathbb{A}^n$ satisfy $X \cap Y \neq \emptyset$, in general

$$\dim(X \cap Y) \ge \dim X + \dim Y - n$$

holds. This is called the *dimension inequality*. The reason this is an inequality is that in extreme situations such as, for instance, $X=Y$, the desired equality may not hold. The case where equality holds is called a *proper intersection*.
:::

---

**References**

**[Har]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.  
**[Hart]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.  
**[AM]** M. F. Atiyah and I. G. Macdonald, *Introduction to Commutative Algebra*, Addison-Wesley, 1969.
