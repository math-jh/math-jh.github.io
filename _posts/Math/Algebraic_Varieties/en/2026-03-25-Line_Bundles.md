---
title: "Line Bundles and Vector Bundles"
description: "A line bundle on a manifold assigns a one-dimensional vector space to each point, allowing independent variation of parameters without local restrictions. This post begins with the definition of line bundles and extends the discussion to vector bundles."
excerpt: "Line bundles, invertible sheaves, and the Picard group"

categories: [Math / Algebraic Varieties]
permalink: /en/math/algebraic_varieties/line_bundles
sidebar:
    nav: "algebraic_varieties-en"


date: 2026-03-25
weight: 10
translated_at: 2026-08-15T23:50:56+00:00
translation_source: kimi-cli
---
In the previous post we defined divisors on a variety $X$ and saw that their linear equivalence classes form $\Cl(X)$. However, not every divisor arises as the zero or pole locus of some rational function. For instance, since $\Cl(\mathbb{P}^n) \cong \mathbb{Z}$ ([§Divisors, ⁋Example 11](/en/math/algebraic_varieties/divisors#ex11)), a general divisor $dH$ on $\mathbb{P}^n$ is the zero set of a homogeneous polynomial only when $d \ge 0$.

To overcome this restriction we introduce *line bundles*. A line bundle $\mathcal{L}$ is a geometric object that assigns a one-dimensional vector space to each point $p \in X$, and a section $s$ of $\mathcal{L}$ naturally defines a divisor $\divisor(s)$. From this viewpoint, for any divisor $D$ we can construct a line bundle $\mathcal{O}_X(D)$ whose sections correspond to divisors greater than or equal to $D$. In other words, line bundles allow us to treat divisors independently, free from the constraint of being zeros or poles of functions.

## Definition of Line Bundles

Line bundles, and more generally vector bundles which we will define later in this post, are defined in the same way as in other fields such as differential geometry. ([\[Differential Manifolds\] §Tangent and Cotangent Bundles, ⁋Definition 1](/en/math/manifolds/tangent_and_cotangent_bundles#def1) or [\[Algebraic Topology\] §Stiefel-Whitney Characteristic Classes, ⁋Definition 2](/en/math/algebraic_topology/stiefel_whitney_classes#def2), etc.)

::: Definition 1
A *line bundle* $\mathcal{L}$ on a variety $X$ consists of the following data.

1. A projection $\pi: \mathcal{L} \rightarrow X$.
2. An open cover $\{U_i\}$ of $X$ and for each $i$ a *local trivialization* $\phi_i: \pi^{-1}(U_i) \overset{\sim}{\longrightarrow} U_i \times \mathbb{A}^1$. The maps

    $$\phi_j \circ \phi_i^{-1}: (U_i \cap U_j) \times \mathbb{A}^1 \rightarrow (U_i \cap U_j) \times \mathbb{A}^1$$

    are of the form $(p, t) \mapsto (p, g_{ij}(p)t)$ for suitable *transition functions* $g_{ij} \in \mathcal{O}_X(U_i \cap U_j)^\times$.
:::

A sheaf $\mathcal{F}$ is an *$\mathcal{O}_X$-module* if for every open set $U$, the group $\mathcal{F}(U)$ is an $\mathcal{O}_X(U)$-module and this multiplication is compatible with restriction maps; that is, we can multiply a section by a locally defined regular function. A *morphism* of $\mathcal{O}_X$-modules is a sheaf morphism that preserves this multiplication, i.e. an $\mathcal{O}_X(U)$-module homomorphism on each $U$.

A *morphism* $\varphi \colon \mathcal{L} \rightarrow \mathcal{M}$ between two line bundles $\mathcal{L}, \mathcal{M} \rightarrow X$ is a $\mathbb{K}$-linear map $\varphi_p \colon \mathcal{L}_p \rightarrow \mathcal{M}_p$ on each fiber at $p \in X$, which can be expressed over a suitable open cover $\{U_k\}$ as an $\mathcal{O}_X(U_k)$-module homomorphism

$$\varphi_k \colon \mathcal{O}_{U_k} \rightarrow \mathcal{O}_{U_k}$$

satisfying

$$g^{\mathcal{L}}_{kl} \circ \varphi_l = \varphi_k \circ g^{\mathcal{M}}_{kl}.$$

Since the fiber of a line bundle is one-dimensional, each $\varphi_k$ is given by multiplication by some $h_k \in \mathcal{O}_X(U_k)$, i.e. $s \mapsto h_k s$. When $\varphi$ is bijective on each fiber, we call it an *isomorphism* and write $\mathcal{L} \cong \mathcal{M}$. Because the fiber is one-dimensional, this is equivalent to giving a nonzero scalar at each point, i.e. choosing $h_k \in \mathcal{O}_X(U_k)^\ast$ compatibly.

The following proposition follows directly from the definition of transition functions.

::: Proposition 2 (Cocycle condition)
The transition functions $\{g_{ij}\}$ satisfy the following *cocycle condition*:

1. $g_{ii} = 1$ for all $i$.
2. $g_{ij} = g_{ji}^{-1}$ for all $i, j$.
3. $g_{ij} g_{jk} = g_{ik}$ on $U_i \cap U_j \cap U_k$ for all $i, j, k$.
:::

::: Example 3
The *trivial line bundle* $X \times \mathbb{A}^1$ is the line bundle all of whose transition functions are $g_{ij} = 1$. This is the simplest line bundle with no twist.
:::

Thus the second condition of [Definition 1](#def1) means that the line bundle $\mathcal{L}$ becomes isomorphic to the trivial line bundle when restricted to a suitable open set $U \subseteq X$.

[Proposition 2](#prop2) is the usual gluing condition, and by this condition a line bundle can be thought of as a kind of sheaf. ([\[Topology\] §Sheaves, ⁋Definition 1](/en/math/topology/sheaves#def1)) Concretely, given a line bundle $\mathcal{L}$, we define its sheaf of sections by

$$U\mapsto \mathcal{O}_X(\mathcal{L})(U)=\{s: U \rightarrow \mathcal{L} \mid \pi \circ s = \id_U\}.$$

That is, $\mathcal{O}_X(\mathcal{L})$ is the sheaf of sections of the surjection $\pi$. ([\[Topology\] §Sheaves, ⁋Example 9](/en/math/topology/sheaves#ex9))

Then by the local trivialization $\phi_i: \pi^{-1}(U_i) \rightarrow U_i \times \mathbb{A}^1$ we have $\mathcal{O}_X(\mathcal{L})\vert_{U_i} \cong \mathcal{O}_{U_i}$. Hence over $U_i$ we may think of these sections locally as ordinary $\mathbb{K}$-valued functions.

This means the following.

::: Definition 4
An $\mathcal{O}_X$-module $\mathcal{F}$ is called *invertible* if for every point $p \in X$ there is a neighborhood $U$ such that $\mathcal{F}\vert_U \cong \mathcal{O}_U$ as an $\mathcal{O}_U$-module.
:::

What we have shown above is that the sheaf of sections of a line bundle is invertible. The next proposition shows that the converse also holds.

::: Proposition 5
The sheaf of sections $\mathcal{O}_X(\mathcal{L})$ of a line bundle $\mathcal{L}$ is an invertible sheaf. Conversely, every invertible sheaf arises, uniquely up to isomorphism, from a line bundle.
:::

::: Proof
For an invertible sheaf $\mathcal{F}$, one can define transition functions from the local isomorphisms $\mathcal{F}\vert_{U_i} \cong \mathcal{O}_{U_i}$, and from these reconstruct a line bundle.
:::

By this proposition we know that line bundles and invertible sheaves are the same concept. For this reason, when denoting a line bundle we use $\mathcal{L}$ rather than the roman $L$ used to denote a space.

## Operations on Line Bundles

In the world of differential geometry it is natural to construct new bundles by bringing over fiberwise the operations of linear algebra. The same is true in algebraic geometry; since we are currently looking at line bundles, what we need to examine are $\otimes$ and $\Hom$, and in particular the dual $(-)^\vee$.

::: Proposition 6
The tensor product $\mathcal{L} \otimes \mathcal{M}$ of two line bundles $\mathcal{L}, \mathcal{M}$ is also a line bundle. Its transition functions are $\{g_{ij} h_{ij}\}$, where $\{g_{ij}\}, \{h_{ij}\}$ are the transition functions of $\mathcal{L}, \mathcal{M}$ respectively.
:::
::: Proof
The fiber of the tensor product is $\mathcal{L}_p \otimes_{\mathbb{K}} \mathcal{M}_p$, which is again one-dimensional since it is the tensor product of two one-dimensional vector spaces. The transition function is the product of $\phi_j \circ \phi_i^{-1}$ and $\psi_j \circ \psi_i^{-1}$, hence $g_{ij} h_{ij}$.
:::

For any line bundle $\mathcal{L}$, the dual bundle $\mathcal{L}^\vee$ is the bundle whose fibers are given by

$$\mathcal{L}_x^\vee=\Hom_\mathbb{K}(\mathcal{L}_x, \mathbb{K}).$$

If we think of line bundles as (invertible) sheaves following [Proposition 5](#prop5), then $\mathcal{L}^\vee$ corresponds to the sheaf Hom $\sHom_{\mathcal{O}_X}(\mathcal{L}, \mathcal{O}_X)$.

::: Proposition 7
The *dual bundle* $\mathcal{L}^\vee$ of a line bundle $\mathcal{L}$ is also a line bundle, and its transition functions are $\{g_{ij}^{-1}\}$.
:::

::: Proof
The fiber of the dual bundle is $\mathcal{L}_p^\vee = \Hom_{\mathbb{K}}(\mathcal{L}_p, \mathbb{K})$, which is again one-dimensional since it is the dual of a one-dimensional vector space. The transition function is the inverse of $g_{ij}$.
:::

The following proposition shows the relation between $\otimes$ and $(-)^\vee$, which plays an important role in defining the Picard group.

::: Proposition 8
For any line bundle $\mathcal{L}$ we have $\mathcal{L} \otimes \mathcal{L}^\vee \cong \mathcal{O}_X$.
:::

::: Proof
The transition functions of $\mathcal{L} \otimes \mathcal{L}^\vee$ are $g_{ij} \cdot g_{ij}^{-1} = 1$, so it is the trivial bundle.
:::

As always, we can understand the structure of a line bundle by looking at it over a sufficiently small affine open set. Consider a line bundle $\mathcal{L}$ and choose an affine open subset $U_i$ on which $\mathcal{L}$ is trivial. Then the projection map

$$\pi\vert_{\pi^{-1}(U_i)}:\pi^{-1}(U_i) \rightarrow U_i$$

is a morphism between affine varieties, and hence induces a ring homomorphism between coordinate rings by [§Affine Varieties, ⁋Proposition 16](/en/math/algebraic_varieties/affine_varieties#prop16). This ring homomorphism makes the coordinate ring of $\pi^{-1}(U_i)$ into an algebra over the coordinate ring $A$ of $U_i$, and the $A$-module $\mathcal{O}_X(\mathcal{L})(U_i)$ formed by the sections of $\pi$ is identified with $A$ via the trivialization $\phi_i$, so it is a free module of rank $1$. Since $\mathcal{L}$ is trivial over any open subset of $U_i$, we see that a line bundle becomes, affine-locally, an invertible module over the coordinate ring. ([\[Commutative Algebra\] §Fractional Ideals, ⁋Definition 1](/en/math/commutative_algebra/fractional_ideals#def1)) Then the operations $\otimes$ and $\vee$ defined on line bundles come from the operations of [\[Commutative Algebra\] §Fractional Ideals, ⁋Theorem 3](/en/math/commutative_algebra/fractional_ideals#thm3), and therefore it is not unnatural to adopt the following name following [\[Commutative Algebra\] §Fractional Ideals, ⁋Definition 5](/en/math/commutative_algebra/fractional_ideals#def5).

::: Definition 9
The *Picard group* $\Pic(X)$ of a variety $X$ is the group obtained by taking the set of isomorphism classes of line bundles on $X$ with tensor product as the operation. The identity element is the trivial bundle $\mathcal{O}_X$, and the inverse of $\mathcal{L}$ is $\mathcal{L}^\vee$.
:::

That the trivial bundle actually serves as the identity element can be checked directly from [Example 3](#ex3) and [Proposition 6](#prop6). Moreover, by the properties of the tensor product the following holds.

::: Proposition 10
$\Pic(X)$ is an abelian group.
:::

::: Proof
By [Proposition 6](#prop6) the tensor product is a binary operation on line bundles, and by [Proposition 8](#prop8) $\mathcal{O}_X$ is the identity and $\mathcal{L}^\vee$ is the inverse of $\mathcal{L}$. The commutativity $\mathcal{L} \otimes \mathcal{M} \cong \mathcal{M} \otimes \mathcal{L}$ and associativity $(\mathcal{L} \otimes \mathcal{M}) \otimes \mathcal{N} \cong \mathcal{L} \otimes (\mathcal{M} \otimes \mathcal{N})$ of the tensor product follow directly at the level of transition functions from $g_{ij}h_{ij} = h_{ij}g_{ij}$ and $(g_{ij}h_{ij})k_{ij} = g_{ij}(h_{ij}k_{ij})$.
:::

As in the previous post, our toy examples are $\mathbb{A}^n$ and $\mathbb{P}^n$.

::: Example 11
The coordinate ring $R = \mathbb{K}[\x_1, \ldots, \x_n]$ of $\mathbb{A}^n$ is a Noetherian UFD, and by the above discussion line bundles on $\mathbb{A}^n$ correspond to invertible modules over $R$. By [\[Commutative Algebra\] §Fractional Ideals, ⁋Theorem 4](/en/math/commutative_algebra/fractional_ideals#thm4) an invertible module over a Noetherian UFD is free, so $\Pic(\mathbb{A}^n) = 0$.
:::


::: Example 12
We define the line bundle $\mathcal{O}_{\mathbb{P}^n}(d)$ on $\mathbb{P}^n$ as follows. First, each standard open set

$$U_i = \{[x_0 : \cdots : x_n] \mid x_i \ne 0\}$$

is a trivializing open set for this bundle. We explicitly define the trivialization over each of these by

$$\phi_i\colon \mathcal{O}(d)\vert_{U_i} \xrightarrow{\sim} \mathcal{O}_{U_i}, \qquad \phi_i(s) = s \cdot \x_i^{-d}.$$

From this we know that the space of sections has the form

$$\mathcal{O}(d)(U_i) = \x_i^d \cdot \mathcal{O}(U_i) = \x_i^d\mathbb{K}[\x_0/\x_i, \ldots, \widehat{\x_i/\x_i}, \ldots, \x_n/\x_i].$$

Now comparing the two trivializations on $U_i \cap U_j$, we can derive the transition function. That is, the transition function $\phi_j \circ \phi_i^{-1}\colon \mathcal{O}_{U_i}\vert_{U_i \cap U_j} \rightarrow \mathcal{O}_{U_j}\vert_{U_i \cap U_j}$ is

$$\phi_j \circ \phi_i^{-1}(f) = (\x_i/\x_j)^d \cdot f,$$

so we obtain $g_{ij} = (\x_i/\x_j)^d$. More concretely, for each point $x \in U_i \cap U_j$ and fiber $v \in \mathcal{O}_{\mathbb{P}^n}(d)_x \cong \mathbb{A}^1$ at that point,

$$g_{ij}(x)\colon v \mapsto (\x_i/\x_j)^d(x) \cdot v.$$

Now we can define a group homomorphism

$$\mathbb{Z}\rightarrow \Pic(\mathbb{P}^n);\qquad d\mapsto [\mathcal{O}_{\mathbb{P}^n}(d)].$$

Our claim is that this is an isomorphism. First, for any line bundle $\mathcal{L}$, since $\mathcal{L}\vert_{U_i}$ is isomorphic to the trivial line bundle by [Example 11](#ex11), the transition functions $h_{ij}$ on each $U_i\cap U_j$ completely determine $\mathcal{L}$. But by definition $h_{ij}\in \mathcal{O}_{\mathbb{P}^n}(U_i\cap U_j)^\ast$ on $U_i\cap U_j$, so $h_{ij}$ must be of the form $c_{ij}(\x_i/\x_j)^d$. Since a line bundle whose transition functions differ by a constant is trivial, we see from this that the above group homomorphism is surjective. Similarly, assuming $\mathcal{O}_{\mathbb{P}^n}(d)\cong \mathcal{O}_{\mathbb{P}^n}(d')$ and comparing transition functions, we obtain

$$\mathcal{O}_{\mathbb{P}^n}(d-d')\cong \mathcal{O}_{\mathbb{P}^n}(d)\otimes \mathcal{O}_{\mathbb{P}^n}(-d')\cong \mathcal{O}_{\mathbb{P}^n}(d)\otimes \mathcal{O}_{\mathbb{P}^n}(d')^\vee\cong \mathcal{O}_{\mathbb{P}^n}.$$

Now setting $e:=d-d'$, the statement $\mathcal{O}_{\mathbb{P}^n}(e)\cong \mathcal{O}_{\mathbb{P}^n}$ means that there exist $u_i\in \mathcal{O}(U_i)^\ast$ satisfying $(\x_i/\x_j)^e=u_i/u_j$; but since $U_i\cong \mathbb{A}^n$ we have $\mathcal{O}(U_i)^\ast=\mathbb{K}^\ast$, and therefore $(\x_i/\x_j)^e$ must be a constant, i.e. $e=0$. Hence it is also injective.
:::

Intuitively, the integer $d$ in the line bundle $\mathcal{O}_{\mathbb{P}^n}(d)$ on $\mathbb{P}^n$ can be understood as a measure of how many times the fiber twists as it moves over the base. When $d=0$, $\mathcal{O}(0)$ is the trivial bundle so there is no twist; when $d>0$ it twists $d$ times in one direction, and when $d<0$ it twists $\lvert d\rvert$ times in the opposite direction. This means that $d$ directly indicates the amount of twisting, as seen from the transition function $g_{ij}(x) = (x_i/x_j)^d(x)$. However, this intuition may be somewhat imprecise, so a little explanation will be added after [Example 16](#ex16).

On the other hand, on the projective space $\mathbb{P}^n$ there is a special line bundle naturally induced by its very definition. This *tautological bundle* is the bundle that assigns to each point of $\mathbb{P}^n$ the line represented by that point, and it plays a fundamental role in understanding the geometry of projective space.

::: Definition 13
For each point $x = [x_0 : \cdots : x_n]$ of $\mathbb{P}^n$, consider the space obtained by attaching to each point the line $\ell_x = \{(\lambda x_0, \ldots, \lambda x_n) \mid \lambda \in \mathbb{K}\}$ passing through the origin of $\mathbb{A}^{n+1}$:

$$\mathcal{O}_{\mathbb{P}^n}(-1) = \{(x, v) \in \mathbb{P}^n \times \mathbb{A}^{n+1} \mid v \in \ell_x\}.$$

Then the line bundle defined by the projection map $\pi=\pr_1$ from $\mathcal{O}_{\mathbb{P}^n}(-1)$ to $\mathbb{P}^n$ is called the *tautological line bundle* over $\mathbb{P}^n$.
:::

That is, in this definition each fiber $\mathcal{O}_{\mathbb{P}^n}(-1)_x$ is exactly the line represented by the point $x$. As the notation suggests, the following holds. For distinction, in the next proposition only, let us regard $\mathcal{O}_{\mathbb{P}^n}(-1)$ as the bundle from [Definition 13](#def13), not from [Example 12](#ex12).

::: Proposition 14
The tautological bundle $\mathcal{O}_{\mathbb{P}^n}(-1)$ is the dual of $\mathcal{O}_{\mathbb{P}^n}(1)$ defined in [Example 12](#ex12) above. That is, $\mathcal{O}_{\mathbb{P}^n}(-1) \cong \mathcal{O}_{\mathbb{P}^n}(1)^\vee$.
:::

::: Proof
Let us construct a local trivialization of $\mathcal{O}_{\mathbb{P}^n}(-1)$ over the standard open cover $U_i = \{x \mid x_i \ne 0\}$. Since for any $(x, v) \in \mathcal{O}_{\mathbb{P}^n}(-1)$ we can write $v = \lambda x$ ($\lambda \in \mathbb{K}$), defining $\phi_i(x, v) = (x, v_i)$ gives $\phi_i: \pi^{-1}(U_i) \rightarrow U_i \times \mathbb{A}^1$. The inverse map is $\phi_i^{-1}(x, t) = (x, (t/x_i)x)$. The transition function on $U_i \cap U_j$ is obtained from $\phi_j \circ \phi_i^{-1}(x, t) = (x, t x_j / x_i)$ as $g_{ij}(x) = x_j/x_i$. This is the inverse of the transition function $x_i/x_j$ of $\mathcal{O}_{\mathbb{P}^n}(1)$.
:::

In particular, examining $\mathcal{O}(-1)$ on $\mathbb{P}^1$, the meaning of the *twist* described intuitively above becomes much clearer. The process of forming $\mathbb{P}^1$ from $\mathbb{A}^2\setminus \{0\}$ can be thought of as first radially projecting $\mathbb{A}^2\setminus\{0\}$ onto the unit circle, then identifying antipodal points on the unit circle; in this process, vectors pointing in opposite directions become identified, which is exactly the phenomenon of the fiber twisting. One way to see this twist is to look at sections of a line bundle $\mathcal{L}$.

::: Definition 15
We write $\Gamma(X, \mathcal{L})$ for the space of *global sections* of a line bundle $\mathcal{L}$. That is, $\Gamma(X, \mathcal{L})$ is the set of regular maps assigning to each point $x\in X$ an element in the fiber $\pi^{-1}(x)\subseteq \mathcal{L}$.
:::

Another popular notation for the global section space is $H^0(X, \mathcal{L})$. This notation will be justified in [\[Algebraic Varieties\] §Sheaf Cohomology, ⁋Definition 1](/en/math/algebraic_varieties/sheaf_cohomology#def1), but until then we shall use $\Gamma(X, \mathcal{L})$.

::: Example 16
The only global section of $\mathcal{O}_{\mathbb{P}^n}(-1)$ is $0$. That is,

$$\Gamma(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n}(-1)) = 0.$$

To verify this, by [Example 12](#ex12) we have $\mathcal{O}(-1)(U_i) = \x_i^{-1} \cdot \mathbb{K}[\x_0/\x_i, \ldots, \widehat{\x_i/\x_i}, \ldots, \x_n/\x_i]$, and the trivialization is given by $\phi_i(s) = s \cdot \x_i$. Hence the trivialized section $\phi_i(s) \in \mathcal{O}(U_i) = \mathbb{K}[\x_0/\x_i, \ldots, \x_n/\x_i]$, and on $U_i \cap U_j$ the cocycle condition requires

$$\phi_j(s) = (\x_j/\x_i)\phi_i(s).$$

However, since $\phi_i(s) \in \mathbb{K}[\x_0/\x_i, \ldots, \widehat{\x_i/\x_i}, \ldots, \x_n/\x_i]$ cannot contain any $\x_i/\x_j$ term, for $(\x_j/\x_i)\phi_i(s)$ to lie in $\mathcal{O}(U_j) = \mathbb{K}[\x_0/\x_j, \ldots, \widehat{\x_j/\x_j}, \ldots, \x_n/\x_j]$ we must have $\phi_i(s) = 0$. Therefore $s = 0$.
:::

This proposition exhibits the *twist* of the tautological bundle from the viewpoint of sections. For instance, the fact that $\Gamma(\mathbb{P}^1, \mathcal{O}(-1))=0$ means in particular that there is not even a "constant function" assigning $1$ in the fiber at every $x\in \mathbb{P}^1$. From the geometric viewpoint above, this is because after going around $\mathbb{P}^1$ once, the original $1$ has become (for example) $-1$.

Meanwhile, the computation in [Example 16](#ex16) can be extended to arbitrary $d$; in particular, the same argument shows that $\Gamma(\mathbb{P}^1, \mathcal{O}(d))=0$ for any $d<0$, and for $d=0$, i.e. $\mathcal{O}_{\mathbb{P}^n}(0)=\mathcal{O}_{\mathbb{P}^n}$, one checks that the sections are homogeneous polynomials of degree $0$, i.e. constant functions, so the computation in [§Quasi-Projective Varieties, ⁋Example 6](/en/math/algebraic_varieties/quasi_projective_varieties#ex6) is recovered.

The case to pay attention to is $d>0$. In this case, by exactly the same computation as in [Example 16](#ex16), one verifies that the sections are homogeneous polynomials of degree $d$. In particular $\Gamma(\mathbb{P}^n, \mathcal{O}(d))\neq 0$, and this may be regarded as a computation showing that the intuition after [Example 12](#ex12) was somewhat overly simplistic.

A more precise explanation of this phenomenon is as follows. For convenience let us look at the example on $\mathbb{P}^1$. The sections of $\mathcal{O}(-1)$ are homogeneous of degree $-1$, so for instance they have the form

$$s([x_0:x_1])=\frac{a}{x_0}+\frac{b}{x_1},$$

and for this function to be defined on all of $\mathbb{P}^1$ we must necessarily have $a=b=0$. On the other hand, the sections of $\mathcal{O}(1)$ are homogeneous polynomials of degree $1$, so they are functions of the form

$$s([x_0:x_1])=ax_0+bx_1,$$

and unlike above there is no restriction on $a,b$. Intuitively, the sections of $\mathcal{O}(-1)$ cannot cross the zero section because of the denominators, and therefore every section cannot avoid the problem created by the twist of "$1$ attaching to $-1$". This same twist creates the same problem in $\mathcal{O}(1)$ as well: namely, the "constant section" $s([x_0:x_1])=1$ is likewise not a section in $\mathcal{O}(1)$. However, this time the sections of $\mathcal{O}(1)$ can cross the zero section, and therefore $\Gamma(\mathbb{P}^1, \mathcal{O}(1))\neq 0$. Understanding this from the viewpoint of transition functions or trivializations, one may think of it as follows: since $\mathcal{O}(d)$ multiplies by the degree $d$ polynomial $\x_i^d$, the trivialization can erase poles of degree at most $d$.

## Divisor -- Line Bundle Correspondence

We now establish the essential connection between divisors and line bundles. First we show that one can construct a line bundle from a Cartier divisor.

::: Definition 17
For a Cartier divisor $D = \{(U_i, f_i)\}$, we define the line bundle $\mathcal{O}_X(D)$ by the transition functions $g_{ij} = f_j/f_i$.
:::

That is, we take the trivial bundle over each $U_i$ and glue them over the overlaps using exactly the information contained in the Cartier divisor. If we view $\mathcal{O}_X(D)$ as a sheaf, i.e. consider the sheaf of sections of the line bundle defined above, then on each open set $U$ the sheaf $\mathcal{O}_X(D)(U)$ consists of functions satisfying

$$\divisor(f)+D\geq 0.$$

Thus $\mathcal{O}_X(D)$ is, if we regard $D$ as a codimension $1$ subvariety of $X$, the sheaf of rational functions that may have poles of order at most $1$ along $D$. Conversely, when $D$ is effective, $\mathcal{O}_X(-D)$ is given by

$$\divisor(f)-D\geq 0,$$

which is exactly the sheaf of functions vanishing on $D$. That is,

$$\mathcal{O}_X(-D)(U)=\{f\in \mathcal{O}_X(U)\mid \text{$f$ vanishes on $D\cap U$}\},$$

and from this we obtain the short exact sequence

$$0\rightarrow \mathcal{O}_X(-D)\rightarrow \mathcal{O}_X\rightarrow \mathcal{O}_D\rightarrow 0.$$

Then $\mathcal{O}_X(-D)$ is the sheaf of ideals defining $D$, and for this reason we write it as $\mathcal{I}_D$ and call it the *ideal sheaf*.

::: Proposition 18
The above definition is well-defined. That is, equivalent Cartier divisors define isomorphic line bundles.
:::

::: Proof
If two Cartier divisors $\{(U_i, f_i)\}$ and $\{(V_j, g_j)\}$ are equivalent, then $f_i/g_j \in \mathcal{O}_X(U_i \cap V_j)^\ast$. Let us compare the two line bundles on the common refinement $\{U_i \cap V_j\}$ and set $u_{ij} := g_j/f_i \in \mathcal{O}_X(U_i \cap V_j)^\ast$. Then on $(U_i \cap V_j) \cap (U_k \cap V_l)$ the transition functions of the two line bundles are respectively $f_k/f_i$ and

$$\frac{g_l}{g_j} = \frac{u_{kl} f_k}{u_{ij} f_i} = \frac{u_{kl}}{u_{ij}} \cdot \frac{f_k}{f_i}.$$

That is, they differ only by the units $\{u_{ij}\}$, and hence the two line bundles are identified by the isomorphism they define.
:::

For example, for any principal divisor $\divisor(f)$ the transition function is $1$, so it becomes the trivial bundle. We now summarize the relationship between line bundles and Cartier divisors.

::: Proposition 19
For any variety $X$, we have $\Pic(X) \cong \CaCl(X)$.
:::

::: Proof
First we verify that $D \mapsto \mathcal{O}_X(D)$ is a group homomorphism from $\CaDiv(X)$ to $\Pic(X)$. For a Cartier divisor $D = \{(U_i, f_i)\}$, the transition function of $\mathcal{O}_X(D)$ is $g_{ij} = f_j/f_i \in \mathcal{O}_X(U_i \cap U_j)^\times$, so it defines a line bundle. Moreover, writing two Cartier divisors $D = \{(U_i, f_i)\}$ and $D' = \{(U_i, f_i')\}$ on a common refinement with the same cover, we have $D + D' = \{(U_i, f_i f_i')\}$ and its transition function is $(f_j f_j')/(f_i f_i') = g_{ij} g_{ij}'$, so by [Proposition 6](#prop6) we obtain $\mathcal{O}_X(D + D') \cong \mathcal{O}_X(D) \otimes \mathcal{O}_X(D')$. That is, $D \mapsto \mathcal{O}_X(D)$ is additive. A principal divisor $\divisor(h)$ corresponds to the trivial bundle since its transition function is $1$, and hence we obtain a well-defined group homomorphism from $\CaCl(X) = \CaDiv(X)/\Prin(X)$ to $\Pic(X)$.

To show that this is an isomorphism, suppose an arbitrary line bundle $\mathcal{L}$ is given. On a trivializing open set $U \subseteq X$ we have $\mathcal{L}\vert_U \cong \mathcal{O}_U$, so we can pick $s \in \mathcal{L}(U)$ corresponding to the constant section $1$ of $\mathcal{O}_U$, and this $s$ is a nonzero rational section. Now consider a trivializing cover $\{U_i\}$ of $\mathcal{L}$. Choose on each $U_i$ a trivialization $\psi_i\colon \mathcal{L}\vert_{U_i} \cong \mathcal{O}_{U_i}$, and define $f_i := \psi_i(s\vert_{U_i \cap U}) \in \mathcal{O}_X(U_i \cap U) \subseteq \mathbb{K}(X)$. Then on $U_i \cap U_j \cap U$ we have $f_j = g_{ij} f_i$, and since $X$ is irreducible, $U_i \cap U_j \cap U$ is a dense open subset of $U_i \cap U_j$, so this relation holds on all of $U_i \cap U_j$. That is, $f_j/f_i = g_{ij} \in \mathcal{O}_X(U_i \cap U_j)^\times$, so $D = \{(U_i, f_i)\}$ is a Cartier divisor, and since the transition function of $\mathcal{O}_X(D)$ is $\{g_{ij}\}$, we have $\mathcal{O}_X(D) \cong \mathcal{L}$.

Finally we show injectivity. Write two Cartier divisors $D = \{(U_i, f_i)\}$ and $D' = \{(U_i, f_i')\}$ on a common refinement with the same cover, and suppose $\mathcal{O}_X(D) \cong \mathcal{O}_X(D')$. The transition functions of two isomorphic line bundles differ by suitable units $u_i \in \mathcal{O}_X(U_i)^\times$ as

$$\frac{f_j'}{f_i'} = \frac{u_j}{u_i} \cdot \frac{f_j}{f_i}.$$

Rewriting this relation, on $U_i \cap U_j$ we have $u_i f_i/f_i' = u_j f_j/f_j'$, so $h := u_i f_i/f_i'$ defines a single rational function $h \in \mathbb{K}(X)^\times$ independent of the choice of $i$. Since $u_i$ is a unit on each $U_i$, we have $\divisor(u_i) = 0$ and $\divisor(h) = \divisor(f_i) - \divisor(f_i')$, hence $D - D' = \divisor(h)$, i.e. the two Cartier divisors are linearly equivalent.
:::

If $X$ is smooth, we already know that $\CaCl(X)\cong \Cl(X)$.

## Pullback of Line Bundles

Given a morphism $\varphi: X \rightarrow Y$, the operation of "pulling back" a line bundle on $Y$ to $X$ is defined naturally. For example, pulling a hypersurface on $Y$ back to $X$ via $\varphi$ should pull back the corresponding line bundle as well. This pullback operation induces a group homomorphism between Picard groups, and in the case of an embedding it can be understood as restricting line bundles from the ambient space to the subvariety.

::: Proposition 20
For a morphism $\varphi: X \rightarrow Y$ and a line bundle $\mathcal{L}$ on $Y$, the *pullback* $\varphi^\ast \mathcal{L}$ is a line bundle on $X$. Its transition functions are $\{g_{ij} \circ \varphi\}$, where $\{g_{ij}\}$ are the transition functions of $\mathcal{L}$.
:::

::: Proof
Suppose the line bundle $\mathcal{L}$ is given by transition functions $\{g_{ij}\}$ over an open cover $\{U_i\}$. The pullback $\varphi^\ast \mathcal{L}$ is defined by transition functions $\{g_{ij} \circ \varphi\}$ over the open cover $\{\varphi^{-1}(U_i)\}$. To verify that $\varphi^\ast \mathcal{L}$ is a line bundle on $X$, it suffices to check that the transition functions satisfy the cocycle condition.

We check all three cocycle conditions.

1. $g_{ii} \circ \varphi = 1 \circ \varphi = 1$ since $g_{ii} = 1$.
2. $(g_{ij} \circ \varphi)(g_{ji} \circ \varphi) = (g_{ij} g_{ji}) \circ \varphi = 1 \circ \varphi = 1$ since $g_{ij} g_{ji} = 1$.
3. $(g_{ij} \circ \varphi)(g_{jk} \circ \varphi) = (g_{ij} g_{jk}) \circ \varphi = g_{ik} \circ \varphi$ since $g_{ij} g_{jk} = g_{ik}$.

Hence $\{g_{ij} \circ \varphi\}$ satisfies the cocycle condition.
:::

::: Proposition 21
Pullback induces a group homomorphism $\varphi^\ast: \operatorname{Pic}(Y) \rightarrow \operatorname{Pic}(X)$.
:::

::: Proof
Since $\varphi^\ast(\mathcal{L} \otimes \mathcal{M}) \cong \varphi^\ast \mathcal{L} \otimes \varphi^\ast \mathcal{M}$ and $\varphi^\ast \mathcal{O}_Y \cong \mathcal{O}_X$, pullback is a group homomorphism.

To verify this, let us look from the viewpoint of transition functions. The transition function of $\mathcal{L} \otimes \mathcal{M}$ is $g_{ij}^{\mathcal{L}} g_{ij}^{\mathcal{M}}$, so the transition function of $\varphi^\ast(\mathcal{L} \otimes \mathcal{M})$ is $(g_{ij}^{\mathcal{L}} g_{ij}^{\mathcal{M}}) \circ \varphi = (g_{ij}^{\mathcal{L}} \circ \varphi)(g_{ij}^{\mathcal{M}} \circ \varphi)$. These are respectively the transition functions of $\varphi^\ast\mathcal{L}$ and $\varphi^\ast\mathcal{M}$, so we obtain $\varphi^\ast(\mathcal{L} \otimes \mathcal{M}) \cong \varphi^\ast\mathcal{L} \otimes \varphi^\ast\mathcal{M}$. Moreover, since the transition functions of $\mathcal{O}_Y$ are all $1$, the transition functions of $\varphi^\ast\mathcal{O}_Y$ are also $1$, i.e. $\varphi^\ast\mathcal{O}_Y \cong \mathcal{O}_X$.
:::

::: Example 22
For an embedding $i: C \hookrightarrow \mathbb{P}^n$, the pullback $i^\ast \mathcal{O}_{\mathbb{P}^n}(1)$ is a line bundle on the curve $C$. We call this the *hyperplane bundle* on $C$ and denote it by $\mathcal{O}_C(1)$. In general $\mathcal{O}_C(1)$ is nontrivial; for instance, when $\mathbb{P}^1$ is embedded as a line in $\mathbb{P}^n$, the bundle $\mathcal{O}_C(1) = \mathcal{O}_{\mathbb{P}^1}(1)$ on $C = \mathbb{P}^1$ is nontrivial, as we saw in [Example 12](#ex12). The name "hyperplane bundle" comes from the fact that it is obtained by pulling back to $C$ the line bundle $\mathcal{O}_{\mathbb{P}^n}(1)$ corresponding to a hyperplane $H$, i.e. a hypersurface of degree $1$ in $\mathbb{P}^n$.
:::

## Vector Bundle

So far we have examined line bundles, whose fibers are one-dimensional vector spaces. We can generalize this notion to *vector bundles*, whose fibers are higher-dimensional vector spaces. Vector bundles capture structures that arise naturally in geometry, such as tangent spaces and normal spaces of a variety, and are the algebraic-geometric analogues of tangent bundles and vector fields in differential geometry. A line bundle is precisely the special case of a vector bundle of rank 1, and many properties of line bundles become clearer from the perspective of vector bundle theory.

::: Definition 23
A *rank r vector bundle* $\mathcal{E}$ on a variety $X$ consists of the following data.

1. A projection $\pi: \mathcal{E} \rightarrow X$.
2. An open cover $\{U_i\}$ of $X$ and, for each $i$, a *local trivialization* $\phi_i: \pi^{-1}(U_i) \overset{\sim}{\longrightarrow} U_i \times \mathbb{A}^r$. The maps

    $$\phi_j \circ \phi_i^{-1}: (U_i \cap U_j) \times \mathbb{A}^r \rightarrow (U_i \cap U_j) \times \mathbb{A}^r$$

    have the form $(p, v) \mapsto (p, g_{ij}(p)v)$ for suitable *transition functions* $g_{ij} \in \GL_r(\mathcal{O}_X(U_i \cap U_j))$.
:::

Comparing with the definition of a line bundle, the only difference is that the fiber is $\mathbb{A}^r$ instead of $\mathbb{A}^1$, and the transition functions take values in $\GL_r(\mathcal{O}_X(U_i \cap U_j))$ rather than in $\mathcal{O}_X(U_i \cap U_j)^\times = \GL_1(\mathcal{O}_X(U_i \cap U_j))$. Hence a line bundle is exactly a rank 1 vector bundle.

The same cocycle condition as in [Proposition 2](#prop2) holds. However, since the transition functions are matrix-valued, one must be careful about the order of multiplication.

::: Example 24
The simplest example is the rank $r$ *trivial vector bundle* $\mathcal{O}_X^{\oplus r}$ obtained from the line bundle $\mathcal{O}_X$. This is constructed by taking the direct sum of $r$ copies of the line bundle $\mathcal{O}_X$.

Geometrically important objects are the tangent bundle and the cotangent bundle. The *tangent bundle* $\mathcal{T}_X$ is the vector bundle whose fiber over each point $p \in X$ is the tangent space $T_p X$; if $X$ is an $n$-dimensional smooth variety, it is a rank $n$ vector bundle, and in local coordinates $\x_1, \ldots, \x_n$ the partial derivatives $\partial/\partial \x_1, \ldots, \partial/\partial \x_n$ form a local frame. The *cotangent bundle* $\Omega_X^1 = \mathcal{T}_X^\vee$ is the dual of the tangent bundle, and in local coordinates $\dd{\x_1}, \ldots, \dd{\x_n}$ form a local frame.

Intuitively, $\Omega_X^1$ is the bundle of differential $1$-forms on $X$, so we can take their $r$-th exterior power to obtain the bundle of $r$-forms. Among these, the most interesting is the top exterior power $\omega_X = \bigwedge^n \Omega_X^1$, which is a rank $1$ vector bundle, i.e. a line bundle; in differential geometry this would be thought of as the bundle of volume forms. We call this the *canonical line bundle*.
:::

As above, we can define operations on vector bundles analogous to those for line bundles. The tensor product $\mathcal{E} \otimes \mathcal{F}$ of two vector bundles $\mathcal{E}, \mathcal{F}$ is defined by the fiberwise tensor product, and its transition functions are $g_{ij}^{\mathcal{E}} \otimes g_{ij}^{\mathcal{F}}$. The transition functions of the dual bundle $\mathcal{E}^\vee$ are $\left(g_{ij}^{\mathcal{E}}\right)^{-t}$ (inverse transpose). Moreover, the direct sum $\mathcal{E} \oplus \mathcal{F}$ is defined by the fiberwise direct sum, and in this case the transition functions become the block diagonal matrix $\begin{pmatrix} g_{ij}^{\mathcal{E}} & 0 \\ 0 & g_{ij}^{\mathcal{F}} \end{pmatrix}$.

## Tautological Bundle on Grassmannian

The tautological bundle $\mathcal{O}_{\mathbb{P}^n}(-1)$ on $\mathbb{P}^n$ defined above generalizes naturally to Grassmannians. The Grassmannian $\Gr(k, n)$ is the space of $k$-dimensional subspaces of an $n$-dimensional vector space, and in this generalization the tautological bundle becomes a rank $k$ vector bundle; the *quotient bundle* dual to it is also defined naturally.

::: Definition 25
We define the following two vector bundles on the Grassmannian $\Gr(k, n)$.

1. *Tautological bundle* $S$: a rank $k$ vector bundle that assigns to each point $[V] \in \Gr(k, n)$ (where $V \subseteq \mathbb{A}^n$ is a $k$-dimensional subspace) the subspace $V$ itself as its fiber.
   $$S = \{([V], v) \in \Gr(k, n) \times \mathbb{A}^n \mid v \in V\}$$

2. *Quotient bundle* $Q$: a rank $n-k$ vector bundle that assigns to each point $[V]$ the quotient space $\mathbb{A}^n / V$ as its fiber.
   $$Q = \{([V], [w]) \in \Gr(k, n) \times (\mathbb{A}^n / S) \mid [w] \in \mathbb{A}^n / V\}$$
:::

Between these there is a natural short exact sequence.

$$0 \rightarrow S \rightarrow \mathcal{O}_{\Gr(k,n)}^{\oplus n} \rightarrow Q \rightarrow 0$$

Here the middle term is $\Gr(k, n) \times \mathbb{A}^n$, the trivial bundle of rank $n$. The first morphism is the inclusion of each point $([V], v) \in S$ into $([V], v) \in \mathcal{O}^{\oplus n}$, and the second morphism is the quotient map sending $([V], w) \in \mathcal{O}^{\oplus n}$ to $([V], [w]) \in Q$.

::: Proposition 26
On $\Gr(1, n+1) = \mathbb{P}^n$, the tautological bundle $S$ is isomorphic to $\mathcal{O}_{\mathbb{P}^n}(-1)$.
:::

::: Proof
Each point of $\Gr(1, n+1)$ is a one-dimensional subspace of $\mathbb{A}^{n+1}$, i.e. a line through the origin. This corresponds exactly to a point of $\mathbb{P}^n$. Since each fiber of the tautological bundle $S$ is this line itself, it is identical to $\mathcal{O}_{\mathbb{P}^n}(-1)$ defined in [Definition 13](#def13).
:::

This proposition shows that the tautological bundle on a Grassmannian reduces to the familiar $\mathcal{O}(-1)$ on projective space. As for the quotient bundle $Q$, on $\Gr(1, n+1) = \mathbb{P}^n$ it has rank $n$ and is closely related to the tangent bundle $\mathcal{T}_{\mathbb{P}^n}$. Indeed, we have $\mathcal{T}_{\mathbb{P}^n} \cong \Hom(S, Q) \cong S^\vee \otimes Q$.

---

**References**

**[Hart]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.
