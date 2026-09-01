---
title: "Stacks"
description: "Motivated by the fact that moduli problems take values in groupoids rather than sets, this post defines fibered categories and fibrations in groupoids over a base, and introduces stacks over a site, where descent holds, as a generalization of faithfully flat descent."
excerpt: "Groupoids, categories fibered in groupoids, descent, and the definition of a stack"

categories: [Math / Stacks]
permalink: /en/math/stacks/fibered_categories_and_stacks
sidebar: 
    nav: "stacks-en"

date: 2026-08-30
weight: 2
translated_at: 2026-09-01T19:15:05+00:00
translation_source: kimi-cli
---
The stacks we will deal with essentially come from moduli problems, and a representative example of such problems is the problem of classifying principal $G$-bundles over a topological space $X$, or vector bundles of rank $r$, which we saw in [\[Algebraic Topology\] §Classifying Spaces, ⁋Theorem 8](/en/math/algebraic_topology/classifying_spaces#thm8). The nicest fact we obtain from the functor of points perspective introduced in [\[Schemes\] §Functors of Points](/en/math/scheme_theory/functor_of_points) is that in the algebro-geometric form of this problem, we can regard a correspondence of this kind

$$F:\Sch^\op\rightarrow \Set;\qquad T\mapsto \{\text{principal $G$-bundles over $T$}\}$$

as a functor in its own right and then ask whether this functor is actually represented by a scheme. However, this formula itself is not a well-defined functor, the essential reason being that to establish the functoriality of this correspondence, one must transport a bundle over $X$ to one over $Y$ using the pullback $f^\ast P$ of a bundle along a morphism $f:Y\rightarrow X$, yet the pullback bundle itself is by nature only determined up to unique isomorphism.

The way topology resolves this was simple. Instead of the naive correspondence above, everything is settled in $\hTop$. That is, one considers the correspondence

$$X\mapsto \{\text{principal $G$-bundles over $X$}\}/{\cong}$$

The important result of that theory is then that there exists a universal bundle $\E G\rightarrow\B G$ over the classifying space $\B G$ of $G$, and that the correspondence pulling it back gives a bijection

$$[X,\B G]\xrightarrow{\sim}\{\text{principal $G$-bundles over $X$}\}/{\cong};\qquad [f]\mapsto[f^\ast\E G]$$

What makes this work is the condition that $\E G$ is contractible: if the pullbacks along two classifying maps are isomorphic, then the two $G$-equivariant maps from that bundle to $\E G$ are homotopic, and hence the two classifying maps are homotopic as well. In other words, this classification theorem is the statement that the two sets obtained after killing bundle isomorphisms and homotopies between morphisms as equivalence relations are equal.

The problem is that the language of algebraic geometry is more rigid than that of topology, and cannot accommodate homotopy in this way. The solution is to not kill the isomorphisms but to keep all of them alive; as a result, the moduli functor $F$ is now not $\Set$-valued but $\Grpd$-valued.

## Groupoids

First, let us recall the following definition.

::: Definition 1
A category $\mathcal{G}$ is a *groupoid* if every morphism of $\mathcal{G}$ is an isomorphism. ([\[Category Theory\] §Category, ⁋Definition 11](/en/math/category_theory/categories#def11))
:::

In [\[Category Theory\] §Category, ⁋Definition 10](/en/math/category_theory/categories#def10), we defined a group as a category with a single object in which every morphism is an isomorphism. Thus, for an object $x\in \mathcal{G}$ of a groupoid $\mathcal{G}$, $\Aut_\mathcal{G}(x)=\Hom_\mathcal{G}(x, x)$ forms a group under composition, which we call the *automorphism group* of $x$. We write $\Grpd$ for the category whose objects are groupoids and whose morphisms are functors between them.

In this way a groupoid can be viewed as a generalization of a group, but that is not the whole story. The point of view useful to us is that it can also be seen as a generalization of a set, since any set can be regarded as a category whose only morphisms are identities. A groupoid $\mathcal{G}$ then has several objects just like a set, but it also carries an isomorphism structure between them.

In the example from the introduction, the collection of all principal $G$-bundles over a fixed space $X$ corresponds to a groupoid structure. Choosing one representative from each isomorphism class then amounts to choosing a skeleton $\sk\mathcal{G}$ of the groupoid $\mathcal{G}$. That is, $\sk \mathcal{G}$ coincides with the collection of isomorphism classes of $\mathcal{G}$. Meanwhile, since a skeleton is a full subcategory, it faithfully retains the automorphism group $\Aut_\mathcal{G}(x)$ of each representative $x$; once we forget even the information of these automorphisms, what we obtain is a discrete groupoid, that is, a set.

::: Example 2
The following are examples of groupoids that we will examine in detail.

1. For a fixed scheme $T$, the category whose objects are line bundles over $T$ and whose morphisms are isomorphisms of $\mathcal{O}_T$-modules between line bundles is a groupoid, and the automorphism group of each object $\mathcal{L}$ is $\Aut(\mathcal{L})=\Gamma(T, \mathcal{O}_T)^\ast=\mathbb{G}_m(T)$. If we then extract the set of isomorphism classes of this groupoid in the manner above, it is exactly the Picard group $\Pic(T)$, and this amounts to forgetting the information of the automorphism group $\mathbb{G}_m(T)$.
2. Another familiar example is the *fundamental groupoid* $\Pi_1(X)$ of a topological space $X$. ([\[Algebraic Topology\] §Homotopy, ⁋Definition 11](/en/math/algebraic_topology/homotopy#def11)) This is the category whose objects are points and whose morphisms are homotopy classes of paths, and the automorphism group at a point is exactly the fundamental group $\pi_1(X,x)$.
3. As a trivial example in the flow of our story, any functor $F:\mathcal{C}^\op \rightarrow \Set$ is the special case assigning to each $T$ the discrete groupoid $F(T)$. That is, $\Set$-valued functors are a special case of $\Grpd$-valued functors.
:::

In particular, the first example is the object we will mainly study. In general, $\Pic(T)$ may contain a nontrivial line bundle $\mathcal{L}$, but by the definition of a line bundle, $\mathcal{L}$ is locally trivial. As we saw in [\[Schemes\] §Faithfully Flat Descent, ⁋Theorem 11](/en/math/scheme_theory/faithfully_flat_descent#thm11), if one gives local trivial line bundles over a covering together with isomorphisms gluing them over the overlaps as a descent datum, effective descent yields a single global line bundle. The transition data for gluing the $\mathbb{G}_m$-torsors of [\[Schemes\] §Group Schemes, ⁋Example 15](/en/math/scheme_theory/group_schemes#ex15) are exactly these isomorphisms. Therefore, to distinguish line bundles that all look locally trivial, we must record these isomorphisms without forgetting them.

## Pseudofunctors

Meanwhile, if we think of the moduli functor $F$ of principal $G$-bundles considered in the introduction, the intuitive reason its output sets had to be quotiented by isomorphism classes was the pullback. This is not something resolved merely by upgrading the target of the functor to $\Grpd$-valued. Therefore, to obtain the functoriality of $F$ in the strict sense, we must well-define the pullback

$$f^\ast=F(f): F(V)\rightarrow F(U)$$

that gives this functoriality; in other words, whenever a morphism $f: U\rightarrow V$ and an object over $V$ are given, we must make a *choice* that consistently picks out a pullback representation. And, however such choices are made, the pullback along a composite of two morphisms

$$U\overset{f}{\longrightarrow}V\overset{g}{\longrightarrow}W$$

is now *no longer* equal to the composite of the two pullbacks, and must only satisfy the condition that there exists an isomorphism

$$\varepsilon_{f, g}: f^\ast g^\ast P \xRightarrow{\sim} (g\circ f)^\ast P$$

between the two. The idea of a pseudofunctor is to take all of these as data and to require that they define consistent data.

::: Definition 3
A *pseudofunctor* $F:\mathcal{C}^\op \rightarrow \Grpd$ over a category $\mathcal{C}$ consists of the following data.

1. A groupoid $F(U)$ associated to each object $U\in \mathcal{C}$,
2. A functor $f^\ast: F(V) \rightarrow F(U)$ associated to each morphism $f: U \rightarrow V$,
3. For each composable pair $U\overset{f}{\longrightarrow}V\overset{g}{\longrightarrow}W$, a natural isomorphism

    $$\varepsilon_{f, g}: f^\ast\circ g^\ast \xRightarrow{\sim} (g\circ f)^\ast,$$

    and for each object $U$, a natural isomorphism

    $$\eta_U:\id_{F(U)}\xRightarrow{\sim}(\id_U)^\ast.$$

The compatibility conditions these must satisfy are as follows.

> For three morphisms $U\overset{f}{\longrightarrow}V\overset{g}{\longrightarrow}W\overset{h}{\longrightarrow}Z$,
>
> $$\varepsilon_{f, h\circ g}\circ(\id_{f^\ast}\ast \varepsilon_{g, h})=\varepsilon_{g\circ f, h}\circ(\varepsilon_{f, g}\ast \id_{h^\ast})$$
>
> holds, and for any morphism $f: U\rightarrow V$,
>
> $$\varepsilon_{f, \id_V}\circ(\id_{f^\ast}\ast \eta_V)=\id_{f^\ast},\qquad \varepsilon_{\id_U, f}\circ(\eta_U\ast \id_{f^\ast})=\id_{f^\ast}$$
>
> hold.
:::

The data and conditions of Definition 3 can be visualized in diagrams as follows. First, the natural isomorphisms $\varepsilon_{f,g}$ and $\eta_U$ in item 3 appear as 2-morphisms between the two paths shown in the following diagram, respectively.

{% diagram Math/Stacks/Fibered_Categories_and_Stacks-1.svg width="29.13em" alt="Composition isomorphisms and identity isomorphisms" %}

The $\ast$ appearing in the compatibility conditions is the horizontal composition of $2$-morphisms; for example, the first equation asserts that the following diagram

{% diagram Math/Stacks/Fibered_Categories_and_Stacks-2.svg width="17.76em" alt="Associativity coherence" %}

commutes, and the second equation asserts that the following diagrams

{% diagram Math/Stacks/Fibered_Categories_and_Stacks-3.svg width="25.28em" alt="Unit coherence" %}

each commute. If all the $\varepsilon_{f, g}$ and $\eta_U$ are identities, then $F$ is not merely a pseudofunctor but an ordinary functor $\mathcal{C}^\op \rightarrow \Grpd$, and this case is called a *strict* functor.

In the end, the definition is somewhat complicated and long, but the essential observation, as we saw above, is that one adds as extra data a choice of a concrete pullback for each $f: U\rightarrow V$ and each object; such a choice is called a *cleavage*.

## Categories Fibered in Groupoids

A pseudofunctor is a familiar notion in that it generalizes a presheaf $\mathcal{C}^\op\rightarrow \Set$, but to put it to use in serious computation, there are already two kinds of isomorphisms to keep track of. The category fibered in groupoids that we treat in this section is an object carrying essentially equivalent data, but instead of remembering the choices of isomorphisms one by one as above, it hides them inside Cartesian diagrams.

The basic idea is as follows. Earlier we kept a separate groupoid $F(U)$ for each object $U$; instead, we now collect the objects of all the $F(U)$ into a single category $\mathcal{F}$. To recover the original $F(U)$'s from this, we need a projection functor $P: \mathcal{F}\rightarrow \mathcal{C}$ that records over which $U$ each object lies. The key idea of this point of view is that the pullback $f^\ast$ enters as a *Cartesian morphism* in $\mathcal{F}$, and the universal property of this Cartesian morphism is exactly the data hiding the choices of isomorphisms above.

::: Definition 4
Fix a functor $P:\mathcal{F}\rightarrow \mathcal{C}$. A morphism $\varphi: \xi\rightarrow \eta$ of $\mathcal{F}$ is a *lift* of a morphism $f: U\rightarrow V$ of $\mathcal{C}$ if $P(\varphi)=f$. A lift $\varphi$ of $f$ is then called a *cartesian morphism* (or *cartesian lift*) if it satisfies the following universal property.

> Whenever an object $\zeta$ of $\mathcal{F}$, a morphism $\psi:\zeta \rightarrow \eta$, and $h: P(\zeta)\rightarrow U$ satisfy $f\circ h=P(\psi)$, there exists a unique morphism $\chi:\zeta \rightarrow \xi$ that is a lift of $h$ and satisfies $\varphi\circ \chi=\psi$.
:::

Thinking of the following diagram roughly shows that the name cartesian morphism is justified.

{% diagram Math/Stacks/Fibered_Categories_and_Stacks-4.svg width="14.13em" alt="Universal property of a cartesian morphism" %}

The universality of this cartesian morphism then says that if a $\xi$ satisfying the condition exists, it is determined uniquely up to unique isomorphism, and in this way $\varepsilon$ and $\eta$ are hidden. We write this $\xi$ as $f^\ast \eta$ and call it the *pullback* of $\eta$ along $f$. If we now require that every morphism factor through such pullbacks and that each fiber be a groupoid, we obtain the notion of a *category fibered in groupoids*.

::: Definition 5
A functor $P:\mathcal{F} \rightarrow \mathcal{C}$ is a *category fibered in groupoids* if it satisfies the following two conditions.

1. For any morphism $f: U \rightarrow V$ and any object $\eta$ over $V$, there exists a cartesian morphism $\varphi:\xi \rightarrow \eta$ that is a lift of $f$ with codomain $\eta$.
2. Every morphism of $\mathcal{F}$ is cartesian.

In this case, for an object $U\in \mathcal{C}$, the subcategory of $\mathcal{F}$ consisting of the objects lying over $U$ and the morphisms that are lifts of $\id_U$ is called the *fiber* $\mathcal{F}(U)$ over $U$.
:::

Choosing one cartesian lift $f^\ast\eta\rightarrow\eta$ for each morphism $f:U\rightarrow V$ and each object $\eta\in\mathcal{F}(V)$ is called a *cleavage*. A cleavage is the choice that consistently picks actual representatives among the pullbacks, which are unique up to isomorphism by universality, in order to define the pullback functors.

::: Proposition 6
For a CFG $P:\mathcal{F} \rightarrow \mathcal{C}$, the following hold.

1. Each fiber $\mathcal{F}(U)$ is a groupoid.
2. Once a cleavage is chosen, for each morphism $f:U\rightarrow V$ a functor $f^\ast:\mathcal{F}(V) \rightarrow \mathcal{F}(U)$ is defined, and a different choice changes this functor only up to canonical natural isomorphism. Moreover, for composable $U\xrightarrow{f}V\xrightarrow{g}W$ there is a canonical natural isomorphism $f^\ast\circ g^\ast\cong(g\circ f)^\ast$.
:::
::: Proof
1. First, let $\alpha:\xi \rightarrow \eta$ be a morphism that is a lift of $\id_U$. Since every morphism of $\mathcal{F}$ is cartesian, $\alpha$ is a cartesian morphism. Hence, applying the universality of cartesian morphisms with $\psi=\id_\eta$ and $h=\id_U$, there exists a unique $\theta:\eta \rightarrow \xi$ such that $\alpha\circ \theta=\id_\eta$ and $P(\theta)=\id_U$, giving a right inverse of $\alpha$. In the same way, $\theta$ is also a cartesian morphism, so applying universality again yields $\theta':\xi \rightarrow \eta$ with $\theta\circ \theta'=\id_\xi$ and $P(\theta')=\id_U$. Now, from $\alpha\circ \theta=\id_\eta$,

    $$\alpha=(\alpha\circ \theta)\circ \theta'=\theta'$$

    so $\alpha$ and $\theta$ are inverse to each other. That is, every morphism of $\mathcal{F}(U)$ is invertible, so $\mathcal{F}(U)$ is a groupoid.

2. Fix a cleavage. Then first, for each $\eta\in \mathcal{F}(V)$ a cartesian lift $\varphi_\eta:f^\ast \eta\rightarrow\eta$ is given. Now, for a morphism $\beta:\eta \rightarrow \eta'$ of $\mathcal{F}(V)$, apply the universal property of cartesian morphisms to the composite $\beta\circ \varphi_\eta:f^\ast \eta \rightarrow \eta'$ together with the cartesian morphism $\varphi_{\eta'}:f^\ast \eta' \rightarrow \eta'$ over $\eta$ and $h=\id_U$: then a unique $\theta:f^\ast \eta \rightarrow f^\ast \eta'$ with $\varphi_{\eta'}\circ \theta=\beta\circ \varphi_\eta$ and $P(\theta)=\id_U$ is determined, and we can therefore define it to be $f^\ast\beta$. Uniqueness then easily shows $f^\ast(\beta'\circ \beta)=f^\ast \beta'\circ f^\ast \beta$ and $f^\ast \id=\id$, so $f^\ast$ is a functor.

    If instead one had chosen a different cleavage $\widetilde{\varphi}_\eta:\widetilde{f^\ast \eta}\rightarrow\eta$ above, the universal property of the two cartesian morphisms gives an isomorphism $\widetilde{f^\ast \eta}\cong f^\ast \eta$, natural in $\eta$.

    Finally, the composite $f^\ast g^\ast \eta \rightarrow g^\ast \eta \rightarrow \eta$ is a cartesian morphism lying over $g\circ f$, and $(g\circ f)^\ast \eta \rightarrow \eta$ is also one, so the universal property yields an isomorphism $f^\ast g^\ast \eta\cong(g\circ f)^\ast \eta$.
:::

Thus, given a CFG, one can recover a pseudofunctor through a cleavage, and this differs only up to canonical natural isomorphism depending on the choice of cleavage. We will show that, conversely, a pseudofunctor also gives a CFG and that these are inverse to each other, so the two formulations carry essentially the same information.

To state this correspondence precisely, we must first examine exactly what kind of object the collection of pseudofunctors and CFGs forms. For this we need to look at what the target $\Grpd$ really is: since it is a category of categories, viewing it as a $2$-category is presumably the way to lose no information. The most transparent example showing that this is actually necessary is the following. Consider the terminal groupoid $\ast$, and for an arbitrary groupoid $\mathcal{G}$, a functor $\ast\rightarrow \mathcal{G}$ is a choice of one object of $\mathcal{G}$, and a natural transformation between two such functors is the same as a morphism between those two objects. Therefore

$$\Fun(\ast,\mathcal{G})\simeq\mathcal{G}$$

. On the other hand, if we view $\Grpd$ only as an ordinary category, $\Hom_{\Grpd}(\ast,\mathcal{G})$ retains only the objects of $\mathcal{G}$ as a set, losing the isomorphisms and automorphisms between them, which defeats the original purpose of passing from $\Set$ to $\Grpd$.

For this reason, if we regard $\Grpd$ as a $2$-category (more precisely, as a $(2,1)$-category), it is natural to view the pseudofunctors with target $\Grpd$ as forming a $2$-category whose $1$-morphisms are pseudonatural transformations and whose $2$-morphisms are modifications between them. Indeed, the reason the canonical natural isomorphisms $\varepsilon_{f,g}$ and $\eta_U$ of a pseudofunctor can be recorded as coherence data is that the target $\Grpd$ has such $2$-morphisms. For this reason our correspondence ([Theorem 8](#thm8)) will also be given as a $2$-equivalence between $2$-categories, and to this end we must first define the $1$-morphisms and $2$-morphisms between CFGs.

::: Definition 7
A *morphism* between two CFGs $P:\mathcal{F} \rightarrow \mathcal{C}$ and $Q:\mathcal{G} \rightarrow \mathcal{C}$ is a functor $G:\mathcal{F} \rightarrow \mathcal{G}$ satisfying $Q\circ G=P$. A *2-morphism* between two morphisms $G, G':\mathcal{F} \rightarrow \mathcal{G}$ is a natural transformation $\alpha: G\Rightarrow G'$ each of whose components $\alpha_\xi$ lies over $\id_{P(\xi)}$.
:::

One can then easily check that a morphism between CFGs sends cartesian morphisms to cartesian morphisms. Also, by the above definition, the category of CFGs forms a 2-category. The condition in the definition that each component of a $2$-morphism lies over $\id$ means that it is a morphism inside some fiber $\mathcal{G}(U)$; in particular, since $\mathcal{G}(U)$ is a groupoid by [Proposition 6](#prop6), a $2$-morphism is always a natural isomorphism. Then the following holds.

::: Theorem 8 (Grothendieck)
The 2-category of CFGs over a category $\mathcal{C}$ and the 2-category of pseudofunctors $\mathcal{C}^\op \rightarrow \Grpd$ are 2-equivalent.
:::

We omit the proof, but the *Grothendieck construction* $\int_\mathcal{C}F$ corresponding to a pseudofunctor $F$ is itself already familiar. ([\[Category Theory\] §Representable Functors, ⁋Definition 7](/en/math/category_theory/representable_functors#def7)) The objects of this category are pairs $(U, x)$ with $U\in \mathcal{C}$, $x\in F(U)$, a morphism from $(U, x)$ to $(V, y)$ is a pair $(f, \alpha)$ with $f: U \rightarrow V$ and $\alpha: x\xrightarrow{\sim}f^\ast y$ in $F(U)$, and the projection $(U, x)\mapsto U$ makes it into a CFG.

In any case, by [Theorem 8](#thm8) we can freely describe a "groupoid varying over a base category" either as a pseudofunctor or as a CFG. From now on we mix the two languages according to context; in particular, we give definitions cleanly in terms of CFGs, but carry out concrete computations with notation such as the pullback $f^\ast$ and $x\vert_V$ of a pseudofunctor. The following examples are the main objects of this post.

::: Example 9
1. For a fixed object $X\in \mathcal{C}$, the structure on the slice category $\mathcal{C}_{/X}$ given by the projection $P:(T \rightarrow X)\mapsto T$ is a CFG. In this case, the fiber $\mathcal{C}_{/X}(T)$ over $T$ is, by its definition, the set of morphisms $\Hom_\mathcal{C}(T, X)$ viewed as a discrete groupoid, and this is the CFG corresponding to the functor of points $h_X$.

2. Consider the category $\mathcal{QCoh}$ whose objects are pairs $(T, \mathcal{F})$ consisting of a scheme $T$ and a quasi-coherent sheaf $\mathcal{F}$ on it. A morphism from $(T, \mathcal{F})$ to $(T', \mathcal{F}')$ is given by a pair $(f, \alpha)$ of $f: T \rightarrow T'$ and an isomorphism $\alpha: \mathcal{F}\xrightarrow{\sim}f^\ast \mathcal{F}'$ of quasi-coherent sheaves. Endowing this with the projection $(T, \mathcal{F})\mapsto T$ makes it a CFG, and the fiber $\mathcal{QCoh}(T)$ over $T$ is the groupoid $\QCoh(T)$ of quasi-coherent sheaves on $T$. Here $\QCoh(T)$ takes only isomorphisms as morphisms.

3. Similar to the example of principal $G$-bundles we saw in the introduction, we consider a category whose objects are the $T$-families of some geometric object and whose morphisms are the isomorphisms between these families, and then endow it with a projection as in the two cases above to obtain a CFG. Such a situation is called a *moduli problem*.
:::

## Descent

If we write a moduli problem as a set-valued presheaf $F$ as in the introduction, then *solving* it means finding a geometric object $X$ having a functor of points $h_X$ that is naturally isomorphic to $F$. So far we have changed the target to $\Grpd$ to obtain a language that remembers both families and the isomorphisms between them, but this alone does not guarantee representability or local-to-global properties.

In this section we show that such representability questions are closely related to the moduli functor being a sheaf. To talk about the sheaf condition, we must first put a topology on the base category. Since no topology was used in the definitions so far, there is no guarantee that compatible objects and isomorphisms over a covering glue into a global object. A stack is a $\Grpd$-valued sheaf obtained by imposing a descent condition on a CFG for the coverings of [§Grothendieck Topology, ⁋Definition 6](/en/math/stacks/grothendieck_topology#def6).

In this section $(\mathcal{C}, \tau)$ is a site, and we describe the topology by a pretopology given through covering families $\{U_i \rightarrow U\}$. ([§Grothendieck Topology, ⁋Definition 4](/en/math/stacks/grothendieck_topology#def4)) Also, when working with a CFG, we fix one cleavage of $P:\mathcal{F} \rightarrow \mathcal{C}$ and use the pullback $f^\ast$ of $f: V\rightarrow U$ and the restriction $x\vert_V=f^\ast x$.

::: Definition 10
Suppose a CFG $P:\mathcal{F} \rightarrow \mathcal{C}$, an object $U\in \mathcal{C}$, and two objects $x, y\in \mathcal{F}(U)$ are given. The *Isom presheaf* over $U$ is the presheaf on the slice site $\mathcal{C}_{/U}$ defined by the assignment

$$\rIsom_U(x, y):(\mathcal{C}_{/U})^\op \rightarrow \Set;\qquad (f: V \rightarrow U)\mapsto \Hom_{\mathcal{F}(V)}(f^\ast x, f^\ast y)$$

.
:::

In this presheaf, the restriction map for a morphism $g: W \rightarrow V$ of $\mathcal{C}_{/U}$ is induced by the pullback $g^\ast$ and the isomorphism $g^\ast f^\ast\cong(f\circ g)^\ast$. Concretely, restricting an isomorphism $\beta: f^\ast x\xrightarrow{\sim}f^\ast y$ over $V$ to $W$ yields

$$g^\ast\beta: g^\ast f^\ast x\rightarrow g^\ast f^\ast y$$

. This is an isomorphism since $g^\ast$ is a functor, and identifying the two ends via $g^\ast f^\ast\cong(f\circ g)^\ast$ makes it an element of $\rIsom_U(x,y)(W)$.

In the strategy explained earlier, a CFG corresponds to a $\Grpd$-valued presheaf, so to make it into a $\Grpd$-valued sheaf we must be able to glue the local fiber groupoids over a covering into a single global fiber groupoid. Since a groupoid consists of objects and the isomorphisms between them, this involves both the problem of gluing morphisms and the problem of gluing objects.

Let us first consider the problem of gluing morphisms. For two fixed objects $x,y\in\mathcal{F}(U)$, $\rIsom_U(x,y)$ is the presheaf collecting the local isomorphisms that exist between their restrictions. Here the source and target of the local isomorphisms are already given as restrictions of the global objects $x,y$. For this presheaf to be a sheaf means that local isomorphisms given over a covering glue into a unique global isomorphism whenever they agree on the overlaps. This is descent for morphisms, and in the categorical equivalence of [\[Schemes\] §Faithfully Flat Descent, ⁋Theorem 6](/en/math/scheme_theory/faithfully_flat_descent#thm6) it corresponds to full faithfulness.

In the problem of gluing objects, no global object is given in advance. Therefore, in addition to the objects $x_i$ over each $U_i$, one must also give isomorphisms $\varphi_{ij}$ over the overlaps $U_{ij}$ identifying them. These are the data specifying how to glue the $x_i$'s, and what one obtains when they satisfy the cocycle condition is a descent datum. Asking whether this descent datum comes from the restrictions of an actual global object is effective descent for objects, and in the above categorical equivalence it corresponds to essential surjectivity. Since essential surjectivity does not follow from full faithfulness alone, being able to glue morphisms does not by itself allow one to glue objects. This is the transport of the descent datum of [\[Schemes\] §Faithfully Flat Descent, ⁋Definition 4](/en/math/scheme_theory/faithfully_flat_descent#def4) to an arbitrary CFG.

To this end, let us fix the notation to be used in the next definition. For a given covering family $\{f_i: U_i \rightarrow U\}_{i\in I}$, we write

$$U_{ij}=U_i\times_U U_j,\qquad U_{ijk}=U_i\times_U U_j\times_U U_k$$

and so on, and denote the pullback along a projection $\pr: U_{ij} \rightarrow U_i$ etc. by $\vert_{U_{ij}}$.

::: Definition 11
Suppose a CFG $P:\mathcal{F} \rightarrow \mathcal{C}$ and a covering family $\{f_i: U_i \rightarrow U\}_{i\in I}$ are given. A *descent datum* for this covering consists of

1. an object $x_i\in \mathcal{F}(U_i)$ defined for each $i$,
2. an isomorphism $\varphi_{ij}: x_j\vert_{U_{ij}}\xrightarrow{\sim}x_i\vert_{U_{ij}}$ of $\mathcal{F}(U_{ij})$ defined for each pair $(i, j)$,

satisfying the *cocycle condition* $\varphi_{ik}\vert_{U_{ijk}}=\varphi_{ij}\vert_{U_{ijk}}\circ \varphi_{jk}\vert_{U_{ijk}}$ over $U_{ijk}$.
:::

As with descent for schemes, if there exist an object $x\in \mathcal{F}(U)$ and isomorphisms $\psi_i: x\vert_{U_i}\rightarrow x_i$ such that $\varphi_{ij}\circ(\psi_j\vert_{U_{ij}})=\psi_i\vert_{U_{ij}}$ holds over each $U_{ij}$, we call this an *effective* descent. That is, when the pieces are glued together through the descent datum, an actually existing element $x$ is obtained. In faithfully flat descent, descent data for modules were always effective ([\[Schemes\] §Faithfully Flat Descent, ⁋Theorem 6](/en/math/scheme_theory/faithfully_flat_descent#thm6)), but for a general CFG, effectivity is a separate condition. Combining these two conditions defines a stack.

::: Definition 12
For a CFG $P:\mathcal{F} \rightarrow \mathcal{C}$ over a site $(\mathcal{C}, \tau)$,

1. $\mathcal{F}$ is a *prestack* means that for any $U$ and $x, y\in \mathcal{F}(U)$, the presheaf $\rIsom_U(x, y)$ is a sheaf on $\mathcal{C}_{/U}$. ([§Grothendieck Topologies, ⁋Definition 9](/en/math/stacks/grothendieck_topology#def9)
2. $\mathcal{F}$ is a *stack* means that $\mathcal{F}$ is a prestack and moreover every descent datum for any covering family is effective.
:::

By [Theorem 8](#thm8), passing to the pseudofunctor $F:\mathcal{C}^\op\rightarrow\Grpd$ corresponding to $\mathcal{F}$, Definition 12 can be expressed as a single equivalence condition. Fix a covering $\mathcal{U}=\{U_i\rightarrow U\}$, and write $\Desc_F(\mathcal{U})$ for the groupoid whose objects are the descent data of [Definition 11](#def11). A morphism between two descent data $(x_i,\varphi_{ij})$ and $(y_i,\psi_{ij})$ is a family $\theta_i:x_i\rightarrow y_i$ of local morphisms satisfying $\psi_{ij}\circ\theta_j=\theta_i\circ\varphi_{ij}$ on each overlap.

Restricting a global object $x\in F(U)$ to each $U_i$ and using the canonical comparison isomorphisms of the pseudofunctor on double overlaps produces a descent datum. Hence the restriction functor

$$F(U)\longrightarrow\Desc_F(\mathcal{U})$$

is defined. The stack condition of Definition 12 is equivalent to this functor being an equivalence of groupoids for every covering $\mathcal{U}$. Its being fully faithful is the prestack condition that local morphisms glue uniquely into a global morphism, and its being essentially surjective is the condition that every descent datum is effective.

Thus a stack, in one sentence, is a $\Grpd$-valued sheaf over a site (more precisely, a sheaf in the 2-categorical sense). In particular, when the target is $\Set$, as for an ordinary set-valued moduli functor, every fiber is a discrete groupoid, so the above equivalence condition reduces to the ordinary sheaf condition. The following proposition makes this precise.

::: Proposition 13
Suppose that every fiber $\mathcal{F}(U)$ of a CFG $P:\mathcal{F} \rightarrow \mathcal{C}$ is a discrete groupoid. Then $\mathcal{F}$ corresponds to some presheaf $F:\mathcal{C}^\op \rightarrow \Set$, and in this case $\mathcal{F}$ being a prestack is equivalent to $F$ being a separated presheaf, and $\mathcal{F}$ being a stack is equivalent to $F$ being a sheaf.
:::
::: Proof
Since the fibers are discrete, the pseudofunctor of [Theorem 8](#thm8) is a strict functor $F:\mathcal{C}^\op \rightarrow \Set$ (viewing $\Set$ as the category of discrete groupoids). For two objects $x, y\in \mathcal{F}(U)=F(U)$, the set $\Hom_{\mathcal{F}(V)}(x\vert_V, y\vert_V)$ is a one-element set if $x\vert_V=y\vert_V$ and empty otherwise. Hence $\rIsom_U(x, y)$ being a sheaf means that if $x, y$ agree on each $U_i$ of a covering (with the gluing condition holding vacuously), then they agree on $U$; in other words, amalgamations in $F$ are unique. ([§Grothendieck Topologies, ⁋Definition 9](/en/math/stacks/grothendieck_topology#def9)

Next, consider effective descent. In discrete fibers, every isomorphism $\varphi_{ij}$ is necessarily the identity, so a descent datum is merely a family $(x_i)$ satisfying $x_i\vert_{U_{ij}}=x_j\vert_{U_{ij}}$, that is, a matching family of $F$. Its effectivity is precisely the existence of an amalgamation $x\in F(U)$. Hence every descent datum being effective means every matching family of $F$ has an amalgamation, and combined with the prestack condition this is exactly the sheaf condition. ([§Grothendieck Topologies, ⁋Proposition 10](/en/math/stacks/grothendieck_topology#prop10)
:::

From this we obtain the following corollary, which is important for our purposes.

::: Corollary 14
Suppose the site $(\mathcal{C}, \tau)$ is subcanonical. Then for any object $X\in\mathcal{C}$, the functor of points $h_X$ is a sheaf, and the corresponding representable CFG $\mathcal{C}_{/X}$ is a stack.
:::
::: Proof
Being subcanonical means that every representable presheaf $h_X$ is a sheaf. Hence it suffices to apply [Proposition 13](#prop13) to the $\mathcal{C}_{/X}$ of [Example 9](#ex9).
:::

By [§Grothendieck Topologies, ⁋Theorem 14](/en/math/stacks/grothendieck_topology#thm14), the corollary above applies in particular to the fpqc site. In other words, the functor of points built from any scheme is a sheaf, and the corresponding CFG is a stack. More generally, by [Proposition 13](#prop13), if a set-valued presheaf $F$ is a sheaf, then viewing each $F(U)$ as a discrete groupoid yields a stack. That is, for moduli problems without automorphisms, everything we have examined so far applies almost for free.

## Examples of Stacks

We now construct concrete stacks. The most fundamental example is the quasi-coherent sheaf CFG of [Example 9](#ex9); the fact that it is a stack is a direct translation of faithfully flat descent.

::: Theorem 15
Take the base site to be the fpqc site on $\Sch$ (or $\Sch_{/S}$). ([[\[Schemes\] §Faithfully Flat Descent, ⁋Definition 9](/en/math/scheme_theory/faithfully_flat_descent#def9) Then the quasi-coherent sheaf CFG $\mathcal{QCoh}$ of [Example 9](#ex9) is a stack.
:::
::: Proof
We reduce the prestack condition and effectivity in turn to faithfully flat descent. Both conditions concern fpqc coverings, and by quasi-compactness one can collect a finite subcover, take the disjoint union, and thereby reduce to the case of a single affine faithfully flat morphism $\Spec B \rightarrow \Spec A$.

First we verify the prestack condition. For two quasi-coherent sheaves $\mathcal{F}, \mathcal{G}$ on $T=\Spec A$, i.e. two $A$-modules $M, N$, we must show that the presheaf $\rIsom_T(\mathcal{F}, \mathcal{G})$ is a sheaf. For this it suffices to show that the homomorphism presheaf

$$(\Spec A' \rightarrow \Spec A)\mapsto \Hom_{A'}(M\otimes_A A', N\otimes_A A')$$

is a sheaf. This is because an isomorphism is cut out as a subsheaf by the condition that a pair of homomorphisms in each direction compose to the identity. Now, the faithfully flat descent functor $\rMod{A} \rightarrow \Desc(B/A)$ is a categorical equivalence ([[\[Schemes\] §Faithfully Flat Descent, ⁋Theorem 6](/en/math/scheme_theory/faithfully_flat_descent#thm6), hence in particular it is fully faithful. ([[\[Category Theory\] §Functor, ⁋Definition 10](/en/math/category_theory/functors#def10) Full faithfulness says precisely that homomorphisms descend uniquely along the covering $\{\Spec B \rightarrow \Spec A\}$, i.e. the sheaf condition for the $\Hom$ presheaf.

For effectivity, a descent datum over a covering family $\{T_i \rightarrow T\}$ consists of quasi-coherent sheaves $\mathcal{F}_i$ on each $T_i$ together with cocycle isomorphisms $\varphi_{ij}$ over $T_{ij}$. This is exactly a descent datum for quasi-coherent sheaves, and since quasi-coherent sheaves satisfy effective descent for the fpqc topology ([[\[Schemes\] §Faithfully Flat Descent, ⁋Theorem 11](/en/math/scheme_theory/faithfully_flat_descent#thm11), they glue uniquely to a quasi-coherent sheaf $\mathcal{F}$ on $T$ together with isomorphisms $\mathcal{F}\vert_{T_i}\cong \mathcal{F}_i$. Therefore every descent datum is effective, and together with the prestack condition this shows that $\mathcal{QCoh}$ is a stack.
:::

[Theorem 15](#thm15) makes explicit once again the principle we saw above: the prestack condition reduces to the full faithfulness of [[\[Schemes\] §Faithfully Flat Descent, ⁋Theorem 6](/en/math/scheme_theory/faithfully_flat_descent#thm6), while effectivity reduces to the effective descent of [[\[Schemes\] §Faithfully Flat Descent, ⁋Theorem 11](/en/math/scheme_theory/faithfully_flat_descent#thm11), respectively.

On the other hand, not every CFG is a stack, so we need a universal operation that completes a prestack into a stack. This is *stackification*, the stack version of the sheafification of [§Grothendieck Topologies, ⁋Theorem 12](/en/math/stacks/grothendieck_topology#thm12).

::: Theorem 16 (Stackification)
For any CFG $\mathcal{F}$ over a site $(\mathcal{C}, \tau)$, there exist a stack $\mathcal{F}^a$ and a morphism $\iota:\mathcal{F} \rightarrow \mathcal{F}^a$ with the following universal property: for any stack $\mathcal{G}$, composition with $\iota$

$$\Hom(\mathcal{F}^a, \mathcal{G})\xrightarrow{\ \sim\ }\Hom(\mathcal{F}, \mathcal{G})$$

is an equivalence of categories. In other words, the 2-category of stacks is a reflective subcategory of the 2-category of CFGs, with $\iota$ as the unit.
:::

As with its origin [§Grothendieck Topologies, ⁋Theorem 12](/en/math/stacks/grothendieck_topology#thm12), the proof is quite long, so we omit it. In any case, this is the 2-categorical version of the sheafification adjunction: just as sheafification is the left adjoint sending presheaves to sheaves, stackification is the 2-categorical reflection sending CFGs to stacks. Thanks to this construction, we can freely write down a moduli problem as a CFG first and then, if necessary, stackify it to obtain an object for which descent holds.

At last, it is time to wrap up the example from the introduction.

::: Definition 17
Let $G$ be a sheaf of groups on a site $(\mathcal{C}, \tau)$ and $T\in \mathcal{C}$ an object. A *$G$-torsor* (or *principal $G$-bundle*) over $T$ is a sheaf $P$ on $\mathcal{C}_{/T}$ together with a left action $G\vert_T\times P \rightarrow P$ such that, over some covering $\{T_i \rightarrow T\}$, there exists a $G\vert_{T_i}$-equivariant isomorphism

$$P\vert_{T_i}\cong G\vert_{T_i}$$

where the right-hand side carries the left-translation action of $G\vert_{T_i}$. A morphism of $G$-torsors is a $G$-equivariant sheaf morphism, and the $G$-torsors over $T$ form a groupoid $\bB G(T)$. We write $\bB G$ for the CFG defined by the correspondence $T\mapsto \bB G(T)$, called the *classifying stack* $\bB G$.
:::

Comparing the local trivializations $P\vert_{T_i}\cong G\vert_{T_i}$ yields $G$-valued transition data $g_{ij}\in G(T_{ij})$ over $T_{ij}$, which form a cocycle. The trivial torsor $G\vert_T$ is an object of $\bB G(T)$ with automorphism group $\Aut_{\bB G(T)}(G\vert_T)\cong G(T)$. Thus $\bB G$ remembers $G$ as automorphisms even of the trivial torsor, and the isomorphism classes of $\bB G(T)$ are classified by $H^1(T, G)$. The most important case is $G=\mathbb{G}_m$; this is the classification of line bundles anticipated in [Example 2](#ex2).

::: Theorem 18
Over the fpqc site on $\Sch$ (or $\Sch_{/S}$), the classifying stack $\bB\mathbb{G}_m$ of $\mathbb{G}_m$-torsors is equivalent to the CFG whose fiber over $T$ is the groupoid $\mathcal{L}(T)$ of line bundles over $T$, and this CFG is a stack.
:::
::: Proof
First, the equivalence between $\mathbb{G}_m$-torsors and line bundles was seen in [[\[Schemes\] §Group Schemes, ⁋Example 15](/en/math/scheme_theory/group_schemes#ex15). Under the frame torsor construction, isomorphisms of line bundles correspond to $\mathbb{G}_m$-equivariant isomorphisms of frame torsors, and this correspondence is compatible with base change. Hence $\bB\mathbb{G}_m(T)\cong \mathcal{L}(T)$ for each $T$, and the two CFGs are equivalent.

We now show that the line bundle CFG $\mathcal{L}$ is a stack. It is the full sub-CFG of $\mathcal{QCoh}$ consisting only of invertible sheaves, so the Isom presheaf between two line bundles $\mathcal{E}, \mathcal{F}\in\mathcal{L}(T)$ coincides with the presheaf $\rIsom_T(\mathcal{E}, \mathcal{F})$ computed in $\mathcal{QCoh}$. By [Theorem 15](#thm15), this presheaf is a sheaf; hence $\mathcal{L}$ is a prestack.

Next we check object descent. Suppose we have line bundles $\mathcal{L}_i$ over a covering family $\{T_i \rightarrow T\}$ and isomorphisms $\varphi_{ij}$ over the overlaps forming a descent datum. By [Theorem 15](#thm15), there exists a quasi-coherent sheaf $\mathcal{F}$ realizing this datum, with isomorphisms $\mathcal{F}\vert_{T_i}\cong \mathcal{L}_i$. Since being locally free of rank $1$ descends along fpqc coverings by [[\[Schemes\] §Faithfully Flat Descent, ⁋Proposition 7](/en/math/scheme_theory/faithfully_flat_descent#prop7), $\mathcal{F}$ is also invertible. Hence every descent datum is effective inside $\mathcal{L}(T)$, and $\mathcal{L}\cong \bB\mathbb{G}_m$ is a stack.
:::

---

**References**

**[FGA]** B. Fantechi, L. Göttsche, L. Illusie, S. Kleiman, N. Nitsure, A. Vistoli, *Fundamental algebraic geometry: Grothendieck's FGA explained*. Mathematical Surveys and Monographs, American Mathematical Society, 2005.  
**[Stacks]** The Stacks Project Authors, *The Stacks Project*. Available [online](https://stacks.math.columbia.edu/).
