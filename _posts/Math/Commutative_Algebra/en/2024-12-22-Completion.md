---
title: "Completion"
description: "The completion of a ring is a construction that turns a ring into a complete ring via a given ideal filtration. It includes the definitions of adic completion and local complete rings, and satisfies a universal property as a categorical limit."
excerpt: "Completion of rings and modules defined by a filtration"

categories: [Math / Commutative Algebra]
permalink: /en/math/commutative_algebra/completion
sidebar: 
    nav: "commutative_algebra-en"

date: 2024-12-22
last_modified_at: 2024-12-22
weight: 14
translated_at: 2026-05-30T22:00:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-30T22:00:04+00:00
---
## Definition of Completion

Given an abelian group $$G$$ and a decreasing sequence of its subgroups

$$\mathcal{J}:\qquad G=H_0\supseteq H_1\supseteq\cdots$$

the quotient maps $$G/ H_{i+1} \rightarrow G/H_{i}$$ are well-defined, and more generally, by composing them appropriately, we obtain maps $$\rho_{ji}:G/H_j \rightarrow G/H_i$$ for all $$j>i$$. From these data we form the inverse limit

$$\widehat{G}_\mathcal{J}=\varprojlim_i G/H_i=\left\{(g_1,g_2,\ldots)\in \prod G/H_i\,\middle\vert\,\text{$\rho_{ji}(g_j)=g_i$ for all $j>i$}\right\}$$

together with the canonical morphisms $$\rho_i:\widehat{G}_{\mathcal{J}} \rightarrow G/ H_i$$, which satisfy $$\rho_{ji}\circ\rho_j=\rho_i$$ for all $$j>i$$. For notational convenience, when $$\mathcal{J}$$ is clear from context we simply write $$\widehat{G}$$.

