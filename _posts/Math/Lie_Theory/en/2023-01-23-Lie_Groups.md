---
title: "Lie Groups"
excerpt: "Definitions and properties of Lie groups"

categories: [Math / Lie Theory]
permalink: /en/math/lie_theory/Lie_groups
header:
    overlay_image: /assets/images/Math/Lie_Theory/Lie_Groups.png
    overlay_filter: 0.5
sidebar: 
    nav: "Lie_theory-en"

date: 2023-01-23
last_modified_at: 2025-11-06
weight: 1
translated_at: 2026-05-21T21:00:01+00:00
translation_source: kimi-cli
---
In the posts in this category we cover Lie groups and Lie algebras. The definition of a Lie group is very simple.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A group $$G$$ is called a *Lie group* if $$G$$ itself has a manifold structure and, with respect to this manifold structure, the following function

$$G\times G\rightarrow G;\qquad (x,y)\mapsto xy^{-1}$$

is $$C^\infty$$.

</div>

In other words, a Lie group is itself a group, and at the same time a smooth manifold equipped with a differentiable structure that makes the two operations defining this group—multiplication and inversion—smooth. More generally, a topological space whose group operations are continuous is called a *topological group*, but we do not need this generalization right away.

Then a morphism between two Lie groups $$G, H$$ means a smooth map $$f:G \rightarrow H$$ that is also a group homomorphism. These data define the category $$\LieGrp$$, and the notion of isomorphism here is also
