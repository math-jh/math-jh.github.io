---
title: "Abelian Categories"
description: "This post covers the definitions of additive and Abelian categories. It introduces additive functors, zero maps, kernels, and cokernels to lay the groundwork for chain complexes and exact sequences."
excerpt: "Abelian categories"

categories: [Math / Category Theory]
permalink: /en/math/category_theory/abelian_categories
sidebar: 
    nav: "category_theory-en"

date: 2024-08-29
weight: 9
translated_at: 2026-08-18T06:17:32+00:00
translation_source: kimi-cli
---
In this post we define the notions of an abelian category, chain complex, and exact sequence.

## Additive category

To define an abelian category, we must first define an additive category.

::: Definition 1
A category $\mathcal{A}$ is called an *$\Ab$-category* if each $\Hom_\mathcal{A}(A,B)$ is equipped with the structure of an abelian group and $(\Hom_\mathcal{A}(A,B),+)$ satisfies the distributive law with respect to composition. That is, for any $g_1,g_2\in\Hom_\mathcal{A}(B,C)$ and any $f:A\rightarrow B$ or $h:C\rightarrow D$,

$$(g_1+g_2)\circ f=g_1\circ f+g_2\circ f,\qquad h\circ(g_1+g_2)=h\circ g_1+h\circ g_2$$

both hold. An $\Ab$-category that possesses a zero object $0$ and has a product for any two objects is called an *additive category*.
:::

A functor $F:\mathcal{A}\rightarrow\mathcal{B}$ between two additive categories $\mathcal{A},\mathcal{B}$ is called an *additive functor* if $F$ induces a group homomorphism from the abelian group $\Hom_\mathcal{A}(A,B)$ to $\Hom_\mathcal{B}(F(A),F(B))$.

In an additive category, for any $A,B\in\obj(\mathcal{A})$, the *zero map* $0_{AB}:A\rightarrow B$ is defined as $A\rightarrow 0\rightarrow B$. This zero map is, of course, the identity element for addition in the abelian group $\Hom_\mathcal{A}(A,B)$.

::: Proposition 2
For any additive category $\mathcal{A}$ and any two objects $A,B\in\obj(\mathcal{A})$, the zero map $0_{AB}$ defined above is the identity element for addition in $\Hom_\mathcal{A}(A,B)$.
:::
::: Proof
There is a unique morphism $0_{0B}$ from the zero object $0$ to $B$. Hence $0_{0B}+0_{0B}=0_{0B}$ holds. The given proposition now follows from the identity

$$0_{AB}+0_{AB}=0_{0B}\circ0_{A0}+0_{0B}\circ0_{A0}=(0_{0B}+0_{0B})\circ 0_{A0}=0_{0B}\circ 0_{A0}=0_{AB}$$

Indeed, adding $-0_{AB}$ to both sides of the above equation in the abelian group $\Hom_\mathcal{A}(A,B)$ yields that $0_{AB}$ is the identity element for addition.
:::

## Abelian category

For any morphism $f:A \rightarrow B$ in an additive category $\mathcal{A}$, the kernel of $f$ is defined as the equalizer $\Eq(f,0)$ with $0:A \rightarrow B$, and similarly the cokernel of $f$ is defined as the coequalizer $\CoEq(f,0)$ with $0$.

We can now define an abelian category.

::: Definition 3
An additive category $\mathcal{A}$ is called an *abelian category* if the following additional conditions hold.

1. Every morphism has a kernel and a cokernel.
2. Every monomorphism $f$ is the kernel of $\coker f$.
3. Every epimorphism $f$ is the cokernel of $\ker f$.
:::

In particular, in this situation, when an exact sequence

$$0 \rightarrow A \rightarrow B \rightarrow C$$

