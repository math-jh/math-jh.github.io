---
title: "다중적분"
description: "여러 변수 함수의 다중적분을 리만 합으로 일반적으로 정의하고, 반복적분으로 환원하는 푸비니 정리를 다룬다. 야코비 행렬식을 통한 변수변환과 극·원기둥·구면 좌표, 가우스 적분, 부피 응용을 이중·삼중적분 계산 예시로 본다."
excerpt: "다중적분, 푸비니 정리, 변수변환과 야코비 행렬식"

categories: [Math / Calculus]
permalink: /ko/math/calculus/multiple_integrals
sidebar: 
    nav: "calculus-ko"

date: 2026-07-03
weight: 15
---

우리는 [§다변수함수와 편미분](/ko/math/calculus/partial_derivatives)에서 다변수함수들을 정의하고, 이들의 미분을 살펴보았다. 이제는 적분을 살펴볼 차례다.

## 다중적분

한 변수 정적분이 구간 위의 함수값을 더한 것이었듯, 다변수에서는 영역 위의 함수값을 더한다. $\mathbb{R}^n$의 closed 상자부터 시작하자.

::: 정의 1
Closed 상자 $R = [a_1,b_1]\times\cdots\times[a_n,b_n]\subset \mathbb{R}^n$ 위의 유계함수 $f$에 대하여, $R$을 작은 상자들(부피 $\Delta V$)로 분할하고 각 조각에서 표본점 $\mathbf{x}^\ast$을 택해 만든 리만 합

$$\sum f(\mathbf{x}^\ast) \Delta V$$

이 분할을 잘게 할 때 한 값으로 수렴하면, 그 값을 $f$의 *다중적분<sub>multiple integral</sub>*이라 하고 

$$\int_R f \mathop{dV}$$

로 적는다. 변수를 드러낼 필요가 있을 때는 

$$\int\cdots\int_R f(x_1,\ldots,x_n) \mathop{dx_1}\cdots \mathop{dx_n}$$

로도 쓰기도 한다.
:::

차원에 따라 이 적분은 서로 다른 양을 계산한다. $n=1$이면 익숙한 정적분, 곧 곡선 아래의 넓이를 계산하는 것이다. $n=2$이고 $f\geq 0$이면, 이것이 계산하는 양은 밑면이 영역 $R$이고 윗면이 곡면 $z=f(x,y)$인 입체의 부피가 되며, 이 경우를 특별히 *이중적분<sub>double integral</sub>*이라 부른다. 위의 $dV$는 $n$-차원 부피를 염두에 둔 표기이지만, $2$차원 부피, 즉 넓이는 우리가 이미 익숙한 대상이므로 이를 나타낼 때는 관례적으로

$$\iint_R f dA$$

와 같이 적기도 한다. 여기서 보면 적분의 의미가 더 명확한데, 리만 합의 각 항 $f(x_i^\ast, y_j^\ast) \Delta A_{ij}$은 밑면 넓이 $\Delta A_{ij}$에 높이 $f$를 곱한 가느다란 기둥의 부피이고, 이 기둥들을 모아 입체를 근사한 뒤 분할을 무한히 잘게 하는 극한이 바로 이중적분이다. 차원을 하나 더 올려 $n=3$이면 *삼중적분<sub>triple integral</sub>* 

$$\iiint_E f \mathop{dV}$$

이 된다.

연속함수는 다중적분가능하며, 상자가 아닌 일반 영역 $D$ 위의 적분은 $D$를 포함하는 상자 안에서, $D$ 밖에서는 함수값을 $0$으로 갖도록 함수를 확장한 것의 적분으로 정의된다. $D$의 boundary가 smooth한 곡면들로 이루어져 있고 함수가 그 위에서 연속인 한 적분값은 잘 정의되며, 적분의 기본 성질도 한 변수의 경우와 똑같이 성립한다는 것을 확인할 수 있다. 이 글에서 우리는 이들을 일일이 열거하는 대신, 새롭게 등장하는 것들만 간단히 정리한다. 

