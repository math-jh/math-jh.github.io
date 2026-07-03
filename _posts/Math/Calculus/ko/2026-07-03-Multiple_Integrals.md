---
title: "다중적분"
description: "여러 변수 함수의 다중적분을 리만 합으로 일반적으로 정의하고, 반복적분으로 환원하는 푸비니 정리를 다룬다. 야코비 행렬식을 통한 변수변환과 극·원기둥·구면 좌표, 가우스 적분, 부피·질량 응용을 이중·삼중적분 계산 예시로 본다."
excerpt: "다중적분, 푸비니 정리, 변수변환과 야코비 행렬식"

categories: [Math / Calculus]
permalink: /ko/math/calculus/multiple_integrals
sidebar: 
    nav: "calculus-ko"

date: 2026-07-03
weight: 15
published: false
---

우리는[§다변수함수와 편미분](/ko/math/calculus/partial_derivatives)에서 다변수함수들을 정의하고, 이들의 미분을 살펴보았다. 이제는 적분을 살펴볼 차례다.

## 다중적분

한 변수 정적분이 구간 위의 함수값을 더한 것이었듯, 다변수에서는 영역 위의 함수값을 더한다. $$\mathbb{R}^n$$의 닫힌 상자부터 시작하자.

::: 정의 1
닫힌 상자 $$R = [a_1,b_1]\times\cdots\times[a_n,b_n]\subset \mathbb{R}^n$$ 위의 유계함수 $$f$$에 대하여, $$R$$을 작은 상자들(부피 $$\Delta V$$)로 분할하고 각 조각에서 표본점 $$\mathbf{x}^\ast$$을 택해 만든 리만 합

$$\sum f(\mathbf{x}^\ast) \Delta V$$

이 분할을 잘게 할 때 한 값으로 수렴하면, 그 값을 $$f$$의 *다중적분<sub>multiple integral</sub>*이라 하고 $$\int_R f dV$$로 적는다. 변수를 드러내어 $$\int\cdots\int_R f(x_1,\ldots,x_n) dx_1\cdots dx_n$$로도 쓴다.
:::

차원에 따라 이 적분은 서로 다른 양을 계산한다. $$n=1$$이면 익숙한 정적분, 곧 곡선 아래의 넓이로 돌아간다. $$n=2$$이고 $$f\geq 0$$이면, 밑면이 영역 $$R$$이고 윗면이 곡면 $$z=f(x,y)$$인 입체의 부피가 되며 이 경우를 특별히 *이중적분<sub>double integral</sub>*이라 하여 $$\iint_R f dA$$로 적는다. 리만 합의 각 항 $$f(x_i^\ast, y_j^\ast) \Delta A_{ij}$$은 밑면 넓이 $$\Delta A_{ij}$$에 높이 $$f$$를 곱한 가느다란 기둥의 부피이고, 이 기둥들을 모아 입체를 근사한 뒤 분할을 무한히 잘게 하는 극한이 이중적분이다. 차원을 하나 더 올려 $$n=3$$이면 *삼중적분<sub>triple integral</sub>* $$\iiint_E f dV$$이 되어, $$f\equiv 1$$을 넣으면 입체 $$E$$의 부피를, 밀도 $$\rho(x,y,z)$$를 넣으면 $$E$$의 질량을 준다. 일반적으로 $$f\equiv 1$$을 넣은 $$\int_D dV$$는 영역 $$D$$의 $$n$$차원 부피를 준다.

