---
title: "Representable Functors"
description: "A representable functor is a functor naturally isomorphic to the Hom functor, and Yoneda's lemma establishes a one-to-one correspondence between natural transformations on an arbitrary functor and the elements of that functor."
excerpt: "Initial object, terminal object, representable functor"

categories: [Math / Category Theory]
permalink: /en/math/category_theory/representable_functors
sidebar: 
    nav: "category_theory-en"

date: 2023-06-22
last_modified_at: 2023-06-22
weight: 4
translated_at: 2026-05-30T14:00:03+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-30T14:00:03+00:00
---
## Yoneda lemma

For any object $$A$$ in a (locally small) category $$\mathcal{A}$$, we define two functors 

$$\Hom_\mathcal{A}(A,-):\mathcal{A}\rightarrow\Set,\qquad \Hom_\mathcal{A}(-,A):\mathcal{A}\rightarrow\Set$$

the first covariant and the second contravariant. ([§Functors, ⁋Example 4](/en/math/category_theory/functors#ex4))

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Let a category $$\mathcal{A}$$ be given.

1. A covariant functor $$F:\mathcal{A}\rightarrow\Set$$ is called a *representable functor* if there exists an object $$A\in\obj(\mathcal{A})$$ such that $$F$$ and $$\Hom_\mathcal{A}(A,-)$$ are naturally isomorphic.
2. A contravariant functor $$F:\mathcal{A}\rightarrow\Set$$ is called a *representable functor* if there exists an object $$A\in\obj(\mathcal{A})$$ such that $$F$$ and $$\Hom_\mathcal{A}(-,A)$$ are naturally isomorphic.

For any functor $$F$$, we call the choice of an object $$A\in\obj(\mathcal{A})$$ satisfying the above condition together with a natural isomorphism a *representation* of $$F$$.

</div>

<div class="example" markdown="1">

<ins id="ex2">**Example 2**</ins> For instance, $$\id_\Set:\Set \rightarrow \Set$$ is representable. This is because for any singleton $$\ast$$, the natural isomorphism

$$\id_\Set\cong\Hom_\Set(\ast,-)$$

holds. For any set $$A$$, the bijection

$$\id_\Set(A)=A\rightarrow\Hom_\Set(\ast,A)$$

sends each element $$a\in A$$ to the function $$a:\ast\rightarrow A$$ whose image is $$\{a\}$$; conversely, the image of any function $$\ast\rightarrow A$$ yields an element of $$A$$. The naturality of this correspondence follows because for any function $$f:A \rightarrow B$$ and any $$a\in A$$, writing $$b=f(a)$$, the map $$\id_\Set(B)\rightarrow\Hom_\Set(\ast,B)$$ sends this to the function $$b:\ast \rightarrow B$$ with image $$\{b\}$$, which is precisely the composite $$\ast\overset{a}{\longrightarrow}A\overset{f}{\longrightarrow}B$$.

</div>

The most important theorem in this context is the Yoneda lemma.

<div class="proposition" markdown="1">

<ins id="thm3">**Theorem 3 (Yoneda)**</ins> For any functor $$F:\mathcal{A}\rightarrow\Set$$ and any $$A\in\obj(\mathcal{A})$$, there exists a bijection of sets

$$\Phi:\{\text{natural transformations from $\Hom_\mathcal{A}(A,-)$ to $F$}\}\rightarrow F(A);\qquad \alpha\mapsto \alpha_A(\id_A)$$

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, let us briefly examine how the above function operates. A natural transformation from $$\Hom_\mathcal{A}(A,-)$$ to $$F$$ assigns, to each object $$X$$, a function $$\alpha_X:\Hom_\mathcal{A}(A,X)\rightarrow F(X)$$. In particular, for $$X=A$$, the function $$\alpha_A$$ maps $$\Hom_\mathcal{A}(A,A)$$ to $$F(A)$$, and since $$\id_A\in\Hom_\mathcal{A}(A,A)$$, we have $$\alpha_A(\id_A)\in F(A)$$.

To show that this function is a bijection, it suffices to construct an inverse. That is, from an arbitrary element $$x\in F(A)$$ we must produce a natural transformation $$\Psi(x)$$, which is given, for each object $$X$$ in $$\mathcal{A}$$, by a function $$\Psi(x)_X:\Hom_\mathcal{A}(A,X)\rightarrow F(X)$$. Now, if $$\Psi(x)$$ is a natural transformation, the following diagram must commute.

![naturality](/assets/images/Math/Category_Theory/Representable_Functors-1.png){:style="width:15em" class="invert" .align-center}

Consider again $$\id_A\in\Hom_\mathcal{A}(A,A)$$. Traversing the upper-right path yields $$F(f)(\Psi(x)_A(\id_A))$$, while the lower-left path gives $$\Psi(x)_X(f)$$. Hence

$$\Psi(x)_X(f)=F(f)(\Psi(x)_A(\id_A))$$

must hold. On the other hand, for $$\Psi$$ to be the inverse of $$\Phi$$ we require $$(\Psi\circ\Phi)(x)=x$$, so from the definition of $$\Psi$$ we see that $$\Psi(x)_A(\id_A)$$ must equal $$x$$ exactly. Thus we must define $$\Psi(x)$$ by the formula

$$\Psi(x)_X(f)=F(f)(x)$$

We must additionally verify that $$\Psi$$ so defined is indeed a natural transformation, but this is straightforward.

</details>

Moreover, regarding both sides as functors from $$\mathcal{A}\times\Set^\mathcal{A}$$ to $$\Set$$, this bijection is natural in each component of $$\mathcal{A}$$ and $$\Set^\mathcal{A}$$. We will not use this fact immediately, so we mention it only in passing; its proof is likewise not difficult, much as above. Also, by duality there is a Yoneda lemma for contravariant functors.

<div class="proposition" markdown="1">

<ins id="thm4">**Theorem 4 (Yoneda)**</ins> For any contravariant functor $$F:\mathcal{A}\rightarrow\Set$$ and any $$A\in\obj(\mathcal{A})$$, there exists a bijection of sets

$$\Phi:\{\text{natural transformations from $\Hom_\mathcal{A}(-,A)$ to $F$}\}\rightarrow F(A);\qquad \alpha\mapsto \alpha_A(\id_A)$$

</div>

For ease of exposition, in the remainder of this post we treat only the covariant case; however, the same statements hold for contravariant functors in an obvious manner.

## Universal property

Looking at [Definition 1](#def1), we agreed to call the choice of an object $$A$$ together with a natural isomorphism $$F\cong\Hom_\mathcal{A}(A,-)$$ a *representation*. Yet by [Theorem 3](#thm3), choosing a natural isomorphism is equivalent to selecting a suitable element of $$F(A)$$. We formalize this as follows.

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> Let a representable functor $$F:\mathcal{A}\rightarrow\Set$$ be given. For a natural isomorphism $$\Hom_\mathcal{A}(-,A)\cong F$$, we call an element $$x\in F(A)$$ a *universal element*, and we call the pair $$(A,x)$$ a *universal property*. 

</div>

The following example makes this more intuitive.

<div class="example" markdown="1">

<ins id="ex6">**Example 6**</ins> Fixing two $$k$$-vector spaces $$V,W$$, define the functor $$\operatorname{Bilin}(V,W;-)$$ from the category $$\Vect_k$$ to $$\Set$$ by

$$\operatorname{Bilin}(V,W;U)=\{\text{bilinear maps from $V\times W$ to $U$}\}$$

It is well known that this functor is representable. That is, there exists a suitable $$k$$-vector space $$V\otimes W$$ for which the natural isomorphism

$$\Hom_{\Vect_k}(V\otimes W,-)\cong\operatorname{Bilin}(V,W;-)$$

holds. In this case, by the Yoneda lemma the natural isomorphism is determined by an element of $$\operatorname{Bilin}(V,W;V\otimes W)$$, i.e., by a bilinear map $$V\times W\rightarrow V\otimes W$$. 

In other words, the universal property of the tensor product consists of the object $$V\otimes W$$ together with the universal element $$V\times W\rightarrow V\otimes W$$, and what the above natural isomorphism asserts is precisely that whenever a bilinear map $$V\times W\rightarrow U$$ is given (right-hand side), there is a unique $$k$$-linear map $$V\otimes W\rightarrow U$$ (left-hand side).

</div>

Through this example we can see that objects defined via universal properties in various fields are indeed of this form. However, from a purely category-theoretic standpoint, so far the only justification for calling these universal properties is that we chose the name in [Definition 5](#def5).  
To justify the terminology, let us call an object $$I$$ of a category $$\mathcal{A}$$ an *initial object* if for every object $$A$$ there exists a unique morphism $$I\rightarrow A$$. Dually, we define a *terminal object*. Then [Proposition 8](#prop8) provides an appropriate answer: all such objects can be regarded as initial (or terminal) objects in suitable categories. To explain this, we need the following definition.

<div class="definition" markdown="1">

<ins id="def7">**Definition 7**</ins> The *category of elements* of a functor $$F: \mathcal{A}\rightarrow \Set$$ is the category $$\int F$$ defined by the following data.

- The objects of $$\int F$$ are pairs $$(A,x)$$ with $$A\in \mathcal{A}$$ and $$x\in F(A)$$.
- A morphism $$(A_1,x_1) \rightarrow (A_2, x_2)$$ in $$\int F$$ is a morphism $$f$$ in $$\mathcal{A}$$ satisfying $$F(f)(x_1)=x_2$$. 

</div>

For example, the category of elements of $$\Hom_{\mathcal{A}}(A,-):\mathcal{A}\rightarrow\Set$$ is given by the following data.

- The objects of $$\int \Hom_\mathcal{A}(A,-)$$ are pairs $$(X,\pi)$$ with $$X\in \mathcal{A}$$ and $$\pi\in \Hom_\mathcal{A}(A,X)$$.
- A morphism $$f:(X_1,\pi_1)\rightarrow(X_2,\pi_2)$$ in $$\int \Hom_\mathcal{A}(A,-)$$ is a morphism in $$\mathcal{A}$$ satisfying $$\pi_2=\Hom_\mathcal{A}(A,f)(\pi_1)=f\circ\pi_1$$.

That is, $$\int\Hom_\mathcal{A}(A,-)$$ is the under category $${}_{A/}\mathcal{A}$$. 

We are now ready to prove the following proposition.

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8**</ins> A functor $$F:\mathcal{A}\rightarrow\Set$$ is representable if and only if $$\int F$$ has an initial object.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

If $$F$$ is representable, there exist a suitable object $$A$$ and a natural isomorphism $$\alpha$$ such that $$F\cong\Hom_\mathcal{A}(A,-)$$. From this we obtain an isomorphism $$(X,x)\mapsto (X,\alpha_X(x))$$ from $$\int F$$ to $$\int\Hom_\mathcal{A}(A,-)$$. But $$\int\Hom_\mathcal{A}(A,-)={}_{A/}\mathcal{A}$$ has the initial object $$\id_A$$. 

Now suppose $$\int F$$ has an initial object $$(A,x)$$; we must construct from this a natural isomorphism $$\Hom_\mathcal{A}(A,-)\Rightarrow F$$. First, from [Theorem 3](#thm3) we know that the bijection

$$\Phi:\{\text{natural transformations from $\Hom_\mathcal{A}(A,-)$ to $F$}\}\rightarrow F(A)$$

exists, and in proving that it is a bijection we defined, for each $$x\in F(A)$$, a natural transformation $$\Psi(x):\Hom_\mathcal{A}(A,-)\Rightarrow F$$ by

$$\Psi(x)_X(f)=F(f)(x)$$

Meanwhile, in $$\int F$$, the condition that $$(A,x)$$ is initial means that for any $$(X,y)\in\int F$$ there exists a unique morphism $$f:A \rightarrow X$$ in $$\mathcal{A}$$ with $$F(f)(x)=y\in F(X)$$. By the formula above, $$F(f)(x)=\Psi(x)_X(f)$$; and since $$y$$ can be chosen arbitrarily in $$F(X)$$ once $$X$$ is fixed, this says that for any given $$y\in F(X)$$ there is always a unique $$f\in\Hom_\mathcal{A}(A,X)$$ satisfying $$y=\Psi(x)_X(f)$$. Hence $$\Psi(x)_X$$ is an isomorphism for every $$X$$, and since $$X$$ is arbitrary, $$\Psi(x)$$ defines a natural isomorphism from $$\Hom_\mathcal{A}(A,-)$$ to $$F$$. 

</details>

Since the initial object of any category is uniquely determined up to unique isomorphism, the universal property is also uniquely determined up to unique isomorphism.

---

**References**

**[Rie]** Emily Riehl. *Category Theory in Context*. Dover Publications, 2016.

---
