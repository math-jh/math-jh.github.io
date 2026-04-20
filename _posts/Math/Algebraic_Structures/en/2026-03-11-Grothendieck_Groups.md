---

title: "Grothendieck Groups"
excerpt: "The Grothendieck group and the definition of integers"

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/Grothendieck_groups
header:
    overlay_image: /assets/images/Math/Algebraic_Structures/Grothendieck_groups.png
    overlay_filter: 0.5
sidebar:
    nav: "algebraic_structures-en"

date: 2026-03-11
last_modified_at: 2026-03-11
weight: 3

---

In the previous post, we examined the definition of a monoid. Notably, the natural numbers defined in set theory form a commutative monoid under addition. In this post, we introduce a method for obtaining an abelian group from a commutative semigroup.

First, consider the category $$\Ab$$ of abelian groups. Since any abelian group can be regarded as a commutative monoid by forgetting the information about inverses, there exists a forgetful functor $$U: \Ab \rightarrow \cMon$$. This functor is known to have a left adjoint $$K:\cMon \rightarrow \Ab$$, and this adjunction can be expressed as the equation

$$\Hom_\Ab(K(M), G)\cong\Hom_\cMon(M, U(G))$$

That is, given a commutative monoid $$M$$ and a monoid homomorphism $$M\rightarrow U(G)$$, we should be able to obtain a unique group homomorphism $$K(M)\rightarrow G$$.

## Universal Mapping Problem

We now need to demonstrate the existence of the left adjoint $$K$$ described above. More generally, following our main reference **\[Bou\]**, we examine the process of obtaining an abelian group from a commutative *semigroup*. Meanwhile, using the unit of the adjunction, we can spell out the properties that $$K$$ must satisfy.

> The abelian group $$K(S)$$ and the semigroup homomorphism $$\eta_S:S\rightarrow K(S)$$ form a pair satisfying the following property.
>
>![universal_property](/assets/images/Math/Algebraic_Structures/Grothendieck_groups-1.png){:style="width:7.4em"  class="invert" .align-center}
>
>(Universal mapping problem) Whenever an abelian group $$G$$ and a semigroup homomorphism $$f:S\rightarrow G$$ are given, there exists a unique *group homomorphism* $$\bar{f}:K(S)\rightarrow G$$ such that $$f=\bar{f}\circ\eta_S$$.

Intuitively, $$K(S)$$ can be thought of as the smallest abelian group containing $$(S,+)$$.

The $$K(S)$$ satisfying the above property is unique up to isomorphism.

<div class="proposition" markdown="1">

<ins id="prop1">**Proposition 1**</ins> If an abelian group $$H$$ and semigroup homomorphism $$\eta_S'$$ satisfy the above universal mapping problem, then $$K(S)\cong H$$ holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, consider the following diagram.

![uniqueness_1](/assets/images/Math/Algebraic_Structures/Grothendieck_groups-2.png){:style="width:7.4em"  class="invert" .align-center}

By the universal property, there exists $$\bar{\eta}_S': K(S)\rightarrow H$$ such that $$\eta_S'= \bar{\eta}_S'\circ\eta_S$$. On the other hand, from the following diagram

![uniqueness_2](/assets/images/Math/Algebraic_Structures/Grothendieck_groups-3.png){:style="width:7.4em"  class="invert" .align-center}

using the universal property for $$H$$, there exists $$\bar{\eta}_S:H\rightarrow K(S)$$ such that $$\eta_S=\bar{\eta}_S\circ\eta_S'$$. Then

$$\bar{\eta}_S'\circ\bar{\eta}_S\circ\eta_S'=\bar{\eta}_S'\circ \eta_S=\eta=\id_{H}\circ \eta_S' $$

and since $$f$$ satisfying $$f\circ \eta_S'=\eta_S'$$ is unique by the universal property, we have $$f=\id_H=\bar{\eta}_S'\circ \bar{\eta}_S$$. Alternatively, in the language of diagrams, since the unique $$H\rightarrow H$$ making the following diagram commute must be $$\id_H=\bar{\eta}_S'\circ \bar{\eta}_S$$.

![uniqueness_3](/assets/images/Math/Algebraic_Structures/Grothendieck_groups-4.png){:style="width:8.8em"  class="invert" .align-center}

Similarly, we can show that $$\id_{K(S)}=\bar{\eta}_S\circ \bar{\eta}_S'$$, and therefore $$K(S)\cong H$$.
</details>

