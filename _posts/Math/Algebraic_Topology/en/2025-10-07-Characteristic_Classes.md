---
title: "Characteristic Classes of Vector Bundles"
description: "Starting from the Euler class of an oriented vector bundle, we define Chern and Pontryagin characteristic classes via the Thom isomorphism and the Gysin long exact sequence."
excerpt: "Euler, Chern, and Pontryagin characteristic classes"

categories: [Math / Algebraic Topology]
permalink: /en/math/algebraic_topology/characteristic_classes
sidebar: 
    nav: "algebraic_topology-en"

date: 2025-10-07
weight: 14
translated_at: 2026-08-15T18:20:16+00:00
translation_source: kimi-cli
---
## Euler Class

So far we have effectively avoided the issue of orientability by using $\mathbb{Z}/2$-coefficients. We now take orientation into account as well. With $\mathbb{Z}/2$-coefficients we cannot distinguish signs, so every fiber automatically carried a "direction"; but upon passing to $\mathbb{Z}$-coefficients, $1$ and $-1$ become genuinely distinct elements, and the question becomes whether one can consistently assign a direction to each fiber. When this is possible, a more refined invariant appears, lifting the top Stiefel-Whitney class $w_n$ to the integers. This is the Euler class.

::: Definition 1
An *orientation* of a rank $n$ vector bundle $p:E\rightarrow B$ is a continuous choice, in each local trivialization, of a generator $u_x$ of $H^n(p^{-1}(x), p^{-1}(x)\setminus 0;\mathbb{Z})\cong\mathbb{Z}$ for each fiber $p^{-1}(x)$. A bundle admitting such an orientation is called an *oriented vector bundle*.
:::

One can think of giving an orientation in three broad ways. First, we usually regard the base $B$ as sitting inside $E$ via the zero section $0:B\rightarrow E$. Then in the definition above, the relative cohomology $H^n(p^{-1}(x), p^{-1}(x)\setminus 0;\mathbb{Z})$ is, in itself, the data of attaching a $+$ or $-$ sign to the origin of the fiber, that is, to the corresponding point of the base $B$.

In differential geometry this is interpreted as follows. Since the fiber $p^{-1}(x)\cong\mathbb{R}^n$ with the origin removed deformation retracts onto the sphere $S^{n-1}$, the long exact sequence of the pair yields the isomorphism

$$H^n(p^{-1}(x), p^{-1}(x)\setminus 0;\mathbb{Z})\cong \widetilde{H}^{n-1}(S^{n-1};\mathbb{Z})\cong\mathbb{Z}.$$

In differential geometry the top-dimensional cohomology of a manifold contains the volume form, and this is what determines the orientation; thus one may think of orienting the vector bundle by using the orientation of $S^{n-1}$, a space we know well.

