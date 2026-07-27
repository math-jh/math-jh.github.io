---
title: "Closed Subschemes of Projective Space"
description: "Closed subschemes of projective space can be represented as zero sets of homogeneous polynomials. This property allows them to be studied in a manner almost identical to affine schemes."
excerpt: "Correspondence between closed subschemes of projective space and homogeneous ideals"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/closed_subschemes_of_projective_spaces
sidebar: 
    nav: "scheme_theory-en"

date: 2025-03-08
weight: 11
translated_at: 2026-07-27T21:45:03+00:00
translation_source: kimi-cli
last_polished_at: 2026-07-27T21:45:03+00:00
---
We now examine closed subschemes of $\mathbb{P}^n=\mathbb{P}_\mathbb{K}^n$ as examples of closed subschemes. Although $\mathbb{P}^n$ is slightly more complicated than affine schemes, it is still easier to handle than a general scheme, because by [[Projective Spaces and the Proj Construction] §..., ⁋Definition 4](/en/math/scheme_theory/projective_schemes#def4), any closed subset of $\mathbb{P}^n$ can always be written as the zero set of homogeneous polynomials in $\mathbb{K}[\x_0,\ldots, \x_n]$. In other words, although these homogeneous polynomials are not functions defined on $\mathbb{P}^n$, they at least allow us to represent closed subsets in a manner almost analogous to affine schemes.

In this post, we lift this correspondence to the level of schemes. That is, we show that a homogeneous ideal defines a closed subscheme of $\mathbb{P}^n$, and conversely that any closed subscheme of $\mathbb{P}^n$ arises in this way. Throughout this post, $A_\bullet=\mathbb{K}[\x_0,\ldots,\x_n]$ denotes the graded ring with its standard grading, and $\mathbb{P}^n=\Proj A_\bullet$.

## Construction of $V_+(\mathfrak{a})$

We already know that $\Proj$ is not a functor. This was because for a graded ring homomorphism $\phi_\bullet:A_\bullet \rightarrow B_\bullet$ and a homogeneous prime ideal $\mathfrak{q}$ not containing $B_+$, its inverse image $\phi^{-1}(\mathfrak{q})$ may contain $A_+$, so that even if $\mathfrak{q}$ is a point of $\Proj B_\bullet$, $\phi^{-1}(\mathfrak{q})$ need not be a point of $\Proj A_\bullet$. However, if $\phi_\bullet$ is a *surjection*, the situation changes. In this case $\phi(A_+)=B_+$, so $\phi^{-1}(\mathfrak{q})$ containing $A_+$ is equivalent to $\mathfrak{q}$ containing $B_+$, and thus $\mathfrak{q}$ would not have been a point of $\Proj B_\bullet$ to begin with, allowing us to avoid the problem. On the other hand, in the affine case a surjective ring homomorphism corresponds exactly to a closed subscheme (see the discussion after [[Closed Subschemes] §..., ⁋Proposition 3](/en/math/scheme_theory/closed_subschemes#prop3)), and the same holds for projective space.

::: Proposition 1
Let a homogeneous ideal $\mathfrak{a}\subseteq A_\bullet$ and the canonical projection $\pi:A_\bullet \rightarrow A_\bullet/\mathfrak{a}$ be given. Then $\pi$ induces a closed embedding

$$\iota:\Proj (A_\bullet/\mathfrak{a}) \rightarrow \Proj A_\bullet=\mathbb{P}^n$$

whose image is $Z_+(\mathfrak{a})$.
:::
::: Proof
As we saw in [[Algebraic Structures] §Graded Rings](/en/math/algebraic_structures/graded_rings), $A_\bullet/\mathfrak{a}$ is a graded ring, and the ideal correspondence for quotient rings sends homogeneous ideals to homogeneous ideals. Since $\pi$ is surjective, $\pi(A_+)=(A_\bullet/\mathfrak{a})_+$, and thus $\mathfrak{q}$ not containing $(A_\bullet/\mathfrak{a})_+$ is equivalent to $\pi^{-1}(\mathfrak{q})$ not containing $A_+$. In particular, $\mathfrak{q}\mapsto \pi^{-1}(\mathfrak{q})$ is a bijection from the points of $\Proj(A_\bullet/\mathfrak{a})$, i.e., homogeneous prime ideals not containing $(A_\bullet/\mathfrak{a})_+$, to the homogeneous prime ideals of $A_\bullet$ containing $\mathfrak{a}$ but not $A_+$, and the latter are exactly $Z_+(\mathfrak{a})$. ([[Projective Spaces and the Proj Construction] §..., ⁋Definition 2](/en/math/scheme_theory/projective_schemes#def2)) Moreover, under this correspondence, a closed set of the form $Z_+(\bar{\mathfrak{b}})$ corresponds to $Z_+(\pi^{-1}(\bar{\mathfrak{b}}))\cap Z_+(\mathfrak{a})$, so $\iota$ is a homeomorphism onto its image $Z_+(\mathfrak{a})$.

We now verify the scheme morphism structure and the surjectivity of the sheaf morphism on the standard affine cover. For each $i$, write $\bar{\x}_i=\pi(\x_i)$; then by the above correspondence, $\iota^{-1}(D_+(\x_i))=D_+(\bar{\x}_i)$. Under the identification of the scheme structure on $\Proj$ from [[Projective Spaces and the Proj Construction] §..., ⁋Theorem 10](/en/math/scheme_theory/projective_schemes#thm10), namely $D_+(\x_i)\cong\Spec A_{(\x_i)}$ and $D_+(\bar\x_i)\cong \Spec (A_\bullet/\mathfrak{a})_{(\bar\x_i)}$, the restriction of $\iota$ is the morphism of affine schemes induced by the ring homomorphism

$$A_{(\x_i)} \rightarrow (A_\bullet/\mathfrak{a})_{(\bar\x_i)};\qquad \frac{f}{\x_i^d}\mapsto \frac{\pi(f)}{\bar\x_i^d}.$$

Since $\pi$ is surjective, this ring homomorphism is also surjective, and its kernel is, by exactness of localization,

$$\mathfrak{a}_{(\x_i)}=\left\{\frac{a}{\x_i^d}\middle\vert\text{$a\in\mathfrak{a}$ homogeneous of degree $d$}\right\}.$$

Thus $\iota$ is a closed embedding of the form $\Spec\bigl(A_{(\x_i)}/\mathfrak{a}_{(\x_i)}\bigr) \rightarrow \Spec A_{(\x_i)}$ on each chart, and these are compatible on the $D_+(\x_i\x_j)$. Indeed, under the identification of [[Projective Spaces and the Proj Construction] §..., ⁋Lemma 9](/en/math/scheme_theory/projective_schemes#lem9), $D_+(\x_i\x_j)$ is $\Spec A_{(\x_i\x_j)}$, and the composition of the above ring homomorphism with $A_{(\x_i)} \rightarrow A_{(\x_i\x_j)}$ is given by $f/(\x_i\x_j)^d\mapsto \pi(f)/(\bar\x_i\bar\x_j)^d$, which is symmetric in the roles of $i$ and $j$. Hence they glue to a single scheme morphism $\iota$. On the other hand, as the proof of [[Closed Subschemes] §..., ⁋Proposition 3](/en/math/scheme_theory/closed_subschemes#prop3) shows, it suffices to check that $\iota$ is a closed embedding on a single affine open cover, so $\iota$ is a closed embedding.
:::

We denote the closed subscheme thus obtained by $V_+(\mathfrak{a})$. That is, $V_+(\mathfrak{a})$ is $Z_+(\mathfrak{a})$ as a topological space, and $\Proj(A_\bullet/\mathfrak{a})$ as a scheme. As the notation suggests, this is the projective analogue of the affine correspondence $\mathfrak{a}\mapsto \Spec(B/\mathfrak{a})$.

::: Example 2
For the ideal $(f)$ generated by a nonzero homogeneous polynomial $f$ of positive degree, we call $V_+(f)=\Proj\bigl(\mathbb{K}[\x_0,\ldots,\x_n]/(f)\bigr)$ a *hypersurface* of degree $\deg f$. If $f=0$ then $V_+(0)=\mathbb{P}^n$, and if $f$ is a nonzero constant then $V_+(f)=\emptyset$, so this condition is necessary. For example, in $\mathbb{P}^2$, $V_+(\x_0\x_2-\x_1^2)$ is a conic.

On the other hand, comparing the two closed subschemes $V_+(\x_0)$ and $V_+(\x_0^2)$ in $\mathbb{P}^2$, their underlying spaces are the same, namely $Z_+(\x_0)=Z_+(\x_0^2)$, but their scheme structures differ. Indeed, on the chart $D_+(\x_2)\cong\Spec\mathbb{K}[\x_0/\x_2,\x_1/\x_2]$, the former is given by the ideal $(\x_0/\x_2)$ and the latter by $(\x_0^2/\x_2^2)$, and the coordinate ring of the latter has nilpotent elements. This is the same kind of non-reduced thickening as the double point examined in [[Closed Subschemes] §..., ⁋Example 1](/en/math/scheme_theory/closed_subschemes#ex1). However, since this thickening is supported not on a point but on the line $V_+(\x_0)\cong \mathbb{P}^1$, it is not a double point but a double line.
:::

## Homogeneous ideal of a closed subscheme

We now show conversely that any closed subscheme of $\mathbb{P}^n$ is of the form $V_+(\mathfrak{a})$.

::: Theorem 3
For any closed subscheme $Z$ of $\mathbb{P}^n$, there exists a homogeneous ideal $\mathfrak{a}\subseteq A_\bullet$ such that $Z=V_+(\mathfrak{a})$.
:::
::: Proof
For each $i$, $Z\cap D_+(\x_i)$ is a closed subscheme of the affine scheme $D_+(\x_i)\cong\Spec A_{(\x_i)}$, so by the discussion after [[Closed Subschemes] §..., ⁋Proposition 3](/en/math/scheme_theory/closed_subschemes#prop3) it corresponds to a unique ideal $\mathfrak{b}_i\subseteq A_{(\x_i)}$. Consider the set of homogeneous elements

$$T=\left\{f\in A_\bullet\middle\vert\text{$f$ homogeneous,}\quad \frac{f}{\x_i^{\deg f}}\in \mathfrak{b}_i\text{ for all }i\right\}$$

and let $\mathfrak{a}$ be the ideal generated by $T$. Since $T$ consists of homogeneous elements, $\mathfrak{a}$ is a homogeneous ideal. Our claim is that $\mathfrak{a}_{(\x_i)}=\mathfrak{b}_i$ for all $i$.

First, $\mathfrak{a}_{(\x_i)}$ is the ideal of $A_{(\x_i)}$ generated by elements of the form $f/\x_i^{\deg f}$ for $f\in T$, and by the definition of $T$ all these generators lie in $\mathfrak{b}_i$, so $\mathfrak{a}_{(\x_i)}\subseteq \mathfrak{b}_i$.

Conversely, let $g=f/\x_i^d\in \mathfrak{b}_i$ be given, where $f$ is a homogeneous polynomial of degree $d$. If we show that $\x_i^Nf\in T$ for sufficiently large $N$, then $g=(\x_i^Nf)/\x_i^{N+d}\in\mathfrak{a}_{(\x_i)}$ and the proof is complete. To this end, for each $j$ we find an $N$ such that $(\x_i^Nf)/\x_j^{N+d}\in \mathfrak{b}_j$. The case $j=i$ holds for any $N$, so let $j\neq i$.

The key point is that $\mathfrak{b}_i$ and $\mathfrak{b}_j$ are compatible on the intersection $D_+(\x_i\x_j)$. Considering the ideal sheaf $\mathcal{I}_{Z/\mathbb{P}^n}=\ker\iota^\sharp$ of $Z$ ([[Closed Subschemes] §..., ⁋Definition 5](/en/math/scheme_theory/closed_subschemes#def5)), the kernel is computed on sections, so $\mathcal{I}_{Z/\mathbb{P}^n}(D_+(\x_i))=\mathfrak{b}_i$. On the other hand, by [[Projective Spaces and the Proj Construction] §..., ⁋Lemma 9](/en/math/scheme_theory/projective_schemes#lem9), $D_+(\x_i\x_j)$ is the principal open subset $D(\x_j/\x_i)$ of $\Spec A_{(\x_i)}$, and since the sections of the structure sheaf and $\iota_\ast\mathcal{O}_Z$ on an affine scheme are given by localization, exactness of localization yields

$$\mathcal{I}_{Z/\mathbb{P}^n}(D_+(\x_i\x_j))=(\mathfrak{b}_i)_{\x_j/\x_i}=(\mathfrak{b}_j)_{\x_i/\x_j}.$$

Here both sides are ideals of $A_{(\x_i\x_j)}$.

Now the image of $g\in \mathfrak{b}_i$ in $A_{(\x_i\x_j)}$ lies in $(\mathfrak{b}_j)_{\x_i/\x_j}$. On the other hand, for $h=f/\x_j^d\in A_{(\x_j)}$, we have $h=(\x_i/\x_j)^d g$ in $A_{(\x_i\x_j)}$, so the image of $h$ also lies in $(\mathfrak{b}_j)_{\x_i/\x_j}$. Hence there exists $m_j\geq 0$ such that

$$\left(\frac{\x_i}{\x_j}\right)^{m_j}h=\frac{\x_i^{m_j}f}{\x_j^{m_j+d}}\in \mathfrak{b}_j.$$

Then taking $N=\max_{j\neq i}m_j$, since $\mathfrak{b}_j$ is an ideal we have $(\x_i^Nf)/\x_j^{N+d}=(\x_i/\x_j)^{N-m_j}\cdot(\x_i^{m_j}f)/\x_j^{m_j+d}\in \mathfrak{b}_j$ for all $j$, and thus $\x_i^Nf\in T$.

In summary, $Z$ and $V_+(\mathfrak{a})$ have the same ideal sheaf as closed subschemes of $\mathbb{P}^n$, so applying [[Closed Subschemes] §..., ⁋Lemma 9](/en/math/scheme_theory/closed_subschemes#lem9) in both directions gives $Z=V_+(\mathfrak{a})$.
:::

Unlike the affine case, this correspondence is not one-to-one. For example, for any homogeneous ideal $\mathfrak{a}$ and any $N\geq 1$, $\mathfrak{a}$ and $\mathfrak{a}A_+^N$ always define the same closed subscheme. Indeed, $V_+(\mathfrak{a})$ is determined on each chart $D_+(\x_i)$ by the ideal $\mathfrak{a}_{(\x_i)}$ computed in the proof of [Proposition 1](#prop1), and

$$\mathfrak{a}A_+^N\subseteq \mathfrak{a}$$

is obvious, so $(\mathfrak{a}A_+^N)_{(\x_i)}\subseteq \mathfrak{a}_{(\x_i)}$. Conversely, an element of $\mathfrak{a}_{(\x_i)}$ is of the form $f/\x_i^d$ for a homogeneous element $f\in \mathfrak{a}$ of degree $d$, and writing this as $\x_i^Nf/\x_i^{N+d}$ shows that this element belongs to $(\mathfrak{a}A_+^N)_{(\x_i)}$. Thus $\mathfrak{a}_{(\x_i)}=(\mathfrak{a}A_+^N)_{(\x_i)}$ for all $i$, from which we see that the above correspondence is not one-to-one.

## Saturation

The issue revealed in the above computation is that when computing the ideal on a chart, powers of $\x_i$ are absorbed into the denominator, so elements that enter $\mathfrak{a}$ after multiplying by a sufficiently high power of $\x_i$ carry the same information as elements of $\mathfrak{a}$ itself. In other words, the data that each element of $\mathfrak{a}$ gives on a chart is already known from the higher-degree element obtained by multiplying that element by a power of $\x_i$, so in fact if two homogeneous ideals agree in sufficiently large degree, they define the same closed subscheme.

Read in the reverse direction, even if a homogeneous element $f$ of degree $d$ does not belong to $\mathfrak{a}$, as long as $\x_i^Nf\in \mathfrak{a}$ for some $N$, we have $f/\x_i^d=\x_i^Nf/\x_i^{N+d}$ already belonging to $\mathfrak{a}_{(\x_i)}$. Such an $f$ is information already contained by $\mathfrak{a}$ on the chart, so even if we enlarge the ideal by collecting all such $f$ for every $i$, each $\mathfrak{a}_{(\x_i)}$ remains unchanged and hence the closed subscheme remains unchanged as well.

::: Definition 4
For a homogeneous ideal $\mathfrak{a}\subseteq A_\bullet$, the set of $f\in A_\bullet$ such that for each $i$ there exists $N\geq 0$ with $\x_i^Nf\in \mathfrak{a}$ is called the *saturation* of $\mathfrak{a}$ and is denoted $\mathfrak{a}^\sat$. A homogeneous ideal with $\mathfrak{a}=\mathfrak{a}^\sat$ is called *saturated*.
:::

By definition, it is obvious that $\mathfrak{a}^\sat$ is an ideal containing $\mathfrak{a}$. Also, since $\mathfrak{a}$ is homogeneous, $\x_i^Nf\in \mathfrak{a}$ holds for each homogeneous component of $f$, and therefore $\mathfrak{a}^\sat$ is also a homogeneous ideal.

::: Proposition 5
For homogeneous ideals $\mathfrak{a},\mathfrak{b}\subseteq A_\bullet$, the following hold.

1. $V_+(\mathfrak{a})=V_+(\mathfrak{a}^\sat)$.
2. $V_+(\mathfrak{a})=V_+(\mathfrak{b})$ if and only if $\mathfrak{a}^\sat=\mathfrak{b}^\sat$.

In particular, closed subschemes of $\mathbb{P}^n$ are in one-to-one correspondence with saturated homogeneous ideals.
:::
::: Proof
As we saw in the proof of [Proposition 1](#prop1), $V_+(\mathfrak{a})\cap D_+(\x_i)$ is determined by the ideal $\mathfrak{a}_{(\x_i)}\subseteq A_{(\x_i)}$, and since closed subschemes of an affine scheme correspond one-to-one with ideals (see the discussion after [[Closed Subschemes] §..., ⁋Proposition 3](/en/math/scheme_theory/closed_subschemes#prop3)), $V_+(\mathfrak{a})=V_+(\mathfrak{b})$ is equivalent to $\mathfrak{a}_{(\x_i)}=\mathfrak{b}_{(\x_i)}$ for all $i$.

1. Since $\mathfrak{a}\subseteq \mathfrak{a}^\sat$, we have $\mathfrak{a}_{(\x_i)}\subseteq (\mathfrak{a}^\sat)_{(\x_i)}$. Conversely, if $f\in \mathfrak{a}^\sat$ is a homogeneous element of degree $d$ and $\x_i^Nf\in \mathfrak{a}$, then

    $$\frac{f}{\x_i^d}=\frac{\x_i^Nf}{\x_i^{N+d}}\in \mathfrak{a}_{(\x_i)}$$

    so the reverse inclusion also holds.
2. One direction follows from (1). Conversely, suppose $V_+(\mathfrak{a})=V_+(\mathfrak{b})$ and let $f\in \mathfrak{a}^\sat$ be a homogeneous element of degree $d$. By the computation in (1), $f/\x_i^d\in \mathfrak{a}_{(\x_i)}=\mathfrak{b}_{(\x_i)}$, so there exists a homogeneous element $g\in \mathfrak{b}$ of degree $e$ such that $f/\x_i^d=g/\x_i^e$ in $A_{(\x_i)}$. Since $A_\bullet$ is an integral domain, $A_\bullet \rightarrow A_{\x_i}$ is injective, so this means $\x_i^ef=\x_i^dg\in \mathfrak{b}$. Since $i$ was arbitrary, $f\in \mathfrak{b}^\sat$, and checking homogeneous components yields $\mathfrak{a}^\sat\subseteq \mathfrak{b}^\sat$. Exchanging the roles of $\mathfrak{a}$ and $\mathfrak{b}$ gives the reverse inclusion.

The final claim follows because by [Theorem 3](#thm3) and (1), any closed subscheme arises from a saturated ideal, and (2) gives the uniqueness of such an ideal.
:::

The second result of [Proposition 5](#prop5) tells us that $\mathfrak{a}^\sat$ is the largest homogeneous ideal defining $V_+(\mathfrak{a})$. Indeed, if $V_+(\mathfrak{b})=V_+(\mathfrak{a})$, then $\mathfrak{b}\subseteq \mathfrak{b}^\sat=\mathfrak{a}^\sat$. That is, saturation is the operation of choosing a canonical representative among the ideals defining the same closed subscheme, and since $N$ in $\x_i^Nf\in \mathfrak{a}$ can be made arbitrarily large, this representative is determined by the sufficiently large degree part of $\mathfrak{a}$ alone. Thus, as mentioned at the beginning of this section, if two homogeneous ideals agree in sufficiently large degree, their saturations are equal, and hence they define the same closed subscheme. On the other hand, from this perspective, the ideal constructed in the proof of [Theorem 3](#thm3) is already saturated, because the set $T$ in that proof was the set of homogeneous elements $f$ such that $f/\x_i^{\deg f}\in \mathfrak{b}_i$ for all $i$, and the above computation shows that these are exactly the homogeneous elements of $\mathfrak{a}^\sat$.

::: Example 6
Consider $\mathfrak{a}=(\x_0^2,\x_0\x_1)$ in $\mathbb{P}^1$. On $D_+(\x_1)$, the ideal $\mathfrak{a}_{(\x_1)}$ is generated by $\x_0^2/\x_1^2$ and $\x_0\x_1/\x_1^2=\x_0/\x_1$, so it is $(\x_0/\x_1)$, while on $D_+(\x_0)$ it contains $\x_0^2/\x_0^2=1$ and hence is all of $A_{(\x_0)}$. Therefore $V_+(\mathfrak{a})$ is the reduced closed subscheme consisting of the single point $[0:1]$, namely $V_+(\x_0)$.

Reading this via saturation, since $\x_0^N\cdot \x_0\in (\x_0^2)$ and $\x_1^N\cdot \x_0\in (\x_0\x_1)$, we have $\x_0\in \mathfrak{a}^\sat$. Conversely, if $f\in \mathfrak{a}^\sat$, then $\x_1^Nf\in \mathfrak{a}\subseteq (\x_0)$, and since $(\x_0)$ is a prime ideal and $\x_1\notin (\x_0)$, we have $f\in (\x_0)$. Thus $\mathfrak{a}^\sat=(\x_0)$, and $\mathfrak{a}$ defines this point but is not saturated.

In the language of cones, what $\mathfrak{a}$ cuts out in $\mathbb{A}^2$ is the line $\x_0=0$ with an embedded point at the origin ([[Algebra of Schemes] §..., ⁋Example 11](/en/math/scheme_theory/algebra_of_schemes#ex11)), and saturation erases this component leaving only the line. The origin does not appear in any chart of $\mathbb{P}^1$, so this difference is invisible in $V_+(\mathfrak{a})$.
:::

## Projective scheme

In [[Algebraic Varieties] §Projective Varieties, ⁋Definition 3](/en/math/algebraic_varieties/projective_varieties#def3), we called the closed subsets of $\mathbb{P}^n$ cut out by homogeneous polynomials projective algebraic sets, and the irreducible ones among them projective varieties. The results of this post allow us to lift this definition to the language of schemes.

::: Definition 7
A scheme $X$ over a field $\mathbb{K}$ is called a *projective scheme* if there exist $n\geq 0$ and a closed embedding $X \rightarrow \mathbb{P}^n_\mathbb{K}$. ([[Closed Subschemes] §..., ⁋Definition 2](/en/math/scheme_theory/closed_subschemes#def2))
:::

By [Theorem 3](#thm3) and [Proposition 5](#prop5), up to isomorphism, projective schemes over $\mathbb{K}$ are exactly the $\Proj\bigl(\mathbb{K}[\x_0,\ldots,\x_n]/\mathfrak{a}\bigr)$ for saturated homogeneous ideals $\mathfrak{a}\subseteq \mathbb{K}[\x_0,\ldots,\x_n]$. Conversely, a projective scheme is the $\Proj$ of a finitely generated graded $\mathbb{K}$-algebra generated by elements of degree $1$. Indeed, choosing $n+1$ generators of the degree $1$ part of such an algebra $B_\bullet$ yields a surjection $\mathbb{K}[\x_0,\ldots,\x_n] \rightarrow B_\bullet$, and [Proposition 1](#prop1) carries this to a closed embedding $\Proj B_\bullet \rightarrow \mathbb{P}^n_\mathbb{K}$. On the other hand, [Definition 7](#def7) removes irreducibility from the classical definition, and when $\mathbb{K}$ is algebraically closed, the projective varieties correspond to integral projective schemes. ([[Algebra of Schemes] §..., ⁋Definition 1](/en/math/scheme_theory/algebra_of_schemes#def1))

---

**References**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).

---
