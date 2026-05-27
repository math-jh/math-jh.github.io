---title: "Associated Primes"
excerpt: "The prime avoidance lemma and the definition and properties of associated primes"

categories: [Math / Commutative Algebra]
permalink: /en/math/commutative_algebra/associated_primes
header:
    overlay_image: /assets/images/Math/Commutative_Algebra/Associated_Primes.png
    overlay_filter: 0.5
sidebar: 
    nav: "commutative_algebra-en"

date: 2024-10-16
last_modified_at: 2024-10-16
weight: 6
translated_at: 2026-05-28T11:36:15+00:00
translation_source: kimi-cli
---
## Prime avoidance lemma

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> For a ring $$A$$ and an $$A$$-module $$M$$, a prime ideal $$\mathfrak{p}$$ of $$A$$ is called an *associated prime ideal* of $$M$$ if $$\mathfrak{p}=\ann(x)$$ for some $$x\in M$$. We denote the set of associated primes by $$\Ass M$$.

However, when $$M=\mathfrak{a}$$ is an ideal of $$A$$, by convention the associated prime ideals of $$\mathfrak{a}$$ mean $$\Ass A/\mathfrak{a}$$, <em-ko>not</em-ko> $$\Ass \mathfrak{a}$$.

</div>

By definition, $$\mathfrak{p}$$ being an associated prime of $$M$$ is equivalent to $$A/\mathfrak{p}$$ being a submodule of $$M$$. This follows immediately by defining $$A \rightarrow M$$ via $$1\mapsto x$$ and applying the first isomorphism theorem.

In this post we study various properties of associated prime ideals. The following lemma plays an important role in this process.

<div class="proposition" markdown="1">

<ins id="lem2">**Lemma 2 (Prime avoidance lemma)**</ins> Let $$\mathfrak{a}_1,\ldots, \mathfrak{a}_n, \mathfrak{b}$$ be ideals of $$A$$, and suppose $$\mathfrak{b}\subseteq \mathfrak{a}_1\cup\cdots\cup \mathfrak{a}_n$$. If $$R$$ contains an infinite field, or at most two of the $$\mathfrak{a}_i$$ are not prime ideals, then $$\mathfrak{b}$$ is contained in one of $$\mathfrak{a}_1,\ldots, \mathfrak{a}_n$$.

In addition, if $$A$$ is graded and $$\mathfrak{b}$$ is a homogeneous ideal and all the $$\mathfrak{a}_i$$ are prime ideals, then the conclusion still holds under the assumption that the homogeneous elements of $$\mathfrak{b}$$ belong to $$\mathfrak{a}_1\cup\cdots\cup \mathfrak{a}_n$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

If $$R$$ contains an infinite field $$\mathbb{K}$$, then viewing each ideal as a $$\mathbb{K}$$-vector space, we have

$$\mathfrak{b}=\bigcup_{i=1}^n (\mathfrak{b}\cap \mathfrak{a}_i),$$

and this is obvious because no $$\mathbb{K}$$-vector space can be expressed as a finite union of its proper subspaces.

We prove the remaining case by induction on $$n$$. There is nothing to prove when $$n=1$$.

For larger $$n$$, if the inclusion in the hypothesis still holds when we omit one of $$\mathfrak{a}_1,\ldots, \mathfrak{a}_n$$, then this can be resolved by the inductive hypothesis, so it suffices to consider the case where this is not so. In other words, we may assume that for each $$i$$ there exists $$x_i\in \mathfrak{b}$$ satisfying $$x_i\not\in \bigcup_{j\neq i}\mathfrak{a}_j$$, and by the condition on $$x_i$$ we must have $$x_i\in \mathfrak{a}_i$$.

Now consider the case $$n=2$$, and look at the element $$x_1+x_2\in \mathfrak{b}$$. If $$x_1+x_2\in \mathfrak{a}_1$$, then $$x_2=(x_1+x_2)-x_1\in \mathfrak{a}_1$$, which is a contradiction; similarly $$x_1+x_2$$ cannot be an element of $$\mathfrak{a}_2$$. This contradicts the assumption that $$\mathfrak{b}\subseteq \mathfrak{a}_1\cup \mathfrak{a}_2$$.

