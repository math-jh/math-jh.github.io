---
title: "Functor of Points"
description: "This post develops the viewpoint of regarding a scheme as its functor of points, using the language of the Yoneda lemma and representable functors. It then examines key examples, including affine space, projective space, Grassmannians, and fiber products."
excerpt: "Functor of points, Yoneda embedding, representability, fiber products"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/functor_of_points
sidebar: 
    nav: "scheme_theory-en"

date: 2026-08-23
weight: 22
translated_at: 2026-09-01T23:46:54+00:00
translation_source: kimi-cli
---
We now begin preparations to extend the language of schemes further. For this we need the functor of points perspective that we saw in [§Morphisms of Schemes, ⁋Definition 6](/en/math/scheme_theory/morphism_of_schemes#def6). This was already defined in [§Morphisms of Schemes, ⁋Definition 9](/en/math/scheme_theory/morphism_of_schemes#def9): to study a scheme $X$, one looks at the collection of $T$-points of $X$ for every possible test scheme $T$. In other words, one considers the functor

$$h_X=\Hom_\Sch(-,X): \Sch^\op \rightarrow \Set$$

Our first goal is to confirm, via the Yoneda lemma, that this functor determines $X$ completely up to isomorphism, and to see how this functorial perspective provides a natural language for dealing with affine space, projective space, Grassmannians, fiber products, and the like.

Before starting the discussion in earnest, let us fix notation. For each scheme $T$, we write $X(T)$ for $h_X(T)=\Hom_\Sch(T,X)$, and for a scheme morphism $\tau: T' \rightarrow T$, we denote by $h_X(\tau): X(T) \rightarrow X(T')$ the composition $h_X(\tau)(\psi)=\psi\circ \tau$. In particular, when $T=\Spec A$ we simply write $X(A)$ for $X(\Spec A)$, and as defined above we also call an element of the set $X(T)$ a *$T$-valued point*. Under this name, $X(\tau)$ amounts to pulling a $T$-point of $X$ back to a $T'$-point along $\tau$.

Meanwhile, functoriality also exists in the direction of $X$. Given a scheme morphism $\varphi: X\rightarrow Y$, for a fixed test scheme $T$ the composition

$$h_\varphi(T): X(T) \rightarrow Y(T);\qquad \psi\mapsto \varphi\circ \psi$$

is well-defined, and moreover for any $\tau: T' \rightarrow T$ we have $h_\varphi(T')\circ h_X(\tau)=h_Y(\tau)\circ h_\varphi(T)$. That is, $\varphi$ induces a natural transformation $h_\varphi: h_X \rightarrow h_Y$, and from this we know that $X\mapsto h_X$ defines a functor

$$h_{(-)}:\Sch \rightarrow \Fun(\Sch^\op, \Set)$$

This perspective remains valid if we change our object of interest to $\Sch_{/S}$, but in this post, for convenience, we will carry out everything in $\Sch$.

## The Yoneda Lemma and Representability

We now show that the functor of points $h_X$ defined by $X$ actually carries sufficient scheme-theoretic information about $X$. This is essentially something already covered in category theory, so here we will proceed with only a brief review.

