---
title: "Monoid Objects"
description: "A monoid object is defined in a monoidal category by a multiplication and a unit morphism. It provides a unified categorical framework for diverse algebraic structures, including ordinary monoids, topological monoids, associative algebras, and differential graded algebras."
excerpt: "Monoid objects in monoidal categories and their examples"

categories: [Math / Category Theory]
permalink: /en/math/category_theory/monoid_objects
sidebar: 
    nav: "category_theory-en"

date: 2024-06-14
weight: 7
translated_at: 2026-08-19T17:15:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-08-19T17:15:04+00:00
---
## Monoid Objects

We can now define a monoid object.

::: Definition 1
In a monoidal category $(\mathcal{A},\otimes, I)$, a *monoid object* is given by the following data:
- an object $M$,
- a *multiplication* $\mu:M\otimes M \rightarrow M$,
- a *unit* $\eta:I \rightarrow M$.
These must satisfy the following conditions.

- (Associativity)[^1]
{% diagram Math/Category_Theory/Monoid_Objects-1.svg width="29.37em" alt="associativity" %}
- (Unit)
{% diagram Math/Category_Theory/Monoid_Objects-2.svg width="17.03em" alt="unit" %}
:::

For any monoidal category $(\mathcal{A},\otimes, I)$, the unit object $I$ is always a monoid object. Also, if $M$ is a monoid object in a symmetric monoidal category, then $M\otimes M$ is again a monoid object; this is easily verified.

::: Example 2
The following are all examples of monoid objects.

- In the cartesian monoidal category $\Set$, a monoid object is a monoid in the usual sense.
- In $\Top$, a monoid object is a *topological monoid*.
- For any commutative ring $A$, a monoid object in $(\lMod{A},\otimes_A, A)$ is an associative unital $A$-algebra.
- For any commutative ring $A$, a monoid object in $(\Ch(A),\otimes_A, A)$ is a differential graded $A$-algebra. Here the unit $A$ is the chain complex with $A$ in degree $0$ and $0$ in all other degrees.
:::

We need to explain the above examples not from the categorical perspective, but in the algebraic language we already know.

First, for the first example, the statement that a monoid object $(M,\mu,\eta)$ in $\Set$ can be thought of as an ordinary monoid means the following. The underlying set of the monoid $M$ is $M$, and an operation on $M$ is defined via the multiplication $\mu:M\times M \rightarrow M$. On the other hand, since the terminal object in $\Set$ is a singleton, the image of the unit $\eta$ in $M$ will be some single element of $M$, which can be regarded as the unit of the monoid. The second example can be explained similarly.

To examine the third example, it is helpful to first look at the symmetric monoidal category structure of $\lMod{A}$. Unlike cartesian monoidal categories, the monoidal product in $\lMod{A}$ is given not by the categorical product but by the tensor product, and hence the unit object is $A$ rather than a terminal object. As for the unitors, for each given $A$-module $M$, the left unitor $\lambda_M$ is the isomorphism determined by

$$\lambda_M: A\otimes M \rightarrow M;\quad a\otimes m\mapsto am,$$

and similarly $\rho_M$ is the uniquely determined $A$-linear map given by $m\otimes a\mapsto am$.

Every object of $\lMod{A}$ already carries an addition structure. A monoid object $(M,\mu,\eta)$ in $\lMod{A}$ can be understood as endowing $M$ with a multiplication structure compatible with its existing addition structure, and in this way $M$ becomes an $A$-algebra. The fact that the addition and multiplication structures are compatible, i.e., that distributivity and the like hold, follows from the one-to-one correspondence between arbitrary $A$-linear maps $M\otimes M \rightarrow M$ and $A$-bilinear maps $M\times M \rightarrow M$.

The last remaining piece to give $M$ a multiplication structure is an identity element for this multiplication, and this information can be specified by $\eta:A \rightarrow M$. Considering the left $A$-module structure defined on $A$, the information contained in $\eta$ is exactly equivalent to $\eta(1)$, and this element $\eta(1)\in M$ serves as the identity element for the newly defined multiplication:

$$\mu(\eta(1)\otimes m)=\mu((\eta\otimes\id_M)(1\otimes m))=\lambda_M(1\otimes m)=m,$$

and similarly using the right unitor one can show $\mu(m\otimes\eta(1))=m$.

For any monoidal category $\mathcal{A}$, we can also define morphisms between monoid objects defined over it, and thus we can consider the category of monoid objects. However, we will not pursue defining the category of monoid objects in this direction.

## Group Objects

Analogously to the above, we can define a group object. To do so, just as when defining a monoid object, we need to express each property of a group as a diagram. A group $(G, \mu, e,(-)^{-1})$ exactly satisfies the following conditions.

- $(G,\mu,e)$ is a monoid.
- $(-)^{-1}:G \rightarrow G$ satisfies the following equation for every $g\in G$:

  $$\mu(g^{-1},g)=\mu(g,g^{-1})=e.$$

However, there is a problem in translating this into the language of monoidal categories. If we try to write the second condition as a diagram, it would have to be

{% diagram Math/Category_Theory/Monoid_Objects-3.svg width="9.69em" alt="group_axiom" %}

where $e_G$ is the group homomorphism sending every element of $G$ to the identity element of $G$, and $((-)^{-1},\id_G)$ is the morphism determined jointly by the two maps $(-)^{-1}:G \rightarrow G$ and $\id_G:G \rightarrow G$, i.e., the map sending an element $g$ to $(g^{-1},g)$. Of course one could add both pieces of data and call this a group object, but that would not be a good solution because, for example, the unit $\eta:I \rightarrow G$ (as a monoid object) and the newly defined morphism $e_G$ would be completely unrelated.

