---
title: "Properties of Scheme Morphisms"
description: "We define key properties of scheme morphisms, introduce the concepts and basic properties of quasi-compact and quasi-separated morphisms, and define rational and birational maps."
excerpt: "Basic properties of scheme morphisms and rational maps"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/properties_of_scheme_morphisms
sidebar: 
    nav: "scheme_theory-en"

date: 2025-02-21
weight: 9
translated_at: 2026-09-26T15:15:05+00:00
translation_source: antigravity-gemini-3.8-flash-high
---
In the previous post, we explored several perspectives for understanding scheme morphisms. In this post, we formally define properties of scheme morphisms. First, we define the following property shared by them.

::: Definition 1
A property $P$ of scheme morphisms is said to be *local on target* if the following two conditions hold:
1. If a scheme morphism $\varphi:X \rightarrow Y$ satisfies $P$, then on $Y$, for any open subscheme $V$, the scheme morphism $\varphi\vert_{\varphi^{-1}(V)}: \varphi^{-1}(V) \rightarrow V$ also satisfies $P$.
2. If, for a scheme morphism $\varphi:X \rightarrow Y$, $Y$ admits an open covering $\{V_j\}$ such that the scheme morphisms $\varphi\vert_{\varphi^{-1}(V_j)}: \varphi^{-1}(V_j) \rightarrow V_j$ all satisfy $P$, then so does $\varphi$.
:::

Schemes are built from affine schemes. If a property $P$ of scheme morphisms is local on target, for a scheme morphism $\varphi:X \rightarrow Y$ we may assume that the target $Y$ is $\Spec B$, and then via the adjunction

$$\Hom_\Sch(X, \Spec B)\cong \Hom_\cRing(B, \Gamma(X, \mathcal{O}_X))$$

we can always reduce to the case where the target is affine.

## Quasi-compact and Quasi-separated Morphisms

::: Definition 2
A scheme morphism $\varphi: X \rightarrow Y$ is *quasi-compact* if for every affine open subset $V\subseteq Y$, the preimage $\varphi^{-1}(V)$ is quasi-compact.
:::

