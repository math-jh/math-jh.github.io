---
title: "Linear Systems"
excerpt: "Linear systems of divisors and their properties"

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

[\[Picard Group\]](/ko/math/algebraic_geometry/picard_group)에서 우리는 line bundle들의 isomorphism class들이 abelian group을 형성함을 보았다. 이제 우리는 하나의 line bundle $\mathcal{L}$의 global sections들이 어떤 기하학적 구조를 갖는지 살펴볼 것이다. 이는 *linear system*의 개념으로 이어진다.

Linear system은 line bundle의 global sections들의 projective space이다. 예를 들어, $\mathbb{P}^n$에서 hyperplane bundle $\mathcal{O}_{\mathbb{P}^n}(1)$의 linear system은 $\mathbb{P}^n$의 모든 hyperplane들의 family이다. 이는 사영공간 $\mathbb{P}^{n-1}$과 자연스럽게 동형이며, 각 점 $[a_0 : \cdots : a_n] \in \mathbb{P}^{n-1}$은 hyperplane $V(a_0 \x_0 + \cdots + a_n \x_n)$에 대응된다.

## Complete Linear System

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Divisor $D$의 *complete linear system* $\lvert D \rvert$는 $D$와 linearly equivalent한 모든 effective divisor들의 집합이다.

$$\lvert D \rvert = \{D' \ge 0 \mid D' \sim D\}$$

</div>

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> Complete linear system $\lvert D \rvert$는 projective space $\mathbb{P}(H^0(X, \mathcal{O}_X(D)))$와 자연스럽게 동형이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

