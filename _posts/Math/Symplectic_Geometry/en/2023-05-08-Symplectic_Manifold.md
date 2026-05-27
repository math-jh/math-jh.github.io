---
title: "Symplectic Manifolds"
excerpt: "Definitions and properties of symplectic manifolds"

categories: [Math / Symplectic Geometry]
permalink: /en/math/symplectic_geometry/symplectic_manifold
header:
    overlay_image: /assets/images/Math/Symplectic_Geometry/Symplectic_Manifold.png
    overlay_filter: 0.5
sidebar: 
    nav: "symplectic_geometry-en"

date: 2023-05-08
last_modified_at: 2023-05-08
weight: 3
translated_at: 2026-05-28T11:36:15+00:00
translation_source: kimi-cli
---
In **[MS]**, symplectic vector spaces are introduced, after which more time is spent on the Maslov class, among other topics. We will introduce these later when they are needed for Floer theory, and for now follow **[Cd]** to first define symplectic manifolds.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A *symplectic form* $$\omega$$ on a manifold $$M$$ is a differential $$2$$-form such that $$d\omega=0$$ and, for every $$p\in M$$, $$\omega_p:T_pM\times T_pM\rightarrow \mathbb{R}$$ is a linear symplectic form. We then call $$(M,\omega)$$ a *symplectic manifold*.

</div>

For a symplectic manifold $$(M,\omega)$$, the vector space $$T_pM$$ is equipped with a linear symplectic form $$\omega_p$$, so $$\dim T_pM$$ is even, and therefore $$M$$ must also be even-dimensional.
