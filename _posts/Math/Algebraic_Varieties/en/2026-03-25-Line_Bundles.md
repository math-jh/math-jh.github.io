---
title: "Line Bundles and Vector Bundles"
description: "A line bundle on a manifold assigns a one-dimensional vector space to each point, allowing arbitrary parameters to be treated independently without local constraints. This post extends the definition from line bundles to vector bundles."
excerpt: "Line bundles, invertible sheaves, and the Picard group"

categories: [Math / Algebraic Varieties]
permalink: /en/math/algebraic_varieties/line_bundles
sidebar:
    nav: "algebraic_varieties-en"


date: 2026-03-25
weight: 10
translated_at: 2026-07-11T07:00:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-07-11T07:00:02+00:00
---
We defined divisors on a variety $X$ in the previous post and saw that their linear equivalence classes form $\Cl(X)$. However, not every divisor arises as the zero or pole locus of some rational function. For instance, since $\Cl(\mathbb{P}^n) \cong \mathbb{Z}$ ([§Divisors, ⁋Example 11](/en/math/algebraic_varieties/divisors#ex11)), a general divisor $dH$ on $\mathbb{P}^n$ is the zero set of some function only when $d \ge 0$.

To overcome this restriction, we introduce *line bundles*. A line bundle $\mathcal{L}$ is a geometric object that assigns a one-dimensional vector space to each point $p \in X$, and a section $s$ of $\mathcal{L}$ naturally defines a divisor $\divisor(s)$. From this perspective, for any divisor $D$ we can construct a line bundle $\mathcal{O}_X(D)$, whose sections correspond to divisors greater than or equal to $D$. In other words, line bundles allow us to treat divisors independently of the constraint that they be zeros or poles of functions.

## Definition of Line Bundles

Line bundles, and more generally vector bundles, which we will define later in this post, are defined in the same way as in other fields such as differential geometry. ([\[Manifolds\] §Tangent and Cotangent Bundles, ⁋Definition 1](/en/math/manifolds/tangent_and_cotangent_bundles#def1) or [\[Algebraic Topology\] §Stiefel-Whitney Characteristic Classes, ⁋Definition 2](/en/math/algebraic_topology/stiefel_whitney_classes#def2), etc.)

::: Definition 1
A *line bundle* $\mathcal{L}$ on a variety $X$ consists of the following data.

1. A projection $\pi: \mathcal{L} \rightarrow X$.
2. An open cover $\{U_i\}$ of $X$ and, for each $i$, a *local trivialization* $\phi_i: \pi^{-1}(U_i) \overset{\sim}{\longrightarrow} U_i \times \mathbb{A}^1$. These define

    $$\phi_j \circ \phi_i^{-1}: (U_i \cap U_j) \times \mathbb{A}^1 \rightarrow (U_i \cap U_j) \times \mathbb{A}^1$$

    which has the form $(p, t) \mapsto (p, g_{ij}(p)t)$ for suitable *transition functions* $g_{ij} \in \mathcal{O}_X(U_i \cap U_j)^\times$.
:::

A *morphism* $\varphi \colon \mathcal{L} \rightarrow \mathcal{M}$ between two line bundles $\mathcal{L}, \mathcal{M} \rightarrow X$ defines a $\mathbb{K}$-linear map $\varphi_p \colon \mathcal{L}_p \rightarrow \mathcal{M}_p$ between fibers at each point $p \in X$, and can be expressed over a suitable open cover $\{U_k\}$ as an $\mathcal{O}_X(U_k)$-module homomorphism

$$\varphi_k \colon \mathcal{O}_{U_k} \rightarrow \mathcal{O}_{U_k}$$

such that

$$g^{\mathcal{M}}_{kl} \circ \varphi_l = \varphi_k \circ g^{\mathcal{L}}_{kl}$$

holds. Since the fiber of a line bundle is one-dimensional, each $\varphi_k$ is given by multiplication by some $h_k \in \mathcal{O}_X(U_k)$, i.e. $s \mapsto h_k s$. When $\varphi$ is bijective on each fiber, we call it an *isomorphism* and write $\mathcal{L} \cong \mathcal{M}$. Because the fibers are one-dimensional, this is equivalent to giving a nonzero scalar at each point, i.e. choosing $h_k \in \mathcal{O}_X(U_k)^\ast$ compatibly.

The following proposition follows directly from the definition of the cocycle condition.

::: Proposition 2 (Cocycle condition)
The transition functions $\{g_{ij}\}$ satisfy the following *cocycle condition*.

1. $g_{ii} = 1$ for all $i$.
2. $g_{ij} = g_{ji}^{-1}$ for all $i, j$.
3. $g_{ij} g_{jk} = g_{ik}$ on $U_i \cap U_j \cap U_k$ for all $i, j, k$.
:::

::: Example 3
The *trivial line bundle* $X \times \mathbb{A}^1$ is the line bundle with all transition functions $g_{ij} = 1$. This is the simplest line bundle, with no twist.
:::

Thus the second condition in [Definition 1](#def1) means that the line bundle $\mathcal{L}$ becomes isomorphic to the trivial line bundle when restricted to a suitable open subset $U \subseteq X$.

[Proposition 2](#prop2) is a common gluing condition, and by it a line bundle can be thought of as a kind of sheaf. ([\[Topology\] §Sheaves, ⁋Definition 1](/en/math/topology/sheaves#def1)) Concretely, given a line bundle $\mathcal{L}$, we define its sheaf of sections by

$$U\mapsto \mathcal{O}_X(\mathcal{L})(U)=\{s: U \rightarrow \mathcal{L} \mid \pi \circ s = \id_U\}$$

That is, $\mathcal{O}_X(\mathcal{L})$ is the sheaf of sections of the surjection $\pi$. ([\[Topology\] §Sheaves, ⁋Example 9](/en/math/topology/sheaves#ex9))

Then by the local trivialization $\phi_i: \pi^{-1}(U_i) \rightarrow U_i \times \mathbb{A}^1$ we have $\mathcal{O}_X(\mathcal{L})\vert_{U_i} \cong \mathcal{O}_{U_i}$. Through this, on each $U_i$ we can locally think of these sections as ordinary $\mathbb{K}$-valued functions.

This means the following.

::: Definition 4
A sheaf $\mathcal{F}$ is called *invertible* if for every point $p \in X$ there is a neighborhood $U$ such that $\mathcal{F}\vert_U \cong \mathcal{O}_U$.
:::

What we showed above is that the sheaf of sections of a line bundle is invertible. The next proposition shows that the converse also holds.

::: Proposition 5
The sheaf of sections $\mathcal{O}_X(\mathcal{L})$ of a line bundle $\mathcal{L}$ is an invertible sheaf. Conversely, every invertible sheaf comes from a unique line bundle.
:::

::: Proof
For an invertible sheaf $\mathcal{F}$, one can define transition functions from the local isomorphisms $\mathcal{F}\vert_{U_i} \cong \mathcal{O}_{U_i}$, and reconstruct the line bundle from them.
:::

By this proposition, we know that line bundles and invertible sheaves are the same concept. For this reason, when denoting a line bundle we use the calligraphic $\mathcal{L}$ rather than the roman $L$ used to denote the space.

## Operations on Line Bundles

In the world of differential geometry, it is natural to construct new bundles by bringing in operations from linear algebra fiberwise. The same is true in algebraic geometry; since we are currently looking at the case of line bundles, what we need to examine now are $\otimes$ and $\Hom$, and in particular the dual $(-)^\vee$.

::: Proposition 6
The tensor product $\mathcal{L} \otimes \mathcal{M}$ of two line bundles $\mathcal{L}, \mathcal{M}$ is also a line bundle. Its transition functions are $\{g_{ij} h_{ij}\}$, where $\{g_{ij}\}, \{h_{ij}\}$ are the transition functions of $\mathcal{L}, \mathcal{M}$ respectively.
:::
::: Proof
The fiber of the tensor product is $\mathcal{L}_p \otimes_{\mathbb{K}} \mathcal{M}_p$, which is again one-dimensional since it is the tensor product of two one-dimensional vector spaces. The transition function is the product of $\phi_j \circ \phi_i^{-1}$ and $\psi_j \circ \psi_i^{-1}$, hence $g_{ij} h_{ij}$.
:::

For any line bundle $\mathcal{L}$, the dual bundle $\mathcal{L}^\vee$ is the bundle whose fibers are given by

$$\mathcal{L}_x^\vee=\Hom_\mathbb{K}(\mathcal{L}_x, \mathbb{K})$$

If we think of line bundles as (invertible) sheaves following [Proposition 5](#prop5), then $\mathcal{L}^\vee$ is the line bundle corresponding to the sheaf Hom $\sHom_{\mathcal{O}_X}(\mathcal{L}, \mathcal{O}_X)$.

::: Proposition 7
The *dual bundle* $\mathcal{L}^\vee$ of a line bundle $\mathcal{L}$ is also a line bundle, and its transition functions are $\{g_{ij}^{-1}\}$.
:::

::: Proof
The fiber of the dual bundle is $\mathcal{L}_p^\vee = \Hom_{\mathbb{K}}(\mathcal{L}_p, \mathbb{K})$, which is again one-dimensional since it is the dual of a one-dimensional vector space. The transition function is the inverse of $g_{ij}$.
:::

The following proposition now shows the relationship between $\otimes$ and $(-)^\vee$, which plays an important role in defining the Picard group.

::: Proposition 8
For any line bundle $\mathcal{L}$, we have $\mathcal{L} \otimes \mathcal{L}^\vee \cong \mathcal{O}_X$.
:::

::: Proof
The transition functions of $\mathcal{L} \otimes \mathcal{L}^\vee$ are $g_{ij} \cdot g_{ij}^{-1} = 1$, so it is the trivial bundle.
:::

As always, we can understand the structure of a line bundle by looking at it on a sufficiently small affine open set. Consider a line bundle $\mathcal{L}$ and choose an affine open subset $U_i$ on which $\mathcal{L}$ is trivial. Then the projection map

$$\pi\vert_{\pi^{-1}(U_i)}:\pi^{-1}(U_i) \rightarrow U_i$$

is a morphism between affine varieties, and therefore induces a ring homomorphism between coordinate rings by [§Affine Varieties, ⁋Proposition 16](/en/math/algebraic_varieties/affine_varieties#prop16). This ring homomorphism makes the coordinate ring of $\pi^{-1}(U_i)$ into a module over the coordinate ring of $U_i$, and considering dimensions, its rank is 1. Since $\mathcal{L}$ is trivial on any open subset of $U_i$ as well, we can verify that a line bundle becomes, affine-locally, an invertible module over the coordinate ring. ([\[Commutative Algebra\] §Fractional Ideals, ⁋Definition 1](/en/math/commutative_algebra/fractional_ideals#def1)) Then the operations $\otimes$ and $\vee$ defined on line bundles come from the operations in [\[Commutative Algebra\] §Fractional Ideals, ⁋Theorem 3](/en/math/commutative_algebra/fractional_ideals#thm3), and therefore it is not unnatural to adopt the following name following [\[Commutative Algebra\] §Fractional Ideals, ⁋Definition 5](/en/math/commutative_algebra/fractional_ideals#def5).

::: Definition 9
The *Picard group* $\Pic(X)$ of a variety $X$ is the group obtained by endowing the set of isomorphism classes of line bundles on $X$ with the tensor product as the operation. The identity element is the trivial bundle $\mathcal{O}_X$, and the inverse of $\mathcal{L}$ is $\mathcal{L}^\vee$.
:::

That the trivial bundle actually serves as the identity element can be checked directly from [Example 3](#ex3) and [Proposition 6](#prop6). Moreover, by the properties of the tensor product, the following holds.

::: Proposition 10
$\Pic(X)$ is an abelian group.
:::

::: Proof
By [Proposition 6](#prop6), the tensor product is a binary operation on line bundles, and by [Proposition 8](#prop8), $\mathcal{O}_X$ is the identity and $\mathcal{L}^\vee$ is the inverse of $\mathcal{L}$. The commutativity $\mathcal{L} \otimes \mathcal{M} \cong \mathcal{M} \otimes \mathcal{L}$ and associativity $(\mathcal{L} \otimes \mathcal{M}) \otimes \mathcal{N} \cong \mathcal{L} \otimes (\mathcal{M} \otimes \mathcal{N})$ of the tensor product follow directly at the level of transition functions from $g_{ij}h_{ij} = h_{ij}g_{ij}$ and $(g_{ij}h_{ij})k_{ij} = g_{ij}(h_{ij}k_{ij})$.
:::

As in the previous post, our toy examples are $\mathbb{A}^n$ and $\mathbb{P}^n$.

::: Example 11
The coordinate ring $R = \mathbb{K}[\x_1, \ldots, \x_n]$ of $\mathbb{A}^n$ is a UFD, and by the above discussion, line bundles on $\mathbb{A}^n$ correspond to invertible modules over $R$. By [\[Commutative Algebra\] §Fractional Ideals, ⁋Theorem 4](/en/math/commutative_algebra/fractional_ideals#thm4), invertible modules over a UFD are free, so $\Pic(\mathbb{A}^n) = 0$.
:::


::: Example 12
We define the line bundle $\mathcal{O}_{\mathbb{P}^n}(d)$ on $\mathbb{P}^n$ as follows. First, the standard open cover

$$U_i = \{[x_0 : \cdots : x_n] \mid x_i \ne 0\}$$

gives trivializing open sets for this bundle. We explicitly define the trivialization on each of these by

$$\phi_i\colon \mathcal{O}(d)\vert_{U_i} \xrightarrow{\sim} \mathcal{O}_{U_i}, \qquad \phi_i(s) = s \cdot \x_i^{-d}$$

From this, we know that the section space has the form

$$\mathcal{O}(d)(U_i) = \x_i^d \cdot \mathcal{O}(U_i) = \x_i^d\mathbb{K}[\x_0/\x_i, \ldots, \widehat{\x_i/\x_i}, \ldots, \x_n/\x_i]$$

Now comparing the two trivializations on $U_i \cap U_j$, we can derive the transition function. That is, the transition function $\phi_j \circ \phi_i^{-1}\colon \mathcal{O}_{U_i}\vert_{U_i \cap U_j} \rightarrow \mathcal{O}_{U_j}\vert_{U_i \cap U_j}$ is

$$\phi_j \circ \phi_i^{-1}(f) = (\x_i/\x_j)^d \cdot f$$

so we obtain $g_{ij} = (\x_i/\x_j)^d$. More concretely, for each point $x \in U_i \cap U_j$ and its fiber $v \in \mathcal{O}_{\mathbb{P}^n}(d)_x \cong \mathbb{A}^1$,

$$g_{ij}(x)\colon v \mapsto (\x_i/\x_j)^d(x) \cdot v$$

Now we can define a group homomorphism

$$\mathbb{Z}\rightarrow \Pic(\mathbb{P}^n);\qquad d\mapsto [\mathcal{O}_{\mathbb{P}^n}(d)]$$

Our claim is that this is an isomorphism. First, for any line bundle $\mathcal{L}$, since $\mathcal{L}\vert_{U_i}$ is isomorphic to the trivial line bundle by [Example 11](#ex11), the transition functions $h_{ij}$ on each $U_i\cap U_j$ completely determine $\mathcal{L}$. But by definition, on $U_i\cap U_j$ we have $h_{ij}\in \mathcal{O}_{\mathbb{P}^n}(U_i\cap U_j)^\ast$, so $h_{ij}$ must be of the form $c_{ij}(\x_i/\x_j)^d$. Since a line bundle whose transition functions differ by a constant factor is trivial, we know that the above group homomorphism is surjective. Similarly, assuming $\mathcal{O}_{\mathbb{P}^n}(d)\cong \mathcal{O}_{\mathbb{P}^n}(d')$ and comparing transition functions,

$$\mathcal{O}_{\mathbb{P}^n}(d-d')\cong \mathcal{O}_{\mathbb{P}^n}(d)\otimes \mathcal{O}_{\mathbb{P}^n}(-d')\cong \mathcal{O}_{\mathbb{P}^n}(d)\otimes \mathcal{O}_{\mathbb{P}^n}(d')^\vee\cong \mathcal{O}_{\mathbb{P}^n}$$

for this to hold we must have $d-d'=0$, so it is also injective.
:::

Intuitively, the integer $d$ in the line bundle $\mathcal{O}_{\mathbb{P}^n}(d)$ on $\mathbb{P}^n$ can be understood as a measure of how many times the fiber twists as it moves along the base. When $d=0$, $\mathcal{O}(0)$ is the trivial bundle so there is no twist; when $d>0$ it twists $d$ times in one direction, and when $d<0$ it twists $\lvert d\rvert$ times in the opposite direction. This means that in the transition function $g_{ij}(x) = (x_i/x_j)^d(x)$, the exponent $d$ directly represents the degree of twisting. However, this intuition may be somewhat imprecise, so some additional explanation will be needed after [Example 16](#ex16).

On the other hand, on the projective space $\mathbb{P}^n$ there exists a special line bundle that arises naturally from its definition. This *tautological bundle* is the bundle that assigns to each point of $\mathbb{P}^n$ the line represented by that point, and it plays a fundamental role in understanding the geometry of projective space.

::: Definition 13
For each point $x = [x_0 : \cdots : x_n]$ in $\mathbb{P}^n$, consider the space

$$\mathcal{O}_{\mathbb{P}^n}(-1) = \{(x, v) \in \mathbb{P}^n \times \mathbb{A}^{n+1} \mid v \in \ell_x\}$$

where $\ell_x = \{(\lambda x_0, \ldots, \lambda x_n) \mid \lambda \in \mathbb{K}\}$ is the line through the origin in $\mathbb{A}^{n+1}$ corresponding to each point. Then the line bundle defined by the projection map $\pi=\pr_1$ from $\mathcal{O}_{\mathbb{P}^n}(-1)$ to $\mathbb{P}^n$ is called the *tautological line bundle* on $\mathbb{P}^n$.
:::

That is, in this definition, each fiber $\mathcal{O}_{\mathbb{P}^n}(-1)_x$ is the line represented by the point $x$ itself. As the notation suggests, the following holds. For distinction, in the next proposition only, let us think of $\mathcal{O}_{\mathbb{P}^n}(-1)$ as the bundle from [Definition 13](#def13), not [Example 12](#ex12).

::: Proposition 14
The tautological bundle $\mathcal{O}_{\mathbb{P}^n}(-1)$ is the dual of $\mathcal{O}_{\mathbb{P}^n}(1)$ defined in [Example 12](#ex12) above. That is, $\mathcal{O}_{\mathbb{P}^n}(-1) \cong \mathcal{O}_{\mathbb{P}^n}(1)^\vee$.
:::

::: Proof
Let us construct a local trivialization of $\mathcal{O}_{\mathbb{P}^n}(-1)$ on the standard open cover $U_i = \{x \mid x_i \ne 0\}$. For any $(x, v) \in \mathcal{O}_{\mathbb{P}^n}(-1)$, we can write $v = \lambda x$ ($\lambda \in \mathbb{K}$), so defining $\phi_i(x, v) = (x, v_i)$ gives $\phi_i: \pi^{-1}(U_i) \rightarrow U_i \times \mathbb{A}^1$. The inverse is $\phi_i^{-1}(x, t) = (x, (t/x_i)x)$. The transition function on $U_i \cap U_j$ is obtained from $\phi_j \circ \phi_i^{-1}(x, t) = (x, t x_j / x_i)$ as $g_{ij}(x) = x_j/x_i$. This is the inverse of the transition function $x_i/x_j$ of $\mathcal{O}_{\mathbb{P}^n}(1)$.
:::

In particular, examining $\mathcal{O}(-1)$ on $\mathbb{P}^1$ makes the meaning of the intuitive *twist* explained above much clearer. The process of making $\mathbb{P}^1$ from $\mathbb{A}^2\setminus \{0\}$ can be thought of as first mapping $\mathbb{A}^2\setminus\{0\}$ to the unit circle via radial projection, and then identifying antipodal points of the unit circle; during this process, vectors in opposite directions are identified, which causes the fibers to twist. One way to see this twist is to look at sections of the line bundle $\mathcal{L}$.

::: Definition 15
We denote the space of *global sections* of a line bundle $\mathcal{L}$ by $\Gamma(X, \mathcal{L})$. That is, $\Gamma(X, \mathcal{L})$ is the set of regular maps assigning to each point $x\in X$ an element of the fiber $\pi^{-1}(x)\subseteq \mathcal{L}$.
:::

Another popular notation for the global section space is $H^0(X, \mathcal{L})$. This notation will be justified in [§Sheaf Cohomology, ⁋Definition 1](/en/math/algebraic_varieties/sheaf_cohomology#def1), but until then we will use $\Gamma(X, \mathcal{L})$.

::: Example 16
The only global section of $\mathcal{O}_{\mathbb{P}^n}(-1)$ is $0$. That is,

$$\Gamma(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n}(-1)) = 0$$

To verify this, by [Example 12](#ex12) we have $\mathcal{O}(-1)(U_i) = \x_i^{-1} \cdot \mathbb{K}[\x_0/\x_i, \ldots, \widehat{\x_i/\x_i}, \ldots, \x_n/\x_i]$, and the trivialization is given by $\phi_i(s) = s \cdot \x_i$. Therefore the trivialized section $\phi_i(s) \in \mathcal{O}(U_i) = \mathbb{K}[\x_0/\x_i, \ldots, \x_n/\x_i]$, and on $U_i \cap U_j$ the cocycle condition requires

$$\phi_j(s) = (\x_j/\x_i)\phi_i(s)$$

However, since $\phi_i(s) \in \mathbb{K}[\x_0/\x_i, \ldots, \widehat{\x_i/\x_i}, \ldots, \x_n/\x_i]$ cannot contain a term $\x_i/\x_j$, for $(\x_j/\x_i)\phi_i(s)$ to lie in $\mathcal{O}(U_j) = \mathbb{K}[\x_0/\x_j, \ldots, \widehat{\x_j/\x_j}, \ldots, \x_n/\x_j]$ we must have $\phi_i(s) = 0$. Therefore $s = 0$.
:::

This proposition shows the *twist* of the tautological bundle from the viewpoint of sections. For example, the fact that $\Gamma(\mathbb{P}^1, \mathcal{O}(-1))=0$ means in particular that there is no "constant function" assigning the element 1 of the fiber to every $x\in \mathbb{P}^1$. From the geometric perspective above, this is because when we go around $\mathbb{P}^1$ once, the original 1 becomes (for example) $-1$.

On the other hand, the computation in [Example 16](#ex16) can be extended to arbitrary $d$; in particular, for any $d<0$ we can show $\Gamma(\mathbb{P}^1, \mathcal{O}(d))=0$ by the same logic, and for $d=0$, i.e. for $\mathcal{O}_{\mathbb{P}^n}(0)=\mathcal{O}_{\mathbb{P}^n}$, the sections are homogeneous polynomials of degree $0$, i.e. constant functions, so the computation in [§Quasi-Projective Varieties, ⁋Example 6](/en/math/algebraic_varieties/quasi_projective_varieties#ex6) is confirmed again.

The part to pay attention to is the case $d>0$. In this case, by exactly the same computation as in [Example 16](#ex16), we can verify that the sections are homogeneous polynomials of degree $d$. In particular $\Gamma(\mathbb{P}^n, \mathcal{O}(d))\neq 0$, which can be thought of as a computation showing that the intuition after [Example 12](#ex12) was somewhat oversimplified.

A more precise explanation of this phenomenon is as follows. For convenience, let us look at the example on $\mathbb{P}^1$. The sections of $\mathcal{O}(-1)$ are homogeneous of degree $-1$, so in particular they have the form

$$s([x_0:x_1])=\frac{a}{x_0}+\frac{b}{x_1}$$

and for this function to be defined on all of $\mathbb{P}^1$ we must have $a=b=0$. On the other hand, the sections of $\mathcal{O}(1)$ are homogeneous polynomials of degree $1$, so they are functions of the form

$$s([x_0:x_1])=ax_0+bx_1$$

and unlike above, there is no restriction on $a, b$. Intuitively, the sections of $\mathcal{O}(-1)$ cannot escape the zero section because of the denominators, so every section is forced to encounter the problem created by the "twist" where "$1$ attaches to $-1$". This twist creates the same problem in $\mathcal{O}(1)$ as well. That is, the "constant section" $s([x_0:x_1])$ is not a section in $\mathcal{O}(1)$ either. However, this time the sections of $\mathcal{O}(1)$ can escape the zero section, so we get $\Gamma(\mathbb{P}^1, \mathcal{O}(1))\neq 0$. From the viewpoint of transition functions or trivializations, one can also think of this as follows: $\mathcal{O}(d)$ multiplies by the degree $d$ polynomial $\x_i^d$, so poles of degree at most $d$ can be erased by this trivialization.

## Divisor -- Line Bundle Correspondence

We now establish the essential connection between divisors and line bundles. First we show that a line bundle can be constructed from a Cartier divisor.

::: Definition 17
For a Cartier divisor $D = \{(U_i, f_i)\}$, we define the line bundle $\mathcal{O}_X(D)$ by the transition functions $g_{ij} = f_i/f_j$.
:::

That is, we take the trivial bundle on each $U_i$ and glue them together on the overlaps using exactly the information contained in the Cartier divisor. If we view $\mathcal{O}_X(D)$ as a sheaf, i.e. consider the sheaf of sections of the line bundle defined above, then on each open set $U$ the sheaf $\mathcal{O}_X(D)(U)$ consists of (as a sheaf) functions satisfying

$$\divisor(f)+D\geq 0$$

That is, $\mathcal{O}_X(D)$ is the sheaf of rational functions that may have poles of order at most $1$ along $D$, if we view $D$ as a codimension $1$ subvariety of $X$. Conversely, $\mathcal{O}_X(-D)$ is given by

$$\divisor(f)-D\geq 0$$

which is exactly the sheaf of functions vanishing on $D$. That is,

$$\mathcal{O}_X(-D)(U)=\{f\in \mathcal{O}_X(U)\mid \text{$f$ vanishes on $D\cap U$}\}$$

and from this we obtain the short exact sequence

$$0\rightarrow \mathcal{O}_X(-D)\rightarrow \mathcal{O}_X\rightarrow \mathcal{O}_D\rightarrow 0$$

Then $\mathcal{O}_X(-D)$ is the sheaf of ideals defining $D$, and for this reason we denote it by $\mathcal{I}_D$ and call it the *ideal sheaf*.

::: Proposition 18
The above definition is well-defined. That is, equivalent Cartier divisors define isomorphic line bundles.
:::

::: Proof
If two Cartier divisors $\{(U_i, f_i)\}$ and $\{(V_j, g_j)\}$ are equivalent, then $f_i/g_j \in \mathcal{O}_X(U_i \cap V_j)^\ast$. The transition functions of the line bundles defined from these are compatible, so they define isomorphic line bundles.
:::

For example, for any principal divisor $\divisor(f)$, the transition function is $1$, so it becomes the trivial bundle. We now summarize the relationship between line bundles and Cartier divisors.

::: Proposition 19
For any variety $X$, we have $\Pic(X) \cong \CaCl(X)$.
:::

::: Proof
First we verify that $D \mapsto \mathcal{O}_X(D)$ is a group homomorphism from $\CaDiv(X)$ to $\Pic(X)$. For a Cartier divisor $D = \{(U_i, f_i)\}$, the transition function of $\mathcal{O}_X(D)$ is $g_{ij} = f_i/f_j \in \mathcal{O}_X(U_i \cap U_j)^\times$, so it defines a line bundle. A principal divisor $\divisor(h)$ corresponds to the trivial bundle since its transition function is $1$, and therefore we obtain a well-defined group homomorphism from $\CaCl(X) = \CaDiv(X)/\Prin(X)$ to $\Pic(X)$.

To show that this is an isomorphism, let an arbitrary line bundle $\mathcal{L}$ be given. On a trivializing open $U \subseteq X$, we have $\mathcal{L}\vert_U \cong \mathcal{O}_U$, so we can pick $s \in \mathcal{L}(U)$ corresponding to the constant section $1$ of $\mathcal{O}_U$, and this $s$ is a nonzero rational section. Now consider a trivializing cover $\{U_i\}$ of $\mathcal{L}$. On each $U_i$, pick a trivialization $\psi_i\colon \mathcal{L}\vert_{U_i} \cong \mathcal{O}_{U_i}$ and define $f_i := \psi_i(s\vert_{U_i \cap U}) \in \mathcal{O}_X(U_i \cap U) \subseteq \mathbb{K}(X)$. Then on $U_i \cap U_j \cap U$ we have $f_i = g_{ij} f_j$, and since $X$ is irreducible, $U_i \cap U_j \cap U$ is a dense open subset of $U_i \cap U_j$, so this relation holds on all of $U_i \cap U_j$. That is, $f_i/f_j = g_{ij} \in \mathcal{O}_X(U_i \cap U_j)^\times$, so $D = \{(U_i, f_i)\}$ is a Cartier divisor, and since the transition function of $\mathcal{O}_X(D)$ is $\{g_{ij}\}$, we have $\mathcal{O}_X(D) \cong \mathcal{L}$.

Finally we show injectivity. If $\mathcal{O}_X(D) \cong \mathcal{O}_X(D')$, then the transition functions of the two line bundles are equal, so $f_i/f_i' = f_j/f_j'$ on $U_i \cap U_j$ (for all $i, j$). Since this relation holds on a dense open subset of $U_i \cap U_j$ again, $f_i/f_i'$ is the same rational function $h \in \mathbb{K}(X)^\times$ for all $i$, and $D - D' = \divisor(h)$, so they are linearly equivalent.
:::

If $X$ is smooth, we already know that $\CaCl(X)\cong \Cl(X)$. Their relationship is contained in the following commutative diagram.

img

## Pullback of Line Bundles

When a morphism $\varphi: X \rightarrow Y$ is given, the operation of "pulling back" a line bundle on $Y$ to $X$ is defined naturally. For example, if we pull back a hypersurface on $Y$ to $X$ via $\varphi$, the corresponding line bundle should also be pulled back. This pullback operation induces a group homomorphism between Picard groups, and in the case of an embedding, it can be understood as restricting line bundles on the ambient space to the subvariety.

::: Proposition 20
For a morphism $\varphi: X \rightarrow Y$ and a line bundle $\mathcal{L}$ on $Y$, the *pullback* $\varphi^\ast \mathcal{L}$ is a line bundle on $X$. Its transition functions are $\{g_{ij} \circ \varphi\}$, where $\{g_{ij}\}$ are the transition functions of $\mathcal{L}$.
:::

::: Proof
Suppose the line bundle $\mathcal{L}$ is given by transition functions $\{g_{ij}\}$ on an open cover $\{U_i\}$. The pullback $\varphi^\ast \mathcal{L}$ is defined by transition functions $\{g_{ij} \circ \varphi\}$ on the open cover $\{\varphi^{-1}(U_i)\}$. To verify that $\varphi^\ast \mathcal{L}$ is a line bundle on $X$, we need to check that the transition functions satisfy the cocycle condition.

We check all three cocycle conditions.

1. $g_{ii} \circ \varphi = 1 \circ \varphi = 1$ since $g_{ii} = 1$.
2. $(g_{ij} \circ \varphi)(g_{ji} \circ \varphi) = (g_{ij} g_{ji}) \circ \varphi = 1 \circ \varphi = 1$ since $g_{ij} g_{ji} = 1$.
3. $(g_{ij} \circ \varphi)(g_{jk} \circ \varphi) = (g_{ij} g_{jk}) \circ \varphi = g_{ik} \circ \varphi$ since $g_{ij} g_{jk} = g_{ik}$.

Therefore $\{g_{ij} \circ \varphi\}$ satisfies the cocycle condition.
:::

::: Proposition 21
Pullback induces a group homomorphism $\varphi^\ast: \operatorname{Pic}(Y) \rightarrow \operatorname{Pic}(X)$.
:::

::: Proof
Since $\varphi^\ast(\mathcal{L} \otimes \mathcal{M}) \cong \varphi^\ast \mathcal{L} \otimes \varphi^\ast \mathcal{M}$ and $\varphi^\ast \mathcal{O}_Y \cong \mathcal{O}_X$, pullback is a group homomorphism.

To verify this from the transition function perspective, the transition function of $\mathcal{L} \otimes \mathcal{M}$ is $g_{ij}^{\mathcal{L}} g_{ij}^{\mathcal{M}}$, so the transition function of $\varphi^\ast(\mathcal{L} \otimes \mathcal{M})$ is $(g_{ij}^{\mathcal{L}} g_{ij}^{\mathcal{M}}) \circ \varphi = (g_{ij}^{\mathcal{L}} \circ \varphi)(g_{ij}^{\mathcal{M}} \circ \varphi)$. These are the transition functions of $\varphi^\ast\mathcal{L}$ and $\varphi^\ast\mathcal{M}$ respectively, so we obtain $\varphi^\ast(\mathcal{L} \otimes \mathcal{M}) \cong \varphi^\ast\mathcal{L} \otimes \varphi^\ast\mathcal{M}$. Also, since the transition functions of $\mathcal{O}_Y$ are all $1$, the transition functions of $\varphi^\ast\mathcal{O}_Y$ are also $1$, i.e. $\varphi^\ast\mathcal{O}_Y \cong \mathcal{O}_X$.
:::

::: Example 22
For an embedding $i: C \hookrightarrow \mathbb{P}^n$, $i^\ast \mathcal{O}_{\mathbb{P}^n}(1)$ is a line bundle on the curve $C$. We call this the *hyperplane bundle* on $C$ and denote it by $\mathcal{O}_C(1)$. In general $\mathcal{O}_C(1)$ is nontrivial; for example, when $C = \mathbb{P}^1 \subseteq \mathbb{P}^n$, $\mathcal{O}_C(1) = \mathcal{O}_{\mathbb{P}^1}(1)$ is a nontrivial line bundle as seen in [Example 12](#ex12). The name "hyperplane bundle" comes from the fact that it is obtained by pulling back the line bundle $\mathcal{O}_{\mathbb{P}^n}(1)$ corresponding to a hyperplane $H$, which is a hypersurface of degree $1$ in $\mathbb{P}^n$, to $C$.
:::

## Vector Bundle

So far we have examined line bundles, whose fibers are one-dimensional vector spaces. We can generalize this concept to define *vector bundles*, whose fibers are higher-dimensional vector spaces. Vector bundles capture structures that arise naturally in geometry, such as tangent and normal spaces of a variety, and are the algebraic-geometric analogues of tangent bundles, vector fields, etc. in differential geometry. Line bundles are the special case of rank 1 vector bundles, and the properties of line bundles can be understood more clearly from the viewpoint of vector bundle theory.

::: Definition 23
A *rank r vector bundle* $\mathcal{E}$ on a variety $X$ consists of the following data.

1. A projection $\pi: \mathcal{E} \rightarrow X$.
2. An open cover $\{U_i\}$ of $X$ and, for each $i$, a *local trivialization* $\phi_i: \pi^{-1}(U_i) \overset{\sim}{\longrightarrow} U_i \times \mathbb{A}^r$. These define

    $$\phi_j \circ \phi_i^{-1}: (U_i \cap U_j) \times \mathbb{A}^r \rightarrow (U_i \cap U_j) \times \mathbb{A}^r$$

    which has the form $(p, v) \mapsto (p, g_{ij}(p)v)$ for suitable *transition functions* $g_{ij} \in \GL_r(\mathcal{O}_X(U_i \cap U_j))$.
:::

Comparing with the definition of a line bundle, the only difference is that the fiber is $\mathbb{A}^r$ instead of $\mathbb{A}^1$, and the transition function takes values in $\GL_r(\mathcal{O}_X(U_i \cap U_j))$ instead of $\mathcal{O}_X(U_i \cap U_j)^\times = \GL_1(\mathcal{O}_X(U_i \cap U_j))$. Therefore a line bundle is exactly a rank 1 vector bundle.

The same cocycle condition as in [Proposition 2](#prop2) holds. However, since the transition functions are matrix-valued, one must be careful about the order of multiplication.

::: Example 24
The simplest example is the rank $r$ *trivial vector bundle* $\mathcal{O}_X^{\oplus r}$ coming from the line bundle $\mathcal{O}_X$. This is obtained by taking the direct sum of the line bundle $\mathcal{O}_X$ $r$ times.

Geometrically important objects are the tangent bundle and cotangent bundle. The *tangent bundle* $\mathcal{T}_X$ is the vector bundle with tangent space $T_p X$ as the fiber at each point $p \in X$; if $X$ is an $n$-dimensional smooth variety, it is a rank $n$ vector bundle, and in local coordinates $\x_1, \ldots, \x_n$ the partial derivatives $\partial/\partial \x_1, \ldots, \partial/\partial \x_n$ form a local frame. The *cotangent bundle* $\Omega_X^1 = \mathcal{T}_X^\vee$ is the dual of the tangent bundle, and in local coordinates $d\x_1, \ldots, d\x_n$ form a local frame.

Intuitively, since $\Omega_X^1$ is the bundle of differential $1$-forms on $X$, we can tensor them $r$ times to obtain the bundle of $r$-forms. Among these, the most interesting is the top exterior power $\omega_X = \bigwedge^n \Omega_X^1$, which is a rank $1$ vector bundle, i.e. a line bundle, and in differential geometry would have been thought of as the bundle of volume forms. We call this the *canonical line bundle*.
:::

As above, similar operations can be defined for vector bundles as for line bundles. The tensor product $\mathcal{E} \otimes \mathcal{F}$ of two vector bundles $\mathcal{E}, \mathcal{F}$ is defined as the fiberwise tensor product, and its transition functions are $g_{ij}^{\mathcal{E}} \otimes g_{ij}^{\mathcal{F}}$. The transition functions of the dual bundle $\mathcal{E}^\vee$ are $\left(g_{ij}^{\mathcal{E}}\right)^{-t}$ (inverse transpose). Also, the direct sum $\mathcal{E} \oplus \mathcal{F}$ is defined as the fiberwise direct sum, and in this case the transition functions become the block diagonal matrix $\begin{pmatrix} g_{ij}^{\mathcal{E}} & 0 \\ 0 & g_{ij}^{\mathcal{F}} \end{pmatrix}$.

## Tautological Bundle on Grassmannian

The tautological bundle $\mathcal{O}_{\mathbb{P}^n}(-1)$ on $\mathbb{P}^n$ defined above generalizes naturally to Grassmannians. The Grassmannian $\Gr(k, n)$ is the space of $k$-dimensional subspaces of an $n$-dimensional vector space, and in this generalization the tautological bundle becomes a rank $k$ vector bundle, and the *quotient bundle* dual to it is also defined naturally.

::: Definition 25
We define the following two vector bundles on the Grassmannian $\Gr(k, n)$.

1. *Tautological bundle* $S$: The rank $k$ vector bundle that assigns to each point $[V] \in \Gr(k, n)$ (where $V \subseteq \mathbb{A}^n$ is a $k$-dimensional subspace) the subspace $V$ itself as the fiber.
   $$S = \{([V], v) \in \Gr(k, n) \times \mathbb{A}^n \mid v \in V\}$$

2. *Quotient bundle* $Q$: The rank $n-k$ vector bundle that assigns to each point $[V]$ the quotient space $\mathbb{A}^n / V$ as the fiber.
   $$Q = \{([V], [w]) \in \Gr(k, n) \times (\mathbb{A}^n / S) \mid [w] \in \mathbb{A}^n / V\}$$
:::

There is a natural short exact sequence between these.

$$0 \rightarrow S \rightarrow \mathcal{O}_{\Gr(k,n)}^{\oplus n} \rightarrow Q \rightarrow 0$$

Here the middle term is $\Gr(k, n) \times \mathbb{A}^n$, the trivial bundle of rank $n$. The first map is the inclusion of each point $([V], v) \in S$ into $([V], v) \in \mathcal{O}^{\oplus n}$, and the second map is the quotient map sending $([V], w) \in \mathcal{O}^{\oplus n}$ to $([V], [w]) \in Q$.

::: Proposition 26
On $\Gr(1, n+1) = \mathbb{P}^n$, the tautological bundle $S$ is isomorphic to $\mathcal{O}_{\mathbb{P}^n}(-1)$.
:::

::: Proof
Each point of $\Gr(1, n+1)$ is a $1$-dimensional subspace of $\mathbb{A}^{n+1}$, i.e. a line through the origin. This corresponds exactly to a point of $\mathbb{P}^n$. Since each fiber of the tautological bundle $S$ is this line itself, it is identical to $\mathcal{O}_{\mathbb{P}^n}(-1)$ defined in [Definition 13](#def13).
:::

This proposition shows that the tautological bundle on a Grassmannian reduces to the familiar $\mathcal{O}(-1)$ on projective space. For the quotient bundle $Q$, on $\Gr(1, n+1) = \mathbb{P}^n$ it has rank $n$ and is closely related to the tangent bundle $\mathcal{T}_{\mathbb{P}^n}$. In fact, $\mathcal{T}_{\mathbb{P}^n} \cong \Hom(S, Q) \cong S^\vee \otimes Q$ holds.

---

**References**

**[Hart]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.
