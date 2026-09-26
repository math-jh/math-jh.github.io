---
title: "Moduli Space of Stable Maps"
description: "We examine the proper Deligne-Mumford stack of stable maps along with its natural morphisms and boundary structure, and compute the virtual dimension from the exact sequence of deformations and obstructions."
excerpt: "Moduli of stable maps, Deligne-Mumford stacks, virtual dimensions, and convex targets"

categories: [Math / Gromov-Witten Theory]
permalink: /en/math/gromov-witten_theory/moduli_of_stable_maps
sidebar: 
    nav: "gromov-witten_theory-en"

date: 2026-09-14
weight: 2
translated_at: 2026-09-18T11:15:05+00:00
translation_source: antigravity-gemini-3.8-flash-high
---
Although we have already seen the importance of the properness of moduli spaces in [\[Stacks\] §Proper Stacks](/en/math/stacks/proper_stacks){: data-lid="5ib31" }, we cannot expect such a property in general enumerative problems. Among problems of this kind, a classical one is counting curves in $\mathbb{P}^2$ passing through $3d-1$ general points that are degree $d$ rational curves; for example, when $d=2$, it is known that this value is $1$. That is, a curve in $\mathbb{P}^2$ passing through $5$ points must exist uniquely. On the other hand, if we consider the map

$$\mu_t:\mathbb{P}^1\longrightarrow\mathbb{P}^2,\qquad [\u:\v]\longmapsto[-t\u\v:\u(\u-(1+t)\v):\v(\u-(1+t)\v)],\qquad t\neq 0,-1$$

this is a conic satisfying the equation

$$C_t=V(\x\y+t\y\z-(1+t)\x\z)$$

and we can verify that these pass through the four points

$$q_1=[1:0:0],\qquad q_2=[0:1:0],\qquad q_3=[0:0:1],\qquad q_4=[1:1:1]$$

According to the result above, choosing an additional point besides these four points uniquely determines $C_t$; for example, if we choose the last point to be $q_5=[0:1:2]$, the condition $q_5\in C_t$ forces $2t=0$, that is, $t=0$. However, at $t=0$, this curve is $C_0=V(\x(\y-\z))$, which is the union of the two lines $V(\x)$ and $V(\y-\z)$.

This happens because properness fails when considering only smooth rational curves, and to resolve this, limits must be added in some way. Stable maps are what realize this idea. A stable map remembers a curve together with a map $\mu:C\rightarrow X$ and allows nodal curves for the domain, thereby preserving both the split components and the maps on each component in the limit.

In this post, we always take the target $X$ to be a smooth projective variety over the complex numbers $\mathbb{C}$.

## Stable Maps

In the preceding computation, the limit of smooth conics was a curve where two lines meet at a point, so to preserve this as a limit of maps, the domain must also be able to split. Indeed, since the image of $\mathbb{P}^1$ is irreducible, a morphism with the domain fixed to $\mathbb{P}^1$ cannot cover both lines. Instead, if we glue two copies of $\mathbb{P}^1$ at a single point and send each to the corresponding line, the values of the two maps agree at the glued point, yielding a morphism on the entire domain. Therefore, to include such limits, we must broaden the scope of domains from smooth curves to nodal curves.

