---
title: "Faithfully Flat Descent"
description: "This post covers Grothendieck's descent theory for sending algebraic and geometric data down along a faithfully flat morphism. Starting from the exactness of the Amitsur complex, it derives the descent theorem for modules, shows that the category of descent data is equivalent to the category of modules over the base ring, and extends this to the descent of quasi-coherent sheaves and morphisms in the fpqc topology."
excerpt: "Descent data, the cocycle condition, fpqc topology, and effective descent"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/faithfully_flat_descent
sidebar: 
    nav: "scheme_theory-en"

date: 2026-08-25
weight: 27
translated_at: 2026-09-02T05:45:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-09-02T05:45:05+00:00
---
One of the most common constructions in algebraic geometry is that of gluing local objects together into a single object; the most familiar example is gluing sections of a sheaf along an open cover. This essentially uses only a special kind of base change, the one given by localization, but many situations we actually want to treat are more general than this. For example, the morphism $\Spec \mathbb{L}\rightarrow \Spec \mathbb{K}$ corresponding to a field extension $\mathbb{L}/\mathbb{K}$ cannot be regarded as an open embedding, since the residue fields differ.

The idea for resolving this is to treat not only open embeddings but also faithfully flat, quasi-compact morphisms as valid coverings. We first examine the algebraic reason these can be treated as valid coverings, and then transfer this to geometry.

## Faithfully Flat Morphisms

As the name suggests, faithful flatness is a condition that adds a kind of surjectivity to flatness.

::: Definition 1
A ring homomorphism $\phi: A \rightarrow B$ is *faithfully flat* if $B$ is a flat $A$-module and, at the same time, for any $A$-module $M$, $M\otimes_A B=0$ implies $M=0$.
:::

In other words, the additional faithfulness imposed on top of flatness is that $-\otimes_A B$ sends no nonzero module to $0$. This admits the following equivalent formulations.

::: Proposition 2
For a flat ring homomorphism $\phi: A \rightarrow B$, the following are equivalent.

1. $\phi$ is faithfully flat.
2. A sequence $M' \rightarrow M \rightarrow M''$ of $A$-modules is exact if and only if the sequence $M'\otimes_A B \rightarrow M\otimes_A B \rightarrow M''\otimes_A B$ of $B$-modules is exact.
3. The scheme morphism $\varphi: \Spec B \rightarrow \Spec A$ corresponding to $\phi$ is surjective.
:::
::: Proof
We first show that the first and second conditions are equivalent. To this end, assume the first condition. Since $B$ is flat by assumption, an exact sequence remains exact after applying $-\otimes_A B$, so one direction of the second condition is trivial. The point is the converse; to show it, suppose that

$$M'\otimes_AB \overset{f\otimes_AB}{\longrightarrow} M\otimes_AB \overset{g\otimes_AB}{\longrightarrow} M''\otimes_AB$$

is an exact sequence. First of all,

$$0=(g\otimes B)\circ(f\otimes B)=(g\circ f)\otimes B,$$

so the image of

$$\im(g\circ f)\otimes_A B \rightarrow M''\otimes_A B,$$

which comes from the inclusion, is also $0$. Viewing this map as arising from $\im(g\circ f)\hookrightarrow M''$, it is injective since $B$ is flat; hence by faithfulness $\im(g\circ f)=0$, and $\im f\subseteq \ker g$ holds. Now, to verify exactness it suffices to show that $H=\ker g/\im f$ is $0$, which is immediate since $B$ is flat. By the same argument as before, faithfulness then gives $H=0$, and therefore the original sequence is exact.

Conversely, assume the second condition and let us prove the first. If $M\otimes_A B=0$, then the sequence $0 \rightarrow M \rightarrow 0$ becomes exact after applying $-\otimes_A B$, so by assumption $0 \rightarrow M \rightarrow 0$ is exact. That is, $M=0$, and $\phi$ is faithfully flat.

We now show that the first and third conditions are equivalent. First, assume the first condition and pick an arbitrary $\mathfrak{p}\in \Spec A$. Then $\mathfrak{p}$ lies in the image of $\varphi$ if and only if its fiber $\Spec(B\otimes_A \kappa(\mathfrak{p}))$ is nonempty, i.e. if and only if $B\otimes_A \kappa(\mathfrak{p})\neq 0$. But by faithful flatness, if $\kappa(\mathfrak{p})\neq 0$ then its base change $B\otimes_A \kappa(\mathfrak{p})$ is likewise nonzero, so this holds.

Finally, assume the third condition and let us prove the first. For this, it suffices to show that $M\otimes_A B\neq 0$ for every $A$-module $M$ with $M\neq 0$. Picking $0\neq x\in M$, we have $Ax\cong A/{\ann(x)}$, which is a submodule of $M$. Now pick a maximal ideal $\mathfrak{m}$ with $\ann(x)\subseteq \mathfrak{m}$. By assumption this lies in the image of $\varphi$, so $\kappa(\mathfrak{m})\otimes_A B\neq 0$. Meanwhile, applying $-\otimes_A B$ to the surjection $A/{\ann(x)}\twoheadrightarrow A/\mathfrak{m}=\kappa(\mathfrak{m})$ yields a surjection

$$(A/{\ann(x)})\otimes_A B\twoheadrightarrow \kappa(\mathfrak{m})\otimes_A B,$$

