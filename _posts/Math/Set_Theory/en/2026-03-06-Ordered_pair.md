---
title: "Ordered Pair"
excerpt: "The definition of ordered pairs in set theory"

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

## Inclusion Relation of Sets

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> $A\subseteq B$ means that for any $x$, the proposition $x\in A\implies x\in B$ is always true.

</div>

The following two propositions are properties of $\subset$.

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

From the above two propositions, we know that $\subseteq$ is an order relation between sets.

## Ordered Pair

The almost only tool we use in set theory is binary relations, and the language to express them is ordered pairs. For example, the binary relation $\subseteq$ we saw above can be thought of as a "set"

$$\subseteq=\{(A,B),(B,C),\cdots\}

along with all ordered pairs $(A,B)$ satisfying $A\subseteq B$. Similarly, a function $y=f(x)$ can be thought of as the set

$$F=\{(x_1,f(x_1)), (x_2,f(x_2)),\cdots\}

and the *equivalence relation* we haven't defined yet can also be represented as a set of ordered pairs like this.

However, among the sets we've defined, there's no tool that plays the role of the ordered pairs we learned in middle and high school. For example, since $\\{A,B\\}=\\{B,A\\}$, we cannot distinguish the order of $A$ and $B$ by simply using the axiom of pair once.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> An *ordered pair* $(x,y)$ is defined as the set $\{\{x\}, \{x,y\}\}$.

</div>

For the above definition to make sense, we must first show the following lemma.

<div class="proposition" markdown="1">

<ins id="lem5">**Lemma 5**</ins> For two sets $x$ and $y$, the set $(x,y)$ always exists and is unique.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

The set $\\{x\\}=\\{x,x\\}$ and $\\{x,y\\}$ exist by the axiom of pair, and therefore the set $\\{\\{x\\}, \\{x,y\\}\\}$ also exists by the axiom of pair again.

For uniqueness, we can verify that the sets $\\{x\\}=\\{x,x\\}$ and $\\{x,y\\}$ are uniquely determined first, and then the set $(x,y)$ obtained by applying the axiom of pair to them is also uniquely determined by applying extensionality twice.

</details>

We've confirmed that the ordered pair $(x,y)$ is well-defined, but we need to check whether this defined ordered pair satisfies $(x,y)\neq (y,x)$ for general $x,y$.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> For two ordered pairs $(x,y)$ and $(x',y')$, the statement "$(x,y)=(x',y')$" is equivalent to "$x=x'$ and $y=y'$".

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

If $x=x'$ and $y=y'$, then $(x,y)=(x', y')$ is obvious. This is because $\\{x\\}=\\{x'\\}$ and $\\{x,y\\}=\\{x',y'\\}$.

Now suppose the other direction $(x,y)=(x',y')$. By definition,

$$\big\{\{x\},\{x,y\}\big\}=\big\{\{x'\},\{x',y'\}\big\}

holds. Since exactly one of $x=y$ and $x\neq y$ must hold, let's approach by dividing into two cases.

- If $x=y$, then the left side of the above equation is

    $$\big\{\{x\},\{x,x\}\big\}=\big\{\{x\},\{x\}\big\}=\big\{\{x\}\big\}

    so $\big\\{\\{x\\}\big\\}=\big\\{\\{x'\\},\\{x',y'\\}\big\\}$. Therefore $\\{x\\}=\\{x'\\}=\\{x',y'\\}$, so $x=x'=y'$ and thus $x=x'=y=y'$. That is, $x=x'$ and $y=y'$, so this case is proven.

- The remaining case is $x\neq y$. In this case, $\\{x,y\\}\neq\\{x'\\}$ so for the two ordered pairs to be equal, it must necessarily be that $\\{x\\}=\\{x'\\}$ and $\\{x,y\\}=\\{x',y'\\}$. Then from $\\{x\\}=\\{x'\\}$ we must have $x=x'$, and from $\\{x,y\\}=\\{x',y'\\}$ we must have $y=y'$. Therefore this case is also proven.

</details>

Consider the set

$$\bigcup z=\{x\}\cup\{x,y\}=\{x,y\}$$

Now define the following property

> $P(s)$: There exists some $t$ such that $z=(s,t)$.

and we obtain the subset of the earilier set $\bigcup z$:

$$\left\{s\in\bigcup z\mid P(s)\right\}.$$

This is a singleton 