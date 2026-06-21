---
title: "유한차원 가환대수의 표현과 spectrum"
description: "유한차원 가환대수의 정규표현이 정의하는 연산자족의 동시 일반화고유공간 분해가 정확히 대수의 character들로 색인됨을 보이고, character와 maximal ideal, spectrum의 점 사이의 사전을 정리한다."
excerpt: "Character = 정규표현의 동시 고유값 = spectrum의 점"

categories: [Math / Representation Theory]
permalink: /ko/math/representation_theory/spectrum_of_finite_dimensional_algebras
sidebar: 
    nav: "representation_theory-ko"

date: 2026-06-15
weight: 3

published: false

---

앞선 두 글에서 우리는 finite group $$G$$의 표현을 group algebra $$\mathbb{C}[G]$$ 위의 module로 보아 분석하였다. 이번 글에서 우리는 대상을 group algebra가 아니라 임의의 유한차원 가환대수로 바꾸어, 대수 그 자체가 자기 위에 곱셈으로 작용하는 *정규표현*을 분석한다. 핵심적인 관찰은 다음의 세 가지 대상이 본질적으로 같다는 것이다. 첫째, 대수에서 ground field로 가는 algebra homomorphism인 *character*; 둘째, 정규표현이 정의하는 연산자들의 *동시 고유값*; 셋째, 대수의 *spectrum*을 이루는 점들. 우리는 이 사전을 정확히 서술하고 증명한다.

이 글에서 $$k$$는 field이고, $$A$$는 유한차원 unital $$k$$-algebra를 가리킨다. 차원은 항상 $$k$$ 위에서의 차원 $$\dim=\dim_k$$이며, 주된 결과를 다룰 때에는 $$A$$가 commutative이고 $$k$$가 algebraically closed임을 명시적으로 가정한다. $$A$$-algebra의 일반론은 [\[대수적 구조\] §대수](/ko/math/algebraic_structures/algebras)에서 다룬 것을 따르며, 특히 algebra homomorphism은 곱셈과 스칼라곱, 그리고 항등원을 보존하는 사상을 뜻한다.

## 정규표현

추상적으로 주어진 대수의 원소들을 다루는 한 가지 방법은, 각 원소를 어떤 벡터공간 위의 선형연산자로 실현한 뒤 그 연산자의 고유값이나 대각화 가능성과 같은 선형대수학적 정보를 묻는 것이다. 가장 자연스러운 실현은 대수가 자기 자신 위에 곱셈으로 작용하도록 두는 것이다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 유한차원 unital $$k$$-algebra $$A$$와 원소 $$a\in A$$에 대하여, *곱셈연산자<sub>multiplication operator</sub>* $$M_a:A\rightarrow A$$를

$$M_a(x)=ax$$

으로 정의한다. 이 때 $$a\mapsto M_a$$로 주어지는 표현 $$A\rightarrow \End_k(A)$$를 $$A$$의 *정규표현<sub>regular representation</sub>*이라 부른다.

</div>

여기서 $$\End_k(A)$$는 $$A$$를 단순히 유한차원 $$k$$-벡터공간으로 보았을 때의 $$k$$-선형 자기준동형사상들이 이루는 대수이다. 정규표현이 실제로 표현, 곧 unital algebra homomorphism이라는 것을 먼저 확인하자.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 대응 $$a\mapsto M_a$$는 injective unital $$k$$-algebra homomorphism $$A\hookrightarrow \End_k(A)$$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 각 $$M_a$$가 $$k$$-선형사상인 것은 $$A$$의 곱셈이 둘째 변수에 대해 $$k$$-bilinear이기 때문이다. 즉 임의의 $$\alpha\in k$$와 $$x,y\in A$$에 대하여

$$M_a(\alpha x+y)=a(\alpha x+y)=\alpha(ax)+ay=\alpha M_a(x)+M_a(y)$$

이다. 다음으로 대응 $$a\mapsto M_a$$가 $$k$$-선형인 것은 곱셈이 첫째 변수에 대해 $$k$$-bilinear이기 때문이며, 곱셈을 보존하는 것은 $$A$$의 결합법칙으로부터

$$M_{ab}(x)=(ab)x=a(bx)=M_a(M_b(x))$$

이 모든 $$x\in A$$에 대해 성립하여 $$M_{ab}=M_a\circ M_b$$이기 때문이다. 또 $$M_1(x)=1\cdot x=x$$이므로 $$M_1=\id_A$$이고, 따라서 항등원을 보존한다. 마지막으로 injectivity를 보이자. 만일 $$M_a=0$$이라면 특히

$$a=a\cdot 1=M_a(1)=0$$

이므로 $$a=0$$이다. 따라서 $$\ker(a\mapsto M_a)=0$$이고 대응은 injective이다.

</details>

명제 2에 의하여 우리는 $$A$$를 $$\End_k(A)$$의 부분대수와 동일시할 수 있으며, 추상적인 원소 $$a$$에 대한 질문을 구체적인 연산자 $$M_a$$에 대한 질문으로 번역할 수 있다. 만일 $$A$$가 commutative이라면 임의의 $$a,b\in A$$에 대하여 $$ab=ba$$이므로 $$M_aM_b=M_{ab}=M_{ba}=M_bM_a$$이고, 따라서 연산자족 $$\{M_a\}_{a\in A}$$는 서로 commute하는 연산자들의 모임이다. 이러한 가환 연산자족은 선형대수학에서 잘 알려진 대로 좋은 동시분해를 가지며, 이 분해를 대수적으로 해석하는 것이 이 글의 목표이다.

## Character와 maximal ideal

연산자 $$M_a$$의 고유값을 추적하는 가장 작은 표현은 $$1$$차원 표현, 곧 대수에서 ground field로 가는 준동형사상이다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 유한차원 unital $$k$$-algebra $$A$$의 *character* $$\chi$$는 unital $$k$$-algebra homomorphism $$\chi:A\rightarrow k$$이다. 즉 $$\chi$$는 $$k$$-선형이며 모든 $$a,b\in A$$에 대해 $$\chi(ab)=\chi(a)\chi(b)$$, 그리고 $$\chi(1)=1$$을 만족한다.