For $$n>3$$ we use a similar idea. By the given condition, at least one of $$\mathfrak{a}_1,\ldots, \mathfrak{a}_n$$ is a prime ideal, so without loss of generality we may assume that $$\mathfrak{a}_1$$ is a prime ideal. Then consider the element $$x_1+x_2x_3\cdots x_n$$, and using the assumption that $$\mathfrak{a}_1$$ is prime we obtain a contradiction.

In the graded case, it suffices to multiply $$x_i$$ repeatedly so that it has the same degree as $$x_2x_3\cdots$$.

</details>

In particular, the above lemma is most often used when the latter hypothesis is satisfied rather than the former.

## Associated prime ideals

Now we investigate $$\Ass M$$ in more detail.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> Fix an $$A$$-module $$M$$, and suppose $$\mathfrak{a}$$ is maximal among ideals of the form $$\ann(x)$$. Then $$\mathfrak{a}$$ is a prime ideal.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Suppose $$ab\in \mathfrak{a}$$ and $$b\not\in \mathfrak{a}$$; we must show $$a\in \mathfrak{a}$$. Write $$\mathfrak{a}=\ann(x)$$. Then by assumption $$abx=0$$ and $$bx\neq 0$$. Now $$\mathfrak{a}\subseteq\ann(bx)$$, so by maximality of $$\mathfrak{a}$$ we have $$\mathfrak{a}=\ann(bx)$$. Hence

$$(a)+\mathfrak{a}\subseteq \ann(bx)=\mathfrak{a}$$

and therefore $$a\in \mathfrak{a}$$.

</details>

The ideal $$\mathfrak{a}$$ obtained from the above proposition is a prime ideal and simultaneously the annihilator of some element, so by definition it belongs to $$\Ass M$$.