연속함수는 다중적분가능하며, 상자가 아닌 일반 영역 $$D$$ 위의 적분은 $$D$$를 포함하는 상자에서 $$D$$ 밖을 $$0$$으로 둔 함수를 적분하여 정의한다. $$D$$의 경계가 매끄러운 곡면들로 이루어져 있고 함수가 그 위에서 연속인 한 적분값은 잘 정의된다. 적분의 기본 성질도 한 변수의 경우와 똑같이 성립한다. 선형성 $$\int_D (\alpha f + \beta g) dV = \alpha\int_D f dV + \beta\int_D g dV$$, 단조성 ($$f\leq g$$이면 $$\int_D f dV \leq \int_D g dV$$), 영역가법성 ($$D = D_1\cup D_2$$가 겹치지 않는 두 조각이면 $$\int_D f dV = \int_{D_1} f dV + \int_{D_2} f dV$$) 이 그것이다. 영역 $$D$$ 위에서 함수 $$f$$의 *평균값<sub>average value</sub>*은 $$\frac{1}{\operatorname{vol}(D)}\int_D f dV$$로 정의되며, 한 변수 적분의 평균값을 다차원으로 옮긴 것이다.

## 푸비니 정리

다중적분의 정의는 $$n$$차원 극한이라 직접 계산하기 어렵다. 다행히 한 변수씩 차례로 적분하는 *반복적분<sub>iterated integral</sub>*으로 환원된다.

::: 정리 2 (푸비니)
$$f$$가 상자 $$R = [a_1,b_1]\times\cdots\times[a_n,b_n]$$에서 연속이면

$$\int_R f dV = \int_{a_1}^{b_1}\left(\int_{a_2}^{b_2}\cdots\left(\int_{a_n}^{b_n} f(x_1,\ldots,x_n) dx_n\right)\cdots dx_2\right)dx_1$$

이며, 적분 순서는 임의로 바꿀 수 있다.
:::

안쪽 적분은 한 변수를 상수로 고정하고 다른 변수로 적분하는 보통의 정적분이므로, 다중적분은 [§미적분의 기본정리](/ko/math/calculus/fundamental_theorem_of_calculus)와 적분법으로 푸는 한 변수 적분들의 연쇄로 환원된다. 피적분함수가 $$f(x_1,\ldots,x_n) = g_1(x_1)\cdots g_n(x_n)$$처럼 변수분리되고 영역이 상자이면 한 단계 더 나아가, 다중적분은 $$n$$개의 한 변수 적분의 곱 $$(\int_{a_1}^{b_1} g_1)\cdots(\int_{a_n}^{b_n} g_n)$$으로 분해된다.

일반 영역에서는 적분 구간이 다른 변수에 의존한다. $$n=2$$로 예를 보면, $$D = \{(x,y) \mid a\leq x\leq b,\ g_1(x)\leq y\leq g_2(x)\}$$이면

$$\iint_D f dA = \int_a^b \int_{g_1(x)}^{g_2(x)} f(x,y) dy dx$$

이며, 안쪽 적분의 끝값이 바깥 변수의 함수가 됨에 유의한다. 같은 영역을 반대 순서로 적분하려면 영역을 $$y$$ 기준으로 다시 기술해야 한다. 가령 꼭짓점이 $$(0,0), (1,0), (1,1)$$인 삼각형은 $$0 \leq x \leq 1$$, $$0 \leq y \leq x$$로도 $$0 \leq y \leq 1$$, $$y \leq x \leq 1$$로도 적힌다. $$n=3$$에서도 같다. 입체 $$E = \{(x,y,z) \mid (x,y)\in D,\ u_1(x,y)\leq z\leq u_2(x,y)\}$$를 먼저 $$z$$로 적분하고, 그 결과를 평면 영역 $$D$$ 위의 이중적분으로 처리한다.

순서를 어떻게 잡느냐는 답을 바꾸지 않지만, 한쪽 순서로는 안쪽 적분이 초등함수로 풀리는 반면 다른 순서로는 풀리지 않는 일이 흔하다. 그래서 *적분 순서 교환*은 단순한 형식 조작이 아니라 실용적인 계산 전략이다.

::: 예시 3 (적분 순서 교환)
이중적분

$$\int_0^1 \int_x^1 e^{y^2} dy dx$$

