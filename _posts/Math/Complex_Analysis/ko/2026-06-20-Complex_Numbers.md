---
title: "복소수와 복소평면"
description: "체 ℂ를 복습하고, 절댓값과 켤레, 극형식과 Euler 형식을 통해 복소수 곱셈의 기하적 의미를 밝힌다. 거리 d(z,w)=|z−w|로 ℂ를 ℝ²와 동일시하여 완비성과 컴팩트성을 옮기고, 입체사영으로 얻는 확장복소평면과 Riemann 구면을 소개한다."
excerpt: "체 ℂ, 절댓값과 켤레, 극형식, ℂ의 거리·완비성·컴팩트성, Riemann 구면"

categories: [Math / Complex Analysis]
permalink: /ko/math/complex_analysis/complex_numbers
sidebar: 
    nav: "complex_analysis-ko"

date: 2026-06-20

weight: 1

published: false
---

복소해석학은 복소수 위에서 정의된 함수의 미분과 적분을 다룬다. 실해석학과 달리 복소미분가능성은 매우 강한 조건이어서, 한 번 미분가능한 함수가 자동으로 무한히 미분가능하고 멱급수로 전개되는 등 풍부한 구조가 따라 나온다. 이 모든 이론의 무대가 되는 것이 복소수 전체의 집합 $$\mathbb{C}$$이며, 이 글에서는 $$\mathbb{C}$$를 대수적 대상(체)으로, 또 기하적·위상적 대상(평면과 거리공간)으로 정비한다. 복소수의 체 구조 자체는 선형대수학에서 이미 다루었으므로 ([\[선형대수학\] §가환군과 체, ⁋예시 4](/ko/math/linear_algebra/fields#ex4)) 여기서 다시 구성하지 않고, 절댓값·켤레·극형식이라는 추가 구조와 그로부터 따라 나오는 해석학적 성질에 집중한다.

## 체 ℂ와 그 위의 대수적 구조

복소수 전체의 집합 $$\mathbb{C}$$가 덧셈과 곱셈에 대하여 field<sub>체</sub>를 이룬다는 것은 이미 알고 있다 ([\[선형대수학\] §가환군과 체, ⁋정의 5](/ko/math/linear_algebra/fields#def5)). 우리는 그 표준적 표현, 곧 $$i^2 = -1$$을 만족하는 *허수단위<sub>imaginary unit</sub>* $$i$$를 도입하여 모든 복소수를 실수 두 개로 적는 방식을 출발점으로 삼는다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> *복소수<sub>complex number</sub>*는 실수 $$a, b$$에 대하여 $$z = a + bi$$ 꼴로 적히는 수이며, 여기서 $$i$$는 $$i^2 = -1$$을 만족하는 기호이다. 이때 $$a$$를 $$z$$의 *실수부<sub>real part</sub>*라 하여 $$\Real z$$로, $$b$$를 *허수부<sub>imaginary part</sub>*라 하여 $$\Img z$$로 적는다. 두 복소수의 덧셈과 곱셈은

$$(a + bi) + (c + di) = (a + c) + (b + d)i, \qquad (a + bi)(c + di) = (ac - bd) + (ad + bc)i$$

로 정의된다.

</div>

곱셈의 정의는 분배법칙을 형식적으로 전개한 뒤 $$i^2 = -1$$을 대입한 것에 지나지 않는다. 실수부와 허수부를 좌표로 읽으면 $$z = a + bi$$를 평면의 점 $$(a, b) \in \mathbb{R}^2$$와 동일시할 수 있으며, 이렇게 본 $$\mathbb{R}^2$$를 *복소평면<sub>complex plane</sub>*이라 부른다. 덧셈은 평면에서의 벡터 덧셈과 정확히 일치하고, 실수배 $$\lambda z = \lambda a + \lambda b i$$ ($$\lambda \in \mathbb{R}$$) 또한 벡터의 스칼라배와 일치하므로, $$\mathbb{C}$$는 $$\mathbb{R}$$ 위의 $$2$$차원 벡터공간이기도 하다. 복소수 곱셈만이 평면의 벡터 구조에 없는 새로운 연산이며, 그 기하적 의미는 아래 극형식에서 드러난다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 복소수 $$z = a + bi$$에 대하여 그 *복소켤레<sub>complex conjugate</sub>*를 $$\bar{z} = a - bi$$로 정의하고, *절댓값<sub>modulus</sub>* 혹은 *modulus<sub>절댓값</sub>*를

$$\lvert z\rvert = \sqrt{a^2 + b^2}$$

로 정의한다.

</div>

절댓값 $$\lvert z\rvert$$는 복소평면에서 점 $$z$$와 원점 사이의 유클리드 거리이며, 켤레 $$\bar{z}$$는 $$z$$를 실수축에 대해 반사한 점이다. 이 두 연산은 서로 긴밀히 얽혀 있어, 절댓값을 켤레로 표현할 수 있다. 실제로 $$z\bar{z} = (a+bi)(a-bi) = a^2 + b^2 = \lvert z\rvert^2$$이므로 $$\lvert z\rvert = \sqrt{z\bar{z}}$$이다. 이 항등식 덕분에 $$0$$이 아닌 $$z$$의 역원을 명시적으로 적을 수 있다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> 임의의 복소수 $$z, w$$에 대하여 다음이 성립한다.

1. $$\overline{z + w} = \bar{z} + \bar{w}$$이고 $$\overline{zw} = \bar{z}\,\bar{w}$$이다.
2. $$\overline{\bar{z}} = z$$이고, $$z + \bar{z} = 2\Real z$$, $$z - \bar{z} = 2i\Img z$$이다. 특히 $$z = \bar{z}$$인 것은 $$z$$가 실수인 것과 동치이다.
3. $$z\bar{z} = \lvert z\rvert^2$$이고, $$z \neq 0$$이면 $$z^{-1} = \dfrac{\bar{z}}{\lvert z\rvert^2}$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$z = a + bi$$, $$w = c + di$$로 둔다.

1. 덧셈에 대하여 $$\overline{z + w} = \overline{(a+c)+(b+d)i} = (a+c)-(b+d)i = (a-bi)+(c-di) = \bar{z}+\bar{w}$$이다. 곱셈에 대하여는 [정의 1](#def1)의 곱셈 공식으로

    $$\overline{zw} = \overline{(ac - bd) + (ad + bc)i} = (ac - bd) - (ad + bc)i$$

    이고, 한편 $$\bar{z}\,\bar{w} = (a - bi)(c - di) = (ac - bd) - (ad + bc)i$$이므로 둘이 같다.

2. $$\overline{\bar{z}} = \overline{a - bi} = a + bi = z$$이다. 또 $$z + \bar{z} = (a+bi)+(a-bi) = 2a = 2\Real z$$이고 $$z - \bar{z} = 2bi = 2i\Img z$$이다. 따라서 $$z = \bar{z}$$인 것은 $$\Img z = b = 0$$, 곧 $$z$$가 실수인 것과 동치이다.

3. 위에서 본 대로 $$z\bar{z} = a^2 + b^2 = \lvert z\rvert^2$$이다. $$z \neq 0$$이면 $$\lvert z\rvert^2 > 0$$이고

    $$z \cdot \frac{\bar{z}}{\lvert z\rvert^2} = \frac{z\bar{z}}{\lvert z\rvert^2} = \frac{\lvert z\rvert^2}{\lvert z\rvert^2} = 1$$

    이므로 $$\bar{z}/\lvert z\rvert^2$$가 $$z$$의 곱셈에 대한 역원이다. 역원의 유일성 ([\[선형대수학\] §가환군과 체, ⁋명제 2](/ko/math/linear_algebra/fields#prop2)) 에 의해 이것이 $$z^{-1}$$이다.

</details>

명제 3의 셋째 항은 복소수 나눗셈을 실질적으로 계산하는 방법을 준다. 분모와 분자에 분모의 켤레를 곱하면 분모가 실수가 되어, 가령 $$\dfrac{1}{1+i} = \dfrac{1-i}{(1+i)(1-i)} = \dfrac{1-i}{2}$$와 같이 표준형 $$a + bi$$로 정리된다. 이어서 절댓값이 곱셈과 어떻게 어울리는지를 보면, 절댓값은 곱셈을 정확히 보존하며 덧셈에 대해서는 삼각부등식을 만족한다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> 임의의 복소수 $$z, w$$에 대하여 다음이 성립한다.

1. $$\lvert z\rvert \geq 0$$이고, $$\lvert z\rvert = 0$$인 것은 $$z = 0$$인 것과 동치이다.
2. $$\lvert zw\rvert = \lvert z\rvert\,\lvert w\rvert$$이고 $$\lvert \bar{z}\rvert = \lvert z\rvert$$이다.
3. (삼각부등식) $$\lvert z + w\rvert \leq \lvert z\rvert + \lvert w\rvert$$이며, 또한 $$\bigl\lvert \lvert z\rvert - \lvert w\rvert \bigr\rvert \leq \lvert z - w\rvert$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

1. $$\lvert z\rvert = \sqrt{a^2 + b^2} \geq 0$$이고, 이것이 $$0$$인 것은 $$a^2 + b^2 = 0$$, 곧 $$a = b = 0$$인 것과 동치이다.

2. 곱셈의 보존성은 켤레의 곱셈성 ([명제 3](#prop3))으로부터 따라 나온다.

    $$\lvert zw\rvert^2 = (zw)\overline{(zw)} = zw\bar{z}\bar{w} = (z\bar{z})(w\bar{w}) = \lvert z\rvert^2\,\lvert w\rvert^2$$

    이고 양변이 음이 아니므로 $$\lvert zw\rvert = \lvert z\rvert\,\lvert w\rvert$$이다. 또 $$\lvert \bar{z}\rvert^2 = \bar{z}\,\overline{\bar{z}} = \bar{z}z = \lvert z\rvert^2$$이므로 $$\lvert \bar{z}\rvert = \lvert z\rvert$$이다.

3. 먼저 임의의 복소수 $$u$$에 대해 $$\Real u \leq \lvert u\rvert$$임에 유의한다. $$u = x + yi$$이면 $$x \leq \sqrt{x^2 + y^2}$$이기 때문이다. 이를 $$u = z\bar{w}$$에 적용하면

    $$\begin{aligned}
    \lvert z + w\rvert^2
    &= (z + w)(\bar{z} + \bar{w}) = z\bar{z} + z\bar{w} + w\bar{z} + w\bar{w} \\
    &= \lvert z\rvert^2 + \lvert w\rvert^2 + (z\bar{w} + \overline{z\bar{w}}) \\
    &= \lvert z\rvert^2 + \lvert w\rvert^2 + 2\Real(z\bar{w}) \\
    &\leq \lvert z\rvert^2 + \lvert w\rvert^2 + 2\lvert z\bar{w}\rvert = \lvert z\rvert^2 + \lvert w\rvert^2 + 2\lvert z\rvert\,\lvert w\rvert = (\lvert z\rvert + \lvert w\rvert)^2
    \end{aligned}$$

    이고, 둘째 줄에서 $$w\bar{z} = \overline{z\bar{w}}$$를, 마지막 줄에서 $$\lvert z\bar{w}\rvert = \lvert z\rvert\,\lvert w\rvert$$를 썼다. 양변에 제곱근을 취하면 삼각부등식을 얻는다. 역삼각부등식은 $$\lvert z\rvert = \lvert (z - w) + w\rvert \leq \lvert z - w\rvert + \lvert w\rvert$$에서 $$\lvert z\rvert - \lvert w\rvert \leq \lvert z - w\rvert$$를, $$z$$와 $$w$$의 역할을 바꾸어 $$\lvert w\rvert - \lvert z\rvert \leq \lvert z - w\rvert$$를 얻어 둘을 합치면 따라 나온다.

</details>

곱셈에 대한 절댓값의 보존성 $$\lvert zw\rvert = \lvert z\rvert\,\lvert w\rvert$$은 복소수에서만 나타나는 특별한 성질로, 실수의 절댓값 $$\lvert xy\rvert = \lvert x\rvert\,\lvert y\rvert$$를 평면으로 끌어올린 것이다. 이 성질은 곧 보게 될 극형식에서 곱셈이 절댓값을 곱하고 각도를 더하는 변환이라는 사실의 대수적 그림자이다.

## 극형식과 곱셈의 기하

복소수를 평면의 점으로 보면 직교좌표 $$(a, b)$$ 대신 극좌표, 곧 원점으로부터의 거리와 양의 실수축과 이루는 각도로 표현하는 것이 자연스럽다. 이 표현에서 복소수 곱셈의 기하적 의미가 가장 선명하게 드러난다.

이 글에서는 다음의 *Euler 공식<sub>Euler's formula</sub>*

$$e^{i\theta} = \cos\theta + i\sin\theta \qquad (\theta \in \mathbb{R})$$

을 표기상의 약속으로 받아들여, $$\cos\theta + i\sin\theta$$를 $$e^{i\theta}$$로 줄여 적는다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> $$0$$이 아닌 복소수 $$z$$에 대하여 $$r = \lvert z\rvert > 0$$이라 하고, $$z/r$$가 단위원 위의 점이므로 $$z/r = \cos\theta + i\sin\theta$$를 만족하는 실수 $$\theta$$를 잡을 수 있다. 그러면

$$z = r(\cos\theta + i\sin\theta) = re^{i\theta}$$

로 적히며, 이를 $$z$$의 *극형식<sub>polar form</sub>*이라 한다. 여기서 $$\theta$$를 $$z$$의 *편각<sub>argument</sub>*이라 하고 $$\arg z$$로 적는다.

</div>

편각은 $$2\pi$$의 정수배를 더해도 같은 복소수를 주므로 유일하게 결정되지 않는다. 곧 $$\arg z$$는 $$2\pi$$를 법으로 하여서만 정해진다. 이 다가성은 복소로그함수와 거듭제곱근을 다룰 때 본질적인 역할을 하지만, 여기서는 곱셈의 기하적 해석에 집중한다. Euler 공식과 지수법칙 $$e^{i\theta}e^{i\varphi} = e^{i(\theta + \varphi)}$$ (이는 삼각함수의 덧셈정리와 동치이다) 로부터 곱셈이 극형식에서 어떻게 작동하는지가 곧바로 나온다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> $$z = re^{i\theta}$$, $$w = se^{i\varphi}$$ ($$r, s > 0$$) 이면

$$zw = rs\, e^{i(\theta + \varphi)}$$

이다. 따라서 $$\lvert zw\rvert = \lvert z\rvert\,\lvert w\rvert$$이고 $$\arg(zw) = \arg z + \arg w$$ (법 $$2\pi$$) 이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

삼각함수의 덧셈정리로

$$\begin{aligned}
(\cos\theta + i\sin\theta)(\cos\varphi + i\sin\varphi)
&= (\cos\theta\cos\varphi - \sin\theta\sin\varphi) + i(\sin\theta\cos\varphi + \cos\theta\sin\varphi) \\
&= \cos(\theta + \varphi) + i\sin(\theta + \varphi)
\end{aligned}$$

이므로 $$e^{i\theta}e^{i\varphi} = e^{i(\theta + \varphi)}$$이다. 따라서

$$zw = (re^{i\theta})(se^{i\varphi}) = rs\, e^{i\theta}e^{i\varphi} = rs\, e^{i(\theta + \varphi)}$$

이다. $$rs > 0$$이고 $$e^{i(\theta+\varphi)}$$가 단위원 위의 점이므로 이것이 $$zw$$의 극형식이며, 절댓값은 $$rs = \lvert z\rvert\,\lvert w\rvert$$, 편각은 $$\theta + \varphi$$이다.

</details>

명제 6은 복소수 $$z$$를 곱하는 변환 $$w \mapsto zw$$가 평면 위에서 *절댓값 $$\lvert z\rvert$$만큼의 확대와 각도 $$\arg z$$만큼의 회전*을 합성한 것임을 말한다. 특히 절댓값이 $$1$$인 복소수 $$e^{i\theta}$$를 곱하는 것은 원점을 중심으로 한 각도 $$\theta$$의 회전이고, $$i = e^{i\pi/2}$$를 곱하는 것은 반시계방향 $$90^\circ$$ 회전이다. 이로써 곱셈이라는 대수적 연산이 평면의 닮음변환이라는 기하적 대상과 정확히 대응함을 본다. 같은 사실을 반복 적용하면 거듭제곱과 거듭제곱근의 공식이 따라 나온다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7 (de Moivre 공식)**</ins> 임의의 정수 $$n$$과 실수 $$\theta$$에 대하여

$$(\cos\theta + i\sin\theta)^n = \cos(n\theta) + i\sin(n\theta)$$

이다. 따라서 $$0$$이 아닌 복소수 $$z = re^{i\theta}$$의 $$n$$제곱근은 정확히 $$n$$개 존재하며,

$$z_k = r^{1/n}\exp\!\left(i\,\frac{\theta + 2\pi k}{n}\right) \qquad (k = 0, 1, \ldots, n-1)$$

로 주어진다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

먼저 $$n \geq 0$$에 대한 de Moivre 공식을 귀납법으로 보인다. $$n = 0$$이면 양변이 $$1$$로 자명하다. $$n$$에서 성립한다고 가정하면 명제 6에 의해

$$(\cos\theta + i\sin\theta)^{n+1} = (\cos\theta + i\sin\theta)^n(\cos\theta + i\sin\theta) = (\cos n\theta + i\sin n\theta)(\cos\theta + i\sin\theta) = \cos((n+1)\theta) + i\sin((n+1)\theta)$$

이다. 음의 정수 $$n = -m$$ ($$m > 0$$) 에 대하여는 $$(\cos\theta + i\sin\theta)^{-1} = \cos\theta - i\sin\theta = \cos(-\theta) + i\sin(-\theta)$$이므로 위의 결과를 $$-\theta$$에 적용하면 된다.

이제 $$w = se^{i\varphi}$$가 $$w^n = z$$를 만족한다고 하자. 절댓값을 비교하면 $$s^n = r$$이므로 $$s = r^{1/n}$$ (양의 실수 제곱근) 이다. 편각을 비교하면 $$n\varphi \equiv \theta \pmod{2\pi}$$, 곧 어떤 정수 $$k$$에 대해 $$n\varphi = \theta + 2\pi k$$이므로 $$\varphi = (\theta + 2\pi k)/n$$이다. $$k$$와 $$k + n$$은 편각을 $$2\pi$$만큼 차이 나게 하여 같은 복소수를 주므로, 서로 다른 근은 $$k = 0, 1, \ldots, n-1$$에서 나오는 $$n$$개뿐이다.

</details>

de Moivre 공식의 한 특수한 경우인 $$n$$제곱근 $$1$$, 곧 *단위근<sub>root of unity</sub>*은 $$z = 1$$에 위 공식을 적용한 $$\exp(2\pi i k/n)$$ ($$k = 0, \ldots, n-1$$) 이며, 복소평면에서 단위원에 내접하는 정 $$n$$각형의 꼭짓점을 이룬다. 이 기하적 그림은 복소수의 곱셈 구조가 평면의 대칭성과 직결됨을 보여 주는 가장 단순한 예이다.

## 거리공간으로서의 ℂ

절댓값은 복소평면에 거리를 부여하여 $$\mathbb{C}$$를 해석학의 무대로 만든다. 이 거리는 본질적으로 $$\mathbb{R}^2$$의 유클리드 거리와 같으며, 따라서 $$\mathbb{R}^2$$에서 확립한 완비성과 컴팩트성이 그대로 옮겨 온다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> 두 복소수 $$z, w$$에 대하여 그 *거리<sub>distance</sub>*를

$$d(z, w) = \lvert z - w\rvert$$

로 정의한다.

</div>

이 $$d$$가 [\[해석학\] §거리공간, ⁋정의 1](/ko/math/analysis/metric_spaces#def1)의 거리공간 공리를 만족함은 명제 4에서 곧바로 나온다. 비음성과 $$d(z,w)=0 \Leftrightarrow z=w$$는 명제 4의 첫째 항이고, 대칭성 $$\lvert z - w\rvert = \lvert w - z\rvert$$는 $$\lvert -u\rvert = \lvert u\rvert$$로부터, 삼각부등식 $$\lvert z - w\rvert \leq \lvert z - v\rvert + \lvert v - w\rvert$$는 $$z - w = (z - v) + (v - w)$$에 명제 4의 삼각부등식을 적용하여 얻는다. 더 나아가 이 거리는 $$\mathbb{R}^2$$의 유클리드 거리와 글자 그대로 일치한다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> $$z = a + bi$$를 $$(a, b) \in \mathbb{R}^2$$와 동일시하면, $$\mathbb{C}$$의 거리 $$d(z, w) = \lvert z - w\rvert$$는 $$\mathbb{R}^2$$의 유클리드 거리와 같다. 따라서 점열 $$z_n = a_n + b_n i$$가 $$z = a + bi$$로 수렴하는 것은 $$a_n \to a$$이고 $$b_n \to b$$인 것과 동치이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$z = a + bi$$, $$w = c + di$$이면 $$z - w = (a - c) + (b - d)i$$이므로

$$d(z, w) = \lvert z - w\rvert = \sqrt{(a - c)^2 + (b - d)^2}$$

이고, 이것이 곧 $$\mathbb{R}^2$$에서 점 $$(a, b)$$와 $$(c, d)$$ 사이의 유클리드 거리이다 ([\[해석학\] §거리공간, ⁋예시 2](/ko/math/analysis/metric_spaces#ex2)). 수렴의 동치성은 좌표별 부등식

$$\lvert a_n - a\rvert,\ \lvert b_n - b\rvert \;\leq\; \sqrt{(a_n - a)^2 + (b_n - b)^2} \;\leq\; \lvert a_n - a\rvert + \lvert b_n - b\rvert$$

에서 따라 나온다. 가운데 항이 $$d(z_n, z)$$이므로, 이것이 $$0$$으로 가는 것은 양 끝의 두 실수열 $$\lvert a_n - a\rvert$$, $$\lvert b_n - b\rvert$$이 모두 $$0$$으로 가는 것, 곧 $$a_n \to a$$이고 $$b_n \to b$$인 것과 동치이다.

</details>

명제 9는 복소수의 수렴이 실수부와 허수부의 동시 수렴으로 환원됨을 말하며, 이로써 $$\mathbb{C}$$ 위의 해석학을 $$\mathbb{R}^2$$ 위의 해석학으로 번역할 수 있게 된다. 가장 먼저 옮겨 오는 것은 완비성이다.

<div class="proposition" markdown="1">

<ins id="thm10">**정리 10**</ins> $$(\mathbb{C}, d)$$는 완비 거리공간이다. 곧 $$\mathbb{C}$$의 모든 Cauchy 점열은 $$\mathbb{C}$$의 한 점으로 수렴한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$z_n = a_n + b_n i$$가 $$\mathbb{C}$$에서 Cauchy라 하자. 좌표별 부등식 $$\lvert a_m - a_n\rvert \leq \lvert z_m - z_n\rvert$$과 $$\lvert b_m - b_n\rvert \leq \lvert z_m - z_n\rvert$$에 의해 두 실수열 $$(a_n)$$, $$(b_n)$$도 각각 Cauchy이다. 실수의 완비성 ([\[해석학\] §Cauchy 수열과 완비성, ⁋정리 4](/ko/math/analysis/cauchy_sequences#thm4))에 의해 $$a_n \to a$$, $$b_n \to b$$인 실수 $$a, b$$가 존재한다. 그러면 명제 9에 의해 $$z_n \to a + bi \in \mathbb{C}$$이다. 따라서 임의의 Cauchy 점열이 $$\mathbb{C}$$ 안에서 수렴하므로 $$(\mathbb{C}, d)$$는 완비이다.

</details>

이는 $$\mathbb{R}^2$$가 완비라는 사실 ([\[해석학\] §거리공간](/ko/math/analysis/metric_spaces)에서 좌표별 논증으로 언급된 것) 의 한 표현이기도 하다. 완비성은 멱급수의 수렴, 적분의 존재, 부동점 논증 등 복소해석학의 거의 모든 존재 정리가 의지하는 토대이다. 컴팩트성 또한 같은 동일시를 통해 그대로 따라 나온다.

<div class="proposition" markdown="1">

<ins id="thm11">**정리 11 (ℂ의 Bolzano–Weierstrass / Heine–Borel)**</ins> $$\mathbb{C}$$의 부분집합 $$K$$가 점렬컴팩트인 것은 $$K$$가 닫혀 있고 유계인 것과 동치이다. 특히 $$\mathbb{C}$$의 임의의 유계 점열은 수렴하는 부분수열을 가진다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

명제 9에 의해 $$(\mathbb{C}, d)$$는 거리공간으로서 $$(\mathbb{R}^2, d_{\text{euc}})$$와 동일하며, 닫힘·유계·점렬컴팩트는 모두 거리만으로 정의되는 개념이므로 두 공간에서 일치한다. 따라서 $$\mathbb{R}^2$$에 대한 Heine–Borel 정리 ([\[해석학\] §컴팩트성, ⁋정리 2](/ko/math/analysis/compactness#thm2))를 그대로 옮기면 결론을 얻는다.

뒷부분은 다음과 같이도 직접 볼 수 있다. $$(z_n)$$이 유계, 곧 모든 $$n$$에서 $$\lvert z_n\rvert \leq M$$이라 하자. $$z_n = a_n + b_n i$$로 적으면 $$\lvert a_n\rvert, \lvert b_n\rvert \leq \lvert z_n\rvert \leq M$$이므로 두 실수열이 유계이다. 먼저 $$(a_n)$$에 Bolzano–Weierstrass 정리 ([\[해석학\] §부분수열과 Bolzano–Weierstrass 정리, ⁋정리 4](/ko/math/analysis/bolzano_weierstrass#thm4))를 적용하여 $$a_{n_k} \to a$$인 부분수열을 뽑고, 그 부분수열 위에서 $$(b_{n_k})$$가 여전히 유계이므로 다시 Bolzano–Weierstrass를 적용하여 $$b_{n_{k_j}} \to b$$인 부분수열을 뽑는다. 이 부분수열 위에서 두 좌표가 동시에 수렴하므로 명제 9에 의해 $$z_{n_{k_j}} \to a + bi$$이다.

</details>

따라서 닫힌 원판 $$\overline{B}(z_0, R) = \{z \in \mathbb{C} \mid \lvert z - z_0\rvert \leq R\}$$이나 원 $$\{z \mid \lvert z\rvert = 1\}$$ 같은 집합은 컴팩트이고, 반면 열린 원판이나 $$\mathbb{C}$$ 전체는 컴팩트가 아니다. 이 컴팩트성은 곧 연속함수가 컴팩트집합 위에서 최댓값을 가진다는 결과로 이어져, 최대절댓값원리나 Liouville 정리 같은 복소해석학의 정리들이 서는 발판이 된다.

<div class="example" markdown="1">

<ins id="ex12">**예시 12 (등비점열의 수렴과 발산)**</ins> 복소수 $$z$$에 대해 점열 $$(z^n)$$의 거동은 절댓값 $$\lvert z\rvert$$로 완전히 결정된다. 명제 4에 의해 $$\lvert z^n\rvert = \lvert z\rvert^n$$이므로, $$\lvert z\rvert < 1$$이면

$$\lvert z^n - 0\rvert = \lvert z\rvert^n \to 0$$

이어서 $$z^n \to 0$$이다 ([\[해석학\] §수열의 수렴, ⁋예시 10](/ko/math/analysis/convergence_of_sequences#ex10)에서 본 실수열 $$\lvert z\rvert^n$$의 수렴). 반대로 $$\lvert z\rvert > 1$$이면 $$\lvert z^n\rvert \to \infty$$이므로 $$(z^n)$$은 유계가 아니어서 수렴하지 않는다. $$\lvert z\rvert = 1$$인 경계의 경우는 더 섬세하다. $$z = 1$$이면 $$z^n = 1$$로 일정하지만, 가령 $$z = i$$이면 $$z^n$$이 $$i, -1, -i, 1$$을 주기적으로 순환하여 ($$\lvert z^n\rvert = 1$$로 유계이지만) 수렴하지 않는다. 후자는 정리 11이 보장하는 수렴 부분수열의 존재를 명시적으로 보여 주는 예이기도 하다. 점열 $$(i^n)$$은 네 개의 상수 부분수열로 쪼개지며, 각각은 $$i, -1, -i, 1$$로 수렴한다.

</div>

## 확장복소평면과 Riemann 구면

복소해석학에서는 함수가 무한대로 발산하는 양상을 한 점 $$\infty$$를 덧붙여 다루는 것이 편리하다. 이렇게 얻는 *확장복소평면*은 평면에 점 하나를 더한 집합에 그치지 않고, 입체사영을 통해 구면이라는 컴팩트한 기하적 대상과 동일시된다.

<div class="definition" markdown="1">

<ins id="def13">**정의 13**</ins> 복소평면에 형식적 기호 $$\infty$$를 하나 덧붙인 집합 $$\widehat{\mathbb{C}} = \mathbb{C} \cup \{\infty\}$$을 *확장복소평면<sub>extended complex plane</sub>* 혹은 *Riemann 구면<sub>Riemann sphere</sub>*이라 한다.

</div>

$$\widehat{\mathbb{C}}$$를 구면과 동일시하기 위해, 단위구면 $$S^2 = \{(x_1, x_2, x_3) \in \mathbb{R}^3 \mid x_1^2 + x_2^2 + x_3^2 = 1\}$$과 그 위의 북극 $$N = (0, 0, 1)$$을 생각한다. 복소평면을 $$\mathbb{R}^3$$의 평면 $$\{x_3 = 0\}$$에 놓고, 점 $$z = x + yi$$를 $$(x, y, 0)$$과 동일시한다. *입체사영<sub>stereographic projection</sub>*은 북극 $$N$$과 평면 위의 점 $$z$$를 잇는 직선이 구면과 다시 만나는 점을 $$z$$에 대응시키는 사상이다. 직선 $$N + t\,(z - N)$$이 $$S^2$$와 만나는 조건을 풀면, $$z = x + yi$$에 대응하는 구면 위의 점은

$$\sigma(z) = \left( \frac{2x}{\lvert z\rvert^2 + 1},\ \frac{2y}{\lvert z\rvert^2 + 1},\ \frac{\lvert z\rvert^2 - 1}{\lvert z\rvert^2 + 1} \right)$$

이다. 이 대응은 평면 전체를 북극을 뺀 구면 $$S^2 \setminus \{N\}$$ 위로 일대일로 보내며, $$\lvert z\rvert \to \infty$$일 때 $$\sigma(z) \to N$$이므로 $$\infty$$를 북극 $$N$$에 대응시키면 $$\widehat{\mathbb{C}}$$ 전체가 구면 $$S^2$$와 일대일로 대응한다.

구면과의 동일시는 $$\widehat{\mathbb{C}}$$에 자연스러운 거리를 부여한다. 구면 위 두 점 사이의 $$\mathbb{R}^3$$에서의 직선거리(현의 길이)를 평면으로 끌어내린 것이 *현거리<sub>chordal metric</sub>*이다.

<div class="definition" markdown="1">

<ins id="def14">**정의 14**</ins> $$\widehat{\mathbb{C}}$$ 위의 *현거리<sub>chordal metric</sub>* $$\chi$$를, $$z, w \in \mathbb{C}$$에 대하여

$$\chi(z, w) = \frac{2\,\lvert z - w\rvert}{\sqrt{1 + \lvert z\rvert^2}\,\sqrt{1 + \lvert w\rvert^2}}, \qquad \chi(z, \infty) = \frac{2}{\sqrt{1 + \lvert z\rvert^2}}$$

로 정의한다.

</div>

이 $$\chi(z, w)$$는 정확히 구면 위의 두 점 $$\sigma(z)$$, $$\sigma(w)$$ 사이의 $$\mathbb{R}^3$$ 직선거리 $$\lVert \sigma(z) - \sigma(w)\rVert$$와 같으며, $$\chi(z, \infty)$$는 $$\sigma(z)$$와 북극 $$N$$ 사이의 직선거리이다. 따라서 $$(\widehat{\mathbb{C}}, \chi)$$는 $$\mathbb{R}^3$$의 부분공간 $$S^2$$를 그 유클리드 거리로 잰 거리공간과 등거리동형이며, 거리공간 공리는 $$S^2 \subseteq \mathbb{R}^3$$의 것을 물려받아 자동으로 성립한다. 두 거리 사이의 관계는 다음 명제로 정리된다.

<div class="proposition" markdown="1">

<ins id="prop15">**명제 15**</ins> 현거리 $$\chi$$는 $$\mathbb{C}$$ 위에서 표준거리 $$d(z, w) = \lvert z - w\rvert$$와 같은 위상을 준다. 곧 $$\mathbb{C}$$의 점열 $$(z_n)$$과 $$z \in \mathbb{C}$$에 대해 $$\chi(z_n, z) \to 0$$인 것은 $$\lvert z_n - z\rvert \to 0$$인 것과 동치이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$z \in \mathbb{C}$$를 고정하고 $$z_n \to z$$ (표준거리) 라 하자. 그러면 $$(z_n)$$은 유계이므로 어떤 $$M$$에 대해 $$\lvert z_n\rvert \leq M$$이고,

$$\chi(z_n, z) = \frac{2\,\lvert z_n - z\rvert}{\sqrt{1 + \lvert z_n\rvert^2}\,\sqrt{1 + \lvert z\rvert^2}} \leq \frac{2\,\lvert z_n - z\rvert}{\sqrt{1 + \lvert z\rvert^2}} \to 0$$

이다. 분모는 $$\sqrt{1 + \lvert z\rvert^2} \geq 1$$로 아래로 유계이고 분자가 $$0$$으로 가기 때문이다. 역으로 $$\chi(z_n, z) \to 0$$이라 하자. 분모는 모든 $$n$$에서

$$\sqrt{1 + \lvert z_n\rvert^2}\,\sqrt{1 + \lvert z\rvert^2}$$

인데, 만일 $$(z_n)$$이 유계가 아니라면 어떤 부분수열에서 $$\lvert z_n\rvert \to \infty$$이고, 그때 $$\chi(z_n, z) \to \chi(\infty, z) = 2/\sqrt{1 + \lvert z\rvert^2} > 0$$이 되어 $$\chi(z_n, z) \to 0$$에 모순이다. 따라서 $$(z_n)$$은 유계이고 $$\lvert z_n\rvert \leq M$$이라 두면

$$\lvert z_n - z\rvert = \frac{\sqrt{1 + \lvert z_n\rvert^2}\,\sqrt{1 + \lvert z\rvert^2}}{2}\,\chi(z_n, z) \leq \frac{\sqrt{1 + M^2}\,\sqrt{1 + \lvert z\rvert^2}}{2}\,\chi(z_n, z) \to 0$$

이다. 따라서 두 거리는 $$\mathbb{C}$$ 위에서 같은 수렴을 정의하며, 같은 위상을 준다.

</details>

명제 15는 $$\widehat{\mathbb{C}}$$가 $$\mathbb{C}$$를 위상적으로 변형 없이 품으면서 무한대에 한 점을 더해 컴팩트하게 만든 공간임을 말한다. 실제로 $$\widehat{\mathbb{C}}$$는 구면 $$S^2$$와 등거리동형이고 $$S^2$$는 $$\mathbb{R}^3$$의 닫힌 유계집합이므로, Heine–Borel 정리에 의해 $$(\widehat{\mathbb{C}}, \chi)$$는 컴팩트한 거리공간이다. 컴팩트하지 않은 $$\mathbb{C}$$에 점 하나를 더해 컴팩트한 공간을 얻는 이 구성은 위상수학의 *한 점 컴팩트화<sub>one-point compactification</sub>*의 가장 중요한 예이며, 무한대에서의 함수의 거동을 유한한 점에서의 거동과 동등하게 다룰 수 있게 해 준다. 유리형함수를 $$\widehat{\mathbb{C}}$$ 사이의 사상으로 보는 관점이 여기서 출발한다.

---

**참고문헌**

**[Ahl]** L.V. Ahlfors, *Complex analysis*, 3rd ed., McGraw–Hill, 1979.

**[Con]** J.B. Conway, *Functions of one complex variable I*, 2nd ed., Graduate Texts in Mathematics 11, Springer, 1978.

**[SS]** E.M. Stein, R. Shakarchi, *Complex analysis*, Princeton Lectures in Analysis II, Princeton University Press, 2003.