On the other hand, if $$S$$ is already an abelian group, then $$K(S)$$ should be $$S$$ itself without adding any additional elements.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> If $$S$$ is an abelian group, then the abelian group $$K(S)$$ satisfying the above universal mapping problem satisfies $$K(S)\cong S$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Since $$S$$ and $$\id_S$$ trivially satisfy the universal property, by [Proposition 1](#prop1), any abelian group satisfying the universal property must be isomorphic to $$S$$.

</details>

The above propositions show that $$K(S)$$ satisfying the universal mapping problem is the abelian group we are looking for, but they do not demonstrate that $$K(S)$$ actually exists.

## Definition of $$K(S)$$

The reason why $$S$$ cannot be an abelian group is that inverses may not exist for all elements. Intuitively, this can be resolved by adding *negatives*.

Given a commutative semigroup $$(S,+)$$, consider the product semigroup $$S\times S$$. ([§Algebraic Structures, ⁋Example 5](/en/math/algebraic_structures/algebraic_structures#ex5)) If we think of the second component of $$S\times S$$ as representing negatives, the equation

$$(a_1, b_1)+(a_2, b_2)=(a_1+a_2, b_1+b_2)$$

can be thought of as representing

$$(a_1+a_2)-(b_1+b_2)=(a_1-b_1)+(a_2-b_2)$$

Of course, in general, even if $$a$$ and $$b$$ are different, the value $$a-b$$ can vary significantly, so we define an equivalence relation $$R$$ on $$S\times S$$ as follows.

$$(a_1, b_1)\equiv (a_2, b_2)\pmod{R}\iff a_1+b_2+c=a_2+b_1+c\text{ for some $c\in S$}$$

First, we need to show that this relation is an equivalence relation.

<div class="proposition" markdown="1">

<ins id="lem3">**Lemma 3**</ins> The relation $$R$$ defined above is an equivalence relation compatible with the operation on the product semigroup $$S\times S$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, let us show that $$R$$ is an equivalence relation. For any $$(a,b)\in S\times S$$,

$$a+b+c=a+b+c$$

holds for any $$c\in S$$, so $$(a,b)\equiv(a,b)$$. Suppose $$(a_1,b_1)\equiv (a_2,b_2)$$. That is, for some $$c\in S$$,

$$a_1+b_2+c=a_2+b_1+c$$

holds. But this is precisely the condition for $$(a_2,b_2)\equiv (a_1,b_1)$$, so $$R$$ is symmetric. Finally, suppose $$(a_1,b_1)\equiv(a_2,b_2)$$ and $$(a_2,b_2)\equiv (a_3,b_3)$$. Then for some $$c$$ and $$c'$$,

$$a_1+b_2+c=a_2+b_1+c,\qquad a_2+b_3+c'=a_3+b_2+c'$$

hold. Adding these two equations,

$$a_1+b_3+(a_2+b_2+c+c')=a_3+b_1+(a_2+b_2+c+c')$$

so $$(a_1,b_1)\equiv(a_3,b_3)$$ holds. Thus $$R$$ is an equivalence relation.

Now we need to show that $$R$$ is compatible with the operation on $$S\times S$$. For this, suppose $$(a_1, b_1)\equiv(a_1',b_1')$$ and $$(a_2, b_2)\equiv (a_2',b_2')$$. We need to show that $$(a_1+a_2, b_1+b_2)\equiv(a_1'+a_2', b_1'+b_2')$$. From the given conditions, there exist $$c_1$$ and $$c_2$$ such that

$$a_1+b_1'+c_1=a_1'+b_1+c_1,\qquad a_2+b_2'+c_2=a_2'+b_2+c_2$$

hold. Adding these two equations,

$$(a_1+a_2)+(b_1'+b_2')+(c_1+c_2)=(a_1'+a_2')+(b_1+b_2)+(c_1+c_2)$$

holds, so by definition $$(a_1+a_2, b_1+b_2)\equiv(a_1'+a_2', b_1'+b_2')\pmod{R}$$, and thus $$R$$ is compatible with the operation on $$S\times S$$.

</details>

Therefore, $$(S\times S)/R$$ becomes a commutative semigroup. Let us denote this by $$K(S)$$.

<div class="proposition" markdown="1">

<ins id="lem4">**Lemma 4**</ins> $$K(S)$$ is an abelian group.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

It suffices to show that $$K(S)$$ has an identity element and inverses. Since we are thinking of $$(a,b)$$ as $$a-b$$, the identity element will be of the form $$(a,a)$$, and the inverse of $$(a,b)$$ will be $$-(a-b)=b-a$$, i.e., $$(b,a)$$. Let us prove this.

First, we show that for any $$c\in S$$, $$[(c,c)]$$ is the identity element. For any $$[(a,b)]\in K(S)$$,

$$[(a,b)]+[(c,c)]=[(a+c, b+c)]$$

holds. Since

$$(a+c)+b+d=(b+c)+a+d$$

holds for any $$d\in S$$, we have $$(a+c, b+c)\equiv (a,b)$$, and therefore $$[(a+c, b+c)]=[(a,b)]$$. By commutativity, $$[(c,c)]+[(a,b)]=[(a,b)]$$ also holds, so $$[(c,c)]$$ is the identity element of $$K(S)$$.

On the other hand, for any $$[(a,b)]\in K(S)$$,

$$[(a,b)]+[(b,a)]=[(a+b,a+b)]$$

so by the previous argument, $$[(a,b)]+[(b,a)]$$ is the identity element of $$K(S)$$, as is $$[(b,a)]+[(a,b)]$$. Thus every element of $$K(S)$$ has an inverse, so $$K(S)$$ has a group structure.

</details>

Thus $$K(S)$$ becomes the abelian group we were looking for. That is, $$K(S)$$ satisfies the above universal mapping problem.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> For a commutative semigroup $$(S, +)$$, the abelian group $$K(S)$$ constructed as above and the natural semigroup homomorphism $$\eta_S:S\rightarrow K(S)$$ satisfy the universal property.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, let us consider what the *natural semigroup homomorphism* from $$S$$ to $$K(S)$$ should be. Since we are treating $$(a,b)$$ in $$K(S)$$ as $$a-b$$, we see that $$a$$ in $$K(S)$$ corresponds to $$(a+b)-b$$, i.e., $$[(a+b, b)]$$. Therefore, let us define $$\eta_S$$ by $$a\mapsto[(a+a, a)]$$. Of course, choosing any $$b$$ and defining $$a\mapsto[(a+b,b)]$$ yields the same value.

To prove the universal property, suppose an arbitrary abelian group $$G$$ and a semigroup homomorphism $$f:S\rightarrow G$$ are given.

First, if $$\bar{f}:K(S)\rightarrow S$$ satisfying the given property exists, then $$\bar{f}$$ must be unique. For any $$[(a,b)]$$,

$$\begin{aligned}\bar{f}\left([(a,b)]\right)&=\bar{f}\left([(a+(a+b), b+(a+b))]\right)=\bar{f}\left([(a+a,a)]+[(b, b+b)]\right)\\ &\bar{f}\left([(a+a, a)]\right)+\bar{f}\left([(b,b+b)]\right)=\bar{f}\left(\eta_S(a)\right)-\bar{f}\left(\eta_S(b)\right)\\ &=f(a)-f(b)\end{aligned}$$

so the function values at each element are uniquely determined.

Now, taking a hint from the uniqueness proof, let us define $$\bar{f}([(a,b)])$$ as $$f(a)-f(b)$$. First, this definition is well-defined. That is, if $$(a_1,b_1)\equiv(a_2,b_2)$$, then $$f(a_2)-f(b_2)=f(a_1)-f(b_1)$$. Since $$(a_1,b_1)\equiv(a_2,b_2)$$, there exists $$c\in S$$ such that $$a_1+b_2+c=a_2+b_1+c$$, so

$$f(a_1)+f(b_2)+f(c)=f(a_1+b_2+c)=f(a_2+b_1+c)=f(a_2)+f(b_1)+f(c)$$

Subtracting $$f(c)$$ from both sides and rearranging,

$$f(a_1)-f(b_1)=f(a_2)-f(b_2)$$

is obtained.

Also, $$\bar{f}$$ is a group homomorphism. For any $$[(a_1, b_1)]$$ and $$[(a_2,b_2)]$$,

$$\begin{aligned}\bar{f}\left([(a_1,b_1)]+[(a_2, b_2)]\right)&=\bar{f}\left([(a_1+a_2, b_1+b_2)]\right)=f(a_1+a_2)-f(b_1+b_2)\\&=f(a_1)+f(a_2)-f(b_1)-f(b_2)=(f(a_1)-f(b_1))+(f(a_2)-f(b_2))\\&=\bar{f}\left([(a_1, b_1)]\right)+\bar{f}\left([(a_2,b_2)]\right)\end{aligned}$$

holds.

Finally, that $$\bar{f}$$ satisfies the given condition $$f=\bar{f}\circ\eta_S$$ is obvious upon calculation.

</details>

Thus, we have obtained the desired abelian semigroup $$K(S)$$. In particular, we can define integers rigorously.

<div class="definition" markdown="1">

<ins id="def6">**Definition 6**</ins> For the monoid $$(\mathbb{N},+)$$, the abelian group obtained through the above process is denoted by $$(\mathbb{Z},+)$$.

</div>

## Monoid of Fractions

In the above discussion, we obtained $$K(S)$$ by adding inverses for all elements of $$S$$. On the other hand, looking at [Definition 6](#def6), what we actually do is add inverses only for elements of the subset $$\mathbb{N}\setminus\{0\}$$ of $$\mathbb{N}$$. This can also be obtained with slight modifications to the above discussions; we will omit the proofs and only sketch the process.

Consider a commutative monoid $$E$$, a subset $$S$$ of $$E$$, and the submonoid $$S'$$ of $$E$$ generated by $$S$$. Also, assume the operation of $$E$$ is written as multiplication. Define the following relation on $$E\times S'$$

$$(a,p)\equiv (b,q)\pmod{R}\iff aqs=bps\text{ for some $s\in S'$}$$

Then this relation is an equivalence relation compatible with the operation on $$E\times S'$$, so $$(E\times S')/R$$ becomes a monoid.

<div class="definition" markdown="1">

<ins id="def7">**Definition 7**</ins> The monoid $$(E\times S')/R$$ obtained as above is called the *monoid of fractions* of $$E$$ with denominator $$S$$, denoted by $$E_S$$. Elements $$(a,p)$$ of this monoid are denoted by $$a/p$$.

</div>

In this case, since $$E$$ is a monoid, unlike the above discussion, it has an identity element $$1$$. Then the homomorphism $$\eta_S$$ in [Proposition 5](#prop5) can be explicitly thought of as $$a\mapsto a/1$$.

---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.

---
