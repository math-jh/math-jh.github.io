---
title: "함수와 극한"
description: "미적분학의 출발점인 실함수와 극한의 개념을 정리한다. 함수의 극한을 ε-δ 언어로 엄밀히 정의하고, 극한의 사칙연산 법칙과 압착정리, 한쪽 극한과 무한대에서의 극한을 예시와 함께 다룬다."
excerpt: "실함수의 극한을 ε-δ로 정의하고, 극한법칙·압착정리를 증명한다"

categories: [Math / Calculus]
permalink: /ko/math/calculus/functions_and_limits
sidebar: 
    nav: "calculus-ko"

header:
    overlay_image: /assets/images/Math/Calculus/Functions_and_Limits.png
    overlay_filter: 0.5

date: 2026-06-03
last_modified_at: 2026-06-03

weight: 1

published: false
---

미적분학은 실수 위에서 정의된 함수의 변화와 누적을 다루는 학문이다. 그 모든 개념 — 연속, 미분, 적분 — 의 바탕에 *극한*이 있다. 이 글에서 우리는 실함수의 극한을 직관에서 출발하여 엄밀한 정의로 다듬고, 이후 글들에서 거듭 쓰일 극한의 기본 법칙들을 정리한다.

여기서 함수란 ([\[집합론\] §함수](/ko/math/set_theory/functions))에서 정의한 일반적인 함수 중, 정의역과 공역이 모두 실수 집합 $$\mathbb{R}$$의 부분집합인 것을 말한다. 즉 $$D \subseteq \mathbb{R}$$ 위에서 정의된 *실함수<sub>real function</sub>* $$f: D \to \mathbb{R}$$를 다룬다. 본 글에서 다루는 극한은 직관적으로는 "$$x$$가 $$a$$에 한없이 가까워질 때 $$f(x)$$가 한없이 가까워지는 값"이지만, "한없이 가까워진다"는 표현은 그 자체로는 수학적 정의가 되지 못한다. 이를 부등식으로 옮긴 것이 다음의 ε-δ 정의이다.

## 극한의 정의

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $$f$$가 점 $$a$$의 근방(단, $$a$$ 자신은 제외해도 좋다)에서 정의된 실함수라 하자. 실수 $$L$$이 $$x \to a$$일 때 $$f$$의 *극한<sub>limit</sub>*이라는 것은, 임의의 $$\varepsilon > 0$$에 대하여 어떤 $$\delta > 0$$이 존재하여

$$0 < \lvert x - a \rvert < \delta \implies \lvert f(x) - L \rvert < \varepsilon$$

이 성립하는 것이다. 이때 $$\displaystyle\lim_{x \to a} f(x) = L$$로 적는다.

</div>

정의의 뜻을 풀어 보면 이렇다. 우리가 $$f(x)$$를 $$L$$에 "$$\varepsilon$$만큼 가깝게" 만들고 싶다고 요구하면 ($$\lvert f(x) - L\rvert < \varepsilon$$), 그것을 보장해 주는 "$$x$$가 $$a$$에 얼마나 가까워야 하는가"의 기준 $$\delta$$를 항상 찾아낼 수 있다는 것이다. 조건 $$0 < \lvert x - a\rvert$$는 $$x = a$$인 경우를 제외하므로, 극한은 $$f$$가 $$a$$에서 어떤 값을 갖는지 (혹은 정의되는지) 와 무관하게 결정된다.

극한이 존재하면 그 값은 유일하다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2 (극한의 유일성)**</ins> $$\displaystyle\lim_{x\to a} f(x) = L$$이고 $$\displaystyle\lim_{x\to a} f(x) = L'$$이면 $$L = L'$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$L \neq L'$$이라 가정하면 $$\varepsilon = \tfrac{1}{2}\lvert L - L'\rvert > 0$$이다. 정의 1에 의해 각각에 대응하는 $$\delta_1, \delta_2 > 0$$이 존재하여, $$0 < \lvert x-a\rvert < \delta_1$$이면 $$\lvert f(x) - L\rvert < \varepsilon$$이고, $$0 < \lvert x-a\rvert < \delta_2$$이면 $$\lvert f(x) - L'\rvert < \varepsilon$$이다. $$\delta = \min(\delta_1, \delta_2)$$로 두면 $$0 < \lvert x-a\rvert < \delta$$인 $$x$$에 대해 삼각부등식으로

$$\lvert L - L'\rvert \leq \lvert L - f(x)\rvert + \lvert f(x) - L'\rvert < \varepsilon + \varepsilon = \lvert L - L'\rvert$$

이 되어 모순이다. 따라서 $$L = L'$$이다.

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

3을 보이자. 먼저 $$f$$는 $$a$$ 근방에서 유계이다: $$\varepsilon = 1$$에 대응하는 $$\delta_0$$을 잡으면 $$0 < \lvert x-a\rvert < \delta_0$$에서 $$\lvert f(x)\rvert < \lvert L\rvert + 1$$이다. 이제

