---
title: "Moduli Spaces"
description: "Moduli problems are formalized via functors and stacks. The post covers representability of fine moduli spaces with universal families, automorphism obstructions, and the roles of coarse moduli spaces and moduli stacks."
excerpt: "Moduli functors, fine and coarse moduli spaces, and why the moduli stack is the right object"

categories: [Math / Stacks]
permalink: /en/math/stacks/moduli_spaces
sidebar: 
    nav: "stacks-en"

date: 2026-09-02
weight: 4
translated_at: 2026-09-02T21:15:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-09-02T21:15:05+00:00
---
We now turn to the moduli problem that was our original object of interest. As we have seen, a moduli problem is a functor

$$F:\Sch^\op\rightarrow \Grpd$$

that assigns to each object $T$ a family of geometric objects defined over $T$, and in the preceding posts we examined the conditions under which this functor becomes a sheaf. Building on this preparation, in this post we address the problem of realizing such a functor as a geometric object, and look at examples.

## Moduli Functors

We have already finished formulating such a problem as a $\Grpd$-valued pseudofunctor in [§Stacks, ⁋Example 9](/en/math/stacks/fibered_categories_and_stacks#ex9), so here we begin by giving that functor a name and fixing notation.

::: Definition 1
A pseudofunctor $\mathcal{M}:\Sch^\op \rightarrow \Grpd$ is called a *moduli functor*. ([§Stacks, ⁋Definition 3](/en/math/stacks/fibered_categories_and_stacks#def3))

For each scheme $T$, an object of the fiber groupoid $\mathcal{M}(T)$ is called a *$T$-family*. The set-valued functor obtained by retaining only isomorphism classes,

$$\underline{M}:\Sch^\op \rightarrow \Set,\qquad \underline{M}(T)=\obj \mathcal{M}(T)/\cong$$

is called the *coarse moduli functor* or the *set-valued moduli functor* of $\mathcal{M}$.
:::

The essential content of a moduli functor lies in which geometric objects a $T$-family contains. For example, when classifying curves of genus $g$, one should take a $T$-family to be a smooth projective morphism $X \rightarrow T$ all of whose geometric fibers are curves of genus $g$; when classifying vector bundles on a fixed variety $X$, one should take a rank $r$ vector bundle on $X\times T$. In either case, the pullback is given by the fiber product along a morphism $f: T' \rightarrow T$, and the compatibility condition of the pseudofunctor comes from the universal property of this fiber product, that is, from the data of canonical isomorphisms. For this reason $\mathcal{M}$ is a pseudofunctor rather than a functor, and since $\mathcal{M}(T)$ contains the $T$-families, as we saw above, one universally uses the language of CFGs when working with it. ([§Stacks, ⁋Theorem 8](/en/math/stacks/fibered_categories_and_stacks#thm8))

What unifies these two structures is the notion of a *universal family*. Recall that for a contravariant functor $F:\Sch^\op \rightarrow \Set$ and a scheme $M$, the bijection between the natural transformations from $\Hom_\Sch(-, M)$ to $F$ and the set $F(M)$ was given explicitly by

$$\alpha\mapsto \alpha_M(\id_M)$$

([\[Category Theory\] §Representable Functors, ⁋Theorem 4](/en/math/category_theory/representable_functors#thm4)). That is, a natural transformation $\alpha$ is completely determined by its single value $\alpha_M(\id_M)$ at the identity morphism, and when $\alpha$ is a natural isomorphism, the element so obtained was called a *universal element*. ([\[Category Theory\] §Representable Functors, ⁋Definition 5](/en/math/category_theory/representable_functors#def5))

The Yoneda lemma itself concerns $\Set$-valued functors, but it can be lifted to the $\Grpd$-valued setting. As in [§Stacks, ⁋Example 9](/en/math/stacks/fibered_categories_and_stacks#ex9), if we regard each scheme $T$ as the CFG given by its slice category, then the groupoid formed by the morphisms from $T$ to $\mathcal{M}$ and the 2-morphisms between them is equivalent to the fiber groupoid $\mathcal{M}(T)$, and as above this equivalence sends $f:T\rightarrow\mathcal{M}$ to $f(\id_T)$. Hence the entire datum of $f$ is determined up to isomorphism by the $T$-family $X=f(\id_T)$, and a 2-morphism between two morphisms is likewise determined by its component at $\id_T$, that is, by an isomorphism between the two $T$-families. Conversely, $X\in\mathcal{M}(T)$ determines a morphism $f_X:T\rightarrow\mathcal{M}$ assigning $u^\ast X$ to each $u:T'\rightarrow T$.

Accordingly, we can read $\id_\mathcal{M}:\mathcal{M}\rightarrow\mathcal{M}$ as the universal family over $\mathcal{M}$. Pulling it back along the morphism $f_X:T\rightarrow\mathcal{M}$ corresponding to a $T$-family $X$ amounts to taking $\id_\mathcal{M}\circ f_X=f_X$, which under the equivalence above is again $X$. That is, *every* family defined by the moduli functor $\mathcal{M}$ is obtained by pulling back the single universal family $\id_\mathcal{M}$; this is a direct generalization of [\[Algebraic Topology\] §Classifying Spaces, ⁋Theorem 8](/en/math/algebraic_topology/classifying_spaces#thm8).

## Fine Moduli Spaces

Since the only datum a scheme $M$ carries over $\Sch$ is its functor of points $\Hom_\Sch(-, M)$, which is set-valued, if we want to realize a moduli functor as a scheme, the object we should care about is not $\mathcal{M}$ itself but the coarse moduli functor $\underline{M}$. We originally made $\mathcal{M}$ take values in $\Grpd$ in order to remember the automorphisms of each family, so if the classification problem asks only for isomorphism classes, nothing is lost in this weakening. The remaining questions are whether the resulting $\underline{M}$ coincides with the functor of points of some scheme, and whether it has the properties we expect.

::: Definition 2
When the coarse moduli functor $\underline{M}:\Sch^\op \rightarrow \Set$ of a moduli functor $\mathcal{M}$ is *representable* by a scheme $M$, that is, when there exists a natural isomorphism

$$\underline{M}\cong \Hom_{\Sch}(-, M)$$

we call $M$ a *fine moduli space* of $\mathcal{M}$. In this case, the element

$$\mathcal{U}\in \underline{M}(M)$$

corresponding to the identity morphism $\id_M\in \Hom_\Sch(M, M)$ under this natural isomorphism is called the *universal family*.
:::

The universal family above is obtained by applying the Yoneda lemma to the $\Set$-valued functor $\underline{M}$: for any scheme $T$ and any $T$-family $X\in \underline{M}(T)$, the morphism $f_X: T \rightarrow M$ that the component $\underline{M}(T)\cong \Hom_\Sch(T, M)$ of the natural isomorphism assigns to $X$ is, by the naturality of Yoneda, the unique morphism satisfying

$$X\cong f_X^\ast \mathcal{U}$$

and it is called the *classifying morphism* of $X$.

This information is not essentially new. If we regard the scheme $M$ as a representable CFG, then by the 2-Yoneda lemma from the previous section, choosing a morphism $s:M\rightarrow\mathcal{M}$ is the same as choosing an $M$-family. Hence, once we choose a representative in $\mathcal{M}(M)$ of the universal family $\mathcal{U}\in\underline{M}(M)$ of a fine moduli space, the corresponding morphism $s:M\rightarrow\mathcal{M}$ is determined up to 2-isomorphism. Conversely, pulling back the tautological universal family $\id_\mathcal{M}$ over $\mathcal{M}$ along $s$ gives $\id_\mathcal{M}\circ s=s$, and the $M$-family corresponding to this morphism under the 2-Yoneda lemma is precisely $\mathcal{U}$.

From this viewpoint the relation between a moduli functor $\mathcal{M}$ and a scheme $M$ representing it also becomes clear. Choosing an arbitrary morphism $g:T\rightarrow\mathcal{M}$ determines, on the $\mathcal{M}$ side, a $T$-family $X=g(\id_T)$ that remembers even automorphisms. On the other hand, taking only the isomorphism class $[X]\in\underline{M}(T)$ of this family $X$ also determines, since $M$ represents $\underline{M}$, a unique morphism $f_X:T\rightarrow M$ on the $M$ side. Now

$$(s\circ f_X)(\id_T)=f_X^\ast s(\id_M)=f_X^\ast\mathcal{U}\cong X=g(\id_T)$$

so by the 2-Yoneda lemma again we see that $g\simeq s\circ f_X$. In other words, every morphism from a scheme to $\mathcal{M}$ factors through $M$ via $s$ up to $2$-isomorphism; conversely, an $h:T\rightarrow M$ satisfying such a condition $g\simeq s\circ h$ necessarily satisfies $X\cong h^\ast\mathcal{U}$, so $h=f_X$. Thus what looked like the universal property of $M$ is in fact the universal property of $\mathcal{M}$ together with the factorization claim $g\simeq s\circ f_X$. This factorization is unique up to $2$-isomorphism, but the $2$-isomorphism itself need not be unique when $X$ has nontrivial automorphisms.

::: Example 3 (Grassmannian)
In [\[Schemes\] §Functor of Points, ⁋Example 6](/en/math/scheme_theory/functor_of_points#ex6), for integers $0<k<n$ we defined the contravariant functor $F_{k,n}:\Sch^\op\rightarrow\Set$ by

$$F_{k,n}(T)=\{\mathcal{O}_T^{\oplus n}\twoheadrightarrow\mathcal{Q}\mid\mathcal{Q}\text{ is locally free of rank }k\}/{\cong}$$

and saw that it is naturally isomorphic to the functor of points $\Gr(k,n)$ of the Grassmannian. In this example we revisit it in the language of moduli spaces.

Writing the tautological quotient over the Grassmannian as

$$q^{\mathrm{univ}}:\mathcal{O}_{\Gr(k,n)}^{\oplus n}\twoheadrightarrow\mathcal{Q}^{\mathrm{univ}}$$

the natural isomorphism by which $\Gr(k,n)$ represents $F_{k,n}$ is given explicitly by

$$\Phi_T:\Hom_\Sch(T,\Gr(k,n))\longrightarrow F_{k,n}(T),\qquad f\longmapsto [f^\ast q^{\mathrm{univ}}]$$

In [Definition 2](#def2), the universal family is the element corresponding to $\id_{\Gr(k,n)}$ under this natural isomorphism, so

$$\mathcal{U}=\Phi_{\Gr(k,n)}(\id_{\Gr(k,n)})=[\id_{\Gr(k,n)}^\ast q^{\mathrm{univ}}]=[q^{\mathrm{univ}}]$$

Hence the universal family of $\Gr(k,n)$ is precisely the universal quotient $q^{\mathrm{univ}}$. Moreover, a quotient $q:\mathcal{O}_T^{\oplus n}\twoheadrightarrow\mathcal{Q}$ over $T$ determines a unique classifying morphism $f_q:T\rightarrow\Gr(k,n)$, and $q$ is obtained by pulling back $q^{\mathrm{univ}}$ along $f_q$.

Let us extract from the universal family the object represented by a point of this parametrizing scheme. Choosing a geometric point $x:\Spec\mathbb{K}\rightarrow\Gr(k,n)$ and pulling back the universal quotient along $x$, we obtain

$$\mathbb{K}^n\twoheadrightarrow Q_x:=x^\ast\mathcal{Q}^{\mathrm{univ}}$$

Here $Q_x$ is the geometric fiber of $\mathcal{Q}^{\mathrm{univ}}$ at $x$, and the quotient map $\mathbb{K}^n\twoheadrightarrow Q_x$ is the moduli object corresponding to $x$. Since this quotient is uniquely determined by its kernel $S_x\subseteq\mathbb{K}^n$ and $\dim S_x=n-k$, the $\mathbb{K}$-points of $\Gr(k,n)$ parametrize the $(n-k)$-dimensional subspaces of $\mathbb{K}^n$.
:::

On the other hand, a general moduli problem need not have a fine moduli space, and the moduli problem classifying vector bundles on a scheme is exactly such an example. By contrast, the functor $F_{k,n}$ of [Example 3](#ex3) classifies a rank $k$ vector bundle $\mathcal{Q}$ together with a quotient map $q:\mathcal{O}_T^{\oplus n}\twoheadrightarrow\mathcal{Q}$, and it is representable by the Grassmannian $\Gr(k,n)$. In other words, once we included the quotient map as extra data on the vector bundle, a fine moduli space appeared. This difference stems from the constraint that the quotient map imposes on automorphisms.

Why automorphisms cause trouble becomes intuitively clear when one thinks in terms of families. Using an automorphism of a moduli object, one can build a family that is locally constant but not constant over the whole base. If a fine moduli space existed, the classifying morphisms of the two families would agree locally and hence globally, yet one cannot obtain two non-isomorphic families by pulling back a single universal family along the same morphism.

The essential reason the moduli problem classifying vector bundles has no fine moduli space is that a vector bundle $\mathcal{Q}$ can have nontrivial automorphisms. By contrast, if we include the quotient map $q$ as extra data, an automorphism $\theta:\mathcal{Q}\rightarrow\mathcal{Q}$ of the whole datum must preserve $q$, so it satisfies $\theta\circ q=q$. Since $q$ is surjective, this equality forces $\theta=\id_\mathcal{Q}$. In this way, extra data added to the object being classified increases the conditions an automorphism must preserve, shrinking the automorphism group, and with enough conditions only the identity morphism remains. This effect is called rigidity, and extra data such as the quotient map $q$ of [Example 3](#ex3) is called rigidifying data.

The following proposition, then, states the failure of fine moduli spaces seen above more precisely.

::: Proposition 4
Suppose that for a moduli functor $\mathcal{M}$ there exist a scheme $T$, a surjective étale covering $S\rightarrow T$, a $T$-family $X\in\mathcal{M}(T)$, and a fixed moduli object $E$ such that $X\times_TS\cong E\times S$ but $X\not\cong E\times T$. Then $\mathcal{M}$ has no fine moduli space.
:::
::: Proof
Assume, contrary to the conclusion, that a fine moduli space $M$ exists. By [Definition 2](#def2), the set-valued moduli functor is the representable functor $\underline{M}\cong \Hom_\Sch(-, M)$. A representable functor is a sheaf for the fpqc topology, hence also for the étale topology. Among the sheaf conditions, separatedness says that for any covering $S \rightarrow T$ the restriction map

$$\underline{M}(T) \rightarrow \underline{M}(S)$$

is injective.

Now regard the two families $X$ and $E\times T$ of the hypothesis as elements of $\underline{M}(T)$. Pulling back to $S$, we have $X\times_T S\cong E\times S\cong (E\times T)\times_T S$, so the two isomorphism classes are sent to the same element of $\underline{M}(S)$. However, by hypothesis $X$ and $E\times T$ are not isomorphic over $T$, so they are distinct elements of $\underline{M}(T)$. This contradicts the injectivity of the restriction map $\underline{M}(T) \rightarrow \underline{M}(S)$. Hence $\underline{M}$ cannot even be a separated presheaf, so it cannot be representable, and a fine moduli space does not exist.
:::

The isotrivial family of [Proposition 4](#prop4) can be constructed by twisting the descent datum of the constant family $E\times S$ by elements of $\Aut(E)$. If this descent datum defines a nontrivial $\Aut(E)$-torsor, the descended family is constant over the covering but not over the base. Still, the mere existence of automorphisms does not always produce this phenomenon, so the actual obstruction must be checked separately in each moduli problem.

## Elliptic Curves

An elliptic curve over a field $\mathbb{K}$ is a smooth projective genus $1$ curve $(E,0)$ with a specified $\mathbb{K}$-rational point $0$. Over a field of characteristic $0$, it is known that every elliptic curve can be written in a short Weierstrass equation

$$E_{a,b}:\y^2=\x^3+a\x+b,\qquad \Delta=-16(4a^3+27b^2)\neq 0$$

and in this representation, a (pointed) isomorphism exists between two short Weierstrass curves $E_{a,b}$ and $E_{a',b'}$ if and only if

$$(a',b')=(\lambda^4a,\lambda^6b)$$

holds for some $\lambda\in\mathbb{K}^\times$. In this case the isomorphism is given by the coordinate change $(\x,\y)\mapsto(\lambda^2\x,\lambda^3\y)$, and the quantity that is unchanged under this coordinate change,

$$j(E_{a,b})=1728\frac{4a^3}{4a^3+27b^2}$$

is called the $j$-invariant. Over an algebraically closed field, two elliptic curves are isomorphic if and only if their $j$-invariants are equal.

Pointed automorphisms can be computed directly from this coordinate change. The $\lambda$ corresponding to an automorphism of $E_{a,b}$ satisfies $\lambda^4a=a$ and $\lambda^6b=b$. Hence if $a,b\neq0$ then $\lambda^2=1$; if $a=0$ then $\lambda^6=1$; if $b=0$ then $\lambda^4=1$. Over an algebraically closed field of characteristic $0$, these are the cases $j(E)\neq0,1728$, $j(E)=0$, and $j(E)=1728$ respectively, so

$$\Aut(E,0)\cong\begin{cases}\mu_6 & j(E)=0,\\ \mu_4 & j(E)=1728,\\ \mu_2 & j(E)\neq 0,1728\end{cases}$$

In particular, every elliptic curve retains $\mu_2=\{\pm1\}$. Writing its nontrivial automorphism as $\iota_E$, we have

$$\iota_E:(\x,\y)\longmapsto(\x,-\y)$$

::: Example 5 (Elliptic curves)
Over an algebraically closed field $\mathbb{K}$ of characteristic $0$, fix an elliptic curve $E=E_{a,b}$ with

$$ab(4a^3+27b^2)\neq0$$

Then in particular $\Delta\neq 0$, and since $a,b\neq 0$ we have $j(E)\neq0,1728$, so $\Aut(E,0)=\mu_2=\{1,\iota_E\}$.

In the moduli problem, we consider families of elliptic curves satisfying such conditions. Here a family of elliptic curves over a scheme $T$ is a pair consisting of a smooth proper morphism $\pi:\mathcal{E}\rightarrow T$ all of whose geometric fibers are smooth projective genus $1$ curves, and a section $0:T\rightarrow\mathcal{E}$.

The purpose of this example is to compute [Proposition 4](#prop4) in a concrete case. According to it, to show that the moduli of elliptic curves is not a fine moduli space, it suffices to use the nontrivial automorphism $\iota_E$ to construct a family that is locally trivial but not constant. To this end, set $T=\Spec\mathbb{K}(t)$ and consider the extension $\mathbb{K}(t)\subseteq\mathbb{K}(t)[\sqrt{t}]$. Over it, the coordinate change for $c=\sqrt{t}$ gives an isomorphism between $E_{a,b}$ and $E_{c^4a,c^6b}=E_{t^2a,t^3b}$, so we define the curve over $T$ by

$$X:\y^2=\x^3+t^2a\x+t^3b$$

Indeed, the discriminant of $X$ is $\Delta_X=t^6\Delta_E$, which is nonzero, so $X$ is an elliptic curve, and over the étale double covering $S=\Spec(\mathbb{K}(t)[\sqrt{t}])\rightarrow T$, the coordinate change $(\x,\y)\mapsto(t\x,t\sqrt{t}\y)$ gives $X\times_TS\cong E\times_{\mathbb{K}}S$. Since the two choices of $\sqrt{t}$ in this isomorphism differ by $\iota_E$, $X$ is the *quadratic twist* obtained from $\iota_E$.

On the other hand, for such an isomorphism to exist over $T$, some $c\in\mathbb{K}(t)^\times$ would have to satisfy $c^4=t^2$ and $c^6=t^3$. Then $c^2=t$, but $t$ is not a square in $\mathbb{K}(t)$. Thus $X$ is constant over $S$ but not constant over $T$.

Therefore, by [Proposition 4](#prop4), the moduli functor of elliptic curves has no fine moduli space. Moreover, since the powers of $t$ appearing in the coefficients cancel as $t^6$ in both the numerator and the denominator of the $j$-invariant, we have $j(X)=j(E)$. From this we also learn that no universal family can exist even over the affine line $\mathbb{A}^1_j$ that represents geometric isomorphism classes by the value of $j$.
:::

In the Grassmannian, the quotient map eliminated automorphisms, but for elliptic curves $\iota_E$ remains even after fixing the section, producing a nontrivial twist. This difference leads to two approaches: passing to a geometric object that remembers automorphisms, and finding an approximation that discards automorphisms and keeps only isomorphism classes.

## Moduli Stacks and Coarse Moduli Spaces

The simplest way to resolve this problem is something we already have.

::: Definition 6
When a moduli functor $\mathcal{M}$ is an algebraic stack, it is called a *moduli stack*. ([§Algebraic Stacks, ⁋Definition 6](/en/math/stacks/algebraic_stacks#def6))
:::

That is, we use the original moduli problem $\mathcal{M}$ as it is, without weakening it any further, and require only the minimal condition for it to behave geometrically, namely that it be an algebraic stack. In addition, a moduli stack $\mathcal{M}$ is a Deligne–Mumford stack if and only if the diagonal $\Delta:\mathcal{M}\rightarrow\mathcal{M}\times\mathcal{M}$ is unramified, equivalently, if and only if the stabilizer of every geometric point is unramified. ([§Algebraic Stacks, ⁋Definition 6](/en/math/stacks/algebraic_stacks#def6))

Another approach is to still consider the coarse moduli functor, but give up on the universal family and look only at a base space that records isomorphism classes.

::: Definition 7
For the coarse moduli functor $\underline{M}:\Sch^\op \rightarrow \Set$ of a moduli functor $\mathcal{M}$, a pair consisting of an algebraic space $M$ and a natural transformation $\Phi:\underline{M} \rightarrow M$ is called a *coarse moduli space* if it satisfies the following two conditions.

1. (Universality) For any algebraic space $N$ and any natural transformation $\Psi:\underline{M} \rightarrow N$, there exists a unique morphism $\pi:M\rightarrow N$ such that $\Psi=\pi\circ \Phi$.

2. (Bijection on geometric points) For any algebraically closed field $\mathbb{K}$, the component $\Phi(\Spec\mathbb{K}):\underline{M}(\Spec\mathbb{K})\rightarrow M(\mathbb{K})$ of $\Phi$ is bijective.
:::

Universality says that every natural transformation from $\underline{M}$ to an algebraic space factors uniquely through $M$, and we already discussed this condition thoroughly right after [Definition 2](#def2). The new second condition guarantees that the geometric points of $M$ correspond exactly to the geometric isomorphism classes of the objects being classified; for instance, in [Example 3](#ex3), where a fine moduli space was given, we used a similar idea to extract the object lying over a geometric point of the family. The difference, however, is that unlike then, the absence of a universal family means it is no longer possible to see functorially which geometric object such a point actually contains.

With the requirements weakened in this way, the representative result guaranteeing the existence of a coarse moduli space is the Keel–Mori theorem.

::: Theorem 8 (Keel–Mori)
If the inertia morphism

$$I_\mathcal{M}=\mathcal{M}\times_{\mathcal{M}\times_S\mathcal{M}}\mathcal{M}\longrightarrow\mathcal{M}$$

of an algebraic stack $\mathcal{M}$ that is locally of finite type over a Noetherian base $S$ is finite, then a coarse moduli space $\pi:\mathcal{M}\rightarrow M$ exists. Here $M$ is an algebraic space locally of finite type over $S$, and $\pi$ induces a bijection between geometric isomorphism classes and the geometric points of $M$. In particular, every separated Deligne–Mumford stack of finite type has a coarse moduli space.
:::

The geometric fiber of the inertia stack $I_\mathcal{M}$ is the stabilizer group scheme of the corresponding point. Hence [Theorem 8](#thm8) cannot be applied to $\bB\mathbb{G}_m$ from [§Algebraic Stacks, ⁋Example 11](/en/math/stacks/algebraic_stacks#ex11) or to $[\mathbb{A}^1/\mathbb{G}_m]$ from [§Algebraic Stacks, ⁋Example 12](/en/math/stacks/algebraic_stacks#ex12), which have positive-dimensional stabilizers. The theorem gives no conclusion about the existence of a coarse moduli space in such cases.

::: Example 9 (Coarse moduli space of elliptic curves)
Over an algebraically closed field $\mathbb{K}$ of characteristic $0$, let the parameter scheme of Weierstrass coefficients with $\Delta\neq0$ be

$$U=\Spec\mathbb{K}[a,b,\Delta^{-1}]$$

Viewing the coordinate change of elliptic curves as the $\mathbb{G}_m$-action $\lambda\cdot(a,b)=(\lambda^4a,\lambda^6b)$, the moduli stack of elliptic curves is expressed as the quotient stack

$$\mathcal{M}_{1,1}\cong[U/\mathbb{G}_m]$$

([§Algebraic Stacks, ⁋Definition 7](/en/math/stacks/algebraic_stacks#def7)). In this case, the stabilizer of each point is $\Aut(E,0)$, computed earlier. These are finite étale in characteristic $0$, so $\mathcal{M}_{1,1}$ is a Deligne–Mumford stack, and since the inertia is finite, [Theorem 8](#thm8) applies. ([§Algebraic Stacks, ⁋Theorem 10](/en/math/stacks/algebraic_stacks#thm10))

In this action, the weights of $a$ and $b$ are $4$ and $6$ respectively, and the weight of $\Delta$ is $12$. Hence the invariant ring is

$$\mathbb{K}[a,b,\Delta^{-1}]^{\mathbb{G}_m}=\mathbb{K}[j]$$

By this computation, the coarse moduli morphism guaranteed by [Theorem 8](#thm8) is given by the natural transformation

$$\Phi:\underline{M}_{1,1}\longrightarrow\mathbb{A}^1_j,\qquad(E,0)\longmapsto j(E)$$

coming from the $j$-invariant. Over an algebraically closed field, the $j$-invariant completely determines the isomorphism class of an elliptic curve, so $\Phi$ is bijective on geometric points. Therefore $(\mathbb{A}^1_j,\Phi)$ is the coarse moduli space of $\mathcal{M}_{1,1}$.

However, no universal family exists over $\mathbb{A}^1_j$. The nontrivial quadratic twist of [Example 5](#ex5) has constant $j$-invariant, so it determines the same constant morphism to $\mathbb{A}^1_j$, yet the two families are not isomorphic over the base. On the other hand, the classifying morphism to $\mathcal{M}_{1,1}$ distinguishes this twist. Moreover, over $j=0$ and $j=1728$, $\mathcal{M}_{1,1}$ remembers the $\mu_6$ and $\mu_4$ stabilizers respectively, while $\mathbb{A}^1_j$ represents these as ordinary points. This example shows that a moduli stack and its coarse moduli space carry the same geometric isomorphism classes while preserving different information.
:::

Since an elliptic curve is a smooth projective curve of genus $1$ with one marked point, $\mathcal{M}_{1,1}$ is the case $(g,n)=(1,1)$ of the moduli stack $\mathcal{M}_{g,n}$ of pointed curves. Varying the genus and the number of marked points leads to the moduli of general curves, and the questions for the next step are how to preserve automorphisms in a stack, when a coarse moduli space can be obtained, and how to compactify by adding stable curves.

**References**

**[FGA]** B. Fantechi, L. Göttsche, L. Illusie, S. L. Kleiman, N. Nitsure, A. Vistoli, *Fundamental algebraic geometry: Grothendieck's FGA explained*, American Mathematical Society, 2005.  
**[Stacks]** The Stacks Project Authors, *The Stacks Project*, https://stacks.math.columbia.edu.
