---
title: "Continuous Functions"
description: "We define the notion of continuous functions in topological spaces, show that the composition of two continuous functions is continuous, and discuss equivalent conditions for continuous functions using open and closed sets."
excerpt: "Properties of continuous functions"

categories: [Math / Topology]
permalink: /en/math/topology/continuous_functions
sidebar: 
    nav: "topology-en"

date: 2022-11-13
weight: 5
translated_at: 2026-06-03T03:00:01+00:00
translation_source: kimi-cli
last_polished_at: 2026-11-08T07:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
## Continuous Functions

We now define the notion of a continuous function. Intuitively, this can be thought of as a function that preserves topological structure, just like a homomorphism in an algebraic setting.

::: Definition 1
For arbitrary topological spaces $X$, $Y$, that a function $f:X\rightarrow Y$ is *continuous* at $x\in X$ means that for every neighborhood of $f(x)\in Y$, $V$, there exists, such that $f(U)\subseteq V$, a neighborhood of $x$, $U$.
:::

Between arbitrary sets $X,Y$, for any function $f:X\rightarrow Y$ and any $U\subseteq X$, since $U\subseteq f^{-1}(f(U))$ holds, if any set $V\subseteq Y$ satisfies $f(U)\subseteq V$, then

$$U\subseteq f^{-1}(f(U))\subseteq f^{-1}(V)$$

holds. Therefore, to prove that a function $f:X\rightarrow Y$ between two topological spaces is continuous at $x\in X$, it suffices to show that for every neighborhood of $f(x)\in Y$, $V$, the set $f^{-1}(V)$ is a neighborhood of $x$, and more generally, it suffices to show that for a fixed local base of $f(x)$, $\mathcal{B}(f(x))$, and any $V\in\mathcal{B}(f(x))$, we have $f^{-1}(V)\in\mathcal{N}(x)$.

