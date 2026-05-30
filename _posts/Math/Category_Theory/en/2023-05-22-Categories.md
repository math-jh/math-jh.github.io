---
title: "Categories"
description: "We introduce the definition of a category in terms of objects, morphisms, and composition, and examine the conditions of associativity and identity morphisms. Through concrete examples including the category of sets, we show how diverse mathematical structures are described in the language of categories."
excerpt: "Definitions and basic concepts of category theory"

categories: [Math / Category Theory]
permalink: /en/math/category_theory/categories
header:
    overlay_image: /assets/images/Math/Category_Theory/Categories.png
    overlay_filter: 0.5
sidebar: 
    nav: "category_theory-en"

date: 2023-05-22
last_modified_at: 2023-05-28
weight: 1
translated_at: 2026-05-30T11:30:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-30T11:30:04+00:00
---
Whenever a subject is a branch of mathematics, there are certain notions it naturally possesses. The *objects* we wish to study, and the *morphisms* between these objects, are such examples. Since category theory is the study of this structure in the abstract, specific theorems from each field can serve as examples in category theory. However, this does not mean we must study all these fields before learning category theory; our goal is to study category theory as dryly as possible, leaving most examples to be examined separately when studying the corresponding fields.

## Definition and Examples of Categories

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A *Category* $$\mathcal{A}$$ consists of the following data.

- A collection $$\obj(\mathcal{A})$$ of *objects*,
- A collection $$\Hom_\mathcal{A}(A_1,A_2)$$ of *morphisms* from a *domain* $$A_1\in\obj(\mathcal{A})$$ to a *codomain* $$A_2\in\obj(\mathcal{A})$$,
- A *composition* of two morphisms $$f\in\Hom_\mathcal{A}(A_1,A_2)$$, $$g\in\Hom_\mathcal{A}(A_2,A_3)$$

  $$\circ:\Hom_\mathcal{A}(A_1,A_2)\times\Hom_\mathcal{A}(A_2,A_3)\rightarrow\Hom_\mathcal{A}(A_1,A_3);\qquad (f,g)\mapsto g\circ f$$

In addition, these satisfy the following conditions.

- Composition of morphisms is associative. That is, $$(f\circ g)\circ h=f\circ(g\circ h)$$ holds.
- For each $$A\in\obj(\mathcal{A})$$, there exists $$\id_A\in\Hom_\mathcal{A}(A,A)$$ such that for all $$f\in\Hom_\mathcal{A}(A,A_1)$$ and all $$g\in\Hom_\mathcal{A}(A_2,A)$$,

  $$f\circ{\id_A}=f,\qquad {\id_A}\circ g=g$$

  hold.

</div>

Much of what we have known so far can be written in this language. For instance, the category $$\Set$$ of sets consists of the following data.

