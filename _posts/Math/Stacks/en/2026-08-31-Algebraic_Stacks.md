---
title: "Algebraic Stacks"
description: "We define algebraic stacks (Artin and Deligne-Mumford) via representability of the diagonal and the existence of a smooth atlas, then construct the quotient stack [U/G] of a group action and BG = [pt/G], discussing their geometric meaning."
excerpt: "Artin and Deligne-Mumford stacks via atlases, and quotient stacks"

categories: [Math / Stacks]
permalink: /en/math/stacks/algebraic_stacks
sidebar: 
    nav: "stacks-en"

date: 2026-08-31
weight: 3
translated_at: 2026-09-02T08:15:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-09-02T08:15:05+00:00
---
In the previous post, we turned the naive moduli problem we had been considering into a $\Grpd$-valued functor, assigning to each object $T$ the groupoid $\mathcal{X}(T)$ of $T$-families over $T$ and isomorphisms between them. As in [\[Schemes\] §Morphisms of Schemes, ⁋Definition 9](/en/math/scheme_theory/morphism_of_schemes#def9), we will think of these as the collection of $T$-points of $\mathcal{X}$, but there were several problems to resolve first. One of them was that the pullback along a morphism $u: T'\rightarrow T$ is determined only up to unique isomorphism, so in order to actually write down a pullback functor $u^\ast: \mathcal{X}(T)\rightarrow \mathcal{X}(T')$, we needed a choice of a representative for each pullback, namely a cleavage. Because of this, for composable morphisms $T''\overset{v}{\rightarrow}T'\overset{u}{\rightarrow}T$, the two paths of pulling back could differ, and to resolve this we had to remember, as additional data, the canonical isomorphism

$$v^\ast u^\ast x\xrightarrow{\sim}(u\circ v)^\ast x$$

together with the coherence conditions these must satisfy, and the object so obtained was the *pseudofunctor* $\mathcal{X}:\mathcal{C}^\op\rightarrow\Grpd$. ([§Stacks, ⁋Definition 3](/en/math/stacks/fibered_categories_and_stacks#def3)) Conceptually, since these pseudofunctors must be determined by all the $T$-points $\mathcal{X}(T)$ together with the extra data added above, knowing for every $T\in \mathcal{C}$ the groupoid $\mathcal{X}(T)\in \Grpd$ given by the pseudofunctor (and the auxiliary data) means we have captured all the information it is meant to carry, and from this viewpoint we defined a CFG $\mathcal{F}\rightarrow \mathcal{C}$. ([§Stacks, ⁋Definition 5](/en/math/stacks/fibered_categories_and_stacks#def5)) What justifies moving between these two viewpoints is [§Stacks, ⁋Theorem 8](/en/math/stacks/fibered_categories_and_stacks#thm8), where we saw that pseudofunctors and CFGs each form a $2$-category, and indeed that these two $2$-categories are $2$-equivalent.

A stack, then, is an object obtained by equipping the original category $\mathcal{C}$ with a topology to make it a site, and gluing via the descent that this topology defines, more precisely descent in the $2$-categorical sense. That is, to define a stack one needs to uniquely glue morphisms along coverings and to glue compatible local objects, and from this viewpoint a stack could be defined as a $\Grpd$-valued (2-categorical) sheaf on a site. ([§Stacks, ⁋Definition 12](/en/math/stacks/fibered_categories_and_stacks#def12))

From this viewpoint, a morphism $f:\mathcal{X}\rightarrow\mathcal{Y}$ of stacks is a pseudonatural transformation between pseudofunctors. It is the data of a functor $f_T:\mathcal{X}(T)\rightarrow\mathcal{Y}(T)$ for each $T$, and for each $u:T'\rightarrow T$ a natural isomorphism

$$f_{T'}(u^\ast x)\xrightarrow{\sim}u^\ast f_T(x)$$

making it compatible with pullback. A 2-morphism between two stack morphisms is a natural transformation connecting these functors and compatible with the pullback coherences. In the language of CFGs, these are expressed as a functor over the base and a natural transformation, respectively. ([§Stacks, ⁋Definition 7](/en/math/stacks/fibered_categories_and_stacks#def7))

The descent condition for a stack guarantees that local data can be glued into a global object, but it does not provide a local model such as a scheme or an algebraic space. Hence we cannot yet discuss notions like dimension, tangent spaces, or smoothness in the familiar language of algebraic geometry. The goal of this post is to single out, among stacks, the algebraic stacks (those that carry such a geometry).

## Fiber Products of Stacks

The first thing we need in order to discuss the geometry of stacks is the fiber product. Just as we regarded properties of schemes that behave well under base change as good geometric properties, we must define base change for morphisms between stacks as well. The problem is that, unlike $\Sch$ or $\Sch_{/S}$, the category $\Stk$ is a $2$-category, so the fiber product in it must also be defined as a $2$-fiber product.

Let us examine what data is needed for this. Given two stack morphisms $f: \mathcal{X}\rightarrow \mathcal{Z}$ and $g:\mathcal{Y}\rightarrow \mathcal{Z}$, recalling [\[Schemes\] §Functor of Points, ⁋Proposition 7](/en/math/scheme_theory/functor_of_points#prop7), to define the fiber product of stack morphisms it suffices to define, for each $T$, the fiber product

$$\mathcal{X}(T)\times_{\mathcal{Z}(T)}\mathcal{Y}(T).$$

When defining the fiber product of schemes, we took $X(T)\times_{Z(T)}Y(T)$ to consist of those elements satisfying $f_T(x)=g_T(y)$ inside the *set* $Z(T)$, but now that $\mathcal{Z}(T)$ is a groupoid, this condition must be relaxed to an isomorphism. This is exactly the same situation as the one we examined right after [§Stacks, ⁋Proposition 6](/en/math/stacks/fibered_categories_and_stacks#prop6): if we regard a point $x\in \mathcal{X}(T)$ as a functor $x:\ast\rightarrow \mathcal{X}(T)$ between groupoids, then $f_T(x)$ and $g_T(y)$ become two functors

$$f(x),g(y): \ast\rightarrow \mathcal{Z}(T)$$

between groupoids, and a $2$-morphism between these two functors translates into a morphism inside $\mathcal{Z}(T)$, more precisely, since $\mathcal{Z}(T)$ is a groupoid, into an isomorphism $f(x)\rightarrow g(y)$.

In general, when one considers a commuting condition in a $2$-category, one usually works with a $2$-commutative condition. For example, consider the following triangle.

{% diagram Math/Stacks/Algebraic_Stacks-1.svg width="12.05em" alt="2-commutative triangle" %}

Saying that this triangle is $2$-commutative means that, together with the three $1$-morphisms $p,q,r$, an invertible $2$-morphism

$$\alpha:q\circ p\Rightarrow r$$

connecting the composite $q\circ p$ with $r$ has been specified. Thus the data of this diagram is given by $(p,q,r,\alpha)$. Applying this to the present situation, we obtain the following diagram.

{% diagram Math/Stacks/Algebraic_Stacks-2.svg width="14.89em" alt="2-commutative cone over a stack" %}

The $\alpha$ in the middle of the diagram lies between $\mathcal{X}(T)$ and $\mathcal{Y}(T)$ and represents a $2$-morphism connecting the composites $f\circ x,g\circ y:\ast\rightarrow\mathcal{Z}(T)$ given by the two paths. Translating this into the language of morphisms in $\mathcal{Z}(T)$ examined above, we see that the data of this cone is given by a triple

$$(x,y,\alpha),\qquad \alpha:f(x)\xrightarrow{\sim}g(y).$$

In other words, we must explicitly remember the isomorphism from $f(x)$ to $g(y)$. We therefore define as follows.

::: Definition 1
Let $f:\mathcal{X}\rightarrow\mathcal{Z}$ and $g:\mathcal{Y}\rightarrow\mathcal{Z}$ be morphisms of CFGs over a site $\mathcal{C}$. Their *2-fiber product* $\mathcal{X}\times_\mathcal{Z}\mathcal{Y}$ is the following category. Its objects are triples $(x,y,\alpha)$ consisting of $x\in\mathcal{X}(T)$ and $y\in\mathcal{Y}(T)$ for some $T\in\mathcal{C}$, together with an isomorphism

$$\alpha: f(x)\xrightarrow{\ \sim\ }g(y)$$

in $\mathcal{Z}(T)$. A morphism from $(x,y,\alpha)$ over $T$ to $(x',y',\alpha')$ over $T'$ is a pair of morphisms $(a:x\rightarrow x',b:y\rightarrow y')$ lying over the same morphism $h:T\rightarrow T'$, such that in $\mathcal{Z}$ one has

$$\alpha'\circ f(a)=g(b)\circ\alpha.$$

Identity morphisms and composition are defined componentwise.
:::

The projections $(x,y,\alpha)\mapsto T$ and $(a,b)\mapsto h$ define a functor $\mathcal{X}\times_\mathcal{Z}\mathcal{Y}\rightarrow\mathcal{C}$. Choosing cartesian lifts in $\mathcal{X}$ and $\mathcal{Y}$ componentwise, the compatibility condition above forces $\alpha$ to be pulled back along with them, so this projection makes $\mathcal{X}\times_\mathcal{Z}\mathcal{Y}$ a CFG. This CFG comes with the two projection functors $\pr_\mathcal{X}:(x,y,\alpha)\mapsto x$ and $\pr_\mathcal{Y}:(x,y,\alpha)\mapsto y$, and the natural isomorphism $f\circ\pr_\mathcal{X}\cong g\circ\pr_\mathcal{Y}$ given by $\alpha$. In general, for an arbitrary CFG $\mathcal{T}$, giving a morphism $\mathcal{T}\rightarrow\mathcal{X}\times_\mathcal{Z}\mathcal{Y}$ is equivalent to giving morphisms $a:\mathcal{T}\rightarrow\mathcal{X}$, $b:\mathcal{T}\rightarrow\mathcal{Y}$ and a 2-isomorphism $\beta:f\circ a\cong g\circ b$, and this is the 2-categorical universal property of the 2-fiber product.

Since the above definition merely declares the 2-fiber product as a CFG, a separate argument is needed to show that it actually exists within the 2-category of stacks. This is obtained by gluing the descent data of each component.

::: Proposition 2
For stack morphisms $f:\mathcal{X}\rightarrow\mathcal{Z}$ and $g:\mathcal{Y}\rightarrow\mathcal{Z}$ over a site $(\mathcal{C},\tau)$, the 2-fiber product $\mathcal{X}\times_\mathcal{Z}\mathcal{Y}$ is a stack.
:::

From now on we simply call $\mathcal{X}\times_\mathcal{Z}\mathcal{Y}$ the *fiber product* of stacks, and we understand every commutative diagram of stacks as being filled with a $2$-isomorphism.

## Algebraic Spaces

We now endow stacks with algebro-geometric properties, as announced. Or rather, as we have already done for schemes, this can be accomplished by assigning algebro-geometric properties to stack morphisms. Our strategy is to use fiber products, and this is why the first definition of this post was the fiber product of stacks.

Most properties $P$ of scheme morphisms are closed under base change. That is, if any $f:X\rightarrow Y$ has property $P$, then for any scheme $T$ and morphism $T\rightarrow Y$, the base change morphism $f_T:X\times_YT\rightarrow T$ also has it. Conversely, if $f_T$ satisfies property $P$ for *every* scheme $T$ and morphism $T\rightarrow Y$, then taking $T=Y$ and $T\rightarrow Y$ to be $\id_Y$, we see that $f_T=f$ has property $P$.

With this as our idea, we will define properties of a stack morphism $f:\mathcal{X}\rightarrow \mathcal{Y}$ using properties of scheme morphisms and base change. That is, the idea is to declare that $f$ has the *property $P$ of stack morphisms* if, for every scheme $T$ and morphism $T\rightarrow \mathcal{Y}$, the base change $f_T:\mathcal{X}\times_\mathcal{Y}T\rightarrow T$ is a morphism of schemes having the *property $P$ of scheme morphisms*.

The problem is that allowing the source $\mathcal{X}\times_\mathcal{Y}T$ of the base change to be only a scheme makes the scope far too narrow. On the other hand, if we allow arbitrary stacks, then $f_T$ can no longer be controlled in the language of scheme morphisms, so the strategy itself becomes impossible. We therefore require that $\mathcal{X}\times_\mathcal{Y}T$ remain an object only slightly broader than a scheme, to which scheme-theoretic geometry can still be applied, and that object is precisely an *algebraic space*.

::: Definition 3
A sheaf $F:\Sch^\op \rightarrow \Set$ on the site $(\Sch, \et)$ ([§Grothendieck Topologies, ⁋Example 8](/en/math/stacks/grothendieck_topology#ex8)) is an *algebraic space* if it satisfies the following two conditions.

1. (Representability) The diagonal morphism $F \rightarrow F\times F$ is representable by schemes. That is, for any scheme $T$ and morphism $T \rightarrow F\times F$, the fiber product $F\times_{F\times F}T$ is a scheme.
2. (Étale atlas) There exist a scheme $U$ and a representable étale morphism $U \rightarrow F$, and this morphism is an epimorphism of sheaves.
:::

The first condition is almost identical to the idea explained above; with this terminology, our strategy below can be phrased succinctly: we consider only those stack morphisms that are represented by algebraic spaces.

We call the morphism $U\rightarrow F$ in the second condition an *étale atlas* of $F$. Intuitively, this means that the scheme $U$ completely covers $F$, and that $F$ is recovered by quotienting $U$ by the equivalence relation recording these overlaps. To write this more concretely, suppose we are given two schemes $R, U$ and two morphisms $f,g:R\rightarrow U$ between them. If for every scheme $T$,

$$(f,g): R(T)\rightarrow U(T)\times U(T)$$

is injective and its image defines an equivalence relation on $U(T)$, then we call this data $R\rightrightarrows U$ an *equivalence relation* between schemes.

An étale atlas $p: U\rightarrow F$ then gives rise to an equivalence relation in the following way. First, take the product of two copies of $p: U\rightarrow F$ and set $R=U\times_F U$. By the first condition of [Definition 3](#def3), $R$ exists as a scheme. Then, explicitly,

$$(U\times_FU)(T)=\{(x,y)\in U(T)\times U(T)\mid p(x)=p(y)\},$$

so this is the equivalence relation collecting those elements of $U(T)$ regarded as the same under $p$, and through the tautological inclusion $R(T)\hookrightarrow U(T)\times U(T)$ it is actually a subset of $U(T)\times U(T)$, so $R(T)$ gives an equivalence relation between schemes. Thus, intuitively, $U$ provides a scheme chart covering $F$, and $R$ records how the overlaps of this chart must be identified, and from this $F$ is recovered as the sheaf quotient $U/R$. Locally, for any scheme $T$ and point $x\in F(T)$, base-changing $U\rightarrow F$ along $x:T\rightarrow F$ yields an étale surjection $U\times_F T\rightarrow T$, and from this there exists an étale covering $\{T_i\rightarrow T\}$ over which each restriction $x\vert_{T_i}$ can be lifted to a point of $U(T_i)$.

By definition every scheme is an algebraic space, so this is a generalization of schemes, and the two often coincide under assumptions such as quasi-projectivity. Rather than developing this theory in detail, we will merely remember that it is a mild generalization of schemes and return to our original goal.

## Representable Morphisms

Now, to endow a stack morphism $f:\mathcal{X}\rightarrow\mathcal{Y}$ with a property of scheme morphisms, the morphism

$$f_T: \mathcal{X}\times_\mathcal{Y}T\rightarrow T,$$

obtained by base-changing $f$ at an arbitrary scheme-valued point $y: T\rightarrow \mathcal{Y}$ of $\mathcal{Y}$, must appear as a morphism between algebraic spaces as explained above. Requiring that the source $\mathcal{X}\times_\mathcal{Y}T$ of the above expression be an algebraic space for every $y$ is precisely the *representability* of the stack morphism $f$.

An algebraic space is a mild generalization of a scheme, and for the most part one can transfer a property $P$ of scheme morphisms to a property $P$ of algebraic spaces. Now, to lift this property $P$ to stacks, the following two properties are needed.

1. The property $P$ must be closed under arbitrary base change.
2. The property $P$ is fppf-local on the target.

The first condition is automatic, and the second is required because the objects we are interested in are described fppf-locally; from now on, in the general context, by a *stack* we mean a stack over the fppf site ([§Grothendieck Topologies, ⁋Example 8](/en/math/stacks/grothendieck_topology#ex8)) $(\Sch, \fppf)$. Since any scheme $S$ can always be regarded as a stack, it makes sense to say that a stack $\mathcal{X}$ is an $S$-stack, and morphisms between $S$-stacks or the product $\mathcal{X}\times_S \mathcal{Y}$ of two objects over it are well-defined, and one can see that this is, by definition, the same thing as a stack defined over the fppf site $(\Sch_{/S}, \fppf)$.

The necessity of the $\fppf$ site was already foreshadowed to some extent at the level of schemes. For example, in [\[Schemes\] §Group Schemes, ⁋Example 15](/en/math/scheme_theory/group_schemes#ex15), a $\mathbb{G}_m$-torsor was Zariski-locally trivial, but we already remarked in that example that this was a special phenomenon due to Hilbert theorem 90, and indeed the first example given there, the $\mathbb{Z}/2$-torsor $\Spec\mathbb{C}\rightarrow\Spec\mathbb{R}$, was fppf-locally trivial yet not Zariski-locally trivial. For this reason, if we agree that stacks are defined over the $\fppf$ site, then in order to locally trivialize an object of a stack over an fppf covering, check the property of $f_T$, and descend the result to $T$, the property $P$ must be fppf-local on the target.

::: Definition 4
Suppose we are given a property $P$ of morphisms of algebraic spaces satisfying the above condition. We say that a representable stack morphism $f:\mathcal{X}\rightarrow\mathcal{Y}$ *has property $P$* if, for every scheme $T$ and every morphism $y:T\rightarrow\mathcal{Y}$, the base change $f_T:\mathcal{X}\times_\mathcal{Y}T\rightarrow T$ has $P$ as a morphism of algebraic spaces.
:::

The list of properties that $P$ can be is as follows.

> open embedding, closed embedding, quasi-compact, quasi-separated, affine, finite, integral, locally of finite type, finite type, quasi-finite, locally of finite presentation, finite presentation, flat, smooth, unramified, étale, surjective, separated, proper, ...

The important exceptions are projective and quasi-projective. These are closed under base change and are also defined for morphisms of algebraic spaces, but they are not even Zariski-local on the target, so they cannot be lifted to properties of stack morphisms via the fppf descent method above, and must instead be defined separately, for instance through the existence of a relative ample line bundle or an immersion into a projective bundle.

Just as, in the definition of an algebraic space, representability of the diagonal morphism allowed us to treat the locus where two points agree as a scheme, for stacks the diagonal morphism plays the role of treating isomorphisms between two objects geometrically. Base-changing the diagonal morphism $\Delta:X\rightarrow X\times_S X$ of a scheme along two morphisms $a,b:T\rightarrow X$ yields the locus $\Eq(a,b)$ where the two agree. In a stack one remembers isomorphisms instead of equality, so $\rIsom$ appears in its place.

::: Proposition 5
For an $S$-stack $\mathcal{X}$, an $S$-scheme $T$, and two objects $x_1,x_2\in\mathcal{X}(T)$, there is a natural equivalence

$$\mathcal{X}\times_{\mathcal{X}\times_S \mathcal{X}}T\simeq \rIsom_T(x_1,x_2)$$

between the discrete CFG $\rIsom_T(x_1,x_2)$ and the fiber product defined by the diagonal morphism $\Delta: \mathcal{X}\rightarrow\mathcal{X}\times_S\mathcal{X}$. In particular, the following three conditions are equivalent.

1. $\Delta:\mathcal{X}\rightarrow\mathcal{X}\times_S\mathcal{X}$ is representable.
2. For every $S$-scheme $T$ and $x_1,x_2\in\mathcal{X}(T)$, $\rIsom_T(x_1,x_2)$ is an algebraic space.
3. For every $S$-scheme $T$ and $x\in\mathcal{X}(T)$, the morphism $x:T\rightarrow\mathcal{X}$ is representable.
:::
::: Proof
First, applying [Definition 1](#def1), a $T'$-object of $\mathcal{X}\times_{\mathcal{X}\times_S\mathcal{X}}T$ is defined by $S$-morphisms

$$t: T' \rightarrow T, \qquad x: T'\rightarrow \mathcal{X}$$

together with an isomorphism $\alpha: \Delta\circ x\rightarrow (x_1, x_2)\circ t$ in $\mathcal{X}\times_S\mathcal{X}$; since the base scheme of the fiber product is $\mathcal{X}\times_S\mathcal{X}$, $\alpha$ can be written more explicitly in the form $\alpha=(a,b)$ for two isomorphisms

$$a: x\rightarrow x_1\circ t=x_1\vert_{T'}, \qquad b:x\rightarrow x_2\circ t=x_2\vert_{T'}.$$

Now sending this datum $(t,x,a,b)$ to $b\circ a^{-1}:x_1\vert_{T'}\xrightarrow{\sim}x_2\vert_{T'}$ defines a functor

$$\mathcal{X}\times_{\mathcal{X}\times_S \mathcal{X}}T\rightarrow \rIsom_T(x_1,x_2).$$

Our claim is that this functor is a natural equivalence. To verify this, first suppose that two data $(t,x,a,b)$ and $(t',x',a',b')$ of $\mathcal{X}\times_{\mathcal{X}\times_S \mathcal{X}}T$ are sent to the same object of $\rIsom_T(x_1,x_2)$. Since this CFG is discrete, $t=t'$ and

$$b\circ a^{-1}=b'\circ(a')^{-1}.$$

Now consider the isomorphism

$$c=(a')^{-1}\circ a:x\xrightarrow{\sim}x'.$$

Then $a'\circ c=a$, and from the equation above we obtain

$$b'\circ c=b'\circ(a')^{-1}\circ a=b\circ a^{-1}\circ a=b.$$

Therefore $c$, together with $\id_t$, satisfies the compatibility condition of the fiber product, so it defines a morphism from $(t,x,a,b)$ to $(t,x',a',b')$. Conversely, such a morphism must satisfy $a'\circ c=a$, so necessarily $c=(a')^{-1}\circ a$, and hence it is unique. Thus this functor is fully faithful. On the other hand, any $\beta:x_1\vert_{T'}\xrightarrow{\sim}x_2\vert_{T'}$ comes from $(t,x,a,b)=(t,x_1\vert_{T'},\id,\beta)$, so this functor is essentially surjective. Since this construction is compatible with pullback, we obtain the natural equivalence above.

That the first and second conditions are equivalent is now immediate from the natural equivalence constructed above. Next, assuming the first condition, we show the third. For this, assume the first condition and take two morphisms $x:T\rightarrow\mathcal{X}$ and $y:T'\rightarrow\mathcal{X}$ from $S$-schemes. Then in the isomorphism

$$T\times_\mathcal{X}T'\cong(T\times_S T')\times_{\mathcal{X}\times_S\mathcal{X},\Delta}\mathcal{X}$$

the right-hand side is a base change of $\Delta$, hence an algebraic space. Therefore $x:T\rightarrow\mathcal{X}$ is representable and the third condition holds.

Finally, assuming the third condition, we show the second. First, for arbitrary $x_1,x_2\in\mathcal{X}(T)$, since $x_1:T\rightarrow\mathcal{X}$ is representable, $T\times_{x_1,\mathcal{X},x_2}T$ is an algebraic space. In this fiber product, the two morphisms to $T$ may differ from each other, but base-changing along the diagonal morphism $\Delta_T:T\rightarrow T\times_S T$ restricts them to be equal. Hence we obtain a natural isomorphism

$$\rIsom_T(x_1,x_2)\cong(T\times_{x_1,\mathcal{X},x_2}T)\times_{T\times_S T,\Delta_T}T$$

and the right-hand side is a base change of an algebraic space, hence an algebraic space. Therefore the second condition holds.
:::

In the isomorphism sheaf $\rIsom_T(x_1, x_2)$, in the special case $x_1=x_2=x$, the group sheaf $\rAut_T(x)=\rIsom_T(x,x)$ associated to a single object $x\in\mathcal{X}(T)$ is called the *stabilizer* of $x$. Collecting all these stabilizers over $\mathcal{X}$ at once gives the *inertia stack*, defined by the following $2$-fiber product

$$\mathcal{I}_\mathcal{X}:=\mathcal{X}\times_{\mathcal{X}\times_S\mathcal{X}}\mathcal{X}.$$

In other words, a $T$-object of the inertia stack is a pair $(x,\alpha)$ with $x\in\mathcal{X}(T)$ and $\alpha\in\rAut_T(x)$, and the fiber of the projection $\mathcal{I}_\mathcal{X}\rightarrow\mathcal{X}$ over $x$ is exactly $\rAut_T(x)$.

## Algebraic Stacks and Deligne–Mumford Stacks

In [Definition 3](#def3), we defined an algebraic space as a sheaf on $(\Sch, \et)$ whose diagonal is representable by schemes and which admits an étale surjective atlas $U\rightarrow F$ from a scheme. Raising this definition one level, consider a groupoid-valued stack $\mathcal{X}$ on the fppf site; as announced, requiring the diagonal to be representable by algebraic spaces instead of schemes gives the definition of a *Deligne–Mumford stack*.

::: Definition 6
A stack $\mathcal{X}$ on the site $(\Sch_{/S}, \fppf)$ (over a base scheme $S$) is a *Deligne–Mumford stack* (or simply a *DM stack*) if it satisfies the following two conditions.

1. (Representability) The diagonal morphism $\Delta:\mathcal{X} \rightarrow \mathcal{X}\times_S \mathcal{X}$ is representable by algebraic spaces.
2. (Étale atlas) There exist a scheme $U$ and a representable étale morphism $\pi: U \rightarrow \mathcal{X}$, and this morphism is an epimorphism of sheaves (i.e. surjective). This $\pi$ is called an *atlas* (or *presentation*) of $\mathcal{X}$.

More generally, a stack obtained by allowing smooth morphisms instead of étale morphisms in condition 2 is called an *algebraic stack* or an *Artin stack*. ([\[Schemes\] §Smooth and Étale Morphisms, ⁋Definition 11](/en/math/scheme_theory/smooth_and_etale_morphisms#def11))
:::

An atlas, just as for algebraic spaces, is a way of covering the stack $\mathcal{X}$ by a scheme $U$. Since a DM stack uses an étale atlas, its geometric fibers are discrete and the relative dimension is $0$. An Artin stack allows smooth atlases, covering $\mathcal{X}$ by thicker schemes in the sense that the smooth fibers may have positive dimension.

If the atlas $\pi:U\rightarrow\mathcal{X}$ of a stack has relative dimension $d$, we define $\dim\mathcal{X}=\dim U-d$, and this does not depend on the choice of atlas. For a DM stack, $d=0$ and the stabilizers are unramified, so there are no infinitesimal directions of automorphisms. For an Artin stack, $d>0$ is possible, and the positive dimension of the atlas fibers may also include automorphism directions contributed by the positive-dimensional stabilizers of each point. In this sense, DM stacks allow points to be folded together only by discrete stabilizers, while Artin stacks also allow folding along positive-dimensional automorphism families.

Strictly speaking, for an algebraic stack $\mathcal{X}$, the following three conditions are equivalent.

1. $\mathcal{X}$ is a DM stack.
2. The diagonal morphism $\Delta:\mathcal{X} \rightarrow \mathcal{X}\times_S \mathcal{X}$ is unramified. ([\[Schemes\] §Smooth and Étale Morphisms, ⁋Definition 9](/en/math/scheme_theory/smooth_and_etale_morphisms#def9))
3. For every geometric point $x:\Spec\mathbb{K}\rightarrow\mathcal{X}$, the stabilizer $\rAut_\mathbb{K}(x)$ is unramified over $\mathbb{K}$.

In the usual finite-type, quasi-separated situation, these stabilizers are of finite type and quasi-compact, so under the DM condition they become finite étale group schemes. In particular, in characteristic $0$, every finite group scheme is étale, so the DM condition follows from the condition of having finite stabilizers alone.

## Quotient Stacks

In [Definition 6](#def6) of the previous section, we defined DM stacks and emphasized what they have in common with algebraic spaces, but we have not yet sufficiently addressed the crucial difference that actually makes them stacks, namely the fact that they are $\Grpd$-valued functors. This difference is most clearly visible in the étale atlas. By definition, an atlas of an algebraic space or a DM stack is a surjective morphism from a scheme $U$ to the object in question. Then, if we treat the points of $U$ identified by this morphism as the same and consider the quotient of $U$, we should recover that algebraic space or DM stack.

The difference lies in this part of *treating as the same*. For an algebraic space, a $\Set$-valued functor, two points being equal really is equality; but for a DM stack, a $\Grpd$-valued functor, one even remembers the isomorphisms connecting two points. To write this more explicitly, we already saw, right after [Definition 3](#def3), that for an algebraic space, $R$ defined by

$$R(T)=(U\times_FU)(T)=\{(f,g)\in U(T)\times_{S(T)}U(T)\mid p\circ f=p\circ g\}$$

is a scheme, and that there is an *inclusion* into $U(T)\times_{S(T)}U(T)$. On the other hand, the set defined by an atlas $p:U\rightarrow\mathcal{X}$ of a DM stack,

$$R(T)=(U\times_\mathcal{X}U)(T)=U(T)\times_{\mathcal{X}(T)}U(T)=\{(f,g,\alpha)\mid \alpha: p\circ f\overset{\sim}{\rightarrow} p\circ g\}$$

admits a map to $U(T)\times_{S(T)}U(T)$ in the same way, but this map need not be injective. Indeed, the triple $(f,g,\alpha)$ is sent to the pair $(f,g)$, and the fiber over $(f,g)$ is the set of isomorphisms $\rIsom_{\mathcal{X}(T)}(p\circ f,p\circ g)$. In particular, when $f=g$, this fiber is the stabilizer $\rAut_T(p\circ f)$, so intuitively a DM stack can be thought of as a space with a stabilizer attached to each point as separate information.

::: Definition 7
The fiber of the *quotient stack* $[U/G]$ over $T\in\Sch_{/S}$ is the following groupoid. Its objects are pairs $(P,\varphi)$ satisfying the following two conditions.

1. $P\rightarrow T$ is a $G$-torsor ([§Stacks, ⁋Definition 17](/en/math/stacks/fibered_categories_and_stacks#def17)), and
2. $\varphi:P\rightarrow U$ is a $G$-equivariant morphism; that is, $\varphi(g\cdot p)=g\cdot\varphi(p)$ holds.

A morphism from $(P,\varphi)$ to $(P',\varphi')$ is a $G$-torsor morphism $\psi:P\rightarrow P'$ with $\varphi'\circ\psi=\varphi$.
:::

Then any $\psi$ satisfying the above condition is automatically an isomorphism, since a $G$-equivariant morphism of $G$-torsors is essentially nothing but a translation. In particular, each fiber is a groupoid. Moreover, pulling back torsors and equivariant morphisms along base change provides cartesian morphisms, so these fiber groupoids form a CFG over $\Sch_{/S}$. As a special case, when $G$ acts on the base space $U=S$ with the trivial action, $[S/G]$ becomes the classifying stack $\bB G$ we already saw in [§Stacks, ⁋Definition 17](/en/math/stacks/fibered_categories_and_stacks#def17).

Intuitively, a $T$-point $(P,\varphi)$ of $[U/G]$ amounts to giving a section of the space $P\times^G U\rightarrow T$ over $T$, whose fibers are $U$, twisted by a $G$-torsor $P$. ([\[Algebraic Topology\] §Classifying Spaces, ⁋Definition 3](/en/math/algebraic_topology/classifying_spaces#def3)) If the torsor is trivial so that $P=G\times_ST$, then $\varphi(g,t)=g\cdot\varphi(e,t)$, so $\varphi$ is uniquely determined by its value $a=\varphi\circ e:T\rightarrow U$ at the identity section $e:T\rightarrow G\times_ST$; thus restricting to the trivial torsor recovers exactly the same information as a point of $U(T)$.

On the other hand, just as in the descent argument applied to $\bB\mathbb{G}_m$ in [§Stacks, ⁋Theorem 18](/en/math/stacks/fibered_categories_and_stacks#thm18), torsors and equivariant morphisms satisfy effective descent for fppf coverings, and the componentwise descent argument of [Proposition 2](#prop2) applies verbatim, so $[U/G]$ is a stack. Now, to show that this stack is an algebraic stack, we construct an atlas.

::: Proposition 8
Let an $S$-scheme $U$ and a group $S$-scheme $G$ acting on it be given. For every $S$-scheme $T$ and every $T$-point $u\in U(T)$ of $U$, the assignment

$$\pi(u)=\bigl(G\times_S T,\varphi_u\bigr),\qquad \varphi_u(g,t)=g\cdot u(t),$$

sending $u$ to the trivial torsor together with the equivariant morphism it defines, is a stack morphism and an epimorphism.
:::
::: Proof
The functoriality of $\pi$ follows since base change of $u$ is compatible with base change of the trivial torsor. Now, to show that this is an epimorphism, we must show that every $(P,\varphi)\in [U/G](T)$ arises locally in this way; since every $G$-torsor is fppf-locally trivial ([§Stacks, ⁋Definition 17](/en/math/stacks/fibered_categories_and_stacks#def17)), we can take a trivializing fppf covering $\{T_i\rightarrow T\}$ and sections $s_i\in P(T_i)$ over each $T_i$. Then the restriction $(P,\varphi)\vert_{T_i}$ of $(P,\varphi)$ to $T_i$ is isomorphic to the $\pi(u_i)$ determined by $u_i=\varphi(s_i)\in U(T_i)$, and therefore $\pi$ is an epimorphism.
:::

The $\pi$ of [Proposition 8](#prop8) is a morphism that attaches the trivial torsor to a point of $U$ and sends it to the quotient by the $G$-action. It is therefore the quotient map itself considered above, and being an epimorphism, it is a natural candidate for an atlas. What remains is to show that $\pi$ is representable and smooth. First, computing the base change along $\pi$ itself reveals once again the action groupoid that records how identifications are made in the quotient.

::: Proposition 9
For the morphism $\pi:U\rightarrow[U/G]$ of [Proposition 8](#prop8), the following diagram

{% diagram Math/Stacks/Algebraic_Stacks-3.svg width="10.10em" alt="base change of an atlas" %}

is a 2-fiber product diagram.
:::
::: Proof
That is, it suffices to show that the canonical isomorphism

$$U\times_{[U/G]}U\cong G\times_SU$$

exists such that the two projections $\pr_1,\pr_2:U\times_{[U/G]}U\rightarrow U$ correspond to the group action $\rho:(g,u)\mapsto g\cdot u$ and the projection $(g,u)\mapsto u$, respectively.

This can be written out explicitly. First, an object of $(U\times_{[U/G]}U)(T)$ is given by

$$(u_1,u_2,\psi),\qquad u_1,u_2\in U(T),\quad \psi:\pi(u_1)\xrightarrow{\sim}\pi(u_2).$$

On the other hand, from the definition of $\pi$ in [Proposition 8](#prop8),

$$\pi(u_1)=(G\times_ST,\varphi_{u_1}), \qquad \pi(u_2)=(G\times_ST,\varphi_{u_2}),$$

and since $\psi$ in this correspondence was a $2$-isomorphism in the original data, we have $\varphi_{u_2}\circ\psi=\varphi_{u_1}$. In other words, $\psi$ induces $G$-equivariant automorphisms between the $G$-torsors. Conversely, given any $g\in G$, the translation it defines is a $G$-equivariant automorphism, so the above process can be reversed.

We must now show the $2$-commutativity of the given diagram. For $(g,u)\in(G\times_SU)(T)$, the two paths give $\pi(\rho(g,u))=\pi(g\cdot u)$ and $\pi(\pr_2(g,u))=\pi(u)$, and by [Definition 7](#def7), a morphism between them is a $G$-equivariant automorphism $\psi$ of the trivial torsor $G\times_ST$ satisfying $\varphi_u\circ\psi=\varphi_{g\cdot u}$. For the right translation $\psi_g:(h,t)\mapsto(hg,t)$ defined by $g$, we have

$$\varphi_u(\psi_g(h,t))=(hg)\cdot u(t)=h\cdot\bigl(g\cdot u(t)\bigr)=\varphi_{g\cdot u}(h,t),$$

so $\psi_g$ provides such a morphism. This correspondence is natural in $(g,u)$ and compatible with base change, hence it defines a $2$-isomorphism $\alpha:\pi\circ\rho\Rightarrow\pi\circ\pr_2$, and therefore the given diagram is $2$-commutative. Then by the universal property of the $2$-fiber product discussed right after [Definition 1](#def1), this data $(\rho,\pr_2,\alpha)$ induces a morphism

$$\Phi:G\times_SU\rightarrow U\times_{[U/G]}U,\qquad \Phi(g,u)=(g\cdot u,u,\psi_g),$$

so it remains to show that $\Phi$ is an isomorphism.

Since $U$ is $\Set$-valued, a pair $(a,b)$ forming a morphism between two objects $(u_1,u_2,\psi)$ and $(u_1',u_2',\psi')$ over $T$ as in [Definition 1](#def1) must consist of identity morphisms, so $u_1=u_1'$ and $u_2=u_2'$, and the condition $\psi'\circ\pi(a)=\pi(b)\circ\psi$ forces $\psi=\psi'$. Thus $(U\times_{[U/G]}U)(T)$ is a discrete groupoid, and so showing that $\Phi$ is an isomorphism is equivalent to showing that the object correspondence $\Phi_T$ is a bijection for each $T$.

Injectivity of $\Phi_T$ follows because the second component of $\Phi_T(g,u)$ recovers $u$, and the value of the third component at $(e,t)$ recovers $g$. For surjectivity, suppose an arbitrary object $(u_1,u_2,\psi)$ is given. Since $\psi$ is a morphism over $T$, it uniquely determines an element $\gamma\in G(T)$ such that $\psi(e,t)=(\gamma(t),t)$, and by the $G$-equivariance of $\psi$,

$$\psi(h,t)=h\cdot\psi(e,t)=(h\gamma(t),t),$$

so $\psi=\psi_\gamma$. In other words, the $G$-equivariant automorphisms of the trivial torsor are exactly the right translations. ([§Stacks, ⁋Definition 17](/en/math/stacks/fibered_categories_and_stacks#def17)) The remaining condition $\varphi_{u_2}\circ\psi_\gamma=\varphi_{u_1}$ requires

$$h\cdot\bigl(\gamma(t)\cdot u_2(t)\bigr)=\varphi_{u_2}(h\gamma(t),t)=\varphi_{u_1}(h,t)=h\cdot u_1(t)$$

for all $(h,t)$; substituting $h=e$ shows this is equivalent to $u_1=\gamma\cdot u_2$, and conversely if $u_1=\gamma\cdot u_2$, then the equality holds for all $(h,t)$. Hence $(u_1,u_2,\psi)=\Phi_T(\gamma,u_2)$.

All of these correspondences are compatible with base change, so $\Phi_T$ is functorial in $T$, and therefore $\Phi$ is an isomorphism. By construction $\pr_1\circ\Phi=\rho$ and $\pr_2\circ\Phi=\pr_2$, so under this isomorphism $\pr_1$ corresponds to the action $\rho:(g,u)\mapsto g\cdot u$ and $\pr_2$ to the projection $(g,u)\mapsto u$.
:::

[Proposition 9](#prop9) can be summarized by saying that $[U/G]$ is the stack quotient of the *action groupoid* $G\times_SU\rightrightarrows U$. More generally, from a groupoid object $R\rightrightarrows U$ with smooth source and target, one obtains an algebraic stack $[U/R]$; the quotient stack is the special case where $R=G\times_SU$.

We will now show that, under suitable conditions, the quotient stack thus defined is a DM stack, as suggested by the intuition from the beginning of this section.

::: Theorem 10
Let $U$ be an $S$-scheme with an action by a smooth group $S$-scheme $G$. Then the quotient stack $[U/G]$ is an algebraic stack, and the morphism $\pi:U\rightarrow[U/G]$ from [Proposition 8](#prop8) is a smooth atlas. Moreover, base changing the diagonal $\Delta:[U/G]\rightarrow[U/G]\times_S[U/G]$ along $\pi\times\pi$ yields the action morphism

$$a=(\rho,\pr_2):G\times_SU\rightarrow U\times_SU,\qquad (g,u)\mapsto(g\cdot u,u).$$

It follows that:

1. If $G$ is separated over $S$, then $\Delta$ is separated. Moreover, $[U/G]$ is separated (that is, $\Delta$ is proper) if and only if $a$ is proper.
2. If the stabilizers of all geometric points are unramified, then $[U/G]$ is a DM stack. In particular, if $G$ is étale over $S$, then $\pi$ itself is an étale atlas.
:::
::: Proof
First, we prove the claims common to both statements. To show $[U/G]$ is an algebraic stack, we must verify representability of the diagonal and existence of a smooth atlas ([Definition 6](#def6)).

First we show the diagonal is representable. By [Proposition 5](#prop5), it suffices to show that for any $S$-scheme $T$ and $(P,\varphi),(P',\varphi')\in[U/G](T)$, $\rIsom_T((P,\varphi),(P',\varphi'))$ is an algebraic space. Taking an fppf covering $\{T_i\rightarrow T\}$ trivializing both objects, as in the proof of [Proposition 8](#prop8), the two objects over each $T_i$ have the form $\pi(u_i),\pi(u_i')$, and by the computation in [Proposition 9](#prop9), for any $V\rightarrow T_i$,

$$\rIsom_{T_i}(\pi(u_i),\pi(u_i'))(V)=\{g\in G(V)\mid g\cdot u_i'\vert_V=u_i\vert_V\}$$

is representable by the fiber product of the morphism $(g\mapsto(g\cdot u_i',u_i)):G_{T_i}\rightarrow U\times_SU$ and the diagonal $\Delta_{U/S}:U\rightarrow U\times_SU$. These local presentations glue via the descent data to form an algebraic space.

Now we show $\pi$ is a smooth atlas. If $T\rightarrow[U/G]$ is given by an object $(P,\varphi)$, then via the canonical isomorphism $U\times_{[U/G]}T\cong P$, every base change of $\pi$ is a $G$-torsor $P\rightarrow T$. Since a torsor is fppf-locally $G\times_ST$, it is an algebraic space, and since $G$ is smooth, $P\rightarrow T$ is smooth as well. As $\pi$ is an epimorphism by [Proposition 8](#prop8), $\pi$ is a smooth atlas, and hence $[U/G]$ is an algebraic stack.

For the common claims, it remains to compute the base change of the diagonal. Applying [Proposition 5](#prop5) to $T=U\times_SU$ with the two objects $\pi\circ\pr_1$ and $\pi\circ\pr_2$, the base change of $\Delta$ along $\pi\times\pi$ is $U\times_{[U/G]}U$, which by [Proposition 9](#prop9) is $G\times_SU$, and the morphism to $U\times_SU$ is $(\rho,\pr_2)=a$. Since $\pi$ is a smooth epimorphism, so is $\pi\times\pi$; separated, proper, and unramified are all stable under base change and fppf-local on the target ([Definition 4](#def4)), so $\Delta$ has each of these properties if and only if $a$ does.

Now for the individual claims.

1. Since $\pr_2\circ a=\pr_2$ and $\pr_2:G\times_SU\rightarrow U$ is the base change of $G\rightarrow S$, if $G$ is separated then this composition is separated. If a composite $X\rightarrow Y\rightarrow Z$ is separated, then so is $X\rightarrow Y$, so $a$ is separated and hence so is $\Delta$. A stack being separated means $\Delta$ is proper, which by the above criterion is equivalent to $a$ being proper.

2. By the equivalent condition discussed right after [Definition 6](#def6), $[U/G]$ being a DM stack is equivalent to $\Delta$ being unramified, which by the above criterion is equivalent to $a$ being unramified. The fiber of $a$ over a geometric point $(u_1,u_2)\in(U\times_SU)(\mathbb{K})$ is

    $$\{g\in G_\mathbb{K}\mid g\cdot u_2=u_1\},$$

    so it is empty if the two points lie in different orbits, and otherwise a torsor under the stabilizer $\rAut_\mathbb{K}(u_2)$. Since $\pr_2\circ a=\pr_2$ is smooth, it is locally of finite type, and if a composite is locally of finite type, so is the first morphism, hence $a$ is locally of finite type. Now, unramifiedness of a locally finite type morphism amounts to the vanishing of its cotangent sheaf, and by [\[Schemes\] §Kähler Differentials and Cotangent Sheaves, ⁋Proposition 5](/en/math/scheme_theory/sheaf_of_differentials#prop5) the cotangent sheaf commutes with base change, so the restriction of $\Omega_a$ to a fiber is the cotangent sheaf of that fiber. Since $\Omega_a$ is of finite type, [\[Commutative Algebra\] §Integral Extensions, ⁋Lemma 8](/en/math/commutative_algebra/integral_extension#lem8) shows that vanishing at each point implies vanishing of the stalks; therefore, if all stabilizers are unramified, then $a$ is unramified. Finally, if $G$ is étale, then the base change $P\rightarrow T$ seen above is étale, so $\pi$ itself is an étale atlas as required by [Definition 6](#def6).
:::

This completes the program introduced at the beginning of this section: under suitable finiteness conditions, a quotient stack is a DM stack. Conversely, it is known that every DM stack is locally a quotient stack. More precisely, for a finite-type point $x$ of a quasi-separated DM stack $\mathcal{X}$ with geometric stabilizer $G_x$, one can find an affine scheme $\Spec A$ on which $G_x$ acts and a stabilizer-preserving étale morphism $[\Spec A/G_x]\rightarrow\mathcal{X}$. The proof of this fact lies beyond the scope of this post, but since it greatly supports our geometric motivation, we record it here without proof.

Now let us apply [Theorem 10](#thm10) to the case $U=S$ from [Definition 7](#def7), i.e. the classifying stack, to read off the atlas and stabilizers directly.

::: Example 11 ($\bB\mathbb{G}_m$ and $\bB(\mathbb{Z}/n)$)
Fix a field $\mathbb{K}$ as the base scheme.

1. $\bB\mathbb{G}_m=[\Spec\mathbb{K}/\mathbb{G}_m]$ is an algebraic stack. Since $\mathbb{G}_m$ is affine and smooth ([\[Schemes\] §Group Schemes, §§Group Schemes](/en/math/scheme_theory/group_schemes#group-schemes)), [Theorem 10](#thm10) applies; the atlas is $\Spec\mathbb{K}\rightarrow\bB\mathbb{G}_m$, and its base change is $\mathbb{G}_m\rightrightarrows\Spec\mathbb{K}$. The groupoid $\bB\mathbb{G}_m(T)$ is the groupoid of line bundles on $T$ ([§Stacks, ⁋Theorem 18](/en/math/stacks/fibered_categories_and_stacks#thm18)), and the stabilizer of a point is $\mathbb{G}_m$. Since the stabilizer is $1$-dimensional, $\bB\mathbb{G}_m$ is not a DM stack but an Artin stack, of dimension $\dim\Spec\mathbb{K}-\dim\mathbb{G}_m=0-1=-1$.

2. Viewing $\mathbb{Z}/n$ as a constant group scheme, $\bB(\mathbb{Z}/n)=[\Spec\mathbb{K}/(\mathbb{Z}/n)]$ is a DM stack. The constant group scheme $\mathbb{Z}/n$ is the disjoint union $\coprod_{i=1}^n\Spec\mathbb{K}$, hence finite étale. Thus the atlas $\Spec\mathbb{K}\rightarrow\bB(\mathbb{Z}/n)$ is an étale epimorphism, with base change $\mathbb{Z}/n\times\Spec\mathbb{K}\rightrightarrows\Spec\mathbb{K}$. The groupoid $\bB(\mathbb{Z}/n)(T)$ is the groupoid of $\mathbb{Z}/n$-torsors over $T$, i.e. finite étale coverings on whose fibers $\mathbb{Z}/n$ acts simply transitively, and the stabilizer of the trivial torsor is $\mathbb{Z}/n$.
:::

In the above examples the scheme being acted on is a single point, which makes the computation transparent. The next is a standard action whose stabilizer varies from point to point.

::: Example 12 ($[\mathbb{A}^1/\mathbb{G}_m]$)
Over an algebraically closed field $\mathbb{K}$, let $\mathbb{G}_m$ act on the affine line $\mathbb{A}^1$ by scalar multiplication $t\cdot x=tx$. The origin $\{0\}$ is a fixed point, and its complement $\mathbb{A}^1\setminus\{0\}=\mathbb{G}_m$ is an open orbit on which $\mathbb{G}_m$ acts simply transitively. The quotient stack $[\mathbb{A}^1/\mathbb{G}_m]$ remembers the distinct stabilizers of these two orbits.

1. The action over the open orbit $\mathbb{G}_m\hookrightarrow\mathbb{A}^1$ is free, so $[\mathbb{G}_m/\mathbb{G}_m]\cong\Spec\mathbb{K}$, an open point with trivial stabilizer.

2. The origin $\{0\}=\Spec\mathbb{K}$ is a fixed point on which $\mathbb{G}_m$ acts trivially, so $[\{0\}/\mathbb{G}_m]=\bB\mathbb{G}_m$, a closed point with stabilizer $\mathbb{G}_m$. ([Example 11](#ex11))

$[\mathbb{A}^1/\mathbb{G}_m]$ has dimension $1-1=0$, but the closed point carries the positive-dimensional stabilizer $\mathbb{G}_m$. Thus it is an Artin stack, not a DM stack, preserving automorphism information that no scheme or algebraic space could retain.
:::

---

**References**

**[FGA]** B. Fantechi, L. Göttsche, L. Illusie, S. Kleiman, N. Nitsure, A. Vistoli, *Fundamental algebraic geometry: Grothendieck's FGA explained*. Mathematical Surveys and Monographs, American Mathematical Society, 2005.  
**[Stacks]** The Stacks Project Authors, *The Stacks Project*. Available [online](https://stacks.math.columbia.edu/).
