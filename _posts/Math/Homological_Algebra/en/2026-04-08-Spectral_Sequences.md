---
title: "Spectral Sequences"
description: "We introduce the formal definition of a spectral sequence that approximates the cohomology of a filtered complex page by page, and discuss the concepts of decreasing filtrations and filtered complexes."
excerpt: "Spectral sequences that approximate the cohomology of a filtered complex page by page"

categories: [Math / Homological Algebra]
permalink: /en/math/homological_algebra/spectral_sequences
header:
    overlay_image: /assets/images/Math/Homological_Algebra/Spectral_Sequences.png
    overlay_filter: 0.5
sidebar:
    nav: "homological_algebra-en"

date: 2026-04-08
last_modified_at: 2026-04-12
weight: 7
translated_at: 2026-05-31T15:00:06+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-31T15:00:06+00:00
---
In the previous post, we used filtrations and induction to prove the balancing of $$\Ext$$ and $$\Tor$$. This can be regarded as a primitive form of the spectral sequence we discuss here. A spectral sequence is a systematic device for approximating the cohomology of a cochain complex equipped with a filtration, proceeding through successive pages. Let us formally define this structure.

## Spectral Sequences

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A *spectral sequence* is a collection of the following data.

1. A bigraded object $$E_r=(E_r^{p,q})_{p,q}$$,
2. A differential $$d_r$$ on $$E_r$$ of bidegree $$(r,1-r)$$, i.e., $$d_r:E_r^{p,q}\rightarrow E_r^{p+r, q-r+1}$$ (so that $$d_r^2=0$$)

For each $$r$$, the bigraded complex $$(E_r^{p,q}, d_r)$$ is called the *$$r$$-th page*. These two pieces of data are related by the formula

$$E_{r+1}^{p,q}\cong \frac{\ker(d_r^{p,q}: E_r^{p,q}\rightarrow E_r^{p+r,q-r+1})}{\im(d_r^{p-r,q+r-1}: E_r^{p-r, q+r-1}\rightarrow E_r^{p,q})}$$

</div>

If we visualize the elements of the $$E_r$$ page as points $$(p,q)$$ in the plane, then $$d_r^{p,q}$$ goes from $$(p,q)$$ to $$(p+r, q-r+1)$$, and these arrows form a cochain complex. In particular, from this viewpoint $$E_{r+1}^{p,q}$$ can be regarded as the cohomology at the point $$(p,q)$$ of the cochain complex passing through $$(p,q)$$.

Drawing on our experience, if we view a spectral sequence as arising from the total complex of some double complex, then the differentials on each page can be thought of as a careful analysis of the components of the differential on the total complex, namely

$$d^n:\bigoplus_{p+q=n}C^{p,q}\rightarrow \bigoplus_{p+q=n+1}C^{p+q}$$

