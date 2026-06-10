---
title: "Affine Schemes"
description: "We define the structure sheaf on the spectrum of a ring to construct an affine scheme, and discuss locally ringed spaces and their morphisms."
excerpt: "Affine schemes defined by the structure sheaf on the spectrum of a ring"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/affine_schemes
sidebar: 
    nav: "scheme_theory-en"

date: 2025-01-27
last_modified_at: 2025-01-27
weight: 3
translated_at: 2026-06-02T00:00:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-02T00:00:02+00:00
---
The most basic example of a sheaf on a topological space is the collection of continuous functions on that space, and the $$\mathscr{O}_{\Spec A}$$ we are about to define is similar. However, if $$\mathscr{O}_{\Spec A}$$ were merely the sheaf of continuous functions on $$\Spec A$$, there would be no need to give it a new name. For the simplest example, since the only prime ideal of any field $$\mathbb{K}$$ is $$(0)$$, the topological space $$\Spec \mathbb{K}$$ is always a singleton, and there is only one topology on it. In other words, if we wish to distinguish the spectra of two non-isomorphic fields, that information must be encoded in the structure sheaf of $$\Spec \mathbb{K}$$. To ensure that the spectrum carries enough algebraic information, we define $$\mathscr{O}_{\Spec A}$$ as the sheaf of algebraic functions on $$A$$.

## Locally ringed space

We have already treated sheaves on a topological space in [[Topology] §Sheaves](/en/math/topology/sheaves), but the definitions given there are insufficient to describe the structure sheaf we will define on $$\Spec A$$.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A pair $$(X,\mathscr{O}_X)$$ consisting of a topological space $$X$$ and a $$\cRing$$-valued sheaf $$\mathscr{O}_X$$ on it is called a *ringed space*. If for every point $$x$$ of $$X$$, the stalk $$\mathscr{O}_{X,x}$$ at $$x$$ is always a local ring, then this pair $$(X, \mathscr{O}_X)$$ is called a *locally ringed space*.

</div>

