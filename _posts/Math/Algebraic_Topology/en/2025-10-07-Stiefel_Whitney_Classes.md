---
title: "Stiefel-Whitney Characteristic Classes"
description: "This post defines fiber bundles and vector bundles, then introduces Stiefel-Whitney characteristic classes as the first characteristic classes via Cech cohomology, along with the infinite Grassmannian as their classifying space."
excerpt: "Vector bundles, Stiefel-Whitney classes, and the infinite Grassmannian"

categories: [Math / Algebraic Topology]
permalink: /en/math/algebraic_topology/stiefel_whitney_classes
sidebar: 
    nav: "algebraic_topology-en"

date: 2025-10-07
weight: 13
translated_at: 2026-08-15T18:45:04+00:00
translation_source: kimi-cli
---
In the previous post, the map $p:\Spe(\or_M^A)\rightarrow M$ played an important role as a covering space, and these had the following properties.

1. For any $x\in M$, we have $p^{-1}(x)\cong \{x\}\times A^\times$.
2. Moreover, for any $x\in M$, there exists a suitable open set $U$ such that $p^{-1}(U)\cong U\times A^\times$.

Now we generalize this further and examine the case where $p^{-1}(x)$ carries additional structure (rather than being merely a discrete set). The most general definition is as follows.

::: Definition 1
For a continuous surjection $p:E \rightarrow B$ between topological spaces and a topological space $F$, we say that $p$ is a *fiber bundle* with fiber space $F$ if for each $x\in B$, there exists an open set $U$ containing $x$ and a homeomorphism $\phi:U\times F\rightarrow p^{-1}(U)$ making the following diagram

{% diagram Math/Algebraic_Topology/Stiefel_Whitney_Classes-1.svg width="10.09em" alt="fiber_bundle" %}

commute.
:::

Here, $B$ is called the *base space*, $E$ the *total space*, and $F$ the *fiber* of this bundle; if we can take $U=B$, then this fiber bundle is called a *trivial bundle*. For instance, in the previous example, $M$ is the base space, $\Spe(\or_M^A)$ is the total space, and $A^\times$ equipped with the discrete topology is the fiber. More generally, any covering space can be regarded as a fiber bundle whose fiber has the discrete topology.

The two cases of particular interest to us are when the fiber $F$ is a vector space, and when it is a topological group. For convenience, we henceforth assume that $B$ is connected.

## Vector Bundles

