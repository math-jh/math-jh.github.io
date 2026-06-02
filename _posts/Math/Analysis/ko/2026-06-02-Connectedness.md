---
title: "연결성과 중간값 정리"
description: "연결집합을 열린집합에 의한 분할의 부재로 정의하고, 실수의 연결 부분집합이 정확히 구간임을 보인다. 연속함수가 연결성을 보존함을 증명하여 중간값 정리를 엄밀하게 끌어낸다."
excerpt: "연결집합, 실수의 구간, 중간값 정리"

categories: [Math / Analysis]
permalink: /ko/math/analysis/connectedness
sidebar: 
    nav: "analysis-ko"

header:
    overlay_image: /assets/images/Math/Analysis/Connectedness.png
    overlay_filter: 0.5

date: 2026-06-02
last_modified_at: 2026-06-02
weight: 11

published: false
---

[§연속함수의 성질](/ko/math/analysis/continuous_functions)에서 연속함수가 컴팩트성을 보존함을 보았다. 연속함수가 보존하는 또 하나의 근본 성질이 연결성이며, 이로부터 [\[미적분학\] §연속함수](/ko/math/calculus/continuity)에서 도구로 받아들였던 중간값 정리가 엄밀하게 따라 나온다.

## 연결집합

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 거리공간의 부분집합 $$E$$가 *연결되지 않았다<sub>disconnected</sub>*는 것은, 열린집합 $$U, V$$가 존재하여 $$E \subseteq U \cup V$$, $$U \cap E \neq \varnothing$$, $$V \cap E \neq \varnothing$$, 그리고 $$U \cap V \cap E = \varnothing$$인 것이다. 이러한 분할이 존재하지 않으면 $$E$$가 *연결<sub>connected</sub>*되었다고 한다.

</div>

정의 1의 분할 조건을 곱씹어 두는 것이 좋다. 우리는 $$E$$ 자체를 두 열린집합으로 가르는 것이 아니라, 주변 거리공간의 열린집합 $$U, V$$로 $$E$$를 덮되 두 조각 $$U \cap E$$와 $$V \cap E$$가 둘 다 비어 있지 않고 서로 겹치지 않도록 한다. 이때 $$U \cap E$$와 $$V \cap E$$는 부분공간 $$E$$의 상대위상에서 각각 열린집합이면서 동시에 (서로의 여집합이므로) 닫힌집합이 된다. 따라서 연결성은 "$$E$$ 안에서 공집합도 전체도 아닌 열린·닫힌 집합이 존재하지 않음"으로 바꾸어 말할 수 있다.

직관적으로 연결집합은 두 덩어리로 갈라 떼어 놓을 수 없는 집합이다. 실수 위에서 연결집합은 정확히 "구멍 없는" 집합, 곧 구간이라는 것이 다음 정리의 내용이다.

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2**</ins> $$\mathbb{R}$$의 부분집합이 연결인 것은 그것이 구간 (한 점 또는 공집합 포함) 인 것과 동치이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$E$$가 구간이 아니라 하자. 그러면 $$a, b \in E$$이면서 $$a < c < b$$인 $$c \notin E$$가 있다. $$U = (-\infty, c)$$, $$V = (c, \infty)$$로 두면 두 열린집합이 $$E$$를 분할하므로 $$E$$는 연결이 아니다.

거꾸로 $$E$$가 구간인데 열린집합 $$U, V$$로 분할되었다 하자. $$a \in U \cap E$$, $$b \in V \cap E$$ ($$a < b$$로 두자) 를 택하면 $$[a, b] \subseteq E$$이다. $$s = \sup\{x \in [a,b] \mid x \in U\}$$를 생각하자. $$s \in U$$이면 ($$U$$가 열려 있어) $$s$$ 오른쪽 약간도 $$U$$에 있어 $$s$$가 상한이라는 데 모순이거나 $$s = b \in V$$와 충돌하고, $$s \in V$$이면 ($$V$$가 열려 있어) $$s$$ 왼쪽 약간이 $$V$$에 있어 상한 정의에 모순이다. 어느 경우든 $$s$$가 $$U$$에도 $$V$$에도 속할 수 없어, $$[a,b] \subseteq U \cup V$$에 모순이다. 따라서 구간은 연결이다.

</details>

실수의 연결집합이 곧 구간이라는 이 동치는 앞으로의 모든 예시와 중간값 정리의 토대가 된다. 먼저 가장 간단한 예와 반례를 정리해 두자.

<div class="example" markdown="1">

<ins id="ex3">**예시 3 (연결집합과 비연결집합)**</ins> 

다음은 $$\mathbb{R}$$의 부분집합들이다.

