---
title: "Torus Action"
excerpt: "Torus actions and weight space decomposition"

categories: [Math / Lie Theory]
permalink: /en/math/lie_theory/torus_action
header:
    overlay_image: /assets/images/Math/Lie_Theory/Torus_Action.png
    overlay_filter: 0.5
sidebar: 
    nav: "Lie_theory-en"

date: 2026-02-24
last_modified_at: 2026-02-24
weight: 2
translated_at: 2026-05-20T22:30:02+00:00
translation_source: kimi-cli
---
Given an arbitrary finite group $$G$$, one way to study it carefully is to look at its finite-dimensional representation

$$\rho:G\rightarrow \Aut(V)$$

Once we choose a basis for $$V$$, handling the image of $$G$$ under $$\rho$$ is nothing but linear algebra, so we can understand the structure of $$G$$ much more easily.

For Lie groups, this representation-theoretic perspective is even more helpful, because Lie groups act on other objects, such as $$\GL(n;\mathbb{R})$$ or $$\Diff(M)$$.

However, if we define the representation theory of $$G$$ as in [\[Representation Theory\] §Representation Theory of Finite Groups, ⁋Definition 1](/en/math/representation_theory/representations_of_finite_groups#def1), we lose the smooth structure on the Lie group $$G$$, so we must define it as follows.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> For a Lie group $$G$$, a *representation* of $$G$$ is given by a finite-dimensional vector space $$V$$ and a smooth map

$$\rho:G\rightarrow \Aut(V)$$

</div>

If we regard $$G$$ as a Lie group with the discrete topology and the trivial smooth structure, this definition can be thought of as a generalization of [\[Representation Theory\] §Representation Theory of Finite Groups, ⁋Definition 1](/en/math/representation_theory/representations_of_finite_groups#def1). Similarly, all the definitions in [\[Representation Theory\] §Representation Theory of Finite Groups, §§Basic Concepts of Representation Theory](/en/math/representation_theory/representations_of_finite_groups#표현론의-기본-개념들) can be carried out for Lie groups as well.

What played an important role in that post was the fact that the group $$G$$ was finite. For example, the idea of averaging over all elements of $$G$$ was based on this fact. To generalize this to Lie groups, we must impose some kind of finiteness condition on $$G$$.

We therefore often treat the case where $$G$$ is a *compact* Lie group. In this case, as a locally compact Hausdorff space, $$G$$ admits a Haar measure, and so we can replace sums over elements of $$G$$ by integrals over all of $$G$$. Of course, to do this rigorously one must properly define the $$\delta_x$$ function and generalize the function space to an appropriate space, but such work is beyond our current purpose so we omit it. What is important is that the representation theory of Lie groups can also be approached by the same methods as the representation theory of finite groups. In particular, any finite-dimensional representation can be written as a direct sum of irreducible decompositions.

Meanwhile, given a finite-dimensional representation $$G\rightarrow\Aut(V)$$, the best thing is that we can think of their images $$\rho(g)$$ as matrices (by choosing a basis). Thus we can investigate it using our tools for matrices and linear maps.

One of the most important tools in linear algebra is diagonalization. Therefore, for a given Lie group action $$\rho:G \rightarrow \Aut(V)$$, we are interested in choosing a basis for $$V$$ so that the matrix representation of $$\rho(g)$$ becomes a diagonal matrix. If $$G$$ were a finite group, we could find such a basis for each $$g$$, but since $$G$$ is now infinite, this is difficult. Thus we naturally become interested in elements that are simultaneously diagonalizable. Now, since [\[Linear Algebra\] §Eigenspace Decomposition, ⁋Proposition 10](/en/math/linear_algebra/eigenspace_decomposition#prop10) tells us that two diagonalizable matrices are simultaneously diagonalizable if and only if they commute, it is reasonable to make the following definition.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> For a compact, connected Lie group $$G$$, a subgroup $$T$$ of $$G$$ is called a *maximal torus* if $$T$$ is a torus and is maximal with respect to inclusion.

</div>

Choosing an arbitrary element $$X$$ of the Lie algebra $$\mathfrak{g}$$, the closure of the one-parameter subgroup traced out by the exponential map in this direction becomes a torus. Therefore, the existence of a maximal torus is obvious by [\[Set Theory\] §Axiom of Choice, ⁋Theorem 4](/en/math/set_theory/axiom_of_choice#thm4).

One should be careful not to fall into the misconception that the one-parameter group $$\exp(tX)$$ we are considering will create a one-dimensional torus; this is not always the case. For example, consider the two-dimensional torus

$$T^2\cong \mathbb{R}^2/\mathbb{Z}^2$$

Before taking the quotient, the one-parameter subgroup in the direction $$(1,\sqrt{2})$$ densely covers the whole $$T^2$$, and the closure of its image is exactly the entire $$T^2$$. An element $$t\in T$$ satisfying

$$T=\overline{\langle t\rangle}$$

is called a *generator* of $$T$$.

## Weight Decomposition

Our claim is that $$\rho(T)$$ is simultaneously diagonalizable. To see this, it suffices to show that each element of $$\rho(T)$$ is diagonalizable. To this end, consider an arbitrary finite-dimensional representation $$\rho:G\rightarrow \Aut(V)$$ and its restriction $$\rho\vert_T$$ to a maximal torus $$T$$. The first thing to check is that $$T$$ is a compact Lie group. Therefore, both [\[Representation Theory\] §Representation Theory of Finite Groups, ⁋Proposition 6](/en/math/representation_theory/representations_of_finite_groups#prop6) and [\[Representation Theory\] §Representation Theory of Finite Groups, ⁋Lemma 8](/en/math/representation_theory/representations_of_finite_groups#lem8) hold.

Writing them out in more detail, first from the fact that $$\rho\vert_T$$ is a unitary representation we obtain the following irreducible decomposition

$$V=\bigoplus_i V_i$$

Here each $$V_\lambda$$ is an irreducible $$T$$-representation. On the other hand, since $$T$$ is abelian, for any $$t\in T$$, $$\rho(t)$$ commutes with all $$T$$-actions, and thus when restricted to each $$V_i$$, $$\rho(t)$$ is a $$T$$-automorphism. Now, by the second result of [\[Representation Theory\] §Representation Theory of Finite Groups, ⁋Lemma 8](/en/math/representation_theory/representations_of_finite_groups#lem8), $$\rho(t)$$ is given by a scalar multiple

$$\rho(t)(v)=\lambda_i(t)v\qquad \lambda_i(t)\in \mathbb{C}^\times$$

But now, if $$T$$ acts on $$V_i$$ by scalars, then any subspace of $$V_i$$ is $$T$$-invariant, and therefore for $$V_i$$ to be irreducible we must have $$\dim V_i=1$$.

Now since $$\dim V_i=1$$, we have $$\Aut(V_i)\cong \mathbb{C}^\times$$, and we can think of the above $$\lambda_i: T\rightarrow \mathbb{C}^\times$$ as exactly corresponding to the character of $$\rho$$, so that the irreducible decomposition is directly parametrized by characters $$\lambda_i$$. That is, through the formula

$$$V=\bigoplus_\lambda V_\lambda;\qquad V_\lambda=\{t\cdot v=\lambda(t)v\text{ for all $$t\in T$$}\}$$$

let us think of the irreducible decomposition as being given. Then for each $$t\in T$$, $$\rho(t)$$ is diagonalized by this decomposition, and the eigenvalue corresponding to each eigenspace $$V_\lambda$$ is $$\lambda(t)$$. A different choice of $$t$$ leaves the above decomposition unchanged and only changes the eigenvalue corresponding to each eigenspace $$V_\lambda$$.

Intuitively, we can think of $$t\mapsto e^{2\pi i\lambda_i(X)}$$ as a rotational motion with angular velocity $$\lambda_i(X)$$, and adopting this viewpoint we know that for each given $$X\in \mathfrak{t}$$, we can describe this torus action by the angular velocity $$\lambda_i(X)$$ in this direction. We call each such $$\lambda_i$$ a *weight*. Then we know that for each weight $$\lambda_i$$ there exists an appropriate $$V_i$$ on which the torus action operates as $$t\cdot v=\rchi_{\lambda_i}(t)v$$. Such a $$V_i$$ is called a *weight space*.

<div class="example" markdown="1">

<ins id="ex3">**Example 3**</ins> As a special example, consider the one-dimensional torus

$$S^1\cong T \cong \mathbb{R}/\mathbb{Z}$$

Then $$S^1$$ can be thought of as the set

$$S^1=\left\{e^{2\pi i t}\mid t\in \mathbb{R}/\mathbb{Z}\right\}$$

Now suppose this set acts on the two-dimensional vector space $$\mathbb{C}^2$$ by the formula

$$e^{2\pi i t}\cdot (z_1,z_2)=(e^{4\pi i t}z_1, e^{-2\pi i t}z_2)$$

This action may look artificial, but as we saw above, given any torus $$T$$ and any representation $$V$$, if we take the irreducible decomposition of $$V$$ and choose bases $$e_i$$ of the irreducible components, then every torus action appears (upon a suitable choice of basis) in this form.

Writing this as a matrix, the above action can be represented as the element (family of elements)

$$\begin{pmatrix}e^{4\pi i t}&0\\0&e^{-2\pi i t}\end{pmatrix}$$

of $$\GL(2;\mathbb{C})$$. Then the trace $$e^{4\pi i t}+e^{-2\pi i t}$$ of this matrix is exactly the character of this representation.

It is obvious that the weight spaces of this action are $$\span(e_1), \span(e_2)$$, and for example the weight corresponding to $$\span(e_1)$$ is given by the linear functional $$\lambda_1:\mathfrak{t}\rightarrow \mathbb{C}$$ satisfying the formula

$$$\rchi_{\lambda_1}(\exp (X))=e^{2\pi i \lambda_1(X)}\qquad\text{for all $$X\in \mathfrak{t}$$}$$$

This is of course defined by $$\lambda_1(t)=2t$$, which sends $$1\in \mathbb{R}$$ to $$2$$, and so the weight corresponding to this weight space can be called, with a slight abuse of notation, $$2$$. For $$\lambda$$ to satisfy the above formula, since $$e^{2\pi i}=1$$, we must have $$\lambda(1)\in \mathbb{\mathbb{Z}}$$.

More generally, if an action of an $$r$$-dimensional torus is given, $$\mathfrak{t}$$ will be $$\mathbb{R}^r$$, and writing the torus $$T$$ as

$$T^r=\left\{(e^{2\pi i t_1}, \ldots e^{2\pi i t_r})\mid t_i\in \mathbb{R}/\mathbb{Z}\right\}$$

then among the Lie algebra $$\mathfrak{t}\cong \mathbb{R}^r$$ the elements that can be weights are those belonging to $$\mathbb{Z}^r$$, and so a weight $$\lambda$$ is given by the $$r$$-tuple

$$\lambda=(n_1, \ldots, n_r)$$

Explicitly, this weight is the linear functional that outputs $$n_1x_1+\cdots+n_rx_r$$ when given an arbitrary $$X=(x_1,\ldots, x_r)\in \mathfrak{t}$$.

</div>

Just as in eigenspace decompositions in linear algebra, the multiplicity of each weight need not be $$1$$. For example, considering the torus action

$$e^{2\pi i t}\cdot(z_1, z_2)=(e^{4\pi i t}z_1, e^{4\pi i t} z_2)$$

this time $$T$$ acts as if it had weight $$2$$ on the two-dimensional space $$\mathbb{C}^2$$. Collecting components that have the same weight $$\lambda$$ in this way and calling it $$V_\lambda$$, we obtain a *weight space decomposition* $$V=\bigoplus V_\lambda$$. Writing our discussion so far rigorously as a definition, we have the following.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> Let a torus $$T$$ and a complex $$T$$-module $$V$$ be given. For an irreducible character $$\rchi_\lambda: T \rightarrow S^1$$ and the corresponding linear functional $$\lambda:\mathfrak{t}\rightarrow\mathbb{C}$$, we say that $$\lambda$$ is a *weight* of $$V$$ if the following set

$$$V_\lambda=\left\{v\in V\mid t\cdot v=\rchi_\lambda(t)v\text{ for all $$t\in T$$}\right\}$$$

is nontrivial. In this case, we call $$V_\lambda$$ the *weight space* of $$\lambda$$, and the decomposition

$$V=\bigoplus_\lambda V_\lambda$$

is called the *weight decomposition* of $$V$$.

</div>

## Maximal Torus

In this section we show that any element of a compact connected Lie group $$G$$ is always contained in some maximal torus, and that all maximal tori are conjugate to each other.

Our claim is that for a compact connected Lie group $$G$$ and its maximal torus $$T$$, the map

$$q: G/T\times T\rightarrow G; \qquad (g,t)\mapsto gtg^{-1}$$

is surjective. Then in particular, for any other torus $$T'$$ and its generator $$t'$$, we will be able to find $$t\in T$$ satisfying $$gtg^{-1}=t'$$, and using the maximality of $$T$$ and $$T'$$ respectively, the two claims mentioned above will be proved.

We can not only show that this map is surjective, but also compute its explicit mapping degree. For this, let us define the following.

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> For a compact, connected Lie group $$G$$, a maximal torus $$T$$, and the normalizer of $$T$$

$$N=\{g\in G\mid gTg^{-1}=T\}$$

we define the group $$W=N/T$$ as the *Weyl group* of $$G$$.

</div>

Then the following holds.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> The Weyl group $$W=N/T$$ is always finite.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

By definition, $$N$$ acts on $$T$$ by conjugation

$$N\rightarrow\Aut(T);\qquad n\mapsto (t\mapsto ntn^{-1})$$

Now, $$\Aut(T)$$ is determined by where the lattice of the torus $$T=\mathbb{R}^k/\mathbb{Z}^k$$ is sent, and this is embedded in $$\GL(k;\mathbb{Z})$$ via $$\Ad(n)$$. That is, this action can be thought of as a continuous function from $$N$$ to $$\GL(k;\mathbb{Z})$$. Since $$\GL(k;\mathbb{Z})$$ is discrete, if we consider the identity component $$N_0$$ of $$N$$, then $$N_0$$ must all be sent to the identity matrix. In other words, $$N_0$$ acts trivially on $$T$$.

Now, for any one-parameter subgroup $$\alpha:\mathbb{R}\rightarrow N_0$$, we must have $$\alpha(\mathbb{R})\cdot T=T$$, and from this we know that $$\alpha(\mathbb{R})\subset T$$ must hold. But by [\[Differential Manifolds\] §Vector Fields, ⁋Theorem 6](/en/math/manifold/vector_fields#thm6), these cover some open neighborhood of the identity in $$N_0$$, and thus generate $$N_0$$. That is, $$N_0=T$$.

Therefore, $$N/T$$ is exactly the number of connected components of $$N$$, and since $$N$$ is a closed subspace of the compact Lie group $$G$$, it is likewise compact, so this cannot be infinite.

</details>

Now our claim is as follows.

<div class="proposition" markdown="1">

<ins id="lem7">**Lemma 7**</ins> For a compact, connected Lie group $$G$$, a maximal torus $$T$$, and the map

$$q:G/T\times T\rightarrow G;\qquad (gT, s)\mapsto gsg^{-1}$$

the mapping degree of $$q$$ is $$\lvert W\rvert$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

To compute the mapping degree, we choose one regular value and find all its preimages, then compute the sign of the differential at each preimage.

For this, first choose a generator $$t$$ of $$T$$ and consider its preimage $$q^{-1}(t)$$. For an arbitrary $$(gT,s)\in G/T\times T$$, the condition $$q(gT,s)=t$$ means $$gsg^{-1}=t$$. On the other hand, $$g^{-1}tg=s\in T$$, and

$$\overline{\langle s\rangle}=g^{-1}\overline{\langle t\rangle}g=g^{-1}Tg$$

but since $$s\in T$$, we have $$g^{-1}Tg\subseteq T$$. However, conjugation is a homeomorphism, so $$g^{-1}Tg$$ is a torus isomorphic to $$T$$, and from this we know that $$g^{-1}Tg=T$$ and $$g\in N=N_G(T)$$. Moreover, since $$s=g^{-1}tg=(gT)\cdot t$$, we have

$$q^{-1}(t)=\{(gT, (gT)\cdot t)\mid gT\in W\}$$

Here $$W$$ is the Weyl group defined as $$N/T$$, and we see that $$q^{-1}(t)$$ is in one-to-one correspondence with $$W$$.

Thus it remains to show that they all have the same sign, so that the mapping degree comes out to be exactly $$\lvert W\rvert$$. For this, we identify the tangent spaces of $$G/T\times T$$ and $$G$$ with $$\mathfrak{g}$$. Specifically, decomposing the Lie algebra $$\mathfrak{g}$$ into the direct sum of $$\mathfrak{t}$$ and its orthogonal complement $$\mathfrak{f}=\mathfrak{t}^\perp$$

$$\mathfrak{g}=\mathfrak{t}\oplus\mathfrak{f}$$

then near the origin, the tangent space of $$T$$ is $$\mathfrak{t}$$ and the tangent space of $$G/T$$ is $$\mathfrak{f}$$. Therefore, the tangent space of $$G/T\times T$$ is $$\mathfrak{t}\oplus\mathfrak{f}\cong\mathfrak{g}$$.

Now, for arbitrary $$X\in\mathfrak{t}$$ and $$Y\in\mathfrak{f}$$, the differential of $$q$$ at $$(eT,t)$$ is computed as follows. For the direction $$X$$, that is, considering variation in the $$T$$ direction,

$$d q_{(eT,t)}(X,0)=\frac{d}{d\epsilon}\bigg\vert_{\epsilon=0}q(eT, t\exp(\epsilon X))=\frac{d}{d\epsilon}\bigg\vert_{\epsilon=0}t\exp(\epsilon X)=X$$

Here we used that $$T$$ is abelian, so $$t$$ and $$\exp(\epsilon X)$$ commute. Next, for the direction $$Y$$, that is, considering variation in the $$G/T$$ direction,

$$d q_{(eT,t)}(0,Y)=\frac{d}{d\epsilon}\bigg\vert_{\epsilon=0}q(\exp(\epsilon Y)T, t)=\frac{d}{d\epsilon}\bigg\vert_{\epsilon=0}\exp(\epsilon Y)t\exp(-\epsilon Y)$$

Now, writing $$t=\exp(H)$$ ($$H\in\mathfrak{t}$$), we have

$$\exp(\epsilon Y)t\exp(-\epsilon Y)=\exp(\epsilon Y)\exp(H)\exp(-\epsilon Y)=\exp(\Ad_{\exp(\epsilon Y)}(H))=\exp(e^{\epsilon\ad_Y}H)$$

and therefore

$$\frac{d}{d\epsilon}\bigg\vert_{\epsilon=0}\exp(\epsilon Y)t\exp(-\epsilon Y)=\frac{d}{d\epsilon}\bigg\vert_{\epsilon=0}\exp(H+\epsilon[Y,H])=\exp(H)\cdot [Y,H]$$

Here, since $$\mathfrak{t}$$ is abelian, $$[Y,H]\in\mathfrak{f}$$, and since $$\exp(H)=t$$, this can be written as $$t\cdot(\Ad_t^{-1}(Y)-Y)$$. Summarizing, under the appropriate identification,

$$d q_{(eT,t)}=\begin{pmatrix} I & 0 \\ 0 & \Ad_t^{-1}\vert_\mathfrak{f}-I \end{pmatrix}$$

where the first block corresponds to the $$\mathfrak{t}$$ direction and the second block to the $$\mathfrak{f}$$ direction.

Now we show that $$\Ad_t^{-1}\vert_\mathfrak{f}-I$$ is invertible and that the signs match at all preimages. If there exists $$Y\in\mathfrak{f}$$ such that $$(\Ad_t^{-1}-I)Y=0$$, then $$\Ad_t(Y)=Y$$. Then for any integer $$m$$ we have $$\Ad_{t^m}(Y)=Y$$, and by the assumption that $$t$$ is a generator, $$\Ad_s(Y)=Y$$ for all $$s\in T$$. Now, for any $$H\in\mathfrak{t}$$,

$$[H,Y]=\frac{d}{d\epsilon}\bigg\vert_{\epsilon=0}\Ad_{\exp(\epsilon H)}(Y)=0$$

so $$Y$$ commutes with every element of $$\mathfrak{t}$$. But since $$\mathfrak{t}$$ is a maximal abelian subalgebra, $$Y\in\mathfrak{t}$$, and therefore $$Y\in\mathfrak{f}\cap\mathfrak{t}=\{0\}$$. That is, $$\Ad_t^{-1}\vert_\mathfrak{f}-I$$ is invertible.

Finally, let us check whether the determinant of $$dq$$ has the same sign at all points of $$q^{-1}(t)$$. Choose an arbitrary $$w\in W$$ and let it be represented by $$x\in N$$. Then since $$q(xT,x^{-1}tx)=t$$, we have $$(xT, x^{-1}tx)\in q^{-1}(t)$$. To compute the differential at this point, from the definition of $$q$$

$$q(gT, s)=gsg^{-1}$$

considering left translation by $$x$$ and conjugation by $$x$$, we have

$$d q_{(xT, x^{-1}tx)}=\Ad_x\circ d q_{(eT, t)}\circ (\text{left translation})$$

In particular, both $$\Ad_x\vert_\mathfrak{f}$$ and $$\Ad_x\vert_\mathfrak{t}$$ are linear maps with determinant $$1$$ (the former because it is an orthogonal map, the latter because $$x\in N$$ implies $$\Ad_x$$ preserves $$\mathfrak{t}$$), and therefore the determinant of $$d q_{(xT, x^{-1}tx)}$$ equals that of $$d q_{(eT,t)}$$.

On the other hand, $$\det(\Ad_t^{-1}\vert_\mathfrak{f}-I)$$ is the same for $$w\cdot t$$ as well. Indeed,

$$\Ad_{wt^{-1}w^{-1}}\vert_\mathfrak{f}-I=\Ad_w\circ(\Ad_t^{-1}\vert_\mathfrak{f}-I)\circ\Ad_w^{-1}$$

so these two operators are similar and hence have the same determinant.

From the above, we have confirmed that $$t$$ is a regular value of $$q$$, that the number of elements in $$q^{-1}(t)$$ is $$\lvert W\rvert$$, and that the determinant of $$dq$$ has the same sign at every preimage point. Therefore, under a suitable choice of orientation, $$\deg q=\lvert W\rvert$$.

</details>

As mentioned above, the core content of this section follows immediately from this lemma.

<div class="proposition" markdown="1">

<ins id="thm8">**Theorem 8**</ins> For a compact connected Lie group $$G$$, the following hold.

1. Any element of $$G$$ is contained in some maximal torus.
2. Any two maximal tori of $$G$$ are always conjugate.

</div>

Therefore, for any compact connected Lie group $$G$$ and maximal torus $$T$$, we obtain the decomposition

$$G=\bigcup_{g\in G}gTg^{-1}$$

This is called the *Cartan decomposition*.

## Weyl Group Parametrization

The Cartan decomposition tells us that each element of $$G$$ belongs to some maximal torus, but we can describe this decomposition more explicitly. The key is the fact that the map

$$q:G/T\times T\rightarrow G;\qquad (gT,t)\mapsto gtg^{-1}$$

defined in [Lemma 7](#lem7) is a $$\lvert W\rvert$$-to-1 covering. From this, each element of $$G$$ has $$\lvert W\rvert$$ preimages, and the Weyl group exactly describes the relations among them.

Specifically, let us define the following $$W$$-action on $$G/T\times T$$:

$$w\cdot(gT, t)=(gw^{-1}T, wtw^{-1})$$

Then

$$q(w\cdot(gT,t))=q(gw^{-1}T, wtw^{-1})=gw^{-1}(wtw^{-1})wg^{-1}=gtg^{-1}=q(gT,t)$$

so $$q$$ is $$W$$-invariant, and therefore induces a map

$$(G/T\times T)/W\rightarrow G$$

from the orbit space. [Lemma 7](#lem7) proves that this map is a bijection.

Meanwhile, let $$\Conj(G)$$ denote the space of conjugacy classes of $$G$$. Then each conjugacy class

$$[g]=\{hgh^{-1}\mid h\in G\}$$

is described through $$T$$ and $$W$$ as follows.

<div class="proposition" markdown="1">

<ins id="prop9">**Proposition 9**</ins> Two elements of a maximal torus $$T$$ are conjugate in $$G$$ if and only if they belong to the same orbit of the Weyl group action.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$x,y$$ be two elements of $$T$$ that are conjugate to each other. That is, for some $$g\in G$$ we have $$gxg^{-1}=y$$. Comparing $$T$$ and $$gTg^{-1}$$, we see that they are maximal tori of the centralizer $$Z_G(y)$$. Therefore there exists $$h\in Z_G(y)$$ such that $$T=h(gTg^{-1})h^{-1}$$, from which $$(hg)x(hg)^{-1}=y$$ and $$hg\in N_G(T)$$. That is, $$y=(hgT)\cdot x$$, so $$x$$ and $$y$$ belong to the same $$W$$-orbit.

Conversely, if $$x,y$$ belong to the same $$W$$-orbit then they are obviously conjugate in $$G$$.

</details>

From this we know that for each conjugacy class $$[g]$$, the intersection $$[g]\cap T$$ is exactly one $$W$$-orbit. Therefore we obtain the following one-to-one correspondence.

<div class="proposition" markdown="1">

<ins id="prop10">**Proposition 10**</ins> There exists a natural one-to-one correspondence between $$T/W$$ and $$\Conj(G)$$.

</div>

Under this one-to-one correspondence, the conjugation action on $$G$$ acts trivially on $$T/W$$. That is, each element of $$G$$ preserves the conjugacy class to which it belongs.

## Decomposition of the Conjugation Action

Now let us examine the situation where $$G$$ acts on itself by conjugation. For this, for each $$g'\in G$$ we define the conjugation map

$$c_{h}:G\rightarrow G;\qquad g\mapsto hgh^{-1}$$

Our goal is to transfer this to $$(G/T\times T)/W$$ and see concretely how it acts.

First, observe the following. For any $$(gT, t)\in G/T\times T$$ and $$h\in G$$,

$$c_{h}(gtg^{-1})=h(gtg^{-1})h^{-1}=(hg)t(hg)^{-1}=q(hgT, t)$$

holds. That is, when we pull $$c_h$$ back to $$G/T\times T$$ via the identification $$(G/T\times T)/W\cong G$$, $$c_h$$ sends $$(gT, t)$$ to $$(hgT, t)$$, so we can think of the following $$G$$-action as being defined on $$G/T\times T$$:

$$h\cdot(gT,t)=(hgT,t)$$

Now it is obvious that this action commutes with the $$W$$-action, and therefore $$G$$ induces a well-defined action on the quotient $$(G/T\times T)/W$$ as well. From this observation we obtain the following.

<div class="proposition" markdown="1">

<ins id="prop11">**Proposition 11**</ins> Under the identification $$(G/T\times T)/W\cong G$$, the conjugation action is expressed as follows:

$$h\cdot[(gT,t)]=[(hgT,t)]$$

That is, it acts by left multiplication on the $$G/T$$ component and preserves the $$T$$ component.

</div>

Meanwhile, we know from [Proposition 10](#prop10) that there is a one-to-one correspondence between $$T/W$$ and $$\Conj(G)$$. By definition, $$c_h$$ does not change the conjugacy class in $$G$$, and we can check that this is reflected in the fact that there is no change in the $$T$$ direction in the above proposition. Instead, the conjugation action can be thought of as acting precisely on $$G/T$$.

To understand the $$G$$-action on $$G/T$$ in more detail, we will rewrite this space using the Weyl group. First, for $$N=N(T)$$, consider the projection map

$$\pi: G/T\rightarrow G/N;\qquad gT\mapsto gN$$

Then for each coset $$gN\in G/N$$, its fiber is

$$\pi^{-1}(gN)=\{hT\mid h\in gN\}=\{gxT\mid x\in N\}$$

and since $$g$$ is fixed, this fiber is essentially $$\{xT\mid x\in N\}$$, that is, the same as $$N/T$$