Our claim is that we can define a suitable structure sheaf $$\mathscr{O}_{\Spec A}$$ on $$\Spec A$$ to make $$(\Spec A, \mathscr{O}_{\Spec A})$$ a locally ringed space, and that $$\Spec$$ defined in this way enjoys the same functoriality as in [§Spectra, ⁋Proposition 2](/en/math/scheme_theory/spectrums#prop2) or [§Spectra, ⁋Proposition 8](/en/math/scheme_theory/spectrums#prop8). To write this down mathematically, we must first define morphisms between locally ringed spaces.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> For two ringed spaces $$(X, \mathscr{O}_X)$$ and $$(Y, \mathscr{O}_Y)$$, a morphism between them is a pair consisting of a continuous map $$\varphi:X \rightarrow Y$$ and a morphism $$\varphi^\sharp:\mathscr{O}_Y \rightarrow \varphi_\ast \mathscr{O}_X$$ in $$\Sh(Y,\cRing)$$.

A morphism between two locally ringed spaces $$(X, \mathscr{O}_X)$$ and $$(Y, \mathscr{O}_Y)$$ is a morphism $$(\varphi,\varphi^\sharp)$$ of ringed spaces that additionally induces a local homomorphism $$\varphi_x^\sharp:\mathscr{O}_{Y,\varphi(x)} \rightarrow \mathscr{O}_{X,x}$$ for each $$x\in X$$.

</div>

## Algebraic Functions on $$\Spec A$$

Now we must define $$\mathscr{O}_{\Spec A}$$. As mentioned at the beginning of this post, it is the sheaf of algebraic functions on $$\Spec A$$, and we saw in [§Spectra, §§Classical algebraic geometry](/en/math/scheme_theory/spectrums#classical-algebraic-geometry) that when $$A=\mathbb{K}[\x_1,\ldots, \x_n]$$, these are functions that can be represented as rational functions on a suitable neighborhood. What played an important role in this process was that elements of $$A$$, i.e., polynomials, could be treated as functions on $$\mathbb{A}_\mathbb{K}^n=\mSpec A$$; however, in the general case, elements of $$A$$ are not polynomials, and moreover we cannot evaluate points of $$\Spec A$$ at elements of $$A$$.

Therefore, to generalize this discussion, we argue as follows. First, we regard an element of $$A$$ as a function $$f$$, just as in the preceding example. Then the *function value* of $$f$$ at a point $$\mathfrak{p}\in\Spec A$$ is the image of $$f$$ under the canonical projection $$\pr_\mathfrak{p}: A \rightarrow A/\mathfrak{p}$$. In particular, the condition that $$f$$ vanishes at the point $$\mathfrak{p}$$ is

$$f\equiv 0\pmod{\mathfrak{p}}\iff f\in \mathfrak{p}\iff \mathfrak{p}\in Z(f)$$

That is, $$Z(f)$$ can be understood as the set of points where $$f=0$$, and its complement, the principal open set $$D(f)$$, as the set of points where $$f\neq 0$$.

From this perspective, we can describe what the *algebraic functions* on $$\Spec A$$ are. As in [§Spectra, §§Classical algebraic geometry](/en/math/scheme_theory/spectrums#classical-algebraic-geometry), these are defined as functions that can be represented as rational functions whose denominators are functions not vanishing on the given open set.

Now suppose a principal open set $$D(f)$$ is given. Then by definition, when an algebraic function on $$D(f)$$ is represented as a rational function $$g/h$$, the functions $$h$$ that can appear in the denominator must satisfy $$D(f)\subseteq D(h)$$.

<div class="proposition" markdown="1">

<ins id="lem3">**Lemma 3**</ins> For a fixed element $$f\in A$$, define

$$S(f)=\{h\in A\mid D(f)\subseteq D(h)\}$$

Then $$S(f)$$ is a multiplicative subset of $$A$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, since $$D(1)=\Spec A$$, it is obvious that $$S(f)$$ contains the empty product $$1$$. Now if $$h_1,h_2\in S(f)$$, then from the equality

$$D(h_1h_2)=\Spec A\setminus Z(h_1h_2)=\Spec A\setminus (Z(h_1)\cup Z(h_2))=(\Spec A\setminus Z(h_1))\cap (\Spec A\setminus Z(h_2))=D(h_1)\cap D(h_2)$$

we know that $$D(f)\subseteq D(h_1)\cap D(h_2)=D(h_1h_2)$$. This equality is nothing but a geometric explanation of [[Algebraic Structures] §Field of Fractions, ⁋Proposition 8](/en/math/algebraic_structures/field_of_fractions#prop8).

</details>

It is intuitive that the collection of algebraic functions on the subset $$D(f)$$ of $$\Spec A$$ should be defined as $$S(f)^{-1}A$$, and indeed we will define it this way. Before doing so, we prove the following lemma.

<div class="proposition" markdown="1">

<ins id="lem4">**Lemma 4**</ins> $$D(f)\subseteq D(h)$$ holds if and only if there exists an integer $$n\geq 1$$ such that $$f^n\in (h)$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

That $$D(f)\subseteq D(h)$$ is equivalent to $$Z(h)\subseteq Z(f)$$, which by the third result of [§Spectra, ⁋Lemma 6](/en/math/scheme_theory/spectrums#lem6) is equivalent to $$\sqrt{(f)}\subseteq \sqrt{(h)}$$.

If $$\sqrt{(f)}\subseteq \sqrt{(h)}$$, then from $$(f)\subseteq \sqrt{(f)}\subseteq \sqrt{(h)}$$ we get $$f\in \sqrt{(h)}$$, and thus there exists an integer $$n\geq 1$$ such that $$f^n\in (h)$$. Conversely, if there exists an integer $$n\geq 1$$ such that $$f^n\in (h)$$, then from $$f\in \sqrt{(h)}$$ we get $$(f)\subseteq \sqrt{(h)}$$, and therefore

$$\sqrt{(f)}\subseteq\sqrt{\sqrt{(h)}}=\sqrt{(h)}$$

.

</details>

Using this lemma, we can express $$S(f)^{-1}A$$ in a cleaner way.

<div class="proposition" markdown="1">

<ins id="lem5">**Lemma 5**</ins> For any $$f\in A$$, there exists an isomorphism

$$S(f)^{-1}A\cong S_f^{-1}A$$

Moreover, if $$S(g)\subseteq S(f)$$, then the following diagram

![localizations](/assets/images/Math/Scheme_Theory/Affine_Schemes-1.png){:style="width:10.4em" class="invert" .align-center}

commutes.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, let us denote the canonical morphisms by $$\epsilon(f): A \rightarrow S(f)^{-1}A$$ and $$\epsilon_f:A \rightarrow S_f^{-1}A$$. Then since $$D(f)=D(f^n)$$ for any $$n\geq 1$$, we have $$f^n\in S(f)$$, and therefore the image of $$S_f$$ under $$\epsilon(f)$$ consists entirely of units in $$S(f)^{-1}A$$. Hence from [[Commutative Algebra] §Localization, ⁋Proposition 6](/en/math/commutative_algebra/localization#prop6) we obtain the following commutative diagram

![universal_property-1](/assets/images/Math/Scheme_Theory/Affine_Schemes-2.png){:style="width:8.5em" class="invert" .align-center}

.

Now observe the following equivalence

$$D(f)\subseteq D(g)\iff f^n\in (g)\text{ for some $n\geq 1$}\iff f^n=ag\text{ for some $n\geq 1$ and $a\in A$}\tag{$\ast$}$$

Then for any $$g$$ satisfying $$D(f)\subseteq D(g)$$, we can find suitable $$n\geq 1$$ and $$a\in A$$ such that $$f^n=ag$$, so from

$$\frac{g}{1}\frac{a}{f^n}=1\qquad\text{in $S_f^{-1}A$}$$

we know that $$g$$ is a unit in $$S_f^{-1}A$$. Therefore, again from [[Commutative Algebra] §Localization, ⁋Proposition 6](/en/math/commutative_algebra/localization#prop6) we obtain the following commutative diagram

![universal_property-2](/assets/images/Math/Scheme_Theory/Affine_Schemes-3.png){:style="width:8.5em" class="invert" .align-center}

That $$\overline{\epsilon(f)}$$ and $$\overline{\epsilon_f}$$ are inverse to each other is obvious from uniqueness.

Now suppose $$S(g)\subseteq S(f)$$. Then $$\widehat{\epsilon(f)}:S(g)^{-1}A \rightarrow S(f)^{-1}A$$ is again obviously defined via [[Commutative Algebra] §Localization, ⁋Proposition 6](/en/math/commutative_algebra/localization#prop6) by the following diagram

![universal_property-3](/assets/images/Math/Scheme_Theory/Affine_Schemes-4.png){:style="width:8.5em" class="invert" .align-center}

and since $$S(g)\subseteq S(f)\iff D(f)\subseteq D(g)$$, from the equivalence ($$\ast$$) above we know that $$g$$ is a unit in $$S_f^{-1}A$$, and therefore so are all $$g^k$$. From this we obtain the following commutative diagram involving $$\widecheck{\epsilon_f}: S_g^{-1}A \rightarrow S_f^{-1}A$$:

![universal_property-4](/assets/images/Math/Scheme_Theory/Affine_Schemes-5.png){:style="width:8em" class="invert" .align-center}

Then that the diagram in question commutes is obvious from considering the following diagram:

![universal_property-5](/assets/images/Math/Scheme_Theory/Affine_Schemes-6.png){:style="width:17em" class="invert" .align-center}

That is, from

$$\epsilon_f=\widecheck{\epsilon_f}\circ\epsilon_g=\widecheck{\epsilon_f}\circ\overline{\epsilon_g}\circ\epsilon(g)$$

and

$$\epsilon_f=\overline{\epsilon_f}\circ\epsilon(f)=\overline{\epsilon_f}\circ\widehat{\epsilon(f)}\circ\epsilon(g)$$

we know that $$\epsilon_f$$ sends elements of $$S(g)$$ to units in $$S_f^{-1}A$$, and moreover from the uniqueness of $$\widetilde{\epsilon_f}$$ defined to satisfy $$\epsilon_f=\widetilde{\epsilon_f}\circ\epsilon(g)$$ via [[Commutative Algebra] §Localization, ⁋Proposition 6](/en/math/commutative_algebra/localization#prop6), we obtain $$\widecheck{\epsilon_f}\circ\overline{\epsilon_g}=\overline{\epsilon_f}\circ\widehat{\epsilon(f)}$$.

</details>

Therefore, it suffices to regard algebraic functions on $$D(f)$$ as elements of $$S_f^{-1}A$$. In the previous post we agreed to write $$S_f^{-1}A$$ as $$A_f$$ for convenience.

<div class="proposition" markdown="1">

<ins id="lem6">**Lemma 6**</ins> For the base $$\{D(f)\}_{f\in A}$$ of $$\Spec A$$, define for each $$f_i\in A$$

$$\mathscr{F}(D(f_i))=S(f_i)^{-1}A\cong A_{f_i}$$

Also, for each $$f_i,f_j\in A$$ satisfying $$D(f_i)\subseteq D(f_j)$$, define the restriction map

$$\rho_{ji}: S(f_j)^{-1}(A) \rightarrow S(f_i)^{-1}(A)$$

as the map obtained by applying [[Commutative Algebra] §Localization, ⁋Proposition 6](/en/math/commutative_algebra/localization#prop6) to the canonical morphism $$A\rightarrow S(f_i)^{-1}(A)$$. Then these data satisfy the two conditions of [[Topology] §Sheaves, ⁋Proposition 8](/en/math/topology/sheaves#prop8), and therefore the ($$\cRing$$-valued) sheaf on $$\Spec A$$ extending $$\mathscr{F}$$ is uniquely determined.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

That the $$\rho_{ji}$$ satisfy the conditions for restriction maps ([[Topology] §Presheaves, ⁋Definition 2](/en/math/topology/presheaves#def2)) is obvious from the universal property of [[Commutative Algebra] §Localization, ⁋Proposition 6](/en/math/commutative_algebra/localization#prop6). Here, by [Lemma 5](#lem5), the map $$\rho_{ji}: S(f_j)^{-1}(A) \rightarrow S(f_i)^{-1}(A)$$ simply takes an element of $$S(f_j)^{-1}(A)$$, written in the form

$$g/h,\qquad\text{where $h\in S(f_j)$}\tag{$\ast$}$$

and views it as an element of $$S(f_i)^{-1}(A)$$; indeed, from the relation

$$h\in S(f_j)\iff D(f_j)\subseteq D(h)\implies D(f_i)\subseteq D(h)\iff h\in S(f_i)$$

we can regard ($$\ast$$) as an element of $$S(f_i)^{-1}(A)$$.

We now prove the two conditions of [[Topology] §Sheaves, ⁋Proposition 8](/en/math/topology/sheaves#prop8). For notational convenience, since $$D(f)=\Spec A_f$$, it suffices to consider the case $$f=1$$ after replacing $$A$$ by $$A_f$$. Fix elements $$f_i\in A$$ satisfying $$\Spec A=\bigcup_{i\in I}D(f_i)$$.

First, to show the first condition, suppose an element $$s\in A$$ satisfies $$s=0$$ in $$S(f_i)^{-1}A$$ for all $$i\in I$$, and let us show that $$s$$ is also $$0$$ as an element of $$A$$. Then by [§Spectra, ⁋Lemma 12](/en/math/scheme_theory/spectrums#lem12) we can choose $$f_1,\ldots, f_n$$ among the $$f_i$$ such that $$\Spec A=\bigcup_{i=1}^n D(f_i)$$, and by assumption there exist integers $$m_i$$ satisfying

$$f_i^{m_i}s=0$$

for all $$i=1,\ldots, n$$. On the other hand, from the calculation after [§Spectra, ⁋Lemma 11](/en/math/scheme_theory/spectrums#lem11) we have $$D(f_i^{m_i})=D(f_i)$$ for all $$i$$, so

$$\Spec A=\bigcup_{i=1}^n D(f_i^{m_i})$$

and from this there exist elements $$a_i\in A$$ such that $$1=\sum_{i=1}^n a_i f_i^{m_i}$$. (See the proof of [§Spectra, ⁋Lemma 12](/en/math/scheme_theory/spectrums#lem12), or the proof of [[Commutative Algebra] §Integral Extensions, ⁋Proposition 15](/en/math/commutative_algebra/integral_extension#prop15))

Therefore

$$s=1s=\left(\sum_{i=1}^n a_i f_i^{m_i}\right)s=\sum_{i=1}^n a_i (f_i^{m_i}s)=0$$

.

Now to show the second condition, suppose that for each $$i$$ there exists an element $$s_i=a_i/f_i^{m_i}$$ in $$S(f_i)^{-1}A$$ such that for each $$i,j$$

$$\frac{a_i}{f_i^{m_i}}=\frac{a_j}{f_j^{m_j}}\quad\text{ in $D(f_i)\cap D(f_j)=D(f_if_j)$}$$

But since $$D(f_i)=D(f_i^{m_i})$$ and $$D(f_j)=D(f_j^{m_j})$$, we have

$$D(f_if_j)=D(f_i)\cap D(f_j)=D(f_i^{m_i})\cap D(f_j^{m_j})=D(f_i^{m_i}f_j^{m_j})$$

and therefore there exists an integer $$N_{ij}$$ such that

$$(f_i^{m_i}f_j^{m_j})^{N_{ij}}(a_jf_i^{m_j}-a_if_j^{m_i})=0$$

Let $$N=\max_{i,j}\{N_{ij}\}$$, so that

$$(f_i^{m_i}f_j^{m_j})^N(a_jf_i^{m_j}-a_if_j^{m_i})=0$$

that is,

$$a_if_i^{Nm_i}f_j^{Nm_j+m_j}=a_jf_j^{Nm_j}f_i^{Nm_i+m_i}$$

From the given assumption

$$\Spec A=\bigcup_{i=1}^n D(f_i)=\bigcup_{i=1}^n D(f_i^{Nm_i+m_i})$$

there exist elements $$b_i\in A$$ such that

$$1=\sum_{i=1}^n b_ia_if_i^{Nm_i+m_i}$$

Now set $$s=\sum_{i=1}^n b_ia_i f_i^{Nm_i}$$; then

$$sf_j^{Nm_j+m_j}=\sum_{i=1}^n b_ia_i f_i^{Nm_i} f_j^{Nm_j+m_j}=\sum_{i=1}^nb_ia_jf_j^{Nm_j}f_i^{Nm_i+m_i}=a_jf_j^{Nm_j}$$

so $$f_j^{Nm_j}(sf_j^{m_j}-a_j)=0$$ holds for all $$j$$, and therefore on $$D(f_j)$$

$$\frac{s}{1}=\frac{a_j}{f_j^{m_j}}$$

From this we obtain the desired $$s$$.

If $$I$$ is infinite, choose a finite subset $$J=\{1,\ldots, n\}$$ of $$I$$ satisfying $$\Spec A=\bigcup_{j\in J} D(f_j)$$ and repeat the above to obtain $$s\in \mathscr{F}(\Spec A)$$; then it suffices to show that this also satisfies $$s_\alpha=s\vert_{D(f_\alpha)}$$ on $$D(f_\alpha)$$ for $$\alpha\in I\setminus J$$. To show this, repeat the same process for the finite set

$$J\cup\{\alpha\}=\{1,2,\ldots, n,\alpha\}\subseteq I$$

to obtain $$s'\in \mathscr{F}(\Spec A)$$. Then by definition $$s$$ and $$s'$$ satisfy $$s\vert_{D(f_i)}=s'\vert_{D(f_i)}$$ for all $$i=1,\ldots, n$$, and since $$\Spec A=\bigcup D(f_i)$$, by the first condition of [[Topology] §Sheaves, ⁋Proposition 8](/en/math/topology/sheaves#prop8) shown above we know $$s=s'$$, and from this

$$s\vert_{D(f_\alpha)}=s'\vert_{D(f_\alpha)}=s_\alpha$$

Since this holds for every $$\alpha$$, the restriction of $$s$$ to any $$D(f_\alpha)$$ equals $$s_\alpha$$.

</details>

<div class="definition" markdown="1">

<ins id="def7">**Definition 7**</ins> We write the sheaf on $$\Spec A$$ defined by [Lemma 5](#lem5) as $$\mathscr{O}_{\Spec A}$$, and call it the *structure sheaf*.

</div>

Then $$(\Spec A,\mathscr{O}_{\Spec A})$$ is a locally ringed space.

<div class="proposition" markdown="1">

<ins id="lem8">**Lemma 8**</ins> For $$(\Spec A,\mathscr{O}_{\Spec A})$$ and any point $$\mathfrak{p}\in \Spec A$$, there exists an isomorphism

$$A_\mathfrak{p}\cong \mathscr{O}_{\Spec A, \mathfrak{p}}=\varinjlim_\text{\scriptsize $U\ni\mathfrak{p}$ open} \mathscr{O}_{\Spec A}(U)$$

Moreover, for any $$f\in A$$ satisfying $$\mathfrak{p}\in D(f)$$, the following diagram

![stalk_and_localization-1](/assets/images/Math/Scheme_Theory/Affine_Schemes-7.png){:style="width:13.2em" class="invert" .align-center}

commutes.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Since the $$D(f)$$ form a base for $$\Spec A$$ by [[Topology] §Bases of Topological Spaces, ⁋Proposition 2](/en/math/topology/topological_bases#prop2), we have

$$\mathscr{O}_{\Spec A, \mathfrak{p}}=\varinjlim_{D(f)\ni\mathfrak{p}} \mathscr{O}_{\Spec A}(D(f))$$

by [[Topology] §Bases of Topological Spaces, ⁋Proposition 5](/en/math/topology/topological_bases#prop5). On the other hand, since $$\mathfrak{p}\in D(f)\iff f\not\in \mathfrak{p}$$, we obtain the following diagram

![stalk_and_localization-2](/assets/images/Math/Scheme_Theory/Affine_Schemes-8.png){:style="width:32em" class="invert" .align-center}

and therefore proving the given isomorphism is the same as proving the following algebraic isomorphism

$$A_\mathfrak{p}\cong \varinjlim_{\mathfrak{p}\not\ni f} A_f\tag{$\ast\ast$}$$

which follows by using the universal property of localization ([[Commutative Algebra] §Localization, ⁋Proposition 6](/en/math/commutative_algebra/localization#prop6)) and the universal property of direct limits. For the diagram in question, one simply replaces $$\varinjlim A_f$$ by $$A_\mathfrak{p}$$ in the above diagram via the isomorphism ($$\ast\ast$$).

</details>

Now we are finally ready to write down the functoriality of $$\Spec$$ in the form we want.

<div class="proposition" markdown="1">

<ins id="prop9">**Proposition 9**</ins> The correspondence $$A\mapsto (\Spec A, \mathscr{O}_{\Spec A})$$ defines a contravariant functor $$\Spec: \cRing^\op \rightarrow \LRS$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

We already know that a ring homomorphism $$\phi: A \rightarrow B$$ induces a continuous map $$\Spec\phi: \Spec B \rightarrow \Spec A$$. ([§Spectra, ⁋Proposition 8](/en/math/scheme_theory/spectrums#prop8)) Therefore it suffices to describe

$$(\Spec\phi)^\sharp: \mathscr{O}_{\Spec A} \rightarrow (\Spec\phi)_\ast \mathscr{O}_{\Spec B}$$

For this, we look at the map on principal open sets

$$(\Spec\phi)^\sharp(D(f)): \mathscr{O}_{\Spec A}(D(f)) \rightarrow \mathscr{O}_{\Spec B}((\Spec \phi)^{-1}(D(f)))$$

On the other hand, from the proof of [§Spectra, ⁋Proposition 8](/en/math/scheme_theory/spectrums#prop8) we know that

$$(\Spec\phi)^{-1}(Z(f))=Z(\phi(f))$$

and therefore

$$(\Spec\phi)^{-1}(D(f))=D(\phi(f))$$

Thus, by the definition of the structure sheaf, defining $$(\Spec\phi)^\sharp(D(f))$$ is the same as defining

$$A_f \rightarrow B_{\phi(f)}$$

and this is obtained by applying [[Commutative Algebra] §Localization, ⁋Proposition 6](/en/math/commutative_algebra/localization#prop6) to the composition

$$A \overset{\phi}{\longrightarrow}B \overset{\epsilon}{\longrightarrow} B_{\phi(f)}$$

Of course, we must show that this $$(\Spec\phi)^\sharp$$ defines the same map on the intersection $$D(f)\cap D(g)$$, but this follows from using the uniqueness result in [[Commutative Algebra] §Localization, ⁋Proposition 6](/en/math/commutative_algebra/localization#prop6) on $$D(f)\cap D(g)$$.

From the above we know that $$(\Spec\phi, (\Spec\phi)^\sharp): (\Spec B, \mathscr{O}_{\Spec B}) \rightarrow (\Spec A, \mathscr{O}_{\Spec A})$$ is a morphism of ringed spaces. Now to show that this is a morphism of locally ringed spaces, it suffices to show that for any $$\mathfrak{q}\in \Spec B$$,

$$(\Spec\phi)^\sharp_\mathfrak{q}:\mathscr{O}_{\Spec A, (\Spec \phi)(\mathfrak{q})} \rightarrow\mathscr{O}_{\Spec B, \mathfrak{q}}$$

is a local homomorphism. But $$(\Spec \phi)(\mathfrak{q})=\phi^{-1}(\mathfrak{q})$$, and therefore by [Lemma 8](#lem8) the map $$(\Spec\phi)^\sharp_\mathfrak{q}$$ is a ring homomorphism from $$A_{\phi^{-1}(\mathfrak{q})}$$ to $$B_{\mathfrak{q}}$$ that sends the unique maximal ideal $$\phi^{-1}(\mathfrak{q})A_{\phi^{-1}(\mathfrak{q})}$$ of $$A_{\phi^{-1}(\mathfrak{q})}$$ to the unique maximal ideal $$\mathfrak{q}B_\mathfrak{q}$$ of $$B_{\mathfrak{q}}$$.

</details>

## Affine Schemes

<div class="definition" markdown="1">

<ins id="def10">**Definition 10**</ins> We define the essential image of the functor $$\Spec:\cRing^\op \rightarrow \LRS$$ from [Proposition 9](#prop9) as the *affine scheme*.

</div>

We write the category of affine schemes as $$\AffSch$$. Then the contravariant functor $$\Spec:\cRing^\op \rightarrow \AffSch$$ is essentially surjective by definition. ([[Category Theory] §Natural Transformations, ⁋Theorem 5](/en/math/category_theory/natural_transformations#thm5)) Also, if $$(\varphi, \varphi^\sharp): (\Spec B, \mathscr{O}_{\Spec B}) \rightarrow (\Spec A, \mathscr{O}_{\Spec A})$$ is induced by some ring homomorphism $$\phi$$, then taking $$1=f\in A$$ in the proof of [Proposition 9](#prop9) gives

$$\varphi^\sharp(D(1))= \bigl(A \overset{\phi}{\longrightarrow} B \overset{\id_B}{\longrightarrow} B_{\phi(1)}=B\bigr)=\phi$$

and therefore this functor is necessarily faithful. Moreover, the following holds.

<div class="proposition" markdown="1">

<ins id="prop11">**Proposition 11**</ins> The functor $$\Spec: \cRing^\op \rightarrow \LRS$$ is fully faithful.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Suppose we are given two affine schemes $$(X, \mathscr{O}_{X})$$ and $$(Y, \mathscr{O}_{Y})$$ and a morphism

$$(X, \mathscr{O}_{X}) \rightarrow (Y, \mathscr{O}_{Y})$$

between them. Then via isomorphisms $$(\Spec B, \mathscr{O}_{\Spec B})\cong (X, \mathscr{O}_X)$$ and $$(\Spec A, \mathscr{O}_{\Spec A})\cong (Y, \mathscr{O}_Y)$$, we can view this as a morphism

$$(\varphi, \varphi^\sharp): (\Spec B, \mathscr{O}_{\Spec B}) \rightarrow (\Spec A, \mathscr{O}_{\Spec A})$$

between the two spectra (as locally ringed spaces). Therefore it suffices to prove that this morphism of locally ringed spaces comes from some ring homomorphism $$\phi$$. Taking a hint from the above proof that $$\Spec$$ is faithful, define a ring homomorphism $$\phi:A \rightarrow B$$ by

$$\phi=\varphi^\sharp(D(1)):A \rightarrow B$$

Now to complete the claim we must show that $$\Spec\phi=(\varphi,\varphi^\sharp)$$. This is shown by proving that for any $$\mathfrak{q}\in \Spec B$$,

$$(\Spec \phi)(\mathfrak{q})=\phi^{-1}(\mathfrak{q})=\varphi(\mathfrak{q})$$

First, putting $$f=1$$ in [Lemma 8](#lem8), we obtain the following diagram

![faithuful](/assets/images/Math/Scheme_Theory/Affine_Schemes-9.png){:style="width:32em" class="invert" .align-center}

In this diagram, the vertical maps are all isomorphisms, and we know that all faces except the following one

![commuting_square](/assets/images/Math/Scheme_Theory/Affine_Schemes-10.png){:style="width:11em" class="invert" .align-center}

are commuting squares. Therefore, in the above diagram the map $$A \rightarrow \mathscr{O}_{\Spec B, \mathfrak{q}}$$ is determined equally no matter which path we take, and applying [[Commutative Algebra] §Localization, ⁋Proposition 6](/en/math/commutative_algebra/localization#prop6) to this map uniquely determines $$A_{\varphi(\mathfrak{q})} \rightarrow \mathscr{O}_{\Spec B, \mathfrak{q}}$$. From this we know that *all* faces of the above diagram are commuting squares. That is, $$\phi_\mathfrak{q}:A_{\varphi(\mathfrak{q})}\rightarrow B_\mathfrak{q}$$ is also a local homomorphism, and therefore $$\phi^{-1}(\mathfrak{q})=\varphi(\mathfrak{q})$$. Now that $$\phi$$ equals $$\varphi^\sharp$$ on the structure sheaf follows by considering only restriction maps, so the desired claim is proved from the above.

</details>

Therefore, viewing $$\Spec$$ as a contravariant functor from $$\cRing$$ to $$\AffSch$$, it is a categorical equivalence between the two categories $$\cRing^\op$$ and $$\AffSch$$. Moreover, by [Proposition 11](#prop11), $$\AffSch$$ is a full subcategory of $$\LRS$$.

By [[Category Theory] §Natural Transformations, ⁋Theorem 5](/en/math/category_theory/natural_transformations#thm5), it suffices to show that $$\Spec$$ is full.

On the other hand, for any spectrum $$(\Spec A, \mathscr{O}_{\Spec A})$$, we know by definition that

$$\mathscr{O}_{\Spec A}(A)=\mathscr{O}_{\Spec A}(D(1))\cong A$$

If a locally ringed space $$(X, \mathscr{O}_X)$$ is an affine scheme, then by examining $$\mathscr{O}_X(X)$$ in the same way we can determine whether $$(X, \mathscr{O}_X)$$ is isomorphic to the spectrum of some ring. That is, for an affine scheme $$(X, \mathscr{O}_X)$$, if we set $$A=\mathscr{O}_X(X)$$ then $$(X, \mathscr{O}_X)\cong (\Spec A, \mathscr{O}_{\Spec A})$$ holds. More generally, we define the following.

<div class="definition" markdown="1">

<ins id="def12">**Definition 12**</ins> For any locally ringed space $$(X, \mathscr{O}_X)$$, we define the *global section functor* $$\Gamma:\LRS \rightarrow \cRing^\op$$ by $$X\mapsto \Gamma(X, \mathscr{O}_X)=\mathscr{O}_X(X)$$.[^1]

</div>

A notable fact in the proof of [Proposition 11](#prop11) is that the hypothesis that $$(X, \mathscr{O}_X)$$ is an affine scheme is unnecessary. That is, even if we drop the assumption $$(X, \mathscr{O}_X)\cong(\Spec B, \mathscr{O}_{\Spec B})$$ and use the following diagram instead of the diagram in [Proposition 11](#prop11),

![adjoint](/assets/images/Math/Scheme_Theory/Affine_Schemes-11.png){:style="width:32em" class="invert" .align-center}

we can carry out a similar argument, and in this case the $$B$$ in the conclusion is replaced by $$\Gamma(X, \mathscr{O}_X)$$. Since $$\mathscr{O}_X$$ is data determined by $$X$$ anyway, writing this briefly as $$\Gamma(X)$$, we obtain the following theorem.

<div class="proposition" markdown="1">

<ins id="thm13">**Theorem 13**</ins> For any locally ringed space $$(X, \mathscr{O}_X)$$ and any ring $$A$$, there exists a natural isomorphism

$$\Hom_\LRS(X, \Spec A)\cong \Hom_{\cRing^\op}(\Gamma(X), A)=\Hom_{\cRing}(A, \Gamma(X))$$

That is, the global section functor $$\Gamma: \LRS \rightarrow \cRing^\op$$ is the left adjoint of the $$\Spec$$ functor $$\Spec:\cRing^\op \rightarrow \LRS$$.

</div>

---
**References**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/). 

---

[^1]: In general, for any sheaf $$\mathscr{F}$$ on $$X$$ we write $$\mathscr{F}(X)$$ as $$\Gamma(X, \mathscr{F})$$.
