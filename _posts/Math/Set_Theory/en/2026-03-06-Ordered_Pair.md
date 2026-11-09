---
title: "Ordered Pairs"
description: "We examine set inclusion as a binary relation, then define ordered pairs as sets and prove their existence and uniqueness."
excerpt: "Set inclusion and the definition of ordered pairs"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/ordered_pair


sidebar: 
    nav: "set_theory-en"

date: 2021-08-09

weight: 2
translated_at: 2026-06-02T10:00:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-31T15:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
## Subset Relations

::: Definition 1
$A\subseteq B$ means that for any $x$, the proposition $x\in A\implies x\in B$ is always true.
:::

The following two propositions are two properties of $\subseteq$.

::: Proposition 2
$A\subseteq A$ always holds.
:::
::: Proof
$x\in A\implies x\in A$ is always true.
:::

::: Proposition 3
If $A\subseteq B$ and $B\subseteq C$, then $A\subseteq C$.
:::
::: Proof
First, the premise means that for any $x$, the two propositions $x\in A\implies x\in B$ and $x\in B\implies x\in C$ are true. Therefore, by syllogism, $x\in A\implies x\in C$ is also true, and since $x$ can be chosen arbitrarily, $A\subseteq C$ holds.
:::

From the two propositions above and the axiom of extensionality that if $A\subseteq B$ and $B\subseteq A$, then $A=B$, we know that $\subseteq$ is an order relation between sets. ([§Definition of Order Relations, ⁋Definition 2](/en/math/set_theory/order_relations#def2){: data-lid="kqyue" })

## Ordered Pairs

Almost the only tool we will use in set theory is a binary relation, and the language expressing it is the ordered pair. For example, the binary relation $\subseteq$ examined above can be thought of as the "set" collecting pairs satisfying $A\subseteq B$ into ordered pairs $(A,B)$,

$$\subseteq=\{(A,B),(B,C),\cdots\}$$

.[^1] Similarly, a function $y=f(x)$ can be thought of as the following set

$$F=\{(x_1,f(x_1)), (x_2,f(x_2)),\cdots\}$$

and an *equivalence relation*, which we have not yet defined, can also be represented as a set of ordered pairs in this way.

However, among the sets we have defined, there is no tool that can play the role of the ordered pair learned in middle and high school. For instance, since $\{A,B\}=\{B,A\}$, simply using the axiom of pair once does not allow us to distinguish the order of $A$ and $B$.

::: Definition 4
We define the *ordered pair* $(x,y)$ as the set $\big\{\{x\}, \{x,y\}\big\}$.
:::

For the above definition to be meaningful, we must first show the following lemma.[^2]

::: Lemma 5
For two sets $x$, $y$, the set $(x,y)$ always exists and is unique.
:::
::: Proof
The sets $\{x\}=\{x,x\}$ and $\{x,y\}$ each exist by the axiom of pair, and therefore the set $\big\{\{x\}, \{x,y\}\big\}$ also exists by the axiom of pair again.

For uniqueness, $\{x\}=\{x,x\}$ and $\{x,y\}$ are first determined uniquely, and then the set $(x,y)$ obtained by applying the axiom of pair to them again is also uniquely determined; this can be verified by using extensionality twice.
:::

We have confirmed that the ordered pair $(x,y)$ is well-defined, but we must check whether, for general $x,y$, the ordered pair defined in this way satisfies $(x,y)\neq (y,x)$.

::: Proposition 6
For two ordered pairs $(x,y)$, $(x',y')$, that $(x,y)=(x',y')$ is equivalent to $x=x'$ and $y=y'$.
:::
::: Proof
If $x=x'$ and $y=y'$, then $(x,y)=(x', y')$ is obvious, because $\{x\}=\{x'\}$ and $\{x,y\}=\{x', y'\}$.

Now conversely suppose $(x,y)=(x',y')$. By definition,

$$\big\{\{x\},\{x,y\}\big\}=\big\{\{x'\},\{x',y'\}\big\}$$

holds. Since exactly one of $x=y$ and $x\neq y$ must hold, let us approach by dividing into two cases.

- If $x=y$, the left-hand side of the above equation becomes

    $$\big\{\{x\},\{x,x\}\big\}=\big\{\{x\},\{x\}\big\}=\big\{\{x\}\big\}$$

    so $\big\{\{x\}\big\}=\big\{\{x'\},\{x',y'\}\big\}$. Hence $\{x\}=\{x'\}=\{x',y'\}$, so $x=x'=y'$ and therefore $x=x'=y=y'$. That is, $x=x'$ and $y=y'$.

- The remaining case is $x\neq y$. In this case, since $\{x,y\}\neq\{x'\}$, for the two ordered pairs to be equal we must have $\{x\}=\{x'\}$ and $\{x,y\}=\{x',y'\}$. Then from $\{x\}=\{x'\}$ we must have $x=x'$, and from this and $\{x,y\}=\{x',y'\}$ we must have $y=y'$.
:::

For an ordered pair $z=(x,y)$, consider the set

$$\bigcup z=\{x\}\cup\{x,y\}=\{x,y\}$$

. Now, if we define the property

> $P(s)$: there exists some $t$ such that $z=(s,t)$,

we obtain the subset of the preceding set $\bigcup z$

$$\left\{s\in\bigcup z\mid P(s)\right\}$$

. This set is the singleton $\{x\}$. If we define the property $Q$ similarly well, we obtain the singleton $\{y\}$.

::: Definition 7
For the two sets $\{x\}$, $\{y\}$ obtained by the above process, we call the unique element of $\{x\}$, $x$, the *first component* of $z=(x,y)$, and the unique element of $\{y\}$, $y$, the *second component* of $z=(x,y)$, and denote them respectively by

$$x=\pr_1 z,\qquad y=\pr_2 z$$
:::

Here $\pr$ is short for **pr**ojection. Meanwhile, for two sets $A$, $B$, we can define the product $A\times B$ as follows.

::: Definition 8
For two sets $A$, $B$, we call the following set

$$\{z\mid(z=(x,y))\wedge (x\in A)\wedge(y\in B)\}$$

the *cartesian product* of $A$ and $B$, and simply denote it by $A\times B$.

Also, similarly to [Definition 7](#def7){: data-lid="1888f" }, we call the sets $A$ and $B$ the first and second components of $A\times B$.
:::

To know the condition under which two product sets $A\times B$ and $A'\times B'$ become equal, it suffices to determine definitively when one product set is *contained* in the other.

::: Proposition 9
For four sets $A$, $B$, $A'$, $B'$, if $A'$ and $B'$ are nonempty, then $A'\times B'\subseteq A\times B$ is equivalent to $A'\subseteq A$ and $B'\subseteq B$.
:::
::: Proof
First, assume $A'\times B'\subseteq A\times B$. Since we must show $A'\subseteq A$, let an arbitrary $a'\in A'$ be given and show that $a'\in A$.  
Since $B'$ is nonempty, there exists some element $b'\in B'$. Hence $(a',b')\in A'\times B'$, and since $A'\times B'\subseteq A\times B$, we have $(a',b')\in A\times B$ and $a'\in A$. Similarly, $B'\subseteq B$ can also be shown.

Conversely, suppose $A'\subseteq A$ and $B'\subseteq B$. Given an arbitrary $z'\in A'\times B'$, we must show that $z'\in A\times B$.  
Let $z'=(a',b')$. That is, $a'\in A'$ and $b'\in B'$, and by hypothesis $a'$ and $b'$ are also elements of $A$ and $B$, so $(a',b')\in A\times B$.
:::

When one of $A,B$ is empty, the following proposition can be applied.

::: Proposition 10
For two sets $A$, $B$, the statement $A\times B=\emptyset$ is equivalent to $A=\emptyset$ or $B=\emptyset$.
:::
::: Proof
First, suppose $A\times B=\emptyset$. If both $A$ and $B$ are nonempty, we can pick some $a\in A$ and $b\in B$, so that $(a,b)\in A\times B$, which is a contradiction.

Conversely, assume $A$ or $B$ is empty. Again, negating the conclusion, if $A\times B$ is nonempty, there exists some element $(a,b)\in A\times B$. Thus $a\in A$ and $b\in B$, which contradicts the assumption that $A$ or $B$ is empty.
:::

---
**References**

**[HJJ]** K. Hrbacek, T.J. Jeck, and T. Jech. *Introduction to Set Theory*. Lecture Notes in Pure and Applied Mathematics. M. Dekker, 1978.  
**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---

[^1]: Of course, this "set" is not a set. ([§ZFC Axioms, ⁋Example 4](/en/math/set_theory/zfc_axioms#ex4){: data-lid="p57o8" })
[^2]: From the end of the proof of this lemma onward, we no longer mention the axioms used in the proof process.