- The objects of $$\Set$$ are sets.
- For two objects $$A_1,A_2\in\obj(\mathcal{A})$$, a morphism from $$A_1$$ to $$A_2$$ is a function from the set $$A_1$$ to $$A_2$$. ([[Set Theory] §Functions, ⁋Definition 1](/en/math/set_theory/functions#def1))
- Composition of two morphisms is defined as composition of functions. ([[Set Theory] §Operations of Functions, ⁋Proposition 1](/en/math/set_theory/operation_of_functions#prop1)) That this composition is associative was seen in [[Set Theory] §Operations of Binary Relations, ⁋Proposition 5](/en/math/set_theory/operation_of_binary_relations#prop5).
- For any object $$A\in\obj(\mathcal{A})$$, $$\id_A\in\Hom_\Set(A,A)$$ is the identity function $$\id_A$$. ([[Set Theory] §Functions, ⁋Definition 2](/en/math/set_theory/functions#def2)) That the identity function satisfies the two conditions of [Definition 1](#def1) was seen after [[Set Theory] §Operations of Binary Relations, ⁋Definition 9](/en/math/set_theory/operation_of_binary_relations#def9).

In a similar manner, the following can all be seen to be examples of categories.

<div class="example" markdown="1">

<ins id="ex2">**Example 2 (Concrete categories)**</ins> The following are all examples of categories.

- The category $$\Set$$ of sets and functions
- The category $$\Mon$$ of monoids and monoid homomorphisms
- The category $$\Grp$$ of groups and group homomorphisms
- The category $$\Ab$$ of abelian groups and group homomorphisms
- The category $$\Ring$$ of rings and ring homomorphisms
- The category $$\Field$$ of fields and field extensions
- The categories $$\lset{G},\rset{G}$$ of left, right $$G$$-sets and $$G$$-set homomorphisms
- The categories $$\lMod{R},\rMod{R}$$ of left, right $$R$$-modules and $$R$$-module homomorphisms
- The category $$\Vect_k$$ of $$k$$-vector spaces and linear maps
- The category $$\FVect_k$$ of finite-dimensional $$k$$-vector spaces and linear maps
- The category $$\Top$$ of topological spaces and continuous functions
- The category $$\Man^k$$ of $$C^k$$-manifolds and $$C^k$$-maps
- The category $$\Ch(R)$$ of chain complexes of $$R$$-modules and chain maps
- The category $$\Set_\ast$$ of pointed sets and pointed functions
- The category $$\Top_\ast$$ of pointed topological spaces and pointed continuous maps

Here, a pointed set means a pair $$(S,x)$$ where $$S$$ is a set and $$x$$ is a fixed element of $$S$$, and a pointed function from $$(S,x)$$ to $$(S',x')$$ is a function $$f:S \rightarrow S'$$ satisfying $$f(x)=x'$$. Similarly, one can define pointed topological spaces and pointed continuous maps.

</div>

In all the categories above, the objects are sets endowed with additional structure. Such categories are called *concrete categories*. Among categories, there are also many that are not concrete categories.

<div class="example" markdown="1">

<ins id="ex3">**Example 3**</ins> Any preordered set $$(S,\preceq)$$ can be regarded as a category through the following process. ([[Set Theory] §Definition of Order Relations, ⁋Definition 7](/en/math/set_theory/order_relations#def7))

- $$\obj(S)=S$$.
- For any $$x,y\in S$$, if $$x\preceq y$$ then there exists a unique morphism $$x \rightarrow y$$, and otherwise $$\Hom_S(x,y)$$ is empty.

The composition of two morphisms $$x \rightarrow y$$ and $$y \rightarrow z$$ is given by the morphism $$x \rightarrow z$$. The existence of the morphism $$x \rightarrow z$$ comes from the transitivity of $$\preceq$$. Then associativity follows from

$$((x \rightarrow y) \rightarrow z)\rightarrow w=x \rightarrow y \rightarrow z \rightarrow y=x \rightarrow (y \rightarrow (z \rightarrow w))$$

Also, by the reflexivity of $$\preceq$$, for any $$x\in S$$, $$\Hom_\mathcal{S}(x,x)$$ contains the unique morphism $$x \rightarrow x$$, and one can verify that this plays the role of $$\id_x$$.

</div>

In the preceding definition, we referred to $$\obj(\mathcal{A})$$ as a *collection* of objects rather than a *set* because this collection may not actually be a set. Usually, such collections are called *classes*. Every set is a class, but among classes there exist ones that are not sets.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> Let a category $$\mathcal{A}$$ be given.

- $$\mathcal{A}$$ is called a *small category* if the collection $$\Hom(\mathcal{A})$$ of all morphisms belonging to $$\mathcal{A}$$ is a set.
- $$\mathcal{A}$$ is called a *locally small category* if for any fixed objects $$A_1,A_2\in\mathcal{A}$$, $$\Hom_\mathcal{A}(A_1,A_2)$$ is a set.

</div>

By definition, any small category is also locally small. Moreover, for any small category $$\mathcal{A}$$, $$\obj(\mathcal{A})$$ is necessarily a set. This is because for any $$A\in\obj(\mathcal{A})$$, $$\id_A$$ is always a morphism of $$\mathcal{A}$$, and thus $$\obj(\mathcal{A})$$ can be regarded as a subset of the set $$\Hom(\mathcal{A})$$.

When introducing examples, we did not worry about this point, and we will not do so in the future either. However, for safety, we assume that all categories appearing from now on are locally small.

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> For a category $$\mathcal{C}$$, a *subcategory* of $$\mathcal{C}$$ is data consisting of a subcollection of the objects and morphisms of $$\mathcal{C}$$ that itself forms a category.

</div>

## Isomorphisms

Generally, after learning about mathematical objects, we care about when these objects can be regarded as the same.

<div class="definition" markdown="1">

<ins id="def6">**Definition 6**</ins> Let an arbitrary category $$\mathcal{A}$$ be given, and let $$A_1,A_2\in\obj(\mathcal{A})$$. We say that $$A_1$$ and $$A_2$$ are *isomorphic* if there exist $$f\in\Hom_\mathcal{A}(A_1,A_2)$$, $$g\in\Hom_\mathcal{A}(A_2,A_1)$$ satisfying the two conditions

$$f\circ g=\id_{A_2},\qquad g\circ f=\id_{A_1}$$

In this case, we call $$f$$ and $$g$$ *isomorphisms* and call each an *inverse* of the other.

</div>

In the situation of the above definition, suppose there exists another $$g'\in\Hom_\mathcal{A}(A_2,A_1)$$ satisfying the two conditions

$$f\circ g'=\id_{A_2},\qquad g'\circ f=\id_{A_1}$$

Then from

$$g=g\circ\id_{A_2}=g\circ(f\circ g')=(g\circ f)\circ g'=\id_{A_1}\circ g'=g'$$

we see that $$g=g'$$. Thus, given any $$f\in\Hom_\mathcal{A}(A_1,A_2)$$, if there exists $$g\in\Hom_\mathcal{A}(A_2,A_1)$$ satisfying the two conditions of [Definition 8](#def8), it is unique, and therefore we may write $$g=f^{-1}$$.

In many examples, an isomorphism is the same as a bijective morphism, but this is not always the case. ([[Topology] §Continuous Functions, ⁋Example 5](/en/math/topology/continuous_functions#ex5)) After all, there is no guarantee that morphisms in an arbitrary category are functions, so it does not even make sense to say that a morphism is a bijection. Instead, we define the following.

<div class="definition" markdown="1">

<ins id="def7">**Definition 7**</ins> Consider a category $$\mathcal{A}$$ and a morphism $$f:A_1\rightarrow A_2$$.

- $$f$$ is a *monomorphism* if for any two morphisms $$g_1,g_2:A_0\rightarrow A_1$$, whenever $$f\circ g_1=f\circ g_2$$ holds, then $$g_1=g_2$$ holds.
- $$f$$ is an *epimorphism* if for any two morphisms $$h_1,h_2:A_2\rightarrow A_3$$, whenever $$h_1\circ f=h_2\circ f$$ holds, then $$h_1=h_2$$ holds.
- $$f$$ is a *bimorphism* if $$f$$ is both a monomorphism and an epimorphism.

</div>

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8**</ins> Any isomorphism is a bimorphism.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Suppose $$f:A_1\rightarrow A_2$$ is an isomorphism. If $$g_1,g_2:A_0\rightarrow A_1$$ satisfy $$f\circ g_1=f\circ g_2$$, then from the following equation

$$g_1=\id_{A_1}\circ g_1=(f^{-1}\circ f)\circ g_1=f^{-1}\circ(f\circ g_1)=f^{-1}\circ(f\circ g_2)=\id_{A_1}\circ g_2=g_2$$

we see that $$f$$ is a monomorphism. By the same argument, $$f$$ is also an epimorphism, and therefore $$f$$ is a bimorphism.

</details>

## $$\End(A)$$ and $$\Aut(A)$$

Let an arbitrary category $$\mathcal{A}$$ be given. For two morphisms $$f\in\Hom_\mathcal{A}(A_1,A_2)$$, $$g\in\Hom_\mathcal{A}(A_3,A_4)$$, the composition $$g\circ f$$ is well-defined only when $$A_2=A_3$$. That is, not every pair of morphisms in a category $$\mathcal{A}$$ can be composed.

On the other hand, for a fixed $$A\in\obj(\mathcal{A})$$, the elements of $$\Hom_\mathcal{A}(A,A)$$ all have domain and codomain equal to $$A$$, so they can be composed as much as we like. Such elements are called *endomorphisms*, and in particular, endomorphisms that are isomorphisms are called *automorphisms*. As explained above, $$\Hom_\mathcal{A}(A,A)$$ can be thought of not merely as a set, but as an algebraic structure equipped with a specific operation $$\circ$$.

<div class="definition" markdown="1">

<ins id="def9">**Definition 9**</ins> Fix an arbitrary category $$\mathcal{A}$$ and an object $$A\in\obj(\mathcal{A})$$.

- The *endomorphism monoid* of $$A$$ is the data consisting of the set $$\End_\mathcal{A}(A)=\Hom_\mathcal{A}(A,A)$$ and the composition $$\circ$$.
- The *automorphism group* of $$A$$ is the data consisting of the set $$\Aut_\mathcal{A}(A)$$, which collects only the isomorphisms among the elements of $$\End_\mathcal{A}(A)$$, and the composition $$\circ$$.

</div>

It is not difficult to see that $$\End(A)$$ and $$\Aut(A)$$ satisfy the conditions of the algebraically defined monoid and group. ([[Algebraic Structures] §Semigroups, Monoids, Groups, ⁋Definition 3](/en/math/algebraic_structures/groups#def3) and [Semigroups, Monoids, and Groups, ⁋Definition 11](/en/math/algebraic_structures/groups#def11)) In category theory, monoids and groups can be defined as follows.

<div class="definition" markdown="1">

<ins id="def10">**Definition 10**</ins> A category with only one object is called a *monoid*. A monoid in which every morphism is an isomorphism is called a *group*.

</div>

More generally, we can define the following.

<div class="definition" markdown="1">

<ins id="def11">**Definition 11**</ins> A category in which every morphism is an isomorphism is called a *groupoid*.

</div>

This simply means that all the properties of a group hold, except that the group operation need only be defined for certain pairs of elements rather than for all elements.

## Examples of Categories

Now we examine ways to construct new categories from existing ones.

<div class="example" markdown="1">

<ins id="ex12">**Example 12**</ins> Let two categories $$\mathcal{A},\mathcal{B}$$ be given. Their *product category* $$\mathcal{A}\times \mathcal{B}$$ consists of the following data.

- The objects of $$\obj(\mathcal{A}\times \mathcal{B})$$ are pairs $$(A,B)$$.
- For any $$(A_1,B_1),(A_2,B_2)\in\obj(\mathcal{A}\times \mathcal{B})$$, the morphisms $$\Hom_{\mathcal{A}\times \mathcal{B}}((A_1,B_1),(A_2,B_2))$$ are of the form $$(f,g)$$ for $$f\in\Hom_\mathcal{A}(A_1,A_2),g\in\Hom_\mathcal{B}(B_1,B_2)$$.
- For any $$A\times B\in \mathcal{A}\times \mathcal{B}$$, the identity at $$A\times B$$ is given by $$(\id_A,\id_B)$$.
- For any $$(f_1,g_1):(A_1,B_1)\rightarrow(A_2,B_2)$$, $$(f_2,g_2):(A_2,B_2)\rightarrow(A_3,B_3)$$, their composition is given by $$(f_2\circ f_1,g_2\circ g_1)\in\Hom((A_1,B_1),(A_3,B_3))$$.

</div>

<div class="example" markdown="1">

<ins id="ex13">**Example 13**</ins> Let a category $$\mathcal{A}$$ be given, and fix $$A\in\obj(\mathcal{A})$$.

- The *slice category over $$A$$* $$A_{/\mathcal{A}}$$ of $$\mathcal{A}$$ is given by the following data.
  - The objects of $$\mathcal{A}_{/A}$$ are morphisms $$f:A_1\rightarrow A$$ in $$\mathcal{A}$$.
  - For any $$(A_1\overset{f_1}{\longrightarrow}A)\in\obj(\mathcal{A}_{/A})$$ and $$(A_2\overset{f_2}{\longrightarrow}A)\in\obj(\mathcal{A}_{/A})$$, a morphism from $$f_1$$ to $$f_2$$ is a morphism $$g:A_1\rightarrow A_2$$ such that $$f_1=g\circ f_2$$ holds.
- The *slice category under $$A$$* $${}_{A/}\mathcal{A}$$ of $$\mathcal{A}$$ is given by the following data.
  - The objects of $${}_{A/}\mathcal{A}$$ are morphisms $$f:A\rightarrow A_1$$ in $$\mathcal{A}$$.
  - For any $$(A\overset{f_1}{\longrightarrow}A_1)\in\obj({}_{A/}\mathcal{A})$$ and $$(A\overset{f_2}{\longrightarrow}A_2)\in\obj({}_{A/}\mathcal{A})$$, a morphism from $$f_1$$ to $$f_2$$ is a morphism $$g:A_1\rightarrow A_2$$ such that $$f_2=g\circ f_1$$ holds.

</div>

---

**References**

**[Rie]** Emily Riehl. *Category Theory in Context*. Dover Publications, 2016.

---