Meanwhile, by [§Properties of Localization, ⁋Lemma 3](/en/math/commutative_algebra/properties_of_localization#lem3), for any $$A$$-module $$M$$, an element $$x\in M$$ is zero if and only if its image under the localization $$\epsilon_\mathfrak{m}: M \rightarrow M_\mathfrak{m}$$ is zero for every maximal ideal $$\mathfrak{m}$$; thus to show $$x=0$$ it suffices to show that $$\epsilon_\mathfrak{p}(x)=0$$ for every prime ideal $$\mathfrak{p}$$. The following corollary can also be understood in the same context.

<div class="proposition" markdown="1">

<ins id="cor4">**Corollary 4**</ins> Let $$M$$ be a module over a Noetherian ring $$A$$. Then the following hold.

1. For an element $$x\in M$$, we have $$x=0$$ if and only if $$\epsilon_\mathfrak{p}(x)=0$$ for every maximal associated prime $$\mathfrak{p}$$ of $$M$$.
2. For a submodule $$L$$ of $$M$$, we have $$L=0$$ if and only if $$L_\mathfrak{p}=0$$ for all $$\mathfrak{p}\in\Ass M$$.
3. An $$A$$-linear map $$u:M \rightarrow N$$ is injective if and only if $$u_\mathfrak{p}$$ is injective for every $$\mathfrak{p}\in \Ass M$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, for statement 1, the hypothesis that $$A$$ is Noetherian allows us to choose, for each $$x\in M$$, a maximal ideal $$\mathfrak{p}$$ among the annihilator ideals containing $$\ann(x)$$, and by [Proposition 3](#prop3) we have $$\mathfrak{p}\in \Ass M$$. Hence $$x/1$$ is nonzero in $$M_\mathfrak{p}$$. Statement 2 follows immediately from statement 1, and for statement 3 we set $$L=\ker u$$ in statement 2.

</details>

The goal of this post is to prove [Theorem 7](#thm7). For this we need the following two lemmas.

<div class="proposition" markdown="1">

<ins id="lem5">**Lemma 5**</ins> Given a short exact sequence of $$A$$-modules

$$0 \rightarrow M' \rightarrow M \rightarrow M'' \rightarrow 0$$

we have

$$\Ass M'\subset \Ass M\subset (\Ass M')\cup (\Ass M'').$$

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

The first inclusion is obvious. For the second inclusion, assume that $$\mathfrak{p}\in\Ass M$$ does not belong to $$\Ass M'$$, and let us show that it belongs to $$\Ass M''$$. If $$\mathfrak{p}=\ann(x)$$ for some $$x\in M$$, then $$Ax\cong A/\mathfrak{p}$$. Since $$\mathfrak{p}$$ is a prime ideal, for any nonzero $$ax\in Ax$$ we have

$$a'\in\ann(ax)\iff a'ax=0\iff a'a\in \mathfrak{p}\iff a'\in \mathfrak{p}$$

so that $$\ann(ax)=\mathfrak{p}$$. Here the last equivalence uses the fact that $$ax\neq 0$$ and $$Ax\cong A/\mathfrak{p}$$ to obtain $$a\not\in \mathfrak{p}$$. This equality shows in particular that any nonzero submodule of $$Ax$$ has annihilator $$\mathfrak{p}$$; combining this with the fact that $$\mathfrak{p}\not\in \Ass M'$$, we see that $$Ax\cap M'=0$$. Therefore the image of $$Ax$$ in $$M''$$ is isomorphic to $$Ax$$, and hence $$\mathfrak{p}\in \Ass M''$$.

</details>

<div class="proposition" markdown="1">

<ins id="lem6">**Lemma 6**</ins> For a finitely generated module $$M$$ over a Noetherian ring $$A$$, there exists a filtration

$$0=M_0\subseteq M_1\subseteq\cdots\subseteq M_n=M,\qquad \text{$M_{k+1}/M_k\cong A/\mathfrak{p}_k$ for some prime $\mathfrak{p}_k$, for all $k$}$$

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, using [Proposition 3](#prop3) we can find an associated prime $$\mathfrak{p}_1\in\Ass M$$ of $$M$$, and thus there exists a submodule $$M_1$$ satisfying $$M_1\cong A/\mathfrak{p}_1$$. Applying the same argument to $$M/M_1$$ we obtain $$M_2$$, and repeating this process yields the desired conclusion because $$M$$ is Noetherian.

</details>

<div class="proposition" markdown="1">

<ins id="thm7">**Theorem 7**</ins> Let $$M$$ be a finitely generated module over a Noetherian ring $$A$$. Then the following hold.

1. $$\Ass M$$ is a nonempty finite set, and each of its elements contains $$\ann M$$. Moreover, the minimal prime ideals among those containing $$\ann M$$ all belong to $$\Ass M$$.
2. The union of the associated primes consists of $$0$$ and the zero-divisors on $$M$$.
3. The following formula holds:

    $$\Ass_{S^{-1}A}S^{-1}M=\{\mathfrak{p}S^{-1}A: \mathfrak{p}\in\Ass M, \mathfrak{p}\cap S=\emptyset\}$$

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, for the first statement, that $$\Ass M$$ is nonempty follows from [Proposition 3](#prop3), and that every element of $$\Ass M$$ contains $$\ann M$$ is obvious. Meanwhile, by [Lemma 5](#lem5), considering the short exact sequence

$$0 \rightarrow M_{n-1} \rightarrow M_n \rightarrow M_n/M_{n-1} \rightarrow 0$$

we obtain $$\Ass M_n \subseteq \Ass M_{n-1}\cup \Ass M_n/M_{n-1}=\Ass M_{n-1}\cup \Ass A/\mathfrak{p}_n$$.

On the other hand, we can show that $$\Ass(A/\mathfrak{p})=\{\mathfrak{p}\}$$ for any prime ideal $$\mathfrak{p}$$ as follows. Let $$\mathfrak{q}\in \Ass(A/\mathfrak{p})$$, and write $$\mathfrak{q}=\ann(x+\mathfrak{p})$$. Then first it is obvious that $$\mathfrak{p}\subseteq \mathfrak{q}$$, because for any $$p\in \mathfrak{p}$$,

$$p(x+\mathfrak{p})=px+\mathfrak{p}=0+\mathfrak{p}$$

we have. If $$\mathfrak{q}\not\subseteq \mathfrak{p}$$, then there exists $$q\in \mathfrak{q}\setminus \mathfrak{p}$$. Then from

$$0=q(x+\mathfrak{p})=qx+\mathfrak{p}$$

we see that $$qx\in \mathfrak{p}$$, and since $$q\not\in \mathfrak{p}$$ we must have $$x+\mathfrak{p}=0$$. But this means $$\mathfrak{q}=A$$, which is a contradiction.

Therefore, repeating

$$\Ass M \Ass M_{n-1}\cup \{ \mathfrak{p}_{n-1}\}\subseteq \Ass M_{n-2}\cup \{\mathfrak{p}_{n-1},\mathfrak{p}_{n-2}\}\cdots$$

in this way, we obtain the finiteness in the first statement.

The remaining part of the first statement is obtained by proving the third statement. Before that, for the second statement, if $$a\in A$$ belongs to the annihilator ideal of some $$x\in M$$, then we can consider a maximal annihilator ideal containing this annihilator ideal, which belongs to $$\Ass M$$, so this is obvious. For the third statement, one need only pay attention to the notation and use [§Properties of Localization, ⁋Proposition 5](/en/math/commutative_algebra/properties_of_localization#prop5).

Assuming the third statement, the remaining part is also obvious. If $$\mathfrak{p}$$ is minimal among the prime ideals containing $$\ann M$$, then using the third statement we may consider the maximal ideal $$\mathfrak{p}$$ in the localization $$A_\mathfrak{p}$$; since $$\mathfrak{p}$$ is the only prime ideal containing $$\ann M$$, we must have $$\mathfrak{p}\in \Ass M$$.

</details>

Through this we can extract a great deal of information about $$M$$. For example, when $$M=A$$ and $$A$$ is reduced, we obtain the following corollary.

<div class="proposition" markdown="1">

<ins id="cor8">**Corollary 8**</ins> For a reduced Noetherian ring $$A$$, let $$K$$ be its total ring of fractions. Then $$K$$ is a finite product of fields.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, setting $$M=A$$ we have $$\ann(A)=\{0\}$$. Therefore all the minimal prime ideals $$\mathfrak{p}_1,\ldots, \mathfrak{p}_k$$ of $$A$$ belong to $$\Ass M$$, and their union consists of the zero-divisors of $$A$$.

Moreover, if $$A$$ is reduced, then their union is exactly the set of all zero-divisors of $$A$$. To verify this, observe first from the assumption that $$A$$ is reduced that we have

$$(0)=\mathfrak{N}(A)=\bigcap_\text{\scriptsize$\mathfrak{p}$ a prime}\mathfrak{p}\supseteq \bigcap_{i=1}^k \mathfrak{p}_i.$$

Then for any zero-divisor $$a\neq 0$$ and any $$b\neq 0$$ with $$ab=0$$, there must exist some $$\mathfrak{p}_i$$ such that $$b\not\in \mathfrak{p}_i$$, and then since $$ab=0\in \mathfrak{p}_i$$ we must have $$a\in \mathfrak{p}_i$$.

Therefore, letting $$S=A\setminus(\mathfrak{p}_1\cup\cdots\cup \mathfrak{p}_k)$$, the total ring of fractions $$K$$ of $$A$$ is $$K=S^{-1}A$$, and one can show that the prime ideals of this ring are exactly the images of the $$\mathfrak{p}_i$$, and that $$K$$ is the product of the rings $$S^{-1}A/\mathfrak{p}_iS^{-1}A$$.

</details>

---

**References**

**[Eis]** David Eisenbud. *Commutative Algebra: with a view toward algebraic geometry*. Springer, 1995.

---
