---
title: "Monoid Object"
description: "A monoid object is an object in a monoidal category defined by multiplication and unit morphisms. It categorically unifies diverse algebraic structures ranging from ordinary monoids to topological monoids, associative algebras, and differential graded algebras."
excerpt: "Monoid objects in a monoidal category and their examples"

categories: [Math / Category Theory]
permalink: /en/math/category_theory/monoid_objects
sidebar: 
    nav: "category_theory-en"

date: 2024-06-14
weight: 7
translated_at: 2026-08-19T17:15:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-03T11:15:05+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
## Monoid Objects

We can now define a monoid object.

::: Definition 1
In a monoidal category $(\mathcal{A},\otimes, I)$, a *monoid object* is given by the following data:
- an object $M$,
- a *multiplication* $\mu:M\otimes M \rightarrow M$,
- a *unit* $\eta:I \rightarrow M$.
These satisfy the following conditions.

- (Associativity)[^1]
{% diagram Math/Category_Theory/Monoid_Objects-1.svg width="29.37em" alt="associativity" %}
- (Unit)
{% diagram Math/Category_Theory/Monoid_Objects-2.svg width="17.03em" alt="unit" %}
:::

Any monoidal category $(\mathcal{A},\otimes, I)$ always has a monoid object $I$. Also, if $M$ is a monoid object in a symmetric monoidal category, one can easily verify that $M\otimes M$ is also a monoid object.

::: Example 2
The following are all examples of monoid objects.

- In the cartesian monoidal category $\Set$, a monoid object is a monoid in the usual sense.
- A monoid object in $\Top$ is a *topological monoid*.
- For any commutative ring $A$, a monoid object in $(\lMod{A},\otimes_A, A)$ is an associative unital $A$-algebra.
- For any commutative ring $A$, a monoid object in $(\Ch(A),\otimes_A, A)$ is a differential graded $A$-algebra. Here the unit $A$ is the chain complex where degree $0$ has $A$ and all other degrees are $0$.
:::

We need to explain the above examples not from the perspective of category theory, but in the algebraic language we already know.

First, in the case of the first example, that a monoid object in $\Set$, $(M,\mu,\eta)$, can be thought of as an ordinary monoid means the following. The underlying set of the monoid $M$ is $M$, and via the multiplication $\mu:M\times M \rightarrow M$, an operation on $M$ is defined. Meanwhile, since the terminal object in $\Set$ is a singleton, the image of the unit $\eta$ in $M$ will be a single element of $M$, which can be regarded as the unit of the monoid. Similarly, the second example can also be explained.

To examine the third example, it is good to first look at the symmetric monoidal category structure of $\lMod{A}$. Unlike cartesian monoidal categories, the monoidal product in $\lMod{A}$ is given not by the categorical product but by the tensor product, and therefore the unit object is also not a terminal object, but $A$. As for the unitors, whenever an $A$-module $M$ is given, $\lambda_M$ is the isomorphism determined by

$$\lambda_M: A\otimes M \rightarrow M;\quad a\otimes m\mapsto am$$

and similarly, $\rho_M$ is, via $m\otimes a\mapsto am$, the uniquely determined $A$-linear map.

Any object of $\lMod{A}$ already has an addition structure. A monoid object in $\lMod{A}$, $(M,\mu,\eta)$, can be understood as giving $M$, in addition to its existing addition structure, a multiplication structure compatible with this addition structure, and in this way $M$ becomes an $A$-algebra. Here, the fact that the addition and multiplication structures are compatible, that is, that things such as the distributive laws hold, is obtained from the fact that there is a one-to-one correspondence between an arbitrary map $M\otimes M \rightarrow M$ that is $A$-linear and a map from $M\times M$ to $M$ that is $A$-bilinear.

The last thing remaining in order to give a multiplication structure to $M$ is an identity element for this multiplication, and this information can be determined from $\eta:A \rightarrow M$. Considering the left $A$-module structure defined on $A$, the information contained in $\eta$ is precisely equivalent to $\eta(1)$, and this element $\eta(1)\in M$ serves as the identity element for the newly defined multiplication.

