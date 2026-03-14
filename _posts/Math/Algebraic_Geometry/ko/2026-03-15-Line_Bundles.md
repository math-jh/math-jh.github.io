---
title: "Line Bundles"
excerpt: "Line bundles, sections, and the correspondence with divisors"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/line_bundles
sidebar: 
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Line_Bundles.png
    overlay_filter: 0.5

date: 2026-03-15
last_modified_at: 2026-03-15
weight: 10
---

## 도입

Divisor는 정칙함수 또는 유리함수의 영점과 극점을 "점수"로 기술하는 도구였다. 하지만 divisor는 단순한 형식합이며, 기하적으로 더 자연스러운 대상은 **line bundle**이다.

Line bundle은 각 점 $p \in X$ 위에 1차원 벡터공간 $L_p$를 붙인 대상이다. 예를 들어 $\mathbb{P}^n$ 위의 **tautological line bundle** $\mathcal{O}(-1)$은 각 점 $[v] \in \mathbb{P}^n$ 위에 그 점이 나타내는 직선 $\mathbb{K}v$를 붙인다.

Line bundle과 divisor는 밀접하게 연관되어 있다. 사실 smooth variety에서는 이 둘이 거의 같은 정보를 담고 있다.

## Line Bundle의 정의

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Variety $X$ 위의 **line bundle<sub>선다발</sub>** (또는 **invertible sheaf<sub>가역층</sub>**) $L$은 다음을 만족하는 $\mathbb{K}$-vector bundle이다:

1. 각 점 $p \in X$에 대해 fiber $L_p$는 1차원 $\mathbb{K}$-벡터공간이다.
2. $X$의 각 점 $p$에 대해 적당한 열린근방 $U$와 isomorphism $\varphi_U: L|_U \to U \times \mathbb{K}$가 존재한다.

</div>

### Section

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Line bundle $L$의 **section<sub>단면</sub>** $s$는 각 점 $p \in X$에 대해 $s(p) \in L_p$를 만족하는 함수이다. Section들의 집합을 $\Gamma(X, L)$ 또는 $H^0(X, L)$로 표기한다.

정칙 section은 국소적으로 $\varphi_U$를 통해 $U$ 위의 정칙함수로 보이는 section이다.

</div>

<div class="example" markdown="1">

<ins id="ex3">**예시 3 (Trivial line bundle)**</ins> $X \times \mathbb{K}$는 $X$ 위의 line bundle이다. 이를 **trivial line bundle** $\mathcal{O}_X$라 부른다. Section $\Gamma(X, \mathcal{O}_X)$는 정칙함수 $\mathcal{O}(X)$와 같다.

</div>

<div class="example" markdown="1">

<ins id="ex4">**예시 4 ($\mathbb{P}^n$ 위의 $\mathcal{O}(1)$)**</ins> $\mathbb{P}^n$ 위의 line bundle $\mathcal{O}(1)$을 다음과 같이 정의한다. 각 점 $[x_0 : \cdots : x_n] \in \mathbb{P}^n$에 대해 fiber는 선형함수들로 구성된 공간이다.

$\mathcal{O}(1)$의 section은 차수 1의 동차다항식들에 의해 주어진다. 예를 들어 $x_0, x_1, \ldots, x_n$은 $\mathcal{O}(1)$의 global section이다.

</div>

## Line Bundle과 Divisor의 대응

Smooth variety $X$에서 line bundle과 divisor는 밀접하게 연관된다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Divisor $D = \sum n_i Y_i$에 대해, 이에 대응하는 **line bundle** $\mathcal{O}(D)$를 다음과 같이 정의한다. 유리함수 $f$가 $D + \operatorname{div}(f) \geq 0$을 만족하면 $f$는 $\mathcal{O}(D)$의 section이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> Smooth variety $X$에서 다음이 성립한다:

1. 각 divisor $D$에 대해 line bundle $\mathcal{O}(D)$가 존재한다.
2. $D_1 \sim D_2$인 것과 $\mathcal{O}(D_1) \cong \mathcal{O}(D_2)$인 것은 동치이다.
3. 각 line bundle $L$에 대해 $L \cong \mathcal{O}(D)$인 divisor $D$가 존재한다.

따라서 $\operatorname{Cl}(X) \cong \operatorname{Pic}(X)$이다.

</div>

<details class="proof" markdown="1">
<summary>증명 (Sketch)</summary>

1. Divisor $D$의 각 성분 $Y_i$에 대해, $Y_i$를 "pole"으로 갖는 유리함수들의 sheaf를 정의하고, 이들을 tensor하여 $\mathcal{O}(D)$를 얻는다.

2. $D_1 \sim D_2$이면 $D_1 - D_2 = \operatorname{div}(f)$인 유리함수 $f$가 존재한다. 이 $f$에 의해 $\mathcal{O}(D_1)$과 $\mathcal{O}(D_2)$ 사이의 isomorphism이 주어진다.

3. Line bundle $L$의 section이 "pole"을 갖는 방식을 기술하여 대응하는 divisor를 얻는다. Smooth variety에서는 이것이 항상 가능하다.

</details>

## Tensor Product와 Dual

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> Line bundle들의 tensor product는 line bundle이다. 구체적으로:

1. $L_1 \otimes L_2$는 line bundle이다.
2. $\mathcal{O}(D_1) \otimes \mathcal{O}(D_2) \cong \mathcal{O}(D_1 + D_2)$이다.
3. $L$의 dual $L^\ast$는 line bundle이고, $L \otimes L^\ast \cong \mathcal{O}$이다.
4. $\mathcal{O}(D)^\ast \cong \mathcal{O}(-D)$이다.

</div>

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> $\mathbb{P}^n$ 위에서 $\mathcal{O}(d) = \mathcal{O}(1)^{\otimes d}$이고, $\mathcal{O}(-d) = \mathcal{O}(1)^\ast{}^{\otimes d}$이다.

$\mathcal{O}(d)$의 global section은 차수 $d$의 동차다항식들이다. 특히 $\Gamma(\mathbb{P}^n, \mathcal{O}(d)) \cong \mathbb{K}[x_0, \ldots, x_n]_d$이다.

</div>

## Picard Group

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> Variety $X$ 위의 line bundle들의 isomorphism class들은 tensor product에 대해 abelian group을 이룬다. 이를 **Picard group<sub>Picard 군</sub>**이라 하고 $\operatorname{Pic}(X)$로 표기한다.

단위원은 trivial line bundle $\mathcal{O}_X$이고, $L$의 역원은 dual $L^\ast$이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> Smooth variety $X$에 대해 $\operatorname{Pic}(X) \cong \operatorname{Cl}(X)$이다.

</div>

<div class="example" markdown="1">

<ins id="ex11">**예시 11**</ins> $\operatorname{Pic}(\mathbb{P}^n) \cong \mathbb{Z}$이며, 생성원은 $\mathcal{O}(1)$이다. 이는 $\operatorname{Cl}(\mathbb{P}^n) \cong \mathbb{Z}$과 일치한다.

</div>

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.
