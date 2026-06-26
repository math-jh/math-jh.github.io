---
title: "Richardson Varieties and Peterson Varieties"
description: "This post covers Richardson varieties, defined as intersections of Schubert and opposite Schubert varieties, and Peterson varieties, cut out by regular nilpotent elements. It examines the definitions, dimensions, roles in intersection theory, concrete appearances in Grassmannians and type A, and stratifications by Bruhat cells."
excerpt: "Richardson varieties as transversal intersections of opposite Schubert varieties, and Peterson varieties from regular nilpotents: definitions, dimensions, intersection theory, and stratification"

categories: [Math / Lie Theory]
permalink: /en/math/lie_theory/richardson_peterson_variety
sidebar:
    nav: "Lie_theory-en"

date: 2026-06-09
weight: 6
translated_at: 2026-06-26T19:00:01+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-26T19:00:01+00:00
---
In [§Bruhat decomposition](/en/math/lie_theory/bruhat_decomposition) we saw that the partial flag variety $$G/P$$ decomposes into Bruhat cells, and that the geometry of $$G/P$$ is encoded in the combinatorics of the Weyl group through the closures of these cells, the Schubert varieties. In this post we discuss two kinds of subvarieties that naturally sit above this decomposition. One is the *Richardson variety*, obtained as the intersection of two opposite Bruhat decompositions, and the other is the *Peterson variety*, cut out by a single regular nilpotent element.

## Richardson variety

