---
title: "유수를 이용한 실적분 계산"
description: "유수정리를 이용하여 유리함수의 무한적분, Jordan 보조정리를 통한 Fourier 적분, 단위원 치환에 의한 삼각적분, 실축 위의 극이 있는 적분(Cauchy 주값), 분지절단과 열쇠구멍 경로, 그리고 cot를 이용한 무한급수의 합을 계산한다. 각 경로에서 큰 원과 작은 원 위의 적분이 소멸하는 이유를 부등식으로 직접 확인하고, 가정이 빠지면 공식이 어떻게 무너지는지를 반례로 보인다."
excerpt: "유리함수의 무한적분, Jordan 보조정리, 단위원 치환, Cauchy 주값, 열쇠구멍 경로, 원점 우회 반원, π cot πz 급수 합"

categories: [Math / Complex Analysis]
permalink: /ko/math/complex_analysis/residue_integrals
sidebar: 
    nav: "complex_analysis-ko"

date: 2026-10-13
weight: 11

published: false

---

[§유수정리, ⁋정리 2](/ko/math/complex_analysis/residue_theorem#thm2)는 닫힌 경로를 따른 적분을 경로 안의 극에서의 residue 계산으로 바꾸어 준다. 이를 실변수 적분에 쓰려면 적분 구간을 닫힌 경로의 일부로 만들어야 한다. 실축 위의 구간에 복소평면 안의 호나 선분을 이어 붙여 경로를 닫고, 닫힌 경로 전체의 적분을 residue로 계산한 다음, 우리가 원하지 않는 부분의 적분이 극한에서 $0$이 됨을 보이면 실축 위의 적분만 남는다. 이 글의 모든 계산은 이 세 단계를 따르며, 경로마다 달라지는 것은 어떤 호를 붙이는가와 그 호 위의 적분이 왜 소멸하는가이다. 소멸의 근거는 매번 [§복소적분, ⁋명제 6](/ko/math/complex_analysis/complex_integration#prop6), 곧 경로 위의 적분의 절댓값이 경로의 길이와 피적분함수의 최댓값의 곱 이하라는 부등식이다.

이 글에서 쓰는 유수정리는 다음 형태이다. $f$가 닫힌 경로 $\gamma$와 그 내부에서 유한 개의 극을 제외하고 holomorphic이고 극이 $\gamma$ 위에 놓이지 않으면, $\gamma$가 내부의 각 극을 한 번씩 반시계방향으로 도는 경우

$$\oint_\gamma f(z)\dd{z} = 2\pi i\sum_j \operatorname{Res}_{z=z_j} f$$

이다. 극이 단순극이면 [§유수정리, ⁋명제 3](/ko/math/complex_analysis/residue_theorem#prop3)에 의하여 $\operatorname{Res}_{z=z_0}f = \lim_{z\to z_0}(z-z_0)f(z)$이고, $f=g/h$에서 $h(z_0)=0$, $h'(z_0)\neq0$, $g(z_0)\neq0$이면 $\operatorname{Res}_{z=z_0}f = g(z_0)/h'(z_0)$이다. 이상적분은 [\[미적분학\] §이상적분, ⁋정의 1](/ko/math/calculus/improper_integrals#def1)로 정의하고, 수렴은 [\[미적분학\] §이상적분, ⁋명제 3](/ko/math/calculus/improper_integrals#prop3)에 의하여 판정한다. 특히 양쪽이 무한대인 이상적분은 두 극한을 독립적으로 보내어 정의하므로, $\int_{-R}^{R}$에서 $R\to\infty$로 보낸 극한과 일반적으로는 다르다. 이 차이가 아래 여러 곳에서 실제로 문제가 된다.

## 유리함수의 무한적분

가장 단순한 경우는 유리함수 $f=P/Q$의 $\int_{-\infty}^{\infty}f(x)\dd{x}$이다. 실축 $[-R,R]$에 상반평면의 반원호 $C_R=\{Re^{i\theta}\mid 0\le\theta\le\pi\}$를 이어 붙여 닫힌 경로를 만든다. 반원호는 둘레 $\pi R$의 arc이므로, 그 위의 적분이 $0$으로 가려면 $f$가 $R$보다 빠르게 감소해야 한다. 유리함수는 이를 분모와 분자의 차수 차이로 보장한다.

::: 명제 1 (유리함수의 무한적분)
$P,Q$가 polynomial이고 $Q$가 실축 위에서 영점을 갖지 않으며 $\deg Q\ge\deg P+2$라 하자. $f=P/Q$이면 $\int_{-\infty}^{\infty}f(x)\dd{x}$는 수렴하고

$$\int_{-\infty}^{\infty}f(x)\dd{x}=2\pi i\sum_{\Img z_j>0}\operatorname{Res}_{z=z_j}f$$

이다. 합은 상반평면에 있는 $f$의 극 전체에 걸친다.
:::

::: 증명
$m=\deg P$, $n=\deg Q$라 하고 $P,Q$의 최고차 계수를 $p_m,q_n$이라 하자. $P(z)=p_mz^m(1+O(1/z))$, $Q(z)=q_nz^n(1+O(1/z))$이므로 어떤 $R_0$이 있어 $\lvert z\rvert\ge R_0$에서 $\lvert P(z)\rvert\le2\lvert p_m\rvert\lvert z\rvert^m$, $\lvert Q(z)\rvert\ge\lvert q_n\rvert\lvert z\rvert^n/2$이다. 따라서 상수 $M$이 있어

$$\lvert f(z)\rvert\le\frac{M}{\lvert z\rvert^{n-m}}\le\frac{M}{\lvert z\rvert^{2}}\qquad(\lvert z\rvert\ge R_0)$$

이다. $f$는 실축에서 연속이고 $\lvert x\rvert\ge R_0$에서 $M/x^2$로 눌리므로, [\[미적분학\] §이상적분, ⁋명제 3](/ko/math/calculus/improper_integrals#prop3)과 [\[미적분학\] §이상적분, ⁋명제 4](/ko/math/calculus/improper_integrals#prop4)에 의하여 $\int_{-\infty}^{\infty}f(x)\dd{x}$가 수렴한다. 수렴하는 이상적분은 $\int_{-R}^{R}$의 극한과 같으므로 $\lim_{R\to\infty}\int_{-R}^{R}f(x)\dd{x}$를 계산하면 된다.

$R>R_0$이고 $R$이 $Q$의 모든 영점의 절댓값보다 크다고 하자. 선분 $[-R,R]$과 $C_R$을 이은 경로는 상반평면의 극을 각각 한 번씩 반시계방향으로 돌므로 [§유수정리, ⁋정리 2](/ko/math/complex_analysis/residue_theorem#thm2)에 의하여

$$\int_{-R}^{R}f(x)\dd{x}+\int_{C_R}f(z)\dd{z}=2\pi i\sum_{\Img z_j>0}\operatorname{Res}_{z=z_j}f$$

이다. $C_R$ 위에서 $\lvert f\rvert\le M/R^2$이고 $C_R$의 길이는 $\pi R$이므로

$$\left\lvert\int_{C_R}f(z)\dd{z}\right\rvert\le\frac{M}{R^2}\cdot\pi R=\frac{\pi M}{R}\longrightarrow0\qquad(R\to\infty)$$

이다. 위 등식에서 $R\to\infty$로 보내면 주장을 얻는다.
:::

가령 $\int_{-\infty}^{\infty}\dd{x}/(x^4+1)$에서 $Q=z^4+1$의 영점은 $e^{i\pi/4},e^{3i\pi/4},e^{5i\pi/4},e^{7i\pi/4}$이고 상반평면에는 앞의 둘이 있다. $z^4=-1$이므로 $z_0$에서의 residue는 $1/(4z_0^3)=z_0/(4z_0^4)=-z_0/4$이고, 둘의 합은 $-(e^{i\pi/4}+e^{3i\pi/4})/4=-i\sqrt2/4$이다. 따라서 적분은 $2\pi i\cdot(-i\sqrt2/4)=\pi/\sqrt2$이다.

차수 조건 $\deg Q\ge\deg P+2$는 반원호 적분을 죽이는 [§복소적분, ⁋명제 6](/ko/math/complex_analysis/complex_integration#prop6)에서 나온 것이며, 차이가 $1$이면 공식이 성립하지 않는다.

::: 예시 2 (차수 차이가 1인 경우)
$f(x)=x/(x^2+1)$이면 $\deg Q-\deg P=1$이다. 이때 $f$는 기함수이므로 모든 $R$에 대해 $\int_{-R}^{R}f\dd{x}=0$이다. 그러나 $\int_0^R f\dd{x}=(1/2)\ln(1+R^2)$은 $R\to\infty$에서 발산하므로 $\int_{-\infty}^{\infty}f\dd{x}$는 수렴하지 않는다. 반원호 위에서는 $z/(z^2+1)=1/z+O(1/z^3)$이고 $\int_{C_R}\dd{z}/z=i\pi$이므로

$$\int_{C_R}\frac{z}{z^2+1}\dd{z}\longrightarrow i\pi\neq0$$

이다. 실제로 [§유수정리, ⁋정리 2](/ko/math/complex_analysis/residue_theorem#thm2)는 $0+i\pi=2\pi i\operatorname{Res}_{z=i}f=2\pi i\cdot(1/2)$로 성립하며, 반원호의 기여가 살아남아 실축 적분만을 뽑아낼 수 없다.
:::

## Jordan 보조정리와 Fourier 적분

$\cos ax$나 $\sin ax$가 곱해진 적분은 $\int f(x)e^{iax}\dd{x}$의 실수부와 허수부로 다룬다. 이때는 $\lvert e^{iaz}\rvert=e^{-a\Img z}$가 상반평면에서 $1$ 이하이므로, 반원호 위에서 $f$가 단지 $0$으로 가기만 하면 충분하다. 이를 정확히 하는 것이 Jordan 보조정리이다.

::: 보조정리 3 (Jordan)
$a>0$이라 하고 $f$가 $\{\Img z\ge0,\ \lvert z\rvert\ge R_0\}$에서 연속이라 하자. $M(R)=\max_{z\in C_R}\lvert f(z)\rvert$가 $R\to\infty$에서 $0$으로 가면

$$\lim_{R\to\infty}\int_{C_R}f(z)e^{iaz}\dd{z}=0$$

이다.
:::

::: 증명
$z=Re^{i\theta}$로 매개화하면 $\dd{z}=iRe^{i\theta}\dd{\theta}$이고 $\lvert e^{iaz}\rvert=e^{-aR\sin\theta}$이다. 따라서

$$\left\lvert\int_{C_R}f(z)e^{iaz}\dd{z}\right\rvert\le M(R)R\int_0^{\pi}e^{-aR\sin\theta}\dd{\theta}$$

이다. $\sin(\pi-\theta)=\sin\theta$이므로 $\int_0^\pi=2\int_0^{\pi/2}$이다. $[0,\pi/2]$에서 $\sin$은 오목하고 $\sin0=0$, $\sin(\pi/2)=1$이므로 오목함수의 그래프가 현 $\theta\mapsto2\theta/\pi$ 위에 놓여 $\sin\theta\ge2\theta/\pi$이다. 그러므로

$$\int_0^{\pi/2}e^{-aR\sin\theta}\dd{\theta}\le\int_0^{\pi/2}e^{-2aR\theta/\pi}\dd{\theta}=\frac{\pi}{2aR}\bigl(1-e^{-aR}\bigr)\le\frac{\pi}{2aR}$$

이고, 이를 대입하면

$$\left\lvert\int_{C_R}f(z)e^{iaz}\dd{z}\right\rvert\le M(R)R\cdot2\cdot\frac{\pi}{2aR}=\frac{\pi}{a}M(R)\longrightarrow0$$

이다.
:::

[§복소적분, ⁋명제 6](/ko/math/complex_analysis/complex_integration#prop6)을 그대로 쓰면 $\lvert e^{iaz}\rvert\le1$이므로 $M(R)\cdot\pi R$만 얻는데, [보조정리 3](#lem3)은 $e^{-aR\sin\theta}$를 적분하여 $R$ 인자를 $1/R$로 상쇄한다. 이 때문에 $f$가 $1/R^2$만큼 빠르게 줄어들 필요가 없고 $0$으로 가기만 하면 된다. 또 $a>0$일 때 상반평면에서 닫아야 하는 이유도 여기에 있다. 하반평면에서는 $\lvert e^{iaz}\rvert=e^{aR\lvert\sin\theta\rvert}$가 지수적으로 커져서 반원호 적분이 소멸하지 않는다. $\cos$은 우함수이고 $\sin$은 기함수이므로 $a>0$인 경우만 다루면 충분하다.

::: 명제 4 (Fourier 적분)
$P,Q$가 polynomial이고 $Q$가 실축 위에서 영점을 갖지 않으며 $\deg Q\ge\deg P+1$이라 하자. $f=P/Q$이고 $a>0$이면 $\int_{-\infty}^{\infty}f(x)e^{iax}\dd{x}$는 수렴하고

$$\int_{-\infty}^{\infty}f(x)e^{iax}\dd{x}=2\pi i\sum_{\Img z_j>0}\operatorname{Res}_{z=z_j}\bigl(f(z)e^{iaz}\bigr)$$

이다. $P,Q$의 계수가 실수이면 양변의 실수부와 허수부를 비교하여 $\int f(x)\cos ax\dd{x}$와 $\int f(x)\sin ax\dd{x}$를 얻는다.
:::

::: 증명
[명제 1](#prop1)의 증명에서와 같이 $\lvert z\rvert\ge R_0$에서 $\lvert f(z)\rvert\le M/\lvert z\rvert$이므로 $M(R)\le M/R\to0$이고, [보조정리 3](#lem3)에 의해 반원호 적분이 소멸한다. [명제 1](#prop1)과 같은 닫힌 경로에 [§유수정리, ⁋정리 2](/ko/math/complex_analysis/residue_theorem#thm2)를 쓰고 $R\to\infty$로 보내면

$$\lim_{R\to\infty}\int_{-R}^{R}f(x)e^{iax}\dd{x}=2\pi i\sum_{\Img z_j>0}\operatorname{Res}_{z=z_j}\bigl(f(z)e^{iaz}\bigr)$$

이다. 남은 것은 이상적분 자체가 수렴함, 곧 양쪽 극한이 독립적으로 존재함이다. 이 경우 $f$가 $1/x$ 정도로만 감소하여 절대수렴은 보장되지 않으므로 부분적분을 쓴다. $x\ge R_0$에서

$$\int_{R_0}^{t}f(x)e^{iax}\dd{x}=\left[\frac{f(x)e^{iax}}{ia}\right]_{R_0}^{t}-\frac{1}{ia}\int_{R_0}^{t}f'(x)e^{iax}\dd{x}$$

이다. 첫째 항은 $f(t)\to0$이므로 $t\to\infty$에서 수렴한다. $f'=(P'Q-PQ')/Q^2$에서 분자의 차수는 $\deg P+\deg Q-1$ 이하이고 분모의 차수는 $2\deg Q$이므로 $\deg Q-\deg(\text{분자})\ge2$이고, 따라서 $\lvert f'(x)\rvert\le M'/x^2$이다. [\[미적분학\] §이상적분, ⁋명제 3](/ko/math/calculus/improper_integrals#prop3)과 [\[미적분학\] §이상적분, ⁋명제 4](/ko/math/calculus/improper_integrals#prop4)에 의하여 둘째 항의 적분도 수렴한다. $t\to-\infty$ 쪽도 같으므로 두 극한이 독립적으로 존재하고, 그 합은 대칭 극한과 같다.
:::

::: 예시 5 (차수 차이가 1인 Fourier 적분)
$a>0$일 때 $\int_{-\infty}^{\infty}x\sin(ax)/(x^2+1)\dd{x}=\pi e^{-a}$이다. $f(z)=z/(z^2+1)$은 $\deg Q-\deg P=1$이므로 [명제 1](#prop1)이 아닌 [명제 4](#prop4)를 쓴다. $f(z)e^{iaz}$의 상반평면 극은 $z=i$ 하나이고 [§유수정리, ⁋명제 3](/ko/math/complex_analysis/residue_theorem#prop3)에 의하여

$$\operatorname{Res}_{z=i}\frac{ze^{iaz}}{z^2+1}=\frac{ze^{iaz}}{2z}\bigg\rvert_{z=i}=\frac{e^{-a}}{2}$$

이므로 $\int_{-\infty}^{\infty}xe^{iax}/(x^2+1)\dd{x}=2\pi i\cdot e^{-a}/2=i\pi e^{-a}$이다. 실수부는 $\int x\cos(ax)/(x^2+1)\dd{x}=0$으로 피적분함수가 기함수임과 일치하고, 허수부가 구하는 값 $\pi e^{-a}$이다. 이 적분은 $x\sin(ax)/(x^2+1)\sim\sin(ax)/x$라 절대수렴하지 않으며, [예시 2](#ex2)에서 보았듯 [보조정리 3](#lem3) 없이 ML 부등식만으로는 반원호 적분이 소멸함을 보일 수 없다.
:::

## 단위원 치환에 의한 삼각적분

$0$부터 $2\pi$까지 $\cos\theta$와 $\sin\theta$의 유리식을 적분하는 경우에는 경로를 만들어 붙일 필요가 없다. $z=e^{i\theta}$로 두면 구간 $[0,2\pi]$ 자체가 단위원이므로 실적분이 처음부터 닫힌 경로 위의 적분이다. 따라서 추정해야 할 호 적분도 없다.

::: 명제 6 (단위원 치환)
$R(u,v)$가 두 변수의 유리함수이고 $R(\cos\theta,\sin\theta)$의 분모가 $\theta\in[0,2\pi]$에서 $0$이 되지 않는다고 하자.

$$F(z)=\frac{1}{iz}R\Bigl(\frac{z+z^{-1}}{2},\frac{z-z^{-1}}{2i}\Bigr)$$

로 두면 $F$는 단위원 위에 극이 없는 $z$의 유리함수이고

$$\int_0^{2\pi}R(\cos\theta,\sin\theta)\dd{\theta}=2\pi i\sum_{\lvert z_j\rvert<1}\operatorname{Res}_{z=z_j}F$$

이다. 합은 단위원판 안의 극 전체에 걸친다.
:::

::: 증명
$z=e^{i\theta}$이면 $\cos\theta=(z+z^{-1})/2$, $\sin\theta=(z-z^{-1})/(2i)$이고, $\dd{z}=ie^{i\theta}\dd{\theta}=iz\dd{\theta}$이다. 단위원을 $\gamma(\theta)=e^{i\theta}$ ($0\le\theta\le2\pi$)로 매개화하면

$$\oint_{\lvert z\rvert=1}F(z)\dd{z}=\int_0^{2\pi}F(e^{i\theta})ie^{i\theta}\dd{\theta}=\int_0^{2\pi}R(\cos\theta,\sin\theta)\dd{\theta}$$

이다. $F(e^{i\theta})$의 분모는 $R(\cos\theta,\sin\theta)$의 분모에서 오므로 단위원 위에서 $0$이 되지 않고, 따라서 $F$는 단위원 위에 극이 없다. 단위원은 내부의 각 극을 한 번씩 반시계방향으로 돌므로 [§유수정리, ⁋정리 2](/ko/math/complex_analysis/residue_theorem#thm2)에 의하여 결론을 얻는다.
:::

주의할 점은 $F$의 극에 원점이 포함될 수 있다는 것이다. $1/(iz)$ 인자와, $\cos n\theta$ 같은 항에서 나오는 $z^{-n}$ 때문에 원점은 보통 극이 되며, 이 경우 residue는 [§유수정리, ⁋명제 3](/ko/math/complex_analysis/residue_theorem#prop3)의 단순극 공식이 아니라 Laurent 전개나 고차극 공식으로 구해야 한다.

표준적인 경우로 $a>1$일 때 $\int_0^{2\pi}\dd{\theta}/(a+\cos\theta)$를 보자. 치환하면 피적분함수가

$$F(z)=\frac{1}{iz}\cdot\frac{1}{a+\frac12(z+z^{-1})}=\frac{2}{i}\cdot\frac{1}{z^2+2az+1}$$

이 되고, 분모의 두 근 $z_\pm=-a\pm\sqrt{a^2-1}$은 $z_+z_-=1$을 만족한다. $a>1$이면 $\lvert z_+\rvert<1<\lvert z_-\rvert$이므로 단위원판 안의 극은 $z_+$ 하나이고, [§유수정리, ⁋명제 3](/ko/math/complex_analysis/residue_theorem#prop3)에 의하여 그 residue는 $2/\bigl(i(z_+-z_-)\bigr)=1/\bigl(i\sqrt{a^2-1}\bigr)$이다. 따라서 적분은 $2\pi/\sqrt{a^2-1}$이다. 가정이 빠지는 경우는 $\lvert a\rvert<1$이다. 이때 $z_\pm$가 모두 단위원 위에 놓이고, 원래 적분에서는 $a+\cos\theta_0=0$인 $\theta_0$에서 $-\sin\theta_0\neq0$이어서 피적분함수가 $1/(\theta-\theta_0)$처럼 발산하므로 적분이 수렴하지 않는다.

::: 예시 7 (고차극이 원점에 있는 경우)
$\int_0^{2\pi}\cos2\theta/(5-4\cos\theta)\dd{\theta}=\pi/6$이다. $\cos2\theta=(z^2+z^{-2})/2=(z^4+1)/(2z^2)$이고 $5-4\cos\theta=5-2z-2z^{-1}=-(2z-1)(z-2)/z$이므로

$$F(z)=-\frac{z^4+1}{2iz^2(2z-1)(z-2)}$$

이다. 단위원판 안의 극은 이차극 $z=0$과 단순극 $z=1/2$이다. $z=1/2$에서는

$$\operatorname{Res}_{z=1/2}F=-\frac{z^4+1}{2iz^2\cdot2(z-2)}\bigg\rvert_{z=1/2}=\frac{17}{24i}$$

이다. 원점에서는 $g(z)=-(z^4+1)/\bigl(2i(2z-1)(z-2)\bigr)$로 두고 $F=g/z^2$이므로 [§유수정리, ⁋명제 3](/ko/math/complex_analysis/residue_theorem#prop3)에 의하여 $\operatorname{Res}_{z=0}F=g'(0)$이다. $h(z)=(2z-1)(z-2)=2z^2-5z+2$에서 $h(0)=2$, $h'(0)=-5$이므로

$$g'(0)=-\frac{1}{2i}\cdot\frac{4z^3h-(z^4+1)h'}{h^2}\bigg\rvert_{z=0}=-\frac{1}{2i}\cdot\frac{5}{4}=-\frac{5}{8i}$$

이다. 두 residue의 합은 $17/(24i)-15/(24i)=1/(12i)$이고, 적분은 $2\pi i\cdot1/(12i)=\pi/6$이다.
:::

## 실축 위의 극과 Cauchy 주값

피적분함수가 실축 위에 극을 가지면 앞의 경로는 극을 지나가게 되어 쓸 수 없다. 극이 실축 위의 $c$에 있으면 이상적분은 $c$의 양쪽에서 독립적인 극한으로 정의되어야 한다. 그런데 $\int dx/x$처럼 이 독립적인 극한은 존재하지 않아도, $c$의 양쪽에서 같은 속도로 극을 도려낸 극한은 존재할 수 있다. 이를 이용하여 *Cauchy 주값<sub>principal value</sub>*을

$$\operatorname{PV}\int_{-\infty}^{\infty}f(x)\dd{x}=\lim_{\substack{\varepsilon\to0^+\\R\to\infty}}\Bigl(\int_{-R}^{R}f(x)\dd{x}-\sum_k\int_{c_k-\varepsilon}^{c_k+\varepsilon}f(x)\dd{x}\Bigr)$$

로 정의한다. 여기서 $c_k$는 실축 위의 극이고, $\sum_k$ 항은 각 극 둘레의 구간 $(c_k-\varepsilon,c_k+\varepsilon)$ 위의 적분이다. 실제로는 $[-R,R]$에서 이 구간들을 뺀 나머지 구간들 위의 적분을 뜻한다. 이상적분이 수렴하면 주값은 그 값과 같지만, 역은 성립하지 않는다. 가령 $\operatorname{PV}\int_{-1}^{1}\dd{x}/x=0$이지만 $\int_{-1}^{1}\dd{x}/x$는 이상적분으로서 정의되지 않는다.

극을 피하는 방법은 극 둘레에 작은 반원을 그려 우회하는 것이다. 그 반원 위의 적분은 $\varepsilon\to0$에서 residue의 일부를 준다.

::: 보조정리 8 (작은 반원)
$f$가 $c$에서 단순극을 갖고 residue가 $r$이라 하자. $\gamma_\varepsilon(\theta)=c+\varepsilon e^{i\theta}$ ($\theta_1\le\theta\le\theta_2$)이면

$$\lim_{\varepsilon\to0^+}\int_{\gamma_\varepsilon}f(z)\dd{z}=i(\theta_2-\theta_1)r$$

이다.
:::

::: 증명
단순극이므로 $c$의 근방에서 $f(z)=r/(z-c)+g(z)$이고 $g$는 $c$에서 holomorphic이다. 따라서 $c$ 둘레의 닫힌 원판에서 $\lvert g\rvert\le K$이다. 첫째 항은 직접 계산하여

$$\int_{\gamma_\varepsilon}\frac{r}{z-c}\dd{z}=r\int_{\theta_1}^{\theta_2}\frac{i\varepsilon e^{i\theta}}{\varepsilon e^{i\theta}}\dd{\theta}=i(\theta_2-\theta_1)r$$

이고, 둘째 항은 [§복소적분, ⁋명제 6](/ko/math/complex_analysis/complex_integration#prop6)으로 $\bigl\lvert\int_{\gamma_\varepsilon}g\dd{z}\bigr\rvert\le K\cdot\varepsilon(\theta_2-\theta_1)\to0$이다.
:::

단순극이라는 가정은 본질적이다. 이차극 $1/z^2$의 경우 $\theta=\pi$에서 $0$까지의 반원 위 적분은 $[-1/z]_{-\varepsilon}^{\varepsilon}=-2/\varepsilon$이어서 $\varepsilon\to0$에서 발산한다.

::: 명제 9 (실축 위에 단순극이 있는 Fourier 적분)
$P,Q$가 polynomial이고 $\deg Q\ge\deg P+1$이며 $Q$의 실영점 $c_1,\dots,c_k$가 모두 단순영점이라 하자. $f=P/Q$이고 $a>0$이면

$$\operatorname{PV}\int_{-\infty}^{\infty}f(x)e^{iax}\dd{x}=2\pi i\sum_{\Img z_j>0}\operatorname{Res}_{z=z_j}\bigl(f(z)e^{iaz}\bigr)+\pi i\sum_{l=1}^{k}\operatorname{Res}_{z=c_l}\bigl(f(z)e^{iaz}\bigr)$$

이다.
:::

::: 증명
$R$을 크게, $\varepsilon$을 작게 잡아 $Q$의 상반평면 영점이 모두 $\lvert z\rvert<R$ 안에 있고 $c_l$ 둘레의 반지름 $\varepsilon$인 닫힌 반원판들이 서로 만나지 않으며 다른 극을 포함하지 않게 한다. 경로 $\Gamma_{\varepsilon,R}$를 다음과 같이 만든다. 실축 위에서 $-R$부터 $R$까지 각 $c_l$ 근방 $(c_l-\varepsilon,c_l+\varepsilon)$를 건너뛰며 가고, 건너뛴 곳에서는 상반평면 쪽 반원 $c_l+\varepsilon e^{i\theta}$를 $\theta=\pi$에서 $0$으로 시계방향으로 돈 다음, 마지막에 $C_R$을 따라 $R$에서 $-R$로 돌아온다. 이 경로의 내부에는 $f e^{iaz}$의 실축 위 극이 없고 상반평면의 극이 각각 회전수 $1$로 들어 있으므로 [§유수정리, ⁋정리 2](/ko/math/complex_analysis/residue_theorem#thm2)에 의하여

$$\int_{[-R,R]\setminus\bigcup(c_l-\varepsilon,c_l+\varepsilon)}f(x)e^{iax}\dd{x}+\sum_l\int_{\gamma_{l,\varepsilon}}fe^{iaz}\dd{z}+\int_{C_R}fe^{iaz}\dd{z}=2\pi i\sum_{\Img z_j>0}\operatorname{Res}\bigl(fe^{iaz}\bigr)$$

이다. $fe^{iaz}$는 $c_l$에서 단순극 또는 removable singularity이므로(분자가 $0$이면 residue가 $0$이다) [보조정리 8](#lem8)에서 $\theta_1=\pi$, $\theta_2=0$으로 놓으면 각 작은 반원 적분은 $-i\pi\operatorname{Res}_{z=c_l}(fe^{iaz})$로 수렴한다. $C_R$ 위의 적분은 [명제 4](#prop4)의 증명처럼 [보조정리 3](#lem3)으로 $0$으로 간다. 이항하면 주장을 얻는다.
:::

작은 반원이 시계방향이어서 $-\pi i\operatorname{Res}$가 좌변에 나타나고, 이를 우변으로 넘겨 $+\pi i\operatorname{Res}$가 된다. 이 부호가 실수하기 쉬운 곳이다.

::: 예시 10 (Dirichlet 적분)
$\int_0^{\infty}\sin x/x\dd{x}=\pi/2$이다. $f(z)=1/z$로 놓으면 $\deg Q-\deg P=1$이고 실영점 $0$은 단순영점이며 상반평면에는 극이 없다. $\operatorname{Res}_{z=0}e^{iz}/z=1$이므로 [명제 9](#prop9)에서

$$\operatorname{PV}\int_{-\infty}^{\infty}\frac{e^{ix}}{x}\dd{x}=\pi i$$

이다. 실수부 $\operatorname{PV}\int\cos x/x\dd{x}$는 기함수라 $0$이다. 허수부에서 $\sin x/x$는 $x=0$에서 $1$로 연속 확장되므로 원점을 도려내는 것과 무관하게 $\int_{-\infty}^{\infty}\sin x/x\dd{x}=\pi$이다. 수렴은 [명제 4](#prop4)의 증명과 같은 부분적분으로 확인되고, 피적분함수가 우함수이므로 $\int_0^\infty=\pi/2$이다. 작은 반원의 기여 $-i\pi$를 빠뜨리면 허수부가 $0$이 되어 틀린 값을 얻는다.
:::

## 분지절단과 열쇠구멍 경로

피적분함수에 $x^{a-1}$ ($a$가 정수가 아님)이 들어 있으면 적분 구간이 $[0,\infty)$ 하나이고 피적분함수가 우함수도 아니어서, 앞의 반원 경로처럼 구간을 실축 전체로 대칭 확장할 수 없다. 대신 $z^{a-1}$이 원점 둘레를 한 바퀴 돌 때 $e^{2\pi i(a-1)}$배가 되어 multivalued라는 점을 이용한다. 양의 실축을 따라 branch cut을 두고 절단의 위아래 둑을 모두 경로에 넣는다. 위 둑에서는 $\arg z=0$, 아래 둑에서는 $\arg z=2\pi$이고, 두 둑 위의 값의 비 $e^{2\pi i(a-1)}=e^{2\pi ia}$가 적분을 $\int_0^\infty$ 하나로 묶어 내는 계수가 된다.

::: 명제 11 (열쇠구멍 경로)
$0<a<1$이면

$$\int_0^{\infty}\frac{x^{a-1}}{1+x}\dd{x}=\frac{\pi}{\sin\pi a}$$

이다.
:::

::: 증명
수렴부터 확인한다. $0<x\le1$에서 $x^{a-1}/(1+x)\le x^{a-1}$이고 $\int_0^1x^{a-1}\dd{x}$는 $a>0$에서 수렴한다. $x\ge1$에서 $x^{a-1}/(1+x)\le x^{a-2}$이고 $\int_1^\infty x^{a-2}\dd{x}$는 $a<1$에서 수렴한다. [\[미적분학\] §이상적분, ⁋명제 3](/ko/math/calculus/improper_integrals#prop3)에 의하여 구하는 적분은 수렴한다.

$\log z=\ln\lvert z\rvert+i\arg z$ ($0<\arg z<2\pi$)로 $z^{a-1}=e^{(a-1)\log z}$를 정의하면 $f(z)=z^{a-1}/(1+z)$는 $\mathbb{C}\setminus[0,\infty)$에서 $z=-1$을 제외하고 holomorphic이다. $0<\varepsilon<1<R$에 대해 경로 $\Gamma$를 네 조각으로 만든다. 위 둑 $\Gamma_1$은 $\varepsilon$에서 $R$까지, 큰 원 $C_R$은 반지름 $R$인 원을 반시계방향으로, 아래 둑 $\Gamma_2$는 $R$에서 $\varepsilon$까지, 작은 원 $c_\varepsilon$은 반지름 $\varepsilon$인 원을 시계방향으로 돈다. 경로는 절단에서 각 $\delta$만큼 띄워 잡고 $\delta\to0$으로 보내며, $f$가 각 둑까지 연속으로 확장되므로 극한은 둑 위의 적분이다.

경로 안의 극은 $z=-1=e^{i\pi}$ 하나이고 $(-1)^{a-1}=e^{(a-1)i\pi}=-e^{i\pi a}$이므로 [§유수정리, ⁋명제 3](/ko/math/complex_analysis/residue_theorem#prop3)에 의하여 $\operatorname{Res}_{z=-1}f=-e^{i\pi a}$이다. 둑 위의 적분은, 위 둑에서 $z=x$이고 아래 둑에서 $z=xe^{2\pi i}$라 $z^{a-1}=x^{a-1}e^{2\pi i(a-1)}=x^{a-1}e^{2\pi ia}$이므로

$$\int_{\Gamma_1}f\dd{z}+\int_{\Gamma_2}f\dd{z}=\int_\varepsilon^R\frac{x^{a-1}}{1+x}\dd{x}-e^{2\pi ia}\int_\varepsilon^R\frac{x^{a-1}}{1+x}\dd{x}$$

이다. 큰 원 위에서 $\lvert z^{a-1}\rvert=R^{a-1}$이고 $\lvert1+z\rvert\ge R-1$이므로 [§복소적분, ⁋명제 6](/ko/math/complex_analysis/complex_integration#prop6)에서

$$\left\lvert\int_{C_R}f\dd{z}\right\rvert\le\frac{R^{a-1}}{R-1}\cdot2\pi R=\frac{2\pi R^{a}}{R-1}\longrightarrow0\qquad(R\to\infty)$$

이다. 이는 $a<1$일 때 분자의 차수 $a$가 분모의 차수 $1$보다 작기 때문이다. 작은 원 위에서는 $\lvert z^{a-1}\rvert=\varepsilon^{a-1}$이고 $\lvert1+z\rvert\ge1-\varepsilon$이므로

$$\left\lvert\int_{c_\varepsilon}f\dd{z}\right\rvert\le\frac{\varepsilon^{a-1}}{1-\varepsilon}\cdot2\pi\varepsilon=\frac{2\pi\varepsilon^{a}}{1-\varepsilon}\longrightarrow0\qquad(\varepsilon\to0^+)$$

이며, 이는 $a>0$일 때이다. 따라서 $\varepsilon\to0$, $R\to\infty$에서 [§유수정리, ⁋정리 2](/ko/math/complex_analysis/residue_theorem#thm2)는

$$\bigl(1-e^{2\pi ia}\bigr)\int_0^\infty\frac{x^{a-1}}{1+x}\dd{x}=2\pi i\cdot\bigl(-e^{i\pi a}\bigr)$$

가 된다. $a$가 정수가 아니므로 $1-e^{2\pi ia}\neq0$이고

$$\int_0^\infty\frac{x^{a-1}}{1+x}\dd{x}=\frac{-2\pi ie^{i\pi a}}{1-e^{2\pi ia}}=\frac{-2\pi i}{e^{-i\pi a}-e^{i\pi a}}=\frac{-2\pi i}{-2i\sin\pi a}=\frac{\pi}{\sin\pi a}$$

이다.
:::

$0<a<1$이라는 조건은 증명에서 세 번 쓰였다. 적분의 $0$ 근방 수렴($a>0$), $\infty$ 근방 수렴($a<1$), 그리고 두 원 위 적분의 소멸이다. 실제로 $a\to0^+$ 또는 $a\to1^-$에서 우변 $\pi/\sin\pi a$가 발산하는 것은 이 조건이 깨질 때 적분 자체가 발산하는 것과 일치한다. 흔한 실수는 아래 둑에서 $\arg z=2\pi$로 오르는 것을 잊고 $z^{a-1}$의 값을 위 둑과 같게 두는 것이며, 그러면 $(1-e^{2\pi ia})$ 인자가 $0$이 되어 아무 정보도 얻지 못한다.

## 원점을 우회하는 반원 경로

피적분함수에 $\log$가 들어 있는 $\int_0^\infty\ln x/(1+x^2)\dd{x}$는 열쇠구멍 경로로 같은 피적분함수 $\operatorname{Log}z/(1+z^2)$를 적분해서는 풀리지 않는다. 위 둑과 아래 둑의 $\ln x$ 항이 서로 소거되어 구하려는 적분이 식에서 사라지기 때문이다. 대신 상반평면 반원 경로에 원점을 작은 반원으로 우회시킨다. 이 경로에서는 음의 실축 위의 $\operatorname{Log}z$가 $\ln\lvert x\rvert+i\pi$가 되어 $\int\ln x/(1+x^2)$가 두 번 나타난다.

::: 예시 12 (로그가 있는 적분)
$\int_0^\infty\ln x/(1+x^2)\dd{x}=0$이다. 먼저 수렴을 확인한다. $x\ge1$에서 $\ln x\le2\sqrt x$이므로 $\ln x/(1+x^2)\le2x^{-3/2}$이고, $0<x\le1$에서 $\sqrt x\lvert\ln x\rvert\le2/e$이므로 $\lvert\ln x\rvert/(1+x^2)\le(2/e)x^{-1/2}$이다. [\[미적분학\] §이상적분, ⁋명제 3](/ko/math/calculus/improper_integrals#prop3)에 의하여 $\int_0^\infty$는 수렴한다. 이를 $J$라 하자.

$\operatorname{Log}z=\ln\lvert z\rvert+i\arg z$ ($-\pi/2<\arg z<3\pi/2$)로 두면 $f(z)=\operatorname{Log}z/(1+z^2)$은 상반평면의 닫힌 영역에서 원점과 $z=i$를 제외하고 holomorphic이다. $0<\varepsilon<1<R$에 대해 경로는 $[\varepsilon,R]$, 반원호 $C_R$($\theta:0\to\pi$), $[-R,-\varepsilon]$, 원점을 도는 작은 반원 $c_\varepsilon$($\theta:\pi\to0$, 시계방향)을 차례로 잇는다. 경로 안의 극은 $z=i$ 하나이고 [§유수정리, ⁋명제 3](/ko/math/complex_analysis/residue_theorem#prop3)에 의하여 $\operatorname{Res}_{z=i}f=\operatorname{Log}i/(2i)=(i\pi/2)/(2i)=\pi/4$이므로 경로 적분은 $2\pi i\cdot\pi/4=i\pi^2/2$이다.

$[\varepsilon,R]$ 위에서의 적분은 $\int_\varepsilon^R\ln x/(1+x^2)\dd{x}$이다. $[-R,-\varepsilon]$에서는 $z=-x$로 놓으면 $\operatorname{Log}z=\ln x+i\pi$이고 $\dd{z}=-\dd{x}$, $x$는 $R$에서 $\varepsilon$까지이므로

$$\int_{-R}^{-\varepsilon}f\dd{z}=\int_\varepsilon^R\frac{\ln x+i\pi}{1+x^2}\dd{x}$$

이다. 두 선분의 합은 $\varepsilon\to0$, $R\to\infty$에서 $2J+i\pi\int_0^\infty\dd{x}/(1+x^2)=2J+i\pi^2/2$이다. 큰 반원 위에서는 $\lvert\operatorname{Log}z\rvert\le\ln R+\pi$이고 $\lvert1+z^2\rvert\ge R^2-1$이므로

$$\left\lvert\int_{C_R}f\dd{z}\right\rvert\le\frac{\ln R+\pi}{R^2-1}\cdot\pi R\longrightarrow0$$

이다. 작은 반원 위에서는 $\lvert\operatorname{Log}z\rvert\le\lvert\ln\varepsilon\rvert+\pi$이고 $\lvert1+z^2\rvert\ge1-\varepsilon^2$이므로

$$\left\lvert\int_{c_\varepsilon}f\dd{z}\right\rvert\le\frac{\lvert\ln\varepsilon\rvert+\pi}{1-\varepsilon^2}\cdot\pi\varepsilon\longrightarrow0$$

이다. 마지막 극한은 $\varepsilon\ln\varepsilon\to0$에서 온다. 따라서 $2J+i\pi^2/2=i\pi^2/2$이고 $J=0$이다.
:::

## cotangent를 이용한 급수의 합

[§유수정리, ⁋정리 2](/ko/math/complex_analysis/residue_theorem#thm2)는 무한급수의 합에도 쓰인다. 함수 $\pi\cot\pi z=\pi\cos\pi z/\sin\pi z$는 분모 $\sin\pi z$가 정확히 정수에서 단순영점을 가지므로 모든 정수에서 단순극을 갖고, [§유수정리, ⁋명제 3](/ko/math/complex_analysis/residue_theorem#prop3)에 의하여 $z=n$에서의 residue는

$$\operatorname{Res}_{z=n}\frac{\pi\cos\pi z}{\sin\pi z}=\frac{\pi\cos\pi n}{(\sin\pi z)'\vert_{z=n}}=\frac{\pi\cos\pi n}{\pi\cos\pi n}=1$$

이다. 따라서 $f$가 $n$에서 holomorphic이면 $\pi\cot(\pi z)f(z)$의 $n$에서의 residue는 $f(n)$이고, 이 함수를 큰 경로에서 적분하면 $\sum f(n)$이 나타난다. 경로는 정수를 피해야 하므로 정사각형 $\Gamma_N$의 꼭짓점을 $(\pm(N+1/2),\pm(N+1/2))$로 잡는다.

::: 명제 13 (cotangent 합 공식)
$P,Q$가 polynomial이고 $\deg Q\ge\deg P+2$이며 $f=P/Q$의 극이 정수가 아니라 하자. 그럼

$$\sum_{n=-\infty}^{\infty}f(n)=-\sum_{j}\operatorname{Res}_{z=z_j}\bigl[\pi\cot(\pi z)f(z)\bigr]$$

이다. 오른쪽 합은 $f$의 극 $z_j$ 전체에 걸친다.
:::

::: 증명
먼저 $\Gamma_N$ 위에서 $\lvert\cot\pi z\rvert$가 $N$과 무관한 상수로 유계임을 보인다. 수직변 $z=\pm(N+1/2)+iy$에서 $\cos(\pi z)=\mp i(-1)^N\sinh\pi y$, $\sin(\pi z)=(-1)^N\cosh\pi y$이므로 $\lvert\cot\pi z\rvert=\lvert\tanh\pi y\rvert\le1$이다. 수평변 $z=x\pm i(N+1/2)$에서는 $s=\sinh^2\pi y$로 두면

$$\lvert\cot\pi z\rvert^2=\frac{\cos^2\pi x+s}{\sin^2\pi x+s}\le\frac{1+s}{s}=\coth^2\pi y$$

이다. 부등호는 $u=\sin^2\pi x$로 두고 $(1-u+s)s\le(u+s)(1+s)$를 전개하면 $-us\le u+us$가 되어 성립한다. $\lvert y\rvert=N+1/2\ge1/2$이므로 $\lvert\cot\pi z\rvert\le\coth(\pi/2)=:C$이고, 수직변에서도 $1\le C$이므로 $\Gamma_N$ 전체에서 $\lvert\cot\pi z\rvert\le C$이다.

$\deg Q\ge\deg P+2$이므로 [명제 1](#prop1)의 증명과 같이 $\lvert z\rvert\ge R_0$에서 $\lvert f(z)\rvert\le A/\lvert z\rvert^2$이다. $N$을 $N+1/2>R_0$이고 $f$의 모든 극이 $\Gamma_N$ 안쪽에 놓일 만큼 크게 잡으면 $\Gamma_N$ 위에서 $\lvert z\rvert\ge N+1/2$이다. $\Gamma_N$의 둘레가 $8(N+1/2)$이므로 [§복소적분, ⁋명제 6](/ko/math/complex_analysis/complex_integration#prop6)에서

$$\left\lvert\oint_{\Gamma_N}\pi\cot(\pi z)f(z)\dd{z}\right\rvert\le\pi C\cdot\frac{A}{(N+\frac12)^2}\cdot8\Bigl(N+\frac12\Bigr)=\frac{8\pi CA}{N+\frac12}\longrightarrow0$$

이다. 한편 $\Gamma_N$ 안의 극은 정수 $-N,\dots,N$과 $f$의 극들이므로 [§유수정리, ⁋정리 2](/ko/math/complex_analysis/residue_theorem#thm2)로

$$\frac{1}{2\pi i}\oint_{\Gamma_N}\pi\cot(\pi z)f(z)\dd{z}=\sum_{n=-N}^{N}f(n)+\sum_j\operatorname{Res}_{z=z_j}\bigl[\pi\cot(\pi z)f(z)\bigr]$$

이다. $\lvert f(n)\rvert\le A/n^2$이므로 $\sum f(n)$은 절대수렴하여 $N\to\infty$에서 $\sum_{n=-N}^{N}f(n)\to\sum_{n=-\infty}^{\infty}f(n)$이다. 좌변이 $0$으로 가므로 주장을 얻는다.
:::

차수 조건이 $\deg Q\ge\deg P+2$인 이유는 두 가지이다. 급수 $\sum f(n)$이 절대수렴해야 하고, 둘레가 $N$에 비례하는 $\Gamma_N$ 위에서 ML 부등식이 $N\to\infty$에서 $0$을 주어야 한다. 가령 $f(z)=1/z$이면 둘째 조건이 깨져서 위 어림이 상수를 줄 뿐이다.

::: 예시 14 (Basel 문제)
$a>0$일 때 $f(z)=1/(z^2+a^2)$는 [명제 13](#prop13)의 조건을 만족하고 극은 $\pm ia$이다. $\cot(i\pi a)=\cos(i\pi a)/\sin(i\pi a)=\cosh(\pi a)/(i\sinh\pi a)=-i\coth\pi a$이므로

$$\operatorname{Res}_{z=ia}\frac{\pi\cot\pi z}{z^2+a^2}=\frac{\pi\cot(i\pi a)}{2ia}=-\frac{\pi\coth\pi a}{2a}$$

이고, $\cot$이 기함수이므로 $z=-ia$에서도 같은 값이다. [명제 13](#prop13)에서

$$\sum_{n=-\infty}^{\infty}\frac{1}{n^2+a^2}=\frac{\pi\coth\pi a}{a}$$

이고, 좌변을 $1/a^2+2\sum_{n\ge1}1/(n^2+a^2)$로 쓰면 다음의 식을 얻는다.

$$\sum_{n=1}^{\infty}\frac{1}{n^2+a^2}=\frac{\pi a\coth\pi a-1}{2a^2}$$

$0<a\le1$에서 $1/(n^2+a^2)\le1/n^2$이므로 급수는 $a$에 대해 균등수렴하고 $a\to0^+$에서 극한을 항별로 취할 수 있다. $x\coth x=(1+x^2/2+\cdots)/(1+x^2/6+\cdots)=1+x^2/3+O(x^4)$이므로 $\pi a\coth\pi a-1=\pi^2a^2/3+O(a^4)$이고

$$\sum_{n=1}^{\infty}\frac{1}{n^2}=\lim_{a\to0^+}\frac{\pi^2a^2/3+O(a^4)}{2a^2}=\frac{\pi^2}{6}$$

이다.
:::

---

**참고문헌**

**[Ahl]** L.V. Ahlfors, *Complex analysis*, 3rd ed., McGraw–Hill, 1979.  
**[Con]** J.B. Conway, *Functions of one complex variable I*, 2nd ed., Graduate Texts in Mathematics 11, Springer, 1978.  
**[SS]** E.M. Stein, R. Shakarchi, *Complex analysis*, Princeton Lectures in Analysis II, Princeton University Press, 2003.
