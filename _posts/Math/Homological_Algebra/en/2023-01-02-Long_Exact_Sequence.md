---
title: "Long Exact Sequences"
description: "It covers the process by which a short exact sequence induces a long exact sequence between homologies, including a proof using the snake lemma and diagram chasing."
excerpt: "Long exact sequences"

categories: [Math / Homological Algebra]
permalink: /en/math/homological_algebra/long_exact_sequence
sidebar: 
    nav: "homological_algebra-en"

date: 2023-01-02
weight: 3
translated_at: 2026-08-27T15:15:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-10T23:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
We now show that a short exact sequence in $\Ch(\mathcal{A})$ induces a *long exact sequence*.

## Long exact sequences

We have seen earlier that the image and kernel of a chain map $f_\bullet$ form chain complexes consisting of the image and kernel of each $f_n$, respectively. Therefore, one can verify that saying

$$0\rightarrow A_\bullet\rightarrow B_\bullet\rightarrow C_\bullet\rightarrow 0$$

is a *short exact sequence* is equivalent to saying that for every $n$,

$$0\rightarrow A_n\rightarrow B_n\rightarrow C_n\rightarrow 0$$

is a short exact sequence.

The main theorem of this post is the following [Theorem 1](#thm1){: data-lid="8gqgm" }. Here, the snake lemma plays an important role in the proof, and since the proof can be easily completed using the connecting map explicitly obtained when the category is $\lMod{A}$, just as in [§Diagram chasing](/en/math/homological_algebra/diagram_chasing){: data-lid="2megj" }, we actively use the Freyd-Mitchell embedding theorem and proceed with the proof of the following theorem in $\lMod{A}$.

::: Theorem 1 (The long exact sequence)
Suppose that the following short exact sequence

$$0\rightarrow A_\bullet\rightarrow B_\bullet\rightarrow C_\bullet\rightarrow 0$$

is given. Then a *long exact sequence* between the homologies

$$\cdots\rightarrow H_n(A)\rightarrow H_n(B)\rightarrow H_n(C)\rightarrow H_{n-1}(A)\rightarrow \cdots$$

exists.
:::
::: Proof
For this, it suffices to consider the following diagram:

{% diagram Math/Homological_Algebra/Long_Exact_Sequence-1.svg width="32.84em" alt="long_exact_sequence" %}

Here, the maps $\partial$ are all defined as in $\partial^A(a+\im d^A_{n+1})=d_n^Aa\in\ker d^A_{n-1}$. Then one can easily verify that in the diagram above, $\ker\partial^A$ equals $H_n(A)=\ker d_n^A/\im(d^A_{n+1})$ and $\coker\partial^A$ equals $H_{n-1}(A)=\ker d^A_{n-1}/\im d^A_n$.

Therefore, if we only show that both the top and bottom rows are exact, the given long exact sequence is well induced by the snake lemma. To show this, consider again the following diagram:

{% diagram Math/Homological_Algebra/Long_Exact_Sequence-2.svg width="22.98em" alt="long_exact_sequence_exactness" %}

If we apply [§Diagram chasing, ⁋Lemma 5](/en/math/homological_algebra/diagram_chasing#lem5){: data-lid="plcik" } to this diagram, the two exact sequences

$$0\rightarrow \ker(d_n^A)\rightarrow \ker(d_n^B)\rightarrow \ker(d_n^C)$$

and

$$\coker(d_n^A)\rightarrow\coker(d_n^B)\rightarrow\coker(d_n^C)\rightarrow 0$$

are obtained. Here, the $0$ at each end comes, respectively, from the fact that since $A_n\rightarrow B_n$ is injective, the map $\ker(d_n^A)\rightarrow\ker(d_n^B)$ obtained by restricting it is also injective, and from the fact that since $B_{n-1}\rightarrow C_{n-1}$ is surjective, the map $\coker(d_n^B)\rightarrow\coker(d_n^C)$ that it induces is also surjective.
:::

The long exact sequence constructed above has functoriality in the following sense.

::: Proposition 2
Given a chain map between two short exact sequences

{% diagram Math/Homological_Algebra/Long_Exact_Sequence-3.svg width="19.34em" alt="morphism_in_SES" %}

there exists a chain map

{% diagram Math/Homological_Algebra/Long_Exact_Sequence-4.svg width="35.61em" alt="functoriality" %}

between the corresponding long exact sequences.
:::
::: Proof
Write the two short exact sequences as

$$0 \rightarrow A_\bullet\overset{u}{\rightarrow}B_\bullet\overset{v}{\rightarrow}C_\bullet \rightarrow 0,\qquad 0 \rightarrow A_\bullet'\overset{u'}{\rightarrow}B_\bullet'\overset{v'}{\rightarrow}C_\bullet' \rightarrow 0$$

