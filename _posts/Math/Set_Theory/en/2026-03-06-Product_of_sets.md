---

title: "Product of Sets"
excerpt: "Product of Sets"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/product_of_sets
header:
    overlay_image: /assets/images/Math/Set_Theory/Product_of_sets.png
    overlay_filter: 0.5
sidebar: 
    nav: "set_theory-en"

date: 2026-03-06
last_modified_at: 2026-03-06
weight: 10

---

## Product of Sets

The most natural generalization of an ordered pair is a function. For instance, an $$n$$-tuple may be regarded as a function with domain $$I=\{1,2,\cdots, n\}$$ that returns the $$i$$-th component when given $$i$$ as input.

Consider sets $$A_1$$ and $$A_2$$. The product $$A_1\times A_2$$ is the collection of ordered pairs $$(x_1,x_2)$$. Viewing ordered pairs as functions as above, $$A_1\times A_2$$ is the *collection of functions* with domain $$\{1,2\}$$, where each function $$f$$ satisfies $$f(1)=x_1\in A_1$$ and $$f(2)=x_2\in A_2$$.

It is then natural to define the product of a general family as follows.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Let $$(A_i)\_{i\in I}$$ be a family of sets. The *product* of this family is the collection $$P$$ of all functions from $$I$$ to $$\bigcup A_i$$ satisfying $$x_i=f(i)\in A_i$$.

As with the notation for families of sets, elements of $$P$$ are written as $$(x_i)\_{i\in I}$$; each $$x_i$$ is called the *$$i$$-th component*. The function sending $$F\in P$$ to $$F(i)$$ is called the *$$i$$-th projection* and is denoted by $$\pr\_i$$.

</div>

Thus to consider the product of sets is to consider a *set of functions*.

Let sets $$A$$ and $$B$$ be given. A function from $$A$$ to $$B$$ is an element of $$\mathcal{P}(A\times B)$$, so the collection of all such functions is a subset of $$\mathcal{P}(A\times B)$$. We denote this set by $$B^A$$. Let $$\Fun(A,B)$$ denote the set of all functions from $$A$$ to $$B$$. For any $$F\in B^A$$, the triple $$f=(F,A,B)$$ is a function from $$A$$ to $$B$$, and the assignment $$F\mapsto f$$ is a function from $$B^A$$ to $$\Fun(A,B)$$.

Conversely, for any function $$f=(F,A,B)$$, the correspondence sending $$f$$ to the element $$F\in B^A$$ is not only a function but also the inverse of the correspondence defined above. Hence there exists a natural bijection between $$B^A$$ and $$\Fun(A,B)$$, and these two sets may be identified.

Let functions $$u:A'\rightarrow A$$ and $$v:B\rightarrow B'$$ be given, and consider the following diagram.

![induced_mapping](/assets/images/Math/Set_Theory/Product_of_sets-1.png){:style="width:6em"  class="invert" .align-center}

In this diagram, whenever a function $$f:A\rightarrow B$$ is given, we can associate to it the function $$\tilde{f}=v\circ f\circ u$$ from $$A'$$ to $$B'$$. The assignment $$f\mapsto \tilde{f}$$ is a function from $$\Fun(A, B)$$ to $$\Fun(A', B')$$.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> In the diagram above, if $$u$$ is surjective and $$v$$ is injective, then $$f\mapsto \tilde{f}$$ is injective. If $$u$$ is injective and $$v$$ is surjective, then $$f\mapsto \tilde{f}$$ is surjective.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First suppose $$u$$ and $$v$$ are surjective and injective respectively. To show that $$f\mapsto\tilde{f}$$ is injective, we must prove that $$\tilde{f}=\tilde{g}$$ implies $$f=g$$. Let $$s$$ and $$r$$ be a section and retraction corresponding to $$u$$ and $$v$$ respectively. If $$\tilde{f}=\tilde{g}$$, then

