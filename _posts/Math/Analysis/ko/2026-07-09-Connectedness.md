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

date: 2026-07-09
last_modified_at: 2026-07-09

weight: 11

published: false
---

[§연속함수의 성질](/ko/math/analysis/continuous_functions)에서 연속함수가 컴팩트성을 보존함을 보았다. 연속함수가 보존하는 또 하나의 근본 성질이 연결성이며, 이로부터 [\[미적분학\] §연속함수](/ko/math/calculus/continuity)에서 도구로 받아들였던 중간값 정리가 엄밀하게 따라 나온다.

## 연결집합

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 거리공간의 부분집합 $$E$$가 *연결되지 않았다<sub>disconnected</sub>*는 것은, 열린집합 $$U, V$$가 존재하여 $$E \subseteq U \cup V$$, $$U \cap E \neq \varnothing$$, $$V \cap E \neq \varnothing$$, 그리고 $$U \cap V \cap E = \varnothing$$인 것이다. 이러한 분할이 존재하지 않으면 $$E$$가 *연결<sub>connected</sub>*되었다고 한다.

</div>

직관적으로 연결집합은 두 덩어리로 갈라 떼어 놓을 수 없는 집합이다. 실수 위에서 연결집합은 정확히 "구멍 없는" 집합, 곧 구간이다.

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2**</ins> $$\mathbb{R}$$의 부분집합이 연결인 것은 그것이 구간 (한 점 또는 공집합 포함) 인 것과 동치이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$E$$가 구간이 아니라 하자. 그러면 $$a, b \in E$$이면서 $$a < c < b$$인 $$c \notin E$$가 있다. $$U = (-\infty, c)$$, $$V = (c, \infty)$$로 두면 두 열린집합이 $$E$$를 분할하므로 $$E$$는 연결이 아니다.

거꾸로 $$E$$가 구간인데 열린집합 $$U, V$$로 분할되었다 하자. $$a \in U \cap E$$, $$b \in V \cap E$$ ($$a < b$$로 두자) 를 택하면 $$[a, b] \subseteq E$$이다. $$s = \sup\{x \in [a,b] \mid x \in U\}$$를 생각하자. $$s \in U$$이면 ($$U$$가 열려 있어) $$s$$ 오른쪽 약간도 $$U$$에 있어 $$s$$가 상한이라는 데 모순이거나 $$s = b \in V$$와 충돌하고, $$s \in V$$이면 ($$V$$가 열려 있어) $$s$$ 왼쪽 약간이 $$V$$에 있어 상한 정의에 모순이다. 어느 경우든 $$s$$가 $$U$$에도 $$V$$에도 속할 수 없어, $$[a,b] \subseteq U \cup V$$에 모순이다. 따라서 구간은 연결이다.

</details>

## 연결성의 보존과 중간값 정리

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3**</ins> $$f : X \to Y$$가 연속이고 $$E \subseteq X$$가 연결이면, 상 $$f(E)$$도 연결이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$f(E)$$가 열린집합 $$U, V$$로 분할된다고 하자. 연속성의 위상적 특징화 ([§함수의 극한과 연속, ⁋명제 3](/ko/math/analysis/limits_and_continuity#prop3))에 의해 $$f^{-1}(U)$$와 $$f^{-1}(V)$$는 열려 있고, 이들이 $$E$$를 분할함을 쉽게 확인할 수 있어 $$E$$가 연결이 아니라는 모순이 생긴다. 따라서 $$f(E)$$는 연결이다.

</details>

정리 2와 정리 3을 결합하면 중간값 정리가 즉시 따른다.

<div class="proposition" markdown="1">

<ins id="cor4">**따름정리 4 (중간값 정리)**</ins> $$f : [a, b] \to \mathbb{R}$$가 연속이고 $$f(a)$$와 $$f(b)$$ 사이의 임의의 값 $$y$$에 대하여, $$f(c) = y$$인 $$c \in [a, b]$$가 존재한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$[a,b]$$가 구간이므로 연결이고 (정리 2), 정리 3에 의해 $$f([a,b])$$도 연결, 곧 구간이다. $$f(a), f(b) \in f([a,b])$$이고 구간은 두 점 사이의 모든 값을 포함하므로 $$y \in f([a,b])$$, 즉 $$f(c) = y$$인 $$c$$가 있다.

</details>

이로써 [\[미적분학\] §연속함수, ⁋정리 4](/ko/math/calculus/continuity#thm4)에서 받아들였던 중간값 정리가 실수의 완비성에 기초하여 증명되었다. 연결성은 위상적 불변량으로, 일반 위상공간에 대한 이론은 [\[위상수학\] §연결공간](/ko/math/topology/connected_spaces)에서 다룬다.
