---
title: "Quasi-Projective Varieties"
description: "We introduce quasi-projective varieties, defined as open subsets of projective varieties, and show that every affine and projective variety is quasi-projective. We also examine morphisms between quasi-projective varieties and properties of the Zariski topology."
excerpt: "Quasi-projective varieties and regular maps"

categories: [Math / Algebraic Varieties]
permalink: /en/math/algebraic_varieties/quasi_projective_varieties
sidebar: 
    nav: "algebraic_varieties-en"

date: 2026-03-15
weight: 3
translated_at: 2026-08-17T08:18:27+00:00
translation_source: kimi-cli
---
In [§Affine Varieties](/en/math/algebraic_varieties/affine_varieties) and [§Projective Varieties](/en/math/algebraic_varieties/projective_varieties), we examined geometric objects defined as subsets of affine space and projective space, respectively. However, the most natural objects in algebraic geometry belong to a larger category encompassing both. In this section, we define *quasi-projective varieties* and show that they include both affine and projective varieties. We also define morphisms between quasi-projective varieties and verify that they are compatible with the existing notions.

## Definition of Quasi-projective Variety

Open subsets of projective space are natural geometric objects. For instance, the standard open set $U_0$ obtained by removing the line $\x_0=0$ from $\mathbb{P}^2$ is not a projective variety, but it is still an object defined by polynomials, and in fact it is an affine variety.

::: Definition 1
An open subset $X \subseteq Y$ of a projective variety $Y \subseteq \mathbb{P}^n$ is called a *quasi-projective variety*.
:::

Of course, $X$ inherits the topology of $Y$, and this topology is also called the *Zariski topology*. By definition, it is obvious that quasi-projective varieties encompass all projective varieties. Our first proposition is that any affine variety is quasi-projective.

::: Proposition 2
Any affine variety is a quasi-projective variety.
:::
::: Proof
Let an arbitrary affine variety $X\subseteq \mathbb{A}^n$ be given. We already know that the following embedding exists:

$$i:\mathbb{A}^n\rightarrow \mathbb{P}^n;\qquad (x_1,\ldots, x_n)\mapsto [1:x_1:\cdots:x_n]$$

