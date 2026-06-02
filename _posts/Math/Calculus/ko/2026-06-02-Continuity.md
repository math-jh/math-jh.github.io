---
title: "연속함수"
description: "함수의 연속을 극한으로 정의하고, 연속함수의 사칙연산과 합성, 그리고 닫힌구간 위 연속함수가 갖는 핵심 성질인 최대·최소 정리와 중간값 정리를 다룬다."
excerpt: "연속의 정의와 연속함수의 성질 — 최대·최소 정리와 중간값 정리"

categories: [Math / Calculus]
permalink: /ko/math/calculus/continuity
sidebar: 
    nav: "calculus-ko"

header:
    overlay_image: /assets/images/Math/Calculus/Continuity.png
    overlay_filter: 0.5

date: 2026-06-02
last_modified_at: 2026-06-02
weight: 2

published: false
---

[§함수와 극한](/ko/math/calculus/functions_and_limits)에서 극한을 정의하였다. 직관적으로 함수가 "끊김 없이 이어진다"는 것은, 점 $$a$$에서의 함숫값과 그 점으로 다가갈 때의 극한값이 일치한다는 뜻이다. 이를 극한으로 정확히 옮긴 것이 연속의 정의이다.

## 연속의 정의

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 함수 $$f$$가 정의역의 점 $$a$$에서 *연속<sub>continuous</sub>*이라는 것은

$$\lim_{x \to a} f(x) = f(a)$$

가 성립하는 것이다. 이를 ε-δ로 풀어 쓰면, 임의의 $$\varepsilon > 0$$에 대하여 어떤 $$\delta > 0$$이 존재하여 $$\lvert x - a\rvert < \delta$$이면 $$\lvert f(x) - f(a)\rvert < \varepsilon$$이 성립하는 것이다. $$f$$가 정의역의 모든 점에서 연속이면 $$f$$를 *연속함수*라 부른다.

</div>

