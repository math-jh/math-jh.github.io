---
title: "Quasi-projective Varieties"
excerpt: "Quasi-projective varieties and regular maps"

categories: [Math / Algebraic Varieties]
permalink: /en/math/algebraic_varieties/quasi_projective_varieties
sidebar: 
    nav: "algebraic_varieties-en"

header:
    overlay_image: /assets/images/Math/Algebraic_Varieties/Quasi_Projective_Varieties.png
    overlay_filter: 0.5

date: 2026-03-15
last_modified_at: 2026-03-17
weight: 3
translated_at: 2026-05-19T03:30:01+00:00
translation_source: kimi-cli
---
In [§Affine Varieties](/en/math/algebraic_varieties/affine_varieties) and [§Projective Varieties](/en/math/algebraic_varieties/projective_varieties), we examined geometric objects defined as subsets of affine space and projective space, respectively. However, the most natural objects in algebraic geometry belong to a larger category that encompasses both. In this section we define *quasi-projective varieties* and show that they include both affine and projective varieties. We also define morphisms between quasi-projective varieties and show that they agree with the existing notions.

## Definition of Quasi-projective Varieties

Open subsets of projective space are natural geometric objects. For example, the standard affine cover $$U_0$$ obtained by removing the line $$\x_0=0$$ from $$\mathbb{P}^2$$ is not a projective variety, but it is still an object defined by polynomials—in fact, it is an affine variety.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> An open subset $$X \subseteq Y$$ of a projective variety $$Y \subseteq \mathbb{P}^n$$ is called a *quasi-projective variety*.

</div>

Of course, $$X$$ inherits the topology of $$Y$$, and this topology is also called the *Zariski topology*. By definition, it is obvious that quasi-projective varieties include all projective varieties. Our first proposition is that any affine variety is quasi-projective.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> Any affine variety is a quasi-projective variety.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$X \subseteq \mathbb{A}^n$$ be an arbitrary affine variety. We already know that there exists an embedding

$$i:\mathbb{A}^n\rightarrow \mathbb{P}^n;\qquad (x_1,\ldots, x_n)\mapsto [1:x_1:\cdots:x_n]$$

