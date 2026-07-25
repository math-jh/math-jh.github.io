---
title: "Affine Schemes"
description: "We construct affine schemes by defining structure sheaves on the spectra of rings, and discuss the definitions of locally ringed spaces and their morphisms."
excerpt: "Affine schemes defined by structure sheaves on ring spectra"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/affine_schemes
sidebar: 
    nav: "scheme_theory-en"

date: 2025-01-27
weight: 3
translated_at: 2026-07-18T15:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-07-18T15:30:02+00:00
---
Among the most basic examples of a sheaf on a topological space is the collection of continuous functions defined on it, and the sheaf $\mathcal{O}_{\Spec A}$ we are about to define is similar: the only difference is that we think of *regular functions* instead of continuous ones.

## Locally ringed space

The basic definitions of sheaves on topological spaces were already covered in [\[Topology\] §Sheaves](/en/math/topology/sheaves), but that definition is somewhat insufficient for describing the structure sheaf on $\Spec A$.

::: Definition 1
A pair $(X,\mathcal{O}_X)$ of a topological space $X$ and an $\cRing$-valued sheaf $\mathcal{O}_X$ on it is called a *ringed space*. If for every point $x$ of $X$, the stalk $\mathcal{O}_{X,x}$ at $x$ is always a local ring, then this pair $(X, \mathcal{O}_X)$ is called a *locally ringed space*.
:::

