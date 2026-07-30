---
title: "Flat Morphisms"
description: "Flatness is a key property ensuring that the fibers of a morphism maintain uniform algebraic and geometric behavior over the base. This post covers the definition, geometric significance, criteria, and examples of flat morphisms in algebraic geometry."
excerpt: "Definition, geometric meaning, criteria, and examples of flat morphisms"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/flat_morphisms
sidebar: 
    nav: "scheme_theory-en"

date: 2025-02-21
weight: 14
translated_at: 2026-07-27T18:45:03+00:00
translation_source: kimi-cli
last_polished_at: 2026-07-27T18:45:03+00:00
---
We read a scheme morphism $\varphi: X \rightarrow S$ as a family parametrized by $S$ ([§Morphisms of Schemes, ⁋Example 10](/en/math/scheme_theory/morphism_of_schemes#ex10)), and defined the member of this family at $s\in S$ to be the fiber $X_s=X\times_S\Spec \kappa(s)$. ([§Fiber Products, ⁋Definition 12](/en/math/scheme_theory/fiber_products#def12)) However, how nicely this family behaves is not something we can verify at present.

Indeed, such a family can behave badly; for instance, consider

$$\Spec \mathbb{K}[t,\x]/(t\x) \longrightarrow \mathbb{A}^1_\mathbb{K}=\Spec \mathbb{K}[t].$$

Thinking of this as a family parametrized by the variable $t$, over a fixed point $t_0\neq 0$ the equation $t_0\x=0$ forces the fiber to be the single point $\x=0$, whereas over $t=0$ this condition becomes vacuous and the fiber becomes the entire line $\mathbb{A}^1_\mathbb{K}$ in the $\x$-direction. The dimension of the fiber jumps from $0$ to $1$.

What goes wrong algebraically is revealed by computing this fiber directly. Let $A=\mathbb{K}[t]$ and $B=\mathbb{K}[t,\x]/(t\x)$; then corresponding to the point $t_0$ is the maximal ideal $(t-t_0)$ of $A$, and the embedding of this point into $\Spec A$ is given by

$$\Spec \kappa(t_0)\rightarrow \Spec A$$

induced by the projection $A\rightarrow \kappa(t_0)=A/(t-t_0)$ to the residue field. That is, the fiber $X_{t_0}$ over the point $t_0$ is the pullback of this point along $\varphi$, i.e. the following diagram

{% diagram Math/Scheme_Theory/Flat_Morphisms-1.svg width="11.64em" alt="fiber_as_pullback" %}

and in this case we know from [§Fiber Products, ⁋Lemma 2](/en/math/scheme_theory/fiber_products#lem2) that $X_{t_0}$ is given by the spectrum of the tensor product

$$B\otimes_A\kappa(t_0)=\mathbb{K}[t,\x]/(t\x, t-t_0)=\mathbb{K}[\x]/(t_0\x).$$

Then if $t_0\neq 0$, since $t_0$ is a unit this becomes $\mathbb{K}[\x]/(\x)=\mathbb{K}$, a single point, and if $t_0=0$ there is nothing to divide by so it becomes $\mathbb{K}[\x]$ itself, the entire line.

Now let us examine more closely what happens at $t_0=0$, where the dimension jumps. To obtain the residue field $\kappa(0)$ we think of it as the cokernel of $\times t: A\rightarrow A$, and indeed since $A$ is an integral domain we know the following exact sequence exists:

$$0 \longrightarrow A \xrightarrow{\ \times t\ } A \longrightarrow \kappa(0) \longrightarrow 0.$$

Now applying $-\otimes_AB$ to obtain the fiber gives the following diagram

{% diagram Math/Scheme_Theory/Flat_Morphisms-2.svg width="19.88em" alt="tensoring_kills_injectivity" %}

and since the tensor product is right exact, the $0$ on the left end of the bottom row does not remain. The failure of injectivity of $\times t$ in $B$ is precisely the phenomenon that $\x\neq 0$ goes to $t\x=0$ via $\times t$, and geometrically this manifested exactly as the entire affine line surviving at $t_0=0$.

Since taking fibers is base change and base change in the affine case is tensor product, for general $X=\Spec B$ and $S=\Spec A$ the fiber at $s\in S$ is also $\Spec (B\otimes_A\kappa(s))$. More generally, the operation of moving a family along the base is always the functor $-\otimes_AB$, and as we saw above this functor need not be exact, so a similar problem occurs then too. That is, the condition we primarily desire for a family is precisely that $-\otimes_AB$ be an exact functor, i.e. flatness.

The definition of a flat module and its basic criteria are essentially the machinery we examined in [[Multilinear Algebra] §Projective, Injective, and Flat Modules, ⁋Definition 7](/en/math/multilinear_algebra/various_modules#def7) and [[Commutative Algebra] §Flatness](/en/math/commutative_algebra/flatness). As is the case with much of algebraic geometry, what matters for flatness is not so much how this machinery was built, but how it operates in the language of schemes.

> The concept of flatness is a riddle that comes out of algebra, but which technically is the answer to many prayers. - Mumford

## Definition of Flat Morphisms

As pointed out above, the condition we want is to bring the notion of a flat module from commutative algebra into geometry.

::: Definition 1
A morphism $\varphi: X \rightarrow Y$ is called *flat* if for every $x \in X$, the local ring $\mathcal{O}_{X,x}$ is flat as an $\mathcal{O}_{Y,\varphi(x)}$-module. If in addition the corresponding morphism of topological spaces is surjective, we call it *faithfully flat*.
:::

Although flatness in the above definition is given as a local condition at each point, in the affine case it can be recast as a global condition.

::: Lemma 2
For a ring homomorphism $\phi: A \rightarrow B$ and the induced morphism $\varphi: \Spec B \rightarrow \Spec A$, $\varphi$ being flat is equivalent to $B$ being flat as an $A$-module.
:::
::: Proof
For notational convenience, whenever $\mathfrak{q}\in \Spec B$ is given we write $\mathfrak{p}=\phi^{-1}(\mathfrak{q})$.

First assume $B$ is $A$-flat. Since localization $B \rightarrow B_\mathfrak{q}$ is flat ([[Commutative Algebra] §Properties of Localization, ⁋Proposition 2](/en/math/commutative_algebra/properties_of_localization#prop2)), the functor $-\otimes_AB_\mathfrak{q}$ is the composition of $-\otimes_AB$ and $-\otimes_BB_\mathfrak{q}$, hence exact. That is, $B_\mathfrak{q}$ is $A$-flat. On the other hand, since $B_\mathfrak{q}$ is an $A_\mathfrak{p}$-algebra we have $A_\mathfrak{p}\otimes_AB_\mathfrak{q}\cong B_\mathfrak{q}$, and therefore for any $A_\mathfrak{p}$-module $M$,

$$M\otimes_AB_\mathfrak{q}\cong M\otimes_{A_\mathfrak{p}}(A_\mathfrak{p}\otimes_AB_\mathfrak{q})\cong M\otimes_{A_\mathfrak{p}}B_\mathfrak{q}$$

holds. Now an injective map $M'\hookrightarrow M$ of $A_\mathfrak{p}$-modules is also an injective map of $A$-modules, so $M'\otimes_AB_\mathfrak{q} \rightarrow M\otimes_AB_\mathfrak{q}$ is injective, and by the above isomorphism $M'\otimes_{A_\mathfrak{p}}B_\mathfrak{q} \rightarrow M\otimes_{A_\mathfrak{p}}B_\mathfrak{q}$ is also injective. That is, $\mathcal{O}_{\Spec B,\mathfrak{q}}=B_\mathfrak{q}$ is $\mathcal{O}_{\Spec A,\mathfrak{p}}=A_\mathfrak{p}$-flat, and since $\mathfrak{q}$ was arbitrary, $\varphi$ is flat.

Conversely, suppose $\varphi$ is flat. For each $\mathfrak{q}$, $B_\mathfrak{q}$ is $A_\mathfrak{p}$-flat and $A \rightarrow A_\mathfrak{p}$ is flat, so by the same argument as above $B_\mathfrak{q}$ is $A$-flat. Now choose an injective map $M'\hookrightarrow M$ of $A$-modules and set

$$K=\ker(M'\otimes_AB \longrightarrow M\otimes_AB).$$

Since localization is an exact functor, for any maximal ideal $\mathfrak{q}$ of $B$ we have $K_\mathfrak{q}=\ker(M'\otimes_AB_\mathfrak{q} \rightarrow M\otimes_AB_\mathfrak{q})=0$. However, if there existed $0\neq \xi\in K$, then $\ann(\xi)$ would be a proper ideal of $B$ and hence contained in some maximal ideal $\mathfrak{q}$, and from $K_\mathfrak{q}=0$ there would exist $s\in B\setminus \mathfrak{q}$ with $s\xi=0$, giving $\ann(\xi)\not\subseteq \mathfrak{q}$, a contradiction. Therefore $K=0$ and $B$ is $A$-flat.
:::

By this lemma, when checking flatness we can almost always use the tools of commutative algebra. For instance, that flatness is stable under base change and composition is now purely algebraic computation.

::: Proposition 3
Flat morphisms are closed under base change and composition. That is, the following hold.

1. If $\varphi: X \rightarrow Y$ is flat and $Z \rightarrow Y$ is any morphism, then the base change $X \times_Y Z \rightarrow Z$ is flat. ([§Fiber Products](/en/math/scheme_theory/fiber_products))
2. If $\varphi: X \rightarrow Y$ and $\psi: Y \rightarrow Z$ are both flat, then the composition $\psi \circ \varphi: X \rightarrow Z$ is also flat.
:::
::: Proof
By [Lemma 2](#lem2), both reduce to the affine case.

(1) It suffices to show that when $A \rightarrow B$ is flat, for any $A$-algebra $C$ the map $C \rightarrow B\otimes_AC$ is flat. For any $C$-module $M$,

$$(B \otimes_A C) \otimes_C M \cong B \otimes_A (C \otimes_C M) \cong B \otimes_A M$$

so applying $-\otimes_C (B \otimes_A C)$ to an injection $M' \hookrightarrow M$ of $C$-modules gives the same as $B \otimes_A M' \rightarrow B \otimes_A M$. Since $B$ is $A$-flat, this morphism is injective, and therefore $B \otimes_A C$ is $C$-flat.

(2) Let $A \rightarrow B$ and $B \rightarrow C$ both be flat. For any $A$-module $N$, $N \otimes_A C \cong (N \otimes_A B) \otimes_B C$, so the functor $-\otimes_A C$ is the composition of $-\otimes_A B$ and $-\otimes_B C$. Since both functors are exact, their composition is as well, and therefore $C$ is $A$-flat.
:::

## Flat Families

Now let us examine some concrete situations.

::: Example 4
The following are the most basic examples of flat morphisms.

1. The inclusion morphism $U \hookrightarrow X$ of an open subscheme is flat. This is because locally it is localization, and localization is always flat. ([[Commutative Algebra] §Properties of Localization, ⁋Proposition 2](/en/math/commutative_algebra/properties_of_localization#prop2))
2. The projection $\mathbb{A}^{n+m}_\mathbb{K} \rightarrow \mathbb{A}^n_\mathbb{K}$ between affine spaces is flat. The corresponding ring homomorphism $\mathbb{K}[\x_1,\ldots,\x_n] \rightarrow \mathbb{K}[\x_1,\ldots,\x_n,\y_1,\ldots,\y_m]$ gives a free module structure, and free modules are flat.
3. The constant family $C \times_\mathbb{K} S \rightarrow S$ is flat. Since every module over a field is free, $C \rightarrow \Spec \mathbb{K}$ is flat, and by base change from [Proposition 3](#prop3) its pullback $C\times_\mathbb{K}S \rightarrow S$ is also flat.

As a representative example of a non-flat morphism, we have the one examined in the introduction,

$$X=\Spec \mathbb{K}[t,\x]/(t\x) \rightarrow \mathbb{A}^1_\mathbb{K}.$$

We have already seen that $\times t$ on $B=\mathbb{K}[t,\x]/(t\x)$ is not injective, so its failure to be flat is now a direct consequence of [Lemma 2](#lem2). Intuitively, $X$ is the union of the two coordinate axes in the plane, of which $\{\x=0\}$ surjects onto the base but $\{t=0\}$ maps to only a single point of the base. That is, $X$ has a component that does not spread out along the base but lies entirely over a single fiber, and this is what caused the fiber at $t=0$ to blow up.
:::

Reading the above counterexample algebraically again, the fact that there is an element $\x\neq 0$ in $B$ killing the parameter $t$, i.e. that $t$ is a zerodivisor in $B$, is what broke flatness. When the base is the spectrum of a PID, this phenomenon becomes exactly equivalent to the failure of flatness.

::: Proposition 5
Let $A$ be a PID and $B$ an $A$-algebra. Then $\Spec B \rightarrow \Spec A$ is flat if and only if no nonzero element of $A$ is a zerodivisor in $B$.
:::
::: Proof
By [Lemma 2](#lem2), this is equivalent to $B$ being $A$-flat. Since $A$ is a PID it is in particular an integral domain, so every nonzero element of $A$ is not a zerodivisor in $A$. Now apply [[Commutative Algebra] §Flatness, ⁋Corollary 3](/en/math/commutative_algebra/flatness#cor3) to $M=B$.
:::

That is, a family over $\mathbb{K}[t]$ being flat is the same as its coordinate ring having no torsion as a $\mathbb{K}[t]$-module. A torsion element is one killed by a single function from the base, and geometrically a component trapped in a single fiber gives rise to such an element.

To write this precisely we need the dominant morphism from [§Properties of Scheme Morphisms, ⁋Definition 19](/en/math/scheme_theory/properties_of_scheme_morphisms#def19). Below, saying that an irreducible component $Z$ of $X$ dominates the base means that after giving $Z$ a reduced closed subscheme structure, the composition of the inclusion with $\varphi$ is dominant.

::: Corollary 6
Let $B$ be a Noetherian $\mathbb{K}[t]$-algebra and suppose $X=\Spec B$ is reduced. Then $X \rightarrow \mathbb{A}^1_\mathbb{K}$ is flat if and only if every irreducible component of $X$ dominates $\mathbb{A}^1_\mathbb{K}$.
:::
::: Proof
By [Proposition 5](#prop5), flatness is equivalent to no nonzero element of $\mathbb{K}[t]$ being a zerodivisor in $B$.

Since $B$ is Noetherian, the zerodivisors of $B$ are the union of the elements of $\Ass B$. ([[Commutative Algebra] §Associated Primes, ⁋Theorem 7](/en/math/commutative_algebra/associated_primes#thm7)) Adding the assumption that $B$ is reduced, this union becomes exactly the union of the minimal prime ideals $\mathfrak{p}_1,\ldots, \mathfrak{p}_k$ of $B$. Indeed, the first result of this theorem is that minimal primes always belong to $\Ass B$, and conversely if $B$ is reduced then

$$(0)=\mathfrak{N}(B)=\bigcap_{i=1}^k \mathfrak{p}_i$$

so for a zerodivisor $a$ with $ab=0$ and $b\neq 0$, choosing $i$ such that $b\not\in \mathfrak{p}_i$ gives $a\in \mathfrak{p}_i$ from $ab=0\in \mathfrak{p}_i$.

On the other hand, the $\mathfrak{p}_i$ correspond exactly to the generic points of the irreducible components $Z_i=V(\mathfrak{p}_i)$ of $X$. Now $0\neq f\in \mathbb{K}[t]$ being a zerodivisor in $B$ is the same as $f\in \mathfrak{p}_i$ for some $i$, i.e. $f$ vanishing identically on $Z_i$. But $f$ vanishing on $Z_i$ means the image of $Z_i$ is contained in the proper closed subset $Z(f)\subsetneq \mathbb{A}^1_\mathbb{K}$, i.e. $Z_i$ does not dominate $\mathbb{A}^1_\mathbb{K}$. Conversely, if $Z_i$ does not dominate then the closure of its image is a proper closed subset, so there exists a nonzero $f\in \mathbb{K}[t]$ vanishing on it, and this $f$ belongs to $\mathfrak{p}_i$ and becomes a zerodivisor. The conclusion follows from the above.
:::

The $X=\Spec \mathbb{K}[t,\x]/(t\x)$ from the introduction is reduced and its component $\{t=0\}$ does not dominate the base, so [Corollary 6](#cor6) immediately gives non-flatness.

However, what must be noted is that flatness does not prevent the family itself from changing, but only prevents the family from collapsing. For instance, any fiber of a flat family can be singular.

::: Example 7
In this example we examine the case where a specific fiber in a family of curves becomes singular. Recall that among curve singularities, the cusp singularity and the nodal singularity occupied special positions. ([[Algebraic Varieties] §Tangent Spaces and Smoothness, ⁋Example 7](/en/math/algebraic_varieties/tangent_spaces_and_smoothness#ex7))

First consider the family of curves

$$\Spec \mathbb{K}[t, \x, \y]/(\y^2 - \x^3 - t) \longrightarrow \mathbb{A}^1_\mathbb{K}.$$

Since the relation gives $t = \y^2 - \x^3$, the coordinate ring is isomorphic to $\mathbb{K}[\x,\y]$, and under this isomorphism the action of $\mathbb{K}[t]$ is given by $t \mapsto \y^2-\x^3$. Since $\y^2-\x^3$ is not constant it is transcendental over $\mathbb{K}$, and therefore $\mathbb{K}[t] \rightarrow \mathbb{K}[\x,\y]$ is injective. Then nonzero elements of $\mathbb{K}[t]$ map to nonzero elements of an integral domain and cannot be zerodivisors, so by [Proposition 5](#prop5) this morphism is flat. Nevertheless, the fiber over $t=0$ is $\y^2=\x^3$, which has a cusp singularity.

Another family of curves

$$\Spec \mathbb{K}[t, \x, \y]/(\x\y - t) \longrightarrow \mathbb{A}^1_\mathbb{K}$$

is the same. Setting $t=\x\y$, the coordinate ring is isomorphic to the integral domain $\mathbb{K}[\x,\y]$ and $\x\y$ is also not constant, so for the same reason it is flat, and the fiber over $t\neq 0$ is the smooth hyperbola $\x\y=t$, while the fiber over $t=0$ is $\x\y=0$, two lines meeting at a nodal singularity.

In short, what flatness controls is not whether fibers become singular, but whether fibers continue with their size maintained.
:::

In the families we have seen so far, the fibers were all curves in $\mathbb{A}^2$, so points at infinity were missing. To include these as well, it is natural to cut the curves inside $\mathbb{P}^2$. ([§Projective Schemes](/en/math/scheme_theory/projective_schemes)) Then $X$ is no longer affine, so flatness must be checked on each affine chart.

::: Example 8
Consider the graded ring $A_\bullet=\mathbb{K}[t][\x,\y,\z]$ graded by the degree in $\x,\y,\z$. Here $t$ has degree $0$, so the base ring is $A_0=\mathbb{K}[t]$. Computing charts, $A_{(\x)}=\mathbb{K}[t][\y/\x,\z/\x]$ so $D_+(\x)$ is $\mathbb{A}^2_{\mathbb{K}[t]}$, and since $t$ has degree $0$ it survives localization. Patching the three charts, $\Proj A_\bullet$ becomes $\mathbb{P}^2\times_\mathbb{K}\mathbb{A}^1_\mathbb{K}$, and since $A_0\subseteq A_{(f)}$ for all $f$, these patch together to give the structure morphism $\Proj A_\bullet \rightarrow \mathbb{A}^1_\mathbb{K}$.

Now consider $\x\z-t\y^2$; since $\x\z$ and $t\y^2$ are both degree $2$ in $\x,\y,\z$, this is a homogeneous element. Here too the fact that $t$ has degree $0$ is used. Therefore $(\x\z-t\y^2)$ is a homogeneous ideal, and by [§Closed Subschemes of Projective Space, ⁋Proposition 1](/en/math/scheme_theory/closed_subschemes_of_projective_spaces#prop1),

$$X=\Proj A_\bullet/(\x\z-t\y^2)$$

is the closed subscheme $Z_+(\x\z-t\y^2)$ of $\mathbb{P}^2\times_\mathbb{K}\mathbb{A}^1_\mathbb{K}$. That is, $X$ is a family of curves cut out in $\mathbb{P}^2$ by the equation $\x\z=t\y^2$, and the above structure morphism makes this a family over $\mathbb{A}^1_\mathbb{K}$.

That this morphism is flat is checked on the three affine charts. On $D_+(\y)$, setting $u=\x/\y$, $v=\z/\y$ and dividing the relation by $\y^2$ gives $uv=t$, so the coordinate ring is $\mathbb{K}[t][u,v]/(uv-t)$, which is isomorphic to the integral domain $\mathbb{K}[u,v]$ via $t=uv$. Since $uv$ is also not constant, by the same reason as in [Example 7](#ex7) it is flat by [Proposition 5](#prop5). On $D_+(\x)$, setting $w=\y/\x$, $s=\z/\x$ and dividing by $\x^2$ gives $s=tw^2$, so the coordinate ring is $\mathbb{K}[t][w]$, which is a free $\mathbb{K}[t]$-module and hence flat. The case of $D_+(\z)$ is symmetric. Since these three cover $X$, $X \rightarrow \mathbb{A}^1_\mathbb{K}$ is flat.

Looking at the fibers, over $t=a\neq 0$ we get the smooth conic $\x\z=a\y^2$ in $\mathbb{P}^2$, which is isomorphic to $\mathbb{P}^1$. On the other hand, over $t=0$ we get $\x\z=0$, i.e. the curve consisting of the two lines $\{\x=0\}$ and $\{\z=0\}$ meeting at the point $[0:1:0]$. That is, this is a family of non-constant curves where a smooth conic degenerates into two lines, yet every fiber remains $1$-dimensional.
:::

## Failure of Flatness

Then let us examine when a morphism fails to be flat. Intuitively, a morphism fails to be flat when some part of $X$ in some way cannot spread out along the base and lies entirely over a single fiber. In the language of [Proposition 5](#prop5), this manifests as an element killed by a function from the base, i.e. torsion. However, depending on what is trapped, the outward appearance splits into three cases.

The first is $\Spec \mathbb{K}[t,\x]/(t\x)$ from the introduction of this article, where the $\x$-axis sat entirely in the fiber over $t=0$ and the dimension of the fiber jumped from $0$ to $1$. This corresponds to the case where a positive-dimensional component in the fiber direction is trapped, and was already treated in [Example 4](#ex4).

The second example is the case where what is trapped is $0$-dimensional. In this case the dimension does not jump anywhere, but only the number of points in the fiber changes.

::: Example 9
Let $X$ be the affine line with one isolated point added above the origin. The coordinate ring representing this is

$$B=\mathbb{K}[t]\times \mathbb{K},$$

and indeed this picture becomes clear if we write out the prime ideals of $B$ directly. Since $e=(0,1)$ satisfies $e(1-e)=0$, we know that any prime ideal of $B$ contains exactly one of $e$ and $1-e$, and those containing $e$ correspond to prime ideals of $B/(0\times \mathbb{K})=\mathbb{K}[t]$, while those containing $1-e$ correspond to prime ideals of $B/(\mathbb{K}[t]\times 0)=\mathbb{K}$. This can be represented in the plane $\mathbb{A}^2_\mathbb{K}$ as $X=Z(t\x, \x^2-\x)$.

Now define $\phi:\mathbb{K}[t] \rightarrow B$ by $t\mapsto (t,0)$. Then $\phi(f)=(f, f(0))$, so

$$\phi^{-1}(\mathfrak{p}\times \mathbb{K})=\mathfrak{p},\qquad \phi^{-1}(\mathbb{K}[t]\times 0)=(t).$$

That is, every point of the affine line except the origin, which is the target of $\Spec\phi$, has exactly the same point of $X$ as the unique point of its fiber, but the fiber over the origin has two points: the origin of $X$ and one point above the origin. That is, the dimension of the fiber is $0$ everywhere, but the number of points making up the fiber jumps from $1$ to $2$.

That this is not flat is because $(0,1)\neq 0$ while $t\cdot (0,1)=0$, so $t$ is a zerodivisor in $B$. ([Proposition 5](#prop5)) Since $X$ is reduced, we obtain the same conclusion from [Corollary 6](#cor6) as well, because the isolated point among the two components cannot dominate $\mathbb{A}^1_\mathbb{K}$.
:::

The last example is the case where what is trapped is an embedded point ([§Algebraic Structure of Schemes, ⁋Definition 9](/en/math/scheme_theory/algebra_of_schemes#def9)); this time neither the dimension nor the number of points changes, but the length of the fiber differs. ([[Commutative Algebra] §Jordan-Hölder Theorem, ⁋Definition 2](/en/math/commutative_algebra/Jordan-Holder_theorem#def2))

::: Example 10
Consider the scheme morphism

$$X=\Spec \mathbb{K}[t,\x]/(\x^2, t\x) \longrightarrow \mathbb{A}^1_\mathbb{K}.$$

Since the ideal decomposes as $(\x^2, t\x)=(\x)\cap (t,\x^2)$, $X$ is the $t$-axis with the origin becoming an embedded point.

The fiber of this morphism over $t=a$ is $\mathbb{K}[\x]/(\x^2, a\x)$. If $a\neq 0$ then $a$ is a unit so $\x=0$ is forced and this fiber becomes $\mathbb{K}$, but if $a=0$ it becomes $\mathbb{K}[\x]/(\x^2)$, a single point of length $2$. Topologically both $\Spec \mathbb{K}$ and $\Spec \mathbb{K}[\x]/(\x^2)$ are single points, so the dimension and number of the fiber remain the same, yet the length still jumps from $1$ to $2$.

This morphism is indeed not flat by [Proposition 5](#prop5), since $\x\neq 0$ while $t\x=0$. What requires a bit of care is that [Corollary 6](#cor6), which is the criterion derived from this, cannot be applied in this situation, because $X$ is not reduced. Indeed, the reduced structure of $X$, which is the $t$-axis, is isomorphic to the base and hence flat, so this failure is revealed only by looking at the scheme structure.
:::

Looking at these three cases, there are two interesting things. First, although we examined three different examples, essentially the length in [Example 10](#ex10) includes the failure of [Example 9](#ex9) as well. Moreover, if we lift this one level to the Hilbert polynomial, it also covers the example from the introduction. ([[Algebraic Varieties] §Bézout's Theorem, ⁋Proposition 3](/en/math/algebraic_varieties/bezout_theorem#prop3)) That is, all three failures are a single polynomial jumping, and indeed for a projective family over a Noetherian integral scheme, being flat is equivalent to the Hilbert polynomial of the fibers being constant. Another interesting point these examples reveal is about the direction of the jump: in all three cases, the value was smaller on a general open set and only grew larger as one approached where flatness broke, never moving in the opposite direction. At the end of this article we will see that this is not a coincidence.

## Generic Flatness and Chevalley's Theorem

Now in the remaining part of the article we examine further geometric properties of flat morphisms. For this, two preparations are needed, and this section is for them. Both of these preparations can be proved using [[Commutative Algebra] §Noether Normalization, ⁋Theorem 5](/en/math/commutative_algebra/noether_normalization#thm5).

::: Proposition 11 (Generic flatness)
Let $Y$ be a Noetherian integral scheme and $\varphi: X \rightarrow Y$ a finite type morphism. Then there exists a dense open subset $U$ of $Y$ such that $\varphi\rvert^U: \varphi^{-1}(U) \rightarrow U$ is flat.
:::
::: Proof
Since $Y$ is irreducible, every nonempty open subset of $Y$ is dense. Therefore it suffices to fix one affine open $V=\Spec A$ of $Y$ and find $U$ inside it. Since $Y$ is an integral scheme, $A=\mathcal{O}_Y(V)$ is an integral domain, and since an affine open of a Noetherian scheme is the spectrum of a Noetherian ring, $A$ is also a Noetherian ring. ([§The Topological Structure of Schemes, ⁋Lemma 13](/en/math/scheme_theory/topology_of_schemes#lem13))

On the other hand, since $\varphi$ is of finite type, $\varphi^{-1}(V)$ is covered by finitely many affine opens $\Spec B_1,\ldots, \Spec B_k$ ([§Properties of Scheme Morphisms, ⁋Definition 14](/en/math/scheme_theory/properties_of_scheme_morphisms#def14)), and each $B_i$ is a finite type $A$-algebra. Applying [[Commutative Algebra] §Noether Normalization, ⁋Theorem 5](/en/math/commutative_algebra/noether_normalization#thm5) to $M=B_i$, there exists $0\neq a_i\in A$ such that $(B_i)_{a_i}$ is a free $A_{a_i}$-module. Setting $a=a_1\cdots a_k$, each $(B_i)_a$ is a localization of the free module $(B_i)_{a_i}$ and hence remains a free $A_a$-module, and since free modules are flat, by [Lemma 2](#lem2)

$$\Spec (B_i)_a \longrightarrow \Spec A_a=D(a)$$

is flat. Since flatness is a local condition on $X$ and the $\Spec (B_i)_a$ cover $\varphi^{-1}(D(a))$, the map $\varphi^{-1}(D(a)) \rightarrow D(a)$ is flat. Since $A$ is an integral domain and $a\neq 0$, $D(a)$ is nonempty, so we may take $U=D(a)$ as the open set.
:::

The second proposition concerns the shape of the image. While the image of a general morphism is neither open nor closed, the image of a finite type morphism is always a "nice" set in the following sense.

::: Definition 12
A subset of a topological space $T$ is called *constructible* if it can be written as a finite union of locally closed subsets. ([[Topology] §Quotient Spaces, ⁋Definition 1](/en/math/topology/quotient_spaces#def1))
:::

Intuitively, a constructible subset is a set that can be cut out by finitely many equations and their complements, matching the pieces of geometric objects we think about. More precisely, a locally closed subset is written as the intersection $U\cap Z$ of an open and a closed set, and its complement is again a union of two locally closed subsets $(T\setminus U)\cup(T\setminus Z)$, so ([[Topology] §Quotient Spaces, ⁋Proposition 2](/en/math/topology/quotient_spaces#prop2)) we know that the collection of constructible subsets is closed under finite unions, finite intersections, and complements.

::: Theorem 13 (Chevalley)
For a Noetherian scheme $Y$ and a finite type morphism $\varphi: X \rightarrow Y$, $\varphi(X)$ is a constructible subset of $Y$.
:::
::: Proof
Since $Y$ is Noetherian it is covered by finitely many affine opens $V_j$, and since $\varphi$ is of finite type each $\varphi^{-1}(V_j)$ is also covered by finitely many affine opens. Therefore $\varphi(X)$ is a finite union of images of morphisms of the form $\Spec B \rightarrow \Spec A$. A constructible subset of an open set $V_j$ is a constructible subset of $Y$, and a finite union of constructible subsets is constructible, so it suffices to show the case where $Y=\Spec A$, $X=\Spec B$ from the start, and $B$ is a finite type $A$-algebra via a ring homomorphism $\phi: A \rightarrow B$.

This affine case is resolved by Noetherian induction on closed subsets of $Y$. For a closed subset $Z$ of $Y=\Spec A$, let the statement $P(Z)$ be:

> The image of any finite type morphism of the form $\Spec C \rightarrow Z$ is a constructible subset of $Y$.

Since $A$ is Noetherian, $Y=\Spec A$ is a Noetherian space ([§The Topological Structure of Schemes, ⁋Proposition 7](/en/math/scheme_theory/topology_of_schemes#prop7)), and we can use Noetherian induction on it. ([[Topology] §Dimension, ⁋Proposition 14](/en/math/topology/dimension#prop14)) That is, assuming $P(Z)$ holds for every proper closed subset $Z\subsetneq Y$, we show $P(Y)$.

First, for the nilradical $\mathfrak{N}=\mathfrak{N}(A)$ of $A$, since $\mathfrak{N}B$ is a nilpotent ideal of $B$, $\Spec B/\mathfrak{N}B$ and $\Spec B$ have the same underlying topological space, and the same holds for $\Spec A/\mathfrak{N}$ and $\Spec A$. ([§Dimension, §§Dimension of Schemes](/en/math/scheme_theory/dimension#dimension-of-schemes)) Therefore, if necessary we may replace $A$ by $A/\mathfrak{N}$ and $B$ by $B/\mathfrak{N}B$ to assume $A$ is reduced.

Now let $\mathfrak{p}_1,\ldots, \mathfrak{p}_k$ be the minimal primes of $A$. Then since any prime ideal always contains some minimal prime, $Y=\bigcup_j V(\mathfrak{p}_j)$. If $k\geq 2$, each $V(\mathfrak{p}_j)$ is a proper closed subset of $Y$ and

$$\varphi(X)=\bigcup_{j=1}^k \varphi\big(X\times_Y V(\mathfrak{p}_j)\big)$$

where each base change $X\times_YV(\mathfrak{p}_j)=\Spec (B\otimes_AA/\mathfrak{p}_j) \rightarrow V(\mathfrak{p}_j)$ is still affine and of finite type, so by the induction hypothesis $P(V(\mathfrak{p}_j))$ each term is constructible and hence $\varphi(X)$ is constructible. Therefore it suffices to consider only the case $k=1$, i.e. $A$ is an integral domain.

The case $B=0$ is trivial, so assume $B\neq 0$. Then by [[Commutative Algebra] §Noether Normalization, ⁋Theorem 5](/en/math/commutative_algebra/noether_normalization#thm5), there exists $0\neq a\in A$ such that $B_a$ is a free $A_a$-module. The case where $a$ is a unit is likewise trivial, so assume $a$ is a non-unit. In this case, since $A$ is an integral domain, $V(a)$ is a proper closed subset of $Y$.

First, if $B_a=0$, this means $\phi(a)$ is nilpotent in $B$, so $\phi(a)$ belongs to every prime ideal of $B$. Therefore $\varphi(X)\subseteq V(a)$, and $\varphi(X)$ equals the image of the base change $X\times_YV(a) \rightarrow V(a)$, so it is constructible by the induction hypothesis $P(V(a))$.

Finally, consider the case $B_a\neq 0$ so that $B_a$ is a nonzero free $A_a$-module. For any $\mathfrak{p}\in D(a)$, letting $r$ be the rank of $B_a$,

$$B_a\otimes_{A_a}\kappa(\mathfrak{p})\cong \kappa(\mathfrak{p})^{\oplus r}\neq 0$$

so the fiber over $\mathfrak{p}$ is nonempty, and therefore $D(a)\subseteq \varphi(X)$. Then

$$\varphi(X)=D(a)\cup \big(\varphi(X)\cap V(a)\big)$$

and $\varphi(X)\cap V(a)$ is the image of the base change $X\times_YV(a) \rightarrow V(a)$, so it is constructible by the induction hypothesis $P(V(a))$. Since $D(a)$ is open and hence constructible, $\varphi(X)$ is constructible.
:::

Finally, we also record when a constructible set becomes an open set.

::: Lemma 14
Let $E$ be a constructible subset of a Noetherian scheme $Y$. If $E$ is closed under generization, i.e. whenever $y\in E$ and $y\in \overline{\{y'\}}$ we have $y'\in E$, then $E$ is an open subset of $Y$.
:::
::: Proof
The complement $F=Y\setminus E$ is constructible and closed under specialization. Using this we show $F$ is closed. The case $F=\emptyset$ is trivial, so assume $F\neq \emptyset$ and let $Z_1,\ldots, Z_k$ be the irreducible components of $Z=\overline{F}$. Since $Y$ is Noetherian, these are finite in number.

First we show $\overline{F\cap Z_j}=Z_j$ for each $j$. If $W=\overline{F\cap Z_j}\subsetneq Z_j$, then $F\subseteq W\cup \bigcup_{i\neq j}Z_i$ and since the right side is closed, $Z=\overline{F}\subseteq W\cup \bigcup_{i\neq j}Z_i$, which contradicts $Z_j$ being an irreducible component of $Z$.

Now write $F$ as a finite union of locally closed subsets $F=\bigcup_{i=1}^n (U_i\cap C_i)$. Since $Z_j$ is irreducible and

$$Z_j=\overline{F\cap Z_j}=\bigcup_{i=1}^n \overline{U_i\cap C_i\cap Z_j},$$

for suitable $i$ we have $\overline{U_i\cap C_i\cap Z_j}=Z_j$. Then $U_i\cap C_i\cap Z_j\subseteq C_i$ and since $C_i$ is closed, $Z_j\subseteq C_i$, and therefore

$$U_i\cap Z_j\subseteq U_i\cap C_i\subseteq F.$$

On the other hand, $U_i\cap Z_j$ is an open subset of $Z_j$ whose closure is $Z_j$, so it is nonempty. Since $Z_j$ is an irreducible closed subset of $Y$, it has a generic point $\zeta_j$, and any nonempty open subset of $Z_j$ always contains $\zeta_j$, so $\zeta_j\in F$.

Since $F$ is closed under specialization, $Z_j=\overline{\{z_j\}}\subseteq F$, and since this holds for all $j$, we have $Z=\bigcup_j Z_j\subseteq F$. Since $F\subseteq Z$ is obvious, $F=Z$ is closed.
:::

## Geometric Properties of Flat Morphisms

Now that all preparations are complete, let us examine the geometric meaning of flatness. The content of flatness lies in controlling how fibers are connected to one another, and the starting point is the following observation that a flat local homomorphism is automatically faithfully flat.

::: Lemma 15
Let $\phi: (A,\mathfrak{m}) \rightarrow (B,\mathfrak{n})$ be a local homomorphism between local rings that makes $B$ a flat $A$-module. Then for any nonzero $A$-module $M$, we have $M\otimes_AB\neq 0$, and in particular $\Spec B \rightarrow \Spec A$ is surjective.
:::
::: Proof
Choose $0\neq \xi\in M$. Since $\ann(\xi)$ is a proper ideal of $A$, we have $\ann(\xi)\subseteq \mathfrak{m}$, and $A/\ann(\xi)\cong A\xi$ is a submodule of $M$. Applying the flat functor $-\otimes_AB$ gives the injective map

$$B/\ann(\xi)B\cong (A/\ann(\xi))\otimes_AB\hookrightarrow M\otimes_AB.$$

However, since $\phi$ is a local homomorphism, $\ann(\xi)B\subseteq \mathfrak{m}B\subseteq \mathfrak{n}\subsetneq B$, and therefore $B/\ann(\xi)B\neq 0$. That is, $M\otimes_AB\neq 0$.

Now for any $\mathfrak{p}\in \Spec A$, setting $M=\kappa(\mathfrak{p})$, since $\kappa(\mathfrak{p})\neq 0$ the ring

$$B\otimes_A\kappa(\mathfrak{p})$$

representing the fiber is nonzero, and hence has a prime ideal. The point of $\Spec B$ corresponding to such a prime ideal lies over $\mathfrak{p}$, so $\Spec B \rightarrow \Spec A$ is surjective.
:::

From this we obtain the *going-down* property that flat morphisms lift generizations. ([[Commutative Algebra] §System of Parameters, ⁋Lemma 8](/en/math/commutative_algebra/system_of_parameters#lem8))

::: Proposition 16
Let $\varphi: X \rightarrow Y$ be a flat morphism and $x \in X$ a point, and let $y'$ be a generization of $y=\varphi(x)$, i.e. a point $y'$ with $y \in \overline{\{y'\}}$. Then there exists a generization $x'$ of $x$ such that $\varphi(x')=y'$.
:::
::: Proof
Choose an affine open neighborhood $V=\Spec A$ of $y$, and then an affine open neighborhood $U=\Spec B$ of $x$ inside $\varphi^{-1}(V)$. Since $y'$ is a generization of $y$, we have $y'\in V$. Therefore it suffices to show the case $X=\Spec B$, $Y=\Spec A$, where letting $\phi: A \rightarrow B$ be the ring homomorphism corresponding to $\varphi$, we have $x=\mathfrak{q}$, $y=\mathfrak{p}=\phi^{-1}(\mathfrak{q})$, $y'=\mathfrak{p}'\subseteq \mathfrak{p}$.

By [Lemma 2](#lem2), $A_\mathfrak{p} \rightarrow B_\mathfrak{q}$ is a flat local homomorphism, so by [Lemma 15](#lem15), $\Spec B_\mathfrak{q} \rightarrow \Spec A_\mathfrak{p}$ is surjective. In particular, there exists a point of $\Spec B_\mathfrak{q}$ lying over $\mathfrak{p}'A_\mathfrak{p}\in \Spec A_\mathfrak{p}$, and pulling this back to a prime ideal of $B$ gives $\mathfrak{q}'$ with $\mathfrak{q}'\subseteq \mathfrak{q}$ and $\phi^{-1}(\mathfrak{q}')=\mathfrak{p}'$. Since $\mathfrak{q}'\subseteq \mathfrak{q}$ means $x\in \overline{\{x'\}}$, the point $x'=\mathfrak{q}'$ is the desired one.
:::

That is, a flat morphism always lifts generizations from the base upward. In particular, if $Y$ is irreducible and its generic point is $y$, then any point of $X$ is a specialization of some point of the generic fiber $X_y$, and therefore no component of $X$ can be trapped in a single fiber. What was observed for families over curves in [Corollary 6](#cor6) holds in general.

The first consequence of going-down is an exact equality for dimension. For a flat morphism, the local dimension of $X$ decomposes exactly into the local dimension of the base plus the local dimension of the fiber.

::: Proposition 17
For a flat morphism $\varphi: X \rightarrow Y$ between locally Noetherian schemes and points $x\in X$, $y=\varphi(x)$,

$$\dim \mathcal{O}_{X,x}=\dim \mathcal{O}_{Y,y}+\dim \mathcal{O}_{X_y,x}$$

holds. Here $X_y=\varphi^{-1}(y)$ is the fiber at $y$.
:::
::: Proof
First we check what the local ring of the fiber is. Localizing to the affine situation $X=\Spec B$, $Y=\Spec A$, letting $\phi: A \rightarrow B$ be the ring homomorphism corresponding to $\varphi$, and setting $x=\mathfrak{q}$, $y=\mathfrak{p}=\phi^{-1}(\mathfrak{q})$, by definition $X_y=\Spec (B\otimes_A\kappa(\mathfrak{p}))$, and the local ring at the point corresponding to $x$ is

$$\mathcal{O}_{X_y,x}=(B\otimes_A\kappa(\mathfrak{p}))_\mathfrak{q}\cong B_\mathfrak{q}\otimes_{A_\mathfrak{p}}\kappa(\mathfrak{p})\cong B_\mathfrak{q}/\mathfrak{p}B_\mathfrak{q}=\mathcal{O}_{X,x}/\mathfrak{m}_y\mathcal{O}_{X,x}.$$

That is, the local ring of the fiber is $\mathcal{O}_{X,x}$ divided by the maximal ideal of $\mathcal{O}_{Y,y}$.

On the other hand, since $X$ and $Y$ are locally Noetherian, $\mathcal{O}_{X,x}$ and $\mathcal{O}_{Y,y}$ are Noetherian local rings, and by [Lemma 2](#lem2), $\mathcal{O}_{Y,y} \rightarrow \mathcal{O}_{X,x}$ is a flat local homomorphism. Therefore applying [[Commutative Algebra] §System of Parameters, ⁋Theorem 9](/en/math/commutative_algebra/system_of_parameters#thm9) gives the desired equality.
:::

If $X$ and $Y$ are finite type integral schemes over a field $\mathbb{K}$, then at closed points $\dim \mathcal{O}_{X,x}=\dim X$ holds, so for closed points $y$ in the image of $\varphi$, [Proposition 17](#prop17) becomes the familiar form

$$\dim X_y=\dim X-\dim Y.$$

This equality explains the non-flatness of the example from the introduction once more. Thinking of the origin $x$ of $X=\Spec \mathbb{K}[t,\x]/(t\x)$ in that example, by [§Dimension, ⁋Proposition 8](/en/math/scheme_theory/dimension#prop8) the dimension of the local ring is given by the maximal length of chains of irreducible closed subsets going upward from the origin. The problem is that the moment we go up along the two irreducible closed subsets containing the origin (namely the $t$-axis and the $\x$-axis), there exists no irreducible closed subset containing them, so $\dim \mathcal{O}_{X,x}=1$. On the other hand, thinking of the origin $y$ of $Y=\mathbb{A}_\mathbb{K}^1$, the dimension of this point in $Y$ is likewise $\dim \mathcal{O}_{Y,y}=1$ for the same reason, and the local ring at the origin of the fiber $X_y=\mathbb{A}^1_\mathbb{K}$ is also so. Therefore $1\neq 1+1$, so this morphism is not flat. In the language of [Proposition 16](#prop16), this manifests as the $\x$-axis component passing through $x$ being trapped entirely in the fiber over $t=0$ and unable to extend in the base direction, giving $\dim \mathcal{O}_{X,x}=1\neq 2$; a component trapped in one fiber contributes its fiber-direction dimension $1$ to the right-hand side but has no base direction, breaking the equality.

Another geometric property of flat morphisms is that they send open sets to open sets, which is a consequence of [Theorem 13](#thm13) and [Lemma 14](#lem14).

::: Proposition 18
For a Noetherian scheme $Y$ and a flat finite type morphism $\varphi: X \rightarrow Y$, $\varphi$ is an open map. That is, for any open set $U\subseteq X$, $\varphi(U)$ is an open subset of $Y$.
:::
::: Proof
Since $Y$ is Noetherian and $\varphi$ is of finite type, each affine open covering $X$ is the spectrum of a finite type algebra over a Noetherian ring and hence Noetherian by [[Commutative Algebra] §Basic Notions, ⁋Theorem 12](/en/math/commutative_algebra/basic_notions#thm12), and since $\varphi$ is quasi-compact, $X$ is also quasi-compact. That is, $X$ is a Noetherian scheme in the sense of [§The Topological Structure of Schemes, ⁋Definition 14](/en/math/scheme_theory/topology_of_schemes#def14), and in particular is Noetherian as a topological space. Then an open set $U\subseteq X$ is again Noetherian by [[Topology] §Dimension, ⁋Proposition 13](/en/math/topology/dimension#prop13), and hence quasi-compact by [[Topology] §Dimension, ⁋Proposition 12](/en/math/topology/dimension#prop12), and since the inclusion of an open subscheme is flat ([Example 4](#ex4)), by [Proposition 3](#prop3) the composition $\varphi\vert_U: U \rightarrow Y$ is also flat and of finite type. Therefore it suffices to show the case $U=X$ from the start, i.e. that $\varphi(X)$ is open.

By [Theorem 13](#thm13), $\varphi(X)$ is constructible. Also, given $y\in \varphi(X)$ and its generization $y'$, choosing $x$ with $\varphi(x)=y$ and applying [Proposition 16](#prop16) gives $x'$ with $\varphi(x')=y'$, so $y'\in \varphi(X)$. That is, $\varphi(X)$ is closed under generization. Now from [Lemma 14](#lem14) we obtain that $\varphi(X)$ is open.
:::

## Local Criteria for Flatness

Finally, we record criteria for checking flatness at each point. The tool algebraically measuring how far $\otimes$ deviates from being left-exact is the left derived functor of $\otimes$, namely $\Tor$. In particular, since flatness was expressed as the vanishing of $\Tor_1^A(A/\mathfrak{a}, M)$ for all finitely generated ideals $\mathfrak{a}$ ([[Commutative Algebra] §Flatness, ⁋Proposition 1](/en/math/commutative_algebra/flatness#prop1)), translating this into the language of geometry gives the following.

::: Proposition 19
For a locally Noetherian scheme $Y$ and a morphism $\varphi: X \rightarrow Y$ locally of finite type, and points $x\in X$, $y=\varphi(x)$, $\mathcal{O}_{X,x}$ being $\mathcal{O}_{Y,y}$-flat is equivalent to

$$\Tor_1^{\mathcal{O}_{Y,y}}(\kappa(y), \mathcal{O}_{X,x})=0.$$
:::
::: Proof
Since $Y$ is locally Noetherian, $A=\mathcal{O}_{Y,y}$ is a Noetherian local ring, and since $\varphi$ is locally of finite type, $X$ is also locally Noetherian so $E=\mathcal{O}_{X,x}$ is also a Noetherian local ring. The map $A \rightarrow E$ induced by $\varphi$ is a local homomorphism, so $\mathfrak{m}_yE\subseteq \mathfrak{m}_x$ holds. Now setting $M=E$, since $M$ is a finitely generated $E$-module, all hypotheses of [[Commutative Algebra] §Flatness and Localization, ⁋Theorem 1](/en/math/commutative_algebra/local_criterion_for_flatness#thm1) are satisfied, and its conclusion is exactly the claimed equivalence.
:::

Since flatness is essentially a definition about *how* a family moves, knowing that a morphism is flat at a single point has little geometric meaning by itself. The following theorem resolves this.

::: Theorem 20 (Openness of the flat locus)
For a locally Noetherian scheme $Y$ and a morphism $\varphi: X \rightarrow Y$ locally of finite type, the set of points $x\in X$ where $\mathcal{O}_{X,x}$ is $\mathcal{O}_{Y,\varphi(x)}$-flat is an open subset of $X$.
:::

More generally, the above theorem holds even without any Noetherian condition on $Y$, as long as $\varphi$ is only locally of finite presentation. With some effort, the proof of this theorem could also be done to some extent within what we know, but we omit it for the overall length of this article.

Now by [Theorem 20](#thm20), verifying the vanishing of $\Tor$ at a point via [Proposition 19](#prop19) makes $\varphi\vert_U$ a flat morphism over an open neighborhood $U$ of that point, so results requiring flatness of the entire morphism such as [Proposition 3](#prop3) or [Proposition 18](#prop18) can be applied. In other words, the points where flatness fails form a closed set, and are confined to special places where components collide or get trapped in fibers, like the origin in the example from the introduction.

## Flatness and Semicontinuity

Earlier we observed that this breaking always occurs only in the direction of growing larger; to write this precisely, we first need the language measuring how an integer-valued invariant varies over a space.

::: Definition 21
A function $f: X \rightarrow \mathbb{Z}$ on a topological space $X$ is called *upper semicontinuous* if for every $i\in \mathbb{Z}$, the set

$$\{x\in X\mid f(x)\leq i\}$$

is an open subset of $X$. Likewise, $f$ is called *lower semicontinuous* if for every $i\in \mathbb{Z}$, the set $\{x\in X\mid f(x)\geq i\}$ is an open subset of $X$.
:::

In [Example 9](#ex9) and [Example 10](#ex10), as well as the example from the introduction, we confirmed that certain quantities measuring the failure of flatness only grew larger as one approached the point where flatness broke, never moving in the opposite direction, and this is exactly what upper semicontinuity rigorously defines. As a representative example of such a quantity, consider the following proposition.

::: Proposition 22
For a ring $A$ and a finitely generated $A$-module $M$, define the function $\mu:\Spec A \rightarrow \mathbb{Z}$ by

$$\mu(\mathfrak{p})=\dim_{\kappa(\mathfrak{p})}M\otimes_A\kappa(\mathfrak{p}).$$

Then $\mu$ is upper semicontinuous.
:::
::: Proof
We have $M\otimes_A\kappa(\mathfrak{p})=M_\mathfrak{p}/\mathfrak{p}M_\mathfrak{p}$ and $\mathfrak{p}A_\mathfrak{p}$ is the Jacobson radical of $A_\mathfrak{p}$, so by [[Commutative Algebra] §Integral Extensions, ⁋Lemma 8](/en/math/commutative_algebra/integral_extension#lem8), $\mu(\mathfrak{p})$ equals the minimum number of generators of $M_\mathfrak{p}$.

Fix $\mathfrak{p}\in \Spec A$ and let $r=\mu(\mathfrak{p})$. Multiplying the $r$ elements generating $M_\mathfrak{p}$ by denominators gives elements $m_1,\ldots, m_r$ of $M$ whose images generate $M_\mathfrak{p}$. Letting $N$ be the cokernel of $\psi: A^r \rightarrow M$ defined by these, since $N$ is a quotient of $M$ it is finitely generated, and since $\psi_\mathfrak{p}$ is surjective we have $N_\mathfrak{p}=0$.

For each generator $n_1,\ldots, n_k$ of $N$ there exists $s_j\notin \mathfrak{p}$ with $s_jn_j=0$, and since $\mathfrak{p}$ is prime, $f=s_1\cdots s_k$ also does not belong to $\mathfrak{p}$. Then $fN=0$, so for any $\mathfrak{q}\in D(f)$ we have $N_\mathfrak{q}=0$, and hence the images of $m_1,\ldots, m_r$ generate $M_\mathfrak{q}$, giving $\mu(\mathfrak{q})\leq r$. Therefore for any $\mathfrak{p}$ with $\mu(\mathfrak{p})\leq i$, we have $\mathfrak{p}\in D(f)\subseteq \{\mu\leq r\}\subseteq \{\mu\leq i\}$, so $\{\mu\leq i\}$ is open.
:::

What $\mu$ measures becomes clear when translated into the language of families. When a morphism $\Spec B \rightarrow \Spec A$ is finite, setting $M=B$ makes $\mu(\mathfrak{p})$ the dimension of the coordinate ring of the fiber $B\otimes_A\kappa(\mathfrak{p})$ as a vector space over $\kappa(\mathfrak{p})$. This algebra is Artinian so decomposes into a product of local rings, and in each factor the factors of a composition series are its residue fields, so

$$\mu(\mathfrak{p})=\sum_{x\in X_\mathfrak{p}}\length(\mathcal{O}_{X_\mathfrak{p},x})\cdot[\kappa(x):\kappa(\mathfrak{p})]$$

holds. That is, $\mu$ measures the length of the fiber together with the degree of the residue field, and if all points of the fiber are $\kappa(\mathfrak{p})$-rational, it becomes simply the length. Thus the failures of flatness examined in [Example 9](#ex9) and [Example 10](#ex10) both become instances of [Proposition 22](#prop22). If we lift this to the Hilbert polynomial, the example from the introduction can also be explained through this framing, but since we have not yet treated the scheme version of sheaf cohomology, we pass over this for now.

On the other hand, flipping [Proposition 22](#prop22) around gives lower semicontinuity. If $A$ is Noetherian then $M$ has a finite presentation

$$A^m\overset{\psi}{\rightarrow}A^n \rightarrow M \rightarrow 0$$

and since the tensor product is right exact, $\mu(\mathfrak{p})=n-\rank(\psi\otimes\kappa(\mathfrak{p}))$, so [Proposition 22](#prop22) is the same content as the matrix $\psi$ having lower semicontinuous rank. That is, the closed set where $\mu$ jumps up is explicitly given by the locus where minors of $\psi$ vanish, and the ideal generated by these minors is the Fitting ideal of [[Commutative Algebra] §Fitting Ideals, ⁋Definition 2](/en/math/commutative_algebra/fitting_ideals#def2).

---

**References**

**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).
