---
title: "Ordered Pairs"
excerpt: "Subset relations of sets and the definition of ordered pairs"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/ordered_pair

header:
    overlay_image: /assets/images/Math/Set_Theory/Ordered_pair.png
    overlay_filter: 0.5

sidebar: 
    nav: "set_theory-en"

date: 2026-03-06
last_modified_at: 2026-03-06

weight: 2

---

## Subset Relations of Sets

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> $A\subseteq B$ means that for any $x$, the proposition $x\in A\implies x\in B$ is always true.

</div>

The following two propositions are two properties of $\subset$.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> $A\subseteq A$ always holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

$x\in A\implies x\in A$ is always true.

</details>

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> If $A\subseteq B$ and $B\subseteq C$, then $A\subseteq C$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, the premise means that for any $x$, the two propositions $x\in A\implies x\in B$ and $x\in B\implies x\in C$ are true. Therefore, by syllogism, $x\in A\implies x\in C$ is also true, and since $x$ can be chosen arbitrarily, $A\subseteq C$ holds.

</details>

From the above two propositions, we understand that $\subseteq$ becomes an order relation among sets. ([§Definition of Order Relations, ⁋Definition 1](/en/math/set_theory/order_relations#def1))

## Ordered Pairs

Almost the only tool we will use in set theory is the binary relation, and the language used to express it is the ordered pair. For example, the binary relation $\subseteq$ examined above can be thought of as the "set"

$$\subseteq=\{(A,B),(B,C),\cdots\}$$

that collects all ordered pairs $(A,B)$ satisfying $A\subseteq B$.[^1] Similarly, a function $y=f(x)$ can be thought of as the following set

$$F=\{(x_1,f(x_1)), (x_2,f(x_2)),\cdots\}$$

and the *equivalence relation*, which we have not yet defined, can also be represented as a set of ordered pairs in this way.

However, among the sets we have defined, there is no tool that can serve the role of ordered pairs that we learned in middle and high school. For example, since $\\{A,B\\}=\\{B,A\\}$, we cannot distinguish the order of $A$ and $B$ simply by using the axiom of pair once.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> An *ordered pair* $(x,y)$ is defined as the set $\big\\{\\{x\\}, \\{x,y\\}\big\\}$.

</div>

For the above definition to have meaning, we must first prove the following lemma.[^2]

<div class="proposition" markdown="1">

<ins id="lem5">**Lemma 5**</ins> For two sets $x$, $y$, the set $(x,y)$ always exists and is unique.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

The sets $\\{x\\}=\\{x,x\\}$ and $\\{x,y\\}$ each exist by the axiom of pair, and therefore the set $\big\\{\\{x\\}, \\{x,y\\}\big\\}$ also exists by the axiom of pair.

For uniqueness, $\\{x\\}=\\{x,x\\}$ and $\\{x,y\\}$ are first uniquely determined, and by applying the axiom of pair to these again, we can verify that the set $(x,y)$ obtained is also uniquely determined by using extensionality twice.

</details>

We have confirmed that the ordered pair $(x,y)$ is well-defined, but we need to verify whether the ordered pair defined this way satisfies $(x,y)\neq (y,x)$ for general $x,y$.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> For two ordered pairs $(x,y)$ and $(x',y')$, <phrase>$(x,y)=(x',y')$</phrase> and <phrase>$x=x'$ and $y=y'$</phrase> are equivalent.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

If $x=x'$ and $y=y'$, then $(x,y)=(x', y')$ is obvious. This is because $\\{x\\}=\\{x'\\}$ and $\\{x,y\\}=\\{x', y'\\}$.

Now, conversely, assume $(x,y)=(x',y')$. By definition,

$$\big\{\{x\},\{x,y\}\big\}=\big\{\{x'\},\{x',y'\}\big\}$$

holds. Since exactly one of $x=y$ and $x\neq y$ must hold, let us approach by dividing into two cases.

- If $x=y$, the left side of the above equation becomes

    $$\big\{\{x\},\{x,x\}\big\}=\big\{\{x\},\{x\}\big\}=\big\{\{x\}\big\}$$

    so $\big\\{\\{x\\}\big\\}=\big\\{\\{x'\\},\\{x',y'\\}\big\\}$. Therefore, $\\{x\\}=\\{x'\\}=\\{x',y'\\}$, so $x=x'=y'$, and thus $x=x'=y=y'$. That is, since $x=x'$ and $y=y'$, the proof is complete for this case.

- The remaining case is $x\neq y$. In this case, since $\\{x,y\\}\neq\\{x'\\}$, for the two ordered pairs to be equal, we must have $\\{x\\}=\\{x'\\}$ and $\\{x,y\\}=\\{x',y'\\}$. Then from $\\{x\\}=\\{x'\\}$, we must have $x=x'$, and from this and $\\{x,y\\}=\\{x',y'\\}$, we must have $y=y'$. Thus, the proof is complete for this case as well.

</details>

Consider the set

$$\bigcup z=\{x\}\cup\{x,y\}=\{x,y\}$$

Now, if we define the property

> $P(s)$: There exists some $t$ such that $z=(s,t)$.

then we obtain the subset

$$\left\{s\in\bigcup z\mid P(s)\right\}$$

of the preceding set $\bigcup z$. This set is the singleton $\\{x\\}$. If we define a property $Q$ similarly, we obtain the singleton $\\{y\\}$.

<div class="definition" markdown="1">

<ins id="def7">**Definition 7**</ins> For the two sets $\\{x\\}$, $\\{y\\}$ obtained by the above process, the unique element $x$ of $\\{x\\}$ is called the *first component* of $z=(x,y)$, and the unique element $y$ of $\\{y\\}$ is called the *second component* of $z=(x,y)$. These are denoted respectively as

$$x=\pr_1 z,\qquad y=\pr_2 z$$

</div>

Here, $\pr$ is an abbreviation for **pr**ojection. Meanwhile, we can define the product $A\times B$ of two sets $A$ and $B$ as follows.

<div class="definition" markdown="1">

<ins id="def8">**Definition 8**</ins> For two sets $A$ and $B$, the following set

$$\{z\mid(z=(x,y))\wedge (x\in A)\wedge(y\in B)\}$$

is called the *cartesian product* of $A$ and $B$, and is simply denoted as $A\times B$.

Also, similar to [Definition 7](#def7), the sets $A$ and $B$ are called the first and second components of $A\times B$.

</div>

To determine the conditions under which two product sets $A\times B$ and $A'\times B'$ become equal, we only need to determine when one product set is *contained* in another.

<div class="proposition" markdown="1">

<ins id="prop9">**Proposition 9**</ins> For two non-empty sets $A'$ and $B'$, <phrase>$A'\times B'\subseteq A\times B$</phrase> and <phrase>$A'\subseteq A$ and $B'\subseteq B$</phrase> are equivalent.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, assume $A'\times B'\subseteq A\times B$. We need to show $A'\subseteq A$, so let any $a'\in A'$ be given and show that $a'\in A$.
Since $B'$ is not empty, there exists some element $b'\in B'$. Therefore $(a',b')\in A'\times B'$, and since $A'\times B'\subseteq A\times B$, we have $(a',b')\in A\times B$ and $a'\in A$. Similarly, we can show $B'\subseteq B$.

Conversely, assume $A'\subseteq A$ and $B'\subseteq B$. We need to show that when any $z'\in A'\times B'$ is given, $z'\in A\times B$.
Let $z'=(a',b')$. That is, $a'\in A'$ and $b'\in B'$, but by assumption, $a'$ and $b'$ are also elements of $A$ and $B$, so $(a,b)\in A\times B$.

</details>

When one of $A,B$ is empty, the following proposition can be applied.

<div class="proposition" markdown="1">

<ins id="prop10">**Proposition 10**</ins> For two sets $A$ and $B$, <phrase>$A\times B=\emptyset$</phrase> and <phrase>$A=\emptyset$ or $B=\emptyset$</phrase> are equivalent.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, assume $A\times B=\emptyset$. If both $A$ and $B$ are non-empty, we can pick some $a\in A$ and $b\in B$, so $(a,b)\in A\times B$, which is a contradiction.

Conversely, assume $A$ or $B$ is empty. Again, by contradiction, if $A\times B$ is non-empty, there exists some element $(a,b)\in A\times B$. Therefore $a\in A$ and $b\in B$, which contradicts the assumption that $A$ or $B$ is empty. The proof is complete.

</details>

---
**References**

**[HJJ]** K. Hrbacek, T.J. Jeck, and T. Jech. *Introduction to Set Theory*. Lecture Notes in Pure and Applied Mathematics. M. Dekker, 1978.  
**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---

[^1]: Of course, this "set" is not a set. ([§ZFC Axioms, ⁋Example 4](/en/math/set_theory/zfc_axioms#ex4))
[^2]: With the proof of this lemma, we will no longer mention the axioms used in proofs.
