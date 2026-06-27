---
title: "Examples of Equivalence Relations"
description: "This post covers examples of equivalence relations naturally defined from functions, along with saturation of equivalence relations and isomorphism theorems."
excerpt: "Examples of equivalence relations, saturation, and isomorphism theorems"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/examples_of_equivalence
sidebar: 
    nav: "set_theory-en"

date: 2021-08-22
weight: 13
translated_at: 2026-06-27T01:00:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-27T01:00:02+00:00
---
In this post, we examine examples of equivalence relations that appear in various contexts.

## Equivalence relation defined by a function

In the previous post, we saw that from an equivalence relation $$(R,A,A)$$, the canonical function $$p:A\rightarrow A/R$$ is well defined; the converse also holds. That is, given any function, we can use it to construct an equivalence relation.

<div class="proposition" markdown="1">

<ins id="prop1">**Proposition 1**</ins> Let a set $$A$$ and a function $$f$$ with domain $$A$$ be given. Then the relation between $$x$$ and $$y$$ defined by <phrase>$x,y\in A$ and $f(x)=f(y)$</phrase> is an equivalence relation on $$A$$.
</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

That the given relation is reflexive on $$A$$ is obvious. On the other hand, if $$f(x)=f(y)$$ then $$f(y)=f(x)$$, and if $$f(x)=f(y)$$ and $$f(y)=f(z)$$ then $$f(x)=f(z)$$, so this relation is also symmetric and transitive.

</details>

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> The equivalence relation defined in the above proposition is called the *equivalence relation defined by $$f$$*.

</div>

For an equivalence relation $$(R,A,A)$$ and the induced $$p:A\rightarrow A/R$$, one can verify that the equivalence relation $$R$$ is exactly the same as the equivalence relation obtained by applying [Definition 2](#def2) to $$p$$.

## Equivalence relations compatible with a unary relation

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> Let $$(R,A,A)$$ be an equivalence relation. Then a unary relation $$P$$ is *compatible* with $$R$$ if $$P(x)\wedge (x\sim_{\tiny R}y)\implies P(y)$$.

</div>

For example, the unary relation

>$$x$$ is even

is compatible with the equivalence relation

>$$x-y$$ is a multiple of 4.

From the viewpoint of equivalence classes, the above definition can be rewritten as follows.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> Let $$R$$ be an equivalence relation on a set $$A$$, and let $$P$$ be a unary relation compatible with $$R$$. Then the statement <phrase>$t\in A/R$ and there exists some $x\in t$ such that $P(x)$</phrase> and the statement <phrase>$t\in A/R$ and $P(x)$ holds for all $x\in t$</phrase> are equivalent.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

In other words,

> When $$P$$ is compatible with $$R$$, if a single element of an equivalence class satisfies $$P$$, then $$P$$ holds for all elements in the same class as that element.

And this is exactly the definition of a compatible unary relation.

The converse direction is obvious. Suppose for some $$t\in A/R$$ there exists $$a\in t$$ such that $$P(a)$$. Then for every $$x\in t$$ we have $$a\sim_{\tiny R}x$$, so $$P(x)$$ holds.

</details>

## Saturation of an equivalence relation

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> Let $$R$$ be an equivalence relation on $$A$$ and let $$X$$ be a subset of $$A$$. We say that $$X$$ is *saturated* with respect to $$R$$ if the unary relation $$x\in A$$ is compatible with $$R$$.

</div>

![saturated_set](/assets/images/Math/Set_Theory/Examples_of_Equivalence-1.png){:style="width:600px" class="invert" .align-center}

<cap>A saturated subset (left) and a non-saturated subset (right) in a given quotient set (above)</cap>

According to the above definition, for a set $$X$$ to be $$R$$-saturated, <phrase>if $x\in X$ then $R(x)\subseteq X$</phrase> must necessarily hold. Therefore, an $$R$$-saturated subset $$X$$ is a set that can be expressed as $$\bigcup_{x\in B}R(x)$$ for some subset $$B\subseteq A$$. From this, the following two results can be easily verified.

1. If $$(A_i)_{i\in I}$$ is a family of $$R$$-saturated subsets, then $$\bigcup_{i\in I} A_i$$ and $$\bigcap_{i\in I} A_i$$ are also $$R$$-saturated.
2. If $$X\subseteq A$$ is $$R$$-saturated, then $$A\setminus X$$ is also $$R$$-saturated.

Now consider the canonical projection $$p:A\rightarrow A/R$$ and $$X\subseteq A$$. By [§Operations on Binary Relations, ⁋Proposition 7](/en/math/set_theory/operation_of_binary_relations#prop7), we obtain

$$p^{-1}(p(X))\supseteq X$$

In general, the reverse inclusion does not hold, but if $$X$$ is $$R$$-saturated, then the reverse inclusion also holds. For each $$x\in X$$, since $$p^{-1}(\left\{p(x)\right\})\subseteq X$$, we have

$$p^{-1}(p(X))=\bigcup_{x\in X}p^{-1}(\left\{p(x)\right\})\subseteq X$$

On the other hand, even if $$X$$ is not $$R$$-saturated, the set $$p^{-1}(p(X))$$ is $$R$$-saturated. To see this, choose any $$x\in p^{-1}(p(X))$$ and suppose any $$x'$$ satisfying $$x\sim_{\tiny R} x'$$ is given. Then

$$x\sim_{\tiny R} x'\iff p(x)=p(x')$$

and since $$p(x)\in p(X)$$ by the given assumption, we obtain $$x'\in p^{-1}(p(X))$$. On the other hand, if $$X'$$ is an $$R$$-saturated subset containing $$X$$, then

$$X'=p^{-1}(p(X'))\supseteq p^{-1}(p(X))$$

