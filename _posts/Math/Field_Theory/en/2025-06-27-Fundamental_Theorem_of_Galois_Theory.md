---
title: "The Fundamental Theorem of Galois Theory"
description: "We prove the fundamental theorem of Galois theory, which establishes a correspondence between intermediate fields of a Galois extension and closed subgroups of its Galois group."
excerpt: "The Galois correspondence between subgroups and intermediate fields"

categories: [Math / Field Theory]
permalink: /en/math/field_theory/fundamental_theorem_of_galois_theory
header:
    overlay_image: /assets/images/Math/Field_Theory/Fundamental_Theorem_of_Galois_Theory.png
    overlay_filter: 0.5
sidebar: 
    nav: "field_theory-en"

date: 2025-06-27
last_modified_at: 2025-06-27
weight: 10
translated_at: 2026-05-31T08:30:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-31T08:30:05+00:00
---
We can now finally prove the fundamental theorem of Galois theory.

<div class="proposition" markdown="1">

<ins id="thm1">**Theorem 1**</ins> Consider a Galois extension $$\mathbb{L}/\mathbb{K}$$ of a field $$\mathbb{K}$$ and its Galois group $$\Gamma=\Gal(\mathbb{L}/\mathbb{K})$$. Let $$\mathscr{K}$$ be the collection of subextensions of $$\mathbb{L}$$, and let $$\mathscr{G}$$ be the collection of closed subgroups of $$\Gamma$$. Then the two functions between $$\mathscr{K}$$ and $$\mathscr{G}$$

$$k:\mathscr{G}\rightarrow\mathscr{K};\qquad G\mapsto k(G)\text{ the field of invariants of $G$}$$

and

$$g:\mathscr{K}\rightarrow\mathscr{G};\qquad \mathbb{M}\mapsto g(\mathbb{M})\text{ the group of $\mathbb{M}$-automorphisms of $L$}$$

are inverses of each other.

</div>

To prove this, we divide the proof into two steps as follows.

<div class="proposition" markdown="1">

<ins id="lem2">**Lemma 2**</ins> For any subextension $$\mathbb{M}\in \mathscr{K}$$, $$\mathbb{L}/\mathbb{M}$$ is also a Galois extension. In this case, if we regard the Galois group $$\Gal(\mathbb{L}/\mathbb{M})$$ as a subgroup of $$\Gal(\mathbb{L}/\mathbb{K})$$ in the obvious way, it is a *closed* subgroup of $$\Gal(\mathbb{L}/\mathbb{K})$$, and therefore $$g$$ is well-defined.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>



</details>
