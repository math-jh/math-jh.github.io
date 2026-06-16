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
last_polished_at: 2026-06-02T19:30:02+00:00
---
A function is a binary relation satisfying certain conditions, and we have already defined the composition and inverse of binary relations. For the composition and inverse of functions to be well-defined, the result of composing them as binary relations or taking their inverse as binary relations must itself be a function.

## Composition of Functions

The composition of functions is unremarkable.

<div class="proposition" markdown="1">

<ins id="prop1">**Proposition 1**</ins> Consider functions $$f:A\rightarrow B$$ and $$g:B\rightarrow C$$. Then $$g\circ f$$ is a function from $$A$$ to $$C$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

That the domain of $$g\circ f$$ is all of $$A$$ is immediate: the value of $$f$$ is defined for every element of $$A$$, and the value of $$g$$ is defined for every element of $$B$$, hence in particular for every element of $$f(A)\subseteq B$$. Therefore, to prove the proposition it suffices to show:

> For any $$x\in A$$, if $$(x,z)$$ and $$(x,z')\in G\circ H$$, then necessarily $$z=z'$$.

Suppose $$(x,z),(x,z')\in G\circ F$$. By the definition of $$G\circ F$$, there exist $$y$$ and $$y'$$ such that $$(x,y)\in F$$, $$(y,z)\in G$$ and $$(x,y')\in F$$, $$(y',z')\in G$$, respectively. Since $$f$$ is a function, $$(x,y)\in F$$ and $$(x,y')\in F$$ imply $$y=y'$$. From $$(y,z)\in G$$, $$(y',z')\in G$$, and $$y=y'$$, together with the fact that $$g$$ is a function, we conclude $$z=z'$$.

</details>

Thus, the composition of functions is nothing other than the composition of binary relations, and the resulting binary relation is always a function.



## Inverse Functions

Defining inverse functions is somewhat more involved. Although we may consider the inverse relation $$f^{-1}$$ of a function $$f$$ as a binary relation, this relation need not be a function. To characterize when $$f^{-1}$$ is a function, we must first define injective, surjective, and bijective functions.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> Consider a function $$f:A\rightarrow B$$. The function $$f$$ is *injective* if any two distinct elements of $$A$$ have distinct images under $$f$$. The function $$f$$ is *surjective* if $$f(A)=B$$. If $$f$$ is both injective and surjective, then this function is said to be *bijective*.

</div>

These terms became standard only relatively recently in the broader history of mathematics. Previously,

- instead of *injection*, the term *one-to-one* was used,
- instead of *surjection*, the term *onto* was used,
- instead of *bijection*, the term *one-to-one and onto* was used,

and the Korean terms *일대일함수* (one-to-one function) and *일대일대응* (one-to-one correspondence) commonly used in high school are remnants of this earlier terminology.

<div class="example" markdown="1">

<ins id="ex3">**Example 3**</ins> Let $$A\subseteq B$$. Defining $$f:A\rightarrow B$$ by $$x\mapsto x$$ yields an injective function. This function is called the *canonical injection*.

For any function $$f:A\rightarrow B$$, subset $$X\subseteq A$$, and canonical injection $$i:X\hookrightarrow A$$, it is easy to verify that

$$f\vert_X=f\circ i$$

holds. Occasionally the right-hand side is written as $$i_\ast f$$.

</div>

<div class="example" markdown="1">

<ins id="ex4">**Example 4**</ins> By definition, it is clear that $$\id_A=(\Delta_A,A,A)$$ is bijective.

</div>

Now we may define inverse functions as promised.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> For a function $$f:A\rightarrow B$$, $$f^{-1}$$ is a function if and only if $$f$$ is bijective.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

If $$f^{-1}$$ is bijective, then it is also surjective, so its domain is $$B$$. Moreover, since $$f$$ is injective, $$f^{-1}$$ is a function.

Conversely, suppose $$f^{-1}$$ is a function. Then by definition, $$\pr_1 f^{-1}=B$$. Substituting $$R_2=\id_A$$ and $$R_1=f^{-1}$$ into the first equation of [§Operations on Binary Relations, ⁋Proposition 8](/en/math/set_theory/operation_of_binary_relations#prop8) yields $$\pr_1f^{-1}=f(A)$$, so $$B=f(A)$$, and therefore $$f$$ is surjective.

Also, suppose $$(x,f(x))\in F$$ and $$(y, f(y))\in F$$ are well-defined. Then $$(f(x), x)\in F^{-1}$$ and $$(f(y),y)\in F^{-1}$$. If in addition $$f(x)=f(y)$$, then since $$f^{-1}$$ is a function, we have $$x=y$$. Therefore, $$f$$ is injective.

</details>

This $$f^{-1}$$ is called the *inverse function* of $$f$$. We can easily verify that $$f^{-1}\circ f=\id_A$$ and $$f\circ f^{-1}=\id_B$$.

The following remark provides important intuition for defining retractions and sections in the next article. On the other hand,

<div class="remark" markdown="1">

<ins id="rmk6">**Remark 6**</ins> The two equations $$f^{-1}\circ f=\id_A$$ and $$f\circ f^{-1}=\id_B$$ remain partially valid even if $$f$$ is not bijective but merely surjective or injective.

- If $$f$$ is injective, then $$f$$ is a bijection between $$A$$ and $$f(A)\subseteq B$$, so $$\tilde{f}^{-1}:f(A)\rightarrow A$$ exists. Then $$\tilde{f}^{-1}\circ f=\id_A$$.
- If $$f$$ is surjective, then for every $$y\in B$$ there exists some $$x$$ such that $$f(x)=y$$. Letting $$\tilde{f}^{-1}$$ be the function that maps each such $$y$$ to a corresponding $$x$$, we have $$f\circ \tilde{f}^{-1}=\id_B$$.

</div>

## Product of Functions

<div class="definition" markdown="1">

<ins id="def7">**Definition 7**</ins> A *function of two variables* is a function whose domain is a set of ordered pairs.

</div>

If $$f$$ is a function of two variables, we write $$f(x,y)$$ instead of $$f((x,y))$$ to denote the value of $$f$$ at $$(x,y)$$. The most significant feature of such functions is that we have two variables to manipulate when observing the behavior of $$f$$. For example, to see how $$f$$ varies as the first coordinate changes, we may fix the second coordinate and treat $$f$$ as a function taking only the first coordinate as input.

<div class="definition" markdown="1">

<ins id="def8">**Definition 8**</ins> Let $$f:A\rightarrow B$$ be a function of two variables. For every $$y$$, define $$A_y$$ as the set of all $$x$$ such that $$(x,y)\in A$$. Then the function $$x\mapsto f(x,y_0)$$ from $$A_{y_0}$$ to $$B$$ is called the *partial mapping* of $$f$$ at $$y_0$$, and is written as $$f(-,y_0)$$. Similarly, $$f(x_0,-)$$ is also defined.

</div>

For any two functions $$u:A\rightarrow C$$ and $$v:B\rightarrow D$$, we can always combine them to create a function of two variables from $$A\times B$$ to $$C\times D$$. That is, we set

$$z\mapsto (u(\pr_1 z),v(\pr_2z))$$

This function is called the *product* of $$u$$ and $$v$$, and is written as $$u\times v$$. Of course, this function has nothing to do with a function obtained by multiplying the two values $$u(x)$$ and $$v(x)$$.

---
**References**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
