---
title: "도함수의 응용"
description: "평균값 정리로부터 함수의 증가·감소 판정, 일계·이계도함수에 의한 극값 판정, 볼록성과 변곡점을 끌어낸다. 코시 평균값 정리에 기반한 로피탈 정리로 부정형 극한을 계산하고, 최적화 문제에 적용한다."
excerpt: "단조성과 극값 판정, 볼록성, 로피탈 정리, 최적화"

categories: [Math / Calculus]
permalink: /ko/math/calculus/applications_of_derivatives
sidebar: 
    nav: "calculus-ko"

date: 2026-06-02
weight: 9

drift_needed: true

published: false
---

[§평균값 정리](/ko/math/calculus/mean_value_theorem)는 도함수의 값이 함수의 거동을 통제함을 보여 주었다. 이 글에서는 그 통제를 구체적인 판정법으로 바꾸어, 도함수로부터 함수의 증감과 극값, 그래프의 굽은 방향을 읽어 내고 극한 계산과 최적화에 응용한다.

## 단조성

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1 (단조성 판정)**</ins> $$f$$가 구간 $$I$$에서 미분가능하다고 하자. $$I$$의 모든 내부 점에서 $$f'(x) > 0$$이면 $$f$$는 $$I$$에서 순증가하고, $$f'(x) < 0$$이면 순감소한다. $$f'(x) \geq 0$$이면 (넓은 의미로) 증가한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$I$$의 두 점 $$x_1 < x_2$$에 대해 평균값 정리 ([§평균값 정리, ⁋정리 4](/ko/math/calculus/mean_value_theorem#thm4))를 적용하면 $$f(x_2) - f(x_1) = f'(c)(x_2 - x_1)$$인 $$c \in (x_1, x_2)$$가 있다. $$x_2 - x_1 > 0$$이므로 우변의 부호는 $$f'(c)$$의 부호와 같다. $$f' > 0$$이면 $$f(x_2) > f(x_1)$$이어서 순증가하고, 나머지도 같다.

</details>

## 극값 판정