([§Projective Varieties, ⁋Proposition 9](/en/math/algebraic_varieties/projective_varieties#prop9)). Now consider the image $$i(X)$$ in $$\mathbb{P}^n$$, and take its closure $$\overline{i(X)}$$ in $$\mathbb{P}^n$$. Then $$\overline{i(X)}$$ is a projective variety, and within it $$X$$ is represented as

$$X=\overline{i(X)}\cap U_0$$

an open set. This completes the proof.

</details>

Examining the proof above, one easily sees that the Zariski topology defined on a quasi-projective variety agrees with the Zariski topology previously defined on an affine variety, and similarly for projective varieties.

In general, for both the affine and projective cases, open subsets of a given variety are more often not themselves affine or projective varieties. Quasi-projective varieties form a much broader category than these, and the following holds.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> An open subset of a quasi-projective variety $$X$$ is a quasi-projective variety. Also, an irreducible closed subset of $$X$$ is a quasi-projective variety.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Suppose $$X$$ is an open subset of a projective variety $$Y \subset \mathbb{P}^n$$. Since an open subset of $$X$$ is also an open subset of $$Y$$, it is obvious that any open subset of $$X$$ is a quasi-projective variety. Thus it suffices to show that any irreducible closed set in $$X$$ is quasi-projective. For this, write

$$X=Y\cap U,\qquad \text{$U$ open in $\mathbb{P}^n$}$$

and let $$Z$$ be an arbitrary irreducible closed set in $$X$$. Then there exists a suitable irreducible closed subset $$W$$ of $$\mathbb{P}^n$$ such that

$$Z=X\cap W=(Y\cap U)\cap W=(Y\cap W)\cap U$$

Hence $$Z$$ is an open subset of the projective variety $$Y \cap W$$.

</details>

## Regular Functions and Regular Maps

From now on, unless otherwise mentioned, a variety will always mean a quasi-projective variety. Our geometric intuition is that every point of a variety $$X$$ has an affine open neighborhood. We have already proved this for the affine and projective cases respectively, so we only need to extend it to the quasi-projective case.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> For any variety $$X$$ and any point $$x \in X$$, there exists a cover of $$X$$ by affine varieties.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, since $$X$$ is quasi-projective, there exists a suitable projective variety $$Y \subset \mathbb{P}^n$$ such that $$X$$ is an open subset of $$Y$$. Now $$X$$ can be covered by the sets $$X \cap U_i$$ using the standard affine charts, and each $$X \cap U_i$$ is an open subset of the affine variety $$Y \cap U_i$$. ([§Projective Varieties, ⁋Proposition 10](/en/math/algebraic_varieties/projective_varieties#prop10)) By [§Affine Varieties, ⁋Proposition 6](/en/math/algebraic_varieties/affine_varieties#prop6), any open subset of an affine variety can be covered by principal open sets, and these are affine by [§Affine Varieties, ⁋Proposition 7](/en/math/algebraic_varieties/affine_varieties#prop7), which completes the proof.

</details>

Now, by the proposition above, we can make the following definition.

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> A function $$f: X \rightarrow \mathbb{K}$$ on a quasi-projective variety $$X$$ is called *regular* if there exists an open affine cover $$\{U_i\}$$ of $$X$$ such that, for each $$i$$, the restriction

$$f\vert_{U_i}:U_i\rightarrow\mathbb{K}$$

is an element of the coordinate ring $$\mathbb{K}[U_i]$$ of the affine variety $$U_i$$. The sheaf of all regular functions on $$X$$ is denoted by $$\mathcal{O}_X$$, or more simply by $$\mathcal{O}$$. ([\[Topology\] §Sheaves, ⁋Definition 1](/en/math/topology/sheaves#def1))

</div>

The following are examples of regular functions.

<div class="example" markdown="1">

<ins id="ex6">**Example 6**</ins> Let us look at some examples of regular functions.

1. For an affine variety $$X$$, we have $$\mathcal{O}(X) = \mathbb{K}[X]$$.
2. For $$\mathbb{P}^n$$, we have $$\mathcal{O}(\mathbb{P}^n) = \mathbb{K}$$. To verify this, consider the standard open cover $$U_i = \{x_i \ne 0\}$$. In particular, a regular function on $$U_0$$ is an element of $$\mathbb{K}[\x_1/\x_0, \ldots, \x_n/\x_0]$$, and a regular function on $$U_1$$ is an element of $$\mathbb{K}[\x_0/\x_1, \x_2/\x_1, \ldots, \x_n/\x_1]$$. Thus, if a function $$f$$ is regular on all of $$\mathbb{P}^n$$, then on $$U_0$$ it is a polynomial in the $$\mathrm{s}_i = \x_i/\x_0$$, and on $$U_1$$ it is a polynomial in the $$\mathrm{t}_i = \x_i/\x_1$$. Now on $$U_0 \cap U_1$$, we know that these coordinate functions satisfy the following equations:

    $$\mathrm{t}_0=\frac{1}{\mathrm{s}_1},\qquad \mathrm{t}_j=\frac{\mathrm{s}_j}{\mathrm{s}_1}$$

Therefore, if

    $$f\vert_{U_0}=p(\mathrm{s}_1, \ldots, \mathrm{s}_n),\qquad f\vert_{U_1}=q(\mathrm{t}_0,\mathrm{t}_2,\ldots, \mathrm{t}_n)$$

then the fact that they must define the same function on $$U_0 \cap U_1$$ together with the above equations implies that

    $$p(\mathrm{s}_1,\ldots, \mathrm{s}_n)=q\left(\frac{1}{\mathrm{s}_1},\frac{\mathrm{s}_2}{\mathrm{s}_1}, \ldots,\frac{\mathrm{s}_n}{\mathrm{s}_1}\right)$$

must hold. For the right-hand side to be a polynomial, $$q$$ must be a constant function so that the $$\mathrm{s}_1$$ in the denominator disappears, and hence both $$p$$ and $$q$$ must be constant functions. Applying the same argument to all charts $$U_i, U_j$$ gives the desired result.

</div>

We now define morphisms between varieties, that is, regular maps. There are several ways to define this, but we will always assume that a variety is given together with an embedding into projective space, and since morphisms between projective spaces have already been defined, we use them to make the following definition. ([§Projective Varieties, ⁋Definition 15](/en/math/algebraic_varieties/projective_varieties#def15))

<div class="definition" markdown="1">

<ins id="def7">**Definition 7**</ins> A function $$\varphi: X \rightarrow Y$$ between two varieties $$X \subseteq \mathbb{P}^n$$ and $$Y \subseteq \mathbb{P}^m$$ is called a *morphism* (or *regular map*) if for every $$x \in X$$ there exist a suitable open neighborhood $$U \subseteq X$$ of $$x$$ and homogeneous polynomials $$F_0, \ldots, F_m$$ of the same degree such that

$$\varphi(q) = [F_0(q) : \cdots : F_m(q)]$$

holds for all $$q \in U$$.

</div>

Up to now, whenever we spoke of a variety we assumed an embedding into affine space or projective space, and the above definition is also in line with this assumption. This allows us to perform concrete calculations, but the definition cannot be said to be intrinsic. The next proposition shows that this definition admits a natural interpretation from the viewpoint of regular functions.

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8**</ins> A function $$\varphi: X \to Y$$ is a morphism if and only if, for every affine open set $$V$$ of $$Y$$ and every regular function $$f \in \mathcal{O}_Y(V)$$, the composition $$f \circ \varphi: \varphi^{-1}(V) \to \mathbb{K}$$ is a regular function.

</div>

The key point of the proof is that a morphism is represented locally by homogeneous polynomials, and regular functions on $$Y$$ can be written in the form $$F/G$$ for homogeneous polynomials $$F, G$$ of the same degree $$d$$ (thinking of the dehomogenization process), so their composition must also be a regular function. Using this, we can prove the following.

<div class="proposition" markdown="1">

<ins id="prop9">**Proposition 9**</ins> Regular maps between affine varieties are exactly the regular maps when they are viewed as quasi-projective varieties.

</div>

This is essentially [§Affine Varieties, ⁋Proposition 15](/en/math/algebraic_varieties/affine_varieties#prop15).

## Properties of Regular Maps

<div class="proposition" markdown="1">

<ins id="prop10">**Proposition 10**</ins> A regular map $$\varphi: X \to Y$$ is a continuous function.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

If $$Z \subseteq Y$$ is a closed set, then there exists an open cover $$\{V_\alpha\}$$ of $$Y$$ such that for each $$V_\alpha$$ there are regular functions $$f_{\alpha,1}, \ldots, f_{\alpha,k_\alpha}$$ with

$$Z \cap V_\alpha = \{y \in V_\alpha \mid f_{\alpha,1}(y) = \cdots = f_{\alpha,k_\alpha}(y) = 0\}$$

Then

$$\varphi^{-1}(Z) \cap \varphi^{-1}(V_\alpha) = \{x \in \varphi^{-1}(V_\alpha) \mid f_{\alpha,1}(\varphi(x)) = \cdots = f_{\alpha,k_\alpha}(\varphi(x)) = 0\}$$

Since $$\varphi$$ is a regular map, each $$f_{\alpha,i} \circ \varphi$$ is a regular function on $$\varphi^{-1}(V_\alpha)$$. Therefore $$\varphi^{-1}(Z) \cap \varphi^{-1}(V_\alpha)$$ is a closed subset of $$\varphi^{-1}(V_\alpha)$$, and since $$\{\varphi^{-1}(V_\alpha)\}$$ is an open cover of $$X$$, we conclude that $$\varphi^{-1}(Z)$$ is a closed subset of $$X$$.

</details>

<div class="proposition" markdown="1">

<ins id="prop11">**Proposition 11**</ins> The composition of regular maps is a regular map. The identity map is a regular map.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$\varphi: X \to Y$$ and $$\psi: Y \to Z$$ be regular maps. If $$W \subseteq Z$$ is an open set and $$f \in \mathcal{O}(W)$$, then since $$\psi$$ is regular we have $$f \circ \psi \in \mathcal{O}(\psi^{-1}(W))$$. Now since $$\varphi$$ is regular, $$(f \circ \psi) \circ \varphi \in \mathcal{O}(\varphi^{-1}(\psi^{-1}(W)))$$. That is,

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

Let $$\varphi: X \to Y$$ be a regular map and let $$Z \subseteq Y$$ be a closed set. Consider $$\psi = \varphi\vert_{\varphi^{-1}(Z)}: \varphi^{-1}(Z) \to Z$$. If $$f$$ is a regular function on an open set $$V$$ of $$Z$$, then $$f$$ extends to a regular function on some open set $$V' \supseteq V$$ of $$Y$$ (at least locally). Specifically, by intersecting $$V$$ with an open affine cover of $$Z$$ and defining regular functions on each piece, we can glue them regularly to obtain a regular function on an open neighborhood $$V'$$ in $$Y$$. This is because regular functions are essentially local representations of rational functions, so their definitions on affine charts glue consistently on intersections of Zariski open covers. Then $$f \circ \psi = (f \circ \varphi)\vert_{\varphi^{-1}(Z)}$$, and since $$f \circ \varphi$$ is regular on $$\varphi^{-1}(V')$$, its restriction is also regular.

The case of an open subset is simpler. If $$U \subseteq Y$$ is open and $$f$$ is regular on $$V \subseteq U$$, then $$f \circ \varphi$$ is regular on $$\varphi^{-1}(V)$$.

</details>

<div class="definition" markdown="1">

<ins id="def13">**Definition 13**</ins> A morphism $$\varphi: X \to Y$$ is called an *isomorphism* if there exists an inverse function $$\psi: Y \to X$$ that is also a morphism.

</div>

The notion of an isomorphism means geometrically that the two varieties are the same. That is, isomorphic varieties cannot be distinguished from the viewpoint of regular functions.

<div class="example" markdown="1">

<ins id="ex14">**Example 14**</ins> We have already examined morphisms between projective varieties and morphisms between affine varieties separately, so the functions that connect projective and affine varieties are new. For example, the canonical surjection

$$\mathbb{A}^{n+1}\setminus\{(0,\ldots, 0)\}\rightarrow \mathbb{P}^n;\qquad (x_0,\ldots, x_n)\mapsto [x_0:\cdots:x_n]$$

is a morphism between quasi-projective varieties. Also, the canonical inclusion

$$\iota_i:\mathbb{A}^n\hookrightarrow \mathbb{P}^n$$

is also a morphism between quasi-projective varieties.

</div>

---

**References**

**[Har]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.