The categorical foundation of the functor of points perspective is, of course, the Yoneda lemma and representability. Applying [\[Category Theory\] §Representable Functors, ⁋Theorem 4](/en/math/category_theory/representable_functors#thm4) with $\mathcal{A}=\Sch$, we know that the functor $h_{(-)}:\Sch \rightarrow \Fun(\Sch^\op, \Set)$ is fully faithful. This shows that a scheme $X$ is uniquely determined by $h_X$ up to isomorphism, and that a scheme morphism is exactly the same data as a natural transformation between functors of points.

As we saw above, given a scheme morphism $\varphi:X\rightarrow Y$, one can send a $T$-point $\psi:T\rightarrow X$ to the composition $\varphi\circ\psi:T\rightarrow Y$. In this way, $\varphi$ gives maps $X(T)\rightarrow Y(T)$ that are compatible across all test schemes. The key observation is that this works in reverse as well. Suppose we are given a collection of such compatible maps $\alpha_T:X(T)\rightarrow Y(T)$. The element $\alpha_X(\id_X)$ to which $\alpha_X$ sends the identity morphism $\id_X:X\rightarrow X$ is an $X$-point of $Y$, that is, a scheme morphism $f:X\rightarrow Y$. By naturality, for any $\psi:T\rightarrow X$ we have $\alpha_T(\psi)=f\circ\psi$, so the maps at all other $T$-points are forced to be composition with $f$. In other words, a natural transformation between functors of points is exactly the same data as a single scheme morphism.

Thus, the condition for a presheaf $F:\Sch^\op\rightarrow\Set$ to actually arise as the functor of points of some scheme is that $F$ be a representable functor. ([\[Category Theory\] §Representable Functors, ⁋Definition 1](/en/math/category_theory/representable_functors#def1)) Given an isomorphism $F\cong h_X$, there is a universal element over $X$ corresponding to $\id_X$ in $h_X(X)$, and any scheme morphism $f:T\rightarrow X$ pulls this back to $T$ to give an element of $F(T)$. This is the same way that, in [\[Algebraic Topology\] §Classifying Spaces, ⁋Theorem 8](/en/math/algebraic_topology/classifying_spaces#thm8), a classifying map $f:B\rightarrow \B G$ pulls back the universal bundle to give a principal $G$-bundle over $B$; the difference is that here, instead of a homotopy class, the actual scheme morphism $f:T\rightarrow X$ itself appears.

## Affine Space and Projective Space as Functors

We now examine, from this perspective, geometric objects we already know. The starting point is, of course, affine space and projective space.

::: Proposition 1
For the affine line $\mathbb{A}^1=\Spec \mathbb{Z}[\x]$ over $\mathbb{Z}$ and an arbitrary scheme $T$, the set of $T$-points of $\mathbb{A}^1$ is given by

$$\mathbb{A}^1(T)\cong \Gamma(T, \mathcal{O}_T)=\mathcal{O}_T(T)$$

and this correspondence is natural in $T$.
:::
::: Proof
In the adjunction

$$\Hom_\Sch(T, \Spec A)\cong \Hom_\cRing(A, \Gamma(T, \mathcal{O}_T))$$

which we saw in [§Affine Scheme, ⁋Theorem 13](/en/math/scheme_theory/affine_schemes#thm13), set $A=\mathbb{Z}[\x]$. Since the ring $\mathbb{Z}[\x]$ is a free object in $\cRing$, giving a ring homomorphism $\mathbb{Z}[\x] \rightarrow \Gamma(T, \mathcal{O}_T)$ amounts to freely choosing the image $\x\mapsto a$ of the generator $\x$, which is exactly choosing one element $a\in \Gamma(T, \mathcal{O}_T)$. Therefore

$$\mathbb{A}^1(T)=\Hom_\Sch(T, \Spec \mathbb{Z}[\x])\cong \Hom_\cRing(\mathbb{Z}[\x], \Gamma(T, \mathcal{O}_T))\cong \Gamma(T, \mathcal{O}_T)$$

The naturality of this correspondence (for any $\tau: T' \rightarrow T$, the restriction map $\Gamma(T, \mathcal{O}_T) \rightarrow \Gamma(T', \mathcal{O}_{T'})$ commutes with the correspondence above) follows from the naturality of the adjunction.
:::

In the language introduced in the previous section, $\mathbb{A}^1$ represents the global section functor $T\mapsto\Gamma(T,\mathcal{O}_T)$. The universal element is then the one corresponding to the identity morphism $\id_{\mathbb{A}^1}$ inside $h_{\mathbb{A}^1}(\mathbb{A}^1)=\Hom_\Sch(\mathbb{A}^1,\mathbb{A}^1)$, and chasing through the correspondence of [Proposition 1](#prop1) above, we see that it corresponds to $\x$ inside $\Gamma(\mathbb{A}^1,\mathcal{O}_{\mathbb{A}^1})=\mathbb{Z}[\x]$.

Now any scheme morphism $f:T\rightarrow\mathbb{A}^1$ defines, via the pullback map $f^\ast:\Gamma(\mathbb{A}^1,\mathcal{O}_{\mathbb{A}^1})\rightarrow\Gamma(T,\mathcal{O}_T)$, a (global) regular function $f^\ast \x$ defined on $T$. Conversely, given any global regular function $a\in\Gamma(T,\mathcal{O}_T)$, there is a ring homomorphism $\mathbb{Z}[\x]\rightarrow\Gamma(T,\mathcal{O}_T)$ determined by $\x\mapsto a$, and this very choice gives a unique scheme morphism $f:T\rightarrow\mathbb{A}^1$, which satisfies $f^\ast\x=a$. Generalizing this to $n$ generators, we obtain the following.

::: Proposition 2
For the affine $n$-space $\mathbb{A}^n=\Spec \mathbb{Z}[\x_1,\ldots, \x_n]$ over $\mathbb{Z}$, there exists a natural bijection

$$\mathbb{A}^n(T)\cong \Gamma(T, \mathcal{O}_T)^n$$

That is, a $T$-point of $\mathbb{A}^n$ is an $n$-tuple of regular functions on $T$.
:::
::: Proof
Exactly as in the proof of [Proposition 1](#prop1), a ring homomorphism out of the free ring $\mathbb{Z}[\x_1,\ldots, \x_n]$ freely chooses the images $a_i\in \Gamma(T, \mathcal{O}_T)$ of the generators $\x_i$, so we obtain

$$\mathbb{A}^n(T)\cong \Hom_\cRing(\mathbb{Z}[\x_1,\ldots, \x_n], \Gamma(T, \mathcal{O}_T))\cong \Gamma(T, \mathcal{O}_T)^n$$

:::

In particular, when $T=\Spec A$ we have $\mathbb{A}^n(A)\cong A^n$, which agrees exactly with the classical intuition. That is, an $A$-point of affine $n$-space is a coordinate made up of $n$ elements of $A$. More generally, if $T$ is not affine, then $\Gamma(T,\mathcal{O}_T)$ can be richer, so $\mathbb{A}^n(T)$ also carries more information than classical coordinates. Meanwhile, extracting only the units with respect to multiplication from the global section functor yields the following functor.

::: Proposition 3
For $\mathbb{G}_m=\Spec \mathbb{Z}[\t, \t^{-1}]$, there exists a natural bijection

$$\mathbb{G}_m(T)\cong \Gamma(T, \mathcal{O}_T)^\times$$

Here $\Gamma(T, \mathcal{O}_T)^\times$ is the group of units of the ring $\Gamma(T, \mathcal{O}_T)$.
:::
::: Proof
Since $\mathbb{Z}[\t, \t^{-1}]=\mathbb{Z}[\t]_\t$, ring homomorphisms $\mathbb{Z}[\t, \t^{-1}] \rightarrow \Gamma(T, \mathcal{O}_T)$ are in bijection with those for which the image $a$ of $\t$ is invertible. Indeed, by the universal property of localization, ring homomorphisms out of $\mathbb{Z}[\t]_\t$ correspond exactly to those $\mathbb{Z}[\t] \rightarrow \Gamma(T, \mathcal{O}_T)$ sending $\t$ to a unit, and as we saw in [Proposition 1](#prop1), this amounts to choosing one unit $a\in \Gamma(T, \mathcal{O}_T)^\times$.
:::

Using this, one can obtain projective space from affine space. To this end, consider the open subscheme $U$ obtained by removing the origin from $\mathbb{A}^{n+1}$. First, define the scheme morphism

$$\mu:\mathbb{G}_m\times\mathbb{A}^{n+1}\rightarrow\mathbb{A}^{n+1}$$

by the expression

$$\mathbb{Z}[\x_0,\ldots,\x_n]\rightarrow\mathbb{Z}[\t,\t^{-1},\x_0,\ldots,\x_n];\qquad \x_i\mapsto\t\x_i$$

This is the scalar multiplication action of $\mathbb{G}_m$, and it also restricts to $U$. Classically, projective space was thought of as the quotient $U/\mathbb{G}_m$ by this action.

Examining this on $T$-points, since $\mathbb{G}_m(T)=\Gamma(T,\mathcal{O}_T)^\times$ by [Proposition 3](#prop3), the above action can be thought of, on $T$-points, as a unit function $u$ acting on a tuple $(a_0,\ldots,a_n)\in U(T)$ by

$$u\cdot(a_0,\ldots,a_n)=(ua_0,\ldots,ua_n)$$

Here each of the $a_i$ is a function defined on $T$, and the tuple $(a_0(t),\ldots, a_n(t))$ at any point $t$ of $T$ must not be the zero vector.

The natural expectation would be that $\mathbb{P}^n(T)=U(T)/\mathbb{G}_m(T)$, but this does not hold. Indeed, for such a tuple $(a_0,\ldots, a_n)\in U(T)$,

$$T_i=\{t\in T\mid \text{$a_i(t)$ invertible}\}$$

are open subschemes of $T$, and since the ratios $a_j/a_i$ are always defined on $T_i$, each morphism $T_i\rightarrow D_+(\x_i)$ is defined via the expression

$$\mathbb{Z}[\x_0/\x_i,\ldots, \x_n/\x_i]\rightarrow \Gamma(T_i, \mathcal{O}_T);\qquad \x_j/\x_i\mapsto a_j/a_i$$

and these agree on overlaps and glue into a single morphism $T\rightarrow\mathbb{P}^n$. Moreover, since the $\mathbb{G}_m(T)$-action does not change the ratios $a_j/a_i$, the fact itself that a correspondence $U(T)/\mathbb{G}_m(T)\rightarrow\mathbb{P}^n(T)$ is obtained is natural.

The problem is that this correspondence is not surjective in general, the reason being that when the image of $\psi: T \rightarrow \mathbb{P}^n$ spans several charts of $\mathbb{P}^n$, the way of choosing homogeneous coordinates may differ from chart to chart. Concretely, given a morphism $\psi:T\rightarrow\mathbb{P}^n$, the $V_i=\psi^{-1}(D_+(\x_i))$ form an open cover of $T$, and on each $V_i$ the tuple normalized so that the $i$-th coordinate is $1$,

$$a^{(i)}=(\psi^\ast(\x_0/\x_i),\ldots, \psi^\ast(\x_n/\x_i))\in U(V_i)$$

is defined, and the transition relation connecting two different charts is given by

$$a^{(i)}=\psi^\ast(\x_j/\x_i)\cdot a^{(j)}$$

The problem is that the factor $\psi^\ast(\x_j/\x_i)$ here is a unit function defined only on $V_i\cap V_j$, whereas the factor we considered when gluing the $T_i$ above came from $\mathbb{G}_m(T)$, that is, from a global scaling factor. Thus, simply thinking $\mathbb{P}^n(T)=U(T)/\mathbb{G}_m(T)$ misses such $T$-points.

Meanwhile, we happen to know well a way to carry a scaling factor locally in each such case: namely, consider a line bundle defined on $T$. On the resulting line bundle $\mathcal{L}$, the coordinates of the local tuples combine into $n+1$ global sections $s_0,\ldots, s_n\in \Gamma(T, \mathcal{L})$, and the fact that the $i$-th coordinate of $a^{(i)}$ was $1$ becomes the statement that $s_i$ generates $\mathcal{L}$ on $V_i$. In order for these ratios to be well-defined, we must require the following condition.

::: Definition 4
*Globally generating sections* $s_0,\ldots, s_n\in \Gamma(T, \mathcal{L})$ of a line bundle $\mathcal{L}$ on a scheme $T$ means that at each point $t\in T$, the stalk $\mathcal{L}_t$ is generated as an $\mathcal{O}_{T,t}$-module by the germs $(s_0)_t,\ldots, (s_n)_t$. Two pieces of data $(\mathcal{L}, s_0,\ldots, s_n)$ and $(\mathcal{L}', s_0',\ldots, s_n')$ are said to be *isomorphic* if there exists an $\mathcal{O}_T$-module isomorphism $\theta:\mathcal{L} \rightarrow \mathcal{L}'$ such that $\theta(s_i)=s_i'$ for each $i$.
:::

This isomorphism condition records the scaling of homogeneous coordinates. In particular, when $\mathcal{L}=\mathcal{O}_T$, the only automorphisms of $\mathcal{O}_T$ are multiplication by a unit function $u\in\Gamma(T,\mathcal{O}_T)^\times$. Hence $(\mathcal{O}_T,s_0,\ldots,s_n)$ and $(\mathcal{O}_T,us_0,\ldots,us_n)$ are isomorphic data.

Under this definition, the functor of points of $\mathbb{P}^n$ is then described cleanly as follows.

::: Theorem 5
For the projective space $\mathbb{P}^n=\Proj \mathbb{Z}[\x_0,\ldots, \x_n]$ over $\mathbb{Z}$, $\mathbb{P}^n(T)$ is naturally in bijection with the isomorphism classes of data $(\mathcal{L}, s_0,\ldots, s_n)$ consisting of a line bundle $\mathcal{L}$ on $T$ together with globally generating sections $s_0,\ldots, s_n\in \Gamma(T, \mathcal{L})$.
:::
::: Proof
Suppose a morphism $\psi: T \rightarrow \mathbb{P}^n$ is given. The twisting sheaf $\mathcal{O}_{\mathbb{P}^n}(1)$ on $\mathbb{P}^n$ is a line bundle and its global sections $\x_0,\ldots, \x_n$ are globally generating sections, so taking the pullback we obtain the line bundle $\mathcal{L}=\psi^\ast \mathcal{O}_{\mathbb{P}^n}(1)$ on $T$ and the sections $s_i=\psi^\ast \x_i$. Since pullback preserves the property of being globally generating sections, $(\mathcal{L}, s_0,\ldots, s_n)$ forms the above data.

Conversely, suppose we are given a line bundle $\mathcal{L}$ on $T$ and its globally generating sections $s_0,\ldots, s_n$. For each $i$, the locus $T_{s_i}=\{t\in T\mid (s_i)_t \text{ generates } \mathcal{L}_t\}$ where the section $s_i$ generates is an open set, and since the sections globally generate $\mathcal{L}$, the collection $\{T_{s_i}\}_{i=0}^n$ forms an open cover of $T$. On $T_{s_i}$, the section $s_i$ gives a trivialization of $\mathcal{L}\vert_{T_{s_i}}$, so for each $j$ the ratio $s_j/s_i\in \Gamma(T_{s_i}, \mathcal{O}_T)$ is well-defined. From this we define $T_{s_i} \rightarrow D_+(\x_i)$ in the same way as in [§Morphisms of Schemes, ⁋Example 5](/en/math/scheme_theory/morphism_of_schemes#ex5), and checking the gluing condition on overlaps, we obtain a morphism $\psi: T \rightarrow \mathbb{P}^n$.

The fact that these two constructions are inverse to each other and that isomorphic data give the same morphism is verified from the fact that transporting the whole $(\mathcal{L}, s_0,\ldots, s_n)$ by an $\mathcal{O}_T$-module isomorphism does not change the $s_j/s_i$, and therefore gives the same gluing data. Naturality is the statement that for $\tau: T' \rightarrow T$, pulling back the above data agrees with composing the morphism.
:::

Concretely, let us re-examine in this language the $\mathbb{K}[\epsilon]/(\epsilon^2)$-point of $\mathbb{P}^n_\mathbb{K}$ that we saw in [§From Varieties to Schemes, ⁋Example 5](/en/math/scheme_theory/from_varieties_to_schemes#ex5). Since this is a one-point space, the only line bundle over it is the trivial line bundle, so fixing one trivialization we have $\Gamma(T,\mathcal{L})\cong\Gamma(T,\mathcal{O}_T)=A$, and choosing a section of a line bundle over it amounts to choosing an element of $A$. Meanwhile, the condition that these be globally generating becomes, since the stalk at the unique point of $\Spec A$ is $A$ itself, the condition that some $a_i$ is invertible, which is exactly the condition $(a_0,\ldots, a_n)\in U(A)$.

Now, to see how [Theorem 5](#thm5) works, let us examine the isomorphism classes. Since the automorphisms of $\mathcal{O}_T$ are now just multiplication by an element of $A^\times$, two tuples giving the same $A$-point is equivalent to their being scalar multiples by $A^\times$. Therefore

$$\mathbb{P}^n(A)=U(A)/A^\times$$

where $U(A)$ consists of those $(n+1)$-tuples $(a_0, \ldots, a_n)$ with coordinates in $A$ for which at least one coordinate is invertible, and $A^\times$ is obtained by multiplying all components by an element of $A^\times$.

Now let $V=\mathbb{K}^{n+1}$, and write an element of $U(A)$ in the form $a=b+\epsilon c$. Then we can consider the correspondence

$$\widetilde{\rho}: U(A)\rightarrow \mathbb{P}^n(\mathbb{K});\qquad b+\epsilon c\mapsto [b]$$

Intuitively, this is the function that forgets the tangent vector direction and remembers only its base point. Writing an element $u=\lambda+\epsilon\mu\in A^\times$ with $\lambda\in\mathbb{K}^\times$, $\mu\in\mathbb{K}$, the $A^\times$ action on $U(A)$ is

$$u(b+\epsilon c)=\lambda b+\epsilon(\lambda c+\mu b)$$

so this $\widetilde{\rho}$ descends to $\rho: \mathbb{P}^n(A)\rightarrow \mathbb{P}^n(\mathbb{K})$.

The $\rho$ thus obtained is in fact the map induced functorially from the ring homomorphism

$$q:A\rightarrow\mathbb{K};\qquad \epsilon\mapsto0$$

That is, if we let $\iota:\Spec\mathbb{K}\rightarrow\Spec A$ be the morphism corresponding to this ring homomorphism, one can check that $\rho$ sends an $A$-point $\psi:\Spec A\rightarrow\mathbb{P}^n$ to the composition $\psi\circ\iota$, and that this agrees exactly with the $\rho$ defined above.

Hence $\rho^{-1}(\ell)$ is the set of $A$-points that become $\ell$ when restricted along $\Spec\mathbb{K}\rightarrow\Spec A$. Let us compute this directly. First, pick a class $[b+\epsilon c]\in\rho^{-1}(\ell)$; then $\ell=\mathbb{K}b\subseteq V$, and from this $A$-point we can define the $\mathbb{K}$-linear map

$$\phi:\ell\rightarrow V/\ell,\qquad \phi(b)=c+\ell$$

This does not depend on the choice of representative. Indeed, using the earlier computation, for $\lambda b+\epsilon(\lambda c+\mu b)$ belonging to the same class as $b+\epsilon c$, the value to which $\lambda b$ is sent via $\phi$ is

$$(\lambda c+\mu b)+\ell=\lambda(c+\ell)$$

Conversely, suppose a one-dimensional subspace $\ell\subseteq V$ and a linear map $\phi:\ell\rightarrow V/\ell$ are given. Choose a nonzero $b\in\ell$ and a lift $c\in V$ of $\phi(b)$; then we obtain $b+\epsilon c\in U(A)$. First of all, this does not depend on the lift of $b$: if we choose another lift $c'=c+\mu b$, then

$$b+\epsilon c'=(1+\epsilon\mu)(b+\epsilon c)$$

which belongs to the same $A^\times$-class. Similarly, if we choose a basis $b'=\lambda b$ and its lift $c'=\lambda c+\mu b$, then

$$b'+\epsilon c'=(\lambda+\epsilon\mu)(b+\epsilon c)$$

so an $A^\times$-class independent of any choice is given. One can check that this is the inverse process of the construction above, and therefore we obtain the isomorphism

$$\mathbb{P}^n(A)\cong\{(\ell,\phi)\mid \ell\in \mathbb{P}^n(\mathbb{K}),\ \phi\in \Hom_\mathbb{K}(\ell, V/\ell)\}$$

That is, $\mathbb{P}^n(A)$ is the collection of tangent vectors at all points of $\mathbb{P}^n$, and since $\rho$ keeps only the base point among them, $\rho^{-1}(\ell)$ gives the tangent space $T_\ell\mathbb{P}^n$ of $\mathbb{P}^n$ at $\ell$. More generally, for an arbitrary $\mathbb{K}$-scheme $X$, the set $X(A)$ is the collection of tangent spaces at all $\mathbb{K}$-points.

::: Example 6
We now concretely examine the functor defined by the projective space we saw above. First, the $\mathcal{L}$ and globally generating sections $s_0,\ldots, s_n$ representing $\mathbb{P}^n(T)$ can be rewritten as the surjection

$$\mathcal{O}_T^{\oplus n+1}\twoheadrightarrow \mathcal{L};\qquad e_i\mapsto s_i$$

Now define an isomorphism between such surjections by the diagram

{% diagram Math/Scheme_Theory/Functor_of_Points-1.svg width="11.42em" alt="isomorphic_surjections" %}

and consider the functor $F_{n+1}$ that takes $T\in\Sch$ to such an isomorphism class. Here, functoriality at the level of morphisms is given by pulling back the surjection along $\tau:T'\rightarrow T$ to define

$$\mathcal{O}_{T'}^{\oplus n+1}\twoheadrightarrow\tau^\ast\mathcal{L}$$

That is, this correspondence defines a contravariant functor

$$F_{n+1}:\Sch^\op\rightarrow\Set$$

From this perspective, [Theorem 5](#thm5) says that there exists a bijection

$$\mathbb{P}^n(T)\cong F_{n+1}(T)$$

natural in every scheme $T$, and that the projective space $\mathbb{P}^n$ represents this functor. By [\[Category Theory\] §Representable Functors, ⁋Theorem 4](/en/math/category_theory/representable_functors#thm4), the universal element corresponding to $\id_{\mathbb{P}^n}$ is the quotient bundle

$$\mathcal{O}_{\mathbb{P}^n}^{\oplus n+1}\twoheadrightarrow\mathcal{O}_{\mathbb{P}^n}(1)$$

on $\mathbb{P}^n$, and any $T$-point is obtained by pulling this universal quotient back to $T$ to get a rank $1$ quotient.

The Grassmannian is obtained by changing the rank $1$ target in the above functor to a rank $k$ target. That is, for integers $0<k<n$, we associate to a scheme $T$ the set

$$F_{k,n}(T)=\left\{\mathcal{O}_T^n\twoheadrightarrow\mathcal{Q}\mid \mathcal{Q}\text{ is locally free of rank }k\right\}\big/\cong$$

and to a morphism $\tau:T'\rightarrow T$ we associate the pullback. The scheme representing this contravariant functor is denoted $\Gr(k,n)$, so there exists a bijection

$$\Gr(k,n)(T)\cong F_{k,n}(T)$$

natural in every scheme $T$.

When $T=\Spec\mathbb{K}$, an element of $F_{k,n}(T)$ is a rank $k$ quotient space $\mathbb{K}^n\twoheadrightarrow Q$. Since this is uniquely determined by its kernel, an $(n-k)$-dimensional subspace $\bar S\subseteq\mathbb{K}^n$, the set $\Gr(k,n)(\mathbb{K})$ coincides with the set of such subspaces. In the convention of [\[Algebraic Varieties\] §Grassmann Varieties, ⁋Definition 1](/en/math/algebraic_varieties/grassmannians#def1), which classifies subspaces directly, this set is denoted $\Gr(n-k,n)$. In particular, when $k=1$ it classifies rank $1$ quotients, so we recover the $\mathbb{P}^{n-1}$ of [Theorem 5](#thm5).

:::

Showing that such a functorial definition is representable is the starting point of moduli theory, and in the case of the Grassmannian, one can construct the representing scheme and the universal quotient using the fact that the quotient bundle is expressed as matrix data over the standard affine charts.

## Fiber Products as Functors

The functor of points perspective fits well with the fiber product defined in [§Fiber Products, ⁋Definition 1](/en/math/scheme_theory/fiber_products#def1). The universal property of the fiber product $X\times_S Y$ tells us directly, at the functor level, how its $T$-points are determined for any test scheme $T$.

::: Proposition 7
Suppose scheme morphisms $X \rightarrow S$ and $Y \rightarrow S$ are given. Then for any scheme $T$, there exists a natural bijection

$$(X\times_S Y)(T)\cong X(T)\times_{S(T)} Y(T)$$

Here the right-hand side is the fiber product in $\Set$, that is, the set of pairs in $X(T)\times Y(T)$ for which $X(T) \rightarrow S(T)$ and $Y(T) \rightarrow S(T)$ give the same value.
:::
::: Proof
The universal property of [§Fiber Products, ⁋Definition 1](/en/math/scheme_theory/fiber_products#def1) means that a morphism from $T$ to $X\times_S Y$ corresponds uniquely to a pair consisting of $\psi_X: T \rightarrow X$ and $\psi_Y: T \rightarrow Y$ whose compositions to $S$ agree, that is, a pair such that $\psi_X$ and $\psi_Y$ go to the same $S$-point via $X(T) \rightarrow S(T)$ and $Y(T) \rightarrow S(T)$. Writing this in the language of sets,

$$(X\times_S Y)(T)\cong \{(\psi_X, \psi_Y)\in X(T)\times Y(T)\mid \psi_X, \psi_Y \text{ map to the same element of } S(T)\}=X(T)\times_{S(T)} Y(T)$$

Naturality (for $\tau: T' \rightarrow T$ the pullbacks of both sides agree) follows from the naturality of the universal property.
:::

[Proposition 7](#prop7) allows us to interpret the fiber product as the operation of taking the fiber product *pointwise* at the functor level. From this perspective, the existence proof of [§Fiber Products, ⁋Theorem 8](/en/math/scheme_theory/fiber_products#thm8) is reinterpreted as showing that the functor $T\mapsto X(T)\times_{S(T)} Y(T)$, which is trivially defined pointwise, is representable. In particular, for the product $X\times Y=X\times_{\Spec \mathbb{Z}} Y$, one simply has $(X\times Y)(T)\cong X(T)\times Y(T)$.

---

**References**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundations of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).  

---