First, we consider the case where $F$ is a vector space. When the fiber $F$ is a topological group, $F$ is already equipped with a topology, so the topology on the product space $U\times F$ in [Definition 1](#def1) is clear; however, when $F$ is a vector space, the situation is somewhat ambiguous. In the most general setting, one could use the notion of a topological vector space $V$ over a topological ring $\mathbb{K}$, but for convenience we shall for now only consider the case where the base field of $F$ is $\mathbb{R}$ and $F$ is equipped with the metric topology arising from the canonical inner product.

::: Definition 2
A fiber bundle $p:E \rightarrow B$ is called a *vector bundle* if the fiber space $F$ is an $\mathbb{R}$-vector space equipped with a topology as above, and moreover for each $x\in B$ there exists an open set $U$ containing $x$ and a homeomorphism $\phi:U\times  F\rightarrow p^{-1}(U)$ as in [Definition 1](#def1) such that the function

$$\phi(x,-):F \rightarrow p^{-1}(x);\qquad v\mapsto \phi(x,v)$$

is an isomorphism of vector spaces.
:::

Through this, each fiber $p^{-1}(x)$ inherits a vector space structure from $F$. In general, given two vector bundles $p_1:E_1 \rightarrow B_1$ and $p_2:E_2\rightarrow B_2$, a *morphism* between them means a commutative diagram of continuous functions

{% diagram Math/Algebraic_Topology/Stiefel_Whitney_Classes-2.svg width="7.15em" alt="morphism_of_bundles" %}

where, restricting $g$ to $p_1^{-1}(x)\rightarrow p_2^{-1}(f(x))$ for each $x\in B_1$, this function must be a linear map between vector spaces. How to define an isomorphism between vector bundles is then obvious.

Meanwhile, in [Definition 2](#def2) above, we only considered the case where $F$ is an $\mathbb{R}$-vector space, and we defined a topology on it using the inner product structure on $\mathbb{R}^n$ and the topology on $\mathbb{R}$. But strictly speaking, the only information needed here is the topology on the vector space $F$, and when we view $F$ as an inner product space, this is called a *Euclidean bundle*. In any case, since we will mostly consider $\mathbb{R}$-vector spaces, we shall gloss over this distinction.

::: Example 3
As a non-trivial example, the Möbius strip considered as a line bundle over $S^1$ is a classic instance. On the other hand, in [§Poincaré Duality, ⁋Example 5](/en/math/algebraic_topology/Poincare_duality#ex5) we also considered a non-trivial cover of $S^1$, which can be generalized geometrically as follows.

For an $(n+1)$-dimensional vector space $\mathbb{R}^{n+1}$, we call the space of lines through the origin the *projective $n$-space* and denote it by $\RP^n$. Among the points on a line through the origin, the two points at distance $1$ from the origin specify the same line, so we can think of this as the quotient space obtained from the unit $n$-sphere $S^n$ by identifying antipodal points.

Now let us take this space $\RP^n$ as the base space $B$, and define a vector bundle $E(\gamma_n^1)$ over it as follows. As a set,

$$E(\gamma_n^1)=\{(x,v)\in \RP^n\times \mathbb{R}^{n+1}\mid v\in \span(x)\}$$

and the projection $\gamma_n^1:E(\gamma_n^1)\rightarrow \RP^n$ is projection onto the first coordinate. That is, $\gamma_n^1$ attaches to each point $x\in \RP^n$ exactly the line in $\mathbb{R}^{n+1}$ that $x$ originally belonged to.

When $n\geq 1$, this is not a trivial bundle. If it were trivial, there would exist a non-vanishing continuous section $\RP^n\rightarrow E(\gamma_n^1)$. For instance, the function sending every point of $B$ to $1$ in the fiber would be such a section. But given any section $s:\RP^n \rightarrow E(\gamma_n^1)$, consider the following composition using the quotient map $q:S^n \rightarrow \RP^n$:

$$S^n \overset{q}{\longrightarrow} \RP^n \overset{s}{\longrightarrow} E\overset{\pr_2}{\longrightarrow} \mathbb{R}^{n+1}$$

This function sends $\mathbf{x}\in S^n\subseteq\mathbb{R}^{n+1}$ to a scalar multiple of $\mathbf{x}$. Denoting this scalar by $t(\mathbf{x})$, then $t$ is a continuous function from $S^n$ to $\mathbb{R}$, and because of the quotient map $q$ it satisfies

$$t(-\mathbf{x})=-t(\mathbf{x}).$$

Now since $S^n$ is connected, by the intermediate value theorem there exists $\mathbf{x}_0\in S^n$ with $t(\mathbf{x}_0)=0$.
:::

More generally, the following holds.

::: Proposition 4
For a vector bundle $E$ of rank $n$ over a topological space $B$, $E$ is a trivial bundle if and only if there exist $n$ everywhere linearly independent sections $s_1,\ldots, s_n$.
:::
::: Proof
If $E$ is trivial, pick an isomorphism $\psi:B\times\mathbb{R}^n\rightarrow E$ and set $s_i(x)=\psi(x,e_i)$; then since $\psi(x,-)$ is an isomorphism for each $x$, these become everywhere linearly independent sections.

Conversely, suppose such sections are given and define

$$\varphi:B\times\mathbb{R}^n\rightarrow E;\qquad (x,a)\mapsto \sum_i a_is_i(x).$$

Then $\varphi$ is a continuous function covering $\id_B$ and is linear on each fiber; since $s_1(x),\ldots,s_n(x)$ are linearly independent, they form a basis of $p^{-1}(x)$ and so $\varphi(x,-)$ is an isomorphism. It remains to show the continuity of $\varphi^{-1}$; picking a local trivialization $\phi:U\times\mathbb{R}^n \rightarrow p^{-1}(U)$ from [Definition 2](#def2) and looking at $\phi^{-1}\circ\varphi$, this has the form $(x,a)\mapsto (x,A(x)a)$ where $A:U\rightarrow \GL(n;\mathbb{R})$ is continuous. Since taking the inverse of a matrix is continuous, $x\mapsto A(x)^{-1}$ is also continuous, and therefore $\varphi^{-1}$ is continuous on each $U$.
:::

Meanwhile, given any vector bundle $p:E \rightarrow B$ and any continuous map $f:B'\rightarrow B$, we can define a new vector bundle $f^\ast E \rightarrow B'$ by the formula

$$f^\ast E=\{(x,v)\in B'\times E\mid f(x)=p(v)\}\subseteq B'\times E.$$

We call this the *pullback bundle*, and it is not difficult to see that for any vector bundle $E' \rightarrow B'$, if a bundle map $E'\rightarrow E$ covering $f$ is given, then this factors uniquely through $E'\rightarrow f^\ast E \rightarrow E$.

Meanwhile, given any two vector bundles $p_1:E_1\rightarrow B_1$, $p_2:E_2\rightarrow B_2$, their product

$$p_1\times p_2: E_1\times E_2 \rightarrow B_1\times B_2$$

is also a vector bundle over $B_1\times B_2$. Now if $B_1=B_2=B$, then as usual using the diagonal map

$$\Delta: B\rightarrow B\times B$$

the pullback bundle $\Delta^\ast(p_1\times p_2)$ becomes a bundle over $B$. We call this the *Whitney sum* of the two vector bundles $E_1\rightarrow B$, $E_2\rightarrow B$ and denote it by $p_1\oplus p_2:E_1\oplus E_2\rightarrow B$. As the notation suggests, fiberwise this corresponds to the direct sum of the fibers of the two vector bundles $E_1,E_2$.

Although we have not given detailed proofs, in a similar manner we can lift operations defined on each fiber (that is, on vector spaces) to vector bundles. For instance, given two vector bundles $E_1\rightarrow B$, $E_2 \rightarrow B$, we can form their tensor product bundle $E_1\otimes E_2 \rightarrow B$, and it is also possible to use operations such as $\Hom$ or $\bigwedge$.

## Čech Cohomology

At this point we establish another cohomology theory. Like the sheaf cohomology in [§Poincaré Duality, ⁋Definition 15](/en/math/algebraic_topology/Poincare_duality#def15), this is a cohomology for sheaves defined on a topological space, and it plays an important role in our story because via the étale space construction, a sheaf whose stalks are vector spaces can be identified with a vector bundle.

Sheaf cohomology showed that cohomology encodes the obstruction to the existence of global sections of a sheaf. The Čech cohomology we now examine gives a similar result, but differs in that it answers this question by examining the process of patching local sections together to form a global section. In any case, for nice cases including manifolds, Čech cohomology gives the same result as sheaf cohomology, and thus the Čech cohomology of a constant sheaf recovers the cohomology we already knew.

Consider a topological space $X$, a sheaf $\mathcal{F}$ defined on it, and an open cover $\mathcal{U}=\{U_i\}_{i\in I}$ of $X$. For each $p\geq 0$, the group of *Čech $p$-cochains* is defined by the formula

$$\check{C}^p(\mathcal{U},\mathcal{F})=\prod_{i_0,\ldots,i_p}\mathcal{F}(U_{i_0}\cap \cdots\cap U_{i_p}).$$

That is, this is the collection of sections defined over all $(p+1)$-fold intersections. The differential

$$\check{C}^p(\mathcal{U},\mathcal{F})\rightarrow \check{C}^{p+1}(\mathcal{U}, \mathcal{F})$$

is given by the formula

$$(\delta c)_{i_0,\ldots, i_{p+1}}=\sum_{k=0}^{p+1} (-1)^k c_{i_0,\ldots,\hat{i}_k,\ldots,i_{p+1}}\vert_{U_{i_0}\cap\cdots\cap U_{i_{p+1}}}.$$

Then *Čech cohomology* is given by the formula

$$\check{H}^p(\mathcal{U}, \mathcal{F})=\frac{\ker(\check{C}^p\rightarrow \check{C}^{p+1})}{\im(\check{C}^{p-1}\rightarrow \check{C}^{p})}.$$

If $\mathcal{U}$ is a sufficiently good cover (for instance, if every finite intersection is contractible, or is acyclic for $\mathcal{F}$), then we obtain a canonical isomorphism

$$H^p(X,\mathcal{F})\cong \check{H}^p(\mathcal{U},\mathcal{F}).$$

Now any rank $n$ vector bundle is determined by how its fiber is glued over an open cover. That is, it is determined by functions

$$g_{ij}:U_{ij}=U_i\cap U_j \rightarrow \GL(n;\mathbb{R}).$$

These must satisfy the condition

$$g_{ij}\cdot g_{jk}\cdot g_{ki}=\id,$$

and if this condition were absent, on a triple intersection $U_i\cap U_j\cap U_k$, carrying the local trivialization from $U_i$ to $U_j$ via $g_{ij}$, then to $U_k$ via $g_{jk}$, then back to $U_i$ via $g_{ki}$, the trivialization would differ, whereas in reality it does not. Then these transition functions $g_{ij}$ form a Čech 1-cocycle by the above condition. If we change the local trivialization over each $U_i$ by a function $h_i:U_i\rightarrow \GL(n;\mathbb{R})$, then $g_{ij}$ changes to $h_ig_{ij}h_j^{-1}$, so cocycles giving the same vector bundle must be identified under this relation. That is, there is a one-to-one correspondence between isomorphism classes of rank $n$ vector bundles trivializable over an open cover $\mathcal{U}$ and $\check{H}^1(\mathcal{U}, \GL(n;\mathbb{R}))$. However, since $\GL(n;\mathbb{R})$ is a non-abelian group, the $\check{H}^1$ here is not the cohomology group defined by the differential above, but rather a pointed set defined separately by the cocycle condition $g_{ij}g_{jk}g_{ki}=\id$ and the equivalence relation just mentioned.

Earlier, in [§Poincaré Duality, ⁋Proposition 7](/en/math/algebraic_topology/Poincare_duality#prop7), we saw that the $A$-orientability of a manifold $M$ is defined by the group homomorphism

$$\pi_1(M,x)\rightarrow A^\times.$$

On the other hand, since $A$ is a commutative ring, this group homomorphism factors through the abelian group homomorphism

$$H_1(M)\rightarrow A^\times$$

and by [§Cohomology, ⁋Proposition 3](/en/math/algebraic_topology/cohomology#prop3) this is an element of $H^1(M;A^\times)$. If this element is $0$, this is equivalent to the monodromy action being trivial, which in turn means that $\Spe(\or_M^A)$ is a trivial covering space and so $M$ becomes an $A$-orientable manifold. On the other hand, for any commutative ring $A$, since the initial object of $\cRing$ is $\mathbb{Z}$, for any manifold $M$ once a $\mathbb{Z}$-orientation $H_1(M)\rightarrow \mathbb{Z}^\times$ is determined, we can compose it with $\mathbb{Z}^\times\rightarrow A^\times$ to determine an $A$-orientation $H_1(M)\rightarrow A^\times$; thus the essential information about whether $\Spe(\or_M^A)$ is a trivial cover is contained in $H^1(M;\mathbb{Z}/2)$, and thinking of $\mathbb{Z}/2$ as $\GL(1;\mathbb{Z})$, this is an example of how first cohomology encodes information about covering spaces.

In this manner, information about a vector bundle $E\rightarrow B$ of rank $k$ can be regarded as being contained in $\check{H}^1(B; \underline{\GL(k;\mathbb{R})})$. However, since the coefficients in the cohomology of $B$ that we use are $\mathbb{Z}$, we do not have all the data contained there. Instead, our goal is to find weaker substitutes for this, namely invariants in the cohomology ring $H^\bullet(B)$.

## Stiefel-Whitney Classes

The first characteristic class we examine is the *Stiefel-Whitney class*. First, for any given vector bundle $p:E\rightarrow B$, this is an element $w(p)$ of the cohomology ring $H^\bullet(B;\mathbb{Z}/2)$, and as above, if $E$ is a trivial bundle then $w(p)=1$. Indeed, a trivial bundle has $n=\rank(E)$ everywhere linearly independent continuous sections by [Proposition 4](#prop4), and the extent to which $w(p)$ deviates from $1$ measures the obstruction to choosing such sections. To see this, decomposing $w(p)$ according to degree in the cohomology ring as

$$w(p)=w_0(p)+w_1(p)+\cdots,$$

each $w_i(p)$ becomes an *obstruction class* to choosing $n-i+1$ everywhere linearly independent sections. That is, if $w_i(p)\neq 0$, then $n-i+1$ everywhere linearly independent sections cannot exist. In particular, if $w_n(p)\neq 0$, then not even a single everywhere linearly independent section can exist, so any section must vanish somewhere.

For convenience, when the projection map $p$ and base $B$ are clear, we sometimes use notation such as $w(E)$ instead of $w(p)$. We now present the axioms that $w(E)$ satisfies.

::: Definition 5
For a vector bundle $E \rightarrow B$ of rank $n$ and a vector bundle $F\rightarrow B$, the cohomology classes $w_i(E)\in H^i(B;\mathbb{Z}/2)$ satisfying the following axioms are called the *Stiefel-Whitney classes* of $E$.

1. (Rank) $w_0(E)=1$, and if $i>n$ then $w_i(E)=0$.
2. (Naturality) For any $f:B'\rightarrow B$, we have $w(f^\ast E)=f^\ast w(E)$.
3. (Whitney product formula) $w(E\oplus F)=w(E)w(F)$ holds.
4. (Normalization) For the tautological line bundle $\gamma_1^1:E(\gamma_1^1)\rightarrow \RP^1$ of [Example 3](#ex3), we have $w_1(\gamma_1^1)\neq 0$.
:::

From this we obtain the following results.

::: Proposition 6
For two vector bundles $p_1:E_1\rightarrow B$, $p_2:E_2\rightarrow B$ defined over a topological space $B$, if $p_1,p_2$ are isomorphic then $w(E_1)=w(E_2)$. In particular, if $p:E\rightarrow B$ is a trivial bundle then $w(E)=1$.
:::

For the first claim, an isomorphism between $E_1$ and $E_2$ gives $E_1\cong \id_B^\ast E_2$, so by naturality in [Definition 5](#def5) we have $w(E_1)=\id_B^\ast w(E_2)=w(E_2)$. For the second claim, it suffices to verify that a trivial bundle is given by the following pullback

{% diagram Math/Algebraic_Topology/Stiefel_Whitney_Classes-3.svg width="5.34em" alt="trivial_bundle" %}

An interesting observation is that the isomorphism classes of line bundles over $S^1$ are only two, namely the trivial line bundle and the line bundle of [Example 3](#ex3); indeed, one can check that a line bundle over $S^1$ obtained by "twisting twice" is isomorphic to the trivial line bundle. This is to some extent predictable from [Proposition 6](#prop6), because the Stiefel-Whitney class of a line bundle over $S^1$ must lie in $H^1(S^1;\mathbb{Z}/2)$, which is isomorphic to $\mathbb{Z}/2$.

Another observation is that these are pullbacks of the tautological line bundle over $\RP^1$. The trivial line bundle over $S^1$ is the pullback via a continuous map sending every point of $S^1$ to a fixed point of $\RP^1$, while the nontrivial line bundle is the pullback of the line bundle via a homeomorphism $S^1 \rightarrow \RP^1$.

## Grassmannians

More generally, any rank $k$ vector bundle over a paracompact space is obtained by pulling back the universal bundle $\gamma^k_\infty:E(\gamma_\infty^k)\rightarrow \Gr(k,\mathbb{R}^\infty)$ from the *infinite Grassmannian* $\Gr(k,\mathbb{R}^\infty)$. That is, given any vector bundle $p:E \rightarrow B$ over a paracompact space $B$, there exists a bundle map from $p$ to $\gamma^k_\infty$, unique up to homotopy, making the following diagram

{% diagram Math/Algebraic_Topology/Stiefel_Whitney_Classes-4.svg width="8.86em" alt="universality" %}

commute, and this is isomorphic to the following pullback diagram

{% diagram Math/Algebraic_Topology/Stiefel_Whitney_Classes-5.svg width="10.63em" alt="universality-2" %}

Moreover, the Stiefel-Whitney class of a vector bundle $E$ is also obtained by pulling back the Stiefel-Whitney class $w(\gamma^k_\infty)$ of the universal bundle $\gamma^k_\infty$.

In the sense that this single bundle realizes all rank $k$ bundles as its pullbacks without exception, we call $\gamma^k_\infty$ the *universal family* of rank $k$ vector bundles. Soon this one bundle parametrizes all rank $k$ bundles, and the isomorphism class of a bundle corresponds one-to-one with the homotopy class of the classifying map $B\rightarrow\Gr(k,\mathbb{R}^\infty)$.

Therefore, we must examine the (infinite) Grassmannian and the universal bundle over it, as well as the cohomology ring $H^\bullet(\Gr(k,\mathbb{R}^\infty), \mathbb{Z}/2)$ of the infinite Grassmannian in which the Stiefel-Whitney class of this bundle lives. Since rigorously proving all properties of Grassmannians is a complex task, in this section we shall content ourselves with an introduction to these properties and, where possible, simple explanations.

First, we examine the basic properties and cohomology ring of $\Gr(k,\mathbb{R}^n)$. By definition, $\Gr(k,\mathbb{R}^{n})$ is the space of all $k$-dimensional linear subspaces of $\mathbb{R}^{n}$. For example, $\Gr(1,\mathbb{R}^{n+1})$ is by definition the projective space $\RP^n$. Since each point of $\Gr(k,\mathbb{R}^{n})$ is a subspace of $\mathbb{R}^{n}$, we intuitively know how close two points (that is, two $k$-dimensional subspaces of $\mathbb{R}^{n}$) are to each other. This is the same phenomenon as, for example, points in $\RP^n$ corresponding to lines in $\mathbb{R}^{n+1}$ with similar "slopes" being close to each other; this can be defined rigorously using $n\times k$ matrices, and with this topology $\Gr(k,\mathbb{R}^{n})$ becomes a $k(n-k)$-dimensional compact topological manifold.

Now let us examine the cohomology rings of these spaces. Since we are in any case using $\mathbb{Z}/2$-coefficients, by [§Poincaré Duality, ⁋Theorem 11](/en/math/algebraic_topology/Poincare_duality#thm11), we may instead think in terms of homology cycles of $\Gr(k,\mathbb{R}^n)$.

For this, fix a full flag of $\mathbb{R}^n$

$$F_\bullet:\qquad 0=F_0\subseteq F_1\subseteq F_2\subseteq\cdots\subseteq F_n=\mathbb{R}^n.$$

Then for any $k$-plane $X$ in $\mathbb{R}^n$ we have

$$0=\dim (X\cap F_0)\leq\dim(X\cap F_1)\leq\cdots\leq \dim(X\cap F_n)=k,$$

and this sequence shows how $X$ sits inside $\mathbb{R}^n$. To track this, we define a *Schubert symbol* $\sigma=(\sigma_1,\ldots, \sigma_k)$ as a sequence satisfying the condition

$$1\leq \sigma_1<\sigma_2<\cdots<\sigma_k\leq n.$$

These $\sigma_i$ indicate when the space $X\cap F_i$ grows. That is, they can encode the information measuring where the dimension jumps via

$$\dim(X\cap F_{\sigma(i)})=i, \qquad \dim(X\cap F_{\sigma(i)-1})=i-1.$$

Reversing this, we can capture this information by assigning to a suitable partition

$$\lambda:\qquad \lambda_1\geq\lambda_2\geq\cdots\geq\lambda_k,\qquad \lambda_1\leq n-k$$

the condition

$$\dim(X\cap F_{n-k+i-\lambda_i})\geq i.$$

These partitions show, once the flag

$$F_0\subseteq F_1\subseteq\cdots\subseteq F_n$$

is fixed, how early the dimension of $X\cap F_i$ jumped. That is, $\lambda_i=n-k+i-\sigma_i$ measures how far the $i$-th jump was moved forward from the latest possible position $\sigma_i=n-k+i$, and because of this $\lambda_i-\lambda_{i+1}=\sigma_{i+1}-\sigma_i-1\geq 0$, so $\lambda$ automatically becomes a decreasing sequence. For example, $\lambda=(0,0,\ldots,0)$ is the generic case where all jumps occur as late as possible, and since the condition $\dim(X\cap F_{n-k+i})\geq i$ is satisfied by any $k$-plane, $\Omega_{(0,\ldots,0)}$ becomes the entire Grassmannian. Conversely, when $X=F_k$, since $\dim(F_k\cap F_j)=\min(k,j)$, we have $\sigma_i=i$, that is $\lambda_i=n-k$, and the corresponding partition is the full rectangle $(n-k,\ldots,n-k)$, which is the smallest case corresponding to a single point of the Grassmannian.

Now based on this, consider the following subsets

$$\Omega_\lambda^\circ(F_\bullet)=\left\{V\in\Gr(k,F_n)\mid\text{$\dim(V\cap F_{n-k+i-\lambda_i})= i$ and $\dim(V\cap F_{n-k+i-\lambda_i-1})= i-1$ for all $1\leq i\leq k$}\right\}$$

These are each dense open subsets inside their closures

$$\Omega_\lambda(F_\bullet)=\left\{V\in\Gr(k,F_n)\mid\text{$\dim(V\cap F_{n-k+i-\lambda_i})\geq i$ for all $1\leq i\leq k$}\right\}$$

and these $\Omega_\lambda(F_\bullet)$ define homology classes in $H_\bullet(\Gr(k,\mathbb{R}^n);\mathbb{Z}/2)$ by pushing forward their mod $2$ fundamental class along the inclusion 

$$\Omega_\lambda(F_\bullet)\hookrightarrow \Gr(k,\mathbb{R}^n).$$

We call the subspace $\Omega_\lambda(F_\bullet)$ a *Schubert cycle*, and the Poincaré dual $\sigma_\lambda$ of the homology class thus obtained a *Schubert class*. These are cohomology classes of degree $\lvert \lambda\rvert=\sum \lambda_i$. The Schubert cycle itself depends on the choice of flag $F_\bullet$, but the Schubert class it defines does not depend on the choice of $F_\bullet$. Also, $H^\bullet(\Gr(k,\mathbb{R}^n);\mathbb{Z}/2)$ has the Schubert classes $\sigma_\lambda$ for partitions $\lambda$ satisfying the above conditions as a basis as a $\mathbb{Z}/2$-module, and therefore it suffices for us to examine only the cup product structure among these.

::: Example 7
For example, let us look at $H^\bullet(\Gr(2,\mathbb{R}^4);\mathbb{Z}/2)$. We shall examine the square of the Schubert class $\sigma_{(1,0)}$ corresponding to the partition $(1,0)$:

$$\sigma_{(1,0)}\smile\sigma_{(1,0)}=\sigma_{(1,1)}+\sigma_{(2,0)}.$$

To utilize our geometric intuition, let us think of this as an intersection of Schubert cycles, just as in [§Poincaré Duality, ⁋Example 16](/en/math/algebraic_topology/Poincare_duality#ex16). For this, we need to consider two subspaces in general position corresponding to the homology class of $\sigma_{(1,0)}$, which is possible by changing the choice of flag.

For a fixed flag $F_\bullet$, let us explicitly write out what condition the partition $\lambda=(1,0)$ represents:

$$\dim(X\cap F_{4-2+1-1})=\dim(X\cap F_2)\geq 1,\qquad \dim(X\cap F_{4-2+2-0})=\dim (X\cap F_4)\geq 2.$$

That is, the only effectively valid condition is $\dim(X\cap F_2)\geq 1$. This means that $X$ meets $F_2$ in dimension at least $1$, which can be rephrased as the condition that $X$ contains a suitable line $L$ contained in $F_2$.

Now to compute the cup product $\sigma_{(1,0)}\smile\sigma_{(1,0)}$, we need to consider two flags $F_\bullet$ and $F_\bullet'$ in general position. For instance,

$$F_\bullet:\quad \langle e_1\rangle\subseteq \langle e_1,e_2\rangle\subseteq \langle e_1,e_2,e_3\rangle,\qquad F_\bullet':\quad \langle e_4\rangle\subseteq \langle e_3,e_4\rangle\subseteq \langle e_2,e_3,e_4\rangle$$

are such flags. Now the $V$ we consider must meet both $\langle e_1,e_2\rangle$ and $\langle e_3,e_4\rangle$ in dimension $1$. For this, consider another flag

$$G_\bullet:\quad \langle e_1+e_4\rangle\subseteq\langle e_1+e_4,e_2+e_3\rangle\subseteq \langle e_1+e_4,e_2+e_3,e_2-e_3\rangle.$$

First, since $F_2\cap F_2'=0$, a $2$-dimensional subspace satisfying both conditions $\dim(V\cap F_2)\geq 1$ and $\dim(V\cap F_2')\geq 1$ is exactly represented as the sum of a line $L$ in $F_2$ and a line $L'$ in $F_2'$. That is, the intersection of the two Schubert cycles is

$$S=\left\{L\oplus L'\mid L\subseteq F_2,\ L'\subseteq F_2'\right\}\cong \mathbb{P}^1\times\mathbb{P}^1$$

and the coefficient $1$ attached to each of the two terms on the right-hand side is because $S$ meets each of the two Schubert cycles determined by $G_\bullet$ in exactly one point.

Indeed, the condition for $\Omega_{(1,1)}(G)$ is $V\subseteq G_3=\left\{x\mid x_1=x_4\right\}$, so for $L\oplus L'$ to belong here, $x_1=x_4=0$ is forced from each of $L$ and $L'$, leaving only $L=\span(e_2)$ and $L'=\span(e_3)$. On the other hand, the condition for $\Omega_{(2,0)}(G)$ is $G_1=\langle e_1+e_4\rangle\subseteq V$; decomposing $e_1+e_4$ along $F_2\oplus F_2'$ gives $e_1$ and $e_4$, so this time $L=\span(e_1)$ and $L'=\span(e_4)$ are forced. Thus the two intersection points are $\span(e_2,e_3)$ and $\span(e_1,e_4)$ respectively, one each, and this is why $\sigma_{(1,1)}$ and $\sigma_{(2,0)}$ appear with coefficient $1$.
:::

More generally, we represent these partitions by *Young diagrams*, and using this we can compute, when calculating the cup product $\sigma_\lambda\smile\sigma_\mu$ of two Schubert classes, the coefficient appearing in front of $\sigma_\nu$ for $\nu$ satisfying $\lvert\nu\rvert=\lvert\lambda\rvert+\lvert\mu\rvert$. The rule for reading off this coefficient from the Young diagram is called the *Littlewood-Richardson rule*.

Now we must define $\Gr(k,\mathbb{R}^\infty)$ and the universal bundle over it. For this, we first define the tautological bundle over $\Gr(k,\mathbb{R}^n)$. In the same manner as [Example 3](#ex3), the following bundle attaching to each point of $\Gr(k,\mathbb{R}^{n+k})$ the vector space corresponding to that point

$$E(\gamma^k_n)=\left\{([V], x)\in \Gr(k,\mathbb{R}^{n+k})\times \mathbb{R}^{n+k}\mid \text{$V$ a $k$-dimensional subspace of $\mathbb{R}^{n+k}$ and $x\in V$}\right\}$$

exists, and we call this the *tautological bundle* over $\Gr(k,\mathbb{R}^{n+k})$.

Now for each $n$, the formula

$$\mathbb{R}^{k+n} \rightarrow \mathbb{R}^{k+n+1};\qquad (x_1,\ldots,x_{k+n}) \mapsto (x_1,\ldots,x_{k+n},0)$$

defines an inclusion of $\mathbb{R}^{k+n}$ into $\mathbb{R}^{k+n+1}$, and through this we can view a $k$-dimensional subspace of $\mathbb{R}^{k+n}$ as a $k$-dimensional subspace of $\mathbb{R}^{k+n+1}$. That is, the above inclusion induces an inclusion $\Gr(k,\mathbb{R}^{k+n})\rightarrow \Gr(k,\mathbb{R}^{k+n+1})$ between Grassmannians. Now considering the directed system

$$\Gr(k,\mathbb{R}^k)\hookrightarrow \Gr(k,\mathbb{R}^{k+1})\hookrightarrow\cdots$$

we call their direct limit

$$\Gr(k,\mathbb{R}^\infty)=\varinjlim_{n\geq 0}\Gr(k,\mathbb{R}^{k+n})$$

the *infinite Grassmannian*. In the same manner, the direct limit of total spaces

$$E(\gamma_\infty^k)=\varinjlim_{n\geq 0} E(\gamma^k_{k+n})$$

is defined, and this defines a rank $k$ vector bundle over $\Gr(k,\mathbb{R}^\infty)$. These of course do not depend on the choice of the inclusion $\mathbb{R}^{k+n}\hookrightarrow \mathbb{R}^{k+n+1}$.

Intuitively, $\Gr(k,\mathbb{R}^\infty)$ can be thought of as giving a complex structure by gluing together the various $\Gr(k,\mathbb{R}^{k+n})$. Moreover, the tautological bundles $E(\gamma^k_{n+k})$ also become attached compatibly with this structure.

Carrying over the Schubert cycles of finite Grassmannians to the infinite Grassmannian is not the right direction. In our convention, $\Omega_\lambda(F_\bullet)$ has codimension $\lvert\lambda\rvert$, so its dimension grows with $n$. However, as explained above, the infinite Grassmannian is a space having finite Grassmannians as subcomplexes, and the Schubert classes constructed above behave well under these inclusions. That is, if we attach a new direction at the bottom of the flag, letting $F'_1$ be that direction and $F'_{j+1}=F'_1\oplus F_j$, then the condition defining $\Omega_\lambda(F'_\bullet)$ read for an element of $\Gr(k,\mathbb{R}^{k+i})$ becomes the same as the condition defining $\Omega_\lambda(F_\bullet)$, so for the inclusion $\iota:\Gr(k,\mathbb{R}^{k+i})\hookrightarrow \Gr(k,\mathbb{R}^{k+i+1})$ we have $\iota^\ast\sigma_\lambda=\sigma_\lambda$. In this way, for each $\lambda$ a cohomology class $\sigma_\lambda$ of $\Gr(k,\mathbb{R}^\infty)$ is determined.

Now consider the $k$ partitions

$$\lambda_1=(1,0,\cdots, 0),\quad \lambda_2=(1,1,0,\cdots,0),\qquad \lambda_k=(1,\cdots,1).$$

Then we obtain the corresponding Schubert classes

$$w_1\in H^1(\Gr(k,\mathbb{R}^\infty);\mathbb{Z}/2),\cdots, w_k\in H^k(\Gr(k,\mathbb{R}^\infty);\mathbb{Z}/2).$$

The condition imposed by $\lambda_i$ in $\Gr(k,\mathbb{R}^n)$ collapses to the single condition $\dim(V\cap F_{n-k+i-1})\geq i$, which is where $k-i+1$ sections of the tautological bundle lose independence; thus we see that what we earlier read as $w_i$ being the obstruction class to choosing such sections is exactly this. On the other hand, the Schubert class for the single-row partition $(i,0,\cdots,0)$ is the degree $i$ component of the formal inverse $\bar w$ of $w(\gamma^k_\infty)$, so for $i\geq 2$ it differs from $w_i$, as in $\bar w_2=w_1^2+w_2$.

Then $H^\bullet(\Gr(k,\mathbb{R}^\infty);\mathbb{Z}/2)$ is generated by these $w_i$ as a *polynomial algebra*. For instance, the monomials

$$w_1^{a_1}w_2^{a_2}\cdots w_k^{a_k}$$

form a (infinite) basis of this ring as a *$\mathbb{Z}/2$-module*, and the Schubert classes $\sigma_\lambda$ constructed above also form such a basis. However, although the number of elements in each degree is the same for the two bases, they are different bases, so one cannot simply read the parts of a partition as exponents to correspond $\sigma_\lambda$ to a monomial; the cup product between them is computed by the Littlewood-Richardson rule mentioned above. Now these $w_i$ satisfy all the axioms that Stiefel-Whitney classes satisfy, and existence is proved from the fact that this is preserved under pullback.

---

**References**

**[Hat]** A. Hatcher, *Vector Bundles and K-Theory*, online notes, 2017.  
**[MS]** J. W. Milnor and J. D. Stasheff, *Characteristic Classes*, Annals of Mathematics Studies 76, Princeton University Press, 1974.
