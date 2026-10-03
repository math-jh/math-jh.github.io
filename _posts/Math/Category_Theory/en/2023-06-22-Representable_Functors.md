---
title: "Representable Functors"
description: "A representable functor is a functor that is naturally isomorphic to a Hom functor. Yoneda's lemma shows a one-to-one correspondence between natural transformations for an arbitrary functor and elements of the functor."
excerpt: "Initial objects, terminal objects, and representable functors"

categories: [Math / Category Theory]
permalink: /en/math/category_theory/representable_functors
sidebar: 
    nav: "category_theory-en"

date: 2023-06-22
weight: 4
translated_at: 2026-08-19T16:15:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-03T03:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
## Yoneda lemma

In a (locally small) category $\mathcal{A}$, any object $A$ defines two functors

$$\Hom_\mathcal{A}(A,-):\mathcal{A}\rightarrow\Set,\qquad \Hom_\mathcal{A}(-,A):\mathcal{A}\rightarrow\Set$$

where the first is a covariant functor and the second is a contravariant functor. ([§Functor, ⁋Example 4](/en/math/category_theory/functors#ex4){: data-lid="4fnzo" })

::: Definition 1
Let a category $\mathcal{A}$ be given.

1. A covariant functor $F:\mathcal{A}\rightarrow\Set$ is called a *representable functor* if there exists an object $A\in\obj(\mathcal{A})$ such that $F$ and $\Hom_\mathcal{A}(A,-)$ are naturally isomorphic.
2. A contravariant functor $F:\mathcal{A}\rightarrow\Set$ is called a *representable functor* if there exists an object $A\in\obj(\mathcal{A})$ such that $F$ and $\Hom_\mathcal{A}(-,A)$ are naturally isomorphic.

For any functor $F$, a choice of $A\in\obj(\mathcal{A})$ and a natural isomorphism satisfying the condition above is called a *representation* of $F$.
:::

::: Example 2
For example, $\id_\Set:\Set \rightarrow \Set$ is representable. This is because for any singleton $\ast$, the natural isomorphism

$$\id_\Set\cong\Hom_\Set(\ast,-)$$

holds. For any set $A$, the bijection

$$\id_\Set(A)=A\rightarrow\Hom_\Set(\ast,A)$$

is given by sending an arbitrary element of $A$, $a$, to the function whose image is $a$, namely $a:\ast\rightarrow A$; conversely, by looking at the image of a function $\ast\rightarrow A$, one can obtain an element of $A$. The naturality of this correspondence follows from the fact that, given any function $f:A \rightarrow B$, if for any $a\in A$ we set $b=f(a)$, then under $\id_\Set(B)\rightarrow\Hom_\Set(\ast,B)$, the image of $b$ is the function $b:\ast \rightarrow B$, which is precisely the composite $\ast\overset{a}{\longrightarrow}A\overset{f}{\longrightarrow}B$.
:::

The most important theorem related to this is the following Yoneda lemma.

::: Theorem 3 (Yoneda)
For any functor $F:\mathcal{A}\rightarrow\Set$ and any $A\in\obj(\mathcal{A})$, there exists a bijection of sets

$$\Phi:\{\text{natural transformations from $\Hom_\mathcal{A}(A,-)$ to $F$}\}\rightarrow F(A);\qquad \alpha\mapsto \alpha_A(\id_A)$$

:::
::: Proof
First, if we briefly look at how the above function works, a natural transformation from $\Hom_\mathcal{A}(A,-)$ to $F$ is given, for any object $X$, by a function $\alpha_X$ from $\Hom_\mathcal{A}(A,X)$ to $F(X)$. In the special case where $X=A$, the function $\alpha_A$ is given as a function from $\Hom_\mathcal{A}(A,A)$ to $F(A)$, and since $\id_A\in\Hom_\mathcal{A}(A,A)$, we have $\alpha_A(\id_A)\in F(A)$.

To show that this function is a bijection, it suffices to construct its inverse. That is, from any element $x\in F(A)$ we must produce a natural transformation $\Psi(x)$, where $\Psi(x)$ is in turn given, for any object $X$ of $\mathcal{A}$, by a function $\Psi(x)_X:\Hom_\mathcal{A}(A,X)\rightarrow F(X)$. However, if $\Psi(x)$ is a natural transformation, the following diagram must commute.

{% diagram Math/Category_Theory/Representable_Functors-1.svg width="15.03em" alt="naturality" %}

Consider again $\id_A\in\Hom_\mathcal{A}(A,A)$. Then tracing the upper-right path gives $F(f)(\Psi(x)_A(\id_A))$, and tracing the lower-left path gives $\Psi(x)_X(f)$. That is,

$$\Psi(x)_X(f)=F(f)(\Psi(x)_A(\id_A))$$

must hold. On the other hand, for $\Psi$ to be the inverse of $\Phi$, we must have $(\Phi\circ\Psi)(x)=x$, so considering how $\Psi$ is defined, we see that $\Psi(x)_A(\id_A)$ must be precisely $x$. That is, through the following equation

$$\Psi(x)_X(f)=F(f)(x)$$

we must define $\Psi(x)$.

That $\Psi(x)$ defined in this way is actually a natural transformation follows immediately from the functoriality of $F$. For any morphism $g:X\rightarrow Y$ and any $f\in\Hom_\mathcal{A}(A,X)$,

$$\Psi(x)_Y(g\circ f)=F(g\circ f)(x)=F(g)(F(f)(x))=F(g)(\Psi(x)_X(f))$$

and since $\Hom_\mathcal{A}(A,g)(f)=g\circ f$, the naturality square required for $\Psi(x)$ commutes.

Now let us verify that $\Phi$ and $\Psi$ are inverses of each other. First, for any $x\in F(A)$, from the definition of $\Psi$ and $F(\id_A)=\id_{F(A)}$ we obtain $\Phi(\Psi(x))=\Psi(x)_A(\id_A)=F(\id_A)(x)=x$, so $\Phi\circ\Psi=\id_{F(A)}$. Conversely, if we take any natural transformation $\alpha$ from $\Hom_\mathcal{A}(A,-)$ to $F$, the computation we performed above for $\Psi(x)$ used only naturality, so it applies equally to $\alpha$, and $\alpha_X(f)=F(f)(\alpha_A(\id_A))$ holds. However, the right-hand side is equal to $\Psi(\Phi(\alpha))_X(f)$, and since $X$ and $f$ were chosen arbitrarily, $\alpha=\Psi(\Phi(\alpha))$; that is, $\Psi\circ\Phi$ is also the identity function.
:::

Moreover, regarding both sides as functors from $\mathcal{A}\times\Fun(\mathcal{A},\Set)$ to $\Set$, this bijection is natural in each component of $\mathcal{A}$ and $\Fun(\mathcal{A},\Set)$. We will not use this fact immediately, so we only mention it in passing, but its proof is also not particularly difficult, just as with the proof above. Also, by duality, there is a Yoneda lemma for contravariant functors as well.

::: Theorem 4 (Yoneda)
For any contravariant functor $F:\mathcal{A}\rightarrow\Set$ and any $A\in\obj(\mathcal{A})$, there exists a bijection of sets

$$\Phi:\{\text{natural transformations from $\Hom_\mathcal{A}(-,A)$ to $F$}\}\rightarrow F(A);\qquad \alpha\mapsto \alpha_A(\id_A)$$

:::

For convenience of exposition, in the remainder of this post we treat only the case of covariant functors, but the same statements apply to contravariant functors in an obvious manner.

## Universal property

Looking at [Definition 1](#def1){: data-lid="6kanm" }, we agreed to call the choice of an object $A$ and a natural isomorphism $F\cong\Hom_\mathcal{A}(A,-)$ together a *representation*. But by [Theorem 3](#thm3){: data-lid="jgko5" }, choosing a natural isomorphism is the same as picking out a suitable element of $F(A)$. We define this as follows.

::: Definition 5
Let a representable functor $F:\mathcal{A}\rightarrow\Set$ be given. For a natural isomorphism $\alpha:\Hom_\mathcal{A}(A,-)\cong F$, we call the element $x=\alpha_A(\id_A)\in F(A)$ corresponding to it by [Theorem 3](#thm3){: data-lid="6irrk" } a *universal element*, and we call $A$ and $x$ together a *universal property*.
:::

We can understand this more intuitively by looking at the following example.

::: Example 6
Fix two $k$-vector spaces $V,W$, and define, from the category $\Vect_k$ to $\Set$, the functor $\operatorname{Bilin}(V,W;-)$ by

$$\operatorname{Bilin}(V,W;U)=\{\text{bilinear maps from $V\times W$ to $U$}\}$$

Then it is well known that this functor is representable. That is, there exists a suitable $k$-vector space $V\otimes W$ such that the natural isomorphism

$$\Hom_{\Vect_k}(V\otimes W,-)\cong\operatorname{Bilin}(V,W;-)$$

exists. Here, by the Yoneda lemma, the natural isomorphism is defined by a single element of $\operatorname{Bilin}(V,W;V\otimes W)$, namely a bilinear map from $V\times W$ to $V\otimes W$.

In other words, the universal property of the tensor product is captured by the object $V\otimes W$ and the universal element $V\times W\rightarrow V\otimes W$, and what the natural isomorphism above says is precisely that whenever a bilinear map from $V\times W$ to $U$ is given (right-hand side), a unique $k$-linear map $V\otimes W\rightarrow U$ (left-hand side) is given.
:::

Through the above example, we can see that objects defined via universal properties in various fields are in fact of this form. However, looking solely from the perspective of category theory, so far no reason can be found to call them universal properties other than that we named them so in [Definition 5](#def5){: data-lid="3ep3j" }.  
To justify this, in a category $\mathcal{A}$, if an object $I$ has, whenever an arbitrary object $A$ is given, a unique morphism $I\rightarrow A$, let us call it an *initial object* of $\mathcal{A}$. Similarly, we also define a *terminal object*. Then [Proposition 8](#prop8){: data-lid="w26fy" } gives an appropriate answer to the question above. That is, all such objects can be regarded as initial (or terminal) objects of a suitable category. To explain this, the following definition is needed.

::: Definition 7
The *category of elements* of a functor $F: \mathcal{A}\rightarrow \Set$ is the category $\int F$ consisting of the following data.

- The objects of $\int F$ are pairs consisting of $A\in \mathcal{A}$ and $x\in F(A)$, denoted $(A,x)$.
- In $\int F$, a morphism $(A_1,x_1) \rightarrow (A_2, x_2)$ is, satisfying $F(f)(x_1)=x_2$, a morphism in $\mathcal{A}$, $f$.
:::

For example, the category of elements of $\Hom_{\mathcal{A}}(A,-):\mathcal{A}\rightarrow\Set$ consists of the following data.

- The objects of $\int \Hom_\mathcal{A}(A,-)$ are pairs consisting of $X\in \mathcal{A}$ and $\pi\in \Hom_\mathcal{A}(A,X)$, denoted $(X,\pi)$.
- In $\int \Hom_\mathcal{A}(A,-)$, a morphism $f:(X_1,\pi_1)\rightarrow(X_2,\pi_2)$ is, satisfying $\pi_2=\Hom_\mathcal{A}(A,f)(\pi_1)=f\circ\pi_1$, a morphism in $\mathcal{A}$.

That is, $\int\Hom_\mathcal{A}(A,-)$ is the under category ${}_{A/}\mathcal{A}$.

We are now ready to prove the following proposition.

::: Proposition 8
A functor $F:\mathcal{A}\rightarrow\Set$ is representable if and only if $\int F$ has an initial object.
:::
::: Proof
If $F$ is representable, then for $F\cong\Hom_\mathcal{A}(A,-)$ to hold, there exist a suitable $A$ and a natural isomorphism $\alpha$. Then via this, we can construct, from $\int F$ to $\int\Hom_\mathcal{A}(A,-)$, an isomorphism $(X,x)\mapsto (X,\alpha_X(x))$. But $\int\Hom_\mathcal{A}(A,-)={}_{A/}\mathcal{A}$ has the initial object $\id_A$.

Now suppose that $\int F$ has an initial object $(A,x)$; from this we must construct a natural isomorphism $\Hom_\mathcal{A}(A,-)\Rightarrow F$. First, from [Theorem 3](#thm3){: data-lid="p9662" }, we know that the bijection

$$\Phi:\{\text{natural transformations from $\Hom_\mathcal{A}(A,-)$ to $F$}\}\rightarrow F(A)$$

exists, and to prove that it is a bijection, we had defined, for each $x\in F(A)$, the natural transformation $\Psi(x):\Hom_\mathcal{A}(A,-)\Rightarrow F$ by the formula

$$\Psi(x)_X(f)=F(f)(x)$$

On the other hand, in $\int F$, that $(A,x)$ is initial means that whenever we take any $(X,y)\in\int F$, there exists in $\mathcal{A}$ a unique morphism $f:A \rightarrow X$ such that $F(f)(x)=y\in F(X)$. But by the above formula, $F(f)(x)=\Psi(x)_X(f)$, and since for fixed $X$ we can choose $y$ arbitrarily from $F(X)$, in other words this means that whenever any $y\in F(X)$ is given, satisfying $y=\Psi(x)_X(f)$, we can always uniquely find $f\in\Hom_\mathcal{A}(A,X)$. That is, $\Psi(x)_X$ is an isomorphism, and since $X$ can also be chosen arbitrarily, $\Psi(x)$ defines a natural isomorphism from $\Hom_\mathcal{A}(A,-)$ to $F$.
:::

Now, since an initial object in any category is always uniquely determined up to unique isomorphism, a universal property is also uniquely determined up to unique isomorphism.

---

**References**

**[Rie]** Emily Riehl. *Category Theory in Context*. Dover Publications, 2016.

---
