---
title: "정칙함수"
description: "복소미분가능성을 한 변수 차분비의 극한으로 정의하고, 영역에서 복소미분가능한 정칙함수를 도입한다. Cauchy–Riemann 방정식과 Wirtinger 미분으로 실미분가능성과의 관계를 밝히고, 멱급수·지수·삼각함수의 정칙성과 실수부·허수부가 이루는 조화함수를 다룬다."
excerpt: "복소미분가능성, 정칙함수, Cauchy–Riemann 방정식, Wirtinger 미분, 멱급수, 조화함수"

categories: [Math / Complex Analysis]
permalink: /ko/math/complex_analysis/holomorphic_functions
sidebar: 
    nav: "complex_analysis-ko"

date: 2026-06-21
weight: 2

published: false
---

복소평면을 거리공간으로 정비하고 ([§복소수와 복소평면](/ko/math/complex_analysis/complex_numbers)) 나면, 그 위에서 정의된 함수의 미분을 물을 수 있다. 형식상 복소미분의 정의는 실함수의 미분과 똑같이 차분비 $$(f(z_0+h)-f(z_0))/h$$의 극한이지만, 이번에는 증분 $$h$$가 복소수여서 평면의 모든 방향에서 같은 극한을 강요한다. 이 한 줄의 조건이 실함수에는 없는 엄청난 경직성을 낳아, 한 번 복소미분가능한 함수가 무한히 미분가능하고 멱급수로 전개되며 그 실수부와 허수부가 조화방정식을 만족하는 등 풍부한 구조가 따라 나온다. 이 글에서는 복소미분가능성과 *정칙성*을 정의하고, 그것이 실미분가능성과 어떻게 다른지를 Cauchy–Riemann 방정식으로 정확히 잡아낸다.

함수의 정의역으로는 항상 $$\mathbb{C}$$의 *영역<sub>domain</sub>*, 곧 공집합이 아닌 열린 연결집합 $$\Omega \subseteq \mathbb{C}$$를 택한다. 영역에서 함수를 다루는 까닭은, 미분이 본질적으로 한 점 근방의 정보를 요구하므로 정의역이 열려 있어야 하고, 연결성은 뒤에서 보듯 "도함수가 $$0$$이면 상수" 같은 전역적 결론을 가능하게 하기 때문이다.

## 복소미분가능성과 정칙성

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 열린집합 $$\Omega \subseteq \mathbb{C}$$ 위의 함수 $$f : \Omega \to \mathbb{C}$$와 점 $$z_0 \in \Omega$$에 대하여, 극한

$$f'(z_0) = \lim_{h \to 0} \frac{f(z_0 + h) - f(z_0)}{h}$$

이 존재하면 $$f$$가 $$z_0$$에서 *복소미분가능<sub>complex differentiable</sub>*하다고 하고, 그 극한값 $$f'(z_0)$$을 $$z_0$$에서의 *도함수<sub>derivative</sub>*라 한다. 여기서 $$h$$는 $$0$$이 아닌 복소수이며 $$z_0 + h \in \Omega$$인 범위에서 $$0$$으로 보낸다.

</div>

극한 $$h \to 0$$은 복소평면 위에서의 극한, 곧 $$\lvert h\rvert \to 0$$이므로 $$h$$가 $$0$$에 다가가는 *방향*에 무관하게 같은 값을 주어야 한다는 강한 요구이다. 실수축을 따라 $$h \to 0$$으로 보내든, 허수축을 따라 보내든, 혹은 나선을 그리며 보내든 차분비가 모두 같은 극한 $$f'(z_0)$$으로 수렴해야 한다. 실함수의 한쪽·양쪽 미분과 달리 평면에는 다가가는 길이 무수히 많으므로, 이 일치 요구가 곧 아래 Cauchy–Riemann 방정식이라는 구속으로 번역된다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 함수 $$f : \Omega \to \mathbb{C}$$가 영역 $$\Omega$$의 *모든* 점에서 복소미분가능하면, $$f$$를 $$\Omega$$ 위의 *holomorphic function<sub>정칙함수</sub>*이라 한다. $$\mathbb{C}$$ 전체에서 정칙인 함수는 *entire function<sub>전해석함수</sub>*이라 부른다.

</div>

