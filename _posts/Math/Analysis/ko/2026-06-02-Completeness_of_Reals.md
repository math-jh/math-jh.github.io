---
title: "실수의 완비성"
description: "실수를 순서체로 보고, 해석학 전체를 떠받치는 완비성 공리(상한 성질)를 도입한다. 이로부터 아르키메데스 성질과 유리수의 조밀성을 유도하고, 완비성이 유리수와 실수를 가르는 본질적 차이임을 본다."
excerpt: "순서체와 상한 공리, 아르키메데스 성질, 유리수의 조밀성"

categories: [Math / Analysis]
permalink: /ko/math/analysis/completeness_of_reals
sidebar: 
    nav: "analysis-ko"

header:
    overlay_image: /assets/images/Math/Analysis/Completeness_of_Reals.png
    overlay_filter: 0.5

date: 2026-06-02
last_modified_at: 2026-06-02
weight: 1

published: false
---

[\[미적분학\] §함수와 극한](/ko/math/calculus/functions_and_limits)에서 우리는 극한을 다루며 실수의 "빈틈 없음"을 직관적으로 사용하였고, [\[미적분학\] §연속함수, ⁋정리 4](/ko/math/calculus/continuity#thm4)의 중간값 정리가 유리수 위에서는 성립하지 않음을 지적하였다. 해석학은 이 직관적 성질을 하나의 공리로 명확히 못박는 데서 출발한다. 그것이 *완비성*이며, 미적분학의 모든 존재 정리 — 극한, 최댓값, 적분의 존재 — 가 궁극적으로 여기에 기댄다.

## 순서체로서의 실수

실수 $$\mathbb{R}$$은 사칙연산과 대소관계를 갖춘 *순서체<sub>ordered field</sub>*이다. 즉 $$\mathbb{R}$$은 체이면서 전순서 $$\leq$$ ([\[집합론\] §순서관계의 정의](/ko/math/set_theory/order_relations))를 가지고, 그 순서가 연산과 다음과 같이 호환된다: $$a \leq b$$이면 $$a + c \leq b + c$$이고, $$a \leq b$$이고 $$0 \leq c$$이면 $$ac \leq bc$$이다. 유리수 $$\mathbb{Q}$$ 역시 순서체이므로, 이 성질만으로는 $$\mathbb{R}$$과 $$\mathbb{Q}$$가 구별되지 않는다. 둘을 가르는 것이 바로 다음에 도입할 완비성이다.

먼저 순서로부터 정해지는 상계와 상한의 개념을 정리한다 ([\[집합론\] §순서집합의 원소들](/ko/math/set_theory/elements_in_ordered_set)).

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $$S \subseteq \mathbb{R}$$가 공집합이 아니라 하자. 실수 $$M$$이 $$S$$의 *상계<sub>upper bound</sub>*라는 것은 모든 $$s \in S$$에 대해 $$s \leq M$$인 것이고, 상계가 하나라도 존재하면 $$S$$를 *위로 유계<sub>bounded above</sub>*라 한다. $$S$$의 상계 중 가장 작은 것이 존재하면 그것을 $$S$$의 *상한<sub>supremum</sub>*이라 하고 $$\sup S$$로 적는다. 대칭적으로 *하계*, *아래로 유계*, *하한* $$\inf S$$를 정의한다.

</div>

상한 $$\alpha = \sup S$$는 두 조건으로 특징지어진다: (i) $$\alpha$$는 상계이다 (모든 $$s \in S$$에 대해 $$s \leq \alpha$$); (ii) $$\alpha$$는 가장 작은 상계이다 — 즉 임의의 $$\varepsilon > 0$$에 대해 $$\alpha - \varepsilon$$은 더 이상 상계가 아니므로 $$s > \alpha - \varepsilon$$인 $$s \in S$$가 존재한다. 조건 (ii)의 이 형태는 앞으로 거듭 쓰인다.

## 완비성 공리

<div class="definition" markdown="1">

<ins id="def2">**정의 2 (완비성 공리)**</ins> 순서체 $$\mathbb{R}$$은 *완비<sub>complete</sub>*하다. 즉 위로 유계인 공집합이 아닌 모든 부분집합 $$S \subseteq \mathbb{R}$$은 상한 $$\sup S \in \mathbb{R}$$를 갖는다. 이를 *상한 성질<sub>least upper bound property</sub>*이라 부른다.

</div>

이것이 실수를 정의하는 마지막 공리이며, $$\mathbb{Q}$$에서는 성립하지 않는다. 예를 들어 $$S = \{x \in \mathbb{Q} \mid x^2 < 2\}$$는 $$\mathbb{Q}$$ 안에서 위로 유계이지만, 그 상한은 $$\sqrt{2}$$여야 하는데 이것이 유리수가 아니므로 $$\mathbb{Q}$$ 안에는 상한이 없다. 완비성은 바로 이런 "빈틈"이 $$\mathbb{R}$$에는 없음을 단언한다.

하한에 대한 대응 명제는 공리로 따로 둘 필요가 없다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> 아래로 유계인 공집합이 아닌 모든 $$S \subseteq \mathbb{R}$$은 하한 $$\inf S$$를 갖는다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$-S = \{-s \mid s \in S\}$$를 생각하자. $$S$$가 하계 $$m$$을 가지면 $$-m$$은 $$-S$$의 상계이므로 $$-S$$는 위로 유계이고, 완비성 공리에 의해 $$\alpha = \sup(-S)$$가 존재한다. 그러면 $$-\alpha = \inf S$$임이 정의로부터 직접 확인된다.

</details>

## 아르키메데스 성질과 조밀성

완비성의 첫 수확은 "자연수가 한없이 커진다"는 당연해 보이는 사실인데, 놀랍게도 이는 완비성 없이는 보장되지 않는다.

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4 (아르키메데스 성질)**</ins> 임의의 실수 $$x$$에 대하여, $$n > x$$인 자연수 $$n$$이 존재한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

자연수 집합 $$\mathbb{N}$$이 위로 유계라 가정하고 모순을 이끌자. 그러면 완비성에 의해 $$\alpha = \sup \mathbb{N}$$가 존재한다. $$\alpha$$가 가장 작은 상계이므로 $$\alpha - 1$$은 상계가 아니고, 따라서 $$n > \alpha - 1$$인 자연수 $$n$$이 있다. 그러면 $$n + 1 > \alpha$$인데 $$n + 1$$도 자연수이므로 $$\alpha$$가 상계라는 데 모순이다. 따라서 $$\mathbb{N}$$은 위로 유계가 아니고, 임의의 $$x$$에 대해 $$n > x$$인 $$n$$이 존재한다.

</details>

아르키메데스 성질의 동치 형태로, 임의의 $$\varepsilon > 0$$에 대해 $$\frac{1}{n} < \varepsilon$$인 자연수 $$n$$이 존재한다 ($$n > 1/\varepsilon$$을 잡으면 된다). 이로부터 유리수가 실수 안에 촘촘히 들어차 있음을 얻는다.

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5 (유리수의 조밀성)**</ins> 임의의 두 실수 $$a < b$$ 사이에는 유리수 $$q$$가 존재한다. 즉 $$a < q < b$$인 $$q \in \mathbb{Q}$$가 있다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$b - a > 0$$이므로 아르키메데스 성질에 의해 $$\frac{1}{n} < b - a$$, 즉 $$nb - na > 1$$인 자연수 $$n$$이 있다. 두 실수의 차가 $$1$$보다 크므로 그 사이에 정수가 존재한다 — 구체적으로 $$m = \lfloor na\rfloor + 1$$로 두면 $$na < m \leq na + 1 < nb$$이다. 양변을 $$n$$으로 나누면 $$a < \frac{m}{n} < b$$이고, $$q = m/n$$이 원하는 유리수이다.

</details>

이처럼 완비성 하나로부터 실수의 핵심 성질들이 줄줄이 따라 나온다. 다음 글 [§수열의 수렴](/ko/math/analysis/convergence_of_sequences)에서는 완비성을 수열의 언어로 옮겨 단조수렴정리를 얻고, 이어 [§Cauchy 수열과 완비성](/ko/math/analysis/cauchy_sequences)에서 완비성의 또 다른 동치 형태를 본다. 이 완비성이 있어야 비로소 [\[미적분학\] §연속함수](/ko/math/calculus/continuity)에서 도구로 받아들였던 최대·최소 정리와 중간값 정리를 [§연속함수의 성질](/ko/math/analysis/continuous_functions), [§연결성과 중간값 정리](/ko/math/analysis/connectedness)에서 증명할 수 있다.
