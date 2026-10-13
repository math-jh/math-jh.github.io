---
title: "다변수 미분"
description: "다변수함수의 미분을 한 점에서의 일차근사를 주는 선형사상으로 정의하고, 편미분·방향미분·야코비 행렬과의 관계를 정리한다. 편미분이 존재해도 미분가능하지 않은 반례, C¹ 함수의 미분가능성, 연쇄법칙, 그리고 벡터값 함수에서 등식이 실패하는 평균값 정리와 그 대안인 평균값 부등식을 증명과 함께 다룬다."
excerpt: "전미분, 편미분과의 차이, 연쇄법칙, 평균값 부등식"

categories: [Math / Analysis]
permalink: /ko/math/analysis/multivariable_differentiation
sidebar: 
    nav: "analysis-ko"

date: 2026-06-02
weight: 25

published: false

---

[\[미적분학\] §다변수함수와 편미분, ⁋정의 2](/ko/math/calculus/partial_derivatives#def2)에서 편미분을 다루었다. 이 글에서는 $f:\mathbb{R}^n\to\mathbb{R}^m$의 미분을 일변수의 $f(a+h)=f(a)+f'(a)h+o(h)$를 그대로 옮긴 형태로 정의한다. 일변수에서 $f'(a)$는 증분 $h$를 받아 $f'(a)h$를 돌려주는 곱셈이고, 입력과 출력이 모두 벡터가 되면 이 곱셈의 자리에 오는 것은 [\[선형대수학\] §선형사상, ⁋정의 1](/ko/math/linear_algebra/linear_map#def1)의 선형사상이다. 이렇게 정의한 미분은 편미분보다 엄격하게 강한 조건이며, 이 차이가 이 글의 첫 번째 주제이다. 이어서 연쇄법칙과 평균값 정리를 다변수로 옮긴다. 평균값 정리는 값이 벡터인 순간 등식이 성립하지 않게 되고, 부등식 형태만 살아남는다.

## 전미분

$\mathbb{R}^n$과 $\mathbb{R}^m$에는 Euclid 노름 $\lVert\cdot\rVert$를 쓴다. 선형사상 $L:\mathbb{R}^n\to\mathbb{R}^m$의 행렬을 $(L_{ij})$라 하면 [\[선형대수학\] §내적공간, ⁋명제 3](/ko/math/linear_algebra/inner_product_spaces#prop3)에 의해 $\lVert Lx\rVert^2=\sum_i\bigl(\sum_j L_{ij}x_j\bigr)^2\le\bigl(\sum_{i,j}L_{ij}^2\bigr)\lVert x\rVert^2$이므로, 모든 $x$에 대해 $\lVert Lx\rVert\le M\lVert x\rVert$인 상수 $M$이 존재한다. 이런 $M$ 중 최솟값을 $\lVert L\rVert$로 적는다. 정의에 의해 $\lVert Lx\rVert\le\lVert L\rVert\lVert x\rVert$이고, 특히 선형사상은 연속이다.

::: 정의 1
$U\subseteq\mathbb{R}^n$이 열린집합이고 $a\in U$라 하자. 함수 $f:U\to\mathbb{R}^m$이 $a$에서 *미분가능<sub>differentiable</sub>*하다는 것은 선형사상 $L:\mathbb{R}^n\to\mathbb{R}^m$이 존재하여

$$\lim_{h\to 0}\frac{\lVert f(a+h)-f(a)-Lh\rVert}{\lVert h\rVert}=0$$

이 성립하는 것이다. 이러한 $L$은 뒤의 [명제 2](#prop2)에 의해 유일하며, 이를 $f$의 $a$에서의 *미분* $Df(a)$라 부른다.
:::

잔차를 $r(h)=f(a+h)-f(a)-Df(a)h$로 두면 $f(a+h)=f(a)+Df(a)h+r(h)$이고 $\lVert r(h)\rVert/\lVert h\rVert\to 0$이다. 곧 $h\mapsto f(a)+Df(a)h$가 $f$를 $a$ 근방에서 $\lVert h\rVert$보다 빠른 속도로 좁혀지는 오차 안에서 근사한다. $n=m=1$이면 선형사상은 수 하나를 곱하는 것이므로 $Df(a)h=f'(a)h$이고 이 정의는 일변수 미분가능성과 같다.

미분을 선형사상 $\mathbb{R}^n\to\mathbb{R}^m$으로 정의했으므로 그 좌표 표현은 $m\times n$ 행렬이다. 함수 $f=(f_1,\dots,f_m)$의 편미분 $\partial f_i/\partial x_j(a)$를 $(i,j)$ 성분으로 갖는 행렬을 $f$의 $a$에서의 *야코비 행렬* $J_f(a)$라 한다. 또 $v\in\mathbb{R}^n$ 방향의 *방향미분*을 $D_vf(a)=\lim_{t\to 0}\bigl(f(a+tv)-f(a)\bigr)/t$로 정의한다. 편미분은 $v=e_j$인 방향미분이다.

::: 명제 2
$f:U\to\mathbb{R}^m$이 $a$에서 미분가능하다고 하자. 그러면 다음이 성립한다.

1. $f$는 $a$에서 연속이다.
2. 모든 $v\in\mathbb{R}^n$에 대해 방향미분 $D_vf(a)$가 존재하고 $D_vf(a)=Df(a)v$이다.
3. $Df(a)$를 표준기저로 나타낸 행렬은 야코비 행렬 $J_f(a)$이다. 특히 [정의 1](#def1)의 조건을 만족하는 선형사상은 하나뿐이다.
:::

::: 증명
$L$이 [정의 1](#def1)의 조건을 만족하는 임의의 선형사상이라 하고 $r(h)=f(a+h)-f(a)-Lh$로 둔다.

(1) $\lVert Lh\rVert\le\lVert L\rVert\lVert h\rVert\to 0$이고, $\lVert r(h)\rVert=\bigl(\lVert r(h)\rVert/\lVert h\rVert\bigr)\lVert h\rVert\to 0$이다. 따라서 $f(a+h)-f(a)=Lh+r(h)\to 0$이다.

(2) $v=0$이면 양변이 $0$이다. $v\neq 0$이면 $h=tv$에 대해 $L(tv)=tLv$이므로

$$\frac{f(a+tv)-f(a)}{t}-Lv=\frac{r(tv)}{t}$$

이고, $\lVert r(tv)/t\rVert=\lVert v\rVert\cdot\lVert r(tv)\rVert/\lVert tv\rVert\to 0$이다. 따라서 $D_vf(a)$가 존재하고 $Lv$와 같다.

(3) (2)에서 $v=e_j$로 두면 $Le_j$의 $i$번째 성분은 $f_i$의 $x_j$에 대한 편미분이다. 곧 $L$의 $j$번째 열이 $J_f(a)$의 $j$번째 열이므로 $L$은 $J_f(a)$가 정하는 선형사상이다. $L$이 임의였으므로 유일성도 얻는다.
:::

실숫값 함수($m=1$)에서 $J_f(a)$는 한 줄짜리 행렬이고, 이를 열벡터로 쓴 것이 기울기 $\nabla f(a)$이다. 이때 [명제 2](#prop2)의 (2)는 $D_vf(a)=\nabla f(a)\cdot v$를 뜻한다. 반대로 $n=1$인 곡선 $\gamma:I\to\mathbb{R}^m$에서는 $J_\gamma(t)$가 한 열짜리 행렬, 곧 속도벡터 $\gamma'(t)$이다.

## 편미분과 미분가능성

[명제 2](#prop2)의 역은 성립하지 않는다. 편미분이 모두 존재하는 것은 좌표축 방향 $n$개에서만 일차근사가 있다는 뜻이고, 미분가능성은 모든 방향에서 오차가 $o(\lVert h\rVert)$로 균일하게 줄어든다는 뜻이다. 아래 두 반례는 이 차이가 연속성에서까지 드러남을 보여 준다.

::: 예시 3 (편미분은 존재하나 미분가능하지 않다)
$f(x,y)=xy/(x^2+y^2)$ ($(x,y)\neq(0,0)$), $f(0,0)=0$으로 두자. $f(x,0)=0=f(0,y)$이므로 원점에서 $\partial f/\partial x=\partial f/\partial y=0$으로 두 편미분이 모두 존재한다. 그러나 $t\neq 0$에서 $f(t,t)=1/2$이므로 $f$는 원점에서 연속이 아니고, [명제 2](#prop2)의 (1)에 의해 미분가능하지 않다.
:::

::: 예시 4 (모든 방향미분이 존재하나 연속이 아니다)
$f(x,y)=x^2y/(x^4+y^2)$ ($(x,y)\neq(0,0)$), $f(0,0)=0$으로 두자. 방향 $v=(p,q)$에 대해 $t\neq 0$에서

$$\frac{f(tp,tq)-f(0,0)}{t}=\frac{p^2q}{t^2p^4+q^2}$$

이다. $q\neq 0$이면 $t\to 0$에서 $p^2/q$로 수렴하고, $q=0$이면 항상 $0$이다. 따라서 원점에서 모든 방향미분이 존재한다. 그럼에도 포물선 $y=x^2$ 위에서 $f(t,t^2)=t^4/(2t^4)=1/2$이므로 $f$는 원점에서 연속이 아니다. 방향미분 $v\mapsto D_vf(0)$이 $q\neq 0$에서 $p^2/q$이고 $q=0$에서 $0$이어서 $v$에 대해 선형도 아니라는 점도 [명제 2](#prop2)의 (2)와 어긋난다.
:::

[예시 4](#ex4)는 모든 직선을 따라 원점으로 접근할 때의 극한이 같아도 함수가 연속이 아닐 수 있음을 보여 준다. 직선 위의 값만 보는 방향미분으로는 포물선 같은 곡선 위의 거동이 잡히지 않는다.

편미분에 연속성을 더하면 미분가능성이 따라온다. 열린집합 $U$ 위에서 모든 편미분이 존재하고 연속인 함수를 $C^1$ 함수라 한다.

::: 정리 5
$f:U\to\mathbb{R}^m$의 모든 편미분이 $a$를 포함하는 열린 공 $B\subseteq U$ 위에서 존재하고 $a$에서 연속이면 $f$는 $a$에서 미분가능하다. 특히 $C^1$ 함수는 $U$의 모든 점에서 미분가능하다.
:::

::: 증명
성분 $f_1,\dots,f_m$이 각각 $a$에서 미분가능하면 $f$도 그러하다. 실제로 $f_i$의 미분이 $L_i$이면 $Lh=(L_ih)_i$로 정의한 선형사상 $L$에 대해 $\lVert f(a+h)-f(a)-Lh\rVert\le\sum_i\lvert f_i(a+h)-f_i(a)-L_ih\rvert$이고, 우변을 $\lVert h\rVert$로 나눈 값이 $0$으로 가기 때문이다. 따라서 $m=1$인 경우만 보인다.

$h=(h_1,\dots,h_n)$이 충분히 작아 $a+h\in B$라 하고, $a^{(0)}=a$, $a^{(j)}=a+(h_1,\dots,h_j,0,\dots,0)$로 둔다. $\lVert a^{(j)}-a\rVert\le\lVert h\rVert$이므로 모든 $a^{(j)}$가 $B$ 안에 있고, $a^{(j-1)}$에서 $a^{(j)}$로 가는 선분도 $B$ 안에 있다. 증분을 한 좌표씩 켜는 망원합

$$f(a+h)-f(a)=\sum_{j=1}^n\bigl(f(a^{(j)})-f(a^{(j-1)})\bigr)$$

을 쓴다. 각 항에서 $s\mapsto f(a^{(j-1)}+se_j)$는 $0$과 $h_j$ 사이에서 편미분의 존재 때문에 미분가능하다. 한 변수의 [§평균값 정리와 테일러 정리, ⁋정리 3](/ko/math/analysis/mean_value_theorem#thm3)을 적용하면 $a^{(j-1)}$과 $a^{(j)}$를 잇는 선분 위의 점 $\xi_j$가 있어

$$f(a^{(j)})-f(a^{(j-1)})=\frac{\partial f}{\partial x_j}(\xi_j)h_j$$

이다. 이를 대입하고 $\sum_j(\partial f/\partial x_j)(a)h_j$를 빼면

$$f(a+h)-f(a)-\sum_{j=1}^n\frac{\partial f}{\partial x_j}(a)h_j=\sum_{j=1}^n\left(\frac{\partial f}{\partial x_j}(\xi_j)-\frac{\partial f}{\partial x_j}(a)\right)h_j$$

이다. $\lvert h_j\rvert\le\lVert h\rVert$이므로 좌변의 절댓값을 $\lVert h\rVert$로 나눈 값은 $\sum_j\lvert\partial_jf(\xi_j)-\partial_jf(a)\rvert$ 이하이다. 여기서 $\lVert\xi_j-a\rVert\le\lVert h\rVert$이므로 $h\to 0$일 때 $\xi_j\to a$이고, 편미분이 $a$에서 연속이므로 이 합은 $0$으로 간다. 따라서 선형사상 $h\mapsto\sum_j\partial_jf(a)h_j$가 [정의 1](#def1)의 조건을 만족한다.
:::

연속성 가정에서 쓰인 곳은 $\xi_j$가 $a$ 자신이 아니라 $a$ 근방의 점이라는 부분이다. 편미분이 $a$에서 연속이 아니면 $\partial_jf(\xi_j)-\partial_jf(a)$를 제어할 수 없고, [예시 3](#ex3)의 함수가 실제로 그 경우이다. 한편 [정리 5](#thm5)의 역은 성립하지 않는다.

::: 예시 6 (미분가능하나 $C^1$이 아니다)
$f(x)=x^2\sin(1/x)$ ($x\neq 0$), $f(0)=0$으로 두자. $\lvert f(h)-f(0)\rvert/\lvert h\rvert=\lvert h\sin(1/h)\rvert\le\lvert h\rvert\to 0$이므로 $f'(0)=0$이다. 그러나 $x\neq 0$에서 $f'(x)=2x\sin(1/x)-\cos(1/x)$이고 $x\to 0$일 때 $2x\sin(1/x)\to 0$이지만 $\cos(1/x)$는 극한이 없으므로 $f'$은 $0$에서 연속이 아니다.
:::

## 연쇄법칙

연쇄법칙은 선형사상의 합성이라는 형태로 가장 간명하게 쓰인다.

::: 정리 7 (연쇄법칙)
$U\subseteq\mathbb{R}^n$, $V\subseteq\mathbb{R}^m$이 열린집합이고 $f:U\to V$가 $a$에서, $g:V\to\mathbb{R}^p$가 $b=f(a)$에서 미분가능하면 $g\circ f$는 $a$에서 미분가능하고

$$D(g\circ f)(a)=Dg(b)\circ Df(a)$$

이다. 따라서 $J_{g\circ f}(a)=J_g(b)J_f(a)$이다.
:::

::: 증명
$A=Df(a)$, $B=Dg(b)$로 두고 잔차를 $r(h)=f(a+h)-f(a)-Ah$, $s(k)=g(b+k)-g(b)-Bk$로 쓴다. $f$가 $a$에서 연속이므로 $h$가 작으면 $f(a+h)\in V$이고, $k(h)=f(a+h)-b=Ah+r(h)$로 두면

$$(g\circ f)(a+h)-(g\circ f)(a)=Bk(h)+s(k(h))=BAh+\bigl(Br(h)+s(k(h))\bigr)$$

이다. 따라서 $\rho(h)=Br(h)+s(k(h))$가 $o(\lVert h\rVert)$임을 보이면 된다.

첫 항은 $\lVert Br(h)\rVert\le\lVert B\rVert\lVert r(h)\rVert=o(\lVert h\rVert)$이다. 둘째 항에서는 $s(k)/\lVert k\rVert$를 $k=0$에서도 정의되도록 $\sigma(k)=s(k)/\lVert k\rVert$ ($k\neq 0$), $\sigma(0)=0$으로 둔다. $B$의 미분가능성에 의해 $\sigma(k)\to 0$ ($k\to 0$)이고, 모든 $k$에 대해 $\lVert s(k)\rVert=\lVert\sigma(k)\rVert\lVert k\rVert$이다. $k(h)=0$이 되는 $h$가 있어도 이 식이 성립하므로 $\lVert k\rVert$로 나누는 일을 피할 수 있다. 한편 $h$가 충분히 작으면 $\lVert r(h)\rVert\le\lVert h\rVert$이므로 $\lVert k(h)\rVert\le(\lVert A\rVert+1)\lVert h\rVert$이다. 따라서

$$\frac{\lVert s(k(h))\rVert}{\lVert h\rVert}=\lVert\sigma(k(h))\rVert\frac{\lVert k(h)\rVert}{\lVert h\rVert}\le(\lVert A\rVert+1)\lVert\sigma(k(h))\rVert$$

이고, $h\to 0$이면 $k(h)\to 0$이므로 우변이 $0$으로 간다. 두 항을 합쳐 $\rho(h)=o(\lVert h\rVert)$이고, [정의 1](#def1)에 의해 $D(g\circ f)(a)=BA$이다. 행렬의 식은 선형사상의 합성이 행렬곱에 대응하는 데서 나온다.
:::

행렬곱을 성분으로 쓰면 $\partial(g\circ f)_i/\partial x_j(a)=\sum_k\partial g_i/\partial y_k(b)\cdot\partial f_k/\partial x_j(a)$이다. 특히 $g$가 실숫값이고 $\gamma$가 미분가능한 곡선이면 $(g\circ\gamma)'(t)=\nabla g(\gamma(t))\cdot\gamma'(t)$이며, $\gamma(t)=a+tv$로 두면 $D_vg(a)=\nabla g(a)\cdot v$를 다시 얻는다.

연쇄법칙의 가정은 두 함수가 각각 미분가능하다는 것이지 편미분이 존재한다는 것이 아니다. 편미분만으로 위의 공식을 쓰면 틀린 답을 낼 수 있다.

::: 예시 8 (편미분만으로는 연쇄법칙이 성립하지 않는다)
[예시 3](#ex3)의 $f$와 곡선 $\gamma(t)=(t,t)$를 생각하자. $\gamma$는 미분가능하고 $f$의 두 편미분은 원점에서 모두 $0$이므로 $\sum_j\partial_jf(\gamma(0))\gamma_j'(0)=0$이다. 그러나 합성 $f\circ\gamma$는 $t\neq 0$에서 $1/2$, $t=0$에서 $0$이어서 $0$에서 연속조차 아니다. 이 경우 $f$가 원점에서 미분가능하지 않으므로 [정리 7](#thm7)의 가정이 깨진 것이다.
:::

## 평균값 정리

[§평균값 정리와 테일러 정리, ⁋정리 3](/ko/math/analysis/mean_value_theorem#thm3)의 등식 $f(b)-f(a)=f'(\xi)(b-a)$는 다변수에서 선분 위로 제한하여 옮길 수 있다. $a,b\in U$일 때 선분 $\{a+t(b-a):0\le t\le 1\}$이 $U$에 포함되어 있다고 가정한다.

::: 정리 9 (실숫값 함수의 평균값 정리)
$f:U\to\mathbb{R}$가 $U$ 위에서 미분가능하고 $a$와 $b$를 잇는 선분이 $U$에 포함되면, $\theta\in(0,1)$이 존재하여

$$f(b)-f(a)=Df\bigl(a+\theta(b-a)\bigr)(b-a)$$

이다.
:::

::: 증명
$\gamma(t)=a+t(b-a)$이면 $\gamma^{-1}(U)$는 $\mathbb{R}$의 열린집합이고 $[0,1]$을 포함하므로, $\varphi=f\circ\gamma$는 $[0,1]$을 포함하는 열린구간 위에서 정의된다. [정리 7](#thm7)에 의해 $\varphi$는 거기서 미분가능하고 $\varphi'(t)=Df(\gamma(t))(b-a)$이다. 한 변수의 [§평균값 정리와 테일러 정리, ⁋정리 3](/ko/math/analysis/mean_value_theorem#thm3)을 적용하면 $\theta\in(0,1)$이 있어 $f(b)-f(a)=\varphi(1)-\varphi(0)=\varphi'(\theta)$이다.
:::

값이 벡터이면 같은 형태의 등식이 성립하지 않는다. 성분마다 [§평균값 정리와 테일러 정리, ⁋정리 3](/ko/math/analysis/mean_value_theorem#thm3)을 적용하면 $\theta$가 성분마다 달라지기 때문이다.

::: 예시 10 (벡터값 함수에서 평균값 등식의 실패)
$f:\mathbb{R}\to\mathbb{R}^2$, $f(t)=(\cos t,\sin t)$로 두고 $a=0$, $b=2\pi$로 하자. $f(b)-f(a)=0$이다. 그러나 $Df(t)(b-a)=2\pi(-\sin t,\cos t)$이고 그 노름은 모든 $t$에서 $2\pi$이므로 $0$이 될 수 없다. 따라서 $f(b)-f(a)=Df(\xi)(b-a)$를 만족하는 $\xi$는 존재하지 않는다.
:::

등식을 포기하면 크기에 대한 부등식이 남는다. 이는 도함수가 유계이면 함수값의 변화도 유계라는 형태로 쓰인다.

::: 정리 11 (평균값 부등식)
$f:U\to\mathbb{R}^m$이 $U$ 위에서 미분가능하고, $a$와 $b$를 잇는 선분 위의 모든 $x$에서 $\lVert Df(x)\rVert\le M$이면

$$\lVert f(b)-f(a)\rVert\le M\lVert b-a\rVert$$

이다.
:::

::: 증명
$z=f(b)-f(a)$로 두고 $z=0$이면 자명하므로 $z\neq 0$이라 하자. 실숫값 함수 $\varphi(t)=z\cdot f(a+t(b-a))$를 생각한다. $y\mapsto z\cdot y$가 $\mathbb{R}^m\to\mathbb{R}$의 선형사상이므로 [정리 7](#thm7)에 의해 $\varphi$는 미분가능하고 $\varphi'(t)=z\cdot Df(a+t(b-a))(b-a)$이다. 한 변수의 [§평균값 정리와 테일러 정리, ⁋정리 3](/ko/math/analysis/mean_value_theorem#thm3)에 의해 $\theta\in(0,1)$이 있어 $\xi=a+\theta(b-a)$에 대해

$$\lVert z\rVert^2=\varphi(1)-\varphi(0)=\varphi'(\theta)=z\cdot Df(\xi)(b-a)\le\lVert z\rVert\lVert Df(\xi)\rVert\lVert b-a\rVert\le\lVert z\rVert M\lVert b-a\rVert$$

이다. 가운데 부등식은 [\[선형대수학\] §내적공간, ⁋명제 3](/ko/math/linear_algebra/inner_product_spaces#prop3)과 노름의 정의에서 나온다. $\lVert z\rVert\neq 0$으로 나누면 결론을 얻는다.
:::

증명은 벡터값 함수를 $z$ 방향으로 사영하여 실숫값 문제로 환원한 것이다. 사영하는 방향 $z$가 $f(b)-f(a)$ 자체로 잡혀 있어서, [예시 10](#ex10)처럼 점 $\xi$가 성분마다 달라지는 문제가 일어나지 않는다. 대신 $\xi$가 어디인지에 대한 정보는 잃고, 선분 위 $\lVert Df\rVert$의 상한만 남는다.

::: 따름정리 12
$U$가 열린 연결집합이고 모든 점에서 $Df=0$이면 $f:U\to\mathbb{R}^m$은 상수이다.
:::

::: 증명
$x_0\in U$를 고정하고 $S=\{x\in U:f(x)=f(x_0)\}$로 둔다. 임의의 $x\in U$에 대해 $x$를 중심으로 하는 열린 공 $B\subseteq U$를 잡으면, 공은 볼록하므로 $B$의 두 점을 잇는 선분이 $B$에 포함된다. [정리 11](#thm11)을 $M=0$으로 적용하면 $f$는 $B$ 위에서 상수이다. 따라서 $x\in S$이면 $B\subseteq S$이고 $x\notin S$이면 $B\cap S=\emptyset$이므로 $S$와 $U\setminus S$가 모두 열린집합이다. $U$가 연결이고 $x_0\in S$이므로 [§연결성과 중간값 정리, ⁋정의 1](/ko/math/analysis/connectedness#def1)에 의해 $S=U$이다.
:::

---

**참고문헌**

**[Rud]** W. Rudin, *Principles of mathematical analysis*, 3rd ed., McGraw-Hill, 1976.
