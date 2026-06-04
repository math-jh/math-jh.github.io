---
title: "Line Bundles and Vector Bundles"
description: "A line bundle on a manifold assigns a one-dimensional vector space to each point, allowing arbitrary parameters to be handled independently without asymptotic constraints. This article begins with the definition of a line bundle and extends it to vector bundles."
excerpt: "Line bundles, invertible sheaves, and the Picard group"

categories: [Math / Algebraic Varieties]
permalink: /en/math/algebraic_varieties/line_bundles
sidebar:
    nav: "algebraic_varieties-en"


date: 2026-03-25
last_modified_at: 2026-04-08
weight: 9
translated_at: 2026-05-30T03:45:31+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-30T03:45:31+00:00
---
In previous posts we defined divisors on a variety $$X$$ and saw that their linear equivalence classes form $$\Cl(X)$$. However, not every divisor arises as the zero or pole locus of a rational function. For example, since $$\Cl(\mathbb{P}^n) \cong \mathbb{Z}$$ ([§Divisors, ⁋Example 11](/en/math/algebraic_varieties/divisors#ex11)), a general divisor $$dH$$ on $$\mathbb{P}^n$$ is the zero set of a function only when $$d \ge 0$$.

To overcome this restriction we introduce the notion of a *line bundle*. A line bundle $$\mathcal{L}$$ is a geometric object that assigns a one-dimensional vector space to each point $$p \in X$$, and a section $$s$$ of $$\mathcal{L}$$ naturally defines a divisor $$\divisor(s)$$. From this viewpoint, for any divisor $$D$$ we can construct a line bundle $$\mathcal{O}_X(D)$$ whose sections correspond to divisors greater than or equal to $$D$$. In other words, line bundles let us treat divisors independently of the constraint that they be zeros or poles of functions.

## Definition of a Line Bundle

Line bundles, and more generally vector bundles which we define later in this post, are defined in the same way as in differential geometry and other fields. ([\[Manifolds\] §Tangent and Cotangent Bundles, ⁋Definition 1](/en/math/manifold/tangent_and_cotangent_bundles#def1) or [\[Algebraic Topology\] §Characteristic Classes, ⁋Definition 2](/en/math/algebraic_topology/characteristic_classes#def2), etc.)

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A *line bundle* $$\mathcal{L}$$ over a variety $$X$$ consists of the following data.

1. A projection $$\pi: \mathcal{L} \to X$$.
2. An open cover $$\{U_i\}$$ of $$X$$ and, for each $$i$$, a *local trivialization* $$\phi_i: \pi^{-1}(U_i) \overset{\sim}{\longrightarrow} U_i \times \mathbb{A}^1$$. The maps

    $$\phi_j \circ \phi_i^{-1}: (U_i \cap U_j) \times \mathbb{A}^1 \to (U_i \cap U_j) \times \mathbb{A}^1$$

    have the form $$(p, t) \mapsto (p, g_{ij}(p)t)$$ for suitable *transition functions* $$g_{ij} \in \mathcal{O}_X(U_i \cap U_j)^\ast$$.

</div>

A *morphism* $$\varphi \colon \mathcal{L} \to \mathcal{M}$$ between two line bundles $$\mathcal{L}, \mathcal{M} \to X$$ defines a $$\mathbb{K}$$-linear map $$\varphi_p \colon \mathcal{L}_p \to \mathcal{M}_p$$ on each fiber, and over a suitable open cover $$\{U_k\}$$ it can be expressed as an $$\mathcal{O}_X(U_k)$$-module homomorphism

$$\varphi_k \colon \mathcal{O}_{U_k} \to \mathcal{O}_{U_k}$$

satisfying

$$g^{\mathcal{M}}_{kl} \circ \varphi_l = \varphi_k \circ g^{\mathcal{L}}_{kl}.$$

Since the fiber of a line bundle is one-dimensional, each $$\varphi_k$$ is given by multiplication by some $$h_k \in \mathcal{O}_X(U_k)$$, i.e. $$s \mapsto h_k s$$. When $$\varphi$$ is bijective on every fiber, we call it an *isomorphism* and write $$\mathcal{L} \cong \mathcal{M}$$. Because the fiber is one-dimensional, this is equivalent to giving a nonzero scalar at each point, i.e. to choosing $$h_k \in \mathcal{O}_X(U_k)^\ast$$ compatibly.

The following proposition follows directly from the definition of the cocycle condition.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2 (Cocycle condition)**</ins> The transition functions $$\{g_{ij}\}$$ satisfy the following *cocycle condition*.

1. $$g_{ii} = 1$$ for all $$i$$.
2. $$g_{ij} = g_{ji}^{-1}$$ for all $$i, j$$.
3. $$g_{ij} g_{jk} = g_{ik}$$ on $$U_i \cap U_j \cap U_k$$ for all $$i, j, k$$.

</div>

<div class="example" markdown="1">

<ins id="ex3">**Example 3**</ins> The *trivial line bundle* $$X \times \mathbb{A}^1$$ is the line bundle all of whose transition functions are $$g_{ij} = 1$$. This is the simplest line bundle, with no twist.

</div>

Thus the second condition in [Definition 1](#def1) means that the line bundle $$\mathcal{L}$$ becomes isomorphic to the trivial line bundle when restricted to a suitable open subset $$U \subseteq X$$.

[Proposition 2](#prop2) is the usual gluing condition, and by virtue of it a line bundle can be thought of as a kind of sheaf. ([\[Topology\] §Sheaves, ⁋Definition 1](/en/math/topology/sheaves#def1)) Concretely, given a line bundle $$\mathcal{L}$$, we define its sheaf of sections by

$$U\mapsto \mathcal{O}_X(\mathcal{L})(U)=\{s: U \to \mathcal{L} \mid \pi \circ s = \id_U\}.$$

That is, $$\mathcal{O}_X(\mathcal{L})$$ is the sheaf of sections of the surjection $$\pi$$. ([\[Topology\] §Sheaves, ⁋Example 9](/en/math/topology/sheaves#ex9))

Then by the local trivialization $$\phi_i: \pi^{-1}(U_i) \to U_i \times \mathbb{A}^1$$ we have $$\mathcal{O}_X(\mathcal{L})\vert_{U_i} \cong \mathcal{O}_{U_i}$$. Hence over $$U_i$$ we may regard these sections locally as ordinary $$\mathbb{K}$$-valued functions.

This means the following.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> A sheaf $$\mathcal{F}$$ is called *invertible* if for every point $$p \in X$$ there is a neighborhood $$U$$ such that $$\mathcal{F}\vert_U \cong \mathcal{O}_U$$.

</div>

What we showed above is that the sheaf of sections of a line bundle is invertible. The next proposition shows that the converse also holds.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> The sheaf of sections $$\mathcal{O}_X(\mathcal{L})$$ of a line bundle $$\mathcal{L}$$ is an invertible sheaf. Conversely, every invertible sheaf comes from a unique line bundle.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

For an invertible sheaf $$\mathcal{F}$$, one can define transition functions from the local isomorphisms $$\mathcal{F}\vert_{U_i} \cong \mathcal{O}_{U_i}$$, and reconstruct a line bundle from them.

</details>

By this proposition we know that line bundles and invertible sheaves are the same concept. For this reason, when denoting a line bundle we use $$\mathcal{L}$$ rather than the upright $$L$$ used to denote a space.

## Operations on Line Bundles

In differential geometry it is natural to construct new bundles by performing fiberwise linear-algebraic operations. The same is true in algebraic geometry; since we are currently looking at line bundles, the operations we need to examine are $$\otimes$$ and $$\Hom$$, and in particular the dual $$(-)^\vee$$.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> The tensor product $$\mathcal{L} \otimes \mathcal{M}$$ of two line bundles $$\mathcal{L}, \mathcal{M}$$ is again a line bundle. Its transition functions are $$\{g_{ij} h_{ij}\}$$, where $$\{g_{ij}\}, \{h_{ij}\}$$ are the transition functions of $$\mathcal{L}, \mathcal{M}$$ respectively.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

The fiber of the tensor product is $$\mathcal{L}_p \otimes_{\mathbb{K}} \mathcal{M}_p$$, which is again one-dimensional since it is the tensor product of two one-dimensional vector spaces. The transition function is the product of $$\phi_j \circ \phi_i^{-1}$$ and $$\psi_j \circ \psi_i^{-1}$$, hence $$g_{ij} h_{ij}$$.

</details>

For any line bundle $$\mathcal{L}$$, the dual bundle $$\mathcal{L}^\vee$$ is the bundle whose fibers are

$$\mathcal{L}_x^\vee=\Hom_\mathbb{K}(\mathcal{L}_x, \mathbb{K}).$$

If we think of line bundles as (invertible) sheaves following [Proposition 5](#prop5), then $$\mathcal{L}^\vee$$ corresponds to the sheaf Hom $$\sHom_{\mathcal{O}_X}(\mathcal{L}, \mathcal{O}_X)$$.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> The *dual bundle* $$\mathcal{L}^\vee$$ of a line bundle $$\mathcal{L}$$ is also a line bundle, and its transition functions are $$\{g_{ij}^{-1}\}$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

The fiber of the dual bundle is $$\mathcal{L}_p^\vee = \Hom_{\mathbb{K}}(\mathcal{L}_p, \mathbb{K})$$, which is again one-dimensional since it is the dual of a one-dimensional vector space. The transition function is the inverse of $$g_{ij}$$.

</details>

The next proposition shows the relationship between $$\otimes$$ and $$(-)^\vee$$, which plays an important role in defining the Picard group.

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8**</ins> For any line bundle $$\mathcal{L}$$ we have $$\mathcal{L} \otimes \mathcal{L}^\vee \cong \mathcal{O}_X$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

The transition functions of $$\mathcal{L} \otimes \mathcal{L}^\vee$$ are $$g_{ij} \cdot g_{ij}^{-1} = 1$$, so it is the trivial bundle.

</details>

As always, we can understand the structure of a line bundle by looking at it over a sufficiently small affine open set. Consider a line bundle $$\mathcal{L}$$ and choose an affine open subset $$U_i$$ over which $$\mathcal{L}$$ is trivial. Then the projection map

$$\pi\vert_{\pi^{-1}(U_i)}:\pi^{-1}(U_i) \rightarrow U_i$$

is a morphism of affine varieties, and hence induces a ring homomorphism between coordinate rings by [§Affine Varieties, ⁋Proposition 16](/en/math/algebraic_varieties/affine_varieties#prop16). This ring homomorphism makes the coordinate ring of $$\pi^{-1}(U_i)$$ into a module over the coordinate ring of $$U_i$$, and considering dimensions we see that its rank is 1. Since $$\mathcal{L}$$ is trivial over any open subset of $$U_i$$, we can verify that a line bundle becomes an invertible module over the coordinate ring affine-locally. ([\[Commutative Algebra\] §Fractional Ideals, ⁋Definition 1](/en/math/commutative_algebra/fractional_ideals#def1)) Then the operations $$\otimes$$ and $$\vee$$ defined on line bundles come from the operations in [\[Commutative Algebra\] §Fractional Ideals, ⁋Theorem 3](/en/math/commutative_algebra/fractional_ideals#thm3), and therefore it is natural to adopt the following name following [\[Commutative Algebra\] §Fractional Ideals, ⁋Definition 5](/en/math/commutative_algebra/fractional_ideals#def5).

<div class="definition" markdown="1">

<ins id="def9">**Definition 9**</ins> The *Picard group* $$\Pic(X)$$ of a variety $$X$$ is the group obtained by taking the set of isomorphism classes of line bundles over $$X$$ with tensor product as the group operation. The identity element is the trivial bundle $$\mathcal{O}_X$$, and the inverse of $$\mathcal{L}$$ is $$\mathcal{L}^\vee$$.

</div>

That the trivial bundle actually serves as the identity is verified directly by [Example 3](#ex3) and [Proposition 6](#prop6). Moreover, the following holds by the properties of the tensor product.

<div class="proposition" markdown="1">

<ins id="prop10">**Proposition 10**</ins> $$\Pic(X)$$ is an abelian group.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

By [Proposition 6](#prop6) the tensor product is a binary operation on line bundles, and by [Proposition 8](#prop8) $$\mathcal{O}_X$$ is the identity and $$\mathcal{L}^\vee$$ is the inverse of $$\mathcal{L}$$. The commutativity $$\mathcal{L} \otimes \mathcal{M} \cong \mathcal{M} \otimes \mathcal{L}$$ and associativity $$(\mathcal{L} \otimes \mathcal{M}) \otimes \mathcal{N} \cong \mathcal{L} \otimes (\mathcal{M} \otimes \mathcal{N})$$ follow directly at the level of transition functions from $$g_{ij}h_{ij} = h_{ij}g_{ij}$$ and $$(g_{ij}h_{ij})k_{ij} = g_{ij}(h_{ij}k_{ij})$$.

</details>

As in previous posts, our toy examples are $$\mathbb{A}^n$$ and $$\mathbb{P}^n$$.

<div class="example" markdown="1">

<ins id="ex11">**Example 11**</ins> The coordinate ring $$R = \mathbb{K}[\x_1, \ldots, \x_n]$$ of $$\mathbb{A}^n$$ is a UFD, and by the above discussion line bundles over $$\mathbb{A}^n$$ correspond to invertible modules over $$R$$. By ([\[Commutative Algebra\] §Fractional Ideals, ⁋Theorem 4](/en/math/commutative_algebra/fractional_ideals#thm4)) invertible modules over a UFD are free, so $$\Pic(\mathbb{A}^n) = 0$$.

</div>


<div class="example" markdown="1">

<ins id="ex12">**Example 12**</ins> We define the line bundle $$\mathcal{O}_{\mathbb{P}^n}(d)$$ on $$\mathbb{P}^n$$ as follows. First, the standard open cover

$$U_i = \{[x_0 : \cdots : x_n] \mid x_i \ne 0\}$$

gives trivializing open sets for this bundle. We explicitly define the trivialization over each of them by

$$\phi_i\colon \mathcal{O}(d)\vert_{U_i} \xrightarrow{\sim} \mathcal{O}_{U_i}, \qquad \phi_i(s) = s \cdot \x_i^{-d}.$$

From this we know that the space of sections has the form

$$\mathcal{O}(d)(U_i) = \x_i^d \cdot \mathcal{O}(U_i) = \x_i^d\mathbb{K}[\x_0/\x_i, \ldots, \widehat{\x_i/\x_i}, \ldots, \x_n/\x_i].$$

Now comparing the two trivializations over $$U_i \cap U_j$$ we can derive the transition function. That is, the transition function $$\phi_i \circ \phi_j^{-1}\colon \mathcal{O}_{U_j}\vert_{U_i \cap U_j} \to \mathcal{O}_{U_i}\vert_{U_i \cap U_j}$$ satisfies

$$\phi_i \circ \phi_j^{-1}(f) = (\x_i/\x_j)^d \cdot f,$$

so we obtain $$g_{ij} = (\x_i/\x_j)^d$$. More concretely, for each point $$x \in U_i \cap U_j$$ and fiber $$v \in \mathcal{O}_{\mathbb{P}^n}(d)_x \cong \mathbb{A}^1$$ at that point,

$$g_{ij}(x)\colon v \mapsto (\x_i/\x_j)^d(x) \cdot v.$$

We can now define the group homomorphism

$$\mathbb{Z}\rightarrow \Pic(\mathbb{P}^n);\qquad d\mapsto [\mathcal{O}_{\mathbb{P}^n}(d)].$$

Our claim is that this is an isomorphism. First, for any line bundle $$\mathcal{L}$$, $$\mathcal{L}\vert_{U_i}$$ is isomorphic to the trivial line bundle by [Example 11](#ex11), so the transition functions $$h_{ij}$$ on each $$U_i\cap U_j$$ completely determine $$\mathcal{L}$$. But by definition $$h_{ij}\in \mathcal{O}_{\mathbb{P}^n}(U_i\cap U_j)^\ast$$ on $$U_i\cap U_j$$, so $$h_{ij}$$ must have the form $$c_{ij}(\x_i/\x_j)^d$$. Since line bundles whose transition functions differ by a constant factor are trivial, we see from this that the above group homomorphism is surjective. Similarly, assuming $$\mathcal{O}_{\mathbb{P}^n}(d)\cong \mathcal{O}_{\mathbb{P}^n}(d')$$ and comparing transition functions,

$$\mathcal{O}_{\mathbb{P}^n}(d-d')\cong \mathcal{O}_{\mathbb{P}^n}(d)\otimes \mathcal{O}_{\mathbb{P}^n}(-d')\cong \mathcal{O}_{\mathbb{P}^n}(d)\otimes \mathcal{O}_{\mathbb{P}^n}(d')^\vee\cong \mathcal{O}_{\mathbb{P}^n}$$

requires $$d-d'=0$$, so it is also injective.

</div>

Intuitively, the integer $$d$$ in the line bundle $$\mathcal{O}_{\mathbb{P}^n}(d)$$ on $$\mathbb{P}^n$$ can be understood as a measure of how many times the fiber twists as it moves along the base. When $$d=0$$, $$\mathcal{O}(0)$$ is the trivial bundle so there is no twist; when $$d>0$$ it twists $$d$$ times in one direction, and when $$d<0$$ it twists $$\lvert d\rvert$$ times in the opposite direction. This means that $$d$$ directly indicates the amount of twisting in the transition function $$g_{ij}(x) = (x_i/x_j)^d(x)$$. However, this intuition may be somewhat imprecise, so we will supplement it with additional explanation after [Example 16](#ex16).

On the other hand, there is a special line bundle on projective space $$\mathbb{P}^n$$ that arises naturally from its very definition. This *tautological bundle* is the bundle that assigns to each point of $$\mathbb{P}^n$$ the line represented by that point, and it plays a fundamental role in understanding the geometry of projective space.

<div class="definition" markdown="1">

<ins id="def13">**Definition 13**</ins> Each point $$x = [x_0 : \cdots : x_n]$$ of $$\mathbb{P}^n$$ corresponds to the line $$\ell_x = \{(\lambda x_0, \ldots, \lambda x_n) \mid \lambda \in \mathbb{K}\}$$ passing through the origin in $$\mathbb{A}^{n+1}$$. Consider the space

$$\mathcal{O}_{\mathbb{P}^n}(-1) = \{(x, v) \in \mathbb{P}^n \times \mathbb{A}^{n+1} \mid v \in \ell_x\}$$

with the projection map $$\pi=\pr_1$$ from $$\mathcal{O}_{\mathbb{P}^n}(-1)$$ to $$\mathbb{P}^n$$. The line bundle defined by this projection is called the *tautological line bundle* on $$\mathbb{P}^n$$.

</div>

That is, in this definition each fiber $$\mathcal{O}_{\mathbb{P}^n}(-1)_x$$ is the line represented by the point $$x$$ itself. As the notation suggests, the following holds. For distinction, in the next proposition only, let us regard $$\mathcal{O}_{\mathbb{P}^n}(-1)$$ as the bundle from [Definition 13](#def13), not [Example 12](#ex12).

<div class="proposition" markdown="1">

<ins id="prop14">**Proposition 14**</ins> The tautological bundle $$\mathcal{O}_{\mathbb{P}^n}(-1)$$ is the dual of $$\mathcal{O}_{\mathbb{P}^n}(1)$$ defined in [Example 12](#ex12) above. That is, $$\mathcal{O}_{\mathbb{P}^n}(-1) \cong \mathcal{O}_{\mathbb{P}^n}(1)^\vee$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Let us construct a local trivialization of $$\mathcal{O}_{\mathbb{P}^n}(-1)$$ over the standard open cover $$U_i = \{x \mid x_i \ne 0\}$$. For any $$(x, v) \in \mathcal{O}_{\mathbb{P}^n}(-1)$$ we can write $$v = \lambda x$$ ($$\lambda \in \mathbb{K}$$), so defining $$\phi_i(x, v) = (x, v_i)$$ gives $$\phi_i: \pi^{-1}(U_i) \to U_i \times \mathbb{A}^1$$. The inverse is $$\phi_i^{-1}(x, t) = (x, (t/x_i)\, x)$$. The transition function on $$U_i \cap U_j$$ is obtained from $$\phi_j \circ \phi_i^{-1}(x, t) = (x, t x_j / x_i)$$ as $$g_{ij}(x) = x_j/x_i$$. This is the inverse of the transition function $$x_i/x_j$$ of $$\mathcal{O}_{\mathbb{P}^n}(1)$$.

</details>

In particular, examining $$\mathcal{O}(-1)$$ on $$\mathbb{P}^1$$ makes the meaning of the *twisting* described intuitively above much clearer. The process of forming $$\mathbb{P}^1$$ from $$\mathbb{A}^2\setminus \{0\}$$ can be thought of as first radially projecting $$\mathbb{A}^2\setminus\{0\}$$ onto the unit circle and then identifying antipodal points on the unit circle; in this process, the identification of vectors in opposite directions—that is, the twisting of fibers—occurs. One way to detect this twisting is to look at sections of the line bundle $$\mathcal{L}$$.

<div class="definition" markdown="1">

<ins id="def15">**Definition 15**</ins> We denote the space of *global sections* of a line bundle $$\mathcal{L}$$ by $$\Gamma(X, \mathcal{L})$$. That is, $$\Gamma(X, \mathcal{L})$$ is the set of regular maps assigning to each point $$x\in X$$ an element of the fiber $$\pi^{-1}(x)\subset \mathcal{L}$$.

</div>

Another common notation for the space of global sections is $$H^0(X, \mathcal{L})$$. This notation will be justified in [§Sheaf Cohomology, ⁋Definition 1](/en/math/algebraic_varieties/sheaf_cohomology#def1), but until then we will use $$\Gamma(X, \mathcal{L})$$.

<div class="example" markdown="1">

<ins id="ex16">**Example 16**</ins> The only global section of $$\mathcal{O}_{\mathbb{P}^n}(-1)$$ is $$0$$. That is,

$$\Gamma(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n}(-1)) = 0.$$

To verify this, by [Example 12](#ex12) we have $$\mathcal{O}(-1)(U_i) = \x_i^{-1} \cdot \mathbb{K}[\x_0/\x_i, \ldots, \widehat{\x_i/\x_i}, \ldots, \x_n/\x_i]$$, and the trivialization is given by $$\phi_i(s) = s \cdot \x_i$$. Hence the trivialized section $$\phi_i(s)$$ lies in $$\mathcal{O}(U_i) = \mathbb{K}[\x_0/\x_i, \ldots, \x_n/\x_i]$$, and on $$U_i \cap U_j$$ the cocycle condition requires

$$\phi_j(s) = (\x_j/\x_i)\, \phi_i(s).$$

But $$\phi_i(s) \in \mathbb{K}[\x_0/\x_i, \ldots, \widehat{\x_i/\x_i}, \ldots, \x_n/\x_i]$$ cannot contain a term $$\x_i/\x_j$$, so for $$(\x_j/\x_i)\, \phi_i(s)$$ to lie in $$\mathcal{O}(U_j) = \mathbb{K}[\x_0/\x_j, \ldots, \widehat{\x_j/\x_j}, \ldots, \x_n/\x_j]$$ we must have $$\phi_i(s) = 0$$. Therefore $$s = 0$$.

</div>

This proposition shows the twisting of the tautological bundle from the viewpoint of sections. For instance, the fact that $$\Gamma(\mathbb{P}^1, \mathcal{O}(-1))=0$$ means in particular that there is not even a "constant function" assigning 1 in the fiber to every $$x\in \mathbb{P}^1$$. From the geometric viewpoint above, this is because when we go around $$\mathbb{P}^1$$ once, the original 1 becomes (for example) $$-1$$.

Meanwhile, the computation in [Example 16](#ex16) can be extended to arbitrary $$d$$; in particular, for any $$d<0$$ we can show $$\Gamma(\mathbb{P}^1, \mathcal{O}(d))=0$$ by the same logic, and for $$d=0$$, i.e. $$\mathcal{O}_{\mathbb{P}^n}(0)=\mathcal{O}_{\mathbb{P}^n}$$, we can verify that the sections are homogeneous polynomials of degree $$0$$, i.e. constant functions, so the computation in [§Quasi-Projective Varieties, ⁋Example 6](/en/math/algebraic_varieties/quasi_projective_varieties#ex6) is confirmed again.

The case to pay attention to is $$d>0$$. In this case, by exactly the same computation as in [Example 16](#ex16), we can verify that the sections are homogeneous polynomials of degree $$d$$. In particular $$\Gamma(\mathbb{P}^n, \mathcal{O}(d))\neq 0$$, which we may think of as a computation showing that the intuition after [Example 12](#ex12) was somewhat overly simplified.

A more accurate explanation of this phenomenon is as follows. For convenience let us look at the example on $$\mathbb{P}^1$$. The sections of $$\mathcal{O}(-1)$$ are homogeneous of degree $$-1$$, so in particular they have the form

$$s([x_0:x_1])=\frac{a}{x_0}+\frac{b}{x_1},$$

and for this function to be defined on all of $$\mathbb{P}^1$$ we must have $$a=b=0$$. On the other hand, the sections of $$\mathcal{O}(1)$$ are homogeneous polynomials of degree $$1$$, so they are functions of the form

$$s([x_0:x_1])=ax_0+bx_1$$

with no restriction on $$a,b$$. Intuitively, the sections of $$\mathcal{O}(-1)$$ cannot cross the zero section because of the denominators, so every section is forced to encounter the problem created by the twisting of "1 attaching to $$-1$$". This twisting creates the same problem in $$\mathcal{O}(1)$$ as well. That is, the "constant section" $$s([x_0:x_1])$$ is not a section in $$\mathcal{O}(1)$$ either. However, this time the sections of $$\mathcal{O}(1)$$ can cross the zero section, so we get $$\Gamma(\mathbb{P}^1, \mathcal{O}(1))\neq 0$$. From the viewpoint of transition functions or trivializations, we may think that $$\mathcal{O}(d)$$ multiplies by the degree $$d$$ polynomial $$\x_i^d$$, so poles of degree at most $$d$$ can be erased by this trivialization.

## Divisor–Line Bundle Correspondence

We now establish the essential connection between divisors and line bundles. First we show that a line bundle can be constructed from a Cartier divisor.

<div class="definition" markdown="1">

<ins id="def17">**Definition 17**</ins> For a Cartier divisor $$D = \{(U_i, f_i)\}$$, we define the line bundle $$\mathcal{O}_X(D)$$ by the transition functions $$g_{ij} = f_i/f_j$$.

</div>

That is, we take trivial bundles over the $$U_i$$ and glue them together over each overlap using exactly the information contained in the Cartier divisor. If we view $$\mathcal{O}_X(D)$$ as a sheaf—that is, consider the sheaf of sections of the line bundle defined above—then over each open set $$U$$ the sheaf $$\mathcal{O}_X(D)(U)$$ consists of (as a sheaf) functions satisfying

$$\divisor(f)+D\geq 0.$$

That is, $$\mathcal{O}_X(D)$$ is the sheaf of rational functions that may have poles of order at most $$1$$ along $$D$$, if we view $$D$$ as a codimension-$$1$$ subvariety of $$X$$. Conversely, $$\mathcal{O}_X(-D)$$ is given by

$$\divisor(f)-D\geq 0,$$

which is exactly the sheaf of functions vanishing on $$D$$. That is,

$$\mathcal{O}_X(-D)(U)=\{f\in \mathcal{O}_X(U)\mid \text{$f$ vanishes on $D\cap U$}\},$$

and from this we obtain the short exact sequence

$$0\rightarrow \mathcal{O}_X(-D)\rightarrow \mathcal{O}_X\rightarrow \mathcal{O}_D\rightarrow 0.$$

Then $$\mathcal{O}_X(-D)$$ is the sheaf of ideals defining $$D$$, and for this reason we denote it by $$\mathcal{I}_D$$ and call it the *ideal sheaf*.

<div class="proposition" markdown="1">

<ins id="prop18">**Proposition 18**</ins> The above definition is well-defined. That is, equivalent Cartier divisors define isomorphic line bundles.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

If two Cartier divisors $$\{(U_i, f_i)\}$$ and $$\{(V_j, g_j)\}$$ are equivalent, then $$f_i/g_j \in \mathcal{O}_X(U_i \cap V_j)^\ast$$. The transition functions of the line bundles defined by them are compatible, so they define isomorphic line bundles.

</details>

For example, for any principal divisor $$\divisor(f)$$ the transition function is $$1$$, so it becomes the trivial bundle. We now summarize the relationship between line bundles and Cartier divisors.

<div class="proposition" markdown="1">

<ins id="prop19">**Proposition 19**</ins> For any variety $$X$$ we have $$\Pic(X) \cong \CaCl(X)$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

First we verify that $$D \mapsto \mathcal{O}_X(D)$$ is a group homomorphism from $$\CaDiv(X)$$ to $$\Pic(X)$$. For a Cartier divisor $$D = \{(U_i, f_i)\}$$, the transition function of $$\mathcal{O}_X(D)$$ is $$g_{ij} = f_i/f_j \in \mathcal{O}_X(U_i \cap U_j)^\times$$, so it defines a line bundle. A principal divisor $$\divisor(h)$$ corresponds to the trivial bundle since its transition function is $$1$$, and hence we obtain a well-defined group homomorphism from $$\CaCl(X) = \CaDiv(X)/\Prin(X)$$ to $$\Pic(X)$$.

To show that this is an isomorphism, let an arbitrary line bundle $$\mathcal{L}$$ be given. Over a trivializing open set $$U \subseteq X$$ we have $$\mathcal{L}\vert_U \cong \mathcal{O}_U$$, so we can pick $$s \in \mathcal{L}(U)$$ corresponding to the constant section $$1$$ of $$\mathcal{O}_U$$; this $$s$$ is a nonzero rational section. Now consider a trivializing cover $$\{U_i\}$$ of $$\mathcal{L}$$. On each $$U_i$$ choose a trivialization $$\psi_i\colon \mathcal{L}\vert_{U_i} \cong \mathcal{O}_{U_i}$$ and define $$f_i := \psi_i(s\vert_{U_i \cap U}) \in \mathcal{O}_X(U_i \cap U) \subseteq \mathbb{K}(X)$$. Then on $$U_i \cap U_j \cap U$$ we have $$f_i = g_{ij} f_j$$, and since $$X$$ is irreducible, $$U_i \cap U_j \cap U$$ is a dense open subset of $$U_i \cap U_j$$, so this relation holds on all of $$U_i \cap U_j$$. That is, $$f_i/f_j = g_{ij} \in \mathcal{O}_X(U_i \cap U_j)^\times$$, so $$D = \{(U_i, f_i)\}$$ is a Cartier divisor, and since the transition function of $$\mathcal{O}_X(D)$$ is $$\{g_{ij}\}$$, we have $$\mathcal{O}_X(D) \cong \mathcal{L}$$.

Finally we show injectivity. If $$\mathcal{O}_X(D) \cong \mathcal{O}_X(D')$$, then the transition functions of the two line bundles are the same, so $$f_i/f_i' = f_j/f_j'$$ on $$U_i \cap U_j$$ (for all $$i, j$$). Since this relation holds on a dense open subset of $$U_i \cap U_j$$, $$f_i/f_i'$$ is the same rational function $$h \in \mathbb{K}(X)^\times$$ for all $$i$$, and $$D - D' = \divisor(h)$$, so they are linearly equivalent.

</details>

If $$X$$ is smooth, we already know that $$\CaCl(X)\cong \Cl(X)$$. Their relationship is summarized in the following commutative diagram.

img

## Pullback of Line Bundles

Given a morphism $$\varphi: X \to Y$$, the operation of "pulling back" a line bundle on $$Y$$ to $$X$$ is naturally defined. For example, pulling back a hypersurface on $$Y$$ via $$\varphi$$ to $$X$$ should pull back the corresponding line bundle as well. This pullback operation induces a group homomorphism between Picard groups, and in the case of an embedding it can be understood as restricting a line bundle on the ambient space to the subvariety.

<div class="proposition" markdown="1">

<ins id="prop20">**Proposition 20**</ins> For a morphism $$\varphi: X \to Y$$ and a line bundle $$\mathcal{L}$$ on $$Y$$, the *pullback* $$\varphi^\ast \mathcal{L}$$ is a line bundle on $$X$$. Its transition functions are $$\{g_{ij} \circ \varphi\}$$, where $$\{g_{ij}\}$$ are the transition functions of $$\mathcal{L}$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Suppose the line bundle $$\mathcal{L}$$ is given by transition functions $$\{g_{ij}\}$$ over an open cover $$\{U_i\}$$. The pullback $$\varphi^\ast \mathcal{L}$$ is defined by transition functions $$\{g_{ij} \circ \varphi\}$$ over the open cover $$\{\varphi^{-1}(U_i)\}$$. To verify that $$\varphi^\ast \mathcal{L}$$ is a line bundle on $$X$$, we need only check that the transition functions satisfy the cocycle condition.

We check all three cocycle conditions.

1. $$g_{ii} \circ \varphi = 1 \circ \varphi = 1$$ since $$g_{ii} = 1$$.
2. $$(g_{ij} \circ \varphi)(g_{ji} \circ \varphi) = (g_{ij} g_{ji}) \circ \varphi = 1 \circ \varphi = 1$$ since $$g_{ij} g_{ji} = 1$$.
3. $$(g_{ij} \circ \varphi)(g_{jk} \circ \varphi) = (g_{ij} g_{jk}) \circ \varphi = g_{ik} \circ \varphi$$ since $$g_{ij} g_{jk} = g_{ik}$$.

Therefore $$\{g_{ij} \circ \varphi\}$$ satisfies the cocycle condition.

</details>

<div class="proposition" markdown="1">

<ins id="prop21">**Proposition 21**</ins> Pullback induces a group homomorphism $$\varphi^\ast: \operatorname{Pic}(Y) \to \operatorname{Pic}(X)$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Since $$\varphi^\ast(\mathcal{L} \otimes \mathcal{M}) \cong \varphi^\ast \mathcal{L} \otimes \varphi^\ast \mathcal{M}$$ and $$\varphi^\ast \mathcal{O}_Y \cong \mathcal{O}_X$$, pullback is a group homomorphism.

To verify this from the transition function viewpoint, the transition function of $$\mathcal{L} \otimes \mathcal{M}$$ is $$g_{ij}^{\mathcal{L}} g_{ij}^{\mathcal{M}}$$, so the transition function of $$\varphi^\ast(\mathcal{L} \otimes \mathcal{M})$$ is $$(g_{ij}^{\mathcal{L}} g_{ij}^{\mathcal{M}}) \circ \varphi = (g_{ij}^{\mathcal{L}} \circ \varphi)(g_{ij}^{\mathcal{M}} \circ \varphi)$$. These are precisely the transition functions of $$\varphi^\ast\mathcal{L}$$ and $$\varphi^\ast\mathcal{M}$$ respectively, so we obtain $$\varphi^\ast(\mathcal{L} \otimes \mathcal{M}) \cong \varphi^\ast\mathcal{L} \otimes \varphi^\ast\mathcal{M}$$. Moreover, the transition functions of $$\mathcal{O}_Y$$ are all $$1$$, so the transition functions of $$\varphi^\ast\mathcal{O}_Y$$ are also $$1$$, i.e. $$\varphi^\ast\mathcal{O}_Y \cong \mathcal{O}_X$$.

</details>

<div class="example" markdown="1">

<ins id="ex22">**Example 22**</ins> For an embedding $$i: C \hookrightarrow \mathbb{P}^n$$, the pullback $$i^\ast \mathcal{O}_{\mathbb{P}^n}(1)$$ is a line bundle on the curve $$C$$. We call this the *hyperplane bundle* on $$C$$ and denote it by $$\mathcal{O}_C(1)$$. In general $$\mathcal{O}_C(1)$$ is nontrivial; for example, when $$C = \mathbb{P}^1 \subset \mathbb{P}^n$$ we have $$\mathcal{O}_C(1) = \mathcal{O}_{\mathbb{P}^1}(1)$$, which is a nontrivial line bundle as we saw in [Example 12](#ex12). The name "hyperplane bundle" comes from the fact that it is obtained by pulling back the line bundle $$\mathcal{O}_{\mathbb{P}^n}(1)$$ corresponding to a hyperplane $$H$$, i.e. a hypersurface of degree $$1$$ in $$\mathbb{P}^n$$, to $$C$$.

</div>

## Vector Bundle

So far we have examined line bundles, whose fibers are one-dimensional vector spaces. We can generalize this concept to define *vector bundles*, whose fibers are higher-dimensional vector spaces. Vector bundles capture structures that arise naturally in geometry, such as tangent spaces and normal spaces of varieties, and are the algebraic-geometric analogues of tangent bundles and vector fields in differential geometry. A line bundle is the special case of a rank-$$1$$ vector bundle, and the properties of line bundles can be understood more clearly from the viewpoint of vector bundle theory.

<div class="definition" markdown="1">

<ins id="def23">**Definition 23**</ins> A *rank r vector bundle* $$\mathcal{E}$$ over a variety $$X$$ consists of the following data.

1. A projection $$\pi: \mathcal{E} \to X$$.
2. An open cover $$\{U_i\}$$ of $$X$$ and, for each $$i$$, a *local trivialization* $$\phi_i: \pi^{-1}(U_i) \overset{\sim}{\longrightarrow} U_i \times \mathbb{A}^r$$. The maps

    $$\phi_j \circ \phi_i^{-1}: (U_i \cap U_j) \times \mathbb{A}^r \to (U_i \cap U_j) \times \mathbb{A}^r$$

    have the form $$(p, v) \mapsto (p, g_{ij}(p)v)$$ for suitable *transition functions* $$g_{ij} \in \operatorname{GL}_r(\mathcal{O}_X(U_i \cap U_j))$$.

</div>

Comparing with the definition of a line bundle, the only differences are that the fiber is $$\mathbb{A}^r$$ rather than $$\mathbb{A}^1$$, and the transition function takes values in $$\operatorname{GL}_r(\mathcal{O}_X(U_i \cap U_j))$$ rather than $$\mathcal{O}_X(U_i \cap U_j)^\ast = \operatorname{GL}_1(\mathcal{O}_X(U_i \cap U_j))$$. Hence a line bundle is exactly a rank-$$1$$ vector bundle.

The same cocycle condition as in [Proposition 2](#prop2) holds. However, since the transition functions are matrix-valued, one must be careful about the order of multiplication.

<div class="example" markdown="1">

<ins id="ex24">**Example 24**</ins> The simplest example is the rank-$$r$$ *trivial vector bundle* $$\mathcal{O}_X^{\oplus r}$$ coming from the line bundle $$\mathcal{O}_X$$. This is obtained by taking the direct sum of the line bundle $$\mathcal{O}_X$$ with itself $$r$$ times.

Geometrically important objects are the tangent bundle and the cotangent bundle. The *tangent bundle* $$\mathcal{T}_X$$ is the vector bundle whose fiber at each point $$p \in X$$ is the tangent space $$T_p X$$; if $$X$$ is an $$n$$-dimensional smooth variety then it is a rank-$$n$$ vector bundle, and in local coordinates $$\x_1, \ldots, \x_n$$ the vectors $$\partial/\partial \x_1, \ldots, \partial/\partial \x_n$$ form a local frame. The *cotangent bundle* $$\Omega_X^1 = \mathcal{T}_X^\vee$$ is the dual of the tangent bundle, and in local coordinates $$d\x_1, \ldots, d\x_n$$ form a local frame.

Intuitively $$\Omega_X^1$$ is the bundle of differential $$1$$-forms on $$X$$, so by tensoring them $$r$$ times we can obtain the bundle of $$r$$-forms. Among these the most interesting is the top exterior power $$\omega_X = \bigwedge^n \Omega_X^1$$, which is a rank-$$1$$ vector bundle, i.e. a line bundle, and in differential geometry would be thought of as the bundle of volume forms. We call this the *canonical line bundle*.

</div>

As above, similar operations to those for line bundles can be defined for vector bundles. The tensor product $$\mathcal{E} \otimes \mathcal{F}$$ of two vector bundles $$\mathcal{E}, \mathcal{F}$$ is defined by the fiberwise tensor product, and its transition functions are $$g_{ij}^{\mathcal{E}} \otimes g_{ij}^{\mathcal{F}}$$. The transition functions of the dual bundle $$\mathcal{E}^\vee$$ are $$\left(g_{ij}^{\mathcal{E}}\right)^{-t}$$ (inverse transpose). Also, the direct sum $$\mathcal{E} \oplus \mathcal{F}$$ is defined by the fiberwise direct sum, and in this case the transition functions become the block diagonal matrix $$\begin{pmatrix} g_{ij}^{\mathcal{E}} & 0 \\ 0 & g_{ij}^{\mathcal{F}} \end{pmatrix}$$.

## Tautological Bundle on Grassmannian

The tautological bundle $$\mathcal{O}_{\mathbb{P}^n}(-1)$$ on $$\mathbb{P}^n$$ defined above generalizes naturally to Grassmannians. The Grassmannian $$\Gr(k, n)$$ is the space of $$k$$-dimensional subspaces of an $$n$$-dimensional vector space, and in this generalization the tautological bundle becomes a rank-$$k$$ vector bundle; the *quotient bundle* dual to it is also naturally defined.

<div class="definition" markdown="1">

<ins id="def25">**Definition 25**</ins> We define the following two vector bundles over the Grassmannian $$\Gr(k, n)$$.

1. *Tautological bundle* $$S$$: a rank-$$k$$ vector bundle assigning to each point $$[V] \in \Gr(k, n)$$ (where $$V \subseteq \mathbb{A}^n$$ is a $$k$$-dimensional subspace) the subspace $$V$$ itself as fiber.
   $$S = \{([V], v) \in \Gr(k, n) \times \mathbb{A}^n \mid v \in V\}$$

2. *Quotient bundle* $$Q$$: a rank-$$(n-k)$$ vector bundle assigning to each point $$[V]$$ the quotient space $$\mathbb{A}^n / V$$ as fiber.
   $$Q = \{([V], [w]) \in \Gr(k, n) \times (\mathbb{A}^n / S) \mid [w] \in \mathbb{A}^n / V\}$$

</div>

There is a natural short exact sequence between them.

$$0 \to S \to \mathcal{O}_{\Gr(k,n)}^{\oplus n} \to Q \to 0$$

Here the middle term is $$\Gr(k, n) \times \mathbb{A}^n$$, the trivial bundle of rank $$n$$. The first map is the inclusion $$([V], v) \in S \mapsto ([V], v) \in \mathcal{O}^{\oplus n}$$, and the second map is the quotient map sending $$([V], w) \in \mathcal{O}^{\oplus n}$$ to $$([V], [w]) \in Q$$.

<div class="proposition" markdown="1">

<ins id="prop26">**Proposition 26**</ins> On $$\Gr(1, n+1) = \mathbb{P}^n$$, the tautological bundle $$S$$ is isomorphic to $$\mathcal{O}_{\mathbb{P}^n}(-1)$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Each point of $$\Gr(1, n+1)$$ is a $$1$$-dimensional subspace of $$\mathbb{A}^{n+1}$$, i.e. a line through the origin. This corresponds exactly to a point of $$\mathbb{P}^n$$. Since each fiber of the tautological bundle $$S$$ is this line itself, it is the same as $$\mathcal{O}_{\mathbb{P}^n}(-1)$$ defined in [Definition 13](#def13).

</details>

This proposition shows that the tautological bundle on a Grassmannian reduces to the familiar $$\mathcal{O}(-1)$$ on projective space. In the case of the quotient bundle $$Q$$, on $$\Gr(1, n+1) = \mathbb{P}^n$$ it has rank $$n$$ and is closely related to the tangent bundle $$\mathcal{T}_{\mathbb{P}^n}$$. In fact $$\mathcal{T}_{\mathbb{P}^n} \cong \Hom(S, Q) \cong S^\vee \otimes Q$$ holds.

---

**References**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.
