---
title: "연속함수의 성질"
description: "연속함수가 컴팩트집합을 컴팩트집합으로 보냄을 보이고, 그로부터 최대·최소 정리를 증명한다. 컴팩트집합 위의 연속함수가 균등연속이라는 하이네–칸토어 정리도 다룬다."
excerpt: "컴팩트성의 보존, 최대·최소 정리, 균등연속성"

categories: [Math / Analysis]
permalink: /ko/math/analysis/continuous_functions
sidebar: 
    nav: "analysis-ko"

header:
    overlay_image: /assets/images/Math/Analysis/Continuous_Functions.png
    overlay_filter: 0.5

date: 2026-07-04
last_modified_at: 2026-07-04

weight: 10

published: false
---

[\[미적분학\] §연속함수](/ko/math/calculus/continuity)에서 우리는 최대·최소 정리를 증명 없이 도구로 받아들였다. 이제 [§컴팩트성](/ko/math/analysis/compactness)을 갖추었으므로 이를 증명할 수 있다. 핵심은 연속함수가 컴팩트성을 보존한다는 단 하나의 사실이다.

## 컴팩트성의 보존

<div class="proposition" markdown="1">

<ins id="thm1">**정리 1**</ins> $$f : X \to Y$$가 연속이고 $$K \subseteq X$$가 점렬컴팩트이면, 상 $$f(K)$$도 점렬컴팩트이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$f(K)$$의 점열 $$(y_n)$$을 택하면 $$y_n = f(x_n)$$인 $$x_n \in K$$이 있다. $$K$$가 점렬컴팩트이므로 $$x_{n_k} \to x \in K$$인 부분수열이 있고, $$f$$의 연속성과 점열 특징화 ([§함수의 극한과 연속, ⁋명제 2](/ko/math/analysis/limits_and_continuity#prop2))에 의해 $$y_{n_k} = f(x_{n_k}) \to f(x) \in f(K)$$이다. 따라서 $$(y_n)$$이 $$f(K)$$ 안의 점으로 수렴하는 부분수열을 가지므로 $$f(K)$$는 점렬컴팩트이다.

</details>

## 최대·최소 정리

실숫값 연속함수에 정리 1을 적용하면 최댓값과 최솟값의 존재가 곧바로 따른다.

<div class="proposition" markdown="1">

<ins id="cor2">**따름정리 2 (최대·최소 정리)**</ins> $$K$$가 점렬컴팩트이고 $$f : K \to \mathbb{R}$$가 연속이면, $$f$$는 $$K$$에서 최댓값과 최솟값을 가진다. 특히 닫힌구간 $$[a,b]$$에서 연속인 함수는 최댓값과 최솟값을 가진다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

정리 1에 의해 $$f(K) \subseteq \mathbb{R}$$는 점렬컴팩트이고, 하이네–보렐 정리 ([§컴팩트성, ⁋정리 2](/ko/math/analysis/compactness#thm2))에 의해 닫혀 있고 유계이다. 유계이므로 $$M = \sup f(K)$$가 존재하고 ([§실수의 완비성, ⁋정의 2](/ko/math/analysis/completeness_of_reals#def2)), 상한의 성질로 $$M$$으로 수렴하는 $$f(K)$$의 점열이 있으며, $$f(K)$$가 닫혀 있으므로 $$M \in f(K)$$이다. 즉 $$M = f(x_{\max})$$인 $$x_{\max} \in K$$가 있어 $$M$$이 최댓값이다. 최솟값도 같다. $$[a,b]$$는 점렬컴팩트이므로 마지막 주장이 따른다.

</details>

이로써 [\[미적분학\] §연속함수, ⁋정리 3](/ko/math/calculus/continuity#thm3)에서 받아들였던 최대·최소 정리가 완비성에 기초하여 증명되었고, 그것에 의존하던 [\[미적분학\] §평균값 정리](/ko/math/calculus/mean_value_theorem)의 롤의 정리도 정당화된다.

## 균등연속성

컴팩트성은 연속의 $$\delta$$를 점에 무관하게 고를 수 있게 해 준다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> $$f : X \to Y$$가 *균등연속<sub>uniformly continuous</sub>*이라는 것은, 임의의 $$\varepsilon > 0$$에 대하여 $$\delta > 0$$이 존재하여 ($$x$$에 무관하게) 모든 $$x, x'$$에 대해 $$d_X(x, x') < \delta$$이면 $$d_Y(f(x), f(x')) < \varepsilon$$인 것이다.

</div>

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4 (하이네–칸토어)**</ins> 점렬컴팩트집합 위에서 연속인 함수는 균등연속이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$f$$가 $$K$$에서 연속이지만 균등연속이 아니라 하자. 그러면 어떤 $$\varepsilon > 0$$에 대해, 모든 $$\delta = 1/n$$이 실패하여 $$d_X(x_n, x_n') < 1/n$$이면서 $$d_Y(f(x_n), f(x_n')) \geq \varepsilon$$인 점들이 있다. $$K$$가 점렬컴팩트이므로 $$x_{n_k} \to x \in K$$인 부분수열이 있고, $$d_X(x_{n_k}, x_{n_k}') < 1/n_k \to 0$$이므로 $$x_{n_k}'$$도 같은 $$x$$로 수렴한다. 연속성에 의해 $$f(x_{n_k})$$와 $$f(x_{n_k}')$$이 모두 $$f(x)$$로 수렴하여 그 거리가 $$0$$으로 가야 하는데, 이는 거리가 $$\varepsilon$$ 이상이라는 데 모순이다.

</details>

균등연속성은 연속함수의 적분가능성을 증명하는 데 핵심적으로 쓰여, 다음 글들에서 [§Riemann 적분](/ko/math/analysis/riemann_integral)의 기초가 된다. 한편 연속함수가 보존하는 또 하나의 성질인 연결성과, 그로부터 따라 나오는 중간값 정리는 [§연결성과 중간값 정리](/ko/math/analysis/connectedness)에서 다룬다.