$$\begin{aligned}
  f&=\id_B\circ f\circ\id_A=(r\circ v)\circ f\circ(u\circ s)=r\circ(v\circ f\circ u)\circ s\\
  &=r\circ\tilde{f}\circ s=r\circ\tilde{g}\circ s\\
  &=r\circ(v\circ g\circ u)\circ s=(r\circ v)\circ g\circ (u\circ s)=\id_B\circ g\circ\id_A=g
\end{aligned}$$

so $$f=g$$. Hence the given function is injective.

Similarly, suppose $$u$$ and $$v$$ are injective and surjective respectively. We must show that for any $$f'\in\Fun(A',B')$$, there exists $$f\in\Fun(A,B)$$ with $$\tilde{f}=f'$$. Let $$r'$$ and $$s'$$ be a retraction and section for $$u$$ and $$v$$ respectively. Then

$$f'=\id_{B'}\circ f'\circ\id_{A'}=(v\circ s')\circ f'\circ(r'\circ u)=v\circ(s'\circ f'\circ r')\circ u$$

so $$f=s'\circ f'\circ r'$$ is an element of $$\Fun(A,B)$$ satisfying $$f'=\tilde{f}$$. Hence the given function is surjective.

</details>

In particular, if both $$u$$ and $$v$$ are bijections, then $$f\mapsto \tilde{f}$$ is also a bijection.

Earlier we saw that the sum of sets satisfies a universal property. Similarly, the product satisfies an analogous universal property.

<div class="proposition" markdown="1">

<ins id="thm3">**Theorem 3**</ins> Let $$P$$ be the product of a family of sets $$(A_i)$$, with projection functions $$\pr\_i:P\rightarrow A_i$$. Given another set $$B$$ and functions $$f_i:B\rightarrow A_i$$, there exists a unique function $$f:B\rightarrow P$$ satisfying $$f_i=\pr\_i\circ f$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Suppose functions $$f$$ and $$f'$$ are given, both satisfying the condition $$f\_i=\pr\_i\circ f$$. We must show that $$f(y)=f'(y)$$ for every $$y\in B$$. Since $$f(y)$$ and $$f'(y)$$ are elements of $$A$$ and hence functions (ordered pairs), they are determined by the values they assign to each $$i$$ (the $$i$$-th coordinates). Thus it suffices to show that $$\pr\_i(f(y))=\pr\_i(f'(y))$$ for any given $$y\in B$$ and $$i\in I$$. But