This is because

$$\mu(\eta(1)\otimes m)=\mu((\eta\otimes\id_M)(1\otimes m))=\lambda_M(1\otimes m)=m$$

and similarly, using the right unitor, one can also show that $\mu(m\otimes\eta(1))=m$.

For any monoidal category $\mathcal{A}$, one can also define morphisms between monoid objects defined on it, and thus can also consider the category of monoid objects. However, we will not define the category of monoid objects in this direction.

## Group Objects

Similarly to the previous definition, we can define a group object. To do this, just as when defining a monoid object, we need to express each property of a group as a diagram. A group $(G, \mu, e,(-)^{-1})$ satisfies precisely the following conditions.

- $(G,\mu,e)$ is a monoid.
- $(-)^{-1}:G \rightarrow G$ satisfies, for all $g\in G$, the following equation:

  $$\mu(g^{-1},g)=\mu(g,g^{-1})=e$$

However, there is a problem in translating this into the language of monoidal categories. If we write the second condition as a diagram, it should be

{% diagram Math/Category_Theory/Monoid_Objects-3.svg width="9.69em" alt="group_axiom" %}

where $e_G$ is the group homomorphism sending every element of $G$ to the identity element of $G$, and $((-)^{-1},\id_G)$ is the morphism jointly determined by the two maps $(-)^{-1}:G \rightarrow G$ and $\id_G:G \rightarrow G$, that is, the map sending an element $g$ to $(g^{-1},g)$. Of course, one could add both pieces of data and call this a group object, but that would not be a good solution because, for example, the unit $\eta:I \rightarrow G$ (as a monoid object) and the newly defined morphism $e_G$ would have no relation to each other.

However, if the original category were not just a monoidal category, but a cartesian monoidal category, all these problems are resolved cleanly. First, $e_G$ is given by the composition

$$G\overset{\epsilon_G}{\longrightarrow}\{e\}\overset{\eta}{\longrightarrow}G$$

where $\epsilon_G$ is the unique morphism from $G$ to the terminal object $\{e\}$, and $\eta$ is the unit of $G$ as a monoid object. Furthermore, in a cartesian monoidal category, since the monoidal product is the categorical product, via the following diagram

{% diagram Math/Category_Theory/Monoid_Objects-4.svg width="11.93em" alt="inverse_morphism" %}

$((-)^{-1},\id_G)$ is well-defined.

::: Definition 3
For a cartesian monoidal category $(\mathcal{A},\times, I)$, a *group object* in this category is given by the following data:
- an object $G$,
- a *multiplication* $\mu:G\times G \rightarrow G$,
- a *unit* $\eta:I \rightarrow G$,
- an *inverse* $\iota:G \rightarrow G$.

Letting $e_G$ be the composite $G\rightarrow I\overset{\eta}{\rightarrow}G$, these satisfy the following conditions.

- (Associativity) The following diagram
  {% diagram Math/Category_Theory/Monoid_Objects-5.svg width="12.13em" alt="associative_group_law" %}
  commutes.
- (Unit element) The following diagram
  {% diagram Math/Category_Theory/Monoid_Objects-6.svg width="11.81em" alt="identity_element" %}
  commutes. 
- (Inverse element) The following diagram
  {% diagram Math/Category_Theory/Monoid_Objects-7.svg width="11.08em" alt="inverse_element" %}
  commutes.
:::

