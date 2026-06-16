---
title: "Grothendieck Groups"
excerpt: "The Grothendieck group and the definition of integers"

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/Grothendieck_groups
sidebar:
    nav: "algebraic_structures-en"

date: 2026-03-11
weight: 3
translated_at: 2026-05-29T16:03:58+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-24T07:30:03+00:00
---
In the previous post, we examined the definition of a monoid; in particular, the natural numbers as defined in set theory form a commutative monoid under addition. In this post, we introduce a method for constructing an abelian group from a commutative semigroup.

First, consider the category $$\Ab$$ of abelian groups. Since any abelian group can be viewed as a commutative monoid by forgetting the information about inverses, there is a forgetful functor $$U: \Ab \rightarrow \cMon$$. It is known that this functor has a left adjoint $$K:\cMon \rightarrow \Ab$$, and writing out this adjunction yields the formula

$$\Hom_\Ab(K(M), G)\cong\Hom_\cMon(M, U(G))$$

That is, given a commutative monoid $$M$$ and a monoid homomorphism $$M\rightarrow U(G)$$, there must exist a unique group homomorphism $$K(M)\rightarrow G$$.

## Universal mapping problem

We now show the existence of the left adjoint $$K$$ described above. More generally, following our main reference **\[Bou\]**, we examine the process of constructing an abelian group from a commutative *semigroup*. Meanwhile, using the unit of the adjunction, we can spell out the properties that $$K$$ must satisfy.

> The abelian group $$K(S)$$ and the semigroup homomorphism $$\eta_S:S\rightarrow K(S)$$ constitute a pair satisfying the following property.
>
>![universal_property](/assets/images/Math/Algebraic_Structures/Grothendieck_Groups-1.svg){:style="width:6.91em"  class="invert" .align-center}
>
>(Universal mapping problem) Given any abelian group $$G$$ and any semigroup homomorphism $$f:S\rightarrow G$$, there exists a unique *group homomorphism* $$\bar{f}:K(S)\rightarrow G$$ such that $$f=\bar{f}\circ\eta_S$$.

Intuitively, $$K(S)$$ may be thought of as the smallest abelian group containing $$(S,+)$$.

Any $$K(S)$$ satisfying the above property is unique up to isomorphism.

<div class="proposition" markdown="1">

<ins id="prop1">**Proposition 1**</ins> If an abelian group $$H$$ and a semigroup homomorphism $$\eta_S'$$ satisfy the above universal mapping problem, then $$K(S)\cong H$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, consider the following diagram.

![uniqueness_1](/assets/images/Math/Algebraic_Structures/Grothendieck_Groups-2.svg){:style="width:6.91em"  class="invert" .align-center}

Then by the universal property, there exists a map $$\bar{\eta}_S': K(S)\rightarrow H$$ such that $$\eta_S'= \bar{\eta}_S'\circ\eta_S$$. On the other hand, from the following diagram

![uniqueness_2](/assets/images/Math/Algebraic_Structures/Grothendieck_Groups-3.svg){:style="width:6.91em"  class="invert" .align-center}

using the universal property for $$H$$, there exists a map $$\bar{\eta}_S:H\rightarrow K(S)$$ such that $$\eta_S=\bar{\eta}_S\circ\eta_S'$$. Then

$$\bar{\eta}_S'\circ\bar{\eta}_S\circ\eta_S'=\bar{\eta}_S'\circ \eta_S=\eta=\id_{H}\circ \eta_S' $$

and by the universal property again, the map $$f$$ satisfying $$f\circ \eta_S'=\eta_S'$$ is unique, so $$f=\id_H=\bar{\eta}_S'\circ \bar{\eta}_S$$. Or, in the language of diagrams, the unique map $$H\rightarrow H$$ making the following diagram commute must be $$\id_H=\bar{\eta}_S'\circ \bar{\eta}_S$$.

![uniqueness_3](/assets/images/Math/Algebraic_Structures/Grothendieck_Groups-4.svg){:style="width:9.96em"  class="invert" .align-center}

Similarly, one can show that $$\id_{K(S)}=\bar{\eta}_S\circ \bar{\eta}_S'$$, and therefore $$K(S)\cong H$$.
</details>

