---
title: "지수함수, 로그, 거듭제곱"
description: "멱급수로 정의된 지수함수의 덧셈정리, 주기성, 치역을 정리하고 복소 삼각함수와 쌍곡함수의 성질을 다룬다. 다가함수 arg와 log를 정의하여 분지와 분지절단, 주치 로그의 정칙성을 보이고, 이를 바탕으로 거듭제곱 z^a와 제곱근의 분지를 분석한다."
excerpt: "지수함수의 주기성, 복소 삼각함수, arg와 log, 분지와 분지절단, 주치 로그, 거듭제곱, 제곱근"

categories: [Math / Complex Analysis]
permalink: /ko/math/complex_analysis/elementary_functions
sidebar: 
    nav: "complex_analysis-ko"

date: 2026-10-13
weight: 3

published: false

---

[§복소정칙함수, ⁋정의 10](/ko/math/complex_analysis/holomorphic_functions#def10)에서 지수함수 $e^z=\sum_{n\ge 0}z^n/n!$과 $\cos z$, $\sin z$를 멱급수로 정의했고, 이들이 entire function이며 $(e^z)'=e^z$이고 Euler 공식 $e^{iz}=\cos z+i\sin z$가 성립함을 보았다. 이 글에서는 이 함수들의 대수적 성질을 먼저 정리한다. 실수에서 $e^x$는 단사이고 치역이 $(0,\infty)$이어서 역함수 $\ln$이 존재하지만, 복소수에서는 $e^z$가 주기를 가지므로 이 사정이 달라진다. 역함수가 하나의 함수로 정의되지 않고 $2\pi i$의 정수배만큼의 모호함을 갖는다는 사실에서 분지(branch)의 개념이 나오며, 거듭제곱 $z^a=e^{a\log z}$와 제곱근은 모두 이 모호함을 물려받는다.

## 지수함수의 덧셈정리와 주기

::: 명제 1
모든 $z,w\in\mathbb{C}$에 대하여 $e^{z+w}=e^ze^w$이다. 특히 $e^z e^{-z}=1$이므로 $e^z\ne 0$이다.
:::

::: 증명
$w$를 고정하고 entire function $g(z)=e^ze^{w-z}$를 생각한다. 곱과 합성에 대한 [§복소정칙함수, ⁋명제 3](/ko/math/complex_analysis/holomorphic_functions#prop3)과 $(e^z)'=e^z$에 의하여

$$g'(z)=e^ze^{w-z}-e^ze^{w-z}=0$$

이다. 임의의 $z$에 대하여 $h(t)=g(tz)$ ($t\in[0,1]$)로 두면 $h'(t)=zg'(tz)=0$이므로 [\[해석학\] §평균값 정리와 테일러 정리, ⁋따름정리 4](/ko/math/analysis/mean_value_theorem#cor4)에 의하여 $\Real h$와 $\Img h$가 모두 상수이고, 따라서 $g(z)=h(1)=h(0)=g(0)=e^w$이다. 즉 모든 $z,w$에 대해 $e^ze^{w-z}=e^w$이고, $w$ 자리에 $z+w$를 넣으면 $e^ze^w=e^{z+w}$를 얻는다. $w=-z$를 넣으면 $e^ze^{-z}=e^0=1$이다.
:::

$z=x+iy$ ($x,y$는 실수)이면 [명제 1](#prop1)과 Euler 공식에 의하여

$$e^z=e^xe^{iy}=e^x(\cos y+i\sin y)$$

이다. 따라서 $\lvert e^z\rvert=e^{\Real z}$이고 $\Img z$는 $e^z$의 편각 중 하나이다. 실수부는 크기만, 허수부는 방향만 결정한다. 이로부터 $e^z$가 어떤 값을 몇 번 취하는지가 곧바로 읽힌다.

::: 명제 2
(i) $e^z=e^w$인 것은 $z-w\in 2\pi i\mathbb{Z}$인 것과 동치이다. 특히 $e^z$는 주기 $2\pi i$를 갖는다.

(ii) $e^z$의 치역은 $\mathbb{C}\setminus\{0\}$이다.
:::

::: 증명
(i) [명제 1](#prop1)에 의하여 $e^z=e^w$는 $e^{z-w}=1$과 동치이다. $\zeta=s+it$에 대하여 $e^\zeta=1$이면 $\lvert e^\zeta\rvert=e^s=1$에서 $s=0$이고, $e^{it}=\cos t+i\sin t=1$에서 $\cos t=1$, $\sin t=0$이므로 $t\in 2\pi\mathbb{Z}$이다. 역으로 $\zeta=2\pi ik$이면 $e^\zeta=\cos 2\pi k+i\sin 2\pi k=1$이다.

(ii) [명제 1](#prop1)에서 $e^z\ne 0$이다. $w\ne 0$이면 $w=re^{i\theta}$ ($r=\lvert w\rvert>0$, $\theta$는 $w$의 편각)로 쓸 수 있고 ([§복소수와 복소평면, ⁋정의 5](/ko/math/complex_analysis/complex_numbers#def5)), $z=\ln r+i\theta$로 두면 $e^z=re^{i\theta}=w$이다.
:::

[명제 2](#prop2)는 $e^z$가 $\mathbb{C}$ 전체에서는 단사가 아님을 말한다. 수평 띠 $\{a<\Img z\le a+2\pi\}$ 위로 제한하면 $e^z$는 $\mathbb{C}\setminus\{0\}$ 위로의 일대일대응이 되지만, 이 띠의 선택에는 $a$만큼의 자유가 있다. 이 자유가 아래 로그의 분지 선택에 그대로 대응한다. 실수축 위에서는 이런 현상이 없으므로, 실수에서 익숙한 지수법칙 중 역함수에 관련된 것은 모두 복소수에서 주의가 필요하다.

## 삼각함수와 쌍곡함수

$\cos z$는 우함수이고 $\sin z$는 기함수이므로 Euler 공식에 $-z$를 넣으면 $e^{-iz}=\cos z-i\sin z$이다. 이 식을 $e^{iz}=\cos z+i\sin z$와 더하고 빼면

$$\cos z=\frac{e^{iz}+e^{-iz}}{2},\qquad \sin z=\frac{e^{iz}-e^{-iz}}{2i}$$

를 얻는다. 쌍곡함수는 $\cosh z=(e^z+e^{-z})/2$, $\sinh z=(e^z-e^{-z})/2$로 정의한다. 실수 $y$에 대하여 위 식에서 $\cos(iy)=\cosh y$, $\sin(iy)=i\sinh y$이다.

[명제 1](#prop1)에서 $e^{iz}e^{-iz}=1$이므로 $(\cos z+i\sin z)(\cos z-i\sin z)=1$, 곧 $\cos^2z+\sin^2z=1$이 모든 복소수 $z$에서 성립한다. 또 $e^{i(z+w)}=e^{iz}e^{iw}$를 전개한 식과, $(z,w)$를 $(-z,-w)$로 바꾼 식을 더하고 빼면 실수에서와 같은 덧셈공식

$$\cos(z+w)=\cos z\cos w-\sin z\sin w,\qquad \sin(z+w)=\sin z\cos w+\cos z\sin w$$

를 얻는다. 실수에서 성립하던 삼각함수 항등식은 이처럼 모두 지수함수의 성질에서 따라 나오고, 같은 이유로 복소수 전체에서 유지된다. 그러나 크기에 관해서는 실수와 전혀 다르다.

::: 명제 3
$z=x+iy$ ($x,y$는 실수)라 하자.

(i) $\sin z=\sin x\cosh y+i\cos x\sinh y$, $\cos z=\cos x\cosh y-i\sin x\sinh y$이고, $\lvert\sin z\rvert^2=\sin^2x+\sinh^2y$, $\lvert\cos z\rvert^2=\cos^2x+\sinh^2y$이다.

(ii) $\sin z=0$인 것은 $z\in\pi\mathbb{Z}$인 것과 동치이고, $\cos z=0$인 것은 $z\in\pi/2+\pi\mathbb{Z}$인 것과 동치이다. 곧 영점은 모두 실수이다.

(iii) $\sin z$와 $\cos z$는 $\mathbb{C}$에서 유계가 아니며, 각각 모든 복소수 값을 취한다.
:::

::: 증명
(i) 덧셈공식에 $\cos(iy)=\cosh y$, $\sin(iy)=i\sinh y$를 대입하면 앞의 두 식을 얻는다. 그러면 $\cosh^2y=1+\sinh^2y$이므로

$$\begin{aligned}
\lvert\sin z\rvert^2&=\sin^2x\cosh^2y+\cos^2x\sinh^2y\\
&=\sin^2x(1+\sinh^2y)+\cos^2x\sinh^2y=\sin^2x+\sinh^2y
\end{aligned}$$

이다. $\cos z$도 같은 방식이다.

(ii) $\sin z=0$은 $e^{iz}=e^{-iz}$, 곧 $e^{2iz}=1$과 같고, [명제 2](#prop2)에 의하여 이는 $2iz\in 2\pi i\mathbb{Z}$, 곧 $z\in\pi\mathbb{Z}$와 동치이다. $\cos z=0$은 $e^{2iz}=-1=e^{i\pi}$와 같고 [명제 2](#prop2)에 의하여 $2iz-i\pi\in 2\pi i\mathbb{Z}$, 곧 $z\in\pi/2+\pi\mathbb{Z}$와 동치이다.

(iii) (i)에서 $\lvert\sin(iy)\rvert=\sinh\lvert y\rvert$, $\lvert\cos(iy)\rvert=\cosh y$이고 이들은 $\lvert y\rvert\to\infty$일 때 발산한다. 값의 표현성은 $\cos z$에 대해 보인다. $w\in\mathbb{C}$에 대하여 $\cos z=w$는 $\zeta=e^{iz}$에 대한 방정식 $\zeta^2-2w\zeta+1=0$과 같다. 이 이차방정식의 두 근의 곱이 $1$이므로 해 $\zeta$는 $0$이 아니고, [명제 2](#prop2)에 의하여 $e^{iz}=\zeta$인 $z$가 존재한다. $\sin z=\cos(z-\pi/2)$이므로 $\sin z$도 같다.
:::

실수에서 $\lvert\sin x\rvert\le 1$이므로, 허수축 방향으로 $\sin$이 지수적으로 커진다는 (iii)은 복소 삼각함수가 실수 삼각함수의 단순한 연장이 아님을 보여 준다. 또 (ii)는 허수 방향으로 새로운 영점이 생기지 않음을 말하므로, $\tan z=\sin z/\cos z$는 $\pi/2+\pi\mathbb{Z}$를 제외한 $\mathbb{C}$에서 holomorphic이다.

## 다가함수 arg와 log

실수 $x>0$에 대하여 $\ln x$는 $e^t=x$의 유일한 해이다. 복소수 $z\ne 0$에 대하여 방정식 $e^w=z$를 풀면, [명제 2](#prop2)에 의하여 해가 존재하고 서로 $2\pi i\mathbb{Z}$만큼 다르다. 이 해집합을 로그의 값으로 삼는다.

::: 정의 4
$z\ne 0$에 대하여 $z=\lvert z\rvert e^{i\theta}$를 만족하는 실수 $\theta$ 전체의 집합을 $\arg z$라 쓰고, $e^w=z$를 만족하는 $w$ 전체의 집합을 $\log z$라 쓴다. 이들은 각각 하나의 수가 아니라 집합이며, 이런 대응을 *다가함수<sub>multivalued function</sub>*라 부른다. $\arg z$의 원소 중 $(-\pi,\pi]$에 속하는 유일한 값을 $\operatorname{Arg}z$라 하고, 

$$\operatorname{Log}z=\ln\lvert z\rvert+i\operatorname{Arg}z$$

를 $z$의 *주치 로그<sub>principal logarithm</sub>*라 한다.
:::

$\arg z=\operatorname{Arg}z+2\pi\mathbb{Z}$이고, $e^w=z$는 $\lvert z\rvert=e^{\Real w}$와 $\Img w\in\arg z$로 쪼개지므로

$$\log z=\ln\lvert z\rvert+i\arg z=\operatorname{Log}z+2\pi i\mathbb{Z}$$

이다. $0$에서는 $\arg$와 $\log$가 정의되지 않는다. $z>0$이면 $\operatorname{Log}z=\ln z$이다. 실수의 $\ln(xy)=\ln x+\ln y$에 해당하는 식은 집합으로는 성립한다. $\arg(zw)=\arg z+\arg w$ (두 집합의 원소끼리의 합 전체)이기 때문이다. 그러나 이 식은 주치값에서 깨진다.

::: 예시 5 ($\operatorname{Log}(zw)\ne\operatorname{Log}z+\operatorname{Log}w$)
$z=w=e^{3\pi i/4}$로 두면 $\operatorname{Arg}z=\operatorname{Arg}w=3\pi/4$이므로 $\operatorname{Log}z+\operatorname{Log}w=3\pi i/2$이다. 한편 $zw=e^{3\pi i/2}=-i$이고 $\operatorname{Arg}(zw)=-\pi/2$이므로 $\operatorname{Log}(zw)=-\pi i/2$이다. 두 값은 $2\pi i$만큼 다르다. 일반적으로 $\operatorname{Arg}z+\operatorname{Arg}w\in(-2\pi,2\pi]$가 $(-\pi,\pi]$를 벗어날 때마다 식이 깨지고, 그 오차는 $2\pi i$의 정수배이다.
:::

## 분지와 분지절단

다가함수의 값 중 하나를 연속적으로 골라 하나의 함수로 만들 수 있는지가 문제이다.

::: 정의 6
영역 $\Omega\subseteq\mathbb{C}\setminus\{0\}$ 위의 연속함수 $L:\Omega\to\mathbb{C}$가 모든 $z\in\Omega$에서 $e^{L(z)}=z$를 만족하면, $L$을 $\Omega$ 위의 $\log$의 *분지<sub>branch</sub>*라 한다.
:::

분지는 $L(z)\in\log z$를 연속적으로 고른 것이다. 그 허수부 $\Img L(z)\in\arg z$는 $\arg$의 연속적인 선택이 된다. 연속성만 요구해도 holomorphic함이 자동으로 따라 나온다.

::: 명제 7
$L$이 $\Omega$ 위의 $\log$의 분지이면 $L$은 holomorphic이고 $L'(z)=1/z$이다. 또 $L_1,L_2$가 $\Omega$ 위의 분지이면 어떤 정수 $k$가 있어 $L_1-L_2=2\pi ik$이다.
:::

::: 증명
$z_0\in\Omega$을 잡고 $w_0=L(z_0)$이라 하자. $z\ne z_0$이면 $e^{L(z)}=z\ne z_0=e^{w_0}$이므로 $w=L(z)\ne w_0$이고, $L$이 연속이므로 $z\to z_0$일 때 $w\to w_0$이다. 따라서

$$\frac{L(z)-L(z_0)}{z-z_0}=\frac{w-w_0}{e^w-e^{w_0}}$$

에서 $(e^w-e^{w_0})/(w-w_0)\to e^{w_0}\ne 0$이므로 우변은 $1/e^{w_0}=1/z_0$로 수렴한다.

유일성을 보이자. $e^{L_1-L_2}=z/z=1$이므로 [명제 2](#prop2)에 의하여 $L_1-L_2$는 discrete set $2\pi i\mathbb{Z}$의 값을 갖는 연속함수이다. $\Omega$가 연결이므로 [\[해석학\] §연결성과 중간값 정리, ⁋정리 3](/ko/math/analysis/connectedness#thm3)에 의하여 그 치역은 연결집합이고, discrete set의 연결subset은 한 점이므로 $L_1-L_2$는 상수이다.
:::

분지가 존재하는 대표적인 정의역은 원점에서 뻗는 ray 하나를 뺀 평면이다. 가장 표준적인 선택은 음의 실수축 $(-\infty,0]$를 빼는 것이고, 이때 분지는 주치 로그이다.

::: 정리 8 (주치 로그)
$\operatorname{Log}$는 $\mathbb{C}\setminus(-\infty,0]$ 위에서 $\log$의 분지이며, 따라서 holomorphic이고 $\operatorname{Log}'z=1/z$이다. 또 $\operatorname{Log}$는 음의 실수축의 모든 점에서 불연속이다.
:::

::: 증명
$z=x+iy\notin(-\infty,0]$이고 $r=\lvert z\rvert$라 하자. 이때 $r+x>0$이다. $z=re^{i\theta}$ ($\theta=\operatorname{Arg}z\in(-\pi,\pi)$)이면

$$\frac{y}{r+x}=\frac{r\sin\theta}{r+r\cos\theta}=\tan\frac{\theta}{2}$$

이고 $\theta/2\in(-\pi/2,\pi/2)$이므로 $\operatorname{Arg}z=2\arctan\bigl(y/(r+x)\bigr)$이다. 우변은 $\mathbb{C}\setminus(-\infty,0]$에서 연속이므로 $\operatorname{Arg}$가, 따라서 $\operatorname{Log}$가 연속이다. $e^{\operatorname{Log}z}=z$는 정의에서 나오므로 분지이고, 나머지는 [명제 7](#prop7)이다.

불연속성은 $x<0$에서 $y\to 0^+$일 때 $r+x=y^2/(r-x)$이므로 $y/(r+x)=(r-x)/y\to+\infty$이고 $\operatorname{Arg}(x+iy)\to\pi$이며, $y\to 0^-$이면 $-\pi$로 가는 데서 따른다. 두 극한의 허수부가 $\pm\pi$로 달라 $\operatorname{Log}$는 연속일 수 없다.
:::

이때 뺀 ray $(-\infty,0]$를 이 분지의 *분지절단<sub>branch cut</sub>*이라 한다. 분지절단은 $\log$가 유일하게 정의되지 않는다는 사실의 흔적이며, 절단선 자체는 절대적인 것이 아니다. 실수 $\alpha$에 대하여 ray $\{te^{i\alpha}:t\ge 0\}$를 뺀 평면 위에서 $z=re^{i\theta}$ ($\alpha<\theta<\alpha+2\pi$)에 $\ln r+i\theta$를 대응시키면 $\operatorname{Log}$와 같은 방식으로 연속이고, 이는 [정리 8](#thm8)의 $\operatorname{Log}$를 $e^{-i(\alpha+\pi)}z$에 적용하고 $i(\alpha+\pi)$를 더한 것과 같다. 곧 절단선은 원점에서 무한대로 가는 임의의 ray (혹은 곡선)으로 바꿀 수 있고, 절단선을 바꾸면 분지가 바뀐다. 한편 절단선을 아무리 줄이거나 옮겨도 원점을 한 바퀴 도는 폐곡선을 포함하는 영역에서는 분지가 존재할 수 없다.

::: 정리 9
$\Omega\subseteq\mathbb{C}\setminus\{0\}$이 어떤 원 $\{\lvert z\rvert=r\}$을 포함하면 $\Omega$ 위에서는 $\log$의 분지가 존재하지 않는다. 특히 $\mathbb{C}\setminus\{0\}$ 위에는 분지가 없다.
:::

::: 증명
$L$이 $\Omega$ 위의 분지라고 가정한다. $t\in[0,2\pi]$에 대하여 $e^{L(re^{it})}=re^{it}=e^{\ln r+it}$이므로 [명제 2](#prop2)에 의하여 $c(t)=L(re^{it})-\ln r-it\in 2\pi i\mathbb{Z}$이다. $c$는 연속이고 discrete set의 값을 가지므로, [\[해석학\] §연결성과 중간값 정리, ⁋정리 3](/ko/math/analysis/connectedness#thm3)에 의하여 $c([0,2\pi])$가 연결집합이고 따라서 $c$는 상수 $2\pi ik$이다. 그런데 $re^{i0}=re^{2\pi i}$이므로 $L(re^{i0})=L(re^{2\pi i})$이어야 하지만, 위의 식에서 $L(re^{i0})=\ln r+2\pi ik$이고 $L(re^{2\pi i})=\ln r+2\pi i+2\pi ik$이다. 모순이다.
:::

[정리 9](#thm9)는 원점 근방에서 $\log$를 연속적으로 정의하려는 시도가 모두 실패함을 말한다. 임의의 $z_0\ne 0$은 $0$을 포함하지 않는 작은 원판을 가지며, 그 원판은 원점에서 뻗는 어떤 ray과도 만나지 않도록 잡을 수 있어 분지가 존재한다. 그러나 $0$은 어떤 뚫린 원판 $\{0<\lvert z\rvert<\rho\}$ 위에서도 분지를 허락하지 않는다. 일반적으로 함수의 *분지점<sub>branch point</sub>*이란 어떤 뚫린 근방 위에서도 분지를 연속적으로 고를 수 없는 점을 가리키며, $\log$의 분지점은 $0$이다. 분지점은 임의의 다가함수가 가진 이 현상, 곧 점 주위를 한 바퀴 돌았을 때 값이 원래대로 돌아오지 않는 현상이 일어나는 점이다.

분지가 holomorphic이므로 분지에 holomorphic function을 합성하면 합성이 정의되는 영역에서 다시 holomorphic이다. 다만 정의역에 주의하여야 한다. 합성함수 $\operatorname{Log}(f(z))$는 $f(z)$가 분지절단과 만나는 점에서 불연속일 수 있다.

::: 예시 10 ($\operatorname{Log}(z^2)\ne 2\operatorname{Log}z$)
$\operatorname{Log}(z^2)$은 $z^2\in(-\infty,0]$인 점, 곧 $z$가 허수축 위에 있는 점에서 불연속이고 그 밖의 모든 점에서 holomorphic이다. $\Real z>0$이면 $\operatorname{Arg}z\in(-\pi/2,\pi/2)$이므로 $\operatorname{Arg}(z^2)=2\operatorname{Arg}z$이고 $\operatorname{Log}(z^2)=2\operatorname{Log}z$이다. 그러나 $\Real z<0$, $\Img z>0$이면 $\operatorname{Arg}z\in(\pi/2,\pi)$이고 $2\operatorname{Arg}z\in(\pi,2\pi)$이므로 $\operatorname{Arg}(z^2)=2\operatorname{Arg}z-2\pi$, 곧 $\operatorname{Log}(z^2)=2\operatorname{Log}z-2\pi i$이다. $\Img z<0$이면 같은 방식으로 $\operatorname{Log}(z^2)=2\operatorname{Log}z+2\pi i$이다. 따라서 $\operatorname{Log}(z^2)=2\operatorname{Log}z$는 $\Real z>0$에서만 성립한다.
:::

## 거듭제곱

정수가 아닌 지수의 거듭제곱은 $z^a=e^{a\log z}$로 정의한다. 우변의 $\log$가 다가함수이므로 $z^a$도 값이 하나가 아닐 수 있다.

::: 정의 11
$z\ne 0$과 $a\in\mathbb{C}$에 대하여 $z^a=\{e^{aw}:w\in\log z\}$로 정의한다. $\operatorname{Log}z$를 택한 값 $e^{a\operatorname{Log}z}$를 $z^a$의 *주치<sub>principal value</sub>*라 한다.
:::

$a=n$이 정수이면 $e^{nw}=(e^w)^n=z^n$이므로 값이 하나이고 보통의 거듭제곱과 일치한다. 이때 $e^z$를 $e$의 거듭제곱 $e^{z\log e}$로 읽으면 값이 여러 개가 되므로, $e^z$는 항상 지수함수 자체를 가리키는 것으로 약속한다. 일반의 $a$에 대하여 $z^a$의 값은 다음과 같이 센다.

::: 명제 12
$z\ne 0$일 때 $z^a$의 서로 다른 값의 개수는 $a=p/q$ (기약분수, $q\ge1$)이면 $q$이고, $a$가 유리수가 아니면 무한이다.
:::

::: 증명
$\log z=\operatorname{Log}z+2\pi i\mathbb{Z}$이므로 $z^a$의 값은 $e^{a\operatorname{Log}z}e^{2\pi iak}$ ($k\in\mathbb{Z}$)이다. $e^{2\pi iak}=e^{2\pi iak'}$은 [명제 2](#prop2)에 의하여 $a(k-k')\in\mathbb{Z}$와 동치이다. $a=p/q$이면 이는 $q\mid k-k'$와 같으므로 $k$를 $q$로 나눈 나머지에 따라 $q$개의 값이 나온다. $a$가 유리수가 아니면 $a(k-k')\in\mathbb{Z}$는 $k=k'$에서만 성립하므로 값이 모두 서로 다르다.
:::

특히 $a=1/n$이면 $z^{1/n}$은 $z$의 $n$개의 $n$제곱근 전체이다. 이 값들이 지수가 정수일 때와 달리 서로 다르다는 사실이 분지가 필요한 이유이다. 비유리수 지수에서는 무한히 많은 값이 나오며, 이 경우 $i^i$ 같은 거듭제곱도 정의된다. $\log i=i(\pi/2+2\pi k)$이므로

$$i^i=e^{i\cdot i(\pi/2+2\pi k)}=e^{-\pi/2-2\pi k}\qquad(k\in\mathbb{Z})$$

이다. 값이 모두 양의 실수이고 주치는 $e^{-\pi/2}\approx 0.2079$이다.

분지 $L$이 주어진 영역 위에서는 $z^a$의 값을 연속적으로 고를 수 있다.

::: 명제 13
$L$이 $\Omega$ 위의 $\log$의 분지이면 $f(z)=e^{aL(z)}$는 $\Omega$ 위에서 $z^a$의 값을 연속적으로 고른 holomorphic function이며, $f'(z)=ae^{(a-1)L(z)}$이다. 이는 $z^{a-1}$의 같은 분지에서의 값에 $a$를 곱한 것이다.
:::

::: 증명
$f(z)\in z^a$는 정의에서 나온다. $L$이 holomorphic이므로 ([명제 7](#prop7)) 합성에 대한 [§복소정칙함수, ⁋명제 3](/ko/math/complex_analysis/holomorphic_functions#prop3)에 의하여 $f'(z)=aL'(z)e^{aL(z)}=ae^{aL(z)}/z=ae^{aL(z)}e^{-L(z)}=ae^{(a-1)L(z)}$이다.
:::

$\Omega=\mathbb{C}\setminus(-\infty,0]$이고 $L=\operatorname{Log}$이면 이것이 주치 거듭제곱 $z^a=e^{a\operatorname{Log}z}$이고, $(z^a)'=az^{a-1}$이 여기서 성립한다. 실수에서 성립하던 지수법칙 중 여러 값이 섞이는 것은 주치에서 깨진다. $(zw)^a=z^aw^a$는 [예시 5](#ex5)의 이유로 깨지고, $(z^a)^b=z^{ab}$도 마찬가지이다.

::: 예시 14 ($(z^2)^{1/2}\ne z$)
주치 거듭제곱에서 $z=-1$이면 $z^2=1$이고 $1^{1/2}=e^{(1/2)\operatorname{Log}1}=1$이므로 $(z^2)^{1/2}=1\ne -1=z$이다. 주치로 $z^2$을 취하는 순간 $z$의 부호 정보가 사라지기 때문이다.
:::

## 제곱근과 그 분지점

$\sqrt z=z^{1/2}$는 $z\ne 0$에서 서로 부호만 다른 두 값을 갖는다. 주치는 $\sqrt z=e^{(1/2)\operatorname{Log}z}=\sqrt{\lvert z\rvert}e^{i\operatorname{Arg}z/2}$이고, 이 값은 실수부가 $0$ 이상이다.

::: 명제 15
(i) 주치 $\sqrt z$는 $\mathbb{C}\setminus(-\infty,0]$ 위에서 holomorphic이고 $(\sqrt z)'=1/(2\sqrt z)$이다. 음의 실수축의 점 $x<0$에서 위쪽으로 접근하면 $i\sqrt{\lvert x\rvert}$로, 아래쪽으로 접근하면 $-i\sqrt{\lvert x\rvert}$로 수렴한다.

(ii) $\Omega\subseteq\mathbb{C}\setminus\{0\}$이 어떤 원 $\{\lvert z\rvert=r\}$을 포함하면 $\Omega$ 위에서 $s(z)^2=z$인 연속함수 $s$는 존재하지 않는다. 따라서 $0$은 $\sqrt z$의 분지점이다.
:::

::: 증명
(i) [명제 13](#prop13)에서 $a=1/2$이고 $(\sqrt z)'=\frac12 e^{-\operatorname{Log}z/2}=1/(2\sqrt z)$이다. 접근하는 극한은 $\operatorname{Arg}(x+iy)\to\pm\pi$ ([정리 8](#thm8)의 증명)를 $e^{i\operatorname{Arg}z/2}$에 대입하면 $e^{\pm i\pi/2}=\pm i$로 얻는다.

(ii) $s$가 있다고 하자. $q(t)=s(re^{it})/(\sqrt re^{it/2})$ ($t\in[0,2\pi]$)로 두면 $q(t)^2=re^{it}/(re^{it})=1$이므로 $q(t)\in\{1,-1\}$이고 $q$는 연속이므로 [\[해석학\] §연결성과 중간값 정리, ⁋정리 3](/ko/math/analysis/connectedness#thm3)에 의하여 상수 $\varepsilon$이다. $t=0$에서 $s(r)=\varepsilon\sqrt r$인데 $t=2\pi$에서 $s(r)=\varepsilon\sqrt re^{i\pi}=-\varepsilon\sqrt r$이다. 모순이다. 뚫린 원판은 이런 원을 포함하므로 $0$이 분지점이다.
:::

(i)의 불연속은 [정리 8](#thm8)에서 $\operatorname{Log}$가 절단선을 가로지를 때 $2\pi i$만큼 튀는 것의 절반이 $\sqrt z$에서 부호 반전으로 나타난 것이다. 원점을 한 바퀴 돌면 $\log$의 값이 $2\pi i$ 바뀌므로 $\sqrt z$의 값은 $e^{\pi i}=-1$배가 되어 두 값이 서로 교환된다. 같은 이유로 $z^{p/q}$의 값은 원점을 $q$번 돌아야 원래대로 돌아오며, 지수가 유리수가 아니면 돌아오지 않는다.

---

**참고문헌**

**[Ahl]** L.V. Ahlfors, *Complex analysis*, 3rd ed., McGraw–Hill, 1979.  
**[Con]** J.B. Conway, *Functions of one complex variable I*, 2nd ed., Graduate Texts in Mathematics 11, Springer, 1978.  
**[SS]** E.M. Stein, R. Shakarchi, *Complex analysis*, Princeton Lectures in Analysis II, Princeton University Press, 2003.
