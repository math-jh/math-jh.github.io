---
title: "사영다양체"
excerpt: "Projective varieties and homogeneous coordinates"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/projective_varieties
sidebar: 
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Projective_Varieties.png
    overlay_filter: 0.5

date: 2026-03-11
last_modified_at: 2026-03-11
weight: 2

---

## 사영공간

[§아핀다양체](/ko/math/algebraic_geometry/affine_varieties)에서 우리는 아핀공간 $\mathbb{A}^n$과 그 위의 다항식으로 정의되는 부분집합들을 살펴보았다. 그러나 아핀공간에는 몇 가지 불편한 점이 있다. 가장 큰 문제는 *compactness*가 결여되어 있다는 것이다. 예를 들어 $\mathbb{A}^1$은 Zariski 위상에서 quasi-compact이지만, 직관적으로 "무한히 확장"되어 있어 닫힌 곡선과 같은 기하적 대상을 다루기에 적합하지 않다.

사영공간 $\mathbb{P}^n$은 이러한 문제를 해결한다. 사영공간은 아핀공간에 "무한원점들"을 추가하여 compact하게 만든 것이다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 체 $\mathbb{k}$ 위의 *$n$차원 사영공간<sub>projective $n$-space</sub>* $\mathbb{P}^n_{\mathbb{k}}$은 다음과 같이 정의된다. 집합으로서

$$\mathbb{P}^n = (\mathbb{k}^{n+1} \setminus \{0\}) / \sim$$

이며, 여기서 동치관계 $\sim$은

$$(x_0, \ldots, x_n) \sim (y_0, \ldots, y_n) \iff \text{$x_i = \lambda y_i$ for some $\lambda \ne 0$, for all $i$}$$

으로 주어진다. 혼동의 여지가 없을 때는 $\mathbb{P}^n$으로 적는다.

</div>

동치류 $[(x_0, \ldots, x_n)]$은 보통 $[x_0 : \cdots : x_n]$으로 표기하며, 이를 *homogeneous coordinates*라 부른다. $x_0, \ldots, x_n$을 *좌표<sub>coordinate</sub>*라 하고, 이들 중 적어도 하나는 $0$이 아니어야 한다.

<div class="remark" markdown="1">

**참고 2** Homogeneous coordinates의 핵심은 좌표들이 *비율*만을 결정한다는 것이다. 즉, $[x_0 : \cdots : x_n] = [\lambda x_0 : \cdots : \lambda x_n]$ for $\lambda \ne 0$이다.

</div>

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> $\mathbb{P}^1$의 점들:

- $[1 : 0]$, $[0 : 1]$, $[1 : 1]$, $[2 : 3]$, $[1 : 2]$, ...
- $[1 : 0]$과 $[2 : 0]$은 같은 점 ($\lambda = 2$)
- $[0 : 1]$은 "무한원점"으로 생각할 수 있음

</div>

## Standard Open Cover

사영공간 $\mathbb{P}^n$은 $n+1$개의 아핀공간들로 덮을 수 있다. 이는 사영공간을 이해하는 가장 중요한 방법 중 하나이다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> $i = 0, 1, \ldots, n$에 대하여, *$i$번째 standard open set* $U_i$를

$$U_i = \{[x_0 : \cdots : x_n] \in \mathbb{P}^n \mid x_i \ne 0\}$$

으로 정의한다.

</div>

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> 각각의 $U_i$는 아핀공간 $\mathbb{A}^n$과 naturally bijective하다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$U_0$의 경우, map $\varphi_0: U_0 \to \mathbb{A}^n$을

$$\varphi_0([x_0 : x_1 : \cdots : x_n]) = \left(\frac{x_1}{x_0}, \ldots, \frac{x_n}{x_0}\right)$$

으로 정의하자. 역함수 $\psi_0: \mathbb{A}^n \to U_0$는

$$\psi_0(a_1, \ldots, a_n) = [1 : a_1 : \cdots : a_n]$$

이다. 일반적인 $U_i$도 비슷하게 보인다.

</details>

<div class="remark" markdown="1">

**참고 6** 위의 bijection을 통해 우리는 $U_i$를 "좌표 $x_i$가 무한대가 아닌 점들"로 생각할 수 있다. 즉, $\mathbb{P}^n = U_0 \cup \cdots \cup U_n$이고, 각 $U_i \cong \mathbb{A}^n$이다.

</div>

## Homogeneous Polynomials and Varieties

사영공간에서는 *homogeneous polynomial*들만이 잘 정의된 함수를 준다.

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> 다항식 $F \in \mathbb{k}[x_0, \ldots, x_n]$이 *homogeneous of degree $d$*라는 것은 모든 $\lambda \in \mathbb{k}$에 대해

