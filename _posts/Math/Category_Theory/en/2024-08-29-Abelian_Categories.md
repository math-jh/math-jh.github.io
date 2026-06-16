---
title: "Abelian Categories"
description: "This post covers the definitions of additive and Abelian categories, and introduces chain complexes and exact sequences through the concepts of additive functors, zero maps, kernels, and cokernels."
excerpt: "Abelian Categories"

categories: [Math / Category Theory]
permalink: /en/math/category_theory/abelian_categories
sidebar: 
    nav: "category_theory-en"

date: 2022-12-21
weight: 9
translated_at: 2026-05-30T15:30:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-30T15:30:04+00:00
---
In this post we define the notions of abelian categories, chain complexes, and exact sequences.

## Additive category

To define abelian categories, we must first define additive categories.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A category $$\mathcal{A}$$ is called an *$$\Ab$$-category* if each $$\Hom_\mathcal{C}(A,B)$$ carries the structure of an abelian group, and addition in $$\Hom_\mathcal{C}(A,B)$$ distributes over composition. That is, for any $$g_1,g_2\in\Hom_\mathcal{C}(B,C)$$ and any $$f:A\rightarrow B$$ or $$h:C\rightarrow D$$,

$$(g_1+g_2)\circ f=g_1\circ f+g_2\circ f,\qquad h\circ(g_1+g_2)=h\circ g_1+h\circ g_2$$

both hold. An $$\Ab$$-category that has a zero object $$0$$ and in which the product of any two objects exists is called an *additive category*.

</div>

A functor $$F:\mathcal{A}\rightarrow\mathcal{B}$$ between two additive categories $$\mathcal{A},\mathcal{B}$$ is called an *additive functor* if $$F$$ induces a group homomorphism from the abelian group $$\Hom_\mathcal{A}(A,B)$$ to $$\Hom_\mathcal{B}(F(A),F(B))$$.

In an additive category, for any $$A,B\in\obj(\mathcal{A})$$, the *zero map* $$0_{AB}:A\rightarrow B$$ is defined as the composite $$A\rightarrow 0\rightarrow B$$. The zero map so defined is of course the additive identity in the abelian group $$\Hom_\mathcal{A}(A,B)$$.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> For any additive category $$\mathcal{A}$$ and any two objects $$A,B\in\obj(\mathcal{A})$$, the zero map $$0_{AB}$$ defined above is the additive identity in $$\Hom_\mathcal{A}(A,B)$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

There exists a unique morphism $$0_{0B}$$ from the zero object $$0$$ to $$B$$. Hence $$0_{0B}+0_{0B}=0_{0B}$$ holds. The proposition is now immediate from the equation

$$0_{AB}+0_{AB}=0_{0B}\circ0_{A0}+0_{0B}\circ0_{A0}=(0_{0B}+0_{0B})\circ 0_{A0}=0_{0B}\circ 0_{A0}=0_{AB}$$

</details>

## Abelian category

We may now define abelian categories.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> An additive category $$\mathcal{A}$$ is called an *abelian category* if the following additional conditions are satisfied.

1. Every morphism has a kernel and a cokernel.
2. Every monomorphism $$f$$ is the kernel of $$\coker f$$.
3. Every epimorphism $$f$$ is the cokernel of $$\ker f$$.

</div>

In an additive category $$\mathcal{A}$$, the kernel of any morphism $$f:A \rightarrow B$$ is defined as the equalizer $$\Eq(f,0)$$ with $$0:A \rightarrow B$$, and similarly the cokernel of $$f$$ is defined as the coequalizer $$\CoEq(f,0)$$ with $$0$$.

In particular, in this situation, given the exact sequence

$$0 \rightarrow A \rightarrow B \rightarrow C$$

we may identify $$A$$ with the kernel of $$B \rightarrow C$$, and given the exact sequence

$$A \rightarrow B \rightarrow C \rightarrow 0$$

we may identify $$C$$ with the cokernel of $$A \rightarrow B$$. In an abelian category, for any homomorphism $$f:A\rightarrow B$$, the kernel $$i:\ker f\rightarrow A$$ and the cokernel $$p:B\rightarrow \coker f$$ of $$f$$ exist.

In any abelian category $$\mathcal{A}$$, the *image* of $$f$$ is the morphism

$$\ker(\coker f)\rightarrow\coker f$$

Similarly, the *coimage* of $$f$$ is defined as the morphism

$$\coim(f)=\coker(\ker(f))$$

In a general abelian category, given a monomorphism $$f:A\rightarrow B$$, we call $$\coker f$$ the *quotient object* and denote it by $$B\rightarrow B/A$$, or more simply by $$B/A$$.

## Chain complex

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> Consider the following data defined in an additive category $$\mathcal{A}$$.

- a collection of objects $$(A_n)_{n\in \mathbb{Z}}$$,
- a collection of morphisms $$(d_n:A_n \rightarrow A_{n-1})_{n\in \mathbb{Z}}$$

If this data satisfies the condition $$d_n\circ d_{n-1}=0$$, we call it a *chain complex* and write it as $$A_\bullet$$.

</div>

A morphism between chain complexes $$A_\bullet$$ and $$B_\bullet$$ is called a *chain map*; it is given by a collection of morphisms $$(f_n: A_n \rightarrow B_n)_{n\in \mathbb{Z}}$$ satisfying the condition $$d_n^B\circ f_n=f_{n-1}\circ d_n^A$$. This allows us to define the category $$\Ch(\mathcal{A})$$ of chain complexes.

