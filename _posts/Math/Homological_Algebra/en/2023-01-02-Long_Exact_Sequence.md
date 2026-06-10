---
title: "The Long Exact Sequence"
description: "This post explains how a short exact sequence induces a long exact sequence in homology, including a proof using the snake lemma and diagram chasing."
excerpt: "The long exact sequence"

categories: [Math / Homological Algebra]
permalink: /en/math/homological_algebra/long_exact_sequence
sidebar: 
    nav: "homological_algebra-en"

date: 2023-01-02
last_modified_at: 2024-10-31
weight: 3
published: false
translated_at: 2026-05-31T13:00:06+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-31T13:00:06+00:00
---
Now we show that a short exact sequence in $$\Ch(\mathcal{A})$$ induces a *long exact sequence*. 

## The Long Exact Sequence

We have already seen that the image and kernel of a chain map $$f_\bullet$$ form chain complexes consisting of the images and kernels of each $$f_n$$, respectively. Therefore, one can verify that

$$0\rightarrow A_\bullet\rightarrow B_\bullet\rightarrow C_\bullet\rightarrow 0$$

is a *short exact sequence* if and only if

$$0\rightarrow A_n\rightarrow B_n\rightarrow C_n\rightarrow 0$$

is a short exact sequence for every $$n$$. 

