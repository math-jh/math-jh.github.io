---
title: "Krull Dimension"
description: "This post introduces the definition of Krull dimension in commutative algebra, defines the notions of ideals and codimension, and covers dimension computations in Noetherian rings."
excerpt: "Krull dimension via prime chains and its basic properties"

categories: [Math / Commutative Algebra]
permalink: /en/math/commutative_algebra/Krull_dimension
sidebar: 
    nav: "commutative_algebra-en"

date: 2025-01-16
weight: 16
translated_at: 2026-08-27T21:45:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-06T11:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
## Definition of Dimension

In the next few posts, we define the dimension of a ring and examine its properties. The definition of dimension itself is not difficult.

::: Definition 1
The *Krull dimension* of a ring $A$ is defined, over descending chains of prime ideals of $A$

$$\mathfrak{p}_r\supsetneq \mathfrak{p}_{r-1}\supsetneq\cdots\supsetneq \mathfrak{p}_1\supsetneq \mathfrak{p}_0$$

as the supremum of the lengths $r$, and is denoted by $\dim A$. If no such $r$ exists, we define $\dim A=\infty$.
:::

For short, we simply call the Krull dimension of a ring $A$ the dimension of $A$. For example, a field $\mathbb{K}$ has the unique prime ideal $(0)$, so $\mathbb{K}$ is always $0$-dimensional.

More generally, we define the following.

::: Definition 2
For a ring $A$ and an ideal $\mathfrak{a}$, the dimension of $\mathfrak{a}$ is defined by

$$\dim \mathfrak{a}=\dim A/\mathfrak{a}$$

In $A$, for a prime ideal $\mathfrak{p}$, the *codimension* of $\mathfrak{p}$, $\codim \mathfrak{p}$, is defined as the dimension of $A_\mathfrak{p}$; for a general ideal $\mathfrak{a}$, $\codim \mathfrak{a}$ is defined as the minimum of the codimensions of the prime ideals containing $\mathfrak{a}$.

Finally, for an arbitrary $A$-module $M$, the dimension and codimension of $M$ are defined as the dimension and codimension of $\ann(M)$, respectively.
:::