</div>

Character는 정확히 $$A$$의 $$1$$차원 표현에 해당한다. $$1$$차원 벡터공간 위의 표현 $$A\rightarrow \End_k(k)=k$$는 곧 algebra homomorphism $$A\rightarrow k$$이기 때문이다. Character의 kernel은 다음과 같이 대수의 ideal 이론과 직접 연결된다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $$A$$의 임의의 character $$\chi:A\rightarrow k$$에 대하여, $$\ker\chi$$는 codimension $$1$$인 ideal이며 따라서 maximal ideal이고, 유도되는 사상

$$A/\ker\chi\xrightarrow{\ \cong\ } k$$

는 isomorphism이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\chi$$는 algebra homomorphism이므로 그 kernel $$\ker\chi$$는 $$A$$의 ideal이다. ([\[대수적 구조\] §대수, ⁋정의 10](/ko/math/algebraic_structures/algebras#def10)) $$\chi(1)=1\neq 0$$이므로 $$\chi$$는 nonzero이고, $$k$$가 field이므로 $$\chi$$는 surjective이다. 따라서 첫째 동형정리 ([\[대수적 구조\] §대수, ⁋명제 12](/ko/math/algebraic_structures/algebras#prop12))에 의하여

$$A/\ker\chi\cong \im\chi=k$$

이다. 우변이 $$k$$이므로 $$\ker\chi$$의 codimension은 $$\dim_k(A/\ker\chi)=\dim_k k=1$$이다. 마지막으로 $$A/\ker\chi\cong k$$가 field이므로 $$\ker\chi$$는 maximal ideal이다.

</details>

<div class="remark" markdown="1">

<ins id="rmk5">**참고 5**</ins> 여기에서 정의한 character는 [§유한군의 표현론](/ko/math/representation_theory/representations_of_finite_groups)과 [§표현의 지표](/ko/math/representation_theory/character_theory)에서 다룬 *지표*<sub>character</sub>와 이름은 같으나 일반적으로는 서로 다른 개념이다. 후자는 표현 $$\rho:G\rightarrow \Aut(V)$$에 대하여 각 $$g$$를 $$\tr\rho(g)$$로 보내는 함수 $$\rchi_\rho:G\rightarrow k$$, 곧 trace character이다 ([§표현의 지표, ⁋정의 1](/ko/math/representation_theory/character_theory#def1)). 이는 일반적으로 곱셈을 보존하지 않으므로 algebra homomorphism이 아니다. 두 개념이 일치하는 것은 표현이 $$1$$차원일 때이다. $$1$$차원 표현 $$\rho:G\rightarrow k^\times$$에 대하여 $$\tr\rho(g)=\rho(g)$$이고, 이를 group algebra 위로 선형확장한 $$\mathbb{C}[G]\rightarrow k$$는 곱셈을 보존하므로, 정의 3의 의미에서 $$\mathbb{C}[G]$$의 character가 된다. 실제로 $$A=\mathbb{C}[G]$$의 character $$\mathbb{C}[G]\rightarrow \mathbb{C}$$들은 정확히 $$G$$의 $$1$$차원 표현들과 일대일로 대응되는데, 이는 group algebra의 universal property ([\[대수적 구조\] §대수, ⁋명제 6](/ko/math/algebraic_structures/algebras#prop6))로부터 algebra homomorphism $$\mathbb{C}[G]\rightarrow \mathbb{C}$$들이 group homomorphism $$G\rightarrow \mathbb{C}^\times$$들과 대응되기 때문이다.

</div>

명제 4가 보여 주듯, character는 항상 maximal ideal을 낳는다. 그 역, 곧 모든 maximal ideal이 character로부터 온다는 것은 $$k$$가 algebraically closed일 때 성립하며, 이는 character와 maximal ideal을 동일시할 수 있게 해 준다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> $$k$$가 algebraically closed이고 $$A$$가 유한차원 commutative $$k$$-algebra라 하자. 그럼 대응

$$\chi\longmapsto \ker\chi$$

는 $$A$$의 character들의 집합과 $$A$$의 maximal ideal들의 집합 사이의 전단사이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

먼저 이 대응이 surjective임을 보이자. $$\mathfrak{m}$$을 $$A$$의 임의의 maximal ideal이라 하면 $$A/\mathfrak{m}$$은 field이다. $$A$$가 유한차원이므로 $$A/\mathfrak{m}$$ 또한 $$k$$ 위에서 유한차원이고, 따라서 $$A/\mathfrak{m}$$은 $$k$$의 finite field extension이다. 그런데 $$k$$가 algebraically closed이므로 $$k$$의 finite extension은 $$k$$ 자신뿐이며, 따라서 자연스러운 포함 $$k\hookrightarrow A/\mathfrak{m}$$은 isomorphism $$A/\mathfrak{m}\cong k$$이다. 이는 [\[가환대수학\] §영점정리](/ko/math/commutative_algebra/nullstellensatz)에서 사용한 Zariski의 보조정리의 특수한 경우이기도 하다. 이제 합성

$$\chi:A\xrightarrow{\ \pi\ } A/\mathfrak{m}\xrightarrow{\ \cong\ } k$$

는 unital algebra homomorphism, 곧 character이며, $$\ker\chi=\ker\pi=\mathfrak{m}$$이다.

다음으로 injectivity를 보이자. 두 character $$\chi,\chi'$$가 $$\ker\chi=\ker\chi'=:\mathfrak{m}$$을 만족한다 하자. 명제 4에 의하여 둘 다 isomorphism $$A/\mathfrak{m}\cong k$$를 유도하며, 이 두 isomorphism $$\bar\chi,\bar\chi'$$은 모두 $$k$$의 image $$1+\mathfrak{m}$$을 $$1$$로 보낸다. $$A/\mathfrak{m}\cong k$$가 $$1+\mathfrak{m}$$으로 $$k$$-벡터공간으로서 생성되므로 $$k$$-선형사상 $$\bar\chi,\bar\chi'$$은 일치하고, 따라서 $$\chi=\bar\chi\circ\pi=\bar\chi'\circ\pi=\chi'$$이다.

</details>

명제 6에서 commutativity는 maximal ideal $$\mathfrak{m}$$에 대해 $$A/\mathfrak{m}$$이 commutative field가 되도록 하는 데 사용되었고, algebraically closed 가정은 그 extension이 $$k$$로 붕괴되도록 하는 데 사용되었다. 두 가정 중 하나라도 빠지면 maximal ideal이 반드시 character를 낳지는 않는다. 가령 $$k=\mathbb{R}$$ 위의 $$A=\mathbb{C}$$에서 $$(0)$$은 maximal ideal이지만 $$A/(0)=\mathbb{C}$$는 $$\mathbb{R}$$이 아니므로 character를 정의하지 않는다.

## 동시 일반화고유공간 분해

이제 우리는 commutative한 경우의 주된 정리로 향한다. $$A$$가 commutative이면 $$\{M_a\}_{a\in A}$$는 가환 연산자족이고, $$k$$가 algebraically closed이면 이 족은 동시에 삼각화될 수 있어 좋은 분해를 가진다. 그 분해의 색인이 정확히 character임을 보이는 것이 목표이다.

준비로 한 가지 선형대수학적 사실을 정리한다. 유한차원 벡터공간 위의 가환 연산자족이 algebraically closed field 위에서 *동시 삼각화 가능*, 곧 적당한 basis에 대하여 모든 연산자가 동시에 상삼각행렬로 표현된다는 것은 표준적인 결과이다. 단일 연산자의 경우 algebraically closed field 위에서 고유값이 존재하여 삼각화가 가능하고, 가환족의 경우 공통 고유벡터의 존재로부터 차원에 대한 귀납법으로 동시 삼각화가 따라온다. 동시 삼각화가 주어지면, 각 연산자 $$M_a$$의 대각성분들은 그 고유값들이며, 가환성으로 인해 같은 대각위치에 놓이는 고유값들의 모임은 $$a$$에 대한 함수 $$\lambda:A\rightarrow k$$를 정의한다. 이러한 함수 $$\lambda$$로 색인되는 부분공간이 다음의 동시 일반화고유공간이다.

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> 유한차원 commutative $$k$$-algebra $$A$$와 함수 $$\lambda:A\rightarrow k$$에 대하여,

$$A_\lambda=\{x\in A\mid (M_a-\lambda(a)\id_A)^{\dim A}x=0\ \text{ for all }a\in A\}$$

을 $$\lambda$$에 대응하는 *동시 일반화고유공간<sub>simultaneous generalized eigenspace</sub>*이라 부른다.

</div>

각각의 $$a$$에 대하여 $$\ker(M_a-\lambda(a)\id_A)^{\dim A}$$은 연산자 $$M_a$$의 고유값 $$\lambda(a)$$에 대한 일반화고유공간이고, $$A_\lambda$$는 이들을 모든 $$a\in A$$에 대하여 교집합한 것이다. 지수 $$\dim A$$를 택한 이유는, 유한차원 벡터공간 위의 연산자에 대하여 일반화고유공간은 충분히 큰 거듭제곱의 kernel로 안정되며 그 안정점이 차원에 의해 위에서 제한되기 때문이다. $$A_\lambda$$가 $$0$$이 아닌 함수 $$\lambda$$들만이 의미를 가지며, 우리는 이들이 정확히 character임을 보인다.

<div class="proposition" markdown="1">

<ins id="thm8">**정리 8**</ins> $$k$$가 algebraically closed이고 $$A$$가 유한차원 commutative $$k$$-algebra라 하자. 그럼

$$A=\bigoplus_{\lambda} A_\lambda$$

이 성립한다. 여기서 합은 $$A_\lambda\neq 0$$인 함수 $$\lambda:A\rightarrow k$$들에 대하여 취하며, 이러한 $$\lambda$$들은 정확히 $$A$$의 character들이다. 따라서 각 $$a\in A$$에 대하여 연산자 $$M_a$$의 고유값들의 집합은 $$\{\chi(a)\mid \chi\text{ is a character of }A\}$$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

**분해의 존재.** $$\{M_a\}_{a\in A}$$는 [명제 2](#prop2)의 논의에 의하여 서로 commute하는 연산자족이다. $$k$$가 algebraically closed이므로 이 족은 동시 삼각화 가능하다. 동시 삼각화 basis를 택하여 각 $$M_a$$를 상삼각행렬로 보면, 그 대각성분들이 $$M_a$$의 고유값이다. 같은 대각위치 $$i$$에 대응하는 고유값을 $$a$$에 대한 함수로 모으면 함수 $$\lambda_i:A\rightarrow k$$를 얻는다. 서로 다른 $$\lambda_i$$들을 $$\lambda^{(1)},\ldots,\lambda^{(r)}$$이라 하자.

각 $$\lambda^{(s)}$$에 대하여 $$A_{\lambda^{(s)}}$$가 $$A$$의 부분공간임은 정의로부터 명백하다. 또한 단일 연산자에 대한 일반화고유공간 분해를 가환족에 적용하면 (각 $$M_a$$가 다른 모든 $$M_b$$와 commute하므로 서로의 일반화고유공간을 보존한다), 벡터공간 $$A$$는 동시 일반화고유공간들의 직합

$$A=\bigoplus_{s=1}^r A_{\lambda^{(s)}}$$

으로 분해되며, 위에 나타나지 않는 다른 함수 $$\lambda$$에 대해서는 $$A_\lambda=0$$이다. 실제로 $$A_\lambda\neq 0$$이려면 어떤 공통 일반화고유벡터가 모든 $$a$$에 대해 고유값 $$\lambda(a)$$를 가져야 하는데, 동시 삼각화에서 나타나는 공통 고유값의 묶음은 정확히 $$\lambda^{(1)},\ldots,\lambda^{(r)}$$뿐이기 때문이다.

**각 $$\lambda^{(s)}$$는 character.** 이제 고정된 $$\lambda=\lambda^{(s)}$$가 $$A_\lambda\neq 0$$을 만족한다 하고, $$\lambda$$가 character임을 보이자. 블록 $$A_\lambda$$ 위에서 각 $$M_a$$는 $$A_\lambda$$를 보존하므로 그 제한 $$M_a\vert_{A_\lambda}$$를 생각할 수 있고, 정의에 의하여 $$M_a\vert_{A_\lambda}-\lambda(a)\id$$은 nilpotent이다. 따라서

$$M_a\vert_{A_\lambda}=\lambda(a)\id+N_a,\qquad N_a:=M_a\vert_{A_\lambda}-\lambda(a)\id$$

이고 $$N_a$$는 nilpotent이다. 더욱이 $$M_a$$들이 서로 commute하므로 $$N_a$$들도 서로 commute한다. 한편 $$\lambda$$가 $$k$$-선형이라는 것은 대응 $$a\mapsto M_a$$가 $$k$$-선형 ([명제 2](#prop2))이라는 것과 고유값이 $$k$$-선형으로 추출된다는 것으로부터 따라온다. 구체적으로 임의의 $$\alpha\in k$$와 $$a,b\in A$$에 대하여

$$M_{\alpha a+b}\vert_{A_\lambda}=\alpha M_a\vert_{A_\lambda}+M_b\vert_{A_\lambda}=(\alpha\lambda(a)+\lambda(b))\id+(\alpha N_a+N_b)$$

이고 우변의 nilpotent 부분 $$\alpha N_a+N_b$$은 $$\lambda(\alpha a+b)\id$$을 뺀 나머지여야 하므로, 일반화고유값의 유일성으로부터 $$\lambda(\alpha a+b)=\alpha\lambda(a)+\lambda(b)$$이다.

곱셈을 보존함을 보이자. 블록 위에서

$$\begin{aligned}
M_{ab}\vert_{A_\lambda}&=M_a\vert_{A_\lambda}\,M_b\vert_{A_\lambda}=(\lambda(a)\id+N_a)(\lambda(b)\id+N_b)\\
&=\lambda(a)\lambda(b)\id+\bigl(\lambda(a)N_b+\lambda(b)N_a+N_aN_b\bigr)
\end{aligned}$$

이다. 여기서 $$N_a,N_b$$가 서로 commute하는 nilpotent이므로 $$\lambda(a)N_b+\lambda(b)N_a+N_aN_b$$ 또한 nilpotent이다. 서로 commute하는 nilpotent 연산자들의 $$k$$-선형결합과 곱은 다시 nilpotent이기 때문이다. 그런데 정의에 의하여 $$M_{ab}\vert_{A_\lambda}-\lambda(ab)\id$$ 역시 nilpotent이므로, 두 표현

$$M_{ab}\vert_{A_\lambda}=\lambda(ab)\id+(\text{nilpotent})=\lambda(a)\lambda(b)\id+(\text{nilpotent})$$

을 비교하면 $$(\lambda(ab)-\lambda(a)\lambda(b))\id$$이 nilpotent이어야 하고, 스칼라 배 $$c\,\id$$이 nilpotent인 것은 $$c=0$$일 때뿐이므로 $$\lambda(ab)=\lambda(a)\lambda(b)$$이다. 마지막으로 $$M_1=\id_A$$이므로 블록 위에서 $$M_1\vert_{A_\lambda}=\id$$, 곧 $$\lambda(1)=1$$이다. 따라서 $$\lambda$$는 unital algebra homomorphism, 곧 character이다.

**역으로 모든 character가 나타남.** $$\chi$$를 $$A$$의 임의의 character라 하자. $$\chi$$를 위 분해에 적용하기 위하여, $$\chi$$가 어떤 블록 위에서 일반화고유값으로 실현됨을 보이면 된다. 각 $$a$$에 대하여 $$M_a-\chi(a)\id_A$$의 행렬식을 생각하면, 이는 $$A/\ker\chi\cong k$$ 위에서 $$M_a$$가 스칼라 $$\chi(a)$$로 작용한다는 사실로부터 가역이 아니다. 더 구체적으로, [명제 6](#prop6)에 의하여 $$\chi$$는 maximal ideal $$\mathfrak{m}=\ker\chi$$에 대응하고, $$\mathfrak{m}$$을 보존하는 분해의 한 블록이 정확히 $$\chi$$를 일반화고유값으로 갖는다. 따라서 $$\chi=\lambda^{(s)}$$인 $$s$$가 존재한다. 결국 $$A_\lambda\neq 0$$인 $$\lambda$$들의 집합은 character들의 집합과 일치한다.

**고유값에 관한 결론.** 동시 삼각화에서 $$M_a$$의 대각성분, 곧 고유값들은 정확히 $$\lambda^{(1)}(a),\ldots,\lambda^{(r)}(a)$$이고, 이들이 character들에서의 값 $$\chi(a)$$이므로 $$M_a$$의 고유값 집합은 $$\{\chi(a)\mid \chi\text{ character}\}$$이다.

</details>

정리 8은 추상적인 대수의 원소 $$a$$를 연산자 $$M_a$$로 실현했을 때, 그 고유값들이 character들의 값으로 완전히 결정됨을 말해 준다. 이는 단일 연산자의 고유값 이론을 대수 전체의 character 이론으로 일반화한 것으로 볼 수 있다. 다음 절에서 우리는 이 분해를 더 정교하게 다듬어, 분해가 대수적으로도 곱대수 구조를 준다는 것을 본다.

## 구조분해와 reduced 대수

정리 8의 직합 분해는 단순한 벡터공간 분해가 아니라 대수의 분해이기도 하다. 이를 정리하기 위해 직합 분해에 따르는 idempotent들을 도입한다.

<div class="proposition" markdown="1">

<ins id="cor9">**따름정리 9**</ins> [정리 8](#thm8)의 가정 하에서, 각 character $$\chi$$에 대응하는 부분공간 $$A_\chi$$는 $$A$$의 ideal이며, 적당한 원소들 $$e_\chi\in A_\chi$$가 존재하여

$$e_\chi e_{\chi'}=\delta_{\chi\chi'}e_\chi,\qquad \sum_\chi e_\chi=1$$

을 만족한다. 이 때 $$A_\chi=e_\chi A$$이고, 곱셈을 통해

$$A\cong \prod_\chi A_\chi$$

이 성립한다. 또한 각 $$A_\chi$$는 유일한 maximal ideal $$\mathfrak{n}_\chi=\{x\in A_\chi\mid \chi(x)=0\}$$을 갖는 local algebra이고 $$\mathfrak{n}_\chi$$의 모든 원소는 nilpotent이며,

$$\dim A=\sum_\chi \dim A_\chi$$

이고 character의 개수는 $$\dim A$$ 이하이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

각 $$A_\chi$$가 ideal임을 보이자. $$x\in A_\chi$$이고 $$b\in A$$라 하자. $$M_b$$는 다른 모든 $$M_a$$와 commute하므로 $$A_\chi$$를 보존한다. 즉 $$bx=M_b(x)\in A_\chi$$이며, 따라서 $$A_\chi$$는 ideal이다.

[정리 8](#thm8)의 직합 분해 $$A=\bigoplus_\chi A_\chi$$에서 $$1\in A$$를 성분별로 분해하여 $$1=\sum_\chi e_\chi$$라 쓰자. 여기서 $$e_\chi\in A_\chi$$이다. 임의의 $$x\in A_{\chi'}$$에 대하여 $$x=1\cdot x=\sum_\chi e_\chi x$$인데, $$A_\chi$$가 ideal이므로 $$e_\chi x\in A_\chi\cap A_{\chi'}$$이고, 직합이므로 $$\chi\neq\chi'$$이면 $$A_\chi\cap A_{\chi'}=0$$이다. 따라서 $$e_\chi x=0$$ ($$\chi\neq\chi'$$) 이고 $$e_{\chi'}x=x$$이다. 특히 $$x=e_{\chi'}$$로 두면 $$e_{\chi'}e_{\chi'}=e_{\chi'}$$, $$x=e_\chi$$ ($$\chi\neq \chi'$$) 로 두면 $$e_{\chi'}e_\chi=0$$을 얻으므로 $$e_\chi e_{\chi'}=\delta_{\chi\chi'}e_\chi$$이다. 또 위 계산은 $$e_{\chi'}$$이 $$A_{\chi'}$$ 위에서 항등원처럼 작용함을 보이므로 $$A_{\chi'}=e_{\chi'}A$$이고, 각 $$A_\chi$$는 항등원 $$e_\chi$$를 갖는 unital algebra이다. 사상

$$A\longrightarrow \prod_\chi A_\chi;\qquad x\longmapsto (e_\chi x)_\chi$$

은 위 idempotent 관계에 의하여 algebra homomorphism이고 ([\[대수적 구조\] §대수의 직접곱, 직합, 텐서곱, ⁋명제 1](/ko/math/algebraic_structures/operations_of_algebras#prop1)), $$x=\sum_\chi e_\chi x$$로부터 역사상 $$(x_\chi)_\chi\mapsto \sum_\chi x_\chi$$이 존재하므로 isomorphism이다.

각 $$A_\chi$$가 local임을 보이자. 블록 $$A_\chi$$ 위에서 [정리 8](#thm8)의 증명에 의해 $$M_a\vert_{A_\chi}=\chi(a)\id+N_a$$이고 $$N_a$$는 nilpotent이다. 특히 $$a\in A_\chi$$에 대하여 $$\chi(a)$$가 $$0$$이면 $$M_a\vert_{A_\chi}=N_a$$이 nilpotent이고, $$a=M_a\vert_{A_\chi}(e_\chi)$$이므로 $$a$$ 자신이 nilpotent이다. 따라서 $$\mathfrak{n}_\chi=\{x\in A_\chi\mid \chi(x)=0\}$$의 모든 원소는 nilpotent이다. 반대로 $$\chi(a)\neq 0$$이면 $$M_a\vert_{A_\chi}=\chi(a)\id+N_a=\chi(a)(\id+\chi(a)^{-1}N_a)$$이고 괄호 안의 연산자는 nilpotent를 더한 항등원이므로 가역이다. 즉 $$a$$는 $$A_\chi$$에서 unit이다. 결국 $$A_\chi$$의 nonunit들은 정확히 $$\mathfrak{n}_\chi$$를 이루므로 $$\mathfrak{n}_\chi$$가 유일한 maximal ideal이고 $$A_\chi$$는 local이다.

마지막으로 직합 분해로부터 $$\dim A=\sum_\chi \dim A_\chi$$이고, 각 $$A_\chi\neq 0$$이므로 $$\dim A_\chi\geq 1$$이다. 따라서 character의 개수는 $$\sum_\chi 1\leq \sum_\chi \dim A_\chi=\dim A$$ 이하이다.

</details>

따름정리 9는 정리 8의 분해가 곧 대수의 구조분해 $$A\cong\prod_\chi A_\chi$$임을 보여 준다. 각 블록 $$A_\chi$$는 하나의 character를 갖는 local algebra로, character의 "위치"와 그 위에 얹힌 nilpotent 정보 $$\mathfrak{n}_\chi$$로 이루어진다. 분해가 $$1$$차원 블록들로, 곧 nilpotent 부분 없이 깔끔하게 떨어지는 경우를 따로 정의한다.

<div class="definition" markdown="1">

<ins id="def10">**정의 10**</ins> 대수 $$A$$가 *reduced<sub>감약</sub>*라는 것은 $$A$$의 nonzero nilpotent 원소가 존재하지 않는 것, 곧 $$a^n=0$$이면 $$a=0$$인 것이다.

</div>

reduced라는 조건은 정리 8의 분해에서 nilpotent 부분이 완전히 사라지는 것과 동치이며, 이는 다시 정규표현이 동시대각화 가능하다는 선형대수학적 조건과 같다.

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> $$k$$가 algebraically closed이고 $$A$$가 유한차원 commutative $$k$$-algebra이며 $$N=\dim A$$라 하자. 다음 네 조건이 동치이다.

1. $$A$$는 reduced이다.
2. 모든 character $$\chi$$에 대하여 $$A_\chi=k\,e_\chi$$, 곧 $$\mathfrak{n}_\chi=0$$이다.
3. character의 개수가 정확히 $$N$$이며, $$A\cong k^N$$이다.
4. 정규표현 $$\{M_a\}_{a\in A}$$이 동시대각화 가능하다.

이 때 각 idempotent $$e_\chi$$는 모든 $$M_a$$의 공통 고유벡터이며 $$M_a e_\chi=\chi(a)e_\chi$$를 만족한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

**(1) $$\Rightarrow$$ (2).** $$A$$가 reduced라 하자. [따름정리 9](#cor9)에 의하여 $$\mathfrak{n}_\chi$$의 모든 원소는 nilpotent이고, $$A$$에 nonzero nilpotent가 없으므로 $$\mathfrak{n}_\chi=0$$이다. 따라서 $$A_\chi$$는 maximal ideal이 $$0$$인 local algebra, 곧 field이고 동시에 $$k$$-algebra이며 $$A_\chi/\mathfrak{n}_\chi=A_\chi\cong k$$이므로 $$A_\chi=k\,e_\chi$$이다.

**(2) $$\Rightarrow$$ (3).** $$A_\chi=k\,e_\chi$$이면 $$\dim A_\chi=1$$이므로 [따름정리 9](#cor9)의 $$\dim A=\sum_\chi\dim A_\chi$$로부터 character의 개수는 $$\sum_\chi 1=\dim A=N$$이다. 또 $$A\cong\prod_\chi A_\chi\cong\prod_\chi k=k^N$$이다.

**(3) $$\Rightarrow$$ (4).** $$A\cong k^N$$의 정규표현을 생각하자. $$k^N$$에서 곱셈은 성분별이므로 표준 basis $$\{\varepsilon_1,\ldots,\varepsilon_N\}$$ (각 $$\varepsilon_i$$는 $$i$$번째 성분만 $$1$$) 에 대하여 임의의 $$a=(a_1,\ldots,a_N)$$의 곱셈연산자 $$M_a$$는 $$M_a\varepsilon_i=a_i\varepsilon_i$$로 작용한다. 즉 모든 $$M_a$$가 이 공통 basis에 대해 동시에 대각행렬이므로 정규표현은 동시대각화 가능하다.

**(4) $$\Rightarrow$$ (1).** 정규표현이 동시대각화 가능하다 하자. 그럼 각 $$M_a$$가 대각화 가능하므로 nilpotent가 아닌 한 $$0$$이 아닌 고유값을 가지며, 특히 어떤 $$a$$에 대해 $$M_a$$가 nilpotent라면 $$M_a=0$$이다. [명제 2](#prop2)에 의해 $$a\mapsto M_a$$가 injective이므로 $$M_a=0$$은 $$a=0$$을 뜻한다. 따라서 $$a^n=0$$이면 $$M_a^n=M_{a^n}=0$$이고 $$M_a$$가 nilpotent이므로 $$M_a=0$$, 곧 $$a=0$$이다. 따라서 $$A$$는 reduced이다.

마지막 주장은 (3)의 증명에서 본 대각화에서 $$\varepsilon_i$$가 $$e_{\chi}$$에 해당하고 $$M_a e_\chi=\chi(a)e_\chi$$임을 관찰하면 된다. 실제로 일반적인 경우에도 [따름정리 9](#cor9)의 idempotent $$e_\chi$$에 대하여 $$a\,e_\chi\in A_\chi$$이고 $$a\,e_\chi=\chi(a)e_\chi+N_a(e_\chi)$$인데, reduced인 경우 $$N_a=0$$이므로 $$M_a e_\chi=\chi(a)e_\chi$$이다.

</details>

명제 11은 reduced인 가환대수가 정확히 정규표현이 동시대각화되는 경우, 곧 각 블록이 $$1\times 1$$로 떨어지는 경우임을 말해 준다. 이 경우 character의 개수는 차원과 정확히 같고, idempotent $$e_\chi$$들이 공통 고유벡터들의 basis를 이룬다. 일반적인 경우와의 차이는 오직 nilpotent 부분 $$\mathfrak{n}_\chi$$의 존재 여부이다.

## Spectrum

지금까지의 사전을 기하학적인 언어로 다시 쓰면, character들은 대수의 "점"을 이루고 대수는 그 점들 위의 함수환처럼 행동한다.

<div class="definition" markdown="1">

<ins id="def12">**정의 12**</ins> 유한차원 commutative $$k$$-algebra $$A$$에 대하여, $$A$$의 character들의 집합을 $$A$$의 *maximal spectrum* $$\Specm A$$라 부른다.

</div>

$$k$$가 algebraically closed일 때, [명제 6](#prop6)에 의하여 $$\Specm A$$는 $$A$$의 maximal ideal들의 집합과 동일시되며, [따름정리 9](#cor9)에 의하여 유한집합이다. 각 점 $$\chi\in\Specm A$$에는 $$\dim A_\chi$$라는 양의 정수가 따라붙는데, 이를 점 $$\chi$$의 *multiplicity*라 부른다. 그럼 $$\dim A=\sum_\chi\dim A_\chi$$는 점들의 multiplicity를 모두 합한 것이다. 각 원소 $$a\in A$$는 character에서의 값들을 통해 $$\Specm A$$ 위의 함수로 볼 수 있으며, 이를 정식화하면 다음을 얻는다.

<div class="proposition" markdown="1">

<ins id="prop13">**명제 13**</ins> $$k$$가 algebraically closed이고 $$A$$가 유한차원 commutative $$k$$-algebra라 하자. 평가사상

$$\ev:A\longrightarrow k^{\Specm A};\qquad a\longmapsto (\chi(a))_{\chi\in\Specm A}$$

은 unital $$k$$-algebra homomorphism이고, 그 kernel은 $$A$$의 nilradical, 곧 nilpotent 원소들의 집합 $$\bigcap_\chi\mathfrak{m}_\chi$$이다. 따라서 $$\ev$$이 injective인 것과 $$A$$가 reduced인 것이 동치이며, 이 경우 $$\ev$$은 isomorphism $$A\cong k^{\Specm A}$$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\ev$$은 각 성분이 character $$\chi$$이므로 algebra homomorphism들의 곱이고, 따라서 그 자체로 algebra homomorphism이다. ([\[대수적 구조\] §대수의 직접곱, 직합, 텐서곱, ⁋명제 2](/ko/math/algebraic_structures/operations_of_algebras#prop2)) 또 각 $$\chi(1)=1$$이므로 $$\ev(1)=(1,\ldots,1)$$은 $$k^{\Specm A}$$의 항등원이고 $$\ev$$은 unital이다.

kernel을 계산하자. $$\ev(a)=0$$인 것은 모든 character $$\chi$$에 대하여 $$\chi(a)=0$$, 곧 $$a\in\bigcap_\chi\ker\chi=\bigcap_\chi\mathfrak{m}_\chi$$인 것과 같다. 이제 이 교집합이 정확히 nilpotent 원소들의 집합임을 보이자. [따름정리 9](#cor9)의 isomorphism $$A\cong\prod_\chi A_\chi$$에서 $$a=(a_\chi)_\chi$$로 쓰면, $$\chi'(a)$$는 $$a_{\chi'}$$의 $$A_{\chi'}\rightarrow A_{\chi'}/\mathfrak{n}_{\chi'}\cong k$$에서의 image이다. 따라서 모든 $$\chi$$에 대하여 $$\chi(a)=0$$인 것은 각 성분 $$a_\chi$$가 $$\mathfrak{n}_\chi$$에 속하는 것과 같다. 그런데 [따름정리 9](#cor9)에 의하여 $$\mathfrak{n}_\chi$$의 원소는 모두 nilpotent이고, 곱이 성분별이므로 $$(a_\chi)_\chi$$이 nilpotent인 것은 각 $$a_\chi$$가 nilpotent인 것, 곧 각 $$a_\chi\in\mathfrak{n}_\chi$$인 것과 동치이다. 따라서 $$\ker\ev$$은 정확히 $$A$$의 nilpotent 원소들의 집합이다.

그러므로 $$\ev$$이 injective인 것은 $$A$$에 nonzero nilpotent가 없는 것, 곧 $$A$$가 reduced인 것과 동치이다. 마지막으로 $$A$$가 reduced이면 [명제 11](#prop11)에 의하여 character의 개수가 $$\dim A$$와 같으므로 $$\dim k^{\Specm A}=\dim A$$이고, injective인 $$\ev$$은 차원 비교에 의하여 isomorphism이다.

</details>

명제 13은 reduced인 유한차원 가환대수가 정확히 그 유한한 점집합 $$\Specm A$$ 위의 $$k$$-값 함수환임을 말해 준다. 이는 가환 Banach algebra에 대한 Gelfand 표현의 유한차원 대수적 판본으로, character를 점으로, 대수의 원소를 점 위의 함수로 보는 관점을 정당화한다. nilpotent가 존재하는 일반적인 경우에는 $$\ev$$이 nilradical만큼의 정보를 잃으며, 그 손실분이 각 점 위의 nilpotent 두께 $$\mathfrak{n}_\chi$$로 나타난다.

## 예시

지금까지의 이론을 가장 단순하고 핵심적인 예시인 한 변수 다항식의 몫대수에서 확인하자. 이 예시는 단일 연산자의 고유값 이론이 이 사전의 특수한 경우임을 직접 보여 준다.

<div class="example" markdown="1">

<ins id="ex14">**예시 14**</ins> $$k$$가 algebraically closed이고 $$p(\x)\in k[\x]$$가 차수 $$n$$의 monic polynomial이라 하자. $$A=k[\x]/(p(\x))$$은 차원 $$n$$의 commutative $$k$$-algebra이다. $$k$$가 algebraically closed이므로

$$p(\x)=\prod_{i=1}^r(\x-c_i)^{m_i},\qquad \sum_{i=1}^r m_i=n$$

으로 서로 다른 근 $$c_1,\ldots,c_r$$에 대해 인수분해된다. 중국인의 나머지정리에 의하여

$$A\cong\prod_{i=1}^r k[\x]/\bigl((\x-c_i)^{m_i}\bigr)$$

이고, 각 인수 $$A_i=k[\x]/((\x-c_i)^{m_i})$$은 차원 $$m_i$$의 local algebra로 그 maximal ideal은 $$(\x-c_i)$$의 image가 생성하는 nilpotent ideal이다. $$A$$의 character는 각 인수에서 $$\x\mapsto c_i$$로 평가하는 것들, 곧 근 $$\{c_1,\ldots,c_r\}$$과 일대일로 대응하며, 이것이 정확히 $$\Specm A$$이다.

정규표현의 입장에서 $$M_\x:A\rightarrow A$$는 $$\x$$의 곱셈연산자이고, basis $$\{1,\x,\ldots,\x^{n-1}\}$$에 대하여 $$p$$의 companion matrix로 표현된다. 그 고유값은 $$p$$의 근 $$c_1,\ldots,c_r$$이며, 이는 [정리 8](#thm8)이 말하는 $$\{\chi(\x)\}$$과 정확히 일치한다. 점 $$c_i$$의 multiplicity는 $$\dim A_i=m_i$$, 곧 근의 중복도이다. 따라서 $$A$$가 reduced인 것은 모든 $$m_i=1$$인 것, 곧 $$p$$가 squarefree인 것과 동치이고, 이 경우 $$A\cong k^n$$이며 $$M_\x$$는 대각화 가능하다.

</div>

위 예시의 가장 작은 비자명한 경우들을 따로 떼어 보면 reduced와 non-reduced의 대비가 분명해진다.

<div class="example" markdown="1">

<ins id="ex15">**예시 15**</ins> $$A=k[\sigma]/(\sigma^2)$$을 생각하자. 여기서 $$p(\sigma)=\sigma^2=(\sigma-0)^2$$이므로 근은 $$0$$ 하나뿐이고 중복도는 $$2$$이다. 따라서 character는 $$\chi:\sigma\mapsto 0$$ 하나뿐이고 $$\Specm A$$는 한 점이다. $$M_\sigma$$는 basis $$\{1,\sigma\}$$에 대하여

$$M_\sigma=\begin{pmatrix}0&0\\1&0\end{pmatrix}$$

으로 nilpotent이며 대각화 불가능하다. $$\sigma$$ 자체가 nonzero nilpotent이므로 $$A$$는 reduced가 아니다. 그러나 [정리 8](#thm8)에 따라 $$M_\sigma$$의 유일한 고유값은 여전히 $$0=\chi(\sigma)$$이다. 즉 character가 고유값 정보를 잃지 않으면서도, 대각화 가능성이라는 추가 정보는 nilpotent 두께 $$\mathfrak{n}_\chi=k\sigma$$에 담겨 있다.

반면 $$\operatorname{char}k\neq 2$$인 $$k$$ 위에서 $$c\neq 0$$에 대해 $$A=k[\sigma]/(\sigma^2-c)$$를 생각하면, $$\sigma^2-c=(\sigma-\sqrt c)(\sigma+\sqrt c)$$이 서로 다른 두 근을 가지므로

$$A\cong k\times k$$

이고 character는 $$\sigma\mapsto \sqrt c$$와 $$\sigma\mapsto -\sqrt c$$ 둘이다. 이 경우 $$A$$는 reduced이고 $$M_\sigma$$는 고유값 $$\pm\sqrt c$$로 대각화된다.

</div>

마지막으로 첫 두 글에서 다룬 유한군의 표현론과의 다리를 놓는 예시를 본다.

<div class="example" markdown="1">

<ins id="ex16">**예시 16**</ins> 유한 abelian group $$\mathbb{Z}/n$$의 group algebra를 $$k=\mathbb{C}$$ 위에서 생각하자. 생성원 $$\sigma$$가 만족하는 유일한 관계는 $$\sigma^n=1$$이므로

$$\mathbb{C}[\mathbb{Z}/n]\cong\mathbb{C}[\sigma]/(\sigma^n-1)$$

이다. $$\mathbb{C}$$ 위에서 $$\sigma^n-1=\prod_{j=0}^{n-1}(\sigma-\zeta^j)$$ ($$\zeta=e^{2\pi i/n}$$) 은 서로 다른 $$n$$개의 근을 가지므로 squarefree이고, 따라서 [예시 14](#ex14)에 의하여

$$\mathbb{C}[\mathbb{Z}/n]\cong\mathbb{C}^n$$

이며 reduced이다. 그 $$n$$개의 character는 각각 $$\sigma\mapsto\zeta^j$$ ($$0\leq j<n$$) 로 주어지는데, 이는 정확히 $$\mathbb{Z}/n$$의 $$1$$차원 표현들, 곧 [§표현의 지표](/ko/math/representation_theory/character_theory)의 의미에서의 $$\mathbb{Z}/n$$의 (trace) character들이다. 즉 abelian group의 경우 두 종류의 character가 일치하며 ([참고 5](#rmk5)), 정규표현의 동시대각화는 군의 character 분해를 그대로 재현한다.

</div>

## 비가환 방향과 응용

지금까지 우리는 commutativity를 본질적으로 사용하여, 정규표현의 모든 블록이 하나의 character로 색인되는 동시 일반화고유공간으로 떨어진다는 것을 보았다. Commutativity를 떼면 그림은 더 풍부해진다. semisimple algebra의 일반론에 따르면, algebraically closed field 위의 유한차원 semisimple algebra는 matrix algebra들의 곱 $$\prod_i\Mat_{n_i}(k)$$으로 분해된다. 우리가 다룬 commutative reduced인 경우는 모든 $$n_i=1$$인, 곧 모든 블록이 $$1\times 1$$인 가장 단순한 구석에 해당한다. 한편 $$\operatorname{char}k\nmid\lvert G\rvert$$인 경우 Maschke의 정리에 의해 group algebra $$k[G]$$가 semisimple이 되고 ([§유한군의 표현론, ⁋따름정리 7](/ko/math/representation_theory/representations_of_finite_groups#cor7)), 이로부터 유한군의 표현론이 회복된다. $$G$$가 abelian이면 $$k[G]$$가 commutative이므로 모든 기약표현이 $$1$$차원이고, 이는 [예시 16](#ex16)에서 본 것처럼 우리의 commutative 이론으로 완전히 설명된다.

이 사전은 표현론 바깥에서도 같은 모습으로 나타난다. 예컨대 적당히 국소화한 유한차원 가환 양자 코호몰로지 환의 maximal spectrum은 유한개의 점으로 이루어지며, 그 점들은 양자 곱셈 연산자들의 동시 고유값에 해당한다. 이는 정규표현의 동시 일반화고유공간 분해라는 우리의 이야기가 그대로 적용되는 한 사례이다.

---

**참고문헌**

**[AM]** M. F. Atiyah and I. G. Macdonald, *Introduction to commutative algebra*, Addison-Wesley, 1969.

**[FH]** W. Fulton and J. Harris, *Representation theory: a first course*, Springer, 1991.
