---
title: "Algebra of Schemes"
excerpt: "Definitions and properties of reduced schemes and integral schemes"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/algebra_of_schemes
header:
    overlay_image: /assets/images/Math/Algebraic_Varieties/Algebra_of_schemes.png
    overlay_filter: 0.5
sidebar: 
    nav: "scheme_theory-en"

date: 2025-02-05
last_modified_at: 2025-02-11
weight: 6
translated_at: 2026-05-25T10:30:03+00:00
translation_source: kimi-cli
---
A scheme is a geometric and algebraic object at the same time, so to understand it well, we need to consider not only the topological structure of schemes that we studied in previous posts but also their algebraic structure simultaneously, and we briefly saw how this philosophy is reflected in previous posts. In this post, we develop this philosophy further.

## Reduced Schemes and Integral Schemes

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A scheme $$X$$ is a *reduced scheme* if for every open subset $$U$$, $$\mathscr{O}_X(U)$$ is reduced. ([\[Algebraic Structures\] §Field of Fractions, ⁋Definition 11](/en/math/algebraic_structures/field_of_fractions#def11)) Similarly, $$X$$ is *integral* if for every open subset $$U$$, $$\mathscr{O}_X(U)$$ is an integral domain. ([\[Algebraic Structures\] §Field of Fractions, ⁋Definition 5](/en/math/algebraic_structures/field_of_fractions#def5))

</div>

Then the following holds.

<div class="proposition" markdown="1">

<ins id="lem2">**Lemma 2**</ins> A scheme $$X$$ is a reduced scheme if and only if for every $$x\in X$$, the stalk $$\mathscr{O}_{X, x}$$ is a reduced ring.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, for any point $$x\in X$$ of a reduced scheme $$X$$, consider an affine open subscheme $$U=\Spec A$$ containing $$x$$. Let $$\mathfrak{p}$$ be the prime ideal corresponding to $$x$$ in $$\Spec A$$; then

$$\mathscr{O}_{X,x}=(\mathscr{O}_X\vert_U)_x\cong \mathscr{O}_{\Spec A, \mathfrak{p}}\cong A_\mathfrak{p}$$

and by assumption $$\mathscr{O}_X(U)\cong A$$ is reduced, so $$A_\mathfrak{p}$$ is also reduced.

Conversely, suppose $$\mathscr{O}_{X,x}$$ is reduced for every $$x\in X$$. Then for any open subset $$U$$, considering the inclusion

$$\mathscr{O}_X(U)\hookrightarrow\prod_{x\in U} \mathscr{O}_{X,x}$$

we can verify that $$\mathscr{O}_X(U)$$ is reduced.

</details>

From this we see that reducedness is a stalk-local property. ([§Topology of Schemes, ⁋Proposition 16](/en/math/scheme_theory/topology_of_schemes#prop16)) Also, since it is easy to show that if a ring $$A$$ is reduced then so is any localization of it, we can show that the spectrum of a reduced ring is reduced.

Similarly, the spectrum of an integral domain is an integral scheme. This is not difficult to prove directly, but in [Proposition 4](#prop4) we prove that a scheme $$X$$ is integral if and only if $$X$$ is irreducible and reduced. Then the spectrum $$\Spec A$$ of an integral domain $$A$$ is

1. a reduced scheme because $$A$$ is a reduced ring, and
2. irreducible because $$A$$ has a unique minimal prime ideal $$\{0\}$$.

That is, accepting this, we can see that the spectrum of an integral domain is an integral scheme.

For the proof of [Proposition 4](#prop4), it is helpful to express irreducibility in algebraic language as follows.

<div class="proposition" markdown="1">

<ins id="lem3">**Lemma 3**</ins> An affine scheme $$\Spec A$$ is irreducible if and only if its nilradical $$\mathfrak{N}(A)$$ is a prime ideal.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

$$\Spec A$$ is irreducible if and only if for any two basis elements $$D(f),D(g)\neq\emptyset$$, we have $$D(fg)\neq\emptyset$$. From the equivalence

$$D(f)\neq\emptyset\iff f\not\in \mathfrak{p}\text{ for some $\mathfrak{p}$}\iff f\not\in \mathfrak{N}(A)$$

([\[Algebraic Structures\] §Field of Fractions, ⁋Proposition 14](/en/math/algebraic_structures/field_of_fractions#prop14)) we know that the statement $$D(f),D(g)\neq\emptyset\implies D(fg)\not\in\emptyset$$ is equivalent to the statement

$$f,g\not\in \mathfrak{N}(A)\implies fg\not\in \mathfrak{N}(A).$$

</details>

Now we obtain the following.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> $$X$$ is integral if and only if $$X$$ is reduced and irreducible.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, suppose $$X$$ is integral. Since any integral domain is always reduced, $$X$$ is a reduced scheme. If $$X$$ were not an irreducible scheme, then there would exist two disjoint nonempty open subsets $$U_1,U_2\neq\emptyset$$. Then for the open subset $$U_1\cup U_2$$,

$$\mathscr{O}_X(U_1\cup U_2)=\mathscr{O}_X(U_1)\times \mathscr{O}_X(U_2)$$

and the right-hand side is not an integral domain, which contradicts the assumption that $$X$$ is integral.

Conversely, suppose we are given an irreducible reduced scheme $$X$$, and let us show that $$X$$ is an integral scheme. That is, given any open subset $$U$$ of $$X$$, we must show that $$\mathscr{O}_X(U)$$ is an integral domain. First we prove the following claim.

**Claim** For any affine open subset $$\Spec A\cong V\subseteq X$$, $$\mathscr{O}_X(V)\cong A$$ is always an integral domain.
> From the assumption that $$X$$ is reduced, we know that $$A$$ must be a reduced ring. On the other hand, since $$X$$ is an irreducible closed subset of $$X$$, $$V$$ is also irreducible, and ([\[Topology\] §Dimension, ⁋Proposition 13](/en/math/topology/dimension#prop14)) therefore by [Lemma 3](#lem3), $$\mathfrak{N}(A)=0$$ is a prime ideal, so $$A$$ is an integral domain.

Now we show that for a general open subset $$U$$ of $$X$$, $$\mathscr{O}_X(U)$$ is an integral domain. To this end, suppose two elements $$f,g\in \mathscr{O}_X(U)$$ satisfy $$fg=0$$. Then for the two open subsets of $$U$$

$$D_U(f)=\{x\in U\mid f_x\not\in \mathfrak{m}_x\},\qquad D_U(g)=\{x\in U\mid g_x\not\in \mathfrak{m}_x\}$$

and their complements $$Z_U(f), Z_U(g)$$, we have $$U=Z_U(f)\cup Z_U(g)$$. Since $$X$$ is irreducible, by ([\[Topology\] §Dimension, ⁋Proposition 13](/en/math/topology/dimension#prop14)) we know that its open subset $$U$$ is likewise, and therefore either $$Z_U(f)=U$$ or $$Z_U(g)=U$$ must hold. Without loss of generality, suppose $$Z_U(f)=U$$. Then for any open affine subset $$V$$ of $$U$$, defining

$$D_V(f)=\{x\in V\mid f_x\not\in \mathfrak{m}_x\}$$

in $$V$$, we have $$D_V(f)=D_U(f)\cap V=D(f\vert_{U\cap D_U(f)})\subseteq V$$, and for this to be empty, $$f\vert_{U\cap D_U(f)}$$ must be a nilpotent element of $$\mathscr{O}_X(V)$$. However, by the claim above, $$\mathscr{O}_X(V)$$ is an integral domain, so from this we know that $$f\vert_{U\cap D_U(f)}=0$$ must hold, and since this holds for any open affine subset $$V$$ of $$U$$, we must have $$f=0$$.

</details>

On the other hand, looking at [§Topology of Schemes, ⁋Example 6](/en/math/scheme_theory/topology_of_schemes#ex6), we know that the irreducibility of an arbitrary scheme $$X$$ cannot be determined by looking at stalks alone. For example, $$Z(\x(\x-1))$$ splits into two components, so points in each component know nothing about points in the other component. Therefore, integrality also cannot be determined by looking at stalks alone.

However, if $$X$$ were a *connected* scheme, the irreducible components would necessarily meet at some point, and by looking at the stalk at this point we might be able to determine irreducibility. The following proposition makes this idea precise.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> A Noetherian scheme $$X$$ is integral if and only if $$X$$ is nonempty and connected and each stalk $$\mathscr{O}_{X,x}$$ is an integral domain.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, if $$X$$ is integral then $$X$$ is irreducible and hence connected, and since the localization of an integral domain is an integral domain, one direction is obvious.

For the opposite direction, that $$X$$ is reduced is obvious because any integral domain is reduced and reducedness is a stalk-local property. Thus, using the given conditions, it suffices to show that $$X$$ is irreducible; the rest follows from [Proposition 4](#prop4).

First, since $$X$$ is a Noetherian scheme, there exist suitable Noetherian rings $$A_1,\ldots, A_r$$ such that $$X=\bigcup \Spec A_i$$. Also, $$X$$ is Noetherian as a topological space, and therefore by ([\[Topology\] §Dimension, ⁋Proposition 12](/en/math/topology/dimension#prop13)) $$X$$ has finitely many irreducible components. Now, letting

$$X=\bigcup_{j=1}^s X_j\tag{$\ast$}$$

be the decomposition of $$X$$ into irreducible components, for a fixed $$i$$, among the sets

$$X_1\cap \Spec A_i,\quad X_2\cap \Spec A_i,\quad\ldots,\quad X_s\cap \Spec A_i$$

the nonempty ones become the irreducible components of $$\Spec A_i$$. Now by [§Spectra, ⁋Proposition 16](/en/math/scheme_theory/spectrums#prop16), each of these defines a minimal prime ideal $$\mathfrak{q}_j=I(X_j)$$, and conversely any minimal prime ideal of $$A_i$$ uniquely determines an irreducible component $$X_j\cap \Spec A_i$$.

On the other hand, since $$X$$ is connected, considering the intersection

$$X_1\cap \bigcup_{j=2}^s X_j$$

in the irreducible decomposition ($$\ast$$), this is the intersection of two nonempty open subsets of $$X$$, and since $$X$$ is connected they must meet at some point $$x$$. That is, there exists a suitable $$j$$ such that $$x\in X_1\cap X_j$$. Now let $$\Spec A_i$$ be an affine cover of $$X$$ containing the point $$x$$, and suppose $$x$$ corresponds to a prime ideal $$\mathfrak{p}$$. That is,

$$x\in \Spec A_i\cap X_1\cap X_j=(\Spec A_i\cap X_1)\cap (\Spec A_i\cap X_j).$$

Now from the preceding argument, $$\Spec A_i\cap X_1$$ has generic point $$\mathfrak{q}_1$$, and $$\Spec A_i\cap X_j$$ has generic point $$\mathfrak{q}_j$$, and these are minimal prime ideals of $$A_i$$. Now considering the stalk at $$x$$, $$\mathscr{O}_{X,x}\cong (A_i)_\mathfrak{p}$$, by the minimality of $$\mathfrak{q}_1,\mathfrak{q}_2$$ we have $$\mathfrak{q}_1,\mathfrak{q}_2\subseteq \mathfrak{p}$$, and therefore $$\mathfrak{q}_1 A_i, \mathfrak{q}_2 A_i$$ become minimal prime ideals of $$A_i$$. ([\[Commutative Algebra\] §Localization, ⁋Proposition 8](/en/math/commutative_algebra/localization#prop8)) However, an integral domain has a unique minimal prime ideal $$(0)$$, so this contradicts the assumption that $$\mathscr{O}_{X,x}$$ is an integral domain.

</details>

The key logic in the above proof can be summarized as follows:

1. Since $$X$$ is connected, if we decompose $$X$$ into irreducible components, each irreducible component must meet another irreducible component[^1]
2. Let $$x$$ be a point where two irreducible components meet; then any open neighborhood of $$x$$ will contain the generic point of each irreducible component ([§Spectra, ⁋Proposition 16](/en/math/scheme_theory/spectrums#prop16)),
3. Therefore these generic points survive in the stalk $$\mathscr{O}_{X,x}$$ at $$x$$, but this is impossible since $$\mathscr{O}_{X,x}$$ is an integral domain.

We will examine this property of generic points at the end of this post.

## Normal Schemes

Similarly to integral schemes, we can define the following.

<div class="definition" markdown="1">

<ins id="def6">**Definition 6**</ins> A scheme $$X$$ is *normal* if for every $$x\in X$$, the stalk $$\mathscr{O}_{X,x}$$ is a normal domain. ([\[Commutative Algebra\] §Integral Extensions, ⁋Definition 3](/en/math/commutative_algebra/integral_extension#def3))

</div>

In general, the localization of a normal domain is always a normal domain. ([\[Commutative Algebra\] §Integral Extensions, ⁋Proposition 12](/en/math/commutative_algebra/integral_extension#prop12)) From this we know that the spectrum $$\Spec A$$ of a normal domain $$A$$ is a normal scheme.

Any integral domain is always reduced, and since reducedness can be checked on stalks by [Lemma 2](#lem2), any normal scheme is reduced. On the other hand, since being an integral scheme is not a stalk-local property, a normal scheme is not generally an integral scheme. However, if $$X$$ is a connected, nonempty Noetherian scheme, then by [Proposition 5](#prop5) we know that normality implies integrality.

On the other hand, we know that a unique factorization domain is always a normal domain. ([\[Commutative Algebra\] §Integral Extensions, ⁋Proposition 9](/en/math/commutative_algebra/integral_extension#prop9)) From this we define the following.

<div class="definition" markdown="1">

<ins id="def7">**Definition 7**</ins> A scheme $$X$$ is *factorial* if for every $$x\in X$$, the stalk $$\mathscr{O}_{X,x}$$ is a unique factorization domain.

</div>

Therefore any factorial scheme is a normal scheme. Also, since the localization of a unique factorization domain is a unique factorization domain, the spectrum $$\Spec A$$ of a unique factorization domain $$A$$ is factorial.

## Associated Points

By [§Spectra, ⁋Corollary 17](/en/math/scheme_theory/spectrums#cor17), we know that there is a one-to-one correspondence between the irreducible components of a scheme $$X=\Spec A$$ and the minimal prime ideals of the ring $$A$$. This was used importantly in [Proposition 5](#prop5) above.

On the other hand, algebraically, a minimal prime ideal is always an associated prime ideal. This can be checked by viewing the ring $$A$$ as a module over itself: since $$\ann A=\{0\}$$, we apply ([\[Commutative Algebra\] §Associated Primes, ⁋Theorem 7](/en/math/commutative_algebra/associated_primes#thm7)). Therefore we define the associated points of a (locally Noetherian) scheme as follows.

<div class="definition" markdown="1">

<ins id="def8">**Definition 8**</ins> For a point $$x$$ of a locally Noetherian scheme $$X$$ and an affine open neighborhood $$U\cong \Spec A$$ of $$x$$, we say that $$x$$ is an *associated point* of $$X$$ if the prime ideal $$\mathfrak{p}_x\subset A$$ corresponding to $$x$$ is an associated prime ideal of $$A$$.

</div>

Then this definition does not depend on the choice of $$U$$, and moreover can be expressed stalk-locally. This is because, for an affine open neighborhood $$\Spec A$$ containing $$x$$, assuming $$A$$ is a Noetherian ring from the condition that $$X$$ is a locally Noetherian scheme, from the third condition of ([\[Commutative Algebra\] §Associated Primes, ⁋Theorem 7](/en/math/commutative_algebra/associated_primes#thm7)) we know that there is a one-to-one correspondence between the set of associated prime ideals of $$A$$ contained in $$\mathfrak{p}_x$$ and the associated prime ideals of $$A_{\mathfrak{p}_x}$$, and from this correspondence [Definition 8](#def8) can be rewritten as:

> For a point $$x$$ of a locally Noetherian scheme $$X$$, we say that $$x$$ is an *associated point* of $$X$$ if $$\mathfrak{m}_x$$ is an associated prime ideal of $$\mathscr{O}_{X,x}$$.

Now the first condition of ([\[Commutative Algebra\] §Associated Primes, ⁋Theorem 7](/en/math/commutative_algebra/associated_primes#thm7)) also guarantees the finiteness of associated points when $$X$$ is a quasicompact locally Noetherian scheme, that is, when $$X$$ is a Noetherian scheme.

Also, by this condition, since any minimal prime ideal is an associated prime ideal, this notion generalizes the concept of generic points on $$\Spec A$$. By [Definition 8](#def8) we may restrict our attention to the spectrum $$\Spec A$$ of a Noetherian ring.

<div class="definition" markdown="1">

<ins id="def9">**Definition 9**</ins> Among the associated points of the spectrum $$\Spec A$$ of a Noetherian ring, those that do not correspond to the generic points of the irreducible components of $$\Spec A$$ are called *embedded points*.

</div>

On the other hand, the following holds by definition.

<div class="proposition" markdown="1">

<ins id="prop10">**Proposition 10**</ins> The associated points of the spectrum $$\Spec A$$ of a Noetherian ring are precisely the generic points of the irreducible components of $$\supp(f)$$ for suitable $$f\in A$$, and conversely.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, for any $$g\in A$$ and prime ideal $$\mathfrak{q}\in \Spec A$$,

$$\mathfrak{q}\in \supp(g)\iff g_\mathfrak{q}\neq 0\text{ in $A_\mathfrak{q}$}\iff \ann(g_\mathfrak{q})\neq A_\mathfrak{q}$$

holds. Now by ([\[Commutative Algebra\] §Localization, ⁋Proposition 5](/en/math/commutative_algebra/localization#prop5))

$$\ann(g_\mathfrak{q})=\ann(g)A_\mathfrak{q}$$

so the last condition is equivalent to $$\ann(g)\setminus \mathfrak{q}=\emptyset$$, that is, $$\mathfrak{q}\in Z(\ann(g))$$. From this we know that for any $$g\in A$$,

$$\supp(g)=Z(\ann(g))$$

holds. Therefore there is a one-to-one correspondence between the irreducible components of $$\supp(g)$$ and the minimal prime ideals containing $$\ann(g)$$.

Now given any associated point $$\mathfrak{p}$$ of $$\Spec A$$, by definition there exists a suitable $$f\in A$$ such that $$\mathfrak{p}=\ann(f)$$. Now

$$\supp(f)=Z(\ann(f))=Z(\mathfrak{p})$$

and since it is obvious that $$\mathfrak{p}$$ is a minimal prime of $$\ann(f)=\mathfrak{p}$$, we see that $$\mathfrak{p}$$ is a generic point of $$\supp f$$. This argument works in the reverse direction as well, based on the observation above.

</details>

Looking at the formula

$$\supp(f)=Z(\ann(f))$$

used in the proof above, if $$A$$ were an integral domain then $$\ann(f)$$ is all of $$A$$ only when $$f=0$$, and is $$0$$ otherwise. That is, in this case $$\supp(f)$$ is empty only when $$f=0$$, and is all of $$\Spec A$$ otherwise, and since we know from [Proposition 4](#prop4) that $$\Spec A$$ is irreducible, we know that the only associated point of $$\Spec A$$ is the generic point $$(0)$$.

More generally, if $$A$$ is not an integral domain, there exist cases where $$\ann(f)$$ is neither $$0$$ nor $$A$$, so the possibility of embedded points exists.

<div class="example" markdown="1">

<ins id="ex11">**Example 11**</ins> Consider the affine scheme $$X=\Spec \mathbb{K}[\x_1,\x_2]/(\x_2^2, \x_1\x_2)$$. Then by [§Spectra, ⁋Lemma 6](/en/math/scheme_theory/spectrums) and [§Spectra, ⁋Proposition 9](/en/math/scheme_theory/spectrums#prop9), as a set

$$X= Z(\x_2^2,\x_1\x_2)=Z(\x_2^2)\cap Z(\x_1\x_2)=\{(0,0)\}.$$

</div>

## Rational Functions

Now we define rational functions defined on a scheme. First, by the second result of ([\[Commutative Algebra\] §Associated Primes, ⁋Corollary 4](/en/math/commutative_algebra/associated_primes#cor4)), we know that the map

$$A \rightarrow \prod_\text{\scriptsize $\mathfrak{p}$ associated prime} A_\mathfrak{p}$$

is injective. Therefore for any open subset $$U$$ of a locally Noetherian scheme $$X$$, the map

$$\Gamma(U, \mathscr{O}_X) \rightarrow \prod_\text{\scriptsize $x$ associated in $U$} \mathscr{O}_{X,x}\tag{$\ast$}$$

is injective.

<div class="definition" markdown="1">

<ins id="def12">**Definition 12**</ins> For a locally Noetherian scheme $$X$$ and an open subset $$U$$ containing all associated points of $$X$$, we call the image of $$\Gamma(U, \mathscr{O}_X)$$ under ($$\ast$$) a *rational function* defined on $$X$$.

</div>

Therefore, by definition, a rational function defined on $$X$$ consists of the data of (1) a *domain of definition* $$U$$ containing all associated points of $$X$$, and (2) a function $$f\in \Gamma(U, \mathscr{O}_X)$$ on it, and two such pairs $$(U, f)$$ and $$(U',f')$$ define the same function if $$f$$ and $$f'$$ define the same function on $$U\cap U'$$.

<div class="example" markdown="1">

<ins id="ex13">**Example 13**</ins> Consider the affine scheme $$X=\Spec \mathbb{K}[\x_1,\x_2]/(\x_2-\x_1^2)$$. Then $$X$$ has a unique associated prime $$(0)$$, and any open subset of $$X$$ contains this point, so a rational function on $$X$$ consists of any nonempty open subset $$U$$ and a function $$f\in\Gamma(U, \mathscr{O}_X)$$ on it.

On the other hand, we know that any (nonempty) open subset of an affine scheme $$X=\Spec A$$ is of the form $$\Spec A_f$$ for a suitable nonzero $$f\in A$$, and the functions on it are given by $$A_f$$. For example, in this example if we choose $$f$$ to be the image of $$\x_1$$ in $$A$$, then by the isomorphism

$$\left(\frac{\mathbb{K}[\x_1,\x_2]}{(\x_2-\x_1^2)}\right)_{\x_1}\cong\frac{\mathbb{K}[\x_1,\x_2]_{\x_1}}{(\x_2-\x_1^2)_{\x_1}}$$

functions such as $$1/\x_1$$ defined on the open subset $$\Spec A_{\x_1}$$ become rational functions on $$X$$. Through this we know that all rational expressions not having $$\x_2-\x_1^2$$ as a factor in the denominator become rational functions on $$X$$ (on a suitable open subset).

</div>

The collection of rational functions defined on a locally Noetherian scheme $$X$$ defines the *total quotient ring* $$K(X)$$. Now, as above, suppose $$X$$ is an integral scheme. Then in particular $$X$$ is irreducible, so it has a unique generic point $$x$$. This point must correspond to the unique minimal prime ideal $$(0)$$ of the integral domain $$A$$ for any affine open subset $$U\cong\Spec A$$. The localization at this point is obtained by adding all nonzero elements of $$A$$ to the denominator, that is, it is the same as $$\Frac(A)$$.

---
**References**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).  

---
[^1]: In this process we used the fact that each component is an open subset because there are finitely many irreducible components of $$X$$.
