---
title: "콤팩트 실형식"
description: "복소 Lie algebra의 real form을 복소화가 원래 대수가 되는 실형식으로 정의하고, Killing form이 음의 정부호인 compact real form을 도입한다. 복소 semisimple Lie algebra가 Chevalley basis로부터 항상 compact real form을 가짐을 보이고 그 유일성을 conjugation을 통해 논한 뒤, Weyl의 unitarian trick으로 완전가약성의 군론적 증명을 제시한다."
excerpt: "real form, compact real form, Killing form 음의 정부호, Chevalley basis 구성, 유일성, Weyl unitarian trick, su(n)·so(n)·sp(n)"

categories: [Math / Lie Theory]
permalink: /ko/math/lie_theory/compact_real_form
sidebar: 
    nav: "lie_theory-ko"

date: 2026-06-21
weight: 7.6

published: false
---

복소수체 위의 semisimple Lie algebra $$\mathfrak{g}$$는 Cartan subalgebra와 root system을 통해 그 구조가 완전히 결정되지만 ([§근계, ⁋명제 12](/ko/math/lie_theory/root_systems#prop12)), 이 복소 대수가 실수 위에서 몇 가지 본질적으로 다른 모습으로 실현된다는 사실은 표현론과 미분기하 양쪽에서 중요하다. 가령 $$\sl(2;\mathbb{C})$$는 $$\sl(2;\mathbb{R})$$로도, $$\su(2)$$로도 복소화되는데, 두 실대수는 같은 복소화를 가지면서도 전혀 다른 군을 만든다. 전자에 대응하는 군 $$\SL(2;\mathbb{R})$$은 noncompact이고 후자에 대응하는 군 $$\SU(2)$$는 compact이다. 이 글에서 우리는 복소 Lie algebra의 *real form*을 그 복소화가 원래 대수가 되는 실대수로 정의하고, 그중에서도 Killing form이 음의 정부호인 *compact real form*에 주목한다. 핵심 결과는 임의의 복소 semisimple Lie algebra가 항상 compact real form을 가지며 그것이 본질적으로 유일하다는 것, 그리고 이 compact form을 매개로 한 Weyl의 unitarian trick이 semisimple Lie algebra의 완전가약성에 군론적 증명을 제공한다는 것이다.

이 글에서 별다른 언급이 없는 한 $$\mathfrak{g}$$는 $$\mathbb{C}$$ 위의 유한차원 Lie algebra이고, real form을 다룰 때 $$\mathfrak{g}_0,\mathfrak{u}$$ 등은 $$\mathbb{R}$$ 위의 유한차원 Lie algebra이다. Killing form은 [§Killing 형식과 Cartan 판정법, ⁋정의 1](/ko/math/lie_theory/killing_form_and_cartan_criterion#def1)에서 정의한 $$\kappa(x,y)=\tr(\ad x\,\ad y)$$를 가리킨다.

## Real form

복소 벡터공간을 실 벡터공간으로 보면 차원이 두 배가 되며, 거꾸로 실 벡터공간에 복소수 스칼라를 허용하는 복소화가 있다. Lie algebra에 대해서도 같은 두 방향이 있으나, 우리가 관심을 두는 것은 주어진 복소 대수를 복소화로 갖는 실대수가 무엇인가 하는 역방향이다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $$\mathfrak{g}_0$$가 $$\mathbb{R}$$ 위의 Lie algebra일 때, 실 벡터공간 $$\mathfrak{g}_0\otimes_{\mathbb{R}}\mathbb{C}$$ 위에

$$[x\otimes\lambda,\,y\otimes\mu]=[x,y]\otimes\lambda\mu$$

으로 bracket을 확장하면 $$\mathbb{C}$$ 위의 Lie algebra가 되며, 이를 $$\mathfrak{g}_0$$의 *complexification<sub>복소화</sub>* $$(\mathfrak{g}_0)_{\mathbb{C}}$$라 부른다. 거꾸로 $$\mathbb{C}$$ 위의 Lie algebra $$\mathfrak{g}$$에 대하여, $$\mathbb{R}$$ 위의 Lie algebra $$\mathfrak{g}_0$$가 $$\mathfrak{g}$$의 *real form<sub>실형식</sub>*이라는 것은 Lie algebra isomorphism

$$(\mathfrak{g}_0)_{\mathbb{C}}=\mathfrak{g}_0\otimes_{\mathbb{R}}\mathbb{C}\xrightarrow{\ \sim\ }\mathfrak{g}$$

이 존재하는 것이다.

</div>

복소화의 bracket이 $$\mathbb{C}$$-bilinear가 되도록 위와 같이 잘 정의됨은 $$\mathfrak{g}_0$$의 bracket이 $$\mathbb{R}$$-bilinear라는 데에서 곧바로 따른다. 실 벡터공간으로서 $$\mathfrak{g}_0\otimes_{\mathbb{R}}\mathbb{C}=\mathfrak{g}_0\oplus i\mathfrak{g}_0$$이므로, real form을 가진 $$\mathfrak{g}$$는 $$\dim_{\mathbb{C}}\mathfrak{g}=\dim_{\mathbb{R}}\mathfrak{g}_0$$을 만족한다. real form을 등가적으로 기술하는 것은 $$\mathfrak{g}$$ 위의 *conjugation*, 곧 복소 켤레의 추상적 대응물이다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> $$\mathbb{C}$$ 위의 Lie algebra $$\mathfrak{g}$$ 위에서 *conjugation<sub>켤레</sub>*은 다음을 만족하는 사상 $$\tau:\mathfrak{g}\rightarrow\mathfrak{g}$$이다.

1. $$\tau$$는 $$\mathbb{R}$$-선형이고 $$\tau(\lambda x)=\bar\lambda\,\tau(x)$$ (곧 $$\tau$$는 conjugate-linear)이다.
2. $$\tau$$는 involution, 곧 $$\tau^2=\id$$이다.
3. $$\tau$$는 bracket을 보존한다. 곧 $$\tau([x,y])=[\tau x,\tau y]$$이다.

</div>

Conjugation $$\tau$$가 주어지면 그 고정점 집합 $$\mathfrak{g}^{\tau}=\{x\in\mathfrak{g}\mid\tau x=x\}$$은 $$\mathbb{R}$$ 위의 Lie subalgebra가 되고, $$\tau$$가 conjugate-linear involution이라는 데에서 $$\mathfrak{g}=\mathfrak{g}^{\tau}\oplus i\mathfrak{g}^{\tau}$$로 분해된다. 임의의 $$x\in\mathfrak{g}$$에 대하여 $$\tfrac12(x+\tau x)$$는 $$\tau$$-고정, $$\tfrac1{2i}(x-\tau x)$$도 $$\tau$$-고정이고 $$x=\tfrac12(x+\tau x)+i\cdot\tfrac1{2i}(x-\tau x)$$이기 때문이다. 따라서 $$\mathfrak{g}^{\tau}$$는 $$\mathfrak{g}$$의 real form이며, 역으로 real form $$\mathfrak{g}_0\subseteq\mathfrak{g}$$가 주어지면 $$\mathfrak{g}=\mathfrak{g}_0\oplus i\mathfrak{g}_0$$ 위에서 $$\tau(x+iy)=x-iy$$ ($$x,y\in\mathfrak{g}_0$$)로 정의된 conjugation이 $$\mathfrak{g}_0$$를 고정점 집합으로 갖는다. 이로써 real form과 conjugation은 일대일로 대응한다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> $$\mathfrak{g}_0$$가 복소 Lie algebra $$\mathfrak{g}$$의 real form이고 $$\kappa_0,\kappa$$가 각각 $$\mathfrak{g}_0,\mathfrak{g}$$의 Killing form이면, $$\kappa$$를 $$\mathfrak{g}_0\times\mathfrak{g}_0$$로 제한한 것은 $$\kappa_0$$와 같다. 특히 $$\mathfrak{g}$$의 Killing form은 $$\mathfrak{g}_0$$의 Killing form의 $$\mathbb{C}$$-bilinear 확장이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\mathfrak{g}_0$$의 $$\mathbb{R}$$-기저 $$(x_1,\ldots,x_n)$$을 택하면, 이는 곧 $$\mathfrak{g}=\mathfrak{g}_0\otimes_{\mathbb{R}}\mathbb{C}$$의 $$\mathbb{C}$$-기저이기도 하다. 임의의 $$x\in\mathfrak{g}_0$$에 대하여 $$\ad x$$가 $$\mathfrak{g}_0$$를 보존하므로, 이 기저에서 $$\mathfrak{g}_0$$ 위의 $$\ad_{\mathfrak{g}_0}x$$를 나타내는 실행렬과 $$\mathfrak{g}$$ 위의 $$\ad_{\mathfrak{g}}x$$를 나타내는 복소행렬은 같은 (실)행렬이다. 따라서 임의의 $$x,y\in\mathfrak{g}_0$$에 대하여 $$\ad_{\mathfrak{g}}x\,\ad_{\mathfrak{g}}y$$를 나타내는 행렬은 $$\ad_{\mathfrak{g}_0}x\,\ad_{\mathfrak{g}_0}y$$의 행렬과 같고, 그 trace도 같으므로 $$\kappa(x,y)=\kappa_0(x,y)$$이다. $$\kappa$$가 $$\mathbb{C}$$-bilinear이므로 이 등식이 $$\mathfrak{g}_0$$ 위에서의 일치로부터 $$\mathfrak{g}$$ 전체로 유일하게 확장됨이 따른다.

</details>

이 명제는 real form의 Killing form을 복소 대수의 Killing form으로부터 직접 읽을 수 있게 해 준다. 특히 $$\mathfrak{g}$$가 semisimple, 곧 $$\kappa$$가 nondegenerate이면 ([§Killing 형식과 Cartan 판정법, ⁋정리 9](/ko/math/lie_theory/killing_form_and_cartan_criterion#thm9)), 제한 $$\kappa_0$$ 역시 nondegenerate이므로 모든 real form $$\mathfrak{g}_0$$도 semisimple이다. 그러나 nondegenerate인 실대칭 bilinear form은 signature를 가지므로, 서로 다른 real form들은 $$\kappa_0$$의 signature로 구별된다. 다음 절에서 다루는 compact real form은 이 signature가 가장 한쪽으로 치우친 경우, 곧 $$\kappa_0$$가 음의 정부호인 경우이다.

## Compact real form

Real form의 이름에 붙은 "compact"는 그 real form에 대응하는 연결 단순연결 Lie group이 compact라는 데에서 온다. 이 군론적 조건이 Lie algebra 차원에서는 Killing form의 부호로 정확히 번역되며, 우리는 후자를 정의로 삼는다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> 복소 semisimple Lie algebra $$\mathfrak{g}$$의 real form $$\mathfrak{u}$$가 *compact real form<sub>콤팩트 실형식</sub>*이라는 것은 $$\mathfrak{u}$$의 Killing form $$\kappa_{\mathfrak{u}}$$가 음의 정부호, 곧 모든 $$0\neq x\in\mathfrak{u}$$에 대하여 $$\kappa_{\mathfrak{u}}(x,x)<0$$인 것이다.

</div>

음의 정부호인 Killing form은 그 자체로 nondegenerate이므로, compact real form $$\mathfrak{u}$$는 [§Killing 형식과 Cartan 판정법, ⁋정리 9](/ko/math/lie_theory/killing_form_and_cartan_criterion#thm9)에 의해 semisimple이다. 이 정의가 "compact"라는 이름을 정당화하는 까닭은 다음과 같다. $$\mathfrak{u}$$의 연결 단순연결 Lie group을 $$U$$라 하면 ([§리 군, ⁋정리 15](/ko/math/lie_theory/Lie_groups#thm15)), $$-\kappa_{\mathfrak{u}}$$는 $$\mathfrak{u}$$ 위의 양의 정부호 inner product이고 Killing form이 $$\Aut(\mathfrak{u})$$-불변이므로 ([§Killing 형식과 Cartan 판정법, ⁋명제 3](/ko/math/lie_theory/killing_form_and_cartan_criterion#prop3)) $$\Ad(U)$$-불변이다. 따라서 $$\Ad:U\rightarrow\GL(\mathfrak{u})$$의 상은 직교군 $$\mathrm{O}(\mathfrak{u},-\kappa_{\mathfrak{u}})$$ 안에 들어가는 closed subgroup이고, 이는 compact이다. semisimple의 경우 $$\ker\Ad=Z(U)$$가 이산이고 유한하므로 $$U$$ 자신도 compact가 된다. 우리는 이 군론적 사실을 동기로만 사용하고, 이후의 논증은 Killing form의 부호 조건만으로 진행한다.

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> $$\su(n)$$은 trace가 $$0$$인 skew-Hermitian 복소행렬들의 실 Lie algebra, 곧

$$\su(n)=\{X\in\Mat_n(\mathbb{C})\mid X^\ast=-X,\ \tr X=0\}$$

이다 (여기에서 $$X^\ast=\bar X^{\mathsf T}$$는 conjugate transpose이다). 이는 $$\mathbb{R}$$ 위의 Lie algebra이며 $$\su(n)$$에 $$i$$를 곱하면 trace가 $$0$$인 Hermitian 행렬을 얻으므로, 실 벡터공간으로서

$$\su(n)\oplus i\,\su(n)=\{X\in\Mat_n(\mathbb{C})\mid\tr X=0\}=\sl(n;\mathbb{C})$$

이다. 따라서 $$\su(n)$$은 $$\sl(n;\mathbb{C})$$의 real form이다. $$\su(n)$$ 위의 Killing form은 $$\kappa(X,Y)=2n\tr(XY)$$로 계산되며, $$X\in\su(n)$$이 $$0$$이 아니면 $$\tr(X^2)=-\tr(X^\ast X)=-\sum_{i,j}\lvert X_{ij}\rvert^2<0$$이므로 $$\kappa$$가 음의 정부호이다. 곧 $$\su(n)$$은 $$\sl(n;\mathbb{C})$$의 compact real form이고, 대응하는 군 $$\SU(n)$$은 compact이다.

</div>

같은 방식으로 다른 고전적 compact 군의 Lie algebra가 그 복소화의 compact real form이 된다. 실 skew-symmetric 행렬들의 대수 $$\so(n)=\{X\in\Mat_n(\mathbb{R})\mid X^{\mathsf T}=-X\}$$은 복소화하면 복소 skew-symmetric 행렬들의 대수 $$\so(n;\mathbb{C})$$가 되어 $$\so(n)$$이 그 real form이고, $$\kappa(X,Y)=(n-2)\tr(XY)$$ ($$n\geq 3$$)이 음의 정부호이므로 $$\so(n)$$은 compact real form이다. 사원수 위의 unitary 군의 Lie algebra인 compact symplectic 대수 $$\sp(n)=\{X\in\Mat_n(\mathbb{H})\mid X^\ast=-X\}$$ 역시 $$\sp(2n;\mathbb{C})$$의 compact real form이며, 대응하는 군 $$\mathrm{Sp}(n)$$이 compact이다. 이들은 모두 어떤 양의 정부호 Hermitian (또는 그 실·사원수 판본) 형식을 보존하는 군의 Lie algebra이고, 그 보존 조건이 곧 $$X^\ast=-X$$로 나타나 Killing form의 음의 정부호성을 보장한다.

## 존재성

이제 임의의 복소 semisimple Lie algebra가 compact real form을 가짐을 증명한다. 핵심은 root decomposition의 root vector들을 적절히 정규화하여 구조상수를 실수, 나아가 부호까지 통제된 형태로 만든 다음, 그로부터 명시적으로 음의 정부호 real form을 적는 것이다. 먼저 root decomposition을 이용해 좋은 기저를 마련한다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> $$\mathfrak{g}$$가 복소 semisimple Lie algebra, $$\mathfrak{h}$$가 Cartan subalgebra, $$\mathfrak{g}=\mathfrak{h}\oplus\bigoplus_{\alpha\in\Phi}\mathfrak{g}_\alpha$$가 그 root decomposition이라 하자 ([§근계, ⁋명제 6](/ko/math/lie_theory/root_systems#prop6)). 그럼 각 root $$\alpha\in\Phi$$마다 root vector $$e_\alpha\in\mathfrak{g}_\alpha$$와 원소 $$h_\alpha\in\mathfrak{h}$$를 다음을 만족하도록 택할 수 있다.

1. $$[h_\alpha,e_\beta]=\langle\beta,\alpha^\vee\rangle e_\beta$$이고 $$[e_\alpha,e_{-\alpha}]=h_\alpha$$이며 $$[h_\alpha,e_{\pm\alpha}]=\pm2 e_{\pm\alpha}$$이다.
2. $$\alpha+\beta\in\Phi$$일 때 $$[e_\alpha,e_\beta]=N_{\alpha,\beta}e_{\alpha+\beta}$$로 두면 구조상수 $$N_{\alpha,\beta}$$는 모두 실수이고 $$N_{\alpha,\beta}=-N_{-\alpha,-\beta}$$를 만족한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

각 $$\alpha\in\Phi$$에 대하여 $$\mathfrak{g}_\alpha$$는 $$1$$차원이고 ([§근계, ⁋명제 6](/ko/math/lie_theory/root_systems#prop6) 이후의 $$\sl_2$$ 분석), Killing form은 $$\mathfrak{g}_\alpha\times\mathfrak{g}_{-\alpha}$$ 위에서 nondegenerate pairing을 준다 ([§근계, ⁋명제 6](/ko/math/lie_theory/root_systems#prop6)의 3). 표준적인 $$\sl_2$$-삼중항 정규화에 따라, 각 $$\alpha$$에 대하여 $$\mathbb{C}e_\alpha\oplus\mathbb{C}h_\alpha\oplus\mathbb{C}e_{-\alpha}\cong\sl(2;\mathbb{C})$$가 $$[h_\alpha,e_{\pm\alpha}]=\pm2 e_{\pm\alpha}$$, $$[e_\alpha,e_{-\alpha}]=h_\alpha$$를 만족하도록 $$e_{\pm\alpha}$$를 정규화할 수 있으며, 이때 $$h_\alpha$$는 coroot $$\alpha^\vee$$에 대응하여 $$[h_\alpha,e_\beta]=\langle\beta,\alpha^\vee\rangle e_\beta$$가 성립한다.

이러한 정규화는 각 root pair $$\{\alpha,-\alpha\}$$에서 $$e_\alpha$$를 $$0$$이 아닌 스칼라배로 바꿀 자유를 남기며, 그에 따라 $$e_{-\alpha}$$는 $$[e_\alpha,e_{-\alpha}]=h_\alpha$$를 유지하도록 역수배로 조정된다. Chevalley는 이 자유를 이용해 모든 $$N_{\alpha,\beta}$$가 정수가 되도록 기저를 택할 수 있음을 보였고 (Chevalley basis), 특히 $$N_{\alpha,\beta}$$는 실수이다. 같은 구성에서 $$N_{\alpha,\beta}=-N_{-\alpha,-\beta}$$가 성립함은 $$x\mapsto -x$$로 주어지는 자기동형 아래 $$e_\alpha\mapsto -e_{-\alpha}$$가 bracket을 보존하도록 부호를 맞출 수 있다는 데에서 따른다. 우리에게 필요한 것은 모든 $$N_{\alpha,\beta}$$가 실수이고 이 부호 관계를 만족한다는 사실뿐이다.

</details>

위 명제의 기저를 *Chevalley basis<sub>슈발레 기저</sub>*라 부른다. 이제 이 기저로부터 compact real form을 직접 적는다.

<div class="proposition" markdown="1">

<ins id="thm7">**정리 7**</ins> $$\mathfrak{g}$$가 복소 semisimple Lie algebra이고 [명제 6](#prop6)의 Chevalley basis $$\{h_\alpha\}\cup\{e_\alpha\}_{\alpha\in\Phi}$$가 주어졌다 하자. 그럼 실 부분공간

$$\mathfrak{u}=\span_{\mathbb{R}}\bigl(\{i h_\alpha\mid\alpha\in\Phi^+\}\cup\{e_\alpha-e_{-\alpha}\mid\alpha\in\Phi^+\}\cup\{i(e_\alpha+e_{-\alpha})\mid\alpha\in\Phi^+\}\bigr)$$

은 $$\mathfrak{g}$$의 compact real form이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

먼저 $$\mathfrak{u}$$가 $$\mathfrak{g}$$의 real form임을 보인다. $$\Phi^+$$를 positive root들의 모임이라 하면 ([§근계, ⁋정의 15](/ko/math/lie_theory/root_systems#def15)) $$\{h_\alpha\mid\alpha\in\Phi^+\}$$가 $$\mathfrak{h}$$의 (실은 복소) 기저를 이루도록 simple root들에 대응하는 $$h$$들을 택할 수 있고, $$\{e_\alpha\}_{\alpha\in\Phi}$$가 root space들의 기저이므로, 위 세 묶음의 원소들은 $$\mathfrak{g}$$의 $$\mathbb{R}$$-기저를 이룬다. 실제로 $$ih_\alpha$$, $$e_\alpha-e_{-\alpha}$$, $$i(e_\alpha+e_{-\alpha})$$ 및 그 $$i$$배인 $$h_\alpha$$, $$i(e_\alpha-e_{-\alpha})$$, $$-(e_\alpha+e_{-\alpha})$$를 합치면 $$\{h_\alpha,e_\alpha,e_{-\alpha}\}$$ 전체를 $$\mathbb{C}$$-생성하므로, $$\mathfrak{u}\oplus i\mathfrak{u}=\mathfrak{g}$$이고 $$\dim_{\mathbb{R}}\mathfrak{u}=\dim_{\mathbb{C}}\mathfrak{g}$$이다.

$$\mathfrak{u}$$가 bracket에 대해 닫혀 있음을 확인한다. 이는 conjugation $$\tau$$를 통해 깔끔하게 처리된다. $$\mathfrak{g}$$ 위의 conjugate-linear 사상 $$\tau$$를 기저 위에서

$$\tau(h_\alpha)=-h_\alpha,\qquad \tau(e_\alpha)=-e_{-\alpha}$$

로 정의하고 conjugate-linear하게 확장하자. $$\tau$$가 bracket을 보존함을 모든 기저쌍에서 확인하면 된다. $$[h_\alpha,e_\beta]=\langle\beta,\alpha^\vee\rangle e_\beta$$에 대해

$$\tau[h_\alpha,e_\beta]=\langle\beta,\alpha^\vee\rangle\,\tau(e_\beta)=-\langle\beta,\alpha^\vee\rangle e_{-\beta}$$

이고, 한편 $$\langle-\beta,\alpha^\vee\rangle=-\langle\beta,\alpha^\vee\rangle$$이므로

$$[\tau h_\alpha,\tau e_\beta]=[-h_\alpha,-e_{-\beta}]=[h_\alpha,e_{-\beta}]=\langle-\beta,\alpha^\vee\rangle e_{-\beta}=-\langle\beta,\alpha^\vee\rangle e_{-\beta}$$

이어서 둘이 같다. $$[e_\alpha,e_{-\alpha}]=h_\alpha$$에 대해서는 $$\tau[e_\alpha,e_{-\alpha}]=\tau(h_\alpha)=-h_\alpha$$이고 $$[\tau e_\alpha,\tau e_{-\alpha}]=[-e_{-\alpha},-e_\alpha]=[e_{-\alpha},e_\alpha]=-h_\alpha$$이다. 마지막으로 $$\alpha+\beta\in\Phi$$인 경우 $$\tau[e_\alpha,e_\beta]=N_{\alpha,\beta}\,\tau(e_{\alpha+\beta})=-N_{\alpha,\beta}e_{-\alpha-\beta}$$ ($$N_{\alpha,\beta}$$가 실수이므로 conjugate-linear 사상이 그대로 통과한다)이고, $$[\tau e_\alpha,\tau e_\beta]=[-e_{-\alpha},-e_{-\beta}]=[e_{-\alpha},e_{-\beta}]=N_{-\alpha,-\beta}e_{-\alpha-\beta}=-N_{\alpha,\beta}e_{-\alpha-\beta}$$이다 ([명제 6](#prop6)의 $$N_{\alpha,\beta}=-N_{-\alpha,-\beta}$$). 따라서 $$\tau$$는 conjugation이며, 그 고정점 집합 $$\mathfrak{g}^{\tau}$$는 real form이다.

이제 $$\mathfrak{u}=\mathfrak{g}^{\tau}$$임을 확인한다. $$\tau(ih_\alpha)=-i\,\tau(h_\alpha)=ih_\alpha$$, $$\tau(e_\alpha-e_{-\alpha})=-e_{-\alpha}+e_\alpha=e_\alpha-e_{-\alpha}$$, $$\tau(i(e_\alpha+e_{-\alpha}))=-i(-e_{-\alpha}-e_\alpha)=i(e_\alpha+e_{-\alpha})$$이므로 $$\mathfrak{u}$$의 생성원이 모두 $$\tau$$-고정이고, 차원이 같으므로 $$\mathfrak{u}=\mathfrak{g}^{\tau}$$이다.

마지막으로 $$\mathfrak{u}$$ 위에서 Killing form이 음의 정부호임을 보인다. $$\mathfrak{g}$$의 Killing form $$\kappa$$를 root decomposition에 대해 분석하면, $$\kappa$$는 $$\mathfrak{h}$$와 $$\bigoplus_\alpha\mathfrak{g}_\alpha$$를 직교시키고 $$\alpha+\beta\neq0$$인 $$\mathfrak{g}_\alpha,\mathfrak{g}_\beta$$를 직교시킨다 ([§근계, ⁋명제 6](/ko/math/lie_theory/root_systems#prop6)의 2). 위 정규화에서 $$\kappa(e_\alpha,e_{-\alpha})>0$$이고 $$\kappa(h_\alpha,h_\alpha)>0$$임이 $$\sl_2$$-삼중항의 표준 계산으로 따른다 (Killing form은 $$\mathfrak{h}$$ 위에서 root들이 주는 실 inner product의 양의 정부호 형식으로 제한된다). 이제 $$\mathfrak{u}$$의 생성원에서 $$\kappa$$를 계산하면

$$\kappa(ih_\alpha,ih_\alpha)=-\kappa(h_\alpha,h_\alpha)<0$$

이고, $$\kappa(e_\alpha,e_\beta)=0$$ ($$\alpha+\beta\neq0$$), $$\kappa(e_\alpha,e_\alpha)=0$$임을 써서

$$\begin{aligned}
\kappa(e_\alpha-e_{-\alpha},\,e_\alpha-e_{-\alpha})&=-2\kappa(e_\alpha,e_{-\alpha})<0,\\
\kappa(i(e_\alpha+e_{-\alpha}),\,i(e_\alpha+e_{-\alpha}))&=-2\kappa(e_\alpha,e_{-\alpha})<0
\end{aligned}$$

을 얻는다. 또 서로 다른 생성원들은 위 직교성에 의해 $$\kappa$$에 대해 직교하므로, $$\kappa$$는 $$\mathfrak{u}$$의 이 기저에서 음의 대각행렬로 표현된다. 따라서 $$\kappa_{\mathfrak{u}}$$는 음의 정부호이고 ([명제 3](#prop3)에 의해 $$\kappa_{\mathfrak{u}}$$는 $$\kappa$$의 제한이다), $$\mathfrak{u}$$는 compact real form이다.

</details>

이로써 모든 복소 semisimple Lie algebra가 적어도 하나의 compact real form을 가짐을 보였다. 구성에서 핵심은 두 가지였다. 첫째, $$\mathfrak{h}$$의 실 방향 $$h_\alpha$$에 $$i$$를 곱해 Killing form이 양의 정부호이던 방향을 음의 정부호로 뒤집은 것이고, 둘째, 각 root space 쌍 $$\mathfrak{g}_\alpha\oplus\mathfrak{g}_{-\alpha}$$에서 hyperbolic하게 분포하던 Killing form을 $$e_\alpha-e_{-\alpha}$$와 $$i(e_\alpha+e_{-\alpha})$$라는 두 실 방향으로 옮겨 둘 다 음으로 만든 것이다. 예시 5의 $$\su(n)$$이 정확히 이 구성의 $$\sl(n;\mathbb{C})$$에 대한 특수한 경우이다.

## 유일성

존재성에 이어 자연스러운 물음은 compact real form이 본질적으로 하나뿐인가 하는 것이다. 답은 $$\mathfrak{g}$$의 automorphism으로 옮겨 가는 것을 제외하면 그렇다는 것이며, 이는 두 compact real form에 대응하는 conjugation들이 서로 켤레라는 형태로 진술된다. 증명의 핵심 도구는 다음의 관찰이다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> $$\mathfrak{u}$$가 복소 semisimple Lie algebra $$\mathfrak{g}$$의 compact real form이고 $$\tau$$가 $$\mathfrak{u}$$에 대응하는 conjugation이면, 임의의 $$x\in\mathfrak{g}$$에 대하여

$$H_\tau(x,y)=-\kappa(x,\tau y)$$

는 $$\mathfrak{g}$$ 위의 양의 정부호 Hermitian form이다. 나아가 각 $$x\in\mathfrak{u}$$에 대하여 $$\ad x$$는 이 Hermitian form에 대해 skew-Hermitian이고, 각 $$x\in i\mathfrak{u}$$에 대하여 $$\ad x$$는 Hermitian이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\kappa$$가 $$\mathbb{C}$$-bilinear symmetric이고 $$\tau$$가 conjugate-linear이므로 $$H_\tau(x,y)=-\kappa(x,\tau y)$$는 첫 변수에 $$\mathbb{C}$$-선형, 둘째 변수에 conjugate-linear이다. Hermitian 대칭성 $$H_\tau(y,x)=\overline{H_\tau(x,y)}$$은 $$\tau$$가 $$\kappa$$의 양변에 작용할 때 $$\kappa(\tau x,\tau y)=\overline{\kappa(x,y)}$$임을 ($$\tau$$가 bracket을 보존하는 conjugate-linear 사상이라는 데에서) 써서 따른다. 양의 정부호성은 $$\mathfrak{g}=\mathfrak{u}\oplus i\mathfrak{u}$$로 분해하여 본다. $$x=u+iv$$ ($$u,v\in\mathfrak{u}$$)이면 $$\tau x=u-iv$$이므로

$$H_\tau(x,x)=-\kappa(u+iv,\,u-iv)=-\kappa(u,u)-\kappa(v,v)+i\bigl(\kappa(u,v)-\kappa(v,u)\bigr)$$

인데 $$\kappa$$가 symmetric이라 허수부가 사라지고, $$\kappa_{\mathfrak{u}}$$가 음의 정부호이므로 $$-\kappa(u,u)-\kappa(v,v)\geq0$$이며 $$x\neq0$$이면 $$u,v$$ 중 하나가 $$0$$이 아니어서 양수이다.

skew-Hermitian성은 $$\kappa$$의 invariance ([§Killing 형식과 Cartan 판정법, ⁋명제 2](/ko/math/lie_theory/killing_form_and_cartan_criterion#prop2))에서 따른다. $$x\in\mathfrak{u}$$이면 $$\tau x=x$$이고 $$\tau$$가 bracket을 보존하므로 $$\tau([x,y])=[x,\tau y]$$이다. 따라서

$$H_\tau([x,y],z)=-\kappa([x,y],\tau z)=-\kappa(y,[\,\tau z,x\,])=\kappa(y,[x,\tau z])=\kappa(y,\tau[x,z])=-H_\tau(y,[x,z])$$

이고, 이는 $$\ad x$$가 $$H_\tau$$에 대해 skew-Hermitian, 곧 $$(\ad x)^\ast=-\ad x$$임을 뜻한다. $$x\in i\mathfrak{u}$$이면 $$\tau x=-x$$이므로 같은 계산에서 부호가 한 번 더 뒤집혀 $$(\ad x)^\ast=\ad x$$, 곧 Hermitian이다.

</details>

이 명제는 compact real form이 $$\mathfrak{g}$$ 위에 $$\Ad(U)$$-불변 inner product를 제공한다는 위 동기를 Hermitian form의 형태로 정밀화한 것으로, 두 compact form의 conjugation $$\tau_1,\tau_2$$를 비교하는 표준 논법의 출발점이 된다. $$\theta=\tau_1\tau_2$$가 $$\mathfrak{g}$$의 automorphism이고 $$H_{\tau_1}$$에 대해 양의 정부호 자기수반 작용소가 되므로, 그 실 거듭제곱 $$\theta^t$$를 통해 $$\tau_2$$를 $$\tau_1$$로 연속적으로 옮기는 $$\mathfrak{g}$$의 automorphism을 만들 수 있다. 우리는 이 표준적 사실의 결론만을 정리로 기록한다.

<div class="proposition" markdown="1">

<ins id="thm9">**정리 9**</ins> 복소 semisimple Lie algebra $$\mathfrak{g}$$의 두 compact real form $$\mathfrak{u}_1,\mathfrak{u}_2$$에 대하여, $$\varphi(\mathfrak{u}_1)=\mathfrak{u}_2$$를 만족하는 automorphism $$\varphi\in\Aut(\mathfrak{g})$$가 존재한다. 특히 $$\mathfrak{u}_1$$과 $$\mathfrak{u}_2$$는 $$\mathbb{R}$$ 위의 Lie algebra로서 isomorphic하다. 곧 $$\mathfrak{g}$$의 compact real form은 동형을 제외하고 유일하다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\tau_1,\tau_2$$를 각각 $$\mathfrak{u}_1,\mathfrak{u}_2$$에 대응하는 conjugation이라 하고, $$H=H_{\tau_1}$$을 [명제 8](#prop8)의 양의 정부호 Hermitian form이라 하자. $$\theta=\tau_1\tau_2$$는 두 conjugate-linear involution의 합성이므로 $$\mathfrak{g}$$의 ($$\mathbb{C}$$-선형) automorphism이다. $$\theta$$가 $$H$$에 대해 양의 정부호 자기수반임을 보인다. $$\tau_1$$이 $$H$$에 대해 등거리적 conjugate-linear involution이라는 데에서 $$\tau_1^\ast=\tau_1$$ 꼴의 관계가 성립하고, $$\theta$$의 자기수반성은 $$N=\theta^\ast\theta$$가 양의 정부호 자기수반 automorphism임을 준다. 실제로는 $$\theta$$ 자신이 $$H$$에 대해 양의 정부호 자기수반이 되도록 $$\tau_1,\tau_2$$를 잡을 수 있으며, 이는 표준적 계산이다.

$$\theta$$가 양의 정부호 자기수반 automorphism이므로, 스펙트럼 분해를 통해 실수 $$t$$에 대한 거듭제곱 $$\theta^t$$가 잘 정의되고 각 $$\theta^t$$ 역시 $$\mathfrak{g}$$의 automorphism이다 ($$\theta$$가 automorphism이고 그 고유공간 분해가 bracket과 호환되기 때문이다). $$\varphi=\theta^{-1/2}$$로 두면, $$\theta\tau_1=\tau_1\theta^{-1}$$ (따라서 실수 거듭제곱에 대해 $$\theta^t\tau_1=\tau_1\theta^{-t}$$) 이라는 관계로부터 $$\varphi\tau_1\varphi^{-1}=\theta^{-1/2}\tau_1\theta^{1/2}=\tau_1\theta=\tau_2$$임이 따른다 ($$\theta=\tau_1\tau_2$$에서 $$\tau_1\theta=\tau_2$$이므로). conjugation을 옮기는 automorphism은 그 고정점 집합인 real form을 옮기므로

$$\varphi(\mathfrak{u}_1)=\varphi(\mathfrak{g}^{\tau_1})=\mathfrak{g}^{\varphi\tau_1\varphi^{-1}}=\mathfrak{g}^{\tau_2}=\mathfrak{u}_2$$

이다. $$\varphi$$가 automorphism이므로 그 제한 $$\varphi\vert_{\mathfrak{u}_1}:\mathfrak{u}_1\rightarrow\mathfrak{u}_2$$는 실 Lie algebra isomorphism이고, 따라서 두 compact real form은 동형이다.

</details>

유일성은 compact real form을 복소 semisimple Lie algebra의 불변량으로 취급할 수 있게 한다. 곧 단순 복소 Lie algebra의 분류 ([§근계, ⁋정의 16](/ko/math/lie_theory/root_systems#def16)의 Cartan matrix에 의한)는 단순 compact Lie algebra, 나아가 단순연결 단순 compact Lie group의 분류와 일대일로 대응한다. $$A_n,B_n,C_n,D_n$$ 계열에 대응하는 compact form이 각각 $$\su(n+1),\so(2n+1),\sp(n),\so(2n)$$이라는 사실이 그 가장 직접적인 형태이다.

## Weyl의 unitarian trick

Compact real form의 존재성과 유일성이 주는 가장 중요한 응용 가운데 하나는 semisimple Lie algebra의 완전가약성에 대한 군론적 증명이다. Compact 군의 표현은 invariant inner product를 평균내는 단순한 논법으로 완전가약임이 보이는데, compact real form은 임의의 복소 semisimple Lie algebra를 이 compact 세계로 옮기는 다리를 놓아 준다. 먼저 compact 군 쪽의 평균화 논법을 정리한다.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> $$U$$가 compact Lie group이고 $$\rho:U\rightarrow\GL(V)$$가 유한차원 복소 표현이면, $$\rho$$는 완전가약이다. 곧 $$V$$는 기약 부분표현들의 직합으로 분해된다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\langle-,-\rangle_0$$을 $$V$$ 위의 임의의 Hermitian inner product라 하고, compact 군 $$U$$ 위의 정규화된 Haar measure $$du$$ ($$\int_U du=1$$)에 대하여

$$\langle v,w\rangle=\int_U\langle\rho(u)v,\rho(u)w\rangle_0\,du$$

로 평균낸 form을 정의한다. compactness가 이 적분의 수렴과 $$du$$의 존재를 보장하며, 적분 안의 각 피적분 함수가 양의 정부호 Hermitian form이므로 $$\langle-,-\rangle$$도 양의 정부호 Hermitian form이다. Haar measure의 좌불변성에서 임의의 $$g\in U$$에 대하여

$$\langle\rho(g)v,\rho(g)w\rangle=\int_U\langle\rho(ug)v,\rho(ug)w\rangle_0\,du=\langle v,w\rangle$$

이므로 $$\langle-,-\rangle$$은 $$U$$-불변이다. 이제 $$W\subseteq V$$가 부분표현이면 그 직교여공간 $$W^\perp$$ 역시 부분표현이다. 임의의 $$w\in W$$, $$x\in W^\perp$$, $$g\in U$$에 대하여 $$\langle w,\rho(g)x\rangle=\langle\rho(g^{-1})w,x\rangle=0$$이고 ($$\rho(g^{-1})w\in W$$), 따라서 $$\rho(g)x\in W^\perp$$이기 때문이다. 그럼 $$V=W\oplus W^\perp$$가 표현의 직합 분해이고, $$\dim V$$에 대한 귀납법으로 $$V$$가 기약 부분표현들의 직합임이 따른다.

</details>

이 논법은 적분 가능한 군, 곧 compact 군에서만 직접 통한다. $$\SL(n;\mathbb{C})$$ 같은 noncompact 군이나 추상 semisimple Lie algebra에는 평균낼 측도가 없으므로 그대로 적용되지 않는다 ([§근계](/ko/math/lie_theory/root_systems)의 $$\sl_2$$ 논의에서 지적한 바와 같다). Weyl의 착상은 표현을 일단 compact real form $$\mathfrak{u}$$에 대응하는 compact 군 $$U$$의 표현으로 끌어내려 거기에서 완전가약성을 얻은 뒤, 그 분해가 원래의 복소 Lie algebra 표현의 분해이기도 함을 복소화로 되돌려 받는 것이다.

<div class="proposition" markdown="1">

<ins id="thm11">**정리 11 (Weyl의 unitarian trick)**</ins> $$\mathfrak{g}$$가 복소 semisimple Lie algebra이면 $$\mathfrak{g}$$의 모든 유한차원 표현은 완전가약이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\rho:\mathfrak{g}\rightarrow\gl(V)$$를 유한차원 복소 표현이라 하자. [정리 7](#thm7)에 의해 $$\mathfrak{g}$$는 compact real form $$\mathfrak{u}$$를 가지며, $$\mathfrak{g}=\mathfrak{u}\oplus i\mathfrak{u}$$이다. $$\mathfrak{u}$$의 연결 단순연결 Lie group을 $$U$$라 하면 ([§리 군, ⁋정리 15](/ko/math/lie_theory/Lie_groups#thm15)), $$\mathfrak{u}$$가 compact real form이라는 데에서 $$U$$는 compact이다 ([정의 4](#def4) 이후의 논의).

$$\rho$$를 $$\mathfrak{u}\subseteq\mathfrak{g}$$로 제한하면 실 Lie algebra 표현 $$\rho\vert_{\mathfrak{u}}:\mathfrak{u}\rightarrow\gl(V)$$를 얻고, $$U$$가 단순연결이므로 이는 군 표현 $$\widetilde\rho:U\rightarrow\GL(V)$$로 적분된다 ([§리 군, ⁋정리 15](/ko/math/lie_theory/Lie_groups#thm15)의 1). $$U$$가 compact이므로 [명제 10](#prop10)에 의해 $$\widetilde\rho$$는 완전가약이고, $$V=\bigoplus_j W_j$$로 $$U$$-기약 부분표현들의 직합으로 분해된다.

이제 각 $$W_j$$가 $$\mathfrak{g}$$-부분표현임을 본다. $$W_j$$가 $$U$$-불변이므로 $$\widetilde\rho$$를 미분한 $$\rho\vert_{\mathfrak{u}}$$ 아래 $$\mathfrak{u}$$-불변, 곧 모든 $$x\in\mathfrak{u}$$에 대하여 $$\rho(x)W_j\subseteq W_j$$이다. 임의의 $$z\in\mathfrak{g}$$는 $$z=x+iy$$ ($$x,y\in\mathfrak{u}$$) 꼴이고 $$\rho$$가 $$\mathbb{C}$$-선형이므로 $$\rho(z)=\rho(x)+i\rho(y)$$가 $$W_j$$를 보존한다. 따라서 각 $$W_j$$는 $$\mathfrak{g}$$-부분표현이다.

마지막으로 각 $$W_j$$가 $$\mathfrak{g}$$-기약임을 본다. $$W_j$$가 $$0$$이 아닌 $$\mathfrak{g}$$-부분표현 $$W'\subsetneq W_j$$를 가진다면, 위와 같은 이유로 $$W'$$는 $$\mathfrak{u}$$-불변이고 따라서 ($$U$$가 연결이므로) $$U$$-불변인 진부분표현이 되어 $$W_j$$의 $$U$$-기약성에 모순이다. 그러므로 $$V=\bigoplus_j W_j$$는 $$\mathfrak{g}$$-기약 부분표현들의 직합이고, $$\rho$$는 완전가약이다.

</details>

이로써 Weyl 완전가약성 정리 ([§Weyl 완전가약성 정리, ⁋정리 7](/ko/math/lie_theory/weyl_complete_reducibility#thm7))를 Casimir element를 통한 순수 대수적 증명과는 독립적으로, compact 군의 평균화 논법으로 다시 얻었다. 두 증명은 같은 결론에 이르지만 강조점이 다르다. Casimir element를 쓰는 증명은 표수 $$0$$의 임의의 대수적으로 닫힌 체 위에서 작동하는 반면, unitarian trick은 $$\mathbb{C}$$ 위에서 compact 군의 위상적·해석적 성질에 의존한다. Weyl의 원래 동기는 후자였으며, compact real form은 복소 semisimple Lie algebra의 표현론과 compact Lie group의 표현론을 잇는 핵심 고리로 남는다.

---

**참고문헌**

**[Kna]** A. W. Knapp, *Lie groups beyond an introduction*, 2nd ed., Progress in Mathematics, Birkhäuser, 2002.  
**[Hum]** J. E. Humphreys, *Introduction to Lie algebras and representation theory*, Graduate Texts in Mathematics, Springer, 1972.  
**[Hel]** S. Helgason, *Differential geometry, Lie groups, and symmetric spaces*, Academic Press, 1978.  