[\[Line Bundles\] §명제 18](/ko/math/algebraic_geometry/line_bundles#prop18)에서 $H^0(X, \mathcal{O}_X(D))$는 $D + \operatorname{div}(f) \ge 0$인 유리함수 $f$들의 공간과 동형임을 보였다. Nonzero section $s \in H^0(X, \mathcal{O}_X(D))$에 대해 $\operatorname{div}(s)$는 $\lvert D \rvert$의 원소이고, 두 section이 같은 divisor를 정의하는 것은 서로 scalar multiple인 것과 동치이다. 따라서 $\lvert D \rvert \cong \mathbb{P}(H^0(X, \mathcal{O}_X(D)))$이다.

</details>

이 동형에 의해 $\lvert D \rvert$는 자연스러운 projective space 구조를 갖는다. 그 dimension을 $\dim \lvert D \rvert = h^0(X, \mathcal{O}_X(D)) - 1$로 정의한다.

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> **$\mathbb{P}^n$의 hyperplane system**: $H = V(\x_0)$에 대해 $\lvert H \rvert$는 $\mathbb{P}^n$의 모든 hyperplane들의 family이다. [\[Line Bundles\] §예시 19](/ko/math/algebraic_geometry/line_bundles#ex19)에서 $H^0(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n}(1))$이 차수 1의 동차다항식들의 공간과 동형임을 보였으므로, $\dim \lvert H \rvert = n$이다. 이는 $\mathbb{P}^n$이 $n$차원 projective space라는 사실과 일치한다.

</div>

## Linear System

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> *Linear system*은 complete linear system $\lvert D \rvert$의 nonempty linear subspace이다. 즉, $H^0(X, \mathcal{O}_X(D))$의 subspace $V$에 대해 $\mathbb{P}(V) \subseteq \lvert D \rvert$의 꼴이다.

</div>

Linear system은 종종 $V$의 dimension을 그대로 사용하여 *$r$-dimensional linear system*이라 부른다. 1차원 linear system을 *pencil*, 2차원을 *net*, 3차원을 *web*이라 부르기도 한다.

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> **$\mathbb{P}^2$의 conic pencil**: 두 conic $C_1 = V(F_1)$, $C_2 = V(F_2)$의 pencil은 $\{\lambda F_1 + \mu F_2 = 0\}_{[\lambda:\mu] \in \mathbb{P}^1}$이다. 이는 $\lvert 2H \rvert$의 1차원 subspace이다. Pencil의 각 원소는 차수 2의 curve이며, 이들은 모두 $C_1 \cap C_2$를 지난다.

</div>

## Base Locus

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> Linear system $L$의 *base locus* $\operatorname{Bs}(L)$는 $L$의 모든 원소가 공유하는 closed subset이다.

$$\operatorname{Bs}(L) = \bigcap_{D \in L} \operatorname{Supp}(D)$$

</div>

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> Linear system $L$이 *basepoint-free*라는 것은 $\operatorname{Bs}(L) = \emptyset$인 것이다.

</div>

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> **$\mathbb{P}^n$의 hyperplane system**: $\lvert H \rvert$는 basepoint-free이다. 임의의 점 $p \in \mathbb{P}^n$에 대해 $p$를 지나지 않는 hyperplane이 존재하기 때문이다.

</div>

<div class="example" markdown="1">

<ins id="ex9">**예시 9**</ins> **Pencil의 base locus**: [예시 5](#ex5)의 conic pencil의 base locus는 $C_1 \cap C_2$이다. Bézout's theorem에 의해 이는 최대 4개의 점으로 구성된다.

</div>

## Fixed Part와 Moving Part

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> Complete linear system $\lvert D \rvert$가 base locus를 가지면, $D = F + M$으로 분해된다. 여기서 $F$는 *fixed part* (모든 $D' \in \lvert D \rvert$가 포함)이고, $\lvert M \rvert$는 basepoint-free이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Base locus $\operatorname{Bs}(\lvert D \rvert) = \bigcap_{D' \in \lvert D \rvert} \operatorname{Supp}(D')$를 생각하자. 이를 divisor $F$로 표현하면 (각 component에 최소 multiplicity를 부여), 모든 $D' \in \lvert D \rvert$는 $D' = F + M'$의 꼴이다. 그럼 $\lvert D \rvert = F + \lvert M \rvert$이고, $\lvert M \rvert$는 basepoint-free이다.

</details>

## Very Ample과 Ample Line Bundles

<div class="definition" markdown="1">

<ins id="def11">**정의 11**</ins> Line bundle $\mathcal{L}$이 *very ample*이라는 것은 $\lvert \mathcal{L} \rvert$가 embedding $\varphi_{\mathcal{L}}: X \hookrightarrow \mathbb{P}^N$을 정의하는 것이다. 구체적으로, basis $s_0, \ldots, s_N \in H^0(X, \mathcal{L})$에 대해

$$\varphi_{\mathcal{L}}(p) = [s_0(p) : \cdots : s_N(p)]$$

으로 정의된 map이 embedding인 것이다.

</div>

<div class="definition" markdown="1">

<ins id="def12">**정의 12**</ins> Line bundle $\mathcal{L}$이 *ample*이라는 것은 어떤 $n > 0$에 대해 $\mathcal{L}^{\otimes n}$이 very ample인 것이다.

</div>

<div class="example" markdown="1">

<ins id="ex13">**예시 13**</ins> **$\mathcal{O}_{\mathbb{P}^n}(1)$은 very ample**: [\[사영다양체\] §예시 16](/ko/math/algebraic_geometry/projective_varieties#ex16)에서 보듯, 이는 identity embedding $\mathbb{P}^n \hookrightarrow \mathbb{P}^n$을 정의한다.

</div>

<div class="example" markdown="1">

<ins id="ex14">**예시 14**</ins> **$\mathcal{O}_{\mathbb{P}^n}(d)$도 very ample**: $d > 0$이면, 이는 *Veronese embedding* $\mathbb{P}^n \hookrightarrow \mathbb{P}^N$을 정의한다. 여기서 $N = \binom{n+d}{d} - 1$이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop15">**명제 15**</ins> Line bundle $\mathcal{L}$이 very ample이면 $\lvert \mathcal{L} \rvert$는 basepoint-free이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$\varphi_{\mathcal{L}}$이 embedding이므로 모든 점에서 정의된다. 즉, 각 점 $p$에 대해 어떤 section $s_i$가 $s_i(p) \ne 0$이다. 따라서 basepoint가 없다.

</details>

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.
