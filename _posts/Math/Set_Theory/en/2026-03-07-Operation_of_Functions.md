---
title: "Operations on Functions"
description: "We define function composition as the composition of binary relations, and explore when an inverse function exists through the concepts of injective, surjective, and bijective functions."
excerpt: "Inverse and composition of functions, surjective and injective functions"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/operation_of_functions


sidebar: 
    nav: "set_theory-en"

date: 2022-11-23

weight: 6
translated_at: 2026-06-02T19:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-11-04T03:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
A function is a binary relation satisfying certain conditions, and we have already defined the composition and inverse of binary relations. For the composition and inverse of functions to be well-defined, the result of composing them as binary relations or taking their inverse as binary relations must itself be a function.

## Composition of Functions

The composition of functions is nothing special.

::: Proposition 1
Consider functions $f:A\rightarrow B$ and $g:B\rightarrow C$. Then $g\circ f$ is a function from $A$ to $C$.
:::
::: Proof
First, that the domain of $g\circ f$ is all of $A$ is immediate: the value of $f$ is defined for every element of $A$, and the value of $g$ is defined for every element of $B$, in particular for every element of $f(A)\subseteq B$. Therefore, to prove the given proposition it suffices to show:

> For any $x\in A$, if $(x,z)$, $(x,z')\in G\circ F$, then necessarily $z=z'$.

Suppose $(x,z),(x,z')\in G\circ F$. Then, by the definition of $G\circ F$, there exist elements satisfying $(x,y)\in F$, $(y,z)\in G$ and $(x,y')\in F$, $(y',z')\in G$, namely $y,y'$, respectively. However, since $f$ is a function, $(x,y)\in F$ and $(x,y')\in F$ imply $y=y'$. Now, from the two conditions $(y,z)\in G$ and $(y',z')\in G$, together with $y=y'$ and the fact that $g$ is a function, we know that $z=z'$.
:::

Thus, the composition of functions is nothing other than the composition of binary relations, and the resulting binary relation is always a function.



## Inverse Functions

Defining inverse functions is somewhat more involved. Although for a function $f$, we may consider its inverse relation $f^{-1}$ as a binary relation, this relation need not be a function. To state when $f^{-1}$ is a function, we must first define injective, surjective, and bijective functions.

::: Definition 2
Consider a function $f:A\rightarrow B$. The function $f$ is *injective* if any two distinct elements of $A$ have distinct images under $f$. The function $f$ is *surjective* if $f(A)=B$. If $f$ is both an injective function and a surjective function, then this function is said to be *bijective*.
:::

These terms became standard only relatively recently in the broader history of mathematics. Prior to that, terms such as

- *one-to-one* instead of the term *injection*,
- *onto* instead of the term *surjection*,
- *one-to-one and onto* instead of the term *bijection*

were used, and Korean terms commonly used in high school, such as *일대일함수* (one-to-one function) and *일대일대응* (one-to-one correspondence), are remnants of these terms.

::: Example 3
Let $A\subseteq B$. Defining $f:A\rightarrow B$ by $x\mapsto x$ yields an injective function. This function is called the *canonical injection*.

For any function $f:A\rightarrow B$, subset $X\subseteq A$, and canonical injection $i:X\hookrightarrow A$, it is easy to verify that

$$f\vert_X=f\circ i$$

holds. Occasionally the expression on the right-hand side is written as $i^\ast f$.
:::

::: Example 4
By definition, it is clear that $\id_A=(\Delta_A,A,A)$ is bijective.
:::

Now we may define inverse functions as promised.

::: Proposition 5
For a function $f:A\rightarrow B$, $f^{-1}$ being a function is equivalent to $f$ being a bijective function.
:::
::: Proof
If $f$ is bijective, then since it is also a surjective function, its domain is $B$. In addition, since $f$ is also an injective function, $f^{-1}$ is a function.

Conversely, suppose that $f^{-1}$ is a function. Then by definition, $\pr_1 f^{-1}=B$. However, substituting $R_2=\id_A$ and $R_1=f^{-1}$ into the first equation of [§Operations on Binary Relations, ⁋Proposition 8](/en/math/set_theory/operation_of_binary_relations#prop8){: data-lid="c7ul5" }, we have $\pr_1f^{-1}=f(A)$, so $B=f(A)$, and thus $f$ is a surjective function. 

Also, suppose that $(x,f(x))\in F$ and $(y, f(y))\in F$ are well-defined. Then $(f(x), x)\in F^{-1}$ and $(f(y),y)\in F^{-1}$. In addition, if $f(x)=f(y)$, then since $f^{-1}$ is a function, we have $x=y$. Therefore, $f$ is an injective function.
:::

The $f^{-1}$ defined in this way is called the *inverse function* of $f$. We can easily verify that $f^{-1}\circ f=\id_A$ and $f\circ f^{-1}=\id_B$. 

The following remark provides important intuition when defining retractions and sections in the next article.

::: Remark 6
The two equations $f^{-1}\circ f=\id_A$ and $f\circ f^{-1}=\id_B$ remain partially true even if $f$ is not a bijective function, but only surjective or injective individually.  

- If $f$ is an injective function, then since $f$ is a bijection between $A$ and $f(A)\subseteq B$, there exists $\tilde{f}^{-1}:f(A)\rightarrow A$. Now $\tilde{f}^{-1}\circ f=\id_A$.   
- If $f$ is a surjective function, then for every $y\in B$, there always exists some $x$ such that $f(x)=y$. Now, if we let $\tilde{f}^{-1}$ be the function that maps $y$ determined in this way to $x$, then $f\circ \tilde{f}^{-1}=\id_B$.
:::

## Product of Functions

::: Definition 7
A *function of two variables* is a function whose domain is a set of ordered pairs.
:::

If $f$ is a function of two variables, then to express the value at $(x,y)$ of $f$, instead of $f((x,y))$ we write $f(x,y)$. The most significant feature of such a function is that there are two variables we can manipulate to observe the behavior of $f$.  
For example, to see how $f$ varies as the first coordinate changes, after fixing the second coordinate, we can treat $f$ as if it were a function taking only the first coordinate as input.

::: Definition 8
Let $f:A\rightarrow B$ be a function of two variables. For every $y$, define $A_y$ to be the set of elements satisfying $(x,y)\in A$ among all $x$. Then, provided $A_{y_0}\neq\emptyset$, for such $y_0$, the function from $A_{y_0}$ to $B$ given by $x\mapsto f(x,y_0)$ is called the *partial mapping* at $y_0$ of $f$, and is written as $f(-,y_0)$. Similarly, $f(x_0,-)$ is also defined.
:::

For any two functions $u:A\rightarrow C$ and $v:B\rightarrow D$, we can always combine them to form a function of two variables from $A\times B$ to $C\times D$. That is, it suffices to set

$$z\mapsto (u(\pr_1 z),v(\pr_2z))$$

This function is called the *product* of $u$ and $v$, and is written as $u\times v$. Of course, this function has nothing to do with the function obtained by multiplying the two values $u(x)$ and $v(x)$.

---
**References**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
