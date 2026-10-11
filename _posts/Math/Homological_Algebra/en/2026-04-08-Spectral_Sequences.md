---
title: "Spectral Sequences"
description: "We introduce the formal definition of a spectral sequence that approximates the cohomology of a complex equipped with a filtration page by page, and discuss the concepts of decreasing filtrations and filtered complexes."
excerpt: "Spectral sequence approximating the cohomology of a filtered complex page by page"

categories: [Math / Homological Algebra]
permalink: /en/math/homological_algebra/spectral_sequences
sidebar:
    nav: "homological_algebra-en"

date: 2026-04-08
weight: 7
translated_at: 2026-05-31T15:00:06+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-11T11:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
In the previous post, in proving the balancing of $\Ext$ and $\Tor$, we made useful use of filtrations and induction based on them. This can be regarded as a primitive form of the spectral sequence we discuss in this post. A spectral sequence is a systematic method for approximating the cohomology of a cochain complex equipped with a filtration, step by step through pages. Let us formally define these data.

## Spectral Sequences

::: Definition 1
A *spectral sequence* is a collection of the following data.

1. A bigraded object $E_r=(E_r^{p,q})_{p,q}$,
2. On $E_r$, a bidegree $(r,1-r)$ differential $d_r:E_r^{p,q}\rightarrow E_r^{p+r, q-r+1}$ (i.e., $d_r^2=0$)

For each $r$, the bigraded complex $(E_r^{p,q}, d_r)$ is called the *$r$-th page*. Here, these two pieces of data are connected via the following formula:

$$E_{r+1}^{p,q}\cong \frac{\ker(d_r^{p,q}: E_r^{p,q}\rightarrow E_r^{p+r,q-r+1})}{\im(d_r^{p-r,q+r-1}: E_r^{p-r, q+r-1}\rightarrow E_r^{p,q})}$$
:::

If we visualize the elements of the $E_r$ page as points $(p,q)$ in the plane, then $d_r^{p,q}$ goes from the point $(p,q)$ to $(p+r, q-r+1)$, and these points form a cochain complex. In particular, from this viewpoint, $E_{r+1}^{p,q}$ can be regarded as the cohomology at the point $(p,q)$ of the cochain complex passing through $(p,q)$.

Drawing on our experience, if we view a spectral sequence as the total complex of some double complex, then the differentials on each of these pages can be thought of as analyzing in detail each component of the differential on the total complex, namely

$$d^n:\bigoplus_{p+q=n}C^{p,q}\rightarrow \bigoplus_{p+q=n+1}C^{p,q}$$