and let the chain maps between them be $f:A_\bullet \rightarrow A_\bullet'$, $g:B_\bullet \rightarrow B_\bullet'$, $h:C_\bullet \rightarrow C_\bullet'$. That is, $u'f=gu$ and $v'g=hv$ hold.

In the diagram to be constructed, the squares not involving the connecting morphism $\partial$ commute immediately by the functoriality of homology. For instance,

$$H_n(g)\circ H_n(u)=H_n(gu)=H_n(u'f)=H_n(u')\circ H_n(f)$$

and likewise for the square involving $v$. Therefore it suffices to show that the following square

$$\begin{aligned}H_n(C)&\overset{\partial}{\longrightarrow} H_{n-1}(A)\\ H_n(h)\downarrow\quad&\qquad\quad\downarrow H_{n-1}(f)\\ H_n(C')&\overset{\partial'}{\longrightarrow}H_{n-1}(A')\end{aligned}$$

commutes. Following the construction in the proof of [Theorem 1](#thm1){: data-lid="aja6h" }, $\partial$ is computed as follows. For any $[c]\in H_n(C)$, since $v_n$ is surjective there exists $b\in B_n$ such that $v_n(b)=c$, and since $v_{n-1}(d_n^Bb)=d_n^Cv_n(b)=d_n^Cc=0$, by exactness there exists a unique $a\in A_{n-1}$ such that $u_{n-1}(a)=d_n^Bb$, and $\partial[c]=[a]$. One can also check that this value is independent of the choice of lift $b$: if $v_n(b)=v_n(\tilde{b})=c$, then there exists $\alpha\in A_n$ such that $b-\tilde{b}=u_n(\alpha)$, and the two corresponding elements $a,\tilde{a}$ then satisfy $u_{n-1}(a-\tilde{a})=d^B_n(b-\tilde{b})=u_{n-1}(d^A_n\alpha)$, so by the injectivity of $u_{n-1}$ we have $a-\tilde{a}=d_n^A\alpha$, whence $[a]=[\tilde{a}]$.

Now fix $[c]\in H_n(C)$ and the elements $b,a$ appearing in the construction above. Then we may take $g_n(b)$ as a lift of $h_n(c)\in C_n'$. Indeed,

$$v_n'(g_n(b))=h_n(v_n(b))=h_n(c)$$

Then, since

$$d_n^{B'}(g_n(b))=g_{n-1}(d_n^Bb)=g_{n-1}(u_{n-1}(a))=u_{n-1}'(f_{n-1}(a))$$

by the definition of $\partial'$, we have

$$\partial'[h_n(c)]=[f_{n-1}(a)]=H_{n-1}(f)(\partial[c])$$

That is, the square above commutes.
:::

## Quasi-isomorphic chain complexes

It is clear how one should define an isomorphism between the chain complexes we have considered so far.

::: Definition 3
Suppose two chain complexes $C_\bullet$, $D_\bullet$ are given. We say that $C_\bullet$ and $D_\bullet$ are *isomorphic* if there exist two chain maps $f:C_\bullet\rightarrow D_\bullet$, $g:D_\bullet\rightarrow C_\bullet$ such that $fg=\id_D$ and $gf=\id_C$. In this case, we call $f,g$ *isomorphisms* between the two chain complexes.
:::

This is equivalent to the existence of a chain map $(f_n)_{n\in\mathbb{Z}}$ in which each $f_n$ is an isomorphism.

On the other hand, since homology is the only tool available to us in homological algebra, we may weaken the notion of isomorphism as follows.

::: Definition 4
Two chain complexes $C_\bullet$, $D_\bullet$ are said to be *quasi-isomorphic* if there exists a chain map $f:C_\bullet\rightarrow D_\bullet$ such that $H_n(f)$ is an isomorphism for every $n$. In this case, $f$ is called a *quasi-isomorphism*.[^1]
:::

By definition, two isomorphic chain complexes are also quasi-isomorphic. The converse, however, does not hold. The only chain complex isomorphic to the sequence

$$\cdots\rightarrow 0\rightarrow 0\rightarrow 0\rightarrow\cdots$$

all of whose components are 0 is itself, but for any exact sequence $C_\bullet$, every homology module is 0, so the zero map $C_\bullet\rightarrow 0$ is a quasi-isomorphism.

## Chain homotopy

Meanwhile, if we weaken the equivalence relation between two chain complexes to quasi-isomorphism as above, then by the same logic it is somewhat more reasonable to also regard two chain maps as the same whenever they define the same maps on the respective homologies. To this end, we define the following.

::: Definition 5
Suppose two chain complexes $C,D$ and chain maps $f,g:C\rightarrow D$ are given. Then a *chain homotopy* between $f$ and $g$ is, in the diagram

{% diagram Math/Homological_Algebra/Long_Exact_Sequence-5.svg width="30.61em" alt="chain_homotopy" %}

such that $f_n-g_n=d_{n+1}^Dh_n+h_{n-1}d_n^C$ holds, a collection of $h_n:C_n\rightarrow D_{n+1}$. If a chain homotopy between $f,g$ exists, we call $f$ and $g$ *homotopic* chain maps.
:::

If for some chain map $f$, $f=\dd{h}+hd$ holds for some $h$, then $h$ can be regarded as a chain homotopy between $f$ and $0$. Therefore, when such an $h$ exists, we call $f$ *null homotopic*.

::: Proposition 6
Two homotopic chain maps $f,g:C\rightarrow D$ induce the same maps on homologies.
:::
::: Proof
Take any $[a]\in H_n(C)=\ker(d^C_{n})/\im(d^C_{n+1})$, and let $a\in\ker(d_{n}^C)$ be a representative. We must show that

$$f_n(a)-g_n(a)\in\im(d_{n+1}^D)$$

But from the identity

$$(d_{n+1}^D\circ h_n)(a)+(h_{n-1}\circ d_n^C)(a)=f_n(a)-g_n(a)$$

since $a\in \ker(d_n^C)$, we obtain

$$f_n(a)-g_n(a)=d_{n+1}^D(h_n(a))\in\im(d_{n+1}^D)$$
:::

If for some chain map $f:C\rightarrow D$ there exists a chain map $g:D\rightarrow C$ such that $gf$ is homotopic to $\id_C$ and $fg$ is homotopic to $\id_D$, then $f$ is called a *chain homotopy equivalence*.

## Homotopy category

Thanks to [Proposition 6](#prop6){: data-lid="fh6iy" }, we can define the *homotopy category* $\mathbf{K}(\mathcal{A})$ through the following procedure. First, the following lemma is immediate.

::: Lemma 7
The homotopy relation between two chain maps is an equivalence relation.
:::

This allows us to define an equivalence relation on $\Hom_{\Ch(\mathcal{A})}(C_\bullet,D_\bullet)$. Let us define $\Hom_{\mathbf{K}(\mathcal{A})}(C_\bullet,D_\bullet)$ to be the quotient set arising from this equivalence relation.

$\mathbf{K}(\mathcal{A})$ has the same objects as $\Ch(\mathcal{A})$, the set of morphisms between them is $\Hom_{\mathbf{K}(\mathcal{A})}$ defined as above, and one can check that this set has the structure of an abelian group.

Suppose two homotopic chain maps $f,g:C\rightarrow D$ are given. For any $u:B\rightarrow C$, $v:D\rightarrow E$, consider the two maps $vfu$ and $vgu$. Considering the following diagram

{% diagram Math/Homological_Algebra/Long_Exact_Sequence-6.svg width="30.61em" alt="composition_in_homotopy_category" %}

we have

$$\begin{aligned}v_nf_nu_n-v_ng_nu_n&=v_n(f_n-g_n)u_n\\&=v_n(d_{n+1}h_n+h_{n-1}d_n)u_n\\&=d_{n+1}v_{n+1}h_nu_n+v_nh_{n-1}u_{n-1}d_n\end{aligned}$$

so we know that between $vfu$ and $vgu$ a chain homotopy

$$(h'_n=v_{n+1}h_nu_n)_{n\in\mathbb{Z}}$$

exists. In other words, the equivalence relation defined above is also compatible with composition in $\Ch(\mathcal{A})$.

By similar reasoning, one can show that $\mathbf{K}(\mathcal{A})$ is an additive category, and the trivial functor $\Ch(\mathcal{A})\rightarrow\mathbf{K}(\mathcal{A})$ is an additive functor.

However, in general $\mathbf{K}(\mathcal{A})$ is not an abelian category.

## Mapping cone

In [Definition 4](#def4){: data-lid="pkm8l" }, we agreed to call chain complexes connected by a chain map inducing an isomorphism on homology quasi-isomorphic, and to treat them as the same. The mapping cone serves as a tool for determining whether a given chain map $f:C_\bullet \rightarrow D_\bullet$ is a quasi-isomorphism.

::: Definition 8
For any chain map $f:C_\bullet\rightarrow D_\bullet$, the *mapping cone* of $f$, $\Cone(f)$, is the following chain complex

$$\cdots\longrightarrow\underbrace{C_n\oplus D_{n+1}}_{\Cone(f)_{n+1}}\overset{d_{n+1}}{\longrightarrow}\underbrace{C_{n-1}\oplus D_n}_{\Cone(f)_n}\overset{d_n}{\longrightarrow}\underbrace{C_{n-2}\oplus D_{n-1}}_{\Cone(f)_{n-1}}\longrightarrow\cdots$$

Here, the differential is given by the formula

$$d_n(x,y)=(-d_{n-1}(x), d_n(y)-f_{n-1}(x))\qquad (x\in C_{n-1},y\in D_n)$$

:::

Suppose a chain map $f: C_\bullet \rightarrow D_\bullet$ is given, and for the mapping cone of $f$, $\Cone(f)$, consider the sequence of chain complexes

$$0 \longrightarrow D \longrightarrow \Cone(f) \overset{\delta}{\longrightarrow} C[-1] \longrightarrow0$$

Here, $D \rightarrow\Cone(f)$ sends $y$ to $(0,y)$, and $\delta$ sends $(x,y)$ to $-x$. Then, since it is immediate from the definitions of these maps that the sequence above is a short exact sequence, by [Theorem 1](#thm1){: data-lid="nxgqc" } there exists the following long exact sequence

$$\cdots \rightarrow H_{n+1}(\Cone(f)) \rightarrow H_n(C) \rightarrow H_n(D) \rightarrow H_n(\Cone(f)) \rightarrow H_{n-1}(C) \rightarrow \cdots$$

Meanwhile, a closer look at the proof of this theorem shows that the connecting maps $H_n(C) \rightarrow H_n(D)$ obtained above are precisely $H_n(f)$. Therefore, the following holds.

::: Corollary 9
A chain map $f: C_\bullet \rightarrow D_\bullet$ is a quasi-isomorphism if and only if $\Cone(f)$ is an exact sequence.
:::


---

**References**

**[Wei]** C.A. Weibel. *An Introduction to Homological Algebra*. Cambridge Studies in Advanced Mathematics. Cambridge University Press, 1995.

---

[^1]: The appropriate translation of the prefix quasi- seems to be *jun-* (준-), but in the case of quasi-isomorphism, since homomorphism already uses the translation *jun-donghyeong-sasang* (준동형사상), we had no choice but to newly adopt the term *yusa-donghyeong-sasang* (유사동형사상).
