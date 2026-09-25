---
title: "Characters of Representations"
description: "We define characters of group representations and examine their additive and multiplicative properties. Introducing class functions and inner products shows that characters are constant on conjugacy classes and distinguish irreducible representations."
excerpt: "Definitions and orthogonality relations of character functions"

categories: [Math / Representation Theory]
permalink: /en/math/representation_theory/character_theory
sidebar: 
    nav: "representation_theory-en"

date: 2026-02-14
weight: 2
translated_at: 2026-09-25T19:15:05+00:00
translation_source: antigravity-gemini-3.8-flash-high
---
In this post, we define character functions and examine their properties. These will be of great help in our goal of classifying representations. 

## Characters of Group Representations

::: Definition 1
Given a representation of $G$, $\rho:G\rightarrow\Aut(V)$, we define the corresponding *character* $\rchi_\rho:G\rightarrow\mathbb{C}$ by

$$\rchi_\rho(g)=\tr(\rho(g))$$
:::

That is, what this function does is take each $g\in G$ and return the trace of the linear map $\rho(g):V\rightarrow V$ defined by it. As we will see later, this function plays an important role in describing representations of $G$. For example, something we can see immediately is that this function encodes the dimension of $V$:

$$\rchi_\rho(e)=\tr(\rho(e))=\tr(\id_V)=\dim V.$$

Similarly, given two linear maps 

$$L_V:V\rightarrow V,\qquad L_W:W\rightarrow W$$

we know how their direct sum $L_V\oplus L_W: V\oplus W\rightarrow V\oplus W$, their tensor product $L_V\otimes L_W: V\otimes W \rightarrow V\otimes W$, and so on are defined, and we also know what their traces are (for instance, by calculating in terms of matrices). From this, we obtain the following proposition. 

::: Proposition 2
For representations $V, W$, the following hold: 

1. $\rchi_{V\oplus W}=\rchi_V+\rchi_W$
2. $\rchi_{V\otimes W}=\rchi_V\rchi_W$
3. $\rchi_{V^\ast}=\overline{\rchi_V}$
:::

In particular, by the first identity, since any representation has an irreducible decomposition

$$V\cong V_1^{\oplus a_1}\oplus\cdots\oplus V_r^{\oplus a_r}$$

we know that the character of any representation can be expressed as

$$\rchi_V=a_1\rchi_{V_1}+\cdots+a_r\rchi_{V_r}$$

On the other hand, since by definition

$$\rchi_\rho(hgh^{-1})=\tr(\rho(h)\rho(g)\rho(h)^{-1})=\tr(\rho(g))=\rchi_\rho(g)$$

