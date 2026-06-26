---
title: "열린집합과 닫힌집합"
description: "거리공간에서 열린집합과 닫힌집합을 정의하고, 열린집합이 위상의 공리를 만족함을 보인다. 닫힌집합을 수렴하는 점열의 극한으로 특징짓고, 폐포의 개념을 도입하여 위상수학과의 연결을 명확히 한다."
excerpt: "열린집합과 위상, 닫힌집합의 점열 특징화, 폐포"

categories: [Math / Analysis]
permalink: /ko/math/analysis/open_and_closed_sets
sidebar: 
    nav: "analysis-ko"

date: 2026-06-02
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

[명제 2](#prop2)의 세 성질은 정확히 위상공간의 공리이다 ([\[위상수학\] §열린집합](/ko/math/topology/open_sets)). 즉 거리는 그로부터 정해지는 열린집합들의 모임, 곧 거리가 유도하는 *위상*을 통해 위상공간의 구조를 낳는다. 무한개의 교집합은 열려 있지 않을 수 있다: $$\bigcap_{n} (-1/n, 1/n) = \{0\}$$은 $$\mathbb{R}$$에서 열린집합이 아니다.

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

집합 $$A$$를 포함하는 가장 작은 닫힌집합을 $$A$$의 *폐포<sub>closure</sub>* $$\overline{A}$$라 한다. [명제 4](#prop4)에 의해 $$\overline{A}$$는 정확히 $$A$$의 점열로 도달할 수 있는 모든 점, 즉 $$A$$의 극한점들을 $$A$$에 더한 것이다. 이러한 내부·폐포·경계의 위상적 개념들은 [\[위상수학\] §집합의 내부, 폐포, 경계](/ko/math/topology/other_concepts)에서 일반 위상공간에 대해 다루어진다.

여집합을 취하면 [명제 2](#prop2)가 닫힌집합에 대한 쌍대 명제로 그대로 옮겨진다. 드모르간 법칙에 의해 합집합과 교집합의 역할이 뒤바뀌므로, 닫힌집합의 모임은 임의의 교집합과 유한 합집합에 대해 닫혀 있다. 이를 정리하면 다음과 같다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> 거리공간 $$X$$에서 다음이 성립한다.

1. $$\varnothing$$과 $$X$$는 닫힌집합이다.
2. 임의의 (개수 무관) 닫힌집합들의 교집합은 닫힌집합이다.
3. 유한개의 닫힌집합의 합집합은 닫힌집합이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$F_\alpha$$가 닫혀 있으면 $$X \setminus F_\alpha$$는 열려 있다. 드모르간 법칙

$$X \setminus \bigcap_\alpha F_\alpha = \bigcup_\alpha (X \setminus F_\alpha), \qquad X \setminus \bigcup_{i=1}^n F_i = \bigcap_{i=1}^n (X \setminus F_i)$$

을 쓰면, 임의 교집합의 여집합은 열린집합들의 합집합이라 [명제 2](#prop2)의 (2)로 열려 있고, 유한 합집합의 여집합은 열린집합들의 유한 교집합이라 [명제 2](#prop2)의 (3)으로 열려 있다. 따라서 각각의 본래 집합이 닫혀 있다. (1)은 $$\varnothing$$과 $$X$$가 서로의 여집합이며 둘 다 열려 있음에서 따른다.

</details>

[명제 2](#prop2)에서 무한 교집합이 열림을 보장하지 못했던 것처럼, 여기서도 무한 합집합은 닫혀 있지 않을 수 있다. 닫힌구간들의 합집합 $$\bigcup_{n\geq 1} [1/n, 1] = (0, 1]$$은 $$\mathbb{R}$$에서 닫힌집합이 아니다. 점열 $$x_n = 1/n$$이 이 집합 안에 있으면서 극한 $$0$$이 밖에 있기 때문이며, 이는 [명제 4](#prop4)의 점열 판정으로도 곧장 확인된다.

## 예시와 계산

추상적 정의에 살을 붙이기 위해 실직선과 평면에서 구체적인 집합들을 분류한다. 핵심은 [정의 1](#def1)로 돌아가 "각 점에서 양의 반지름을 가진 공이 통째로 들어가는가"를 직접 확인하는 데 있다.

한 점이 열림을 막는 유일한 방식은 그 점이 집합의 가장자리에 놓이는 것임을 먼저 짚어 둔다. 가장 간단한 가장자리의 예로, 한 점만 제거한 직선 $$\mathbb{R} \setminus \{0\}$$은

$$\mathbb{R} \setminus \{0\} = (-\infty, 0) \cup (0, \infty)$$

처럼 두 열린구간의 합집합이므로 열린집합이고, 따라서 한원소집합 $$\{0\}$$은 그 여집합이라 닫힌집합이다. 일반적으로 거리공간에서 모든 한원소집합은 닫혀 있다.

표준거리를 준 $$\mathbb{R}$$에서 열린공은 열린구간 $$B(x, r) = (x - r, x + r)$$이므로, 열린구간 $$(a, b)$$는 각 점에서 $$r = \min\{x - a,\ b - x\} > 0$$짜리 공이 통째로 들어가 열린집합이고, 닫힌구간 $$[a, b]$$는 여집합 $$(-\infty, a) \cup (b, \infty)$$가 열려 있어 닫힌집합이다. 반면 반열린구간 $$[a, b)$$는 둘 중 어느 쪽도 아니다: 점 $$a$$에서는 어떤 공도 왼쪽으로 새어나가 담기지 못하므로 열려 있지 않고, 점열 $$b - 1/n \in [a, b)$$의 극한 $$b$$가 밖에 있으므로 닫혀 있지도 않다. 이렇게 열린집합도 닫힌집합도 아닌 집합이 존재한다는 사실은 두 개념이 서로의 부정이 아님을, 곧 "열려 있지 않음"이 "닫혀 있음"을 뜻하지 않음을 분명히 한다. 반대 극단으로 두 성질을 동시에 갖는 집합도 있다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6 (동시에 열리고 닫힌 집합)**</ins> 임의의 거리공간 $$X$$에서 $$\varnothing$$과 $$X$$는 [명제 2](#prop2)와 [명제 5](#prop5)에 의해 둘 다 열려 있고 닫혀 있다. 이렇게 열리면서 닫힌 집합을 *열린닫힌집합<sub>clopen set</sub>*이라 한다. 연결되지 않은 공간에서는 자명하지 않은 열린닫힌집합이 나타난다. 부분공간 $$X = (0, 1) \cup (2, 3) \subseteq \mathbb{R}$$에서 조각 $$(0, 1)$$은 $$X$$의 열린집합이면서, 그 여집합 $$(2, 3)$$도 열려 있어 동시에 닫힌집합이다. 한 공간에서 자명하지 않은 열린닫힌집합이 존재하는지 여부가 연결성의 척도가 된다.

</div>

폐포는 점열의 극한을 모두 더해 집합을 닫는 연산이다. 정의로 직접 계산하기보다 [명제 4](#prop4)의 [§함수의 극한과 연속, ⁋명제 2](/ko/math/analysis/limits_and_continuity#prop2)를 쓰면 폐포를 손쉽게 결정할 수 있다. 가령 $$\overline{(a, b)} = [a, b]$$인데 끝점 $$a, b$$가 각각 $$a + 1/n$$, $$b - 1/n$$의 극한으로 도달되기 때문이고, $$\overline{\mathbb{Q}} = \mathbb{R}$$인데 [§실수의 완비성, ⁋정리 5](/ko/math/analysis/completeness_of_reals#thm5)에 의해 임의의 실수가 유리수열의 극한이기 때문이다.

폐포가 점열의 극한을 더하는 연산임을 가장 또렷이 보여 주는 것은 집합 $$\{1/n : n \in \mathbb{N}\}$$이다. 이 집합 자체는 닫혀 있지 않다. 점열

$$x_n = \frac1n \longrightarrow 0$$

의 극한 $$0$$이 집합 밖에 있어 [명제 4](#prop4)의 판정에 걸리기 때문이다. 이 한 점을 더한 $$\{1/n : n \in \mathbb{N}\} \cup \{0\}$$은 더 이상 빠져나갈 극한이 없어 닫히며, 그것이 곧 폐포이다.

폐포는 닫힘 연산으로서 깔끔한 대수적 성질을 가진다. 특히 합집합과는 잘 어울리지만 교집합과는 그렇지 않다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> $$A, B \subseteq X$$에 대하여 $$\overline{A \cup B} = \overline{A} \cup \overline{B}$$이다. 그러나 일반적으로 $$\overline{A \cap B} \subseteq \overline{A} \cap \overline{B}$$만 성립하며 등호는 성립하지 않을 수 있다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$A \subseteq A \cup B$$이고 폐포는 포함을 보존하므로 $$\overline{A} \subseteq \overline{A \cup B}$$, 마찬가지로 $$\overline{B} \subseteq \overline{A \cup B}$$이며, 따라서

$$\overline{A} \cup \overline{B} \subseteq \overline{A \cup B}$$

이다. 역포함을 위해 $$\overline{A} \cup \overline{B}$$가 닫힌집합임을 보면 충분하다 ([명제 5](#prop5)의 (3), 두 닫힌집합의 합집합). $$A \cup B \subseteq \overline{A} \cup \overline{B}$$이고 우변이 $$A \cup B$$를 포함하는 닫힌집합이므로, 폐포가 그러한 가장 작은 닫힌집합이라는 정의에서 $$\overline{A \cup B} \subseteq \overline{A} \cup \overline{B}$$를 얻는다. 교집합의 경우 $$A \cap B \subseteq A$$에서 $$\overline{A \cap B} \subseteq \overline{A}$$, 같은 식으로 $$\overline{A \cap B} \subseteq \overline{B}$$이므로 $$\overline{A \cap B} \subseteq \overline{A} \cap \overline{B}$$이다. 등호가 깨지는 예로 $$A = (0, 1)$$, $$B = (1, 2)$$를 들면 $$A \cap B = \varnothing$$이라 $$\overline{A \cap B} = \varnothing$$이지만, $$\overline{A} \cap \overline{B} = [0, 1] \cap [1, 2] = \{1\}$$이다.

</details>

마지막으로 폐포·내부·경계가 점의 위치를 어떻게 분류하는지 한 예에서 종합한다. 집합 $$A$$의 *내부<sub>interior</sub>* $$A^\circ$$는 $$A$$에 포함되는 가장 큰 열린집합이고, *경계<sub>boundary</sub>* $$\partial A$$는 $$\overline{A} \setminus A^\circ$$로 정의된다.

<div class="example" markdown="1">

<ins id="ex8">**예시 8 (내부·폐포·경계)**</ins> $$\mathbb{R}^2$$에서 닫힌 단위원판 $$A = \{ (x, y) : x^2 + y^2 \leq 1 \}$$을 보자. 표준거리에서

$$A^\circ = \{ (x, y) : x^2 + y^2 < 1 \}, \qquad \overline{A} = A, \qquad \partial A = \{ (x, y) : x^2 + y^2 = 1 \}$$

이다. 내부는 열린 원판이다: 경계원 위의 점 $$p$$에서는 아무리 작은 공도 원 밖으로 새어나가 $$A$$에 담기지 못하므로 $$p \notin A^\circ$$이지만, $$\lVert p\rVert < 1$$인 점에서는 $$r = 1 - \lVert p\rVert > 0$$짜리 공이 $$A$$에 들어간다. $$A$$가 이미 닫혀 있으므로 폐포는 자기 자신이고, 경계는 정의에 따라 단위원이 된다. 같은 집합을 부분공간 $$X = A$$ 자체에서 보면 사정이 달라진다. $$X$$ 안에서는 $$A$$ 전체가 $$X$$이므로 열린닫힌집합이고 $$A^\circ = A$$, $$\partial A = \varnothing$$이 된다. 열림·닫힘·경계는 모두 그 집합이 놓인 주위 공간에 상대적인 개념임을 보여 준다.

</div>

열림과 닫힘이 거리 자체가 아니라 거리가 유도하는 열린집합들의 모임에만 의존한다는 점은, 거리를 바꾸어 보면 분명해진다. 같은 바탕집합 위에 서로 다른 거리를 주더라도 두 거리가 같은 열린집합들을 낳으면 (이를 *동치인 거리<sub>equivalent metrics</sub>*라 한다) 열린·닫힌집합의 개념은 완전히 일치한다.

<div class="example" markdown="1">

<ins id="ex9">**예시 9 (이산거리)**</ins> 집합 $$X$$ 위에 *이산거리<sub>discrete metric</sub>*를

$$d(x, y) = \begin{cases} 0 & (x = y) \\ 1 & (x \neq y) \end{cases}$$

로 주자. 반지름 $$r \leq 1$$인 열린공은 $$B(x, r) = \{x\}$$ 한 점뿐이다. 따라서 모든 한원소집합 $$\{x\}$$가 열린집합이고, 임의의 부분집합은 한원소 열린집합들의 합집합이라 [명제 2](#prop2)의 (2)에 의해 열려 있다. 곧 $$X$$의 모든 부분집합이 열린집합이며, 여집합도 모두 열려 있으므로 모든 부분집합이 동시에 닫힌집합이다. 이 공간에서는 수렴하는 점열이 결국 한 점에 머무는 점열뿐이라, [명제 4](#prop4)의 점열 판정으로도 모든 집합이 닫혀 있음을 다시 확인할 수 있다.

</div>

이산거리는 열린·닫힌집합의 구조가 표준거리에서 익숙해진 직관과 얼마나 멀어질 수 있는지 보여 주는 극단적 예이며, 위상이 거리의 세부가 아니라 "어떤 집합을 열린집합으로 부를 것인가"라는 선택에 달려 있음을 다시 한번 일깨운다.