$$\pr_i(f(y))=f_i(y)=\pr_i(f'(y))$$

so any such function $$f$$ must be unique.

For existence, taking a cue from the uniqueness proof above, we define the value $$f(y)$$ to be the function (or ordered pair whose $$i$$-th coordinate is $$f_i(y)$$) satisfying

> $$(f(y))(i)=f_i(y)$$

and then verify that the correspondence $$y\mapsto f(y)$$ is indeed a function.

</details>

Since at least one $$(P, \pr\_i)$$ satisfying the conditions of [Theorem 3](#thm3) exists ([Definition 1](#def1)), we may take this as the definition of the product set. That is, the product of $$(A\_i)\_{i\in I}$$ can be characterized as a set $$\prod\_{i\in I} A\_i$$ together with functions $$\pr\_i:\prod\_{i\in I}A\_i\rightarrow A_i$$ satisfying the following universal property.

![universal_property_of_product](/assets/images/Math/Set_Theory/Product_of_sets-2.png){:style="width:13em" class="invert" .align-center}

By the same reasoning as in [§Sum of Sets, ⁋Corollary 9](/en/math/set_theory/sum_of_sets#cor9), one can verify that the object and projections $$\pr\_i$$ satisfying this universal property are unique up to bijection.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> Let $$A$$, $$B$$, $$C$$ be sets and let $$f:B\times C\rightarrow A$$. If $$\tilde{f}$$ is the function from $$C$$ to $$\Fun(B,A)$$ defined by $$y\mapsto f(-,y)$$, then $$f\mapsto\tilde{f}$$ is a bijection. That is, there exists a bijection between $$\Fun(B\times C,A)$$ and $$\Fun(C, \Fun(B, A))$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Since $$\tilde{f}$$ is a function from $$C$$ to $$\Fun(B,A)$$, we have $$\tilde{f}\in\Fun(C,\Fun(B,A))$$. Thus the given correspondence is a function from $$\Fun(B\times C, A)$$ to $$\Fun(C, \Fun(B,A))$$. To show that this function is bijective, we construct its inverse.

Let $$g\in\Fun(C, \Fun(B,A))$$ be given. For any $$y\in C$$, $$g(y)$$ is an element of $$\Fun(B, A)$$. Define $$\bar{g}:B\times C\rightarrow A$$ to be the function sending $$(x, y)$$ to $$g(y)(x)$$. Then for any $$g\in \Fun(C,\Fun(B,A))$$, we have a function

$$\begin{aligned}
-:\Fun(C, \Fun(B,A))&\rightarrow\Fun(B\times C,A)\\
g\phantom{function}&\mapsto\phantom{function}\bar{g}
\end{aligned}$$

We must show that this function $$-$$ is the inverse of the original function

$$\begin{aligned}
\sim\;:\Fun(B\times C,A)&\rightarrow\Fun(C, \Fun(B,A))\\
f\phantom{function}&\mapsto\phantom{function}\tilde{f}
\end{aligned}$$

For any $$f:B\times C\rightarrow A$$, we have $$\tilde{f}\in \Fun(C, \Fun(B, A))$$. Applying $$-$$ to this function to return to $$\Fun(B\times C,A)$$, the result $$\bar{\tilde{f}}$$ is the function sending $$(x, y)$$ to $$\tilde{f}(y)(x)$$. Since $$\tilde{f}(y)$$ is the function $$f(-, y)$$, we have $$\bar{\tilde{f}}=f$$.

On the other hand, for any $$g\in\Fun(C, \Fun(B, A))$$, applying first $$\bar{g}$$ and then $$\tilde{\bar{g}}$$, we see that $$\tilde{\bar{g}}$$ is the function defined by $$y\mapsto \bar{g}(-,y)$$. By the definition of $$\bar{g}$$, this is the function sending $$y$$ to $$g(y)(-)$$. That is, $$\tilde{\bar{g}}=g$$. From $$\bar{\tilde{f}}=f$$ and $$\tilde{\bar{g}}=g$$, we conclude that these are inverse functions of each other. We have thus shown that

$$\begin{aligned}
  f\overset{\sim}{\longrightarrow}&\tilde{f}\overset{-}{\longrightarrow}\bar{\tilde{f}}=f,\\
  g\overset{-}{\longrightarrow}&\bar{g}\overset{\sim}{\longrightarrow}\tilde{\bar{g}}=g
\end{aligned}$$

Therefore $$\sim\;:f\mapsto\tilde{f}$$ is a bijection.
</details>

Immediately after defining the union, we observed that replacing the index set via a surjection has no effect. For products of sets, replacing the index set via a bijection likewise has no effect.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> Let $$(A_i)\_{i\in I}$$ be a family of sets and let $$u:K\rightarrow I$$ be a bijection. For any $$f:I\rightarrow \prod_{i\in I}A\_i$$, the function $$f\mapsto f\circ u$$ sending $$f$$ to $$f\circ u: K\rightarrow \prod\_{i\in I} A\_i$$ is a bijection.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>
Consider the diagram

![induced_bijection](/assets/images/Math/Set_Theory/Product_of_sets-3.png){:style="width:13em"  class="invert" .align-center}

Here $$v$$ is the bijection sending $$(x_i)\_{i\in I}$$ to $$(x\_{u(k)})\_{k\in K}$$. By [Proposition 2](#prop2) above, $$F\mapsto F\circ U$$ is a bijection.
</details>



---
**References**

**[HJJ]** K. Hrbacek, T.J. Jeck, and T. Jech. *Introduction to Set Theory*. Lecture Notes in Pure and Applied Mathematics. M. Dekker, 1978.  
**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---