## 푸비니 정리

다중적분의 정의는 $n$차원 극한이라 직접 계산하기 어렵다. 다행히 한 변수씩 차례로 적분하는 *반복적분<sub>iterated integral</sub>*으로 환원된다.

::: 정리 2 (푸비니)
$f$가 상자 $R = [a_1,b_1]\times\cdots\times[a_n,b_n]$에서 연속이면

$$\int_R f \mathop{dV} = \int_{a_1}^{b_1}\left(\int_{a_2}^{b_2}\cdots\left(\int_{a_n}^{b_n} f(x_1,\ldots,x_n) \mathop{dx_n}\right)\cdots \mathop{dx_2}\right)\mathop{dx_1}$$

이며, 적분 순서는 임의로 바꿀 수 있다.
:::

엄밀한 증명은 $f$가 콤팩트인 상자 $R$ 위에서 균등연속이라는 해석학적 사실에 본질적으로 기대므로, 이 글에서는 생략한다. 어쨌든, 위 정리의 우변에 있는 안쪽 적분은 한 변수를 상수로 고정하고 다른 변수로 적분하는 보통의 정적분이므로, 다중적분은 [§미적분의 기본정리](/ko/math/calculus/fundamental_theorem_of_calculus)와 적분법으로 푸는 한 변수 적분들의 반복이 된다. 피적분함수가 $f(x_1,\ldots,x_n) = g_1(x_1)\cdots g_n(x_n)$처럼 변수분리되고 영역이 상자이면 한 단계 더 나아가, 다중적분은 $n$개의 한 변수 적분의 곱 

$$(\int_{a_1}^{b_1} g_1)\cdots(\int_{a_n}^{b_n} g_n)$$

으로 분해된다.

일반 영역에서는 적분구간이 다른 변수에 의존할 수 있다. $n=2$로 예를 보면, 

$$D = \{(x,y) \mid a\leq x\leq b,\ g_1(x)\leq y\leq g_2(x)\}$$

이면

$$\iint_D f dA = \int_a^b \int_{g_1(x)}^{g_2(x)} f(x,y) dy dx$$

이며, 안쪽 적분의 끝값이 바깥 변수의 함수가 된다. 따라서 같은 영역을 반대 순서로 적분하려면 영역을 $y$ 기준으로 다시 기술해야 한다. 가령 꼭짓점이 $(0,0), (1,0), (1,1)$인 삼각형은 

$$0 \leq x \leq 1,\quad 0 \leq y \leq x$$

로도 적을 수 있지만, 순서를 바꾸기 위해서는 

$$0 \leq y \leq 1,\quad y \leq x \leq 1$$

과 같이 적어줄 수도 있다. 순서를 어떻게 잡느냐는 답을 바꾸지 않지만, 한쪽 순서로는 안쪽 적분이 초등함수로 풀리는 반면 다른 순서로는 풀리지 않는 일이 흔하다.

::: 예시 3 (적분 순서 교환)
이중적분

$$\int_0^1 \int_x^1 e^{y^2} \mathop{dy} \mathop{dx}$$

는 $e^{y^2}$의 부정적분이 초등함수가 아니라 안쪽부터 풀 수 없다. 그러나 적분 영역은 $\{0 \leq x \leq y \leq 1\}$이므로 순서를 바꾸면 바깥 변수가 영역의 끝값으로 들어오면서 새 인자 $y$가 생겨

$$\int_0^1 \int_0^y e^{y^2} \mathop{dx} \mathop{dy} = \int_0^1 y e^{y^2} \mathop{dy} = \frac{1}{2}(e - 1)$$

로 풀린다.
:::

## 변수변환

한 변수의 치환적분에 대응하는 것이 다변수의 변수변환이며, 길이 비율 $g'$의 자리에 야코비 행렬식이 들어간다.

