---
title: "Classifying Spaces"
description: "We define principal bundles with an arbitrary topological group as structure group, and classify them using homotopy theory via universal bundles and classifying spaces."
excerpt: "Classification of principal G-bundles and the construction of classifying space BG"

categories: [Math / Algebraic Topology]
permalink: /en/math/algebraic_topology/classifying_spaces
sidebar: 
    nav: "algebraic_topology-en"

date: 2026-07-07
weight: 12
translated_at: 2026-07-11T23:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-07-11T23:30:02+00:00
---
In previous posts, we introduced characteristic classes to classify vector bundles. One of the most interesting aspects is the manner in which their existence is established: we examined how a certain *universal* bundle defined over a large space exists so that any bundle can be realized as its pullback. For instance, in the case of real vector bundles, the tautological $k$-plane bundle over the infinite real Grassmannian

$$E(\gamma^k_\infty)\rightarrow \Gr(k, \mathbb{R}^\infty)$$

played this role ([§Stiefel-Whitney Characteristic Classes, §§Grassmannians](/en/math/algebraic_topology/stiefel_whitney_classes#grassmannians)), and a similar construction existed for complex vector bundles as well. ([§Characteristic Classes of Vector Bundles, ⁋Example 8](/en/math/algebraic_topology/characteristic_classes#ex8)) On the other hand, since the pullback of a vector bundle depends only on the homotopy class of the map, the isomorphism class of a rank $k$ vector bundle over a fixed space $B$ becomes the collection of homotopy classes of maps into these spaces $[B, \Gr(k, \mathbb{R}^\infty)]$ (or $[B, \Gr(k, \mathbb{C}^\infty)]$).

Another perspective on vector bundles was to regard them as a collection of transition functions. For example, any vector bundle could be specified by giving

$$g_{ij}: U_i\cap U_j\rightarrow \GL(k;\mathbb{R})$$

on the overlaps of two trivializing open covers, and this perspective was powerful in that, for example, replacing $\GL(k;\mathbb{R})$ with $\GL^+(k;\mathbb{R})$ also accounted for *oriented* vector bundles.

The purpose of this post is to connect these two perspectives. That is, we will more generally define the *principal $G$-bundle* that appears when the structure group is a (topological) group $G$, and define the *classifying space* $\B G$, which is the space that classifies these. In this post, $G$ always denotes a topological group, and unless otherwise stated, the base space is assumed to be paracompact.

## Definition of Principal Bundle

In a vector bundle, the fiber carries a vector space structure, and its transition function is a linear automorphism preserving this structure, that is, an element of $\GL(k;\mathbb{R})$. When dealing with a general structure group $G$, it is natural to take the fiber itself to be $G$ and give the transition by left translation in $G$. A slight difference is that there is no distinguished point from this perspective; an element of the fiber that is the identity in one chart is understood as a different element of the fiber in another chart via left translation. In other words, these elements should be thought of as *$G$-torsors*, and to describe this in a coordinate-independent manner we use a $G$-action on the total space.

::: Definition 1
For a topological group $G$, suppose a fiber bundle $p:P\rightarrow X$ and a continuous right action $P\times G\rightarrow P$ on it are given. This data is called a *principal $G$-bundle* if the following three conditions hold.

1. The $G$-action preserves the fiber. That is, for all $y\in P$ and $g\in G$, $p(y\cdot g)=p(y)$.
2. The $G$-action on each fiber is free and transitive. That is, for any $x\in X$, fixing one point $y\in p^{-1}(x)$, the map $g\mapsto y\cdot g$ is a bijection from $G$ to $p^{-1}(x)$.
3. ($G$-equivariant local triviality) For each $x\in X$, there exists an open neighborhood $U$ and a $G$-equivariant homeomorphism $\varphi:p^{-1}(U)\rightarrow U\times G$ compatible with $p$ over $U$. Here, the $G$-action on $U\times G$ is given by $(u,h)\cdot g=(u,hg)$.
:::

Thus, locally, we attach copies of $G$ in the fiber direction over the base space, and $G$ acts on each fiber by right translation.

A *morphism* between two principal $G$-bundles $P,P'\rightarrow X$ is a continuous function $f:P\rightarrow P'$ satisfying $p'\circ f=p$ and compatible with the $G$-action, and if this is a homeomorphism, we call it an *isomorphism* between the two principal bundles. Fixing local trivializations $\varphi_i:p^{-1}(U_i)\rightarrow U_i\times G$, a continuous function $g_{ij}:U_i\cap U_j\rightarrow G$ is determined on $U_i\cap U_j$ satisfying $\varphi_i\circ\varphi_j^{-1}(u,h)=(u,g_{ij}(u)h)$. These transition functions satisfy the same cocycle condition as in vector bundles,

$$g_{ij}(x)g_{jk}(x)=g_{ik}(x),\qquad g_{ii}(x)=e,$$

and two cocycles $(g_{ij})$ and $(g_{ij}')$ give the same bundle if and only if there exist continuous functions $\lambda_i:U_i\rightarrow G$ such that $g_{ij}'=\lambda_i g_{ij}\lambda_j^{-1}$. Therefore, the isomorphism classes of principal $G$-bundles trivializing over an open cover $\{U_i\}$ are classified by nonabelian Čech cohomology $\check{H}^1(X;G)$, and when $G=\GL(k;\mathbb{R})$ this exactly coincides with the classification of vector bundles in the previous post.

A vector bundle always has a zero section, but since the fiber of a principal bundle is a $G$-torsor rather than $G$ itself, it is not obvious how to pick a section playing this role. Indeed, the following proposition shows that the existence of a section completely determines the triviality of a principal bundle.

::: Proposition 2
A principal $G$-bundle $p:P\rightarrow X$ is isomorphic to the trivial bundle if and only if there exists a continuous global section $s:X\rightarrow P$.
:::
::: Proof
The trivial bundle $X\times G$ has the section $x\mapsto(x,e)$, so if $P$ is trivial we obtain a section via the isomorphism. Conversely, suppose a section $s:X\rightarrow P$ exists, and consider the map

$$\Phi:X\times G\rightarrow P,\qquad (x,g)\mapsto s(x)\cdot g.$$

Since the $G$-action on each fiber is simply transitive (condition (2) of [Definition 1](#def1)), the restriction of $\Phi$ to each fiber $\{x\}\times G\rightarrow p^{-1}(x)$ is bijective, and thus $\Phi$ is bijective. By definition, $\Phi$ satisfies $p\circ\Phi=\pr_1$ and is compatible with the $G$-action, so it is a morphism over $X$. Finally, that $\Phi$ is a homeomorphism can be checked locally: on a trivialization $\varphi:p^{-1}(U)\rightarrow U\times G$, if $s$ is written as $x\mapsto(x,\sigma(x))$ ($\sigma:U\rightarrow G$ continuous), then $\Phi$ becomes $(x,g)\mapsto(x,\sigma(x)g)$, and its inverse $(x,h)\mapsto(x,\sigma(x)^{-1}h)$ is continuous.
:::

This proposition reveals the decisive difference between principal bundles and vector bundles. Therefore, to relate principal bundles and vector bundles, we need an object that connects the two.

One of the simplest reasons a principal $G$-bundle cannot be a vector bundle is that the fiber of a vector bundle is a vector space, not a group. We resolve this by making the following definition.

::: Definition 3
Suppose a principal $G$-bundle $p:P\rightarrow X$ and a topological space $F$ on which $G$ acts continuously from the left are given. Then define the $G$-action on $P\times F$ by

$$(y,f)\cdot g=(y\cdot g,\ g^{-1}\cdot f)$$

and write its orbit space as $P\times_G F=(P\times F)/G$. Then the map $P\times_G F\rightarrow X$ induced by $(y,f)\mapsto p(y)$ is a fiber bundle with fiber $F$, and we call this the *associated bundle* of $P$.
:::

Intuitively, this attaches the fiber $F$ along the *twisted* structure of the principal $G$-bundle; for example, applying this to the trivial $G$-bundle $X\times G$ and fiber $F$ yields the trivial fiber bundle $X\times F$, and similarly, applying it to a slightly twisted (that is, non-trivial) principal $G$-bundle $P$ and fiber $F$ gives a fiber bundle with fiber $F$ that inherits the twisting data from $P$.

The most transparent example is a vector bundle, so let us follow the definition step by step here. The topological group $G=\GL(k;\mathbb{R})$ acts on the left on the dimension $k$ real vector space $F=V$. Also, for convenience, suppose the trivial $G$-bundle $P=X\times G$ is given. Then the $G$-action defined on the product space $P\times F=(X\times G)\times V$ is

$$\bigl((x,g),v\bigr)\cdot h=\bigl((x, gh),h^{-1}v\bigr)$$

and its orbit space is nothing but $X\times V$. This is because taking the action of $h=g^{-1}$ on any element $((x,g),v)$ gives

$$((x,g),v)\cdot g^{-1}=\bigl((x,e),gv\bigr),$$

and in this process we identified $(x,e)$ in $X\times G$ with the element $x$ in $X$, using the fact that the map

$$[((x,g),v)]\mapsto(x,gv)$$

is a well-defined homeomorphism. That is, starting from a trivial $G$-bundle, the associated bundle is also trivial.

More generally, if $P$ is given by transition functions $g_{ij}$ over $\{U_i\}$, then $P\times_G F$ becomes a bundle over the same $U_i$ with fiber $F$ and transition given by the action of $g_{ij}$ on $F$.

The reverse construction is also possible. Given a rank $n$ vector bundle $E\rightarrow X$, the space of all ordered bases, that is, *frames*, of the fiber $E_x$ over each $x$,

$$\Fr(E)=\{(x,b)\mid x\in X,b\text{ an ordered basis of $E_x$}\}$$

becomes a principal $\GL(n;\mathbb{R})$-bundle with respect to the action of $\GL(n;\mathbb{R})$ sending a basis to a matrix, and we call this the *frame bundle* of $E$. The following proposition shows that these two constructions are inverse processes.

::: Proposition 4
Over a topological space $X$, there is a natural one-to-one correspondence between isomorphism classes of principal $\GL(n;\mathbb{R})$-bundles and isomorphism classes of rank $n$ real vector bundles. This correspondence sends a principal bundle $P$ to the associated bundle $P\times_{\GL(n;\mathbb{R})}\mathbb{R}^n$, and a vector bundle $E$ to the frame bundle $\Fr(E)$.
:::
::: Proof
It suffices to check that the two correspondences are inverses of each other.

First, by definition, a point of the frame bundle $\Fr(E)$ is the same as an ordered basis of the fiber $E_x$, and this is exactly the same information as a linear isomorphism $b:\mathbb{R}^n\rightarrow E_x$, since we only need to see where each standard basis vector of the standard Euclidean space $\mathbb{R}^n$ goes. The map defined in this way,

$$\Fr(E)\times_{\GL(n;\mathbb{R})}\mathbb{R}^n\rightarrow E,\qquad [(b,v)]\mapsto b(v)$$

is well-defined because even if we change $(b,v)$ to $(b\circ A, A^{-1}v)$, we obtain the same value $(b\circ A)(A^{-1}v)=b(v)$. This map is a linear isomorphism on each fiber, so it is an isomorphism of vector bundles.

Conversely, starting from a principal bundle $P$, we can check that the frame bundle of $P\times_G\mathbb{R}^n$ is again isomorphic to $P$ by verifying that the transition functions $g_{ij}$ match on both sides via local trivialization.

Both constructions preserve the transition function, so they preserve the isomorphism class, and the naturality of the map follows from compatibility with pullback.
:::

Thanks to this equivalence, every classification problem for vector bundles is translated into a problem for principal $\GL(n;\mathbb{R})$-bundles. In the same way, complex vector bundles correspond to principal $\GL(n;\mathbb{C})$-bundles, and oriented real vector bundles correspond to principal $\GL^+(n,\mathbb{R})$-bundles. Therefore, if we can classify principal $G$-bundles for an arbitrary structure group $G$, all these cases are solved at once.

Just as with vector bundles, given a continuous function $f:X'\rightarrow X$ and a principal $G$-bundle $p:P\rightarrow X$, the *pullback bundle*

$$f^\ast P=\{(x',y)\in X'\times P\mid f(x')=p(y)\}$$

is defined. Giving the action $(x',y)\cdot g=(x',y\cdot g)$ here makes $f^\ast P\rightarrow X'$ again a principal $G$-bundle, and from the perspective of transition functions this corresponds to pulling back $g_{ij}$ to $g_{ij}\circ f$. The crucial fact is that this pullback depends only on the homotopy class of $f$.

::: Theorem 5 (Homotopy Invariance of Pullback)
Suppose $X$ is paracompact and $f_0,f_1:X\rightarrow Y$ are homotopic. ([§Homotopy, ⁋Definition 2](/en/math/algebraic_topology/homotopy#def2)) Then for any principal $G$-bundle $p:P\rightarrow Y$, $f_0^\ast P$ and $f_1^\ast P$ are isomorphic over $X$.
:::
::: Proof
The key is the following fact.

> When $X$ is paracompact, a principal $G$-bundle $Q$ over $X\times[0,1]$ is isomorphic to the pullback of its restriction to $X\times\{0\}$ by the projection $X\times[0,1]\rightarrow X\times\{0\}$.

This follows from the covering homotopy property of bundles, which in turn follows from the fact that a trivializing cover over a paracompact base admits a locally finite partition of unity. The gist of the proof is to divide $[0,1]$ into small intervals, glue trivializations over each interval, and paste these local isomorphisms using a partition of unity.

Now let a homotopy $H:X\times[0,1]\rightarrow Y$ connecting $f_0,f_1$ be given and define $Q=H^\ast P$. By the above fact, $Q$ is isomorphic to the pullback of $Q\vert_{X\times\{0\}}=f_0^\ast P$ by the projection, and repeating the same argument at the end $X\times\{1\}$, $Q\vert_{X\times\{1\}}=f_1^\ast P$ is also isomorphic to the same bundle.
:::

In particular, if $X$ is contractible, then the identity map is homotopic to a constant map, so all principal $G$-bundles over $X$ are trivial. In general, a CW complex is always paracompact, so the hypothesis of the above theorem is automatically satisfied for the bases we intend to deal with.

## Universal Bundle and Classifying Space

[Theorem 5](#thm5) tells us that sending a function $f$ to $f^\ast P$ depends only on the homotopy class of $f$. Therefore, if we can take a fixed principal $G$-bundle as a source from which all other bundles can be obtained by pullback, the classification of principal $G$-bundles would be reduced to counting homotopy classes into that source space, which generalizes the fact that in vector bundles, the universal bundle over $\Gr(k,\mathbb{R}^\infty)$ was such a source.

::: Definition 6
For a topological group $G$, a principal $G$-bundle $p:\E G\rightarrow \B G$ is called a *universal bundle* if the total space $EG$ is contractible, that is, $\E G$ is homotopy equivalent to a point. ([§Homotopy, ⁋Definition 4](/en/math/algebraic_topology/homotopy#def4)) In this case, we call the base space $\B G$ the *classifying space* of $G$.
:::

That is, a universal $G$-bundle is a free $G$-action on a contractible space, and its orbit space $\B G=\E G/G$ is the base space, with the projection map to it being the bundle map. The condition that $\E G$ is contractible will be used crucially in [Theorem 8](#thm8). Before that, we first note the following.

::: Theorem 7 (Milnor)
For any topological group $G$, a universal bundle $\E G\rightarrow \B G$ exists.
:::

The proof uses the infinite join of $G$,

$$\E G=G\ast G\ast G\ast\cdots,$$

and the point is that this space is $n$-connected for any $n$, and thus weakly contractible, and under a CW structure it is contractible. We leave the details to [Mil].

Meanwhile, the universal bundle is essentially unique. If two universal bundles $\E G\rightarrow \B G$ and $\E G'\rightarrow \B G'$ are given, since $\E G'$ is contractible, by [Theorem 5](#thm5) there exists a classifying map pulled back to $\B G$, and applying this argument in both directions connects $\B G$ and $\B G'$ by maps that are homotopy inverses of each other. Thus $\B G$ is determined without ambiguity beyond homotopy equivalence, and we call $\B G$ *the* classifying space.

Then the most central result of this post is, of course, the following theorem.

::: Theorem 8 (Classification Theorem)
For a paracompact space $X$ and a topological group $G$, let $[X,\B G]$ be the set of free homotopy classes from $X$ to $\B G$. Then the map pulling back the universal bundle $\E G\rightarrow \B G$,

$$[X,\B G]\rightarrow\{\text{principal $G$-bundles over $X$}\}/{\cong};\qquad [f]\mapsto f^\ast \E G$$

is a well-defined bijection, and it is natural in the sense that it is compatible with pullback along a map $X'\rightarrow X$.

{% diagram Math/Algebraic_Topology/Classifying_Spaces-1.svg width="8.21em" alt="Pullback square of the classifying map" %}

:::
::: Proof
That $[f]\mapsto f^\ast \E G$ does not depend on the choice of representative for $[f]$ is by [Theorem 5](#thm5). We briefly examine that this is a bijection.

First, suppose a principal $G$-bundle $P$ over $X$ is given. Since $X$ is paracompact, by [\[Topology\] §Compactness and Paracompactness, ⁋Theorem 27](/en/math/topology/compactness#thm27) we can take together an open cover $\{U_i\}$ trivializing $P$ and a locally finite partition of unity $\{\rho_i\}$ subordinate to it. The trivialization over each $U_i$ gives a $G$-equivariant map $\psi_i:p^{-1}(U_i)\rightarrow G$, so

$$\widetilde{f}:P\rightarrow \E G,\qquad y\mapsto \sum_i \rho_i(p(y))\psi_i(y)$$

is a well-defined $G$-equivariant map. A $G$-equivariant map descends to a map $f:X\rightarrow \B G$ between base spaces, and since $\widetilde{f}$ is an isomorphism on each fiber, we obtain $P\cong f^\ast \ EG$.

To show injectivity now, suppose for $f_0,f_1:X\rightarrow \B G$ that $f_0^\ast \E G\cong f_1^\ast \E G=:P$. We need to show that $f_0$ and $f_1$ are homotopic. Each $f_i$ has a bundle map $P\cong f_i^\ast \E G\rightarrow \E G$, that is, a $G$-equivariant bundle map $\Phi_i:P\rightarrow \E G$ from $P$ to the universal bundle. However, since $\E G$ is contractible, any two $G$-equivariant maps from a principal bundle $P$ over a paracompact space to $EG$ are $G$-equivariantly homotopic to each other, so there exists a $G$-equivariant homotopy $P\times[0,1]\rightarrow \E G$ connecting $\Phi_0$ and $\Phi_1$, and this descends to the base to give a homotopy between $f_0$ and $f_1$, so $[f_0]=[f_1]$.
:::

This theorem translates the geometric classification of principal $G$-bundles into purely homotopy data $[X,\B G]$. Combined with [Proposition 4](#prop4), the classification of rank $n$ real vector bundles is translated to $[X,\B\GL(n;\mathbb{R})]$, and in the complex case to $[X,\B\GL(n;\mathbb{C})]$, and indeed we will soon see that these $\B\GL(n; \mathbb{R})$ and $\B\GL(n;\mathbb{C})$ are actually (real/complex) Grassmannians.

::: Lemma 9
The construction of the classifying space is functorial in $G$. Given a continuous group homomorphism $\phi:G\rightarrow H$, the associated bundle $\E G\times_G H$ obtained by changing the $G$-action on $\E G$ to an $H$-action via $\phi$ induces a map $\B\phi:\B G\rightarrow \B H$. This satisfies $\B(\psi\circ\phi)\simeq \B\psi\circ \B\phi$, making $G\mapsto \B G$ a functor on the homotopy category. For example, the inclusion $\Umat(n)\hookrightarrow\GL(n;\mathbb{C})$ induces $\B\Umat(n)\rightarrow \B\GL(n;\mathbb{C})$, which is used below.
:::

## Examples of Classifying Spaces

In reality, the most useful part of this post is not the existence but how these classifying spaces are given. The simplest case is as follows.

::: Example 10
Suppose $G$ is a discrete group. Then a principal $G$-bundle defined over any base $B$ becomes a covering space over $B$ since its fiber is discrete. From this perspective, the right action of $G$ becomes a Deck transformation, and since the Deck group acts transitively on the fiber, this covering space is a *regular* covering space.

Now apply this to the universal bundle $\E G \rightarrow \B G$. Then by [§Covering Spaces, ⁋Corollary 12](/en/math/algebraic_topology/covering_spaces#cor12), the Deck transformation group of this covering space is isomorphic to $\pi_1(\B G)$, but we saw earlier that this Deck group must be $G$, so $\pi_1(\B G)\cong G$, and since $EG$ is contractible, the universal cover of $\B G$ is also contractible, so $\pi_n(\B G)=0$ ($n\geq 2$). That is, $\B G$ is an Eilenberg–MacLane space $K(G,1)$.

For more concrete examples, let us look at the cases $G=\mathbb{Z}/2$ and $G=\mathbb{Z}$ respectively. First, for $\mathbb{Z}/2$, we need to find a contractible space on which $\mathbb{Z}/2$ acts freely, and giving the antipodal action on $S^\infty$ exactly satisfies both of these conditions. Then the orbit space of this action becomes $\RP^\infty$. For $\mathbb{Z}$, we can also find it from an example already familiar to us, namely the $\mathbb{R}\rightarrow S^1$ introduced as a standard example of a covering space right after [§Covering Spaces, ⁋Definition 3](/en/math/algebraic_topology/covering_spaces#def3).
:::

Now let us examine the classifying spaces of the groups we are actually interested in. The most basic example among non-discrete groups is $G=S^1$, which is generally thought of as the collection of complex numbers of length $1$, the $e^{2\pi it}$, contained in $\mathbb{C}^\times$. Then $S^1$ acts freely on $\mathbb{C}^\infty\setminus\{0\}$ by scalar multiplication.

Now we can deformation retract each $\mathbb{C}^n\setminus 0$ to the unit sphere

$$S^{2n-1}\subseteq\mathbb{C}^n\cong\mathbb{R}^{2n}$$

via radial deformation retract, and observe that the canonical inclusion

$$\mathbb{C}^n\hookrightarrow\mathbb{C}^{n+1}\hookrightarrow \mathbb{C}^{n+2}\hookrightarrow \cdots$$

induces the inclusion $S^{2n-1}\hookrightarrow S^{2n+1}$ putting the previous unit sphere into the equator of the next unit sphere. Therefore, if we view $\mathbb{C}^\infty\setminus \{0\}$ as the colimit $\varinjlim (\mathbb{C}^n\setminus \{0\})$, this deformation retracts to the colimit $\varinjlim S^{2n-1}$, which is a cofinal subsequence of the inclusions

$$S^1\subseteq S^2\subseteq S^3\cdots $$

appearing in the definition of $S^\infty$, so the result is the same as $S^\infty$. On the other hand, since the scalar multiplication of $S^1$ preserves the norm, this action restricts to a free action on the unit sphere $S^\infty\subseteq\mathbb{C}^\infty\setminus\{0\}$. That is, if we take $\E S^1=S^\infty$, this is a contractible space on which $S^1$ acts freely, and since the trace of each complex line in $\mathbb{C}^\infty$ intersecting $S^\infty$ is exactly one $S^1$-orbit, that is, the unit circle in that line, the orbit space is the complex projective space

$$\B S^1=S^\infty/S^1=\CP^\infty.$$

To see what this means in the language of vector bundles, let us return to the associated bundle of [Definition 3](#def3). Since $S^1$ acts on $\mathbb{C}$ by scalar multiplication, for any principal $S^1$-bundle $P\rightarrow X$, the associated bundle

$$P\times_{S^1}\mathbb{C}\rightarrow X$$

is defined. As we saw earlier, this is a bundle over the same open cover as $P$ with fiber $\mathbb{C}$ and transition given by the action of $g_{ij}$ on $\mathbb{C}$, but since scalar multiplication is $\mathbb{C}$-linear, these transitions are linear automorphisms given by elements of $S^1\subseteq\mathbb{C}^\times=\GL(1;\mathbb{C})$, and therefore $P\times_{S^1}\mathbb{C}$ is a complex line bundle. That is, a principal $S^1$-bundle naturally becomes a line bundle just by attaching $\mathbb{C}$. Conversely, given a line bundle $L\rightarrow X$, by paracompactness we can put a Hermitian metric on it, and the sphere bundle $S(L)\subseteq L$ of unit vectors in each fiber becomes a principal $S^1$-bundle with respect to the scalar multiplication of $S^1$. By the same argument as in [Proposition 4](#prop4) replacing ordered bases with unit vectors, we can check that these two constructions are inverses of each other, and this is the reason we can reduce the structure group of a line bundle from $\GL(1;\mathbb{C})$ to $S^1=\Umat(1)$.

Applying this explicitly to the universal bundle $ES^1=S^\infty\rightarrow\CP^\infty$ gives the line bundle

$$S^\infty\times_{S^1}\mathbb{C}\longrightarrow\CP^\infty.$$

Looking at the fiber over a point $[\ell]\in\CP^\infty$, the equivalence class $[e,z]$ is the same as the element $ze\in\ell$ of the line $\ell=\mathbb{C}e$ determined by the unit vector $e$, so this is the tautological line bundle $\gamma$ having each line as its own fiber. That is, the reason $\gamma$ became the universal family of complex line bundles in [§Characteristic Classes of Vector Bundles, ⁋Example 8](/en/math/algebraic_topology/characteristic_classes#ex8) is that the result of attaching $\mathbb{C}$ to the universal principal $S^1$-bundle is exactly $\gamma$, and conversely, the $S^\infty$ that appeared there as the sphere bundle of $\gamma$ is precisely $\E S^1$.

::: Example 11 (Classifying Spaces of Linear Groups)
The above discussion generalizes to arbitrary rank $n$ bundles. First, observe generally that if a continuous representation

$$G\rightarrow\GL(n;\mathbb{C})$$

of a topological group $G$ is given, then for any principal $G$-bundle $P$, the associated bundle $P\times_G\mathbb{C}^n$ becomes a rank $n$ complex vector bundle. Since a line bundle was obtained by attaching the standard representation $\mathbb{C}$ to a principal $\Umat(1)=S^1$-bundle, it is natural to expect that a rank $n$ complex vector bundle is obtained by attaching the standard representation $\mathbb{C}^n$ to a principal $\Umat(n)$-bundle.

What is needed for this is a universal principal $\Umat(n)$-bundle, which is given by the *complex Stiefel manifold*

$$V_n(\mathbb{C}^\infty)=\varinjlim_k V_n(\mathbb{C}^k)$$

of all orthonormal $n$-frames in $\mathbb{C}^\infty$, with $\Umat(n)$ acting on the right by matrix multiplication and the orbit space being $\Gr(n,\mathbb{C}^\infty)$. An orthonormal $1$-frame is just a unit vector, so for $n=1$ this is exactly $\E S^1=S^\infty\rightarrow\CP^\infty$ in the main text, and for general $n$ as well, by the same argument as we saw for $S^\infty$, $V_n(\mathbb{C}^\infty)$ deformation retracts to a point and is contractible, so this principal bundle is universal.

Now attaching the canonical representation $\mathbb{C}^n$ gives the associated bundle

$$V_n(\mathbb{C}^\infty)\times_{\Umat(n)}\mathbb{C}^n\longrightarrow\Gr(n,\mathbb{C}^\infty).$$

Looking at the fiber over a point $[V]$, for $z=(z_1,\ldots,z_n)\in\mathbb{C}^n$, the equivalence class $[(e_1,\ldots,e_n),z]$ is the same as the element $z_1e_1+\cdots+z_ne_n\in V$ of the subspace $V$ spanned by the frame, so just as with line bundles, this is the tautological $n$-plane bundle $\gamma^n$ having each subspace as its own fiber, and conversely, collecting all orthonormal frames of each fiber of $\gamma^n$ also recovers $V_n(\mathbb{C}^\infty)$, just as with line bundles. That is,

$$\B\Umat(n)=\Gr(n,\mathbb{C}^\infty)$$

and the universal bundle over it is the tautological $n$-plane bundle.

On the other hand, the process by which [Proposition 4](#prop4), or more precisely its complex version, assigns a rank $n$ complex vector bundle must, strictly speaking, use the associated bundle via a principal $\GL(n;\mathbb{C})$-bundle. That is, for the above calculation to lead to the classification of arbitrary complex vector bundles, $\B\GL(n;\mathbb{C})$ and $\B\Umat(n)$ must be the same, and indeed they are. This is by [\[Linear Algebra\] §Complex Inner Product Spaces, ⁋Proposition 7](/en/math/linear_algebra/complex_inner_product_spaces#prop7): any element of $\GL(n;\mathbb{C})$ decomposes uniquely as a product of a unitary matrix and an upper-triangular matrix with positive diagonal entries, and this decomposition can be shown to be continuous. Now contracting the upper-triangular component toward the identity gives exactly the deformation retract of $\GL(n;\mathbb{C})$ to $\Umat(n)$. That is, the inclusion $\Umat(n)\hookrightarrow\GL(n;\mathbb{C})$ is a homotopy equivalence, and by the functoriality of classifying spaces [Lemma 9](#lem9),

$$\B\GL(n;\mathbb{C})\simeq \B\Umat(n)=\Gr(n,\mathbb{C}^\infty).$$

Repeating the same entire story for the real Stiefel manifold $V_n(\mathbb{R}^\infty)$ of all orthonormal $n$-frames in $\mathbb{R}^\infty$, $\Omat(n)$, and Gram–Schmidt orthogonalization gives

$$\B\GL(n;\mathbb{R})\simeq \B\Omat(n)=\Gr(n,\mathbb{R}^\infty).$$
:::

## Cohomology of Classifying Spaces

By [Theorem 8](#thm8), a characteristic class of a bundle with structure group $G$ is the pullback of a cohomology class of $\B G$ by the classifying map. Therefore, characteristic class theory is the same as computing the cohomology ring of $\B G$, and we organize this for the most basic groups.

The starting point is the cohomology ring of complex projective space. In [§Characteristic Classes of Vector Bundles, ⁋Example 8](/en/math/algebraic_topology/characteristic_classes#ex8) we saw that

$$H^\bullet(\CP^\infty;\mathbb{Z})=\mathbb{Z}[t],\qquad \lvert t\rvert=2$$

and the generator $t$ was the first Chern class of the tautological line bundle. Since we saw above that $\B S^1=\CP^\infty$, this means

$$H^\bullet(\B S^1;\mathbb{Z})=\mathbb{Z}[t],\qquad \lvert t\rvert=2.$$

For the torus, it follows from the cohomology of product spaces.

::: Corollary 12
For the $n$-dimensional torus $T=(S^1)^n$,

$$H^\bullet(\B T;\mathbb{Z})=\mathbb{Z}[t_1,\ldots,t_n],\qquad \lvert t_i\rvert=2$$

is a polynomial ring generated by $n$ generators of degree $2$. Moreover, the degree $2$ part $H^2(\B T;\mathbb{Z})$ is canonically isomorphic to $\Hom(T,S^1)$.
:::
::: Proof
Since $\B T=(\CP^\infty)^n$, let $\pi_i:\B T\rightarrow\CP^\infty$ be the projection to the $i$-th factor. From the calculation of $\B S^1=\CP^\infty$ above, the cohomology $H^\bullet(\CP^\infty;\mathbb{Z})=\mathbb{Z}[t]$ of each factor is a free abelian group in each degree, so when applying [§Cohomology, ⁋Corollary 10](/en/math/algebraic_topology/cohomology#cor10), no Tor term appears. Therefore, the cross product gives a cohomology ring isomorphism

$$H^\bullet(\B T;\mathbb{Z})\cong\bigotimes_{i=1}^n \mathbb{Z}[t_i]=\mathbb{Z}[t_1,\ldots,t_n]$$

([§Cup Product, ⁋Proposition 3](/en/math/algebraic_topology/cup_products#prop3)), where the generator $t_i$ is the pullback of the generator $t$ of the $i$-th factor by $\pi_i$, that is, $t_i=\pi_i^\ast t$.

Now let us look at the degree $2$ part. A *character* $\rchi:T\rightarrow S^1$ induces

$$\B\rchi:\B T\rightarrow \B S^1=\CP^\infty$$

by functoriality, so the pullbacks $(\B\rchi)^\ast t\in H^2(\B T;\mathbb{Z})$ of the generator $t$ are determined. One can check that this correspondence $\rchi\mapsto(\B\rchi)^\ast t$ gives a homomorphism $\Hom(T,S^1)\rightarrow H^2(\B T;\mathbb{Z})$, and what is decisive is that, as we saw above, the $i$-th coordinate projection $\pr_i:T\rightarrow S^1$ goes exactly to $t_i$. That is, $\B\pr_i$ is exactly the same as the $i$-th projection $\pi_i$, and therefore

$$(\B\pr_i)^\ast t=\pi_i^\ast t=t_i.$$

Thus the standard basis $\{\pr_1,\ldots,\pr_n\}$ of $\Hom(T,S^1)\cong\mathbb{Z}^n$ maps to the basis $\{t_1,\ldots,t_n\}$ of $H^2(\B T;\mathbb{Z})=\bigoplus_i\mathbb{Z}t_i$, so this correspondence is an isomorphism.
:::

This isomorphism allows us to read polynomials on the character lattice as cohomology classes of $\B T$, and becomes central when dealing with invariants of spaces on which a torus acts. For the unitary group, a calculation one step further is needed, but we already saw the result in the previous post.

::: Proposition 13
For the unitary group $\Umat(n)$,

$$H^\bullet(\B\Umat(n);\mathbb{Z})=\mathbb{Z}[c_1,\ldots,c_n],\qquad \lvert c_i\rvert=2i$$

is a polynomial ring generated by the Chern classes $c_i$ of the universal complex bundle.
:::
::: Proof
Since $\B\Umat(n)=\Gr_n(\mathbb{C}^\infty)$, and we already saw after [\[Algebraic Topology\] §Characteristic Classes of Vector Bundles, ⁋Example 8](/en/math/algebraic_topology/characteristic_classes#ex8) that its cohomology ring is a polynomial ring generated by the Chern classes of the universal bundle,

$$H^\bullet(\Gr_n(\mathbb{C}^\infty);\mathbb{Z})=\mathbb{Z}[c_1,\ldots,c_n],$$

it suffices to show only the latter claim.

This calculation is essentially the same as [Corollary 12](#cor12), and the key is, just as before, the map $\B T\rightarrow\B\Umat(n)$ obtained by embedding the maximal torus $T=(S^1)^n\subseteq\Umat(n)$ as diagonal matrices. Restricting the canonical representation $\mathbb{C}^n$ of $\Umat(n)$ to $T$ splits it along the coordinate axes as

$$\mathbb{C}^n=L_1\oplus\cdots\oplus L_n$$

and $T$ acts on the $i$-th line $L_i$ exactly by the character $\pr_i$. Therefore, the pullback of the universal bundle $E$ to $\B T$ is the sum of line bundles $\bigoplus_i\mathcal{L}_i$ attached to each character, and its $i$-th component is exactly the line bundle for which we already computed $c_1(\mathcal{L}_i)=(\B\pr_i)^\ast t=t_i$ in [Corollary 12](#cor12). Applying the Whitney formula here gives

$$c(E)\vert_{\B T}=\prod_{i=1}^n(1+t_i);\qquad c_i\vert_{\B T}=e_i(t_1,\ldots,t_n).$$

Here $e_i$ is the $i$-th elementary symmetric polynomial, and since $\lvert t_i\rvert=2$, we have $\lvert c_i\rvert=2i$. What remains is that $H^\bullet(\B\Umat(n);\mathbb{Z})\rightarrow H^\bullet(\B T;\mathbb{Z})=\mathbb{Z}[t_1,\ldots,t_n]$ is injective and its image is the invariant ring $\mathbb{Z}[t_1,\ldots,t_n]^{S_n}$ of the Weyl group $S_n$; since integer-coefficient symmetric polynomials are freely generated by elementary symmetric polynomials, we have $\mathbb{Z}[t_1,\ldots,t_n]^{S_n}=\mathbb{Z}[e_1,\ldots,e_n]=\mathbb{Z}[c_1,\ldots,c_n]$, and ultimately the cohomology of $\B\Umat(n)$ is the $S_n$-symmetric part of the polynomial ring in [Corollary 12](#cor12). We leave the detailed calculation to [MS].
:::

Since the cohomology of $\B\Umat(n)$ consists entirely of polynomials in the Chern classes, all characteristic classes of a complex vector bundle are polynomials in the Chern classes. In the same way, $H^\bullet(\B\Omat(n);\mathbb{Z}/2)=\mathbb{Z}/2[w_1,\ldots,w_n]$ gives the Stiefel–Whitney class, and for oriented bundles, $\B\SO(n)$ gives the Euler class. When dealing with a space with a $G$-action instead of a single space $X$, $\B G$ and the homotopy quotient over it become the foundation of equivariant cohomology taking this cohomology as the base.

---

**References**

**[Mil]** J. W. Milnor, *Construction of universal bundles, II*, Annals of Mathematics **63** (1956), 430–436.  
**[MS]** J. W. Milnor and J. D. Stasheff, *Characteristic Classes*, Annals of Mathematics Studies 76, Princeton University Press, 1974.  
**[Hat]** A. Hatcher, *Algebraic Topology*, Cambridge University Press, 2002.  
**[tD]** T. tom Dieck, *Algebraic Topology*, EMS Textbooks in Mathematics, European Mathematical Society, 2008.  
**[Hus]** D. Husemoller, *Fibre Bundles*, 3rd ed., Graduate Texts in Mathematics 20, Springer, 1994.