But if the original category were not just a monoidal category but a cartesian monoidal category, all these problems are neatly resolved. First, $e_G$ is given by the following composite:

$$G\overset{\epsilon_G}{\longrightarrow}\{e\}\overset{\eta}{\longrightarrow}G.$$

Here $\epsilon_G$ is the unique morphism from $G$ to the terminal object $\{e\}$, and $\eta$ is the unit of $G$ as a monoid object. Moreover, since in a cartesian monoidal category the monoidal product is the categorical product, $((-)^{-1},\id_G)$ is well defined via the diagram

{% diagram Math/Category_Theory/Monoid_Objects-4.svg width="11.93em" alt="inverse_morphism" %}

::: Definition 3
For a cartesian monoidal category $(\mathcal{A},\times, I)$, a *group object* in this category is given by the following data:
- an object $G$,
- a *multiplication* $\mu:G\times G \rightarrow G$,
- a *unit* $\eta:I \rightarrow G$,
- an *inverse* $\iota:G \rightarrow G$.

Letting $e_G$ be the composite $G\rightarrow I\overset{\eta}{\rightarrow}G$, these must satisfy the following conditions.

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

Since [Definition 3](#def3) started from a cartesian monoidal category, we were able to draw the diagrams as above omitting the associator and unitors by using the universal property of the categorical product. If we wrote them all out explicitly, the first two diagrams are exactly the conditions for a monoid object, and the last condition can be regarded as the newly added one.

::: Example 4
The following are all group objects.

- A group object in $\Set$ is a group.
- A group object in $\Top$ is a topological group.
- A group object in $\Man^\infty$ is a Lie group.
- A group object in $\Var$ is an algebraic group.
- A group object in $\Sch$ is a group scheme.
- A group object in $\Grp$ is an abelian group.
:::

Only the last example may look slightly less obvious, but this follows from the condition that the multiplication $\mu:G\times G \rightarrow G$ must be a group homomorphism. Since the terminal object of $\Grp$ is the trivial group, the image of the unit $\eta$ is the identity element $e$ of $G$, and by the second condition of [Definition 3](#def3), $e$ is also the identity element for $\mu$. On the other hand, since the operation on $G\times G$ is given componentwise, the fact that $\mu$ is a group homomorphism means that $\mu(xz,yw)=\mu(x,y)\mu(z,w)$ holds for arbitrary $x,y,z,w\in G$, which is precisely the interchange law between $\mu$ and the original product of $G$. Since two operations sharing the same identity element satisfy the interchange law, the Eckmann–Hilton argument implies that $\mu$ coincides with the original product and this product is commutative.

## Hopf Monoid

Looking back at what was needed to make [Definition 3](#def3) above, what we needed was exactly the diagonal map $\Delta: G \rightarrow G\otimes G$, the augmentation map $G \rightarrow I$, and the inverse map $\iota: G \rightarrow G$. Sorting out what is needed here, we can first make the following definition.

::: Definition 5
Let a monoidal category $(\mathcal{A},\otimes,I)$ be given. We say that an object $M$ of $\mathcal{A}$ is a *comonoid* if $M$ is a monoid object in $\mathcal{A}^\op$.
:::

Unpacking this, the data contained in a comonoid consists of a *comultiplication* $\Delta: M \rightarrow M\otimes M$ and a *counit* $\epsilon:M \rightarrow I$, and these satisfy the dual versions of the two conditions of [Definition 1](#def1).

::: Definition 6
Let a symmetric monoidal category $(\mathcal{A},\otimes,I)$ be given. Then $(M,\mu,\eta,\Delta,\epsilon)$ is a *bimonoid* if the following hold.

- $(M,\mu,\eta)$ is a monoid object.
- $(M,\Delta,\epsilon)$ is a comonoid.
- The comultiplication and counit are both monoid morphisms.
:::

When a monoid object $M$ is given, the role of the symmetry is important in giving $M\otimes M$ a monoid structure, so the notion of a bimonoid is generally defined only in a symmetric monoidal category. We now define a Hopf monoid as follows.

::: Definition 7
In a symmetric monoidal category $(\mathcal{A},\otimes,I)$, $(H,\mu,\eta,\Delta,\epsilon,\iota)$ is a *Hopf monoid* if $(H,\mu,\eta,\Delta,\epsilon)$ is a bimonoid and $\iota$ satisfies the same condition as the last diagram of [Definition 3](#def3).
:::

To write the condition on $\iota$ explicitly, we need to translate all the diagrams given in [Definition 3](#def3) into the data that a Hopf monoid possesses; for instance, one of the triangles can be expanded as the diagram

{% diagram Math/Category_Theory/Monoid_Objects-8.svg width="14.39em" alt="Hopf_inverse" %}

and similarly, using $\iota\otimes\id_H$, one obtains the other triangle.

::: Example 8
The following are all examples of Hopf monoids.

- Any monoid object in a cartesian monoidal category naturally carries a bimonoid structure, and hence any group object in a cartesian monoidal category is a Hopf monoid.
- A Hopf monoid in $\Vect$ is a Hopf algebra.
:::

---

**References**

**[nLab]** nLab. *Monoidal category*. ([Link](https://ncatlab.org/nlab/show/monoidal+category))  
**[Rie]** Emily Riehl. *Category Theory in Context*. Dover Publications, 2016.

---

[^1]: In the diagram for the associativity of a monoid that we examined for motivation in the previous post, $(M\times M)\times M$ and $M\times(M\times M)$ were regarded as the same, so the diagram was a square; here, however, $(M\otimes M)\otimes M$ and $M\otimes(M\otimes M)$ are different objects, so it becomes a pentagon.
