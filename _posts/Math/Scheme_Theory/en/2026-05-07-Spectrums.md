---
title: "Spectrum"
excerpt: "The prime spectrum of a commutative ring and the Zariski topology"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/spectrums
header:
    overlay_image: /assets/images/Math/Algebraic_Varieties/Spectrums.png
    overlay_filter: 0.5
sidebar: 
    nav: "scheme_theory-en"

date: 2025-01-27
last_modified_at: 2025-01-27
weight: 2
translated_at: 2026-05-23T20:30:01+00:00
translation_source: kimi-cli
---
<div class="remark" markdown="1">

In all posts in this category, a ring means a commutative ring (with unity).

</div>

In this post we define the spectrum, the most fundamental object in algebraic geometry. The spectrum is a topological space equipped with a suitable structure sheaf; in this post we first define it as a set and define a topology on it. Then, in the next post, we will define the structure sheaf on $$\Spec A$$.

## $$\Spec A$$ as a Set

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> For a ring $$A$$, $$\Spec A$$ is the set of all prime ideals of $$A$$, called the *spectrum* of $$A$$.

</div>

Now suppose a ring homomorphism $$\phi: A \rightarrow B$$ is given. Then by [\[Algebraic Structures\] §Field of Fractions, ⁋Proposition 9](/en/math/algebraic_structures/field_of_fractions#prop9), the following map

$$\Spec\phi: \Spec B \rightarrow \Spec A;\qquad \mathfrak{q}\mapsto \phi^{-1}(\mathfrak{q})$$

is well-defined.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> The $$\Spec: \cRing^\op \rightarrow \Set$$ defined
