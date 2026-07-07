---
title: "Characteristic Classes of Vector Bundles"
description: "Starting from the Euler class of an oriented vector bundle, we define Chern and Pontryagin classes via the Thom isomorphism and the Gysin exact sequence."
excerpt: "Euler, Chern, and Pontryagin characteristic classes"

categories: [Math / Algebraic Topology]
permalink: /en/math/algebraic_topology/characteristic_classes
sidebar: 
    nav: "algebraic_topology-en"

date: 2025-10-07
weight: 11
translated_at: 2026-07-07T07:00:01+00:00
translation_source: kimi-cli
last_polished_at: 2026-07-07T07:00:01+00:00
---
## Euler Class

So far we have used $$\mathbb{Z}/2$$-coefficients to effectively sidestep the issue of orientability. We now take orientation into account as well. With $$\mathbb{Z}/2$$-coefficients we cannot distinguish signs, so every fiber automatically carried a "direction"; but upon passing to $$\mathbb{Z}$$-coefficients, $$1$$ and $$-1$$ become genuinely distinct elements, and the question becomes whether we can assign directions to the fibers consistently. When this is possible, a more delicate invariant appears, lifting the top Stiefel–Whitney class $$w_n$$ to an integer. This is the Euler class.

::: Definition 1
An *orientation* of a rank $$n$$ vector bundle $$p:E\rightarrow B$$ is a continuous choice, in each local trivialization, of a generator $$u_x$$ of $$H^n(p^{-1}(x), p^{-1}(x)\setminus 0;\mathbb{Z})\cong\mathbb{Z}$$ for each fiber $$p^{-1}(x)$$. A bundle admitting such an orientation is called an *oriented vector bundle*.
:::

Giving an orientation can be thought of in three main ways. First, when we are given a vector bundle $$E\rightarrow B$$, we usually think of $$B$$ as sitting inside $$E$$ via the zero section $$0:B\rightarrow E$$. Then in the definition above, the relative cohomology $$H^n(p^{-1}(x), p^{-1}(x)\setminus 0;\mathbb{Z})$$ is itself the data of attaching a $$+$$ or $$-$$ sign to the origin of the fiber, i.e. to the corresponding point of the base $$B$$.

In differential geometry this is interpreted as follows. Removing the origin from the fiber $$p^{-1}(x)\cong\mathbb{R}^n$$ deformation retracts onto the sphere $$S^{n-1}$$, so from the long exact sequence of the pair we obtain the isomorphism

$$H^n(p^{-1}(x), p^{-1}(x)\setminus 0;\mathbb{Z})\cong \widetilde{H}^{n-1}(S^{n-1};\mathbb{Z})\cong\mathbb{Z}.$$

In differential geometry, the top-dimensional cohomology of a manifold contains the volume forms, and this is what determines the orientation; thus we may think of orienting a vector bundle as using the orientation of $$S^{n-1}$$, a space we know well.

