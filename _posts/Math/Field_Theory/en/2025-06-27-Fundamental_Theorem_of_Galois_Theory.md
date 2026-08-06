---
title: "The Fundamental Theorem of Galois Theory"
description: "We prove the fundamental theorem of Galois theory, which establishes a correspondence between intermediate fields of a Galois extension and closed subgroups of its Galois group."
excerpt: "The Galois correspondence between subgroups and intermediate fields"

categories: [Math / Field Theory]
permalink: /en/math/field_theory/fundamental_theorem_of_galois_theory
sidebar: 
    nav: "field_theory-en"

date: 2025-06-27
weight: 10
published: false
translated_at: 2026-05-31T08:30:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-31T08:30:05+00:00
---
We can now finally prove the fundamental theorem of Galois theory.

::: Theorem 1
Consider a Galois extension $\mathbb{L}/\mathbb{K}$ of a field $\mathbb{K}$ and its Galois group $\Gamma=\Gal(\mathbb{L}/\mathbb{K})$. Let $\Sub(\mathbb{L}/\mathbb{K})$ be the collection of subextensions of $\mathbb{L}$, and let $\Sub^{\cl}(\Gamma)$ be the collection of closed subgroups of $\Gamma$. Then the two functions between $\Sub(\mathbb{L}/\mathbb{K})$ and $\Sub^{\cl}(\Gamma)$

$$k:\Sub^{\cl}(\Gamma)\rightarrow\Sub(\mathbb{L}/\mathbb{K});\qquad G\mapsto k(G)\text{ the field of invariants of $G$}$$

and

$$g:\Sub(\mathbb{L}/\mathbb{K})\rightarrow\Sub^{\cl}(\Gamma);\qquad \mathbb{M}\mapsto g(\mathbb{M})\text{ the group of $\mathbb{M}$-automorphisms of $L$}$$

are inverses of each other.
:::

To prove this, we divide the proof into two steps as follows.

::: Lemma 2
For any subextension $\mathbb{M}\in \Sub(\mathbb{L}/\mathbb{K})$, $\mathbb{L}/\mathbb{M}$ is also a Galois extension. In this case, if we regard the Galois group $\Gal(\mathbb{L}/\mathbb{M})$ as a subgroup of $\Gal(\mathbb{L}/\mathbb{K})$ in the obvious way, it is a *closed* subgroup of $\Gal(\mathbb{L}/\mathbb{K})$, and therefore $g$ is well-defined.
:::
::: Proof
:::

---

**References**

**[Bou]** N. Bourbaki. *Algebra II: Chapters 4–7*. Springer, 2003.
