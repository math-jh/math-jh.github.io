---
title: "역함수 정리와 음함수 정리"
description: "연속미분가능한 사상의 미분이 한 점에서 가역이면 그 점 근방에서 사상이 가역임을 축소사상 정리로 증명한다. 이로부터 음함수 정리, 등위집합의 tangent space, Lagrange 승수법을 유도하고, 가정이 빠지면 결론이 무너지는 반례를 함께 다룬다."
excerpt: "역함수 정리, 음함수 정리, Lagrange 승수법"

categories: [Math / Analysis]
permalink: /ko/math/analysis/inverse_function_theorem
sidebar: 
    nav: "analysis-ko"

date: 2026-06-02
weight: 27

published: false

---

[§다변수 미분, ⁋정의 1](/ko/math/analysis/multivariable_differentiation#def1){: data-lid="v9twh" }에서 사상 $f$의 미분 $Df(a)$는 $a$ 근방에서 $f$를 가장 잘 근사하는 선형사상이었다. 선형사상이 가역이면 그것이 근사하는 사상도 $a$ 근방에서 가역이리라 기대할 수 있고, 역함수 정리는 이 기대가 $C^1$ 가정 아래 참임을 말해 준다.

한 변수에서는 이 사실에 별도의 증명이 필요하지 않다. $f$가 $C^1$이고 $f'(a)\neq 0$이면 $f'$의 연속성에 의해 $a$ 근방에서 $f'$의 부호가 유지되고, 따라서 [§평균값 정리와 테일러 정리, ⁋따름정리 4](/ko/math/analysis/mean_value_theorem#cor4){: data-lid="k0a3i" }에 의해 $f$는 그 근방에서 순단조이다. 여러 변수에서는 단조성이라는 도구가 없으므로, 방정식 $f(x)=y$의 해의 존재와 유일성을 [§완비 거리공간과 축소사상 정리, ⁋정리 5](/ko/math/analysis/contraction_mapping#thm5){: data-lid="hbqbs" }로 직접 확보하는 것이 증명의 골격이 된다. 이 글에서는 사상의 정의역을 $\mathbb{R}^n$의 열린집합으로 두고, $\mathbb{R}^n$에는 Euclid 노름을, 선형사상에는 연산자 노름 $\lVert T\rVert=\sup_{\lVert v\rVert=1}\lVert Tv\rVert$을 쓴다. 따라서 $\lVert Tv\rVert\leq\lVert T\rVert\lVert v\rVert$이다.

## 역함수 정리

::: 정리 1 (역함수 정리)
$\Omega\subseteq\mathbb{R}^n$이 열린집합이고 $f:\Omega\to\mathbb{R}^n$이 $C^1$ 사상이며 $a\in\Omega$에서 $Df(a)$가 가역이라 하자. 그럼 $a$의 열린 근방 $U\subseteq\Omega$와 $f(a)$의 열린 근방 $V$가 존재하여 $f:U\to V$가 전단사이고, 역사상 $g=f^{-1}:V\to U$는 $C^1$이며 모든 $x\in U$에 대해

$$Dg(f(x))=\bigl(Df(x)\bigr)^{-1}$$

이다.
:::

증명에서는 $\Omega$ 안의 볼록집합에서 미분의 크기를 통제해 사상의 변화량을 억제하는 부등식이 필요하다.

::: 보조정리 2 (평균값 부등식)
$\Omega\subseteq\mathbb{R}^n$이 열린집합, $\varphi:\Omega\to\mathbb{R}^m$이 미분가능하고, $S\subseteq\Omega$가 볼록집합이며 모든 $\xi\in S$에서 $\lVert D\varphi(\xi)\rVert\leq M$이라 하자. 그럼 모든 $x,y\in S$에 대해 $\lVert\varphi(x)-\varphi(y)\rVert\leq M\lVert x-y\rVert$이다.
:::

::: 증명
$\varphi(x)=\varphi(y)$이면 자명하므로 $\varphi(x)\neq\varphi(y)$라 하고, $u=\bigl(\varphi(x)-\varphi(y)\bigr)/\lVert\varphi(x)-\varphi(y)\rVert$로 둔다. 실숫값 함수 $\psi(t)=u\cdot\varphi\bigl(y+t(x-y)\bigr)$는 $[0,1]$을 포함하는 열린 구간에서 미분가능하다. $\Omega$가 열린집합이므로 $t$가 $[0,1]$ 바깥으로 조금 나가도 점 $y+t(x-y)$는 $\Omega$ 안에 있기 때문이다. [§평균값 정리와 테일러 정리, ⁋정리 3](/ko/math/analysis/mean_value_theorem#thm3){: data-lid="uomu4" }을 $\psi$에 적용하면 어떤 $\tau\in(0,1)$이 존재하여, $\xi=y+\tau(x-y)\in S$에 대해

$$\lVert\varphi(x)-\varphi(y)\rVert=\psi(1)-\psi(0)=\psi'(\tau)=u\cdot D\varphi(\xi)(x-y)\leq\lVert D\varphi(\xi)\rVert\lVert x-y\rVert\leq M\lVert x-y\rVert$$

이다. 첫 등호는 $u$의 정의에서, 첫 부등호는 [\[선형대수학\] §내적공간, ⁋명제 3](/ko/math/linear_algebra/inner_product_spaces#prop3){: data-lid="8zhze" }에서 나온다.
:::

::: 증명 (정리 1)
$A=Df(a)$, $c=\lVert A^{-1}\rVert$로 둔다. $Df$가 $a$에서 연속이므로 $a$를 중심으로 하는 닫힌 공 $\overline{B}=\overline{B}(a,r)\subseteq\Omega$를 충분히 작게 잡아 모든 $x\in\overline{B}$에서

$$\lVert Df(x)-A\rVert\leq\frac{1}{2c}$$

이 되게 할 수 있다. 여기서 $C^1$ 가정이 쓰인다. 각 $y\in\mathbb{R}^n$에 대해 사상 $\varphi_y:\Omega\to\mathbb{R}^n$을

$$\varphi_y(x)=x+A^{-1}\bigl(y-f(x)\bigr)$$

로 정의한다. $\varphi_y(x)=x$는 $A^{-1}\bigl(y-f(x)\bigr)=0$, 곧 $f(x)=y$와 동치이므로, 방정식 $f(x)=y$를 푸는 일은 $\varphi_y$의 fixed point를 찾는 일이다. $D\varphi_y(x)=I-A^{-1}Df(x)=A^{-1}\bigl(A-Df(x)\bigr)$이고 $y$에 무관하므로, $\overline{B}$ 위에서

$$\lVert D\varphi_y(x)\rVert\leq c\cdot\frac{1}{2c}=\frac{1}{2}$$

이다. $\overline{B}$가 볼록이므로 [보조정리 2](#lem2){: data-lid="xmh3k" }에 의해 모든 $x_1,x_2\in\overline{B}$에서

$$\lVert\varphi_y(x_1)-\varphi_y(x_2)\rVert\leq\frac{1}{2}\lVert x_1-x_2\rVert\tag{$\ast$}$$

이다. 상수 $1/2$은 $1$보다 작기만 하면 되는 값이고, $c$를 곱해 $1/2$로 맞춘 것이 위의 $\overline{B}$ 선택이다.

먼저 $f$가 $\overline{B}$ 위에서 단사임을 보인다. $\varphi_y(x_1)-\varphi_y(x_2)=(x_1-x_2)-A^{-1}\bigl(f(x_1)-f(x_2)\bigr)$이므로 삼각부등식과 $(\ast)$로부터

$$\lVert x_1-x_2\rVert-c\lVert f(x_1)-f(x_2)\rVert\leq\frac{1}{2}\lVert x_1-x_2\rVert$$

이고, 따라서

$$\lVert x_1-x_2\rVert\leq 2c\lVert f(x_1)-f(x_2)\rVert\tag{$\ast\ast$}$$

이다. $f(x_1)=f(x_2)$이면 $x_1=x_2$이다.

다음으로 $f(\overline{B})$가 $f(a)$의 근방을 포함함을 보인다. $\rho=r/(2c)$로 두고 $V=B\bigl(f(a),\rho\bigr)$로 놓자. $y\in V$이면 $\varphi_y(a)-a=A^{-1}\bigl(y-f(a)\bigr)$의 크기가 $c\rho=r/2$보다 작으므로, $x\in\overline{B}$에 대해

$$\lVert\varphi_y(x)-a\rVert\leq\lVert\varphi_y(x)-\varphi_y(a)\rVert+\lVert\varphi_y(a)-a\rVert<\frac{1}{2}r+\frac{1}{2}r=r$$

이 되어 $\varphi_y$는 $\overline{B}$를 열린 공 $B(a,r)$ 안으로 보낸다. $\rho$를 $r/(2c)$로 고른 이유가 이것이다. 이 값이어야 $\varphi_y$가 $\overline{B}$를 자기 자신으로 보내고, 축소사상 정리의 가정이 완성된다. $\overline{B}$는 $\mathbb{R}^n$의 닫힌집합이므로 [§완비 거리공간과 축소사상 정리, ⁋명제 2](/ko/math/analysis/contraction_mapping#prop2){: data-lid="04zmd" }에 의해 완비 거리공간이고, $\varphi_y$는 $(\ast)$에 의해 축소상수 $1/2$의 축소사상이다. [§완비 거리공간과 축소사상 정리, ⁋정리 5](/ko/math/analysis/contraction_mapping#thm5){: data-lid="9ji9i" }에 의해 $\varphi_y$는 $\overline{B}$ 안에 fixed point $x$를 하나 갖는다. 위의 계산에서 $x=\varphi_y(x)\in B(a,r)$이고 $f(x)=y$이다.

이제 $U=B(a,r)\cap f^{-1}(V)$로 둔다. $f$가 연속이므로 $U$는 열린집합이고 $a\in U$이다. 위에서 각 $y\in V$에 대해 $f(x)=y$인 $x\in\overline{B}$가 존재하고 $B(a,r)$에 속하므로 $x\in U$이며, $\overline{B}$ 위의 단사성에 의해 유일하다. 따라서 $f:U\to V$는 전단사이다. $(\ast\ast)$를 $g=f^{-1}$에 쓰면 $\lVert g(y_1)-g(y_2)\rVert\leq 2c\lVert y_1-y_2\rVert$이고, 특히 $g$는 연속이다.

$Df(x)$가 $x\in\overline{B}$에서 가역임을 확인한다. $Df(x)v=0$이면 $D\varphi_y(x)v=v-A^{-1}Df(x)v=v$이고, $\lVert D\varphi_y(x)v\rVert\leq\frac{1}{2}\lVert v\rVert$이므로 $\lVert v\rVert\leq\frac{1}{2}\lVert v\rVert$, 곧 $v=0$이다. 정방행렬의 핵이 자명하므로 [\[선형대수학\] §동형사상, ⁋정리 7](/ko/math/linear_algebra/isomorphic_vector_spaces#thm7){: data-lid="4d21s" }에 의해 $Df(x)$는 가역이다.

$g$의 미분가능성을 보인다. $y\in V$, $x=g(y)$로 두고 $y+k\in V$에 대해 $h=g(y+k)-g(y)$라 하자. $k\neq 0$이면 $g$의 단사성에 의해 $h\neq 0$이고, $f$가 $x$에서 미분가능하므로 $\rho(h)=f(x+h)-f(x)-Df(x)h$는 [§다변수 미분, ⁋정의 1](/ko/math/analysis/multivariable_differentiation#def1){: data-lid="6rqsb" }에 의해 $\lVert\rho(h)\rVert/\lVert h\rVert\to 0$ ($h\to 0$)을 만족한다. $f(x+h)-f(x)=k$이므로

$$g(y+k)-g(y)-\bigl(Df(x)\bigr)^{-1}k=h-\bigl(Df(x)\bigr)^{-1}\bigl(Df(x)h+\rho(h)\bigr)=-\bigl(Df(x)\bigr)^{-1}\rho(h)$$

이다. 한편 $\lVert h\rVert\leq 2c\lVert k\rVert$이고 $k\to 0$이면 $h\to 0$이므로, 우변의 크기를 $\lVert k\rVert$로 나눈 값은

$$\frac{\lVert\bigl(Df(x)\bigr)^{-1}\rho(h)\rVert}{\lVert k\rVert}\leq\lVert\bigl(Df(x)\bigr)^{-1}\rVert\cdot 2c\cdot\frac{\lVert\rho(h)\rVert}{\lVert h\rVert}\to 0$$

이다. 따라서 $g$는 $y$에서 미분가능하고 $Dg(y)=\bigl(Df(g(y))\bigr)^{-1}$이다.

마지막으로 $Dg$의 연속성을 보인다. $Dg$는 $y\mapsto Df(g(y))$와 가역행렬을 그 역행렬로 보내는 사상의 합성이다. 앞의 것은 $g$와 $Df$가 연속이므로 연속이고, 뒤의 것은 역행렬의 성분이 수반행렬을 행렬식으로 나눈 값이라 원래 성분의 유리함수이므로 연속이다. 따라서 $g$는 $C^1$이다.
:::

위의 증명에서 $C^1$ 가정은 두 번 쓰였다. 하나는 $a$ 근방에서 $\lVert Df(x)-A\rVert$를 작게 만들어 축소상수를 확보하는 데 쓰였고, 다른 하나는 $Dg$의 연속성에 쓰였다. 둘째 용법에서 더 나아가, $f$가 $C^k$이면 $g$도 $C^k$이다. $Dg=\operatorname{inv}\circ Df\circ g$이고 $\operatorname{inv}$는 $C^\infty$이므로, $g$가 $C^j$ ($j<k$)이면 우변이 $C^j$여서 $g$가 $C^{j+1}$이 되고, $j=1$에서 귀납하면 된다.

또 [정리 1](#thm1){: data-lid="3juga" }은 열린집합 $\Omega$ 위의 $C^1$ 사상 $f$가 모든 점에서 $Df$가 가역이고 전체에서 단사이면 $f(\Omega)$가 열린집합이고 $f^{-1}:f(\Omega)\to\Omega$가 $C^1$임을 준다. 각 점의 근방에서 [정리 1](#thm1){: data-lid="71xbl" }의 역사상이 $f^{-1}$과 일치하기 때문이다.

## 국소성과 $C^1$ 가정

[정리 1](#thm1){: data-lid="pv7vp" }이 주는 가역성은 국소적일 뿐이다. 모든 점에서 $Df$가 가역이어도 $f$가 전체에서 단사일 필요는 없다.

::: 예시 3 (국소 가역이나 전역 단사가 아닌 사상)
$f(x,y)=(e^x\cos y, e^x\sin y)$는 복소지수함수 $z\mapsto e^z$를 $\mathbb{R}^2=\mathbb{C}$ 위에서 쓴 것이다. 야코비 행렬은

$$Df(x,y)=e^x\begin{pmatrix}\cos y&-\sin y\\ \sin y&\cos y\end{pmatrix},\qquad\det Df(x,y)=e^{2x}>0$$

이므로 모든 점에서 가역이다. [정리 1](#thm1){: data-lid="v8o49" }에 의해 모든 점이 $f$가 단사인 근방을 갖는다. 그러나 $f(x,y+2\pi)=f(x,y)$이므로 $f$는 $\mathbb{R}^2$ 전체에서 단사가 아니다. 점 $(x_0,y_0)$ 근방의 역사상은 $\mathbb{R}\times(y_0-\pi,y_0+\pi)$ 위에서 극좌표의 각을 $(y_0-\pi,y_0+\pi)$에서 고른 것에 해당하며, 근방을 $y$ 방향으로 $2\pi$ 이상 늘리면 역사상이 존재하지 않는다.
:::

다음은 $C^1$ 가정을 미분가능성으로 약화할 수 없음을 보이는 한 변수 반례이다. $f'(a)\neq 0$이라는 조건만으로는 부족하고, $f'$이 $a$에서 연속이어야 한다.

::: 예시 4 ($C^1$이 아닌 경우의 반례)
$f(x)=x+2x^2\sin(1/x)$ ($x\neq 0$), $f(0)=0$으로 정의한다. $h\neq 0$에서 $f(h)/h=1+2h\sin(1/h)\to 1$이므로 $f$는 $0$에서 미분가능하고 $f'(0)=1$이다. $x\neq 0$에서는

$$f'(x)=1+4x\sin\frac{1}{x}-2\cos\frac{1}{x}$$

이므로 $f$는 $\mathbb{R}$ 전체에서 미분가능하다. 그러나 $x_k=1/(2\pi k)$에서 $\sin(1/x_k)=0$, $\cos(1/x_k)=1$이어서 $f'(x_k)=-1$이고 $x_k\to 0$이므로, $f'$은 $0$에서 연속이 아니다.

$0$의 어떤 근방에서도 $f$는 단사가 아니다. $0$을 포함하는 열린 구간 $I$ 위에서 $f$가 단사라 하자. $f$는 연속이므로 [§연결성과 중간값 정리, ⁋따름정리 4](/ko/math/analysis/connectedness#cor4){: data-lid="kjwsu" }에 의해 $I$ 위에서 순단조이다. $f'(0)=1>0$이므로 순증가이고, 따라서 $I$ 위에서 $f'\geq 0$이다. 그런데 $k$가 충분히 크면 $x_k\in I$이고 $f'(x_k)=-1$이어서 모순이다. 여기서 $f'(0)\neq 0$이고 $f$가 어디서나 미분가능하지만 역함수 정리의 결론은 성립하지 않는다.
:::

한 변수의 증명 구조와 비교하면 이유가 분명하다. $f'$이 연속이면 $f'(a)>0$이 $a$ 근방에서 유지되어 단조성이 따라 나오지만, 위의 $f$는 $0$ 바로 옆에서 $f'$이 $-1$까지 내려가 단조성이 깨진다. [정리 1](#thm1){: data-lid="0fvm2" }의 증명에서는 같은 일이 $\lVert Df(x)-A\rVert\leq 1/(2c)$를 만족하는 근방이 존재하지 않는 형태로 나타난다.

## 음함수 정리

방정식 $F(x,y)=0$이 주어졌을 때, 점 $(a,b)$ 근방에서 $y$를 $x$의 함수로 풀 수 있는 조건을 역함수 정리로부터 얻는다. $\mathbb{R}^{n+m}=\mathbb{R}^n\times\mathbb{R}^m$의 점을 $(x,y)$로 적고, $F$의 미분 $DF(a,b)$를 $x$ 방향 블록 $D_xF(a,b)$($m\times n$ 행렬)와 $y$ 방향 블록 $D_yF(a,b)$($m\times m$ 행렬)로 나눈다.

::: 정리 5 (음함수 정리)
$\Omega\subseteq\mathbb{R}^n\times\mathbb{R}^m$이 열린집합, $F:\Omega\to\mathbb{R}^m$이 $C^1$ 사상이고 $F(a,b)=0$이며 $D_yF(a,b)$가 가역이라 하자. 그럼 $a$의 열린 근방 $W\subseteq\mathbb{R}^n$, $b$의 열린 근방 $W'\subseteq\mathbb{R}^m$, 그리고 $C^1$ 사상 $g:W\to W'$이 존재하여 $g(a)=b$이고, $(x,y)\in W\times W'$에 대해

$$F(x,y)=0\iff y=g(x)$$

이다. 또 $Dg(x)=-\bigl(D_yF(x,g(x))\bigr)^{-1}D_xF(x,g(x))$이다.
:::

::: 증명
$\Phi(x,y)=\bigl(x,F(x,y)\bigr)$로 정의된 $C^1$ 사상 $\Phi:\Omega\to\mathbb{R}^n\times\mathbb{R}^m$을 생각한다. 이 사상의 미분은

$$D\Phi(a,b)=\begin{pmatrix}I_n&0\\ D_xF(a,b)&D_yF(a,b)\end{pmatrix}$$

이고 블록 하삼각행렬이므로 [\[선형대수학\] §행렬식의 존재성과 유일성, ⁋따름정리 10](/ko/math/linear_algebra/existence_and_uniqueness_of_determinant#cor10){: data-lid="rpa92" }에 의해 $\det D\Phi(a,b)=\det D_yF(a,b)\neq 0$이다. [정리 1](#thm1){: data-lid="uuzyu" }을 $\Phi$에 적용하면 $(a,b)$의 열린 근방 $\mathcal{U}$와 $\Phi(a,b)=(a,0)$의 열린 근방 $\mathcal{V}$가 있어 $\Phi:\mathcal{U}\to\mathcal{V}$가 전단사이고 역사상 $\Psi$가 $C^1$이다. $\Phi$는 첫 성분을 바꾸지 않으므로 $\Psi(x,z)=\bigl(x,h(x,z)\bigr)$ 꼴이다. $(x,0)\in\mathcal{V}$인 $x$에 대해 $g(x)=h(x,0)$으로 두면 $g$는 $C^1$이고 $\Phi\bigl(x,g(x)\bigr)=(x,0)$, 곧 $F(x,g(x))=0$이다.

$\mathcal{U}$는 열린집합이므로 $W_0\times W'\subseteq\mathcal{U}$인 열린 근방 $W_0\ni a$, $W'\ni b$를 잡을 수 있다. $g$의 정의역은 열린집합이고 $g$가 연속이며 $g(a)=b$이므로, $W=\{x\in W_0\mid(x,0)\in\mathcal{V}, g(x)\in W'\}$는 $a$를 포함하는 열린집합이다. $x\in W$, $y\in W'$이고 $F(x,y)=0$이라 하면 $(x,y)$와 $(x,g(x))$가 모두 $\mathcal{U}$에 속하고 $\Phi$에 의한 상이 $(x,0)$으로 같다. $\Phi$가 $\mathcal{U}$ 위에서 단사이므로 $y=g(x)$이다.

미분 공식은 $F(x,g(x))=0$의 양변에 [§다변수 미분, ⁋정리 7](/ko/math/analysis/multivariable_differentiation#thm7){: data-lid="q7dxy" }을 적용해 미분한 $D_xF+D_yF\cdot Dg=0$을 $D_yF$가 가역임을 써서 풀면 된다. $W$를 더 줄이면 모든 $x\in W$에서 $D_yF(x,g(x))$가 가역이다. 이는 $\det D_yF$가 연속이고 $(a,b)$에서 $0$이 아니기 때문이다.
:::

미분 공식은 한 변수에서 친숙한 음함수 미분 $\dd{y}/\dd{x}=-F_x/F_y$의 다변수 꼴이다. 방정식을 명시적으로 풀지 않고도 $g$의 미분을 얻는다는 점이 이 정리의 실용성이다.

단위원 $F(x,y)=x^2+y^2-1$에서 $D_yF=2y$이다. $b\neq 0$인 점 $(a,b)$ 근방에서 원은 $y=g(x)$의 그래프이고 $g'(x)=-x/g(x)$이다. $b=0$인 점 $(\pm 1,0)$에서는 가정이 깨지고 실제로 원이 수직 접선을 가져, 어떤 근방에서도 $y$를 $x$의 함수로 쓸 수 없다. 그런데 이 점에서 $D_xF=2x\neq 0$이므로 역할을 바꾼 [정리 5](#thm5){: data-lid="787pd" }에 의해 $x$를 $y$의 함수로 쓸 수 있다.

가정 $D_yF(a,b)$의 가역성은 충분조건이지 필요조건이 아니다. $F(x,y)=y^3-x$는 $(0,0)$에서 $D_yF=0$이지만 $y=x^{1/3}$으로 풀린다. 다만 이 해는 $0$에서 미분가능하지 않으므로, [정리 5](#thm5){: data-lid="vwf8b" }가 보장하는 $C^1$ 해는 가정이 성립할 때에 한한다.

### 등위집합의 tangent space

[정리 5](#thm5){: data-lid="7a2zi" }는 방정식의 해집합이 국소적으로 그래프임을 말하며, 따라서 해집합의 tangent space를 미분으로 기술할 수 있다. $G:\Omega\to\mathbb{R}^m$이 $\Omega\subseteq\mathbb{R}^N$ 위의 $C^1$ 사상이고 $M=\{G=0\}$, $p\in M$에서 $DG(p)$의 rank가 $m$이라 하자. $M$ 안의 $p$를 지나는 $C^1$ 곡선 $\gamma$의 속도 $\gamma'(0)$들을 모은 집합을 $p$에서의 *tangent space*라 부른다.

::: 명제 6 (등위집합의 tangent space)
위의 설정에서 $p$에서의 tangent space는 $\ker DG(p)$이고, 차원은 $N-m$이다.
:::

::: 증명
$M$ 안의 곡선 $\gamma$에 대해 $G(\gamma(t))=0$에 [§다변수 미분, ⁋정리 7](/ko/math/analysis/multivariable_differentiation#thm7){: data-lid="ywnob" }을 적용해 $t=0$에서 미분하면 $DG(p)\gamma'(0)=0$이므로, tangent space는 $\ker DG(p)$에 포함된다. 반대 방향을 보이기 위해 좌표를 재배열해 $D_yG(p)$가 가역이 되도록 한다. rank가 $m$이므로 일차독립인 열 $m$개를 $y$ 좌표로 잡을 수 있다. $p=(a,b)$로 쓰고 [정리 5](#thm5){: data-lid="qbw01" }의 $g$를 취하면, $p$ 근방에서 $M$은 $g$의 그래프이다. $v=(v_x,v_y)\in\ker DG(p)$이면 $D_xG v_x+D_yG v_y=0$이므로 $v_y=-D_yG^{-1}D_xG v_x=Dg(a)v_x$이다. 곡선 $\gamma(t)=\bigl(a+tv_x, g(a+tv_x)\bigr)$는 $\lvert t\rvert$가 작을 때 $M$ 안에 있고 $\gamma'(0)=(v_x,Dg(a)v_x)=v$이다. $DG(p)$의 rank가 $m$이므로 [\[선형대수학\] §동형사상, ⁋정리 7](/ko/math/linear_algebra/isomorphic_vector_spaces#thm7){: data-lid="gub40" }에 의해 $\dim\ker DG(p)=N-m$이다.
:::

원 $x^2+y^2=1$의 점 $p=(a,b)$에서 $DG(p)=(2a,2b)\neq 0$이므로 tangent space는 $\ker DG(p)=\{(v_1,v_2)\mid av_1+bv_2=0\}$이고, $p$를 지나는 접선은 $a(x-a)+b(y-b)=0$, 곧 $ax+by=1$이다. 구 $x^2+y^2+z^2=1$의 점 $p=(a,b,c)$에서도 같은 계산으로 접평면 $ax+by+cz=1$을 얻는다. 일반적으로 $m=1$이면 tangent space는 기울기 벡터 $\nabla G(p)$에 수직인 초평면이다.

## Lagrange 승수법

제약조건 아래의 극값 문제에 [명제 6](#prop6){: data-lid="wr0ak" }의 tangent space 기술이 쓰인다. $G:\Omega\to\mathbb{R}^m$이 $\Omega\subseteq\mathbb{R}^N$ 위의 $C^1$ 사상, $m<N$이고 $M=\{G=0\}$일 때, $C^1$ 함수 $f:\Omega\to\mathbb{R}$가 $p\in M$에서 $M$ 위의 *극값*을 갖는다는 것은 $p$의 어떤 근방 $N_p$에서 모든 $q\in M\cap N_p$에 대해 $f(q)\leq f(p)$ 또는 모든 $q\in M\cap N_p$에 대해 $f(q)\geq f(p)$임을 뜻한다.

::: 정리 7 (Lagrange 승수법)
$f$가 $p\in M$에서 $M$ 위의 극값을 갖고 $DG(p)$의 rank가 $m$이면, $\lambda_1,\dots,\lambda_m\in\mathbb{R}$이 존재하여

$$Df(p)=\sum_{i=1}^m\lambda_i DG_i(p)$$

이다. 곧 $\nabla f(p)$는 $\nabla G_1(p),\dots,\nabla G_m(p)$의 일차결합이다.
:::

::: 증명
좌표를 재배열해 $\mathbb{R}^N=\mathbb{R}^n\times\mathbb{R}^m$, $p=(a,b)$, $D_yG(p)$가 가역이 되도록 한다. [정리 5](#thm5){: data-lid="adxl7" }에 의해 $a$의 근방 $W$ 위의 $C^1$ 사상 $g$가 있어 $p$ 근방에서 $M$은 $g$의 그래프이다. $h(x)=f(x,g(x))$로 두면 $h$는 $C^1$이고, $g$의 연속성에 의해 $x$가 $a$에 충분히 가까울 때 점 $(x,g(x))\in M$이 $p$의 극값 근방 $N_p$ 안에 들어오므로 $h$는 $a$에서 극값을 갖는다. 각 좌표 방향으로 $t\mapsto h(a+te_i)$가 $t=0$에서 한 변수 함수의 극값을 가지므로 [§미분, ⁋명제 5](/ko/math/analysis/differentiation#prop5){: data-lid="x63ci" }에 의해 $Dh(a)=0$이다. [§다변수 미분, ⁋정리 7](/ko/math/analysis/multivariable_differentiation#thm7){: data-lid="hsv0s" }에 의해

$$D_xf(p)+D_yf(p) Dg(a)=0,\qquad Dg(a)=-D_yG(p)^{-1}D_xG(p)$$

이다. 행벡터 $\lambda=D_yf(p) D_yG(p)^{-1}\in\mathbb{R}^m$을 잡으면 $D_yf(p)=\lambda D_yG(p)$이고, 위의 식으로부터 $D_xf(p)=D_yf(p) D_yG(p)^{-1}D_xG(p)=\lambda D_xG(p)$이다. 따라서 $Df(p)=\lambda DG(p)$이다.
:::

[정리 7](#thm7){: data-lid="yczbg" }은 필요조건이다. 제약조건 집합이 컴팩트이면 [§연속함수의 성질, ⁋따름정리 2](/ko/math/analysis/continuous_functions#cor2){: data-lid="7bluo" }에 의해 $f$가 최댓값과 최솟값을 가지므로, [정리 7](#thm7){: data-lid="0qv32" }의 조건과 $DG$의 rank 조건이 깨지는 점을 모두 후보로 모아 $f$ 값을 비교해 극값을 결정한다. 예를 들어 단위원 위에서 $f(x,y)=x+y$의 극값은 $(1,1)=\lambda(2x,2y)$와 $x^2+y^2=1$에서 $x=y=\pm 1/\sqrt{2}$로 후보가 둘 남고, 최댓값 $\sqrt{2}$와 최솟값 $-\sqrt{2}$를 갖는다.

rank 조건은 생략할 수 없다.

::: 예시 8 (rank 조건이 깨진 경우)
$G(x,y)=y^2-x^3$, $f(x,y)=x$로 둔다. $M=\{y^2=x^3\}$ 위에서 $x\geq 0$이므로 $f$는 $(0,0)$에서 $M$ 위의 최솟값 $0$을 갖는다. 그런데 $DG(x,y)=(-3x^2, 2y)$이므로 $DG(0,0)=(0,0)$이어서 rank가 $0$이고, $Df(0,0)=(1,0)$은 $DG(0,0)$의 어떤 배수도 아니다. [정리 7](#thm7){: data-lid="yggip" }의 결론이 성립하지 않는 이유는 $M$이 원점에서 뾰족점(cusp)을 가져 [명제 6](#prop6){: data-lid="urjn5" }의 그래프 구조가 없기 때문이다.
:::

---

**참고문헌**

**[Rud]** W. Rudin, *Principles of mathematical analysis*, 3rd ed., McGraw-Hill, 1976.
