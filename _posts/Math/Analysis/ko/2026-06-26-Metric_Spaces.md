---
title: "거리공간"
description: "두 점 사이의 거리라는 개념을 공리화한 거리공간을 정의하고, 여러 예를 든다. 거리로부터 수렴과 Cauchy 수열, 완비성을 일반화하여 실수에서 얻은 해석학의 언어를 추상적 공간으로 옮긴다."
excerpt: "거리공간의 공리, 수렴과 완비성, 위상으로의 연결"

categories: [Math / Analysis]
permalink: /ko/math/analysis/metric_spaces
sidebar: 
    nav: "analysis-ko"

header:
    overlay_image: /assets/images/Math/Analysis/Metric_Spaces.png
    overlay_filter: 0.5

date: 2026-06-26
last_modified_at: 2026-06-26

weight: 6

published: false
---

지금까지의 해석학은 실수 위에서 전개되었다. 그러나 수렴·Cauchy·연속 같은 개념의 본질은 "두 대상이 얼마나 가까운가"라는 거리뿐이며, 그 거리가 몇 가지 자연스러운 성질만 만족하면 실수에서 했던 논증이 거의 그대로 옮겨 간다. 이러한 추상화가 거리공간이다.

## 거리공간의 정의

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 집합 $$X$$와 함수 $$d : X \times X \to \mathbb{R}$$가 다음을 만족하면 $$(X, d)$$를 *거리공간<sub>metric space</sub>*, $$d$$를 *거리<sub>metric</sub>*라 한다. 모든 $$x, y, z \in X$$에 대하여

1. $$d(x, y) \geq 0$$이고, $$d(x, y) = 0$$인 것은 $$x = y$$인 것과 동치이다;
2. (대칭성) $$d(x, y) = d(y, x)$$;
3. (삼각부등식) $$d(x, z) \leq d(x, y) + d(y, z)$$.

</div>

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> 다음은 모두 거리공간이다.

- $$\mathbb{R}$$에 $$d(x, y) = \lvert x - y\rvert$$를 준 것. 우리가 다뤄 온 표준 거리이다.
- $$\mathbb{R}^n$$에 유클리드 거리 $$d(x, y) = \sqrt{\sum_{i=1}^n (x_i - y_i)^2}$$를 준 것.
- 임의의 집합 $$X$$에 $$x \neq y$$이면 $$d(x, y) = 1$$, $$x = y$$이면 $$0$$으로 준 *이산거리*.
- 닫힌구간 위의 연속함수들의 공간 $$C[a,b]$$에 $$d(f, g) = \sup_{x}\lvert f(x) - g(x)\rvert$$를 준 것.

</div>

## 수렴과 완비성

거리만 있으면 수렴과 Cauchy 조건을 [§수열의 수렴](/ko/math/analysis/convergence_of_sequences)·[§Cauchy 수열과 완비성](/ko/math/analysis/cauchy_sequences)에서와 똑같은 형태로 정의할 수 있다. $$\lvert a_n - L\rvert$$을 $$d(a_n, L)$$로 바꾸기만 하면 된다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 거리공간 $$(X, d)$$의 점열 $$(x_n)$$이 $$x \in X$$로 *수렴*한다는 것은 $$d(x_n, x) \to 0$$인 것이다. $$(x_n)$$이 *Cauchy*라는 것은 임의의 $$\varepsilon > 0$$에 대해 $$N$$이 있어 $$m, n \geq N$$이면 $$d(x_m, x_n) < \varepsilon$$인 것이다. 중심 $$x$$, 반지름 $$r > 0$$의 *열린공<sub>open ball</sub>*은 $$B(x, r) = \{y \in X \mid d(x, y) < r\}$$이다.

</div>

실수에서와 마찬가지로 수렴하는 점열은 Cauchy이지만, 그 역은 공간에 따라 성립하지 않을 수 있다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> 거리공간 $$(X, d)$$에서 모든 Cauchy 점열이 (그 공간 안의 점으로) 수렴하면 $$(X, d)$$를 *완비<sub>complete</sub>*하다고 한다.

</div>

실수의 완비성 ([§Cauchy 수열과 완비성, ⁋정리 4](/ko/math/analysis/cauchy_sequences#thm4))은 곧 표준 거리를 준 $$\mathbb{R}$$이 완비 거리공간이라는 진술이다. 같은 논증을 좌표별로 적용하면 유클리드 공간 $$\mathbb{R}^n$$도 완비임을 얻는다. 반면 유리수 $$\mathbb{Q}$$나 개구간 $$(0,1)$$은 완비가 아니다 — 경계로 다가가는 Cauchy 점열의 극한이 빠져 있기 때문이다. 완비성은 부동점 정리를 비롯한 존재 정리들의 무대가 되며, 이는 [§미분방정식의 존재성과 유일성](/ko/math/analysis/existence_uniqueness_ode)에서 결정적으로 쓰인다.

## 위상으로의 연결

열린공은 거리공간에 "열린집합"이라는 위상적 구조를 부여하는 출발점이다. 다음 글 [§열린집합과 닫힌집합](/ko/math/analysis/open_and_closed_sets)에서 이를 정식화하면, 거리공간은 [\[위상수학\] §열린집합](/ko/math/topology/open_sets)에서 공리적으로 도입하는 위상공간의 가장 중요한 예가 됨을 보게 된다. 즉 해석학의 거리 기반 개념들은 위상수학의 더 일반적인 틀 안에 자연스럽게 자리 잡는다.
