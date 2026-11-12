---
title: "Product of Sets"
description: "This post defines the product of sets from the perspective of functions, and explores component functions as a generalization of ordered pairs and the structure of products. It also examines the conditions for induced maps to be injective or surjective."
excerpt: "Product between sets"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/product_of_sets
sidebar: 
    nav: "set_theory-en"

date: 2021-08-15
weight: 10
translated_at: 2026-06-02T11:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-11-01T07:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
## Product of Sets

The most natural generalization of an ordered pair is a function. For example, an $n$-tuple can be thought of as a function with domain $I=\{1,2,\cdots, n\}$ that, when given $i$, returns the $i$-th component.

For example, for sets $A_1$ and $A_2$, $A_1\times A_2$ is the collection of ordered pairs $(x_1,x_2)$. Viewing ordered pairs as functions as above, $A_1\times A_2$ is a *collection of functions* with domain $\{1,2\}$, where these functions $f$ satisfy $f(1)=x_1\in A_1$ and $f(2)=x_2\in A_2$. 

Then it is natural to define the product of a general family as follows.

::: Definition 1
Let $(A_i)_{i\in I}$ be a family of sets. Then, among all functions from $I$ to $\bigcup A_i$, the collection of those satisfying $x_i=f(i)\in A_i$, denoted by $P$, is called the *product* of this family.

As with the notation for families of sets, the elements of $P$ are written as $(x_i)_{i\in I}$, each $x_i$ is called the *$i$-th component*, and the function sending $F\in P$ to $F(i)$ is called the *$i$-th component function* and denoted by $\pr_i$.
:::

Thus, considering the product of sets is the same as considering a *set of functions*. 

Suppose sets $A,B$ are given. Then the graph of a function from $A$ to $B$ is an element of $\mathcal{P}(A\times B)$, so their collection is a subset of $\mathcal{P}(A\times B)$. We denote this by $B^A$. Let the set of functions from $A$ to $B$ be denoted by $\Fun(A,B)$. Then for any $F\in B^A$, $f=(F,A,B)$ is a function from $A$ to $B$, and this correspondence $F\mapsto f$ is a function from $B^A$ to $\Fun(A,B)$. 

On the other hand, for any function $f=(F,A,B)$, if we associate to it the element of $B^A$, namely $F$, one can easily verify that this correspondence is not only a function, but also the inverse of the correspondence defined above. That is, there exists a natural bijection between $B^A$ and $\Fun(A,B)$, so we can consider these two sets to be the same.

Suppose functions $u:A'\rightarrow A$ and $v:B\rightarrow B'$ are given, and consider the following diagram.

{% diagram Math/Set_Theory/Product_of_Sets-1.svg width="6.00em" alt="induced_mapping" %}

In this diagram, whenever a function $f:A\rightarrow B$ is given, we can consider the corresponding function from $A'$ to $B'$, $\tilde{f}=v\circ f\circ u$. This correspondence $f\mapsto \tilde{f}$ is a function from $\Fun(A, B)$ to $\Fun(A', B')$.

::: Proposition 2
In the diagram above, if $u$ is surjective and $v$ is injective, then $f\mapsto \tilde{f}$ is injective. If $u$ is injective and $v$ is surjective, then $f\mapsto \tilde{f}$ is surjective.
:::
::: Proof
First, suppose $u$ and $v$ are surjective and injective, respectively. To show that the given function $f\mapsto\tilde{f}$ is injective, we must show that $\tilde{f}=\tilde{g}$ implies $f=g$. Let $s$ and $r$ be the corresponding section and retraction, respectively. If $\tilde{f}=\tilde{g}$, then

$$\begin{aligned}
  f&=\id_B\circ f\circ\id_A=(r\circ v)\circ f\circ(u\circ s)=r\circ(v\circ f\circ u)\circ s\\
  &=r\circ\tilde{f}\circ s=r\circ\tilde{g}\circ s\\
  &=r\circ(v\circ g\circ u)\circ s=(r\circ v)\circ g\circ (u\circ s)=\id_B\circ g\circ\id_A=g
