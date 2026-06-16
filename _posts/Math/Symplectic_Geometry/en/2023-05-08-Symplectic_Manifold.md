---
title: "Symplectic Manifolds"
description: "This post introduces symplectic manifolds through the concept of a symplectic form defined on a manifold. It covers the basic properties and structure of symplectic manifolds, which exist only in even dimensions."
excerpt: "Definitions and properties of symplectic manifolds"

categories: [Math / Symplectic Geometry]
permalink: /en/math/symplectic_geometry/symplectic_manifold
sidebar: 
    nav: "symplectic_geometry-en"

date: 2023-05-08
weight: 3
translated_at: 2026-06-03T00:00:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-03T00:00:02+00:00
---
In **[MS]**, symplectic vector spaces are introduced, after which additional time is spent on the Maslov class and related topics. We will defer these to later, introducing them as needed in the context of Floer theory, and for now follow **[Cd]** in first defining symplectic manifolds.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A *symplectic form* $$\omega$$ on a manifold $$M$$ is a differential $$2$$-form such that $$d\omega=0$$ and, for every $$p\in M$$, the map $$\omega_p:T_pM\times T_pM\rightarrow \mathbb{R}$$ is a linear symplectic form. We then call $$(M,\omega)$$ a *symplectic manifold*.

</div>

For a symplectic manifold $$(M,\omega)$$, each tangent space $$T_pM$$ carries a linear symplectic form $$\omega_p$$; hence $$\dim T_pM$$ is even, and therefore $$M$$ itself must be even-dimensional.