If $$\mathcal{A}$$ is an abelian category, we can examine this in somewhat more detail. Let us fix the names and notation commonly used when dealing with chain complexes in this setting. First, each $$d_n$$ is called a *differential* or a *boundary map*, depending on context.

Their kernels and images are denoted respectively by

$$Z_n=\ker(d_{n-1}),\qquad B_n=\im(d_n)$$

and their elements are called *$$n$$-cycles* and *$$n$$-boundaries*, respectively. The elements of $$C_n$$ are called *$$n$$-chains*. It is not difficult to verify that the monomorphisms

$$Z_n \hookrightarrow B_n \hookrightarrow C_n$$

exist, and in this case we call the cokernel $$Z_n/B_n$$ the *$$n$$-th homology* of $$A_\bullet$$ and write it as $$H_n(A_\bullet)$$ or simply $$H_n(A)$$.

A chain complex in $$\mathcal{A}^\op$$ is called a *cochain complex*.

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> Suppose a chain complex $$A_\bullet$$ is given. Then

$$\cdots \rightarrow A_{n+1}\overset{d_{n+1}}{\longrightarrow}A_n\overset{d_n}{\longrightarrow}A_{n-1}\rightarrow\cdots$$

is *exact* at $$A_n$$ if the above monomorphism $$Z_n \rightarrow B_n$$ is an isomorphism. A chain complex that is exact everywhere is called an *exact sequence*.

</div>

<div class="example" markdown="1">

<ins id="ex6">**Example 6**</ins> The chain complex

$$\cdots 0 \rightarrow 0 \rightarrow A \rightarrow B \rightarrow C \rightarrow 0 \rightarrow 0 \rightarrow \cdots$$

is called a *short exact sequence*, and is abbreviated as

$$0 \rightarrow A \rightarrow B \rightarrow C \rightarrow 0$$

</div>

Suppose an additive functor $$F:\mathcal{A}\rightarrow \mathcal{B}$$ is given. Then for any chain complex $$A_\bullet$$ defined in $$\mathcal{A}$$, the data

$$\cdots \rightarrow F(A_{n+1}) \overset{F(d_{n+1})}{\longrightarrow} F(A_n) \overset{F(d_n)}{\longrightarrow} F(A_{n-1})\rightarrow\cdots$$

is easily verified to be a chain complex. That is, an additive functor $$F$$ induces a functor $$\Ch(\mathcal{A})\rightarrow \Ch(\mathcal{B})$$. However, for a general functor, the exactness of the original chain complex $$A_\bullet$$ does not guarantee that the new complex $$F(A_\bullet)$$ obtained as above is exact.

<div class="definition" markdown="1">

<ins id="def7">**Definition 7**</ins> An additive functor $$F: \mathcal{A} \rightarrow \mathcal{B}$$ is called *left exact* if for any short exact sequence

$$0 \rightarrow A \rightarrow B \rightarrow C \rightarrow 0$$

the sequence

$$0 \rightarrow F(A) \rightarrow F(B) \rightarrow F(C)$$

is exact. Similarly, $$F$$ is called *right exact* if, given any short exact sequence as above, the sequence

$$A \rightarrow B \rightarrow C \rightarrow 0$$

is exact. A functor that is both left exact and right exact is called an *exact functor*.

</div>

In other words, an additive functor that preserves kernels is called a left exact functor, and a functor that preserves cokernels is called a right exact functor. In particular, we can verify that a left adjoint functor is right exact, and a right adjoint functor is left exact.

Even if $$F$$ is contravariant, we can define left exactness and right exactness in the same way as above.

## Freyd-Mitchell embedding theorem

As we saw earlier, in an abelian category kernels, cokernels, images, and quotients are all defined. From this, theorems in $$\lMod{A}$$ can be transferred to an arbitrary abelian category. For instance, rewriting the first isomorphism theorem in the language of an arbitrary abelian category,

> Suppose a morphism $$f:A\rightarrow B$$ in an arbitrary abelian category $$\mathcal{A}$$ is given. Then $$A/\ker f\cong \im f$$ holds.

can be written as above, and the left-hand side becomes the quotient object obtained from $$i:\ker f\rightarrow A$$. Theorems of this kind can all be lifted to abelian categories, and their proofs can also be carried out using only the universal properties of kernels and cokernels, but these proofs are somewhat complicated.

Therefore, instead of proving such theorems one by one, we generally use the following theorem.

<div class="proposition" markdown="1">

<ins id="thm8">**Theorem 8 (Freyd-Mitchell embedding theorem)**</ins> For any small abelian category $$\mathcal{A}$$, there exist a suitable ring $$A$$ and a fully faithful exact functor $$F:\mathcal{A}\rightarrow\lMod{A}$$.

</div>

Therefore, we may just as well think of the objects of an arbitrary abelian category as $$A$$-modules and their morphisms as $$A$$-linear maps, and then perform calculations.

---

**References**

**[Wei]** C.A. Weibel. *An Introduction to Homological Algebra*. Cambridge Studies in Advanced Mathematics. Cambridge University Press, 1995.  
**[Vak]** R. Vakil, *The rising sea: foundations of algebraic geometry*. 2015. Preprint. [link](http://math.stanford.edu/~vakil/216blog/FOAGnov1817public.pdf)

---

[^1]: That these are actually sets is obvious from the fact that $$B^A$$ is a set. Therefore, the categories of algebraic structures discussed in the corresponding example are all locally small.