holds ([\[Linear Algebra\] §Characteristic Polynomial, ⁋Corollary 5](/en/math/linear_algebra/characteristic_polynomial#cor5){: data-lid="yowsd" }), we see from this that $\rchi_\rho$ is constant on the *conjugacy classes* of $G$. There is also a name for such functions. 

::: Definition 3
A function $\rchi:G\rightarrow\mathbb{C}$ is a *class function* if $\rchi(hgh^{-1})=\rchi(g)$ holds for all $g,h\in G$. We denote the collection of all class functions defined on $G$ by $\mathbb{C}_\class(G)$. 
:::

By definition, class functions are determined by their values on each conjugacy class, and therefore as a vector space, $\mathbb{C}_\class(G)$ has dimension equal to the number of conjugacy classes of $G$. Meanwhile, the important idea we considered in the previous post was that given any value, averaging it over all of $G$ yields a $G$-invariant value; using this, we can make the following definition on $\mathbb{C}_\class(G)$.

::: Definition 4
For any class functions $\rchi_1,\rchi_2: G\rightarrow \mathbb{C}$, we define

$$\langle \rchi_1,\rchi_2\rangle=\frac{1}{\lvert G\rvert}\sum_{g\in G} \rchi_1(g)\overline{\rchi_2(g)}$$
:::

This is simply transferring the standard Hermitian product defined on the target space $\mathbb{C}$ onto $\mathbb{C}_\class(G)$. On the other hand, for any representation $\rho$ with character $\rchi_\rho$, we can choose $\rho$ to be unitary by [§Representation Theory of Finite Groups, ⁋Proposition 6](/en/math/representation_theory/representations_of_finite_groups#prop6){: data-lid="qd9uh" }, so for any $g\in G$,

$$\rchi_\rho(g^{-1})=\tr(\rho(g^{-1}))=\tr(\rho(g)^{-1})=\tr(\rho(g)^\dagger)=\overline{\tr(\rho(g))}=\overline{\rchi_\rho(g)}$$

holds; therefore, for two characters $\rchi_1,\rchi_2$, we see that the following equation

$$\langle \rchi_1,\rchi_2\rangle=\frac{1}{\lvert G\rvert}\sum_{g\in G}\rchi_1(g)\overline{\rchi_2(g)}=\frac{1}{\lvert G\rvert}\sum_{g\in G}\rchi_1(g^{-1})\overline{\rchi_2(g^{-1})}=\frac{1}{\lvert G\rvert}\sum_{g\in G}\overline{\rchi_1(g)}\rchi_2(g)=\langle \rchi_2,\rchi_1\rangle$$

holds. That is, when restricted to characters, this inner product takes real values.

## Orthogonality of Characters

As seen in the previous post, for any representation $U$, there exists the following subspace of fixed points

$$U^G=\{u\in U\mid g\cdot u=u\text{ for all $g\in G$}\}$$

, where

$$p:U\rightarrow U^G;\qquad u\mapsto \frac{1}{\lvert G\rvert}\sum_{g\in G}g\cdot u$$

defines a projection from $U$ to $U$ that is $G$-invariant, and its image is $U^G$. By definition, the subrepresentation defined on $U^G$ is precisely the trivial representation

$$G\rightarrow \Aut(U^G);\quad g\mapsto \id_{U^G}$$

, so from this we can decompose the representation $U$ into the trivial representation $U^G$ and the remaining part $W$ to obtain

$$U=U^G\oplus W$$

.

Moreover, we can also compute the dimension of $U^G$. In the decomposition above, by choosing suitable bases for $U^G$ and $W$, we can represent this in the form of a block matrix

$$\begin{pmatrix}\id_{U^G}&0\\0&0\end{pmatrix}$$

, so the trace of $p: U\rightarrow U$ is equal to $\dim U^G$. Now by definition,

$$\dim U^G=\tr(p)=\tr\left(\frac{1}{\lvert G\rvert}\sum_{g\in G}\rho(g)\right)=\frac{1}{\lvert G\rvert}\sum_{g\in G}\tr(\rho(g))=\frac{1}{\lvert G\rvert}\sum_{g\in G}\rchi(g)\tag{1}$$

.

More generally, in [§Representation Theory of Finite Groups, ⁋Definition 3](/en/math/representation_theory/representations_of_finite_groups#def3){: data-lid="fxp7g" }, for any $G$-representations $V,W$, regarding them as underlying $\mathbb{C}$-vector spaces, we defined on their $\Hom$-set $\Hom_\mathbb{C}(V,W)$ the $G$-action

$$(g\cdot f)(v)=g\cdot f(g^{-1}\cdot v)\qquad\text{for all $v\in V$}$$

. Then the equation

$$\Hom_\mathbb{C}(V,W)^G=\Hom_G(V,W)$$

holds; therefore, applying equation (1) to $U=\Hom(V,W)$ and the corresponding projection $p$, we see that

$$\dim \Hom_G(V,W)=\tr(p)=\frac{1}{\lvert G\rvert}\sum_{g\in G}\rchi_{\Hom(V,W)}(g)$$

. On the other hand, using $\Hom_\mathbb{C}(V,W)\cong V^\ast\otimes W$, the character on the right-hand side is given by the equation

$$\rchi_{\Hom_\mathbb{C}(V,W)}(g)=\overline{\rchi_V(g)}\rchi_W(g)$$

, so the equation above can be rewritten as

$$\dim\Hom_G(V,W)=\frac{1}{\lvert G\rvert}\sum_{g\in G}\overline{\rchi_V(g)}\rchi_W(g)=\langle \rchi_W, \rchi_V\rangle$$

. Finally, assuming that $V,W$ are irreducible representations, we know from [§Representation Theory of Finite Groups, ⁋Lemma 8](/en/math/representation_theory/representations_of_finite_groups#lem8){: data-lid="cn3dy" } that for $\Hom_G(V,W)$, if $V\cong W$, it is $1$-dimensional, and otherwise $0$-dimensional, so

$$\dim \Hom_\mathbb{C}(V,W)^G=\dim \Hom_G(V,W)=\begin{cases}1&\text{if $V\cong W$,}\\0&\text{otherwise}\end{cases}$$

, from which we obtain the equation

$$\langle \rchi_W,\rchi_V\rangle=\delta_{VW}$$

. That is, with respect to the inner product of [Definition 4](#def4){: data-lid="0euwm" }, the irreducible characters form an orthonormal set. Since we know that $\mathbb{C}_\class(G)$ has dimension equal to the number of conjugacy classes of $G$, it follows from this that there cannot be more irreducible representations than the number of conjugacy classes of $G$. Moreover, using this inner product, for any representation $V$ with character $\rchi_V$, and a fixed irreducible representation $V_i$ with character $\rchi_{V_i}$, we can take their inner product to compute within $V$ the multiplicity of $V_i$.

## Regular Representation

In this section, we obtain the Artin-Wedderburn decomposition considered in [§Representation Theory of Finite Groups, §§Maschke's Theorem](/en/math/representation_theory/representations_of_finite_groups#maschkes-theorem){: data-lid="b18uv" } using characters. To this end, first observe that $\mathbb{C}[G]$ is a left $\mathbb{C}[G]$-module defined over itself, and thus from the categorical equivalence

$$\Rep_\mathbb{C}(G)\cong \lMod{\mathbb{C}[G]}$$

, it is also a representation of $G$. This is obtained simply by restricting the module structure defined on $\mathbb{C}[G]$, that is, the multiplication structure of $\mathbb{C}[G]$ as a ring, to $G$; explicitly, for any $g\in G$, using its image in $\mathbb{C}[G]$, $\delta_g=\sum_{x\in G}\delta_g(x)x$, we can write

$$g\cdot \left(\sum_{y\in G} \phi(y)y\right)=\left(\sum_{x\in G}\delta_g(x)x\right)\left(\sum_{y\in G}\phi(y)y\right)=\sum_{z\in G}\left(\sum_{x\in G}\delta_g(x)\phi(x^{-1}z)\right)z=\sum_{z\in G}\phi(g^{-1}z)z=\sum_{z\in G}\phi(z)(gz)$$

, and such a representation is called the *regular representation*.

Now to decompose $\mathbb{C}[G]$, we consider the character theory of the regular representation. Viewing $\mathbb{C}[G]$ as above as a vector space with the elements $g\in G$ (more precisely, the $\delta_g$) as a basis, if we represent each linear operator from the regular representation $\rho_\reg$, that is, $\rho_\reg(g)$, as a matrix and consider its trace, we have

$$\rchi_{\mathbb{C}[G]}(g)=\begin{cases}\lvert G\rvert&\text{if $g=e$}\\0&\text{otherwise}\end{cases}\tag{2}$$

. Now if $V_i$ is an irreducible subrepresentation of $\mathbb{C}[G]$, then

$$\langle\rchi_{\mathbb{C}[G]}, \rchi_{V_i}\rangle=\frac{1}{\lvert G\rvert}\sum_{g\in G}\rchi_{\mathbb{C}[G]}(g)\overline{\rchi_{V_i}(g)}=\frac{1}{\lvert G\rvert} \rchi_{\mathbb{C}[G]}(e)\overline{\rchi_{V_i}(e)}=\dim V_i$$

holds. That is, we obtain the following decomposition:

$$\mathbb{C}[G]\cong \bigoplus_{i=1}^r V_i^{\oplus\dim V_i}$$

. Furthermore, considering that $\mathbb{C}[G]$ acts on itself by multiplication, and under this action, by [§Representation Theory of Finite Groups, ⁋Lemma 8](/en/math/representation_theory/representations_of_finite_groups#lem8){: data-lid="8laa2" }, $V_i$ is mapped only to $V_i$, we know that each $V_i^{\oplus\dim V_i}$ is precisely the matrix algebra $\Mat_{d_i}(\mathbb{C})$, and from the uniqueness of the Artin-Wedderburn theorem, we can verify that this is indeed equal to

$$\mathbb{C}[G]\cong \bigoplus_{i=1}^r\Mat_{d_i}(\mathbb{C})$$

.

## Projection Formula

Earlier, we showed that the characters of irreducible representations form an orthonormal set in $\mathbb{C}_\class(G)$. Now we show that they form an orthonormal basis of $\mathbb{C}_\class(G)$.

::: Lemma 5
Let an arbitrary function $\phi:G\rightarrow \mathbb{C}$ and an arbitrary representation $\rho:G\rightarrow\Aut(V)$ be given. If we define

$$\rho_\phi=\sum_{g\in G} \phi(g)\rho(g): V\rightarrow V$$

then $\rho_\phi$ is a $G$-map if and only if $\phi$ is a class function. 
:::
::: Proof
In order for $\rho_\phi$ to be a $G$-map, for any $h\in G$ and any $v\in V$, the equation

$$\rho_\phi(h\cdot v)=h\cdot\rho_\phi(v)$$

must hold. Directly computing the left-hand side,

$$\rho_\phi(h\cdot v)=\sum_{g\in G}\phi(g)\rho(g)(h\cdot v)$$

and since taking this sum over $hgh^{-1}$ yields the same sum, we can write

$$\rho_\phi(hv)=\sum_{g\in G}\phi(hgh^{-1})\rho(hgh^{-1})(h\cdot v)=\sum_{g\in G}\phi(hgh^{-1})\rho(h)\rho(g)(v)=\rho(h)\left(\sum_{g\in G}\phi(hgh^{-1})\rho(g)v\right)$$

Now, for this to be equal to

$$h\cdot\rho_\phi(v)=\rho(h)\rho_\phi(v)=\rho(h)\left(\sum_{g\in G}\phi(g)\rho(g)(v)\right)$$

it must precisely be that $\phi(g)=\phi(hgh^{-1})$, that is, $\phi$ must be a class function. 
:::

Now, using this, we show that every class function is expressed as a linear combination of irreducible characters. That is, for a class function $\phi$, we must show that if $\langle \rchi_V,\phi\rangle=0$ holds for all irreducible characters $\rchi_V$, then $\phi=0$. 

To this end, let us apply the above lemma to a class function $\phi$ and an irreducible representation $\rho:G\rightarrow\Aut(V)$. Since $\phi$ is a class function, so is $\overline{\phi}$, and thus $\rho_{\overline{\phi}}$ is a $G$-map; by [§Representation Theory of Finite Groups, ⁋Lemma 8](/en/math/representation_theory/representations_of_finite_groups#lem8){: data-lid="kyv69" }, $\rho_{\overline{\phi}}$ is of the form $\lambda\id_V$. Taking the trace here, we see that

$$(\dim V)\lambda=\tr(\rho_{\overline{\phi}})=\tr\left(\sum_{g\in G}\overline{\phi(g)}\rho(g)\right)=\sum_{g\in G}\overline{\phi(g)}\rchi_V(g)=\lvert G\rvert\langle \rchi_V,\phi\rangle=0$$

Now, since every representation has an irreducible decomposition, we know that $\sum \overline{\phi(g)}g$ must act as $0$ on every representation, and in particular on the regular representation $\mathbb{C}[G]$. However, acting this element on $\delta_e$ in the regular representation gives

$$\left(\sum\overline{\phi(g)}g\right)\cdot \delta_e=\sum_{g\in G}\overline{\phi(g)}g$$

and therefore $\overline{\phi(g)}=0$ must hold for all $g$. 

## Example: $S_3$

We conclude this post with an example illustrating the theory developed since the previous post. First, for an arbitrary *abelian* group $G$, in an irreducible representation $\rho:G\rightarrow\Aut(V)$, each $\rho(h)$ is a $G$-map and thus acts as a scalar by [§Representation Theory of Finite Groups, ⁋Lemma 8](/en/math/representation_theory/representations_of_finite_groups#lem8){: data-lid="vzycy" }, from which every subspace of $V$ is a subrepresentation, so $V$ is $1$-dimensional. Therefore, to test our theory, we need a non-abelian group. For computational convenience, let us consider the smallest non-abelian group, $S_3$. Explicitly,

$$S_3=\{(\ ),(1\ 2),(1\ 3),(2\ 3),(1\ 2\ 3),(1\ 3\ 2)\}$$

First, it is clear that the following two representations

$$\rho_0: S_3 \rightarrow \Aut(\mathbb{C})\qquad \sigma\mapsto \id_\mathbb{C}$$

and 

$$\rho_\sgn: S_3 \rightarrow \Aut(\mathbb{C})\qquad \sigma\mapsto \sgn(\sigma)\id_\mathbb{C}$$

are two irreducible representations of $S_3$. Meanwhile, $S_3$ acts on $\mathbb{C}^3$ by permutation via

$$\sigma\cdot(x_1,x_2,x_3)=(x_{\sigma(1)},x_{\sigma(2)},x_{\sigma(3)})$$

However, this action is trivial along the line spanned by $(1,1,1)$, and can be viewed as acting entirely on the subspace

$$V_\std=\{(x_1,x_2,x_3)\mid x_1+x_2+x_3=0\}$$

orthogonal to this line, and one can verify that this subrepresentation is irreducible. We call this the *standard representation* of $S_3$. 

These three representations are $1,1,2$-dimensional, respectively, and since

$$\lvert S_3\rvert=6=1^2+1^2+2^2$$

we can verify that the dimensions match the irreducible decomposition. Going a step further, let us compute the characters of these three irreducible representations. For this, consider the conjugacy classes of $S_3$:

$$A_1=\{(\ )\},\qquad A_2=\{(1\ 2),(1\ 3),(2\ 3)\},\qquad A_3=\{(1\ 2\ 3),(1\ 3\ 2)\}$$

For convenience of notation, if a character $\rchi$ takes values $a_1,a_2,a_3$ on $A_1,A_2,A_3$, we write it in the vector form $(a_1,a_2,a_3)$. 

- $\rho_0$ sends every element of $S_3$ to $\id_\mathbb{C}\in \Aut(\mathbb{C})$, and since the trace of this $1\times 1$ matrix is $1$, $\rchi_0$ is $(1,1,1)$. 
- $\rho_\sgn$ sends only the odd permutations of $S_3$ (i.e. the elements of $A_2$) to $-\id_\mathbb{C}\in\Aut(\mathbb{C})$, and sends the remaining elements to $\id_\mathbb{C}\in \Aut(\mathbb{C})$, so $\rchi_\sgn$ is $(1,-1,1)$. 

For the standard representation $\rho_\std$, there are two ways to compute its character $\rchi_\std$, and we present both methods.

First, to compute this directly, let us choose a basis of $V_\std$:

$$\{e_1=(1,0,-1), e_2=(0,1,-1)\}$$

Then $(\ )$ does not affect this basis, so naturally $\rchi_\std$ takes the value $2$ on $A_1$. On $A_2$, for instance, acting by $(1\ 2)$ swaps the basis elements with each other, which corresponds to the matrix

$$\rho_\std((1\ 2))=\begin{pmatrix}0&1\\1&0\end{pmatrix}$$

whose trace is $0$. For reference, if $(1\ 3)$ acts on this basis, $e_1$ is sent to $-e_1$ and $e_2$ is sent to $(-1,1,0)=-e_1+e_2$, corresponding to the matrix

$$\rho_\std((1\ 3))=\begin{pmatrix}-1&-1\\0&1\end{pmatrix}$$

and since the trace of this matrix is also $0$, we can confirm by calculation that the character function is indeed a class function. In the case of $A_3$, since it sends $e_1$ to $(-1,1,0)=-e_1+e_2$ and $e_2$ to $(-1,0,1)=-e_1$, we have

$$\rho_\std((1\ 2\ 3))=\begin{pmatrix}-1&-1\\1&0\end{pmatrix}$$

showing that $\rchi_\std$ is $(2,0,-1)$. 

A more convenient calculation method is, denoting the representation spaces of $\rho_0$ and the permutation representation by $V_0$ and $V_\perm$ respectively, to use the decomposition

$$V_\perm=V_0\oplus V_\std$$

We already know that the character of $V_0$ is $(1,1,1)$. Now considering the action on $V_\perm$, since

$$\rho_\perm((\ ))=\begin{pmatrix}1&0&0\\0&1&0\\0&0&1\end{pmatrix},\quad \rho_\perm((1\ 2))=\begin{pmatrix}0&1&0\\1&0&0\\0&0&1\end{pmatrix},\quad \rho_\perm((1\ 2\ 3))=\begin{pmatrix}0&1&0\\0&0&1\\1&0&0\end{pmatrix}$$

we know that $\rchi_\perm$ is $(3,1,0)$, and now from [Proposition 2](#prop2){: data-lid="j4xpb" }, since $\rchi_\perm=\rchi_0+\rchi_\std$, we see that $\rchi_\std$ is $(2,0,-1)$. The three characters obtained in this way,

$$\rchi_0=(1,1,1),\qquad \rchi_\sgn=(1,-1,1),\qquad \rchi_\std=(2,0,-1)$$

are orthonormal (as expected).

From the calculation of the character of the regular representation, we know that

$$\rchi_{\mathbb{C}[S_3]}(g)=\begin{cases}6&\text{if $g=e$}\\0&\text{otherwise}\end{cases}$$

(equation (2)). This must be a $\mathbb{Z}_{\geq 0}$-linear combination of the three characters above, and indeed we can verify that

$$\rchi_{\mathbb{C}[S_3]}=\rchi_0+\rchi_\sgn+2\rchi_\std$$

This result also agrees with the discussion above that the multiplicity of each irreducible factor in the regular representation must equal its own dimension. 

---

**References**

**[FH]** W. Fulton and J. Harris, *Representation theory: a first course*, Springer, 1991.
