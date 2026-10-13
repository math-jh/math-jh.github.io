---
title: "Richardson Varieties and Peterson Varieties"
description: "This post covers Richardson varieties, defined as intersections of Schubert and opposite Schubert varieties, and Peterson varieties, cut out by regular nilpotent elements. It examines the definitions and dimensions of the two subvarieties, their roles in intersection theory, concrete appearances in Grassmannians and type A, and stratification by Bruhat cells."
excerpt: "Richardson varieties and Peterson varieties: definitions, dimensions, intersection theory, and stratification"

categories: [Math / Lie Theory]
permalink: /en/math/lie_theory/richardson_peterson_variety
sidebar:
    nav: "Lie_theory-en"

date: 2026-06-09
weight: 8
translated_at: 2026-06-26T19:00:01+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-13T11:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
In [§Bruhat Decomposition](/en/math/lie_theory/bruhat_decomposition){: data-lid="4vqmm" }, we saw that the partial flag variety $G/P$ decomposes into Bruhat cells, and that the geometry of $G/P$ is contained in the combinatorics of the Weyl group through the Schubert varieties, the closures of each cell. In this post, we discuss two kinds of subvarieties that naturally sit on this decomposition. One is the *Richardson variety*, obtained as the intersection of two opposite Bruhat decompositions, and the other is the *Peterson variety*, cut out by a single regular nilpotent element.

## Richardson variety