\end{aligned}$$

so $f=g$. Hence the given function is injective. 

Similarly, suppose $u$ and $v$ are injective and surjective, respectively. We must show that for any $f'\in\Fun(A',B')$, $\tilde{f}=f'$ holds for some $f\in\Fun(A,B)$. Let $r'$ and $s'$ be a retraction and section of $u$ and $v$, respectively. Then

$$f'=\id_{B'}\circ f'\circ\id_{A'}=(v\circ s')\circ f'\circ(r'\circ u)=v\circ(s'\circ f'\circ r')\circ u$$

so $f=s'\circ f'\circ r'$ is an element of $\Fun(A,B)$ and satisfies $f'=\tilde{f}$. Therefore, the given function is surjective.
:::

In particular, if both $u$ and $v$ are bijections, then $f\mapsto \tilde{f}$ is also a bijection. 

Earlier, the sum of sets satisfied a universal property; likewise, the product satisfies a similar universal property.

::: Theorem 3
Suppose we are given a family of sets $(A_i)$, its product $P$, and component functions $\pr_i:P\rightarrow A_i$. Given another set $B$ and functions $f_i:B\rightarrow A_i$, there exists, satisfying the equation $f_i=\pr_i\circ f$, a unique function $f:B\rightarrow P$.
:::
::: Proof
First, suppose we are given, satisfying the given condition $f_i=\pr_i\circ f$, functions $f,f'$. We must show that for any $y\in B$, $f(y)=f'(y)$. However, since $f(y)$ and $f'(y)$ are in any case elements of $P$, they are functions (ordered pairs), and are therefore determined by the values to which $i$ corresponds (the $i$-th coordinates). Therefore, given any $y\in B$ and $i\in I$, it suffices to show that $\pr_i(f(y))=\pr_i(f'(y))$. But since

