---
title: "함수와 극한"
description: "미적분학의 출발점인 함수의 극한을 ε-δ 언어로 정의하고, 극한의 사칙연산 법칙과 거듭제곱·근의 극한, 압착정리, 한쪽 극한과 무한대에서의 극한을 예시와 함께 다룬다. 수열은 정의역이 자연수인 특수한 함수로, 함수 극한의 이론을 바탕으로 ε-N 언어로 정리한다."
excerpt: "함수의 극한을 ε-δ로, 수열의 극한을 ε-N으로 정의하고 극한법칙·압착정리를 증명한다"

categories: [Math / Calculus]
permalink: /ko/math/calculus/functions_and_limits
sidebar: 
    nav: "calculus-ko"

date: 2026-06-15
last_modified_at: 2026-06-15
weight: 1

published: false
---

미적분학은 실수 위에서 정의된 함수의 변화와 누적을 다루는 학문이며, 우리는 이 카테고리에서 이러한 함수들의 미분과 극한에 대해 공부한다. 먼저 함수의 극한을 ε-δ 언어로 정의하고 극한의 기본 성질을 정리한 뒤, 마지막에 수열의 극한을 함수 극한의 특수한 경우 — 정의역이 자연수 집합인 함수의 극한 — 로 다룬다. 수열은 $$n \to \infty$$의 거동만을 다루는 이산적 판본이며, 그 극한은 함수의 극한 이론을 바탕으로 이해할 수 있다.

## 극한의 정의

함수의 미분과 적분을 정의하기 위해서는, 고등학교 때 배우는 것과 마찬가지로 극한의 개념이 필요하다. 그 때와 비교하여 지금 우리가 다루는 극한이 더 발전한 것은 이제 우리는 극한을 <em-ko>정의</em-ko>한다는 것이다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $$f$$가 점 $$a$$의 근방에서 정의된 실함수라 하자(단, $$a$$ 자신은 제외한다). 실수 $$L$$이 $$x \to a$$일 때 $$f$$의 *극한<sub>limit</sub>*이라는 것은, 임의의 $$\varepsilon > 0$$에 대하여 어떤 $$\delta > 0$$이 존재하여

$$0 < \lvert x - a \rvert < \delta \implies \lvert f(x) - L \rvert < \varepsilon$$

이 성립하는 것이다. 이때 $$\displaystyle\lim_{x \to a} f(x) = L$$로 적는다.

</div>

정의의 뜻을 풀어 본다. 우리가 $$f(x)$$를 $$L$$에 "$$\varepsilon$$만큼 가깝게" 만들고 싶다고 요구하면 ($$\lvert f(x) - L\rvert < \varepsilon$$), 그것을 보장해 주는 "$$x$$가 $$a$$에 얼마나 가까워야 하는가"의 기준 $$\delta$$를 항상 찾아낼 수 있다는 것이다. 도전자가 $$\varepsilon$$을 아무리 작게 불러도 응답자가 그에 맞는 $$\delta$$를 낼 수 있다는, 일종의 게임으로 이해하면 좋다. 결정적으로 $$\delta$$는 $$\varepsilon$$에 의존하여도 좋으며, 보통 $$\varepsilon$$이 작아질수록 $$\delta$$도 작아진다.

조건 $$0 < \lvert x - a\rvert$$는 $$x = a$$인 경우를 제외하므로, 극한은 $$f$$가 $$a$$에서 어떤 값을 갖는지 (혹은 정의되는지) 와 무관하게 결정된다. 이것이 극한과 함숫값의 본질적 차이이다. 예컨대 $$f(x) = \dfrac{x^2 - 1}{x - 1}$$은 $$x = 1$$에서 정의되지 않지만, $$x \neq 1$$에서 $$f(x) = x + 1$$이므로 $$\displaystyle\lim_{x\to 1} f(x) = 2$$이다. 만일 $$f(1) = 5$$라고 따로 값을 부여하더라도 극한은 여전히 $$2$$이다 — 극한은 $$x = 1$$에서의 값이 아니라 그 *주변*에서의 거동만을 본다.

