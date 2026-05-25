---
title: "Torus Actions"
excerpt: "Actions of a torus and weight space decomposition"

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
translated_at: 2026-05-25T05:30:02+00:00
translation_source: kimi-cli
---
Given an arbitrary finite group $$G$$, one way to study it is through its finite-dimensional representation

$$\rho:G\rightarrow \Aut(V)$$

Once we choose a basis for $$V$$, understanding the image of $$G$$ under $$\rho$$ becomes a matter of linear algebra, so we can extract the structure of $$G$$ much more easily.

For Lie groups, this representation-theoretic perspective is even more helpful, because Lie groups act on other objects by their very nature—such as $$\GL(n;\mathbb{R})$$ or $$\Diff(M)$$.

However, if we define the representation theory of $$G$$ as in [\[Representation Theory\] §Representation Theory of Finite Groups, ⁋Definition 1](/en/math/representation_theory/representations_of_finite_groups#def1), we lose the smooth structure on the Lie group $$G$$. Thus we need the following definition.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> For a Lie group $$G$$, a *representation* of $$G$$ is a finite-dimensional vector space $$V$$ together with a smooth map

$$\rho:G\rightarrow \Aut(V)$$

</div>

If we regard $$G$$ as a Lie group with the discrete topology and the trivial smooth structure, this definition can be thought of as a generalization of [\[Representation Theory\] §Representation Theory of Finite Groups, ⁋Definition 1](/en/math/representation_theory/representations_of_finite_groups#def1). Similarly, all definitions in [\[Representation Theory\] §Representation Theory of Finite Groups, §§Basic Concepts of Representation Theory](/en/math/representation_theory/representations_of_finite_groups#표현론의-기본-개념들) can be carried over to Lie groups.

What played a crucial role above was the fact that $$G$$ was a finite group. For instance, the idea of averaging over all elements of $$G$$ relied on this. To generalize this to Lie groups, we need to impose some kind of finiteness condition on $$G$$.

Therefore, we often consider the case where $$G$$ is a *compact* Lie group. In this case, as a locally compact Hausdorff space, $$G$$ admits a Haar measure, so we can replace sums over elements of $$G$$ by integrals over $$G$$. Of course, this requires properly defining $$\delta_x$$ functions and generalizing function spaces appropriately, but we omit these details as they are beyond our current scope. The important point is that the representation theory of Lie groups can be approached by the same methods as that of finite groups. In particular, any finite-dimensional representation decomposes as a direct sum of irreducible ones.

On the other hand, given a finite-dimensional representation $$G\rightarrow\Aut(V)$$, the best thing about it is that we can think of the images $$\rho(g)$$ as matrices (via a choice of basis). Hence we can investigate it using our tools for matrices and linear maps.

One of the most important tools in linear algebra is diagonalization. Thus, for a given Lie group action $$\rho:G \rightarrow \Aut(V)$$, we are interested in choosing a basis of $$V$$ so that the matrix representation of each $$\rho(g)$$ becomes diagonal. If $$G$$ were finite, we could find such a basis for each $$g$$ individually, but since $$G$$ is now infinite this is difficult. Therefore, we naturally become interested in elements that are simultaneously diagonalizable. Now, [\[Linear Algebra\] §Eigenspace Decomposition, ⁋Proposition 10](/en/math/linear_algebra/eigenspace_decomposition#prop10) tells us that two diagonalizable matrices are simultaneously diagonalizable if and only if they commute, so the following definition is justified.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> For a compact, connected Lie group $$G$$, a subgroup $$T$$ of $$G$$ is called a *maximal torus* if $$T$$ is a torus and is maximal with respect to inclusion.

</div>

Given any element $$X$$ of the Lie algebra $$\mathfrak{g}$$, the closure of the one-parameter subgroup traced out by the exponential map in this direction becomes a torus. Hence the existence of a maximal torus is immediate from [\[Set Theory\] §Axiom of Choice, ⁋Theorem 4](/en/math/set_theory/axiom_of_choice#thm4).

It is worth noting that one might easily fall into the misconception that the one-parameter group $$\exp(tX)$$ considered above will always produce a one-dimensional torus, but this is not always the case. For example, consider the two-dimensional torus

$$T^2\cong \mathbb{R}^2/\mathbb{Z}^2$$

Before taking the quotient, the one-parameter subgroup in the direction $$(1,\sqrt{2})$$ densely covers all of $$T^2$$, and the closure of this image is precisely all of $$T^2$$. An element $$t\in T$$ satisfying

$$T=\overline{\langle t\rangle}$$

is called a *generator* of $$T$$.

## Weight Decomposition

Our claim is that $$\rho(T)$$ is simultaneously diagonalizable. To show this, it suffices to prove that each element of $$\rho(T)$$ is diagonalizable. To this end, consider an arbitrary finite-dimensional representation $$\rho:G\rightarrow \Aut(V)$$ and its restriction $$\rho\vert_T$$ to a maximal torus $$T$$. The first thing to check is that $$T$$ is a compact Lie group. Therefore, both [\[Representation Theory\] §Representation Theory of Finite Groups, ⁋Proposition 6](/en/math/representation_theory/representations_of_finite_groups#prop6) and [\[Representation Theory\] §Representation Theory of Finite Groups, ⁋Lemma 8](/en/math/representation_theory/representations_of_finite_groups#lem8) hold.

Writing these out in more detail, first, since $$\rho\vert_T$$ is a unitary representation, we obtain the following irreducible decomposition

$$V=\bigoplus_i V_i$$

where each $$V_\lambda$$ is an irreducible $$T$$-representation. On the other hand, since $$T$$ is abelian, for any $$t\in T$$, $$\rho(t)$$ commutes with the entire $$T$$-action, and hence the restriction of $$\rho(t)$$ to each $$V_i$$ is a $$T$$-automorphism. Now, by the second result of [\[Representation Theory\] §Representation Theory of Finite Groups, ⁋Lemma 8](/en/math/representation_theory/representations_of_finite_groups#lem8), $$\rho(t)$$ acts as a scalar multiple

$$\rho(t)(v)=\lambda_i(t)v\qquad \lambda_i(t)\in \mathbb{C}^\times$$

But if $$T$$ acts on $$V_i$$ by scalar multiples, then any subspace of $$V_i$$ is $$T$$-invariant, so for $$V_i$$ to be irreducible we must have $$\dim V_i=1$$.

Now since $$\dim V_i=1$$, we have $$\Aut(V_i)\cong \mathbb{C}^\times$$, and we see that the above $$\lambda_i: T\rightarrow \mathbb{C}^\times$$ corresponds exactly to a character of $$\rho$$, so the irreducible decomposition can be thought of as being directly parametrized by characters $$\lambda_i$$. That is, consider the irreducible decomposition given by the formula

$$$V=\bigoplus_\lambda V_\lambda;\qquad V_\lambda=\{t\cdot v=\lambda(t)v\text{ for all $$t\in T$$}\}$$$

Then for each $$t\in T$$, $$\rho(t)$$ is diagonalized by this decomposition, and the eigenvalue corresponding to each eigenspace $$V_\lambda$$ is $$\lambda(t)$$. A different choice of $$t$$ leaves the above decomposition unchanged and only changes the eigenvalue assigned to each eigenspace $$V_\lambda$$.

Intuitively, we can think of $$t\mapsto e^{2\pi i\lambda_i(X)}$$ as a rotation with angular velocity $$\lambda_i(X)$$, and adopting this viewpoint we see that for each $$X\in \mathfrak{t}$$, we can describe this torus action by asking what the angular velocity $$\lambda_i(X)$$ is in this direction. Each of these $$\lambda_i$$ is called a *weight*. Then for each weight $$\lambda_i$$, there is a corresponding $$V_i$$ on which the torus action operates by $$t\cdot v=\rchi_{\lambda_i}(t)v$$. Such a $$V_i$$ is called a *weight space*.

<div class="example" markdown="1">

<ins id="ex3">**Example 3**</ins> As a special example, consider the one-dimensional torus

$$S^1\cong T \cong \mathbb{R}/\mathbb{Z}$$

Then $$S^1$$ can be thought of as the set

$$S^1=\left\{e^{2\pi i t}\mid t\in \mathbb{R}/\mathbb{Z}\right\}$$

Now suppose this set acts on the two-dimensional vector space $$\mathbb{C}^2$$ by the formula

$$e^{2\pi i t}\cdot (z_1,z_2)=(e^{4\pi i t}z_1, e^{-2\pi i t}z_2)$$

This action may look contrived, but as we saw above, given any torus $$T$$ and any representation $$V$$, if we take the irreducible decomposition of $$V$$ and choose bases $$e_i$$ for each irreducible component, then every torus action can be written in this form (with a suitable choice of basis).

Writing this as a matrix, the above action is represented by the element (family of elements) of $$\GL(2;\mathbb{C})$$

$$\begin{pmatrix}e^{4\pi i t}&0\\0&e^{-2\pi i t}\end{pmatrix}$$

The trace of this matrix, $$e^{4\pi i t}+e^{-2\pi i t}$$, is precisely the character of this representation.

It is obvious that the weight spaces of this action are $$\span(e_1)$$ and $$\span(e_2)$$; for instance, the weight corresponding to $$\span(e_1)$$ is given by the linear functional $$\lambda_1:\mathfrak{t}\rightarrow \mathbb{C}$$ satisfying

$$$\rchi_{\lambda_1}(\exp (X))=e^{2\pi i \lambda_1(X)}\qquad\text{for all $$X\in \mathfrak{t}$$}$$$

This is of course defined by $$\lambda_1(t)=2t$$, which sends $$1\in \mathbb{R}$$ to $$2$$, and thus the weight corresponding to this weight space can be called $$2$$ (with a slight abuse of notation). For $$\lambda$$ to satisfy the above formula, since $$e^{2\pi i}=1$$, we must have $$\lambda(1)\in \mathbb{Z}$$.

More generally, if an action of an $$r$$-dimensional torus is given, then $$\mathfrak{t}$$ will be $$\mathbb{R}^r$$, and if we write the torus $$T$$ as

$$T^r=\left\{(e^{2\pi i t_1}, \ldots e^{2\pi i t_r})\mid t_i\in \mathbb{R}/\mathbb{Z}\right\}$$

then the elements that can be weights in $$\mathfrak{t}\cong \mathbb{R}^r$$ are those belonging to $$\mathbb{Z}^r$$, so a weight $$\lambda$$ is given by the $$r$$-tuple

$$\lambda=(n_1, \ldots, n_r)$$

Explicitly, this weight is the linear functional that outputs $$n_1x_1+\cdots+n_rx_r$$ when given arbitrary $$X=(x_1,\ldots, x_r)\in \mathfrak{t}$$.

</div>

Just as in eigenspace decompositions in linear algebra, the multiplicity of each weight need not be $$1$$. For example, consider the torus action

$$e^{2\pi i t}\cdot(z_1, z_2)=(e^{4\pi i t}z_1, e^{4\pi i t} z_2)$$

This time $$T$$ acts on the two-dimensional space $$\mathbb{C}^2$$ as if it had weight $$2$$. Collecting components that share the same weight $$\lambda$$ into a single space $$V_\lambda$$, we obtain the *weight space decomposition* $$V=\bigoplus V_\lambda$$. Writing our discussion so far rigorously as a definition, we have the following.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> Let a torus $$T$$ and a complex $$T$$-module $$V$$ be given. For an irreducible character $$\rchi_\lambda: T \rightarrow S^1$$ and the corresponding linear functional $$\lambda:\mathfrak{t}\rightarrow\mathbb{C}$$, we say that $$\lambda$$ is a *weight* of $$V$$ if the set

$$$V_\lambda=\left\{v\in V\mid t\cdot v=\rchi_\lambda(t)v\text{ for all $$t\in T$$}\right\}$$$

is nontrivial. We call $$V_\lambda$$ the *weight space* of $$\lambda$$, and the decomposition

$$V=\bigoplus_\lambda V_\lambda$$

is called the *weight decomposition* of $$V$$.

</div>

## Maximal Tori

In this section we show that any element of a compact connected Lie group $$G$$ is always contained in some maximal torus, and that all maximal tori are conjugate to each other.

Our claim is that for a compact connected Lie group $$G$$ and its maximal torus $$T$$, the map

$$q: G/T\times T\rightarrow G; \qquad (g,t)\mapsto gtg^{-1}$$

is surjective. Then in particular, for any other torus $$T'$$ and its generator $$t'$$, we could find $$t\in T$$ satisfying $$gtg^{-1}=t'$$, and using the maximality of $$T$$ and $$T'$$ respectively would prove the two claims mentioned above.

We can determine not only that this map is surjective, but also its explicit mapping degree. For this purpose, we make the following definition.

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> For a compact, connected Lie group $$G$$, a maximal torus $$T$$, and the normalizer of $$T$$

$$N=\{g\in G\mid gTg^{-1}=T\}$$

we define the group $$W=N/T$$ to be the *Weyl group* of $$G$$.

</div>

Then the following holds.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> The Weyl group $$W=N/T$$ is always finite.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

By definition, $$N$$ acts on $$T$$ by conjugation

$$N\rightarrow\Aut(T);\qquad n\mapsto (t\mapsto ntn^{-1})$$

Now $$\Aut(T)$$ is determined by where the lattice of the torus $$T=\mathbb{R}^k/\mathbb{Z}^k$$ is sent, and this is embedded in $$\GL(k;\mathbb{Z})$$ via $$\Ad(n)$$. That is, this action can be thought of as a continuous map from $$N$$ to $$\GL(k;\mathbb{Z})$$. Since $$\GL(k;\mathbb{Z})$$ is discrete, considering the identity component $$N_0$$ of $$N$$, all of $$N_0$$ must map to the identity matrix. In other words, $$N_0$$ acts trivially on $$T$$.

Now for any one-parameter subgroup $$\alpha:\mathbb{R}\rightarrow N_0$$, we must have $$\alpha(\mathbb{R})\cdot T=T$$, and from this we see that $$\alpha(\mathbb{R})\subset T$$. But by [\[Differential Manifolds\] §Vector Fields, ⁋Theorem 6](/en/math/manifold/vector_fields#thm6), these cover some open neighborhood of the identity in $$N_0$$, and hence generate $$N_0$$. That is, $$N_0=T$$.

Therefore $$N/T$$ is exactly the number of connected components of $$N$$, and since $$N$$ is a closed subspace of the compact Lie group $$G$$, it is likewise compact, so this cannot be infinite.

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

For this, first choose a generator $$t$$ of $$T$$ and consider its preimage $$q^{-1}(t)$$. For arbitrary $$(gT,s)\in G/T\times T$$, the condition $$q(gT,s)=t$$ means $$gsg^{-1}=t$$. On the other hand, $$g^{-1}tg=s\in T$$, and

$$\overline{\langle s\rangle}=g^{-1}\overline{\langle t\rangle}g=g^{-1}Tg$$

and since $$s\in T$$, we have $$g^{-1}Tg\subseteq T$$. But conjugation is a homeomorphism, so $$g^{-1}Tg$$ is a torus isomorphic to $$T$$, and hence $$g^{-1}Tg=T$$ and $$g\in N=N_G(T)$$. Moreover, since $$s=g^{-1}tg=(gT)\cdot t$$, we have

$$q^{-1}(t)=\{(gT, (gT)\cdot t)\mid gT\in W\}$$

where $$W$$ is the Weyl group defined as $$N/T$$, and we see that $$q^{-1}(t)$$ is in one-to-one correspondence with $$W$$.

Thus what remains is to show that all of these have the same sign, so that the mapping degree comes out exactly as $$\lvert W\rvert$$. For this, we identify the tangent spaces of $$G/T\times T$$ and $$G$$ with $$\mathfrak{g}$$. Specifically, decomposing the Lie algebra $$\mathfrak{g}$$ into the direct sum of $$\mathfrak{t}$$ and its orthogonal complement $$\mathfrak{f}=\mathfrak{t}^\perp$$

$$\mathfrak{g}=\mathfrak{t}\oplus\mathfrak{f}$$

then near the origin, the tangent space of $$T$$ is $$\mathfrak{t}$$ and the tangent space of $$G/T$$ is $$\mathfrak{f}$$. Hence the tangent space of $$G/T\times T$$ is $$\mathfrak{t}\oplus\mathfrak{f}\cong\mathfrak{g}$$.

On the other hand, for arbitrary $$X\in\mathfrak{t}$$ and $$Y\in\mathfrak{f}$$, the differential of $$q$$ at $$(eT,t)$$ is computed as follows. For the direction $$X$$, i.e., variation in the $$T$$ direction,

$$d q_{(eT,t)}(X,0)=\frac{d}{d\epsilon}\bigg\vert_{\epsilon=0}q(eT, t\exp(\epsilon X))=\frac{d}{d\epsilon}\bigg\vert_{\epsilon=0}t\exp(\epsilon X)=X$$

Here we used that $$T$$ is abelian, so $$t$$ and $$\exp(\epsilon X)$$ commute. Next, for the direction $$Y$$, i.e., variation in the $$G/T$$ direction,

$$d q_{(eT,t)}(0,Y)=\frac{d}{d\epsilon}\bigg\vert_{\epsilon=0}q(\exp(\epsilon Y)T, t)=\frac{d}{d\epsilon}\bigg\vert_{\epsilon=0}\exp(\epsilon Y)t\exp(-\epsilon Y)$$

Now writing $$t=\exp(H)$$ ($$H\in\mathfrak{t}$$),

$$\exp(\epsilon Y)t\exp(-\epsilon Y)=\exp(\epsilon Y)\exp(H)\exp(-\epsilon Y)=\exp(\Ad_{\exp(\epsilon Y)}(H))=\exp(e^{\epsilon\ad_Y}H)$$

and therefore

$$\frac{d}{d\epsilon}\bigg\vert_{\epsilon=0}\exp(\epsilon Y)t\exp(-\epsilon Y)=\frac{d}{d\epsilon}\bigg\vert_{\epsilon=0}\exp(H+\epsilon[Y,H])=\exp(H)\cdot [Y,H]$$

Here, since $$\mathfrak{t}$$ is abelian, $$[Y,H]\in\mathfrak{f}$$, and since $$\exp(H)=t$$, this can be written as $$t\cdot(\Ad_t^{-1}(Y)-Y)$$. Summarizing, under suitable identifications,

$$d q_{(eT,t)}=\begin{pmatrix} I & 0 \\ 0 & \Ad_t^{-1}\vert_\mathfrak{f}-I \end{pmatrix}$$

where the first block corresponds to the $$\mathfrak{t}$$ direction and the second block to the $$\mathfrak{f}$$ direction.

Now we show that $$\Ad_t^{-1}\vert_\mathfrak{f}-I$$ is invertible, and that the signs match at all preimages. If there existed $$Y\in\mathfrak{f}$$ with $$(\Ad_t^{-1}-I)Y=0$$, then $$\Ad_t(Y)=Y$$. Then for any integer $$m$$, $$\Ad_{t^m}(Y)=Y$$, and from the assumption that $$t$$ is a generator, $$\Ad_s(Y)=Y$$ for all $$s\in T$$. Now for arbitrary $$H\in\mathfrak{t}$$,

$$[H,Y]=\frac{d}{d\epsilon}\bigg\vert_{\epsilon=0}\Ad_{\exp(\epsilon H)}(Y)=0$$

so $$Y$$ commutes with every element of $$\mathfrak{t}$$. But since $$\mathfrak{t}$$ is a maximal abelian subalgebra, $$Y\in\mathfrak{t}$$, and hence $$Y\in\mathfrak{f}\cap\mathfrak{t}=\{0\}$$. That is, $$\Ad_t^{-1}\vert_\mathfrak{f}-I$$ is invertible.

Finally, let us verify that the determinant of $$dq$$ has the same sign at all points of $$q^{-1}(t)$$. Choose arbitrary $$w\in W$$ and let it be represented by $$x\in N$$. Then $$q(xT,x^{-1}tx)=t$$, so $$(xT, x^{-1}tx)\in q^{-1}(t)$$. To compute the differential at this point, from the definition of $$q$$,

$$q(gT, s)=gsg^{-1}$$

so considering left translation by $$x$$ and conjugation by $$x$$,

$$d q_{(xT, x^{-1}tx)}=\Ad_x\circ d q_{(eT, t)}\circ (\text{left translation})$$

In particular, both $$\Ad_x\vert_\mathfrak{f}$$ and $$\Ad_x\vert_\mathfrak{t}$$ are linear maps with determinant $$1$$ (the former because it is an orthogonal map, the latter because $$x\in N$$ so $$\Ad_x$$ preserves $$\mathfrak{t}$$), and hence the determinant of $$d q_{(xT, x^{-1}tx)}$$ equals that of $$d q_{(eT,t)}$$.

On the other hand, $$\det(\Ad_t^{-1}\vert_\mathfrak{f}-I)$$ is the same for $$w\cdot t$$ as well. Indeed,

$$\Ad_{wt^{-1}w^{-1}}\vert_\mathfrak{f}-I=\Ad_w\circ(\Ad_t^{-1}\vert_\mathfrak{f}-I)\circ\Ad_w^{-1}$$

so these two operators are similar and therefore have the same determinant.

From the above, we have verified that $$t$$ is a regular value of $$q$$, that the number of elements in $$q^{-1}(t)$$ is $$\lvert W\rvert$$, and that the determinant of $$dq$$ has the same sign at every preimage point. Hence, with a suitable choice of orientation, $$\deg q=\lvert W\rvert$$.

</details>

As mentioned above, the core content of this section follows immediately from this lemma.

<div class="proposition" markdown="1">

<ins id="thm8">**Theorem 8**</ins> For a compact connected Lie group $$G$$, the following hold.

1. Any element of $$G$$ is contained in some maximal torus.
2. Any two maximal tori of $$G$$ are conjugate.

</div>

Thus, for any compact connected Lie group $$G$$ and maximal torus $$T$$, we obtain the decomposition

$$G=\bigcup_{g\in G}gTg^{-1}$$

This is called the *Cartan decomposition*.

## Weyl Group Parametrization

The Cartan decomposition tells us that each element of $$G$$ lies in some maximal torus, but we can describe this decomposition more explicitly. The key is that the map

$$q:G/T\times T\rightarrow G;\qquad (gT,t)\mapsto gtg^{-1}$$

defined in [Lemma 7](#lem7) is a $$\lvert W\rvert$$-to-1 covering. From this, each element of $$G$$ has $$\lvert W\rvert$$ preimages, and the relations among them are precisely described by the Weyl group.

Specifically, define the following $$W$$-action on $$G/T\times T$$:

$$w\cdot(gT, t)=(gw^{-1}T, wtw^{-1})$$

Then

$$q(w\cdot(gT,t))=q(gw^{-1}T, wtw^{-1})=gw^{-1}(wtw^{-1})wg^{-1}=gtg^{-1}=q(gT,t)$$

so $$q$$ is $$W$$-invariant, and hence induces a map from the orbit space $$(G/T\times T)/W$$ to $$G$$

$$(G/T\times T)/W\rightarrow G$$

[Lemma 7](#lem7) proves that this map is a bijection.

On the other hand, let $$\Conj(G)$$ denote the space of conjugacy classes of $$G$$. Then each conjugacy class

$$[g]=\{hgh^{-1}\mid h\in G\}$$

is described via $$T$$ and $$W$$ as follows.

<div class="proposition" markdown="1">

<ins id="prop9">**Proposition 9**</ins> Two elements of a maximal torus $$T$$ are conjugate in $$G$$ if and only if they lie in the same orbit under the Weyl group action.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Suppose two elements $$x,y$$ of $$T$$ are conjugate. That is, for some $$g\in G$$, $$gxg^{-1}=y$$. Now comparing $$T$$ and $$gTg^{-1}$$, they are maximal tori in the centralizer $$Z_G(y)$$. Hence there exists $$h\in Z_G(y)$$ such that $$T=h(gTg^{-1})h^{-1}$$, and from this $$(hg)x(hg)^{-1}=y$$ and $$hg\in N_G(T)$$. That is, $$y=(hgT)\cdot x$$, so $$x$$ and $$y$$ lie in the same $$W$$-orbit.

Conversely, if $$x,y$$ lie in the same $$W$$-orbit, they are trivially conjugate in $$G$$.

</details>

From this, we see that for each conjugacy class $$[g]$$, the intersection $$[g]\cap T$$ is exactly one $$W$$-orbit. Hence we obtain the following one-to-one correspondence.

<div class="proposition" markdown="1">

<ins id="prop10">**Proposition 10**</ins> There is a natural one-to-one correspondence between $$T/W$$ and $$\Conj(G)$$.

</div>

Under this one-to-one correspondence, the conjugation action on $$G$$ acts trivially on $$T/W$$. That is, each element of $$G$$ preserves the conjugacy class to which it belongs.

## Decomposition of the Conjugation Action

Now let us examine the situation where $$G$$ acts on itself by conjugation. For this, for each $$g'\in G$$, define the conjugation map

$$c_{h}:G\rightarrow G;\qquad g\mapsto hgh^{-1}$$

Our goal is to transfer this to $$(G/T\times T)/W$$ and see concretely how it acts.

First, observe the following. For arbitrary $$(gT, t)\in G/T\times T$$ and $$h\in G$$,

$$c_{h}(gtg^{-1})=h(gtg^{-1})h^{-1}=(hg)t(hg)^{-1}=q(hgT, t)$$

holds. That is, when we pull back $$c_h$$ to $$G/T\times T$$ via the identification $$(G/T\times T)/W\cong G$$, $$c_h$$ sends $$(gT, t)$$ to $$(hgT, t)$$, so we can think of the following $$G$$-action being defined on $$G/T\times T$$:

$$h\cdot(gT,t)=(hgT,t)$$

Now it is trivial that this action commutes with the $$W$$-action, and hence $$G$$ induces a well-defined action on the quotient $$(G/T\times T)/W$$. From this observation we obtain the following.

<div class="proposition" markdown="1">

<ins id="prop11">**Proposition 11**</ins> Under the identification $$(G/T\times T)/W\cong G$$, the conjugation action is expressed as

$$h\cdot[(gT,t)]=[(hgT,t)]$$

That is, it acts by left multiplication on the $$G/T$$ component and preserves the $$T$$ component.

</div>

On the other hand, by [Proposition 10](#prop10), we know that there is a one-to-one correspondence between $$T/W$$ and $$\Conj(G)$$. By definition, $$c_h$$ does not change the conjugacy class in $$G$$, and we can verify that this is reflected in the absence of change in the $$T$$ direction in the above proposition. Instead, the conjugation action can be thought of as acting precisely on $$G/T$$.

To understand the $$G$$-action on $$G/T$$ in more detail, we will rewrite this space using the Weyl group. First, for $$N=N(T)$$, consider the projection map

$$\pi: G/T\rightarrow G/N;\qquad gT\mapsto gN$$

Then for each coset $$gN\in G/N$$, its fiber is

$$\pi^{-1}(gN)=\{hT\mid h\in gN\}=\{gxT\mid x\in N\}$$

and since $$g$$ is fixed, this fiber is essentially $$\{xT\mid x\in N\}$$, that is, the same as $$N/T$$. Moreover, topologically $$\pi$$ is exactly a $$\lvert W\rvert$$-fold covering map. ([\[Algebraic Topology\] §Covering Spaces, ⁋Definition 3](/en/math/algebraic_topology/covering_spaces#def3)) More precisely, this is a principal $$W$$-bundle with each fiber being $$W$$.

## Example: $$\SU(2)$$

Let us verify the discussion so far for the compact connected Lie group

$$\SU(2)=\{A\in\GL(2;\mathbb{C})\mid A^\dagger A=I,\det A=1\}=\left\{\begin{pmatrix}\alpha&-\overline{\beta}\\\beta&\overline{\alpha}\end{pmatrix}\,\middle\vert\;\alpha,\beta\in \mathbb{C},\lvert\alpha\rvert^2+\lvert\beta\rvert^2=1\right\}$$

First we need to find a maximal torus of $$\SU(2)$$. Our claim is that the set

$$T=\left\{\begin{pmatrix}e^{i\theta}&0\\0&e^{-i\theta}\end{pmatrix}\,\middle\vert \;\theta\in\mathbb{R}/2\pi\mathbb{Z}\right\}$$

is a maximal torus of $$\SU(2)$$. That $$T$$ is a one-dimensional torus is obvious, so it suffices to show maximality. For this, suppose $$A$$ is an abelian subgroup of $$\SU(2)$$ containing $$T$$. Then any element

$$\begin{pmatrix}a&b\\c&d\end{pmatrix}\in A$$

must commute with every element of $$T$$, so in particular it must commute with

$$\begin{pmatrix}i&0\\0&-i\end{pmatrix}$$

and computing this,

$$\begin{pmatrix}a&b\\c&d\end{pmatrix}\begin{pmatrix}i&0\\0&-i\end{pmatrix}=\begin{pmatrix}ai&-bi\\ci&-di\end{pmatrix},\qquad \begin{pmatrix}i&0\\0&-i\end{pmatrix}\begin{pmatrix}a&b\\c&d\end{pmatrix}=\begin{pmatrix}ai&bi\\-ci&-di\end{pmatrix}$$

so from this we see that $$b=c=0$$. Hence $$A\subset T$$.

Now to compute the Weyl group, we show that the normalizer $$N=N_{\SU(2)}(T)$$ of $$T$$ is given by the formula

$$N=T\cup \begin{pmatrix}0&1\\-1&0\end{pmatrix}T$$

First, for arbitrary $$g\in \SU(2)$$, writing

$$g=\begin{pmatrix}a&b\\c&d\end{pmatrix}$$

we have

$$g \begin{pmatrix}e^{i\theta}&0\\0&e^{-i\theta}\end{pmatrix}g^{-1} = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} e^{i\theta} & 0 \\ 0 & e^{-i\theta} \end{pmatrix} \begin{pmatrix} \overline{a} & \overline{c} \\ \overline{b} & \overline{d} \end{pmatrix} = \begin{pmatrix} \lvert\alpha\rvert^2 e^{i\theta} + \lvert b\rvert^2 e^{-i\theta} & a\overline{c}e^{i\theta} + b\overline{d}e^{-i\theta} \\ c\overline{a}e^{i\theta} + d\overline{b}e^{-i\theta} & \lvert c\rvert^2 e^{i\theta} + \lvert d\rvert^2 e^{-i\theta} \end{pmatrix}$$

so for this to lie in $$T$$, we must have

$$a\overline{c}e^{i\theta}+b\overline{d}e^{-i\theta}=0$$

for all $$\theta$$, hence $$a\overline{c}=0$$ and $$b\overline{d}=0$$. If $$a\neq 0$$, then $$\overline{c}=0$$ so $$c=0$$, and from $$ad-bc=1$$ we get $$d=\overline{a}$$, and thus from $$b\overline{d}=0$$ we must have $$b=0$$. That is, in this case $$g\in T$$. If $$a=0$$, then from $$\lvert a\rvert^2+\lvert b\rvert^2=1$$ we have $$\lvert b\rvert=1$$, and from $$ad-bc=1$$ we must have $$c=\overline{b}$$, and similarly $$d=0$$. Hence $$g$$ must be of the form

$$\begin{pmatrix}0&e^{i\alpha}\\ -e^{-i\alpha}&0\end{pmatrix}$$

and from this we can verify that $$N$$ is given by the above formula. Moreover, the nontrivial element of the Weyl group $$W\cong\mathbb{Z}_2$$ corresponds to $$\begin{pmatrix}0&1\\-1&0\end{pmatrix}$$, and the action of this element on $$T$$ is

$$\begin{pmatrix}0&1\\-1&0\end{pmatrix}\begin{pmatrix}e^{i\theta}&0\\0&e^{-i\theta}\end{pmatrix}\begin{pmatrix}0&-1\\1&0\end{pmatrix}=\begin{pmatrix}e^{-i\theta}&0\\0&e^{i\theta}\end{pmatrix}$$

so it corresponds to the reflection $$\theta\mapsto -\theta$$ on the torus $$S^1$$.

Now consider the standard representation of $$\SU(2)$$ on $$\mathbb{C}^2$$. Then $$\Aut(\mathbb{C}^2)=\GL(2;\mathbb{C})$$, so the representation $$\rho:\SU(2)\rightarrow \GL(2;\mathbb{C})$$ is just the inclusion. The same holds for its restriction to the torus $$T$$, and from this we see that the weights of $$T$$ are $$\theta$$ and $$-\theta$$, the corresponding weight spaces are $$\mathbb{C}e_1$$ and $$\mathbb{C}e_2$$, and the weight decomposition is $$\mathbb{C}e_1\oplus \mathbb{C}e_2$$. We can verify that on this space, the Weyl group acts by interchanging the weights.

## Weyl Chamber

Finally, we look at a definition that gives a taste of the motivation for the root system to be covered in the next post. In [Lemma 7](#lem7), we computed the preimage of $$q$$ at a generator $$t$$ of $$T$$ and checked that there are $$\lvert W\rvert$$ of them. Now that we know $$W$$ acts on $$T$$, we can write this condition as follows.

<div class="definition" markdown="1">

<ins id="def12">**Definition 12**</ins> An element $$t$$ of a maximal torus $$T$$ is called *regular* if the only $$w\in W$$ satisfying $$wtw^{-1}=t$$ is $$w=e$$. Conversely, if there exists $$w\neq e$$ with $$wtw^{-1}=t$$, then $$t$$ is called *singular*.

</div>

That is, a regular element is one whose stabilizer under the Weyl group action is trivial, and a singular element is one with a nontrivial stabilizer. In general, to compute the mapping degree of $$q$$, one must evaluate at a regular value of $$q$$; thinking of the orbit-stabilizer theorem, for the preimage to have $$\lvert W\rvert$$ images, the stabilizer must necessarily be trivial. Hence it is natural to call such elements regular.

<div class="example" markdown="1">

<ins id="ex13">**Example 13**</ins> For $$\SU(2)$$, we have $$T=\{\text{diag}(e^{i\theta}, e^{-i\theta})\}$$ and $$W=\mathbb{Z}_2$$ acting by $$\theta\mapsto -\theta$$. Therefore:

- **Regular:** Elements with $$\theta \neq 0, \pi$$. These are not fixed points of the reflection.
- **Singular:** $$\theta=0$$ (the identity) and $$\theta=\pi$$ ($$\text{diag}(-1,-1)$$). These are fixed by the reflection.

On the torus $$T\cong S^1$$, there are exactly two singular elements, and the regular elements are their complement.

</div>

In general, the following holds.

<div class="proposition" markdown="1">

<ins id="prop14">**Proposition 14**</ins> For a maximal torus $$T$$ of a compact connected Lie group $$G$$:

1. The regular elements form a dense open subset of $$T$$.
2. The singular elements form a closed subset of codimension $$\geq 1$$ in $$T$$.
3. The set of singular elements is a union of finitely many subgroups.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

(1) and (2): For each $$w\in W$$, $$w\neq e$$, the fixed point set $$\{t\in T: wtw^{-1}=t\}$$ is a proper closed subgroup of $$T$$. The set of singular elements is a finite union of these, hence closed, and its complement (the regular elements) is dense and open.

(3): The fixed point set for each $$w\neq e$$ is a closed subgroup of $$T$$, and since $$W$$ is finite, the set of singular elements is a union of finitely many subgroups.

</details>

The set formed by the singular elements in $$T$$ divides the torus into several pieces. For example, in the case of $$\SU(2)$$, the two singular elements divide $$S^1$$ into two semicircles. On each semicircle the Weyl group defines a free action, and the Weyl group action serves to identify them with each other.

From this perspective, the quotient $$T_{\text{reg}}/W$$ of the regular elements of $$T$$ is a connected space, and this can be connected to the notion of a *Weyl chamber*. For $$\SU(2)$$, $$T_{\text{reg}}/W \cong (0,\pi)$$ is a one-dimensional interval, and this corresponds to a one-dimensional Weyl chamber.

For more general Lie groups, the singular elements divide the torus into several chambers, and each chamber serves as a fundamental domain for the Weyl group action. This is the geometric foundation for the root system and Weyl chambers to be discussed in the next post.

---

**References**

**[Bro]** Armand Borel, *Linear Algebraic Groups*, Graduate texts in mathematics, Springer, 1991.  
**[BtD]** Theodor Bröcker, Tammo tom Dieck, *Representations of Compact Lie Groups*, Graduate texts in mathematics, Springer, 1985.
