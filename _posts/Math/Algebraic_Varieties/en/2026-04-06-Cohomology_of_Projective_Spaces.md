---
title: "Cohomology of Projective Space"
description: "Sheaf cohomology is a richer invariant that includes higher cohomology groups, and for line bundles on projective space it is completely computed by Bott's formula. The post includes a proof using Cech cohomology."
excerpt: "Bott's formula and the cohomology of line bundles on projective space"

categories: [Math / Algebraic Varieties]
permalink: /en/math/algebraic_varieties/cohomology_of_projective_spaces
sidebar:
    nav: "algebraic_varieties-en"

date: 2026-04-06
weight: 14
translated_at: 2026-07-30T20:15:03+00:00
translation_source: kimi-cli
last_polished_at: 2026-07-30T20:15:03+00:00
---
We previously defined the line bundle $\mathcal{O}(d)$ in [§Line Bundles and Vector Bundles, ⁋Example 12](/en/math/algebraic_varieties/line_bundles#ex12), and verified through the computation of [§Line Bundles and Vector Bundles, ⁋Example 16](/en/math/algebraic_varieties/line_bundles#ex16) that its global sections $H^0(\mathbb{P}^n, \mathcal{O}(d))$ are isomorphic to homogeneous polynomials of degree $d$. However, the sheaf cohomology introduced in our earlier post [§Sheaf Cohomology, ⁋Definition 1](/en/math/algebraic_varieties/sheaf_cohomology#def1) is a richer invariant that includes not only $H^0$ but also the higher cohomology groups $H^1, H^2, \ldots$. Thus, we now aim to extract all information about $\mathcal{O}(d)$ using not just $H^0$ but all higher cohomology groups.

## Bott's Formula

Since $\mathcal{O}(d)$ is a line bundle, it is a quasi-coherent sheaf, and therefore it suffices to use Čech cohomology with the standard affine cover $\mathcal{U}=\{U_0,\ldots, U_n\}$ to compute its sheaf cohomology. The following is the result of that computation.

::: Proposition 1 (Bott)
The cohomology of the line bundle $\mathcal{O}(d)$ on $\mathbb{P}^n$ is as follows.

$$H^q(\mathbb{P}^n, \mathcal{O}(d)) = \begin{cases}
\mathbb{K}[\x_0, \ldots, \x_n]_d & q = 0, d \geq 0 \\
\mathbb{K}[\x_0^{-1}, \ldots, \x_n^{-1}]_{-d-n-1} & q = n, d \leq -n-1 \\
0 & \text{otherwise}
\end{cases}$$
:::

::: Proof
As explained above, we use Čech cohomology. First, recall that on each open set, the sections $\mathcal{O}(d)(U_i)$ are

$$\x_i^d \cdot \mathbb{K}[\x_0/\x_i, \ldots, \widehat{\x_i/\x_i}, \ldots, \x_n/\x_i].$$

([§Line Bundles and Vector Bundles, ⁋Example 12](/en/math/algebraic_varieties/line_bundles#ex12)) Then a Čech cochain $f \in \check{C}^p(\mathcal{U}, \mathcal{O}(d))$ assigns to each $(p+1)$-tuple $(i_0, \ldots, i_p)$ a regular section on the open set $U_{i_0}\cap\cdots\cap U_{i_p}$. For this section to be regular on the intersection $U_{i_0}\cap\cdots\cap U_{i_p}$, only the coordinates that do not vanish, namely $\x_{i_0}, \ldots, \x_{i_p}$, may appear in the denominator; the rest are not allowed. Thus the monomials

$$f_{i_0 \cdots i_p} = \x_0^{a_0} \cdots \x_n^{a_n},\qquad \sum_{j=0}^n a_j=d,\quad a_j\geq 0\text{ for $j\not\in \{i_0, \ldots, i_p\}$}$$

generate the sections.

For the coboundary map $\delta : \check{C}^p \rightarrow \check{C}^{p+1}$, we have

$$(\delta f)_{i_0 \cdots i_{p+1}} = \sum_{k=0}^{p+1} (-1)^k f_{i_0 \cdots \hat{i_k} \cdots i_{p+1}}.$$

That is, we take the alternating sum of the sections corresponding to the $p$-tuples obtained by omitting one index from each $(p+1)$-tuple.

Now let us use this data to compute each cohomology group. Starting with the case of $\mathbb{P}^1$, the Čech complex is

$$0 \longrightarrow \check{C}^0\overset{\delta}{\longrightarrow}\check{C}^1\longrightarrow 0.$$

Here

$$\check{C}^0=\mathcal{O}(d)(U_0)\oplus \mathcal{O}(d)(U_1),\qquad \check{C}^1=\mathcal{O}(d)(U_0\cap U_1),$$

and the respective section spaces are

$$\mathcal{O}(d)(U_0) = \x_0^d \cdot \mathbb{K}[\x_1/\x_0], \qquad \mathcal{O}(d)(U_1) = \x_1^d \cdot \mathbb{K}[\x_0/\x_1], \qquad \mathcal{O}(d)(U_0 \cap U_1) = \mathbb{K}[\x_0^{\pm 1}, \x_1^{\pm 1}]_d.$$

First, to compute the cohomology in $\check{C}^0$, we analyze $\ker\delta$. Since $H^0(\mathbb{P}^n, \mathcal{O}(d))=\Gamma(\mathbb{P}^n, \mathcal{O}(d))$, this is merely a re-verification of the computation in [§Line Bundles and Vector Bundles, ⁋Example 16](/en/math/algebraic_varieties/line_bundles#ex16); but instead of treating it as a separate example, let us carry out the Čech cohomology computation within this proof.

By definition, a cochain $(f_0, f_1) \in \check{C}^0$ lies in $\ker \delta$ precisely when $f_0 = f_1$ holds in $\mathcal{O}(d)(U_0 \cap U_1)$. Looking first at the $U_0$ part, we know that any monomial belonging to $\mathcal{O}(d)(U_0)$ must be of the form $\x_0^{d-a}\x_1^a$ for some $a\geq 0$. Similarly, any monomial belonging to $\mathcal{O}(d)(U_1)$ must be of the form $\x_0^b\x_1^{d-b}$ for some $b\geq 0$. Now for a given cocycle $(f_0,f_1)$ to lie in $\ker\delta$, we must have $f_0=f_1$, so only monomials satisfying $a+b=d$ can belong to $\ker\delta$. In other words, the monomials

$$\x_0^d, \quad\x_0^{d-1}\x_1,\quad\ldots, \quad\x_0\x_1^{d-1},\quad \x_1^d$$

form a basis of $H^0$, and this gives the desired result. If $d<0$, then $a,b\geq 0$ cannot satisfy this equation, so $H^0$ is $0$.

Now let us compute $H^1$. That is, we must compute $\coker\delta$. From the computation above, we know that the image of $\delta$ consists of elements of the form

$$f_1-f_0=\sum_{i\geq 0}a_i \x_0^{d-i}\x_1^i-\sum_{j\geq 0}b_j\x_0^j\x_1^{d-j}\tag{$\ast$}$$

for suitable constants $a_i,b_j$. On the other hand, $\check{C}^1=\mathcal{O}(d)(U_0\cap U_1)=\mathbb{K}[\x_0^{\pm 1}, \x_1^{\pm 1}]_d$ is an infinite-dimensional space with basis the degree-$d$ monomials

$$\x_0^a\x_1^{d-a},\qquad a\in\mathbb{Z}\tag{$\ast\ast$}$$

with no restriction on the exponents. The two sums in ($\ast$) give respectively the monomials with $a\leq d$ and those with $a\geq 0$, so the image of $\delta$ is the subspace spanned by those monomials in ($\ast\ast$) for which $a\geq 0$ or $d-a\geq 0$. Hence a basis for $\coker\delta$ is given by the monomials corresponding to $a$ satisfying $d+1\leq a\leq -1$, i.e. those for which both exponents are negative. If $d\geq -1$, no such $a$ exists and $\coker\delta=0$; if $d\leq -2$, then the $-d-1$ monomials

$$\x_0^{-1}\x_1^{d+1}, \quad \x_0^{-2}\x_1^{d+2},\quad\ldots,\quad \x_0^{d+1}\x_1^{-1}$$

form a basis of $\coker \delta$. We will explain the notation in the statement separately after the proof.

We now finish the proof for general $n$. In the $\mathbb{P}^1$ computation above, we examined for each monomial whether it belonged to $\ker$ or $\im$ and drew a conclusion; this was not a coincidence. Since the coboundary map sends monomials to monomials anyway, the entire Čech complex splits as a direct sum of subcomplexes, one for each Laurent monomial $\x^a=\x_0^{a_0}\cdots\x_n^{a_n}$ ($a\in\mathbb{Z}^{n+1}$, $\sum_ja_j=d$), and therefore computing the subcomplex for each $a$ yields all $q$ at once.

Fix a multi-index $a$, and partition the indices according to the signs of the exponents into two sets $N_{<0}(a)=\{j\mid a_j<0\}$ and $N_{\geq 0}(a)=\{j\mid a_j\geq 0\}$. By the monomial condition seen above, $\x^a$ is regular on $U_{i_0}\cap\cdots\cap U_{i_p}$ if and only if

$$N_{<0}(a)\subseteq\{i_0,\ldots, i_p\}.$$

Hence the $p$-th term of the subcomplex corresponding to $a$ is the vector space spanned by the $(p+1)$-element index sets $I=\{i_0,\ldots, i_p\}$ containing $N_{<0}(a)$, and its differential is the alternating sum of those obtained by removing one index from $I$. Since $I\supseteq N_{<0}(a)$, we can write $I=N_{<0}(a)\sqcup J$ uniquely, where $J$ is a subset of $N_{\geq 0}(a)$, and $|I|=p+1$ means $|J|=p+1-|N_{<0}(a)|$. That is, the $N_{<0}(a)$ part of $I$ is forced and only $J$ is free, so this subcomplex is the complex built from subsets of $N_{\geq 0}(a)$

$$K^q=\bigoplus_{\substack{J\subseteq N_{\geq 0}(a) \\ \lvert J\rvert=q}}\mathbb{K}\cdot e_J, \qquad \delta(e_J)=\sum_{v\in N_{\geq 0}(a)\setminus J}\pm e_{J\cup\{v\}}$$

shifted in degree by $|N_{<0}(a)|$.

For this complex, observe that if $N_{\geq 0}(a)$ is non-empty then $K^\bullet$ is exact. Indeed, fixing $v\in N_{\geq 0}(a)$ and setting

$$h(e_J)=\begin{cases} e_{J\setminus\{v\}} & v\in J \\ 0 & v\notin J\end{cases}$$

we have $\delta h+h\delta=\mathrm{id}$ with appropriate sign choices. Then the cohomology of the complex with $K^0$ removed,

$$0 \rightarrow K^1 \rightarrow K^2 \rightarrow \cdots \rightarrow 0,$$

is $\mathbb{K}$ in degree $q=1$ because

$$\ker(K^1 \rightarrow K^2)=\im(K^0 \rightarrow K^1)\cong K^0=\mathbb{K},$$

and $0$ in all other degrees. Thus, if $N_{\geq 0}(a)$ is non-empty and the above subcomplex is the whole $K^\bullet$, then the cohomology vanishes in every degree; for something to survive, one of these two conditions must fail. As we saw above, the latter condition concerns whether the term corresponding to the empty set $J=\emptyset$, namely $K^0$, is present: if $N_{<0}(a)\neq\emptyset$, then $I=N_{<0}(a)$ itself satisfies the condition at $p=|N_{<0}(a)|-1\geq 0$, so that term is included; if $N_{<0}(a)=\emptyset$, then $I$ cannot be empty, so it is omitted.

The conclusion now splits into three cases according to $N_{<0}(a)$. First, if $N_{<0}(a)=\emptyset$, i.e. all $a_j\geq 0$, then as seen above $N_{\geq 0}(a)$ is the whole set and $K^0$ is missing, so the cohomology is $\mathbb{K}$ only at $q=1$, i.e. $p=0$, and such $\x^a$ form a basis of $H^0(\mathbb{P}^n, \mathcal{O}(d))$. These are the degree-$d$ monomials with all exponents non-negative, which exist only when $d\geq 0$ and give $\mathbb{K}[\x_0,\ldots, \x_n]_d$. Next, if $N_{<0}(a)=\{0,\ldots, n\}$, i.e. all $a_j<0$, then $N_{\geq 0}(a)=\emptyset$, so the only admissible $I$ is the whole set, and the complex consists of a single $\mathbb{K}$ at $p=n$; such $\x^a$ form a basis of $H^n(\mathbb{P}^n, \mathcal{O}(d))$. This time all exponents are at most $-1$, so their sum is at most $-n-1$, and they exist only when $d\leq -n-1$. Finally, if $N_{<0}(a)$ is neither empty nor the whole set, then $N_{\geq 0}(a)$ is non-empty while $K^0$ is present, so $K^\bullet$ itself is exact and contributes nothing in any degree. That is, the cohomology vanishes for $0<q<n$.
:::

In the proof above, we showed that for each variable $\x_0,\cdots, \x_n$ and for $d\leq -n-1$, the group $H^n(\mathbb{P}^n, \mathcal{O}(d))$ is generated by the monomials

$$\x_0^{a_0} \cdots \x_n^{a_n},\qquad  a_i \leq -1, \quad \sum a_i=d.$$

(Note that $d$ is negative.) Regarding each $\x_i^{-1}$ as a new variable $\y_i=\x_i^{-1}$, this space can also be described as generated by the expressions

$$\y_0^{\lvert a_0\rvert},\cdots \y_n^{\lvert a_n\rvert}\qquad \lvert a_i\rvert\geq 1,\quad \sum \lvert a_i\rvert=\lvert d\rvert.$$

Here all $a_i$ and $d$ are negative, so $|a_i|=-a_i$ and $|d|=-d$. This space is almost the space of homogeneous polynomials of degree $|d|$, except that the $|a_i|$ cannot be zero. Thus, substituting $b_i=|a_i|-1$, we can think of this space as

$$\y_0^{b_0}\cdots \y_n^{b_n},\qquad b_i\geq 0,\quad \sum b_i=\lvert d\rvert-(n+1).$$

In other words, this space can be viewed as the space of "negative degree" monomials of degree $-d-n-1$, and for this reason it is denoted by

$$\mathbb{K}[\x_0^{-1}, \ldots, \x_n^{-1}]_{-d-n-1}.$$

For later use, we define the Euler characteristic.

::: Definition 2
For a variety $X$ and a coherent sheaf $\mathcal{F}$ defined on it, the *Euler characteristic* of $\mathcal{F}$ is defined by the formula

$$\rchi(X, \mathcal{F}) = \sum_{i=0}^{n} (-1)^i \dim H^i(X, \mathcal{F}).$$
:::

In the special case where $X=\mathbb{P}^n$ and $\mathcal{F}=\mathcal{O}(d)$, in any case the intermediate cohomology groups all vanish and only the two end cohomology groups matter, so we can easily prove the following corollary.

::: Corollary 3
The Euler characteristic of $\mathcal{O}(d)$ on $\mathbb{P}^n$ is given by the formula

$$\rchi(\mathbb{P}^n, \mathcal{O}(d)) = \binom{n+d}{n}.$$


:::

::: Proof
By [Proposition 1](#prop1), the cohomology falls into three cases.

First, if $d \geq 0$, then only $H^0$ is non-zero, so

$$\rchi(\mathcal{O}(d)) = \dim H^0(\mathbb{P}^n, \mathcal{O}(d)) = \dim \mathbb{K}[\x_0, \ldots, \x_n]_d = \binom{n+d}{n}.$$

Second, if $-n \leq d \leq -1$, then all cohomology vanishes, so $\rchi(\mathcal{O}(d)) = 0$, and in this case we usually define $\binom{n+d}{n}=0$, which agrees with the convention.

Finally, consider the case $d \leq -n-1$. Here only $H^n$ is non-zero, so

$$\rchi(\mathcal{O}(d)) = (-1)^n \dim \mathbb{K}[\x_0^{-1}, \ldots, \x_n^{-1}]_{-d-n-1}.$$

By the explanation following [Proposition 1](#prop1), the dimension of this space is

$$\binom{-d-1}{n}=(-1)^n\binom{n+d}{n}.$$

Here $\binom{n+d}{n}$ follows the usual convention for binomial coefficient notation, as in the previous case.
:::

The Euler characteristic has the important property of additivity with respect to short exact sequences. That is, for a short exact sequence

$$0 \rightarrow \mathcal{F} \rightarrow \mathcal{G} \rightarrow \mathcal{H} \rightarrow 0,$$

we have $\rchi(\mathcal{G}) = \rchi(\mathcal{F}) + \rchi(\mathcal{H})$. Thus the Euler characteristic becomes an invariant that is much easier to compute and manipulate, at the cost of losing information about individual cohomology groups.

## Serre Vanishing

According to [Proposition 1](#prop1), on $\mathbb{P}^n$ the higher cohomology of $\mathcal{O}(d)$ vanishes for sufficiently large $d$. Since every line bundle on $\mathbb{P}^n$ is of the form $\mathcal{O}(d)$ for some $d$, this means that for any line bundle $\mathcal{L}$ on $\mathbb{P}^n$, the twisted line bundle

$$\mathcal{L}\otimes \mathcal{O}(d)$$

has vanishing higher cohomology for sufficiently large $d\gg 0$.

More generally, we can extend this to an arbitrary projective variety and an arbitrary coherent sheaf defined on it. For this we first need something to play the role of $\mathcal{O}(1)$; in our definition, a projective variety $X$ is always given by an embedding $X\hookrightarrow\mathbb{P}^N$, so we can simply pull back $\mathcal{O}(1)$ from $\mathbb{P}^N$.

::: Proposition 4 (Serre Vanishing)
Let $X$ be a projective variety, $\mathcal{L}$ an ample line bundle, and $\mathcal{F}$ a coherent sheaf. Then for sufficiently large $m$,

$$H^i(X, \mathcal{F} \otimes \mathcal{L}^{\otimes m}) = 0 \quad (i > 0).$$
:::

::: Proof
Since $\mathcal{L}$ is ample, for sufficiently large $m_0$ the bundle $\mathcal{L}^{\otimes m_0}$ is very ample. That is, there exists an embedding $i \colon X \hookrightarrow \mathbb{P}^N$ such that $\mathcal{L}^{\otimes m_0} = i^\ast\mathcal{O}(1)$. Restricting the standard affine cover $\{U_i\}$ of $\mathbb{P}^N$ to $X$ gives an affine open cover $\{X \cap U_i\}$. Since a finite intersection $U_{i_0} \cap \cdots \cap U_{i_p}$ is affine, so is $(X \cap U_{i_0}) \cap \cdots \cap (X \cap U_{i_p}) = X \cap (U_{i_0} \cap \cdots \cap U_{i_p})$. Hence the two Čech complexes are literally the same, and

$$\check{H}^i(\{X \cap U_j\}, \mathcal{F}) = \check{H}^i(\{U_j\}, i_\ast\mathcal{F})$$

holds. Since $X$ and $\mathbb{P}^N$ are separated schemes ([§Sheaf Cohomology, ⁋Theorem 11](/en/math/algebraic_varieties/sheaf_cohomology#thm11)), for quasi-coherent sheaves Čech cohomology equals sheaf cohomology:

$H^i(X, \mathcal{F}) = \check{H}^i(\{X \cap U_j\}, \mathcal{F}) = \check{H}^i(\{U_j\}, i_\ast\mathcal{F}) = H^i(\mathbb{P}^N, i_\ast\mathcal{F})$ Therefore it suffices to show the following: for a coherent sheaf $\mathcal{G}$ on $\mathbb{P}^N$, we have $H^i(\mathbb{P}^N, \mathcal{G}(n)) = 0$ ($i > 0$) for sufficiently large $n$. Here $\mathcal{G}(n) = \mathcal{G} \otimes \mathcal{O}_{\mathbb{P}^N}(n)$.

**Key Lemma**. We show that $\mathcal{G}(n)$ is globally generated for sufficiently large $n$. (See [Definition 6](#def6) below.)

Let $S = \mathbb{K}[\x_0, \ldots, \x_N]$, and let $M = \bigoplus_{n \in \mathbb{Z}} \Gamma(\mathbb{P}^N, \mathcal{G}(n))$ be a graded $S$-module. On each standard affine open set $D_+(\x_j)$, $\Gamma(D_+(\x_j), \mathcal{G})$ is the degree-0 localisation $M_{(\x_j)}$, which is a finitely generated module over $S_{(\x_j)}$. Choose generators $\bar{m}_1, \ldots, \bar{m}_{r_j} \in M_{(\x_j)}$. Each $\bar{m}_k$ can be written in the form $m_k / \x_j^{d_k}$, where $m_k \in M$ is a homogeneous element. Setting $d_0 = \max_j \max_k d_k$, we multiply each generator by $\x_j^{d_0 - d_k}$ to obtain homogeneous elements $m_k \cdot \x_j^{d_0 - d_k} \in M_{d_0}$. These are elements of $\Gamma(\mathbb{P}^N, \mathcal{G}(d_0))$, and they generate the stalk of $\mathcal{G}$ on $D_+(\x_j)$. Taking the maximum over $j$, we obtain that $\mathcal{G}(d_0)$ is globally generated.

**Vanishing**. We now show $H^i(\mathbb{P}^N, \mathcal{G}(n)) = 0$ ($i > 0$, $n \gg 0$).

If $N = 0$, then $\mathbb{P}^0$ is a point, so this is trivial. Assume $N \geq 1$. By the lemma above, $\mathcal{G}(n_0)$ is globally generated for $n_0 \gg 0$, so there exists a surjection

$$\mathcal{O}_{\mathbb{P}^N}^{\oplus r_0} \twoheadrightarrow \mathcal{G}(n_0).$$

The kernel $\mathcal{K}_0$ is coherent. From the long exact sequence of the short exact sequence

$$0 \rightarrow \mathcal{K}_0 \rightarrow \mathcal{O}^{\oplus r_0} \rightarrow \mathcal{G}(n_0) \rightarrow 0,$$

since $H^j(\mathbb{P}^N, \mathcal{O}^{\oplus r_0}) = 0$ ($j > 0$) by [Proposition 1](#prop1), we obtain

$$H^j(\mathcal{G}(n_0)) \cong H^{j+1}(\mathcal{K}_0) \quad (j \geq 1).$$

Now repeat the same process for $\mathcal{K}_0$. That is, choose $n_1 \gg 0$ such that $\mathcal{K}_0(n_1)$ is globally generated, and for the kernel $\mathcal{K}_1$ of the surjection

$$\mathcal{O}^{\oplus r_1} \twoheadrightarrow \mathcal{K}_0(n_1)$$

we obtain from the long exact sequence of

$$0 \rightarrow \mathcal{K}_1 \rightarrow \mathcal{O}^{\oplus r_1} \rightarrow \mathcal{K}_0(n_1) \rightarrow 0$$

that

$$H^{j+1}(\mathcal{K}_0(n_1)) \cong H^{j+2}(\mathcal{K}_1) \quad (j \geq 1).$$

Repeating this process $N$ times yields

$$H^j(\mathcal{G}(n_0)) \cong H^{j+N}(\mathcal{K}_{N-1}).$$

Since the cohomological dimension of $\mathbb{P}^N$ is $N$, we have $H^{j+N} = 0$ ($j \geq 1$, $j + N \geq N+1 > N$), and therefore $H^j(\mathcal{G}(n_0)) = 0$.

Finally, since $\mathcal{G}(n_0)$ is globally generated, $\mathcal{G}(n) = \mathcal{G}(n_0) \otimes \mathcal{O}(n - n_0)$ is also globally generated for $n \geq n_0$, and hence the same resolution argument applies to $\mathcal{G}(n)$ as well, so vanishing holds for all $n \geq n_0$.
:::

## Regularity

[Proposition 4](#prop4) gave a qualitative result that higher cohomology vanishes after sufficiently large twisting. Regularity quantifies this, measuring exactly how much twisting is needed.

Intuitively, higher cohomology arises from failures in lower-degree cohomology, so less twisting is needed in higher degrees. Keeping this in mind, the following definition is natural.

::: Definition 5
Let a projective variety $X$ and an ample line bundle $\mathcal{L}$ on it be fixed. Then a coherent sheaf $\mathcal{F}$ on $X$ is said to be *$m$-regular* if for every $i>0$,

$$H^i(X, \mathcal{F} \otimes \mathcal{L}^{\otimes m - i}) = 0$$

holds.
:::

In general, computing all cohomology groups of a coherent sheaf is almost impossible, but the basic idea is that higher cohomology vanishes after sufficient twisting. Regularity goes further: it is a concept that measures exactly how much twisting is needed.

One of the key reasons such twisting becomes useful when dealing with coherent sheaves is that sufficiently twisted coherent sheaves become *globally generated*. To gain intuition for this concept, let us first consider the case of line bundles. A line bundle $\mathcal{L}$ being *basepoint-free*, as defined in [§Linear Systems, ⁋Definition 5](/en/math/algebraic_varieties/linear_systems#def5), means that for every point $p \in X$ there exists a global section $s \in H^0(X, \mathcal{L})$ with $s(p) \neq 0$. That is, the base locus is empty, and the linear system $\lvert \mathcal{L} \rvert$ provides a non-zero value at each point. This is equivalent to the evaluation map

$$H^0(X, \mathcal{L}) \otimes \mathcal{O}_X \rightarrow \mathcal{L}$$

being surjective. *Globally generated* generalizes this condition to arbitrary coherent sheaves: a coherent sheaf $\mathcal{F}$ is globally generated if, similarly, the evaluation map of the above form is surjective, so that the stalk at each point can be generated by global sections. In particular, for line bundles, being globally generated is equivalent to being basepoint-free. This property played a key role in the proof of [Proposition 4](#prop4).

::: Definition 6
A coherent sheaf $\mathcal{F}$ is said to be *globally generated* if the evaluation map

$$H^0(X, \mathcal{F}) \otimes \mathcal{O}_X \rightarrow \mathcal{F}$$

is surjective. That is, the stalks can all be generated by global sections.
:::

To define regularity in general, we first need the notion of twist. On $\mathbb{P}^n$, since $\mathcal{O}(1)$ is used as the base, we write $\mathcal{F}(d) := \mathcal{F} \otimes \mathcal{O}(d)$. On an arbitrary projective variety $X$, we choose an ample line bundle $\mathcal{L}$ and define $\mathcal{F}(d) := \mathcal{F} \otimes \mathcal{L}^{\otimes d}$. Twist satisfies the following properties. By the associativity of the tensor product, $\mathcal{F}(d)(e) = \mathcal{F}(d+e)$ holds. Also, since the tensor product functor $- \otimes \mathcal{L}^{\otimes d}$ is a line bundle, it is exact, and therefore for a short exact sequence

$$0 \rightarrow \mathcal{F} \rightarrow \mathcal{G} \rightarrow \mathcal{H} \rightarrow 0,$$

the sequence

$$0 \rightarrow \mathcal{F}(d) \rightarrow \mathcal{G}(d) \rightarrow \mathcal{H}(d) \rightarrow 0$$

is also short exact.


::: Proposition 7 (Castelnuovo-Mumford Regularity)
Let $X$ be a projective variety, $\mathcal{L}$ an ample line bundle, and $\mathcal{F}$ a coherent sheaf. If $\mathcal{F}$ is $m$-regular with respect to $\mathcal{L}$, then the following hold.

1. $\mathcal{F} \otimes \mathcal{L}^{\otimes m}$ is globally generated.
2. $\mathcal{F} \otimes \mathcal{L}^{\otimes p}$ is $(m+p)$-regular with respect to $\mathcal{L}$ for all $p \geq 0$.
:::

::: Proof
We prove by induction on the dimension of $X$. If $\dim X = 0$, then $X$ is a point and a coherent sheaf $\mathcal{F}$ is a finite-dimensional vector space, so all cohomology except $H^0$ vanishes automatically. Now assume $\dim X \geq 1$.

The key is to use the restriction exact sequence for an effective divisor $D$ defined by a global section $s \in H^0(X, \mathcal{L})$. Choosing a general $s$, Bertini's theorem implies that $D$ is smooth, and we obtain the following short exact sequence.

$$0 \rightarrow \mathcal{F} \otimes \mathcal{L}^{\otimes k-1} \xrightarrow{\cdot s} \mathcal{F} \otimes \mathcal{L}^{\otimes k} \rightarrow \mathcal{F} \otimes \mathcal{L}^{\otimes k}\vert_D \rightarrow 0$$

The long exact sequence in cohomology of this sequence gives

$$\cdots \rightarrow H^i(\mathcal{F} \otimes \mathcal{L}^{\otimes k-1}) \rightarrow H^i(\mathcal{F} \otimes \mathcal{L}^{\otimes k}) \rightarrow H^i(\mathcal{F} \otimes \mathcal{L}^{\otimes k}\vert_D) \rightarrow H^{i+1}(\mathcal{F} \otimes \mathcal{L}^{\otimes k-1}) \rightarrow \cdots$$

In the special case of $\mathbb{P}^n$, we have $\mathcal{L} = \mathcal{O}(1)$, $s$ is a general linear form, and $D$ becomes a hyperplane $H$ isomorphic to $\mathbb{P}^{n-1}$.

**Step 1: $m$-regularity of $\mathcal{F}\vert_D$.** Since $\mathcal{F}$ is $m$-regular with respect to $\mathcal{L}$, we have $H^i(\mathcal{F} \otimes \mathcal{L}^{\otimes m-i}) = 0$ for $i > 0$. Let us show that $\mathcal{F}\vert_D$ is $m$-regular with respect to $\mathcal{L}\vert_D$. Substituting $k = m - i$ into the restriction sequence ($0 < i \leq n-1$) gives

$$0 \rightarrow \mathcal{F} \otimes \mathcal{L}^{\otimes m-i-1} \rightarrow \mathcal{F} \otimes \mathcal{L}^{\otimes m-i} \rightarrow \mathcal{F}\vert_D \otimes (\mathcal{L}\vert_D)^{\otimes m-i} \rightarrow 0,$$

and from its long exact sequence we have

$$H^i(\mathcal{F} \otimes \mathcal{L}^{\otimes m-i}) \rightarrow H^i(\mathcal{F}\vert_D \otimes (\mathcal{L}\vert_D)^{\otimes m-i}) \rightarrow H^{i+1}(\mathcal{F} \otimes \mathcal{L}^{\otimes m-i-1}).$$

By $m$-regularity, $H^i(\mathcal{F} \otimes \mathcal{L}^{\otimes m-i}) = 0$, and $H^{i+1}(\mathcal{F} \otimes \mathcal{L}^{\otimes m-i-1}) = 0$ ($i+1 > 0$), so we obtain

$$H^i(\mathcal{F}\vert_D \otimes (\mathcal{L}\vert_D)^{\otimes m-i}) = 0$$

for $0 < i \leq n-1$. This means that $\mathcal{F}\vert_D$ is $m$-regular with respect to $\mathcal{L}\vert_D$.

**Step 2: $\mathcal{F} \otimes \mathcal{L}^{\otimes m}$ is globally generated.** Apply the inductive hypothesis to $D$. The divisor $D$ is a projective variety with $\dim D < \dim X$, and $\mathcal{L}\vert_D$ is an ample line bundle. Since $\mathcal{F}\vert_D$ is $m$-regular, the inductive hypothesis implies that $\mathcal{F}\vert_D \otimes (\mathcal{L}\vert_D)^{\otimes m}$ is globally generated on $D$.

Now we show that $\mathcal{F} \otimes \mathcal{L}^{\otimes m}$ is globally generated. It suffices to verify that the fiber $(\mathcal{F} \otimes \mathcal{L}^{\otimes m})_p$ at an arbitrary point $p \in X$ is generated by the images of global sections. Choose a general divisor $D$ passing through $p$, and substitute $k = m$ into the restriction sequence:

$$0 \rightarrow \mathcal{F} \otimes \mathcal{L}^{\otimes m-1} \rightarrow \mathcal{F} \otimes \mathcal{L}^{\otimes m} \rightarrow \mathcal{F}\vert_D \otimes (\mathcal{L}\vert_D)^{\otimes m} \rightarrow 0.$$

From $m$-regularity with $i = 1$, we have $H^1(\mathcal{F} \otimes \mathcal{L}^{\otimes m-1}) = 0$, so

$$H^0(\mathcal{F} \otimes \mathcal{L}^{\otimes m}) \rightarrow H^0(\mathcal{F}\vert_D \otimes (\mathcal{L}\vert_D)^{\otimes m})$$

is surjective. By the inductive hypothesis, $\mathcal{F}\vert_D \otimes (\mathcal{L}\vert_D)^{\otimes m}$ is globally generated on $D$, so its fiber at $p$ is generated by the image of $H^0(\mathcal{F}\vert_D \otimes (\mathcal{L}\vert_D)^{\otimes m})$. Since the restriction map is surjective, the global sections of $\mathcal{F} \otimes \mathcal{L}^{\otimes m}$ also generate the fiber at $p$. Hence $\mathcal{F} \otimes \mathcal{L}^{\otimes m}$ is globally generated.

**Step 3: $\mathcal{F} \otimes \mathcal{L}^{\otimes p}$ is $(m+p)$-regular.** Since $\mathcal{F} \otimes \mathcal{L}^{\otimes m}$ is globally generated, there exists a surjection

$$\mathcal{O}_X^{\oplus r_0} \twoheadrightarrow \mathcal{F} \otimes \mathcal{L}^{\otimes m}$$

for suitable $r_0$. Tensoring this with $\mathcal{L}^{\otimes p}$ yields

$$(\mathcal{L}^{\otimes p})^{\oplus r_0} \twoheadrightarrow \mathcal{F} \otimes \mathcal{L}^{\otimes m+p}.$$

Hence, if $H^i(X, \mathcal{L}^{\otimes p}) = 0$ for any $i > 0$ and $p \geq 0$, then $H^i(\mathcal{F} \otimes \mathcal{L}^{\otimes m+p}) = 0$ holds. For $p = 0$, $H^i(\mathcal{F} \otimes \mathcal{L}^{\otimes m}) = 0$ ($i > 0$) is exactly the definition of $m$-regularity of $\mathcal{F}$. For $p \geq 1$, since $\mathcal{L}$ is ample, $H^i(\mathcal{L}^{\otimes p}) = 0$ for sufficiently large $p$ by [Proposition 4](#prop4), but for small $p$ this factor may not vanish.

To resolve this, we use induction on $p$. For $p = 0$, the $m$-regularity of $\mathcal{F}(m)$ is the definition. Assume $p \geq 1$, and let us show that $\mathcal{F}(m+p)$ is $(m+p)$-regular, i.e. $H^i(\mathcal{F} \otimes \mathcal{L}^{\otimes m+p-i}) = 0$ ($i > 0$). For $i = 1$, substituting $k = m + p - 1$ into the restriction sequence gives

$$H^0(\mathcal{F}\vert_D \otimes (\mathcal{L}\vert_D)^{\otimes m+p-1}) \rightarrow H^1(\mathcal{F} \otimes \mathcal{L}^{\otimes m+p-2}) \rightarrow H^1(\mathcal{F} \otimes \mathcal{L}^{\otimes m+p-1}).$$

By the inductive hypothesis (for $p-1$), $H^1(\mathcal{F} \otimes \mathcal{L}^{\otimes m+p-2}) = 0$. Also, since $\mathcal{F}\vert_D$ is $m$-regular (Step 2), the inductive hypothesis on dimension implies that $\mathcal{F}\vert_D \otimes (\mathcal{L}\vert_D)^{\otimes p}$ is $(m+p)$-regular, and therefore $H^1(\mathcal{F}\vert_D \otimes (\mathcal{L}\vert_D)^{\otimes m+p-1}) = 0$. From the exact sequence, $H^1(\mathcal{F} \otimes \mathcal{L}^{\otimes m+p-1})$ embeds into $H^1(\mathcal{F}\vert_D \otimes (\mathcal{L}\vert_D)^{\otimes m+p-1})$, so we obtain $H^1(\mathcal{F} \otimes \mathcal{L}^{\otimes m+p-1}) = 0$. For $i \geq 2$, from the same restriction sequence we have

$$H^{i-1}(\mathcal{F}\vert_D \otimes (\mathcal{L}\vert_D)^{\otimes m+p-i}) \rightarrow H^i(\mathcal{F} \otimes \mathcal{L}^{\otimes m+p-i-1}) \rightarrow H^i(\mathcal{F} \otimes \mathcal{L}^{\otimes m+p-i}) \rightarrow H^i(\mathcal{F}\vert_D \otimes (\mathcal{L}\vert_D)^{\otimes m+p-i}).$$

By the inductive hypothesis, $H^i(\mathcal{F} \otimes \mathcal{L}^{\otimes m+p-i-1}) = 0$ (the hypothesis for $p' = p-1$, $j = i$), and by the inductive hypothesis for $\mathcal{F}\vert_D$ (induction on dimension), $H^{i-1}(\mathcal{F}\vert_D \otimes (\mathcal{L}\vert_D)^{\otimes m+p-i}) = 0$ and $H^i(\mathcal{F}\vert_D \otimes (\mathcal{L}\vert_D)^{\otimes m+p-i}) = 0$ hold for $i-1 \geq 1$, $i \leq n-1$. Therefore we obtain $H^i(\mathcal{F} \otimes \mathcal{L}^{\otimes m+p-i}) = 0$.
:::

::: Example 8
Let us compute the regularity of the line bundle $\mathcal{O}(d)$ on $\mathbb{P}^n$. Here $\mathcal{L} = \mathcal{O}(1)$, so twisting is $\mathcal{O}(d) \otimes \mathcal{O}(m) = \mathcal{O}(d+m)$. The $m$-regularity condition is $H^i(\mathbb{P}^n, \mathcal{O}(d+m-i)) = 0$ ($i > 0$). If $d \geq 0$ and we choose $m = 0$, we must check $H^i(\mathcal{O}(d-i))$; for $i = 1$, $H^1(\mathcal{O}(d-1))$ is $0$ when $d \geq 1$, and when $d = 0$, $H^1(\mathcal{O}(-1)) = 0$ (by Bott's formula, since $-1 \geq -n$, all cohomology is $0$). In general, if $d \geq 0$ and $i > 0$, then $d - i \geq -n$ implies $H^i(\mathcal{O}(d-i)) = 0$, and if $d - i < -n$, i.e. $i > d + n$, then $i > n$ and hence $H^i = 0$ anyway. Therefore $\mathcal{O}(d)$ is $0$-regular with respect to $\mathcal{L} = \mathcal{O}(1)$. On the other hand, if $d < 0$, then $\mathcal{O}(d)$ is $(-d)$-regular. By [Proposition 7](#prop7), $\mathcal{O}(d) \otimes \mathcal{L}^{\otimes 0} = \mathcal{O}(d)$ is globally generated when $d \geq 0$, which agrees with what was verified in [§Line Bundles and Vector Bundles, ⁋Example 16](/en/math/algebraic_varieties/line_bundles#ex16).
:::

## Properties of Very Ample and Ample

The above [Proposition 4](#prop4) and [Proposition 7](#prop7) are representative results on the properties of ample line bundles. We conclude this post by examining additional properties of ample and very ample line bundles.

::: Proposition 9
If $\mathcal{L}$ is very ample and $\mathcal{M}$ is globally generated, then $\mathcal{L} \otimes \mathcal{M}$ is very ample.
:::

::: Proof
Since $\mathcal{L}$ is very ample, there exists a projective embedding $i: X \hookrightarrow \mathbb{P}^N$ such that $\mathcal{L} = i^\ast\mathcal{O}_{\mathbb{P}^N}(1)$. On the other hand, since $\mathcal{M}$ is globally generated, there are global sections $s_0, \ldots, s_n \in H^0(X, \mathcal{M})$ that generate the stalk at every point, and from these we can define a morphism $\phi: X \rightarrow \mathbb{P}^n$.

Now consider the closed embedding $(i, \phi): X \rightarrow \mathbb{P}^N \times \mathbb{P}^n$. Composing this with the Segre embedding ([§Projective Varieties, ⁋Example 16](/en/math/algebraic_varieties/projective_varieties#ex16))

$$\sigma: \mathbb{P}^N \times \mathbb{P}^n \hookrightarrow \mathbb{P}^{Nn+N+n}$$

we have $\sigma^\ast\mathcal{O}(1) = \pi_1^\ast\mathcal{O}(1) \otimes \pi_2^\ast\mathcal{O}(1)$, so

$$(\sigma \circ (i, \phi))^\ast\mathcal{O}(1) = i^\ast\mathcal{O}(1) \otimes \phi^\ast\mathcal{O}(1) = \mathcal{L} \otimes \mathcal{M}.$$

Hence $\mathcal{L} \otimes \mathcal{M}$ is very ample.
:::

That is, although the explanation was somewhat involved, the gist is that the morphism $\phi:X\rightarrow \mathbb{P}^n$ defined by a globally generated line bundle $\mathcal{M}$ need not be a closed embedding, but by tensoring with $\mathcal{L}$ and mapping into projective space in the form $(i,\phi)$, the first component $i$ makes this map a closed embedding. From this, the following useful result can also be proved.

::: Proposition 10
Let $X$ be a projective variety, $\mathcal{L}$ an ample line bundle on $X$, and $\mathcal{M}$ an arbitrary line bundle. Then for sufficiently large $n$, the bundle $\mathcal{M} \otimes \mathcal{L}^{\otimes n}$ is very ample.
:::

::: Proof
First, since $\mathcal{L}$ is ample, $\mathcal{L}^{\otimes m}$ is very ample for some $m>0$. On the other hand, by [Proposition 4](#prop4) we can choose $k$ sufficiently large so that the higher cohomology of $\mathcal{M}\otimes \mathcal{L}^{\otimes k}$ vanishes; for such $k$, the sheaf $\mathcal{M}\otimes \mathcal{L}^{\otimes k}$ is globally generated. Now by [Proposition 9](#prop9),

$$(\mathcal{M} \otimes \mathcal{L}^{\otimes k}) \otimes \mathcal{L}^{\otimes m} = \mathcal{M} \otimes \mathcal{L}^{\otimes (k+m)}$$

is very ample, and setting $n = k + m$ completes the proof.
:::

---

**References**

**[Hart]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Bot]** R. Bott, *Homogeneous vector bundles*, Annals of Mathematics, 1957.  
**[Laz]** R. Lazarsfeld, *Positivity in Algebraic Geometry I*, Ergebnisse der Mathematik, Springer, 2004.  
**[Mum]** D. Mumford, *Lectures on Curves on an Algebraic Surface*, Annals of Mathematics Studies, Princeton, 1966.
