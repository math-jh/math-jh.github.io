---

title: "Free Products"
excerpt: "Free product and universal property"

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/free_products
header:
    overlay_image: /assets/images/Math/Algebraic_Structures/Free_products.png
    overlay_filter: 0.5
sidebar:
    nav: "algebraic_structures-en"

date: 2026-03-11
last_modified_at: 2026-03-11
weight: 9

---

Unlike abelian groups, the weak direct product defined in the previous post does not satisfy the universal property for general groups.

<div class="example" markdown="1">

<ins id="ex1">**Example 1**</ins> Consider an arbitrary nonabelian group $$G$$, and let $$a,b\in G$$ satisfy $$ab\neq ba$$. Define group homomorphisms $$f_1, f_2: (\mathbb{Z},+)\rightarrow (G,\cdot)$$ by

$$f_1(1)=a, \qquad f_2(1)=b$$

Since the index set $$I=\{1,2\}$$ is finite, the weak direct product of two copies of $$(\mathbb{Z},+)$$ equals $$\mathbb{Z}\times\mathbb{Z}$$.

However, we can see that there is no $$f:\mathbb{Z}\times\mathbb{Z}\rightarrow G$$ making the following diagram

![counterexample](/assets/images/Math/Algebraic_Structures/Free_products-1.png){:style="width:11.6em" class="invert" .align-center}

commute. If such an $$f$$ existed, then

$$\begin{aligned}ab&=f_1(1)f_2(1)=f(\iota_1(1))f(\iota_2(1))=f(\iota_1(1)+\iota_2(1))\\
&=f(\iota_2(1)+\iota_1(1))=f(\iota_2(1))f(\iota_1(1))=f_2(1)f_1(1)\\
&=ba\end{aligned}$$

contradicting the choice of $$a,b$$.

</div>

Therefore, to find an object satisfying the universal property among general groups, analogous to direct sums, we need to introduce a new method. For this, we first need to define free groups.

## Free Group

Any group $$G$$ can be thought of as a set with a binary operation, an identity element, and inverses added to it. Moreover, any group homomorphism can naturally be viewed as a function between sets. That is, there exists a forgetful functor $$U: \Grp \rightarrow\Set$$. In this section, we define the left adjoint $$F:\Set \rightarrow\Grp$$ of $$U$$. By the definition of a left adjoint functor, this is a functor satisfying the natural isomorphism

$$\Hom_\Set(X, U(G))\cong\Hom_\Grp(F(X), G)$$