However, the most familiar way to orient a vector space is to fix a reference ordered basis and declare that another ordered basis has the negative orientation if the change-of-basis matrix to the reference basis has negative determinant. The problem is that this definition carries too much information: all we actually see is the sign of the change-of-basis determinant. This viewpoint is closely connected to the Čech cohomology explained earlier in [§Stiefel–Whitney Classes, §§Čech Cohomology](/en/math/algebraic_topology/stiefel_whitney_classes#체흐-코호몰로지). That is, we defined an arbitrary vector bundle by a trivializing open cover $$\{U_i\}$$ and transition functions $$g_{ij}: U_{ij}\rightarrow \GL(n;\mathbb{R})$$ over $$U_{ij}$$; choosing one of the two signs of $$\det$$ is then the same as reducing the structure group from $$\GL(n;\mathbb{R})$$ to $$\GL^+(n;\mathbb{R})$$. In other words, the transition functions are no longer allowed to have negative determinant when passing from one chart to another, i.e. orientation reversal is forbidden, and this restriction filters out the non-orientable vector bundles.

When this is possible is told by $$\pi_0(\GL(n;\mathbb{R}))\cong \mathbb{Z}/2$$ that we saw earlier. That is, the only information remaining in each transition function related to orientation is the sign $$\varepsilon_{ij}=\operatorname{sgn}\det g_{ij}:U_{ij}\rightarrow \{\pm 1\}$$ of $$\det g_{ij}$$, and the class $$[\varepsilon_{ij}]\in H^1(B;\mathbb{Z}/2)$$ obtained by gluing these together becomes the obstruction to the reduction to $$\GL^+$$. This class is exactly $$w_1(E)$$ ([§Stiefel–Whitney Classes, ⁋Definition 5](/en/math/algebraic_topology/stiefel_whitney_classes#def5)), and one should think of this as the rank $$n$$ version of the fact that $$H^1(M;\mathbb{Z}/2)$$ carried the orientation information of covering spaces. That is, $$E$$ is orientable if and only if $$w_1(E)=0$$.

Henceforth in this section we assume all bundles are oriented. Once an orientation is given, the generators $$u_x$$ scattered over the fibers coalesce into a single cohomology class.

::: Theorem 2 (Thom isomorphism)
For an oriented rank $$n$$ vector bundle $$p:E\rightarrow B$$, let $$E_0=E\setminus 0(B)$$ be the complement of the zero section. Then there exists a unique *Thom class* $$u\in H^n(E, E_0;\mathbb{Z})$$ whose restriction to $$(p^{-1}(x), p^{-1}(x)\setminus 0)$$ is $$u_x$$ for each $$x\in B$$. Moreover, the composite of cup product and pullback

$$H^k(B;\mathbb{Z})\xrightarrow{\ \cong\ }H^{k+n}(E, E_0;\mathbb{Z}),\qquad \alpha\longmapsto p^\ast\alpha\smile u$$

is an isomorphism for all $$k$$.
:::

::: Proof
The key point is that when $$E$$ is the trivial bundle $$B\times\mathbb{R}^n$$, the pair $$(E, E_0)=(B\times\mathbb{R}^n, B\times(\mathbb{R}^n\setminus 0))$$, and by the relative version of the Künneth formula

$$H^{k+n}(B\times\mathbb{R}^n, B\times(\mathbb{R}^n\setminus 0))\cong H^k(B)\otimes H^n(\mathbb{R}^n,\mathbb{R}^n\setminus 0).$$

The second factor on the right is $$\mathbb{Z}$$, and its generator is the orientation $$u_x$$ of the fiber. In this case it suffices to set $$u=1\otimes u_x$$, and the general case follows by taking a trivializing open cover and gluing these isomorphisms via Mayer–Vietoris. We leave the detailed proof to Chapter 10 of [MS].
:::

The Thom class can be understood as a cohomology class concentrated near the zero section of the vector bundle $$E$$, pointing in the fiber direction. Then the above isomorphism stretches a cohomology class $$\alpha$$ living on $$B$$ into the fiber direction of $$E$$ and multiplies it by $$u$$, and the assertion of the theorem is that this is an isomorphism. Alternatively, from the viewpoint of [§Poincaré Duality, ⁋Example 16](/en/math/algebraic_topology/Poincare_duality#ex16), $$u$$ is the (relative) Poincaré dual of the zero section, and the above isomorphism can be thought of as taking the homology class defined by $$\alpha$$, stretching it along the fiber, and then intersecting it with the zero section to return (but now the homology class lives in the homology group of the total space).

Pulling this Thom class back to the base yields the Euler class.

::: Definition 3
The *Euler class* $$e(E)\in H^n(B;\mathbb{Z})$$ of an oriented rank $$n$$ vector bundle $$E\rightarrow B$$ is defined, for the zero section $$0:B\rightarrow E$$ and the Thom class $$u$$ from [Theorem 2](#thm2), by

$$e(E)=0^\ast\bigl(j^\ast u\bigr).$$

Here $$j^\ast:H^n(E, E_0)\rightarrow H^n(E)$$ is the restriction from the pair to all of $$E$$.
:::

Then $$0^\ast:H^n(E)\rightarrow H^n(B)$$ is an isomorphism because $$p$$ is a homotopy equivalence.

Above we explained that the Thom class is the Poincaré dual of the zero section. Then the Euler class $$e(E)$$ is obtained by restricting this back to the zero section; that is, thinking again in terms of Poincaré duality, it is the self-intersection of the zero section, obtained by pushing the zero section slightly to a generic section and then taking the intersection with the original zero section, which can be thought of as the vanishing locus of a generic section. Making this intuition precise gives the following.

::: Proposition 4
The Euler class satisfies the following.

1. (Naturality) For any $$f:B'\rightarrow B$$, $$e(f^\ast E)=f^\ast e(E)$$.
2. (Whitney) For two oriented bundles, $$e(E\oplus F)=e(E)\smile e(F)$$.
3. (Vanishing) If $$E$$ admits a nowhere-zero section then $$e(E)=0$$. In particular, trivial bundles have $$e=0$$.
4. (Mod 2 reduction) The $$\mathbb{Z}/2$$-reduction of $$e(E)$$ is the top Stiefel–Whitney class $$w_n(E)$$ from [§Stiefel–Whitney Classes, ⁋Definition 5](/en/math/algebraic_topology/stiefel_whitney_classes#def5).
5. (Orientation reversal) Reversing the orientation changes the sign of $$e(E)$$. Hence if $$n$$ is odd then $$2e(E)=0$$.
:::

::: Proof
(1) follows from the compatibility of the Thom class with pullback, and (2) from the fact that the external product of the Thom classes of two bundles becomes the Thom class of their Whitney sum ([MS] §9–10).

For (3), suppose there exists a nowhere-zero section $$s':B\rightarrow E_0$$. The straight-line homotopy $$t\mapsto t\cdot s'$$ is a homotopy in $$E$$ between the zero section $$0$$ and $$s'$$, so $$0^\ast=s'^\ast:H^n(E)\rightarrow H^n(B)$$. On the other hand, $$s'$$ factors through $$i:E_0\hookrightarrow E$$, and from the long exact sequence of the pair the composite $$H^n(E, E_0)\xrightarrow{j^\ast}H^n(E)\xrightarrow{i^\ast}H^n(E_0)$$ is zero, so $$i^\ast(j^\ast u)=0$$, i.e. $$j^\ast u$$ dies on $$E_0$$. Since $$s'$$ passes through $$E_0$$, we have $$s'^\ast(j^\ast u)=0$$, and therefore $$e(E)=0^\ast(j^\ast u)=s'^\ast(j^\ast u)=0$$.

(4) holds because the $$\mathbb{Z}/2$$-reduction of the Thom class is exactly the Thom class defining the Stiefel–Whitney class ([MS] §8), and since restriction commutes with reduction, $$e(E)\bmod 2=w_n(E)$$. For (5), flipping the orientation on each fiber reverses the sign of every $$u_x$$, so $$u\mapsto -u$$ and hence $$e\mapsto -e$$. If $$n$$ is odd, the reflection $$v\mapsto -v$$ on each fiber is a bundle automorphism with determinant $$(-1)^n=-1$$ that reverses the orientation, so this automorphism forces $$e=-e$$, giving $$2e(E)=0$$.
:::

All five properties of [Proposition 4](#prop4) are read off from the picture we saw earlier, namely that $$e(E)$$ is the Poincaré dual recording the zero locus of a generic section, including the signs. Apart from the somewhat formal first two conditions, the remaining three are stories about signs and obstructions.

For instance, the third condition says that if there is a nowhere-zero section, then a generic section can also be chosen without zeros, so the self-intersection disappears and hence $$e(E)=0$$. A picture worth noting is the trivial line bundle over $$S^1$$ twisted twice; a generic section of this bundle meets the zero section twice, but the intersection directions are opposite, so they cancel to give $$0$$.

In the case of the fourth claim, over $$\mathbb{Z}$$ we count the zeros of a generic section with signs, but reducing modulo $$\mathbb{Z}/2$$ forgets those signs. Then the unsigned count of zeros is exactly the top Stiefel–Whitney class $$w_n$$, so $$e(E)$$ is the lift of $$w_n$$ to integers that remembers the signs, and mod $$2$$ is the reverse process.

For the fifth claim, reversing the orientation flips the sign of every zero, so $$e\mapsto -e$$, and in particular when $$n$$ is odd the reflection $$v\mapsto -v$$ on each fiber is a bundle automorphism with determinant $$(-1)^n=-1$$ that reverses the orientation, forcing $$e=-e$$ and hence $$2e(E)=0$$; thus the Euler class of an odd-rank oriented bundle is always $$2$$-torsion.

The name Euler class comes from what it measures. If $$M$$ is a closed oriented $$n$$-manifold and $$E=TM$$ is its tangent bundle, then evaluating $$e(TM)$$ on the fundamental class $$[M]$$ from [§Poincaré Duality, ⁋Definition 10](/en/math/algebraic_topology/Poincare_duality#def10) yields exactly the Euler characteristic

$$\rchi(M)=\int_{[M]} e(TM).$$

That is, the Euler class measures the obstruction to this bundle admitting a nonvanishing section, and if not, how much it is obstructed; in the case of the tangent bundle, the answer turned out to be the topological invariant $$\rchi(M)$$.

Let us verify this concretely on $$S^2$$. From [§Degree of a Map and Brouwer–Lefschetz Fixed-Point Theorem, ⁋Theorem 8](/en/math/algebraic_topology/degree_and_fixed_point_theorems#thm8) we know that every section of $$TS^2$$ must have a zero somewhere. For example, suppose $$S^2$$ is embedded in $$\mathbb{R}^3$$ by

$$S^2=\{(x,y,z): x^2+y^2+z^2=1\}$$

and consider the height function $$z$$ defined on it. Then the gradient vector $$\nabla z$$ gives a section of the tangent bundle by

$$(\nabla z)_{(x,y,z)}=(-xz,-yz,x^2+y^2).$$

We know that this section vanishes exactly at $$(x,y,z)=(0,0,\pm 1)$$. One can check that this section meets the zero section transversely and that both intersection points are positive, so the Euler class must be $$2\in H^2(S^2; \mathbb{Z})$$. Indeed, using the familiar computation of the Euler characteristic we find $$\rchi(S^2)=2$$, confirming our intuition.

## Chern Classes

The Stiefel–Whitney and Euler classes considered so far were invariants of real vector bundles. We now turn our attention to complex vector bundles. Of course any complex vector space can be viewed as a real vector space by separating real and imaginary parts, but the natural morphisms between complex vector spaces lie in $$\GL(n;\mathbb{C})$$ rather than $$\GL(2n;\mathbb{R})$$, and this difference changes many things.

For example, $$\GL(2n;\mathbb{R})$$ is not connected, but $$\GL(n;\mathbb{C})$$ is connected, so every complex vector bundle is automatically orientable. Intuitively it suffices to look at what happens on a single fiber $$V\cong\mathbb{C}^n$$; choosing a (complex) basis

$$v_1,\ldots,v_n$$

for this fiber, the isomorphism $$\mathbb{C}^n\cong \mathbb{R}^{2n}$$ naturally yields the real basis

$$v_1,iv_1,\ldots,v_n,iv_n.$$

Our claim is that this orientation is preserved even when we choose a different complex basis, because viewing the matrix $$A\in\GL(n;\mathbb{C})$$ connecting two bases as a real linear map, its real determinant is

$$\det\nolimits_{\mathbb{R}}(A)=\lvert\det\nolimits_{\mathbb{C}}(A)\rvert^2>0.$$

For instance, in the simplest case $$n=1$$, multiplication by $$z=a+bi$$ is represented by the real matrix

$$\begin{pmatrix}a&-b\\ b&a\end{pmatrix}$$

with determinant $$a^2+b^2>0$$, and for general $$A$$ the determinant always becomes positive in this way. That is, change of basis in a complex vector space always preserves orientation, so $$V$$ carries a canonical orientation as a real vector space, and what we computed above is exactly $$\GL(n;\mathbb{C})\subset \GL^+(2n; \mathbb{R})$$.

In particular, the Euler class is canonically and well defined for any complex vector bundle. Moreover, there are additional invariants beyond the Euler class. For example, a complex vector bundle $$E$$ and its conjugate $$\bar{E}$$ have the same underlying real bundle, but are generally different as complex vector bundles, and the *Chern classes* we will define can distinguish them.

Since the top Chern class satisfies $$c_n=e(E_\mathbb{R})$$, the Chern classes can be thought of as characteristic classes extending the Euler class. There are several ways to define them. In differential geometry one extracts them from the curvature of a connection via Chern–Weil theory, or one can take an axiomatic approach as we did for Stiefel–Whitney. (Of course in this case existence must be proved separately.) Following [MS], we define the Chern classes by descending one step at a time from the Euler class, i.e. the top Chern class. The tool needed in this process is the *Gysin exact sequence* of [Theorem 5](#thm5).

To describe this, we first make the following definition. If the base $$B$$ is paracompact, a partition of unity gives a fiber metric on $$E$$, and then the set of vectors of length $$1$$

$$S(E)=\{v\in E:\lvert v\rvert=1\}$$

becomes a fiber bundle with fiber $$S^{n-1}$$. This is called the *sphere bundle* of $$E$$, and similarly

$$D(E)=\{v\in E:\lvert v\rvert\leq 1\}$$

is called the *disk bundle*, with fiber the disk $$D^n$$. We used a metric for convenience, but this is not essential; what matters is that for the pair $$(D(E), S(E))$$ and the space $$E_0=E\setminus 0(B)$$ with the zero section removed, the pair $$(D(E), S(E))$$ is homotopy equivalent to $$(E, E_0)$$. First we use [§Computations in Homology, ⁋Theorem 2](/en/math/algebraic_topology/computation_of_homology#thm2) to obtain

$$H^\ast(E, E_0)\cong H^\ast\bigl(D(E), D(E)\setminus 0(B)\bigr)$$

for the complement of the zero section in $$D(E)$$, and then apply radial retraction to get

$$(E, E_0)\simeq (D(E), S(E)).$$

Using this we obtain the following.

::: Theorem 5 (Gysin exact sequence)
For the sphere bundle $$\pi:S(E)\rightarrow B$$ of an oriented rank $$n$$ vector bundle $$E\rightarrow B$$, there is a long exact sequence

$$\cdots\rightarrow H^{k-n}(B)\xrightarrow{\ \smile e\ }H^k(B)\xrightarrow{\ \pi^\ast\ }H^k(S(E))\xrightarrow{\ \pi_!\ }H^{k-n+1}(B)\rightarrow H^{k+1}(B)\rightarrow\cdots$$

Here $$e=e(E)$$ is the Euler class, $$\pi^\ast$$ is the pullback, and $$\pi_!$$ is integration along the fiber.
:::

::: Proof
Consider the cohomology long exact sequence of the pair $$(D(E), S(E))$$

$$\cdots\rightarrow H^k(D(E), S(E))\rightarrow H^k(D(E))\rightarrow H^k(S(E))\xrightarrow{\ \delta\ }H^{k+1}(D(E), S(E))\rightarrow\cdots$$

First, the initial term is identified using [Theorem 2](#thm2) as

$$H^k(D(E), S(E))\cong H^k(E, E_0)\cong H^{k-n}(B),$$

and for the second term retraction gives $$H^k(D(E))\cong H^k(B)$$. Through these identifications we obtain the following commutative diagram:

![pair cohomology exact sequence and Gysin exact sequence](/assets/images/Math/Algebraic_Topology/Characteristic_Classes-1.svg){:style="width:40.87em" class="invert" .align-center}

The maps in the second row are those from the upper exact sequence transported along the vertical isomorphisms. Let us trace the first map $$H^{k-n}(B)\rightarrow H^k(B)$$ in detail. Lift $$\alpha\in H^{k-n}(B)$$ to $$H^k(E, E_0)$$ via the Thom isomorphism $$\Phi:\alpha\mapsto p^\ast\alpha\smile u$$, and then compose with the first map $$j^\ast$$ in the upper row to get

$$j^\ast\Phi(\alpha)=j^\ast(p^\ast\alpha\smile u)=p^\ast\alpha\smile j^\ast u.$$

The second equality uses the fact that $$j^\ast$$ is a homomorphism of relative cohomology rings and preserves cup product, i.e. $$j^\ast p^\ast\alpha=p^\ast\alpha$$; intuitively, $$p^\ast\alpha$$ already lives on $$H^\ast(E)$$, so this is obvious. Now we bring this down via the vertical identification $$H^k(E)\cong H^k(B)$$, which is achieved by the zero section $$0:B\hookrightarrow E$$ (with $$p\circ 0=\mathrm{id}$$), so

$$0^\ast(p^\ast\alpha\smile j^\ast u)=0^\ast p^\ast\alpha\smile 0^\ast j^\ast u=\alpha\smile e(E)$$

([Definition 3](#def3)). Similarly, the second map $$H^k(D(E))=H^k(B)\rightarrow H^k(S(E))$$ is the restriction, i.e. $$\pi^\ast$$, and the Gysin map $$\pi_!$$ is the connecting homomorphism $$\delta$$ transported by the Thom isomorphism $$H^{k+1}(D(E), S(E))\cong H^{k-n+1}(B)$$.
:::

The third map $$\pi_!:H^k(S(E))\rightarrow H^{k-n+1}(B)$$ has a somewhat special character. The natural map induced on cohomology by a continuous map $$\pi:S(E)\rightarrow B$$ is usually the pullback $$\pi^\ast:H^\ast(B)\rightarrow H^\ast(S(E))$$, which goes in the reverse direction of $$\pi$$ and preserves degree. By contrast, $$\pi_!$$ goes in the same direction as $$\pi$$ while lowering degree by $$(n-1)$$; a map that goes against the direction that would naturally be induced by a continuous function is called a *wrong way map*, and the subscript $$!$$ is the customary notation.

The intuition for this map is that it reverses [Theorem 2](#thm2). If the Thom isomorphism $$\alpha\mapsto p^\ast\alpha\smile u$$ was a lift in the fiber direction, copying the base class $$\alpha$$ to each point of the fiber ($$p^\ast\alpha$$) and then multiplying by the fiber-direction class $$u$$ to raise degree, then $$\pi_!$$ should be thought of as its inverse. That is, viewing a class on $$S(E)$$ as having a base-direction component and a fiber-direction component, the fiber-direction component is integrated out along each fiber $$S^{n-1}$$ (hence the degree drops by fiber dimension $$n-1$$), and the remaining base-direction class is returned as is. The mathematical formulation of this property is precisely the *projection formula*

$$\pi_!(\pi^\ast\alpha\smile\beta)=\alpha\smile\pi_!\beta,\qquad \alpha\in H^\ast(B), \quad\beta\in H^\ast(S(E)).$$

To see this in action, consider the tangent bundle $$TS^2$$ of $$S^2$$ that we examined above. In the Gysin sequence,

$$\smile e:H^0(S^2)\rightarrow H^2(S^2)$$

is given by the $$\times 2$$ map, and its cokernel $$\mathbb{Z}/2$$ appears as torsion in $$H^2$$ of the sphere bundle $$S(TS^2)$$. On the other hand, if we had started from the trivial bundle $$E$$ over $$S^2$$, this part would have been $$\mathbb{Z}$$; so the trace of the Euler class pushing the sphere bundle away from a product is contained in this torsion.

Now we define the Chern class from this. The key fact is that when $$k<n-1$$,

$$H^{k-n}(B)=H^{k-n+1}(B)=0,$$

so $$\pi^\ast:H^k(B)\rightarrow H^k(S(E))$$ is an isomorphism. That is, the cohomology of the sphere bundle agrees exactly with that of the base in low degrees, and after that the Euler class makes an additional contribution on top of what comes from the base.

Consider the deleted total space $$E_0=E\setminus 0(B)$$ that we have been looking at. A point of $$E_0$$ is an ordered pair of a point $$x\in B$$ of the base and a *nonzero* vector $$v\in E_x$$ in the fiber of $$E$$ at that point. Now define the *tautological bundle* $$\pi_0^\ast E$$ over $$E_0$$. This is the vector bundle obtained by pulling back the vector bundle $$E\rightarrow B$$ along the projection map $$\pi_0:E_0\rightarrow B$$, and its fiber at each point $$(x,v)\in E_0$$ is $$(\pi_0^\ast E)_{(x,v)}= E_x$$. That is, $$v$$ is also an element of the vector space attached to the point $$(x,v)$$, and since it is nonzero it defines a $$1$$-dimensional subspace $$\langle v\rangle$$ inside this vector space. Attaching such a line to every point of $$E_0$$ in this way yields a line bundle $$L\rightarrow E_0$$, and we can consider the quotient $$(\pi_0^\ast E)/L\rightarrow E_0$$ that it defines inside $$\pi_0^\ast E$$. This is a canonical complex rank $$(n-1)$$ bundle over $$E_0$$ with fiber $$E_x/\langle v\rangle$$ at each point $$(x,v)$$, and if we give a Hermitian inner product on each fiber it is also realized as the orthogonal complement $$v^\perp\subseteq E_x$$ of $$v$$. ([\[Linear Algebra\] §Complex Inner Product Spaces, ⁋Proposition 4](/en/math/linear_algebra/complex_inner_product_spaces#prop4)) Since the two realizations are canonically isomorphic, we shall denote this rank $$(n-1)$$ bundle by $$L^\perp$$ for convenience.

Now let a <em>complex</em> vector bundle $$E$$ be given, and denote by $$E_\mathbb{R}$$ the same bundle viewed as an (oriented) real vector bundle. If $$E$$ has complex dimension $$n$$, then $$E_\mathbb{R}$$ has real dimension $$2n$$. Then $$E_0$$ is homotopy equivalent to the sphere bundle $$S(E_{\mathbb{R}})$$ of $$E_{\mathbb{R}}$$, so the Gysin exact sequence of [Theorem 5](#thm5)

$$\cdots\rightarrow H^{k-2n}(B)\xrightarrow{\ \smile e\ }H^k(B)\xrightarrow{\ \pi_0^\ast\ }H^k(E_0)\rightarrow H^{k-2n+1}(B)\rightarrow\cdots$$

holds, and as we saw above, when $$k\leq 2n-2$$ the outer terms $$H^{k-2n}(B)$$ and $$H^{k-2n+1}(B)$$ both have negative degree and hence are $$0$$, so $$\pi_0^\ast:H^k(B)\rightarrow H^k(E_0)$$ is an isomorphism.

::: Definition 6
The *Chern classes* $$c_i(E)\in H^{2i}(B;\mathbb{Z})$$ of a complex rank $$n$$ vector bundle $$E\rightarrow B$$ are defined inductively on the rank $$n$$ of the vector bundle as follows.

First $$c_0(E)=1$$, and $$c_i(E)=0$$ for $$i>n$$;

$$c_n(E)=e(E_{\mathbb{R}})\in H^{2n}(B;\mathbb{Z}).$$

For $$0<i<n$$, since $$L^\perp$$ defined above is a rank $$(n-1)$$ vector bundle whose Chern classes are already defined by the inductive hypothesis, we transport them via the isomorphism $$\pi_0^\ast:H^{2i}(B)\rightarrow H^{2i}(E_0)$$ and define the (unique) classes $$c_i(E)\in H^{2i}(B)$$ satisfying

$$\pi_0^\ast c_i(E)=c_i(L^\perp)$$

to be the $$i$$th Chern class of $$E$$. The sum $$c(E)=1+c_1(E)+\cdots+c_n(E)\in H^\bullet(B;\mathbb{Z})$$ is called the *total Chern class*.
:::

As in other situations, what is as important as the definition are the following properties that it satisfies.

::: Proposition 7
The Chern classes satisfy the following.

1. (Naturality) For any $$f:B'\rightarrow B$$, $$c(f^\ast E)=f^\ast c(E)$$.
2. $$c_0(E)=1$$, and $$c_i(E)=0$$ for $$i>\rank_{\mathbb{C}}E$$.
3. (Top class) $$c_n(E)=e(E_{\mathbb{R}})$$, and hence if $$E$$ has a nonzero section then $$c_n(E)=0$$.
:::

::: Proof
The second and third conditions follow immediately from the definition using the vanishing of $$c_n=e(E_{\mathbb{R}})$$ and the third condition of [Proposition 4](#prop4).

The first condition is proved by induction on $$n$$. The naturality of $$c_n$$ comes from the naturality of the Euler class (first condition of [Proposition 4](#prop4)). For $$0<i<n$$, the map $$f$$ induces a bundle map $$E_0'\rightarrow E_0$$ compatible with the deleted spaces, complement bundles, and the entire Gysin sequence, and since $$f^\ast(L^\perp)\cong(f^\ast L)^\perp$$ on it, the naturality of $$c_i$$ follows from the inductive hypothesis and the naturality of $$\pi_0^\ast$$.
:::

Thus the Chern class satisfies axiomatic properties of a similar kind to the Stiefel–Whitney class. ([§Stiefel–Whitney Classes, ⁋Definition 5](/en/math/algebraic_topology/stiefel_whitney_classes#def5)) We showed the existence of Stiefel–Whitney classes by considering the real infinite Grassmannian $$\Gr(k,\mathbb{R}^\infty)$$, pulling back cohomology classes from there to the original space, and showing that they satisfy the axiomatic conditions for Stiefel–Whitney classes; a similar construction is possible for Chern classes.

::: Example 8
As the complex analogue of the real tautological line bundle from [§Stiefel–Whitney Classes, ⁋Example 3](/en/math/algebraic_topology/stiefel_whitney_classes#ex3), consider the tautological complex line bundle $$\gamma$$ over $$\CP^\infty=\Gr(1,\mathbb{C}^\infty)$$. The sphere bundle of $$\gamma$$ is the unit sphere $$S^\infty$$ in $$\mathbb{C}^\infty$$, which is contractible[^1], so $$H^k(S^\infty)=0$$ for all $$k>0$$. Hence by [Theorem 5](#thm5), $$H^1(\CP^\infty)=0$$ and

$$\smile c_1(\gamma):H^{k-2}(\CP^\infty)\rightarrow H^k(\CP^\infty)$$

is an isomorphism for $$k\geq 2$$. Starting from $$H^0(\CP^\infty)=\mathbb{Z}$$, we find that $$c_1(\gamma)$$ is a generator of $$H^2(\CP^\infty;\mathbb{Z})\cong\mathbb{Z}$$, and

$$H^\bullet(\CP^\infty;\mathbb{Z})=\mathbb{Z}[c_1(\gamma)].$$

This is, just as for real bundles in [§Stiefel–Whitney Classes, §§Grassmann Varieties](/en/math/algebraic_topology/stiefel_whitney_classes#그라스만-다양체), the *universal family* for complex line bundles. That is, any complex line bundle is obtained uniquely as a pullback of $$\gamma$$, so the first Chern class gives a one-to-one correspondence

$$\{\text{complex line bundles over }B\}/\cong\ \xrightarrow{\ c_1\ }\ H^2(B;\mathbb{Z})$$

which is a group isomorphism sending tensor product to addition. Thus all information about a complex line bundle is packed into $$c_1$$.
:::

More generally, the complex Grassmannian $$\Gr(k,\mathbb{C}^\infty)$$ takes the place of the real Grassmannian, and its cohomology ring is

$$H^\bullet(\Gr(k,\mathbb{C}^\infty);\mathbb{Z})=\mathbb{Z}[c_1,\ldots,c_k]$$

the polynomial ring generated by the Chern classes of the universal bundle, and we shall revisit this kind of computation before long.

Meanwhile, just as the Stiefel–Whitney classes obeyed the Whitney sum formula, it is natural to expect the same formula for Chern classes here. The key step in actually proving this is [§Projective Bundles and the Leray–Hirsch Theorem, ⁋Theorem 5](/en/math/algebraic_topology/projective_bundles#thm5); the proof of this theorem is certainly possible with the discussion so far, but for the sake of narrative flow we defer it to the next post.

::: Theorem 9 (Whitney sum formula)
For two complex vector bundles $$E,E'\rightarrow B$$,

$$c(E\oplus E')=c(E)\smile c(E')$$

holds. That is, for all $$k$$,

$$c_k(E\oplus E')=\sum_{i+j=k}c_i(E)\smile c_j(E').$$
:::

::: Proof
By [§Projective Bundles and the Leray–Hirsch Theorem, ⁋Theorem 5](/en/math/algebraic_topology/projective_bundles#thm5), there exists a continuous map $$\rho:F(E)\rightarrow B$$ such that the pullback $$\rho^\ast:H^\bullet(B)\hookrightarrow H^\bullet(F(E))$$ is injective and $$\rho^\ast E$$ splits as a Whitney sum $$L_1\oplus\cdots\oplus L_n$$ of complex line bundles. By naturality and the injectivity of $$\rho^\ast$$, it suffices to prove the formula assuming every bundle is a sum of line bundles.

Then it suffices to show that for a sum of line bundles,

$$c(L_1\oplus\cdots\oplus L_n)=\prod_{i=1}^n\bigl(1+c_1(L_i)\bigr).$$

The key is the two equalities for two line bundles $$L,L'$$:

$$c_1(L\oplus L')=c_1(L)+c_1(L'),\qquad c_2(L\oplus L')=c_1(L)\smile c_1(L').$$

The second equality is obtained immediately over any base. By [Definition 6](#def6), the top class of a rank $$2$$ bundle is

$$c_2(L\oplus L')=e\bigl((L\oplus L')_{\mathbb{R}}\bigr),$$

and by the second result of [Proposition 4](#prop4) this equals $$e(L_{\mathbb{R}})\smile e(L'_{\mathbb{R}})=c_1(L)\smile c_1(L')$$.

For the first equality, we first show that for any rank $$n$$ complex vector bundle $$E$$ and trivial line bundle $$\varepsilon^1$$,

$$c(E\oplus\varepsilon^1)=c(E)$$

holds. Let $$E'=E\oplus\varepsilon^1$$; the section $$s(x)=(0,1)$$ taking the constant $$1$$ from the trivial summand is nowhere zero, so it gives a section $$s:B\rightarrow E'_0$$ with $$\pi_0\circ s=\mathrm{id}$$. Now at each point the orthogonal complement of $$(0,1)$$ is exactly the fiber of $$E$$, so $$s^\ast(E'^\perp)\cong E$$, and hence applying $$s^\ast$$ to the equation $$\pi_0^\ast c_i(E')=c_i(E'^\perp)$$ from [Definition 6](#def6) for $$0<i\leq n$$ gives, by naturality from [Proposition 7](#prop7),

$$c_i(E')=s^\ast\pi_0^\ast c_i(E')=s^\ast c_i(E'^\perp)=c_i(s^\ast E'^\perp)=c_i(E).$$

The top class $$c_{n+1}(E')=e(E'_{\mathbb{R}})$$ is zero by (3) of [Proposition 4](#prop4) because a nowhere-zero section exists, which matches $$c_{n+1}(E)=0$$.

On the other hand, as we saw in [Example 8](#ex8), $$\gamma$$ is the universal family for complex line bundles, so any two line bundles $$L,L'$$ over a base $$B$$ are pullbacks $$f_1^\ast\gamma$$, $$f_2^\ast\gamma$$ via morphisms $$f_1,f_2:B\rightarrow\CP^\infty$$ of the base. Setting

$$f=(f_1, f_2): B\rightarrow \CP^\infty\times\CP^\infty,$$

we obtain the following commutative diagram between bases:

![classifying map decomposition](/assets/images/Math/Algebraic_Topology/Characteristic_Classes-2.svg){:style="width:20.62em" class="invert" .align-center}

and therefore showing the formula

$$c_1(L\oplus L')=c_1(L)+c_1(L')$$

over $$B$$ for $$L,L'$$, i.e.

$$c_1(f^\ast(\pi_1^\ast\gamma \oplus \pi_2^\ast\gamma))=c_1(f_1^\ast\gamma)+c_1(f_2^\ast\gamma),$$

is by the first result of [Proposition 7](#prop7) the same as showing

$$c_1(\pi_1^\ast\gamma\oplus \pi_2^\ast\gamma)=c_1(\pi_1^\ast\gamma)+c_1(\pi_2^\ast\gamma).$$

That is, it suffices to show the formula holds for any two line bundles $$L_1,L_2$$ over $$\CP^\infty\times\CP^\infty$$.

For this, first observe by [§Cohomology, ⁋Corollary 10](/en/math/algebraic_topology/cohomology#cor10) that

$$H^2(\CP^\infty\times\CP^\infty;\mathbb{Z})\cong H^2(\CP^\infty;\mathbb{Z})\oplus H^2(\CP^\infty;\mathbb{Z}).$$

That is, defining the restriction maps $$j_1^\ast$$, $$j_2^\ast$$ via the inclusions $$j_1:z\mapsto(z,q)$$, $$j_2:z\mapsto(q,z)$$, these read off the respective components. We showed above that the desired formula holds for trivial line bundles, and $$j_1^\ast L_2$$ and $$j_2^\ast L_1$$ are trivial, so

$$j_1^\ast c_1(L_1\oplus L_2)=c_1(\gamma\oplus\varepsilon^1)=c_1(\gamma)=j_1^\ast\bigl(c_1(L_1)+c_1(L_2)\bigr)$$

and the analogous formula holds for $$j_2^\ast$$. Hence,

$$c_1(L_1\oplus L_2)=c_1(L_1)+c_1(L_2),$$

and as we saw, adding naturality gives the result for arbitrary $$L,L'$$.
:::

Earlier we claimed that the Chern classes can distinguish a complex vector bundle $$E$$ from its conjugate $$\bar{E}$$, i.e. the same underlying real bundle with scalar multiplication twisted to $$z\cdot v=\bar{z}v$$. We now make this claim precise.

::: Proposition 10
For the conjugate $$\bar{E}$$ of a complex vector bundle $$E\rightarrow B$$,

$$c_i(\bar{E})=(-1)^ic_i(E)$$

holds for all $$i$$.
:::
::: Proof
First consider the case of a line bundle $$L$$. By [Definition 6](#def6), $$c_1(L)=e(L_{\mathbb{R}})$$, and $$L$$ and $$\bar{L}$$ have the same underlying real bundle but opposite canonical orientations. Indeed, for a nonzero vector $$v$$ in the fiber, the canonical orientation of $$L$$ is given by the ordered basis $$(v,iv)$$, while in $$\bar{L}$$ the scalar $$i$$ sends $$v$$ to $$-iv$$, so the canonical orientation is given by $$(v,-iv)$$, and the determinant of the change-of-basis matrix between the two is $$-1$$. Hence by (5) of [Proposition 4](#prop4), $$c_1(\bar{L})=-c_1(L)$$.

The general case also follows using the splitting principle, just as in the proof above.
:::

For example, for the tautological bundle $$\gamma$$ from [Example 8](#ex8), $$c_1(\gamma)$$ is a generator of $$H^2(\CP^\infty;\mathbb{Z})\cong\mathbb{Z}$$, so $$c_1(\bar{\gamma})=-c_1(\gamma)\neq c_1(\gamma)$$, and hence $$\gamma\not\cong\bar{\gamma}$$. Of course there is a limit to this distinction: if all odd Chern classes of a bundle are $$2$$-torsion or $$0$$, its conjugate cannot be distinguished by Chern classes alone, but we can still see that Chern classes carry richer information than real bundles.

Meanwhile, all examples so far have been line bundles, so let us give one example showing how [Theorem 9](#thm9) is used in actual computation for higher-rank bundles.

::: Example 11
In this post we compute the total Chern class of the tangent bundle of the finite-dimensional complex projective space $$\CP^n=\Gr(1,\mathbb{C}^{n+1})$$.

For this, first consider the tautological line bundle $$\gamma\subseteq\CP^n\times\mathbb{C}^{n+1}$$ defined on it. This is the restriction of the universal line bundle $$\gamma$$ from [Example 8](#ex8) to $$\CP^n\hookrightarrow\CP^\infty$$, and since the cell structure has cells only in even dimensions, the restriction $$H^k(\CP^\infty;\mathbb{Z})\rightarrow H^k(\CP^n;\mathbb{Z})$$ is an isomorphism for $$k\leq 2n$$. Hence setting $$\x=c_1(\bar{\gamma})=-c_1(\gamma)$$ by [Proposition 10](#prop10),

$$H^\bullet(\CP^n;\mathbb{Z})=\mathbb{Z}[\x]/(\x^{n+1}).$$

Now consider the tangent bundle. A point $$\ell\in\CP^n$$ of this space is a line $$\ell\subseteq\mathbb{C}^{n+1}$$, and fixing a Hermitian inner product, lines near $$\ell$$ are uniquely represented as graphs of linear maps $$\ell\rightarrow\ell^\perp$$. That is, writing the bundle of $$\mathbb{C}$$-linear maps fiberwise as $$\Hom$$,

$$T\CP^n\cong\Hom(\gamma,\gamma^\perp).$$

Adding the trivial line bundle $$\Hom(\gamma,\gamma)$$ via Whitney sum gives

$$T\CP^n\oplus\Hom(\gamma,\gamma)\cong\Hom(\gamma,\gamma^\perp\oplus\gamma)\cong\Hom(\gamma,\varepsilon^{n+1})\cong\Hom(\gamma,\varepsilon^1)^{\oplus(n+1)}.$$

Here $$\varepsilon^{n+1}$$ is the rank $$n+1$$ trivial bundle. Hence, identifying $$\Hom(\gamma, \varepsilon^1)$$ on the right with $$\overline{\gamma}$$, we obtain from [Theorem 9](#thm9) the formula

$$c(T\CP^n)=c\bigl(T\CP^n\oplus\Hom(\gamma,\gamma)\bigr)=c(\bar{\gamma})^{n+1}=(1+\x)^{n+1},$$

and expanding this, since $$H^\bullet(\CP^n)=\mathbb{Z}[\x]/(\x^{n+1})$$,

$$c(T\CP^n)=(n+1)\x^n+\cdots +1.$$

## Pontryagin Classes

For real vector bundles as well, $$\mathbb{Z}$$-coefficient invariants can be obtained via the complex Chern classes.

::: Definition 12
The *Pontryagin classes* $$p_i(E)\in H^{4i}(B;\mathbb{Z})$$ of a real vector bundle $$E\rightarrow B$$ are defined from the Chern classes of the complexification $$E\otimes_{\mathbb{R}}\mathbb{C}$$ by

$$p_i(E)=(-1)^i c_{2i}(E\otimes_{\mathbb{R}}\mathbb{C}).$$
:::

The complexification $$E\otimes_{\mathbb{R}}\mathbb{C}$$ is isomorphic to its conjugate $$\overline{E\otimes\mathbb{C}}$$ via $$v\otimes z\mapsto v\otimes\bar{z}$$. Then by [Proposition 10](#prop10), $$c_{2i+1}(E\otimes\mathbb{C})=-c_{2i+1}(E\otimes\mathbb{C})$$, i.e. the odd Chern classes are all $$2$$-torsion ($$2c_{2i+1}=0$$) and essentially carry no meaningful information. For this reason we define the $$i$$th class using only the even-positioned (signed) Chern classes, and since the Chern class essentially lives in cohomology of degree twice its index, the Pontryagin class ends up in $$H^{4i}(B;\mathbb{Z})$$. Intuitively this is bringing the work of Stiefel–Whitney classes over $$\mathbb{Z}/2$$ to $$\mathbb{Z}$$-coefficients (without passing to complex vector bundles), or bringing the work of Chern classes for complex vector bundles down to real vector bundles.

The basic properties also descend from the Chern classes via complexification. The total Pontryagin class is written $$p(E)=1+p_1(E)+p_2(E)+\cdots$$.

::: Proposition 13
For real vector bundles $$E,F\rightarrow B$$, the following hold.

1. (Naturality) For any $$f:B'\rightarrow B$$, $$p(f^\ast E)=f^\ast p(E)$$.
2. (Whitney) $$2\bigl(p(E\oplus F)-p(E)\smile p(F)\bigr)=0$$. In particular, if there is no $$2$$-torsion in $$H^\bullet(B;\mathbb{Z})$$ then $$p(E\oplus F)=p(E)\smile p(F)$$.
3. For a complex vector bundle $$E$$, $$E_{\mathbb{R}}\otimes_{\mathbb{R}}\mathbb{C}\cong E\oplus\bar{E}$$, and hence $$p_i(E_{\mathbb{R}})$$ is a polynomial in the Chern classes of $$E$$. For example, $$p_1(E_{\mathbb{R}})=c_1(E)^2-2c_2(E)$$.
:::
::: Proof
(1) follows immediately because complexification commutes with pullback and from the naturality in [Proposition 7](#prop7). For (2), apply [Theorem 9](#thm9) to $$(E\oplus F)\otimes\mathbb{C}\cong(E\otimes\mathbb{C})\oplus(F\otimes\mathbb{C})$$; by the observation below [Definition 12](#def12), the odd Chern classes are all $$2$$-torsion, so the terms containing them vanish when multiplied by $$2$$, and the remaining even terms give $$p(E)\smile p(F)$$.

Only (3) requires a small calculation. When we complexify $$E_{\mathbb{R}}\otimes\mathbb{C}$$, the complex structure appears as $$J\in \End(E)$$ with eigenvalues $$\pm i$$. Extending this $$\mathbb{C}$$-linearly, the $$\pm i$$ eigenspace decomposition gives $$E_{\mathbb{R}}\otimes\mathbb{C}\cong E\oplus\bar{E}$$. Then by [Theorem 9](#thm9) and [Proposition 10](#prop10), $$c_2(E_{\mathbb{R}}\otimes\mathbb{C})=c_2(E\oplus\bar{E})=2c_2(E)-c_1(E)^2$$, and bringing this to the Pontryagin class yields the desired result.
:::

---

**References**

**[MS]** J. W. Milnor and J. D. Stasheff, *Characteristic Classes*, Annals of Mathematics Studies 76, Princeton University Press, 1974.

**[BT]** R. Bott and L. W. Tu, *Differential Forms in Algebraic Topology*, Springer, 1982.

**[Hat]** A. Hatcher, *Vector Bundles and K-Theory*, online notes, 2017.

---
[^1]: View $$S^\infty$$ as the unit sphere in $$\mathbb{C}^\infty=\bigcup_n\mathbb{C}^n$$. For the shift map $$T(x_1,x_2,\ldots)=(0,x_1,x_2,\ldots)$$, normalize vectors by $$v\mapsto v/\lvert v\rvert$$; the two straight-line homotopies $$x\mapsto\bigl((1-t)x+tT(x)\bigr)/\lvert(1-t)x+tT(x)\rvert$$ and $$x\mapsto\bigl((1-t)T(x)+te_1\bigr)/\lvert(1-t)T(x)+te_1\rvert$$ connect the identity to $$T$$, and $$T$$ to the constant map $$x\mapsto e_1=(1,0,\ldots)$$, respectively. Neither denominator vanishes: for the former, the coordinates of $$x$$ and $$T(x)$$ are shifted by one, so $$(1-t)x+tT(x)=0$$ forces $$x=0$$; for the latter, the first coordinate of the sum is $$t$$, so for it to be $$0$$ we need $$t=0$$, which then gives $$T(x)=0$$, i.e. $$x=0$$. Joining these two shows that $$S^\infty$$ contracts to a point.
