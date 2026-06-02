---
title: "미적분의 기본정리"
description: "미분과 적분이 서로 역연산임을 밝히는 미적분의 기본정리를 두 형태로 증명한다. 가변상한 적분이 피적분함수의 원시함수임을 보이고, 이를 통해 정적분을 원시함수의 차로 계산하는 평가정리를 얻는다."
excerpt: "기본정리 제1형, 원시함수의 존재, 평가정리"

categories: [Math / Calculus]
permalink: /ko/math/calculus/fundamental_theorem_of_calculus
sidebar: 
    nav: "calculus-ko"

header:
    overlay_image: /assets/images/Math/Calculus/Fundamental_Theorem_of_Calculus.png
    overlay_filter: 0.5

date: 2026-06-25
last_modified_at: 2026-06-25

weight: 10

published: false
---

미분과 적분은 서로 다른 동기에서 출발했다. 미분은 순간변화율을, 정적분 ([§정적분](/ko/math/calculus/definite_integral))은 누적된 넓이를 잰다. 미적분의 기본정리는 이 둘이 정확히 서로의 역연산임을 밝히며, 이것이 미적분학 전체의 초석이다.

## 가변상한 적분과 제1기본정리

연속함수 $$f$$의 적분의 상한을 변수로 두어 새 함수를 만든다.

<div class="proposition" markdown="1">

<ins id="thm1">**정리 1 (미적분의 기본정리, 제1형)**</ins> $$f$$가 $$[a,b]$$에서 연속이고 $$F(x) = \displaystyle\int_a^x f(t)\,dt$$로 정의하면, $$F$$는 $$[a,b]$$에서 미분가능하고 모든 $$x$$에서

$$F'(x) = f(x)$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$h > 0$$에 대해 구간가법성 ([§정적분, ⁋명제 4](/ko/math/calculus/definite_integral#prop4))으로

$$F(x+h) - F(x) = \int_x^{x+h} f(t)\,dt$$

이다. $$f$$가 $$[x, x+h]$$에서 연속이므로 그 구간에서 최솟값 $$m_h$$와 최댓값 $$M_h$$를 가지며 ([§연속함수, ⁋정리 3](/ko/math/calculus/continuity#thm3)), 단조성에 의해 $$m_h\, h \leq F(x+h) - F(x) \leq M_h\, h$$, 즉

$$m_h \leq \frac{F(x+h) - F(x)}{h} \leq M_h$$

이다. $$h \to 0$$일 때 구간이 한 점 $$x$$로 줄어들고 $$f$$의 연속성으로 $$m_h, M_h \to f(x)$$이므로, 조임에 의해 차분몫이 $$f(x)$$로 수렴한다. $$h < 0$$인 경우도 같으므로 $$F'(x) = f(x)$$이다.

</details>

제1기본정리는 부정적분에서 미뤄 둔 존재성 문제를 해결한다.

<div class="proposition" markdown="1">

<ins id="cor2">**따름정리 2**</ins> $$[a,b]$$에서 연속인 모든 함수는 원시함수를 가진다. 구체적으로 $$F(x) = \int_a^x f$$가 그 하나이다.

</div>

이는 [§부정적분](/ko/math/calculus/antiderivatives)에서 예고했던 사실로, 연속이라는 조건만으로 원시함수의 존재가 보장됨을 말한다.

## 평가정리

제1기본정리와 평균값 정리의 따름정리를 결합하면, 정적분을 원시함수의 차로 계산하는 강력한 도구를 얻는다.

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3 (미적분의 기본정리, 제2형)**</ins> $$f$$가 $$[a,b]$$에서 연속이고 $$G$$가 $$f$$의 임의의 원시함수이면

$$\int_a^b f(x)\,dx = G(b) - G(a)$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$F(x) = \int_a^x f$$로 두면 정리 1에 의해 $$F$$도 $$f$$의 원시함수이다. 두 원시함수는 상수 차이뿐이므로 ([§평균값 정리, ⁋따름정리 5](/ko/math/calculus/mean_value_theorem#cor5)) $$F = G + C$$인 상수 $$C$$가 있다. $$F(a) = \int_a^a f = 0$$이므로 $$C = -G(a)$$이고, 따라서

$$\int_a^b f = F(b) = G(b) + C = G(b) - G(a)$$

이다.

</details>

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> $$\displaystyle\int_0^1 x^2\,dx$$를 구하자. $$x^2$$의 원시함수로 $$G(x) = \tfrac{x^3}{3}$$을 택하면 평가정리에 의해 $$\int_0^1 x^2\,dx = G(1) - G(0) = \tfrac13$$이다. 리만 합의 극한을 직접 계산하지 않고도 넓이를 얻었다.

</div>

평가정리 덕분에 정적분의 계산은 원시함수를 찾는 문제로 귀착되며, 이를 위한 치환적분·부분적분 같은 기법은 다음 글 [§적분법](/ko/math/calculus/integration_techniques)에서 다룬다. 적분 구간이나 피적분함수가 무한으로 가는 경우로의 확장은 [§이상적분](/ko/math/calculus/improper_integrals)에서, 그리고 본 정리의 가정인 연속함수의 적분가능성에 대한 엄밀한 증명은 [\[해석학\] §미적분의 기본정리](/ko/math/analysis/fundamental_theorem_of_calculus)에서 다룬다.
