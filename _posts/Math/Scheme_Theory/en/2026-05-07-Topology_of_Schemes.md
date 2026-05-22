---
title: "Topological Structure of Schemes"
excerpt: "Generic points, Zariski topology, and irreducible components"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/topology_of_schemes
header:
    overlay_image: /assets/images/Math/Algebraic_Varieties/Topology_of_schemes.png
    overlay_filter: 0.5
sidebar: 
    nav: "scheme_theory-en"

date: 2025-02-03
last_modified_at: 2025-02-23
weight: 5
translated_at: 2026-05-22T20:30:02+00:00
translation_source: kimi-cli
---
## Generic Points

Now we examine the topological structure that schemes possess. As we already saw in [§Spectrums](/en/math/scheme_theory/spectrums), a scheme $$X$$ is endowed with a topology different from the topological spaces we usually think of. One of the most peculiar features is that a singleton may not be a closed set.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A point $$x$$ of a topological space $$X$$ is called a *closed point* if $$\{x\}$$ is a closed subset of $$X$$.

</div>

Thus, we know that a space $$X$$ being a $$T_1$$-space is equivalent to every point of $$X$$ being a closed point. ([\[Topology\] §Hausdorff Spaces, ⁋Definition 3](/en/math/topology/Hausdorff_spaces#def3)) In particular, we saw that the spectrum of an integral domain that is not a field has no closed points.

On the other hand, any affine scheme necessarily has a closed point.[^1] This is because if we pick a maximal ideal $$\mathfrak{m}$$ of a ring $$A$$, then $$Z(\mathfrak{m})=\{\mathfrak{m}\}$$, and hence by applying [§Spectrums, ⁋Proposition 14](/en/math/scheme_theory/spectrums#prop14) and [\[Set Theory\] §Filters and Ideals, Galois Correspondence, ⁋Proposition 7](/en/math/set_theory/filter_and_ideal#prop7) we obtain

$$\cl(\{\mathfrak{m}\})=ZI(\{\mathfrak{m}\})=ZIZ(\mathfrak{m})=Z(\mathfrak{m})=\{\mathfrak{m}\}$$.

Similarly, if an arbitrary affine scheme $$\Spec A$$ has a closed point $$\mathfrak{p}$$, then from $$I(\{\mathfrak{p}\})=\mathfrak{p}$$ and [§Spectrums, ⁋Proposition 14](/en/math/scheme_theory/spectrums#prop14) we get

$$Z(\mathfrak{p})=ZI(\{\mathfrak{p}\})=\cl(\{\mathfrak{p}\})=\{\mathfrak{p}\}$$,

so $$\mathfrak{p}$$ must be a maximal ideal.

By definition, if a point $$\mathfrak{p}$$ of $$\Spec A$$ is not a closed point, there exists a point $$\mathfrak{q}\neq \mathfrak{p}$$ of $$\Spec A$$ satisfying $$\mathfrak{q}\in \cl(\{\mathfrak{p}\})$$.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> Let $$x,y$$ be two points of a topological space $$X$$ satisfying $$x\in\cl(\{y\})$$. Then we call $$x$$ a *specialization* of $$y$$, and $$y$$ a *generalization* of $$x$$. If for a closed subset $$C$$ of a topological space $$X$$, the equality $$C=\cl(\{x\})$$ holds, then we call $$x$$ a *generic point* of $$C$$.

</div>

Then by definition, if $$x$$ is a generic point of $$C$$, any open subset $$U$$ always contains $$x$$. Thus, a generic point can be thought of as a point close to every point of $$C$$.

In particular, when $$X$$ is an affine scheme $$\Spec A$$, we verified that any irreducible closed set of $$\Spec A$$ is of the form $$Z(\mathfrak{p})$$ for a suitable prime ideal $$\mathfrak{p}$$ of $$A$$. Then obviously $$\mathfrak{p}\in Z(\mathfrak{p})$$, and since it is obvious that $$\mathfrak{p}$$ is (uniquely) minimal among the prime ideals belonging to $$Z(\mathfrak{p})$$, it becomes the (unique) generic point of $$Z(\mathfrak{p})$$.

To make this more geometric, let $$A=\mathbb{K}[\x_1,\x_2]/(\x_2-\x_1^2)$$. Then in [§Spectrums, ⁋Proposition 9](#prop9) we showed that $$\Spec A$$ is a closed subset of $$\mathbb{A}_\mathbb{K}^2=\Spec \mathbb{K}[\x_1,\x_2]$$. Now we know that the prime ideal $$(\x_2-\x_1^2)\in \Spec \mathbb{K}[\x_1,\x_2]$$ is the generic point of $$\Spec A\cong Z(\x_2-\x_1^2)$$. That is, the generic point can be interpreted as representing the curve $$\x_2-\x_1^2$$ itself.

## Topological Properties of Schemes

A scheme, if we ignore the structure sheaf, is just a topological space, so it can have properties of topological spaces.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> Let a scheme $$(X,\mathscr{O}_X)$$ be given. If $$X$$ is quasi-compact (resp. irreducible, connected) as a topological space, then we call $$X$$ a quasi-compact (resp. irreducible, connected) scheme.

</div>

The corresponding topological definitions for the above can be found in [\[Topology\] §Compact Spaces, ⁋Definition 1](/en/math/topology/compact_spaces#def1), [\[Topology\] §Dimension, ⁋Definition 6](/en/math/topology/dimension#def6), and [\[Topology\] §Connected Spaces, ⁋Definition 1](/en/math/topology/connected_spaces#def1), respectively.[^2] The following are examples and counterexamples for this definition.

<div class="example" markdown="1">

<ins id="ex4">**Example 4**</ins> By [§Spectrums, ⁋Lemma 12](/en/math/scheme_theory/spectrums#lem12), we know that any affine scheme is quasi-compact. As an example of a scheme that is not quasi-compact, there is of course a disjoint union of infinitely many schemes.

</div>

For irreducibility, let us look at the following examples.

<div class="example" markdown="1">

<ins id="ex5">**Example 5**</ins> For any integral domain $$A$$, $$\Spec A$$ is always irreducible. This is because if we consider the generic point $$\{0\}$$, the closed subset containing $$\{0\}$$ must be only $$\Spec A$$ itself, so it is impossible to represent $$\Spec A$$ as a union of two proper closed subsets. Thus, setting $$A=\mathbb{K}[\x_0,\ldots, \x_n]$$, we see that affine $$n$$-space $$\mathbb{A}_\mathbb{K}^n$$ is irreducible. Then projective space $$\mathbb{P}^n_\mathbb{K}$$ has irreducible open subsets $$D_+(\x_i)$$, so by [\[Topology\] §Dimension, ⁋Proposition 8](/en/math/topology/dimension#prop8), $$\mathbb{P}^n_\mathbb{K}$$ is also irreducible.

Conversely, any irreducible closed set $$Z$$ of a scheme $$X$$ always has a generic point $$I(Z)$$. ([§Spectrums, ⁋Proposition 16](/en/math/scheme_theory/spectrums#prop16))

</div>

Since an irreducible space is always connected, the above examples are also examples of connected spaces. The following example provides examples of schemes that are not connected, and schemes that are connected but not irreducible, given as certain *closed subschemes* of the affine plane $$\mathbb{A}^2_\mathbb{K}$$.

We have not yet defined closed subschemes, but at least in [§Spectrums, ⁋Proposition 9](/en/math/scheme_theory/spectrums#prop9) we already saw that for an affine scheme $$\Spec A$$ and any ideal $$\mathfrak{a}$$ of $$A$$, via the canonical morphism $$A \rightarrow A/\mathfrak{a}$$, the spaces $$\Spec A/\mathfrak{a}$$ and $$Z(\mathfrak{a})\subseteq \Spec A$$ are homeomorphic as topological spaces. Since connectedness and irreducibility are both properties of topological spaces, the topological properties of $$\Spec A/\mathfrak{a}$$ can be checked by examining the topological structure of the closed subset $$Z(\mathfrak{a})$$ of $$\Spec A$$. When we call these closed subschemes, the only thing missing is the relationship between the structure sheaf of $$\Spec A/\mathfrak{a}$$ and the structure sheaf of $$\Spec A$$ (restricted to $$Z(\mathfrak{a})$$), which we will revisit in [§Closed Subschemes](/en/math/scheme_theory/closed_subschemes).

<div class="example" markdown="1">

<ins id="ex6">**Example 6**</ins> First, an example of a scheme that is not connected is the closed subscheme of $$\mathbb{A}^2_\mathbb{K}$$

$$\Spec \frac{\mathbb{K}[\x,\y]}{(\x(\x-1))}$$.

That this is not connected can be seen by verifying that it can be written as a disjoint union of two subschemes $$\Spec \mathbb{K}[\x,\y]/(\x)$$ and $$\Spec \mathbb{K}[\x,\y]/(\x-1)$$.

On the other hand, as an example of a scheme that is connected but not irreducible, there is

$$Z(\x\y)=\Spec \frac{\mathbb{K}[\x,\y]}{(\x\y)}$$,

and the irreducible components of this scheme are $$\Spec\mathbb{K}[\x,\y]/(\x)$$ and $$\Spec \mathbb{K}[\x,\y]/(\y)$$.

![counterexamples](/assets/images/Math/Algebraic_Varieties/Properties_of_schemes-1.png){:style="width:20em" class="invert" .align-center}

</div>

Meanwhile, examples of noetherian schemes are obtained by the following proposition.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> For a noetherian ring $$A$$, $$\Spec A$$ is always a noetherian topological space.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Given a chain of closed subsets of $$\Spec A$$

$$Z(\mathfrak{a}_1)\supseteq Z(\mathfrak{a}_2)\supseteq\cdots$$

we obtain a chain of ideals of $$A$$

$$IZ(\mathfrak{a}_1)\subseteq IZ(\mathfrak{a}_2)\supseteq\cdots$$

and this is equal to

$$\sqrt{\mathfrak{a}_1}\subseteq \sqrt{\mathfrak{a}_2}\subseteq\cdots$$.

Now from the assumption that $$A$$ is a noetherian ring, there exists a suitable $$k$$ such that

$$\sqrt{\mathfrak{a}_k}=\sqrt{\mathfrak{a}_{k+1}}=\cdots$$

holds, and hence

$$Z(\sqrt{\mathfrak{a}_k})=Z(\sqrt{\mathfrak{a}_{k+1}})=\cdots$$.

Now from [§Spectrums, ⁋Proposition 5](/en/math/scheme_theory/spectrums#prop5) we obtain the desired result.

</details>

However, the converse does not hold in general.

## Locality

In the next post we will examine the algebraic properties of schemes. The topological properties examined in this post and the algebraic properties to be examined in the next post are, of course, closely related, and looking at them simultaneously deepens our understanding of schemes. We conclude this post by giving definitions that allow us to examine this more closely. In particular, in the remaining part we can give a geometric intuition for the localizations $$A_f$$ and $$A_\mathfrak{p}$$ of a ring $$A$$.

<div class="definition" markdown="1">

<ins id="def8">**Definition 8**</ins> A property $$Q$$ of rings is called *local* if the following two conditions hold.

1. For any ring $$A$$ and $$f\in A$$, if $$A$$ satisfies $$Q$$, then $$A_f$$ also satisfies $$Q$$.
2. Let $$A$$ be any ring and $$f_1,\ldots, f_n\in A$$ satisfy $$A=(f_1,\ldots, f_n)$$. Then if all $$A_{f_i}$$ satisfy $$Q$$, then $$A$$ also satisfies $$Q$$.

</div>

Let us rephrase this in the language of affine schemes. If a ring $$A$$ satisfies a local property $$Q$$,

$$D(f)\cong \Spec A_f$$

so the global sections $$\mathscr{O}_{\Spec A}(D(f))$$ of the principal open set $$D(f)$$ of $$\Spec A$$ also satisfy $$P$$. Conversely, if $$A$$ is generated by $$f_1,\ldots, f_r$$, then from the following formula

$$A=A\setminus \emptyset=A\setminus Z(1)=A\setminus Z\left(\sum_{i=1}^r Z(f_i)\right)=A\setminus\bigcap_{i=1}^r Z(f_i)=\bigcup_{i=1}^rA\setminus Z(f_i)=\bigcup_{i=1}^r D(f_i)$$

we see that the $$D(f_i)$$ cover $$\Spec A$$. For convenience, if the ring $$\mathscr{O}_X(X)$$ of global sections of an affine scheme $$X$$ has property $$Q$$, let us say that $$X$$ has property $$P$$. Then from the above, the two conditions of [Definition 8](#def8) can be translated as follows.

1. If $$\Spec A$$ satisfies $$P$$, then any principal open set $$D(f)$$ also satisfies $$P$$.
2. If an open covering $$D(f_1),\ldots, D(f_r)$$ of $$\Spec A$$ each satisfies $$P$$, then $$\Spec A$$ also satisfies $$P$$.

On the other hand, a general open set $$U$$ of $$\Spec A$$ can be represented as a union of principal open sets ([§Spectrums, ⁋Lemma 11](/en/math/scheme_theory/spectrums#lem11)), and therefore if $$\Spec A$$ satisfies $$P$$, we know that any *affine* open subset $$U$$ of $$\Spec A$$ satisfies $$P$$. From this perspective, a property $$P$$ of schemes satisfying the above two conditions is also called an *affine-local property*.

<div class="definition" markdown="1">

<ins id="def9">**Definition 9**</ins> A property $$P$$ defined for suitable affine subschemes of a scheme $$X$$ is called an *affine-local property* if the following two conditions hold.

1. If $$\Spec A\subseteq X$$ satisfies $$P$$, then for any $$f\in A$$, $$\Spec A_f\subseteq X$$ also satisfies $$P$$.
2. If $$A=(f_1,\ldots, f_r)$$ and all $$\Spec A_{f_i}\subseteq X$$ satisfy $$P$$, then $$\Spec A \subseteq X$$ also satisfies $$P$$.

</div>

On the other hand, since we already saw in [§Schemes, ⁋Example 8](/en/math/scheme_theory/schemes#ex8) that an open subscheme of an affine scheme need not be affine, even if $$P$$ is a local property of rings, a property $$P$$ defined in this way is not a local property in the true sense. To remedy this, we define as follows.

<div class="definition" markdown="1">

<ins id="def10">**Definition 10**</ins> For an affine-local property $$P$$ of schemes, a scheme $$(X, \mathscr{O}_X)$$ is called *locally $$P$$* if for every $$x\in X$$ there exists a suitable open affine neighborhood $$U$$ such that the affine open subscheme $$U$$ of $$X$$ satisfies $$P$$.

</div>

Then in [Lemma 12](#lem12) we show that if a scheme $$X$$ is locally $$P$$, then any open subscheme of $$X$$ is locally $$P$$. First, let us prove the following lemma.

<div class="proposition" markdown="1">

<ins id="lem11">**Lemma 11 (Nike)**</ins> Let a scheme $$X$$ and arbitrary affine open subsets $$U,V$$ be given. Then for any $$x\in U\cap V$$, there exists a suitable $$x\in W\subseteq U\cap V$$ such that $$W$$ is a principal open subset in both $$U$$ and $$V$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

For notation, let $$U=\Spec A$$, $$V=\Spec B$$, and suppose $$x$$ corresponds to prime ideals $$\mathfrak{p}\subset A$$ and $$\mathfrak{q}\subset B$$ in each of them, respectively. Then first, viewing $$U\cap V$$ as an open subset of $$U$$ and applying [§Spectrums, ⁋Lemma 11](/en/math/scheme_theory/spectrums#lem11), we can choose a principal open set $$D(f)$$ of $$U$$ such that

$$\mathfrak{p}\in D(f)\subseteq U\cap V$$.

Here, since $$D(f)\cong \Spec A_f$$, the inclusion $$D(f)\hookrightarrow V$$ is obtained from the ring homomorphism $$i:B \rightarrow A_f$$.

On the other hand, now viewing $$D(f)\cong\Spec A_f$$ as an open subset of $$V$$, there again exists a principal open set $$D(g)$$ of $$V$$ such that

$$\mathfrak{q}\in D(g)\subseteq D(f)\cap V$$.

Now it suffices to verify that the open subscheme $$D(g)$$ of $$\Spec B$$ and the open subscheme $$D(i(g))$$ of $$\Spec A$$ are equal.

</details>

<div class="proposition" markdown="1">

<ins id="lem12">**Lemma 12**</ins> For a scheme $$X$$ and an affine-local property $$P$$ of schemes, the following are all equivalent.

1. $$X$$ is locally $$P$$.
2. For any affine open subset $$U\subseteq X$$ of $$X$$, the open subscheme $$U$$ of $$X$$ satisfies $$P$$.
3. There exists a suitable affine open covering $$\{U_i\}$$ of $$X$$ such that the open subschemes $$U_i$$ of $$X$$ all satisfy $$P$$.
4. There exists a suitable open covering $$\{U_i\}$$ of $$X$$ such that each open subscheme $$(U_i, \mathscr{O}_X\vert_{U_i})$$ is locally $$P$$.

In particular, if $$X$$ is locally $$P$$, then any open subscheme of $$X$$ is locally $$P$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

If the first condition holds, then for each $$x$$ there exists an open affine neighborhood $$U_x$$. Thus $$\{U_x\}_{x\in X}$$ becomes an affine open covering of $$X$$ as required in the third condition. Conversely, given an affine open covering $$\{U_i\}$$ provided by the third condition, whenever a point $$x$$ of $$X$$ is given we can choose a $$U_i$$ satisfying $$x\in U_i$$, and the $$U_i$$ thus obtained becomes an open affine neighborhood of $$x$$ as required in [Definition 9](#def9). Therefore the first and third conditions are equivalent. Also, it is obvious that the second condition implies the first condition.

Now assume that the third condition holds and show that the second condition holds. Suppose an affine open covering $$\{U_i=\Spec A_i\}$$ of $$X$$ satisfying the third condition is given. Then for any affine open subset $$V=\Spec A$$ of $$X$$, since each $$V\cap U_i$$ is also an open subset of $$V$$, by [Lemma 11](#lem11) we can find

$$V=\bigcup_{i\in I} V\cap U_i=\bigcup_{i\in I} \bigcup_{j\in J_i} \Spec (A_i)_{f_j}$$

satisfying this, and knowing that each of the $$\Spec (A_i)_{f_j}$$ can be taken as suitable localizations $$\Spec A_{g_j}$$ of $$\Spec A$$, by using [§Spectrums, ⁋Lemma 12](/en/math/scheme_theory/spectrums#lem12) we may assume that there are only finitely many $$g_j$$. Now from the discussion before [Definition 9](#def9) and the assumption that $$P$$ is local, we know that each $$\Spec (A_i)_{f_j}=\Spec A_{g_j}$$ satisfies $$P$$, and from this we know that $$\Spec A$$ satisfies $$P$$.

From the above we know that the first through third conditions are all equivalent.

Now suppose $$X$$ is locally $$P$$, and let $$U$$ be any open subscheme of $$X$$. Then for any $$x\in U$$, by [§Spectrums, ⁋Lemma 11](/en/math/scheme_theory/spectrums#lem11) we can take an affine open subset $$D(f)$$ of $$X$$ satisfying $$x\in D(f)\subseteq U$$, and now from the second condition we know that $$D(f)$$ is an affine scheme satisfying $$P$$. Therefore the scheme $$U$$ is also locally $$P$$, obtaining the last claim. Finally, that the fourth condition is equivalent to the rest follows by using this claim and simply dropping the affine assumption from the second and third conditions.

</details>

Meanwhile, we showed in [Proposition 7](#prop7) that for a noetherian ring $$A$$, $$\Spec A$$ is a noetherian space. Now let us define what it means for an arbitrary scheme $$X$$ to be noetherian.

<div class="proposition" markdown="1">

<ins id="lem13">**Lemma 13**</ins> That a ring $$A$$ is noetherian is a local property, and therefore defines an affine-local property $$P$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

We must prove the two conditions of [Definition 8](#def8).

The first condition is obtained from [\[Commutative Algebra\] §Localization, ⁋Corollary 9](/en/math/commutative_algebra/localization#cor9), or it suffices to use the first result of [\[Topology\] §Dimension, ⁋Proposition 12](/en/math/topology/dimension#prop13).

Let us look at the second condition. If $$A=(f_1,\ldots, f_r)$$, we know that the $$D(f_i)$$ form an open covering of $$\Spec A$$, and therefore from the fact that $$\mathscr{O}_{\Spec A}$$ satisfies the first condition of [\[Topology\] §Sheaves, ⁋Definition 1](/en/math/topology/sheaves#def1) we obtain the following inclusion

$$A \cong \mathscr{O}_{\Spec A}(\Spec A) \hookrightarrow \prod_{i=1}^r \mathscr{O}_{\Spec A}(D(f_i))\cong\prod_{i=1}^r A_{f_i}$$.

Now if all the $$A_{f_i}$$ are noetherian, then their (finite) product $$\prod A_{f_i}$$ is also noetherian, and therefore since $$A$$ is a subring of a noetherian ring, it is noetherian by [\[Commutative Algebra\] §Basic Notions, ⁋Theorem 3](/en/math/commutative_algebra/basic_notions#thme).

</details>

<div class="definition" markdown="1">

<ins id="def14">**Definition 14**</ins> A scheme $$X$$ is called a *locally noetherian scheme* if there exists an affine open covering $$\{U_i=\Spec A_i\}$$ of $$X$$ such that all $$A_i$$ are noetherian. If $$X$$ is a quasi-compact locally noetherian scheme, we call it a *noetherian scheme*.

</div>

Then if $$A$$ is noetherian, it is obvious from the definition and [§Spectrums, ⁋Lemma 12](/en/math/scheme_theory/spectrums#lem12) that $$\Spec A$$ is a noetherian scheme. Also, just as in [Proposition 7](#prop7), any noetherian scheme is noetherian as a topological space. However, as pointed out after [Proposition 7](#prop7), one should be careful that even if a scheme $$X$$ is noetherian as a topological space, the above condition need not hold.

Finally, we define a notion of locality somewhat different from [Definition 9](#def9), namely the notion of *stalk-local*.

<div class="definition" markdown="1">

<ins id="def15">**Definition 15**</ins> A property $$P$$ of a scheme $$X$$ is called *stalk-local* if for each $$x\in X$$, the ring $$\mathscr{O}_{X,x}$$ satisfies a property $$Q$$ of rings.

</div>

Then the following holds.

<div class="proposition" markdown="1">

<ins id="prop16">**Proposition 16**</ins> For a stalk-local property $$P$$ of a scheme $$X$$, the following are all equivalent.

1. $$X$$ satisfies $$P$$.
2. Any open subscheme of $$X$$ satisfies $$P$$.
3. Any affine open subscheme of $$X$$ satisfies $$P$$.
4. One can choose an affine open cover $$\{U_i\}$$ of $$X$$ such that each open subscheme $$U_i$$ satisfies $$P$$.
5. One can choose an open cover $$\{U_i\}$$ of $$X$$ such that each open subscheme $$U_i$$ satisfies $$P$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, $$2\implies 3\implies 4\implies 5$$ is obvious, so it suffices to show $$5\implies 1$$ and $$1\implies 2$$, and these are obvious from the following isomorphism

$$\mathscr{O}_{X,x}= \varinjlim_{V\ni x} \mathscr{O}_X(U)\cong \varinjlim_{U\supseteq V\ni x}\mathscr{O}(V)=\mathscr{O}_{U, x}$$.

</details>

In particular, any stalk-local property is also an affine-local property. However, this is a proposition that requires some care, because for example if a stalk-local property on $$X$$ is given by

$$\text{$X$ is $P$}\iff \text{$\mathscr{O}_{X,x}$ satisfies $Q$}$$

then it is <em-ko>not</em-ko> that $$\mathscr{O}_X(U)$$ satisfies $$Q$$ for an arbitrary affine open subset $$U$$, but rather that $$\mathscr{O}_{U,x}$$ satisfies property $$Q$$ for any affine open subset $$U$$ and element $$x\in U$$, and therefore the affine open subscheme $$U$$ satisfies property $$P$$.

For example, consider the affine scheme

$$X=\Spec A=\Spec\left(\prod_{i=1}^\infty \mathbb{Z}/2\mathbb{Z}\right)$$.

Any element $$x$$ of $$A$$ satisfies $$x^2=x$$, and therefore so does any element of an arbitrary localization $$A_\mathfrak{p}$$. Now from $$x(1-x)=0$$ holding in $$A_{\mathfrak{p}}$$, we know that either $$x\in \mathfrak{p}A_\mathfrak{p}$$ or $$1-x\in \mathfrak{p}A_\mathfrak{p}$$, and we know that an element not belonging to $$\mathfrak{p}A_\mathfrak{p}$$ is a unit. ([\[Commutative Algebra\] §Localization, ⁋Proposition 2](/en/math/commutative_algebra/localization#prop2)) Therefore $$x=0$$ or $$x=1$$, so the chain of ideals of $$A_\mathfrak{p}$$ is just $$(0)\subseteq (1)=A_\mathfrak{p}$$. From this each $$A_\mathfrak{p}$$ is noetherian, but considering

$$A\times \{0\}\times\{0\}\times\cdots\subseteq A\times A\times\{0\}\subseteq\cdots$$

we see that $$A$$ is not noetherian.

---
**References**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).  

---

[^1]: However, there exist schemes having no closed points.
[^2]: After [§Spectrums, ⁋Lemma 11](/en/math/scheme_theory/spectrums#lem11) we agreed to call a compact topological space (which may not be Hausdorff) *quasi-compact*.
