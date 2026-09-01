---
title: "Functors of Points"
description: "This post develops the viewpoint of regarding schemes through their functors of points, using the language of the Yoneda lemma and representable functors. It then examines key examples such as affine space, projective space, Grassmannians, and fiber products."
excerpt: "Functor of points, Yoneda embedding, representability, and fiber products"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/functor_of_points
sidebar: 
    nav: "scheme_theory-en"

date: 2026-08-23
weight: 22
translated_at: 2026-08-28T00:45:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-08-28T00:45:05+00:00
---
We now begin preparing to extend the language of schemes further. For this we need the functor of points viewpoint that we saw in [§Morphisms of Schemes, ⁋Definition 6](/en/math/scheme_theory/morphism_of_schemes#def6). This was already defined in [§Morphisms of Schemes, ⁋Definition 9](/en/math/scheme_theory/morphism_of_schemes#def9): to study a scheme $X$, we look at the collection of $T$-points of $X$ for every possible test scheme $T$. In other words, we consider the functor

$$h_X=\Hom_\Sch(-,X): \Sch^\op \rightarrow \Set$$

Our first goal is to verify, via the Yoneda lemma, that this functor determines $X$ completely up to isomorphism, and to see how this functorial viewpoint provides a natural language for working with affine space, projective space, Grassmannians, fiber products, and so forth.

Before starting the main discussion, let us fix notation. For each scheme $T$ we write $h_X(T)=\Hom_\Sch(T,X)$ as $X(T)$, and for a scheme morphism $\tau: T' \rightarrow T$, the map $h_X(\tau): X(T) \rightarrow X(T')$ is the composition $h_X(\tau)(\psi)=\psi\circ \tau$. In particular, when $T=\Spec A$ we write $X(\Spec A)$ simply as $X(A)$, and as above, we also call an element of the set $X(T)$ a *$T$-valued point*. In these terms, $X(\tau)$ pulls a $T$-point of $X$ back along $\tau$ to a $T'$-point.

There is also functoriality in the $X$ direction. Given a scheme morphism $\varphi: X\rightarrow Y$, for a fixed test scheme $T$ the composition

$$h_\varphi(T): X(T) \rightarrow Y(T);\qquad \psi\mapsto \varphi\circ \psi$$

