---
title: "Cardinals"
description: "After reviewing the axiom of choice and the well-ordering theorem, we compare the sizes of sets using the equipotence relation, then define the concept of cardinal numbers and cardinal operations."
excerpt: "Definition of cardinal numbers"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/cardinals
sidebar: 
    nav: "set_theory-en"

date: 2021-09-04
weight: 23
translated_at: 2026-06-02T17:00:01+00:00
translation_source: kimi-cli
last_polished_at: 2026-11-03T07:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
## Review

First, let us briefly summarize the important topics from the previous post before moving on. We briefly constructed the natural numbers, and after that defined ordinal numbers and examined their properties. A topic not significantly related to ordinal numbers was well-ordering; first, a well-ordering is defined as follows.

::: definition Definition {#def-3}
On a set $A$, a totally ordered set $R$ defined on it is a *well-ordering* if every non-empty subset of $A$, $X$, has a least element. 
:::

And, in fact, we proved that every set can be given a well-order, and the proof relied on the following *Axiom of Choice*. 

::: misc The Axiom of Choice. {#axiom-choice}
Every set has a choice function.
:::


::: proposition Theorem (Zermelo) {#thm-2}
Every set $A$ can be given a well-order.
:::

::: proposition Theorem (Zorn's lemma) {#thm-1}
Every inductive set has a maximal element.
:::

Among the results proved using these, the one we will use this time is the following theorem.

::: proposition Proposition {#prop-0}
Let $A,B$ be two well-ordered sets. Then at least one of the following holds.
1. There exists an order isomorphism from $A$ to a segment of $B$, or
2. There exists an order isomorphism from $B$ to a segment of $A$.
:::

And finally, we saw that we can rigorously define the size of a set using ordinal numbers.

In this post, we define the size of a set in a somewhat less rigorous way and define operations on them. 

## Basic Definitions

In any case, let us begin. The cardinal of a set is a generalization of the size of the set, that is, the number of its elements. However, because we have not even defined the natural numbers yet, we must take a different perspective. Even if we cannot define how large a given set is, we can define when sets have the same size as follows.

::: Definition 1
A set $A$ is *equipotent* to a set $B$ if there exists a bijection from $A$ to $B$.
:::

Then

1. For any set $A$, $\id_A$ is a bijection from $A$ to $A$.
2. For any sets $A,B$, if there exists a bijection $f:A\rightarrow B$, then its inverse $f^{-1}:B\rightarrow A$ is a bijection from $B$ to $A$.
3. The composition of two bijections is also a bijection.

From the above, the only condition in the definition of an equivalence relation that is not satisfied is the condition that the above relation be reflexive *on a specific set $U$*; therefore, if only the problem that a universal set does not exist is resolved, this relation can be considered an equivalence relation defined on the universal set. 

Although this is not a rigorous solution, from now on we proceed under the assumption that this problem has been resolved. (See: [Wikipedia, Class](https://en.wikipedia.org/wiki/Class_(set_theory)))

::: Definition 2
A representative of the equivalence class of a set $A$ is called the *cardinal* of $A$, denoted by $\card A$.
:::

Since the empty set is unique, $\card\emptyset$ is precisely $\emptyset$. When dealing with cardinals, we write this set as $\mathbf{0}$. Sets with a single element, such as $\{a\}$ and $\{b\}$, are all mutually equipotent. This is because $\{(a,b)\}$ is a bijection from $\{a\}$ to $\{b\}$. Let us write this as $\mathbf{1}$. Although these do not yet become natural numbers, we will soon give operations to cardinals and view them like natural numbers.

Before defining operations, let us first define the order relation between cardinals.

::: Definition 3
The relation among cardinals

> $\mathfrak{a}$ is equipotent to a subset of $\mathfrak{b}$.

is an order relation, and we write this as $\mathfrak{a}\leq\mathfrak{b}$.
:::

Of course, we have not verified that this relation is indeed an order relation. However, the only non-trivial part is antisymmetry.

::: Lemma 4 (Cantor-Bernstein)
The relation $\leq$ above is antisymmetric.
:::
::: Proof
Suppose that for two cardinals $\mathfrak{a}$ and $\mathfrak{b}$, $\mathfrak{a}\leq\mathfrak{b}$ and $\mathfrak{b}\leq\mathfrak{a}$.  

If we let $i$ be a bijection from $\mathfrak{a}$ to a subset of $\mathfrak{b}$, then $i(\mathfrak{a})\subseteq\mathfrak{b}$ and $\mathfrak{a}$ and $i(\mathfrak{a})$ are equipotent. Therefore, it suffices to show that there exists a bijection between $i(\mathfrak{a})$ and $\mathfrak{b}$.  
Since $\mathfrak{b}\leq\mathfrak{a}$, there exists a bijection from $\mathfrak{b}$ to a subset of $\mathfrak{a}$, which can be viewed as an injection from $\mathfrak{b}$ to $\mathfrak{a}$. On the other hand, since $\mathfrak{a}$ is equipotent to $i(\mathfrak{a})$, composing the bijection between them with the previous injection yields an injection from $\mathfrak{b}$ to $i(\mathfrak{a})$. Let this be $f$. Now let $C_0=\mathfrak{b}\setminus i(\mathfrak{a})$, define $C_{n+1}=f(C_n)$ inductively, and set $C=\bigcup C_n$. We define $h:\mathfrak{b}\rightarrow i(\mathfrak{a})$ by the formula

$$h(x)=\begin{cases} f(x)&x\in C\\ x&x\not\in C\end{cases}$$

and will show that it is a bijection from $\mathfrak{b}$ to $i(\mathfrak{a})$.

First, $h$ is a function from $\mathfrak{b}$ to $i(\mathfrak{a})$. That $h$ is well-defined is clear, and we need only verify that the target of this function is $i(\mathfrak{a})$. If $x\in C$, then $h(x)=f(x)\in i(\mathfrak{a})$, which is clear, and if $x\not\in C$, then since $x\not\in C_0$, we have $x\not\in\mathfrak{b}\setminus i(\mathfrak{a})$. Therefore, in this case as well, $x\in i(\mathfrak{a})$.

Moreover, $h$ is injective. If $h(x)=h(y)$, then in the case where $x,y\in C$, we have $f(x)=f(y)$, and since $f$ is injective, $x=y$. And in the case where $x,y\not\in C$, clearly $x=y$.  
The non-trivial case is when one is an element of $C$ and the other is not an element of $C$. Suppose $x\in C$ and $y\not\in C$. Then $x\in C_n$ for some $n$, and in particular since $h(x)=f(x)\in C_{n+1}\subseteq C$, we have $h(x)\in C$. On the other hand, $h(y)=y$, and since $y\not\in C$ by assumption, this contradicts the assumption that $h(x)=h(y)$. Therefore, $x=y$ always holds, and $h$ is injective.

Finally, let us show that $h$ is surjective. For any $y\in i(\mathfrak{a})$, either $y\in C$ or $y\not\in C$. If $y\not\in C$, then $h(y)=y$ by the definition of $h$. If $y\in C$, then $y\in C_{n}$ for some $n\geq 1$ (since $y\in C_0=\mathfrak{b}\setminus i(\mathfrak{a})$ is impossible). Thus $y\in f(C_{n-1})$, so there exists $x\in C_{n-1}$ such that $y=f(x)$. Since this $x$ is also an element of $C$, $h(x)=f(x)=y$, and therefore $h$ is surjective.
:::

Furthermore, any set of cardinals is a well-ordered set.

::: Theorem 5
Any non-empty set $E$ of cardinals has a least element.
:::
::: Proof
Consider the set $A=\bigcup_{\mathfrak{a}\in E}\mathfrak{a}$. Then every cardinal $\mathfrak{a}\in E$ is a subset of $A$.

By the well-ordering principle, there exists a well-ordering on this set; denote it by $\leq$. Also, every subset of $A$ is equipotent to a segment of $A$ ([Proposition](#prop-0){: data-lid="md6h3" } in Review). Thus for any cardinal $\mathfrak{a}\in E$, the set of segments of $A$ equipotent to it is non-empty, and since the set $A^\ast$ of all segments of $A$ is well-ordered with respect to $\subseteq$ ([§Properties of Well-Ordered Sets, ⁋Proposition 1](/en/math/set_theory/well_ordering#prop1){: data-lid="ywgfe" }), there exists a least element. Denote this element by $\varphi(\mathfrak{a})$.  
If we show that $\mathfrak{a}\leq\mathfrak{b}$ is equivalent to $\varphi(\mathfrak{a})\subseteq\varphi(\mathfrak{b})$, then the proof will be complete by the well-orderedness of $A^\ast$. 

First, the latter condition clearly implies the former. Conversely, suppose $\mathfrak{a}\leq\mathfrak{b}$; that is, suppose $\mathfrak{a}$ is equipotent to a subset of $\mathfrak{b}=\varphi(\mathfrak{b})$ (equality holds as cardinals). If $\varphi(\mathfrak{b})\subseteq\varphi(\mathfrak{a})$ and $\varphi(\mathfrak{a})\neq\varphi(\mathfrak{b})$, then some segment of $\varphi(\mathfrak{b})$ would be equipotent to $\mathfrak{a}$, which contradicts the minimality of $\varphi(\mathfrak{a})$; therefore, the two conditions are equivalent.
:::

---
**References**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
