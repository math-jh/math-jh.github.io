---
title: "컴팩트성"
description: "점렬컴팩트성을 정의하고, 유클리드 공간에서 그것이 닫혀 있고 유계인 것과 동치라는 하이네–보렐 정리를 Bolzano–Weierstrass 정리로부터 증명한다. 열린덮개에 의한 컴팩트성과의 관계도 정리한다."
excerpt: "점렬컴팩트성, 하이네–보렐 정리, 열린덮개와 컴팩트"

categories: [Math / Analysis]
permalink: /ko/math/analysis/compactness
sidebar: 
    nav: "analysis-ko"

header:
    overlay_image: /assets/images/Math/Analysis/Compactness.png
    overlay_filter: 0.5

date: 2026-07-03
last_modified_at: 2026-07-03

weight: 9

published: false
---

[§부분수열과 Bolzano–Weierstrass 정리](/ko/math/analysis/bolzano_weierstrass)는 유계수열에서 수렴하는 부분수열을 뽑았다. 이 "부분수열을 추출하여 극한을 얻는" 능력을 집합의 성질로 추상화한 것이 컴팩트성이며, 해석학의 존재 정리들을 떠받치는 가장 중요한 위상적 개념이다.

## 점렬컴팩트성

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 거리공간의 부분집합 $$K$$가 *점렬컴팩트<sub>sequentially compact</sub>*라는 것은, $$K$$의 점들로 이루어진 모든 점열이 $$K$$의 한 점으로 수렴하는 부분수열을 가지는 것이다. $$K$$가 *유계<sub>bounded</sub>*라는 것은 어떤 공 $$B(x_0, R)$$에 포함되는 것이다.

</div>

극한이 다시 $$K$$ 안에 있어야 한다는 조건에 유의한다. 유클리드 공간에서는 이 추상적 성질이 친숙한 두 조건으로 완전히 특징지어진다.

## 하이네–보렐 정리

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2 (하이네–보렐)**</ins> $$\mathbb{R}^n$$의 부분집합 $$K$$가 점렬컴팩트인 것은 $$K$$가 닫혀 있고 유계인 것과 동치이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

($$\Leftarrow$$) $$K$$가 닫혀 있고 유계라 하자. $$K$$의 점열 $$(x_m)$$은 유계이므로, 각 좌표가 유계인 실수열이다. 첫 좌표에 Bolzano–Weierstrass 정리 ([§부분수열과 Bolzano–Weierstrass 정리, ⁋정리 4](/ko/math/analysis/bolzano_weierstrass#thm4))를 적용해 수렴하는 부분수열을 뽑고, 그 부분수열에서 둘째 좌표에 다시 적용하는 식으로 $$n$$개의 좌표를 차례로 처리하면, 모든 좌표가 수렴하는 부분수열을 얻는다. 그 극한 $$x$$로 부분수열이 수렴하며, $$K$$가 닫혀 있으므로 ([§열린집합과 닫힌집합, ⁋명제 4](/ko/math/analysis/open_and_closed_sets#prop4)) $$x \in K$$이다.

($$\Rightarrow$$) $$K$$가 점렬컴팩트라 하자. $$K$$가 유계가 아니면 $$\lVert x_m\rVert \to \infty$$인 점열을 잡을 수 있는데, 이는 수렴하는 부분수열을 가질 수 없어 모순이다. $$K$$가 닫혀 있지 않으면, $$K$$의 점열 $$x_m \to x$$이면서 $$x \notin K$$인 경우가 있는데 ([§열린집합과 닫힌집합, ⁋명제 4](/ko/math/analysis/open_and_closed_sets#prop4)), 그 부분수열은 모두 $$x$$로 수렴하므로 $$K$$ 안의 점으로 수렴하는 부분수열이 없어 모순이다.

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

컴팩트성의 위력은 다음 글 [§연속함수의 성질](/ko/math/analysis/continuous_functions)에서 드러난다. 연속함수가 컴팩트집합을 컴팩트집합으로 보낸다는 사실 하나에서 최대·최소 정리와 균등연속성이 한꺼번에 따라 나온다.