Since [Definition 3](#def3){: data-lid="8hyeh" } started from a cartesian monoidal category, by using the universal property of the categorical product we could draw the diagrams omitting the associator and unitors as above. If we write them all out, the first two diagrams are precisely the conditions for a monoid object, and the last condition can be seen as newly added.

::: Example 4
The following are all group objects.

- A group object in $\Set$ is a group.
- A group object in $\Top$ is a topological group.
- A group object in $\Man^\infty$ is a Lie group.
- A group object in $\Var$ is an algebraic group.
- A group object in $\Sch$ is a group scheme.
- A group object in $\Grp$ is an abelian group.
:::

Only the last example may look slightly less obvious, but this follows from the condition that the multiplication $\mu:G\times G \rightarrow G$ must be a group homomorphism. Since the terminal object of $\Grp$ is the trivial group, the image of the unit $\eta$ is the identity element $e$ of $G$, and by the second condition of [Definition 3](#def3){: data-lid="zzp4i" }, $e$ is also the identity element for $\mu$. On the other hand, since the operation on $G\times G$ is given componentwise, the fact that $\mu$ is a group homomorphism means that $\mu(xz,yw)=\mu(x,y)\mu(z,w)$ holds for arbitrary $x,y,z,w\in G$, which is precisely the interchange law between $\mu$ and the original product of $G$. Since two operations sharing the same identity element satisfy the interchange law, the Eckmann–Hilton argument implies that $\mu$ coincides with the original product and this product is commutative.

## Hopf monoid

Looking at what was needed to formulate [Definition 3](#def3){: data-lid="n0xkl" } above, what we need is precisely the diagonal map $\Delta: G \rightarrow G\otimes G$, the augmentation map $G \rightarrow I$, and the inverse map $\iota: G \rightarrow G$. Sorting out what is needed here, we can first define the following.

::: Definition 5
Let a monoidal category $(\mathcal{A},\otimes,I)$ be given. An object $M$ of $\mathcal{A}$ is a *comonoid* if $M$ is a monoid object in $\mathcal{A}^\op$.
:::

Unpacking this, the data contained in a comonoid consists of a *comultiplication* $\Delta: M \rightarrow M\otimes M$ and a *counit* $\epsilon:M \rightarrow I$, and these satisfy the dual versions of the two conditions of [Definition 1](#def1){: data-lid="egwxw" }.

::: Definition 6
Let a symmetric monoidal category $(\mathcal{A},\otimes,I)$ be given. Then $(M,\mu,\eta,\Delta,\epsilon)$ is a *bimonoid* if the following hold.

- $(M,\mu,\eta)$ is a monoid object.
- $(M,\Delta,\epsilon)$ is a comonoid.
- The comultiplication and counit are both monoid morphisms.
:::

When a monoid object $M$ is given, because the role of symmetry is important in giving $M\otimes M$ a monoid structure, the notion of a bimonoid is generally defined only in a symmetric monoidal category. We now define a Hopf monoid as follows.

::: Definition 7
In a symmetric monoidal category $(\mathcal{A},\otimes,I)$, $(H,\mu,\eta,\Delta,\epsilon,\iota)$ is a *Hopf monoid* if $(H,\mu,\eta,\Delta,\epsilon)$ is a bimonoid and $\iota$ satisfies the same condition as the last diagram of [Definition 3](#def3){: data-lid="13tfg" }.
:::

To write the condition on $\iota$ explicitly, we need to translate the entire diagram given in [Definition 3](#def3){: data-lid="m2rzb" } into the data that a Hopf monoid possesses; for instance, one of the triangles can be expanded as the following diagram

{% diagram Math/Category_Theory/Monoid_Objects-8.svg width="14.39em" alt="Hopf_inverse" %}

and similarly, using $\iota\otimes\id_H$, one obtains the other triangle.

::: Example 8
The following are all examples of Hopf monoids.

- Any monoid object in a cartesian monoidal category naturally carries a bimonoid structure, and hence all group objects in any cartesian monoidal category are Hopf monoids.
- A Hopf monoid in $\Vect$ is a Hopf algebra.
:::

---

**References**

**[nLab]** nLab. *Monoidal category*. ([Link](https://ncatlab.org/nlab/show/monoidal+category))  
**[Rie]** Emily Riehl. *Category Theory in Context*. Dover Publications, 2016.

---

[^1]: In the diagram for the associativity of a monoid that we examined for motivation in the previous post, $(M\times M)\times M$ and $M\times(M\times M)$ were regarded as the same, so the diagram was a square; here, however, $(M\otimes M)\otimes M$ and $M\otimes(M\otimes M)$ are different objects, so it became a pentagon.