([\[Category Theory\] §Adjoint Functors, ⁋Definition 1](/en/math/category_theory/adjoints#def1)) That is, functor $$F$$ is given by a bijection that uniquely corresponds an element of $$\Hom_\Grp(F(X),G)$$ to each $$f\in\Hom_\Set(X, U(G))$$ for any set $$X$$ and any group $$G$$. This can be rewritten as follows.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> For a nonempty set $$X$$, the *free group* $$F(X)$$ defined by $$X$$ is determined as the solution $$(F(X), \eta_X\in\Hom_\Set(X,UF(X)))$$ to the following universal mapping problem.

> For any group $$G$$, if a function $$f:X\rightarrow U(G)$$ is given, there exists a unique group homomorphism $$\hat{f}:F(X)\rightarrow G$$ satisfying $$U(\hat{f})\circ\eta_X=f$$.

</div>

Here, $$\eta_X$$ is merely the unit of the adjunction $$F\dashv U$$. Of course, for this, we need to actually construct $$F(X)$$.

We outline the general approach. First, consider a set $$X^{-1}$$ that is disjoint from $$X$$ and has the same cardinality. There is no particular reason for $$X^{-1}$$ to be any specific set, but we will choose a bijection $$X\rightarrow X^{-1}$$ and denote the image of $$x\in X$$ in $$X^{-1}$$ as $$x^{-1}$$. Also, choose a singleton set disjoint from $$X\cup X^{-1}$$ and denote its element as $$e$$.

Then the elements of group $$F$$ are the collection of *reduced words* defined by the set $$X\cup X^{-1}\cup \{e\}$$. Here, a *word* is simply a sequence of elements of the set $$X\cup X^{-1}\cup \{e\}$$, but if the same element appears twice in a row like $$xx$$, or $$x^{-1}$$ appears immediately after $$x$$ like $$xx^{-1}$$, or $$e$$ lies between two terms like $$xey$$, these can be shortened to $$x^2$$, $$e$$, and $$xy$$, respectively. However, for example, if $$y\neq x^{-1}$$, there is no way to shorten $$xyx$$. A word shortened in this way is called a *reduced word*.

We can shorten every word to a reduced word.[^1] Let us define the operation and identity element among these. The identity element is naturally the reduced word $$e$$. The operation is defined as concatenating two words and then shortening to a reduced word. For example, the operation of words $$x_1x_2$$ and $$x_3x_4$$ is given by $$x_1x_2x_3x_4$$. Then $$e$$ can also be viewed as the *empty word* under this operation. This operation is trivially associative. The inverse is obtained by taking the inverse of each term of the original element and reversing their order. For example, the inverse of the word

$$x_1x_2^{-1}x_3^2$$

is

$$x_3^{-2}x_2x_1^{-1}$$

and we can verify that actually computing the operation of these two gives $$e$$.

Now we have constructed the group $$F$$, and by identifying the length-1 elements consisting of elements of $$X$$ with the elements of $$X$$, we also obtain $$\iota:X\rightarrow F$$. Then it is easy to show that these satisfy the universal property of [Definition 2](#def2). For this, it suffices to define $$\bar{f}$$ as the function that replaces all elements $$x\in X$$ appearing in $$F$$ with $$g(x)$$, and verify that this is a group homomorphism.

<div class="proposition" markdown="1">

<ins id="cor3">**Corollary 3**</ins> Any group $$G$$ is a homomorphic image of a free group.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Consider the collection $$X$$ of generators of $$G$$, and consider the free group $$F$$ on $$X$$. There exists a group homomorphism from $$F$$ to $$G$$ defined by the function $$X\hookrightarrow G$$, and since the image of this homomorphism contains all generators of $$G$$, it is surjective.

</details>

## Free Product

Applying the above idea, we can similarly define the free product, which becomes the coproduct we have been seeking. Similarly, we only briefly introduce the construction.

Let a family of groups $$(G_i)$$ be given. For convenience, assume they are all mutually disjoint, and let $$X=\coprod G_i$$. That is, for any element $$x\in X$$, we can uniquely find $$i$$ such that $$x\in G_i$$. Since $$G_i$$ already contain inverses, it suffices to consider $$X\cup\{e\}$$ as the collection of generators.

The *free product* $$\prod^\ast  G_i$$ of $$(G_i)$$ is the collection of reduced words constructed from this set $$X\cup\{e\}$$. The overall flow is the same as when defining free groups, but this time, since elements of $$G_i$$ can be operated among themselves, we need to be a bit more careful when defining reduced words. A reduced word used in defining the free product refers to a word

$$x_1x_2\cdots x_n$$

made from elements of the set $$X\cup\{e\}$$ satisfying the following three conditions.

1. If $$n>1$$, none of the $$x_k$$ equals $$e$$.
2. If $$x_k\in X$$, then $$x_k$$ is not the identity element in the group $$G_i$$ containing this element.
3. Two adjacent elements $$x_i, x_{i+1}$$ must belong to different groups.

Given any word, the method to make it a reduced word is simple. Check whether adjacent elements belong to the same group, and combine elements belonging to the same group into a single element through the operation in that group. If during this process (or originally) an identity element in some group appears, simply delete that element.

Then the operation on $$\prod^\ast G_i$$ is, as in defining free groups, the *concatenation* operation, and it is not difficult to verify that this collection has a group structure. Also, the situation like [Example 1](#ex1) no longer occurs because even if two groups $$G_1,G_2$$ are abelian, their free product $$G_1\ast G_2$$ is no longer an abelian group.

<div class="example" markdown="1">

<ins id="ex4">**Example 4**</ins> Consider the same situation as [Example 1](#ex1). Instead, for notational convenience, let $$G_1=\langle a\rangle\cong\mathbb{Z}$$ and $$G_2=\langle b\rangle\cong\mathbb{Z}$$. Then elements of $$G_1\ast G_2$$ are the collection of elements like

$$ab, a^2b, a^{-1}ba^3, bab^2, \cdots$$

For example, operating two elements $$a^2b$$ and $$bab^2$$ gives

$$(a^2b)(bab^2)=a^2bbab^2=a^2b^2ab^2$$

Here $$\langle a\rangle$$ and $$\langle b\rangle$$ are cyclic subgroups of $$G_1\ast G_2$$, so by defining homomorphisms from $$G_1$$ and $$G_2$$ to $$G_1\ast G_2$$ by $$a\mapsto a$$ and $$b\mapsto b$$, we obtain natural inclusion maps $$\iota_1$$ and $$\iota_2$$.

Of course, the problem like [Example 1](#ex1) also does not occur. $$\iota_1(a)\iota_2(b)=ab$$ and $$\iota_2(b)\iota_1(a)=ba$$, but these two elements are different elements of $$\prod^\ast G_i$$.

</div>

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> The free product $$\prod^\ast G_i$$ is the coproduct in $$\Grp$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let an arbitrary group $$H$$ and group homomorphisms $$f_i:G_i\rightarrow H$$ be given. By the universal property of $$X=\coprod U(G_i)$$, there exists a unique function $$f:X\rightarrow U(H)$$ satisfying $$U(f_i)=f\circ \iota_i$$ for the inclusion maps $$\iota_i:U(G_i)\rightarrow X$$. Now from the universal property of free products ([Definition 2](#def2)), we obtain a group homomorphism $$\hat{f}:F(X)\rightarrow H$$, and using the fact that $$f_i$$ are group homomorphisms, we see that $$f$$ factors through the above reduction process, thus defining $$\prod^\ast G_i\rightarrow H$$.

</details>

On the other hand, for any group $$G$$, a group homomorphism $$\mathbb{Z}\rightarrow G$$ is uniquely determined by which element of $$G$$ $$1\in \mathbb{Z}$$ is sent to. That is, there exists an isomorphism

$$\Hom_\Grp(\mathbb{Z},G)\cong U(G)$$

and by an argument similar to [\[Category Theory\] §Representable Functors, Example 2](/en/math/category_theory/representable_functors#ex2), we see that the above isomorphism is a representation of $$U$$, and moreover, thinking of

$$\Hom_\Grp(\mathbb{Z},G)\cong \Hom_\Set(\ast, U(G))$$

we can interpret this as $$\mathbb{Z}=F(\ast)$$. Therefore, for any set $$X$$, using [\[Category Theory\] §Adjoint Functors, ⁋Theorem 9](/en/math/category_theory/adjoints#thm9), we can express the free group $$F(X)$$ as the free product of copies of $$\mathbb{Z}$$

$$F(X)=F\left(\coprod_{x\in X} \{x\}\right)\cong \coprod_{x\in X} F(\ast)={\prod_{x\in X}}^\ast \mathbb{Z}$$

---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.

---

[^1]: While it is not strictly necessary to introduce reduced words to define the operation between words, it is good to introduce reduced words for uniqueness of representation.
