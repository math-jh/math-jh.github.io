---
title: "Topological Structure of Schemes"
description: "We define closed points, generic points, and specialization in the topological structure of schemes, and examine how points of an affine scheme relate to ideals and express topological properties."
excerpt: "Generic points, Zariski topology, and irreducible components"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/topology_of_schemes
sidebar: 
    nav: "scheme_theory-en"

date: 2025-02-03
last_modified_at: 2025-02-23
weight: 5
translated_at: 2026-06-02T07:30:01+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-02T07:30:01+00:00
---
## Generic Points

We now examine the topological structure carried by a scheme. As we saw in [§Spectra](/en/math/scheme_theory/spectrums), a scheme $$X$$ is endowed with a topology quite different from the spaces one usually encounters. One of its most peculiar features is that a singleton need not be closed.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A point $$x$$ of a topological space $$X$$ is called a *closed point* if $$\{x\}$$ is a closed subset of $$X$$.

</div>

Thus, a space $$X$$ is a $$T_1$$-space if and only if every point of $$X$$ is closed. ([\[Topology\] §Hausdorff Spaces, ⁋Definition 3](/en/math/topology/Hausdorff_spaces#def3)) In particular, we have already seen that the spectrum of an integral domain which is not a field has no closed points.

On the other hand, every affine scheme necessarily has a closed point.[^1] Indeed, choosing a maximal ideal $$\mathfrak{m}$$ of a ring $$A$$, we have $$Z(\mathfrak{m})=\{\mathfrak{m}\}$$, and applying [§Spectra, ⁋Proposition 14](/en/math/scheme_theory/spectrums#prop14) and [\[Set Theory\] §Filters, Ideals, and Galois Connections, ⁋Proposition 7](/en/math/set_theory/filter_and_ideal#prop7) yields

$$\cl(\{\mathfrak{m}\})=ZI(\{\mathfrak{m}\})=ZIZ(\mathfrak{m})=Z(\mathfrak{m})=\{\mathfrak{m}\}$$.

Similarly, if an affine scheme $$\Spec A$$ has a closed point $$\mathfrak{p}$$, then from $$I(\{\mathfrak{p}\})=\mathfrak{p}$$ and [§Spectra, ⁋Proposition 14](/en/math/scheme_theory/spectrums#prop14) we obtain

$$Z(\mathfrak{p})=ZI(\{\mathfrak{p}\})=\cl(\{\mathfrak{p}\})=\{\mathfrak{p}\}$$,

so $$\mathfrak{p}$$ must be a maximal ideal.

By definition, if a point $$\mathfrak{p}$$ of $$\Spec A$$ is not closed, there exists a point $$\mathfrak{q}\neq \mathfrak{p}$$ of $$\Spec A$$ with $$\mathfrak{q}\in \cl(\{\mathfrak{p}\})$$.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> Let $$x,y$$ be two points of a topological space $$X$$ with $$x\in\cl(\{y\})$$. Then we call $$x$$ a *specialization* of $$y$$, and $$y$$ a *generalization* of $$x$$. If for a closed subset $$C$$ of a topological space $$X$$ we have $$C=\cl(\{x\})$$, then we call $$x$$ a *generic point* of $$C$$.

</div>

Then by definition, if $$x$$ is a generic point of $$C$$, every open subset $$U$$ contains $$x$$. Hence a generic point can be regarded as a point lying arbitrarily close to every point of $$C$$.

In particular, when $$X$$ is an affine scheme $$\Spec A$$, we have already verified that any irreducible closed subset of $$\Spec A$$ is of the form $$Z(\mathfrak{p})$$ for some prime ideal $$\mathfrak{p}$$ of $$A$$. Then $$\mathfrak{p}\in Z(\mathfrak{p})$$ trivially, and since $$\mathfrak{p}$$ is obviously (uniquely) minimal among the prime ideals belonging to $$Z(\mathfrak{p})$$, it is the (unique) generic point of $$Z(\mathfrak{p})$$.

To make this more geometric, let $$A=\mathbb{K}[\x_1,\x_2]/(\x_2-\x_1^2)$$. Then in [§Spectra, ⁋Proposition 9](/en/math/scheme_theory/spectrums#prop9) we showed that $$\Spec A$$ is a closed subset of $$\mathbb{A}_\mathbb{K}^2=\Spec \mathbb{K}[\x_1,\x_2]$$. We now see that the prime ideal $$(\x_2-\x_1^2)\in \Spec \mathbb{K}[\x_1,\x_2]$$ is the generic point of $$\Spec A\cong Z(\x_2-\x_1^2)$$. That is, the generic point can be interpreted as representing the curve $$\x_2-\x_1^2$$ itself.

## Topological Properties of Schemes

A scheme, if we ignore its structure sheaf, is simply a topological space, and therefore may possess properties of topological spaces.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> Let $$(X,\mathscr{O}_X)$$ be a scheme. If $$X$$ is quasi-compact (resp. irreducible, connected) as a topological space, we call $$X$$ a quasi-compact (resp. irreducible, connected) scheme.

</div>

The corresponding definitions in topology can be found in [\[Topology\] §Compact Spaces, ⁋Definition 1](/en/math/topology/compact_spaces#def1), [\[Topology\] §Dimension, ⁋Definition 6](/en/math/topology/dimension#def6), and [\[Topology\] §Connected Spaces, ⁋Definition 1](/en/math/topology/connected_spaces#def1), respectively.[^2] The following are examples and counterexamples illustrating this definition.

<div class="example" markdown="1">

<ins id="ex4">**Example 4**</ins> By [§Spectra, ⁋Lemma 12](/en/math/scheme_theory/spectrums#lem12), we know that every affine scheme is quasi-compact. As an example of a scheme that is not quasi-compact, one may of course take a disjoint union of infinitely many schemes.

</div>

For irreducibility, consider the following examples.

<div class="example" markdown="1">

<ins id="ex5">**Example 5**</ins> For any integral domain $$A$$, the space $$\Spec A$$ is always irreducible. Indeed, considering the generic point $$\{0\}$$, any closed subset containing $$\{0\}$$ must be $$\Spec A$$ itself, so it is impossible to write $$\Spec A$$ as a union of two proper closed subsets. Thus, setting $$A=\mathbb{K}[\x_0,\ldots, \x_n]$$, we see that affine $$n$$-space $$\mathbb{A}_\mathbb{K}^n$$ is irreducible. Then projective space $$\mathbb{P}^n_\mathbb{K}$$ has irreducible open subsets $$D_+(\x_i)$$, so by [\[Topology\] §Dimension, ⁋Proposition 8](/en/math/topology/dimension#prop8), $$\mathbb{P}^n_\mathbb{K}$$ is also irreducible.

Conversely, any irreducible closed subset $$Z$$ of a scheme $$X$$ always has a generic point $$I(Z)$$. ([§Spectra, ⁋Proposition 16](/en/math/scheme_theory/spectrums#prop16))

</div>

Since an irreducible space is always connected, the above examples also furnish examples of connected spaces. The following example provides schemes that are not connected, and schemes that are connected but not irreducible, realized as certain *closed subschemes* of the affine plane $$\mathbb{A}^2_\mathbb{K}$$.

We have not yet defined closed subschemes, but at least in [§Spectra, ⁋Proposition 9](/en/math/scheme_theory/spectrums#prop9) we already saw that for an affine scheme $$\Spec A$$ and any ideal $$\mathfrak{a}$$ of $$A$$, the canonical morphism $$A \rightarrow A/\mathfrak{a}$$ makes $$\Spec A/\mathfrak{a}$$ and $$Z(\mathfrak{a})\subseteq \Spec A$$ homeomorphic as topological spaces. Since connectedness and irreducibility are both topological properties, the topological properties of $$\Spec A/\mathfrak{a}$$ can be checked by examining the topological structure of the closed subset $$Z(\mathfrak{a})$$ of $$\Spec A$$. When we call these closed subschemes, the only missing ingredient is the relationship between the structure sheaf of $$\Spec A/\mathfrak{a}$$ and the structure sheaf of $$\Spec A$$ (restricted to $$Z(\mathfrak{a})$$), which we will revisit in [§Closed Subschemes](/en/math/scheme_theory/closed_subschemes).

<div class="example" markdown="1">

<ins id="ex6">**Example 6**</ins> First, an example of a scheme that is not connected is the closed subscheme of $$\mathbb{A}^2_\mathbb{K}$$

$$\Spec \frac{\mathbb{K}[\x,\y]}{(\x(\x-1))}$$.

That this is not connected follows from the observation that it can be written as a disjoint union of the two subschemes $$\Spec \mathbb{K}[\x,\y]/(\x)$$ and $$\Spec \mathbb{K}[\x,\y]/(\x-1)$$.

On the other hand, an example of a scheme that is connected but not irreducible is

$$Z(\x\y)=\Spec \frac{\mathbb{K}[\x,\y]}{(\x\y)}$$,

and the irreducible components of this scheme are $$\Spec\mathbb{K}[\x,\y]/(\x)$$ and $$\Spec \mathbb{K}[\x,\y]/(\y)$$.

![counterexamples](/assets/images/Math/Algebraic_Varieties/Properties_of_schemes-1.png){:style="width:20em" class="invert" .align-center}

</div>

Meanwhile, examples of noetherian schemes are provided by the following proposition.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> For a noetherian ring $$A$$, the space $$\Spec A$$ is always a noetherian topological space.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Given a descending chain of closed subsets of $$\Spec A$$

$$Z(\mathfrak{a}_1)\supseteq Z(\mathfrak{a}_2)\supseteq\cdots$$

we obtain a chain of ideals of $$A$$

$$IZ(\mathfrak{a}_1)\subseteq IZ(\mathfrak{a}_2)\subseteq\cdots$$

which equals

$$\sqrt{\mathfrak{a}_1}\subseteq \sqrt{\mathfrak{a}_2}\subseteq\cdots$$.

Since $$A$$ is assumed noetherian, there exists $$k$$ such that

$$\sqrt{\mathfrak{a}_k}=\sqrt{\mathfrak{a}_{k+1}}=\cdots$$

holds, and hence

$$Z(\sqrt{\mathfrak{a}_k})=Z(\sqrt{\mathfrak{a}_{k+1}})=\cdots$$.

Now [§Spectra, ⁋Proposition 5](/en/math/scheme_theory/spectrums#prop5) gives the desired result.

</details>

However, the converse does not hold in general.

## Locality

In the next post we will examine the algebraic properties of schemes. The topological properties examined here and the algebraic properties to be examined next are, of course, closely related, and considering them together deepens our understanding of schemes. We conclude this post by introducing definitions that let us examine this interplay more closely. In particular, in what follows we can endow the localizations $$A_f$$ and $$A_\mathfrak{p}$$ of a ring $$A$$ with geometric intuition.

<div class="definition" markdown="1">

<ins id="def8">**Definition 8**</ins> A property $$Q$$ of rings is called *local* if the following two conditions hold.

1. For any ring $$A$$ and any $$f\in A$$, if $$A$$ satisfies $$Q$$, then $$A_f$$ also satisfies $$Q$$.
2. Let $$A$$ be any ring and let $$f_1,\ldots, f_n\in A$$ satisfy $$A=(f_1,\ldots, f_n)$$. If all $$A_{f_i}$$ satisfy $$Q$$, then $$A$$ also satisfies $$Q$$.

</div>

Let us rephrase this in the language of affine schemes. If a ring $$A$$ satisfies a local property $$Q$$,

$$D(f)\cong \Spec A_f$$

so the global sections $$\mathscr{O}_{\Spec A}(D(f))$$ of the principal open set $$D(f)$$ of $$\Spec A$$ also satisfy $$P$$. Conversely, if $$A$$ is generated by $$f_1,\ldots, f_r$$, then from the identity

$$A=A\setminus \emptyset=A\setminus Z(1)=A\setminus Z\left(\sum_{i=1}^r Z(f_i)\right)=A\setminus\bigcap_{i=1}^r Z(f_i)=\bigcup_{i=1}^rA\setminus Z(f_i)=\bigcup_{i=1}^r D(f_i)$$

we see that the $$D(f_i)$$ cover $$\Spec A$$. For convenience, if the ring $$\mathscr{O}_X(X)$$ of global sections of an affine scheme $$X$$ has property $$Q$$, let us say that $$X$$ has property $$P$$. Then the two conditions of [Definition 8](#def8) translate as follows.

1. If $$\Spec A$$ satisfies $$P$$, then every principal open set $$D(f)$$ also satisfies $$P$$.
2. If an open covering $$D(f_1),\ldots, D(f_r)$$ of $$\Spec A$$ satisfies $$P$$, then $$\Spec A$$ also satisfies $$P$$.

On the other hand, a general open set $$U$$ of $$\Spec A$$ can be written as a union of principal open sets ([§Spectra, ⁋Lemma 11](/en/math/scheme_theory/spectrums#lem11)), and therefore if $$\Spec A$$ satisfies $$P$$, we know that every *affine* open subset $$U$$ of $$\Spec A$$ satisfies $$P$$. From this perspective, a property $$P$$ of schemes satisfying the above two conditions is also called an *affine-local property*.

<div class="definition" markdown="1">

<ins id="def9">**Definition 9**</ins> A property $$P$$ defined for suitable affine subschemes of a scheme $$X$$ is called an *affine-local property* if the following two conditions hold.

1. If $$\Spec A\subseteq X$$ satisfies $$P$$, then for any $$f\in A$$, the subscheme $$\Spec A_f\subseteq X$$ also satisfies $$P$$.
2. If $$A=(f_1,\ldots, f_r)$$ and all $$\Spec A_{f_i}\subseteq X$$ satisfy $$P$$, then $$\Spec A \subseteq X$$ also satisfies $$P$$.

</div>

On the other hand, since we already saw in [§Schemes, ⁋Example 8](/en/math/scheme_theory/schemes#ex8) that an open subscheme of an affine scheme need not be affine, even if $$P$$ is a local property of rings, a property $$P$$ defined in this manner is not a local property in the true sense. To remedy this, we make the following definition.

<div class="definition" markdown="1">

<ins id="def10">**Definition 10**</ins> For an affine-local property $$P$$ of schemes, a scheme $$(X, \mathscr{O}_X)$$ is called *locally $$P$$* if for every $$x\in X$$ there exists an open affine neighborhood $$U$$ of $$x$$ such that the affine open subscheme $$U$$ of $$X$$ satisfies $$P$$.

</div>

Then in [Lemma 12](#lem12) we show that if a scheme $$X$$ is locally $$P$$, then every open subscheme of $$X$$ is locally $$P$$. First, we prove the following lemma.

<div class="proposition" markdown="1">

<ins id="lem11">**Lemma 11 (Nike)**</ins> Let $$X$$ be a scheme and let $$U,V$$ be affine open subsets. Then for any $$x\in U\cap V$$, there exists $$W$$ with $$x\in W\subseteq U\cap V$$ such that $$W$$ is a principal open subset in both $$U$$ and $$V$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

For notation, write $$U=\Spec A$$ and $$V=\Spec B$$, and suppose $$x$$ corresponds to prime ideals $$\mathfrak{p}\subset A$$ and $$\mathfrak{q}\subset B$$, respectively. First, viewing $$U\cap V$$ as an open subset of $$U$$ and applying [§Spectra, ⁋Lemma 11](/en/math/scheme_theory/spectrums#lem11), we can choose a principal open set $$D(f)$$ of $$U$$ such that

$$\mathfrak{p}\in D(f)\subseteq U\cap V$$.

Here, since $$D(f)\cong \Spec A_f$$, the inclusion $$D(f)\hookrightarrow V$$ is obtained from the ring homomorphism $$i:B \rightarrow A_f$$.

Now viewing $$D(f)\cong\Spec A_f$$ as an open subset of $$V$$, there again exists a principal open set $$D(g)$$ of $$V$$ such that

$$\mathfrak{q}\in D(g)\subseteq D(f)\cap V$$.

It remains to verify that the open subscheme $$D(g)$$ of $$\Spec B$$ and the open subscheme $$D(i(g))$$ of $$\Spec A$$ coincide.

</details>

<div class="proposition" markdown="1">

<ins id="lem12">**Lemma 12**</ins> For a scheme $$X$$ and an affine-local property $$P$$ of schemes, the following are all equivalent.

1. $$X$$ is locally $$P$$.
2. Every affine open subset $$U\subseteq X$$ satisfies $$P$$ as an open subscheme of $$X$$.
3. There exists an affine open covering $$\{U_i\}$$ of $$X$$ such that every open subscheme $$U_i$$ of $$X$$ satisfies $$P$$.
4. There exists an open covering $$\{U_i\}$$ of $$X$$ such that each open subscheme $$(U_i, \mathscr{O}_X\vert_{U_i})$$ is locally $$P$$.

In particular, if $$X$$ is locally $$P$$, then every open subscheme of $$X$$ is locally $$P$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

If the first condition holds, then for each $$x$$ there exists an open affine neighborhood $$U_x$$. Thus $$\{U_x\}_{x\in X}$$ is an affine open covering of $$X$$ as required in the third condition. Conversely, given an affine open covering $$\{U_i\}$$ as in the third condition, for any point $$x$$ of $$X$$ we can choose $$U_i$$ with $$x\in U_i$$, and this $$U_i$$ is an open affine neighborhood of $$x$$ as required in [Definition 9](#def9). Hence the first and third conditions are equivalent. It is obvious that the second condition implies the first.

Now assume the third condition and prove the second. Let $$\{U_i=\Spec A_i\}$$ be an affine open covering of $$X$$ satisfying the third condition. For any affine open subset $$V=\Spec A$$ of $$X$$, since each $$V\cap U_i$$ is also an open subset of $$V$$, by [Lemma 11](#lem11) we can find

$$V=\bigcup_{i\in I} V\cap U_i=\bigcup_{i\in I} \bigcup_{j\in J_i} \Spec (A_i)_{f_j}$$

and, knowing that each $$\Spec (A_i)_{f_j}$$ can be taken as a suitable localization $$\Spec A_{g_j}$$ of $$\Spec A$$, by using [§Spectra, ⁋Lemma 12](/en/math/scheme_theory/spectrums#lem12) we may assume that the $$g_j$$ are finite in number. Now from the discussion before [Definition 9](#def9) and the assumption that $$P$$ is local, we know that each $$\Spec (A_i)_{f_j}=\Spec A_{g_j}$$ satisfies $$P$$, and hence that $$\Spec A$$ satisfies $$P$$.

Thus the first three conditions are all equivalent.

Now suppose $$X$$ is locally $$P$$, and let $$U$$ be any open subscheme of $$X$$. For any $$x\in U$$, by [§Spectra, ⁋Lemma 11](/en/math/scheme_theory/spectrums#lem11) we can find an affine open subset $$D(f)$$ of $$X$$ with $$x\in D(f)\subseteq U$$, and by the second condition we know that $$D(f)$$ is an affine scheme satisfying $$P$$. Therefore the scheme $$U$$ is also locally $$P$$, yielding the final claim. Finally, the equivalence of the fourth condition with the rest follows from this claim by simply dropping the affine hypothesis in the second and third conditions.

</details>

Meanwhile, we showed in [Proposition 7](#prop7) that for a noetherian ring $$A$$, the space $$\Spec A$$ is noetherian. Let us now define what it means for an arbitrary scheme $$X$$ to be noetherian.

<div class="proposition" markdown="1">

<ins id="lem13">**Lemma 13**</ins> The property of a ring $$A$$ being noetherian is a local property, and therefore defines an affine-local property $$P$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

We must verify the two conditions of [Definition 8](#def8).

The first condition follows from [\[Commutative Algebra\] §Localization, ⁋Corollary 9](/en/math/commutative_algebra/localization#cor9), or alternatively from the first part of [\[Topology\] §Dimension, ⁋Proposition 13](/en/math/topology/dimension#prop13).

For the second condition, suppose $$A=(f_1,\ldots, f_r)$$. We know that the $$D(f_i)$$ form an open covering of $$\Spec A$$, and therefore since $$\mathscr{O}_{\Spec A}$$ satisfies the first condition of [\[Topology\] §Sheaves, ⁋Definition 1](/en/math/topology/sheaves#def1) we obtain the inclusion

$$A \cong \mathscr{O}_{\Spec A}(\Spec A) \hookrightarrow \prod_{i=1}^r \mathscr{O}_{\Spec A}(D(f_i))\cong\prod_{i=1}^r A_{f_i}$$.

Now if all the $$A_{f_i}$$ are noetherian, then their (finite) product $$\prod A_{f_i}$$ is also noetherian, and since $$A$$ is a subring of a noetherian ring, it is noetherian by [\[Commutative Algebra\] §Basic Notions, ⁋Theorem 3](/en/math/commutative_algebra/basic_notions#thm3).

</details>

<div class="definition" markdown="1">

<ins id="def14">**Definition 14**</ins> A scheme $$X$$ is called a *locally noetherian scheme* if there exists an affine open covering $$\{U_i=\Spec A_i\}$$ of $$X$$ such that all $$A_i$$ are noetherian. If $$X$$ is a quasi-compact locally noetherian scheme, we call it a *noetherian scheme*.

</div>

Then if $$A$$ is noetherian, it is obvious from the definition and [§Spectra, ⁋Lemma 12](/en/math/scheme_theory/spectrums#lem12) that $$\Spec A$$ is a noetherian scheme. Also, just as in [Proposition 7](#prop7), any noetherian scheme is noetherian as a topological space. However, as pointed out after [Proposition 7](#prop7), one should be careful that even if a scheme $$X$$ is noetherian as a topological space, the above condition need not hold.

Finally, we define a notion of locality somewhat different from [Definition 9](#def9), namely the notion of *stalk-local*.

<div class="definition" markdown="1">

<ins id="def15">**Definition 15**</ins> A property $$P$$ of a scheme $$X$$ is called *stalk-local* if for each $$x\in X$$, the ring $$\mathscr{O}_{X,x}$$ satisfies a property $$Q$$ of rings.

</div>

Then the following holds.

<div class="proposition" markdown="1">

<ins id="prop16">**Proposition 16**</ins> For a stalk-local property $$P$$ of a scheme $$X$$, the following are all equivalent.

1. $$X$$ satisfies $$P$$.
2. Every open subscheme of $$X$$ satisfies $$P$$.
3. Every affine open subscheme of $$X$$ satisfies $$P$$.
4. One can choose an affine open cover $$\{U_i\}$$ of $$X$$ such that each open subscheme $$U_i$$ satisfies $$P$$.
5. One can choose an open cover $$\{U_i\}$$ of $$X$$ such that each open subscheme $$U_i$$ satisfies $$P$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, $$2\implies 3\implies 4\implies 5$$ is obvious, so it suffices to show $$5\implies 1$$ and $$1\implies 2$$, and these follow from the isomorphism

$$\mathscr{O}_{X,x}= \varinjlim_{V\ni x} \mathscr{O}_X(V)\cong \varinjlim_{U\supseteq V\ni x}\mathscr{O}_X(V)=\mathscr{O}_{U, x}$$.

</details>

In particular, any stalk-local property is also an affine-local property. However, this is a proposition requiring some care, because for instance if a stalk-local property on $$X$$ is given by

$$\text{$X$ is $P$}\iff \text{$\mathscr{O}_{X,x}$ satisfies $Q$}$$

then it is <em-ko>not</em-ko> that $$\mathscr{O}_X(U)$$ satisfies $$Q$$ for an arbitrary affine open subset $$U$$, but rather that $$\mathscr{O}_{U,x}$$ satisfies property $$Q$$ for any affine open subset $$U$$ and any element $$x\in U$$, and therefore the affine open subscheme $$U$$ satisfies property $$P$$.

For example, consider the affine scheme

$$X=\Spec A=\Spec\left(\prod_{i=1}^\infty \mathbb{Z}/2\mathbb{Z}\right)$$.

Any element $$x$$ of $$A$$ satisfies $$x^2=x$$, and therefore so does any element of an arbitrary localization $$A_\mathfrak{p}$$. From $$x(1-x)=0$$ in $$A_{\mathfrak{p}}$$, we know that either $$x\in \mathfrak{p}A_\mathfrak{p}$$ or $$1-x\in \mathfrak{p}A_\mathfrak{p}$$, and we know that an element not belonging to $$\mathfrak{p}A_\mathfrak{p}$$ is a unit. ([\[Commutative Algebra\] §Localization, ⁋Proposition 2](/en/math/commutative_algebra/localization#prop2)) Therefore $$x=0$$ or $$x=1$$, so the chain of ideals of $$A_\mathfrak{p}$$ is simply $$(0)\subseteq (1)=A_\mathfrak{p}$$. Hence each $$A_\mathfrak{p}$$ is noetherian, but considering

$$A\times \{0\}\times\{0\}\times\cdots\subseteq A\times A\times\{0\}\subseteq\cdots$$

we see that $$A$$ is not noetherian.

---
**References**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).  

---

[^1]: However, there exist schemes having no closed points.
[^2]: After [§Spectra, ⁋Lemma 11](/en/math/scheme_theory/spectrums#lem11) we agreed to call a compact topological space (which may not be Hausdorff) *quasi-compact*.