so $$p^{-1}(p(X))$$ is the smallest $$R$$-saturated subset containing $$X$$. We call this the *saturation* of $$X$$.

## Canonical decomposition

<div class="definition" markdown="1">

<ins id="def6">**Definition 6**</ins> For an equivalence relation $$(R,A,A)$$ and a function $$f$$ with domain $$A$$, we say that $$f$$ is *compatible* with $$R$$ if the unary relation $$y=f(x)$$ in $$x$$ is compatible with $$R$$.

</div>

That is, for $$f$$ to be compatible with $$R$$, $$f$$ must become a constant function when restricted to each equivalence class. Now applying [§Retraction and Section, ⁋Proposition 4](/en/math/set_theory/retraction_and_section#prop4), we obtain the following.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> Consider an equivalence relation $$(R,A,A)$$ and the canonical $$p:A\rightarrow A/R$$. Then $$f:A\rightarrow B$$ is compatible with $$R$$ if and only if there exists $$h:A/R\rightarrow B$$ such that $$f=h\circ p$$.

</div>

That is, the following diagram commutes.

![induced_injection](/assets/images/Math/Set_Theory/Examples_of_Equivalence-2.svg){:style="width:6.67em"  class="invert" .align-center}

In this case, $$h$$ is uniquely determined by a section $$s$$ of $$p$$ via $$h=f\circ s$$.

In particular, suppose $$R$$ is the equivalence relation defined by $$f$$. ([Definition 2](#def2)) Then we can consider the following diagram.

![canonical_decomposition](/assets/images/Math/Set_Theory/Examples_of_Equivalence-3.svg){:style="width:12.57em"  class="invert" .align-center}

Here $$\tilde{f}$$ is the function obtained by restricting the codomain $$F$$ of $$f$$ to $$f(A)$$, and $$j$$ is the canonical injection. From the commutativity of the above diagram, we obtain the equation

$$f=j\circ\tilde{f}=j\circ h\circ p$$

If $$h(t)=h(t')$$ for some $$t, t'\in A/R$$, then for $$x\in t$$, $$x'\in t'$$ we have $$f(x)=f(x')$$, so $$x\sim_{\tiny R}x'$$, and thus $$t=t'$$, which shows that $$h$$ is injective. However, since the codomain of $$h$$ is restricted to the image of $$f$$, $$h$$ is also surjective. Therefore $$h$$ is bijective, and we call the above equation the *canonical decomposition* of $$f$$.

Additionally, suppose an equivalence relation $$S$$ is given on the codomain $$B$$. Then we first obtain the following diagram.

![induced_mapping_of_equivalence](/assets/images/Math/Set_Theory/Examples_of_Equivalence-4.svg){:style="width:7.95em"  class="invert" .align-center}

If $$q\circ f$$ is compatible with $$R$$, then we say that $$f$$ is *$$(R,S)$$-compatible*. By [Proposition 7](#prop7), this is equivalent to the existence of $$h:A/R\rightarrow B/S$$ such that $$h\circ p=q\circ f$$.

## Preimage of an equivalence relation

Let a function $$f:A\rightarrow B$$ be given, and consider the equivalence relation $$(S,B,B)$$ and the canonical $$p:B\rightarrow B/S$$.

![inverse_image_of_equivalence](/assets/images/Math/Set_Theory/Examples_of_Equivalence-5.svg){:style="width:6.57em"  class="invert" .align-center}

Then the function $$p\circ f:A\rightarrow B/S$$ is naturally defined, and the equivalence relation on $$A$$ created by this function via [Definition 2](#def2) is called the *preimage* of $$S$$ under $$f$$.

## Quotient of equivalence relations

The following definition was already mentioned in [§Equivalence Relations, ⁋Example 5](/en/math/set_theory/equivalence_relations#ex5).

<div class="definition" markdown="1">

<ins id="def8">**Definition 8**</ins> For two equivalence relations $$R,S$$ defined on a set $$A$$, we say that $$S$$ is *finer* than $$R$$ if $$x\sim_{\tiny S}y\implies x\sim_{\tiny R}y$$ always holds.

</div>

Let two equivalence relations $$R,S$$ be defined on a set $$A$$, and suppose $$S$$ is finer than $$R$$.

![third_iso_1](/assets/images/Math/Set_Theory/Examples_of_Equivalence-6.svg){:style="width:8.11em"  class="invert" .align-center}

Then the function $$p_S$$ is surjective, and $$p_S(x)=p_S(y)\implies p_R(x)=p_R(y)$$ always holds. Therefore, there exists a unique $$h:A/S \rightarrow A/R$$ such that $$p_R=h\circ p_S$$. ([§Retraction and Section, ⁋Proposition 4](/en/math/set_theory/retraction_and_section#prop4)) In this case, we call the equivalence relation that $$h$$ defines on $$A/S$$ the *quotient* of $$R$$ by $$S$$, and denote it by $$R/S$$. Passing through the canonical decomposition, we have

![third_iso_2](/assets/images/Math/Set_Theory/Examples_of_Equivalence-7.svg){:style="width:18.05em"  class="invert" .align-center}

and in particular, $$k$$ is bijective.

## Product of equivalence relations

Finally, suppose two equivalence relations $$(R,A,A)$$, $$(R',A',A')$$ are given, and define the relation $$(S, A\times A', A\times A')$$ by

> $$u\sim_{\tiny S}v$$ means that there exist $$x$$, $$x'$$, $$y$$, $$y'$$ such that $$u=(x,x')$$, $$v=(y,y')$$ and $$x\sim_{\tiny R}y$$, $$x'\sim_{\tiny R'}y'$$.

Let $$u=(x,x'),v=(y,y'),w=(z,z')$$ be elements of $$A\times A'$$. Then

- That $$u\sim_{\tiny S}u$$ always holds is obvious, since $$x\sim_{\tiny R}x$$ and $$x'\sim_{\tiny R'}x'$$.
- If $$u\sim_{\tiny S}v$$, then <phrase>$x\sim_{\tiny R}y$ and $x'\sim_{\tiny R'}y'$</phrase>, so <phrase>$y\sim_{\tiny R}x$ and $y'\sim_{\tiny R'}x'$</phrase>, and therefore $$v\sim_{\tiny S}u$$.
- Suppose $$u\sim_{\tiny S}v$$ and $$v\sim_{\tiny S}w$$. Then <phrase>$x\sim_{\tiny R}y,x'\sim_{\tiny R'}y',y\sim_{\tiny R}z,y'\sim_{\tiny R'}z'$</phrase> each hold. Now from $$x\sim_{\tiny R}y$$ and $$y\sim_{\tiny R}z$$ we get $$x\sim_{\tiny R}z$$, and from $$x'\sim_{\tiny R'}y'$$ and $$y'\sim_{\tiny R'}z'$$ we get $$x'\sim_{\tiny R'}z'$$. That is, $$u\sim_{\tiny S}w$$ holds.

Therefore $$S$$ is an equivalence relation. We call this equivalence relation the *product* of $$R$$ and $$R'$$, and denote it by $$R\times R'$$.

Let two functions $$f:A\rightarrow B$$, $$f':A'\rightarrow B'$$ be given, and let $$R$$ and $$R'$$ be the equivalence relations induced by $$f$$ and $$f'$$ respectively. Then $$f\times f':A\times A'\rightarrow B\times B'$$ is well defined, and through this function we can define an equivalence relation on $$A\times A'$$. Let us call this equivalence relation $$S$$ for a moment; then for any $$u=(x,x'),v=(y,y')\in A\times A'$$,

$$\begin{aligned}u\sim_{\tiny S}v&\iff (f\times f')(u)=(f\times f')(v)\iff (f(x),f'(x')=(f(y),f'(y'))\\
&\iff (f(x)=f(y))\wedge(f'(x')=f'(y'))\iff (x\sim_{\tiny R}y)\wedge(x'\sim_{\tiny R'}y')\\&\iff u\sim_{\tiny R\times R'}v\end{aligned}$$

so $$S=R\times R'$$. Since the image of $$A\times A'$$ under $$f\times f'$$ equals $$f(A)\times f'(A')$$, considering the canonical decomposition of $$f\times f'$$, there exists a bijection between $$(A\times A')/(R\times R')$$ and $$f(A)\times f'(A')$$.

![canonical_bijection_between_product](/assets/images/Math/Set_Theory/Examples_of_Equivalence-8.svg){:style="width:26.00em" class="invert" .align-center}

On the other hand, consider the following diagram.

![canonical_bijection_between_product_2](/assets/images/Math/Set_Theory/Examples_of_Equivalence-9.svg){:style="width:20.50em" class="invert" .align-center}

Here $$A/R\rightarrow f(A)$$ and $$A'/R'\rightarrow f'(A')$$ are the bijections obtained from the canonical decompositions of $$f$$ and $$f'$$ respectively. Therefore, the function $$(A/R)\times (A/R')\rightarrow f(A)\times f'(A')$$ induced by them is also bijective.

By appropriately composing the two bijections obtained above and their inverses, we can obtain a bijection between $$(A\times A')/(R\times R')$$ and $$(A/R)\times(A'/R')$$. These bijections are also called canonical.

---
**References**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