([§Projective Varieties, ⁋Proposition 9](/en/math/algebraic_varieties/projective_varieties#prop9)) Now consider the image $i(X)$ of $X$ in $\mathbb{P}^n$, and the closure $\overline{i(X)}$ of $i(X)$ in $\mathbb{P}^n$. Then $\overline{i(X)}$ is a projective variety, and within it, $i(X)$ is an open subset because

$$i(X)=\overline{i(X)}\cap U_0$$

This completes the proof.
:::

Unpacking the proof above, one easily sees that the Zariski topology defined on a quasi-projective variety coincides with the Zariski topology previously defined on an affine variety, and the same holds for projective varieties.

In general, for both the affine and projective cases, open subsets of a given variety more often failed to be affine or projective varieties themselves. Quasi-projective varieties form a much broader category than these, and the following holds.

::: Proposition 3
An open subset of a quasi-projective variety $X$ is a quasi-projective variety. Also, an irreducible closed subset of $X$ is a quasi-projective variety.
:::
::: Proof
Suppose $X$ is an open subset of a projective variety $Y\subseteq \mathbb{P}^n$. Since an open subset of $X$ is also an open subset of $Y$, it is obvious that any open subset of $X$ is a quasi-projective variety. Thus it suffices to show that any irreducible closed subset of $X$ is quasi-projective. To this end, write

$$X=Y\cap U,\qquad \text{$U$ open in $\mathbb{P}^n$}$$

and let an arbitrary irreducible closed subset $Z$ of $X$ be given. Now consider the closure $\overline{Z}$ of $Z$ in $\mathbb{P}^n$; since $Z$ is irreducible, $\overline{Z}$ is also an irreducible closed set. Moreover, since $Z\subseteq X\subseteq Y$ and $Y$ is closed in $\mathbb{P}^n$, we have $\overline{Z}\subseteq Y$, and therefore $\overline{Z}$ is itself a projective variety. On the other hand, since $Z$ is closed in $X$, we have $Z=X\cap C$ for some closed subset $C$ of $\mathbb{P}^n$, and then from $Z\subseteq X\cap \overline{Z}\subseteq X\cap C=Z$ we obtain

$$Z=X\cap \overline{Z}=(Y\cap U)\cap \overline{Z}=\overline{Z}\cap U$$

Thus $Z$ is an open subset of the projective variety $\overline{Z}$.
:::

## Regular Functions and Regular Maps

Henceforth, unless stated otherwise, a variety shall always mean a quasi-projective variety. Our geometric intuition is that any point of a variety $X$ always has an affine open neighborhood. This was already proved in the affine and projective cases respectively, so we need only extend it to the quasi-projective case.

::: Proposition 4
For any variety $X$ and any $x\in X$, there exists an open covering of $X$ by affine varieties.
:::
::: Proof
First, since $X$ is quasi-projective, there exists a suitable projective variety $Y\subseteq \mathbb{P}^n$ such that $X$ is an open subset of $Y$. Now $X$ can be covered by the $X\cap U_i$ using standard affine charts, and each $X\cap U_i$ is an open subset of the affine variety $Y\cap U_i$. ([§Projective Varieties, ⁋Proposition 10](/en/math/algebraic_varieties/projective_varieties#prop10)) Now by [§Affine Varieties, ⁋Proposition 6](/en/math/algebraic_varieties/affine_varieties#prop6), any open subset of an affine variety can be covered by principal open sets, and these are affine by [§Affine Varieties, ⁋Proposition 7](/en/math/algebraic_varieties/affine_varieties#prop7), which completes the proof.
:::

Now by the above proposition, we can define the following.

::: Definition 5
A function $f: X \rightarrow \mathbb{K}$ on a quasi-projective variety $X$ is called *regular* if there exists an open affine cover $\{U_i\}$ of $X$ such that for each $i$, the restriction

$$f\vert_{U_i}:U_i\rightarrow\mathbb{K}$$

is an element of the coordinate ring $\mathbb{K}[U_i]$ of the affine variety $U_i$. The sheaf of all regular functions on $X$ is denoted $\mathcal{O}_X$ or more simply $\mathcal{O}$. ([\[Topology\] §Sheaves, ⁋Definition 1](/en/math/topology/sheaves#def1))
:::

Here are some examples of regular functions.

::: Example 6
Let us examine some examples of regular functions.

1. For an affine variety $X$, we have $\mathcal{O}(X) = \mathbb{K}[X]$. In [Definition 5](#def5), we may choose $X$ itself as the open affine cover, so $\mathbb{K}[X]\subseteq \mathcal{O}(X)$, and the reverse inclusion follows from the fact that a function given locally by a rational expression is again an element of the coordinate ring, that is, the equivalence of [§Affine Varieties, ⁋Definition 11](/en/math/algebraic_varieties/affine_varieties#def11) and [§Affine Varieties, ⁋Definition 14](/en/math/algebraic_varieties/affine_varieties#def14).
2. On $\mathbb{P}^n$, we have $\mathcal{O}(\mathbb{P}^n) = \mathbb{K}$. To verify this, consider the standard open cover $U_i = \{x_i \ne 0\}$. In particular, a regular function on $U_0$ is an element of $\mathbb{K}[\x_1/\x_0, \ldots, \x_n/\x_0]$, and a regular function on $U_1$ is an element of $\mathbb{K}[\x_0/\x_1, \x_2/\x_1, \ldots, \x_n/\x_1]$. Thus if a function $f$ is regular on all of $\mathbb{P}^n$, then on $U_0$ it is a polynomial in $\mathrm{s}_i=\x_i/\x_0$, and on $U_1$ it is a polynomial in $\mathrm{t}_i=\x_i/\x_1$. However, on $U_0\cap U_1$, we know that these coordinate functions satisfy the relations
    
    $$\mathrm{t}_0=\frac{1}{\mathrm{s}_1},\qquad \mathrm{t}_j=\frac{\mathrm{s}_j}{\mathrm{s}_1}\quad (j=2,\ldots, n)$$

    Therefore, if

    $$f\vert_{U_0}=p(\mathrm{s}_1, \ldots, \mathrm{s}_n),\qquad f\vert_{U_1}=q(\mathrm{t}_0,\mathrm{t}_2,\ldots, \mathrm{t}_n)$$

    then the requirement that these define the same function on $U_0\cap U_1$ together with the above relations implies that

    $$p(\mathrm{s}_1,\ldots, \mathrm{s}_n)=q\left(\frac{1}{\mathrm{s}_1},\frac{\mathrm{s}_2}{\mathrm{s}_1}, \ldots,\frac{\mathrm{s}_n}{\mathrm{s}_1}\right)$$

    must hold. Now for the right-hand side to be a polynomial, $q$ must be a constant function so that the denominators involving $\mathrm{s}_1$ disappear, and from this we see that $p$ and $q$ must be constant functions. Applying the same argument to all charts $U_i, U_j$ yields the desired result.
:::

Now we define morphisms between varieties, that is, regular maps. There are several ways to do this, but we shall always assume that a variety is given as embedded in some projective space, and since morphisms between projective spaces have already been defined, we use this to define morphisms as follows. ([§Projective Varieties, ⁋Definition 15](/en/math/algebraic_varieties/projective_varieties#def15))

::: Definition 7
A function $\varphi:X \rightarrow Y$ between two varieties $X \subseteq \mathbb{P}^n$ and $Y \subseteq \mathbb{P}^m$ is called a *morphism* (or *regular map*) if for every $x\in X$ there exist a suitable open neighborhood $U \subseteq X$ of $x$ and homogeneous polynomials $F_0, \ldots, F_m$ of the same degree such that

$$\varphi(q) = [F_0(q) : \cdots : F_m(q)] \in \mathbb{P}^m$$

holds for all $q \in U$.
:::

So far, when discussing varieties we have assumed an embedding into affine space or projective space, and the above definition is also in line with this assumption. Through this we can perform concrete calculations, but this definition can hardly be called intrinsic. The following proposition shows that this definition admits a natural interpretation from the perspective of regular functions.

::: Proposition 8
A continuous map $\varphi: X \rightarrow Y$ is a morphism if and only if for every affine open set $V$ of $Y$ and every regular function $f \in \mathcal{O}_Y(V)$, the composition $f \circ \varphi: \varphi^{-1}(V) \rightarrow \mathbb{K}$ is a regular function.
:::

The heart of the proof is that a morphism is expressed locally by homogeneous polynomials, and regular functions on $Y$ can be written in the form $F/G$ for homogeneous polynomials $F, G$ of the same degree $d$ (considering the dehomogenization process), so their composition must also be a regular function. Using this, we can show the following.

::: Proposition 9
Regular maps between affine varieties are exactly the regular maps when these are viewed as quasi-projective varieties.
:::

This is essentially due to [§Affine Varieties, ⁋Definition 15](/en/math/algebraic_varieties/affine_varieties#def15).

## Properties of Regular Maps

::: Proposition 10
A regular map $\varphi: X \rightarrow Y$ is a continuous map.
:::

::: Proof
Let $C \subseteq Y$ be a closed set. Then there exist homogeneous polynomials $G_1, \ldots, G_r$ in $\mathbb{K}[\x_0, \ldots, \x_m]$ such that $C = Y \cap Z(G_1, \ldots, G_r)$, and since the image of $\varphi$ lies in $Y$, we have $\varphi^{-1}(C) = \varphi^{-1}(Z(G_1, \ldots, G_r))$.

Now for arbitrary $x \in X$, choose the open neighborhood $U \subseteq X$ and homogeneous polynomials $F_0, \ldots, F_m$ of the same degree given by [Definition 7](#def7). Since $\varphi = [F_0 : \cdots : F_m]$ on $U$, we have

$$\varphi^{-1}(C) \cap U = \{q \in U \mid G_1(F_0(q), \ldots, F_m(q)) = \cdots = G_r(F_0(q), \ldots, F_m(q)) = 0\}$$

and each $G_k(F_0, \ldots, F_m)$ is again a homogeneous polynomial in $\x_0, \ldots, \x_n$, so the right-hand side is the intersection of a closed subset of $\mathbb{P}^n$ with $U$. That is, $\varphi^{-1}(C) \cap U$ is closed in $U$, and since such $U$ cover $X$, we conclude that $\varphi^{-1}(C)$ is closed in $X$.
:::

::: Proposition 11
The composition of regular maps is a regular map. The identity map is a regular map.
:::

::: Proof
Let $\varphi: X \rightarrow Y$ and $\psi: Y \rightarrow Z$ be regular maps. If $W \subseteq Z$ is open and $f \in \mathcal{O}(W)$, then since $\psi$ is regular, we have $f \circ \psi \in \mathcal{O}(\psi^{-1}(W))$. Now since $\varphi$ is regular, $(f \circ \psi) \circ \varphi \in \mathcal{O}(\varphi^{-1}(\psi^{-1}(W)))$. That is,

$$f \circ (\psi \circ \varphi) \in \mathcal{O}((\psi \circ \varphi)^{-1}(W))$$

so $\psi \circ \varphi$ is a regular map.

For the identity map $\id_X: X \rightarrow X$, we have $f \circ \id_X = f$, so it is trivially a regular map.
:::

Thus quasi-projective varieties and regular maps form a category.

::: Proposition 12
The restriction of a regular map to a closed subset is a regular map. The restriction of a regular map to an open subset is also a regular map.
:::

::: Proof
Let $\varphi: X \rightarrow Y$ be a regular map and let $Z \subseteq Y$ be a closed subset. Considering $\psi = \varphi\vert_{\varphi^{-1}(Z)}: \varphi^{-1}(Z) \rightarrow Z$, by [Proposition 10](#prop10) $\varphi$ is continuous, so $\psi$ is also continuous. Now if $f$ is a regular function on an open subset $V$ of $Z$, then $f$ extends to a regular function on an open subset of $Y$ in a neighborhood of each point of $V$. Specifically, choosing an affine open set $W$ of $Y$ containing a point of $V$, we have that $W\cap Z$ is a closed subset of the affine variety $W$, so regular functions on it are restrictions of elements of $\mathbb{K}[W]$ ([Example 6](#ex6)), and $f$ is given locally as a quotient of such functions, so we simply lift numerator and denominator to $\mathbb{K}[W]$. Then $f \circ \psi = (f \circ \varphi)\vert_{\varphi^{-1}(Z)}$, and since regularity is determined locally, the regularity of $f \circ \varphi$ on these neighborhoods implies that $f\circ\psi$ is also regular.

The case of an open subset is simpler. If $U \subseteq Y$ is open, then whenever $f$ is regular on $V \subseteq U$, the composition $f \circ \varphi$ is regular on $\varphi^{-1}(V)$.
:::

::: Definition 13
A morphism $\varphi: X \rightarrow Y$ is called an *isomorphism* if there exists an inverse function $\psi: Y \rightarrow X$ such that $\psi$ is also a morphism.
:::

The notion of isomorphism means geometrically that two varieties are the same. That is, isomorphic varieties cannot be distinguished from the perspective of regular functions.

::: Example 14
We have already examined morphisms between projective varieties and morphisms between affine varieties separately, so functions linking projective and affine varieties are new ones. For instance, the canonical surjection

$$\mathbb{A}^{n+1}\setminus\{(0,\ldots, 0)\}\rightarrow \mathbb{P}^n;\qquad (x_0,\ldots, x_n)\mapsto [x_0:\cdots:x_n]$$

is a morphism between quasi-projective varieties. Also, the canonical inclusion

$$\iota_i:\mathbb{A}^n\hookrightarrow \mathbb{P}^n$$

is a morphism between quasi-projective varieties.
:::

---

**References**

**[Har]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.
