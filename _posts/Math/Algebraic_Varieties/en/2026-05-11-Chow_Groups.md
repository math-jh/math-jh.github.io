---
title: "Chow Groups"
description: "This post defines the Chow group, which generalizes the divisor class group on arbitrary varieties, and explains how to extend intersection numbers to any variety using algebraic cycles and rational equivalence."
excerpt: "Chow groups and the cycle class map"

categories: [Math / Algebraic Varieties]
permalink: /en/math/algebraic_varieties/chow_groups
sidebar: 
    nav: "algebraic_varieties-en"

header:
    overlay_image: /assets/images/Math/Algebraic_Varieties/Chow_Groups.png
    overlay_filter: 0.5

date: 2026-05-11
last_modified_at: 2026-05-11
weight: 18
translated_at: 2026-05-30T06:00:03+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-30T06:00:03+00:00
---
Previously, in [§The Riemann–Roch Theorem for Surfaces, ⁋Definition 1](/en/math/algebraic_varieties/riemann_roch_surfaces#def1), we defined the intersection number of two divisors. This is a very interesting notion, and in this post we define the *Chow group* in order to generalize it to arbitrary varieties.

## Chow Groups

In [§Divisors, ⁋Definition 1](/en/math/algebraic_varieties/divisors#def1), we defined a (Weil) divisor as a formal sum of codimension 1 closed irreducible subvarieties, and collected these up to linear equivalence to obtain the divisor class group $$\Cl(X)$$. Similarly, the Chow group is obtained by taking formal sums of $$k$$-dimensional closed irreducible subvarieties up to rational equivalence.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> An *algebraic $$k$$-cycle* on a variety $$X$$ is a formal sum

$$Z = \sum_{i} n_i V_i$$

of $$k$$-dimensional closed irreducible subvarieties of $$X$$. Here each $$V_i \subset X$$ is a $$k$$-dimensional closed irreducible subvariety and $$n_i \in \mathbb{Z}$$. We write $$Z_k(X)$$ for the free abelian group of $$k$$-cycles.

</div>

By definition, an algebraic $$k$$$-cycle is close to homology. When we need to interpret this from the cohomology perspective (via duality), we denote a *codimension $$k$$ cycle* by $$Z^k(X) = Z_{n-k}(X)$$ (where $$n = \dim X$$). As mentioned above, the Chow group is obtained by imposing a specific equivalence relation on these $$Z_k(X)$$.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> Let $$X$$ be a variety, $$Y \subset X$$ a $$(k+1)$$-dimensional closed irreducible subvariety, and $$f \in \mathbb{K}(Y)^\ast$$ a rational function on $$Y$$. The *principal cycle* $$\divisor(f) \in Z_k(X)$$ is defined by the formula

$$\divisor(f) = \sum_{V \subset Y, \dim V = k} v_V(f) \cdot V$$

where $$v_V(f)$$ is the valuation of $$f$$ at $$V$$.

</div>

Intuitively, this definition is nothing more than repeating [§Divisors, ⁋Definition 3](/en/math/algebraic_varieties/divisors#def3) with $$Y$$ as the ambient variety, and is thus the natural generalization of that definition. A somewhat subtle point is the normality mentioned in the introduction of that post: even if $$X$$ is a nice (e.g., normal) variety, an arbitrary subvariety of $$X$$ need not inherit this property, so in this case normalization becomes somewhat more essential. Keeping this in mind, we make the following definition.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> Two $$k$$-cycles $$Z_1, Z_2$$ are *rationally equivalent* if there exist $$(k+1)$$-dimensional closed irreducible subvarieties $$Y_j$$ of $$X$$ and rational functions $$f_j \in \mathbb{K}(Y_j)^\ast$$ on them such that

$$Z_1 - Z_2 = \sum_j \divisor(f_j)$$

We denote this by $$Z_1 \sim_{\text{rat}} Z_2$$.

</div>

That is, just as when defining the divisor class group, we regard two divisors as the same if they differ by a principal divisor. This equivalence relation can be thought of, in the same spirit as the intuition explained right after [§Divisors, ⁋Definition 9](/en/math/algebraic_varieties/divisors#def9), as translating the notion of homotopy into algebraic geometry.

Then the following proposition holds.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> Rational equivalence is an equivalence relation on $$Z_k(X)$$.

</div>

The proof of this is almost a repetition of [§Divisors, ⁋Proposition 8](/en/math/algebraic_varieties/divisors#prop8), so we omit it here. As a consequence of this proposition, we can finally make the following definition.

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> The $$k$$-th *Chow group* $$\CH_k(X)$$ is defined as the group of $$k$$-cycles modulo rational equivalence:

$$\CH_k(X) = Z_k(X) / \sim_{\text{rat}}$$

</div>

The codimension $$k$$ Chow group is defined by $$\CH^k(X) = \CH_{n-k}(X)$$, and is mainly used in situations where the cohomology convention is needed, as mentioned above.

## Functoriality

In algebraic topology, homology and cohomology are functorial for arbitrary continuous maps, but Chow groups are not. Chow groups have pushforward functoriality only for **proper morphisms**, and pullback functoriality only for **flat morphisms**.

First, a morphism $$f: X \to Y$$ between two varieties being a *proper morphism* is roughly the algebraic-geometric analogue of a compact map. ([\[Scheme Theory\] §Valuation Rings, ⁋Definition 8](/en/math/scheme_theory/valuative_criteria#def8)) One must be careful, however: compactness does not work well in algebraic geometry, so we cannot translate it directly. The intuition is that, just as the fibers and image of a compact map do not escape to infinity, the same holds for a proper morphism; in particular, what matters is that only finitely many additional coordinates are needed to describe each fiber. ([\[Scheme Theory\] §Properties of Scheme Morphisms, ⁋Example 15](/en/math/scheme_theory/properties_of_scheme_morphisms#ex15)) The number of coordinates needed is computed by the extension degree of function fields $$[\mathbb{K}(V):\mathbb{K}(f(V))]$$, which is defined when $$V$$ and $$f(V)$$ have the same dimension. For convenience, writing

$$\deg(V/f(V))=\begin{cases}[\mathbb{K}(V):\mathbb{K}(f(V))]&\text{if $\dim f(V)=\dim V$,}\\ 0&\text{if $\dim f(V)<\dim V$}\end{cases}$$

the following holds.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> For a proper morphism $$f: X \to Y$$, there exists a pushforward $$f_\ast: \CH_k(X) \to \CH_k(Y)$$. In particular, for any subvariety $$V\subset X$$,

$$f_\ast[V]=\deg(V/f(V))[f(V)]$$

holds.

</div>

That is, intuitively, if an algebraic cycle $$[V]$$ is mapped to $$[f(V)]$$ with degree $$d$$ via a proper morphism $$f$$, then $$f_\ast[V]$$ captures precisely this degree.

Now we examine pullback. Since this is closer to the cohomology convention than the homology convention, we consider the codimension $$k$$ Chow group. The pullback $$f^\ast: \CH^k(Y)\rightarrow \CH^k(X)$$ can be thought of intuitively as taking a cycle on the target $$Y$$ and stretching it in the fiber direction to give a cycle on the source. For this to be well defined, the dimension of the fiber over each point of $$Y$$ must be constant, and moreover the structure of the fiber must not change abruptly as the parameter varies over $$Y$$. A *flat morphism* is precisely the morphism reflecting these properties, and in this case we obtain the following proposition.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> For a flat morphism $$f: X \to Y$$, there exists a pullback $$f^\ast: \CH^k(Y) \to \CH^k(X)$$. For a subvariety $$V \subset Y$$, we have $$f^\ast[V] = [f^{-1}(V)]$$.

</div>

## Computing Chow Groups

We have seen two kinds of functoriality so far, and using them together allows us to better understand the structure of Chow groups. For example, let $$Z \subset X$$ be a closed subvariety and let $$U = X \setminus Z$$. Then $$i: Z \hookrightarrow X$$ is a closed embedding, hence a proper morphism, and so the pushforward $$i_\ast$$ is defined. On the other hand, $$j: U \hookrightarrow X$$ is an open embedding, hence a flat morphism, and so the pullback $$j^\ast$$ is defined.

One thing to note here is that the pullback $$j^\ast$$ is originally a contravariant operation defined for the cohomology convention $$\CH^k$$. However, in the case of an open embedding, $$U$$ has the same dimension as $$X$$, so restricting a $$k$$-dimensional cycle directly to $$U$$ is naturally defined.

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8 (Localization Exact Sequence)**</ins> If $$Z \subset X$$ is a closed subvariety and $$U = X \setminus Z$$, then the following exact sequence holds:

$$\operatorname{CH}_k(Z) \xrightarrow{i_\ast} \operatorname{CH}_k(X) \xrightarrow{j^\ast} \operatorname{CH}_k(U) \to 0$$

where $$i: Z \hookrightarrow X$$ is the closed embedding and $$j: U \hookrightarrow X$$ is the open embedding.

</div>

The reason this exact sequence holds is as follows. First, the surjectivity of $$j^\ast$$ is obvious. More important is that $$\ker j^\ast = \im i_\ast$$, which means that cycles disappearing in $$U$$ must be cycles supported along $$Z$$, and this is obvious since $$U$$ is defined as $$X\setminus Z$$.

The following example serves as a basic starting point for computing various Chow groups.

<div class="example" markdown="1">

<ins id="ex9">**Example 9**</ins> As the most basic example,

$$\CH_k(\mathbb{A}^n)=\begin{cases}\mathbb{Z}&\text{if $k=n$}\\0&\text{otherwise}\end{cases}$$

and

$$\CH_k(\mathbb{P}^n)=\mathbb{Z}\qquad\text{for all $0\leq k\leq n$}$$

hold. This matches the homology of Euclidean space and projective space, showing that the Chow group we defined actually reflects geometric intuition well.

</div>

In general,

<div class="example" markdown="1">

<ins id="ex10">**Example 10**</ins> To see the above example more intuitively, define a degree $$d$$ morphism $$f: \mathbb{P}^1 \to \mathbb{P}^1$$ by

$$f([x:y]) = [x^d:y^d]$$

This is proper, and for the coordinate $$t = x/y$$ on $$\mathbb{P}^1$$ we have $$f^\ast(t) = t^d$$, so the field extension $$\mathbb{K}(\mathbb{P}^1) \hookrightarrow \mathbb{K}(\mathbb{P}^1)$$ is given by $$t \mapsto t^d$$, and the extension degree in this case is $$d$$. Therefore, by [Proposition 6](#prop6),

$$f_\ast[\mathbb{P}^1] = d \cdot [\mathbb{P}^1] \in \CH_1(\mathbb{P}^1) \cong \mathbb{Z}$$

holds. That is, $$\mathbb{P}^1$$ is covered by $$\mathbb{P}^1$$ with $$d$$ sheets, and the pushforward captures this.

</div>

By definition, the following proposition is almost obvious.

<div class="proposition" markdown="1">

<ins id="prop11">**Proposition 11**</ins> For a smooth variety $$X$$,

$$\CH^1(X) \cong \Cl(X) \cong \Pic(X)$$

holds.

</div>

Also, in [Example 9](#ex9) we saw that the cases of $$\mathbb{A}^n$$ and $$\mathbb{P}^n$$ match classical computations, and this can be formulated rigorously as follows.

<div class="proposition" markdown="1">

<ins id="prop12">**Proposition 12**</ins> For a complex variety $$X$$, there exists a *cycle class map*

$$\cl: \CH_k(X) \to H^{\text{BM}}_{2k}(X, \mathbb{Z})$$

This is a map that interprets algebraic cycles topologically, and if $$X$$ is smooth projective, then by Poincaré duality it can be viewed as $$\cl: \CH^k(X) \to H^{2k}(X, \mathbb{Z})$$.

</div>

Here $$H^{\text{BM}}$$ on the right-hand side is Borel–Moore homology, which unlike singular homology allows us to view a closed oriented submanifold (in the non-compact situation) as a class in Borel–Moore homology. From this perspective, we can see that Borel–Moore homology is a slightly better analogue of our Chow group than singular cohomology. Also, since $$X$$ is a complex variety, the dimension on the right-hand side doubles to become $$2k$$, which is worth noting.

## Chow Ring

We conclude this post by introducing the following proposition as motivation for introducing the intersection product.

<div class="proposition" markdown="1">

<ins id="prop13">**Proposition 13**</ins> For a smooth variety $$X$$, $$\CH^\ast(X) = \bigoplus_k \CH^k(X)$$ forms a graded ring under the intersection product. ([§Intersection Product](/en/math/algebraic_varieties/intersection_product))

</div>

This ring structure also matches the cohomology ring structure we already knew, just as in [Proposition 12](#prop12).

<div class="example" markdown="1">

<ins id="ex14">**Example 14 ($$\mathbb{P}^n$$)**</ins> $$\CH^\ast(\mathbb{P}^n) \cong \mathbb{Z}[H] / (H^{n+1})$$

Here $$H$$ is the hyperplane class. $$H^k$$ represents a $$k$$-codimensional linear subspace.

</div>

The intersection product of [Proposition 13](#prop13) will be introduced rigorously in the next post.

---

**References**

**[Ful]** W. Fulton, *Intersection Theory*, Springer, 1984.  
**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.