However, the most familiar way to orient a vector space is to fix a reference ordered basis and declare that another ordered basis is negatively oriented if the change-of-basis matrix to the reference basis has negative determinant. The trouble with such a definition is that it carries too much information: what we actually see is only the sign of the $\det$ of the change of basis. This viewpoint is closely connected to the Čech cohomology explained earlier in [§Stiefel-Whitney Characteristic Classes, §§Čech Cohomology](/en/math/algebraic_topology/stiefel_whitney_classes#čech-cohomology). That is, we defined an arbitrary vector bundle by a trivializing open cover $\{U_i\}$ and transition functions $g_{ij}: U_{ij}\rightarrow \GL(n;\mathbb{R})$ over $U_{ij}$; choosing one of the two signs of $\det$ is then the same as reducing the structure group from $\GL(n;\mathbb{R})$ to $\GL^+(n;\mathbb{R})$. In other words, when passing from one chart to another via the transition functions, a negative determinant (that is, a reversal of orientation) is no longer allowed, and this restriction filters out the non-orientable vector bundles.

When this is possible is told by $\pi_0(\GL(n;\mathbb{R}))\cong \mathbb{Z}/2$ seen earlier. Namely, the only information about orientation remaining from each transition function is the sign $\varepsilon_{ij}=\operatorname{sgn}\det g_{ij}:U_{ij}\rightarrow \{\pm 1\}$, and the class $[\varepsilon_{ij}]\in H^1(B;\mathbb{Z}/2)$ obtained by gluing these together becomes the obstruction to reducing to $\GL^+$. This class is exactly $w_1(E)$ ([§Stiefel-Whitney Characteristic Classes, ⁋Definition 5](/en/math/algebraic_topology/stiefel_whitney_classes#def5)), and one should think of this as the rank-$n$ version of the fact that $H^1(M;\mathbb{Z}/2)$ carried the orientation information of covering spaces. That is, $E$ being orientable is equivalent to $w_1(E)=0$.

Henceforth we assume that all bundles discussed in this section are oriented. Once an orientation is given, the generators $u_x$ that were scattered over the individual fibers coalesce into a single cohomology class.

::: Theorem 2 (Thom isomorphism)
For an oriented rank $n$ vector bundle $p:E\rightarrow B$, let $E_0=E\setminus 0(B)$ be the subspace with the zero section removed. Then there exists a unique *Thom class* $u\in H^n(E, E_0;\mathbb{Z})$ such that for each $x\in B$, the restriction of $u$ to $(p^{-1}(x), p^{-1}(x)\setminus 0)$ is $u_x$. Moreover, the composite of cup product and pullback

$$H^k(B;\mathbb{Z})\xrightarrow{\ \cong\ }H^{k+n}(E, E_0;\mathbb{Z}),\qquad \alpha\longmapsto p^\ast\alpha\smile u$$

is an isomorphism for every $k$.
:::

::: Proof
Keeping only the core idea, if $E$ is the trivial bundle $B\times\mathbb{R}^n$, then the pair $(E, E_0)=(B\times\mathbb{R}^n, B\times(\mathbb{R}^n\setminus 0))$, and by the relative version of the Künneth formula

$$H^{k+n}(B\times\mathbb{R}^n, B\times(\mathbb{R}^n\setminus 0))\cong H^k(B)\otimes H^n(\mathbb{R}^n,\mathbb{R}^n\setminus 0).$$

The second factor on the right is $\mathbb{Z}$, and its generator is the orientation $u_x$ of the fiber. In this case it suffices to set $u=1\otimes u_x$, and the general case follows by taking a trivializing open cover and gluing these isomorphisms via Mayer-Vietoris. We leave the detailed proof to Chapter 10 of [MS].
:::

The Thom class can be understood as a cohomology class concentrated near the zero section of the vector bundle $E$ and pointing in the fiber direction. The above isomorphism then stretches a cohomology class $\alpha$ living on $B$ in the fiber direction of $E$ and multiplies it by $u$, and the content of the theorem is that this is an isomorphism. Alternatively, from the viewpoint of [§Poincaré Duality, ⁋Example 16](/en/math/algebraic_topology/Poincare_duality#ex16), $u$ is the (relative) Poincaré dual of the zero section, and the above isomorphism can be thought of as taking the homology class defined by $\alpha$, stretching it along the fiber, and then intersecting it with the zero section to return (but now the homology class lives in the homology group of the total space).

Pulling this Thom class back to the base yields the Euler class.

::: Definition 3
For an oriented rank $n$ vector bundle $E\rightarrow B$, the *Euler class* $e(E)\in H^n(B;\mathbb{Z})$ is defined by

$$e(E)=0^\ast\bigl(j^\ast u\bigr)$$

for the zero section $0:B\rightarrow E$ and the Thom class $u$ of [Theorem 2](#thm2). Here $j^\ast:H^n(E, E_0)\rightarrow H^n(E)$ is the restriction from the pair to all of $E$.
:::

Then $0^\ast:H^n(E)\rightarrow H^n(B)$ is an isomorphism because $p$ is a homotopy equivalence.

Above we explained that the Thom class is the Poincaré dual of the zero section. Then the Euler class $e(E)$ is obtained by restricting this back onto the zero section; that is, viewing it again as a Poincaré dual, one pushes the zero section slightly to a generic section and takes its intersection with the original zero section (namely the self-intersection of the zero section), which can be thought of as the vanishing locus of a generic section. This intuition is made precise as follows.

::: Proposition 4
The Euler class satisfies the following.

1. (Naturality) For any $f:B'\rightarrow B$, $e(f^\ast E)=f^\ast e(E)$.
2. (Whitney) For two oriented bundles, $e(E\oplus F)=e(E)\smile e(F)$.
3. (Vanishing) If $E$ admits a nowhere-vanishing section then $e(E)=0$. In particular, trivial bundles have $e=0$.
4. (Mod 2 reduction) The $\mathbb{Z}/2$-reduction of $e(E)$ is the top Stiefel-Whitney class $w_n(E)$ of [§Stiefel-Whitney Characteristic Classes, ⁋Definition 5](/en/math/algebraic_topology/stiefel_whitney_classes#def5).
5. (Orientation reversal) Reversing the orientation changes the sign of $e(E)$. Hence if $n$ is odd, $2e(E)=0$.
:::
::: Proof
(1) follows from the fact that the Thom class is compatible with pullback, and (2) from the fact that the external product of the Thom classes of two bundles becomes the Thom class of the Whitney sum ([MS] §9–10).

For (3), suppose there exists a nowhere-zero section $s':B\rightarrow E_0$. The straight-line homotopy $t\mapsto t\cdot s'$ is a homotopy in $E$ between the zero section $0$ and $s'$, so $0^\ast=s'^\ast:H^n(E)\rightarrow H^n(B)$. On the other hand $s'$ factors through $i:E_0\hookrightarrow E$, and from the long exact sequence of the pair the composite $H^n(E, E_0)\xrightarrow{j^\ast}H^n(E)\xrightarrow{i^\ast}H^n(E_0)$ is zero, so $i^\ast(j^\ast u)=0$, i.e. $j^\ast u$ dies on $E_0$. Since $s'$ passes through $E_0$, we have $s'^\ast(j^\ast u)=0$, and therefore $e(E)=0^\ast(j^\ast u)=s'^\ast(j^\ast u)=0$.

(4) holds because the $\mathbb{Z}/2$-reduction of the Thom class is exactly the Thom class defining the Stiefel-Whitney class ([MS] §8), and since restriction commutes with reduction, $e(E)\bmod 2=w_n(E)$. For (5), reversing the orientation on each fiber flips the sign of every $u_x$, so $u\mapsto -u$ and hence $e\mapsto -e$. When $n$ is odd, the reflection $v\mapsto -v$ on each fiber is a bundle automorphism with determinant $(-1)^n=-1$ that reverses orientation, and this automorphism forces $e=-e$, so $2e(E)=0$.
:::

All five properties of [Proposition 4](#prop4) are read off from the picture seen earlier, namely that $e(E)$ is the Poincaré dual recording the zero locus of a generic section with signs. Apart from the somewhat formal first two conditions, the remaining three are stories of signs and obstructions.

For instance, the third condition says that if there is a nowhere-vanishing section, then a generic section can also be chosen without zeros, the self-intersection disappears, and hence $e(E)=0$. A picture worth noting is the trivial line bundle over $S^1$ twisted twice; a generic section of this bundle meets the zero section twice, but the intersection directions are opposite, so they cancel to give $0$.

For the fourth claim, over $\mathbb{Z}$ we count the zeros of a generic section with signs, but upon reducing to $\mathbb{Z}/2$ we forget those signs. Then the unsigned count of zeros is exactly the top Stiefel-Whitney class $w_n$, so $e(E)$ is the lift of $w_n$ to the integers so as to remember the signs, and the reverse process is taking mod $2$.

For the fifth claim, reversing the orientation flips the sign of every zero together, giving $e\mapsto -e$; in particular, when $n$ is odd the reflection $v\mapsto -v$ on each fiber is a bundle automorphism with determinant $(-1)^n=-1$ that reverses orientation, forcing $e=-e$ and hence $2e(E)=0$. Thus we immediately obtain that the Euler class of an odd-rank oriented bundle is always $2$-torsion.

The name Euler class comes from what it measures. If $M$ is a closed oriented $n$-manifold and $E=TM$ is its tangent bundle, then evaluating $e(TM)$ on the fundamental class $[M]$ of [§Poincaré Duality, ⁋Definition 10](/en/math/algebraic_topology/Poincare_duality#def10) yields exactly the Euler characteristic

$$\rchi(M)=\int_{[M]} e(TM).$$

That is, the Euler class is the obstruction measuring whether this bundle admits a nonvanishing section, and if not, how much it is obstructed; in the case of the tangent bundle, the answer manifested itself as the topological invariant $\rchi(M)$.

Let us verify this concretely on $S^2$. For example, from [§Mapping Degree and Brouwer–Lefschetz Fixed-Point Theorem, ⁋Theorem 8](/en/math/algebraic_topology/degree_and_fixed_point_theorems#thm8) we know that any section of $TS^2$ must vanish somewhere. Suppose $S^2$ sits in $\mathbb{R}^3$ as

$$S^2=\{(x,y,z)\mid x^2+y^2+z^2=1\},$$

and consider the height function $z$ defined on it. Then the gradient vector $\nabla z$ gives a section of the tangent bundle by

$$(\nabla z)_{(x,y,z)}=(-xz,-yz,x^2+y^2),$$

and indeed this section vanishes at $(x,y,z)=(0,0,\pm 1)$. One can check that this section meets the zero section transversely and that both intersection points are positive, so the Euler class must be $2\in H^2(S^2; \mathbb{Z})$. Using the familiar computation of the Euler characteristic, we find $\rchi(S^2)=2$, confirming that this indeed supports our intuition.

## Chern Classes

Both the Stiefel-Whitney and Euler classes discussed so far were invariants of real vector bundles. We now turn our attention to complex vector bundles. Of course any complex vector space can be viewed as a real vector space by separating real and imaginary parts, but the natural morphisms between complex vector spaces lie in $\GL(n;\mathbb{C})$, not $\GL(2n;\mathbb{R})$, and this difference changes many things.

For example, $\GL(2n;\mathbb{R})$ is not connected, whereas $\GL(n;\mathbb{C})$ is connected, so every complex vector bundle is automatically orientable. Intuitively it suffices to look at what happens on a single fiber $V\cong\mathbb{C}^n$; taking a (complex) basis

$$v_1,\ldots,v_n$$

for this fiber, the isomorphism $\mathbb{C}^n\cong \mathbb{R}^{2n}$ naturally yields the real basis

$$v_1,iv_1,\ldots,v_n,iv_n.$$

Our claim is that this orientation is preserved even when a different complex basis is chosen, because when the matrix $A\in\GL(n;\mathbb{C})$ joining the two bases is viewed as a real linear map, its real determinant is

$$\det\nolimits_{\mathbb{R}}(A)=\lvert\det\nolimits_{\mathbb{C}}(A)\rvert^2>0.$$

For instance, in the simplest case $n=1$, multiplication by $z=a+bi$ becomes the real matrix

$$\begin{pmatrix}a&-b\\ b&a\end{pmatrix}$$

with determinant $a^2+b^2>0$, and for general $A$ the determinant always becomes positive in this way. That is, change of basis in a complex vector space always preserves orientation, so $V$ carries a canonical orientation (as a real vector space), and the calculation above is exactly the statement that $\GL(n;\mathbb{C})\subseteq \GL^+(2n; \mathbb{R})$.

In particular, the Euler class is canonically and well defined for any complex vector bundle. Moreover, there are additional invariants beyond the Euler class. For example, a complex vector bundle $E$ and its conjugate $\bar{E}$ are the same as underlying real vector bundles, but they are generally different as complex vector bundles, and the *Chern classes* we will define can distinguish them.

The Chern classes satisfy $c_n=e(E_\mathbb{R})$ for the top Chern class, so they can be thought of as characteristic classes extending the Euler class. There are several ways to define them. In differential geometry one derives them from the curvature of a connection via Chern–Weil theory, or one can take an axiomatic approach as was done for Stiefel-Whitney classes. (Of course in this case existence must be proved separately.) Following [MS], we define Chern classes by descending step by step from the Euler class, i.e. the top Chern class. What is needed in this process is the *Gysin exact sequence* of [Theorem 5](#thm5).

To describe this, we first make the following definition. If the base $B$ is paracompact, then by a partition of unity we can put a fiber metric on $E$ giving an inner product on each fiber, and then the set of vectors of length $1$

$$S(E)=\{v\in E:\lvert v\rvert=1\}$$

becomes a fiber bundle with fiber $S^{n-1}$. This is called the *sphere bundle* of $E$, and similarly

$$D(E)=\{v\in E:\lvert v\rvert\leq 1\}$$

with fiber the disk $D^n$ is called the *disk bundle* of $E$. We used a metric for convenience, but it is not essential; what matters is that for the space $E_0=E\setminus 0(B)$ with the zero section removed, the pair $(D(E), S(E))$ is homotopy equivalent to $(E, E_0)$. This is obtained by first using [§Computing Homology, ⁋Theorem 2](/en/math/algebraic_topology/computation_of_homology#thm2) to get

$$H^\ast(E, E_0)\cong H^\ast\bigl(D(E), D(E)\setminus 0(B)\bigr)$$

and then applying radial retraction to obtain

$$(E, E_0)\simeq (D(E), S(E)).$$

Using this, we obtain the following.

::: Theorem 5 (Gysin exact sequence)
For the sphere bundle $\pi:S(E)\rightarrow B$ of an oriented rank $n$ vector bundle $E\rightarrow B$ over a paracompact base space $B$, the following long exact sequence

$$\cdots\rightarrow H^{k-n}(B)\xrightarrow{\ \smile e\ }H^k(B)\xrightarrow{\ \pi^\ast\ }H^k(S(E))\xrightarrow{\ \pi_!\ }H^{k-n+1}(B)\rightarrow H^{k+1}(B)\rightarrow\cdots$$

exists. Here $e=e(E)$ is the Euler class, $\pi^\ast$ is the pullback, and $\pi_!$ is integration along the fiber.
:::

::: Proof
Consider the cohomology long exact sequence of the pair $(D(E), S(E))$

$$\cdots\rightarrow H^k(D(E), S(E))\rightarrow H^k(D(E))\rightarrow H^k(S(E))\xrightarrow{\ \delta\ }H^{k+1}(D(E), S(E))\rightarrow\cdots$$

First, the first term is identified using [Theorem 2](#thm2) as

$$H^k(D(E), S(E))\cong H^k(E, E_0)\cong H^{k-n}(B)$$

and for the second term we obtain $H^k(D(E))\cong H^k(B)$ via the retraction. Through these identifications we obtain the following commutative diagram

{% diagram Math/Algebraic_Topology/Characteristic_Classes-1.svg width="40.87em" alt="pair cohomology exact sequence and Gysin exact sequence" %}

where the maps in the second column are obtained by transporting the maps in the upper exact sequence along the vertical isomorphisms. Concretely, let us follow the first morphism $H^{k-n}(B)\rightarrow H^k(B)$. Lifting $\alpha\in H^{k-n}(B)$ to $H^k(E, E_0)$ via the Thom isomorphism $\Phi:\alpha\mapsto p^\ast\alpha\smile u$ and then composing with the first morphism $j^\ast$ in the upper row gives

$$j^\ast\Phi(\alpha)=j^\ast(p^\ast\alpha\smile u)=p^\ast\alpha\smile j^\ast u$$

Here the second equality uses that $j^\ast:H^\ast(E, E_0)\rightarrow H^\ast(E)$ is an $H^\ast(E)$-module homomorphism, which is intuitively clear since $p^\ast\alpha$ already lives over $H^\ast(E)$. Now we descend this again via the vertical identification $H^k(E)\cong H^k(B)$, which is accomplished through the zero section $0:B\hookrightarrow E$ ($p\circ 0=\id$), so we get

$$0^\ast(p^\ast\alpha\smile j^\ast u)=0^\ast p^\ast\alpha\smile 0^\ast j^\ast u=\alpha\smile e(E)$$

([Definition 3](#def3)) Similarly, the second map $H^k(D(E))=H^k(B)\rightarrow H^k(S(E))$ is the restriction, that is $\pi^\ast$, and the Gysin map $\pi_!$ is the connecting homomorphism $\delta$ transported by the Thom isomorphism $H^{k+1}(D(E), S(E))\cong H^{k-n+1}(B)$.
:::

The third morphism $\pi_!:H^k(S(E))\rightarrow H^{k-n+1}(B)$ has a somewhat special property. The natural morphism that a continuous map $\pi:S(E)\rightarrow B$ induces on cohomology is usually the pullback $\pi^\ast:H^\ast(B)\rightarrow H^\ast(S(E))$, which goes in the reverse direction of $\pi$ and preserves degree. By contrast, $\pi_!$ goes in the same direction as $\pi$ while lowering degree by $(n-1)$; a morphism that goes against the direction naturally induced by a continuous function is conventionally called a *wrong way map* and denoted with the subscript $!$.

The intuition for this morphism lies in reversing [Theorem 2](#thm2). If the Thom isomorphism $\alpha\mapsto p^\ast\alpha\smile u$ was a lift in the fiber direction, copying the base class $\alpha$ to each point of the fiber via $p^\ast\alpha$ and then multiplying by the fiber-direction class $u$ to raise degree, then $\pi_!$ should be thought of as its inverse. That is, viewing a class on $S(E)$ as having a base-direction component and a fiber-direction component, the fiber-direction component is integrated out along each fiber $S^{n-1}$, and the remaining base-direction class is returned as-is; in this process the fiber dimension $n-1$ is lost. The precise mathematical formulation of this property is the *projection formula*

$$\pi_!(\pi^\ast\alpha\smile\beta)=\alpha\smile\pi_!\beta,\qquad \alpha\in H^\ast(B), \quad\beta\in H^\ast(S(E))$$

To see this in action, consider the tangent bundle $TS^2$ of $S^2$ examined above. Then in the Gysin sequence

$$\smile e:H^0(S^2)\rightarrow H^2(S^2)$$

is given by the $\times 2$ map, and its cokernel $\mathbb{Z}/2$ appears as torsion in $H^2$ of the sphere bundle $S(TS^2)$. On the other hand, if we had started with the trivial bundle $E$ over $S^2$, this part would have been $\mathbb{Z}$; thus the trace of the Euler class pushing the sphere bundle away from the product is encoded precisely in this torsion.

Now we define the Chern class from this. The key fact is that for $k<n-1$

$$H^{k-n}(B)=H^{k-n+1}(B)=0$$

so $\pi^\ast:H^k(B)\rightarrow H^k(S(E))$ is an isomorphism. That is, the cohomology of the sphere bundle coincides exactly with that of the base in low degrees, and beyond that the Euler class contributes additional terms on top of what comes from the base cohomology.

Henceforth let $E\rightarrow B$ be a *complex* rank $n$ vector bundle, and consider the deleted total space $E_0=E\setminus 0(B)$ that we have been examining. A point of $E_0$ is an ordered pair of a point $x\in B$ of the base and a *nonzero* $v\in E_x$ in the fiber of $E$ at that point. Now define the *tautological bundle* $\pi_0^\ast E$ over $E_0$. This is the vector bundle obtained by pulling back $E\rightarrow B$ along the projection map $\pi_0:E_0\rightarrow B$, and concretely it is the vector bundle having fiber $(\pi_0^\ast E)_{(x,v)}= E_x$ at each point $(x,v)\in E_0$. That is, $v$ is also an element of the vector space attached to each point $(x,v)$, and since it is nonzero it defines a 1-dimensional subspace $\langle v\rangle$ inside this vector space. Now attaching such a line to every point of $E_0$ in this way produces a line bundle $L\rightarrow E_0$, and we can consider the quotient $(\pi_0^\ast E)/L\rightarrow E_0$ defined inside $\pi_0^\ast E$. This is the canonical complex rank $(n-1)$ bundle over $E_0$ with fiber $E_x/\langle v\rangle$ at each point $(x,v)$, and if we give a Hermitian inner product on each fiber it is also realized as the orthogonal complement $v^\perp\subseteq E_x$ of $v$. ([\[Linear Algebra\] §Complex Inner Product Spaces, ⁋Proposition 4](/en/math/linear_algebra/complex_inner_product_spaces#prop4)) Since the two realizations are canonically isomorphic, we shall denote this rank $(n-1)$ bundle by $L^\perp$ for notational convenience.

Now write $E_\mathbb{R}$ for $E$ viewed as an (oriented) real vector bundle. Since $E$ has complex dimension $n$, $E_\mathbb{R}$ has real dimension $2n$. Then $E_0$ is homotopy equivalent to the sphere bundle $S(E_{\mathbb{R}})$ of $E_{\mathbb{R}}$, so by [Theorem 5](#thm5)

$$\cdots\rightarrow H^{k-2n}(B)\xrightarrow{\ \smile e\ }H^k(B)\xrightarrow{\ \pi_0^\ast\ }H^k(E_0)\rightarrow H^{k-2n+1}(B)\rightarrow\cdots$$

holds, and as seen above, for $k\leq 2n-2$ the outer terms $H^{k-2n}(B)$ and $H^{k-2n+1}(B)$ both have negative degree hence are $0$, so $\pi_0^\ast:H^k(B)\rightarrow H^k(E_0)$ is an isomorphism.

::: Definition 6
The *Chern class* $c_i(E)\in H^{2i}(B;\mathbb{Z})$ of a complex rank $n$ vector bundle $E\rightarrow B$ is defined inductively on the rank $n$ of the vector bundle as follows.

First $c_0(E)=1$, and $c_i(E)=0$ for $i>n$, and we set

$$c_n(E)=e(E_{\mathbb{R}})\in H^{2n}(B;\mathbb{Z})$$

For $0<i<n$, since the $L^\perp$ examined above is a rank $(n-1)$ vector bundle whose Chern classes are already defined by the inductive hypothesis, we transport them via the isomorphism $\pi_0^\ast:H^{2i}(B)\rightarrow H^{2i}(E_0)$ and define the (unique) $c_i(E)\in H^{2i}(B)$ satisfying

$$\pi_0^\ast c_i(E)=c_i(L^\perp)$$

to be the $i$-th Chern class of $E$. The sum $c(E)=1+c_1(E)+\cdots+c_n(E)\in H^\bullet(B;\mathbb{Z})$ of all of them is called the *total Chern class*.
:::

As in other situations, what is as important as the definition are the following characteristic properties it satisfies.

::: Proposition 7
The Chern class satisfies the following.

1. (Naturality) For any $f:B'\rightarrow B$, we have $c(f^\ast E)=f^\ast c(E)$.
2. $c_0(E)=1$, and $c_i(E)=0$ for $i>\rank_{\mathbb{C}}E$.
3. (Top degree) $c_n(E)=e(E_{\mathbb{R}})$, and hence if $E$ has a nonzero section then $c_n(E)=0$.
:::

::: Proof
The second and third conditions follow immediately from the definition once we use the vanishing of $c_n=e(E_{\mathbb{R}})$ via the third condition of [Proposition 4](#prop4).

The first condition is proved by induction on $n$. The naturality of $c_n$ comes from the naturality of the Euler class. (First condition of [Proposition 4](#prop4)) For $0<i<n$, $f$ induces a bundle map $E_0'\rightarrow E_0$ compatible with the deleted spaces, complement bundles, and the entire Gysin sequence, and on it $f^\ast(L^\perp)\cong(f^\ast L)^\perp$, so the naturality of $c_i$ follows from the inductive hypothesis and the naturality of $\pi_0^\ast$.
:::

That is, the Chern class satisfies axiomatic properties of a similar kind to the Stiefel-Whitney class. ([§Stiefel-Whitney Characteristic Classes, ⁋Definition 5](/en/math/algebraic_topology/stiefel_whitney_classes#def5)) We showed the existence of Stiefel-Whitney classes by considering the real infinite Grassmannian $\Gr(k,\mathbb{R}^\infty)$ and then pulling back cohomology classes from there to the original space to show that they satisfy the axiomatic conditions for Stiefel-Whitney classes; a similar construction is possible for Chern classes.

::: Example 8
As the complex analogue of the real tautological line bundle in [§Stiefel-Whitney Characteristic Classes, ⁋Example 3](/en/math/algebraic_topology/stiefel_whitney_classes#ex3), consider the tautological complex line bundle $\gamma$ over $\CP^\infty=\Gr(1,\mathbb{C}^\infty)$. Then the sphere bundle of $\gamma$ is the unit sphere $S^\infty$ in $\mathbb{C}^\infty$, which is contractible,[^1] so $H^k(S^\infty)=0$ for all $k>0$. Therefore, by [Theorem 5](#thm5) we have $H^1(\CP^\infty)=0$ and

$$\smile c_1(\gamma):H^{k-2}(\CP^\infty)\rightarrow H^k(\CP^\infty)$$

is an isomorphism for $k\geq 2$. Starting from $H^0(\CP^\infty)=\mathbb{Z}$, we obtain that $c_1(\gamma)$ is a generator of $H^2(\CP^\infty;\mathbb{Z})\cong\mathbb{Z}$, and

$$H^\bullet(\CP^\infty;\mathbb{Z})=\mathbb{Z}[c_1(\gamma)]$$

This is, just as we saw for real bundles in [§Stiefel-Whitney Characteristic Classes, §§Grassmannians](/en/math/algebraic_topology/stiefel_whitney_classes#grassmannians), the *universal family* for complex line bundles. That is, since any complex line bundle is obtained uniquely as a pullback of $\gamma$, the first Chern class gives a one-to-one correspondence

$$\{\text{complex line bundles over }B\}/\cong\ \xrightarrow{\ c_1\ }\ H^2(B;\mathbb{Z})$$

which is a group isomorphism sending tensor product to addition. Thus all information about a complex line bundle is encoded in $c_1$ alone.
:::

More generally, the complex Grassmannian $\Gr(k,\mathbb{C}^\infty)$ takes the place of the real Grassmannian, and its cohomology ring is

$$H^\bullet(\Gr(k,\mathbb{C}^\infty);\mathbb{Z})=\mathbb{Z}[c_1,\ldots,c_k]$$

a polynomial ring generated by the Chern classes of the universal bundle, and we shall revisit this kind of computation before long.

Meanwhile, just as the Stiefel-Whitney class satisfied the Whitney sum formula, it is natural to expect that the Chern class satisfies the same formula here as well. The key step in actually proving this is [§Projective Bundles and the Leray–Hirsch Theorem, ⁋Theorem 5](/en/math/algebraic_topology/projective_bundles#thm5); while the proof of this theorem is already possible with the discussion so far, we separate it into the next post solely for the flow of the story.

::: Theorem 9 (Whitney sum formula)
For two complex vector bundles $E,E'\rightarrow B$ over a paracompact base space $B$,

$$c(E\oplus E')=c(E)\smile c(E')$$

holds. That is, for every $k$,

$$c_k(E\oplus E')=\sum_{i+j=k}c_i(E)\smile c_j(E')$$

holds.
:::

::: Proof
By [§Projective Bundles and the Leray–Hirsch Theorem, ⁋Theorem 5](/en/math/algebraic_topology/projective_bundles#thm5), there exists a continuous map $\rho:F(E)\rightarrow B$ such that the pullback $\rho^\ast:H^\bullet(B)\hookrightarrow H^\bullet(F(E))$ is injective and splits $\rho^\ast E$ as a Whitney sum $L_1\oplus\cdots\oplus L_n$ of complex line bundles. By naturality and the injectivity of $\rho^\ast$, it suffices to prove the formula assuming every bundle is a sum of line bundles.

Thus it is enough to show that for a sum of line bundles,

$$c(L_1\oplus\cdots\oplus L_n)=\prod_{i=1}^n\bigl(1+c_1(L_i)\bigr).$$

The key is the two identities for two line bundles $L,L'$:

$$c_1(L\oplus L')=c_1(L)+c_1(L'),\qquad c_2(L\oplus L')=c_1(L)\smile c_1(L').$$

The second identity is obtained immediately over an arbitrary base. By [Definition 6](#def6), the top class of a rank $2$ bundle is

$$c_2(L\oplus L')=e\bigl((L\oplus L')_{\mathbb{R}}\bigr),$$

and by the second result of [Proposition 4](#prop4), this equals $e(L_{\mathbb{R}})\smile e(L'_{\mathbb{R}})=c_1(L)\smile c_1(L')$.

For the first identity, let us first show that for any rank $n$ complex vector bundle $E$ and trivial line bundle $\varepsilon^1$,

$$c(E\oplus\varepsilon^1)=c(E)$$

holds. If $E'=E\oplus\varepsilon^1$, then the section $s(x)=(0,1)$ taking the constant $1$ from the trivial component is nowhere zero, giving a section $s:B\rightarrow E'_0$ with $\pi_0\circ s=\id$. Now at each point, the orthogonal complement of $(0,1)$ is exactly the fiber of $E$, so $s^\ast(E'^\perp)\cong E$, and thus applying $s^\ast$ to the formula $\pi_0^\ast c_i(E')=c_i(E'^\perp)$ from [Definition 6](#def6) for $0<i\leq n$ yields, by naturality from [Proposition 7](#prop7),

$$c_i(E')=s^\ast\pi_0^\ast c_i(E')=s^\ast c_i(E'^\perp)=c_i(s^\ast E'^\perp)=c_i(E).$$

The top class $c_{n+1}(E')=e(E'_{\mathbb{R}})$ is zero by (3) of [Proposition 4](#prop4) since there exists a nowhere vanishing section, which agrees with $c_{n+1}(E)=0$.

On the other hand, as we saw in [Example 8](#ex8), $\gamma$ is the universal family of complex line bundles, so any two line bundles $L,L'$ over a base $B$ are pullbacks $f_1^\ast\gamma$, $f_2^\ast\gamma$ along morphisms $f_1,f_2:B\rightarrow\CP^\infty$ of the base. Now setting

$$f=(f_1, f_2): B\rightarrow \CP^\infty\times\CP^\infty,$$

we obtain the following commutative diagram between bases

{% diagram Math/Algebraic_Topology/Characteristic_Classes-2.svg width="20.62em" alt="Decomposition of classifying maps" %}

and therefore showing the identity over $B$ for $L, L'$

$$c_1(L\oplus L')=c_1(L)+c_1(L'),$$

that is,

$$c_1(f^\ast(\pi_1^\ast\gamma \oplus \pi_2^\ast\gamma))=c_1(f_1^\ast\gamma)+c_1(f_2^\ast\gamma),$$

is, by the first result of [Proposition 7](#prop7), the same as showing

$$c_1(\pi_1^\ast\gamma\oplus \pi_2^\ast\gamma)=c_1(\pi_1^\ast\gamma)+c_1(\pi_2^\ast\gamma).$$

That is, it suffices to show that the above identity holds for the two line bundles $L_1=\pi_1^\ast\gamma$, $L_2=\pi_2^\ast\gamma$ over $\CP^\infty\times\CP^\infty$.

For this, let us first observe by [§Cohomology, ⁋Corollary 10](/en/math/algebraic_topology/cohomology#cor10) and [§Cohomology, ⁋Theorem 5](/en/math/algebraic_topology/cohomology#thm5) that

$$H^2(\CP^\infty\times\CP^\infty;\mathbb{Z})\cong H^2(\CP^\infty;\mathbb{Z})\oplus H^2(\CP^\infty;\mathbb{Z}).$$

That is, defining the restriction maps $j_1^\ast$, $j_2^\ast$ via the inclusions $j_1:z\mapsto(z,q)$, $j_2:z\mapsto(q,z)$, these read off the respective components. On the other hand, we showed above that the desired identity holds for trivial line bundles, and $j_1^\ast L_2$ and $j_2^\ast L_1$ are trivial, so

$$j_1^\ast c_1(L_1\oplus L_2)=c_1(\gamma\oplus\varepsilon^1)=c_1(\gamma)=j_1^\ast\bigl(c_1(L_1)+c_1(L_2)\bigr)$$

and the analogous identity holds for $j_2^\ast$ as well. Thus,

$$c_1(L_1\oplus L_2)=c_1(L_1)+c_1(L_2),$$

and as we saw above, adding naturality shows that this holds for arbitrary $L,L'$ as well.

Now if we show the sum formula for an arbitrary vector bundle and a line bundle, we can use induction. First, let $X=(\CP^\infty)^n$ and for each projection $\pi_i:X\rightarrow\CP^\infty$ set $L_i=\pi_i^\ast\gamma$, $x_i=c_1(L_i)$. In this case one can compute that $H^\bullet(X;\mathbb{Z})=\mathbb{Z}[x_1,\ldots,x_n]$, and by the same argument as above it suffices to show the formula only over this space. Now considering the inclusion $\iota_j:(\CP^\infty)^{n-1}\rightarrow X$ obtained by fixing the $j$-th coordinate at an arbitrary point, $\iota_j^\ast L_j$ is trivial so $\iota_j^\ast x_j=0$, and thus applying $c(E\oplus\varepsilon^1)=c(E)$ shown above and using the inductive hypothesis for $n-1$, we obtain

$$\iota_j^\ast\left(c(L_1\oplus\cdots\oplus L_n)-\prod_{i=1}^n(1+x_i)\right)=0.$$

However, $\iota_j^\ast$ leaves the remaining $x_i$ unchanged, so its kernel is the ideal $(x_j)$, and the difference inside $\iota_j^\ast$ must be a multiple of $x_j$. But since the same argument holds for every $j$, this difference is a multiple of $x_1\cdots x_n$, and considering the rank of $L_1\oplus\cdots L_n$, this difference must be exactly an integer multiple of $x_1\cdots x_n$. But in the top degree, $c(L_1\oplus\cdots \oplus L_n)$ must equal the Euler class, so it must be $x_1\cdots x_n$, and therefore expanding the product in the back shows that this integer is $0$. That is, $c(L_1\oplus\cdots\oplus L_n)=\prod_{i=1}^n(1+x_i)$.
:::

Earlier we claimed that Chern classes can distinguish a complex vector bundle $E$ from its conjugate $\bar{E}$, that is, the bundle with the same underlying real bundle but with scalar multiplication twisted by $z\cdot v=\bar{z}v$. We can now make this claim precise.

::: Proposition 10
For the conjugate $\bar{E}$ of a complex vector bundle $E\rightarrow B$,

$$c_i(\bar{E})=(-1)^ic_i(E)$$

holds for all $i$.
:::
::: Proof
Let us first consider the case of a line bundle $L$. By [Definition 6](#def6), $c_1(L)=e(L_{\mathbb{R}})$, and $L$ and $\bar{L}$ have the same underlying real bundle but opposite standard orientations. Indeed, for a nonzero vector $v$ in the fiber, the standard orientation of $L$ is given by the ordered basis $(v,iv)$, while in $\bar{L}$ since $i$ sends $v$ to $-iv$, the standard orientation is given by $(v,-iv)$, and the determinant of the change of basis matrix between the two bases is $-1$. Therefore by (5) of [Proposition 4](#prop4), $c_1(\bar{L})=-c_1(L)$.

The general case also follows by the splitting principle, just as in the proof above.
:::

For instance, for the tautological bundle $\gamma$ of [Example 8](#ex8), $c_1(\gamma)$ is a generator of $H^2(\CP^\infty;\mathbb{Z})\cong\mathbb{Z}$, so $c_1(\bar{\gamma})=-c_1(\gamma)\neq c_1(\gamma)$, and therefore $\gamma\not\cong\bar{\gamma}$. Of course this distinction has its limitations: the conjugate of a bundle whose odd Chern classes are all $2$-torsion or $0$ cannot be distinguished by Chern classes alone, but we can still confirm that Chern classes carry richer information than real bundles.

Since all examples so far have been line bundles, let us look at one example showing how [Theorem 9](#thm9) is actually used in calculations for bundles of higher rank.

::: Example 11
In this post we compute the total Chern class of the tangent bundle of the finite-dimensional complex projective space $\CP^n=\Gr(1,\mathbb{C}^{n+1})$.

For this, let us first consider the tautological line bundle $\gamma\subseteq\CP^n\times\mathbb{C}^{n+1}$ defined over it. This is the restriction of the universal line bundle $\gamma$ of [Example 8](#ex8) via $\CP^n\hookrightarrow\CP^\infty$, and since the cell structure has cells only in even dimensions, the restriction $H^k(\CP^\infty;\mathbb{Z})\rightarrow H^k(\CP^n;\mathbb{Z})$ is an isomorphism for $k\leq 2n$. Therefore, setting $\x=c_1(\bar{\gamma})=-c_1(\gamma)$ by [Proposition 10](#prop10),

$$H^\bullet(\CP^n;\mathbb{Z})=\mathbb{Z}[\x]/(\x^{n+1})$$

holds.

Now consider the tangent bundle. A point $\ell\in\CP^n$ of this space is a line $\ell\subseteq\mathbb{C}^{n+1}$, and fixing a Hermitian inner product, lines near $\ell$ are uniquely represented as graphs of linear maps $\ell\rightarrow\ell^\perp$. That is, writing the bundle of $\mathbb{C}$-linear maps fiberwise as $\Hom$,

$$T\CP^n\cong\Hom(\gamma,\gamma^\perp)$$

holds. Adding the trivial line bundle $\Hom(\gamma,\gamma)$ by Whitney sum,

$$T\CP^n\oplus\Hom(\gamma,\gamma)\cong\Hom(\gamma,\gamma^\perp\oplus\gamma)\cong\Hom(\gamma,\varepsilon^{n+1})\cong\Hom(\gamma,\varepsilon^1)^{\oplus(n+1)}$$

holds. Here $\varepsilon^{n+1}$ is the rank $n+1$ trivial bundle. Therefore, identifying $\Hom(\gamma, \varepsilon^1)$ on the right-hand side with $\overline{\gamma}$, we obtain from [Theorem 9](#thm9) the identity

$$c(T\CP^n)=c\bigl(T\CP^n\oplus\Hom(\gamma,\gamma)\bigr)=c(\bar{\gamma})^{n+1}=(1+\x)^{n+1},$$

and expanding this, since $H^\bullet(\CP^n)=\mathbb{Z}[\x]/(\x^{n+1})$,

$$c(T\CP^n)=(n+1)\x^n+\cdots +1$$

holds.
:::

## Pontryagin Classes

For real vector bundles as well, $\mathbb{Z}$-coefficient invariants can be obtained via complex Chern classes.

::: Definition 12
The *Pontryagin class* $p_i(E)\in H^{4i}(B;\mathbb{Z})$ of a real vector bundle $E\rightarrow B$ is defined by the Chern class of the complexification $E\otimes_{\mathbb{R}}\mathbb{C}$ as

$$p_i(E)=(-1)^i c_{2i}(E\otimes_{\mathbb{R}}\mathbb{C}).$$
:::

The complexification $E\otimes_{\mathbb{R}}\mathbb{C}$ is isomorphic to its conjugate $\overline{E\otimes\mathbb{C}}$ via $v\otimes z\mapsto v\otimes\bar{z}$. Then by [Proposition 10](#prop10), $c_{2i+1}(E\otimes\mathbb{C})=-c_{2i+1}(E\otimes\mathbb{C})$, that is, the odd Chern classes all become $2$-torsion ($2c_{2i+1}=0$) and thus carry no essential information. For this reason we define the $i$-th class using only the even Chern classes (with sign), and since Chern classes live in cohomology of index twice their own number, Pontryagin classes end up living in $H^{4i}(B;\mathbb{Z})$. Intuitively, this can be thought of as bringing what Stiefel–Whitney classes did over $\mathbb{Z}/2$ to $\mathbb{Z}$-coefficients (without passing to complex vector bundles), or as bringing down what Chern classes did for complex vector bundles to real vector bundles.

The basic properties also descend from Chern classes via complexification. The total Pontryagin class is written as $p(E)=1+p_1(E)+p_2(E)+\cdots$.

::: Proposition 13
For real vector bundles $E,F\rightarrow B$, the following hold.

1. (Naturality) For any $f:B'\rightarrow B$, $p(f^\ast E)=f^\ast p(E)$.
2. (Whitney) $2\bigl(p(E\oplus F)-p(E)\smile p(F)\bigr)=0$. In particular, if $H^\bullet(B;\mathbb{Z})$ has no $2$-torsion, then $p(E\oplus F)=p(E)\smile p(F)$.
3. For a complex vector bundle $E$, $E_{\mathbb{R}}\otimes_{\mathbb{R}}\mathbb{C}\cong E\oplus\bar{E}$, and therefore $p_i(E_{\mathbb{R}})$ is a polynomial in the Chern classes of $E$. For instance, $p_1(E_{\mathbb{R}})=c_1(E)^2-2c_2(E)$.
:::
::: Proof
(1) follows immediately from the fact that complexification commutes with pullback and naturality from [Proposition 7](#prop7). (2) also follows by applying [Theorem 9](#thm9) to $(E\oplus F)\otimes\mathbb{C}\cong(E\otimes\mathbb{C})\oplus(F\otimes\mathbb{C})$: as observed below [Definition 12](#def12), the odd Chern classes are all $2$-torsion, so the terms involving them vanish upon multiplication by $2$, and the remaining even terms give $p(E)\smile p(F)$.

Only (3) requires a small calculation. When we complexify $E_{\mathbb{R}}\otimes\mathbb{C}$, the complex structure emerges as $J\in \End(E_{\mathbb{R}})$. Extending this $\mathbb{C}$-linearly, its $\pm i$ eigenspace decomposition gives $E_{\mathbb{R}}\otimes\mathbb{C}\cong E\oplus\bar{E}$. Then by [Theorem 9](#thm9) and [Proposition 10](#prop10), $c_2(E_{\mathbb{R}}\otimes\mathbb{C})=c_2(E\oplus\bar{E})=2c_2(E)-c_1(E)^2$, and bringing this down to the Pontryagin class gives the desired result.
:::

---

**References**

**[MS]** J. W. Milnor and J. D. Stasheff, *Characteristic Classes*, Annals of Mathematics Studies 76, Princeton University Press, 1974.  
**[BT]** R. Bott and L. W. Tu, *Differential Forms in Algebraic Topology*, Springer, 1982.  
**[Hat]** A. Hatcher, *Vector Bundles and K-Theory*, online notes, 2017.

---
[^1]: View $S^\infty$ as the unit sphere in $\mathbb{C}^\infty=\bigcup_n\mathbb{C}^n$. For the shift morphism $T(x_1,x_2,\ldots)=(0,x_1,x_2,\ldots)$, the two straight line homotopies $x\mapsto\bigl((1-t)x+tT(x)\bigr)/\lvert(1-t)x+tT(x)\rvert$ and $x\mapsto\bigl((1-t)T(x)+te_1\bigr)/\lvert(1-t)T(x)+te_1\rvert$, with vectors normalized by $v\mapsto v/\lvert v\rvert$, respectively connect the identity to $T$, and $T$ to the constant map $x\mapsto e_1=(1,0,\ldots)$. Neither denominator becomes zero: for the former, the coordinates of $x$ and $T(x)$ are shifted by one so $(1-t)x+tT(x)=0$ forces $x=0$, and for the latter, the first coordinate of the sum is $t$ so for it to be $0$ we need $t=0$, which then gives $T(x)=0$, that is, $x=0$. Joining these two shows that $S^\infty$ contracts to a point.
