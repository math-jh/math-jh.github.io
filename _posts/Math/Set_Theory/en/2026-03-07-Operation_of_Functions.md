---

title: "Operations on Functions"
excerpt: "Inverse and composition of functions, surjective and injective functions"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/operation_of_functions

header:
    overlay_image: /assets/images/Math/Set_Theory/Operation_of_functions.png
    overlay_filter: 0.5

sidebar: 
    nav: "set_theory-en"

date: 2026-03-07
last_modified_at: 2026-03-07

weight: 6

---

A function is a binary relation satisfying certain conditions, and we have already defined the composition and inverse of binary relations. For the composition and inverse of functions to be well-defined, the result of composing them as binary relations or taking their inverse as binary relations must be a function.

## Composition of Functions

The composition of functions is straightforward.

<div class="proposition" markdown="1">

<ins id="prop1">**Proposition 1**</ins> Consider functions $$f:A\rightarrow B$$ and $$g:B\rightarrow C$$. Then $$g\circ f$$ is a function from $$A$$ to $$C$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

It is clear that the domain of $$g\circ f$$ is all of $$A$$. This is because the value of $$f$$ is defined for all elements of $$A$$, and the value of $$g$$ is defined for all elements of $$B$$, in particular for all elements of $$f(A)\subseteq B$$. Therefore, to prove the given proposition, it suffices to show:

> For any $$x\in A$$, if $$(x,z)$$ and $$(x,z')\in G\circ H$$, then necessarily $$z=z'$$.

Suppose $$(x,z),(x,z')\in G\circ F$$. By the definition of $$G\circ F$$, there exist $$y$$ and $$y'$$ such that $$(x,y)\in F$$, $$(y,z)\in G$$, and $$(x,y')\in F$$, $$(y',z')\in G$$, respectively. Since $$f$$ is a function, from $$(x,y)\in F$$ and $$(x,y')\in F$$, we have $$y=y'$$. Now from the conditions $$(y,z)\in G$$ and $$(y',z')\in G$$, together with $$y=y'$$ and the fact that $$g$$ is a function, we conclude $$z=z'$$.

</details>

Therefore, the composition of functions is nothing more than the composition of binary relations, and the resulting binary relation is always a function.



## Inverse Functions

Defining inverse functions is somewhat more involved. While we can consider the inverse relation $$f^{-1}$$ of a function $$f$$ as a binary relation, this relation may not be a function. To determine when $$f^{-1}$$ is a function, we must first define injective, surjective, and bijective functions.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> Consider a function $$f:A\rightarrow B$$. The function $$f$$ is *injective* if any two distinct elements of $$A$$ have distinct values under $$f$$. The function $$f$$ is *surjective* if $$f(A)=B$$. If $$f$$ is both injective and surjective, then this function is said to be *bijective*.

</div>

These terms have only recently become standard in the broader history of mathematics. Previously,

- Instead of *injection*, the term *one-to-one* was used,
- Instead of *surjection*, the term *onto* was used,
- Instead of *bijection*, the term *one-to-one and onto* was used,

and the Korean terms *일대일함수* (one-to-one function) and *일대일대응* (one-to-one correspondence) commonly used in high school are remnants of this earlier terminology.

<div class="example" markdown="1">

<ins id="ex3">**Example 3**</ins> Let $$A\subseteq B$$. If we define $$f:A\rightarrow B$$ by $$x\mapsto x$$, this function is injective. This function is called the *canonical injection*.

For any function $$f:A\rightarrow B$$, subset $$X\subseteq A$$, and canonical injection $$i:X\hookrightarrow A$$, it is easy to verify that

$$f|_X=f\circ i$$

holds. Sometimes the right-hand side is written as $$i_\ast f$$.

</div>

<div class="example" markdown="1">

<ins id="ex4">**Example 4**</ins> By definition, it is clear that $$\id_A=(\Delta_A,A,A)$$ is bijective.

</div>

Now we can define the inverse function as promised.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> For a function $$f:A\rightarrow B$$, $$f^{-1}$$ is a function if and only if $$f$$ is bijective.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

If $$f^{-1}$$ is bijective, then it is also a surjective function, so its domain becomes $$B$$. Also, since $$f$$ is injective, $$f^{-1}$$ becomes a function.

Conversely, suppose $$f^{-1}$$ is a function. Then by definition, $$\pr_1 f^{-1}=B$$. However, substituting $$R_2=\id_A$$ and $$R_1=f^{-1}$$ into the first equation of [§Operations on Binary Relations, ⁋Proposition 8](/en/math/set_theory/operation_of_binary_relations#prop8) gives $$\pr_1f^{-1}=f(A)$$, so $$B=f(A)$$, and therefore $$f$$ is a surjective function.

Also, suppose $$(x,f(x))\in F$$ and $$(y, f(y))\in F$$ are well-defined. Then $$(f(x), x)\in F^{-1}$$ and $$(f(y),y)\in F^{-1}$$. Furthermore, if $$f(x)=f(y)$$, then from the fact that $$f^{-1}$$ is a function, we have $$x=y$$. Therefore, $$f$$ is an injective function.

</details>

This defined $$f^{-1}$$ is called the *inverse function* of $$f$$. We can easily verify that $$f^{-1}\circ f=\id_A$$ and $$f\circ f^{-1}=\id_B$$.

The following remark provides important intuition for defining retractions and sections in the next article.

<div class="remark" markdown="1">

<ins id="rmk1">**Remark**</ins> The two equations $$f^{-1}\circ f=\id_A$$ and $$f\circ f^{-1}=\id_B$$ remain partially true even if $$f$$ is not bijective, but only surjective or injective.

- If $$f$$ is injective, then $$f$$ is a bijection between $$A$$ and $$f(A)\subseteq B$$, so $$\tilde{f}^{-1}:f(A)\rightarrow A$$ exists. Now $$\tilde{f}^{-1}\circ f=\id_A$$.
- If $$f$$ is surjective, then for every $$y\in B$$, there always exists some $$x$$ such that $$f(x)=y$$. Letting $$\tilde{f}^{-1}$$ be the function that maps each such $$y$$ to $$x$$, we have $$f\circ \tilde{f}^{-1}=\id_B$$.

</div>

## Product of Functions

<div class="definition" markdown="1">

<ins id="def6">**Definition 6**</ins> A *function of two variables* is a function whose domain is a set of ordered pairs.

</div>

If $$f$$ is a function of two variables, we write $$f(x,y)$$ instead of $$f((x,y))$$ to denote the value of $$f$$ at $$(x,y)$$. The most significant feature of such functions is that we have two variables to manipulate when observing the behavior of $$f$$. For example, to see how $$f$$ changes as the first coordinate varies, we can fix the second coordinate and treat $$f$$ as a function taking only the first coordinate as input.

<div class="definition" markdown="1">

<ins id="def7">**Definition 7**</ins> Let $$f:A\rightarrow B$$ be a function of two variables. For every $$y$$, define $$A_y$$ as the set of all $$x$$ such that $$(x,y)\in A$$. Then the function $$x\mapsto f(x,y_0)$$ from $$A_{y_0}$$ to $$B$$ is called the *partial mapping* of $$f$$ at $$y_0$$, and is written as $$f(-,y_0)$$. Similarly, $$f(x_0,-)$$ is also defined.

</div>

For any two functions $$u:A\rightarrow C$$ and $$v:B\rightarrow D$$, we can always combine them to create a function of two variables from $$A\times B$$ to $$C\times D$$. That is, we define

$$z\mapsto (u(\pr_1 z),v(\pr_2z))$$

This function is called the *product* of $$u$$ and $$v$$, and is written as $$u\times v$$. Of course, this function has nothing to do with a function created by multiplying the two values $$u(x)$$ and $$v(x)$$.

---
**References**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
