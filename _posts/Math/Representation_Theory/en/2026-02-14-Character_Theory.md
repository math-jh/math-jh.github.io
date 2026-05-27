---
title: "Characters"
excerpt: "Definition of character functions and orthogonality relations"

categories: [Math / Representation Theory]
permalink: /en/math/representation_theory/character_theory
header:
    overlay_image: /assets/images/Math/Representation_Theory/Character_Theory.png
    overlay_filter: 0.5
sidebar: 
    nav: "representation_theory-en"

date: 2026-02-14
last_modified_at: 2026-02-14
weight: 2
translated_at: 2026-05-28T11:36:15+00:00
translation_source: kimi-cli
---
In this post we define character functions and examine their properties. They will be of great help in our goal of classifying representations.

## Characters of Group Representations

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> For a representation $$\rho:G\rightarrow\Aut(V)$$ of $$G$$, the corresponding *character* $$\rchi_\rho:G\rightarrow\mathbb{C}$$ is defined by

$$\rchi_\rho(g)=\tr(\rho(g))$$

.

</div>

In other words, this function takes each $$g\in G$$ and returns the trace of the linear map $$\rho(g):V\rightarrow V$$ it defines. As we shall see, this function plays a major role in describing representations of $$G$$. For instance, we can immediately see that this function encodes the dimension of $$V$$.

$$\rchi_\rho(e)=\tr(\rho(e))=\tr(\id_V)=\dim V.$$

Similarly, when two linear maps

$$L_V:V\rightarrow V,\qquad L_W:W\rightarrow W$$

are given, we know how their direct sum $$L_V\oplus L_W: V\oplus W\rightarrow V\oplus W$$, their tensor product $$L_V\otimes L_W: V\otimes W \rightarrow V\otimes W$$, and so on are defined, and we also know what their traces are (for instance, by computing with matrices). From this we obtain the following proposition.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> For representations $$V, W$$, the following hold.

1. $$\rchi_{V\oplus W}=\rchi_V\oplus \rchi_W$$
2. $$\rchi_{V\otimes W}=\rchi_V\rchi_W$$
3. $$\rchi_{V^\ast}=\overline{\rchi}_V$$

</div>

In particular, by the first formula, since any representation admits an irreducible decomposition

$$V\cong V_1^{\oplus a_1}\oplus\cdots\oplus V_r^{\oplus a_r}$$

we know that the character of any representation can be expressed as

$$\rchi_V=a_1\rchi_{V_1}+\cdots+a_r\rchi_{V_r}$$

.

On the other hand, by definition,

$$\rchi_\rho(hgh^{-1})=\tr(\rho(h)\rho(g)\rho(h)^{-1})=\tr(\rho(g))=\rchi_\rho(g)$$

