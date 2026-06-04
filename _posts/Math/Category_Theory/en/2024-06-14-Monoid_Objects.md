---
title: "Monoid Objects"
description: "A monoid object is defined in a monoidal category using a multiplication and a unit morphism. It provides a unified categorical framework for various algebraic structures, ranging from ordinary monoids and topological monoids to associative algebras and differential graded algebras."
excerpt: "Monoid objects in a monoidal category and their examples"

categories: [Math / Category Theory]
permalink: /en/math/category_theory/monoid_objects
sidebar: 
    nav: "category_theory-en"

date: 2024-06-14
last_modified_at: 2024-06-14
weight: 8
translated_at: 2026-05-30T15:00:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-30T15:00:04+00:00
---
## Monoid Objects

Now we can define monoid objects.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A *monoid object* in a monoidal category $$(\mathcal{A},\otimes, I)$$ consists of the following data:
- an object $$M$$,
- *multiplication* $$\mu:M\otimes M \rightarrow M$$,
- *unit* $$\eta:I \rightarrow M$$.

These satisfy the following conditions.

- (Associativity)[^1]
![associativity](/assets/images/Math/Category_Theory/Monoid_Objects-1.png){:style="width:26em" class="invert" .align-center}
- (Unit)
![unit](/assets/images/Math/Category_Theory/Monoid_Objects-2.png){:style="width:16.6em" class="invert" .align-center}

</div>

Any monoidal category $$(\mathcal{A},\otimes, I)$$ always has the monoid object $$I$$. Also, if $$M$$ is a monoid object in a symmetric monoidal category, then one can easily check that $$M\otimes M$$ is also a monoid object.

<div class="example" markdown="1">

<ins id="ex2">**Example 2**</ins> The following are all examples of monoid objects.

- In the cartesian monoidal category $$\Set$$, a monoid object is a monoid in the usual sense.
- In $$\Top$$, a monoid object is a *topological monoid*.
- For any commutative ring $$R$$, a monoid object in $$(\lMod{R},\otimes_R, R)$$ is an associative unital $$R$$-algebra.
- For any commutative ring $$R$$, a monoid object in $$(\Ch(R),\otimes_R, R)$$ is a differential graded $$R$$-algebra. Here the unit $$R$$ is the chain complex with $$R$$ in degree $$0$$ and $$0$$ in all other degrees.

</div>

We need to explain the above examples not from a categorical perspective, but in the algebraic language we already know.

For the first example, the fact that a monoid object $$(M,\mu,\eta)$$ in $$\Set$$ can be thought of as an ordinary monoid means the following. The underlying set of the monoid $$M$$ is $$M$$, and an operation on $$M$$ is defined via the multiplication $$\mu:M\times M \rightarrow M$$. Meanwhile, since the terminal object in $$\Set$$ is a singleton, the image of the unit $$\eta$$ in $$M$$ will be some element of $$M$$, which can be regarded as the unit of the monoid. The second example can be explained similarly.

To examine the third example, it is best to first look at the symmetric monoidal category structure of $$\lMod{R}$$. Unlike cartesian monoidal categories, the monoidal product in $$\lMod{R}$$ is given by the tensor product rather than the categorical product, and thus the unit object is not a terminal object but $$R$$. For the unitors, whenever an $$R$$-module $$M$$ is given, $$\lambda_M$$ is the isomorphism

$$\lambda_M: R\otimes M \rightarrow M;\quad r\otimes m\mapsto rm$$

determined by this formula, and similarly $$\rho_M$$ is the uniquely determined $$R$$-linear map given by $$m\otimes r\mapsto rm$$.

Every object of $$\lMod{R}$$ already carries an additive structure. A monoid object $$(M,\mu,\eta)$$ in $$\lMod{R}$$ can be understood as endowing $$M$$, which already has an additive structure, with a multiplicative structure compatible with this addition, and in this way $$M$$ becomes an $$R$$-algebra. Here, the compatibility of the additive and multiplicative structures—that is, the validity of distributivity and similar properties—follows from the existence of a one-to-one correspondence between arbitrary elements of $$M\otimes M \rightarrow M$$ and $$R$$-bilinear maps from $$M\times M$$ to $$M$$.

