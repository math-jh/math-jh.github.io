---

title: "Computation of Homology"
excerpt: ""

categories: [Math / Algebraic Topology]
permalink: /en/math/algebraic_topology/computation_of_homology
header:
    overlay_image: /assets/images/Math/Algebraic_Topology/Computation_of_homology.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_topology-en"

date: 2026-03-12
last_modified_at: 2026-03-12
weight: 5

---

We now explore tools for computing homology in practice. Since directly computing the homology of an arbitrary space from its definition is nearly impossible, we need to develop tools for breaking large spaces into smaller pieces and computing the homology of the large space from the homology of the smaller ones. The most intuitive situation would be that of the Seifert-van Kampen theorem ([§Covering Spaces, ⁋Theorem 13](/en/math/algebraic_topology/covering_spaces#thm13)), where we observed that the functor $$\pi_1:\Top \rightarrow \Grp$$ preserves colimits. However, the abelianization functor $$\ab:\Grp \rightarrow \Ab$$ is the left adjoint of the forgetful functor $$U:\Ab \rightarrow \Grp$$ ([\[Algebraic Structures\] §Abelian Groups, ⁋Proposition 7](/en/math/algebraic_structures/abelian_groups#prop7)), and left adjoint functors preserve colimits ([\[Category Theory\] §Adjoint Functors, ⁋Theorem 9](/en/math/category_theory/adjoints#thm9)), so the first homology functor $$H_1:\Top \rightarrow \Ab$$, being their composition ([§Covering Spaces, ⁋Theorem 15](/en/math/algebraic_topology/covering_spaces#thm15)), should also preserve colimits. In particular, as in [§Covering Spaces, ⁋Corollary 14](/en/math/algebraic_topology/covering_spaces#cor14), suppose a topological space $$X$$ is expressed as the union of two connected open subsets $$U,V$$. Then in the category $$\Ab$$, since the pushout of two abelian groups is given as the coequalizer of their direct sum, the following isomorphism

$$H_1(X)=H_1(U\cup V)\cong \frac{H_1(U)\oplus H_1(V)}{\left\langle (f(x),-g(x))\mid x\in H_1(U\cap V)\right\rangle}\tag{1}$$

should hold. In this article, we will treat this in a more general way.

## Relative homology

For this, we first need to generalize homology. For a space $$X$$ and an arbitrary subspace $$A$$, let us define the $$k$$-th relative chain group $$C_k(X,A)$$ as the quotient

$$C_k(X,A):=C_k(X)/C_k(A)$$

It is then not difficult to see that the boundary map $$\partial_k:C_k(X) \rightarrow C_{k-1}(X)$$ induces a map $$C_k(X,A) \rightarrow C_{k-1}(X,A)$$ between quotient groups. From this, we can construct the following chain complex

$$\cdots \longrightarrow C_k(X,A)\overset{\partial}{\longrightarrow} C_{k-1}(X,A)\longrightarrow\cdots$$

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> The $$k$$-th homology $$H_k(X,A)$$ of the above chain complex is called the *relative homology*.

</div>

Now consider the short exact sequence in the category $$\Ch_{\geq 0}(\Ab)$$

$$0 \rightarrow C_\bullet(A) \rightarrow C_\bullet(X) \rightarrow C_\bullet(X,A) \rightarrow 0$$ 

Then by [\[Homological Algebra\] §Long Exact Sequences, ⁋Theorem 1](/en/math/homological_algebra/long_exact_sequence#thm1), the following long exact sequence exists

$$\cdots \rightarrow H_k(A) \rightarrow H_k(X) \rightarrow H_k(X,A)\rightarrow H_{k-1}(A) \rightarrow \cdots$$

Here, the connecting map $$H_k(X,A) \rightarrow H_{k-1}(A)$$ is simply the boundary map applied to any cycle (or any representative thereof) in $$H_k(X,A)$$. Moreover, if a continuous map $$f:X \rightarrow Y$$ satisfies $$f(A)\subseteq B$$, then $$f$$ induces not only the existing chain map $$C_\bullet(X)\rightarrow C_\bullet(Y)$$ but also $$C_\bullet(A) \rightarrow C_\bullet(B)$$, and from the fact that the following diagram

![relative_homology](/assets/images/Math/Algebraic_Topology/Computation_of_homology-1.png){:style="width:12em" class="invert" .align-center}

commutes, a chain map $$C_\bullet(X,A) \rightarrow C_\bullet(Y,B)$$ is also induced. That is, $$f:(X,A) \rightarrow (Y,B)$$ satisfying such conditions also induces a map $$H_k(f):H_k(X,A) \rightarrow H_k(Y,B)$$ in homology. Then by applying [§Homotopy, ⁋Proposition 6](/en/math/algebraic_topology/homotopy#prop6) to $$X$$ and $$A$$ separately and using [\[Homological Algebra\] §Diagram Chasing, ⁋Corollary 2](/en/math/homological_algebra/diagram_chasing#cor2), we can see that homotopic continuous functions $$f,g$$ satisfying this condition induce the same map in homology.

## Excision theorem

Intuitively, the relative homology $$H_\bullet(X,A)$$ for $$(X,A)$$ is the homology of the chain complex $$C_\bullet(X,A)$$, which corresponds to the cokernel of the inclusion $$C_\bullet(A)\hookrightarrow C_\bullet(X)$$ in $$\Ch_{\geq 0}(\Ab)$$. Intuitively, since information about $$C_\bullet(A)$$ disappears through taking the quotient in this process, it seems plausible that the relative homology would not change if we subtract a subset contained in $$A$$ from the whole. This is true under the following mild conditions.

<div class="proposition" markdown="1">

<ins id="thm2">**Theorem 2 (Excision theorem)**</ins> Let $$A$$ be a subspace of a space $$X$$, and let $$Z$$ be a subspace of $$A$$ satisfying $$\cl Z\subseteq \interior A$$. Then the map

$$H_k(X\setminus Z, A\setminus Z)\rightarrow H_k(X,A)$$

induced by the inclusion

$$(X\setminus Z, A\setminus Z)\hookrightarrow (X,A)$$

is an isomorphism.

</div>

However, while this theorem may seem intuitively obvious, its proof involves some technical aspects, so we will omit the proof here.

On the other hand, we know of a way to ignore information contained in $$A$$ in geometric settings. That is, the quotient space $$X/A$$ obtained by collapsing $$A$$ to a single point. It is then a reasonable conjecture that there is a relationship between the homology $$H_k(X/A)$$ and the relative homology $$H_k(X,A)$$. Of course, as with the theorem above, this requires that $$A$$ is not a pathological space.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> For a space $$X$$ and a subspace $$A$$, the pair $$(X,A)$$ is called a *good pair* if $$A$$ is closed and there exists an open set $$U$$ of $$X$$ such that $$A\subset U$$ and $$A$$ is a strong deformation retract of $$U$$.

</div>

Let $$(X,A)$$ be a good pair, and let $$U$$ be an open set satisfying the assumption of [Definition 3](#def3). Then in the following diagram

![3*3_diagram](/assets/images/Math/Algebraic_Topology/Computation_of_homology-2.png){:style="width:26em" class="invert" .align-center}

each row is exact and the first two columns are also exact, so by [\[Homological Algebra\] §Diagram Chasing, ⁋Corollary 7](/en/math/homological_algebra/diagram_chasing#cor7), we obtain a short exact sequence of chain complexes

$$0\rightarrow C_\bullet(U,A)\rightarrow C_\bullet(X,A)\rightarrow C_\bullet(X,U)\rightarrow 0$$

and the long exact sequence derived from it

$$\cdots \rightarrow H_k(U,A) \rightarrow H_k(X,A)\rightarrow H_k(X,U)\rightarrow H_{k-1}(U,A)\rightarrow \cdots$$

However, from the assumption that $$A$$ is a strong deformation retract of $$U$$, we have $$H_k(U,A)=0$$ for all $$k$$, and therefore the isomorphism $$H_k(X,A)\cong H_k(X,U)$$ holds for all $$k$$.

On the other hand, for any closed subspace $$A$$, the quotient space $$X/A$$ obtained by collapsing $$A$$ to a point is well-defined, and the projection $$X \rightarrow X/A$$ is a function that sends $$A$$ to a single point $$[A]$$ and is a homeomorphism outside of $$A$$. In this case, applying the same argument to the inclusion

$$\{[A]\}\subseteq U/A\subseteq X/A$$

we see that since $$U/A$$ strong deformation retracts to a single point $$[A]$$, from $$H_k(U/A,[A])=0$$ we obtain the following isomorphism

$$H_k(X/A, [A])\cong H_k(X/A, U/A)$$

which can be placed in the following diagram induced by the quotient map

![excision-1](/assets/images/Math/Algebraic_Topology/Computation_of_homology-3.png){:style="width:16em" class="invert" .align-center}

Now, from the assumption that $$(X,A)$$ is a good pair, $$A\subset U\subset X$$ satisfies the condition $$\cl A\subseteq \interior U$$ of [Theorem 2](#thm2), and therefore the map $$H_k(X\setminus A, U\setminus A)\rightarrow H_k(X,U)$$ induced by the inclusion

$$(X\setminus A, U\setminus A)\hookrightarrow (X,U)$$

is an isomorphism. Similarly, applying [Theorem 2](#thm2) to the inclusion $$\{[A]\}\subseteq U/A\subseteq X/A$$, we see that the following map

$$H_k((X/A)\setminus [A], (U/A)\setminus [A])$$

is an isomorphism. These also fit into the following diagram induced by the quotient map

![excision-2](/assets/images/Math/Algebraic_Topology/Computation_of_homology-4.png){:style="width:24em" class="invert" .align-center}

where the left vertical map $$H_k(X\setminus A, U\setminus A)\rightarrow H_k((X/A)\setminus [A], (U/A)\setminus [A])$$ is an isomorphism due to the assumption that the quotient map $$p:X\rightarrow X/A$$ is a homeomorphism outside of $$A$$. Combining these results, we obtain the following isomorphism

$$H_k(X,A)\cong H_k(X/A,[A])\tag{2}$$

On the other hand, by [§Homology, ⁋Proposition 11](/en/math/algebraic_topology/homology#prop11) and [\[Homological Algebra\] §Diagram Chasing, ⁋Corollary 2](/en/math/homological_algebra/diagram_chasing#cor2), for any space $$X$$ and a point $$x\in X$$, the following long exact sequence

$$\begin{aligned}\cdots &\rightarrow H_k(x)\rightarrow H_k(X)\rightarrow H_k(X,x) \rightarrow H_{k-1}(x)\rightarrow\cdots \\\cdots&\rightarrow H_1(x)\rightarrow H_1(X) \rightarrow H_1(X,x) \rightarrow H_0(x) \rightarrow H_0(X)\rightarrow H_0(X,x)\rightarrow 0\end{aligned}$$

gives an isomorphism $$H_k(X)\cong H_k(X,x)$$ for all $$k>1$$. Moreover, looking at the long exact sequence for $$k=1$$

$$0 \rightarrow H_1(X) \rightarrow H_1(X, x) \overset{\partial}{\longrightarrow} H_{0}(x) \overset{\iota_\ast}{\longrightarrow} H_{0}(X)$$

the map $$\iota_\ast$$ sends the generator of $$H_0(x)$$ to the path component of $$X$$ containing $$x$$, so it is injective, and therefore $$\partial$$ is the zero map, yielding the same isomorphism $$H_1(X)\cong H_1(X,x)$$.

On the other hand, from the fact that $$\iota_\ast$$ is injective, we obtain the following long exact sequence

$$0 \rightarrow H_0(x)\rightarrow H_0(X) \rightarrow H_0(X,x)\rightarrow 0$$

from which we obtain the isomorphism $$H_0(X,x)\cong H_0(X)/\mathbb{Z}$$. Geometrically, this corresponds to removing the path component of $$H_0(X)$$ that contains $$x$$. For notational convenience, we define the *reduced homology* $$\widetilde{H}_k(X)$$ for a fixed $$x\in X$$ by

$$\widetilde{H}_k(X)=H_k(X,x)$$

Then the right-hand side of the isomorphism (2) above can be replaced with $$\widetilde{H}_k(X/A)$$ and written as follows.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> For a good pair $$(X,A)$$, the quotient map $$X \rightarrow X/A$$ induces an isomorphism

$$H_k(X,A)\cong \widetilde{H}_k(X/A)$$

for all $$k$$.

</div>

## Simplicial Homology and Singular Homology

On the other hand, since the way we defined relative homology was by taking the cokernel of a monomorphism $$C_\bullet(A)\rightarrow C_\bullet(X)$$ in $$\Ch_{\geq 0}(\Ab)$$, this process can be repeated for $$C^\Delta_\bullet(A) \rightarrow C^\Delta_\bullet(X)$$. As a result, we obtain the simplicial homology version of relative homology $$H_n^\Delta(X,A)$$. Now, since simplicial homology consists of "non-singular" chains, there exists a canonical homomorphism

$$H_\bullet^\Delta(X)\rightarrow H_\bullet(X)\tag{3}$$

induced by the inclusion

$$C_\bullet^\Delta(X) \rightarrow C_\bullet(X)$$

and similarly, the following canonical homomorphisms

$$H_\bullet^\Delta(A)\rightarrow H_\bullet^\Delta(A),\qquad H_\bullet^\Delta(X,A)\rightarrow H_\bullet(X,A)$$

exist. By [\[Homological Algebra\] §Long Exact Sequences, ⁋Proposition 2](/en/math/homological_algebra/long_exact_sequence#prop2), these define the following commutative diagram

![functoriality](/assets/images/Math/Algebraic_Topology/Computation_of_homology-5.png){:style="width:48em" class="invert" .align-center}

Using this, we obtain the following.

<div class="proposition" markdown="1">

<ins id="thm5">**Theorem 5**</ins> For any $$\Delta$$-complex $$X$$, the homomorphism in (3) is an isomorphism.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

We describe the general outline. By the commutative diagram above, consider the filtration

$$X_0\subset X_1\subset\cdots\subset X_l=X$$

defined by the $$\Delta$$-complex structure of $$X$$, and then apply [\[Homological Algebra\] §Diagram Chasing, ⁋Corollary 2](/en/math/homological_algebra/diagram_chasing#cor2) to the following diagram

![induction](/assets/images/Math/Algebraic_Topology/Computation_of_homology-6.png){:style="width:56em" class="invert" .align-center}

to run an induction. For the induction, it suffices to show that for any $$n$$ and any $$k$$, the homomorphism between relative homologies

$$H_n^\Delta(X^k, X^{k-1})\rightarrow H_n(X^k, X^{k-1})$$

is an isomorphism. Assuming this, first by [§Homology, ⁋Proposition 10](/en/math/algebraic_topology/homology#prop10), $$H_n^\Delta(X^0)\cong H_n(X^0)$$ holds for all $$n$$ when $$k=1$$, so by [\[Homological Algebra\] §Diagram Chasing, ⁋Corollary 2](/en/math/homological_algebra/diagram_chasing#cor2), we can show that $$H_n^\Delta(X^1)\cong H_n(X^1)$$, and from this, we can inductively construct the desired isomorphism for larger $$k$$.

First, by definition, $$C_\bullet^\Delta(X^k, X^{k-1})$$ is nontrivial only when $$n=k$$, and therefore $$H_n^\Delta(X^k, X^{k-1})$$ is a nontrivial free abelian group (generated by $$k$$-simplices) only when $$n=k$$, and is trivial in all other cases.

A similar result holds for singular homology: specifically, $$H_n(\Delta^k,\partial\Delta^k)$$ is a free abelian group only when $$n=k$$, and its generator is $$\id:\Delta^k \rightarrow \Delta^k$$. To verify this, let $$\Lambda$$ be defined by removing one of the $$(k-1)$$-dimensional faces of $$\Delta^k$$, and look at the long exact sequence corresponding to $$(\Delta^k, \partial\Delta^k, \Lambda)$$

$$\cdots\rightarrow H_n(\Delta^k,\Lambda)\rightarrow H_n(\Delta^k, \partial\Delta^k)\rightarrow H_{n-1}(\partial\Delta^k, \Lambda)\rightarrow H_{n-1}(\Delta^k,\Lambda)\rightarrow \cdots$$

Since $$H_\bullet(\Delta^k,\Lambda)=0$$ as $$\Delta^k$$ deformation retracts to $$\Lambda$$, we have $$H_k(\Delta^k, \partial\Delta^k)\cong H_{n-1}{\partial\Delta^k,\Lambda}$$, and since the quotient space $$\partial\Delta^k/\Lambda$$ is homeomorphic to the quotient space $$\Delta^{k-1}/\partial\Delta^{k-1}$$ for the good pair $$(\partial\Delta^k,\Lambda)$$, using these we obtain

$$H_k(\Delta^k, \partial\Delta^{k})\cong H_{k-1}(\Delta^{k-1}, \partial\Delta^{k-1})$$

and thus we can show the desired result inductively.

Examining this process, we see that the generator of $$H_k(\Delta^k,\partial\Delta^k)$$ (as singular homology) is exactly the $$k$$-simplex $$\Delta^k$$. Since the pair $$(X^k,X^{k-1})$$ is a union of such pairs $$(\Delta^k,\partial\Delta^k)$$, by [§Homology, ⁋Proposition 9](/en/math/algebraic_topology/homology#prop9), we obtain the desired result.

</details>

## Mayer-Vietoris Sequence

Although we have not written the proof due to length, the excision theorem [Theorem 2](#thm2) is useful when dealing with homology theory. For example, in the proof of [Theorem 5](#thm5), we used the excision theorem to ignore simplices of dimension less than $$k-1$$, which allowed us to use induction where the base step was the homology of a one-point space. This process essentially possesses all the properties that homology should satisfy, and axiomatizing this gives the following.

<div class="definition" markdown="1">

<ins id="def6">**Definition 6 (Eilenberg-Steenrod axioms)**</ins> For functors $$H_k$$ from the category of pairs of topological spaces to the category of abelian groups, and natural transformations between them

$$\partial:H_k(X,A)\rightarrow H_{k-1}(A,\emptyset):=H_{k-1}(A)$$

the *Eilenberg-Steenrod axioms* refer to the following axioms.

- (Homotopy) If two homotopic maps $$(X,A) \rightarrow (Y,B)$$ are given, the two homomorphisms $$H_k(X,A) \rightarrow H_k(Y,B)$$ they induce are identical.
- (Excision) For $$(X,A,Z)$$ satisfying the conditions of [Theorem 2](#thm2), $$(X\setminus Z, A\setminus Z)\hookrightarrow (X,A)$$ induces an isomorphism.
- (Dimension) For a one-point space $$\ast$$, $$H_k(\ast)=0$$ holds for all $$k>0$$.
- (Additivity) If $$X=\coprod X_\alpha$$, then $$H_k(X)\cong\bigoplus H_k(X_\alpha)$$.
- (Exactness) For each pair $$(X,A)$$ and the two inclusions $$(A,\emptyset) \hookrightarrow (X,\emptyset)$$ and $$(X,\emptyset)\hookrightarrow (X,A)$$, they fit into the following long exact sequence
    
    $$\cdots \rightarrow H_k(A)\rightarrow H_k(X) \rightarrow H_k(X,A) \rightarrow H_{k-1}(A)\rightarrow \cdots$$

</div>

The result of Eilenberg and Steenrod shows that homology theories defined in this way, if the *coefficient group* $$H_0(\ast)$$ is fixed, are all naturally isomorphic. For example, we previously proved that simplicial homology and singular homology coincide on $$\Delta$$-complexes, and examining the proof step by step, we can verify that what we essentially used were the axioms in [Definition 6](#def6) above. For practical computation of homology, it is good to introduce *cellular homology* defined on *CW complexes*, and this homology also satisfies the axioms above, so it gives the same computation as simplicial homology and singular homology.

On the other hand, all these homology theories have the coefficient group fixed as $$\mathbb{Z}$$, but replacing this with an arbitrary abelian group $$A$$, all axioms of [Definition 6](#def6) still hold. In fact, when defining singular homology or simplicial homology, if instead of taking the chain groups

$$C^\Delta_\bullet(X),\qquad C_\bullet(X)$$

as free abelian groups, we took them as free $$A$$-modules

$$C^\Delta_\bullet(X;A):=C^\Delta_\bullet(X)\otimes_\mathbb{Z}A,\qquad C_\bullet(X;A):=C_\bullet(X)\otimes_\mathbb{Z}A$$

we would have obtained this kind of homology.

Most properties of homology follow from the axioms in [Definition 6](#def6). For example, the generalization of equation (1), which is the goal of this article, can be derived from this. Suppose a topological space $$X$$ is expressed as the union of two open sets $$X=U\cup V$$. Then applying homology to the following inclusions

![inclusions](/assets/images/Math/Algebraic_Topology/Computation_of_homology-7.png){:style="width:8em" class="invert" .align-center}

we obtain a morphism between long exact sequences by exactness, and here the inclusion

$$(V,U\cap V)\rightarrow (X,U)$$

induces an isomorphism in homology by the excision axiom, so all corresponding parts in the above morphism are isomorphisms. That is, we obtain the following long exact sequence morphism

![morphism_of_les](/assets/images/Math/Algebraic_Topology/Computation_of_homology-8.png){:style="width:44em" class="invert" .align-center}

Here $$i,j,k$$ are maps induced by each inclusion, $$\partial$$ are connecting maps, and $$p$$ are cokernel morphisms. For convenience, indices are omitted. Now let us call this long exact sequence morphism $$\alpha$$, and denote the mapping cone exact sequence of $$\alpha$$

$$\begin{aligned}\cdots &\overset{\overline{\partial}}{\longrightarrow} H_{n+1}(X)\oplus H_{n+1}(V, U\cap V)\overset{\overline{\Phi}}{\longrightarrow} H_{n+1}(X,U)\oplus H_n(U\cap V)\overset{\overline{\Psi}}{\longrightarrow} H_n(U)\oplus H_n(V)\\ \phantom{\cdots}&\overset{\overline{\partial}}{\longrightarrow} H_n(X)\oplus H_n(V, U\cap V)\rightarrow \cdots\end{aligned}$$

as $$\Cone(\alpha)$$. Then by the result of the excision axiom earlier, the following long exact sequence

$$\cdots \rightarrow 0 \rightarrow H_{n+1}(V, U\cap V)\rightarrow H_{n+1}(X,U)\rightarrow 0 \rightarrow \cdots\tag{4}$$

exists, and using this, we can see that $$\Cone(\alpha)$$ can be expressed as the direct sum of this trivial long exact sequence and the following long exact sequence

$$\cdots \rightarrow H_{n+1}(U)\oplus H_{n+1}(V)\rightarrow H_{n+1}(X)\rightarrow H_n(U\cap V)\rightarrow H_n(U)\oplus H_n(V)\rightarrow\cdots\tag{5}$$

Since both $$\Cone(\alpha)$$ and (4) are exact, (5) is also exact, and the differential maps of the exact sequence (5) are obtained through the change of basis defined by the isomorphisms $$i_V$$ in the mapping cone exact sequence. Computing this explicitly, we obtain the following.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7 (Mayer-Vietoris sequence)**</ins> Suppose a topological space $$X$$ is expressed as the union of two open sets $$X=U\cap V$$, and consider a homology theory $$H$$ defined on it. Then the long exact sequence

$$\cdots \rightarrow H_{n+1}(U)\oplus H_{n+1}(V)\overset{\Psi}{\longrightarrow} H_{n+1}(X)\overset{\partial}{\longrightarrow} H_n(U\cap V)\overset{\Phi}{\longrightarrow} H_n(U)\oplus H_n(V)\rightarrow\cdots$$

exists, where the maps $$\Psi, \Phi$$ are given by

$$\Psi(u,v)=u+v,\qquad \Phi(x)=(x,-x)$$

</div>

In particular, for $$n=1$$, we obtain equation (1), which we derived at the beginning by translating the Seifert-van Kampen theorem through abelianization, and in this respect, the Mayer-Vietoris sequence can be thought of as the homology version of the Seifert-van Kampen theorem.

--- 

**References**

[Hat] A. Hatcher, *Algebraic Topology*. Cambridge University Press, 2022.  
[May] J. P. May, *A concise course in algebraic topology*.

---
