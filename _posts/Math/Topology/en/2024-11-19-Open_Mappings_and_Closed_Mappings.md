---
title: "Open Mappings and Closed Mappings"
description: "This post defines open maps and closed maps between topological spaces and examines their basic properties for composite, surjective, and injective functions. It also discusses criteria for determining when a map is open or closed."
excerpt: "Definitions of open and closed maps and their relationship to quotient maps"

categories: [Math / Topology]
permalink: /en/math/topology/open_mappings_and_closed_mappings
sidebar: 
    nav: "topology-en"

date: 2024-11-19
weight: 12
translated_at: 2026-06-03T06:00:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-11-09T15:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
## Definitions and Basic Properties

::: Definition 1
For any two topological spaces $X,Y$ and a function $f:X \rightarrow Y$, we define the following. 

1. If, in $X$, for any open set $U$, $f(U)$ is always an open set of $Y$, then we call $f$ an *open mapping*. 
2. If, in $X$, for any closed set $A$, $f(A)$ is always a closed set of $Y$, then we call $f$ a *closed mapping*. 
:::

Then the following holds.

::: Proposition 2
Let topological spaces $X,Y,Z$ and functions $f:X \rightarrow Y$, $g:Y \rightarrow Z$ be given. Then the following holds. 

1. If $f, g$ are both open (resp. closed), then $g\circ f$ is also open (resp. closed).
2. If $g\circ f$ is open (resp. closed) and $f$ is a continuous surjection, then $g$ is open (resp. closed). 
3. If $g\circ f$ is open (resp. closed) and $g$ is a continuous injection, then $f$ is open (resp. closed). 
:::
::: Proof
1. In $X$, for any open set (resp. closed set) $U$, since $f$ is open (resp. closed), $f(U)$ is an open set (resp. closed set) of $Y$, and again since $g$ is open (resp. closed), $g(f(U))$ is an open set (resp. closed set) of $Z$. 
2. In $Y$, let an arbitrary open set $V$ be given. Then since $f$ is continuous, $f^{-1}(V)$ is an open set of $X$, and therefore
    
    $$(g\circ f)(f^{-1}(V))=g(f(f^{-1}(V)))=g(V)$$

    holds, so $g(V)$ is an open set of $Z$. Here, that $f(f^{-1}(V))=V$ used that $f$ is a surjection. ([\[Set Theory\] §Retraction and Section, ⁋Definition 2](/en/math/set_theory/retraction_and_section#def2){: data-lid="suv4m" }) Meanwhile, in the same manner, if in $Y$ an arbitrary closed set $B$ is given, then by [§Continuous Functions, ⁋Theorem 4](/en/math/topology/continuous_functions#thm4){: data-lid="ohmya" } the same argument as above can be applied.
3. As in the second proof, it suffices to consider only the open case. In $X$, for any open set $U$, since $g\circ f$ is open, $g(f(U))$ is open, and thus using that $g$ is continuous and the above [\[Set Theory\] §Retraction and Section, ⁋Definition 2](/en/math/set_theory/retraction_and_section#def2){: data-lid="g2zp9" }, from the following formula
    
    $$g^{-1}(g(f(U)))=f(U)$$

    we see that $f(U)$ is an open set.
:::

The following proposition helps determine when a function between topological spaces is open or closed.

::: Proposition 3
Let a function $f:X \rightarrow Y$ between two topological spaces be given. Then the following holds.

1. If $f$ is open (resp. closed), then in $Y$, for any subset $A$, $f\vert_{f^{-1}(A)}: f^{-1}(A) \rightarrow A$ is also open (resp. closed).
2. Suppose a covering of $Y$, $(A_i)_{i\in I}$, is either (1) a locally finite closed covering, or (2) $(\interior A_i)_{i\in I}$ is an open covering of $Y$. If each $f\vert_{f^{-1}(A_i)}$ is open (resp. closed), then so is $f$. 
:::
::: Proof
To show the first result, choose an open set (resp. closed set) in $f^{-1}(A)$. Then in $X$, there exists an open set (resp. closed set) $U$ such that it can be written in the form $U\cap f^{-1}(A)$. Therefore

$$f\vert_{f^{-1}(A)}(U\cap f^{-1}(A))=f(U)\cap A$$

and by assumption $f(U)$ is an open set (resp. closed set), so we obtain the desired result.

The second result can be proved similarly. In $X$, let an open set (resp. closed set) $U$ be given, and define $U_i$ by the following formula

$$U_i=U\cap f^{-1}(A_i)$$

Then $f\vert_{f^{-1}(A_i)}(U_i)=f(U)\cap A_i$ holds, and thus by assumption $f(U)\cap A_i$ is an open set (resp. closed set) of $A_i$ for all $i$. In the case of (1), since each $A_i$ is a closed set, the sets $f(U)\cap A_i$ if $U$ is a closed set, or the sets $A_i\setminus f(U)$ if $U$ is an open set, form a locally finite family of closed sets of $Y$. Therefore, by [§Interior, Closure, and Boundary, ⁋Proposition 4](/en/math/topology/other_concepts#prop4){: data-lid="ej1v1" }, their union $f(U)$ or $Y\setminus f(U)$ is a closed set. In the case of (2), since each $\interior A_i$ is an open set, the sets $f(U)\cap\interior A_i$ if $U$ is an open set, or the sets $(\interior A_i)\setminus f(U)$ if $U$ is a closed set, are open sets of $Y$, and their union $f(U)$ or $Y\setminus f(U)$ is an open set. 
:::

## Equivalence Relations

::: Definition 4
On a topological space $X$, an equivalence relation $R$ is said to be *open (resp. closed)* if the canonical map $X \rightarrow X/R$ is open (resp. closed). 
:::

Then the following can be easily shown.

::: Proposition 5
Between two topological spaces $X,Y$, consider a continuous function $f:X \rightarrow Y$ and the canonical decomposition of $f$

$$X \overset{p}{\rightarrow} X/R \overset{h}{\rightarrow} f(X)\overset{i}{\rightarrow}Y$$

Then the following are all equivalent.

1. $f$ is open (resp. closed).
2. $p,h,i$ are all open (resp. closed).
3. $R$ is open (resp. closed), $h$ is a homeomorphism, and $f(X)$ is an open (resp. closed) subset of $Y$.
:::

## Properties of Open Mappings

We now examine the properties possessed by open mappings and closed mappings, respectively. We begin with the case of open mappings. 

::: Proposition 6
:::

---

**References**

**[Bou]** N. Bourbaki, <i>General Topology</i>. Elements of mathematics. Springer, 1995.
