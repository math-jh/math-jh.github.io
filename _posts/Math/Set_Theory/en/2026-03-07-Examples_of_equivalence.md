---

title: "Examples of Equivalence Relations"
excerpt: "Examples of equivalence relations, saturation of equivalence relations, isomorphism theorems"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/examples_of_equivalence
header:
    overlay_image: /assets/images/Math/Set_Theory/Examples_of_equivalence.png
    overlay_filter: 0.5
sidebar: 
    nav: "set_theory-en"

date: 2026-03-07
last_modified_at: 2026-03-07
weight: 13

---

In this article, we explore examples of equivalence relations that arise in various contexts.

## Equivalence Relations Defined by Functions

In the previous article, we saw that from an equivalence relation $$(R,A,A)$$, a canonical function $$p:A\rightarrow A/R$$ is well-defined. The converse also holds: given any function, we can use it to construct an equivalence relation.

<div class="proposition" markdown="1">

<ins id="prop1">**Proposition 1**</ins> Let a set $$A$$ and a function $$f$$ with domain $$A$$ be given. Then the relation on $$x$$ and $$y$$ given by "$$x,y\in A$$ and $$f(x)=f(y)$$" is an equivalence relation on $$A$$.
</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

It is obvious that the given relation is reflexive on $$A$$. Moreover, if $$f(x)=f(y)$$, then $$f(y)=f(x)$$, and if $$f(x)=f(y)$$ and $$f(y)=f(z)$$, then $$f(x)=f(z)$$, so this relation is also symmetric and transitive.

</details>

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> The equivalence relation defined in the previous proposition is called the *equivalence relation defined by $$f$$*.

</div>

For an equivalence relation $$(R,A,A)$$ and the induced $$p:A\rightarrow A/R$$, we can verify that the equivalence relation $$R$$ is exactly the same as the equivalence relation obtained by applying [Definition 2](#def2) to $$p$$.

## Unary Relations and Compatible Equivalence Relations

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> Let $$(R,A,A)$$ be an equivalence relation. A unary relation $$P$$ is *compatible* with $$R$$ if $$P(x)\wedge (x\sim_{\tiny R}y)\implies P(y)$$.

</div>

For example, the unary relation

> $$x$$ is even

is compatible with the equivalence relation

> $$x-y$$ is a multiple of 4

Rewriting the definition above from the perspective of equivalence classes, we have the following.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> Let $$R$$ be an equivalence relation on a set $$A$$, and let $$P$$ be a unary relation compatible with $$R$$. Then the statements "$$t\in A/R$$ and there exists $$x\in t$$ such that $$P(x)$$" and "$$t\in A/R$$ and for all $$x\in t$$, $$P(x)$$" are equivalent.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

To put it more explicitly:

> When $$P$$ is compatible with $$R$$, if even a single element of an equivalence class satisfies $$P$$, then $$P$$ holds for all elements in the same class.

And this is exactly the definition of a compatible unary relation.

The reverse direction is obvious. Suppose for some $$t\in A/R$$ there exists $$a\in t$$ such that $$P(a)$$. Then for all $$x\in t$$, since $$a\sim_{\tiny R}x$$, we have $$P(x)$$.

</details>

## Saturation of Equivalence Relations

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> Let $$R$$ be an equivalence relation on $$A$$ and $$X$$ be a subset of $$A$$. $$X$$ is *saturated* with respect to $$R$$ if the unary relation $$x\in A$$ is compatible with $$R$$.

</div>

![saturated_set](/assets/images/Math/Set_Theory/Examples_of_equivalence-1.png){:style="width:600px" class="invert" .align-center}

<cap>A saturated subset (left) and a non-saturated subset (right) in a given quotient set (top)</cap>

According to the definition above, for a set $$X$$ to be $$R$$-saturated, it must satisfy the condition that if $$x\in X$$, then $$R(x)\subseteq X$$. Therefore, an $$R$$-saturated subset $$X$$ is a set that can be expressed as $$\bigcup_{x\in B}R(x)$$ for some subset $$B\subseteq A$$. From this, we can easily verify the following two results:

1. If $$(A_i)_{i\in I}$$ is a family of $$R$$-saturated subsets, then $$\bigcup_{i\in I} A_i$$ and $$\bigcap_{i\in I} A_i$$ are also $$R$$-saturated.
2. If $$X\subseteq A$$ is $$R$$-saturated, then $$A\setminus X$$ is also $$R$$-saturated.

Now consider the canonical projection $$p:A\rightarrow A/R$$ and $$X\subseteq A$$. By [§Operations on Binary Relations, ⁋Proposition 7](/en/math/set_theory/operation_of_binary_relations#prop7), we obtain

$$p^{-1}(p(X))\supseteq X$$

The reverse inclusion does not hold in general, but if $$X$$ is $$R$$-saturated, then the reverse inclusion also holds. For each $$x\in X$$, since $$p^{-1}(\left\{p(x)\right\})\subseteq X$$,

$$p^{-1}(p(X))=\bigcup_{x\in X}p^{-1}(\left\{p(x)\right\})\subseteq X$$

holds.

On the other hand, even if $$X$$ is not $$R$$-saturated, the set $$p^{-1}(p(X))$$ becomes $$R$$-saturated. To see this, choose $$x\in p^{-1}(p(X))$$ arbitrarily, and let any $$x'$$ satisfying $$x\sim_{\tiny R} x'$$ be given. Then

$$x\sim_{\tiny R} x'\iff p(x)=p(x')$$

and from the given assumption, $$p(x)\in p(X)$$, so we obtain $$x'\in p^{-1}(p(X))$$. Meanwhile, if $$X'$$ is an $$R$$-saturated subset containing $$X$$, then

$$X'=p^{-1}(p(X'))\supseteq p^{-1}(p(X))$$

