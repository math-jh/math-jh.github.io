---
title: "Computing Homology"
description: "This post covers practical tools for computing homology. It analyzes homology using adjoint functors and colimit-preserving properties from category theory, and examines computation techniques through relative homology and long exact sequences."
excerpt: "Practical homology computations via relative homology and Mayer-Vietoris"

categories: [Math / Algebraic Topology]
permalink: /en/math/algebraic_topology/computation_of_homology
sidebar: 
    nav: "algebraic_topology-en"

date: 2025-08-05
weight: 5
translated_at: 2026-08-15T15:48:11+00:00
translation_source: kimi-cli
---
We now examine tools that allow us to compute homology in practice. Directly calculating the homology of an arbitrary space from the definition is nearly impossible, so we must develop methods for breaking large spaces into smaller pieces and computing the homology of the large space from those of the pieces. The most intuitive situation is that of [§Covering Spaces, ⁋Theorem 13](/en/math/algebraic_topology/covering_spaces#thm13), where we saw that the functor $\pi_1:\Top_\ast \rightarrow \Grp$ preserves colimits. Now the abelianization functor $\ab:\Grp \rightarrow \Ab$ is the left adjoint of the forgetful functor $U:\Ab \rightarrow \Grp$ ([[Algebraic Structures] §Abelian Groups, ⁋Proposition 7](/en/math/algebraic_structures/abelian_groups#prop7)), left adjoints preserve colimits ([[Category Theory] §Adjoints, ⁋Theorem 9](/en/math/category_theory/adjoints#thm9)), and the first homology functor $H_1:\Top \rightarrow \Ab$ is the composite of these. Indeed, the map $\pi_1(X)\rightarrow H_1(X)$ sending a loop $\gamma$ to a singular $1$-simplex is well-defined, and when $X$ is path-connected its kernel is exactly the commutator subgroup $[\pi_1(X),\pi_1(X)]$, yielding $H_1(X)\cong\pi_1(X)^\ab$. Thus for pushouts of the type given by [§Covering Spaces, ⁋Corollary 14](/en/math/algebraic_topology/covering_spaces#cor14), we can expect an analogous result for $H_1$. In particular, suppose as in [§Covering Spaces, ⁋Corollary 14](/en/math/algebraic_topology/covering_spaces#cor14) that a topological space $X$ is the union of two connected open subsets $U,V$ with $U\cap V$ also connected. Then in the category $\Ab$, the pushout of two abelian groups is given by the coequalizer of their direct sum, so for the maps $f:H_1(U\cap V)\rightarrow H_1(U)$ and $g:H_1(U\cap V)\rightarrow H_1(V)$ induced by the two inclusions, we have the isomorphism

$$H_1(X)=H_1(U\cup V)\cong \frac{H_1(U)\oplus H_1(V)}{\left\langle (f(x),-g(x))\mid x\in H_1(U\cap V)\right\rangle}\tag{1}$$

In this post we treat this in a more general manner.

## Relative homology

To do so, we first need to generalize homology. For a space $X$ and any subspace $A$, we define the $k$-th relative chain group $C_k(X,A)$ as the quotient

$$C_k(X,A):=C_k(X)/C_k(A)$$

It is not difficult to see that the boundary map $\partial_k:C_k(X) \rightarrow C_{k-1}(X)$ induces a map $C_k(X,A) \rightarrow C_{k-1}(X,A)$ between the quotient groups. From this we obtain the chain complex

$$\cdots \longrightarrow C_k(X,A)\overset{\partial}{\longrightarrow} C_{k-1}(X,A)\longrightarrow\cdots$$

::: Definition 1
The $k$-th homology of the above chain complex, denoted $H_k(X,A)$, is called *relative homology*.
:::

Now consider the short exact sequence in the category $\Ch_{\geq 0}(\Ab)$

$$0 \rightarrow C_\bullet(A) \rightarrow C_\bullet(X) \rightarrow C_\bullet(X,A) \rightarrow 0$$

Then by [[Homological Algebra] §Long Exact Sequence, ⁋Theorem 1](/en/math/homological_algebra/long_exact_sequence#thm1), we have the following long exact sequence

$$\cdots \rightarrow H_k(A) \rightarrow H_k(X) \rightarrow H_k(X,A)\rightarrow H_{k-1}(A) \rightarrow \cdots$$

Here the connecting map $H_k(X,A) \rightarrow H_{k-1}(A)$ is nothing but taking the boundary map of an arbitrary cycle (or any representative thereof) in $H_k(X,A)$. Moreover, if a continuous map $f:X \rightarrow Y$ satisfies $f(A)\subseteq B$, then $f$ induces not only the original chain map $C_\bullet(X)\rightarrow C_\bullet(Y)$ but also $C_\bullet(A) \rightarrow C_\bullet(B)$, and from the fact that the following diagram

{% diagram Math/Algebraic_Topology/Computation_of_Homology-1.svg width="12.65em" alt="relative_homology" %}

commutes, we also obtain a chain map $C_\bullet(X,A) \rightarrow C_\bullet(Y,B)$. That is, such an $f:(X,A) \rightarrow (Y,B)$ satisfying this condition also induces a map $H_k(f):H_k(X,A) \rightarrow H_k(Y,B)$ in homology. Then the $h_n$ constructed in the proof of [§Homotopy, ⁋Proposition 6](/en/math/algebraic_topology/homotopy#prop6) sends $C_\bullet(A)$ into $C_\bullet(B)$, so it descends to a chain homotopy between relative chain complexes; hence two maps $f,g:(X,A)\rightarrow (Y,B)$ that are homotopic via a homotopy $F$ with $F(A\times I)\subseteq B$ induce the same map in homology.

## Excision theorem

Intuitively, the relative homology $H_\bullet(X,A)$ of a pair $(X,A)$ is the homology of the chain complex $C_\bullet(X,A)$, which corresponds to the cokernel of the inclusion $C_\bullet(A)\hookrightarrow C_\bullet(X)$. Intuitively, in this process the information about $C_\bullet(A)$ disappears upon taking the quotient, so it seems plausible that removing a subset contained in $A$ would not change the relative homology. This is true under the following mild condition.

::: Theorem 2 (Excision theorem)
Let $A$ be a subspace of a space $X$, and let $Z$ be a subspace of $A$ satisfying $\cl Z\subseteq \interior A$. Then the inclusion

$$(X\setminus Z, A\setminus Z)\hookrightarrow (X,A)$$

induces an isomorphism

$$H_k(X\setminus Z, A\setminus Z)\rightarrow H_k(X,A)$$
:::

However, despite this theorem being intuitively obvious, its proof involves somewhat technical details, so we omit it here and refer to [Hat].

On the other hand, in geometric situations we already know a way to ignore information contained in $A$ in this manner: namely the quotient space $X/A$ obtained by collapsing $A$ to a point. It is then reasonable to conjecture that there is a relationship between the homology $H_k(X/A)$ and the relative homology $H_k(X,A)$. Of course, as with the theorem above, this is only possible if $A$ is not too pathological.

::: Definition 3
For a space $X$ and a nonempty subspace $A$, the pair $(X,A)$ is called a *good pair* if $A$ is a closed subset and there exists a suitable open subset $U$ of $X$ such that $A\subseteq U$ and $A$ is a strong deformation retract of $U$.
:::

Given a good pair $(X,A)$, let $U$ be an open subset satisfying the hypothesis of [Definition 3](#def3). Then in the following diagram

{% diagram Math/Algebraic_Topology/Computation_of_Homology-2.svg width="27.21em" alt="3*3_diagram" %}

each row is exact and the first two columns are also exact, so by [[Homological Algebra] §Diagram Chasing, ⁋Corollary 7](/en/math/homological_algebra/diagram_chasing#cor7) we obtain a short exact sequence of chain complexes

$$0\rightarrow C_\bullet(U,A)\rightarrow C_\bullet(X,A)\rightarrow C_\bullet(X,U)\rightarrow 0$$

and the resulting long exact sequence

$$\cdots \rightarrow H_k(U,A) \rightarrow H_k(X,A)\rightarrow H_k(X,U)\rightarrow H_{k-1}(U,A)\rightarrow \cdots$$

Now from the assumption that $A$ is a strong deformation retract of $U$, we have $H_k(U,A)=0$ for all $k$, and therefore the isomorphism $H_k(X,A)\cong H_k(X,U)$ holds for all $k$.

On the other hand, for any closed subspace $A$, the quotient space $X/A$ obtained by collapsing $A$ to a point is well-defined, and the projection $X \rightarrow X/A$ sends $A$ to a single point $[A]$ and is a homeomorphism outside $A$. Then applying the same argument as above to the inclusions

$$\{[A]\}\subseteq U/A\subseteq X/A$$

we obtain that since $U/A$ strongly deformation retracts onto the point $[A]$, we have $H_k(U/A,[A])=0$ and thus the isomorphism

$$H_k(X/A, [A])\cong H_k(X/A, U/A)$$

and these fit into the following diagram induced by the quotient map

{% diagram Math/Algebraic_Topology/Computation_of_Homology-3.svg width="17.12em" alt="excision-1" %}

Now from the assumption that $(X,A)$ is a good pair, the inclusions $A\subseteq U\subseteq X$ satisfy the condition $\cl A\subseteq \interior U$ of [Theorem 2](#thm2), so the inclusion

$$(X\setminus A, U\setminus A)\hookrightarrow (X,U)$$

induces an isomorphism $H_k(X\setminus A, U\setminus A)\rightarrow H_k(X,U)$, and similarly applying [Theorem 2](#thm2) to the inclusions $\{[A]\}\subseteq U/A\subseteq X/A$ shows that the map

$$H_k((X/A)\setminus [A], (U/A)\setminus [A])\rightarrow H_k(X/A,U/A)$$

is an isomorphism. These fit into the following diagram also induced by the quotient map

{% diagram Math/Algebraic_Topology/Computation_of_Homology-4.svg width="24.44em" alt="excision-2" %}

and here the left vertical map $H_k(X\setminus A, U\setminus A)\rightarrow H_k((X/A)\setminus [A], (U/A)\setminus [A])$ is an isomorphism because the quotient map $p:X\rightarrow X/A$ is a homeomorphism outside $A$. Combining these results we obtain the isomorphism

$$H_k(X,A)\cong H_k(X/A,[A])\tag{2}$$

On the other hand, by [§Homology, ⁋Proposition 11](/en/math/algebraic_topology/homology#prop11), for any space $X$ and a point $x\in X$ the following long exact sequence

$$\begin{aligned}\cdots &\rightarrow H_k(x)\rightarrow H_k(X)\rightarrow H_k(X,x) \rightarrow H_{k-1}(x)\rightarrow\cdots \\\cdots&\rightarrow H_1(x)\rightarrow H_1(X) \rightarrow H_1(X,x) \rightarrow H_0(x) \rightarrow H_0(X)\rightarrow H_0(X,x)\rightarrow 0\end{aligned}$$

gives isomorphisms $H_k(X)\cong H_k(X,x)$ for all $k>1$. Moreover, looking at the long exact sequence for $k=1$,

$$0 \rightarrow H_1(X) \rightarrow H_1(X, x) \overset{\partial}{\longrightarrow} H_{0}(x) \overset{\iota_\ast}{\longrightarrow} H_{0}(X)$$

here $\iota_\ast$ sends the generator of $H_0(x)$ to the path component of $X$ containing $x$, so it is injective; hence $\partial$ is the zero map, and from this we again obtain the isomorphism $H_1(X)\cong H_1(X,x)$.

From the fact that $\iota_\ast$ is injective we also obtain the long exact sequence

$$0 \rightarrow H_0(x)\rightarrow H_0(X) \rightarrow H_0(X,x)\rightarrow 0$$

and from this the isomorphism $H_0(X,x)\cong H_0(X)/\mathbb{Z}$. Geometrically this is the same as removing the path component of $H_0(X)$ containing $x$. For notational convenience, if $X$ is path-connected we define the *reduced homology* $\widetilde{H}_k(X)$ for a fixed $x\in X$ by

$$\widetilde{H}_k(X)=H_k(X,x)$$

then we can rewrite the right-hand side of the above isomorphism (2) as $\widetilde{H}_k(X/A)$, giving the following.

::: Proposition 4
For a good pair $(X,A)$, the quotient map $X \rightarrow X/A$ induces, for all $k$, the isomorphism

$$H_k(X,A)\cong \widetilde{H}_k(X/A)$$
:::

## Simplicial homology and singular homology

On the other hand, since the way we defined relative homology was by taking the cokernel of the monomorphism $C_\bullet(A)\rightarrow C_\bullet(X)$ in $\Ch_{\geq 0}(\Ab)$, we can repeat this process for $C^\Delta_\bullet(A) \rightarrow C^\Delta_\bullet(X)$. As a result we obtain a simplicial homology version of relative homology, denoted $H_n^\Delta(X,A)$. Now simplicial homology uses chains that are not "singular," so the inclusion

$$C_\bullet^\Delta(X) \rightarrow C_\bullet(X)$$

induces a canonical homomorphism

$$H_\bullet^\Delta(X)\rightarrow H_\bullet(X)\tag{3}$$

and similarly we have the following canonical homomorphisms

$$H_\bullet^\Delta(A)\rightarrow H_\bullet(A),\qquad H_\bullet^\Delta(X,A)\rightarrow H_\bullet(X,A)$$

Then by [[Homological Algebra] §Long Exact Sequence, ⁋Proposition 2](/en/math/homological_algebra/long_exact_sequence#prop2) these define the following commutative diagram

{% diagram Math/Algebraic_Topology/Computation_of_Homology-5.svg width="36.61em" alt="functoriality" %}

Using this, the following holds.

::: Theorem 5
For any $\Delta$-complex $X$, the homomorphism in (3) is an isomorphism.
:::
::: Proof
We sketch the main idea. Using the above commutative diagram, we consider the filtration defined by the $\Delta$-complex structure of $X$

$$X^0\subseteq X^1\subseteq\cdots\subseteq X^l=X$$

and apply [[Homological Algebra] §Diagram Chasing, ⁋Corollary 2](/en/math/homological_algebra/diagram_chasing#cor2) to the following diagram

{% diagram Math/Algebraic_Topology/Computation_of_Homology-6.svg width="56.75em" alt="induction" %}

to run an induction. For the induction step, it suffices to show that for any $n$ and any $k$, the homomorphism between relative homologies

$$H_n^\Delta(X^k, X^{k-1})\rightarrow H_n(X^k, X^{k-1})$$

is an isomorphism. Once this is assumed, first by [§Homology, ⁋Proposition 11](/en/math/algebraic_topology/homology#prop11) we have $H_n^\Delta(X^0)\cong H_n(X^0)$ for all $n$ when $k=1$, so by [[Homological Algebra] §Diagram Chasing, ⁋Corollary 2](/en/math/homological_algebra/diagram_chasing#cor2) we can show $H_n^\Delta(X^1)\cong H_n(X^1)$, and then inductively construct the desired isomorphism for larger $k$.

First, by definition $C_n^\Delta(X^k, X^{k-1})$ is nontrivial only when $n=k$, so $H_n^\Delta(X^k, X^{k-1})$ is a nontrivial free abelian group (generated by the $k$-simplices) only when $n=k$, and trivial otherwise.

A similar result holds for singular homology: specifically, $H_n(\Delta^k,\partial\Delta^k)$ is a free abelian group only when $n=k$, and its generator is $\id:\Delta^k \rightarrow \Delta^k$. To verify this, define $\Lambda$ to be $\Delta^k$ with one of its $(k-1)$-dimensional faces removed, and consider the long exact sequence for $(\Delta^k, \partial\Delta^k, \Lambda)$

$$\cdots\rightarrow H_n(\Delta^k,\Lambda)\rightarrow H_n(\Delta^k, \partial\Delta^k)\rightarrow H_{n-1}(\partial\Delta^k, \Lambda)\rightarrow H_{n-1}(\Delta^k,\Lambda)\rightarrow \cdots$$

Since $\Delta^k$ deformation retracts onto $\Lambda$, the groups $H_\bullet(\Delta^k,\Lambda)$ vanish, so $H_k(\Delta^k, \partial\Delta^k)\cong H_{k-1}(\partial\Delta^k,\Lambda)$, and on the other hand for the good pair $(\partial\Delta^k,\Lambda)$ the quotient space $\partial\Delta^k/\Lambda$ is homeomorphic to the quotient space $\Delta^{k-1}/\partial\Delta^{k-1}$, so using these we obtain

$$H_k(\Delta^k, \partial\Delta^{k})\cong H_{k-1}(\Delta^{k-1}, \partial\Delta^{k-1})$$

and thus the desired result follows inductively.

Examining this process, we see that the generator of $H_k(\Delta^k,\partial\Delta^k)$ (as singular homology) is exactly the $k$-simplex $\Delta^k$ itself. On the other hand $(X^k,X^{k-1})$ is a good pair and its quotient is the wedge sum $X^k/X^{k-1}\cong\bigvee_\alpha \Delta^k_\alpha/\partial\Delta^k_\alpha$, so by [Proposition 4](#prop4) we have $H_n(X^k,X^{k-1})\cong\widetilde{H}_n(X^k/X^{k-1})$, and applying additivity for wedge sums gives the desired result. Each chain contains only finitely many simplices and the image of each simplex is compact, so it lies in a suitable $X^k$; hence for infinite-dimensional $\Delta$-complexes we also obtain the same conclusion by taking a direct limit of the above results.
:::

## Mayer-Vietoris sequence

Although we have omitted the proof for reasons of length, the excision theorem of [Theorem 2](#thm2) is a powerful tool in homology theory. For example, in the proof of [Theorem 5](#thm5) we used the excision theorem to ignore simplices of dimension less than $k-1$, which allowed us to use induction with the base step being the homology of a one-point space. This process can be seen as essentially having all the properties that homology should satisfy, and axiomatizing this gives the following.

::: Definition 6 (Eilenberg-Steenrod axioms)
For functors $H_k$ from the category of pairs of topological spaces to the category of abelian groups, together with natural transformations

$$\partial:H_k(X,A)\rightarrow H_{k-1}(A,\emptyset):=H_{k-1}(A)$$

the *Eilenberg-Steenrod axioms* are the following axioms.

- (Homotopy) If two maps $(X,A) \rightarrow (Y,B)$ are homotopic, then the two homomorphisms $H_k(X,A) \rightarrow H_k(Y,B)$ they induce are identical.
- (Excision) For $(X,A,Z)$ satisfying the condition of [Theorem 2](#thm2), the inclusion $(X\setminus Z, A\setminus Z)\hookrightarrow (X,A)$ induces an isomorphism.
- (Dimension) For a one-point space $\ast$, $H_k(\ast)=0$ for all $k>0$.
- (Additivity) If $X=\coprod X_\alpha$, then $H_k(X)\cong\bigoplus H_k(X_\alpha)$.
- (Exactness) For each pair $(X,A)$, the two inclusions $(A,\emptyset) \hookrightarrow (X,\emptyset)$ and $(X,\emptyset)\hookrightarrow (X,A)$ fit into the following long exact sequence

    $$\cdots \rightarrow H_k(A)\rightarrow H_k(X) \rightarrow H_k(X,A) \rightarrow H_{k-1}(A)\rightarrow \cdots$$
:::

Then the result of Eilenberg and Steenrod shows that homology theories defined in this manner are all naturally isomorphic on the category of CW pairs, provided the *coefficient group* $H_0(\ast)$ is fixed. For example, we proved earlier that simplicial homology and singular homology agree on $\Delta$-complexes, and examining the proof step by step reveals that what we essentially used were the axioms of [Definition 6](#def6) above. For practical computation of homology it is useful to introduce *cellular homology* defined on *CW complexes*; likewise this homology also satisfies the above axioms and therefore gives the same computations as simplicial and singular homology.

On the other hand, in these homology theories the coefficient group is fixed to be $\mathbb{Z}$, but if we replace it with an arbitrary abelian group $A$, all the axioms of [Definition 6](#def6) still hold unchanged. Indeed, when defining singular or simplicial homology, if we had taken the chain groups

$$C^\Delta_\bullet(X),\qquad C_\bullet(X)$$

not as free abelian groups but as direct sums of $A$ indexed by simplices

$$C^\Delta_\bullet(X;A):=C^\Delta_\bullet(X)\otimes_\mathbb{Z}A,\qquad C_\bullet(X;A):=C_\bullet(X)\otimes_\mathbb{Z}A$$

we would have obtained this type of homology.

Most properties of homology follow from the axioms of [Definition 6](#def6). For example, the generalization of equation (1), which is the goal of this post, can be derived from them. Suppose a topological space $X$ is expressed as the union of two open sets $X=U\cup V$. Then taking homology of the following inclusions

{% diagram Math/Algebraic_Topology/Computation_of_Homology-7.svg width="7.54em" alt="inclusions" %}

gives, by exactness, a morphism between long exact sequences, and here the inclusion

$$(V,U\cap V)\rightarrow (X,U)$$

induces an isomorphism in homology by the excision axiom, so the corresponding maps in the above morphism are all isomorphisms. That is, we obtain the following morphism of long exact sequences

{% diagram Math/Algebraic_Topology/Computation_of_Homology-8.svg width="43.25em" alt="morphism_of_les" %}

where $i,j,k$ are the maps induced by the respective inclusions, the $\partial$'s are connecting maps, and the $p$'s are cokernel morphisms. We have omitted the indices for convenience. Now let $\alpha$ denote this morphism of long exact sequences, and consider the mapping cone exact sequence of $\alpha$ given by [[Homological Algebra] §Long Exact Sequence, ⁋Definition 8](/en/math/homological_algebra/long_exact_sequence#def8)

$$\begin{aligned}\cdots &\overset{\overline{\partial}}{\longrightarrow} H_{n+1}(V, U\cap V)\oplus H_{n+1}(X)\overset{\overline{\Phi}}{\longrightarrow} H_n(U\cap V)\oplus H_{n+1}(X,U)\overset{\overline{\Psi}}{\longrightarrow} H_n(V)\oplus H_n(U)\\ \phantom{\cdots}&\overset{\overline{\partial}}{\longrightarrow} H_n(V, U\cap V)\oplus H_n(X)\rightarrow \cdots\end{aligned}$$

and denote it by $\Cone(\alpha)$. Then by the previous consequence of the excision axiom, we have the following long exact sequence

$$\cdots \rightarrow 0 \rightarrow H_{n+1}(V, U\cap V)\rightarrow H_{n+1}(X,U)\rightarrow 0 \rightarrow \cdots\tag{4}$$

Here the differential of $\Cone(\alpha)$ sends an element of the first component to the second component as well, so the two components do not simply split apart; however, after a change of basis defined by the isomorphisms $i_V$, we can represent $\Cone(\alpha)$ as the direct sum of this trivial long exact sequence and the following long exact sequence

$$\cdots \rightarrow H_{n+1}(U)\oplus H_{n+1}(V)\rightarrow H_{n+1}(X)\rightarrow H_n(U\cap V)\rightarrow H_n(U)\oplus H_n(V)\rightarrow\cdots\tag{5}$$

Now since the two long exact sequences connected by $\alpha$ are both exact, $\alpha$ is a quasi-isomorphism, and therefore by [[Homological Algebra] §Long Exact Sequence, ⁋Corollary 9](/en/math/homological_algebra/long_exact_sequence#cor9), $\Cone(\alpha)$ is exact. Then since (4) is also exact, (5) is exact as well, and the differential maps of the exact sequence (5) are obtained through the above change of basis. Computing this explicitly gives the following.

::: Proposition 7 (Mayer-Vietoris sequence)
Suppose a topological space $X$ is expressed as the union of two open sets $X=U\cup V$, and consider a homology theory $H$ defined on it. Then there exists a long exact sequence

$$\cdots \rightarrow H_{n+1}(U)\oplus H_{n+1}(V)\overset{\Psi}{\longrightarrow} H_{n+1}(X)\overset{\partial}{\longrightarrow} H_n(U\cap V)\overset{\Phi}{\longrightarrow} H_n(U)\oplus H_n(V)\rightarrow\cdots$$

where the maps $\Psi, \Phi$ are given by

$$\Psi(u,v)=u+v,\qquad \Phi(x)=(x,-x)$$
:::

In particular, looking at the case $n=1$, we recover equation (1) obtained earlier by abelianizing the Seifert-van Kampen theorem, and in this sense the Mayer-Vietoris sequence can be thought of as the homology version of the Seifert-van Kampen theorem.

---

**References**

**[Hat]** A. Hatcher, *Algebraic Topology*. Cambridge University Press, 2022.  
**[May]** J. P. May, *A concise course in algebraic topology*.

---
