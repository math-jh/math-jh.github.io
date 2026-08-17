---
title: "Long Exact Sequence"
description: "This post explains how a short exact sequence induces a long exact sequence in homology, including a proof using the snake lemma and diagram chasing."
excerpt: "Long exact sequence"

categories: [Math / Homological Algebra]
permalink: /en/math/homological_algebra/long_exact_sequence
sidebar: 
    nav: "homological_algebra-en"

date: 2023-01-02
weight: 3
revising: true
translated_at: 2026-07-14T00:00:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-07-14T00:00:02+00:00
---
Now we show that a short exact sequence in $\Ch(\mathcal{A})$ induces a *long exact sequence*.

## Long Exact Sequence

We have already seen that the image and kernel of a chain map $f_\bullet$ form chain complexes consisting of the images and kernels of each $f_n$, respectively. Therefore, the statement that

$$0\rightarrow A_\bullet\rightarrow B_\bullet\rightarrow C_\bullet\rightarrow 0$$

is a *short exact sequence* is equivalent to the statement that

$$0\rightarrow A_n\rightarrow B_n\rightarrow C_n\rightarrow 0$$

is a short exact sequence for all $n$.

The main theorem of this post is the following [Theorem 1](#thm1). In its proof, the snake lemma plays an important role, and since the proof can be completed easily by using the connecting map that is obtained explicitly when the category is $\lMod{A}$, we actively use the Freyd–Mitchell embedding theorem as in [§Diagram chasing](/en/math/homological_algebra/diagram_chasing) to carry out the proof of the following theorem in $\lMod{A}$.

::: Theorem 1 (The long exact sequence)
Given a short exact sequence

$$0\rightarrow A_\bullet\rightarrow B_\bullet\rightarrow C_\bullet\rightarrow 0$$

there exists a *long exact sequence* of homologies

$$\cdots\rightarrow H_n(A)\rightarrow H_n(B)\rightarrow H_n(C)\rightarrow H_{n-1}(A)\rightarrow \cdots$$
:::
::: Proof
It suffices to consider the following diagram

{% diagram Math/Homological_Algebra/Long_Exact_Sequence-1.svg width="32.84em" alt="long_exact_sequence" %}

Here, the $\partial$'s are all functions defined by $\partial^A(a+\im d^A_{n+1})=d_n^Aa\in\ker d^A_{n-1}$. Then in the above diagram, one can easily verify that $\ker\partial^A$ is equal to $H_{n+1}(A)=\ker d_n^A/\im(d^A_{n+1})$, and $\coker\partial^A$ is equal to $H_{n-1}(A)=\ker d^A_{n-1}/\im d^A_n$.

Therefore, it suffices to show that the top and bottom rows are exact; then the snake lemma yields the desired long exact sequence. To show this, consider again the following diagram

{% diagram Math/Homological_Algebra/Long_Exact_Sequence-2.svg width="22.98em" alt="long_exact_sequence_exactness" %}

Applying the snake lemma (more precisely, [§Diagram chasing, ⁋Lemma 5](/en/math/homological_algebra/diagram_chasing#lem5)) to this diagram once more, we obtain two exact sequences

$$0\rightarrow \ker(d_n^A)\rightarrow \ker(d_n^B)\rightarrow \ker(d_n^C)$$

and

$$\coker(d_n^A)\rightarrow\coker(d_n^B)\rightarrow\coker(d_n^C)\rightarrow 0$$
:::

The long exact sequence constructed above has functoriality in the following sense.

::: Proposition 2
Given a chain map between two short exact sequences

{% diagram Math/Homological_Algebra/Long_Exact_Sequence-3.svg width="19.34em" alt="morphism_in_SES" %}

there exists a chain map between the corresponding long exact sequences

{% diagram Math/Homological_Algebra/Long_Exact_Sequence-4.svg width="35.61em" alt="functoriality" %}
:::
::: Proof
Write the two short exact sequences as

$$0 \rightarrow A_\bullet\overset{u}{\rightarrow}B_\bullet\overset{v}{\rightarrow}C_\bullet \rightarrow 0,\qquad 0 \rightarrow A_\bullet'\overset{u'}{\rightarrow}B_\bullet'\overset{v'}{\rightarrow}C_\bullet' \rightarrow 0$$

and denote the chain maps between them by $f:A_\bullet \rightarrow A_\bullet'$, $g:B_\bullet \rightarrow B_\bullet'$, $h:C_\bullet \rightarrow C_\bullet'$. That is, $u'f=gu$ and $v'g=hv$ hold.

In the diagram we need to construct, the squares not containing the connecting morphism $\partial$ commute immediately by the functoriality of homology. For example,

$$H_n(g)\circ H_n(u)=H_n(gu)=H_n(u'f)=H_n(u')\circ H_n(f)$$

and the square on the $v$ side is the same. Therefore, it suffices to show that the following square

$$\begin{aligned}H_n(C)&\overset{\partial}{\longrightarrow} H_{n-1}(A)\\ H_n(h)\downarrow\quad&\qquad\quad\downarrow H_{n-1}(f)\\ H_n(C')&\overset{\partial'}{\longrightarrow}H_{n-1}(A')\end{aligned}$$

commutes. Following the construction in the proof of [Theorem 1](#thm1), $\partial$ is computed as follows. For arbitrary $[c]\in H_n(C)$, since $v_n$ is surjective, there exists $b\in B_n$ such that $v_n(b)=c$, and since $v_{n-1}(d_n^Bb)=d_n^Cv_n(b)=d_n^Cc=0$, by exactness there exists a unique $a\in A_{n-1}$ such that $u_{n-1}(a)=d_n^Bb$, and $\partial[c]=[a]$. One can also verify that this value is independent of the choice of lift $b$: if $v_n(b)=v_n(\tilde{b})=c$, then there exists $\alpha\in A_n$ such that $b-\tilde{b}=u_n(\alpha)$, and then the corresponding two elements $a,\tilde{a}$ satisfy $u_{n-1}(a-\tilde{a})=d^B_n(b-\tilde{b})=u_{n-1}(d^A_n\alpha)$, so by the injectivity of $u_{n-1}$ we have $a-\tilde{a}=d_n^A\alpha$, giving $[a]=[\tilde{a}]$.

Now fix $[c]\in H_n(C)$ and the $b,a$ appearing in the above construction. Then $g_n(b)$ can be chosen as a lift of $h_n(c)\in C_n'$. Indeed,

$$v_n'(g_n(b))=h_n(v_n(b))=h_n(c)$$

Then since

$$d_n^{B'}(g_n(b))=g_{n-1}(d_n^Bb)=g_{n-1}(u_{n-1}(a))=u_{n-1}'(f_{n-1}(a))$$

by the definition of $\partial'$, we have

$$\partial'[h_n(c)]=[f_{n-1}(a)]=H_{n-1}(f)(\partial[c])$$

That is, the above square commutes.
:::

## Quasi-Isomorphic Chain Complexes

It is clear how to define an isomorphism between the chain complexes we have examined so far.

::: Definition 3
Given two chain complexes $C_\bullet$, $D_\bullet$, we say that $C_\bullet$ and $D_\bullet$ are *isomorphic* if there exist two chain maps $f:C_\bullet\rightarrow D_\bullet$, $g:D_\bullet\rightarrow C_\bullet$ such that $fg=\id_D$ and $gf=\id_C$. In this case, we call $f,g$ *isomorphisms* between the two chain complexes.
:::

This is equivalent to the existence of a chain map $(f_n)_{n\in\mathbb{Z}}$ such that each $f_n$ is an isomorphism.

On the other hand, since the only tool we have available in homological algebra is homology, we can weaken the notion of isomorphism as follows.

::: Definition 4
Two chain complexes $C_\bullet$, $D_\bullet$ are *quasi-isomorphic* if $H_n(C)\cong H_n(D)$ for all $n$. If a chain map $f:C\rightarrow D$ is such that $H_n(f)$ is an isomorphism for all $n$, we call $f$ a *quasi-isomorphism*.[^1]
:::

By definition, two isomorphic chain complexes are also quasi-isomorphic. However, the converse does not hold. A chain complex isomorphic to the sequence with all terms zero

$$\cdots\rightarrow 0\rightarrow 0\rightarrow 0\rightarrow\cdots$$

is only itself, but any exact sequence always has all homology modules equal to zero.

## Chain Homotopy

On the other hand, if we weaken the equivalence relation between two chain complexes to quasi-isomorphism as above, then by the same logic it would be somewhat more reasonable to also treat two chain maps as the same if they define the same function on each homology. For this purpose, we define the following.

::: Definition 5
Given two chain complexes $C,D$ and chain maps $f,g:C\rightarrow D$, a *chain homotopy* between $f$ and $g$ is a collection of $h_n:C_n\rightarrow D_{n+1}$ in the following diagram

{% diagram Math/Homological_Algebra/Long_Exact_Sequence-5.svg width="30.61em" alt="chain_homotopy" %}

such that $f_n-g_n=d_{n+1}^Dh_n+h_{n-1}d_n^C$ holds. If a chain homotopy between $f,g$ exists, we say that $f$ and $g$ are *homotopic* chain maps.
:::

If for a chain map $f$, there exists $h$ satisfying $f=\dd{h}+hd$, then $h$ can be viewed as a chain homotopy between $f$ and $0$. Therefore, when such an $h$ exists, we call $f$ *null-homotopic*.

::: Proposition 6
Two homotopic chain maps $f,g:C\rightarrow D$ induce the same function on homologies.
:::
::: Proof
Choose arbitrary $[a]\in H_n(C)=\ker(d^C_{n})/\im(d^C_{n+1})$ and let $a\in\ker(d_{n}^C)$ be a representative. We need to show

$$f_n(a)-g_n(a)\in\im(d_{n+1}^D)$$

However, from the equation

$$(d_{n+1}^D\circ h_n)(a)+(h_{n-1}\circ d_n^C)(a)=f_n(a)-g_n(a)$$

since $a\in \ker(d_n^C)$, we obtain

$$f_n(a)-g_n(a)=d_{n+1}^D(h_n(a))\in\im(d_{n+1}^D)$$
:::

If for a chain map $f:C\rightarrow D$, there exists a chain map $g:D\rightarrow C$ such that $gf$ is homotopic to $\id_C$ and $fg$ is homotopic to $\id_D$, we call $f$ a *chain homotopy equivalence*.

## Homotopy Category

Relying on [Proposition 6](#prop6), we can define the *homotopy category* $\mathbf{K}(\mathcal{C})$ through the following process. First, the following lemma is trivial.

::: Lemma 7
The homotopy relation between two chain maps is an equivalence relation.
:::

Through this, we can define an equivalence relation on $\Hom_{\mathbf{Ch}(\mathcal{C})}(C_\bullet,D_\bullet)$. Let the quotient set obtained by this equivalence relation be $\Hom_{\mathbf{K}(\mathcal{C})}(C_\bullet,D_\bullet)$.

$\mathbf{K}(\mathcal{C})$ has the same objects as $\mathbf{Ch}(\mathcal{C})$, the set of morphisms between them is the $\Hom_{\mathbf{K}(\mathcal{C})}$ defined above, and one can verify that this set has the structure of an abelian group.

Given two homotopic chain maps $f,g:C\rightarrow D$, consider the two maps $vfu$ and $vgu$ for arbitrary $u:B\rightarrow C$, $v:D\rightarrow E$. Considering the following diagram

{% diagram Math/Homological_Algebra/Long_Exact_Sequence-6.svg width="30.61em" alt="composition_in_homotopy_category" %}

we have

$$\begin{aligned}v_nf_nu_n-v_ng_nu_n&=v_n(f_n-g_n)u_n\\&=v_n(d_{n+1}h_n+h_{n-1}d_n)u_n\\&=d_{n+1}v_{n+1}h_nu_n+v_nh_{n-1}u_{n-1}d_n\end{aligned}$$

so we know that a chain homotopy

$$(h'_n=v_{n+1}h_nu_n)_{n\in\mathbb{Z}}$$

exists between $vfu$ and $vgu$. That is, the equivalence relation defined above is also compatible with composition in $\mathbf{Ch}(\mathcal{C})$.

By similar logic, one can show that $\mathbf{K}(\mathcal{C})$ is an additive category, and the obvious functor $\mathbf{Ch}(\mathcal{C})\rightarrow\mathbf{K}(\mathcal{C})$ is an additive functor.

However, in general $\mathbf{K}(\mathcal{C})$ is not an abelian category.

## Mapping Cone

In [Definition 4](#def4), we called chain complexes with isomorphic homology quasi-isomorphic and decided to treat them as the same. The mapping cone is a tool for determining whether a given chain map $f:C_\bullet \rightarrow D_\bullet$ is a quasi-isomorphism.

::: Definition 8
For any chain map $f:C_\bullet\rightarrow D_\bullet$, the *mapping cone* $\Cone(f)$ of $f$ is the following chain complex

$$\cdots\longrightarrow\underbrace{C_n\oplus D_{n+1}}_{\Cone(f)_{n+1}}\overset{d_{n+1}}{\longrightarrow}\underbrace{C_{n-1}\oplus D_n}_{\Cone(f)_n}\overset{d_n}{\longrightarrow}\underbrace{C_{n-2}\oplus D_{n-1}}_{\Cone(f)_{n-1}}\longrightarrow\cdots$$

Here, the differential is given by the formula

$$d_n(x,y)=(-d_{n-1}(x), d_n(y)-f_{n-1}(x))\qquad (x\in C_{n-1},y\in D_n)$$
:::

Given a chain map $f: C_\bullet \rightarrow D_\bullet$ and its mapping cone $\Cone(f)$, consider the sequence of chain complexes

$$0 \longrightarrow D \longrightarrow \Cone(f) \overset{\delta}{\longrightarrow} C[-1] \longrightarrow0$$

Here, $D \rightarrow\Cone(f)$ sends $y$ to $(0,y)$, and $\delta$ sends $(x,y)$ to $-x$. Then by the definitions of these functions, it is trivial that the above sequence is a short exact sequence, so by [Theorem 1](#thm1) the following long exact sequence exists

$$\cdots \rightarrow H_{n+1}(\Cone(f)) \rightarrow H_n(B) \rightarrow H_n(C) \rightarrow H_n(\Cone(f)) \rightarrow H_{n-1}(B) \rightarrow \cdots$$

On the other hand, examining the proof of this theorem, one can see that the connecting maps $H_n(B) \rightarrow H_n(C)$ obtained above are exactly $H_n(f)$. Therefore, the following holds.

::: Corollary 9
A chain map $f: C_\bullet \rightarrow D_\bullet$ is a quasi-isomorphism if and only if $\Cone(f)$ is an exact sequence.
:::


---

**References**

**[Wei]** C.A. Weibel. *An Introduction to Homological Algebra*. Cambridge Studies in Advanced Mathematics. Cambridge University Press, 1995.

---

[^1]: The appropriate translation of the prefix quasi- appears to be 준- (jun-), but since quasi-isomorphism is already translated as 준동형사상 (quasi-isomorphism), we had no choice but to newly use the name 유사동형사상 (quasi-isomorphism).
