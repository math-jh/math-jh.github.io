---
title: "Affine Scheme"
description: "We construct the affine scheme by defining the structure sheaf on the spectrum of a ring, and cover the definition of locally ringed spaces and their morphisms."
excerpt: "Affine scheme defined by the structure sheaf on a ring's spectrum"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/affine_schemes
sidebar: 
    nav: "scheme_theory-en"

date: 2025-01-27
weight: 3
translated_at: 2026-07-26T21:15:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-27T11:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
The most basic example of a sheaf defined on a topological space is the collection of continuous functions defined on a topological space, and $\mathcal{O}_{\Spec A}$, which we will define, is also similar; the difference is that we consider *regular functions* instead of continuous functions.

## Locally ringed space

Basically, sheaves defined on topological spaces were already treated in [\[Topology\] §Sheaves](/en/math/topology/sheaves){: data-lid="nfbwj" }, but the definition in that post is somewhat insufficient to describe the structure sheaf to be defined on $\Spec A$.

::: Definition 1
For a topological space $X$ and a $\cRing$-valued sheaf $\mathcal{O}_X$ defined on it, the pair $(X,\mathcal{O}_X)$ is called a *ringed space*. If, for any point in $X$, $x$, the stalk at $x$, $\mathcal{O}_{X,x}$, is always a local ring, this pair $(X, \mathcal{O}_X)$ is called a *locally ringed space*.
:::