::: Proposition 3
A scheme morphism $\varphi: X \rightarrow Y$ is quasi-compact if and only if the preimage of every quasi-compact open subset of $Y$ is quasi-compact.
:::
::: Proof
Since every affine scheme is quasi-compact ([§The Spectrum, ⁋Lemma 12](/en/math/scheme_theory/spectrums#lem12){: data-lid="1w4g6" }), it is obvious that the given condition implies the condition of [Definition 2](#def2){: data-lid="3nvmf" }.

Conversely, suppose a quasi-compact morphism $\varphi: X \rightarrow Y$ is given. Now, if for $Y$ an arbitrary quasi-compact open subset $V$ is given, there exists a covering of $V$ by finitely many affine open subsets $\{V_j\}$, and their preimages $\varphi^{-1}(V_j)$ are all quasi-compact. Now,

$$\varphi^{-1}(V)=\varphi^{-1}\left(\bigcup_{j\in J} V_j\right)=\bigcup_{j\in J}\varphi^{-1}(V_j)$$

and since a finite union of quasi-compact sets is again quasi-compact, we obtain the desired result.
:::

Then from the equivalence in [Proposition 3](#prop3){: data-lid="vyu1o" }, we see that the composition of quasi-compact morphisms is again quasi-compact. Moreover, the following holds.

::: Proposition 4
For a Noetherian scheme $X$, a scheme morphism $\varphi: X \rightarrow Y$ is always quasi-compact.
:::
::: Proof
Suppose an affine open subset $V\subseteq Y$ is given; we must show that $\varphi^{-1}(V)$ is quasi-compact. However, by [\[Topology\] §Dimension, ⁋Proposition 12](/en/math/topology/dimension#prop12){: data-lid="zqr2y" } and the first result of [\[Topology\] §Dimension, ⁋Proposition 13](/en/math/topology/dimension#prop13){: data-lid="beu8u" }, any subspace of a Noetherian topological space is quasi-compact.
:::

Similarly, we define quasi-separated morphisms. To this end, we first define quasi-separated schemes.

::: Definition 5
A scheme $X$ is *quasi-separated* if the intersection of any two quasi-compact open subsets of $X$ is again quasi-compact. A scheme morphism $\varphi: X \rightarrow Y$ is *quasi-separated* if for every affine open set $V\subseteq Y$, $\varphi^{-1}(V)$ is quasi-separated.
:::

Then the following holds.

::: Proposition 6
A locally Noetherian scheme is always quasi-separated. 
:::
::: Proof
Let $X$ be a locally Noetherian scheme, and let $V_1=\Spec B_1, V_2=\Spec B_2$ be any two affine open subsets; we must show that $V_1\cap V_2$ is quasi-compact. 

First, since $X$ is locally Noetherian, we can cover $X$ by spectra $U_i=\Spec A_i$ of Noetherian rings. Now for each $i$, by [§The Topology of Schemes, ⁋Lemma 11](/en/math/scheme_theory/topology_of_schemes#lem11){: data-lid="rqpr9" }, we can cover $U_i\cap V_1$ by spectra $\Spec (A_i)_g$ of Noetherian rings. Collecting all of these covers $V_1$ by spectra of Noetherian rings, and by [§The Spectrum, ⁋Lemma 12](/en/math/scheme_theory/spectrums#lem12){: data-lid="eo0c4" }, $V_1=\Spec B_1$ is covered by finitely many spectra of Noetherian rings. Therefore, by [§The Topology of Schemes, ⁋Lemma 13](/en/math/scheme_theory/topology_of_schemes#lem13){: data-lid="4rbw5" }, $B_1$ is a Noetherian ring, and hence $V_1=\Spec B_1$ is Noetherian. Furthermore, since any subspace of a Noetherian topological space is quasi-compact by [\[Topology\] §Dimension, ⁋Proposition 12](/en/math/topology/dimension#prop12){: data-lid="zeqj2" } and the first result of [\[Topology\] §Dimension, ⁋Proposition 13](/en/math/topology/dimension#prop13){: data-lid="8ywui" }, in particular $V_1\cap V_2$ is also quasi-compact. By the same reasoning, any affine open of $X$ is Noetherian, and since a quasi-compact open is a union of finitely many affine opens, it is also Noetherian. Since a subspace of a Noetherian topological space is quasi-compact, the intersection of any two quasi-compact opens is also quasi-compact, and thus by [Definition 5](#def5){: data-lid="wigyz" }, $X$ is quasi-separated. 
:::

Then quasi-compactness and quasi-separatedness not only satisfy the properties of [Definition 1](#def1){: data-lid="j4zin" }, but are also *affine-local on target*, as can be seen in the following proposition. ([§The Topology of Schemes, ⁋Definition 9](/en/math/scheme_theory/topology_of_schemes#def9){: data-lid="uoptb" })

::: Proposition 7
For a scheme morphism $\varphi: X \rightarrow Y$, the following hold.

1. If $Y$ has an affine open covering $\{V_j\}$ such that each $\varphi^{-1}(V_j)$ is quasi-compact, then $\varphi$ is quasi-compact. 
2. If $Y$ has an affine open covering $\{V_j\}$ such that each $\varphi^{-1}(V_j)$ is quasi-separated, then $\varphi$ is quasi-separated. 
:::
::: Proof
1. Let an arbitrary affine open subset $V$ of $Y$ be given. Then by [§The Topology of Schemes, ⁋Lemma 11](/en/math/scheme_theory/topology_of_schemes#lem11){: data-lid="uriva" }, we can cover $V\cap V_j$ by open sets that are principal open sets in both $V$ and $V_j$, and considering this for all $j$ and using the quasi-compactness of $V$, we can choose only finitely many such sets. Let this be $V=\bigcup W_l$.   
    On the other hand, for each $l$, choosing $V_{j(l)}$ that has $W_l$ as a principal open subset, since $\varphi^{-1}(V_{j(l)})$ is quasi-compact, we can cover it by finitely many affine open subsets $U_{j(l)k}$. Now since $\varphi^{-1}(W_l)\cap U_{j(l)k}$ is a principal open set of $U_{j(l)k}$ by [§The Spectrum, ⁋Proposition 8](/en/math/scheme_theory/spectrums#prop8){: data-lid="gjph5" }, each $\varphi^{-1}(W_l)$ can be expressed as a finite union of affine open sets, and hence $\varphi^{-1}(V)$ can also be expressed as a finite union of affine open sets. Since a finite union of quasi-compact spaces is quasi-compact, we obtain the desired result.
2. First, a scheme $Z$ is quasi-separated if and only if the intersection of any two affine open subsets of $Z$ is quasi-compact. Since affine schemes are quasi-compact, one direction is trivial; conversely, since any quasi-compact open subset of $Z$ is a union of finitely many affine open subsets, the intersection of two quasi-compact open subsets is the union of finitely many intersections of affine open sets, and is therefore quasi-compact.     
    Now, as in the proof of the first statement, choose a finite covering $V=\bigcup_{l=1}^n W_l$ of $V$ such that each $W_l$ is a principal open subset in both $V$ and a suitable $V_{j(l)}$. Given two affine open subsets $U_1,U_2$ of $\varphi^{-1}(V)$, we have
    
    $$U_1\cap U_2=\bigcup_{l=1}^n\left(U_1\cap \varphi^{-1}(W_l)\right)\cap\left(U_2\cap \varphi^{-1}(W_l)\right)$$
    
    Here, since $W_l$ is a principal open subset of $V$, $U_1\cap \varphi^{-1}(W_l)$ is the principal open set defined on the affine scheme $U_1$ by the pullback of the function defining $W_l$ ([§The Spectrum, ⁋Proposition 8](/en/math/scheme_theory/spectrums#prop8){: data-lid="j2t1s" }), and hence is affine; the same holds for $U_2$. But these are all affine open subsets of $\varphi^{-1}(W_l)\subseteq \varphi^{-1}(V_{j(l)})$, and since $\varphi^{-1}(V_{j(l)})$ is quasi-separated, each intersection is quasi-compact by the above criterion. From the above, $U_1\cap U_2$ is quasi-compact as it is a union of finitely many quasi-compact sets, and again by the above criterion, $\varphi^{-1}(V)$ is quasi-separated. 
:::

## Affine Morphisms

From the adjunction

$$\Hom_\Sch(X, \Spec B)\cong\Hom_\cRing (B, \Gamma(X, \mathcal{O}_X))$$

we know that in particular when $X=\Spec A$,

$$\Hom_\Sch(\Spec A,\Spec B)\cong\Hom_\cRing (B, A)$$

holds. ([§Affine Scheme, ⁋Proposition 11](/en/math/scheme_theory/affine_schemes#prop11){: data-lid="dx7qq" }) Therefore, when examining properties of scheme morphisms that are affine-local on target as above, it would be desirable if for any affine open subset $V\cong\Spec B$ of $Y$, $U=\varphi^{-1}(V)$ were also an open subscheme $U\cong \Spec A$ of $X$, so that $\varphi\vert_U: U \rightarrow V$ becomes a morphism between affine schemes and we could obtain this property from the ring homomorphism 

$$(\varphi\vert_U)^\sharp(V): \mathcal{O}_V(V) \rightarrow \mathcal{O}_U(U)$$

However, of course, for an arbitrary scheme morphism $\varphi: X \rightarrow Y$, the preimage of an affine open subset of $Y$ need not be affine. ([§Schemes, ⁋Example 8](/en/math/scheme_theory/schemes#ex8){: data-lid="poxcb" })

::: Definition 8
A scheme morphism $\varphi: X \rightarrow Y$ is an *affine morphism* if for any affine open subset $V$ of $Y$, $\varphi^{-1}(V)$ is an affine open subset of $X$. 
:::

Then it is clear that the composition of affine morphisms is affine. Furthermore, this property also satisfies the conditions of [Definition 1](#def1){: data-lid="nbmuc" }, the proof of which is given in the next proposition.

::: Proposition 9
For a scheme morphism $\varphi:X \rightarrow Y$, if there exists an affine open covering $\{V_j\}$ of $Y$ such that each $\varphi^{-1}(V_j)$ is affine, then $\varphi$ is affine. 
:::
::: Proof
For an affine open subset $\Spec B$ of $Y$, define the property $P$ by "$\varphi^{-1}(\Spec B)$ is an affine open subset of $X$". Then $\varphi$ being affine means that every affine open subset of $Y$ satisfies $P$, and the given assumption is that some affine open covering of $Y$ satisfies $P$. Thus, by the equivalence between the second and third conditions of [§The Topology of Schemes, ⁋Lemma 12](/en/math/scheme_theory/topology_of_schemes#lem12){: data-lid="chi4h" }, it suffices to show that $P$ is an affine-local property in the sense of [§The Topology of Schemes, ⁋Definition 9](/en/math/scheme_theory/topology_of_schemes#def9){: data-lid="sxsxy" }. In what follows, we write the component of the sheaf morphism $\varphi^\sharp: \mathcal{O}_Y \rightarrow \varphi_\ast \mathcal{O}_X$ on an open set $V$ as $\varphi^\sharp(V): \mathcal{O}_Y(V) \rightarrow \mathcal{O}_X(\varphi^{-1}(V))$.

First, let us verify the first condition of [§The Topology of Schemes, ⁋Definition 9](/en/math/scheme_theory/topology_of_schemes#def9){: data-lid="wvr3n" }. If $\varphi^{-1}(\Spec B)$ is an affine open subset $\Spec A$, then by [§Affine Scheme, ⁋Proposition 11](/en/math/scheme_theory/affine_schemes#prop11){: data-lid="1u4l4" }, $\Spec A \rightarrow \Spec B$ is of the form $\Spec\phi$ for some ring homomorphism $\phi: B \rightarrow A$, and from the formula

$$(\Spec\phi)^{-1}(D(f))=D(\phi(f))$$

obtained in the proof of [§The Spectrum, ⁋Proposition 8](/en/math/scheme_theory/spectrums#prop8){: data-lid="1flwg" }, for any $f\in B$ we have $\varphi^{-1}(\Spec B_f)=D(\phi(f))\cong\Spec A_{\phi(f)}$, so $\Spec B_f$ also satisfies $P$.

Now we must check the second condition. That is, assuming $B=(f_1,\ldots, f_r)$ and that each $U_i=\varphi^{-1}(D(f_i))$ is affine, we must show that $U=\varphi^{-1}(\Spec B)$ is affine. For convenience, let $R=\Gamma(U, \mathcal{O}_X)$, and let the image of $f_i$ under $\varphi^\sharp(\Spec B): B \rightarrow R$ be $g_i\in R$. Also, for $g\in \Gamma(U, \mathcal{O}_X)$, for points at which the stalk of $g$ does *not* belong to the maximal ideal of $\mathcal{O}_{X,x}$, we write the set of such points $x$ as $U_g$. Then for any affine open subset of $U$, say $\Spec A$, it is clear by definition that $U_g\cap \Spec A=D(g\vert_{\Spec A})$, and in particular $U_g$ is open.

We make the following three observations. First, since $B=(f_1,\ldots, f_r)$, we have $\Spec B=\bigcup_{i=1}^rD(f_i)$, and hence $\{U_i\}_{i=1}^r$ is a finite affine open covering of $U$. Furthermore, since $1=\sum_{i=1}^rb_if_i$ for some $b_i\in B$, applying $\varphi^\sharp(\Spec B)$ shows that $g_1,\ldots, g_r$ generate the unit ideal of $R$. Second, since $\varphi$ is a morphism of locally ringed spaces, at each $x\in U$ the map $\varphi^\sharp_x:\mathcal{O}_{Y,\varphi(x)} \rightarrow \mathcal{O}_{X,x}$ is a local homomorphism, and hence $\varphi(x)\in D(f_i)$ is equivalent to $x\in U_{g_i}$, so $U_i=U_{g_i}$. Third, writing $U_i\cong \Spec A_i$ and letting the ring homomorphism corresponding to $\Spec A_i \rightarrow \Spec B_{f_i}$ be $\phi_i$, since $D(f_j)\cap D(f_i)$ is a principal open set of $\Spec B_{f_i}$, applying [§The Spectrum, ⁋Proposition 8](/en/math/scheme_theory/spectrums#prop8){: data-lid="dyn9e" } as above shows that $U_i\cap U_j$ is a principal open set of $\Spec A_i$, and in particular affine.

Now, for each $i$, we show that the canonical map $R_{g_i} \rightarrow \Gamma(U_{g_i}, \mathcal{O}_X)$ is an isomorphism. For the open covering of $U$ given by $\{U_j\}_{j=1}^r$, the two conditions of [\[Topology\] §Sheaves, ⁋Definition 1](/en/math/topology/sheaves#def1){: data-lid="t4ykt" } are equivalent to the existence of the following exact sequence:

$$0 \rightarrow R \rightarrow \bigoplus_{j=1}^r \mathcal{O}_X(U_j) \rightarrow \bigoplus_{j,k=1}^r \mathcal{O}_X(U_j\cap U_k)$$

Here, the second map is $(s_j)_j\mapsto (s_j\vert_{U_j\cap U_k}-s_k\vert_{U_j\cap U_k})_{j,k}$. Since this is an exact sequence of $R$-modules and the direct sums are finite, by [\[Commutative Algebra\] §Properties of Localization, ⁋Proposition 2](/en/math/commutative_algebra/properties_of_localization#prop2){: data-lid="uyj08" }, exactness is preserved upon localizing at $g_i$, so we obtain the exact sequence

$$0 \rightarrow R_{g_i} \rightarrow \bigoplus_{j=1}^r \mathcal{O}_X(U_j)_{g_i} \rightarrow \bigoplus_{j,k=1}^r \mathcal{O}_X(U_j\cap U_k)_{g_i}$$

(Here, the localization of $\mathcal{O}_X(U_j)$ means localization at the restriction of $g_i$ to $U_j$.) On the other hand, both $U_j$ and $U_j\cap U_k$ are affine, and for an affine scheme $\Spec A$ and $a\in A$ we have $\mathcal{O}_{\Spec A}(D(a))=A_a$ ([§Schemes, ⁋Lemma 2](/en/math/scheme_theory/schemes#lem2){: data-lid="t0i9x" }), so from $U_g\cap \Spec A=D(g\vert_{\Spec A})$ observed above, we obtain

$$\mathcal{O}_X(U_j)_{g_i}=\mathcal{O}_X(U_j\cap U_{g_i}),\qquad \mathcal{O}_X(U_j\cap U_k)_{g_i}=\mathcal{O}_X(U_j\cap U_k\cap U_{g_i})$$

However, this exact sequence is precisely the exact sequence given by the sheaf condition for the open covering of $U_{g_i}$ by $\{U_j\cap U_{g_i}\}_{j=1}^r$, so $R_{g_i}$ and $\Gamma(U_{g_i}, \mathcal{O}_X)$ are both kernels of the same map, and thus the canonical map $R_{g_i} \rightarrow \Gamma(U_{g_i}, \mathcal{O}_X)$ is an isomorphism.

Finally, in the adjunction of [§Affine Scheme, ⁋Theorem 13](/en/math/scheme_theory/affine_schemes#thm13){: data-lid="3h3ot" },

$$\Hom_\Sch(U, \Spec R)\cong \Hom_\cRing(R, \Gamma(U, \mathcal{O}_X))$$

consider the scheme morphism $\psi: U \rightarrow \Spec R$ corresponding to $\id_R$. Since $\psi$ is also a morphism of locally ringed spaces, at each $x\in U$ the map $\psi^\sharp_x$ is a local homomorphism, and since the composition $R \rightarrow \mathcal{O}_{\Spec R, \psi(x)} \rightarrow \mathcal{O}_{X,x}$ is the canonical map $R=\Gamma(U, \mathcal{O}_X) \rightarrow \mathcal{O}_{X,x}$, the point $\psi(x)$ is the preimage under this canonical map of the maximal ideal of $\mathcal{O}_{X,x}$. Therefore,

$$\psi^{-1}(D(g_i))=U_{g_i}=U_i$$

and since $\psi\vert_{U_i}: U_i \rightarrow D(g_i)\cong \Spec R_{g_i}$ is a morphism between affine schemes corresponding to the isomorphism $R_{g_i}\cong \Gamma(U_i, \mathcal{O}_X)$ just obtained, it is an isomorphism by [§Affine Scheme, ⁋Proposition 11](/en/math/scheme_theory/affine_schemes#prop11){: data-lid="jkb7q" }. Now, since the $g_i$ generate the unit ideal of $R$, the open sets $\{D(g_i)\}$ cover $\Spec R$ and $\{U_i\}$ covers $U$, so $\psi$ is an isomorphism. That is, $U\cong\Spec R$ is affine. 
:::

## Finite Morphisms, Integral Morphisms, and Morphisms of Finite Type

::: Definition 10
A scheme morphism $\varphi:X \rightarrow Y$ is *finite* if $\varphi$ is affine, and for every affine open subset $V$ of $Y$, the ring homomorphism

$$(\varphi\vert_{\varphi^{-1}(V)})^\sharp(V): \mathcal{O}_V(V) \rightarrow \mathcal{O}_{\varphi^{-1}(V)}(\varphi^{-1}(V))$$

is a finite ring homomorphism. ([\[Commutative Algebra\] §Integral Extensions, ⁋Definition 3](/en/math/commutative_algebra/integral_extension#def3){: data-lid="jkjaj" })
:::

To help understand this, let us write an affine open subset $V\subseteq Y$ as $\Spec B$. Then, from the assumption that $\varphi$ is affine, $U=\varphi^{-1}(V)$ is an affine open subset of $X$, and thus there exists $A$ such that $U\cong\Spec A$. Through this identification, the scheme morphism $\varphi\vert_U: U \rightarrow V$ is the same as a morphism between spectra $\Spec A \rightarrow \Spec B$, and $\varphi$ being finite now means that the ring homomorphism $B \rightarrow A$ corresponding to this morphism is finite. Similarly, we define the following.

::: Definition 11
A scheme morphism $\varphi:X \rightarrow Y$ is *integral* if $\varphi$ is affine, and for every affine open subset $V$ of $Y$, the ring homomorphism

$$(\varphi\vert_{\varphi^{-1}(V)})^\sharp(V): \mathcal{O}_V(V) \rightarrow \mathcal{O}_{\varphi^{-1}(V)}(\varphi^{-1}(V))$$

is an integral ring homomorphism. ([\[Commutative Algebra\] §Integral Extensions, ⁋Definition 3](/en/math/commutative_algebra/integral_extension#def3){: data-lid="1vftw" }) 
:::

Now from the definitions, we see that finite morphisms and integral morphisms are closed under composition. In addition, since we can see that they satisfy the affine-local property condition of [§The Topology of Schemes, ⁋Definition 9](/en/math/scheme_theory/topology_of_schemes#def9){: data-lid="fepvg" } from [Proposition 9](#prop9){: data-lid="1e5fl" } and [\[Commutative Algebra\] §Integral Extensions, ⁋Proposition 14](/en/math/commutative_algebra/integral_extension#prop14){: data-lid="arb1f" }, [\[Commutative Algebra\] §Integral Extensions, ⁋Proposition 15](/en/math/commutative_algebra/integral_extension#prop15){: data-lid="igqsg" }, they are both affine-local on target. 

We know that every finite morphism is integral by [\[Commutative Algebra\] §Integral Extensions, ⁋Lemma 4](/en/math/commutative_algebra/integral_extension#lem4){: data-lid="7bzin" }. Now, in order to state this lemma completely in the language of algebraic geometry, we must define morphisms of finite type. 

::: Definition 12
A scheme morphism $\varphi:X \rightarrow Y$ is *locally of finite type* if for every affine open subset $V$ of $Y$ and every affine open subset $U$ of $\varphi^{-1}(V)$, 

$$(\varphi\vert_{U})^\sharp(V): \mathcal{O}_V(V) \rightarrow \mathcal{O}_U(U)$$

is of finite type. ([\[Commutative Algebra\] §Integral Extensions, ⁋Definition 3](/en/math/commutative_algebra/integral_extension#def3){: data-lid="d2pdc" }) 
:::

Just as above, let $V\cong \Spec B$ and let $U\cong\Spec A\subseteq \varphi^{-1}(V)$. Then we can view the scheme morphism $\varphi\vert_U: U \rightarrow V$ as $\Spec A \rightarrow \Spec B$, and this requires that the corresponding ring homomorphism $B \rightarrow A$ be of finite type.

Since [Definition 12](#def12){: data-lid="fvpao" } quantifies over *all* affine open subsets of $\varphi^{-1}(V)$, we must show separately that a single affine open covering is sufficient to check this. This is the content of the following lemma.

::: Lemma 13
Let a scheme morphism $\varphi: W \rightarrow \Spec B$ be given, and suppose $W$ has an affine open covering $\{\Spec A_i\}$ such that each $B \rightarrow A_i$ is of finite type. Then on $W$, for *any* affine open subset $U$, the map $B \rightarrow \mathcal{O}_W(U)$ is also of finite type. 
:::
::: Proof
For an affine open subset of $W$, $\Spec R$, define a property $Q$ by 

> $B \rightarrow R$ is of finite type,

and let us show that $Q$ is an affine-local property in the sense of [§The Topology of Schemes, ⁋Definition 9](/en/math/scheme_theory/topology_of_schemes#def9){: data-lid="g7qki" }. Then, since the given covering $\{\Spec A_i\}$ satisfies $Q$, the desired result follows from the second condition of [§The Topology of Schemes, ⁋Lemma 12](/en/math/scheme_theory/topology_of_schemes#lem12){: data-lid="9anst" }.

The first condition is clear because when $B \rightarrow R$ is of finite type, adjoining to the generators of $R$ the element $1/h$ makes $R_h$ finitely generated as a $B$-algebra. For the second condition, suppose that $R=(h_1,\ldots, h_m)$ and that each $B \rightarrow R_{h_t}$ is of finite type. For each $t$, choosing a finite generating set of $R_{h_t}$ as a $B$-algebra and clearing denominators, there exist elements in $R$, $x_{t1},\ldots, x_{tn_t}$, such that $R_{h_t}$ is generated by the $x_{tk}/1$ and $1/h_t$ as a $B$-algebra. Also, write $1=\sum_{t=1}^ma_th_t$ with $a_t\in R$. Now, let the finite set $\{h_t\}\cup\{a_t\}\cup\{x_{tk}\}$ generate in $R$ a $B$-subalgebra $R'$; then since $R'$ is a finite type $B$-algebra, it suffices to show that $R'=R$. For any $x\in R$, in $R_{h_t}$ the element $x/1$ is a polynomial in the $x_{tk}/1$ and $1/h_t$ with coefficients in $B$, so for some $r_t\in R'$ and $n_t\geq 0$ we have $x/1=r_t/h_t^{n_t}$, and thus for some $N_t$, in $R$ we have $h_t^{N_t}(h_t^{n_t}x-r_t)=0$, that is, $h_t^{N_t+n_t}x=h_t^{N_t}r_t\in R'$. Since there are only finitely many $t$, we can choose a common $M$ such that for all $t$, we have $h_t^Mx\in R'$. Meanwhile, from $1=\sum_ta_th_t$, since $a_t,h_t\in R'$, the elements $h_1,\ldots, h_m$ generate the unit ideal of $R'$, and by raising both sides of this equation to a sufficiently high power, we see that $h_1^M,\ldots, h_m^M$ also generate the unit ideal of $R'$. That is, we can write $1=\sum_tc_th_t^M$ for some $c_t\in R'$, and therefore

$$x=\sum_{t=1}^mc_t(h_t^Mx)\in R'$$

as desired. 
:::

Then morphisms of finite type are defined as follows.

::: Definition 14
A scheme morphism $\varphi:X \rightarrow Y$ is a *morphism of finite type* if $\varphi$ is a quasi-compact morphism locally of finite type. 
:::

From the definition, it is clear that morphisms locally of finite type are affine-local on the target. In addition, since quasi-compact morphisms are affine-local on the target by [Proposition 7](#prop7){: data-lid="ghf3q" }, morphisms of finite type are also affine-local on the target. 

Then by [\[Commutative Algebra\] §Integral Extensions, ⁋Lemma 4](/en/math/commutative_algebra/integral_extension#lem4){: data-lid="u5il1" }, the following holds.

::: Proposition 15
A scheme morphism $\varphi:X \rightarrow Y$ is finite if and only if $\varphi$ is an integral morphism (locally) of finite type. 
:::
::: Proof
First, suppose that $\varphi$ is finite. For any affine open subset $V=\Spec B\subseteq Y$, we have $\varphi^{-1}(V)=\Spec A$ and $B \rightarrow A$ is finite, so by [\[Commutative Algebra\] §Integral Extensions, ⁋Lemma 4](/en/math/commutative_algebra/integral_extension#lem4){: data-lid="3ahg6" }, this is integral and in particular of finite type. That is, $\varphi$ is integral, and taking $\{\varphi^{-1}(V)\}$ itself as an affine open covering and applying [Lemma 13](#lem13){: data-lid="pxsgj" }, for $\varphi^{-1}(V)$, *every* affine open subset $U$ also satisfies that $B \rightarrow \mathcal{O}_X(U)$ is of finite type, so $\varphi$ is locally of finite type. For the converse, from the assumption that $\varphi$ is integral, we first know that for any affine open subset $V\subseteq Y$, the preimage $\varphi^{-1}(V)$ is an affine open subset of $X$, and it suffices to apply [\[Commutative Algebra\] §Integral Extensions, ⁋Lemma 4](/en/math/commutative_algebra/integral_extension#lem4){: data-lid="xytg7" } to the ring map obtained in this way. 
:::

In the proposition above, since $\varphi$ is an integral morphism, it is an affine morphism, and hence a quasi-compact morphism ([§The Spectrum, ⁋Lemma 12](/en/math/scheme_theory/spectrums#lem12){: data-lid="gyplv" }); thus whether $\varphi$ is of finite type or locally of finite type amounts to the same hypothesis.

::: Example 16
Let us look at examples of the morphisms examined in this section. In the world of affine schemes, this is merely looking at examples from [\[Commutative Algebra\] §Integral Extensions, ⁋Definition 3](/en/math/commutative_algebra/integral_extension#def3){: data-lid="l5qy6" }. The purpose of this example is to give them geometric intuition.

First, for an algebraically closed field $\mathbb{K}$, if we consider the ring map $\iota:\mathbb{K}[\x] \rightarrow \mathbb{K}[\x,\y]$, then $\mathbb{K}[\x,\y]$ is generated by a single element $\y$ as a $\mathbb{K}[\x]$-algebra, so it is a ring homomorphism of finite type; however, as a $\mathbb{K}[\x]$-module, it is not finitely generated, and thus is not a finite ring homomorphism. 

Now consider the corresponding morphism of schemes $\Spec\iota: \Spec \mathbb{K}[\x,\y] \rightarrow\Spec \mathbb{K}[\x]$. This is the map that takes any prime ideal $\mathfrak{p}\subseteq \mathbb{K}[\x,\y]$ and sends it to the prime ideal $\mathfrak{p}\cap \mathbb{K}[\x]$ of $\mathbb{K}[\x]$. Geometrically, this is the map sending a point $(x,y)$ on the affine plane $\mathbb{A}^2_\mathbb{K}$ to the point $x$ on the affine line $\mathbb{A}^1_\mathbb{K}$. 

{% diagram Math/Scheme_Theory/Properties_of_Scheme_Morphisms-1.svg width="28.04em" alt="finite_type_morphism" %}

An example of a related finite morphism is obtained by composing the ring homomorphism $\iota:\mathbb{K}[\x]\rightarrow \mathbb{K}[\x,\y]$ above with the projection map $\pi:\mathbb{K}[\x,\y] \rightarrow \mathbb{K}[\x,\y]/(\x-\y^2)$. Then $\mathbb{K}[\x,\y]/(\x-\y^2)$ is generated by $1$ and $\y$ as a $\mathbb{K}[\x]$-module, so $\phi:\mathbb{K}[\x] \rightarrow \mathbb{K}[\x,\y]/(\x-\y^2)$ is a finite ring homomorphism. 

Meanwhile, we know that a ring homomorphism $\pi:A \rightarrow A/\mathfrak{a}$ corresponds geometrically to the inclusion of the closed subset defined by $\mathfrak{a}$. Therefore, the morphism of schemes defined by the composition

$$\phi: \mathbb{K}[\x] \rightarrow \mathbb{K}[\x,\y] \rightarrow \mathbb{K}[\x,\y]/(\x-\y^2)$$

which is

$$\Spec\phi: \Spec \frac{\mathbb{K}[\x,\y]}{(\x-\y^2)}\rightarrow \Spec \mathbb{K}[\x,\y] \rightarrow \Spec\mathbb{K}[\x]$$

can be viewed geometrically as the projection from the zero set $Z(\x-\y^2)$ of $\x=\y^2$ to the $x$-axis.

{% diagram Math/Scheme_Theory/Properties_of_Scheme_Morphisms-2.svg width="25.72em" alt="finite_morphism" %}

The geometric difference between these two examples is quite clear. In the first example, the fiber over a point of the target is an infinite set, whereas in the second example, the fiber over a point is a finite set. Algebraically, when we take any point $\mathfrak{p}=(\x-a)$ of the target $\mathbb{A}_\mathbb{K}^1$, any $\mathfrak{q}_b=(\x-a, \y-b)\in \mathbb{A}_\mathbb{K}^2$ satisfies $(\Spec\iota)(\mathfrak{q}_b)=\mathfrak{p}$, whereas in the second example, since $\y^2=\x$ must hold, only $b$ such that $b^2=a$ are possible, and thus there are at most two points satisfying $(\Spec\phi)(\mathfrak{q})=\mathfrak{p}$, namely $\mathfrak{q}_+=(\x-a, \y-\sqrt{a})$ and $\mathfrak{q}_-=(\x-a, \y+\sqrt{a})$. These two points are distinct when $\operatorname{char}\mathbb{K}\neq 2$ and $a\neq 0$; if $a=0$, the two points coincide, and when $\operatorname{char}\mathbb{K}=2$, we have $\y^2-a=(\y-\sqrt{a})^2$, so the fiber is a single point for every $a$. 

In this way, a morphism of finite type is geometrically related to fibers being finite-dimensional, and a finite morphism is related to fibers being finite sets. 
:::

For now, to compute the fibers of a morphism of schemes in situations like [Example 16](#ex16){: data-lid="5vwhy" } above, we have no choice but to compute them directly on a case-by-case basis, but once we compute fiber products later on, we will be able to use a more systematic approach. For that time, we define the following.

::: Definition 17
A morphism of schemes $\varphi: X \rightarrow Y$ is *quasi-finite* if $\varphi$ is a morphism of finite type and for every $y\in Y$, the set $\varphi^{-1}(y)$ is always a finite set. 
:::

Then the geometric intuition regarding finite morphisms in [Example 16](#ex16){: data-lid="38q0a" } is always true. That is, every finite morphism is always quasi-finite. While it is possible to prove this right now, we postpone it until after defining the fiber product. 

Finally, we define the following.

::: Definition 18
A scheme morphism $\varphi: X \rightarrow Y$ is *locally of finite presentation* if for every affine open subset $V\cong \Spec B$ of $Y$, there exists a covering $\varphi^{-1}(V)=\bigcup \Spec A_i$ of $\varphi^{-1}(V)$ such that each $B \rightarrow A_i$ is finitely presented. If a scheme morphism $\varphi:X \rightarrow Y$ is quasi-compact, quasi-separated, and locally of finite presentation, then $\varphi$ is called a *morphism of finite presentation*. 
:::

In most cases, we consider the situation where all schemes are locally Noetherian, in which case this concept is not new. Indeed, if $B$ is a Noetherian ring and $B \rightarrow A$ is of finite type, then we can write $A\cong B[\x_1,\ldots, \x_n]/\mathfrak{a}$, and since $B[\x_1,\ldots, \x_n]$ is Noetherian by [\[Commutative Algebra\] §Basic Notions, ⁋Theorem 12](/en/math/commutative_algebra/basic_notions#thm12){: data-lid="my4y7" }, $\mathfrak{a}$ is finitely generated and thus $B \rightarrow A$ is finitely presented. Furthermore, since locally Noetherian schemes are quasi-separated ([Proposition 6](#prop6){: data-lid="oid3b" }), the difference between requiring a morphism to be of finite presentation and requiring it to be of finite type also disappears. 

## Rational Maps

In [§Algebraic Structure of Schemes, ⁋Definition 12](/en/math/scheme_theory/algebra_of_schemes#def12){: data-lid="b6u0x" }, we defined a rational function on a scheme $X$ as the equivalence class of a pair consisting of a domain $U$ and a function $f\in \Gamma(U, \mathcal{O}_X)$ on it. Meanwhile, viewing $U$ as a locally ringed space in its own right, by the adjunction of [§Affine Scheme, ⁋Theorem 13](/en/math/scheme_theory/affine_schemes#thm13){: data-lid="bq75h" } we obtain

$$\Hom_\LRS(U, \Spec \mathbb{Z}[\x])\cong \Hom_{\cRing}(\mathbb{Z}[\x], \Gamma(U,\mathcal{O}_X))$$

and since the ring homomorphism $\mathbb{Z}[\x]\rightarrow \Gamma(U, \mathcal{O}_X)$ on the right-hand side is uniquely determined by the image of $\x$, the right-hand side can be connected via an additional isomorphism

$$\Hom_{\cRing}(\mathbb{Z}[\x], \Gamma(U,\mathcal{O}_X))\cong \Gamma(U, \mathcal{O}_X)$$

to give that supplying a function $f$ on $U$ is the same data as supplying a scheme morphism $U \rightarrow \Spec \mathbb{Z}[\x]=\mathbb{A}^1_\mathbb{Z}$. 

On the other hand, having defined scheme morphisms, we may now choose a general $\Spec A$ as the base scheme instead of $\Spec \mathbb{Z}$, so repeating this argument allows us to think of a rational function as a morphism defined on $U$ with target $\Spec A[\x]$. To write this down precisely, we must specify which open sets are admissible as domains, and when two morphisms on different domains are to be considered equivalent. First, we give a name to morphisms whose image is not trapped inside a small closed subset of the target.

::: Definition 19
A scheme morphism $\varphi: X \rightarrow Y$ is *dominant* if the image of $\varphi$ is dense in $Y$, that is, $\cl(\varphi(X))=Y$. 
:::

A surjective morphism is always dominant, but the converse does not hold. For instance, for an integral domain $A$ that is not a field, the image of $\Spec \Frac A \rightarrow \Spec A$ consists only of the generic point $(0)$, but as we saw immediately after [§The Spectrum, ⁋Definition 7](/en/math/scheme_theory/spectrums#def7){: data-lid="uhwfh" }, the only closed subset of $\Spec A$ containing $(0)$ is $\Spec A$ itself, so this morphism is dominant. Dominance between affine schemes can be interpreted purely algebraically as follows.

::: Proposition 20
For a ring homomorphism $\phi: B \rightarrow A$ and the corresponding scheme morphism $\varphi=\Spec \phi:\Spec A \rightarrow \Spec B$, the identity

$$\cl\left(\varphi(\Spec A)\right)=Z(\ker\phi)$$

holds. Therefore, $\varphi$ is dominant if and only if $\ker\phi\subseteq \mathfrak{N}(B)$.
:::
::: Proof
By the second result of [§The Spectrum, ⁋Proposition 14](/en/math/scheme_theory/spectrums#prop14){: data-lid="smxep" }, for any $T\subseteq \Spec B$ we have $\cl(T)=Z(I(T))$, so for $T=\varphi(\Spec A)$ it suffices to compute $I(T)$. Since the elements of $T$ are precisely of the form $\phi^{-1}(\mathfrak{q})$, we obtain

$$I(T)=\bigcap_{\mathfrak{q}\in \Spec A}\phi^{-1}(\mathfrak{q})=\phi^{-1}\left(\bigcap_{\mathfrak{q}\in \Spec A}\mathfrak{q}\right)$$

. On the other hand, applying the first result of [§The Spectrum, ⁋Proposition 14](/en/math/scheme_theory/spectrums#prop14){: data-lid="0tk0p" } to $S=\{0\}$, we know that the intersection of all prime ideals of $A$ is $\sqrt{(0)}=\mathfrak{N}(A)$, and for any $b\in B$, $\phi(b)$ being nilpotent is equivalent to having $b^n\in\ker\phi$ for some $n$, so

$$I(T)=\phi^{-1}(\mathfrak{N}(A))=\sqrt{\ker\phi}$$

holds. Now, applying the first result of [§The Spectrum, ⁋Proposition 14](/en/math/scheme_theory/spectrums#prop14){: data-lid="vi43a" } again to the identity $Z(I(Z(S)))=Z(S)$, we have $Z(\sqrt{\ker\phi})=Z(\ker\phi)$, which yields the desired formula.

The last assertion holds because $Z(\ker\phi)=\Spec B$ is equivalent to $\ker\phi$ being contained in every prime ideal of $B$, which, for the same reason as above, is equivalent to $\ker\phi\subseteq \mathfrak{N}(B)$.
:::

In particular, if $B$ is a reduced ring, then $\Spec\phi$ being dominant is equivalent to $\phi$ being injective. For example, as seen in [Example 16](#ex16){: data-lid="gg9nf" }, $\iota: \mathbb{K}[\x] \rightarrow \mathbb{K}[\x,\y]$ is injective, so $\Spec\iota$ is dominant; and for an ideal $\mathfrak{a}\subseteq B$, the morphism $\Spec B/\mathfrak{a} \rightarrow \Spec B$ defined by the quotient map is dominant if and only if $\mathfrak{a}\subseteq \mathfrak{N}(B)$, that is, the closed set defined by $\mathfrak{a}$ is all of $\Spec B$.

We now specify the open subsets that will serve as domains. Just as in the case of rational functions, the domain must be sufficiently large in $X$, and the topological formulation of this is the density condition. As one can guess from the argument above, in a reduced scheme, this condition alone preserves the information of the function.

::: Lemma 21
For a reduced scheme $X$ and a dense open subset $U$, the restriction map $\Gamma(X, \mathcal{O}_X) \rightarrow \Gamma(U, \mathcal{O}_X)$ is injective. 
:::
::: Proof
Suppose that $s\in \Gamma(X, \mathcal{O}_X)$ satisfies $s\vert_U=0$. Pick any affine open subset of $X$, denoted $\Spec A$, and for convenience, let us denote the restriction of $s$ to $\Spec A$ again by $s\in A$. Then, since $X$ is reduced, $A$ is a reduced ring ([§Algebraic Structure of Schemes, ⁋Definition 1](/en/math/scheme_theory/algebra_of_schemes#def1){: data-lid="hfa23" }), and since any nonempty open subset of $\Spec A$ is also an open subset of $X$ and thus meets $U$, the intersection $U\cap \Spec A$ is dense in $\Spec A$. 

Now, for any $\mathfrak{p}\in U\cap \Spec A$, since the germ of $s$ in the stalk $\mathcal{O}_{X,\mathfrak{p}}=A_\mathfrak{p}$ is $0$, we have $ts=0$ for some $t\in A\setminus \mathfrak{p}$, and since $\mathfrak{p}$ is a prime ideal, this yields $s\in \mathfrak{p}$. That is, $U\cap \Spec A\subseteq Z(s)$; since $Z(s)$ is closed and $U\cap \Spec A$ is dense, we have $Z(s)=\Spec A$, which means that $s$ belongs to every prime ideal of $A$. Therefore, by the first result of [§The Spectrum, ⁋Proposition 14](/en/math/scheme_theory/spectrums#prop14){: data-lid="2z242" }, we have $s\in \mathfrak{N}(A)=0$. Since this holds for any affine open subset of $X$, we obtain $s=0$. 
:::

In this lemma, the assumption that the scheme is reduced cannot be omitted. For $X=\Spec \mathbb{K}[\x_1,\x_2]/(\x_2^2,\x_1\x_2)$ in [§Algebraic Structure of Schemes, ⁋Example 11](/en/math/scheme_theory/algebra_of_schemes#ex11){: data-lid="0kdfs" }, the nilradical is the prime ideal $(\x_2)$, so $X$ is irreducible ([§Algebraic Structure of Schemes, ⁋Lemma 3](/en/math/scheme_theory/algebra_of_schemes#lem3){: data-lid="oamsz" }), and therefore the nonempty open subset $D(\x_1)$ is dense. However, from $\x_1\x_2=0$, making $\x_1$ invertible yields $\x_2\vert_{D(\x_1)}=0$, so a non-$0$ function vanishes on a dense open subset. Requiring the domain of a rational function to contain *all* associated points in [§Algebraic Structure of Schemes, ⁋Definition 12](/en/math/scheme_theory/algebra_of_schemes#def12){: data-lid="hdduv" } was precisely intended to prevent this.

On the other hand, there are largely two conditions that the domain $U$ of a rational map can satisfy. One is to take $U$ to be a dense open subset, just as in classical algebraic geometry ([\[Algebraic Varieties\] §Rational Maps, ⁋Definition 5](/en/math/algebraic_varieties/rational_maps#def5){: data-lid="gfgtb" }), and the other is to view a rational map as a generalization of [§Algebraic Structure of Schemes, ⁋Definition 12](/en/math/scheme_theory/algebra_of_schemes#def12){: data-lid="z9q6s" } and impose the condition that it contains all associated points. As seen above, for a non-reduced scheme, requiring it to be a dense open subset is generally a weaker condition than requiring it to contain all associated points; however, for a locally Noetherian reduced scheme, these two conditions coincide. To verify this, we first show that in $X$, every irreducible component $C$ has a generic point (since $C$ meets an affine open subset $\Spec A$, it suffices to take the closure in $X$ of the point obtained by applying [§The Spectrum, ⁋Proposition 16](/en/math/scheme_theory/spectrums#prop16){: data-lid="t7163" }), and from this deduce that an open subset of $X$ is dense if and only if it contains the generic point of every irreducible component of $X$. Then, for a reduced ring $A$, the associated points of $\Spec A$ are always minimal prime ideals, that is, the generic points of the irreducible components; conversely, since we have already verified in [§Algebraic Structure of Schemes, §§Associated Primes](/en/math/scheme_theory/algebra_of_schemes#associated-primes){: data-lid="70q0l" } that the minimal prime ideals of a Noetherian ring are always associated prime ideals, these two conditions coincide.

::: Definition 22
A *rational map* from a scheme $X$ to a scheme $Y$ is an equivalence class of pairs $(U,\alpha)$ consisting of a dense open subset $U$ of $X$ and a morphism of schemes $\alpha: U \rightarrow Y$. Here, two pairs $(U,\alpha)$ and $(V,\beta)$ are equivalent if there exists an open subset $W$ contained in $U\cap V$ and dense in $X$ such that $\alpha\vert_W=\beta\vert_W$. 
:::

A rational map is written with a dashed arrow as $\varphi: X \dashrightarrow Y$, where the dashed arrow indicates that $\varphi$ may not be defined at all points of $X$. That the above definition is indeed an equivalence relation is because the intersection of two dense open subsets is again a dense open subset; while this is a weaker condition than the classical requirement that two representatives agree on the entirety of $U\cap V$ ([\[Algebraic Varieties\] §Rational Maps, ⁋Definition 5](/en/math/algebraic_varieties/rational_maps#def5){: data-lid="ts2qm" }), the two coincide if $X$ is reduced and $Y=\Spec B$ is affine. This is because two morphisms $\alpha,\beta: U\cap V \rightarrow Y$ correspond by [§Affine Scheme, ⁋Theorem 13](/en/math/scheme_theory/affine_schemes#thm13){: data-lid="ntsan" } to ring homomorphisms $B \rightarrow \Gamma(U\cap V, \mathcal{O}_X)$, and since $U\cap V$ is a reduced scheme and $W$ is dense in it, $\Gamma(U\cap V, \mathcal{O}_X) \rightarrow \Gamma(W, \mathcal{O}_X)$ is injective by [Lemma 21](#lem21){: data-lid="xv4yz" }.

A rational map $\varphi: X \dashrightarrow Y$ is *dominant* if its representative $(U,\alpha)$ is a dominant morphism in the sense of [Definition 19](#def19){: data-lid="n41f7" }. This does not depend on the choice of representative, because if $W\subseteq U$ is an open subset dense in $X$, then $W$ is dense in $U$ as well, and since $\alpha$ is continuous, $\cl(\alpha(U))=\cl(\alpha(W))$ holds. The reason dominant rational maps are important becomes apparent when composing two rational maps $\varphi: X\dashrightarrow Y$ and $\psi: Y \dashrightarrow Z$. Let us choose representatives $(U,\alpha)$ and $(V,\beta)$ of the two rational maps. Then the actual domain of their composition $\beta\circ \alpha$ is the part where $\alpha$ enters the domain of the latter function, namely $\alpha^{-1}(V)$, so for this map to define a rational map, $\alpha^{-1}(V)$ must be dense in $X$. A condition that can naturally be required then is the dominance of $\alpha$; requiring this ensures that $\alpha(U)$ meets $V$, so $\alpha^{-1}(V)$ does not become empty. However, in the world of schemes, this condition is still somewhat insufficient. For example, if we let $X$ be the disjoint union of $\mathbb{A}^1_\mathbb{K}$ and $\Spec\mathbb{K}$, let $Y=\mathbb{A}^1_\mathbb{K}$, and let $\alpha$ be the morphism that is the identity map on the first component and sends the second component to a closed point $p$, then $\alpha$ is dominant, but for $V=Y\setminus \{p\}$, $\alpha^{-1}(V)$ is only $\mathbb{A}^1_\mathbb{K}\setminus\{p\}$ in the first component, which fails to meet the second component, a nonempty open subset of $X$. This problem arises because $X$ is split into multiple pieces; if $X$ is irreducible, every nonempty open subset is dense, so this problem disappears. Moreover, since we have already seen in the counterexample immediately following [Lemma 21](#lem21){: data-lid="4tgvc" } that $X$ needs to be reduced, for convenience we consider the case where $X,Y$ are both integral schemes. ([§Algebraic Structure of Schemes, ⁋Proposition 4](/en/math/scheme_theory/algebra_of_schemes#prop4){: data-lid="kelfx" }) Then, in this case, for a dominant rational map $\varphi: X\dashrightarrow Y$ and an arbitrary rational map $\psi: Y \dashrightarrow Z$, their composition $\psi\circ\varphi$ is well-defined by the representative $(\alpha^{-1}(V), \beta\circ \alpha)$, and it is not difficult to show that this does not depend on the choice of representatives.

::: Definition 23
For integral schemes $X, Y$, a dominant rational map $\varphi: X \dashrightarrow Y$ is a *birational map* if there exists a dominant rational map $\psi: Y \dashrightarrow X$ such that $\psi\circ\varphi$ and $\varphi\circ\psi$ are equal to the rational maps defined by $\id_X$ and $\id_Y$, respectively. Two integral schemes $X, Y$ are said to be *birationally equivalent* if there exists such a birational map $\varphi: X\dashrightarrow Y$. 
:::

If an isomorphism means that two schemes have completely identical structures, birational equivalence means that two schemes have the same structure on dense open subsets. The following proposition makes this precise.

::: Proposition 24
For integral schemes $X, Y$, given a dominant rational map $\varphi: X \dashrightarrow Y$, the following two conditions are equivalent.

1. $\varphi$ is a birational map. 
2. There exist a non-empty open subset of $X$, $\widetilde{U}$, and a non-empty open subset of $Y$, $\widetilde{V}$, such that an isomorphism $\widetilde{U} \rightarrow \widetilde{V}$ is a representative of $\varphi$. 
:::
::: Proof
First, suppose that $\varphi$ is a birational map, and choose a representative of $\varphi$, $(U,\alpha)$, and a representative of $\psi$ playing that role, $(V,\beta)$. Then, from $\psi\circ\varphi=\id_X$, there exists a non-empty open subset of $X$, $W_1\subseteq \alpha^{-1}(V)$, such that $(\beta\circ \alpha)\vert_{W_1}=\id_{W_1}$, and from $\varphi\circ\psi=\id_Y$, there exists a non-empty open subset of $Y$, $W_2\subseteq \beta^{-1}(U)$, such that $(\alpha\circ \beta)\vert_{W_2}=\id_{W_2}$. Now, we set

$$\widetilde{U}=W_1\cap \alpha^{-1}(W_2),\qquad \widetilde{V}=W_2\cap \beta^{-1}(W_1)$$

Since $W_1$ is dense in $U$ and $\varphi$ is dominant, $\cl(\alpha(W_1))=\cl(\alpha(U))=Y$, and therefore the non-empty open subset $W_2$ meets $\alpha(W_1)$, so that $\widetilde{U}\neq\emptyset$. 

In $\widetilde{U}$, for any point $x$, we have $\alpha(x)\in W_2$, and since $x\in W_1$, it follows that $\beta(\alpha(x))=x\in W_1$, that is, $\alpha(x)\in \beta^{-1}(W_1)$. Thus $\alpha(\widetilde{U})\subseteq \widetilde{V}$, and in the same way, in $\widetilde{V}$, for any point $y$, we have $\beta(y)\in W_1$ and $\alpha(\beta(y))=y\in W_2$, so $\beta(\widetilde{V})\subseteq \widetilde{U}$. For the two morphisms $\alpha\vert_{\widetilde{U}}: \widetilde{U} \rightarrow \widetilde{V}$ and $\beta\vert_{\widetilde{V}}: \widetilde{V} \rightarrow \widetilde{U}$ obtained this way, their compositions are the identity maps by $\widetilde{U}\subseteq W_1$ and $\widetilde{V}\subseteq W_2$, respectively, so $\alpha\vert_{\widetilde{U}}$ is an isomorphism, and since $\widetilde{U}$ is dense in $X$, $(\widetilde{U}, \alpha\vert_{\widetilde{U}})$ is a representative of $\varphi$. 

Conversely, suppose that an isomorphism $\alpha: \widetilde{U} \rightarrow \widetilde{V}$ is a representative of $\varphi$, and let its inverse be $\beta: \widetilde{V} \rightarrow \widetilde{U}$. Then, since $\widetilde{V}$ is dense in $Y$, the composition of $\beta$ and the inclusion map of the open subset $\widetilde{U} \hookrightarrow X$ defines a rational map $\psi: Y \dashrightarrow X$, and since $\beta$ is surjective, $\psi$ is dominant. Moreover, $\psi\circ\varphi$ restricts on $\widetilde{U}$ to $\beta\circ \alpha=\id_{\widetilde{U}}$, and $\varphi\circ\psi$ restricts on $\widetilde{V}$ to $\alpha\circ \beta=\id_{\widetilde{V}}$, so these two are equal to the rational maps defined by $\id_X$ and $\id_Y$, respectively. 
:::

If an integral scheme $X$ is locally Noetherian, the domain of definition of a rational function in [§Algebraic Structure of Schemes, ⁋Definition 12](/en/math/scheme_theory/algebra_of_schemes#def12){: data-lid="4mrs1" } is precisely a non-empty open subset of $X$. Indeed, for a non-empty affine open subset of $X$, $\Spec A$, since $A$ is an integral domain ([§Algebraic Structure of Schemes, ⁋Definition 1](/en/math/scheme_theory/algebra_of_schemes#def1){: data-lid="8a95s" }), the annihilator of an element other than $0$ is always $(0)$, and therefore the only associated point of $\Spec A$ is $(0)$. In other words, the only associated point of $X$ is the generic point $\eta$, so the condition that the domain of definition must contain all associated points becomes equivalent to the condition that the domain of definition is non-empty. We have already seen that the collection of rational functions $K(X)$ obtained in this way coincides with $\mathcal{O}_{X,\eta}\cong\Frac A$ and forms a field ([§Algebraic Structure of Schemes, §§Rational Functions](/en/math/scheme_theory/algebra_of_schemes#rational-functions){: data-lid="xindv" }), and we call this the *function field* of $X$.

::: Corollary 25
For two birationally equivalent integral locally Noetherian schemes $X, Y$, we have $K(X)\cong K(Y)$. 
:::
::: Proof
By [Proposition 24](#prop24){: data-lid="uarkc" }, there exists a birational map having an isomorphism $\alpha: \widetilde{U} \rightarrow \widetilde{V}$ as a representative. Since the generic point of $X$, $\eta_X$, belongs to the non-empty open subset $\widetilde{U}$ and stalks do not change under restriction to an open subscheme, $K(X)=\mathcal{O}_{X,\eta_X}=\mathcal{O}_{\widetilde{U}, \eta_X}$, and for the same reason, $K(Y)=\mathcal{O}_{\widetilde{V}, \eta_Y}$. Meanwhile, since $\widetilde{V}$ is a non-empty open subset of $Y$, its generic point is $\eta_Y$, and since $\alpha$ is an isomorphism, $\alpha(\eta_X)=\eta_Y$. Therefore, the isomorphism between stalks induced by $\alpha$ gives $K(X)\cong K(Y)$. 
:::

That is, birational equivalence preserves function fields. In the case of varieties, we verified in [\[Algebraic Varieties\] §Rational Maps, ⁋Proposition 10](/en/math/algebraic_varieties/rational_maps#prop10){: data-lid="rn1qn" } that the converse also holds. 

---

**References**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).