so $(A/{\ann(x)})\otimes_A B\neq 0$. Also, since $B$ is flat, applying $-\otimes_A B$ to the inclusion $A/{\ann(x)}\cong Ax\hookrightarrow M$ yields an inclusion

$$(A/{\ann(x)})\otimes_A B\hookrightarrow M\otimes_A B.$$

Therefore $M\otimes_A B\neq 0$, and $B$ is a faithful $A$-module.
:::

What is particularly noteworthy in this proposition is the second condition, which says that exactness may be checked after base change. The third condition shows that this algebraically defined property corresponds exactly to the surjectivity of the morphism $\Spec B \rightarrow \Spec A$; hence a faithfully flat ring homomorphism can be thought of as an affine faithfully flat morphism in the sense of [§Flat Morphisms, ⁋Definition 1](/en/math/scheme_theory/flat_morphisms#def1).

A special example is $A \rightarrow \prod_i A_{f_i}$, obtained when elements $f_1,\ldots, f_n$ of $A$ generate all of $A$: since each $A_{f_i}$ is flat, so is their product, and since $\Spec \prod A_{f_i}=\coprod D(f_i)$ covers $\Spec A$, it is surjective. This is exactly a Zariski cover of an affine scheme, and it shows that the notion above subsumes the everyday gluing of sheaves. Moreover, in the case of a field extension $\mathbb{L}/\mathbb{K}$, which could not be accounted for by open embeddings above, $\mathbb{L}$ is (of course) free as a $\mathbb{K}$-vector space, and the geometric morphism between them is a surjective morphism sending one point to one point, so it is faithfully flat.

## Amitsur Complex

Given a ring homomorphism $\phi: A \rightarrow B$, we are given two morphisms

$$d^0, d^1: B \rightrightarrows B\otimes_A B,\qquad d^0(b)=b\otimes 1,\quad d^1(b)=1\otimes b.$$

These are the two homomorphisms recording the two ways in which $B$ may be inserted into $B\otimes_AB$, and taking their difference $d=d^1-d^0$ we may consider the morphism $d: B\rightarrow B\otimes_AB$. Moreover, since any element coming from $A$ lies in the kernel of $d$ by the defining property of the tensor product, we may consider the sequence

$$0\rightarrow A \overset{\phi}{\longrightarrow}B\overset{d}{\longrightarrow}B\otimes_AB.$$

More generally, let $C^n=B^{\otimes (n+1)}$ be the $(n+1)$-th tensor power of $B$, and consider the morphisms from $C^n$ to $C^{n+1}$ given by

$$\delta_i: C^n \rightarrow C^{n+1};\qquad \delta_i(b_0\otimes \cdots \otimes b_n)=b_0\otimes \cdots \otimes b_{i-1}\otimes 1\otimes b_i\otimes \cdots \otimes b_n.$$

That is, $\delta_i$ is the morphism inserting $1$ in the $i$-th position, and their alternating sum

$$\partial^n=\sum_{i=0}^{n+1}(-1)^i\delta_i: C^n \rightarrow C^{n+1}$$

is again a morphism from $C^n$ to $C^{n+1}$. A short computation confirms that this forms a complex, and we call the sequence

$$0 \rightarrow A \overset{\phi}{\longrightarrow} B \overset{\partial^0}{\longrightarrow} B\otimes_A B \overset{\partial^1}{\longrightarrow} B\otimes_A B\otimes_A B \rightarrow \cdots$$

obtained by adjoining $\phi$ as above the *Amitsur complex* of $\phi$.

The key observation is that if $\phi$ is faithfully flat, then this complex is exact, so that $C^\bullet$ is a resolution of $A$. However, what we actually use in this post is not the whole resolution but only the first two morphisms, so we claim only the following.

::: Lemma 3
For a ring homomorphism $\phi: A \rightarrow B$, the sequence of $B$-modules

$$0 \rightarrow B \overset{\phi\otimes B}{\longrightarrow} B\otimes_A B \overset{d\otimes B}{\longrightarrow} B\otimes_A B\otimes_A B$$

obtained by applying $-\otimes_A B$ to the above sequence is split exact. In particular, if $\phi$ is faithfully flat, then the sequence

$$0 \rightarrow A \overset{\phi}{\longrightarrow} B \overset{d}{\longrightarrow} B\otimes_A B$$

is exact.
:::
::: Proof
First, consider the sequence

$$0 \rightarrow B \overset{\phi\otimes B}{\longrightarrow} B\otimes_A B \overset{d\otimes B}{\longrightarrow} B\otimes_A B\otimes_A B$$

obtained by applying $-\otimes_A B$. Our claim is that this is a split exact sequence.

To see this, consider the two maps

$$s: B\otimes_AB \rightarrow B;\quad b\otimes b'\mapsto bb',\qquad t: B\otimes_AB\otimes_AB\rightarrow B\otimes_AB;\quad b\otimes b'\otimes b''\mapsto b\otimes b'b''.$$

Endowing each of $B\otimes_AB$ and $B\otimes_AB\otimes_AB$ with the $B$-module structure acting on the rightmost $B$, these two maps become $B$-linear, and it is immediate that the identity

$$s\circ(\phi\otimes B)=\id_B$$

holds. In particular, $\phi\otimes B$ is injective. Moreover, if $b\otimes b'\in\ker(d\otimes B)$, then by definition

$$0=(d\otimes B)(b\otimes b')=1\otimes b\otimes b'-b\otimes 1\otimes b',$$

so $1\otimes b\otimes b'=b\otimes 1\otimes b'$, and applying $t$ gives

$$b\otimes b'=t(b\otimes 1\otimes b')=t(1\otimes b\otimes b')=1\otimes bb'=(\phi\otimes B)(s(b\otimes b')),$$

so $\ker(d\otimes B)\subseteq \im(\phi\otimes B)$. The reverse inclusion is immediate from $d\circ \phi=0$, so the base-changed sequence is exact. In particular, if $\phi$ is faithfully flat, then the original sequence is also exact by [Proposition 2](#prop2).

To complete the proof of split exactness, we return to $t$: for any $b\otimes b'$ we have $t((d\otimes B)(b\otimes b'))=1\otimes bb'-b\otimes b'$, so

$$(\phi\otimes B)\circ s-t\circ (d\otimes B)=\id_{B\otimes_AB},$$

which, together with $s\circ (\phi\otimes B)=\id_B$, confirms that $(s,-t)$ is a contracting homotopy of this sequence.
:::

The reason this serves as the engine of gluing becomes manifest when we look at the Zariski open cover of an affine scheme considered earlier. Suppose $A=(f_1,\ldots, f_n)$, and let $B=\prod_i A_{f_i}$. Then

$$B\otimes_AB=\left(\prod_i A_{f_i}\right)\otimes_A \left(\prod_j A_{f_j}\right),$$

and since the products here are finite, we can combine them and write

$$B\otimes_AB \cong\prod_{i,j} A_{f_i}\otimes A_{f_j}\cong\prod_{i,j} A_{f_if_j}.$$

([[\[Commutative Algebra\] §Properties of Localization, ⁋Lemma 1]](/en/math/commutative_algebra/properties_of_localization#lem1)) Under this identification, $d^0$ places an element of $B$ into the first factor, indexed by $i$, and $d^1$ places it into the second factor, indexed by $j$.

Geometrically, since $D(f_i)\cap D(f_j)=D(f_if_j)$, we can think of $B\otimes_AB$ as the ring of functions defined on the overlaps $D(f_i)\cap D(f_j)$, and then $d^0$ and $d^1$ become the respective restrictions

$$d^0\bigl((s_i)_i\bigr)=\bigl(s_i\vert_{D(f_if_j)}\bigr)_{i,j},\qquad d^1\bigl((s_i)_i\bigr)=\bigl(s_j\vert_{D(f_if_j)}\bigr)_{i,j}.$$

In other words, the difference between the two morphisms comes from whether one looks at $s_i$ or at $s_j$ on the overlap $D(f_if_j)$, and saying that an element $(s_i)_i$ of $B$ lies in the kernel of $d$ means that $s_i$ and $s_j$ agree on that overlap for all $i,j$. That is, it gives the gluing condition for the $s_i$ defined on the various $D(f_i)$. Moreover, the injectivity of $\phi$ is exactly the assertion that an element of $A$ vanishing on every $D(f_i)$ is $0$, so it gives the identity axiom of a sheaf; hence [Lemma 3](#lem3) is nothing but the sheaf condition of $\mathcal{O}_{\Spec A}$ for the open cover $\{D(f_i)\}_i$. More generally, the remaining terms of the Amitsur complex form the Čech complex of this cover.

## Descent Data

[Lemma 3](#lem3) tells us exactly how $A$ is recovered from the data of $B$; the slogan is that collecting the elements of $B$ on which the two ways of base changing agree yields exactly $A$.

Descent is what results from lifting this principle to modules. Suppose a $B$-module $N$ is given, and consider the process of producing a $B\otimes_AB$-module by applying $-\otimes_AB$ or $B\otimes_A-$ to it. As in the case of rings, the two $B\otimes_AB$-modules $N\otimes_AB$ and $B\otimes_AN$ are two structures that differ according to whether $N$ enters the first factor or the second factor, and our goal is to compare them and take their equalizer. The problem is that, unlike the situation for rings, $N\otimes_AB$ and $B\otimes_AN$ are *genuinely* different[^1] objects. Therefore, comparing them and computing the equalizer requires an additional input, namely an identification between $N\otimes_AB$ and $B\otimes_AN$, and this is exactly what a descent datum is.

To treat this, let us fix notation. We define the morphisms

$$p_1: B\rightarrow B\otimes_AB;\quad b\mapsto b\otimes 1, \qquad p_2: B\rightarrow B\otimes_AB;\quad b\mapsto 1\otimes b$$

and, similarly, we define

$$p_{12}, p_{13}, p_{23}: B\otimes_A B \rightarrow B\otimes_A B\otimes_A B$$

as the morphisms mapping into the two of the three factors singled out by the indices. Then for a $B$-module $N$, we have $p_1^\ast N=N\otimes_A B$ and $p_2^\ast N=B\otimes_A N$.

::: Definition 4
A *descent datum* for a ring homomorphism $\phi: A \rightarrow B$ is a pair $(N, \Phi_N)$ consisting of a $B$-module $N$ and a $B\otimes_A B$-module isomorphism

$$\Phi_N: p_1^\ast N=N\otimes_A B \overset{\sim}{\longrightarrow} B\otimes_A N=p_2^\ast N$$

satisfying the *cocycle condition*

$$p_{13}^\ast \Phi_N=p_{23}^\ast \Phi_N\circ p_{12}^\ast \Phi_N$$

over $B\otimes_A B\otimes_A B$. A *morphism* between two descent data $(N, \Phi_N)$ and $(N', \Phi_{N'})$ is a $B$-module homomorphism $g: N \rightarrow N'$ satisfying $\Phi_{N'}\circ(g\otimes B)=(B\otimes g)\circ \Phi_N$. We write $\Desc(B/A)$ for the category they form.
:::

Here the cocycle condition says that the gluing is consistently defined over triple intersections; it can be represented by the diagram

{% diagram Math/Scheme_Theory/Faithfully_Flat_Descent-1.svg width="15.94em" alt="cocycle condition" %}

where each morphism, for instance $p_{12}^\ast \Phi_N: p_1^\ast N\rightarrow p_2^\ast N$, is given by the formula

$$N\otimes_A B\otimes_A B \rightarrow B\otimes_A N\otimes_A B;\qquad n\otimes b\otimes b'\mapsto \Phi_N(n\otimes b)\otimes b'.$$

In studying the Amitsur complex for rings, our first observation was that the kernel of $d=d^1-d^0$ already contains $A$. What corresponds to this in the module setting is the case where the $B$-module $N$ comes from the base change $M\otimes_A B$ of some $A$-module $M$; in this case the identification demanded above as an extra input comes for free. Here the two base changes are

$$p_1^\ast N=M\otimes_A B\otimes_A B,\qquad p_2^\ast N=B\otimes_A M\otimes_A B,$$

which are distinct $B\otimes_AB$-modules, just as in the general case examined above. In both, however, the $B\otimes_AB$-module structure is such that the first factor of $B\otimes_AB$ acts on the left $B$-factor and the second factor acts on the right $B$-factor; moving the $M$-factor of $p_2^\ast N$ to the front using the commutativity of $A$ yields a $B\otimes_AB$-module isomorphism, through which $p_1^\ast N$ and $p_2^\ast N$ can be compared.

::: Example 5
Given an $A$-module $M$, set $N=M\otimes_A B$; then the $B\otimes_A B$-module isomorphism

$$\sigma_M: M\otimes_A B\otimes_A B \overset{\sim}{\longrightarrow} B\otimes_A M\otimes_A B;\qquad m\otimes x\otimes y\mapsto x\otimes m\otimes y$$

between the two base changes $p_1^\ast N=M\otimes_A B\otimes_A B$ and $p_2^\ast N=B\otimes_A M\otimes_A B$ seen above defines a descent datum $(M\otimes_A B, \sigma_M)$. We call this the *canonical descent datum* attached to $M$.

More generally, an $A$-module homomorphism $M \rightarrow M'$ base-changes to a morphism between canonical descent data, so the assignment $M\mapsto (M\otimes_A B, \sigma_M)$ defines a functor

$$\rMod{A} \rightarrow \Desc(B/A).$$
:::

## Faithfully Flat Descent

We are now ready to state the central claim of this post. It is essentially nothing more than a restatement of the principle verified in [Lemma 3](#lem3).
::: Theorem 6 (Grothendieck)
If the ring homomorphism $\phi: A \rightarrow B$ is faithfully flat, then the functor

$$\rMod{A} \rightarrow \Desc(B/A);\qquad M\mapsto (M\otimes_A B, \sigma_M)$$

from [Example 5](#ex5) is an equivalence of categories. Its inverse functor sends a descent datum $(N, \Phi_N)$ to

$$N^\Phi=\{n\in N\mid \Phi_N(n\otimes 1)=1\otimes n\}.$$
:::
::: Proof
First, suppose an $A$-module $M$ is given, and consider the canonical descent datum $(M\otimes_A B, \sigma_M)$ it defines. Applying the inverse functor above to it, we obtain

$$(M\otimes_AB)^\sigma=\{x\in M\otimes_A B\mid \sigma_M(x\otimes 1)=1\otimes x\},$$

and since $\sigma_M$ merely moves the $M$-factor, moving the $M$-factors of both sides back to the front and reading the condition inside $M\otimes_A B\otimes_A B$, the condition becomes $x\otimes 1=1\otimes x$. Hence what we must show is the exactness of the sequence

$$0 \rightarrow M \rightarrow M\otimes_A B \rightarrow M\otimes_A B\otimes_A B,$$

and this is obtained by repeating the proof of [Lemma 3](#lem3) verbatim with coefficient $M$ attached.

The part with real content is the other direction. Namely, given a descent datum $(N, \Phi_N)$, set $M=N^\Phi$; we must show that the $B$-module morphism

$$u: M\otimes_A B \rightarrow N;\qquad m\otimes b\mapsto bm$$

is an isomorphism from the descent datum $(M\otimes_AB, \sigma_M)$ to $(N, \Phi_N)$.

We now construct an inverse $v: N\rightarrow M\otimes_AB$ of $u$. The idea is that, in order to send an element of $N$ into $M\otimes_AB$, one has no choice but to send $n$ to an element of the same shape as $n\otimes 1$; bearing this in mind and computing a little, we see that we are forced to define it using the descent datum as $n\mapsto \Phi_N^{-1}(1\otimes n)$. For convenience write $\Psi=\Phi_N^{-1}$; our claim is that the image of this assignment $n\mapsto \Psi(1\otimes n)$ lands in $M\otimes_AB$.

To check this, write $\Psi(1\otimes n)=\sum_j n_j\otimes c_j$. Then by the cocycle condition $p_{13}^\ast \Psi=p_{12}^\ast \Psi\circ p_{23}^\ast \Psi$, and evaluating both sides at the element $1\otimes 1\otimes n\in B\otimes_A B\otimes_A N$ gives

$$p_{13}^\ast \Psi(1\otimes 1\otimes n)=\sum_j n_j\otimes 1\otimes c_j,\qquad (p_{12}^\ast \Psi\circ p_{23}^\ast \Psi)(1\otimes 1\otimes n)=\sum_j \Psi(1\otimes n_j)\otimes c_j.$$

Now identifying these two and applying $p_{12}^\ast \Phi_N$ to both sides, we obtain the equality

$$\sum_j \Phi_N(n_j\otimes 1)\otimes c_j=\sum_j (1\otimes n_j)\otimes c_j.$$

Therefore, defining $d_N: N \rightarrow B\otimes_A N$ by $d_N(n)=\Phi_N(n\otimes 1)-1\otimes n$, we have $(d_N\otimes B)\bigl(\sum_j n_j\otimes c_j\bigr)=0$. Our claim is then that $\ker(d_N\otimes B)=M\otimes_AB$, so that the above assignment lands in $M\otimes_AB$. Now by the definition of $M$, the sequence $0 \rightarrow M \rightarrow N \overset{d_N}{\longrightarrow} B\otimes_A N$ is exact, and since $B$ is flat, applying $-\otimes_AB$ yields

$$0 \rightarrow M\otimes_A B \rightarrow N\otimes_A B \overset{d_N\otimes B}{\longrightarrow} B\otimes_A N\otimes_A B,$$

which is again exact. That is, inside $N\otimes_A B$ we have $M\otimes_A B=\ker(d_N\otimes B)$.

Now let us show that the assignment $v: n\mapsto \Psi(1\otimes n)$ so constructed is indeed inverse to $u$. First,

$$v(u(m\otimes b))=\Psi(1\otimes bm)=(1\otimes b)\Psi(1\otimes m)=(1\otimes b)(m\otimes 1)=m\otimes b$$

is immediate. Conversely, for $u(v(n))=n$: since $v(n)$ is an element of $M\otimes_A B$, we can choose $m_k\in M$ and write $v(n)=\sum_k m_k\otimes b_k$; applying $\Phi_N$ gives $\Phi_N(v(n))=\Phi_N(\Psi(1\otimes n))=1\otimes n$, and therefore

$$1\otimes n=\sum_k (1\otimes b_k)\Phi_N(m_k\otimes 1)=\sum_k (1\otimes b_k)(1\otimes m_k)=1\otimes \sum_k b_km_k.$$

But the injectivity of $n\mapsto n\otimes 1$ is supplied by [Lemma 3](#lem3) (its version with coefficient $M$), and the map $n\mapsto 1\otimes n: N \rightarrow B\otimes_A N$, obtained from it by swapping the order, is likewise injective; hence $u(v(n))=\sum_k b_km_k=n$.

Finally, that $u$ is actually an isomorphism of descent data is checked by applying the two composites to $m\otimes b\otimes b'$, and naturality can likewise be verified by a small computation.
:::

Logically, the categorical equivalence of [Theorem 6](#thm6) contains two distinct claims. Full faithfulness says that when two $A$-modules $M,M'$ are already given, a compatible $B$-module morphism $M\otimes_A B\rightarrow M'\otimes_A B$ between canonical descent data comes from a unique $A$-module morphism $M\rightarrow M'$. Here the source and target are given globally, and one merely glues the morphism between them. This is descent for morphisms.

In essential surjectivity, no global $A$-module is given in advance. From an arbitrary descent datum $(N,\Phi_N)$ one must find an $A$-module $M$ and express $(N,\Phi_N)\cong(M\otimes_A B,\sigma_M)$; in the proof above we constructed this $M$ as $N^\Phi$. This is effective descent for objects. Since essential surjectivity does not follow from full faithfulness alone, the ability to glue morphisms does not by itself imply that objects can be glued.

As a direct consequence of this theorem, many properties of an $A$-module $M$ may be checked not on $M$ itself but on $M\otimes_A B$, lifted up to $B$. For instance, if $M\otimes_A B$ is a finitely generated $B$-module then $M$ is finitely generated; if $M\otimes_A B$ is finitely presented then so is $M$; and if $M\otimes_A B$ is flat then so is $M$. This is because each of these properties can be expressed by an exact sequence, and [Proposition 2](#prop2) reflects that exactness back down to $A$.

::: Proposition 7
Let the ring homomorphism $\phi: A \rightarrow B$ be faithfully flat and let $M$ be an $A$-module. Then $M$ is finitely generated (resp. finitely presented, flat, locally free of finite rank) if and only if $M\otimes_A B$ is finitely generated (resp. finitely presented, flat, locally free of finite rank) as a $B$-module.
:::
::: Proof
The direction that $M\otimes_A B$ has the property whenever $M$ does is trivial, since each property is preserved under base change; the heart of this proposition is that the converse directions hold.

First, suppose $M\otimes_AB$ is generated by $y_1,\ldots, y_n$. Each $y_i$ can be written as a sum of finitely many elements $m_{ij}\otimes b_{ij}$, so gathering all the $m_{ij}$ we obtain a finitely generated submodule $M_0\subseteq M$ of $M$. Then $M_0\otimes_AB\rightarrow M\otimes_AB$ is surjective, hence $(M/M_0)\otimes_A B=0$, so by faithfulness $M/M_0=0$. That is, $M=M_0$ is finitely generated.

Now consider the case of finite presentation. Under this hypothesis we already know from the above that $M$ is finitely generated, so it suffices to show that the kernel $K$ of $A^n \twoheadrightarrow M$ is finitely generated. For this, base-changing the exact sequence

$$0 \rightarrow K \rightarrow A^n \rightarrow M \rightarrow 0$$

to $B$ gives

$$0 \rightarrow K\otimes_A B \rightarrow B^n \rightarrow M\otimes_A B \rightarrow 0,$$

which is exact, and since $M\otimes_A B$ is finitely presented, $K\otimes_A B$ is finitely generated (the discussion following [\[Commutative Algebra\] §Flatness, ⁋Corollary 6](/en/math/commutative_algebra/flatness#cor6)). Therefore, applying the finitely generated case above to $K$, we conclude that $K$ is finitely generated and $M$ is finitely presented.

For flatness, to show that $M$ is flat it suffices to show that for every injective $A$-module morphism $M' \hookrightarrow M''$, the map $M'\otimes_A M \rightarrow M''\otimes_A M$ is injective. Again applying $-\otimes_AB$, we obtain a morphism $M'\otimes_A M\otimes_A B \rightarrow M''\otimes_A M\otimes_A B$, which can be regarded as obtained by tensoring the injective homomorphism $M'\otimes_A B \rightarrow M''\otimes_A B$ with the flat $B$-module $M\otimes_A B$, so it is again injective.

Finally, locally free of finite rank is equivalent to being finitely presented and flat ([\[Commutative Algebra\] §Flatness, ⁋Corollary 6](/en/math/commutative_algebra/flatness#cor6)), so there is nothing more to prove.
:::

## Descent of Quasi-coherent Sheaves

We now have all the tools needed for gluing. What remains is merely to attach the appropriate names. Namely, having seen that gluing works well even when the notion of open embedding is extended to faithfully flat morphisms, we may as well rewrite the notion of *open set* outright using these faithfully flat morphisms.

::: Definition 8
A *Grothendieck pretopology* on a category $\mathcal{C}$ having fiber products is an assignment, to each object $U$, of a collection of families $\{f_i: U_i \rightarrow U\}_{i\in I}$ of morphisms with codomain $U$, whose members are called *coverings* of $U$. These satisfy the following three conditions.

1. If $f: V \rightarrow U$ is an isomorphism, then $\{f: V \rightarrow U\}$ is a covering.
2. If $\{f_i: U_i \rightarrow U\}$ is a covering and $g: V \rightarrow U$ is an arbitrary morphism, then the family $\{U_i\times_U V \rightarrow V\}_{i\in I}$ given by base change is also a covering.
3. If $\{f_i: U_i \rightarrow U\}$ is a covering and for each $i$ the family $\{g_{ij}: U_{ij} \rightarrow U_i\}_{j\in J_i}$ is a covering, then the family $\{f_i\circ g_{ij}: U_{ij} \rightarrow U\}_{i, j}$ given by composition is also a covering.
:::

In particular, since $\Sch$ has fiber products ([§Fiber Products, ⁋Theorem 8](/en/math/scheme_theory/fiber_products#thm8)), we can apply this definition. Reading an open cover $\{U_i\}$ of a topological space as the family of inclusions $\{U_i\hookrightarrow U\}$, the three conditions above hold, with $U_i\times_U V$ being the intersection $U_i\cap V$. In other words, the three conditions merely require that an object covers itself, that the restriction of a covering is again a covering, and that a covering of a covering is a covering. The topology we will use employs coverings by faithfully flat morphisms satisfying a quasi-compactness condition; abbreviating its name *fidèlement plat quasi-compact*, we call it the fpqc topology.

::: Definition 9
A family $\{\psi_i: U_i \rightarrow X\}_{i\in I}$ of morphisms over a scheme $X$ is an *fpqc cover* if each $\psi_i$ is flat, $\coprod_i U_i \rightarrow X$ is surjective, and the quasi-compactness condition holds: every affine open $V\subseteq X$ is covered by the images of finitely many affine opens $W_{ij}$ of the $U_i$. The Grothendieck topology on $\Sch$ defined by these coverings is called the *fpqc topology*.
:::

In the fpqc topology, the simplest covering of a single affine scheme $\Spec A$ is $\{\Spec B \rightarrow \Spec A\}$, consisting of one faithfully flat ring homomorphism $A \rightarrow B$.

The reason we took the trouble to lift [Lemma 3](#lem3) to modules is, of course, to deal with quasi-coherent sheaves ([§Quasi-coherent Sheaves, ⁋Definition 8](/en/math/scheme_theory/quasicoherent_sheaves#def8)).

::: Theorem 10
For any scheme $X$ and any quasi-coherent sheaf $\mathcal{F}$ on $X$, the presheaf

$$T\mapsto \Gamma(T, \psi^\ast \mathcal{F})\qquad (\psi: T \rightarrow X)$$

is a sheaf for the fpqc topology. That is, for every fpqc cover $\{T_i \rightarrow T\}$, the sequence

$$\Gamma(T, \psi^\ast\mathcal{F}) \rightarrow \prod_i \Gamma(T_i, \psi_i^\ast\mathcal{F}) \rightrightarrows \prod_{i,j}\Gamma(T_i\times_T T_j, \psi_{ij}^\ast\mathcal{F})$$

is exact.
:::
::: Proof
The problem is local, and thanks to the quasi-compactness condition it reduces to a finite covering, so it suffices to treat the case where $T=\Spec A$ is affine and the covering is a single faithfully flat morphism $\{\Spec B \rightarrow \Spec A\}$. In this case, choose an $A$-module $M$ with $\mathcal{F}=\widetilde M$; since pullback is given by base change ([§Quasi-coherent Sheaves, ⁋Proposition 15](/en/math/scheme_theory/quasicoherent_sheaves#prop15)), the above sequence becomes

$$M \rightarrow M\otimes_A B \rightrightarrows M\otimes_A B\otimes_A B.$$

The claim is then the exactness of the sequence

$$0 \rightarrow M \rightarrow M\otimes_A B \rightarrow M\otimes_A B\otimes_A B$$

obtained by generalizing [Lemma 3](#lem3) with $M$ as coefficient, which was already shown in the proof of [Theorem 6](#thm6). Now the fact that the equalizer of the two morphisms $d^0, d^1$ is $M$ is precisely the sheaf condition above, so we obtain the conclusion.
:::

[Theorem 10](#thm10) allows us to compute global sections of a quasi-coherent sheaf over a faithfully flat covering. From this we obtain descent for quasi-coherent sheaves themselves.

::: Theorem 11
Let $\{\psi_i: U_i \rightarrow X\}$ be an fpqc cover. Then giving a quasi-coherent sheaf on $X$ is equivalent to giving the data of quasi-coherent sheaves $\mathcal{F}_i$ on each $U_i$, together with isomorphisms $\Phi_{ij}: \pr_2^\ast \mathcal{F}_j\cong \pr_1^\ast \mathcal{F}_i$ on $U_i\times_X U_j$ satisfying the cocycle condition.
:::
::: Proof
Since the problem is local, it suffices to consider the case where $X=\Spec A$ and the covering is a single faithfully flat morphism $\Spec B \rightarrow \Spec A$. In this situation, $U_i\times_X U_j$ is $\Spec(B\otimes_A B)$, and the given data is exactly a cocycle pair consisting of a $B$-module $N=\Gamma(\Spec B, \mathcal{F}_1)$ and a $B\otimes_A B$-module isomorphism $\Phi_N$, i.e. a descent datum in the sense of [Definition 4](#def4). Since this data corresponds exactly to an object of $\Desc(B/A)$, by [Theorem 6](#thm6) it comes from a unique $A$-module $M$, i.e. a unique quasi-coherent sheaf $\widetilde M$, and this correspondence preserves morphisms as well.

For a general fpqc cover, use the quasi-compactness condition to extract a finite subcover, form its disjoint union into a single affine faithfully flat morphism, apply the affine case above, and then glue the results over the affine opens of $X$. The consistency of the gluing is guaranteed by the sheaf property of [Theorem 10](#thm10).
:::

Once again, the essential point of [Theorem 11](#thm11) is that when a descent datum $(\mathcal{F}_i, \Phi)$ of the above form is given, one can actually glue these together to obtain a single sheaf $\mathcal{F}$.

## Descent of Morphisms

We now turn to the problem of gluing objects one step more geometric than quasi-coherent sheaves. Our first goal is to glue schemes. Suppose an fpqc cover $\{\psi_i:U_i\rightarrow S\}$ is given, that for each $i$ a $U_i$-scheme structure $V_i\rightarrow U_i$ is given, and that on each overlap $U_i\times_SU_j$ an identification of these via isomorphisms satisfying the cocycle condition is already given. Our goal is to find an $S$-scheme $V\rightarrow S$ gluing these $U_i$-schemes together; the condition that it extends the $V_i$ is given by the isomorphisms

$$V\times_SU_i\cong V_i.$$

In general such a construction is not always possible, and the most basic condition making it possible is that the $V_i\rightarrow U_i$ be affine.

::: Theorem 12
Suppose we are given an fpqc cover $\{\psi_i:U_i \rightarrow S\}$, affine morphisms $V_i \rightarrow U_i$ defined over each of them, and cocycle isomorphism data identifying these over the intersections $U_i\times_S U_j$. Then there exist an affine morphism $V\rightarrow S$ over $S$ and isomorphisms $V\times_SU_i\cong V_i$ compatible with the given cocycle isomorphisms, and such a $V$ is unique up to unique isomorphism.
:::
::: Proof
Our strategy is to use the gluing of quasi-coherent sheaves that we already have. To this end, we regard the affine morphisms $\varphi_i: V_i\rightarrow U_i$ as quasi-coherent $\mathcal{O}_{U_i}$-algebras

$$\mathcal{A}_i=(\varphi_i)_\ast\mathcal{O}_{V_i}$$

([§Quasi-coherent Sheaves, ⁋Theorem 20](/en/math/scheme_theory/quasicoherent_sheaves#thm20)). That is, we think of $V_i$ as the relative spec $\rSpec_{U_i}(\mathcal{A}_i)$; it suffices to glue these quasi-coherent algebras into a single quasi-coherent algebra and then turn it back into an affine morphism.

Now the cocycle isomorphisms among the $V_i$ translate in this language into cocycle isomorphisms among the pullbacks of the $\mathcal{A}_i$, so applying [Theorem 11](#thm11) yields a quasi-coherent sheaf $\mathcal{A}$ on $S$ together with isomorphisms

$$\psi_i^\ast\mathcal{A}\cong\mathcal{A}_i.$$

We must now endow it with an algebra structure. As we checked in the proof of [§Quasi-coherent Sheaves, ⁋Proposition 22](/en/math/scheme_theory/quasicoherent_sheaves#prop22), pullback is compatible with tensor products and $\psi_i^\ast\mathcal{O}_S\cong\mathcal{O}_{U_i}$, so the multiplication and unit of each $\mathcal{A}_i$,

$$\mu_i:\mathcal{A}_i\otimes\mathcal{A}_i\rightarrow\mathcal{A}_i,\qquad \eta_i:\mathcal{O}_{U_i}\rightarrow\mathcal{A}_i,$$

can be viewed as morphisms between the pullbacks of $\mathcal{A}\otimes\mathcal{A}$ and $\mathcal{A}$, and between the pullbacks of $\mathcal{O}_S$ and $\mathcal{A}$, respectively. Since these are compatible with the given algebra isomorphisms, the correspondence on morphisms in [Theorem 11](#thm11) yields unique morphisms

$$\mu:\mathcal{A}\otimes\mathcal{A}\rightarrow\mathcal{A},\qquad \eta:\mathcal{O}_S\rightarrow\mathcal{A}$$

whose pullbacks agree with $\mu_i$ and $\eta_i$, respectively. Associativity and the unit law hold after pulling back over the $U_i$, and sheaf morphisms that agree over an fpqc cover also agree over $S$, so $\mathcal{A}$ is a quasi-coherent $\mathcal{O}_S$-algebra. Therefore, setting

$$V=\rSpec_S(\mathcal{A})$$

gives an affine scheme over $S$. By [§Quasi-coherent Sheaves, ⁋Proposition 22](/en/math/scheme_theory/quasicoherent_sheaves#prop22), the relative spectrum is compatible with base change, so

$$V\times_SU_i\cong\rSpec_{U_i}(\psi_i^\ast\mathcal{A})\cong\rSpec_{U_i}(\mathcal{A}_i)\cong V_i,$$

and these isomorphisms recover the cocycle data given at the start. Moreover, since $\mathcal{A}$ and its algebra structure are unique up to unique isomorphism by [Theorem 11](#thm11), and an affine morphism is recovered from its quasi-coherent algebra, $V$ is also unique in the same sense.
:::

More generally, a quasi-compact, quasi-separated morphism of schemes $\varphi:V\rightarrow U$ is *quasi-affine* if the canonical morphism $V\rightarrow\rSpec_U(\varphi_\ast\mathcal{O}_V)$ is a quasi-compact open immersion. The conclusion of [Theorem 12](#thm12) holds in this case as well. A generalization in another direction is the case of quasi-projective morphisms; being quasi-projective alone is not enough, and one must be given an ample line bundle together with a compatible descent datum on it. Roughly, the proof descends the section algebra of the ample line bundle to form a relative Proj; the original schemes then appear as open subschemes of it, and one glues these together.

Meanwhile, faithfully flat base change is not only an exact functor; the essential point is that the exactness verified there can be brought back down to the original, and [Proposition 7](#prop7) used this to descend flatness and finiteness conditions of modules. Applying the same argument affine-locally, one can also check properties of an already given scheme morphism $\psi:X\rightarrow Y$ over a cover. For this, taking an fpqc cover $\{Y_i\rightarrow Y\}$ of $Y$, the morphism $\psi$ defines morphisms

$$\psi_i:X\times_YY_i\rightarrow Y_i.$$

Lifting [Proposition 7](#prop7) scheme-theoretically then yields the flatness and finiteness properties in the following proposition, while surjectivity and affineness can be handled in the same manner as [Theorem 12](#thm12).

::: Proposition 13
Let a scheme morphism $\psi: X\rightarrow Y$ and an fpqc cover $\{Y_i \rightarrow Y\}$ of $Y$ be given. Then $\psi$ has one of the following properties if and only if each base change $\psi_i: X\times_Y Y_i \rightarrow Y_i$ has that property.

> Flat, faithfully flat, affine, locally of finite type, locally of finite presentation, surjective.
:::

---

**References**

**[Vak]** R. Vakil, *The rising sea: Foundations of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).  
**[FGA]** B. Fantechi, L. Göttsche, L. Illusie, S. Kleiman, N. Nitsure, A. Vistoli, *Fundamental algebraic geometry: Grothendieck's FGA explained*. Mathematical Surveys and Monographs. American Mathematical Society, 2005.  

---

[^1]: For rings, both of these objects were $B\otimes_AB$.