As in [§Bruhat decomposition](/en/math/lie_theory/bruhat_decomposition), we fix a connected reductive algebraic group $$G$$ over the field $$\mathbb{C}$$, a Borel subgroup $$B$$, and a parabolic subgroup $$P$$ containing $$B$$. Taking also the opposite Borel subgroup $$B^-$$ (with $$B\cap B^-=T$$), we obtain the two cell structures introduced in [§Bruhat decomposition, ⁋Definition 16](/en/math/lie_theory/bruhat_decomposition#def16)

$$X_w^\circ=BwP/P,\qquad X^w_\circ=B^-wP/P\qquad(w\in W^P)$$

and their Zariski closures, the Schubert variety $$X_w=\overline{X_w^\circ}$$ and the opposite Schubert variety $$X^w=\overline{X^w_\circ}$$. The two cells satisfy $$X_w^\circ\cong\mathbb{A}^{\ell(w)}$$ and $$X^w_\circ\cong\mathbb{A}^{\dim(G/P)-\ell(w)}$$, and the Richardson variety is the intersection of these two cells.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> For $$u,w\in W^P$$, the intersection of a Schubert variety and an opposite Schubert variety

$$R_{u,w}=X_w\cap X^u$$

is called a *Richardson variety*, and the intersection of the two open cells

$$\mathring{R}_{u,w}=X_w^\circ\cap X^u_\circ$$

is called an *open Richardson variety*.

</div>

By definition $$R_{u,w}$$ is a closed subvariety of $$G/P$$, and $$\mathring{R}_{u,w}$$ is a Zariski open subset of it. This intersection already appeared in the work of Kazhdan–Lusztig [KL80] and Deodhar [Deo85], and its general geometric properties were later studied by Richardson [Ric92].

The usefulness of this definition is best seen in the Grassmannian $$\Gr(k,n)$$ (or more generally in a partial flag variety). Fixing a reference flag $$E_\bullet\colon E_1\subset E_2\subset\cdots\subset E_n=\mathbb{C}^n$$, recall that each Schubert cell is determined by the way a $$k$$-dimensional subspace $$V$$ meets this flag, namely by the jumps in $$\dim(V\cap E_j)$$ as $$j$$ increases. Computing the intersection of two Schubert cells inside the Grassmannian amounts to finding the incidence conditions they satisfy simultaneously. However, if the two Schubert cells are defined with respect to the same reference flag, the two conditions are not independent and the intersection fails to have the expected dimension; one must instead choose reference flags in generic position.

The easiest example of this is the *opposite flag* $$\tilde{E}_j=\span\{e_n,\ldots,e_{n-j+1}\}$$, which reads the given flag $$E_i=\span\{e_1,\ldots,e_i\}$$ in reverse. These two flags satisfy the transversality condition

$$\dim(E_i\cap\tilde{E}_j)=\max(0,\,i+j-n)$$

for all $$i,j$$. In other words, any pair of pieces from the two flags meets as little as possible. The Richardson variety is precisely the simultaneous imposition of Schubert conditions with respect to two reference flags in generic position, and the fact that $$X_w$$ encodes the condition for the standard flag fixed by $$B$$ while $$X^u$$ encodes the condition for the opposite flag fixed by $$B^-$$ corresponds exactly to this transversality.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2 (Richardson [Ric92])**</ins> The open Richardson variety $$\mathring{R}_{u,w}$$ is nonempty if and only if $$u\leq w$$ in the Bruhat order. When this holds, $$\mathring{R}_{u,w}$$ is a smooth irreducible affine variety of dimension $$\ell(w)-\ell(u)$$, and $$R_{u,w}$$ is its Zariski closure.

</div>

Intuitively, recall that the Schubert variety $$X_w$$ grows outward from a point $$X_e=\{eP\}$$ in increasing dimension, while the opposite Schubert variety $$X^u$$ descends from all of $$G/P$$ in decreasing dimension. Concretely, $$\dim X_w=\ell(w)$$ and $$\dim X^u=\dim(G/P)-\ell(u)$$, so for the two varieties to meet, the sum of their dimensions must be at least $$\dim(G/P)$$, i.e. $$\ell(u)\leq\ell(w)$$, and the expected dimension of the intersection is then

$$\ell(w)+\dim (G/P)-\ell(u)-\dim (G/P)=\ell(w)-\ell(u).$$

However, having the correct dimension alone does not guarantee the intersection is nonempty. For instance, consider the incomparable pair $$u=1423$$, $$w=2314$$ from [§Bruhat decomposition, ⁋Example 18](/en/math/lie_theory/bruhat_decomposition#ex18): their lengths are equal so the expected dimension is $$0$$, yet their intersection is empty rather than a set of points. Let us see directly what happens in $$\Gr(2,4)$$. A point of $$X_{2314}$$ satisfies the rank condition $$\dim(V\cap E_3)\geq2$$, i.e. $$V\subseteq E_3$$. On the other hand, every point of the opposite cell $$X^{1423}_\circ=B^-\cdot\span\{e_1,e_4\}$$ contains $$e_4$$ (lower triangular matrices fix $$e_4$$ up to scalar), and since $$e_4\in V$$ is a closed condition, this persists in the closure $$X^{1423}$$. Because $$e_4\notin E_3$$, the two requirements are incompatible, and the two varieties pass by each other despite having sufficient dimension.

This phenomenon arises because $$X_w$$ and $$X^u$$ are not arbitrary subvarieties in general position; both are invariant under the action of the maximal torus $$T$$, placing them in special positions. Because of this, their intersection $$X_w\cap X^u$$ is also a closed $$T$$-stable subvariety, and it is known that any nonempty closed $$T$$-stable subvariety contains a $$T$$-fixed point (Borel fixed point theorem, see [Bri]). Now the $$T$$-fixed points of $$G/P$$ are precisely the coordinate points $$vP$$ for $$v\in W^P$$ ([§Bruhat decomposition, ⁋Proposition 19](/en/math/lie_theory/bruhat_decomposition#prop19)). Moreover, $$vP\in X_w$$ is equivalent to $$v\leq w$$ ([§Bruhat decomposition, ⁋Proposition 17](/en/math/lie_theory/bruhat_decomposition#prop17)), and symmetrically $$vP\in X^u$$ is equivalent to $$u\leq v$$. Therefore

$$X_w\cap X^u\neq\emptyset\iff\text{there exists }v\in W^P\text{ with }u\leq v\leq w\iff u\leq w.$$

In the example above, the jump set condition $$\{1,4\}\leq\{v(1),v(2)\}\leq\{2,3\}$$ requires $$4\leq v(2)\leq3$$, so no such $$v$$ exists; conversely, if $$u\leq w$$ then choosing $$v=u$$ makes the fixed point $$uP$$ a point of $$R_{u,w}$$. This is the precise geometric content of the condition $$u\leq w$$ in [Proposition 2](#prop2).

It is then natural to expect the following proposition.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> For $$u,w\in W^P$$, in the cohomology ring $$H^\ast(G/P)$$ we have

$$[X_w]\cdot[X^u]=[R_{u,w}]$$

(where if $$u\not\leq w$$ then $$R_{u,w}=\emptyset$$ and both sides are $$0$$). In particular, when $$\ell(u)=\ell(w)$$,

$$\int_{G/P}[X_w]\cdot[X^u]=\delta_{u,w}$$

so the opposite Schubert classes $$\{[X^u]\}_{u\in W^P}$$ form the Poincaré dual basis to the Schubert classes $$\{[X_w]\}_{w\in W^P}$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

$$X_w$$ and $$X^u$$ meet transversally in the generic position given by $$B$$ and $$B^-$$, so their intersection class equals the product of the two classes. This gives $$[X_w]\cdot[X^u]=[R_{u,w}]$$ (Kleiman's generic transversality, see [Bri]). When $$\ell(u)=\ell(w)$$, the dimension of $$R_{u,w}$$ is $$\ell(w)-\ell(u)=0$$, and by [Proposition 2](#prop2), if $$u=w$$ it is a reduced point, while if $$u\neq w$$ (so $$u\leq w$$ fails) it is empty. Hence the degree of this $$0$$-dimensional class, namely $$\int_{G/P}[X_w]\cdot[X^u]$$, is $$\delta_{u,w}$$.

</details>

[Proposition 3](#prop3) reduces the structure constants for multiplication in the Schubert basis to the degrees of Richardson varieties. Integrating the triple product $$[X_w]\cdot[X^u]\cdot[X_v]$$ gives the intersection number of three Schubert varieties in generic position, which is precisely the structure constant; in the case of the Grassmannian this becomes the Littlewood–Richardson coefficient, and from this classical Schubert calculus unfolds.

Again, the most tangible case is the Grassmannian $$G/P=\Gr(k,n)\cong\GL_n(\mathbb{C})/P_k$$. Here $$W=S_n$$, $$W_{P_k}=S_k\times S_{n-k}$$, and the minimal length coset representatives $$W^{P_k}$$ are the $$(k,n-k)$$-shuffles from [§Bruhat decomposition, ⁋Proposition 14](/en/math/lie_theory/bruhat_decomposition#prop14). The Schubert variety $$X_w$$ is cut out by rank conditions of the form $$\dim(V\cap E_{w(a)})\geq a$$ with respect to the standard flag $$E_\bullet$$, and the opposite Schubert variety $$X^u$$ is cut out by symmetric rank conditions with respect to the opposite flag $$\tilde{E}_\bullet$$ ($$\tilde{E}_j=\span\{e_n,\ldots,e_{n-j+1}\}$$). The Richardson variety is the simultaneous imposition of both conditions.

<div class="example" markdown="1">

<ins id="ex4">**Example 4**</ins> In $$\Gr(2,4)$$, take $$u=1324$$ and $$w=2413$$. In the jump set order from [§Bruhat decomposition, ⁋Example 18](/en/math/lie_theory/bruhat_decomposition#ex18), we have $$1324\leftrightarrow\{1,3\}$$ and $$2413\leftrightarrow\{2,4\}$$, and since $$1\leq2$$ and $$3\leq4$$ componentwise, we have $$u\leq w$$, with $$\ell(2413)-\ell(1324)=3-1=2$$. The two Schubert conditions are

$$X_{2413}=\{V\mid\dim(V\cap E_2)\geq1\},\qquad X^{1324}=\{V\mid\dim(V\cap\tilde{E}_2)\geq1\}$$

where $$E_2=\span\{e_1,e_2\}$$ and $$\tilde{E}_2=\span\{e_3,e_4\}$$ are two complementary planes. Thus

$$R_{1324,2413}=\{V\in\Gr(2,4)\mid V\cap E_2\neq0,\ V\cap\tilde{E}_2\neq0\}$$

is the family of planes spanned by a line in $$E_2$$ and a line in $$\tilde{E}_2$$. Since $$E_2\cap\tilde{E}_2=0$$, the two lines are always independent, and the correspondence $$([\,p\,],[\,q\,])\mapsto\langle p,q\rangle$$ gives an isomorphism

$$R_{1324,2413}\cong\mathbb{P}(E_2)\times\mathbb{P}(\tilde{E}_2)\cong\mathbb{P}^1\times\mathbb{P}^1.$$

This is a variety of dimension $$2$$, matching exactly the dimension from [Proposition 2](#prop2). Its open part is parametrized by matrices

$$V=\operatorname{rowspan}\begin{pmatrix}1&s&0&0\\0&0&1&t\end{pmatrix}\qquad(s,t)\in\mathbb{A}^2$$

the jump set of the above matrix is $$\{2,4\}$$ so $$V\in X_{2413}^\circ$$, and the second row lies in $$\tilde{E}_2$$ so $$V\in X^{1324}_\circ$$. Thus $$\mathring{R}_{1324,2413}$$ is an open subset of this $$(s,t)$$-plane, and its affine dimension $$2$$ is immediately visible from the coordinates.

</div>

## Peterson variety

We now shift our perspective somewhat to define a new variety. This begins with a new way of looking at the flag variety $$G/B$$. Recall that $$G$$ acts on its own Borel subalgebras by conjugation

$$g\cdot\mathfrak{b}'=\Ad(g)\,\mathfrak{b}'$$

([§Borel subgroup, ⁋Proposition 10](/en/math/lie_theory/borel_subgroup#prop10)). Since any two Borel subalgebras are conjugate, this action is transitive, and the stabilizer of $$\mathfrak{b}$$ is its normalizer $$N_G(\mathfrak{b})=B$$. Hence the orbit-stabilizer theorem gives a bijection $$gB\mapsto\Ad(g)\mathfrak{b}$$ between $$G/B$$ and the set of Borel subalgebras of $$G$$. In other words, $$G/B$$ can be thought of as the variety of Borel subalgebras of $$G$$.

Now recall again that $$G/B$$ is a flag variety, and that $$gB$$ determines a single flag as a point of this variety. That is, the above bijection attaches to each flag the corresponding Borel subalgebra $$\Ad(g)\mathfrak{b}$$. But this can be generalized a bit further. If we choose an $$\ad(\mathfrak{b})$$-stable subspace $$H\subseteq\mathfrak{g}$$ containing $$\mathfrak{b}$$, then $$H$$ is $$B$$-stable, so $$\Ad(g)H$$ depends only on the coset $$gB$$. Thus we can assign to each flag a subspace $$\Ad(g)H$$.

From this perspective, asking whether a fixed element $$X\in\mathfrak{g}$$ lies in one of these subspaces is interpreted in the flag variety as an incidence condition of an appropriate kind. Indeed, the condition $$\Ad(g^{-1})X\in H$$ is a polynomial condition on the entries of $$g$$, so the set of $$gB$$ satisfying it actually forms a closed subvariety of $$G/B$$.

Our object of interest is this closed variety, which of course depends on the choices of $$X$$ and $$H$$. For instance, if $$X=0$$ then the condition always holds, so we get the entire flag variety $$G/B$$. A useful measure of the dependence on $$X$$ is its centralizer. Consider an element $$z$$ of $$G$$ that centralizes $$X$$. If $$z$$ acts on $$G/B$$ by $$gB\mapsto zgB$$, then the left-hand side of the incidence condition becomes

$$\Ad((zg)^{-1})X=\Ad(g^{-1})X.$$

Thus this incidence condition is invariant under left translation by $$z$$, and from this we obtain a group action of the centralizer $$C_G(X)$$ on the closed variety we are considering. That is, this closed variety is a union of $$C_G(X)$$-orbits, so intuitively we expect that the larger the centralizer, the larger the closed subvariety of $$G/B$$ cut out in this way. The case $$X=0$$ was the extreme case where the centralizer is all of $$G$$. However, it is known that the dimension of the centralizer cannot drop below $$\rank(\mathfrak{g})$$ for any $$X\in\mathfrak{g}$$ ([Kos63]), so the opposite extreme is the elements achieving this minimum.

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> A nilpotent element $$X\in\mathfrak{g}$$ is called *regular* if the dimension of its centralizer $$\mathfrak{z}_{\mathfrak{g}}(X)=\{Z\in\mathfrak{g}\mid[Z,X]=0\}$$ equals $$\rank(\mathfrak{g})$$.

</div>

Regular nilpotents always exist by a standard construction: for each simple root $$\alpha_i$$ choose $$0\neq e_i\in\mathfrak{g}_{\alpha_i}$$ and set $$e=\sum_i e_i$$; this gives a regular nilpotent.

In the familiar type $$A_{n-1}$$, this yields a concrete example. The above construction gives the principal nilpotent with all superdiagonal entries equal to $$1$$:

$$N=\sum_{i=1}^{n-1}E_{i,i+1}=\begin{pmatrix}0&1&&\\&0&\ddots&\\&&\ddots&1\\&&&0\end{pmatrix}.$$

Solving $$[Z,N]=0$$ entrywise, one finds that the centralizer consists of polynomials in $$N$$:

$$\mathfrak{z}_{\mathfrak{sl}_n}(N)=\span\{N,N^2,\ldots,N^{n-1}\}$$

and since this space has dimension exactly $$n-1=\rank(\mathfrak{sl}_n)$$, $$N$$ is regular. From the viewpoint of Jordan canonical form, $$N$$ is the nilpotent with a single Jordan block, corresponding to the partition $$(n)$$. The more Jordan blocks, the larger the centralizer, so a regular nilpotent can be thought of as the nilpotent element in the conjugacy class with the smallest centralizer.

In general type, the fact that $$e=\sum_i e_i$$ is regular, that all regular nilpotents are conjugate under the adjoint action of $$G$$, and that their centralizer is always abelian, are classical results of Kostant [Kos].

Now let us add the dependence on $$H$$ to the closed subvariety we were considering with $$X$$ fixed. For convenience we give it a name first.

<div class="definition" markdown="1">

<ins id="def6">**Definition 6**</ins> For $$X\in\mathfrak{g}$$ and an $$\ad(\mathfrak{b})$$-stable subspace $$H\subseteq\mathfrak{g}$$ containing $$\mathfrak{b}$$ (i.e. $$[\mathfrak{b},H]\subseteq H$$), the *Hessenberg variety* is the closed subvariety of $$G/B$$ defined by

$$\mathcal{B}(X,H)=\{\,gB\in G/B\;\mid\;\Ad(g^{-1})X\in H\,\}.$$

</div>

As we saw above, $$X$$ influences the size of the variety through its centralizer, and the same holds for the subspace $$H$$. Two extreme situations: when $$H=\mathfrak{g}$$, the condition $$\Ad(g^{-1})X\in\mathfrak{g}$$ holds trivially and the Hessenberg variety is all of $$G/B$$. At the opposite extreme $$H=\mathfrak{b}$$, the condition $$\Ad(g^{-1})X\in\mathfrak{b}$$ says that the Borel subalgebra $$\Ad(g)\mathfrak{b}$$ contains $$X$$, and if $$X$$ is nilpotent we call this the *Springer fiber* of $$X$$.

The Peterson variety we will define can be thought of as the closed subvariety obtained by imposing the strongest possible conditions using $$X$$ and $$H$$. For $$X$$, the argument before [Definition 6](#def6) shows that the regular nilpotent condition imposes the strongest constraint, in which case $$X$$ belongs to exactly one Borel subalgebra and the Springer fiber $$\mathcal{B}(X, \mathfrak{b})$$ collapses to a point. Thus we loosen the condition on $$H$$ slightly to define the Peterson variety.

To see in which direction we can enlarge $$H$$, it becomes clear if we work out the condition of [Definition 6](#def6) in coordinates in type $$A$$.

<div class="example" markdown="1">

<ins id="ex7">**Example 7**</ins> Let us return to type $$A_{n-1}$$ examined above. Here $$G=\GL_n(\mathbb{C})$$, $$\mathfrak{b}$$ is the space of upper triangular matrices, and the Cartan subalgebra of $$\gl_n$$ is the space of diagonal matrices $$\mathfrak{h}$$.[^1]

Since $$H$$ is $$\ad(\mathfrak{b})$$-stable, it must also be $$\ad(\mathfrak{h})$$-stable. Computing the bracket of an arbitrary $$Y\in H$$ with an arbitrary diagonal matrix $$\diag(t_1,\ldots, t_n)$$, we get

$$\ad(\diag(t_1,\ldots, t_n))Y=[\diag(t_1,\ldots, t_n), Y]=((t_j-t_k)Y_{jk})_{1\leq j,k\leq n}$$

and for $$\ad(\mathfrak{h})$$-stability this must again lie in $$H$$.

Moreover, the above calculation shows in particular that when viewed as a linear operator on $$\gl_n$$, this linear operator has all the basis elements $$E_{jk}$$ as eigenvectors. Now taking $$t$$ generic, the eigenvalues $$t_j-t_k$$ for $$j\neq k$$ are all distinct from each other and from $$0$$, so an invariant subspace $$H$$ of this operator decomposes into intersections with each eigenspace, giving a weight decomposition

$$H=(H\cap \mathfrak{h})\oplus\bigoplus_{j\neq k}(H\cap \mathbb{C}E_{jk}).$$

Thus $$H$$ is determined by the positions of the matrix entries it contains. That is, $$H$$ is the span of the full diagonal ($$\mathfrak{h}\subseteq\mathfrak{b}\subseteq H$$) together with the elementary matrices $$E_{jk}$$ it contains. To see concretely which entries can belong to $$H$$, we compute brackets with the upper triangular direction: for $$l\leq j$$ and $$k\leq m$$,

$$[E_{lj},E_{jk}]=E_{lk}-\delta_{kl}E_{jj},\qquad[E_{jk},E_{km}]=E_{jm}-\delta_{jm}E_{kk}$$

and since the $$\delta$$ terms already lie in $$\mathfrak{h}\subseteq H$$, if $$H$$ contains position $$(j,k)$$ then it must also contain all positions above it in the same column, $$(l,k)$$ for $$l\leq j$$, and all positions to the right in the same row, $$(j,m)$$ for $$m\geq k$$. Thus each column is filled from the top without gaps, and the filled depth does not decrease as we move to the right. Writing $$h(k)$$ for the depth of the $$k$$-th column, $$H$$ is the staircase determined by a nondecreasing function $$h\colon\{1,\ldots,n\}\to\{1,\ldots,n\}$$ with $$h(i)\geq i$$ (a *Hessenberg function*):

$$H_h=\{\,Y\in\mathfrak{gl}_n\;\mid\;YE_i\subseteq E_{h(i)}\ \forall i\,\}=\{\,Y\;\mid\;Y_{jk}=0\ \text{whenever }j>h(k)\,\}$$

and the converse is easily verified. For example, when $$n=4$$ the two staircases

$$\mathfrak{b}=H_{(1,2,3,4)}=\begin{pmatrix}\ast&\ast&\ast&\ast\\0&\ast&\ast&\ast\\0&0&\ast&\ast\\0&0&0&\ast\end{pmatrix},\qquad H_{(2,3,4,4)}=\begin{pmatrix}\ast&\ast&\ast&\ast\\\ast&\ast&\ast&\ast\\0&\ast&\ast&\ast\\0&0&\ast&\ast\end{pmatrix}$$

correspond to $$h(i)=i$$ and $$h(i)=\min(i+1,n)$$ respectively.

Now returning to the language of flag varieties, let the flag corresponding to a coset $$gB$$ be $$V_\bullet=g\cdot E_\bullet$$ (i.e. $$V_i=\span\{ge_1,\ldots,ge_i\}$$). Then for arbitrary $$X\in\mathfrak{gl}_n$$,

$$\Ad(g^{-1})X\in H_h\iff g^{-1}Xg\in H_h\iff XgE_i\subseteq gE_{h(i)}\iff XV_i\subseteq V_{h(i)}.$$

Thus in type $$A$$, the Hessenberg variety is the variety of flags that $$X$$ is allowed to send down by at most the amount permitted by $$h$$ at each step.

</div>

The picture from [Example 7](#ex7) holds in the general case as well. Here, as above, the positions that the staircase fills above $$\mathfrak{b}$$ are below the diagonal, i.e. in the *negative* root directions. Indeed, $$\mathfrak{b}=\mathfrak{h}\oplus\bigoplus_{\alpha>0}\mathfrak{g}_\alpha$$ already contains all positive root directions, so enlarging $$H$$ beyond $$\mathfrak{b}$$ can only mean adding negative root directions. However, $$\ad(\mathfrak{b})$$-stability forces an additional simple condition: while the direction of a nonsimple positive root $$\alpha=\beta+\gamma$$ pulls in shallower positions together via $$[\mathfrak{g}_\beta,\mathfrak{g}_{-\alpha}]=\mathfrak{g}_{-\gamma}$$, the negative simple root directions are such that $$\mathfrak{b}\oplus\mathfrak{g}_{-\alpha_i}$$ is stable by itself. That is, the minimal units of expansion from $$\mathfrak{b}$$ one step at a time are precisely the $$\mathfrak{g}_{-\alpha_i}$$, and in type $$A$$ these are the subdiagonal positions in the picture above. Then the Peterson variety's $$H$$ is obtained by adding these directions to $$\mathfrak{b}$$.

<div class="definition" markdown="1">

<ins id="def8">**Definition 8**</ins> The *Peterson variety* $$\mathcal{Y}$$ is the closed subvariety of $$G/B$$ defined by

$$\mathcal{Y}=\{\,gB\in G/B\;\mid\;\Ad(g^{-1})e\in H\,\}$$

where $$e=\sum_i e_i$$ is a regular nilpotent element and $$H=\mathfrak{b}\oplus\bigoplus_i\mathbb{C}f_i$$ with $$f_i\in\mathfrak{g}_{-\alpha_i}$$ root vectors for the simple negative roots.

</div>

This definition appears to depend on several choices, but is in fact essentially unique. The choice of $$f_i$$ does not change $$H$$ since $$\mathbb{C}f_i=\mathfrak{g}_{-\alpha_i}$$ is $$1$$-dimensional, and replacing $$e$$ by another regular nilpotent merely translates $$\mathcal{Y}$$ inside $$G/B$$ (by the conjugacy discussed after [Definition 5](#def5)).

As we saw above, the degrees of freedom added to $$\mathfrak{b}$$ by $$H$$ are one for each simple root, totaling $$\rank(\mathfrak{g})$$. Since $$H=\mathfrak{b}$$ gave a point (as discussed after [Definition 6](#def6)), we expect the Peterson variety to have dimension growing from a point by that amount. Indeed this is the content of the next proposition.

<div class="proposition" markdown="1">

<ins id="prop9">**Proposition 9 (Tymoczko [Tym], Precup [Pre], Insko–Tymoczko [IT])**</ins> The Peterson variety $$\mathcal{Y}$$ admits an affine paving structure via its intersection with the Bruhat decomposition. That is, each $$\mathcal{Y}\cap BwB/B$$ is isomorphic to an affine space, and $$\mathcal{Y}$$ is their disjoint union. In particular, under this structure the largest piece has dimension $$\rank(\mathfrak{g})$$, so the dimension of $$\mathcal{Y}$$ also equals $$\rank(\mathfrak{g})$$.

</div>

We omit the proof of this proposition, but the affine paving structure itself is worth remembering. The key point is that this affine paving is indexed by subsets $$\mathcal{P}(\Delta)$$ of the simple roots: for instance, the subset containing no simple root directions, i.e. the empty set, adds no directions to $$\mathfrak{b}$$, so by the argument after [Definition 6](#def6) the corresponding affine space is a point. The affine spaces above it are determined by subsets of $$\Delta$$, and this is not merely an analogy but their relative positions are also actually governed by the subsets of $$\Delta$$.

More precisely, the piece corresponding to $$A\subseteq\Delta$$ is the intersection with the Bruhat cell defined by the longest element $$w_A$$ of the subgroup $$W_A$$ of the Weyl group generated by the reflections corresponding to the simple roots in $$A$$:

$$\mathcal{Y}\cap Bw_AB/B\cong \mathbb{A}^{\lvert A\rvert}$$

the piece where exactly the directions in $$A$$ among the degrees of freedom added to $$\mathfrak{b}$$ are activated. Moreover, under this indexing the closure relations among the pieces replicate the Boolean lattice of subsets of $$\Delta$$ exactly. That is,

$$\overline{\mathcal{Y}\cap Bw_AB/B}\;=\;\bigsqcup_{A'\subseteq A}\bigl(\mathcal{Y}\cap Bw_{A'}B/B\bigr)$$

holds. In fact this closure coincides with the intermediate Hessenberg variety obtained by enlarging $$H$$ only in the $$A$$ directions, $$\mathcal{B}(e,\,\mathfrak{b}\oplus\bigoplus_{i\in A}\mathbb{C}f_i)$$, and furthermore it is isomorphic to the Peterson variety of the Levi subgroup generated by $$A$$ ([IT]). Thus the Peterson variety has a structure of smaller Peterson varieties nested according to the subset order, from the point $$B/B$$ ($$A=\emptyset$$) using no degrees of freedom, up to the largest piece ($$A=\Delta$$) which is the intersection with the big Bruhat cell, with all intermediate relative positions governed by the combinatorics of the simple roots.

<div class="example" markdown="1">

<ins id="ex10">**Example 10**</ins> Let us examine this structure in the type $$A$$ case discussed earlier. As in [Example 7](#ex7), choosing the Hessenberg function $$h(i)=\min(i+1, n)$$, $$H$$ is the set of matrices allowed to descend exactly one step below the diagonal, and from the last equivalence in that example we know that the Peterson variety is given inside the complete flag variety $$\Fl_n=\GL_n(\mathbb{C})/B$$ by

$$\Pet_n=\{\,V_\bullet\mid NV_i\subseteq V_{i+1},\ i=1,\ldots,n-1\,\}.$$

Its dimension is

$$\sum_{j=1}^n\bigl(h(j)-j\bigr)=n-1$$

which equals $$\rank(\mathfrak{sl}_n)$$, confirming [Proposition 9](#prop9) again.

To see the individual cells, let us look more concretely at the case $$n=3$$. We have $$Ne_1=0$$, $$Ne_2=e_1$$, $$Ne_3=e_2$$, and the last condition $$NV_2\subseteq V_3=\mathbb{C}^3$$ is automatic, so using the definition directly we get

$$\Pet_3=\{(V_1\subset V_2)\in \Fl_3\mid NV_1\subseteq V_2\}.$$

As we saw above, from $$\dim_\mathbb{C}\Fl_3=3$$ the single condition cuts the dimension by $$1$$, giving $$\dim\Pet_3=2$$. Since the dimension of the Peterson variety equals $$\rank(\mathfrak{g})$$, by the above description the Peterson variety $$\Pet_3$$ should split into $$2^2=4$$ pieces. On the other hand, thinking of the Bruhat decomposition of $$\GL_3$$, the Bruhat cells are indexed by $$w\in S_3$$, giving $$6$$ cells. That is, among the $$6$$ cells there are two that do not define an affine paving of the Peterson variety; to identify them, consider the coordinate flags

$$E^w_\bullet:\qquad 0\subset \span\{e_{w(1)}\}\subset \span \{e_{w(1)}, e_{w(2)}\}\subset \span\{e_{w(1)}, e_{w(2)},e_{w(3)}\}=\mathbb{C}^3.$$

For this to lie in $$\Pet_3$$ we need $$Ne_{w(1)}\in\span\{e_{w(1)},e_{w(2)}\}$$, i.e.

$$w\in\{e,\,s_1,\,s_2,\,w_0\}=\{123,\,213,\,132,\,321\}$$

and only these four remain. Indeed, writing out the points of the Bruhat cells corresponding to the two missing elements $$231, 312$$ and considering their intersection with $$\Pet_3$$, one easily verifies that it is empty.

The four flags obtained above are the $$2^{n-1}=4$$ coordinate flags corresponding to subsets $$A\subseteq\{\alpha_1,\alpha_2\}$$ of simple roots and the maximal length elements $$w_A$$ of the Weyl groups $$W_A$$ they define, showing that the Peterson variety remembers the combinatorics of the simple roots.

</div>

Meanwhile, the key idea of [Proposition 9](#prop9) was to decompose $$\mathcal{Y}$$ by taking its intersection with the Bruhat decomposition of $$G/B$$. But we already examined in [§Bruhat decomposition, ⁋Theorem 8](/en/math/lie_theory/bruhat_decomposition#thm8) the decomposition via the opposite Borel subgroup, so we can also explore the properties of $$\mathcal{Y}$$ through $$\mathcal{Y}\cap B^-wB/B$$.

The nature of the result is completely different. The pieces are no longer affine spaces; instead, each piece is an affine variety meaningful in its own right. Again there are exactly $$2^{\rank(\mathfrak{g})}$$ nonempty pieces, with the same indexing as the paving. That is, the nonempty pieces are the locally closed subvarieties given for each $$A\subseteq\Delta$$ by the intersection with the $$B^-$$ Bruhat cell of the same longest element $$w_A$$:

$$\mathcal{Y}\cap B^-w_AB/B$$

[Pet]. At this point the subset $$A\subseteq\Delta$$ is in bijection with the standard parabolic subgroup $$B\subseteq P\subseteq G$$ having $$W_A$$ as its Weyl group, so (for a reason we will see shortly) we write this piece as $$\mathcal{Y}_P$$ and obtain a stratification of $$\mathcal{Y}$$:

$$\mathcal{Y}=\bigsqcup_{P\supseteq B}\mathcal{Y}_P.$$

Looking at the two extremes: the stratum for $$P=G$$ ($$A=\Delta$$, $$w_A=w_0$$) is the point $$\{w_0B\}$$, and the stratum for $$P=B$$ ($$A=\emptyset$$, $$w_A=e$$) is the Zariski dense open subset of $$\mathcal{Y}$$ given by the intersection with the opposite big cell:

$$\mathcal{Y}_B=\mathcal{Y}\cap B^-B/B.$$

In general, the dimension of $$\mathcal{Y}_P$$ equals $$\lvert\Delta\setminus A\rvert$$, i.e. the number of simple roots not in $$P$$. Thus the paving cell and the stratification stratum are two pieces attached to the same $$w_A$$, having the same count and both containing the point $$w_AB$$, while their dimensions grow in complementary directions as $$\lvert A\rvert$$ and $$\lvert\Delta\setminus A\rvert$$.

This decomposition has meaning beyond simply replacing $$B$$ by $$B^-$$: it carries information about quantum cohomology. In the following theorem, the *Langlands dual group* $$G^\vee$$ of the Lie group $$G$$ is the dual group obtained by interchanging roots and coroots in the root datum; in this situation let $$\mathcal{Y}^\vee$$ be the Peterson variety constructed following [Definition 8](#def8), and let $$\mathcal{Y}^\vee_P$$ denote the stratum of $$\mathcal{Y}^\vee$$ corresponding to the Langlands dual $$P^\vee$$ of a parabolic subgroup $$P$$ of $$G$$.

<div class="proposition" markdown="1">

<ins id="thm11">**Theorem 11 (Peterson)**</ins> In the Peterson variety of the Langlands dual $$G^\vee$$ of $$G$$, the coordinate ring of the stratum $$\mathcal{Y}^\vee_P$$ corresponding to each standard parabolic subgroup $$P\supseteq B$$ is isomorphic to the small quantum cohomology ring of the partial flag variety $$G/P$$.

$$\mathbb{C}[\mathcal{Y}^\vee_P]\cong QH^\ast(G/P)$$

</div>

This theorem was introduced in Peterson's 1997 MIT lecture; there is no separate publication, but the proof can be found in [lecture notes](https://math.soimeme.org/~arunram/Resources/PetersonGmodBcourse1997.pdf) and elsewhere. However, in the case of the Grassmannian that we have mainly been looking at, $$\GL_n$$ is Langlands self-dual so $$G\cong G^\vee$$ and this duality is not very visible.

Since introducing the flag variety in [§Borel subgroup, ⁋Definition 12](/en/math/lie_theory/borel_subgroup#def12), we have not used the language of algebraic geometry very heavily, but to understand the spirit of this theorem we can no longer postpone it. The key point is the way algebraic geometry interprets a ring $$A$$ as a geometric space $$\Spec A$$ over $$\mathbb{C}$$, with $$A$$ as the ring of functions on that space. In this dictionary, the points of the space $$\Spec A$$ correspond to maximal ideals of $$A$$, and a ring homomorphism $$A\rightarrow B$$ corresponds to a geometric function $$\Spec B\rightarrow \Spec A$$. An important special case is when $$A=\mathbb{C}$$ and $$B=\mathbb{C}$$: first, if $$A=\mathbb{C}$$, then algebraically $$\mathbb{C}\rightarrow B$$ is the structure morphism making the ring $$B$$ a $$\mathbb{C}$$-algebra. In the geometric world, $$\Spec \mathbb{C}$$ is a point, so the function $$\Spec B\rightarrow \Spec A$$ becomes a function to a point. If both $$A,B$$ are $$\mathbb{C}$$-algebras and the following commutative diagram

![If $$A, B$$ are $$\mathbb{C}$$-algebras, the unit gives structure morphisms $$\mathbb{C}\to A$$, $$\mathbb{C}\to B$$, and a ring homomorphism $$\varphi\colon A\to B$$ commuting with these (i.e. fixing $$\mathbb{C}$$) is the condition for $$\varphi$$ to be a $$\mathbb{C}$$-algebra homomorphism.](/assets/images/Math/Lie_Theory/Richardson_Peterson_Variety-1.svg){:style="width:12em" class="invert" .align-center}

exists, then applying $$\operatorname{Spec}$$ to the above triangle reverses all arrows, and $$\operatorname{Spec}\varphi\colon\operatorname{Spec}B\to\operatorname{Spec}A$$ becomes a morphism over the point $$\operatorname{Spec}\mathbb{C}$$.](/assets/images/Math/Lie_Theory/Richardson_Peterson_Variety-2.svg){:style="width:18em" class="invert" .align-center}

On the other hand, when $$B=\mathbb{C}$$, a ring homomorphism $$A\rightarrow \mathbb{C}$$ translates in the geometric world to $$\Spec \mathbb{C}\rightarrow\Spec A$$, i.e. this ring homomorphism is itself a point. Also recall that when $$A$$ is a $$\mathbb{C}$$-algebra, we usually interpreted this ring homomorphism as an evaluation map. Finally, viewing $$B$$ as an $$A$$-algebra via a ring homomorphism $$A\rightarrow B$$ is interpreted as a morphism $$\Spec B\rightarrow\Spec A$$, i.e. a relative space over the base $$\Spec A$$, and an $$A$$-module is viewed as a sheaf over $$\Spec A$$ (an object analogous to a vector bundle). In particular, a free module of rank $$N$$ corresponds to a trivial rank $$N$$ bundle, so the $$\Spec$$ of such an $$A$$-algebra is a finite morphism whose fibers (counting dimension) have $$N$$ points. The most basic case is affine space: the polynomial algebra $$\mathbb{C}[\x_1,\ldots,\x_n]$$ becomes affine $$n$$-space $$\mathbb{A}^n$$ under $$\Spec$$, and more generally $$A[\x_1,\ldots,\x_n]$$ corresponds to a relative affine space over the base $$\Spec A$$.

Now, to return to the interpretation of [Theorem 11](#thm11), let us first add a geometric setup to $$QH^\ast(G/P)$$. For notational convenience, suppose there are $$k$$ quantum parameters and write $$q$$ for this family; then $$QH^\ast(G/P)$$ is (as a module) a free module of rank $$N=\dim_\mathbb{C}H^\ast(G/P)$$ over the polynomial ring $$\mathbb{C}[q]$$ of quantum parameters. Considering the structure morphism $$\mathbb{C}[q]\rightarrow QH^\ast(G/P)$$, geometrically this defines $$\Spec QH^\ast(G/P)\rightarrow \Spec\mathbb{C}[q]$$. Then as we saw above, this is a rank $$N$$ finite morphism from $$\Spec QH^\ast(G/P)$$ to $$\mathbb{A}^k$$.

Then considering an arbitrary generic fiber over a point $$q_0$$ in $$\Spec \mathbb{C}[q]\cong\mathbb{A}^k$$ corresponds exactly to the following diagram:

![The commutative square corresponding to the fiber over $$q=q_0$$. Restricting the character $$\rchi_y$$ of a point $$y$$ to $$\mathbb{C}[q]$$ gives the evaluation $$\operatorname{ev}_{q_0}$$ at $$q_0$$, meaning that $$y$$ lies over $$q_0$$.](/assets/images/Math/Lie_Theory/Richardson_Peterson_Variety-3.svg){:style="width:14em" class="invert" .align-center}

Algebraically this is the following tensor product

$$QH^\ast(G/P)\otimes_{\mathbb{C}[q]}\mathbb{C}[q]/(q-q_0)\cong QH^\ast(G/P)/(q-q_0)$$

and a point of this fiber is again a ring homomorphism $$QH^\ast(G/P)/(q-q_0)\rightarrow \mathbb{C}$$. Similarly, applying the isomorphism of [Theorem 11](#thm11) gives the following commutative diagram:

![The picture of the Peterson isomorphism realizing the spectrum of quantum cohomology as flags. A point $$y$$ of $$\mathcal{Y}^\vee_P$$ (i.e. a flag of $$G^\vee/B^\vee$$) gives an evaluation $$\operatorname{ev}_y$$, which via the Peterson isomorphism $$\Phi\colon a\mapsto f_a$$ lifts to the character $$\rchi_y=\operatorname{ev}_y\circ\Phi$$ (right square, $$\rchi_y(a)=f_a(y)$$), and restricting to $$\mathbb{C}[q]$$ gives the evaluation at the quantum parameter value $$q_0$$ of $$y$$ (left square). That is, a fiber point over $$q_0$$ = a character over $$q_0$$ = a flag.](/assets/images/Math/Lie_Theory/Richardson_Peterson_Variety-4.svg){:style="width:24em" class="invert" .align-center}

and at this point the last vertical map $$\ev_y$$ defines a point on $$\mathcal{Y}^\vee_P$$. Let us now decode what this point contains, following the dictionary. First, $$QH^\ast(G/P)/(q-q_0)$$ is a finite-dimensional algebra over $$\mathbb{C}$$, and on it each cohomology class $$a$$ gives the operator $$a\qtimes-$$ of quantum multiplication by $$a$$. For the point $$y$$ obtained above, the corresponding character $$\rchi_y\colon QH^\ast(G/P)/(q-q_0)\to\mathbb{C}$$ assigns to each $$a$$ a scalar $$\rchi_y(a)$$, and since it is a ring homomorphism, it satisfies $$\rchi_y(a\qtimes b)=\rchi_y(a)\,\rchi_y(b)$$ and $$\rchi_y(1)=1$$. This means that $$\rchi_y(a)$$ is an eigenvalue of the operator $$a\qtimes-$$, and these eigenvalues are assigned simultaneously without contradiction with the quantum product. In other words, a point of the fiber is a way to consistently assign a simultaneous eigenvalue tuple to all quantum multiplication operators at a generic $$q_0$$.

And [Theorem 11](#thm11) tells us where these simultaneous eigenvalues live. Under the isomorphism $$\mathbb{C}[\mathcal{Y}^\vee_P]\cong QH^\ast(G/P)$$, each class $$a$$ corresponds to a regular function $$f_a$$ on $$\mathcal{Y}^\vee_P$$, so in the language of the dictionary the above character $$\rchi_y$$ is nothing but the evaluation $$\rchi_y=\ev_y$$ at the flag $$y$$, and thus $$\rchi_y(a)=f_a(y)$$. That is, the simultaneous eigenvalue $$\rchi_y(a)$$ is not an abstract floating number, but the value of the coordinate function $$f_a$$ at a concrete flag $$y$$ inside $$G^\vee/B^\vee$$. In this way, the spectrum $$\Spec QH^\ast(G/P)=\mathcal{Y}^\vee_P$$ of the abstract algebra $$QH^\ast(G/P)$$ sits as actual points inside the flag variety $$G^\vee/B^\vee$$, and each point (i.e. each flag) hands us a simultaneous eigenvalue tuple for quantum multiplication.

In the smallest Grassmannian $$\mathbb{P}^1=\Gr(1,2)$$ we can see all of this by hand. For $$n=2$$ the Peterson condition $$NV_1\subseteq V_2=\mathbb{C}^2$$ is vacuous, so $$\mathcal{Y}=\Fl_2=\mathbb{P}^1$$ is the whole space, and the stratum $$\mathcal{Y}_B$$ is the intersection with the opposite big cell, $$\mathbb{P}^1\setminus\{w_0B\}\cong\mathbb{A}^1$$. On the other hand $$QH^\ast(\mathbb{P}^1)=\mathbb{C}[\sigma,q]/(\sigma^2-q)\cong\mathbb{C}[\sigma]$$ is also a polynomial ring in one variable, consistent with the theorem's isomorphism, and under this isomorphism the quantum parameter is realized as the square of the affine coordinate, $$q=\sigma^2$$. The fiber over a generic $$q_0$$ consists of the two points $$\sigma=\pm\sqrt{q_0}$$, i.e. $$\binom{2}{1}=2$$ points, and the fiber over $$q_0=0$$ is a double point of length $$2$$ sitting over the single point $$B/B$$, whose coordinate ring is classical cohomology $$\mathbb{C}[\sigma]/(\sigma^2)=H^\ast(\mathbb{P}^1)$$. That is, the degeneration from quantum to classical happens geometrically within the stratum.

In general $$\Gr(k,n)$$ as well, the fiber over a generic $$q_0$$ consists of $$\binom{n}{k}$$ distinct points. These finitely many points have another explicit model: they are realized as critical points of a certain Laurent polynomial, a superpotential, which is one of the contents of mirror symmetry, and constructing this correspondence for general $$G/P$$ remains an actively studied topic (see [mirror symmetry](/en/mirror_symmetry/)).

<div class="remark" markdown="1">

<ins id="rmk12">**Remark 12**</ins> The affine paving of [Proposition 9](#prop9) is also the starting point for cohomology computations. By the paving, the cohomology of $$\mathcal{Y}$$ is a free module with a basis indexed by the cells, and vanishes in odd degrees. That is, the affine paving argument for flag varieties from [§Bruhat decomposition, ⁋Proposition 17](/en/math/lie_theory/bruhat_decomposition#prop17) works for Peterson varieties in exactly the same way, and Insko–Tymoczko [IT] developed the intersection theory of Peterson varieties on this basis.

</div>

---

**References**

**[KL80]** D. Kazhdan, G. Lusztig, *Schubert varieties and Poincaré duality*, Geometry of the Laplace operator, Proc. Sympos. Pure Math. **36**, AMS, 1980.

**[Deo85]** V. V. Deodhar, *On some geometric aspects of Bruhat orderings. I. A finer decomposition of Bruhat cells*, Invent. Math. **79** (1985), 499--511.

**[Ric92]** R. W. Richardson, *Intersections of double cosets in algebraic groups*, Indag. Math. **3** (1992), 69--77.

**[Bri]** M. Brion, *Lectures on the geometry of flag varieties*, in *Topics in cohomological studies of algebraic varieties*, Trends Math., Birkhäuser, 2005, 33--85.

**[Kos]** B. Kostant, *The principal three-dimensional subgroup and the Betti numbers of a complex simple Lie group*, Amer. J. Math. **81** (1959), 973--1032.

**[Kos63]** B. Kostant, *Lie group representations on polynomial rings*, Amer. J. Math. **85** (1963), 327--404.

**[Kos96]** B. Kostant, *Flag manifold quantum cohomology, the Toda lattice, and the representation with highest weight $$\rho$$*, Selecta Math. (N.S.) **2** (1996), 43--91.

**[LS]** T. Lam, M. Shimozono, *Quantum cohomology of $$G/P$$ and homology of affine Grassmannian*, Acta Math. **204** (2010), 49--90.

**[Pet]** D. Peterson, Lecture notes, Massachusetts Institute of Technology, Spring 1997 (unpublished).

**[Tym]** J. S. Tymoczko, *Paving Hessenberg varieties by affines*, Selecta Math. (N.S.) **13** (2007), 353--367.

**[Pre]** M. Precup, *Affine pavings of Hessenberg varieties for semisimple groups*, Selecta Math. (N.S.) **19** (2013), 903--922.

**[IT]** E. Insko, J. Tymoczko, *Affine pavings of regular nilpotent Hessenberg varieties and intersection theory of the Peterson variety*, J. Combin. Theory Ser. A **187** (2022), 105572.

---
[^1]: Note that the $$\mathfrak{h}$$ denoting the Cartan subalgebra, which comes from [§Root system, ⁋Definition 4](/en/math/lie_theory/root_systems#def4), is <em>unrelated</em> to the $$H$$ in our discussion.