Our claim is that we can define a suitable structure sheaf $\mathcal{O}_{\Spec A}$ on $\Spec A$ to make $(\Spec A, \mathcal{O}_{\Spec A})$ a locally ringed space, and that this $\Spec$ so defined enjoys the same functoriality as in [§Spectrums, ⁋Proposition 2](/en/math/scheme_theory/spectrums#prop2) or [§Spectrums, ⁋Proposition 8](/en/math/scheme_theory/spectrums#prop8). To write this down mathematically, we first need to define morphisms between locally ringed spaces.

::: Definition 2
For two ringed spaces $(X, \mathcal{O}_X)$ and $(Y, \mathcal{O}_Y)$, a morphism between them means a pair consisting of a continuous function $\varphi:X \rightarrow Y$ and a morphism $\varphi^\sharp:\mathcal{O}_Y \rightarrow \varphi_\ast \mathcal{O}_X$ in $\Sh(Y;\cRing)$.

A morphism between two locally ringed spaces $(X, \mathcal{O}_X)$ and $(Y, \mathcal{O}_Y)$ is a morphism $(\varphi,\varphi^\sharp)$ of ringed spaces that additionally induces a local homomorphism $\varphi_x^\sharp:\mathcal{O}_{Y,\varphi(x)} \rightarrow \mathcal{O}_{X,x}$ for each $x\in X$.
:::

## Algebraic functions on $\Spec A$

We now need to define $\mathcal{O}_{\Spec A}$. As mentioned at the beginning of this post, this is the sheaf of algebraic functions on $\Spec A$, and it is precisely the generalization of [\[Algebraic Varieties\] §Affine Varieties, ⁋Definition 14](/en/math/algebraic_varieties/affine_varieties#def14).

Let us generalize this discussion to schemes. First, we think of elements of $A$ as functions $f$, just as in algebraic varieties. Then the *function value* of $f$ at a point $\mathfrak{p}\in\Spec A$ is the image of $f$ under the canonical projection $\pi: A \rightarrow A/\mathfrak{p}$. In particular, $f$ vanishing at the point $\mathfrak{p}$ means

$$f\equiv 0\pmod{\mathfrak{p}}\iff f\in \mathfrak{p}\iff \mathfrak{p}\in Z(f)$$

That is, $Z(f)$ can be understood as the locus of points where $f=0$, and its complement, the principal open set $D(f)$, can be understood as the locus of points where $f\neq 0$.

From this perspective, we can describe what the *algebraic functions* on $\Spec A$ are. Just as in [\[Algebraic Varieties\] §Affine Varieties, ⁋Definition 14](/en/math/algebraic_varieties/affine_varieties#def14), they are defined to be functions that can be represented as rational functions whose denominators are functions not vanishing on the given open set.

Now suppose a principal open set $D(f)$ is given. Then by definition, when an algebraic function on $D(f)$ is represented as a rational function $g/h$, the functions $h$ that can appear in the denominator must satisfy $D(f)\subseteq D(h)$.

::: Lemma 3
For a fixed element $f\in A$, define

$$S(f)=\{h\in A\mid D(f)\subseteq D(h)\}$$

Then $S(f)$ is a multiplicative subset of $A$.
:::
::: Proof
First, since $D(1)=\Spec A$, it is trivial that $S(f)$ contains the empty product $1$. Now if $h_1,h_2\in S(f)$, then from the identity

$$D(h_1h_2)=\Spec A\setminus Z(h_1h_2)=\Spec A\setminus (Z(h_1)\cup Z(h_2))=(\Spec A\setminus Z(h_1))\cap (\Spec A\setminus Z(h_2))=D(h_1)\cap D(h_2)$$

we know that $D(f)\subseteq D(h_1)\cap D(h_2)=D(h_1h_2)$. This identity is merely a geometric interpretation of [\[Algebraic Structures\] §Field of Fractions, ⁋Proposition 8](/en/math/algebraic_structures/field_of_fractions#prop8).
:::

It is intuitive, and indeed we will define it this way, that the collection of algebraic functions defined on a subset $D(f)$ of $\Spec A$ should be $S(f)^{-1}A$. Before that, we prove the following lemma.

::: Lemma 4
The inclusion $D(f)\subseteq D(h)$ is equivalent to the existence of some $n\geq 1$ such that $f^n\in (h)$.
:::
::: Proof
$D(f)\subseteq D(h)$ is equivalent to $Z(h)\subseteq Z(f)$, which by the third result of [§Spectrums, ⁋Lemma 6](/en/math/scheme_theory/spectrums#lem6) is equivalent to $\sqrt{(f)}\subseteq \sqrt{(h)}$.

If $\sqrt{(f)}\subseteq \sqrt{(h)}$, then from $(f)\subseteq \sqrt{(f)}\subseteq \sqrt{(h)}$ we get $f\in \sqrt{(h)}$, and thus there exists some $n\geq 1$ such that $f^n\in (h)$. Conversely, if there exists some $n\geq 1$ such that $f^n\in (h)$, then from $f\in \sqrt{(h)}$ we get $(f)\subseteq \sqrt{(h)}$, and therefore

$$\sqrt{(f)}\subseteq\sqrt{\sqrt{(h)}}=\sqrt{(h)}$$

as desired.
:::

Using this lemma, we can express $S(f)^{-1}A$ in a cleaner way.

::: Lemma 5
For any $f\in A$, there exists an isomorphism

$$S(f)^{-1}A\cong S_f^{-1}A$$

Moreover, if $S(g)\subseteq S(f)$, then the following diagram

{% diagram Math/Scheme_Theory/Affine_Schemes-1.svg width="10.55em" alt="localizations" %}

commutes.
:::
::: Proof
Let us denote the canonical morphisms by $\epsilon(f): A \rightarrow S(f)^{-1}A$ and $\epsilon_f:A \rightarrow S_f^{-1}A$. Then since $D(f)=D(f^n)$ for any $n\geq 1$, we have $f^n\in S(f)$, and thus the image of $S_f$ under $\epsilon(f)$ consists entirely of units in $S(f)^{-1}A$. Therefore, from [\[Commutative Algebra\] §Localization, ⁋Proposition 6](/en/math/commutative_algebra/localization#prop6) we obtain the following commutative diagram

{% diagram Math/Scheme_Theory/Affine_Schemes-2.svg width="8.64em" alt="universal_property-1" %}

Now observe the following equivalence

$$D(f)\subseteq D(g)\iff f^n\in (g)\text{ for some $n\geq 1$}\iff f^n=ag\text{ for some $n\geq 1$ and $a\in A$}\tag{$\ast$}$$

Then for any $g$ satisfying $D(f)\subseteq D(g)$, we can find suitable $n\geq 1$ and $a\in A$ with $f^n=ag$, so from

$$\frac{g}{1}\frac{a}{f^n}=1\qquad\text{in $S_f^{-1}A$}$$

we know that $g$ is a unit in $S_f^{-1}A$. Thus again from [\[Commutative Algebra\] §Localization, ⁋Proposition 6](/en/math/commutative_algebra/localization#prop6) we obtain the following commutative diagram

{% diagram Math/Scheme_Theory/Affine_Schemes-3.svg width="8.64em" alt="universal_property-2" %}

That $\overline{\epsilon(f)}$ and $\overline{\epsilon_f}$ are inverses of each other is now obvious from uniqueness.

Now suppose $S(g)\subseteq S(f)$. Then $\widehat{\epsilon(f)}:S(g)^{-1}A \rightarrow S(f)^{-1}A$ is similarly defined through [\[Commutative Algebra\] §Localization, ⁋Proposition 6](/en/math/commutative_algebra/localization#prop6) by the following diagram

{% diagram Math/Scheme_Theory/Affine_Schemes-4.svg width="8.64em" alt="universal_property-3" %}

and since $S(g)\subseteq S(f)\iff D(f)\subseteq D(g)$, from the equivalence ($\ast$) above we know that $g$ is a unit in $S_f^{-1}A$, and hence so are all $g^k$. From this, the following commutative diagram containing $\widecheck{\epsilon_f}: S_g^{-1}A \rightarrow S_f^{-1}$ exists

{% diagram Math/Scheme_Theory/Affine_Schemes-5.svg width="7.13em" alt="universal_property-4" %}

That the diagram in the claim commutes is then obvious from considering the following diagram

{% diagram Math/Scheme_Theory/Affine_Schemes-6.svg width="17.14em" alt="universal_property-5" %}

namely, from

$$\epsilon_f=\widecheck{\epsilon_f}\circ\epsilon_g=\widecheck{\epsilon_f}\circ\overline{\epsilon_g}\circ\epsilon(g)$$

and

$$\epsilon_f=\overline{\epsilon_f}\circ\epsilon(f)=\overline{\epsilon_f}\circ\widehat{\epsilon(f)}\circ\epsilon(g)$$

we know that $\epsilon_f$ sends elements of $S(g)$ to units in $S_f^{-1}A$, and moreover from the uniqueness of $\widetilde{\epsilon_f}$ satisfying $\epsilon_f=\widetilde{\epsilon_f}\circ\epsilon(g)$ via [\[Commutative Algebra\] §Localization, ⁋Proposition 6](/en/math/commutative_algebra/localization#prop6) we obtain $\widecheck{\epsilon_f}\circ\overline{\epsilon_g}=\overline{\epsilon_f}\circ\widehat{\epsilon(f)}$.
:::

Therefore, it suffices to think of algebraic functions defined on $D(f)$ as elements of $S_f^{-1}A$. For convenience, in previous posts we agreed to denote $S_f^{-1}A$ by $A_f$.

::: Lemma 6
For the base $\{D(f)\}_{f\in A}$ of $\Spec A$, define for each $f_i\in A$

$$\mathcal{F}(D(f_i))=S(f_i)^{-1}A\cong A_{f_i}$$

Also, for each $f_i,f_j\in A$ satisfying $D(f_i)\subseteq D(f_j)$, define the restriction map

$$\rho_{ji}: S(f_j)^{-1}(A) \rightarrow S(f_i)^{-1}(A)$$

to be the map obtained by applying [\[Commutative Algebra\] §Localization, ⁋Proposition 6](/en/math/commutative_algebra/localization#prop6) to the canonical morphism $A\rightarrow S(f_i)^{-1}(A)$. Then these data satisfy the two conditions of [\[Topology\] §Sheaves, ⁋Proposition 8](/en/math/topology/sheaves#prop8), and therefore a ($\cRing$-valued) sheaf on $\Spec A$ extending $\mathcal{F}$ is uniquely determined.
:::
::: Proof
That the $\rho_{ji}$ satisfy the conditions for restriction maps in [\[Topology\] §Presheaves, ⁋Definition 2](/en/math/topology/presheaves#def2) is obvious from the universal property of [\[Commutative Algebra\] §Localization, ⁋Proposition 6](/en/math/commutative_algebra/localization#prop6). Here, $\rho_{ji}: S(f_j)^{-1}(A) \rightarrow S(f_i)^{-1}(A)$ is, by [Lemma 5](#lem5), simply the map that sends an element of $S(f_j)^{-1}(A)$ written in the form

$$g/h,\qquad\text{where $h\in S(f_j)$}\tag{$\ast$}$$

to the same expression viewed as an element of $S(f_i)^{-1}(A)$, since

$$h\in S(f_j)\iff D(f_j)\subseteq D(h)\implies D(f_i)\subseteq D(h)\iff h\in S(f_i)$$

We now prove the two conditions of [\[Topology\] §Sheaves, ⁋Proposition 8](/en/math/topology/sheaves#prop8). For notational convenience, since $D(f)=\Spec A_f$, it suffices to consider only the case $f=1$ after replacing $A$ by $A_f$. Fix $f_i\in A$ such that $\Spec A=\bigcup_{i\in I}D(f_i)$.

First, to show the first condition, suppose an element $s\in A$ satisfies $s=0$ in $S(f_i)^{-1}A$ for all $i\in I$, and let us show that $s$ is also $0$ as an element of $A$. Then by [§Spectrums, ⁋Lemma 12](/en/math/scheme_theory/spectrums#lem12) we can choose $f_1,\ldots, f_n$ among the $f_i$ such that $\Spec A=\bigcup_{i=1}^n D(f_i)$, and by assumption there exist $m_i$ satisfying

$$f_i^{m_i}s=0$$

for all $i=1,\ldots, n$. On the other hand, since $D(f_i^{m_i})=D(f_i)$ for all $i$ by the computation after [§Spectrums, ⁋Lemma 11](/en/math/scheme_theory/spectrums#lem11),

$$\Spec A=\bigcup_{i=1}^n D(f_i^{m_i})$$

and from this there exist $a_i\in A$ such that

$$1=\sum_{i=1}^n a_i f_i^{m_i}$$

(See the proof of [§Spectrums, ⁋Lemma 12](/en/math/scheme_theory/spectrums#lem12), or the proof of [\[Commutative Algebra\] §Integral Extension, ⁋Proposition 15](/en/math/commutative_algebra/integral_extension#prop15).)

Therefore

$$s=1s=\left(\sum_{i=1}^n a_i f_i^{m_i}\right)s=\sum_{i=1}^n a_i (f_i^{m_i}s)=0$$

Now to show the second condition, suppose for each $i$ there exists an element $s_i=a_i/f_i^{m_i}$ of $S(f_i)^{-1}A$ such that for each $i,j$

$$\frac{a_i}{f_i^{m_i}}=\frac{a_j}{f_j^{m_j}}\quad\text{ in $D(f_i)\cap D(f_j)=D(f_if_j)$}$$

But since $D(f_i)=D(f_i^{m_i})$ and $D(f_j)=D(f_j^{m_j})$,

$$D(f_if_j)=D(f_i)\cap D(f_j)=D(f_i^{m_i})\cap D(f_j^{m_j})=D(f_i^{m_i}f_j^{m_j})$$

and thus there exists suitable $N_{ij}$ such that

$$(f_i^{m_i}f_j^{m_j})^{N_{ij}}(a_if_j^{m_j}-a_jf_i^{m_i})=0$$

Let $N=\max_{i,j}\{N_{ij}\}$ so that

$$(f_i^{m_i}f_j^{m_j})^N(a_if_j^{m_j}-a_jf_i^{m_i})=0$$

that is,

$$a_if_i^{Nm_i}f_j^{Nm_j+m_j}=a_jf_j^{Nm_j}f_i^{Nm_i+m_i}$$

From the given assumption

$$\Spec A=\bigcup_{i=1}^n D(f_i)=\bigcup_{i=1}^n D(f_i^{Nm_i+m_i})$$

we can find suitable $b_i\in A$ such that

$$1=\sum_{i=1}^n b_if_i^{Nm_i+m_i}$$

Now set $s=\sum_{i=1}^n b_ia_i f_i^{Nm_i}$; then

$$sf_j^{Nm_j+m_j}=\sum_{i=1}^n b_ia_i f_i^{Nm_i} f_j^{Nm_j+m_j}=\sum_{i=1}^nb_ia_jf_j^{Nm_j}f_i^{Nm_i+m_i}=a_jf_j^{Nm_j}$$

so $f_j^{Nm_j}(sf_j^{m_j}-a_j)=0$ holds for all $j$, and therefore on $D(f_j)$

$$\frac{s}{1}=\frac{a_j}{f_j^{m_j}}$$

From this we obtain the desired $s$.

If $I$ is infinite, choose a finite subset $J=\{1,\ldots, n\}$ of $I$ such that $\Spec A=\bigcup_{j\in J} D(f_j)$, repeat the above to obtain $s\in \mathcal{F}(\Spec A)$, and then show that this also satisfies $s_\alpha=s\vert_{D(f_\alpha)}$ for $D(f_\alpha)$ with $\alpha\in I\setminus J$. To show this, repeat the same process for the finite set

$$J\cup\{\alpha\}=\{1,2,\ldots, n,\alpha\}\subseteq I$$

to obtain $s'\in \mathcal{F}(\Spec A)$. Then by definition $s$ and $s'$ satisfy $s\vert_{D(f_i)}=s'\vert_{D(f_i)}$ for all $i=1,\ldots, n$, and since $\Spec A=\bigcup D(f_i)$, from the first condition of [\[Topology\] §Sheaves, ⁋Proposition 8](/en/math/topology/sheaves#prop8) shown above we know $s=s'$, and thus

$$s\vert_{D(f_\alpha)}=s'\vert_{D(f_\alpha)}=s_\alpha$$

Since this holds for every $\alpha$, we know that $s$ restricts to $s_\alpha$ on any $D(f_\alpha)$.
:::

::: Definition 7
The sheaf on $\Spec A$ defined by [Lemma 6](#lem6) is denoted $\mathcal{O}_{\Spec A}$ and is called the *structure sheaf*.
:::

Then $(\Spec A,\mathcal{O}_{\Spec A})$ is a locally ringed space.

::: Lemma 8
For $(\Spec A,\mathcal{O}_{\Spec A})$ and any point $\mathfrak{p}\in \Spec A$, there exists an isomorphism

$$A_\mathfrak{p}\cong \mathcal{O}_{\Spec A, \mathfrak{p}}=\varinjlim_\text{\scriptsize $U\ni\mathfrak{p}$ open} \mathcal{O}_{\Spec A}(U)$$

Moreover, for any $f\in A$ satisfying $\mathfrak{p}\in D(f)$, the following diagram

{% diagram Math/Scheme_Theory/Affine_Schemes-7.svg width="14.55em" alt="stalk_and_localization-1" %}

commutes.
:::
::: Proof
By [\[Topology\] §Topological Bases, ⁋Proposition 2](/en/math/topology/topological_bases#prop2), the $D(f)$ form a base for $\Spec A$, so by [\[Topology\] §Topological Bases, ⁋Proposition 5](/en/math/topology/topological_bases#prop5)

$$\mathcal{O}_{\Spec A, \mathfrak{p}}=\varinjlim_{D(f)\ni\mathfrak{p}} \mathcal{O}_{\Spec A}(D(f))$$

On the other hand, since $\mathfrak{p}\in D(f)\iff f\not\in \mathfrak{p}$, we obtain the following diagram

{% diagram Math/Scheme_Theory/Affine_Schemes-8.svg width="37.01em" alt="stalk_and_localization-2" %}

and therefore showing the given isomorphism is the same as showing the following algebraic isomorphism

$$A_\mathfrak{p}\cong \varinjlim_{\mathfrak{p}\not\ni f} A_f\tag{$\ast\ast$}$$

which follows from using the universal property of [\[Commutative Algebra\] §Localization, ⁋Proposition 6](/en/math/commutative_algebra/localization#prop6) and the universal property of direct limits. The diagram in the claim is obtained by replacing $\varinjlim A_f$ with $A_\mathfrak{p}$ in the above diagram via the isomorphism ($\ast\ast$).
:::

We are now finally ready to write the functoriality of $\Spec$ in the form we want.

::: Proposition 9
The correspondence $A\mapsto (\Spec A, \mathcal{O}_{\Spec A})$ defines a contravariant functor $\Spec: \cRing^\op \rightarrow \LRS$.
:::
::: Proof
We already know that a ring homomorphism $\phi: A \rightarrow B$ induces a continuous function $\Spec\phi: \Spec B \rightarrow \Spec A$. ([§Spectrums, ⁋Proposition 8](/en/math/scheme_theory/spectrums#prop8)) Thus it suffices to describe

$$(\Spec\phi)^\sharp: \mathcal{O}_{\Spec A} \rightarrow (\Spec\phi)_\ast \mathcal{O}_{\Spec B}$$

For this, we look at the functions on principal open sets

$$(\Spec\phi)^\sharp(D(f)): \mathcal{O}_{\Spec A}(D(f)) \rightarrow \mathcal{O}_{\Spec B}((\Spec \phi)^{-1}(D(f)))$$

On the other hand, from the proof of [§Spectrums, ⁋Proposition 8](/en/math/scheme_theory/spectrums#prop8)

$$(\Spec\phi)^{-1}(Z(f))=Z(\phi(f))$$

so we know

$$(\Spec\phi)^{-1}(D(f))=D(\phi(f))$$

Therefore, by the definition of the structure sheaf, defining $(\Spec\phi)^\sharp(D(f))$ is the same as defining

$$A_f \rightarrow B_{\phi(f)}$$

which is obtained by applying [\[Commutative Algebra\] §Localization, ⁋Proposition 6](/en/math/commutative_algebra/localization#prop6) to the composition

$$A \overset{\phi}{\longrightarrow}B \overset{\epsilon}{\longrightarrow} B_{\phi(f)}$$

Of course, we must show that $(\Spec\phi)^\sharp$ so defined gives the same function on the intersection $D(f)\cap D(g)$, but this follows from using the uniqueness result in [\[Commutative Algebra\] §Localization, ⁋Proposition 6](/en/math/commutative_algebra/localization#prop6) on $D(f)\cap D(g)$.

From the above, we know that $(\Spec\phi, (\Spec\phi)^\sharp): (\Spec B, \mathcal{O}_{\Spec B}) \rightarrow (\Spec A, \mathcal{O}_{\Spec A})$ is a morphism of ringed spaces. To show that this is a morphism of locally ringed spaces, it suffices to show that for any $\mathfrak{q}\in \Spec B$,

$$(\Spec\phi)^\sharp_\mathfrak{q}:\mathcal{O}_{\Spec A, (\Spec \phi)(\mathfrak{q})} \rightarrow\mathcal{O}_{\Spec B, \mathfrak{q}}$$

is a local homomorphism. But $(\Spec \phi)(\mathfrak{q})=\phi^{-1}(\mathfrak{q})$, and therefore by [Lemma 8](#lem8) we know that $(\Spec\phi)^\sharp_\mathfrak{q}$ is a ring homomorphism from $A_{\phi^{-1}(\mathfrak{q})}$ to $B_{\mathfrak{q}}$ that sends the unique maximal ideal $\phi^{-1}(\mathfrak{q})A_{\phi^{-1}(\mathfrak{q})}$ of $A_{\phi^{-1}(\mathfrak{q})}$ to the unique maximal ideal $\mathfrak{q}B_\mathfrak{q}$ of $B_\mathfrak{q}$.
:::

## Affine scheme

::: Definition 10
The essential image of the functor $\Spec:\cRing^\op \rightarrow \LRS$ from [Proposition 9](#prop9) is defined to be the *affine scheme*.
:::

We denote the category of affine schemes by $\AffSch$. Then the contravariant functor $\Spec:\cRing^\op \rightarrow \AffSch$ is essentially surjective by definition. ([\[Category Theory\] §Natural Transformations, ⁋Theorem 5](/en/math/category_theory/natural_transformations#thm5)) Also, if $(\varphi, \varphi^\sharp): (\Spec B, \mathcal{O}_{\Spec B}) \rightarrow (\Spec A, \mathcal{O}_{\Spec A})$ is induced from some ring homomorphism $\phi$, then taking $1=f\in A$ in the proof of [Proposition 9](#prop9)

$$\varphi^\sharp(D(1))= \bigl(A \overset{\phi}{\longrightarrow} B \overset{\id_B}{\longrightarrow} B_{\phi(1)}=B\bigr)=\phi$$

so this functor is necessarily faithful. Moreover, the following holds.

::: Proposition 11
The functor $\Spec: \cRing^\op \rightarrow \LRS$ is fully faithful.
:::
::: Proof
Given any two affine schemes $(X, \mathcal{O}_{X})$, $(Y, \mathcal{O}_{Y})$ and a morphism between them

$$(X, \mathcal{O}_{X}) \rightarrow (Y, \mathcal{O}_{Y})$$

via isomorphisms $(\Spec B, \mathcal{O}_{\Spec B})\cong (X, \mathcal{O}_X)$ and $(\Spec A, \mathcal{O}_{\Spec A})\cong (Y, \mathcal{O}_Y)$, we can view this as a morphism of (locally ringed spaces between) two spectra

$$(\varphi, \varphi^\sharp): (\Spec B, \mathcal{O}_{\Spec B}) \rightarrow (\Spec A, \mathcal{O}_{\Spec A})$$

Thus it suffices to prove that this morphism of locally ringed spaces comes from some ring homomorphism $\phi$. Taking a hint from the above proof that $\Spec$ is faithful, define a ring homomorphism $\phi:A \rightarrow B$ by

$$\phi=\varphi^\sharp(D(1)):A \rightarrow B$$

To complete the claim, we must now show that $\Spec\phi=(\varphi,\varphi^\sharp)$. This follows from showing that for any $\mathfrak{q}\in \Spec B$

$$(\Spec \phi)(\mathfrak{q})=\phi^{-1}(\mathfrak{q})=\varphi(\mathfrak{q})$$

First, taking $f=1$ in [Lemma 8](#lem8), we obtain the following diagram

{% diagram Math/Scheme_Theory/Affine_Schemes-9.svg width="39.41em" alt="faithful" %}

In this diagram, the vertical maps are all isomorphisms, and we know that all faces except the following face

{% diagram Math/Scheme_Theory/Affine_Schemes-10.svg width="13.26em" alt="commuting_square" %}

are commuting squares. Therefore, in the above diagram, $A \rightarrow \mathcal{O}_{\Spec B, \mathfrak{q}}$ is determined identically regardless of which path we take, and applying [\[Commutative Algebra\] §Localization, ⁋Proposition 6](/en/math/commutative_algebra/localization#prop6) to this function uniquely determines $A_{\varphi(\mathfrak{q})} \rightarrow \mathcal{O}_{\Spec B, \mathfrak{q}}$. From this we know that *all* faces of the above diagram are commuting squares. That is, $\phi_\mathfrak{q}:A_{\varphi(\mathfrak{q})}\rightarrow B_\mathfrak{q}$ is also a local homomorphism, and therefore $\phi^{-1}(\mathfrak{q})=\varphi(\mathfrak{q})$. Now that $\phi$ agrees with $\varphi^\sharp$ on the structure sheaf, it suffices to consider restriction maps, and thus the desired claim is proved.
:::

Therefore, viewing $\Spec$ as a contravariant functor from $\cRing$ to $\AffSch$, it is a categorical equivalence between the two categories $\cRing^\op$ and $\AffSch$. Moreover, by [Proposition 11](#prop11), $\AffSch$ is a full subcategory of $\LRS$.

On the other hand, for any spectrum $(\Spec A, \mathcal{O}_{\Spec A})$, we know by definition that

$$\mathcal{O}_{\Spec A}(A)=\mathcal{O}_{\Spec A}(D(1))\cong A$$

If a locally ringed space $(X, \mathcal{O}_X)$ were an affine scheme, we could similarly examine $\mathcal{O}_X(X)$ to see whether $(X, \mathcal{O}_X)$ is isomorphic to the spectrum of some ring. That is, for an affine scheme $(X, \mathcal{O}_X)$, setting $A=\mathcal{O}_X(X)$ gives $(X, \mathcal{O}_X)\cong (\Spec A, \mathcal{O}_{\Spec A})$. More generally, we define the following.

::: Definition 12
For any locally ringed space $(X, \mathcal{O}_X)$, we define the *global section functor* $\Gamma:\LRS \rightarrow \cRing^\op$ by $X\mapsto \Gamma(X, \mathcal{O}_X)=\mathcal{O}_X(X)$.[^1]
:::

A notable fact from the proof of [Proposition 11](#prop11) is that the assumption that $(X, \mathcal{O}_X)$ is an affine scheme was unnecessary. That is, even if we drop the assumption $(X, \mathcal{O}_X)\cong(\Spec B, \mathcal{O}_{\Spec B})$ and use the following diagram instead of the diagram in [Proposition 11](#prop11)

{% diagram Math/Scheme_Theory/Affine_Schemes-11.svg width="34.92em" alt="adjoint" %}

we can carry out a similar argument, and in this case the $B$ in the conclusion is replaced by $\Gamma(X, \mathcal{O}_X)$. Since $\mathcal{O}_X$ is data determined by $X$ anyway, abbreviating this as $\Gamma(X)$, we obtain the following theorem.

::: Theorem 13
For any locally ringed space $(X, \mathcal{O}_X)$ and any ring $A$, there exists a natural isomorphism

$$\Hom_\LRS(X, \Spec A)\cong \Hom_{\cRing^\op}(\Gamma(X), A)=\Hom_{\cRing}(A, \Gamma(X))$$

That is, the global section functor $\Gamma: \LRS \rightarrow \cRing^\op$ is the left adjoint of the $\Spec$ functor $\Spec:\cRing^\op \rightarrow \LRS$.
:::
::: Proof
Through the isomorphism $\mathcal{O}_{\Spec A}(D(f))\cong A_f$ from [Lemma 6](#lem6), let us identify $\mathcal{O}_{\Spec A}(\Spec A)=\mathcal{O}_{\Spec A}(D(1))$ with $A$. Under this identification, the restriction map of $\mathcal{O}_{\Spec A}$ from $\mathcal{O}_{\Spec A}(\Spec A)$ to $\mathcal{O}_{\Spec A}(D(f))$ is the canonical morphism $\epsilon_f: A \rightarrow A_f$.

First define the two correspondences $\Phi$ and $\Psi$, and then show that they are inverses of each other. Given a morphism $(\varphi,\varphi^\sharp): X \rightarrow \Spec A$ of locally ringed spaces, computing $\varphi^\sharp$ on the open set $\Spec A$ gives a ring homomorphism

$$\Phi(\varphi,\varphi^\sharp)=\varphi^\sharp(\Spec A): A=\mathcal{O}_{\Spec A}(\Spec A) \rightarrow (\varphi_\ast\mathcal{O}_X)(\Spec A)=\mathcal{O}_X(X)=\Gamma(X)$$

Conversely, suppose a ring homomorphism $\phi:A \rightarrow \Gamma(X)$ is given. For each $x\in X$, denote by $\phi_x:A \rightarrow \mathcal{O}_{X,x}$ the ring homomorphism obtained by composing $\phi$ with taking the germ at $x$, i.e., $\phi_x(a)=\phi(a)_x$. Since $(X,\mathcal{O}_X)$ is a locally ringed space, $\mathcal{O}_{X,x}$ is a local ring with unique maximal ideal $\mathfrak{m}_x$, and therefore by [\[Algebraic Structures\] §Field of Fractions, ⁋Proposition 9](/en/math/algebraic_structures/field_of_fractions#prop9)

$$\varphi(x)=\phi_x^{-1}(\mathfrak{m}_x)$$

is a prime ideal of $A$, i.e., a point of $\Spec A$.

Let us show that the function $\varphi: X \rightarrow \Spec A$ so defined is continuous. For this, we show that for any $s\in \Gamma(X)$,

$$X_s=\{x\in X\mid \text{$s_x\not\in \mathfrak{m}_x$}\}$$

is an open set of $X$. By [\[Commutative Algebra\] §Localization, ⁋Proposition 2](/en/math/commutative_algebra/localization#prop2), $\mathfrak{m}_x$ is the set of all non-units of the local ring $\mathcal{O}_{X,x}$, so $x\in X_s$ is equivalent to $s_x$ being a unit in $\mathcal{O}_{X,x}$. Now if $x\in X_s$, there exists $t\in \mathcal{O}_{X,x}$ with $s_xt=1$, and choosing a suitable open neighborhood $W$ of $x$ and a section $u\in \mathcal{O}_X(W)$ representing $t$, we have $(s\vert_Wu)_x=1_x$, so if necessary we can shrink $W$ so that $s\vert_Wu=1$ in $\mathcal{O}_X(W)$. Then for any $y\in W$, since $s_yu_y=1$, $s_y$ is a unit in $\mathcal{O}_{X,y}$, and thus $W\subseteq X_s$. That is, $X_s$ is an open set.

On the other hand, for any $f\in A$

$$\varphi^{-1}(D(f))=\{x\in X\mid f\not\in \varphi(x)\}=\{x\in X\mid \phi(f)_x\not\in \mathfrak{m}_x\}=X_{\phi(f)}$$

and since the principal open sets form a base for $\Spec A$ ([§Spectrums, ⁋Lemma 11](/en/math/scheme_theory/spectrums#lem11)), $\varphi$ is a continuous function.

We now define the sheaf morphism $\varphi^\sharp: \mathcal{O}_{\Spec A} \rightarrow \varphi_\ast \mathcal{O}_X$. For each $f\in A$, set $V_f=\varphi^{-1}(D(f))=X_{\phi(f)}$, and denote by

$$\theta_f: A\overset{\phi}{\longrightarrow} \Gamma(X) \longrightarrow \mathcal{O}_X(V_f)$$

the ring homomorphism obtained by composing $\phi$ with the restriction map. Our claim is that $\theta_f(f)=\phi(f)\vert_{V_f}$ is a unit in $\mathcal{O}_X(V_f)$. Indeed, by the definition of $V_f$, for any $y\in V_f$ the germ $\phi(f)_y$ is a unit in $\mathcal{O}_{X,y}$, so repeating the argument above we can find an open neighborhood $W_y\subseteq V_f$ of $y$ and $u_y\in \mathcal{O}_X(W_y)$ such that $\phi(f)\vert_{W_y}u_y=1$. Then on the intersection $W_y\cap W_{y'}$, the restrictions of $u_y$ and $u_{y'}$ are both inverses of $\phi(f)\vert_{W_y\cap W_{y'}}$ under multiplication, hence they agree, and therefore by the gluability axiom of [\[Topology\] §Sheaves, ⁋Definition 1](/en/math/topology/sheaves#def1) they glue to a single $u\in \mathcal{O}_X(V_f)$. Now since $\phi(f)\vert_{V_f}u$ and $1$ agree on each $W_y$, by the identity axiom we have $\phi(f)\vert_{V_f}u=1$.

In particular, $\theta_f$ sends all elements of the multiplicative subset $S_f=\{1,f,f^2,\ldots\}$ to units in $\mathcal{O}_X(V_f)$, so by [\[Commutative Algebra\] §Localization, ⁋Proposition 6](/en/math/commutative_algebra/localization#prop6) there exists a unique ring homomorphism

$$\varphi^\sharp(D(f)): A_f=\mathcal{O}_{\Spec A}(D(f)) \rightarrow \mathcal{O}_X(V_f)=(\varphi_\ast\mathcal{O}_X)(D(f))$$

satisfying

$$\varphi^\sharp(D(f))\circ \epsilon_f=\theta_f$$

If $D(g)\subseteq D(f)$, then $V_g\subseteq V_f$, and both compositions

$$A_f \overset{\varphi^\sharp(D(f))}{\longrightarrow} \mathcal{O}_X(V_f) \longrightarrow \mathcal{O}_X(V_g),\qquad A_f \longrightarrow A_g \overset{\varphi^\sharp(D(g))}{\longrightarrow} \mathcal{O}_X(V_g)$$

compose with $\epsilon_f$ to give $\theta_g$, so again by the uniqueness in [\[Commutative Algebra\] §Localization, ⁋Proposition 6](/en/math/commutative_algebra/localization#prop6) they are equal. That is, the $\varphi^\sharp(D(f))$ commute with restriction maps.

Now for any open set $U\subseteq \Spec A$ and $s\in \mathcal{O}_{\Spec A}(U)$, consider for each principal open set $D(f)$ contained in $U$ the section

$$\varphi^\sharp(D(f))(s\vert_{D(f)})\in (\varphi_\ast\mathcal{O}_X)(D(f))$$

Since the intersection of two principal open sets $D(f)\cap D(g)=D(fg)$ is also a principal open set, by the commutativity above these sections agree on the intersection, and therefore by the gluability axiom and identity axiom of the sheaf $\varphi_\ast\mathcal{O}_X$ they glue to a unique $\varphi^\sharp(U)(s)\in (\varphi_\ast\mathcal{O}_X)(U)$. That the so defined $\varphi^\sharp(U)$ is a ring homomorphism and commutes with restriction maps follows again from the identity axiom, and thus we obtain the sheaf morphism $\varphi^\sharp$.

Finally, let us show that $(\varphi,\varphi^\sharp)$ is a morphism of locally ringed spaces. For any $x\in X$ and $\mathfrak{p}=\varphi(x)$, by [Lemma 8](#lem8) we have $\mathcal{O}_{\Spec A,\mathfrak{p}}\cong A_\mathfrak{p}$, and under this identification the stalk morphism $\varphi_x^\sharp: A_\mathfrak{p} \rightarrow \mathcal{O}_{X,x}$ induced by $\varphi^\sharp$ satisfies

$$\varphi^\sharp_x\circ\epsilon=\phi_x$$

by taking germs at $x$ of both sides of the equation $\varphi^\sharp(D(f))\circ\epsilon_f=\theta_f$. Here $\epsilon: A \rightarrow A_\mathfrak{p}$ is the canonical morphism. Now for any $a/s\in A_\mathfrak{p}$, since $s\not\in \mathfrak{p}=\phi_x^{-1}(\mathfrak{m}_x)$, we know $\phi_x(s)$ is a unit, and therefore

$$\varphi_x^\sharp(a/s)=\phi_x(a)\phi_x(s)^{-1}$$

In particular, if $a\in \mathfrak{p}$ then $\phi_x(a)\in \mathfrak{m}_x$, so $\varphi_x^\sharp(a/s)\in \mathfrak{m}_x$, and thus the ideal $(\varphi_x^\sharp)^{-1}(\mathfrak{m}_x)$ contains $\mathfrak{p}A_\mathfrak{p}$. On the other hand, since $\varphi_x^\sharp(1)=1\not\in \mathfrak{m}_x$, this ideal is not all of $A_\mathfrak{p}$, and since $\mathfrak{p}A_\mathfrak{p}$ is the unique maximal ideal of $A_\mathfrak{p}$ ([\[Commutative Algebra\] §Localization, ⁋Proposition 8](/en/math/commutative_algebra/localization#prop8))

$$(\varphi_x^\sharp)^{-1}(\mathfrak{m}_x)=\mathfrak{p}A_\mathfrak{p}$$

That is, $\varphi_x^\sharp$ is a local homomorphism, and by [Definition 2](#def2) we know that $\Psi(\phi)=(\varphi,\varphi^\sharp)$ is a morphism of locally ringed spaces.

We now show that $\Phi$ and $\Psi$ are inverses of each other. First, for $\Psi(\phi)=(\varphi,\varphi^\sharp)$, taking $f=1$ gives $D(1)=\Spec A$, $V_1=X$, and $\epsilon_1=\id_A$, so the above construction gives

$$\Phi(\Psi(\phi))=\varphi^\sharp(\Spec A)=\theta_1=\phi$$

Conversely, given a morphism $(\varphi,\varphi^\sharp): X \rightarrow \Spec A$ of locally ringed spaces, let $\phi=\Phi(\varphi,\varphi^\sharp)=\varphi^\sharp(\Spec A)$ and $\Psi(\phi)=(\varphi',(\varphi')^\sharp)$. For any $x\in X$, since $\varphi^\sharp$ commutes with restriction maps, the stalk morphism $\varphi_x^\sharp: \mathcal{O}_{\Spec A, \varphi(x)}\cong A_{\varphi(x)} \rightarrow \mathcal{O}_{X,x}$ induced by $\varphi^\sharp$ satisfies $\varphi_x^\sharp\circ\epsilon=\phi_x$, where $\epsilon: A \rightarrow A_{\varphi(x)}$ being the canonical morphism follows from [Lemma 8](#lem8). On the other hand, since $(\varphi,\varphi^\sharp)$ is a morphism of locally ringed spaces, $\varphi_x^\sharp$ is a local homomorphism, and thus the ideal $(\varphi_x^\sharp)^{-1}(\mathfrak{m}_x)$ is a proper ideal containing $\varphi(x)A_{\varphi(x)}$, i.e., it is $\varphi(x)A_{\varphi(x)}$ itself. Therefore by [\[Commutative Algebra\] §Localization, ⁋Proposition 8](/en/math/commutative_algebra/localization#prop8)

$$\varphi'(x)=\phi_x^{-1}(\mathfrak{m}_x)=\epsilon^{-1}\left((\varphi_x^\sharp)^{-1}(\mathfrak{m}_x)\right)=\epsilon^{-1}\left(\varphi(x)A_{\varphi(x)}\right)=\varphi(x)$$

and the two continuous functions $\varphi$ and $\varphi'$ are equal. Now from the fact that $\varphi^\sharp$ commutes with restriction maps, for any $f\in A$

$$\varphi^\sharp(D(f))\circ\epsilon_f=\theta_f$$

holds, and this is exactly the equation defining $(\varphi')^\sharp(D(f))$, so by the uniqueness in [\[Commutative Algebra\] §Localization, ⁋Proposition 6](/en/math/commutative_algebra/localization#prop6) we have $\varphi^\sharp(D(f))=(\varphi')^\sharp(D(f))$. Since the two sheaf morphisms agree on the base $\{D(f)\}_{f\in A}$, by the identity axiom of $\varphi_\ast\mathcal{O}_X$ we have $\varphi^\sharp=(\varphi')^\sharp$, and therefore $\Psi(\Phi(\varphi,\varphi^\sharp))=(\varphi,\varphi^\sharp)$.

Finally, let us verify that this bijection is natural. Given a morphism $\psi: X' \rightarrow X$ of locally ringed spaces, computing the composition $(\varphi\circ\psi)^\sharp$ on $\Spec A$ gives $\psi^\sharp(X)\circ\varphi^\sharp(\Spec A)$, so

$$\Phi(\varphi\circ\psi)=\Gamma(\psi)\circ\Phi(\varphi)$$

Also, given a ring homomorphism $\theta: A \rightarrow A'$, from the construction in [Proposition 9](#prop9) with $f=1$ we have $(\Spec\theta)^\sharp(\Spec A)=\theta$, so for any $\varphi: X \rightarrow \Spec A'$

$$\Phi((\Spec\theta)\circ\varphi)=\Phi(\varphi)\circ\theta$$

That is, the given bijection is natural in both $X$ and $A$, and from this we obtain the natural isomorphism in the claim.
:::

---
**References**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/). 

---

[^1]: In general, for any sheaf $\mathcal{F}$ on any $X$, we denote $\mathcal{F}(X)$ by $\Gamma(X, \mathcal{F})$.