"정칙"이라는 말은 한 점이 아니라 열린집합 전체에서의 복소미분가능성을 가리킨다는 점이 핵심이다. 한 점에서만 복소미분가능한 것은 그 점의 임의의 작은 근방으로 확장되지 않을 수 있어 약한 성질이지만, 열린 근방 전체에서 복소미분가능하다는 조건은 앞서 말한 풍부한 구조 전부를 끌어낸다. 도함수가 다시 $$\Omega$$ 위의 함수 $$f' : \Omega \to \mathbb{C}$$를 정의하므로, $$f'$$ 자신이 또 정칙인지를 물을 수 있고 실제로 그러한데, 그 깊은 사실은 적분 이론에서 따로 다룬다. 우선 정의로부터 곧바로 따라 나오는 미분 규칙들을 정리한다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> $$f, g$$가 $$z_0$$에서 복소미분가능하면 $$f + g$$, $$fg$$도 그러하며

$$(f + g)'(z_0) = f'(z_0) + g'(z_0), \qquad (fg)'(z_0) = f'(z_0)g(z_0) + f(z_0)g'(z_0)$$

이다. $$g(z_0) \neq 0$$이면 $$f/g$$도 $$z_0$$에서 복소미분가능하고

$$\left(\frac{f}{g}\right)'(z_0) = \frac{f'(z_0)g(z_0) - f(z_0)g'(z_0)}{g(z_0)^2}$$

이다. 또 $$f$$가 $$z_0$$에서, $$g$$가 $$f(z_0)$$에서 복소미분가능하면 $$g \circ f$$가 $$z_0$$에서 복소미분가능하고 $$(g \circ f)'(z_0) = g'(f(z_0))\,f'(z_0)$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

차분비의 극한이 가지는 대수적 성질은 실함수에서와 글자 그대로 같으며, 복소수의 사칙연산과 극한이 어울린다는 사실에만 의존한다. 합에 대하여는 차분비가

$$\frac{(f+g)(z_0+h) - (f+g)(z_0)}{h} = \frac{f(z_0+h)-f(z_0)}{h} + \frac{g(z_0+h)-g(z_0)}{h}$$

이므로 두 극한의 합으로 $$f'(z_0) + g'(z_0)$$이 된다. 곱에 대하여는

$$\frac{f(z_0+h)g(z_0+h) - f(z_0)g(z_0)}{h} = \frac{f(z_0+h)-f(z_0)}{h}\,g(z_0+h) + f(z_0)\,\frac{g(z_0+h)-g(z_0)}{h}$$

으로 쪼개고, $$g$$가 $$z_0$$에서 복소미분가능하면 연속이므로 $$h \to 0$$일 때 $$g(z_0+h) \to g(z_0)$$임을 쓰면 우변이 $$f'(z_0)g(z_0) + f(z_0)g'(z_0)$$으로 수렴한다. 몫의 경우 먼저 $$g(z_0)\neq 0$$이고 $$g$$가 연속이므로 $$z_0$$의 작은 근방에서 $$g$$가 $$0$$이 아니어서 $$f/g$$가 정의되며,

