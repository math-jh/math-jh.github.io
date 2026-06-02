---
title: "평균값 정리"
description: "내부 극값에서 도함수가 사라진다는 페르마 정리에서 출발하여 롤의 정리와 평균값 정리를 증명한다. 도함수가 0이면 함수가 상수라는 따름정리와, 로피탈 정리의 토대가 되는 코시 평균값 정리도 다룬다."
excerpt: "페르마 정리, 롤의 정리, 평균값 정리, 코시 평균값 정리"

categories: [Math / Calculus]
permalink: /ko/math/calculus/mean_value_theorem
sidebar: 
    nav: "calculus-ko"

header:
    overlay_image: /assets/images/Math/Calculus/Mean_Value_Theorem.png
    overlay_filter: 0.5

date: 2026-06-11
last_modified_at: 2026-06-11

weight: 5

published: false
---

[§미분과 도함수](/ko/math/calculus/derivatives)에서 도함수를 정의하였으나, 도함수의 값이 함수 자체의 거동을 어떻게 통제하는지는 아직 보지 않았다. 그 다리를 놓는 것이 평균값 정리이며, 미분이 함수의 증감·극값·근사에 대해 말해 주는 거의 모든 정리가 여기서 나온다.

## 극값과 페르마 정리

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 함수 $$f$$가 점 $$c$$에서 *극댓값<sub>local maximum</sub>*을 가진다는 것은, $$c$$를 포함하는 어떤 열린구간 안의 모든 $$x$$에 대해 $$f(x) \leq f(c)$$인 것이다. *극솟값<sub>local minimum</sub>*도 대칭적으로 정의하며, 둘을 통틀어 *극값<sub>local extremum</sub>*이라 한다.

</div>

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2 (페르마 정리)**</ins> $$f$$가 내부의 점 $$c$$에서 극값을 가지고 $$c$$에서 미분가능하면 $$f'(c) = 0$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$c$$가 극댓값인 경우를 보자 (극솟값은 $$-f$$를 보면 된다). $$c$$ 근방에서 $$f(x) \leq f(c)$$이므로, 차분몫 $$\dfrac{f(c+h)-f(c)}{h}$$의 분자는 $$0$$ 이하이다. 따라서 $$h > 0$$인 쪽에서 차분몫은 $$0$$ 이하이고 그 극한 $$f'(c) \leq 0$$이며, $$h < 0$$인 쪽에서 차분몫은 $$0$$ 이상이고 그 극한 $$f'(c) \geq 0$$이다. $$f$$가 $$c$$에서 미분가능하여 두 한쪽 극한이 같아야 하므로 $$f'(c) = 0$$이다.

</details>

도함수가 $$0$$이거나 존재하지 않는 점을 *임계점<sub>critical point</sub>*이라 한다. 페르마 정리는 내부 극값이 반드시 임계점에서 일어남을 말한다. 단, 역은 거짓이다: $$f(x) = x^3$$은 $$x = 0$$에서 $$f'(0) = 0$$이지만 극값을 갖지 않는다.

## 롤의 정리와 평균값 정리

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3 (롤의 정리)**</ins> $$f$$가 닫힌구간 $$[a,b]$$에서 연속이고 열린구간 $$(a,b)$$에서 미분가능하며 $$f(a) = f(b)$$이면, $$f'(c) = 0$$인 $$c \in (a,b)$$가 존재한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$f$$가 $$[a,b]$$에서 연속이므로 최대·최소 정리 ([§연속함수, ⁋정리 3](/ko/math/calculus/continuity#thm3))에 의해 $$[a,b]$$에서 최댓값과 최솟값을 가진다. 두 값이 모두 끝점에서만 일어난다면, $$f(a) = f(b)$$이므로 최댓값과 최솟값이 같아 $$f$$는 상수이고 모든 내부 점에서 $$f' = 0$$이다. 그렇지 않으면 최댓값이나 최솟값 중 적어도 하나가 내부 점 $$c$$에서 일어나며, 그 점은 극값이므로 페르마 정리에 의해 $$f'(c) = 0$$이다.

</details>

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4 (평균값 정리)**</ins> $$f$$가 $$[a,b]$$에서 연속이고 $$(a,b)$$에서 미분가능하면

