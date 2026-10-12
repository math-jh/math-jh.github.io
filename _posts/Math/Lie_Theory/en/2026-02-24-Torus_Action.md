---
title: "Torus Actions"
description: "The representation theory of Lie groups is compared with that of finite groups, and finite-dimensional representations of compact Lie groups are discussed via Haar measure and irreducible decomposition."
excerpt: "Actions of a torus and weight space decomposition"

categories: [Math / Lie Theory]
permalink: /en/math/lie_theory/torus_action
sidebar: 
    nav: "Lie_theory-en"

date: 2026-02-24
weight: 2
translated_at: 2026-05-31T17:00:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-12T11:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
Given an arbitrary finite group $G$, one way to examine it closely is to look at its finite-dimensional representation

$$\rho:G\rightarrow \Aut(V)$$

Once we choose a basis for $V$, dealing with the image of $G$ under $\rho$ is merely linear algebra, so we can determine the structure of $G$ much more easily.

For Lie groups, this representation-theoretic perspective is even more helpful, because Lie groups such as $\GL(n;\mathbb{R})$ or $\Diff(M)$ are inherently things that act on other objects.

However, if we define the representation theory of $G$ as in [\[Representation Theory\] §Representation Theory of Finite Groups, ⁋Definition 1](/en/math/representation_theory/representations_of_finite_groups#def1){: data-lid="qmibx" }, we miss the smooth structure on the Lie group $G$, so we must define it as follows.

::: Definition 1
For a Lie group $G$, a *representation* of $G$ consists of a finite-dimensional vector space $V$ and a smooth homomorphism

$$\rho:G\rightarrow \Aut(V)$$
:::

If we regard $G$ as a Lie group equipped with the discrete topology and the trivial smooth structure, this definition can also be viewed as a generalization of [\[Representation Theory\] §Representation Theory of Finite Groups, ⁋Definition 1](/en/math/representation_theory/representations_of_finite_groups#def1){: data-lid="11bya" }. Similarly, all definitions in [\[Representation Theory\] §Representation Theory of Finite Groups, §§Basic Notions of Representation Theory](/en/math/representation_theory/representations_of_finite_groups#basic-notions-of-representation-theory){: data-lid="mqls6" } can be made for Lie groups as well.

What played an important role in that post was the fact that the group $G$ is a finite group. For instance, the idea of averaging over all elements of $G$ was based on this fact. To generalize this to Lie groups, we must impose some kind of finiteness on $G$.

We therefore often deal with the case where $G$ is a *compact* Lie group. In this case, as a locally compact Hausdorff space, there exists a Haar measure on $G$, and thus we can replace sums over the elements of $G$ with an integral over all of $G$. Of course, for this, one must go through the work of properly defining the $\delta_x$ function and generalizing the function space to a suitable space, but since this work is not our present objective, we omit it. What is important is that the representation theory of Lie groups can also be approached through the same methodology as the representation theory of finite groups. In particular, any finite-dimensional representation can be expressed as a direct sum of irreducible decompositions.

Meanwhile, given a finite-dimensional representation $G\rightarrow\Aut(V)$, the best aspect is that we can regard their images $\rho(g)$ as matrices (through a choice of basis). Therefore, through this, we can investigate this using our tools for matrices and linear maps.

One of the most important tools in linear algebra is diagonalization. Therefore, for a given Lie group action $\rho:G \rightarrow \Aut(V)$, we are interested in suitably choosing a basis of $V$ to make the matrix representation of $\rho(g)$ a diagonal matrix. If $G$ were a finite group, we could have found such a basis for each $g$, but currently, since $G$ is infinite, it is difficult to do this. Therefore, we naturally become interested in elements that are simultaneously diagonalizable. However, since we know from [\[Linear Algebra\] §Eigenspace Decomposition, ⁋Proposition 10](/en/math/linear_algebra/eigenspace_decomposition#prop10){: data-lid="uaxjr" } that two diagonalizable matrices that commute with each other are simultaneously diagonalizable, it is reasonable to make the following definition.

::: Definition 2
For a compact, connected Lie group $G$, a subgroup of $G$, $T$, is a *maximal torus* if $T$ is a torus and is maximal with respect to inclusion.
:::

If we choose in the Lie algebra $\mathfrak{g}$ an arbitrary element $X$, the closure of the one-parameter subgroup traced by the exponential map in this direction is a torus. Therefore, the existence of a maximal torus is immediate by [\[Set Theory\] §Axiom of Choice, ⁋Theorem 4](/en/math/set_theory/axiom_of_choice#thm4){: data-lid="7t2xc" }.

It should be noted that it is easy to mistakenly think that the one-parameter group $\exp(tX)$ considered above forms a one-dimensional torus, but this is not always the case. For example, considering the two-dimensional torus

$$T^2\cong \mathbb{R}^2/\mathbb{Z}^2$$

before taking the quotient, the one-parameter subgroup in the direction $(1,\sqrt{2})$ densely covers the whole $T^2$, and the closure of this image is precisely the whole $T^2$. An element satisfying

$$T=\overline{\langle t\rangle}$$

in this way, $t\in T$, is called a *generator* of $T$.

## Weight decomposition

Our claim is that $\rho(T)$ is simultaneously diagonalizable. For this, it suffices to show that each element of $\rho(T)$ is diagonalizable. To this end, consider an arbitrary finite-dimensional representation $\rho:G\rightarrow \Aut(V)$, and restricting it to the maximal torus $T$, consider the representation $\rho\vert_T$. The first thing that can be checked is the fact that $T$ is a compact Lie group. Therefore, both [\[Representation Theory\] §Representation Theory of Finite Groups, ⁋Proposition 6](/en/math/representation_theory/representations_of_finite_groups#prop6){: data-lid="r86tg" } and [\[Representation Theory\] §Representation Theory of Finite Groups, ⁋Lemma 8](/en/math/representation_theory/representations_of_finite_groups#lem8){: data-lid="i0it7" } hold.

Writing these out in more detail one by one, first from the fact that $\rho\vert_T$ is a unitary representation, we can consider the following irreducible decomposition

$$V=\bigoplus_i V_i$$

Here each $V_i$ is an irreducible $T$-representation. Meanwhile, since $T$ is abelian, for any $t\in T$, $\rho(t)$ commutes with all the $T$-actions, and thus when restricted to each $V_i$, $\rho(t)$ is a $T$-automorphism. Now by the second result of [\[Representation Theory\] §Representation Theory of Finite Groups, ⁋Lemma 8](/en/math/representation_theory/representations_of_finite_groups#lem8){: data-lid="tzupu" }, $\rho(t)$ is given by a scalar multiple

$$\rho(t)(v)=\lambda_i(t)v\qquad \lambda_i(t)\in \mathbb{C}^\times$$

Now, if on $V_i$, $T$ acts by scalar multiples, then any subspace of $V_i$ will be $T$-invariant, and therefore for $V_i$ to be irreducible, we must have $\dim V_i=1$.

Now since $\dim V_i=1$, we have $\Aut(V_i)\cong \mathbb{C}^\times$, and we can think of the above $\lambda_i: T\rightarrow \mathbb{C}^\times$ as corresponding precisely to the character of $V_i$, so that the irreducible decomposition can be thought of as being directly parametrized by the characters $\lambda_i$. That is, let us consider the irreducible decomposition as being given by the equation

$$V=\bigoplus_\lambda V_\lambda;\qquad V_\lambda=\{v\in V\mid t\cdot v=\lambda(t)v\text{ for all $t\in T$}\}$$

Then for each $t\in T$, $\rho(t)$ is diagonalized by this very decomposition, and the eigenvalue corresponding to each eigenspace $V_\lambda$ is $\lambda(t)$. A different choice of $t$ leaves the above decomposition unchanged and only changes the eigenvalue corresponding to each eigenspace $V_\lambda$.

Intuitively, we can think of $t\mapsto e^{2\pi i t\lambda_i(X)}$ as an angular motion with angular velocity $\lambda_i(X)$, and adopting this perspective, we know that when each $X\in \mathfrak{t}$ is given, we can describe this torus action through what the angular velocity $\lambda_i(X)$ in this direction is. In this case, we call each $\lambda_i$ a *weight*. Then we know that for each weight $\lambda_i$, there exists an appropriate $V_i$ on which the torus action operates as $t\cdot v=\rchi_{\lambda_i}(t)v$. Such a $V_i$ is called a *weight space*.

::: Example 3
As a special example, consider the one-dimensional torus

$$S^1\cong T \cong \mathbb{R}/\mathbb{Z}$$

Then $S^1$ can be thought of as the set

$$S^1=\left\{e^{2\pi i t}\mid t\in \mathbb{R}/\mathbb{Z}\right\}$$

Now suppose this set acts on the two-dimensional vector space $\mathbb{C}^2$ by the formula

$$e^{2\pi i t}\cdot (z_1,z_2)=(e^{4\pi i t}z_1, e^{-2\pi i t}z_2)$$

This action may look artificial, but as we saw above, given any torus $T$ and any representation $V$, if we consider the irreducible decomposition of $V$ and choose a basis $e_i$ for each irreducible component, we know that every torus action takes this form (by an appropriate choice of basis).

Writing this as a matrix, the above action can be represented by the element (family of elements) of $\GL(2;\mathbb{C})$

$$\begin{pmatrix}e^{4\pi i t}&0\\0&e^{-2\pi i t}\end{pmatrix}$$

Here, the trace $e^{4\pi i t}+e^{-2\pi i t}$ of this matrix is precisely the character of this representation.

The weight spaces of this action are obviously $\span(e_1), \span(e_2)$, and for example, the weight corresponding to $\span(e_1)$ is given by the linear functional $\lambda_1:\mathfrak{t}\rightarrow \mathbb{R}$ satisfying

$$\rchi_{\lambda_1}(\exp (X))=e^{2\pi i \lambda_1(X)}\qquad\text{for all $X\in \mathfrak{t}$}$$

This is of course defined by $\lambda_1(t)=2t$, which sends $1\in \mathbb{R}$ to $2$, and thus the weight corresponding to this weight space can be said to be $2$ (with a slight abuse of notation). Here, for $\lambda$ to satisfy the above equation, since $e^{2\pi i}=1$, we must have $\lambda(1)\in \mathbb{Z}$.

More generally, if an action of an $r$-dimensional torus is given, then $\mathfrak{t}$ will be $\mathbb{R}^r$, and if we write the torus $T$ as

$$T^r=\left\{(e^{2\pi i t_1}, \ldots e^{2\pi i t_r})\mid t_i\in \mathbb{R}/\mathbb{Z}\right\}$$

then among the dual $\mathfrak{t}^\ast\cong \mathbb{R}^r$ of its Lie algebra, the elements that can be weights are those belonging to $\mathbb{Z}^r$, and thus a weight $\lambda$ will be given by the following $r$-tuple

$$\lambda=(n_1, \ldots, n_r)$$

Explicitly, this weight is the linear functional that outputs $n_1x_1+\cdots+n_rx_r$ when given an arbitrary $X=(x_1,\ldots, x_r)\in \mathfrak{t}$.
:::

Just as in eigenspace decomposition in linear algebra, the multiplicity of each weight need not be $1$. For example, if we consider the following torus action

$$e^{2\pi i t}\cdot(z_1, z_2)=(e^{4\pi i t}z_1, e^{4\pi i t} z_2)$$

this is because this time $T$ acts on the two-dimensional space $\mathbb{C}^2$ as if it has weight $2$. Collecting components that have the same weight $\lambda$ together in this way and calling this $V_\lambda$, we obtain the *weight space decomposition* $V=\bigoplus V_\lambda$. Writing the discussion so far rigorously as a definition, we have the following.

::: Definition 4
Let a torus $T$ and a complex $T$-module $V$ be given. For an irreducible character $\rchi_\lambda: T \rightarrow S^1$ and the corresponding linear functional $\lambda:\mathfrak{t}\rightarrow\mathbb{R}$, we say that $\lambda$ is a *weight* of $V$ if the following set

$$V_\lambda=\left\{v\in V\mid t\cdot v=\rchi_\lambda(t)v\text{ for all $t\in T$}\right\}$$

is nontrivial. In this case, $V_\lambda$ is called the *weight space* of $\lambda$, and the decomposition

$$V=\bigoplus_\lambda V_\lambda$$

is called the *weight decomposition* of $V$.
:::

## Maximal tori

In this section we show that any element of a compact connected Lie group $G$ is always contained in some maximal torus, and that all maximal tori are conjugate to each other.

Our claim is that for a compact connected Lie group $G$ and its maximal torus $T$, the following map

$$q: G/T\times T\rightarrow G; \qquad (g,t)\mapsto gtg^{-1}$$

is surjective. Then in particular, for any other torus $T'$ and its generator $t'$, we will be able to find $t\in T$ satisfying $gtg^{-1}=t'$, and using the maximality of $T$ and $T'$ respectively, the two claims mentioned above will be proved.

We can not only show that this map is surjective, but also compute its explicit mapping degree. For this purpose, let us define the following.

::: Definition 5
For a compact, connected Lie group $G$, a maximal torus $T$, and the normalizer of $T$

$$N=\{g\in G\mid gTg^{-1}=T\}$$

we define the group $W=N/T$ as the *Weyl group* of $G$.
:::

Then the following holds.

::: Proposition 6
The Weyl group $W=N/T$ is always finite.
:::
::: Proof
By definition, $N$ acts on $T$ via the conjugation action

$$N\rightarrow\Aut(T);\qquad n\mapsto (t\mapsto ntn^{-1})$$

However, $\Aut(T)$ is determined by where the lattice of the torus $T=\mathbb{R}^k/\mathbb{Z}^k$ is sent, and this is embedded in $\GL(k;\mathbb{Z})$ via $\Ad(n)$. That is, this action can be thought of as a continuous map from $N$ to $\GL(k;\mathbb{Z})$. But since $\GL(k;\mathbb{Z})$ is discrete, considering the identity component $N_0$ of $N$, all of $N_0$ must be sent to the identity matrix. That is, $N_0$ acts trivially on $T$.

Now for an arbitrary 1-parameter subgroup $\alpha:\mathbb{R}\rightarrow N_0$, since the elements of $\alpha(\mathbb{R})$ commute with all elements of $T$, the closure of $\alpha(\mathbb{R})T$ is a connected compact abelian subgroup containing $T$, that is, a torus. Therefore, from the maximality of $T$, we know that $\alpha(\mathbb{R})\subseteq T$. But by [\[Manifolds\] §Vector Fields, ⁋Theorem 6](/en/math/manifolds/vector_fields#thm6){: data-lid="ddgfb" }, these cover some open neighborhood of the identity in $N_0$, and therefore generate $N_0$. That is, $N_0=T$.

Therefore $N/T$ is exactly the number of connected components of $N$, and since $N$ is a closed subspace of the compact Lie group $G$, it is likewise compact, so this cannot be infinite.
:::

Now our claim is as follows.

::: Lemma 7
For a compact, connected Lie group $G$, a maximal torus $T$, and a map

$$q:G/T\times T\rightarrow G;\qquad (gT, s)\mapsto gsg^{-1}$$

the mapping degree of $q$ is $\lvert W\rvert$.
:::
::: Proof
To compute the mapping degree, it suffices to choose one regular value, find all of its preimages, and compute the sign of the differential at each preimage.

To this end, first choose from $T$ a generator $t$ and consider its preimage $q^{-1}(t)$. For any $(gT,s)\in G/T\times T$, the condition $q(gT,s)=t$ means that $gsg^{-1}=t$. On the other hand, $g^{-1}tg=s\in T$, and

$$\overline{\langle s\rangle}=g^{-1}\overline{\langle t\rangle}g=g^{-1}Tg$$

but since $s\in T$, we have $g^{-1}Tg\subseteq T$. However, since conjugation is a homeomorphism, $g^{-1}Tg$ is a torus isomorphic to $T$, and from this we know that $g^{-1}Tg=T$ and $g\in N=N_G(T)$. Also, since $s=g^{-1}tg=(gT)^{-1}\cdot t$,

$$q^{-1}(t)=\{(gT, (gT)^{-1}\cdot t)\mid gT\in W\}$$

holds. Here $W$ is the Weyl group defined as $N/T$, and we see that $q^{-1}(t)$ is in one-to-one correspondence with $W$.

Therefore, what remains is to show that all of these have the same sign, so that the mapping degree comes out to be exactly $\lvert W\rvert$. For this, we identify both tangent spaces of $G/T\times T$ and $G$ with $\mathfrak{g}$. Specifically, if we decompose the Lie algebra $\mathfrak{g}$ into the direct sum of $\mathfrak{t}$ and its orthogonal complement $\mathfrak{f}=\mathfrak{t}^\perp$

$$\mathfrak{g}=\mathfrak{t}\oplus\mathfrak{f}$$

then near the origin, the tangent space of $T$ is $\mathfrak{t}$ and the tangent space of $G/T$ is given by $\mathfrak{f}$. Thus the tangent space of $G/T\times T$ is $\mathfrak{t}\oplus\mathfrak{f}\cong\mathfrak{g}$.

On the other hand, for arbitrary $X\in\mathfrak{t}$ and $Y\in\mathfrak{f}$, the differential of $q$ at $(eT,t)$ is computed as follows. For the direction $X$, that is, considering variation in the $T$ direction,

$$\dd{q_{(eT,t)}}(X,0)=\frac{d}{\dd{\epsilon}}\bigg\vert_{\epsilon=0}q(eT, t\exp(\epsilon X))=\frac{d}{\dd{\epsilon}}\bigg\vert_{\epsilon=0}t\exp(\epsilon X)=X$$

holds. Here we used that $T$ is abelian, so $t$ and $\exp(\epsilon X)$ commute. Next, for the direction $Y$, that is, considering variation in the $G/T$ direction,

$$\dd{q_{(eT,t)}}(0,Y)=\frac{d}{\dd{\epsilon}}\bigg\vert_{\epsilon=0}q(\exp(\epsilon Y)T, t)=\frac{d}{\dd{\epsilon}}\bigg\vert_{\epsilon=0}\exp(\epsilon Y)t\exp(-\epsilon Y)$$

holds. Now writing $t=\exp(H)$ ($H\in\mathfrak{t}$),

$$\exp(\epsilon Y)t\exp(-\epsilon Y)=\exp(\epsilon Y)\exp(H)\exp(-\epsilon Y)=\exp(\Ad_{\exp(\epsilon Y)}(H))=\exp(e^{\epsilon\ad_Y}H)$$

holds. Here since $t\in T$, $\Ad_t$ fixes $\mathfrak{t}$ and preserves its orthogonal complement $\mathfrak{f}$, and therefore $\Ad_t^{-1}(Y)-Y\in\mathfrak{f}$. In summary, under an appropriate identification,

$$\dd{q_{(eT,t)}}=\begin{pmatrix} I & 0 \\ 0 & \Ad_t^{-1}\vert_\mathfrak{f}-I \end{pmatrix}$$

holds. Here the first block corresponds to the $\mathfrak{t}$ direction and the second block to the $\mathfrak{f}$ direction.

Now we show that $\Ad_t^{-1}\vert_\mathfrak{f}-I$ is invertible and that the signs match at all preimages. If $(\Ad_t^{-1}-I)Y=0$ for some $Y\in\mathfrak{f}$, then $\Ad_t(Y)=Y$. Then for any integer $m$, we have $\Ad_{t^m}(Y)=Y$, and from the assumption that $t$ is a generator, for all $s\in T$, we have $\Ad_s(Y)=Y$. Now for arbitrary $H\in\mathfrak{t}$,

$$[H,Y]=\frac{d}{\dd{\epsilon}}\bigg\vert_{\epsilon=0}\Ad_{\exp(\epsilon H)}(Y)=0$$

so $Y$ commutes with all elements of $\mathfrak{t}$. But since $\mathfrak{t}$ is a maximal abelian subalgebra, $Y\in\mathfrak{t}$, and therefore $Y\in\mathfrak{f}\cap\mathfrak{t}=\{0\}$. That is, $\Ad_t^{-1}\vert_\mathfrak{f}-I$ is invertible.

Finally, let us verify that at all points of $q^{-1}(t)$, the determinant of $\dd{q}$ has the same sign. Choose arbitrary $w\in W$ and let it be represented by $x\in N$. Then since $q(xT,x^{-1}tx)=t$, we have $(xT, x^{-1}tx)\in q^{-1}(t)$. To compute the differential at this point, since from the definition of $q$

$$q(gT, s)=gsg^{-1}$$

considering left translation by $x$ and conjugation by $x$ yields

$$\dd{q_{(xT, x^{-1}tx)}}=\Ad_x\circ \dd{q_{(eT, t)}}\circ (\text{left translation})$$

holds. In particular, both $\Ad_x\vert_\mathfrak{f}$ and $\Ad_x\vert_\mathfrak{t}$ are linear maps with determinant $1$ (the former because it is an orthogonal map, the latter because $x\in N$ so $\Ad_x$ preserves $\mathfrak{t}$), and therefore the determinant of $\dd{q_{(xT, x^{-1}tx)}}$ equals the determinant of $\dd{q_{(eT,t)}}$.

On the other hand, $\det(\Ad_t^{-1}\vert_\mathfrak{f}-I)$ is also the same for $w\cdot t$. Indeed,

$$\Ad_{wt^{-1}w^{-1}}\vert_\mathfrak{f}-I=\Ad_w\circ(\Ad_t^{-1}\vert_\mathfrak{f}-I)\circ\Ad_w^{-1}$$

so these two operators are similar and thus have the same determinant.

From the above, we have verified that $t$ is a regular value of $q$, the number of elements in $q^{-1}(t)$ is $\lvert W\rvert$, and the determinant of $\dd{q}$ has the same sign at all preimage points. Therefore, with an appropriate choice of orientation, $\deg q=\lvert W\rvert$.
:::

As mentioned above, the core content of this section follows immediately from this lemma.

::: Theorem 8
For a compact connected Lie group $G$, the following hold.

1. Any element of $G$ is contained in some maximal torus.
2. Any two maximal tori of $G$ are always conjugate.
:::

Therefore, for any compact connected Lie group $G$ and maximal torus $T$, we obtain the following decomposition

$$G=\bigcup_{g\in G}gTg^{-1}$$

This is called the *Cartan decomposition*.

## Weyl group parametrization

The Cartan decomposition tells us that each element of $G$ belongs to some maximal torus, but we can describe this decomposition more explicitly. The key is the fact that the map defined in [Lemma 7](#lem7){: data-lid="g8ycq" },

$$q:G/T\times T\rightarrow G;\qquad (gT,t)\mapsto gtg^{-1}$$

becomes a $\lvert W\rvert$-to-1 covering when restricted to the regular elements to be defined in [Definition 12](#def12){: data-lid="b1vee" }. That is, if we denote the set of regular elements of $T$ by $T_{\text{reg}}$ and the union of their conjugates by $G_{\text{reg}}$, then $q:G/T\times T_{\text{reg}}\rightarrow G_{\text{reg}}$ is a $\lvert W\rvert$-to-1 covering. From this, each element of $G_{\text{reg}}$ has $\lvert W\rvert$ preimages, and the relations among them are precisely described by the Weyl group.

Specifically, on $G/T\times T$, define the following $W$-action:

$$w\cdot(gT, t)=(gw^{-1}T, wtw^{-1})$$

Then, since

$$q(w\cdot(gT,t))=q(gw^{-1}T, wtw^{-1})=gw^{-1}(wtw^{-1})wg^{-1}=gtg^{-1}=q(gT,t)$$

$q$ is $W$-invariant, and thus it induces a function from the orbit space $(G/T\times T)/W$ to $G$

$$(G/T\times T)/W\rightarrow G$$

By the same argument as in the proof of [Lemma 7](#lem7){: data-lid="tszxp" }, we see that this function restricted to regular elements, $(G/T\times T_{\text{reg}})/W\rightarrow G_{\text{reg}}$, is a bijection.

Meanwhile, let the space of conjugacy classes of $G$ be $\Conj(G)$. Then each conjugacy class

$$[g]=\{hgh^{-1}\mid h\in G\}$$

is described through $T$ and $W$ as follows.

::: Proposition 9
Two elements of a maximal torus $T$ are conjugate in $G$ if and only if they belong to the same orbit under the Weyl group action.
:::
::: Proof
Suppose that in $T$, two elements $x,y$ are conjugate to each other. That is, for some $g\in G$, we have $gxg^{-1}=y$. Now comparing $T$ and $gTg^{-1}$, these are maximal tori of the centralizer of $y$, $Z_G(y)$. Therefore, $T=h(gTg^{-1})h^{-1}$ holds for some $h\in Z_G(y)$, from which $(hg)x(hg)^{-1}=y$ and $hg\in N_G(T)$. That is, $y=(hgT)\cdot x$, so $x$ and $y$ belong to the same $W$-orbit.

Conversely, if $x,y$ belong to the same $W$-orbit, they are obviously conjugate in $G$.
:::

From this, we know that for each conjugacy class $[g]$, $[g]\cap T$ is exactly one $W$-orbit. Therefore, we obtain the following one-to-one correspondence.

::: Proposition 10
There is a natural one-to-one correspondence between $T/W$ and $\Conj(G)$.
:::

Under this one-to-one correspondence, the conjugation action on $G$ acts trivially on $T/W$. That is, conjugation by each element of $G$ sends every conjugacy class to itself.

## Decomposition of the conjugation action

Now let us examine the situation where $G$ acts on itself by conjugation. For this, for each $h\in G$, define the conjugation map

$$c_{h}:G\rightarrow G;\qquad g\mapsto hgh^{-1}$$

Our goal is to transfer this to $(G/T\times T)/W$ and see concretely how it acts.

First, observe the following. For arbitrary $(gT, t)\in G/T\times T$ and $h\in G$,

$$c_{h}(gtg^{-1})=h(gtg^{-1})h^{-1}=(hg)t(hg)^{-1}=q(hgT, t)$$

holds. That is, via $(G/T\times T)/W\cong G$, when we transfer $c_h$ to $G/T\times T$, since $c_h$ sends $(gT, t)$ to $(hgT, t)$, we can think of $G/T\times T$ as having the following $G$-action defined on it:

$$h\cdot(gT,t)=(hgT,t)$$

Now it is obvious that this action commutes with the $W$-action, and therefore $G$ induces a well-defined action on the quotient $(G/T\times T)/W$ as well. From this observation we obtain the following.

::: Proposition 11
Under the identification $(G/T\times T)/W\cong G$, the conjugation action is expressed as follows.

$$h\cdot[(gT,t)]=[(hgT,t)]$$

That is, it acts by left multiplication on the $G/T$ component and preserves the $T$ component.
:::

On the other hand, by [Proposition 10](#prop10){: data-lid="n1578" }, we know that there is a one-to-one correspondence between $T/W$ and $\Conj(G)$. By definition, $c_h$ does not change the conjugacy class in $G$, and we can check that this is reflected in the proposition above as the absence of change in the $T$ direction. Instead, the conjugation action can be thought of as acting precisely on $G/T$.

Now, to understand the action on $G/T$ by $G$ in more detail, we will rewrite this space using the Weyl group. First, for $N=N(T)$, consider the following projection map

$$\pi: G/T\rightarrow G/N;\qquad gT\mapsto gN$$

Then for each coset $gN\in G/N$, its fiber is

$$\pi^{-1}(gN)=\{hT\mid h\in gN\}=\{gxT\mid x\in N\}$$

and since $g$ is fixed, this fiber is essentially $\{xT\mid x\in N\}$, that is, the same as $N/T$. Furthermore, topologically we can verify that $\pi$ is exactly a $\lvert W\rvert$-fold covering map. ([\[Algebraic Topology\] §Covering Spaces, ⁋Definition 3](/en/math/algebraic_topology/covering_spaces#def3){: data-lid="0nuau" }) More precisely, this is a principal $W$-bundle with each fiber being $W$. 

## Example: $\SU(2)$

Let us verify the discussion so far in the compact connected Lie group

$$\SU(2)=\{A\in\GL(2;\mathbb{C})\mid A^\dagger A=I,\det A=1\}=\left\{\begin{pmatrix}\alpha&-\overline{\beta}\\\beta&\overline{\alpha}\end{pmatrix} : \alpha,\beta\in \mathbb{C},\lvert\alpha\rvert^2+\lvert\beta\rvert^2=1\right\}$$

First, we need to find a maximal torus of $\SU(2)$. Our claim is that the set

$$T=\left\{\begin{pmatrix}e^{i\theta}&0\\0&e^{-i\theta}\end{pmatrix}\middle\vert \theta\in\mathbb{R}/2\pi\mathbb{Z}\right\}$$

is a (particular) maximal torus of $\SU(2)$. That $T$ is a $1$-dimensional torus is obvious, so it suffices to show maximality. For this, suppose an abelian subgroup containing $T$ in $\SU(2)$, $A$, is given. Then any element

$$\begin{pmatrix}a&b\\c&d\end{pmatrix}\in A$$

must commute with all elements of $T$, and in particular must commute with 

$$\begin{pmatrix}i&0\\0&-i\end{pmatrix}$$

and computing this,

$$\begin{pmatrix}a&b\\c&d\end{pmatrix}\begin{pmatrix}i&0\\0&-i\end{pmatrix}=\begin{pmatrix}ai&-bi\\ci&-di\end{pmatrix},\qquad \begin{pmatrix}i&0\\0&-i\end{pmatrix}\begin{pmatrix}a&b\\c&d\end{pmatrix}=\begin{pmatrix}ai&bi\\-ci&-di\end{pmatrix}$$

so from this we know that $b=c=0$. From this we know that $A\subseteq T$. 

Now to compute the Weyl group, let us show that the normalizer of $T$, $N=N_{\SU(2)}(T)$, is given by the formula

$$N=T\cup \begin{pmatrix}0&1\\-1&0\end{pmatrix}T$$

First, for an arbitrary $g\in \SU(2)$, if we write

$$g=\begin{pmatrix}a&b\\c&d\end{pmatrix}$$

then

$$g \begin{pmatrix}e^{i\theta}&0\\0&e^{-i\theta}\end{pmatrix}g^{-1} = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} e^{i\theta} & 0 \\ 0 & e^{-i\theta} \end{pmatrix} \begin{pmatrix} \overline{a} & \overline{c} \\ \overline{b} & \overline{d} \end{pmatrix} = \begin{pmatrix} \lvert a\rvert^2 e^{i\theta} + \lvert b\rvert^2 e^{-i\theta} & a\overline{c}e^{i\theta} + b\overline{d}e^{-i\theta} \\ c\overline{a}e^{i\theta} + d\overline{b}e^{-i\theta} & \lvert c\rvert^2 e^{i\theta} + \lvert d\rvert^2 e^{-i\theta} \end{pmatrix}$$

so for this to belong to $T$, for all $\theta$ we must have

$$a\overline{c}e^{i\theta}+b\overline{d}e^{-i\theta}=0$$

which implies that $a\overline{c}=0$ and $b\overline{d}=0$. If $a\neq 0$, then since $\overline{c}=0$ we must have $c=0$, and from $ad-bc=1$ we get $d=\overline{a}$, and thus from $b\overline{d}=0$ we must have $b=0$. That is, in this case $g\in T$. If $a=0$, then since $\lvert a\rvert^2+\lvert b\rvert^2=1$ we have $\lvert b\rvert=1$, and from $ad-bc=1$ we must have $c=-\overline{b}$, and similarly we know that $d=0$. From this, $g$ must be of the form

$$\begin{pmatrix}0&e^{i\alpha}\\ -e^{-i\alpha}&0\end{pmatrix}$$

so from this we can verify that $N$ is given by the above formula. Furthermore, the nontrivial element of the Weyl group $W\cong\mathbb{Z}_2$ corresponds to $\begin{pmatrix}0&1\\-1&0\end{pmatrix}$, and the action of this element on $T$ is

$$\begin{pmatrix}0&1\\-1&0\end{pmatrix}\begin{pmatrix}e^{i\theta}&0\\0&e^{-i\theta}\end{pmatrix}\begin{pmatrix}0&-1\\1&0\end{pmatrix}=\begin{pmatrix}e^{-i\theta}&0\\0&e^{i\theta}\end{pmatrix}$$

so on the torus $S^1$, this corresponds to the reflection $\theta\mapsto -\theta$.

Now considering the standard representation of $\SU(2)$ on $\mathbb{C}^2$, we have $\Aut(\mathbb{C}^2)=\GL(2;\mathbb{C})$, and thus the representation $\rho:\SU(2)\rightarrow \GL(2;\mathbb{C})$ is the inclusion. The same holds for its restriction to the torus $T$, and from this we know that the weights of $T$ are $1, -1$, respectively, the corresponding weight spaces are $\mathbb{C}e_1$, $\mathbb{C}e_2$, and the weight decomposition is $\mathbb{C}e_1\oplus \mathbb{C}e_2$. On this, we can verify that the Weyl group acts by interchanging the weights.

## Weyl chamber

Finally, we examine a definition that gives a taste of the motivation for root systems, which we will cover in the next post. In [Lemma 7](#lem7){: data-lid="6nmdd" }, at a generator of $T$, $t$, we computed the preimage under $q$ and checked that there are $\lvert W\rvert$ of them. Now that we know that $T$ is acted upon by $W$, we can write this condition as follows.

::: Definition 12
For a maximal torus $T$, an element $t$ is called *regular* if $wtw^{-1}=t$ is satisfied by $w\in W$ only for $w=e$. Conversely, if $wtw^{-1}=t$ holds for some $w\neq e$, then $t$ is called *singular*.
:::

That is, a regular element is an element whose stabilizer under the Weyl group action is trivial, and a singular element is an element with a nontrivial stabilizer. In general, to compute the mapping degree of $q$, one must compute the value at a regular value of $q$, and considering the orbit-stabilizer theorem, we know that for the preimage to have $\lvert W\rvert$ images in this way, the stabilizer must necessarily be trivial. From this, it is natural to call such an element a regular element.

::: Example 13
In the case of $\SU(2)$, $T=\{\text{diag}(e^{i\theta}, e^{-i\theta})\}$ and $W=\mathbb{Z}_2$ acts by $\theta\mapsto -\theta$. Therefore:

- **Regular:** Elements with $\theta \neq 0, \pi$. These are not fixed points of the reflection.
- **Singular:** $\theta=0$ (identity) and $\theta=\pi$ ($\text{diag}(-1,-1)$). These are fixed by the reflection.

On the torus $T\cong S^1$, the singular elements are exactly two points, and the regular elements are their complement.
:::

In general, the following holds.

::: Proposition 14
For a compact connected Lie group $G$ and a maximal torus $T$:

1. The regular elements form a dense open subset of $T$.
2. In $T$, the singular elements form a closed subset of codimension $\geq 1$.
3. The set of singular elements is a union of finitely many subgroups.
:::
::: Proof
(1) and (2): For each $w\in W$, $w\neq e$, the fixed point set $\{t\in T\mid wtw^{-1}=t\}$ is a proper closed subgroup of $T$. The set of singular elements is a finite union of these, so it is closed, and its complement (the regular elements) is dense open.

(3): For each $w\neq e$, the fixed point set is a closed subgroup of $T$, and since $W$ is finite, it is a union of finitely many subgroups.
:::

The set formed by singular elements in $T$ divides the torus into several pieces. For example, in the case of $\SU(2)$, the two singular elements divide $S^1$ into two semicircles. The Weyl group action interchanges these two semicircles and defines a free action on the regular elements.

From this perspective, the quotient of the regular elements of $T$, $T_{\text{reg}}/W$, is a connected space, and this can be connected to the concept of a *Weyl chamber*. In the case of $\SU(2)$, $T_{\text{reg}}/W \cong (0,\pi)$ is a one-dimensional interval, and this corresponds precisely to a one-dimensional Weyl chamber.

In more general Lie groups, the singular elements divide the torus into several chambers, and each chamber serves as a fundamental domain for the Weyl group action. This forms the geometric foundation for the root systems and Weyl chambers to be covered in the next post.

---

**References**

**[Bro]** Armand Borel, *Linear Algebraic Groups*, Graduate texts in mathematics, Springer, 1991.  
**[BtD]** Theodor Bröcker, Tammo tom Dieck, *Representations of Compact Lie Groups*, Graduate texts in mathematics, Springer, 1985.
