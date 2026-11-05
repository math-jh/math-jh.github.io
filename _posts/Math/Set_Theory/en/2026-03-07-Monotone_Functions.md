---
title: "Monotone Functions"
description: "Defines the restriction and product of preorders on subsets, and discusses how this structure extends to order relations."
excerpt: "Operations on ordered sets and monotone functions"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/monotone_functions
sidebar: 
    nav: "set_theory-en"

date: 2021-08-22
weight: 15
translated_at: 2026-06-02T21:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-11-05T03:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
## Restriction of a Preorder Relation

Consider a preorder relation $(R,A,A)$, and let any subset $A'\subseteq A$ be given. Then the relation defined by $R\cap (A'\times A')$ defines a preorder relation on $A'$.

::: Proposition 1
The above set $R\cap (A'\times A')$ is a preorder relation defined on $A'$.
:::
::: Proof
First, for any $x\in A'$, since $x$ is also an element of $A$, we have $(x,x)\in R$. Moreover, since $(x,x)\in A'\times A'$, it follows that $(x,x)\in R\cap(A'\times A')$.

Now suppose $(x,y),(y,z)\in R\cap (A'\times A')$. Then $x,y,z\in A'$ and $(x,y),(y,z)\in R$. Since $R$ is transitive, $(x,z)\in R$, and from $x,z\in A'$, we see that $(x,z)\in R\cap(A'\times A')$.
:::

Intuitively, this relation is the same as restricting $\leq_R$ to $A'$. By a slight abuse of notation, we also write this relation as $\leq_R$.

## Product of Preorder Relations

For any index set $I$, let preorder relations $(R_i,A_i,A_i)$ be given. Then, for any two elements $x=(x_i)_{i\in I}$ and $y=(y_i)_{i\in I}$ of the product set $\prod_{i\in I} A_i$, we can consider the following relation:

$$x\leq y\iff \forall i((i\in I)\implies(x_i\leq_{\tiny R_i} y_i))$$

::: Proposition 2
The above relation $\leq$ is a preorder relation defined on $\prod A_i$.
:::
::: Proof
For any $(x_i)\in \prod A_i$, since $x_i\leq_{\tiny R_i} x_i$ holds for all $i\in I$, we have $(x_i)\leq (x_i)$.

Now suppose $(x_i)\leq (y_i)$ and $(y_i)\leq (z_i)$. Then for all $i\in I$,

$$x_i\leq y_i\leq z_i\implies x_i\leq z_i$$

holds, and therefore $(x_i)\leq (z_i)$.
:::

::: Example 3
 A function from any set $A$ to $B$, $f$, can be viewed as an element of the set obtained by taking $A$ as the index set and taking, for each $a\in A$, the product of $B$, namely the set $B^A=\prod_{a\in A}B$.

Now, on a set $B$, suppose a preorder relation $R$ is defined. By the preceding [Proposition 2](#prop2){: data-lid="avdib" }, the product of preorder relations defines a preorder relation on the set of functions $B^A$. If we write this as $\leq$, then $f\leq g$ means that for any $x\in A$, $f(x)\leq_{\tiny R} g(x)$.
:::

The contents of the preceding two sections remain valid even if all preorder relations are replaced by order relations. That is, if the originally given preorder relations have antisymmetry and thus are order relations, then the preorder relations obtained in [Proposition 1](#prop1){: data-lid="gpisb" } and [Proposition 2](#prop2){: data-lid="xv0f2" } also satisfy antisymmetry and hence become order relations.

In this case, some care is needed when examining strict orders. For instance, suppose that on a set $B$ an order relation $R$ is given, and let the strict order defined by $R$ be $S$. From the order relation $\leq$ constructed through [Example 3](#ex3){: data-lid="ii8st" }, the resulting strict order $<$ is *different* from the relation defined by

$$f< g\iff\forall x\bigl((x\in A)\implies (f(x)<_{\tiny R}g(x))\bigr)$$

The relation $f<g$ holds even if for only *a single* $y\in A$ we have $f(y)<_{\tiny R} g(y)$, and for all remaining $x\in A$ we have $f(x)\leq_{\tiny R} g(x)$.

## Monotone Functions

::: Definition 4
Consider preorders $R,R'$ given on sets $A$ and $A'$, respectively. For a function $f:A\rightarrow A'$, being an *increasing function* means that $x\leq_{\tiny R} y\implies f(x)\leq_{\tiny R'} f(y)$ always holds. If $x\leq_{\tiny R}y\implies f(y)\leq_{\tiny R'} f(x)$ always holds, this function is called a *decreasing function*. Increasing and decreasing functions are collectively called *monotone functions*.
:::

::: remark Remark {#rmk}
Any constant function is both increasing and decreasing. However, the converse does not hold. Let $A$ be a set with two or more elements, and consider the order relation $=$ defined on it. Then the identity function from $A$ to $A$ is both increasing and decreasing, but is not a constant function.
:::

And replacing $\leq$ with $<$, we obtain the following definition.

::: Definition 5
Given strict orders $S,S'$, consider sets $A$ and $A'$. A function $f:A\rightarrow A'$ is a *strictly increasing function* if $x <_{\tiny S} y\implies f(x) <_{\tiny S'} f(y)$ is always true, and a *strictly decreasing function* if $x <_{\tiny S} y\implies f(y)<_{\tiny S'}f(x)$ always holds. Strictly increasing and strictly decreasing functions are collectively called *strictly monotone functions*.
:::

::: Remark 6
By definition, an injective monotone function is always strictly monotone. However, the converse does not always hold. For example, on $\mathbb{N}$, define a strict order $\prec$ by

$$m\prec n\iff ((n-m\text{ is even}) \wedge (m<n))$$

and let this set be $A$. That is, in $A$, even numbers can be compared with even numbers and odd numbers with odd numbers, but no comparison is possible between even and odd numbers. Also, let the ordered set obtained by endowing the set of natural numbers $\mathbb{N}$ with the usual strict order $<$ be $B$. Then the function from $A$ to $B$ given by $m\mapsto \lfloor m/2\rfloor$ is strictly increasing but not injective.
:::

::: Proposition 7
Let $A$ and $A'$ be ordered sets, let $u:A\rightarrow A'$ and $v:A'\rightarrow A$ be decreasing functions, and suppose that $v(u(x))\geq x$ and $u(v(x'))\geq x'$ hold for all $x\in A$ and $x'\in A'$. Then $u\circ v\circ u=u$ and $v\circ u\circ v=v$.
:::

::: Proof
Since $u$ is a decreasing function, from $v(u(x))\geq x$ we have that $u(v(u(x)))\leq u(x)$ holds for all $x$, but from the second part of the assumption, $u(v(u(x)))\geq u(x)$ holds. Since $A'$ is an ordered set, by antisymmetry we obtain $u(v(u(x)))=u(x)$, that is, $u\circ v\circ u=u$. Applying the same argument with $u$ and $v$ interchanged, we obtain $v\circ u\circ v=v$.
:::

---
**References**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
