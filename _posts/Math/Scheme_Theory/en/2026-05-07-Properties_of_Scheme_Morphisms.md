---
title: "Properties of Scheme Morphisms"
description: "This post defines key properties of scheme morphisms and introduces the concepts and basic properties of quasi-compact and quasi-separated morphisms."
excerpt: "Basic properties of scheme morphisms: affine, finite, and finite type"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/properties_of_scheme_morphisms
sidebar: 
    nav: "scheme_theory-en"

date: 2025-02-21
weight: 9
translated_at: 2026-07-14T06:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-07-14T06:30:02+00:00
---
In the previous post, we examined several viewpoints for studying scheme morphisms. In this post, we begin in earnest to define the properties that scheme morphisms may possess. First, we define the following property common to all of them.

::: Definition 1
A property $P$ of scheme morphisms is said to be *local on target* if the following two conditions hold.
1. If a scheme morphism $\varphi:X \rightarrow Y$ satisfies $P$, then for any open subscheme $V$ of $Y$, the scheme morphism $\varphi\vert_{\varphi^{-1}(V)}: \varphi^{-1}(V) \rightarrow V$ also satisfies $P$.
2. If for a scheme morphism $\varphi:X \rightarrow Y$ there exists an open covering $\{V_j\}$ of $Y$ such that every $\varphi\vert_{\varphi^{-1}(V_j)}: \varphi^{-1}(V_j) \rightarrow V_j$ satisfies $P$, then so does $\varphi$.
:::

Schemes are built from affine schemes. If a property $P$ of scheme morphisms is local on target, we may assume the target $Y$ of a scheme morphism $\varphi:X \rightarrow Y$ to be $\Spec B$, and then via the adjunction

$$\Hom_\Sch(X, \Spec B)\cong \Hom_\cRing(B, \Gamma(X, \mathcal{O}_X))$$

we can define the property of a scheme morphism $X \rightarrow \Spec B$ through the property of the ring homomorphism $B \rightarrow \Gamma(X, \mathcal{O}_X)$.

## Quasi-compact and Quasi-separated Morphisms

::: Definition 2
A scheme morphism $\varphi: X \rightarrow Y$ is said to be *quasi-compact* if for any affine open subset $V\subseteq Y$, the preimage $\varphi^{-1}(V)$ is quasi-compact.
:::

