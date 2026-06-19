---
title: "연속함수"
description: "함수의 연속을 극한으로 정의하고, 연속함수의 사칙연산과 합성, 그리고 닫힌구간 위 연속함수가 갖는 핵심 성질인 최대·최소 정리와 중간값 정리를 다룬다."
excerpt: "연속의 정의와 연속함수의 성질 — 최대·최소 정리와 중간값 정리"

categories: [Math / Calculus]
permalink: /ko/math/calculus/continuity
sidebar: 
    nav: "calculus-ko"

date: 2026-06-19
weight: 2

published: false
---

우리는 [§함수와 수열의 극한](/ko/math/calculus/functions_and_limits)에서 극한을 엄밀하게 정의하였으며, 그럼 자연스러운 다음 스텝은 연속성이다. 

## 연속의 정의

본질적으로, 연속의 정의에서 엄밀하지 않았던 부분, 즉 극한 부분은 이미 우리가 이전 글에서 엄밀하게 정의하였으므로, 다음 정리는 사실상 공짜라고 할 수 있다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 함수 $$f$$가 정의역의 점 $$a$$에서 *연속<sub>continuous</sub>*이라는 것은

$$\lim_{x \to a} f(x) = f(a)$$

가 성립하는 것이다. $$f$$가 정의역의 모든 점에서 연속이면 $$f$$를 *연속함수*라 부른다.

</div>

이를 풀어쓰면, , 임의의 $$\epsilon > 0$$에 대하여 어떤 $$\delta > 0$$이 존재하여 

$$\lvert x - a\rvert < \delta\Rightarrow\lvert f(x) - f(a)\rvert < \epsilon$$

이 성립하는 것이다. 여기서 $$x = a$$를 제외하는 조건 $$0 < \lvert x-a\rvert$$가 사라졌는데, 이는 $$x = a$$일 때는 $$\lvert f(a)-f(a)\rvert = 0 < \epsilon$$이 자동으로 성립하므로 굳이 제외할 필요가 없기 때문이다.

이 정의를 뜯어 보면 연속이 성립하려면 세 가지가 모두 충족되어야 함을 알 수 있다.

1. $$f(a)$$가 정의되어 있다. 
2. 극한 $$\lim_{x\to a} f(x)$$가 존재한다.
3. 위의 두 값이 서로 같다.

이 조건들 중 어느 것이 성립하지 않는지에 따라 불연속의 종류가 갈리게 되는데, 이는 연속함수의 기본 성질들을 살펴본 후 다시 돌아오기로 한다. 

## 연속함수의 연산

