---
title: "Sheaf Cohomology"
excerpt: "Derived functors and sheaf cohomology"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/sheaf_cohomology
sidebar: 
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Sheaf_Cohomology.png
    overlay_filter: 0.5

date: 2026-03-15
last_modified_at: 2026-03-15
weight: 16
---

## 도입

Sheaf $\mathcal{F}$의 global section $\Gamma(X, \mathcal{F})$은 중요한 불변량이다. 하지만 많은 경우 $\Gamma(X, \mathcal{F})$만으로는 충분한 정보를 얻을 수 없다.

**Sheaf cohomology** $H^i(X, \mathcal{F})$는 이 문제를 해결한다. 이는 $\Gamma(X, -)$의 **derived functor**로 정의되며, sheaf의 "higher obstruction"들을 측정한다.

## Injective Resolution과 Derived Functor

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Abelian category $\mathcal{A}$에서 object $I$가 **injective**라는 것은 임의의 monomorphism $A \to B$와 morphism $A \to I$에 대해 다음 diagram을 완성하는 $B \to I$가 존재하는 것이다:

```
0 → A → B
    ↓   ↗
    I
```

</div>

<div class="theorem" markdown="1">

<ins id="thm2">**정리 2**</ins> Category of $\mathcal{O}_X$-modules는 enough injectives를 갖는다. 즉, 각 $\mathcal{F}$에 대해 injective resolution $0 \to \mathcal{F} \to I^0 \to I^1 \to \cdots$가 존재한다.

</div>

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Sheaf $\mathcal{F}$의 **cohomology group<sub>코호몰로지 군</sub>** $H^i(X, \mathcal{F})$를 injective resolution $0 \to \mathcal{F} \to I^\bullet$에 대해 다음과 같이 정의한다:

$$H^i(X, \mathcal{F}) = H^i(\Gamma(X, I^\bullet))$$

</div>

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $H^i(X, \mathcal{F})$는 injective resolution의 선택과 무관하다.

</div>

## 기본 성질

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> Sheaf cohomology의 기본 성질:

1. $H^0(X, \mathcal{F}) = \Gamma(X, \mathcal{F})$
2. $I$가 injective이면 $i > 0$에 대해 $H^i(X, I) = 0$
3. Short exact sequence $0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$에 대해 long exact sequence가 존재한다:
   $$0 \to H^0(\mathcal{F}') \to H^0(\mathcal{F}) \to H^0(\mathcal{F}'') \to H^1(\mathcal{F}') \to \cdots$$

</div>

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6 (Dimension bound)**</ins> $n$차원 variety $X$에 대해 $i > n$이면 $H^i(X, \mathcal{F}) = 0$이다.

</div>

## Flasque Sheaf

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> Sheaf $\mathcal{F}$가 **flasque<sub>플라스크 층</sub>**라는 것은 모든 열린집합 $U \subseteq V$에 대해 restriction map $\mathcal{F}(V) \to \mathcal{F}(U)$가 surjective인 것이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> $\mathcal{F}$가 flasque이면 $i > 0$에 대해 $H^i(X, \mathcal{F}) = 0$이다.

</div>

<div class="example" markdown="1">

<ins id="ex9">**예시 9**</ins> Injective sheaf는 flasque이다.

</div>

## Euler Characteristic

<div class="definition" markdown="1">

<ins id="def10">**정의 10**</ins> Sheaf $\mathcal{F}$의 **Euler characteristic<sub>오일러 지표</sub>**를 다음과 같이 정의한다:

$$\chi(X, \mathcal{F}) = \sum_{i=0}^{n} (-1)^i \dim H^i(X, \mathcal{F})$$

(모든 $H^i(X, \mathcal{F})$가 finite dimensional인 경우)

</div>

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11 (Additivity)**</ins> Short exact sequence $0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$에 대해:

$$\chi(X, \mathcal{F}) = \chi(X, \mathcal{F}') + \chi(X, \mathcal{F}'')$$

</div>

## 예시

<div class="example" markdown="1">

<ins id="ex12">**예시 12 ($\mathbb{P}^n$)**</ins> $\mathbb{P}^n$ 위에서:

$$H^i(\mathbb{P}^n, \mathcal{O}(d)) = \begin{cases}
\mathbb{K}[x_0, \ldots, x_n]_d & i = 0, d \geq 0 \\
\mathbb{K}[x_0^{-1}, \ldots, x_n^{-1}]_{-d-n-1} & i = n, d < -n \\
0 & \text{otherwise}
\end{cases}$$

</div>

<div class="example" markdown="1">

<ins id="ex13">**예시 13 (Curve)**</ins> Genus $g$인 smooth projective curve $C$에 대해:

- $H^0(C, \mathcal{O}_C) = \mathbb{K}$
- $H^1(C, \mathcal{O}_C)$는 $g$차원

따라서 $\chi(\mathcal{O}_C) = 1 - g$이다.

</div>

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[God]** R. Godement, *Topologie algébrique et théorie des faisceaux*, Hermann, 1958.