Incidence conditions can also be recorded as data of a map. The condition that a curve passes through a given point $q_i\in X$ can be specified by designating a point $p_i$ on the domain and requiring $\mu(p_i)=q_i$, so the domains of the maps we desire are precisely all contained in prestable curves. ([§Deformations of Nodal Curves, ⁋Definition 1](/en/math/gromov-witten_theory/deformations_of_nodal_curves#def1){: data-lid="ovp6z" }) In the earlier example, it suffices to mark the point corresponding to each $q_i$ of the limit on the corresponding component, and general incidence conditions are imposed by requiring $\mu(p_i)$ to belong to a designated subvariety.

Now, the issue that arises when we encode data into maps is that when the same curve changes through a different parametrization, it appears as a different map. Thus, we identify them by isomorphisms of domains that preserve the marked points and the map. The problem is that automorphisms can also arise within a single piece of data; generally, the automorphisms we consider are meaningful pieces of information because they represent symmetries of the map itself. However, allowing nodal domains can introduce degrees of freedom in parametrization that add no meaningful information whatsoever. For example, if a $\mathbb{P}^1$ component mapped to a single point has only one node and no marked points, this component has infinitely many automorphisms, yet even if we ignore this component, the information of the rest of the map and marked points remains intact. To rule out such components, we impose the stability condition that the automorphism group is finite, which is the key condition that allows finite symmetries of the map while ensuring that the moduli space becomes a Deligne–Mumford stack. Fixing the curve class $\beta$ in addition, we obtain the following definition.

::: Definition 1
Suppose we are given a genus $g$, $n$-pointed prestable curve $(C,p_1,\ldots,p_n)$ and a class $\beta\in H_2(X,\mathbb{Z})$. A *stable map* is a pair consisting of a prestable curve and a map $\mu$ with this curve as its domain,

$$(C,p_1,\ldots,p_n,\mu),\qquad \mu:C\rightarrow X$$

satisfying the following two conditions:

- $\mu_\ast[C]=\beta$.
- The automorphism group $\Aut(C,p_1,\ldots,p_n,\mu)$ is finite.

Two stable maps are said to be *isomorphic* if there exists an isomorphism of the domains preserving the marked points and the map to $X$.
:::

The first condition means that the sum of the classes of the images, taking into account the mapping degree of each component, equals $\beta$. Looking at the second condition, since the number of automorphisms arising from permutations of distinct components and nodes, or exchanging the two branches of a self-node, is finite, the finiteness of the automorphism group is essentially a condition on the finiteness of the automorphism group of each component of the domain curve.

Fixing such automorphisms means requiring that the marked points and nodes remain fixed; we refer to these two types of points collectively as *special points*. For the domain curve $C$, let the normalization of an irreducible component $C_i$ be $\widetilde{C}_i$, and let the number of special points on $\widetilde{C}_i$ be $s_i$.

Now, if we let the genus of $\widetilde{C}_i$ be $h_i$, the degree of the tangent bundle $\mathcal{T}_{\widetilde{C}_i}$ is $2-2h_i$. If we write the sum of the special points as the divisor $D_i$, then by [§Deformations of Nodal Curves, ⁋Proposition 4](/en/math/gromov-witten_theory/deformations_of_nodal_curves#prop4){: data-lid="paz7d" } and the discussion following it, the infinitesimal automorphisms fixing these points are computed as

$$H^0\bigl(\widetilde{C}_i,\mathcal{T}_{\widetilde{C}_i}(-D_i)\bigr)$$

Since this was equal to the tangent space at the identity of the group of automorphisms of $\widetilde{C}_i$ fixing each of the special points, denoted by $G$, if this dimension is $0$, then the dimension of $G$ at the identity, and furthermore at any point, is $0$. It is generally known that the automorphism group of a smooth projective curve fixing a finite number of points is of finite type, and from this fact we obtain that $G$ is finite.

Now, if $h_i\geq2$, then $\deg\mathcal{T}_{\widetilde{C}_i}=2-2h_i<0$, so there are no global vector fields. ([\[Algebraic Varieties\] §The Riemann–Roch Theorem for Curves, ⁋Proposition 3](/en/math/algebraic_varieties/riemann_roch_theorem#prop3){: data-lid="pq7bu" }) Therefore, in this case, the automorphism group is finite even without special points. This argument does not hold in general for lower genus, where we must reduce the degrees of freedom using the condition that the special points are fixed. First, in the case where $h_i=0$, we have $\widetilde{C}_i\cong\mathbb{P}^1$ and $\mathcal{T}_{\mathbb{P}^1}(-D_i)\cong\mathcal{O}_{\mathbb{P}^1}(2-s_i)$, so the dimension of the space above is $\max\{3-s_i,0\}$, and therefore $s_i$ must be at least $3$. Intuitively, since an automorphism of $\mathbb{P}^1$ is of the form $(az+b)/(cz+d)$, there are $3$ degrees of freedom, and this corresponds to the special points killing these degrees of freedom one by one. In the case where $h_i=1$, the tangent bundle is trivial, so the space of global vector fields has dimension $1$, and killing this requires at least one special point.

In summary, the finiteness of the automorphism group is equivalent, in the situation above, to the condition that

$$2g(\widetilde{C}_i)-2+s_i>0$$

holds. That is, in genus $0$ at least $3$ special points are required, in genus $1$ at least $1$ is required, and in genus $2$ or higher there is no additional condition. This condition applies only when $\mu$ contracts the component $C_i$ to a point; if $\mu$ is nonconstant on $C_i$, the finiteness already follows from the fact that the automorphism group must preserve $\mu$.

::: Example 2
We now examine an actual case where the automorphism group turns out to be (nontrivially) finite. Let $C$ be an irreducible nodal cubic and let $\mu:C\rightarrow X$ be a constant map. The arithmetic genus of $C$ is $1$, but its normalization is $\mathbb{P}^1$. ([\[Algebraic Varieties\] §Tangent Spaces and Smoothness, ⁋Example 7](/en/math/algebraic_varieties/tangent_spaces_and_smoothness#ex7){: data-lid="0htg0" }) If we choose the two points above the node to be $0,\infty$, then in the absence of marked points, every $z\mapsto az$ ($a\in\mathbb{C}^{\times}$) fixes these two points and descends to an automorphism of $C$. Thus this map is not stable, which can also be verified by substituting $h_i=0$, $s_i=2$ into the inequality above. 

Now, if we pick a marked point $p$ on the smooth locus and choose coordinates so that its preimage is $1$, then $s_i=3$, which satisfies the stability condition. However, note that the automorphism group is not the trivial group. That is, the only automorphism fixing each of $0,1,\infty$ is the identity map, but at the initial normalization stage there is the freedom to interchange the two branches of the node; indeed, $z\mapsto1/z$ serves as an automorphism that swaps $0,\infty$ and fixes $1$. That is,

$$\Aut(C,p,\mu)\cong\mathbb{Z}/2$$

On the other hand, the inclusion $C\hookrightarrow\mathbb{P}^2$ of the same nodal cubic is stable even without marked points, since the only automorphism preserving the map is the identity map.
:::

In this way, stability determines whether continuous degrees of freedom remain in the parametrization of each component. On a contracted component, the special points constrain this freedom, while on a nonconstant component, the map itself constrains it. As in the example of the nodal cubic, finite symmetries can remain, and recording even these symmetries is why we treat the moduli of stable maps as a Deligne–Mumford stack.

## Moduli Space of Stable Maps

As seen in [Example 2](#ex2){: data-lid="nr248" }, a stable map can have nontrivial automorphisms. Therefore, the space collecting stable maps is treated as a stack that remembers even the automorphisms of the map represented by each point. For a fixed genus $g$, number of marked points $n$, and effective class $\beta$ (that is, a class given by a sum of homology classes of irreducible curves in $X$ with non-negative integer coefficients), we denote by

$$\overline{\mathcal{M}}_{g,n}(X,\beta)$$

the stack consisting of families of stable maps and isomorphisms between them. The isomorphism classes of geometric points of this stack correspond to the isomorphism classes of stable maps, and the stabilizer of each point is the automorphism group of the corresponding stable map.

::: Proposition 3
If $\beta$ is an effective class, then $\overline{\mathcal{M}}_{g,n}(X,\beta)$ is a proper Deligne–Mumford stack ([\[Stacks\] §Algebraic Stacks, ⁋Definition 6](/en/math/stacks/algebraic_stacks#def6){: data-lid="r3t1v" }), and its coarse moduli space is a projective scheme. ([\[Stacks\] §Moduli Spaces, ⁋Definition 7](/en/math/stacks/moduli_spaces#def7){: data-lid="d7w0d" })
:::

The reason properness was needed in the introduction is that the limit of curves must remain in the moduli when varying the given conditions, and the proposition above shows that $\overline{\mathcal{M}}_{g,n}(X,\beta)$ is a moduli space satisfying such a condition. For instance, if the image splits into two in the conic calculation of the introduction, we can also divide its domain into two components, so this is no longer an issue. On the other hand, problematic limits do not arise only in such situations; for example, when two marked points collide into a single point, the limit does not naively stay inside $\overline{\mathcal{M}}_{g,n}(X,\beta)$. In this case, we remember the original configuration by attaching a $\mathbb{P}^1$ component at this collision point and placing the two colliding marked points on this component. At this time, the newly created $\mathbb{P}^1$ component is mapped via $\mu$ to the image of the collision point $\mu(p)$, and since this component has one node and two marked points, the stability condition is still satisfied.

Rigorously, this can be understood by considering a family of curves. To this end, locally near the collision point, we use a parameter $\t$ to parameterize a family of curves $C_\t$, and suppose that the two marked points collide at the central fiber $\t=0$. In this picture, the family of curves is $S\rightarrow \mathbb{A}^1_\t$ whose total space is a surface, and the trajectory of each marked point appears as two sections of this projection; hence, the collision of the two marked points at $\t=0$ can be understood as these sections having an intersection at $\t=0$. For example, if we let the local coordinate of each fiber be $\z$ and take the two sections to be $\z=0$ and $\z=\t$, these two sections have an intersection at $(\z,\t)=(0,0)$. The standard way to resolve the collision in such a situation is a blowup: the bubble $\mathbb{P}^1$ attached above is precisely the exceptional curve of this blowup, and in the blowup coordinate $\u=\z/\t$, the strict transforms of the two sections become $\u=0,\u=1$, so that two distinct marked points appear on this component. In our example, since the two sections met to first order, a single blowup was sufficient, but when these sections meet to higher order, one must repeat blowups until they are separated. However, the intermediate components created in this process do not satisfy stability and are contracted to a point, so the final picture is identical to the one described above.

Now, on this moduli stack $\overline{\mathcal{M}}_{g,n}(X,\beta)$, there exist several natural morphisms. First, the *evaluation map*, which reads off the image of each marked point, is defined by

$$\ev_i:\overline{\mathcal{M}}_{g,n}(X,\beta)\rightarrow X,\qquad (C,p_\bullet,\mu)\mapsto\mu(p_i)$$

and its meaning is also clear. In typical enumerative problems, one often imposes incidence conditions that the $i$-th marked point passes through a given subvariety; in such cases, one can simply pull back the class of that subvariety via $\ev_i$.

Another morphism is the *forgetful morphism*, which forgets the last marked point,

$$\pi:\overline{\mathcal{M}}_{g,n+1}(X,\beta)\rightarrow\overline{\mathcal{M}}_{g,n}(X,\beta)$$

which is always defined when $\beta\neq 0$ or $2g-2+n>0$. Since the number of marked points is a variable controlling stability, simply forgetting the last marked point may not result in a stable map; $\pi$ is the morphism that ensures the result is a stable map by also including the stabilization process that contracts such unstable components to points, and for this, the aforementioned assumption $\beta\neq 0$ or $2g-2+n>0$ is required. The morphism $\pi$ defined in this way becomes the universal curve over $\overline{\mathcal{M}}_{g,n}(X,\beta)$. ([\[Stacks\] §Moduli Spaces, §§Moduli Functors](/en/math/stacks/moduli_spaces#moduli-functors){: data-lid="r8e2o" }) In fact, if for convenience we fix a stable map, that is, a point of $\overline{\mathcal{M}}_{g,n}(X,\beta)$, and look at the fiber of $\pi$ over it, determining a section from this point to the fiber is precisely the same as choosing where to place the last marked point on this stable map, and therefore the fiber over this point turns out to be the domain curve of that stable map.

Finally, if $2g-2+n>0$, we can stabilize to a pointed curve that is stable even without the map. In this case, after forgetting the map to $X$, contracting the components that are unstable as pointed curves yields

$$\overline{\mathcal{M}}_{g,n}(X,\beta)\rightarrow\overline{\mathcal{M}}_{g,n},\qquad (C,p_\bullet,\mu)\mapsto(C,p_\bullet)^{\mathrm{stab}}$$
.

When explaining properness earlier, we saw that a family of stable maps with smooth domains can degenerate into a stable map with a nodal domain, so such limits must also be included in the moduli. Now we call the locus of such nodal domains the *boundary*, and describe it by separating the domain at the nodes and then gluing them back together. First, when separating the two branches of a single node, if the curve splits into two connected curves and $\{1,\ldots,n\}=A\sqcup B$, $g=g_1+g_2$, $\beta=\beta_1+\beta_2$, the gluing morphism is

$$\overline{\mathcal{M}}_{g_1,A\cup\{\bullet\}}(X,\beta_1)\times_X\overline{\mathcal{M}}_{g_2,B\cup\{\bullet\}}(X,\beta_2)\rightarrow\overline{\mathcal{M}}_{g,n}(X,\beta)$$
.
Since the evaluations of the newly attached marked points $\bullet$ on the two factors must agree to glue them into a single node, the fiber product is formed over $X$. At this time, the source distinguishes the two curves before gluing as first and second, but the glued result does not remember their order. Therefore, when the genus, marking, and class data of the two factors are identical so that they can be interchanged, this morphism may not be isomorphic to its image. Furthermore, on a curve with multiple nodes, one may choose different nodes that yield the same decomposition data, and in this case as well, different gluing data can yield the same stable map. This is the situation where different local branches of the boundary meet.

On the other hand, even after separating the two branches of a node, the curve may still be connected. The irreducible nodal cubic in [Example 2](#ex2){: data-lid="vz072" } is precisely such a case: resolving the node does not split the curve into two, but instead on a single $\mathbb{P}^1$, two points $0,\infty$ appear. In general, resolving the node in this case reduces the arithmetic genus by one, so we attach two marked points on a connected curve of genus $g-1$. The corresponding gluing morphism is

$$\overline{\mathcal{M}}_{g-1,n+2}(X,\beta)\times_{X\times X}X\rightarrow\overline{\mathcal{M}}_{g,n}(X,\beta)$$

and $X\rightarrow X\times X$ is the diagonal. Here again, the source distinguishes the order of the last two marked points, but the glued result does not remember it. In Example 2, $z\mapsto1/z$ interchanges these two points, so before gluing it is not an automorphism preserving each marked point, but after gluing it becomes an automorphism of the stable map.

## Virtual dimension
{: #virtual-dimension }

In general, $\overline{\mathcal{M}}_{g,n}(X,\beta)$ is not smooth, and even with $g,n,\beta$ fixed, it can have multiple irreducible components. Moreover, these components may meet each other, and their respective dimensions may also differ.

On the other hand, if we denote the infinitesimal deformation space of a stable map $(C,p_\bullet,\mu)$ by $T^1$ and the obstruction space by $T^2$, this deformation–obstruction theory defines the *virtual dimension*

$$\vdim=\dim T^1-\dim T^2$$
.
Intuitively, $T^1$ contains the first-order directions in which the given stable map can move within the moduli, so it is roughly like a tangent space, but the problem lies in the fact that there is no guarantee that motions appearing possible to first order lead to an actual family. Since the obstruction to such an extension is an element of $T^2$, if we think of the coordinates of $T^1$ as variables, the vanishing of the obstruction can be understood as imposing equations on these variables taking values in $T^2$. The virtual dimension is thus the number of variables minus the number of equations. Since each equation lowers the dimension by at most $1$, the actual dimension is greater than or equal to the virtual dimension, and can be strictly larger if the equations do not act independently.

To compute this in practice, we first consider the natural morphism defined by $\mu:C\rightarrow X$, namely $\mu^\ast\Omega_X\rightarrow\Omega_C$. The dual of this morphism sends a vector field $v$ on the domain to the infinitesimal variation $\dd{\mu}(v)$ of the map, which is the first-order change induced on the map by an infinitesimal reparametrization of the domain. That is, if we denote the infinitesimal automorphism corresponding to $v$ by $\varphi_\epsilon$, the first-order change of $\mu\circ\varphi_\epsilon$ is $\dd{\mu}(v)$. When considering stable maps, we must reflect the marked points here, so we compose this with $\Omega_C\rightarrow\Omega_C(p_1+\cdots+p_n)$. Here,

$$\Hom_C(\Omega_C(p_1+\cdots+p_n),\mathcal{O}_C)$$

contains derivations that vanish at the marked points, and therefore records the infinitesimal automorphisms of the domain fixing the marked points. We write the two-term complex obtained in this way as

$$\LL_\mu=\Bigl[\at{-1}{\mu^\ast\Omega_X}\longrightarrow\at{0}{\Omega_C(p_1+\cdots+p_n)}\Bigr]$$
.
Intuitively, this incorporates the twist by the marked points into the domain term of the two-term model representing the relative cotangent complex of $\mu:C\rightarrow X$; by the standard interpretation in deformation theory, in the problem of deforming the pointed domain and the map together while fixing $X$,

$$T^i=H^i\bigl(R\Hom_C(\LL_\mu,\mathcal{O}_C)\bigr)=\Ext_C^i(\LL_\mu,\mathcal{O}_C)$$

gives the deformation space $T^1$ and the obstruction space $T^2$. Through this, we obtain the following exact sequence.

::: Proposition 4
For a stable map $(C,p_\bullet,\mu)$, the deformation space $T^1$ and obstruction space $T^2$ fit into the exact sequence

$$\begin{aligned}
0&\rightarrow\Ext_C^0\left(\Omega_C(p_1+\cdots+p_n),\mathcal{O}_C\right)\rightarrow H^0(C,\mu^\ast T_X)\rightarrow T^1 \\
&\rightarrow\Ext_C^1\left(\Omega_C(p_1+\cdots+p_n),\mathcal{O}_C\right)\rightarrow H^1(C,\mu^\ast T_X)\rightarrow T^2\rightarrow0
\end{aligned}$$

Therefore, the virtual dimension of $\overline{\mathcal{M}}_{g,n}(X,\beta)$ is

$$\vdim=\int_\beta c_1(T_X)+(\dim X-3)(1-g)+n$$

:::

Here, the first $\Ext^0$ is the infinitesimal automorphisms of the pointed domain, and $H^0(C,\mu^\ast T_X)$ is the deformations of the map with the domain fixed. The next $\Ext^1$ is the deformations of the pointed domain, and from $H^1(C,\mu^\ast T_X)$ we read the obstructions to gluing local deformations of the map.

::: Proof
Applying to $\LL_\mu$ defined above the functor $R\Hom_C(-,\mathcal{O}_C)$ yields the exact sequence above. The kernel of the first morphism consists of those infinitesimal automorphisms of the pointed domain that also preserve the map; by stability, this kernel is $0$, so $0$ is attached to the left of the sequence.

Now let $E=\mu^\ast T_X$ and $A^i=\Ext_C^i(\Omega_C(p_1+\cdots+p_n),\mathcal{O}_C)$. Since the alternating sum of dimensions in the exact sequence above is $0$, this decomposes as

$$\dim T^1-\dim T^2=\bigl(\dim A^1-\dim A^0\bigr)+\rchi(C,E)$$

Here, the first term in parentheses is the difference between the dimensions of the deformation space and the infinitesimal automorphism space of the pointed domain, so by [§Deformations of Nodal Curves, ⁋Corollary 6](/en/math/gromov-witten_theory/deformations_of_nodal_curves#cor6){: data-lid="5ao1g" }, it is $3g-3+n$.

For the second term, first, on a smooth projective curve $Y$, for a rank $r$ vector bundle $F$, the vector bundle version of [\[Algebraic Varieties\] §The Riemann–Roch Theorem for Curves, ⁋Proposition 3](/en/math/algebraic_varieties/riemann_roch_theorem#prop3){: data-lid="ol72u" } gives

$$\rchi(Y,F)=\deg F+r(1-g(Y))$$

Although our domain $C$ is not a smooth curve, we can transfer this calculation via the normalization $\nu:\widetilde{C}=\coprod_{j=1}^c\widetilde{C}_j\rightarrow C$. Let the genus of each $\widetilde{C}_j$ be $h_j$, the number of nodes be $d$, and the rank of $E$ be $r$. Tensoring the normalization exact sequence of the structure sheaf (immediately after [§Deformations of Nodal Curves, ⁋Definition 1](/en/math/gromov-witten_theory/deformations_of_nodal_curves#def1){: data-lid="uihgw" }) with the locally free sheaf $E$, we obtain

$$0\rightarrow E\rightarrow\nu_\ast\nu^\ast E\rightarrow\bigoplus_{q\in\Sing C}E\otimes_{\mathcal{O}_C}\kappa(q)\rightarrow0$$

Using this, we have

$$\rchi(C,E)=\sum_{j=1}^c\rchi(\widetilde{C}_j,\nu^\ast E\vert_{\widetilde{C}_j})-rd=\sum_{j=1}^c\left(\deg(\nu^\ast E\vert_{\widetilde{C}_j})+r(1-h_j)\right)-rd=\deg E+r\left(c-\sum_{j=1}^c h_j-d\right)=\deg E+r(1-g)$$

and substituting $E=\mu^\ast T_X$ into this formula, since $\rank E=\dim X$ and $\mu_\ast[C]=\beta$, we obtain

$$\deg E=\int_C\mu^\ast c_1(T_X)=\int_\beta c_1(T_X)$$

Finally, combining all these calculations, we obtain

$$\dim T^1-\dim T^2=(3g-3+n)+\int_\beta c_1(T_X)+\dim X(1-g)=\int_\beta c_1(T_X)+(\dim X-3)(1-g)+n$$
:::

## Examples

As mentioned above, the virtual dimension is always less than or equal to the actual dimension. A representative case where the virtual dimension equals the actual dimension is when the target $X$ is convex, for genus $0$ stable maps. Here, a smooth projective variety $X$ is said to be *convex* if for every morphism $\mu:\mathbb{P}^1\rightarrow X$, we have $H^1(\mathbb{P}^1,\mu^\ast T_X)=0$.

::: Proposition 5
If $X$ is convex, then for any effective $\beta$ and $n\geq0$, $\overline{\mathcal{M}}_{0,n}(X,\beta)$ is a smooth proper Deligne–Mumford stack of virtual dimension

$$\int_\beta c_1(T_X)+\dim X-3+n$$
:::

Although convexity is a condition on a smooth $\mathbb{P}^1$, one can show that for a nodal genus $0$ curve we also have $H^1(C,\mu^\ast T_X)=0$. Therefore, by [Proposition 4](#prop4){: data-lid="qh7wb" }, we see that $T^2=0$. A representative example of such a convex target is a homogeneous space $G/P$; in this case, convexity holds because $T_{G/P}$ is globally generated.

::: Example 6
Let $X=\mathbb{P}^r$, $g=0$, $n=0$, and $\beta=[\text{line}]$. A degree $1$ stable map sends $\mathbb{P}^1$ isomorphically to a line in $\mathbb{P}^r$, and the freedom of parametrization is absorbed by $\Aut(\mathbb{P}^1)$. Therefore, the remaining data is the line itself, and we have

$$\overline{\mathcal{M}}_{0,0}(\mathbb{P}^r,1)\cong\Gr(2,r+1)$$

The dimension of this Grassmannian is $2(r+1-2)=2r-2$, and since $c_1(T_{\mathbb{P}^r})=(r+1)H$, the virtual dimension is also

$$\vdim=(r+1)+(r-3)=2r-2$$

so we can verify that the two values agree.
:::

Applying the same calculation to $\overline{\mathcal{M}}_{0,0}(\mathbb{P}^2,2)$ yields

$$\vdim=\int_{2[\text{line}]}c_1(T_{\mathbb{P}^2})+(2-3)=6-1=5$$

Since $\mathbb{P}^2$ is convex, this value coincides with the actual dimension.

---

**References**

**[FP]** W. Fulton, R. Pandharipande, *Notes on stable maps and quantum cohomology*, in *Algebraic Geometry, Santa Cruz 1995*, Proc. Sympos. Pure Math. **62**, Part 2, AMS, 1997, pp. 45–96.  
**[HKK+]** K. Hori, S. Katz, A. Klemm, R. Pandharipande, R. Thomas, C. Vafa, R. Vakil, E. Zaslow, *Mirror Symmetry*, Clay Mathematics Monographs **1**, AMS, 2003.
