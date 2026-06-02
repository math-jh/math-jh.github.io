---
title: "열린집합과 닫힌집합"
description: "거리공간에서 열린집합과 닫힌집합을 정의하고, 열린집합이 위상의 공리를 만족함을 보인다. 닫힌집합을 수렴하는 점열의 극한으로 특징짓고, 폐포의 개념을 도입하여 위상수학과의 연결을 명확히 한다."
excerpt: "열린집합과 위상, 닫힌집합의 점열 특징화, 폐포"

categories: [Math / Analysis]
permalink: /ko/math/analysis/open_and_closed_sets
sidebar: 
    nav: "analysis-ko"

header:
    overlay_image: /assets/images/Math/Analysis/Open_and_Closed_Sets.png
    overlay_filter: 0.5

date: 2026-06-02
last_modified_at: 2026-06-02
weight: 7

published: false
---

[§거리공간](/ko/math/analysis/metric_spaces)에서 열린공을 정의하였다. 열린공을 기본 단위로 삼으면 거리공간 위에 열린집합과 닫힌집합이라는 구조가 생기며, 이는 연속·컴팩트·연결 같은 해석학의 핵심 개념을 거리 없이 집합의 언어만으로 다룰 수 있게 한다.

## 열린집합

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 거리공간 $$(X, d)$$의 부분집합 $$U$$가 *열린집합<sub>open set</sub>*이라는 것은, 모든 점 $$x \in U$$에 대하여 어떤 $$r > 0$$이 존재하여 열린공 $$B(x, r) \subseteq U$$인 것이다.

</div>

직관적으로 열린집합은 그 안의 어느 점에서도 사방으로 약간의 여유를 가진 집합이다. 열린공 자체가 열린집합임은 삼각부등식으로 확인된다. 열린집합 전체는 다음의 닫힘 성질을 가진다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 거리공간 $$X$$에서 다음이 성립한다.

1. $$\varnothing$$과 $$X$$는 열린집합이다.
2. 임의의 (개수 무관) 열린집합들의 합집합은 열린집합이다.
3. 유한개의 열린집합의 교집합은 열린집합이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

2: $$x \in \bigcup_\alpha U_\alpha$$이면 어떤 $$U_\alpha$$에 속하고, $$U_\alpha$$가 열려 있어 $$B(x, r) \subseteq U_\alpha \subseteq \bigcup_\alpha U_\alpha$$인 $$r$$가 있다. 3: $$x \in \bigcap_{i=1}^n U_i$$이면 각 $$i$$에 대해 $$B(x, r_i) \subseteq U_i$$인 $$r_i$$가 있고, $$r = \min_i r_i > 0$$으로 두면 $$B(x, r) \subseteq \bigcap_i U_i$$이다.

</details>

명제 2의 세 성질은 정확히 위상공간의 공리이다 ([\[위상수학\] §열린집합](/ko/math/topology/open_sets)). 즉 거리는 그로부터 정해지는 열린집합들의 모임 — 거리가 유도하는 *위상* — 을 통해 위상공간의 구조를 낳는다. 무한개의 교집합은 열려 있지 않을 수 있다: $$\bigcap_{n} (-\tfrac1n, \tfrac1n) = \{0\}$$은 $$\mathbb{R}$$에서 열린집합이 아니다.

## 닫힌집합과 폐포

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 거리공간 $$X$$의 부분집합 $$F$$가 *닫힌집합<sub>closed set</sub>*이라는 것은 그 여집합 $$X \setminus F$$가 열린집합인 것이다.

</div>

닫힌집합은 점열의 극한을 통해 해석학적으로 특징지어진다. 이것이 닫힌집합이 해석학에서 중요한 이유이다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $$F \subseteq X$$가 닫힌집합인 것은, $$F$$의 점들로 이루어진 수렴하는 모든 점열의 극한이 다시 $$F$$에 속하는 것과 동치이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$F$$가 닫혀 있다고 하자. $$x_n \in F$$, $$x_n \to x$$인데 $$x \notin F$$라면 $$x$$는 열린집합 $$X \setminus F$$의 점이므로 $$B(x, r) \subseteq X\setminus F$$인 $$r$$가 있다. 그러나 $$x_n \to x$$이므로 큰 $$n$$에서 $$x_n \in B(x, r)$$, 즉 $$x_n \notin F$$가 되어 모순이다. 따라서 $$x \in F$$이다.

거꾸로 $$F$$가 점열 극한에 대해 닫혀 있다고 하자. $$X \setminus F$$가 열려 있지 않다면, 어떤 $$x \in X\setminus F$$에 대해 모든 $$r$$에서 $$B(x, r)$$가 $$F$$의 점을 포함한다. $$r = 1/n$$으로 잡아 $$x_n \in F \cap B(x, 1/n)$$을 택하면 $$x_n \to x$$이고 가정에 의해 $$x \in F$$가 되어 $$x \in X\setminus F$$에 모순이다.

</details>

집합 $$A$$를 포함하는 가장 작은 닫힌집합을 $$A$$의 *폐포<sub>closure</sub>* $$\overline{A}$$라 한다. 명제 4에 의해 $$\overline{A}$$는 정확히 $$A$$의 점열로 도달할 수 있는 모든 점, 즉 $$A$$의 극한점들을 $$A$$에 더한 것이다. 이러한 내부·폐포·경계의 위상적 개념들은 [\[위상수학\] §집합의 내부, 폐포, 경계](/ko/math/topology/other_concepts)에서 일반 위상공간에 대해 다루어진다.

열린·닫힌집합의 언어는 다음 글들의 토대가 된다. [§컴팩트성](/ko/math/analysis/compactness)은 열린덮개로, [§연결성과 중간값 정리](/ko/math/analysis/connectedness)는 열린집합으로의 분할로 정의되며, 함수의 연속성도 [§연속함수의 성질](/ko/math/analysis/continuous_functions)에서 "열린집합의 역상이 열림"으로 다시 표현된다.
