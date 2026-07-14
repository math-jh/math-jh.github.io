---
title: "Valuation Rings"
description: "We define separated and proper morphisms, and examine how they generalize the topological notions of Hausdorff and compactness into algebraic geometry. The structure of discrete valuation rings is also discussed."
excerpt: "Valuative criteria for separated and proper morphisms"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/valuative_criteria
sidebar: 
    nav: "scheme_theory-en"

date: 2024-05-24
weight: 14
translated_at: 2026-07-14T02:00:01+00:00
translation_source: kimi-cli
last_polished_at: 2026-07-14T02:00:01+00:00
---
In this post we define separated morphisms and proper morphisms. It is helpful to think of them as the algebraic-geometric transplants of the Hausdorff and compactness conditions from topology.

In previous posts we defined open subschemes ([§Schemes, ⁋Definition 4](/en/math/scheme_theory/schemes#def4)), examined closed embeddings and the resulting closed subschemes, and studied ideal sheaves ([§Closed Subschemes, ⁋Definition 2](/en/math/scheme_theory/closed_subschemes#def2), [⁋Definition 5](/en/math/scheme_theory/closed_subschemes#def5)). We now add the following concepts.

::: Definition 1
Let an arbitrary scheme $X$ be given.

1. A scheme morphism $f:X \rightarrow Y$ is called an *open immersion* if it induces an isomorphism between $X$ and an open subscheme of $Y$.
2. A morphism $f:X \rightarrow Y$ is called *projective* if for some suitable $n$, $f$ can be factored as a composition of a closed embedding and a projection of the form $X\hookrightarrow \mathbb{P}^n_Y \rightarrow Y$. ([§Projective Schemes](/en/math/scheme_theory/projective_schemes))
3. A morphism $f:X \rightarrow Y$ is called *quasi-projective* if it can be factored as a composition of a suitable open immersion $X \rightarrow X'$ and a projective morphism $X' \rightarrow Y$.
:::

Before starting the main discussion, it is helpful to examine the following example.

::: Example 2
Let $A$ be a discrete valuation ring. That is, $A$ is a principal ideal domain with exactly two prime ideals $(0)$ and $\mathfrak{m}$, of which $\mathfrak{m}$ is the unique maximal ideal consisting of the non-units.

Then $\Spec A$ consists of the two points $(0)$ and $\mathfrak{m}$, and since

$$Z((0))=\{(0),\mathfrak{m}\},\quad Z(\mathfrak{m})=\{\mathfrak{m}\}$$

the only nontrivial open subset of $\Spec A$ is

$$D(\mathfrak{m})=\{(0)\}.$$

On the other hand, if $\mathfrak{m}=(\pi)$, then by [§Spectra, ⁋Proposition 5](/en/math/scheme_theory/spectrums#prop5)

$$\mathcal{O}(D(\mathfrak{m}))=\mathcal{O}(D(\pi))\cong A_\pi\cong \Frac(A).$$

Of course $\mathcal{O}(\Spec A)\cong A$.

The two points of $\Spec A$ can be viewed geometrically as follows: each point is determined by the ring homomorphism from $A$ to its residue field, namely $\kappa((0))$ and $\kappa(\mathfrak{m})$. Using [§Spectra, ⁋Proposition 5](/en/math/scheme_theory/spectrums#prop5) again, from

$$\mathcal{O}_{(0)}\cong A_{(0)}\cong \Frac(A),\qquad \mathcal{O}_\mathfrak{m}\cong A_\mathfrak{m}$$

we obtain

$$\kappa((0))=\Frac(A), \qquad \kappa(\mathfrak{m})=A_\mathfrak{m}/\mathfrak{m}A_\mathfrak{m}\cong \Frac(A/\mathfrak{m})\cong A/\mathfrak{m}.$$
:::

Let us take note of what this example means. Since $Z((0))=\Spec A$, the closure of $(0)$ is all of $\Spec A$, so $(0)$ is the generic point and the unique closed point $\mathfrak{m}$ is a specialization of $(0)$. Removing the closed point yields the only nontrivial open subset $D(\mathfrak{m})=\{(0)\}$, and the functions on it were $K=\Frac(A)$; thus the canonical morphism $\Spec K \rightarrow \Spec A$ is exactly this "punctured" inclusion. Geometrically, one may think of $\Spec A$ as a germ of a curve at a point, and $\Spec K$ as that germ with the point removed.

Then a morphism $\Spec K \rightarrow X$ is a punctured curve germ mapping into $X$, and extending it to $\Spec A \rightarrow X$ amounts to recovering the missing point inside $X$ and gluing the curve back together, i.e., finding the limit of the curve. The statement that there is at most one such extension is separatedness, and that there is exactly one is properness; this is the content of the two criteria we will see below. This exactly mirrors the topological picture: limits are unique in a Hausdorff space, and limits always exist in a compact space.

## Separated Morphisms

::: Definition 3
For a scheme morphism $f:X \rightarrow Y$, we define the *diagonal morphism* as $\Delta: X \rightarrow X \times_Y X$.

![diagonal_morphism](/assets/images/Math/Scheme_Theory/Valuative_Criteria-1.svg){:style="width:13.51em" class="invert" .align-center}

If $\Delta$ is a closed embedding, we call $f$ *separated*, and say $X$ is *separated* over $Y$. If $X$ is separated over $\Spec \mathbb{Z}$, we simply call $X$ a *separated* scheme.
:::

In algebraic geometry, separatedness is regarded as the property replacing Hausdorffness, thanks to the following proposition.

::: Proposition 4
The following are equivalent for $f:X \rightarrow Y$: $f$ is separated, and the image of $X$ under the diagonal morphism $\Delta: X \rightarrow X\times_YX$ is a closed set.
:::
::: Proof
By definition, if $f$ is separated then $\Delta(X)$ is closed is obvious. Thus we assume $\Delta(X)$ is closed and show that $\Delta$ is a closed embedding. That $\Delta(X)$ is a closed subset of $X\times_YX$ is clear, so it suffices to show that $\mathcal{O}_{X\times_YX} \rightarrow \Delta_\ast \mathcal{O}_X$ is surjective. On the other hand, surjectivity of a sheaf morphism can be checked on stalks. Choose an arbitrary $p\in X$. Then we can first choose an open affine subset $U$ containing $p$, and if necessary restrict $U$ so that $f(U)$ lies in some open affine subset $V$ of $Y$. Then $U\times_VU$ is an open neighborhood of $\Delta(p)$, and on it $\Delta: U \rightarrow U\times_VU$ is a closed embedding by the following [Lemma 5](#lem5), and the proof is complete.
:::

::: Lemma 5
Any morphism between affine schemes is always separated.
:::
::: Proof
If $X=\Spec A, Y=\Spec B$, then $\Delta$ is induced by the ring homomorphism

$$A\otimes_BA \rightarrow A;\quad a\otimes a'\mapsto aa'$$

and this is surjective, so it is obvious.
:::

An example of a non-separated scheme is the line with double origin constructed in [§Schemes, ⁋Example 10](/en/math/scheme_theory/schemes#ex10). For convenience, let us denote this scheme by $X$. Then $X\times X$ will look like the ordinary coordinate plane away from the axes, but along the coordinate axes, especially at the origin, there will be four origins. Intuitively, if we think about how $\Delta$ sits inside $X\times X$, away from the axes it will look like the usual diagonal, but when the two origins of $X$ are mapped into $X\times X$ via $\Delta$, it is unclear which two of the four origins they land in. In fact, all four origins lie in the closure of $\Delta(X)$, so we see that it is not separated. This space was, as expected, an example of a non-Hausdorff space in topology.

::: Theorem 6
For a Noetherian scheme $X$ and a scheme morphism $f:X \rightarrow Y$, the following are equivalent: $f$ is separated; and for every valuation ring $A$ and its quotient field $K=\Frac(A)$, given any scheme morphisms $\Spec A \rightarrow Y$, $\Spec K \rightarrow X$ and the following commutative diagram

![valuative_criterion](/assets/images/Math/Scheme_Theory/Valuative_Criteria-2.svg){:style="width:8.27em" class="invert" .align-center}

with the outer square given, there is at most one $\Spec A \rightarrow X$ making the whole diagram commute.
:::
::: Proof
That the outer square is given means that morphisms $u:\Spec K \rightarrow X$ and $v: \Spec A \rightarrow Y$ are given such that for the inclusion $A\hookrightarrow K$ inducing $j: \Spec K \rightarrow \Spec A$, we have $f\circ u=v\circ j$; a lifting of this square means a $g:\Spec A \rightarrow X$ satisfying $g\circ j=u$ and $f\circ g=v$.

Throughout the proof we use two standard facts. The first is the existence theorem for valuation rings: given a field $K$ and a local subring $\mathcal{O}$ inside it, there exists a valuation ring $A$ with $\Frac(A)=K$, $\mathcal{O}\subseteq A$, and $\mathfrak{m}_A\cap \mathcal{O}=\mathfrak{m}_\mathcal{O}$. In this case we say $A$ *dominates* $\mathcal{O}$, and the existence of such $A$ is a standard result in commutative algebra obtained from Zorn's lemma. The second is that for a field $K$, a morphism $\Spec K \rightarrow X$ corresponds bijectively to a pair of a point $x\in X$ and a field homomorphism $\kappa(x) \rightarrow K$. This follows from the fact that when $X=\Spec B$, a ring homomorphism $B \rightarrow K$ gives the pair of its kernel, a prime ideal $\mathfrak{p}$, and $\kappa(\mathfrak{p}) \rightarrow K$; the general case is handled by choosing an affine open neighborhood of $x$.

First assume $f$ is separated, and suppose two liftings $g_1, g_2$ of the above square are given. Since $f\circ g_1=f\circ g_2=v$, by the universal property of the fiber product there exists a unique $h:\Spec A \rightarrow X\times_YX$ such that $p_1\circ h=g_1$, $p_2\circ h=g_2$. Here $p_1,p_2$ are the two projections. Now since $\Delta$ is a closed embedding, the base change

$$Z=\Spec A\times_{X\times_YX}X \longrightarrow \Spec A$$

is also a closed embedding. That closed embeddings are stable under base change follows from the affine-local fact that the base change of $B \rightarrow B/\mathfrak{b}$ is $C \rightarrow C\otimes_B(B/\mathfrak{b})\cong C/\mathfrak{b}C$, which is still surjective. ([§Closed Subschemes, ⁋Proposition 3](/en/math/scheme_theory/closed_subschemes#prop3))

On the other hand $p_1\circ h\circ j=g_1\circ j=u$ and $p_2\circ h\circ j=g_2\circ j=u$, and $p_1\circ \Delta\circ u=u$ and $p_2\circ\Delta\circ u=u$, so by the uniqueness in the universal property we have $h\circ j=\Delta\circ u$. Therefore $j$ factors through the pullback $Z$, and in particular the image of $Z \rightarrow \Spec A$ is a closed set containing the image of $j$, namely the zero ideal $(0)$ of $A$. Since $A$ is a domain, $(0)$ is the generic point of $\Spec A$ ([§Topology of Schemes, ⁋Example 5](/en/math/scheme_theory/topology_of_schemes#ex5)), and thus the only closed subset of $\Spec A$ containing $(0)$ is $\Spec A$ itself. Then $Z$ is a closed subscheme of $\Spec A$ of the form $\Spec(A/\mathfrak{a})$ for some ideal $\mathfrak{a}\subseteq A$ ([§Closed Subschemes, ⁋Proposition 3](/en/math/scheme_theory/closed_subschemes#prop3)), and the fact that its image is all of $\Spec A$ means that $\mathfrak{a}$ is contained in every prime ideal of $A$, i.e.,

$$\mathfrak{a}\subseteq \sqrt{(0)}=(0).$$

The last equality comes from the fact that $A$ is a domain. Therefore $Z \rightarrow \Spec A$ is an isomorphism, which means that $h$ factors through $\Delta$, i.e., $h=\Delta\circ g$ for some $g:\Spec A \rightarrow X$. Then

$$g_1=p_1\circ h=p_1\circ \Delta\circ g=g,\qquad g_2=p_2\circ h=p_2\circ\Delta\circ g=g$$

so $g_1=g_2$. In this direction the assumption that $X$ is Noetherian is not used.

Conversely, assume that for every square there is at most one lifting. By [Proposition 4](#prop4) it suffices to show that $\Delta(X)$ is a closed subset of $X\times_YX$.

First we observe that every point of $\cl(\Delta(X))$ is a specialization of some point of $\Delta(X)$. Since $X$ is a Noetherian scheme, it is also Noetherian as a topological space ([§Topology of Schemes, ⁋Definition 14](/en/math/scheme_theory/topology_of_schemes#def14)), and thus has finitely many irreducible components $X_1,\ldots, X_r$. ([[Topology] §Dimension, ⁋Proposition 13](/en/math/topology/dimension#prop13)) Each $X_i$ is an irreducible closed subset, so it has a generic point $\eta_i$ ([§Spectra, ⁋Proposition 16](/en/math/scheme_theory/spectrums#prop16)), and $X=\bigcup_{i=1}^r\cl(\{\eta_i\})$. Now since $\Delta$ is continuous, $\Delta(X)\subseteq \bigcup_{i=1}^r \cl(\{\Delta(\eta_i)\})$ and the right-hand side is a finite union hence closed; conversely each $\Delta(\eta_i)$ lies in $\Delta(X)$, so we obtain

$$\cl(\Delta(X))=\bigcup_{i=1}^r\cl(\{\Delta(\eta_i)\}).$$

That is, every point of $\cl(\Delta(X))$ is a specialization of some $\Delta(\eta_i)\in \Delta(X)$. ([§Topology of Schemes, ⁋Definition 2](/en/math/scheme_theory/topology_of_schemes#def2)) Therefore, if we show that $\Delta(X)$ is closed under specialization, then $\Delta(X)=\cl(\Delta(X))$ and the proof is finished.

Let $\xi=\Delta(x)\in \Delta(X)$ and $\eta\in\cl(\{\xi\})$. Giving the closed set $T=\cl(\{\xi\})$ a reduced scheme structure ([§Closed Subschemes, ⁋Definition 14](/en/math/scheme_theory/closed_subschemes#def14)), $T$ is an integral scheme with generic point $\xi$. Choose an affine open subset $\Spec B\subseteq T$ containing $\eta$. Since the generic point belongs to every nonempty open set, $\Spec B$ also contains $\xi$, and $B$ is a domain and $\xi$ corresponds to the zero ideal of $B$, so

$$K:=\kappa(\xi)=\mathcal{O}_{T,\xi}=\Frac(B), \qquad \mathcal{O}:=\mathcal{O}_{T,\eta}=B_\mathfrak{q}\subseteq K$$

where $\mathfrak{q}$ is the prime ideal corresponding to $\eta$. In particular $\mathcal{O}$ is a local domain with $\Frac(\mathcal{O})=K$. Choosing a valuation ring $A$ of $K$ dominating $\mathcal{O}$ by the existence theorem quoted above, the local homomorphism $\mathcal{O} \rightarrow A$ induces a morphism

$$q:\Spec A \longrightarrow \Spec \mathcal{O} \longrightarrow T \hookrightarrow X\times_YX$$

which sends the generic point $(0)$ of $\Spec A$ to $\xi$ and the closed point $\mathfrak{m}_A$ to $\eta$.

Now set $g_1=p_1\circ q$, $g_2=p_2\circ q$, and since $f\circ p_1=f\circ p_2$ we have a well-defined $w=f\circ g_1=f\circ g_2:\Spec A \rightarrow Y$. As seen in the proof of [Proposition 4](#prop4), choosing an affine open neighborhood $U$ of $x$ and an affine open subset $V$ of $Y$ containing $f(U)$, we have that $U\times_VU$ is an open neighborhood of $\xi$ in $X\times_YX$ and on it $\Delta$ is a closed embedding ([Lemma 5](#lem5)), so the map on stalks $\mathcal{O}_{X\times_YX,\xi} \rightarrow \mathcal{O}_{X,x}$ is surjective and therefore $\kappa(\xi) \rightarrow \kappa(x)$ is also surjective. On the other hand $p_1\circ\Delta=\id_X$, so the composition $\kappa(x) \rightarrow \kappa(\xi) \rightarrow \kappa(x)$ is the identity, and thus the two maps are inverse isomorphisms of each other. Hence $K=\kappa(\xi)\cong\kappa(x)$. Under this identification, let $u:\Spec K \rightarrow X$ be the canonical morphism defined by the point $x$ and $\kappa(x)\cong K$; then $\Delta\circ u$ is the canonical morphism defined by the point $\xi$ and $\kappa(\xi)\cong K$, and this equals $q\circ j$. Indeed, $q\circ j$ has image $\xi$ and induces the identity on $K$ on residue fields because $\kappa(\xi)=\Frac(\mathcal{O})=K$. Therefore

$$g_1\circ j=p_1\circ q\circ j=p_1\circ \Delta\circ u=u,\qquad g_2\circ j=p_2\circ q\circ j=p_2\circ\Delta\circ u=u$$

and $f\circ g_1=f\circ g_2=w$, so $g_1$ and $g_2$ are two liftings of the square given by $u$ and $w$. By assumption $g_1=g_2$, and then $\Delta\circ g_1$ and $q$ give $g_1$ and $g_2=g_1$ respectively when composed with $p_1$, $p_2$, so by the universal property of the fiber product $q=\Delta\circ g_1$. Therefore

$$\eta=q(\mathfrak{m}_A)=\Delta(g_1(\mathfrak{m}_A))\in \Delta(X)$$

and $\Delta(X)$ is closed under specialization. Combined with the previous observation, $\Delta(X)=\cl(\Delta(X))$, so $\Delta(X)$ is a closed set, and by [Proposition 4](#prop4) $f$ is separated.
:::

On the other hand, it is known that if $Y$ is Noetherian and $f$ is a finite type morphism, then in the above theorem one may replace arbitrary valuation rings by arbitrary discrete valuation rings. With this change, it becomes easier to explain the theorem using geometric intuition: thinking of $\Spec A$ as a germ of a smooth curve and $\Spec K$ as that germ with one point removed, the theorem says that there is only one way to embed such $\Spec K\hookrightarrow \Spec A$.

From this we obtain the following.

::: Corollary 7
For Noetherian schemes,

1. Open immersions and closed embeddings are both separated.
2. The composition of two separated morphisms is separated.
3. Separated morphisms are preserved under base change.
4. Separated morphisms are preserved under fiber products.
5. If $f:X \rightarrow Y$, $g:Y \rightarrow Z$ are scheme morphisms and $g\circ f$ is a separated morphism, then $f$ is also a separated morphism.
:::

## Proper Morphisms

::: Definition 8
A morphism $f:X \rightarrow Y$ is called *universally closed* if $f$ is a closed map and for every $Y' \rightarrow Y$, the map $X\times_Y Y' \rightarrow Y'$ is also closed. A finite type morphism that is separated and universally closed is called a *proper morphism*.
:::

Just as in [Theorem 6](#thm6), there is a valuative criterion for proper morphisms.

::: Theorem 9
For a Noetherian scheme $X$ and a finite type scheme morphism $f:X \rightarrow Y$, the following are equivalent: $f$ is proper; and for every valuation ring $A$ and its quotient field $K=\Frac(A)$, given any scheme morphisms $\Spec A \rightarrow Y$, $\Spec K \rightarrow X$ and the following commutative diagram

![valuative_criterion](/assets/images/Math/Scheme_Theory/Valuative_Criteria-2.svg){:style="width:8.27em" class="invert" .align-center}

with the outer square given, there exists exactly one $\Spec A \rightarrow X$ making the whole diagram commute.
:::
::: Proof
As in the proof of [Theorem 6](#thm6), we write the outer square as $u:\Spec K \rightarrow X$, $v:\Spec A \rightarrow Y$, $j:\Spec K \rightarrow \Spec A$, and continue to use the two standard facts cited in that proof. Namely, every local subring in a field $K$ is dominated by a valuation ring $A$ with $\Frac(A)=K$, and a morphism $\Spec K \rightarrow X$ is the same as a pair of a point $x\in X$ and a field homomorphism $\kappa(x) \rightarrow K$. To this we add the following maximality of valuation rings. If a local subring $\mathcal{O}\subseteq K$ is given that dominates a valuation ring $A$ of $K$, then $\mathcal{O}=A$. Indeed, if $c\in\mathcal{O}$ is nonzero and $c\notin A$, then by the definition of a valuation ring $c^{-1}\in A$, and since $c\notin A$, $c^{-1}$ is not a unit of $A$. Hence $c^{-1}\in\mathfrak{m}_A\subseteq \mathfrak{m}_\mathcal{O}$, but $c\in\mathcal{O}$ so $c^{-1}$ is a unit of $\mathcal{O}$, a contradiction. Therefore $\mathcal{O}\subseteq A$, and by the definition of domination $A\subseteq\mathcal{O}$, so $\mathcal{O}=A$.

First assume $f$ is proper. Since a proper morphism is separated, by [Theorem 6](#thm6) there is at most one lifting, so we only need to show existence. Base changing along $v$, we obtain $X_A=X\times_Y\Spec A$ and the projection $\pi:X_A \rightarrow \Spec A$. Since $f$ is universally closed, $\pi$ is a closed map. ([Definition 8](#def8)) On the other hand, $u$ and $j$ induce by the universal property of the fiber product a morphism $\tilde{u}:\Spec K \rightarrow X_A$ over $\Spec A$, and finding an extension of $\tilde{u}$ to a section of $\pi$ of the form $\Spec A \rightarrow X_A$ and projecting it to $X$ gives the desired lifting.

Let $\xi\in X_A$ be a point in the image of $\tilde{u}$ and give $Z=\cl(\{\xi\})$ a reduced scheme structure. ([§Closed Subschemes, ⁋Definition 14](/en/math/scheme_theory/closed_subschemes#def14)) Since $\pi\circ\tilde{u}=j$, $\pi(\xi)$ is the generic point $(0)$ of $\Spec A$, and since $\pi$ is a closed map, $\pi(Z)$ is a closed set containing $(0)$, hence all of $\Spec A$. Therefore there exists $z\in Z$ with $\pi(z)=\mathfrak{m}_A$.

Let us examine the residue fields. The map $\kappa((0))=K \rightarrow K$ induced by $\pi\circ \tilde{u}=j$ at $(0)$ is the identity, and this is the composition of the map $K\rightarrow\kappa(\xi)$ induced by $\pi$ and the map $\kappa(\xi) \rightarrow K$ induced by $\tilde{u}$, so the two maps are inverse isomorphisms of each other. Hence $\kappa(\xi)\cong K$. Then since $Z$ is an integral scheme with generic point $\xi$, as in the proof of [Theorem 6](#thm6) we choose an affine open subset containing $z$ and know that

$$\mathcal{O}:=\mathcal{O}_{Z,z}\subseteq \kappa(\xi)=K,\qquad \Frac(\mathcal{O})=K.$$

Also the map $A=\mathcal{O}_{\Spec A,\mathfrak{m}_A} \rightarrow \mathcal{O}_{Z,z}$ induced by $\pi\vert_Z$ is a local homomorphism, and since the map $K \rightarrow \kappa(\xi)=K$ it induces at the generic point is the identity, this map is an inclusion of subrings of $K$. That is, $\mathcal{O}$ is a local subring of $K$ dominating $A$, and by the maximality above we have $\mathcal{O}_{Z,z}=A$.

Then we obtain the canonical morphism $\Spec A=\Spec\mathcal{O}_{Z,z} \rightarrow Z \hookrightarrow X_A$, and its composition with $\pi$ corresponds to the identity on $A$ at the ring level, so it is a section of $\pi$. The restriction of this section to $\Spec K$ has image $\xi$ and induces the identity on $K$ on residue fields because $\kappa(\xi)=K$, so it equals $\tilde{u}$. Therefore projecting this section to $X$ gives $g:\Spec A \rightarrow X$ with $g\circ j=u$ and $f\circ g=v$.

Conversely, assume the criterion holds. From the uniqueness of the lifting and [Theorem 6](#thm6) we get that $f$ is separated, and finite type is assumed, so we only need to show that $f$ is universally closed. Since we are working in the category of Noetherian schemes, we restrict base changes $Y' \rightarrow Y$ to those between Noetherian schemes.

First, the criterion is stable under base change. Suppose $Y' \rightarrow Y$ and $X'=X\times_YY'$, $f':X' \rightarrow Y'$ are given, and $\Spec K \rightarrow X'$ and $\Spec A \rightarrow Y'$ form an outer square for $f'$. Composing these with $X' \rightarrow X$, $Y' \rightarrow Y$ gives an outer square for $f$, so there is a unique lifting $g:\Spec A \rightarrow X$, and $g$ and $\Spec A \rightarrow Y'$ give a unique $g':\Spec A \rightarrow X'$ by the universal property. $g'\circ j$ and the given $\Spec K \rightarrow X'$ are equal because they give the same result when composed with $X' \rightarrow X$ and $X' \rightarrow Y'$, so $g'$ is a lifting for $f'$. Uniqueness also follows by composing two liftings with $X' \rightarrow X$ and using the uniqueness of the lifting for $f$. On the other hand, finite type morphisms are stable under base change and a finite type scheme over a Noetherian scheme is again Noetherian, so $X'$ is Noetherian and $f'$ is of finite type. Therefore, if we show that $f$ is a closed map whenever a Noetherian scheme $X$ and a finite type morphism $f:X \rightarrow Y$ satisfy the existence part of the criterion, then applying this to all base changes finishes the proof.

To show this, choose a closed subset $T$ of $X$ and give it a reduced scheme structure. The closed embedding $T\hookrightarrow X$ is a finite morphism, so ([§Closed Subschemes, ⁋Proposition 4](/en/math/scheme_theory/closed_subschemes#prop4)) it is of finite type, and thus $T$ is a Noetherian scheme and $f\vert_T:T \rightarrow Y$ is also of finite type. Moreover $f\vert_T$ inherits the existence part of the criterion. Indeed, if $\Spec K \rightarrow T$ and $\Spec A \rightarrow Y$ form a square for $f\vert_T$, applying the criterion to $\Spec K \rightarrow T\hookrightarrow X$ gives a lifting $g_0:\Spec A \rightarrow X$. Every point of $\Spec A$ is a specialization of the generic point $(0)$ and morphisms preserve specialization, so $g_0(\Spec A)\subseteq \cl(\{g_0((0))\})\subseteq T$, and since $\Spec A$ is reduced, $g_0$ factors through $T$. The last fact is obtained as follows. Suppose the image of a morphism $\varphi:S \rightarrow X$ from a reduced scheme $S$ lies in a closed subset $T$, and choose an affine open subset $\Spec B$ of $X$ and an affine open subset $\Spec R$ of $\varphi^{-1}(\Spec B)$. If $T\cap \Spec B=Z(\mathfrak{b})$ ($\mathfrak{b}$ a radical ideal), then the reduced structure of $T$ is $\Spec (B/\mathfrak{b})$ on it, and the corresponding ring homomorphism $\psi:B \rightarrow R$ satisfies $\mathfrak{b}\subseteq \psi^{-1}(\mathfrak{p})$ for every prime ideal $\mathfrak{p}\subseteq R$, so

$$\psi(\mathfrak{b})\subseteq \bigcap_{\mathfrak{p}\in\Spec R}\mathfrak{p}=\sqrt{(0)}=(0).$$

That is, $\psi$ uniquely factors through $B/\mathfrak{b}$, and these local factorizations glue by uniqueness.

Therefore it suffices to show that $f(T)=f\vert_T(T)$ is a closed set, and ultimately it is enough to show that the image $f(X)$ of a finite type morphism $f:X \rightarrow Y$ (with $X$ Noetherian) satisfying the existence part of the criterion is closed.

First we show that $f(X)$ is closed under specialization. Let $y_1=f(x_1)\in f(X)$ and $y_0\in\cl(\{y_1\})$. Giving $W=\cl(\{y_1\})$ a reduced scheme structure, $W$ is an integral scheme with generic point $y_1$, and as before $\mathcal{O}=\mathcal{O}_{W,y_0}$ is a local domain with $\Frac(\mathcal{O})=\kappa(y_1)$. Now set $K=\kappa(x_1)$ and view $\mathcal{O}$ as a local subring of $K$ via the field homomorphism $\kappa(y_1)\hookrightarrow K$ induced by $f$. Then there exists a valuation ring $A$ of $K$ dominating $\mathcal{O}$, and from this we obtain two morphisms

$$\Spec A \longrightarrow \Spec\mathcal{O} \longrightarrow W\hookrightarrow Y,\qquad u:\Spec K \longrightarrow X$$

where $u$ is the canonical morphism defined by the point $x_1$ and $\kappa(x_1)=K$. These form an outer square because the two compositions $\Spec K \rightarrow Y$ are both the canonical morphism defined by the point $y_1$ and the field homomorphism $\kappa(y_1)\hookrightarrow K$. By the existence part of the criterion there is a lifting $g_0:\Spec A \rightarrow X$, and since $\Spec A \rightarrow \Spec\mathcal{O}$ comes from a local homomorphism, $\mathfrak{m}_A$ maps to $\mathfrak{m}_\mathcal{O}$, i.e., to $y_0$. Therefore $f(g_0(\mathfrak{m}_A))=y_0$ and $y_0\in f(X)$.

Finally we repeat the topological observation from the proof of [Theorem 6](#thm6) verbatim. If $\eta_1,\ldots,\eta_r$ are the generic points of the irreducible components $X_1,\ldots,X_r$ of $X$, then $X=\bigcup_{i=1}^r\cl(\{\eta_i\})$, so

$$\cl(f(X))=\bigcup_{i=1}^r\cl(\{f(\eta_i)\})$$

and thus every point of $\cl(f(X))$ is a specialization of a point of $f(X)$. Since we showed above that $f(X)$ is closed under specialization, we have $f(X)=\cl(f(X))$.
:::

Similarly, the following corollary holds.

::: Corollary 10
For Noetherian schemes,

1. A closed embedding is proper.
2. The composition of proper morphisms is proper.
3. Proper morphisms are preserved under base change.
4. Proper morphisms are preserved under fiber products.
5. If $f:X \rightarrow Y$, $g:Y \rightarrow Z$ are scheme morphisms and $g\circ f$ is a proper morphism, then $f$ is also a proper morphism.
:::

::: Theorem 11
A projective morphism between Noetherian schemes is a proper morphism, and a quasi-projective morphism is a separated, finite type morphism.
:::
::: Proof
The heart of the proof is that $\pi:\mathbb{P}^n_\mathbb{Z} \rightarrow \Spec\mathbb{Z}$ is proper, which is obtained by directly verifying the criterion of [Theorem 9](#thm9). First, $\mathbb{P}^n_\mathbb{Z}$ is obtained by gluing $n+1$ affine charts

$$U_i=\Spec \mathbb{Z}[\x_0/\x_i,\ldots,\x_n/\x_i]\qquad (i=0,\ldots,n)$$

along $U_i\cap U_j=D(\x_j/\x_i)\subseteq U_i$. Here $\x_i/\x_i=1$, so each $U_i$ is the spectrum of an $n$-variable polynomial ring over $\mathbb{Z}$. In particular each $U_i$ is the spectrum of a Noetherian ring, and since there are finitely many charts, $\mathbb{P}^n_\mathbb{Z}$ is a Noetherian scheme, and $\pi$ is of finite type. ([§Properties of Scheme Morphisms, ⁋Definition 13](/en/math/scheme_theory/properties_of_scheme_morphisms#def13))

That $\pi$ is separated is checked directly on the charts. $\mathbb{P}^n_\mathbb{Z}\times_\mathbb{Z}\mathbb{P}^n_\mathbb{Z}$ is covered by affine open subsets $U_i\times_\mathbb{Z}U_j$ and since $p_1\circ\Delta=p_2\circ\Delta=\id$, we have $\Delta^{-1}(U_i\times_\mathbb{Z}U_j)=U_i\cap U_j$. Now looking at the ring homomorphism induced by $\Delta$ on this,

$$\mathbb{Z}[\x_0/\x_i,\ldots,\x_n/\x_i]\otimes_\mathbb{Z}\mathbb{Z}[\x_0/\x_j,\ldots,\x_n/\x_j] \longrightarrow \mathcal{O}(U_i\cap U_j)=\mathbb{Z}[\x_0/\x_i,\ldots,\x_n/\x_i]_{\x_j/\x_i}$$

the right-hand side is generated over $\mathbb{Z}$ by the $\x_l/\x_i$ and $(\x_j/\x_i)^{-1}=\x_i/\x_j$; the former come from the first factor and the latter from the second, so this map is surjective. Therefore $\Delta$ is a closed embedding on each $U_i\times_\mathbb{Z}U_j$, and since closed embeddings are affine-local on the target ([§Closed Subschemes, ⁋Proposition 3](/en/math/scheme_theory/closed_subschemes#prop3)), $\Delta$ itself is a closed embedding.

Since $\Spec \mathbb{Z}$ is a terminal object in the category of schemes, giving the outer square for a valuation ring $A$ and $K=\Frac(A)$ is the same as giving a morphism $\Spec K \rightarrow \mathbb{P}^n_\mathbb{Z}$. The uniqueness of the lifting follows from $\pi$ being separated and [Theorem 6](#thm6), so we only need to show existence. Since $\Spec K$ is a single point, the image of the given morphism lies in some chart $U_i$, and thus this morphism corresponds to a ring homomorphism

$$\mathbb{Z}[\x_0/\x_i,\ldots,\x_n/\x_i] \longrightarrow K.$$

Let the image of $\x_j/\x_i$ be $a_j\in K$; then $a_i=1$. Now define $s\preceq t$ on $K^\times$ by $t/s\in A$; then by the definition of a valuation ring, for any $s,t$ either $s\preceq t$ or $t\preceq s$, and if $t/s\in A$ and $r/t\in A$ then $r/s=(r/t)(t/s)\in A$, so $\preceq$ is a total preorder on $K^\times$. Since $a_i=1\neq 0$, the finite set $\{a_j : a_j\neq 0\}$ is nonempty, and thus we can choose a minimal element $a_k$ of this set. That is, for every $j$

$$b_j:=a_j/a_k\in A.$$

(If $a_j=0$, then $b_j=0\in A$.) In particular $b_k=1$, so the ring homomorphism

$$\mathbb{Z}[\x_0/\x_k,\ldots,\x_n/\x_k] \longrightarrow A;\qquad \x_j/\x_k\mapsto b_j$$

is defined and gives a morphism $\Spec A \rightarrow U_k\subseteq\mathbb{P}^n_\mathbb{Z}$. To show that this is a lifting, it suffices to check that its composition with $A\hookrightarrow K$ equals the originally given morphism. Since $a_k\neq 0$, the original ring homomorphism sends $\x_k/\x_i$ to the unit $a_k$ of $K$, and thus the image of the original morphism lies in $D(\x_k/\x_i)=U_i\cap U_k$. Then on $U_k$ this morphism is given by $\x_j/\x_k\mapsto a_j/a_k=b_j$ via the transition relation

$$\x_j/\x_k=(\x_j/\x_i)\cdot(\x_k/\x_i)^{-1},$$

so it exactly equals the restriction to $\Spec K$ of the $\Spec A \rightarrow U_k$ constructed above. Hence the existence part of the criterion holds, and by [Theorem 9](#thm9) $\pi$ is proper.

For any Noetherian scheme $Y$, we have $\mathbb{P}^n_Y=\mathbb{P}^n_\mathbb{Z}\times_{\Spec\mathbb{Z}}Y$. This is because when $Y=\Spec B$, the chart $\Spec B[\x_0/\x_i,\ldots,\x_n/\x_i]$ of $\mathbb{P}^n_B$ coincides with $U_i\times_{\Spec\mathbb{Z}}\Spec B$, and for general $Y$ we glue these. Therefore by [Corollary 10](#cor10) $\mathbb{P}^n_Y \rightarrow Y$ is proper, and in particular of finite type, so $\mathbb{P}^n_Y$ is a Noetherian scheme.

Now if $f:X \rightarrow Y$ is projective, then $f$ is the composition of a closed embedding $X\hookrightarrow \mathbb{P}^n_Y$ and the projection $\mathbb{P}^n_Y \rightarrow Y$. ([Definition 1](#def1)) Closed embeddings are proper and the composition of two proper morphisms is proper ([Corollary 10](#cor10)), so $f$ is proper.

Finally, suppose $f:X \rightarrow Y$ is quasi-projective, and factor it as a composition $f=g\circ\iota$ of an open immersion $\iota: X \rightarrow X'$ and a projective morphism $g:X' \rightarrow Y$. ([Definition 1](#def1)) By what we just showed, $g$ is proper, hence separated and of finite type. On the other hand, open immersions are separated and the composition of two separated morphisms is separated ([Corollary 7](#cor7)), so $f$ is separated. Also an open immersion is locally of finite type, and since $X$ is Noetherian, the preimage of any affine open subset of $X'$ under $\iota$ is quasi-compact as an open subset of a Noetherian space. That is, $\iota$ is of finite type ([§Properties of Scheme Morphisms, ⁋Definition 13](/en/math/scheme_theory/properties_of_scheme_morphisms#def13)), and the composition of two finite type morphisms is of finite type, so $f$ is also of finite type.
:::