::: 정리 4 (변수변환)
일대일 $C^1$ 사상 $\mathbf{x} = \mathbf{T}(\mathbf{u})$가 영역 $D'\subset \mathbb{R}^n$을 $D$로 보내고 야코비 행렬식이 $D'$에서 $0$이 아니면

$$\int_D f(\mathbf{x}) \mathop{dV} = \int_{D'} f(\mathbf{T}(\mathbf{u})) \lvert \det J_{\mathbf{T}}(\mathbf{u})\rvert \mathop{dV'}$$

이다. 여기서 $J_{\mathbf{T}}$는 $\mathbf{T}$의 편도함수들을 모은 *야코비 행렬<sub>Jacobi matrix</sub>*

$$J_{\mathbf{T}}=\begin{pmatrix} \partial x_1/\partial u_1 & \cdots & \partial x_1/\partial u_n \\ \vdots & \ddots & \vdots \\ \partial x_n/\partial u_1 & \cdots & \partial x_n/\partial u_n\end{pmatrix}$$

이다.
:::
역시 이 또한 우리는 선형대수의 내용은 블랙박스로 두기로 하였으므로, 그 증명은 해석학에 미뤄둔다. 어쨌든 중요한 것은 직관으로, 야코비 행렬식 $\lvert\det J_{\mathbf{T}}\rvert$은 $\mathbf{T}$가 부피를 늘이는 국소 비율이다. 즉, $\mathbf{u}$ 공간의 작은 상자가 $\mathbf{T}$에 의해 $\mathbf{x}$ 공간의 작은 평행육면체로 옮겨지는데, 그 부피가 원래 상자의 부피에 $\lvert\det J_{\mathbf{T}}\rvert$를 곱해준 것이 되므로 부피 원소는 $\mathop{dV} = \lvert\det J_{\mathbf{T}}(\mathbf{u})\rvert \mathop{dV}'$로 변환된다. $n=2$에서 평행육면체는 평행사변형이 되어, 두 변 $\mathbf{T}_u \Delta u$와 $\mathbf{T}_v \Delta v$ ($\mathbf{T}_u, \mathbf{T}_v$는 $\mathbf{T}$의 편도함수 벡터) 가 이루는 넓이가 바로 $\lvert\det J_{\mathbf{T}}\rvert \Delta u \Delta v$인 것이다. 이 식을 리만 합에 대입해 극한을 취한 것이 [정리 4](#thm4)이며, 절댓값을 붙이는 이유는 부피가 항상 양수이기 때문이다.

변수변환의 가장 흔한 쓰임은 좌표계를 바꾸는 것으로, 우리는 $2\times 2$ 행렬과 $3\times 3$ 행렬의 행렬식만 도입하였으므로 이들이 우리 예시의 전부이다. 

::: 예시 5 (이중적분의 변수변환 — 극좌표)
이중적분에서 가장 흔한 변환은 극좌표 $x = r\cos\theta$, $y = r\sin\theta$이다. 그럼 그 야코비 행렬식은

$$\det J = \det\begin{pmatrix}\cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta\end{pmatrix} = r$$

이므로 $dA = r dr d\theta$이다. 이 여분의 인자 $r$이 직교좌표에서는 막히던 적분을 풀어 주는 일이 잦다. 가령 단위원판 $D$에서 이중적분

$$\iint_D e^{-(x^2+y^2)} \mathop{dA} = \int_0^{2\pi} \int_0^1 e^{-r^2} r \mathop{dr}\mathop{d\theta} = \pi(1 - e^{-1})$$

인데, $e^{-r^2} r$의 부정적분이 $-e^{-r^2}/2$로 명시적으로 주어지므로 이 계산을 완료할 수 있다. 
:::

위의 예시를 이용하면, 우리는 하나의 변수로 풀리지 않던 가우스 적분의 값을 구할 수 있다.

