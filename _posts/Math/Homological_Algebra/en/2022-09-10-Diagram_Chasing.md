---
title: "Diagram chasing"
description: "This post proves the five lemma and snake lemma, two fundamental results in homological algebra, using diagram chasing techniques, and discusses their generalization via the Freyd-Mitchell embedding theorem."
excerpt: "Five lemma, snake lemma"

categories: [Math / Homological Algebra]
permalink: /en/math/homological_algebra/diagram_chasing
header:
    overlay_image: /assets/images/Math/Homological_Algebra/Diagram_Chasing.png
    overlay_filter: 0.5
sidebar: 
    nav: "homological_algebra-en"

date: 2022-09-10
last_modified_at: 2024-10-31
weight: 1
translated_at: 2026-05-31T12:00:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-31T12:00:04+00:00
---
Homological algebra is, literally, the study of the properties of chain complexes via their homology. ([\[Category Theory\] §Abelian Categories, ⁋Definition 4](/en/math/category_theory/abelian_categories#def4)) Chain complexes are defined in any abelian category, but by the Freyd-Mitchell embedding theorem they can all be embedded as a full subcategory of some $$\lMod{A}$$. ([\[Category Theory\] §Abelian Categories, ⁋Theorem 8 (Freyd-Mitchell embedding theorem)](/en/math/category_theory/abelian_categories#thm8))

In this post we prove the five lemma and the snake lemma, two essential lemmas in homological algebra. Their proofs can be carried out using the universal properties of kernels and cokernels, but this would make the arguments unnecessarily long, so we work throughout in $$\lMod{A}$$. In particular, this means we may pick elements from each object. Such arguments are called diagram chasing, and the passage from an arbitrary abelian category to $$\lMod{A}$$ is justified by the Freyd-Mitchell embedding theorem mentioned above.

## The Five Lemma

<div class="proposition" markdown="1">

<ins id="prop1">**Proposition 1 (The four lemma)**</ins> Consider a commutative diagram whose rows are exact

![Four_lemma](/assets/images/Math/Homological_Algebra/Diagram_Chasing-1.png){:style="width:14em" class="invert" .align-center}

and assume that $$\alpha$$ is surjective and $$\delta$$ is injective. Then

1. If $$\gamma$$ is surjective, then $$\beta$$ is also surjective.
2. If $$\beta$$ is injective, then $$\gamma$$ is also injective.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

1. Pick any $$b'\in B'$$. We must show that there exists some $$b\in B$$ with $$\beta(b)=b'$$. Since $$\gamma$$ is surjective by assumption, there exists some $$c\in C$$ such that $$\gamma(c)=g'(b')\in C'$$. Now
  
    $$\delta(h(c))=h'(\gamma(c))=h'(g'(b'))=0$$

    so $$h(c)\in\ker\delta$$, and since $$\delta$$ is injective we have $$h(c)=0$$. Thus $$c\in\ker(h)=\im(g)$$, so there exists some $$b_0\in B$$ such that $$g(b_0)=c$$. For this $$b_0$$, consider $$b'-\beta(b_0)\in B'$$. Then

    $$g'(b'-\beta(b_0))=g'(b')-g'(\beta(b_0))=\gamma(c)-\gamma(g(b_0))=\gamma(c)-\gamma(c)=0$$

    so $$b'-\beta(b_0)\in\ker(g')=\im(f')$$. Hence there exists some $$a'\in A'$$ such that $$f'(a')=b'-\beta(b_0)$$. Since $$\alpha$$ is surjective, there exists $$a\in A$$ satisfying $$\alpha(a)=a'$$. Then

    $$\beta(f(a))=f'(\alpha(a))=f'(a')=b'-\beta(b_0)$$

    and setting $$b=b_0+f(a)$$ we obtain $$\beta(b)=b'$$.
2. Suppose some $$c\in C$$ satisfies $$\gamma(c)=0$$. We must show that $$c=0$$. First,

    $$0=h'(0)=h'(\gamma(c))=\delta(h(c))$$

    and since $$\delta$$ is injective we know that $$h(c)=0$$. Thus $$c\in\ker(h)=\im(g)$$, so there exists some $$b_0\in B$$ such that $$g(b_0)=c$$. Now consider the element $$\beta(b_0)\in B'$$:

    $$g'(\beta(b_0))=\gamma(g(b_0))=\gamma(c)=0$$

    so $$\beta(b_0)\in\ker(g')=\im(f')$$. Hence there exists some $$a'\in A'$$ such that $$f'(a')=\beta(b_0)$$, and since $$\alpha$$ is surjective there also exists $$a\in A$$ satisfying $$\alpha(a)=a'$$. Set $$b=b_0-f(a)$$. Then

    $$g(b)=g(b_0-f(a))=g(b_0)-g(f(a))=g(b_0)=c$$

    On the other hand,

    $$\beta(b)=\beta(b_0-f(a))=\beta(b_0)-\beta(f(a))=\beta(b_0)-f'(\alpha(a))=\beta(b_0)-f'(a')=\beta(b_0)-\beta(b_0)=0$$

    so $$b\in\ker(\beta)$$, and since $$\beta$$ is injective we get $$b=0$$. Therefore $$c=g(b)=0$$, and $$\gamma$$ is injective.

</details>

The above proposition has the following two immediate corollaries.

<div class="proposition" markdown="1">

<ins id="cor2">**Corollary 2 (The five lemma)**</ins> Consider a commutative diagram whose rows are exact

![five_lemma](/assets/images/Math/Homological_Algebra/Diagram_Chasing-2.png){:style="width:17.8em" class="invert" .align-center}

If $$\alpha,\beta,\delta,\epsilon$$ are all isomorphisms, then $$\gamma$$ is also an isomorphism.

</div>

<div class="proposition" markdown="1">

<ins id="cor3">**Corollary 3 (The short five lemma)**</ins> Consider a commutative diagram whose rows are exact

![short_five_lemma](/assets/images/Math/Homological_Algebra/Diagram_Chasing-3.png){:style="width:18em" class="invert" .align-center}

If $$\alpha,\gamma$$ are both injective then $$\beta$$ is also injective, and if $$\alpha,\gamma$$ are both surjective then $$\beta$$ is also surjective.

</div>

## The Snake Lemma

The main goal of the remainder of this post is to prove the snake lemma, and for this we need two lemmas.

<div class="proposition" markdown="1">

<ins id="lem4">**Lemma 4**</ins> Suppose a commutative square

![induced_morphism](/assets/images/Math/Homological_Algebra/Diagram_Chasing-4.png){:style="width:6em" class="invert" .align-center}

is given. Then $$\xi$$ sends $$\ker(h)$$ to $$\ker(h')$$ and $$\eta$$ sends $$\im(h)$$ to $$\im(h')$$, and in particular the following maps

$$\xi^\sharp:\ker(h)\rightarrow\ker(h'),\quad \eta^\sharp:\im(h)\rightarrow\im(h'),\quad\xi^\ast:X/\ker(h)\rightarrow X'/\ker(h'),\quad \eta^\ast:\coker(h)\rightarrow\coker(h')$$

are well-defined.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Consider the composition $$\xi\circ i:\ker h\rightarrow X'$$ of $$i:\ker(h)\rightarrow X$$ and $$\xi$$. Then

$$h'\circ(\xi\circ i)=(\eta\circ h)\circ i=\eta\circ 0=0$$

so by the universal property of the kernel there exists a unique $$\xi^\sharp:\ker(h)\rightarrow\ker(h')$$.

![induced_morphism_kernel](/assets/images/Math/Homological_Algebra/Diagram_Chasing-5.png){:style="width:13em" class="invert" .align-center}

Similarly, from $$p'\circ\eta:Y\rightarrow \coker (h')$$,

$$(p'\circ\eta)\circ h=p'\circ(h'\circ\xi)=(p'\circ h')\circ\xi=0\circ\xi=0$$

and we can define $$\eta^\ast$$ from the universal property of $$\coker(h)$$.

![induced_morphism_cokernel](/assets/images/Math/Homological_Algebra/Diagram_Chasing-6.png){:style="width:13.6em" class="invert" .align-center}

By definition $$\coker(h)=Y/\im(h)$$ and $$\coker(h')=Y'/\im(h')$$, so since $$\eta^\ast$$ sends $$0$$ to $$0$$, $$\eta^\sharp$$ is also well-defined. Finally, for $$\xi^\ast$$, consider $$p:X'\rightarrow X'/\ker(h')$$; then

$$\ker(h)\subseteq\ker(p\circ\xi)$$

and therefore $$p\circ\xi$$ induces $$\xi^\ast:X/\ker(h)\rightarrow X'/\ker(h')$$.

</details>

Using this we can prove the following lemma.

<div class="proposition" markdown="1">

<ins id="lem5">**Lemma 5**</ins> Suppose a commutative diagram whose rows are exact

![induced_exact_sequence](/assets/images/Math/Homological_Algebra/Diagram_Chasing-7.png){:style="width:10.4em" class="invert" .align-center}

is given. Then $$f,g$$ and $$f',g'$$ induce the two columns

$$\ker(\alpha)\rightarrow\ker(\beta)\rightarrow\ker(\gamma),\qquad \coker(\alpha)\rightarrow\coker(\beta)\rightarrow\coker(\gamma)$$

Moreover, if $$f':A'\rightarrow B'$$ is injective then the first column is exact, and if $$g:B\rightarrow C$$ is surjective then the second column is exact.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

That $$f,g$$ and $$f',g'$$ induce the two given columns

$$\ker(\alpha)\overset{f^\sharp}{\longrightarrow}\ker(\beta)\overset{g^\sharp}{\longrightarrow}\ker(\gamma),\qquad \coker(\alpha)\overset{(f')^\ast}{\longrightarrow}\coker(\beta)\overset{(g')^\ast}{\longrightarrow}\coker(\gamma)$$

is a consequence of [Lemma 4](#lem4). Moreover, letting $$i_A, i_B, i_C$$ be the canonical maps from the kernels to $$A,B,C$$ respectively,

$$i_C\circ g^\sharp\circ f^\sharp=g\circ i_B\circ f^\sharp=g\circ f\circ i_A=0$$

and since $$i_C$$ is injective we verify that $$g^\sharp\circ f^\sharp=0$$. Similarly, letting $$p_A,p_B,p_C$$ be the canonical maps from $$A,B,C$$ to the cokernels respectively,

$$(g')^\ast\circ(f')^\ast\circ p_C=(g')^\ast\circ p_B\circ f=p_A\circ g'\circ f'=0$$

and since $$p_C$$ is surjective we verify that $$(g')^\ast\circ(f')^\ast=0$$. Therefore, to prove the statement it suffices to show that if $$f':A'\rightarrow B'$$ is injective then $$\ker(g^\sharp)\subset\im(f^\sharp)$$, and if $$g:B\rightarrow C$$ is surjective then $$\ker((g')^\ast)\subset\im((f')^\ast)$$.

First assume that $$f'$$ is injective. If $$g^\sharp(b)=0$$ for some $$b\in\ker(\beta)$$, then by the definition of $$g^\sharp$$ we have $$g(b)=0$$ and therefore $$b\in\ker(g)=\im(f)$$. Thus there exists some $$a\in A$$ such that $$f(a)=b$$. But

$$(f'\circ\alpha)(a)=(\beta\circ f)(a)=\beta(f(a))=\beta(b)=0$$

and since $$f'$$ is injective we have $$a\in\ker(\alpha)$$, and from $$f(a)=f^\sharp(a)=b$$ we obtain $$b\in\im(f^\sharp)$$.

Now assume that $$g$$ is surjective. Let $$b'\in\coker(\beta)$$ be an element of $$\ker((g')^\ast)$$. That is, $$((g')^\ast)(b')=g'(b')+\im(\gamma)=0$$. But $$g'(b')\in\im(\gamma)$$, so there exists some $$c\in C$$ such that $$\gamma(c)=g'(b')$$, and since $$g$$ is surjective there exists some $$b\in B$$ such that $$g(b)=c$$. Then

$$g'(b')=\gamma(c)=(\gamma\circ g)(b)=(g'\circ\beta)(b)$$

so $$b'-\beta(b)\in\ker(g')=\im(f')$$. Now pick $$a'\in A'$$ satisfying $$f'(a')=b'-\beta(b)$$. Then $$f'(a')-b'\in\im(\beta)$$, so

$$f'(a')+\im(\beta)=b'+\im(\beta)$$

and therefore

$$((f')^\ast)(a'+\im(\alpha))=b'+\im(\beta)$$

holds.

</details>

Now we can finally prove the snake lemma.

<div class="proposition" markdown="1">

<ins id="thm6">**Theorem 6 (The snake lemma)**</ins> Consider a commutative diagram whose rows are exact

![snake_diagram](/assets/images/Math/Homological_Algebra/Diagram_Chasing-8.png){:style="width:18.8em" class="invert" .align-center}

Here the top and bottom rows are each exact. Then there exists a map $$\delta:\ker(\gamma)\rightarrow\coker(\alpha)$$ connecting the two exact sequences obtained from [Lemma 5](#lem5)

$$\ker(\alpha)\rightarrow\ker(\beta)\rightarrow\ker(\gamma),\qquad \coker(\alpha)\rightarrow\coker(\beta)\rightarrow\coker(\gamma)$$

so that the following column, joined through it,

$$\ker(\alpha)\rightarrow\ker(\beta)\rightarrow\ker(\gamma)\rightarrow\coker(\alpha)\rightarrow\coker(\beta)\rightarrow\coker(\gamma)$$

forms an exact sequence.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

To prove this it suffices to construct $$\delta$$ and then show that the above column is exact at $$\ker(\gamma)$$ and $$\coker(\alpha)$$.

First pick some $$c\in\ker(\gamma)$$. Since $$g$$ is surjective, there exists some $$b\in B$$ such that $$g(b)=c$$, and this $$b$$ satisfies

$$0=\gamma(c)=\gamma(g(b))=(\gamma\circ g)(b)=(g'\circ\beta)(b)=g'(\beta(b))$$

That is, $$\beta(b)\in\ker(g')=\im(f')$$. Hence there exists a unique $$a'$$ such that $$f'(a')=\beta(b)$$. For this $$a'$$, set $$\delta(c)=a'+\im(\alpha)\in \coker(\alpha)$$.

For the map $$\delta$$ to be well-defined, the above value must not depend on the choice of $$b$$. Pick another $$b_1\in B$$ satisfying $$g(b_1)=c$$, and in the same way pick $$a_1'\in A'$$ satisfying $$f'(a_1')=\beta(b_1)$$. Then

$$0=(g'\circ f')(a_1'-a_1)=(g'\circ \beta)(b_1-b)=(\gamma\circ g)(b_1-b)$$

so $$b_1-b\in\ker(g)=\im(f)$$ holds. Now finding $$a\in A$$ such that $$f(a)=b_1-b$$, we have

$$f'(\alpha(a))=\beta(f(a))=\beta(b_1)-\beta(b)=f'(a_1'-a')$$

and since $$f'$$ is injective, $$\alpha(a)=a_1'-a'$$ holds. That is, $$a_1'\equiv a' \mod \im(\alpha)$$, and $$\delta$$ is well-defined. It is not difficult to show that $$\delta$$ is a homomorphism of $$A$$-modules.

We must show that this $$\delta$$ makes the following column

$$\ker(\beta)\rightarrow\ker(\gamma)\rightarrow\coker(\alpha)\rightarrow\coker(\beta)$$

into an exact sequence. First let $$b\in \ker(\beta)$$. If we write $$\delta(g^\sharp(b))=a'+\im(\alpha)$$, then $$a'$$ is determined by the equation $$f'(a')=\beta(b)$$; since $$b\in\ker(\beta)$$ we have $$f'(a')=0$$, and since $$f'$$ is injective we must have $$a'=0$$. Thus $$\delta\circ g^\sharp=0$$. Similarly, for any $$c\in\ker(\gamma)$$ if we write $$\delta(c)=a'+\im(\alpha)$$, then

$$((f')^\ast)(a'+\im(\alpha))=f'(a')+\im(\beta)=\beta(b)+\im(\beta)=0$$

Therefore it suffices to show that $$\ker(\delta)\subset\im(g^\sharp)$$ and $$\ker(f')^\ast\subset\im(\delta)$$.

First let $$c\in\ker(\delta)$$. Then $$a'$$ is defined as the element satisfying $$f'(a')=\beta(b)$$ for $$b$$ with $$g(b)=c$$, so $$a'\in\im(\alpha)$$. Now pick $$a\in A$$ satisfying $$\alpha(a)=a'$$. Then

$$\beta(b)=f'(a')=f'(\alpha(a))=\beta(f(a))$$

so $$b-f(a)\in\ker(\beta)$$. Now

$$g^\sharp(b-f(a))=g(b-f(a))=g(b)-g(f(a))=g(b)=c$$

so $$c\in\im g^\sharp$$ holds.

Similarly let $$a'\in\ker(f')^\ast$$. Then $$f'(a')\in\im(\beta)$$, so there exists some $$b\in B$$ such that $$\beta(b)=f'(a')$$, and for this $$b$$

$$\gamma(g(b))=(g'\circ\beta)(b)=(g'\circ f')(a')=0$$

holds, so $$g(b)\in\ker(\gamma)$$. Therefore $$\delta(g(b))$$ is well-defined, and since $$b$$ was chosen exactly as the element satisfying $$f'(a')=\beta(b)$$, this value equals exactly $$a'+\im(\alpha)$$.

</details>

This theorem is called the snake lemma because when the connecting map $$\delta$$ is drawn, the following shape appears.

![connecting_map_of_snake_diagram](/assets/images/Math/Homological_Algebra/Diagram_Chasing-9.png){:style="width:27em" class="invert" .align-center}

The snake lemma is usually used to draw long exact sequences as in the next post, but it also has the following additional corollary.

<div class="proposition" markdown="1">

<ins id="cor7">**Corollary 7 (The 3×3 lemma)**</ins> Consider a commutative diagram whose rows are exact

![Nine_lemma](/assets/images/Math/Homological_Algebra/Diagram_Chasing-10.png){:style="width:19em" class="invert" .align-center}

If the first two columns are both short exact sequences then the last column is also a short exact sequence, and if the last two columns are both short exact sequences then the first column is also a short exact sequence.

</div>

---

**References**

**[Hu]** S.T. Hu, *Introduction to homological algebra*. University Microfilms, 1979.
