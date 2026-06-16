---
title: "Computation of Homology"
excerpt: "Practical computation of homology via relative homology and Mayer–Vietoris"

categories: [Math / Algebraic Topology]
permalink: /en/math/algebraic_topology/computation_of_homology
sidebar: 
    nav: "algebraic_topology-en"

date: 2026-03-12
weight: 5
translated_at: 2026-05-29T02:00:58+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-25T16:00:04+00:00
---
We now turn to tools for computing homology in practice. Computing the homology of an arbitrary space directly from the definition is essentially impossible, so we must develop methods for decomposing a large space into smaller pieces and recovering the homology of the whole from that of the parts. The most intuitive analogue is the Seifert–van Kampen theorem ([§Covering Spaces, ⁋Theorem 13](/en/math/algebraic_topology/covering_spaces#thm13)), where we observed that the functor $$\pi_1:\Top \rightarrow \Grp$$ preserves colimits. Now the abelianization functor $$\ab:\Grp \rightarrow \Ab$$ is the left adjoint of the forgetful functor $$U:\Ab \rightarrow \Grp$$ ([\[Algebraic Structures\] §Abelian Groups, ⁋Proposition 7](/en/math/algebraic_structures/abelian_groups#prop7)), and left adjoints preserve colimits ([\[Category Theory\] §Adjoint Functors, ⁋Theorem 9](/en/math/category_theory/adjoints#thm9)); hence the first homology functor $$H_1:\Top \rightarrow \Ab$$, being their composite ([§Covering Spaces, ⁋Theorem 15](/en/math/algebraic_topology/covering_spaces#thm15)), must also preserve colimits. In particular, as in [§Covering Spaces, ⁋Corollary 14](/en/math/algebraic_topology/covering_spaces#cor14), let a topological space $$X$$ be the union of two connected open subsets $$U,V$$. In the category $$\Ab$$, the pushout of two abelian groups is the coequalizer of their direct sum, so the isomorphism

$$H_1(X)=H_1(U\cup V)\cong \frac{H_1(U)\oplus H_1(V)}{\left\langle (f(x),-g(x))\mid x\in H_1(U\cap V)\right\rangle}\tag{1}$$

must hold. In this post we treat this in a more general setting.

## Relative homology

To do so, we first need a generalization of homology itself. For a space $$X$$ and an arbitrary subspace $$A$$, define the $$k$$-th relative chain group $$C_k(X,A)$$ as the quotient

$$C_k(X,A):=C_k(X)/C_k(A)$$

It is then straightforward to verify that the boundary map $$\partial_k:C_k(X) \rightarrow C_{k-1}(X)$$ induces a map $$C_k(X,A) \rightarrow C_{k-1}(X,A)$$ between the quotient groups. This yields the chain complex

$$\cdots \longrightarrow C_k(X,A)\overset{\partial}{\longrightarrow} C_{k-1}(X,A)\longrightarrow\cdots$$

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> The $$k$$-th homology $$H_k(X,A)$$ of the above chain complex is called the *relative homology*.

</div>

Now consider the short exact sequence in $$\Ch_{\geq 0}(\Ab)$$

$$0 \rightarrow C_\bullet(A) \rightarrow C_\bullet(X) \rightarrow C_\bullet(X,A) \rightarrow 0$$ 

By [\[Homological Algebra\] §The Long Exact Sequence, ⁋Theorem 1 (The long exact sequence)](/en/math/homological_algebra/long_exact_sequence#thm1), we obtain the long exact sequence

$$\cdots \rightarrow H_k(A) \rightarrow H_k(X) \rightarrow H_k(X,A)\rightarrow H_{k-1}(A) \rightarrow \cdots$$

Here the connecting map $$H_k(X,A) \rightarrow H_{k-1}(A)$$ is nothing more than the boundary map applied to any cycle (or any representative thereof) in $$H_k(X,A)$$. Moreover, if a continuous map $$f:X \rightarrow Y$$ satisfies $$f(A)\subseteq B$$, then $$f$$ induces not only the chain map $$C_\bullet(X)\rightarrow C_\bullet(Y)$$ but also $$C_\bullet(A) \rightarrow C_\bullet(B)$$, and from the commutativity of the diagram

![relative_homology](/assets/images/Math/Algebraic_Topology/Computation_of_Homology-1.svg){:style="width:12.65em" class="invert" .align-center}

we obtain an induced chain map $$C_\bullet(X,A) \rightarrow C_\bullet(Y,B)$$. Thus any $$f:(X,A) \rightarrow (Y,B)$$ satisfying these conditions induces a map $$H_k(f):H_k(X,A) \rightarrow H_k(Y,B)$$ in homology. Applying [§Homotopy, ⁋Proposition 6](/en/math/algebraic_topology/homotopy#prop6) to $$X$$ and $$A$$ separately and using [\[Homological Algebra\] §Diagram chasing, ⁋Corollary 2 (The five lemma)](/en/math/homological_algebra/diagram_chasing#cor2), we see that homotopic continuous maps $$f,g$$ satisfying this condition induce the same map in homology.

## Excision theorem

Intuitively, the relative homology $$H_\bullet(X,A)$$ of a pair $$(X,A)$$ is the homology of the chain complex $$C_\bullet(X,A)$$, which is the cokernel of the inclusion $$C_\bullet(A)\hookrightarrow C_\bullet(X)$$ in $$\Ch_{\geq 0}(\Ab)$$. Since information about $$C_\bullet(A)$$ is lost upon taking the quotient, one expects that removing a subset contained in $$A$$ should not change the relative homology. This is indeed true under the following mild hypothesis.

<div class="proposition" markdown="1">

<ins id="thm2">**Theorem 2 (Excision theorem)**</ins> Let $$A$$ be a subspace of a space $$X$$, and let $$Z$$ be a subspace of $$A$$ satisfying $$\cl Z\subseteq \interior A$$. Then the inclusion

$$(X\setminus Z, A\setminus Z)\hookrightarrow (X,A)$$

induces an isomorphism

$$H_k(X\setminus Z, A\setminus Z)\rightarrow H_k(X,A)$$

</div>

However, despite its intuitive plausibility, the proof of this theorem involves some technicalities, so we omit it here.

On the other hand, in geometric situations we already know a way to discard the information contained in $$A$$: the quotient space $$X/A$$ obtained by collapsing $$A$$ to a point. It is therefore reasonable to conjecture a relation between the homology $$H_k(X/A)$$ and the relative homology $$H_k(X,A)$$. As with the theorem above, this requires that $$A$$ not be too pathological.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> For a space $$X$$ and a subspace $$A$$, the pair $$(X,A)$$ is called a *good pair* if $$A$$ is closed and there exists an open set $$U$$ in $$X$$ such that $$A\subset U$$ and $$A$$ is a strong deformation retract of $$U$$.

</div>

Let $$(X,A)$$ be a good pair, and let $$U$$ be an open set satisfying the hypothesis of [Definition 3](#def3). In the diagram

![3*3_diagram](/assets/images/Math/Algebraic_Topology/Computation_of_Homology-2.svg){:style="width:27.21em" class="invert" .align-center}

each row is exact and the first two columns are exact as well; hence by [\[Homological Algebra\] §Diagram chasing, ⁋Corollary 7 (The 3×3 lemma)](/en/math/homological_algebra/diagram_chasing#cor7) we obtain a short exact sequence of chain complexes

$$0\rightarrow C_\bullet(U,A)\rightarrow C_\bullet(X,A)\rightarrow C_\bullet(X,U)\rightarrow 0$$

and the associated long exact sequence

$$\cdots \rightarrow H_k(U,A) \rightarrow H_k(X,A)\rightarrow H_k(X,U)\rightarrow H_{k-1}(U,A)\rightarrow \cdots$$

Since $$A$$ is a strong deformation retract of $$U$$, we have $$H_k(U,A)=0$$ for all $$k$$, and therefore $$H_k(X,A)\cong H_k(X,U)$$ for all $$k$$.

On the other hand, for any closed subspace $$A$$ the quotient space $$X/A$$ obtained by collapsing $$A$$ to a point is well defined, and the projection $$X \rightarrow X/A$$ sends $$A$$ to the single point $$[A]$$ and is a homeomorphism outside $$A$$. Applying the same argument to the inclusions

$$\{[A]\}\subseteq U/A\subseteq X/A$$

we see that since $$U/A$$ strong deformation retracts onto the point $$[A]$$, the fact that $$H_k(U/A,[A])=0$$ yields the isomorphism

$$H_k(X/A, [A])\cong H_k(X/A, U/A)$$

which fits into the following diagram induced by the quotient map

![excision-1](/assets/images/Math/Algebraic_Topology/Computation_of_Homology-3.svg){:style="width:17.12em" class="invert" .align-center}

Now, since $$(X,A)$$ is a good pair, the inclusions $$A\subset U\subset X$$ satisfy the condition $$\cl A\subseteq \interior U$$ of [Theorem 2](#thm2); hence the map $$H_k(X\setminus A, U\setminus A)\rightarrow H_k(X,U)$$ induced by the inclusion

$$(X\setminus A, U\setminus A)\hookrightarrow (X,U)$$

is an isomorphism. Similarly, applying [Theorem 2](#thm2) to the inclusions $$\{[A]\}\subseteq U/A\subseteq X/A$$, we see that the map

$$H_k((X/A)\setminus [A], (U/A)\setminus [A])$$

is an isomorphism. These also fit into the following diagram induced by the quotient map

![excision-2](/assets/images/Math/Algebraic_Topology/Computation_of_Homology-4.svg){:style="width:24.44em" class="invert" .align-center}

where the left-hand vertical map $$H_k(X\setminus A, U\setminus A)\rightarrow H_k((X/A)\setminus [A], (U/A)\setminus [A])$$ is an isomorphism because the quotient map $$p:X\rightarrow X/A$$ is a homeomorphism outside $$A$$. Combining these results, we obtain the isomorphism

$$H_k(X,A)\cong H_k(X/A,[A])\tag{2}$$

On the other hand, by [§Homology, ⁋Proposition 11](/en/math/algebraic_topology/homology#prop11) and [\[Homological Algebra\] §Diagram chasing, ⁋Corollary 2 (The five lemma)](/en/math/homological_algebra/diagram_chasing#cor2), for any space $$X$$ and a point $$x\in X$$ the long exact sequence

$$\begin{aligned}\cdots &\rightarrow H_k(x)\rightarrow H_k(X)\rightarrow H_k(X,x) \rightarrow H_{k-1}(x)\rightarrow\cdots \\\cdots&\rightarrow H_1(x)\rightarrow H_1(X) \rightarrow H_1(X,x) \rightarrow H_0(x) \rightarrow H_0(X)\rightarrow H_0(X,x)\rightarrow 0\end{aligned}$$

yields an isomorphism $$H_k(X)\cong H_k(X,x)$$ for all $$k>1$$. Moreover, examining the long exact sequence for $$k=1$$,

$$0 \rightarrow H_1(X) \rightarrow H_1(X, x) \overset{\partial}{\longrightarrow} H_{0}(x) \overset{\iota_\ast}{\longrightarrow} H_{0}(X)$$

we see that $$\iota_\ast$$ sends the generator of $$H_0(x)$$ to the path component of $$X$$ containing $$x$$, hence is injective; therefore $$\partial$$ is the zero map, and we obtain the same isomorphism $$H_1(X)\cong H_1(X,x)$$.

From the injectivity of $$\iota_\ast$$ we also obtain the short exact sequence

$$0 \rightarrow H_0(x)\rightarrow H_0(X) \rightarrow H_0(X,x)\rightarrow 0$$

and hence the isomorphism $$H_0(X,x)\cong H_0(X)/\mathbb{Z}$$. Geometrically, this amounts to removing the path component of $$H_0(X)$$ that contains $$x$$. For notational convenience, we define the *reduced homology* $$\widetilde{H}_k(X)$$ for a fixed $$x\in X$$ by

$$\widetilde{H}_k(X)=H_k(X,x)$$

Then the right-hand side of isomorphism (2) can be replaced by $$\widetilde{H}_k(X/A)$$, giving the following statement.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> For a good pair $$(X,A)$$, the quotient map $$X \rightarrow X/A$$ induces an isomorphism

$$H_k(X,A)\cong \widetilde{H}_k(X/A)$$

for every $$k$$.

</div>

## Simplicial homology and singular homology

Since relative homology was defined by taking the cokernel of the monomorphism $$C_\bullet(A)\rightarrow C_\bullet(X)$$ in $$\Ch_{\geq 0}(\Ab)$$, the same procedure can be carried out for $$C^\Delta_\bullet(A) \rightarrow C^\Delta_\bullet(X)$$. The result is the simplicial-homology version of relative homology, denoted $$H_n^\Delta(X,A)$$. Because simplicial homology uses "non-singular" chains, the inclusion

$$C_\bullet^\Delta(X) \rightarrow C_\bullet(X)$$

induces a canonical homomorphism

$$H_\bullet^\Delta(X)\rightarrow H_\bullet(X)\tag{3}$$

and similarly we have canonical homomorphisms

$$H_\bullet^\Delta(A)\rightarrow H_\bullet^\Delta(A),\qquad H_\bullet^\Delta(X,A)\rightarrow H_\bullet(X,A)$$

By [\[Homological Algebra\] §The Long Exact Sequence, ⁋Proposition 2](/en/math/homological_algebra/long_exact_sequence#prop2), these fit into the commutative diagram

![functoriality](/assets/images/Math/Algebraic_Topology/Computation_of_Homology-5.svg){:style="width:35.64em" class="invert" .align-center}

Using this, we obtain the following.

<div class="proposition" markdown="1">

<ins id="thm5">**Theorem 5**</ins> For any $$\Delta$$-complex $$X$$, the homomorphism in (3) is an isomorphism.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

We sketch the overall strategy. Using the commutative diagram above, consider the filtration

$$X_0\subset X_1\subset\cdots\subset X_l=X$$

defined by the $$\Delta$$-complex structure on $$X$$, and apply [\[Homological Algebra\] §Diagram chasing, ⁋Corollary 2 (The five lemma)](/en/math/homological_algebra/diagram_chasing#cor2) to the diagram

![induction](/assets/images/Math/Algebraic_Topology/Computation_of_Homology-6.svg){:style="width:56.75em" class="invert" .align-center}

to run an induction. For the induction step, it suffices to show that for every $$n$$ and every $$k$$, the homomorphism between relative homologies

$$H_n^\Delta(X^k, X^{k-1})\rightarrow H_n(X^k, X^{k-1})$$

is an isomorphism. Once this is assumed, [§Homology, ⁋Proposition 10](/en/math/algebraic_topology/homology#prop10) gives $$H_n^\Delta(X^0)\cong H_n(X^0)$$ for all $$n$$ when $$k=1$$; then by [\[Homological Algebra\] §Diagram chasing, ⁋Corollary 2 (The five lemma)](/en/math/homological_algebra/diagram_chasing#cor2) we obtain $$H_n^\Delta(X^1)\cong H_n(X^1)$$, and inductively we construct the desired isomorphism for larger $$k$$.

First, by definition $$C_\bullet^\Delta(X^k, X^{k-1})$$ is nontrivial only when $$n=k$$; hence $$H_n^\Delta(X^k, X^{k-1})$$ is a nontrivial free abelian group (generated by the $$k$$-simplices) only when $$n=k$$, and is trivial otherwise.

A similar result holds for singular homology: specifically, $$H_n(\Delta^k,\partial\Delta^k)$$ is a free abelian group only when $$n=k$$, and its generator is $$\id:\Delta^k \rightarrow \Delta^k$$. To verify this, let $$\Lambda$$ be obtained from $$\Delta^k$$ by removing one of its $$(k-1)$$-dimensional faces, and consider the long exact sequence for the triple $$(\Delta^k, \partial\Delta^k, \Lambda)$$

$$\cdots\rightarrow H_n(\Delta^k,\Lambda)\rightarrow H_n(\Delta^k, \partial\Delta^k)\rightarrow H_{n-1}(\partial\Delta^k, \Lambda)\rightarrow H_{n-1}(\Delta^k,\Lambda)\rightarrow \cdots$$

Since $$\Delta^k$$ deformation retracts onto $$\Lambda$$, we have $$H_\bullet(\Delta^k,\Lambda)=0$$, and therefore $$H_k(\Delta^k, \partial\Delta^k)\cong H_{n-1}{\partial\Delta^k,\Lambda}$$; moreover, for the good pair $$(\partial\Delta^k,\Lambda)$$ the quotient space $$\partial\Delta^k/\Lambda$$ is homeomorphic to $$\Delta^{k-1}/\partial\Delta^{k-1}$$. Using these facts we obtain

$$H_k(\Delta^k, \partial\Delta^{k})\cong H_{k-1}(\Delta^{k-1}, \partial\Delta^{k-1})$$

and the desired result follows inductively.

Examining this process, we see that the generator of $$H_k(\Delta^k,\partial\Delta^k)$$ in singular homology is exactly the $$k$$-simplex $$\Delta^k$$ itself. Since the pair $$(X^k,X^{k-1})$$ is a union of such pairs $$(\Delta^k,\partial\Delta^k)$$, [§Homology, ⁋Proposition 9](/en/math/algebraic_topology/homology#prop9) yields the desired conclusion.

</details>

## Mayer–Vietoris sequence

Although we have omitted the proof for reasons of length, the excision theorem [Theorem 2](#thm2) is a powerful tool in homology theory. For instance, in the proof of [Theorem 5](#thm5) we used excision to ignore simplices of dimension less than $$k-1$$, which made an inductive argument possible with the homology of a one-point space as the base case. This process essentially exhibits all the properties that homology ought to satisfy; axiomatizing them leads to the following.

<div class="definition" markdown="1">

<ins id="def6">**Definition 6 (Eilenberg–Steenrod axioms)**</ins> Let $$H_k$$ be functors from the category of pairs of topological spaces to the category of abelian groups, and let

$$\partial:H_k(X,A)\rightarrow H_{k-1}(A,\emptyset):=H_{k-1}(A)$$

be natural transformations. The *Eilenberg–Steenrod axioms* are the following.

- (Homotopy) If two maps $$(X,A) \rightarrow (Y,B)$$ are homotopic, then the two induced homomorphisms $$H_k(X,A) \rightarrow H_k(Y,B)$$ coincide.
- (Excision) For $$(X,A,Z)$$ satisfying the conditions of [Theorem 2](#thm2), the inclusion $$(X\setminus Z, A\setminus Z)\hookrightarrow (X,A)$$ induces an isomorphism.
- (Dimension) For a one-point space $$\ast$$, we have $$H_k(\ast)=0$$ for all $$k>0$$.
- (Additivity) If $$X=\coprod X_\alpha$$, then $$H_k(X)\cong\bigoplus H_k(X_\alpha)$$.
- (Exactness) For each pair $$(X,A)$$, the two inclusions $$(A,\emptyset) \hookrightarrow (X,\emptyset)$$ and $$(X,\emptyset)\hookrightarrow (X,A)$$ fit into the long exact sequence
    
    $$\cdots \rightarrow H_k(A)\rightarrow H_k(X) \rightarrow H_k(X,A) \rightarrow H_{k-1}(A)\rightarrow \cdots$$

</div>

Eilenberg and Steenrod proved that any homology theory defined in this way is naturally isomorphic to any other, provided the *coefficient group* $$H_0(\ast)$$ is fixed. For example, we previously proved that simplicial and singular homology agree on $$\Delta$$-complexes; inspecting that proof step by step, one verifies that what we used were precisely the axioms of [Definition 6](#def6). For practical computations it is convenient to introduce *cellular homology* on *CW complexes*; this homology also satisfies the above axioms, and therefore yields the same calculations as simplicial and singular homology.

All these homology theories have coefficient group $$\mathbb{Z}$$; however, replacing $$\mathbb{Z}$$ by an arbitrary abelian group $$A$$ leaves every axiom in [Definition 6](#def6) intact. Indeed, had we defined singular or simplicial homology using not free abelian groups

$$C^\Delta_\bullet(X),\qquad C_\bullet(X)$$

but free $$A$$-modules

$$C^\Delta_\bullet(X;A):=C^\Delta_\bullet(X)\otimes_\mathbb{Z}A,\qquad C_\bullet(X;A):=C_\bullet(X)\otimes_\mathbb{Z}A$$

we would have obtained exactly this kind of homology theory.

Most properties of homology follow from the axioms in [Definition 6](#def6). For example, the generalization of equation (1), which is the goal of this post, can be derived from them. Let a topological space $$X$$ be the union of two open sets $$X=U\cup V$$. Applying homology to the inclusions

![inclusions](/assets/images/Math/Algebraic_Topology/Computation_of_Homology-7.svg){:style="width:7.54em" class="invert" .align-center}

we obtain, by exactness, a morphism between long exact sequences; here the inclusion

$$(V,U\cap V)\rightarrow (X,U)$$

induces an isomorphism in homology by the excision axiom, so all corresponding components in the above morphism are isomorphisms. That is, we obtain the following morphism of long exact sequences

![morphism_of_les](/assets/images/Math/Algebraic_Topology/Computation_of_Homology-8.svg){:style="width:43.25em" class="invert" .align-center}

Here $$i,j,k$$ are the maps induced by the respective inclusions, $$\partial$$ are connecting maps, and $$p$$ are cokernel morphisms; indices are omitted for convenience. Denote this morphism of long exact sequences by $$\alpha$$, and let $$\Cone(\alpha)$$ be its mapping-cone exact sequence

$$\begin{aligned}\cdots &\overset{\overline{\partial}}{\longrightarrow} H_{n+1}(X)\oplus H_{n+1}(V, U\cap V)\overset{\overline{\Phi}}{\longrightarrow} H_{n+1}(X,U)\oplus H_n(U\cap V)\overset{\overline{\Psi}}{\longrightarrow} H_n(U)\oplus H_n(V)\\ \phantom{\cdots}&\overset{\overline{\partial}}{\longrightarrow} H_n(X)\oplus H_n(V, U\cap V)\rightarrow \cdots\end{aligned}$$

By the excision result above, the long exact sequence

$$\cdots \rightarrow 0 \rightarrow H_{n+1}(V, U\cap V)\rightarrow H_{n+1}(X,U)\rightarrow 0 \rightarrow \cdots\tag{4}$$

exists, and using this we can express $$\Cone(\alpha)$$ as the direct sum of this trivial long exact sequence and the long exact sequence

$$\cdots \rightarrow H_{n+1}(U)\oplus H_{n+1}(V)\rightarrow H_{n+1}(X)\rightarrow H_n(U\cap V)\rightarrow H_n(U)\oplus H_n(V)\rightarrow\cdots\tag{5}$$

Since both $$\Cone(\alpha)$$ and (4) are exact, (5) is exact as well; the differential maps of (5) are obtained from the mapping-cone exact sequence by the change of basis determined by the isomorphisms $$i_V$$. Carrying out this computation explicitly yields the following.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7 (Mayer–Vietoris sequence)**</ins> Let a topological space $$X$$ be the union of two open sets $$X=U\cup V$$, and let $$H$$ be a homology theory on $$X$$. Then there is a long exact sequence

$$\cdots \rightarrow H_{n+1}(U)\oplus H_{n+1}(V)\overset{\Psi}{\longrightarrow} H_{n+1}(X)\overset{\partial}{\longrightarrow} H_n(U\cap V)\overset{\Phi}{\longrightarrow} H_n(U)\oplus H_n(V)\rightarrow\cdots$$

where the maps $$\Psi, \Phi$$ are given by

$$\Psi(u,v)=u+v,\qquad \Phi(x)=(x,-x)$$

</div>

In particular, for $$n=1$$ we recover equation (1), which we obtained at the outset by abelianizing the Seifert–van Kampen theorem; in this sense the Mayer–Vietoris sequence may be regarded as the homology analogue of the Seifert–van Kampen theorem.

--- 

**References**

[Hat] A. Hatcher, *Algebraic Topology*. Cambridge University Press, 2022.  
[May] J. P. May, *A concise course in algebraic topology*.

---
