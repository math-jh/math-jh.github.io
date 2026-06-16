---
title: "Properties of Scheme Morphisms"
description: "We define the main properties of scheme morphisms and introduce the concepts and basic properties of quasi-compact and quasi-separated morphisms."
excerpt: "Basic properties of scheme morphisms such as affine, finite, and finite type"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/properties_of_scheme_morphisms
sidebar: 
    nav: "scheme_theory-en"

date: 2025-02-21
last_modified_at: 2025-02-21
weight: 8
translated_at: 2026-06-02T06:00:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-02T06:00:02+00:00
---
In previous posts we explored several viewpoints for studying scheme morphisms. In this post we define the properties that scheme morphisms can have. First we define the following property shared by all of them.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A property $$P$$ of scheme morphisms is called *local on target* if the following two conditions hold.
1. If a scheme morphism $$\varphi:X \rightarrow Y$$ satisfies $$P$$, then for any open subscheme $$V$$ of $$Y$$, the scheme morphism $$\varphi\vert_{\varphi^{-1}(V)}: \varphi^{-1}(V) \rightarrow V$$ also satisfies $$P$$.
2. If for a scheme morphism $$\varphi:X \rightarrow Y$$ there exists an open covering $$\{V_j\}$$ of $$Y$$ such that each $$\varphi\vert_{\varphi^{-1}(V_j)}: \varphi^{-1}(V_j) \rightarrow V_j$$ satisfies $$P$$, then $$\varphi$$ also satisfies $$P$$.

</div>

Schemes are built from affine schemes. If a property $$P$$ of scheme morphisms is local on target, then for a scheme morphism $$\varphi:X \rightarrow Y$$ we may assume the target $$Y$$ is $$\Spec B$$, and then by the adjunction

$$\Hom_\Sch(X, \Spec B)\cong \Hom_\cRing(B, \Gamma(X, \mathcal{O}_X))$$

we can define the property of a scheme morphism $$X \rightarrow \Spec B$$ through the property of the ring homomorphism $$B \rightarrow \Gamma(X, \mathcal{O}_X)$$.

## Quasi-Compact and Quasi-Separated Morphisms

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> A scheme morphism $$\varphi: X \rightarrow Y$$ is *quasi-compact* if for every affine open subset $$V\subseteq Y$$, the preimage $$\varphi^{-1}(V)$$ is quasi-compact.

