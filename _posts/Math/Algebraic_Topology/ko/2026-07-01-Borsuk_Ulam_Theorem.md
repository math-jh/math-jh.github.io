---
title: "Borsuk–Ulam 정리"
description: "antipode를 보존하는 사상의 차수가 홀수임을 이용해 Borsuk–Ulam 정리의 여러 동치형을 증명하고, 그로부터 ham sandwich 정리와 Lusternik–Schnirelmann 덮개 정리 등의 귀결을 얻는다."
excerpt: "The Borsuk–Ulam theorem, odd maps, and the ham sandwich theorem"

categories: [Math / Algebraic Topology]
permalink: /ko/math/algebraic_topology/borsuk_ulam_theorem
sidebar: 
    nav: "algebraic_topology-ko"

date: 2026-07-01
last_modified_at: 2026-07-01
weight: 5.7

published: false

---

## Antipode를 보존하는 사상

구 $$S^n\subseteq\mathbb{R}^{n+1}$$ 위에는 각 점 $$x$$를 그 대척점 $$-x$$로 보내는 대합 $$x\mapsto-x$$이 놓여 있다. 이 대합과 잘 맞물리는 연속함수, 곧 $$-x$$를 언제나 상의 대척점으로 보내는 함수는 대합의 대칭성을 그대로 물려받아 대단히 강하게 제약된다. Borsuk–Ulam 정리는 이러한 제약의 원형으로서, 겉보기에 순전히 위상적인 진술이면서도 측도를 동시에 이등분하는 초평면의 존재나 구의 덮개 구조와 같은 구체적인 귀결을 낳는다. 앞선 글에서 우리는 구면 자기사상에 정수 하나를 붙이는 차수 이론을 마련하였으므로 ([§사상의 차수와 Brouwer·Lefschetz 고정점 정리, ⁋정의 2](/ko/math/algebraic_topology/degree_and_fixed_point_theorems#def2)), 이제 antipode를 보존하는 사상의 차수가 강한 산술적 제약을 받는다는 사실을 지렛대로 삼아 이 정리와 그 여러 동치형을 증명한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 연속함수 $$f:S^n\rightarrow\mathbb{R}^m$$ 또는 $$f:S^n\rightarrow S^m$$이 모든 $$x\in S^n$$에 대하여

$$f(-x)=-f(x)$$

를 만족할 때, $$f$$를 *antipodal map<sub>대척사상</sub>* 또는 *odd map<sub>기함수형 사상</sub>*이라 부른다.

</div>

정의의 조건은 실함수의 경우 기함수 조건 $$f(-x)=-f(x)$$과 형태가 같으므로 odd map이라는 이름이 붙었다. 대표적인 antipodal map은 antipodal 사상 $$a(x)=-x$$ 자신이며, 좌표를 뒤집는 어떤 선형사상의 제한도 antipodal map이다. 반대로 상수함수는 $$0$$이 아닌 값을 가지는 한 antipodal map이 될 수 없는데, $$f(x)=f(-x)=-f(x)$$가 강제되어 $$f(x)=0$$이어야 하기 때문이다. 이처럼 antipodal 조건은 상수사상을 곧바로 배제하며, 우리는 이 조건이 훨씬 더 강한 제약을 낳음을 보게 된다.

## 정리와 그 동치형

Borsuk–Ulam 정리는 여러 모습으로 나타난다. 가장 널리 인용되는 것은 구면에서 유클리드 공간으로 가는 임의의 연속함수가 어떤 대척쌍을 한 점으로 붙인다는 진술이지만, 이는 antipodal map의 비존재나 antipodal 자기사상의 차수에 대한 진술과 긴밀히 얽혀 있다.

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2 (Borsuk–Ulam)**</ins> $$n\geq 1$$에 대하여 다음 세 명제가 성립하며, 서로 밀접히 관련되어 있다.

1. 임의의 연속함수 $$f:S^n\rightarrow\mathbb{R}^n$$에 대하여 $$f(x)=f(-x)$$인 점 $$x\in S^n$$이 존재한다.
2. Antipodal map $$g:S^n\rightarrow S^{n-1}$$은 존재하지 않는다.
3. 임의의 antipodal 자기사상 $$f:S^n\rightarrow S^n$$의 차수 $$\deg f$$는 홀수이며, 특히 $$0$$이 아니다.

</div>

우리는 이 절의 나머지에서 이 정리를 증명한다. 논증의 뼈대는 다음과 같다. 먼저 [명제 3](#prop3)에서 (1)과 (2)가 서로 동치임을 순수하게 기초적인 방법으로 보인다. 이로써 정리는 antipodal map $$S^n\rightarrow S^{n-1}$$이 없다는 진술 (2)로 환원된다. 이어서 세 진술 가운데 가장 강한 (3), 곧 antipodal 자기사상의 차수가 홀수라는 사실을 확립하고 ([정리 5](#thm5)), 이로부터 (2)가 곧바로 따라 나옴을 [따름정리 6](#cor6)에서 확인한다. 결국 (3)이 (2)를, 따라서 (1)을 함의하며 정리 전체가 성립한다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> $$n\geq 1$$에 대하여, [정리 2](#thm2)의 진술 (1)과 (2)는 서로 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

먼저 (1)이 성립한다고 가정하고 (2)를 보인다. Antipodal map $$g:S^n\rightarrow S^{n-1}$$이 존재한다고 하자. $$S^{n-1}\subseteq\mathbb{R}^n$$이므로 $$g$$를 연속함수 $$g:S^n\rightarrow\mathbb{R}^n$$으로 볼 수 있고, (1)에 의하여 $$g(x)=g(-x)$$인 점 $$x$$가 존재한다. 그런데 $$g$$가 antipodal이므로 $$g(-x)=-g(x)$$이고, 따라서 $$g(x)=-g(x)$$, 곧 $$g(x)=0$$이다. 이는 $$g(x)\in S^{n-1}$$, 곧 $$\lvert g(x)\rvert=1$$이라는 사실에 모순이다. 그러므로 그러한 $$g$$는 존재하지 않으며 (2)가 성립한다.

역으로 (2)가 성립한다고 가정하고 (1)을 보인다. 만일 (1)이 거짓이라면 모든 $$x\in S^n$$에 대하여 $$f(x)\neq f(-x)$$인 연속함수 $$f:S^n\rightarrow\mathbb{R}^n$$이 존재한다. 그러면 $$f(x)-f(-x)$$는 어디서도 $$0$$이 아니므로

$$g(x)=\frac{f(x)-f(-x)}{\lvert f(x)-f(-x)\rvert}$$

가 잘 정의된 연속함수 $$g:S^n\rightarrow S^{n-1}$$을 준다. 나아가

$$g(-x)=\frac{f(-x)-f(x)}{\lvert f(-x)-f(x)\rvert}=-g(x)$$

이므로 $$g$$는 antipodal map이고, 이는 (2)에 모순이다. 따라서 (1)이 성립한다.

</details>

명제 3은 정리의 해석적 형태 (1)과 위상적 형태 (2)를 자유로이 오갈 수 있게 해준다. 특히 (2)의 비존재 진술은 차수라는 정수 불변량으로 공략하기에 알맞다. Antipodal 자기사상의 차수를 통제하는 것이 관건이므로, 우리는 차원 $$1$$에서 시작하여 antipodal 자기사상의 차수가 반드시 홀수임을 확립한다.

## Antipodal 자기사상의 차수

차원 $$1$$의 경우는 원의 피복 $$\mathbb{R}\rightarrow S^1$$과 그 위의 lifting 이론만으로 완결적으로 다룰 수 있다. 이 기초 사례가 이후 일반 차원 귀납의 출발점이 된다.

<div class="proposition" markdown="1">

<ins id="lem4">**보조정리 4**</ins> 임의의 antipodal 연속 자기사상 $$f:S^1\rightarrow S^1$$의 차수 $$\deg f$$는 홀수이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$S^1=\{e^{2\pi i\theta}\mid\theta\in\mathbb{R}\}$$으로 보고, 피복사상 $$p:\mathbb{R}\rightarrow S^1$$, $$p(\theta)=e^{2\pi i\theta}$$을 생각하자. 이때 대척점 $$-e^{2\pi i\theta}=e^{2\pi i(\theta+1/2)}$$은 $$\theta\mapsto\theta+1/2$$에 대응한다.

주어진 연속함수 $$f:S^1\rightarrow S^1$$에 대하여 합성 $$\theta\mapsto f(e^{2\pi i\theta})$$은 $$\mathbb{R}$$에서 $$S^1$$로 가는 연속함수이다. 정의역 $$\mathbb{R}$$의 각 구간 위에서 이 사상을 경로로 보고 [§피복공간, ⁋보조정리 6](/ko/math/algebraic_topology/covering_spaces#lem6)의 유일한 경로 들어올림을 이어붙이면, $$F(0)$$의 값을 한 번 고정할 때

$$p(F(\theta))=f(e^{2\pi i\theta})\qquad(\theta\in\mathbb{R})$$

를 만족하는 연속함수 $$F:\mathbb{R}\rightarrow\mathbb{R}$$이 유일하게 결정된다. $$f(e^{2\pi i(\theta+1)})=f(e^{2\pi i\theta})$$이므로 $$p(F(\theta+1))=p(F(\theta))$$, 곧 $$F(\theta+1)-F(\theta)$$는 정수이고 연속함수이므로 상수이다. 이 정수 $$\deg f=F(1)-F(0)$$은 [§사상의 차수와 Brouwer·Lefschetz 고정점 정리, ⁋정의 2](/ko/math/algebraic_topology/degree_and_fixed_point_theorems#def2)에서 정의한 $$S^1$$ 자기사상의 차수와 일치하는 감음수이다.

이제 $$f$$가 antipodal이라 하자. 그러면 $$f(e^{2\pi i(\theta+1/2)})=-f(e^{2\pi i\theta})=e^{\pi i}f(e^{2\pi i\theta})$$이므로

$$p\bigl(F(\theta+1/2)\bigr)=p\bigl(F(\theta)+\frac12\bigr)$$

를 얻는다. 따라서 $$F(\theta+1/2)-F(\theta)-1/2$$은 정수값 연속함수이므로 상수이며, 그 값을 $$q\in\mathbb{Z}$$라 하면

$$F(\theta+1/2)=F(\theta)+\frac12+q$$

이다. 이 식을 두 번 적용하면

$$\begin{aligned}
F(\theta+1)&=F\bigl((\theta+\frac12)+\frac12\bigr)=F(\theta+\frac12)+\frac12+q\\
&=\Bigl(F(\theta)+\frac12+q\Bigr)+\frac12+q=F(\theta)+1+2q
\end{aligned}$$

가 되어 $$\deg f=F(1)-F(0)=1+2q$$이다. 이는 홀수이다.

</details>

보조정리 4의 증명에서 antipodal 조건은 반주기 $$1/2$$만큼의 이동이 lifting을 정확히 $$1/2+q$$만큼 밀어낸다는 사실로 번역되었고, 한 바퀴는 반주기의 두 배이므로 감음수가 $$1+2q$$라는 홀수 형태로 강제되었다. 같은 현상이 임의의 차원에서 성립하며, 이것이 다음 정리의 내용이다.

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5 (Borsuk)**</ins> $$n\geq 1$$에 대하여, 임의의 antipodal 연속 자기사상 $$f:S^n\rightarrow S^n$$의 차수 $$\deg f$$는 홀수이다.

</div>
<details class="proof" markdown="1">
<summary>증명 (핵심 아이디어)</summary>

$$n$$에 대한 귀납법을 사용한다. 기저 단계 $$n=1$$은 [보조정리 4](#lem4)에서 이미 확립하였다. 이제 $$n\geq 2$$라 하고, 한 차원 낮은 구에서 antipodal 자기사상의 차수가 홀수라는 것을 가정한다. 일반 단계의 증명은 antipode에 의한 몫공간, 곧 실사영공간 $$\RP^n=S^n/(x\sim-x)$$을 매개로 진행되며, 여기에서는 그 골격만 제시하고 세부는 [Hat]의 §2.B와 [Mat]에 넘긴다.

첫째, $$f$$가 antipodal이면 $$f(-x)=-f(x)$$이므로 이중피복 $$p:S^n\rightarrow\RP^n$$의 몫 위에 유도된 연속함수 $$\bar f:\RP^n\rightarrow\RP^n$$이 $$p\circ f=\bar f\circ p$$를 만족하며 잘 정의된다.

둘째, $$n\geq 2$$일 때 $$\pi_1(\RP^n)\cong\mathbb{Z}/2$$이다. 이 fundamental group의 생성원은 $$S^n$$에서 한 점 $$x$$와 그 대척점 $$-x$$를 잇는 경로가 $$p$$ 아래에서 이루는 loop로 실현된다. $$f$$는 antipodal이므로 이 경로를 $$f(x)$$와 $$-f(x)$$를 잇는 경로로 보내고, 그 상은 다시 $$\RP^n$$의 자명하지 않은 loop로 사영된다. 따라서 $$\bar f$$가 유도하는 $$\pi_1(\RP^n)\rightarrow\pi_1(\RP^n)$$은 항등, 곧 $$\mathbb{Z}/2$$ 위의 유일한 자기동형이다. ([§피복공간, ⁋보조정리 6](/ko/math/algebraic_topology/covering_spaces#lem6)의 lifting을 사용한다.)

셋째, 계수를 $$\mathbb{Z}/2$$로 잡은 호몰로지에서 이 정보를 최고차까지 밀어올린다. 여기서 "장거리 완전열"이란 이중피복 $$p:S^n\rightarrow\RP^n$$에 결부된 Gysin(전달) 완전열

$$\cdots\rightarrow H_i(S^n;\mathbb{Z}/2)\xrightarrow{p_\ast}H_i(\RP^n;\mathbb{Z}/2)\xrightarrow{\cap w}H_{i-1}(\RP^n;\mathbb{Z}/2)\rightarrow H_{i-1}(S^n;\mathbb{Z}/2)\rightarrow\cdots$$

을 말하며, $$w\in H^1(\RP^n;\mathbb{Z}/2)$$은 이 이중피복을 분류하는 유일한 비자명 원소이다. $$H_i(S^n;\mathbb{Z}/2)$$은 $$i=0,n$$에서만 $$\mathbb{Z}/2$$이고 그 사이에서는 $$0$$이므로, $$2\leq i\leq n-1$$인 중간 차수에서 완전열은 $$\cap w:H_i(\RP^n;\mathbb{Z}/2)\xrightarrow{\sim}H_{i-1}(\RP^n;\mathbb{Z}/2)$$가 isomorphism임을 준다. $$\bar f$$는 $$p\circ f=\bar f\circ p$$를 만족하므로 이 완전열의 자연스러운 사다리를 유도하고, $$H^1(\RP^n;\mathbb{Z}/2)\cong\mathbb{Z}/2$$이라 $$\bar f^\ast w=w$$이어서 그 사다리는 $$\cap w$$와 가환한다. 둘째 단계에서 $$\bar f_\ast$$가 $$H_1(\RP^n;\mathbb{Z}/2)$$ 위에서 isomorphism임을 이미 알고 있으므로, 이 $$\cap w$$-isomorphism들을 따라 차수를 하나씩 올리면 $$\bar f_\ast$$가 모든 $$0\leq i\leq n$$에서 $$H_i(\RP^n;\mathbb{Z}/2)$$ 위의 isomorphism임이 귀납적으로 따라 나온다. 끝으로 완전열의 전달사상이 주는 자연스러운 isomorphism $$H_n(\RP^n;\mathbb{Z}/2)\cong H_n(S^n;\mathbb{Z}/2)$$과 사다리의 가환성을 결합하면, 최고차에서 $$\bar f_\ast$$가 isomorphism이라는 사실은 $$f$$가 $$H_n(S^n;\mathbb{Z}/2)\cong\mathbb{Z}/2$$ 위에서 항등으로 작용함, 곧 $$\deg f\equiv 1\pmod 2$$임과 동치이다. 그러므로 $$\deg f$$는 홀수이다.

</details>

정리 5는 antipodal 자기사상이 차수 $$0$$을 가질 수 없음을 함축하므로, 그러한 사상은 결코 상수사상과 homotopic하지 않다. 이 결론은 앞선 글에서 얻은 antipodal 사상 $$a(x)=-x$$의 차수 계산과도 정확히 부합한다. [§사상의 차수와 Brouwer·Lefschetz 고정점 정리, ⁋따름정리 5](/ko/math/algebraic_topology/degree_and_fixed_point_theorems#cor5)에 의하여 $$\deg a=(-1)^{n+1}$$이므로 $$n$$의 홀짝과 무관하게 $$\deg a=\pm 1$$은 늘 홀수이며, 이는 antipodal 사상이 antipodal map의 원형이라는 사실과 잘 어울린다. 이제 이 차수의 홀짝성으로부터 antipodal map $$S^n\rightarrow S^{n-1}$$의 비존재를 이끌어낸다.

<div class="proposition" markdown="1">

<ins id="cor6">**따름정리 6**</ins> $$n\geq 1$$에 대하여, antipodal map $$g:S^n\rightarrow S^{n-1}$$은 존재하지 않는다. 따라서 [정리 2](#thm2)의 세 진술이 모두 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Antipodal map $$g:S^n\rightarrow S^{n-1}$$이 존재한다고 가정하자. $$S^{n-1}$$을 $$S^n$$의 적도, 곧 마지막 좌표가 $$0$$인 점들의 집합으로 보는 포함사상 $$\iota:S^{n-1}\hookrightarrow S^n$$을 생각하면, $$\iota(-y)=-\iota(y)$$이므로 합성 $$\iota\circ g:S^n\rightarrow S^n$$은 다시 antipodal 자기사상이다. 그런데 이 합성의 상은 적도에 놓여 있어 북극과 남극을 포함하지 않으므로, $$\iota\circ g$$는 전사가 아니다.

전사가 아닌 자기사상은 어떤 점 $$q$$를 상에서 빠뜨리므로 그 상이 $$S^n\setminus\{q\}$$에 담긴다. $$S^n\setminus\{q\}$$은 stereographic projection에 의해 $$\mathbb{R}^n$$과 homeomorphic한 contractible 공간이므로, $$\iota\circ g$$는 한 점을 거쳐 인수분해되어 상수사상과 homotopic하다. 따라서 그 차수는 [§사상의 차수와 Brouwer·Lefschetz 고정점 정리, ⁋명제 3](/ko/math/algebraic_topology/degree_and_fixed_point_theorems#prop3)의 homotopy 불변성과 상수사상의 차수가 $$0$$이라는 사실에 의하여 $$\deg(\iota\circ g)=0$$이다. 그러나 $$\iota\circ g$$는 antipodal이므로 [정리 5](#thm5)에 의하여 그 차수가 홀수여야 하고, 이는 $$0$$과 모순이다. 그러므로 그러한 $$g$$는 존재하지 않는다.

이로써 [정리 2](#thm2)의 (2)가 성립하고, [명제 3](#prop3)에 의하여 (1)도 성립하며, (3)은 [정리 5](#thm5) 그 자체이다.

</details>

<div class="remark" markdown="1">

<ins id="rmk7">**참고 7**</ins> [정리 2](#thm2)의 세 진술은 모두 참이지만, 우리가 실제로 세운 함의의 방향은 (3) $$\Rightarrow$$ (2) $$\Leftrightarrow$$ (1)이다. 곧 차수의 홀짝성을 다루는 (3)이 가장 강한 형태이며, 나머지 둘을 함의한다. (1)과 (2)의 동치는 [명제 3](#prop3)에서 보듯 초등적이지만, 이들로부터 차수가 정확히 홀수라는 (3)을 되돌려 얻는 것은 그만큼 직접적이지 않다. 문헌에 따라 "Borsuk–Ulam 정리"는 (1)이나 (2)를 가리키기도 하고, Borsuk의 원래 정리인 (3)을 가리키기도 한다.

</div>

## Ham sandwich 정리

Borsuk–Ulam 정리의 첫 귀결은 측도들을 동시에 이등분하는 초평면의 존재이다. 이름은 빵과 햄과 치즈로 이루어진 샌드위치를 한 번의 칼질로 세 재료 모두 정확히 반씩 나눌 수 있다는 삼차원의 그림에서 왔다. 이를 엄밀히 진술하려면 이등분의 대상이 될 측도의 조건을 정해야 한다. 우리는 각 초평면에 측도 $$0$$을 주는 유한 Borel measure를 다루는데, 이 조건은 예컨대 Lebesgue measure에 대해 절대연속인 유한측도가 모두 만족하며, 초평면 위에 질량이 뭉쳐 있지 않아 이등분이 연속적으로 변한다는 것을 보장한다.

<div class="proposition" markdown="1">

<ins id="thm8">**정리 8 (Ham sandwich)**</ins> $$\mathbb{R}^n$$ 위의 유한 Borel measure $$\mu_1,\ldots,\mu_n$$이 각각 모든 초평면에 측도 $$0$$을 준다고 하자. 그러면 하나의 affine 초평면이 존재하여 이들 $$n$$개의 측도를 동시에 이등분한다. 곧 그 초평면이 결정하는 두 닫힌 반공간 $$H,H'$$에 대하여 모든 $$i$$에서

$$\mu_i(H)=\mu_i(H')=\frac12\mu_i(\mathbb{R}^n)$$

이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

초평면 전체를 구 $$S^n$$으로 매개변수화한다. $$u=(u_0,u_1,\ldots,u_n)\in S^n\subseteq\mathbb{R}^{n+1}$$에 대하여 닫힌 반공간

$$H_u=\{x\in\mathbb{R}^n\mid u_1x_1+\cdots+u_nx_n\leq u_0\}$$

을 대응시키자. 대척점 $$-u$$에 대응하는 반공간은

$$H_{-u}=\{x\in\mathbb{R}^n\mid u_1x_1+\cdots+u_nx_n\geq u_0\}$$

이므로, $$H_u\cup H_{-u}=\mathbb{R}^n$$이고 $$H_u\cap H_{-u}$$은 초평면 $$\{u_1x_1+\cdots+u_nx_n=u_0\}$$이다. 가정에 의하여 각 $$\mu_i$$은 이 초평면에 측도 $$0$$을 주므로

$$\mu_i(H_u)+\mu_i(H_{-u})=\mu_i(\mathbb{R}^n)\tag{$\ast$}$$

이 성립한다.

이제 함수

$$f:S^n\rightarrow\mathbb{R}^n;\qquad f(u)=\bigl(\mu_1(H_u),\ldots,\mu_n(H_u)\bigr)$$

을 생각하자. 각 $$\mu_i$$이 유한하고 초평면에 측도 $$0$$을 준다는 조건에서, $$u$$를 조금 흔들 때 대칭차 $$H_u\triangle H_{u'}$$의 측도가 $$0$$으로 수렴하므로 $$u\mapsto\mu_i(H_u)$$은 연속이다. ([Mat]의 dominated convergence 논증을 따른다.) 따라서 $$f$$는 연속함수이며, [정리 2](#thm2)의 (1)에 의하여 $$f(u)=f(-u)$$인 점 $$u\in S^n$$이 존재한다. 곧 모든 $$i$$에서 $$\mu_i(H_u)=\mu_i(H_{-u})$$이고, $$(\ast)$$과 결합하면

$$\mu_i(H_u)=\mu_i(H_{-u})=\frac12\mu_i(\mathbb{R}^n)$$

이다.

남은 것은 이 $$u$$가 실제로 초평면을 결정함, 곧 $$(u_1,\ldots,u_n)\neq 0$$임을 확인하는 일이다. 만일 $$(u_1,\ldots,u_n)=0$$이라면 $$u=(\pm 1,0,\ldots,0)$$이고, 이때 $$H_u$$은 조건 $$0\leq u_0$$의 성립 여부에 따라 $$\mathbb{R}^n$$ 전체이거나 공집합이므로 $$\mu_i(H_u)\in\{0,\mu_i(\mathbb{R}^n)\}$$이다. 모든 $$\mu_i$$의 전체질량이 $$0$$인 자명한 경우에는 임의의 affine 초평면이 결정하는 두 반공간 $$H,H'$$에서 $$\mu_i(H)=\mu_i(H')=0$$이 자동으로 성립하여 이등분 조건이 자명하게 충족되므로 결론이 이미 성립한다. 그렇지 않아 어떤 $$\mu_i$$이 양의 전체질량을 가진다면, 위의 두 극점 $$u=(\pm 1,0,\ldots,0)$$에서는 $$\mu_i(H_u)\in\{0,\mu_i(\mathbb{R}^n)\}$$이 서로 달라 $$f(u)\neq f(-u)$$이 되므로 앞에서 찾은 점 $$u$$는 이 극점일 수 없다. 따라서 $$(u_1,\ldots,u_n)\neq 0$$이고 $$\{u_1x_1+\cdots+u_nx_n=u_0\}$$은 $$n$$개의 측도 $$\mu_1,\ldots,\mu_n$$을 동시에 이등분하는 초평면이다.

</details>

증명에서 antipodal 대칭은 두 반공간을 맞바꾸는 것으로 나타났으며, Borsuk–Ulam 정리가 제공하는 대척쌍 $$u,-u$$의 일치가 곧 두 반공간이 각 측도를 정확히 반씩 담는다는 이등분 조건이 되었다. 차원의 대응도 자연스럽다. $$\mathbb{R}^n$$의 affine 초평면은 방향과 위치를 합쳐 $$n$$개의 자유도를 가지며, 이는 $$S^n$$을 매개변수 공간으로 삼아 $$n$$개의 이등분 조건을 동시에 맞추기에 꼭 맞는 크기이다.

## Lusternik–Schnirelmann 덮개 정리

두 번째 귀결은 구를 닫힌집합들로 덮을 때 나타나는 조합적 제약이다. Antipode를 피하는 닫힌 덮개가 얼마나 많은 조각을 필요로 하는가라는 물음에 Borsuk–Ulam 정리가 정확한 하한을 준다.

<div class="proposition" markdown="1">

<ins id="thm9">**정리 9 (Lusternik–Schnirelmann–Borsuk)**</ins> $$S^n$$이 $$n+1$$개의 닫힌집합 $$A_1,\ldots,A_{n+1}$$의 합집합으로 덮인다고 하자. 그러면 어떤 $$A_j$$은 대척쌍을 포함한다. 곧 $$x,-x\in A_j$$인 점 $$x\in S^n$$이 존재하는 $$j$$가 있다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

처음 $$n$$개의 집합까지의 거리를 모아 연속함수

$$f:S^n\rightarrow\mathbb{R}^n;\qquad f(x)=\bigl(\operatorname{dist}(x,A_1),\ldots,\operatorname{dist}(x,A_n)\bigr)$$

을 정의하자. 각 $$\operatorname{dist}(\cdot,A_i)$$은 연속이므로 $$f$$도 연속이며, [정리 2](#thm2)의 (1)에 의하여 $$f(x)=f(-x)$$인 점 $$x\in S^n$$이 존재한다. 곧 모든 $$1\leq i\leq n$$에서 $$\operatorname{dist}(x,A_i)=\operatorname{dist}(-x,A_i)$$이다.

두 경우로 나눈다. 만일 어떤 $$1\leq i\leq n$$에서 $$\operatorname{dist}(x,A_i)=0$$이라면, $$A_i$$이 닫힌집합이므로 $$x\in A_i$$이고, 위의 등식에서 $$\operatorname{dist}(-x,A_i)=0$$이므로 $$-x\in A_i$$이다. 따라서 $$A_i$$이 대척쌍 $$x,-x$$을 포함한다.

반대로 모든 $$1\leq i\leq n$$에서 $$\operatorname{dist}(x,A_i)>0$$이라면, $$x$$와 $$-x$$ 둘 다 $$A_1,\ldots,A_n$$ 가운데 어느 것에도 속하지 않는다. 그런데 $$A_1,\ldots,A_{n+1}$$이 $$S^n$$을 덮으므로 $$x\in A_{n+1}$$이고 $$-x\in A_{n+1}$$이어야 한다. 따라서 이 경우에는 $$A_{n+1}$$이 대척쌍을 포함한다.

</details>

정리 9의 조각 개수 $$n+1$$은 더 줄일 수 없다는 의미에서 최적이다. 조각을 하나 더 허용하면 antipode를 완전히 피하는 닫힌 덮개가 실제로 존재하기 때문이다.

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> $$S^n$$은 대척쌍을 하나도 포함하지 않는 $$n+2$$개의 닫힌집합으로 덮인다. 원점을 내부에 품는 $$(n+1)$$-simplex $$\Delta\subseteq\mathbb{R}^{n+1}$$을 택하자. 예컨대 원점 중심의 정규 simplex를 잡으면 된다. 그 경계 $$\partial\Delta$$은 $$n+2$$개의 facet $$F_0,\ldots,F_{n+1}$$로 이루어지고, 원점이 내부에 있으므로 방사 사영

$$\pi:\partial\Delta\rightarrow S^n;\qquad\pi(y)=\frac{y}{\lvert y\rvert}$$

은 homeomorphism이다. 각 $$C_j=\pi(F_j)$$은 닫힌집합이고 $$S^n$$을 덮는다.

이제 각 $$C_j$$이 대척쌍을 포함하지 않음을 보인다. 원점이 $$\Delta$$의 내부에 있으므로 각 facet $$F_j$$은 원점을 지나지 않는 affine 초평면 $$\{y\mid\langle a_j,y\rangle=1\}$$에 놓이며, $$\Delta$$의 내부는 $$\langle a_j,\cdot\rangle<1$$ 쪽에 있다. 만일 $$v$$와 $$-v$$이 둘 다 $$C_j$$에 속한다면, 어떤 양수 $$s,t>0$$에 대하여 $$sv,-tv\in F_j$$이므로 $$\langle a_j,sv\rangle=1$$과 $$\langle a_j,-tv\rangle=1$$이 성립한다. 앞의 식은 $$\langle a_j,v\rangle=1/s>0$$을, 뒤의 식은 $$\langle a_j,v\rangle=-1/t<0$$을 주어 서로 모순이다. 그러므로 어떤 $$C_j$$도 대척쌍을 담지 않으며, $$n+2$$개의 조각으로는 antipode를 완전히 피할 수 있다. 이로써 [정리 9](#thm9)의 $$n+1$$이 최적임이 확인된다.

</div>

## 구의 매장 불가능성

마지막으로, Borsuk–Ulam 정리는 구가 한 차원 낮아 보이는 유클리드 공간에 들어갈 수 없다는 사실을 즉시 준다. 매장이 있다면 그것은 특히 단사인 연속함수를 낳는데, Borsuk–Ulam 정리는 그러한 단사성을 대척쌍에서 곧바로 무너뜨린다.

<div class="proposition" markdown="1">

<ins id="cor11">**따름정리 11**</ins> $$n\geq 1$$에 대하여, $$S^n$$은 $$\mathbb{R}^n$$에 위상적으로 매장되지 않는다. 곧 상 위로의 homeomorphism이 되는 연속 단사함수 $$e:S^n\rightarrow\mathbb{R}^n$$은 존재하지 않는다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

그러한 매장 $$e:S^n\rightarrow\mathbb{R}^n$$이 존재한다고 하자. 특히 $$e$$은 연속함수이므로 [정리 2](#thm2)의 (1)에 의하여 $$e(x)=e(-x)$$인 점 $$x\in S^n$$이 존재한다. $$n\geq 1$$에서 $$x\neq-x$$이므로 이는 $$e$$의 단사성에 모순이다. 따라서 그러한 매장은 존재하지 않는다.

</details>

같은 논증은 매장뿐 아니라 임의의 단사 연속함수 $$S^n\rightarrow\mathbb{R}^n$$의 비존재를 말해준다. 콤팩트 공간 $$S^n$$에서 Hausdorff 공간으로 가는 단사 연속함수는 자동으로 상 위로의 homeomorphism이 되므로 매장과 단사 연속함수는 이 맥락에서 사실상 같은 것이다. 결국 $$S^n$$의 대척 대합이 강제하는 $$f(x)=f(-x)$$이라는 한 점의 일치가, 구를 낮은 차원에 평탄하게 눕히려는 어떠한 시도도 좌절시키는 셈이다.

---

**참고문헌**

[Hat] A. Hatcher, *Algebraic Topology*. Cambridge University Press, 2002.  
[Mat] J. Matoušek, *Using the Borsuk–Ulam Theorem*. Springer, 2003.  
[Mun] J. R. Munkres, *Elements of Algebraic Topology*. Addison-Wesley, 1984.

---