We analyzed this, and our main goal was ultimately to compute the homology of this total complex. Toward this end, in the proof of [§Ext and Tor, ⁋Proposition 3](/en/math/homological_algebra/ext_and_tor#prop3) we defined a filtration using the horizontal and vertical degrees of the total complex $$A^\bullet=\Tot(K)^\bullet$$. Thus we need to introduce the notion of a *filtered complex* in greater generality.

## Filtrations

As mentioned above, the following [Definition 2](#def2) is a much more general version, but the philosophy of decomposing a complex more finely remains essentially the same.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> A *decreasing filtration* $$F$$ on a cochain complex $$A^\bullet$$ is a sequence of subcomplexes $$(F^p A^\bullet)_p$$ satisfying

$$\cdots \supset F^{p-1}A^\bullet \supset F^pA^\bullet \supset F^{p+1}A^\bullet \supset \cdots$$

A cochain complex equipped with a (decreasing) filtration is called a *filtered complex*, denoted $$(A^\bullet, F)$$.

</div>

In particular, since each $$F^p A^\bullet$$ is a subcomplex of $$A^\bullet$$, the differential of $$A^\bullet$$ restricts to $$F^pA^\bullet$$ and the cohomology with respect to this restricted differential is well defined. Intuitively, as $$p$$ increases, $$F^p A^\bullet$$ becomes smaller, and one can understand that new information is added at each stage. In the proof of [§Ext and Tor, ⁋Proposition 3](/en/math/homological_algebra/ext_and_tor#prop3) above, we considered $$F^{p+1}A^\bullet/F^pA^\bullet$$ in order to apply induction and identified this with the original double complex $$K^{p, \bullet-p}$$; in the general case too, this information is important in that it *exactly* captures the $$p$$-th filtration step. The cochain complex obtained in this way,

$$\gr^p A^\bullet = F^p A^\bullet / F^{p+1} A^\bullet$$

is called the *associated graded complex* with respect to $$F$$. Of course, the differential on this complex is induced from that of the original cochain complex $$A^\bullet$$.

The most important fact about a filtration is that when a filtered complex $$A^\bullet$$ is given, the filtration descends naturally to the cohomology level as well. We will use this filtration to define the convergence of the spectral sequence induced from a filtered complex.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> Let $$(A^\bullet, F)$$ be a filtered complex. The image at the cohomology level of the inclusion $$F^pA^\bullet\rightarrow A^\bullet$$ is defined by

$$F^p H^n = \operatorname{im}\bigl(H^n(F^p A^\bullet) \to H^n(A^\bullet)\bigr)$$

</div>

This filtration consists of the cohomology classes induced by cocycles contained in $$F^p A^\bullet$$. As $$p$$ increases, $$F^p A^\bullet$$ becomes smaller, so $$F^p H^n$$ also becomes smaller.

## Convergence of Spectral Sequences

Now we explain the convergence of spectral sequences. Intuitively, since each page $$E_r^{p,q}$$ of a spectral sequence is an object that is progressively refined as $$r$$ increases, we must examine what this approximation ultimately converges to. We therefore begin with the following definition.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> A spectral sequence $$\{E_r^{p,q}, d_r\}$$ is *regular* if for each $$(p,q)$$, we have $$E_r^{p,q} = E_{r+1}^{p,q}$$ for all sufficiently large $$r$$. The stabilized value is then denoted $$E_\infty^{p,q}$$.

</div>

Since regularity means that the pages of the spectral sequence no longer change at each bidegree, it enables the following definition.

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> A spectral sequence $$\{E_r^{p,q}, d_r\}$$ *converges* to a filtered graded object $$(H^n, F)$$ if for each $$(p,q)$$,

$$E_\infty^{p,q} \cong F^p H^{p+q} / F^{p+1} H^{p+q} = \gr^p H^{p+q}$$

holds. We write this as $$E_r^{p,q} \Rightarrow H^{p+q}$$.

</div>

Again, thinking of the familiar example of the total complex of a double complex, this can be regarded as a generalization of the phenomenon that the homology of the total complex emerges when we impose the horizontal filtration on the double complex and send $$p$$ to $$0$$.

If for each $$n$$ we have $$\bigcap_p F^p H^n = 0$$ (Hausdorff condition), $$\bigcup_p F^p H^n = H^n$$ (exhaustive condition), and the spectral sequence is regular, then one can uniquely reconstruct $$H^n$$ from the information of the successive quotients $$\gr^p H^{p+q}$$. When these three conditions are satisfied, the spectral sequence is said to *strongly converge* to $$(H^n, F)$$. On the other hand, if any one of these three conditions fails, it is said to *weakly converge*, and in this case $$E_\infty^{p,q}$$ alone cannot uniquely determine $$H^n$$.

In general, regularity of a spectral sequence does not always hold. However, if for all $$r$$ the terms $$E_r^{p,q}$$ are supported only in the first quadrant, that is, if $$E_r^{p,q}\neq 0$$ is possible only when $$p,q\geq 0$$, then for sufficiently large $$r$$ the differential $$d_r$$ sends any given point into the second or fourth quadrant, where it vanishes; hence the spectral sequence is always regular. That is, the following holds.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> A first quadrant spectral sequence, i.e., one for which $$E_r^{p,q} = 0$$ whenever $$p < 0$$ or $$q < 0$$, is always regular. Moreover, when such a spectral sequence converges as $$E_r^{p,q} \Rightarrow H^{p+q}$$, for each $$(p,q)$$ we have $$E_r^{p,q} = E_\infty^{p,q}$$ for all sufficiently large $$r$$.

</div>

## Filtrations and Spectral Sequences

Until now, we have guided our intuition by thinking of the total complex of a double complex and the spectral sequence associated to it, but the connection remains somewhat unclear because we have not yet identified the spectral sequence that this total complex actually defines. In this section we explain the concrete construction of a spectral sequence from an arbitrary filtered complex. In particular, in the proof of [§Ext and Tor, ⁋Proposition 3](/en/math/homological_algebra/ext_and_tor#prop3), the objects on the two sides correspond to the spectral sequences arising from the filtrations taken in the vertical and horizontal directions, respectively, and the basic idea of the proof is that these converge to the same object.

Let $$(A^\bullet, F)$$ be a filtered complex. We construct the $$E_0$$ page directly by the formula

$$E_0^{p,q} = \gr^p A^{p+q} = F^p A^{p+q} / F^{p+1} A^{p+q}$$

Now let us define the differential on this precisely. First, since the filtration preserves the differential, we obtain

$$F^p A^{p+q}\rightarrow F^p A^{p+q+1}$$

Let us denote this by $$F^p d$$ for convenience. Then the desired differential is obtained by composing $$F^p d$$ with the quotient

$$F^pA^{p+q+1}\rightarrow F^pA^{p+q+1}/F^{p+1}A^{p+q+1}$$

and then using the first isomorphism theorem to factor this through as

$$F^p A^{p+q}/F^{p+1}A^{p+q}\rightarrow F^pA^{p+q+1}/F^{p+1}A^{p+q+1}$$

Here the first isomorphism theorem applies cleanly: if $$a \in F^{p+1}A^{p+q}$$, then $$d(a) \in F^{p+1}A^{p+q+1}$$, so it maps to $$0$$ in the codomain quotient $$F^p A^{p+q+1}/F^{p+1}A^{p+q+1}$$.

More generally, the differential $$d_r$$ on the $$E_r$$ page is defined in a similar manner. Essentially, since $$E_r^{p,q}$$ is constructed by taking successive quotients of $$F^pC^{p+q}$$, an element of $$E_r^{p,q}$$ can be represented by a suitable equivalence class $$[x]$$ of some element $$x\in F^pC^{p+q}$$. Then $$d_r^{p,q}: E_r^{p,q}\rightarrow E_r^{p+r, q-r+1}$$ is given by the formula

$$d_r^{p,q}([x])=[dx]\in E_r^{p+r, q-r+1}\tag{$\ast$}$$

Of course, verifying that this correspondence is well defined and actually defines a differential requires somewhat involved calculations ([link](https://stacks.math.columbia.edu/tag/012K)), but what matters is that the elements of $$E_r^{p,q}$$ can be characterized by the following two conditions:

- $$dx\in F^{p+r}C^{p+q+1}$$, and
- If $$x,y\in F^{p+r}C^{p+q}$$ differ only by a boundary of the $$(r-1)$$-th stage, then $$x$$ and $$y$$ are identified.

In particular, what ($$\ast$$) reveals is that all the $$d_r$$ are essentially the same map as $$d$$, and the index $$r$$ serves only to measure how far across the filtration one jumps. That is, the following holds.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> The $$E_r^{p,q}$$ and $$d_r$$ constructed from a filtered complex $$(A^\bullet, F)$$ as above satisfy the conditions of a spectral sequence in [Definition 1](#def1). Namely,

$$d_r \circ d_r = 0$$

holds, and $$E_{r+1}^{p,q} \cong H(E_r, d_r)$$.

</div>

Moreover, the spectral sequence defined in this way also enjoys a form of functoriality.

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8**</ins> Let $$f : (A^\bullet, F) \to (B^\bullet, G)$$ be a chain map between filtered complexes. That is, for each $$p$$,

$$f(F^p A^\bullet) \subset G^p B^\bullet$$

holds. Then $$f$$ induces a well-defined map $$f_r : E_r(A) \to E_r(B)$$ for each $$r$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Since $$f$$ is a chain map, it sends cocycles to cocycles and boundaries to boundaries. Also, since $$f(F^p) \subset G^p$$, we have $$f(Z_r^{p,q}(A)) \subset Z_r^{p,q}(B)$$ and $$f(B_r^{p,q}(A)) \subset B_r^{p,q}(B)$$. Therefore $$f$$ induces a well-defined map on each $$E_r$$.

</details>

Our core result is that this spectral sequence actually reaches the cohomology of the original complex. Let us first define the following.

<div class="definition" markdown="1">

<ins id="def9">**Definition 9**</ins> A filtered complex $$(A^\bullet, F)$$ is *bounded* if for each $$n$$ there exists a sufficiently large $$p$$ with $$F^pA^n=0$$, and a sufficiently small $$p$$ with $$F^pA^n=A^n$$.

</div>

That is, fixing [Definition 2](#def2) in degree $$n$$ and considering the filtration

$$\cdots\supset F^{p-1}A^n\supset \cdots F^p A^n \supset \cdots F^{p+1}A^n\supset\cdots$$

there, this filtration is bounded. Then for each $$(p,q)$$ there exist $$(m, n)$$ such that $$F^nA^{p+q}=A^{p+q}$$ and $$F^mA^{p+q}=0$$, so for a fixed $$(p,q)$$, if we take $$r$$ large enough that the differential $$d_r$$ escapes this interval, one can verify that a bounded filtered complex is regular.

Moreover, from the above description of the elements of $$E_r^{p,q}$$ we can show that

$$E_\infty^{p,q}\cong F^p H^{p+q}(A^\bullet)/F^{p+1}H^{p+q}(A^\bullet)$$

and from this we obtain the following result.

<div class="proposition" markdown="1">

<ins id="prop10">**Proposition 10**</ins> Let $$(A^\bullet, F)$$ be a bounded filtered complex, and let $$(E_r^{p,q})$$ be the spectral sequence it defines. Then $$(E_r^{p,q})$$ converges to the filtered graded object $$(H^\bullet, F)$$ of [Definition 3](#def3). That is, $$E_r^{p,q}\Rightarrow H^{p+q}(A^\bullet)$$.

</div>

## Spectral Sequences of Double Complexes

We have taken the proof of the balancing of $$\Ext$$ and $$\Tor$$ in [§Ext and Tor, ⁋Proposition 3](/en/math/homological_algebra/ext_and_tor#prop3) as the motivation for our theory. We close this post by examining the spectral sequence defined from a double complex.

<div class="example" markdown="1">
    
<ins id="ex11">**Example 11**</ins> Consider the total complex $$\Tot(K)^\bullet$$ of an arbitrary double complex $$K^{p,q}$$. We can equip this total complex with a filtration in two ways.

First, define the *vertical filtration* by

$$F^p_v \Tot(K)^n = \bigoplus_{j \geq p} K^{n-j, j}$$

Then the associated graded object for this filtration is $$\mathrm{gr}^p_v \Tot(K)^{p+q} = K^{p,q}$$, so the $$E_0$$ page is

$$E_0^{p,q} = K^{p,q}$$

and $$d_0$$ is a derivation of degree $$(0,1)$$ given by the vertical differential $$d_v$$. Therefore the $$E_1$$ page is

$$E_1^{p,q} = H^q_v(K^{p,\bullet})$$

and the $$d_1$$ on the $$E_1$$ page is a derivation of degree $$(1,0)$$ induced by the horizontal differential $$d_h$$. On the other hand, if we define the *horizontal filtration* by

$$F^p_h \Tot(K)^n = \bigoplus_{i \geq p} K^{i, n-i}$$

then similarly the $$E_0$$ page is

$$E_0^{p,q} = K^{p,q}$$

and $$d_0$$ is given by the horizontal differential $$d_h$$. Therefore the $$E_1$$ page is

$$E_1^{p,q} = H^p_h(K^{\bullet, q})$$

and $$d_1$$ is induced by the vertical differential $$d_v$$.

</div>

In particular, let $$K^{p,q}$$ be a first quadrant double complex. Then both filtrations define bounded filtered complexes, so by [Proposition 10](#prop10) each spectral sequence converges to $$H^\bullet(\Tot(K))$$. From this we can reconstruct the proof of [§Ext and Tor, ⁋Proposition 3](/en/math/homological_algebra/ext_and_tor#prop3) in fancier language.

---

**References**

**[GM]** S. I. Gelfand, Y. I. Manin, *Methods of homological algebra*, Springer, 2003.
**[Wei]** C. A. Weibel, *An introduction to homological algebra*, Cambridge University Press, 1994.
**[God]** R. Godement, *Topologie algébrique et théorie des faisceaux*, Hermann, 1958.
