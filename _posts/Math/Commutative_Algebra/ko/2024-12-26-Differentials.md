---
title: "미분"
description: "라이프니츠 법칙을 만족하는 유도 사상의 정의부터 시작하여 켈러 미분가군의 구조와 representable 성질을 다루고, 다항식환에서의 계산과 국소화, 그리고 추이 완전열과 conormal 완전열을 유도한다. 마지막으로 conormal 완전열을 왼쪽으로 연장하는 naive 코탄젠트 복합체를 정의하고, 그 호몰로지가 표현의 선택과 무관함을 보인다."
excerpt: "Kähler differential module의 universal property와 naive cotangent complex"

categories: [Math / Commutative Algebra]
permalink: /ko/math/commutative_algebra/differentials
drift_needed: true
sidebar: 
    nav: "commutative_algebra-ko"

date: 2024-12-26
weight: 34

---

이번 글에서의 목표는 대수적으로 derivation을 정의하는 것이다. 이로부터 얻어지는 Kähler differential module과 그 두 개의 fundamental exact sequence를 살펴본 뒤, 마지막 두 절에서는 그 가운데 conormal sequence를 왼쪽으로 한 항 더 연장하는 naive cotangent complex를 다룬다. 

## 캘러미분가군

::: 정의 1
Ring $A$와 $A$-algebra $E$, 그리고 $E$-module $M$이 주어졌다 하자. 그럼 다음의 Leibniz rule

$$\dd{(xy)}=y\dd{x}+x\dd{y}$$

을 모든 $x,y\in E$에 대해 만족하는 $A$-linear map들을 *$A$-derivation*이라 부르고 이들의 모임을 $\Der_A(E,M)$으로 적는다. 
:::

Derivation의 기본적인 성질 중 하나는 $\Der_A(E,M)$이 $E$-module 구조를 갖는다는 것으로, 이는 임의의 $x\in E$와 $d\in \Der_A(E, M)$에 대하여, $A$-linear map $x d$를 다음의 식

$$xd: E \rightarrow M;\qquad y\mapsto x\dd{(y)}$$

으로 정의하면 임의의 $y_1,y_2\in E$에 대하여 다음 식

$$(xd)(y_1y_2)=x\dd{(y_1y_2)}=x\, (y_1\dd{y_2}+y_2\dd{y_1})=y_1(xd)(y_2)+y_2(xd)(y_1)$$

이 성립하기 때문이다. 뿐만 아니라 임의의 $A$-derivation $d: E \rightarrow M$과 임의의 $E$-linear map $u:M \rightarrow M'$이 주어졌을 때, 합성

$$u\circ d: E \rightarrow M'$$

또한 $A$-derivation이 되는 것을 확인할 수 있는데, 이는 다음 식

$$(u\circ d)(y_1y_2)=u(y_1\dd{y_2}+y_2\dd{y_1})=y_1u(\dd{y_2})+y_2u(\dd{y_1})=y_1(u\circ d)(y_2)+y_2(u\circ d)(y_1)$$

에 따른 것이다. 즉, $\Der_A(E, -)$는 $\lMod{E}$에서 자기자신으로의 functor가 된다. 

::: 보조정리 2
Functor $\Der_A(E, -)$는 representable하다. 즉, $\lMod{E}$에서 자기자신으로의 두 functor들 사이의 natural isomorphism

$$\Der_A(E,-)\cong\Hom_E(\Omega_{E/A},-)$$

이 성립하도록 하는 $E$-module $\Omega_{E/A}$이 존재한다. 
:::

Representing object $\Omega_{E/A}$는 다음과 같이 정의된다. 

::: 정의 3
$A$-algebra $E$에 대하여, $E$의 $A$에 대한 *Kähler differential module<sub>캘러 미분가군</sub>*은 $\{\dd{f}\mid f\in E\}$로 생성되는 $E$-module에, 다음의 relation들

$$\text{$d(xy)=x\,dy+y\,dx$ for all $x,y\in E$},\qquad \text{$d(ax+by)=a\,dx+b\,dy$ for all $x,y\in E$ and $a,b\in A$}$$

을 주어 만들어지는 $E$-module이며, 이를 $\Omega_{E/A}$로 표기한다. 이 때, $f\mapsto \dd{f}$로 정의되는 $A$-linear derivation $d:E \rightarrow \Omega_{E/A}$를 *universal $A$-derivation<sub>보편 $A$-미분</sub>*이라 적는다. 
:::

