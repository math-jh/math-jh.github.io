---
title: "Linear Systems"
excerpt: "Linear systems, base loci, and maps to projective space"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/linear_systems
sidebar: 
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Linear_Systems.png
    overlay_filter: 0.5

date: 2026-03-15
last_modified_at: 2026-03-15
weight: 12
---

## 도입

Line bundle $L$의 section들은 벡터공간 $\Gamma(X, L)$을 이룬다. 이 section들 중 어떤 것을 선택하면 $X$를 projective space로 보내는 map을 정의할 수 있다. 예를 들어 $\mathbb{P}^n$ 위의 $\mathcal{O}(1)$의 section $x_0, \ldots, x_n$을 사용하면 identity map $\mathbb{P}^n \to \mathbb{P}^n$을 얻는다.

**Linear system**은 line bundle의 section들의 특정한 부분공간이다. 이를 통해 우리는 variety를 projective space로 embed하거나, variety 사이의 rational map을 정의할 수 있다.

## Complete Linear System

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Divisor $D$에 대해 **complete linear system<sub>완비 선형계</sub>** $|D|$는 $D' \geq 0$이고 $D' \sim D$인 모든 effective divisor들의 집합이다.

이는 $\Gamma(X, \mathcal{O}(D))$의 non-zero section들의 projectivization과 일대일 대응한다:

$$|D| = \mathbb{P}(\Gamma(X, \mathcal{O}(D))) = (\Gamma(X, \mathcal{O}(D)) \setminus \{0\}) / \mathbb{K}^\ast$$

</div>

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Divisor $D$의 **dimension<sub>차원</sub>**을 $\dim |D| = \dim \Gamma(X, \mathcal{O}(D)) - 1$으로 정의한다. 이를 $l(D)$로 표기하기도 한다.

</div>

<div class="example" markdown="1">

<ins id="ex3">**예시 3 ($\mathbb{P}^n$)**</ins> $d \geq 0$에 대해 $|dH|$ (여기서 $H$는 hyperplane)의 dimension은

$$\dim |dH| = \dim \Gamma(\mathbb{P}^n, \mathcal{O}(d)) - 1 = \binom{n+d}{d} - 1$$

이다. 이는 차수 $d$의 동차다항식들의 projectivization이다.

</div>

## Linear System과 Projective Space로의 Map

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> **Linear system** $V \subseteq |D|$는 $|D|$의 projective subspace이다. 즉, $\Gamma(X, \mathcal{O}(D))$의 subspace $W$에 대해 $V = \mathbb{P}(W)$이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> Linear system $V = \mathbb{P}(W) \subseteq |D|$가 주어지면, rational map $\varphi_V: X \dashrightarrow \mathbb{P}(W^\ast)$를 정의할 수 있다. 구체적으로, basis $s_0, \ldots, s_k$ of $W$에 대해

$$\varphi_V(p) = [s_0(p) : \cdots : s_k(p)]$$

이다. (단, $s_i(p)$가 모두 0이 아닌 점 $p$에서 정의됨)

</div>

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> Linear system $V$의 **base locus<sub>기저점자리</sub>** $\operatorname{Bs}(V)$는 모든 $D \in V$에 포함된 점들의 집합이다:

$$\operatorname{Bs}(V) = \bigcap_{D \in V} \operatorname{Supp}(D)$$

Base locus가 empty이면 $V$는 **base-point-free**이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> $V$가 base-point-free인 것과 $\varphi_V$가 everywhere regular인 것은 동치이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$\varphi_V(p)$가 정의되려면 $s_i(p)$ 중 적어도 하나가 0이 아니어야 한다. 모든 $D \in V$에 대해 $p \in D$이면 $p$에서 모든 section이 vanish하므로 $\varphi_V(p)$가 정의되지 않는다. 반대로 $p \notin \operatorname{Bs}(V)$이면 어떤 $D \in V$에 대해 $p \notin D$이고, 이에 대응하는 section $s$가 $s(p) \neq 0$을 만족한다.

</details>

## Very Ample과 Ample

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> Line bundle $L$이 **very ample<sub>매우 풍부한</sub>**이라는 것은 complete linear system $|L|$이 $X$를 $\mathbb{P}^N$으로 embed하는 map을 정의하는 것이다. 즉:

1. $\operatorname{Bs}(|L|) = \emptyset$
2. $\varphi_{|L|}: X \to \mathbb{P}^N$이 closed embedding

</div>

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> Line bundle $L$이 **ample<sub>풍부한</sub>**이라는 것은 어떤 $m > 0$에 대해 $L^{\otimes m}$이 very ample인 것이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> $\mathcal{O}(1)$은 $\mathbb{P}^n$ 위에서 very ample이다. 더 일반적으로 $\mathcal{O}(d)$는 $d > 0$일 때 ample이다.

</div>

<div class="example" markdown="1">

<ins id="ex11">**예시 11 (Degree 2 curve)**</ins> $\mathbb{P}^1$ 위에서 $|2p|$ (임의의 점 $p$)의 dimension은 1이다. Basis $1, x$ (여기서 $x$는 $p$에서 pole을 갖는 유리함수)를 사용하면

$$\varphi_{|2p|}: \mathbb{P}^1 \to \mathbb{P}^2, \quad [1 : t] \mapsto [1 : t : t^2]$$

를 얻는다. 이것이 **conic**의 parameterization이다.

</div>

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.