The last thing remaining to give $$M$$ a multiplicative structure is the identity element for this multiplication, and this information can be specified by $$\eta:R \rightarrow M$$. Considering the left $$R$$-module structure defined on $$R$$, the information encoded in $$\eta$$ is exactly equivalent to $$\eta(1)$$, and this element $$\eta(1)\in M$$ serves as the identity element for the newly defined multiplication:

$$\mu(\eta(1)\otimes m)=\mu((\eta\otimes\id_M)(1\otimes m))=\lambda_M(1\otimes m)=m$$

and similarly, using the right unitor one can also show $$\mu(m\otimes\eta(1))=m$$.

For any monoidal category $$\mathcal{A}$$, we can also define morphisms between monoid objects defined over it, and thus we can consider the category of monoid objects. However, we will not pursue the definition of a monoid category in this direction.

## Group Objects

As with the previous definition, we can define group objects. To do so, as was the case when defining monoid objects, we need to express each property of groups as a diagram. A group $$(G, \mu, e,(-)^{-1})$$ precisely satisfies the following conditions.

- $$(G,\mu,e)$$ is a monoid.
- $$(-)^{-1}:G \rightarrow G$$ satisfies, for all $$g\in G$$, the equation

  $$\mu(g^{-1},g)=\mu(g,g^{-1})=e$$

However, there is a problem if we try to translate this into the language of monoidal categories. If we write the second condition as a diagram,

![group_axiom](/assets/images/Math/Category_Theory/Monoid_Objects-3.png){:style="width:10em" class="invert" .align-center}

it should look as follows. Here $$e_G$$ is the group homomorphism sending every element of $$G$$ to the identity element of $$G$$, and $$(-1)^{-1}\times \id_G$$ is the product of the two maps $$(-)^{-1}:G \rightarrow G$$ and $$\id_G:G \rightarrow G$$. Of course one could add both pieces of data and call this a group object, but doing so would not be a good solution because, for example, the unit $$\eta:I \rightarrow G$$ (as a monoid object) and the newly defined morphism $$e_G$$ would be entirely unrelated.

But if the original category were not merely a monoidal category but a cartesian monoidal category, then all these problems would be neatly resolved. First, $$e_G$$ is given by the composition

$$G\overset{\epsilon_G}{\longrightarrow}\{e\}\overset{\eta}{\longrightarrow}G$$

where $$\epsilon_G$$ is the unique morphism from $$G$$ to the terminal object $$\{e\}$$, and $$\eta$$ is the unit of $$G$$ as a monoid object. Moreover, in a cartesian monoidal category the monoidal product is the categorical product, so the following diagram

![inverse_morphism](/assets/images/Math/Category_Theory/Monoid_Objects-4.png){:style="width:12.6em" class="invert" .align-center}

shows that $$(-1)^{-1}\times \id_G$$ is well defined.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> In a cartesian monoidal category $$(\mathcal{A},\times, I)$$, a *group object* consists of the following data:
- an object $$G$$,
- *multiplication* $$\mu:G\otimes G \rightarrow G$$,
- *unit* $$\eta:I \rightarrow G$$,
- *inverse* $$\iota:G \rightarrow G$$.

Let $$e_G$$ denote the composition $$G\rightarrow I\overset{\eta}{\rightarrow}G$$. These satisfy the following conditions.

- (Associativity) The following diagram
  ![associative_group_law](/assets/images/Math/Category_Theory/Monoid_Objects-5.png){:style="width:12em" class="invert" .align-center}
  commutes.
- (Unit element) The following diagram
  ![identity_element](/assets/images/Math/Category_Theory/Monoid_Objects-6.png){:style="width:11.6em" class="invert" .align-center}
  commutes.
- (Inverse element) The following diagram
  ![inverse_element](/assets/images/Math/Category_Theory/Monoid_Objects-7.png){:style="width:11.6em" class="invert" .align-center}
  commutes.

</div>

