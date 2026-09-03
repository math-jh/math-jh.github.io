---
title: "Group Schemes"
description: "We define group schemes as group objects in the category of schemes over a base and check that this is equivalent to the pointwise description where the functor of points takes values in groups. We then cover the antiequivalence between affine group schemes and commutative Hopf algebras, the correspondence between representations and comodules, and criteria for torsors to be trivial, including fppf-local triviality."
excerpt: "Group schemes, Hopf algebras, comodules, and torsors"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/group_schemes
sidebar: 
    nav: "scheme_theory-en"

date: 2026-08-27
weight: 28
translated_at: 2026-09-02T06:15:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-09-02T06:15:04+00:00
---
We now define a *group scheme*, that is, a group object of $\Sch_{/S}$.

## Group Schemes

Classically, an algebraic group was defined as a variety equipped with a group structure whose multiplication and inversion are morphisms. ([\[Algebraic Varieties\] §Algebraic Groups, ⁋Definition 1](/en/math/algebraic_varieties/algebraic_groups#def1)) To transport this into the world of schemes, we use the categorical product and the terminal object of $\Sch_{/S}$: we regard $\Sch_{/S}$ as a cartesian monoidal category and consider group objects inside it.

::: Definition 1
A *group scheme* over a scheme $S$ is a group object of $\Sch_{/S}$. That is, a group scheme $G$ is an $S$-scheme $G$ with a structure morphism $\vartheta: G \rightarrow S$, together with three $S$-morphisms

$$\mu_G: G\times_SG \rightarrow G,\qquad \iota_G: G \rightarrow G,\qquad \epsilon_G: S \rightarrow G$$

satisfying all the conditions of [\[Category Theory\] §Monoid Objects, ⁋Definition 3](/en/math/category_theory/monoid_objects#def3). A *homomorphism* between two group schemes $G, H$ is an $S$-morphism preserving this structure.
:::

[Definition 1](#def1) specifies a group scheme as a structure internal to $\Sch_{/S}$. On the other hand, using [§Functor of Points](/en/math/scheme_theory/functor_of_points), we can turn it into an actual group, since for any test scheme $T$ the set $G(T)$ of $T$-points is a group.

::: Proposition 2
An $S$-scheme $G$ is a group scheme if and only if there is a functor $\widetilde{h}_G:(\Sch_{/S})^\op\rightarrow\Grp$ whose composition with the forgetful functor $U:\Grp\rightarrow\Set$ equals the functor of points $h_G$ of $G$. Moreover, for two group schemes $G,H$, an $S$-morphism $\varphi:G\rightarrow H$ is a group scheme homomorphism if and only if $\varphi_T:G(T)\rightarrow H(T)$ is a group homomorphism for every $T$.
:::
::: Proof
By [\[Category Theory\] §Representable Functors, ⁋Theorem 4](/en/math/category_theory/representable_functors#thm4), the Yoneda embedding $h_{(-)}:\Sch_{/S}\rightarrow\Fun((\Sch_{/S})^\op,\Set)$ is fully faithful, and by [§Functor of Points, ⁋Proposition 7](/en/math/scheme_theory/functor_of_points#prop7) it preserves finite products. Meanwhile, a group object structure in a functor category is given pointwise, so a group object structure on $h_G$ is the same data as a functor $\widetilde{h}_G:(\Sch_{/S})^\op\rightarrow\Grp$ with $U\circ\widetilde{h}_G=h_G$. The fully faithfulness of the Yoneda embedding therefore puts group object structures on $G$ in one-to-one correspondence with such functors $\widetilde{h}_G$, and applying the same argument to morphisms between group objects yields the final claim.
:::

The following are some frequently occurring examples.

::: Example 3
All of the following are group schemes over $\Spec \mathbb{Z}$.

1. The *additive group* $\mathbb{G}_a=\Spec \mathbb{Z}[\x]=\mathbb{A}^1$. By [§Functor of Points, ⁋Proposition 1](/en/math/scheme_theory/functor_of_points#prop1), we have $\mathbb{G}_a(T)\cong \Gamma(T, \mathcal{O}_T)$, and equipping this with the addition of the ring $\Gamma(T, \mathcal{O}_T)$ makes it a group. The map induced by any morphism is a ring homomorphism, hence preserves addition, so functoriality holds.

2. The *multiplicative group* $\mathbb{G}_m=\Spec \mathbb{Z}[\x, \x^{-1}]$. By [§Functor of Points, ⁋Proposition 3](/en/math/scheme_theory/functor_of_points#prop3), we have $\mathbb{G}_m(T)\cong \Gamma(T, \mathcal{O}_T)^\times$, which we equip with the multiplication of units.

3. The *$n$-th roots of unity* $\mu_n=\Spec \mathbb{Z}[\x]/(\x^n-1)$. By the adjunction of [§Affine Scheme, ⁋Theorem 13](/en/math/scheme_theory/affine_schemes#thm13),

    $$\mu_n(T)\cong \{a\in \Gamma(T, \mathcal{O}_T)\mid a^n=1\}$$

    and since $a^n=1$ implies that $a$ is a unit, this is a subgroup of $\mathbb{G}_m(T)$.

4. The *general linear group* $\GL_n=\Spec \mathbb{Z}[\x_{11},\ldots, \x_{nn}, \det{}^{-1}]$. Here $\det$ is the determinant of the matrix $(\x_{ij})$, and we have taken the localization making it invertible. Since a matrix is invertible if and only if its determinant is,

   $$\GL_n(T)=\GL(n;\Gamma(T,\mathcal{O}_T))$$

   holds. ([\[Ring Theory\] §Invertible Elements and Zero Divisors, ⁋Example 9](/en/math/ring_theory/units_and_zero_divisors#ex9)) In particular, when $T=\Spec A$ we have $\GL_n(T)=\GL(n; A)$.

5. The *special linear group* $\SL_n=\Spec \mathbb{Z}[\x_{11},\ldots, \x_{nn}]/(\det-1)$. For each $T$,

   $$\SL_n(T)=\SL(n;\Gamma(T,\mathcal{O}_T))$$

   holds. As above, in particular when $T=\Spec A$ we have $\SL_n(T)=\SL(n; A)$.

6. The *constant group scheme*. For any finite group $\Gamma$, consider the disjoint union of copies of $\Spec \mathbb{Z}$ indexed by the elements of $\Gamma$

   $$\underline{\Gamma}=\coprod_{\gamma\in\Gamma}\Spec\mathbb{Z}=\Spec\Bigl(\prod_{\gamma\in\Gamma}\mathbb{Z}\Bigr)$$

   Then for any scheme $T$, $\underline{\Gamma}(T)$ is the group of locally constant functions from the topological space $\lvert T\rvert$ to the topological group $\Gamma$ equipped with the discrete topology. In particular, when $T$ is connected, $\underline{\Gamma}(T)\cong \Gamma$.
:::

In each of the examples above, the group scheme structure was obtained via [Proposition 2](#prop2), which demonstrates the usefulness of that proposition. Moreover, although these examples were defined over $\Spec \mathbb{Z}$, they are essentially defined over every base $S$. As we saw after [§Morphisms of Schemes, ⁋Example 4](/en/math/scheme_theory/morphism_of_schemes#ex4), $\Spec \mathbb{Z}$ is the terminal object of $\Sch$, so every scheme $S$ carries a unique structure morphism $p: S\rightarrow \Spec \mathbb{Z}$, and we can consider the base change morphism it induces

$$p^\ast: \Sch\rightarrow \Sch_{/S};\qquad X\mapsto X\times_\mathbb{Z}S$$

through which a group scheme $G$ defined over $\mathbb{Z}$ can be transported to $G_S=p^\ast G$ and regarded as an $S$-scheme. From the viewpoint of [Proposition 2](#prop2), this amounts to composing $\widetilde{h}_G: \Sch^\op\rightarrow \Grp$ with the opposite functor $p_\ast^\op$ of the functor

$$p_\ast: \Sch_{/S}\rightarrow \Sch;\qquad (T\rightarrow S)\mapsto (T\rightarrow S\rightarrow \Spec\mathbb{Z})$$

to define $\widetilde{h}_{G_S}=\widetilde{h}_G\circ p_\ast^\op$, and the fact that these two agree is guaranteed by the adjunction

$$\Hom_S(T, p^\ast G)\cong \Hom_\mathbb{Z}(p_\ast T, G)$$

We write the relative group schemes over $S$ obtained in this way with subscripts, as $\mathbb{G}_{a,S}, \mathbb{G}_{m,S},\underline{\Gamma}_S,\mu_{n,S},\GL_{n,S},\SL_{n,S}$ and so on, and when the base is clear from context we drop the subscript and write $\mathbb{G}_a, \mathbb{G}_m, \underline{\Gamma}$ and so on.

All of the schemes in the examples above are affine group schemes, and the way they were defined is explicit. It is also easy to see that the examples other than $\mu_n$ are smooth over affine space. First, $\mathbb{G}_a$ is the affine line itself, so no further argument is needed, and $\GL_n$ is the open subscheme $D(\det)$ of $n^2$-dimensional affine space cut out by $\det$, of which the special case $n=1$ is $\mathbb{G}_m$. Finally, for $\SL_n$, the Laplace expansion of [\[Linear Algebra\] §Existence and Uniqueness of the Determinant, ⁋Theorem 12](/en/math/linear_algebra/existence_and_uniqueness_of_determinant#thm12) shows that the partial derivative of $f=\det-1$ with respect to $\x_{ij}$ is the cofactor $C_{ij}$ in the $(i,j)$ direction. Therefore, by [§Smooth and Étale Morphisms, ⁋Theorem 4](/en/math/scheme_theory/smooth_and_etale_morphisms#thm4), its Jacobian is given by the $1\times n^2$ matrix

$$J_f=(\partial f/\partial\x_{ij})_{i,j}=(C_{ij})_{ij}$$

Now, for any matrix belonging to $\SL_n$, fixing the $i$-th row of the matrix and considering the Laplace expansion gives the identity $\sum_j\x_{ij}C_{ij}=1$, so the ideal generated by the entries $C_{i1},\ldots, C_{in}$ among the components of the Jacobian above is the whole ring. The Jacobian therefore has full rank at every point, and hence $\SL_n$ is smooth of relative dimension $n^2-1$ over its base.

On the other hand, $\mu_n$ is finite étale if $n$ is invertible in the base. By contrast, over a field $\mathbb{K}$ of characteristic $p$, both $\mu_p$ and $\alpha_p=\ker(\Frob:\mathbb{G}_a\rightarrow\mathbb{G}_a)$ have a single point as their underlying topological space but are nonreduced *infinitesimal* group schemes. This is the same phenomenon as in [§Smooth and Étale Morphisms, ⁋Example 14](/en/math/scheme_theory/smooth_and_etale_morphisms#ex14), where a nontrivial thickening remained in the geometric fiber of an inseparable extension, preventing it from being étale, and it is another example of a property peculiar to characteristic $p$.

## Subgroup Schemes

In general, a *subgroup scheme* of a group scheme $G$ over $S$ is the data of a group scheme $H$ together with a monomorphism $\iota:H\rightarrow G$ that is a group scheme homomorphism; when $\iota$ is a closed embedding, it is called a *closed subgroup scheme*. Just as [\[Lie Theory\] §Lie Groups, ⁋Theorem 5](/en/math/lie_theory/Lie_groups#thm5) endows a closed subgroup of a Lie group with a canonical Lie group structure, the algebraic subgroups one mainly encounters for group schemes also appear as closed subgroup schemes. For instance, the first thing one examines after defining a group scheme homomorphism is its kernel. Since the kernel of a group is the preimage of the identity element, in the language of schemes this becomes the fiber product along the identity morphism.

::: Definition 4
For a group scheme homomorphism $\varphi:G\rightarrow H$ over $S$, its *kernel* is defined as the fiber product

$$\ker \varphi=G\times_{\varphi, H, \epsilon_H}S$$

Here $\epsilon_H:S\rightarrow H$ is the identity morphism of [Definition 1](#def1).
:::

Computing with [§Functor of Points, ⁋Proposition 7](/en/math/scheme_theory/functor_of_points#prop7), for each $S$-scheme $T$ we have

$$(\ker \varphi)(T)=G(T)\times_{H(T)}S(T)=\{g\in G(T)\mid \varphi_T(g)=\epsilon_{H,T}\}$$

so this definition transports the usual definition of the kernel unchanged. Since the right-hand side is a subgroup of $G(T)$ and the correspondence is natural in $T$, [Proposition 2](#prop2) implies that $\ker \varphi$ is a group scheme. What remains is whether $\ker \varphi \rightarrow G$ is a closed embedding; this depends on whether $\epsilon_H$ is a closed embedding, and that condition is precisely separatedness. ([§Valuation Rings, ⁋Definition 3](/en/math/scheme_theory/valuative_criteria#def3))

::: Proposition 5
For a group scheme homomorphism $\varphi: G \rightarrow H$ over $S$, if $H \rightarrow S$ is separated then $\ker \varphi$ is a closed subgroup scheme of $G$.
:::
::: Proof
First, closed embeddings are preserved under base change. ([§Closed Subschemes, ⁋Proposition 3](/en/math/scheme_theory/closed_subschemes#prop3)) Now let $\vartheta_H:H\rightarrow S$ be the structure morphism, and consider the following diagram.

{% diagram Math/Scheme_Theory/Group_Schemes-1.svg width="11.23em" alt="section_as_base_change" %}

Since $\epsilon_H$ is a section of $\vartheta_H$, we have $\vartheta_H\circ\epsilon_H=\id_S$, and therefore

$$(\epsilon_H\circ \vartheta_H,\id_H)\circ\epsilon_H=(\epsilon_H\circ \vartheta_H\circ\epsilon_H,\epsilon_H)=(\epsilon_H,\epsilon_H)=\Delta_{H/S}\circ\epsilon_H$$

so this square commutes. Moreover, for any scheme $T$ and morphisms $a,b:T\rightarrow H$,

$$(\epsilon_H\circ \vartheta_H,\id_H)\circ a=\Delta_{H/S}\circ b \iff(\epsilon_H\circ \vartheta_H\circ a,a)=(b,b) \iff a=b=\epsilon_H\circ \vartheta_H\circ a$$

so a $t$ with $a=b=\epsilon_H\circ t$ is uniquely determined as $\vartheta_H\circ a$. That is, the diagram above is Cartesian, and the $\epsilon_H$ on the left is the base change of $\Delta_{H/S}$. Since $\vartheta_H$ is separated, $\Delta_{H/S}$ is a closed embedding, and therefore $\epsilon_H$ is also a closed embedding. In turn, $\ker\varphi\rightarrow G$ is the base change of $\epsilon_H$ along $\varphi$, so it is a closed embedding. Since we already verified above that $\ker\varphi$ is a group scheme, it is a closed subgroup scheme of $G$.
:::

Since a morphism between affine schemes is always separated ([§Valuation Rings, ⁋Lemma 5](/en/math/scheme_theory/valuative_criteria#lem5)), the hypothesis of [Proposition 5](#prop5) holds automatically for affine group schemes over an affine base. One of the most important examples is the $n$-th power morphism $(-)^n:\mathbb{G}_m \rightarrow \mathbb{G}_m$, the homomorphism given by $a\mapsto a^n$ on each $T$. Writing the coordinate of the codomain as $\y$, this corresponds at the ring level to $\y\mapsto \x^n$, and since the identity morphism corresponds to the counit with $\y\mapsto 1$,

$$\ker(-)^n=\Spec\left(\mathbb{Z}[\x,\x^{-1}]\otimes_{\mathbb{Z}[\y,\y^{-1}]}\mathbb{Z}\right)=\Spec \mathbb{Z}[\x,\x^{-1}]/(\x^n-1)=\Spec \mathbb{Z}[\x]/(\x^n-1)=\mu_n$$

holds. ([§Fiber Products, ⁋Lemma 2](/en/math/scheme_theory/fiber_products#lem2)) Here, since $\mathbb{Z}=\mathbb{Z}[\y,\y^{-1}]/(\y-1)$, the tensor product becomes the quotient by the ideal generated by $\x^n-1$, and since $\x$ is already invertible here, the localization can be stripped off. Thus $\mu_n$ is a closed subgroup scheme of $\mathbb{G}_m$.

## Hopf Algebras

Now let us consider the case where both the base and the group scheme itself are affine. If $G=\Spec B$ and $S=\Spec A$, then since $\Spec$ is contravariant, the three morphisms $\mu_G,\epsilon_G,\iota_G$ of [Definition 1](#def1) appear on coordinate rings as $A$-algebra homomorphisms with their directions reversed:

$$\Delta:B\rightarrow B\otimes_AB,\qquad \epsilon:B\rightarrow A,\qquad \iota:B\rightarrow B$$

The associativity, identity, and inverse conditions of a group object are likewise flipped into the coassociativity, counit, and antipode conditions, respectively, and as it happens, we have already defined such an object. ([\[Category Theory\] §Monoid Objects, ⁋Definition 7](/en/math/category_theory/monoid_objects#def7)) There we called a Hopf monoid object of the symmetric monoidal category $(\rMod{A},\otimes_A,A)$ a *Hopf algebra*, and in the cases we deal with, it suffices to assume that $B$ is a commutative ring. It is then natural to expect the following.

::: Theorem 6
For a ring $A$, $\Spec$ gives an anti-equivalence between the category of commutative Hopf $A$-algebras and the category of affine group schemes over $\Spec A$. Under this correspondence, $\Delta,\epsilon,\iota$ correspond to $\mu_G,\epsilon_G,\iota_G$, respectively.
:::
::: Proof
By [§Affine Scheme, ⁋Theorem 13](/en/math/scheme_theory/affine_schemes#thm13), commutative $A$-algebras and affine schemes over $\Spec A$ are anti-equivalent, and this correspondence carries tensor products and $A$ to fiber products and the terminal object, respectively. ([§Fiber Products, ⁋Lemma 2](/en/math/scheme_theory/fiber_products#lem2)) Hence the data $\mu_G,\epsilon_G,\iota_G$ of [Definition 1](#def1) become the data $\Delta,\epsilon,\iota$ above upon reversing the arrows. Since this equivalence preserves composition and identity morphisms, the three axioms of a group object are carried to the three axioms of a Hopf algebra, and applying the same argument to structure-preserving morphisms yields the claimed anti-equivalence.
:::

In particular, for an affine group scheme $G=\Spec B$ and an arbitrary $A$-algebra $E$, the structure of the group $G(E)=\Hom_{\cAlg{A}}(B,E)$ of $E$-points of $G$ can be described completely in terms of the Hopf algebra structure of $B$: the multiplication is defined by $g\ast h=\mu_E\circ(g\otimes h)\circ\Delta$, the identity by $\eta_E\circ\epsilon$, and the inverse by $g\mapsto g\circ\iota$, where $\mu_E:E\otimes_AE\rightarrow E$ is the multiplication and $\eta_E:A\rightarrow E$ is the structure morphism.

## Representation Theory of Group Schemes

A useful tool when working with group objects is representation theory. In [\[Representation Theory\] §Representation Theory of Finite Groups, ⁋Proposition 4](/en/math/representation_theory/representations_of_finite_groups#prop4), we interpreted a representation of an ordinary group $G$ as a module over the group algebra, that is, a $G$-module, and this point of view proved useful for representations of Lie groups as well. It is only reasonable to examine it for group schemes too.

To do so, as in [Example 3](#ex3), we consider an action on some $\mathcal{O}_T$-module $\mathcal{E}_T$ for each $S$-scheme $p:T\rightarrow S$, requiring compatibility with pullback along any $S$-morphism $\varphi: T'\rightarrow T$. To bundle these together, it suffices to fix a single $\mathcal{O}_S$-module $\mathcal{E}$ and set $\mathcal{E}_T=p^\ast \mathcal{E}$ for every $p:T\rightarrow S$.

To say that the $\mathcal{E}_T$ so defined is a $G(T)$-module is then to say that a group homomorphism

$$\varrho_T:G(T)\rightarrow \Aut_{\mathcal{O}_T}(\mathcal{E}_T)$$

is given. For this to be compatible with pullback in the manner above, these homomorphisms must be natural in $T$. To state this condition properly, given a group scheme $G$ over $S$ and an $\mathcal{O}_S$-module $\mathcal{E}$ defined over $S$, consider the group-valued functor

$$\rAut(\mathcal{E}): (\Sch_{/S})^\op\rightarrow\Grp,\qquad T\mapsto\Aut_{\mathcal{O}_T}(\mathcal{E}_T)$$

then it suffices to give a morphism (that is, a natural transformation) $\widetilde{\rho}: \widetilde{h}_G\Rightarrow\rAut(\mathcal{E})$ between them; as explained above, the $T$-component of $\widetilde{\rho}$ is exactly the group homomorphism $\varrho_T$ required earlier.

Now, in order to apply the results of [\[Category Theory\] §Representable Functors](/en/math/category_theory/representable_functors), we compose each of these two functors with the forgetful functor $U: \Grp\rightarrow\Set$, and thereby regard $\widetilde{\rho}:\widetilde{h}_G\Rightarrow \rAut(\mathcal{E})$ as a natural transformation $\rho: h_G \Rightarrow F$ between the two $\Set$-valued functors $h_G = \Hom_S(-, G)$ and $F = U \circ \rAut(\mathcal{E})$. In other words, for each $S$-scheme $T$, $\rho_T$ is the group homomorphism $\widetilde{\rho}_T:G(T)\rightarrow \Aut_{\mathcal{O}_T}(\mathcal{E}_T)$ viewed as a function between the underlying sets. By [\[Category Theory\] §Representable Functors, ⁋Theorem 4](/en/math/category_theory/representable_functors#thm4), $\rho$ is then completely determined by its single value at the universal element $\id_G\in h_G(G)$:

$$\lambda:=\rho_G(\id_G)\in F(G)=\Aut_{\mathcal{O}_G}(\mathcal{E}_G).$$

Here, for $\vartheta:G\rightarrow S$, we have $\mathcal{E}_G=\vartheta^\ast\mathcal{E}$. Indeed, for any $S$-scheme $T$ and any $T$-point $g\in G(T)=\Hom_S(T, G)$, considering the diagram

{% diagram Math/Scheme_Theory/Group_Schemes-2.svg width="9.23em" alt="naturality" %}

we obtain

$$\varrho_T(g)=\rho_T(g)=\rho_T(g^\ast\id_G)=g^\ast(\rho_G(\id_G))=g^\ast\lambda,$$

so the action $\varrho_T(g)$ of an arbitrary $g\in G(T)$ is recovered as the pullback of this single automorphism $\lambda$.

The catch is that [\[Category Theory\] §Representable Functors, ⁋Theorem 4](/en/math/category_theory/representable_functors#thm4) is a result about $\Set$-valued functors, so for an *arbitrary* $\lambda\in\Aut_{\mathcal{O}_G}(\mathcal{E}_G)$, the function $\varrho_T: G(T)\rightarrow \Aut_{\mathcal{O}_T}(\mathcal{E}_T)$ defined by the method above is merely a function between sets and is not automatically a group homomorphism. Fortunately, the condition for $\varrho_T$ to be a group homomorphism can be written out explicitly, and it translates into the following two conditions on $\lambda$.

1. First, since $gh=\mu_G\circ(g, h)$ for any $g, h\in G(T)$, the condition $\varrho_T(gh)=\varrho_T(g)\circ\varrho_T(h)$ is equivalent to

    $$(g, h)^\ast(\mu_G^\ast\lambda)=(g, h)^\ast(\pr_1^\ast\lambda\circ\pr_2^\ast\lambda).$$

    Since this must hold for all $T$ and $(g, h)$, substituting the universal pair $(g, h)=\id_{G\times_S G}$ shows that the identity

    $$\mu_G^\ast\lambda=\pr_1^\ast\lambda\circ\pr_2^\ast\lambda$$

    must hold over $G\times_SG$.
2. Next, since the identity of $G(T)$ is $e_T=\epsilon_G\circ \vartheta_T$, the condition $\varrho_T(e_T)=\id_{\mathcal{E}_T}$ is equivalent to

    $$\vartheta_T^\ast(\epsilon_G^\ast\lambda)=\id_{\mathcal{E}_T}.$$

    Substituting $T=S, \vartheta_T=\id_S$ shows that the identity

    $$\epsilon_G^\ast\lambda=\id_\mathcal{E}$$

    must hold over $S$.

An $\mathcal{O}_G$-module automorphism

$$\lambda:\vartheta^\ast\mathcal{E}\xrightarrow{\sim}\vartheta^\ast\mathcal{E}$$

satisfying these two conditions is called a *$G$-linearization* of $\mathcal{E}$. Since these two conditions were obtained at the universal pair $\id_{G\times_S G}$ and at $\id_S$, respectively, for an arbitrary $S$-scheme $T$ and $g, h\in G(T)$ the original conditions for a group homomorphism are recovered by taking the pullbacks $(g, h)^\ast$ and $\vartheta_T^\ast$. In other words, giving a $G$-linearization and giving a representation of $G$ are exactly the same data. In particular, when $\mathcal{E}$ is finite locally free, $\rAut(\mathcal{E})$ is represented by the general linear group scheme $\GL(\mathcal{E})$, so this datum coincides with a group scheme homomorphism $G\rightarrow\GL(\mathcal{E})$; this is why it is called a *linearization*.

We now focus on the situation where $S=\Spec A$. Then in particular, a quasi-coherent $\mathcal{O}_S$-module $\mathcal{E}$ arises from some $A$-module $V$, so we may write $\mathcal{E}=\widetilde{V}$. Unpacking the definitions above in this situation, for an affine test scheme $\vartheta_T:T=\Spec E\rightarrow S$ we have

$$\vartheta_T^\ast\mathcal{E}\cong\widetilde{V\otimes_AE},\qquad \Aut_{\mathcal{O}_T}(\vartheta_T^\ast\mathcal{E})\cong\Aut_E(V\otimes_AE).$$

Spelled out algebraically, this becomes the following.

::: Definition 7
Suppose a ring $A$ and an $A$-module $V$ are given, and let $G$ be a group scheme over $\Spec A$. A *linear representation* of $G$ on $V$ consists of a group homomorphism

$$\varrho_E: G(E) \rightarrow \Aut_E(V\otimes_AE)$$

for each $A$-algebra $E$, natural in $E$. A *morphism* between two representations $(V, \varrho)$ and $(W, \varrho')$ is an $A$-linear map $u: V \rightarrow W$ such that $\varrho'_E(g)\circ(u\otimes\id_E)=(u\otimes\id_E)\circ\varrho_E(g)$ for every $E$ and every $g\in G(E)$.
:::

Here, the naturality of $\varrho$ means that for every $A$-algebra homomorphism $\phi: E \rightarrow E'$, the diagram

{% diagram Math/Scheme_Theory/Group_Schemes-3.svg width="36.16em" alt="naturality of representation" %}

commutes.

Now writing $G=\Spec B$, we can express the $G$-module structure in the above definition in algebraic language, that is, in the language of $B$. Of course, by the contravariance of $\Spec$, in this process we must consider a *comodule* structure.

::: Definition 8
For a Hopf $A$-algebra $B$, a $B$-*comodule* is an $A$-module $V$ together with an $A$-linear map $\rho: V \rightarrow V\otimes_AB$ satisfying the following two conditions.

1. $(\rho\otimes\id_B)\circ\rho=(\id_V\otimes\Delta)\circ\rho$.
2. Under the identification $V\otimes_AA\cong V$, $(\id_V\otimes\epsilon)\circ\rho=\id_V$.

A *morphism* between two comodules is an $A$-linear map $u: V \rightarrow W$ such that $\rho_W\circ u=(u\otimes\id_B)\circ\rho_V$.
:::

The two conditions recast the coassociativity and counit conditions of the Hopf algebra in the form imposed on $V$, and the case $V=B$ with $\rho=\Delta$ is the trivial example. The following theorem is then to be expected.

::: Theorem 9
For an affine group scheme $G=\Spec B$ over a ring $A$ and an $A$-module $V$, linear representations of $G$ on $V$ and $B$-comodule structures on $V$ are in one-to-one correspondence. Moreover, this gives an equivalence between the two categories.
:::
::: Proof
By [§Affine Scheme, ⁋Theorem 13](/en/math/scheme_theory/affine_schemes#thm13), for any $A$-algebra $E$ we have $G(E)=\Hom_{\cAlg{A}}(B, E)$, and as noted immediately after [Theorem 6](#thm6), its group structure is given by $g\ast h=\mu_E\circ(g\otimes h)\circ\Delta$, identity $\eta_E\circ\epsilon$, and inverse $g\circ\iota$.

Suppose a representation $\{\varrho_E\}_E$ is given. Choosing the universal element $\id_B\in G(B)$ and writing $\sigma=\varrho_B(\id_B)$, we define

$$\rho: V \rightarrow V\otimes_AB;\qquad \rho(v)=\sigma(v\otimes 1).$$

An arbitrary $g\in G(E)$ is an $A$-algebra homomorphism $g:B\rightarrow E$ with $G(g)(\id_B)=g$, so by naturality we obtain

$$\varrho_E(g)(v\otimes 1)=(\id_V\otimes g)(\rho(v))\tag{$\ast$}$$

and hence the whole representation is recovered from the single map $\rho$. Applying this identity to the identity element $\epsilon\in G(A)$ and to the product of the two universal elements $b\mapsto b\otimes 1,1\otimes b$, the identity condition and associativity of the group action become the counit condition and coassociativity of $\rho$, respectively.

Conversely, given a comodule structure $\rho$, one can define $\varrho_E(g)$ by the right-hand side of $(\ast)$ and extend it to an $E$-linear map. Coassociativity and the counit condition yield $\varrho_E(g)\circ\varrho_E(h)=\varrho_E(g\ast h)$ and $\varrho_E(\eta_E\circ\epsilon)=\id$, respectively, and by the antipode condition, $\varrho_E(g\circ\iota)$ is the inverse of $\varrho_E(g)$. Naturality also follows directly from $(\ast)$, so $\{\varrho_E\}_E$ is a representation, and the fact that the two constructions are mutually inverse, as well as the correspondence of morphism conditions, follows from the same identity.
:::

The most basic case is the following.

::: Example 10
Using [Theorem 9](#thm9), we classify the linear representations of the torus $\mathbb{G}_m=\Spec A[\x,\x^{-1}]$. Our claim is that representations of $\mathbb{G}_m$ on $V$ are in one-to-one correspondence with $\mathbb{Z}$-gradings

$$V=\bigoplus_{n\in \mathbb{Z}}V_n$$

of $V$.

First, any $A$-linear map $\rho: V \rightarrow V\otimes_AB$ expands uniquely with respect to the basis $\{\x^n\}_{n\in \mathbb{Z}}$ of $B$ in the form

$$\rho(v)=\sum_{n\in\mathbb{Z}}\rho_n(v)\otimes\x^n.$$

Here each $\rho_n: V \rightarrow V$ is an $A$-linear map, and for each $v\in V$ only finitely many $\rho_n(v)$ are nonzero.

Now let us find a necessary and sufficient condition for $\rho$ to satisfy the comodule conditions of [Definition 8](#def8). For the counit condition, we must have $(\id_V\otimes\epsilon)\circ\rho=\id_V$ under the identification $V\otimes_AA\cong V$, so

$$v=(\id_V\otimes\epsilon)(\rho(v))=(\id_V\otimes\epsilon)\left(\sum_{n\in\mathbb{Z}}\rho_n(v)\otimes\x^n\right)=\sum_{n\in\mathbb{Z}}\rho_n(v)\epsilon(\x^n)=\sum_{n\in\mathbb{Z}}\rho_n(v)$$

must hold. Since this holds for all $v\in V$, we obtain $\sum_{n\in\mathbb{Z}}\rho_n=\id_V$. For the coassociativity condition $(\rho\otimes\id_B)\circ\rho=(\id_V\otimes\Delta)\circ\rho$, computing the two sides gives

$$\begin{aligned}(\rho\otimes\id_B)(\rho(v))&=(\rho\otimes\id_B)\left(\sum_{n\in\mathbb{Z}}\rho_n(v)\otimes\x^n\right)=\sum_{m, n\in\mathbb{Z}}\rho_m(\rho_n(v))\otimes\x^m\otimes\x^n,\\ (\id_V\otimes\Delta)(\rho(v))&=(\id_V\otimes\Delta)\left(\sum_{k\in\mathbb{Z}}\rho_k(v)\otimes\x^k\right)=\sum_{k\in\mathbb{Z}}\rho_k(v)\otimes\x^k\otimes\x^k.\end{aligned}$$

Since the basis $\{\x^m\otimes\x^n\}_{m, n\in\mathbb{Z}}$ of $B\otimes_AB$ is linearly independent, comparing coefficients on both sides gives the condition $\rho_n\circ\rho_n=\rho_n$ where $m=n$, and $\rho_m\circ\rho_n=0$ for the remaining $m\neq n$. That is, $\{\rho_n\}_{n\in\mathbb{Z}}$ is a family of pairwise orthogonal idempotents summing to $\id_V$, and using them, if we define $V_n:=\rho_n(V)=\{v\in V\mid \rho(v)=v\otimes\x^n\}$ for each $n\in\mathbb{Z}$, then $V$ has a direct sum decomposition

$$V=\bigoplus_{n\in\mathbb{Z}}V_n.$$

Conversely, given such a $\mathbb{Z}$-grading, defining $\rho(v)=\sum_n v_n\otimes\x^n$ for each $v=\sum_n v_n$ ($v_n\in V_n$) and running the computation above in reverse shows that $\rho$ gives a $B$-comodule structure.

Now that $B$-comodule structures have been completely classified, what remains is to translate this into the geometric language $\varrho$. We have already seen that for any $A$-algebra $E$,

$$\mathbb{G}_m(E)=\Hom_{\cAlg{A}}(A[\x,\x^{-1}], E)\cong E^\times,$$

where a unit $u\in E^\times$ corresponds to the $A$-algebra homomorphism $g_u: A[\x,\x^{-1}]\rightarrow E$ defined by $\x\mapsto u$. Since $g_u(\x^n)=u^n$, for $v\in V_n$ the identity $(\ast)$ becomes

$$\varrho_E(u)(v\otimes 1)=(\id_V\otimes g_u)(\rho(v))=(\id_V\otimes g_u)(v\otimes\x^n)=v\otimes g_u(\x^n)=u^n(v\otimes 1).$$

That is, by $E$-linearity, $u\in\mathbb{G}_m(E)=E^\times$ acts on the elements of $V_n\otimes_AE$ exactly as multiplication by $u^n$.
:::

We call $V_n$ in [Example 10](#ex10) the part of weight $n$; this decomposition becomes a standard tool when dealing with torus actions. For the torus $\mathbb{G}_m^r$, repeating the same computation shows that the grading is indexed by $\mathbb{Z}^r$, with each component corresponding to one character of the torus.

## Torsors

The reason we consider group schemes is (of course) to define group actions on schemes.

::: Definition 11
Let $G$ be a group scheme defined over $S$, and let $X$ be an $S$-scheme. A *left action* of $G$ on $X$ is an $S$-scheme morphism $\varrho: G\times_SX \rightarrow X$ such that, for every $S$-scheme $T$, the induced map

$$\varrho_T: G(T)\times X(T) \rightarrow X(T)$$

is an action of $G(T)$ on the set $X(T)$.
:::

Then again, in the spirit of [Proposition 2](#prop2), the condition above is equivalent to the following two conditions that a group action must satisfy:

$$\varrho\circ(\mu_G\times\id_X)=\varrho\circ(\id_G\times\varrho),\qquad \varrho\circ(\epsilon_G\circ p, \id_X)=\id_X$$

Here $p: X \rightarrow S$ is the structure morphism.

Once a group action on a scheme is given, the next geometrically natural question is to construct the space of orbits, namely the quotient $\overline{X}=X/G$ and the quotient morphism $\varpi: X \rightarrow \overline{X}$, and to understand its structure. However, this is not always the behavior one expects even for topological spaces, and we would like the action to be at least free and simply transitive on each orbit. In this case, the fiber $\varpi^{-1}(\overline{x})$ over each orbit point $\overline{x}\in \overline{X}$ has the same shape as $G$, so we can interpret $X\rightarrow \overline{X}$ as a collection of fibers shaped like $G$. Now the problem, much as in [\[Algebraic Topology\] §Classifying Spaces, ⁋Definition 1](/en/math/algebraic_topology/classifying_spaces#def1), is that there is no way to choose, for each orbit, a basepoint corresponding to the identity of $G$; because of this, each fiber is not $G$ itself but a fiber that only remembers the way $G$ acts.

::: Definition 12
Let $G$ be a group scheme over $S$ and let $P$ be an $S$-scheme equipped with a left action $\varrho: G\times_SP \rightarrow P$. We say that $P$ is a *$G$-torsor* if the following two conditions hold.

1. $P \rightarrow S$ is faithfully flat and locally of finite presentation. ([§Flat Morphisms, ⁋Definition 1](/en/math/scheme_theory/flat_morphisms#def1), [§Properties of Scheme Morphisms, ⁋Definition 18](/en/math/scheme_theory/properties_of_scheme_morphisms#def18))
2. The morphism induced by the action and the projection

   $$(\varrho, \pr_2): G\times_SP \rightarrow P\times_SP$$

   is an isomorphism.

A $G$-torsor $P$ is *trivial* if there exists a $G$-equivariant isomorphism of $S$-schemes with $G$ itself, equipped with the left translation action.
:::

The second condition reflects the requirement that, for each test scheme,

$$G(T)\times P(T) \rightarrow P(T)\times P(T);\qquad (g, q)\mapsto (g\cdot q, q)$$

is a bijection, that is, the simply transitive condition. Roughly speaking, the first condition is needed to properly formulate local triviality: as we saw in [§Faithfully Flat Descent](/en/math/scheme_theory/faithfully_flat_descent), in algebraic geometry a Zariski open cover alone does not carry enough information, so we require $P \rightarrow S$ itself to play the role of an *fppf covering*. Here fppf abbreviates *fidèlement plat de présentation finie*.

Meanwhile, just as in [\[Algebraic Topology\] §Classifying Spaces, ⁋Proposition 2](/en/math/algebraic_topology/classifying_spaces#prop2), the (global) triviality of a torsor is exactly equivalent to the existence of a global section.

::: Proposition 13
For a $G$-torsor $P$ over $S$, $P$ is trivial if and only if $P(S)\neq \emptyset$, that is, if and only if $P \rightarrow S$ admits a section.
:::
::: Proof
If $P$ is trivial, then the element of $P(S)$ corresponding to the identity $\epsilon_G\in G(S)$ of $G$ provides a section.

Conversely, suppose a section $s\in P(S)$ is given. As in [\[Algebraic Topology\] §Classifying Spaces, ⁋Proposition 2](/en/math/algebraic_topology/classifying_spaces#prop2), consider the composition

$$\varphi: G\cong G\times_SS\xrightarrow{\ \id_G\times s\ }G\times_SP\xrightarrow{\ \varrho\ }P$$

Then for every $S$-scheme $T$ we have $\varphi_T(g)=g\cdot s_T$. By the second condition of [Definition 12](#def12), $g\mapsto g\cdot s_T$ is a bijection from $G(T)$ to $P(T)$, so by [\[Category Theory\] §Representable Functors, ⁋Theorem 4](/en/math/category_theory/representable_functors#thm4), $\varphi$ is an isomorphism. Moreover, $\varphi_T(g'g)=(g'g)\cdot s_T=g'\cdot\varphi_T(g)$, so $\varphi$ is $G$-equivariant, and therefore $P$ is trivial.
:::

[Proposition 13](#prop13) says that whether a torsor is trivial over the original base $S$ depends solely on the existence of a global section $S \rightarrow P$. Thus a torsor without a global section is never trivial over $S$. On the other hand, if we base change a torsor $P$ over itself via the morphism $P \rightarrow S$, the diagonal morphism $\Delta: P \rightarrow P\times_SP$ always serves as a section, so over $P$ we always have $P\times_SP \cong G\times_SP$, and it becomes trivial. This is the same phenomenon as in topology, where pulling a principal bundle back over its total space always makes it trivial.

::: Proposition 14
For a $G$-torsor $P$ over $S$, the following hold.

1. The second projection $P\times_SP \rightarrow P$ is a torsor over $P$ for the group scheme $G_P=G\times_SP$, and it is trivial. In other words, $P$ becomes trivial over the fppf covering $\{P \rightarrow S\}$.
2. If $G \rightarrow S$ is affine and $P \rightarrow S$ is quasi-compact ([§Properties of Scheme Morphisms, ⁋Definition 2](/en/math/scheme_theory/properties_of_scheme_morphisms#def2)), then $P \rightarrow S$ is also affine.
:::
::: Proof
Let us prove 1. The properties of being flat, locally of finite presentation, and surjective, as well as isomorphisms of fiber products, are all preserved under base change ([§Flat Morphisms, ⁋Proposition 3](/en/math/scheme_theory/flat_morphisms#prop3), [§Fiber Products, ⁋Proposition 16](/en/math/scheme_theory/fiber_products#prop16)), so the second projection $P\times_SP \rightarrow P$ is a $G_P$-torsor over $P$. Since the diagonal morphism $\Delta: P \rightarrow P\times_SP$ is a section of this projection, by [Proposition 13](#prop13) this torsor is trivial. That is, over $P$ we have $P\times_SP\cong G\times_SP$. Meanwhile, $P \rightarrow S$ is an fppf covering by definition.

Let us prove 2. Choose an affine open subset $V$ of $S$; then $V$ is quasi-compact ([§The Spectrum, ⁋Lemma 12](/en/math/scheme_theory/spectrums#lem12)), and since $P \rightarrow S$ is quasi-compact, its preimage is also quasi-compact. Hence $\{P \rightarrow S\}$ is an fpqc covering in the sense of [§Faithfully Flat Descent, ⁋Definition 9](/en/math/scheme_theory/faithfully_flat_descent#def9). Now, being affine is preserved under base change, so $G\times_SP \rightarrow P$ is affine, and by 1, $P\times_SP \rightarrow P$ is also affine. Since affineness is local on the base for fpqc coverings ([§Faithfully Flat Descent, ⁋Proposition 13](/en/math/scheme_theory/faithfully_flat_descent#prop13)), $P \rightarrow S$ itself is affine.
:::

As can be seen from the proof above, the quasi-compact assumption in the second item of [Proposition 14](#prop14) serves to promote the fppf covering $\{P \rightarrow S\}$ to an fpqc covering; in general, a quasi-compact fppf covering is always an fpqc covering. If $P$ is a Noetherian scheme, then by [§Properties of Scheme Morphisms, ⁋Proposition 4](/en/math/scheme_theory/properties_of_scheme_morphisms#prop4) an fppf morphism is automatically quasi-compact, so this assumption always holds.

More generally, for a covering family $\{f_i: U_i \rightarrow X\}$ of a scheme $X$, we call it a *Zariski covering* if the $f_i$ are open immersions, an *étale covering* if they are flat and unramified, an *fppf covering* if they are flat and locally of finite presentation, and an *fpqc covering* if they are flat and quasi-compact. By definition, we then have the implications

$$\text{Zariski}\implies\text{étale}\implies\text{fppf}$$

among the properties of a given covering. [Proposition 14](#prop14) above partially illustrates how these implications are used: as we saw in the proof, a quasi-compact fppf covering is an fpqc covering, and using this fact we transferred the affineness statement for fpqc coverings seen in [§Faithfully Flat Descent, ⁋Proposition 13](/en/math/scheme_theory/faithfully_flat_descent#prop13) to the fppf setting.

Intuitively, [Proposition 14](#prop14) shows that even if a torsor $P$ may differ from $G$ over the base $S$, once we pass to the fppf covering $\{P \rightarrow S\}$ it becomes the trivial torsor $G\times_SP$. In other words, a torsor can be understood as an object obtained by gluing $G$ along an fppf covering via a descent datum in the sense of [§Faithfully Flat Descent, ⁋Definition 4](/en/math/scheme_theory/faithfully_flat_descent#def4), and when $G$ is affine, [§Faithfully Flat Descent, ⁋Theorem 12](/en/math/scheme_theory/faithfully_flat_descent#thm12) guarantees that such data actually give rise to a scheme over $S$.

::: Example 15
1. Consider the $S=\Spec\mathbb{R}$-scheme $p:P=\Spec \mathbb{C}\rightarrow S$, and let $\vartheta:G\rightarrow S$ be the constant group $S$-scheme

    $$G=\underline{(\mathbb{Z}/2)}_S=S\amalg S=\Spec(\mathbb{R}\times\mathbb{R})$$

    defined by the finite group $\mathbb{Z}/2$. ([Example 3](#ex3)) This is a two-point set, with each point carrying the information of $\mathbb{R}$. We now consider the situation in which it acts on $\Spec \mathbb{C}$, another one-point set. Writing $c$ for complex conjugation, we can define the group scheme action $\varrho: G\times_SP\rightarrow P$ on it by the diagram

    {% diagram Math/Scheme_Theory/Group_Schemes-4.svg width="13.92em" alt="action_definition" %}

    Intuitively, $\varrho$ carries one component $P$ over by $\id_P$, while the other component $P$ is carried over by the map induced by $c$.

    Then this is a $G$-torsor. Checking the conditions of [Definition 12](#def12), first, since $\mathbb{C}$ is a free module of rank $2$ over $\mathbb{R}$, the map $P \rightarrow S$ is faithfully flat and locally of finite presentation. For the second condition, we have $G\times_SP=\Spec(\mathbb{C}\times\mathbb{C})$ and $P\times_SP=\Spec(\mathbb{C}\otimes_\mathbb{R}\mathbb{C})$, and writing out algebraically the algebra homomorphism corresponding to $\varrho$, it is given by

    $$\rho:\mathbb{C}\rightarrow\mathbb{C}\times\mathbb{C};\qquad z\mapsto(z,\bar z)$$

    Then $(\varrho, \pr_2)$ is, algebraically,

   $$\mathbb{C}\otimes_\mathbb{R}\mathbb{C} \rightarrow \mathbb{C}\times\mathbb{C};\qquad z\otimes w\mapsto (zw, \bar zw)$$

   and since this is an $\mathbb{R}$-algebra isomorphism, the second condition of [Definition 12](#def12) holds.

   On the other hand, since there exists no $\mathbb{R}$-algebra homomorphism $\mathbb{C} \rightarrow \mathbb{R}$, we have $P(S)=\emptyset$, and by [Proposition 13](#prop13) this torsor is not trivial.

2. Consider the multiplicative group scheme $G=\mathbb{G}_{m, S}=\Spec_S \mathcal{O}_S[\x, \x^{-1}]$ over a base scheme $S$, and an invertible sheaf $\mathcal{L}$. Just as we assembled the bases (frames) of each fiber of a vector bundle to form a principal bundle in [\[Algebraic Topology\] §Classifying Spaces, ⁋Proposition 4](/en/math/algebraic_topology/classifying_spaces#prop4), in algebraic geometry we can likewise construct from $\mathcal{L}$ a $\mathbb{G}_m$-torsor $P_\mathcal{L}$, a kind of frame bundle. First, since $\mathcal{L}$ is by definition Zariski-locally free of rank $1$, there exists an affine Zariski open cover $\{U_i\}$ with local trivializations $\varphi_i: \mathcal{L}\vert_{U_i} \xrightarrow{\sim} \mathcal{O}_{U_i}$. Let the transition functions be

    $$g_{ij} = \varphi_i\circ \varphi_j^{-1}\in \Gamma(U_i\cap U_j, \mathcal{O}_S^\times)=\mathbb{G}_m(U_i\cap U_j)$$

    If we glue the schemes $P_i = \mathbb{G}_{m, U_i} = \Spec \mathcal{O}_S(U_i)[\x, \x^{-1}]$ over each $U_i$ along the overlaps $U_i\cap U_j$ via multiplication by the transitions $g_{ij}$

    $$(t, u)\sim (g_{ij}(u)t, u)$$

    then by [§Schemes, ⁋Lemma 9](/en/math/scheme_theory/schemes#lem9), an $S$-scheme $p:P_\mathcal{L}\rightarrow S$ is well defined. The group scheme action $\varrho: \mathbb{G}_m\times_S P_\mathcal{L} \rightarrow P_\mathcal{L}$ on it is now defined over each $U_i$ by the multiplication of $\mathbb{G}_m$

    $$\mathbb{G}_{m, U_i}\times_{U_i} \mathbb{G}_{m, U_i} \longrightarrow \mathbb{G}_{m, U_i};\qquad (a, t)\mapsto at$$

    Our claim is that this is a $G$-torsor.

    First, since locally $P_\mathcal{L}\vert_{U_i}\cong \mathbb{G}_{m, U_i} \rightarrow U_i$ is faithfully flat and of finite presentation, and these properties are local on the base, the map $p:P_\mathcal{L}\rightarrow S$ is faithfully flat and locally of finite presentation. As for the map $(\varrho, \pr_2): \mathbb{G}_m\times_S P_\mathcal{L} \rightarrow P_\mathcal{L}\times_S P_\mathcal{L}$ in the second condition of [Definition 12](#def12), over each $U_i$ it corresponds to the morphism

    $$\mathbb{G}_{m, U_i}\times_{U_i}\mathbb{G}_{m, U_i} \longrightarrow \mathbb{G}_{m, U_i}\times_{U_i}\mathbb{G}_{m, U_i};\qquad (a, t)\mapsto (at, t)$$

    which, algebraically, is given by the map between coordinate rings

    $$\mathcal{O}(U_i)[\x^{\pm 1}, \y^{\pm 1}]\rightarrow \mathcal{O}(U_i)[\x^{\pm 1}, \y^{\pm 1}];\qquad \x\mapsto \x\y, \y\mapsto \y$$

    Since this is an isomorphism with inverse $\x\mapsto \x\y^{-1}$, $\y\mapsto \y$, the map $(\varrho, \pr_2)$ is an isomorphism.

    Hence $P_\mathcal{L}$ is a $\mathbb{G}_m$-torsor over $S$, and by [Proposition 13](#prop13) one can check that $P_\mathcal{L}$ being trivial is equivalent to $\mathcal{L}\cong \mathcal{O}_S$.

    Looking at how this gluing works from the viewpoint of cohomology, the transition data $g_{ij}\in \Gamma(U_i\cap U_j, \mathcal{O}_S^\times)$ gluing together $P_\mathcal{L}$ satisfy exactly the Čech 1-cocycle condition $g_{ij}g_{jk}=g_{ik}$ over $U_i\cap U_j\cap U_k$. Moreover, if we change the base of each local trivialization $\varphi_i$ over $U_i$ by a nonvanishing function $c_i\in \Gamma(U_i, \mathcal{O}_S^\times)$, the new transition data becomes $c_i g_{ij} c_j^{-1}$, so the difference arising from the choice of trivialization corresponds exactly to a Čech 1-coboundary. Thus these transition data determine a class $[g_{ij}]\in \check{H}^1(\{U_i\}, \mathcal{O}_S^\times)$ in Čech cohomology, and the image of this class in sheaf cohomology corresponds to the isomorphism class $[\mathcal{L}]\in H^1_\Zar(S, \mathcal{O}_S^\times)\cong \Pic(S)$ of $\mathcal{L}$.

    A noteworthy fact is that this gluing was carried out at the level of Zariski open sets. To distinguish them, if we write $H^1_\Zar(S, \mathcal{O}_S^\times)$ for the (ordinary) sheaf cohomology with respect to Zariski open sets, then since every Zariski covering is an fppf covering, it is known that there exists a natural inclusion

    $$H^1_\Zar(S, \mathcal{O}_S^\times)\hookrightarrow H^1_\fppf(S, \mathbb{G}_m)$$

    In particular, if $H^1_\fppf(S, \mathbb{G}_m)=0$, then $H^1_\Zar(S, \mathcal{O}_S^\times)=0$ is forced. What is interesting is that for a general group scheme $G$, such an inclusion $H^1_\Zar(S, G)\hookrightarrow H^1_\fppf(S, G)$ can be strict; this means that there may exist more twisted $G$-torsors that are locally trivial over an fppf covering but not trivial over any Zariski open cover, and the $\mathbb{Z}/2$-torsor $P=\Spec \mathbb{C}\rightarrow \Spec \mathbb{R}$ of the first example is exactly such a case. In this situation, $H^1_\Zar(\Spec \mathbb{R}, \mathbb{Z}/2)=0$ but $H^1_\fppf(\Spec \mathbb{R}, \mathbb{Z}/2)\cong \mathbb{Z}/2$, yielding the strict inclusion $H^1_\Zar \subsetneq H^1_\fppf$.

    On the other hand, in the special case $G=\mathbb{G}_m$, Grothendieck's Hilbert theorem 90 holds: $H^1_\fppf(X, \mathbb{G}_m)\cong \Pic(X)$ for any scheme $X$. In particular, since every invertible module over a local ring is a free module of rank $1$, we have $H^1_\fppf(\Spec \mathcal{O}_{S,s}, \mathbb{G}_m)=0$ for each point $s\in S$ of the scheme. A trivialization at each point extends to some Zariski open neighborhood, so any fppf $\mathbb{G}_m$-torsor is already trivialized over some Zariski open cover and is therefore isomorphic to the frame bundle $P_\mathcal{L}$ of an invertible sheaf. That is, for $\mathbb{G}_m$ the above inclusion is not strict but an isomorphism, so that

    $$H^1_\fppf(S, \mathbb{G}_m)\cong H^1_\Zar(S, \mathcal{O}_S^\times)\cong \Pic(S)$$

    holds.
:::

As seen in [Example 15](#ex15), for an affine group scheme $G$, the equivalence classes of transition data gluing together a $G$-torsor over a covering form the first cohomology set $H^1(S, G)$ (in the fppf topology, $H^1_\fppf(S, G)$). When $G$ is not abelian, $H^1(S, G)$ is a pointed set without a group structure, but it still classifies all isomorphism classes of $G$-torsors over $S$. Meanwhile, instead of merely counting torsors as a set, one can treat the groupoid they form as a single geometric object; quotient stacks such as $[\Spec \mathbb{K}/\mathbb{G}_m]$, which classifies $\mathbb{G}_m$-torsors over a field $\mathbb{K}$, are exactly the objects obtained this way, and they form the starting point of stack theory.

---

**References**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).