$$\frac{1}{h}\left(\frac{1}{g(z_0+h)} - \frac{1}{g(z_0)}\right) = -\frac{1}{g(z_0+h)g(z_0)}\cdot\frac{g(z_0+h)-g(z_0)}{h} \to -\frac{g'(z_0)}{g(z_0)^2}$$

이므로 $$(1/g)'(z_0) = -g'(z_0)/g(z_0)^2$$이고, 여기에 곱셈규칙을 적용하면 몫공식을 얻는다. 합성에 대하여는 $$w_0 = f(z_0)$$로 두고 보조함수

$$\psi(w) = \begin{cases} \dfrac{g(w) - g(w_0)}{w - w_0}, & w \neq w_0, \\[1mm] g'(w_0), & w = w_0 \end{cases}$$

를 생각하면 $$g$$의 복소미분가능성에서 $$\psi$$가 $$w_0$$에서 연속이고, 모든 $$w$$에 대해 $$g(w) - g(w_0) = \psi(w)(w - w_0)$$이다. 이를 $$w = f(z_0+h)$$에 적용하면

$$\frac{g(f(z_0+h)) - g(f(z_0))}{h} = \psi(f(z_0+h))\,\frac{f(z_0+h)-f(z_0)}{h}$$

이고, $$f$$의 연속성으로 $$f(z_0+h) \to w_0$$이므로 $$\psi(f(z_0+h)) \to \psi(w_0) = g'(w_0)$$이며 우변이 $$g'(f(z_0))f'(z_0)$$으로 수렴한다.

</details>

명제 3은 복소미분이 실미분과 동일한 형식 규칙을 따름을 말한다. 상수함수의 도함수가 $$0$$이고 항등함수 $$z \mapsto z$$의 도함수가 $$1$$임은 정의에서 즉시 나오므로, 곱셈규칙을 반복하면 $$z^n$$ ($$n \geq 0$$)의 도함수가 $$nz^{n-1}$$이고, 따라서 모든 다항식 $$p(z) = \sum_{k=0}^n a_k z^k$$이 전해석함수이며 $$p'(z) = \sum_{k=1}^n k a_k z^{k-1}$$이다. 몫공식에 의해 유리함수 $$p(z)/q(z)$$는 분모가 $$0$$이 되지 않는 영역에서 정칙이다. 반면 다음 예시가 보이듯, 평면 위의 매우 매끄러운 실함수조차 복소미분가능하지 않을 수 있다.

<div class="example" markdown="1">

<ins id="ex4">**예시 4 (켤레함수는 정칙이 아니다)**</ins> 함수 $$f(z) = \bar{z}$$를 생각하자. $$z_0$$에서의 차분비는

$$\frac{\overline{z_0 + h} - \overline{z_0}}{h} = \frac{\bar{h}}{h}$$

이다. $$h$$를 실수축을 따라 $$0$$으로 보내면 ($$h = t \in \mathbb{R}$$, $$t \to 0$$) $$\bar{h}/h = t/t = 1$$이지만, 허수축을 따라 보내면 ($$h = it$$, $$t \to 0$$) $$\bar{h}/h = -it/(it) = -1$$이다. 두 극한이 다르므로 $$\bar{h}/h$$는 $$h \to 0$$일 때 극한을 가지지 않는다. 따라서 $$f(z) = \bar{z}$$는 어느 점에서도 복소미분가능하지 않으며, 평면의 어디에서도 정칙이 아니다. 그럼에도 $$\bar{z} = x - iy$$는 실수부·허수부가 다항식이라 실함수로서는 매끄럽다. 복소미분가능성이 실미분가능성보다 훨씬 강한 조건임을 단적으로 보여 주는 예이다.

</div>

## Cauchy–Riemann 방정식

예시 4는 복소미분가능성이 차분비의 방향 독립성을 요구하며, 이것이 실수부와 허수부 사이의 관계로 번역됨을 시사한다. 이 관계를 정확히 적은 것이 Cauchy–Riemann 방정식이다. 함수 $$f : \Omega \to \mathbb{C}$$를 실수부와 허수부로 갈라 $$f(z) = u(x, y) + i\,v(x, y)$$ ($$z = x + iy$$) 로 적으면, $$f$$는 두 실숫값 함수 $$u, v : \Omega \to \mathbb{R}$$의 쌍, 곧 평면사상 $$(x, y) \mapsto (u, v)$$로 볼 수 있다. 이때 $$f$$의 복소미분가능성은 그 평면사상의 실미분가능성 ([\[해석학\] §다변수 미분, ⁋정의 1](/ko/math/analysis/multivariable_differentiation#def1)) 에 한 쌍의 편미분 등식을 더한 것과 정확히 동치이다.

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5 (Cauchy–Riemann 방정식)**</ins> $$\Omega \subseteq \mathbb{C}$$가 열려 있고 $$f = u + iv : \Omega \to \mathbb{C}$$이며 $$z_0 = x_0 + iy_0 \in \Omega$$이라 하자. 그러면 $$f$$가 $$z_0$$에서 복소미분가능한 것은 $$u, v$$가 $$(x_0, y_0)$$에서 ($$\mathbb{R}^2$$의 함수로서) 실미분가능하고 그곳에서

$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}, \qquad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$$

가 성립하는 것과 동치이다. 이때 도함수는

$$f'(z_0) = \frac{\partial u}{\partial x}(x_0, y_0) + i\,\frac{\partial v}{\partial x}(x_0, y_0)$$

으로 주어진다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

먼저 $$f$$가 $$z_0$$에서 복소미분가능하고 $$f'(z_0) = a + ib$$라 하자. 정의 1의 극한에서

$$f(z_0 + h) - f(z_0) = f'(z_0)\,h + r(h), \qquad \frac{r(h)}{h} \to 0 \;\;(h \to 0)$$

이며, $$\lvert r(h)\rvert/\lvert h\rvert = \lvert r(h)/h\rvert \to 0$$이므로 $$r(h) = o(\lvert h\rvert)$$이다. $$h = s + it$$로 적고 복소수 곱 $$f'(z_0)h = (a+ib)(s+it) = (as - bt) + i(bs + at)$$을 실허로 나누면

$$\begin{aligned}
u(x_0+s, y_0+t) - u(x_0, y_0) &= as - bt + \Real r(h), \\
v(x_0+s, y_0+t) - v(x_0, y_0) &= bs + at + \Img r(h)
\end{aligned}$$

이 된다. $$\Real r, \Img r$$도 각각 $$o(\lvert h\rvert) = o(\lVert(s,t)\rVert)$$이므로, 이는 $$u, v$$가 $$(x_0,y_0)$$에서 실미분가능하고 그 야코비 행렬이

$$\begin{pmatrix} u_x & u_y \\ v_x & v_y \end{pmatrix} = \begin{pmatrix} a & -b \\ b & a \end{pmatrix}$$

임을 뜻한다. 여기서 곧바로 $$u_x = a = v_y$$, $$u_y = -b = -v_x$$, 곧 Cauchy–Riemann 방정식을 읽으며, $$f'(z_0) = a + ib = u_x + i v_x$$이다.

역으로 $$u, v$$가 $$(x_0, y_0)$$에서 실미분가능하고 그곳에서 $$u_x = v_y$$, $$u_y = -v_x$$라 하자. $$a = u_x$$, $$b = v_x$$로 두면 $$v_y = a$$, $$u_y = -b$$이므로 위 야코비 행렬이 다시 $$\left(\begin{smallmatrix} a & -b \\ b & a \end{smallmatrix}\right)$$ 꼴이다. 실미분가능성을 실허 두 성분으로 묶어 $$h = s + it$$로 쓰면

$$\begin{aligned}
f(z_0 + h) - f(z_0)
&= (as - bt) + i(bs + at) + \rho(h) \\
&= (a + ib)(s + it) + \rho(h) = (a+ib)\,h + \rho(h)
\end{aligned}$$

이고 $$\rho(h) = o(\lVert(s,t)\rVert) = o(\lvert h\rvert)$$이다. 따라서

$$\frac{f(z_0 + h) - f(z_0)}{h} = (a + ib) + \frac{\rho(h)}{h}$$

인데 $$\lvert \rho(h)/h\rvert = \lvert\rho(h)\rvert/\lvert h\rvert \to 0$$이므로 차분비가 $$a + ib$$로 수렴한다. 그러므로 $$f$$는 $$z_0$$에서 복소미분가능하고 $$f'(z_0) = a + ib = u_x + i v_x$$이다.

</details>

정리 5의 증명이 드러내는 핵심은, 복소미분가능성이 곧 평면사상 $$(u, v)$$의 미분이 *복소수 곱*의 꼴, 곧 $$\left(\begin{smallmatrix} a & -b \\ b & a \end{smallmatrix}\right)$$ 행렬이어야 한다는 조건이라는 점이다. 이 형태의 행렬은 정확히 평면의 회전·확대를 합성한 것 ([§복소수와 복소평면, ⁋명제 6](/ko/math/complex_analysis/complex_numbers#prop6)) 이므로, 복소미분가능한 함수의 미분은 한 점에서 평면을 회전·확대하는 *각도를 보존하는* 선형사상이다. 일반적인 실미분은 임의의 $$2\times 2$$ 행렬을 야코비로 가질 수 있는 데 반해, 복소미분가능성은 그 야코비를 한 복소수로 표현되는 닮음변환으로 제한한다. 이것이 복소미분의 경직성의 근원이며, 정칙함수가 등각사상이 되는 기하적 사실의 대수적 핵심이다.

한편 실미분가능성을 직접 확인하기 번거로울 때를 위해, 편미분의 연속성을 가정하면 Cauchy–Riemann 방정식만으로 정칙성을 판정할 수 있다. 이는 연속인 편미분이 실미분가능성을 보장한다는 사실 ([\[해석학\] §다변수 미분, ⁋명제 4](/ko/math/analysis/multivariable_differentiation#prop4)) 의 직접적 귀결이다.

<div class="proposition" markdown="1">

<ins id="cor6">**따름정리 6**</ins> $$\Omega \subseteq \mathbb{C}$$가 열려 있고 $$f = u + iv : \Omega \to \mathbb{C}$$의 네 편미분 $$u_x, u_y, v_x, v_y$$이 $$\Omega$$에서 모두 존재하고 연속이라 하자. 그러면 $$f$$가 $$\Omega$$에서 정칙인 것은 $$\Omega$$의 모든 점에서 Cauchy–Riemann 방정식 $$u_x = v_y$$, $$u_y = -v_x$$가 성립하는 것과 동치이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

편미분이 연속이면 $$u, v$$가 각 점에서 실미분가능하다 ([\[해석학\] §다변수 미분, ⁋명제 4](/ko/math/analysis/multivariable_differentiation#prop4)). 따라서 실미분가능성은 가정에서 자동으로 충족되고, 정리 5의 동치성에서 복소미분가능성은 각 점에서 Cauchy–Riemann 방정식과 동치로 환원된다. 이것이 $$\Omega$$의 모든 점에서 성립하는 것이 곧 $$f$$가 $$\Omega$$에서 정칙이라는 것이다.

</details>

따름정리 6은 실제 계산에서 정칙성을 확인하는 가장 흔한 도구이다. 가령 다항식이나 $$e^x(\cos y + i\sin y)$$처럼 성분이 매끄러운 함수에 대해서는 편미분의 연속성이 자동이므로, Cauchy–Riemann 두 등식만 점검하면 된다. 이 판정을 더 간결하게 적는 표기가 다음 절의 Wirtinger 미분이다.

## Wirtinger 미분

Cauchy–Riemann 방정식의 두 등식은 적절한 미분연산자를 도입하면 단 하나의 등식으로 압축된다. 발상은 함수를 실변수 $$x, y$$가 아니라 형식적으로 $$z = x + iy$$와 $$\bar{z} = x - iy$$의 함수로 보고, 이 두 변수에 대한 미분을 정의하는 것이다.

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> $$\Omega \subseteq \mathbb{C}$$에서 실미분가능한 함수 $$f$$에 대하여 *Wirtinger 미분<sub>Wirtinger derivative</sub>*을

$$\frac{\partial f}{\partial z} = \frac{1}{2}\left(\frac{\partial f}{\partial x} - i\,\frac{\partial f}{\partial y}\right), \qquad \frac{\partial f}{\partial \bar{z}} = \frac{1}{2}\left(\frac{\partial f}{\partial x} + i\,\frac{\partial f}{\partial y}\right)$$

으로 정의하고, 각각 $$\partial_z f$$, $$\partial_{\bar{z}} f$$로도 적는다. 여기서 $$\partial_x f$$, $$\partial_y f$$는 $$f$$를 두 실변수 $$x, y$$의 (복소숫값) 함수로 본 편미분이다.

</div>

이 정의는 $$\partial_z$$가 $$z = x + iy$$, $$\partial_{\bar{z}}$$가 $$\bar{z} = x - iy$$에 대한 "도함수"처럼 행동하도록 고안된 것이다. 실제로 형식적으로 $$x = (z + \bar{z})/2$$, $$y = (z - \bar{z})/(2i)$$로 두고 연쇄법칙을 적용하면 위 두 연산자가 나온다. 표기의 정당성은 다음 항등식들로 확인되는데, $$\partial_z z = 1$$, $$\partial_z \bar{z} = 0$$, $$\partial_{\bar{z}} z = 0$$, $$\partial_{\bar{z}} \bar{z} = 1$$이 성립한다. 가령 $$z = x + iy$$에 대해 $$\partial_{\bar z} z = \tfrac12(\partial_x + i\partial_y)(x + iy) = \tfrac12(1 + i\cdot i) = 0$$이다. 이 표기로 Cauchy–Riemann 방정식은 단 하나의 등식이 된다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> $$f = u + iv$$가 $$z_0$$에서 실미분가능하다고 하자. 그러면 $$z_0$$에서 Cauchy–Riemann 방정식이 성립하는 것은

$$\frac{\partial f}{\partial \bar{z}}(z_0) = 0$$

인 것과 동치이며, 이때 $$f'(z_0) = \dfrac{\partial f}{\partial z}(z_0)$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$f = u + iv$$의 편미분을 직접 대입하면

$$\frac{\partial f}{\partial \bar{z}} = \frac{1}{2}\left( (u_x + i v_x) + i(u_y + i v_y) \right) = \frac{1}{2}\bigl( (u_x - v_y) + i(v_x + u_y) \bigr)$$

이다. 이 복소수가 $$0$$인 것은 실부와 허부가 모두 $$0$$인 것, 곧 $$u_x - v_y = 0$$이고 $$v_x + u_y = 0$$인 것과 동치인데, 이는 정확히 $$u_x = v_y$$, $$u_y = -v_x$$, 곧 Cauchy–Riemann 방정식이다. 한편

$$\frac{\partial f}{\partial z} = \frac{1}{2}\left( (u_x + i v_x) - i(u_y + i v_y) \right) = \frac{1}{2}\bigl( (u_x + v_y) + i(v_x - u_y) \bigr)$$

인데, Cauchy–Riemann 방정식이 성립하면 $$v_y = u_x$$, $$u_y = -v_x$$이므로 우변이 $$\tfrac12(2u_x + i\,2v_x) = u_x + i v_x$$가 되어, 정리 5의 도함수 공식에 의해 $$f'(z_0) = u_x + i v_x = \partial_z f(z_0)$$이다.

</details>

명제 8은 정칙성을 "$$f$$가 $$\bar{z}$$에 의존하지 않는다"로 해석하게 해 준다. 형식적으로 $$\partial_{\bar z} f = 0$$은 $$f$$가 $$\bar{z}$$에 무관하게 $$z$$만의 함수임을 뜻하며, 정칙함수가 곧 "$$z$$만의 함수"라는 직관을 정당화한다. 이 관점에서 예시 4의 $$f(z) = \bar{z}$$는 $$\partial_{\bar z}\bar z = 1 \neq 0$$이라 어디에서도 정칙이 아님이 즉시 보인다. 또 정칙함수의 도함수가 $$\partial_z f$$로 주어지므로, 실무에서는 $$f$$를 $$z$$로 적고 평범하게 미분하면 도함수가 나온다. 가령 $$f(z) = z^2$$이면 $$\partial_z f = 2z$$, $$\partial_{\bar z} f = 0$$이다.

## 멱급수와 초등함수

다항식 다음으로 자연스러운 정칙함수의 공급원은 수렴하는 멱급수이다. 멱급수는 수렴원판 안에서 정칙일 뿐 아니라 항별로 미분되며, 이로써 지수함수와 삼각함수를 복소변수로 확장하고 그 정칙성과 도함수를 한꺼번에 얻는다.

<div class="proposition" markdown="1">

<ins id="thm9">**정리 9 (멱급수의 정칙성과 항별미분)**</ins> 멱급수 $$\sum_{n=0}^{\infty} a_n (z - z_0)^n$$의 수렴반지름이 $$R > 0$$이라 하자. 그러면 이 급수가 정의하는 함수

$$f(z) = \sum_{n=0}^{\infty} a_n (z - z_0)^n$$

은 열린 원판 $$B(z_0, R) = \{z \mid \lvert z - z_0\rvert < R\}$$에서 정칙이고, 그 도함수는 항별미분으로 얻어지는 급수

$$f'(z) = \sum_{n=1}^{\infty} n\,a_n (z - z_0)^{n-1}$$

로 주어진다. 이 항별미분 급수도 수렴반지름이 $$R$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

평행이동으로 $$z_0 = 0$$이라 두어도 일반성을 잃지 않는다. 먼저 항별미분 급수 $$g(z) = \sum_{n\geq 1} n a_n z^{n-1}$$의 수렴반지름을 본다. $$\limsup_n \lvert n a_n\rvert^{1/n} = \limsup_n \lvert a_n\rvert^{1/n}$$인데 이는 $$\sqrt[n]{n} \to 1$$이기 때문이며 ([\[해석학\] §수열의 수렴, ⁋예시 12](/ko/math/analysis/convergence_of_sequences#ex12)에서 본 $$\sqrt[n]{n} \to 1$$), Cauchy–Hadamard 공식 ([\[해석학\] §멱급수와 해석함수, ⁋정리 1](/ko/math/analysis/power_series#thm1))에 의해 $$g$$의 수렴반지름도 $$R$$이다. 따라서 $$g$$는 $$B(0, R)$$에서 잘 정의된다.

이제 $$\lvert w\rvert < R$$을 고정하고 $$\lvert w\rvert < \rho < R$$인 $$\rho$$를 잡는다. $$\lvert z - w\rvert$$가 작아 $$\lvert z\rvert < \rho$$인 $$z \neq w$$에 대하여, 차분비에서 $$g(w)$$를 빼면

$$\frac{f(z) - f(w)}{z - w} - g(w) = \sum_{n=2}^{\infty} a_n \left( \frac{z^n - w^n}{z - w} - n w^{n-1} \right)$$

이다 ($$n = 0, 1$$ 항은 소거된다). 인수분해 $$\dfrac{z^n - w^n}{z - w} = \sum_{k=0}^{n-1} z^k w^{n-1-k}$$를 쓰면 괄호 안은

$$\sum_{k=0}^{n-1} \bigl( z^k - w^k \bigr) w^{n-1-k} = (z - w)\sum_{k=1}^{n-1} \left( \sum_{j=0}^{k-1} z^j w^{k-1-j} \right) w^{n-1-k}$$

이 되고, $$\lvert z\rvert, \lvert w\rvert < \rho$$이므로 가장 안쪽 합의 각 항의 크기가 $$\rho^{n-2}$$ 이하, 따라서 괄호 전체의 크기가 $$\lvert z - w\rvert \cdot \binom{n}{2}\rho^{n-2}$$ 이하이다. 그러므로

$$\left\lvert \frac{f(z) - f(w)}{z - w} - g(w) \right\rvert \leq \lvert z - w\rvert \sum_{n=2}^{\infty} \lvert a_n\rvert \binom{n}{2}\rho^{n-2}$$

인데, 우변의 급수 $$\sum_n \lvert a_n\rvert \binom{n}{2}\rho^{n-2}$$는 $$\rho < R$$에서 수렴한다 (두 번 항별미분한 급수의 절대수렴이며, 위와 같은 수렴반지름 논증을 반복하면 된다). 따라서 그 합을 상수 $$C$$라 하면 위 부등식의 우변은 $$C\lvert z - w\rvert \to 0$$이고, $$z \to w$$일 때 차분비가 $$g(w)$$로 수렴한다. 이는 $$f$$가 $$w$$에서 복소미분가능하고 $$f'(w) = g(w)$$임을 뜻한다. $$w$$가 임의였으므로 $$f$$는 $$B(0,R)$$에서 정칙이고 $$f' = g$$이다.

</details>

정리 9는 멱급수로 정의된 함수가 자동으로 정칙임을 보장한다. 이를 표준적인 급수들에 적용하면 복소 지수함수와 삼각함수를 정의하고 그 정칙성을 동시에 얻는다.

<div class="definition" markdown="1">

<ins id="def10">**정의 10**</ins> 복소수 $$z$$에 대하여 *지수함수<sub>exponential function</sub>*, *코사인<sub>cosine</sub>*, *사인<sub>sine</sub>*을 멱급수

$$e^z = \sum_{n=0}^{\infty} \frac{z^n}{n!}, \qquad \cos z = \sum_{n=0}^{\infty} \frac{(-1)^n z^{2n}}{(2n)!}, \qquad \sin z = \sum_{n=0}^{\infty} \frac{(-1)^n z^{2n+1}}{(2n+1)!}$$

으로 정의한다.

</div>

세 급수는 모두 수렴반지름이 $$\infty$$이다. 가령 $$e^z$$의 계수는 $$a_n = 1/n!$$이고 $$\lvert a_n\rvert^{1/n} = (n!)^{-1/n} \to 0$$이므로 수렴반지름이 $$\infty$$이며, 따라서 $$e^z$$는 전해석함수이다. 같은 이유로 $$\cos z$$, $$\sin z$$도 전해석함수이다. 정리 9의 항별미분을 적용하면 익숙한 도함수 공식이 그대로 따라 나온다. 곧

$$\frac{d}{dz}e^z = \sum_{n=1}^{\infty} \frac{n z^{n-1}}{n!} = \sum_{n=1}^{\infty} \frac{z^{n-1}}{(n-1)!} = e^z$$

이고, 마찬가지로 항별미분하면 $$\dfrac{d}{dz}\sin z = \cos z$$, $$\dfrac{d}{dz}\cos z = -\sin z$$이다. 또 급수를 직접 비교하면 모든 복소수 $$z$$에 대해 *Euler 공식<sub>Euler's formula</sub>*

$$e^{iz} = \cos z + i\sin z$$

가 성립하며, 이로써 ([§복소수와 복소평면, ⁋정의 5](/ko/math/complex_analysis/complex_numbers#def5))에서 표기상의 약속으로 받아들였던 $$e^{i\theta} = \cos\theta + i\sin\theta$$가 이제 정의된 함수들 사이의 진짜 등식으로 정당화된다. 특히 $$z = x + iy$$에 대해 덧셈정리 $$e^{z+w} = e^z e^w$$ (이는 두 멱급수의 Cauchy 곱으로 증명된다) 와 결합하면 $$e^z = e^x(\cos y + i\sin y)$$이고, 이 형태에 따름정리 6을 적용해도 정칙성과 도함수 $$e^z$$를 다시 확인할 수 있다.

## 조화함수

정칙함수의 실수부와 허수부는 단지 매끄러운 실함수가 아니라, 평면의 Laplace 방정식을 만족하는 조화함수라는 더 강한 구조를 가진다. 이 사실은 복소해석학과 평면의 퍼텐셜 이론을 잇는 다리가 된다. 이 절에서는 정칙함수가 두 번 복소미분가능하다는 사실, 곧 $$u, v$$가 $$C^2$$급이라는 사실을 받아들이고 출발한다. 이는 적분 이론에서 증명되는 정칙함수의 무한미분가능성의 한 귀결이다.

<div class="definition" markdown="1">

<ins id="def11">**정의 11**</ins> 열린집합 $$\Omega \subseteq \mathbb{R}^2$$ 위의 $$C^2$$급 실숫값 함수 $$u$$가 *조화함수<sub>harmonic function</sub>*라는 것은 $$\Omega$$에서 *Laplace 방정식*

$$\Delta u = \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0$$

을 만족하는 것이다. 여기서 $$\Delta = \partial_x^2 + \partial_y^2$$를 *Laplace 연산자<sub>Laplacian</sub>*라 한다.

</div>

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins> $$f = u + iv$$가 영역 $$\Omega$$에서 정칙이면, $$u = \Real f$$와 $$v = \Img f$$는 $$\Omega$$에서 조화함수이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$f$$가 정칙이면 $$u, v$$는 ($$C^2$$급이므로) Cauchy–Riemann 방정식 $$u_x = v_y$$, $$u_y = -v_x$$를 만족한다. 첫 등식을 $$x$$로, 둘째 등식을 $$y$$로 편미분하면

$$u_{xx} = v_{yx}, \qquad u_{yy} = -v_{xy}$$

이다. $$v$$가 $$C^2$$급이므로 혼합편미분이 순서에 무관하여 $$v_{yx} = v_{xy}$$이고 ([\[미적분학\] §다변수함수와 편미분, ⁋정리 8](/ko/math/calculus/partial_derivatives#thm8)의 클레로 정리), 따라서

$$\Delta u = u_{xx} + u_{yy} = v_{yx} - v_{xy} = 0$$

이다. $$v$$에 대해서도 같은 방식으로, $$u_y = -v_x$$를 $$x$$로, $$u_x = v_y$$를 $$y$$로 편미분하여 $$v_{xx} = -u_{yx}$$, $$v_{yy} = u_{xy}$$를 얻고 $$u_{yx} = u_{xy}$$를 쓰면 $$\Delta v = v_{xx} + v_{yy} = -u_{yx} + u_{xy} = 0$$이다. 따라서 $$u, v$$가 모두 조화이다.

</details>

명제 12에서 정칙함수 하나가 두 조화함수 $$u, v$$를 주며, 이 둘은 Cauchy–Riemann 방정식으로 묶여 있다. 이 관계에 이름을 붙인다.

<div class="definition" markdown="1">

<ins id="def13">**정의 13**</ins> 영역 $$\Omega$$ 위의 두 조화함수 $$u, v$$가 Cauchy–Riemann 방정식 $$u_x = v_y$$, $$u_y = -v_x$$를 만족하면, $$v$$를 $$u$$의 *harmonic conjugate<sub>조화켤레</sub>*라 한다.

</div>

조화켤레는 정의 13의 비대칭성이 시사하듯 $$u$$에서 $$v$$로의 일방적 관계이며, 실제로 $$v$$가 $$u$$의 조화켤레이면 $$-u$$가 $$v$$의 조화켤레가 된다 (Cauchy–Riemann 방정식의 두 등식을 $$(v, -u)$$에 대해 다시 쓰면 확인된다). 주어진 조화함수 $$u$$에 대해 그 조화켤레 $$v$$가 (적절한 영역에서) 존재하면, $$f = u + iv$$가 정칙함수가 되어 임의의 조화함수를 정칙함수의 실수부로 실현할 수 있다. 가장 단순한 예로 $$u(x, y) = x^2 - y^2$$를 보면 $$u_{xx} + u_{yy} = 2 - 2 = 0$$이라 조화이고, $$v(x, y) = 2xy$$가 $$v_y = 2x = u_x$$, $$v_x = 2y = -u_y$$로 조화켤레이며, 둘을 합치면 $$f(z) = (x^2 - y^2) + i\,2xy = z^2$$으로 정칙함수를 회복한다.

<div class="example" markdown="1">

<ins id="ex14">**예시 14 (지수함수의 실허부와 조화성)**</ins> 전해석함수 $$e^z = e^x(\cos y + i\sin y)$$의 실수부와 허수부는

$$u(x, y) = e^x \cos y, \qquad v(x, y) = e^x \sin y$$

이다. 명제 12에 의해 둘 다 조화여야 하는데, 직접 확인하면 $$u_{xx} = e^x\cos y$$, $$u_{yy} = -e^x\cos y$$이므로 $$\Delta u = 0$$이고, 같은 계산으로 $$\Delta v = 0$$이다. 또 $$u_x = e^x\cos y = v_y$$, $$u_y = -e^x\sin y = -v_x$$로 Cauchy–Riemann 방정식이 성립하여 $$v$$가 $$u$$의 조화켤레임을 본다. 도함수는 명제 8의 $$f' = \partial_z f = u_x + i v_x = e^x\cos y + i\,e^x\sin y = e^z$$로, 앞서 항별미분으로 얻은 $$(e^z)' = e^z$$와 일치한다.

</div>

---

**참고문헌**

**[Ahl]** L.V. Ahlfors, *Complex analysis*, 3rd ed., McGraw–Hill, 1979.

**[Con]** J.B. Conway, *Functions of one complex variable I*, 2nd ed., Graduate Texts in Mathematics 11, Springer, 1978.

**[SS]** E.M. Stein, R. Shakarchi, *Complex analysis*, Princeton Lectures in Analysis II, Princeton University Press, 2003.
</content>
</invoke>
