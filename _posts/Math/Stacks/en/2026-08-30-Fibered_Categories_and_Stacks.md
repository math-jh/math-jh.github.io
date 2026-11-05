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
translated_at: 2026-09-02T06:45:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-11-05T19:15:07+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
The stacks we will deal with essentially come from moduli problems, and a representative example of such problems is the problem of classifying, over a topological space $X$, principal $G$-bundles, or vector bundles of rank $r$, which we saw in [\[Algebraic Topology\] §Classifying Spaces, ⁋Theorem 8](/en/math/algebraic_topology/classifying_spaces#thm8){: data-lid="4ipsq" }. The nicest fact we gain from the functor of points perspective introduced in [\[Schemes\] §Functor of Points](/en/math/scheme_theory/functor_of_points){: data-lid="86kzw" } is that, in the algebro-geometric form of this problem, we can regard a correspondence of this kind

$$F:\Sch^\op\rightarrow \Set;\qquad T\mapsto \{\text{principal $G$-bundles over $T$}\}$$

as a functor in its own right and then examine whether this functor is actually represented by a scheme. However, this formula itself is not a well-defined functor, the essential reason being that, to show the functoriality of this correspondence, one must, for a morphism $f:Y\rightarrow X$, use the pullback $f^\ast P$ of a bundle to transport a bundle over $X$ to $Y$, yet the pullback bundle itself is by its very nature uniquely determined only up to unique isomorphism.

The way topology resolved this was simple. Instead of the naive correspondence above, everything is settled in $\hTop$. That is, one only needs to consider the correspondence

$$X\mapsto \{\text{principal $G$-bundles over $X$}\}/{\cong}$$

Then an important result of this theory was that for $G$, over its classifying space $\B G$, there exists a universal bundle $\E G\rightarrow\B G$, and the correspondence pulling it back gives a bijection

$$[X,\B G]\xrightarrow{\sim}\{\text{principal $G$-bundles over $X$}\}/{\cong};\qquad [f]\mapsto[f^\ast\E G]$$

What makes this work is the condition that $\E G$ is contractible: if the pullbacks along two classifying maps are isomorphic, then from that bundle to $\E G$, the two $G$-equivariant maps are homotopic, and therefore the two classifying maps are homotopic as well. In other words, this classification theorem is the statement that the two sets obtained after killing bundle isomorphisms and homotopies between morphisms respectively by equivalence relations are equal.

The problem is that the language of algebraic geometry is more rigid than that of topology and cannot accommodate homotopy in this way. The solution to this is not to kill the isomorphisms but to keep all of them alive; as a result, the moduli functor $F$ is now not $\Set$-valued but $\Grpd$-valued.

## Groupoids

First, let us recall the following definition.

::: Definition 1
A category $\mathcal{G}$ is a *groupoid* if every morphism of $\mathcal{G}$ is an isomorphism. ([\[Category Theory\] §Category, ⁋Definition 11](/en/math/category_theory/categories#def11){: data-lid="wf47x" })
:::

In [\[Category Theory\] §Category, ⁋Definition 10](/en/math/category_theory/categories#def10){: data-lid="mosoa" }, we defined a group as a category with a single object in which every morphism is an isomorphism. Thus, in a groupoid $\mathcal{G}$, for an object $x\in \mathcal{G}$, $\Aut_\mathcal{G}(x)=\Hom_\mathcal{G}(x, x)$ forms a group under composition, which we call the *automorphism group* of $x$. We write $\Grpd$ for the category whose objects are groupoids and whose morphisms are functors between them.

In this way, a groupoid can be viewed as a generalization of a group, but that is not the whole story. The point of view useful to us is that it can also be regarded as a generalization of a set, since any set can be seen as a category whose only morphisms are identities. A groupoid $\mathcal{G}$ then has multiple objects just like a set, but it also carries an isomorphism structure between them.

In the example examined in the introduction, the collection of all principal $G$-bundles over a fixed space $X$ corresponds to a groupoid structure. Then taking isomorphism classes here and leaving only one representative from each corresponds to choosing for the groupoid $\mathcal{G}$ a skeleton $\sk\mathcal{G}$. That is, $\sk \mathcal{G}$ coincides with the collection of isomorphism classes of $\mathcal{G}$. Meanwhile, since a skeleton is a full subcategory, it preserves for each representative $x$ the automorphism group $\Aut_\mathcal{G}(x)$ intact; once we forget even the information of these automorphisms, what we obtain is a discrete groupoid, that is, a set.

::: Example 2
The following are examples of groupoids that we will examine in detail.

1. For a fixed scheme $T$, the category whose objects are the line bundles over $T$ and whose morphisms are the isomorphisms of $\mathcal{O}_T$-modules between line bundles is a groupoid, and the automorphism group of each object $\mathcal{L}$ is $\Aut(\mathcal{L})=\Gamma(T, \mathcal{O}_T)^\ast=\mathbb{G}_m(T)$. If we then obtain the set of isomorphism classes of this groupoid in the manner above, it is precisely the Picard group $\Pic(T)$, and this amounts to forgetting the information of the automorphism group $\mathbb{G}_m(T)$.
2. Another familiar example is the *fundamental groupoid* $\Pi_1(X)$ of a topological space $X$. ([\[Algebraic Topology\] §Homotopy, ⁋Definition 11](/en/math/algebraic_topology/homotopy#def11){: data-lid="aja10" }) This is the category whose objects are points and whose morphisms are homotopy classes of paths, and the automorphism group at a point is exactly the fundamental group $\pi_1(X,x)$.
3. As a trivial example in the flow of our discussion, any functor $F:\mathcal{C}^\op \rightarrow \Set$ is the special case assigning to each $T$ the discrete groupoid $F(T)$. That is, a $\Set$-valued functor is a special case of a $\Grpd$-valued functor.
:::

In particular, the first example is the object we will mainly study. In general, $\Pic(T)$ may contain a nontrivial line bundle $\mathcal{L}$, but by the definition of a line bundle, $\mathcal{L}$ is locally trivial. As we saw in [\[Schemes\] §Faithfully Flat Descent, ⁋Theorem 11](/en/math/scheme_theory/faithfully_flat_descent#thm11){: data-lid="3qlfa" }, if one gives local trivial line bundles over a covering together with isomorphisms connecting them over the overlaps as a descent datum, effective descent yields a single global line bundle. The transition data for gluing the $\mathbb{G}_m$-torsors of [\[Schemes\] §Group Schemes, ⁋Example 15](/en/math/scheme_theory/group_schemes#ex15){: data-lid="z5w01" } are precisely these isomorphisms. Therefore, to distinguish line bundles that all look locally trivial, we must record these isomorphisms without forgetting them.

## Pseudofunctors

Meanwhile, considering the moduli functor $F$ of principal $G$-bundles from the introduction, the intuitive reason the set output by this functor had to be reduced to isomorphism classes was the pullback. This is not a problem resolved merely by upgrading the target of the functor to be $\Grpd$-valued. Therefore, to obtain the functoriality of $F$ in the strict sense, we must properly define the pullback

$$f^\ast=F(f): F(V)\rightarrow F(U)$$

that provides this functoriality; in other words, whenever a morphism $f: U\rightarrow V$ and an object over $V$ are given, we must make a *choice* that consistently picks out its pullback representative. And however such choices are made, the pullback along a composite of two morphisms

$$U\overset{f}{\rightarrow}V\overset{g}{\rightarrow}W$$

is now *no longer* equal to the composite of the two pullbacks, and one must be satisfied merely with the existence of an isomorphism 

$$\varepsilon_{f, g}: f^\ast g^\ast P \xRightarrow{\sim} (g\circ f)^\ast P$$

between the two. The idea of a pseudofunctor is to take all of these as data and to require that they define coherent data.

::: Definition 3
On a category $\mathcal{C}$, a *pseudofunctor* $F:\mathcal{C}^\op \rightarrow \Grpd$ consists of the following data.

1. For each object $U\in \mathcal{C}$, a corresponding groupoid $F(U)$,
2. For each morphism $f: U \rightarrow V$, a corresponding functor $f^\ast: F(V) \rightarrow F(U)$,
3. For each composable pair $U\overset{f}{\rightarrow}V\overset{g}{\rightarrow}W$, a natural isomorphism 
    
    $$\varepsilon_{f, g}: f^\ast\circ g^\ast \xRightarrow{\sim} (g\circ f)^\ast,$$

    and for each object $U$, a natural isomorphism

    $$\eta_U:\id_{F(U)}\xRightarrow{\sim}(\id_U)^\ast.$$

The compatibility conditions they must satisfy are as follows. 

> For three morphisms $U\overset{f}{\rightarrow}V\overset{g}{\rightarrow}W\overset{h}{\rightarrow}Z$,
> 
> $$\varepsilon_{f, h\circ g}\circ(\id_{f^\ast}\ast \varepsilon_{g, h})=\varepsilon_{g\circ f, h}\circ(\varepsilon_{f, g}\ast \id_{h^\ast})$$
> 
> holds, and for any morphism $f: U\rightarrow V$,
> 
> $$\varepsilon_{f, \id_V}\circ(\id_{f^\ast}\ast \eta_V)=\id_{f^\ast},\qquad \varepsilon_{\id_U, f}\circ(\eta_U\ast \id_{f^\ast})=\id_{f^\ast}$$
> 
> hold.
:::

The data and conditions of Definition 3 can be visualized in diagrams as follows. First, the natural isomorphisms $\varepsilon_{f,g}$ and $\eta_U$ in condition 3 appear as 2-morphisms between the two paths represented by the following diagram, respectively.

{% diagram Math/Stacks/Fibered_Categories_and_Stacks-1.svg width="29.13em" alt="Composition isomorphisms and identity isomorphisms" %}

The $\ast$ appearing in the compatibility conditions is the horizontal composition of $2$-morphisms; for example, the first equation means that the following diagram

{% diagram Math/Stacks/Fibered_Categories_and_Stacks-2.svg width="17.76em" alt="Associativity coherence" %}

commutes, and the second equation means that the following diagrams

{% diagram Math/Stacks/Fibered_Categories_and_Stacks-3.svg width="25.28em" alt="unit coherence" %}

each commute. If all $\varepsilon_{f, g}$ and $\eta_U$ are identities, then $F$ is not merely a pseudofunctor but an ordinary functor $\mathcal{C}^\op \rightarrow \Grpd$, and this case is called a *strict* functor. 

In the end, while the definition is somewhat complicated and long, the essential observation, as we saw above, is that one includes as extra data a choice of a concrete pullback for each $f: U\rightarrow V$ and each object; such a choice is called a *cleavage*. 

## Categories Fibered in Groupoids

A pseudofunctor is a familiar notion in that it generalizes a presheaf $\mathcal{C}^\op\rightarrow \Set$, but to put it to use in serious computation there are already two kinds of isomorphisms to keep track of. The category fibered in groupoids that we treat in this section is an object carrying essentially equivalent data, but instead of remembering the choices of isomorphisms one by one as above, it hides them inside Cartesian diagrams.

The basic idea is as follows. Earlier, for each object $U$ we had a separate groupoid $F(U)$; instead, we now collect the objects of all $F(U)$ into a single category $\mathcal{F}$. To recover the original $F(U)$ from this, to see over which $U$ each object lies, we need a projection functor $P: \mathcal{F}\rightarrow \mathcal{C}$. The key idea of this point of view is that the pullback $f^\ast$ enters as a *Cartesian morphism* in $\mathcal{F}$, and the universal property of this Cartesian morphism is precisely the data hiding the choices of isomorphisms above.

::: Definition 4
Fix a functor $P:\mathcal{F}\rightarrow \mathcal{C}$. A morphism in $\mathcal{F}$, $\varphi: \xi\rightarrow \eta$, is a *lift* of a morphism in $\mathcal{C}$, $f: U\rightarrow V$, if $P(\varphi)=f$. In this case, a lift of $f$, $\varphi$, is called a *cartesian morphism* (or *cartesian lift*) if it satisfies the following universal property.

> Whenever an object of $\mathcal{F}$, $\zeta$, a morphism $\psi:\zeta \rightarrow \eta$, and $h: P(\zeta)\rightarrow U$ satisfy $f\circ h=P(\psi)$, there exists a unique lift of $h$ satisfying $\varphi\circ \chi=\psi$, a morphism $\chi:\zeta \rightarrow \xi$.
:::

Thinking of the following diagram roughly shows that the name cartesian morphism is justified.

{% diagram Math/Stacks/Fibered_Categories_and_Stacks-4.svg width="14.13em" alt="Universal property of a cartesian morphism" %}

The universality of this cartesian morphism then says that if $\xi$ satisfying this condition exists, it is determined uniquely up to unique isomorphism, and in this way $\varepsilon$ and $\eta$ are hidden. Then we write this $\xi$ as $f^\ast \eta$ and call it the *pullback* of $\eta$ along $f$. If we now require that every morphism decompose into such pullbacks and that each fiber be a groupoid, we obtain the notion of a *category fibered in groupoids*.

::: Definition 5
A functor $P:\mathcal{F} \rightarrow \mathcal{C}$ is a *category fibered in groupoids* if it satisfies the following two conditions.

1. For any morphism $f: U \rightarrow V$ and any object over $V$, $\eta$, there exists a lift of $f$ with codomain $\eta$ that is a cartesian morphism $\varphi:\xi \rightarrow \eta$.
2. Every morphism of $\mathcal{F}$ is cartesian.

In this case, for an object $U\in \mathcal{C}$, the subcategory consisting of the objects lying over $U$ and the morphisms that are lifts of $\id_U$ in $\mathcal{F}$ is called the *fiber* over $U$, $\mathcal{F}(U)$.
:::

For each morphism $f:U\rightarrow V$ and each object $\eta\in\mathcal{F}(V)$, choosing one cartesian lift $f^\ast\eta\rightarrow\eta$ is called a *cleavage*. A cleavage is a choice that consistently picks actual representatives among the pullbacks, which are unique up to isomorphism by universality, in order to define a pullback functor.

::: Proposition 6
For a CFG $P:\mathcal{F} \rightarrow \mathcal{C}$, the following hold.

1. Each fiber $\mathcal{F}(U)$ is a groupoid.
2. Once a cleavage is chosen, for each morphism $f:U\rightarrow V$ a functor $f^\ast:\mathcal{F}(V) \rightarrow \mathcal{F}(U)$ is defined, and a different choice changes this functor only up to canonical natural isomorphism. Moreover, for composable $U\xrightarrow{f}V\xrightarrow{g}W$ there is a canonical natural isomorphism $f^\ast\circ g^\ast\cong(g\circ f)^\ast$.
:::
::: Proof
1. First, let $\alpha:\xi \rightarrow \eta$ be a morphism that is a lift of $\id_U$. Since every morphism of $\mathcal{F}$ is cartesian, $\alpha$ is a cartesian morphism. Therefore, applying the universality of cartesian morphisms to $\psi=\id_\eta$ and $h=\id_U$, there uniquely exists a morphism satisfying $\alpha\circ \theta=\id_\eta$ and $P(\theta)=\id_U$, namely $\theta:\eta \rightarrow \xi$, yielding a right inverse of $\alpha$. In the same way, $\theta$ is also a cartesian morphism, so applying universality yields a morphism satisfying $\theta\circ \theta'=\id_\xi$ and $P(\theta')=\id_U$, namely $\theta':\xi \rightarrow \eta$. Now, from $\alpha\circ \theta=\id_\eta$,

    $$\alpha=(\alpha\circ \theta)\circ \theta'=\theta'$$

    so $\alpha$ and $\theta$ are inverses of each other. That is, every morphism of $\mathcal{F}(U)$ is invertible, so $\mathcal{F}(U)$ is a groupoid.

2. Fix a cleavage. Then first, for each $\eta\in \mathcal{F}(V)$, a cartesian lift $\varphi_\eta:f^\ast \eta\rightarrow\eta$ is given. Now, for a morphism in $\mathcal{F}(V)$, $\beta:\eta \rightarrow \eta'$, applying the universal property of cartesian morphisms to the composite $\beta\circ \varphi_\eta:f^\ast \eta \rightarrow \eta'$, the cartesian morphism of $\eta$, $\varphi_{\eta'}:f^\ast \eta' \rightarrow \eta'$, as well as $h=\id_U$, a morphism satisfying $\varphi_{\eta'}\circ \theta=\beta\circ \varphi_\eta$ and $P(\theta)=\id_U$, namely $\theta:f^\ast \eta \rightarrow f^\ast \eta'$, is uniquely determined, and thus we can define this to be $f^\ast\beta$. Then by uniqueness, it is easy to show that $f^\ast(\beta'\circ \beta)=f^\ast \beta'\circ f^\ast \beta$ and $f^\ast \id=\id$, so $f^\ast$ is a functor.

    If instead one had chosen a different cleavage $\widetilde{\varphi}_\eta:\widetilde{f^\ast \eta}\rightarrow\eta$ above, by the universal property of the two cartesian morphisms an isomorphism $\widetilde{f^\ast \eta}\cong f^\ast \eta$ exists naturally with respect to $\eta$.

    Finally, the composite $f^\ast g^\ast \eta \rightarrow g^\ast \eta \rightarrow \eta$ is a cartesian morphism lying over $g\circ f$, and $(g\circ f)^\ast \eta \rightarrow \eta$ is also one, so by the universal property we obtain an isomorphism $f^\ast g^\ast \eta\cong(g\circ f)^\ast \eta$.
:::

That is, given a CFG, one can recover a pseudofunctor via a cleavage, and this differs only up to canonical natural isomorphism with respect to the choice of cleavage. We will show that, conversely, a pseudofunctor also gives a CFG and that these are inverse to each other, so the two representations contain essentially the same information.

To state this correspondence precisely, we must first examine what kind of object the collection of pseudofunctors and CFGs forms. For this, we must examine what kind of object the target $\Grpd$ is; since this is a category of categories, viewing it as a $2$-category will be the way not to lose information. The most transparent example showing that this is actually necessary is the following. Consider the terminal groupoid $\ast$ and an arbitrary groupoid $\mathcal{G}$; then a functor $\ast\rightarrow \mathcal{G}$ is a choice of an object of $\mathcal{G}$, and a natural transformation between two such functors is the same as a morphism between those two objects. Therefore

$$\Fun(\ast,\mathcal{G})\simeq\mathcal{G}$$

On the other hand, if we view $\Grpd$ only as an ordinary category, $\Hom_{\Grpd}(\ast,\mathcal{G})$ retains only the objects of $\mathcal{G}$ as a set and loses the isomorphisms and automorphisms between them, defeating the original purpose of having elevated from $\Set$ to $\Grpd$ in the first place.

For this reason, if we view $\Grpd$ as a $2$-category, or more precisely as a $(2,1)$-category, it is natural to view pseudofunctors having target $\Grpd$ also, taking pseudonatural transformations as $1$-morphism and modifications between them as $2$-morphism, as a $2$-category. Indeed, the reason the canonical natural isomorphisms $\varepsilon_{f,g}$ and $\eta_U$ of a pseudofunctor can be recorded as coherence data is that the target $\Grpd$ has such $2$-morphism. For this reason, our correspondence ([Theorem 8](#thm8){: data-lid="202jl" }) will also be given, between $2$-category structures, as a $2$-equivalence, and to this end we must first define the notions of $1$-morphism and $2$-morphism between CFGs.

::: Definition 7
A *morphism* between two CFGs $P:\mathcal{F} \rightarrow \mathcal{C}$ and $Q:\mathcal{G} \rightarrow \mathcal{C}$ is, satisfying $Q\circ G=P$, a functor $G:\mathcal{F} \rightarrow \mathcal{G}$. A *2-morphism* between two morphisms $G, G':\mathcal{F} \rightarrow \mathcal{G}$ is a natural transformation $\alpha: G\Rightarrow G'$ each of whose components $\alpha_\xi$ lies over $\id_{P(\xi)}$.
:::

Then, first, one can easily check that a morphism between CFGs sends cartesian morphisms to cartesian morphisms. Also, by the above definition, the category of CFGs forms a 2-category. The condition above that each component of a $2$-morphism lies over $\id$ means that it is a morphism inside some fiber $\mathcal{G}(U)$; in particular, since $\mathcal{G}(U)$ is a groupoid by [Proposition 6](#prop6){: data-lid="pof0e" }, a $2$-morphism is always a natural isomorphism. Then the following holds.

::: Theorem 8 (Grothendieck)
The 2-category of CFGs over a category $\mathcal{C}$ and the 2-category of pseudofunctors $\mathcal{C}^\op \rightarrow \Grpd$ are 2-equivalent.
:::

We omit the proof of this, but corresponding to a pseudofunctor $F$, the *Grothendieck construction* $\int_\mathcal{C}F$ itself is already familiar. ([\[Category Theory\] §Representable Functors, ⁋Definition 7](/en/math/category_theory/representable_functors#def7){: data-lid="7rb34" }) The objects of this category are pairs of $U\in \mathcal{C}$ and $x\in F(U)$, $(U, x)$; a morphism from $(U, x)$ to $(V, y)$ is a pair of $f: U \rightarrow V$ and $\alpha: x\xrightarrow{\sim}f^\ast y$ in $F(U)$, $(f, \alpha)$; and the projection $(U, x)\mapsto U$ makes it into a CFG.

In any case, by [Theorem 8](#thm8){: data-lid="riaxf" } we can freely describe a "groupoid varying over a base category" either as a pseudofunctor or as a CFG. From now on we mix the two languages according to context; in particular, we give definitions cleanly in terms of CFGs, but carry out concrete computations with notation such as the pullback $f^\ast$ and $x\vert_V$ of a pseudofunctor. The following examples are the main objects of this post.

::: Example 9
1. For a fixed object $X\in \mathcal{C}$, the slice category $\mathcal{C}_{/X}$ endowed with the projection $P:(T \rightarrow X)\mapsto T$ is a CFG. In this case, the fiber over $T$, $\mathcal{C}_{/X}(T)$, is by its definition the set of morphisms $\Hom_\mathcal{C}(T, X)$ viewed as a discrete groupoid, and this is the CFG corresponding to the functor of points $h_X$.

2. For a scheme $T$ and a quasi-coherent sheaf $\mathcal{F}$ on it, consider the category having pairs $(T, \mathcal{F})$ as objects, denoted $\mathcal{QCoh}$. In this case, a morphism from $(T, \mathcal{F})$ to $(T', \mathcal{F}')$ is given by $f: T \rightarrow T'$ and an isomorphism $\alpha: \mathcal{F}\xrightarrow{\sim}f^\ast \mathcal{F}'$ between quasi-coherent sheaves as a pair $(f, \alpha)$. Endowing this with the projection $(T, \mathcal{F})\mapsto T$ makes it a CFG, and the fiber over $T$, $\mathcal{QCoh}(T)$, is the groupoid of quasi-coherent sheaves on $T$, $\QCoh(T)$. Here $\QCoh(T)$ takes only isomorphisms as morphisms.

3. Similar to the example of principal $G$-bundles we saw in the introduction, we consider a category whose objects are the $T$-families of some geometric object and whose morphisms are the isomorphisms between these families, and then endow it with a projection as in the two cases above to obtain a CFG. Such a situation is called a *moduli problem*.
:::

## Descent

If we write a moduli problem as a set-valued presheaf $F$ as in the introduction, *solving* it means finding, naturally isomorphic to $F$, the functor of points $h_X$ of a geometric object $X$. So far we have changed the target to $\Grpd$ to obtain a language that remembers both families and the isomorphisms between them, but this alone does not guarantee representability or local-to-global properties.

In this section we show that such representability questions are closely related to the moduli functor being a sheaf. To talk about the sheaf condition, we must first put a topology on the base category. Since no topology was used in the definitions so far, there is no guarantee that compatible objects and isomorphisms over a covering glue into a global object. A stack is a $\Grpd$-valued sheaf obtained by imposing a descent condition on a CFG for the coverings of [§Grothendieck Topologies, ⁋Definition 6](/en/math/stacks/grothendieck_topology#def6){: data-lid="memtv" }.

In this section $(\mathcal{C}, \tau)$ is a site, and we describe the topology by a pretopology given through covering families $\{U_i \rightarrow U\}$. ([§Grothendieck Topologies, ⁋Definition 4](/en/math/stacks/grothendieck_topology#def4){: data-lid="aqaxp" }) Also, when working with a CFG, we fix one cleavage of $P:\mathcal{F} \rightarrow \mathcal{C}$ and use, for $f: V\rightarrow U$, the pullback $f^\ast$ and the restriction $x\vert_V=f^\ast x$.

::: Definition 10
Suppose a CFG $P:\mathcal{F} \rightarrow \mathcal{C}$, an object $U\in \mathcal{C}$, and two objects $x, y\in \mathcal{F}(U)$ are given. The *Isom presheaf* over $U$ is the presheaf defined by the assignment

$$\rIsom_U(x, y):(\mathcal{C}_{/U})^\op \rightarrow \Set;\qquad (f: V \rightarrow U)\mapsto \Hom_{\mathcal{F}(V)}(f^\ast x, f^\ast y)$$

on the slice site $\mathcal{C}_{/U}$.
:::

In this presheaf, the restriction map for a morphism in $\mathcal{C}_{/U}$, $g: W \rightarrow V$, is induced by the pullback $g^\ast$ and the isomorphism $g^\ast f^\ast\cong(f\circ g)^\ast$. Concretely, restricting an isomorphism over $V$, $\beta: f^\ast x\xrightarrow{\sim}f^\ast y$, to $W$ yields

$$g^\ast\beta: g^\ast f^\ast x\rightarrow g^\ast f^\ast y$$

This is an isomorphism since $g^\ast$ is a functor, and identifying both ends via $g^\ast f^\ast\cong(f\circ g)^\ast$ makes it an element of $\rIsom_U(x,y)(W)$.

In the strategy explained earlier, a CFG corresponds to a $\Grpd$-valued presheaf, so to make it into a $\Grpd$-valued sheaf we must be able to glue the local fiber groupoids over a covering into a single global fiber groupoid. Since a groupoid consists of objects and the isomorphisms between them, this involves both the problem of gluing morphisms and the problem of gluing objects.

Let us first consider the problem of gluing morphisms. For two fixed objects $x,y\in\mathcal{F}(U)$, $\rIsom_U(x,y)$ is the presheaf collecting the local isomorphisms that exist between their restrictions. Here the source and target of the local isomorphisms are already given as restrictions of the global objects $x,y$. For this presheaf to be a sheaf means that local isomorphisms given over a covering glue into a unique global isomorphism whenever they agree on the overlaps. This is descent for morphisms, and in the categorical equivalence of [\[Schemes\] §Faithfully Flat Descent, ⁋Theorem 6](/en/math/scheme_theory/faithfully_flat_descent#thm6){: data-lid="a9deb" }, this corresponds to full faithfulness.

In the problem of gluing objects, no global object is given in advance. Therefore, one must give not only for each $U_i$ an object $x_i$, but also over the overlap $U_{ij}$ an isomorphism $\varphi_{ij}$ identifying them. These are the data specifying how to glue the $x_i$, and what one obtains when they satisfy the cocycle condition is a descent datum. Asking whether this descent datum comes from the restriction of an actual global object is effective descent for objects, and in the above categorical equivalence it corresponds to essential surjectivity. Since essential surjectivity does not follow from full faithfulness alone, being able to glue morphisms does not by itself allow one to glue objects. This transports the descent datum of [\[Schemes\] §Faithfully Flat Descent, ⁋Definition 4](/en/math/scheme_theory/faithfully_flat_descent#def4){: data-lid="nqy0f" } to an arbitrary CFG.

To this end, let us fix the notation to be used in the next definition. For a given covering family $\{f_i: U_i \rightarrow U\}_{i\in I}$, we write

$$U_{ij}=U_i\times_U U_j,\qquad U_{ijk}=U_i\times_U U_j\times_U U_k$$

and so on, and denote the pullback along a projection $\pr: U_{ij} \rightarrow U_i$ etc. by $\vert_{U_{ij}}$.

::: Definition 11
Suppose a CFG $P:\mathcal{F} \rightarrow \mathcal{C}$ and a covering family $\{f_i: U_i \rightarrow U\}_{i\in I}$ are given. A *descent datum* for this covering consists of

1. for each $i$, an object $x_i\in \mathcal{F}(U_i)$,
2. for each pair $(i, j)$, an isomorphism in $\mathcal{F}(U_{ij})$, $\varphi_{ij}: x_j\vert_{U_{ij}}\xrightarrow{\sim}x_i\vert_{U_{ij}}$,

satisfying, over $U_{ijk}$, the *cocycle condition* $\varphi_{ik}\vert_{U_{ijk}}=\varphi_{ij}\vert_{U_{ijk}}\circ \varphi_{jk}\vert_{U_{ijk}}$.
:::

As with descent for schemes, if there exist an object $x\in \mathcal{F}(U)$ and isomorphisms $\psi_i: x\vert_{U_i}\rightarrow x_i$ such that over each $U_{ij}$, $\varphi_{ij}\circ(\psi_j\vert_{U_{ij}})=\psi_i\vert_{U_{ij}}$ holds, this is called *effective* descent. That is, when these are glued together through the descent datum, an actually existing object $x$ is obtained. In faithfully flat descent, descent data for modules were always effective ([\[Schemes\] §Faithfully Flat Descent, ⁋Theorem 6](/en/math/scheme_theory/faithfully_flat_descent#thm6){: data-lid="48acc" }), but for a general CFG, effectivity is a separate condition. Combining these two conditions defines a stack.

::: Definition 12
Over a site $(\mathcal{C}, \tau)$, for a CFG $P:\mathcal{F} \rightarrow \mathcal{C}$,

1. $\mathcal{F}$ is a *prestack* if, for any $U$ and $x, y\in \mathcal{F}(U)$, the presheaf $\rIsom_U(x, y)$ is a sheaf on $\mathcal{C}_{/U}$. ([§Grothendieck Topologies, ⁋Definition 9](/en/math/stacks/grothendieck_topology#def9){: data-lid="tnyyr" })
2. $\mathcal{F}$ is a *stack* if $\mathcal{F}$ is a prestack and at the same time every descent datum for any covering family is effective.
:::

By [Theorem 8](#thm8){: data-lid="d58tn" }, if we consider the pseudofunctor corresponding to $\mathcal{F}$, $F:\mathcal{C}^\op\rightarrow\Grpd$, Definition 12 can be expressed as a single equivalence condition. Fix a covering $\mathcal{U}=\{U_i\rightarrow U\}$, and write $\Desc_F(\mathcal{U})$ for the groupoid whose objects are the descent data of [Definition 11](#def11){: data-lid="lbxrq" }. A morphism between two descent data $(x_i,\varphi_{ij})$ and $(y_i,\psi_{ij})$ is a family of local morphisms $\theta_i:x_i\rightarrow y_i$ satisfying $\psi_{ij}\circ\theta_j=\theta_i\circ\varphi_{ij}$ on each overlap.

Restricting a global object $x\in F(U)$ to each $U_i$ and using the canonical comparison isomorphisms of the pseudofunctor on double overlaps produces a descent datum. Hence the restriction functor

$$F(U)\rightarrow\Desc_F(\mathcal{U})$$

is defined. The stack condition of Definition 12 is equivalent to this functor being an equivalence of groupoids for every covering $\mathcal{U}$. That this functor is fully faithful is the prestack condition that local morphisms glue uniquely into a global morphism, and that it is essentially surjective is the condition that every descent datum is effective.

Thus a stack, summarized in one sentence, is a $\Grpd$-valued sheaf over a site, or more precisely, a sheaf in the 2-categorical sense. In particular, when the target is $\Set$ as for an ordinary set-valued moduli functor, each fiber is a discrete groupoid, so the above equivalence condition reduces to the ordinary sheaf condition. The following proposition expresses this precisely.

::: Proposition 13
Suppose that for a CFG $P:\mathcal{F} \rightarrow \mathcal{C}$, every fiber $\mathcal{F}(U)$ is a discrete groupoid. Then $\mathcal{F}$ corresponds to some presheaf $F:\mathcal{C}^\op \rightarrow \Set$, and in this case $\mathcal{F}$ being a prestack is equivalent to $F$ being a separated presheaf, and $\mathcal{F}$ being a stack is equivalent to $F$ being a sheaf.
:::
::: Proof
Since the fibers are discrete, the pseudofunctor of [Theorem 8](#thm8){: data-lid="f8f0r" } is a strict functor $F:\mathcal{C}^\op \rightarrow \Set$ (viewing $\Set$ as the category of discrete groupoids). For two objects $x, y\in \mathcal{F}(U)=F(U)$, the set $\Hom_{\mathcal{F}(V)}(x\vert_V, y\vert_V)$ is a one-element set if $x\vert_V=y\vert_V$ and empty otherwise. Hence $\rIsom_U(x, y)$ being a sheaf means that if $x, y$ agree on each $U_i$ of a covering (with the gluing condition holding vacuously), then they agree on $U$; that is, the uniqueness of amalgamations in $F$. ([§Grothendieck Topologies, ⁋Definition 9](/en/math/stacks/grothendieck_topology#def9){: data-lid="i58cr" })

Next, consider effective descent. In discrete fibers, every isomorphism $\varphi_{ij}$ can only be the identity, so a descent datum is merely that satisfying $x_i\vert_{U_{ij}}=x_j\vert_{U_{ij}}$, namely a family $(x_i)$, that is, a matching family of $F$. Its effectivity is equivalent to the existence of an amalgamation $x\in F(U)$. Hence every descent datum being effective means every matching family of $F$ has an amalgamation, and combined with the prestack condition this is exactly the sheaf condition. ([§Grothendieck Topologies, ⁋Proposition 10](/en/math/stacks/grothendieck_topology#prop10){: data-lid="2jffk" })
:::

From this we obtain the following corollary, which is important in our development.

::: Corollary 14
Suppose the site $(\mathcal{C}, \tau)$ is subcanonical. Then for any object $X\in\mathcal{C}$, the functor of points $h_X$ is a sheaf, and the corresponding representable CFG $\mathcal{C}_{/X}$ is a stack.
:::
::: Proof
Being subcanonical means that every representable presheaf $h_X$ is a sheaf. Hence it suffices to apply [Proposition 13](#prop13){: data-lid="3o3pm" } to the $\mathcal{C}_{/X}$ of [Example 9](#ex9){: data-lid="0w65l" }.
:::

By [§Grothendieck Topologies, ⁋Theorem 14](/en/math/stacks/grothendieck_topology#thm14){: data-lid="fr57a" }, the corollary above applies in particular to the fpqc site. In other words, the functor of points built from any scheme is a sheaf, and the corresponding CFG is a stack. More generally, by [Proposition 13](#prop13){: data-lid="st33h" }, if a set-valued presheaf $F$ is a sheaf, then viewing each $F(U)$ as a discrete groupoid yields a stack. That is, for moduli problems without automorphisms, the results we have examined so far apply almost for free.

## Examples of Stacks

We now construct concrete stacks. The most fundamental example is the quasi-coherent sheaf CFG of [Example 9](#ex9){: data-lid="7umnk" }; the fact that it is a stack is a direct translation of faithfully flat descent.

::: Theorem 15
Take the base site to be the fpqc site on $\Sch$ (or $\Sch_{/S}$). ([\[Schemes\] §Faithfully Flat Descent, ⁋Definition 9](/en/math/scheme_theory/faithfully_flat_descent#def9){: data-lid="atezg" }) Then the quasi-coherent sheaf CFG $\mathcal{QCoh}$ of [Example 9](#ex9){: data-lid="apoj5" } is a stack.
:::
::: Proof
We reduce the prestack condition and effectivity in turn to faithfully flat descent. Both conditions concern fpqc coverings, and by choosing a finite subcover using quasi-compactness and taking the disjoint union, the problem reduces to the case of a single affine faithfully flat morphism $\Spec B \rightarrow \Spec A$.

First, we prove the prestack condition. For two quasi-coherent sheaves $\mathcal{F}, \mathcal{G}$ on $T=\Spec A$, that is, two $A$-modules $M, N$, we must show that the presheaf $\rIsom_T(\mathcal{F}, \mathcal{G})$ is a sheaf. For this it suffices to show that the homomorphism presheaf

$$(\Spec A' \rightarrow \Spec A)\mapsto \Hom_{A'}(M\otimes_A A', N\otimes_A A')$$

is a sheaf. This is because the isomorphism presheaf is the subsheaf cut out by the condition that homomorphisms in both directions compose to the identity. Now, since the faithfully flat descent functor $\rMod{A} \rightarrow \Desc(B/A)$ is a categorical equivalence ([\[Schemes\] §Faithfully Flat Descent, ⁋Theorem 6](/en/math/scheme_theory/faithfully_flat_descent#thm6){: data-lid="tby9o" }), it is in particular fully faithful. ([\[Category Theory\] §Functor, ⁋Definition 10](/en/math/category_theory/functors#def10){: data-lid="5swb6" }) Full faithfulness precisely gives that homomorphisms descend uniquely along the covering $\{\Spec B \rightarrow \Spec A\}$, that is, the sheaf condition for the $\Hom$ presheaf.

For effectivity, a descent datum over a covering family $\{T_i \rightarrow T\}$ consists of data of a quasi-coherent sheaf $\mathcal{F}_i$ on each $T_i$ and cocycle isomorphisms $\varphi_{ij}$ over $T_{ij}$. This is precisely a descent datum for quasi-coherent sheaves, and since quasi-coherent sheaves have effective descent with respect to the fpqc topology ([\[Schemes\] §Faithfully Flat Descent, ⁋Theorem 11](/en/math/scheme_theory/faithfully_flat_descent#thm11){: data-lid="v91b0" }), this glues uniquely into a quasi-coherent sheaf $\mathcal{F}$ on $T$ together with isomorphisms $\mathcal{F}\vert_{T_i}\cong \mathcal{F}_i$. Therefore every descent datum is effective, and together with the prestack condition, $\mathcal{QCoh}$ is a stack.
:::

[Theorem 15](#thm15){: data-lid="hr17k" } explicitly demonstrates once again the principle we saw above: that is, the prestack condition reduces to the full faithfulness of [\[Schemes\] §Faithfully Flat Descent, ⁋Theorem 6](/en/math/scheme_theory/faithfully_flat_descent#thm6){: data-lid="7viro" }, and effectivity reduces to the effective descent of [\[Schemes\] §Faithfully Flat Descent, ⁋Theorem 11](/en/math/scheme_theory/faithfully_flat_descent#thm11){: data-lid="ffz9a" }, respectively.

On the other hand, not every CFG is a stack, so we need an operation that universally completes a prestack into a stack. This is stackification, the stack version of the sheafification of [§Grothendieck Topologies, ⁋Theorem 12](/en/math/stacks/grothendieck_topology#thm12){: data-lid="rjuh9" }.

::: Theorem 16 (Stackification)
Over a site $(\mathcal{C}, \tau)$, for any CFG $\mathcal{F}$, there exist a stack $\mathcal{F}^a$ and a morphism $\iota:\mathcal{F} \rightarrow \mathcal{F}^a$ with the following universal property: for any stack $\mathcal{G}$, composition with $\iota$

$$\Hom(\mathcal{F}^a, \mathcal{G})\xrightarrow{\ \sim\ }\Hom(\mathcal{F}, \mathcal{G})$$

is an equivalence of categories. In other words, the 2-category of stacks is a reflective subcategory of the 2-category of CFGs, and $\iota$ is its unit.
:::

As with its origin [§Grothendieck Topologies, ⁋Theorem 12](/en/math/stacks/grothendieck_topology#thm12){: data-lid="yq9y2" }, the proof is quite long, so we omit it. In any case, this is the 2-categorical version of the sheafification adjunction, and the key point is that just as sheafification was the left adjoint sending presheaves to sheaves, stackification is the 2-categorical reflection sending CFGs to stacks. Thanks to this operation, we can freely write down a moduli problem as a CFG first and then, if necessary, stackify it to turn it into an object for which descent holds.

Meanwhile, it is time to wrap up the example from the introduction.

::: Definition 17
Suppose given a site $(\mathcal{C}, \tau)$, a sheaf of groups $G$ on it, and an object $T\in \mathcal{C}$. Over $T$, a *$G$-torsor* (or *principal $G$-bundle*) is, on $\mathcal{C}_{/T}$, a sheaf $P$ together with a left action $G\vert_T\times P \rightarrow P$ that admits, over some covering $\{T_i \rightarrow T\}$, a $G\vert_{T_i}$-equivariant isomorphism

$$P\vert_{T_i}\cong G\vert_{T_i}$$

Here, the right-hand side carries the left translation action of $G\vert_{T_i}$. A morphism between two $G$-torsors is a $G$-equivariant sheaf morphism, and over $T$, the $G$-torsors form a groupoid $\bB G(T)$. The CFG defined by the correspondence $T\mapsto \bB G(T)$ is written as the *classifying stack* $\bB G$.
:::

Comparing the local trivializations $P\vert_{T_i}\cong G\vert_{T_i}$ yields, over $T_{ij}$, $G$-valued transition data $g_{ij}\in G(T_{ij})$, which form a cocycle. The trivial torsor $G\vert_T$ is an object of $\bB G(T)$, and its automorphism group is $\Aut_{\bB G(T)}(G\vert_T)\cong G(T)$. In other words, $\bB G$ remembers the group $G$ as automorphisms even on the trivial torsor, and the isomorphism classes of $\bB G(T)$ are classified by $H^1(T, G)$. The most important case is $G=\mathbb{G}_m$; this is the classification of line bundles anticipated in [Example 2](#ex2){: data-lid="6lgz6" }.

::: Theorem 18
On the fpqc site over $\Sch$ (or $\Sch_{/S}$), the classifying stack of $\mathbb{G}_m$-torsors $\bB\mathbb{G}_m$ is equivalent to the CFG whose fiber over $T$ is the groupoid $\mathcal{L}(T)$ of line bundles, and this CFG is a stack.
:::
::: Proof
First, the equivalence between $\mathbb{G}_m$-torsors and line bundles was seen in [\[Schemes\] §Group Schemes, ⁋Example 15](/en/math/scheme_theory/group_schemes#ex15){: data-lid="5p6cn" }. Under the frame torsor construction, isomorphisms between line bundles and $\mathbb{G}_m$-equivariant isomorphisms between frame torsors correspond to each other, and this correspondence is compatible with base change. Therefore, for each $T$, the groupoids $\bB\mathbb{G}_m(T)$ and $\mathcal{L}(T)$ are equivalent, and the two CFGs are also equivalent.

We now show that the line bundle CFG $\mathcal{L}$ is a stack. It is the full sub-CFG of $\mathcal{QCoh}$ consisting only of invertible sheaves. Therefore, the Isom presheaf between two line bundles $\mathcal{E}, \mathcal{F}\in\mathcal{L}(T)$ is equal to the presheaf computed in $\mathcal{QCoh}$, $\rIsom_T(\mathcal{E}, \mathcal{F})$. By [Theorem 15](#thm15){: data-lid="5ngpx" }, this presheaf is a sheaf, so $\mathcal{L}$ is a prestack.

Next, we check object descent. Suppose that over a covering family $\{T_i \rightarrow T\}$, line bundles $\mathcal{L}_i$ and isomorphisms $\varphi_{ij}$ over the overlaps form a descent datum. By [Theorem 15](#thm15){: data-lid="6drh8" }, there exist a quasi-coherent sheaf $\mathcal{F}$ realizing this datum and isomorphisms $\mathcal{F}\vert_{T_i}\cong \mathcal{L}_i$. By [\[Schemes\] §Faithfully Flat Descent, ⁋Proposition 7](/en/math/scheme_theory/faithfully_flat_descent#prop7){: data-lid="cay8q" }, the property of being locally free of rank $1$ descends along fpqc coverings, so $\mathcal{F}$ is also invertible. Therefore, every descent datum is effective inside $\mathcal{L}(T)$, and $\mathcal{L}\cong \bB\mathbb{G}_m$ is a stack.
:::

---

**References**

**[FGA]** B. Fantechi, L. Göttsche, L. Illusie, S. Kleiman, N. Nitsure, A. Vistoli, *Fundamental algebraic geometry: Grothendieck's FGA explained*. Mathematical Surveys and Monographs, American Mathematical Society, 2005.  
**[Stacks]** The Stacks Project Authors, *The Stacks Project*. Available [online](https://stacks.math.columbia.edu/).