as defined in [Definition 5](#def5) is given, we may identify $A$ with the kernel of $B \rightarrow C$, and when the exact sequence

$$A \rightarrow B \rightarrow C \rightarrow 0$$

is given, we may identify $C$ with the cokernel of $A \rightarrow B$. In an abelian category, for any morphism $f:A\rightarrow B$, the kernel $i:\ker f\rightarrow A$ and the cokernel $p:B\rightarrow \coker f$ of $f$ exist.

In any abelian category $\mathcal{A}$, the *image* of $f$ is defined as the morphism

$$\ker(\coker f)\rightarrow B$$

Similarly, the *coimage* of $f$ is defined as the morphism

$$\coim(f)=\coker(\ker(f))$$

In a general abelian category, if a monomorphism $f:A\rightarrow B$ is given, we call $\coker f$ a *quotient object* and denote it by $B\rightarrow B/A$, or more simply $B/A$.

## Chain complex

::: Definition 4
Consider the following data defined in an additive category $\mathcal{A}$.

- A collection of objects $(A_n)_{n\in \mathbb{Z}}$,
- A collection of morphisms $(d_n:A_n \rightarrow A_{n-1})_{n\in \mathbb{Z}}$

If these data satisfy the condition $d_n\circ d_{n+1}=0$, we call this a *chain complex* and write it as $A_\bullet$.
:::

On the other hand, a morphism between chain complexes $A_\bullet$ and $B_\bullet$ is called a *chain map*; it is given by a collection of morphisms $(f_n: A_n \rightarrow B_n)_{n\in \mathbb{Z}}$ satisfying the condition $d_n^B\circ f_n=f_{n-1}\circ d_n^A$. This allows us to define the category of chain complexes $\Ch(\mathcal{A})$.

If $\mathcal{A}$ is an abelian category, we can examine this in more detail. Let us fix the names and notation commonly used when dealing with chain complexes in this situation. First, each $d_n$ is called a *differential* or a *boundary map*, depending on context.

We denote their kernels and images by

$$Z_n=\ker(d_n),\qquad B_n=\im(d_{n+1})$$

respectively, and their elements are called *$n$-cycles* and *$n$-boundaries*. An element of $A_n$ is called an *$n$-chain*. It is not difficult to verify that the following monomorphisms exist:

$$B_n \hookrightarrow Z_n \hookrightarrow A_n$$

and in this case we call the cokernel $Z_n/B_n$ the *$n$-th homology* of $A_\bullet$ and write it as $H_n(A_\bullet)$ or simply $H_n(A)$.

A chain complex in $\mathcal{A}^\op$ is called a *cochain complex*.

::: Definition 5
Let an arbitrary chain complex $A_\bullet$ be given. Then

$$\cdots \rightarrow A_{n+1}\overset{d_{n+1}}{\longrightarrow}A_n\overset{d_n}{\longrightarrow}A_{n-1}\rightarrow\cdots$$

is said to be *exact* at $A_n$ if the monomorphism $B_n \rightarrow Z_n$ above is an isomorphism. A chain complex that is exact everywhere is called an *exact sequence*.
:::

::: Example 6
The exact sequence

$$\cdots 0 \rightarrow 0 \rightarrow A \rightarrow B \rightarrow C \rightarrow 0 \rightarrow 0 \rightarrow \cdots$$

is called a *short exact sequence*, and it is written simply as

$$0 \rightarrow A \rightarrow B \rightarrow C \rightarrow 0$$
:::

Let an additive functor $F:\mathcal{A}\rightarrow \mathcal{B}$ be given. Then for any chain complex $A_\bullet$ defined in $\mathcal{A}$, one easily checks that the data

$$\cdots \rightarrow F(A_{n+1}) \overset{F(d_{n+1})}{\longrightarrow} F(A_n) \overset{F(d_n)}{\longrightarrow} F(A_{n-1})\rightarrow\cdots$$

form a chain complex. That is, the additive functor $F$ induces a functor $\Ch(\mathcal{A})\rightarrow \Ch(\mathcal{B})$. However, for a general additive functor, the fact that the original chain complex $A_\bullet$ is exact does not guarantee that the new complex $F(A_\bullet)$ obtained as above is exact.

::: Definition 7
An additive functor $F: \mathcal{A} \rightarrow \mathcal{B}$ is called *left exact* if for any short exact sequence

$$0 \rightarrow A \rightarrow B \rightarrow C \rightarrow 0$$

the sequence

$$0 \rightarrow F(A) \rightarrow F(B) \rightarrow F(C)$$

is exact. Similarly, $F$ is called *right exact* if for any short exact sequence as above, the sequence

$$F(A) \rightarrow F(B) \rightarrow F(C) \rightarrow 0$$

is exact. A functor that is both left exact and right exact is called an *exact functor*.
:::

That is, an additive functor preserving kernels is called a left exact functor, and a functor preserving cokernels is called a right exact functor. Then one can verify in particular that a left adjoint functor is right exact and a right adjoint functor is left exact.

Even if $F$ is contravariant, left exactness and right exactness can be defined in the same way as above.

## Freyd-Mitchell embedding theorem

Meanwhile, as we have seen, kernels, cokernels, images, and quotients are all defined in an abelian category. From this, theorems in $\lMod{A}$ can be transferred to an arbitrary abelian category. For example, restating the first isomorphism theorem in the language of an arbitrary abelian category, we can write:

> Let a morphism $f:A\rightarrow B$ in an arbitrary abelian category $\mathcal{A}$ be given. Then $A/\ker f\cong \im f$ holds.

where the left-hand side becomes the quotient object obtained from $i:\ker f\rightarrow A$. Theorems of this kind can all be lifted to an abelian category, and their proofs can be carried out using only the universal properties of kernels and cokernels, though the proofs are somewhat complicated.

Therefore, instead of proving such theorems one by one, one generally uses the following theorem.

::: Theorem 8 (Freyd-Mitchell embedding theorem)
For any small abelian category $\mathcal{A}$, there exist a suitable ring $A$ and a fully faithful, exact functor $F:\mathcal{A}\rightarrow\lMod{A}$.
:::

Hence, we may regard the objects of an arbitrary small abelian category as $A$-modules and their morphisms as $A$-linear maps, and perform calculations without issue.

---

**References**

**[Wei]** C.A. Weibel. *An Introduction to Homological Algebra*. Cambridge Studies in Advanced Mathematics. Cambridge University Press, 1995.  
**[Vak]** R. Vakil, *The rising sea: foundations of algebraic geometry*. 2015. Preprint. [링크](http://math.stanford.edu/~vakil/216blog/FOAGnov1817public.pdf)