페르마 정리 ([§평균값 정리, ⁋정리 2](/ko/math/calculus/mean_value_theorem#thm2))에 의해 극값은 임계점에서만 일어나므로, 극값 탐색은 임계점을 조사하는 것으로 귀착된다. 임계점이 실제로 극값인지는 도함수의 부호 변화로 판정한다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2 (일계도함수 판정)**</ins> $$f$$가 $$c$$ 근방에서 연속이고 $$c$$를 제외한 근방에서 미분가능하다고 하자. $$c$$의 왼쪽에서 $$f' > 0$$, 오른쪽에서 $$f' < 0$$이면 $$f$$는 $$c$$에서 극댓값을 가진다. 부호가 반대이면 극솟값을, 부호 변화가 없으면 극값이 아니다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

[명제 1](#prop1)에 의해 $$f$$는 $$c$$의 왼쪽 구간에서 증가하고 오른쪽 구간에서 감소하므로, $$c$$ 근방의 모든 $$x$$에 대해 $$f(x) \leq f(c)$$이다. 따라서 $$c$$는 극댓값이다. 나머지 경우도 같다.

</details>

## 볼록성과 변곡점

이계도함수는 그래프가 굽는 방향을 알려 준다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 함수 $$f$$가 구간 $$I$$에서 *볼록<sub>convex</sub>*하다는 것은, $$I$$의 임의의 두 점 $$x_1, x_2$$와 $$0 \leq t \leq 1$$에 대하여

$$f\bigl((1-t)x_1 + t x_2\bigr) \leq (1-t)f(x_1) + t f(x_2)$$

가 성립하는 것이다. 즉 그래프가 두 점을 잇는 현 아래에 놓인다. 부등호가 반대이면 *오목<sub>concave</sub>*하다고 한다.

</div>

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $$f$$가 구간 $$I$$에서 두 번 미분가능하다고 하자. $$I$$에서 $$f''(x) \geq 0$$이면 $$f$$는 볼록하고, $$f''(x) \leq 0$$이면 오목하다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$f'' \geq 0$$이면 [명제 1](#prop1)에 의해 $$f'$$이 증가한다. 볼록성은 $$f'$$이 증가하는 것과 동치임이 평균값 정리로 확인된다. $$x_1 < x < x_2$$에 대해 $$[x_1, x]$$와 $$[x, x_2]$$에 [§평균값 정리와 테일러 정리, ⁋정리 3](/ko/math/analysis/mean_value_theorem#thm3)를 적용하면 $$\xi_1 < \xi_2$$인 $$\xi_1, \xi_2$$가 있어

$$\frac{f(x)-f(x_1)}{x - x_1} = f'(\xi_1) \leq f'(\xi_2) = \frac{f(x_2)-f(x)}{x_2 - x}$$

이고, 이를 정리하면 [정의 3](#def3)의 부등식을 얻는다.

</details>

볼록과 오목이 갈리는 점, 즉 그래프의 굽은 방향이 바뀌는 점을 *변곡점<sub>inflection point</sub>*이라 한다. $$f$$가 두 번 미분가능하면 변곡점에서 $$f'' = 0$$이다. 이계도함수는 임계점의 판정에도 쓰인다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5 (이계도함수 판정)**</ins> $$f'(c) = 0$$이고 $$f''(c) < 0$$이면 $$f$$는 $$c$$에서 극댓값을, $$f''(c) > 0$$이면 극솟값을 가진다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$f''(c) < 0$$이라 하자. $$f'(c) = 0$$이므로

$$f''(c) = \lim_{x\to c}\frac{f'(x) - f'(c)}{x - c} = \lim_{x\to c}\frac{f'(x)}{x - c} < 0$$

이고, 따라서 $$c$$ 근방에서 $$f'(x)/(x - c) < 0$$이다. 즉 $$c$$의 왼쪽($$x < c$$)에서 $$f'(x) > 0$$, 오른쪽에서 $$f'(x) < 0$$이고, [명제 2](#prop2)에 의해 $$c$$는 극댓값이다.

</details>

## 부정형 극한과 로피탈 정리

코시 평균값 정리는 $$\frac{0}{0}$$ 꼴의 부정형 극한을 도함수의 비로 바꾸어 준다.

<div class="proposition" markdown="1">

<ins id="thm6">**정리 6 (로피탈 정리)**</ins> $$f, g$$가 $$a$$ 근방에서 미분가능하고 $$g' \neq 0$$이며 $$\lim_{x\to a} f(x) = \lim_{x\to a} g(x) = 0$$이라 하자. 만약 극한 $$\lim_{x\to a} f'(x)/g'(x) = L$$이 존재하면

$$\lim_{x \to a} \frac{f(x)}{g(x)} = L$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$f(a) = g(a) = 0$$이 되도록 두 함수를 $$a$$에서 (재)정의하면 둘 다 $$a$$에서 연속이다. $$a$$에 충분히 가까운 $$x$$에 대해, $$a$$와 $$x$$ 사이에서 [§평균값 정리, ⁋정리 6](/ko/math/calculus/mean_value_theorem#thm6)를 적용하면

$$\frac{f(x)}{g(x)} = \frac{f(x) - f(a)}{g(x) - g(a)} = \frac{f'(\xi_x)}{g'(\xi_x)}$$

인 $$\xi_x$$가 $$a$$와 $$x$$ 사이에 있다. $$x \to a$$이면 $$\xi_x \to a$$이므로 우변은 $$L$$로 수렴한다.

</details>

예를 들어 $$\lim_{x\to 0} (\sin x)/x$$는 $$0/0$$ 꼴이고, 도함수의 비 $$\cos x / 1 \to 1$$이므로 그 값은 $$1$$이다.

로피탈 정리는 한 번 적용한 비가 다시 부정형이면 거듭 적용할 수 있다. 또한 같은 논증을 코시 평균값 정리로 다시 펴면 $$x \to a^+$$, $$x \to \infty$$ 같은 한쪽 극한이나 무한대에서의 극한, 그리고 $$\infty/\infty$$ 꼴에 대해서도 동일한 결론이 성립한다. 이 변형으로 임의의 $$\alpha > 0$$에 대해

$$\lim_{x\to\infty}\frac{\ln x}{x^\alpha} = \lim_{x\to\infty}\frac{1/x}{\alpha x^{\alpha-1}} = \lim_{x\to\infty}\frac{1}{\alpha x^\alpha} = 0$$

이 나오므로, 로그함수는 임의의 양의 거듭제곱보다 느리게 발산한다. 곱이나 차의 부정형 $$0\cdot\infty$$, $$\infty - \infty$$도 적절히 분수로 바꾸면 로피탈 정리의 영역으로 들어온다. 예컨대 $$\lim_{x\to 0^+} x\ln x$$는 $$0\cdot(-\infty)$$ 꼴이지만 $$x\ln x = \ln x / (1/x)$$로 쓰면 $$-\infty/\infty$$ 꼴이 되어

$$\lim_{x\to 0^+} x \ln x = \lim_{x\to 0^+}\frac{\ln x}{1/x} = \lim_{x\to 0^+}\frac{1/x}{-1/x^2} = \lim_{x\to 0^+}(-x) = 0$$

이고, 이로부터 $$\lim_{x\to 0^+} x^x = \exp\bigl(\lim_{x\to 0^+} x\ln x\bigr) = e^0 = 1$$과 같은 거듭제곱 부정형도 계산된다.

## 최적화

위 판정법들을 종합하면 실제 최적화 문제를 풀 수 있다. 가령 둘레가 $$P$$로 고정된 직사각형 중 넓이가 최대인 것은, 가로 $$x$$에 대한 넓이 $$A(x) = x(P/2 - x)$$ ($$0 < x < P/2$$) 를 미분해 $$A'(x) = P/2 - 2x = 0$$에서 임계점 $$x = P/4$$를 얻고 $$A''(x) = -2 < 0$$이므로 정사각형일 때 최대 $$P^2/16$$임이 나온다. 이렇게 정의역이 열린 구간이면 임계점 하나가 곧 최대를 주지만, 정의역이 닫힌 구간 $$[a, b]$$이면 사정이 다르다. 연속함수는 닫힌 유계 구간에서 최댓값과 최솟값을 가지며 ([§연속함수, ⁋정리 4](/ko/math/calculus/continuity#thm4)), 그 값은 임계점이거나 구간의 끝점에서만 일어난다. 따라서 닫힌 구간에서의 전역 최적화는 임계점에서의 값과 두 끝점에서의 값을 모두 비교하는 것으로 끝난다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7 (닫힌 구간의 전역 극값)**</ins> $$f$$가 닫힌 유계 구간 $$[a, b]$$에서 연속이고 $$(a, b)$$에서 미분가능하면, $$f$$의 최댓값과 최솟값은 $$(a, b)$$의 임계점들과 두 끝점 $$a, b$$로 이루어진 유한 후보 집합에서 달성된다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

[§연속함수, ⁋정리 4](/ko/math/calculus/continuity#thm4)에 의해 $$f$$는 어떤 점 $$c \in [a, b]$$에서 최댓값을 가진다. $$c$$가 끝점이면 후보에 들어 있다. $$c$$가 내부 점 $$(a, b)$$에 있으면 그 점은 전역 최댓값이므로 특히 극댓값이고, 페르마 정리 ([§평균값 정리, ⁋정리 2](/ko/math/calculus/mean_value_theorem#thm2))에 의해 $$f'(c) = 0$$, 즉 임계점이다. 최솟값도 같다. 따라서 두 극값은 모두 명시한 유한 집합 안에서 일어난다.

</details>

가령 $$f(x) = x^3 - 3x$$를 $$[-2, 2]$$에서 최적화하면 $$f'(x) = 3(x-1)(x+1)$$의 임계점 $$x = \pm 1$$과 두 끝점에서의 값 $$f(-2) = -2$$, $$f(-1) = 2$$, $$f(1) = -2$$, $$f(2) = 2$$를 비교하여, 최댓값 $$2$$ ($$x = -1, 2$$)와 최솟값 $$-2$$ ($$x = -2, 1$$)를 얻는다.

마지막으로 단조성·볼록성·극값 판정을 한데 모아 한 함수의 그래프 전체를 분석하는 예시를 든다. 이러한 종합 분석이 도함수 응용의 전형이다.

<div class="example" markdown="1">

<ins id="ex8">**예시 8 (그래프의 종합 분석)**</ins> $$f(x) = x e^{-x}$$를 $$\mathbb{R}$$ 위에서 분석하자. 일계·이계도함수는

$$f'(x) = (1 - x)e^{-x}, \qquad f''(x) = (x - 2)e^{-x}$$

이다. $$e^{-x} > 0$$이므로 $$f'$$의 부호는 $$1 - x$$가, $$f''$$의 부호는 $$x - 2$$가 결정한다. 따라서 $$x < 1$$에서 $$f' > 0$$ (순증가), $$x > 1$$에서 $$f' < 0$$ (순감소)이고, [명제 2](#prop2)에 의해 $$x = 1$$에서 극댓값 $$f(1) = e^{-1}$$을 가진다. 또 $$x < 2$$에서 $$f'' < 0$$ (오목), $$x > 2$$에서 $$f'' > 0$$ (볼록)이므로 $$x = 2$$가 변곡점이며 그 값은 $$f(2) = 2e^{-2}$$이다. 끝으로 $$\lim_{x\to\infty} x e^{-x} = 0$$ (로그·거듭제곱의 비와 같은 유형의 극한)이고 $$\lim_{x\to -\infty} x e^{-x} = -\infty$$이므로, 그래프는 왼쪽에서 음의 무한대로 내려가 $$x = 1$$에서 최고점 $$e^{-1}$$에 이른 뒤 $$x$$축에 점근하며 내려간다.

</div>

이처럼 도함수는 함수의 정성적 모양 전체, 곧 증감과 극값, 볼록성을 결정한다.
