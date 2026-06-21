---
title: "Krull–Schmidt 정리"
description: "유한 길이 module과 quiver의 유한차원 representation에 대하여, indecomposable의 정의로부터 Fitting의 보조정리(M=ker φ^n ⊕ im φ^n)와 indecomposable의 endomorphism ring이 local임을 보이고, 이를 이용해 indecomposable들로의 분해가 isomorphism과 순서를 무시하면 유일하다는 Krull–Schmidt 정리를 local endomorphism ring의 exchange 논법으로 증명한다."
excerpt: "Fitting의 보조정리, indecomposable의 local endomorphism ring, Krull–Schmidt 정리"

categories: [Math / Representation Theory]
permalink: /ko/math/representation_theory/krull_schmidt
sidebar: 
    nav: "representation_theory-ko"

date: 2026-06-20
weight: 11

published: false

---

앞선 글에서 우리는 quiver $$Q$$의 representation들이 이루는 category $$\Rep(Q)$$가 path algebra $$kQ$$ 위의 left module들이 이루는 category와 동치임을 보였다 ([§Quiver와 경로대수, ⁋정리 12](/ko/math/representation_theory/path_algebras#thm12)). 이 동치 아래에서 유한차원 representation은 $$k$$ 위에서 유한차원인, 따라서 유한 길이를 갖는 $$kQ$$-module에 대응한다. 표현론의 첫 번째 목표는 이러한 대상들을 가능한 한 작은 조각으로 쪼개고 그 조각들을 분류하는 것이다. 이 글에서 우리는 그러한 분해가 존재하며 본질적으로 유일하다는 것, 곧 *Krull–Schmidt 정리*를 증명한다.

분해의 더 이상 쪼갤 수 없는 단위는 *indecomposable* 대상이다. 분해의 존재성은 길이에 대한 귀납으로 어렵지 않게 얻어지지만, 유일성은 그렇지 않다. 유일성의 핵심은 indecomposable 대상의 endomorphism ring이 *local ring*이라는 사실이며, 이는 다시 *Fitting의 보조정리*로부터 따라온다. 이 글에서 $$k$$는 field이고, module이라 하면 별다른 언급이 없는 한 left module을 뜻한다. 길이와 합성열의 일반론은 [\[가환대수학\] §조르단-횔더 정리, ⁋정의 2](/ko/math/commutative_algebra/Jordan-Holder_theorem#def2)에서 다룬 것을 따른다. $$\Rep(Q)\cong\lMod{kQ}$$의 동치 덕분에 우리는 representation과 module을 자유롭게 오가며, 결과는 어느 쪽 언어로 적어도 무방하다.

## Indecomposable

분해를 논하기 위해 먼저 더 이상 쪼갤 수 없는 대상을 정의한다. 자명한 직합 $$M=M\oplus 0$$은 분해로 치지 않으므로, 두 *nonzero* submodule의 직합으로 적히지 않는다는 조건을 붙인다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $$A$$-module $$M$$이 *indecomposable<sub>분해불가능</sub>*이라는 것은 $$M\neq 0$$이며, $$M=M_1\oplus M_2$$이도록 하는 nonzero submodule $$M_1,M_2$$가 존재하지 않는 것이다. 곧 $$M$$이 두 submodule의 직합으로 적힐 때마다 그중 하나는 반드시 $$0$$이어야 한다. Quiver $$Q$$의 representation $$V$$가 indecomposable이라는 것도 같은 방식으로, $$V\neq 0$$이며 $$V=V_1\oplus V_2$$가 nonzero representation들의 직합이 될 수 없다는 것으로 정의한다.

</div>

$$\Rep(Q)\cong\lMod{kQ}$$ 아래에서 representation의 direct sum이 module의 direct sum에 대응하므로 ([§Quiver와 경로대수, ⁋정의 11](/ko/math/representation_theory/path_algebras#def11)), representation $$V$$가 indecomposable인 것과 대응하는 $$kQ$$-module이 indecomposable인 것은 동치이다. 따라서 두 정의는 동치의 양변에서 같은 개념을 가리킨다.

한 module이 둘 이상의 submodule의 직합 $$M=M_1\oplus\cdots\oplus M_r$$로 적힐 때, 각 $$M_i$$가 다시 indecomposable이면 이를 $$M$$의 *indecomposable 분해*라 부른다. Indecomposable의 정의는 이러한 분해를 더 이상 정련할 수 없게 만드는 최소 단위를 골라낸 것이다. Direct sum의 정사영과 포함을 통해, $$M=M_1\oplus M_2$$인 nonzero 분해가 존재한다는 것은 $$M$$ 위에 $$\id_M$$도 $$0$$도 아닌 idempotent endomorphism이 존재한다는 것과 동치인데, 이 관점은 [보조정리 3](#lem3) 이후에 다시 쓰인다.

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> Simple module은 indecomposable이다. $$M$$이 simple이면 ([\[가환대수학\] §조르단-횔더 정리, ⁋정의 1](/ko/math/commutative_algebra/Jordan-Holder_theorem#def1)) submodule이 $$0$$과 $$M$$ 뿐이므로 $$M=M_1\oplus M_2$$일 때 $$M_1,M_2$$ 각각이 $$0$$ 또는 $$M$$이고, 둘이 직합을 이루려면 그중 하나는 $$0$$이어야 한다. 그러나 그 역은 성립하지 않는다. 선형 $$A_2$$ quiver $$1\xrightarrow{\ \alpha\ }2$$ ([§Quiver와 경로대수, ⁋예시 6](/ko/math/representation_theory/path_algebras#ex6)) 에서 representation

$$V:\quad k\xrightarrow{\ 1\ }k$$

곧 $$V_1=V_2=k$$이고 $$V_\alpha=\id_k$$인 representation을 생각하자. $$V$$의 nonzero subrepresentation $$W$$가 $$V$$의 진부분이려면 $$W_1,W_2$$ 중 적어도 하나가 $$0$$이어야 하는데, $$V_\alpha=\id_k$$가 동형이므로 $$W_1\neq 0$$이면 $$W_2=V_\alpha(W_1)=k$$이고, 따라서 $$W$$를 다른 subrepresentation으로 보충하여 $$V$$를 nonzero 직합으로 적을 수 없다. 곧 $$V$$는 indecomposable이지만, $$V_1\neq 0\neq V_2$$이므로 simple은 아니다.

</div>

위 예시는 indecomposable이 simple보다 진정으로 약한 개념임을 보여 준다. Simple module은 부분구조가 전혀 없는 대상인 반면, indecomposable module은 부분구조를 가질 수 있되 전체를 두 조각의 직합으로 갈라놓는 분해만 허용하지 않는다. 표현론에서 분류의 단위가 되는 것은 simple이 아니라 indecomposable이며, 이 글의 정리는 모든 유한차원 representation이 indecomposable들의 직합으로, 그것도 본질적으로 유일하게 적힌다는 것을 보장한다.

## Fitting의 보조정리

분해의 유일성으로 가는 첫 단계는 indecomposable 대상의 endomorphism들을 통제하는 것이다. 유한 길이 module 위의 endomorphism $$\varphi$$를 반복 적용하면, image들의 내림사슬과 kernel들의 오름사슬이 모두 유한 길이라는 제약 때문에 결국 안정된다. 이 안정점에서 module이 kernel 부분과 image 부분으로 깔끔하게 갈라진다는 것이 Fitting의 보조정리이다.

<div class="proposition" markdown="1">

<ins id="lem3">**보조정리 3**</ins> (Fitting) $$M$$이 유한 길이 $$A$$-module이고 $$\varphi\in\End_A(M)$$이라 하자. 그럼 충분히 큰 $$n$$에 대하여

$$M=\ker\varphi^n\oplus\im\varphi^n$$

이 성립한다. 더 나아가 $$M$$이 indecomposable이면 임의의 $$\varphi\in\End_A(M)$$은 nilpotent이거나 automorphism이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Image들의 사슬과 kernel들의 사슬

$$\im\varphi\supseteq\im\varphi^2\supseteq\im\varphi^3\supseteq\cdots,\qquad \ker\varphi\subseteq\ker\varphi^2\subseteq\ker\varphi^3\subseteq\cdots$$

을 생각하자. $$M$$이 유한 길이를 가지므로 artinian인 동시에 noetherian이고 ([\[가환대수학\] §조르단-횔더 정리, ⁋정리 3](/ko/math/commutative_algebra/Jordan-Holder_theorem#thm3)), 따라서 첫째 내림사슬과 둘째 오름사슬은 모두 어느 단계에서 멈춘다. 곧 적당한 $$n$$이 있어 $$m\geq n$$이면

$$\im\varphi^m=\im\varphi^n,\qquad \ker\varphi^m=\ker\varphi^n$$

이 된다. 이러한 $$n$$을 하나 고정하고 $$N=\ker\varphi^n$$, $$I=\im\varphi^n$$으로 적자.

먼저 $$N\cap I=0$$임을 보인다. $$x\in N\cap I$$이면 $$\varphi^n(x)=0$$이고 $$x=\varphi^n(y)$$인 $$y\in M$$이 있다. 그럼 $$\varphi^{2n}(y)=\varphi^n(x)=0$$이므로 $$y\in\ker\varphi^{2n}=\ker\varphi^n$$이고, 따라서 $$x=\varphi^n(y)=0$$이다. 다음으로 $$M=N+I$$임을 보인다. 임의의 $$x\in M$$에 대하여 $$\varphi^n(x)\in\im\varphi^n=\im\varphi^{2n}$$이므로 $$\varphi^n(x)=\varphi^{2n}(z)$$인 $$z\in M$$이 있다. 그럼

$$x=\bigl(x-\varphi^n(z)\bigr)+\varphi^n(z)$$

인데, 우변 첫째 항은 $$\varphi^n\bigl(x-\varphi^n(z)\bigr)=\varphi^n(x)-\varphi^{2n}(z)=0$$이므로 $$N$$에 속하고, 둘째 항은 $$I$$에 속한다. 따라서 $$M=N\oplus I=\ker\varphi^n\oplus\im\varphi^n$$이다.

이제 $$M$$이 indecomposable이라 하자. 위의 직합에서 indecomposable의 정의에 의하여 $$N$$과 $$I$$ 중 하나는 $$0$$이다. $$N=\ker\varphi^n=0$$이면 $$\varphi^n$$이 단사이고, 유한차원이 아니어도 유한 길이 module 위의 단사 endomorphism은 전사이다. 실제로 $$\im\varphi^n=\im\varphi^{2n}$$과 $$\ker\varphi^n=0$$으로부터, 임의의 $$x$$에 대하여 $$\varphi^n(x)=\varphi^{2n}(z)$$인 $$z$$를 잡으면 $$\varphi^n\bigl(x-\varphi^n(z)\bigr)=0$$이어서 $$x=\varphi^n(z)\in\im\varphi^n$$이므로 $$\varphi^n$$은 전사이다. 따라서 $$\varphi^n$$이 동형이고, 그럼 $$\varphi$$ 또한 동형, 곧 automorphism이다. 반대로 $$I=\im\varphi^n=0$$이면 $$\varphi^n=0$$이므로 $$\varphi$$는 nilpotent이다. 두 경우가 indecomposable에서 망라되므로 결론을 얻는다.

</details>

위 증명에서 직합 $$M=\ker\varphi^n\oplus\im\varphi^n$$이 indecomposable 가정 아래 둘 중 하나가 사라지도록 강제된다는 점이 본질적이다. $$N=0$$인 경우가 automorphism, $$I=0$$인 경우가 nilpotent에 해당하며, 이 두 경우 사이에는 중간 지대가 없다. 이로부터 indecomposable의 endomorphism ring의 구조가 곧바로 결정된다.

<div class="proposition" markdown="1">

<ins id="cor4">**따름정리 4**</ins> $$M$$이 유한 길이를 갖는 indecomposable $$A$$-module이면, endomorphism ring $$\End_A(M)$$은 *local ring*이다. 곧 가역이 아닌 원소들의 집합 $$\mathfrak{m}=\{\varphi\in\End_A(M)\mid \varphi\text{ is not an automorphism}\}$$이 양측 ideal을 이루며, 이것이 $$\End_A(M)$$의 유일한 maximal left ideal이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[보조정리 3](#lem3)에 의하여 $$\mathfrak{m}$$은 정확히 nilpotent endomorphism들의 집합이다. Local ring임을 보이려면 $$\mathfrak{m}$$이 양측 ideal이고 두 비가역원의 합이 다시 비가역임을 보이면 충분하다. 비가역원들의 집합이 ideal을 이루면 그것이 모든 proper left ideal을 포함하므로 유일한 maximal left ideal이 되기 때문이다.

$$\varphi\in\mathfrak{m}$$이고 $$\psi\in\End_A(M)$$이라 하자. $$\psi\varphi$$가 automorphism이라 가정하면 $$\varphi$$가 단사이고, [보조정리 3](#lem3)의 증명에서 보았듯 유한 길이 module 위의 단사 endomorphism은 전사이므로 $$\varphi$$가 automorphism이 되어 가정에 모순이다. 따라서 $$\psi\varphi\in\mathfrak{m}$$이다. 마찬가지로 $$\varphi\psi$$가 automorphism이면 $$\varphi$$가 전사이고, 유한 길이 module 위의 전사 endomorphism은 단사이므로 ($$\length(\im\varphi)=\length(M)$$이려면 $$\ker\varphi=0$$이어야 한다) $$\varphi$$가 automorphism이 되어 모순이다. 따라서 $$\varphi\psi\in\mathfrak{m}$$이며, $$\mathfrak{m}$$은 곱셈에 대하여 닫혀 있다.

이제 $$\varphi,\psi\in\mathfrak{m}$$이고 $$\varphi+\psi$$가 automorphism이라 가정하여 모순을 이끈다. $$\eta=(\varphi+\psi)^{-1}$$로 두면 $$\eta\varphi+\eta\psi=\id_M$$이다. 앞 문단에서 보인 대로 $$\eta\varphi,\eta\psi\in\mathfrak{m}$$, 곧 둘 다 nilpotent이다. $$\rho=\eta\varphi$$로 두면 $$\eta\psi=\id_M-\rho$$이다. $$\rho$$가 nilpotent, 곧 적당한 $$N$$에 대하여 $$\rho^N=0$$이면

$$(\id_M-\rho)(\id_M+\rho+\rho^2+\cdots+\rho^{N-1})=\id_M-\rho^N=\id_M$$

이므로 $$\id_M-\rho=\eta\psi$$가 automorphism이 되는데, 이는 $$\eta\psi\in\mathfrak{m}$$에 모순이다. 따라서 $$\varphi+\psi\in\mathfrak{m}$$이고, $$\mathfrak{m}$$은 덧셈에 대하여 닫혀 있다. 이로써 $$\mathfrak{m}$$은 양측 ideal이며 $$\End_A(M)$$은 local ring이다.

</details>

따름정리 4가 주는 정보를 다음 형태로 다시 적어 두면 유일성 증명에서 곧장 쓸 수 있다. Local ring $$R=\End_A(M)$$에서는 두 원소의 합 $$\varphi+\psi$$가 가역이면 $$\varphi,\psi$$ 중 적어도 하나가 가역이다. 만일 둘 다 비가역이면 $$\mathfrak{m}$$이 ideal이므로 합도 $$\mathfrak{m}$$에 속하여 비가역이 될 것이기 때문이다. 귀납적으로, 유한합 $$\varphi_1+\cdots+\varphi_r$$이 가역이면 어떤 $$\varphi_i$$가 가역이다. 이것이 아래 exchange 논법의 동력이 된다.

## Krull–Schmidt 정리

이제 유한 길이 module의 indecomposable 분해가 존재하며 isomorphism과 순서를 무시하면 유일함을 증명한다. 존재성은 길이에 대한 귀납으로, 유일성은 endomorphism ring이 local이라는 사실을 이용한 exchange 논법으로 얻는다. 다음 보조정리가 두 분해를 맞바꾸는 핵심 단계를 담는다.

<div class="proposition" markdown="1">

<ins id="lem5">**보조정리 5**</ins> $$M$$이 유한 길이를 갖는 indecomposable $$A$$-module이라 하자. $$M\cong N_1\oplus\cdots\oplus N_s$$인 동형이 주어지고, 이 분해에 대한 정사영 $$\pi_j:M\rightarrow N_j$$와 포함 $$\iota_j:N_j\rightarrow M$$을 생각하면 $$\sum_{j=1}^s\iota_j\pi_j=\id_M$$이다. 그럼 어떤 $$j$$가 존재하여 $$\pi_j:M\rightarrow N_j$$가 split monomorphism, 곧 왼쪽 역을 가지는 단사사상이고, 그 상 $$\pi_j(M)$$은 $$N_j$$의 한 direct summand이다. 특히 그 $$N_j$$가 indecomposable이면 $$\pi_j:M\rightarrow N_j$$는 isomorphism이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

분해 $$M\cong N_1\oplus\cdots\oplus N_s$$를 동일시하면 정사영과 포함의 정의로부터 $$\sum_{j=1}^s\iota_j\pi_j=\id_M$$이다. $$\id_M$$은 $$\End_A(M)$$의 가역원이고, $$M$$이 유한 길이 indecomposable이므로 [따름정리 4](#cor4)에 의하여 $$\End_A(M)$$은 local ring이다. 따름정리 4 직후에 관찰한 대로, local ring에서 가역원이 유한개의 합으로 적히면 그 합의 항 중 적어도 하나가 가역이다. 따라서 어떤 $$j$$에 대하여 $$\theta:=\iota_j\pi_j\in\End_A(M)$$이 automorphism이다.

이 $$j$$를 고정하자. $$\theta=\iota_j\pi_j$$가 가역이므로

$$(\theta^{-1}\iota_j)\circ\pi_j=\theta^{-1}(\iota_j\pi_j)=\theta^{-1}\theta=\id_M$$

이고, 따라서 $$\pi_j:M\rightarrow N_j$$는 왼쪽 역 $$\sigma:=\theta^{-1}\iota_j:N_j\rightarrow M$$을 가지는 split monomorphism이다. 일반적으로 왼쪽 역 $$\sigma$$를 가지는 사상 $$\pi_j$$에 대하여 $$\pi_j\sigma:N_j\rightarrow N_j$$는 $$(\pi_j\sigma)(\pi_j\sigma)=\pi_j(\sigma\pi_j)\sigma=\pi_j\sigma$$이므로 idempotent이고, 이로부터 $$N_j=\im(\pi_j\sigma)\oplus\ker(\pi_j\sigma)$$이며 $$\im(\pi_j\sigma)=\pi_j(M)$$이다. 곧 $$\pi_j(M)$$은 $$N_j$$의 direct summand이고, $$\pi_j$$는 $$M$$에서 이 summand 위로의 isomorphism이다.

끝으로 $$N_j$$가 indecomposable이라 하자. $$N_j=\pi_j(M)\oplus\ker(\pi_j\sigma)$$인데 $$\pi_j(M)\cong M\neq 0$$이므로 indecomposable의 정의에 의하여 $$\ker(\pi_j\sigma)=0$$, 곧 $$\pi_j(M)=N_j$$이다. 따라서 단사사상 $$\pi_j:M\rightarrow N_j$$가 전사이기도 하여 isomorphism이다.

</details>

위 보조정리의 핵심은 다음과 같다. 유한 길이 indecomposable $$M$$이 indecomposable들의 직합 $$N_1\oplus\cdots\oplus N_s$$와 동형이면, 정사영 $$\pi_j$$ 중 적어도 하나가 $$M$$과 $$N_j$$ 사이의 isomorphism이다. 곧 indecomposable $$M$$은 그것과 동형인 임의의 indecomposable 분해의 한 조각과 반드시 동형이다. 이 관찰을 두 분해에 적용하면 분해의 유일성이 따라온다.

<div class="proposition" markdown="1">

<ins id="thm6">**정리 6**</ins> (Krull–Schmidt) $$M$$이 nonzero 유한 길이 $$A$$-module이면, $$M$$은 유한개의 indecomposable submodule들의 직합

$$M=M_1\oplus M_2\oplus\cdots\oplus M_r$$

으로 적힌다. 또한 이 분해는 isomorphism과 순서를 무시하면 유일하다. 곧 다른 indecomposable 분해 $$M=N_1\oplus\cdots\oplus N_s$$가 주어지면 $$r=s$$이고, 적절한 치환 $$\sigma$$가 존재하여 모든 $$i$$에 대하여 $$M_i\cong N_{\sigma(i)}$$이다.

특히 quiver $$Q$$의 임의의 nonzero 유한차원 representation은 indecomposable representation들의 직합으로 적히며, 그 분해는 isomorphism과 순서를 무시하면 유일하다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

**존재성.** $$\length(M)$$에 대한 귀납으로 보인다. $$M$$이 indecomposable이면 자기 자신이 길이 $$1$$짜리 indecomposable 분해이다. 그렇지 않으면 $$M=M'\oplus M''$$인 nonzero submodule $$M',M''$$이 있고, 직합에서 각 인자의 길이가 진하게 작으므로 $$\length(M')<\length(M)$$이고 $$\length(M'')<\length(M)$$이다. 귀납가정에 의하여 $$M'$$과 $$M''$$이 각각 indecomposable 분해를 가지고, 이들을 합치면 $$M$$의 indecomposable 분해를 얻는다. 길이가 유한이므로 이 과정은 유한 번에 끝난다.

**유일성.** 두 indecomposable 분해

$$M=M_1\oplus\cdots\oplus M_r=N_1\oplus\cdots\oplus N_s$$

가 주어졌다 하자. $$r$$에 대한 귀납으로 진행한다. $$r=0$$이면 $$M=0$$이고 $$s=0$$이므로 자명하다. $$r\geq 1$$이라 하자. $$M_1$$에 관련된 사상들을 모은다. 둘째 분해에 대한 정사영 $$\pi_j:M\rightarrow N_j$$와 포함 $$\iota_j:N_j\rightarrow M$$, 그리고 첫째 분해에 대한 $$M_1$$로의 정사영 $$p:M\rightarrow M_1$$과 포함 $$q:M_1\rightarrow M$$을 생각하자. $$\sum_{j=1}^s\iota_j\pi_j=\id_M$$이므로 $$M_1$$ 위에서

$$\sum_{j=1}^s (p\,\iota_j)(\pi_j\,q)=p\Bigl(\sum_{j=1}^s\iota_j\pi_j\Bigr)q=p\,q=\id_{M_1}$$

이 성립한다. 여기서 각 $$p\iota_j\pi_j q$$는 $$M_1$$의 endomorphism이다. $$M_1$$이 유한 길이 indecomposable이므로 [따름정리 4](#cor4)에 의하여 $$\End_A(M_1)$$은 local ring이고, 가역원 $$\id_{M_1}$$이 위와 같이 $$s$$개의 합으로 적혔으므로 어떤 $$j$$에 대하여 $$g:=(p\iota_j)(\pi_j q)\in\End_A(M_1)$$이 automorphism이다. 순서를 바꾸어 $$j=1$$이라 해도 좋다.

이제 $$f:=\pi_1 q:M_1\rightarrow N_1$$과 $$h:=p\iota_1:N_1\rightarrow M_1$$을 보면 $$hf=g$$가 automorphism이다. 따라서 $$f$$는 단사이고 $$g^{-1}h$$가 $$f$$의 왼쪽 역이므로 $$f$$는 split monomorphism이며, $$f(M_1)$$은 $$N_1$$의 direct summand이다. 그런데 $$N_1$$이 indecomposable이고 $$f(M_1)\cong M_1\neq 0$$이므로, [보조정리 5](#lem5)의 마지막 결론과 같은 논법에 의하여 $$f:M_1\rightarrow N_1$$이 isomorphism이다.

이로부터 $$M_1\cong N_1$$을 얻었다. 남은 것은 $$M_1$$을 떼어낸 나머지가 다시 같은 형태의 두 분해를 이룬다는 것이며, 이를 위해 $$N_1$$이 $$M_2\oplus\cdots\oplus M_r$$의 보충으로 $$M_1$$을 대신할 수 있음을 보인다. $$M''=M_2\oplus\cdots\oplus M_r$$로 두면 $$M=M_1\oplus M''$$이고 $$p:M\rightarrow M_1$$은 $$M''$$을 따른 정사영이다. 합성

$$p\,\iota_1=h:N_1\rightarrow M_1$$

은 $$hf=g$$가 동형이고 $$f$$가 동형이므로 $$h=gf^{-1}$$ 또한 동형이다. 따라서 $$\iota_1(N_1)\cap M''=0$$이다. 실제로 $$x\in\iota_1(N_1)\cap M''$$이면 $$x=\iota_1(y)$$인 $$y\in N_1$$이 있고 $$x\in M''=\ker p$$이므로 $$h(y)=p\iota_1(y)=p(x)=0$$인데, $$h$$가 단사이므로 $$y=0$$, 곧 $$x=0$$이다. 또 길이를 비교하면 $$\length(\iota_1(N_1))+\length(M'')=\length(N_1)+\length(M'')=\length(M_1)+\length(M'')=\length(M)$$이므로, $$\iota_1(N_1)\oplus M''$$이 $$M$$의 길이와 같은 submodule이어서 $$M$$ 전체와 일치한다. 곧

$$M=N_1\oplus M''=N_1\oplus M_2\oplus\cdots\oplus M_r$$

이 성립한다 (여기서 $$\iota_1(N_1)$$을 $$N_1$$과 동일시하였다). 한편 $$M=N_1\oplus N_2\oplus\cdots\oplus N_s$$였으므로, 두 직합에서 공통 인자 $$N_1$$을 소거하면

$$M_2\oplus\cdots\oplus M_r\cong N_2\oplus\cdots\oplus N_s$$

를 얻는다. 좌변은 $$r-1$$개의 indecomposable 분해이므로 귀납가정에 의하여 $$r-1=s-1$$, 곧 $$r=s$$이고, $$\{2,\ldots,r\}$$ 위의 치환 $$\sigma'$$가 존재하여 $$M_i\cong N_{\sigma'(i)}$$이다. 여기에 $$M_1\cong N_1$$을 더하면 원하는 치환 $$\sigma$$를 얻는다.

마지막으로 representation에 대한 진술은 $$\Rep(Q)\cong\lMod{kQ}$$의 동치에서 따라온다 ([§Quiver와 경로대수, ⁋정리 12](/ko/math/representation_theory/path_algebras#thm12)). 유한차원 representation은 $$k$$ 위에서 유한차원, 따라서 유한 길이인 $$kQ$$-module에 대응하고, indecomposable representation은 indecomposable module에 대응하며 direct sum이 보존되므로, module에 대한 위의 결과가 그대로 옮겨진다.

</details>

위 증명의 핵심은 첫째 분해의 indecomposable 조각 $$M_1$$을 둘째 분해의 어떤 조각 $$N_1$$과 맞바꾸어 $$M=N_1\oplus M_2\oplus\cdots\oplus M_r$$를 얻은 데에 있다. 이렇게 한 분해의 한 조각을 다른 분해의 조각으로 교체할 수 있다는 성질을 *exchange property*라 부르며, [따름정리 4](#cor4)가 보장하는 local endomorphism ring이 정확히 이 교체를 가능케 하는 조건이다. 일단 $$M_1$$을 $$N_1$$로 바꾸고 나면 양쪽 분해에서 $$N_1$$을 소거하여 $$M_2\oplus\cdots\oplus M_r\cong N_2\oplus\cdots\oplus N_s$$를 얻고, 귀납이 이를 마무리한다.

이 정리가 보장하는 유일성 덕분에, 유한차원 representation $$V$$에 대하여 그 분해에 나타나는 indecomposable들의 isomorphism class와 각각의 중복도가 $$V$$의 불변량으로 잘 정의된다. 따라서 $$\Rep(Q)$$의 유한차원 대상을 이해하는 문제는 indecomposable representation들을 isomorphism을 무시하고 분류하는 문제로 환원된다. 예시 2에서 보았듯 선형 $$A_2$$ quiver의 indecomposable은 두 simple representation과 한 개의 비simple indecomposable로 이루어지며, 이러한 분류가 모든 quiver에 대하여 가능한지, 가능하다면 그 목록이 무엇인지가 다음 논의의 주제이다.

<div class="remark" markdown="1">

<ins id="rmk7">**참고 7**</ins> Krull–Schmidt 정리는 indecomposable들의 isomorphism class를 유한차원 representation 이론의 기본 단위로 확정한다. 이 단위 위에서 indecomposable들 사이의 사상을 체계적으로 기술하는 것이 *Auslander–Reiten 이론*이며, almost split sequence와 Auslander–Reiten quiver가 그 핵심 도구이다. 또한 어떤 quiver $$Q$$가 유한개의 indecomposable representation만을 가지는지, 곧 *representation-finite*인지를 묻는 문제의 답이 *Gabriel의 정리*로, $$Q$$의 underlying graph가 type $$A$$, $$D$$, $$E$$의 Dynkin diagram일 때에 한정된다. 두 이론 모두 분해의 존재성과 유일성을 전제로 indecomposable의 세계를 분석하므로, 이 글의 결과가 그 출발점에 놓인다.

</div>

---

**참고문헌**

**[ASS]** I. Assem, D. Simson, and A. Skowroński, *Elements of the representation theory of associative algebras, Volume 1: Techniques of representation theory*, Cambridge University Press, 2006.

**[Sch]** R. Schiffler, *Quiver representations*, Springer, 2014.

**[DW]** H. Derksen and J. Weyman, *An introduction to quiver representations*, American Mathematical Society, 2017.

**[Bass]** H. Bass, *Algebraic K-theory*, W. A. Benjamin, 1968.
