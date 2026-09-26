---
title: "Algebraic Structure of Schemes"
description: "This post explores the algebraic structure of schemes, examining the definitions and properties of reduced and integral schemes and proving that reducedness is a stalk-local property. It also shows that an integral scheme is equivalent to an irreducible reduced scheme."
excerpt: "Definitions and properties of reduced and integral schemes"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/algebra_of_schemes
sidebar: 
    nav: "scheme_theory-en"

date: 2025-02-05
weight: 7
translated_at: 2026-09-26T11:15:05+00:00
translation_source: antigravity-gemini-3.8-flash-high
---
Since schemes are both geometric and algebraic objects, to understand them well we need to consider not only the topological structure of schemes examined in the previous post, but also their algebraic structure simultaneously, and we briefly saw how this philosophy is reflected in the previous post. In this post, we develop this philosophy further. 

## Reduced Schemes and Integral Schemes

::: Definition 1
A scheme $X$ is a *reduced scheme* if $\mathcal{O}_X(U)$ is reduced for every open set $U$. ([\[Algebraic Structures\] §Field of Fractions, ⁋Definition 12](/en/math/algebraic_structures/field_of_fractions#def12){: data-lid="e4nuc" }) Similarly, $X$ is *integral* if $X\neq\emptyset$ and $\mathcal{O}_X(U)$ is an integral domain for every non-empty open set $U$. ([\[Algebraic Structures\] §Field of Fractions, ⁋Definition 5](/en/math/algebraic_structures/field_of_fractions#def5){: data-lid="e8cts" })
:::

Then the following holds.

::: Lemma 2
A scheme $X$ is a reduced scheme if and only if $\mathcal{O}_{X, x}$ is a reduced ring for every $x\in X$.
:::
::: Proof
First, for any point $x\in X$ of a reduced scheme $X$, consider an affine open subscheme $U=\Spec A$ containing $x$. If we let $\mathfrak{p}$ be the prime ideal corresponding to $x$ in $\Spec A$, then

$$\mathcal{O}_{X,x}=(\mathcal{O}_X\vert_U)_x\cong \mathcal{O}_{\Spec A, \mathfrak{p}}\cong A_\mathfrak{p}$$

and since $\mathcal{O}_X(U)\cong A$ is reduced by assumption, $A_\mathfrak{p}$ is also reduced. 

Conversely, suppose that $\mathcal{O}_{X,x}$ is reduced for every $x\in X$. Then for any open set $U$, considering the inclusion

$$\mathcal{O}_X(U)\hookrightarrow\prod_{x\in U} \mathcal{O}_{X,x}$$

shows that $\mathcal{O}_X(U)$ is reduced. 
:::

From this, we see that reducedness is a stalk-local property. ([§The Topology of Schemes, ⁋Proposition 16](/en/math/scheme_theory/topology_of_schemes#prop16){: data-lid="jn7hv" }) Also, if a ring $A$ is reduced, it is easy to show that its localization is also reduced, and thus we can show that the spectrum of a reduced ring is reduced. 

Similarly, the spectrum of an integral domain is an integral scheme. While showing this directly is not difficult, in [Proposition 4](#prop4){: data-lid="yx1e6" } we prove that a scheme $X$ is integral if and only if the scheme $X$ is an irreducible, reduced scheme. Then the spectrum $\Spec A$ of an integral domain $A$ is:

1. a reduced scheme since $A$ is a reduced ring, and
2. irreducible since $A$ has the unique minimal prime ideal $\{0\}$.

That is, if we accept this, we see that the spectrum of an integral domain is an integral scheme. 

To prove [Proposition 4](#prop4){: data-lid="h8chk" }, it is useful to rephrase irreducibility in algebraic terms as follows.

::: Lemma 3
An affine scheme $\Spec A$ is irreducible if and only if the nilradical $\mathfrak{N}(A)$ is a prime ideal.
:::
::: Proof
That $\Spec A$ is irreducible is equivalent to $D(fg)\neq\emptyset$ for any two basis elements $D(f),D(g)\neq\emptyset$ of this space. However, from the equivalence

$$D(f)\neq\emptyset\iff f\not\in \mathfrak{p}\text{ for some $\mathfrak{p}$}\iff f\not\in \mathfrak{N}(A)$$

([\[Algebraic Structures\] §Field of Fractions, ⁋Proposition 15](/en/math/algebraic_structures/field_of_fractions#prop15){: data-lid="d7i7i" }), we see that the statement $D(f),D(g)\neq\emptyset\implies D(fg)\neq\emptyset$ is equivalent to the statement that

$$f,g\not\in \mathfrak{N}(A)\implies fg\not\in \mathfrak{N}(A)$$

holds. 
:::

Now we obtain the following.

::: Proposition 4
$X$ is integral if and only if $X$ is reduced and irreducible.
:::
::: Proof
First, suppose that $X$ is integral. Since any integral domain is always reduced, $X$ is a reduced scheme. If $X$ were not an irreducible scheme, there would exist two disjoint non-empty open sets $U_1,U_2\neq\emptyset$. Then for the open set $U_1\cup U_2$,

$$\mathcal{O}_X(U_1\cup U_2)=\mathcal{O}_X(U_1)\times \mathcal{O}_X(U_2)$$

and since the right-hand side is not an integral domain, this contradicts the assumption that $X$ is integral.

Conversely, suppose that an irreducible reduced scheme $X$ is given, and we show that $X$ is an integral scheme. That is, given any open set $U$ of $X$, we must show that $\mathcal{O}_X(U)$ is an integral domain. First, we show the following claim.

> **Claim.** For any affine open subset $\Spec A\cong V\subseteq X$, $\mathcal{O}_X(V)\cong A$ is always an integral domain.  
> **Proof.** From the assumption that $X$ is reduced, we know that $A$ must be a reduced ring. On the other hand, since $X$ is an irreducible closed subset of $X$, $V$ is also irreducible ([\[Topology\] §Dimension, ⁋Proposition 15](/en/math/topology/dimension#prop15){: data-lid="sfrt1" }), and therefore by [Lemma 3](#lem3){: data-lid="e92g1" }, $\mathfrak{N}(A)=0$ is a prime ideal, so $A$ is an integral domain. 

Now, in general, we show that $\mathcal{O}_X(U)$ is an integral domain for any open set $U$ of $X$. To this end, suppose that two elements $f,g\in \mathcal{O}_X(U)$ satisfy $fg=0$. Then for the two open sets of $U$

$$D_U(f)=\{x\in U\mid f_x\not\in \mathfrak{m}_x\},\qquad D_U(g)=\{x\in U\mid g_x\not\in \mathfrak{m}_x\}$$

and their complements $Z_U(f), Z_U(g)$, the equality $U=Z_U(f)\cup Z_U(g)$ holds. Now since $X$ is irreducible, we know by [\[Topology\] §Dimension, ⁋Proposition 15](/en/math/topology/dimension#prop15){: data-lid="e4aa0" } that its open set $U$ is also irreducible, and thus either $Z_U(f)=U$ or $Z_U(g)=U$. Without loss of generality, assume $Z_U(f)=U$. Then for any open affine subset $V$ of $U$, if we define on $V$

$$D_V(f)=\{x\in V\mid f_x\not\in \mathfrak{m}_x\}$$

then $D_V(f)=D_U(f)\cap V$, and for this to be empty, $f\vert_V$ must be a nilpotent element of $\mathcal{O}_X(V)$. However, $\mathcal{O}_X(V)$ is an integral domain by the claim above, so from this we know that $f\vert_V=0$, and since this holds for every open affine subset $V$ of $U$, it follows that $f=0$. 
:::

Meanwhile, looking at [§The Topology of Schemes, ⁋Example 6](/en/math/scheme_theory/topology_of_schemes#ex6){: data-lid="bydim" }, we know that the irreducibility of an arbitrary scheme $X$ cannot be determined solely by looking at the stalks. For instance, since $Z(\x(\x-1))$ decomposes into two components, a point in each component does not have information about points in the other component. Therefore, integrality also cannot be determined solely by looking at the stalks. 

However, if $X$ were a *connected* scheme, the irreducible components would necessarily meet at some point, and looking at the stalk at this point might allow one to determine irreducibility. The following proposition formulates this idea rigorously.

::: Proposition 5
A Noetherian scheme $X$ is integral if and only if $X$ is nonempty, connected, and each $\mathcal{O}_{X,x}$ is an integral domain. 
:::
::: Proof
First, if $X$ is integral, then $X$ is irreducible and hence connected, and since the localization of an integral domain is an integral domain, one direction is clear.

For the converse, that the scheme $X$ is reduced is clear because any integral domain is reduced and reducedness is a stalk-local property. Therefore, if we use the given conditions to show that $X$ is irreducible, the rest is clear from [Proposition 4](#prop4){: data-lid="pm5t4" }.

First, since $X$ is a Noetherian scheme, there exist Noetherian rings $A_1,\ldots, A_r$ such that $X=\bigcup \Spec A_i$. Moreover, $X$ is Noetherian as a topological space, and hence by [\[Topology\] §Dimension, ⁋Proposition 13](/en/math/topology/dimension#prop13){: data-lid="h9alj" }, $X$ has finitely many irreducible components. Now if

$$X=\bigcup_{j=1}^s X_j\tag{$\ast$}$$

is the decomposition of $X$ into irreducible components, then for a fixed $i$, among the sets

$$X_1\cap \Spec A_i,\quad X_2\cap \Spec A_i,\quad\ldots,\quad X_s\cap \Spec A_i$$

those that are nonempty are the irreducible components of $\Spec A_i$. Now by [§The Spectrum, ⁋Corollary 17](/en/math/scheme_theory/spectrums#cor17){: data-lid="a5n1s" }, each of these defines a minimal prime ideal $\mathfrak{q}_j=I(X_j\cap \Spec A_i)$, and conversely, any minimal prime ideal of $A_i$ uniquely determines an irreducible component $X_j\cap \Spec A_i$.

On the other hand, if $s=1$, then $X$ is already irreducible, so there is nothing to prove. Thus assume $s\geq 2$, and consider the two closed sets

$$X_1,\qquad \bigcup_{j=2}^s X_j$$

in the irreducible decomposition ($\ast$). An irreducible component is always a nonempty closed set ([\[Topology\] §Dimension, ⁋Definition 9](/en/math/topology/dimension#def9){: data-lid="sn5z9" }), and since a finite union of closed sets is closed, these are both nonempty closed sets. If these two sets were disjoint, $X$ would be the union of two disjoint closed sets, so each of them would also be open, contradicting the assumption that $X$ is connected. Therefore, there exist some $j$ and a point $x$ such that $x\in X_1\cap X_j$. Now let an affine open containing the point $x$ in the affine cover of $X$ be $\Spec A_i$, and suppose that $x$ corresponds to the prime ideal $\mathfrak{p}$. That is,

$$x\in \Spec A_i\cap X_1\cap X_j=(\Spec A_i\cap X_1)\cap (\Spec A_i\cap X_j)$$

Now from the previous argument, $\Spec A_i\cap X_1$ has generic point $\mathfrak{q}_1$ and $\Spec A_i\cap X_j$ has generic point $\mathfrak{q}_j$, which are minimal prime ideals of $A_i$. Now consider the stalk at $x$, $\mathcal{O}_{X,x}\cong (A_i)_\mathfrak{p}$. Since $x$ belongs to both $X_1$ and $X_j$, we have $\mathfrak{q}_1,\mathfrak{q}_j\subseteq \mathfrak{p}$, and therefore by [\[Commutative Algebra\] §Localization, ⁋Proposition 8](/en/math/commutative_algebra/localization#prop8){: data-lid="bvwya" }, $\mathfrak{q}_1(A_i)_\mathfrak{p}$ and $\mathfrak{q}_j(A_i)_\mathfrak{p}$ are distinct minimal prime ideals of $(A_i)_\mathfrak{p}\cong\mathcal{O}_{X,x}$. However, an integral domain has a unique minimal prime ideal $(0)$, so this contradicts the assumption that $\mathcal{O}_{X,x}$ is an integral domain.
:::

The key logic in the above proof can be summarized as follows:

1. Since $X$ is connected, when $X$ is decomposed into irreducible components, each irreducible component must intersect another irreducible component;[^1]
2. if we let $x$ be a point where two irreducible components intersect, any open neighborhood of $x$ will contain the generic point of each irreducible component ([§The Spectrum, ⁋Proposition 16](/en/math/scheme_theory/spectrums#prop16){: data-lid="ae6cb" }); and
3. therefore, these generic points also survive in the stalk at $x$, $\mathcal{O}_{X,x}$, but this is impossible since $\mathcal{O}_{X,x}$ is an integral domain.

We will examine this property of generic points at the end of this post.

## Normal Schemes

Similarly to integral schemes, we can define the following.

::: Definition 6
A scheme $X$ is *normal* if for every $x\in X$, $\mathcal{O}_{X,x}$ is a normal domain. ([\[Commutative Algebra\] §Integral Extensions, ⁋Definition 3](/en/math/commutative_algebra/integral_extension#def3){: data-lid="vse57" })
:::

In general, a localization of a normal domain is always a normal domain. ([\[Commutative Algebra\] §Integral Extensions, ⁋Proposition 12](/en/math/commutative_algebra/integral_extension#prop12){: data-lid="popqy" }) From this, we see that for a normal domain $A$, its spectrum $\Spec A$ is a normal scheme. 

Any integral domain is always reduced, and since reducedness can be checked on stalks by [Lemma 2](#lem2){: data-lid="y4iu0" }, any normal scheme is reduced. On the other hand, being an integral scheme is not a stalk-local property, so in general a normal scheme is not always an integral scheme. However, if $X$ is a connected, nonempty Noetherian scheme, we know by [Proposition 5](#prop5){: data-lid="54xij" } that normality implies integrality. 

Meanwhile, we know that a unique factorization domain is always a normal domain. ([\[Commutative Algebra\] §Integral Extensions, ⁋Proposition 9](/en/math/commutative_algebra/integral_extension#prop9){: data-lid="grefg" }) From this, we make the following definition.

::: Definition 7
A scheme $X$ is *factorial* if for every $x\in X$, $\mathcal{O}_{X,x}$ is a unique factorization domain.
:::

Therefore, any factorial scheme is a normal scheme. Also, since a localization of a unique factorization domain is a unique factorization domain, for a unique factorization domain $A$, its spectrum $\Spec A$ is factorial. 

## Associated Primes

By [§The Spectrum, ⁋Corollary 17](/en/math/scheme_theory/spectrums#cor17){: data-lid="ig8xj" }, we know that there is a one-to-one correspondence between the irreducible components of a scheme $X=\Spec A$ and the minimal prime ideals of the ring $A$. This was crucially used in [Proposition 5](#prop5){: data-lid="xer9g" } above.

Algebraically, on the other hand, a minimal prime ideal of a Noetherian ring $A$ is always an associated prime ideal. This can be verified by viewing $A$ as a module over itself, in which case $\ann A=\{0\}$, and applying [\[Commutative Algebra\] §Associated Primes of Ideals, ⁋Theorem 7](/en/math/commutative_algebra/associated_primes#thm7){: data-lid="hfvnw" }. The Noetherian hypothesis is essential: for instance, $A=\mathbb{K}[\x_1,\x_2,\ldots]/(\x_1^2,\x_2^2,\ldots)$ has a unique prime ideal $\mathfrak{m}=(\x_1,\x_2,\ldots)$, but since any nonzero element of $A$ uses only finitely many variables, for an unused $\x_j$ we have $\x_jf\neq 0$, so we cannot have $\ann(f)=\mathfrak{m}$, and therefore $\Ass(A)=\emptyset$.

However, associated prime ideals contain more information than minimal primes. For a Noetherian ring $A$, according to the second result of [\[Commutative Algebra\] §Associated Primes of Ideals, ⁋Theorem 7](/en/math/commutative_algebra/associated_primes#thm7){: data-lid="x17sx" }, the union of the associated primes of $A$ is precisely the set consisting of $0$ and the zero-divisors of $A$. For instance, in the case of $Z(\x\y)$ seen in [§The Topology of Schemes, ⁋Example 6](/en/math/scheme_theory/topology_of_schemes#ex6){: data-lid="kiqwh" }, the zero-divisors $\x,\y$ were functions that are $0$ on each of the distinct irreducible components, and that zero-divisor relationship was already completely explained solely by the minimal primes $(\x),(\y)$, the generic points of the two components. However, as seen in [Example 11](#ex11){: data-lid="4ju2l" } below, this is not always the case, and associated points capture all the locations of zero-divisors that are missed by minimal primes, that is, by generic points of irreducible components alone.

::: Definition 8
For a locally Noetherian scheme $X$, a point $x$, and an affine open neighborhood of $x$, $U\cong \Spec A$, we say that $x$ is an *associated point* of $X$ if the prime ideal corresponding to $x$, $\mathfrak{p}_x\subseteq A$, is an associated prime ideal of $A$. 
:::

Then this definition does not depend on the choice of $U$, and furthermore, it can be written stalk-locally. This is because, first, for an affine open neighborhood of $x$, say $\Spec A$, if we assume from the condition that $X$ is a locally Noetherian scheme that $A$ is a Noetherian ring, we know from the third condition of [\[Commutative Algebra\] §Associated Primes of Ideals, ⁋Theorem 7](/en/math/commutative_algebra/associated_primes#thm7){: data-lid="z089f" } that there exists a bijection between the collection of prime ideals contained in $\mathfrak{p}_x$ that are associated prime ideals of $A$ and the associated prime ideals of $A_{\mathfrak{p}_x}$; and from this bijection, we can rewrite [Definition 8](#def8){: data-lid="jj4wu" } as:

> For a locally Noetherian scheme $X$ and a point $x$, $x$ is an *associated point* of $X$ if $\mathfrak{m}_x$ is an associated prime ideal of $\mathcal{O}_{X,x}$.

Now, the first condition of [\[Commutative Algebra\] §Associated Primes of Ideals, ⁋Theorem 7](/en/math/commutative_algebra/associated_primes#thm7){: data-lid="80ka0" } also guarantees the finiteness of associated points when $X$ is a quasicompact locally Noetherian scheme, that is, when $X$ is a Noetherian scheme. Since [Definition 8](#def8){: data-lid="w94sj" } can be restated solely in terms of the stalk independently of the choice of $U$ as seen above, we can restrict our attention to the spectrum $\Spec A$ of a Noetherian ring. 

::: Definition 9
Among the associated points of the spectrum $\Spec A$ of a Noetherian ring, any point that does not correspond to the generic point of an irreducible component of $\Spec A$ is called an *embedded point*. 
:::

That is, the points corresponding to the locations of zero-divisors that are missed by the generic points of irreducible components alone, which we mentioned before introducing [Definition 8](#def8){: data-lid="1t6oc" }, are precisely the embedded points, and this can be seen concretely in [Example 11](#ex11){: data-lid="85tve" }. Intuitively, an embedded point is a point that already belongs to another (larger) irreducible component, yet records that $A$ locally carries additional information in a nilpotent direction at that location, so that near that point, the scheme actually contains more information than the reduced structure determined by that component alone.

Meanwhile, the following holds by definition.

::: Proposition 10
The associated points of the spectrum $\Spec A$ of a Noetherian ring are the generic points of the irreducible components of the support $\supp(f)$ ([§Schemes, ⁋Definition 6](/en/math/scheme_theory/schemes#def6){: data-lid="7ho94" }) for some $f\in A$, and conversely.
:::
::: Proof
First, for any $g\in A$ and prime ideal $\mathfrak{q}\in \Spec A$,

$$\mathfrak{q}\in \supp(g)\iff g_\mathfrak{q}\neq 0\text{ in $A_\mathfrak{q}$}\iff \ann(g_\mathfrak{q})\neq A_\mathfrak{q}$$

holds. But by [\[Commutative Algebra\] §Localization, ⁋Proposition 5](/en/math/commutative_algebra/localization#prop5){: data-lid="9j5jb" },

$$\ann(g_\mathfrak{q})=\ann(g)A_\mathfrak{q}$$

so the last condition is equivalent to $\ann(g)\setminus \mathfrak{q}=\emptyset$, that is, $\mathfrak{q}\in Z(\ann(g))$. From this, we see that for any $g\in A$,

$$\supp(g)=Z(\ann(g))$$

holds. Therefore, there is a one-to-one correspondence between the irreducible components of $\supp(g)$ and the minimal prime ideals containing $\ann(g)$.

Now suppose any associated point $\mathfrak{p}$ of $\Spec A$ is given. By definition, there exists some $f\in A$ such that $\mathfrak{p}=\ann(f)$. Then

$$\supp(f)=Z(\ann(f))=Z(\mathfrak{p})$$

and since it is clear that $\mathfrak{p}$ is a minimal prime of $\ann(f)=\mathfrak{p}$, $\mathfrak{p}$ is the generic point of $\supp f$.

Conversely, suppose that $\mathfrak{p}$ is the generic point of $\supp(g)$ for some $g\in A$. That is, suppose that $\mathfrak{p}$ is a minimal prime ideal containing $\ann(g)$. Since the kernel of the morphism $A \rightarrow Ag$, $a\mapsto ag$ is precisely $\ann(g)$, we have $Ag\cong A/\ann(g)$, and in particular $\ann(A/\ann(g))=\ann(g)$. Now, applying the first result of [\[Commutative Algebra\] §Associated Primes of Ideals, ⁋Theorem 7](/en/math/commutative_algebra/associated_primes#thm7){: data-lid="p3r2e" } to the $A$-module $A/\ann(g)$, we obtain $\mathfrak{p}\in \Ass(A/\ann(g))=\Ass(Ag)$. Since $Ag$ is a submodule of $A$, the first inclusion of [\[Commutative Algebra\] §Associated Primes of Ideals, ⁋Lemma 5](/en/math/commutative_algebra/associated_primes#lem5){: data-lid="j6ipp" } gives $\Ass(Ag)\subseteq \Ass(A)$, and thus $\mathfrak{p}\in \Ass(A)$, meaning that $\mathfrak{p}$ is an associated point of $\Spec A$.
:::

Examining the equation

$$\supp(f)=Z(\ann(f))$$

used in the proof above, we see that the associated point $\mathfrak{p}=\ann(f)$ precisely records the set of elements whose product with $f$ is $0$, that is, the locus of the zero-divisor relations involving $f$. If $A$ were an integral domain, such zero-divisor relations would not exist in the first place, so $\ann(f)$ would be all of $A$ only when $f=0$, and $0$ otherwise. That is, in this case $\supp(f)$ is empty only when $f$ is $0$, and is all of $\Spec A$ otherwise; since we know from [Proposition 4](#prop4){: data-lid="kot7r" } that $\Spec A$ is irreducible, we see that the only associated point of $\Spec A$ is the generic point $(0)$.

Therefore, to see an example of an embedded point, we must consider the case where $A$ is not an integral domain, and hence $\ann(f)$ is neither $0$ nor $A$.

::: Example 11
Consider the affine scheme $X=\Spec \mathbb{K}[\x_1,\x_2]/(\x_2^2, \x_1\x_2)$. Then by [§The Spectrum, ⁋Proposition 9](/en/math/scheme_theory/spectrums#prop9){: data-lid="vwjdf" }, as a set $X=Z(\x_2^2,\x_1\x_2)$, and since $\sqrt{(\x_2^2,\x_1\x_2)}=(\x_2)$, this is $Z(\x_2)$, that is, the $\x_1$-axis $\Spec\mathbb{K}[\x_1]$. 

Now let us directly find the associated points in the form $\ann(f)$ according to [Proposition 10](#prop10){: data-lid="zs8ws" }. Any element of the ring $A=\mathbb{K}[\x_1,\x_2]/(\x_2^2,\x_1\x_2)$ can be uniquely written in the form

$$p(\x_1)+c\x_2,\qquad p\in \mathbb{K}[\x_1],\quad c\in \mathbb{K}$$ 

and since $\x_1\x_2=0$, we have

$$\x_1\cdot(p(\x_1)+c\x_2)=p(\x_1)\x_1$$

That is, $\ann(\x_1)=(\x_2)$, which is the generic point of the unique irreducible component of $X$. 

On the other hand, from $\x_2^2=0$ and $\x_1\x_2=0$, we have

$$\x_2\cdot(p(\x_1)+c\x_2)=p(0)\x_2$$

so $\ann(\x_2)=(\x_1,\x_2)$. This is an ideal containing $\ann(\x_1)=(\x_2)$ as a proper subset, geometrically corresponding to the origin. Unlike the example above, this is a point that does not appear as the generic point of an irreducible component of $X$, that is, an embedded point. 

In fact, these two points are all the associated points of $X$. For $f=p(\x_1)+c\x_2$ and $g=q(\x_1)+d\x_2$, from $\x_1\x_2=\x_2^2=0$, we have

$$fg=p(\x_1)q(\x_1)+\bigl(dp(0)+cq(0)\bigr)\x_2$$

so when $p=0$ and $c\neq 0$, the annihilator $\ann(f)$ is given by the condition $q(0)=0$ on $g$, that is, $(\x_1,\x_2)$; when $p\neq 0$ and $p(0)=0$, we are forced to have $q=0$, so $\ann(f)=(\x_2)$; and when $p(0)\neq 0$, both $q=0$ and $d=0$ are forced, so $\ann(f)=0$. That is, the only prime ideals obtained as the annihilator of a nonzero element are $(\x_2)$ and $(\x_1,\x_2)$. 

Unlike $Z(\x\y)$ in [§The Topology of Schemes, ⁋Example 6](/en/math/scheme_theory/topology_of_schemes#ex6){: data-lid="jzc1u" }, note that this zero-divisor relation does not arise from the product of two irreducible components. Specifically, the side $\x_2\in \ann(\x_1)$ is data already visible at the generic point $(\x_2)$, but for the side $\x_1\in \ann(\x_2)$, as $\supp(\x_2)=Z(\ann(\x_2))=\{(\x_1,\x_2)\}$ shows, the fact that $\x_2$ vanishes everywhere except at the origin means that it is captured as an associated prime only at the embedded point. 
:::

## Rational Functions

Now we define rational functions defined on a scheme. First, by the second result of [\[Commutative Algebra\] §Associated Primes of Ideals, ⁋Corollary 4](/en/math/commutative_algebra/associated_primes#cor4){: data-lid="2i9rw" }, we know that the map

$$A \rightarrow \prod_\text{\scriptsize $\mathfrak{p}$ associated prime} A_\mathfrak{p}$$

is injective. Therefore, on a locally Noetherian scheme $X$, for any open subset $U$, the map

$$\Gamma(U, \mathcal{O}_X) \rightarrow \prod_\text{\scriptsize $x$ associated in $U$} \mathcal{O}_{X,x}\tag{$\ast$}$$

is injective. This also holds even when $U$ is not affine: for if we cover $U$ with affine open subsets $V_k$ that are spectra of Noetherian rings, then from the reformulation immediately following [Definition 8](#def8){: data-lid="0v5xr" }, the associated points of $V_k$ are precisely those in $V_k$ that are associated points of $U$, so applying the injectivity in the affine case above to each $V_k$, we obtain $f\vert_{V_k}=0$.

::: Definition 12
For a locally Noetherian scheme $X$ and an open set $U$ containing all associated points of $X$, the image of an element of $\Gamma(U, \mathcal{O}_X)$ under ($\ast$) is called a *rational function* defined on $X$.
:::

Therefore, by definition, a rational function defined on $X$ consists of the data of (1) an open set containing all associated points of $X$, namely the *domain* $U$, and (2) a function $f\in \Gamma(U, \mathcal{O}_X)$ on it; two such pairs $(U, f)$ and $(U',f')$ define the same function if on $U\cap U'$, $f$ and $f'$ define the same function. The structure of these pairs and this equivalence relation is of exactly the same form as the definition of a rational function on a variety in [\[Algebraic Varieties\] §Rational Maps, ⁋Definition 1](/en/math/algebraic_varieties/rational_maps#def1){: data-lid="e7mph" }. The only difference is the condition that the domain $U$ must now contain all associated points, which is not so surprising since associated points are points that were not visible in classical algebraic geometry.

Examining where this condition comes from is essential to understanding [Definition 12](#def12){: data-lid="xd0bi" }. First, by [Proposition 10](#prop10){: data-lid="ynexj" }, for $X=\Spec A$ and any associated point $\mathfrak{p}$ of it,

$$\mathfrak{p}=\ann(f),\qquad \supp(f)=Z(\mathfrak{p})$$

holds for some nonzero function $f\in \Gamma(X, \mathcal{O}_X)$, and since this satisfies the condition of [Definition 12](#def12){: data-lid="5bskc" }, the pair $(X, f)$ defines a nonzero rational function via ($\ast$).

Now, for this associated point $\mathfrak{p}$, consider an open set $U$ that misses it. Then since $Z(\mathfrak{p})$ is an irreducible closed subset having $\mathfrak{p}$ as its generic point ([§The Spectrum, ⁋Proposition 16](/en/math/scheme_theory/spectrums#prop16){: data-lid="4rsgv" }), any nonempty open subset of $Z(\mathfrak{p})$ always contains $\mathfrak{p}$, and thus we know that we must have $U\cap Z(\mathfrak{p})=\emptyset$. That is, at all points contained in such an open set $U$, and in particular at the associated points contained in $U$, the germ of $f$ must be $0$. The problem is that if we allow such an open set $U$ as the domain of a rational function, $f$ becomes indistinguishable from $0$ by the injectivity of ($\ast$) above.

Looking at the case of a generic point as the simplest example, when $\mathfrak{p}$ is the generic point of some irreducible component $C$, we have $Z(\mathfrak{p})=C$; thus, if $f$ is not defined at $\mathfrak{p}$ (that is, intuitively, if it has a pole at this point), the above argument means that $U$ misses $C$ entirely, so that $f\vert_U=0$. Similarly, when $\mathfrak{p}$ is an embedded point, this $Z(\mathfrak{p})$ is merely replaced by a smaller closed set rather than an entire component, but such a loss still occurs.

For example, consider $Z(\x\y)=\Spec \mathbb{K}[\x,\y]/(\x\y)$ from [§The Topology of Schemes, ⁋Example 6](/en/math/scheme_theory/topology_of_schemes#ex6){: data-lid="udwon" }. This scheme has two irreducible components, the $y$-axis $Z(\x)$ and the $x$-axis $Z(\y)$, whose generic points are $(\x)$ and $(\y)$, respectively. Also, since $\ann(\y)=(\x)$, the function $f$ obtained as a result of [Proposition 10](#prop10){: data-lid="22qna" } is precisely $\y$, and indeed $\supp(\y)=Z(\x)$, which shows the entire $y$-axis. Now, if we consider an open set such as $U=D(\x)$, which excludes this generic point $(\x)$, then from $\x\y=0$,

$$\y=\x^{-1}(\x\y)=0\qquad\text{in $A_\x$}$$

we have $\y\vert_U=0$. That is, the moment we take $U$ as the domain, as for the $y$-axis, the function $\y$ carrying its information becomes indistinguishable from the rational function $0$, which precisely reflects the fact that $U$ completely misses an entire component, the $y$-axis.

::: Example 13
Let us examine concretely what rational functions look like on $X=\Spec \mathbb{K}[\x_1,\x_2]/(\x_2^2,\x_1\x_2)$ from [Example 11](#ex11){: data-lid="t3ugt" }. By the second result of [\[Commutative Algebra\] §Associated Primes of Ideals, ⁋Theorem 7](/en/math/commutative_algebra/associated_primes#thm7){: data-lid="fgdns" }, the set of all zero-divisors of $A=\mathbb{K}[\x_1,\x_2]/(\x_2^2,\x_1\x_2)$ is equal to the union of the associated primes

$$(\x_2)\cup(\x_1,\x_2)=(\x_1,\x_2)$$

so the non-zerodivisors are precisely the elements that do not vanish at the origin, that is, with $q(0)\ne0$ for $q$, elements of the form $s=q(\x_1)+c'\x_2$. Since such an $s$ belongs to neither of the two associated primes $(\x_2),(\x_1,\x_2)$, $D(s)$ contains both associated points of $X$, making it a valid domain of definition satisfying the condition of [Definition 12](#def12){: data-lid="hwdbq" }, and by [§Affine Scheme, ⁋Lemma 6](/en/math/scheme_theory/affine_schemes#lem6){: data-lid="raedx" }, the functions on it are given by $A_s$.

Our claim is that considering only the rational functions defined on these domains $D(s)$ already yields all rational functions on the whole of $X$. To this end, suppose that an arbitrary domain of definition $U$ is given, and let $X\setminus U=Z(I)$. Then, since $U$ must contain the associated points, there must exist a function among the elements of $I$ that does not become $0$ at the origin, that is, an element not contained in the ideal $(\x_1,\x_2)$. Such an element is precisely the non-zerodivisor $s$ examined above, and from $s\in I$ we obtain $D(s)\subseteq U$. That is, any domain of definition always contains such a $D(s)$ within it, which allows us to restrict a function defined on $U$ to $D(s)$; and since $D(s)$ already contains all associated points, by the injectivity of ($\ast$), this restriction preserves distinct functions on $U$ as distinct functions on $D(s)$. Furthermore, for the same reason, ($\ast$) for $U$ factors as the composition of this restriction and ($\ast$) for $D(s)$, so restricting a function on $U$ to $D(s)$ does not change its image, that is, the rational function it defines.

From the above, the total quotient ring of $X$, $K(X)$, formed by all rational functions, using the notation for elements seen in [Example 11](#ex11){: data-lid="p3s3r" }, takes the form

$$K(X)=\left\{\frac{p(\x_1)+c\x_2}{q(\x_1)+c'\x_2} \mid q(0)\neq0\right\}.$$

This parallels the classical case where the fraction field was the collection of rational expressions whose denominator is not $0$, but with the condition changed to requiring that the denominator must not vanish even at the origin (not just at the generic point).

What distinguishes this from the classical function field is that the $K(X)$ above contains nonzero nilpotents, which is precisely due to the embedded point. Specifically, $\x_2$ is a nilpotent element satisfying $\x_2^2=0$, yet it is a nonzero function in $K(X)$. If [Definition 12](#def12){: data-lid="7yy9s" } had not required the domain of definition to contain this embedded point, $D(\x_1)$, with the origin removed, would also have been allowed as a domain of definition; as seen in [Example 11](#ex11){: data-lid="o1sue" }, since $\x_2$ is already $0$ on it, $\x_2$ would have vanished in $K(X)$, and consequently the thickening of $X$ in the nilpotent direction would not have been detected in $K(X)$.
:::

More generally, the collection of rational functions defined on a locally Noetherian scheme $X$ defines the *total quotient ring* $K(X)$ in the same manner as the construction above. If $X$ is an integral scheme, then $X$ is in particular irreducible and thus has a unique generic point $\xi$, and for any affine open subset $U\cong\Spec A$, this point must correspond to the unique minimal prime ideal $(0)$ of the integral domain $A$. Then the localization at this point is obtained by adding all nonzero elements of $A$ to the denominator, that is, it is equal to $\Frac(A)$, so that $K(X)\cong \mathcal{O}_{X,\xi}\cong \Frac(A)$; this shows that when $X$ consists of a single affine open $\Spec A$, the fraction field of $A$ that we already knew continues to serve as the field of rational functions for general integral schemes as well.

---
**References**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).

---
[^1]: In this process, we used the fact that $X$ has only finitely many irreducible components. This ensures that the union of the remaining components is again a closed set; therefore, if the two closed sets do not intersect, they become open sets simultaneously, contradicting connectedness.