::: Proposition 3
A scheme morphism $\varphi: X \rightarrow Y$ is quasi-compact if and only if the preimage of every quasi-compact open subset of $Y$ is quasi-compact.
:::
::: Proof
Since any affine scheme is quasi-compact ([§Spectrums, ⁋Lemma 12](/en/math/scheme_theory/spectrums#lem12)), it is obvious that the given condition implies the condition of [Definition 2](#def2).

Conversely, suppose a quasi-compact morphism $\varphi: X \rightarrow Y$ is given. Now if any quasi-compact open subset $V$ of $Y$ is given, there exists a covering of $V$ by finitely many affine open subsets $\{V_j\}$, and the preimages $\varphi^{-1}(V_j)$ are all quasi-compact. Now

$$\varphi^{-1}(V)=\varphi^{-1}\left(\bigcup_{j\in J} V_j\right)=\bigcup_{j\in J}\varphi^{-1}(V_j)$$

and a finite union of quasi-compact sets is again quasi-compact, so we obtain the desired result.
:::

Then from the equivalence of [Proposition 3](#prop3), we know that the composition of any quasi-compact morphisms is again quasi-compact. Moreover, the following holds.

::: Proposition 4
For a Noetherian scheme $X$, any scheme morphism $\varphi: X \rightarrow Y$ is always quasi-compact.
:::
::: Proof
Suppose any affine open subset $V\subseteq Y$ is given; we must show that $\varphi^{-1}(V)$ is quasi-compact. But by the first result of [\[Topology\] §Dimension, ⁋Proposition 12](/en/math/topology/dimension#prop12) and [\[Topology\] §Dimension, ⁋Proposition 13](/en/math/topology/dimension#prop13), any subspace of a Noetherian topological space is quasi-compact.
:::

Similarly, we define quasi-separated morphisms. For this, we must first define quasi-separated schemes.

::: Definition 5
A scheme $X$ is said to be *quasi-separated* if the intersection of any two quasi-compact open subsets of $X$ is again quasi-compact. A scheme morphism $\varphi: X \rightarrow Y$ is said to be *quasi-separated* if for any affine open set $V\subseteq Y$, the preimage $\varphi^{-1}(V)$ is quasi-separated.
:::

Then the following holds.

::: Proposition 6
A locally Noetherian scheme is always quasi-separated.
:::
::: Proof
Suppose any two affine open subsets $V_1=\Spec B_1, V_2=\Spec B_2$ of a locally Noetherian scheme $X$ are given; we must show that $V_1\cap V_2$ is quasi-compact.

First, since $X$ is locally Noetherian, we can cover $X$ by spectra $\Spec A_i$ of Noetherian rings. Now for each $i$, by [§Topology of Schemes, ⁋Lemma 11](/en/math/scheme_theory/topology_of_schemes#lem11), we can cover $U_i\cap V_1$ by spectra $\Spec (A_i)_g$ of Noetherian rings. Collecting all of these, we can cover $V_1$ by spectra of Noetherian rings, and by [§Spectrums, ⁋Lemma 12](/en/math/scheme_theory/spectrums#lem12), $V_1=\Spec B_1$ is covered by finitely many spectra of Noetherian rings. Therefore, by [§Topology of Schemes, ⁋Lemma 13](/en/math/scheme_theory/topology_of_schemes#lem13), $B_1$ is a Noetherian ring, and thus $V_1=\Spec B_1$ is Noetherian. Again, by the first result of [\[Topology\] §Dimension, ⁋Proposition 12](/en/math/topology/dimension#prop12) and [\[Topology\] §Dimension, ⁋Proposition 13](/en/math/topology/dimension#prop13), any subspace of a Noetherian topological space is quasi-compact, so in particular $V_1\cap V_2$ is also quasi-compact.
:::

Then quasi-compactness and quasi-separatedness not only satisfy the property of [Definition 1](#def1), but as can be checked in the following proposition, they are *affine-local on target*. ([§Topology of Schemes, ⁋Definition 9](/en/math/scheme_theory/topology_of_schemes#def9))

::: Proposition 7
For a scheme morphism $\varphi: X \rightarrow Y$, the following hold.

1. If there exists an affine open covering $\{V_j\}$ of $Y$ such that each $\varphi^{-1}(V_j)$ is quasi-compact, then $\varphi$ is quasi-compact.
2. If there exists an affine open covering $\{V_j\}$ of $Y$ such that each $\varphi^{-1}(V_j)$ is quasi-separated, then $\varphi$ is quasi-separated.
:::
::: Proof
1. Suppose any affine open subset $V$ of $Y$ is given. Then by [§Topology of Schemes, ⁋Lemma 11](/en/math/scheme_theory/topology_of_schemes#lem11), we can cover $V\cap V_j$ by open sets that are principal open sets in both $V$ and $V_j$, and considering this for all $j$ and using the quasi-compactness of $V$, we can choose only finitely many of these. Let this be $V=\bigcup W_l$.
    On the other hand, for each $j$, since $\varphi^{-1}(V_j)$ is quasi-compact, we can cover it by finitely many affine open subsets $U_{jk}$, and now $\varphi^{-1}(W_l)\cap U_{jk}$ is a principal open set of $U_{jk}$ by [§Spectrums, ⁋Proposition 8](/en/math/scheme_theory/spectrums#prop8), so each $\varphi^{-1}(W_l)$ can be expressed as a finite union of affine open sets, and thus $\varphi^{-1}(V)$ can also be expressed as a finite union of affine open sets. Since a finite union of quasi-compact spaces is quasi-compact, we obtain the desired result.
2. This can also be proved in the same manner as the first result, using [§Topology of Schemes, ⁋Lemma 11](/en/math/scheme_theory/topology_of_schemes#lem11) to cover any affine open subset $V=\Spec B$ by principal open subsets whose preimages are quasi-separated.
:::

## Affine Morphisms

From the adjunction

$$\Hom_\Sch(X, \Spec B)\cong\Hom_\cRing (B, \Gamma(X, \mathcal{O}_X))$$

we know that in the special case where $X=\Spec A$,

$$\Hom_\Sch(\Spec A,\Spec B)\cong\Hom_\cRing (B, A)$$

holds. ([§Affine Schemes, ⁋Proposition 11](/en/math/scheme_theory/affine_schemes#prop11)) Therefore, when examining a property of scheme morphisms that is affine-local on target as above, for any affine open subset $V\cong\Spec B$ of $Y$, the preimage $U=\varphi^{-1}(V)$ is also an open subscheme $U\cong \Spec A$ of $X$, and thus $\varphi\vert_U: U \rightarrow V$ becomes a morphism between affine schemes, so it would be desirable to obtain this property from the ring homomorphism

$$(\varphi\vert_U)^\sharp(V): \mathcal{O}_V(V) \rightarrow \mathcal{O}_U(U)$$

However, of course, for an arbitrary scheme morphism $\varphi: X \rightarrow Y$, the preimage of an affine open subset of $Y$ need not be affine. ([§Schemes, ⁋Example 8](/en/math/scheme_theory/schemes#ex8))

::: Definition 8
A scheme morphism $\varphi: X \rightarrow Y$ is said to be *affine* if for any affine open subset $V$ of $Y$, the preimage $\varphi^{-1}(V)$ is an affine open subset of $X$.
:::

Then the composition of affine morphisms being affine is obvious. Moreover, this property also satisfies the property of [Definition 1](#def1), but the proof is somewhat lengthy, so we omit it.

::: Proposition 9
For a scheme morphism $\varphi:X \rightarrow Y$, if there exists an affine open covering $\{V_j\}$ of $Y$ such that each $\varphi^{-1}(V_j)$ is affine, then $\varphi$ is affine.
:::
::: Proof
Let us define the property $P$ for an affine open subset $\Spec B$ of $Y$ as "$\varphi^{-1}(\Spec B)$ is an affine open subset of $X$." Then $\varphi$ being affine means that every affine open subset of $Y$ satisfies $P$, and the given assumption means that some affine open covering of $Y$ satisfies $P$, so by the equivalence between the second and third conditions of [§Topology of Schemes, ⁋Lemma 12](/en/math/scheme_theory/topology_of_schemes#lem12), it suffices to show that $P$ is an affine-local property in the sense of [§Topology of Schemes, ⁋Definition 9](/en/math/scheme_theory/topology_of_schemes#def9). In what follows, we write the component of the sheaf morphism $\varphi^\sharp: \mathcal{O}_Y \rightarrow \varphi_\ast \mathcal{O}_X$ at an open set $V$ as $\varphi^\sharp(V): \mathcal{O}_Y(V) \rightarrow \mathcal{O}_X(\varphi^{-1}(V))$.

First, let us verify the first condition of [§Topology of Schemes, ⁋Definition 9](/en/math/scheme_theory/topology_of_schemes#def9). If $\varphi^{-1}(\Spec B)$ is an affine open subset $\Spec A$, then by [§Affine Schemes, ⁋Proposition 11](/en/math/scheme_theory/affine_schemes#prop11), $\Spec A \rightarrow \Spec B$ is of the form $\Spec\phi$ for some ring homomorphism $\phi: B \rightarrow A$, and from the formula

$$(\Spec\phi)^{-1}(D(f))=D(\phi(f))$$

obtained in the proof of [§Spectrums, ⁋Proposition 8](/en/math/scheme_theory/spectrums#prop8), for any $f\in B$ we have $\varphi^{-1}(\Spec B_f)=D(\phi(f))\cong\Spec A_{\phi(f)}$, so $\Spec B_f$ also satisfies $P$.

Now we must verify the second condition. That is, assuming $B=(f_1,\ldots, f_r)$ and each $U_i=\varphi^{-1}(D(f_i))$ is affine, we must show that $U=\varphi^{-1}(\Spec B)$ is affine. For convenience, let $R=\Gamma(U, \mathcal{O}_X)$ and let the image of $f_i$ under $\varphi^\sharp(\Spec B): B \rightarrow R$ be $g_i\in R$. Also, for $g\in \Gamma(U, \mathcal{O}_X)$, let us write $U_g$ for the set of points $x$ where the stalk of $g$ does not belong to the maximal ideal of $\mathcal{O}_{X,x}$. Then for any affine open subset $\Spec A$ of $U$, it is obvious by definition that $U_g\cap \Spec A=D(g\vert_{\Spec A})$, and in particular $U_g$ is an open set.

We make the following three observations. First, since $B=(f_1,\ldots, f_r)$, we have $\Spec B=\bigcup_{i=1}^rD(f_i)$ and thus $\{U_i\}_{i=1}^r$ is a finite affine open covering of $U$. Moreover, choosing $b_i\in B$ such that $1=\sum_{i=1}^rb_if_i$ and applying $\varphi^\sharp(\Spec B)$, we know that $g_1,\ldots, g_r$ generate the unit ideal of $R$. Second, since $\varphi$ is a morphism of locally ringed spaces, for each $x\in U$ the map $\varphi^\sharp_x:\mathcal{O}_{Y,\varphi(x)} \rightarrow \mathcal{O}_{X,x}$ is a local homomorphism, and thus $\varphi(x)\in D(f_i)$ is equivalent to $x\in U_{g_i}$, so $U_i=U_{g_i}$. Third, letting $U_i\cong \Spec A_i$ and letting $\phi_i$ be the ring homomorphism corresponding to $\Spec A_i \rightarrow \Spec B_{f_i}$, since $D(f_j)\cap D(f_i)$ is a principal open set of $\Spec B_{f_i}$, applying [§Spectrums, ⁋Proposition 8](/en/math/scheme_theory/spectrums#prop8) as above, we know that $U_i\cap U_j$ is a principal open set of $\Spec A_i$, hence in particular affine.

Now for each $i$, we show that the canonical map $R_{g_i} \rightarrow \Gamma(U_{g_i}, \mathcal{O}_X)$ is an isomorphism. The two conditions of [\[Topology\] §Sheaves, ⁋Definition 1](/en/math/topology/sheaves#def1) for the open covering $\{U_j\}_{j=1}^r$ of $U$ are equivalent to the existence of the following exact sequence

$$0 \rightarrow R \rightarrow \bigoplus_{j=1}^r \mathcal{O}_X(U_j) \rightarrow \bigoplus_{j,k=1}^r \mathcal{O}_X(U_j\cap U_k)$$

Here the second map is $(s_j)_j\mapsto (s_j\vert_{U_j\cap U_k}-s_k\vert_{U_j\cap U_k})_{j,k}$. This is an exact sequence of $R$-modules, and since the direct sum is finite, by [\[Commutative Algebra\] §Properties of Localization, ⁋Proposition 2](/en/math/commutative_algebra/properties_of_localization#prop2), localizing at $g_i$ preserves exactness, yielding the following exact sequence

$$0 \rightarrow R_{g_i} \rightarrow \bigoplus_{j=1}^r \mathcal{O}_X(U_j)_{g_i} \rightarrow \bigoplus_{j,k=1}^r \mathcal{O}_X(U_j\cap U_k)_{g_i}$$

(Here the localization of $\mathcal{O}_X(U_j)$ means the localization of the restriction of $g_i$ to $U_j$.) On the other hand, since $U_j$ and $U_j\cap U_k$ are both affine, and for an affine scheme $\Spec A$ and $a\in A$ we have $\mathcal{O}_{\Spec A}(D(a))=A_a$ ([§Schemes, ⁋Lemma 2](/en/math/scheme_theory/schemes#lem2)), from the observed $U_g\cap \Spec A=D(g\vert_{\Spec A})$ above we obtain

$$\mathcal{O}_X(U_j)_{g_i}=\mathcal{O}_X(U_j\cap U_{g_i}),\qquad \mathcal{O}_X(U_j\cap U_k)_{g_i}=\mathcal{O}_X(U_j\cap U_k\cap U_{g_i})$$

But the exact sequence thus obtained is precisely the exact sequence given by the sheaf condition for the open covering $\{U_j\cap U_{g_i}\}_{j=1}^r$ of $U_{g_i}$, so $R_{g_i}$ and $\Gamma(U_{g_i}, \mathcal{O}_X)$ are both the kernel of the same map, and thus the canonical map $R_{g_i} \rightarrow \Gamma(U_{g_i}, \mathcal{O}_X)$ is an isomorphism.

Finally, from the adjunction of [§Affine Schemes, ⁋Theorem 13](/en/math/scheme_theory/affine_schemes#thm13)

$$\Hom_\Sch(U, \Spec R)\cong \Hom_\cRing(R, \Gamma(U, \mathcal{O}_X))$$

consider the scheme morphism $\psi: U \rightarrow \Spec R$ corresponding to $\id_R$. Since $\psi$ is also a morphism of locally ringed spaces, for each $x\in U$ the map $\psi^\sharp_x$ is a local homomorphism, and the composition $R \rightarrow \mathcal{O}_{\Spec R, \psi(x)} \rightarrow \mathcal{O}_{X,x}$ is the canonical map $R=\Gamma(U, \mathcal{O}_X) \rightarrow \mathcal{O}_{X,x}$, so $\psi(x)$ is the preimage of the maximal ideal of $\mathcal{O}_{X,x}$ under this canonical map. Therefore

$$\psi^{-1}(D(g_i))=U_{g_i}=U_i$$

and $\psi\vert_{U_i}: U_i \rightarrow D(g_i)\cong \Spec R_{g_i}$, as a morphism between affine schemes, corresponds to the isomorphism $R_{g_i}\cong \Gamma(U_i, \mathcal{O}_X)$ just obtained, so by [§Affine Schemes, ⁋Proposition 11](/en/math/scheme_theory/affine_schemes#prop11) it is an isomorphism. Now since the $g_i$ generate the unit ideal of $R$, $\{D(g_i)\}$ covers $\Spec R$ and $\{U_i\}$ covers $U$, so $\psi$ is an isomorphism. That is, $U\cong\Spec R$ is affine.
:::

## Finite, Integral, and Finite Type Morphisms

::: Definition 10
A scheme morphism $\varphi:X \rightarrow Y$ is said to be *finite* if $\varphi$ is affine and, for any affine open subset $V$ of $Y$, the ring homomorphism

$$(\varphi\vert_{\varphi^{-1}(V)})^\sharp(V): \mathcal{O}_V(V) \rightarrow \mathcal{O}_{\varphi^{-1}(V)}(\varphi^{-1}(V))$$

is a finite ring homomorphism. ([\[Commutative Algebra\] §Integral Extension, ⁋Definition 3](/en/math/commutative_algebra/integral_extension#def3))
:::

To aid understanding, let us write an affine open subset $V\subseteq Y$ as $\Spec B$. Then from the assumption that $\varphi$ is affine, the preimage $U=\varphi^{-1}(V)$ is an affine open subset of $X$, and thus there exists $A$ such that $U\cong\Spec A$. Through this identification, the scheme morphism $\varphi\vert_U: U \rightarrow V$ is the same as a morphism $\Spec A \rightarrow \Spec B$ between spectra, and now $\varphi$ being finite means that the ring homomorphism $B \rightarrow A$ corresponding to this morphism is finite. Similarly, we define the following.

::: Definition 11
A scheme morphism $\varphi:X \rightarrow Y$ is said to be *integral* if $\varphi$ is affine and, for any affine open subset $V$ of $Y$, the ring homomorphism

$$(\varphi\vert_{\varphi^{-1}(V)})^\sharp(V): \mathcal{O}_V(V) \rightarrow \mathcal{O}_{\varphi^{-1}(V)}(\varphi^{-1}(V))$$

is an integral ring homomorphism. ([\[Commutative Algebra\] §Integral Extension, ⁋Definition 3](/en/math/commutative_algebra/integral_extension#def3))
:::

From their definitions, we know that finite morphisms and integral morphisms are closed under composition. Also, since the fact that they satisfy the conditions of [Definition 1](#def1) follows from [\[Commutative Algebra\] §Integral Extension, ⁋Proposition 14](/en/math/commutative_algebra/integral_extension#prop14) and [\[Commutative Algebra\] §Integral Extension, ⁋Proposition 15](/en/math/commutative_algebra/integral_extension#prop15), they are all affine-local on target.

By [\[Commutative Algebra\] §Integral Extension, ⁋Lemma 4](/en/math/commutative_algebra/integral_extension#lem4), we know that any finite morphism is integral. Now, to completely restate this lemma in the language of algebraic geometry, we must define finite type morphisms.

::: Definition 12
A scheme morphism $\varphi:X \rightarrow Y$ is said to be *locally of finite type* if for any affine open subset $V$ of $Y$ and any affine open subset $U$ of $\varphi^{-1}(V)$,

$$(\varphi\vert_{U})^\sharp(V): \mathcal{O}_V(V) \rightarrow \mathcal{O}_U(U)$$

is of finite type. ([\[Commutative Algebra\] §Integral Extension, ⁋Definition 3](/en/math/commutative_algebra/integral_extension#def3))
:::

As above, let $V\cong \Spec B$ and $U\cong\Spec A\subseteq \varphi^{-1}(V)$. Then the scheme morphism $\varphi\vert_U: U \rightarrow V$ can be viewed as $\Spec A \rightarrow \Spec B$, and we require that the corresponding ring homomorphism $B \rightarrow A$ be of finite type. Then finite type morphisms are defined as follows.

::: Definition 13
A scheme morphism $\varphi:X \rightarrow Y$ is said to be a *morphism of finite type* if $\varphi$ is a quasi-compact morphism locally of finite type.
:::

From the definition, it is clear that morphisms locally of finite type are affine-local on target. Also, since quasi-compact morphisms are affine-local on target by [Proposition 7](#prop7), finite type morphisms are also affine-local on target.

Then by [\[Commutative Algebra\] §Integral Extension, ⁋Lemma 4](/en/math/commutative_algebra/integral_extension#lem4), the following holds.

::: Proposition 14
A scheme morphism $\varphi:X \rightarrow Y$ is finite if and only if it is an integral morphism (locally) of finite type.
:::
::: Proof
One direction is obvious. For the converse, first from the assumption that $\varphi$ is integral, we know that for any affine open subset $V\subseteq Y$, the preimage $\varphi^{-1}(V)$ is an affine open subset of $X$, and applying [\[Commutative Algebra\] §Integral Extension, ⁋Lemma 4](/en/math/commutative_algebra/integral_extension#lem4) to the ring map thus obtained suffices.
:::

In the above proposition, since $\varphi$ is an integral morphism, it is an affine morphism, and thus a quasi-compact morphism ([§Spectrums, ⁋Lemma 12](/en/math/scheme_theory/spectrums#lem12)), so whether $\varphi$ is of finite type or locally of finite type becomes the same assumption.

::: Example 15
Let us look at examples of the morphisms examined in this section. In the world of affine schemes, this is nothing more than looking at the examples of [\[Commutative Algebra\] §Integral Extension, ⁋Definition 3](/en/math/commutative_algebra/integral_extension#def3). The purpose of this example is to give geometric intuition to them.

First, for an algebraically closed field $\mathbb{K}$, considering the ring map $\iota:\mathbb{K}[\x] \rightarrow \mathbb{K}[\x,\y]$, we see that $\mathbb{K}[\x,\y]$ is generated as a $\mathbb{K}[\x]$-algebra by a single element $\y$, so it is a finite type ring homomorphism, but it is not a finite ring homomorphism since it is not finitely generated as a $\mathbb{K}[\x]$-module.

Now consider the corresponding scheme morphism $\Spec\iota: \Spec \mathbb{K}[\x,\y] \rightarrow\Spec \mathbb{K}[\x]$. This is the function that takes any prime ideal $\mathfrak{p}\subset \mathbb{K}[\x,\y]$ and outputs the prime ideal $\mathfrak{p}\cap \mathbb{K}[\x]$ of $\mathbb{K}[\x]$. Geometrically, this is the function that sends a point $(x,y)$ of the affine plane $\mathbb{A}^2_\mathbb{K}$ to the point $x$ of the affine line $\mathbb{A}^1_\mathbb{K}$.

![finite_type_morphism](/assets/images/Math/Scheme_Theory/Properties_of_Scheme_Morphisms-1.svg){:style="width:27.72em" class="invert" .align-center}

As a related example of a finite morphism, there is the composition of the above ring homomorphism $\iota:\mathbb{K}[\x]\rightarrow \mathbb{K}[\x,\y]$ with the projection map $\pi:\mathbb{K}[\x,\y] \rightarrow \mathbb{K}[\x,\y]/(\x-\y^2)$. Then $\mathbb{K}[\x,\y]/(\x-\y^2)$ is generated as a $\mathbb{K}[\x]$-module by $1$ and $\y$, so $\phi:\mathbb{K}[\x] \rightarrow \mathbb{K}[\x,\y]/(\x-\y^2)$ is a finite morphism.

On the other hand, we know that the ring homomorphism $\pi:A \rightarrow A/\mathfrak{a}$ geometrically corresponds to the inclusion of the closed set defined by $\mathfrak{a}$. Therefore, the scheme morphism

$$\Spec\phi: \Spec \frac{\mathbb{K}[\x,\y]}{(\x-\y^2)}\rightarrow \Spec \mathbb{K}[\x,\y] \rightarrow \Spec\mathbb{K}[\x]$$

defined by the composition

$$\phi: \mathbb{K}[\x] \rightarrow \mathbb{K}[\x,\y] \rightarrow \mathbb{K}[\x,y]/(\x-\y^2)$$

can be viewed geometrically as the projection from the zero set $Z(\x-\y^2)$ of $\x=\y^2$ onto the $x$-axis.

![finite_morphism](/assets/images/Math/Scheme_Theory/Properties_of_Scheme_Morphisms-2.svg){:style="width:25.48em" class="invert" .align-center}

The geometric difference between these two examples is quite clear. In the first example, the fiber over a point of the target is an infinite set, whereas in the second example the fiber over a point is a finite set. Algebraically, this can be checked by taking any point $\mathfrak{p}=(\x-a)$ of the target $\mathbb{A}_\mathbb{K}^1$: any $\mathfrak{q}_b=(\x-a, \y-b)\in \mathbb{A}_\mathbb{K}^2$ satisfies $(\Spec\iota)(\mathfrak{q}_b)=\mathfrak{p}$, whereas in the second example only two points $\mathfrak{q}_+=(\x-a, \y-\sqrt{a})$ and $\mathfrak{q}_-=(\x-a, \y+\sqrt{a})$ satisfy $(\Spec\phi)(\mathfrak{q}_\pm)=\mathfrak{p}$.

Thus, geometrically, finite type morphisms are related to fibers being finite-dimensional, and finite morphisms are related to fibers being finite sets.
:::

For now, in situations like the above [Example 15](#ex15), to compute the fiber of a scheme morphism we have no choice but to carry out calculations straightforwardly according to the situation each time, but once we have computed fiber products, we will be able to use a somewhat more standardized method. For that time, we define the following.

::: Definition 16
A scheme morphism $\varphi: X \rightarrow Y$ is said to be *quasi-finite* if $\varphi$ is a morphism of finite type and for any $y\in Y$, the set $\varphi^{-1}(y)$ is always a finite set.
:::

Then the geometric intuition for finite morphisms in [Example 15](#ex15) is always true. That is, any finite morphism is always quasi-finite. It is possible to prove this right now, but we postpone it until after defining fiber products.

Finally, we define the following.

::: Definition 17
A scheme morphism $\varphi: X \rightarrow Y$ is said to be *locally of finite presentation* if whenever any affine open subset $V\cong \Spec B$ of $Y$ is given, there exists a covering $\varphi^{-1}(V)=\bigcup \Spec A_i$ such that all $B \rightarrow A_i$ are finitely presented. If a scheme morphism $\varphi:X \rightarrow Y$ is quasi-compact, quasi-separated, and locally of finite presentation, then $\varphi$ is called a *morphism of finite presentation*.
:::

In most cases, we think of all schemes being locally Noetherian, and in this case by [\[Commutative Algebra\] §Basic Notions, ⁋Proposition 9](/en/math/commutative_algebra/basic_notions#prop9) this notion is nothing new.
