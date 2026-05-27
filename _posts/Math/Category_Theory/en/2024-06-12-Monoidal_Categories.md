---title: "Monoidal Categories"
excerpt: "The definition of monoidal categories and coherence conditions"

categories: [Math / Category Theory]
permalink: /en/math/category_theory/monoidal_categories
header:
    overlay_image: /assets/images/Math/Category_Theory/Monoidal_Categories.png
    overlay_filter: 0.5
sidebar: 
    nav: "category_theory-en"

date: 2024-06-12
last_modified_at: 2024-06-12
weight: 7
translated_at: 2026-05-28T11:36:15+00:00
translation_source: kimi-cli
---
Posts in the category theory category are basically written so that they can be understood by reading only the posts in the [\[Set Theory\]](/en/set_theory/) category, and although the monoidal categories covered in this post could have been written in that way as well, the first part of this post in particular draws on posts from the [\[Algebraic Structures\]](/en/algebraic_structures) category to aid understanding.

In this post and the next, we examine monoidal categories and monoidal objects defined within them. Roughly speaking, a monoid object is an object in some category that has properties similar to the algebraically defined monoid; to say that it has properties similar to a monoid, this category must be a monoidal category. Therefore, we first briefly review what a monoid was algebraically, and then consider how this story can be rewritten in the language of categories.

## Monoid

