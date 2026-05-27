---title: "Complete Intersections"
excerpt: "Codimension of vanishing schemes and complete intersections"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/complete_intersections
header:
    overlay_image: /assets/images/Math/Algebraic_Varieties/Complete_intersections.png
    overlay_filter: 0.5
sidebar: 
    nav: "scheme_theory-en"

date: 2025-03-08
last_modified_at: 2025-03-08
weight: 15
translated_at: 2026-05-28T11:36:15+00:00
translation_source: kimi-cli
---
From dimension

An important example of closed subschemes is the vanishing scheme defined in [§Closed Subschemes, ⁋Definition 7](/en/math/scheme_theory/closed_subschemes); the motivation for this is naturally the hypersurface $$f=0$$ in Euclidean space $$\mathbb{R}^n$$ defined by $$f^{-1}(0)$$ for a function $$f: \mathbb{R}^n \rightarrow \mathbb{R}$$.

Meanwhile, we are also interested more generally in the vanishing scheme $$Z(s_1,\ldots, s_k)$$ defined by a (finite) family of global sections $$s_1,\ldots, s_k\in \Gamma(X, \mathscr{O}_X)$$. Intuitively, this is obtained by first considering the vanishing scheme $$\iota_1:Z(s_1)\hookrightarrow X$$ using the global section $$s_1$$ on $$X$$, then iterating the process of finding the vanishing scheme of $$s_2\vert_{Z(s_1)}$$ on $$Z(s_1)$$ through the global section

$$s_2\vert_{Z(s_1)}=\iota^\sharp(X)(s_2)\in(\iota_1)_\ast \mathscr{O}_{Z(s_1)}(X)=\Gamma(Z(s_1), \mathscr{O}_{Z(s_1)})$$

; of course, for this to work, this process must yield the same scheme regardless of the order of $$s_1, \ldots, s_k$$.


## Locally principal embedding

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A closed embedding $$\iota: Z \hookrightarrow X$$ is said to be *locally principal* if there exists an open cover $$\{U_i\}$$ of $$X$$ such that, for each of the closed embeddings

$$\iota\vert^{U_i}: \iota^{-1}(U_i) \rightarrow U_i$$

obtained by restricting the codomain of $$\iota$$ to each $$U_i$$, there exists a suitable $$s_i\in \Gamma(U_i, \mathscr{O}_X)$$ such that the two closed embeddings $$\iota\vert^{U_i}$$ and $$Z(s_i)\hookrightarrow U_i$$ are isomorphic.

</div>

Now if $$\iota: Z\hookrightarrow X$$ is locally principal, then by covering each of the $$U_i$$ in the definition with affine open sets and restricting the $$s_i$$ to these, we may assume that $$\{U_i\}$$ is an affine open covering.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> A closed embedding $$\iota: Z \hookrightarrow X$$ is called an *effective Cartier divisor* if there exists an affine open cover $$\{U_i=\Spec A_i\}$$ of $$X$$ such that, for each of the closed embeddings

$$\iota\vert^{U_i}:\iota^{-1}(U_i) \rightarrow U_i$$

there exists a suitable non-zerodivisor $$s_i\in A_i=\Gamma(U_i, \mathscr{O}_X)$$ such that the two closed embeddings $$\iota^{U_i}$$ and $$Z(s_i)\hookrightarrow U_i$$ are isomorphic.

</div>

By definition, a locally principal embedding is roughly one whose ideal sheaf is generated (locally) by a single element, i.e., a principal ideal; an effective Cartier divisor is one for which this single element can be taken to be a non-zerodivisor over a suitable affine cover. Thus every effective Cartier divisor is locally principal, but the converse does not hold.
