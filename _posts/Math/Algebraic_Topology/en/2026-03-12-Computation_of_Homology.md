---
title: "Computation of Homology"
description: "Practical tools for computing homology are covered, with homology analyzed using adjoint functors and colimit-preserving properties from category theory, and computation techniques examined through the definition of relative homology and long exact sequences. Concrete computation processes utilizing abelianization and colimit preservation are addressed."
excerpt: "Practical computation of homology via relative homology and Mayer-Vietoris"

categories: [Math / Algebraic Topology]
permalink: /en/math/algebraic_topology/computation_of_homology
sidebar: 
    nav: "algebraic_topology-en"

date: 2025-08-05
weight: 5
translated_at: 2026-08-18T14:15:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-09-20T11:15:05+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
We now examine tools that allow us to compute homology in practice. Directly calculating the homology of an arbitrary space from the definition is nearly impossible, so we must develop tools for breaking large spaces into smaller spaces and computing the homology of the large space from their homologies. The most intuitive situation is that of [§Covering Spaces, ⁋Theorem 13](/en/math/algebraic_topology/covering_spaces#thm13){: data-relation="weak" reviewed="" }, where we saw that the functor $\pi_1:\Top_\ast \rightarrow \Grp$ preserves colimits. Now the abelianization functor $\ab:\Grp \rightarrow \Ab$ is the left adjoint of the forgetful functor $U:\Ab \rightarrow \Grp$ ([\[Algebraic Structures\] §Abelian Groups, ⁋Proposition 7](/en/math/algebraic_structures/abelian_groups#prop7){: data-relation="weak" reviewed="" }), left adjoints preserve colimits ([\[Category Theory\] §Adjoint Functors, ⁋Theorem 9](/en/math/category_theory/adjoints#thm9){: data-relation="weak" reviewed="" }), and the first homology functor $H_1:\Top \rightarrow \Ab$ is the composite of these. Indeed, the morphism $\pi_1(X)\rightarrow H_1(X)$ sending a loop $\gamma$ to a singular $1$-simplex is well-defined, and when $X$ is path-connected its kernel is exactly the commutator subgroup $[\pi_1(X),\pi_1(X)]$, yielding $H_1(X)\cong\pi_1(X)^\ab$. Thus for pushouts of the type given by [§Covering Spaces, ⁋Corollary 14](/en/math/algebraic_topology/covering_spaces#cor14){: data-relation="weak" reviewed="" }, we can expect a result of the same form for $H_1$ as well. In particular, suppose as in [§Covering Spaces, ⁋Corollary 14](/en/math/algebraic_topology/covering_spaces#cor14){: data-relation="weak" reviewed="" } that a topological space $X$ is the union of two connected open subsets $U,V$ with $U\cap V$ also connected. Then in the category $\Ab$, the pushout of two abelian groups is given by the coequalizer of their direct sum, so for the maps $f:H_1(U\cap V)\rightarrow H_1(U)$ and $g:H_1(U\cap V)\rightarrow H_1(V)$ induced by the two inclusions, the following isomorphism

$$H_1(X)=H_1(U\cup V)\cong \frac{H_1(U)\oplus H_1(V)}{\left\langle (f(x),-g(x))\mid x\in H_1(U\cap V)\right\rangle}\tag{1}$$

must hold. In this post we treat this in a more general manner.

## Relative homology

To do so, we first need to generalize homology. For a space $X$ and any subspace $A$, we define the $k$-th relative chain group $C_k(X,A)$ as the quotient

$$C_k(X,A):=C_k(X)/C_k(A)$$

Then it is not difficult to see that the boundary map $\partial_k:C_k(X) \rightarrow C_{k-1}(X)$ induces a map $C_k(X,A) \rightarrow C_{k-1}(X,A)$ between the quotient groups. From this we can construct the chain complex

$$\cdots \longrightarrow C_k(X,A)\overset{\partial}{\longrightarrow} C_{k-1}(X,A)\longrightarrow\cdots$$

::: Definition 1
The $k$-th homology $H_k(X,A)$ of the above chain complex is called *relative homology*.
:::

Now consider the short exact sequence in the category $\Ch_{\geq 0}(\Ab)$

$$0 \rightarrow C_\bullet(A) \rightarrow C_\bullet(X) \rightarrow C_\bullet(X,A) \rightarrow 0$$

Then by [\[Homological Algebra\] §Long Exact Sequences, ⁋Theorem 1](/en/math/homological_algebra/long_exact_sequence#thm1){: data-relation="required" reviewed="" }, there exists the following long exact sequence

$$\cdots \rightarrow H_k(A) \rightarrow H_k(X) \rightarrow H_k(X,A)\rightarrow H_{k-1}(A) \rightarrow \cdots$$

Here, the connecting map $H_k(X,A) \rightarrow H_{k-1}(A)$ is nothing but applying the boundary map to an arbitrary cycle (or any representative thereof) of $H_k(X,A)$. Moreover, if a continuous map $f:X \rightarrow Y$ satisfies $f(A)\subseteq B$, then $f$ induces not only the original chain map $C_\bullet(X)\rightarrow C_\bullet(Y)$ but also $C_\bullet(A) \rightarrow C_\bullet(B)$, and from the fact that the following diagram

{% diagram Math/Algebraic_Topology/Computation_of_Homology-1.svg width="12.65em" alt="relative_homology" %}

commutes, a chain map $C_\bullet(X,A) \rightarrow C_\bullet(Y,B)$ is also induced. That is, $f:(X,A) \rightarrow (Y,B)$ satisfying this condition also induces a map $H_k(f):H_k(X,A) \rightarrow H_k(Y,B)$ on homology. Then the $h_n$ constructed in the proof of [§Homotopy, ⁋Proposition 6](/en/math/algebraic_topology/homotopy#prop6){: data-relation="required" reviewed="" } sends $C_\bullet(A)$ into $C_\bullet(B)$, so it descends to a chain homotopy between relative chain complexes; thus we see that whenever $F(A\times I)\subseteq B$ holds for a homotopy $F$, two maps $f,g:(X,A)\rightarrow (Y,B)$ homotopic via it induce the same map on homology.

## Excision theorem

Intuitively, for $(X,A)$, the relative homology $H_\bullet(X,A)$ is the homology of the chain complex corresponding to the cokernel of the inclusion $C_\bullet(A)\hookrightarrow C_\bullet(X)$, namely $C_\bullet(X,A)$. Intuitively, in this process the information about $C_\bullet(A)$ disappears upon taking the quotient, so it seems intuitively plausible that removing a subset contained in $A$ from the whole space would not change the relative homology. This is true under the following weak condition.

::: Theorem 2 (Excision theorem)
Let $X$ be a space with a subspace $A$, and in $A$, let a subspace $Z$ satisfy $\cl Z\subseteq \interior A$. Then the inclusion

$$(X\setminus Z, A\setminus Z)\hookrightarrow (X,A)$$

induces a map

$$H_k(X\setminus Z, A\setminus Z)\rightarrow H_k(X,A)$$

that is an isomorphism.
:::

However, while this theorem is intuitively obvious, its proof is somewhat technical, so we omit the proof here and refer to [Hat].

Meanwhile, in geometric situations we know a way to ignore the information contained in $A$ like this: that is, collapsing $A$ to a single point gives the quotient space $X/A$. Then it is a reasonable conjecture that there is a relationship between the homology $H_k(X/A)$ and the relative homology $H_k(X,A)$. Of course, as with the theorem above, this is possible only if $A$ is not too pathological a space.

::: Definition 3
For a space $X$ and a nonempty subspace $A$, the pair $(X,A)$ is called a *good pair* if $A$ is closed and there exists in $X$ an open subset $U$ such that $A\subseteq U$ and $A$ is a strong deformation retract of $U$.
:::

Given a good pair $(X,A)$, let $U$ be an open subset satisfying the hypothesis of [Definition 3](#def3){: data-relation="required" reviewed="" }. Then in the following diagram

{% diagram Math/Algebraic_Topology/Computation_of_Homology-2.svg width="27.21em" alt="3*3_diagram" %}

each row is exact and the first two columns are also exact, so by [\[Homological Algebra\] §Diagram chasing, ⁋Corollary 7](/en/math/homological_algebra/diagram_chasing#cor7){: data-relation="required" reviewed="" } we obtain a short exact sequence of chain complexes

$$0\rightarrow C_\bullet(U,A)\rightarrow C_\bullet(X,A)\rightarrow C_\bullet(X,U)\rightarrow 0$$

and the resulting long exact sequence

$$\cdots \rightarrow H_k(U,A) \rightarrow H_k(X,A)\rightarrow H_k(X,U)\rightarrow H_{k-1}(U,A)\rightarrow \cdots$$

Now from the assumption that $A$ is a strong deformation retract of $U$, we have $H_k(U,A)=0$ for all $k$, and therefore the isomorphism $H_k(X,A)\cong H_k(X,U)$ holds for all $k$.

On the other hand, for any closed subspace $A$, collapsing $A$ to a point yields a well-defined quotient space $X/A$, and the projection $X \rightarrow X/A$ sends $A$ to a single point $[A]$ and is a homeomorphism outside $A$. Then applying the same argument as above to the inclusion

$$\{[A]\}\subseteq U/A\subseteq X/A$$

since $U/A$ strongly deformation retracts onto the point $[A]$, from $H_k(U/A,[A])=0$ we obtain the following isomorphism

$$H_k(X/A, [A])\cong H_k(X/A, U/A)$$

and these fit into the following diagram induced by the quotient map

{% diagram Math/Algebraic_Topology/Computation_of_Homology-3.svg width="17.12em" alt="excision-1" %}

Now from the assumption that $(X,A)$ is a good pair, $A\subseteq U\subseteq X$ satisfies the condition $\cl A\subseteq \interior U$ of [Theorem 2](#thm2){: data-relation="required" reviewed="" }, so the inclusion

$$(X\setminus A, U\setminus A)\hookrightarrow (X,U)$$

induces an isomorphism $H_k(X\setminus A, U\setminus A)\rightarrow H_k(X,U)$, and similarly applying [Theorem 2](#thm2){: data-relation="required" reviewed="" } to the inclusion $\{[A]\}\subseteq U/A\subseteq X/A$ shows that the following map

$$H_k((X/A)\setminus [A], (U/A)\setminus [A])\rightarrow H_k(X/A,U/A)$$

is an isomorphism. These fit into the following diagram also induced by the quotient map

{% diagram Math/Algebraic_Topology/Computation_of_Homology-4.svg width="24.44em" alt="excision-2" %}

and here the left vertical map $H_k(X\setminus A, U\setminus A)\rightarrow H_k((X/A)\setminus [A], (U/A)\setminus [A])$ is an isomorphism because the quotient map $p:X\rightarrow X/A$ is a homeomorphism outside $A$. Combining these results we obtain the following isomorphism

$$H_k(X,A)\cong H_k(X/A,[A])\tag{2}$$

On the other hand, by [§Homology, ⁋Proposition 11](/en/math/algebraic_topology/homology#prop11){: data-relation="required" reviewed="" }, for any space $X$ and a point $x\in X$ the following long exact sequence

$$\begin{aligned}\cdots &\rightarrow H_k(x)\rightarrow H_k(X)\rightarrow H_k(X,x) \rightarrow H_{k-1}(x)\rightarrow\cdots \\\cdots&\rightarrow H_1(x)\rightarrow H_1(X) \rightarrow H_1(X,x) \rightarrow H_0(x) \rightarrow H_0(X)\rightarrow H_0(X,x)\rightarrow 0\end{aligned}$$

gives, for all $k>1$, the isomorphism $H_k(X)\cong H_k(X,x)$. Moreover, looking at the long exact sequence for $k=1$,

$$0 \rightarrow H_1(X) \rightarrow H_1(X, x) \overset{\partial}{\longrightarrow} H_{0}(x) \overset{\iota_\ast}{\longrightarrow} H_{0}(X)$$

here $\iota_\ast$ sends the generator of $H_0(x)$ to the path component of $X$ containing $x$, so it is injective; hence $\partial$ is the zero map, and from this we likewise obtain the isomorphism $H_1(X)\cong H_1(X,x)$.

Meanwhile, from the fact that $\iota_\ast$ is injective we obtain the following long exact sequence

$$0 \rightarrow H_0(x)\rightarrow H_0(X) \rightarrow H_0(X,x)\rightarrow 0$$

and from this the isomorphism $H_0(X,x)\cong H_0(X)/\mathbb{Z}$. Geometrically this is the same as removing the path component of $H_0(X)$ containing $x$. For notational convenience, if $X$ is path-connected we define the *reduced homology* $\widetilde{H}_k(X)$ for a fixed $x\in X$ by

$$\widetilde{H}_k(X)=H_k(X,x)$$

then we can rewrite the right-hand side of the above isomorphism (2) as $\widetilde{H}_k(X/A)$ and write as follows.

::: Proposition 4
For a good pair $(X,A)$, the quotient map $X \rightarrow X/A$ induces the following isomorphism for all $k$:

$$H_k(X,A)\cong \widetilde{H}_k(X/A)$$
:::

## Simplicial homology and singular homology

On the other hand, since the way we defined relative homology was by taking the cokernel of the monomorphism $C_\bullet(A)\rightarrow C_\bullet(X)$ in $\Ch_{\geq 0}(\Ab)$, we can repeat this process for $C^\Delta_\bullet(A) \rightarrow C^\Delta_\bullet(X)$. Then, as a result, we obtain the simplicial homology version of relative homology $H_n^\Delta(X,A)$. Now, since simplicial homology consists of chains that are not "singular", the inclusion

$$C_\bullet^\Delta(X) \rightarrow C_\bullet(X)$$

induces a canonical homomorphism

$$H_\bullet^\Delta(X)\rightarrow H_\bullet(X)\tag{3}$$

and similarly, there exist the following canonical homomorphisms:

$$H_\bullet^\Delta(A)\rightarrow H_\bullet(A),\qquad H_\bullet^\Delta(X,A)\rightarrow H_\bullet(X,A)$$

Then by [\[Homological Algebra\] §Long Exact Sequences, ⁋Proposition 2](/en/math/homological_algebra/long_exact_sequence#prop2){: data-relation="required" reviewed="" }, these define the following commutative diagram:

{% diagram Math/Algebraic_Topology/Computation_of_Homology-5.svg width="36.61em" alt="functoriality" %}

Using this, the following holds.

::: Theorem 5
For any $\Delta$-complex $X$, the homomorphism in (3) is an isomorphism. 
:::
::: Proof
We outline the general flow. By the above commutative diagram, after considering the filtration

$$X^0\subseteq X^1\subseteq\cdots\subseteq X^l=X$$

defined by the $\Delta$-complex structure of $X$, let us run an induction by applying [\[Homological Algebra\] §Diagram chasing, ⁋Corollary 2](/en/math/homological_algebra/diagram_chasing#cor2){: data-relation="required" reviewed="" } to the following diagram

{% diagram Math/Algebraic_Topology/Computation_of_Homology-6.svg width="56.75em" alt="induction" %}

For the induction, it suffices to show that for any $n$ and any $k$, the homomorphism between relative homologies

$$H_n^\Delta(X^k, X^{k-1})\rightarrow H_n(X^k, X^{k-1})$$

is an isomorphism. This is because, once this is assumed, first by [§Homology, ⁋Proposition 11](/en/math/algebraic_topology/homology#prop11){: data-relation="required" reviewed="" }, $H_n^\Delta(X^0)\cong H_n(X^0)$ holds for all $n$ when $k=1$, so by [\[Homological Algebra\] §Diagram chasing, ⁋Corollary 2](/en/math/homological_algebra/diagram_chasing#cor2){: data-relation="required" reviewed="" } we can show that $H_n^\Delta(X^1)\cong H_n(X^1)$, and from this we can again inductively construct the desired isomorphism for larger $k$.

First, by definition, $C_n^\Delta(X^k, X^{k-1})$ is nontrivial only when $n=k$, and therefore $H_n^\Delta(X^k, X^{k-1})$ is a nontrivial free abelian group (generated by the $k$-simplices) only when $n=k$, and is trivial in all other cases.
  
A similar result holds for singular homology: specifically, $H_n(\Delta^k,\partial\Delta^k)$ is a free abelian group only when $n=k$, and its generator is $\id:\Delta^k \rightarrow \Delta^k$. To verify this, define $\Lambda$ to be all but one of the $k-1$-dimensional faces of $\Delta^k$, and looking at the long exact sequence corresponding to $(\Delta^k, \partial\Delta^k, \Lambda)$

$$\cdots\rightarrow H_n(\Delta^k,\Lambda)\rightarrow H_n(\Delta^k, \partial\Delta^k)\rightarrow H_{n-1}(\partial\Delta^k, \Lambda)\rightarrow H_{n-1}(\Delta^k,\Lambda)\rightarrow \cdots$$

we see that the groups $H_\bullet(\Delta^k,\Lambda)$ are $0$ because $\Delta^k$ deformation retracts to $\Lambda$, and thus $H_k(\Delta^k, \partial\Delta^k)\cong H_{k-1}(\partial\Delta^k,\Lambda)$; on the other hand, for the good pair $(\partial\Delta^k,\Lambda)$, the quotient space $\partial\Delta^k/\Lambda$ is homeomorphic to the quotient space $\Delta^{k-1}/\partial\Delta^{k-1}$, so using these we obtain 

$$H_k(\Delta^k, \partial\Delta^{k})\cong H_{k-1}(\Delta^{k-1}, \partial\Delta^{k-1})$$

and can therefore show the desired result inductively.
  
Examining this process, we see that the generator of $H_k(\Delta^k,\partial\Delta^k)$ (as singular homology) is exactly the $k$-simplex $\Delta^k$. On the other hand, $(X^k,X^{k-1})$ is a good pair and its quotient is the wedge sum $X^k/X^{k-1}\cong\bigvee_\alpha \Delta^k_\alpha/\partial\Delta^k_\alpha$, so by [Proposition 4](#prop4){: data-relation="required" reviewed="" } we have $H_n(X^k,X^{k-1})\cong\widetilde{H}_n(X^k/X^{k-1})$, and applying additivity for wedge sums gives the desired result. Each chain contains only finitely many simplices and the image of each simplex is compact, so it lies in a suitable $X^k$; therefore, even for infinite-dimensional $\Delta$-complexes, taking the direct limit of the above results yields the same conclusion. 
:::

## Mayer-Vietoris sequence

Although we did not include the proof due to space constraints, [Theorem 2](#thm2){: data-relation="weak" reviewed="" } is very useful when dealing with homology theory. For example, in the proof of [Theorem 5](#thm5){: data-relation="weak" reviewed="" }, we used the excision theorem when ignoring simplices of dimension less than $k-1$, which allowed us to use induction, where the base step was the homology of a one-point space. This process can be seen as essentially possessing all the properties that homology should satisfy, and axiomatizing this gives the following.

::: Definition 6 (Eilenberg-Steenrod axioms)
For functors $H_k$ from the category of pairs of topological spaces to the category of abelian groups and natural transformations between them

$$\partial:H_k(X,A)\rightarrow H_{k-1}(A,\emptyset):=H_{k-1}(A)$$

the *Eilenberg-Steenrod axioms* refer to the following axioms.

- (Homotopy) If two homotopic maps $(X,A) \rightarrow (Y,B)$ are given, the two homomorphisms $H_k(X,A) \rightarrow H_k(Y,B)$ they induce are also identical.
- (Excision) For $(X,A,Z)$ satisfying the condition of [Theorem 2](#thm2){: data-relation="required" reviewed="" }, the inclusion $(X\setminus Z, A\setminus Z)\hookrightarrow (X,A)$ induces an isomorphism.
- (Dimension) For a one-point space $\ast$, $H_k(\ast)=0$ holds for all $k>0$.
- (Additivity) If $X=\coprod X_\alpha$, then $H_k(X)\cong\bigoplus H_k(X_\alpha)$.
- (Exactness) For each pair $(X,A)$, the two inclusions $(A,\emptyset) \hookrightarrow (X,\emptyset)$ and $(X,\emptyset)\hookrightarrow (X,A)$ fit into the following long exact sequence:

    $$\cdots \rightarrow H_k(A)\rightarrow H_k(X) \rightarrow H_k(X,A) \rightarrow H_{k-1}(A)\rightarrow \cdots$$
:::

Then the result of Eilenberg and Steenrod shows that homology theories defined in this manner are all naturally isomorphic on the category of CW pairs, provided the *coefficient group* $H_0(\ast)$ is fixed. For example, we proved earlier that simplicial homology and singular homology agree on $\Delta$-complexes, and examining the proof step by step reveals that what we essentially used were the axioms of [Definition 6](#def6){: data-relation="weak" reviewed="" } above. For practical computation of homology, it is useful to introduce *cellular homology* defined on *CW complexes*; likewise, this homology also satisfies the above axioms and therefore gives the same computations as simplicial and singular homology.

On the other hand, in these homology theories the coefficient group is fixed to be $\mathbb{Z}$, but even if we replace it with an arbitrary abelian group $A$, all the axioms of [Definition 6](#def6){: data-relation="required" reviewed="" } still hold unchanged. Indeed, when defining singular or simplicial homology, if we had taken the chain groups

$$C^\Delta_\bullet(X),\qquad C_\bullet(X)$$

not as free abelian groups but as direct sums of $A$ indexed by simplices

$$C^\Delta_\bullet(X;A):=C^\Delta_\bullet(X)\otimes_\mathbb{Z}A,\qquad C_\bullet(X;A):=C_\bullet(X)\otimes_\mathbb{Z}A$$

we would have obtained this type of homology. ([\[Algebraic Structures\] §Abelian Groups, ⁋Definition 13](/en/math/algebraic_structures/abelian_groups#def13){: data-relation="weak" reviewed="" }) In particular, when the coefficient $A$ is a commutative ring $R$, this corresponds to taking the extension of scalars via the ring homomorphism $\mathbb{Z}\rightarrow R$ ([\[Algebraic Structures\] §Change of Scalars, ⁋Proposition 6](/en/math/algebraic_structures/change_of_base_ring#prop6){: data-relation="required" reviewed="" }), and the resulting chain complex and homology naturally have an $R$-module structure.

Most properties of homology follow from the axioms of [Definition 6](#def6){: data-relation="required" reviewed="" }. For example, the generalization of equation (1), which is the goal of this post, can be derived from them. Suppose a topological space $X$ is expressed as the union of two open sets $X=U\cup V$. Then taking homology of the following inclusions

{% diagram Math/Algebraic_Topology/Computation_of_Homology-7.svg width="7.54em" alt="inclusions" %}

gives, by exactness, a morphism between long exact sequences, and here the inclusion

$$(V,U\cap V)\rightarrow (X,U)$$

induces an isomorphism in homology by the excision axiom, so the corresponding maps in the above morphism are all isomorphisms. That is, we obtain the following morphism of long exact sequences

{% diagram Math/Algebraic_Topology/Computation_of_Homology-8.svg width="43.25em" alt="morphism_of_les" %}

where $i,j,k$ are the maps induced by the respective inclusions, the $\partial$'s are connecting maps, and the $p$'s are cokernel morphisms. We have omitted the indices for convenience. Now let $\alpha$ be this morphism of long exact sequences, and let the mapping cone exact sequence of $\alpha$ given by [\[Homological Algebra\] §Long Exact Sequences, ⁋Definition 8](/en/math/homological_algebra/long_exact_sequence#def8){: data-relation="required" reviewed="" }

$$\begin{aligned}\cdots &\overset{\overline{\partial}}{\longrightarrow} H_{n+1}(V, U\cap V)\oplus H_{n+1}(X)\overset{\overline{\Phi}}{\longrightarrow} H_n(U\cap V)\oplus H_{n+1}(X,U)\overset{\overline{\Psi}}{\longrightarrow} H_n(V)\oplus H_n(U)\\ \phantom{\cdots}&\overset{\overline{\partial}}{\longrightarrow} H_n(V, U\cap V)\oplus H_n(X)\rightarrow \cdots\end{aligned}$$

be denoted by $\Cone(\alpha)$. Then by the preceding consequence of the excision axiom, there exists the following long exact sequence:

$$\cdots \rightarrow 0 \rightarrow H_{n+1}(V, U\cap V)\rightarrow H_{n+1}(X,U)\rightarrow 0 \rightarrow \cdots\tag{4}$$

Here, the differential of $\Cone(\alpha)$ also sends elements of the first component to the second component, so the two components do not simply split apart; however, we know that after a change of basis defined by the isomorphisms $i_V$, $\Cone(\alpha)$ can be represented as the direct sum of this trivial long exact sequence and the following long exact sequence:

$$\cdots \rightarrow H_{n+1}(U)\oplus H_{n+1}(V)\rightarrow H_{n+1}(X)\rightarrow H_n(U\cap V)\rightarrow H_n(U)\oplus H_n(V)\rightarrow\cdots\tag{5}$$

Now since the two long exact sequences connected by $\alpha$ are both exact, $\alpha$ is a quasi-isomorphism, and therefore by [\[Homological Algebra\] §Long Exact Sequences, ⁋Corollary 9](/en/math/homological_algebra/long_exact_sequence#cor9){: data-relation="required" reviewed="" }, $\Cone(\alpha)$ is exact. Then since (4) is also exact, (5) is exact as well, and the differential maps of the exact sequence (5) are obtained through the above change of basis. Computing this explicitly gives the following.

::: Proposition 7 (Mayer-Vietoris sequence)
Suppose a topological space $X$ is expressed as the union of two open sets $X=U\cup V$, and consider a homology theory $H$ defined on it. Then there exists a long exact sequence

$$\cdots \rightarrow H_{n+1}(U)\oplus H_{n+1}(V)\overset{\Psi}{\longrightarrow} H_{n+1}(X)\overset{\partial}{\longrightarrow} H_n(U\cap V)\overset{\Phi}{\longrightarrow} H_n(U)\oplus H_n(V)\rightarrow\cdots$$

where the maps $\Psi, \Phi$ are given respectively by

$$\Psi(u,v)=u+v,\qquad \Phi(x)=(x,-x)$$
:::

In particular, looking at the case $n=1$, we obtain (1), which was carried over from the Seifert-van Kampen theorem through abelianization at the very beginning, and in this respect the Mayer-Vietoris sequence can be thought of as the homology version of the Seifert-van Kampen theorem.

---

**References**

**[Hat]** A. Hatcher, *Algebraic Topology*. Cambridge University Press, 2022.  
**[May]** J. P. May, *A concise course in algebraic topology*.

---