As in [§Bruhat Decomposition](/en/math/lie_theory/bruhat_decomposition){: data-lid="iy70d" }, we fix a connected reductive algebraic group $G$ over the field $\mathbb{C}$, a Borel subgroup $B$, and a parabolic subgroup $P$ containing $B$. Taking also the opposite Borel subgroup $B^-$ ($B\cap B^-=T$), we obtain the cell structures in both directions introduced in [§Bruhat Decomposition, ⁋Definition 16](/en/math/lie_theory/bruhat_decomposition#def16){: data-lid="2l18y" }

$$X_w^\circ=BwP/P,\qquad X^w_\circ=B^-wP/P\qquad(w\in W^P)$$

and their Zariski closures, the Schubert variety $X_w=\overline{X_w^\circ}$ and the opposite Schubert variety $X^w=\overline{X^w_\circ}$. The two cells are $X_w^\circ\cong\mathbb{A}^{\ell(w)}$ and $X^w_\circ\cong\mathbb{A}^{\dim(G/P)-\ell(w)}$, respectively, and a Richardson variety is the intersection of cells from these two directions.

::: Definition 1
For $u,w\in W^P$, the intersection of a Schubert variety and an opposite Schubert variety

$$R_{u,w}=X_w\cap X^u$$

is called a *Richardson variety*, and the intersection of the two open cells

$$\mathring{R}_{u,w}=X_w^\circ\cap X^u_\circ$$

is called an *open Richardson variety*.
:::

By definition, $R_{u,w}$ is a closed subvariety of $G/P$, and $\mathring{R}_{u,w}$ is a Zariski open subset of it. This intersection already appeared in the work of Kazhdan–Lusztig [KL80] and Deodhar [Deo85], and its general geometric properties were later studied by Richardson [Ric92].

The usefulness of this definition can be seen in the Grassmannian $\Gr(k,n)$ (or more generally in a partial flag variety). Fixing a reference flag $E_\bullet\colon E_1\subseteq E_2\subseteq\cdots\subseteq E_n=\mathbb{C}^n$, recall that each Schubert cell is determined by the way a $k$-dimensional subspace $V$ in it meets this flag, namely by the positions where $\dim(V\cap E_j)$ jumps as $j$ increases. Computing the intersection of two Schubert cells inside the Grassmannian amounts to finding the incidence conditions that they satisfy simultaneously. However, if the two Schubert cells are defined with respect to the same reference flag, the two conditions are not independent, so the intersection fails to have the expected dimension; one must instead choose reference flags that are in generic position with respect to each other.

The example in which this is most easily computed is precisely the *opposite flag* $\tilde{E}_j=\span\{e_n,\ldots,e_{n-j+1}\}$, which reads the given flag $E_i=\span\{e_1,\ldots,e_i\}$ in reverse. The two flags chosen this way satisfy the transversality condition

$$\dim(E_i\cap\tilde{E}_j)=\max(0,i+j-n)$$

for all $i,j$. In other words, whichever pair of pieces from the two flags is taken, their intersection is as small as possible. A Richardson variety is precisely viewing the intersection of two Schubert cells by simultaneously imposing Schubert conditions with respect to two reference flags in generic position like this, and the fact that in the definition $X_w$ is the condition with respect to the standard flag fixed by $B$ and $X^u$ is the condition with respect to the opposite flag fixed by $B^-$ corresponds precisely to this transversality.

::: Proposition 2 (Richardson [Ric92])
The open Richardson variety $\mathring{R}_{u,w}$ is nonempty if and only if $u\leq w$ in the Bruhat order. When this condition holds, $\mathring{R}_{u,w}$ is a smooth irreducible affine variety of dimension $\ell(w)-\ell(u)$, and $R_{u,w}$ is its Zariski closure.
:::

Intuitively, recall that the Schubert variety $X_w$ grows from the single point $X_e=\{eP\}$ starting from lower dimensions, while the opposite Schubert variety $X^u$ descends from the whole of $G/P$ starting from higher dimensions. Concretely, $\dim X_w=\ell(w)$ and $\dim X^u=\dim(G/P)-\ell(u)$, so in order for the expected dimension of the intersection to be nonnegative, first the sum of their dimensions must be at least $\dim(G/P)$, that is, $\ell(u)\leq\ell(w)$, in which case this expected dimension is the proposition's

$$\ell(w)+\dim (G/P)-\ell(u)-\dim (G/P)=\ell(w)-\ell(u)$$

.

However, matching dimensions alone do not allow us to conclude that the intersection is nonempty. For instance, consider the incomparable pair $u=1423$, $w=2314$ from [§Bruhat Decomposition, ⁋Example 18](/en/math/lie_theory/bruhat_decomposition#ex18){: data-lid="jwdm4" }: although their lengths are equal so that the expected dimension is $0$, their intersection is not a set of points, but the empty set. Let us see directly what happens in $\Gr(2,4)$. A point of $X_{2314}$ satisfies the rank condition $\dim(V\cap E_3)\geq2$, that is, $V\subseteq E_3$. On the other hand, every point of the opposite cell $X^{1423}_\circ=B^-\cdot\span\{e_1,e_4\}$ contains $e_4$ (lower triangular matrices fix $e_4$ up to a scalar multiple), and since $e_4\in V$ is a closed condition, it is preserved in the closure $X^{1423}$ as well. Because $e_4\notin E_3$, the two requirements are incompatible, and the two varieties miss each other despite having sufficient dimension.

This phenomenon is due to the fact that $X_w$ and $X^u$ are not arbitrary subvarieties in general position, but are both subvarieties in special positions that are invariant under the action of the maximal torus $T$. Due to this property, their intersection $X_w\cap X^u$ is also a closed $T$-stable subvariety, and it is known that any nonempty closed $T$-stable subvariety contains a $T$-fixed point (see the Borel fixed point theorem, [Bri]). However, the only $T$-fixed points of $G/P$ are the coordinate points $vP$ ($v\in W^P$) ([§Bruhat Decomposition, ⁋Proposition 19](/en/math/lie_theory/bruhat_decomposition#prop19){: data-lid="iddu3" }). Meanwhile, $vP\in X_w$ is equivalent to $v\leq w$ (by [§Bruhat Decomposition, ⁋Proposition 17](/en/math/lie_theory/bruhat_decomposition#prop17){: data-lid="ezved" }), and symmetrically $vP\in X^u$ is equivalent to $u\leq v$. Therefore

$$X_w\cap X^u\neq\emptyset\iff\text{there exists }v\in W^P\text{ with }u\leq v\leq w\iff u\leq w$$

. In the example above, the jump set condition $\{1,4\}\leq\{v(1),v(2)\}\leq\{2,3\}$ requires $4\leq v(2)\leq3$, so no such $v$ exists; conversely, if $u\leq w$, one can choose $v=u$, so that the fixed point $uP$ is already a point of $R_{u,w}$. This is the precise geometric content of the condition $u\leq w$ in [Proposition 2](#prop2){: data-lid="h05xg" }.

It is then natural to expect the following proposition.

::: Proposition 3
For $u,w\in W^P$, in the cohomology ring $H^\ast(G/P)$,

$$[X_w]\cdot[X^u]=[R_{u,w}]$$

holds (where if $u\not\leq w$, then $R_{u,w}=\emptyset$ and both sides are $0$). In particular, when $\ell(u)=\ell(w)$,

$$\int_{G/P}[X_w]\cdot[X^u]=\delta_{u,w}$$

so the opposite Schubert classes $\{[X^u]\}_{u\in W^P}$ form the Poincaré dual basis to the Schubert classes $\{[X_w]\}_{w\in W^P}$.
:::
::: Proof
$X_w$ and $X^u$ meet transversally in the generic position given by $B$ and $B^-$, so their intersection class equals the product of the two classes. This gives $[X_w]\cdot[X^u]=[R_{u,w}]$ (see [Bri]). When $\ell(u)=\ell(w)$, the dimension of $R_{u,w}$ is $\ell(w)-\ell(u)=0$, and by [Proposition 2](#prop2){: data-lid="6k8aa" }, if $u=w$ it is a single reduced point, while if $u\neq w$ (since $u\leq w$ fails) it is empty. Hence the degree of this 0-dimensional class, namely $\int_{G/P}[X_w]\cdot[X^u]$, is $\delta_{u,w}$.
:::

[Proposition 3](#prop3){: data-lid="p3064" } reduces the structure constants for multiplication in the Schubert basis to the degrees of Richardson varieties. Integrating the product of three classes $[X_w]\cdot[X^u]\cdot[X_v]$ gives the intersection number of three Schubert varieties in generic position, which is precisely the structure constant; in the case of the Grassmannian this becomes the Littlewood–Richardson coefficient, and from this classical Schubert calculus unfolds.

Again, the most tangible case is the Grassmannian $G/P=\Gr(k,n)\cong\GL_n(\mathbb{C})/P_k$. Here $W=S_n$, $W_{P_k}=S_k\times S_{n-k}$, and the minimal length coset representatives $W^{P_k}$ are the $(k,n-k)$-shuffles from [§Bruhat Decomposition, ⁋Proposition 14](/en/math/lie_theory/bruhat_decomposition#prop14){: data-lid="uk8zo" }. The Schubert variety $X_w$ is cut out by rank conditions of the form $\dim(V\cap E_{w(a)})\geq a$ with respect to the standard flag $E_\bullet$, and the opposite Schubert variety $X^u$ is cut out by symmetric rank conditions with respect to the opposite flag $\tilde{E}_\bullet$ ($\tilde{E}_j=\span\{e_n,\ldots,e_{n-j+1}\}$). The Richardson variety is obtained by imposing both conditions simultaneously.

::: Example 4
In $\Gr(2,4)$, take $u=1324$ and $w=2413$. In the jump set order from [§Bruhat Decomposition, ⁋Example 18](/en/math/lie_theory/bruhat_decomposition#ex18){: data-lid="cdqfr" }, we have $1324\leftrightarrow\{1,3\}$ and $2413\leftrightarrow\{2,4\}$, and since $1\leq2$ and $3\leq4$ componentwise, we have $u\leq w$, with $\ell(2413)-\ell(1324)=3-1=2$. The two Schubert conditions are, respectively,

$$X_{2413}=\{V\mid\dim(V\cap E_2)\geq1\},\qquad X^{1324}=\{V\mid\dim(V\cap\tilde{E}_2)\geq1\}$$

where $E_2=\span\{e_1,e_2\}$ and $\tilde{E}_2=\span\{e_3,e_4\}$ are two complementary planes. Thus

$$R_{1324,2413}=\{V\in\Gr(2,4)\mid V\cap E_2\neq0,\ V\cap\tilde{E}_2\neq0\}$$

is the collection of planes spanned by choosing a line in $E_2$ and a line in $\tilde{E}_2$. Since $E_2\cap\tilde{E}_2=0$, the two lines are always independent, and the correspondence $([p],[q])\mapsto\langle p,q\rangle$ gives an isomorphism

$$R_{1324,2413}\cong\mathbb{P}(E_2)\times\mathbb{P}(\tilde{E}_2)\cong\mathbb{P}^1\times\mathbb{P}^1$$

This is a variety of dimension $2$, matching exactly the dimension from [Proposition 2](#prop2){: data-lid="x2djg" }. Its open part is coordinatized by the matrices

$$V=\operatorname{rowspan}\begin{pmatrix}1&s&0&0\\0&0&1&t\end{pmatrix}\qquad(s,t)\in\mathbb{A}^2$$

where, when $s,t\neq0$, the jump set of the above matrix is $\{2,4\}$, so $V\in X_{2413}^\circ$, and since the second row lies in $\tilde{E}_2$, we have $V\in X^{1324}_\circ$. That is, $\mathring{R}_{1324,2413}$ is an open subset of this $(s,t)$-plane, and its affine dimension $2$ is immediately visible from the coordinates.
:::

## Peterson variety

We now shift our perspective somewhat to define a new variety. This begins first with a new way of looking at the flag variety $G/B$. Recall that $G$ acts on its own Borel subalgebras by the following conjugation action

$$g\cdot\mathfrak{b}'=\Ad(g)\mathfrak{b}'$$

([§Borel Subgroups, ⁋Proposition 10](/en/math/lie_theory/borel_subgroup#prop10){: data-lid="3nwpn" }). At this point, since any two Borel subalgebras are conjugate, this action is transitive, and the stabilizer of $\mathfrak{b}$ is its normalizer $N_G(\mathfrak{b})=B$. Therefore, $gB\mapsto\Ad(g)\mathfrak{b}$ obtained from the orbit-stabilizer theorem gives a one-to-one correspondence between $G/B$ and the set of Borel subalgebras. That is, $G/B$ can be thought of as the variety of Borel subalgebras of $G$.

Now recall again that $G/B$ is the flag variety, and that $gB$, as a point of this variety, determines a flag. That is, the above bijection attaches to each flag of $G/B$ the corresponding Borel subalgebra $\Ad(g)\mathfrak{b}$. But this can be generalized a bit further. If we choose, containing $\mathfrak{b}$, an $\ad(\mathfrak{b})$-stable subspace $H\subseteq\mathfrak{g}$, then since $H$ is $B$-stable, $\Ad(g)H$ also depends only on the coset $gB$. That is, to each flag we can assign a subspace $\Ad(g)H$.

From this perspective, considering which of these subspaces a fixed element $X\in \mathfrak{g}$ belongs to is interpreted on the flag variety as an incidence condition of an appropriate kind. Indeed, since this condition $\Ad(g^{-1})X\in H$ is a polynomial condition on each entry of $g$, the set of $gB$ satisfying it actually forms a closed subvariety of $G/B$.

Our object of interest is this closed variety, which naturally depends on the choices of $X$ and $H$. For instance, if $X=0$, the above condition will always hold, so this is the entire flag variety $G/B$. What allows us to gauge the dependence on $X$ is the centralizer of $X$. Consider an element centralizing $X$ in $G$, say $z$. Then, when $z$ acts on $G/B$ by $gB\mapsto zgB$, the left-hand side of the incidence condition becomes

$$\Ad((zg)^{-1})X=\Ad(g^{-1})X$$

That is, this incidence condition is invariant under left translation by $z$, and from this a group action of the centralizer $C_G(X)$ is defined on the closed variety under consideration. That is, this closed variety is a union of $C_G(X)$-orbits, and thus intuitively we can expect that the larger the centralizer, the larger the closed subvariety of $G/B$ cut out in this way. For example, the case $X=0$ was the extreme case where the centralizer is all of $G$. However, since it is known that the dimension of the centralizer cannot drop below $\rank(\mathfrak{g})$ for any choice of $X\in\mathfrak{g}$ ([Kos63]), the opposite extreme consists of the elements achieving this minimum.

::: Definition 5
A nilpotent element $X\in\mathfrak{g}$ is *regular* if the dimension of its centralizer $\mathfrak{z}_{\mathfrak{g}}(X)=\{Z\in\mathfrak{g}\mid[Z,X]=0\}$ equals $\rank(\mathfrak{g})$.
:::

Regular nilpotents always exist by a standard construction. This is because for each simple root $\alpha_i$, choosing $0\neq e_i\in\mathfrak{g}_{\alpha_i}$ and setting $e=\sum_i e_i$ yields a regular nilpotent.

In the familiar type $A_{n-1}$, this provides a familiar, concrete example. The above construction gives the principal nilpotent with all superdiagonal entries equal to $1$:

$$N=\sum_{i=1}^{n-1}E_{i,i+1}=\begin{pmatrix}0&1&&\\&0&\ddots&\\&&\ddots&1\\&&&0\end{pmatrix}$$

Solving $[Z,N]=0$ entrywise, one finds that the centralizer consists of polynomials in $N$:

$$\mathfrak{z}_{\mathfrak{sl}_n}(N)=\span\{N,N^2,\ldots,N^{n-1}\}$$

and since the dimension of this space is exactly $n-1=\rank(\mathfrak{sl}_n)$, $N$ is regular. From the viewpoint of Jordan canonical form, $N$ is a nilpotent with a single Jordan block, corresponding to the partition $(n)$. The more Jordan blocks there are, the larger the centralizer becomes, so a regular nilpotent can be thought of as the conjugacy class with the smallest centralizer among nilpotent elements.

In general type, the fact that $e=\sum_i e_i$ is regular, that all regular nilpotents are conjugate to each other under the adjoint action of $G$, and that their centralizer is always abelian, are classical results of Kostant [Kos].

Now let us add the dependence on $H$ to this closed subvariety, which we had been considering with $X$ fixed. For convenience, let us first give it a name.

::: Definition 6
For $X\in\mathfrak{g}$ and a subspace containing $\mathfrak{b}$ that is $\ad(\mathfrak{b})$-stable, $H\subseteq\mathfrak{g}$ (i.e. $[\mathfrak{b},H]\subseteq H$), the *Hessenberg variety* is defined by

$$\mathcal{B}(X,H)=\{gB\in G/B\mid\Ad(g^{-1})X\in H\}$$

as a closed subvariety of $G/B$.
:::

As we saw above, $X$ influences the size of the variety through its centralizer, and the same holds for the subspace $H$. As two extreme situations, in the case $H=\mathfrak{g}$, the condition $\Ad(g^{-1})X\in\mathfrak{g}$ holds trivially and the Hessenberg variety is all of $G/B$. At the opposite extreme $H=\mathfrak{b}$, the condition $\Ad(g^{-1})X\in\mathfrak{b}$ says that the Borel subalgebra $\Ad(g)\mathfrak{b}$ contains $X$, and if $X$ is nilpotent, we call this the *Springer fiber* of $X$.

The Peterson variety we will define can be thought of as the closed subvariety obtained by imposing the strongest possible conditions using $X$ and $H$. For $X$, the argument before [Definition 6](#def6){: data-lid="ne0op" } shows that the regular nilpotent condition imposes the strongest constraint, in which case $X$ belongs to exactly one Borel subalgebra and the Springer fiber $\mathcal{B}(X, \mathfrak{b})$ collapses to a single point. Thus we loosen the condition on $H$ slightly here to define the Peterson variety.

In which direction we can enlarge $H$ becomes clear if, in type $A$, we directly work out the condition of [Definition 6](#def6){: data-lid="2652j" } in coordinates.

::: Example 7
Let us return to type $A_{n-1}$ examined above. In this case, $G=\GL_n(\mathbb{C})$, $\mathfrak{b}$ is the space of upper triangular matrices, and the Cartan subalgebra of $\gl_n$ is the space of diagonal matrices $\mathfrak{h}$.[^1]

Now, since $H$ is $\ad(\mathfrak{b})$-stable, it must also be $\ad(\mathfrak{h})$-stable. Computing the bracket of an arbitrary $Y\in H$ with an arbitrary diagonal matrix $\diag(t_1,\ldots, t_n)$, we have

$$\ad(\diag(t_1,\ldots, t_n))Y=[\diag(t_1,\ldots, t_n), Y]=((t_j-t_k)Y_{jk})_{1\leq j,k\leq n}$$

and for $\ad(\mathfrak{h})$-stability to hold, this must again belong to $H$.

Meanwhile, the above calculation shows in particular that when $\ad(\diag(t_1,\ldots, t_n))$ is viewed as a linear operator on $\gl_n$, this linear operator has all the basis elements of $\gl_n$, $E_{jk}$, as eigenvectors. Now, if we choose $t$ generically, the eigenvalues $t_j-t_k$ ($j\neq k$) are all distinct from $0$ and from each other, and therefore a subspace $H$ invariant under this operator decomposes into intersections with each eigenspace, so that the weight decomposition

$$H=(H\cap \mathfrak{h})\oplus\bigoplus_{j\neq k}(H\cap \mathbb{C}E_{jk})$$

holds. Therefore, $H$ is determined by the positions of the matrix entries that it contains. That is, $H$ is the span of the entire diagonal ($\mathfrak{h}\subseteq\mathfrak{b}\subseteq H$) and the elementary matrices $E_{jk}$ that it contains. Now, to see concretely which entries can enter $H$, we compute the brackets with the upper triangular directions: for $l\leq j$ and $k\leq m$,

$$[E_{lj},E_{jk}]=E_{lk}-\delta_{kl}E_{jj},\qquad[E_{jk},E_{km}]=E_{jm}-\delta_{jm}E_{kk}$$

and since the $\delta$ terms are in $\mathfrak{h}\subseteq H$ anyway, if $H$ contains the position $(j,k)$, then it must also contain all positions $(l,k)$ ($l\leq j$) above it in the same column and all positions $(j,m)$ ($m\geq k$) to the right in the same row. Thus each column is filled from the top without gaps, and the filled depth does not decrease as one moves to the right columns. Therefore, writing $h(k)$ for the depth of the $k$-th column, $H$ is the staircase determined by a nondecreasing function satisfying $h(i)\geq i$, $h\colon\{1,\ldots,n\}\rightarrow\{1,\ldots,n\}$ (*Hessenberg function*):

$$H_h=\{Y\in\mathfrak{gl}_n\mid YE_i\subseteq E_{h(i)}\ \forall i\}=\{Y\mid Y_{jk}=0\ \text{whenever $j>h(k)$}\}$$

and the converse is also easily verified. For example, for $n=4$, the two staircases

$$\mathfrak{b}=H_{(1,2,3,4)}=\begin{pmatrix}\ast&\ast&\ast&\ast\\0&\ast&\ast&\ast\\0&0&\ast&\ast\\0&0&0&\ast\end{pmatrix},\qquad H_{(2,3,4,4)}=\begin{pmatrix}\ast&\ast&\ast&\ast\\\ast&\ast&\ast&\ast\\0&\ast&\ast&\ast\\0&0&\ast&\ast\end{pmatrix}$$

are the cases of $h(i)=i$ and $h(i)=\min(i+1,n)$, respectively.

Now returning to the language of flag varieties, if we let the flag corresponding to a coset $gB$ be $V_\bullet=g\cdot E_\bullet$ (that is, $V_i=\span\{ge_1,\ldots,ge_i\}$), then for any $X\in\mathfrak{gl}_n$,

$$\Ad(g^{-1})X\in H_h\iff g^{-1}Xg\in H_h\iff XgE_i\subseteq gE_{h(i)}\iff XV_i\subseteq V_{h(i)}$$

holds. That is, the Hessenberg variety of type $A$ is the variety of flags cut out by the condition that $X$ allows the flag to slide down at each step only as much as $h$ permits.
:::

The picture in [Example 7](#ex7){: data-lid="ozxbq" } holds in the general case as well. In this case, as above, the positions that the staircase fills in addition to $\mathfrak{b}$ are below the diagonal, that is, in the *negative* root directions. Indeed, since $\mathfrak{b}=\mathfrak{h}\oplus\bigoplus_{\alpha>0}\mathfrak{g}_\alpha$ already contains all positive root directions, enlarging $H$ beyond $\mathfrak{b}$ can only mean adding negative root directions. However, an additional simple condition is forced by $\ad(\mathfrak{b})$-stability: in fact, while the direction of a non-simple positive root $\alpha=\beta+\gamma$ drags in shallower positions along with it via $[\mathfrak{g}_\beta,\mathfrak{g}_{-\alpha}]=\mathfrak{g}_{-\gamma}$, for a negative simple root direction, $\mathfrak{b}\oplus\mathfrak{g}_{-\alpha_i}$ is stable by itself. That is, the minimal units of expansion extending $\mathfrak{b}$ by one cell at a time are precisely the $\mathfrak{g}_{-\alpha_i}$, and in type $A$ these are the subdiagonal positions in the picture above. Then, adding these directions to $\mathfrak{b}$ produces the $H$ of the Peterson variety.

::: Definition 8
The *Peterson variety* $\mathcal{Y}$ is defined as the closed subvariety of $G/B$

$$\mathcal{Y}=\{gB\in G/B\mid\Ad(g^{-1})e\in H\}$$

where $e=\sum_i e_i$ is a regular nilpotent element, $H=\mathfrak{b}\oplus\bigoplus_i\mathbb{C}f_i$, and $f_i\in\mathfrak{g}_{-\alpha_i}$ are root vectors for the simple negative roots.
:::

This definition appears to depend on several choices, but is in fact essentially unique. This is because the choice of $f_i$, since $\mathbb{C}f_i=\mathfrak{g}_{-\alpha_i}$ is $1$-dimensional, does not change $H$, and replacing $e$ with another regular nilpotent merely translates $\mathcal{Y}$ inside $G/B$ (by the conjugacy in the discussion immediately following [Definition 5](#def5){: data-lid="mcty8" }).

As we saw above, the degrees of freedom that $H$ added to $\mathfrak{b}$ are one for each simple root, totaling $\rank(\mathfrak{g})$. Since $H=\mathfrak{b}$ gave a point (the discussion immediately following [Definition 6](#def6){: data-lid="37qud" }), we can expect the dimension of the Peterson variety to grow from a point by that amount. That this is indeed the case is the content of the following proposition.

::: Proposition 9 (Tymoczko [Tym], Precup [Pre], Insko–Tymoczko [IT])
The Peterson variety $\mathcal{Y}$ forms an affine paving structure via its intersection with the Bruhat decomposition. That is, each $\mathcal{Y}\cap BwB/B$ is isomorphic to an affine space, and $\mathcal{Y}$ is their disjoint union. In particular, under this structure the dimension of the largest piece is $\rank(\mathfrak{g})$, so the dimension of $\mathcal{Y}$ also equals $\rank (\mathfrak{g})$.
:::

We omit the proof of this proposition, but the asserted affine paving structure itself is worth remembering. The key point is that this affine paving is indexed by subsets $\mathcal{P}(\Delta)$ of the simple roots: for instance, in the case of the subset containing no simple root directions, that is, the empty set, no directions are added to $\mathfrak{b}$, so by the argument following [Definition 6](#def6){: data-lid="l4yid" } the corresponding affine space is a point. The affine spaces above it are those determined by subsets of $\Delta$, and this is not merely an analogy, but their relative positions are also actually determined by subsets of $\Delta$.

More precisely, the piece corresponding to $A\subseteq\Delta$ is, with the simple roots corresponding to $A$ defining reflections that generate the subgroup $W_A$ of the Weyl group, the intersection with the Bruhat cell defined by $W_A$'s longest element $w_A$:

$$\mathcal{Y}\cap Bw_AB/B\cong \mathbb{A}^{\lvert A\rvert}$$

This is the piece in which, among the degrees of freedom that $H$ added to $\mathfrak{b}$, precisely those in the $A$ directions are activated. Furthermore, under this indexing the closure relations among the pieces replicate the Boolean lattice of subsets of $\Delta$ exactly. That is,

$$\overline{\mathcal{Y}\cap Bw_AB/B}=\bigsqcup_{A'\subseteq A}\bigl(\mathcal{Y}\cap Bw_{A'}B/B\bigr)$$

holds. In fact, this closure coincides with the intermediate Hessenberg variety obtained by enlarging $H$ only in the $A$ directions, $\mathcal{B}(e,\mathfrak{b}\oplus\bigoplus_{i\in A}\mathbb{C}f_i)$, and furthermore is isomorphic to the Peterson variety of the Levi subgroup generated by $A$ ([IT]). That is, the Peterson variety has a structure in which smaller Peterson varieties are nested in subset order, and from the point $B/B$ ($A=\emptyset$) using no degrees of freedom to the largest piece ($A=\Delta$) which is the intersection with the big Bruhat cell, all relative positions in between are governed by the combinatorics of the simple roots.

::: Example 10
Let us examine this structure through an example in type $A$ discussed earlier. As in [Example 7](#ex7){: data-lid="m6kqi" }, if we choose the Hessenberg function $h(i)=\min(i+1, n)$, then $H$ is the collection of matrices allowed to descend exactly one entry below the diagonal, and from the last equivalence in that example we know that the Peterson variety is given inside the complete flag variety $\Fl_n=\GL_n(\mathbb{C})/B$ by

$$\Pet_n=\{V_\bullet\mid NV_i\subseteq V_{i+1},\ i=1,\ldots,n-1\}$$

Its dimension is

$$\sum_{j=1}^n\bigl(h(j)-j\bigr)=n-1$$

which equals $\rank(\mathfrak{sl}_n)$, confirming [Proposition 9](#prop9){: data-lid="k6miq" } again.

Now, to see each cell, let us look more concretely at the case $n=3$. Since $Ne_1=0$, $Ne_2=e_1$, $Ne_3=e_2$ and the last condition $NV_2\subseteq V_3=\mathbb{C}^3$ is automatic, using the above definition directly gives

$$\Pet_3=\{(V_1\subseteq V_2)\in \Fl_3\mid NV_1\subseteq V_2\}$$

Then, as examined above, from $\dim_\mathbb{C}\Fl_3=3$, a single condition reduces the dimension by $1$, giving $\dim\Pet_3=2$. Since the dimension of the Peterson variety equals $\rank(\mathfrak{g})$, according to the description above, the Peterson variety $\Pet_3$ should split into $2^2=4$ pieces. On the other hand, considering the Bruhat decomposition of $\GL_3$, the Bruhat cells are indexed by $w\in S_3$, giving $6$ cells. That is, among the $6$ cells, there are two that do not define an affine paving of the Peterson variety; to identify them, if we consider the coordinate flag

$$E^w_\bullet:\qquad 0\subseteq \span\{e_{w(1)}\}\subseteq \span \{e_{w(1)}, e_{w(2)}\}\subseteq \span\{e_{w(1)}, e_{w(2)},e_{w(3)}\}=\mathbb{C}^3$$

for this to belong to $\Pet_3$, we must have $Ne_{w(1)}\in\span\{e_{w(1)},e_{w(2)}\}$, so one can verify that only the four elements

$$w\in\{e,s_1,s_2,w_0\}=\{123,213,132,321\}$$

remain. Indeed, writing down directly the points of the Bruhat cells corresponding to the two missing elements $231, 312$ and considering their intersection with $\Pet_3$, one can easily verify that it is empty.

The four flags obtained above are the $2^{n-1}=4$ coordinate flags corresponding to subsets of simple roots $A\subseteq\{\alpha_1,\alpha_2\}$ and the maximal length elements $w_A$ of the Weyl groups $W_A$ they define, showing that the Peterson variety remembers the combinatorics of the simple roots.
:::

Meanwhile, the key idea of [Proposition 9](#prop9){: data-lid="nwq2m" } was to decompose $\mathcal{Y}$ by taking the intersection of $\mathcal{Y}$ with the Bruhat decomposition of $G/B$. But we have already examined the decomposition via the opposite Borel subgroup in [§Bruhat Decomposition, ⁋Theorem 8](/en/math/lie_theory/bruhat_decomposition#thm8){: data-lid="81xjh" }, so we can also explore the properties of $\mathcal{Y}$ through $\mathcal{Y}\cap B^-wB/B$.

The nature of the result is completely different. Instead of the pieces being affine spaces, each piece is an affine variety meaningful in its own right. Again there are exactly $2^{\rank(\mathfrak{g})}$ nonempty pieces, with the same indexing as the paving. That is, the nonempty pieces are the locally closed subvarieties given for each $A\subseteq\Delta$ by the intersection

$$\mathcal{Y}\cap B^-w_AB/B$$

with the $B^-$ Bruhat cell of the same longest element $w_A$ [Pet]. At this point, since the subset $A\subseteq\Delta$ is in one-to-one correspondence with the standard parabolic subgroup $B\subseteq P\subseteq G$ having $W_A$ as its Weyl group, we write (for reasons we will see shortly) this piece as $\mathcal{Y}_P$ to obtain the stratification

$$\mathcal{Y}=\bigsqcup_{P\supseteq B}\mathcal{Y}_P$$

of $\mathcal{Y}$. Looking at the two extremes: the stratum for $P=G$ ($A=\Delta$, $w_A=w_0$) is a single point $\{w_0B\}$, and the stratum for $P=B$ ($A=\emptyset$, $w_A=e$) is the Zariski dense open subset of $\mathcal{Y}$ given by the intersection

$$\mathcal{Y}_B=\mathcal{Y}\cap B^-B/B$$

with the opposite big cell. In general, the dimension of $\mathcal{Y}_P$ equals $\lvert\Delta\setminus A\rvert$, that is, the number of simple roots not contained in $P$. That is, the cell of the paving and the stratum of the stratification are two pieces attached to the same $w_A$, having the same count and both containing the point $w_AB$, while their dimensions grow in mutually complementary directions as $\lvert A\rvert$ and $\lvert\Delta\setminus A\rvert$.

The reason this decomposition has significance beyond merely replacing $B$ by $B^-$ is that it carries information about quantum cohomology. In the following theorem, the *Langlands dual group* $G^\vee$ of the Lie group $G$ is the dual group obtained by interchanging roots and coroots in the root datum; in this situation, let $\mathcal{Y}^\vee$ be the Peterson variety constructed following [Definition 8](#def8){: data-lid="348l4" }, and let $\mathcal{Y}^\vee_P$ denote the stratum of $\mathcal{Y}^\vee$ corresponding to the Langlands dual $P^\vee$ of a parabolic subgroup $P$ of $G$.

::: Theorem 11 (Peterson)
In the Peterson variety of $G$'s Langlands dual $G^\vee$, for each standard parabolic subgroup $P\supseteq B$, the coordinate ring of the corresponding stratum $\mathcal{Y}^\vee_P$ is isomorphic to the small quantum cohomology ring of the partial flag variety $G/P$.

$$\mathbb{C}[\mathcal{Y}^\vee_P]\cong QH^\ast(G/P)$$
:::

This theorem was introduced in Peterson's 1997 MIT lecture; there is no separate publication, but its proof can be found in [lecture notes](https://math.soimeme.org/~arunram/Resources/PetersonGmodBcourse1997.pdf) and elsewhere. However, in the case of the Grassmannian that we have mainly been examining, $\GL_n$ is Langlands self-dual, so $G\cong G^\vee$ and this duality is not very visible.

Since introducing the flag variety in [§Borel Subgroups, ⁋Definition 12](/en/math/lie_theory/borel_subgroup#def12){: data-lid="cdyia" }, we have not used the language of algebraic geometry in full earnest, but to understand the spirit of this theorem we can no longer postpone it. The essential point is the way algebraic geometry interprets a ring $A$ itself as a geometric space over $\mathbb{C}$, namely $\Spec A$, with $A$ as the ring of functions on that space. In this dictionary, each point of the space $\Spec A$ corresponds to a maximal ideal of $A$, and a ring homomorphism $A\rightarrow B$ corresponds to a geometric function $\Spec B\rightarrow \Spec A$. Important special cases are when $A=\mathbb{C}$ and $B=\mathbb{C}$ respectively: first, if $A=\mathbb{C}$, then in the algebraic world $\mathbb{C}\rightarrow B$ is the structure morphism that views the ring $B$ as a $\mathbb{C}$-algebra. In the corresponding geometric world, since $\Spec \mathbb{C}$ is a single point, the function $\Spec B\rightarrow \Spec A$ becomes a function to a single point. If both $A,B$ are $\mathbb{C}$-algebras and the following commutative diagram

{% diagram Math/Lie_Theory/Richardson_Peterson_Variety-1.svg width="12em" alt="If $A, B$ are $\mathbb{C}$-algebras, the unit gives structure morphisms $\mathbb{C}\rightarrow A$, $\mathbb{C}\rightarrow B$, and a ring homomorphism $\varphi\colon A\rightarrow B$ commuting with both of these (that is, fixing $\mathbb{C}$) is the condition for $\varphi$ to be a $\mathbb{C}$-algebra homomorphism." %}

exists, then the $\mathbb{C}$-algebra homomorphism $A\rightarrow B$ now translates into the following commutative diagram

{% diagram Math/Lie_Theory/Richardson_Peterson_Variety-2.svg width="18em" alt="Applying $\Spec$ to the triangle above reverses all arrows, so that $\Spec\varphi\colon\Spec B\rightarrow\Spec A$ becomes a morphism over the single point $\Spec\mathbb{C}$." %}

. On the other hand, when $B=\mathbb{C}$, the ring homomorphism $A\rightarrow \mathbb{C}$ translates in the geometric world to $\Spec \mathbb{C}\rightarrow\Spec A$, that is, this ring homomorphism itself becomes a single point. Also recall that when $A$ is a $\mathbb{C}$-algebra, we usually interpreted this ring homomorphism as an evaluation map. Finally, using a ring homomorphism $A\rightarrow B$ to view $B$ as an $A$-algebra is interpreted, as seen above, as a morphism $\Spec B\rightarrow\Spec A$, that is, a relative space lying over the base $\Spec A$, and an $A$-module is viewed as a sheaf on $\Spec A$ (an object analogous to a vector bundle). In particular, a free module of rank $N$ corresponds to a trivial rank $N$ bundle, so for such an $A$-algebra, $\Spec$ becomes a finite morphism whose fibers over the base consist of $N$ points (counting $\dim$). The most basic case is affine space: for the polynomial algebra $\mathbb{C}[\x_1,\ldots,\x_n]$, taking $\Spec$ yields affine $n$-space $\mathbb{A}^n$, and more generally $A[\x_1,\ldots,\x_n]$ corresponds to a relative affine space over the base $\Spec A$.

Now, to return to the interpretation of [Theorem 11](#thm11){: data-lid="1daba" }, let us first add a geometric setup to $QH^\ast(G/P)$. For notational convenience, suppose there are $k$ quantum parameters and write $q$ simply for this family; then $QH^\ast(G/P)$ is (as a module), over the polynomial ring $\mathbb{C}[q]$ of quantum parameters, a free module of rank $N=\dim_\mathbb{C}H^\ast(G/P)$. Now considering the structure morphism $\mathbb{C}[q]\rightarrow QH^\ast(G/P)$, geometrically this defines $\Spec QH^\ast(G/P)\rightarrow \Spec\mathbb{C}[q]$. Then, as seen above, this is a finite morphism from $\Spec QH^\ast(G/P)$ to $\mathbb{A}^k$ of rank $N$.

Then considering the fiber in $\Spec \mathbb{C}[q]\cong\mathbb{A}^k$ over an arbitrary generic point $q_0$ is precisely the same as the following diagram:

{% diagram Math/Lie_Theory/Richardson_Peterson_Variety-3.svg width="14em" alt="Commutative square corresponding to the fiber at $q=q_0$. For a point $y$, restricting its character $\rchi_y$ to $\mathbb{C}[q]$ gives the evaluation at $q_0$, namely $\operatorname{ev}_{q_0}$, meaning that $y$ lies over $q_0$." %}

Algebraically, this is the following tensor product

$$QH^\ast(G/P)\otimes_{\mathbb{C}[q]}\mathbb{C}[q]/(q-q_0)\cong QH^\ast(G/P)/(q-q_0)$$

where a point of the fiber is again a ring homomorphism $QH^\ast(G/P)/(q-q_0)\rightarrow \mathbb{C}$. Similarly, applying the isomorphism of [Theorem 11](#thm11){: data-lid="sqkk7" }, one can consider the following commutative diagram:

{% diagram Math/Lie_Theory/Richardson_Peterson_Variety-4.svg width="24em" alt="Illustration of the Peterson isomorphism realizing the spectrum of quantum cohomology as flags. On $\mathcal{Y}^\vee_P$, a point $y$ (that is, a flag in $G^\vee/B^\vee$) gives an evaluation $\operatorname{ev}_y$, which lifts via the Peterson isomorphism $\Phi\colon a\mapsto f_a$ to the character $\rchi_y=\operatorname{ev}_y\circ\Phi$ (right square, $\rchi_y(a)=f_a(y)$), and restricting to $\mathbb{C}[q]$ gives for $y$ the evaluation at its quantum parameter value $q_0$ (left square). That is, a fiber point over $q_0$ $=$ a character over $q_0$ $=$ flag." %}

where the last vertical map $\ev_y$ defines a point on $\mathcal{Y}^\vee_P$. Now let us decode what this point contains, following the dictionary. First, $QH^\ast(G/P)/(q-q_0)$ is a finite-dimensional algebra over $\mathbb{C}$, on which each cohomology class $a$ gives the operator $a\qtimes-$ of multiplication by the quantum product. For the point $y$ obtained above, the corresponding character $\rchi_y\colon QH^\ast(G/P)/(q-q_0)\rightarrow\mathbb{C}$ assigns to each $a$ a scalar $\rchi_y(a)$, and since it is a ring homomorphism, it respects $\rchi_y(a\qtimes b)=\rchi_y(a)\rchi_y(b)$ and $\rchi_y(1)=1$. This means that $\rchi_y(a)$ is an eigenvalue of the operator $a\qtimes-$, and these eigenvalues are assigned simultaneously without contradiction with the quantum product. In other words, a point of the fiber is a way, at generic $q_0$, to consistently assign a simultaneous set of eigenvalues to all quantum multiplication operators.

And [Theorem 11](#thm11){: data-lid="x7ibo" } tells us where these simultaneous eigenvalues live. Under the isomorphism $\mathbb{C}[\mathcal{Y}^\vee_P]\cong QH^\ast(G/P)$, each class $a$ corresponds on $\mathcal{Y}^\vee_P$ to a regular function $f_a$, so in the language of the dictionary, the character $\rchi_y$ above is nothing other than evaluation at the flag $y$, namely $\rchi_y=\ev_y$, and thus $\rchi_y(a)=f_a(y)$. That is, the simultaneous eigenvalue $\rchi_y(a)$ is not an abstract floating number, but is obtained inside $G^\vee/B^\vee$ at a concrete flag $y$ by reading the value of the coordinate function $f_a$. In this way, the spectrum of the abstract algebra $QH^\ast(G/P)$, namely $\Spec QH^\ast(G/P)=\mathcal{Y}^\vee_P$, sits as actual points inside the flag variety $G^\vee/B^\vee$, and each such point (that is, flag) places a simultaneous set of eigenvalues for quantum multiplication in our hands.

In the smallest Grassmannian $\mathbb{P}^1=\Gr(1,2)$, we can see all of this by hand. For $n=2$, the Peterson condition $NV_1\subseteq V_2=\mathbb{C}^2$ is vacuous, so $\mathcal{Y}=\Fl_2=\mathbb{P}^1$ is the whole space, and the stratum $\mathcal{Y}_B$ is the intersection with the opposite big cell, $\mathbb{P}^1\setminus\{w_0B\}\cong\mathbb{A}^1$. On the other hand, $QH^\ast(\mathbb{P}^1)=\mathbb{C}[\sigma,q]/(\sigma^2-q)\cong\mathbb{C}[\sigma]$ is also a polynomial ring in one variable, in agreement with the isomorphism of the theorem, and under this isomorphism the quantum parameter is realized as the square of the affine coordinate, $q=\sigma^2$. The fiber over generic $q_0$ consists of the two points $\sigma=\pm\sqrt{q_0}$, that is, $\binom{2}{1}=2$ points, and the fiber over $q_0=0$ is a double point sitting over the single point $B/B$ with length $2$, whose coordinate ring is the classical cohomology $\mathbb{C}[\sigma]/(\sigma^2)=H^\ast(\mathbb{P}^1)$. That is, even the degeneration from quantum to classical occurs geometrically within the stratum.

Similarly, for general $\Gr(k,n)$, the fiber over generic $q_0$ consists of $\binom{n}{k}$ distinct points. These finitely many points have another explicit model: that they are realized as the critical points of a Laurent polynomial, namely a superpotential, is one of the assertions of mirror symmetry, and constructing this correspondence for general $G/P$ remains an actively studied topic (see [Mirror Symmetry](/en/mirror_symmetry/)).

::: Remark 12
The affine paving of [Proposition 9](#prop9){: data-lid="q9kxv" } is also the starting point for cohomology computations. By the paving, the cohomology of $\mathcal{Y}$ is a free module with a basis indexed by the cells, and vanishes in odd degrees. That is, the affine paving argument for flag varieties from [§Bruhat Decomposition, ⁋Proposition 17](/en/math/lie_theory/bruhat_decomposition#prop17){: data-lid="ru8lp" } works for Peterson varieties in exactly the same way, and Insko–Tymoczko [IT] developed the intersection theory of Peterson varieties on this basis.
:::

---

**References**

**[KL80]** D. Kazhdan, G. Lusztig, *Schubert varieties and Poincaré duality*, Geometry of the Laplace operator, Proc. Sympos. Pure Math. **36**, AMS, 1980.  
**[Deo85]** V. V. Deodhar, *On some geometric aspects of Bruhat orderings. I. A finer decomposition of Bruhat cells*, Invent. Math. **79** (1985), 499--511.  
**[Ric92]** R. W. Richardson, *Intersections of double cosets in algebraic groups*, Indag. Math. **3** (1992), 69--77.  
**[Bri]** M. Brion, *Lectures on the geometry of flag varieties*, in *Topics in cohomological studies of algebraic varieties*, Trends Math., Birkhäuser, 2005, 33--85.  
**[Kos]** B. Kostant, *The principal three-dimensional subgroup and the Betti numbers of a complex simple Lie group*, Amer. J. Math. **81** (1959), 973--1032.  
**[Kos63]** B. Kostant, *Lie group representations on polynomial rings*, Amer. J. Math. **85** (1963), 327--404.  
**[Kos96]** B. Kostant, *Flag manifold quantum cohomology, the Toda lattice, and the representation with highest weight $\rho$*, Selecta Math. (N.S.) **2** (1996), 43--91.  
**[LS]** T. Lam, M. Shimozono, *Quantum cohomology of $G/P$ and homology of affine Grassmannian*, Acta Math. **204** (2010), 49--90.  
**[Pet]** D. Peterson, Lecture notes, Massachusetts Institute of Technology, Spring 1997 (unpublished).  
**[Tym]** J. S. Tymoczko, *Paving Hessenberg varieties by affines*, Selecta Math. (N.S.) **13** (2007), 353--367.  
**[Pre]** M. Precup, *Affine pavings of Hessenberg varieties for semisimple groups*, Selecta Math. (N.S.) **19** (2013), 903--922.  
**[IT]** E. Insko, J. Tymoczko, *Affine pavings of regular nilpotent Hessenberg varieties and intersection theory of the Peterson variety*, J. Combin. Theory Ser. A **187** (2022), 105572.

---
[^1]: Note that the $\mathfrak{h}$ denoting the Cartan subalgebra, which comes from [§Root Systems, ⁋Definition 4](/en/math/lie_theory/root_systems#def4){: data-lid="bn5k1" }, is <em>unrelated</em> to the $H$ in our discussion.