The main theorem of this post is [Theorem 1](#thm1). In its proof the snake lemma plays an important role, and because the proof is easily completed using the explicitly obtained connecting map when the category is $$\lMod{A}$$, we actively use the Freyd–Mitchell embedding theorem to prove the following theorem in $$\lMod{A}$$, just as in [§Diagram chasing](/en/math/homological_algebra/diagram_chasing).

<div class="proposition" markdown="1">

<ins id="thm1">**Theorem 1 (The long exact sequence)**</ins> Given a short exact sequence

$$0\rightarrow A_\bullet\rightarrow B_\bullet\rightarrow C_\bullet\rightarrow 0$$

there exists a *long exact sequence* of homology groups

$$\cdots\rightarrow H_n(A)\rightarrow H_n(B)\rightarrow H_n(C)\rightarrow H_{n-1}(A)\rightarrow \cdots$$

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

It suffices to consider the following diagram:

![long_exact_sequence](/assets/images/Math/Homological_Algebra/Long_Exact_Sequence-1.png){:style="width:30em" class="invert" .align-center}

Here the maps $$\partial$$ are all defined by formulas such as $$\partial^A(a+\im d^A_{n+1})=d_n^Aa\in\ker d^A_{n-1}$$. Then one easily verifies that in the above diagram $$\ker\partial^A$$ coincides with $$H_{n+1}(A)=\ker d_n^A/\im(d^A_{n+1})$$ and $$\coker\partial^A$$ coincides with $$H_{n-1}(A)=\ker d^A_{n-1}/\im d^A_n$$. 

Therefore, once we show that the top and bottom rows are both exact, the desired long exact sequence follows readily from the snake lemma. To see this, consider again the following diagram:

![long_exact_sequence_exactness](/assets/images/Math/Homological_Algebra/Long_Exact_Sequence-2.png){:style="width:21.4em" class="invert" .align-center}

Applying the snake lemma once more to this diagram (more precisely, [§Diagram chasing, ⁋Lemma 5](/en/math/homological_algebra/diagram_chasing#lem5)), we obtain two exact sequences

$$0\rightarrow \ker(d_n^A)\rightarrow \ker(d_n^B)\rightarrow \ker(d_n^C)$$

and

$$\coker(d_n^A)\rightarrow\coker(d_n^B)\rightarrow\coker(d_n^C)\rightarrow 0$$

</details>

The long exact sequence constructed above enjoys functoriality in the following sense.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> Given a chain map between two short exact sequences

![morphism_in_SES](/assets/images/Math/Homological_Algebra/Long_Exact_Sequence-3.png){:style="width:18em" class="invert" .align-center}

there exists a corresponding chain map between the associated long exact sequences

![functoriality](/assets/images/Math/Homological_Algebra/Long_Exact_Sequence-4.png){:style="width:32em" class="invert" .align-center}

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>



</details>

## Quasi-Isomorphic Chain Complexes

How to define an isomorphism between the chain complexes we have examined so far is clear.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> Let two chain complexes $$C_\bullet$$, $$D_\bullet$$ be given. Then $$C_\bullet$$ and $$D_\bullet$$ are said to be *isomorphic* if there exist chain maps $$f:C_\bullet\rightarrow D_\bullet$$ and $$g:D_\bullet\rightarrow C_\bullet$$ such that $$fg=\id_D$$ and $$gf=\id_C$$. In this case we call $$f,g$$ *isomorphisms* between the two chain complexes.

</div>

This is equivalent to the existence of a chain map $$(f_n)_{n\in\mathbb{Z}}$$ in which each $$f_n$$ is an isomorphism.

On the other hand, since the only tool available to us in homological algebra is homology, we can weaken the notion of isomorphism as follows.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> Two chain complexes $$C_\bullet$$, $$D_\bullet$$ are *quasi-isomorphic* if $$H_n(C)\cong H_n(D)$$ for all $$n$$. If a chain map $$f:C\rightarrow D$$ is such that $$H_n(f)$$ is an isomorphism for every $$n$$, we call $$f$$ a *quasi-isomorphism*.[^1]

</div>

By definition, two isomorphic chain complexes are also quasi-isomorphic. However, the converse does not hold. The only chain complex isomorphic to the sequence

$$\cdots\rightarrow 0\rightarrow 0\rightarrow 0\rightarrow\cdots$$

with all terms zero is itself, yet any exact sequence always has all homology modules equal to zero.

## Chain Homotopy

Meanwhile, if we weaken the equivalence relation between two chain complexes to quasi-isomorphism as above, then by the same logic it would be somewhat more reasonable to regard two chain maps as the same whenever they induce the same map on each homology. For this purpose we make the following definition.

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> Let two chain complexes $$C,D$$ and chain maps $$f,g:C\rightarrow D$$ be given. Then a *chain homotopy* between $$f$$ and $$g$$ is a collection of maps $$h_n:C_n\rightarrow D_{n+1}$$ in the following diagram

![chain_homotopy](/assets/images/Math/Homological_Algebra/Long_Exact_Sequence-5.png){:style="width:28em" class="invert" .align-center}

satisfying $$f_n-g_n=d_{n+1}^Dh_n+h_{n-1}d_n^C$$. If a chain homotopy between $$f$$ and $$g$$ exists, we say that $$f$$ and $$g$$ are *homotopic* chain maps. 

</div>

If for a chain map $$f$$ there exists an $$h$$ satisfying $$f=dh+hd$$, we can regard $$h$$ as a chain homotopy between $$f$$ and $$0$$. Hence, if such an $$h$$ exists, we say that $$f$$ is *null homotopic*. 

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> Two homotopic chain maps $$f,g:C\rightarrow D$$ induce the same map on homology.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Choose an arbitrary $$[a]\in H_n(C)=\ker(d^C_{n})/\im(d^C_{n+1})$$, and let $$a\in\ker(d_{n}^C)$$ be a representative. We must show that

$$f_n(a)-g_n(a)\in\im(d_{n+1}^D)$$

holds. From the equation

$$(d_{n+1}^D\circ h_n)(a)+(h_{n-1}\circ d_n^C)(a)=f_n(a)-g_n(a)$$

and the fact that $$a\in \ker(d_n^C)$$, we obtain

$$f_n(a)-g_n(a)=d_{n+1}^D(h_n(a))\in\im(d_{n+1}^D)$$

</details>

If for a chain map $$f:C\rightarrow D$$ there exists a chain map $$g:D\rightarrow C$$ such that $$gf$$ is homotopic to $$\id_C$$ and $$fg$$ is homotopic to $$\id_D$$, we call $$f$$ a *chain homotopy equivalence*. 

## The Homotopy Category

Building on [Proposition 6](#prop6), we can define the *homotopy category* $$\mathbf{K}(\mathcal{C})$$ through the following process. First, the following lemma is obvious.

<div class="proposition" markdown="1">

<ins id="lem7">**Lemma 7**</ins> The homotopy relation between two chain maps is an equivalence relation.

</div>

Through this we can define an equivalence relation on $$\Hom_{\mathbf{Ch}(\mathcal{C})}(C_\bullet,D_\bullet)$$. Let us define the quotient set arising from this equivalence relation to be $$\Hom_{\mathbf{K}(\mathcal{C})}(C_\bullet,D_\bullet)$$. 

$$\mathbf{K}(\mathcal{C})$$ has the same objects as $$\mathbf{Ch}(\mathcal{C})$$, the sets of morphisms between them are the $$\Hom_{\mathbf{K}(\mathcal{C})}$$ defined as above, and one can check that these sets carry the structure of an abelian group. 

Let two homotopic chain maps $$f,g:C\rightarrow D$$ be given. For arbitrary $$u:B\rightarrow C$$ and $$v:D\rightarrow E$$, consider the two maps $$vfu$$ and $$vgu$$. Considering the diagram

![composition_in_homotopy_category](/assets/images/Math/Homological_Algebra/Long_Exact_Sequence-6.png){:style="width:28em" class="invert" .align-center}

we have

$$\begin{aligned}v_nf_nu_n-v_ng_nu_n&=v_n(f_n-g_n)u_n\\&=v_n(d_{n+1}h_n+h_{n-1}d_n)u_n\\&=d_{n+1}v_{n+1}h_nu_n+v_nh_{n-1}u_{n-1}d_n\end{aligned}$$

so that a chain homotopy

$$(h'_n=v_{n+1}h_nu_n)_{n\in\mathbb{Z}}$$

exists between $$vfu$$ and $$vgu$$. In other words, the equivalence relation defined above is also compatible with composition in $$\mathbf{Ch}(\mathcal{C})$$. 

By a similar argument one can show that $$\mathbf{K}(\mathcal{C})$$ is an additive category, and the obvious functor $$\mathbf{Ch}(\mathcal{C})\rightarrow\mathbf{K}(\mathcal{C})$$ is an additive functor. 

However, in general $$\mathbf{K}(\mathcal{C})$$ is not an abelian category.

## The Mapping Cone

In [Definition 4](#def4), we decided to call chain complexes having isomorphic homology quasi-isomorphic and to treat them as the same. The mapping cone is a tool for determining whether a given chain map $$f:C_\bullet \rightarrow D_\bullet$$ is a quasi-isomorphism.

<div class="definition" markdown="1">

<ins id="def8">**Definition 8**</ins> For any chain map $$f:C_\bullet\rightarrow D_\bullet$$, the *mapping cone* $$\cone(f)$$ of $$f$$ is the following chain complex:

$$\cdots\longrightarrow\underbrace{C_n\oplus D_{n+1}}_{\cone(f)_{n+1}}\overset{d_{n+1}}{\longrightarrow}\underbrace{C_{n-1}\oplus D_n}_{\cone(f)_n}\overset{d_n}{\longrightarrow}\underbrace{C_{n-2}\oplus D_{n-1}}_{\cone(f)_{n-1}}\longrightarrow\cdots$$

Here the differential is given by the formula

$$d_n(x,y)=(-d_{n-1}(x), d_n(y)-f_{n-1}(x))\qquad (x\in C_{n-1},y\in D_n)$$

</div>

Let a chain map $$f: C_\bullet \rightarrow D_\bullet$$ be given, and for its mapping cone $$\cone(f)$$, consider the sequence of chain complexes

$$0 \longrightarrow D \longrightarrow \cone(f) \overset{\delta}{\longrightarrow} C[-1] \longrightarrow0$$

Here $$D \rightarrow\cone(f)$$ sends $$y$$ to $$(0,y)$$, and $$\delta$$ sends $$(x,y)$$ to $$-x$$. Then it is obvious from the definitions of these maps that the above sequence is a short exact sequence, so by [Theorem 1](#thm1) the following long exact sequence

$$\cdots \rightarrow H_{n+1}(\cone(f)) \rightarrow H_n(B) \rightarrow H_n(C) \rightarrow H_n(\cone(f)) \rightarrow H_{n-1}(B) \rightarrow \cdots$$

exists. On the other hand, examining the proof of this theorem, one sees that the connecting maps $$H_n(B) \rightarrow H_n(C)$$ obtained above are exactly $$H_n(f)$$. Therefore the following holds.

<div class="proposition" markdown="1">

<ins id="cor9">**Corollary 9**</ins> A chain map $$f: C_\bullet \rightarrow D_\bullet$$ is a quasi-isomorphism if and only if $$\cone(f)$$ is exact. 

</div>


---

**References**

**[Wei]** C.A. Weibel. *An Introduction to Homological Algebra*. Cambridge Studies in Advanced Mathematics. Cambridge University Press, 1995.

---

[^1]: An appropriate translation of the prefix quasi- seems to be *jun-* (準-); however, since homomorphism is already translated as *jundonghyeongsasang* (準同型寫像), we had no choice but to coin the new term *yusadonghyeongsasang* (類似同型寫像) for quasi-isomorphism.