Our claim is that on $\Spec A$, we can define a suitable structure sheaf $\mathcal{O}_{\Spec A}$ to make $(\Spec A, \mathcal{O}_{\Spec A})$ a locally ringed space, and that $\Spec$ defined in this way has functoriality such as [§The Spectrum, ⁋Proposition 2](/en/math/scheme_theory/spectrums#prop2){: data-lid="kx3vx" } or [§The Spectrum, ⁋Proposition 8](/en/math/scheme_theory/spectrums#prop8){: data-lid="mf87q" }. To write this mathematically, we must first define morphisms between locally ringed spaces.

::: Definition 2
For two ringed spaces $(X, \mathcal{O}_X)$ and $(Y, \mathcal{O}_Y)$, a morphism between them means a pair consisting of a continuous map $\varphi:X \rightarrow Y$ and a morphism in $\Sh(Y;\cRing)$, $\varphi^\sharp:\mathcal{O}_Y \rightarrow \varphi_\ast \mathcal{O}_X$.

A morphism between two locally ringed spaces $(X, \mathcal{O}_X)$ and $(Y, \mathcal{O}_Y)$ is a morphism $(\varphi,\varphi^\sharp)$ of ringed spaces that additionally induces, for each $x\in X$, a local homomorphism $\varphi_x^\sharp:\mathcal{O}_{Y,\varphi(x)} \rightarrow \mathcal{O}_{X,x}$.
:::

## Algebraic functions defined on $\Spec A$

Now we must define $\mathcal{O}_{\Spec A}$. As mentioned at the beginning of this post, this is the sheaf of algebraic functions defined on $\Spec A$, and it is precisely the generalization of [\[Algebraic Varieties\] §Affine Varieties, ⁋Definition 14](/en/math/algebraic_varieties/affine_varieties#def14){: data-lid="4ahr9" }.

Let us generalize this discussion to schemes. First, as in algebraic varieties, we think of an element of $A$ as a function $f$. Then the *function value* of $f$ at the point $\mathfrak{p}\in\Spec A$ is the image under the canonical projection $\pi: A \rightarrow A/\mathfrak{p}$ of $f$. Then, in particular, for $f$ at the point $\mathfrak{p}$ to become $0$ means

$$f\equiv 0\pmod{\mathfrak{p}}\iff f\in \mathfrak{p}\iff \mathfrak{p}\in Z(f)$$

That is, $Z(f)$ can be understood as the collection of points where $f=0$, and its complement, the principal open set $D(f)$, can be understood as the collection of points where $f\neq 0$.

From this perspective, we can describe what the *algebraic functions* on $\Spec A$ are. Just as in [\[Algebraic Varieties\] §Affine Varieties, ⁋Definition 14](/en/math/algebraic_varieties/affine_varieties#def14){: data-lid="41xe6" }, they can be defined as functions that appear, on a suitable neighborhood of each point, in the form of a rational function having as denominator a function that does not become $0$ on that neighborhood. Here, one must be careful that this condition is local. A single fractional expression having the entire open set as its domain does not exist in general, and this is guaranteed only on principal open sets, on which the definition is actually given below.

Now suppose a principal open set $D(f)$ is given. Then, if we consider only functions that appear on the whole of $D(f)$ in the form of a single rational function $g/h$, the functions $h$ that can go into the denominator must satisfy $D(f)\subseteq D(h)$.

::: Lemma 3
For a fixed element $f\in A$, define

$$S(f)=\{h\in A\mid D(f)\subseteq D(h)\}$$

Then $S(f)$ is a multiplicative subset of $A$.
:::
::: Proof
First, since $D(1)=\Spec A$, it is obvious that $S(f)$ contains the empty product $1$. Now if $h_1,h_2\in S(f)$, then from the following identity

$$D(h_1h_2)=\Spec A\setminus Z(h_1h_2)=\Spec A\setminus (Z(h_1)\cup Z(h_2))=(\Spec A\setminus Z(h_1))\cap (\Spec A\setminus Z(h_2))=D(h_1)\cap D(h_2)$$

we see that $D(f)\subseteq D(h_1)\cap D(h_2)=D(h_1h_2)$. This identity is merely a geometric explanation of [\[Algebraic Structures\] §Field of Fractions, ⁋Proposition 9](/en/math/algebraic_structures/field_of_fractions#prop9){: data-lid="n70o8" }.
:::

Now, it is intuitive that the collection of algebraic functions defined on the subset $D(f)$ of $\Spec A$ should be defined as $S(f)^{-1}A$, and indeed we will define it so. Before that, we prove the following lemma.

::: Lemma 4
$D(f)\subseteq D(h)$ holds if and only if there exists some $n\geq 1$ such that $f^n\in (h)$.
:::
::: Proof
$D(f)\subseteq D(h)$ is equivalent to $Z(h)\subseteq Z(f)$, which by the third result of [§The Spectrum, ⁋Lemma 6](/en/math/scheme_theory/spectrums#lem6){: data-lid="7dsjh" } is equivalent to $\sqrt{(f)}\subseteq \sqrt{(h)}$.

If $\sqrt{(f)}\subseteq \sqrt{(h)}$, then from $(f)\subseteq \sqrt{(f)}\subseteq \sqrt{(h)}$ we have $f\in \sqrt{(h)}$, and therefore we see that there must exist some $n\geq 1$ such that $f^n\in (h)$. Conversely, if there exists some $n\geq 1$ such that $f^n\in (h)$, then from $f\in \sqrt{(h)}$ we have $(f)\subseteq \sqrt{(h)}$, and therefore

$$\sqrt{(f)}\subseteq\sqrt{\sqrt{(h)}}=\sqrt{(h)}$$

holds.
:::

Using this lemma, we can express $S(f)^{-1}A$ in a cleaner form.

::: Lemma 5
For any $f\in A$, there exists an isomorphism

$$S(f)^{-1}A\cong S_f^{-1}A$$

Moreover, if $S(g)\subseteq S(f)$, then the following diagram

{% diagram frozen/a212f2a0/Math/Scheme_Theory/Affine_Schemes-1.svg width="10.55em" alt="localizations" %}

commutes.
:::
::: Proof
First, let us denote the canonical morphisms by $\epsilon(f): A \rightarrow S(f)^{-1}A$ and $\epsilon_f:A \rightarrow S_f^{-1}A$. Then, since $D(f)=D(f^n)$ for any $n\geq 1$, we have $S_f\subseteq S(f)$, and thus the image of $S_f$ under $\epsilon(f)$ consists entirely of units in $S(f)^{-1}A$. Conversely, for any $h\in S(f)$, by [Lemma 4](#lem4){: data-lid="t5nbv" } there exist $n\geq 1$ and $a\in A$ satisfying $f^n=ah$, so

$$\frac{h}{1}\frac{a}{f^n}=1\qquad\text{in $S_f^{-1}A$}$$

that is, the image of $S(f)$ under $\epsilon_f$ also consists entirely of units in $S_f^{-1}A$. Therefore, by [\[Commutative Algebra\] §Localization, ⁋Proposition 6](/en/math/commutative_algebra/localization#prop6){: data-lid="9ix75" }, there exist unique morphisms

$$\overline{\epsilon_f}: S(f)^{-1}A \rightarrow S_f^{-1}A,\qquad \overline{\epsilon(f)}: S_f^{-1}A \rightarrow S(f)^{-1}A$$

satisfying $\overline{\epsilon_f}\circ\epsilon(f)=\epsilon_f$ and $\overline{\epsilon(f)}\circ\epsilon_f=\epsilon(f)$, respectively. Then the two composites $\overline{\epsilon(f)}\circ\overline{\epsilon_f}$ and $\overline{\epsilon_f}\circ\overline{\epsilon(f)}$ extend $\epsilon(f)$ and $\epsilon_f$ respectively, so by the same uniqueness they are identity morphisms. That is, they are inverses of each other, and from this we obtain the claimed isomorphism.

Now suppose $S(g)\subseteq S(f)$. Then the elements of $S(g)$ are sent to units by both $\epsilon(f)$ and $\epsilon_f$, and since $S_g\subseteq S(g)$, again by [\[Commutative Algebra\] §Localization, ⁋Proposition 6](/en/math/commutative_algebra/localization#prop6){: data-lid="55ksa" } there exist unique morphisms

$$\widehat{\epsilon(f)}:S(g)^{-1}A \rightarrow S(f)^{-1}A,\qquad \widecheck{\epsilon_f}: S_g^{-1}A \rightarrow S_f^{-1}A$$

extending $\epsilon(f)$ and $\epsilon_f$ respectively, and these are the remaining two arrows of the claimed diagram. Now, both composites $\widecheck{\epsilon_f}\circ\overline{\epsilon_g}$ and $\overline{\epsilon_f}\circ\widehat{\epsilon(f)}$ yield $\epsilon_f$ when composed with $\epsilon(g)$, so by the same uniqueness they are equal.
:::

Thus, it suffices to regard algebraic functions defined on $D(f)$ as elements of $S_f^{-1}A$. In the previous post, we agreed to denote $S_f^{-1}A$ by $A_f$ for convenience.

::: Lemma 6
For $\Spec A$'s base $\{D(f)\}_{f\in A}$, define for each $f_i\in A$

$$\mathcal{F}(D(f_i))=S(f_i)^{-1}A\cong A_{f_i}$$

Also, for each $D(f_i)\subseteq D(f_j)$ with $f_i,f_j\in A$, define the restriction map

$$\rho_{ji}: S(f_j)^{-1}(A) \rightarrow S(f_i)^{-1}(A)$$

to be the map obtained by applying [\[Commutative Algebra\] §Localization, ⁋Proposition 6](/en/math/commutative_algebra/localization#prop6){: data-lid="d07gs" } to the canonical morphism $A\rightarrow S(f_i)^{-1}(A)$. Then these data satisfy the two conditions of [\[Topology\] §Sheaves, ⁋Proposition 8](/en/math/topology/sheaves#prop8){: data-lid="9nr9b" }, and therefore, extending $\mathcal{F}$ to $\Spec A$, a ($\cRing$-valued) sheaf is uniquely determined.
:::
::: Proof
That the $\rho_{ji}$ satisfy the conditions for restriction maps in [\[Topology\] §Presheaves, ⁋Definition 2](/en/math/topology/presheaves#def2){: data-lid="eau97" } is immediate from the universal property of [\[Commutative Algebra\] §Localization, ⁋Proposition 6](/en/math/commutative_algebra/localization#prop6){: data-lid="v37eh" }. Here, $\rho_{ji}: S(f_j)^{-1}(A) \rightarrow S(f_i)^{-1}(A)$ is, by [Lemma 5](#lem5){: data-lid="wi211" }, simply the function such that, when an element of $S(f_j)^{-1}(A)$ is expressed in the form

$$g/h,\qquad\text{where $h\in S(f_j)$}\tag{$\ast$}$$

since from the relation

$$h\in S(f_j)\iff D(f_j)\subseteq D(h)\implies D(f_i)\subseteq D(h)\iff h\in S(f_i)$$

one can view ($\ast$) also as an element of $S(f_i)^{-1}(A)$, it understands $g/h\in S(f_j)^{-1}(A)$ as $g/h\in S(f_i)^{-1}(A)$ through this process.

Now we prove the two conditions of [\[Topology\] §Sheaves, ⁋Proposition 8](/en/math/topology/sheaves#prop8){: data-lid="8efth" }. For convenience of notation, since $D(f)=\Spec A_f$, once we replace $A$ by $A_f$, it suffices to consider only the case $f=1$. Let us fix elements satisfying $\Spec A=\bigcup_{i\in I}D(f_i)$ with $f_i\in A$.

First, to show the first condition, suppose that an element $s\in A$ satisfies, for all $i\in I$, in $S(f_i)^{-1}A$ that $s=0$, and let us show that $s$ as an element of $A$ is also $0$. Then by [§The Spectrum, ⁋Lemma 12](/en/math/scheme_theory/spectrums#lem12){: data-lid="hd72n" }, among the elements of $(f_i)$, so that $\Spec A=\bigcup_{i=1}^n D(f_i)$, we can choose $f_1,\ldots, f_n$, and by assumption, for all $i=1,\ldots, n$, the equation

$$f_i^{m_i}s=0$$

holds for some $m_i\geq 1$. Meanwhile, from the calculation following [§The Spectrum, ⁋Lemma 11](/en/math/scheme_theory/spectrums#lem11){: data-lid="5yrs3" }, $D(f_i^{m_i})=D(f_i)$ holds for all $i$, so

$$\Spec A=\bigcup_{i=1}^n D(f_i^{m_i})$$

and from this, so that $1=\sum_{i=1}^n a_i f_i^{m_i}$, there exist $a_i\in A$. (cf. the proof of [§The Spectrum, ⁋Lemma 12](/en/math/scheme_theory/spectrums#lem12){: data-lid="fhjd3" }, or the proof of [\[Commutative Algebra\] §Integral Extensions, ⁋Proposition 15](/en/math/commutative_algebra/integral_extension#prop15){: data-lid="hiwg5" })

Therefore,

$$s=1s=\left(\sum_{i=1}^n a_i f_i^{m_i}\right)s=\sum_{i=1}^n a_i (f_i^{m_i}s)=0$$

Now to show the second condition, for each $i$ there exists in $S(f_i)^{-1}A$ an element $s_i=a_i/f_i^{m_i}$ such that for each $i,j$

$$\frac{a_i}{f_i^{m_i}}=\frac{a_j}{f_j^{m_j}}\quad\text{ in $D(f_i)\cap D(f_j)=D(f_if_j)$}$$

we may assume this holds. Here, since $a/1=af_i/f_i$, for all $i$ we can choose $m_i\geq 1$. However, since $D(f_i)=D(f_i^{m_i})$ and $D(f_j)=D(f_j^{m_j})$,

$$D(f_if_j)=D(f_i)\cap D(f_j)=D(f_i^{m_i})\cap D(f_j^{m_j})=D(f_i^{m_i}f_j^{m_j})$$

and therefore there exists suitable $N_{ij}$ such that

$$(f_i^{m_i}f_j^{m_j})^{N_{ij}}(a_if_j^{m_j}-a_jf_i^{m_i})=0$$

can be made to hold. Letting $N=\max_{i,j}\{N_{ij}\}$, we obtain

$$(f_i^{m_i}f_j^{m_j})^N(a_if_j^{m_j}-a_jf_i^{m_i})=0$$

that is,

$$a_if_i^{Nm_i}f_j^{Nm_j+m_j}=a_jf_j^{Nm_j}f_i^{Nm_i+m_i}$$

Then from the given assumption

$$\Spec A=\bigcup_{i=1}^n D(f_i)=\bigcup_{i=1}^n D(f_i^{Nm_i+m_i})$$

there exist suitable $b_i\in A$ such that

$$1=\sum_{i=1}^n b_if_i^{Nm_i+m_i}$$

Now if we set $s=\sum_{i=1}^n b_ia_i f_i^{Nm_i}$, then

$$sf_j^{Nm_j+m_j}=\sum_{i=1}^n b_ia_i f_i^{Nm_i} f_j^{Nm_j+m_j}=\sum_{i=1}^nb_ia_jf_j^{Nm_j}f_i^{Nm_i+m_i}=a_jf_j^{Nm_j}$$

so $f_j^{Nm_j}(sf_j^{m_j}-a_j)=0$ holds for all $j$, and therefore on $D(f_j)$

$$\frac{s}{1}=\frac{a_j}{f_j^{m_j}}$$

holds. From this, we obtain the desired $s$.

If $I$ is an infinite set, we can choose, so that $\Spec A=\bigcup_{j\in J} D(f_j)$, a finite subset of $I$, $J=\{1,\ldots, n\}$, and repeat the above to obtain $s\in \mathcal{F}(\Spec A)$; then it suffices to show that, for $\alpha\in I\setminus J$, on $D(f_\alpha)$ this also satisfies $s_\alpha=s\vert_{D(f_\alpha)}$. To show this, let us repeat the same process for the finite set

$$J\cup\{\alpha\}=\{1,2,\ldots, n,\alpha\}\subseteq I$$

as well, to obtain $s'\in \mathcal{F}(\Spec A)$. Then by definition, $s$ and $s'$ satisfy, for each $i=1,\ldots, n$, $s\vert_{D(f_i)}=s'\vert_{D(f_i)}$, and since $\Spec A=\bigcup D(f_i)$, by the first condition of [\[Topology\] §Sheaves, ⁋Proposition 8](/en/math/topology/sheaves#prop8){: data-lid="rx8mf" } shown above we know that $s=s'$, and from this we see that

$$s\vert_{D(f_\alpha)}=s'\vert_{D(f_\alpha)}=s_\alpha$$

holds. Since this holds for all $\alpha$, $s$, even when restricted to any $D(f_\alpha)$, gives $s_\alpha$.
:::

::: Definition 7
The sheaf on $\Spec A$ defined by [Lemma 6](#lem6){: data-lid="064f0" } is denoted $\mathcal{O}_{\Spec A}$ and called the *structure sheaf*.
:::

Although this definition was made only on principal open sets, since the $D(f)$ form a base for $\Spec A$, sections over an arbitrary open set $U$ are determined by the extension in [\[Topology\] §Sheaves, ⁋Proposition 8](/en/math/topology/sheaves#prop8){: data-lid="inrtd" }. That is, an element of $\mathcal{O}_{\Spec A}(U)$ is data given on a cover of $U$ by $D(f)$ in the form $g/h$ that agree on intersections, which corresponds to the local definition mentioned earlier.

Then $(\Spec A,\mathcal{O}_{\Spec A})$ is a locally ringed space.

::: Lemma 8
For $(\Spec A,\mathcal{O}_{\Spec A})$ and any point $\mathfrak{p}\in \Spec A$, there is an isomorphism

$$A_\mathfrak{p}\cong \mathcal{O}_{\Spec A, \mathfrak{p}}=\varinjlim_\text{\scriptsize $U\ni\mathfrak{p}$ open} \mathcal{O}_{\Spec A}(U)$$

Moreover, whenever $\mathfrak{p}\in D(f)$ for $f\in A$, the following diagram

{% diagram Math/Scheme_Theory/Affine_Schemes-7.svg width="14.55em" alt="stalk_and_localization-1" %}

commutes.
:::
::: Proof
By [§The Spectrum, ⁋Lemma 11](/en/math/scheme_theory/spectrums#lem11){: data-lid="3zwgs" }, the $D(f)$ form a base for $\Spec A$, so by [\[Topology\] §Bases of a Topological Space, ⁋Proposition 5](/en/math/topology/topological_bases#prop5){: data-lid="lcqaz" },

$$\mathcal{O}_{\Spec A, \mathfrak{p}}=\varinjlim_{D(f)\ni\mathfrak{p}} \mathcal{O}_{\Spec A}(D(f))$$

holds. On the other hand, since $\mathfrak{p}\in D(f)\iff f\not\in \mathfrak{p}$, we obtain the following diagram

{% diagram frozen/a212f2a0/Math/Scheme_Theory/Affine_Schemes-8.svg width="37.01em" alt="stalk_and_localization-2" %}

and thus showing the given isomorphism is simply equivalent to showing the following algebraic isomorphism

$$A_\mathfrak{p}\cong \varinjlim_{\mathfrak{p}\not\ni f} A_f\tag{$\ast\ast$}$$

which follows by using the universal property of [\[Commutative Algebra\] §Localization, ⁋Proposition 6](/en/math/commutative_algebra/localization#prop6){: data-lid="shjal" } and the universal property of direct limits, respectively. The diagram in the claim is obtained via the isomorphism ($\ast\ast$) by replacing $\varinjlim A_f$ with $A_\mathfrak{p}$ in the above diagram.
:::

We are now finally ready to write the functoriality of $\Spec$ in the form we want.

::: Proposition 9
The correspondence $A\mapsto (\Spec A, \mathcal{O}_{\Spec A})$ defines a functor $\Spec: \cRing^\op \rightarrow \LRS$. 
:::
::: Proof
We already know that a ring homomorphism $\phi: A \rightarrow B$ induces a continuous map $\Spec\phi: \Spec B \rightarrow \Spec A$. ([§The Spectrum, ⁋Proposition 8](/en/math/scheme_theory/spectrums#prop8){: data-lid="wnb7c" }) Thus it suffices to describe

$$(\Spec\phi)^\sharp: \mathcal{O}_{\Spec A} \rightarrow (\Spec\phi)_\ast \mathcal{O}_{\Spec B}$$

For this, it suffices to look at the maps on principal open sets

$$(\Spec\phi)^\sharp(D(f)): \mathcal{O}_{\Spec A}(D(f)) \rightarrow \mathcal{O}_{\Spec B}((\Spec \phi)^{-1}(D(f)))$$

Meanwhile, from the proof of [§The Spectrum, ⁋Proposition 8](/en/math/scheme_theory/spectrums#prop8){: data-lid="d9l8s" }, since

$$(\Spec\phi)^{-1}(Z(f))=Z(\phi(f))$$

we know that

$$(\Spec\phi)^{-1}(D(f))=D(\phi(f))$$

Therefore, by the definition of the structure sheaf, defining $(\Spec\phi)^\sharp(D(f))$ is equivalent to defining

$$A_f \rightarrow B_{\phi(f)}$$

and this is obtained by applying [\[Commutative Algebra\] §Localization, ⁋Proposition 6](/en/math/commutative_algebra/localization#prop6){: data-lid="0yy23" } to the composite

$$A \overset{\phi}{\rightarrow}B \overset{\epsilon}{\rightarrow} B_{\phi(f)}$$

Of course, we must show that the maps defined in this way commute with restriction maps. If $D(g)\subseteq D(f)$, then $D(\phi(g))\subseteq D(\phi(f))$, and since the two composites

$$A_f \rightarrow B_{\phi(f)} \rightarrow B_{\phi(g)},\qquad A_f \rightarrow A_g \rightarrow B_{\phi(g)}$$

both become $A \rightarrow B \rightarrow B_{\phi(g)}$ when composed with $\epsilon_f$, they are equal by the uniqueness above.

Now for an arbitrary open set $U\subseteq \Spec A$ and $s\in \mathcal{O}_{\Spec A}(U)$, consider the sections $(\Spec\phi)^\sharp(D(f))(s\vert_{D(f)})$ for each principal open set $D(f)$ contained in $U$. Since the intersection $D(f)\cap D(g)=D(fg)$ of two principal open sets is also a principal open set, these sections agree on intersections by the commutativity above, and therefore, by the gluability axiom and identity axiom of the sheaf $(\Spec\phi)_\ast\mathcal{O}_{\Spec B}$, they glue to a unique $(\Spec\phi)^\sharp(U)(s)$. That $(\Spec\phi)^\sharp(U)$ defined in this way is a ring homomorphism and commutes with restriction maps also follows from the identity axiom, and thus we obtain the sheaf morphism $(\Spec\phi)^\sharp$.

From the above, we know that $(\Spec\phi, (\Spec\phi)^\sharp): (\Spec B, \mathcal{O}_{\Spec B}) \rightarrow (\Spec A, \mathcal{O}_{\Spec A})$ is a morphism of ringed spaces. Now, to show that this is a morphism of locally ringed spaces, it suffices that for any $\mathfrak{q}\in \Spec B$,

$$(\Spec\phi)^\sharp_\mathfrak{q}:\mathcal{O}_{\Spec A, (\Spec \phi)(\mathfrak{q})} \rightarrow\mathcal{O}_{\Spec B, \mathfrak{q}}$$

be a local homomorphism. However, $(\Spec \phi)(\mathfrak{q})=\phi^{-1}(\mathfrak{q})$, and therefore by [Lemma 8](#lem8){: data-lid="qqe3t" }, $(\Spec\phi)^\sharp_\mathfrak{q}$ is a ring homomorphism from $A_{\phi^{-1}(\mathfrak{q})}$ to $B_{\mathfrak{q}}$, which sends the unique maximal ideal $\phi^{-1}(\mathfrak{q})A_{\phi^{-1}(\mathfrak{q})}$ of $A_{\phi^{-1}(\mathfrak{q})}$ to the unique maximal ideal $\mathfrak{q}B_\mathfrak{q}$ of $B_\mathfrak{q}$.

Finally, let us verify functoriality. Since the map on points was already checked in [§The Spectrum, ⁋Proposition 2](/en/math/scheme_theory/spectrums#prop2){: data-lid="fsfe4" }, we only need to look at the structure sheaf side. When $\phi=\id_A$, the above construction gives, for each $D(f)$, the unique map $A_f \rightarrow A_f$ extending $\epsilon_f$, which is the identity map; hence $\Spec(\id_A)=\id$. Also, for two ring homomorphisms $\phi: A \rightarrow B$ and $\psi: B \rightarrow C$, the map $\Spec(\psi\circ\phi)^\sharp(D(f))$ is the unique map extending the composite $A \rightarrow C \rightarrow C_{\psi(\phi(f))}$, and the composite $A_f \rightarrow B_{\phi(f)} \rightarrow C_{\psi(\phi(f))}$ also extends the same map, so by uniqueness the two are equal. Since the two sheaf morphisms agree on a base, $\Spec(\psi\circ\phi)=(\Spec\phi)\circ(\Spec\psi)$.
:::

## Affine Schemes

::: Definition 10
The essential image of the functor $\Spec:\cRing^\op \rightarrow \LRS$ from [Proposition 9](#prop9){: data-lid="82zvo" } is defined to be an *affine scheme*.
:::

We write $\AffSch$ for the category of affine schemes. Then the functor $\Spec:\cRing^\op \rightarrow \AffSch$ is essentially surjective by definition. ([\[Category Theory\] §Natural Transformations, ⁋Theorem 5](/en/math/category_theory/natural_transformations#thm5){: data-lid="f2mpz" }) Moreover, if $(\varphi, \varphi^\sharp): (\Spec B, \mathcal{O}_{\Spec B}) \rightarrow (\Spec A, \mathcal{O}_{\Spec A})$ is induced from some ring homomorphism $\phi$, then taking $1=f\in A$ in the proof of [Proposition 9](#prop9){: data-lid="wrxu6" } gives

$$\varphi^\sharp(D(1))= \bigl(A \overset{\phi}{\rightarrow} B \overset{\id_B}{\rightarrow} B_{\phi(1)}=B\bigr)=\phi$$

so this functor is necessarily faithful. Furthermore, the following holds.

::: Proposition 11
The functor $\Spec: \cRing^\op \rightarrow \LRS$ is fully faithful.
:::
::: Proof
 Suppose given any two affine schemes $(X, \mathcal{O}_{X})$, $(Y, \mathcal{O}_{Y})$ and a morphism

$$(X, \mathcal{O}_{X}) \rightarrow (Y, \mathcal{O}_{Y})$$

between them. Via isomorphisms $(\Spec B, \mathcal{O}_{\Spec B})\cong (X, \mathcal{O}_X)$ and $(\Spec A, \mathcal{O}_{\Spec A})\cong (Y, \mathcal{O}_Y)$, we can view this as a morphism

$$(\varphi, \varphi^\sharp): (\Spec B, \mathcal{O}_{\Spec B}) \rightarrow (\Spec A, \mathcal{O}_{\Spec A})$$

between the two spectra (as locally ringed spaces). Thus it suffices to prove that this morphism between locally ringed spaces comes from some ring homomorphism $\phi$. Taking a hint from the proof above that $\Spec$ is faithful, if we define via

$$\phi=\varphi^\sharp(D(1)):A \rightarrow B$$

the ring homomorphism $\phi:A \rightarrow B$, then to complete the claim we must show that $\Spec\phi=(\varphi,\varphi^\sharp)$. First, for any $\mathfrak{q}\in \Spec B$, let us show that

$$(\Spec \phi)(\mathfrak{q})=\phi^{-1}(\mathfrak{q})=\varphi(\mathfrak{q})$$

Setting $f=1$ in [Lemma 8](#lem8){: data-lid="e4iwn" }, we obtain the following diagram

{% diagram frozen/a212f2a0/Math/Scheme_Theory/Affine_Schemes-9.svg width="39.41em" alt="faithful" %}

In this diagram, the vertical maps are all isomorphisms, and we know that all faces except the following one

{% diagram Math/Scheme_Theory/Affine_Schemes-10.svg width="13.26em" alt="commuting_square" %}

are commuting squares. Therefore, in the above diagram $A \rightarrow \mathcal{O}_{\Spec B, \mathfrak{q}}$ is determined identically no matter which map we follow, and applying [\[Commutative Algebra\] §Localization, ⁋Proposition 6](/en/math/commutative_algebra/localization#prop6){: data-lid="pd03f" } to this map determines $A_{\varphi(\mathfrak{q})} \rightarrow \mathcal{O}_{\Spec B, \mathfrak{q}}$ uniquely. From this we see that *all* faces of the above diagram are commuting squares. That is, $\phi_\mathfrak{q}:A_{\varphi(\mathfrak{q})}\rightarrow B_\mathfrak{q}$ is also a local homomorphism, and hence $\phi^{-1}(\mathfrak{q})=\varphi(\mathfrak{q})$.

Now let us show that the two sheaf morphisms are equal. Since $\varphi^\sharp$ commutes with the restriction maps, for any $f\in A$,

$$\varphi^\sharp(D(f))\circ\epsilon_f=\epsilon_{\phi(f)}\circ\phi$$

holds. But in the construction of [Proposition 9](#prop9){: data-lid="o2pn8" }, $(\Spec\phi)^\sharp(D(f))$ was precisely the unique morphism satisfying this equation, so by the uniqueness in [\[Commutative Algebra\] §Localization, ⁋Proposition 6](/en/math/commutative_algebra/localization#prop6){: data-lid="xz6we" }, $\varphi^\sharp(D(f))=(\Spec\phi)^\sharp(D(f))$. Since the two sheaf morphisms agree on the base $\{D(f)\}_{f\in A}$, by the identity axiom of $\varphi_\ast\mathcal{O}_{\Spec B}$ we have $\varphi^\sharp=(\Spec\phi)^\sharp$.
:::

Therefore, viewing $\Spec$ as a contravariant functor from $\cRing$ to $\AffSch$, $\Spec$ is a categorical equivalence between the two categories $\cRing^\op$ and $\AffSch$. Moreover, by [Proposition 11](#prop11){: data-lid="55ndo" }, $\AffSch$ is a full subcategory of $\LRS$.

On the other hand, for any spectrum $(\Spec A, \mathcal{O}_{\Spec A})$, by definition we know that

$$\mathcal{O}_{\Spec A}(\Spec A)=\mathcal{O}_{\Spec A}(D(1))\cong A$$

If a locally ringed space $(X, \mathcal{O}_X)$ is an affine scheme, in a similar manner we can examine $\mathcal{O}_X(X)$ to see which ring's spectrum $(X, \mathcal{O}_X)$ is isomorphic to. That is, for an affine scheme $(X, \mathcal{O}_X)$, setting $A=\mathcal{O}_X(X)$ yields $(X, \mathcal{O}_X)\cong (\Spec A, \mathcal{O}_{\Spec A})$. More generally, we define the following.

::: Definition 12
The *global section functor* $\Gamma:\LRS \rightarrow \cRing^\op$ is defined, for any locally ringed space $(X, \mathcal{O}_X)$, by the correspondence

$$X\mapsto \Gamma(X, \mathcal{O}_X)=\mathcal{O}_X(X)$$

and for any morphism $(\varphi,\varphi^\sharp):(X,\mathcal{O}_X) \rightarrow (Y, \mathcal{O}_Y)$, by

$$\Gamma(\varphi,\varphi^\sharp)=\varphi^\sharp(Y):\Gamma(Y, \mathcal{O}_Y) \rightarrow (\varphi_\ast\mathcal{O}_X)(Y)=\Gamma(X, \mathcal{O}_X)$$

[^1]
:::

Here, $\varphi^\sharp(Y)$ is a morphism in $\cRing$ from $\Gamma(Y)$ to $\Gamma(X)$, so we can read this as a morphism in $\cRing^\op$, $\Gamma(X) \rightarrow \Gamma(Y)$. That this correspondence preserves identities and composition follows from the fact that composition of morphisms between ringed spaces is given by composition of the $\varphi^\sharp$, so this is indeed a functor.

Meanwhile, a notable fact from the proof of [Proposition 11](#prop11){: data-lid="efulx" } is that the assumption that $(X, \mathcal{O}_X)$ is an affine scheme is not needed. That is, even if we drop the assumption $(X, \mathcal{O}_X)\cong(\Spec B, \mathcal{O}_{\Spec B})$ and use the following diagram instead of the diagram in [Proposition 11](#prop11){: data-lid="fxs17" }

{% diagram frozen/a212f2a0/Math/Scheme_Theory/Affine_Schemes-11.svg width="34.92em" alt="adjoint" %}

we can carry out a similar argument, in which case $B$ in the conclusion is replaced by $\Gamma(X, \mathcal{O}_X)$. Since $\mathcal{O}_X$ is data determined by $X$ anyway, if we simply denote this by $\Gamma(X)$, from this we obtain the following theorem.

::: Theorem 13
For any locally ringed space $(X, \mathcal{O}_X)$ and any ring $A$, there exists a natural isomorphism

$$\Hom_\LRS(X, \Spec A)\cong \Hom_{\cRing^\op}(\Gamma(X), A)=\Hom_{\cRing}(A, \Gamma(X))$$

That is, the global section functor $\Gamma: \LRS \rightarrow \cRing^\op$ is the left adjoint of the $\Spec$ functor $\Spec:\cRing^\op \rightarrow \LRS$.
:::
::: Proof
Through the isomorphism $\mathcal{O}_{\Spec A}(D(f))\cong A_f$ from [Lemma 6](#lem6){: data-lid="vfvy9" }, let us identify $\mathcal{O}_{\Spec A}(\Spec A)=\mathcal{O}_{\Spec A}(D(1))$ with $A$. Under this identification, the restriction map $\mathcal{O}_{\Spec A}(\Spec A) \rightarrow \mathcal{O}_{\Spec A}(D(f))$ of $\mathcal{O}_{\Spec A}$ is the canonical morphism $\epsilon_f: A \rightarrow A_f$.

We first define two correspondences $\Phi$ and $\Psi$, and then show that they are inverses of each other. Given a morphism $(\varphi,\varphi^\sharp): X \rightarrow \Spec A$ of locally ringed spaces, evaluating $\varphi^\sharp$ on the open set $\Spec A$ yields the ring homomorphism

$$\Phi(\varphi,\varphi^\sharp)=\varphi^\sharp(\Spec A): A=\mathcal{O}_{\Spec A}(\Spec A) \rightarrow (\varphi_\ast\mathcal{O}_X)(\Spec A)=\mathcal{O}_X(X)=\Gamma(X)$$

Conversely, suppose a ring homomorphism $\phi:A \rightarrow \Gamma(X)$ is given. For each $x\in X$, write $\phi_x:A \rightarrow \mathcal{O}_{X,x}$ for the ring homomorphism obtained by composing $\phi$ with the germ map $\Gamma(X) \rightarrow \mathcal{O}_{X,x}$. That is, $\phi_x(a)=\phi(a)_x$. Since $(X,\mathcal{O}_X)$ is a locally ringed space, $\mathcal{O}_{X,x}$ is a local ring with a unique maximal ideal $\mathfrak{m}_x$, and hence by [\[Algebraic Structures\] §Field of Fractions, ⁋Proposition 10](/en/math/algebraic_structures/field_of_fractions#prop10){: data-lid="qr14d" },

$$\varphi(x)=\phi_x^{-1}(\mathfrak{m}_x)$$

is a prime ideal of $A$, that is, a point of $\Spec A$.

We show that the function $\varphi: X \rightarrow \Spec A$ defined in this way is continuous. For this, we show that for any $s\in \Gamma(X)$,

$$X_s=\{x\in X\mid \text{$s_x\not\in \mathfrak{m}_x$}\}$$

is an open set of $X$. By [\[Commutative Algebra\] §Localization, ⁋Proposition 2](/en/math/commutative_algebra/localization#prop2){: data-lid="59mji" }, since $\mathfrak{m}_x$ consists of all non-units of the local ring $\mathcal{O}_{X,x}$, $x\in X_s$ is equivalent to $s_x$ being a unit in $\mathcal{O}_{X,x}$. Now if $x\in X_s$, there exists $t\in \mathcal{O}_{X,x}$ satisfying $s_xt=1$, and choosing a suitable open neighborhood $W$ of $x$ and a section $u\in \mathcal{O}_X(W)$ representing $t$, we have $(s\vert_Wu)_x=1_x$, so by shrinking $W$ if necessary we can ensure that $s\vert_Wu=1$ in $\mathcal{O}_X(W)$. Then for any $y\in W$, $s_yu_y=1$, so $s_y$ is a unit in $\mathcal{O}_{X,y}$, and hence $W\subseteq X_s$. That is, $X_s$ is an open set.

On the other hand, for any $f\in A$,

$$\varphi^{-1}(D(f))=\{x\in X\mid f\not\in \varphi(x)\}=\{x\in X\mid \phi(f)_x\not\in \mathfrak{m}_x\}=X_{\phi(f)}$$

and since principal open sets form a base for $\Spec A$ ([§The Spectrum, ⁋Lemma 11](/en/math/scheme_theory/spectrums#lem11){: data-lid="mo5td" }), $\varphi$ is a continuous function.

Now we define the sheaf morphism $\varphi^\sharp: \mathcal{O}_{\Spec A} \rightarrow \varphi_\ast \mathcal{O}_X$. For each $f\in A$, let $V_f=\varphi^{-1}(D(f))=X_{\phi(f)}$, and write

$$\theta_f: A\overset{\phi}{\rightarrow} \Gamma(X) \rightarrow \mathcal{O}_X(V_f)$$

for the ring homomorphism obtained by composing $\phi$ with the restriction map. Our claim is that $\theta_f(f)=\phi(f)\vert_{V_f}$ is a unit in $\mathcal{O}_X(V_f)$. Indeed, by the definition of $V_f$, for every $y\in V_f$ the element $\phi(f)_y$ is a unit in $\mathcal{O}_{X,y}$, so repeating the argument above, there exist an open neighborhood $W_y\subseteq V_f$ of $y$ and $u_y\in \mathcal{O}_X(W_y)$ such that $\phi(f)\vert_{W_y}u_y=1$. Then on the intersection $W_y\cap W_{y'}$, the restrictions of $u_y$ and $u_{y'}$ are both multiplicative inverses of $\phi(f)\vert_{W_y\cap W_{y'}}$ and hence are equal; thus by the gluability axiom of [\[Topology\] §Sheaves, ⁋Definition 1](/en/math/topology/sheaves#def1){: data-lid="j9udf" }, they glue to a single $u\in \mathcal{O}_X(V_f)$. Now, restricting $\phi(f)\vert_{V_f}u$ and $1$ to each $W_y$ gives the same element, so by the identity axiom, $\phi(f)\vert_{V_f}u=1$.

In particular, $\theta_f$ sends all elements of the multiplicative subset $S_f=\{1,f,f^2,\ldots\}$ to units in $\mathcal{O}_X(V_f)$, so by [\[Commutative Algebra\] §Localization, ⁋Proposition 6](/en/math/commutative_algebra/localization#prop6){: data-lid="4fab2" }, there exists, satisfying

$$\varphi^\sharp(D(f))\circ \epsilon_f=\theta_f$$

a unique ring homomorphism

$$\varphi^\sharp(D(f)): A_f=\mathcal{O}_{\Spec A}(D(f)) \rightarrow \mathcal{O}_X(V_f)=(\varphi_\ast\mathcal{O}_X)(D(f))$$

If $D(g)\subseteq D(f)$, then $V_g\subseteq V_f$, and the two composites

$$A_f \overset{\varphi^\sharp(D(f))}{\rightarrow} \mathcal{O}_X(V_f) \rightarrow \mathcal{O}_X(V_g),\qquad A_f \rightarrow A_g \overset{\varphi^\sharp(D(g))}{\rightarrow} \mathcal{O}_X(V_g)$$

both become $\theta_g$ when composed with $\epsilon_f$, so again by the uniqueness in [\[Commutative Algebra\] §Localization, ⁋Proposition 6](/en/math/commutative_algebra/localization#prop6){: data-lid="s39f6" }, they are equal. That is, the $\varphi^\sharp(D(f))$ commute with restriction maps.

Then, just as in the proof of [Proposition 9](#prop9){: data-lid="3y1cc" }, the morphisms thus given on the base extend uniquely to a sheaf morphism $\varphi^\sharp$ by the gluability axiom and identity axiom of $\varphi_\ast\mathcal{O}_X$.

Finally, we show that $(\varphi,\varphi^\sharp)$ is a morphism of locally ringed spaces. For any $x\in X$ and $\mathfrak{p}=\varphi(x)$, by [Lemma 8](#lem8){: data-lid="mmdq8" } we have $\mathcal{O}_{\Spec A,\mathfrak{p}}\cong A_\mathfrak{p}$, and under this identification, taking the germ at $x$ of both sides of the equation $\varphi^\sharp(D(f))\circ\epsilon_f=\theta_f$ shows that the morphism $\varphi_x^\sharp: A_\mathfrak{p} \rightarrow \mathcal{O}_{X,x}$ between stalks induced by $\varphi^\sharp$ satisfies

$$\varphi^\sharp_x\circ\epsilon=\phi_x$$

where $\epsilon: A \rightarrow A_\mathfrak{p}$ is the canonical morphism. Now for any $a/s\in A_\mathfrak{p}$, since $s\not\in \mathfrak{p}=\phi_x^{-1}(\mathfrak{m}_x)$, the element $\phi_x(s)$ is a unit, and hence

$$\varphi_x^\sharp(a/s)=\phi_x(a)\phi_x(s)^{-1}$$

holds. In particular, if $a\in \mathfrak{p}$, then $\phi_x(a)\in \mathfrak{m}_x$, so $\varphi_x^\sharp(a/s)\in \mathfrak{m}_x$, which means that the ideal $(\varphi_x^\sharp)^{-1}(\mathfrak{m}_x)$ contains $\mathfrak{p}A_\mathfrak{p}$. On the other hand, since $\varphi_x^\sharp(1)=1\not\in \mathfrak{m}_x$, this ideal is not all of $A_\mathfrak{p}$, and since $\mathfrak{p}A_\mathfrak{p}$ is the unique maximal ideal of $A_\mathfrak{p}$ ([\[Commutative Algebra\] §Localization, ⁋Proposition 8](/en/math/commutative_algebra/localization#prop8){: data-lid="x2tn3" }),

$$(\varphi_x^\sharp)^{-1}(\mathfrak{m}_x)=\mathfrak{p}A_\mathfrak{p}$$

That is, $\varphi_x^\sharp$ is a local homomorphism, and by [Definition 2](#def2){: data-lid="silke" }, $\Psi(\phi)=(\varphi,\varphi^\sharp)$ is a morphism of locally ringed spaces.

Now we show that $\Phi$ and $\Psi$ are inverses of each other. First, for $\Psi(\phi)=(\varphi,\varphi^\sharp)$, setting $f=1$ gives $D(1)=\Spec A$, $V_1=X$, and $\epsilon_1=\id_A$, so the above construction yields

$$\Phi(\Psi(\phi))=\varphi^\sharp(\Spec A)=\theta_1=\phi$$

Conversely, suppose a morphism $(\varphi,\varphi^\sharp): X \rightarrow \Spec A$ of locally ringed spaces is given, and let $\phi=\Phi(\varphi,\varphi^\sharp)=\varphi^\sharp(\Spec A)$ and $\Psi(\phi)=(\varphi',(\varphi')^\sharp)$. For any $x\in X$, since $\varphi^\sharp$ commutes with restriction maps, the morphism $\varphi_x^\sharp: \mathcal{O}_{\Spec A, \varphi(x)}\cong A_{\varphi(x)} \rightarrow \mathcal{O}_{X,x}$ between stalks induced by $\varphi^\sharp$ satisfies $\varphi_x^\sharp\circ\epsilon=\phi_x$, where the fact that $\epsilon: A \rightarrow A_{\varphi(x)}$ is the canonical morphism follows from [Lemma 8](#lem8){: data-lid="f2l8g" }. On the other hand, since $(\varphi,\varphi^\sharp)$ is a morphism of locally ringed spaces, $\varphi_x^\sharp$ is a local homomorphism, so the ideal $(\varphi_x^\sharp)^{-1}(\mathfrak{m}_x)$ is a proper ideal containing $\varphi(x)A_{\varphi(x)}$, that is, $\varphi(x)A_{\varphi(x)}$ itself. Therefore, by [\[Commutative Algebra\] §Localization, ⁋Proposition 8](/en/math/commutative_algebra/localization#prop8){: data-lid="uv4h8" },

$$\varphi'(x)=\phi_x^{-1}(\mathfrak{m}_x)=\epsilon^{-1}\left((\varphi_x^\sharp)^{-1}(\mathfrak{m}_x)\right)=\epsilon^{-1}\left(\varphi(x)A_{\varphi(x)}\right)=\varphi(x)$$

and the two continuous functions $\varphi$ and $\varphi'$ are equal. Now since $\varphi^\sharp$ commutes with restriction maps, for any $f\in A$,

$$\varphi^\sharp(D(f))\circ\epsilon_f=\theta_f$$

holds, and since this is precisely the equation defining $(\varphi')^\sharp(D(f))$, by the uniqueness in [\[Commutative Algebra\] §Localization, ⁋Proposition 6](/en/math/commutative_algebra/localization#prop6){: data-lid="ilk73" }, we have $\varphi^\sharp(D(f))=(\varphi')^\sharp(D(f))$. Since the two sheaf morphisms agree on the base $\{D(f)\}_{f\in A}$, by the identity axiom of $\varphi_\ast\mathcal{O}_X$ we have $\varphi^\sharp=(\varphi')^\sharp$, and therefore $\Psi(\Phi(\varphi,\varphi^\sharp))=(\varphi,\varphi^\sharp)$.

Finally, we verify that this bijection is natural. Given a morphism $\psi: X' \rightarrow X$ of locally ringed spaces, evaluating the composite $(\varphi\circ\psi)^\sharp$ on $\Spec A$ gives $\psi^\sharp(X)\circ\varphi^\sharp(\Spec A)$, so

$$\Phi(\varphi\circ\psi)=\Gamma(\psi)\circ\Phi(\varphi)$$

Also, given a ring homomorphism $\theta: A \rightarrow A'$, since setting $f=1$ in the construction of [Proposition 9](#prop9){: data-lid="cc24r" } gives $(\Spec\theta)^\sharp(\Spec A)=\theta$, for any $\varphi: X \rightarrow \Spec A'$ we have

$$\Phi((\Spec\theta)\circ\varphi)=\Phi(\varphi)\circ\theta$$

That is, the given bijection is natural in both $X$ and $A$, from which we obtain the claimed natural isomorphism.
:::

---
**References**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).

---

[^1]: In general, for any sheaf $\mathcal{F}$ on $X$, we denote $\mathcal{F}(X)$ by $\Gamma(X, \mathcal{F})$.