정의를 직접 적용하는 가장 단순한 예로 일차함수를 보자. $$\displaystyle\lim_{x\to 3}(2x - 1) = 5$$임을 정의로 확인하면, $$\lvert (2x-1) - 5\rvert = 2\lvert x - 3\rvert$$이므로, 주어진 $$\varepsilon > 0$$에 대해 $$\delta = \varepsilon/2$$로 두면 $$0 < \lvert x - 3\rvert < \delta$$일 때 $$\lvert (2x-1)-5\rvert = 2\lvert x-3\rvert < 2\delta = \varepsilon$$이 성립한다. 이처럼 $$\delta$$를 $$\varepsilon$$의 식으로 명시적으로 제시하는 것이 ε-δ 논증의 전형이다.

극한이 존재하면 그 값은 유일하다. 이는 당연해 보이지만, 정의가 잘 작동함을 보증하는 첫 정리이므로 증명해 둔다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2 (극한의 유일성)**</ins> $$\displaystyle\lim_{x\to a} f(x) = L$$이고 $$\displaystyle\lim_{x\to a} f(x) = L'$$이면 $$L = L'$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$L \neq L'$$이라 가정하면 $$\varepsilon = \tfrac{1}{2}\lvert L - L'\rvert > 0$$이다. [정의 1](#def1)에 의해 각각에 대응하는 $$\delta_1, \delta_2 > 0$$이 존재하여, $$0 < \lvert x-a\rvert < \delta_1$$이면 $$\lvert f(x) - L\rvert < \varepsilon$$이고, $$0 < \lvert x-a\rvert < \delta_2$$이면 $$\lvert f(x) - L'\rvert < \varepsilon$$이다. $$\delta = \min(\delta_1, \delta_2)$$로 두면 $$0 < \lvert x-a\rvert < \delta$$인 $$x$$에 대해 삼각부등식으로

$$\lvert L - L'\rvert \leq \lvert L - f(x)\rvert + \lvert f(x) - L'\rvert < \varepsilon + \varepsilon = \lvert L - L'\rvert$$

이 되어 모순이다. 따라서 $$L = L'$$이다. (이러한 점 $$x$$가 실제로 존재함은 $$a$$가 극한점이라는 가정에서 보장된다.)

</details>

## 극한의 사칙연산

극한을 매번 정의로 계산하는 것은 번거롭다. 다행히 극한은 사칙연산과 잘 어울리므로, 복잡한 함수의 극한을 기본 함수들의 극한으로 분해할 수 있다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3 (극한법칙)**</ins> $$\displaystyle\lim_{x\to a} f(x) = L$$, $$\displaystyle\lim_{x\to a} g(x) = M$$이라 하자. 그러면

1. $$\displaystyle\lim_{x\to a} \bigl(f(x) + g(x)\bigr) = L + M$$,
2. 임의의 상수 $$c$$에 대해 $$\displaystyle\lim_{x\to a} c\,f(x) = cL$$,
3. $$\displaystyle\lim_{x\to a} f(x)g(x) = LM$$,
4. $$M \neq 0$$이면 $$\displaystyle\lim_{x\to a} \frac{f(x)}{g(x)} = \frac{L}{M}$$

이 성립한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

1을 보이자. $$\varepsilon > 0$$이 주어졌을 때, $$\varepsilon/2$$에 대응하는 $$\delta_1, \delta_2 > 0$$을 각각 $$f, g$$의 극한 정의에서 얻고 $$\delta = \min(\delta_1,\delta_2)$$로 두면, $$0 < \lvert x-a\rvert < \delta$$일 때

$$\lvert (f(x)+g(x)) - (L+M)\rvert \leq \lvert f(x)-L\rvert + \lvert g(x)-M\rvert < \tfrac{\varepsilon}{2} + \tfrac{\varepsilon}{2} = \varepsilon$$

이다. 2는 $$c=0$$이면 자명하고, $$c \neq 0$$이면 $$\varepsilon/\lvert c\rvert$$에 대응하는 $$\delta$$를 잡으면 된다.

3을 보이자. 먼저 $$f$$는 $$a$$ 근방에서 유계이다: $$\varepsilon = 1$$에 대응하는 $$\delta_0$$을 잡으면 $$0 < \lvert x-a\rvert < \delta_0$$에서 $$\lvert f(x)\rvert < \lvert L\rvert + 1$$이다. 이제 같은 항을 더하고 빼는 기법으로

$$\lvert f(x)g(x) - LM\rvert = \lvert f(x)(g(x)-M) + M(f(x)-L)\rvert \leq \lvert f(x)\rvert\,\lvert g(x)-M\rvert + \lvert M\rvert\,\lvert f(x)-L\rvert$$

을 얻는다. $$\varepsilon > 0$$에 대해 $$\lvert g(x)-M\rvert < \frac{\varepsilon}{2(\lvert L\rvert+1)}$$이고 $$\lvert f(x)-L\rvert < \frac{\varepsilon}{2(\lvert M\rvert+1)}$$이 되도록 $$\delta$$를 ($$\delta_0$$과 함께) 충분히 작게 잡으면 우변이 $$\varepsilon$$보다 작아진다.

4은 $$1/g(x) \to 1/M$$을 보인 뒤 3을 적용하면 된다. $$M \neq 0$$이므로 $$a$$ 근방에서 $$\lvert g(x)\rvert > \lvert M\rvert/2$$이고,

$$\left\lvert \frac{1}{g(x)} - \frac{1}{M}\right\rvert = \frac{\lvert g(x)-M\rvert}{\lvert g(x)\rvert\,\lvert M\rvert} < \frac{2}{\lvert M\rvert^2}\lvert g(x)-M\rvert$$

이므로 $$\lvert g(x)-M\rvert$$을 충분히 작게 만들면 된다.

</details>

이 법칙들로부터, 다항함수와 유리함수의 극한은 단순히 그 점에서의 함숫값을 대입하여 얻어짐을 알 수 있다 (유리함수의 경우 분모가 $$0$$이 아닐 때). 예를 들어 $$\displaystyle\lim_{x\to 2}(x^2 - 3x + 1) = 4 - 6 + 1 = -1$$이고, $$\displaystyle\lim_{x\to 0}\frac{x+3}{x^2+1} = \frac{3}{1} = 3$$이다. 거듭제곱과 근에 대해서는 [따름정리 4](#cor4)에서 따로 정리한다.

그러나 극한법칙은 분모와 분자가 모두 $$0$$으로 가는 $$\frac{0}{0}$$ 꼴에는 곧바로 적용되지 않는다. 이런 *부정형<sub>indeterminate form</sub>*은 대수적 변형으로 부정형을 먼저 해소해야 한다. 가령 $$\displaystyle\lim_{x\to 1}\frac{x^2 - 1}{x - 1}$$은 [명제 3](#prop3)의 4를 그대로 쓸 수 없지만, $$x \neq 1$$에서 $$\frac{x^2-1}{x-1} = x + 1$$로 약분되므로 극한은 $$2$$이다. 미분([§미분과 도함수](/ko/math/calculus/derivatives))은 본질적으로 이러한 $$\frac{0}{0}$$ 꼴 극한을 체계적으로 다루는 도구이며, 그 일반적 계산법인 로피탈 정리는 [§도함수의 응용](/ko/math/calculus/applications_of_derivatives)에서 다룬다.

<div class="proposition" markdown="1">

<ins id="cor4">**따름정리 4 (거듭제곱과 근의 극한)**</ins> $$\displaystyle\lim_{x\to a} f(x) = L$$이면

1. 임의의 양의 정수 $$k$$에 대해 $$\displaystyle\lim_{x\to a} \bigl(f(x)\bigr)^k = L^k$$,
2. $$L > 0$$이면 임의의 양의 정수 $$k$$에 대해 $$\displaystyle\lim_{x\to a} \sqrt[k]{f(x)} = \sqrt[k]{L}$$

이 성립한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

1은 $$k$$에 대한 귀납법으로, $$k=1$$은 자명하고 귀납 단계에서 [명제 3](#prop3)의 3을 적용하면 된다.

2를 보이자. 먼저 $$f(x) > 0$$이도록 $$a$$의 근방을 잡을 수 있다. $$L > 0$$이므로 $$\varepsilon_1 = L/2$$에 대응하는 $$\delta_1 > 0$$을 잡으면 $$0 < \lvert x-a\rvert < \delta_1$$에서 $$\lvert f(x)-L\rvert < L/2$$이어서 $$f(x) > L/2 > 0$$이다. 양의 실수 $$u,v$$에 대해

$$u - v = \bigl(u^{1/k}-v^{1/k}\bigr)\bigl(u^{(k-1)/k}+u^{(k-2)/k}v^{1/k}+\cdots+v^{(k-1)/k}\bigr)$$

이고, 두 번째 인자의 각 항은 $$\min(u,v)^{(k-1)/k}$$보다 크므로

$$\bigl\lvert u^{1/k}-v^{1/k}\bigr\rvert \leq \frac{\lvert u-v\rvert}{k\,\min(u,v)^{(k-1)/k}}$$

가 성립한다. 따라서 $$0 < \lvert x-a\rvert < \delta_1$$이면 $$f(x), L > L/2$$이어서

$$\bigl\lvert \sqrt[k]{f(x)}-\sqrt[k]{L}\bigr\rvert \leq \frac{\lvert f(x)-L\rvert}{k\,(L/2)^{(k-1)/k}}$$

이다. 임의의 $$\varepsilon > 0$$에 대해 $$k\,(L/2)^{(k-1)/k}\,\varepsilon$$에 대응하는 $$\delta_2 > 0$$을 택하고 $$\delta = \min(\delta_1,\delta_2)$$로 두면, $$0 < \lvert x-a\rvert < \delta$$일 때 우변이 $$\varepsilon$$보다 작아진다.

</details>

<div class="example" markdown="1">

<ins id="ex5">**예시 5 (극한법칙의 적용)**</ins> [명제 3](#prop3)과 [따름정리 4](#cor4)를 이용하면 다음과 같이 쉽게 계산한다.

$$\lim_{x\to 2}(x^2+1)(x-3) = (2^2+1)(2-3) = -5,$$

$$\lim_{x\to 4}\sqrt{x} = \sqrt{4} = 2,$$

$$\lim_{x\to -1}\frac{x^3+2}{x+2} = \frac{(-1)^3+2}{-1+2} = 1.$$

마지막 예에서 분모는 $$0$$이 아니므로 [명제 3](#prop3)의 4를 바로 쓸 수 있다.

</div>

## 압착정리와 극한의 순서

극한법칙만으로 계산되지 않는 극한은 종종 부등식으로 가두어 처리한다. 이 방법의 핵심 도구가 압착정리이다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6 (압착정리)**</ins> $$a$$의 근방에서 ($$a$$ 제외) $$g(x) \leq f(x) \leq h(x)$$이고 $$\displaystyle\lim_{x\to a} g(x) = \lim_{x\to a} h(x) = L$$이면 $$\displaystyle\lim_{x\to a} f(x) = L$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\varepsilon > 0$$에 대해, $$g$$와 $$h$$의 극한 정의에서 얻은 $$\delta_1, \delta_2$$와 $$g \leq f \leq h$$가 성립하는 근방의 반지름 $$\delta_3$$을 모아 $$\delta = \min(\delta_1,\delta_2,\delta_3)$$으로 두자. $$0 < \lvert x-a\rvert < \delta$$이면 $$L - \varepsilon < g(x) \leq f(x) \leq h(x) < L + \varepsilon$$이므로 $$\lvert f(x) - L\rvert < \varepsilon$$이다.

</details>

부등식과 극한이 어울리는 또 다른 기본 사실은 극한이 순서를 보존한다는 것이다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7 (극한의 순서 보존)**</ins> $$a$$의 근방에서 ($$a$$ 제외) $$f(x) \leq g(x)$$이고 두 극한 $$L = \displaystyle\lim_{x\to a}f(x)$$, $$M = \displaystyle\lim_{x\to a}g(x)$$이 존재하면 $$L \leq M$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$L > M$$이라 가정하고 $$\varepsilon = \tfrac{1}{2}(L - M) > 0$$으로 두자. 충분히 작은 근방에서 $$f(x) > L - \varepsilon = \tfrac{L+M}{2}$$이고 $$g(x) < M + \varepsilon = \tfrac{L+M}{2}$$이므로 $$f(x) > g(x)$$가 되어 가정에 모순이다. 따라서 $$L \leq M$$이다.

</details>

여기서 강한 부등식 $$f < g$$는 강한 부등식 $$L < M$$을 주지 않음에 유의한다. 예컨대 $$f(x) = 0 < x^2 = g(x)$$ ($$x \neq 0$$) 이지만 두 극한은 $$x \to 0$$에서 모두 $$0$$으로 같다. 부등식은 극한에서 약해질 수 있다.

압착정리의 가장 유명한 응용은 다음의 삼각함수 극한으로, 미분에서 삼각함수를 다룰 때 결정적으로 쓰인다.

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> $$\displaystyle\lim_{x\to 0}\frac{\sin x}{x} = 1$$이다. $$0 < x < \pi/2$$에서 단위원의 넓이를 비교하면 (꼭짓각 $$x$$인 삼각형 $$\subseteq$$ 부채꼴 $$\subseteq$$ 직각삼각형) $$\tfrac{1}{2}\sin x \leq \tfrac{1}{2}x \leq \tfrac{1}{2}\tan x$$, 즉 $$\sin x \leq x \leq \tan x$$를 얻는다. 양변을 $$\sin x > 0$$으로 나누면 $$1 \leq \dfrac{x}{\sin x} \leq \dfrac{1}{\cos x}$$, 역수를 취해 $$\cos x \leq \dfrac{\sin x}{x} \leq 1$$이다. $$\cos x \to 1$$이므로 압착정리에 의해 $$x \to 0^+$$에서 극한이 $$1$$이고, $$\dfrac{\sin x}{x}$$가 우함수이므로 양쪽 극한이 같아 결론을 얻는다.

</div>

<div class="example" markdown="1">

<ins id="ex9">**예시 9**</ins> $$\displaystyle\lim_{x\to 0} x\sin\frac{1}{x} = 0$$이다. $$\bigl\lvert x\sin\frac{1}{x}\bigr\rvert \leq \lvert x\rvert$$이므로 $$-\lvert x\rvert \leq x\sin\frac1x \leq \lvert x\rvert$$이고, 양 끝이 $$0$$으로 가므로 압착정리가 적용된다. 반면 $$\sin\frac1x$$ 자체는 $$x \to 0$$에서 극한을 갖지 않는데, $$x$$가 $$0$$에 다가가는 동안 $$-1$$과 $$1$$ 사이를 무한히 진동하기 때문이다. 인자 $$x$$가 이 진동을 $$0$$으로 눌러 주는 것이 핵심이다.

</div>

## 한쪽 극한과 무한대에서의 극한

지금까지의 극한은 $$x$$가 $$a$$로 양쪽에서 다가가는 경우였다. 다가가는 방향을 한쪽으로 제한하거나, $$x$$ 또는 $$f(x)$$가 무한히 커지는 경우로 정의를 확장하면 함수의 거동을 더 세밀하게 기술할 수 있다.

[정의 1](#def1)에서 $$0 < \lvert x-a\rvert < \delta$$를 $$a < x < a+\delta$$로 바꾸면 *오른쪽 극한* $$\displaystyle\lim_{x\to a^+} f(x)$$를, $$a-\delta < x < a$$로 바꾸면 *왼쪽 극한* $$\displaystyle\lim_{x\to a^-} f(x)$$를 얻는다. 극한 $$\displaystyle\lim_{x\to a} f(x)$$가 존재하는 것은 두 한쪽 극한이 모두 존재하고 서로 같은 것과 동치이다. 가령 $$f(x) = \dfrac{\lvert x\rvert}{x}$$는 $$x \to 0^+$$에서 $$1$$, $$x \to 0^-$$에서 $$-1$$로 두 한쪽 극한이 다륯므로, $$x \to 0$$에서의 극한은 존재하지 않는다. 이렇게 두 한쪽 극한이 유한하지만 서로 다른 점을 함수의 *도약<sub>jump</sub>* 불연속점이라 부른다 ([§연속함수](/ko/math/calculus/continuity)). 

함숫값이 한없이 커지는 경우는 *무한대로 발산*한다고 한다: $$\displaystyle\lim_{x\to a} f(x) = \infty$$란 임의의 $$M > 0$$에 대해 어떤 $$\delta > 0$$이 존재하여 $$0 < \lvert x-a\rvert < \delta$$이면 $$f(x) > M$$인 것이다. 예컨대 $$\displaystyle\lim_{x\to 0}\frac{1}{x^2} = \infty$$이며, 이 경우 직선 $$x = 0$$을 그래프의 *수직점근선<sub>vertical asymptote</sub>*이라 한다.

마지막으로, $$x$$가 한없이 커질 때의 거동은 *무한대에서의 극한*으로 다룬다: $$\displaystyle\lim_{x\to\infty} f(x) = L$$이란 임의의 $$\varepsilon > 0$$에 대해 어떤 $$N$$이 존재하여 $$x > N$$이면 $$\lvert f(x) - L\rvert < \varepsilon$$인 것이다. 가령 $$\displaystyle\lim_{x\to\infty}\frac{1}{x} = 0$$이고, 유리함수에서는 최고차항이 거동을 지배하여 $$\displaystyle\lim_{x\to\infty}\frac{2x^2 + 1}{3x^2 - x} = \frac{2}{3}$$이다. 이러한 유한 극한 $$L$$이 존재하면 직선 $$y = L$$이 그래프의 *수평점근선<sub>horizontal asymptote</sub>*이 된다.

<div class="remark" markdown="1">

<ins id="rmk10">**참고 10**</ins> 이들을 따로따로 외울 필요 없이, "목표를 향한 근방"과 "출발점 주변의 근방"이라는 한 틀로 통합하는 관점이 해석학의 [\[해석학\] §함수의 극한과 연속](/ko/math/analysis/limits_and_continuity)에서 거리공간의 언어로 정식화된다. 거기서는 $$\lvert x - a\rvert$$가 일반적인 거리가 되어, 같은 정의가 훨씬 넓은 물의 위에서 작동한다.

</div>

## 극한 계산의 예

지금까지의 도구를 종합하여 몇 가지 전형적 극한을 계산한다.

<div class="example" markdown="1">

<ins id="ex11">**예시 11 (부정형의 해소)**</ins> 직접 대입이 $$\frac00$$을 주면 대수적 변형으로 부정형을 해소한다. 인수분해로

$$\lim_{x\to 2}\frac{x^2 - 4}{x - 2} = \lim_{x\to 2}(x + 2) = 4,$$

분자의 유리화로

$$\lim_{x\to 0}\frac{\sqrt{1+x} - 1}{x} = \lim_{x\to 0}\frac{1}{\sqrt{1+x}+1} = \frac12,$$

그리고 [예시 8](#ex8)과 결합하여 $$\displaystyle\lim_{x\to 0}\frac{\sin 3x}{x} = \lim_{x\to 0}3\cdot\frac{\sin 3x}{3x} = 3$$이다.

</div>

<div class="example" markdown="1">

<ins id="ex12">**예시 12 (ε-δ 검증)**</ins> $$\displaystyle\lim_{x\to 2} x^2 = 4$$를 정의로 확인하자. $$\lvert x^2 - 4\rvert = \lvert x - 2\rvert\,\lvert x + 2\rvert$$인데, $$\lvert x - 2\rvert < 1$$로 제한하면 $$1 < x < 3$$이라 $$\lvert x + 2\rvert < 5$$이다. 따라서 주어진 $$\varepsilon > 0$$에 대해 $$\delta = \min\bigl(1,\ \varepsilon/5\bigr)$$로 두면, $$0 < \lvert x - 2\rvert < \delta$$일 때

$$\lvert x^2 - 4\rvert = \lvert x-2\rvert\,\lvert x+2\rvert < \delta \cdot 5 \leq \varepsilon$$

이다. $$\delta$$를 두 조건의 최솟값으로 잡는 것이 비선형 극한의 ε-δ 증명에서 흔한 기법이다.

</div>

## 수열의 극한

지금까지의 극한 이론에서 정의역은 실수의 부분집합이었다. 정의역을 자연수 집합 $$\mathbb{N}$$으로 제한하면 *수열<sub>sequence</sub>*을 얻고, $$n \to \infty$$로 가는 극한은 앞서 다룬 무한대에서의 함수 극한의 이산적 판본이 된다. 이러한 관점에서 수열의 극한을 ε-N 언어로 정리한다.

<div class="definition" markdown="1">

<ins id="def13">**정의 13**</ins> 실수열 $$(a_n)_{n=1}^\infty$$와 실수 $$L$$에 대해, 임의의 $$\varepsilon > 0$$에 대하여 어떤 자연수 $$N$$이 존재하여

$$n > N \implies \lvert a_n - L \rvert < \varepsilon$$

이 성립할 때, $$L$$을 $$n \to \infty$$일 때 $$a_n$$의 *극한<sub>limit</sub>*이라 하고 $$\displaystyle\lim_{n\to\infty} a_n = L$$로 적는다.

</div>

정의의 뜻은 분명하다. 어떤 오차 허용치 $$\varepsilon$$이 주어져도, 그 이후의 모든 항이 $$L$$에서 $$\varepsilon$$ 이내에 들어오도록 하는 지점 $$N$$을 찾을 수 있다는 것이다. 고등학교에서 익힌 "$$n$$이 커질수록 $$a_n$$이 $$L$$에 가까워진다"는 말을 정확히 만든 것이 ε-N 정의이며, 이는 [참고 10](#rmk10)에서 본 무한대에서의 함수 극한 정의를 정의역 $$\mathbb{N}$$에 적용한 것에 불과하다.

<div class="example" markdown="1">

<ins id="ex14">**예시 14**</ins> $$\displaystyle\lim_{n\to\infty}\frac{1}{n}=0$$임을 확인하자. 임의의 $$\varepsilon > 0$$에 대해 $$N > \frac{1}{\varepsilon}$$인 자연수 $$N$$을 택하면, $$n > N$$일 때 $$\frac{1}{n} < \frac{1}{N} < \varepsilon$$이므로 $$\bigl\lvert \frac{1}{n}-0\bigr\rvert < \varepsilon$$이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop15">**명제 15 (수열의 극한법칙)**</ins> $$\displaystyle\lim_{n\to\infty} a_n = L$$, $$\displaystyle\lim_{n\to\infty} b_n = M$$이라 하자. 그러면

1. $$\displaystyle\lim_{n\to\infty} \bigl(a_n + b_n\bigr) = L + M$$,
2. 임의의 상수 $$c$$에 대해 $$\displaystyle\lim_{n\to\infty} c\,a_n = cL$$,
3. $$\displaystyle\lim_{n\to\infty} a_n b_n = LM$$,
4. $$M \neq 0$$이고 모든 $$n$$에 대해 $$b_n \neq 0$$이면 $$\displaystyle\lim_{n\to\infty} \frac{a_n}{b_n} = \frac{L}{M}$$

이 성립한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

1을 보이자. $$\varepsilon > 0$$이 주어졌을 때, $$\varepsilon/2$$에 대응하는 $$N_1, N_2$$를 각각 $$a_n, b_n$$의 극한 정의에서 얻고 $$N = \max(N_1,N_2)$$로 두면, $$n > N$$일 때

$$\lvert (a_n+b_n)-(L+M)\rvert \leq \lvert a_n-L\rvert + \lvert b_n-M\rvert < \frac{\varepsilon}{2}+\frac{\varepsilon}{2} = \varepsilon$$

이다. 2는 $$c=0$$이면 자명하고, $$c\neq 0$$이면 $$\varepsilon/\lvert c\rvert$$에 대응하는 $$N$$을 잡으면 된다.

3을 보이자. 먼저 $$(a_n)$$은 유계이다: $$\varepsilon=1$$에 대응하는 $$N_0$$을 잡으면 $$n > N_0$$에서 $$\lvert a_n\rvert < \lvert L\rvert+1$$이다. 같은 항을 더하고 빼는 기법으로

$$\lvert a_nb_n-LM\rvert = \lvert a_n(b_n-M)+M(a_n-L)\rvert \leq \lvert a_n\rvert\,\lvert b_n-M\rvert + \lvert M\rvert\,\lvert a_n-L\rvert$$

를 얻는다. $$n > N_0$$이고 추가로 $$\lvert b_n-M\rvert < \frac{\varepsilon}{2(\lvert L\rvert+1)}$$, $$\lvert a_n-L\rvert < \frac{\varepsilon}{2(\lvert M\rvert+1)}$$이 되도록 $$N$$을 충분히 크게 잡으면 우변이 $$\varepsilon$$보다 작아진다.

4은 $$1/b_n \to 1/M$$을 보인 뒤 3을 적용하면 된다. $$M\neq 0$$이므로 $$N_0$$을 충분히 크게 잡으면 $$n > N_0$$에서 $$\lvert b_n\rvert > \lvert M\rvert/2$$이고,

$$\left\lvert \frac{1}{b_n}-\frac{1}{M}\right\rvert = \frac{\lvert b_n-M\rvert}{\lvert b_n\rvert\,\lvert M\rvert} < \frac{2}{\lvert M\rvert^2}\lvert b_n-M\rvert$$

이므로 $$\lvert b_n-M\rvert$$을 충분히 작게 만들면 된다. 각 단계의 논증은 [명제 3](#prop3)의 함수 극한법칙 증명과 동일한 구조를 따른다.

</details>

이로써 극한의 정의와 기본 도구를 갖추었다. 다음 글 [§연속함수](/ko/math/calculus/continuity)에서는 극한을 이용하여 함수의 연속을 정의하고, 연속함수가 갖는 성질들을 다룬다. 한편 본 글에서 직관적으로 다룬 실수의 "빈틈 없음"이 왜 극한 이론을 떠받치는지 — 예컨대 단조유계수열이 왜 수렴하는지 — 는 해석학에서 [§실수의 완비성](/ko/math/analysis/completeness_of_reals)으로 엄밀히 정초된다.