::: 예시 6 (가우스 적분)
적분 $I = \int_{-\infty}^{\infty} e^{-x^2} \mathop{dx}$의 값을 구하자. 이 값의 제곱 $I^2$을 두 개의 독립 변수에 대한 적분으로 보면

$$\begin{aligned}
I^2 &= \left(\int_{-\infty}^\infty e^{-x^2} \mathop{dx}\right) \left(\int_{-\infty}^\infty e^{-y^2} \mathop{dy}\right) \\
&= \iint_{\mathbb{R}^2} e^{-x^2}e^{-y^2} \mathop{dA} = \iint_{\mathbb{R}^2} e^{-(x^2+y^2)} \mathop{dA}
\end{aligned}$$

이고, 이를 극좌표로 바꾸면 $x^2 + y^2 = r^2$이라

$$\begin{aligned}
I^2 &= \int_0^{2\pi} \int_0^\infty e^{-r^2} r \mathop{dr} \mathop{d\theta} \\
&= \int_0^{2\pi} \Bigl[-\frac{1}{2} e^{-r^2}\Bigr]_{r=0}^{r=\infty} \mathop{d\theta} = \int_0^{2\pi}\frac{1}{2} \mathop{d\theta} = \pi
\end{aligned}$$

이므로 $I = \sqrt\pi$이다. 
:::

$2$차원에서의 고전적인 예시는 극좌표계 하나지만, $3$차원에서는 구면좌표계와 원기둥좌표계의 두 가지 치환방법이 있으며, 이를 적절한 방식으로 계산하는 것이 많은 적분을 계산할 때 도움이 된다.

::: 예시 7 (삼중적분의 변수변환 — 구면·원기둥 좌표)
우선 *원기둥좌표<sub>cylindrical coordinates</sub>* $(r, \theta, z)$는 평면의 극좌표에 높이 $z$를 더한 것으로, 

$$x = r\cos\theta,\quad y = r\sin\theta, \quad z = z$$

이고 야코비 행렬식은

$$\det J = \det\begin{pmatrix}\cos\theta & -r\sin\theta & 0 \\ \sin\theta & r\cos\theta & 0 \\ 0 & 0 & 1\end{pmatrix} = r$$

이므로 $\mathop{dV} = r \mathop{dr} \mathop{d\theta} \mathop{dz}$이다. 

*구면좌표<sub>spherical coordinates</sub>* $(\rho, \phi, \theta)$의 경우, 원점으로부터의 거리 $\rho$, 양의 $z$축과의 각 $\phi$, 방위각 $\theta$로 점을 나타내며

$$x = \rho\sin\phi\cos\theta, \quad y = \rho\sin\phi\sin\theta, \quad z = \rho\cos\phi$$

이다. 그 야코비 행렬식을 계산하면 

$$\det J = \det\begin{pmatrix} \sin\phi\cos\theta & \rho\cos\phi\cos\theta & -\rho\sin\phi\sin\theta \\ \sin\phi\sin\theta & \rho\cos\phi\sin\theta & \rho\sin\phi\cos\theta \\ \cos\phi & -\rho\sin\phi & 0 \end{pmatrix} = \rho^2\sin\phi$$

이므로 $\mathop{dV} = \rho^2\sin\phi \mathop{d\rho} \mathop{d\phi} \mathop{d\theta}$이다. 가령 반지름 $R$인 공의 부피는 구면좌표에서 세 변수가 분리되어

$$\iiint_{B_R} \mathop{dV} = \left(\int_0^{2\pi} \mathop{d\theta}\right)\left(\int_0^\pi \sin\phi \mathop{d\phi}\right)\left(\int_0^R \rho^2 \mathop{d\rho}\right) = 2\pi\cdot 2\cdot \frac{R^3}{3} = \frac{4\pi R^3}{3}$$

으로 유도할 수 있다.
:::
