---
title: "사상의 차수와 Brouwer·Lefschetz 고정점 정리"
description: "H_n(S^n)=Z를 이용해 구면 자기사상의 차수를 정의하고 그 성질을 확립한 뒤, no-retraction 보조정리로 Brouwer 고정점 정리와 hairy ball 정리를, 호몰로지 대각합으로 Lefschetz 고정점 정리를 증명한다."
excerpt: "Mapping degree, the Brouwer and Lefschetz fixed-point theorems, and the hairy ball theorem"

categories: [Math / Algebraic Topology]
permalink: /ko/math/algebraic_topology/degree_and_fixed_point_theorems
sidebar: 
    nav: "algebraic_topology-ko"

date: 2026-07-01
last_modified_at: 2026-07-01
weight: 5.5

published: false

---

## 구면의 호몰로지와 사상의 차수

앞선 글에서 우리는 homology를 계산하는 도구들을 마련하였고, 특히 Mayer-Vietoris exact sequence를 이용해 여러 공간의 homology를 얻을 수 있음을 보았다. ([§호몰로지의 계산, ⁋명제 7](/ko/math/algebraic_topology/computation_of_homology#prop7)) 이 절의 출발점은 구 $S^n$의 최고차 homology가 정확히 $\mathbb{Z}$ 하나라는 사실이다. 이 사실은 대단히 강력한 결과를 함축한다. 임의의 연속함수 $f:S^n\rightarrow S^n$은 함수 $H_n(f):H_n(S^n)\rightarrow H_n(S^n)$을 유도하는데 ([§호몰로지, ⁋명제 12](/ko/math/algebraic_topology/homology#prop12)), $H_n(S^n)\cong\mathbb{Z}$이므로 $\mathbb{Z}$에서 $\mathbb{Z}$로의 group homomorphism은 어떤 정수를 곱하는 것에 지나지 않는다. 곧 임의의 자기사상 $f$에 정수 하나가 자연스럽게 붙으며, 우리는 이 정수 하나가 fixed point의 존재나 구면 위의 벡터장 문제와 같은 기하학적 물음들을 지배함을 보게 된다.

먼저 구의 homology를 확정한다. 표기의 편의를 위해, [§호몰로지의 계산, ⁋명제 4](/ko/math/algebraic_topology/computation_of_homology#prop4) 부근에서 도입한 reduced homology $\widetilde{H}_k(X)=H_k(X,x)$를 사용한다. 이는 nonempty path-connected space에 대하여 $H_k(X)$와 $k>0$에서 일치하고 $k=0$에서만 $\mathbb{Z}$ 하나만큼 작다.

::: 명제 1
모든 $n\geq 0$에 대하여, reduced homology는

$$\widetilde{H}_k(S^n)\cong\begin{cases}\mathbb{Z}&k=n\\ 0&k\neq n\end{cases}$$

으로 주어진다. 특히 $n\geq 1$이면 $H_n(S^n)\cong\mathbb{Z}$이고 $0<k<n$과 $k>n$에 대하여 $H_k(S^n)=0$이며, $H_0(S^n)\cong\mathbb{Z}$이다.
:::
::: 증명
$n$에 대한 귀납법을 사용한다. 기저 단계 $n=0$에서 $S^0$은 두 점으로 이루어진 공간이므로 [§호몰로지, ⁋명제 9](/ko/math/algebraic_topology/homology#prop9)와 [§호몰로지, ⁋명제 10](/ko/math/algebraic_topology/homology#prop10)에 의하여 $H_0(S^0)\cong\mathbb{Z}\oplus\mathbb{Z}$이고 다른 homology는 모두 $0$이다. 한 점을 없애는 reduced homology의 정의에 의하여 $\widetilde{H}_0(S^0)\cong\mathbb{Z}$이고 다른 degree에서는 $0$이므로 주장이 성립한다.

이제 $n\geq 1$이라 하고 $S^{n-1}$에 대하여 주장이 성립한다고 가정하자. $S^n$을 북극과 남극을 각각 조금 넘겨 부풀린 두 열린집합

$$U=S^n\setminus\{\text{남극}\},\qquad V=S^n\setminus\{\text{북극}\}$$

의 합집합으로 나타내자. 각 극을 뺀 $U,V$는 stereographic projection에 의해 $\mathbb{R}^n$과 homeomorphic하므로 contractible이고, 교집합 $U\cap V$는 적도 방향으로 $S^{n-1}$에 deformation retract한다. [§호몰로지의 계산, ⁋명제 7](/ko/math/algebraic_topology/computation_of_homology#prop7)의 Mayer-Vietoris exact sequence는 계수와 무관하게 성립하며, 이를 reduced homology 판본으로 적용하면 각 $k$에 대하여 exact sequence

$$\widetilde{H}_k(U)\oplus\widetilde{H}_k(V)\rightarrow\widetilde{H}_k(S^n)\overset{\partial}{\longrightarrow}\widetilde{H}_{k-1}(U\cap V)\rightarrow\widetilde{H}_{k-1}(U)\oplus\widetilde{H}_{k-1}(V)$$

을 얻는다. $U,V$가 contractible이므로 양 끝 항이 모두 $0$이고, 따라서 connecting homomorphism $\partial$은 isomorphism

$$\widetilde{H}_k(S^n)\cong\widetilde{H}_{k-1}(U\cap V)\cong\widetilde{H}_{k-1}(S^{n-1})$$

을 준다. 귀납가정에 의하여 우변은 $k-1=n-1$, 곧 $k=n$일 때 $\mathbb{Z}$이고 그 밖에서는 $0$이므로 원하는 결과를 얻는다.
:::

증명의 귀납 단계는 $S^n$의 최고차 homology를 한 차원 낮은 구의 최고차 homology로 되돌린다. 이 반복적 isomorphism $\widetilde{H}_n(S^n)\cong\widetilde{H}_{n-1}(S^{n-1})\cong\cdots\cong\widetilde{H}_0(S^0)\cong\mathbb{Z}$을 따라 $\widetilde{H}_0(S^0)$의 한 generator를 끌어올린 것을 $H_n(S^n)$의 한 generator로 택할 수 있으며, 우리는 이를 $[S^n]$으로 적고 $S^n$의 *fundamental class<sub>기본류</sub>*라 부른다. 이후의 논의에서 중요한 것은 이 generator의 구체적인 모습이 아니라 $H_n(S^n)$이 정확히 무한순환군이라는 사실뿐이다.

::: 정의 2
$n\geq 1$에 대하여, 연속함수 $f:S^n\rightarrow S^n$을 생각하자. 유도된 준동형 $f_\ast=H_n(f):H_n(S^n)\rightarrow H_n(S^n)$은 $H_n(S^n)\cong\mathbb{Z}$ 위에서 어떤 정수를 곱하는 것이므로, 유일한 정수 $d$가 존재하여

$$f_\ast(\alpha)=d\cdot\alpha\qquad(\alpha\in H_n(S^n))$$

이 성립한다. 이 정수 $d$를 $f$의 *degree<sub>차수</sub>*라 부르고 $\deg f$로 적는다.
:::

정의에서 정수 $\deg f$는 $f_\ast[S^n]=(\deg f)\cdot[S^n]$이라는 식으로 결정된다. 이 값이 generator $[S^n]$의 선택에 의존하지 않음을 짚어두자. 만일 다른 generator를 택한다면 그것은 $\pm[S^n]$뿐이며, $f_\ast(-[S^n])=-f_\ast[S^n]=-(\deg f)[S^n]=(\deg f)(-[S^n])$이므로 곱해지는 정수는 여전히 $\deg f$이다. 곧 $\deg f$는 $\mathbb{Z}\rightarrow\mathbb{Z}$인 group endomorphism이 유일하게 결정하는 정수 그 자체이며, generator의 부호와 무관한 불변량이다.

## 차수의 기본 성질

Degree가 유용한 불변량이 되는 것은 그것이 함수의 연속적 변형에 둔감하면서도 합성과는 잘 맞물리기 때문이다. 다음 명제는 degree의 대수적 성질들을 모은 것이다.

::: 명제 3
$n\geq 1$에 대한 연속함수들 $f,g:S^n\rightarrow S^n$에 대하여 다음이 성립한다.

1. $\deg\id_{S^n}=1$이다.
2. $f$와 $g$가 homotopic하면 $\deg f=\deg g$이다.
3. $f$가 상수함수이면 $\deg f=0$이다.
4. $\deg(g\circ f)=(\deg g)(\deg f)$이다.
:::
::: 증명
(1) $\id_{S^n}$은 $H_n$에서 항등사상을 유도하므로 ($H_n$이 functor이기 때문이다) 곱해지는 정수는 $1$이다.

(2) 두 homotopic map은 homology에서 같은 준동형을 유도하므로 ([§호모토피, ⁋명제 6](/ko/math/algebraic_topology/homotopy#prop6)) $f_\ast=g_\ast$이고 따라서 $\deg f=\deg g$이다.

(3) $f$가 상수함수라 하자. 그럼 $f$는 한 점 $\ast$를 거쳐 $S^n\rightarrow\ast\rightarrow S^n$으로 인수분해된다. 따라서 functoriality에 의하여 $f_\ast$는 $H_n(S^n)\rightarrow H_n(\ast)\rightarrow H_n(S^n)$을 통과하는데, $n\geq 1$에 대하여 $H_n(\ast)=0$이므로 ([§호몰로지, ⁋명제 11](/ko/math/algebraic_topology/homology#prop11)) $f_\ast=0$이고 $\deg f=0$이다.

(4) Functoriality에 의하여 $(g\circ f)_\ast=g_\ast\circ f_\ast$이다. $f_\ast$가 $\deg f$를, $g_\ast$가 $\deg g$를 곱하는 morphism이므로 그 합성은 $(\deg g)(\deg f)$를 곱하는 morphism이고, 이것이 $\deg(g\circ f)$이다.
:::

성질 (2)는 degree가 homotopy 불변량임을 말한다. 이 사실은 degree의 위력의 근원이다. 예를 들어 두 morphism의 degree가 다르면 그들은 결코 homotopic할 수 없으며, 뒤에서 보듯 이 관찰만으로 hairy ball 정리가 따라 나온다. 성질 (1)과 (3)을 합하면 $\id_{S^n}$은 상수함수와 homotopic하지 않다는 것, 곧 $S^n$은 contractible하지 않다는 것을 즉시 얻는다.

이제 degree가 실제로 $0$과 $1$ 이외의 값을 가질 수 있음을, 반사사상과 antipodal morphism을 통해 확인한다.

::: 명제 4
$i$번째 좌표의 부호를 바꾸는 반사사상

$$r:S^n\rightarrow S^n;\qquad r(x_0,\ldots,x_i,\ldots,x_n)=(x_0,\ldots,-x_i,\ldots,x_n)$$

의 degree는 $\deg r=-1$이다.
:::
::: 증명
좌표의 이름을 바꾸어도 일반성을 잃지 않으므로 마지막 좌표를 뒤집는 반사사상을 생각하자. [명제 1](#prop1)의 증명에서 사용한 분해 $S^n=U\cup V$를 북극과 남극이 마지막 좌표축 위에 놓이도록 택하면, 이 반사사상은 두 극을 맞바꾸어 $U$와 $V$를 서로 보내고 적도 $U\cap V\simeq S^{n-1}$을 자기 자신으로 보내되 그 위에서 한 좌표를 뒤집는 반사사상으로 작용한다. Mayer-Vietoris의 connecting homomorphism은 이러한 morphism들에 대하여 자연스러우므로, [명제 1](#prop1)의 isomorphism $\widetilde{H}_n(S^n)\cong\widetilde{H}_{n-1}(S^{n-1})$ 아래에서 $S^n$의 반사사상이 유도하는 준동형은 $S^{n-1}$의 반사사상이 유도하는 준동형과 일치한다. 따라서 degree를 계산하는 문제가 한 차원 낮아지며, 귀납적으로 $n=0$의 경우로 환원된다.

$n=0$의 경우, 반사사상은 $S^0$의 두 점을 맞바꾼다. $\widetilde{H}_0(S^0)\cong\mathbb{Z}$은 두 점의 형식적 차 $[p_+]-[p_-]$가 생성하는데, 두 점을 맞바꾸는 morphism은 이 generator를 $[p_-]-[p_+]$, 곧 그 부호를 뒤집은 것으로 보내므로 유도되는 준동형은 $-1$을 곱하는 morphism이다. 따라서 반사사상의 degree는 $-1$이며, 귀납법에 의하여 모든 $n\geq 0$에서 $\deg r=-1$이다.
:::

::: 따름정리 5
Antipodal morphism $a:S^n\rightarrow S^n$, $a(x)=-x$의 degree는 $\deg a=(-1)^{n+1}$이다.
:::
::: 증명
$S^n\subseteq\mathbb{R}^{n+1}$의 antipodal morphism $x\mapsto-x$은 $n+1$개의 좌표를 모두 뒤집으므로, 각 좌표를 하나씩 뒤집는 [명제 4](#prop4)의 반사사상 $n+1$개의 합성이다. [명제 3](#prop3)의 성질 (4)에 의하여

$$\deg a=(\deg r)^{n+1}=(-1)^{n+1}$$

이다.
:::

따름정리 5는 antipodal morphism의 degree가 짝수 차원 구와 홀수 차원 구에서 부호가 다름을 말한다. $n$이 짝수이면 $\deg a=-1$이므로 $a$는 $\id$과 homotopic하지 않고, $n$이 홀수이면 $\deg a=1$로 $\id$과 degree가 같다. 이 부호 차이가 이어지는 절에서 벡터장의 존재 문제를 가른다.

## No-retraction 보조정리와 Brouwer 고정점 정리

Homology가 fixed point 문제에 개입하는 첫 통로는 원판을 그 boundary로 밀어내는 연속함수, 곧 retraction이 존재할 수 없다는 사실이다. $(n+1)$-공 $D^{n+1}=\{x\in\mathbb{R}^{n+1}\mid\lvert x\rvert\leq 1\}$의 boundary가 $S^n$임을 상기하자. Retraction이란 이 포함관계를 되돌리는 morphism이다.

::: 보조정리 6 (No-retraction)
$n\geq 0$에 대하여, 포함사상 $\iota:S^n\hookrightarrow D^{n+1}$의 retraction, 곧 $r\circ\iota=\id_{S^n}$을 만족하는 연속함수 $r:D^{n+1}\rightarrow S^n$은 존재하지 않는다.
:::
::: 증명
그러한 $r$가 존재한다고 가정하고 모순을 이끌어낸다. 먼저 $n\geq 1$인 경우를 보자. $r\circ\iota=\id_{S^n}$의 양변에 $H_n$을 취하면 functoriality에 의하여

$$H_n(S^n)\overset{\iota_\ast}{\longrightarrow}H_n(D^{n+1})\overset{r_\ast}{\longrightarrow}H_n(S^n)$$

의 합성이 $H_n(S^n)$ 위의 항등사상이 된다. 그런데 $D^{n+1}$은 convex 집합이므로 한 점으로 deformation retract하는 contractible 공간이고, 따라서 $n\geq 1$에 대하여 $H_n(D^{n+1})\cong H_n(\ast)=0$이다. ([§호몰로지, ⁋명제 11](/ko/math/algebraic_topology/homology#prop11)) 곧 항등사상 $\id:H_n(S^n)\rightarrow H_n(S^n)$이 $0$을 통과하게 되는데, [명제 1](#prop1)에 의하여 $H_n(S^n)\cong\mathbb{Z}\neq 0$이므로 이는 모순이다.

$n=0$인 경우, $S^0$은 두 점, $D^1=[-1,1]$은 connected인 구간이다. $r:[-1,1]\rightarrow S^0$이 연속이고 두 끝점을 각각 자기 자신으로 보낸다면, connected space의 연속상은 connected이어야 하는데 $S^0$은 connected가 아니고 $r$의 상은 두 점을 모두 포함하므로 모순이다.
:::

No-retraction 보조정리는 그 자체로도 흥미롭지만, 그 진정한 쓰임은 fixed point 정리로의 환원에 있다. 만일 어떤 자기사상이 fixed point를 갖지 않는다면, 각 점을 그 상으로부터 멀어지는 방향으로 밀어 boundary에 닿게 하는 방식으로 retraction을 만들 수 있고, 이는 보조정리에 어긋난다. 이 착상을 엄밀히 하면 다음의 고전적 정리가 얻어진다.

::: 정리 7 (Brouwer 고정점 정리)
$n\geq 0$에 대하여, 임의의 연속함수 $f:D^{n+1}\rightarrow D^{n+1}$은 fixed point를 갖는다. 곧 $f(x)=x$인 점 $x\in D^{n+1}$이 존재한다.
:::
::: 증명
$f$가 fixed point를 갖지 않는다고 가정하자. 그럼 모든 $x\in D^{n+1}$에 대하여 $f(x)\neq x$이므로, $f(x)$에서 시작하여 $x$를 지나는 반직선을 그을 수 있다. 이 반직선이 boundary $S^n$과 만나는 점을 $r(x)$라 정의하자. 구체적으로 $r(x)=x+t(x)(x-f(x))$의 꼴이며, 여기에서 $t(x)\geq 0$은 $\lvert r(x)\rvert=1$이 되도록 정해지는 유일한 값이다. 이 $t(x)$는 이차방정식 $\lvert x+t(x-f(x))\rvert^2=1$의 음이 아닌 근으로 주어지며, $x-f(x)\neq 0$이므로 그 계수가 연속적으로 변하고 판별식이 양이어서 $t(x)$, 따라서 $r(x)$가 $x$에 대하여 연속이다.

이제 $x\in S^n$이면 $\lvert x\rvert=1$이므로 반직선이 boundary와 만나는 점은 $x$ 자신, 곧 $t(x)=0$이고 $r(x)=x$이다. 따라서 $r:D^{n+1}\rightarrow S^n$은 연속함수이면서 $S^n$ 위에서 항등사상이 되는 retraction이다. 이는 [보조정리 6](#lem6)에 모순이므로, $f$는 fixed point를 가져야 한다.
:::

Brouwer 정리는 $D^{n+1}$이 convex하고 콤팩트하다는 위상적 성질만으로 fixed point의 존재를 보장한다. 그 힘은 morphism $f$에 대한 어떠한 규칙성도 요구하지 않는 데 있다. 우리는 뒤에서 이 정리가 훨씬 일반적인 Lefschetz fixed point 정리의 특수한 경우임을 확인하게 될 것이다.

## Hairy ball 정리

이제 degree의 homotopy 불변성을 벡터장 문제에 적용한다. 구 $S^n$ 위의 tangent vector field란, 각 점 $x\in S^n$에 그 점에서의 tangent space의 벡터, 곧 $x$와 수직인 벡터 $v(x)\in\mathbb{R}^{n+1}$을 연속적으로 대응시키는 것이다. "어디서도 $0$이 아닌" tangent vector field가 존재하는가라는 물음은 구를 빗질하여 가마 없이 매끈하게 눕힐 수 있는가라는 직관적 물음과 같으며, 그 답은 오직 degree에 의해 결정된다.

::: 정리 8 (Hairy ball 정리)
$S^n$ 위에 어디서도 $0$이 아닌 연속 tangent vector field가 존재할 필요충분조건은 $n$이 홀수인 것이다.
:::
::: 증명
먼저 그러한 벡터장 $v$가 존재한다고 가정하자. 각 점에서 $v(x)\neq 0$이므로 $v(x)/\lvert v(x)\rvert$로 normalize하여 처음부터 $\lvert v(x)\rvert=1$이라 두어도 무방하다. Tangent vector field라는 조건은 모든 $x$에 대하여 $x\cdot v(x)=0$을 뜻한다. 이제 함수

$$H:S^n\times[0,1]\rightarrow S^n;\qquad H(x,t)=(\cos\pi t)x+(\sin\pi t)v(x)$$

를 생각하자. $x$와 $v(x)$가 서로 수직인 단위벡터이므로

$$\lvert H(x,t)\rvert^2=\cos^2\pi t\cdot\lvert x\rvert^2+\sin^2\pi t\cdot\lvert v(x)\rvert^2=\cos^2\pi t+\sin^2\pi t=1$$

이고, 따라서 $H$는 실제로 $S^n$으로 가는 값을 가진다. 나아가 $H(x,0)=x$이고 $H(x,1)=-x$이므로, $H$는 항등사상 $\id_{S^n}$에서 antipodal morphism $a$로의 homotopy이다. [명제 3](#prop3)의 성질 (2)에 의하여 $\deg\id_{S^n}=\deg a$, 곧 [따름정리 5](#cor5)에 의하여

$$1=(-1)^{n+1}$$

이어야 하고, 이는 $n+1$이 짝수, 곧 $n$이 홀수임을 강제한다.

역으로 $n$이 홀수라 하자. 그럼 $n+1=2m$이 짝수이고, $S^n\subseteq\mathbb{R}^{2m}$의 좌표를 $(x_1,\ldots,x_{2m})$이라 할 때

$$v(x_1,x_2,\ldots,x_{2m-1},x_{2m})=(-x_2,x_1,\ldots,-x_{2m},x_{2m-1})$$

로 정의하면, 이는 연속이며 $\lvert v(x)\rvert=\lvert x\rvert=1$이므로 어디서도 $0$이 아니다. 또한

$$x\cdot v(x)=-x_1x_2+x_2x_1-\cdots-x_{2m-1}x_{2m}+x_{2m}x_{2m-1}=0$$

이므로 $v$는 tangent vector field이다. 따라서 $n$이 홀수이면 그러한 벡터장이 존재한다.
:::

특히 $S^2$처럼 짝수 차원 구에서는 어디서도 $0$이 아닌 tangent vector field가 존재하지 않는다. 곧 지구 표면의 바람은 어딘가에서 반드시 잦아든다. 증명의 핵심은 $0$이 아닌 tangent vector field가 있으면 그것을 회전의 매개변수로 삼아 $\id$을 antipodal morphism까지 연속적으로 끌고 갈 수 있고, 두 morphism의 degree가 같아야 한다는 제약이 곧바로 $n$의 홀짝성을 결정한다는 데 있다. 이 논증은 오직 degree만을 사용하며 어떠한 추가적 불변량도 필요로 하지 않는다.

## Lefschetz 고정점 정리

Brouwer 정리는 원판이라는 특정한 공간에 대한 결과였다. 이를 임의의 콤팩트 공간으로 확장하려면, 자기사상이 homology에 남기는 흔적 전체를 하나의 정수로 요약하는 불변량이 필요하다. 그 불변량이 Lefschetz 수이며, 이를 정의하기 위해 우리는 계수를 유리수로 바꾼 homology를 사용한다. [§호몰로지의 계산, ⁋정의 6](/ko/math/algebraic_topology/computation_of_homology#def6) 이후의 논의에서 보았듯 계수군을 임의의 abelian group으로 바꾸어도 homology 이론은 그대로 성립하므로, 계수를 $\mathbb{Q}$로 잡은 homology $H_i(X;\mathbb{Q})=H_i(X)\otimes_\mathbb{Z}\mathbb{Q}$를 생각할 수 있다. 이는 $\mathbb{Q}$ 위의 vector space이며, $X$가 유한 CW complex이거나 삼각화가능한 콤팩트 공간이면 각 $H_i(X;\mathbb{Q})$는 유한차원이고 충분히 큰 $i$에 대하여 $0$이다. 유한차원 vector space 사이의 선형사상에는 trace $\operatorname{tr}$이 정의되므로, 다음이 유의미하다.

::: 정의 9
$X$를 유한 CW complex이거나 삼각화가능한 콤팩트 공간이라 하고, $f:X\rightarrow X$를 연속함수라 하자. 각 $i$에 대하여 유도된 선형사상 $f_\ast:H_i(X;\mathbb{Q})\rightarrow H_i(X;\mathbb{Q})$의 trace를 취하여 얻는 정수

$$L(f)=\sum_{i\geq 0}(-1)^i\operatorname{tr}\bigl(f_\ast:H_i(X;\mathbb{Q})\rightarrow H_i(X;\mathbb{Q})\bigr)$$

를 $f$의 *Lefschetz number<sub>레프셰츠 수</sub>*라 부른다.
:::

정의의 합은 유한합이다. $X$가 위의 조건을 만족하면 유한개의 $i$에 대해서만 $H_i(X;\mathbb{Q})\neq 0$이기 때문이다. 또한 $L(f)$는 각 trace가 정수가 아닐 수도 있지만 그 교대합은 항상 정수가 되는데, 이는 $f_\ast$가 실제로는 정수계수 homology 위의 준동형에서 유래하기 때문이다. Lefschetz 수는 명백히 homotopy 불변량이다. Homotopic한 두 morphism은 각 $H_i(X;\mathbb{Q})$ 위에서 같은 선형사상을 유도하므로 trace가 일치한다. 특별히 $f=\id_X$이면 각 $f_\ast$가 항등사상이고 그 trace는 $\dim_\mathbb{Q}H_i(X;\mathbb{Q})$, 곧 $i$번째 Betti 수이므로 $L(\id_X)=\sum_i(-1)^i\dim_\mathbb{Q}H_i(X;\mathbb{Q})$은 $X$의 Euler characteristic과 같다.

::: 정리 10 (Lefschetz 고정점 정리)
$X$를 유한 CW complex이거나 삼각화가능한 콤팩트 공간이라 하고, $f:X\rightarrow X$를 연속함수라 하자. 만일 $L(f)\neq 0$이면 $f$는 fixed point를 갖는다.
:::
::: 증명
대우, 곧 $f$가 fixed point를 갖지 않으면 $L(f)=0$임을 보인다. 증명은 두 개의 축으로 이루어지며, 여기에서는 그 골격만 제시하고 세부는 [Hat]의 §2.C에 넘긴다.

첫째 축은 순수하게 algebraic한 사실, 곧 trace의 교대합이 chain 준위에서 계산되어도 homology 준위에서 계산되어도 같다는 것이다. 유한차원 $\mathbb{Q}$-vector space들의 chain complex $(C_i,\partial)$와 그 위의 chain map $\varphi_\ast=(\varphi_i)$가 주어지면

$$\sum_i(-1)^i\operatorname{tr}(\varphi_i:C_i\rightarrow C_i)=\sum_i(-1)^i\operatorname{tr}(\varphi_\ast:H_i\rightarrow H_i)$$

가 성립한다. 이는 각 $C_i$를 cycle, boundary, 그리고 그 여공간으로 분해하여 trace를 항별로 세면 얻어지는데, boundary와 여공간의 기여가 이웃한 degree에서 부호를 달리하며 상쇄되고 오직 homology의 기여만 남기 때문이다. 이 항등식을 *Hopf trace formula*라 부른다.

둘째 축은 기하이다. $f$가 fixed point를 갖지 않으면, $X$가 콤팩트하므로 $x$와 $f(x)$ 사이의 거리에 양의 하한 $\varepsilon>0$이 존재한다. $X$의 삼각화를 충분히 잘게 세분하고 simplicial approximation 정리를 적용하면, $f$와 homotopic한 simplicial map $g$를 얻되 각 simplex $\sigma$가 자기 자신과 서로소인 simplex들로 보내지도록, 곧 $g(\sigma)\cap\sigma=\emptyset$이 되도록 할 수 있다. 그럼 $g$가 유도하는 chain 준위의 morphism $g_\#:C_i\rightarrow C_i$은 각 기저 simplex를 자기 자신을 포함하지 않는 chain으로 보내므로 그 행렬의 대각성분이 모두 $0$이고, 따라서 모든 $i$에서 $\operatorname{tr}(g_\#)=0$이다.

두 축을 결합하면, $g$에 Hopf trace formula를 적용하여

$$L(g)=\sum_i(-1)^i\operatorname{tr}(g_\ast:H_i\rightarrow H_i)=\sum_i(-1)^i\operatorname{tr}(g_\#:C_i\rightarrow C_i)=0$$

을 얻는다. 그런데 $g$는 $f$와 homotopic하므로 $L$의 homotopy 불변성에 의하여 $L(f)=L(g)=0$이다. 이로써 대우가 증명된다.
:::

증명에서 두 개의 trace, 곧 눈에 보이지 않는 homology 준위의 trace와 조합적으로 계산 가능한 chain 준위의 trace를 이어붙이는 Hopf trace formula가 결정적 역할을 한다. Fixed point의 부재를 chain 준위의 trace가 $0$이라는 조합적 진술로 번역하고, 그것을 다시 homology 준위의 정보인 $L(f)$로 되돌리는 것이 논증의 전부이다. 이제 이 정리로부터 Brouwer 정리가 특수한 경우로 따라 나옴을 확인한다.

::: 따름정리 11
$X$가 삼각화가능한 콤팩트 공간이면서 contractible하면, 임의의 연속함수 $f:X\rightarrow X$는 fixed point를 갖는다. 특히 [정리 7](#thm7)의 Brouwer 정리가 성립한다.
:::
::: 증명
$X$가 contractible하면 한 점과 같은 homology를 가지므로 ([§호몰로지, ⁋명제 11](/ko/math/algebraic_topology/homology#prop11)) $H_0(X;\mathbb{Q})\cong\mathbb{Q}$이고 $i>0$에 대하여 $H_i(X;\mathbb{Q})=0$이다. $X$는 path-connected이므로 $f_\ast:H_0(X;\mathbb{Q})\rightarrow H_0(X;\mathbb{Q})$은 항등사상이고 그 trace는 $1$이다. 따라서

$$L(f)=(-1)^0\cdot 1=1\neq 0$$

이므로 [정리 10](#thm10)에 의하여 $f$는 fixed point를 갖는다. 특히 $D^{n+1}$은 convex하여 contractible하고 삼각형화가능한 콤팩트 공간이므로 ($n+1$-simplex와 위상동형이다), 임의의 $f:D^{n+1}\rightarrow D^{n+1}$이 fixed point를 가진다는 [정리 7](#thm7)의 Brouwer 정리를 얻는다.
:::

## 예시

::: 예시 12
Degree와 Lefschetz 수의 상호작용을 구면 위에서 구체적으로 살펴본다.

1. **degree의 실현.** $S^1$을 복소평면의 단위원 $\{z\in\mathbb{C}\mid\lvert z\rvert=1\}$으로 보면, 각 정수 $k$에 대하여 $f_k(z)=z^k$은 연속 자기사상이다. $H_1(S^1)\cong\mathbb{Z}$의 generator를 원을 한 바퀴 도는 loop로 볼 때 $f_k$은 이를 $k$바퀴 도는 loop로 보내므로 $\deg f_k=k$이다. 곧 $S^1$의 자기사상은 모든 정수 degree를 실현한다. 더 높은 차원에서도, $S^{n-1}$의 degree $k$ morphism을 $S^n$으로 매다는 suspension을 취하면 degree가 보존되어 ($\id$과 반사사상의 관계가 [명제 4](#prop4)에서 한 차원씩 옮겨간 것과 같은 이유로) 모든 정수 degree의 $S^n$ 자기사상을 얻는다.

2. **구면 위의 Lefschetz 수.** $n\geq 1$에 대하여 $f:S^n\rightarrow S^n$을 생각하자. [명제 1](#prop1)에 의하여 $H_0(S^n;\mathbb{Q})\cong\mathbb{Q}$, $H_n(S^n;\mathbb{Q})\cong\mathbb{Q}$이고 그 밖의 homology는 $0$이다. $S^n$이 path-connected이므로 $f_\ast$는 $H_0$ 위에서 항등사상이어서 trace가 $1$이고, $H_n$ 위에서는 $\deg f$를 곱하는 morphism이어서 trace가 $\deg f$이다. 따라서

    $$L(f)=1+(-1)^n\deg f$$

    이다.

3. **fixed point 없는 morphism의 degree.** [정리 10](#thm10)의 대우에 의하여, $f:S^n\rightarrow S^n$이 fixed point를 갖지 않으면 $L(f)=0$, 곧 $1+(-1)^n\deg f=0$이어야 한다. 이를 풀면 $\deg f=-(-1)^n=(-1)^{n+1}$을 얻는다. 곧 fixed point 없는 구면 자기사상은 반드시 degree $(-1)^{n+1}$을 가진다. Antipodal morphism $a(x)=-x$은 fixed point를 갖지 않으며, 실제로 [따름정리 5](#cor5)에 의하여 $\deg a=(-1)^{n+1}$이므로 이 필요조건과 정확히 부합한다. $L(a)=1+(-1)^n(-1)^{n+1}=1-1=0$이어서 Lefschetz 판정이 fixed point의 부재와 모순되지 않음도 확인된다.

4. **역방향의 결론.** 위 관계를 뒤집으면, $\deg f\neq(-1)^{n+1}$인 $S^n$ 자기사상은 반드시 fixed point를 가진다. 예컨대 $n=2$인 경우 $L(f)=1+\deg f$이므로, $S^2$의 자기사상 중 degree가 $-1$이 아닌 것은 모두 fixed point를 가진다. 특히 degree $0$인 상수함수나 degree $1$인 항등사상은 물론이고, 앞서 만든 degree $k\neq-1$의 어떤 morphism도 fixed point를 피할 수 없다.
:::

이 예시들은 하나의 정수 불변량인 degree가 구면 자기사상의 위상적 행동을 얼마나 촘촘히 통제하는지를 보여준다. Degree는 morphism이 실현할 수 있는 값 전체를 훑고, Lefschetz 수는 그 degree를 fixed point의 존재 여부와 직접 연결한다. 두 불변량이 맞물려, 예컨대 짝수 차원 구에서는 antipodal morphism만이 유일하게 degree를 통해 fixed point를 피할 자격을 얻는다는 섬세한 결론에 이른다.

--- 

**참고문헌**

[Hat] A. Hatcher, *Algebraic Topology*. Cambridge University Press, 2002.  
[Mil] J. W. Milnor, *Topology from the Differentiable Viewpoint*. Princeton University Press, 1997.  
[Mun] J. R. Munkres, *Elements of Algebraic Topology*. Addison-Wesley, 1984.

---
