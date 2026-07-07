---
title: "Stiefel-Whitney Characteristic Classes"
description: "This post defines fiber bundles and vector bundles, then introduces Stiefel-Whitney characteristic classes through Cech cohomology and discusses the infinite Grassmannian as their classifying space."
excerpt: "Vector bundles, Stiefel-Whitney classes, and the infinite Grassmannian"

categories: [Math / Algebraic Topology]
permalink: /en/math/algebraic_topology/stiefel_whitney_classes
sidebar: 
    nav: "algebraic_topology-en"

date: 2025-10-07
weight: 10
translated_at: 2026-07-07T07:30:01+00:00
translation_source: kimi-cli
last_polished_at: 2026-07-07T07:30:01+00:00
---
In the previous post, the map $$p:\Spe(\or_M^A)\rightarrow M$$ played an important role as a covering space, and it satisfied the following properties.

1. For any $$x\in M$$, we have $$p^{-1}(x)\cong \{x\}\times A^\times$$.
2. Moreover, for any $$x\in M$$, there exists a suitable open set $$U$$ such that $$p^{-1}(U)\cong U\times A^\times$$.

We now generalize this further and examine the case where the fiber $$p^{-1}(x)$$ carries additional structure (not merely a discrete set). The most general definition is as follows.

::: Definition 1
For a continuous surjection $$p:E \rightarrow B$$ between topological spaces and a topological space $$F$$, a *fiber bundle* is one for which, for each $$x\in B$$, there exists an open set $$U$$ and a homeomorphism $$\phi:U\times F\rightarrow p^{-1}(U)$$ making the following diagram commute:

![fiber_bundle](/assets/images/Math/Algebraic_Topology/Stiefel_Whitney_Classes-1.svg){:style="width:10.09em" class="invert" .align-center}

:::

In this case, $$B$$ is called the *base space*, $$E$$ the *total space*, and $$F$$ the *fiber* of this bundle; if we may take $$U=B$$, then this fiber bundle is called a *trivial bundle*. For example, in the preceding example, $$M$$ is the base space, $$\Spe(\or_M^A)$$ is the total space, and $$A^\times$$ equipped with the discrete topology is the fiber. More generally, any covering space can be regarded as a fiber bundle whose fiber has the discrete topology.

The two cases of particular interest to us are when the fiber $$F$$ is a vector space and when it is a topological group. For convenience, we henceforth assume that $$B$$ is connected.

## Vector Bundles

