---
title: "Proper Stacks"
description: "We define separatedness and properness for algebraic stacks via the diagonal and discuss the valuative criterion allowing finite base change. We also explore the relationship with coarse moduli spaces."
excerpt: "Proper Deligne–Mumford stacks, their valuative criterion, and coarse moduli spaces"

categories: [Math / Stacks]
permalink: /en/math/stacks/proper_stacks
sidebar:
    nav: "stacks-en"

date: 2026-09-15
weight: 5
translated_at: 2026-09-18T23:15:04+00:00
translation_source: antigravity-gemini-3.8-flash-high
---
In the previous post, we looked at moduli spaces. The most elementary example of a moduli space is the Grassmannian examined in [§Moduli Spaces, ⁋Example 3](/en/math/stacks/moduli_spaces#ex3){: data-lid="mn8sm" }; through this, let us see how moduli spaces are used. 

In [\[Algebraic Topology\] §Stiefel-Whitney Characteristic Classes, ⁋Example 7](/en/math/algebraic_topology/stiefel_whitney_classes#ex7){: data-lid="4kw71" data-relation="weak" }, by intersecting two Schubert cycles on $\Gr(2,\mathbb{R}^4)$ in general position, we directly computed the cohomology relation

$$\sigma_{(1,0)}\smile\sigma_{(1,0)}=\sigma_{(1,1)}+\sigma_{(2,0)}$$

The same relation holds in the complex Grassmannian $\Gr(2,\mathbb{C}^4)$, and by projectivizing it, we can identify $\Gr(2,\mathbb{C}^4)$ with the space of lines in $\mathbb{P}^3$. Now, if we let the Schubert divisor of lines meeting a given line $A\subseteq\mathbb{P}^3$ be $\Omega_A$, the left-hand side represents the locus of lines meeting both lines $A,B$, namely $\Omega_A\cap\Omega_B$. If we move the line $B$ so that it meets $A$ at a point $p$, the condition of passing through both $A$ and $B$ simultaneously allows two possibilities: being contained in the plane spanned by $A,B$, or passing through the intersection of $A,B$, and this is precisely what the above formula means.

This specialization also shows why the Grassmannian is a good moduli space of lines. For example, for two skew lines $A,B$ and points $p,q$, consider a line $C$ meeting them respectively at these points. This is uniquely determined by precisely the two points $p,q$, but if, as explained above, we move the point on $B$, $q$, to the point on $A$, $p$, then since a single point $p$ alone cannot specify a line, the component contributed by this limit could have disappeared. Nevertheless, the fact that this component remains is precisely the $\sigma_{(2,0)}$ part examined above, and in algebraic geometry, ensuring that such limits exist was the notion of properness. ([\[Schemes\] §Valuation Rings, ⁋Theorem 11](/en/math/scheme_theory/valuative_criteria#thm11){: data-lid="mvpod" data-relation="weak" })

In this post, we define what it means for an algebraic stack to be proper and examine its properties. Unless stated otherwise, the Deligne–Mumford stacks treated in this post are assumed to be of finite type and quasi-separated over a field $\mathbb{K}$.

## Properness

As with many properties discussed in scheme theory, properness was a property of scheme morphisms rather than of schemes themselves, and we defined an $S$-scheme $X$ to be proper by using this to mean that the structure morphism $X\rightarrow S$ is proper. Conveniently, we know that for a representable stack morphism, we can directly assign the property $P$ as a scheme morphism. ([§Algebraic Stacks, ⁋Definition 4](/en/math/stacks/algebraic_stacks#def4){: data-lid="asugv" data-relation="required" })

However, there is a point to be careful about here. Unlike in scheme theory, where a separated morphism was defined as one whose diagonal is a closed embedding ([\[Schemes\] §Valuation Rings, ⁋Definition 3](/en/math/scheme_theory/valuative_criteria#def3){: data-lid="y52r9" data-relation="required" }), on a stack the diagonal cannot be a monomorphism due to automorphisms of objects. Instead, since a closed embedding is a proper monomorphism (the discussion immediately following [\[Schemes\] §Valuation Rings, ⁋Corollary 13](/en/math/scheme_theory/valuative_criteria#cor13){: data-lid="68l54" data-relation="required" }), we define a morphism of algebraic stacks $f: \mathcal{X}\rightarrow \mathcal{Y}$ to be separated to mean that the *morphism between algebraic spaces* $\Delta_f$ is proper, and after that, we define a *morphism between algebraic stacks* $f: \mathcal{X}\rightarrow \mathcal{Y}$ to be proper as usual by using this definition of separatedness. ([\[Schemes\] §Valuation Rings, ⁋Theorem 11](/en/math/scheme_theory/valuative_criteria#thm11){: data-lid="xmsvo" data-relation="weak" })

::: Definition 1
Suppose we are given two algebraic stacks $\mathcal{X}$, $\mathcal{Y}$ and a morphism $f: \mathcal{X}\rightarrow \mathcal{Y}$ between them. 

1. We say that $f$ is *separated* if the diagonal $\Delta_f$ is proper. 
2. We say that $f$ is *proper* if $f$ is of finite type, separated, and universally closed. 

In particular, when the structure morphism $\mathcal{X}\rightarrow\Spec\mathbb{K}$ is separated or proper, we call $\mathcal{X}$ a separated or proper algebraic stack, respectively.
:::

As explained above, the only difference that arises when passing to stacks is that separatedness of $f$ requires properness of the diagonal; if $f$ were a morphism between schemes or algebraic spaces, the diagonal is a monomorphism, so this definition precisely preserves the original condition. 

Recall that for a general stack, given a geometric point $x:\Spec\mathbb{K}\rightarrow\mathcal{X}$, the stabilizer $\rAut_\mathbb{K}(x)$ was obtained as the fiber of the diagonal $\Delta_\mathcal{X}:\mathcal{X}\rightarrow\mathcal{X}\times_\mathbb{K}\mathcal{X}$ base-changed along $(x,x):\Spec\mathbb{K}\rightarrow\mathcal{X}\times_\mathbb{K}\mathcal{X}$ ([§Algebraic Stacks, ⁋Proposition 5](/en/math/stacks/algebraic_stacks#prop5){: data-lid="iyskn" data-relation="weak" }). In the case of a Deligne–Mumford stack, since this diagonal is unramified, the stabilizer $\rAut_\mathbb{K}(x)$ obtained by base change is also an unramified group scheme over $\mathbb{K}$, and thus it is a locally quasi-finite group scheme. If in addition $\mathcal{X}$ is separated, the diagonal is proper, so the automorphism group is also proper. Since a proper morphism is quasi-compact, the locally quasi-finite $\rAut_{\mathbb{K}}(x)$ is quasi-finite, and hence by the fact that a proper quasi-finite morphism is finite, $\rAut_{\mathbb{K}}(x)$ is a finite group scheme over $\mathbb{K}$. Furthermore, since this is unramified, it is in fact a finite étale group scheme.

## Valuative criterion

Just as we checked separatedness and universally closedness for schemes using valuation rings rather than verifying them directly ([\[Schemes\] §Valuation Rings, ⁋Theorem 6](/en/math/scheme_theory/valuative_criteria#thm6){: data-lid="0ahsc" data-relation="weak" }, [⁋Theorem 11](/en/math/scheme_theory/valuative_criteria#thm11){: data-lid="j8m6v" data-relation="weak" }), the key tool for determining the properness of an object in stacks is the valuative criterion via discrete valuation rings. 

Let $A$ be a complete discrete valuation ring with fraction field $K$, and write the generic point inclusion as $j:\Spec K\rightarrow\Spec A$. For $\mathcal{X}$, a $K$-object $\xi_K$ is the same data as a morphism $\Spec K\rightarrow\mathcal{X}$. In schemes, extending this over $A$ meant having $j^\ast\xi_A=\xi_K$ hold for some $A$-point, but for stacks, instead of diagrams commuting strictly, one must properly keep track of isomorphisms in the $2$-categorical sense. That is, extending this over $A$ means providing $\xi_A\in\mathcal{X}(A)$ together with a specified isomorphism

$$\alpha:j^\ast\xi_A\xrightarrow{\sim}\xi_K$$

and in the valuative criterion for stacks, we must retain this datum of the $2$-isomorphism $\alpha$.

::: Theorem 2 (Valuative criterion)
For a Deligne–Mumford stack $\mathcal{X}$ over $\mathbb{K}$ that is of finite type and quasi-separated, the following two conditions are equivalent.

1. $\mathcal{X}$ is proper.

2. For any complete discrete valuation ring $A$ over $\mathbb{K}$ with fraction field $K$, the following existence and uniqueness hold.

   **Existence.** For any $\xi_K\in\mathcal{X}(K)$, there exist a finite field extension $K'/K$ and, dominating $A$, a discrete valuation ring $A'\subseteq K'$ such that for some $\xi_{A'}\in\mathcal{X}(A')$, an isomorphism

   $$\alpha:\xi_{A'}\vert_{K'}\xrightarrow{\sim}\xi_K\vert_{K'}$$

   exists.

   **Uniqueness.** Given two objects $\xi_A,\eta_A\in\mathcal{X}(A)$ and a *specified* isomorphism on the generic fiber

   $$\varphi_K:\xi_A\vert_K\xrightarrow{\sim}\eta_A\vert_K$$

   there exists a unique isomorphism having $\varphi_K$ as restriction, $\varphi_A:\xi_A\xrightarrow{\sim}\eta_A$.
:::

That is, the valuative criterion for stacks is designed to preserve both the limits in moduli and the automorphism data simultaneously, by properly replacing the $1$-categorical formulation with $2$-isomorphisms.

::: Example 3 (Classifying stack of a finite group)
Assuming $\ch \mathbb{K}$ does not divide the natural number $n\geq 2$, consider the finite étale group scheme $G=\mu_n$. We have already seen that the classifying stack $\bB G=[\Spec\mathbb{K}/G]$ is a Deligne–Mumford stack classifying $G$-torsors. ([§Algebraic Stacks, ⁋Definition 7](/en/math/stacks/algebraic_stacks#def7){: data-lid="autqs" data-relation="required" }) We can verify that $\bB G$ is proper via the valuative criterion in [Theorem 2](#thm2){: data-lid="v8dlh" data-relation="required" }.

First, in the case of uniqueness, between two $G$-torsors $P_A, Q_A$, the scheme $\rIsom_A(P_A, Q_A)$ is a finite étale scheme over $\Spec A$, so an isomorphism $\varphi_K:P_A\vert_K\xrightarrow{\sim} Q_A\vert_K$ of the generic fibers extends uniquely over all of $A$ to $\varphi_A:P_A\xrightarrow{\sim} Q_A$.

On the other hand, for existence, any $G$-torsor $P_K\rightarrow\Spec K$ is a finite étale scheme, so it admits a section over a suitable finite extension $K'/K$. A $G$-torsor admitting a section is trivial, so $P_K\vert_{K'}\cong G\times\Spec K'$, which immediately extends over $A'$ to the trivial torsor $G\times\Spec A'$. For instance, over $A=\mathbb{K}[[t]]$ and $K=\mathbb{K}((t))$, the $\mu_n$-torsor

$$P_K=\Spec K[u]/(u^n-t)$$

is not trivial over $K$ and thus does not directly extend over $A$; however, with $t=s^n$, over $K'=\mathbb{K}((s))$ it is identified via $u=s$ with the trivial torsor, extending over $A'=\mathbb{K}[[s]]$.
:::

## Coarse Moduli Space and Quotient Chart

Since a separated Deligne–Mumford stack of finite type has a finite inertia stack, we can now see that the first assertion of [§Moduli Spaces, ⁋Theorem 8](/en/math/stacks/moduli_spaces#thm8){: data-lid="4iyk3" data-relation="required" } implies the second assertion. We write this as

$$\pi:\mathcal{X}\longrightarrow X$$

In characteristic $0$, over the field $\mathbb{K}$, the stabilizers are finite linearly reductive groups, and the coarse morphism étale-locally takes the form of a finite group quotient.

::: Proposition 4 (Local quotient chart)
Over a characteristic $0$ field $\mathbb{K}$, consider a separated, finite type Deligne–Mumford stack $\mathcal{X}$ and the coarse moduli of $\mathcal{X}$, $\pi: \mathcal{X}\rightarrow X$. For any geometric point of $\mathcal{X}$, $x\rightarrow\mathcal{X}$, and its stabilizer $G_x$, there exist an étale neighborhood of $\bar{x}=\pi(x)$, $U\rightarrow X$, and an affine scheme $V$ equipped with a $G_x$-action such that

$$\mathcal{X}\times_X U\cong[V/G_x],\qquad U\cong V/G_x$$

holds. Furthermore, if $\mathcal{X}$ is smooth, then $V$ can also be chosen to be smooth.
:::

This may well be called a local structure theorem for separated Deligne–Mumford stacks of finite type. That is, a Deligne–Mumford stack is locally represented in the étale topology of its coarse moduli space as a quotient stack by a finite group, and its coarse moduli space can also be thought of as being obtained by gluing the corresponding categorical quotients in the étale topology. In particular, if $\mathcal{X}$ is smooth, then $V$ can be chosen to be smooth, so the coarse moduli space $X$ locally appears in the form of a finite quotient $V/G_x$ of a smooth variety. Consequently, even though $X$ is not smooth in general, it has at most finite quotient singularities.

What is noteworthy is that the group $G_x$ appearing here (even if the original stack is given globally in the form $\mathcal{X}=[M/G]$) need not be equal to this $G$. This can be understood naturally by considering the process of passing from a quotient stack to its coarse moduli.

On the quotient stack $[M/G]$, the action of $G$ contains two types of information simultaneously. One part corresponds to the action that actually moves points on $M$, while the other part is the stabilizer $H$ that fixes the point and remains only as automorphisms of that point. In the process of taking the coarse moduli $M/G$, the former is visible even at the scheme level by identifying all points belonging to a single orbit into a single point, but the latter stabilizer information is lost because the automorphism data attached to the point itself disappears. That is, only the orbits remain in the coarse moduli, and which stabilizer each point originally had is not recorded.

Now, from the viewpoint of the theorem above, if we take a point $x\in\mathcal{X}$ and represent it in a global quotient presentation $[M/G]$ by a point $p\in M$, then the automorphism group of $x$, $G_x=\Stab_G(p)$, is a subgroup of $G$, where among all elements of $G$ only the part fixing $p$ remains as $G_x$, and this is what is used in the local model above. 

Even within $G_x$ in this local model, the elements are divided according to their roles into those that act effectively. Looking at the local quotient $[V/G_x]$ and its coarse moduli $[V/G_x]\longrightarrow V/G_x$, each $G_x$-orbit is collapsed to a point, whereas $H$ disappears in the process of descending to the stack; thus, the elements that actually move points of $V$ form the quotient $G_x/H$. 

Now, to single out the elements of $H$, we can look at the function field. That is, since $H$ acts trivially on $K(V)$, the action of $G_x$ on the function field factors through $G_x/H$, so that

$$K(V/G_x)=K(V)^{G_x}=K(V)^{G_x/H}$$

holds. In characteristic $0$, since $G_x/H$ acts faithfully on $K(V)$,

$$[K(V):K(V/G_x)]=\lvert G_x/H\rvert=\frac{\lvert G_x\rvert}{\lvert H\rvert}$$

holds. 

Another important fact is that the local quotient morphism $[V/G_x]\rightarrow V/G_x$ for a finite group action is proper, so using this local description, the coarse moduli morphism $\pi:\mathcal{X}\rightarrow X$ is also a proper morphism.

::: Theorem 5
Over a field $\mathbb{K}$, for a separated Deligne–Mumford stack $\mathcal{X}$ of finite type and its coarse moduli space $\pi:\mathcal{X}\rightarrow X$, the following two conditions are equivalent:

1. $\mathcal{X}$ is proper.

2. The algebraic space $X$ is proper.
:::
::: Proof
If $X$ is proper, then composing the proper coarse morphism $\pi$ obtained in [Proposition 4](#prop4){: data-lid="1yoye" data-relation="required" } with $X\rightarrow\Spec\mathbb{K}$ shows that $\mathcal{X}$ is proper.

Conversely, suppose $\mathcal{X}$ is proper. The coarse morphism $\pi$ is surjective, and $X$ is a separated algebraic space of finite type. After any base change $T\rightarrow\Spec\mathbb{K}$, the morphism $\mathcal{X}_T\rightarrow X_T$ is also surjective. Since $\mathcal{X}_T\rightarrow T$ is closed, taking the preimage of a closed subset of $X_T$ and sending it to $T$ yields a closed subset, which by surjectivity is equal to the image of the original closed subset. Therefore, $X\rightarrow\Spec\mathbb{K}$ is universally closed, and since it is separated and of finite type, it is proper.
:::

On the other hand, when the stabilizers disappear completely, the difference between the stack and the coarse space also vanishes.

::: Corollary 6
Over a field $\mathbb{K}$, if a separated finite type Deligne–Mumford stack $\mathcal{X}$ has trivial stabilizer at every geometric point, then $\mathcal{X}$ is an algebraic space and the coarse morphism $\pi:\mathcal{X}\rightarrow X$ is an isomorphism.
:::
::: Proof
By the separated Deligne–Mumford condition, the inertia morphism $I_\mathcal{X}\rightarrow\mathcal{X}$ is finite unramified. Since the identity section $e:\mathcal{X}\rightarrow I_\mathcal{X}$ is a section of an unramified morphism, it is an open immersion, and by assumption every geometric point belongs to its image. Thus $e$ is an isomorphism and the inertia is the identity.

Since the difference between any two isomorphisms is an automorphism, the diagonal $\Delta_\mathcal{X}$ is a monomorphism. Therefore, each fiber groupoid is equivalent to a set, and by descent, $\mathcal{X}$ is identified with a set-valued sheaf. This sheaf with an étale atlas is an algebraic space, and applying the universal property of the coarse moduli morphism to this algebraic space itself yields the inverse of $\pi$.
:::

Therefore, to the extent that the moduli stack has trivial stabilizers, the problem of counting geometric points reduces to the problem of counting points of an algebraic space. When stabilizers remain, even if the coarse space has the same geometric isomorphism classes, it does not preserve the automorphism information.

---

**References**

**[AV]** D. Abramovich and A. Vistoli, *Compactifying the space of stable maps*, Journal of the American Mathematical Society **15** (2002), 27–75.  
**[Vis]** A. Vistoli, *Intersection theory on algebraic stacks and on their moduli spaces*, Inventiones Mathematicae **97** (1989), 613–670.  
**[Stacks]** The Stacks Project Authors, *The Stacks Project*, Tags 0CLA, 0CLG, 0CLK, 0CLT, 0CLU, 0CLW, 0CLX, 0CLZ, 0CQ8, 0CQM, https://stacks.math.columbia.edu.
