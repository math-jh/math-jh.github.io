---
title: "Properties of Scheme Morphisms"
description: "We define the main properties of scheme morphisms, introduce the notions of quasi-compact and separated morphisms along with their basic properties, and then define rational maps and birational maps."
excerpt: "Basic properties of scheme morphisms: affine, finite, finite type, and rational maps"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/properties_of_scheme_morphisms
sidebar: 
    nav: "scheme_theory-en"

date: 2025-02-21
weight: 9
translated_at: 2026-07-27T13:15:03+00:00
translation_source: kimi-cli
last_polished_at: 2026-07-27T13:15:03+00:00
---
In the previous post, we examined several viewpoints for understanding scheme morphisms. In this post, we define in earnest the properties that scheme morphisms possess. First, we define the following property shared by these morphisms.

::: Definition 1
A property $P$ of scheme morphisms is said to be *local on target* if the following two conditions hold.
1. If a scheme morphism $\varphi:X \rightarrow Y$ satisfies $P$, then for any open subscheme $V$ of $Y$, the scheme morphism $\varphi\vert_{\varphi^{-1}(V)}: \varphi^{-1}(V) \rightarrow V$ also satisfies $P$.
2. If for a scheme morphism $\varphi:X \rightarrow Y$, there exists an open covering $\{V_j\}$ of $Y$ such that each $\varphi\vert_{\varphi^{-1}(V_j)}: \varphi^{-1}(V_j) \rightarrow V_j$ satisfies $P$, then $\varphi$ also satisfies $P$.
:::

Schemes are built from affine schemes. If a property $P$ of scheme morphisms is local on target, then for a scheme morphism $\varphi:X \rightarrow Y$, we may assume the target $Y$ is $\Spec B$, and through the adjunction

$$\Hom_\Sch(X, \Spec B)\cong \Hom_\cRing(B, \Gamma(X, \mathcal{O}_X))$$

we can always reduce to the case where the target is affine.

## Quasi-compact and Quasi-separated Morphisms

::: Definition 2
A scheme morphism $\varphi: X \rightarrow Y$ is called *quasi-compact* if for any affine open subset $V\subseteq Y$, the preimage $\varphi^{-1}(V)$ is quasi-compact.
:::

