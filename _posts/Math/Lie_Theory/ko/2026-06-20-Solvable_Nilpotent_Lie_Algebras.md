---
title: "가해 Lie algebra와 nilpotent Lie algebra"
description: "추상 Lie algebra의 subalgebra·ideal·quotient와 adjoint representation을 정리하고, derived series와 lower central series로 가해성과 nilpotency를 정의한 뒤 Engel의 정리와 Lie의 정리를 증명한다."
excerpt: "Derived series, lower central series, Engel·Lie 정리"

categories: [Math / Lie Theory]
permalink: /ko/math/lie_theory/solvable_nilpotent_lie_algebras
sidebar: 
    nav: "Lie_theory-ko"

date: 2026-06-20
weight: 3.5

published: false

---

Lie group의 국소 구조는 그 Lie algebra에 담겨 있으며 ([§리 군, ⁋정리 17](/ko/math/lie_theory/Lie_groups#thm17)), Lie algebra의 구조 이론은 두 극단적인 부류, 곧 *가해<sub>solvable</sub>* Lie algebra와 *nilpotent* Lie algebra의 분석에서 출발한다. 이 두 부류는 각각 Lie group의 가해성과 nilpotency에 대응하며, 임의의 유한차원 Lie algebra는 가장 큰 가해 ideal인 radical로 몫을 취해 반단순 부분을 떼어내는 방식으로 분석된다. 이 글에서 우리는 먼저 추상 Lie algebra에 대한 subalgebra, ideal, homomorphism, quotient, 그리고 adjoint representation을 정리하고, derived series와 lower central series를 통해 가해성과 nilpotency를 정의한다. 그 뒤 nilpotency를 ad-nilpotency로 판정하는 Engel의 정리와, 가해 Lie algebra가 동시 상삼각화 가능함을 보이는 Lie의 정리를 증명한다.

이 글 전체에서 $$k$$는 고정된 체이고, 별다른 언급이 없는 한 $$\mathfrak{g}$$는 $$k$$ 위에 정의된 유한차원 Lie algebra이다. ([§리 군, ⁋정의 8](/ko/math/lie_theory/Lie_groups#def8)) Lie bracket은 $$[-,-]$$로 적으며, anticommutativity와 Jacobi identity는 자유로이 사용한다.

## Subalgebra, ideal, quotient

Lie algebra의 구조를 다루기 위해 우선 부분대상과 몫대상을 정비한다. 환의 부분환과 ideal이 그러하듯, Lie algebra에서도 단순히 bracket에 대해 닫힌 부분공간과 더 강한 흡수 조건을 만족하는 부분공간을 구별한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Lie algebra $$\mathfrak{g}$$의 부분공간 $$\mathfrak{h}\subseteq\mathfrak{g}$$가 *Lie subalgebra<sub>부분대수</sub>*라는 것은 임의의 $$x,y\in\mathfrak{h}$$에 대하여 $$[x,y]\in\mathfrak{h}$$가 성립하는 것이다.

</div>

이 때 bracket을 $$\mathfrak{h}$$로 제한하면 $$\mathfrak{h}$$ 자체가 $$k$$ 위의 Lie algebra가 된다. 우리는 두 부분공간 $$\mathfrak{a},\mathfrak{b}\subseteq\mathfrak{g}$$에 대하여, $$[a,b]$$ ($$a\in\mathfrak{a}$$, $$b\in\mathfrak{b}$$) 꼴의 원소들이 생성하는 부분공간을 $$[\mathfrak{a},\mathfrak{b}]$$로 적기로 한다. 이 표기 하에서 부분공간 $$\mathfrak{h}$$가 subalgebra라는 조건은 $$[\mathfrak{h},\mathfrak{h}]\subseteq\mathfrak{h}$$로 간결하게 적힌다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Lie algebra $$\mathfrak{g}$$의 부분공간 $$\mathfrak{a}\subseteq\mathfrak{g}$$가 $$\mathfrak{g}$$의 *ideal<sub>이데알</sub>*이라는 것은 임의의 $$x\in\mathfrak{g}$$와 $$a\in\mathfrak{a}$$에 대하여 $$[x,a]\in\mathfrak{a}$$가 성립하는 것, 곧 $$[\mathfrak{g},\mathfrak{a}]\subseteq\mathfrak{a}$$인 것이다.

</div>

Bracket의 anticommutativity에 의해 $$[x,a]=-[a,x]$$이므로, Lie algebra에서는 환과 달리 좌·우 ideal의 구별이 없다. 모든 ideal은 특히 subalgebra이지만 그 역은 성립하지 않는다. 흡수 조건 $$[\mathfrak{g},\mathfrak{a}]\subseteq\mathfrak{a}$$는 ideal 바깥의 원소와의 bracket까지 통제하므로, 아래에서 보듯 ideal은 몫 Lie algebra를 정의하는 데에 필요한 정확한 조건이다.

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> 몇 가지 기본적인 ideal과 subalgebra를 정리한다.

1. $$\mathfrak{g}$$ 자신과 $$0$$은 항상 ideal이다.
2. *center<sub>중심</sub>* $$Z(\mathfrak{g})=\left\{x\in\mathfrak{g}\mid [x,y]=0\text{ for all }y\in\mathfrak{g}\right\}$$은 ideal이다. 실제로 $$x\in Z(\mathfrak{g})$$이면 임의의 $$y\in\mathfrak{g}$$에 대하여 $$[y,x]=-[x,y]=0\in Z(\mathfrak{g})$$이다.
3. *derived algebra<sub>유도대수</sub>* $$[\mathfrak{g},\mathfrak{g}]$$은 ideal이다. $$[\mathfrak{g},[\mathfrak{g},\mathfrak{g}]]\subseteq[\mathfrak{g},\mathfrak{g}]$$가 정의에서 곧바로 따른다.
4. $$Z(\mathfrak{g})=\mathfrak{g}$$인 경우, 곧 모든 bracket이 $$0$$인 Lie algebra를 *abelian<sub>가환</sub>* Lie algebra라 부른다. 이는 $$[\mathfrak{g},\mathfrak{g}]=0$$인 것과 같다.

</div>

이제 두 Lie algebra 사이의 사상과 몫을 정의한다. Lie algebra의 사상은 단순히 bracket을 보존하는 선형사상이다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> 두 Lie algebra $$\mathfrak{g},\mathfrak{h}$$ 사이의 $$k$$-linear map $$\phi:\mathfrak{g}\rightarrow\mathfrak{h}$$가 *Lie algebra homomorphism<sub>준동형</sub>*이라는 것은 임의의 $$x,y\in\mathfrak{g}$$에 대하여

$$\phi([x,y])=[\phi(x),\phi(y)]$$

이 성립하는 것이다.

</div>

Homomorphism $$\phi:\mathfrak{g}\rightarrow\mathfrak{h}$$의 kernel $$\ker\phi$$는 $$\mathfrak{g}$$의 ideal이고, image $$\operatorname{im}\phi$$는 $$\mathfrak{h}$$의 subalgebra이다. 실제로 $$a\in\ker\phi$$와 $$x\in\mathfrak{g}$$에 대하여 $$\phi([x,a])=[\phi(x),\phi(a)]=[\phi(x),0]=0$$이므로 $$[x,a]\in\ker\phi$$이다. Ideal $$\mathfrak{a}\subseteq\mathfrak{g}$$가 주어지면, 벡터공간 몫 $$\mathfrak{g}/\mathfrak{a}$$ 위에 bracket을 자연스럽게 정의할 수 있다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> $$\mathfrak{a}$$가 $$\mathfrak{g}$$의 ideal이면, 몫 벡터공간 $$\mathfrak{g}/\mathfrak{a}$$ 위에

$$[x+\mathfrak{a},\,y+\mathfrak{a}]=[x,y]+\mathfrak{a}$$

으로 정의되는 연산은 잘 정의된 Lie bracket이며, 이로써 $$\mathfrak{g}/\mathfrak{a}$$는 Lie algebra가 된다. 또한 몫사상 $$\pi:\mathfrak{g}\rightarrow\mathfrak{g}/\mathfrak{a}$$는 surjective homomorphism이고, $$\ker\pi=\mathfrak{a}$$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

연산이 대표원의 선택과 무관함을 보인다. $$x'=x+a$$, $$y'=y+b$$ ($$a,b\in\mathfrak{a}$$)라 하면

$$[x',y']=[x+a,\,y+b]=[x,y]+[x,b]+[a,y]+[a,b]$$

이다. $$\mathfrak{a}$$가 ideal이므로 $$[x,b],[a,y],[a,b]$$는 모두 $$\mathfrak{a}$$에 속하고, 따라서 $$[x',y']+\mathfrak{a}=[x,y]+\mathfrak{a}$$이다. 즉 연산이 잘 정의된다. Bilinearity는 $$\mathfrak{g}$$의 bracket의 bilinearity에서 따라오고, anticommutativity와 Jacobi identity도 몫사상이 선형이므로 $$\mathfrak{g}$$의 해당 항등식에서 직접 내려온다. 가령 임의의 $$\bar x,\bar y,\bar z\in\mathfrak{g}/\mathfrak{a}$$에 대하여

$$[[\bar x,\bar y],\bar z]+[[\bar y,\bar z],\bar x]+[[\bar z,\bar x],\bar y]=\bigl([[x,y],z]+[[y,z],x]+[[z,x],y]\bigr)+\mathfrak{a}=0+\mathfrak{a}$$

이다. $$\pi$$가 surjective homomorphism이고 $$\ker\pi=\mathfrak{a}$$임은 정의에서 즉각적이다.

</details>

이로써 Lie algebra의 first isomorphism theorem이 성립한다. Homomorphism $$\phi:\mathfrak{g}\rightarrow\mathfrak{h}$$에 대하여 $$\mathfrak{g}/\ker\phi\cong\operatorname{im}\phi$$이며, 이는 벡터공간 사이의 동형이 bracket을 보존함을 [명제 5](#prop5)와 같은 방식으로 확인하면 얻어진다. 앞으로 우리는 이 동형을 자유로이 사용한다.

## Adjoint representation

Lie algebra가 자기 자신에 작용하는 방식은 bracket 그 자체로 주어진다. 각 원소 $$x$$에 대하여 $$y\mapsto[x,y]$$로 정의되는 선형사상이 그것이며, 이는 nilpotency를 판정할 때 핵심적인 도구가 된다. 여기에서 벡터공간 $$V$$에 대하여 $$\mathfrak{gl}(V)$$는 $$\End_k(V)$$에 commutator bracket $$[f,g]=f\circ g-g\circ f$$를 준 Lie algebra를 가리킨다. ([§보편 포락 대수, ⁋정의 1](/ko/math/lie_theory/universal_enveloping_algebra#def1))

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> Lie algebra $$\mathfrak{g}$$에 대하여, 각 $$x\in\mathfrak{g}$$에 선형사상

$$\ad x:\mathfrak{g}\rightarrow\mathfrak{g};\qquad (\ad x)(y)=[x,y]$$

를 대응시키는 사상 $$\ad:\mathfrak{g}\rightarrow\mathfrak{gl}(\mathfrak{g})$$를 $$\mathfrak{g}$$의 *adjoint representation<sub>수반 표현</sub>*이라 부른다.

</div>

이 정의는 Lie group $$G$$의 adjoint representation을 미분하여 얻어지는 사상 ([§리 군, ⁋정의 19](/ko/math/lie_theory/Lie_groups#def19))의 추상적·대수적 판본이며, 그 글에서 확인한 $$\ad(x)y=[x,y]$$를 그대로 정의로 채택한 것이다. 다음 명제는 $$\ad$$가 표현, 곧 $$\mathfrak{g}$$에서 $$\mathfrak{gl}(\mathfrak{g})$$로의 homomorphism임을 보이며, 그 본질은 Jacobi identity이다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> $$\ad:\mathfrak{g}\rightarrow\mathfrak{gl}(\mathfrak{g})$$은 Lie algebra homomorphism이며, $$\ker(\ad)=Z(\mathfrak{g})$$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\ad$$가 선형임은 bracket이 첫 변수에 대해 선형이라는 데에서 따라온다. Homomorphism 조건 $$\ad[x,y]=[\ad x,\ad y]$$를 확인하기 위해, 임의의 $$z\in\mathfrak{g}$$에 양변을 적용하자. 우변은 $$\mathfrak{gl}(\mathfrak{g})$$의 commutator이므로

$$[\ad x,\ad y](z)=(\ad x)(\ad y)(z)-(\ad y)(\ad x)(z)=[x,[y,z]]-[y,[x,z]]$$

이다. 한편 좌변은 $$(\ad[x,y])(z)=[[x,y],z]$$이다. Jacobi identity

$$[[x,y],z]+[[y,z],x]+[[z,x],y]=0$$

를 anticommutativity로 정리하면 $$[[x,y],z]=[x,[y,z]]-[y,[x,z]]$$를 얻으므로 두 식이 일치한다. 마지막으로 $$x\in\ker(\ad)$$인 것은 $$\ad x=0$$, 곧 모든 $$y$$에 대하여 $$[x,y]=0$$인 것이고 이는 정확히 $$x\in Z(\mathfrak{g})$$를 뜻한다.

</details>

원소 $$x\in\mathfrak{g}$$가 $$\ad x$$가 nilpotent endomorphism인 경우 우리는 $$x$$를 *ad-nilpotent*라 부른다. 이 국소적 조건이 Lie algebra 전체의 nilpotency와 어떻게 연결되는지가 Engel의 정리의 내용이다.

## Derived series와 lower central series

가해성과 nilpotency는 모두 반복적인 bracket이 결국 $$0$$이 되는지를 묻는 조건이며, 두 조건은 반복 방식의 차이로 구별된다. 한쪽은 매번 직전 단계를 자기 자신과 bracket하고, 다른 쪽은 매번 전체 $$\mathfrak{g}$$와 bracket한다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> Lie algebra $$\mathfrak{g}$$의 *derived series<sub>유도열</sub>* $$\bigl(\mathfrak{g}^{(n)}\bigr)_{n\geq 0}$$는

$$\mathfrak{g}^{(0)}=\mathfrak{g},\qquad \mathfrak{g}^{(n+1)}=[\mathfrak{g}^{(n)},\mathfrak{g}^{(n)}]$$

으로 귀납적으로 정의되는 부분공간들의 열이다.

</div>

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> Lie algebra $$\mathfrak{g}$$의 *lower central series<sub>하향 중심열</sub>* $$\bigl(\mathfrak{g}^{n}\bigr)_{n\geq 1}$$는

$$\mathfrak{g}^{1}=\mathfrak{g},\qquad \mathfrak{g}^{n+1}=[\mathfrak{g},\mathfrak{g}^{n}]$$

으로 귀납적으로 정의되는 부분공간들의 열이다.

</div>

두 열의 각 항은 모두 $$\mathfrak{g}$$의 ideal이다. Derived series의 경우 $$\mathfrak{g}^{(n)}$$이 ideal이면 $$[\mathfrak{g},\mathfrak{g}^{(n+1)}]=[\mathfrak{g},[\mathfrak{g}^{(n)},\mathfrak{g}^{(n)}]]\subseteq\mathfrak{g}^{(n+1)}$$임을 Jacobi identity로 확인할 수 있고, lower central series의 경우 $$\mathfrak{g}^{n+1}=[\mathfrak{g},\mathfrak{g}^n]$$이 정의상 $$[\mathfrak{g},-]$$의 상이므로 ideal이다. 또한 정의에서 두 열은 모두 감소열

$$\mathfrak{g}=\mathfrak{g}^{(0)}\supseteq\mathfrak{g}^{(1)}\supseteq\cdots,\qquad \mathfrak{g}=\mathfrak{g}^{1}\supseteq\mathfrak{g}^{2}\supseteq\cdots$$

을 이루며, $$\mathfrak{g}^{(1)}=\mathfrak{g}^{2}=[\mathfrak{g},\mathfrak{g}]$$로 첫 비자명한 항은 일치한다. 귀납적으로 $$\mathfrak{g}^{(n)}\subseteq\mathfrak{g}^{n+1}$$가 성립하므로, derived series는 lower central series보다 빠르게 줄어든다.

<div class="definition" markdown="1">

<ins id="def10">**정의 10**</ins> Lie algebra $$\mathfrak{g}$$가 *solvable<sub>가해</sub>*이라는 것은 어떤 $$n\geq 0$$에 대하여 $$\mathfrak{g}^{(n)}=0$$인 것이다.

</div>

<div class="definition" markdown="1">

<ins id="def11">**정의 11**</ins> Lie algebra $$\mathfrak{g}$$가 *nilpotent*라는 것은 어떤 $$n\geq 1$$에 대하여 $$\mathfrak{g}^{n}=0$$인 것이다.

</div>

위에서 관찰한 포함관계 $$\mathfrak{g}^{(n)}\subseteq\mathfrak{g}^{n+1}$$로부터, nilpotent Lie algebra는 항상 solvable이다. 이는 아래 [명제 13](#prop13)에서 다시 정리한다. 반대 방향은 성립하지 않으며, 아래 예시가 두 개념을 구별한다.

<div class="example" markdown="1">

<ins id="ex12">**예시 12**</ins> $$\mathfrak{gl}(n;k)$$의 두 subalgebra를 살펴본다.

1. 상삼각행렬 전체로 이루어진 Lie algebra $$\mathfrak{b}=\mathfrak{t}(n;k)$$는 solvable이다. 두 상삼각행렬의 commutator는 대각성분이 모두 $$0$$인 상삼각행렬, 곧 strictly 상삼각행렬이 되므로 $$[\mathfrak{b},\mathfrak{b}]\subseteq\mathfrak{n}$$이고, 여기에서 $$\mathfrak{n}$$은 strictly 상삼각행렬들의 집합이다. 더 나아가 strictly 상삼각행렬들끼리의 곱은 윗쪽으로 한 칸 더 밀리므로, derived series가 유한 단계 안에 $$0$$이 됨을 확인할 수 있다.
2. strictly 상삼각행렬 전체로 이루어진 $$\mathfrak{n}=\mathfrak{n}(n;k)$$는 nilpotent이다. $$\mathfrak{n}$$의 원소를 곱할 때마다 $$0$$이 아닌 성분이 대각선에서 한 칸씩 멀어지므로, $$\mathfrak{n}^{n}=0$$이다.
3. 임의의 abelian Lie algebra는 $$[\mathfrak{g},\mathfrak{g}]=0$$이므로 $$\mathfrak{g}^{2}=0$$, 곧 nilpotent이다.

특히 $$n\geq 2$$이면 $$\mathfrak{b}$$는 solvable이지만 nilpotent가 아니다. 가령 $$n=2$$에서 $$h=\begin{pmatrix}1&0\\0&0\end{pmatrix}$$, $$e=\begin{pmatrix}0&1\\0&0\end{pmatrix}$$에 대하여 $$[h,e]=e$$이므로 $$(\ad h)^m e=e$$가 모든 $$m$$에 대해 성립하여 $$\mathfrak{b}^{n}$$이 결코 $$0$$이 되지 않는다.

</div>

위 예시에서 strictly 상삼각행렬은 $$\mathfrak{gl}(V)$$ 안의 nilpotent endomorphism들이며, 따라서 $$\mathfrak{n}$$의 모든 원소는 nilpotent endomorphism이다. Engel의 정리는 이 현상의 역, 곧 nilpotent endomorphism들로 이루어진 Lie algebra가 항상 동시에 strictly 상삼각화됨을 보인다.

먼저 nilpotency가 solvability를 함의함을 정리한다.

<div class="proposition" markdown="1">

<ins id="prop13">**명제 13**</ins> Nilpotent Lie algebra는 solvable이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

모든 $$n\geq 0$$에 대하여 $$\mathfrak{g}^{(n)}\subseteq\mathfrak{g}^{n+1}$$임을 $$n$$에 대한 귀납법으로 보인다. $$n=0$$이면 $$\mathfrak{g}^{(0)}=\mathfrak{g}=\mathfrak{g}^{1}$$이다. $$\mathfrak{g}^{(n)}\subseteq\mathfrak{g}^{n+1}$$를 가정하면

$$\mathfrak{g}^{(n+1)}=[\mathfrak{g}^{(n)},\mathfrak{g}^{(n)}]\subseteq[\mathfrak{g},\mathfrak{g}^{(n)}]\subseteq[\mathfrak{g},\mathfrak{g}^{n+1}]=\mathfrak{g}^{n+2}$$

인데, 첫 포함은 $$\mathfrak{g}^{(n)}\subseteq\mathfrak{g}$$에서, 둘째 포함은 귀납 가정에서 따라온다. 따라서 어떤 $$m$$에 대하여 $$\mathfrak{g}^{m}=0$$이면 $$\mathfrak{g}^{(m-1)}\subseteq\mathfrak{g}^{m}=0$$이므로 $$\mathfrak{g}$$는 solvable이다.

</details>

## Solvability의 닫힘 성질과 radical

가해성은 부분대상, 몫대상, 그리고 확장에 대해 닫혀 있다. 이 닫힘 성질들은 가장 큰 가해 ideal인 radical이 잘 정의됨을 보장하는 데에 쓰인다.

<div class="proposition" markdown="1">

<ins id="prop14">**명제 14**</ins> Lie algebra $$\mathfrak{g}$$에 대하여 다음이 성립한다.

1. $$\mathfrak{g}$$가 solvable이고 $$\mathfrak{h}\subseteq\mathfrak{g}$$가 subalgebra이면 $$\mathfrak{h}$$도 solvable이다.
2. $$\mathfrak{g}$$가 solvable이고 $$\phi:\mathfrak{g}\rightarrow\mathfrak{h}$$가 surjective homomorphism이면 $$\mathfrak{h}$$도 solvable이다. 특히 solvable Lie algebra의 임의의 몫은 solvable이다.
3. $$\mathfrak{a}\subseteq\mathfrak{g}$$가 ideal이고 $$\mathfrak{a}$$와 $$\mathfrak{g}/\mathfrak{a}$$가 모두 solvable이면 $$\mathfrak{g}$$도 solvable이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

(1) $$\mathfrak{h}\subseteq\mathfrak{g}$$이므로 $$\mathfrak{h}^{(n)}\subseteq\mathfrak{g}^{(n)}$$임을 $$n$$에 대한 귀납법으로 확인할 수 있다. $$n=0$$은 가정이고, $$\mathfrak{h}^{(n)}\subseteq\mathfrak{g}^{(n)}$$이면 $$\mathfrak{h}^{(n+1)}=[\mathfrak{h}^{(n)},\mathfrak{h}^{(n)}]\subseteq[\mathfrak{g}^{(n)},\mathfrak{g}^{(n)}]=\mathfrak{g}^{(n+1)}$$이다. $$\mathfrak{g}^{(n)}=0$$이면 $$\mathfrak{h}^{(n)}=0$$이다.

(2) $$\phi$$가 surjective homomorphism이므로 $$\phi(\mathfrak{g}^{(n)})=\mathfrak{h}^{(n)}$$임을 귀납법으로 보인다. $$n=0$$은 surjectivity이고, $$\phi(\mathfrak{g}^{(n)})=\mathfrak{h}^{(n)}$$이면 homomorphism 성질에서

$$\phi(\mathfrak{g}^{(n+1)})=\phi([\mathfrak{g}^{(n)},\mathfrak{g}^{(n)}])=[\phi(\mathfrak{g}^{(n)}),\phi(\mathfrak{g}^{(n)})]=[\mathfrak{h}^{(n)},\mathfrak{h}^{(n)}]=\mathfrak{h}^{(n+1)}$$

이다. $$\mathfrak{g}^{(n)}=0$$이면 $$\mathfrak{h}^{(n)}=\phi(0)=0$$이다. 몫의 경우는 $$\phi=\pi$$인 특수한 경우이다.

(3) $$\mathfrak{g}/\mathfrak{a}$$가 solvable이므로 어떤 $$m$$에 대하여 $$(\mathfrak{g}/\mathfrak{a})^{(m)}=0$$이다. 몫사상 $$\pi:\mathfrak{g}\rightarrow\mathfrak{g}/\mathfrak{a}$$에 대하여 $$\pi(\mathfrak{g}^{(m)})=(\mathfrak{g}/\mathfrak{a})^{(m)}=0$$이므로 $$\mathfrak{g}^{(m)}\subseteq\ker\pi=\mathfrak{a}$$이다. 한편 $$\mathfrak{a}$$가 solvable이므로 어떤 $$l$$에 대하여 $$\mathfrak{a}^{(l)}=0$$이다. derived series는 부분공간을 포함관계에 따라 보내므로 $$\mathfrak{g}^{(m)}\subseteq\mathfrak{a}$$에서 $$\mathfrak{g}^{(m+l)}=(\mathfrak{g}^{(m)})^{(l)}\subseteq\mathfrak{a}^{(l)}=0$$을 얻는다. 여기에서 $$(\mathfrak{g}^{(m)})^{(l)}$$은 $$\mathfrak{g}^{(m)}$$을 출발점으로 한 derived series의 $$l$$번째 항이며, 일반적으로 $$\mathfrak{g}^{(m+l)}=(\mathfrak{g}^{(m)})^{(l)}$$임은 정의에서 직접 따라온다. 따라서 $$\mathfrak{g}$$는 solvable이다.

</details>

(3)의 직접적인 귀결로, 두 solvable ideal의 합도 solvable이다. 실제로 $$\mathfrak{a},\mathfrak{b}$$가 solvable ideal이면 $$\mathfrak{a}+\mathfrak{b}$$도 ideal이고, second isomorphism theorem에 의한 동형

$$(\mathfrak{a}+\mathfrak{b})/\mathfrak{b}\cong\mathfrak{a}/(\mathfrak{a}\cap\mathfrak{b})$$

의 우변은 solvable $$\mathfrak{a}$$의 몫으로서 (2)에 의해 solvable이다. 따라서 $$(\mathfrak{a}+\mathfrak{b})/\mathfrak{b}$$와 $$\mathfrak{b}$$가 모두 solvable이므로 (3)에 의해 $$\mathfrak{a}+\mathfrak{b}$$가 solvable이다. 이 관찰이 다음 정의를 정당화한다.

<div class="definition" markdown="1">

<ins id="def15">**정의 15**</ins> 유한차원 Lie algebra $$\mathfrak{g}$$의 *radical<sub>근기</sub>* $$\operatorname{rad}\mathfrak{g}$$은 $$\mathfrak{g}$$의 solvable ideal 가운데 포함관계에 대하여 가장 큰 것이다.

</div>

이러한 가장 큰 solvable ideal이 유일하게 존재함을 확인해 둔다. $$\mathfrak{g}$$가 유한차원이므로, 차원이 최대인 solvable ideal $$\mathfrak{r}$$을 택할 수 있다. 만일 $$\mathfrak{a}$$가 임의의 solvable ideal이면 위에서 본 대로 $$\mathfrak{r}+\mathfrak{a}$$도 solvable ideal이고 $$\mathfrak{r}\subseteq\mathfrak{r}+\mathfrak{a}$$이다. $$\mathfrak{r}$$의 차원이 최대이므로 $$\mathfrak{r}+\mathfrak{a}=\mathfrak{r}$$, 곧 $$\mathfrak{a}\subseteq\mathfrak{r}$$이다. 따라서 $$\mathfrak{r}$$은 모든 solvable ideal을 포함하는 유일한 가장 큰 solvable ideal이다. 몫 $$\mathfrak{g}/\operatorname{rad}\mathfrak{g}$$은 자명하지 않은 solvable ideal을 갖지 않으며, 이러한 Lie algebra를 *semisimple*이라 부른다. 임의의 유한차원 Lie algebra는 이렇게 가해 부분과 반단순 부분으로 나뉘어 분석된다.

## Engel의 정리

Engel의 정리의 핵심은 선형대수적 진술, 곧 nilpotent endomorphism들로 이루어진 Lie algebra가 공통의 kernel vector를 가진다는 것이다. 이를 먼저 증명하고, 그로부터 추상적 형태를 따름정리로 얻는다.

<div class="proposition" markdown="1">

<ins id="lem16">**보조정리 16**</ins> $$V$$가 $$0$$이 아닌 유한차원 $$k$$-벡터공간이고 $$\mathfrak{g}\subseteq\mathfrak{gl}(V)$$가 subalgebra로서 그 모든 원소가 nilpotent endomorphism이라 하자. 그럼 어떤 $$0\neq v\in V$$가 존재하여 모든 $$x\in\mathfrak{g}$$에 대하여 $$xv=0$$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\dim\mathfrak{g}$$에 대한 귀납법으로 증명한다. $$\dim\mathfrak{g}=0$$이면 조건이 공허하게 성립하므로, $$\dim\mathfrak{g}\geq 1$$이고 차원이 더 작은 모든 경우에 대하여 결론이 성립한다고 가정한다.

먼저 $$\mathfrak{g}$$가 codimension $$1$$인 ideal $$\mathfrak{h}$$를 가짐을 보인다. 이를 위해 $$\mathfrak{g}$$의 임의의 maximal proper subalgebra $$\mathfrak{h}$$를 택한다. $$\mathfrak{h}$$의 $$\mathfrak{g}$$ 위의 작용을 adjoint로 보면 $$\mathfrak{h}$$는 $$\mathfrak{g}$$와 $$\mathfrak{h}$$ 둘 다에 작용하므로 몫 벡터공간 $$\mathfrak{g}/\mathfrak{h}$$ 위에 작용한다. 곧 각 $$x\in\mathfrak{h}$$에 대하여 $$\ad x$$가 $$\mathfrak{h}$$를 보존하므로, $$\overline{\ad}\,x:\mathfrak{g}/\mathfrak{h}\rightarrow\mathfrak{g}/\mathfrak{h}$$가 유도된다. 이로써 $$\mathfrak{h}$$는 $$\mathfrak{gl}(\mathfrak{g}/\mathfrak{h})$$의 subalgebra의 상이 되는데, 임의의 $$x\in\mathfrak{g}$$에 대하여 $$\ad x$$는 nilpotent endomorphism이다. 이는 $$x$$가 $$\mathfrak{gl}(V)$$ 안의 nilpotent endomorphism일 때, 그 좌·우 곱사상의 차로 표현되는 $$\ad x$$ 역시 nilpotent이기 때문이다. 따라서 $$\dim\mathfrak{h}<\dim\mathfrak{g}$$인 $$\mathfrak{h}$$의 상에 귀납 가정을 적용하면, 어떤 $$0\neq \bar y\in\mathfrak{g}/\mathfrak{h}$$가 존재하여 모든 $$x\in\mathfrak{h}$$에 대하여 $$\overline{\ad}\,x(\bar y)=0$$, 곧 $$[x,y]\in\mathfrak{h}$$이다. 이 $$y\notin\mathfrak{h}$$에 대하여 $$\mathfrak{h}+ky$$는 subalgebra이고 $$\mathfrak{h}$$를 진부분으로 포함하므로, $$\mathfrak{h}$$의 maximality에서 $$\mathfrak{h}+ky=\mathfrak{g}$$이다. $$[\mathfrak{h},y]\subseteq\mathfrak{h}$$이고 $$[\mathfrak{h},\mathfrak{h}]\subseteq\mathfrak{h}$$이므로 $$\mathfrak{h}$$는 $$\mathfrak{g}$$의 ideal이며, $$\dim(\mathfrak{g}/\mathfrak{h})=1$$이다.

이제 $$\dim\mathfrak{h}<\dim\mathfrak{g}$$이고 $$\mathfrak{h}$$의 모든 원소가 $$V$$ 위의 nilpotent endomorphism이므로, 귀납 가정에 의해 공통 kernel 공간

$$W=\left\{v\in V\mid xv=0\text{ for all }x\in\mathfrak{h}\right\}$$

은 $$0$$이 아니다. $$\mathfrak{g}=\mathfrak{h}+ky$$에서 $$y$$를 하나 택하자. $$W$$가 $$y$$에 의해 보존됨을 보인다. $$w\in W$$와 $$x\in\mathfrak{h}$$에 대하여

$$x(yw)=y(xw)+[x,y]w=y\cdot 0+[x,y]w$$

인데, $$\mathfrak{h}$$가 ideal이므로 $$[x,y]\in\mathfrak{h}$$이고 $$w\in W$$이므로 $$[x,y]w=0$$이다. 따라서 $$x(yw)=0$$이 모든 $$x\in\mathfrak{h}$$에 대해 성립하여 $$yw\in W$$이다. 즉 $$y$$는 $$W$$를 보존한다. $$y$$가 $$V$$ 위의 nilpotent endomorphism이므로 그 제한 $$y\vert_W$$도 nilpotent endomorphism이고, $$W\neq 0$$이므로 $$y\vert_W$$는 $$0$$이 아닌 kernel을 갖는다. 곧 어떤 $$0\neq v\in W$$가 존재하여 $$yv=0$$이다. 이 $$v$$는 모든 $$x\in\mathfrak{h}$$에 대하여 $$xv=0$$이고 $$yv=0$$이므로, $$\mathfrak{g}=\mathfrak{h}+ky$$의 모든 원소에 의해 소멸된다.

</details>

위 보조정리에서 공통 kernel vector $$v_1$$을 하나 얻은 뒤, 몫 $$V/kv_1$$에 같은 논증을 반복하면 $$\mathfrak{g}$$가 동시에 strictly 상삼각화됨을 알 수 있다. 이를 정리하면 다음 따름정리가 된다.

<div class="proposition" markdown="1">

<ins id="cor17">**따름정리 17**</ins> $$V$$가 $$0$$이 아닌 유한차원 $$k$$-벡터공간이고 $$\mathfrak{g}\subseteq\mathfrak{gl}(V)$$의 모든 원소가 nilpotent endomorphism이면, $$V$$의 기저를 적절히 택하여 $$\mathfrak{g}$$의 모든 원소가 동시에 strictly 상삼각행렬로 표현되도록 할 수 있다. 동치로, $$V$$의 flag

$$0=V_0\subsetneq V_1\subsetneq\cdots\subsetneq V_n=V,\qquad \dim V_i=i$$

이 존재하여 모든 $$x\in\mathfrak{g}$$에 대하여 $$xV_i\subseteq V_{i-1}$$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\dim V=n$$에 대한 귀납법으로 위 flag를 구성한다. $$n=0$$이면 자명하다. $$n\geq 1$$일 때, [보조정리 16](#lem16)에 의해 $$0\neq v_1\in V$$가 존재하여 모든 $$x\in\mathfrak{g}$$에 대하여 $$xv_1=0$$이다. $$V_1=kv_1$$로 두면 $$\mathfrak{g}V_1=0\subseteq V_0$$이다. 몫공간 $$\bar V=V/V_1$$ 위에서 각 $$x\in\mathfrak{g}$$는 $$\bar x:\bar V\rightarrow\bar V$$를 유도하며, $$x$$가 nilpotent endomorphism이므로 $$\bar x$$도 그러하다. 따라서 $$\bar{\mathfrak{g}}=\{\bar x\mid x\in\mathfrak{g}\}\subseteq\mathfrak{gl}(\bar V)$$는 nilpotent endomorphism들로 이루어진 subalgebra이고, $$\dim\bar V=n-1$$이므로 귀납 가정에 의해 flag

$$0=\bar V_0\subsetneq\bar V_1\subsetneq\cdots\subsetneq\bar V_{n-1}=\bar V$$

이 존재하여 모든 $$\bar x$$에 대하여 $$\bar x\bar V_i\subseteq\bar V_{i-1}$$이다. 몫사상 $$V\rightarrow\bar V$$에 의한 $$\bar V_i$$의 역상을 $$V_{i+1}$$로 두면, $$V_1\subsetneq V_2\subsetneq\cdots\subsetneq V_n=V$$이고 $$\dim V_{i+1}=i+1$$이며, $$xV_{i+1}\subseteq V_i$$가 성립한다. 이 기저에서 $$\mathfrak{g}$$의 원소는 모두 strictly 상삼각행렬이다.

</details>

이제 추상적 형태의 Engel의 정리를 서술한다. 핵심은 $$\ad:\mathfrak{g}\rightarrow\mathfrak{gl}(\mathfrak{g})$$를 통해 위의 선형대수적 결과를 적용하는 것이다.

<div class="proposition" markdown="1">

<ins id="thm18">**정리 18 (Engel)**</ins> 유한차원 Lie algebra $$\mathfrak{g}$$에 대하여, 모든 $$x\in\mathfrak{g}$$가 ad-nilpotent이면, 곧 모든 $$\ad x$$가 nilpotent endomorphism이면 $$\mathfrak{g}$$는 nilpotent이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\dim\mathfrak{g}$$에 대한 귀납법으로 증명한다. $$\mathfrak{g}=0$$이면 자명하다. $$\mathfrak{g}\neq 0$$이라 하자. $$\ad\mathfrak{g}=\{\ad x\mid x\in\mathfrak{g}\}$$는 $$\mathfrak{gl}(\mathfrak{g})$$의 subalgebra이고 ([명제 7](#prop7)), 가정에 의해 그 모든 원소가 nilpotent endomorphism이다. 만일 $$\ad\mathfrak{g}=0$$이면 $$\mathfrak{g}=Z(\mathfrak{g})$$이므로 $$\mathfrak{g}$$는 abelian, 따라서 nilpotent이다. $$\ad\mathfrak{g}\neq 0$$인 경우, $$\mathfrak{g}=\ker(\ad)$$가 아니므로 [보조정리 16](#lem16)을 $$V=\mathfrak{g}$$, $$\ad\mathfrak{g}\subseteq\mathfrak{gl}(\mathfrak{g})$$에 적용하면 어떤 $$0\neq z\in\mathfrak{g}$$가 존재하여 모든 $$x\in\mathfrak{g}$$에 대하여 $$(\ad x)(z)=[x,z]=0$$이다. 곧 $$z\in Z(\mathfrak{g})$$이고 $$z\neq 0$$이므로 $$Z(\mathfrak{g})\neq 0$$이다.

몫 $$\bar{\mathfrak{g}}=\mathfrak{g}/Z(\mathfrak{g})$$를 생각하면 $$\dim\bar{\mathfrak{g}}<\dim\mathfrak{g}$$이다. 몫사상 $$\pi$$에 대하여 $$\overline{\ad}\,\pi(x)=\ad x$$가 $$\bar{\mathfrak{g}}$$ 위에 유도하는 사상은 $$\ad x$$의 몫이므로 nilpotent endomorphism이다. 따라서 $$\bar{\mathfrak{g}}$$의 모든 원소도 ad-nilpotent이고, 귀납 가정에 의해 $$\bar{\mathfrak{g}}$$는 nilpotent이다. 곧 어떤 $$m$$에 대하여 $$\bar{\mathfrak{g}}^{m}=0$$이며, 이는 $$\mathfrak{g}^{m}\subseteq Z(\mathfrak{g})$$를 뜻한다. 그럼

$$\mathfrak{g}^{m+1}=[\mathfrak{g},\mathfrak{g}^{m}]\subseteq[\mathfrak{g},Z(\mathfrak{g})]=0$$

이므로 $$\mathfrak{g}$$는 nilpotent이다.

</details>

이 정리의 역도 성립한다. $$\mathfrak{g}$$가 nilpotent이면 어떤 $$m$$에 대하여 $$\mathfrak{g}^{m}=0$$이고, 정의에서 $$(\ad x_1)(\ad x_2)\cdots(\ad x_{m-1})(y)\in\mathfrak{g}^{m}=0$$이 모든 $$x_i,y\in\mathfrak{g}$$에 대해 성립하므로, 특히 $$(\ad x)^{m-1}=0$$이 되어 모든 $$x$$가 ad-nilpotent이다. 따라서 유한차원 Lie algebra가 nilpotent인 것과 모든 원소가 ad-nilpotent인 것은 동치이다.

## Lie의 정리

Engel의 정리가 임의의 체에서 성립하는 것과 달리, 가해 Lie algebra에 대한 동시 상삼각화는 기반 체에 대한 제약을 요구한다. Lie의 정리는 $$k$$가 대수적으로 닫혀 있고 표수가 $$0$$일 때, 가해 Lie algebra of endomorphisms가 공통 eigenvector를 가짐을 보인다. 표수 $$0$$이라는 가정은 아래 [보조정리 19](#lem19)의 증명에서 어떤 정수로 나누는 단계에 본질적으로 쓰이며, 양의 표수에서는 정리가 성립하지 않는 반례가 알려져 있다.

증명의 핵심은 ideal에 대한 공통 eigenvalue가 정의하는 eigenspace가 전체 Lie algebra의 작용에 의해 보존된다는 다음 불변성 보조정리이다.

<div class="proposition" markdown="1">

<ins id="lem19">**보조정리 19**</ins> $$k$$가 대수적으로 닫힌 표수 $$0$$의 체이고, $$V$$가 $$0$$이 아닌 유한차원 $$k$$-벡터공간, $$\mathfrak{g}\subseteq\mathfrak{gl}(V)$$가 subalgebra라 하자. $$\mathfrak{a}\subseteq\mathfrak{g}$$가 ideal이고 $$\lambda:\mathfrak{a}\rightarrow k$$가 선형범함수일 때,

$$W=\left\{v\in V\mid av=\lambda(a)v\text{ for all }a\in\mathfrak{a}\right\}$$

이 $$0$$이 아니면, $$W$$는 $$\mathfrak{g}$$에 의해 보존된다. 곧 모든 $$x\in\mathfrak{g}$$에 대하여 $$xW\subseteq W$$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$x\in\mathfrak{g}$$와 $$0\neq w\in W$$를 고정한다. 임의의 $$a\in\mathfrak{a}$$에 대하여 $$a(xw)=x(aw)+[a,x]w=\lambda(a)xw+\lambda([a,x])w$$이므로, $$xw\in W$$임을 보이려면 모든 $$a\in\mathfrak{a}$$에 대하여 $$\lambda([a,x])=0$$임을 보이면 충분하다.

이를 위해 부분공간들의 열을 구성한다. $$W_0=0$$으로 두고, $$i\geq 1$$에 대하여 $$W_i$$를 $$w,xw,\ldots,x^{i-1}w$$가 생성하는 부분공간으로 정의하자. $$V$$가 유한차원이므로 어떤 $$m$$에서 $$W_m=W_{m+1}=\cdots$$가 되며, 이 $$m$$은 $$w,xw,\ldots,x^{m-1}w$$가 일차독립이고 $$x^m w\in W_m$$이도록 하는 가장 작은 수이다. 따라서 $$\dim W_m=m$$이고 $$x W_m\subseteq W_m$$이다.

각 $$a\in\mathfrak{a}$$가 $$W_m$$을 보존하며, 기저 $$w,xw,\ldots,x^{m-1}w$$에 대하여 상삼각행렬로, 더 정밀하게는 대각성분이 모두 $$\lambda(a)$$인 상삼각행렬로 작용함을 $$i$$에 대한 귀납법으로 보인다. 곧 모든 $$a\in\mathfrak{a}$$와 모든 $$i\geq 0$$에 대하여

$$a\,x^i w\equiv\lambda(a)\,x^i w\pmod{W_i}$$

이다. $$i=0$$이면 $$aw=\lambda(a)w$$이므로 성립한다. $$i$$까지 모든 $$a$$에 대해 성립한다고 가정하면

$$a\,x^{i+1}w=a x(x^i w)=x a(x^i w)+[a,x]x^i w$$

인데, 귀납 가정에서 $$a(x^i w)=\lambda(a)x^i w+u$$ ($$u\in W_i$$)이므로 $$x a(x^i w)=\lambda(a)x^{i+1}w+xu$$이고 $$xu\in W_{i+1}$$이다. 또 $$[a,x]\in\mathfrak{a}$$이므로 귀납 가정을 $$[a,x]$$에 적용하면 $$[a,x]x^i w\equiv\lambda([a,x])x^i w\in W_{i+1}\pmod{W_i}$$, 곧 $$[a,x]x^i w\in W_{i+1}$$이다. 따라서 $$a\,x^{i+1}w\equiv\lambda(a)x^{i+1}w\pmod{W_{i+1}}$$이다.

이로써 각 $$a\in\mathfrak{a}$$는 $$W_m$$ 위에서 대각성분이 모두 $$\lambda(a)$$인 상삼각행렬이므로, $$W_m$$ 위로 제한한 $$a$$의 trace는

$$\operatorname{tr}(a\vert_{W_m})=m\,\lambda(a)$$

이다. 특히 $$a=[x,b]$$ ($$b\in\mathfrak{a}$$)에 이 식을 적용한다. $$x$$와 $$b$$가 모두 $$W_m$$을 보존하므로 그 commutator $$[x,b]\vert_{W_m}=x\vert_{W_m}b\vert_{W_m}-b\vert_{W_m}x\vert_{W_m}$$의 trace는 $$0$$이다. 따라서

$$0=\operatorname{tr}([x,b]\vert_{W_m})=m\,\lambda([x,b])$$

이며, $$k$$의 표수가 $$0$$이고 $$m\geq 1$$이므로 $$\lambda([x,b])=0$$이다. 임의의 $$a=[a',x]=-[x,a']$$ ($$a'\in\mathfrak{a}$$) 꼴에 대해서도 $$\lambda([a',x])=-\lambda([x,a'])=0$$이므로, 처음의 등식 $$a(xw)=\lambda(a)xw+\lambda([a,x])w$$에서 모든 $$a$$에 대해 $$\lambda([a,x])=0$$이다. 따라서 $$xw\in W$$이다.

</details>

표수 $$0$$ 가정이 사용된 유일한 지점은 마지막 단계에서 $$m\lambda([x,b])=0$$으로부터 $$\lambda([x,b])=0$$을 끌어내는 부분이다. 표수가 $$m$$을 나누는 양의 정수이면 이 추론이 무너지며, 실제로 그러한 체에서 Lie의 정리는 성립하지 않는다. 이제 이 보조정리로부터 공통 eigenvector의 존재를 귀납적으로 얻는다.

<div class="proposition" markdown="1">

<ins id="thm20">**정리 20 (Lie)**</ins> $$k$$가 대수적으로 닫힌 표수 $$0$$의 체이고, $$V$$가 $$0$$이 아닌 유한차원 $$k$$-벡터공간, $$\mathfrak{g}\subseteq\mathfrak{gl}(V)$$가 solvable subalgebra라 하자. 그럼 $$\mathfrak{g}$$의 모든 원소가 공유하는 eigenvector $$0\neq v\in V$$가 존재한다. 곧 선형범함수 $$\lambda:\mathfrak{g}\rightarrow k$$가 존재하여 모든 $$x\in\mathfrak{g}$$에 대하여 $$xv=\lambda(x)v$$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\dim\mathfrak{g}$$에 대한 귀납법으로 증명한다. $$\dim\mathfrak{g}=0$$이면 $$k$$가 대수적으로 닫혀 있으므로 임의의 $$0\neq v\in V$$가 (공허하게) 조건을 만족한다. $$\dim\mathfrak{g}=1$$인 경우, $$\mathfrak{g}=kx$$이고 $$x$$의 eigenvector가 $$k$$가 대수적으로 닫혀 있다는 데에서 존재한다.

이제 $$\dim\mathfrak{g}\geq 1$$이고 차원이 더 작은 모든 solvable subalgebra에 대하여 결론이 성립한다고 가정한다. $$\mathfrak{g}$$가 solvable이고 $$\mathfrak{g}\neq 0$$이므로 $$[\mathfrak{g},\mathfrak{g}]\neq\mathfrak{g}$$이다. 만일 $$[\mathfrak{g},\mathfrak{g}]=\mathfrak{g}$$이면 derived series가 $$\mathfrak{g}$$에서 멈춰 결코 $$0$$에 도달하지 못해 solvability에 모순이기 때문이다. 따라서 $$\mathfrak{g}/[\mathfrak{g},\mathfrak{g}]$$는 $$0$$이 아닌 abelian Lie algebra이고, 그 안에서 codimension $$1$$인 부분공간을 택해 역상을 취하면 $$[\mathfrak{g},\mathfrak{g}]$$를 포함하는 codimension $$1$$의 부분공간 $$\mathfrak{a}\subseteq\mathfrak{g}$$를 얻는다. $$[\mathfrak{g},\mathfrak{g}]\subseteq\mathfrak{a}$$이므로 $$[\mathfrak{g},\mathfrak{a}]\subseteq[\mathfrak{g},\mathfrak{g}]\subseteq\mathfrak{a}$$, 곧 $$\mathfrak{a}$$는 $$\mathfrak{g}$$의 ideal이다. $$\mathfrak{a}$$는 solvable Lie algebra $$\mathfrak{g}$$의 subalgebra이므로 solvable이고 ([명제 14](#prop14)), $$\dim\mathfrak{a}=\dim\mathfrak{g}-1$$이다.

귀납 가정에 의해 $$\mathfrak{a}$$의 공통 eigenvector가 존재한다. 곧 선형범함수 $$\lambda:\mathfrak{a}\rightarrow k$$와 $$0\neq v_0\in V$$가 존재하여 모든 $$a\in\mathfrak{a}$$에 대하여 $$av_0=\lambda(a)v_0$$이다. 따라서 eigenspace

$$W=\left\{v\in V\mid av=\lambda(a)v\text{ for all }a\in\mathfrak{a}\right\}$$

은 $$0$$이 아니다. [보조정리 19](#lem19)에 의해 $$W$$는 $$\mathfrak{g}$$에 의해 보존된다. 이제 $$\mathfrak{g}=\mathfrak{a}+kx$$가 되도록 $$x\in\mathfrak{g}\setminus\mathfrak{a}$$를 하나 택하자. $$x$$가 $$W$$를 보존하고 $$W\neq 0$$이며 $$k$$가 대수적으로 닫혀 있으므로, 제한 $$x\vert_W$$는 $$W$$ 안에 eigenvector $$0\neq v\in W$$를 갖는다. 곧 어떤 $$c\in k$$에 대하여 $$xv=cv$$이다. 이 $$v$$는 $$W$$의 원소이므로 모든 $$a\in\mathfrak{a}$$에 대하여 $$av=\lambda(a)v$$이고, 동시에 $$xv=cv$$이다. $$\lambda$$를 $$\lambda(x)=c$$로 확장하여 $$\mathfrak{g}=\mathfrak{a}+kx$$ 위의 선형범함수로 두면, $$v$$는 모든 $$\mathfrak{g}$$의 원소가 공유하는 eigenvector이다.

</details>

[따름정리 17](#cor17)과 동일한 flag 구성을 반복하면, 공통 eigenvector로부터 동시 상삼각화를 얻는다. 다만 이번에는 매 단계에서 strictly 상삼각이 아니라 단지 상삼각이 된다.

<div class="proposition" markdown="1">

<ins id="cor21">**따름정리 21**</ins> $$k$$가 대수적으로 닫힌 표수 $$0$$의 체이고 $$\mathfrak{g}\subseteq\mathfrak{gl}(V)$$가 $$0\neq V$$ 위의 solvable subalgebra이면, $$V$$의 기저를 적절히 택하여 $$\mathfrak{g}$$의 모든 원소가 동시에 상삼각행렬로 표현되도록 할 수 있다. 곧 flag

$$0=V_0\subsetneq V_1\subsetneq\cdots\subsetneq V_n=V,\qquad \dim V_i=i$$

이 존재하여 모든 $$x\in\mathfrak{g}$$에 대하여 $$xV_i\subseteq V_i$$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\dim V=n$$에 대한 귀납법으로 flag를 구성한다. $$n=0$$이면 자명하다. $$n\geq 1$$일 때, [정리 20](#thm20)에 의해 $$\mathfrak{g}$$의 공통 eigenvector $$0\neq v_1\in V$$가 존재한다. $$V_1=kv_1$$로 두면 모든 $$x\in\mathfrak{g}$$에 대하여 $$xV_1\subseteq V_1$$이다. 몫공간 $$\bar V=V/V_1$$ 위에서 각 $$x\in\mathfrak{g}$$는 $$\bar x:\bar V\rightarrow\bar V$$를 유도하며, 대응 $$x\mapsto\bar x$$는 Lie algebra homomorphism이므로 그 상 $$\bar{\mathfrak{g}}\subseteq\mathfrak{gl}(\bar V)$$는 solvable Lie algebra $$\mathfrak{g}$$의 준동형상으로서 solvable이다. ([명제 14](#prop14)) $$\dim\bar V=n-1$$이므로 귀납 가정에 의해 flag

$$0=\bar V_0\subsetneq\bar V_1\subsetneq\cdots\subsetneq\bar V_{n-1}=\bar V$$

이 존재하여 모든 $$\bar x$$에 대하여 $$\bar x\bar V_i\subseteq\bar V_i$$이다. 몫사상에 의한 $$\bar V_i$$의 역상을 $$V_{i+1}$$로 두면 $$V_1\subsetneq V_2\subsetneq\cdots\subsetneq V_n=V$$이고 $$\dim V_{i+1}=i+1$$이며 $$xV_{i+1}\subseteq V_{i+1}$$이다. 이 flag에 맞춘 기저에서 $$\mathfrak{g}$$의 원소는 모두 상삼각행렬이다.

</details>

추상적 형태로 다시 쓰면, $$k$$가 대수적으로 닫힌 표수 $$0$$의 체이고 $$\mathfrak{g}$$가 유한차원 solvable Lie algebra이면, [따름정리 21](#cor21)를 adjoint representation $$\ad:\mathfrak{g}\rightarrow\mathfrak{gl}(\mathfrak{g})$$의 상에 적용하여 $$\ad\mathfrak{g}$$가 동시 상삼각화됨을 알 수 있다. 그 직접적인 귀결로 $$[\mathfrak{g},\mathfrak{g}]$$의 원소들은 모두 strictly 상삼각인 $$\ad$$로 작용하므로, $$x\in[\mathfrak{g},\mathfrak{g}]$$에 대하여 $$\ad x$$가 nilpotent endomorphism이 된다. 따라서 [정리 18](#thm18)에 의해 $$[\mathfrak{g},\mathfrak{g}]$$는 nilpotent이다. 즉 표수 $$0$$의 대수적으로 닫힌 체 위에서 solvable Lie algebra의 derived algebra는 항상 nilpotent이며, 이는 Cartan의 판정법과 더불어 반단순 Lie algebra의 구조 이론으로 이어지는 출발점이 된다.

---

**참고문헌**

**[Hum]** J. E. Humphreys, *Introduction to Lie algebras and representation theory*, Graduate Texts in Mathematics, Springer, 1972.  
**[Bou]** N. Bourbaki, *Lie groups and Lie algebras, Chapters 1–3*, Springer, 1989.  
**[Ser]** J.-P. Serre, *Lie algebras and Lie groups*, Lecture Notes in Mathematics, Springer, 2006.  

---
