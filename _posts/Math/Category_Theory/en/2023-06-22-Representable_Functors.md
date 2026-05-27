---title: "Representable Functors"
excerpt: "Initial object, terminal object, representable functor"

categories: [Math / Category Theory]
permalink: /en/math/category_theory/representable_functors
header:
    overlay_image: /assets/images/Math/Category_Theory/Representable_Functors.png
    overlay_filter: 0.5
sidebar: 
    nav: "category_theory-en"

date: 2023-06-22
last_modified_at: 2023-06-22
weight: 5
translated_at: 2026-05-28T11:36:15+00:00
translation_source: kimi-cli
---
## Yoneda lemma

For any object $$A$$ in a (locally small) category $$\mathcal{A}$$, we define two functors 

$$\Hom_\mathcal{A}(A,-):\mathcal{A}\rightarrow\Set,\qquad \Hom_\mathcal{A}(-,A):\mathcal{A}\rightarrow\Set$$

the first is a covariant functor and the second is a contravariant functor. ([§Functors, ⁋Example 4](/en/math/category_theory/functors#ex4))

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Let a category $$\mathcal{A}$$ be given.

1. A covariant functor $$F:\mathcal{A}\rightarrow\Set$$ is called a *representable functor* if there exists an object $$A\in\obj(\mathcal{A})$$ such that $$F$$ and $$\Hom_\mathcal{A}(A,-)$$ are naturally isomorphic.
2. A contravariant functor $$F:\mathcal{A}\rightarrow\Set$$ is called a *representable functor* if there exists an object $$A\in\obj(\mathcal{A})$$ such that $$F$$ and $$\Hom_\mathcal{A}(-,A)$$ are naturally isomorphic.

For any functor $$F$$, we call the choice of an object $$A\in\obj(\mathcal{A})$$ satisfying the above condition together with a natural isomorphism a *representation* of $$F$$.

</div>

<div class="example" markdown="1">

<ins id="ex2">**Example 2**</ins> For example, $$\id_\Set:\Set \rightarrow \Set$$ is representable. This is because for any singleton $$\ast$$, the following natural isomorphism

$$\id_\Set\cong\Hom_\Set(\ast,-)$$

holds. For any set $$A$$, the bijection

$$\id_\Set(A)=A\rightarrow\Hom_\Set(\ast,A)$$

is given by taking an arbitrary element $$a$$ of $$A$$ to the function $$a:\ast\rightarrow A$$ whose image is $$a$$, and conversely, by looking at the image of a function $$\ast\rightarrow A$$ we can obtain an element of $$A$$. The naturality of this correspondence is obtained because for any function $$f:A \rightarrow B$$ and any $$a\in A$$, letting $$b=f(a)$$, the map $$\id_\Set(B)\rightarrow\Hom_\Set(\ast,B)$$ sends this to the function $$b:\ast \rightarrow B$$ whose image is $$b$$, which is exactly the composite $$\ast\overset{a}{\longrightarrow}A\overset{f}{\longrightarrow}B$$.

</div>

The most important theorem related to this is the following Yoneda lemma.

<div class="proposition" markdown="1">

<ins id="thm3">**Theorem 3 (Yoneda)**</ins> For any functor $$F:\mathcal{A}\rightarrow\Set$$ and any $$A\in\obj(\mathcal{A})$$, there exists a bijection between sets

$$\Phi:\{\text{natural transformations from $\Hom_\mathcal{A}(A,-)$ to $F$}\}\rightarrow F(A);\qquad \alpha\mapsto \alpha_A(\id_A)$$

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, let us briefly see how the above function works. A natural transformation from $$\Hom_\mathcal{A}(A,-)$$ to $$F$$ is given, for each object $$X$$, by a function $$\alpha_X$$ from the set $$\Hom_\mathcal{A}(A,X)$$ to $$F(X)$$. In particular, when $$X=A$$, the function $$\alpha_A$$ is a function from $$\Hom_\mathcal{A}(A,A)$$ to $$F(A)$$, and since $$\id_A\in\Hom_\mathcal{A}(A,A)$$, we have $$\alpha_A(\id_A)\in F(A)$$.

To show that this function is a bijection, it suffices to construct an inverse function. That is, from an arbitrary element $$x\in F(A)$$ we must construct a natural transformation $$\Psi(x)$$, which is given, for each object $$X$$ in $$\mathcal{A}$$, by a function $$\Psi(x)_X:\Hom_\mathcal{A}(A,X)\rightarrow F(X)$$. Now, if $$\Psi(x)$$ is a natural transformation, the following diagram must commute.

![naturality](/assets/images/Math/Category_Theory/Representable_Functors-1.png){:style="width:15em" class="invert" .align-center}

Consider again $$\id_A\in\Hom_\mathcal{A}(A,A)$$. Then going along the upper-right direction this is $$F(f)(\Psi(x)_A(\id_A))$$, and going along the lower-left direction we obtain $$\Psi(x)_X(f)$$. That is,

$$\Psi(x)_X(f)=F(f)(\Psi(x)_A(\id_A))$$

must hold. On the other hand, for $$\Psi$$ to be the inverse of $$\Phi$$ we must have $$(\Psi\circ\Phi)(x)=x$$, so by considering how $$\Psi$$ is defined we see that $$\Psi(x)_A(\id_A)$$ must be exactly $$x$$. Thus we must define $$\Psi(x)$$ by the formula

$$\Psi(x)_X(f)=F(f)(x)$$

We must additionally show that $$\Psi$$ defined in this way is actually a natural transformation, but this is not difficult. 

</details>

Moreover, if we regard both sides as functors from $$\mathcal{A}\times\Set^\mathcal{A}$$ to $$\Set$$, this bijection is natural in each component of $$\mathcal{A}$$ and $$\Set^\mathcal{A}$$. We will not use this fact immediately, so we only mention it in passing; its proof is also not very difficult, much like the proof above. Also, by duality there exists a Yoneda lemma for contravariant functors as well.

<div class="proposition" markdown="1">

<ins id="thm4">**Theorem 4 (Yoneda)**</ins> For any contravariant functor $$F:\mathcal{A}\rightarrow\Set$$ and any $$A\in\obj(\mathcal{A})$$, there exists a bijection between sets

$$\Phi:\{\text{natural transformations from $\Hom_\mathcal{A}(-,A)$ to $F$}\}\rightarrow F(A);\qquad \alpha\mapsto \alpha_A(\id_A)$$

</div>

For ease of exposition, in the remainder of this post we only treat the case of covariant functors, but the same stories can be told for contravariant functors in an obvious way.

## Universal Property

Looking at [Definition 1](#def1), we agreed to call the choice of an object $$A$$ together with a natural isomorphism $$F\cong\Hom_\mathcal{A}(A,-)$$ a *representation*. However, by [Theorem 3](#thm3), choosing a natural isomorphism is the same as picking an appropriate element of $$F(A)$$. We define this as follows.

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> Let a representable functor $$F:\mathcal{A}\rightarrow\Set$$ be given. For a natural isomorphism $$\Hom_\mathcal{A}(-,A)\cong F$$, we call an element $$x\in F(A)$$ a *universal element*, and we call $$A$$ together with $$x$$ a *universal property*. 

</div>

Looking at the following example, we can understand this a bit more intuitively.

<div class="example" markdown="1">

<ins id="ex6">**Example 6**</ins> Fixing two $$k$$-vector spaces $$V,W$$, define the functor $$\operatorname{Bilin}(V,W;-)$$ from category $$\Vect_k$$ to $$\Set$$ by

$$\operatorname{Bilin}(V,W;U)=\{\text{bilinear maps from $V\times W$ to $U$}\}$$

Then it is well known that this functor is representable. That is, there exists an appropriate $$k$$-vector space $$V\otimes W$$ such that the following natural isomorphism

$$\Hom_{\Vect_k}(V\otimes W,-)\cong\operatorname{Bilin}(V,W;-)$$

exists. In this case, by the Yoneda lemma the natural isomorphism is defined by an element of $$\operatorname{Bilin}(V,W;V\otimes W)$$, that is, by a bilinear map from $$V\times W$$ to $$V\otimes W$$. 

In other words, the universal property of the tensor product consists of the object $$V\otimes W$$ together with the universal element $$V\times W\rightarrow V\otimes W$$, and what the above natural isomorphism says is exactly that whenever a bilinear map from $$V\times W$$ to $$U$$ is given (right-hand side), a unique $$k$$-linear map from $$V\otimes W$$ (left-hand side) is given.

</div>

Through the above example, we can check that objects defined via universal properties in various fields are actually of the above form. However, from a purely category-theoretic viewpoint, so far the only reason we call these universal properties is that we named them so in [Definition 5](#def5).  
To justify this, let us call an object $$I$$ of a category $$\mathcal{A}$$ an *initial object* if for any object $$A$$ there exists a unique morphism $$I\rightarrow A$$. Similarly, we also define a *terminal object*. Then [Proposition 8](#prop8) gives an appropriate answer to the above question. That is, all such objects can be thought of as initial (or terminal) objects of appropriate categories. To explain this, the following definition is needed.

<div class="definition" markdown="1">

<ins id="def7">**Definition 7**</ins> The *category of elements* of a functor $$F: \mathcal{A}\rightarrow \Set$$ is the category $$\int F$$ consisting of the following data.

- The objects of $$\int F$$ are pairs $$(A,x)$$ consisting of $$A\in \mathcal{A}$$ and $$x\in F(A)$$.
- A morphism $$(A_1,x_1) \rightarrow (A_2, x_2)$$ in $$\int F$$ is a morphism $$f$$ in $$\mathcal{A}$$ satisfying $$F(f)(x_1)=x_2$$. 

</div>

For example, the category of elements of $$\Hom_{\mathcal{A}}(A,-):\mathcal{A}\rightarrow\Set$$ consists of the following data.

- The objects of $$\int \Hom_\mathcal{A}(A,-)$$ are pairs $$(X,\pi)$$ consisting of $$X\in \mathcal{A}$$ and $$\pi\in \Hom_\mathcal{A}(A,X)$$.
- A morphism $$f:(X_1,\pi_1)\rightarrow(X_2,\pi_2)$$ in $$\int \Hom_\mathcal{A}(A,-)$$ is a morphism in $$\mathcal{A}$$ satisfying $$\pi_2=\Hom_\mathcal{A}(A,f)(\pi_1)=f\circ\pi_1$$.

That is, $$\int\Hom_\mathcal{A}(A,-)$$ is the under category $${}_{A/}\mathcal{A}$$. 

We are now ready to prove the following proposition.

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8**</ins> A functor $$F:\mathcal{A}\rightarrow\Set$$ is representable if and only if $$\int F$$ has an initial object.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

If $$F$$ is representable, there exist an appropriate object $$A$$ and a natural isomorphism $$\alpha$$ such that $$F\cong\Hom_\mathcal{A}(A,-)$$. Then through this we can construct an isomorphism $$(X,x)\mapsto (X,\alpha_X(x))$$ from $$\int F$$ to $$\int\Hom_\mathcal{A}(A,-)$$. But $$\int\Hom_\mathcal{A}(A,-)={}_{A/}\mathcal{A}$$ has the initial object $$\id_A$$. 

Now suppose $$\int F$$ has an initial object $$(A,x)$$; we must construct from this a natural isomorphism $$\Hom_\mathcal{A}(A,-)\Rightarrow F$$. First, from [Theorem 3](#thm3) we know that the bijection

$$\Phi:\{\text{natural transformations from $\Hom_\mathcal{A}(A,-)$ to $F$}\}\rightarrow F(A)$$

exists, and to prove that this is a bijection we defined, for each $$x\in F(A)$$, a natural transformation $$\Psi(x):\Hom_\mathcal{A}(A,-)\Rightarrow F$$ by the formula

$$\Psi(x)_X(f)=F(f)(x)$$

Meanwhile, in $$\int F$$, the fact that $$(A,x)$$ is initial means that for any $$(X,y)\in\int F$$ there exists a unique morphism $$f:A \rightarrow X$$ in $$\mathcal{A}$$ such that $$F(f)(x)=y\in F(X)$$. But by the above formula we have $$F(f)(x)=\Psi(x)_X(f)$$, and fixing $$X$$, $$y$$ can be chosen arbitrarily from $$F(X)$$; thus this says that for any given $$y\in F(X)$$, we can always find a unique $$f\in\Hom_\mathcal{A}(A,X)$$ satisfying $$y=\Psi(x)_X(f)$$. That is, $$\Psi(x)_X$$ is an isomorphism, and since $$X$$ can also be chosen arbitrarily, $$\Psi(x)$$ defines a natural isomorphism from $$\Hom_\mathcal{A}(A,-)$$ to $$F$$. 

</details>

Since the initial object of any category is always uniquely determined up to unique isomorphism, the universal property is also uniquely determined up to unique isomorphism.

---

**References**

**[Rie]** Emily Riehl. *Category Theory in Context*. Dover Publications, 2016.

---
