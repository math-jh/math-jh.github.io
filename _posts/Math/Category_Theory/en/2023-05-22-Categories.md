---
title: "Category"
description: "We introduce the definition of a category in terms of objects, morphisms, and composition, and examine the associativity and identity conditions. Through concrete examples such as the category of sets, we show how various mathematical structures are described in the language of categories."
excerpt: "Definition and basic concepts of categories"

categories: [Math / Category Theory]
permalink: /en/math/category_theory/categories
sidebar: 
    nav: "category_theory-en"

date: 2023-05-22
weight: 1
translated_at: 2026-08-18T02:18:58+00:00
translation_source: kimi-cli
---
Basically, any field that is a branch of mathematics has certain concepts that it naturally possesses. The *objects* we wish to study and the *morphisms* between these objects are such examples. Category theory is the study of abstracting such structures, so specific theorems from each field can serve as examples in category theory. However, this does not mean that we must study all these fields in order to study category theory; our goal is to study category theory as dryly as possible, and to study most examples separately when we study the corresponding fields.

## Definition and Examples of Categories

::: Definition 1
A *category* $\mathcal{A}$ consists of the following data.

- A collection $\obj(\mathcal{A})$ of *objects*,
- A collection $\Hom_\mathcal{A}(A_1,A_2)$ of *morphisms* from *domain* $A_1\in\obj(\mathcal{A})$ to *codomain* $A_2\in\obj(\mathcal{A})$,
- The *composition* of two morphisms $f\in\Hom_\mathcal{A}(A_1,A_2)$, $g\in\Hom_\mathcal{A}(A_2,A_3)$

  $$\circ:\Hom_\mathcal{A}(A_1,A_2)\times\Hom_\mathcal{A}(A_2,A_3)\rightarrow\Hom_\mathcal{A}(A_1,A_3);\qquad (f,g)\mapsto g\circ f$$

Additionally, these satisfy the following conditions.

- Composition of morphisms is associative. That is, $(f\circ g)\circ h=f\circ(g\circ h)$ holds.
- For each $A\in\obj(\mathcal{A})$, there exists $\id_A\in\Hom_\mathcal{A}(A,A)$ such that for all $f\in\Hom_\mathcal{A}(A,A_1)$ and all $g\in\Hom_\mathcal{A}(A_2,A)$,

  $$f\circ{\id_A}=f,\qquad {\id_A}\circ g=g$$

  hold.
:::

Many things we have known so far can be written in this language. For example, the category $\Set$ of sets consists of the following data.