On the other hand, if $$S$$ is already an abelian group, then $$K(S)$$ should be $$S$$ itself without adjoining any new elements.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> If $$S$$ is an abelian group, then the abelian group $$K(S)$$ satisfying the above universal mapping problem is isomorphic to $$S$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Since $$S$$ and $$\id_S$$ trivially satisfy the universal property, by [Proposition 1](#prop1), any abelian group satisfying the universal property must be isomorphic to $$S$$.

</details>

The above propositions show that a $$K(S)$$ satisfying the universal mapping problem is the abelian group we seek, but they do not establish that such a $$K(S)$$ actually exists.

## Definition of $$K(S)$$

The reason why $$S$$ cannot be an abelian group is that inverses may not exist for all elements. Intuitively, this can be resolved by adding *negatives*.

Given a commutative semigroup $$(S,+)$$, consider the product semigroup $$S\times S$$. ([§Algebraic Structures, ⁋Example 5](/en/math/algebraic_structures/algebraic_structures#ex5)) Interpreting the second component of $$S\times S$$ as a negative, the equation

$$(a_1, b_1)+(a_2, b_2)=(a_1+a_2, b_1+b_2)$$

can be viewed as representing

$$(a_1+a_2)-(b_1+b_2)=(a_1-b_1)+(a_2-b_2)$$

Of course, in general the formal difference $$a-b$$ is far from well-defined, so we define an equivalence relation $$R$$ on $$S\times S$$ as follows.

$$(a_1, b_1)\equiv (a_2, b_2)\pmod{R}\iff a_1+b_2+c=a_2+b_1+c\text{ for some $c\in S$}$$

First, we show that this relation is an equivalence relation.

<div class="proposition" markdown="1">

<ins id="lem3">**Lemma 3**</ins> The relation $$R$$ defined above is an equivalence relation on the product semigroup $$S\times S$$ compatible with its operation.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, we show that $$R$$ is an equivalence relation. For any $$(a,b)\in S\times S$$,

$$a+b+c=a+b+c$$

holds for any $$c\in S$$; hence $$(a,b)\equiv(a,b)$$. Suppose $$(a_1,b_1)\equiv (a_2,b_2)$$. That is, for some $$c\in S$$,

$$a_1+b_2+c=a_2+b_1+c$$

holds. But this is precisely the condition for $$(a_2,b_2)\equiv (a_1,b_1)$$, so $$R$$ is symmetric. Finally, suppose $$(a_1,b_1)\equiv(a_2,b_2)$$ and $$(a_2,b_2)\equiv (a_3,b_3)$$. Then for some $$c$$ and $$c'$$,

$$a_1+b_2+c=a_2+b_1+c,\qquad a_2+b_3+c'=a_3+b_2+c'$$

hold. Adding the two equations,

$$a_1+b_3+(a_2+b_2+c+c')=a_3+b_1+(a_2+b_2+c+c')$$

so $$(a_1,b_1)\equiv(a_3,b_3)$$. Thus $$R$$ is an equivalence relation.

Now we must show that $$R$$ is compatible with the operation on $$S\times S$$. To this end, suppose $$(a_1, b_1)\equiv(a_1',b_1')$$ and $$(a_2, b_2)\equiv (a_2',b_2')$$. We must show that $$(a_1+a_2, b_1+b_2)\equiv(a_1'+a_2', b_1'+b_2')$$. By the given conditions, there exist $$c_1$$ and $$c_2$$ such that

$$a_1+b_1'+c_1=a_1'+b_1+c_1,\qquad a_2+b_2'+c_2=a_2'+b_2+c_2$$

hold. Adding these two equations yields

$$(a_1+a_2)+(b_1'+b_2')+(c_1+c_2)=(a_1'+a_2')+(b_1+b_2)+(c_1+c_2)$$

so by definition $$(a_1+a_2, b_1+b_2)\equiv(a_1'+a_2', b_1'+b_2')\pmod{R}$$. Thus $$R$$ is compatible with the operation on $$S\times S$$.

</details>

Therefore, $$(S\times S)/R$$ is a commutative semigroup. We denote this by $$K(S)$$.

<div class="proposition" markdown="1">

<ins id="lem4">**Lemma 4**</ins> $$K(S)$$ is an abelian group.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

It suffices to show that $$K(S)$$ has an identity element and inverses. Since we regard $$(a,b)$$ as $$a-b$$, the identity element should be of the form $$(a,a)$$, and the inverse of $$(a,b)$$ should be $$-(a-b)=b-a$$, i.e. $$(b,a)$$. Let us prove this.

First, for any $$c\in S$$, we show that $$[(c,c)]$$ is the identity element. For any $$[(a,b)]\in K(S)$$,

$$[(a,b)]+[(c,c)]=[(a+c, b+c)]$$

holds. Since

$$(a+c)+b+d=(b+c)+a+d$$

holds for any $$d\in S$$, we have $$(a+c, b+c)\equiv (a,b)$$, and therefore $$[(a+c, b+c)]=[(a,b)]$$. By commutativity, $$[(c,c)]+[(a,b)]=[(a,b)]$$ also holds, so $$[(c,c)]$$ is the identity element of $$K(S)$$.

On the other hand, for any $$[(a,b)]\in K(S)$$,

$$[(a,b)]+[(b,a)]=[(a+b,a+b)]$$

so by the preceding argument, $$[(a,b)]+[(b,a)]$$ is the identity element of $$K(S)$$, and the same holds for $$[(b,a)]+[(a,b)]$$. Thus every element of $$K(S)$$ has an inverse, so $$K(S)$$ carries a group structure.

</details>

Thus $$K(S)$$ becomes the abelian group we were looking for. That is, $$K(S)$$ satisfies the above universal mapping problem.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> For a commutative semigroup $$(S, +)$$, the abelian group $$K(S)$$ constructed as above, together with the natural semigroup homomorphism $$\eta_S:S\rightarrow K(S)$$, satisfies the universal property.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, let us consider what the *natural semigroup homomorphism* from $$S$$ to $$K(S)$$ should be. Since we regard an element $$(a,b)$$ in $$K(S)$$ as $$a-b$$, we see that $$a$$ corresponds to $$(a+b)-b$$ in $$K(S)$$, i.e. $$[(a+b, b)]$$. Therefore, we define $$\eta_S$$ by $$a\mapsto[(a+a, a)]$$. Of course, choosing any $$b$$ and defining $$a\mapsto[(a+b,b)]$$ yields the same element.

To prove the universal property, let an arbitrary abelian group $$G$$ and a semigroup homomorphism $$f:S\rightarrow G$$ be given.

First, if $$\bar{f}:K(S)\rightarrow S$$ satisfying the given property exists, then $$\bar{f}$$ must be unique. For any $$[(a,b)]$$,

$$\begin{aligned}\bar{f}\left([(a,b)]\right)&=\bar{f}\left([(a+(a+b), b+(a+b))]\right)=\bar{f}\left([(a+a,a)]+[(b, b+b)]\right)\\ &\bar{f}\left([(a+a, a)]\right)+\bar{f}\left([(b,b+b)]\right)=\bar{f}\left(\eta_S(a)\right)-\bar{f}\left(\eta_S(b)\right)\\ &=f(a)-f(b)\end{aligned}$$

so its values on individual elements are uniquely determined.

Guided by the uniqueness argument, we define $$\bar{f}([(a,b)])=f(a)-f(b)$$. First, this definition is well defined. That is, if $$(a_1,b_1)\equiv(a_2,b_2)$$, then $$f(a_2)-f(b_2)=f(a_1)-f(b_1)$$. Since $$(a_1,b_1)\equiv(a_2,b_2)$$, there exists $$c\in S$$ such that $$a_1+b_2+c=a_2+b_1+c$$; therefore

$$f(a_1)+f(b_2)+f(c)=f(a_1+b_2+c)=f(a_2+b_1+c)=f(a_2)+f(b_1)+f(c)$$

Subtracting $$f(c)$$ from both sides and rearranging, we obtain

$$f(a_1)-f(b_1)=f(a_2)-f(b_2)$$

Moreover, $$\bar{f}$$ is a group homomorphism. For any $$[(a_1, b_1)]$$ and $$[(a_2,b_2)]$$,

$$\begin{aligned}\bar{f}\left([(a_1,b_1)]+[(a_2, b_2)]\right)&=\bar{f}\left([(a_1+a_2, b_1+b_2)]\right)=f(a_1+a_2)-f(b_1+b_2)\\&=f(a_1)+f(a_2)-f(b_1)-f(b_2)=(f(a_1)-f(b_1))+(f(a_2)-f(b_2))\\&=\bar{f}\left([(a_1, b_1)]\right)+\bar{f}\left([(a_2,b_2)]\right)\end{aligned}$$

holds.

Finally, that $$\bar{f}$$ satisfies the required condition $$f=\bar{f}\circ\eta_S$$ follows by a direct computation.

</details>

Thus, we have obtained the desired abelian group $$K(S)$$. In particular, this yields a rigorous definition of the integers.

<div class="definition" markdown="1">

<ins id="def6">**Definition 6**</ins> For the monoid $$(\mathbb{N},+)$$, the abelian group obtained through the above process is denoted by $$(\mathbb{Z},+)$$.

</div>

## Monoid of fractions

In the above discussion, we obtained $$K(S)$$ by adjoining inverses for all elements of $$S$$. On the other hand, looking at [Definition 6](#def6), what we are actually doing is adjoining inverses only for the elements of the subset $$\mathbb{N}\setminus\{0\}$$ of $$\mathbb{N}$$. This can also be achieved with slight modifications to the above discussion; we omit the proofs and only sketch the process.

Consider a commutative monoid $$E$$, a subset $$S$$ of $$E$$, and the submonoid $$S'$$ of $$E$$ generated by $$S$$. We also assume that the operation of $$E$$ is written as multiplication. Define the following relation on $$E\times S'$$:

$$(a,p)\equiv (b,q)\pmod{R}\iff aqs=bps\text{ for some $s\in S'$}$$

Then this relation is an equivalence relation on $$E\times S'$$ compatible with its operation, so $$(E\times S')/R$$ is a monoid.

<div class="definition" markdown="1">

<ins id="def7">**Definition 7**</ins> The monoid $$(E\times S')/R$$ obtained as above is called the *monoid of fractions* of $$E$$ with denominator $$S$$, denoted by $$E_S$$. Elements $$(a,p)$$ of this monoid are denoted by $$a/p$$.

</div>

In this case, since $$E$$ is a monoid, unlike in the above discussion, it has an identity element $$1$$. Then the homomorphism $$\eta_S$$ in [Proposition 5](#prop5) can be described explicitly as $$a\mapsto a/1$$.

---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.

---