is well-defined, and moreover $h_\varphi(T')\circ h_X(\tau)=h_Y(\tau)\circ h_\varphi(T)$ holds for any $\tau: T' \rightarrow T$. That is, $\varphi$ induces a natural transformation $h_\varphi: h_X \rightarrow h_Y$, and it follows that $X\mapsto h_X$ defines a functor

$$h_{(-)}:\Sch \rightarrow \Fun(\Sch^\op, \Set)$$

This viewpoint remains valid verbatim if we replace our category of interest by $\Sch_{/S}$, but in this post we carry out everything in $\Sch$ for convenience.

## The Yoneda Lemma and Representability

We now show that the functor of points $h_X$ defined by $X$ actually carries enough scheme-theoretic information about $X$. This is essentially category theory we have already covered, so here we only give a brief review.

The categorical foundation of the functor of points viewpoint is, of course, the Yoneda lemma and representability. Applying [\[Category Theory\] §Representable Functors, ⁋Theorem 4](/en/math/category_theory/representable_functors#thm4) with $\mathcal{A}=\Sch$, we know that the functor $h_{(-)}:\Sch \rightarrow \Fun(\Sch^\op, \Set)$ is fully faithful. This shows that a scheme $X$ is uniquely determined up to isomorphism by $h_X$, and that a scheme morphism is exactly the same data as a natural transformation between functors of points.

As we saw above, given a scheme morphism $\varphi:X\rightarrow Y$, we can send a $T$-point $\psi:T\rightarrow X$ to the composition $\varphi\circ\psi:T\rightarrow Y$. In this way, $\varphi$ gives maps $X(T)\rightarrow Y(T)$ that are compatible across all test schemes. The key observation is that this also works in reverse. Suppose we are given such a compatible collection of maps $\alpha_T:X(T)\rightarrow Y(T)$. The image $\alpha_X(\id_X)$ of the identity morphism $\id_X:X\rightarrow X$ under $\alpha_X$ is an $X$-point of $Y$, that is, a scheme morphism $f:X\rightarrow Y$. By naturality, $\alpha_T(\psi)=f\circ\psi$ holds for any $\psi:T\rightarrow X$, so the maps at all other $T$-points are forced to be composition with $f$. In other words, a natural transformation between functors of points is exactly the same data as a single scheme morphism.

Thus a scheme is essentially a functor $F:\Sch\rightarrow \Fun(\Sch^\op, \Set)$, and for it to actually arise from a scheme, this functor must be representable. ([\[Category Theory\] §Representable Functors, ⁋Definition 1](/en/math/category_theory/representable_functors#def1)) On the scheme $X$ obtained in this way there is a universal element corresponding to $\id_X$ in $h_X(X)$, and any scheme morphism $f:T\rightarrow X$ yields an element of $F(T)$ by pulling this back to $T$. This is the same mechanism by which, in [\[Algebraic Topology\] §Classifying Spaces, ⁋Theorem 8](/en/math/algebraic_topology/classifying_spaces#thm8), a classifying map $f:B\rightarrow \B G$ pulls back the universal bundle to give a principal $G$-bundle over $B$; the difference is that here it is the actual scheme morphism $f:T\rightarrow X$ itself, rather than a homotopy class, that appears.

## Affine Space and Projective Space as Functors

We now examine geometric objects we already know from this viewpoint. The starting point is, of course, affine space and projective space.

::: Proposition 1
For the affine line $\mathbb{A}^1=\Spec \mathbb{Z}[\x]$ over $\mathbb{Z}$ and any scheme $T$, the set of $T$-points of $\mathbb{A}^1$ is given by

$$\mathbb{A}^1(T)\cong \Gamma(T, \mathcal{O}_T)=\mathcal{O}_T(T)$$

and this correspondence is natural in $T$.
:::
::: Proof
In the adjunction

$$\Hom_\Sch(T, \Spec A)\cong \Hom_\cRing(A, \Gamma(T, \mathcal{O}_T))$$

that we saw in [§Affine Scheme, ⁋Theorem 13](/en/math/scheme_theory/affine_schemes#thm13), set $A=\mathbb{Z}[\x]$. Since the ring $\mathbb{Z}[\x]$ is a free object in $\cRing$, a ring homomorphism $\mathbb{Z}[\x] \rightarrow \Gamma(T, \mathcal{O}_T)$ amounts to freely choosing the image $\x\mapsto a$ of the generator $\x$, which is exactly the choice of an element $a\in \Gamma(T, \mathcal{O}_T)$. Hence

$$\mathbb{A}^1(T)=\Hom_\Sch(T, \Spec \mathbb{Z}[\x])\cong \Hom_\cRing(\mathbb{Z}[\x], \Gamma(T, \mathcal{O}_T))\cong \Gamma(T, \mathcal{O}_T)$$

The naturality of this correspondence means that for any $\tau: T' \rightarrow T$, the restriction map $\Gamma(T, \mathcal{O}_T) \rightarrow \Gamma(T', \mathcal{O}_{T'})$ is compatible with the above bijection, which follows from the naturality of the adjunction.
:::

In the language introduced in the previous section, $\mathbb{A}^1$ represents the global section functor $T\mapsto\Gamma(T,\mathcal{O}_T)$. Here the universal element is the one corresponding to the identity morphism $\id_{\mathbb{A}^1}$ in $h_{\mathbb{A}^1}(\mathbb{A}^1)=\Hom_\Sch(\mathbb{A}^1,\mathbb{A}^1)$, and chasing through the correspondence of [Proposition 1](#prop1), we see that it corresponds to $\x$ in $\Gamma(\mathbb{A}^1,\mathcal{O}_{\mathbb{A}^1})=\mathbb{Z}[\x]$.

Now any scheme morphism $f:T\rightarrow\mathbb{A}^1$ defines a (global) regular function $f^\ast \x$ on $T$ via the pullback map $f^\ast:\Gamma(\mathbb{A}^1,\mathcal{O}_{\mathbb{A}^1})\rightarrow\Gamma(T,\mathcal{O}_T)$. Conversely, given any global regular function $a\in\Gamma(T,\mathcal{O}_T)$, there is a ring homomorphism $\mathbb{Z}[\x]\rightarrow\Gamma(T,\mathcal{O}_T)$ determined by $\x\mapsto a$, and this choice determines a unique scheme morphism $f:T\rightarrow\mathbb{A}^1$, which satisfies $f^\ast\x=a$. Generalizing this to $n$ generators, we obtain the following.

::: Proposition 2
For the affine $n$-space $\mathbb{A}^n=\Spec \mathbb{Z}[\x_1,\ldots, \x_n]$ over $\mathbb{Z}$, there exists a natural bijection

$$\mathbb{A}^n(T)\cong \Gamma(T, \mathcal{O}_T)^n$$

That is, a $T$-point of $\mathbb{A}^n$ is an ordered $n$-tuple of regular functions on $T$.
:::
::: Proof
As in the proof of [Proposition 1](#prop1), a ring homomorphism out of the free ring $\mathbb{Z}[\x_1,\ldots, \x_n]$ amounts to freely choosing the images $a_i\in \Gamma(T, \mathcal{O}_T)$ of the generators $\x_i$, so we obtain

$$\mathbb{A}^n(T)\cong \Hom_\cRing(\mathbb{Z}[\x_1,\ldots, \x_n], \Gamma(T, \mathcal{O}_T))\cong \Gamma(T, \mathcal{O}_T)^n$$

:::

In particular, when $T=\Spec A$ we have $\mathbb{A}^n(A)\cong A^n$, which agrees exactly with the classical intuition: an $A$-point of affine $n$-space is a coordinate made of $n$ elements of $A$. More generally, if $T$ is not affine, then $\Gamma(T,\mathcal{O}_T)$ can be richer, so $\mathbb{A}^n(T)$ also carries more information than classical coordinates. On the other hand, extracting only the multiplicatively invertible elements from the global section functor yields the following functor.

::: Proposition 3
For $\mathbb{G}_m=\Spec \mathbb{Z}[\t, \t^{-1}]$, there exists a natural bijection

$$\mathbb{G}_m(T)\cong \Gamma(T, \mathcal{O}_T)^\times$$

Here $\Gamma(T, \mathcal{O}_T)^\times$ is the group of invertible elements of the ring $\Gamma(T, \mathcal{O}_T)$.
:::
::: Proof
Since $\mathbb{Z}[\t, \t^{-1}]=\mathbb{Z}[\t]_\t$, ring homomorphisms $\mathbb{Z}[\t, \t^{-1}] \rightarrow \Gamma(T, \mathcal{O}_T)$ are in bijection with those for which the image $a$ of $\t$ is invertible. Indeed, by the universal property of localization, ring homomorphisms out of $\mathbb{Z}[\t]_\t$ correspond exactly to ring homomorphisms $\mathbb{Z}[\t] \rightarrow \Gamma(T, \mathcal{O}_T)$ sending the image of $\t$ to an invertible element, and as we saw in [Proposition 1](#prop1), this amounts to choosing an invertible element $a\in \Gamma(T, \mathcal{O}_T)^\times$.
:::

Using this, we can obtain projective space from affine space. To this end, consider the open subscheme $U$ obtained by removing the origin from $\mathbb{A}^{n+1}$. First, define the scheme morphism

$$\mu:\mathbb{G}_m\times\mathbb{A}^{n+1}\rightarrow\mathbb{A}^{n+1}$$

by the expression

$$\mathbb{Z}[\x_0,\ldots,\x_n]\rightarrow\mathbb{Z}[\t,\t^{-1},\x_0,\ldots,\x_n];\qquad \x_i\mapsto\t\x_i$$

This is the scalar multiplication action of $\mathbb{G}_m$, and it restricts to $U$ as well. Classically, projective space is thought of as the quotient $U/\mathbb{G}_m$ by this action.

Examining this at the level of $T$-points, by [Proposition 3](#prop3) we have $\mathbb{G}_m(T)=\Gamma(T,\mathcal{O}_T)^\times$, so the above action can be thought of as an invertible function $u$ acting on a tuple $(a_0,\ldots,a_n)\in U(T)$ by

$$u\cdot(a_0,\ldots,a_n)=(ua_0,\ldots,ua_n)$$

Here each $a_i$ is a function defined on $T$, and the tuple $(a_0(t),\ldots, a_n(t))$ at any point $t$ of $T$ must not be the zero vector.

A natural expectation would be that $\mathbb{P}^n(T)=U(T)/\mathbb{G}_m(T)$, but this does not hold. Indeed, for such a tuple $(a_0,\ldots, a_n)\in U(T)$, the loci

$$T_i=\{t\in T\mid \text{$a_i(t)$ invertible}\}$$

are open subschemes of $T$, and since the ratios $a_j/a_i$ are always defined on $T_i$, the expressions

$$\mathbb{Z}[\x_0/\x_i,\ldots, \x_n/\x_i]\rightarrow \Gamma(T_i, \mathcal{O}_T);\qquad \x_j/\x_i\mapsto a_j/a_i$$

define morphisms $T_i\rightarrow D_+(\x_i)$, which agree on the overlaps and glue into a single morphism $T\rightarrow\mathbb{P}^n$. Moreover, since the $\mathbb{G}_m(T)$-action does not change the ratios $a_j/a_i$, it is perfectly natural that we obtain a map $U(T)/\mathbb{G}_m(T)\rightarrow\mathbb{P}^n(T)$.

The problem is that this correspondence is not surjective in general, because when the image of $\psi: T \rightarrow \mathbb{P}^n$ spans several charts of $\mathbb{P}^n$, the way homogeneous coordinates are chosen may differ from chart to chart. Concretely, given a morphism $\psi:T\rightarrow\mathbb{P}^n$, the loci $V_i=\psi^{-1}(D_+(\x_i))$ form an open cover of $T$, and on each $V_i$ the tuple normalized so that the $i$-th coordinate is $1$,

$$a^{(i)}=(\psi^\ast(\x_0/\x_i),\ldots, \psi^\ast(\x_n/\x_i))\in U(V_i)$$

is defined, and the transition relation connecting two different charts is given by

$$a^{(i)}=\psi^\ast(\x_j/\x_i)\cdot a^{(j)}$$

The problem is that the factor $\psi^\ast(\x_j/\x_i)$ here is an invertible function defined only on $V_i\cap V_j$, whereas the factor considered when gluing the $T_i$ above came from $\mathbb{G}_m(T)$, that is, from global scaling factors. Thus, if we simply thought of $\mathbb{P}^n(T)$ as $U(T)/\mathbb{G}_m(T)$, we would miss these $T$-points.

On the other hand, we already know a good way to record a scaling factor locally in each such situation: consider a line bundle on $T$. On the resulting line bundle $\mathcal{L}$, the coordinates of the local tuples combine into $n+1$ global sections $s_0,\ldots, s_n\in \Gamma(T, \mathcal{L})$, and the fact that the $i$-th coordinate of $a^{(i)}$ was $1$ means that $s_i$ generates $\mathcal{L}$ on $V_i$. To make these ratios well-defined, we must require the following condition.

::: Definition 4
By *globally generating sections* $s_0,\ldots, s_n\in \Gamma(T, \mathcal{L})$ of a line bundle $\mathcal{L}$ on a scheme $T$, we mean that at each point $t\in T$, the stalk $\mathcal{L}_t$ is generated as an $\mathcal{O}_{T,t}$-module by the germs $(s_0)_t,\ldots, (s_n)_t$. Two data $(\mathcal{L}, s_0,\ldots, s_n)$ and $(\mathcal{L}', s_0',\ldots, s_n')$ are *isomorphic* if there exists an $\mathcal{O}_T$-module isomorphism $\theta:\mathcal{L} \rightarrow \mathcal{L}'$ such that $\theta(s_i)=s_i'$ for each $i$.
:::

This isomorphism condition records the scaling of homogeneous coordinates. In particular, when $\mathcal{L}=\mathcal{O}_T$, the automorphisms of $\mathcal{O}_T$ are only multiplication by an invertible function $u\in\Gamma(T,\mathcal{O}_T)^\times$. Thus $(\mathcal{O}_T,s_0,\ldots,s_n)$ and $(\mathcal{O}_T,us_0,\ldots,us_n)$ are isomorphic data.

Under this definition, the functor of points of $\mathbb{P}^n$ admits the following clean description.

::: Theorem 5
For the projective space $\mathbb{P}^n=\Proj \mathbb{Z}[\x_0,\ldots, \x_n]$ over $\mathbb{Z}$, $\mathbb{P}^n(T)$ is naturally in bijection with the isomorphism classes of data $(\mathcal{L}, s_0,\ldots, s_n)$ consisting of a line bundle $\mathcal{L}$ on $T$ and globally generating sections $s_0,\ldots, s_n\in \Gamma(T, \mathcal{L})$.
:::
::: Proof
Suppose a morphism $\psi: T \rightarrow \mathbb{P}^n$ is given. The twisting sheaf $\mathcal{O}_{\mathbb{P}^n}(1)$ on $\mathbb{P}^n$ is a line bundle whose global sections $\x_0,\ldots, \x_n$ are globally generating, so pulling back, we obtain a line bundle $\mathcal{L}=\psi^\ast \mathcal{O}_{\mathbb{P}^n}(1)$ on $T$ and sections $s_i=\psi^\ast \x_i$. Since pullback preserves the property of being globally generating, $(\mathcal{L}, s_0,\ldots, s_n)$ forms the data above.

Conversely, suppose a line bundle $\mathcal{L}$ on $T$ and globally generating sections $s_0,\ldots, s_n$ of it are given. For each $i$, the locus $T_{s_i}=\{t\in T\mid (s_i)_t \text{ generates } \mathcal{L}_t\}$ where the section $s_i$ generates is open, and since the sections globally generate $\mathcal{L}$, the family $\{T_{s_i}\}_{i=0}^n$ forms an open cover of $T$. On $T_{s_i}$, the section $s_i$ gives a trivialization of $\mathcal{L}\vert_{T_{s_i}}$, so $s_j/s_i\in \Gamma(T_{s_i}, \mathcal{O}_T)$ is well-defined for each $j$. With this, in the same manner as [§Morphisms of Schemes, ⁋Example 5](/en/math/scheme_theory/morphism_of_schemes#ex5), we define $T_{s_i} \rightarrow D_+(\x_i)$ and check the gluing condition on the overlaps to obtain a morphism $\psi: T \rightarrow \mathbb{P}^n$.

That these two constructions are inverse to each other, and that isomorphic data give the same morphism, follows from the fact that transporting the whole datum $(\mathcal{L}, s_0,\ldots, s_n)$ along an $\mathcal{O}_T$-module isomorphism does not change the ratios $s_j/s_i$, and hence yields the same gluing data. Naturality means that for $\tau: T' \rightarrow T$, pulling back the above data agrees with composing the morphism.
:::

Concretely, let us revisit, in this language, the $\mathbb{K}[\epsilon]/(\epsilon^2)$-points of $\mathbb{P}^n_\mathbb{K}$ that we examined in [§From Varieties to Schemes, ⁋Example 5](/en/math/scheme_theory/from_varieties_to_schemes#ex5). Since this is a one-point space, the only line bundle on it is the trivial line bundle, and once we fix a trivialization we have $\Gamma(T,\mathcal{L})\cong\Gamma(T,\mathcal{O}_T)=A$, so choosing a section of a line bundle on it amounts to choosing an element of $A$. Meanwhile, since the stalk at the unique point of $\Spec A$ is $A$ itself, the condition that these sections are globally generating amounts to the condition that some $a_i$ is invertible, which is exactly the condition $(a_0,\ldots, a_n)\in U(A)$.

Now, to see how [Theorem 5](#thm5) works, let us look at the isomorphism classes: since the automorphisms of $\mathcal{O}_T$ are now only multiplication by elements of $A^\times$, two tuples give the same $A$-point if and only if they are $A^\times$-multiples of each other. Therefore

$$\mathbb{P}^n(A)=U(A)/A^\times$$

where $U(A)$ consists of the $(n+1)$-tuples $(a_0, \ldots, a_n)$ with coordinates in $A$ having at least one invertible coordinate, and $A^\times$ acts by multiplying every component by an element of $A^\times$.

Now let $V=\mathbb{K}^{n+1}$, and write an element of $U(A)$ in the form $a=b+\epsilon c$. Then we can consider the correspondence

$$\widetilde{\rho}: U(A)\rightarrow \mathbb{P}^n(\mathbb{K});\qquad b+\epsilon c\mapsto [b]$$

Intuitively, this is the function that forgets the tangent vector direction and remembers only the base point. Expanding the $A^\times$-action on $U(A)$ as above,

$$u(b+\epsilon c)=\lambda b+\epsilon(\lambda c+\mu b)$$

so this $\widetilde{\rho}$ descends to a map $\rho: \mathbb{P}^n(A)\rightarrow \mathbb{P}^n(\mathbb{K})$.

The $\rho$ thus obtained is in fact the map functorially induced from the ring homomorphism

$$q:A\rightarrow\mathbb{K};\qquad \epsilon\mapsto0$$

That is, if we let $\iota:\Spec\mathbb{K}\rightarrow\Spec A$ be the morphism corresponding to this ring homomorphism, then $\rho$ sends an $A$-point $\psi:\Spec A\rightarrow\mathbb{P}^n$ to the composition $\psi\circ\iota$, and one can check that this agrees exactly with the $\rho$ defined above.

Therefore $\rho^{-1}(\ell)$ is the set of $A$-points that restrict to $\ell$ along $\Spec\mathbb{K}\rightarrow\Spec A$. Let us compute this directly. First, choose a class $[b+\epsilon c]\in\rho^{-1}(\ell)$; then $\ell=\mathbb{K}b\subseteq V$, and from this $A$-point we can define a $\mathbb{K}$-linear map

$$\phi:\ell\rightarrow V/\ell,\qquad \phi(b)=c+\ell$$

This does not depend on the choice of representative. Indeed, using the earlier computation, for $\lambda b+\epsilon(\lambda c+\mu b)$ belonging to the same class as $b+\epsilon c$, the image of $\lambda b$ under $\phi$ is

$$(\lambda c+\mu b)+\ell=\lambda(c+\ell)$$

Conversely, suppose a one-dimensional subspace $\ell\subseteq V$ and a linear map $\phi:\ell\rightarrow V/\ell$ are given. Choose a nonzero $b\in\ell$ and a lift $c\in V$ of $\phi(b)$; then we obtain $b+\epsilon c\in U(A)$. This is, first of all, independent of the choice of lift: if we choose another lift $c'=c+\mu b$, then

$$b+\epsilon c'=(1+\epsilon\mu)(b+\epsilon c)$$

which belongs to the same $A^\times$-class. Similarly, choosing a basis $b'=\lambda b$ and its lift $c'=\lambda c+\mu b$ gives

$$b'+\epsilon c'=(\lambda+\epsilon\mu)(b+\epsilon c)$$

so we obtain an $A^\times$-class independent of all choices. One can check that this is the inverse of the above construction, and therefore we obtain the isomorphism

$$\mathbb{P}^n(A)\cong\{(\ell,\phi)\mid \ell\in \mathbb{P}^n(\mathbb{K}),\ \phi\in \Hom_\mathbb{K}(\ell, V/\ell)\}$$

That is, $\mathbb{P}^n(A)$ is the collection of tangent vectors at all points of $\mathbb{P}^n$, and since $\rho$ retains only the base point, $\rho^{-1}(\ell)$ gives the tangent space $T_\ell\mathbb{P}^n$ of $\mathbb{P}^n$ at $\ell$. More generally, for any $\mathbb{K}$-scheme $X$, the set $X(A)$ collects the tangent spaces at all $\mathbb{K}$-points.

::: Example 6
We now concretely examine the functor defined by the projective space considered above. First, the datum of $\mathcal{L}$ and globally generating sections $s_0,\ldots, s_n$ representing $\mathbb{P}^n(T)$ can be rewritten as the surjection

$$\mathcal{O}_T^{\oplus n+1}\twoheadrightarrow \mathcal{L};\qquad e_i\mapsto s_i$$

We define an isomorphism between such surjections by the diagram

{% diagram Math/Scheme_Theory/Functor_of_Points-1.svg width="11.42em" alt="isomorphic_surjections" %}

and consider the functor $F_{n+1}$ that assigns to $T\in\Sch$ the set of these isomorphism classes. Here functoriality at the level of morphisms is given by pulling back the surjection via $\tau:T'\rightarrow T$ to define

$$\mathcal{O}_{T'}^{\oplus n+1}\twoheadrightarrow\tau^\ast\mathcal{L}$$

That is, this correspondence defines a contravariant functor

$$F_{n+1}:\Sch^\op\rightarrow\Set$$

From this viewpoint, [Theorem 5](#thm5) says that there exists a bijection

$$\mathbb{P}^n(T)\cong F_{n+1}(T)$$

natural in every scheme $T$, and that the projective space $\mathbb{P}^n$ represents this functor. By [\[Category Theory\] §Representable Functors, ⁋Theorem 4](/en/math/category_theory/representable_functors#thm4), the universal element corresponding to $\id_{\mathbb{P}^n}$ is the quotient bundle

$$\mathcal{O}_{\mathbb{P}^n}^{\oplus n+1}\twoheadrightarrow\mathcal{O}_{\mathbb{P}^n}(1)$$

on $\mathbb{P}^n$, and any $T$-point is obtained by pulling this universal quotient back to $T$ to get a rank $1$ quotient.

The Grassmannian is obtained from the above functor by replacing the rank $1$ target with a rank $k$ target. That is, for integers $0<k<n$, we assign to a scheme $T$ the set

$$F_{k,n}(T)=\left\{\mathcal{O}_T^n\twoheadrightarrow\mathcal{Q}\mid \mathcal{Q}\text{ is locally free of rank }k\right\}\big/\cong$$

and to a morphism $\tau:T'\rightarrow T$ we assign pullback. We denote by $\Gr(k,n)$ the scheme representing this contravariant functor, so there exists a bijection

$$\Gr(k,n)(T)\cong F_{k,n}(T)$$

natural in every scheme $T$.

When $T=\Spec\mathbb{K}$, an element of $F_{k,n}(T)$ is a rank $k$ quotient space $\mathbb{K}^n\twoheadrightarrow Q$. Since this is uniquely determined by its kernel, an $(n-k)$-dimensional subspace $\bar S\subseteq\mathbb{K}^n$, the set $\Gr(k,n)(\mathbb{K})$ agrees with the set of such subspaces. In the convention of [\[Algebraic Varieties\] §Grassmann Varieties, ⁋Definition 1](/en/math/algebraic_varieties/grassmannians#def1), which classifies subspaces directly, this set is denoted $\Gr(n-k,n)$. In particular, when $k=1$ we classify rank $1$ quotients, recovering $\mathbb{P}^{n-1}$ of [Theorem 5](#thm5).

:::

Showing that such a functorial definition is representable is the starting point of moduli theory; in the case of the Grassmannian, one can construct the representing scheme and the universal quotient using the fact that the quotient bundle is expressed as matrix data over the standard affine charts.

## Fiber Products as Functors

The functor of points viewpoint fits perfectly with the fiber product defined in [§Fiber Products, ⁋Definition 1](/en/math/scheme_theory/fiber_products#def1). The universal property of the fiber product $X\times_S Y$ tells us directly, at the level of functors, how its $T$-points are determined for any test scheme $T$.

::: Proposition 7
Suppose scheme morphisms $X \rightarrow S$ and $Y \rightarrow S$ are given. Then for any scheme $T$, there exists a natural bijection

$$(X\times_S Y)(T)\cong X(T)\times_{S(T)} Y(T)$$

Here the right-hand side is the fiber product in $\Set$, that is, the set of ordered pairs in $X(T)\times Y(T)$ on which $X(T) \rightarrow S(T)$ and $Y(T) \rightarrow S(T)$ take the same value.
:::
::: Proof
The universal property of [§Fiber Products, ⁋Definition 1](/en/math/scheme_theory/fiber_products#def1) means that a morphism from $T$ to $X\times_S Y$ corresponds uniquely to a pair $\psi_X: T \rightarrow X$ and $\psi_Y: T \rightarrow Y$ whose compositions to $S$ agree, that is, a pair such that $\psi_X$ and $\psi_Y$ map to the same $S$-point under $X(T) \rightarrow S(T)$ and $Y(T) \rightarrow S(T)$. Written in the language of sets, this is

$$(X\times_S Y)(T)\cong \{(\psi_X, \psi_Y)\in X(T)\times Y(T)\mid \psi_X, \psi_Y \text{ map to the same element of } S(T)\}=X(T)\times_{S(T)} Y(T)$$

Naturality means that for $\tau: T' \rightarrow T$, the pullbacks on both sides agree, which follows from the naturality of the universal property.
:::

[Proposition 7](#prop7) lets us interpret the fiber product as the operation of taking fiber products *pointwise* at the level of functors. From this viewpoint, the existence proof of [§Fiber Products, ⁋Theorem 8](/en/math/scheme_theory/fiber_products#thm8) is reinterpreted as the task of showing that the functor $T\mapsto X(T)\times_{S(T)} Y(T)$, which is trivially defined pointwise, is representable. In particular, for the product $X\times Y=X\times_{\Spec \mathbb{Z}} Y$, we simply have $(X\times Y)(T)\cong X(T)\times Y(T)$.

---

**References**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundations of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).  

---
