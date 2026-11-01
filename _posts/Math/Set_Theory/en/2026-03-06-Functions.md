---
title: "Functions"
description: "This post defines a binary relation as a function, explains the concepts of domain and function values, and covers constant functions and family notation."
excerpt: "Basic Definition of Functions"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/functions
sidebar: 
    nav: "set_theory-en"

date: 2021-08-15
weight: 5
translated_at: 2026-06-02T11:00:03+00:00
translation_source: kimi-cli
last_polished_at: 2026-11-01T03:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
In previous posts, we defined binary relations. According to this definition, for the set of natural numbers $\mathbb{N}$, the binary relation $<$ defined on it means the following set:

$${<}=\{(0,1),(0,2),\ldots, (1,2),(1,3),\ldots\}$$

{% diagram Math/Set_Theory/Functions-1.svg width="12.56em" alt="elements" %}

Now, following the notation of [§Binary Relations, ⁋Definition 6](/en/math/set_theory/binary_relation#def6){: data-lid="0h5zg" }, ${<}(1)$ is the collection of elements satisfying $(1,n)\in{<}$ among all $n\in\mathbb{N}$, and thus

$${<}(1)=\{2,3,\ldots\}$$

Conversely, if for every natural number $k$, information about the set ${<}(k)$ is given, we can also recover the set $<$.

The discussion above also holds for a general binary relation $(R,A,B)$, and thus being given an arbitrary binary relation $R$ can be thought of precisely as being given a rule that assigns, to each $a\in A$, the set $R(a)$. In this aspect, a function can be thought of as a binary relation such that for all $a\in A$, $R(a)$ is a singleton set.

## Definition of a Function

::: Definition 1
For a nonempty set $A$, a binary relation $f=(F,A,B)$ is called a *function* if $A=\pr_1F$ and for each $x\in A$, $F(\{x\})$ is a singleton set.[^1]
:::

The condition $A=\pr_1F$ means that in $A$, every element $x$ corresponds to *at least* one $y\in B$, and the second condition means that every $x\in A$ corresponds to *at most* one $y\in B$. Therefore, that $f=(F,A,B)$ is a function means that

> For every $x\in A$, there exists a *unique* $y\in B$ such that $(x,y)\in F$.

This $y$ is called the *function value* of $f$ at $x$, and in this case, the unique element of the set $F(\{x\})$ is denoted by $f(x)$. Also, the set $A=\pr_1F$ is called the *domain* of $f$.

Following the notation above, for the binary relation $F$, the image of a set $X\subseteq A$ is written, instead of $F(X)$, as $f(X)$, and the preimage of a set $Y\subseteq B$ is also written, instead of $F^{-1}(Y)$, as $f^{-1}(Y)$. ([§Binary Relations, ⁋Definition 4](/en/math/set_theory/binary_relation#def4){: data-lid="7awyn" } and [§Operations on Binary Relations, ⁋Definition 1](/en/math/set_theory/operation_of_binary_relations#def1){: data-lid="858xe" }) Also, the triple $f=(F,A,B)$ is simply written as $f:A\rightarrow B$.

Meanwhile, the set representing the function $f=(F,A,B)$,

$$F=\{(x,y)\mid (y=f(x))\wedge(x\in A)\}$$

can also be thought of as the *graph of the function* drawn on the "coordinate plane" $A\times B$, and more generally, a binary relation $R$ can also be thought of as the *graph of the binary relation*. A function $f$ is a *constant function* if for all $x,x'\in \pr_1 F$, $f(x)=f(x')$.

In special cases, expressions such as $f_x$ are also used to denote function values. When using this notation, the domain of $f$ is specifically called an *index set*, and in this case $F$ is called a *family*. When $f=(F,I,A)$ is regarded as a family, $F$ is denoted by $(f_i)_{i\in I}$.

If $f$ is a function from a set $A$ to $A$, then $x\in A$ is said to be *fixed* by $f$ if $f(x)=x$.

::: Definition 2
For any set $A$, the *identity function* $\id_A$ is defined as the triple $(\Delta_A,A,A)$. That is, $\id_A$ is the function defined for any $x\in A$ by the equation $\id_A(x)=x$.
:::

By definition, $\id_A$ is a function that fixes every element of $A$.

## Commutative diagram

When dealing with a large number of functions at once, it is convenient to use *diagrams* such as the following.

{% diagram Math/Set_Theory/Functions-2.svg width="14.24em" alt="commutative_diagram" %}

Here $A\overset{f}{\rightarrow}B$ is a concise notation for $f:A\rightarrow B$.  

In the situation above, if for any $x\in B$ we have $(i\circ g)(x)=(j\circ h)(x)$, then the following square

{% diagram Math/Set_Theory/Functions-3.svg width="9.84em" alt="commuting_square" %}

is said to *commute*. Similarly, that the following diagram

{% diagram Math/Set_Theory/Functions-4.svg width="5.62em" alt="commuting_triangle" %}

is a *commutative diagram* means that $h(x)=(f\circ g)(x)$ holds for all $x$. This situation is sometimes expressed concisely as $h=f\circ g$, a notation which implies not only that $H=F\circ G$ holds, but also that the sources and targets of both sides all coincide.

Meanwhile, when dealing with diagrams, even if not explicitly represented by arrows, we consider that for each object $A$, a function from $A$ to $A$, $\id_A$, is drawn. Therefore, strictly speaking, that the triangle above commutes includes not only $h=f\circ g$, but all of

$${\id_B}\circ h=f\circ g,\qquad h\circ{\id_C}=f\circ{\id_A}\circ g,\quad\cdots$$

However, by the properties of the identity function examined in [§Operations on Binary Relations, ⁋Definition 9](/en/math/set_theory/operation_of_binary_relations#def9){: data-lid="rj8bp" }, the above equations are all no different from $h=f\circ g$. On the other hand, that

{% diagram Math/Set_Theory/Functions-5.svg width="5.62em" alt="commuting_triangle_2" %}

commutes means that the following three conditions

$${\id_A}=g\circ h\circ f,\quad {\id_B}=f\circ g\circ h,\quad {\id_C}=h\circ f\circ g$$

all hold. In particular, that the following diagram

{% diagram Math/Set_Theory/Functions-6.svg width="5.28em" alt="inverses" %}

commutes means that $g\circ f=\id_A$ and $f\circ g=\id_B$.

## Extension and Restriction of Functions

::: Definition 3
Two functions $f=(F,A,B),f'=(F',A',B')$ are *compatible* on a set $S$ if $S$ is contained in the domains of $f$ and $f'$ respectively, and for all $x\in S$, $f(x)=f'(x)$.
:::

Let $f$ and $f'$ be two functions, and suppose $S=\pr_1 F\cap\pr_1 F'$ is non-empty. If the two functions are compatible on $S$, then with $\pr_1F\cup\pr_1F'$ as domain, a new function $g$ can be defined by the expression

$$g(x)=\begin{cases}f(x)&x\in \pr_1F\setminus\pr_1F'\\ f(x)=f'(x)&x\in \pr_1F\cap\pr_1F'\\ f'(x)&x\in\pr_1F'\setminus\pr_1F\end{cases}$$

We define this situation as follows.

::: Definition 4
Let $f=(F,A,B)$ and $f'=(F',A',B')$ be two functions. If $F\subseteq F'$ and $B\subseteq B'$, then $f'$ is called an *extension* of $f$, and we say that $f'$ extends $f$.
:::

Conversely, a function can also be restricted to a smaller domain. Let $f=(F,A,B)$ be a function and let $X\subseteq A$. If we define the relation $R$ by

> $(x\mathrel{R} y)$ if and only if $((x\in X)\wedge(y=f(x)))$

then the collection of $(x,y)$ satisfying this, $R$, becomes a function, and the domain of this function is $X$. Therefore, a new function can be defined as follows.

::: Definition 5
The function $R$ defined above is called the *restriction* of $f$ to $X$, and is denoted by $f\vert_{X}$.
:::



---
**References**

**[Bou]** N. Bourbaki, *Theory of Sets*. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---

[^1]: Strictly speaking, we have not yet defined the cardinality of a set, but this condition can be expressed as $x,y\in R(a)\implies x=y$, for instance.