so $$p^{-1}(p(X))$$ is the smallest $$R$$-saturated subset containing $$X$$. This is called the *saturation* of $$X$$.

## Canonical Decomposition

<div class="definition" markdown="1">

<ins id="def6">**Definition 6**</ins> For an equivalence relation $$(R,A,A)$$ and a function $$f$$ with domain $$A$$, $$f$$ is *compatible* with $$R$$ if the unary relation $$y=f(x)$$ with respect to $$x$$ is compatible with $$R$$.

</div>

That is, for $$f$$ to be compatible with $$R$$, $$f$$ must be a constant function when restricted to each equivalence class. Now applying [§Retraction and Section, ⁋Proposition 4](/en/math/set_theory/retraction_and_section#prop4), we obtain the following.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> Consider an equivalence relation $$(R,A,A)$$ and the canonical projection $$p:A\rightarrow A/R$$. Then $$f:A\rightarrow B$$ is compatible with $$R$$ if and only if there exists $$h:A/R\rightarrow B$$ such that $$f=h\circ p$$.

</div>

That is, the following diagram commutes:

![induced_injection](/assets/images/Math/Set_Theory/Examples_of_equivalence-2.png){:style="width:7em"  class="invert" .align-center}

In this case, $$h$$ is uniquely determined by a section $$s$$ of $$p$$ as $$h=f\circ s$$.

In particular, let $$R$$ be the equivalence relation defined by $$f$$. ([Definition 2](#def2)) Then we can consider the following diagram:

![canonical_decomposition](/assets/images/Math/Set_Theory/Examples_of_equivalence-3.png){:style="width:12.4em"  class="invert" .align-center}

Here $$\tilde{f}$$ is the function obtained by restricting the codomain of $$f$$ to $$f(A)$$, and $$j$$ is the canonical injection. From the commutativity of the diagram above, we obtain the equation

$$f=j\circ\tilde{f}=j\circ h\circ p$$

If $$h(t)=h(t')$$ for some $$t, t'\in A/R$$, then for $$x\in t$$ and $$x'\in t'$$, we have $$f(x)=f(x')$$, so $$x\sim_{\tiny R}x'$$, and therefore $$t=t'$$, making $$h$$ an injective function. But since the codomain of $$h$$ is restricted to the range of $$f$$, $$h$$ is also a surjective function. Therefore, $$h$$ is a bijection, and the above equation is called the *canonical decomposition* of $$f$$.

Additionally, suppose an equivalence relation $$S$$ is given on the codomain $$B$$. Then we first obtain the following diagram:

![induced_mapping_of_equivalence](/assets/images/Math/Set_Theory/Examples_of_equivalence-4.png){:style="width:8em"  class="invert" .align-center}

If $$q\circ f$$ is compatible with $$R$$, then $$f$$ is said to be *$$(R,S)$$-compatible*. By [Proposition 7](#p75), this is equivalent to the existence of $$h:A/R\rightarrow B/S$$ such that $$h\circ p=q\circ f$$.

## Preimage of an Equivalence Relation

Let a function $$f:A\rightarrow B$$ be given, and consider an equivalence relation $$(S,B,B)$$ and the canonical projection $$p:B\rightarrow B/S$$.

![inverse_image_of_equivalence](/assets/images/Math/Set_Theory/Examples_of_equivalence-5.png){:style="width:6.9em"  class="invert" .align-center}

Then the function $$p\circ f:A\rightarrow B/S$$ is naturally defined, and the equivalence relation it creates through [Definition 2](#def2) is called the *preimage* of $$S$$ under $$f$$.

## Quotient of an Equivalence Relation

The following definition was already mentioned in [§Equivalence Relations, ⁋Example 5](/en/math/set_theory/equivalence_relations#ex5).

<div class="definition" markdown="1">

<ins id="def8">**Definition 8**</ins> For two equivalence relations $$R$$ and $$S$$ defined on a set $$A$$, $$S$$ is *finer* than $$R$$ if $$x\sim_{\tiny S}y\implies x\sim_{\tiny R}y$$ always holds.

</div>

Let two equivalence relations $$R$$ and $$S$$ defined on a set $$A$$ be given, and suppose $$S$$ is finer than $$R$$.

![third_iso_1](/assets/images/Math/Set_Theory/Examples_of_equivalence-6.png){:style="width:8em"  class="invert" .align-center}

Then the function $$p_S$$ is surjective, and $$p_S(x)=p_S(y)\implies p_R(x)=p_R(y)$$ always holds. Therefore, there exists a unique $$h:A/S \rightarrow A/R$$ such that $$p_R=h\circ p_S$$. ([§Retraction and Section, ⁋Proposition 4](/en/math/set_theory/retraction_and_section#prop4)) In this case, $$h$$ is called the *quotient* of $$R$$ by $$S$$ defined on $$A/S$$, and is written as $$R/S$$. The canonical decomposition gives:

![third_iso_2](/assets/images/Math/Set_Theory/Examples_of_equivalence-7.png){:style="width:16.6em"  class="invert" .align-center}

In particular, $$k$$ is a bijection.

## Product of Equivalence Relations

Finally, let two equivalence relations $$(R,A,A)$$ and $$(R',A',A')$$ be given, and define the relation $$(S, A\times A', A\times A')$$ by

> $$u\sim_{\tiny S}v$$ if there exist $$x$$, $$x'$$, $$y$$, $$y'$$ such that $$u=(x,x')$$, $$v=(y,y')$$, and $$x\sim_{\tiny R}y$$, $$x'\sim_{\tiny R'}y'$$

Let $$u=(x,x'),v=(y,y'),w=(z,z')$$ be elements of $$A\times A'$$. Then:

- $$u\sim_{\tiny S}u$$ always holds. This is because $$x\sim_{\tiny R}x$$ and $$x'\sim_{\tiny R'}x'$$.
- If $$u\sim_{\tiny S}v$$, then $$x\sim_{\tiny R}y$$ and $$x'\sim_{\tiny R'}y'$$, so $$y\sim_{\tiny R}x$$ and $$y'\sim_{\tiny R'}x'$$, and therefore $$v\sim_{\tiny S}u$$.
- Suppose $$u\sim_{\tiny S}v$$ and $$v\sim_{\tiny S}w$$. Then $$x\sim_{\tiny R}y, x'\sim_{\tiny R'}y', y\sim_{\tiny R}z, y'\sim_{\tiny R'}z'$$ each hold. From $$x\sim_{\tiny R}y$$ and $$y\sim_{\tiny R}z$$, we have $$x\sim_{\tiny R}z$$, and from $$x'\sim_{\tiny R'}y'$$ and $$y'\sim_{\tiny R'}z'$$, we have $$x'\sim_{\tiny R'}z'$$. That is, $$u\sim_{\tiny S}w$$ holds.

Therefore, $$S$$ is an equivalence relation. This equivalence relation is called the *product* of $$R$$ and $$R'$$, and is written as $$R\times R'$$.

Let two functions $$f:A\rightarrow B$$ and $$f':A'\rightarrow B'$$ be given, and let $$R$$ and $$R'$$ be the equivalence relations induced by $$f$$ and $$f'$$, respectively. Then $$f\times f':A\times A'\rightarrow B\times B'$$ is well-defined, and through this function, we can define an equivalence relation on $$A\times A'$$. Calling this equivalence relation $$S$$ temporarily, for any $$u=(x,x'),v=(y,y')\in A\times A'$$,

$$\begin{aligned}u\sim_{\tiny S}v&\iff (f\times f')(u)=(f\times f')(v)\iff (f(x),f'(x')=(f(y),f'(y'))\\
&\iff (f(x)=f(y))\wedge(f'(x')=f'(y'))\iff (x\sim_{\tiny R}y)\wedge(x'\sim_{\tiny R'}y')\\&\iff u\sim_{\tiny R\times R'}v\end{aligned}$$

so $$S=R\times R'$$. At this point, since the image of $$A\times A'$$ under $$f\times f'$$ equals $$f(A)\times f'(A')$$, considering the canonical decomposition of $$f\times f'$$, there exists a bijection between $$(A\times A')/(R\times R')$$ and $$f(A)\times f'(A')$$.

![canonical_bijection_between_product](/assets/images/Math/Set_Theory/Examples_of_equivalence-8.png){:style="width:24em" class="invert" .align-center}

On the other hand, consider the following diagram:

![canonical_bijection_between_product_2](/assets/images/Math/Set_Theory/Examples_of_equivalence-9.png){:style="width:20em" class="invert" .align-center}

Here $$A/R\rightarrow f(A)$$ and $$A'/R'\rightarrow f'(A')$$ are the bijections obtained from the canonical decompositions of $$f$$ and $$f'$$, respectively. Therefore, the function $$(A/R)\times (A/R')\rightarrow f(A)\times f'(A')$$ induced by these is also a bijection.

By appropriately composing the two bijections obtained above and their inverses, we can obtain a bijection between $$(A\times A')/(R\times R')$$ and $$(A/R)\times(A'/R')$$. These bijections are also called canonical.

---
**References**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