We decided to call an associative unital magma a *monoid*. ([\[Algebraic Structures\] §Semigroups, Monoids, Groups, ⁋Definition 3](/en/math/algebraic_structures/groups#def3)) Unpacking this, the statement that $$M$$ is a monoid means the following.

> There exists a binary operation $$\mu:M\times M \rightarrow M$$ defined on $$M$$, and an element $$e\in M$$ of $$M$$, such that
>
> 1. (Associativity) For any $$a,b,c\in M$$, $$\mu(\mu(a,b),c)=\mu(a,\mu(b, c))$$ holds.
> 2. (Unit element) $$e\in M$$ satisfies $$a\cdot e=e\cdot a=a$$ for any $$a\in M$$.

However, these conditions can each be expressed as commutative diagrams. First, for associativity, the following diagram commuting means the same thing.

![Associativity](/assets/images/Math/Category_Theory/Monoidal_Categories-1.png){:style="width:12.6em" class="invert" .align-center}

This is natural because if we pick an arbitrary element $$(a,b,c)$$ from the set in the upper left, proceeding in the $$\urcorner$$ direction gives

$$\mu(\mu(a,b),c)=\mu(a\cdot b,c)=(a\cdot b)\cdot c$$

and similarly, proceeding in the $$\llcorner$$ direction gives

$$\mu(a,\mu(b,c))=\mu(a,b\cdot c)=a\cdot(b\cdot c)$$

and the fact that this diagram commutes means precisely that these two elements of $$M$$ are equal.

Similarly, for the identity element $$e$$, using the set $$I=\{e\}$$ and the inclusion $$i:I\hookrightarrow M$$, the following diagram

![Unit_element](/assets/images/Math/Category_Theory/Monoidal_Categories-2.png){:style="width:14.8em" class="invert" .align-center}

can be written as commuting.

In category theory, it is impossible to extract elements from an object. Therefore, the definition of a monoid examined at the very beginning is unsuitable for explanation using category theory. However, if everything is represented as diagrams as above, this can be lifted appropriately into the language of categories. To do this, we must first define what the $$M\times M$$ we used naturally is.[^1]

## Monoidal Categories

Simply put, a monoidal category is a category equipped with a monoid operation among objects, that is, an operation that is associative and has an identity element. For example, we will soon see that the $$\times$$ used when defining a monoid at the very beginning makes $$\Set$$ a monoidal category.

Before giving the definition, recall that in the two diagrams defining a monoid, $$M\times(M\times M)$$ and $$(M\times M)\times M$$ are different sets, and $$M$$, $$I\times M$$, and $$M\times I$$ are also different sets. They are certainly distinct sets; it is only that natural isomorphisms exist among them.

<div class="definition" markdown="1">

<ins id="def5">**Definition 5 (Monoidal category)**</ins> A *monoidal category* consists of data $$(\mathcal{A},\otimes, I)$$. Here $$\mathcal{A}$$ is a category, $$I\in\obj(\mathcal{A})$$, and $$\otimes:\mathcal{A}\times \mathcal{A}\rightarrow \mathcal{A}$$ is a bifunctor. They satisfy the following conditions.

1. There exists a natural isomorphism between the two functors $$-\otimes(-\otimes-)$$ and $$(-\otimes-)\otimes-$$ from $$\mathcal{A}\times \mathcal{A}\times \mathcal{A}$$ to $$\mathcal{A}$$

    $$\alpha_{A,B,C}:A\otimes(B\otimes C)\rightarrow (A\otimes B)\otimes C$$

    This is called the *associator*.
2. There exist natural isomorphisms among the three functors $$I\otimes-$$, $$-\otimes I$$, and $$\id_\mathcal{A}$$ from $$\mathcal{A}$$ to $$\mathcal{A}$$

    $$\lambda_A:I\otimes A\rightarrow A,\qquad \rho_A:A\otimes I\rightarrow A$$

    They are called the *left unitor* and *right unitor*, respectively.
3. (Coherence condition) The following two diagrams both commute.

- (Associator)
  ![Pentagon_identity](/assets/images/Math/Category_Theory/Monoidal_Categories-3.png){:style="width:26em" class="invert" .align-center}
- (Unitor)
  ![unitor_diagram](/assets/images/Math/Category_Theory/Monoidal_Categories-4.png){:style="width:19em" class="invert" .align-center}

If the symmetric condition on $$\otimes$$ is additionally imposed on a monoidal category $$(\mathcal{A},\otimes,I)$$, it is called a *symmetric monoidal category*. This is expressed by a natural isomorphism (*symmetor*) $$\gamma_{AB}:A\otimes B \rightarrow B\otimes A$$ and the following additional coherence conditions

- (Associativity coherence)
  ![associativity_coherence](/assets/images/Math/Category_Theory/Monoidal_Categories-5.png){:style="width:24em" class="invert" .align-center}
- (Unit coherence)
  ![symmetor](/assets/images/Math/Category_Theory/Monoidal_Categories-6.png){:style="width:12.6em" class="invert" .align-center}
- (Inverse law)
  ![inverse](/assets/images/Math/Category_Theory/Monoidal_Categories-7.png){:style="width:12.6em" class="invert" .align-center}

</div>

If in a symmetric monoidal category, $$\gamma_{A,B}:A\otimes B\rightarrow B\otimes A$$ and $$\gamma_{B,A}:B\otimes A \rightarrow A\otimes B$$ are not inverses of each other, this is called a *braided monoidal category*.

The coherence conditions for the associator and unitors are used in the proof of Mac Lane's coherence theorem. Roughly speaking, this states that given a product $$A_1\otimes\cdots\otimes A_n$$ of $$n$$ objects, no matter which order we compute it in or (in the case of a symmetric monoidal category) no matter how we rearrange the order of the factors, the results are naturally isomorphic, and this is uniquely expressed as a composition of associators, unitors, and (in the case of a symmetric monoidal category) symmetors.

In any case, thanks to the coherence theorem, we know that the monoidal product does not depend on the order of computation or the order in which the objects are listed, so we need not pay as much attention to these natural isomorphisms.

<div class="example" markdown="1">

<ins id="ex6">**Example 6**</ins> The following are all examples of monoidal categories.

- Equipping $$\Set$$ with the usual product ([§Limits, ⁋Example 6](/en/math/category_theory/limits#ex6)) and taking $$I$$ to be any singleton makes $$\Set$$ a symmetric monoidal category.
- Equipping $$\Grp$$ with the usual product and taking $$I$$ to be the trivial group $$\{e\}$$ makes $$\Grp$$ a symmetric monoidal category.
- Giving $$\Top$$ the product structure via the product topology and taking $$I$$ to be any singleton makes $$\Top$$ a symmetric monoidal category.
- For any commutative ring $$R$$, the category $$\lMod{R}$$ of $$R$$-modules is a symmetric monoidal category under the tensor product $$\otimes$$.
- In particular, when $$R=k$$ the above example shows that $$\Vect_k$$ is a symmetric monoidal category, and when $$R=\mathbb{Z}$$ we see that $$\Ab$$ is a symmetric monoidal category.

</div>

The first two examples of [Example 6](#ex6) can be generalized. Let us first define the following.

<div class="definition" markdown="1">

<ins id="def7">**Definition 7**</ins> If every finite family of objects in a category $$\mathcal{A}$$ always has a categorical product, this category is called a *cartesian category*.

</div>

Then in the preceding examples, $$\Set$$ and $$\Grp$$ become cartesian categories. Likewise, $$\Top$$ and $$\Man^\infty$$, etc., are all cartesian categories.

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8**</ins> Any cartesian category carries the structure of a monoidal category.

</div>

Although quite a bit of elaboration is needed for the proof of this proposition, essentially it is enough to recall how $$(A\times B)\times C\cong A\times(B\times C)$$ and $$I\times M\cong M\cong M\times I$$ arise and then repeat the calculations. A monoidal category whose monoidal product is given by the product is called a *cartesian monoidal category*.

One difference between a cartesian monoidal category and a general monoidal category is that several natural morphisms are well defined. For instance, the diagonal morphism $$\Delta_X:X \rightarrow X\times X$$ and the augmentation morphism $$\epsilon_X:X \rightarrow I$$, which are not well defined in a general monoidal category, are well defined here. The morphism $$\epsilon_X$$ is defined naturally because $$I$$ is a terminal object, and $$\Delta_X$$ is obtained via the following diagram.

![diagonal_morphism](/assets/images/Math/Category_Theory/Monoidal_Categories-8.png){:style="width:12em" class="invert" .align-center}

This will be used when we treat group objects in the next post.

---

**References**

**[nLab]** nLab. *Monoidal category*. ([Link](https://ncatlab.org/nlab/show/monoidal+category))  
**[Rie]** Emily Riehl. *Category Theory in Context*. Dover Publications, 2016.

---

[^1]: Although we have previously defined the product of two categories, we have never defined the product of two objects inside a category.