는 $$e^{y^2}$$의 부정적분이 초등함수가 아니라 안쪽부터 풀 수 없다. 그러나 적분 영역은 $$\{0 \leq x \leq y \leq 1\}$$이므로 순서를 바꾸면 바깥 변수가 영역의 끝값으로 들어오면서 새 인자 $$y$$가 생겨

$$\int_0^1 \int_0^y e^{y^2} dx dy = \int_0^1 y e^{y^2} dy = \frac12(e - 1)$$

로 닫힌다. 안쪽 적분이 한 순서로는 막히고 다른 순서로는 풀린다는 것이 순서 교환을 형식 조작 이상으로 만든다.
:::

## 변수변환

한 변수의 치환적분에 대응하는 것이 다변수의 변수변환이며, 길이 비율 $$g'$$의 자리에 야코비 행렬식이 들어간다.

::: 정리 4 (변수변환)
일대일 $$C^1$$ 사상 $$\mathbf{x} = \mathbf{T}(\mathbf{u})$$가 영역 $$D'\subset \mathbb{R}^n$$을 $$D$$로 보내고 야코비 행렬식이 $$D'$$에서 $$0$$이 아니면

$$\int_D f(\mathbf{x}) dV = \int_{D'} f(\mathbf{T}(\mathbf{u})) \lvert \det J_{\mathbf{T}}(\mathbf{u})\rvert dV'$$

이다. 여기서 $$J_{\mathbf{T}} = (\partial x_i/\partial u_j)$$는 $$\mathbf{T}$$의 야코비 행렬이다.
:::

야코비 행렬식 $$\lvert\det J_{\mathbf{T}}\rvert$$은 $$\mathbf{T}$$가 부피를 늘이는 국소 비율로, 한 변수에서 $$dx = \lvert g'(u)\rvert du$$에 해당한다. 직관적으로 보면, $$\mathbf{u}$$ 공간의 작은 상자가 $$\mathbf{T}$$에 의해 $$\mathbf{x}$$ 공간의 작은 평행육면체로 옮겨지는데, 그 부피가 $$\lvert\det J_{\mathbf{T}}\rvert$$ 곱하기 원래 상자의 부피가 되므로 부피 원소는 $$dV = \lvert\det J_{\mathbf{T}}(\mathbf{u})\rvert dV'$$로 변환된다. $$n=2$$에서 평행육면체는 평행사변형이 되어, 두 변 $$\mathbf{T}_u \Delta u$$와 $$\mathbf{T}_v \Delta v$$ ($$\mathbf{T}_u, \mathbf{T}_v$$는 $$\mathbf{T}$$의 편도함수 벡터) 가 이루는 넓이가 바로 $$\lvert\det J_{\mathbf{T}}\rvert \Delta u \Delta v$$인 것이다. 이 식을 리만 합에 대입해 극한을 취한 것이 [정리 4](#thm4)이며, 절댓값을 붙이는 이유는 부피가 항상 양수이기 때문이다 (한 변수의 치환적분에서 적분 구간의 방향이 부호를 흡수하던 것과 대비된다).

좌표계를 바꾸는 것이 변수변환의 가장 흔한 쓰임이고, 여기서 이중적분과 삼중적분이 구체적인 계산 예시로 등장한다.

::: 예시 5 (이중적분의 변수변환 — 극좌표)
이중적분에서 가장 흔한 변환이 극좌표 $$x = r\cos\theta$$, $$y = r\sin\theta$$이며, 그 야코비 행렬식은

$$\det J = \det\begin{pmatrix}\cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta\end{pmatrix} = r$$

이므로 $$dA = r dr d\theta$$이다. 이 여분의 인자 $$r$$이 직교좌표에서는 막히던 적분을 풀어 주는 일이 잦다. 가령 단위원판 $$D$$에서 이중적분

$$\iint_D e^{-(x^2+y^2)} dA = \int_0^{2\pi} \int_0^1 e^{-r^2} r dr d\theta = \pi(1 - e^{-1})$$

인데, $$e^{-r^2} r$$의 부정적분 $$-\frac12 e^{-r^2}$$가 닫힌 꼴이라 계산이 끝난다. 같은 인자가 한 변수로는 풀 수 없는 가우스 적분도 닫는다.
:::

::: 예시 6 (가우스 적분)
한 변수로는 초등함수로 안 풀리는 $$I = \int_{-\infty}^{\infty} e^{-x^2} dx$$를 이중적분으로 구한다. 곱 $$I^2$$을 두 개의 독립 변수에 대한 적분으로 보아 하나로 묶으면

$$\begin{aligned}
I^2 &= \left(\int_{-\infty}^\infty e^{-x^2} dx\right) \left(\int_{-\infty}^\infty e^{-y^2} dy\right) \\
&= \iint_{\mathbb{R}^2} e^{-x^2}e^{-y^2} dA = \iint_{\mathbb{R}^2} e^{-(x^2+y^2)} dA
\end{aligned}$$

이고, 이를 극좌표로 바꾸면 $$x^2 + y^2 = r^2$$이라

$$\begin{aligned}
I^2 &= \int_0^{2\pi} \int_0^\infty e^{-r^2} r dr d\theta \\
&= \int_0^{2\pi} \Bigl[-\frac12 e^{-r^2}\Bigr]_{r=0}^{r=\infty} d\theta = \int_0^{2\pi}\frac12 d\theta = \pi
\end{aligned}$$

이므로 $$I = \sqrt\pi$$이다. 차원을 하나 올려 회전대칭을 활용하는 이 기법이 가우스 적분의 고전적 풀이이며, 핵심은 직교좌표에서 풀리지 않던 안쪽 적분이 극좌표에서 생긴 여분의 인자 $$r$$ 덕분에 닫힌다는 데 있다.
:::

::: 예시 7 (삼중적분의 변수변환 — 구면·원기둥 좌표)
삼중적분에서는 공간의 회전대칭에 맞춘 두 좌표계가 쓰인다. *원기둥좌표<sub>cylindrical coordinates</sub>* $$(r, \theta, z)$$는 평면의 극좌표에 높이 $$z$$를 더한 것으로, $$x = r\cos\theta$$, $$y = r\sin\theta$$, $$z = z$$이고 야코비 행렬식이 $$r$$이라 $$dV = r dr d\theta dz$$이다. *구면좌표<sub>spherical coordinates</sub>* $$(\rho, \phi, \theta)$$는 원점으로부터의 거리 $$\rho$$, 양의 $$z$$축과의 각 $$\phi$$, 방위각 $$\theta$$로 점을 나타내며

$$x = \rho\sin\phi\cos\theta, \quad y = \rho\sin\phi\sin\theta, \quad z = \rho\cos\phi$$

이다. 그 야코비 행렬식을 계산하면 $$\det J = \rho^2\sin\phi$$이므로 $$dV = \rho^2\sin\phi d\rho d\phi d\theta$$이다. 회전대칭이 있는 입체에서 이 좌표들은 삼중적분을 크게 줄여 준다. 가령 반지름 $$R$$인 공의 부피는 구면좌표에서 세 변수가 분리되어

$$\iiint_{B_R} dV = \left(\int_0^{2\pi} d\theta\right)\left(\int_0^\pi \sin\phi d\phi\right)\left(\int_0^R \rho^2 d\rho\right) = 2\pi\cdot 2\cdot \frac{R^3}{3} = \frac{4\pi R^3}{3}$$

으로 곧장 나온다.
:::

야코비 행렬식이 부피의 국소 확대율로 나타나는 것은 미분을 선형사상으로 보는 관점에서 자연스럽다. 이로써 한 변수에서 시작한 미적분학이 다변수로 일관되게 확장된다.
