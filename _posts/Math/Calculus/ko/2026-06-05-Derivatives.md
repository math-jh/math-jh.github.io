---
title: "미분과 도함수"
description: "함수의 순간변화율인 미분계수를 극한으로 정의하고, 미분가능성이 연속성을 함의함을 보인다. 도함수의 개념과 기본적인 미분 공식, 그리고 미분의 기하학적·물리적 의미를 정리한다."
excerpt: "미분계수의 정의, 미분가능성과 연속성, 도함수"

categories: [Math / Calculus]
permalink: /ko/math/calculus/derivatives
sidebar: 
    nav: "calculus-ko"

header:
    overlay_image: /assets/images/Math/Calculus/Derivatives.png
    overlay_filter: 0.5

date: 2026-06-05
last_modified_at: 2026-06-05

weight: 3

published: false
---

[§연속함수](/ko/math/calculus/continuity)에서 끊김 없는 함수를 다루었다. 이제 한 걸음 더 나아가, 함수가 한 점에서 얼마나 빠르게 변하는지를 — 그래프의 접선의 기울기를, 운동의 순간속도를 — 측정한다. 이것이 미분이다.

## 미분계수의 정의

점 $$a$$ 근방에서 함수 $$f$$의 평균변화율은 $$\frac{f(x) - f(a)}{x - a}$$이다. $$x$$를 $$a$$로 보내는 극한이 존재하면, 그 값을 순간변화율로 삼는다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 함수 $$f$$가 점 $$a$$에서 *미분가능<sub>differentiable</sub>*하다는 것은 극한

$$f'(a) := \lim_{x \to a} \frac{f(x) - f(a)}{x - a} = \lim_{h \to 0} \frac{f(a+h) - f(a)}{h}$$

이 존재하는 것이다. 이 값 $$f'(a)$$를 $$f$$의 $$a$$에서의 *미분계수<sub>derivative</sub>*라 부른다. $$f$$가 정의역의 모든 점에서 미분가능하면, $$a \mapsto f'(a)$$로 정의되는 함수 $$f'$$를 $$f$$의 *도함수<sub>derivative function</sub>*라 한다.

</div>

미분계수 $$f'(a)$$는 점 $$(a, f(a))$$에서 그래프에 그은 접선의 기울기이며, $$f$$가 시간에 따른 위치라면 $$f'(a)$$는 시각 $$a$$에서의 순간속도이다. 도함수는 $$\dfrac{df}{dx}$$, $$\dfrac{d}{dx}f$$ 등으로도 적는다.

예를 들어 $$f(x) = x^2$$이면 $$\frac{(a+h)^2 - a^2}{h} = \frac{2ah + h^2}{h} = 2a + h \to 2a$$이므로 $$f'(a) = 2a$$이다. 또 $$f(x) = c$$ (상수) 이면 모든 점에서 $$f'(a) = 0$$이다.

## 미분가능성과 연속성

미분가능은 연속보다 강한 조건이다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> $$f$$가 $$a$$에서 미분가능하면 $$f$$는 $$a$$에서 연속이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$x \neq a$$에서 $$f(x) - f(a) = \dfrac{f(x)-f(a)}{x-a}\cdot(x-a)$$이다. $$x \to a$$일 때 우변의 첫 인자는 $$f'(a)$$로, 둘째 인자는 $$0$$으로 수렴하므로, 극한법칙 ([§함수와 극한, ⁋명제 3](/ko/math/calculus/functions_and_limits#prop3))에 의해 $$\lim_{x\to a}\bigl(f(x)-f(a)\bigr) = f'(a)\cdot 0 = 0$$이다. 따라서 $$\lim_{x\to a} f(x) = f(a)$$, 즉 $$f$$는 $$a$$에서 연속이다.

</details>

역은 성립하지 않는다. 대표적인 예가 $$f(x) = \lvert x\rvert$$로, 이 함수는 $$0$$에서 연속이지만 미분가능하지 않다. 실제로 $$\frac{f(h)-f(0)}{h} = \frac{\lvert h\rvert}{h}$$는 $$h \to 0^+$$일 때 $$1$$, $$h \to 0^-$$일 때 $$-1$$로, 한쪽 극한이 서로 달라 극한이 존재하지 않는다. 즉 뾰족한 점에서는 접선의 기울기가 한 값으로 정해지지 않는다.

## 미분의 선형성과 기본 공식

도함수는 극한이므로, 극한의 선형성으로부터 미분도 선형 연산임을 얻는다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3 (미분의 선형성)**</ins> $$f, g$$가 $$a$$에서 미분가능하고 $$c$$가 상수이면, $$f + g$$와 $$cf$$도 $$a$$에서 미분가능하고

$$(f+g)'(a) = f'(a) + g'(a), \qquad (cf)'(a) = c\,f'(a)$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

차분몫이 $$\dfrac{(f+g)(a+h)-(f+g)(a)}{h} = \dfrac{f(a+h)-f(a)}{h} + \dfrac{g(a+h)-g(a)}{h}$$로 갈라지고, 각 항이 $$f'(a), g'(a)$$로 수렴하므로 합도 수렴한다. $$cf$$도 마찬가지이다.

</details>

거듭제곱함수의 도함수는 다음과 같다: 자연수 $$n$$에 대해 $$\dfrac{d}{dx}x^n = n x^{n-1}$$이다. 이는 $$\frac{(x+h)^n - x^n}{h}$$를 이항정리로 전개하여 $$h \to 0$$을 취하면 얻어진다. 이 공식과 선형성을 결합하면 임의의 다항함수의 도함수를 즉시 계산할 수 있다. 예를 들어 $$\dfrac{d}{dx}(3x^4 - 5x + 2) = 12x^3 - 5$$이다.

곱·몫·합성의 미분, 그리고 삼각함수·지수함수·로그함수의 도함수 공식은 다음 글 [§미분법](/ko/math/calculus/differentiation_rules)에서 체계적으로 정리한다. 미분이 함수의 증감과 극값, 그래프의 모양에 어떻게 정보를 주는지는 [§평균값 정리](/ko/math/calculus/mean_value_theorem)와 [§도함수의 응용](/ko/math/calculus/applications_of_derivatives)에서 다룬다.

본 글에서 미분을 차분몫의 극한으로 정의했으나, 그것이 "$$f(a+h) \approx f(a) + f'(a)h$$"라는 *선형 근사*로 이해될 수 있다는 관점은 다변수로 일반화될 때 핵심이 된다 ([§다변수함수와 편미분](/ko/math/calculus/partial_derivatives)). 미분계수 정의에 쓰인 극한의 존재성 자체를 떠받치는 실수의 완비성은 해석학 [§미분](/ko/math/analysis/differentiation)에서 다시 엄밀하게 다룬다.