$$\pr_i(f(y))=f_i(y)=\pr_i(f'(y))$$

such a function $f$ must be unique.

For existence, similarly taking a hint from the uniqueness proof above, after defining the value of $f(y)$ as

> the function satisfying $(f(y))(i)=f_i(y)$ (or the ordered pair whose $i$-th coordinate is $f_i(y)$)

it suffices to show that this correspondence $y\mapsto f(y)$ is indeed a function.
:::

Now, since there exists at least one $(P, \pr_i)$ satisfying the conditions of [Theorem 3](#thm3){: data-lid="b2jpu" } ([Definition 1](#def1){: data-lid="nv6h6" }), we may take this as the definition of the product set. That is, the product of $(A_i)_{i\in I}$ can be said to be a set $\prod_{i\in I} A_i$ and functions $\pr_i:\prod_{i\in I}A_i\rightarrow A_i$ satisfying the following universal property.

{% diagram Math/Set_Theory/Product_of_Sets-2.svg width="13.37em" alt="universal_property_of_product" %}

By applying exactly the same logic as in [§Sum of Sets, ⁋Corollary 9](/en/math/set_theory/sum_of_sets#cor9){: data-lid="uzl6x" }, one can verify that the object and the $\pr_i$ satisfying this universal property are also unique up to bijection.

::: Proposition 4
Let $A$, $B$, $C$ be sets and let $f:B\times C\rightarrow A$. If $\tilde{f}$ is the function from $C$ to $\Fun(B,A)$ given by $y\mapsto f(-,y)$, then $f\mapsto\tilde{f}$ is a bijection. That is, there exists a bijection between $\Fun(B\times C,A)$ and $\Fun(C, \Fun(B, A))$.
:::

::: Proof
First, since $\tilde{f}$ is a function from $C$ to $\Fun(B,A)$, we have $\tilde{f}\in\Fun(C,\Fun(B,A))$. Thus the given function is a function from $\Fun(B\times C, A)$ to $\Fun(C, \Fun(B,A))$. To show that this function is bijective, we will construct its inverse.

Suppose $g\in\Fun(C, \Fun(B,A))$ is given. Then for any $y\in C$, $g(y)$ is an element of $\Fun(B, A)$. Now define $\bar{g}:B\times C\rightarrow A$ to be the function sending $(x, y)$ to $g(y)(x)$. Then for any $g\in \Fun(C,\Fun(B,A))$, we can consider the function sending $g$ to $\bar{g}$

$$\begin{aligned}
-:\Fun(C, \Fun(B,A))&\rightarrow\Fun(B\times C,A)\\
g\phantom{function}&\mapsto\phantom{function}\bar{g}
\end{aligned}$$

As mentioned earlier, we must show that this function $-$ is the inverse of the original function

$$\begin{aligned}
{\sim}:\Fun(B\times C,A)&\rightarrow\Fun(C, \Fun(B,A))\\
f\phantom{function}&\mapsto\phantom{function}\tilde{f}
\end{aligned}$$

.

For any $f:B\times C\rightarrow A$, we have $\tilde{f}\in \Fun(C, \Fun(B, A))$. Now let us send this function back to $\Fun(B\times C,A)$ via $-$. Then this result $\bar{\tilde{f}}$ is the function sending $(x, y)$ to $\tilde{f}(y)(x)$. Since $\tilde{f}(y)$ is the function $f(-, y)$, we have $\bar{\tilde{f}}=f$.  
On the other hand, for any $g\in\Fun(C, \Fun(B, A))$, if we first apply $\bar{g}$ and then examine $\tilde{\bar{g}}$, $\tilde{\bar{g}}$ is the function determined by $y\mapsto \bar{g}(-,y)$. By the definition of $\bar{g}$, this is again the function sending $y$ to $g(y)(-)$. That is, $\tilde{\bar{g}}$ is again $g$. From this, since $\bar{\tilde{f}}=f$ and $\tilde{\bar{g}}=g$, they are inverses of each other. That is, we have shown the following:

$$\begin{aligned}
  f\overset{\sim}{\rightarrow}&\tilde{f}\overset{-}{\rightarrow}\bar{\tilde{f}}=f,\\
  g\overset{-}{\rightarrow}&\bar{g}\overset{\sim}{\rightarrow}\tilde{\bar{g}}=g
\end{aligned}$$

Therefore ${\sim}:f\mapsto\tilde{f}$ is a bijection.
:::

Immediately after defining the union, we saw in [§Union and Intersection, ⁋Proposition 4](/en/math/set_theory/union_and_intersection#prop4){: data-lid="kwrbs" } that replacing the index set via a surjection has no effect; for products of sets, replacing it via a bijection likewise has no effect.

::: Proposition 5
Let $(A_i)_{i\in I}$ be a family of sets and let $u:K\rightarrow I$ be a bijection. For any $F\in\prod_{i\in I}A_i$, the function sending it to $F\circ u\in\prod_{k\in K}A_{u(k)}$, $F\mapsto F\circ u$, is a bijection.
:::

::: Proof
Consider the following diagram.

{% diagram frozen/81b7e8af/Math/Set_Theory/Product_of_Sets-3.svg width="13.03em" alt="induced_bijection" %}

This is the diagram used earlier to define $\tilde{f}=v\circ f\circ u$, with $A'=K$, $A=I$, $B=B'=\bigcup_{i\in I}A_i$, and $v$ taken to be the identity function. Then since $u$ and $v$ are both bijections, by [Proposition 2](#prop2){: data-lid="8lx5z" } above, $F\mapsto F\circ u$ is a bijection from $\Fun(I,\bigcup_{i\in I}A_i)$ to $\Fun(K,\bigcup_{k\in K}A_{u(k)})$. On the other hand, since $u$ is a bijection, $F(i)\in A_i$ holding for all $i\in I$ is equivalent to $(F\circ u)(k)\in A_{u(k)}$ holding for all $k\in K$, and therefore this bijection restricts to a bijection between $\prod_{i\in I}A_i$ and $\prod_{k\in K}A_{u(k)}$.
:::



---
**References**

**[HJJ]** K. Hrbacek, T.J. Jeck, and T. Jech. *Introduction to Set Theory*. Lecture Notes in Pure and Applied Mathematics. M. Dekker, 1978.  
**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
