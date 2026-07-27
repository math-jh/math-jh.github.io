---
title: "Properties of Scheme Morphisms"
description: "This post defines the main properties of scheme morphisms and introduces the concepts and basic properties of quasi-compact and quasi-separated morphisms."
excerpt: "Basic properties of scheme morphisms: affine, finite, finite type"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/properties_of_scheme_morphisms
sidebar: 
    nav: "scheme_theory-en"

date: 2025-02-21
weight: 9
translated_at: 2026-07-18T23:30:03+00:00
translation_source: kimi-cli
last_polished_at: 2026-07-18T23:30:03+00:00
---
In the previous post, we examined several perspectives for understanding scheme morphisms. In this post, we begin in earnest to define the properties that scheme morphisms can have. First, we define the following property shared by all of them.

::: Definition 1
A property $P$ of scheme morphisms is said to be *local on target* if the following two conditions hold.
1. If a scheme morphism $\varphi:X \rightarrow Y$ satisfies $P$, then for any open subscheme $V$ of $Y$, the scheme morphism $\varphi\vert_{\varphi^{-1}(V)}: \varphi^{-1}(V) \rightarrow V$ also satisfies $P$.
2. If for a scheme morphism $\varphi:X \rightarrow Y$, there exists an open covering $\{V_j\}$ of $Y$ such that $\varphi\vert_{\varphi^{-1}(V_j)}: \varphi^{-1}(V_j) \rightarrow V_j$ all satisfy $P$, then $\varphi$ also satisfies $P$.
:::

Schemes are built from affine schemes. If a property $P$ of scheme morphisms is local on target, we may assume the target $Y$ of a scheme morphism $\varphi:X \rightarrow Y$ is $\Spec B$, and then via the adjunction

$$\Hom_\Sch(X, \Spec B)\cong \Hom_\cRing(B, \Gamma(X, \mathcal{O}_X))$$

we can define the property of a scheme morphism $X \rightarrow \Spec B$ through the property of the corresponding ring homomorphism $B \rightarrow \Gamma(X, \mathcal{O}_X)$.

## Quasi-Compact and Quasi-Separated Morphisms

::: Definition 2
A scheme morphism $\varphi: X \rightarrow Y$ is called *quasi-compact* if for any affine open subset $V\subseteq Y$, the preimage $\varphi^{-1}(V)$ is quasi-compact.
:::