holds, so ([\[Linear Algebra\] §Characteristic Polynomial, ⁋Theorem 5](/en/math/linear_algebra/characteristic_polynomial#cor5)), we see that $$\rchi_\rho$$ is constant on the *conjugacy classes* of $$G$$. Such functions also have a name.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> A function $$\rchi:G\rightarrow\mathbb{C}$$ is called a *class function* if $$\rchi(hgh^{-1})=f(g)$$ holds for all $$g,h\in G$$. We denote the collection of all class functions defined on $$G$$ by $$\mathbb{C}_\class(G)$$.

</div>

By definition, class functions are determined by their values on each conjugacy class, and thus, as a vector space, $$\mathbb{C}_\class(G)$$ has dimension equal to the number of conjugacy classes of $$G$$. Meanwhile, the idea we considered important in the previous post was that given a value, we could average it over all of $$G$$ to obtain a $$G$$-invariant value. Using this, we can give the following definition on $$\mathbb{C}_\class(G)$$.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> For any class functions $$\rchi_1,\rchi_2: G\rightarrow \mathbb{C}$$, we define

$$\langle \rchi_1,\rchi_2\rangle=\frac{1}{\lvert G\rvert}\sum_{g\in G} \rchi_1(g)\overline{\rchi_2(g)}$$

.

</div>

This is merely the standard Hermitian product on the target space $$\mathbb{C}$$ transferred to $$\mathbb{C}_\class(G)$$. On the other hand, for the character $$\rchi_\rho$$ of any representation $$\rho$$, for any $$g\in G$$,

$$\rchi_\rho(g^{-1})=\tr(\rho(g^{-1}))=\tr(\rho(g)^{-1})=\tr(\rho(g)^\dagger)=\overline{\tr(\rho(g))}=\overline{\rchi_\rho(g)}$$

holds, so for two characters $$\rchi_1,\rchi_2$$ we know that the following formula

$$\langle \rchi_1,\rchi_2\rangle=\frac{1}{\lvert G\rvert}\sum_{g\in G}\rchi_1(g)\overline{\rchi_2(g)}=\frac{1}{\lvert G\rvert}\sum_{g\in G}\rchi_1(g^{-1})\overline{\rchi_2(g^{-1})}=\frac{1}{\lvert G\rvert}\sum_{g\in G}\overline{\rchi_1(g)}\rchi_2(g)=\langle \rchi_2,\rchi_1\rangle$$

holds. That is, when restricted to characters, this inner product takes real values.

## Orthogonality of Characters

As we saw in the previous post, for any representation $$U$$, the fixed-point subspace

$$U^G=\{u\in U\mid g\cdot u=u\text{ for all $g\in G$}\}$$

exists, and in this case

$$p:U\rightarrow U^G;\qquad u\mapsto \frac{1}{\lvert G\rvert}\sum_{g\in G}g\cdot u$$

defines a $$G$$-invariant projection from $$U$$ to $$U$$, and its image is $$U^G$$. By its definition, the subrepresentation defined on $$U^G$$ is precisely the trivial representation

$$G\rightarrow \Aut(U^G);\quad g\mapsto \id_{U_G}$$

so from this we can decompose the representation $$U$$ into the trivial representation $$U^G$$ and the remaining part $$W$$, obtaining

$$U=U^G\oplus W$$

.

Moreover, we can also compute the dimension of $$U^G$$. Using suitable bases of $$U^G$$ and $$W$$ in the above decomposition, we can represent this in the block matrix form

$$\begin{pmatrix}\id_{U^G}&0\\0&0\end{pmatrix}$$

so the trace of $$\varphi: U\rightarrow U$$ equals $$\dim U^G$$. Now by definition,

$$\dim U^G=\tr(\varphi)=\tr\left(\frac{1}{\lvert G\rvert}\sum_{g\in G}\rho(g)\right)=\frac{1}{\lvert G\rvert}\sum_{g\in G}\tr(\rho(g))=\frac{1}{\lvert G\rvert}\sum_{g\in G}\rchi(g)\tag{1}$$

.

More generally, in [§Representations of Finite Groups, ⁋Definition 3](/en/math/representation_theory/representations_of_finite_groups#def3) we defined, for any $$G$$-representations $$V,W$$, a $$G$$-action on their $$\Hom$$-set $$\Hom_\mathbb{C}(V,W)$$ (as underlying $$\mathbb{C}$$-vector spaces) by

$$(g\cdot f)(v)=g\cdot f(g^{-1}\cdot v)\qquad\text{for all $v\in V$}$$

.

Then the formula

$$\Hom_\mathbb{C}(V,W)^G=\Hom_G(V,W)$$

holds, and thus applying (1) to $$U=\Hom(V,W)$$ and the corresponding trace map $$\varphi$$, we know that

$$\dim \Hom_G(V,W)=\tr(\varphi)=\frac{1}{\lvert G\rvert}\sum_{g\in G}\rchi_{\Hom(V,W)}(g)$$

.

On the other hand, using $$\Hom_G(V,W)=V^\ast\otimes W$$, the character on the right-hand side is obtained by the formula

$$\rchi_{\Hom_G(V,W)}(g)=\overline{\rchi_V(g)}\rchi_W(g)$$

so the above equation can be rewritten as

$$\dim\Hom_G(V,W)=\frac{1}{\lvert G\rvert}\sum_{g\in G}\overline{\rchi_V(g)}\rchi_W(g)=\langle \rchi_W, \rchi_V\rangle$$

.

Finally, assuming $$V,W$$ are irreducible representations, by [§Representations of Finite Groups, ⁋Lemma 8](/en/math/representation_theory/representations_of_finite_groups#lem8), $$\Hom_G(V,W)$$ is $$1$$-dimensional if $$V\cong W$$ and $$0$$-dimensional otherwise, so

$$\dim \Hom_\mathbb{C}(V,W)^G=\dim \Hom_G(V,W)=\begin{cases}1&\text{if $V\cong W$,}\\0&\text{otherwise}\end{cases}$$

and from this we obtain the formula

$$\langle \rchi_W,\rchi_V\rangle=\delta_{VW}$$

.

That is, with respect to the inner product of [Definition 4](#def4), the irreducible characters form an orthonormal set. Since we know that $$\mathbb{C}_\class(G)$$ has dimension equal to the number of conjugacy classes of $$G$$, it follows that there cannot be more irreducible representations than the number of conjugacy classes of $$G$$. Moreover, using this inner product we can compute the multiplicity of $$V_i$$ inside $$V$$ by taking the inner product of the character $$\rchi_V$$ of any representation $$V$$ with the character $$\rchi_{V_i}$$ of a fixed irreducible representation $$V_i$$.

## Regular Representation

In this section we obtain the Artin–Wedderburn decomposition considered in the previous post ([§Representations of Finite Groups, Equation (1)](/en/math/representation_theory/representations_of_finite_groups#cor7)) using characters. To this end, first observe that $$\mathbb{C}[G]$$ is a left $$\mathbb{C}[G]$$-module over itself, and hence by the categorical equivalence

$$\Rep_\mathbb{C}(G)\cong \lMod{\mathbb{C}[G]}$$

it is also a representation of $$G$$. This is obtained simply by restricting the module structure on $$\mathbb{C}[G]$$, that is, its multiplication structure as a ring, to $$G$$. Explicitly, using the image $$\delta_g=\sum_{x\in X}\delta_g(x)x$$ of any $$g\in G$$ in $$\mathbb{C}[G]$$, we can write

$$g\cdot \left(\sum_{y\in G} \phi(y)y\right)=\left(\sum_{x\in X}\delta_g(x)x\right)\left(\sum_{y\in G}\phi(y)y\right)=\sum_{z\in G}\left(\sum_{x\in G}\delta_g(x)\phi(x^{-1}z)\right)z=\sum_{z\in G}\phi(g^{-1}z)z=\sum_{z\in G}\phi(z)(gz)$$

and we call such a representation the *regular representation*.

Now, to decompose $$\mathbb{C}[G]$$, we consider the character theory of the regular representation. Regarding $$\mathbb{C}[G]$$ as the vector space having the elements $$g\in G$$ (more precisely, the $$\delta_g$$) as a basis, and representing each linear operator $$\rho_\reg(g)$$ given by the regular representation as a matrix via this basis, we find that its trace is

$$\rchi_{\mathbb{C}[G]}(g)=\begin{cases}\lvert G\rvert&\text{if $g=e$}\\0&\text{otherwise}\end{cases}\tag{2}$$

.

Now if $$V_i$$ is an irreducible subrepresentation of $$\mathbb{C}[G]$$, then

$$\langle\rchi_{\mathbb{C}[G]}, \rchi_{V_i}\rangle=\frac{1}{\lvert G\rvert}\sum_{g\in G}\rchi_{\mathbb{C}[G]}(g)\rchi_{V_i}(g)=\frac{1}{\lvert G\rvert} \rchi_{\mathbb{C}[G]}(e)\rchi_{V_i}(e)=\dim V_i$$

holds. Thus we obtain the decomposition

$$\mathbb{C}[G]\cong \bigoplus_{i=1}^r V_i^{\dim V_i}$$

.

Moreover, $$\mathbb{C}[G]$$ acts on itself by multiplication, and under this action, thinking that by [§Representations of Finite Groups, ⁋Lemma 8](/en/math/representation_theory/representations_of_finite_groups#lem8) each $$V_i$$ maps only into $$V_i$$, we know that each $$V_i^{\dim V_i}$$ is exactly the matrix algebra $$\Mat_{d_i}(\mathbb{C})$$, and by the uniqueness of the Artin–Wedderburn theorem we can verify that this is precisely

$$\mathbb{C}[G]\cong \bigoplus_{i=1}^r\Mat_{d_i}(\mathbb{C})$$

.

## Projection Formula

Earlier we showed that the characters of irreducible representations form an orthonormal set inside $$\mathbb{C}_\class(G)$$. Now we show that they form an orthonormal basis of $$\mathbb{C}_\class(G)$$.

<div class="proposition" markdown="1">

<ins id="lem5">**Lemma 5**</ins> Let any function $$\phi:G\rightarrow \mathbb{C}$$ and any representation $$\rho:G\rightarrow\Aut(V)$$ be given. If we define

$$\rho_\phi=\sum_{g\in G} \phi(g)\rho(g): V\rightarrow V$$

then $$\rho_\phi$$ is a $$G$$-map if and only if $$\phi$$ is a class function.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

For $$\rho_\phi$$ to be a $$G$$-map, the formula

$$\rho_\phi(h\cdot v)=h\cdot\rho_\phi(v)$$

must hold for any $$h\in G$$ and any $$v\in V$$. Computing the left-hand side directly,

$$\rho_\phi(h\cdot v)=\sum_{g\in G}\phi(g)\rho(g)(h\cdot v)$$

and since taking this sum over $$hgh^{-1}$$ yields the same sum,

$$\rho_\phi(hv)=\sum_{g\in G}\phi(hgh^{-1})\rho(hgh^{-1})(h\cdot v)=\sum_{g\in G}\phi(hgh^{-1})\rho(h)\rho(g)(v)=\rho(h)\left(\sum_{g\in G}\phi(hgh^{-1})\rho(g)v\right)$$

we can write this. Now for this to equal

$$h\cdot\rho_\phi(v)=\rho(h)\rho_\phi(v)=\rho(h)\left(\sum_{g\in G}\phi(g)\rho(g)(v))$$

we must have exactly $$\phi(g)=\phi(hgh^{-1})$$, that is, $$\phi$$ must be a class function.

</details>

Now we use this to show that every class function can be expressed as a linear combination of irreducible characters. That is, we must show that if for a class function $$\phi$$, $$\langle \rchi_V,\phi\rangle=0$$ holds for all irreducible characters $$\rchi_V$$, then $$\phi=0$$.

To this end, apply the above lemma to a class function $$\phi$$ and an irreducible representation $$\rho:G\rightarrow\Aut(V)$$. Since $$\phi$$ is a class function, so is $$\overline{\phi}$$, and thus $$\rho_{\overline{\phi}}$$ is a $$G$$-map; by [§Representations of Finite Groups, ⁋Lemma 8](/en/math/representation_theory/representations_of_finite_groups#lem8), $$\rho_{\overline{\phi}}$$ is of the form $$\lambda\id_V$$. Now taking the trace here, we know that

$$(\dim V)\lambda=\tr(\rho_{\overline{\phi}})=\tr\left(\sum_{g\in G}\overline{\phi(g)}\rho(g)\right)=\sum_{g\in G}\overline{\phi(g)}\rchi_V(g)=\lvert G\rvert\langle \rchi_V,\phi\rangle=0$$

.

Now since any representation has an irreducible decomposition, we know that $$\sum \overline{\phi(g)}g$$ must act as $$0$$ on any representation, and in particular also on the regular representation $$\mathbb{C}[G]$$. However, letting this element act on $$\delta_e$$ in the regular representation gives

$$\left(\sum\overline{\phi(g)}g\right)\cdot \delta_e=\sum_{g\in G}\overline{\phi(g)}g$$

and therefore $$\overline{\phi(g)}=0$$ must hold for all $$g$$.

## Example: $$S_3$$

We close this post with an example illustrating the theory we have built since the previous posts. First, for any *abelian* group $$G$$ it is obvious that irreducible representations are only $$1$$-dimensional representations, so to test our theory we need a non-abelian group. For convenience of computation, let us consider $$S_3$$, the smallest non-abelian group. Explicitly,

$$S_3=\{(\;),\,(1\;2),\,(1\;3),\,(2\;3),\,(1\;2\;3),\,(1\;3\;2)\}$$

.

First, it is obvious that the following two representations

$$\rho_0: S_3 \rightarrow \Aut(\mathbb{C})\qquad \sigma\mapsto \id_\mathbb{C}$$

and

$$\rho_\sgn: S_3 \rightarrow \Aut(\mathbb{C})\qquad \sigma\mapsto \sgn(\sigma)\id_\mathbb{C}$$

are two irreducible representations of $$S_3$$. Meanwhile, $$S_3$$ acts on $$\mathbb{C}^3$$ by permutation via

$$\sigma\cdot(x_1,x_2,x_3)=(x_{\sigma(1)},x_{\sigma(2)},x_{\sigma(3)})$$

.

However, this action is trivial along the line spanned by $$(1,1,1)$$, and we can view all the action as taking place on the subspace orthogonal to this line,

$$V_\std=\{(x_1,x_2,x_3)\mid x_1+x_2+x_3=0\}$$

and we can verify that this subrepresentation is irreducible. We call this the *standard representation* of $$S_3$$.

These three representations have dimensions $$1,1,2$$ respectively, and since

$$\lvert S_3\rvert=6=1^2+1^2+2^2$$

we can verify that the dimensions in the irreducible decomposition match. To proceed further, let us compute the characters of these three irreducible representations. For this, consider the conjugacy classes of $$S_3$$:

$$A_1=\{(\;)\},\qquad A_2=\{(1\;2),\,(1\;3),\,(2\;3)\},\qquad A_3=\{(1\;2\;3),\,(1\;3\;2)\}$$

.

For notational convenience, if a character $$\rchi$$ takes values $$a_1,a_2,a_3$$ on $$A_1,A_2,A_3$$, we shall write it in the vector form $$(a_1,a_2,a_3)$$.

- $$\rho_0$$ sends every element of $$S_3$$ to $$\id_\mathbb{C}\in \Aut(\mathbb{C})$$, and the trace of this $$1\times 1$$ matrix is $$1$$, so $$\rchi_0$$ is $$(1,1,1)$$.
- $$\rho_\sgn$$ sends only the odd permutations of $$S_3$$ (that is, the elements of $$A_2$$) to $$-\id_\mathbb{C}\in\Aut(\mathbb{C})$$, and the remaining elements to $$\id_\mathbb{C}\in \Aut(\mathbb{C})$$, so $$\rchi_\sgn$$ is $$(1,-1,1)$$.

There are two methods for computing the character $$\rchi_\std$$ of the standard representation $$\rho_\std$$, and we shall introduce both.

First, to compute it directly, choose the basis of $$V_\std$$

$$\{e_1=(1,0,-1), e_2=(0,1,-1)\}$$

.

Then $$(\;)$$ does not touch this basis, so of course $$\rchi_\std$$ takes the value $$2$$ on $$A_1$$. On $$A_2$$, for instance, acting by $$(1\;2)$$ swaps the basis elements, so it corresponds to the matrix

$$\rho_\std((1\;2))\begin{pmatrix}0&1\\1&0\end{pmatrix}$$

and its trace is $$0$$. For reference, if $$(1\;3)$$ acts on this basis, $$e_1$$ is sent to $$-e_1$$ and $$e_2$$ to $$(-1,1,0)=-e_1+e_2$$, so it corresponds to the matrix

$$\rho_\std((1\;3))=\begin{pmatrix}-1&-1\\0&1\end{pmatrix}$$

and since the trace of this matrix is also $$0$$, we can verify by computation that a character function is a class function. In the case of $$A_3$$, since it sends $$e_1$$ to $$(-1,1,0)=-e_1+e_2$$ and $$e_2$$ to $$(-1,0,1)=-e_1$$,

$$\rho_\std((1\;2\;3))=\begin{pmatrix}-1&-1\\1&0\end{pmatrix}$$

so we know that $$\rchi_\std$$ is $$(2,0,-1)$$.

A more convenient computational method uses the decomposition

$$V_\perm=V_0\oplus V_\std$$

.

We already know that the character of $$V_0$$ is $$(1,1,1)$$. Now considering the action of $$V_\perm$$,

$$\rho_\perm((\;))=\begin{pmatrix}1&0&0\\0&1&0\\0&0&1\end{pmatrix},\quad \rho_\perm((1\;2))=\begin{pmatrix}0&1&0\\1&0&0\\0&0&1\end{pmatrix},\quad \rho_\perm((1\;2\;3))=\begin{pmatrix}0&1&0\\0&0&1\\1&0&0\end{pmatrix}$$

we know that $$\rchi_\perm$$ is $$(3,1,0)$$, and now by [Proposition 2](#prop2) we have $$\rchi_\perm=\rchi_0+\rchi_\std$$, so we can see that $$\rchi_\std$$ is $$(2,0,-1)$$. These three characters obtained in this way,

$$\rchi_0=(1,1,1),\qquad \rchi_\sgn=(1,-1,1),\qquad \rchi_\std=(2,0,-1)$$

are (as expected) orthonormal.

From the computation of the character of the regular representation we know that

$$\rho_{\mathbb{C}[S_3]}(g)=\begin{cases}6&\text{if $g=e$}\\0&\text{otherwise}\end{cases}$$

(Equation (2)). This must be a $$\mathbb{Z}^{\geq 0}$$-linear combination of the above three characters, and indeed we can verify that

$$\rchi_{\mathbb{C}[S_3]}=\rchi_0+\rchi_\sgn+2\rchi_\std$$

.

Furthermore, this is a result consistent with the above discussion that in the regular representation, the multiplicity of each irreducible factor must equal its own dimension.