Since [Definition 3](#def3) started from a cartesian monoidal category, we were able to draw the diagrams as above using the universal property of the categorical product, omitting the associators and unitors. If we write them all out explicitly, the first two diagrams are exactly the conditions for a monoid object, and the last condition can be seen as the newly added one.

<div class="example" markdown="1">

<ins id="ex4">**Example 4**</ins> The following are all group objects.

- In $$\Set$$, a group object is a group.
- In $$\Top$$, a group object is a topological group.
- In $$\Man^\infty$$, a group object is a Lie group.
- In $$\Var$$, a group object is an algebraic group.
- In $$\Sch$$, a group object is a group scheme.
- In $$\Grp$$, a group object is an abelian group.

</div>

Only the last example may look slightly less obvious, but this can be verified by checking that since the inverse $$\iota$$ must be a group homomorphism, commutativity follows from this condition.

## Hopf Monoid

Looking at what was needed when constructing [Definition 3](#def3) above, what we needed was precisely the diagonal map $$\Delta: G \rightarrow G\otimes G$$, the augmentation map $$G \rightarrow I$$, and the inverse map $$I \rightarrow G$$. Sorting out what is needed here, we can first define the following.

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> Let a monoidal category $$(\mathcal{A},\otimes,I)$$ be given. An object $$M$$ of $$\mathcal{A}$$ is called a *comonoid* if $$M$$ is a monoid object in $$\mathcal{A}^\op$$.

</div>

Unpacking this, the data constituting a comonoid are *comultiplication* $$\Delta: G \rightarrow G\otimes G$$ and *counit* $$\epsilon:G \rightarrow I$$, and these satisfy the dual versions of the two conditions in [Definition 1](#def1).

<div class="definition" markdown="1">

<ins id="def6">**Definition 6**</ins> Let a symmetric monoidal category $$(\mathcal{A},\otimes,I)$$ be given. Then $$(M,\mu,\eta,\Delta,\epsilon)$$ is called a *bimonoid* if the following hold.

- $$(M,\mu,\eta)$$ is a monoid.
- $$(M,\Delta,\epsilon)$$ is a comonoid.
- The comultiplication and counit are both monoid morphisms.

</div>

When a monoid object $$M$$ is given, the role of the symmetry is important in order to give $$M\otimes M$$ a monoid structure, so generally the notion of a bimonoid is also defined only in a symmetric monoidal category. We now define a Hopf monoid as follows.

<div class="definition" markdown="1">

<ins id="def7">**Definition 7**</ins> In a symmetric monoidal category $$(\mathcal{A},\otimes,I)$$, $$(H,\mu,\eta,\Delta,\epsilon,\iota)$$ is called a *Hopf monoid* if $$(H,\mu,\eta,\Delta,\epsilon)$$ is a bimonoid and $$\iota$$ satisfies the same condition as the last diagram in [Definition 3](#def3).

</div>

To write the condition for $$\iota$$ explicitly, one must translate all the diagrams given in [Definition 3](#def3) into the information that a Hopf monoid carries; for example, one of the triangles is the following diagram

![Hopf_inverse](/assets/images/Math/Category_Theory/Monoid_Objects-8.png){:style="width:14em" class="invert" .align-center}

which can be written out explicitly, and similarly using $$\iota\otimes\id_H$$ one obtains the other triangle.

<div class="example" markdown="1">

<ins id="ex8">**Example 8**</ins> The following are all examples of Hopf monoids.

- Any monoid object in a cartesian monoidal category has a natural bimonoid structure, and thus every group object in a cartesian monoidal category is a Hopf monoid.
- In $$\Vect$$, a Hopf monoid is a Hopf algebra.

</div>

---

**References**

**[nLab]** nLab. *Monoidal category*. ([Link](https://ncatlab.org/nlab/show/monoidal+category))  
**[Rie]** Emily Riehl. *Category Theory in Context*. Dover Publications, 2016.

---

[^1]: In the diagram for the associativity of a monoid that we examined for motivation in a previous post, $$(M\times M)\times M$$ and $$M\times(M\times M)$$ were regarded as the same thing, so the diagram was a quadrilateral, but here $$(M\otimes M)\otimes M$$ and $$M\otimes(M\otimes M)$$ are different objects, so it becomes a pentagon.
[^2]: One might mistakenly think that the product of two morphisms comes from the product category, but when we multiply two morphisms $$f:G\rightarrow G$$ and $$g:G\rightarrow G$$, we get $$(f,g):G\times G \rightarrow G\times G$$. Applying the monoidal product $$\otimes$$ to the latter $$G\times G$$ can make the target of $$(f,g)$$ into $$G\otimes G$$, but