Our main goal was to analyze this and ultimately compute the homology of this total complex; toward this end, in the proof of [§Ext and Tor, ⁋Proposition 3](/en/math/homological_algebra/ext_and_tor#prop3){: data-lid="m6bwa" } we previously defined a filtration using the horizontal/vertical degrees of the total complex $A^\bullet=\Tot(K)^\bullet$. Thus we need to introduce the notion of a *filtered complex* in greater generality.

## Filtrations

As mentioned above, the following [Definition 2](#def2){: data-lid="4s5zq" } can be thought of as a much more generalized version than this, but in any case, the philosophy itself of decomposing a complex more finely may be regarded as the same.

::: Definition 2
On a cochain complex $A^\bullet$, a *decreasing filtration* $F$ is defined by the condition

$$\cdots \supset F^{p-1}A^\bullet \supset F^pA^\bullet \supset F^{p+1}A^\bullet \supset \cdots$$

to be a sequence of subcomplexes $(F^p A^\bullet)_p$. In this case, a cochain complex equipped with a (decreasing) filtration is called a *filtered complex*, denoted $(A^\bullet, F)$.
:::

In particular, from the assumption that $F^p A^\bullet$ is a subcomplex of $A^\bullet$, $F^pA^\bullet$ inherits the differential from $A^\bullet$, and the cohomology with respect to it is also well-defined. In any case, intuitively, as $p$ increases, $F^p A^\bullet$ becomes smaller and smaller, and one can understand that new information is added at each stage. In the proof of [§Ext and Tor, ⁋Proposition 3](/en/math/homological_algebra/ext_and_tor#prop3){: data-lid="zgtf7" } above, we considered $F^pA^\bullet/F^{p+1}A^\bullet$ in order to apply induction and identified this with the original double complex $K^{p, \bullet-p}$; in the general case too, this information is important in that it *exactly* captures the $p$-th filtration step. The cochain complex obtained in this way,

$$\gr^p A^\bullet = F^p A^\bullet / F^{p+1} A^\bullet$$

is called the *associated graded complex* with respect to $F$. Here, the differential of this complex of course comes from the differential on the original cochain complex $A^\bullet$.

The most important fact about a filtration is that when a filtered complex $A^\bullet$ is given, the filtration is naturally defined at the cohomology level as well. We will use this filtration to define the convergence of the spectral sequence induced from a filtered complex.

::: Definition 3
Let $(A^\bullet, F)$ be a filtered complex. Then the image of the inclusion $F^pA^\bullet\rightarrow A^\bullet$ at the cohomology level is defined by

$$F^p H^n = \im\bigl(H^n(F^p A^\bullet) \rightarrow H^n(A^\bullet)\bigr)$$
:::

This filtration consists of the cohomology classes induced by cocycles contained in $F^p A^\bullet$. As $p$ increases, $F^p A^\bullet$ becomes smaller, so $F^p H^n$ also becomes smaller.

## Convergence of Spectral Sequences

Now we explain the convergence of spectral sequences. Intuitively, since each page $E_r^{p,q}$ of a spectral sequence is an object that is progressively refined as $r$ increases, we must examine what this approximation ultimately converges to. Therefore, we first define the following.

::: Definition 4
A spectral sequence $\{E_r^{p,q}, d_r\}$ is *regular* if for each $(p,q)$, for all sufficiently large $r$, $E_r^{p,q} = E_{r+1}^{p,q}$ holds. In this case, the stabilized value is defined as $E_\infty^{p,q}$.
:::

Since regularity means that the pages of the spectral sequence no longer change at each bidegree, it enables the following definition.

::: Definition 5
A spectral sequence $\{E_r^{p,q}, d_r\}$ *converges* to a filtered graded object $(H^n, F)$ if for each $(p,q)$,

$$E_\infty^{p,q} \cong F^p H^{p+q} / F^{p+1} H^{p+q} = \gr^p H^{p+q}$$

holds. In notation, we write this as $E_r^{p,q} \Rightarrow H^{p+q}$.
:::

Again, thinking of the familiar example of the total complex of a double complex, this can be regarded as a generalization of how the homology of the total complex was obtained when we imposed the horizontal filtration on the double complex and sent $p$ to $0$.

If for each $n$ we have $\bigcap_p F^p H^n = 0$ (Hausdorff condition), $\bigcup_p F^p H^n = H^n$ (exhaustive condition), and the spectral sequence is regular, then the $E_\infty^{p,q}$ describe the graded pieces of the filtration on $H^n$ without omission. When these three conditions are satisfied, the spectral sequence is said to *strongly converge* to $(H^n, F)$. On the other hand, if even one of these three conditions is not satisfied, it is said to *weakly converge*, and in this case $E_\infty^{p,q}$ alone cannot uniquely determine $H^n$.

In general, regularity of a spectral sequence does not always hold. However, if for all $r$, the $E_r^{p,q}$ exist only in the first quadrant, that is, if only when $p,q\geq 0$ is $E_r^{p,q}\neq 0$ possible, then when $d_r$ is taken sufficiently many times, the point exits toward the second or fourth quadrant and goes to $0$, so it is always regular. That is, the following holds.

::: Proposition 6
A first quadrant spectral sequence, that is, a spectral sequence such that if $p < 0$ or $q < 0$, then for $(p,q)$ we have $E_r^{p,q} = 0$, is always regular. Moreover, when such a spectral sequence converges as $E_r^{p,q} \Rightarrow H^{p+q}$, for each $(p,q)$, for sufficiently large $r$, $E_r^{p,q} = E_\infty^{p,q}$ holds.
:::

## Filtrations and Spectral Sequences

Until now, we have satisfied our intuition by considering the total complex of a double complex and the spectral sequence associated with it, but the connection remains somewhat unclear in that we do not yet know what spectral sequence this total complex defines. In this section, we explain a concrete method for constructing a spectral sequence from an arbitrary filtered complex. In particular, in [§Ext and Tor, ⁋Proposition 3](/en/math/homological_algebra/ext_and_tor#prop3){: data-lid="z3dcw" }, the objects on both sides correspond to the spectral sequences given by the filtrations placed in the vertical and horizontal directions, respectively, and that these converge to the same object is the basic idea of that proof.

Let $(A^\bullet, F)$ be a filtered complex. Then we can directly construct the $E_0$ page via the formula

$$E_0^{p,q} = \gr^p A^{p+q} = F^p A^{p+q} / F^{p+1} A^{p+q}$$

Now let us define the differential on this precisely. First, since the filtration preserves the differential, from this

$$F^p A^{p+q}\rightarrow F^p A^{p+q+1}$$

is defined. For convenience, let us write this as $F^p d$. Then the desired differential is obtained by composing $F^p d$ with the quotient

$$F^pA^{p+q+1}\rightarrow F^pA^{p+q+1}/F^{p+1}A^{p+q+1}$$

and then using the first isomorphism theorem to factor this through as

$$F^p A^{p+q}/F^{p+1}A^{p+q}\rightarrow F^pA^{p+q+1}/F^{p+1}A^{p+q+1}$$

Here, the first isomorphism theorem applies well: if $a \in F^{p+1}A^{p+q}$, then $\dd{(a)} \in F^{p+1}A^{p+q+1}$, so in the codomain quotient $F^p A^{p+q+1}/F^{p+1}A^{p+q+1}$ it maps to $0$.

More generally, on the $E_r$ page, the differential $d_r$ is also defined in a similar manner. Essentially, since $E_r^{p,q}$ is formed by taking quotients of $F^pA^{p+q}$ in multiple stages, an element of $E_r^{p,q}$ can be thought of, for some element $x\in F^pA^{p+q}$, as a suitable equivalence class $[x]$. Now, $d_r^{p,q}: E_r^{p,q}\rightarrow E_r^{p+r, q-r+1}$ is given by the formula

$$d_r^{p,q}([x])=[\dd{x}]\in E_r^{p+r, q-r+1}\tag{$\ast$}$$

Of course, showing that this correspondence is well-defined and defines a differential requires somewhat complicated calculations ([link](https://stacks.math.columbia.edu/tag/012K)), but what is important is that the elements of $E_r^{p,q}$ can be defined by the following two conditions:

- $\dd{x}\in F^{p+r}A^{p+q+1}$, and
- if the difference of $x,y\in F^{p}A^{p+q}$ can be written as the sum of a boundary of the $r-1$-th stage and an element of $F^{p+1}A^{p+q}$, then $x,y$ are treated as the same.

In particular, what ($\ast$) tells us is that all the $d_r$ are essentially the same as $d$, and the index $r$ is used only to measure how far across the filtration one jumps. That is, the following holds.

::: Proposition 7
From a filtered complex $(A^\bullet, F)$, the $E_r^{p,q}$ and $d_r$ constructed above satisfy the conditions of a spectral sequence in [Definition 1](#def1){: data-lid="4ju1l" }. That is,

$$d_r \circ d_r = 0$$

holds, and $E_{r+1}^{p,q} \cong H(E_r, d_r)$.
:::

Moreover, the spectral sequence defined in this way also has a kind of functoriality.

::: Proposition 8
Let $f : (A^\bullet, F) \rightarrow (B^\bullet, G)$ be a chain map between filtered complexes, and further suppose that for each $p$,

$$f(F^p A^\bullet) \subseteq G^p B^\bullet$$

holds. Then $f$ induces a well-defined morphism $f_r : E_r(A) \rightarrow E_r(B)$ for each $r$.
:::
::: Proof
Since $f$ is a chain map, it sends cocycles to cocycles and boundaries to boundaries. Also, since $f(F^p) \subseteq G^p$, we have $f(Z_r^{p,q}(A)) \subseteq Z_r^{p,q}(B)$ and $f(B_r^{p,q}(A)) \subseteq B_r^{p,q}(B)$. Therefore $f$ induces a well-defined map on $E_r$ for each $r$.
:::

Then our key result is that such a spectral sequence actually reaches the cohomology of the original complex. Let us first define the following.

::: Definition 9
A filtered complex $(A^\bullet, F)$ is *bounded* if for each $n$ there exists a sufficiently large $p$ such that $F^pA^n=0$, and a sufficiently small $p$ such that $F^pA^n=A^n$.
:::

That is, fixing [Definition 2](#def2){: data-lid="pviw6" } at degree $n$ and starting the filtration

$$\cdots\supset F^{p-1}A^n\supset F^p A^n \supset F^{p+1}A^n\supset\cdots$$

here, this means that this filtration is bounded. Then, since for each $(p,q)$ there exists $(m, n)$ such that $F^nA^{p+q}=A^{p+q}$ and $F^mA^{p+q}=0$, for a fixed $(p,q)$, if we take $r$ large enough that the differential $d_r$ leaves this interval, one can verify that a bounded filtered complex is regular.

Moreover, from the above description of the elements of $E_r^{p,q}$ we can show that

$$E_\infty^{p,q}\cong F^p H^{p+q}(A^\bullet)/F^{p+1}H^{p+q}(A^\bullet)$$

and from this we obtain the following result.

::: Proposition 10
Let $(A^\bullet, F)$ be a bounded filtered complex, and let $(E_r^{p,q})$ be the spectral sequence it defines. Then $(E_r^{p,q})$ converges to the filtered graded object $(H^\bullet, F)$ of [Definition 3](#def3){: data-lid="1nm6o" }. That is, $E_r^{p,q}\Rightarrow H^{p+q}(A^\bullet)$.
:::

## Spectral Sequences of Double Complexes

So far, we have taken [§Ext and Tor, ⁋Proposition 3](/en/math/homological_algebra/ext_and_tor#prop3){: data-lid="pysxe" }, where we proved the balancing of $\Ext$ and $\Tor$, as the motivation for our theory. We conclude this post by examining the spectral sequence defined from a double sequence.

::: Example 11
Consider the total complex $\Tot(K)^\bullet$ of an arbitrary double complex $K^{p,q}$. We can define a filtration on this total complex in two ways.

First, let us define the *vertical filtration* by

$$F^p_v \Tot(K)^n = \bigoplus_{j \geq p} K^{n-j, j}$$

Since the associated graded object for this filtration is $\mathrm{gr}^p_v \Tot(K)^{p+q} = K^{q,p}$, the $E_0$ page is

$$E_0^{p,q} = K^{q,p}$$

and $d_0$ is a differential of bidegree $(0,1)$, given by the horizontal differential $d_h$. Therefore, the $E_1$ page is

$$E_1^{p,q} = H^q_h(K^{\bullet,p})$$

and $d_1$ on the $E_1$ page is a differential of bidegree $(1,0)$, induced by the vertical differential $d_v$. On the other hand, this time if we define the *horizontal filtration* by

$$F^p_h \Tot(K)^n = \bigoplus_{i \geq p} K^{i, n-i}$$

then similarly the $E_0$ page is

$$E_0^{p,q} = K^{p,q}$$

and $d_0$ is given by the vertical differential $d_v$. Therefore, the $E_1$ page is

$$E_1^{p,q} = H^q_v(K^{p,\bullet})$$

and $d_1$ is induced by the horizontal differential $d_h$.
:::

In particular, let $K^{p,q}$ be a first quadrant double complex. Then both filtrations define bounded filtered complexes, so by [Proposition 10](#prop10){: data-lid="sqlml" } each spectral sequence converges to $H^\bullet(\Tot(K))$. From this we can recover the proof of [§Ext and Tor, ⁋Proposition 3](/en/math/homological_algebra/ext_and_tor#prop3){: data-lid="31ppi" } in fancier language.

---

**References**

**[GM]** S. I. Gelfand, Y. I. Manin, *Methods of homological algebra*, Springer, 2003.  
**[Wei]** C. A. Weibel, *An introduction to homological algebra*, Cambridge University Press, 1994.  
**[God]** R. Godement, *Topologie algébrique et théorie des faisceaux*, Hermann, 1958.