$$\lvert f(x)g(x) - LM\rvert \leq \lvert f(x)\rvert\,\lvert g(x)-M\rvert + \lvert M\rvert\,\lvert f(x)-L\rvert$$

에서, $$\varepsilon > 0$$에 대해 $$\lvert g(x)-M\rvert < \frac{\varepsilon}{2(\lvert L\rvert+1)}$$이고 $$\lvert f(x)-L\rvert < \frac{\varepsilon}{2(\lvert M\rvert+1)}$$이 되도록 $$\delta$$를 ($$\delta_0$$과 함께) 충분히 작게 잡으면 우변이 $$\varepsilon$$보다 작아진다.

4는 $$1/g(x) \to 1/M$$을 보인 뒤 3을 적용하면 된다. $$M \neq 0$$이므로 $$a$$ 근방에서 $$\lvert g(x)\rvert > \lvert M\rvert/2$$이고,

$$\left\lvert \frac{1}{g(x)} - \frac{1}{M}\right\rvert = \frac{\lvert g(x)-M\rvert}{\lvert g(x)\rvert\,\lvert M\rvert} < \frac{2}{\lvert M\rvert^2}\lvert g(x)-M\rvert$$

이므로 $$\lvert g(x)-M\rvert$$을 충분히 작게 만들면 된다.

</details>

이 법칙들로부터, 다항함수와 유리함수의 극한은 단순히 그 점에서의 함숫값을 대입하여 얻어짐을 알 수 있다 (유리함수의 경우 분모가 $$0$$이 아닐 때). 예를 들어 $$\displaystyle\lim_{x\to 2}(x^2 - 3x + 1) = 4 - 6 + 1 = -1$$이다.

## 압착정리와 한쪽 극한

극한법칙만으로 계산되지 않는 극한은 종종 부등식으로 가두어 처리한다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4 (압착정리)**</ins> $$a$$의 근방에서 ($$a$$ 제외) $$g(x) \leq f(x) \leq h(x)$$이고 $$\displaystyle\lim_{x\to a} g(x) = \lim_{x\to a} h(x) = L$$이면 $$\displaystyle\lim_{x\to a} f(x) = L$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\varepsilon > 0$$에 대해, $$g$$와 $$h$$의 극한 정의에서 얻은 $$\delta_1, \delta_2$$와 $$g \leq f \leq h$$가 성립하는 근방의 반지름 $$\delta_3$$을 모아 $$\delta = \min(\delta_1,\delta_2,\delta_3)$$으로 두자. $$0 < \lvert x-a\rvert < \delta$$이면 $$L - \varepsilon < g(x) \leq f(x) \leq h(x) < L + \varepsilon$$이므로 $$\lvert f(x) - L\rvert < \varepsilon$$이다.

</details>

압착정리의 대표적 응용은 $$\displaystyle\lim_{x\to 0}\frac{\sin x}{x} = 1$$이다. 단위원에서의 넓이 비교로 $$0 < x < \pi/2$$에서 $$\cos x \leq \frac{\sin x}{x} \leq 1$$을 얻고, $$\cos x \to 1$$이므로 압착정리가 적용된다.

한편 $$x$$가 $$a$$로 다가가는 방향을 한쪽으로 제한할 수도 있다. 정의 1에서 $$0 < \lvert x-a\rvert < \delta$$를 $$a < x < a+\delta$$로 바꾸면 *오른쪽 극한* $$\displaystyle\lim_{x\to a^+} f(x)$$를, $$a-\delta < x < a$$로 바꾸면 *왼쪽 극한* $$\displaystyle\lim_{x\to a^-} f(x)$$를 얻는다. 극한 $$\displaystyle\lim_{x\to a} f(x)$$가 존재하는 것은 두 한쪽 극한이 모두 존재하고 서로 같은 것과 동치이다.

마지막으로, $$x$$가 한없이 커질 때의 거동은 *무한대에서의 극한*으로 다룬다: $$\displaystyle\lim_{x\to\infty} f(x) = L$$이란 임의의 $$\varepsilon > 0$$에 대해 어떤 $$N$$이 존재하여 $$x > N$$이면 $$\lvert f(x) - L\rvert < \varepsilon$$인 것이다. 가령 $$\displaystyle\lim_{x\to\infty}\frac{1}{x} = 0$$이다.

이로써 극한의 정의와 기본 도구를 갖추었다. 다음 글 [§연속함수](/ko/math/calculus/continuity)에서는 극한을 이용하여 함수의 연속을 정의하고, 연속함수가 갖는 성질들을 살펴본다. 한편 본 글에서 직관적으로 다룬 실수의 "빈틈 없음"이 왜 극한 이론을 떠받치는지는 해석학에서 [§실수의 완비성](/ko/math/analysis/completeness_of_reals)으로 엄밀히 정초된다.