::: Proposition 3
A scheme morphism $\varphi: X \rightarrow Y$ is quasi-compact if and only if the preimage of any quasi-compact open subset of $Y$ is quasi-compact.
:::
::: Proof
Since any affine scheme is quasi-compact ([§Spectrums, ⁋Lemma 12](/en/math/scheme_theory/spectrums#lem12)), it is obvious that the given condition implies the condition of [Definition 2](#def2).

Conversely, suppose a quasi-compact morphism $\varphi: X \rightarrow Y$ is given. Now, given any quasi-compact open subset $V$ of $Y$, there exists a covering $\{V_j\}$ of $V$ by finitely many affine open subsets, and their preimages $\varphi^{-1}(V_j)$ are all quasi-compact. Now

$$\varphi^{-1}(V)=\varphi^{-1}\left(\bigcup_{j\in J} V_j\right)=\bigcup_{j\in J}\varphi^{-1}(V_j)$$

and since a finite union of quasi-compact sets is again quasi-compact, we obtain the desired result.
:::

Then from the equivalence of [Proposition 3](#prop3), we know that the composition of any quasi-compact morphisms is again quasi-compact. Moreover, the following holds.

::: Proposition 4
For a Noetherian scheme $X$, any scheme morphism $\varphi: X \rightarrow Y$ is always quasi-compact.
:::
::: Proof
Given any affine open subset $V\subseteq Y$, we must show that $\varphi^{-1}(V)$ is quasi-compact. But from the first result of [[Topology] §Dimension, ⁋Proposition 12](/en/math/topology/dimension#prop12) and [[Topology] §Dimension, ⁋Proposition 13](/en/math/topology/dimension#prop13), any subspace of a Noetherian topological space is quasi-compact.
:::

Similarly, we define a quasi-separated morphism. For this, we must first define a quasi-separated scheme.

::: Definition 5
A scheme $X$ is *quasi-separated* if the intersection of any two quasi-compact open subsets of $X$ is again quasi-compact. A scheme morphism $\varphi: X \rightarrow Y$ is *quasi-separated* if for any affine open set $V\subseteq Y$, the preimage $\varphi^{-1}(V)$ is quasi-separated.
:::

Then the following holds.

::: Proposition 6
A locally Noetherian scheme is always quasi-separated.
:::
::: Proof
Given any two affine open subsets $V_1=\Spec B_1, V_2=\Spec B_2$ of a locally Noetherian scheme $X$, we must show that $V_1\cap V_2$ is quasi-compact.

First, since $X$ is locally Noetherian, we can cover $X$ by spectra $U_i=\Spec A_i$ of Noetherian rings. Now for each $i$, by [§Topology of Schemes, ⁋Lemma 11](/en/math/scheme_theory/topology_of_schemes#lem11), we can cover $U_i\cap V_1$ by spectra $\Spec (A_i)_g$ of Noetherian rings. Collecting all of these, we can cover $V_1$ by spectra of Noetherian rings, and by [§Spectrums, ⁋Lemma 12](/en/math/scheme_theory/spectrums#lem12), $V_1=\Spec B_1$ is covered by finitely many spectra of Noetherian rings. Therefore, by [§Topology of Schemes, ⁋Lemma 13](/en/math/scheme_theory/topology_of_schemes#lem13), $B_1$ is a Noetherian ring and thus $V_1=\Spec B_1$ is Noetherian. Again, from the first result of [[Topology] §Dimension, ⁋Proposition 12](/en/math/topology/dimension#prop12) and [[Topology] §Dimension, ⁋Proposition 13](/en/math/topology/dimension#prop13), any subspace of a Noetherian topological space is quasi-compact, so in particular $V_1\cap V_2$ is also quasi-compact. By the same logic, any affine open of $X$ is Noetherian, and a quasi-compact open is a finite union of affine opens, so it is also Noetherian. Since a subspace of a Noetherian topological space is quasi-compact, the intersection of any two quasi-compact opens is also quasi-compact, and thus by [Definition 5](#def5), $X$ is quasi-separated.
:::

Then not only do quasi-compactness and quasi-separatedness satisfy the property of [Definition 1](#def1), but as we can check in the following proposition, they are *affine-local on target*. ([§Topology of Schemes, ⁋Definition 9](/en/math/scheme_theory/topology_of_schemes#def9))

::: Proposition 7
For a scheme morphism $\varphi: X \rightarrow Y$, the following hold.

1. If there exists an affine open covering $\{V_j\}$ of $Y$ such that each $\varphi^{-1}(V_j)$ is quasi-compact, then $\varphi$ is quasi-compact.
2. If there exists an affine open covering $\{V_j\}$ of $Y$ such that each $\varphi^{-1}(V_j)$ is quasi-separated, then $\varphi$ is quasi-separated.
:::
::: Proof
1. Given any affine open subset $V$ of $Y$. Then by [§Topology of Schemes, ⁋Lemma 11](/en/math/scheme_theory/topology_of_schemes#lem11), we can cover $V\cap V_j$ by open subsets that are principal open sets in both $V$ and $V_j$, and considering these for all $j$ and using the quasi-compactness of $V$, we can choose only finitely many of them. Let this be $V=\bigcup W_l$.   
    On the other hand, for each $j$, since $\varphi^{-1}(V_j)$ is quasi-compact, we can cover it by finitely many affine open subsets $U_{jk}$, and now $\varphi^{-1}(W_l)\cap U_{jk}$ is a principal open set of $U_{jk}$ by [§Spectrums, ⁋Proposition 8](/en/math/scheme_theory/spectrums#prop8), so we can express each $\varphi^{-1}(W_l)$ as a finite union of affine open sets, and therefore $\varphi^{-1}(V)$ can also be expressed as a finite union of affine open sets. Now since a finite union of quasi-compact spaces is quasi-compact, we obtain the desired result.
2. This also follows in the same manner as the first result, using [§Topology of Schemes, ⁋Lemma 11](/en/math/scheme_theory/topology_of_schemes#lem11) to cover any affine open subset $V=\Spec B$ by principal open subsets whose preimages are quasi-separated, and then proving.
:::

## Affine Morphisms

From the adjunction

$$\Hom_\Sch(X, \Spec B)\cong\Hom_\cRing (B, \Gamma(X, \mathcal{O}_X))$$

we know that in the special case where $X=\Spec A$,

$$\Hom_\Sch(\Spec A,\Spec B)\cong\Hom_\cRing (B, A)$$

holds. ([§Affine Schemes, ⁋Proposition 11](/en/math/scheme_theory/affine_schemes#prop11)) Therefore, when examining properties of scheme morphisms that are affine-local on target as above, for any affine open subset $V\cong\Spec B$ of $Y$, $U=\varphi^{-1}(V)$ is also an open subscheme $U\cong \Spec A$ of $X$, and thus $\varphi\vert_U: U \rightarrow V$ becomes a morphism between affine schemes, so we would like to obtain this property from the ring homomorphism

$$(\varphi\vert_U)^\sharp(V): \mathcal{O}_V(V) \rightarrow \mathcal{O}_U(U)$$

However, of course, for an arbitrary scheme morphism $\varphi: X \rightarrow Y$, the preimage of an affine open subset of $Y$ need not be affine. ([§Schemes, ⁋Example 8](/en/math/scheme_theory/schemes#ex8))

::: Definition 8
A scheme morphism $\varphi: X \rightarrow Y$ is called *affine* if for any affine open subset $V$ of $Y$, the preimage $\varphi^{-1}(V)$ is an affine open subset of $X$.
:::

That the composition of affine morphisms is affine is obvious. Moreover, this property also satisfies the property of [Definition 1](#def1), and we prove this in the following proposition.

::: Proposition 9
For a scheme morphism $\varphi:X \rightarrow Y$, if there exists an affine open covering $\{V_j\}$ of $Y$ such that each $\varphi^{-1}(V_j)$ is affine, then $\varphi$ is affine.
:::
::: Proof
Define the property $P$ for an affine open subset $\Spec B$ of $Y$ as "$\varphi^{-1}(\Spec B)$ is an affine open subset of $X$". Then $\varphi$ being affine means that any affine open subset of $Y$ satisfies $P$, and the given assumption means that some affine open covering of $Y$ satisfies $P$, so by the equivalence between the second and third conditions of [§Topology of Schemes, ⁋Lemma 12](/en/math/scheme_theory/topology_of_schemes#lem12), it suffices to show that $P$ is an affine-local property in the sense of [§Topology of Schemes, ⁋Definition 9](/en/math/scheme_theory/topology_of_schemes#def9). In what follows, we write the component of the sheaf morphism $\varphi^\sharp: \mathcal{O}_Y \rightarrow \varphi_\ast \mathcal{O}_X$ at an open set $V$ as $\varphi^\sharp(V): \mathcal{O}_Y(V) \rightarrow \mathcal{O}_X(\varphi^{-1}(V))$.

First, let us verify the first condition of [§Topology of Schemes, ⁋Definition 9](/en/math/scheme_theory/topology_of_schemes#def9). If $\varphi^{-1}(\Spec B)$ is an affine open subset $\Spec A$, then by [§Affine Schemes, ⁋Proposition 11](/en/math/scheme_theory/affine_schemes#prop11), $\Spec A \rightarrow \Spec B$ is of the form $\Spec\phi$ for some ring homomorphism $\phi: B \rightarrow A$, and from the formula

$$(\Spec\phi)^{-1}(D(f))=D(\phi(f))$$

obtained in the proof of [§Spectrums, ⁋Proposition 8](/en/math/scheme_theory/spectrums#prop8), for any $f\in B$ we have $\varphi^{-1}(\Spec B_f)=D(\phi(f))\cong\Spec A_{\phi(f)}$, so $\Spec B_f$ also satisfies $P$.

Now we must verify the second condition. That is, assuming $B=(f_1,\ldots, f_r)$ and each $U_i=\varphi^{-1}(D(f_i))$ is affine, we must show that $U=\varphi^{-1}(\Spec B)$ is affine. For convenience, let $R=\Gamma(U, \mathcal{O}_X)$ and let $g_i\in R$ be the image of $f_i$ under $\varphi^\sharp(\Spec B): B \rightarrow R$. Also, for $g\in \Gamma(U, \mathcal{O}_X)$, let $U_g$ denote the set of points $x$ where the stalk of $g$ does *not* belong to the maximal ideal of $\mathcal{O}_{X,x}$. Then for any affine open subset $\Spec A$ of $U$, it is obvious by definition that $U_g\cap \Spec A=D(g\vert_{\Spec A})$, and in particular $U_g$ is an open set.

We observe the following three things. First, since $B=(f_1,\ldots, f_r)$, we have $\Spec B=\bigcup_{i=1}^rD(f_i)$ and thus $\{U_i\}_{i=1}^r$ is a finite affine open covering of $U$. Moreover, choosing $b_i\in B$ with $1=\sum_{i=1}^rb_if_i$ and applying $\varphi^\sharp(\Spec B)$, we know that $g_1,\ldots, g_r$ generate the unit ideal of $R$. Second, since $\varphi$ is a morphism of locally ringed spaces, for each $x\in U$, $\varphi^\sharp_x:\mathcal{O}_{Y,\varphi(x)} \rightarrow \mathcal{O}_{X,x}$ is a local homomorphism, and thus $\varphi(x)\in D(f_i)$ is equivalent to $x\in U_{g_i}$, so $U_i=U_{g_i}$. Third, letting $U_i\cong \Spec A_i$ and letting $\phi_i$ be the ring homomorphism corresponding to $\Spec A_i \rightarrow \Spec B_{f_i}$, since $D(f_j)\cap D(f_i)$ is a principal open set of $\Spec B_{f_i}$, we apply [§Spectrums, ⁋Proposition 8](/en/math/scheme_theory/spectrums#prop8) as above to see that $U_i\cap U_j$ is a principal open set of $\Spec A_i$, hence in particular affine.

Now we show that for each $i$, the canonical map $R_{g_i} \rightarrow \Gamma(U_{g_i}, \mathcal{O}_X)$ is an isomorphism. The two conditions of [[Topology] §Sheaves, ⁋Definition 1](/en/math/topology/sheaves#def1) for the open covering $\{U_j\}_{j=1}^r$ of $U$ are equivalent to the existence of the following exact sequence

$$0 \rightarrow R \rightarrow \bigoplus_{j=1}^r \mathcal{O}_X(U_j) \rightarrow \bigoplus_{j,k=1}^r \mathcal{O}_X(U_j\cap U_k)$$

Here the second map is $(s_j)_j\mapsto (s_j\vert_{U_j\cap U_k}-s_k\vert_{U_j\cap U_k})_{j,k}$. This is an exact sequence of $R$-modules, and since the direct sum is finite, by [[Commutative Algebra] §Properties of Localization, ⁋Proposition 2](/en/math/commutative_algebra/properties_of_localization#prop2), exactness is preserved upon localizing at $g_i$, yielding the following exact sequence

$$0 \rightarrow R_{g_i} \rightarrow \bigoplus_{j=1}^r \mathcal{O}_X(U_j)_{g_i} \rightarrow \bigoplus_{j,k=1}^r \mathcal{O}_X(U_j\cap U_k)_{g_i}$$

(Here the localization of $\mathcal{O}_X(U_j)$ means the localization at the restriction of $g_i$ to $U_j$.) On the other hand, since $U_j$ and $U_j\cap U_k$ are both affine and for an affine scheme $\Spec A$ and $a\in A$, we have $\mathcal{O}_{\Spec A}(D(a))=A_a$ ([§Schemes, ⁋Lemma 2](/en/math/scheme_theory/schemes#lem2)), from $U_g\cap \Spec A=D(g\vert_{\Spec A})$ observed above we obtain

$$\mathcal{O}_X(U_j)_{g_i}=\mathcal{O}_X(U_j\cap U_{g_i}),\qquad \mathcal{O}_X(U_j\cap U_k)_{g_i}=\mathcal{O}_X(U_j\cap U_k\cap U_{g_i})$$

But the exact sequence thus obtained is precisely the exact sequence given by the sheaf condition for the open covering $\{U_j\cap U_{g_i}\}_{j=1}^r$ of $U_{g_i}$, so both $R_{g_i}$ and $\Gamma(U_{g_i}, \mathcal{O}_X)$ become the kernel of the same map, and thus the canonical map $R_{g_i} \rightarrow \Gamma(U_{g_i}, \mathcal{O}_X)$ is an isomorphism.

Finally, in the adjunction

$$\Hom_\Sch(U, \Spec R)\cong \Hom_\cRing(R, \Gamma(U, \mathcal{O}_X))$$

of [§Affine Schemes, ⁋Theorem 13](/en/math/scheme_theory/affine_schemes#thm13), consider the scheme morphism $\psi: U \rightarrow \Spec R$ corresponding to $\id_R$. Since $\psi$ is also a morphism of locally ringed spaces, for each $x\in U$, $\psi^\sharp_x$ is a local homomorphism, and the composition $R \rightarrow \mathcal{O}_{\Spec R, \psi(x)} \rightarrow \mathcal{O}_{X,x}$ is the canonical map $R=\Gamma(U, \mathcal{O}_X) \rightarrow \mathcal{O}_{X,x}$, so $\psi(x)$ is the preimage of the maximal ideal of $\mathcal{O}_{X,x}$ under this canonical map. Therefore

$$\psi^{-1}(D(g_i))=U_{g_i}=U_i$$

and $\psi\vert_{U_i}: U_i \rightarrow D(g_i)\cong \Spec R_{g_i}$ is a morphism between affine schemes corresponding to the isomorphism $R_{g_i}\cong \Gamma(U_i, \mathcal{O}_X)$ just obtained, so by [§Affine Schemes, ⁋Proposition 11](/en/math/scheme_theory/affine_schemes#prop11) it is an isomorphism. Now since the $g_i$ generate the unit ideal of $R$, $\{D(g_i)\}$ covers $\Spec R$ and $\{U_i\}$ covers $U$, so $\psi$ is an isomorphism. That is, $U\cong\Spec R$ is affine.
:::

## Finite, Integral, and Finite Type Morphisms

::: Definition 10
A scheme morphism $\varphi:X \rightarrow Y$ is *finite* if $\varphi$ is affine and, for any affine open subset $V$ of $Y$, the ring homomorphism

$$(\varphi\vert_{\varphi^{-1}(V)})^\sharp(V): \mathcal{O}_V(V) \rightarrow \mathcal{O}_{\varphi^{-1}(V)}(\varphi^{-1}(V))$$

is a finite ring homomorphism. ([[Commutative Algebra] §Integral Extension, ⁋Definition 3](/en/math/commutative_algebra/integral_extension#def3))
:::

To aid understanding, let us write an affine open subset $V\subseteq Y$ as $\Spec B$. Then from the assumption that $\varphi$ is affine, $U=\varphi^{-1}(V)$ is an affine open subset of $X$, and thus there exists $A$ such that $U\cong\Spec A$. Through this identification, the scheme morphism $\varphi\vert_U: U \rightarrow V$ is the same as the morphism $\Spec A \rightarrow \Spec B$ between spectra, and now $\varphi$ being finite means that the ring homomorphism $B \rightarrow A$ corresponding to this morphism is finite. Similarly, we define the following.

::: Definition 11
A scheme morphism $\varphi:X \rightarrow Y$ is *integral* if $\varphi$ is affine and, for any affine open subset $V$ of $Y$, the ring homomorphism

$$(\varphi\vert_{\varphi^{-1}(V)})^\sharp(V): \mathcal{O}_V(V) \rightarrow \mathcal{O}_{\varphi^{-1}(V)}(\varphi^{-1}(V))$$

is an integral ring homomorphism. ([[Commutative Algebra] §Integral Extension, ⁋Definition 3](/en/math/commutative_algebra/integral_extension#def3))
:::

From their definitions, we know that finite morphisms and integral morphisms are closed under composition. Also, that they satisfy the condition of [Definition 1](#def1) can be seen from [[Commutative Algebra] §Integral Extension, ⁋Proposition 14](/en/math/commutative_algebra/integral_extension#prop14) and [[Commutative Algebra] §Integral Extension, ⁋Proposition 15](/en/math/commutative_algebra/integral_extension#prop15), so they are all affine-local on target.

We know from [[Commutative Algebra] §Integral Extension, ⁋Lemma 4](/en/math/commutative_algebra/integral_extension#lem4) that any finite morphism is integral. Now, to completely state this lemma in the language of algebraic geometry, we need to define finite type morphisms.

::: Definition 12
A scheme morphism $\varphi:X \rightarrow Y$ is *locally of finite type* if for any affine open subset $V$ of $Y$ and any affine open subset $U$ of $\varphi^{-1}(V)$,

$$(\varphi\vert_{U})^\sharp(V): \mathcal{O}_V(V) \rightarrow \mathcal{O}_U(U)$$

is of finite type. ([[Commutative Algebra] §Integral Extension, ⁋Definition 3](/en/math/commutative_algebra/integral_extension#def3))
:::

As before, let $V\cong \Spec B$ and $U\cong\Spec A\subseteq \varphi^{-1}(V)$. Then the scheme morphism $\varphi\vert_U: U \rightarrow V$ can be viewed as $\Spec A \rightarrow \Spec B$, and what we require is that the corresponding ring homomorphism $B \rightarrow A$ is of finite type.

Since [Definition 12](#def12) quantifies over *every* affine open subset of $\varphi^{-1}(V)$, we must separately show that checking a single affine open covering suffices. This is the content of the following lemma.

::: Lemma 13
Let $\varphi: W \rightarrow \Spec B$ be a scheme morphism, and suppose there is an affine open covering $\{\Spec A_i\}$ of $W$ such that each $B \rightarrow A_i$ is of finite type. Then for *every* affine open subset $U$ of $W$, the homomorphism $B \rightarrow \mathcal{O}_W(U)$ is also of finite type.
:::
::: Proof
Define the property $Q$ of an affine open subset $\Spec R\subseteq W$ to be "$B \rightarrow R$ is of finite type", and let us show that $Q$ is an affine-local property in the sense of [§Topology of Schemes, ⁋Definition 9](/en/math/scheme_theory/topology_of_schemes#def9). Since the given covering $\{\Spec A_i\}$ satisfies $Q$, the second condition of [§Topology of Schemes, ⁋Lemma 12](/en/math/scheme_theory/topology_of_schemes#lem12) then gives the desired result.

The first condition is immediate, since if $B \rightarrow R$ is of finite type then adjoining $1/h$ to a set of generators of $R$ makes $R_h$ finitely generated as a $B$-algebra. For the second condition, suppose $R=(h_1,\ldots, h_m)$ and each $B \rightarrow R_{h_t}$ is of finite type. For each $t$, choose a finite set generating $R_{h_t}$ as a $B$-algebra and clear denominators, so that there are elements $x_{t1},\ldots, x_{tn_t}$ of $R$ for which $R_{h_t}$ is generated as a $B$-algebra by the $x_{tk}/1$ together with $1/h_t$. Also choose $a_t\in R$ with $1=\sum_{t=1}^ma_th_t$. Now let $R'$ be the $B$-subalgebra of $R$ generated by the finite set $\{h_t\}\cup\{a_t\}\cup\{x_{tk}\}$; since $R'$ is a finite type $B$-algebra, it suffices to show $R'=R$. For any $x\in R$, the element $x/1$ of $R_{h_t}$ is a polynomial in the $x_{tk}/1$ and $1/h_t$ with coefficients in $B$, so $x/1=r_t/h_t^{n_t}$ for some $r_t\in R'$ and $n_t\geq 0$, and hence $h_t^{N_t}(h_t^{n_t}x-r_t)=0$ in $R$ for some $N_t$, that is, $h_t^{N_t+n_t}x=h_t^{N_t}r_t\in R'$. As there are finitely many $t$, we may choose a common $M$ with $h_t^Mx\in R'$ for all $t$. On the other hand, $a_t,h_t\in R'$ in $1=\sum_ta_th_t$, so $h_1,\ldots, h_m$ generate the unit ideal of $R'$, and raising this identity to a sufficiently large power shows that $h_1^M,\ldots, h_m^M$ also generate the unit ideal of $R'$. That is, there are $c_t\in R'$ with $1=\sum_tc_th_t^M$, and therefore

$$x=\sum_{t=1}^mc_t(h_t^Mx)\in R'$$

as desired.
:::

Then finite type morphisms are defined as follows.

::: Definition 14
A scheme morphism $\varphi:X \rightarrow Y$ is a *morphism of finite type* if $\varphi$ is a quasi-compact morphism locally of finite type.
:::

From the definition, it is clear that a morphism locally of finite type is affine-local on target. Also, since a quasi-compact morphism is affine-local on target by [Proposition 7](#prop7), a finite type morphism is also affine-local on target.

Then by [[Commutative Algebra] §Integral Extension, ⁋Lemma 4](/en/math/commutative_algebra/integral_extension#lem4), the following holds.

::: Proposition 15
A scheme morphism $\varphi:X \rightarrow Y$ is finite if and only if $\varphi$ is an integral morphism (locally) of finite type.
:::
::: Proof
One direction is obvious. For the converse, first from the assumption that $\varphi$ is integral, we know that for any affine open subset $V\subseteq Y$, the preimage $\varphi^{-1}(V)$ is an affine open subset of $X$, and then we apply [[Commutative Algebra] §Integral Extension, ⁋Lemma 4](/en/math/commutative_algebra/integral_extension#lem4) to the ring map thus obtained.
:::

In the above proposition, since $\varphi$ is an integral morphism, it is an affine morphism, and thus a quasi-compact morphism ([§Spectrums, ⁋Lemma 12](/en/math/scheme_theory/spectrums#lem12)), so whether $\varphi$ is of finite type or locally of finite type becomes the same assumption.

::: Example 16
Let us look at examples of the morphisms we have examined in this section. In the world of affine schemes, this is nothing more than looking at the examples of [[Commutative Algebra] §Integral Extension, ⁋Definition 3](/en/math/commutative_algebra/integral_extension#def3). The purpose of this example is to give geometric intuition for these.

First, for an algebraically closed field $\mathbb{K}$, considering the ring map $\iota:\mathbb{K}[\x] \rightarrow \mathbb{K}[\x,\y]$, we see that $\mathbb{K}[\x,\y]$ is generated as a $\mathbb{K}[\x]$-algebra by a single element $\y$, so it is a finite type ring homomorphism, but it is not a finite ring homomorphism since it is not finitely generated as a $\mathbb{K}[\x]$-module.

Now consider the scheme morphism $\Spec\iota: \Spec \mathbb{K}[\x,\y] \rightarrow\Spec \mathbb{K}[\x]$ corresponding to this. This is the function that takes any prime ideal $\mathfrak{p}\subseteq \mathbb{K}[\x,\y]$ and outputs the prime ideal $\mathfrak{p}\cap \mathbb{K}[\x]$ of $\mathbb{K}[\x]$. Geometrically, this is the function that corresponds a point $(x,y)$ of the affine plane $\mathbb{A}^2_\mathbb{K}$ to the point $x$ of the affine line $\mathbb{A}^1_\mathbb{K}$.

{% diagram Math/Scheme_Theory/Properties_of_Scheme_Morphisms-1.svg width="28.04em" alt="finite_type_morphism" %}

As a related example of a finite morphism, there is the composition of the above ring homomorphism $\iota:\mathbb{K}[\x]\rightarrow \mathbb{K}[\x,\y]$ with the projection map $\pi:\mathbb{K}[\x,\y] \rightarrow \mathbb{K}[\x,\y]/(\x-\y^2)$. Then $\mathbb{K}[\x,\y]/(\x-\y^2)$ is generated as a $\mathbb{K}[\x]$-module by $1$ and $\y$, so $\phi:\mathbb{K}[\x] \rightarrow \mathbb{K}[\x,\y]/(\x-\y^2)$ is a finite morphism.

On the other hand, we know that the ring homomorphism $\pi:A \rightarrow A/\mathfrak{a}$ geometrically corresponds to the inclusion of the closed subset defined by $\mathfrak{a}$. Therefore, the scheme morphism

$$\Spec\phi: \Spec \frac{\mathbb{K}[\x,\y]}{(\x-\y^2)}\rightarrow \Spec \mathbb{K}[\x,\y] \rightarrow \Spec\mathbb{K}[\x]$$

defined by the composition

$$\phi: \mathbb{K}[\x] \rightarrow \mathbb{K}[\x,\y] \rightarrow \mathbb{K}[\x,\y]/(\x-\y^2)$$

can be viewed geometrically as the projection from the zero set $Z(\x-\y^2)$ of $\x=\y^2$ onto the $x$-axis.

{% diagram Math/Scheme_Theory/Properties_of_Scheme_Morphisms-2.svg width="25.72em" alt="finite_morphism" %}

The geometric difference between these two examples is quite clear. In the first example, the fiber over a point of the target is an infinite set, whereas in the second example, the fiber over a point is a finite set. Algebraically, this can be checked as follows: when we take any point $\mathfrak{p}=(\x-a)$ of the target $\mathbb{A}_\mathbb{K}^1$, any $\mathfrak{q}_b=(\x-a, \y-b)\in \mathbb{A}_\mathbb{K}^2$ satisfies $(\Spec\iota)(\mathfrak{q}_b)=\mathfrak{p}$, whereas in the second example, only the two points $\mathfrak{q}_+=(\x-a, \y-\sqrt{a})$ and $\mathfrak{q}_-=(\x-a, \y+\sqrt{a})$ satisfy $(\Spec\phi)(\mathfrak{q}_\pm)=\mathfrak{p}$.

In this way, geometrically, a finite type morphism is related to having fibers of finite dimension, and a finite morphism is related to having fibers that are finite sets.
:::

For now, to compute the fiber of a scheme morphism in situations like [Example 16](#ex16) above, we have no choice but to carry out calculations straightforwardly on a case-by-case basis, but after we compute fiber products, we will be able to use a somewhat more standardized method. For that time, we define the following.

::: Definition 17
A scheme morphism $\varphi: X \rightarrow Y$ is *quasi-finite* if $\varphi$ is a morphism of finite type and for any $y\in Y$, the set $\varphi^{-1}(y)$ is always a finite set.
:::

Then the geometric intuition for finite morphisms in [Example 16](#ex16) is always true. That is, any finite morphism is always quasi-finite. It is possible to prove this right now, but we postpone it until after we define fiber products.

Finally, we define the following.

::: Definition 18
A scheme morphism $\varphi: X \rightarrow Y$ is *locally of finite presentation* if for any affine open subset $V\cong \Spec B$ of $Y$, there exists a covering $\varphi^{-1}(V)=\bigcup \Spec A_i$ such that $B \rightarrow A_i$ are all finitely presented. If a scheme morphism $\varphi:X \rightarrow Y$ is quasi-compact, quasi-separated, and locally of finite presentation, then $\varphi$ is called a *morphism of finite presentation*.
:::

In most cases, we consider the case where all schemes are locally Noetherian, and in this case, by [[Commutative Algebra] §Basic Notions, ⁋Proposition 9](/en/math/commutative_algebra/basic_notions#prop9), this notion is nothing new.