</div>

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> A scheme morphism $$\varphi: X \rightarrow Y$$ is quasi-compact if and only if the preimage of every quasi-compact open subset of $$Y$$ is quasi-compact.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Since any affine scheme is quasi-compact ([§Spectra, ⁋Lemma 12](/en/math/scheme_theory/spectrums#lem12)), it is obvious that the given condition implies the condition of [Definition 2](#def2).

Conversely, suppose a quasi-compact morphism $$\varphi: X \rightarrow Y$$ is given. Now if any quasi-compact open subset $$V$$ of $$Y$$ is given, there exists a covering $$\{V_j\}$$ of $$V$$ by finitely many affine open subsets, and their preimages $$\varphi^{-1}(V_j)$$ are all quasi-compact. Now

$$\varphi^{-1}(V)=\varphi^{-1}\left(\bigcup_{j\in J} V_j\right)=\bigcup_{j\in J}\varphi^{-1}(V_j)$$

and since a finite union of quasi-compact sets is again quasi-compact, we obtain the desired result.

</details>

Then from the equivalence in [Proposition 3](#prop3), we see that the composition of quasi-compact morphisms is again quasi-compact. Moreover, the following holds.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> For a Noetherian scheme $$X$$, any scheme morphism $$\varphi: X \rightarrow Y$$ is always quasi-compact.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Suppose any affine open subset $$V\subseteq Y$$ is given; we must show that $$\varphi^{-1}(V)$$ is quasi-compact. But by the first result of [[Topology] §Dimension, ⁋Proposition 12](/en/math/topology/dimension#prop12) and [[Topology] §Dimension, ⁋Proposition 13](/en/math/topology/dimension#prop13), any subspace of a Noetherian topological space is quasi-compact.

</details>

Similarly we define quasi-separated morphisms. For this we must first define quasi-separated schemes.

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> A scheme $$X$$ is *quasi-separated* if the intersection of any two quasi-compact open subsets of $$X$$ is again quasi-compact. A scheme morphism $$\varphi: X \rightarrow Y$$ is *quasi-separated* if for every affine open set $$V\subseteq Y$$, the preimage $$\varphi^{-1}(V)$$ is quasi-separated.

</div>

Then the following holds.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> Every locally Noetherian scheme is quasi-separated.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Suppose any two affine open subsets $$V_1=\Spec B_1, V_2=\Spec B_2$$ of a locally Noetherian scheme $$X$$ are given; we must show that $$V_1\cap V_2$$ is quasi-compact.

First, since $$X$$ is locally Noetherian, we can cover $$X$$ by spectra $$\Spec A_i$$ of Noetherian rings. Now for each $$i$$, by [§Topological Structure of Schemes, ⁋Lemma 11](/en/math/scheme_theory/topology_of_schemes#lem11) we can cover $$U_i\cap V_1$$ by spectra $$\Spec (A_i)_g$$ of Noetherian rings. Collecting all of these, we can cover $$V_1$$ by spectra of Noetherian rings, and by [§Spectra, ⁋Lemma 12](/en/math/scheme_theory/spectrums#lem12), $$V_1=\Spec B_1$$ is covered by finitely many spectra of Noetherian rings. Therefore by [§Topological Structure of Schemes, ⁋Lemma 13](/en/math/scheme_theory/topology_of_schemes#lem13), $$B_1$$ is a Noetherian ring and hence $$V_1=\Spec B_1$$ is Noetherian. Again by the first result of [[Topology] §Dimension, ⁋Proposition 12](/en/math/topology/dimension#prop12) and [[Topology] §Dimension, ⁋Proposition 13](/en/math/topology/dimension#prop13), any subspace of a Noetherian topological space is quasi-compact, so in particular $$V_1\cap V_2$$ is also quasi-compact.

</details>

Then quasi-compactness and quasi-separatedness not only satisfy the property of [Definition 1](#def1), but are also *affine-local on target*, as we verify in the following proposition. ([§Topological Structure of Schemes, ⁋Definition 9](/en/math/scheme_theory/topology_of_schemes#def9))

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> For a scheme morphism $$\varphi: X \rightarrow Y$$, the following hold.

1. If there exists an affine open covering $$\{V_j\}$$ of $$Y$$ such that each $$\varphi^{-1}(V_j)$$ is quasi-compact, then $$\varphi$$ is quasi-compact.
2. If there exists an affine open covering $$\{V_j\}$$ of $$Y$$ such that each $$\varphi^{-1}(V_j)$$ is quasi-separated, then $$\varphi$$ is quasi-separated.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

1. Suppose any affine open subset $$V$$ of $$Y$$ is given. Then by [§Topological Structure of Schemes, ⁋Lemma 11](/en/math/scheme_theory/topology_of_schemes#lem11), we can cover $$V\cap V_j$$ by open subsets that are principal open in both $$V$$ and $$V_j$$, and considering this for all $$j$$ and using the quasi-compactness of $$V$$, we can choose only finitely many of these. Write this as $$V=\bigcup W_l$$.   
    On the other hand, for each $$j$$, since $$\varphi^{-1}(V_j)$$ is quasi-compact, we can cover it by finitely many affine open subsets $$U_{jk}$$, and now $$\varphi^{-1}(W_l)\cap U_{jk}$$ is a principal open subset of $$U_{jk}$$ by [§Spectra, ⁋Proposition 8](/en/math/scheme_theory/spectrums#prop8), so each $$\varphi^{-1}(W_l)$$ can be expressed as a finite union of affine open sets, and therefore $$\varphi^{-1}(V)$$ can also be expressed as a finite union of affine open sets. Since a finite union of quasi-compact spaces is quasi-compact, we obtain the desired result.
2. This can also be proved in the same way as the first result, using [§Topological Structure of Schemes, ⁋Lemma 11](/en/math/scheme_theory/topology_of_schemes#lem11) to cover an arbitrary affine open subset $$V=\Spec B$$ by principal open subsets whose preimages are quasi-separated.

</details>

## Affine Morphisms

We know from the adjunction

$$\Hom_\Sch(X, \Spec B)\cong\Hom_\cRing (B, \Gamma(X, \mathcal{O}_X))$$

that in particular, when $$X=\Spec A$$,

$$\Hom_\Sch(\Spec A,\Spec B)\cong\Hom_\cRing (B, A)$$

holds. ([§Affine Schemes, ⁋Proposition 11](/en/math/scheme_theory/affine_schemes#prop11)) Therefore, when examining a property of scheme morphisms that is affine-local on target as above, for any affine open subset $$V\cong\Spec B$$ of $$Y$$, the set $$U=\varphi^{-1}(V)$$ is also an open subscheme $$U\cong \Spec A$$ of $$X$$, and thus $$\varphi\vert_U: U \rightarrow V$$ becomes a morphism between affine schemes, so it would be desirable to obtain this property from the ring homomorphism

$$(\varphi\vert_U)^\sharp(V): \mathcal{O}_V(V) \rightarrow \varphi^\ast \mathcal{O}_U(V)=\mathcal{O}_U(U)$$

However, of course for an arbitrary scheme morphism $$\varphi: X \rightarrow Y$$, the preimage of an affine open subset of $$Y$$ need not be affine. ([§Schemes, ⁋Example 8](/en/math/scheme_theory/schemes#ex8))

<div class="definition" markdown="1">

<ins id="def8">**Definition 8**</ins> A scheme morphism $$\varphi: X \rightarrow Y$$ is *affine* if for every affine open subset $$V$$ of $$Y$$, the preimage $$\varphi^{-1}(V)$$ is an affine open subset of $$X$$.

</div>

Then it is obvious that the composition of affine morphisms is affine. Moreover, this property also satisfies the property of [Definition 1](#def1), but we omit the proof as it is somewhat lengthy.

<div class="proposition" markdown="1">

<ins id="prop9">**Proposition 9**</ins> For a scheme morphism $$\varphi:X \rightarrow Y$$, if there exists an affine open covering $$\{V_j\}$$ of $$Y$$ such that each $$\varphi^{-1}(V_j)$$ is affine, then $$\varphi$$ is affine.

</div>

## Finite, Integral, and Finite Type Morphisms

<div class="definition" markdown="1">

<ins id="def10">**Definition 10**</ins> A scheme morphism $$\varphi:X \rightarrow Y$$ is *finite* if $$\varphi$$ is affine and, for every affine open subset $$V$$ of $$Y$$, the ring homomorphism

$$(\varphi\vert_{\varphi^{-1}(V)})^\sharp(V): \mathcal{O}_V(V) \rightarrow \varphi^\ast \mathcal{O}_{\varphi^{-1}(V)}(V)$$

is a finite ring homomorphism. ([[Commutative Algebra] §Integral Extensions, ⁋Definition 3](/en/math/commutative_algebra/integral_extension#def3))

</div>

To aid understanding, let us write an affine open subset $$V\subseteq Y$$ as $$\Spec B$$. Then from the assumption that $$\varphi$$ is affine, $$U=\varphi^{-1}(V)$$ is an affine open subset of $$X$$, and thus there exists $$A$$ such that $$U\cong\Spec A$$. Through this identification, the scheme morphism $$\varphi\vert_U: U \rightarrow V$$ is the same as the morphism of spectra $$\Spec A \rightarrow \Spec B$$, and now $$\varphi$$ being finite means that the ring homomorphism $$B \rightarrow A$$ corresponding to this morphism is finite. Similarly we define the following.

<div class="definition" markdown="1">

<ins id="def11">**Definition 11**</ins> A scheme morphism $$\varphi:X \rightarrow Y$$ is *integral* if $$\varphi$$ is affine and, for every affine open subset $$V$$ of $$Y$$, the ring homomorphism

$$(\varphi\vert_{\varphi^{-1}(V)})^\sharp(V): \mathcal{O}_V(V) \rightarrow \varphi^\ast \mathcal{O}_{\varphi^{-1}(V)}(V)$$

is an integral ring homomorphism. ([[Commutative Algebra] §Integral Extensions, ⁋Definition 3](/en/math/commutative_algebra/integral_extension#def3))

</div>

From their definitions we now know that finite morphisms and integral morphisms are closed under composition. Also, that they satisfy the conditions of [Definition 1](#def1) follows from [[Commutative Algebra] §Integral Extensions, ⁋Proposition 14](/en/math/commutative_algebra/integral_extension#prop14) and [[Commutative Algebra] §Integral Extensions, ⁋Proposition 15](/en/math/commutative_algebra/integral_extension#prop15), so they are all affine-local on target.

We know by [[Commutative Algebra] §Integral Extensions, ⁋Lemma 4](/en/math/commutative_algebra/integral_extension#lem4) that any finite morphism is integral. To state this lemma completely in the language of algebraic geometry, we must define finite type morphisms.

<div class="definition" markdown="1">

<ins id="def12">**Definition 12**</ins> A scheme morphism $$\varphi:X \rightarrow Y$$ is *locally of finite type* if for every affine open subset $$V$$ of $$Y$$ and every affine open subset $$U$$ of $$\varphi^{-1}(V)$$,

$$(\varphi\vert_{U})^\sharp(V): \mathcal{O}_V(V) \rightarrow \varphi^\ast \mathcal{O}_{\varphi^{-1}(V)}(V)$$

is of finite type. ([[Commutative Algebra] §Integral Extensions, ⁋Definition 3](/en/math/commutative_algebra/integral_extension#def3))

</div>

Just as above, let $$V\cong \Spec B$$ and $$U\cong\Spec A\subseteq \varphi^{-1}(V)$$. Then we can view the scheme morphism $$\varphi\vert_U: U \rightarrow V$$ as $$\Spec A \rightarrow \Spec B$$, and we require that the corresponding ring homomorphism $$B \rightarrow A$$ be of finite type. Then a finite type morphism is defined as follows.

<div class="definition" markdown="1">

<ins id="def13">**Definition 13**</ins> A scheme morphism $$\varphi:X \rightarrow Y$$ is a *morphism of finite type* if $$\varphi$$ is a quasi-compact morphism locally of finite type.

</div>

It is clear from the definition that being locally of finite type is affine-local on target. Also, since being quasi-compact is affine-local on target by [Proposition 7](#prop7), being of finite type is also affine-local on target.

Then by [[Commutative Algebra] §Integral Extensions, ⁋Lemma 4](/en/math/commutative_algebra/integral_extension#lem4), the following holds.

<div class="proposition" markdown="1">

<ins id="prop14">**Proposition 14**</ins> A scheme morphism $$\varphi:X \rightarrow Y$$ is finite if and only if it is an integral morphism (locally) of finite type.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

One direction is obvious. For the converse, first from the assumption that $$\varphi$$ is integral we know that for any affine open subset $$V\subseteq Y$$, the preimage $$\varphi^{-1}(V)$$ is an affine open subset of $$X$$, and then we apply [[Commutative Algebra] §Integral Extensions, ⁋Lemma 4](/en/math/commutative_algebra/integral_extension#lem4) to the resulting ring map.

</details>

In the above proposition, since $$\varphi$$ is an integral morphism it is an affine morphism, and hence a quasi-compact morphism ([§Spectra, ⁋Lemma 12](/en/math/scheme_theory/spectrums#lem12)), so whether $$\varphi$$ is of finite type or locally of finite type becomes the same assumption.

<div class="example" markdown="1">

<ins id="ex15">**Example 15**</ins> Let us look at examples of the morphisms examined in this section. In the world of affine schemes this is nothing more than looking at the examples from [[Commutative Algebra] §Integral Extensions, ⁋Definition 3](/en/math/commutative_algebra/integral_extension#def3). The purpose of this example is to give geometric intuition for these.

First, for an algebraically closed field $$\mathbb{K}$$, consider the ring map $$\iota:\mathbb{K}[\x] \rightarrow \mathbb{K}[\x,\y]$$. Then $$\mathbb{K}[\x,\y]$$ is generated as a $$\mathbb{K}[\x]$$-algebra by the single element $$\y$$, so it is a finite type ring homomorphism, but it is not finitely generated as a $$\mathbb{K}[\x]$$-module, so it is not a finite ring homomorphism.

Now consider the corresponding scheme morphism $$\Spec\iota: \Spec \mathbb{K}[\x,\y] \rightarrow\Spec \mathbb{K}[\x]$$. This is the map that takes any prime ideal $$\mathfrak{p}\subset \mathbb{K}[\x,\y]$$ and returns the prime ideal $$\mathfrak{p}\cap \mathbb{K}[\x]$$ of $$\mathbb{K}[\x]$$. Geometrically this is the map that sends a point $$(x,y)$$ of the affine plane $$\mathbb{A}^2_\mathbb{K}$$ to the point $$x$$ of the affine line $$\mathbb{A}^1_\mathbb{K}$$.

![finite_type_morphism](/assets/images/Math/Scheme_Theory/Properties_of_Scheme_Morphisms-1.svg){:style="width:27.72em" class="invert" .align-center}

As an example of a finite morphism related to this, there is the composition of the above ring homomorphism $$\iota:\mathbb{K}[\x]\rightarrow \mathbb{K}[\x,\y]$$ with the projection map $$\pi:\mathbb{K}[\x,\y] \rightarrow \mathbb{K}[\x,\y]/(\x-\y^2)$$. Then $$\mathbb{K}[\x,\y]/(\x-\y^2)$$ is generated as a $$\mathbb{K}[\x]$$-module by $$1$$ and $$\y$$, so $$\phi:\mathbb{K}[\x] \rightarrow \mathbb{K}[\x,\y]/(\x-\y^2)$$ is a finite morphism.

On the other hand, we know that the ring homomorphism $$\pi:A \rightarrow A/\mathfrak{a}$$ corresponds geometrically to the inclusion of the closed subset defined by $$\mathfrak{a}$$. Therefore the composite

$$\phi: \mathbb{K}[\x] \rightarrow \mathbb{K}[\x,\y] \rightarrow \mathbb{K}[\x,y]/(\x-\y^2)$$

defines the scheme morphism

$$\Spec\phi: \Spec \frac{\mathbb{K}[\x,\y]}{(\x-\y^2)}\rightarrow \Spec \mathbb{K}[\x,\y] \rightarrow \Spec\mathbb{K}[\x]$$

which can be viewed geometrically as the projection from the zero set $$Z(\x-\y^2)$$ of $$\x=\y^2$$ to the $$x$$-axis.

![finite_morphism](/assets/images/Math/Scheme_Theory/Properties_of_Scheme_Morphisms-2.svg){:style="width:25.48em" class="invert" .align-center}

The geometric difference between these two examples is quite clear. In the first example, the fiber over a point of the target is an infinite set, whereas in the second example the fiber over a point is a finite set. Algebraically this can be checked as follows: when we take an arbitrary point $$\mathfrak{p}=(\x-a)$$ of the target $$\mathbb{A}_\mathbb{K}^1$$, any $$\mathfrak{q}_b=(\x-a, \y-b)\in \mathbb{A}_\mathbb{K}^2$$ satisfies $$(\Spec\iota)(\mathfrak{q}_b)=\mathfrak{p}$$, whereas in the second example only the two points $$\mathfrak{q}_+=(\x-a, \y-\sqrt{a})$$ and $$\mathfrak{q}_-=(\x-a, \y+\sqrt{a})$$ satisfy $$(\Spec\phi)(\mathfrak{q}_\pm)=\mathfrak{p}$$.

Thus, finite type morphisms are related geometrically to fibers being finite-dimensional, and finite morphisms are related to fibers being finite sets.

</div>

For now, to compute the fiber of a scheme morphism in a situation like [Example 15](#ex15) above, we have no choice but to carry out calculations straightforwardly according to the situation at hand, but later once we have computed fiber products we will be able to use a somewhat more standardized method. For that time we define the following.

<div class="definition" markdown="1">

<ins id="def16">**Definition 16**</ins> A scheme morphism $$\varphi: X \rightarrow Y$$ is *quasi-finite* if $$\varphi$$ is a morphism of finite type and for every $$y\in Y$$ the set $$\varphi^{-1}(y)$$ is always a finite set.

</div>

Then the geometric intuition for finite morphisms in [Example 15](#ex15) is always true. That is, any finite morphism is always quasi-finite. We could prove this right away, but we postpone it until after we have defined fiber products.

Finally we define the following.

<div class="definition" markdown="1">

<ins id="def17">**Definition 17**</ins> A scheme morphism $$\varphi: X \rightarrow Y$$ is *locally of finite presentation* if for every affine open subset $$V\cong \Spec B$$ of $$Y$$, there exists a covering $$\varphi^{-1}(V)=\bigcup \Spec A_i$$ of $$\varphi^{-1}(V)$$ such that the maps $$B \rightarrow A_i$$ are all finitely presented. If a scheme morphism $$\varphi:X \rightarrow Y$$ is quasi-compact, quasi-separated, and locally of finite presentation, then $$\varphi$$ is called a *morphism of finite presentation*.

</div>

In most cases we consider the situation where all schemes are locally Noetherian, and in this case by [[Commutative Algebra] §Basic Notions, ⁋Proposition 9](/en/math/commutative_algebra/basic_notions#prop9) this notion is not new.