우선 다음 명제는 [§함수와 극한, ⁋명제 4](/ko/math/calculus/functions_and_limits#prop4)의 자명한 결과이다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> $$f$$와 $$g$$가 $$a$$에서 연속이면 $$f+g$$, $$cf$$ ($$c$$는 상수), $$fg$$도 $$a$$에서 연속이고, $$g(a) \neq 0$$이면 $$f/g$$도 $$a$$에서 연속이다. 또한 $$f$$가 $$a$$에서 연속이고 $$g$$가 $$f(a)$$에서 연속이면 합성함수 $$g \circ f$$는 $$a$$에서 연속이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

오직 합성함수만이 새로운 정리이다. 임의의 $$\epsilon > 0$$이 주어졌다 하자. 그럼 우선 $$g$$가 $$b := f(a)$$에서 연속이므로 어떤 $$\eta > 0$$이 존재하여 

$$\lvert y - b\rvert < \eta\Rightarrow\lvert g(y) - g(b)\rvert < \epsilon$$

이다. 다시 $$f$$가 $$a$$에서 연속이므로 이 $$\eta$$에 대응하는 $$\delta > 0$$이 존재하여 

$$\lvert x-a\rvert < \delta\Rightarrow\lvert f(x) - b\rvert < \eta$$

이다. 두 단계를 이으면, $$\lvert x-a\rvert < \delta$$일 때 $$y = f(x)$$가 $$\lvert y - b\rvert < \eta$$를 만족하므로 $$\lvert g(f(x)) - g(f(a))\rvert < \epsilon$$이다.

</details>

우리는 상수함수와 일차함수 $$f(x)=x$$가 연속임을 확인할 수 있다. 따라서, 이들의 합과 곱을 반복하면 임의의 다항함수가 연속이며, 여기에 몫을 취하면 임의의 유리함수는 분모가 $$0$$이 되는 점을 제외한 모든 곳에서 연속이다. 다음은 조금 덜 자명한 연속함수의 예시이다.

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> $$\sin$$ 삼각함수 $$\sin x$$가 정의역의 모든 점에서 연속임을 보이자. 우선 삼각함수의 덧셈공식에서

$$\lvert \sin x - \sin a\rvert= \left\lvert 2\cos\frac{x+a}{2}\sin\frac{x-a}{2}\right\rvert \leq 2\left\lvert \sin\frac{x-a}{2}\right\rvert$$

이 항상 성립하는 것을 안다. 이제 여기에 [§함수와 수열의 극한, ⁋예시 10](/ko/math/calculus/functions_and_limits#ex10)에서 얻은 부등식 $$\lvert \sin t\rvert \leq \lvert t\rvert$$를 적용하면, 임의의 $$a \in \mathbb{R}$$에 대해

$$\lvert \sin x - \sin a\rvert\leq\lvert x-a\rvert$$

가 성립하므로 $$\delta = \epsilon$$으로 두면 된다.

</div>

이제 $$\cos$$ 함수는 $$\sin$$함수를 평행이동하여 얻을 수 있으므로 [명제 2](#prop2)에 의해 연속이며, 따라서 위에서 살펴본 논증에 의하여 $$\tan x$$도 분모가 $$0$$이 되는 지점을 제외한 곳에서는 모두 연속이다. 

## 닫힌구간 위 연속함수의 성질

한편, 연속함수의 한 가지 유용한 성질은 $$f$$가 $$a$$에서 연속이고 $$f(a) > 0$$이면, $$\epsilon = f(a)/2$$에 대응하는 $$\delta$$를 잡을 수 있으므로 이 경우 $$a$$의 $$\delta$$-근방에서 $$f$$가 항상 양수라는 것이다. 이 단순한 사실은 그 자체로도 유용할 뿐만 아니라, 다음의 정리들로도 일반화된다.

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4 (최대·최소 정리)**</ins> $$f$$가 닫힌구간 $$[a,b]$$에서 연속이면, $$f$$는 $$[a,b]$$에서 최댓값과 최솟값을 갖는다. 즉 어떤 $$c, d \in [a,b]$$가 존재하여 모든 $$x \in [a,b]$$에 대해 $$f(d) \leq f(x) \leq f(c)$$이다.

</div>

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5 (중간값 정리)**</ins> $$f$$가 닫힌구간 $$[a,b]$$에서 연속이고 $$f(a) \neq f(b)$$이면, $$f(a)$$와 $$f(b)$$ 사이의 임의의 값 $$y$$에 대하여 $$f(c) = y$$를 만족하는 $$c \in (a,b)$$가 존재한다.

</div>

이 두 정리의 증명은 실수의 *완비성*을 본질적으로 필요로 하므로, 엄밀한 증명은 완비성을 정초한 뒤의 해석학으로 미룬다.

연속의 정의에서 $$\delta$$는 일반적으로 점 $$a$$마다 다르게 잡힌다. 모든 점에 대해 하나의 $$\delta$$를 공통으로 잡을 수 있는 더 강한 성질을 *균등연속*이라 하는데, 닫힌구간 위 연속함수는 항상 균등연속이라는 사실 또한 완비성의 귀결로 해석학에서 다룬다 ([§연속함수의 성질](/ko/math/analysis/continuous_functions)). 균등연속성은 연속함수가 적분가능함을 보이는 데 핵심적으로 쓰인다.

마지막으로, 연속이 깨지는 방식을 분류해 두면 함수의 거동을 기술하는 데 편리하다.

<div class="definition" markdown="1">

<ins id="def6">**정의 6 (불연속의 분류)**</ins> 함수 $$f$$가 점 $$a$$에서 불연속일 때, 두 한쪽 극한 $$\lim_{x\to a^\pm} f(x)$$의 거동에 따라 다음 셋으로 나눈다.

1. *제거가능 불연속<sub>removable</sub>*: 극한 $$\lim_{x\to a} f(x)$$가 존재하나 $$f(a)$$와 다르거나 $$f(a)$$가 정의되지 않은 경우. $$f(a)$$를 극한값으로 (재)정의하면 연속이 된다. 예: $$\dfrac{x^2-1}{x-1}$$ ($$a=1$$).
2. *도약 불연속<sub>jump</sub>*: 두 한쪽 극한이 모두 존재하나 서로 다른 경우. 예: $$\dfrac{\lvert x\rvert}{x}$$ ($$a=0$$).
3. *본질적 불연속<sub>essential</sub>*: 한쪽 극한 중 적어도 하나가 존재하지 않는 (진동하거나 발산하는) 경우. 예: $$\sin\dfrac1x$$ ($$a=0$$).

</div>

## 단조함수와 역함수

중간값 정리의 중요한 응용 하나는 역함수의 연속성이다. 함수가 구간에서 *순증가*(또는 순감소)한다는 것은 $$x_1 < x_2$$이면 항상 $$f(x_1) < f(x_2)$$ (또는 $$>$$) 인 것을 말하며, 이러한 함수를 통틀어 *순단조<sub>strictly monotone</sub>*라 한다. 순단조함수는 자명히 단사이므로 그 상 위에서 역함수를 가진다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> $$f$$가 구간 $$I$$에서 연속이고 순단조이면, 그 상 $$J = f(I)$$도 구간이고 역함수 $$f^{-1} : J \to I$$ 역시 연속인 순단조함수이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$f$$가 순증가한다고 하자. $$J$$가 구간임은 중간값 정리에서 따른다: $$f$$의 두 값 사이의 임의의 값도 $$f$$가 취하므로 $$J$$에 빈틈이 없다. 역함수 $$f^{-1}$$이 순증가함은 $$f$$의 순증가성에서 즉시 나온다. 연속성을 보이려면, $$f^{-1}$$이 불연속인 점이 있으면 그곳에서 $$f^{-1}$$의 상에 도약이 생겨 $$I$$가 구간이 아니게 되는데, 이는 $$I$$가 구간이라는 데 모순이다. 따라서 $$f^{-1}$$은 연속이다.

</details>

예컨대 $$f(x) = x^n$$ ($$x \geq 0$$, $$n$$은 자연수) 은 연속이고 순증가하므로, 그 역함수인 $$n$$제곱근 $$\sqrt[n]{x}$$도 연속이다. 마찬가지로 지수함수의 역함수인 로그함수, 삼각함수를 제한한 것의 역함수인 역삼각함수도 모두 연속이다. 이 명제는 [§미분법](/ko/math/calculus/differentiation_rules)에서 역함수의 미분 공식을 세우는 토대가 된다.


이로써 연속함수의 기본 성질을 갖추었다. 다음 글 [§미분과 도함수](/ko/math/calculus/derivatives)에서는 연속함수 중에서도 "매끄러운" 함수가 갖는 국소적 변화율, 즉 미분을 정의한다. 미분가능성은 연속성보다 강한 조건임을 거기서 보게 된다.