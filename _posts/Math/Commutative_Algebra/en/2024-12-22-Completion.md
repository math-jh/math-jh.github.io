---
title: "Completion"
description: "The completion of a ring is a construction that turns a ring into a complete ring through a given ideal filtration. It covers the definitions of adic completion and complete local rings, and it enjoys a universal property as a categorical limit."
excerpt: "Completion of rings and modules defined by filtrations"

categories: [Math / Commutative Algebra]
permalink: /en/math/commutative_algebra/completion
sidebar: 
    nav: "commutative_algebra-en"

date: 2024-12-22
weight: 14
translated_at: 2026-09-02T03:15:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-09-02T03:15:05+00:00
---
## Definition of Completion

Given an arbitrary abelian group $G$ and a decreasing sequence of subgroups

$$\mathcal{J}:\qquad G=H_0\supseteq H_1\supseteq\cdots$$

the maps $G/ H_{i+1} \rightarrow G/H_{i}$ are well-defined, and more generally, composing these appropriately defines $\rho_{ji}:G/H_j \rightarrow G/H_i$ whenever $j>i$. From these data we obtain the inverse limit

$$\widehat{G}_\mathcal{J}=\varprojlim_i G/H_i=\left\{(g_1,g_2,\ldots)\in \prod G/H_i\middle\vert\text{$\rho_{ji}(g_j)=g_i$ for all $j>i$}\right\}$$

together with canonical morphisms $\rho_i:\widehat{G}_{\mathcal{J}} \rightarrow G/ H_i$, which satisfy $\rho_{ji}\circ\rho_j=\rho_i$ for all $j>i$. For notational convenience, when $\mathcal{J}$ is clear from context we simply write $\widehat{G}$.