$$F(\lambda x_0, \ldots, \lambda x_n) = \lambda^d F(x_0, \ldots, x_n)$$

을 만족하는 것이다.

</div>

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins>

- $F = x_0^2 + x_1 x_2$는 homogeneous of degree 2
- $F = x_0 + x_1$은 homogeneous of degree 1
- $F = x_0^2 + x_1$은 homogeneous가 아님

</div>

<div class="remark" markdown="1">

**참고 9** Homogeneous polynomial $F$에 대해 $F([x_0 : \cdots : x_n])$은 잘 정의되지 않는다. 그러나 조건 $F(x_0, \ldots, x_n) = 0$은 well-defined이다. 왜냐하면

$$F(\lambda x_0, \ldots, \lambda x_n) = \lambda^d F(x_0, \ldots, x_n) = 0 \iff F(x_0, \ldots, x_n) = 0$$

이기 때문이다.

</div>

<div class="definition" markdown="1">

<ins id="def10">**정의 10**</ins> Homogeneous polynomials $F_1, \ldots, F_k \in \mathbb{k}[x_0, \ldots, x_n]$에 대하여, *사영다양체<sub>projective variety</sub>* $V(F_1, \ldots, F_k)$를

$$V(F_1, \ldots, F_k) = \{[x_0 : \cdots : x_n] \in \mathbb{P}^n \mid F_1(x) = \cdots = F_k(x) = 0\}$$

으로 정의한다.

</div>

<div class="example" markdown="1">

<ins id="ex11">**예시 11**</ins> $\mathbb{P}^2$에서의 기본적인 사영다양체들:

1. **사영직선**: $V(a_0 x_0 + a_1 x_1 + a_2 x_2)$
2. **원뿔곡선<sub>conic</sub>**: $V(x_0^2 + x_1^2 - x_2^2)$
3. **세 점**: $V(x_0 x_1 x_2)$ (세 직선의 합집합)

</div>

<div class="example" markdown="1">

<ins id="ex12">**예시 12**</ins> **Veronese embedding**: $\mathbb{P}^1 \to \mathbb{P}^2$를

$$[x : y] \mapsto [x^2 : xy : y^2]$$

으로 정의하면, 그 image는 $V(x_0 x_2 - x_1^2)$이다. 이는 conic이다.

</div>

## Zariski Topology on $\mathbb{P}^n$

<div class="definition" markdown="1">

<ins id="def13">**정의 13**</ins> $\mathbb{P}^n$의 *Zariski 위상*은 사영다양체들을 닫힌집합으로 갖는 위상이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop14">**명제 14**</ins> Zariski 위상은 실제로 위상이다. 특히:

1. $\emptyset$과 $\mathbb{P}^n$은 사영다양체
2. 사영다양체들의 교집합은 사영다양체
3. 유한개의 사영다양체들의 합집합은 사영다양체

</div>

<div class="proposition" markdown="1">

<ins id="prop15">**명제 15**</ins> $\mathbb{P}^n$은 Zariski 위상에서 compact (more precisely, quasi-compact)이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Standard open cover $\mathbb{P}^n = U_0 \cup \cdots \cup U_n$을 생각하자. 각 $U_i \cong \mathbb{A}^n$은 Zariski 위상에서 quasi-compact이다. 유한개의 quasi-compact 열린집합들의 합집합은 quasi-compact이므로 $\mathbb{P}^n$은 quasi-compact이다.

</details>

## Homogeneous Ideal과 Projective Nullstellensatz

<div class="definition" markdown="1">

<ins id="def16">**정의 16**</ins> Ideal $I \subseteq \mathbb{k}[x_0, \ldots, x_n]$이 *homogeneous*라는 것은 $I$가 homogeneous polynomials들로 생성되는 것이다.

</div>

<div class="definition" markdown="1">

<ins id="def17">**정의 17**</ins> 부분집합 $X \subseteq \mathbb{P}^n$의 *homogeneous ideal* $I(X)$를

$$I(X) = \{F \in \mathbb{k}[x_0, \ldots, x_n] \mid F \text{ homogeneous and } F(x) = 0 \text{ for all } x \in X\}$$

으로 정의한다.

</div>

<div class="theorem" markdown="1">

<ins id="thm18">**정리 18**</ins> (Projective Nullstellensatz) $\mathbb{k}$가 대수적으로 닫힌 체이고 $I \subseteq \mathbb{k}[x_0, \ldots, x_n]$이 homogeneous ideal이라 하자. 그럼

