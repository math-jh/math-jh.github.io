---
title: "Affine Scheme"
description: "We construct the affine scheme by defining the structure sheaf on the spectrum of a ring, and cover the definition of locally ringed spaces and their morphisms."
excerpt: "The affine scheme defined by the structure sheaf on a ring's spectrum"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/affine_schemes
sidebar: 
    nav: "scheme_theory-en"

date: 2025-01-27
weight: 3
translated_at: 2026-07-26T21:15:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-07-26T21:15:02+00:00
---
The most basic example of a sheaf on a topological space is the sheaf of continuous functions, and the sheaf $\mathcal{O}_{\Spec A}$ we are about to define is analogous: the only difference is that we use *regular functions* in place of continuous ones.

## Locally ringed space

Sheaves on topological spaces were already treated in [[Topology] §Sheaves](/en/math/topology/sheaves), but that definition is somewhat inadequate for describing the structure sheaf on $\Spec A$.

::: Definition 1
A pair $(X,\mathcal{O}_X)$ consisting of a topological space $X$ and a $\cRing$-valued sheaf $\mathcal{O}_X$ on it is called a *ringed space*. If for every point $x\in X$, the stalk $\mathcal{O}_{X,x}$ at $x$ is a local ring, then this pair $(X, \mathcal{O}_X)$ is called a *locally ringed space*.
:::