1. 단일 구간 $$[0, 1]$$은 연결이다 (정리 2).
2. 두 분리된 구간의 합집합 $$E = [0, 1] \cup [2, 3]$$은 연결이 아니다. 실제로 $$U = (-1, \tfrac{3}{2})$$, $$V = (\tfrac{3}{2}, 4)$$로 두면 
   $$E \subseteq U \cup V, \quad U \cap E = [0,1] \neq \varnothing, \quad V \cap E = [2,3] \neq \varnothing, \quad U \cap V \cap E = \varnothing$$
   이 성립하여 분할이 만들어진다.
3. 유리수 전체 $$\mathbb{Q}$$는 연결이 아니다. 무리수 $$\alpha$$를 하나 잡아 $$U = (-\infty, \alpha)$$, $$V = (\alpha, \infty)$$로 두면 $$\alpha \notin \mathbb{Q}$$이므로 $$\mathbb{Q} \subseteq U \cup V$$이고 두 조각 모두 비어 있지 않다. $$\mathbb{Q}$$는 구간이 아니므로 정리 2와도 일관된다.

</div>

예시 3의 둘째와 셋째는 "$$\mathbb{R}$$의 연결집합은 구간뿐"이라는 정리 2의 한 방향을 구체적으로 보여 준다. 한편 연결집합을 새로 만드는 가장 흔한 방법은 공통점을 가진 연결집합들의 합집합을 취하는 것이다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $$\{E_\alpha\}_{\alpha \in A}$$가 거리공간의 연결 부분집합들의 모임이고 공통점 $$p \in \bigcap_\alpha E_\alpha$$를 가지면, 합집합 $$E = \bigcup_\alpha E_\alpha$$도 연결이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$E$$가 열린집합 $$U, V$$로 분할되었다고 하자. 공통점 $$p$$는 $$U$$나 $$V$$ 가운데 정확히 하나에 속하므로, 일반성을 잃지 않고 $$p \in U$$라 하자. 임의의 $$\alpha$$에 대하여 다음을 관찰한다.

$$\begin{aligned}
E_\alpha &\subseteq E \subseteq U \cup V, \\
U \cap E_\alpha &\ni p, \quad\text{즉 } U \cap E_\alpha \neq \varnothing, \\
U \cap V \cap E_\alpha &\subseteq U \cap V \cap E = \varnothing.
\end{aligned}$$

만약 어떤 $$\alpha$$에서 $$V \cap E_\alpha \neq \varnothing$$이라면 위 세 조건이 $$E_\alpha$$의 분할을 이루어 $$E_\alpha$$가 연결이라는 데 모순이다. 따라서 모든 $$\alpha$$에서 $$V \cap E_\alpha = \varnothing$$, 곧 $$E_\alpha \subseteq U$$이고, 합집합을 취하면 $$E \subseteq U$$여서 $$V \cap E = \varnothing$$이다. 이는 $$V \cap E \neq \varnothing$$이라는 분할 조건에 모순이다. 그러므로 $$E$$는 연결이다.

</details>

명제 4는 연결성을 점에 붙여 전파시키는 도구이다. 한 점 $$x$$를 포함하는 모든 연결집합의 합집합은, 명제 4에 의해 다시 연결이며 그러한 연결집합 가운데 가장 큰 것이 된다. 이를 그 점의 성분이라 부른다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> 거리공간 $$X$$의 점 $$x$$에 대하여, $$x$$를 포함하는 $$X$$의 모든 연결 부분집합의 합집합을 $$x$$의 *연결성분<sub>connected component</sub>*이라 한다.

</div>

연결성분은 명제 4에 의해 그 자체로 연결이며, $$x$$를 포함하는 연결집합 중 극대인 것이다. 서로 다른 두 점의 연결성분은 같거나 서로소이므로, 연결성분들은 $$X$$를 분할한다. 가령 $$\mathbb{Q}$$의 각 점의 연결성분은 그 점 하나뿐인 집합이며 (이런 공간을 완전부정연결<sub>totally disconnected</sub>이라 한다), $$\mathbb{R} \setminus \{0\}$$의 연결성분은 두 반직선 $$(-\infty, 0)$$과 $$(0, \infty)$$이다.


## 연결성의 보존과 중간값 정리

컴팩트성과 마찬가지로 연결성도 연속함수가 보존하는 위상적 성질이다 ([§연속함수의 성질](/ko/math/analysis/continuous_functions)에서 컴팩트성의 보존을 보았다). 핵심 착상은, 상에서의 분할이 있다면 역상을 취해 정의역에서의 분할을 만들 수 있다는 점이다. 역상이 열린집합을 열린집합으로 되돌린다는 사실 — 곧 연속성의 위상적 특징화 — 이 그대로 동력이 된다.