As a point of caution, under the definition above, $\mathfrak{a}$ has two definitions of dimension: its dimension as an ideal defined first, and its dimension when viewed as an $A$-module; the values given by these two definitions may differ. Therefore, when using the notation $\dim \mathfrak{a}$, we mean only the dimension as an ideal of $A$, as defined first in [Definition 2](#def2){: data-lid="fu4uw" }.

Then, by [§Localization, ⁋Proposition 8](/en/math/commutative_algebra/localization#prop8){: data-lid="kyj3x" }, $\codim \mathfrak{p}$ is equal to the supremum of the lengths of decreasing chains starting from the prime ideal $\mathfrak{p}$

$$\mathfrak{p}=\mathfrak{p}_r\supsetneq \mathfrak{p}_{r-1}\supsetneq\cdots\supsetneq \mathfrak{p}_1\supsetneq \mathfrak{p}_0$$

Therefore, the following inequality

$$\dim \mathfrak{a}+\codim \mathfrak{a}\leq \dim A$$

holds. Contrary to what its name suggests, the reverse inequality does not hold in general.

On the other hand, for a local ring $(A, \mathfrak{m})$, any chain of prime ideals giving $\dim A$ can always have $\mathfrak{m}$ inserted at the beginning, so $\dim A=\codim \mathfrak{m}$ necessarily holds.

## Computing Dimensions

In general, when dealing with dimension, one mostly considers the case where the ring $A$ is Noetherian. One of the main reasons is that [Theorem 7](#thm7){: data-lid="6waej" } holds only for Noetherian rings. Before computing dimensions in earnest, let us first look at a simple example.

First, through the equivalence between the first and third conditions of [§The Jordan-Hölder Theorem, ⁋Theorem 4](/en/math/commutative_algebra/Jordan-Holder_theorem#thm4){: data-lid="yu1m9" }, we know precisely what $0$-dimensional Noetherian rings are.

::: Corollary 3
For a Noetherian ring $A$, $\dim A =0$ if and only if $A$ is Artinian.
:::

Meanwhile, by the following proposition, we know that in general, if $\phi:A \rightarrow B$ is integral, then the dimension of an ideal of $B$ is equal to the dimension of its preimage.

::: Proposition 4
Let $\phi: A \rightarrow B$ be integral. Then for any prime ideal containing $\ker\phi$ of $A$, $\mathfrak{p}$, there exists, such that $\mathfrak{p}=\phi^{-1} \mathfrak{q}$, a prime ideal of $B$, $\mathfrak{q}$. Moreover, for any ideal of $B$, $\mathfrak{b}$, we have $\dim \mathfrak{b}=\dim \phi^{-1} \mathfrak{b}$.
:::
::: Proof
The first statement is simply [§Integral Extensions and Ideals, ⁋Proposition 1](/en/math/commutative_algebra/lying_over_and_going_up#prop1){: data-lid="ffffe" }. For the second, since $\phi^{-1}\mathfrak{b}$ is the kernel of the composition $A \rightarrow B \rightarrow B/\mathfrak{b}$, $A/\phi^{-1}\mathfrak{b}\hookrightarrow B/\mathfrak{b}$ is also an integral extension; the inequality $\dim \mathfrak{b}\geq \dim \phi^{-1}\mathfrak{b}$ holds by the second statement of [§Integral Extensions and Ideals, ⁋Proposition 1](/en/math/commutative_algebra/lying_over_and_going_up#prop1){: data-lid="n9pyo" }, and the reverse inequality holds by [§Integral Extensions and Ideals, ⁋Corollary 4](/en/math/commutative_algebra/lying_over_and_going_up#cor4){: data-lid="n2ayk" }.
:::

We now turn our attention to what happens in dimension 1. Before that, we make the following somewhat technical definition.

::: Definition 5
For a prime ideal $\mathfrak{p}\subseteq A$, the *$n$th symbolic power* of $\mathfrak{p}$, $\mathfrak{p}^{(n)}$, is defined by the following equation:

$$\mathfrak{p}^{(n)}=\{a\in A\mid\text{$ba\in \mathfrak{p}^n$ for some $b\in A\setminus \mathfrak{p}$}\}$$
:::

By definition, $\mathfrak{p}^{(n)}$ is obtained via the localization $A \rightarrow A_\mathfrak{p}$ by transferring the ideal $(\mathfrak{p}A_\mathfrak{p})^n$ to $A$. Then elements outside $\mathfrak{p}$ become non-zerodivisors modulo $\mathfrak{p}^{(n)}$, and it is clear that $\mathfrak{p}^{(n)}A_\mathfrak{p}=(\mathfrak{p}A_\mathfrak{p})^n$. There is also a descending chain of symbolic powers

$$A=\mathfrak{p}^{(0)}\supseteq \mathfrak{p}=\mathfrak{p}^{(1)}\supseteq \mathfrak{p}^{(2)}\supseteq \mathfrak{p}^{(3)}\supseteq\cdots$$

We can now prove the following theorem.

::: Theorem 6 (Codimension one Principal Ideal Theorem)
Let $A$ be a Noetherian ring and let $a\in A$ be arbitrary. Suppose $\mathfrak{p}$ is minimal among the prime ideals containing the principal ideal $\mathfrak{a}=(a)$. Then $\codim \mathfrak{p}\leq 1$.
:::

::: Proof
It suffices to show that $\codim \mathfrak{q}=0$ for every prime ideal $\mathfrak{q}\subsetneq \mathfrak{p}$, which in turn, by [§Localization, ⁋Proposition 8](/en/math/commutative_algebra/localization#prop8){: data-lid="ny1o2" }, reduces to showing that $\dim A_\mathfrak{q}=0$.

Now, in $A_\mathfrak{p}$ the ideal $\mathfrak{p}A_\mathfrak{p}$ is the unique maximal ideal, so the ideals $\mathfrak{q}A_\mathfrak{p}$, $(\mathfrak{q}A_\mathfrak{p})^{(n)}$, and $\mathfrak{a}A_\mathfrak{p}$ are all contained in this maximal ideal. In particular, we obtain the following two chains

$$\mathfrak{a}A_\mathfrak{p}\subseteq (\mathfrak{q}A_\mathfrak{p})^{(n)}+\mathfrak{a}A_\mathfrak{p}\subseteq \mathfrak{p}A_\mathfrak{p},\qquad \mathfrak{q}A_\mathfrak{p}\subseteq \mathfrak{p}A_\mathfrak{p}$$

Meanwhile, since $\mathfrak{p}A_\mathfrak{p}$ is minimal among the prime ideals containing $\mathfrak{a}A_\mathfrak{p}$, the ring $A_\mathfrak{p}/\mathfrak{a}A_\mathfrak{p}$ is Artinian by [§The Jordan-Hölder Theorem, ⁋Corollary 8](/en/math/commutative_algebra/Jordan-Holder_theorem#cor8){: data-lid="6uki0" }. From this, we know that the descending chain of symbolic powers

$$(\mathfrak{q}A_\mathfrak{p})^{(1)}+\mathfrak{a}A_\mathfrak{p}\supseteq (\mathfrak{q}A_\mathfrak{p})^{(2)}+\mathfrak{a}A_\mathfrak{p}\supseteq\cdots $$

must stabilize. Thus, let $(\mathfrak{q}A_\mathfrak{p})^{(n)}+\mathfrak{a}A_\mathfrak{p}= (\mathfrak{q}A_\mathfrak{p})^{(n+1)}+\mathfrak{a}A_\mathfrak{p}$. Then, since

$$(\mathfrak{q}A_\mathfrak{p})^{(n)}\subseteq (\mathfrak{q}A_\mathfrak{p})^{(n)}+\mathfrak{a}A_\mathfrak{p}= (\mathfrak{q}A_\mathfrak{p})^{(n+1)}+\mathfrak{a}A_\mathfrak{p}$$

any $f\in (\mathfrak{q}A_\mathfrak{p})^{(n)}$ can be written in the form

$$f=\alpha a+g,\qquad g\in (\mathfrak{q}A_\mathfrak{p})^{(n+1)}\subseteq (\mathfrak{q}A_\mathfrak{p})^{(n)}$$

and from this we must have $\alpha a\in (\mathfrak{q}A_\mathfrak{p})^{(n)}$. But in this expression, since $\mathfrak{p}$ is minimal among the primes containing $\mathfrak{a}$, we have $a\not\in \mathfrak{q}$, and therefore $\alpha\in (\mathfrak{q}A_\mathfrak{p})^{(n)}$. In other words, the equality

$$(\mathfrak{q}A_\mathfrak{p})^{(n)}=\mathfrak{a}(\mathfrak{q}A_\mathfrak{p})^{(n)}+(\mathfrak{q}A_\mathfrak{p})^{(n+1)}$$

holds. Now, passing to $A_\mathfrak{p}/(\mathfrak{q}A_\mathfrak{p})^{(n+1)}$, we have

$$(\mathfrak{q}A_\mathfrak{p})^{(n)}=\mathfrak{a}(\mathfrak{q}A_\mathfrak{p})^{(n)}\pmod{(\mathfrak{q}A_\mathfrak{p})^{(n+1)}}$$

and since $a\in \mathfrak{p}A_\mathfrak{p}=J(A_\mathfrak{p})$, [§Integral Extensions, ⁋Lemma 8](/en/math/commutative_algebra/integral_extension#lem8){: data-lid="l8ecd" } gives $(\mathfrak{q}A_\mathfrak{p})^{(n)}=0\pmod{(\mathfrak{q}A_\mathfrak{p})^{(n+1)}}$. That is, $(\mathfrak{q}A_\mathfrak{p})^{(n)}=(\mathfrak{q}A_\mathfrak{p})^{(n+1)}$. Localizing this equality at $\mathfrak{q}$ now gives

$$(\mathfrak{q}A_\mathfrak{q})^{n+1}=(\mathfrak{q}A_\mathfrak{q})^{n}$$

and since $\mathfrak{q}A_\mathfrak{q}=J(A_\mathfrak{q})$, we have $(\mathfrak{q}A_\mathfrak{q})^{n}=0$. Now, from the equivalence of the second and third conditions of [§The Jordan-Hölder Theorem, ⁋Corollary 8](/en/math/commutative_algebra/Jordan-Holder_theorem#cor8){: data-lid="dsjy3" }, the ring $A_\mathfrak{q}=A_\mathfrak{q}/(0)$ is Artinian, and therefore we know that $\dim A_\mathfrak{q}=0$ by [Corollary 3](#cor3){: data-lid="io2lp" }.
:::

Using this, we can now prove the following by induction.

::: Theorem 7 (Principal Ideal Theorem)
For a Noetherian ring $A$ and any $a_1,\ldots, a_c\in A$, let $\mathfrak{p}$ be minimal among the prime ideals containing $a_1,\ldots, a_c$. Then $\codim \mathfrak{p}\leq c$. 
:::

That is, any prime ideal of a Noetherian ring satisfies the descending chain condition, and the length of a chain starting at $\mathfrak{p}$ is less than or equal to the number of generators of $\mathfrak{p}$. Nevertheless, there exist Noetherian rings of infinite dimension. (**[Nag, Appendix, Example 1]**)

On the other hand, [Theorem 7](#thm7){: data-lid="etgwe" } also has the following converse.

::: Corollary 8
In a Noetherian ring $A$, a codimension $c$ prime ideal $\mathfrak{p}$ is minimal among the prime ideals containing some ideal generated by $c$ elements. 
:::
::: Proof
As claimed, suppose that $\mathfrak{p}$ has codimension $c$. Starting from the ideal generated by $0$ elements, that is, the zero ideal $(0)$, we will inductively choose elements $x_1,\ldots, x_r$ to construct the desired ideal. Now, given $0\leq r< c$, suppose that for $r$ we have constructed the ideal generated by $x_1,\ldots, x_r$. Then, so that it does not belong to any of the minimal prime ideals containing the ideal $(x_1,\ldots, x_r)$, we must choose a suitable $x_{r+1}\in \mathfrak{p}$.

Now let the minimal prime ideals containing $(x_1,\ldots, x_r)$ be $\mathfrak{q}_1,\ldots, \mathfrak{q}_s$. By [Theorem 7](#thm7){: data-lid="v73fq" }, the codimension of each $\mathfrak{q}_i$ is $\leq r$, and since $r< c$, their codimensions are all $< c$. Therefore, $\mathfrak{p}$ cannot be equal to any of these, and in particular $\mathfrak{p}\not\subseteq \bigcup_{i=1}^s \mathfrak{q}_i$. Hence we can choose $x_{r+1}\in \mathfrak{p}\setminus \bigcup_{i=1}^s \mathfrak{q}_i$.

Now, inductively, in $\mathfrak{p}$ we obtain $c$ elements $x_1,\ldots, x_c$. Then, if we choose a minimal prime ideal containing the ideal $(x_1,\ldots, x_c)$, say $\mathfrak{q}$, by [Theorem 7](#thm7){: data-lid="uypzt" } we have $\codim \mathfrak{q}\leq c$. On the other hand, since $\mathfrak{q}\subseteq \mathfrak{p}$ and $\codim \mathfrak{p}=c$, we must have $\mathfrak{q}=\mathfrak{p}$.
:::

If in the corollary above $\codim \mathfrak{p}=0$, then $\mathfrak{p}$ is a minimal prime containing an ideal generated by $0$ elements, that is, the zero ideal. Now, by [§Associated Primes, ⁋Theorem 7](/en/math/commutative_algebra/associated_primes#thm7){: data-lid="bdox3" }, such a prime ideal consists only of zerodivisors. Combining this with [Theorem 6](#thm6){: data-lid="u8770" }, we see that if $\mathfrak{p}$ is a minimal prime ideal containing a *non-zerodivisor* $a$, then we must have $\codim \mathfrak{p}=1$. 

In particular, for a minimal prime containing a non-zerodivisor $a$, say $\mathfrak{p}$,

$$\dim A/\mathfrak{p}+\codim \mathfrak{p}=\dim \mathfrak{p}+\codim \mathfrak{p}\leq \dim A$$

holds, and since $\codim \mathfrak{p}=1$,

$$\dim A/\mathfrak{p}\leq\dim A-1$$

holds. 

In particular, for a Noetherian local ring $(A, \mathfrak{m})$, we have seen that $\dim A=\codim \mathfrak{m}$ holds. Therefore, if we let $d=\dim A=\codim \mathfrak{m}$, by [Theorem 7](#thm7){: data-lid="1e8du" }, $\mathfrak{m}$ must be generated by at least $d$ elements. 

## Dimension in Graded Rings

Let us examine some properties that are useful when computing dimension in a graded ring $R = \bigoplus_{d \ge 0} R_d$. We have already defined homogeneous ideals along with their equivalent conditions in [\[Algebraic Structures\] §Graded Rings, ⁋Proposition 6](/en/math/algebraic_structures/graded_rings#prop6){: data-lid="deh0k" }; in particular, an element of a homogeneous ideal has all of its homogeneous components inside that ideal. We give one more name to this.

::: Definition 9
In a graded ring $R$, a prime ideal $\mathfrak{p}$ is called a *homogeneous prime ideal* if $\mathfrak{p}$ is a homogeneous ideal.
:::

The key observation in graded rings is that prime ideals containing the irrelevant ideal $\mathfrak{m} = \bigoplus_{d > 0} R_d$ are always homogeneous.

::: Proposition 10
In a graded ring $R$, if the irrelevant ideal $\mathfrak{m} = \bigoplus_{d > 0} R_d$ is contained in a prime ideal $\mathfrak{p}$, then this prime ideal is homogeneous.
:::
::: Proof
Suppose $\mathfrak{p}$ is a prime ideal and $\mathfrak{m} \subseteq \mathfrak{p}$. Consider the *homogenization* of $\mathfrak{p}$:

$$\mathfrak{p}^\ast = \langle x \in \mathfrak{p} \mid x \text{ homogeneous}\rangle$$

That this is a graded prime ideal can be seen immediately from the definition. The key point is that $\mathfrak{p} = \mathfrak{p}^\ast$. First, since $\mathfrak{m} \subseteq \mathfrak{p}^\ast \subseteq \mathfrak{p}$ is clear, let us assume $x \in \mathfrak{p}$ and show that $x\in \mathfrak{p}^\ast$.

Write $x$ as its homogeneous decomposition $x = \sum_{d} x_d$. Since $x_+ = \sum_{d > 0} x_d \in \mathfrak{m} \subseteq \mathfrak{p}$, we have $x_0 = x - x_+ \in \mathfrak{p}$. Now $x' = x - x_0 = x_+ \in \mathfrak{p}$, and in the same way one can show that $x_1 \in \mathfrak{p}$. Inductively, each $x_d \in \mathfrak{p}$, and therefore $x \in \mathfrak{p}^\ast$.
:::

From [Proposition 10](#prop10){: data-lid="w51kh" }, we know that prime ideals containing the irrelevant ideal $\mathfrak{m}$ are homogeneous. Conversely, the homogeneous prime ideals not containing $\mathfrak{m}$ correspond to the points of $\operatorname{Proj} R$. We now examine an operation that associates a homogeneous prime ideal to an arbitrary prime ideal.

::: Proposition 11
For a graded ring $R$ and a prime ideal $\mathfrak{p}$, the ideal generated by the homogeneous elements belonging to $\mathfrak{p}$, $\mathfrak{p}^\ast$, is the largest homogeneous ideal contained in $\mathfrak{p}$, and it is also a prime ideal.
:::
::: Proof
By definition, $\mathfrak{p}^\ast$ is generated by homogeneous elements, so it is a homogeneous ideal, and since all of its generators belong to $\mathfrak{p}$, we have $\mathfrak{p}^\ast \subseteq \mathfrak{p}$. Now if $\mathfrak{a}\subseteq \mathfrak{p}$ is a homogeneous ideal, then by the third condition of [\[Algebraic Structures\] §Graded Rings, ⁋Proposition 6](/en/math/algebraic_structures/graded_rings#prop6){: data-lid="45e14" }, $\mathfrak{a}$ is generated by homogeneous elements, and since these generators are all homogeneous elements belonging to $\mathfrak{p}$, we have $\mathfrak{a}\subseteq \mathfrak{p}^\ast$. Thus $\mathfrak{p}^\ast$ is the largest homogeneous ideal contained in $\mathfrak{p}$.

Now let us show that $\mathfrak{p}^\ast$ is prime. First, since $\mathfrak{p}^\ast \subseteq \mathfrak{p}\subsetneq R$, we have $\mathfrak{p}^\ast\neq R$. Then by the third condition of [§Localization of Graded Rings, ⁋Lemma 2](/en/math/commutative_algebra/localization_of_graded_rings#lem2){: data-lid="1d27h" }, it suffices to show that whenever $ab\in \mathfrak{p}^\ast$ for any homogeneous elements $a,b\in R$, either $a\in \mathfrak{p}^\ast$ or $b\in \mathfrak{p}^\ast$. But $ab\in \mathfrak{p}^\ast\subseteq \mathfrak{p}$ and $\mathfrak{p}$ is prime, so $a\in \mathfrak{p}$ or $b\in \mathfrak{p}$; and since $a$ and $b$ are homogeneous, whichever of them lies in $\mathfrak{p}$ is a generator of $\mathfrak{p}^\ast$, and in particular an element of $\mathfrak{p}^\ast$.
:::

For an arbitrary chain of prime ideals $\mathfrak{p}_0 \supsetneq \cdots \supsetneq \mathfrak{p}_s$, we have $\mathfrak{p}_0^\ast \supseteq \cdots \supseteq \mathfrak{p}_s^\ast$, but these inclusions need not be strict. When $R=\mathbb{K}[\x]$ is given the standard grading, every element of $(\x-1)$ vanishes at $\x=1$, whereas the value of a homogeneous element $c\x^n$ at $\x=1$ is $c$; hence the only homogeneous element belonging to $(\x-1)$ is $0$. Thus both terms of the chain $(\x-1)\supsetneq (0)$ are sent to $(0)$. On the other hand, in a chain of prime ideals all containing the irrelevant ideal $\mathfrak{m}$, each term is already homogeneous by [Proposition 10](#prop10){: data-lid="5c40w" }, so such a chain is itself a chain of homogeneous prime ideals.

## Regular Local Rings

::: Definition 12
A Noetherian local ring $(A, \mathfrak{m})$ is called a *regular local ring* if, for $d=\dim A$, the ideal $\mathfrak{m}$ can be generated by exactly $d$ elements.
:::

Then, by [§Integral Extensions, ⁋Lemma 8](/en/math/commutative_algebra/integral_extension#lem8){: data-lid="xkrij" }, the images of $a_1,\ldots, a_d\in \mathfrak{m}$ in $\mathfrak{m}/\mathfrak{m}^2$ generate $\mathfrak{m}/\mathfrak{m}^2$ as an $A/\mathfrak{m}$-vector space if and only if $a_1,\ldots, a_d$ generate $\mathfrak{m}$ as an $A$-module. We will study their properties further at the end of the next post.

---

**References**

**[Eis]** David Eisenbud. *Commutative Algebra: with a view toward algebraic geometry*. Springer, 1995.  
**[Nag]** Masayoshi Nagata. *Local Rings*. Interscience publishers, 1962.

---
