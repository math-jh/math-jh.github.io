---
title: "Computation of Homology"
description: "This post covers practical tools for computing homology. It explores analyzing homology using the adjoint functor and colimit preservation in category theory, and examines computation techniques through the definition of relative homology and long exact sequences. Concrete calculation procedures using abelianization and colimit preservation are also discussed."
excerpt: "Practical homology computation via relative homology and Mayer-Vietoris"

categories: [Math / Algebraic Topology]
permalink: /en/math/algebraic_topology/computation_of_homology
sidebar: 
    nav: "algebraic_topology-en"

date: 2025-08-05
weight: 5
translated_at: 2026-06-24T02:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-24T02:30:02+00:00
---
We now examine tools that allow us to compute homology in practice. Since directly computing the homology of an arbitrary space from the definition is virtually impossible, we must develop tools for breaking large spaces into smaller pieces and computing the homology of the large space from those of the pieces. The most intuitive situation is that of the Seifert–van Kampen theorem ([§Covering Spaces, ⁋Theorem 13](/en/math/algebraic_topology/covering_spaces#thm13)), where we saw that the functor $$\pi_1:\Top \rightarrow \Grp$$ preserves colimits. Now the abelianization functor $$\ab:\Grp \rightarrow \Ab$$ is the left adjoint of the forgetful functor $$U:\Ab \rightarrow \Grp$$ ([\[Algebraic Structures\] §Abelian Groups, ⁋Proposition 7](/en/math/algebraic_structures/abelian_groups#prop7)), and a left adjoint preserves colimits ([\[Category Theory\] §Adjoints, ⁋Theorem 9](/en/math/category_theory/adjoints#thm9)); since the first homology functor $$H_1:\Top \rightarrow \Ab$$ is the composite of these ([§Covering Spaces, ⁋Theorem 15](/en/math/algebraic_topology/covering_spaces#thm15)), it too must preserve colimits. In particular, as in [§Covering Spaces, ⁋Corollary 14](/en/math/algebraic_topology/covering_spaces#cor14), let a topological space $$X$$ be expressed as the union of two connected open subsets $$U,V$$. Then in the category $$\Ab$$, the pushout of two abelian groups is given by the coequalizer of their direct sum, so the following isomorphism

$$H_1(X)=H_1(U\cup V)\cong \frac{H_1(U)\oplus H_1(V)}{\left\langle (f(x),-g(x))\mid x\in H_1(U\cap V)\right\rangle}\tag{1}$$

must hold. In this post we treat this in a more general manner.

## Relative homology

To do so, we first need to generalize homology. For a space $$X$$ and any subspace $$A$$, we define the $$k$$-th relative chain group $$C_k(X,A)$$ as the quotient

$$C_k(X,A):=C_k(X)/C_k(A).$$

Then it is not difficult to see that the boundary map $$\partial_k:C_k(X) \rightarrow C_{k-1}(X)$$ induces a map $$C_k(X,A) \rightarrow C_{k-1}(X,A)$$ between the quotient groups. From this we obtain the following chain complex

$$\cdots \longrightarrow C_k(X,A)\overset{\partial}{\longrightarrow} C_{k-1}(X,A)\longrightarrow\cdots.$$

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> The $$k$$-th homology of the above chain complex, $$H_k(X,A)$$, is called *relative homology*.

</div>

Now consider the short exact sequence in the category $$\Ch_{\geq 0}(\Ab)$$

$$0 \rightarrow C_\bullet(A) \rightarrow C_\bullet(X) \rightarrow C_\bullet(X,A) \rightarrow 0.$$

Then by [\[Homological Algebra\] §Long Exact Sequence, ⁋Theorem 1](/en/math/homological_algebra/long_exact_sequence#thm1) we have the following long exact sequence

$$\cdots \rightarrow H_k(A) \rightarrow H_k(X) \rightarrow H_k(X,A)\rightarrow H_{k-1}(A) \rightarrow \cdots.$$

Here the connecting map $$H_k(X,A) \rightarrow H_{k-1}(A)$$ is simply the boundary map applied to any cycle (any representative thereof) in $$H_k(X,A)$$. Moreover, if a continuous map $$f:X \rightarrow Y$$ satisfies $$f(A)\subseteq B$$, then $$f$$ induces not only the original chain map $$C_\bullet(X)\rightarrow C_\bullet(Y)$$ but also $$C_\bullet(A) \rightarrow C_\bullet(B)$$, and from the fact that the following diagram

![relative_homology](/assets/images/Math/Algebraic_Topology/Computation_of_Homology-1.svg){:style="width:12.65em" class="invert" .align-center}

commutes, a chain map $$C_\bullet(X,A) \rightarrow C_\bullet(Y,B)$$ is also induced. That is, a map $$f:(X,A) \rightarrow (Y,B)$$ satisfying this condition also induces a map $$H_k(f):H_k(X,A) \rightarrow H_k(Y,B)$$ in homology. Then applying [§Homotopy, ⁋Proposition 6](/en/math/algebraic_topology/homotopy#prop6) to $$X$$ and $$A$$ respectively and using [\[Homological Algebra\] §Diagram Chasing, ⁋Corollary 2 (The five lemma)](/en/math/homological_algebra/diagram_chasing#cor2), we see that homotopic continuous functions $$f,g$$ satisfying this condition induce the same map in homology.

## Excision theorem

Intuitively, the relative homology $$H_\bullet(X,A)$$ of a pair $$(X,A)$$ is the homology of the chain complex $$C_\bullet(X,A)$$ corresponding to the cokernel of the inclusion $$C_\bullet(A)\hookrightarrow C_\bullet(X)$$. Since the information about $$C_\bullet(A)$$ disappears upon taking the quotient, it seems plausible that removing a subset contained in $$A$$ from the whole space would not change the relative homology. This is indeed true under the following mild condition.

<div class="proposition" markdown="1">

<ins id="thm2">**Theorem 2 (Excision theorem)**</ins> Let $$A$$ be a subspace of a space $$X$$, and let $$Z$$ be a subspace of $$A$$ satisfying $$\cl Z\subseteq \interior A$$. Then the inclusion

$$(X\setminus Z, A\setminus Z)\hookrightarrow (X,A)$$

induces an isomorphism

$$H_k(X\setminus Z, A\setminus Z)\rightarrow H_k(X,A).$$

</div>

However, compared with how intuitively obvious this theorem is, its proof involves somewhat technical details, so we omit it here.

On the other hand, in geometric situations we already know a way to ignore information contained in $$A$$ in this manner: namely, the quotient space $$X/A$$ obtained by collapsing $$A$$ to a point. Then it is a reasonable guess that there is a relationship between the homology $$H_k(X/A)$$ and the relative homology $$H_k(X,A)$$. Of course, as with the theorem above, this is possible only if $$A$$ is not too pathological a space.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> For a space $$X$$ and a subspace $$A$$, the pair $$(X,A)$$ is called a *good pair* if $$A$$ is a closed set and there exists a suitable open subset $$U$$ of $$X$$ such that $$A\subset U$$ and $$A$$ is a strong deformation retract of $$U$$.

</div>

Let a good pair $$(X,A)$$ be given, and let $$U$$ be an open set satisfying the hypothesis of [Definition 3](#def3). Then in the following diagram

![3*3_diagram](/assets/images/Math/Algebraic_Topology/Computation_of_Homology-2.svg){:style="width:27.21em" class="invert" .align-center}

each row is exact and the first two columns are also exact, so by [\[Homological Algebra\] §Diagram Chasing, ⁋Corollary 7](/en/math/homological_algebra/diagram_chasing#cor7) we obtain a short exact sequence of chain complexes

$$0\rightarrow C_\bullet(U,A)\rightarrow C_\bullet(X,A)\rightarrow C_\bullet(X,U)\rightarrow 0$$

and the resulting long exact sequence

$$\cdots \rightarrow H_k(U,A) \rightarrow H_k(X,A)\rightarrow H_k(X,U)\rightarrow H_{k-1}(U,A)\rightarrow \cdots.$$

But from the assumption that $$A$$ is a strong deformation retract of $$U$$, we have $$H_k(U,A)=0$$ for all $$k$$, and hence the isomorphism $$H_k(X,A)\cong H_k(X,U)$$ holds for all $$k$$.

On the other hand, for any closed subspace $$A$$, the quotient space $$X/A$$ obtained by collapsing $$A$$ to a point is well defined, and the projection $$X \rightarrow X/A$$ sends $$A$$ to a single point $$[A]$$ and is a homeomorphism outside $$A$$. Then, applying the same argument to the inclusions

$$\{[A]\}\subseteq U/A\subseteq X/A$$

we see that $$U/A$$ strongly deformation retracts onto the point $$[A]$$, so from $$H_k(U/A,[A])=0$$ we obtain the following isomorphism

$$H_k(X/A, [A])\cong H_k(X/A, U/A)$$

and these fit into the following diagram induced by the quotient map

![excision-1](/assets/images/Math/Algebraic_Topology/Computation_of_Homology-3.svg){:style="width:17.12em" class="invert" .align-center}

Now from the assumption that $$(X,A)$$ is a good pair, the inclusions $$A\subset U\subset X$$ satisfy the condition $$\cl A\subseteq \interior U$$ of [Theorem 2](#thm2), and hence the map $$H_k(X\setminus A, U\setminus A)\rightarrow H_k(X,U)$$ induced by the inclusion

$$(X\setminus A, U\setminus A)\hookrightarrow (X,U)$$

is an isomorphism; likewise, applying [Theorem 2](#thm2) to the inclusions $$\{[A]\}\subseteq U/A\subseteq X/A$$, we see that the map

$$H_k((X/A)\setminus [A], (U/A)\setminus [A])$$

is an isomorphism. These fit into the following diagram also induced by the quotient map

![excision-2](/assets/images/Math/Algebraic_Topology/Computation_of_Homology-4.svg){:style="width:24.44em" class="invert" .align-center}

and here the left vertical map $$H_k(X\setminus A, U\setminus A)\rightarrow H_k((X/A)\setminus [A], (U/A)\setminus [A])$$ is an isomorphism because the quotient map $$p:X\rightarrow X/A$$ is a homeomorphism outside $$A$$. Combining these results we obtain the following isomorphism

$$H_k(X,A)\cong H_k(X/A,[A])\tag{2}.$$

On the other hand, by [§Homology, ⁋Proposition 11](/en/math/algebraic_topology/homology#prop11) and [\[Homological Algebra\] §Diagram Chasing, ⁋Corollary 2 (The five lemma)](/en/math/homological_algebra/diagram_chasing#cor2), for any space $$X$$ and a point $$x\in X$$ the following long exact sequence

$$\begin{aligned}\cdots &\rightarrow H_k(x)\rightarrow H_k(X)\rightarrow H_k(X,x) \rightarrow H_{k-1}(x)\rightarrow\cdots \\\cdots&\rightarrow H_1(x)\rightarrow H_1(X) \rightarrow H_1(X,x) \rightarrow H_0(x) \rightarrow H_0(X)\rightarrow H_0(X,x)\rightarrow 0\end{aligned}$$

gives isomorphisms $$H_k(X)\cong H_k(X,x)$$ for all $$k>1$$. Moreover, looking at the long exact sequence for $$k=1$$,

$$0 \rightarrow H_1(X) \rightarrow H_1(X, x) \overset{\partial}{\longrightarrow} H_{0}(x) \overset{\iota_\ast}{\longrightarrow} H_{0}(X),$$

here $$\iota_\ast$$ sends the generator of $$H_0(x)$$ to the path component of $$X$$ containing $$x$$, so it is injective; hence $$\partial$$ is the zero map, and from this we likewise obtain the isomorphism $$H_1(X)\cong H_1(X,x)$$.

On the other hand, from the fact that $$\iota_\ast$$ is injective we obtain the following long exact sequence

$$0 \rightarrow H_0(x)\rightarrow H_0(X) \rightarrow H_0(X,x)\rightarrow 0,$$

and from this we get the isomorphism $$H_0(X,x)\cong H_0(X)/\mathbb{Z}$$. Geometrically this is the same as removing the path component of $$H_0(X)$$ containing $$x$$. For notational convenience, fixing a point $$x\in X$$ we define the *reduced homology* $$\widetilde{H}_k(X)$$ by

$$\widetilde{H}_k(X)=H_k(X,x);$$

then we can rewrite the right-hand side of the above isomorphism (2) as $$\widetilde{H}_k(X/A)$$, obtaining the following.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> For a good pair $$(X,A)$$, the quotient map $$X \rightarrow X/A$$ induces, for every $$k$$, the following isomorphism

$$H_k(X,A)\cong \widetilde{H}_k(X/A).$$

</div>

## Simplicial homology and singular homology

Now relative homology was defined by taking the cokernel of the monomorphism $$C_\bullet(A)\rightarrow C_\bullet(X)$$ in $$\Ch_{\geq 0}(\Ab)$$, so we can repeat this process for $$C^\Delta_\bullet(A) \rightarrow C^\Delta_\bullet(X)$$ as well. As a result we obtain the simplicial homology version of relative homology $$H_n^\Delta(X,A)$$. Now since simplicial homology consists of "non-singular" chains, the inclusion

$$C_\bullet^\Delta(X) \rightarrow C_\bullet(X)$$

induces a canonical homomorphism

$$H_\bullet^\Delta(X)\rightarrow H_\bullet(X)\tag{3}$$

and similarly the following canonical homomorphisms

$$H_\bullet^\Delta(A)\rightarrow H_\bullet(A),\qquad H_\bullet^\Delta(X,A)\rightarrow H_\bullet(X,A)$$

exist. Then by [\[Homological Algebra\] §Long Exact Sequence, ⁋Proposition 2](/en/math/homological_algebra/long_exact_sequence#prop2) these define the following commutative diagram

![functoriality](/assets/images/Math/Algebraic_Topology/Computation_of_Homology-5.svg){:style="width:35.64em" class="invert" .align-center}

Using this, the following holds.

<div class="proposition" markdown="1">

<ins id="thm5">**Theorem 5**</ins> For any $$\Delta$$-complex $$X$$, the homomorphism (3) is an isomorphism.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

We sketch the main idea. By the above commutative diagram, consider the filtration defined by the $$\Delta$$-complex structure of $$X$$

$$X_0\subset X_1\subset\cdots\subset X_l=X$$

and then apply [\[Homological Algebra\] §Diagram Chasing, ⁋Corollary 2](/en/math/homological_algebra/diagram_chasing#cor2) to the following diagram

![induction](/assets/images/Math/Algebraic_Topology/Computation_of_Homology-6.svg){:style="width:56.75em" class="invert" .align-center}

to run induction. For the induction step, it suffices to show that for any $$n$$ and any $$k$$ the homomorphism between relative homologies

$$H_n^\Delta(X^k, X^{k-1})\rightarrow H_n(X^k, X^{k-1})$$

is an isomorphism. Once this is assumed, by [§Homology, ⁋Proposition 11](/en/math/algebraic_topology/homology#prop11) we have $$H_n^\Delta(X^0)\cong H_n(X^0)$$ for all $$n$$ when $$k=1$$, so by [\[Homological Algebra\] §Diagram Chasing, ⁋Corollary 2](/en/math/homological_algebra/diagram_chasing#cor2) we can show $$H_n^\Delta(X^1)\cong H_n(X^1)$$, and then inductively obtain the desired isomorphism for larger $$k$$.

First, by definition $$C_\bullet^\Delta(X^k, X^{k-1})$$ is nontrivial only when $$n=k$$, and hence $$H_n^\Delta(X^k, X^{k-1})$$ is a nontrivial free abelian group (generated by the $$k$$-simplices) only when $$n=k$$, and trivial otherwise.

A similar result holds for singular homology: specifically, $$H_n(\Delta^k,\partial\Delta^k)$$ is a free abelian group only when $$n=k$$, and its generator is $$\id:\Delta^k \rightarrow \Delta^k$$. To verify this, define $$\Lambda$$ to be $$\Delta^k$$ with all but one of its $$(k-1)$$-dimensional faces removed, and look at the long exact sequence for $$(\Delta^k, \partial\Delta^k, \Lambda)$$

$$\cdots\rightarrow H_n(\Delta^k,\Lambda)\rightarrow H_n(\Delta^k, \partial\Delta^k)\rightarrow H_{n-1}(\partial\Delta^k, \Lambda)\rightarrow H_{n-1}(\Delta^k,\Lambda)\rightarrow \cdots;$$

the groups $$H_\bullet(\Delta^k,\Lambda)$$ are zero because $$\Delta^k$$ deformation retracts onto $$\Lambda$$, so $$H_k(\Delta^k, \partial\Delta^k)\cong H_{n-1}(\partial\Delta^k,\Lambda)$$, and on the other hand for the good pair $$(\partial\Delta^k,\Lambda)$$ the quotient space $$\partial\Delta^k/\Lambda$$ is homeomorphic to the quotient space $$\Delta^{k-1}/\partial\Delta^{k-1}$$, so using these we obtain

$$H_k(\Delta^k, \partial\Delta^{k})\cong H_{k-1}(\Delta^{k-1}, \partial\Delta^{k-1})$$

and hence the desired result follows inductively.

Looking at this process, we see that the generator of $$H_k(\Delta^k,\partial\Delta^k)$$ (as singular homology) is exactly the $$k$$-simplex $$\Delta^k$$ itself. Since the pair $$(X^k,X^{k-1})$$ is the union of such pairs $$(\Delta^k,\partial\Delta^k)$$, by [§Homology, ⁋Proposition 9](/en/math/algebraic_topology/homology#prop9) we obtain the desired result.

</details>

## Mayer–Vietoris sequence

Although we did not write out the proof for reasons of length, the excision theorem of [Theorem 2](#thm2) is extremely useful in homology theory. For example, in the proof of [Theorem 5](#thm5) we used the excision theorem to ignore simplices of dimension less than $$k-1$$, which allowed us to use induction; the base step of that induction was the homology of a one-point space. This process can be seen as essentially possessing all the properties that homology should satisfy, and axiomatizing this gives the following.

<div class="definition" markdown="1">

<ins id="def6">**Definition 6 (Eilenberg–Steenrod axioms)**</ins> For functors $$H_k$$ from the category of pairs of topological spaces to the category of abelian groups, and natural transformations

$$\partial:H_k(X,A)\rightarrow H_{k-1}(A,\emptyset):=H_{k-1}(A)$$

between them, the *Eilenberg–Steenrod axioms* mean the following axioms.

- (Homotopy) If two homotopic maps $$(X,A) \rightarrow (Y,B)$$ are given, then the two induced homomorphisms $$H_k(X,A) \rightarrow H_k(Y,B)$$ are identical.
- (Excision) For $$(X,A,Z)$$ satisfying the condition of [Theorem 2](#thm2), the inclusion $$(X\setminus Z, A\setminus Z)\hookrightarrow (X,A)$$ induces an isomorphism.
- (Dimension) For a one-point space $$\ast$$, we have $$H_k(\ast)=0$$ for all $$k>0$$.
- (Additivity) If $$X=\coprod X_\alpha$$, then $$H_k(X)\cong\bigoplus H_k(X_\alpha)$$.
- (Exactness) For each pair $$(X,A)$$, the two inclusions $$(A,\emptyset) \hookrightarrow (X,\emptyset)$$ and $$(X,\emptyset)\hookrightarrow (X,A)$$ fit into the following long exact sequence

    $$\cdots \rightarrow H_k(A)\rightarrow H_k(X) \rightarrow H_k(X,A) \rightarrow H_{k-1}(A)\rightarrow \cdots.$$

</div>

Then the result of Eilenberg and Steenrod shows that homology theories defined in this way are all naturally isomorphic, provided the *coefficient group* $$H_0(\ast)$$ is fixed. For example, we proved earlier that simplicial homology and singular homology agree on a $$\Delta$$-complex, and if we separate out the proof step by step we can verify that what we essentially used were the axioms of [Definition 6](#def6). For practical computation of homology it is convenient to introduce *cellular homology* defined on a *CW complex*; likewise this homology also satisfies the above axioms and therefore gives the same computation as simplicial homology and singular homology.

Now all these homology theories have the coefficient group fixed as $$\mathbb{Z}$$, but if we replace this by an arbitrary abelian group $$A$$, all the axioms of [Definition 6](#def6) still hold unchanged. Indeed, when defining singular homology or simplicial homology, if we had taken the chain groups

$$C^\Delta_\bullet(X),\qquad C_\bullet(X)$$

not as free abelian groups but as free $$A$$-modules

$$C^\Delta_\bullet(X;A):=C^\Delta_\bullet(X)\otimes_\mathbb{Z}A,\qquad C_\bullet(X;A):=C_\bullet(X)\otimes_\mathbb{Z}A$$

we would have obtained homology of this kind.

Most properties of homology follow from the axioms of [Definition 6](#def6). For example, we can derive the generalization of equation (1), which was the goal of this post, from them. Let a topological space $$X$$ be expressed as the union of two open sets $$X=U\cup V$$. Then taking homology of the following inclusions

![inclusions](/assets/images/Math/Algebraic_Topology/Computation_of_Homology-7.svg){:style="width:7.54em" class="invert" .align-center}

we obtain, by exactness, a morphism between long exact sequences, and here the inclusion

$$(V,U\cap V)\rightarrow (X,U)$$

induces an isomorphism in homology by the excision axiom, so the corresponding morphisms in the above are all isomorphisms. That is, we obtain the following morphism of long exact sequences

![morphism_of_les](/assets/images/Math/Algebraic_Topology/Computation_of_Homology-8.svg){:style="width:43.25em" class="invert" .align-center}

where $$i,j,k$$ are the maps induced by the respective inclusions, $$\partial$$ are the connecting maps, and $$p$$ are the cokernel morphisms. For convenience we have omitted the indices. Now let $$\alpha$$ denote this morphism of long exact sequences, and let $$\Cone(\alpha)$$ be the mapping cone exact sequence of $$\alpha$$

$$\begin{aligned}\cdots &\overset{\overline{\partial}}{\longrightarrow} H_{n+1}(X)\oplus H_{n+1}(V, U\cap V)\overset{\overline{\Phi}}{\longrightarrow} H_{n+1}(X,U)\oplus H_n(U\cap V)\overset{\overline{\Psi}}{\longrightarrow} H_n(U)\oplus H_n(V)\\ \phantom{\cdots}&\overset{\overline{\partial}}{\longrightarrow} H_n(X)\oplus H_n(V, U\cap V)\rightarrow \cdots.\end{aligned}$$

Then by the preceding consequence of the excision axiom, the following long exact sequence

$$\cdots \rightarrow 0 \rightarrow H_{n+1}(V, U\cap V)\rightarrow H_{n+1}(X,U)\rightarrow 0 \rightarrow \cdots\tag{4}$$

exists, and using this we see that $$\Cone(\alpha)$$ can be expressed as the direct sum of this trivial long exact sequence and the following long exact sequence

$$\cdots \rightarrow H_{n+1}(U)\oplus H_{n+1}(V)\rightarrow H_{n+1}(X)\rightarrow H_n(U\cap V)\rightarrow H_n(U)\oplus H_n(V)\rightarrow\cdots.\tag{5}$$

Since $$\Cone(\alpha)$$ and (4) are both exact, (5) is also exact, and the differential maps of the exact sequence (5) are obtained via the change of basis defined by the isomorphisms $$i_V$$ in the mapping cone exact sequence. Computing this explicitly gives the following.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7 (Mayer–Vietoris sequence)**</ins> Let a topological space $$X$$ be expressed as the union of two open sets $$X=U\cup V$$, and consider a homology theory $$H$$ defined on it. Then there exists a long exact sequence

$$\cdots \rightarrow H_{n+1}(U)\oplus H_{n+1}(V)\overset{\Psi}{\longrightarrow} H_{n+1}(X)\overset{\partial}{\longrightarrow} H_n(U\cap V)\overset{\Phi}{\longrightarrow} H_n(U)\oplus H_n(V)\rightarrow\cdots$$

where the maps $$\Psi, \Phi$$ are given by

$$\Psi(u,v)=u+v,\qquad \Phi(x)=(x,-x).$$

</div>

In particular, looking at the case $$n=1$$ we recover (1), which we initially obtained by transporting the Seifert–van Kampen theorem via abelianization, and in this sense the Mayer–Vietoris sequence can be thought of as the homology version of the Seifert–van Kampen theorem.

---

**References**

[Hat] A. Hatcher, *Algebraic Topology*. Cambridge University Press, 2022.  
[May] J. P. May, *A concise course in algebraic topology*.