- The objects of $\Set$ are sets.
- For two objects $A_1,A_2\in\obj(\Set)$, a morphism from $A_1$ to $A_2$ is a function from the set $A_1$ to $A_2$. ([\[Set Theory\] §Functions, ⁋Definition 1](/en/math/set_theory/functions#def1))
- The composition of two morphisms is defined as the composition of functions. ([\[Set Theory\] §Operations on Functions, ⁋Proposition 1](/en/math/set_theory/operation_of_functions#prop1)) That this composition is associative was examined in [\[Set Theory\] §Operations on Binary Relations, ⁋Proposition 5](/en/math/set_theory/operation_of_binary_relations#prop5).
- For any object $A\in\obj(\Set)$, $\id_A\in\Hom_\Set(A,A)$ is the identity function $\id_A$. ([\[Set Theory\] §Functions, ⁋Definition 2](/en/math/set_theory/functions#def2)) That the identity function satisfies the two conditions of [Definition 1](#def1) was examined after [\[Set Theory\] §Operations on Binary Relations, ⁋Definition 9](/en/math/set_theory/operation_of_binary_relations#def9).

One point to be careful about is that the definition of a function quoted above requires the domain to be non-empty. As it stands, for any set $B$, $\Hom_\Set(\emptyset,B)$ would be empty, and $\id_\emptyset$ would not exist. Henceforth, we agree that for any $B$, the triple $(\emptyset,\emptyset,B)$ is also a function from $\emptyset$ to $B$; then this becomes the unique function from $\emptyset$ to $B$, and we obtain $\id_\emptyset$.

In a similar manner, we can see that the following are all examples of categories.

::: Example 2 (Concrete categories)
The following are all examples of categories.

- The category $\Set$ of sets and functions
- The category $\Mon$ of monoids and monoid homomorphisms
- The category $\Grp$ of groups and group homomorphisms
- The category $\Ab$ of abelian groups and group homomorphisms
- The category $\Ring$ of rings and ring homomorphisms
- The category $\Field$ of fields and field homomorphisms
- The categories $\lset{G},\rset{G}$ of left, right $G$-sets and $G$-set homomorphisms
- The categories $\lMod{R},\rMod{R}$ of left, right $R$-modules and $R$-module homomorphisms
- The category $\Vect_k$ of $k$-vector spaces and linear maps
- The category $\FVect_k$ of finite-dimensional $k$-vector spaces and linear maps
- The category $\Top$ of topological spaces and continuous functions
- The category $\Man^k$ of $C^k$-manifolds and $C^k$-maps
- The category $\Ch(R)$ of chain complexes of $R$-modules and chain maps
- The category $\Set_\ast$ of pointed sets and pointed functions
- The category $\Top_\ast$ of pointed topological spaces and pointed continuous maps

Here, a pointed set means a pair $(S,x)$ where $S$ is a set and $x$ is a fixed element of $S$, and a pointed function from $(S,x)$ to $(S',x')$ is an $f:S \rightarrow S'$ satisfying $f(x)=x'$. Similarly, one can define pointed topological spaces and pointed continuous maps.
:::

In all the categories in the example above, the objects are sets endowed with additional structure. A category of this form is called a *concrete category*. Among categories, there are also many that are not concrete categories.

::: Example 3
Any preordered set $(S,\preceq)$ can be regarded as a category through the following process. ([\[Set Theory\] §Definition of Order Relations, ⁋Definition 7](/en/math/set_theory/order_relations#def7))

- $\obj(S)=S$.
- For any $x,y\in S$, if $x\preceq y$ then there exists a unique morphism $x \rightarrow y$, and otherwise $\Hom_S(x,y)$ is empty.

The composition of two morphisms $x \rightarrow y$ and $y \rightarrow z$ is given by the morphism $x \rightarrow z$. The existence of this morphism $x \rightarrow z$ comes from the transitivity of $\preceq$. Then associativity follows from

$$((x \rightarrow y) \rightarrow z)\rightarrow w=x \rightarrow y \rightarrow z \rightarrow w=x \rightarrow (y \rightarrow (z \rightarrow w)).$$

Also, by the reflexivity of $\preceq$, for any $x\in S$, $\Hom_S(x,x)$ has a unique morphism $x \rightarrow x$, and one can check that this plays the role of $\id_x$.
:::

The reason we called $\obj(\mathcal{A})$ a *collection* of objects rather than a *set* in the previous definition is that this collection may not actually be a set. Usually, we call such objects a *class*. Every set is a class, but among classes there exist ones that are not sets.

::: Definition 4
Let a category $\mathcal{A}$ be given.

- $\mathcal{A}$ is called a *small category* if the collection $\Hom(\mathcal{A})$ of all morphisms belonging to $\mathcal{A}$ is a set.
- $\mathcal{A}$ is called a *locally small category* if for any fixed objects $A_1,A_2\in\mathcal{A}$, $\Hom_\mathcal{A}(A_1,A_2)$ is a set.
:::

By definition, any small category is also locally small. Moreover, for any small category $\mathcal{A}$, $\obj(\mathcal{A})$ is necessarily a set. This is because for any $A\in\obj(\mathcal{A})$, $\id_A$ is always a morphism of $\mathcal{A}$, and thus we can regard $\obj(\mathcal{A})$ as a subset of the set $\Hom(\mathcal{A})$.

When introducing examples, we did not worry about this point, and we will not do so in the future either. However, for safety, we assume that all categories appearing hereafter are locally small.

::: Definition 5
For a category $\mathcal{C}$, a *subcategory* of $\mathcal{C}$ is data consisting of a subcollection of the objects and morphisms of $\mathcal{C}$ that inherits the composition and identities of $\mathcal{C}$ and itself forms a category.
:::

## Isomorphisms

Generally, after we learn about mathematical objects, we concern ourselves with when these objects can be regarded as the same.

::: Definition 6
Let an arbitrary category $\mathcal{A}$ be given, and let $A_1,A_2\in\obj(\mathcal{A})$. We say that $A_1$ and $A_2$ are *isomorphic* if there exist $f\in\Hom_\mathcal{A}(A_1,A_2)$, $g\in\Hom_\mathcal{A}(A_2,A_1)$ satisfying the two conditions

$$f\circ g=\id_{A_2},\qquad g\circ f=\id_{A_1}.$$

In this case, we call $f$ and $g$ *isomorphisms* and call each of them the *inverse* of the other.
:::

In the situation of the above definition, suppose there exists another $g'\in\Hom_\mathcal{A}(A_2,A_1)$ satisfying the two conditions

$$f\circ g'=\id_{A_2},\qquad g'\circ f=\id_{A_1}.$$

Then from

$$g=g\circ\id_{A_2}=g\circ(f\circ g')=(g\circ f)\circ g'=\id_{A_1}\circ g'=g'$$

we know that $g=g'$. Therefore, given any $f\in\Hom_\mathcal{A}(A_1,A_2)$, if there exists a $g\in\Hom_\mathcal{A}(A_2,A_1)$ satisfying the two conditions of [Definition 6](#def6), it is unique, and hence we can write it as $g=f^{-1}$.

In many examples, an isomorphism is the same as a bijective morphism, but this is not always the case. ([\[Topology\] §Continuous Functions, ⁋Example 5](/en/math/topology/continuous_functions#ex5)) In the first place, there is no guarantee that morphisms in an arbitrary category are necessarily functions, so it does not even make sense to say that a morphism is a bijection. Instead, we define the following.

::: Definition 7
Consider a category $\mathcal{A}$ and a morphism $f:A_1\rightarrow A_2$.

- $f$ is called a *monomorphism* if for any two morphisms $g_1,g_2:A_0\rightarrow A_1$, $f\circ g_1=f\circ g_2$ implies $g_1=g_2$.
- $f$ is called an *epimorphism* if for any two morphisms $h_1,h_2:A_2\rightarrow A_3$, $h_1\circ f=h_2\circ f$ implies $h_1=h_2$.
- $f$ is called a *bimorphism* if $f$ is both a monomorphism and an epimorphism.
:::

::: Proposition 8
Any isomorphism is a bimorphism.
:::
::: Proof
Assume that $f:A_1\rightarrow A_2$ is an isomorphism. If $g_1,g_2:A_0\rightarrow A_1$ satisfy $f\circ g_1=f\circ g_2$, then from the following equation

$$g_1=\id_{A_1}\circ g_1=(f^{-1}\circ f)\circ g_1=f^{-1}\circ(f\circ g_1)=f^{-1}\circ(f\circ g_2)=\id_{A_1}\circ g_2=g_2$$

we know that $f$ is a monomorphism. By the same argument, $f$ is also an epimorphism, and therefore $f$ is a bimorphism.
:::

## $\End(A)$ and $\Aut(A)$

Let an arbitrary category $\mathcal{A}$ be given. For two morphisms $f\in\Hom_\mathcal{A}(A_1,A_2)$, $g\in\Hom_\mathcal{A}(A_3,A_4)$, the composition $g\circ f$ is well-defined only if $A_2=A_3$. That is, not every two morphisms in a category $\mathcal{A}$ are always composable.

On the other hand, for a fixed $A\in\obj(\mathcal{A})$, the elements of $\Hom_\mathcal{A}(A,A)$ all have domain and codomain equal to $A$, so they can be composed as much as desired. We call such elements *endomorphisms*, and in particular, an endomorphism that is an isomorphism is called an *automorphism*. As explained above, $\Hom_\mathcal{A}(A,A)$ can be thought of not merely as a set, but as an algebraic structure with a specific operation $\circ$.

::: Definition 9
Fix an arbitrary category $\mathcal{A}$ and an object $A\in\obj(\mathcal{A})$.

- The *endomorphism monoid* of $A$ is the data consisting of the set $\End_\mathcal{A}(A)=\Hom_\mathcal{A}(A,A)$ and the composition $\circ$.
- The *automorphism group* of $A$ is the data consisting of the set $\Aut_\mathcal{A}(A)$, which collects only the isomorphisms among the elements of $\End_\mathcal{A}(A)$, and the composition $\circ$.
:::

It is not difficult to see that $\End(A)$ and $\Aut(A)$ satisfy the conditions of the algebraically defined monoid and group. ([\[Algebraic Structures\] §Semigroups, Monoids, and Groups, ⁋Definition 3](/en/math/algebraic_structures/groups#def3) and [§Semigroups, Monoids, and Groups, ⁋Definition 11](/en/math/algebraic_structures/groups#def11)) In category theory, monoid and group can be defined as follows.

::: Definition 10
A category with only one object is called a *monoid*. A monoid in which every morphism is an isomorphism is called a *group*.
:::

More generally, we can define the following.

::: Definition 11
A category in which every morphism is an isomorphism is called a *groupoid*.
:::

This simply means that all the properties of a group hold, but instead of the group operation being defined for all elements, it suffices for it to be defined only for certain pairs of elements.

## Examples of Categories

We now examine methods of constructing new categories from existing ones.

::: Example 12
Let two categories $\mathcal{A},\mathcal{B}$ be given. Their *product category* $\mathcal{A}\times \mathcal{B}$ consists of the following data.

- The objects of $\obj(\mathcal{A}\times \mathcal{B})$ are pairs $(A,B)$ for $A\in\obj(\mathcal{A}),B\in\obj(\mathcal{B})$.
- For any $(A_1,B_1),(A_2,B_2)\in\obj(\mathcal{A}\times \mathcal{B})$, $\Hom_{\mathcal{A}\times \mathcal{B}}((A_1,B_1),(A_2,B_2))$ consists of pairs $(f,g)$ for $f\in\Hom_\mathcal{A}(A_1,A_2),g\in\Hom_\mathcal{B}(B_1,B_2)$.
- For any $(A,B)\in\obj(\mathcal{A}\times \mathcal{B})$, the identity at $(A,B)$ is given by $(\id_A,\id_B)$.
- For any $(f_1,g_1):(A_1,B_1)\rightarrow(A_2,B_2)$, $(f_2,g_2):(A_2,B_2)\rightarrow(A_3,B_3)$, their composition is given by $(f_2\circ f_1,g_2\circ g_1)\in\Hom((A_1,B_1),(A_3,B_3))$.
:::

::: Example 13
Let a category $\mathcal{A}$ be given, and fix $A\in\obj(\mathcal{A})$.

- The *slice category over $A$* $\mathcal{A}_{/A}$ of $\mathcal{A}$ is given by the following data.
  - The objects of $\mathcal{A}_{/A}$ are morphisms $f:A_1\rightarrow A$ in $\mathcal{A}$.
  - For any $(A_1\overset{f_1}{\longrightarrow}A)\in\obj(\mathcal{A}_{/A})$ and $(A_2\overset{f_2}{\longrightarrow}A)\in\obj(\mathcal{A}_{/A})$, a morphism from $f_1$ to $f_2$ is a $g:A_1\rightarrow A_2$ such that $f_1=f_2\circ g$ holds.
- The *slice category under $A$* ${}_{A/}\mathcal{A}$ of $\mathcal{A}$ is given by the following data.
  - The objects of ${}_{A/}\mathcal{A}$ are morphisms $f:A\rightarrow A_1$ in $\mathcal{A}$.
  - For any $(A\overset{f_1}{\longrightarrow}A_1)\in\obj({}_{A/}\mathcal{A})$ and $(A\overset{f_2}{\longrightarrow}A_2)\in\obj({}_{A/}\mathcal{A})$, a morphism from $f_1$ to $f_2$ is a $g:A_1\rightarrow A_2$ such that $f_2=g\circ f_1$ holds.
:::

---

**References**

**[Rie]** Emily Riehl. *Category Theory in Context*. Dover Publications, 2016.

---
