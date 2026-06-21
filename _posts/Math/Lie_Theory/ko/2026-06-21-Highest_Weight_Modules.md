---
title: "최고 무게 가군"
description: "Semisimple Lie algebra의 Borel subalgebra로 유도되는 Verma module M(λ)를 구성하고, 그 보편성과 PBW 기저, 유일한 maximal submodule과 기약 quotient L(λ)를 확립한다. 이로부터 유한차원 기약 표현이 정확히 dominant integral weight λ에 대한 L(λ)들로 분류된다는 최고 무게 정리를 각 simple root의 sl₂-triple과 Weyl 완전가약성을 통해 증명한다."
excerpt: "Borel subalgebra, weight, highest weight vector, Verma module M(λ), 기약 quotient L(λ), dominant integral weight, 최고 무게 정리"

categories: [Math / Lie Theory]
permalink: /ko/math/lie_theory/highest_weight_modules
sidebar: 
    nav: "lie_theory-ko"

date: 2026-06-21
weight: 7.3

published: false
---

Semisimple Lie algebra $$\mathfrak{g}$$의 표현론은 Weyl의 완전가약성 정리에 의해 기약 표현의 분류 문제로 환원된다 ([§Weyl 완전가약성 정리, ⁋정리 7](/ko/math/lie_theory/weyl_complete_reducibility#thm7)). $$\sl_2$$의 경우 이 분류는 highest weight vector에서 출발해 lowering operator를 반복 적용하는 사슬을 분석하여 완성되었으며, 각 음이 아닌 정수마다 유일한 기약 표현이 대응되었다 ([§sl₂의 표현론, ⁋명제 6](/ko/math/lie_theory/representations_of_sl2#prop6)). 일반적인 semisimple Lie algebra에서도 같은 골격이 유지된다. Cartan subalgebra $$\mathfrak{h}$$에 대한 weight 분해가 $$h$$의 고윳값 분해를 대신하고, positive root들이 정하는 부분대수 $$\mathfrak{n}^+$$가 raising operator의 역할을 모아 담으며, $$\mathfrak{n}^+$$가 죽이는 highest weight vector 하나가 표현 전체를 생성한다.

이 글에서 우리는 그러한 highest weight vector로 생성되는 가장 보편적인 가군인 Verma module $$M(\lambda)$$를 보편 포락 대수의 induced module로 구성하고, 그 유일한 maximal submodule을 몫으로 잘라 기약 가군 $$L(\lambda)$$를 얻는다. 그런 뒤 $$L(\lambda)$$가 유한차원이 되는 것이 정확히 $$\lambda$$가 dominant integral weight일 때임을 보여, 유한차원 기약 표현이 dominant integral weight들과 일대일로 대응한다는 *최고 무게 정리<sub>theorem of the highest weight</sub>*를 확립한다. 이 글 전체에서 $$\mathfrak{g}$$는 대수적으로 닫힌 표수 $$0$$의 체 (편의상 $$\mathbb{C}$$) 위의 유한차원 semisimple Lie algebra이고, $$\mathfrak{h}$$는 그 Cartan subalgebra, $$\Phi\subseteq\mathfrak{h}^\ast$$는 그에 대한 root system이며, 표현 또는 가군이라 하면 $$\mathfrak{g}$$-가군, 곧 Lie algebra 준동형 $$\mathfrak{g}\rightarrow\gl(V)$$가 정하는 $$U(\mathfrak{g})$$-가군을 뜻한다.

## Borel subalgebra와 weight

분류의 무대를 마련하기 위해 root 분해로부터 positive root들이 정하는 부분대수를 떼어낸다. Cartan subalgebra $$\mathfrak{h}$$와 root system $$\Phi$$, 그리고 root space 분해

$$\mathfrak{g}=\mathfrak{h}\oplus\bigoplus_{\alpha\in\Phi}\mathfrak{g}_\alpha$$

는 이미 확립되어 있고, 각 $$\mathfrak{g}_\alpha$$가 $$1$$차원이라는 사실도 알고 있다 ([§근계, ⁋정의 5](/ko/math/lie_theory/root_systems#def5) 및 [§근계, ⁋명제 6](/ko/math/lie_theory/root_systems#prop6) 이후의 논의). positive root들의 모임 $$\Phi^+\subseteq\Phi$$를 하나 고정한다 ([§근계, ⁋정의 15](/ko/math/lie_theory/root_systems#def15)).

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> positive root들에 대응하는 root space들의 합

$$\mathfrak{n}^+=\bigoplus_{\alpha\in\Phi^+}\mathfrak{g}_\alpha,\qquad\mathfrak{n}^-=\bigoplus_{\alpha\in\Phi^+}\mathfrak{g}_{-\alpha}$$

을 각각 $$\mathfrak{g}$$의 *positive nilpotent subalgebra*와 *negative nilpotent subalgebra*라 부르고, 

$$\mathfrak{b}=\mathfrak{h}\oplus\mathfrak{n}^+$$

을 $$\mathfrak{g}$$의 *Borel subalgebra<sub>보렐 부분대수</sub>*라 부른다.

</div>

$$[\mathfrak{g}_\alpha,\mathfrak{g}_\beta]\subseteq\mathfrak{g}_{\alpha+\beta}$$이고 ([§근계, ⁋명제 6](/ko/math/lie_theory/root_systems#prop6)) 두 positive root의 합은 다시 positive root이거나 root가 아니므로, $$\mathfrak{n}^+$$는 $$\mathfrak{g}$$의 부분 Lie algebra이며 같은 이유로 $$\mathfrak{n}^-$$도 그러하다. 또한 $$[\mathfrak{h},\mathfrak{g}_\alpha]\subseteq\mathfrak{g}_\alpha$$이므로 $$\mathfrak{h}$$가 $$\mathfrak{n}^+$$를 정규화하여 $$\mathfrak{b}=\mathfrak{h}\oplus\mathfrak{n}^+$$ 역시 부분 Lie algebra이고, $$\mathfrak{n}^+$$는 $$\mathfrak{b}$$의 ideal이다. 벡터공간으로서

$$\mathfrak{g}=\mathfrak{n}^-\oplus\mathfrak{h}\oplus\mathfrak{n}^+=\mathfrak{n}^-\oplus\mathfrak{b}$$

라는 삼각 분해를 얻으며, 이 분해가 아래 Verma module의 구성과 그 PBW 기저의 토대가 된다. 이름의 nilpotent는 $$\mathfrak{n}^\pm$$가 실제로 nilpotent Lie algebra라는 사실에서 온 것으로, root 높이에 대한 grading이 bracket을 한 단계씩 올려 유한 번 안에 $$0$$이 되기 때문이다.

이제 임의의 $$\mathfrak{g}$$-가군 위에서 $$\mathfrak{h}$$의 작용에 대한 동시 고유공간 분해를 정의한다. 이는 $$\sl_2$$에서 $$h$$ 하나의 고유공간 분해 ([§sl₂의 표현론, ⁋정의 1](/ko/math/lie_theory/representations_of_sl2#def1))를 Cartan subalgebra 전체로 일반화한 것이다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> $$\mathfrak{g}$$-가군 $$V$$와 $$\lambda\in\mathfrak{h}^\ast$$에 대하여, 부분공간

$$V_\lambda=\{v\in V\mid H\cdot v=\lambda(H)\,v\ \text{ for all }H\in\mathfrak{h}\}$$

을 *weight $$\lambda$$의 weight space*라 부른다. $$V_\lambda\neq 0$$인 $$\lambda$$를 $$V$$의 *weight<sub>무게</sub>*라 하고, $$\dim V_\lambda$$를 그 weight의 *multiplicity<sub>중복도</sub>*라 부른다. $$V=\bigoplus_{\lambda\in\mathfrak{h}^\ast}V_\lambda$$로 분해되는 가군을 *weight module<sub>무게 가군</sub>*이라 부른다.

</div>

root space $$\mathfrak{g}_\alpha$$가 adjoint 작용에 대한 weight $$\alpha$$의 weight space라는 점에서, root 분해 자신이 adjoint representation의 weight 분해이다. 일반적인 가군의 작용 위에서 root vector들이 weight를 어떻게 옮기는지는 root 분해의 bracket 관계가 그대로 결정한다. 다음 명제는 [§sl₂의 표현론, ⁋명제 2](/ko/math/lie_theory/representations_of_sl2#prop2)에서 $$e,f$$가 weight를 $$\pm2$$만큼 옮긴다는 사실을 임의의 root vector로 확장한다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> $$\mathfrak{g}$$-가군 $$V$$, weight $$\lambda\in\mathfrak{h}^\ast$$, 그리고 root $$\alpha\in\Phi$$에 대하여

$$\mathfrak{g}_\alpha\cdot V_\lambda\subseteq V_{\lambda+\alpha}$$

가 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$x\in\mathfrak{g}_\alpha$$, $$v\in V_\lambda$$라 하자. 임의의 $$H\in\mathfrak{h}$$에 대하여 가군의 작용이 $$H\cdot(x\cdot v)=x\cdot(H\cdot v)+[H,x]\cdot v$$를 만족하고, $$H\cdot v=\lambda(H)v$$이며 $$[H,x]=\alpha(H)x$$이므로

$$H\cdot(x\cdot v)=\lambda(H)\,x\cdot v+\alpha(H)\,x\cdot v=(\lambda+\alpha)(H)\,(x\cdot v)$$

이다. 이것이 모든 $$H\in\mathfrak{h}$$에 대해 성립하므로 $$x\cdot v\in V_{\lambda+\alpha}$$이다.

</details>

따라서 $$\mathfrak{n}^+$$에 속하는 root vector들은 weight를 positive root만큼 올리고, $$\mathfrak{n}^-$$의 root vector들은 weight를 내린다. $$\mathfrak{h}$$의 원소는 자기 자신이 정하는 weight space를 보존한다. 이로부터 raising operator들에 의해 더 이상 올라가지 않는 벡터, 곧 $$\mathfrak{n}^+$$에 의해 소멸되는 벡터가 분류의 출발점이 된다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> $$\mathfrak{g}$$-가군 $$V$$의 벡터 $$v\neq 0$$이 weight $$\lambda\in\mathfrak{h}^\ast$$의 *highest weight vector<sub>최고무게 벡터</sub>*라는 것은

$$H\cdot v=\lambda(H)\,v\ \text{ for all }H\in\mathfrak{h},\qquad \mathfrak{n}^+\cdot v=0$$

이 성립하는 것이다. 곧 $$v\in V_\lambda$$이고 모든 positive root vector가 $$v$$를 소멸시키는 것이다. 이 때 $$\lambda$$를 $$v$$의 *highest weight<sub>최고무게</sub>*라 부른다.

</div>

$$\mathfrak{n}^+$$가 $$\Phi^+$$의 root vector들로 생성되므로, $$\mathfrak{n}^+\cdot v=0$$이라는 조건은 각 simple root $$\alpha_i$$에 대응하는 raising operator $$e_i\in\mathfrak{g}_{\alpha_i}$$가 $$v$$를 소멸시키는 것과 동치이다. 실제로 임의의 positive root는 simple root들의 음이 아닌 정수 결합이고 $$[\mathfrak{g}_{\alpha},\mathfrak{g}_{\beta}]\subseteq\mathfrak{g}_{\alpha+\beta}$$이므로, $$\mathfrak{n}^+$$는 simple root vector들로 생성되는 부분대수이다. $$\sl_2$$에서 $$e\cdot v=0$$이라는 조건이 highest weight vector를 규정하였던 것 ([§sl₂의 표현론, ⁋정의 3](/ko/math/lie_theory/representations_of_sl2#def3))과 정확히 대응한다.

## Verma module

highest weight $$\lambda$$를 갖는 가군 가운데 가장 보편적인 것을 구성한다. 발상은 highest weight vector 하나만을 형식적으로 도입하여 그 위에서 $$\mathfrak{b}$$가 정해진 방식으로 작용하도록 한 뒤, $$\mathfrak{g}$$ 전체의 작용을 보편 포락 대수의 induced module로 자유롭게 풀어주는 것이다. 먼저 $$\mathfrak{b}$$ 위의 $$1$$차원 표현을 정한다.

$$\lambda\in\mathfrak{h}^\ast$$에 대하여, $$1$$차원 벡터공간 $$\mathbb{C}_\lambda=\mathbb{C}v_\lambda$$ 위에 $$\mathfrak{b}=\mathfrak{h}\oplus\mathfrak{n}^+$$의 작용을

$$H\cdot v_\lambda=\lambda(H)\,v_\lambda\ \text{ for }H\in\mathfrak{h},\qquad \mathfrak{n}^+\cdot v_\lambda=0$$

으로 준다. 이것이 $$\mathfrak{b}$$의 Lie algebra 표현임은 $$\mathfrak{n}^+$$가 $$\mathfrak{b}$$의 ideal이고 $$[\mathfrak{b},\mathfrak{b}]=[\mathfrak{h},\mathfrak{n}^+]+[\mathfrak{n}^+,\mathfrak{n}^+]\subseteq\mathfrak{n}^+$$가 $$\mathbb{C}_\lambda$$ 위에서 $$0$$으로 작용한다는 데에서 따라온다. 따라서 $$\mathbb{C}_\lambda$$는 $$U(\mathfrak{b})$$-가군이다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> $$\lambda\in\mathfrak{h}^\ast$$에 대하여, 위의 $$1$$차원 $$U(\mathfrak{b})$$-가군 $$\mathbb{C}_\lambda$$로부터 유도되는 $$U(\mathfrak{g})$$-가군

$$M(\lambda)=U(\mathfrak{g})\otimes_{U(\mathfrak{b})}\mathbb{C}_\lambda$$

을 highest weight $$\lambda$$의 *Verma module<sub>베르마 가군</sub>*이라 부른다. 여기에서 $$U(\mathfrak{g})$$는 오른쪽 곱으로 $$U(\mathfrak{b})$$-가군이 되고, $$U(\mathfrak{g})$$가 왼쪽 곱으로 작용하여 $$M(\lambda)$$를 $$U(\mathfrak{g})$$-가군으로 만든다.

</div>

$$M(\lambda)$$의 생성원 $$v_\lambda^+=1\otimes v_\lambda$$는 $$M(\lambda)$$의 highest weight vector이다. 임의의 $$H\in\mathfrak{h}$$에 대하여 $$H\cdot(1\otimes v_\lambda)=1\otimes(H\cdot v_\lambda)=\lambda(H)(1\otimes v_\lambda)$$이고, 마찬가지로 $$\mathfrak{n}^+\cdot v_\lambda^+=1\otimes(\mathfrak{n}^+\cdot v_\lambda)=0$$이기 때문이다. 텐서곱에서 $$\mathfrak{b}$$의 원소를 왼쪽 인자에서 오른쪽 인자로 넘길 수 있다는 점이 이 계산의 핵심이며, 같은 이유로 $$M(\lambda)$$는 $$v_\lambda^+$$ 하나로 $$U(\mathfrak{g})$$-가군으로서 생성된다. 다음 명제는 이 highest weight vector가 갖는 보편성을 정확히 진술한다. 곧 $$M(\lambda)$$는 highest weight $$\lambda$$의 highest weight vector를 갖는 가군들의 범주에서 initial object이다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> $$V$$가 $$\mathfrak{g}$$-가군이고 $$w\in V$$가 highest weight $$\lambda$$의 highest weight vector이면, $$\varphi(v_\lambda^+)=w$$를 만족하는 $$\mathfrak{g}$$-가군 준동형 $$\varphi:M(\lambda)\rightarrow V$$가 유일하게 존재한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$w$$가 highest weight $$\lambda$$의 highest weight vector이므로, $$1$$차원 부분공간 $$\mathbb{C}w$$ 위에서 $$\mathfrak{b}$$는 $$\mathbb{C}_\lambda$$와 동일한 방식으로 작용한다. 곧 $$H\cdot w=\lambda(H)w$$이고 $$\mathfrak{n}^+\cdot w=0$$이다. 따라서 $$v_\lambda\mapsto w$$로 주어지는 사상은 $$U(\mathfrak{b})$$-가군 준동형 $$\mathbb{C}_\lambda\rightarrow V$$이다. Induced module의 보편성, 곧 tensor-hom adjunction

$$\Hom_{U(\mathfrak{g})}\bigl(U(\mathfrak{g})\otimes_{U(\mathfrak{b})}\mathbb{C}_\lambda,\,V\bigr)\cong\Hom_{U(\mathfrak{b})}(\mathbb{C}_\lambda,\,V)$$

에 의하여, 이 $$U(\mathfrak{b})$$-사상에 대응하는 $$U(\mathfrak{g})$$-가군 준동형 $$\varphi:M(\lambda)\rightarrow V$$가 유일하게 존재하며, 이는 $$v_\lambda^+=1\otimes v_\lambda$$를 $$w$$로 보낸다. 유일성은 $$M(\lambda)$$가 $$v_\lambda^+$$로 $$U(\mathfrak{g})$$-가군으로서 생성된다는 사실에서 따라온다. $$\mathfrak{g}$$-사상은 $$U(\mathfrak{g})$$-작용과 교환하므로 생성원에서의 값으로 완전히 결정되기 때문이다.

</details>

이 보편성은 highest weight $$\lambda$$의 highest weight vector로 생성되는 임의의 가군이 $$M(\lambda)$$의 몫임을 함의한다. 따라서 그러한 가군들 가운데 $$M(\lambda)$$가 가장 큰 것이며, 특히 highest weight $$\lambda$$의 기약 가군도 $$M(\lambda)$$의 적당한 몫으로 얻어질 것이다. 이 몫을 정확히 짚어내려면 먼저 $$M(\lambda)$$의 크기와 weight 구조를 알아야 하고, 그것을 PBW 정리가 제공한다.

삼각 분해 $$\mathfrak{g}=\mathfrak{n}^-\oplus\mathfrak{b}$$에서 $$\mathfrak{n}^-$$의 기저를 먼저, 그다음 $$\mathfrak{b}$$의 기저를 두는 순서로 $$\mathfrak{g}$$의 기저에 전순서를 주면, PBW 정리는 $$U(\mathfrak{g})$$가 $$U(\mathfrak{n}^-)$$와 $$U(\mathfrak{b})$$의 곱으로 분해됨을 준다. 이로부터 $$M(\lambda)$$가 $$U(\mathfrak{n}^-)$$ 위의 자유가군이 된다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> $$\Phi^+=\{\beta_1,\ldots,\beta_N\}$$을 positive root들의 나열이라 하고, 각 $$\beta_k$$에 대하여 $$0\neq f_k\in\mathfrak{g}_{-\beta_k}$$를 택하자. 그럼 단항식들

$$f_1^{\,m_1}f_2^{\,m_2}\cdots f_N^{\,m_N}\cdot v_\lambda^+,\qquad m_1,\ldots,m_N\geq 0$$

들은 $$M(\lambda)$$의 $$\mathbb{C}$$-기저를 이룬다. 따라서 $$M(\lambda)$$는 $$U(\mathfrak{n}^-)$$ 위의 계수 $$1$$의 자유가군 $$U(\mathfrak{n}^-)\cdot v_\lambda^+$$이며, 그 weight들은 $$\lambda-\sum_k m_k\beta_k$$ ($$m_k\geq 0$$)의 꼴이고 각 weight space는 유한차원이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\mathfrak{g}$$의 기저를 $$\mathfrak{n}^-$$의 기저 $$(f_1,\ldots,f_N)$$, $$\mathfrak{h}$$의 기저 $$(H_1,\ldots,H_l)$$, $$\mathfrak{n}^+$$의 기저 $$(e_1,\ldots,e_N)$$를 이어 붙여 만들고, 이 순서로 첨자에 전순서를 준다. 그럼 PBW 정리 ([§보편 포락 대수, ⁋정리 9](/ko/math/lie_theory/universal_enveloping_algebra#thm9))에 의하여 $$U(\mathfrak{g})$$는 정렬된 단항식

$$f_1^{\,m_1}\cdots f_N^{\,m_N}\,H_1^{\,p_1}\cdots H_l^{\,p_l}\,e_1^{\,q_1}\cdots e_N^{\,q_N}$$

들을 기저로 갖는다. 곧 곱사상 $$U(\mathfrak{n}^-)\otimes U(\mathfrak{h})\otimes U(\mathfrak{n}^+)\rightarrow U(\mathfrak{g})$$가 $$\mathbb{C}$$-벡터공간의 동형이다. 

이제 $$M(\lambda)=U(\mathfrak{g})\otimes_{U(\mathfrak{b})}\mathbb{C}_\lambda$$에서 임의의 원소를 위 기저로 전개한 뒤 $$v_\lambda^+$$에 작용시킨다. 정렬된 단항식의 오른쪽 끝에 있는 $$\mathfrak{b}=\mathfrak{h}\oplus\mathfrak{n}^+$$의 부분 $$H_1^{\,p_1}\cdots e_N^{\,q_N}$$은 $$U(\mathfrak{b})$$에 속하므로 텐서곱을 가로질러 $$\mathbb{C}_\lambda$$에 작용한다. $$q_1=\cdots=q_N=0$$이 아니면 $$\mathfrak{n}^+$$의 원소가 $$v_\lambda$$를 소멸시켜 결과가 $$0$$이고, $$q_k$$가 모두 $$0$$이면 $$H_1^{\,p_1}\cdots H_l^{\,p_l}\cdot v_\lambda=\prod_j\lambda(H_j)^{p_j}\,v_\lambda$$는 $$v_\lambda$$의 스칼라배이다. 따라서 $$M(\lambda)$$의 모든 원소는 $$f_1^{\,m_1}\cdots f_N^{\,m_N}\cdot v_\lambda^+$$들의 일차결합이며, 이들이 $$M(\lambda)$$를 생성한다.

일차독립성은 PBW 기저로부터 곧장 따라온다. $$M(\lambda)$$는 $$\mathbb{C}$$-벡터공간으로서 $$U(\mathfrak{g})\otimes_{U(\mathfrak{b})}\mathbb{C}_\lambda\cong U(\mathfrak{n}^-)\otimes_{\mathbb{C}}\mathbb{C}_\lambda$$이고, 이 동형은 곱사상 $$U(\mathfrak{n}^-)\otimes U(\mathfrak{b})\rightarrow U(\mathfrak{g})$$가 동형이라는 위 사실의 직접적 귀결이다. $$U(\mathfrak{n}^-)$$의 PBW 기저 $$f_1^{\,m_1}\cdots f_N^{\,m_N}$$이 일차독립이므로, 이들을 $$v_\lambda^+$$에 작용시킨 원소들도 일차독립이다. 이로써 $$M(\lambda)$$는 $$U(\mathfrak{n}^-)$$ 위의 자유가군이고 $$v_\lambda^+$$가 그 자유 생성원이다.

끝으로 weight 구조를 본다. $$f_k\in\mathfrak{g}_{-\beta_k}$$이므로 [명제 3](#prop3)에 의하여 $$f_1^{\,m_1}\cdots f_N^{\,m_N}\cdot v_\lambda^+$$는 weight $$\lambda-\sum_k m_k\beta_k$$를 갖는다. 고정된 weight $$\mu=\lambda-\sum_k m_k\beta_k$$를 주는 지수 $$(m_1,\ldots,m_N)$$의 개수는 유한하므로 각 weight space는 유한차원이며, $$M(\lambda)=\bigoplus_\mu M(\lambda)_\mu$$는 weight module이다.

</details>

명제 7은 $$M(\lambda)$$가 $$\sl_2$$에서의 highest weight 사슬을 정확히 일반화함을 보여준다. $$\sl_2$$의 highest weight vector에서 $$f$$를 반복 적용하여 얻은 사슬 ([§sl₂의 표현론, ⁋명제 4](/ko/math/lie_theory/representations_of_sl2#prop4))이 여기에서는 여러 lowering operator의 모든 정렬된 곱으로 대체되며, 그 결과 $$M(\lambda)$$는 무한차원의 weight module이 된다. highest weight space $$M(\lambda)_\lambda$$는 $$v_\lambda^+$$ 하나로 생성되는 $$1$$차원이고, 다른 모든 weight는 $$\lambda$$에서 positive root들을 빼서 얻어지므로 $$\lambda$$보다 "아래"에 놓인다.

## 기약 quotient

이제 $$M(\lambda)$$에서 기약 가군을 잘라낸다. 핵심은 $$M(\lambda)$$가 유일한 maximal submodule을 갖는다는 것이며, 이는 highest weight space가 $$1$$차원이라는 사실과, 진부분가군이 highest weight space를 건드리지 못한다는 관찰에서 나온다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> $$M(\lambda)$$의 임의의 진부분가군 $$W\subsetneq M(\lambda)$$은 highest weight space $$M(\lambda)_\lambda=\mathbb{C}v_\lambda^+$$와 자명하게 만난다. 곧 $$W\cap M(\lambda)_\lambda=0$$이다. 따라서 모든 진부분가군의 합 $$M^{\mathrm{rad}}(\lambda)$$도 진부분가군이며, $$M(\lambda)$$는 이 $$M^{\mathrm{rad}}(\lambda)$$를 유일한 maximal submodule로 갖는다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$W$$가 부분가군이므로 $$\mathfrak{h}$$-작용에 대해 닫혀 있고, [명제 7](#prop7)에 의해 $$M(\lambda)$$가 weight module이므로 $$W$$도 weight module이다. 곧 $$W=\bigoplus_\mu(W\cap M(\lambda)_\mu)$$이다. 만일 $$W\cap M(\lambda)_\lambda\neq 0$$이면 $$M(\lambda)_\lambda=\mathbb{C}v_\lambda^+$$가 $$1$$차원이므로 $$v_\lambda^+\in W$$이고, $$v_\lambda^+$$가 $$M(\lambda)$$를 $$U(\mathfrak{g})$$-가군으로서 생성하므로 $$W=M(\lambda)$$가 되어 $$W$$가 진부분가군이라는 가정에 모순이다. 따라서 $$W\cap M(\lambda)_\lambda=0$$이다.

이제 모든 진부분가군의 합을 $$M^{\mathrm{rad}}(\lambda)=\sum_{W\subsetneq M(\lambda)}W$$라 하자. 각 진부분가군이 weight $$\lambda$$ 성분을 갖지 않으므로 그 합도 그러하여 $$M^{\mathrm{rad}}(\lambda)\cap M(\lambda)_\lambda=0$$이고, 특히 $$v_\lambda^+\notin M^{\mathrm{rad}}(\lambda)$$이므로 $$M^{\mathrm{rad}}(\lambda)\neq M(\lambda)$$, 곧 $$M^{\mathrm{rad}}(\lambda)$$는 진부분가군이다. 정의상 $$M^{\mathrm{rad}}(\lambda)$$는 모든 진부분가군을 포함하는 진부분가군이므로 유일한 maximal submodule이다.

</details>

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> [명제 8](#prop8)의 유일한 maximal submodule $$M^{\mathrm{rad}}(\lambda)$$에 대한 몫

$$L(\lambda)=M(\lambda)/M^{\mathrm{rad}}(\lambda)$$

을 highest weight $$\lambda$$의 *irreducible highest weight module<sub>기약 최고무게 가군</sub>*이라 부른다.

</div>

$$L(\lambda)$$는 유일한 maximal submodule에 대한 몫이므로 $$0$$이 아닌 진부분가군을 갖지 않아 기약이며, $$v_\lambda^+$$의 상 $$\bar v_\lambda$$가 highest weight $$\lambda$$의 highest weight vector로서 $$L(\lambda)$$를 생성한다. 다음 명제는 $$L(\lambda)$$가 highest weight $$\lambda$$를 갖는 유일한 기약 가군임을 보여, weight $$\lambda$$가 기약 가군을 동형을 무시하고 완전히 결정함을 확립한다.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> $$\lambda\in\mathfrak{h}^\ast$$에 대하여 $$L(\lambda)$$는 highest weight $$\lambda$$를 갖는 기약 가군이다. 역으로 $$V$$가 highest weight vector로 생성되는 기약 가군이면, 그 highest weight $$\lambda$$는 유일하게 결정되고 $$V\cong L(\lambda)$$이다. 특히 $$L(\mu)\cong L(\lambda)$$이면 $$\mu=\lambda$$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$L(\lambda)$$가 기약이고 highest weight $$\lambda$$를 가짐은 [정의 9](#def9) 직후에 확인하였다. 역방향을 보인다. $$V$$가 highest weight $$\lambda$$의 highest weight vector $$w$$로 생성되는 기약 가군이라 하자. [명제 6](#prop6)에 의하여 $$\varphi(v_\lambda^+)=w$$인 $$\mathfrak{g}$$-사상 $$\varphi:M(\lambda)\rightarrow V$$가 존재하고, $$V$$가 $$w$$로 생성되므로 $$\varphi$$는 전사이다. 따라서 $$V\cong M(\lambda)/\ker\varphi$$이다. $$V$$가 기약이므로 $$\ker\varphi$$는 $$M(\lambda)$$의 maximal submodule이고, [명제 8](#prop8)에 의해 maximal submodule은 $$M^{\mathrm{rad}}(\lambda)$$ 하나뿐이므로 $$\ker\varphi=M^{\mathrm{rad}}(\lambda)$$, 곧 $$V\cong L(\lambda)$$이다.

highest weight의 유일성을 본다. $$V$$가 highest weight vector로 생성되는 기약 가군이면 위에서 본 대로 $$V\cong L(\lambda)$$이고, [명제 7](#prop7)에 의하여 $$L(\lambda)$$의 모든 weight는 $$\lambda-\sum_k m_k\beta_k$$ ($$m_k\geq 0$$, $$\beta_k\in\Phi^+$$)의 꼴이다. 이 weight들 가운데 어떤 다른 weight $$\mu$$에도 positive root를 더해서는 도달할 수 없는 극대인 것은 $$\lambda$$뿐이다. $$\lambda$$에 positive root를 더하면 $$\lambda$$보다 위의 weight가 되는데 그러한 weight space는 $$0$$이기 때문이다. 따라서 $$\lambda$$는 $$V$$에 의해 내재적으로 결정되며, $$L(\mu)\cong L(\lambda)$$이면 양쪽의 이 극대 weight가 같아 $$\mu=\lambda$$이다.

</details>

명제 10은 모든 기약 highest weight 가군이 정확히 $$\mathfrak{h}^\ast$$의 원소로 색인됨을 말한다. 그러나 임의의 $$\lambda\in\mathfrak{h}^\ast$$에 대하여 $$L(\lambda)$$는 일반적으로 무한차원이다. $$\sl_2$$의 highest weight 사슬이 $$\mu$$가 음이 아닌 정수일 때에만 유한 단계에서 닫혔던 것처럼 ([§sl₂의 표현론, ⁋명제 4](/ko/math/lie_theory/representations_of_sl2#prop4) 이후의 논의), $$L(\lambda)$$가 유한차원이 되려면 $$\lambda$$가 각 simple root 방향으로 정수성 조건을 만족해야 한다. 다음 절에서 그 조건을 정확히 규정한다.

## 최고 무게 정리

유한차원성의 조건을 simple root별 $$\sl_2$$-triple로 환원하여 읽어낸다. 각 root $$\alpha\in\Phi$$는 $$\mathfrak{g}$$ 안에 $$\sl_2$$와 동형인 부분대수 $$\sl_{2,\alpha}=\langle e_\alpha,f_\alpha,h_\alpha\rangle$$를 낳으며, $$h_\alpha\in\mathfrak{h}$$는 표준 관계 $$[h_\alpha,e_\alpha]=2e_\alpha$$, $$[h_\alpha,f_\alpha]=-2f_\alpha$$, $$[e_\alpha,f_\alpha]=h_\alpha$$를 만족하는 *coroot*이다 ([§근계, ⁋명제 12](/ko/math/lie_theory/root_systems#prop12) 이전의 논의). simple root들을 $$\Delta=\{\alpha_1,\ldots,\alpha_l\}$$이라 하고 그 coroot을 $$h_i=h_{\alpha_i}$$, 대응하는 $$\sl_2$$-triple을 $$(e_i,f_i,h_i)$$로 적는다.

<div class="definition" markdown="1">

<ins id="def11">**정의 11**</ins> weight $$\lambda\in\mathfrak{h}^\ast$$이 *dominant integral<sub>지배적 정수</sub>* weight이라는 것은 모든 simple root $$\alpha_i$$에 대하여

$$\lambda(h_i)\in\mathbb{Z}_{\geq 0}$$

이 성립하는 것이다. 곧 각 simple coroot 위에서 $$\lambda$$가 음이 아닌 정숫값을 갖는 것이다.

</div>

$$\lambda(h_i)$$는 $$\sl_2$$ 표현론의 언어로 highest weight vector가 simple root $$\alpha_i$$ 방향의 $$\sl_{2,\alpha_i}$$ 위에서 갖는 highest weight이다. $$\sl_2$$의 유한차원 기약 표현의 highest weight가 항상 음이 아닌 정수였으므로 ([§sl₂의 표현론, ⁋명제 6](/ko/math/lie_theory/representations_of_sl2#prop6)), 유한차원 표현에서 각 $$\lambda(h_i)$$가 음이 아닌 정수여야 함은 필연적이다. 다음 정리는 이 필요조건이 충분조건이기도 함을 보인다.

<div class="proposition" markdown="1">

<ins id="thm12">**정리 12 (최고 무게 정리)**</ins> $$\mathfrak{g}$$가 유한차원 semisimple Lie algebra이면, 대응 $$\lambda\mapsto L(\lambda)$$는 dominant integral weight들의 집합에서 $$\mathfrak{g}$$의 유한차원 기약 표현들의 동형류 집합으로 가는 전단사이다. 곧 모든 유한차원 기약 표현은 어떤 dominant integral weight $$\lambda$$에 대한 $$L(\lambda)$$와 동형이며, 서로 다른 dominant integral weight는 서로 동형이 아닌 기약 표현을 준다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

증명은 세 부분으로 이루어진다. 첫째, 유한차원 기약 표현이 dominant integral highest weight를 가짐을 보인다. 둘째, dominant integral $$\lambda$$에 대하여 $$L(\lambda)$$가 유한차원임을 보인다. 셋째, 단사성과 전사성을 정리한다.

(1) $$V$$를 $$0$$이 아닌 유한차원 기약 표현이라 하자. $$V$$는 weight module이다. 실제로 $$\mathfrak{g}$$가 semisimple이므로 Cartan subalgebra의 각 원소는 $$V$$ 위에서 반단순하게 작용하고 $$\mathfrak{h}$$가 abelian이므로 동시 대각화되어, $$V=\bigoplus_\mu V_\mu$$이다. $$V$$가 유한차원이므로 weight들 가운데 어떤 positive root를 더해도 다시 weight가 되지 않는 극대 weight $$\lambda$$가 존재한다. 이러한 $$\lambda$$의 $$0$$이 아닌 벡터 $$v\in V_\lambda$$는 [명제 3](#prop3)에 의해 $$\mathfrak{n}^+\cdot v\subseteq\bigoplus_{\alpha\in\Phi^+}V_{\lambda+\alpha}=0$$을 만족하므로 highest weight vector이다. $$V$$가 기약이므로 $$v$$가 $$V$$를 생성하고, [명제 10](#prop10)에 의해 $$V\cong L(\lambda)$$이다. 이제 각 simple root $$\alpha_i$$에 대하여 $$\sl_{2,\alpha_i}=\langle e_i,f_i,h_i\rangle$$의 작용으로 $$V$$를 $$\sl_2$$-가군으로 보면, $$e_i\cdot v=0$$이고 $$h_i\cdot v=\lambda(h_i)v$$이므로 $$v$$는 이 $$\sl_2$$-가군의 highest weight vector이다. $$V$$가 유한차원이므로 $$\sl_2$$ 표현론 ([§sl₂의 표현론, ⁋명제 6](/ko/math/lie_theory/representations_of_sl2#prop6))에 의해 그 highest weight $$\lambda(h_i)$$는 음이 아닌 정수이다. 따라서 $$\lambda$$는 dominant integral이다.

(2) 역으로 $$\lambda$$가 dominant integral이라 하고 $$L(\lambda)$$가 유한차원임을 보인다. $$L(\lambda)$$의 생성 highest weight vector를 $$v$$라 하고 각 $$i$$에 대하여 $$n_i=\lambda(h_i)\in\mathbb{Z}_{\geq 0}$$이라 두자. 핵심은 벡터 $$f_i^{\,n_i+1}\cdot v$$가 $$0$$이라는 것이다. 이를 보이기 위해 $$\sl_{2,\alpha_i}$$-부분작용만을 본다. $$v$$는 $$e_i\cdot v=0$$, $$h_i\cdot v=n_i v$$를 만족하는 $$\sl_{2,\alpha_i}$$-highest weight vector이고, $$j\neq i$$인 다른 simple root vector $$e_j$$에 대해서는 $$e_j$$가 $$f_i^{\,m}\cdot v$$를 어떻게 옮기는지를 따져야 한다. $$\alpha_i$$가 simple root이므로 $$j\neq i$$이면 $$\alpha_i-\alpha_j$$는 root가 아니어서 $$[e_j,f_i]\in\mathfrak{g}_{\alpha_j-\alpha_i}=0$$, 곧 $$e_j$$와 $$f_i$$가 교환한다. 따라서

$$e_j\cdot\bigl(f_i^{\,m}\cdot v\bigr)=f_i^{\,m}\cdot(e_j\cdot v)=0\qquad(j\neq i)$$

이고, $$w=f_i^{\,n_i+1}\cdot v$$는 모든 $$e_j$$ ($$j\neq i$$)에 의해 소멸된다. 한편 $$\sl_{2,\alpha_i}$$ 안에서 [§sl₂의 표현론, ⁋명제 4](/ko/math/lie_theory/representations_of_sl2#prop4)를 highest weight $$n_i$$의 사슬에 적용하면

$$e_i\cdot\bigl(f_i^{\,n_i+1}\cdot v\bigr)=(n_i+1)\,(n_i-n_i)\,f_i^{\,n_i}\cdot v=0$$

이므로 $$w$$는 $$e_i$$에 의해서도 소멸된다. 곧 $$w$$는 모든 simple root vector에 의해 죽으므로 $$\mathfrak{n}^+\cdot w=0$$이고, $$w$$가 $$0$$이 아니라면 weight $$\lambda-(n_i+1)\alpha_i$$의 highest weight vector가 된다. 그러나 $$L(\lambda)$$가 기약이면서 highest weight $$\lambda$$를 가지므로 [명제 10](#prop10)에 의해 highest weight는 $$\lambda$$ 하나뿐이고 $$\lambda-(n_i+1)\alpha_i\neq\lambda$$이므로 $$w=0$$이어야 한다. 따라서 각 $$i$$에 대하여 $$f_i^{\,n_i+1}\cdot v=0$$이다.

이제 유한차원성을 본다. $$L(\lambda)$$의 weight들의 집합 $$P(\lambda)$$는 [명제 7](#prop7)에 의해 $$\lambda-\sum_k m_k\beta_k$$ 꼴로 아래로 유계이고, 방금 본 $$f_i^{\,n_i+1}\cdot v=0$$은 각 $$\sl_{2,\alpha_i}$$-방향 사슬이 유한 길이에서 닫힘을 뜻한다. $$P(\lambda)$$가 Weyl group 작용에 대해 불변임을 보이면 유한성이 따라온다. 각 simple reflection $$s_i$$에 대하여, $$L(\lambda)$$를 $$\sl_{2,\alpha_i}$$-가군으로 분해하면 [§sl₂의 표현론, ⁋정리 9](/ko/math/lie_theory/representations_of_sl2#thm9)에 의해 유한차원 $$\sl_2$$-가군들의 직합이고, $$\sl_2$$의 각 기약 성분의 weight 집합이 $$h_i$$의 고윳값 $$\mapsto$$ 그 음수로 보내는 대칭에 대해 닫혀 있으므로, $$\mu\in P(\lambda)$$이면 $$s_i(\mu)=\mu-\mu(h_i)\alpha_i\in P(\lambda)$$이고 그 multiplicity도 보존된다. simple reflection들이 Weyl group $$W$$를 생성하므로 ([§근계, ⁋정의 17](/ko/math/lie_theory/root_systems#def17)) $$P(\lambda)$$는 $$W$$-불변이다. 임의의 weight는 $$W$$-작용으로 dominant chamber 안의 weight로 옮길 수 있고, $$\lambda$$ 아래의 dominant weight는 유한 개뿐이므로 $$P(\lambda)$$는 유한집합이다. 각 weight space가 유한차원이므로 ([명제 7](#prop7)) $$L(\lambda)=\bigoplus_{\mu\in P(\lambda)}L(\lambda)_\mu$$는 유한차원이다.

(3) 단사성과 전사성을 정리한다. (1)에서 모든 $$0$$이 아닌 유한차원 기약 표현이 어떤 dominant integral $$\lambda$$에 대한 $$L(\lambda)$$와 동형임을 보였으므로 대응 $$\lambda\mapsto L(\lambda)$$는 전사이다. (2)에서 dominant integral $$\lambda$$마다 $$L(\lambda)$$가 실제로 유한차원 기약 표현임을 보였으므로 이 대응은 잘 정의된다. 단사성은 [명제 10](#prop10)에서 $$L(\mu)\cong L(\lambda)$$이면 $$\mu=\lambda$$임을 이미 보였으므로 성립한다. 따라서 대응은 전단사이다.

</details>

증명의 핵심은 각 simple root 방향에서 표현을 $$\sl_{2,\alpha_i}$$-가군으로 잘라 $$\sl_2$$의 표현론을 적용하는 데에 있다. dominant integral 조건 $$\lambda(h_i)\in\mathbb{Z}_{\geq 0}$$은 각 방향의 highest weight 사슬이 $$\sl_2$$에서처럼 음이 아닌 정수 단계에서 닫히도록 강제하며, 이것이 무한차원이던 $$M(\lambda)$$의 기약 몫 $$L(\lambda)$$를 유한차원으로 떨어뜨린다. Weyl group 대칭이 이렇게 잘린 유한한 weight 집합을 하나로 묶어 표현 전체의 유한차원성을 보장한다. 

이 정리로 semisimple Lie algebra의 유한차원 표현론은 완결된 그림을 얻는다. Weyl 완전가약성 ([§Weyl 완전가약성 정리, ⁋정리 7](/ko/math/lie_theory/weyl_complete_reducibility#thm7))에 의해 임의의 유한차원 표현은 기약 표현들의 직합이고, 그 기약 인자들은 정리 12에 의해 dominant integral weight들로 색인된다. 따라서 임의의 유한차원 표현은 각 dominant integral weight $$\lambda$$에 대한 $$L(\lambda)$$의 multiplicity로 완전히 결정되며, 표현론의 모든 질문은 이 multiplicity를 계산하는 문제로 환원된다. $$\sl_2$$에서 모든 기약 표현이 음이 아닌 정수 $$n$$으로 색인되고 $$L(n)=V(n)$$이었던 것 ([§sl₂의 표현론, ⁋정의 5](/ko/math/lie_theory/representations_of_sl2#def5))이 이 일반적 그림의 가장 단순한 경우이다.

---

**참고문헌**

**[Hum]** J. E. Humphreys, *Introduction to Lie algebras and representation theory*, Graduate Texts in Mathematics, Springer, 1972.  
**[Hum2]** J. E. Humphreys, *Representations of semisimple Lie algebras in the BGG category $$\mathcal{O}$$*, Graduate Studies in Mathematics, American Mathematical Society, 2008.  
**[Kna]** A. W. Knapp, *Lie groups beyond an introduction*, 2nd ed., Progress in Mathematics, Birkhäuser, 2002.  
**[FH]** W. Fulton and J. Harris, *Representation theory: a first course*, Graduate Texts in Mathematics, Springer, 1991.  
