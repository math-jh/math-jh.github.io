---
title: "Definition of Order Relations"
description: "An order relation is defined as a binary relation satisfying reflexivity, transitivity, and antisymmetry. We also examine ordered sets equipped with such relations and the concept of order isomorphism."
excerpt: "Definition and properties of order relations"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/order_relations
sidebar: 
    nav: "set_theory-en"

date: 2021-08-22
weight: 14
translated_at: 2026-06-02T14:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-11-02T11:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
## Order Relations

::: Definition 1
A binary relation $R$ is said to be *anti-symmetric* if

> whenever $x\mathrel{R}y$ and $y\mathrel{R}x$, then $x=y$

always holds.
:::

Then an order relation is defined as follows.

::: Definition 2
A binary relation $(R,A,A)$ is called an *order relation* if $R$ is reflexive, transitive, and anti-symmetric.
:::

In this case, we say that $A$ is *ordered by* $R$, and we often call $A$ an *ordered set*. Also, as with equivalence relations, we write $x\mathrel{R}y$ as $x\leq_{\tiny R}y$.

::: Example 3
The binary relation $x=y$ is an order relation. The relation $x\subseteq y$ is also an order relation. ([§Ordered Pairs, ⁋Proposition 2](/en/math/set_theory/ordered_pair#prop2){: data-lid="xlgon" } and [§Ordered Pairs, ⁋Proposition 3](/en/math/set_theory/ordered_pair#prop3){: data-lid="fy2i4" }, and for antisymmetry, [§ZFC Axioms, ⁋The Axiom of Extensionality](/en/math/set_theory/zfc_axioms#axiom-extensionality){: data-lid="0fiq0" })
:::

Since an ordered set is a set equipped with an additional relation $\leq$, when we consider functions between such sets we usually focus on those that also preserve $\leq$. In particular, we define the following.

::: Definition 4
If for two order relations $(R, A, A)$ and $(R', A',A')$ there exists a bijection $f$ such that $x\leq_{\tiny R}y$ is equivalent to $f(x)\leq_{\tiny R'}f(y)$, then we call $f$ an *order isomorphism*.
:::

Henceforth, when we speak of an isomorphism between ordered sets, we shall always mean an order isomorphism.

We can do for order relations something analogous to [§Equivalence Relations, ⁋Proposition 3](/en/math/set_theory/equivalence_relations#prop3){: data-lid="ywgxl" }.

::: Proposition 5
A binary relation $(R,A,A)$ is an order relation if and only if the following two conditions hold.

$$R\circ R=R,\qquad R\cap R^{-1}=\Delta_A$$
:::
::: Proof
That the first condition is equivalent to transitivity was already shown in the proof of [§Equivalence Relations, ⁋Proposition 3](/en/math/set_theory/equivalence_relations#prop3){: data-lid="8aehr" }. In the second condition, $\Delta_A\subseteq R\cap R^{-1}$ is reflexivity, and the reverse inclusion $R\cap R^{-1}\subseteq\Delta_A$ is antisymmetry.
:::

## Preorder Relations

First let us look at the following example.

::: Example 6
Consider a function $f:A\rightarrow B$, and suppose an order relation $\leq$ is defined on $B$. Then, just as we derive an equivalence relation from a function, we can define a relation $\preceq$ on $A$ as follows. ([§Examples of Equivalence Relations, ⁋Definition 2](/en/math/set_theory/examples_of_equivalence#def2){: data-lid="93sml" })

$$x\preceq y\iff f(x)\leq f(y)$$

By definition $\preceq$ is reflexive and transitive. However, unless $f$ is injective, $\preceq$ does not generally satisfy antisymmetry.
:::

Therefore, we drop the antisymmetry condition and define the following.

::: Definition 7
A reflexive and transitive relation $R$ is called a *preorder relation*.
:::

If $R$ is a preorder relation we sometimes write it as $\preceq_{\tiny R}$, but since preorders share many properties with order relations, the same symbol $\leq_{\tiny R}$ is also commonly used. We too shall use $\leq_{\tiny R}$ unless there is a special reason not to.

To understand the properties of preorder relations, we must examine more closely antisymmetry, which is a property of order relations but not of preorders. If a relation $R$ were an order relation, antisymmetry would mean $(x\leq_{\tiny R}y)\wedge(y\leq_{\tiny R}x)\implies x=y$. We have seen that this does not hold for preorders, but in this case, by the following proposition, a *generalized equality* (that is, an equivalence relation) gives the same property.

::: Proposition 8
Let $R$ be a preorder relation. Then the relation '$x\leq_{\tiny R}y$ and $y\leq_{\tiny R}x$' is an equivalence relation.
:::
::: Proof
Let the above relation be $S$. We must show that $S$ is reflexive, symmetric, and transitive. First, it is obvious that this relation is reflexive: since $R$ is a preorder, $x\mathrel{R}x$ always holds for any $x$. On the other hand, for arbitrary $x$, $y$, suppose $x\mathrel{S}y$. Then 

$$x\mathrel{S}y\iff(x\leq_{\tiny R}y)\wedge(y\leq_{\tiny R}x)\iff(y\leq_{\tiny R}x)\wedge(x\leq_{\tiny R}y)\iff y\mathrel{S}x$$

so $S$ is symmetric. Finally, if $x\mathrel{S}y$ and $y\mathrel{S}z$, then

$$\begin{aligned}  (x\mathrel{S}y)\wedge(y\mathrel{S}z)&\iff((x\leq_{\tiny R}y)\wedge(y\leq_{\tiny R}x))\wedge((y\leq_{\tiny R}z)\wedge(z\leq_{\tiny R}y))\\
  &\iff(x\leq_{\tiny R}y)\wedge(y\leq_{\tiny R}x)\wedge(y\leq_{\tiny R}z)\wedge(z\leq_{\tiny R}y)\\
  &\iff(x\leq_{\tiny R}y)\wedge(y\leq_{\tiny R}z)\wedge(z\leq_{\tiny R}y)\wedge(y\leq_{\tiny R}x)\\
  &\iff((x\leq_{\tiny R}y)\wedge(y\leq_{\tiny R}z))\wedge((z\leq_{\tiny R}y)\wedge(y\leq_{\tiny R}x))\\
  &\implies(x\leq_{\tiny R}z)\wedge(z\leq_{\tiny R}x)\\
  &\iff x\mathrel{S}z
\end{aligned}$$

so $S$ is transitive, and therefore $S$ is an equivalence relation.
:::

## Strict order

Given an order relation $\leq$, let $<$ be the relation defined by the condition '$x\leq y$ and $x\neq y$'. Here, since $<$ is not reflexive, it can be neither an order relation nor a preorder. Instead, let us define the following.

::: Definition 9
A relation $R$ is said to be *asymmetric* if $x\mathrel{R}y$ implies $y\not{\mathrel{R}}x$. An asymmetric, transitive relation is called a *strict order*.
:::

To denote a strict order, we use $<_{\tiny S}$. Then the following holds.

::: Proposition 10
Let $R$ be an order relation. Then the new relation ‘$x\leq_{\tiny R}y$ and $x\neq y$’ is a strict order.  

Conversely, let $S$ be a strict order. Then the new relation ‘$x<_{\tiny S}y$ or $x=y$’ is an order relation.
:::

::: Proof
First, let $R$ be an order relation, and define a new relation $S$ by the condition that $x\leq_{\tiny R}y$ and $x\neq y$. To show asymmetry, we must show that $x\mathrel{S}y$ and $y\mathrel{S}x$ cannot hold simultaneously. Expanding $(x\mathrel{S}y)\wedge(y\mathrel{S}x)$ gives the following:
  
$$((x\leq_{\tiny R}y)\wedge(x\neq y))\wedge((y\leq_{\tiny R}x)\wedge(y\neq x))$$

But this can be written as follows:

$$((x\leq_{\tiny R}y)\wedge(y\leq_{\tiny R}x))\wedge(x\neq y)$$

By the antisymmetry of $R$, this is $(x=y)\wedge(x\neq y)$, which is always false; hence if $x\mathrel{S} y$ then $y\not{\mathrel{S}}x$. To show transitivity, let $x\mathrel{S}y$ and $y\mathrel{S}z$. Then by the transitivity of $\leq_{\tiny R}$, we have $x\leq_{\tiny R}z$, and if $x=z$, then $x\leq_{\tiny R}y$ and $y\leq_{\tiny R}x$ hold simultaneously, so by the antisymmetry of $R$ we have $x=y$, which contradicts $x\neq y$; thus $x\neq z$, and therefore $x\mathrel{S}z$.

Conversely, let $S$ be a strict order, and define a new relation $R$ by the condition that $x<_{\tiny S}y$ or $x=y$. First, since $x=x$, the latter condition gives $x\mathrel{R}x$. To show antisymmetry, assume that $x\mathrel{R}y$ and $y\mathrel{R}x$ hold. Then 

$$\begin{aligned}  
(x\mathrel{R}y)\wedge(y\mathrel{R}x)&\iff((x<_{\tiny S}y)\vee(x=y))\wedge((y<_{\tiny S}x)\vee(y=x))\\
   &\iff ((x<_{\tiny S}y)\wedge(y<_{\tiny S}x))\vee(x=y)
\end{aligned}$$

By asymmetry, $(x<_{\tiny S}y)\wedge(y<_{\tiny S}x)$ is impossible, so if $(x\mathrel{R}y)\wedge(y\mathrel{R}x)$ holds then necessarily $x=y$. Finally, to show transitivity, let $x\mathrel{R}y$ and $y\mathrel{R}z$. Then

$$\begin{aligned}
  (x\mathrel{R}y)\wedge(y\mathrel{R}z)&\iff ((x<_{\tiny S}y)\vee(x=y))\wedge((y<_{\tiny S}z)\vee(y=z))\\
  &\iff ((x<_{\tiny S}y)\wedge((y<_{\tiny S}z)\vee(y=z)))\vee((x=y)\wedge((y<_{\tiny S}z)\vee(y=z)))\\
  &\iff ((x<_{\tiny S}y)\wedge(y<_{\tiny S}z))\vee((x<_{\tiny S}y)\wedge(y=z))\\
  &\phantom{asdfghjkl}\vee((x=y)\wedge (y<_{\tiny S}z))\vee((x=y)\wedge(y=z))\\
  &\implies (x<_{\tiny S}z)\vee(x<_{\tiny S}z)\vee(x<_{\tiny S}z)\vee(x=y=z)\\
  &\implies x\mathrel{R}z
\end{aligned}$$

so $R$ is transitive. Therefore $R$ is an order relation.
:::

Henceforth, we write the strict order obtained from an order relation $R$ as $<_{\tiny R}$, and the order relation obtained from a strict order $S$ as $\leq_{\tiny S}$. Also, we write $x>y$ to mean $y<x$.

::: Remark 11
In general, $x\not\leq y$ does not imply $x>y$. Let $S=\left\{a,b\right\}$, and define the relation $\leq$ on $\mathcal{P}(S)$ to be the inclusion relation between subsets. Then this is obviously an order relation. Here, $\left\{a\right\}\not\leq \left\{b\right\}$, but $\left\{a\right\}>\left\{b\right\}$ does not hold either.
:::




---
**References**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.  
**[HJJ]** K. Hrbacek, T.J. Jeck, and T. Jech. *Introduction to Set Theory*. Lecture Notes in Pure and Applied Mathematics. M. Dekker, 1978.

---
