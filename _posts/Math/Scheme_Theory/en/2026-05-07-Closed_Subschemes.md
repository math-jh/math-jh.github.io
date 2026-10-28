---
title: "Closed Subschemes"
description: "We examine how the sheaf obtained by topological restriction and the sheaf obtained from a quotient ring differ when defining closed subschemes of an affine scheme. Through a concrete example of the affine line, we see the difference between the two structure sheaves."
excerpt: "Closed subschemes and vanishing schemes defined by an ideal sheaf"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/closed_subschemes
sidebar: 
    nav: "scheme_theory-en"

date: 2025-02-18
weight: 10
translated_at: 2026-07-27T21:15:03+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-28T11:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
In [§Schemes, ⁋Lemma 2](/en/math/scheme_theory/schemes#lem2){: data-lid="3bsbj" }, we saw that for an affine scheme $\Spec A$, any element $f$ defines an open affine subscheme $D(f)\cong \Spec A_f$; in particular, to compare the two structure sheaves, we applied [\[Topology\] §Sheaves, ⁋Lemma 11](/en/math/topology/sheaves#lem11){: data-lid="04zq8" } to

$$(\Spec\epsilon)^\sharp: \mathcal{O}_{\Spec A} \rightarrow (\Spec \epsilon)_\ast \mathcal{O}_{\Spec A_f}$$

obtained from $\epsilon: A \rightarrow A_f$, yielding

$$(\Spec\epsilon \vert^{D(f)})^\sharp: \mathcal{O}_{D(f)} \rightarrow (\Spec\epsilon\vert^{D(f)})_\ast \mathcal{O}_{\Spec A_f}$$

and from the fact that $\Spec A_f$ is isomorphic to the open subset of $\Spec A$, $D(f)$, we could conclude that this is an isomorphism.

On the other hand, by the second result of [§The Spectrum, ⁋Proposition 9](/en/math/scheme_theory/spectrums#prop9){: data-lid="yo2is" }, given an affine scheme $\Spec A$ and, in $A$, an ideal $\mathfrak{a}$, the $\Spec$ functor gives

$$\Spec\pi: \Spec A/\mathfrak{a}\rightarrow \Spec A$$

and we know that in this case $\Spec\pi$ is injective and its image is the closed set $Z(\mathfrak{a})$. In this case as well, just as above, after considering the canonical decomposition

$$\Spec A/\mathfrak{a}\overset{\Spec\pi\vert^{Z(\mathfrak{a})}}{\rightarrow} Z(\mathfrak{a}) \overset{\iota}{\rightarrow}\Spec A$$

we can construct from

$$(\Spec\pi)^\sharp: \mathcal{O}_{\Spec A} \rightarrow (\Spec\pi)_\ast \mathcal{O}_{\Spec A/\mathfrak{a}}$$

a morphism of sheaves defined on $Z(\mathfrak{a})$

$$\iota^{-1} \mathcal{O}_{\Spec A} \rightarrow (\Spec\pi\vert^{Z(\mathfrak{a})})_\ast \mathcal{O}_{\Spec A/\mathfrak{a}}$$

but we have not even defined a scheme structure on $Z(\mathfrak{a})$, and therefore not only do we not know the relationship between $\iota^{-1}\mathcal{O}_{\Spec A}$ and $\mathcal{O}_{Z(\mathfrak{a})}$, but there is also no guarantee that this is an isomorphism. In fact, it is far more likely not to be an isomorphism, because while $\iota^{-1}\mathcal{O}_{\Spec A}$ is defined from the structure sheaf of $\Spec A$ using only topological data for the closed set $Z(\mathfrak{a})$, $(\Spec\pi)_\ast\mathcal{O}_{\Spec A/\mathfrak{a}}$ also carries algebraic information about the ring $A/\mathfrak{a}$.

::: Example 1
For example, fix a field $\mathbb{K}$ and consider the affine $1$-line $\mathbb{A}_\mathbb{K}^1=\Spec \mathbb{K}[\x]$. Then there exist canonical surjections

$$\pi_1:\mathbb{K}[\x] \rightarrow \mathbb{K}[\x]/(\x)\cong \mathbb{K},\qquad \pi_2:\mathbb{K}[\x] \rightarrow \mathbb{K}[\x]/(\x^2)$$

and concretely, $\pi_1$ and $\pi_2$ are defined by $\x\mapsto 0+(\x)$ and $\x\mapsto \x+(\x^2)$, respectively.

On the other hand, since $\mathbb{K}[\x]/(\x)\cong \mathbb{K}$, $\Spec \mathbb{K}[\x]/(\x)$ has only a single point $(0)$. Similarly, $\Spec \mathbb{K}[\x]/(\x^2)$ also has only a single point. This is because there is a one-to-one correspondence between the prime ideals of $\mathbb{K}[\x]/(\x^2)$ and the prime ideals of $\mathbb{K}[\x]$ containing $\x^2$, and since $\mathbb{K}[\x]$ is a principal ideal domain, if we write a prime ideal of $\mathbb{K}[\x]$ as $(p(\x))$, in order for this ideal to contain $\x^2$, $p(\x)$ must divide $\x^2$, so we know that necessarily $p(\x)=\x$.

Therefore, considering the scheme morphisms

$$\Spec\pi_1:\Spec \mathbb{K}[\x]/(\x) \rightarrow \Spec \mathbb{K}[\x],\qquad \Spec\pi_2:\Spec \mathbb{K}[\x]/(\x^2) \rightarrow \Spec \mathbb{K}[\x]$$

defined by these, as continuous maps we know that $\Spec\pi_1$ sends the unique point $(0)$ of $\Spec \mathbb{K}[\x]/(\x)$ to the point $(\x)$ of $\Spec \mathbb{K}[\x]$, and $\Spec\pi_2$ sends the unique point $(\x)$ of $\Spec \mathbb{K}[\x]/(\x^2)$ to the point $(\x)$ of $\Spec \mathbb{K}[\x]$. That is, as continuous maps they define the same function, but of course $\Spec \mathbb{K}[\x]/(\x)$ and $\Spec \mathbb{K}[\x]/(\x^2)$ are not isomorphic as schemes.
:::

Naturally, the structure sheaf we desire is of the form $(\Spec\pi)_\ast \mathcal{O}_{\Spec A/\mathfrak{a}}$, which contains algebraic information, and what relationship this has with $\iota^{-1}\mathcal{O}_{\Spec A}$ will be examined at the end of this post.

## Closed Subschemes

As seen above, our model for a closed subscheme is the canonical projection $\pi: A \rightarrow A/\mathfrak{a}$ and the scheme morphism

$$(\Spec \pi, (\Spec\pi)^\sharp): \Spec A/\mathfrak{a} \rightarrow\Spec A$$

arising from it. Here $\Spec\pi$ is an injective continuous map giving a homeomorphism between $\Spec A/\mathfrak{a}$ and a closed subset of $\Spec A$, and $\Spec\pi^\sharp: \mathcal{O}_{\Spec A} \rightarrow (\Spec\pi)_\ast \mathcal{O}_{\Spec A/\mathfrak{a}}$ is obtained from [§Affine Scheme, ⁋Proposition 9](/en/math/scheme_theory/affine_schemes#prop9){: data-lid="oz92r" }.

On the other hand, the most important property of the ring homomorphism $\pi: A \rightarrow A/\mathfrak{a}$ is that $\pi$ is surjective, and indeed, given any surjective ring homomorphism $\phi: A \rightarrow B$, by the first isomorphism theorem

$$B=\im\phi\cong A/\ker\phi$$

so this property characterizes $\pi$ precisely. Meanwhile, considering [\[Commutative Algebra\] §Properties of Localization, ⁋Proposition 4](/en/math/commutative_algebra/properties_of_localization#prop4){: data-lid="3kuvr" }, the surjectivity of $\pi$ can be checked by examining whether the localization $\pi_\mathfrak{p}: A_\mathfrak{p} \rightarrow (A/\mathfrak{a})_{\mathfrak{p}}$ at an arbitrary prime ideal $\mathfrak{p}$ is surjective, which geometrically amounts to examining the stalk at an arbitrary point $\mathfrak{p}$ of the affine scheme $\Spec A$, and therefore by [\[Topology\] §Sheaves, ⁋Proposition 15](/en/math/topology/sheaves#prop15){: data-lid="jedl9" } this is equivalent to $(\Spec\pi)^\sharp$ being surjective.

::: Definition 2
A scheme morphism $\iota: Z \rightarrow X$ is called a *closed embedding* if, as a continuous map, $\iota$ is a homeomorphism between $Z$ and a closed subset of $X$, and the sheaf morphism $\iota^\sharp: \mathcal{O}_X \rightarrow \iota_\ast \mathcal{O}_Z$ is surjective.

For two closed embeddings $\iota: Z \rightarrow X$ and $\iota': Z' \rightarrow X$ into $X$, if there exists an isomorphism $\theta: Z' \rightarrow Z$ such that $\iota'=\iota\circ \theta$, we say that the two are equivalent, and call this equivalence class a *closed subscheme* of $X$.
:::

The condition on the continuous map $\iota$ is clear, and the intuition for $\iota^\sharp$ also admits a geometric interpretation: it means that functions on $Z$, or more precisely on $\iota(Z)$, must all be obtained by restricting functions on $X$ to $Z$. Or, conversely, given any function on $Z$, it should be possible to extend it locally to a function on $X$ in a neighborhood of each point. Here, the surjectivity of the sheaf morphism is a condition on stalks, so it does not mean global extension. For example, considering $X=\mathbb{P}^1$ and the reduced closed subscheme $Z$ consisting of two points in it, the map from $\Gamma(X,\mathcal{O}_X)=\mathbb{K}$ to $\Gamma(Z,\mathcal{O}_Z)=\mathbb{K}\times \mathbb{K}$ is not surjective. On the other hand, it is worth contrasting with the case where $\iota$ is an open embedding. In this case, $\iota^\sharp:\mathcal{O}_X \rightarrow \iota_\ast\mathcal{O}_Z$ itself is not an isomorphism. For example, considering $X=\mathbb{A}^1_k=\Spec k[t]$ and its open subset $Z=D(t)=\Spec k[t,t^{-1}]$, we have $(\iota_\ast\mathcal{O}_Z)(X)=k[t,t^{-1}]$, so $k[t] \rightarrow k[t,t^{-1}]$ is not surjective. The correct statement is that since $\iota$ maps $Z$ to an open set, we have $\iota^{-1}\mathcal{O}_X\cong\mathcal{O}_Z$, that is, an isomorphism is induced between the stalks at each point of $\iota(Z)$.

This definition is natural, but it is somewhat different in flavor from the properties of scheme morphisms we defined in the previous post. Therefore we examine the following equivalent condition.

::: Proposition 3
For a scheme morphism $\varphi: X \rightarrow Y$, the following two conditions are equivalent.

1. $\varphi$ is a closed embedding.
2. $\varphi$ is an affine morphism, and whenever an affine open subset of $Y$, $V\cong \Spec B$, is given, for its preimage $\varphi^{-1}(V)\cong \Spec A$, $B \rightarrow A$ is surjective.
:::
::: Proof
First assume the second condition and show that $\varphi$ is a closed embedding. If we cover $Y$ by affine open subsets $\{V_i=\Spec B_i\}$, then by assumption $\varphi^{-1}(V_i)\cong \Spec A_i$ and the corresponding $\beta_i: B_i \rightarrow A_i$ is surjective. Then by the first isomorphism theorem, setting $\mathfrak{b}_i=\ker\beta_i$, we have $A_i\cong B_i/\mathfrak{b}_i$, and therefore the restriction of $\varphi$ to $\varphi^{-1}(V_i)$ is the morphism defined by the canonical projection $\pi: B_i \rightarrow B_i/\mathfrak{b}_i$, namely $\Spec\pi$.

Now by [§The Spectrum, ⁋Proposition 9](/en/math/scheme_theory/spectrums#prop9){: data-lid="0xgvz" }, $\Spec\pi$ is injective, its image is the closed set $Z(\mathfrak{b}_i)$, and $\Spec\pi$ is a homeomorphism onto this image. From this we first see that $\varphi$ is injective. Indeed, if $\varphi(x)=\varphi(x')$, then choosing $V_i$ containing this point, we have $x,x'\in \varphi^{-1}(V_i)$, and the restriction of $\varphi$ to $\varphi^{-1}(V_i)$ is injective. Also, for each $i$, $\varphi(X)\cap V_i=Z(\mathfrak{b}_i)$ is a closed subset of $V_i$ and $\{V_i\}$ is an open cover of $Y$, so $\varphi(X)$ is a closed subset of $Y$. Finally, for any open subset of $X$, $U$, from the injectivity of $\varphi$ we have

$$\varphi(U)\cap V_i=\varphi(U\cap \varphi^{-1}(V_i))$$

and since the right-hand side is an open subset of $\varphi(X)\cap V_i$, $\varphi(U)$ is an open subset of $\varphi(X)$. That is, $\varphi$ is a homeomorphism between $X$ and the closed subset of $Y$, $\varphi(X)$.

Next we show that $\varphi^\sharp$ is surjective. By [\[Topology\] §Sheaves, ⁋Proposition 15](/en/math/topology/sheaves#prop15){: data-lid="hjli1" }, it suffices to check stalks at each $y\in Y$. If $y\not\in \varphi(X)$, then since $\varphi(X)$ is closed, there exists, disjoint from $\varphi(X)$, an open neighborhood of $y$, $W$, and in this case $(\varphi_\ast \mathcal{O}_X)(W)=\mathcal{O}_X(\emptyset)=0$, so $(\varphi_\ast \mathcal{O}_X)_y=0$ and there is nothing to check. Now let $y=\varphi(x)$. Since $\varphi$ is a homeomorphism onto its image, for any open set containing $x$ in $X$, $U$, there exists, satisfying $\varphi(U)=W\cap \varphi(X)$, an open set of $Y$, $W\ni y$, and in this case $\varphi^{-1}(W)=U$. That is, the preimages of open neighborhoods of $y$ are cofinal among the open neighborhoods of $x$, and therefore

$$(\varphi_\ast \mathcal{O}_X)_y=\varinjlim_{W\ni y}\mathcal{O}_X(\varphi^{-1}(W))\cong \mathcal{O}_{X,x}$$

holds. Now choose an index with $y\in V_i$, say $i$, and let the prime ideal corresponding to $y$ in $B_i$ be $\mathfrak{q}$, and the prime ideal corresponding to $x$ in $A_i$ be $\mathfrak{p}=\mathfrak{q}/\mathfrak{b}_i$; then by [§Affine Scheme, ⁋Lemma 8](/en/math/scheme_theory/affine_schemes#lem8){: data-lid="a2e1c" }, the morphism between stalks at $y$ is the localization of $\beta_i$

$$(B_i)_\mathfrak{q} \rightarrow (A_i)_\mathfrak{p}\cong (B_i/\mathfrak{b}_i)_\mathfrak{q}.$$

However, since localization is an exact functor ([\[Commutative Algebra\] §Properties of Localization, ⁋Proposition 2](/en/math/commutative_algebra/properties_of_localization#prop2){: data-lid="vkwsp" }), this morphism is surjective, and therefore $\varphi^\sharp$ is surjective. That is, $\varphi$ is a closed embedding.

The converse is not formal. Assume that $\varphi$ is a closed embedding, fix an affine open subset of $Y$, $V=\Spec B$, and write $W=\varphi^{-1}(V)$. Just as in the previous argument, from the fact that $\varphi$ is a homeomorphism onto its image, for any $\mathfrak{q}=\varphi(x)\in \varphi(X)\cap V$ we have $(\varphi_\ast \mathcal{O}_X)_\mathfrak{q}\cong \mathcal{O}_{X,x}$, and at points outside $\varphi(X)$ we have $(\varphi_\ast \mathcal{O}_X)_\mathfrak{q}=0$. That is, we know the stalks of $\varphi_\ast \mathcal{O}_X$. However, this alone does not tell us what sections $\varphi_\ast \mathcal{O}_X$ has over open subsets of $V$, and in particular we cannot know whether $W$ is an affine scheme. What is needed for this is the fact that for a closed embedding $\varphi$, both $\varphi_\ast \mathcal{O}_X$ and the ideal sheaf $\ker\varphi^\sharp$ are *quasi-coherent*, that is, for an affine open subset of $Y$, $\Spec B$, and any $f\in B$, the canonical morphism

$$\left((\varphi_\ast \mathcal{O}_X)(\Spec B)\right)_f \rightarrow (\varphi_\ast \mathcal{O}_X)(D(f))$$

is an isomorphism. This is a condition of exactly the same form as the localization condition required for ideals in [Proposition 6](#prop6){: data-lid="uj3n7" }, but since we do not even know whether $\varphi$ is an affine morphism at present, we cannot obtain this using only the tools we have. Therefore, we merely assert this fact without proof, and conclude the remaining argument with the tools we already have. This fact is proved in [§Quasi-Coherent Sheaves, ⁋Proposition 18](/en/math/scheme_theory/quasicoherent_sheaves#prop18){: data-lid="7w8bu" } as the quasi-coherence of $\varphi_\ast \mathcal{O}_X$.

Set $C=(\varphi_\ast \mathcal{O}_X)(V)=\Gamma(W, \mathcal{O}_W)$ and $\beta=\varphi^\sharp(V): B \rightarrow C$. Then since the $D(f)$ form a base for $V$, repeating the argument of [§Affine Scheme, ⁋Lemma 8](/en/math/scheme_theory/affine_schemes#lem8){: data-lid="71hpo" } verbatim, from the above fact we obtain for any $\mathfrak{q}\in V$

$$(\varphi_\ast \mathcal{O}_X)_\mathfrak{q}\cong C_\mathfrak{q}$$

Here $C_\mathfrak{q}$ is the localization of the $B$-module $C$ at $\mathfrak{q}$, and this isomorphism is induced by the restriction maps.

First, $\beta$ is surjective. Indeed, since $\varphi^\sharp$ is surjective, by [\[Topology\] §Sheaves, ⁋Proposition 15](/en/math/topology/sheaves#prop15){: data-lid="nvd0y" }, at each $\mathfrak{q}$ the morphism between stalks $B_\mathfrak{q} \rightarrow C_\mathfrak{q}$ is surjective, and since this is the localization of the $B$-module homomorphism $\beta$, by [\[Commutative Algebra\] §Properties of Localization, ⁋Proposition 4](/en/math/commutative_algebra/properties_of_localization#prop4){: data-lid="klth0" } $\beta$ is surjective. Therefore, setting $\mathfrak{b}=\ker\beta$, we have $C\cong B/\mathfrak{b}$.

Second, $W$ is an affine scheme. First, topologically, that $\mathfrak{q}\in V$ belongs to $\varphi(X)$ is equivalent to the stalk calculated above not being $0$. We have already seen that the stalk at points outside $\varphi(X)$ is $0$, and in the case $\mathfrak{q}=\varphi(x)$, the stalk is the local ring $\mathcal{O}_{X,x}$ and therefore is not $0$. But $(\varphi_\ast \mathcal{O}_X)_\mathfrak{q}\cong (B/\mathfrak{b})_\mathfrak{q}$, and that this is not $0$ is equivalent to $\mathfrak{b}\subseteq \mathfrak{q}$, so

$$\varphi(X)\cap V=Z(\mathfrak{b})$$

holds. Now applying the adjunction of [§Affine Scheme, ⁋Theorem 13](/en/math/scheme_theory/affine_schemes#thm13){: data-lid="gxxzz" } to the identity map $C \rightarrow \Gamma(W, \mathcal{O}_W)$, we obtain a canonical morphism $\sigma: W \rightarrow \Spec C$, and by the naturality of the adjunction we have $\Spec\beta\circ \sigma=\varphi\vert_W$. On the other hand, $\Spec\beta: \Spec B/\mathfrak{b} \rightarrow \Spec B$ is a homeomorphism onto $Z(\mathfrak{b})$ ([§The Spectrum, ⁋Proposition 9](/en/math/scheme_theory/spectrums#prop9){: data-lid="vjine" }), and $\varphi\vert_W$ is also a homeomorphism onto $\varphi(X)\cap V=Z(\mathfrak{b})$, so $\sigma$ is a homeomorphism. Also, for any $x\in W$ and $\mathfrak{q}=\varphi(x)$, the morphism induced by $\sigma$ on stalks is $C_\mathfrak{q} \rightarrow \mathcal{O}_{W,x}$ by [§Affine Scheme, ⁋Lemma 8](/en/math/scheme_theory/affine_schemes#lem8){: data-lid="caqza" }, which is the same as the morphism induced by the restriction maps, that is, the isomorphism $C_\mathfrak{q}\cong (\varphi_\ast \mathcal{O}_X)_\mathfrak{q}\cong \mathcal{O}_{W,x}$ obtained above. Therefore, $\sigma$ is a homeomorphism and an isomorphism on all stalks, hence an isomorphism of locally ringed spaces.

From the above, $W\cong \Spec C=\Spec B/\mathfrak{b}$ is an affine scheme and $B \rightarrow C$ is surjective. Since $V$ was an arbitrary affine open subset of $Y$, the morphism $\varphi$ is affine and the second condition holds.
:::

Then any closed embedding can always be thought of locally as coming from a suitable $\pi: A \rightarrow A/\mathfrak{a}$ as examined above. In particular, if $Y$ is the affine scheme $\Spec B$, by the equivalence above we see that any closed embedding into $Y$, $\varphi: X \rightarrow Y$, corresponds exactly to $B \rightarrow B/\mathfrak{b}$.

## Properties of Closed Embeddings

By [Proposition 3](#prop3){: data-lid="2ucex" }, any closed embedding is always affine-local on target, and closed embeddings are closed under composition. Moreover, the following holds.

::: Proposition 4
Any closed embedding is always a finite morphism.
:::
::: Proof
Let a closed embedding $\varphi: X \rightarrow Y$ be given. By [Proposition 3](#prop3){: data-lid="wq71j" }, $\varphi$ is an affine morphism, and for any affine open subset of $Y$, $V\cong \Spec B$, we have $\varphi^{-1}(V)\cong\Spec A$ and the corresponding ring homomorphism $\beta: B \rightarrow A$ is surjective. Then for any $a\in A$, there exists $b\in B$ such that $a=\beta(b)=b\cdot 1$, so $A$, as a $B$-module, is generated by $1$, and therefore $\beta$ is a finite ring homomorphism. (Fourth condition of [\[Commutative Algebra\] §Integral Extensions, ⁋Definition 3](/en/math/commutative_algebra/integral_extension#def3){: data-lid="e6reh" }) Now by [§Properties of Scheme Morphisms, ⁋Definition 10](/en/math/scheme_theory/properties_of_scheme_morphisms#def10){: data-lid="myc6q" }, $\varphi$ is a finite morphism.
:::

In light of the geometric intuition for (quasi-)finite morphisms built in [§Properties of Scheme Morphisms, ⁋Example 16](/en/math/scheme_theory/properties_of_scheme_morphisms#ex16){: data-lid="w4jk6" }, it is obvious that at least closed embeddings should always be quasi-finite, and going further from this, a geometric interpretation that they are also finite is possible.

::: Definition 5
For any scheme $Z$, an $\mathcal{O}_Z$-subsheaf $\mathcal{I}$ such that for each open set $U$, $\mathcal{I}(U)$ is an ideal of $\mathcal{O}_Z(U)$ is called an *ideal sheaf* of $Z$. In particular, for a closed embedding $\iota: Z \rightarrow X$, we call the $\mathcal{O}_X$-subsheaf $\ker\iota^\sharp$ the ideal sheaf defined by $\iota$, and denote it by $\mathcal{I}_{Z/X}$.
:::

That is, the following exact sequence

$$0 \rightarrow \mathcal{I}_{Z/X} \rightarrow \mathcal{O}_X \rightarrow \iota_\ast \mathcal{O}_Z \rightarrow 0$$

exists. Therefore, for any affine open subset of $X$, $U=\Spec A$, we have

$$0 \rightarrow \mathcal{I}_{Z/X}(U) \rightarrow \mathcal{O}_X(U)\cong A \rightarrow \iota_\ast \mathcal{O}_Z(U) \rightarrow 0$$

so $\mathcal{I}_{Z/X}(U)$ is an ideal of $A$, which justifies this name.

We saw right after [Proposition 3](#prop3){: data-lid="xpzrm" } that the closed subschemes of any affine scheme $Y=\Spec B$ correspond exactly to the ideals of $B$. On the other hand, since any scheme is built by gluing affine schemes, if ideals are defined on each of these affine schemes and satisfy suitable gluing conditions, then a closed subscheme of the original scheme will be defined through them.

::: Proposition 6
For a scheme $X$, suppose that for each affine open subset $\Spec A$, an ideal $\mathcal{I}(A)\subseteq A$ is given. If for each $f\in A$, the map $A \rightarrow A_f$ induces an isomorphism $\mathcal{I}(A_f)\cong \mathcal{I}(A)_f$, then these data induce a unique closed subscheme of $X$, $Z\hookrightarrow X$.
:::
::: Proof
First cover $X$ by affine open subsets $\{\Spec A_i\}$. Then what we need to show is that for any $i,j$, the closed subscheme on $\Spec A_i$ defined by the ideal $\mathcal{I}(A_i)$ and the closed subscheme on $\Spec A_j$ defined by the ideal $\mathcal{I}(A_j)$ define the same closed subscheme on the intersection of $\Spec A_i$ and $\Spec A_j$.


First, from [§The Topology of Schemes, ⁋Lemma 11](/en/math/scheme_theory/topology_of_schemes#lem11){: data-lid="c64ws" } we can cover the intersection of $\Spec A_i$ and $\Spec A_j$ by principal open subsets

$$\Spec (A_i)_{f_i}\cong\Spec (A_j)_{f_j}$$

Now, restricting the closed subscheme on $\Spec A_i$ defined by $\mathcal{I}(A_i)$ to $D(f_i)\cong\Spec (A_i)_{f_i}$ gives the closed subscheme defined by the ideal $\mathcal{I}(A_i)_{f_i}$, and by the given assumption $\mathcal{I}(A_i)_{f_i}\cong \mathcal{I}((A_i)_{f_i})$. Here $\Spec (A_i)_{f_i}$ and $\Spec (A_j)_{f_j}$ are the *same* open subset of $X$, so through this isomorphism $\mathcal{I}((A_i)_{f_i})$ and $\mathcal{I}((A_j)_{f_j})$ denote the same ideal, and therefore the two closed subschemes agree on this open set.

These locally obtained closed subschemes glue well. Indeed two overlapping pieces agree on principal open subsets covering the overlap by the above argument, and the identifications on them all come from restriction maps so they glue to a single morphism on the overlap ([\[Topology\] §Sheaves, ⁋Definition 1](/en/math/topology/sheaves#def1){: data-lid="wvh21" }), and therefore the cocycle condition also holds automatically. Then by [§Schemes, ⁋Lemma 9](/en/math/scheme_theory/schemes#lem9){: data-lid="x8d0q" } they glue to a single scheme $Z$ and closed embedding $Z \rightarrow X$. Uniqueness follows because by [Proposition 3](#prop3){: data-lid="7j1t9" } a closed subscheme on an affine open subset is completely determined by the ideal on it. That is, two closed subschemes realizing the given data agree on each piece of an affine open covering of $X$, and therefore are equivalent.
:::

Now let an arbitrary scheme $X$ and a global section $s\in \Gamma(X, \mathcal{O}_X)$ be given. Then for each affine open subset $U\cong\Spec A$, the restriction $s\vert_U$ defines the ideal $\mathcal{I}(A)=(s\vert_U)$ of $A$, and the $\mathcal{I}(A)$ defined in this way, since $(s\vert_U)A_f=(s\vert_{D(f)})$, satisfy the condition of [Proposition 6](#prop6){: data-lid="sbr1j" }.

::: Definition 7
For a scheme $X$ and a global section of $X$, $s\in \Gamma(X, \mathcal{O}_X)$, the scheme $Z(s)$ defined as above is called the *vanishing scheme* of $s$.
:::

More generally, for a set $S$ of global sections, it is also clear how $Z(S)$ should be defined, and therefore in particular when $X=\Spec A$ and $S=\mathfrak{a}$ is an ideal of $A$, it is clear how $Z(\mathfrak{a})$ should be defined, and this is obtained by pushing forward the structure sheaf of the affine scheme $\Spec A/\mathfrak{a}$ via $\Spec\pi$ to the closed set $Z(\mathfrak{a})$. Henceforth we always think of $Z(\mathfrak{a})$ as being equipped with such a scheme structure.

::: Definition 8
A scheme morphism $\varphi: X \rightarrow Y$ is called a *locally closed embedding* if there exists an open subscheme $\iota:Z\hookrightarrow Y$ of $Y$ such that through the canonical decomposition

$$X\overset{\varphi\vert^Z}{\rightarrow}Z\overset{\iota}{\rightarrow} Y$$

$\varphi\vert^Z$ is a closed embedding. 
:::

Then any locally closed embedding is always locally of finite type. To check this, fix an affine open subset $V=\Spec B$ of $Y$. First, $Z\cap V$ is covered by principal open subsets $D(f)\cong \Spec B_f$ of $\Spec B$ ([§The Spectrum, ⁋Lemma 11](/en/math/scheme_theory/spectrums#lem11){: data-lid="mt8ef" }), and $B \rightarrow B_f$ is of finite type since it adjoins only $1/f$. Also, since $\varphi\vert^Z$ is a closed embedding, by [Proposition 3](#prop3){: data-lid="ej40n" } the preimage of each $D(f)$ is affine and its coordinate ring is a quotient of $B_f$, so the composition $B \rightarrow B_f \rightarrow B_f/\mathfrak{b}$ is also of finite type. That is, $\varphi^{-1}(V)$ is covered by affine open subsets on which $B \rightarrow \mathcal{O}_X(-)$ is of finite type, and therefore by [§Properties of Scheme Morphisms, ⁋Lemma 13](/en/math/scheme_theory/properties_of_scheme_morphisms#lem13){: data-lid="d59qp" } we obtain the same conclusion for any affine open subset of $\varphi^{-1}(V)$. 

## Image of a Scheme Morphism

Now we define the image of a scheme morphism. Naturally, when an arbitrary scheme morphism $\varphi: X \rightarrow Y$ is given, we would want its image $\im\varphi$ to also be equipped with a scheme structure. However, as a subset of the topological space $Y$, $\im\varphi$ may be neither open nor closed, so defining a structure sheaf on $\im\varphi$ using the structure sheaf of $Y$ seems out of reach. 

The solution to this is to define the *scheme-theoretic image* of $\varphi$ as the smallest closed subscheme containing the image of $\varphi$. For this we must first examine what it means for one closed subscheme of $X$ to be smaller than another.

::: Lemma 9
Let two closed embeddings $\iota_1: Z_1 \rightarrow X$, $\iota_2: Z_2 \rightarrow X$ be given. Then there exists a scheme morphism $\varphi: Z_1 \rightarrow Z_2$ satisfying $\iota_1=\iota_2\circ\varphi$ if and only if $\mathcal{I}_{Z_2/X}\subseteq \mathcal{I}_{Z_1/X}$. In this case, $\varphi$ is a closed embedding.
:::

::: Proof
First, suppose that $\iota_1=\iota_2\circ\varphi$ holds for some $\varphi$. Then $\iota_1^\sharp$ is the following composition

$$\mathcal{O}_X\overset{\iota_2^\sharp}{\rightarrow}(\iota_2)_\ast \mathcal{O}_{Z_2}\overset{(\iota_2)_\ast \varphi^\sharp}{\rightarrow}(\iota_2)_\ast \varphi_\ast \mathcal{O}_{Z_1}=(\iota_1)_\ast \mathcal{O}_{Z_1}$$

so $\ker\iota_2^\sharp\subseteq \ker\iota_1^\sharp$, and hence by [Definition 5](#def5){: data-lid="t0x36" } we have $\mathcal{I}_{Z_2/X}\subseteq \mathcal{I}_{Z_1/X}$.

Conversely, assume $\mathcal{I}_{Z_2/X}\subseteq \mathcal{I}_{Z_1/X}$. If we choose an arbitrary affine open subset of $X$, $U=\Spec A$, then by [Proposition 3](#prop3){: data-lid="u5sf1" } $\iota_k^{-1}(U)$ is an affine open subset, and from the exact sequence right after [Definition 5](#def5){: data-lid="qa62s" } we have

$$\iota_k^{-1}(U)\cong \Spec A/\mathfrak{a}_k,\qquad \mathfrak{a}_k=\mathcal{I}_{Z_k/X}(U)$$

where the restriction of $\iota_k$ to $\iota_k^{-1}(U)$ corresponds to the canonical projection $A \rightarrow A/\mathfrak{a}_k$. By assumption $\mathfrak{a}_2\subseteq \mathfrak{a}_1$, so $A \rightarrow A/\mathfrak{a}_1$ factors uniquely through $A \rightarrow A/\mathfrak{a}_2$, and the resulting $\pi_U: A/\mathfrak{a}_2 \rightarrow A/\mathfrak{a}_1$ is surjective. Therefore, by the discussion right before [Definition 2](#def2){: data-lid="1we66" }, $\varphi_U=\Spec\pi_U: \iota_1^{-1}(U) \rightarrow \iota_2^{-1}(U)$ is a closed embedding, and by construction the restriction of $\iota_1$ to $\iota_1^{-1}(U)$ is the composition of the restriction of $\iota_2$ and $\varphi_U$.

Now, for two affine open subsets of $X$, $U=\Spec A$ and $U'$, it remains to show that $\varphi_U$ and $\varphi_{U'}$ agree on the intersection. By [§The Topology of Schemes, ⁋Lemma 11](/en/math/scheme_theory/topology_of_schemes#lem11){: data-lid="r9lw6" }, we can cover $U\cap U'$ by open sets that are principal open sets in both $U$ and $U'$, and since localization is an exact functor ([\[Commutative Algebra\] §Properties of Localization, ⁋Proposition 2](/en/math/commutative_algebra/properties_of_localization#prop2){: data-lid="c767v" }), on such $D(f)\cong \Spec A_f$ we have $\mathcal{I}_{Z_k/X}(D(f))=\mathfrak{a}_kA_f$. Therefore, $\varphi_U$ and $\varphi_{U'}$ both correspond on $D(f)$ to the canonical projection induced by $\mathfrak{a}_2A_f\subseteq \mathfrak{a}_1A_f$, namely $A_f/\mathfrak{a}_2A_f \rightarrow A_f/\mathfrak{a}_1A_f$, so they agree. Then by [§Morphisms of Schemes, ⁋Proposition 1](/en/math/scheme_theory/morphism_of_schemes#prop1){: data-lid="j27o5" }, these glue to a scheme morphism $\varphi: Z_1 \rightarrow Z_2$, and by construction $\iota_1=\iota_2\circ\varphi$.

Finally, we show that whenever $\iota_1=\iota_2\circ\varphi$, *any* such $\varphi$ is a closed embedding. For an affine open subset of $X$, $U$, we have $\varphi^{-1}(\iota_2^{-1}(U))=\iota_1^{-1}(U)$, and the restriction of $\varphi$ to this open set corresponds to a ring homomorphism $A/\mathfrak{a}_2 \rightarrow A/\mathfrak{a}_1$, which must commute with the two canonical projections from $A$, so it can only be the above $\pi_U$. However, since $\iota_2$ is an affine morphism, as $U$ runs over an affine open covering of $X$, the sets $\iota_2^{-1}(U)$ form an affine open covering of $Z_2$, and since closed embeddings are affine-local on target ([Proposition 3](#prop3){: data-lid="9y7q4" }), $\varphi$ is a closed embedding.
:::

For a scheme $X$ and two closed subschemes $Z_1,Z_2$, if there exists a closed embedding $\varphi:Z_1 \rightarrow Z_2$, let us think of $Z_1$ as a *smaller* closed subscheme than $Z_2$.

::: Definition 10
Let an arbitrary scheme morphism $\varphi: X \rightarrow Y$ be given. Then we say the image of $\varphi$ is *contained* in a closed subscheme $\iota: Z \rightarrow Y$ if the following composition

$$\mathcal{I}_{Z/Y} \rightarrow \mathcal{O}_Y \rightarrow \varphi_\ast \mathcal{O}_X$$

is $0$. In this case, the smallest closed subscheme of $Y$ containing the image of $\varphi$ is called the *scheme-theoretic image* of $\varphi$.
:::

If in the above $Y$ is an affine scheme $\Spec B$, then a closed subscheme of $Y$ is completely determined by an ideal $\mathfrak{b}$ of $B$. Therefore in this case, the scheme-theoretic image of $\varphi$ will be the closed subscheme of $Y$ defined by the kernel of $\mathcal{O}_Y \rightarrow \varphi_\ast \mathcal{O}_X$. In the more special case where $X$ is also an affine scheme, since $\mathcal{O}_Y \rightarrow \varphi_\ast \mathcal{O}_X$ comes from a ring homomorphism $\phi$, we can perform explicit computations.

::: Example 11
Let us examine a slight variation of the example of a closed embedding $\Spec\pi: \Spec \mathbb{K}[\x]/(\x^2) \rightarrow \Spec \mathbb{K}[\x]$ from [Example 1](#ex1){: data-lid="infzy" }. In this example, we write $\mathbb{K}[\x]/(\x^2)$ as $\mathbb{K}[\epsilon]/(\epsilon^2)$ for distinction. 

We know by [\[Algebraic Structures\] §Algebras, ⁋Proposition 8](/en/math/algebraic_structures/algebras#prop8){: data-lid="yqxo4" } that a $\mathbb{K}$-algebra homomorphism $\phi:\mathbb{K}[\x_1,\ldots, \x_n] \rightarrow \mathbb{K}[\epsilon]/(\epsilon^2)$ is completely determined by the values of $\x_i$. Thus let $\phi(\x_i)=a_i+b_i\epsilon$. If there exists a non-$0$ $b_i$, we can show that $\phi$ is surjective, and therefore $\Spec\phi$ is a closed embedding and the scheme-theoretic image of $\Spec\phi$ is the closed subscheme defined by $\Spec\phi$ itself. Concretely writing this out, $\Spec\phi$ sends the unique prime ideal of $\mathbb{K}[\epsilon]/(\epsilon^2)$, $(\epsilon)$, to the maximal ideal of $\Spec \mathbb{K}[\x_1,\ldots, \x_n]$

$$(\Spec\phi)((\epsilon))=\phi^{-1}((\epsilon))=(\x_1-a_1,\ldots, \x_n-a_n)$$

Indeed, since $\phi(\x_i-a_i)=b_i\epsilon\in(\epsilon)$, we have $(\x_1-a_1,\ldots, \x_n-a_n)\subseteq\phi^{-1}((\epsilon))$, and since the left-hand side is a maximal ideal and the right-hand side is a proper ideal, this inclusion becomes an equality. That is, as a continuous map, $\Spec\phi$ sends the one-point space $\Spec \mathbb{K}[\epsilon]/(\epsilon^2)$ to a point of $\mathbb{A}^n$, $(a_1,\ldots, a_n)$.

Geometrically, $\Spec\phi$ corresponds, at a point of $\mathbb{A}^n$, $(a_1,\ldots, a_n)$, to the tangent vector $(b_1,\ldots, b_n)$. This can be verified from the fact that for any $f\in \mathbb{K}[\x_1,\ldots, \x_n]$,

$$\phi(f)=f(a)+\left(\sum_{i=1}^nb_i\frac{\partial f}{\partial \x_i}(a)\right)\epsilon$$

holds, that is, in $\phi(f)$, the $\epsilon$-coefficient is precisely the directional derivative at the point $(a_1,\ldots, a_n)$ in the direction of the vector $(b_1,\ldots, b_n)$. More generally, if instead of $\Spec \mathbb{K}[\epsilon]/(\epsilon^2)$ we consider $\Spec \mathbb{K}[\epsilon]/(\epsilon^k)$, for $\phi(f)$ the $\epsilon^j$-coefficients give the Taylor coefficients of $f$ of order $j$. In characteristic $0$, this amounts to looking at derivatives up to order $k-1$, but one must be careful that this is not the case in positive characteristic.
:::

Although in the above example we assumed that $X$ is an affine scheme, $\varphi^\sharp:\mathcal{O}_Y \rightarrow \varphi_\ast \mathcal{O}_X$ is anyway information contained in the scheme morphism $\varphi$, so there is nothing new here. The difference appears when we generalize $Y$ to a general scheme, because whenever an arbitrary affine open subset of $Y$, $V=\Spec B$, is given, the ideal

$$\mathcal{I}(V):=\ker(\varphi^\sharp(V))\subseteq B$$

defines a closed subscheme of $V$, but whether these can be glued together to produce a single closed subscheme defined on all of $Y$ is a different problem. Of course, for this we will use [Proposition 6](#prop6){: data-lid="5bjn7" }, and this assumption is satisfied in particular when $X$ is a reduced scheme or $\varphi$ is quasi-compact.

::: Corollary 12
Let a scheme morphism $\varphi: X \rightarrow Y$ be given. If $X$ is reduced, or $\varphi$ is quasi-compact, then the ideal sheaf $\mathcal{I}$ defined above satisfies the condition of [Proposition 6](#prop6){: data-lid="lgb5j" }, and therefore $\mathcal{I}$ defines a closed subscheme of $Y$, and this becomes the scheme-theoretic image of $\varphi$.
:::
::: Proof
Fix an affine open subset of $Y$, $V=\Spec B$, and $f\in B$, and let $U=\varphi^{-1}(V)$, $U'=\varphi^{-1}(D(f))$. Then what [Proposition 6](#prop6){: data-lid="xaoe3" } requires is that the canonical map $\mathcal{I}(V)_f \rightarrow \mathcal{I}(D(f))$ be an isomorphism. For convenience, denote the image of $f$ under $\varphi^\sharp(V): B \rightarrow \mathcal{O}_X(U)$ by $g$.

Since $\varphi$ is a morphism of locally ringed spaces, for each $x\in U$ the map $\varphi^\sharp_x$ is a local homomorphism, and therefore $U'$ is precisely the set of points where the stalk of $g$ does *not* belong to the maximal ideal of $\mathcal{O}_{X,x}$. In particular, for any affine open subset of $U$, $\Spec A$, we have $U'\cap \Spec A=D(g\vert_{\Spec A})$, so the restriction of $g$ to $U'$ is a unit of $\mathcal{O}_X(U')$, and therefore by the universal property of [\[Commutative Algebra\] §Localization, ⁋Proposition 6](/en/math/commutative_algebra/localization#prop6){: data-lid="2y2z0" } the restriction map $\mathcal{O}_X(U) \rightarrow \mathcal{O}_X(U')$ induces a canonical map

$$\alpha: \mathcal{O}_X(U)_g \rightarrow \mathcal{O}_X(U')$$

Also, from $\varphi^\sharp$ being a sheaf morphism, $\varphi^\sharp(D(f)): B_f \rightarrow \mathcal{O}_X(U')$ is the composition of the localization of $\varphi^\sharp(V)$, $B_f \rightarrow \mathcal{O}_X(U)_g$, and $\alpha$. But localization is an exact functor ([\[Commutative Algebra\] §Properties of Localization, ⁋Proposition 2](/en/math/commutative_algebra/properties_of_localization#prop2){: data-lid="jn26d" }), so

$$\ker\bigl(B_f \rightarrow \mathcal{O}_X(U)_g\bigr)=\ker\bigl(\varphi^\sharp(V)\bigr)_f=\mathcal{I}(V)_f$$

and therefore if $\alpha$ is injective, then $\mathcal{I}(D(f))=\ker (\varphi^\sharp(D(f)))=\mathcal{I}(V)_f$, so the condition of [Proposition 6](#prop6){: data-lid="xr2jl" } holds. Now we show that $\alpha$ is injective under each of the two assumptions.

First, suppose $\varphi$ is quasi-compact. Then $U$ is quasi-compact, so it is covered by finitely many affine open subsets $\Spec A_1,\ldots, \Spec A_n$. If $s\in \mathcal{O}_X(U)$ satisfies $s\vert_{U'}=0$, then for each $l$, the restriction of $s\vert_{\Spec A_l}\in A_l$ to $U'\cap \Spec A_l=D(g\vert_{\Spec A_l})$ is $0$, so for a suitable $n_l$ we have $(g^{n_l}s)\vert_{\Spec A_l}=0$. Since there are finitely many $l$, choosing a common $N$, $g^Ns$ on all $\Spec A_l$ is $0$, and therefore by the first condition of [\[Topology\] §Sheaves, ⁋Definition 1](/en/math/topology/sheaves#def1){: data-lid="ltp4e" }, $g^Ns=0$. That is, in $\mathcal{O}_X(U)_g$ we have $s/g^m=0$, so $\alpha$ is injective.

Now suppose $X$ is reduced. ([§Algebraic Structure of Schemes, ⁋Definition 1](/en/math/scheme_theory/algebra_of_schemes#def1){: data-lid="qgqty" }) Let $s\in \mathcal{O}_X(U)$ satisfy $s\vert_{U'}=0$ and consider $gs$; at points of $U'$ the stalk of $s$ is $0$, so the stalk of $gs$ is $0$, and at points outside $U'$, say $x$, the stalk of $g$ belongs to the maximal ideal of $\mathcal{O}_{X,x}$. Therefore, for any affine open subset of $U$, $\Spec A$, $(gs)\vert_{\Spec A}$ belongs to all prime ideals of $A$, and from [\[Commutative Algebra\] §Properties of Localization, ⁋Corollary 8](/en/math/commutative_algebra/properties_of_localization#cor8){: data-lid="fo9ma" } and the fact that $A$ is a reduced ring we obtain $(gs)\vert_{\Spec A}=0$. Then again by the sheaf condition, $gs=0$, and therefore $s/g^m=(gs)/g^{m+1}=0$, so $\alpha$ is injective.

From the above, by [Proposition 6](#prop6){: data-lid="tckrz" }, $\mathcal{I}$ uniquely induces a closed subscheme of $Y$, $\iota: Z \rightarrow Y$. That this contains the image of $\varphi$ in the sense of [Definition 10](#def10){: data-lid="p2lul" } is because for any affine open subset of $Y$, $V$, we have $\mathcal{I}_{Z/Y}(V)=\ker (\varphi^\sharp(V))$, so the composition $\mathcal{I}_{Z/Y}(V) \rightarrow \mathcal{O}_Y(V) \rightarrow (\varphi_\ast \mathcal{O}_X)(V)$ is $0$, and affine open subsets form a base for $Y$. Conversely, for any closed subscheme containing the image of $\varphi$, given as a closed subscheme of $Y$, $\iota': Z' \rightarrow Y$, the same composition is $0$, so $\mathcal{I}_{Z'/Y}(V)\subseteq \ker (\varphi^\sharp(V))=\mathcal{I}_{Z/Y}(V)$, and since both ideal sheaves are subsheaves of $\mathcal{O}_Y$, from this we obtain $\mathcal{I}_{Z'/Y}\subseteq \mathcal{I}_{Z/Y}$. Therefore, by [Lemma 9](#lem9){: data-lid="v1z20" } there exists a closed embedding $Z \rightarrow Z'$, and hence $Z$ is the smallest closed subscheme containing the image of $\varphi$, that is, the scheme-theoretic image of $\varphi$.
:::

Assuming the above condition and checking the image of $\varphi$ on each affine open subset, we can verify that the scheme-theoretic image of $\varphi$ is the closure of the image of $\varphi$ (as a continuous map) equipped with a structure sheaf defined on it.

Without the assumption of [Corollary 12](#cor12){: data-lid="k2yoc" }, this does not happen.

::: Example 13
Define a scheme $X$ by the formula

$$X=\coprod_{k\geq 1} \Spec \mathbb{K}[\epsilon]/(\epsilon^k)$$

and let $Y=\Spec \mathbb{K}[\x]$. Now, on each component of $X$, via $\x\mapsto \epsilon$ we can define a scheme morphism $X \rightarrow Y$. Then from [Example 11](#ex11){: data-lid="f2733" }, we know that the image of $X \rightarrow Y$ (as a continuous map) is the single point $0\in \mathbb{A}^1$. 

However, the scheme-theoretic image of the scheme morphism $\varphi:X \rightarrow Y$ is not $0$. To see this, let us observe the morphism $\varphi^\sharp:\mathcal{O}_Y \rightarrow \varphi_\ast \mathcal{O}_X$ between structure sheaves. Then, in $\mathcal{O}_Y$, for an element $f$ to satisfy $\varphi^\sharp(f)=0$, for any $k$ the approximation of $f$ to order $k$ must be $0$, so necessarily $f=0$. That is, $\mathcal{I}_{Z/Y}$ must be $0$, and from this we see that the scheme-theoretic image of $\varphi$ is all of $Y$.
:::

## Reduced Scheme Structure on a Closed Set

At the beginning of this post, for an affine scheme $\Spec A$, we were able to define on any closed set $Z(\mathfrak{a})$ two structure sheaves: $(\Spec\pi)_\ast \mathcal{O}_{\Spec A/\mathfrak{a}}$ and $\iota^{-1} \mathcal{O}_{\Spec A}$. Of these, we decided to consider $(\Spec\pi)_\ast \mathcal{O}_{\Spec A/ \mathfrak{a}}$ as the correct scheme structure defined on $Z(\mathfrak{a})$. Now we examine $\iota^{-1} \mathcal{O}_{\Spec A}$.

More generally, consider an arbitrary scheme $Y$ and, in $Y$, a closed subset $X$. Then, for any affine open subset of $Y$, $\Spec B$, the closed subset of $\Spec B$, $X\cap \Spec B$, can be written, by [§The Spectrum, ⁋Theorem 15](/en/math/scheme_theory/spectrums#thm15){: data-lid="trt0q" }, for a radical ideal of $B$, $\mathfrak{b}$, in the form $Z(\mathfrak{b})$. Moreover, since $\mathfrak{b}$ is by definition, among the ideals such that $X\cap \Spec B= Z(\mathfrak{b}')$, the largest ideal of $B$, by [Lemma 9](#lem9){: data-lid="0ly4e" } it is the smallest closed subscheme structure that can be given to $X\cap \Spec B$. Also, since the radical commutes with localization ($\sqrt{\mathfrak{b}}B_f=\sqrt{\mathfrak{b}B_f}$), these ideals satisfy the condition of [Proposition 6](#prop6){: data-lid="0brbv" }, and therefore glue into a single closed subscheme.

::: Definition 14
For a scheme $Y$ and an arbitrary closed subset $X$, giving $X$ the scheme structure defined above is called the *reduced scheme structure*, and is written as $X^\red$. 
:::

Then in particular when $X=Y$, for any affine subset $\Spec B$, writing $\Spec B=Z(0)$ gives $\mathfrak{b}=\mathfrak{N}(B)$, and $B/\mathfrak{N}(B)$ becomes a reduced ring. On the other hand, the sheaf morphism

$$\iota^{-1}\mathcal{O}_{\Spec A} \rightarrow (\Spec\pi\vert^{Z(\mathfrak{a})})_\ast \mathcal{O}_{\Spec A/\mathfrak{a}}$$

examined above is the canonical sheaf morphism induced from restriction, that is, from the adjunction $\iota^{-1}\dashv \iota_\ast$. However, this should not be confused with the scheme morphism given by [Lemma 9](#lem9){: data-lid="m2j7c" }, because $(Z(\mathfrak{a}),\iota^{-1}\mathcal{O}_{\Spec A})$ is generally not a scheme. For example, if $A=\mathbb{K}[\x]$ and $\mathfrak{a}=(\x)$, then $Z(\mathfrak{a})$ is a single point and the stalk on it is $\mathbb{K}[\x]_{(\x)}$; since the ring of global sections of an affine scheme consisting of a single point must have only one prime ideal, this locally ringed space is not isomorphic to any scheme. The canonical morphism actually given by [Lemma 9](#lem9){: data-lid="w3o0x" } is the one from the reduced structure defined by the radical of $\mathfrak{a}$ to the given structure, that is, $\Spec (A/\sqrt{\mathfrak{a}}) \rightarrow \Spec (A/\mathfrak{a})$.

---
**References**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).

---