$$f'(c) = \frac{f(b) - f(a)}{b - a}$$

를 만족하는 $$c \in (a,b)$$가 존재한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

두 끝점을 잇는 직선을 빼서 롤의 정리를 적용한다. 보조함수

$$g(x) = f(x) - \left[ f(a) + \frac{f(b)-f(a)}{b-a}(x - a) \right]$$

를 두면 $$g$$는 $$[a,b]$$에서 연속, $$(a,b)$$에서 미분가능하고 $$g(a) = g(b) = 0$$이다. 롤의 정리에 의해 $$g'(c) = 0$$인 $$c \in (a,b)$$가 있고, $$g'(c) = f'(c) - \dfrac{f(b)-f(a)}{b-a}$$이므로 정리가 따른다.

</details>

평균값 정리는 "구간 위 어딘가에서 순간변화율이 평균변화율과 같다"는 것으로, 구간 끝의 정보 $$f(a), f(b)$$를 내부의 도함수와 잇는다.

## 평균값 정리의 따름정리

도함수가 함수를 통제한다는 사실의 가장 기본적 형태는 다음이다.

<div class="proposition" markdown="1">

<ins id="cor5">**따름정리 5**</ins> $$f$$가 구간 $$I$$에서 미분가능하고 모든 점에서 $$f'(x) = 0$$이면, $$f$$는 $$I$$에서 상수이다. 따라서 $$f' = g'$$이면 $$f - g$$는 상수이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$I$$의 임의의 두 점 $$x_1 < x_2$$에 대해, 평균값 정리를 $$[x_1, x_2]$$에 적용하면 $$f(x_2) - f(x_1) = f'(c)(x_2 - x_1) = 0$$인 $$c$$가 있다. 따라서 $$f(x_1) = f(x_2)$$이고 $$f$$는 상수이다. 둘째 주장은 $$f - g$$의 도함수가 $$0$$임에서 따른다.

</details>

이 따름정리는 부정적분이 상수 차이를 빼면 유일하다는 사실의 근거이며 ([§부정적분](/ko/math/calculus/antiderivatives)), 미적분의 기본정리에서 결정적으로 쓰인다. 마지막으로, 두 함수의 변화율을 동시에 비교하는 일반화가 부정형 극한 계산의 토대가 된다.

<div class="proposition" markdown="1">

<ins id="thm6">**정리 6 (코시 평균값 정리)**</ins> $$f, g$$가 $$[a,b]$$에서 연속이고 $$(a,b)$$에서 미분가능하면

$$\bigl(f(b) - f(a)\bigr)\,g'(c) = \bigl(g(b) - g(a)\bigr)\,f'(c)$$

를 만족하는 $$c \in (a,b)$$가 존재한다. 특히 $$g(a) \neq g(b)$$이고 $$g' \neq 0$$이면 $$\dfrac{f(b)-f(a)}{g(b)-g(a)} = \dfrac{f'(c)}{g'(c)}$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

보조함수 $$h(x) = \bigl(f(b)-f(a)\bigr)g(x) - \bigl(g(b)-g(a)\bigr)f(x)$$를 두면 $$h(a) = h(b) = f(b)g(a) - f(a)g(b)$$로 같다. 롤의 정리에 의해 $$h'(c) = 0$$인 $$c \in (a,b)$$가 있고, 이것이 곧 주장하는 등식이다.

</details>

평균값 정리에서 끌어낸 단조성·극값·볼록성 판정과 코시 평균값 정리에 기댄 로피탈 정리는 다음 글 [§도함수의 응용](/ko/math/calculus/applications_of_derivatives)에서 다룬다. 평균값 정리를 고계도함수로 반복 적용하면 [§테일러 정리](/ko/math/calculus/taylor_theorem)의 나머지항 평가를 얻는다. 본 글의 정리들은 모두 연속함수의 최대·최소 정리를 전제로 하는데, 그것을 떠받치는 실수의 완비성과 함께 엄밀한 증명은 해석학 [§평균값 정리와 테일러 정리](/ko/math/analysis/mean_value_theorem)에서 다시 다룬다.