These can be viewed as categorical limits, as we saw in [\[Category Theory\] §Limits, ⁋Example 5](/en/math/category_theory/limits#ex5), and therefore they also satisfy the following universal property.

> Whenever maps $$K \rightarrow G/H_i$$ satisfying $$\rho_{ji}\circ\pi_j=\pi_i$$ are given, there exists a unique $$\pi:K \rightarrow \widehat{G}$$ making the following diagram
> 
> ![universal_property](/assets/images/Math/Commutative_Algebra/Completion-1.png){:style="width:14em" class="invert" .align-center}
> 
> commute.

If $$G$$ is equipped with a ring structure and the $$H_i$$ are ideals, then $$\widehat{G}$$ naturally inherits a ring structure as well. The situation we shall study is the following.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Fix a ring $$A$$ and an ideal $$\mathfrak{a}$$. For an $$\mathfrak{a}$$-filtration of ideals of $$A$$

$$\mathcal{J}:\qquad A=\mathfrak{a}_0\supseteq \mathfrak{a}_1\supseteq \mathfrak{a}_2\cdots$$

we call

$$\widehat{A}=\varprojlim_i A/\mathfrak{a}_i$$

the *completion* of $$A$$ with respect to this filtration. If the natural map $$A \rightarrow \widehat{A}$$ is an isomorphism, we call $$A$$ a *complete ring* with respect to this filtration.

In particular, if the above filtration is given by

$$A\supseteq\mathfrak{a}\supseteq \mathfrak{a}^2\cdots$$

we call it the *$$\mathfrak{a}$$-adic completion* of $$A$$. In this case, if $$\mathfrak{a}$$ is a maximal ideal then $$\widehat{A}$$ becomes a local ring with unique maximal ideal $$\widehat{\mathfrak{a}}$$, so we call $$\widehat{A}$$ a *complete local ring*.

</div>

First, the natural map $$\rho:A \rightarrow \widehat{A}$$ is obtained by applying the universal property to the canonical morphisms $$\pr_i: A \rightarrow A/\mathfrak{a}_i$$. Then by definition

$$x\in\ker\rho\iff\rho(x)=0\iff \rho_i(\rho(x))=0\text{ for all $i$}\iff \pr_i(x)=0\text{ for all $i$}\iff x\in \mathfrak{a}_i\text{ for all $i$}$$

so $$\rho$$ is injective if and only if $$\bigcap \mathfrak{a}_i=0$$.

Now let us write $$\widehat{\mathfrak{a}}_i$$ for the kernel of the canonical morphism $$\rho_i:\widehat{A}\rightarrow A/\mathfrak{a}_i$$. Then by definition $$\mathfrak{a}_i=\rho^{-1}(\widehat{\mathfrak{a}}_i)$$, and since the $$\pr_i$$ are surjective and $$\pr_i=\rho_i\circ\rho$$, the $$\rho_i$$ are all surjective; hence by the first isomorphism theorem

$$\widehat{A}/\widehat{\mathfrak{a}}_i\cong A/\mathfrak{a}_i$$

holds. Therefore the descending chain of ideals of $$\widehat{A}$$

$$\widehat{A}=\widehat{\mathfrak{a}}_0\supseteq \widehat{\mathfrak{a}}_1\supseteq\cdots\tag{1}$$

is an $$\mathfrak{a}$$-filtration, and from the above isomorphism we have

$$\widehat{A}=\varprojlim_i A/\mathfrak{a}_i\cong\varprojlim_i \widehat{A}/\widehat{\mathfrak{a}}_i$$

so $$\widehat{A}$$ is complete with respect to the given filtration. Moreover, this isomorphism also yields

$$\gr_\mathcal{J}A\cong\gr_{\widehat{\mathcal{J}}}\widehat{A}.$$

## The $$\mathfrak{a}$$-adic Topology

On the other hand, the process of constructing $$\widehat{A}$$ from $$A$$ can also be understood by endowing $$A$$ with a special kind of topology. First, suppose a topological abelian group $$G$$ is given. Fixing an element $$g\in G$$, the translation map $$T_g$$ defined by it is continuous, so the neighborhood filter at each point of $$G$$ is completely determined by the neighborhood filter at $$0\in G$$. This process can, of course, be reversed.

As in the previous section, suppose a decreasing sequence of subgroups of $$G$$

$$G=H_0\supseteq H_1\supseteq\cdots$$

is given. Then defining

$$\mathcal{N}(0)=\{U\subseteq G\mid\text{$G_n\subseteq U$ for some $n$}\}$$

we know that this satisfies all the conditions of [\[Topology\] §Open Sets, ⁋Proposition 6](/en/math/topology/open_sets#prop6). Now for arbitrary $$g\in G$$ and $$U\in \mathcal{N}(0)$$, declaring $$g+U\in \mathcal{N}(g)$$ gives a topology on $$G$$.

In particular, applying this to the situation of [Definition 1](#def1), the topology defined by the above process is called the *$$\mathfrak{a}$$-adic topology*. In this case, $$0\in A$$ has the countable local base

$$\mathfrak{a}\supseteq \mathfrak{a}^2\supseteq\cdots\tag{2}$$

so the topology on $$A$$ thus defined is first countable.

Returning to a general topological abelian group $$G$$, we can weaken the conditions of [##ref##]() to define the following.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> For a topological group $$(G, +, 0)$$, a sequence $$(x_i)_{i\in \mathbb{N}}$$ of elements of $$G$$ is called a *Cauchy sequence* if for any neighborhood $$U$$ of $$0$$ there exists a natural number $$N$$ such that

$$m,n>N \implies x_m-x_n\in U$$

holds.

</div>

Then, just as in [##ref##]() where completion was defined as the set of equivalence classes of Cauchy filters, we can define when two Cauchy sequences $$(x_m)$$ and $$(y_n)$$ are regarded as the same, and through that define the (topological) completion. However, the object of our interest is the first countable topological group $$A$$ defined by the filtration (2) above, and since a first countable space is sequential, for convenience in the following definition we assume $$G$$ is a first countable space and use Cauchy sequences in place of Cauchy filters.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> Two Cauchy sequences $$(x_m)$$, $$(y_n)$$ of a topological group $$(G, +, 0)$$ are called *equivalent* if for any neighborhood $$U$$ of $$0$$ there exists a natural number $$N$$ such that

$$m,n>N \implies x_m-y_n\in U$$

holds. We call the set of equivalence classes of all Cauchy sequences of a first countable topological group $$G$$, equipped with this equivalence relation, the *completion* of $$G$$, and denote it by $$\widehat{G}$$.

</div>

Now for an open neighborhood $$U$$ of $$0\in G$$, define

$$\widehat{U}=\{[(x_n)]\in \widehat{G}:\text{for any $(y_n)\in [(x_n)]$, $y_n\in U$ for all but finitely many $n$}\}.$$

Then by a short calculation, one can verify that the collection $$\mathcal{N}(0)$$ of subsets of $$\widehat{G}$$ having the $$\widehat{H}_i$$ as a coinitial subset satisfies all the conditions of [\[Topology\] §Open Sets, ⁋Proposition 6](/en/math/topology/open_sets#prop6), and therefore we can define a topology on $$\widehat{G}$$. By definition $$\widehat{G}$$ is also first countable, and the function $$G \rightarrow \widehat{G}$$ sending $$x\in G$$ to the constant sequence $$(x_i=x)$$ is continuous. Moreover, this function coincides exactly with the $$G \rightarrow \widehat{G}$$ defined in the previous section.

## Basic Properties of Completion

Now let us examine the basic properties of completion. By [Definition 3](#def3) above, any element of $$\widehat{A}$$ can be viewed as a Cauchy sequence in the $$\mathfrak{a}$$-adic topology on $$A$$. Then for $$b_j\in \mathfrak{a}^j$$, writing

$$a_i=\sum_{j=1}^i b_j\tag{3}$$

the sequence $$(a_i)$$ is a Cauchy sequence in $$\widehat{A}$$, and therefore the limit of this sequence

$$\sum_{j=1}^\infty b_j$$

defines an element of $$\widehat{A}$$. Conversely, given any element $$(a_n')$$ of $$\widehat{A}$$, using the local base (2) of $$0$$ we can find a Cauchy sequence equivalent to this element and having the form (3).

<div class="example" markdown="1">

<ins id="ex4">**Example 4**</ins> If $$A=\mathbb{K}[\x]$$ and $$\mathfrak{a}=(\x)$$, then $$\widehat{A}$$ is the ring of *formal power series* $$\mathbb{K}[[\x]]$$.

</div>

The ring $$\mathbb{K}[[\x]]$$ is a discrete valuation ring with unique nonzero prime ideal $$\mathfrak{m}=(\x)$$. That is, any element not in $$(\x)$$ is a unit, which essentially follows from the identity

$$\frac{1}{1+\x}=1-\x+\x^2-\cdots$$

This equality, or equivalently

$$(1+\x)(1-\x+\x^2-\cdots)=1$$

is obtained, as in the discussion above, by observing that for the partial sum of $$1-\x+\x^2-\cdots$$ up to degree $$i$$

$$1-\x+\x^2-\cdots+(-1)^i\x^i$$

we have

$$(1+\x)(1-\x+\x^2-\cdots+(-1)^i\x^i)=1+(-1)^i\x^i\in \mathfrak{m}^i$$

so this product is equivalent to the constant sequence $$(1)$$.

Generalizing this calculation, we obtain the following two results.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> Suppose $$A$$ is complete with respect to an ideal $$\mathfrak{a}$$. Then the set

$$U=\{1+a\mid a\in \mathfrak{a}\}$$

consists of units of $$A$$, and $$U$$ is multiplicatively closed.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Replace $$\x$$ by $$a$$ in the above argument.

</details>

<div class="proposition" markdown="1">

<ins id="cor6">**Corollary 6**</ins> For a local ring $$(A, \mathfrak{m})$$, the ring $$A[[\x_1,\ldots, \x_n]]$$ is also a local ring, and its unique maximal ideal is $$\mathfrak{m}+(\x_1,\ldots, \x_n)$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Any element outside $$\mathfrak{m}+(\x_1,\ldots,\x_n)$$ has a nonzero constant term, so by [Proposition 5](#prop5) it is a unit.

</details>

Moreover, the following holds.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> Fix a filtration of ideals of $$A$$

$$A=\mathfrak{a}_0\supseteq \mathfrak{a}_1\supseteq\cdots$$

and the associated graded ring $$\gr A$$ with respect to this filtration. If $$A$$ is complete with respect to this filtration, then for an ideal $$\mathfrak{a}$$ of $$A$$ and its elements $$a_1,\ldots, a_n$$, if $$\initial(\mathfrak{a})$$ is generated by $$\initial(a_1),\ldots, \initial(a_n)$$, then $$\mathfrak{a}$$ is also generated by $$a_1,\ldots, a_n$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$\mathfrak{a}'$$ be the ideal generated by $$a_1,\ldots, a_n$$ and let us show $$\mathfrak{a}=\mathfrak{a}'$$. Without loss of generality we may assume all these elements are nonzero. Also, if $$a_k\in \mathfrak{a}_i$$ held for all $$i$$, then by the canonical morphism $$A \rightarrow \widehat{A}$$ the element $$a_k$$ is sent to $$0\in \widehat{A}$$, and since $$A$$ is complete this means $$a_k=0$$; thus we can choose $$d$$ so that $$a_k\not\in \mathfrak{a}_i$$ holds for all $$k$$.

On the other hand, from the assumption that $$\initial(\mathfrak{a})$$ is generated by the $$\initial(a_k)$$, for any $$a\in \mathfrak{a}$$ there exist $$\beta_k\in \gr_\mathfrak{a}A$$ satisfying

$$\initial(a)=\sum_{k=1}^n \beta_k\initial(a_k)\tag{4}$$

and considering degrees in the above formula, we know that the $$\beta_k$$ are homogeneous and their degrees must satisfy

$$\degree(\beta_k)=\degree (\initial(a))-\degree(\initial(a_k))>\degree(\initial(a))-d.$$

Therefore for $$b_k\in A$$ satisfying $$\initial(b_k)=\beta_k$$, the element $$a-\sum_k b_k a_k$$ lies in $$\mathfrak{m}_{\degree(\initial(a))+1}$$. Repeating this process, we can choose $$a'\in \mathfrak{a}'$$ such that

$$a-\underbrace{\sum_k b_k a_k-\cdots}_{=a'} \in \mathfrak{a}_{d+1}.$$

Now, since $$a'$$ is generated by the $$a_k$$ anyway, showing that $$a$$ is generated by the $$a_k$$ is the same as showing that $$a-a'$$ is generated by the $$a_k$$. That is, without loss of generality we may assume $$a$$ lies in $$\mathfrak{a}_{d+1}$$.

Now let us revisit formula (4) under this assumption. Setting $$\degree(\initial(a))=e$$, we saw above that the degree of $$\beta_k$$ must be at least $$e-d$$. Therefore we can choose the $$b_k$$ from $$\mathfrak{a}_{e-d}$$, and now by the same logic as above

$$a-\sum_{k=1}^n b_ka_k$$

lies in $$\mathfrak{a}_{e-d+1}$$. Repeating this, we can choose $$b_k^{(l)}\in \mathfrak{a}_{e-d+l}$$ such that

$$a-\sum_{k=1}^n\sum_{l=0}^j b_k^{(l)}a_k\in \mathfrak{a}_{e+j+1}.$$

Now since $$A$$ is complete, the infinite sum

$$\sum_{l=0}^\infty b_k^{(l)}$$

can be regarded as an element $$c_k$$ of $$A$$. Then

$$a-\sum_{k=1}^n c_k a_k\in \bigcap \mathfrak{a}_i=0$$

so we obtain the desired result.

</details>


---

**References**

**[AM]** M.F. Atiyah and I.G. Macdonald, *Introduction to commutative algebra*, Basic Books, 1969.  
**[Eis]** David Eisenbud. *Commutative Algebra: with a view toward algebraic geometry*. Springer, 1995.

---