<div class="proposition" markdown="1">

<ins id="thm6">**정리 6**</ins> $$f : X \to Y$$가 연속이고 $$E \subseteq X$$가 연결이면, 상 $$f(E)$$도 연결이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$f(E)$$가 열린집합 $$U, V$$로 분할된다고 하자. 즉 $$f(E) \subseteq U \cup V$$, $$U \cap f(E) \neq \varnothing$$, $$V \cap f(E) \neq \varnothing$$, $$U \cap V \cap f(E) = \varnothing$$이라 하자. 연속성의 위상적 특징화 ([§함수의 극한과 연속, ⁋명제 3](/ko/math/analysis/limits_and_continuity#prop3))에 의해 $$f^{-1}(U)$$와 $$f^{-1}(V)$$는 $$X$$의 열린집합이다. 이제 이 둘이 $$E$$를 분할함을 확인한다.

$$\begin{aligned}
E &\subseteq f^{-1}(f(E)) \subseteq f^{-1}(U \cup V) = f^{-1}(U) \cup f^{-1}(V), \\
f^{-1}(U) \cap E &\neq \varnothing \quad (\text{왜냐하면 } U \cap f(E) \neq \varnothing \text{이라 } f(x) \in U \text{인 } x \in E \text{가 있음}), \\
f^{-1}(V) \cap E &\neq \varnothing \quad (\text{같은 이유}), \\
f^{-1}(U) \cap f^{-1}(V) \cap E &= f^{-1}(U \cap V) \cap E = \varnothing \quad (\text{왜냐하면 } U \cap V \cap f(E) = \varnothing).
\end{aligned}$$

따라서 $$f^{-1}(U), f^{-1}(V)$$가 $$E$$의 분할을 이루어 $$E$$가 연결이라는 데 모순이 생긴다. 그러므로 $$f(E)$$는 연결이다.

</details>

정리 2와 정리 6을 결합하면 중간값 정리가 즉시 따른다.

<div class="proposition" markdown="1">

<ins id="cor7">**따름정리 7 (중간값 정리)**</ins> $$f : [a, b] \to \mathbb{R}$$가 연속이고 $$f(a)$$와 $$f(b)$$ 사이의 임의의 값 $$y$$에 대하여, $$f(c) = y$$인 $$c \in [a, b]$$가 존재한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$[a,b]$$가 구간이므로 연결이고 (정리 2), 정리 6에 의해 $$f([a,b])$$도 연결, 곧 구간이다. $$f(a), f(b) \in f([a,b])$$이고 구간은 두 점 사이의 모든 값을 포함하므로 $$y \in f([a,b])$$, 즉 $$f(c) = y$$인 $$c$$가 있다.

</details>

이로써 [\[미적분학\] §연속함수, ⁋정리 4](/ko/math/calculus/continuity#thm4)에서 받아들였던 중간값 정리가 실수의 완비성에 기초하여 증명되었다. 증명의 구조를 다시 짚으면, 정의역의 연결성(완비성에서 나오는 정리 2)과 연속성에 의한 연결성의 보존(정리 6)이라는 두 위상적 사실만으로 중간값 정리가 따라 나온다. 해석학에서 익숙한 "사잇값을 모두 취한다"는 성질이 실은 순전히 위상적인 진술임을 보여 준다.

## 응용: 근의 존재와 고정점

중간값 정리의 가장 직접적인 쓰임은 방정식의 근이 존재함을 보이는 것이다. 양 끝에서 부호가 바뀌는 연속함수는 그 사이에서 반드시 $$0$$을 지난다.

<div class="example" markdown="1">

<ins id="ex8">**예시 8 (근의 존재)**</ins> 다항식 $$p(x) = x^3 - x - 1$$을 보자. $$p$$는 연속이고

$$p(1) = 1 - 1 - 1 = -1 < 0, \qquad p(2) = 8 - 2 - 1 = 5 > 0$$

이다. 중간값 정리(따름정리 7)를 $$y = 0$$에 적용하면, $$p(1)$$과 $$p(2)$$ 사이의 값 $$0$$에 대해 $$p(c) = 0$$인 $$c \in (1, 2)$$가 존재한다. 즉 이 삼차방정식은 $$1$$과 $$2$$ 사이에 실근을 가진다. 같은 논법으로, 차수가 홀수인 임의의 실계수 다항식은 적어도 하나의 실근을 가진다. 최고차항이 거동을 지배하여 $$x \to +\infty$$와 $$x \to -\infty$$에서 부호가 반대이기 때문이다.

</div>

또 하나의 전형적 응용은 구간을 자기 자신으로 보내는 연속함수가 고정점을 가진다는 사실이다. 이는 일차원에서의 브라우어 고정점 정리에 해당한다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9 (일차원 고정점 정리)**</ins> $$f : [0, 1] \to [0, 1]$$이 연속이면, $$f(c) = c$$인 $$c \in [0, 1]$$이 존재한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

보조함수 $$g(x) = f(x) - x$$를 생각하면 $$g$$는 $$[0,1]$$에서 연속이다. 끝점에서의 값을 보면

$$\begin{aligned}
g(0) &= f(0) - 0 = f(0) \geq 0, \\
g(1) &= f(1) - 1 \leq 0
\end{aligned}$$

인데, 이는 $$f$$의 치역이 $$[0,1]$$에 들어 있기 때문이다. 만약 $$g(0) = 0$$이면 $$c = 0$$이, $$g(1) = 0$$이면 $$c = 1$$이 곧 고정점이다. 그렇지 않으면 $$g(0) > 0 > g(1)$$이므로 중간값 정리(따름정리 7)를 $$y = 0$$에 적용하여 $$g(c) = 0$$, 곧 $$f(c) = c$$인 $$c \in (0, 1)$$를 얻는다.

</details>

연결성은 부호의 변화뿐 아니라 두 값을 잇는 연속적 경로의 존재와도 관련된다. 이 관점에서 자연스러운 변형이 경로연결성이다.

<div class="definition" markdown="1">

<ins id="def10">**정의 10**</ins> 거리공간 $$X$$의 부분집합 $$E$$가 *경로연결<sub>path-connected</sub>*이라는 것은, 임의의 두 점 $$x, y \in E$$에 대하여 연속함수 $$\gamma : [0, 1] \to E$$가 존재하여 $$\gamma(0) = x$$, $$\gamma(1) = y$$인 것이다.

</div>

경로연결은 "두 점을 $$E$$ 안에 머무는 곡선으로 이을 수 있음"을 뜻하며, 직관적으로 연결보다 강한 조건이다. 실제로 경로연결이면 연결이지만 그 역은 일반적으로 성립하지 않는다.

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> 경로연결인 집합은 연결이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$E$$가 경로연결인데 연결이 아니라고 가정하고, 열린집합 $$U, V$$가 $$E$$를 분할한다고 하자. $$x \in U \cap E$$, $$y \in V \cap E$$를 택하고, 경로연결성으로 연속함수 $$\gamma : [0,1] \to E$$를 $$\gamma(0) = x$$, $$\gamma(1) = y$$가 되도록 잡는다. 그러면 정의역 $$[0,1]$$은 연결이므로(정리 2) 정리 6에 의해 상 $$\gamma([0,1])$$도 연결이다. 그런데

$$\begin{aligned}
\gamma([0,1]) &\subseteq E \subseteq U \cup V, \\
U \cap \gamma([0,1]) &\ni \gamma(0) = x, \\
V \cap \gamma([0,1]) &\ni \gamma(1) = y, \\
U \cap V \cap \gamma([0,1]) &\subseteq U \cap V \cap E = \varnothing
\end{aligned}$$

이므로 $$U, V$$가 연결집합 $$\gamma([0,1])$$을 분할하게 되어 모순이다. 따라서 $$E$$는 연결이다.

</details>

명제 11은 연결성을 보이는 실용적인 방법을 준다. 어떤 집합이 연결임을 직접 보이려면 분할이 없음을 보여야 하지만, 두 점을 잇는 경로를 명시적으로 구성하는 편이 종종 더 쉽다. 가령 $$\mathbb{R}^n$$의 볼록집합 $$E$$는 임의의 두 점 $$x, y$$에 대해 선분 $$\gamma(t) = (1-t)x + ty$$가 $$E$$ 안에 있어 경로연결이고, 따라서 연결이다. 한편 그 역이 성립하지 않는 고전적 예는 위상수학자의 사인곡선

$$S = \{(x, \sin(1/x)) : 0 < x \leq 1\} \cup \{(0, y) : -1 \leq y \leq 1\}$$

으로, $$S$$는 연결이지만 경로연결은 아니다. 원점 부근의 진동이 점점 빨라져, 세로 선분 위의 점과 곡선 위의 점을 잇는 연속 경로를 만들 수 없기 때문이다.

지금까지의 결과를 종합하면, 실수 위에서는 연결·경로연결·구간이라는 세 성질이 모두 일치하고, 연속함수가 이 성질을 보존하기에 중간값 정리가 따라 나온다. 연결성은 위상적 불변량으로, 일반 위상공간에 대한 이론은 [\[위상수학\] §연결공간](/ko/math/topology/connected_spaces)에서 다룬다.
