---
title: "연분수"
description: "유한·무한 연분수와 그 점근분수를 정의하고, 점근분수의 점화식과 기본 항등식을 유도한다. 점근분수가 최선의 유리수 근사임과, 이차무리수가 순환연분수로 전개됨을 다룬다."
excerpt: "연분수와 점근분수, 점화식, 최선 근사와 순환성"

categories: [Math / Number Theory]
permalink: /ko/math/number_theory/continued_fractions
sidebar: 
    nav: "number_theory-ko"

header:
    overlay_image: /assets/images/Math/Number_Theory/Continued_Fractions.png
    overlay_filter: 0.5

date: 2026-06-02
last_modified_at: 2026-06-02
weight: 15

published: false
---

[§유클리드 호제법과 Bézout 항등식](/ko/math/number_theory/euclidean_algorithm)의 나눗셈을 거듭하면 유리수가 정수부와 나머지의 역수로 펼쳐진다. 이 펼침을 무리수까지 확장한 것이 연분수이며, 실수를 유리수로 가장 잘 근사하는 도구이자 다음 글의 펠 방정식을 푸는 열쇠이다.

## 연분수와 점근분수

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 정수 $$a_0$$과 양의 정수 $$a_1, a_2, \ldots$$에 대하여

$$[a_0; a_1, a_2, \ldots] = a_0 + \cfrac{1}{a_1 + \cfrac{1}{a_2 + \cfrac{1}{a_3 + \cdots}}}$$

를 *연분수<sub>continued fraction</sub>*라 한다. 유한 단계에서 끊은 $$\dfrac{p_k}{q_k} = [a_0; a_1, \ldots, a_k]$$를 $$k$$번째 *점근분수<sub>convergent</sub>*라 한다.

</div>

실수 $$x$$의 연분수 전개는 $$a_0 = \lfloor x\rfloor$$, $$x_1 = 1/(x - a_0)$$, $$a_1 = \lfloor x_1\rfloor$$, $$\ldots$$로 유클리드 호제법과 똑같은 방식으로 얻는다. $$x$$가 유리수이면 전개는 유한하고, 무리수이면 무한하다.

## 점근분수의 점화식

점근분수는 간단한 점화식으로 계산된다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> $$p_{-1} = 1, p_0 = a_0$$, $$q_{-1} = 0, q_0 = 1$$로 두고

$$p_k = a_k p_{k-1} + p_{k-2}, \qquad q_k = a_k q_{k-1} + q_{k-2}$$

로 정의하면 $$\dfrac{p_k}{q_k} = [a_0; a_1, \ldots, a_k]$$이고, 모든 $$k$$에 대하여

$$p_k q_{k-1} - p_{k-1} q_k = (-1)^{k-1}$$

이 성립한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

점화식이 점근분수를 준다는 것은 $$k$$에 대한 귀납법으로, 마지막 단계 $$a_k$$를 $$a_k + 1/x$$로 바꾸는 변형이 점화식과 양립함을 확인하면 된다. 항등식도 귀납적으로 $$p_k q_{k-1} - p_{k-1}q_k = (a_k p_{k-1} + p_{k-2})q_{k-1} - p_{k-1}(a_k q_{k-1} + q_{k-2}) = -(p_{k-1}q_{k-2} - p_{k-2}q_{k-1})$$이 되어 부호만 바뀜에서 따른다.

</details>

항등식 $$p_k q_{k-1} - p_{k-1}q_k = (-1)^{k-1}$$은 $$\gcd(p_k, q_k) = 1$$, 즉 점근분수가 기약분수임을 즉시 준다. 또한 이로부터 $$\dfrac{p_k}{q_k} - \dfrac{p_{k-1}}{q_{k-1}} = \dfrac{(-1)^{k-1}}{q_k q_{k-1}}$$이므로 점근분수들이 진동하며 극한으로 수렴함을 알 수 있다.

## 최선 근사와 순환성

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3**</ins> 무리수 $$x$$의 점근분수 $$p_k/q_k$$는 $$\left\lvert x - \dfrac{p_k}{q_k}\right\rvert < \dfrac{1}{q_k q_{k+1}} < \dfrac{1}{q_k^2}$$을 만족한다. 더 나아가 $$p_k/q_k$$는 분모가 $$q_k$$ 이하인 모든 유리수 중 $$x$$에 가장 가까운 *최선 근사*이다.

</div>

점근분수는 이처럼 분모에 비해 놀랍도록 정확한 근사를 준다. 한편 이차무리수에 대해서는 전개가 규칙적이다.

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4 (라그랑주)**</ins> 실수의 연분수 전개가 결국 주기적으로 반복되는 것은 그 수가 *이차무리수* — 유리수 계수 이차방정식의 무리수 근 — 인 것과 동치이다.

</div>

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> $$\sqrt{2} = [1; 2, 2, 2, \ldots] = [1; \overline{2}]$$이다. 실제로 $$\sqrt 2 = 1 + (\sqrt 2 - 1)$$이고 $$\dfrac{1}{\sqrt2 - 1} = \sqrt 2 + 1 = 2 + (\sqrt 2 - 1)$$이 같은 꼴로 되풀이된다. 점근분수는 $$\tfrac11, \tfrac32, \tfrac75, \tfrac{17}{12}, \ldots$$로 $$\sqrt2$$에 빠르게 수렴한다.

</div>

이차무리수 $$\sqrt{D}$$의 순환연분수는 다음 글 [§펠 방정식](/ko/math/number_theory/pell_equation)에서 $$x^2 - Dy^2 = 1$$의 정수해를 명시적으로 산출하는 도구가 된다.
