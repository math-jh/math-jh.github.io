---
title: "Open Mappings and Closed Mappings"
description: "This post defines open maps and closed maps between topological spaces, and examines their basic properties under composition, surjection, and injection. It also discusses criteria for determining when a map is open or closed."
excerpt: "Definitions of open maps and closed maps, and their relationship to quotient maps"

categories: [Math / Topology]
permalink: /en/math/topology/open_mappings_and_closed_mappings
sidebar: 
    nav: "topology-en"

date: 2024-11-19
weight: 12
translated_at: 2026-06-03T06:00:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-03T06:00:02+00:00
---
## Definitions and Basic Properties

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> For any two topological spaces $$X,Y$$ and a function $$f:X \rightarrow Y$$, we define the following. 

1. If for every open set $$U$$ of $$X$$, the image $$f(U)$$ is always an open set of $$Y$$, then we call $$f$$ an *open mapping*. 
2. If for every closed set $$A$$ of $$X$$, the image $$f(A)$$ is always a closed set of $$Y$$, then we call $$f$$ a *closed mapping*. 

</div>

Then the following holds.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> Let topological spaces $$X,Y,Z$$ and functions $$f:X \rightarrow Y$$, $$g:Y \rightarrow Z$$ be given. Then the following holds. 

1. If $$f$$ and $$g$$ are both open (resp. closed), then $$g\circ f$$ is also open (resp. closed).
2. If $$g\circ f$$ is open (resp. closed) and $$f$$ is a continuous surjection, then $$g$$ is open (resp. closed). 
3. If $$g\circ f$$ is open (resp. closed) and $$g$$ is a continuous injection, then $$f$$ is open (resp. closed). 

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>
1. Obvious. 
2. Let $$V$$ be an arbitrary open set of $$Y$$. Then since $$f$$ is continuous, $$f^{-1}(V)$$ is an open set of $$X$$, and thus
    
    $$(g\circ f)(f^{-1}(V))=g(f(f^{-1}(V)))=g(V)$$

    holds, so $$g(V)$$ is an open set of $$Z$$. Here we used that $$f(f^{-1}(V))=V$$ since $$f$$ is a surjection. ([\[Set Theory\] §Retraction and Section, ⁋Definition 2](/en/math/set_theory/retraction_and_section#def2)) On the other hand, if $$B$$ is an arbitrary closed set of $$Y$$, then by [§Continuous Functions, ⁋Theorem 4](/en/math/topology/continuous_functions#thm4) we can apply the same argument as above.
3. As in the second proof, it suffices to consider the open case. For any open set $$U$$ of $$X$$, since $$g\circ f$$ is open, $$g(f(U))$$ is open, and thus using that $$g$$ is continuous and the above [\[Set Theory\] §Retraction and Section, ⁋Definition 2](/en/math/set_theory/retraction_and_section#def2), from the following formula
    
    $$g^{-1}(g(f(U)))=f(U)$$

    we see that $$f(U)$$ is an open set.

</details>

The following proposition helps determine when a function between topological spaces is open or closed.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> Let a function $$f:X \rightarrow Y$$ between two topological spaces be given. Then the following holds.

1. If $$f$$ is open (resp. closed), then for any subset $$A$$ of $$Y$$, the restriction $$f\vert_{f^{-1}(A)}: f^{-1}(A) \rightarrow A$$ is also open (resp. closed).
2. Let $$(A_i)_{i\in I}$$ be a covering of $$Y$$ that is either (1) a locally finite closed covering, or (2) $$(\interior A_i)_{i\in I}$$ is an open covering of $$Y$$. If each restriction $$f\vert_{f^{-1}(A_i)}$$ is open (resp. closed), then so is $$f$$. 

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

To show the first result, choose an open set (resp. closed set) in $$f^{-1}(A)$$. Then there exists an open set (resp. closed set) $$U$$ in $$X$$ such that we can write it in the form $$U\cap f^{-1}(A)$$. Therefore

$$f\vert_{f^{-1}(A)}(U)=f(U)\cap A$$

holds, and by assumption $$f(U)$$ is an open set (resp. closed set), so we obtain the desired result.

The second result can be proved similarly. Let $$U$$ be an open set (resp. closed set) in $$X$$, and define $$U_i$$ by the following formula

$$U_i=U\cap f^{-1}(A_i)$$

Then $$f\vert_{f^{-1}(A_i)}(U_i)=f(U)\cap A_i$$ holds, and thus by assumption $$f(U)\cap A_i$$ is an open set (resp. closed set) for all $$i$$. Therefore, if $$U$$ is an open set then $$f(U)$$ is a union of open sets and hence open, and if $$U$$ is a closed set then by [§Interior, Closure, and Boundary, ⁋Proposition 4](/en/math/topology/other_concepts#prop4) it is a closed set. 

</details>

## Equivalence Relations

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> An equivalence relation $$R$$ defined on a topological space $$X$$ is said to be *open (resp. closed)* if the canonical map $$X \rightarrow X/R$$ is open (resp. closed). 

</div>

Then the following can be easily shown.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> Consider a continuous function $$f:X \rightarrow Y$$ between two topological spaces and its canonical decomposition

$$X \overset{p}{\longrightarrow} X/R \overset{h}{\longrightarrow} f(X)\overset{i}{\longrightarrow}Y$$

Then the following are all equivalent.

1. $$f$$ is open (resp. closed).
2. $$p$$, $$h$$, and $$i$$ are all open (resp. closed).
3. $$R$$ is open (resp. closed), $$h$$ is a homeomorphism, and $$f(X)$$ is an open (resp. closed) subset of $$Y$$.

</div>

## Properties of Open Mappings

We now examine the properties possessed by open mappings and closed mappings, respectively. We begin with the case of open mappings. 

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> 

</div>