::: Proposition 3
A scheme morphism $\varphi: X \rightarrow Y$ is quasi-compact if and only if the preimage of any quasi-compact open subset of $Y$ is quasi-compact.
:::
::: Proof
Since any affine scheme is quasi-compact ([§The Spectrum, ⁋Lemma 12](/en/math/scheme_theory/spectrums#lem12)), it is obvious that the given condition implies the condition of [Definition 2](#def2).

Conversely, suppose a quasi-compact morphism $\varphi: X \rightarrow Y$ is given. Now if any quasi-compact open subset $V$ of $Y$ is given, there exists a covering $\{V_j\}$ by finitely many affine open subsets covering $V$, and their preimages $\varphi^{-1}(V_j)$ are all quasi-compact. Now

$$\varphi^{-1}(V)=\varphi^{-1}\left(\bigcup_{j\in J} V_j\right)=\bigcup_{j\in J}\varphi^{-1}(V_j)$$

and since a finite union of quasi-compact sets is again quasi-compact, we obtain the desired result.
:::

Then from the equivalence of [Proposition 3](#prop3), we know that the composition of any quasi-compact morphisms is again quasi-compact. Moreover, the following holds.

::: Proposition 4
For a Noetherian scheme $X$, any scheme morphism $\varphi: X \rightarrow Y$ is always quasi-compact.
:::
::: Proof
Suppose any affine open subset $V\subseteq Y$ is given; we must show that $\varphi^{-1}(V)$ is quasi-compact. However, from the first result of [\[Topology\] §Dimension, ⁋Proposition 12](/en/math/topology/dimension#prop12) and [\[Topology\] §Dimension, ⁋Proposition 13](/en/math/topology/dimension#prop13), any subspace of a Noetherian topological space is quasi-compact.
:::

Similarly, we define quasi-separated morphisms. For this, we must first define quasi-separated schemes.

::: Definition 5
A scheme $X$ is *quasi-separated* if the intersection of any two quasi-compact open subsets of $X$ is again quasi-compact. A scheme morphism $\varphi: X \rightarrow Y$ is *quasi-separated* if for any affine open set $V\subseteq Y$, the preimage $\varphi^{-1}(V)$ is quasi-separated.
:::

Then the following holds.

::: Proposition 6
Any locally Noetherian scheme is quasi-separated.
:::
::: Proof
Suppose any two affine open subsets $V_1=\Spec B_1, V_2=\Spec B_2$ of a locally Noetherian scheme $X$ are given, and we must show that $V_1\cap V_2$ is quasi-compact.

First, since $X$ is locally Noetherian, we can cover $X$ by spectra $U_i=\Spec A_i$ of Noetherian rings. Now for each $i$, by [§The Topological Structure of Schemes, ⁋Lemma 11 (Nike)](/en/math/scheme_theory/topology_of_schemes#lem11), we can cover $U_i\cap V_1$ by spectra $\Spec (A_i)_g$ of Noetherian rings. Collecting all of these, we can cover $V_1$ by spectra of Noetherian rings, and by [§The Spectrum, ⁋Lemma 12](/en/math/scheme_theory/spectrums#lem12), $V_1=\Spec B_1$ is covered by finitely many spectra of Noetherian rings. Therefore, by [§The Topological Structure of Schemes, ⁋Lemma 13](/en/math/scheme_theory/topology_of_schemes#lem13), $B_1$ is a Noetherian ring and thus $V_1=\Spec B_1$ is Noetherian. Again, from the first result of [\[Topology\] §Dimension, ⁋Proposition 12](/en/math/topology/dimension#prop12) and [\[Topology\] §Dimension, ⁋Proposition 13](/en/math/topology/dimension#prop13), any subspace of a Noetherian topological space is quasi-compact, so in particular $V_1\cap V_2$ is also quasi-compact. By the same logic, any affine open of $X$ is Noetherian, and a quasi-compact open is a finite union of affine opens, so it is also Noetherian. Since a subspace of a Noetherian topological space is quasi-compact, the intersection of any two quasi-compact opens is also quasi-compact, and therefore by [Definition 5](#def5), $X$ is quasi-separated.
:::

Then quasi-compactness and quasi-separatedness not only satisfy the property of [Definition 1](#def1), but as we can check in the following proposition, they are *affine-local on target*. ([§The Topological Structure of Schemes, ⁋Definition 9](/en/math/scheme_theory/topology_of_schemes#def9))

::: Proposition 7
For a scheme morphism $\varphi: X \rightarrow Y$, the following hold.

1. If there exists an affine open covering $\{V_j\}$ of $Y$ such that each $\varphi^{-1}(V_j)$ is quasi-compact, then $\varphi$ is quasi-compact.
2. If there exists an affine open covering $\{V_j\}$ of $Y$ such that each $\varphi^{-1}(V_j)$ is quasi-separated, then $\varphi$ is quasi-separated.
:::
::: Proof
1. Suppose any affine open subset $V$ of $Y$ is given. Then by [§The Topological Structure of Schemes, ⁋Lemma 11 (Nike)](/en/math/scheme_theory/topology_of_schemes#lem11), we can cover each $V\cap V_j$ by open subsets that are principal open sets in both $V$ and $V_j$, and considering these for all $j$ and using the quasi-compactness of $V$, we can choose only finitely many of them. Let us write this as $V=\bigcup W_l$.
    On the other hand, for each $j$, since $\varphi^{-1}(V_j)$ is quasi-compact, we can cover it by finitely many affine open subsets $U_{jk}$, and now $\varphi^{-1}(W_l)\cap U_{jk}$ is a principal open set of $U_{jk}$ by [§The Spectrum, ⁋Proposition 8](/en/math/scheme_theory/spectrums#prop8), so we can express each $\varphi^{-1}(W_l)$ as a finite union of affine open sets, and therefore $\varphi^{-1}(V)$ can also be expressed as a finite union of affine open sets. Now since a finite union of quasi-compact spaces is quasi-compact, we obtain the desired result.
2. First, a scheme $Z$ being quasi-separated is equivalent to the intersection of any two affine open subsets of $Z$ being quasi-compact. Since an affine scheme is quasi-compact, one direction is obvious, and conversely, any quasi-compact open subset of $Z$ is a finite union of affine open subsets, so the intersection of two quasi-compact open subsets becomes a union of finitely many affine-affine intersections, which is quasi-compact.
    Now, as in the proof of the first result, choose a finite covering $V=\bigcup_{l=1}^n W_l$ such that each $W_l$ is a principal open subset of $V$ and also of some $V_{j(l)}$. If two affine open subsets $U_1,U_2$ of $\varphi^{-1}(V)$ are given,
    
    $$U_1\cap U_2=\bigcup_{l=1}^n\left(U_1\cap \varphi^{-1}(W_l)\right)\cap\left(U_2\cap \varphi^{-1}(W_l)\right)$$
    
    Here, since $W_l$ is a principal open subset of $V$, $U_1\cap \varphi^{-1}(W_l)$ is the principal open set defined by the pullback of the function defining $W_l$ on the affine scheme $U_1$ ([§The Spectrum, ⁋Proposition 8](/en/math/scheme_theory/spectrums#prop8)), and hence is affine, and similarly for $U_2$. However, these are all affine open subsets of $\varphi^{-1}(W_l)\subseteq \varphi^{-1}(V_{j(l)})$ and $\varphi^{-1}(V_{j(l)})$ is quasi-separated, so by the criterion above, each intersection is quasi-compact. From the above, $U_1\cap U_2$ is a finite union of quasi-compact sets, so it is quasi-compact, and again by the criterion above, $\varphi^{-1}(V)$ is quasi-separated.
:::

## Affine Morphisms

From the adjunction

$$\Hom_\Sch(X, \Spec B)\cong\Hom_\cRing (B, \Gamma(X, \mathcal{O}_X))$$

we know that in the special case $X=\Spec A$,

$$\Hom_\Sch(\Spec A,\Spec B)\cong\Hom_\cRing (B, A)$$

holds. ([§Affine Scheme, ⁋Proposition 11](/en/math/scheme_theory/affine_schemes#prop11)) Therefore, when examining properties of scheme morphisms that are affine-local on target as above, for any affine open subset $V\cong\Spec B$ of $Y$, the preimage $U=\varphi^{-1}(V)$ is also an open subscheme $U\cong \Spec A$ of $X$, and thus it would be desirable if we could obtain the property of $\varphi\vert_U: U \rightarrow V$, which becomes a morphism between affine schemes, from the ring homomorphism

$$(\varphi\vert_U)^\sharp(V): \mathcal{O}_V(V) \rightarrow \mathcal{O}_U(U)$$

However, of course for an arbitrary scheme morphism $\varphi: X \rightarrow Y$, the preimage of an affine open subset of $Y$ need not be affine. ([§Schemes, ⁋Example 8](/en/math/scheme_theory/schemes#ex8))

::: Definition 8
A scheme morphism $\varphi: X \rightarrow Y$ is called *affine* if for any affine open subset $V$ of $Y$, the preimage $\varphi^{-1}(V)$ is an affine open subset of $X$.
:::

Then it is obvious that the composition of affine morphisms is affine. Moreover, this property also satisfies the property of [Definition 1](#def1), and we prove this in the following proposition.

::: Proposition 9
For a scheme morphism $\varphi:X \rightarrow Y$, if there exists an affine open covering $\{V_j\}$ of $Y$ such that each $\varphi^{-1}(V_j)$ is affine, then $\varphi$ is affine.
:::
::: Proof
Define the property $P$ for an affine open subset $\Spec B$ of $Y$ as "$\varphi^{-1}(\Spec B)$ is an affine open subset of $X$." Then $\varphi$ being affine means that any affine open subset of $Y$ satisfies $P$, and the given assumption means that some affine open covering of $Y$ satisfies $P$, so by the equivalence between the second and third conditions of [§The Topological Structure of Schemes, ⁋Lemma 12](/en/math/scheme_theory/topology_of_schemes#lem12), it suffices to show that $P$ is an affine-local property in the sense of [§The Topological Structure of Schemes, ⁋Definition 9](/en/math/scheme_theory/topology_of_schemes#def9). Below, we write the component of the sheaf morphism $\varphi^\sharp: \mathcal{O}_Y \rightarrow \varphi_\ast \mathcal{O}_X$ at an open set $V$ as $\varphi^\sharp(V): \mathcal{O}_Y(V) \rightarrow \mathcal{O}_X(\varphi^{-1}(V))$.

First, let us verify the first condition of [§The Topological Structure of Schemes, ⁋Definition 9](/en/math/scheme_theory/topology_of_schemes#def9). If $\varphi^{-1}(\Spec B)$ is an affine open subset $\Spec A$, then by [§Affine Scheme, ⁋Proposition 11](/en/math/scheme_theory/affine_schemes#prop11), $\Spec A \rightarrow \Spec B$ is of the form $\Spec\phi$ for some ring homomorphism $\phi: B \rightarrow A$, and from the formula

$$(\Spec\phi)^{-1}(D(f))=D(\phi(f))$$

obtained in the proof of [§The Spectrum, ⁋Proposition 8](/en/math/scheme_theory/spectrums#prop8), for any $f\in B$ we have $\varphi^{-1}(\Spec B_f)=D(\phi(f))\cong\Spec A_{\phi(f)}$, so $\Spec B_f$ also satisfies $P$.

Now we must verify the second condition. That is, assuming $B=(f_1,\ldots, f_r)$ and each $U_i=\varphi^{-1}(D(f_i))$ is affine, we must show that $U=\varphi^{-1}(\Spec B)$ is affine. For convenience, let $R=\Gamma(U, \mathcal{O}_X)$ and let $g_i\in R$ be the image of $f_i$ under $\varphi^\sharp(\Spec B): B \rightarrow R$. Also, for $g\in \Gamma(U, \mathcal{O}_X)$, let us write $U_g$ for the set of points $x$ where the stalk of $g$ does *not* belong to the maximal ideal of $\mathcal{O}_{X,x}$. Then for any affine open subset $\Spec A$ of $U$, it is obvious by definition that $U_g\cap \Spec A=D(g\vert_{\Spec A})$, and in particular $U_g$ is an open set.

We observe the following three facts. First, since $B=(f_1,\ldots, f_r)$, we have $\Spec B=\bigcup_{i=1}^rD(f_i)$ and therefore $\{U_i\}_{i=1}^r$ is a finite affine open covering of $U$. Moreover, choosing $b_i\in B$ with $1=\sum_{i=1}^rb_if_i$ and applying $\varphi^\sharp(\Spec B)$, we know that $g_1,\ldots, g_r$ generate the unit ideal of $R$. Second, since $\varphi$ is a morphism of locally ringed spaces, for each $x\in U$ the map $\varphi^\sharp_x:\mathcal{O}_{Y,\varphi(x)} \rightarrow \mathcal{O}_{X,x}$ is a local homomorphism, and therefore $\varphi(x)\in D(f_i)$ is equivalent to $x\in U_{g_i}$, so $U_i=U_{g_i}$. Third, if $U_i\cong \Spec A_i$ and we let $\phi_i$ be the ring homomorphism corresponding to $\Spec A_i \rightarrow \Spec B_{f_i}$, then since $D(f_j)\cap D(f_i)$ is a principal open set of $\Spec B_{f_i}$, applying [§The Spectrum, ⁋Proposition 8](/en/math/scheme_theory/spectrums#prop8) as above, we know that $U_i\cap U_j$ is a principal open set of $\Spec A_i$, hence in particular affine.

Now we show that for each $i$, the canonical map $R_{g_i} \rightarrow \Gamma(U_{g_i}, \mathcal{O}_X)$ is an isomorphism. The two conditions of [\[Topology\] §Sheaves, ⁋Definition 1](/en/math/topology/sheaves#def1) for the open covering $\{U_j\}_{j=1}^r$ of $U$ are equivalent to the existence of the following exact sequence

$$0 \rightarrow R \rightarrow \bigoplus_{j=1}^r \mathcal{O}_X(U_j) \rightarrow \bigoplus_{j,k=1}^r \mathcal{O}_X(U_j\cap U_k)$$

Here, the second map is $(s_j)_j\mapsto (s_j\vert_{U_j\cap U_k}-s_k\vert_{U_j\cap U_k})_{j,k}$. This is an exact sequence of $R$-modules and the direct sum is finite, so by [\[Commutative Algebra\] §Properties of Localization, ⁋Proposition 2](/en/math/commutative_algebra/properties_of_localization#prop2), exactness is preserved upon localizing at $g_i$, yielding the following exact sequence

$$0 \rightarrow R_{g_i} \rightarrow \bigoplus_{j=1}^r \mathcal{O}_X(U_j)_{g_i} \rightarrow \bigoplus_{j,k=1}^r \mathcal{O}_X(U_j\cap U_k)_{g_i}$$

(Here, the localization of $\mathcal{O}_X(U_j)$ means the localization at the restriction of $g_i$ to $U_j$.) On the other hand, since $U_j$ and $U_j\cap U_k$ are both affine and for an affine scheme $\Spec A$ and $a\in A$ we have $\mathcal{O}_{\Spec A}(D(a))=A_a$ ([§Schemes, ⁋Lemma 2](/en/math/scheme_theory/schemes#lem2)), from $U_g\cap \Spec A=D(g\vert_{\Spec A})$ observed above, we obtain

$$\mathcal{O}_X(U_j)_{g_i}=\mathcal{O}_X(U_j\cap U_{g_i}),\qquad \mathcal{O}_X(U_j\cap U_k)_{g_i}=\mathcal{O}_X(U_j\cap U_k\cap U_{g_i})$$

However, the exact sequence thus obtained is precisely the exact sequence given by the sheaf condition for the open covering $\{U_j\cap U_{g_i}\}_{j=1}^r$ of $U_{g_i}$, so $R_{g_i}$ and $\Gamma(U_{g_i}, \mathcal{O}_X)$ both become the kernel of the same map, and therefore the canonical map $R_{g_i} \rightarrow \Gamma(U_{g_i}, \mathcal{O}_X)$ is an isomorphism.

Finally, in the adjunction

$$\Hom_\Sch(U, \Spec R)\cong \Hom_\cRing(R, \Gamma(U, \mathcal{O}_X))$$

of [§Affine Scheme, ⁋Theorem 13](/en/math/scheme_theory/affine_schemes#thm13), consider the scheme morphism $\psi: U \rightarrow \Spec R$ corresponding to $\id_R$. Since $\psi$ is also a morphism of locally ringed spaces, for each $x\in U$ the map $\psi^\sharp_x$ is a local homomorphism, and since the composition $R \rightarrow \mathcal{O}_{\Spec R, \psi(x)} \rightarrow \mathcal{O}_{X,x}$ is the canonical map $R=\Gamma(U, \mathcal{O}_X) \rightarrow \mathcal{O}_{X,x}$, we have that $\psi(x)$ is the preimage of the maximal ideal of $\mathcal{O}_{X,x}$ under this canonical map. Therefore

$$\psi^{-1}(D(g_i))=U_{g_i}=U_i$$

and $\psi\vert_{U_i}: U_i \rightarrow D(g_i)\cong \Spec R_{g_i}$, as a morphism between affine schemes, corresponds to the isomorphism $R_{g_i}\cong \Gamma(U_i, \mathcal{O}_X)$ just obtained, so by [§Affine Scheme, ⁋Proposition 11](/en/math/scheme_theory/affine_schemes#prop11) it is an isomorphism. Now since the $g_i$ generate the unit ideal of $R$, $\{D(g_i)\}$ covers $\Spec R$ and $\{U_i\}$ covers $U$, so $\psi$ is an isomorphism. That is, $U\cong\Spec R$ is affine.
:::

## Finite, Integral, and Finite Type Morphisms

::: Definition 10
A scheme morphism $\varphi:X \rightarrow Y$ is *finite* if $\varphi$ is affine and, for any affine open subset $V$ of $Y$, the ring homomorphism

$$(\varphi\vert_{\varphi^{-1}(V)})^\sharp(V): \mathcal{O}_V(V) \rightarrow \mathcal{O}_{\varphi^{-1}(V)}(\varphi^{-1}(V))$$

is a finite ring homomorphism. ([\[Commutative Algebra\] §Integral Extensions, ⁋Definition 3](/en/math/commutative_algebra/integral_extension#def3))
:::

To aid understanding, let us write an affine open subset $V\subseteq Y$ as $\Spec B$. Then from the assumption that $\varphi$ is affine, $U=\varphi^{-1}(V)$ is an affine open subset of $X$ and thus there exists $A$ such that $U\cong\Spec A$. Through this identification, the scheme morphism $\varphi\vert_U: U \rightarrow V$ is the same as the morphism $\Spec A \rightarrow \Spec B$ between spectra, and now $\varphi$ being finite means that the ring homomorphism $B \rightarrow A$ corresponding to this morphism is finite. Similarly, we define the following.

::: Definition 11
A scheme morphism $\varphi:X \rightarrow Y$ is *integral* if $\varphi$ is affine and, for any affine open subset $V$ of $Y$, the ring homomorphism

$$(\varphi\vert_{\varphi^{-1}(V)})^\sharp(V): \mathcal{O}_V(V) \rightarrow \mathcal{O}_{\varphi^{-1}(V)}(\varphi^{-1}(V))$$

is an integral ring homomorphism. ([\[Commutative Algebra\] §Integral Extensions, ⁋Definition 3](/en/math/commutative_algebra/integral_extension#def3))
:::

From their definitions, we know that finite morphisms and integral morphisms are closed under composition. Also, that they satisfy the condition of [Definition 1](#def1) can be seen from [\[Commutative Algebra\] §Integral Extensions, ⁋Proposition 14](/en/math/commutative_algebra/integral_extension#prop14) and [\[Commutative Algebra\] §Integral Extensions, ⁋Proposition 15](/en/math/commutative_algebra/integral_extension#prop15), so they are all affine-local on target.

We know from [\[Commutative Algebra\] §Integral Extensions, ⁋Lemma 4](/en/math/commutative_algebra/integral_extension#lem4) that any finite morphism is integral. Now, to completely translate this lemma into the language of algebraic geometry, we must define finite type morphisms.

::: Definition 12
A scheme morphism $\varphi:X \rightarrow Y$ is *locally of finite type* if for any affine open subset $V$ of $Y$ and any affine open subset $U$ of $\varphi^{-1}(V)$,

$$(\varphi\vert_{U})^\sharp(V): \mathcal{O}_V(V) \rightarrow \mathcal{O}_U(U)$$

is of finite type. ([\[Commutative Algebra\] §Integral Extensions, ⁋Definition 3](/en/math/commutative_algebra/integral_extension#def3))
:::

Similarly as above, let $V\cong \Spec B$ and $U\cong\Spec A\subseteq \varphi^{-1}(V)$. Then we can view the scheme morphism $\varphi\vert_U: U \rightarrow V$ as $\Spec A \rightarrow \Spec B$, and what we require is that the corresponding ring homomorphism $B \rightarrow A$ is of finite type.

[Definition 12](#def12) quantifies over *all* affine open subsets of $\varphi^{-1}(V)$, so to verify this, we must separately show that it suffices to check on a single affine open covering. This is the content of the following lemma.

::: Lemma 13
Suppose a scheme morphism $\varphi: W \rightarrow \Spec B$ is given, and there exists an affine open covering $\{\Spec A_i\}$ of $W$ such that each $B \rightarrow A_i$ is of finite type. Then for *any* affine open subset $U$ of $W$, $B \rightarrow \mathcal{O}_W(U)$ is also of finite type.
:::
::: Proof
Define the property $Q$ for an affine open subset $\Spec R$ of $W$ as

> $B \rightarrow R$ is of finite type.

and let us show that $Q$ is an affine-local property in the sense of [§The Topological Structure of Schemes, ⁋Definition 9](/en/math/scheme_theory/topology_of_schemes#def9). Then since the given covering $\{\Spec A_i\}$ satisfies $Q$, we obtain the desired result from the second condition of [§The Topological Structure of Schemes, ⁋Lemma 12](/en/math/scheme_theory/topology_of_schemes#lem12).

The first condition is obvious: if $B \rightarrow R$ is of finite type, then adding $1/h$ to the generators of $R$ makes $R_h$ finitely generated as a $B$-algebra. For the second condition, suppose $R=(h_1,\ldots, h_m)$ and each $B \rightarrow R_{h_t}$ is of finite type. For each $t$, choose a finite set generating $R_{h_t}$ as a $B$-algebra and then clear denominators; there exist elements $x_{t1},\ldots, x_{tn_t}$ of $R$ such that $R_{h_t}$ is generated as a $B$-algebra by the $x_{tk}/1$ and $1/h_t$. Also choose $a_t\in R$ with $1=\sum_{t=1}^ma_th_t$. Now let $R'$ be the $B$-subalgebra of $R$ generated by the finite set $\{h_t\}\cup\{a_t\}\cup\{x_{tk}\}$; then $R'$ is a finite type $B$-algebra, so it suffices to show $R'=R$. For any $x\in R$, in $R_{h_t}$ the element $x/1$ is a polynomial in the $x_{tk}/1$ and $1/h_t$ with coefficients in $B$, so for suitable $r_t\in R'$ and $n_t\geq 0$ we have $x/1=r_t/h_t^{n_t}$, and therefore for suitable $N_t$ we have $h_t^{N_t}(h_t^{n_t}x-r_t)=0$ in $R$, that is, $h_t^{N_t+n_t}x=h_t^{N_t}r_t\in R'$. Since there are finitely many $t$, we can choose a common $M$ such that $h_t^Mx\in R'$ for all $t$. On the other hand, from $1=\sum_ta_th_t$ with $a_t,h_t\in R'$, we know that $h_1,\ldots, h_m$ generate the unit ideal of $R'$, and raising both sides of this equation to a sufficiently high power, we know that $h_1^M,\ldots, h_m^M$ also generate the unit ideal of $R'$. That is, there exist $c_t\in R'$ with $1=\sum_tc_th_t^M$, and therefore

$$x=\sum_{t=1}^mc_t(h_t^Mx)\in R'$$

.
:::

Then finite type morphisms are defined as follows.

::: Definition 14
A scheme morphism $\varphi:X \rightarrow Y$ is a *morphism of finite type* if $\varphi$ is a quasi-compact morphism locally of finite type.
:::

From the definition, it is clear that a morphism locally of finite type is affine-local on target. Also, since quasi-compact morphisms are affine-local on target by [Proposition 7](#prop7), finite type morphisms are also affine-local on target.

Then by [\[Commutative Algebra\] §Integral Extensions, ⁋Lemma 4](/en/math/commutative_algebra/integral_extension#lem4), the following holds.

::: Proposition 15
A scheme morphism $\varphi:X \rightarrow Y$ is finite if and only if $\varphi$ is an integral morphism (locally) of finite type.
:::
::: Proof
First, suppose $\varphi$ is finite. For any affine open subset $V=\Spec B\subseteq Y$, we have $\varphi^{-1}(V)=\Spec A$ and $B \rightarrow A$ is finite, so by [\[Commutative Algebra\] §Integral Extensions, ⁋Lemma 4](/en/math/commutative_algebra/integral_extension#lem4), this is integral and in particular of finite type. That is, $\varphi$ is integral, and taking $\{\varphi^{-1}(V)\}$ itself as an affine open covering and applying [Lemma 13](#lem13), we have that for *all* affine open subsets $U$ of $\varphi^{-1}(V)$, $B \rightarrow \mathcal{O}_X(U)$ is of finite type, so $\varphi$ is locally of finite type. For the converse direction, first from the assumption that $\varphi$ is integral, we know that for any affine open subset $V\subseteq Y$, the preimage $\varphi^{-1}(V)$ is an affine open subset of $X$, and applying [\[Commutative Algebra\] §Integral Extensions, ⁋Lemma 4](/en/math/commutative_algebra/integral_extension#lem4) to the ring map thus obtained completes the proof.
:::

In the above proposition, since $\varphi$ is an integral morphism, it is an affine morphism, and therefore a quasi-compact morphism ([§The Spectrum, ⁋Lemma 12](/en/math/scheme_theory/spectrums#lem12)), so whether $\varphi$ is of finite type or locally of finite type becomes the same assumption.

::: Example 16
Let us look at examples of the morphisms examined in this section. In the world of affine schemes, this is nothing more than looking at the examples of [\[Commutative Algebra\] §Integral Extensions, ⁋Definition 3](/en/math/commutative_algebra/integral_extension#def3). The purpose of this example is to give geometric intuition for these.

First, for an algebraically closed field $\mathbb{K}$, considering the ring map $\iota:\mathbb{K}[\x] \rightarrow \mathbb{K}[\x,\y]$, we see that $\mathbb{K}[\x,\y]$ is generated as a $\mathbb{K}[\x]$-algebra by the single element $\y$, so it is a finite type ring homomorphism, but it is not a finite ring homomorphism since it is not finitely generated as a $\mathbb{K}[\x]$-module.

Now consider the corresponding scheme morphism $\Spec\iota: \Spec \mathbb{K}[\x,\y] \rightarrow\Spec \mathbb{K}[\x]$. This is the function that takes any prime ideal $\mathfrak{p}\subseteq \mathbb{K}[\x,\y]$ and outputs the prime ideal $\mathfrak{p}\cap \mathbb{K}[\x]$ of $\mathbb{K}[\x]$. Geometrically, this is the function that corresponds a point $(x,y)$ of the affine plane $\mathbb{A}^2_\mathbb{K}$ to the point $x$ of the affine line $\mathbb{A}^1_\mathbb{K}$.

{% diagram Math/Scheme_Theory/Properties_of_Scheme_Morphisms-1.svg width="28.04em" alt="finite_type_morphism" %}

As a related example of a finite morphism, there is the composition of the above ring homomorphism $\iota:\mathbb{K}[\x]\rightarrow \mathbb{K}[\x,\y]$ with the projection map $\pi:\mathbb{K}[\x,\y] \rightarrow \mathbb{K}[\x,\y]/(\x-\y^2)$. Then $\mathbb{K}[\x,\y]/(\x-\y^2)$ is generated as a $\mathbb{K}[\x]$-module by $1$ and $\y$, so $\phi:\mathbb{K}[\x] \rightarrow \mathbb{K}[\x,\y]/(\x-\y^2)$ is a finite morphism.

On the other hand, we know that the ring homomorphism $\pi:A \rightarrow A/\mathfrak{a}$ corresponds geometrically to the inclusion of the closed subset defined by $\mathfrak{a}$. Therefore, the scheme morphism

$$\Spec\phi: \Spec \frac{\mathbb{K}[\x,\y]}{(\x-\y^2)}\rightarrow \Spec \mathbb{K}[\x,\y] \rightarrow \Spec\mathbb{K}[\x]$$

defined by the composition

$$\phi: \mathbb{K}[\x] \rightarrow \mathbb{K}[\x,\y] \rightarrow \mathbb{K}[\x,\y]/(\x-\y^2)$$

can be viewed geometrically as the projection from the zero set $Z(\x-\y^2)$ of $\x=\y^2$ to the $x$-axis.

{% diagram Math/Scheme_Theory/Properties_of_Scheme_Morphisms-2.svg width="25.72em" alt="finite_morphism" %}

The geometric difference between these two examples is quite clear. In the first example, the fiber over a point of the target is an infinite set, whereas in the second example the fiber over a point is a finite set. Algebraically, this is because when we take any point $\mathfrak{p}=(\x-a)$ of the target $\mathbb{A}_\mathbb{K}^1$, any $\mathfrak{q}_b=(\x-a, \y-b)\in \mathbb{A}_\mathbb{K}^2$ satisfies $(\Spec\iota)(\mathfrak{q}_b)=\mathfrak{p}$, whereas in the second example, since $\y^2=\x$ must hold, only $b$ with $b^2=a$ is possible, and therefore the points satisfying $(\Spec\phi)(\mathfrak{q})=\mathfrak{p}$ are at most two, namely $\mathfrak{q}_+=(\x-a, \y-\sqrt{a})$ and $\mathfrak{q}_-=(\x-a, \y+\sqrt{a})$. These become two distinct points when $\operatorname{char}\mathbb{K}\neq 2$ and $a\neq 0$; when $a=0$ the two points collapse into one, and when $\operatorname{char}\mathbb{K}=2$ we have $\y^2-a=(\y-\sqrt{a})^2$, so for all $a$ the fiber is a single point.

Thus, finite type morphisms are geometrically related to fibers being finite-dimensional, and finite morphisms are related to fibers being finite sets.
:::

For now, in situations like [Example 16](#ex16) above, to compute the fiber of a scheme morphism we have no choice but to carry out straightforward calculations case by case, but once we have computed fiber products, we will be able to use a somewhat more standardized method. For that time, we define the following.

::: Definition 17
A scheme morphism $\varphi: X \rightarrow Y$ is *quasi-finite* if $\varphi$ is a morphism of finite type and for any $y\in Y$, the set $\varphi^{-1}(y)$ is always a finite set.
:::

Then the geometric intuition for finite morphisms in [Example 16](#ex16) is always true. That is, any finite morphism is always quasi-finite. It is possible to prove this right now, but we postpone it until after defining fiber products.

Finally, we define the following.

::: Definition 18
A scheme morphism $\varphi: X \rightarrow Y$ is *locally of finite presentation* if whenever an affine open subset $V\cong \Spec B$ of $Y$ is given, there exists a covering $\varphi^{-1}(V)=\bigcup \Spec A_i$ such that all $B \rightarrow A_i$ are finitely presented. If a scheme morphism $\varphi:X \rightarrow Y$ is quasi-compact, quasi-separated, and locally of finite presentation, then $\varphi$ is called a *morphism of finite presentation*.
:::

In most cases, we consider the case where all schemes are locally Noetherian, and in this case this concept is not new. Indeed, if $B$ is a Noetherian ring and $B \rightarrow A$ is of finite type, then we can write $A\cong B[\x_1,\ldots, \x_n]/\mathfrak{a}$, and by [\[Commutative Algebra\] §Basic Notions, ⁋Theorem 12](/en/math/commutative_algebra/basic_notions#thm12), $B[\x_1,\ldots, \x_n]$ is Noetherian, so $\mathfrak{a}$ is finitely generated and therefore $B \rightarrow A$ is finitely presented. Also, a locally Noetherian scheme is quasi-separated ([Proposition 6](#prop6)), so the difference between requiring a morphism of finite presentation and requiring a morphism of finite type also disappears.

## Rational Maps

In [§Algebraic Structure of Schemes, ⁋Definition 12](/en/math/scheme_theory/algebra_of_schemes#def12), we defined a rational function on a scheme $X$ as an equivalence class of pairs consisting of a domain $U$ and a function $f\in \Gamma(U, \mathcal{O}_X)$ on it. On the other hand, viewing $U$ itself as a locally ringed space, by the adjunction of [§Affine Scheme, ⁋Theorem 13](/en/math/scheme_theory/affine_schemes#thm13) we obtain

$$\Hom_\LRS(U, \Spec \mathbb{Z}[\x])\cong \Hom_{\cRing}(\mathbb{Z}[\x], \Gamma(U,\mathcal{O}_X))$$

and here, since a ring homomorphism $\mathbb{Z}[\x]\rightarrow \Gamma(U, \mathcal{O}_X)$ on the right-hand side is completely determined by the image of $\x$, we can connect the right-hand side with the additional isomorphism

$$\Hom_{\cRing}(\mathbb{Z}[\x], \Gamma(U,\mathcal{O}_X))\cong \Gamma(U, \mathcal{O}_X)$$

That is, giving a function $f$ on $U$ is the same data as giving a scheme morphism $U \rightarrow \Spec \mathbb{Z}[\x]=\mathbb{A}^1_\mathbb{Z}$.

On the other hand, since we can now define scheme morphisms, we can also choose the base scheme to be a general $\Spec A$ instead of $\Spec \mathbb{Z}$, so repeating this argument, we can think of rational functions as morphisms defined on $U$ with target $\Spec A[\x]$. To write this precisely, we must determine which open sets to allow as domains, and when to regard two morphisms on different domains as the same. First, we give a name to morphisms whose image is not contained in a small closed subset of the target.

::: Definition 19
A scheme morphism $\varphi: X \rightarrow Y$ is *dominant* if the image of $\varphi$ is dense in $Y$, that is, if $\cl(\varphi(X))=Y$.
:::

A surjective morphism is always dominant, but the converse does not hold. For example, for an integral domain $A$, the image of $\Spec \Frac A \rightarrow \Spec A$ consists only of the generic point $(0)$, but as examined right after [§The Spectrum, ⁋Definition 7](/en/math/scheme_theory/spectrums#def7), the only closed subset of $\Spec A$ containing $(0)$ is $\Spec A$ itself, so this morphism is dominant. Between affine schemes, dominance is read purely algebraically as follows.

::: Proposition 20
For a ring homomorphism $\phi: B \rightarrow A$ and the corresponding scheme morphism $\varphi=\Spec \phi:\Spec A \rightarrow \Spec B$, the following formula holds:

$$\cl\left(\varphi(\Spec A)\right)=Z(\ker\phi)$$

Therefore, $\varphi$ being dominant is equivalent to $\ker\phi\subseteq \mathfrak{N}(B)$.
:::
::: Proof
By the second result of [§The Spectrum, ⁋Proposition 14](/en/math/scheme_theory/spectrums#prop14), for any $T\subseteq \Spec B$ we have $\cl(T)=Z(I(T))$, so for $T=\varphi(\Spec A)$ it suffices to compute $I(T)$. Since the elements of $T$ are exactly of the form $\phi^{-1}(\mathfrak{q})$, we obtain the following formula

$$I(T)=\bigcap_{\mathfrak{q}\in \Spec A}\phi^{-1}(\mathfrak{q})=\phi^{-1}\left(\bigcap_{\mathfrak{q}\in \Spec A}\mathfrak{q}\right)$$

On the other hand, applying the first result of [§The Spectrum, ⁋Proposition 14](/en/math/scheme_theory/spectrums#prop14) to $S=\{0\}$, we know that the intersection of all prime ideals of $A$ is $\sqrt{(0)}=\mathfrak{N}(A)$, and for any $b\in B$, $\phi(b)$ being nilpotent is equivalent to the existence of $n$ with $b^n\in\ker\phi$, so

$$I(T)=\phi^{-1}(\mathfrak{N}(A))=\sqrt{\ker\phi}$$

Now applying the first result of [§The Spectrum, ⁋Proposition 14](/en/math/scheme_theory/spectrums#prop14) again to the identity $Z(I(Z(S)))=Z(S)$, we have $Z(\sqrt{\ker\phi})=Z(\ker\phi)$, so we obtain the desired formula.

The final claim holds because $Z(\ker\phi)=\Spec B$ is equivalent to $\ker\phi$ being contained in every prime ideal of $B$, which is, for the same reason as above, equivalent to $\ker\phi\subseteq \mathfrak{N}(B)$.
:::

In particular, if $B$ is a reduced ring, then $\Spec\phi$ being dominant is the same as $\phi$ being injective. For example, the $\iota: \mathbb{K}[\x] \rightarrow \mathbb{K}[\x,\y]$ seen in [Example 16](#ex16) is injective, so $\Spec\iota$ is dominant, and the morphism $\Spec B/\mathfrak{a} \rightarrow \Spec B$ defined by the quotient map for an ideal $\mathfrak{a}\subseteq B$ is dominant if and only if $\mathfrak{a}\subseteq \mathfrak{N}(B)$, that is, the closed subset defined by $\mathfrak{a}$ is all of $\Spec B$.

Now we determine the open sets to be used as domains. As in the case of rational functions, the domain must be sufficiently large within $X$, and the topological expression of this is the dense condition. As can be guessed from the above argument, in a reduced scheme this condition alone preserves the information of the function.

::: Lemma 21
For a reduced scheme $X$ and a dense open subset $U$, the restriction map $\Gamma(X, \mathcal{O}_X) \rightarrow \Gamma(U, \mathcal{O}_X)$ is injective.
:::
::: Proof
Suppose $s\in \Gamma(X, \mathcal{O}_X)$ satisfies $s\vert_U=0$, choose any affine open subset $\Spec A$ of $X$, and for convenience write the restriction of $s$ to $\Spec A$ again as $s\in A$. Then since $X$ is reduced, $A$ is a reduced ring ([§Algebraic Structure of Schemes, ⁋Definition 1](/en/math/scheme_theory/algebra_of_schemes#def1)), and any non-empty open subset of $\Spec A$ is also an open subset of $X$ and hence meets $U$, so $U\cap \Spec A$ is dense in $\Spec A$.

Now for any $\mathfrak{p}\in U\cap \Spec A$, since the germ of $s$ at the stalk $\mathcal{O}_{X,\mathfrak{p}}=A_\mathfrak{p}$ is $0$, there exists $t\in A\setminus \mathfrak{p}$ with $ts=0$, and since $\mathfrak{p}$ is a prime ideal, from this we obtain $s\in \mathfrak{p}$. That is, $U\cap \Spec A\subseteq Z(s)$, but since $Z(s)$ is closed and $U\cap \Spec A$ is dense, we have $Z(s)=\Spec A$, that is, $s$ belongs to every prime ideal of $A$. Therefore by the first result of [§The Spectrum, ⁋Proposition 14](/en/math/scheme_theory/spectrums#prop14), $s\in \mathfrak{N}(A)=0$. Since this holds for any affine open subset of $X$, we have $s=0$.
:::

The reduced assumption in this lemma cannot be removed. In the case of $X=\Spec \mathbb{K}[\x_1,\x_2]/(\x_2^2,\x_1\x_2)$ from [§Algebraic Structure of Schemes, ⁋Example 11](/en/math/scheme_theory/algebra_of_schemes#ex11), the nilradical is the prime ideal $(\x_2)$, so $X$ is irreducible ([§Algebraic Structure of Schemes, ⁋Lemma 3](/en/math/scheme_theory/algebra_of_schemes#lem3)), and therefore the non-empty open subset $D(\x_1)$ is dense. However, from $\x_1\x_2=0$, making $\x_1$ invertible gives $\x_2\vert_{D(\x_1)}=0$, so a non-zero function vanishes on a dense open subset. That [§Algebraic Structure of Schemes, ⁋Definition 12](/en/math/scheme_theory/algebra_of_schemes#def12) required the domain of a rational function to contain *all* associated points was precisely to prevent this.

On the other hand, there are largely two possible conditions that the domain $U$ of a rational map can satisfy. One is to take $U$ as a dense open subset, as in classical algebraic geometry ([\[Algebraic Varieties\] §Rational Maps, ⁋Definition 5](/en/math/algebraic_varieties/rational_maps#def5)), and the other is to view the rational map as a generalization of [§Algebraic Structure of Schemes, ⁋Definition 12](/en/math/scheme_theory/algebra_of_schemes#def12) and impose the condition that it contains all associated points. As examined above, for non-reduced schemes, requiring a dense open subset is generally a weaker condition than requiring all associated points to be contained, but for locally Noetherian reduced schemes, these two conditions coincide. To verify this, first show that any irreducible component $C$ of $X$ has a generic point (apply [§The Spectrum, ⁋Proposition 16](/en/math/scheme_theory/spectrums#prop16) to an affine open subset $\Spec A$ meeting $C$ and take the closure of the obtained point in $X$), and from this deduce that an open subset of $X$ being dense is equivalent to it containing the generic point of every irreducible component of $X$. Then for a reduced ring $A$, the associated points of $\Spec A$ are always minimal prime ideals, that is, generic points of irreducible components, and conversely, from [§Algebraic Structure of Schemes, §§Associated Primes](/en/math/scheme_theory/algebra_of_schemes#associated-primes) we have already verified that minimal prime ideals of a Noetherian ring are always associated prime ideals, so these two conditions coincide.

::: Definition 22
A *rational map* from a scheme $X$ to a scheme $Y$ is an equivalence class of pairs $(U,\alpha)$ consisting of an open subset $U$ dense in $X$ and a scheme morphism $\alpha: U \rightarrow Y$. Here, two pairs $(U,\alpha)$ and $(V,\beta)$ are equivalent if there exists an open subset $W$ contained in $U\cap V$ and dense in $X$ such that $\alpha\vert_W=\beta\vert_W$.
:::

A rational map is written with a dashed arrow as $\varphi: X \dashrightarrow Y$, where the dashed line indicates that $\varphi$ may not be defined at every point of $X$. That the above definition is actually an equivalence relation is because the intersection of two dense open subsets is again a dense open subset; this is a weaker condition than the classical requirement that two representatives agree on all of $U\cap V$ ([\[Algebraic Varieties\] §Rational Maps, ⁋Definition 5](/en/math/algebraic_varieties/rational_maps#def5)), but when $X$ is reduced and $Y=\Spec B$ is affine, the two become the same. This is because the two morphisms $\alpha,\beta: U\cap V \rightarrow Y$ correspond by [§Affine Scheme, ⁋Theorem 13](/en/math/scheme_theory/affine_schemes#thm13) to a ring homomorphism $B \rightarrow \Gamma(U\cap V, \mathcal{O}_X)$, and since $U\cap V$ is a reduced scheme and $W$ is dense in it, $\Gamma(U\cap V, \mathcal{O}_X) \rightarrow \Gamma(W, \mathcal{O}_X)$ is injective by [Lemma 21](#lem21).

A rational map $\varphi: X \dashrightarrow Y$ is said to be *dominant* if its representative $(U,\alpha)$ is a dominant morphism in the sense of [Definition 19](#def19). This does not depend on the choice of representative, because if $W\subseteq U$ is an open subset dense in $X$, then $W$ is also dense in $U$ and since $\alpha$ is continuous, $\cl(\alpha(U))=\cl(\alpha(W))$ holds. The reason dominant rational maps are important is revealed when composing two rational maps. Let $(U,\alpha)$ and $(V,\beta)$ be representatives of two rational maps $\varphi: X\dashrightarrow Y$ and $\psi: Y \dashrightarrow Z$. Then the actual domain of the composition $\beta\circ \alpha$ is the part $\alpha^{-1}(V)$ where $\alpha$ lands inside the domain of the later function, so for this function to define a rational map, $\alpha^{-1}(V)$ must be dense in $X$. Then the condition we can naturally require is the dominance of $\alpha$, and requiring this ensures that $\alpha(U)$ must meet $V$, so $\alpha^{-1}(V)$ does not become empty. However, in the world of schemes this condition is also somewhat insufficient. For example, let $X$ be the disjoint union of $\mathbb{A}^1_\mathbb{K}$ and $\Spec\mathbb{K}$, let $Y=\mathbb{A}^1_\mathbb{K}$, and let $\alpha$ be the morphism that is the identity on the first component and sends the second component to a closed point $p$; then $\alpha$ is dominant, but for $V=Y\setminus \{p\}$, the set $\alpha^{-1}(V)$ is only $\mathbb{A}^1_\mathbb{K}\setminus\{p\}$ of the first component, which does not meet the second component, a non-empty open subset of $X$. This is a problem arising from $X$ being split into several pieces, and if $X$ is irreducible, then every non-empty open subset is dense, so this problem disappears. Also, we have already examined in the counterexample right after [Lemma 21](#lem21) that $X$ being reduced is necessary, so for convenience we shall consider the case where both $X,Y$ are integral schemes. ([§Algebraic Structure of Schemes, ⁋Proposition 4](/en/math/scheme_theory/algebra_of_schemes#prop4)) Then in this case, the composition $\psi\circ\varphi$ of a dominant rational map $\varphi: X\dashrightarrow Y$ and any rational map $\psi: Y \dashrightarrow Z$ is well defined by the representative $(\alpha^{-1}(V), \beta\circ \alpha)$, and it is not difficult to show that this does not depend on the choice of representative.

::: Definition 23
A dominant rational map $\varphi: X \dashrightarrow Y$ between integral schemes $X, Y$ is a *birational map* if there exists a dominant rational map $\psi: Y \dashrightarrow X$ such that $\psi\circ\varphi$ and $\varphi\circ\psi$ are the same as the rational maps defined by $\id_X$ and $\id_Y$ respectively. Two integral schemes $X, Y$ are *birationally equivalent* if there exists such a birational map $\varphi: X\dashrightarrow Y$.
:::

If an isomorphism means that two schemes have exactly the same structure, then birational equivalence means that two schemes have the same structure on dense open subsets. The following proposition expresses this precisely.

::: Proposition 24
For a dominant rational map $\varphi: X \dashrightarrow Y$ between integral schemes $X, Y$, the following two conditions are equivalent.

1. $\varphi$ is a birational map.
2. There exist a non-empty open subset $\widetilde U$ of $X$ and a non-empty open subset $\widetilde V$ of $Y$ such that an isomorphism $\widetilde U \rightarrow \widetilde V$ is a representative of $\varphi$.
:::
::: Proof
First, suppose $\varphi$ is a birational map, and choose a representative $(U,\alpha)$ of $\varphi$ and a representative $(V,\beta)$ of $\psi$ playing the inverse role. Then from $\psi\circ\varphi=\id_X$, there exists a non-empty open subset $W_1\subseteq \alpha^{-1}(V)$ of $X$ such that $(\beta\circ \alpha)\vert_{W_1}=\id_{W_1}$, and from $\varphi\circ\psi=\id_Y$, there exists a non-empty open subset $W_2\subseteq \beta^{-1}(U)$ of $Y$ such that $(\alpha\circ \beta)\vert_{W_2}=\id_{W_2}$. Now let

$$\widetilde U=W_1\cap \alpha^{-1}(W_2),\qquad \widetilde V=W_2\cap \beta^{-1}(W_1)$$

Since $W_1$ is dense in $U$ and $\varphi$ is dominant, we have $\cl(\alpha(W_1))=\cl(\alpha(U))=Y$, and therefore the non-empty open subset $W_2$ meets $\alpha(W_1)$, so $\widetilde U\neq\emptyset$.

For a point $x$ of $\widetilde U$, we have $\alpha(x)\in W_2$, and since $x\in W_1$, we have $\beta(\alpha(x))=x\in W_1$, that is, $\alpha(x)\in \beta^{-1}(W_1)$. Therefore $\alpha(\widetilde U)\subseteq \widetilde V$, and similarly for a point $y$ of $\widetilde V$, we have $\beta(y)\in W_1$ and $\alpha(\beta(y))=y\in W_2$, so $\beta(\widetilde V)\subseteq \widetilde U$. The two morphisms $\alpha\vert_{\widetilde U}: \widetilde U \rightarrow \widetilde V$ and $\beta\vert_{\widetilde V}: \widetilde V \rightarrow \widetilde U$ thus obtained have compositions that are identity maps by $\widetilde U\subseteq W_1$ and $\widetilde V\subseteq W_2$, so $\alpha\vert_{\widetilde U}$ is an isomorphism, and since $\widetilde U$ is dense in $X$, $(\widetilde U, \alpha\vert_{\widetilde U})$ is a representative of $\varphi$.

Conversely, suppose an isomorphism $\alpha: \widetilde U \rightarrow \widetilde V$ is a representative of $\varphi$ and let its inverse be $\beta: \widetilde V \rightarrow \widetilde U$. Then since $\widetilde V$ is dense in $Y$, the composition of $\beta$ with the inclusion $\widetilde U \hookrightarrow X$ defines a rational map $\psi: Y \dashrightarrow X$, and since $\beta$ is surjective, $\psi$ is dominant. Also $\psi\circ\varphi$ is $\beta\circ \alpha=\id_{\widetilde U}$ on $\widetilde U$ and $\varphi\circ\psi$ is $\alpha\circ \beta=\id_{\widetilde V}$ on $\widetilde V$, so these are respectively the same as the rational maps defined by $\id_X$ and $\id_Y$.
:::

If an integral scheme $X$ is locally Noetherian, then the domain of a rational function in the sense of [§Algebraic Structure of Schemes, ⁋Definition 12](/en/math/scheme_theory/algebra_of_schemes#def12) is exactly a non-empty open subset of $X$. Indeed, for a non-empty affine open subset $\Spec A$ of $X$, since $A$ is an integral domain ([§Algebraic Structure of Schemes, ⁋Definition 1](/en/math/scheme_theory/algebra_of_schemes#def1)), the annihilator of a non-zero element is always $(0)$, and therefore the associated point of $\Spec A$ is only $(0)$. That is, since the only associated point of $X$ is the generic point $\eta$, the condition that the domain must contain all associated points becomes the same as the condition that the domain is non-empty. We have already verified that the collection $K(X)$ of rational functions thus obtained coincides with $\mathcal{O}_{X,\eta}\cong\Frac A$ and becomes a field ([§Algebraic Structure of Schemes, §§Rational Functions](/en/math/scheme_theory/algebra_of_schemes#rational-functions)), and we call this the *function field* of $X$.

::: Corollary 25
For two birationally equivalent integral locally Noetherian schemes $X, Y$, we have $K(X)\cong K(Y)$.
:::
::: Proof
By [Proposition 24](#prop24), there exists a birational map having an isomorphism $\alpha: \widetilde U \rightarrow \widetilde V$ as representative. The generic point $\eta_X$ of $X$ belongs to the non-empty open subset $\widetilde U$ and the stalk does not change upon restriction to an open subscheme, so $K(X)=\mathcal{O}_{X,\eta_X}=\mathcal{O}_{\widetilde U, \eta_X}$, and similarly $K(Y)=\mathcal{O}_{\widetilde V, \eta_Y}$. On the other hand, since $\widetilde V$ is a non-empty open subset of $Y$, its generic point is $\eta_Y$, and since $\alpha$ is an isomorphism, $\alpha(\eta_X)=\eta_Y$. Therefore the isomorphism between stalks induced by $\alpha$ gives $K(X)\cong K(Y)$.
:::

That is, birational equivalence preserves the function field. In the case of varieties, we have already verified in [\[Algebraic Varieties\] §Rational Maps, ⁋Proposition 10](/en/math/algebraic_varieties/rational_maps#prop10) that the converse also holds.

---

**References**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).
