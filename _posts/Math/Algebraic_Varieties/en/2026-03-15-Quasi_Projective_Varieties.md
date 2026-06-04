---
title: "Quasi-Projective Varieties"
description: "We introduce the notion of quasi-projective varieties defined as open subsets of projective varieties, and show that both affine and projective varieties are quasi-projective. We also examine morphisms between quasi-projective varieties and properties of the Zariski topology."
excerpt: "Quasi-projective varieties and regular maps"

categories: [Math / Algebraic Varieties]
permalink: /en/math/algebraic_varieties/quasi_projective_varieties
sidebar: 
    nav: "algebraic_varieties-en"

date: 2026-03-15
last_modified_at: 2026-03-17
weight: 3
translated_at: 2026-05-30T02:30:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-30T02:30:04+00:00
---
In [§Affine Varieties](/en/math/algebraic_varieties/affine_varieties) and [§Projective Varieties](/en/math/algebraic_varieties/projective_varieties) we examined geometric objects defined as subsets of affine space and projective space, respectively. However, the most natural objects in algebraic geometry belong to a larger category encompassing both. In this section we define *quasi-projective varieties* and show that they include both affine and projective varieties. We also define morphisms between quasi-projective varieties and verify that they agree with the existing notions.

## Definition of a Quasi-Projective Variety

Open subsets of projective space are natural geometric objects. For example, the standard affine cover $$U_0$$ obtained by removing the line $$x_0=0$$ from $$\mathbb{P}^2$$ is not a projective variety, yet it is still an object defined by polynomials—in fact, it is an affine variety.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> An open subset $$X \subseteq Y$$ of a projective variety $$Y \subseteq \mathbb{P}^n$$ is called a *quasi-projective variety*.

</div>

Of course $$X$$ inherits the topology of $$Y$$, and this topology is again called the *Zariski topology*. By definition it is obvious that quasi-projective varieties include all projective varieties. Our first proposition is that every affine variety is quasi-projective.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> Every affine variety is a quasi-projective variety.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let an arbitrary affine variety $$X\subseteq \mathbb{A}^n$$ be given. We already know that the embedding

$$i:\mathbb{A}^n\rightarrow \mathbb{P}^n;\qquad (x_1,\ldots, x_n)\mapsto [1:x_1:\cdots:x_n]$$

