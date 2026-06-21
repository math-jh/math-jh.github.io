---
title: "Weyl 지표 공식"
description: "유한차원 표현의 weight 중복도를 group ring Z[P]의 원소로 묶은 형식 지표를 도입하고, Verma module의 형식 지표 e^μ/∏(1−e^{−α})로부터 dominant integral λ에 대한 기약 표현 L(λ)의 지표가 교대합 ∑_w(−1)^{ℓ(w)}e^{w(λ+ρ)}를 Weyl denominator로 나눈 것임을 보이는 Weyl 지표 공식을 확립한다. 그 따름으로 차원 공식 dim L(λ)=∏_{α>0}⟨λ+ρ,α⟩/⟨ρ,α⟩을 얻고 sl₂·sl₃에서 검산한다."
excerpt: "formal character, group ring Z[P], Verma module의 지표, Weyl denominator, Weyl vector ρ, Weyl 지표 공식, Weyl 차원 공식, sl₂, sl₃"

categories: [Math / Lie Theory]
permalink: /ko/math/lie_theory/weyl_character_formula
sidebar: 
    nav: "lie_theory-ko"

date: 2026-06-21
weight: 7.4

published: false
---

최고 무게 정리는 유한차원 기약 표현이 정확히 dominant integral weight $$\lambda$$에 대한 $$L(\lambda)$$들로 분류됨을 확립하였고, 이로써 표현론의 모든 질문은 각 $$L(\lambda)$$의 weight 구조, 곧 어떤 weight $$\mu$$가 어떤 multiplicity로 나타나는지를 계산하는 문제로 환원되었다 ([§최고 무게 가군, ⁋정리 12](/ko/math/lie_theory/highest_weight_modules#thm12)). $$\sl_2$$에서 이 정보는 단순하였다. highest weight $$m$$의 기약 표현은 $$m, m-2, \ldots, -m$$의 weight를 각각 중복도 $$1$$로 가졌다 ([§sl₂의 표현론, ⁋정의 5](/ko/math/lie_theory/representations_of_sl2#def5)). 그러나 rank가 큰 semisimple Lie algebra에서는 weight 중복도가 더 이상 자명하지 않으며, 이를 닫힌 형태로 주는 것이 Weyl 지표 공식이다.

이 글에서 우리는 표현 $$V$$의 모든 weight 중복도를 한꺼번에 담는 *형식 지표*를 weight lattice의 group ring 안의 원소로 정의하고, Verma module $$M(\mu)$$의 형식 지표가 $$e^\mu/\prod_{\alpha>0}(1-e^{-\alpha})$$라는 명료한 닫힌 형태를 가짐을 본다. 그런 뒤 Casimir 원소가 정하는 central character를 이용하여 $$\mathrm{ch}\,L(\lambda)$$를 Verma module 지표들의 교대합으로 풀고, 이를 정리하면 dominant integral $$\lambda$$에 대하여

$$\mathrm{ch}\,L(\lambda)=\frac{\sum_{w\in W}(-1)^{\ell(w)}e^{w(\lambda+\rho)}}{\sum_{w\in W}(-1)^{\ell(w)}e^{w\rho}}$$

라는 Weyl 지표 공식을 얻는다. 그 직접적 귀결로 차원 공식이 따라오며, $$\sl_2$$와 $$\sl_3$$에서 두 공식을 검산한다. 이 글 전체에서 $$\mathfrak{g}$$는 대수적으로 닫힌 표수 $$0$$의 체 (편의상 $$\mathbb{C}$$) 위의 유한차원 semisimple Lie algebra이고, $$\mathfrak{h}$$는 그 Cartan subalgebra, $$\Phi\subseteq\mathfrak{h}^\ast$$는 root system, $$\Phi^+$$는 고정된 positive root들의 모임, $$W$$는 그 Weyl group이다 ([§근계, ⁋정의 17](/ko/math/lie_theory/root_systems#def17)).

## 형식 지표

표현 $$V$$의 weight 중복도 전체를 하나의 대수적 대상으로 묶기 위해, weight들이 사는 격자의 group ring을 도입한다. 우선 무대가 될 격자를 정한다. weight $$\lambda\in\mathfrak{h}^\ast$$이 모든 simple coroot $$h_i$$ 위에서 정숫값 $$\lambda(h_i)\in\mathbb{Z}$$을 가질 때 이를 integral weight이라 부르며, 그러한 weight들의 모임

$$P=\{\lambda\in\mathfrak{h}^\ast\mid\lambda(h_i)\in\mathbb{Z}\ \text{ for all simple roots }\alpha_i\}$$

은 $$\mathfrak{h}^\ast$$ 안의 격자를 이룬다. 유한차원 표현의 모든 weight는 각 $$\sl_{2,\alpha_i}$$-방향에서 정수 고윳값을 가지므로 ([§최고 무게 가군, ⁋정리 12](/ko/math/lie_theory/highest_weight_modules#thm12)의 증명) $$P$$ 안에 놓이고, 따라서 $$P$$가 형식 지표의 자연스러운 무대가 된다. 이 격자 위에 군환을 얹는다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> weight lattice $$P$$의 *group ring<sub>군환</sub>* $$\mathbb{Z}[P]$$는 형식기호 $$\{e^\mu\mid\mu\in P\}$$를 $$\mathbb{Z}$$-기저로 갖는 자유가군이며, 곱셈을

$$e^\mu\cdot e^\nu=e^{\mu+\nu},\qquad e^0=1$$

로 정한 가환환이다. 곧 $$\mathbb{Z}[P]$$의 일반적인 원소는 유한합 $$\sum_\mu c_\mu e^\mu$$ ($$c_\mu\in\mathbb{Z}$$, 유한 개를 빼고 $$c_\mu=0$$)이다.

</div>

기호 $$e^\mu$$는 단지 격자 원소 $$\mu$$를 곱셈군의 원소로 옮긴 형식적 지수일 뿐이며, $$\mathbb{Z}[P]$$는 추상적으로 Laurent 다항식환 $$\mathbb{Z}[x_1^{\pm 1},\ldots,x_l^{\pm 1}]$$과 동형이다. 여기에서 $$x_i=e^{\varpi_i}$$는 격자 $$P$$의 기저, 곧 fundamental weight들에 대응한다. Weyl group $$W$$는 $$\mathfrak{h}^\ast$$ 위에 작용하고 $$P$$를 보존하므로 $$w\cdot e^\mu=e^{w\mu}$$로 $$\mathbb{Z}[P]$$ 위에 환 자기동형으로 작용한다. 이 $$W$$-작용이 지표 공식의 분자와 분모를 떠받치는 대칭이다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 유한차원 표현 $$V$$의 weight 분해 $$V=\bigoplus_{\mu}V_\mu$$에 대하여, $$V$$의 *formal character<sub>형식 지표</sub>*는 $$\mathbb{Z}[P]$$의 원소

$$\mathrm{ch}\,V=\sum_{\mu\in P}(\dim V_\mu)\,e^\mu$$

이다. 곧 각 weight space의 차원을 그 weight의 형식기호에 계수로 단 것이다.

</div>

형식 지표는 $$V$$의 weight들과 그 중복도를 빠짐없이 기록하므로, $$\mathrm{ch}\,V$$를 안다는 것은 $$V$$의 weight 구조 전부를 안다는 것과 같다. 두 표현의 직합과 텐서곱에 대하여 형식 지표는 환 연산과 정확히 맞물린다. weight space의 차원이 직합에서 더해지고 텐서곱에서 곱해지므로

$$\mathrm{ch}(V\oplus W)=\mathrm{ch}\,V+\mathrm{ch}\,W,\qquad\mathrm{ch}(V\otimes W)=\mathrm{ch}\,V\cdot\mathrm{ch}\,W$$

가 성립한다. 또한 유한차원 표현의 weight 집합은 Weyl group 작용에 대해 불변이고 중복도가 보존되므로 ([§최고 무게 가군, ⁋정리 12](/ko/math/lie_theory/highest_weight_modules#thm12)의 증명) $$\mathrm{ch}\,V$$는 $$W$$-불변, 곧 $$w\cdot\mathrm{ch}\,V=\mathrm{ch}\,V$$이다. 끝으로 $$e^0=1$$의 계수에 모든 weight space의 차원을 모으면 전체 차원을 읽을 수 있는데, 이는 모든 형식기호 $$e^\mu$$를 $$1$$로 평가하는 환 준동형 $$\varepsilon:\mathbb{Z}[P]\rightarrow\mathbb{Z}$$, $$e^\mu\mapsto 1$$을 통해

$$\varepsilon(\mathrm{ch}\,V)=\sum_\mu\dim V_\mu=\dim V$$

로 표현된다. 차원 공식은 바로 이 평가를 지표 공식에 적용하여 얻어질 것이다.

무한차원 표현에서는 weight 집합이 아래로만 유계여서 $$\mathrm{ch}\,V$$가 무한합이 되므로 $$\mathbb{Z}[P]$$에 머무르지 못한다. Verma module의 지표를 다루기 위해 약간 더 넓은 환이 필요하다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> $$\mathbb{Z}[P]$$의 *완비화<sub>completion</sub>* $$\widehat{\mathbb{Z}[P]}$$는 유한 개의 weight $$\lambda_1,\ldots,\lambda_r$$이 존재하여 그 support가 $$\bigcup_i(\lambda_i-Q^+)$$ 안에 들어가는 형식합 $$\sum_\mu c_\mu e^\mu$$들의 집합이다. 여기에서 $$Q^+=\sum_{\alpha\in\Phi^+}\mathbb{Z}_{\geq 0}\,\alpha$$는 positive root들의 음이 아닌 정수 결합으로 이루어진 cone이다.

</div>

이 support 조건 아래에서는 곱셈 $$\bigl(\sum_\mu c_\mu e^\mu\bigr)\bigl(\sum_\nu d_\nu e^\nu\bigr)=\sum_\xi\bigl(\sum_{\mu+\nu=\xi}c_\mu d_\nu\bigr)e^\xi$$의 각 계수가 유한합으로 잘 정의되므로 $$\widehat{\mathbb{Z}[P]}$$는 가환환이 되고 $$\mathbb{Z}[P]$$를 부분환으로 포함한다. weight가 highest weight $$\mu$$에서 positive root들을 빼서만 얻어지는 highest weight 가군의 형식 지표는 정확히 이 환 안에서 닫힌 형태를 갖는다.

## Verma module의 형식 지표

기약 표현의 지표를 직접 다루기는 어렵지만, 그것을 덮는 Verma module $$M(\mu)$$의 지표는 PBW 기저가 곧장 닫힌 형태로 내어준다. Verma module은 $$U(\mathfrak{n}^-)$$ 위의 자유가군이고 그 weight들이 $$\mu$$에서 positive root들을 빼서 얻어지므로 ([§최고 무게 가군, ⁋명제 7](/ko/math/lie_theory/highest_weight_modules#prop7)), 각 weight space의 차원은 순수한 조합론적 양이 된다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> 음이 아닌 정수에 값을 갖는 함수 $$\mathcal{P}:Q^+\rightarrow\mathbb{Z}_{\geq 0}$$을, $$\nu\in Q^+$$를 positive root들의 합 $$\nu=\sum_{\alpha\in\Phi^+}k_\alpha\alpha$$ ($$k_\alpha\in\mathbb{Z}_{\geq 0}$$)로 나타내는 방법의 수로 정의하고 이를 *Kostant partition function<sub>코스탄트 분할 함수</sub>*이라 부른다. $$\nu\notin Q^+$$이면 $$\mathcal{P}(\nu)=0$$으로 둔다.

</div>

$$\mathcal{P}(0)=1$$이며 (빈 합), 각 $$\nu$$에 대해 $$\mathcal{P}(\nu)$$는 유한하다. 이 함수가 Verma module의 weight 중복도를 정확히 센다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> 임의의 $$\mu\in\mathfrak{h}^\ast$$에 대하여 Verma module $$M(\mu)$$의 weight $$\mu-\nu$$의 weight space는 차원 $$\mathcal{P}(\nu)$$를 가지며, 따라서 그 형식 지표는 $$\widehat{\mathbb{Z}[P]}$$ 안에서

$$\mathrm{ch}\,M(\mu)=\frac{e^\mu}{\prod_{\alpha\in\Phi^+}(1-e^{-\alpha})}$$

이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\Phi^+=\{\beta_1,\ldots,\beta_N\}$$이라 하고 각 $$\beta_k$$에 대해 $$0\neq f_k\in\mathfrak{g}_{-\beta_k}$$를 택하면, 단항식들 $$f_1^{\,m_1}\cdots f_N^{\,m_N}\cdot v_\mu^+$$ ($$m_k\geq 0$$)는 $$M(\mu)$$의 $$\mathbb{C}$$-기저를 이루고 각각 weight $$\mu-\sum_k m_k\beta_k$$를 갖는다 ([§최고 무게 가군, ⁋명제 7](/ko/math/lie_theory/highest_weight_modules#prop7)). 따라서 고정된 $$\nu\in Q^+$$에 대하여 weight $$\mu-\nu$$의 weight space의 차원은 $$\sum_k m_k\beta_k=\nu$$를 만족하는 지수 $$(m_1,\ldots,m_N)$$의 개수, 곧 $$\nu$$를 positive root들의 음이 아닌 정수 결합으로 쓰는 방법의 수 $$\mathcal{P}(\nu)$$이다. $$\mu-\nu$$가 이 꼴이 아니면 weight space는 $$0$$이다. 그러므로

$$\mathrm{ch}\,M(\mu)=\sum_{\nu\in Q^+}\mathcal{P}(\nu)\,e^{\mu-\nu}=e^\mu\sum_{\nu\in Q^+}\mathcal{P}(\nu)\,e^{-\nu}$$

이다. 한편 각 positive root $$\alpha$$에 대해 형식 등비급수

$$\frac{1}{1-e^{-\alpha}}=\sum_{k\geq 0}e^{-k\alpha}$$

가 $$\widehat{\mathbb{Z}[P]}$$ 안에서 성립하므로, 이를 모든 $$\alpha\in\Phi^+$$에 대해 곱하면

$$\prod_{\alpha\in\Phi^+}\frac{1}{1-e^{-\alpha}}=\prod_{\alpha\in\Phi^+}\Bigl(\sum_{k_\alpha\geq 0}e^{-k_\alpha\alpha}\Bigr)=\sum_{(k_\alpha)}e^{-\sum_\alpha k_\alpha\alpha}=\sum_{\nu\in Q^+}\mathcal{P}(\nu)\,e^{-\nu}$$

이다. 마지막 등호는 $$\sum_\alpha k_\alpha\alpha=\nu$$를 주는 계수족 $$(k_\alpha)$$의 수가 정의상 $$\mathcal{P}(\nu)$$이기 때문이다. 두 식을 합치면 $$\mathrm{ch}\,M(\mu)=e^\mu\prod_{\alpha\in\Phi^+}(1-e^{-\alpha})^{-1}$$을 얻는다.

</details>

이 공식은 분모가 highest weight $$\mu$$에 의존하지 않는다는 점에서 본질적이다. 모든 Verma module이 같은 분모 $$\prod_{\alpha>0}(1-e^{-\alpha})$$를 공유하고 분자만이 $$e^\mu$$로 바뀌므로, 여러 Verma module 지표의 정수계수 결합은 그 공통 분모를 그대로 둔 채 분자 $$e^\mu$$들의 결합으로 계산된다. 이것이 다음 절에서 $$\mathrm{ch}\,L(\lambda)$$를 Verma 지표들의 교대합으로 풀 때 결정적으로 쓰인다.

분모를 대칭적으로 정리하기 위해 Weyl vector를 도입한다. 이는 $$\sl_2$$에서 highest weight를 절반씩 옮기던 $$\rho$$-이동의 일반화이다.

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> positive root들의 합의 절반

$$\rho=\frac{1}{2}\sum_{\alpha\in\Phi^+}\alpha$$

을 $$\mathfrak{g}$$의 *Weyl vector<sub>바일 벡터</sub>*라 부른다.

</div>

Weyl vector는 모든 simple coroot 위에서 $$\rho(h_i)=1$$을 만족하는 유일한 weight로도 특징지어지며, 따라서 $$P$$의 원소이고 strictly dominant하다. positive root 집합의 절반이라는 정의로부터 곧바로 분모를 $$\rho$$로 대칭화한 형태로 다시 쓸 수 있다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> *Weyl denominator<sub>바일 분모</sub>*

$$\Delta:=\prod_{\alpha\in\Phi^+}\bigl(e^{\alpha/2}-e^{-\alpha/2}\bigr)$$

에 대하여 다음이 성립한다.

$$\Delta=e^{\rho}\prod_{\alpha\in\Phi^+}\bigl(1-e^{-\alpha}\bigr)=\sum_{w\in W}(-1)^{\ell(w)}e^{w\rho}.$$

특히 Verma module의 지표는 $$\mathrm{ch}\,M(\mu)=e^{\mu+\rho}/\Delta$$로 쓸 수 있다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

첫 등호는 각 인자에서 $$e^{\alpha/2}$$를 묶어내면

$$e^{\alpha/2}-e^{-\alpha/2}=e^{\alpha/2}\bigl(1-e^{-\alpha}\bigr)$$

이고, 이를 모든 $$\alpha\in\Phi^+$$에 대해 곱하면 묶여 나온 인자들의 곱이 $$\prod_{\alpha\in\Phi^+}e^{\alpha/2}=e^{\frac12\sum_{\alpha>0}\alpha}=e^\rho$$이므로 따라온다. 이로써 $$\mathrm{ch}\,M(\mu)=e^\mu/\prod_{\alpha>0}(1-e^{-\alpha})=e^{\mu+\rho}/\Delta$$도 [명제 5](#prop5)에서 곧장 나온다.

둘째 등호를 본다. 먼저 $$\Delta$$가 Weyl group 작용에 대해 부호를 갖고 변함을 보인다. 곧 임의의 $$w\in W$$에 대하여 $$w\Delta=(-1)^{\ell(w)}\Delta$$이다. $$W$$가 simple reflection $$s_i$$들로 생성되고 $$\ell$$이 그 생성에 대해 가법적으로 작동하므로 ([§Bruhat decomposition, ⁋정의 3](/ko/math/lie_theory/bruhat_decomposition#def3)) $$w=s_i$$인 경우만 보이면 충분하다. simple reflection $$s_i$$는 positive root $$\alpha_i$$를 $$-\alpha_i$$로 보내고 나머지 positive root 전체를 자기들끼리 치환한다. 따라서 곱

$$s_i\Delta=\prod_{\alpha\in\Phi^+}\bigl(e^{s_i\alpha/2}-e^{-s_i\alpha/2}\bigr)$$

에서 $$\alpha=\alpha_i$$에 해당하는 인자만 $$e^{-\alpha_i/2}-e^{\alpha_i/2}=-(e^{\alpha_i/2}-e^{-\alpha_i/2})$$로 부호가 바뀌고 나머지 인자들은 순서만 뒤바뀌므로, $$s_i\Delta=-\Delta=(-1)^{\ell(s_i)}\Delta$$이다.

이제 $$\Delta$$를 전개한다. 각 인자에서 $$e^{\alpha/2}$$ 또는 $$-e^{-\alpha/2}$$를 고르는 모든 방식을 합하면, $$\Phi^+$$의 각 부분집합 $$S$$에 대해 부호 $$(-1)^{\lvert S\rvert}$$가 붙은 항 $$e^{\rho-\sum_{\alpha\in S}\alpha}$$가 나온다. 그중 $$S=\varnothing$$인 최고차 항은 $$e^\rho$$이며, 이는 dominant weight $$\rho$$에 대응하므로 $$\Delta$$에서 계수 $$+1$$의 항으로 단 한 번만 나타난다. $$\Delta$$가 $$w\Delta=(-1)^{\ell(w)}\Delta$$를 만족하므로, $$e^\rho$$의 $$W$$-궤도 위의 각 항 $$e^{w\rho}$$는 계수 $$(-1)^{\ell(w)}$$를 가져야 한다. $$\rho$$가 strictly dominant이고 정칙이므로 $$W$$는 $$\rho$$ 위에 자유롭게 작용하여 $$w\rho$$들은 서로 다른 $$\lvert W\rvert$$개의 weight이고, 이들 각각은 다시 $$\rho$$ 이하의 weight이다. 한편 $$\Delta$$의 모든 항 $$e^{\rho-\sum_{\alpha\in S}\alpha}$$의 weight는 $$\sum_{\alpha\in S}\alpha\geq 0$$만큼 $$\rho$$ 아래에 있고, $$\Delta$$가 반대칭이므로 $$W$$-정칙이 아닌 weight (어떤 reflection이 고정하는 weight)의 계수는 $$0$$이어야 한다. 정칙 weight들은 정확히 $$W$$-궤도 $$\{w\rho\}$$로 떨어지며 다른 정칙 궤도가 $$\rho$$ 이하에 더 나타나지 않음을 차수 비교로 확인하면, 남는 항은 $$\sum_{w\in W}(-1)^{\ell(w)}e^{w\rho}$$뿐이다.

</details>

따라서 highest weight $$\mu$$를 $$\mu+\rho$$로 옮긴 frame에서 모든 Verma module 지표는 공통 분모 $$\Delta=\sum_w(-1)^{\ell(w)}e^{w\rho}$$ 위의 분자 $$e^{\mu+\rho}$$ 하나로 적힌다. 이 $$\rho$$-이동된 좌표가 지표 공식을 깔끔한 교대합으로 만든다.

## Weyl 지표 공식

이제 기약 표현의 지표를 Verma module 지표들로 표현한다. 발상은 두 가지 사실을 결합하는 것이다. 첫째, 임의의 highest weight 가군은 Jordan–Hölder 인자가 모두 기약 highest weight 가군 $$L(\nu)$$들이므로, 형식 지표의 수준에서 $$\mathrm{ch}\,M(\mu)=\sum_\nu[M(\mu):L(\nu)]\,\mathrm{ch}\,L(\nu)$$이고, 이 관계는 $$\mathrm{ch}\,L(\lambda)$$를 $$\mathrm{ch}\,M(\mu)$$들의 정수계수 결합으로 거꾸로 푸는 것을 허용한다. 둘째, 그 결합에 어떤 $$M(\mu)$$가 실제로 들어올 수 있는지를 Casimir 원소의 central character가 강하게 제약한다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> $$\mathfrak{g}$$의 Casimir 원소 $$\Omega\in U(\mathfrak{g})$$는 Verma module $$M(\mu)$$ 위에서 스칼라 $$\langle\mu+\rho,\mu+\rho\rangle-\langle\rho,\rho\rangle$$로 작용한다. 여기에서 $$\langle-,-\rangle$$은 Killing form이 $$\mathfrak{h}^\ast$$ 위에 유도하는 $$W$$-불변 내적이다. 특히 두 weight $$\mu,\mu'$$에 대하여 $$M(\mu)$$와 $$M(\mu')$$ 위의 $$\Omega$$의 고윳값이 같을 필요충분조건은 $$\mu'+\rho$$가 $$\mu+\rho$$의 Weyl group 궤도 위에 놓이는 것이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\Omega$$는 $$U(\mathfrak{g})$$의 중심에 속하므로 ($$\sl_2$$의 경우가 [§보편 포락 대수, ⁋예시 12](/ko/math/lie_theory/universal_enveloping_algebra#ex12)) 각 weight space를 보존하며 highest weight 가군 위에서는 스칼라로 작용한다. $$\Omega$$를 삼각 분해 $$\mathfrak{g}=\mathfrak{n}^-\oplus\mathfrak{h}\oplus\mathfrak{n}^+$$에 맞춰 정렬하면

$$\Omega=\sum_i H_i^2+\text{(lower terms)}+2\sum_{\alpha\in\Phi^+}f_\alpha e_\alpha+(\mathfrak{h}\text{-part})$$

의 꼴로 쓰이는데, $$M(\mu)$$의 highest weight vector $$v_\mu^+$$에 작용시키면 $$\mathfrak{n}^+$$로 시작하는 항은 모두 $$v_\mu^+$$를 소멸시키고 ([§최고 무게 가군, ⁋정의 4](/ko/math/lie_theory/highest_weight_modules#def4)) $$\mathfrak{h}$$-부분만 남는다. 이를 정리하면 고윳값은 $$\langle\mu,\mu\rangle+2\langle\mu,\rho\rangle=\langle\mu+\rho,\mu+\rho\rangle-\langle\rho,\rho\rangle$$이 된다. $$\Omega$$가 스칼라로 작용하므로 $$M(\mu)$$ 전체에서 이 값이다.

두 고윳값이 같음은 $$\langle\mu+\rho,\mu+\rho\rangle=\langle\mu'+\rho,\mu'+\rho\rangle$$, 곧 $$\mu+\rho$$와 $$\mu'+\rho$$가 같은 길이를 가짐과 동치이다. $$W$$가 이 형식을 보존하므로, $$\mu'+\rho\in W(\mu+\rho)$$이면 두 central character가 같다. 우리가 사용하는 것은 이 함의이다. $$\mathrm{ch}\,L(\lambda)$$를 Verma 지표들의 정수계수 합으로 적을 때 나타나는 $$M(\mu)$$는 모두 $$L(\lambda)$$와 같은 central character를 가지면서 $$\mu\leq\lambda$$인 것들이며, [명제 5](#prop5)의 support 조건에 의해 그러한 $$\mu$$는 유한개이다.

</details>

이제 central character가 같은 Verma module만이 한 블록에 묶인다는 사실과 Verma 지표가 $$\widehat{\mathbb{Z}[P]}$$에서 가역 분모를 갖는다는 사실을 결합하여, 지표 공식을 끌어낸다.

<div class="proposition" markdown="1">

<ins id="thm9">**정리 9 (Weyl 지표 공식)**</ins> dominant integral weight $$\lambda$$에 대하여, 기약 표현 $$L(\lambda)$$의 형식 지표는

$$\mathrm{ch}\,L(\lambda)=\frac{\sum_{w\in W}(-1)^{\ell(w)}\,e^{w(\lambda+\rho)}}{\sum_{w\in W}(-1)^{\ell(w)}\,e^{w\rho}}=\frac{\sum_{w\in W}(-1)^{\ell(w)}\,e^{w(\lambda+\rho)}}{\prod_{\alpha\in\Phi^+}\bigl(e^{\alpha/2}-e^{-\alpha/2}\bigr)}$$

이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$M(\lambda)$$는 유한 길이의 가군이고 그 모든 composition factor는 highest weight $$\nu\leq\lambda$$인 기약 가군 $$L(\nu)$$이며 $$L(\lambda)$$가 중복도 $$1$$로 한 번 나타난다 ([§최고 무게 가군, ⁋명제 8](/ko/math/lie_theory/highest_weight_modules#prop8)). 형식 지표는 short exact sequence에 대해 가법적이므로

$$\mathrm{ch}\,M(\lambda)=\mathrm{ch}\,L(\lambda)+\sum_{\nu<\lambda}[M(\lambda):L(\nu)]\,\mathrm{ch}\,L(\nu)\tag{$\ast$}$$

이다. 여기에서 합에 등장하는 모든 $$L(\nu)$$는 $$M(\nu)$$의 몫이므로 $$M(\nu)$$와 같은 central character, 곧 $$\Omega$$의 같은 고윳값을 갖는다. $$L(\nu)$$가 $$M(\lambda)$$의 composition factor이려면 $$M(\nu)$$가 $$M(\lambda)$$와 같은 $$\Omega$$-고윳값을 가져야 하므로, [명제 8](#prop8)에 의하여 $$\nu+\rho\in W(\lambda+\rho)$$이다. 따라서 $$(\ast)$$에 실제로 기여하는 weight는 $$\nu+\rho=w(\lambda+\rho)$$ 꼴의 유한 개뿐이다.

같은 추론을 각 $$M(w(\lambda+\rho)-\rho)$$에 적용하면, 행렬 $$\bigl([M(\nu):L(\nu')]\bigr)$$이 이 유한한 weight 집합 위에서 단위 대각을 갖는 상삼각 행렬이 되어 가역이다. 그러므로 $$(\ast)$$를 거꾸로 풀면 정수계수 $$c_w$$들이 존재하여

$$\mathrm{ch}\,L(\lambda)=\sum_{w\in W}c_w\,\mathrm{ch}\,M\bigl(w(\lambda+\rho)-\rho\bigr),\qquad c_e=1$$

로 쓰인다. [명제 7](#prop7)에 의해 $$\mathrm{ch}\,M(w(\lambda+\rho)-\rho)=e^{w(\lambda+\rho)}/\Delta$$이므로

$$\Delta\cdot\mathrm{ch}\,L(\lambda)=\sum_{w\in W}c_w\,e^{w(\lambda+\rho)}\tag{$\ast\ast$}$$

이다. 좌변의 성질을 본다. $$\mathrm{ch}\,L(\lambda)$$는 $$W$$-불변이고 ([정의 2](#def2) 이후의 논의) $$\Delta$$는 $$w\Delta=(-1)^{\ell(w)}\Delta$$를 만족하므로 ([명제 7](#prop7)의 증명), 좌변 $$\Delta\cdot\mathrm{ch}\,L(\lambda)$$는 $$W$$-반대칭이다. 곧 임의의 $$w\in W$$에 대하여 $$w\bigl(\Delta\cdot\mathrm{ch}\,L(\lambda)\bigr)=(-1)^{\ell(w)}\Delta\cdot\mathrm{ch}\,L(\lambda)$$이다.

따라서 우변 $$(\ast\ast)$$도 $$W$$-반대칭이어야 하고, 이는 계수가 궤도 위에서 $$c_{ww'}=(-1)^{\ell(w)}c_{w'}$$를 만족하도록 강제한다. $$c_e=1$$이므로 $$c_w=(-1)^{\ell(w)}$$이다. 한편 $$\lambda+\rho$$가 strictly dominant이고 정칙이므로 $$W$$가 그 위에 자유롭게 작용하여 $$w(\lambda+\rho)$$들이 서로 다른 $$\lvert W\rvert$$개의 weight를 주어, 위 계수 부여에 충돌이 없다. 그러므로

$$\Delta\cdot\mathrm{ch}\,L(\lambda)=\sum_{w\in W}(-1)^{\ell(w)}e^{w(\lambda+\rho)}$$

이고, $$\Delta=\sum_w(-1)^{\ell(w)}e^{w\rho}=\prod_{\alpha>0}(e^{\alpha/2}-e^{-\alpha/2})$$로 양변을 나누면 주장한 공식을 얻는다.

</details>

분자와 분모는 각각 $$W$$-반대칭인 $$\widehat{\mathbb{Z}[P]}$$의 원소이고, 그 몫이 $$W$$-불변인 형식 지표를 준다는 점이 공식의 구조를 떠받친다. 분모를 $$\rho$$의 궤도합으로, 분자를 $$\lambda+\rho$$의 궤도합으로 적으면 두 교대합이 같은 꼴을 가지므로, 분자를 분모로 형식적으로 나누는 계산이 곧 weight 중복도를 산출한다. $$\lambda=0$$이면 분자와 분모가 같아 $$\mathrm{ch}\,L(0)=1$$, 곧 자명한 표현을 정확히 회복한다.

## Weyl 차원 공식

지표 공식의 양변을 차원으로 평가하면 닫힌 차원 공식이 따라온다. 차원은 모든 형식기호를 $$1$$로 보내는 평가 $$\varepsilon$$로 얻어지지만 ([정의 2](#def2) 이후의 논의), 분자와 분모가 $$\varepsilon$$에서 모두 $$0$$이 되므로 곧바로 대입할 수는 없다. 대신 $$e^\mu\mapsto e^{t\langle\mu,\rho^\vee\rangle}$$ 류의 일변수 변형을 거쳐 극한을 취하는 방식으로 부정형을 해소한다.

<div class="proposition" markdown="1">

<ins id="cor10">**따름정리 10 (Weyl 차원 공식)**</ins> dominant integral weight $$\lambda$$에 대하여

$$\dim L(\lambda)=\prod_{\alpha\in\Phi^+}\frac{\langle\lambda+\rho,\alpha\rangle}{\langle\rho,\alpha\rangle}$$

이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\mathfrak{h}^\ast$$의 정칙 원소 $$\rho^\vee$$ (모든 positive root $$\alpha$$에 대해 $$\langle\alpha,\rho^\vee\rangle>0$$)를 고정하고, 실변수 $$t$$에 대해 환 준동형 $$F_t:\widehat{\mathbb{Z}[P]}\rightarrow\mathbb{R}$$을 $$F_t(e^\mu)=e^{t\langle\mu,\rho^\vee\rangle}$$로 정의한다. $$F_0=\varepsilon$$이고 $$F_t(\mathrm{ch}\,L(\lambda))$$는 $$t\rightarrow 0$$에서 $$\dim L(\lambda)$$로 수렴한다. [정리 9](#thm9)를 $$F_t$$로 평가하면

$$F_t(\mathrm{ch}\,L(\lambda))=\frac{\sum_{w}(-1)^{\ell(w)}e^{t\langle w(\lambda+\rho),\rho^\vee\rangle}}{\prod_{\alpha>0}\bigl(e^{t\langle\alpha,\rho^\vee\rangle/2}-e^{-t\langle\alpha,\rho^\vee\rangle/2}\bigr)}$$

이다. 여기서 모든 $$\mu\in\mathfrak{h}^\ast$$에 대해 성립하는 항등식

$$\sum_{w\in W}(-1)^{\ell(w)}e^{t\langle\mu,w\rho^\vee\rangle}=\prod_{\alpha\in\Phi^+}\Bigl(e^{t\langle\mu,\alpha^\vee\rangle/2}-e^{-t\langle\mu,\alpha^\vee\rangle/2}\Bigr)$$

를 쓴다. 이는 $$\rho^\vee=\tfrac12\sum_{\alpha>0}\alpha^\vee$$를 이용한 coroot 쪽 Weyl denominator 항등식 ([명제 7](#prop7)의 dual) 이다. $$\langle w(\lambda+\rho),\rho^\vee\rangle=\langle\lambda+\rho,w^{-1}\rho^\vee\rangle$$이므로 분자는 이 항등식의 $$\mu=\lambda+\rho$$ 경우의 좌변, 분모는 $$\mu=\rho$$ 경우의 좌변이다. 따라서

$$F_t(\mathrm{ch}\,L(\lambda))=\frac{\prod_{\alpha>0}\bigl(e^{t\langle\lambda+\rho,\alpha^\vee\rangle/2}-e^{-t\langle\lambda+\rho,\alpha^\vee\rangle/2}\bigr)}{\prod_{\alpha>0}\bigl(e^{t\langle\rho,\alpha^\vee\rangle/2}-e^{-t\langle\rho,\alpha^\vee\rangle/2}\bigr)}$$

이다. 각 인자에 $$e^x-e^{-x}=2x+O(x^3)$$을 적용하면 $$t\rightarrow 0$$에서

$$F_t(\mathrm{ch}\,L(\lambda))\longrightarrow\prod_{\alpha\in\Phi^+}\frac{\langle\lambda+\rho,\alpha^\vee\rangle}{\langle\rho,\alpha^\vee\rangle}=\prod_{\alpha\in\Phi^+}\frac{\langle\lambda+\rho,\alpha\rangle}{\langle\rho,\alpha\rangle}$$

이고, 좌변의 극한은 $$\dim L(\lambda)$$이므로 주장한 등식을 얻는다. 분자와 분모의 인자 수가 모두 $$\lvert\Phi^+\rvert$$로 같아 $$t$$의 거듭제곱이 상쇄되고 상수항만 남는다.

</details>

차원 공식은 각 positive root $$\alpha$$가 비율 $$\langle\lambda+\rho,\alpha\rangle/\langle\rho,\alpha\rangle$$을 기여하고 그 곱이 차원이 된다는 명료한 그림을 준다. $$\lambda=0$$이면 모든 비율이 $$1$$이어서 $$\dim L(0)=1$$이 되고, $$\lambda$$가 한 fundamental weight 방향으로 커질수록 그 방향과 짝하는 root들의 기여가 선형으로 늘어 차원이 다항식적으로 증가한다. 이 공식은 weight 중복도 전체를 알 필요 없이 차원만을 root 데이터에서 직접 읽게 해 준다.

## 예시

가장 작은 두 경우에서 두 공식을 검산한다. 먼저 $$\sl_2$$에서는 모든 양이 한 변수로 적힌다.

<div class="example" markdown="1">

<ins id="ex11">**예시 11**</ins> $$\mathfrak{g}=\sl_2$$에서 positive root는 $$\alpha$$ 하나뿐이고 Weyl group은 $$W=\{e,s_\alpha\}$$, $$\ell(s_\alpha)=1$$이다. fundamental weight $$\varpi$$로 $$\alpha=2\varpi$$이고 $$\rho=\tfrac12\alpha=\varpi$$이다. dominant integral weight를 $$\lambda=m\varpi$$ ($$m\in\mathbb{Z}_{\geq 0}$$)이라 하면 $$\lambda+\rho=(m+1)\varpi$$이다. 형식기호를 $$x=e^{\varpi}$$로 적으면 $$e^{w(\lambda+\rho)}$$는 $$w=e$$에서 $$x^{m+1}$$, $$w=s_\alpha$$에서 $$x^{-(m+1)}$$이고 마찬가지로 분모는 $$x-x^{-1}$$이다. [정리 9](#thm9)는

$$\mathrm{ch}\,L(m\varpi)=\frac{x^{m+1}-x^{-(m+1)}}{x-x^{-1}}=x^m+x^{m-2}+\cdots+x^{-m}$$

을 주며, 이는 weight $$m,m-2,\ldots,-m$$이 각각 중복도 $$1$$로 나타남을 뜻해 [§sl₂의 표현론, ⁋정의 5](/ko/math/lie_theory/representations_of_sl2#def5)의 $$V(m)$$과 정확히 일치한다. 차원 공식은 $$\langle\lambda+\rho,\alpha\rangle/\langle\rho,\alpha\rangle=(m+1)/1=m+1$$을 주어 $$\dim L(m\varpi)=m+1$$로, 같은 결론을 회복한다.

</div>

$$\sl_2$$에서는 분자의 등비급수가 그대로 weight 사슬을 내어주므로 지표 공식이 곧 $$\sl_2$$ 분류의 재서술이 된다. 다음으로 $$\sl_3$$에서는 positive root가 셋이고 Weyl group이 $$S_3$$이어서 중복도가 비로소 자명하지 않게 된다.

<div class="example" markdown="1">

<ins id="ex12">**예시 12**</ins> $$\mathfrak{g}=\sl_3$$에서 simple root는 $$\alpha_1,\alpha_2$$이고 positive root는 $$\alpha_1,\alpha_2,\alpha_1+\alpha_2$$의 셋이다. Weyl group은 $$W\cong S_3$$으로 $$\lvert W\rvert=6$$이며, $$\rho=\alpha_1+\alpha_2$$ (곧 두 fundamental weight의 합 $$\varpi_1+\varpi_2$$)이다. 내적을 $$\langle\alpha_i,\alpha_i\rangle=2$$, $$\langle\alpha_1,\alpha_2\rangle=-1$$로 정규화한다.

adjoint 표현은 highest weight $$\theta=\alpha_1+\alpha_2$$ (최고 root)를 갖는 $$L(\theta)$$이다. 차원을 계산하면 $$\theta+\rho=2(\alpha_1+\alpha_2)$$이고

$$\langle\theta+\rho,\alpha_1\rangle=\langle 2\alpha_1+2\alpha_2,\alpha_1\rangle=2\cdot 2+2\cdot(-1)=2,$$

같은 계산으로 $$\langle\theta+\rho,\alpha_2\rangle=2$$이며, $$\alpha_1+\alpha_2$$에 대해서는 $$\langle\theta+\rho,\alpha_1+\alpha_2\rangle=2+2=4$$이다. 한편 분모는 $$\langle\rho,\alpha_1\rangle=\langle\rho,\alpha_2\rangle=1$$, $$\langle\rho,\alpha_1+\alpha_2\rangle=2$$이다. 따라서 [따름정리 10](#cor10)에 의해

$$\dim L(\theta)=\frac{2}{1}\cdot\frac{2}{1}\cdot\frac{4}{2}=8$$

로, $$\sl_3$$ 자신의 차원 $$3^2-1=8$$과 일치한다. 이 $$8$$차원 표현에서 weight $$0$$은 Cartan subalgebra에 대응하여 중복도 $$2$$로 나타나는데, 지표 공식 [정리 9](#thm9)에서 분자 $$\sum_w(-1)^{\ell(w)}e^{w(\theta+\rho)}$$를 분모로 나누어 $$e^0$$의 계수를 추출하면 정확히 이 중복도 $$2$$가 나온다. 이는 차원 합 $$6\cdot 1+1\cdot 2=8$$로도 맞아떨어진다 (영이 아닌 여섯 root weight가 각 중복도 $$1$$, weight $$0$$이 중복도 $$2$$).

</div>

$$\sl_3$$의 adjoint 표현은 weight $$0$$의 중복도가 $$1$$을 넘는 첫 예로, 지표 공식이 단순한 weight 나열을 넘어 중복도까지 정확히 산출함을 보여준다. 일반적으로 $$\mathfrak{g}$$의 rank가 커질수록 weight 중복도는 Kostant partition function이 정하는 복잡한 양이 되며, Weyl 지표 공식의 분자를 분모로 나누는 형식 계산이 이 모든 중복도를 한꺼번에 결정한다. 차원 공식은 그 가운데 전체 차원이라는 한 정보만을 root 데이터에서 곧바로 읽어내는 특수화이다.

---

**참고문헌**

**[Hum]** J. E. Humphreys, *Introduction to Lie algebras and representation theory*, Graduate Texts in Mathematics, Springer, 1972.  
**[FH]** W. Fulton and J. Harris, *Representation theory: a first course*, Graduate Texts in Mathematics, Springer, 1991.  
**[Kna]** A. W. Knapp, *Lie groups beyond an introduction*, 2nd ed., Progress in Mathematics, Birkhäuser, 2002.  