First, we consider the case where $$F$$ is a vector space. When the fiber $$F$$ is a topological group, it already carries a topology, so the topology on the product space $$U\times F$$ in [Definition 1](#def1) is clear; however, when $$F$$ is a vector space, this is somewhat ambiguous. The most general setting would use a topological vector space $$V$$ over a topological ring $$\mathbb{K}$$, but for convenience, we shall for now consider only the case where the base field of $$F$$ is $$\mathbb{R}$$ and $$F$$ is equipped with the metric topology coming from a canonical inner product.

::: Definition 2
For a fiber bundle $$p:E \rightarrow B$$, suppose the fiber space $$F$$ is an $$\mathbb{R}$$-vector space with the topology as above, and moreover, for any $$x\in B$$ and the homeomorphism $$\phi:U\times  F\rightarrow p^{-1}(U)$$ from [Definition 1](#def1), the function

$$\phi(x,-):F \rightarrow p^{-1}(x);\qquad v\mapsto \phi(x,v)$$

is an isomorphism of vector spaces.
:::

Through this, each fiber $$p^{-1}(x)$$ is endowed with a vector space structure inherited from $$F$$. In general, given two vector bundles $$p_1:E_1 \rightarrow B_1$$ and $$p_2:E_2\rightarrow B_2$$, a *morphism* between them means a commutative diagram of continuous functions

![morphism_of_bundles](/assets/images/Math/Algebraic_Topology/Stiefel_Whitney_Classes-2.svg){:style="width:7.15em" class="invert" .align-center}

where, restricting $$g$$ to $$p^{-1}(x)\rightarrow p_2^{-1}(f(x)))$$ for each $$x\in B_1$$, this function must be a linear map between vector spaces. How to define an isomorphism between vector bundles is obvious.

Meanwhile, in [Definition 2](#def2) above, we considered only the case where $$F$$ is an $$\mathbb{R}$$-vector space, and we defined the topology on it using the inner product structure on $$\mathbb{R}^n$$ and the topology of $$\mathbb{R}$$. But strictly speaking, the only information needed here is the topology of the vector space $$F$$, and when we view $$F$$ as an inner product space, this is called a *Euclidean bundle*. In any case, since we will mostly consider only $$\mathbb{R}$$-vector spaces, we shall gloss over this distinction.

::: Example 3
As a non-trivial example, there is the orientation double cover of the Möbius strip. On the other hand, in [§Poincaré Duality, ⁋Example 5](/en/math/algebraic_topology/Poincare_duality#ex5), we also considered the non-trivial cover of $$S^1$$, which can be generalized geometrically as follows.

For an $$(n+1)$$-dimensional vector space $$\mathbb{R}^{n+1}$$, we call the space of lines passing through the origin the *projective $$n$$-space* and denote it by $$\RP^n$$. Since among the points on a line through the origin, the two points at distance $$1$$ from the origin specify the same line, we can think of this as the quotient space obtained by identifying antipodal points on the unit $$n$$-sphere $$S^n$$.

Now let us take this space $$\RP^n$$ as the base space $$B$$ and define the vector bundle $$E(\gamma_n^1)$$ over it as follows. As a set,

$$E(\gamma_n^1)=\{((x,v)\in \RP^n\times \mathbb{R}^{n+1}\mid x\in \span(x)\}$$

and the projection $$\gamma_n^1:E(\gamma_n^1)\rightarrow \RP^n$$ is projection onto the first coordinate. That is, $$\gamma_n^1$$ attaches to each point $$x\in \RP^n$$ precisely the line that $$x$$ originally belonged to in $$\mathbb{R}^{n+1}$$.

This is not a trivial bundle. If it were, there would exist a non-vanishing continuous section $$\RP^n\rightarrow E(\gamma_n^1)$$. For instance, the function assigning the element $$1$$ in the fiber to every point of $$B$$ would be such. But given any section $$s:\RP^n \rightarrow E(\gamma_n^1)$$, consider the following composition using the quotient map $$q:S^n \rightarrow \RP^n$$:

$$S^n \overset{q}{\longrightarrow} \RP^n \overset{s}{\longrightarrow} E\overset{\pr_2}{\longrightarrow} \mathbb{R}^{n+1}$$

This function sends $$\mathbf{x}\in S^n\subset\mathbb{R}^{n+1}$$ to a scalar multiple of $$\mathbf{x}$$. Letting this scalar be $$t(\mathbf{x})$$, then $$t$$ is a continuous function from $$S^n$$ to $$\mathbb{R}$$, and because of the quotient map $$q$$, it satisfies

$$t(-\mathbf{x})=-t(\mathbf{x}).$$

Now since $$S^n$$ is connected, by the intermediate value theorem there exists $$\mathbf{x}_0\in S^n$$ such that $$t(\mathbf{x}_0)=0$$.
:::

More generally, the following holds.

::: Proposition 4
For a vector bundle $$E$$ of rank $$n$$ over a topological space $$B$$, $$E$$ being a trivial bundle is equivalent to the existence of $$n$$ everywhere linearly independent sections $$s_1,\ldots, s_n$$.
:::

Meanwhile, given any vector bundle $$p:E \rightarrow B$$ and any continuous function $$f:B'\rightarrow B$$, we can define a new vector bundle $$f^\ast E \rightarrow B'$$ by the formula

$$f^\ast E=\{(x,v)\in B'\times E\mid f(x)=p(v)\}\subset E.$$

We call this the *pullback bundle*, and it is not difficult to see that any vector bundle $$E' \rightarrow B'$$ satisfying the above condition factors through $$f^\ast E$$.

Meanwhile, given any two vector bundles $$p_1:E_1\rightarrow B_1$$ and $$p_2:E_2\rightarrow B_2$$, their product

$$p_1\times p_2: E_1\times E_2 \rightarrow B_1\times B_2$$

is also a vector bundle over $$B_1\times B_2$$. Now if $$B_1=B_2=B$$, then as usual, using the diagonal map

$$\Delta: B\rightarrow B\times B$$

the pullback bundle $$\Delta^\ast(p_1\times p_2)$$ becomes a bundle over $$B$$. We call this the *Whitney sum* of the two vector bundles $$E_1\rightarrow B$$ and $$E_2\rightarrow B$$, and denote it by $$p_1\oplus p_2:E_1\oplus E_2\rightarrow B$$. As the notation suggests, fiberwise this corresponds to the direct sum of the fibers of the two vector bundles $$E_1$$ and $$E_2$$.

Although we have not given detailed proofs, in a similar way we can lift operations defined on each fiber (i.e., vector space) to vector bundles. For example, for two vector bundles $$E_1\rightarrow B$$ and $$E_2 \rightarrow B$$, we can form their tensor product bundle $$E_1\otimes E_2 \rightarrow B$$, and it is also possible to use operations such as $$\Hom$$ and $$\bigwedge$$.

## Čech Cohomology

At this point, we establish another cohomology theory. Like sheaf cohomology ([§Poincaré Duality, ⁋Definition 15](/en/math/algebraic_topology/Poincare_duality#def15)), this is a cohomology for sheaves defined over a topological space, and since via the étale space construction we can regard a sheaf whose stalks are vector spaces as the same thing as a vector bundle, it plays an important role in our discussion.

Sheaf cohomology showed that the cohomology captures the obstruction to the existence of global sections of a sheaf. The Čech cohomology we now examine gives a similar result, but differs in that it answers this by examining the process of gluing local sections together to make a global section. In any case, for nice cases including manifolds, Čech cohomology gives the same result as sheaf cohomology, and thus the Čech cohomology of a constant sheaf recovers the cohomology we originally knew.

Let $$X$$ be a topological space, $$\mathcal{F}$$ a sheaf defined on it, and $$\mathcal{U}=\{U_i\}_{i\in I}$$ an open cover of $$X$$. For each $$p\geq 0$$, the group of *Čech $$p$$-cochains* is defined by the formula

$$\check{C}^p(\mathcal{U},\mathcal{F})=\prod_{i_0,\ldots,i_p}\mathcal{F}(U_{i_0}\cap \cdots\cap U_{i_p}).$$

That is, this is the collection of sections defined over all $$p$$-fold intersections. The differential

$$\check{C}^p(\mathcal{U},\mathcal{F})\rightarrow \check{C}^{p+1}(\mathcal{U}, \mathcal{F})$$

is given by the formula

$$(\delta c)_{i_0,\ldots, i_{p+1}}=\sum_{k=0}^{p+1} (-1)^k c_{i_0,\ldots,\hat{i}_k,\ldots,i_{p+1}}\vert_{U_{i_0}\cap\cdots\cap U_{i_{p+1}}}.$$

Then *Čech cohomology* is given by the formula

$$\check{H}^p(\mathcal{U}, \mathcal{F})=\frac{\ker(\check{C}^p\rightarrow \check{C}^{p+1})}{\im(\check{C}^{p-1}\rightarrow \check{C}^{p})}.$$

If $$\mathcal{U}$$ is a sufficiently good cover, for example if any finite intersection is contractible or is acyclic for $$\mathcal{F}$$, then we obtain a canonical isomorphism

$$H^p(X,\mathcal{F})\cong \check{H}^p(\mathcal{U},\mathcal{F}).$$

Now any rank $$n$$ vector bundle is determined by how its fiber is attached over an open cover. That is, it is determined by functions

$$g_{ij}:U_{ij}=U_i\cap U_j \rightarrow \GL(n;\mathbb{R})$$

These must satisfy the condition

$$g_{ij}\cdot g_{jk}\cdot g_{ki}=\id$$

and if this condition were not present, on the triple intersection $$U_i\cap U_j\cap U_k$$, bringing the local trivialization of $$U_i$$ to $$U_j$$ via $$g_{ij}$$, then to $$U_k$$ via $$g_{jk}$$, and then back to $$U_i$$ via $$g_{ki}$$, the trivialization would differ, but in reality it does not. Then the transition functions $$g_{ij}$$ become Čech 1-cochains, and thus fixing a local trivialization $$U_i\rightarrow \GL(n;\mathbb{R})$$, we know there is a one-to-one correspondence between isomorphism classes of rank $$n$$ vector bundles and 1-cochains. That is, there is a one-to-one correspondence between isomorphism classes of rank $$n$$ vector bundles trivializable over an open cover $$U$$ and $$\check{H}^1(\mathcal{U}, \GL(n;\mathbb{R}))$$.

Earlier, in [§Poincaré Duality, ⁋Proposition 7](/en/math/algebraic_topology/Poincare_duality#prop7), we saw that the $$A$$-orientability of a manifold $$M$$ is defined by the group homomorphism

$$\pi_1(M,x)\rightarrow A^\times.$$

On the other hand, since $$A$$ is a commutative ring, the above group homomorphism factors through the abelian group homomorphism

$$H_1(M)\rightarrow A^\times$$

and by [§Cohomology, ⁋Proposition 3](/en/math/algebraic_topology/cohomology#prop3), this is an element of $$H^1(M;A)$$. If this element is $$0$$, this is the same as the monodromy action being the trivial action, which means that $$\Spe(\or_M^A)$$ is a trivial covering space, so that $$M$$ becomes an $$A$$-orientable manifold. On the other hand, for any commutative ring $$A$$, since the initial object of $$\cRing$$ is $$\mathbb{Z}$$, for any manifold $$M$$, once a $$\mathbb{Z}$$-orientation $$H_1(M)\rightarrow \mathbb{Z}^\times$$ is determined, we can compose it with $$\mathbb{Z}^\times\rightarrow A^\times$$ to determine an $$A$$-orientation $$H_1(M)\rightarrow A^\times$$; thus, we know that the essential information about whether $$\Spe(\or_M^A)$$ is a trivial cover lies in $$H^1(M;\mathbb{Z}/2)$$, and thinking of $$\mathbb{Z}/2$$ as $$\GL(1;\mathbb{Z})$$, this is an example of how first cohomology carries information about covering spaces.

In this way, the information about a vector bundle $$E\rightarrow B$$ of rank $$k$$ can be regarded as contained in $$\check{H}^1(B; \underline{\GL(k,\mathbb{R})})$$. However, since the coefficients of the cohomology of $$B$$ that we use are $$\mathbb{Z}$$, it does not contain all the data stored there. Instead, our goal is to find weaker substitutes for this, namely invariants in the cohomology ring $$H^\bullet(B)$$.

## Stiefel-Whitney Characteristic Classes

The first characteristic class we examine is the *Stiefel-Whitney class*. First, this is an element $$w(p)$$ of the cohomology ring $$H^\bullet(B;\mathbb{Z}/2)$$ defined for any vector bundle $$p:E\rightarrow B$$, and as above, if $$w(p)=0$$ then $$E$$ becomes a trivial bundle. That is, if $$w(p)=0$$, then by [Proposition 4](#prop4), there exist $$n=\rank(E)$$ everywhere linearly independent continuous sections. Moreover, decomposing $$w(p)$$ according to the degree in the cohomology ring as

$$w(p)=w_0(p)+w_1(p)+\cdots,$$

each $$w_i(p)$$ becomes an *obstruction class* to choosing $$n-i+1$$ everywhere linearly independent sections. That is, if $$w_i(p)\neq 0$$, then $$n-i+1$$ everywhere linearly independent sections cannot exist. In particular, if $$w_n(p)\neq 0$$, then not even one everywhere linearly independent section can exist, so any section must vanish somewhere.

For convenience, when the projection map $$p$$ and base $$B$$ are clear, we sometimes use notation such as $$w(E)$$ instead of $$w(p)$$. We now present the axioms that $$w(E)$$ satisfies.

::: Definition 5
For a vector bundle $$E \rightarrow B$$ of rank $$n$$ and a vector bundle $$F\rightarrow B$$, the cohomology classes $$w_i(E)\in H^i(B;\mathbb{Z}/2)$$ satisfying the following axioms are called the *Stiefel-Whitney class*.

1. (Rank) $$w_0(E)=1$$, and if $$i>n$$ then $$w_i(E)=0$$.
2. (Naturality) For any $$f:B'\rightarrow B$$, $$w(f^\ast E)=f^\ast w(E)$$ holds.
3. (Whitney product formula) $$w(E\oplus F)=w(E)w(F)$$ holds.
4. (Normalization) For the tautological line bundle $$\gamma_1^1:E(\gamma_1^1)\rightarrow \RP^1$$ from [Example 3](#ex3), $$w_1(\gamma_1^1)\neq 0$$.
:::

Then the following results are obvious.

::: Proposition 6
For two vector bundles $$p_1:E_1\rightarrow B_1$$ and $$p_2:E_2\rightarrow B_2$$, if $$p_1$$ and $$p_2$$ are isomorphic then $$w(E_1)=w(E_2)$$. In particular, if $$p:E\rightarrow B$$ is a trivial bundle then $$w(E)=0$$.
:::

The first claim is obvious. For the second claim, it suffices to check that the trivial bundle is given by the following pullback:

![trivial_bundle](/assets/images/Math/Algebraic_Topology/Stiefel_Whitney_Classes-3.svg){:style="width:5.34em" class="invert" .align-center}

An interesting observation is that the isomorphism classes of line bundles over $$S^1$$ are only two, namely the trivial line bundle and the line bundle from [Example 3](#ex3), and indeed one can verify that among the line bundles defined over $$S^1$$, the line bundle obtained by "twisting twice" is isomorphic to the trivial line bundle. This is somewhat predictable from [Proposition 6](#prop6), because the Stiefel-Whitney class of a line bundle over $$S^1$$ must lie in $$H^1(S^1;\mathbb{Z}/2)$$, which is isomorphic to $$\mathbb{Z}/2$$.

These are pullbacks of the tautological line bundle over $$\RP^1$$. In the case of the trivial line bundle over $$S^1$$, it is the pullback via a continuous function sending every point of $$S^1$$ to a fixed point of $$\RP^1$$, and the nontrivial line bundle is the pullback of the line bundle via the quotient map $$S^1 \rightarrow \RP^1$$.

## Grassmann Varieties

More generally, any rank $$k$$ vector bundle over any space is obtained by pulling back the universal bundle $$\gamma^k_\infty:E(\gamma_\infty^k)\rightarrow \Gr(k,\mathbb{R}^\infty)$$ over the *infinite Grassmannian* $$\Gr(k,\mathbb{R}^\infty)$$. That is, given any vector bundle $$p:E \rightarrow B$$, there exists a unique bundle map from $$p$$ to $$\gamma_k^\infty$$ making the following diagram commute:

![universality](/assets/images/Math/Algebraic_Topology/Stiefel_Whitney_Classes-4.svg){:style="width:8.86em" class="invert" .align-center}

and this is isomorphic to the following pullback diagram:

![universality-2](/assets/images/Math/Algebraic_Topology/Stiefel_Whitney_Classes-5.svg){:style="width:10.63em" class="invert" .align-center}

Moreover, the Stiefel-Whitney class of the vector bundle $$E$$ is also obtained by pulling back the Stiefel-Whitney class $$w(\gamma^k_\infty)$$ of the universal bundle $$\gamma^k_\infty$$.

In the sense that $$\gamma^k_\infty$$ realizes all rank $$k$$ bundles as its pullbacks without omission, we call $$\gamma^k_\infty$$ the *universal family* of rank $$k$$ vector bundles. Soon this single bundle parametrizes all rank $$k$$ bundles, and the isomorphism class of a bundle corresponds one-to-one with the homotopy class of the classifying map $$B\rightarrow\Gr(k,\mathbb{R}^\infty)$$.

Therefore, we must examine the (infinite) Grassmannian and the universal bundle over it, and the cohomology ring $$H^\bullet(\Gr(k,\mathbb{R}^\infty), \mathbb{Z}/2)$$ of the infinite Grassmannian in which the Stiefel-Whitney class of this bundle lives. Proving all properties of Grassmannians rigorously is a complicated task, so in this section we shall content ourselves with an introduction to these properties and, where possible, simple explanations.

First, we examine the basic properties and cohomology ring of $$\Gr(k,\mathbb{R}^n)$$. By definition, $$\Gr(k,\mathbb{R}^{n})$$ is the space of all $$k$$-dimensional linear subspaces of $$\mathbb{R}^{n}$$. For example, $$\Gr(1,\mathbb{R}^{n+1})$$ is by definition the projective space $$\RP^n$$. Since each point of $$\Gr(k,\mathbb{R}^{n})$$ is a subspace of $$\mathbb{R}^{n}$$, we intuitively know how close two points (i.e., two $$k$$-dimensional subspaces of $$\mathbb{R}^{n}$$) are to each other. This is the same thing as, for example, points in $$\RP^n$$ corresponding to two lines in $$\mathbb{R}^{n+1}$$ with similar "slopes" being close, and this can be defined rigorously using $$n\times k$$ matrices; with this topology, $$\Gr(k,\mathbb{R}^{n})$$ becomes a $$k(n-k)$$-dimensional compact topological manifold.

Now let us examine the cohomology rings of these. Since we are anyway using $$\mathbb{Z}/2$$-coefficients, by [§Poincaré Duality, ⁋Theorem 11](/en/math/algebraic_topology/Poincare_duality#thm11), we may think in terms of homology cycles of $$\Gr(k,\mathbb{R}^n)$$.

To this end, fix a full flag of $$\mathbb{R}^n$$

$$F_\bullet:\qquad 0=F_0\subset F_1\subset F_2\subset\cdots\subset F_n=\mathbb{R}^n.$$

Then any $$k$$-plane $$X$$ in $$\mathbb{R}^n$$ defines

$$0=\dim (X\cap F_0)\leq\dim(X\cap F_1)\leq\cdots\leq \dim(X\cap F_n)=k,$$

and this sequence shows how $$X$$ sits inside $$\mathbb{R}^n$$. To track this, we define a *Schubert symbol* $$\sigma=(\sigma_1,\ldots, \sigma_k)$$ as a sequence satisfying the condition

$$1\leq \sigma_1<\sigma_2<\cdots<\sigma_k\leq n.$$

These $$\sigma_i$$ indicate when the space $$X\cap F_i$$ grows. That is, they carry information measuring where the dimension jumps, via

$$\dim(X\cap F_{\sigma(i)})=i, \qquad \dim(X\cap F_{\sigma(i)-1})=i-1.$$

Reversing this, we can encode this information by assigning to a suitable partition

$$\lambda:\qquad \lambda_1\geq\lambda_2\geq\cdots\geq\lambda_k,\qquad \lambda_1\leq n-k$$

the condition

$$\dim(X\cap F_{n-k+i-\lambda_i})\geq i.$$

These partitions show, when the flag

$$F_0\subset F_1\subset\cdots\subset F_n$$

is fixed, when the dimensions of $$X\cap F_i$$ jumped. For example, when $$X=F_k$$, the corresponding partition is $$(0,0,\ldots,0)$$, which means that the $$X\cap F_i$$ complete all dimension jumps without delay, in the first $$k$$ terms as $$i$$ increases. For instance, $$(0,1,0,\ldots,0)$$ means that $$X\cap F_1$$ is 1-dimensional, $$X\cap F_2$$ is also 1-dimensional, $$X\cap F_3$$ is 2-dimensional, and thereafter the dimensions jump one by one without delay.

Now based on this, consider the following subsets:

$$\Omega_\lambda^\circ(F_\bullet)=\left\{V\in\Gr(k,F_n)\mid\text{$\dim(V\cap F_{n-k+i-\lambda_i})= i$ for all $1\leq i\leq k$}\right\}.$$

These are open submanifolds in their closures

$$\Omega_\lambda(F_\bullet)=\left\{V\in\Gr(k,F_n)\mid\text{$\dim(V\cap F_{n-k+i-\lambda_i})\geq i$ for all $1\leq i\leq k$}\right\},$$

and these $$\Omega_\lambda(F_\bullet)$$ define homology classes of $$\Gr(k,\mathbb{R}^n;\mathbb{Z}/2)$$ via the inclusion

$$\Omega_\lambda(F_\bullet)\hookrightarrow \Gr(k,\mathbb{R}^n).$$

We call these *Schubert cycles*, and their Poincaré duals $$\sigma_\lambda$$ *Schubert classes*. These are cohomology classes of degree $$\lvert \lambda\rvert=\sum \lambda_i$$. At this point, each subspace $$\Omega_\lambda(F_\bullet)$$ depends on the choice of flag $$F_\bullet$$, but their images in homology, the Schubert cycles, do not depend on the choice of $$F_\bullet$$, and therefore neither do the Schubert classes. Also, $$H^\bullet(\Gr(k,\mathbb{R}^n);\mathbb{Z}/2)$$ is a polynomial algebra generated by the partitions $$\lambda$$ satisfying the preceding condition, and thus it suffices for us to examine only the cup product structure among these.

::: Example 7
For example, let us look at $$\Gr(2,\mathbb{R}^4;\mathbb{Z}/2)$$. We shall examine the square of the Schubert class $$\sigma_{(1,0)}$$ corresponding to the partition $$(1,0)$$:

$$\sigma_{(1,0)}\smile\sigma_{(1,0)}=\sigma_{(1,1)}+\sigma_{(2,0)}.$$

To use our geometric intuition, as in [§Poincaré Duality, ⁋Example 16](/en/math/algebraic_topology/Poincare_duality#ex16), let us think of this as the intersection of Schubert cycles. For this, we need to consider two subspaces in the homology class corresponding to $$\sigma_{(1,0)}$$ that are in general position, which is possible by changing the choice of flag.

For a fixed flag $$F_\bullet$$, let us explicitly state what condition the partition $$\lambda=(1,0)$$ represents:

$$\dim(X\cap F_{4-2+1-1})=\dim(X\cap F_2)\geq 1,\qquad \dim(X\cap F_{4-2+2-0})=\dim (X\cap F_4)\geq 2.$$

That is, the only effectively valid condition is $$\dim(X\cap F_2)\geq 1$$. That is, $$X$$ meets $$F_2$$ in dimension at least 1, which can be rewritten as the condition that $$X$$ contains a suitable line $$L$$ contained in $$F_2$$.

Now to compute the cup product $$\sigma_{(1,0)}\smile\sigma_{(1,0)}$$, we need to consider two flags $$F_\bullet$$ and $$F_\bullet'$$ in general position. For example,

$$F_\bullet:\quad \langle e_1\rangle\subset \langle e_1,e_2\rangle\subset \langle e_1,e_2,e_3\rangle,\qquad F_\bullet':\quad \langle e_4\rangle\subset \langle e_3,e_4\rangle\subset \langle e_2,e_3,e_4\rangle$$

are such. Now the $$V$$ we consider must meet both $$\langle e_1,e_2\rangle$$ and $$\langle e_3,e_4\rangle$$ in dimension 1. For this, consider another flag

$$G_\bullet:\quad \langle e_1+e_4\rangle\subset\langle e_1+e_4,e_2+e_3\rangle\subset \langle e_1+e_4,e_2+e_3,e_2-e_3\rangle.$$

Then there are two cases. First, one case is when the plane formed by the two lines of $$F_2$$ and $$F_2'$$ is not contained in $$G_3$$. For example, if $$V$$ meets $$F_2$$ at $$\span(e_1+e_2)$$ and $$F_2'$$ at $$\span(e_3+e_4)$$, this corresponds to this case. In this case, $$V$$ can be written exactly as $$\span(e_1+e_2,e_3+e_4)$$, which meets $$G_0$$ and $$G_1$$ in dimension 0, $$G_2$$ and $$G_3$$ in dimension 1, and only at $$G_4$$ in dimension 2. That is, this is the case corresponding to $$(1,1)$$.

The other case is when the plane formed by the two lines of $$F_2$$ and $$F_2'$$ is contained in $$G_3$$. For example, if we consider the case where $$V$$ meets $$F_2$$ at $$\span(e_2)$$ and $$F_3$$ at $$\span(e_3)$$, then $$V=\span(e_2,e_3)$$ and this is contained in $$G_3$$. This case corresponds to $$(2,0)$$.
:::

More generally, we represent these partitions by *Young diagrams*, and using this we can compute the coefficient in front of $$\sigma_\nu$$ when computing the cup product $$\sigma_\lambda\smile\sigma_\mu$$ of two Schubert classes, for $$\nu$$ satisfying $$\lvert\nu\rvert=\lvert\lambda\rvert+\lvert\mu\rvert$$.

Now we must define $$\Gr(k,\mathbb{R}^\infty)$$ and the universal bundle over it. For this, we first define the tautological bundle over $$\Gr(k,\mathbb{R}^n)$$. In the same way as [Example 3](#ex3), the following bundle attaching to each point of $$\Gr(k,\mathbb{R}^{n+k})$$ the vector space corresponding to that point

$$E(\gamma^k_n)=\left\{([V], x)\in \Gr(k,\mathbb{R}^{n+k})\mid \text{$V$ a $k$-dimensional subspace of $\mathbb{R}^{n+k}$ and $x\in V$}\right\}$$

exists, and we call this the *tautological bundle* over $$\Gr(k,\mathbb{R}^{n+k})$$.

Now for each $$n$$, the formula

$$\mathbb{R}^{k+n} \rightarrow \mathbb{R}^{k+n+1};\qquad (x_1,\ldots,x_{k+n}) \mapsto (x_1,\ldots,x_{k+n},0)$$

defines an inclusion of $$\mathbb{R}^{k+n}$$ into $$\mathbb{R}^{k+n+1}$$, and through this we can view a $$k$$-dimensional subspace of $$\mathbb{R}^{k+n}$$ as a $$k$$-dimensional subspace of $$\mathbb{R}^{k+n+1}$$. That is, the above inclusion induces an inclusion of Grassmannians $$\Gr(k,\mathbb{R}^{k+n})\rightarrow \Gr(k,\mathbb{R}^{k+n+1})$$. Now considering the directed system

$$\Gr(k,\mathbb{R}^k)\hookrightarrow \Gr(k,\mathbb{R}^{k+1})\hookrightarrow\cdots$$

we call its direct limit

$$\Gr(k,\mathbb{R}^\infty)=\varinjlim_{n\geq 0}\Gr(k,\mathbb{R}^{k+i})$$

the *infinite Grassmannian*. In the same way, the direct limit of total spaces

$$E(\gamma_\infty^k)=\varinjlim_{n\geq 0} E(\gamma^k_{k+n})$$

is defined, and this defines a rank $$k$$ vector bundle over $$\Gr(k,\mathbb{R}^\infty)$$. These naturally do not depend on the choice of inclusion $$\mathbb{R}^{k+n}\hookrightarrow \mathbb{R}^{k+n+1}$$.

Intuitively, $$\Gr(k,\mathbb{R}^\infty)$$ can be thought of as gluing together each $$\Gr(k,\mathbb{R}^{k+n})$$ and giving it a complex structure. Moreover, the tautological bundles $$E(\gamma^k_{n+k})$$ also fit together compatibly with this structure.

Carrying the Schubert classes of finite Grassmannians to infinite Grassmannians is the wrong direction. However, as explained above, the infinite Grassmannian is a space having finite Grassmannians as subcomplexes, and the Schubert cycles we constructed above behave well with respect to these inclusions. That is, pushing the Schubert cycle of $$\Gr(k,\mathbb{R}^{k+i})$$ corresponding to partition $$\lambda$$ into $$\Gr(k,\mathbb{R}^{k+i+1})$$ via $$\Gr(k,\mathbb{R}^{k+i})\rightarrow \Gr(k,\mathbb{R}^{k+i+1})$$, or intersecting the Schubert cycle corresponding to partition $$\lambda$$ in $$\Gr(k,\mathbb{R}^{k+i+1})$$ directly with $$\Gr(k,\mathbb{R}^n)\subset \Gr(k,\mathbb{R}^{k+i+1})$$, gives the same result.

Now consider the $$k$$ partitions

$$\lambda_1=(1,0,\cdots, 0),\quad \lambda_2=(2,0,\cdots,0),\qquad \lambda_k=(k,0,\cdots,0).$$

Then by the above argument, these become homology classes of $$\Gr(k,\mathbb{R}^\infty)$$, and the functions

$$w_i: H_\bullet(\Gr(k,\mathbb{R}^\infty);\mathbb{Z}/2)\rightarrow \mathbb{Z}/2; \qquad \text{$w_i(\Omega_{\lambda_i}(F_\bullet))=1$ and is $0$ otherwise}$$

lie in the $$i$$th cohomology class $$H^i(\Gr(k,\mathbb{R}^\infty);\mathbb{Z}/2)$$, and thus we know that

$$w_1\in H^1(\Gr(k,\mathbb{R}^\infty);\mathbb{Z}/2),\cdots, w_k\in H^k(\Gr(k,\mathbb{R}^\infty);\mathbb{Z}/2).$$

Then $$H^\bullet(\Gr(k,\mathbb{R}^\infty);\mathbb{Z}/2)$$ is generated as a *polynomial algebra* by these $$w_i$$. For example, any partition $$(a_1,\cdots,a_n)$$ corresponds to the monomial

$$w_1^{a_1}w_2^{a_2}\cdots w_k^{a_k}$$

and this becomes one of the (infinitely many) generators as a *$$\mathbb{Z}/2$$-module* of $$H^\bullet(\Gr(k,\mathbb{R}^\infty);\mathbb{Z}/2)$$, which is computed by the Littlewood-Richardson rule mentioned above. Now these $$w_i$$ satisfy all the axioms that the Stiefel-Whitney class satisfies, and their existence is proved from the fact that they are preserved under pullback.
