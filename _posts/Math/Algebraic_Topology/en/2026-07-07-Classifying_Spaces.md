---
title: "Classifying Spaces"
description: "We define principal bundles with an arbitrary topological group as structure group, and classify them using homotopy theory via universal bundles and classifying spaces."
excerpt: "Classification of principal G-bundles and construction of the classifying space BG"

categories: [Math / Algebraic Topology]
permalink: /en/math/algebraic_topology/classifying_spaces
sidebar: 
    nav: "algebraic_topology-en"

date: 2026-07-07
weight: 12
translated_at: 2026-07-07T09:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-07-07T09:30:02+00:00
---
In previous posts, we introduced characteristic classes to classify vector bundles. One of the most interesting aspects was the manner in which their existence was established: we saw how a certain *universal* bundle defined over a large space allows any bundle to be represented as its pullback. For instance, for real vector bundles, the tautological bundle over the infinite real Grassmannian

$$E(\gamma_n^k)\rightarrow \Gr(k, \mathbb{C}^\infty)$$

played this role ([§Stiefel–Whitney Classes, §§Grassmannian Varieties](/en/math/algebraic_topology/stiefel_whitney_classes#그라스만-다양체)), and a similar construction existed for complex vector bundles. ([§Characteristic Classes of Vector Bundles, ⁋Example 8](/en/math/algebraic_topology/characteristic_classes#ex8)) On the other hand, since the pullback of a vector bundle depends only on the homotopy class of the map, the isomorphism class of a rank $$k$$ vector bundle over a fixed space $$B$$ corresponds to the set of homotopy classes of maps from these spaces $$[B, \Gr(k, \mathbb{R}^\infty)]$$ (or $$[B, \Gr(k, \mathbb{C}^\infty)]$$).

Another perspective on vector bundles was to regard them as a collection of transition functions. For example, any vector bundle could be specified by giving

$$g_{ij}: U_i\cap U_j\rightarrow \GL(k;\mathbb{R})$$

on the overlap of two trivializing open sets, and this perspective was powerful in that, for instance, replacing $$\GL(k;\mathbb{R})$$ with $$\GL^+(k;\mathbb{R})$$ also allowed us to describe *oriented* vector bundles.

The goal of this post is to connect these two perspectives. That is, we will define, more generally, the *principal $$G$$-bundle* that appears when the structure group is a (topological) group $$G$$, and define the *classifying space* $$BG$$, which is the space that classifies such bundles. In this post, $$G$$ always denotes a topological group, and unless otherwise stated, the base space is assumed to be paracompact.

## Definition of Principal Bundle

In a vector bundle, the fiber has a vector space structure, and its transition functions are linear automorphisms preserving this structure—that is, elements of $$\GL(k,\mathbb{R})$$. When dealing with a general structure group $$G$$, it is natural to take the fiber itself to be $$G$$ and to give the transition by left translation in $$G$$. A slight subtlety is that there is no distinguished point from this perspective; the identity element of the fiber in one chart is understood as another element of the fiber in another chart via left translation. In other words, these elements should be thought of as *$$G$$-torsors*, and to describe them independently of coordinates, we use a $$G$$-action on the total space.

::: Definition 1
Let a topological group $$G$$ be given, and let a fiber bundle $$p:P\rightarrow X$$ and a continuous right action $$P\times G\rightarrow P$$ on it be given. This data is called a *principal $$G$$-bundle* if the following three conditions are satisfied.

1. The $$G$$-action preserves the fiber. That is, for all $$y\in P$$ and $$g\in G$$, $$p(y\cdot g)=p(y)$$.
2. The $$G$$-action on each fiber is free and transitive. That is, for any $$x\in X$$, fixing a point $$y\in p^{-1}(x)$$, the map $$g\mapsto y\cdot g$$ is a bijection from $$G$$ to $$p^{-1}(x)$$.
3. ($$G$$-equivariant local triviality) For each $$x\in X$$, there exists an open neighborhood $$U$$ and a $$G$$-equivariant homeomorphism $$\varphi:p^{-1}(U)\rightarrow U\times G$$ compatible with $$p$$ over $$U$$. Here, the $$G$$-action on $$U\times G$$ is given by $$(u,h)\cdot g=(u,hg)$$.
:::

Thus, locally, we attach copies of $$G$$ in the fiber direction over the base space, and on each fiber $$G$$ acts by right translation.

Then, a *morphism* between two principal $$G$$-bundles $$P,P'\rightarrow X$$ is a continuous map $$f:P\rightarrow P'$$ satisfying $$p'\circ f=p$$ and compatible with the $$G$$-action, and if this is a homeomorphism, we call it an *isomorphism* between the two principal bundles. Fixing local trivializations $$\varphi_i:p^{-1}(U_i)\rightarrow U_i\times G$$, continuous functions $$g_{ij}:U_i\cap U_j\rightarrow G$$ are determined on $$U_i\cap U_j$$ satisfying $$\varphi_i\circ\varphi_j^{-1}(u,h)=(u,g_{ij}(u)h)$$. These transition functions satisfy the same cocycle condition as in vector bundles,

$$g_{ij}(x)g_{jk}(x)=g_{ik}(x),\qquad g_{ii}(x)=e,$$

and two cocycles $$(g_{ij})$$ and $$(g_{ij}')$$ give the same bundle if and only if there exist continuous functions $$\lambda_i:U_i\rightarrow G$$ such that $$g_{ij}'=\lambda_i g_{ij}\lambda_j^{-1}$$. Therefore, the isomorphism classes of principal $$G$$-bundles trivializing over an open cover $$\{U_i\}$$ are classified by nonabelian Čech cohomology $$\check{H}^1(X;G)$$, and in the case $$G=\GL(k,\mathbb{R})$$, this exactly matches the classification of vector bundles from the previous post.

While a vector bundle always has a zero section, a principal bundle has a fiber that is a $$G$$-torsor rather than $$G$$ itself, so it is not obvious how to pick a section playing this role. Indeed, the following proposition shows that the existence of a section completely determines the triviality of a principal bundle.

::: Proposition 2
A principal $$G$$-bundle $$p:P\rightarrow X$$ is isomorphic to the trivial bundle if and only if a continuous global section $$s:X\rightarrow P$$ exists.
:::
::: Proof
The trivial bundle $$X\times G$$ has the section $$x\mapsto(x,e)$$, so if $$P$$ is trivial, we obtain a section via the isomorphism. Conversely, suppose a section $$s:X\rightarrow P$$ exists, and consider the map

$$\Phi:X\times G\rightarrow P,\qquad (x,g)\mapsto s(x)\cdot g.$$

Since the $$G$$-action on each fiber is simply transitive (condition (2) of [Definition 1](#def1)), the restriction of $$\Phi$$ to the fiber $$\{x\}\times G\rightarrow p^{-1}(x)$$ is bijective, and thus $$\Phi$$ is bijective. By definition, $$\Phi$$ satisfies $$p\circ\Phi=\pr_1$$ and is compatible with the $$G$$-action, so it is a morphism over $$X$$. Finally, that $$\Phi$$ is a homeomorphism can be checked locally: over a trivialization $$\varphi:p^{-1}(U)\rightarrow U\times G$$, if $$s$$ is written in the form $$x\mapsto(x,\sigma(x))$$ ($$\sigma:U\rightarrow G$$ continuous), then $$\Phi$$ becomes $$(x,g)\mapsto(x,\sigma(x)g)$$, and its inverse $$(x,h)\mapsto(x,\sigma(x)^{-1}h)$$ is continuous.
:::

This proposition reveals the decisive difference between principal bundles and vector bundles. Therefore, to relate principal bundles and vector bundles, we need an object that connects the two.

The simplest reason a principal $$G$$-bundle cannot be a vector bundle is that the fiber of a vector bundle is a vector space, not a group. We resolve this by making the following definition.

::: Definition 3
Let a principal $$G$$-bundle $$p:P\rightarrow X$$ and a topological space $$F$$ on which $$G$$ acts continuously from the left be given. Define the $$G$$-action on $$P\times F$$ by

$$(y,f)\cdot g=(y\cdot g,\ g^{-1}\cdot f)$$

and denote its orbit space by $$P\times_G F=(P\times F)/G$$. Then the map $$P\times_G F\rightarrow X$$ induced by $$(y,f)\mapsto p(y)$$ is a fiber bundle with fiber $$F$$, and we call this the *associated bundle* of $$P$$.
:::

Intuitively, this attaches the fiber $$F$$ along the <em>twisted</em> structure of the principal $$G$$-bundle; for example, applying this to the trivial $$G$$-bundle $$X\times G$$ and fiber $$F$$ yields the trivial fiber bundle $$X\times F$$, and similarly, applying it to a slightly twisted (i.e., non-trivial) principal $$G$$-bundle $$P$$ and fiber $$F$$ gives a fiber bundle whose fiber is $$F$$ and which inherits the twisting data from $$P$$.

The most transparent example is a vector bundle, so let us follow the definition step by step here. The topological group $$G=\GL(k, \mathbb{R})$$ acts on the left on the dimension $$k$$ real vector space $$F=V$$. Also, for convenience, let the trivial $$G$$-bundle $$P=X\times G$$ be given. Then first, the $$G$$-action defined on the product space $$P\times F=(X\times G)\times V$$ is

$$\bigl((x,g),v\bigr)\cdot h=\bigl((x, gh),h^{-1}v\bigr)$$

and its orbit space is nothing but $$X\times V$$. This is because taking the action of an arbitrary element $$((x,g),v)$$ by $$h=g^{-1}$$ gives

$$((x,g),v)\cdot g^{-1}=\bigl((x,e),gv\bigr)$$

and in this process, we identify $$(x,e)$$ in $$X\times G$$ with the element $$x$$ of $$X$$, using the fact that the formula

$$[((x,g),v)]\mapsto(x,gv)$$

is a well-defined homeomorphism. That is, starting from a trivial $$G$$-bundle, the associated bundle is also trivial.

More generally, if $$P$$ is given by transition functions $$g_{ij}$$ over $$\{U_i\}$$, then $$P\times_G F$$ becomes the bundle with fiber $$F$$ over the same $$U_i$$ and transition given by the action of $$g_{ij}$$ on $$F$$.

The reverse construction is also possible. Given a rank $$n$$ vector bundle $$E\rightarrow X$$, the space of all ordered bases, i.e., *frames*, of the fiber $$E_x$$ over each $$x$$,

$$\Fr(E)=\{(x,b)\mid x\in X,b\text{ an ordered basis of $E_x$}\}$$

becomes a principal $$\GL(n,\mathbb{R})$$-bundle under the action of $$\GL(n,\mathbb{R})$$ sending a basis to a matrix, and we call this the *frame bundle* of $$E$$. The following proposition shows that these two constructions are inverse to each other.

::: Proposition 4
Over a topological space $$X$$, there exists a natural one-to-one correspondence between the isomorphism classes of principal $$\GL(n,\mathbb{R})$$-bundles and the isomorphism classes of rank $$n$$ real vector bundles. This correspondence assigns to a principal bundle $$P$$ the associated bundle $$P\times_{\GL(n,\mathbb{R})}\mathbb{R}^n$$, and to a vector bundle $$E$$ the frame bundle $$\Fr(E)$$.
:::
::: Proof
It suffices to verify that the two correspondences are inverse to each other. A point of the frame bundle $$\Fr(E)$$ is a basis of the fiber $$E_x$$, that is, a linear isomorphism $$b:\mathbb{R}^n\xrightarrow{\cong}E_x$$. Then the map

$$\Fr(E)\times_{\GL(n,\mathbb{R})}\mathbb{R}^n\rightarrow E,\qquad [(b,v)]\mapsto b(v)$$

is well-defined. This is because even if we change $$(b,v)$$ to $$(b\circ A, A^{-1}v)$$, the value is the same, not in the form $$b(Av\cdot A^{-1})$$ but as $$(b\circ A)(A^{-1}v)=b(v)$$. Since this map is a linear isomorphism on each fiber, it is an isomorphism of vector bundles. Conversely, starting from a principal bundle $$P$$, we verify that the frame bundle of $$P\times_G\mathbb{R}^n$$ is again isomorphic to $$P$$ by checking that the transition functions $$g_{ij}$$ match on both sides via local trivialization. Both constructions preserve transition functions, so they preserve isomorphism classes, and the naturality of the maps follows from compatibility with pullback.
:::

Thanks to this equivalence, every classification problem for vector bundles translates into a problem for principal $$\GL(n,\mathbb{R})$$-bundles. In the same way, complex vector bundles correspond to principal $$\GL(n,\mathbb{C})$$-bundles, and oriented real vector bundles correspond to principal $$\GL^+(n,\mathbb{R})$$-bundles. Therefore, if we can classify principal $$G$$-bundles for an arbitrary structure group $$G$$, all these cases are solved at once.

Just as with vector bundles, given a continuous map $$f:X'\rightarrow X$$ and a principal $$G$$-bundle $$p:P\rightarrow X$$, the *pullback bundle*

$$f^\ast P=\{(x',y)\in X'\times P\mid f(x')=p(y)\}$$

is defined. Giving the action $$(x',y)\cdot g=(x',y\cdot g)$$ makes $$f^\ast P\rightarrow X'$$ again a principal $$G$$-bundle, and from the perspective of transition functions, this corresponds to pulling back $$g_{ij}$$ to $$g_{ij}\circ f$$. The crucial fact is that this pullback depends only on the homotopy class of $$f$$.

::: Theorem 5 (Homotopy Invariance of Pullback)
Let $$X$$ be paracompact and let $$f_0,f_1:X\rightarrow Y$$ be homotopic. ([§Homotopy, ⁋Definition 2](/en/math/algebraic_topology/homotopy#def2)) Then for any principal $$G$$-bundle $$p:P\rightarrow Y$$, $$f_0^\ast P$$ and $$f_1^\ast P$$ are isomorphic over $$X$$.
:::
::: Proof
The key is the following fact.

> When $$X$$ is paracompact, a principal $$G$$-bundle $$Q$$ over $$X\times[0,1]$$ is isomorphic to the pullback of its restriction to $$X\times\{0\}$$ by the projection $$X\times[0,1]\rightarrow X\times\{0\}$$.

This is the covering homotopy property of bundles, relying on the fact that a trivializing cover of a bundle over a paracompact base admits a locally finite partition of unity. The gist of the proof is to divide $$[0,1]$$ into small intervals, connect trivializations over each interval, and glue these local isomorphisms using a partition of unity.

Now let a homotopy $$H:X\times[0,1]\rightarrow Y$$ connecting $$f_0,f_1$$ be given and define $$Q=H^\ast P$$. By the above fact, $$Q$$ is isomorphic to the pullback of $$Q\vert_{X\times\{0\}}=f_0^\ast P$$ by the projection, and repeating the same argument at the end $$X\times\{1\}$$, $$Q\vert_{X\times\{1\}}=f_1^\ast P$$ is also isomorphic to the same bundle. Since $$[0,1]$$ is connected, the restrictions at both endpoints become isomorphic to the same bundle over $$X$$, yielding $$f_0^\ast P\cong f_1^\ast P$$.
:::

In particular, if $$X$$ is contractible, then the identity map is homotopic to a constant map, so every principal $$G$$-bundle over $$X$$ is trivial. Since CW complexes are always paracompact, the hypothesis of the above theorem is automatically satisfied for the bases we wish to consider.

## Universal Bundle and Classifying Space

[Theorem 5](#thm5) tells us that the correspondence sending a function $$f$$ to $$f^\ast P$$ depends on the homotopy class. Therefore, if we can take some fixed principal $$G$$-bundle as a source from which all other bundles can be obtained by pullback, the classification of principal $$G$$-bundles would be reduced to counting homotopy classes into that source space, which generalizes the fact that the universal bundle over $$\Gr_k(\mathbb{R}^\infty)$$ was such a source in the case of vector bundles.

::: Definition 6
For a topological group $$G$$, a principal $$G$$-bundle $$p:EG\rightarrow BG$$ is called a *universal bundle* if the total space $$EG$$ is contractible, that is, $$EG$$ is homotopy equivalent to a point. ([§Homotopy, ⁋Definition 4](/en/math/algebraic_topology/homotopy#def4)) In this case, we call the base space $$BG$$ the *classifying space* of $$G$$.
:::

That is, a universal bundle is a free $$G$$-action on a contractible space, and $$BG$$ is its orbit space $$EG/G$$. The existence of such a space is not obvious, but Milnor gave a construction for any topological group.

::: Theorem 7 (Milnor)
For any topological group $$G$$, a universal bundle $$EG\rightarrow BG$$ exists.
:::
::: Proof
Milnor's construction uses the infinite join $$EG=G\ast G\ast G\ast\cdots$$ of $$G$$. The diagonal right translation is free, and since the join of two spaces raises connectivity by $$\conn(A\ast B)\geq\conn(A)+\conn(B)+2$$, the colimit $$EG$$ is connected in every dimension, hence weakly contractible (and thus contractible under a CW structure), and $$EG\rightarrow EG/G=BG$$ becomes a principal $$G$$-bundle. For details, we follow §14 of [Mil] and [tD].
:::

The universal bundle is essentially unique. Given two universal bundles $$EG\rightarrow BG$$ and $$EG'\rightarrow BG'$$, since $$EG'$$ is contractible, by Theorem 5 there exists a classifying map pulled back to $$BG$$, and applying this argument in both directions yields that $$BG$$ and $$BG'$$ are connected by maps that are homotopy inverse to each other. Thus, $$BG$$ is determined without ambiguity beyond homotopy equivalence, and we speak of *the* classifying space.

## Classification Theorem

We now state the central result of classification theory. This is the point that justifies the name "classifying space."

::: Theorem 8 (Classification Theorem)
Let $$X$$ be a paracompact space (e.g., a CW complex) and let $$[X,BG]$$ be the set of free homotopy classes from $$X$$ to $$BG$$. Then the map pulling back the universal bundle $$EG\rightarrow BG$$

$$[X,BG]\xrightarrow{\ \cong\ }\{X\text{ 위의 principal }G\text{-bundle}\}/\cong,\qquad [f]\mapsto f^\ast EG$$

is a well-defined bijection, and is natural in the sense that it is compatible with pullback along maps $$X'\rightarrow X$$.
:::
::: Proof
That $$[f]\mapsto f^\ast EG$$ does not depend on the choice of representative for $$[f]$$ is by [Theorem 5](#thm5). We show surjectivity and injectivity in turn.

**Surjectivity.** Let a principal $$G$$-bundle $$P$$ over $$X$$ be given. Since $$X$$ is paracompact, we can take an open cover $$\{U_i\}$$ trivializing $$P$$ together with a locally finite partition of unity $$\{\rho_i\}$$ subordinate to it (with each $$\operatorname{supp}\rho_i\subseteq U_i$$). The trivialization over each $$U_i$$ gives a $$G$$-equivariant map $$\psi_i:p^{-1}(U_i)\rightarrow G$$, so

$$\widetilde{f}:P\rightarrow EG,\qquad y\mapsto \sum_i \rho_i(p(y))\psi_i(y)$$

is a well-defined $$G$$-equivariant continuous map (it is a finite sum at each point, and $$\psi_i$$ appears only where $$\rho_i>0$$). A $$G$$-equivariant map descends to a map $$f:X\rightarrow BG$$ between base spaces, and since $$\widetilde{f}$$ is an isomorphism on each fiber, we obtain $$P\cong f^\ast EG$$.

**Injectivity.** Let $$f_0,f_1:X\rightarrow BG$$ be such that $$f_0^\ast EG\cong f_1^\ast EG=:P$$. Each classifying map $$f_i$$ has as a lift a bundle map $$P\cong f_i^\ast EG\rightarrow EG$$, that is, a $$G$$-equivariant continuous map $$\Phi_i:P\rightarrow EG$$ from $$P$$ to the universal bundle inducing $$f_i$$ on the base. However, since $$EG$$ is contractible, any two $$G$$-equivariant maps from a principal bundle $$P$$ over a paracompact space to $$EG$$ are $$G$$-equivariantly homotopic. Thus, there exists a $$G$$-equivariant homotopy $$P\times[0,1]\rightarrow EG$$ connecting $$\Phi_0$$ and $$\Phi_1$$, and this descends to the base to give a homotopy between $$f_0$$ and $$f_1$$, so $$[f_0]=[f_1]$$. The fact that the two $$G$$-equivariant maps are $$G$$-homotopic itself relies on the contractibility of $$EG$$ and the paracompactness of $$X$$.

Details for both steps follow §14 of [Mil], [tD], and §4 of [Hus].
:::

![Pullback square of the classifying map](/assets/images/Math/Algebraic_Topology/Classifying_Spaces-1.svg){:style="width:8.21em" class="invert" .align-center}

The classification theorem translates the geometric classification of principal $$G$$-bundles into purely homotopy-theoretic data $$[X,BG]$$. Combined with [Proposition 4](#prop4), the classification of rank $$n$$ real vector bundles is reduced to $$[X,B\GL(n,\mathbb{R})]$$, and in the complex case to $$[X,B\GL(n,\mathbb{C})]$$, and we will soon see that this is the same content as the classification via Grassmannians from the previous post.

::: Lemma 9
The construction of the classifying space is functorial in $$G$$. Given a continuous group homomorphism $$\phi:G\rightarrow H$$, the associated bundle $$EG\times_G H$$ obtained by changing the $$G$$-action on $$EG$$ to an $$H$$-action via $$\phi$$ induces a map $$B\phi:BG\rightarrow BH$$ classifying it. This satisfies $$B(\psi\circ\phi)\simeq B\psi\circ B\phi$$, making $$G\mapsto BG$$ a functor on the homotopy category. For example, the inclusion $$\Umat(n)\hookrightarrow\GL(n,\mathbb{C})$$ induces $$B\Umat(n)\rightarrow B\GL(n,\mathbb{C})$$, which is used below.
:::

## Examples of Classifying Spaces

The simplest yet most suggestive case is when $$G$$ is a discrete group. In this case, a principal $$G$$-bundle is a fiber bundle whose fiber is a discrete set, that is, a regular covering space with $$G$$ as its deck transformation group.

::: Example 10
Let $$G$$ be a discrete group. In the universal bundle $$EG\rightarrow BG$$, since $$EG$$ is contractible and $$G$$ acts freely and discretely, $$EG\rightarrow BG$$ is the universal cover of $$BG$$ and its deck transformation group is $$G$$. ([§Covering Spaces, ⁋Theorem 11](/en/math/algebraic_topology/covering_spaces#thm11)) Therefore, $$\pi_1(BG)\cong G$$, and since $$EG$$ is contractible, the universal cover of $$BG$$ is also contractible, so $$\pi_n(BG)=0$$ for $$n\geq 2$$. That is, $$BG$$ is an Eilenberg–MacLane space $$K(G,1)$$.

From this, concrete classifying spaces are read directly from covering space theory. For $$G=\mathbb{Z}/2$$, since $$S^\infty$$ is contractible and the antipodal action is free, we have $$E(\mathbb{Z}/2)=S^\infty$$ and $$B(\mathbb{Z}/2)=S^\infty/(\mathbb{Z}/2)=\RP^\infty$$. For $$G=\mathbb{Z}$$, we obtain $$B\mathbb{Z}=\mathbb{R}/\mathbb{Z}=S^1$$ from the translation action on $$\mathbb{R}$$, which exactly matches the fact that the universal cover $$\mathbb{R}\rightarrow S^1$$ of $$S^1$$ has deck group $$\mathbb{Z}$$. ([§Covering Spaces, ⁋Corollary 12](/en/math/algebraic_topology/covering_spaces#cor12))
:::

In the case of continuous groups, the most basic example is the circle group $$G=S^1$$. $$S^1$$ acts freely on $$\mathbb{C}^\infty\setminus\{0\}$$ by scalar multiplication, and this space deformation retracts onto the unit sphere $$S^\infty=\varinjlim_n S^{2n-1}$$, which is contractible, so $$ES^1=\mathbb{C}^\infty\setminus\{0\}$$ and its orbit space is the space of complex lines

$$BS^1=(\mathbb{C}^\infty\setminus\{0\})/S^1=\CP^\infty.$$

On the other hand, $$\CP^\infty=\Gr_1(\mathbb{C}^\infty)$$ is the classifying space of $$\Umat(1)=S^1$$, exactly the space written as $$B\Umat(1)$$ in the previous post, and thus $$BS^1=B\Umat(1)=\CP^\infty$$. More generally, for the $$n$$-dimensional torus $$T=(S^1)^n$$, since the product goes to the product of classifying spaces,

$$BT=B(S^1)^n=(\CP^\infty)^n.$$

In the same way, for any $$n$$, the classifying spaces of the unitary group and the orthogonal group are realized by the infinite Grassmannians from the previous post. That is, $$B\Umat(n)=\Gr_n(\mathbb{C}^\infty)$$ and $$B\Omat(n)=\Gr_n(\mathbb{R}^\infty)$$, because the frame bundle of the universal vector bundle over $$\Gr_n(\mathbb{C}^\infty)$$ gives the universal principal $$\Umat(n)$$-bundle, and its total space (the colimit of Stiefel spaces) is contractible.

Finally, the fact that the classifying spaces of the general linear group and its maximal compact subgroup have the same homotopy type is frequently used in classification theory.

::: Example 11
The inclusion $$\Umat(n)\hookrightarrow\GL(n,\mathbb{C})$$ induces a homotopy equivalence

$$B\Umat(n)\xrightarrow{\ \simeq\ }B\GL(n,\mathbb{C}).$$

This comes from the Gram–Schmidt orthogonalization deformation retracting $$\GL(n,\mathbb{C})$$ onto $$\Umat(n)$$. Specifically, any matrix in $$\GL(n,\mathbb{C})$$ decomposes uniquely as a product of a unitary matrix and a positive definite upper-triangular matrix ($$QR$$ decomposition), and continuously contracting the upper-triangular factor toward the identity yields that $$\GL(n,\mathbb{C})$$ deformation retracts onto $$\Umat(n)$$. This homotopy equivalence at the group level passes through $$B$$ to give a homotopy equivalence at the classifying space level. Therefore, reducing the structure group of a rank $$n$$ complex vector bundle from $$\GL(n,\mathbb{C})$$ to $$\Umat(n)$$ causes no loss in classification, and this is the classifying-space version of the fact that every complex bundle can be given a Hermitian metric.
:::

## Cohomology of Classifying Spaces

According to the classification theorem, a characteristic class of a bundle with structure group $$G$$ is the pullback of a cohomology class of $$BG$$ by the classifying map. Therefore, characteristic class theory is the same as computing the cohomology ring of $$BG$$, and we summarize this for the most basic groups.

The starting point is the cohomology ring of complex projective space. In the previous post, we saw that

$$H^\bullet(\CP^\infty;\mathbb{Z})=\mathbb{Z}[x],\qquad \lvert x\rvert=2$$

and the generator $$x$$ was the first Chern class of the tautological line bundle. ([§Characteristic Classes of Vector Bundles, ⁋Example 8](/en/math/algebraic_topology/characteristic_classes#ex8)) Since $$BS^1=\CP^\infty$$, this means

$$H^\bullet(BS^1;\mathbb{Z})=\mathbb{Z}[t],\qquad \lvert t\rvert=2.$$

The case of the torus follows from the cohomology of a product space.

::: Corollary 12
For the $$n$$-dimensional torus $$T=(S^1)^n$$,

$$H^\bullet(BT;\mathbb{Z})=\mathbb{Z}[t_1,\ldots,t_n],\qquad \lvert t_i\rvert=2$$

is a polynomial ring generated by $$n$$ degree $$2$$ generators. Moreover, the degree $$2$$ part $$H^2(BT;\mathbb{Z})$$ is canonically isomorphic to the character lattice $$\Hom(T,S^1)$$, and $$H^\bullet(BT;\mathbb{Z})$$ is the symmetric algebra on this lattice.
:::
::: Proof
Since $$BT=(\CP^\infty)^n$$, and from the calculation of $$BS^1=\CP^\infty$$ in the previous section, the cohomology $$H^\bullet(\CP^\infty;\mathbb{Z})=\mathbb{Z}[t_i]$$ of each factor is a free abelian group in each degree, so no Tor terms appear in the Künneth theorem. Therefore, the cross product gives an isomorphism of cohomology rings

$$H^\bullet(BT;\mathbb{Z})\cong\bigotimes_{i=1}^n \mathbb{Z}[t_i]=\mathbb{Z}[t_1,\ldots,t_n].$$

([§Cup Products](/en/math/algebraic_topology/cup_products)) A character $$\chi:T\rightarrow S^1$$ induces $$B\chi:BT\rightarrow BS^1=\CP^\infty$$ ([Lemma 9](#lem9)) and corresponds to $$B\chi^\ast(t)\in H^2(BT;\mathbb{Z})$$, and since the $$i$$-th coordinate projection $$T\rightarrow S^1$$ goes to $$t_i$$, this correspondence is the isomorphism sending $$\Hom(T,S^1)\cong\mathbb{Z}^n$$ to $$H^2(BT;\mathbb{Z})=\bigoplus_i\mathbb{Z}t_i$$. Since the polynomial ring is the symmetric algebra on its degree $$2$$ part, the final claim follows.
:::

This isomorphism allows us to read polynomials on the character lattice as cohomology classes of $$BT$$, and becomes central when dealing with invariants of spaces with a torus action. The case of the unitary group requires a calculation one step further, but we already saw the result in the previous post.

::: Proposition 13
For the unitary group $$\Umat(n)$$,

$$H^\bullet(B\Umat(n);\mathbb{Z})=\mathbb{Z}[c_1,\ldots,c_n],\qquad \lvert c_i\rvert=2i$$

is a polynomial ring generated by the Chern classes $$c_i$$ of the universal complex bundle.
:::
::: Proof
Since $$B\Umat(n)=\Gr_n(\mathbb{C}^\infty)$$, we stated in the previous post that its cohomology ring is the polynomial ring generated by the Chern classes of the universal bundle

$$H^\bullet(\Gr_n(\mathbb{C}^\infty);\mathbb{Z})=\mathbb{Z}[c_1,\ldots,c_n].$$

([§Characteristic Classes of Vector Bundles](/en/math/algebraic_topology/characteristic_classes)) The gist of its proof is that the map $$BT\rightarrow B\Umat(n)$$ induced by the maximal torus $$T\subset\Umat(n)$$ gives an injection in cohomology onto the invariants under the action of the Weyl group $$S_n$$, and the $$S_n$$-invariant part inside $$\mathbb{Z}[t_1,\ldots,t_n]$$ of [Corollary 12](#cor12) is $$\mathbb{Z}[c_1,\ldots,c_n]$$ generated by the elementary symmetric polynomials. Here, $$c_i$$ is expressed as the $$i$$-th elementary symmetric polynomial in $$t_1,\ldots,t_n$$, which is the same formula as decomposing the Chern class into Chern roots in the splitting principle. The complete calculation follows §14 of [MS].
:::

Since the cohomology of $$B\Umat(n)$$ consists entirely of polynomials in the Chern classes, every characteristic class of a complex vector bundle is a polynomial in the Chern classes. In the same way, $$H^\bullet(B\Omat(n);\mathbb{Z}/2)=\mathbb{Z}/2[w_1,\ldots,w_n]$$ is classified by the Stiefel–Whitney class, and for oriented bundles, the Euler class appears in the cohomology of $$B\SO(n)$$. When dealing with a space with a $$G$$-action instead of a space $$X$$, $$BG$$ and the homotopy quotient over it form the basis of equivariant cohomology, which takes this cohomology as its base.

---

**References**

**[Mil]** J. W. Milnor, *Construction of universal bundles, II*, Annals of Mathematics **63** (1956), 430–436.

**[MS]** J. W. Milnor and J. D. Stasheff, *Characteristic Classes*, Annals of Mathematics Studies 76, Princeton University Press, 1974.

**[Hat]** A. Hatcher, *Algebraic Topology*, Cambridge University Press, 2002.

**[tD]** T. tom Dieck, *Algebraic Topology*, EMS Textbooks in Mathematics, European Mathematical Society, 2008.

**[Hus]** D. Husemoller, *Fibre Bundles*, 3rd ed., Graduate Texts in Mathematics 20, Springer, 1994.
