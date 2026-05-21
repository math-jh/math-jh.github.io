---
title: "Line Bundles and Vector Bundles"
excerpt: "Line bundles, invertible sheaves, and the Picard group"

categories: [Math / Algebraic Varieties]
permalink: /en/math/algebraic_varieties/line_bundles
sidebar:
    nav: "algebraic_varieties-en"

header:
    overlay_image: /assets/images/Math/Algebraic_Varieties/Line_Bundles.png
    overlay_filter: 0.5

date: 2026-03-25
last_modified_at: 2026-04-08
weight: 9
translated_at: 2026-05-21T07:30:02+00:00
translation_source: kimi-cli
---
In the previous post we defined divisors on a variety $X$, and saw that their linear equivalence classes form $\Cl(X)$. However, not every divisor comes from the zeros and poles of some rational function. For example, since $\Cl(\mathbb{P}^n) \cong \mathbb{Z}$ ([§Divisors, ⁋Example 11](/en/math/algebraic_varieties/divisors#ex11)), a general divisor $dH$ on $\mathbb{P}^n$ appears as the zero set of some function only when $d \ge 0$.

To overcome this restriction we introduce *line bundles*. A line bundle $\mathcal{L}$ is a geometric object that assigns a one-dimensional vector space to each point $p \in X$, and a section $s$ of $\mathcal{L}$ naturally defines a divisor $\divisor(s)$. From this perspective, for any divisor $D$ we can construct a line bundle $\mathcal{O}_X(D)$, and its sections correspond to divisors greater than or equal to $D$. In other words, line bundles allow us to treat divisors independently, free from the constraint of being zeros or poles of a function.

## Definition of a Line Bundle

Line bundles, and vector bundles which we will define later in this post, are defined in the same way as in differential geometry and other fields. ([\[Differential Manifolds\] §Tangent and Cotangent Bundles, ⁋Definition 1](/en/math/manifold/tangent_and_cotangent_bundles#def1) or [\[Algebraic Topology\] §Characteristic Classes, ⁋Definition 2](/en/math/algebraic_topology/characteristic_classes#def2), etc.)

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A *line bundle* $\mathcal{L}$ over a variety $X$ consists of the following data.

1. A projection $\pi: \mathcal{L} \to X$.
2. An open cover $\{U_i\}$ of $X$ and for each $i$ a *local trivialization* $\phi_i: \pi^{-1}(U_i) \overset{\sim}{\longrightarrow} U_i \times \mathbb{A}^1$. The maps
    
    $$\phi_j \circ \phi_i^{-1}: (U_i \cap U_j) \times \mathbb{A}^1 \to (U_i \cap U_j) \times \mathbb{A}^1$$

    induced by these are of the form $(p, t) \mapsto (p, g_{ij}(p)t)$ for suitable *transition functions* $g_{ij} \in \mathcal{O}_X(U_i \cap U_j)^\ast$.

</div>

A *morphism* $\varphi \colon \mathcal{L} \to \mathcal{M}$ between two line bundles $\mathcal{L}, \mathcal{M} \to X$ defines a $\mathbb{K}$-linear map $\varphi_p \colon \mathcal{L}_p \to \mathcal{M}_p$ between fibers at each point $p \in X$, and can be expressed over a suitable open cover $\{U_k\}$ as an $\mathcal{O}_X(U_k)$-module homomorphism

$$\varphi_k \colon \mathcal{O}_{U_k} \to \mathcal{O}_{U_k}$$

and these satisfy

$$g^{\mathcal{M}}_{kl} \circ \varphi_l = \varphi_k \circ g^{\mathcal{L}}_{kl}.$$

Since the fiber of a line bundle is one-dimensional, each $\varphi_k$ is given by multiplication by a suitable $h_k \in \mathcal{O}_X(U_k)$, i.e. $s \mapsto h_k s$. When $\varphi$ is bijective on each fiber, we call it an *isomorphism* and write $\mathcal{L} \cong \mathcal{M}$. Since the fiber is one-dimensional, this is the same as giving a nonzero scalar at each point, i.e., equivalently, choosing $h_k \in \mathcal{O}_X(U_k)^\ast$ compatibly.

Then the following proposition follows directly from the definition of the cocycle condition.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2 (Cocycle condition)**</ins> The transition functions $\{g_{ij}\}$ satisfy the following *cocycle condition*.

1. $$g_{ii} = 1$$ for all $$i$$.
2. $$g_{ij} = g_{ji}^{-1}$$ for all $$i, j$$.
3. $$g_{ij} g_{jk} = g_{ik}$$ on $$U_i \cap U_j \cap U_k$$ for all $$i, j, k$$.

</div>

<div class="example" markdown="1">

<ins id="ex3">**Example 3**</ins> The *trivial line bundle* $X \times \mathbb{A}^1$ is the line bundle for which every transition function is $g_{ij} = 1$. This is the simplest line bundle, with no twist.

</div>

Thus the second condition of [Definition 1](#def1) means that the line bundle $\mathcal{L}$ is isomorphic to the trivial line bundle when restricted to a suitable open subset $U \subseteq X$.

[Proposition 2](#prop2) is the usual gluing condition, and by this condition a line bundle can be thought of as a kind of sheaf. ([\[Topology\] §Sheaves, ⁋Definition 1](/en/math/topology/sheaves#def1)) Specifically, given a line bundle $\mathcal{L}$, we define its sheaf of sections by

$$U\mapsto \mathcal{O}_X(\mathcal{L})(U)=\{s: U \to \mathcal{L} \mid \pi \circ s = \id_U\}.$$

That is, $\mathcal{O}_X(\mathcal{L})$ is the sheaf of sections of the surjection $\pi$. ([\[Topology\] §Sheaves, ⁋Example 9](/en/math/topology/sheaves#ex9))

Then by the local trivialization $\phi_i: \pi^{-1}(U_i) \to U_i \times \mathbb{A}^1$ we have $\mathcal{O}_X(\mathcal{L})\vert_{U_i} \cong \mathcal{O}_{U_i}$. Through this we can think of these sections locally over $U_i$ as ordinary $\mathbb{K}$-valued functions.

This means the following.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> A sheaf $\mathcal{F}$ is called *invertible* if in a neighborhood $U$ of each point $p \in X$ we have $\mathcal{F}\vert_U \cong \mathcal{O}_U$.

</div>

What we showed above is that the sheaf of sections of a line bundle is invertible. The following proposition shows that the converse also holds.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> The section sheaf $\mathcal{O}_X(\mathcal{L})$ of a line bundle $\mathcal{L}$ is an invertible sheaf. Conversely, every invertible sheaf comes from a unique line bundle.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

For an invertible sheaf $\mathcal{F}$, we can define transition functions from the local isomorphisms $\mathcal{F}\vert_{U_i} \cong \mathcal{O}_{U_i}$, and from these we can reconstruct the line bundle.

</details>

By this proposition we know that line bundles and invertible sheaves are the same concept. For this reason, when denoting a line bundle we use $\mathcal{L}$ instead of the roman $L$ used to denote a space.

## Operations on Line Bundles

In the world of differential geometry it is natural to construct new bundles by bringing in operations from linear algebra fiberwise. The same is true in algebraic geometry; since we are currently examining the case of line bundles, what we need to look at now are $\otimes$ and $\Hom$, and in particular the dual $(-)^\vee$.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> The tensor product $\