극한의 정의 ([§함수와 극한, ⁋정의 1](/ko/math/calculus/functions_and_limits#def1))와 비교하면 두 가지가 다르다. 첫째, 극한값을 미리 $$f(a)$$로 못박았다. 둘째, $$x = a$$를 제외하는 조건 $$0 < \lvert x-a\rvert$$가 사라졌는데, $$x = a$$일 때는 $$\lvert f(a)-f(a)\rvert = 0 < \varepsilon$$이 자동으로 성립하므로 굳이 제외할 필요가 없기 때문이다. 즉 연속이란 "극한이 존재하고, 그 값이 함숫값과 같다"는 것이다.

극한법칙 ([§함수와 극한, ⁋명제 3](/ko/math/calculus/functions_and_limits#prop3))에서 곧바로 다음이 따른다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> $$f$$와 $$g$$가 $$a$$에서 연속이면 $$f+g$$, $$cf$$ ($$c$$는 상수), $$fg$$도 $$a$$에서 연속이고, $$g(a) \neq 0$$이면 $$f/g$$도 $$a$$에서 연속이다. 또한 $$f$$가 $$a$$에서 연속이고 $$g$$가 $$f(a)$$에서 연속이면 합성함수 $$g \circ f$$는 $$a$$에서 연속이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

앞의 네 연산은 극한법칙에 함숫값 일치 조건을 결합하면 즉시 따른다. 예를 들어 $$\lim_{x\to a}(f+g)(x) = f(a)+g(a) = (f+g)(a)$$이다.

합성을 보이자. $$\varepsilon > 0$$이 주어지면, $$g$$가 $$b := f(a)$$에서 연속이므로 어떤 $$\eta > 0$$이 존재하여 $$\lvert y - b\rvert < \eta$$이면 $$\lvert g(y) - g(b)\rvert < \varepsilon$$이다. 다시 $$f$$가 $$a$$에서 연속이므로 이 $$\eta$$에 대응하는 $$\delta > 0$$이 존재하여 $$\lvert x-a\rvert < \delta$$이면 $$\lvert f(x) - b\rvert < \eta$$이다. 따라서 $$\lvert x-a\rvert < \delta$$이면 $$\lvert g(f(x)) - g(f(a))\rvert < \varepsilon$$이다.

</details>

명제 2로부터 다항함수는 모든 점에서 연속이고, 유리함수는 분모가 $$0$$이 아닌 모든 점에서 연속임을 안다. 또한 $$\sin, \cos, \exp$$ 등 기본 초월함수도 연속이며, 이들의 합·곱·합성으로 만들어지는 함수는 정의되는 곳에서 연속이다.

## 닫힌구간 위 연속함수의 성질

연속함수의 진정한 힘은 *닫힌구간* $$[a,b]$$ 위에서 드러난다. 다음 두 정리는 미적분학 전체에서 거듭 쓰이는 핵심 결과이다.

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3 (최대·최소 정리)**</ins> $$f$$가 닫힌구간 $$[a,b]$$에서 연속이면, $$f$$는 $$[a,b]$$에서 최댓값과 최솟값을 갖는다. 즉 어떤 $$c, d \in [a,b]$$가 존재하여 모든 $$x \in [a,b]$$에 대해 $$f(d) \leq f(x) \leq f(c)$$이다.

</div>

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4 (중간값 정리)**</ins> $$f$$가 닫힌구간 $$[a,b]$$에서 연속이고 $$f(a) \neq f(b)$$이면, $$f(a)$$와 $$f(b)$$ 사이의 임의의 값 $$y$$에 대하여 $$f(c) = y$$를 만족하는 $$c \in (a,b)$$가 존재한다.

</div>

이 두 정리의 증명은 실수의 *완비성* — 실수에 "빈틈이 없다"는 성질 — 을 본질적으로 필요로 한다. 가령 유리수 위에서는 $$f(x) = x^2 - 2$$가 $$f(1) < 0 < f(2)$$이지만 $$f(c) = 0$$인 유리수 $$c$$는 없으므로 중간값 정리가 성립하지 않는다. 이 때문에 본 글에서는 두 정리를 미적분의 기본 도구로 받아들이고, 그 엄밀한 증명은 완비성을 정초한 뒤의 해석학으로 미룬다 ([§연속함수의 성질](/ko/math/analysis/continuous_functions), [§연결성과 중간값 정리](/ko/math/analysis/connectedness)). 위상수학의 언어로 보면 최대·최소 정리는 옹골집합의 연속상이 옹골집합이라는 사실 ([\[위상수학\] §옹골성](/ko/math/topology/compactness))의, 중간값 정리는 연결집합의 연속상이 연결집합이라는 사실 ([\[위상수학\] §연결공간](/ko/math/topology/connected_spaces))의 실수판 귀결이다.

중간값 정리는 방정식의 해의 존재를 보이는 데 특히 유용하다. 예를 들어 $$f(x) = x^3 - x - 1$$은 연속이고 $$f(1) = -1 < 0$$, $$f(2) = 5 > 0$$이므로, $$(1,2)$$ 안에 $$f(c) = 0$$인 해 $$c$$가 존재한다.

연속의 정의에서 $$\delta$$는 일반적으로 점 $$a$$마다 다르게 잡힌다. 모든 점에 대해 하나의 $$\delta$$를 공통으로 잡을 수 있는 더 강한 성질을 *균등연속*이라 하는데, 닫힌구간 위 연속함수는 항상 균등연속이라는 사실 또한 완비성의 귀결로 해석학에서 다룬다 ([§연속함수의 성질](/ko/math/analysis/continuous_functions)).

다음 글 [§미분과 도함수](/ko/math/calculus/derivatives)에서는 연속함수 중에서도 "매끄러운" 함수가 갖는 국소적 변화율, 즉 미분을 정의한다.
