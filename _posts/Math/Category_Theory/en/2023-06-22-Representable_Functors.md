---
title: "Representable Functors"
description: "A representable functor is one that is naturally isomorphic to a Hom functor. Yoneda's lemma establishes a bijection between natural transformations from a representable functor and elements of the functor's target set."
excerpt: "Initial objects, terminal objects, and representable functors"

categories: [Math / Category Theory]
permalink: /en/math/category_theory/representable_functors
sidebar: 
    nav: "category_theory-en"

date: 2023-06-22
weight: 4
translated_at: 2026-08-19T16:15:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-08-19T16:15:05+00:00
---
## Yoneda lemma

For any object $A$ of a (locally small) category $\mathcal{A}$, we define two functors

$$\Hom_\mathcal{A}(A,-):\mathcal{A}\rightarrow\Set,\qquad \Hom_\mathcal{A}(-,A):\mathcal{A}\rightarrow\Set$$

the first covariant and the second contravariant. ([§Functor, ⁋Example 4](/en/math/category_theory/functors#ex4))

::: Definition 1
Let a category $\mathcal{A}$ be given.

1. A covariant functor $F:\mathcal{A}\rightarrow\Set$ is called a *representable functor* if there exists an object $A\in\obj(\mathcal{A})$ such that $F$ and $\Hom_\mathcal{A}(A,-)$ are naturally isomorphic.
2. A contravariant functor $F:\mathcal{A}\rightarrow\Set$ is called a *representable functor* if there exists an object $A\in\obj(\mathcal{A})$ such that $F$ and $\Hom_\mathcal{A}(-,A)$ are naturally isomorphic.

For any functor $F$, we call a choice of $A\in\obj(\mathcal{A})$ and a natural isomorphism satisfying the above conditions a *representation* of $F$.
:::

::: Example 2
For example, $\id_\Set:\Set \rightarrow \Set$ is representable. This is because for any singleton $\ast$, the natural isomorphism

$$\id_\Set\cong\Hom_\Set(\ast,-)$$

holds. For any set $A$, the bijection

$$\id_\Set(A)=A\rightarrow\Hom_\Set(\ast,A)$$

sends an element $a\in A$ to the function $a:\ast\rightarrow A$ whose image is $a$; conversely, from any function $\ast\rightarrow A$ we recover an element of $A$ by taking its image. The naturality of this correspondence follows from the fact that, given any function $f:A \rightarrow B$, if we set $b=f(a)$ for arbitrary $a\in A$, then the image of $b$ under $\id_\Set(B)\rightarrow\Hom_\Set(\ast,B)$ is the function $b:\ast \rightarrow B$, which is exactly the composite $\ast\overset{a}{\longrightarrow}A\overset{f}{\longrightarrow}B$.
:::

The most important theorem related to this is the following Yoneda lemma.

::: Theorem 3 (Yoneda)
For any functor $F:\mathcal{A}\rightarrow\Set$ and any $A\in\obj(\mathcal{A})$, there exists a bijection of sets

$$\Phi:\{\text{natural transformations from $\Hom_\mathcal{A}(A,-)$ to $F$}\}\rightarrow F(A);\qquad \alpha\mapsto \alpha_A(\id_A)$$

:::
::: Proof
First, let us briefly see how the above function works. A natural transformation from $\Hom_\mathcal{A}(A,-)$ to $F$ assigns, to each object $X$, a function $\alpha_X$ from $\Hom_\mathcal{A}(A,X)$ to $F(X)$. In the special case $X=A$, the function $\alpha_A$ goes from $\Hom_\mathcal{A}(A,A)$ to $F(A)$, and since $\id_A\in\Hom_\mathcal{A}(A,A)$, we have $\alpha_A(\id_A)\in F(A)$.

To show that this function is a bijection, it suffices to construct its inverse. That is, from any element $x\in F(A)$ we must produce a natural transformation $\Psi(x)$, where $\Psi(x)$ is in turn given, for each object $X$ of $\mathcal{A}$, by a function $\Psi(x)_X:\Hom_\mathcal{A}(A,X)\rightarrow F(X)$. Now if $\Psi(x)$ is a natural transformation, the following diagram must commute.

{% diagram Math/Category_Theory/Representable_Functors-1.svg width="15.03em" alt="naturality" %}

Consider again $\id_A\in\Hom_\mathcal{A}(A,A)$. Then tracing the upper-right path gives $F(f)(\Psi(x)_A(\id_A))$, and tracing the lower-left path gives $\Psi(x)_X(f)$. Hence

$$\Psi(x)_X(f)=F(f)(\Psi(x)_A(\id_A))$$

must hold. On the other hand, for $\Psi$ to be the inverse of $\Phi$, we must have $(\Phi\circ\Psi)(x)=x$, so by the way $\Psi$ is defined we see that $\Psi(x)_A(\id_A)$ must be exactly $x$. Thus we must define $\Psi(x)$ by the formula

$$\Psi(x)_X(f)=F(f)(x)$$

That $\Psi(x)$ thus defined is actually a natural transformation follows immediately from the functoriality of $F$. For any morphism $g:X\rightarrow Y$ and any $f\in\Hom_\mathcal{A}(A,X)$,

$$\Psi(x)_Y(g\circ f)=F(g\circ f)(x)=F(g)(F(f)(x))=F(g)(\Psi(x)_X(f))$$

and since $\Hom_\mathcal{A}(A,g)(f)=g\circ f$, the naturality square required for $\Psi(x)$ commutes.

Now let us verify that $\Phi$ and $\Psi$ are inverses of each other. First, for any $x\in F(A)$, from the definition of $\Psi$ and the equality $F(\id_A)=\id_{F(A)}$ we obtain $\Phi(\Psi(x))=\Psi(x)_A(\id_A)=F(\id_A)(x)=x$, so $\Phi\circ\Psi=\id_{F(A)}$. Conversely, taking any natural transformation $\alpha$ from $\Hom_\mathcal{A}(A,-)$ to $F$, the computation we performed for $\Psi(x)$ used only naturality, so it applies equally to $\alpha$, yielding $\alpha_X(f)=F(f)(\alpha_A(\id_A))$. But the right-hand side equals $\Psi(\Phi(\alpha))_X(f)$, and since $X$ and $f$ were chosen arbitrarily, we have $\alpha=\Psi(\Phi(\alpha))$; that is, $\Psi\circ\Phi$ is also the identity.
:::

Moreover, regarding both sides as functors from $\mathcal{A}\times\Fun(\mathcal{A},\Set)$ to $\Set$, this bijection is natural in each component of $\mathcal{A}$ and $\Fun(\mathcal{A},\Set)$. We will not use this fact immediately, so we only mention it in passing, but its proof is no more difficult than the one above. Also, by duality, there is a Yoneda lemma for contravariant functors as well.

::: Theorem 4 (Yoneda)
For any contravariant functor $F:\mathcal{A}\rightarrow\Set$ and any $A\in\obj(\mathcal{A})$, there exists a bijection of sets

$$\Phi:\{\text{natural transformations from $\Hom_\mathcal{A}(-,A)$ to $F$}\}\rightarrow F(A);\qquad \alpha\mapsto \alpha_A(\id_A)$$

:::
For convenience of exposition, in the remainder of this post we treat only the case of covariant functors, but the same statements apply to contravariant functors in an obvious manner.

## Universal property

Looking at [Definition 1](#def1), we agreed to call the choice of an object $A$ and a natural isomorphism $F\cong\Hom_\mathcal{A}(A,-)$ together a *representation*. But by [Theorem 3](#thm3), choosing a natural isomorphism is the same as picking out a suitable element of $F(A)$. We define this as follows.

::: Definition 5
Let a representable functor $F:\mathcal{A}\rightarrow\Set$ be given. For a natural isomorphism $\alpha:\Hom_\mathcal{A}(A,-)\cong F$, we call the element $x=\alpha_A(\id_A)\in F(A)$ corresponding to it by [Theorem 3](#thm3) a *universal element*, and we call $A$ together with $x$ a *universal property*.
:::

The following example helps make this more intuitive.

::: Example 6
Fix two $k$-vector spaces $V,W$, and define the functor $\operatorname{Bilin}(V,W;-)$ from $\Vect_k$ to $\Set$ by

$$\operatorname{Bilin}(V,W;U)=\{\text{bilinear maps from $V\times W$ to $U$}\}$$

Then it is well known that this functor is representable. That is, there exists a $k$-vector space $V\otimes W$ for which the natural isomorphism

$$\Hom_{\Vect_k}(V\otimes W,-)\cong\operatorname{Bilin}(V,W;-)$$

exists. In this case, the natural isomorphism is determined by the Yoneda lemma as a single element of $\operatorname{Bilin}(V,W;V\otimes W)$, namely a bilinear map $V\times W\rightarrow V\otimes W$.

In other words, the universal property of the tensor product consists of the object $V\otimes W$ and the universal element $V\times W\rightarrow V\otimes W$, and what the above natural isomorphism says is precisely that whenever a bilinear map $V\times W\rightarrow U$ is given (right-hand side), there exists a unique $k$-linear map $V\otimes W\rightarrow U$ (left-hand side).
:::

Through the above example, we can see that objects defined via universal properties in various fields are in fact of this form. However, from a purely category-theoretic point of view, the only reason to call these universal properties so far is that we named them that in [Definition 5](#def5).  
To justify this, let us call an object $I$ of a category $\mathcal{A}$ an *initial object* of $\mathcal{A}$ if, for any object $A$, there is a unique morphism $I\rightarrow A$. Similarly we define a *terminal object*. Then [Proposition 8](#prop8) gives an appropriate answer to the question above. That is, all such objects can be regarded as initial (or terminal) objects in suitable categories. To explain this, the following definition is needed.

::: Definition 7
The *category of elements* of a functor $F: \mathcal{A}\rightarrow \Set$ is the category $\int F$ consisting of the following data.

- The objects of $\int F$ are pairs $(A,x)$ with $A\in \mathcal{A}$ and $x\in F(A)$.
- A morphism $(A_1,x_1) \rightarrow (A_2, x_2)$ in $\int F$ is a morphism $f$ in $\mathcal{A}$ satisfying $F(f)(x_1)=x_2$.
:::

For example, the category of elements of $\Hom_{\mathcal{A}}(A,-):\mathcal{A}\rightarrow\Set$ is given by the following data.

- The objects of $\int \Hom_\mathcal{A}(A,-)$ are pairs $(X,\pi)$ with $X\in \mathcal{A}$ and $\pi\in \Hom_\mathcal{A}(A,X)$.
- A morphism $f:(X_1,\pi_1)\rightarrow(X_2,\pi_2)$ in $\int \Hom_\mathcal{A}(A,-)$ is a morphism in $\mathcal{A}$ satisfying $\pi_2=\Hom_\mathcal{A}(A,f)(\pi_1)=f\circ\pi_1$.

That is, $\int\Hom_\mathcal{A}(A,-)$ is the under category ${}_{A/}\mathcal{A}$.

We are now ready to prove the following proposition.

::: Proposition 8
A functor $F:\mathcal{A}\rightarrow\Set$ is representable if and only if $\int F$ has an initial object.
:::
::: Proof
If $F$ is representable, then there exist an object $A$ and a natural isomorphism $\alpha$ such that $F\cong\Hom_\mathcal{A}(A,-)$. From this we can construct an isomorphism $(X,x)\mapsto (X,\alpha_X(x))$ from $\int F$ to $\int\Hom_\mathcal{A}(A,-)$. But $\int\Hom_\mathcal{A}(A,-)={}_{A/}\mathcal{A}$ has the initial object $\id_A$.

Now suppose $\int F$ has an initial object $(A,x)$; from this we must construct a natural isomorphism $\Hom_\mathcal{A}(A,-)\Rightarrow F$. First, from [Theorem 3](#thm3) we know that the bijection

$$\Phi:\{\text{natural transformations from $\Hom_\mathcal{A}(A,-)$ to $F$}\}\rightarrow F(A)$$

exists, and to prove that it is a bijection we defined, for each $x\in F(A)$, the natural transformation $\Psi(x):\Hom_\mathcal{A}(A,-)\Rightarrow F$ by the formula

$$\Psi(x)_X(f)=F(f)(x)$$

On the other hand, in $\int F$, that $(A,x)$ is initial means that for any $(X,y)\in\int F$, there exists a unique morphism $f:A \rightarrow X$ in $\mathcal{A}$ such that $F(f)(x)=y\in F(X)$. But by the above formula, $F(f)(x)=\Psi(x)_X(f)$, and since for fixed $X$ we can choose $y$ arbitrarily from $F(X)$, this says equivalently that whenever any $y\in F(X)$ is given, there is a unique $f\in\Hom_\mathcal{A}(A,X)$ satisfying $y=\Psi(x)_X(f)$. Hence $\Psi(x)_X$ is an isomorphism, and since $X$ was also chosen arbitrarily, $\Psi(x)$ defines a natural isomorphism from $\Hom_\mathcal{A}(A,-)$ to $F$.
:::

Since an initial object in any category is always unique up to unique isomorphism, a universal property is also determined uniquely up to unique isomorphism.

---

**References**

**[Rie]** Emily Riehl. *Category Theory in Context*. Dover Publications, 2016.

---