exists. ([§Projective Varieties, ⁋Proposition 9](/en/math/algebraic_varieties/projective_varieties#prop9)) Now consider the image $$i(X)$$ of $$X$$ in $$\mathbb{P}^n$$, and the closure $$\overline{i(X)}$$ of $$i(X)$$ in $$\mathbb{P}^n$$. Then $$\overline{i(X)}$$ is a projective variety, and inside it $$X$$ appears as

$$X=\overline{i(X)}\cap U_0$$

and is therefore an open subset. This completes the proof.

</details>

Unraveling the proof above, one easily sees that the Zariski topology defined on a quasi-projective variety agrees with the Zariski topology previously defined on an affine variety, and the same holds for projective varieties.

In general, for both the affine and projective cases, open subsets of a given variety were more often than not not themselves affine or projective varieties. Quasi-projective varieties form a much broader category, and the following holds.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> An open subset of a quasi-projective variety $$X$$ is a quasi-projective variety. Moreover, an irreducible closed subset of $$X$$ is also a quasi-projective variety.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Suppose $$X$$ is an open subset of a projective variety $$Y\subset \mathbb{P}^n$$. Since an open subset of $$X$$ is also an open subset of $$Y$$, it is obvious that any open subset of $$X$$ is a quasi-projective variety. Hence it suffices to show that any irreducible closed subset of $$X$$ is quasi-projective. For this, write

$$X=Y\cap U,\qquad \text{$U$ open in $\mathbb{P}^n$}$$

and let an arbitrary irreducible closed subset $$Z$$ of $$X$$ be given. Then there exists a suitable irreducible closed subset $$W$$ of $$\mathbb{P}^n$$ such that

$$Z=X\cap W=(Y\cap U)\cap W=(Y\cap W)\cap U.$$

Thus $$Z$$ is an open subset of the projective variety $$Y\cap W$$.

</details>

## Regular Functions and Regular Maps

From now on, unless stated otherwise, by a variety we shall always mean a quasi-projective variety. Our geometric intuition is that every point of a variety $$X$$ possesses an affine open neighborhood. This has already been proved for the affine and projective cases separately, so we need only extend it to the quasi-projective case.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> For any variety $$X$$ and any point $$x\in X$$, there exists a covering of $$X$$ by affine varieties.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, since $$X$$ is quasi-projective, there exists a suitable projective variety $$Y\subset \mathbb{P}^n$$ such that $$X$$ is an open subset of $$Y$$. Now $$X$$ can be covered by the sets $$X\cap U_i$$ using the standard affine charts, and each $$X\cap U_i$$ is an open subset of the affine variety $$Y\cap U_i$$. ([§Projective Varieties, ⁋Proposition 10](/en/math/algebraic_varieties/projective_varieties#prop10)) By [§Affine Varieties, ⁋Proposition 6](/en/math/algebraic_varieties/affine_varieties#prop6), any open subset of an affine variety can be covered by principal open sets, and these are affine by [§Affine Varieties, ⁋Proposition 7](/en/math/algebraic_varieties/affine_varieties#prop7), which completes the proof.

</details>

Now, by the proposition above, we can make the following definition.

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> A function $$f: X \rightarrow \mathbb{K}$$ on a quasi-projective variety $$X$$ is called *regular* if there exists an open affine cover $$\{U_i\}$$ of $$X$$ such that for each $$i$$ the restriction

$$f\vert_{U_i}:U_i\rightarrow\mathbb{K}$$

is an element of the coordinate ring $$\mathbb{K}[U_i]$$ of the affine variety $$U_i$$. The sheaf of all regular functions on $$X$$ is denoted by $$\mathcal{O}_X$$, or more simply by $$\mathcal{O}$$. ([\[Topology\] §Sheaves, ⁋Definition 1](/en/math/topology/sheaves#def1))

</div>

The following are examples of regular functions.

<div class="example" markdown="1">

<ins id="ex6">**Example 6**</ins> Let us examine some examples of regular functions.

1. For an affine variety $$X$$, we have $$\mathcal{O}(X) = \mathbb{K}[X]$$.
2. For $$\mathbb{P}^n$$, we have $$\mathcal{O}(\mathbb{P}^n) = \mathbb{K}$$. To verify this, consider the standard open cover $$U_i = \{x_i \ne 0\}$$. In particular, a regular function on $$U_0$$ is an element of $$\mathbb{K}[x_1/x_0, \ldots, x_n/x_0]$$, and a regular function on $$U_1$$ is an element of $$\mathbb{K}[x_0/x_1, x_2/x_1, \ldots, x_n/x_1]$$. Hence if a function $$f$$ is regular on all of $$\mathbb{P}^n$$, then on $$U_0$$ it is a polynomial in the variables $$\mathrm{s}_i=x_i/x_0$$, and on $$U_1$$ it is a polynomial in $$\mathrm{t}_i=x_i/x_1$$. But on $$U_0\cap U_1$$ we know these coordinate functions satisfy
    
    $$\mathrm{t}_0=\frac{1}{\mathrm{s}_1},\qquad \mathrm{t}_j=\frac{\mathrm{s}_j}{\mathrm{s}_1}.$$

    Therefore, if

    $$f\vert_{U_0}=p(\mathrm{s}_1, \ldots, \mathrm{s}_n),\qquad f\vert_{U_1}=q(\mathrm{t}_0,\mathrm{t}_2,\ldots, \mathrm{t}_n)$$

    then the requirement that these define the same function on $$U_0\cap U_1$$ together with the above formulas implies

    $$p(\mathrm{s}_1,\ldots, \mathrm{s}_n)=q\left(\frac{1}{\mathrm{s}_1},\frac{\mathrm{s}_2}{\mathrm{s}_1}, \ldots,\frac{\mathrm{s}_n}{\mathrm{s}_1}\right).$$

    For the right-hand side to be a polynomial, $$q$$ must be a constant function so that the denominators involving $$\mathrm{s}_1$$ disappear, and from this we see that $$p$$ and $$q$$ must both be constant. Applying the same argument to all charts $$U_i, U_j$$ yields the desired result.

</div>

Now we define morphisms between varieties, that is, regular maps. There are several ways to do this, but we shall always assume that a variety is embedded in some projective space, and since morphisms between projective spaces have already been defined, we use this to give the following definition. ([§Projective Varieties, ⁋Definition 15](/en/math/algebraic_varieties/projective_varieties#def15))

<div class="definition" markdown="1">

<ins id="def7">**Definition 7**</ins> A map $$\varphi:X \rightarrow Y$$ between two varieties $$X \subseteq \mathbb{P}^n$$ and $$Y \subseteq \mathbb{P}^m$$ is called a *morphism* (or *regular map*) if for every $$x\in X$$ there exists a suitable open neighborhood $$U \subseteq X$$ of $$x$$ and homogeneous polynomials $$F_0, \ldots, F_m$$ of the same degree such that

$$\varphi(q) = [F_0(q) : \cdots : F_m(q)]$$

holds for all $$q \in U$$.

</div>

So far, when we spoke of a variety we assumed an embedding into affine space or projective space, and the above definition lies on the same line of assumption. Through this we can perform concrete calculations, but one could hardly call this definition intrinsic. The following proposition shows that this definition admits a natural interpretation from the viewpoint of regular functions.

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8**</ins> A map $$\varphi: X \to Y$$ is a morphism if and only if for every affine open set $$V$$ of $$Y$$ and every regular function $$f \in \mathcal{O}_Y(V)$$, the composition $$f \circ \varphi: \varphi^{-1}(V) \to \mathbb{K}$$ is a regular function.

</div>

The heart of the proof is that a morphism is expressed locally by homogeneous polynomials, and a regular function on $$Y$$ can be written in the form $$F/G$$ for homogeneous polynomials $$F, G$$ of the same degree (thinking of the dehomogenization process), so their composition must also be a regular function. Using this, one can show the following.

<div class="proposition" markdown="1">

<ins id="prop9">**Proposition 9**</ins> Regular maps between affine varieties are exactly the regular maps obtained by viewing them as quasi-projective varieties.

</div>

This is essentially [§Affine Varieties, ⁋Definition 15](/en/math/algebraic_varieties/affine_varieties#def15).

## Properties of Regular Maps

<div class="proposition" markdown="1">

<ins id="prop10">**Proposition 10**</ins> A regular map $$\varphi: X \to Y$$ is continuous.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

If $$Z \subseteq Y$$ is closed, then on some open cover $$\{V_\alpha\}$$ of $$Y$$ there exist for each $$V_\alpha$$ regular functions $$f_{\alpha,1}, \ldots, f_{\alpha,k_\alpha}$$ such that

$$Z \cap V_\alpha = \{y \in V_\alpha \mid f_{\alpha,1}(y) = \cdots = f_{\alpha,k_\alpha}(y) = 0\}.$$

Then

$$\varphi^{-1}(Z) \cap \varphi^{-1}(V_\alpha) = \{x \in \varphi^{-1}(V_\alpha) \mid f_{\alpha,1}(\varphi(x)) = \cdots = f_{\alpha,k_\alpha}(\varphi(x)) = 0\}.$$

Since $$\varphi$$ is a regular map, each $$f_{\alpha,i} \circ \varphi$$ is a regular function on $$\varphi^{-1}(V_\alpha)$$. Hence $$\varphi^{-1}(Z) \cap \varphi^{-1}(V_\alpha)$$ is closed in $$\varphi^{-1}(V_\alpha)$$, and since $$\{\varphi^{-1}(V_\alpha)\}$$ is an open cover of $$X$$, it follows that $$\varphi^{-1}(Z)$$ is closed in $$X$$.

</details>

<div class="proposition" markdown="1">

<ins id="prop11">**Proposition 11**</ins> The composition of regular maps is a regular map. The identity map is a regular map.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$\varphi: X \to Y$$ and $$\psi: Y \to Z$$ be regular maps. If $$W \subseteq Z$$ is open and $$f \in \mathcal{O}(W)$$, then since $$\psi$$ is regular we have $$f \circ \psi \in \mathcal{O}(\psi^{-1}(W))$$. Now since $$\varphi$$ is regular, $$(f \circ \psi) \circ \varphi \in \mathcal{O}(\varphi^{-1}(\psi^{-1}(W)))$$. That is,

$$f \circ (\psi \circ \varphi) \in \mathcal{O}((\psi \circ \varphi)^{-1}(W))$$

so $$\psi \circ \varphi$$ is a regular map.

For the identity map $$\id_X: X \to X$$, we have $$f \circ \id_X = f$$, so it is trivially a regular map.

</details>

Thus quasi-projective varieties and regular maps form a category.

<div class="proposition" markdown="1">

<ins id="prop12">**Proposition 12**</ins> The restriction of a regular map to a closed subset is a regular map. The restriction of a regular map to an open subset is also a regular map.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$\varphi: X \to Y$$ be a regular map and let $$Z \subseteq Y$$ be closed. Consider $$\psi = \varphi\vert_{\varphi^{-1}(Z)}: \varphi^{-1}(Z) \to Z$$. If $$f$$ is a regular function on an open set $$V$$ of $$Z$$, then $$f$$ extends to a regular function on some open set $$V' \supseteq V$$ of $$Y$$ (at least locally). Concretely, by intersecting $$V$$ with an open affine cover of $$Z$$ and defining regular functions on each piece, one can glue them regularly to obtain a regular function on an open neighborhood $$V'$$ of $$Y$$. This works because regular functions are essentially local expressions of rational functions, so their definitions on affine charts are consistent and patch together on intersections of Zariski open covers. Then $$f \circ \psi = (f \circ \varphi)\vert_{\varphi^{-1}(Z)}$$, and since $$f \circ \varphi$$ is regular on $$\varphi^{-1}(V')$$, its restriction is also regular.

The case of an open subset is simpler. If $$U \subseteq Y$$ is open and $$f$$ is regular on $$V \subseteq U$$, then $$f \circ \varphi$$ is regular on $$\varphi^{-1}(V)$$.

</details>

<div class="definition" markdown="1">

<ins id="def13">**Definition 13**</ins> A morphism $$\varphi: X \to Y$$ is called an *isomorphism* if there exists an inverse map $$\psi: Y \to X$$ that is also a morphism.

</div>

The notion of isomorphism means geometrically that two varieties are the same. That is, isomorphic varieties cannot be distinguished from the point of view of regular functions.

<div class="example" markdown="1">

<ins id="ex14">**Example 14**</ins> Since we have already examined morphisms between projective varieties and morphisms between affine varieties separately, the functions that tie projective and affine varieties together are the new ones. For example, the canonical surjection

$$\mathbb{A}^{n+1}\setminus\{(0,\ldots, 0)\}\rightarrow \mathbb{P}^n;\qquad (x_0,\ldots, x_n)\mapsto [x_0:\cdots:x_n]$$

is a morphism between quasi-projective varieties. Also, the canonical inclusion

$$\iota_i:\mathbb{A}^n\hookrightarrow \mathbb{P}^n$$

is a morphism between quasi-projective varieties.

</div>

---

**References**

**[Har]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.
