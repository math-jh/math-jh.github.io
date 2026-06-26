---
title: "컴팩트성"
description: "점렬컴팩트성을 정의하고, 유클리드 공간에서 그것이 닫혀 있고 유계인 것과 동치라는 하이네–보렐 정리를 Bolzano–Weierstrass 정리로부터 증명한다. 열린덮개에 의한 컴팩트성과의 관계도 정리한다."
excerpt: "점렬컴팩트성, 하이네–보렐 정리, 열린덮개와 컴팩트"

categories: [Math / Analysis]
permalink: /ko/math/analysis/compactness
sidebar: 
    nav: "analysis-ko"

date: 2026-06-02
weight: 9

published: false
---

[§부분수열과 [§부분수열과 Bolzano–Weierstrass 정리, ⁋정리 4](/ko/math/analysis/bolzano_weierstrass#thm4) 정리](/ko/math/analysis/bolzano_weierstrass)는 유계수열에서 수렴하는 부분수열을 뽑았다. 이 "부분수열을 추출하여 극한을 얻는" 능력을 집합의 성질로 추상화한 것이 컴팩트성이며, 해석학의 존재 정리들을 떠받치는 가장 중요한 위상적 개념이다.

해석학에서 어떤 점의 존재를 보이는 표준 전략은 다음과 같다. 먼저 원하는 성질에 점점 가까워지는 점열 $$(x_m)$$을 구성하고, 그 점열에서 수렴하는 부분수열을 뽑은 뒤, 극한점이 원하는 성질을 가짐을 보이는 것이다. 이 전략이 작동하려면 두 가지가 필요하다. 점열에서 수렴하는 부분수열을 언제나 뽑을 수 있어야 하고, 그 극한이 우리가 다루는 집합 안에 남아 있어야 한다. 바로 이 두 요구를 한 단어로 묶은 것이 점렬컴팩트성이다. 따라서 컴팩트집합은 "극한을 향한 추출"이 막힘없이 이루어지는 무대이며, [§연속함수의 성질, ⁋따름정리 2](/ko/math/analysis/continuous_functions#cor2)나 균등연속성 같은 결과가 이 무대 위에서 자연스럽게 따라 나온다.

## 점렬컴팩트성

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 거리공간의 부분집합 $$K$$가 *점렬컴팩트<sub>sequentially compact</sub>*라는 것은, $$K$$의 점들로 이루어진 모든 점열이 $$K$$의 한 점으로 수렴하는 부분수열을 가지는 것이다. $$K$$가 *유계<sub>bounded</sub>*라는 것은 어떤 공 $$B(x_0, R)$$에 포함되는 것이다.

</div>

극한이 다시 $$K$$ 안에 있어야 한다는 조건에 유의한다. 단순히 부분수열이 수렴한다는 것만으로는 충분하지 않다. 가령 개구간 $$K = (0, 1)$$에서 점열 $$x_m = 1/m$$을 잡으면 이는 $$0$$으로 수렴하고 그 모든 부분수열도 $$0$$으로 수렴하므로, $$K$$ 안의 점으로 수렴하는 부분수열이 하나도 없다. 따라서 $$(0,1)$$은 점렬컴팩트가 아니다. 이 예가 보여 주듯, 점렬컴팩트성은 "극한을 가둘 수 있는가"라는 닫힘의 성격과 "극한이 무한으로 달아나지 않는가"라는 유계의 성격을 동시에 요구한다. 유클리드 공간에서는 이 추상적 성질이 친숙한 두 조건으로 완전히 특징지어진다.

## 하이네–보렐 정리

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2 (하이네–보렐)**</ins> $$\mathbb{R}^n$$의 부분집합 $$K$$가 점렬컴팩트인 것은 $$K$$가 닫혀 있고 유계인 것과 동치이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

($$\Leftarrow$$) $$K$$가 닫혀 있고 유계라 하자. $$K$$의 점열 $$(x_m)$$을 좌표로 적으면

$$x_m = (x_m^{(1)}, x_m^{(2)}, \ldots, x_m^{(n)}) \in \mathbb{R}^n$$

이고, $$K$$가 유계이므로 각 좌표열 $$(x_m^{(j)})_m$$도 유계인 실수열이다. 먼저 첫 좌표열 $$(x_m^{(1)})$$에 Bolzano–Weierstrass 정리 ([§부분수열과 Bolzano–Weierstrass 정리, ⁋정리 4](/ko/math/analysis/bolzano_weierstrass#thm4))를 적용하여 수렴하는 부분수열의 첨자 집합 $$S_1 \subseteq \mathbb{N}$$을 얻는다. 그 부분수열 위에서 둘째 좌표열은 여전히 유계이므로 다시 [§부분수열과 Bolzano–Weierstrass 정리, ⁋정리 4](/ko/math/analysis/bolzano_weierstrass#thm4)를 적용하여 $$S_2 \subseteq S_1$$을 얻고, 이를 반복하면

$$S_1 \supseteq S_2 \supseteq \cdots \supseteq S_n, \qquad x_m^{(j)} \xrightarrow[ m \in S_j ]{} \xi_j \ (1 \leq j \leq n)$$

이 되는 첨자 집합들의 내림차순 사슬을 얻는다. 가장 작은 $$S_n$$을 따라가면 모든 좌표가 동시에 수렴하므로, 그 부분수열은 점

$$x = (\xi_1, \xi_2, \ldots, \xi_n) \in \mathbb{R}^n$$

으로 수렴한다. $$K$$가 닫혀 있으므로 ([§열린집합과 닫힌집합, ⁋명제 4](/ko/math/analysis/open_and_closed_sets#prop4)) 극한 $$x$$는 다시 $$K$$에 속한다. 따라서 임의의 점열에서 $$K$$ 안의 점으로 수렴하는 부분수열을 뽑았으므로 $$K$$는 점렬컴팩트이다.

($$\Rightarrow$$) 대우를 보인다. 먼저 $$K$$가 유계가 아니라 하자. 그러면 각 $$m$$에 대해

$$\lVert x_m \rVert > m$$

인 점 $$x_m \in K$$을 고를 수 있고, 이 점열의 임의의 부분수열도 노름이 무한대로 발산하므로 수렴할 수 없다. 따라서 $$K$$는 점렬컴팩트가 아니다. 다음으로 $$K$$가 닫혀 있지 않다 하자. 명제 4 ([§열린집합과 닫힌집합, ⁋명제 4](/ko/math/analysis/open_and_closed_sets#prop4))에 의해 $$K$$의 점열 $$x_m \to x$$이면서 $$x \notin K$$인 경우가 존재한다. 이때 $$(x_m)$$의 모든 부분수열은 같은 극한 $$x$$로 수렴하는데 ([§부분수열과 Bolzano–Weierstrass 정리, ⁋명제 2](/ko/math/analysis/bolzano_weierstrass#prop2)) $$x \notin K$$이므로, $$K$$ 안의 점으로 수렴하는 부분수열이 하나도 없다. 따라서 $$K$$는 점렬컴팩트가 아니다. 두 경우를 종합하면, $$K$$가 점렬컴팩트이면 $$K$$는 닫혀 있고 유계이다.

</details>

따라서 닫힌구간 $$[a, b]$$, 닫힌 공, 닫힌 직육면체 등은 모두 점렬컴팩트이다. 반면 개구간 $$(0, 1)$$은 닫혀 있지 않아, $$\mathbb{R}$$ 전체는 유계가 아니어서 점렬컴팩트가 아니다.

## 열린덮개에 의한 컴팩트성

위상수학에서 컴팩트성은 점열이 아니라 덮개로 정의된다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 집합 $$K$$의 *열린덮개<sub>open cover</sub>*는 합집합이 $$K$$를 포함하는 열린집합들의 모임이다. $$K$$가 *컴팩트<sub>compact</sub>*라는 것은, 모든 열린덮개가 유한개의 원소로 이루어진 부분덮개를 가지는 것이다.

</div>

<div class="remark" markdown="1">

<ins id="rmk4">**참고 4**</ins> 거리공간에서는 컴팩트성과 점렬컴팩트성이 동치이다. 따라서 하이네–보렐 정리는 열린덮개 의미의 컴팩트성에 대해서도 그대로 성립한다 — $$\mathbb{R}^n$$에서 컴팩트인 것은 닫혀 있고 유계인 것과 같다. 이 동치성과 일반 위상공간에서의 컴팩트성 이론은 [\[위상수학\] §옹골성](/ko/math/topology/compactness)과 [\[위상수학\] §옹골공간](/ko/math/topology/compact_spaces)에서 다룬다.

</div>

## 예시와 계산

하이네–보렐 정리는 $$\mathbb{R}^n$$에서 점렬컴팩트성을 판정하는 일을 두 가지 단순한 점검으로 환원한다. 닫혀 있는가와 유계인가를 확인하면 되며, 둘 중 하나라도 어긋나면 점렬컴팩트가 아니다. 닫힌구간 $$[a,b]$$가 점렬컴팩트인 반면 $$(0,1)$$은 닫혀 있지 않아, $$[0,\infty)$$나 $$\mathbb{Z}$$는 유계가 아니어서 점렬컴팩트가 아닌 것이 그러한 예이다. 흥미로운 경우는 두 조건이 미묘하게 어긋나는 경계에서 나타나는데, 유계성과 닫힘 가운데 하나만으로는 점렬컴팩트성을 보장하지 못함을 다음 예시가 보여 준다.

<div class="example" markdown="1">

<ins id="ex5">**예시 5 (수렴점열과 그 극한)**</ins> 집합

$$A = \Bigl\{  \frac{1}{m} : m \in \mathbb{N}  \Bigr\}$$

는 유계이지만 닫혀 있지 않다. 점열 $$x_m = 1/m$$이 $$A$$ 안에 있으면서 $$0 \notin A$$로 수렴하기 때문이다. 따라서 $$A$$는 점렬컴팩트가 아니다. 그러나 여기에 극한점 $$0$$을 더한

$$A \cup \{0\} = \Bigl\{  0, 1, \frac12, \frac13, \ldots  \Bigr\}$$

은 닫혀 있고 유계이므로 점렬컴팩트가 된다. 실제로 이 집합의 임의의 점열은 무한히 많은 항이 어떤 한 값 $$1/k$$와 같거나, 아니면 $$0$$으로 수렴하는 부분수열을 가지며, 두 경우 모두 극한이 집합 안에 있다.

</div>

좌표별 Bolzano–Weierstrass 논증은 $$\mathbb{R}^n$$의 곱 구조를 직접 활용한다. 컴팩트집합들의 곱이 다시 컴팩트가 됨을 이 논증으로 확인할 수 있다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> $$K \subseteq \mathbb{R}^m$$과 $$L \subseteq \mathbb{R}^n$$이 점렬컴팩트이면, 곱집합 $$K \times L \subseteq \mathbb{R}^{m+n}$$도 점렬컴팩트이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$K \times L$$의 점열 $$z_k = (x_k, y_k)$$를 잡자. $$K$$가 점렬컴팩트이므로 첨자 집합 $$S \subseteq \mathbb{N}$$을 따라

$$x_k \xrightarrow[ k \in S ]{} x \in K$$

인 부분수열이 있다. 이 $$S$$ 위에서 $$(y_k)_{k \in S}$$는 점렬컴팩트집합 $$L$$의 점열이므로, 다시 $$T \subseteq S$$를 따라

$$y_k \xrightarrow[ k \in T ]{} y \in L$$

인 부분수열을 뽑을 수 있다. $$T \subseteq S$$이므로 $$T$$ 위에서는 두 좌표가 동시에 수렴하여

$$z_k = (x_k, y_k) \xrightarrow[ k \in T ]{} (x, y) \in K \times L$$

이다. 따라서 $$K \times L$$의 임의의 점열에서 $$K \times L$$ 안의 점으로 수렴하는 부분수열을 뽑았으므로, $$K \times L$$은 점렬컴팩트이다.

</details>

이 명제를 닫힌구간에 거듭 적용하면, 닫힌 직육면체 $$[a_1, b_1] \times \cdots \times [a_n, b_n]$$이 점렬컴팩트임을 곧바로 얻는다. 하이네–보렐 정리의 ($$\Leftarrow$$) 방향은 임의의 닫힌 유계집합을 이러한 직육면체 안에 가두는 것으로 볼 수도 있다.

## 응용

컴팩트성은 그 자체로 흥미로운 성질이라기보다, 다른 결과를 끌어내는 도구로서 진가를 발휘한다. 점렬컴팩트집합의 닫힌 부분집합이 다시 점렬컴팩트라는 다음 명제는 그 가운데 가장 기본적이며, 자주 쓰인다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> $$K$$가 점렬컴팩트이고 $$F \subseteq K$$가 ($$K$$에서) 닫힌집합이면, $$F$$도 점렬컴팩트이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$F$$의 점열 $$(x_m)$$을 잡자. 이는 $$K$$의 점열이기도 하므로, $$K$$의 점렬컴팩트성에 의해 어떤 부분수열이

$$x_{m_k} \to x \in K$$

로 수렴한다. 그런데 $$(x_{m_k})$$는 $$F$$의 점들로 이루어진 수렴하는 점열이고 $$F$$가 닫혀 있으므로, 그 극한 $$x$$는 다시 $$F$$에 속한다 ([§열린집합과 닫힌집합, ⁋명제 4](/ko/math/analysis/open_and_closed_sets#prop4)). 따라서 $$F$$의 임의의 점열이 $$F$$ 안의 점으로 수렴하는 부분수열을 가지므로, $$F$$는 점렬컴팩트이다.

</details>

수렴하는 점열 자체도 그 극한과 함께라면 점렬컴팩트집합을 이룬다. 이는 [예시 5](#ex5)를 일반화한 것으로, 컴팩트성이 "유한집합에 한 점을 더한 것처럼 행동하는" 작은 무한집합까지 포착함을 보여 준다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> $$\mathbb{R}^n$$에서 $$x_m \to x$$이면, 집합

$$C = \{x\} \cup \{x_m : m \in \mathbb{N}\}$$

은 점렬컴팩트이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

하이네–보렐 정리에 따라 $$C$$가 닫혀 있고 유계임을 보이면 충분하다. 수렴하는 수열은 유계이고 ([§수열의 수렴, ⁋명제 3](/ko/math/analysis/convergence_of_sequences#prop3)) 거기에 극한점 하나를 더해도 유계이므로, $$C$$는 유계이다. 닫혀 있음을 보이기 위해 $$C$$의 점열 $$y_k \to y$$를 잡자. 두 경우로 나눈다.

$$\text{(i) 어떤 값 } a \in C \text{가 무한히 자주 나타나는 경우}, \qquad \text{(ii) 그렇지 않은 경우}.$$

(i)이면 그 상수 부분수열이 $$a$$로 수렴하므로 [§수열의 수렴, ⁋명제 2](/ko/math/analysis/convergence_of_sequences#prop2)에 의해 $$y = a \in C$$이다. (ii)이면 각 값이 유한 번만 나타나므로 $$y_k$$ 자체가 $$x_m$$들을 무한히 훑고, 그 부분수열이 $$x$$로 수렴하여 $$y = x \in C$$이다. 어느 경우든 $$y \in C$$이므로 $$C$$는 닫혀 있다.

</details>

마지막으로, 컴팩트집합은 자기 자신 위에서의 거리함수가 최솟값을 가진다는, 자주 인용되는 사실을 짚어 둔다.

<div class="example" markdown="1">

<ins id="ex9">**예시 9 (한 점에서 컴팩트집합까지의 거리)**</ins> $$K \subseteq \mathbb{R}^n$$이 비어 있지 않은 점렬컴팩트집합이고 $$p \in \mathbb{R}^n$$이라 하자. 거리

$$d(p, K) = \inf_{y \in K} \lVert p - y \rVert$$

는 실제로 $$K$$의 어떤 점에서 달성된다. 즉 $$\lVert p - y_0 \rVert = d(p, K)$$인 $$y_0 \in K$$가 존재한다. 실제로 하한의 정의에 의해

$$\lVert p - y_m \rVert \to d(p, K) \qquad (y_m \in K)$$

인 점열 $$(y_m)$$을 잡을 수 있고, $$K$$가 점렬컴팩트이므로 $$y_{m_k} \to y_0 \in K$$인 부분수열을 뽑는다. 노름이 연속이므로

$$\lVert p - y_0 \rVert = \lim_k \lVert p - y_{m_k} \rVert = d(p, K)$$

이 되어, 하한이 $$y_0 \in K$$에서 달성된다. $$K$$가 닫혀 있지 않으면 이 결론이 깨질 수 있다. 가령 $$K = (0, 1)$$, $$p = 0$$이면 $$d(p, K) = 0$$이지만 이를 달성하는 점이 $$K$$ 안에 없다.

</div>