그럼 $\Omega_{E/A}$가 [보조정리 2](#lem2)의 universal property를 만족하는 것을 쉽게 확인할 수 있다.

한편 우리는 같은 module을 이미 다른 방식으로 만든 적이 있다. [\[다중선형대수학\] §미분가군, ⁋정의 9](/ko/math/multilinear_algebra/differential_modules#def9)에서는 곱셈사상 $m:E\otimes_AE \rightarrow E$의 kernel $\mathfrak{I}$를 잡아 $E$-module $\mathfrak{I}/\mathfrak{I}^2$을 $A$-differential들의 module로 정의하고, $x\mapsto (x\otimes1-1\otimes x)+\mathfrak{I}^2$이 universal $A$-derivation의 역할을 한다는 것을 보였다. Generator와 relation을 직접 적어 만든 [정의 3](#def3)과는 출발점이 다르지만, 두 구성은 canonical하게 일치한다.

::: 명제 4
$A$-algebra $E$에 대하여, 곱셈사상 $m:E\otimes_AE \rightarrow E$의 kernel을 $\mathfrak{I}$라 하자. 그럼 $(x\otimes1-1\otimes x)+\mathfrak{I}^2$을 $\dd{x}$로 보내는 canonical isomorphism

$$\mathfrak{I}/\mathfrak{I}^2\cong\Omega_{E/A}$$

이 존재한다.
:::
::: 증명
[\[다중선형대수학\] §미분가군, ⁋명제 8](/ko/math/multilinear_algebra/differential_modules#prop8)에 의하여 임의의 $E$-module $M$에 대하여 natural isomorphism $\Hom_E(\mathfrak{I}/\mathfrak{I}^2, M)\cong\Der_A(E, M)$이 성립하고, [보조정리 2](#lem2)에 의하여 $\Omega_{E/A}$ 또한 같은 functor를 표현한다. 즉 두 $E$-module이 $\lMod{E}$ 위의 같은 functor를 표현하므로 이들은 canonical하게 isomorphic하며, 이 isomorphism은 양쪽의 universal $A$-derivation을 서로 옮긴다. 따라서 각각의 $x\in E$에 대하여 $(x\otimes1-1\otimes x)+\mathfrak{I}^2$이 $\dd{x}$로 옮겨진다.
:::

가장 기본적인 경우인 polynomial algebra 위에서 이 module은 좌표들의 differential이 이루는 free module이 된다.

::: 명제 5
집합 $S$에 대한 polynomial algebra $R=A[\x_s]_{s\in S}$에 대하여, $\Omega_{R/A}$는 $\{\dd{\x_s}\}_{s\in S}$를 기저로 하는 free $R$-module이며, 임의의 $f\in R$에 대하여

$$\dd{f}=\sum_{s\in S}\frac{\partial f}{\partial \x_s}\dd{\x_s}$$

가 성립한다. 여기에서 $f$가 유한개의 변수만을 포함하므로 우변은 유한합이다.
:::
::: 증명
[정의 3](#def3)에 의하여 $\Omega_{R/A}$는 원소들 $\dd{f}$로 생성된다. $d$가 $A$-linear이므로 $f$가 monomial인 경우만 보면 충분하고, 이 경우 Leibniz 법칙을 차수에 대한 귀납법으로 적용하면 위의 chain rule을 얻는다. 따라서 $\Omega_{R/A}$는 $\dd{\x_s}$들로 생성된다.

이들이 $R$ 위에서 일차독립임을 보이기 위해, 각각의 $t\in S$에 대하여 편미분 $\partial/\partial \x_t:R \rightarrow R$을 생각하자. 이는 $A$-derivation이므로 [보조정리 2](#lem2)에 의하여 $R$-linear map $\partial_t:\Omega_{R/A} \rightarrow R$을 유도하며, 정의에 의하여 $\partial_t(\dd{\x_s})=\delta_{st}$이다. 그럼 유한합 $\sum_sf_s\dd{\x_s}=0$에 $\partial_t$를 적용하여 $f_t=0$을 얻는다.
:::

이는 $M$이 free $A$-module인 경우의 symmetric algebra $\S(M)$에 대한 계산과 같은 것이다. ([\[다중선형대수학\] §미분가군, ⁋예시 10](/ko/math/multilinear_algebra/differential_modules#ex10)) 뿐만 아니라, $\Omega$를 $A$-algebra $A \rightarrow E$를 받아 $\Omega_{E/A}$를 내놓는 functor처럼 생각하면, 다음과 같은 종류의 functoriality 또한 성립한다.

::: 명제 6
다음의 ring homomorphism들의 commutative diagram

{% diagram Math/Commutative_Algebra/Differentials-1.svg width="6.30em" alt="setup" %}

이 주어졌다 하고, $\rho$와 $\rho'$를 통해 $E, E'$를 각각 $A$-algebra와 $A'$-algebra로 보자. 그럼 다음의 diagram

{% diagram Math/Commutative_Algebra/Differentials-2.svg width="11.54em" alt="functoriality" %}

을 commute하게 하는 유일한 $E$-linear map $\Omega_{\varphi/\phi}:\Omega_{E/A} \rightarrow \Omega_{E'/A'}$이 존재한다.
:::
::: 증명
$d_{E'/A'}\circ \varphi: E \rightarrow \Omega_{E'/A'}$가 $A$-derivation이므로 [보조정리 2](#lem2)에 의하여 유일한 $E$-linear map이 존재한다. 
:::

한편 $\Omega_{E'/A'}$는 $E'$-module이므로, [\[대수적 구조\] §스칼라의 변환, ⁋명제 6](/ko/math/algebraic_structures/change_of_base_ring#prop6)에 의하여 

$$\Hom_{E'}(\varphi_! \Omega_{E/A},\Omega_{E'/A'})\cong\Hom_E(\Omega_{E/A}, \varphi^\ast\Omega_{E'/A'})$$

이 성립한다. 그럼 위의 [명제 6](#prop6)에서 얻어지는 $\Omega_{E/A} \rightarrow \Omega_{E'/A'}$는 엄밀히 이야기하자면 $\Omega_{E/A} \rightarrow \varphi^\ast\Omega_{E'/A'}$이므로, 이에 해당하는 유일한 $E'$-linear homomorphism

$$\Omega_{\varphi/\phi}': \varphi_!\Omega_{E/A}=\Omega_{E/A}\otimes_EE' \rightarrow \Omega_{E'/A'}$$

이 존재한다.  

이 functoriality가 주는 가장 기본적인 결과는 Kähler differential module이 localization과 맞아떨어진다는 것이다.

::: 명제 7
$A$-algebra $E$와 $E$의 multiplicative subset $S$가 주어졌다 하고 ([§국소화, ⁋정의 3](/ko/math/commutative_algebra/localization#def3)), canonical homomorphism $\varphi:E \rightarrow S^{-1}E$를 통해 $S^{-1}E$를 $A$-algebra로 보자. 그럼 [명제 6](#prop6)가 주는 $S^{-1}E$-linear homomorphism

$$\Omega_{\varphi/\id_A}':\Omega_{E/A}\otimes_ES^{-1}E \longrightarrow \Omega_{S^{-1}E/A}$$

은 isomorphism이다.
:::
::: 증명
임의의 $S^{-1}E$-module $M$에 대하여 $\varphi$를 따라 restrict하는 map

$$\varphi^\ast:\Der_A(S^{-1}E, M) \longrightarrow \Der_A(E, M)$$

이 bijection임을 보인다. $M$이 $S^{-1}E$-module이므로 $S$의 원소들은 $M$ 위에서 invertible action을 주며, 아래에서 $M$의 원소를 $S$의 원소로 나누는 것은 이 action의 역을 뜻한다.

$D\in\Der_A(S^{-1}E, M)$와 $x\in E$, $s\in S$에 대하여 $x=s(x/s)$에 Leibniz 법칙을 적용하면 $D(x)=sD(x/s)+(x/s)D(s)$이므로

$$D(x/s)=\bigl(D(x)-(x/s)D(s)\bigr)/s$$

이고, 곧 $D$는 $E$ 위에서의 값으로 결정되어 $\varphi^\ast$는 단사이다. 전사성을 위해서는 $D\in\Der_A(E, M)$가 주어졌을 때 위의 식을 정의로 삼아 $\widetilde D(x/s)=\bigl(D(x)-(x/s)D(s)\bigr)/s$로 두면 된다. 이것이 well-defined임을 보이기 위해 $x/s=y/t$라 하면 적당한 $u\in S$가 $u(tx-sy)=0$을 만족하므로 ([§국소화, ⁋정의 4](/ko/math/commutative_algebra/localization#def4)), 여기에 $D$를 적용하여

$$utD(x)+uxD(t)+txD(u)=usD(y)+uyD(s)+syD(u)$$

를 얻는다. $S^{-1}E$ 안에서는 $tx=sy$이므로 양변의 마지막 항이 서로 같고, 남은 것을 $u$로 나누면

$$tD(x)+xD(t)=sD(y)+yD(s)$$

가 된다. 한편 $tx=sy$로부터 $tx/s=y$와 $sy/t=x$이므로, 이 등식은 양변을 $st$로 나눈

$$\bigl(D(x)-(x/s)D(s)\bigr)/s=\bigl(D(y)-(y/t)D(t)\bigr)/t$$

와 같은 것이며, 따라서 $\widetilde D$는 well-defined이다. 이것이 $A$의 원소에 대한 스칼라곱을 보존하는 것은 $D$가 $A$-linear라는 것과 정의식에서 바로 따라나오고, 덧셈의 보존은 $x/s+y/t=(tx+sy)/(st)$에 정의식을 적용한

$$\widetilde D\Bigl(\frac{tx+sy}{st}\Bigr)=\frac{tD(x)+xD(t)+sD(y)+yD(s)}{st}-\Bigl(\frac{x}{s}+\frac{y}{t}\Bigr)\Bigl(\frac{D(s)}{s}+\frac{D(t)}{t}\Bigr)$$

에서 $xD(t)/(st)$와 $yD(s)/(st)$가 상쇄되어 $\widetilde D(x/s)+\widetilde D(y/t)$만 남는 것으로 확인된다. 남은 Leibniz 법칙은

$$\begin{aligned}
\widetilde D\Bigl(\frac{xy}{st}\Bigr)&=\frac{D(xy)}{st}-\frac{xy}{(st)^2}D(st)\\
&=\frac{xD(y)+yD(x)}{st}-\frac{xy}{(st)^2}\bigl(sD(t)+tD(s)\bigr)\\
&=\frac{x}{s}\Bigl(\frac{D(y)}{t}-\frac{y}{t^2}D(t)\Bigr)+\frac{y}{t}\Bigl(\frac{D(x)}{s}-\frac{x}{s^2}D(s)\Bigr)\\
&=\frac{x}{s}\widetilde D\Bigl(\frac{y}{t}\Bigr)+\frac{y}{t}\widetilde D\Bigl(\frac{x}{s}\Bigr)
\end{aligned}$$

로 확인된다. 또 $D(1)=D(1\cdot 1)=2D(1)$에서 $D(1)=0$이므로 $\widetilde D(x/1)=D(x)$이고, 곧 $\varphi^\ast\widetilde D=D$이다.

이제 $\varphi^\ast$가 $M$에 대하여 natural한 bijection이므로, 여기에 [보조정리 2](#lem2)와 [\[대수적 구조\] §스칼라의 변환, ⁋명제 6](/ko/math/algebraic_structures/change_of_base_ring#prop6)의 adjunction을 결합하면 임의의 $S^{-1}E$-module $M$에 대하여

$$\Hom_{S^{-1}E}\bigl(\Omega_{E/A}\otimes_ES^{-1}E, M\bigr)\cong\Hom_E(\Omega_{E/A}, M)\cong\Der_A(E, M)\cong\Der_A(S^{-1}E, M)\cong\Hom_{S^{-1}E}\bigl(\Omega_{S^{-1}E/A}, M\bigr)$$

이 성립하고 이 대응들은 모두 $M$에 대하여 natural하다. 즉 두 $S^{-1}E$-module이 같은 functor를 표현하므로 이들은 canonical하게 isomorphic하며, 이 isomorphism을 generator $\dd{x}\otimes 1$ 위에서 따라가면 $\dd{x}\otimes 1\mapsto \dd{\varphi}(x)$이 되어 이것이 [명제 6](#prop6)가 준 $\Omega_{\varphi/\id_A}'$임을 안다.
:::

특히 $S^{-1}E$의 universal derivation은 $E$의 것으로부터 $\dd{(x/s)}=(s\dd{x}-x\dd{s})/s^2$으로 얻어진다.

## Fundamental sequences

특별히 $\phi:A \rightarrow A'$를 $\id_A:A \rightarrow A$로 두자. 그럼 위에서 만든 $E'$-linear homomorphism은 오직 $A$-linear map $\varphi:E \rightarrow E'$에만 의존하며, 다음의 꼴

$$\Omega_{\varphi/A}':\Omega_{E/A}\otimes_EE' \rightarrow \Omega_{E'/A}$$

이 된다. 한편, $\varphi:E \rightarrow E'$를 통해 $E'$를 $E$-algebra로 보면 $E'$의 $E$에 대한 Kähler differential module $\Omega_{E'/E}$가 정의되며, 이 때 universal $E$-derivation $d_{E'/E}: E' \rightarrow \Omega_{E'/E}$는 $A$-derivation이기도 하므로 다시 [보조정리 2](#lem2)에 의하여 $d_{E'/E}=\Omega_\varphi\circ d_{E'/A}$를 만족하는 유일한 $E'$-linear map

$$\Omega_\varphi:\Omega_{E'/A} \rightarrow \Omega_{E'/E}$$

가 존재한다. 즉 $d_{E'/E}$는 다음의 합성

$$E' \overset{d_{E'/A}}{\longrightarrow}\Omega_{E'/A}\overset{\Omega_\varphi}{\longrightarrow}\Omega_{E'/E}$$

과 동일하다. 

::: 명제 8 (Cotangent sequence)
$E'$-linear map들의 sequence

$$\Omega_{E/A}\otimes_EE'\overset{\Omega_{\varphi/A}'}{\longrightarrow}\Omega_{E'/A}\overset{\Omega_\varphi}{\longrightarrow}\Omega_{E'/E} \longrightarrow 0$$

는 exact이다.
:::
::: 증명
$N$을 $\Omega_{\varphi/A}'$의 image, 즉 원소들 $d_{E'/A}\varphi(x)$ ($x\in E$)로 생성되는 $\Omega_{E'/A}$의 $E'$-submodule이라 하고, $C=\Omega_{E'/A}/N$과 quotient map $\pi:\Omega_{E'/A} \rightarrow C$를 생각하자.

우선 $\Omega_\varphi$가 surjective인 것을 보이자. $\Omega_{E'/E}$는 $E'$-module로서 원소들 $d_{E'/E}y'$ ($y'\in E'$)으로 생성되는데, 위에서 살펴본 식 $d_{E'/E}=\Omega_\varphi\circ d_{E'/A}$에 의하여 이들은 모두 $\Omega_\varphi$의 image에 속하기 때문이다.

다음으로 두 map의 합성이 $0$임을 보이자. $\Omega_{E/A}\otimes_EE'$의 generator $d_{E/A}x\otimes 1$은 $\Omega_{\varphi/A}'$에 의해 $d_{E'/A}\varphi(x)$로 옮겨지고, 다시 $\Omega_\varphi$에 의해 $d_{E'/E}\varphi(x)$로 옮겨진다. 그런데 $d_{E'/E}$는 $E$-derivation이므로 $\varphi(x)$ 꼴의 원소들, 즉 $E$에서 온 원소들을 모두 $0$으로 보낸다. 따라서 $\Omega_\varphi\circ\Omega_{\varphi/A}'=0$이고, 특히 $N\subseteq \ker\Omega_\varphi$이므로 $\Omega_\varphi$는 $E'$-linear map $\psi':C \rightarrow \Omega_{E'/E}$를 유도한다.

이제 $\ker\Omega_\varphi\subseteq N$임을 보이면 증명이 끝난다. 이를 위해 합성 $\delta=\pi\circ d_{E'/A}:E' \rightarrow C$를 생각하자. 그럼 $\delta$는 $A$-derivation이며, $N$의 정의에 의하여 $\varphi(E)$의 원소들을 모두 $0$으로 보낸다. 그런데 임의의 $e\in E$와 $y'\in E'$에 대하여

$$\delta(\varphi(e)y')=\varphi(e)\,\delta(y')+y'\,\delta(\varphi(e))=\varphi(e)\,\delta(y')$$

이므로 $\delta$는 $E$-linear이고, 따라서 $E$-derivation이다. 그럼 [보조정리 2](#lem2)의 universal property에 의하여 $\psi\circ d_{E'/E}=\delta$를 만족하는 유일한 $E'$-linear map $\psi:\Omega_{E'/E} \rightarrow C$가 존재한다. 이제 두 합성 $\psi\circ\psi'$와 $\psi'\circ\psi$를 생각하면, 각각 $C$와 $\Omega_{E'/E}$의 generator들 위에서

$$\pi(d_{E'/A}y')\overset{\psi'}{\longmapsto} d_{E'/E}y'\overset{\psi}{\longmapsto}\pi(d_{E'/A}y'),\qquad d_{E'/E}y'\overset{\psi}{\longmapsto}\pi(d_{E'/A}y')\overset{\psi'}{\longmapsto}d_{E'/E}y'$$

이므로 이들은 모두 identity이다. 즉 $\psi'$는 isomorphism이고, 따라서 $\ker \Omega_\varphi=N=\im \Omega_{\varphi/A}'$이다.
:::

또 다른 중요한 exact sequence는 특별히 $\varphi:E \rightarrow E'$가 surjective인 경우에 얻어진다. 이 경우, first isomorphism theorem에 의하여

$$E/\ker \varphi\cong E'$$

가 성립한다. 편의상 $K=\ker\varphi$라 적자. 그럼 $d_{E/A}:E \rightarrow \Omega_{E/A}$를 $K$로 제한한

$$d_{E/A}\vert_K: K \rightarrow \Omega_{E/A}$$

를 생각하고, 다음의 $E$-linear map

$$K\overset{d\vert_K}{\longrightarrow}\Omega_{E/A}\overset{}{\longrightarrow}\Omega_{E/A}\otimes_EE'$$

을 생각할 수 있다. 그럼 위의 합성의 kernel이 $K^2$를 포함한다는 것을 확인할 수 있고, 따라서 이로부터 $E$-linear map

$$\bar{d}:K/K^2 \rightarrow \Omega_{E/A}\otimes_EE'$$

을 얻는다.

::: 명제 9
위와 같은 상황에서, 다음의 sequence

$$K/K^2 \overset{\bar{d}}{\longrightarrow}\Omega_{E/A}\otimes_EE' \rightarrow\Omega_{E'/A} \longrightarrow 0$$

는 exact이다. 
:::
::: 증명
가운데 map은 [명제 8](#prop8)에서의 $\Omega_{\varphi/A}'$이다. $N'$을 $\bar{d}$의 image로 생성되는 $\Omega_{E/A}\otimes_EE'$의 $E'$-submodule이라 하고, $C'=(\Omega_{E/A}\otimes_EE')/N'$과 quotient map $\pi:\Omega_{E/A}\otimes_EE' \rightarrow C'$를 생각하자.

우선 $\Omega_{\varphi/A}'$가 surjective인 것을 보이자. $\varphi$가 surjective이므로 $\Omega_{E'/A}$의 임의의 generator는 $x\in E$에 대하여 $d_{E'/A}\varphi(x)$의 꼴로 쓸 수 있고, 이는 $\Omega_{\varphi/A}'(d_{E/A}x\otimes 1)$과 같기 때문이다.

다음으로 두 map의 합성이 $0$임을 보이자. 임의의 $k\in K$에 대하여 $\bar{d}(k+K^2)=d_{E/A}k\otimes 1$이고, 이는 $\Omega_{\varphi/A}'$에 의해 $d_{E'/A}\varphi(k)=d_{E'/A}(0)=0$으로 옮겨진다. 특히 $N'\subseteq\ker\Omega_{\varphi/A}'$이므로 $\Omega_{\varphi/A}'$는 $E'$-linear map $\psi':C' \rightarrow \Omega_{E'/A}$를 유도한다.

이제 $\ker\Omega_{\varphi/A}'\subseteq N'$임을 보이면 증명이 끝난다. 함수 $\delta: E' \rightarrow C'$를, $x'\in E'$의 임의의 preimage $x\in E$에 대하여 $\delta(x')=\pi(d_{E/A}x\otimes 1)$으로 정의하자. 이 정의는 preimage의 선택에 의존하지 않는데, 두 preimage의 차는 $K$의 원소 $k$이고 $d_{E/A}k\otimes 1\in N'$이기 때문이다. 그럼 $\delta$는 $A$-linear이고, 임의의 $x',y'\in E'$과 그 preimage들 $x,y$에 대하여

$$\delta(x'y')=\pi(d_{E/A}(xy)\otimes 1)=\pi((x\,d_{E/A}y+y\,d_{E/A}x)\otimes 1)=x'\,\delta(y')+y'\,\delta(x')$$

이므로 $A$-derivation이다. 여기서 마지막 등식은 $\Omega_{E/A}\otimes_EE'$ 위에서 $E$의 action이 $\varphi$를 통한 $E'$의 action과 일치한다는 것에 따른 것이다. 그럼 [보조정리 2](#lem2)의 universal property에 의하여 $\psi\circ d_{E'/A}=\delta$를 만족하는 유일한 $E'$-linear map $\psi:\Omega_{E'/A} \rightarrow C'$가 존재한다. 두 합성 $\psi\circ\psi'$와 $\psi'\circ\psi$는 각각 generator들 위에서

$$\pi(d_{E/A}x\otimes 1)\overset{\psi'}{\longmapsto}d_{E'/A}\varphi(x)\overset{\psi}{\longmapsto}\pi(d_{E/A}x\otimes 1),\qquad d_{E'/A}x'\overset{\psi}{\longmapsto}\pi(d_{E/A}x\otimes 1)\overset{\psi'}{\longmapsto}d_{E'/A}x'$$

이 되어 모두 identity이다. 즉 $\psi'$는 isomorphism이고, 따라서 $\ker\Omega_{\varphi/A}'=N'=\im\bar{d}$이다.
:::

이 exact sequence를 *conormal sequence*라 부르기도 한다.

## Naive cotangent complex

[명제 9](#prop9)의 conormal sequence는 오른쪽 끝에서만 exact이며, 일반적으로 $\bar{d}$는 injective가 아니다. 자연스러운 질문은 $\bar{d}$의 kernel이 어떤 의미를 갖는지, 그리고 이 sequence를 왼쪽으로 연장할 수 있는지이다. 이 절에서는 이 질문에 대한 첫 번째 답인 *naive cotangent complex*를 살펴본다.

핵심 아이디어는 $E$를 가장 다루기 쉬운 algebra, 즉 polynomial algebra의 quotient로 표현하는 것이다. $E$의 spanning set $(t_s)_{s\in S}$를 아무거나 택하면 (가령 $E$ 전체), [\[대수적 구조\] §대수, ⁋명제 8](/ko/math/algebraic_structures/algebras#prop8)의 adjunction에 의하여 $\x_s\mapsto t_s$로 정의되는 surjective $A$-algebra homomorphism

$$p: R=A[\x_s]_{s\in S}\longrightarrow E$$

가 존재한다. 이러한 $p$를 $E$의 *presentation<sub>표현</sub>*이라 부르고, $\mathfrak{I}=\ker p$라 적자. 그럼 [명제 9](#prop9)을 $\varphi=p$, 곧 $E$를 $R$로 $E'$을 $E$로 두어 적용할 수 있으며, 그 conormal sequence의 왼쪽 두 항이 다음의 complex를 이룬다.

::: 정의 10
Presentation $p:R \rightarrow E$에 대하여, $p$의 *naive cotangent complex* $\operatorname{NL}(p)$는 conormal sequence의 왼쪽 두 항으로 이루어진 $E$-module들의 two-term complex

$$\operatorname{NL}(p)=\Bigl[\mathfrak{I}/\mathfrak{I}^2\overset{\bar{d}}{\longrightarrow}\Omega_{R/A}\otimes_RE\Bigr]$$

를 뜻한다. 여기서 $\mathfrak{I}/\mathfrak{I}^2$는 degree $1$, $\Omega_{R/A}\otimes_RE$는 degree $0$에 둔다.
:::

즉 $\operatorname{NL}(p)$는 두 개의 항만 $0$이 아닌 chain complex이고 ([\[호몰로지 대수학\] §호몰로지](/ko/math/homological_algebra/homology)), 그 homology는

$$H_0\bigl(\operatorname{NL}(p)\bigr)=\coker\bar{d},\qquad H_1\bigl(\operatorname{NL}(p)\bigr)=\ker\bar{d}$$

뿐이다. [명제 5](#prop5)에 의하여 $\Omega_{R/A}$는 $\dd{\x_s}$들을 기저로 갖는 free $R$-module이므로, $\operatorname{NL}(p)$의 degree $0$ 항은 free $E$-module이다.

::: 명제 11
임의의 presentation $p:R \rightarrow E$에 대하여, canonical isomorphism

$$H_0\bigl(\operatorname{NL}(p)\bigr)\cong\Omega_{E/A}$$

이 존재한다.
:::
::: 증명
[명제 9](#prop9)의 conormal sequence

$$\mathfrak{I}/\mathfrak{I}^2\overset{\bar{d}}{\longrightarrow}\Omega_{R/A}\otimes_RE\overset{\Omega_{p/A}'}{\longrightarrow}\Omega_{E/A}\longrightarrow0$$

에서 $\Omega_{p/A}'$가 surjective이고 그 kernel이 $\im\bar{d}$이므로, first isomorphism theorem에 의하여 $\coker\bar{d}\cong\Omega_{E/A}$이다.
:::

즉 $H_0$는 presentation에 의존하지 않고 항상 Kähler differential module을 복원한다. 따라서 새로운 정보는 $H_1(\operatorname{NL}(p))$에 들어있으며, 이것이 conormal sequence의 왼쪽 끝에서의 exactness의 실패를 측정한다. 물론 이 이야기가 의미를 가지려면 $H_1$ 또한 presentation의 선택에 의존하지 않아야 한다.

## 표현의 선택과 무관성

두 presentation을 비교하기 위해 우선 다음을 관찰하자. 두 presentation $p:R=A[\x_s]_{s\in S} \rightarrow E$, $p':R'=A[\y_t]_{t\in T} \rightarrow E$가 주어졌다 하면, 각각의 $s\in S$마다 $p'$가 surjective이므로 $p'(g_s)=p(\x_s)$이도록 하는 $g_s\in R'$을 택할 수 있고, $\x_s\mapsto g_s$는 $p'\circ\varphi=p$를 만족하는 $A$-algebra homomorphism $\varphi:R \rightarrow R'$을 유도한다. 그럼 $\varphi(\mathfrak{I})\subseteq\mathfrak{I}'$이므로 $\varphi$는 두 complex 사이의 morphism

$$\operatorname{NL}(\varphi):\operatorname{NL}(p) \rightarrow \operatorname{NL}(p');\qquad \overline{f}\mapsto\overline{\varphi(f)},\quad \dd{\x_s}\otimes1\mapsto \dd{\varphi}(\x_s)\otimes1$$

을 유도한다. 사각형이 commute하는 것은 [명제 5](#prop5)가 주는 식 $\dd{\varphi}(f)=\sum_s\varphi(\partial f/\partial\x_s)\dd{\varphi}(\x_s)$로부터 확인된다.

::: 보조정리 12
위의 상황에서, $p'\circ\varphi=p=p'\circ\psi$를 만족하는 두 $A$-algebra homomorphism $\varphi,\psi:R \rightarrow R'$이 주어졌다 하자. 그럼 임의의 $f\in R$에 대하여 다음의 식

$$\varphi(f)-\psi(f)\equiv\sum_{s\in S}\varphi\left(\frac{\partial f}{\partial \x_s}\right)\bigl(\varphi(\x_s)-\psi(\x_s)\bigr)\pmod{\mathfrak{I}'^2}$$

이 성립한다.
:::
::: 증명
우선 $p'(\varphi(f)-\psi(f))=p(f)-p(f)=0$이므로 $\varphi(f)-\psi(f)\in\mathfrak{I}'$이고, 마찬가지 이유로 위의 합동식의 양변이 모두 $\mathfrak{I}'$의 원소이므로 식이 말이 된다. 주어진 식을 만족하는 $f$들의 모임을 $P$라 하자. $P$가 $A$의 원소들을 포함하고 (양변이 모두 $0$이다), 각각의 변수 $\x_s$를 포함하며 ($\partial\x_s/\partial\x_{s'}$는 $s=s'$일 때 $1$, 아닐 때 $0$이다), $A$-linear combination에 대해 닫혀있는 것은 자명하다. 따라서 $P$가 곱셈에 대해 닫혀있는 것만 보이면 $P=R$이다.

$f,g\in P$라 하고, 편의상 $\alpha=\varphi(f)-\psi(f)$, $\beta=\varphi(g)-\psi(g)\in\mathfrak{I}'$라 적자. 그럼

$$\varphi(fg)-\psi(fg)=\varphi(f)\varphi(g)-\psi(f)\psi(g)=\psi(f)\beta+\varphi(g)\alpha=\varphi(f)\beta+\varphi(g)\alpha-\alpha\beta$$

인데, 마지막 등식은 $\psi(f)\beta=\varphi(f)\beta-\alpha\beta$와 같은 식으로 정리한 것이며 $\alpha\beta\in\mathfrak{I}'^2$이므로

$$\varphi(fg)-\psi(fg)\equiv\varphi(f)\beta+\varphi(g)\alpha\pmod{\mathfrak{I}'^2}$$

이다. 이제 $f,g\in P$라는 가정을 $\alpha,\beta$에 대입하고 Leibniz rule $\partial(fg)/\partial\x_s=f(\partial g/\partial\x_s)+g(\partial f/\partial\x_s)$를 사용하면, $\mathfrak{I}'$의 원소들끼리의 곱이 $\mathfrak{I}'^2$에서 사라진다는 것으로부터 $fg\in P$를 얻는다.
:::

::: 명제 13
[보조정리 12](#lem12)의 상황에서, 두 morphism $\operatorname{NL}(\varphi),\operatorname{NL}(\psi):\operatorname{NL}(p) \rightarrow \operatorname{NL}(p')$은 chain homotopic이다. 특히 이들이 유도하는 homology의 morphism들은 일치한다.
:::
::: 증명
$\Omega_{R/A}\otimes_RE$가 $\dd{\x_s}\otimes1$들을 기저로 갖는 free $E$-module이므로, $E$-linear map

$$h:\Omega_{R/A}\otimes_RE \rightarrow \mathfrak{I}'/\mathfrak{I}'^2;\qquad \dd{\x_s}\otimes1\mapsto\overline{\varphi(\x_s)-\psi(\x_s)}$$

이 잘 정의된다. 여기서 $\varphi(\x_s)-\psi(\x_s)\in\mathfrak{I}'$인 것은 [보조정리 12](#lem12)의 증명에서 보았고, $\mathfrak{I}'$가 $\mathfrak{I}'/\mathfrak{I}'^2$을 annihilate하므로 $\mathfrak{I}'/\mathfrak{I}'^2$은 $E=R'/\mathfrak{I}'$-module이다. 이제 $h$가 $\operatorname{NL}(\varphi)-\operatorname{NL}(\psi)$의 chain homotopy임을 보인다.

우선 degree $0$에서, generator $\dd{\x_s}\otimes 1$에 대하여

$$\bar{d}'\bigl(h(\dd{\x_s}\otimes1)\bigr)=d\bigl(\varphi(\x_s)-\psi(\x_s)\bigr)\otimes1=\bigl(\operatorname{NL}(\varphi)-\operatorname{NL}(\psi)\bigr)(\dd{\x_s}\otimes1)$$

이다. 다음으로 degree $1$에서, 임의의 $f\in\mathfrak{I}$에 대하여 $\dd{f}=\sum_s(\partial f/\partial\x_s)\dd{\x_s}$이므로

$$h\bigl(\bar{d}(\overline{f})\bigr)=\sum_sp\left(\frac{\partial f}{\partial\x_s}\right)\cdot\overline{\varphi(\x_s)-\psi(\x_s)}=\overline{\sum_s\varphi\left(\frac{\partial f}{\partial\x_s}\right)\bigl(\varphi(\x_s)-\psi(\x_s)\bigr)}$$

이다. 마지막 등식은 $\mathfrak{I}'/\mathfrak{I}'^2$ 위에서 $E=R'/\mathfrak{I}'$의 action이 $p'$를 통해 주어지고 $p'\circ\varphi=p$이기 때문이다. 그럼 [보조정리 12](#lem12)에 의하여 이는 $\overline{\varphi(f)-\psi(f)}=\bigl(\operatorname{NL}(\varphi)-\operatorname{NL}(\psi)\bigr)(\overline{f})$와 같다. 따라서 $h$는 chain homotopy이고, chain homotopic한 morphism들이 같은 homology morphism을 유도하는 것은 [\[호몰로지 대수학\] §호몰로지](/ko/math/homological_algebra/homology)에서 살펴보았다.
:::

::: 정리 14
두 presentation $p:R \rightarrow E$, $p':R' \rightarrow E$에 대하여, complex들 $\operatorname{NL}(p)$와 $\operatorname{NL}(p')$은 homotopy equivalent이다. 특히 canonical isomorphism

$$H_i\bigl(\operatorname{NL}(p)\bigr)\cong H_i\bigl(\operatorname{NL}(p')\bigr),\qquad i=0,1$$

이 존재한다.
:::
::: 증명
위에서 살펴본 것과 같이 $p'\circ\varphi=p$이도록 하는 $\varphi:R \rightarrow R'$과 $p\circ\varphi'=p'$이도록 하는 $\varphi':R' \rightarrow R$을 택하자. 그럼 $\varphi'\circ\varphi$와 $\id_R$은 모두 $p\circ(\varphi'\circ\varphi)=p=p\circ\id_R$을 만족하므로 [명제 13](#prop13)에 의하여

$$\operatorname{NL}(\varphi')\circ\operatorname{NL}(\varphi)=\operatorname{NL}(\varphi'\circ\varphi)\simeq\operatorname{NL}(\id_R)=\id_{\operatorname{NL}(p)}$$

이고, symmetrically $\operatorname{NL}(\varphi)\circ\operatorname{NL}(\varphi')\simeq\id_{\operatorname{NL}(p')}$이다. 즉 $\operatorname{NL}(\varphi)$는 homotopy equivalence이고, homology에 isomorphism을 유도한다. 이 isomorphism이 canonical한 것은, $\varphi$의 다른 선택이 [명제 13](#prop13)에 의해 같은 homology morphism을 유도하기 때문이다.
:::

따라서 우리는 presentation의 선택을 잊고, homotopy equivalence를 무시한다는 단서 하에 $\operatorname{NL}_{E/A}$라 적을 수 있다. 그 homology

$$H_0(\operatorname{NL}_{E/A})\cong\Omega_{E/A},\qquad H_1(\operatorname{NL}_{E/A})$$

는 $A$-algebra $E$의 invariant가 된다. $H_1$이 측정하는 것이 무엇인지 다음 예시에서 살펴보자.

::: 예시 15
하나의 다항식으로 표현되는 algebra $E=A[\x]/(f)$를 생각하자. 여기서 $f$는 $A[\x]$의 nonzerodivisor라 가정한다. Presentation $p:R=A[\x] \rightarrow E$에 대하여 $\mathfrak{I}=(f)$이고, $f$가 nonzerodivisor이므로 $\mathfrak{I}/\mathfrak{I}^2$는 $\overline{f}$를 기저로 갖는 free $E$-module이다. 실제로 $af\in(f^2)$라면 $af=bf^2$로부터 $a=bf\in(f)$이다. 따라서

$$\operatorname{NL}_{E/A}=\Bigl[E\overline{f}\overset{\bar{d}}{\longrightarrow}E\dd{\x}\Bigr],\qquad \bar{d}(\overline{f})=\overline{Df}\dd{\x}$$

이다. 여기서 $Df$는 $f$의 derivative이다. 그럼

$$H_0(\operatorname{NL}_{E/A})=\Omega_{E/A}\cong E/(\overline{Df}),\qquad H_1(\operatorname{NL}_{E/A})\cong\ann_E(\overline{Df})$$

이다. 가령 $A=\mathbb{K}$가 characteristic이 $2$가 아닌 field이고 $f=\x^2$이라면 $\overline{Df}=2\overline{\x}$이므로 $H_1\cong\ann_E(2\overline{\x})=(\overline{\x})\neq0$이다. 반면 $f$와 $Df$가 생성하는 ideal이 $A[\x]$ 전체인 경우, 곧 $uf+vDf=1$인 $u,v\in A[\x]$가 존재하는 경우에는 $\overline{Df}$가 $E$의 unit이 되어 $H_0=H_1=0$이다. $A=\mathbb{K}$가 field라면 $A[\x]$가 PID이므로 이 조건은 $f$가 separable polynomial이라는 것과 같다. 즉 $H_1$은 $\Omega_{E/A}$만으로는 보이지 않는, presentation의 relation들이 갖는 중복도에 대한 정보를 담고 있다.
:::

::: 참고 16
Naive cotangent complex는 이름 그대로 더 정교한 대상의 그림자이다. Quillen과 André는 polynomial algebra에 의한 한 번의 presentation 대신 simplicial resolution을 사용하여, 모든 degree에서 homology를 갖는 *cotangent complex* $L_{E/A}$를 정의하였다. 이 complex의 degree $0,1$ 부분이 정확히 위에서 정의한 $\operatorname{NL}_{E/A}$이다. 이러한 homotopy 이론적인 구성은 이 category의 범위를 벗어나므로, 여기서는 두 항짜리 절단인 $\operatorname{NL}_{E/A}$로 만족하기로 한다.
:::

---

**참고문헌**

**[Eis]** David Eisenbud. *Commutative Algebra: with a view toward algebraic geometry*. Springer, 1995.

---