Our claim is that we can define a suitable structure sheaf $\mathcal{O}_{\Spec A}$ on $\Spec A$ so that $(\Spec A, \mathcal{O}_{\Spec A})$ becomes a locally ringed space, and that this $\Spec$ construction enjoys the same functoriality as in [[§Spectrums, ⁋Proposition 2]](/en/math/scheme_theory/spectrums#prop2) or [[§Spectrums, ⁋Proposition 8]](/en/math/scheme_theory/spectrums#prop8). To state this precisely, we first define morphisms between locally ringed spaces.

::: Definition 2
For two ringed spaces $(X, \mathcal{O}_X)$ and $(Y, \mathcal{O}_Y)$, a morphism between them is a pair consisting of a continuous map $\varphi:X \rightarrow Y$ and a morphism $\varphi^\sharp:\mathcal{O}_Y \rightarrow \varphi_\ast \mathcal{O}_X$ in $\Sh(Y;\cRing)$.

A morphism between two locally ringed spaces $(X, \mathcal{O}_X)$ and $(Y, \mathcal{O}_Y)$ is a morphism $(\varphi,\varphi^\sharp)$ of ringed spaces such that, for each $x\in X$, the induced map on stalks $\varphi_x^\sharp:\mathcal{O}_{Y,\varphi(x)} \rightarrow \mathcal{O}_{X,x}$ is a local homomorphism.
:::

## Algebraic functions on $\Spec A$

We now define $\mathcal{O}_{\Spec A}$. As mentioned at the outset, this is the sheaf of algebraic functions on $\Spec A$, and it is precisely the generalization of [[Algebraic Varieties] §Affine Varieties, ⁋Definition 14]](/en/math/algebraic_varieties/affine_varieties#def14).

Let us carry this discussion over to schemes. First, as with algebraic varieties, we regard elements of $A$ as functions $f$. Then the *function value* of $f$ at a point $\mathfrak{p}\in\Spec A$ is the image of $f$ under the canonical projection $\pi: A \rightarrow A/\mathfrak{p}$. In particular, $f$ vanishing at $\mathfrak{p}$ means

$$f\equiv 0\pmod{\mathfrak{p}}\iff f\in \mathfrak{p}\iff \mathfrak{p}\in Z(f)$$

Thus $Z(f)$ can be understood as the locus where $f=0$, and its complement, the principal open set $D(f)$, as the locus where $f\neq 0$.

From this perspective we can describe what the *algebraic functions* on $\Spec A$ are. Just as in [[Algebraic Varieties] §Affine Varieties, ⁋Definition 14]](/en/math/algebraic_varieties/affine_varieties#def14), they are defined to be functions that can be represented, in a suitable neighborhood of each point, as rational functions whose denominators do not vanish on that neighborhood. Note that this condition is local: a single fractional expression valid on the entire open set does not generally exist, and as we shall see below, this is guaranteed only on principal open sets.

Now suppose a principal open set $D(f)$ is given. If we consider only functions representable as a single rational function $g/h$ on all of $D(f)$, then the admissible denominators $h$ must satisfy $D(f)\subseteq D(h)$.

::: Lemma 3
For a fixed element $f\in A$, define

$$S(f)=\{h\in A\mid D(f)\subseteq D(h)\}$$

Then $S(f)$ is a multiplicative subset of $A$.
:::
::: Proof
Since $D(1)=\Spec A$, it is obvious that $S(f)$ contains the empty product $1$. Now if $h_1,h_2\in S(f)$, then from the identity

$$D(h_1h_2)=\Spec A\setminus Z(h_1h_2)=\Spec A\setminus (Z(h_1)\cup Z(h_2))=(\Spec A\setminus Z(h_1))\cap (\Spec A\setminus Z(h_2))=D(h_1)\cap D(h_2)$$

we see that $D(f)\subseteq D(h_1)\cap D(h_2)=D(h_1h_2)$. This identity is merely a geometric interpretation of [[Algebraic Structures] §Field of Fractions, ⁋Proposition 9]](/en/math/algebraic_structures/field_of_fractions#prop9).
:::

It is now intuitively clear, and indeed we shall define it so, that the collection of algebraic functions on the subset $D(f)$ of $\Spec A$ should be $S(f)^{-1}A$. Before doing so, we prove the following lemma.

::: Lemma 4
$D(f)\subseteq D(h)$ holds if and only if there exists $n\geq 1$ such that $f^n\in (h)$.
:::
::: Proof
$D(f)\subseteq D(h)$ is equivalent to $Z(h)\subseteq Z(f)$, which by the third result of [[§Spectrums, ⁋Lemma 6]](/en/math/scheme_theory/spectrums#lem6) is equivalent to $\sqrt{(f)}\subseteq \sqrt{(h)}$.

If $\sqrt{(f)}\subseteq \sqrt{(h)}$, then from $(f)\subseteq \sqrt{(f)}\subseteq \sqrt{(h)}$ we get $f\in \sqrt{(h)}$, so there exists $n\geq 1$ with $f^n\in (h)$. Conversely, if $f^n\in (h)$ for some $n\geq 1$, then $f\in \sqrt{(h)}$, whence $(f)\subseteq \sqrt{(h)}$, and therefore

$$\sqrt{(f)}\subseteq\sqrt{\sqrt{(h)}}=\sqrt{(h)}$$
:::

Using this lemma, we can express $S(f)^{-1}A$ in a cleaner form.

::: Lemma 5
For any $f\in A$, there is an isomorphism

$$S(f)^{-1}A\cong S_f^{-1}A$$

Moreover, if $S(g)\subseteq S(f)$, then the following diagram

{% diagram Math/Scheme_Theory/Affine_Schemes-1.svg width="10.55em" alt="localizations" %}

commutes.
:::
::: Proof
Write the canonical morphisms as $\epsilon(f): A \rightarrow S(f)^{-1}A$ and $\epsilon_f:A \rightarrow S_f^{-1}A$. Since $D(f)=D(f^n)$ for any $n\geq 1$, we have $S_f\subseteq S(f)$, so the image of $S_f$ under $\epsilon(f)$ consists entirely of units in $S(f)^{-1}A$. Conversely, for any $h\in S(f)$, [Lemma 4](#lem4) gives $n\geq 1$ and $a\in A$ with $f^n=ah$, so

$$\frac{h}{1}\frac{a}{f^n}=1\qquad\text{in $S_f^{-1}A$}$$

and thus the image of $S(f)$ under $\epsilon_f$ also consists entirely of units. Therefore, by [[Commutative Algebra] §Localization, ⁋Proposition 6]](/en/math/commutative_algebra/localization#prop6), there exist unique maps

$$\overline{\epsilon_f}: S(f)^{-1}A \rightarrow S_f^{-1}A,\qquad \overline{\epsilon(f)}: S_f^{-1}A \rightarrow S(f)^{-1}A$$

satisfying $\overline{\epsilon_f}\circ\epsilon(f)=\epsilon_f$ and $\overline{\epsilon(f)}\circ\epsilon_f=\epsilon(f)$. Then the two composites $\overline{\epsilon(f)}\circ\overline{\epsilon_f}$ and $\overline{\epsilon_f}\circ\overline{\epsilon(f)}$ each extend $\epsilon(f)$ and $\epsilon_f$, so by the same uniqueness they are identity maps. That is, they are inverses of each other, yielding the claimed isomorphism.

Now suppose $S(g)\subseteq S(f)$. Then elements of $S(g)$ are sent to units by both $\epsilon(f)$ and $\epsilon_f$, and since $S_g\subseteq S(g)$, again by [[Commutative Algebra] §Localization, ⁋Proposition 6]](/en/math/commutative_algebra/localization#prop6) there exist unique maps

$$\widehat{\epsilon(f)}:S(g)^{-1}A \rightarrow S(f)^{-1}A,\qquad \widecheck{\epsilon_f}: S_g^{-1}A \rightarrow S_f^{-1}A$$

extending $\epsilon(f)$ and $\epsilon_f$ respectively, and these are the remaining two arrows of the claimed diagram. Now both composites $\widecheck{\epsilon_f}\circ\overline{\epsilon_g}$ and $\overline{\epsilon_f}\circ\widehat{\epsilon(f)}$ compose with $\epsilon(g)$ to give $\epsilon_f$, so by the same uniqueness they are equal.
:::

Thus, it suffices to regard algebraic functions on $D(f)$ as elements of $S_f^{-1}A$. For convenience, in the previous post we agreed to denote $S_f^{-1}A$ by $A_f$.

::: Lemma 6
For the base $\{D(f)\}_{f\in A}$ of $\Spec A$, define for each $f_i\in A$

$$\mathcal{F}(D(f_i))=S(f_i)^{-1}A\cong A_{f_i}$$

Also, for each $f_i,f_j\in A$ with $D(f_i)\subseteq D(f_j)$, define the restriction map

$$\rho_{ji}: S(f_j)^{-1}(A) \rightarrow S(f_i)^{-1}(A)$$

to be the map obtained by applying [[Commutative Algebra] §Localization, ⁋Proposition 6]](/en/math/commutative_algebra/localization#prop6) to the canonical morphism $A\rightarrow S(f_i)^{-1}(A)$. Then these data satisfy the two conditions of [[Topology] §Sheaves, ⁋Proposition 8]](/en/math/topology/sheaves#prop8), and therefore determine uniquely a ($\cRing$-valued) sheaf $\mathcal{F}$ on $\Spec A$ extending this assignment.
:::
::: Proof
That the $\rho_{ji}$ satisfy the conditions for restriction maps in [[Topology] §Presheaves, ⁋Definition 2]](/en/math/topology/presheaves#def2) is immediate from the universal property of [[Commutative Algebra] §Localization, ⁋Proposition 6]](/en/math/commutative_algebra/localization#prop6). Here, $\rho_{ji}: S(f_j)^{-1}(A) \rightarrow S(f_i)^{-1}(A)$ is, by [Lemma 5](#lem5), simply the map that regards an element of $S(f_j)^{-1}(A)$ written in the form

$$g/h,\qquad\text{where $h\in S(f_j)$}\tag{$\ast$}$$

as an element of $S(f_i)^{-1}(A)$ via the implication

$$h\in S(f_j)\iff D(f_j)\subseteq D(h)\implies D(f_i)\subseteq D(h)\iff h\in S(f_i)$$

We now verify the two conditions of [[Topology] §Sheaves, ⁋Proposition 8]](/en/math/topology/sheaves#prop8). For notational convenience, since $D(f)=\Spec A_f$, it suffices to consider only the case $f=1$ after replacing $A$ by $A_f$. Fix $f_i\in A$ with $\Spec A=\bigcup_{i\in I}D(f_i)$.

First, to verify the first condition, suppose an element $s\in A$ satisfies $s=0$ in $S(f_i)^{-1}A$ for all $i\in I$, and let us show that $s=0$ in $A$. By [[§Spectrums, ⁋Lemma 12]](/en/math/scheme_theory/spectrums#lem12) we can choose $f_1,\ldots, f_n$ from among the $f_i$ such that $\Spec A=\bigcup_{i=1}^n D(f_i)$, and by assumption there exist $m_i\geq 1$ such that

$$f_i^{m_i}s=0$$

for all $i=1,\ldots, n$. On the other hand, from the calculation after [[§Spectrums, ⁋Lemma 11]](/en/math/scheme_theory/spectrums#lem11) we have $D(f_i^{m_i})=D(f_i)$ for all $i$, so

$$\Spec A=\bigcup_{i=1}^n D(f_i^{m_i})$$

and hence there exist $a_i\in A$ with $1=\sum_{i=1}^n a_i f_i^{m_i}$. (See the proof of [[§Spectrums, ⁋Lemma 12]](/en/math/scheme_theory/spectrums#lem12), or the proof of [[Commutative Algebra] §Integral Extension, ⁋Proposition 15]](/en/math/commutative_algebra/integral_extension#prop15).)

Therefore

$$s=1s=\left(\sum_{i=1}^n a_i f_i^{m_i}\right)s=\sum_{i=1}^n a_i (f_i^{m_i}s)=0$$

Now to verify the second condition, suppose for each $i$ there exists $s_i=a_i/f_i^{m_i}\in S(f_i)^{-1}A$ such that for each $i,j$

$$\frac{a_i}{f_i^{m_i}}=\frac{a_j}{f_j^{m_j}}\quad\text{ in }D(f_i)\cap D(f_j)=D(f_if_j)$$

Here, since $a/1=af_i/f_i$, we may choose $m_i\geq 1$ for all $i$. Since $D(f_i)=D(f_i^{m_i})$ and $D(f_j)=D(f_j^{m_j})$,

$$D(f_if_j)=D(f_i)\cap D(f_j)=D(f_i^{m_i})\cap D(f_j^{m_j})=D(f_i^{m_i}f_j^{m_j})$$

so there exists $N_{ij}$ such that

$$(f_i^{m_i}f_j^{m_j})^{N_{ij}}(a_if_j^{m_j}-a_jf_i^{m_i})=0$$

Let $N=\max_{i,j}\{N_{ij}\}$ and obtain

$$(f_i^{m_i}f_j^{m_j})^N(a_if_j^{m_j}-a_jf_i^{m_i})=0$$

that is,

$$a_if_i^{Nm_i}f_j^{Nm_j+m_j}=a_jf_j^{Nm_j}f_i^{Nm_i+m_i}$$

From the given assumption

$$\Spec A=\bigcup_{i=1}^n D(f_i)=\bigcup_{i=1}^n D(f_i^{Nm_i+m_i})$$

we can choose suitable $b_i\in A$ such that

$$1=\sum_{i=1}^n b_if_i^{Nm_i+m_i}$$

Now set $s=\sum_{i=1}^n b_ia_i f_i^{Nm_i}$; then

$$sf_j^{Nm_j+m_j}=\sum_{i=1}^n b_ia_i f_i^{Nm_i} f_j^{Nm_j+m_j}=\sum_{i=1}^nb_ia_jf_j^{Nm_j}f_i^{Nm_i+m_i}=a_jf_j^{Nm_j}$$

so $f_j^{Nm_j}(sf_j^{m_j}-a_j)=0$ holds for all $j$, and hence on $D(f_j)$

$$\frac{s}{1}=\frac{a_j}{f_j^{m_j}}$$

This gives the desired $s$.

If $I$ is infinite, choose a finite subset $J=\{1,\ldots, n\}$ of $I$ with $\Spec A=\bigcup_{j\in J} D(f_j)$ and repeat the above to obtain $s\in \mathcal{F}(\Spec A)$; then we need only show that this also satisfies $s_\alpha=s\vert_{D(f_\alpha)}$ for $D(f_\alpha)$ with $\alpha\in I\setminus J$. To see this, repeat the same process for the finite set

$$J\cup\{\alpha\}=\{1,2,\ldots, n,\alpha\}\subseteq I$$

to obtain $s'\in \mathcal{F}(\Spec A)$. Then by construction $s$ and $s'$ satisfy $s\vert_{D(f_i)}=s'\vert_{D(f_i)}$ for $i=1,\ldots, n$, and since $\Spec A=\bigcup D(f_i)$, the first condition of [[Topology] §Sheaves, ⁋Proposition 8]](/en/math/topology/sheaves#prop8) shown above gives $s=s'$, whence

$$s\vert_{D(f_\alpha)}=s'\vert_{D(f_\alpha)}=s_\alpha$$

This holds for every $\alpha$, so $s$ restricts to $s_\alpha$ on any $D(f_\alpha)$.
:::

::: Definition 7
The sheaf on $\Spec A$ defined by [Lemma 6](#lem6) is denoted $\mathcal{O}_{\Spec A}$ and called the *structure sheaf*.
:::

Although this definition was made only on principal open sets, since the $D(f)$ form a base for $\Spec A$, sections over arbitrary open sets $U$ are determined by the extension in [[Topology] §Sheaves, ⁋Proposition 8]](/en/math/topology/sheaves#prop8). That is, an element of $\mathcal{O}_{\Spec A}(U)$ is data given on $D(f)$ covering $U$ in the form $g/h$ that agree on intersections, which corresponds to the local definition mentioned earlier.

Then $(\Spec A,\mathcal{O}_{\Spec A})$ is a locally ringed space.

::: Lemma 8
For $(\Spec A,\mathcal{O}_{\Spec A})$ and any point $\mathfrak{p}\in \Spec A$, there is an isomorphism

$$A_\mathfrak{p}\cong \mathcal{O}_{\Spec A, \mathfrak{p}}=\varinjlim_\text{\scriptsize $U\ni\mathfrak{p}$ open} \mathcal{O}_{\Spec A}(U)$$

Moreover, for any $f\in A$ with $\mathfrak{p}\in D(f)$, the following diagram

{% diagram Math/Scheme_Theory/Affine_Schemes-7.svg width="14.55em" alt="stalk_and_localization-1" %}

commutes.
:::
::: Proof
By [[Topology] §Topological Bases, ⁋Proposition 2]](/en/math/topology/topological_bases#prop2), the $D(f)$ form a base for $\Spec A$, so by [[Topology] §Topological Bases, ⁋Proposition 5]](/en/math/topology/topological_bases#prop5),

$$\mathcal{O}_{\Spec A, \mathfrak{p}}=\varinjlim_{D(f)\ni\mathfrak{p}} \mathcal{O}_{\Spec A}(D(f))$$

On the other hand, $\mathfrak{p}\in D(f)\iff f\not\in \mathfrak{p}$, so we obtain the following diagram

{% diagram Math/Scheme_Theory/Affine_Schemes-8.svg width="37.01em" alt="stalk_and_localization-2" %}

and thus proving the given isomorphism reduces to showing the algebraic isomorphism

$$A_\mathfrak{p}\cong \varinjlim_{\mathfrak{p}\not\ni f} A_f\tag{$\ast\ast$}$$

which follows from using the universal property of [[Commutative Algebra] §Localization, ⁋Proposition 6]](/en/math/commutative_algebra/localization#prop6) and the universal property of direct limits. The diagram in the claim is obtained by replacing $\varinjlim A_f$ with $A_\mathfrak{p}$ in the above diagram via the isomorphism ($\ast\ast$).
:::

We are now finally ready to write the functoriality of $\Spec$ in the form we want.

::: Proposition 9
The correspondence $A\mapsto (\Spec A, \mathcal{O}_{\Spec A})$ defines a contravariant functor $\Spec: \cRing^\op \rightarrow \LRS$.
:::
::: Proof
We already know that a ring homomorphism $\phi: A \rightarrow B$ induces a continuous map $\Spec\phi: \Spec B \rightarrow \Spec A$. ([[§Spectrums, ⁋Proposition 8]](/en/math/scheme_theory/spectrums#prop8)) Thus it suffices to describe

$$(\Spec\phi)^\sharp: \mathcal{O}_{\Spec A} \rightarrow (\Spec\phi)_\ast \mathcal{O}_{\Spec B}$$

For this we look at the functions on principal open sets

$$(\Spec\phi)^\sharp(D(f)): \mathcal{O}_{\Spec A}(D(f)) \rightarrow \mathcal{O}_{\Spec B}((\Spec \phi)^{-1}(D(f)))$$

Now from the proof of [[§Spectrums, ⁋Proposition 8]](/en/math/scheme_theory/spectrums#prop8),

$$(\Spec\phi)^{-1}(Z(f))=Z(\phi(f))$$

so

$$(\Spec\phi)^{-1}(D(f))=D(\phi(f))$$

Therefore, by the definition of the structure sheaf, defining $(\Spec\phi)^\sharp(D(f))$ is the same as defining

$$A_f \rightarrow B_{\phi(f)}$$

and this is obtained by applying [[Commutative Algebra] §Localization, ⁋Proposition 6]](/en/math/commutative_algebra/localization#prop6) to the composite

$$A \overset{\phi}{\longrightarrow}B \overset{\epsilon}{\longrightarrow} B_{\phi(f)}$$

Of course we must show that these maps commute with restriction maps. If $D(g)\subseteq D(f)$ then $D(\phi(g))\subseteq D(\phi(f))$, and the two composites

$$A_f \longrightarrow B_{\phi(f)} \longrightarrow B_{\phi(g)},\qquad A_f \longrightarrow A_g \longrightarrow B_{\phi(g)}$$

both compose with $\epsilon_f$ to give $A \rightarrow B \rightarrow B_{\phi(g)}$, so by the uniqueness above they are equal.

Now for an arbitrary open set $U\subseteq \Spec A$ and $s\in \mathcal{O}_{\Spec A}(U)$, consider the sections $(\Spec\phi)^\sharp(D(f))(s\vert_{D(f)})$ for each principal open set $D(f)$ contained in $U$. Since the intersection $D(f)\cap D(g)=D(fg)$ of two principal open sets is again principal, the commutativity above shows these sections agree on intersections, and hence by the gluability and identity axioms of the sheaf $(\Spec\phi)_\ast\mathcal{O}_{\Spec B}$ they glue to a unique $(\Spec\phi)^\sharp(U)(s)$. That this $(\Spec\phi)^\sharp(U)$ is a ring homomorphism commuting with restriction maps also follows from the identity axiom, and thus we obtain the sheaf morphism $(\Spec\phi)^\sharp$.

From the above, $(\Spec\phi, (\Spec\phi)^\sharp): (\Spec B, \mathcal{O}_{\Spec B}) \rightarrow (\Spec A, \mathcal{O}_{\Spec A})$ is a morphism of ringed spaces. To show this is a morphism of locally ringed spaces, we need that for any $\mathfrak{q}\in \Spec B$,

$$(\Spec\phi)^\sharp_\mathfrak{q}:\mathcal{O}_{\Spec A, (\Spec \phi)(\mathfrak{q})} \rightarrow\mathcal{O}_{\Spec B, \mathfrak{q}}$$

is a local homomorphism. But $(\Spec \phi)(\mathfrak{q})=\phi^{-1}(\mathfrak{q})$, so by [Lemma 8](#lem8), $(\Spec\phi)^\sharp_\mathfrak{q}$ is a ring homomorphism from $A_{\phi^{-1}(\mathfrak{q})}$ to $B_{\mathfrak{q}}$ sending the unique maximal ideal $\phi^{-1}(\mathfrak{q})A_{\phi^{-1}(\mathfrak{q})}$ of $A_{\phi^{-1}(\mathfrak{q})}$ to the unique maximal ideal $\mathfrak{q}B_\mathfrak{q}$ of $B_\mathfrak{q}$.

Finally, let us verify functoriality. For the map on points this was already checked in [[§Spectrums, ⁋Proposition 2]](/en/math/scheme_theory/spectrums#prop2), so we only need to check the structure sheaf side. When $\phi=\id_A$, the above construction gives, for each $D(f)$, the unique map $A_f \rightarrow A_f$ extending $\epsilon_f$, which is the identity; hence $\Spec(\id_A)=\id$. Also, for two ring homomorphisms $\phi: A \rightarrow B$ and $\psi: B \rightarrow C$, the map $\Spec(\psi\circ\phi)^\sharp(D(f))$ is the unique map extending the composite $A \rightarrow C \rightarrow C_{\psi(\phi(f))}$, and the composite $A_f \rightarrow B_{\phi(f)} \rightarrow C_{\psi(\phi(f))}$ also extends the same map, so by uniqueness they are equal. Since two sheaf morphisms agreeing on a base are equal, $\Spec(\psi\circ\phi)=(\Spec\phi)\circ(\Spec\psi)$.
:::

## Affine scheme

::: Definition 10
The essential image of the functor $\Spec:\cRing^\op \rightarrow \LRS$ from [Proposition 9](#prop9) is called an *affine scheme*.
:::

We write $\AffSch$ for the category of affine schemes. Then the contravariant functor $\Spec:\cRing^\op \rightarrow \AffSch$ is essentially surjective by definition. ([[Category Theory] §Natural Transformations, ⁋Theorem 5]](/en/math/category_theory/natural_transformations#thm5)) Moreover, if $(\varphi, \varphi^\sharp): (\Spec B, \mathcal{O}_{\Spec B}) \rightarrow (\Spec A, \mathcal{O}_{\Spec A})$ is induced from some ring homomorphism $\phi$, then taking $1=f\in A$ in the proof of [Proposition 9](#prop9) gives

$$\varphi^\sharp(D(1))= \bigl(A \overset{\phi}{\longrightarrow} B \overset{\id_B}{\longrightarrow} B_{\phi(1)}=B\bigr)=\phi$$

so this functor is necessarily faithful. Furthermore, the following holds.

::: Proposition 11
The functor $\Spec: \cRing^\op \rightarrow \LRS$ is fully faithful.
:::
::: Proof
 Suppose given any two affine schemes $(X, \mathcal{O}_{X})$, $(Y, \mathcal{O}_{Y})$ and a morphism

$$(X, \mathcal{O}_{X}) \rightarrow (Y, \mathcal{O}_{Y})$$

between them. Via isomorphisms $(\Spec B, \mathcal{O}_{\Spec B})\cong (X, \mathcal{O}_X)$ and $(\Spec A, \mathcal{O}_{\Spec A})\cong (Y, \mathcal{O}_Y)$, we can view this as a morphism

$$(\varphi, \varphi^\sharp): (\Spec B, \mathcal{O}_{\Spec B}) \rightarrow (\Spec A, \mathcal{O}_{\Spec A})$$

between spectra (as locally ringed spaces). Thus it suffices to prove that this morphism of locally ringed spaces comes from some ring homomorphism $\phi$. Taking a hint from the proof of faithfulness above, define a ring homomorphism $\phi:A \rightarrow B$ by

$$\phi=\varphi^\sharp(D(1)):A \rightarrow B$$

To complete the claim we must show $\Spec\phi=(\varphi,\varphi^\sharp)$. First, for any $\mathfrak{q}\in \Spec B$ we show

$$(\Spec \phi)(\mathfrak{q})=\phi^{-1}(\mathfrak{q})=\varphi(\mathfrak{q})$$

Setting $f=1$ in [Lemma 8](#lem8), we obtain the following diagram

{% diagram Math/Scheme_Theory/Affine_Schemes-9.svg width="39.41em" alt="faithful" %}

In this diagram, the vertical maps are all isomorphisms, and we know that all faces except the following one

{% diagram Math/Scheme_Theory/Affine_Schemes-10.svg width="13.26em" alt="commuting_square" %}

are commuting squares. Therefore, in the above diagram $A \rightarrow \mathcal{O}_{\Spec B, \mathfrak{q}}$ is determined identically no matter which path we take, and applying [[Commutative Algebra] §Localization, ⁋Proposition 6]](/en/math/commutative_algebra/localization#prop6) to this map determines $A_{\varphi(\mathfrak{q})} \rightarrow \mathcal{O}_{\Spec B, \mathfrak{q}}$ uniquely. From this we see that *all* faces of the above diagram are commuting squares. That is, $\phi_\mathfrak{q}:A_{\varphi(\mathfrak{q})}\rightarrow B_\mathfrak{q}$ is also a local homomorphism, and hence $\phi^{-1}(\mathfrak{q})=\varphi(\mathfrak{q})$.

Now we show the two sheaf morphisms are equal. Since $\varphi^\sharp$ commutes with restriction maps, for any $f\in A$

$$\varphi^\sharp(D(f))\circ\epsilon_f=\epsilon_{\phi(f)}\circ\phi$$

But in the construction of [Proposition 9](#prop9), $(\Spec\phi)^\sharp(D(f))$ was exactly the unique map satisfying this equation, so by the uniqueness in [[Commutative Algebra] §Localization, ⁋Proposition 6]](/en/math/commutative_algebra/localization#prop6), $\varphi^\sharp(D(f))=(\Spec\phi)^\sharp(D(f))$. Since two sheaf morphisms agreeing on the base $\{D(f)\}_{f\in A}$ are equal, by the identity axiom for $\varphi_\ast\mathcal{O}_{\Spec B}$ we have $\varphi^\sharp=(\Spec\phi)^\sharp$.
:::

Thus, viewing $\Spec$ as a contravariant functor from $\cRing$ to $\AffSch$, it is a categorical equivalence between $\cRing^\op$ and $\AffSch$. Moreover, by [Proposition 11](#prop11), $\AffSch$ is a full subcategory of $\LRS$.

On the other hand, for any spectrum $(\Spec A, \mathcal{O}_{\Spec A})$, by definition we know

$$\mathcal{O}_{\Spec A}(\Spec A)=\mathcal{O}_{\Spec A}(D(1))\cong A$$

If a locally ringed space $(X, \mathcal{O}_X)$ were an affine scheme, we could similarly examine $\mathcal{O}_X(X)$ to see which ring's spectrum $(X, \mathcal{O}_X)$ is isomorphic to. That is, for an affine scheme $(X, \mathcal{O}_X)$, setting $A=\mathcal{O}_X(X)$ gives $(X, \mathcal{O}_X)\cong (\Spec A, \mathcal{O}_{\Spec A})$. More generally, we define:

::: Definition 12
The *global section functor* $\Gamma:\LRS \rightarrow \cRing^\op$ is defined, for any locally ringed space $(X, \mathcal{O}_X)$, by the correspondence

$$X\mapsto \Gamma(X, \mathcal{O}_X)=\mathcal{O}_X(X)$$

and for any morphism $(\varphi,\varphi^\sharp):(X,\mathcal{O}_X) \rightarrow (Y, \mathcal{O}_Y)$, by

$$\Gamma(\varphi,\varphi^\sharp)=\varphi^\sharp(Y):\Gamma(Y, \mathcal{O}_Y) \rightarrow (\varphi_\ast\mathcal{O}_X)(Y)=\Gamma(X, \mathcal{O}_X)$$

[^1]
:::

Here, $\varphi^\sharp(Y)$ is a map in $\cRing$ from $\Gamma(Y)$ to $\Gamma(X)$, which we can read as a map $\Gamma(X) \rightarrow \Gamma(Y)$ in $\cRing^\op$. That this correspondence preserves identities and composition follows from the fact that composition of morphisms of ringed spaces is given by composition of the $\varphi^\sharp$, so this is indeed a functor.

Meanwhile, a notable fact from the proof of [Proposition 11](#prop11) is that the assumption that $(X, \mathcal{O}_X)$ is an affine scheme was unnecessary. That is, even if we drop the assumption $(X, \mathcal{O}_X)\cong(\Spec B, \mathcal{O}_{\Spec B})$ and use the following diagram instead of the one in [Proposition 11](#prop11)

{% diagram Math/Scheme_Theory/Affine_Schemes-11.svg width="34.92em" alt="adjoint" %}

we can carry out a similar argument, where the conclusion's $B$ is replaced by $\Gamma(X, \mathcal{O}_X)$. Since $\mathcal{O}_X$ is data determined by $X$ anyway, abbreviating this as $\Gamma(X)$, we obtain the following theorem.

::: Theorem 13
For any locally ringed space $(X, \mathcal{O}_X)$ and any ring $A$, there exists a natural isomorphism

$$\Hom_\LRS(X, \Spec A)\cong \Hom_{\cRing^\op}(\Gamma(X), A)=\Hom_{\cRing}(A, \Gamma(X))$$

That is, the global section functor $\Gamma: \LRS \rightarrow \cRing^\op$ is the left adjoint of the $\Spec$ functor $\Spec:\cRing^\op \rightarrow \LRS$.
:::
::: Proof
Through the isomorphism $\mathcal{O}_{\Spec A}(D(f))\cong A_f$ from [Lemma 6](#lem6), we identify $\mathcal{O}_{\Spec A}(\Spec A)=\mathcal{O}_{\Spec A}(D(1))$ with $A$. Under this identification, the restriction map $\mathcal{O}_{\Spec A}(\Spec A) \rightarrow \mathcal{O}_{\Spec A}(D(f))$ of $\mathcal{O}_{\Spec A}$ is the canonical morphism $\epsilon_f: A \rightarrow A_f$.

First define two correspondences $\Phi$ and $\Psi$, then show they are inverses of each other. Given a morphism $(\varphi,\varphi^\sharp): X \rightarrow \Spec A$ of locally ringed spaces, evaluating $\varphi^\sharp$ on the open set $\Spec A$ yields the ring homomorphism

$$\Phi(\varphi,\varphi^\sharp)=\varphi^\sharp(\Spec A): A=\mathcal{O}_{\Spec A}(\Spec A) \rightarrow (\varphi_\ast\mathcal{O}_X)(\Spec A)=\mathcal{O}_X(X)=\Gamma(X)$$

Conversely, suppose a ring homomorphism $\phi:A \rightarrow \Gamma(X)$ is given. For each $x\in X$, write $\phi_x:A \rightarrow \mathcal{O}_{X,x}$ for the ring homomorphism obtained by composing $\phi$ with the germ map $\Gamma(X) \rightarrow \mathcal{O}_{X,x}$. That is, $\phi_x(a)=\phi(a)_x$. Since $(X,\mathcal{O}_X)$ is a locally ringed space, $\mathcal{O}_{X,x}$ is a local ring with unique maximal ideal $\mathfrak{m}_x$, so by [[Algebraic Structures] §Field of Fractions, ⁋Proposition 10]](/en/math/algebraic_structures/field_of_fractions#prop10),

$$\varphi(x)=\phi_x^{-1}(\mathfrak{m}_x)$$

is a prime ideal of $A$, i.e., a point of $\Spec A$.

We show this function $\varphi: X \rightarrow \Spec A$ is continuous. To do this, we first show that for any $s\in \Gamma(X)$,

$$X_s=\{x\in X\mid \text{$s_x\not\in \mathfrak{m}_x$}\}$$

is an open set of $X$. By [[Commutative Algebra] §Localization, ⁋Proposition 2]](/en/math/commutative_algebra/localization#prop2), $\mathfrak{m}_x$ consists of all non-units of the local ring $\mathcal{O}_{X,x}$, so $x\in X_s$ is equivalent to $s_x$ being a unit in $\mathcal{O}_{X,x}$. Now if $x\in X_s$, there exists $t\in \mathcal{O}_{X,x}$ with $s_xt=1$, and choosing a suitable open neighborhood $W$ of $x$ and a section $u\in \mathcal{O}_X(W)$ representing $t$, we have $(s\vert_Wu)_x=1_x$, so by shrinking $W$ if necessary we can ensure $s\vert_Wu=1$ in $\mathcal{O}_X(W)$. Then for any $y\in W$, $s_yu_y=1$ so $s_y$ is a unit in $\mathcal{O}_{X,y}$, and hence $W\subseteq X_s$. That is, $X_s$ is open.

On the other hand, for any $f\in A$,

$$\varphi^{-1}(D(f))=\{x\in X\mid f\not\in \varphi(x)\}=\{x\in X\mid \phi(f)_x\not\in \mathfrak{m}_x\}=X_{\phi(f)}$$

and since principal open sets form a base for $\Spec A$ ([[§Spectrums, ⁋Lemma 11]](/en/math/scheme_theory/spectrums#lem11)), $\varphi$ is continuous.

Now we define the sheaf morphism $\varphi^\sharp: \mathcal{O}_{\Spec A} \rightarrow \varphi_\ast \mathcal{O}_X$. For each $f\in A$, set $V_f=\varphi^{-1}(D(f))=X_{\phi(f)}$, and write

$$\theta_f: A\overset{\phi}{\longrightarrow} \Gamma(X) \longrightarrow \mathcal{O}_X(V_f)$$

for the ring homomorphism obtained by composing $\phi$ with the restriction map. Our claim is that $\theta_f(f)=\phi(f)\vert_{V_f}$ is a unit in $\mathcal{O}_X(V_f)$. Indeed, by the definition of $V_f$, for every $y\in V_f$ the element $\phi(f)_y$ is a unit in $\mathcal{O}_{X,y}$, so repeating the argument above we can find an open neighborhood $W_y\subseteq V_f$ of $y$ and $u_y\in \mathcal{O}_X(W_y)$ with $\phi(f)\vert_{W_y}u_y=1$. Then on the intersection $W_y\cap W_{y'}$, the restrictions of $u_y$ and $u_{y'}$ are both multiplicative inverses of $\phi(f)\vert_{W_y\cap W_{y'}}$ and hence equal, so by the gluability axiom of [[Topology] §Sheaves, ⁋Definition 1]](/en/math/topology/sheaves#def1) they glue to a single $u\in \mathcal{O}_X(V_f)$. Now $\phi(f)\vert_{V_f}u$ and $1$ agree on each $W_y$, so by the identity axiom $\phi(f)\vert_{V_f}u=1$.

In particular, $\theta_f$ sends all elements of the multiplicative subset $S_f=\{1,f,f^2,\ldots\}$ to units in $\mathcal{O}_X(V_f)$, so by [[Commutative Algebra] §Localization, ⁋Proposition 6]](/en/math/commutative_algebra/localization#prop6), there exists a unique ring homomorphism

$$\varphi^\sharp(D(f)): A_f=\mathcal{O}_{\Spec A}(D(f)) \rightarrow \mathcal{O}_X(V_f)=(\varphi_\ast\mathcal{O}_X)(D(f))$$

satisfying

$$\varphi^\sharp(D(f))\circ \epsilon_f=\theta_f$$

If $D(g)\subseteq D(f)$ then $V_g\subseteq V_f$, and the two composites

$$A_f \overset{\varphi^\sharp(D(f))}{\longrightarrow} \mathcal{O}_X(V_f) \longrightarrow \mathcal{O}_X(V_g),\qquad A_f \longrightarrow A_g \overset{\varphi^\sharp(D(g))}{\longrightarrow} \mathcal{O}_X(V_g)$$

both compose with $\epsilon_f$ to give $\theta_g$, so again by the uniqueness in [[Commutative Algebra] §Localization, ⁋Proposition 6]](/en/math/commutative_algebra/localization#prop6) they are equal. That is, the $\varphi^\sharp(D(f))$ commute with restriction maps.

Then, just as in the proof of [Proposition 9](#prop9), the maps given on the base extend uniquely to a sheaf morphism $\varphi^\sharp$ by the gluability and identity axioms of $\varphi_\ast\mathcal{O}_X$.

Finally, we show $(\varphi,\varphi^\sharp)$ is a morphism of locally ringed spaces. For any $x\in X$ and $\mathfrak{p}=\varphi(x)$, by [Lemma 8](#lem8) we have $\mathcal{O}_{\Spec A,\mathfrak{p}}\cong A_\mathfrak{p}$, and under this identification the stalk morphism $\varphi_x^\sharp: A_\mathfrak{p} \rightarrow \mathcal{O}_{X,x}$ induced by $\varphi^\sharp$ satisfies, taking germs at $x$ of both sides of the equation $\varphi^\sharp(D(f))\circ\epsilon_f=\theta_f$,

$$\varphi^\sharp_x\circ\epsilon=\phi_x$$

where $\epsilon: A \rightarrow A_\mathfrak{p}$ is the canonical morphism. Now for any $a/s\in A_\mathfrak{p}$, since $s\not\in \mathfrak{p}=\phi_x^{-1}(\mathfrak{m}_x)$, the element $\phi_x(s)$ is a unit, and hence

$$\varphi_x^\sharp(a/s)=\phi_x(a)\phi_x(s)^{-1}$$

In particular, if $a\in \mathfrak{p}$ then $\phi_x(a)\in \mathfrak{m}_x$, so $\varphi_x^\sharp(a/s)\in \mathfrak{m}_x$, and thus the ideal $(\varphi_x^\sharp)^{-1}(\mathfrak{m}_x)$ contains $\mathfrak{p}A_\mathfrak{p}$. On the other hand, $\varphi_x^\sharp(1)=1\not\in \mathfrak{m}_x$ so this ideal is not all of $A_\mathfrak{p}$, and since $\mathfrak{p}A_\mathfrak{p}$ is the unique maximal ideal of $A_\mathfrak{p}$ ([[Commutative Algebra] §Localization, ⁋Proposition 8]](/en/math/commutative_algebra/localization#prop8)),

$$(\varphi_x^\sharp)^{-1}(\mathfrak{m}_x)=\mathfrak{p}A_\mathfrak{p}$$

That is, $\varphi_x^\sharp$ is a local homomorphism, and by [Definition 2](#def2), $\Psi(\phi)=(\varphi,\varphi^\sharp)$ is a morphism of locally ringed spaces.

Now we show $\Phi$ and $\Psi$ are inverses of each other. First, for $\Psi(\phi)=(\varphi,\varphi^\sharp)$, taking $f=1$ gives $D(1)=\Spec A$, $V_1=X$, and $\epsilon_1=\id_A$, so the above construction yields

$$\Phi(\Psi(\phi))=\varphi^\sharp(\Spec A)=\theta_1=\phi$$

Conversely, given a morphism $(\varphi,\varphi^\sharp): X \rightarrow \Spec A$ of locally ringed spaces, let $\phi=\Phi(\varphi,\varphi^\sharp)=\varphi^\sharp(\Spec A)$ and $\Psi(\phi)=(\varphi',(\varphi')^\sharp)$. For any $x\in X$, since $\varphi^\sharp$ commutes with restriction maps, the stalk morphism $\varphi_x^\sharp: \mathcal{O}_{\Spec A, \varphi(x)}\cong A_{\varphi(x)} \rightarrow \mathcal{O}_{X,x}$ induced by $\varphi^\sharp$ satisfies $\varphi_x^\sharp\circ\epsilon=\phi_x$, where $\epsilon: A \rightarrow A_{\varphi(x)}$ being the canonical morphism follows from [Lemma 8](#lem8). On the other hand, since $(\varphi,\varphi^\sharp)$ is a morphism of locally ringed spaces, $\varphi_x^\sharp$ is a local homomorphism, so the ideal $(\varphi_x^\sharp)^{-1}(\mathfrak{m}_x)$ is a proper ideal containing $\varphi(x)A_{\varphi(x)}$, i.e., $\varphi(x)A_{\varphi(x)}$ itself. Therefore, by [[Commutative Algebra] §Localization, ⁋Proposition 8]](/en/math/commutative_algebra/localization#prop8),

$$\varphi'(x)=\phi_x^{-1}(\mathfrak{m}_x)=\epsilon^{-1}\left((\varphi_x^\sharp)^{-1}(\mathfrak{m}_x)\right)=\epsilon^{-1}\left(\varphi(x)A_{\varphi(x)}\right)=\varphi(x)$$

and the two continuous maps $\varphi$ and $\varphi'$ are equal. Now since $\varphi^\sharp$ commutes with restriction maps, for any $f\in A$

$$\varphi^\sharp(D(f))\circ\epsilon_f=\theta_f$$

holds, and this is exactly the equation defining $(\varphi')^\sharp(D(f))$, so by the uniqueness in [[Commutative Algebra] §Localization, ⁋Proposition 6]](/en/math/commutative_algebra/localization#prop6), $\varphi^\sharp(D(f))=(\varphi')^\sharp(D(f))$. Since two sheaf morphisms agreeing on the base $\{D(f)\}_{f\in A}$ are equal, by the identity axiom for $\varphi_\ast\mathcal{O}_X$ we have $\varphi^\sharp=(\varphi')^\sharp$, and hence $\Psi(\Phi(\varphi,\varphi^\sharp))=(\varphi,\varphi^\sharp)$.

Finally, we verify that this bijection is natural. Given a morphism $\psi: X' \rightarrow X$ of locally ringed spaces, computing the composite $(\varphi\circ\psi)^\sharp$ on $\Spec A$ gives $\psi^\sharp(X)\circ\varphi^\sharp(\Spec A)$, so

$$\Phi(\varphi\circ\psi)=\Gamma(\psi)\circ\Phi(\varphi)$$

Also, given a ring homomorphism $\theta: A \rightarrow A'$, from the construction in [Proposition 9](#prop9) with $f=1$ we have $(\Spec\theta)^\sharp(\Spec A)=\theta$, so for any $\varphi: X \rightarrow \Spec A'$,

$$\Phi((\Spec\theta)\circ\varphi)=\Phi(\varphi)\circ\theta$$

That is, the given bijection is natural in both $X$ and $A$, yielding the claimed natural isomorphism.
:::

---
**References**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).

---

[^1]: In general, for any sheaf $\mathcal{F}$ on $X$ we denote $\mathcal{F}(X)$ by $\Gamma(X, \mathcal{F})$.
