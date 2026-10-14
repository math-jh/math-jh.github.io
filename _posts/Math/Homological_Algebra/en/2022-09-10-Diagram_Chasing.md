---
title: "Diagram chasing"
description: "This post proves the five lemma and snake lemma, key lemmas in homological algebra, using diagram chasing techniques, and discusses their generalization via the Freyd-Mitchell embedding theorem."
excerpt: "Five lemma, snake lemma"

categories: [Math / Homological Algebra]
permalink: /en/math/homological_algebra/diagram_chasing
sidebar: 
    nav: "homological_algebra-en"

date: 2022-09-10
weight: 1
translated_at: 2026-05-31T12:00:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-10T15:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
Homological algebra is, literally, the study of examining the properties of chain complexes using their homology when chain complexes are given. ([\[Category Theory\] §Abelian Categories, ⁋Definition 4](/en/math/category_theory/abelian_categories#def4){: data-lid="yy10y" }) Chain complexes are defined in an arbitrary abelian category, but by the Freyd-Mitchell embedding theorem, they can all be embedded into a full subcategory of a suitable $\lMod{A}$. ([\[Category Theory\] §Abelian Categories, ⁋Theorem 8 (Freyd-Mitchell embedding theorem)](/en/math/category_theory/abelian_categories#thm8){: data-lid="0tnor" }) 

In this post, we prove the five lemma and the snake lemma, essential lemmas in homological algebra. Although their proofs can be carried out using the universal property of kernels and cokernels, this can make the proofs unnecessarily long, so we conduct all proofs in $\lMod{A}$. In particular, this means that we can pick elements from each object. Such proofs are called diagram chasing, and carrying out the proofs in $\lMod{A}$ instead of an arbitrary abelian category can be justified by the Freyd-Mitchell embedding theorem mentioned above.

## The Five Lemma

::: Proposition 1 (The four lemma)
Suppose a commutative diagram whose rows are exact

{% diagram Math/Homological_Algebra/Diagram_Chasing-1.svg width="15.54em" alt="Four_lemma" %}

is given, and assume that $\alpha$ is surjective and $\delta$ is injective. Then

1. If $\gamma$ is surjective, then $\beta$ is also surjective.
2. If $\beta$ is injective, then $\gamma$ is also injective.
:::
::: Proof
1. Choose any $b'\in B'$. We must show that there exists some $b\in B$ such that $\beta(b)=b'$. By assumption, $\gamma$ is surjective, so there exists some $c\in C$ such that $\gamma(c)=g'(b')\in C'$ holds. Now
  
    $$\delta(h(c))=h'(\gamma(c))=h'(g'(b'))=0$$

    so $h(c)\in\ker\delta$, and since $\delta$ is injective, $h(c)=0$. That is, $c\in\ker(h)=\im(g)$, so there exists some $b_0\in B$ such that $g(b_0)=c$. Now for this $b_0$, consider $b'-\beta(b_0)\in B'$. Then

    $$g'(b'-\beta(b_0))=g'(b')-g'(\beta(b_0))=\gamma(c)-\gamma(g(b_0))=\gamma(c)-\gamma(c)=0$$

    so $b'-\beta(b_0)\in\ker(g')=\im(f')$ holds. Therefore, there exists some $a'\in A'$ such that $f'(a')=b'-\beta(b_0)$. Since $\alpha$ is surjective, there exists $a\in A$ satisfying $\alpha(a)=a'$. Then

    $$\beta(f(a))=f'(\alpha(a))=f'(a')=b'-\beta(b_0)$$

    and therefore, if we set $b=b_0+f(a)$, we can verify that $\beta(b)=b'$.
2. Suppose some $c\in C$ satisfies $\gamma(c)=0$. We must show that $c=0$. First,

    $$0=h'(0)=h'(\gamma(c))=\delta(h(c))$$

    and since $\delta$ is injective, we know that $h(c)=0$. That is, $c\in\ker(h)=\im(g)$, so there exists some $b_0\in B$ such that $g(b_0)=c$. Now consider, in $B'$, the element $\beta(b_0)$:

    $$g'(\beta(b_0))=\gamma(g(b_0))=\gamma(c)=0$$

    so $\beta(b_0)\in\ker(g')=\im(f')$ holds. Therefore, there exists some $a'\in A'$ such that $f'(a')=\beta(b_0)$, and since $\alpha$ is surjective, there also exists $a\in A$ satisfying $\alpha(a)=a'$. Now let $b=b_0-f(a)$. Then

    $$g(b)=g(b_0-f(a))=g(b_0)-g(f(a))=g(b_0)=c$$

    holds. On the other hand, 

    $$\beta(b)=\beta(b_0-f(a))=\beta(b_0)-\beta(f(a))=\beta(b_0)-f'(\alpha(a))=\beta(b_0)-f'(a')=\beta(b_0)-\beta(b_0)=0$$

    so $b\in\ker(\beta)$, and since $\beta$ is injective, $b=0$. Therefore $c=g(b)=0$, and $\gamma$ is injective.
:::

The above proposition has the following two immediate corollaries.

::: Corollary 2 (The five lemma)
Suppose a commutative diagram whose rows are exact

{% diagram Math/Homological_Algebra/Diagram_Chasing-2.svg width="20.26em" alt="five_lemma" %}

is given. If $\alpha,\beta,\delta,\epsilon$ are all bijective, then $\gamma$ is also bijective.
:::

::: Corollary 3 (The short five lemma)
Suppose a commutative diagram whose rows are exact

{% diagram Math/Homological_Algebra/Diagram_Chasing-3.svg width="18.88em" alt="short_five_lemma" %}

is given. If $\alpha,\gamma$ are both injective, then $\beta$ is also injective, and if $\alpha,\gamma$ are both surjective, then $\beta$ is also surjective.
:::

## The Snake Lemma

In the remainder of this post, our main goal is to prove the snake lemma, and for this we need two lemmas.

::: Lemma 4
Suppose a commutative square

{% diagram Math/Homological_Algebra/Diagram_Chasing-4.svg width="6.22em" alt="induced_morphism" %}

is given. Then $\xi$ sends $\ker(h)$ to $\ker(h')$ and $\eta$ sends $\im(h)$ to $\im(h')$, and in particular the following maps

$$\xi^\sharp:\ker(h)\rightarrow\ker(h'),\quad \eta^\sharp:\im(h)\rightarrow\im(h'),\quad\xi^\ast:X/\ker(h)\rightarrow X'/\ker(h'),\quad \eta^\ast:\coker(h)\rightarrow\coker(h')$$

are well-defined.
:::
::: Proof
Consider the composition $\xi\circ i:\ker h\rightarrow X'$ of $i:\ker(h)\rightarrow X$ and $\xi$. Then

$$h'\circ(\xi\circ i)=(\eta\circ h)\circ i=\eta\circ 0=0$$

so by the universal property of the kernel, we know that there exists a unique $\xi^\sharp:\ker(h)\rightarrow\ker(h')$.

{% diagram Math/Homological_Algebra/Diagram_Chasing-5.svg width="13.20em" alt="induced_morphism_kernel" %}

Similarly, from $p'\circ\eta:Y\rightarrow \coker (h')$,

$$(p'\circ\eta)\circ h=p'\circ(h'\circ\xi)=(p'\circ h')\circ\xi=0\circ\xi=0$$

and we can define $\eta^\ast$ from the universal property of $\coker(h)$.

{% diagram Math/Homological_Algebra/Diagram_Chasing-6.svg width="14.23em" alt="induced_morphism_cokernel" %}

By definition $\coker(h)=Y/\im(h), \coker(h')=Y'/\im(h')$, so since $\eta^\ast$ sends $0$ to $0$, $\eta^\sharp$ is also well-defined. Finally, for $\xi^\ast$, if we consider $q:X'\rightarrow X'/\ker(h')$, then

$$\ker(h)\subseteq\ker(q\circ\xi)$$

and therefore $q\circ\xi$ induces $\xi^\ast:X/\ker(h)\rightarrow X'/\ker(h')$.
:::

Using this, we can prove the following lemma.

::: Lemma 5
Suppose a commutative diagram whose rows are exact

{% diagram Math/Homological_Algebra/Diagram_Chasing-7.svg width="10.84em" alt="induced_exact_sequence" %}

is given. Then $f,g$ and $f',g'$ respectively induce the following two sequences:

$$\ker(\alpha)\rightarrow\ker(\beta)\rightarrow\ker(\gamma),\qquad \coker(\alpha)\rightarrow\coker(\beta)\rightarrow\coker(\gamma)$$

Moreover, if $f':A'\rightarrow B'$ is injective then the first sequence is exact, and if $g:B\rightarrow C$ is surjective then the second sequence is exact.
:::
::: Proof
That $f,g$ and $f',g'$ respectively induce the two given sequences

$$\ker(\alpha)\overset{f^\sharp}{\rightarrow}\ker(\beta)\overset{g^\sharp}{\rightarrow}\ker(\gamma),\qquad \coker(\alpha)\overset{(f')^\ast}{\rightarrow}\coker(\beta)\overset{(g')^\ast}{\rightarrow}\coker(\gamma)$$

is a consequence of [Lemma 4](#lem4){: data-lid="yt1hi" }. Moreover, letting $i_A, i_B, i_C$ be the canonical maps from the kernels to $A,B,C$ respectively, we have

$$i_C\circ g^\sharp\circ f^\sharp=g\circ i_B\circ f^\sharp=g\circ f\circ i_A=0$$

and since $i_C$ is injective, we verify that $g^\sharp\circ f^\sharp=0$. Similarly, letting $p_A,p_B,p_C$ be the canonical maps from $A',B',C'$ to the cokernels respectively, we have

$$(g')^\ast\circ(f')^\ast\circ p_A=(g')^\ast\circ p_B\circ f'=p_C\circ g'\circ f'=0$$

and since $p_A$ is surjective, we verify that $(g')^\ast\circ(f')^\ast=0$. Therefore, to prove the statement it suffices to show that if $f':A'\rightarrow B'$ is injective then $\ker(g^\sharp)\subseteq\im(f^\sharp)$, and if $g:B\rightarrow C$ is surjective then $\ker((g')^\ast)\subseteq\im((f')^\ast)$.

First assume that $f'$ is injective. If $g^\sharp(b)=0$ for some $b\in\ker(\beta)$, then by the definition of $g^\sharp$ we have $g(b)=0$ and therefore $b\in\ker(g)=\im(f)$. Thus there exists some $a\in A$ such that $f(a)=b$. However, from

$$(f'\circ\alpha)(a)=(\beta\circ f)(a)=\beta(f(a))=\beta(b)=0$$

since $f'$ is injective we have $a\in\ker(\alpha)$, and from $f(a)=f^\sharp(a)=b$ we obtain $b\in\im(f^\sharp)$.

Now assume that $g$ is surjective. Let $b'\in\coker(\beta)$ be an element of $\ker((g')^\ast)$. That is, $((g')^\ast)(b')=g'(b')+\im(\gamma)=0$. Since $g'(b')\in\im(\gamma)$, there exists some $c\in C$ such that $\gamma(c)=g'(b')$, and since $g$ is surjective there exists some $b\in B$ such that $g(b)=c$. Then, since

$$g'(b')=\gamma(c)=(\gamma\circ g)(b)=(g'\circ\beta)(b)$$

we have $b'-\beta(b)\in\ker(g')=\im(f')$. Now choose $a'\in A'$ satisfying $f'(a')=b'-\beta(b)$. Then since $f'(a')-b'\in\im(\beta)$,

$$f'(a')+\im(\beta)=b'+\im(\beta)$$

and therefore

$$((f')^\ast)(a'+\im(\alpha))=b'+\im(\beta)$$

holds.
:::

Now we can finally prove the snake lemma.

::: Theorem 6 (The snake lemma)
Suppose a commutative diagram whose rows are exact

{% diagram Math/Homological_Algebra/Diagram_Chasing-8.svg width="18.88em" alt="snake_diagram" %}

is given. Here, the top and bottom rows are each exact. Then there exists $\delta:\ker(\gamma)\rightarrow\coker(\alpha)$ connecting the two exact sequences obtained from [Lemma 5](#lem5){: data-lid="ug6c6" }

$$\ker(\alpha)\rightarrow\ker(\beta)\rightarrow\ker(\gamma),\qquad \coker(\alpha)\rightarrow\coker(\beta)\rightarrow\coker(\gamma)$$

such that the following sequence, joined through it,

$$\ker(\alpha)\rightarrow\ker(\beta)\rightarrow\ker(\gamma)\rightarrow\coker(\alpha)\rightarrow\coker(\beta)\rightarrow\coker(\gamma)$$

forms an exact sequence. 
:::
::: Proof
To prove this, it suffices to construct $\delta$ and then show that the above sequence is exact at $\ker(\gamma)$ and $\coker(\alpha)$, respectively. 

First pick some $c\in\ker(\gamma)$. Since $g$ is surjective, there exists some $b\in B$ such that $g(b)=c$, and this $b$ satisfies the equation

$$0=\gamma(c)=\gamma(g(b))=(\gamma\circ g)(b)=(g'\circ\beta)(b)=g'(\beta(b))$$

That is, $\beta(b)\in\ker(g')=\im(f')$. Hence there exists a unique $a'$ such that $f'(a')=\beta(b)$. For this $a'$, set $\delta(c)=a'+\im(\alpha)\in \coker(\alpha)$. 

For the function $\delta$ to be well-defined, the above value must not depend on the choice of $b$. Pick another $b_1\in B$ satisfying $g(b_1)=c$, and in the same way pick $a_1'\in A'$ satisfying $f'(a_1')=\beta(b_1)$. Then 

$$g(b_1-b)=g(b_1)-g(b)=c-c=0$$

so $b_1-b\in\ker(g)=\im(f)$ holds. Now if we find $a\in A$ such that $f(a)=b_1-b$, then

$$f'(\alpha(a))=\beta(f(a))=\beta(b_1)-\beta(b)=f'(a_1'-a')$$

and since $f'$ is injective, $\alpha(a)=a_1'-a'$ holds. That is, $a_1'\equiv a' \mod{\im}(\alpha)$, and $\delta$ is well-defined. It is not difficult to show that $\delta$ is a homomorphism of $A$-modules.

We must show that $\delta$ constructed in this way makes the following sequence

$$\ker(\beta)\rightarrow\ker(\gamma)\rightarrow\coker(\alpha)\rightarrow\coker(\beta)$$ 

into an exact sequence. First let $b\in \ker(\beta)$. If we set $\delta(g^\sharp(b))=a'+\im(\alpha)$, then $a'$ is determined by the equation $f'(a')=\beta(b)$; since $b\in\ker(\beta)$, we have $f'(a')=0$, and since $f'$ is injective, we must have $a'=0$. That is, $\delta\circ g^\sharp=0$. Similarly, for any $c\in\ker(\gamma)$, if we set $\delta(c)=a'+\im(\alpha)$, then 

$$((f')^\ast)(a'+\im(\alpha))=f'(a')+\im(\beta)=\beta(b)+\im(\beta)=0$$

holds. Therefore, it suffices to show that $\ker(\delta)\subseteq\im(g^\sharp)$ and $\ker((f')^\ast)\subseteq\im(\delta)$.

First let $c\in\ker(\delta)$. Then $a'$ is defined, for $b$ satisfying $g(b)=c$, as the element satisfying the equation $f'(a')=\beta(b)$, so $a'\in\im(\alpha)$. Now pick $a\in A$ satisfying $\alpha(a)=a'$. Then

$$\beta(b)=f'(a')=f'(\alpha(a))=\beta(f(a))$$

so $b-f(a)\in\ker(\beta)$. Now

$$g^\sharp(b-f(a))=g(b-f(a))=g(b)-g(f(a))=g(b)=c$$

so $c\in\im g^\sharp$ holds. 

Similarly, let $a'\in\ker((f')^\ast)$. Then since $f'(a')\in\im(\beta)$, there exists some $b\in B$ such that $\beta(b)=f'(a')$, and for this $b$,

$$\gamma(g(b))=(g'\circ\beta)(b)=(g'\circ f')(a')=0$$

holds, so $g(b)\in\ker(\gamma)$. Therefore $\delta(g(b))$ is well-defined, and since $b$ was defined as precisely the element satisfying $f'(a')=\beta(b)$, this value equals exactly $a'+\im(\alpha)$.
:::

This theorem is called the snake lemma because when the connecting map $\delta$ is drawn, the following shape appears.

{% diagram Math/Homological_Algebra/Diagram_Chasing-9.svg width="27.46em" alt="connecting_map_of_snake_diagram" %}

The snake lemma is usually used to draw long exact sequences as in subsequent posts, but it also has the following other corollary.

::: Corollary 7 (The 3×3 lemma)
Consider a commutative diagram whose rows are exact:

{% diagram Math/Homological_Algebra/Diagram_Chasing-10.svg width="19.30em" alt="Nine_lemma" %}

If the first two columns are both short exact sequences, then the last column is also a short exact sequence, and if the last two columns are both short exact sequences, then the first column is also a short exact sequence.
:::

---

**References**

**[Hu]** S.T. Hu, *Introduction to homological algebra*. University Microfilms, 1979.