1. $V(I) = \emptyset \iff I \supseteq (x_0, \ldots, x_n)$
2. $I(V(I)) = \sqrt{I}$ (if $V(I) \ne \emptyset$)

</div>

<div class="remark" markdown="1">

**참고 19** 아핀 경우와의 차이점: $V(I) = \emptyset$이 $I = (1)$을 의미하지 않는다. 대신 $I$가 *irrelevant ideal* $(x_0, \ldots, x_n)$을 포함하는 것을 의미한다.

</div>

## Projective Varieties와 Affine Varieties의 관계

<div class="proposition" markdown="1">

<ins id="prop20">**명제 20**</ins> 사영다양체 $X \subseteq \mathbb{P}^n$과 standard open set $U_i$에 대하여, $X \cap U_i$는 $U_i \cong \mathbb{A}^n$ 위의 아핀다양체이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$U_0$의 경우, $X = V(F_1, \ldots, F_k)$이고 각 $F_j$가 homogeneous of degree $d_j$라 하자. 그럼 $X \cap U_0$는 $\mathbb{A}^n$에서

$$f_j\left(\frac{x_1}{x_0}, \ldots, \frac{x_n}{x_0}\right) = 0, \quad j = 1, \ldots, k$$

을 만족하는 점들이다. 여기서 $f_j = F_j(1, x_1, \ldots, x_n)$는 $\mathbb{k}[x_1, \ldots, x_n]$의 다항식이다.

</details>

<div class="example" markdown="1">

<ins id="ex21">**예시 21**</ins> $\mathbb{P}^2$에서 원 $X = V(x_0^2 + x_1^2 - x_2^2)$를 생각하자. 그럼

- $X \cap U_2 = V(x^2 + y^2 - 1) \subset \mathbb{A}^2$ (단위원)
- $X \cap U_0 = V(1 + y^2 - z^2) \subset \mathbb{A}^2$ (쌍곡선)

</div>

## Morphisms of Projective Varieties

<div class="definition" markdown="1">

<ins id="def22">**정의 22**</ins> 사영다양체 $X \subseteq \mathbb{P}^n$과 $Y \subseteq \mathbb{P}^m$ 사이의 *morphism* $\varphi: X \to Y$는 각 점 $p \in X$에 대해 다음을 만족하는 함수이다:

적당한 homogeneous polynomials $F_0, \ldots, F_m$ of the same degree가 존재하여

$$\varphi(p) = [F_0(p) : \cdots : F_m(p)]$$

이고, 모든 $p \in X$에 대해 $F_i(p)$들이 모두 $0$이 아니다.

</div>

<div class="example" markdown="1">

<ins id="ex23">**예시 23**</ins>

1. **항등사상**: $\mathbb{P}^n \to \mathbb{P}^n$, $[x_0 : \cdots : x_n] \mapsto [x_0 : \cdots : x_n]$
2. **Veronese embedding**: $\mathbb{P}^1 \to \mathbb{P}^2$, $[x : y] \mapsto [x^2 : xy : y^2]$
3. **Segre embedding**: $\mathbb{P}^1 \times \mathbb{P}^1 \to \mathbb{P}^3$, $([x : y], [u : v]) \mapsto [xu : xv : yu : yv]$

</div>

<div class="example" markdown="1">

<ins id="ex24">**예시 24**</ins> **주의**: $\mathbb{P}^1 \to \mathbb{P}^1$, $[x : y] \mapsto [x : y + 1]$은 *morphism가 아니다*. 왜냐하면 $[0 : 0]$에서 정의되지 않기 때문이다. 대신 이는 *rational map*이다.

</div>

## Examples of Projective Varieties

<div class="example" markdown="1">

<ins id="ex25">**예시 25**</ins> **Quadric hypersurfaces**: $\mathbb{P}^n$에서 homogeneous polynomial of degree 2로 정의되는 사영다양체

- $\mathbb{P}^2$: conics (ellipse, parabola, hyperbola)
- $\mathbb{P}^3$: quadric surfaces

</div>

<div class="example" markdown="1">

<ins id="ex26">**예시 26**</ins> **Twisted cubic in $\mathbb{P}^3$**: 

$$C = \{[1 : t : t^2 : t^3] \mid t \in \mathbb{k}\} \cup \{[0 : 0 : 0 : 1]\}$$

이는 세 개의 quadratic polynomials

$$x_0 x_2 - x_1^2, \quad x_0 x_3 - x_1 x_2, \quad x_1 x_3 - x_2^2$$

의 공통 영점이다.

</div>

---

**참고문헌**

**[Har]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.  
**[Ful]** W. Fulton, *Algebraic Curves*, 2008. (Available online)