::: Proposition 2
For two topological spaces $X,Y$, let a function $f:X\rightarrow Y$ be continuous at a point $x$. If for some $A\subseteq X$ we have $x\in\cl(A)$, then $f(x)\in\cl(f(A))$.
:::
::: Proof
Choose any neighborhood of $f(x)\in Y$, $V$. Then since $f^{-1}(V)$ is a neighborhood of $x$, we have $f^{-1}(V)\cap A\neq\emptyset$ ([§Interior, Closure, and Boundary, ⁋Proposition 6](/en/math/topology/other_concepts#prop6){: data-lid="8n9ux" }), and if we let $x'\in f^{-1}(V)\cap A$, then $f(x')\in V\cap f(A)$. In particular, since $V\cap f(A)\neq\emptyset$, applying [§Interior, Closure, and Boundary, ⁋Proposition 6](/en/math/topology/other_concepts#prop6){: data-lid="gko4r" } again shows that $f(x)\in\cl(f(A))$.
:::

::: Proposition 3
Let topological spaces $X,Y,Z$ be given. If $f:X\rightarrow Y$ is continuous at a point $x\in X$ and $g:Y\rightarrow Z$ is continuous at $f(x)$, then the composition $g\circ f$ is also continuous at the point $x$.
:::
::: Proof
Choose any neighborhood of $(g\circ f)(x)$, $W$. Then since $g$ is continuous at $f(x)$, the set $g^{-1}(W)$ is a neighborhood of $f(x)$. Again, since $f$ is continuous at $x$, the set $f^{-1}(g^{-1}(W))$ is a neighborhood of $x$. ([\[Set Theory\] §Operations on Binary Relations, ⁋Proposition 6](/en/math/set_theory/operation_of_binary_relations#prop6){: data-lid="kek67" })
:::

If $f$ is continuous at every point of $X$, we call $f$ a *continuous function*. The following theorem shows several ways to define continuous functions.

::: Theorem 4
For two topological spaces $X,Y$ and a function $f:X\rightarrow Y$, the following are all equivalent.

1. $f$ is continuous.
2. For any subset of $X$, $A$, $f(\cl A)\subseteq\cl f(A)$ holds.
3. For any closed set in $Y$, $C$, $f^{-1}(C)$ is closed in $X$.
4. For any open set in $Y$, $V$, $f^{-1}(V)$ is open in $X$.
:::
::: Proof
That the first condition implies the second is a consequence of [Proposition 2](#prop2){: data-lid="ifvfg" }.

Now assume the second condition and show the third. For any closed set in $Y$, $C$, since the following inclusion

$$f(\cl(f^{-1}(C)))\subseteq \cl(f(f^{-1}(C)))\subseteq\cl(C)=C$$

holds, from

$$\cl(f^{-1}(C))\subseteq f^{-1}(f(\cl(f^{-1}(C))))\subseteq f^{-1}(C)$$

we see that $f^{-1}(C)$ is closed. Since the identity $(f^{-1}(A))^c=f^{-1}(A^c)$ holds for any subset $A\subseteq Y$, it is obvious that the fourth condition also follows from this.

Therefore, it suffices to assume the fourth condition and show the first. Choose any $x\in X$, and let an arbitrary neighborhood of $f(x)\in Y$, $V$, be given. Then there exists, satisfying $f(x)\in V'\subseteq V$, an *open neighborhood* of $f(x)$, $V'$. Now from the fourth condition, $f^{-1}(V')$ is an open neighborhood of $x\in X$, and from $f^{-1}(V')\subseteq f^{-1}(V)$, we see that $f^{-1}(V)$ is a neighborhood of $x$.
:::

By [Proposition 3](#prop3){: data-lid="1cr1z" }, we know that if two continuous functions $f:X\rightarrow Y$ and $g:Y\rightarrow Z$ are given, then $g\circ f$ is also continuous.

Between two topological spaces $(X,\mathcal{T}_X), (Y,\mathcal{T}_Y)$, let a continuous function $f:X\rightarrow Y$ be given. Then for any $V\in\mathcal{T}_Y$, we have $f^{-1}(V)\in\mathcal{T}_X$, so the following expression

$$f^\mathcal{T}(V):=f^{-1}(V),\qquad V\in\mathcal{T}_Y$$

well-defines a function $f^\mathcal{T}:\mathcal{T}_Y\rightarrow\mathcal{T}_X$.

Now assume that $f$ is a bijection and consider two distinct elements of $\mathcal{T}_Y$, $V_1,V_2$. Without loss of generality, suppose $y\in V_1\setminus V_2$; then

$$f^{-1}(y)\in f^\mathcal{T}(V_1)\setminus f^\mathcal{T}(V_2)$$

holds, so $f^{\mathcal{T}}$ is an injective function.

::: Example 5
In general, $f^{\mathcal{T}}$ need not be a surjective function. For instance, let the space obtained by equipping $\mathbb{N}$ with the discrete topology $\mathcal{T}_1$ be $X_1$, and with the trivial topology $\mathcal{T}_2$ be $X_2$. If we consider the identity map as sets $\id:\mathbb{N}\rightarrow\mathbb{N}$, then $\id$ is a continuous bijection, but the function

$$\id^\mathcal{T}:\mathcal{T}_2\rightarrow\mathcal{T}_1$$

cannot be surjective. ([\[Set Theory\] §Operations on Cardinals, ⁋Proposition 10](/en/math/set_theory/operation_of_cardinals#prop10){: data-lid="kuoq3" })
:::

However, if for a bijection $f$, its inverse function $f^{-1}$ is also continuous, then $(f^{-1})^\mathcal{T}:\mathcal{T}_X\rightarrow\mathcal{T}_Y$ is well-defined, and since it is obvious from the definition that

$$f^\mathcal{T}\circ (f^{-1})^\mathcal{T}=\id_{\mathcal{T}_X},\qquad (f^{-1})^\mathcal{T}\circ f^\mathcal{T}=\id_{\mathcal{T}_Y}$$

holds, $f^\mathcal{T}$ is also a bijection. We define such a situation as follows.

::: Definition 6
A continuous function $f:X\rightarrow Y$ is called a *homeomorphism* if there exists another continuous function $g:Y\rightarrow X$ such that $f\circ g=\id_Y$ and $g\circ f=\id_X$.
:::

That is, for two topological spaces $X,Y$ to be homeomorphic means not only that there exists a bijection between them as sets, but also that this bijection makes even the topological structures of the two sets, namely the open sets, behave in exactly the same way. An example of a continuous bijection that is not a homeomorphism is precisely [Example 5](#ex5){: data-lid="zi95m" } above.

---

**References**

**[Bou]** N. Bourbaki, <i>General Topology</i>. Elements of mathematics. Springer, 1995.

---