These data can be regarded as a categorical limit, as we saw in [\[Category Theory\] §Limits, ⁋Example 5](/en/math/category_theory/limits#ex5), and therefore they also satisfy the following universal property.

> Whenever maps $K \rightarrow G/H_i$ satisfying $\rho_{ji}\circ\pi_j=\pi_i$ are given, there exists a unique $\pi:K \rightarrow \widehat{G}$ making the following diagram
> 
> {% diagram Math/Commutative_Algebra/Completion-1.svg width="13.57em" alt="universal_property" %}
> 
> commute.

If $G$ carries a ring structure and the $H_i$ are ideals, then $\widehat{G}$ also carries a natural ring structure. The situation we will consider is the following.

::: Definition 1
Fix a ring $A$ and an ideal $\mathfrak{a}$. Then for an $\mathfrak{a}$-filtration of ideals of $A$ ([§Blowup Algebras, ⁋Definition 3](/en/math/commutative_algebra/blowup_algebra#def3))

$$\mathcal{J}:\qquad A=\mathfrak{a}_0\supseteq \mathfrak{a}_1\supseteq \mathfrak{a}_2\cdots$$

we call

$$\widehat{A}=\varprojlim_i A/\mathfrak{a}_i$$

the *completion* of $A$ defined by this filtration. If the natural map $A \rightarrow \widehat{A}$ is an isomorphism, we call $A$ a *complete ring* with respect to this filtration.

In particular, if the above filtration is given in the form

$$A\supseteq\mathfrak{a}\supseteq \mathfrak{a}^2\cdots$$

we call it the *$\mathfrak{a}$-adic completion* of $A$. In this case, if $\mathfrak{a}$ is a maximal ideal, then $\widehat{A}$ is a local ring with the unique maximal ideal $\widehat{\mathfrak{a}}$, so we call $\widehat{A}$ a *complete local ring*.
:::

First, the natural map $\rho:A \rightarrow \widehat{A}$ is obtained by applying the universal property to the canonical morphisms $\pr_i: A \rightarrow A/\mathfrak{a}_i$. By definition,

$$x\in\ker\rho\iff\rho(x)=0\iff \rho_i(\rho(x))=0\text{ for all $i$}\iff \pr_i(x)=0\text{ for all $i$}\iff x\in \mathfrak{a}_i\text{ for all $i$}$$

so $\rho$ being injective is equivalent to $\bigcap \mathfrak{a}_i=0$.

Now let us write $\widehat{\mathfrak{a}}_i$ for the kernel of the canonical morphism $\rho_i:\widehat{A}\rightarrow A/\mathfrak{a}_i$. By definition $\mathfrak{a}_i=\rho^{-1}(\widehat{\mathfrak{a}}_i)$, and since the $\pr_i$ are surjective and $\pr_i=\rho_i\circ\rho$, the $\rho_i$ are all surjective, and hence by the first isomorphism theorem

$$\widehat{A}/\widehat{\mathfrak{a}}_i\cong A/\mathfrak{a}_i$$

holds. Therefore the descending chain of ideals of $\widehat{A}$

$$\widehat{A}=\widehat{\mathfrak{a}}_0\supseteq \widehat{\mathfrak{a}}_1\supseteq\cdots\tag{1}$$

is an $\mathfrak{a}$-filtration, and moreover from the above isomorphism

$$\widehat{A}=\varprojlim_i A/\mathfrak{a}_i\cong\varprojlim_i \widehat{A}/\widehat{\mathfrak{a}}_i$$

so $\widehat{A}$ is complete with respect to the given filtration. The above isomorphism also yields the isomorphism

$$\gr_\mathcal{J}A\cong\gr_{\widehat{\mathcal{J}}}\widehat{A}$$

as well.

## The $\mathfrak{a}$-adic Topology

Meanwhile, the process of constructing $\widehat{A}$ from $A$ can also be understood as endowing $A$ with a special kind of topology. First, let a topological abelian group $G$ be given. Fixing an element $g$ of $G$, the translation map $T_g$ defined using it is continuous, so the neighborhood filter at each point of $G$ is entirely determined by the neighborhood filter at $0\in G$. Of course, this process can be carried out in reverse as well.

As in the previous section, suppose we are given a decreasing sequence of subgroups of $G$

$$G=H_0\supseteq H_1\supseteq\cdots$$

Then setting

$$\mathcal{N}(0)=\{U\subseteq G\mid\text{$H_n\subseteq U$ for some $n$}\}$$

we know that this satisfies all the conditions of [\[Topology\] §Open Sets, ⁋Proposition 6](/en/math/topology/open_sets#prop6). Now, for arbitrary $g\in G$ and $U\in \mathcal{N}(0)$, declaring $g+U\in \mathcal{N}(g)$ gives a topology on $G$.

In particular, applying this to the situation of [Definition 1](#def1), we call the topology defined through the above process the *$\mathfrak{a}$-adic topology*. In this case, since $0\in A$ has the countable local base

$$\mathfrak{a}\supseteq \mathfrak{a}^2\supseteq\cdots\tag{2}$$

the topology on $A$ defined in this way is first countable.

Returning to a general topological abelian group $G$, we can weaken the condition for a convergent sequence and define the following.

::: Definition 2
For a topological group $(G, +, 0)$, a sequence $(x_i)_{i\in \mathbb{N}}$ of elements of $G$ is called a *Cauchy sequence* if, whenever an arbitrary neighborhood $U$ of $0$ is given, there exists a natural number $N$ such that the following statement

$$m,n>N \implies x_m-x_n\in U$$

is true.
:::

Then, just as one defines the completion in a general topological group as the collection of equivalence classes of Cauchy filters, given two Cauchy sequences $(x_m)$, $(y_n)$ we can decide when to regard them as the same and thereby define the (topological) completion. However, what we are interested in is the first countable topological group $A$ defined by the filtration (2) above, and since a first countable space is sequential, in the following definition we assume for convenience that $G$ is a first countable space and use Cauchy sequences instead of Cauchy filters.

::: Definition 3
Two Cauchy sequences $(x_m)$, $(y_n)$ of a topological group $(G, +, 0)$ are said to be *equivalent* if, whenever an arbitrary neighborhood $U$ of $0$ is given, there exists a natural number $N$ such that the following statement

$$m,n>N \implies x_m-y_n\in U$$

is true. The set obtained by imposing this equivalence relation on the set of all Cauchy sequences of a first countable topological group $G$ is called the *completion* of $G$, and we write it as $\widehat{G}$.
:::

Now, for an open neighborhood $U$ of $0\in G$, define

$$\widehat{U}=\{[(x_n)]\in \widehat{G}\mid\text{for any $(y_n)\in [(x_n)]$, $y_n\in U$ for all but finitely many $n$}\}$$

Then a short computation shows that the collection $\mathcal{N}(0)$ of subsets of $\widehat{G}$ having the $\widehat{H}_i$ as a coinitial subset satisfies all the conditions of [\[Topology\] §Open Sets, ⁋Proposition 6](/en/math/topology/open_sets#prop6), and therefore we can define a topology on $\widehat{G}$. By definition, $\widehat{G}$ is also first countable, and one can see that the function $G \rightarrow \widehat{G}$ taking $x\in G$ to the constant sequence $(x_i=x)$ is continuous. Moreover, this function is exactly the same as the map $G \rightarrow \widehat{G}$ defined in the previous section.

## Basic Properties of Completion

Let us now examine the basic properties of completion. By [Definition 3](#def3) above, an arbitrary element of $\widehat{A}$ can be thought of as a Cauchy sequence in $A$ with respect to the $\mathfrak{a}$-adic topology. Then, for elements $b_j$ satisfying $b_j\in \mathfrak{a}^j$, writing

$$a_i=\sum_{j=1}^i b_j\tag{3}$$

$(a_i)$ is a Cauchy sequence in $\widehat{A}$, and therefore the limit of this sequence

$$\sum_{j=1}^\infty b_j$$

defines an element of $\widehat{A}$. Conversely, given an arbitrary element $(a_n')$ of $\widehat{A}$, one can use the local base (2) of $0$ to find a Cauchy sequence equivalent to this element and having the form (3).

::: Example 4
If $A=\mathbb{K}[\x]$ and $\mathfrak{a}=(\x)$, then $\widehat{A}$ is the ring $\mathbb{K}[[\x]]$ of *formal power series*.
:::

The ring $\mathbb{K}[[\x]]$ is a local ring with the unique nonzero prime ideal $\mathfrak{m}=(\x)$. That is, any element not belonging to $(\x)$ is a unit, and this essentially follows from the identity

$$\frac{1}{1+\x}=1-\x+\x^2-\cdots$$ 

The above identity, or equivalently the identity

$$(1+\x)(1-\x+\x^2-\cdots)=1$$

is obtained, as in the discussion above, from the fact that for the partial sum of $1-\x+\x^2-\cdots$ up to degree $i$

$$1-\x+\x^2-\cdots+(-1)^i\x^i$$

we have

$$(1+\x)(1-\x+\x^2-\cdots+(-1)^i\x^i)=1+(-1)^i\x^{i+1}$$

and since the difference between this product and $1$ belongs to $\mathfrak{m}^{i+1}$, this product is equivalent to the constant sequence $(1)$.

Generalizing this computation, we obtain the following two results.

::: Proposition 5
Suppose $A$ is complete with respect to an ideal $\mathfrak{a}$. Then every element of the set

$$U=\{1+a\mid a\in \mathfrak{a}\}$$

is a unit of $A$, and $U$ is multiplicatively closed.
:::
::: Proof
Replace $\x$ with $a$ in the argument above.
:::

::: Corollary 6
For a local ring $(A, \mathfrak{m})$, $A[[\x_1,\ldots, \x_n]]$ is also a local ring, and its unique maximal ideal is $\mathfrak{m}+(\x_1,\ldots, \x_n)$.
:::
::: Proof
An element outside $\mathfrak{m}+(\x_1,\ldots,\x_n)$ has constant term not belonging to $\mathfrak{m}$, so its constant term is a unit of $A$; hence by [Proposition 5](#prop5) the element itself is a unit.
:::

Returning once more to the situation of [Definition 1](#def1), let us consider the case where $\mathfrak{a}$ is a maximal ideal and $\widehat{A}$ is its $\mathfrak{a}$-adic completion. First, since $\widehat{A}/\widehat{\mathfrak{a}}_1\cong A/\mathfrak{a}$ is a field, $\widehat{\mathfrak{a}}_1$ is a maximal ideal of $\widehat{A}$. Also, for $k>1$, since $\rho_1=\rho_{k1}\circ\rho_k$ and $\widehat{\mathfrak{a}}_1=\ker\rho_1$, we have $\rho_k(\widehat{\mathfrak{a}}_1)\subseteq \ker\rho_{k1}=\mathfrak{a}/\mathfrak{a}^k$, and therefore $\rho_k(\widehat{\mathfrak{a}}_1^k)\subseteq (\mathfrak{a}/\mathfrak{a}^k)^k=0$, that is, $\widehat{\mathfrak{a}}_1^k\subseteq \ker \rho_k=\widehat{\mathfrak{a}}_k$. Then for an arbitrary $a\in \widehat{\mathfrak{a}}_1$, since $(-a)^k\in \widehat{\mathfrak{a}}_k$, the partial sums of the series $\sum_{k=0}^\infty (-a)^k$ form a Cauchy sequence in $\widehat{A}$, and since $\widehat{A}$ is complete with respect to the filtration (1), the argument of [Proposition 5](#prop5) applies verbatim, so $1+a$ is a unit. Now, if $x\in \widehat{A}$ does not belong to $\widehat{\mathfrak{a}}_1$, then since $\widehat{A}/\widehat{\mathfrak{a}}_1$ is a field there exists $y$ with $xy-1\in \widehat{\mathfrak{a}}_1$, and since $xy$ is a unit by the previous result, $x$ is also a unit. That is, every element of $\widehat{A}$ not belonging to $\widehat{\mathfrak{a}}_1$ is a unit, and therefore $\widehat{A}$ is a local ring with $\widehat{\mathfrak{a}}_1$ as its unique maximal ideal.

Also, the following holds.

::: Proposition 7
Fix a filtration of ideals of $A$

$$A=\mathfrak{a}_0\supseteq \mathfrak{a}_1\supseteq\cdots$$

and the associated graded ring $\gr A$ with respect to the filtration. Suppose $A$ is complete with respect to this filtration. Then, for an ideal $\mathfrak{a}$ of $A$ and its elements $a_1,\ldots, a_n$, if $\initial(\mathfrak{a})$ is generated by $\initial(a_1),\ldots, \initial(a_n)$, then $\mathfrak{a}$ is also generated by $a_1,\ldots, a_n$.
:::
::: Proof
Let $\mathfrak{a}'$ be the ideal generated by the elements $a_1,\ldots, a_n$, and let us show that $\mathfrak{a}=\mathfrak{a}'$. Without loss of generality, we may assume that all of these elements are nonzero. Also, if $a_k\in \mathfrak{a}_i$ held for all $i$, then $a_k$ would be sent to $0\in \widehat{A}$ under the canonical morphism $A \rightarrow \widehat{A}$, and since $A$ is complete this would mean $a_k=0$; therefore we can choose a suitable $d$ so that $a_k\not\in \mathfrak{a}_d$ holds for all $k$.

Meanwhile, from the assumption that $\initial(\mathfrak{a})$ is generated by the $\initial(a_k)$, for an arbitrary $a\in \mathfrak{a}$ there exist $\beta_k\in \gr A$ satisfying

$$\initial(a)=\sum_{k=1}^n \beta_k\initial(a_k)\tag{4}$$

and considering degrees in the above equation, we know that the $\beta_k$ must be homogeneous, with degree

$$\degree(\beta_k)=\degree (\initial(a))-\degree(\initial(a_k))>\degree(\initial(a))-d$$

Therefore, for $b_k\in A$ satisfying $\initial(b_k)=\beta_k$, the element $a-\sum_k b_k a_k$ belongs to $\mathfrak{a}_{\degree(\initial(a))+1}$. Repeating this process, we can choose $a'\in \mathfrak{a}'$ such that

$$a-\underbrace{\left(\sum_k b_k a_k+\cdots\right)}_{=a'} \in \mathfrak{a}_{d+1}$$

At this point, since $a'$ is generated by the $a_k$ anyway, showing that $a$ is generated by the $a_k$ is the same as showing that $a-a'$ is generated by the $a_k$. That is, without loss of generality we may assume that $a$ belongs to $\mathfrak{a}_{d+1}$.

Now let us examine equation (4) again under this assumption. Writing $\degree(\initial(a))=e$, we saw above that the degree of $\beta_k$ must be at least $e-d$. Therefore we can choose the $b_k$ from $\mathfrak{a}_{e-d}$, and now by the same logic as above,

$$a-\sum_{k=1}^n b_ka_k$$

belongs to $\mathfrak{a}_{e-d+1}$. Repeating this, we can choose $b_k^{(l)}\in \mathfrak{a}_{e-d+l}$ such that

$$a-\sum_{k=1}^n\sum_{l=0}^j b_k^{(l)}a_k\in \mathfrak{a}_{e+j+1}$$

Now since $A$ is complete, the infinite sum

$$\sum_{l=0}^\infty b_k^{(l)}$$

can be regarded as an element $c_k$ of $A$. Then

$$a-\sum_{k=1}^n c_k a_k\in \bigcap \mathfrak{a}_i=0$$

so we obtain the desired result.
:::


---

**References**

**[AM]** M.F. Atiyah and I.G. Macdonald, *Introduction to commutative algebra*, Basic Books, 1969.  
**[Eis]** David Eisenbud. *Commutative Algebra: with a view toward algebraic geometry*. Springer, 1995.

---
