---
title: "Weyl 완전가약성 정리"
description: "Semisimple Lie algebra의 유한차원 표현에 대한 Casimir element를 nondegenerate invariant form의 dual basis로 구성하여 그 trace가 dim g임을 보이고, 이를 통해 Whitehead 보조정리와 짧은 완전열의 분할을 증명한다. 그 귀결로 semisimple Lie algebra의 모든 유한차원 표현이 기약 표현의 직합으로 완전가약임을 보이는 Weyl 정리를 확립한다."
excerpt: "표현의 Casimir element, trace 공식, Whitehead 보조정리, 완전열의 분할, Weyl 완전가약성 정리"

categories: [Math / Lie Theory]
permalink: /ko/math/lie_theory/weyl_complete_reducibility
sidebar: 
    nav: "lie_theory-ko"

date: 2026-06-21
weight: 7.2

published: false
---

Semisimple Lie algebra $$\mathfrak{g}$$의 표현론은 그 첫 번째 근본 정리로 완전가약성을 갖는다. 곧 $$\mathfrak{g}$$의 모든 유한차원 표현은 기약 표현들의 직합으로 분해된다. Compact Lie group의 표현에 대해서는 invariant inner product를 Haar measure로 평균내어 임의의 invariant subspace의 orthogonal complement가 다시 invariant임을 보이는 unitarian trick이 같은 결론을 즉시 주지만, $$\SL(n;\mathbb{C})$$와 같은 noncompact group 또는 추상 semisimple Lie algebra에는 이 적분 논법을 직접 적용할 수 없다. 우리는 이미 $$\sl_2$$의 경우에 한해 완전가약성을 Casimir element로 증명하였으며 ([§sl₂의 표현론, ⁋정리 9](/ko/math/lie_theory/representations_of_sl2#thm9)), 이 글에서는 같은 전략을 임의의 semisimple Lie algebra로 확장한다.

핵심 도구는 표현마다 정의되는 Casimir element이다. Cartan의 판정법으로 semisimple Lie algebra의 Killing form이 nondegenerate임을 알고 있으므로 ([§Killing 형식과 Cartan 판정법, ⁋정리 9](/ko/math/lie_theory/killing_form_and_cartan_criterion#thm9)), 표현이 정의하는 invariant bilinear form 역시 nondegenerate가 되도록 만들 수 있고, 그 dual basis로부터 $$\rho(\mathfrak{g})$$ 전체와 교환하는 보편 포락 대수의 원소를 얻는다. 이 원소가 각 기약 인자 위에서 스칼라로 작용하면서도 trace가 표현의 차원과 무관하게 $$\dim\mathfrak{g}$$로 고정된다는 사실이, 짧은 완전열이 항상 분할됨을 보이는 정밀한 산술을 가능하게 한다. 이 글 전체에서 $$k$$는 대수적으로 닫힌 표수 $$0$$의 체이고, $$\mathfrak{g}$$는 $$k$$ 위의 유한차원 semisimple Lie algebra이며, 표현이라 하면 모두 유한차원 $$k$$-표현을 뜻한다.

## 표현의 Casimir element

$$\sl_2$$의 경우 Casimir element는 보편 포락 대수의 중심 원소 $$\Omega=ef+fe+\tfrac{1}{2}h^2$$로 직접 주어졌다 ([§보편 포락 대수, ⁋예시 12](/ko/math/lie_theory/universal_enveloping_algebra#ex12)). 일반적인 semisimple Lie algebra에서는 이러한 명시적 공식 대신, 표현이 결정하는 nondegenerate invariant bilinear form의 dual basis를 통해 같은 종류의 원소를 구성한다. 먼저 그 bilinear form을 정한다.

표현 $$\rho:\mathfrak{g}\rightarrow\gl(V)$$가 주어지면 ([§보편 포락 대수, ⁋명제 4](/ko/math/lie_theory/universal_enveloping_algebra#prop4) 이후의 논의), $$V$$ 위의 endomorphism들의 trace를 통해 $$\mathfrak{g}$$ 위에 bilinear form

$$\beta(x,y)=\tr\bigl(\rho(x)\rho(y)\bigr)$$

가 정해진다. $$\tr(fg)=\tr(gf)$$이므로 $$\beta$$는 symmetric이고, 또한 임의의 $$x,y,z\in\mathfrak{g}$$에 대하여 $$\beta([x,y],z)=\beta(x,[y,z])$$가 성립하는 *invariant<sub>불변</sub>* form이다. 이 invariance는 Killing form의 경우와 똑같이 $$\rho$$가 Lie algebra homomorphism이라는 데에서 $$\rho([x,y])=[\rho(x),\rho(y)]$$를 쓰고 trace의 항등식 $$\tr([f,g]h)=\tr(f[g,h])$$를 적용하여 얻어진다 ([§Killing 형식과 Cartan 판정법, ⁋명제 2](/ko/math/lie_theory/killing_form_and_cartan_criterion#prop2)). Killing form $$\kappa$$ 자신은 adjoint representation $$\rho=\ad$$에 대한 $$\beta$$에 다름 아니다.

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1**</ins> $$\rho:\mathfrak{g}\rightarrow\gl(V)$$가 faithful representation, 곧 $$\ker\rho=0$$이면, bilinear form $$\beta(x,y)=\tr\bigl(\rho(x)\rho(y)\bigr)$$는 nondegenerate이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\beta$$의 radical $$S=\{x\in\mathfrak{g}\mid\beta(x,y)=0\text{ for all }y\in\mathfrak{g}\}$$을 생각한다. $$\beta$$가 invariant이므로 임의의 $$x\in S$$, $$z\in\mathfrak{g}$$에 대하여 모든 $$y$$에 대해 $$\beta([z,x],y)=-\beta(x,[z,y])=0$$이고, 따라서 $$[z,x]\in S$$, 곧 $$S$$는 $$\mathfrak{g}$$의 ideal이다.

$$\rho(S)\subseteq\gl(V)$$는 부분대수이며, 정의에 의해 모든 $$x\in S$$, $$y\in S$$에 대하여 $$\tr\bigl(\rho(x)\rho(y)\bigr)=\beta(x,y)=0$$이다. 특히 $$[\rho(S),\rho(S)]\subseteq\rho(S)$$의 원소와 $$\rho(S)$$의 원소를 곱한 trace가 모두 $$0$$이므로, Cartan의 가해성 판정법 ([§Killing 형식과 Cartan 판정법, ⁋정리 7](/ko/math/lie_theory/killing_form_and_cartan_criterion#thm7))에 의해 $$\rho(S)$$는 solvable이다. $$\rho$$가 faithful이므로 $$S\cong\rho(S)$$이고 따라서 $$S$$ 자신이 solvable ideal이다. 그런데 $$\mathfrak{g}$$가 semisimple이므로 $$0$$이 아닌 solvable ideal을 갖지 않고 ([§가해 Lie algebra와 nilpotent Lie algebra, ⁋정의 15](/ko/math/lie_theory/solvable_nilpotent_lie_algebras#def15) 이후의 논의), 그러므로 $$S=0$$, 곧 $$\beta$$는 nondegenerate이다.

</details>

표현이 faithful이 아니더라도 $$\ker\rho$$는 $$\mathfrak{g}$$의 ideal이고, semisimple Lie algebra의 ideal에 의한 몫은 다시 semisimple이므로 ($$\mathfrak{g}=\ker\rho\oplus(\ker\rho)^{\perp}$$의 직합 분해에서 $$\mathfrak{g}/\ker\rho$$가 simple ideal들의 직합이 됨, [§Killing 형식과 Cartan 판정법, ⁋정리 10](/ko/math/lie_theory/killing_form_and_cartan_criterion#thm10)) $$\rho$$가 결정하는 faithful representation $$\bar\rho:\mathfrak{g}/\ker\rho\rightarrow\gl(V)$$에 위 명제를 적용할 수 있다. 그러나 아래의 구성을 가장 매끄럽게 진행하려면, faithful이 아닌 경우에 $$\beta$$ 대신 항상 nondegenerate인 Killing form $$\kappa$$를 쓰는 편이 편리하다. 우선 faithful한 경우의 구성을 먼저 서술한다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> $$\rho:\mathfrak{g}\rightarrow\gl(V)$$가 faithful representation이라 하고, $$\beta(x,y)=\tr\bigl(\rho(x)\rho(y)\bigr)$$를 [명제 1](#prop1)의 nondegenerate invariant form이라 하자. $$\mathfrak{g}$$의 기저 $$(x_1,\ldots,x_n)$$과 그에 대한 $$\beta$$-dual basis $$(x^1,\ldots,x^n)$$, 곧 $$\beta(x_i,x^j)=\delta_i^j$$를 만족하는 기저를 택할 때, 보편 포락 대수 $$U(\mathfrak{g})$$의 원소

$$c_\rho=\sum_{i=1}^{n}x_i\,x^i$$

의 $$\rho$$에 의한 상 $$\rho(c_\rho)=\sum_{i=1}^{n}\rho(x_i)\rho(x^i)\in\End(V)$$를 표현 $$\rho$$의 *Casimir element<sub>카시미르 원소</sub>*라 부른다.

</div>

$$\beta$$가 nondegenerate이므로 임의의 기저 $$(x_i)$$에 대하여 $$\beta(x_i,x^j)=\delta_i^j$$를 만족하는 dual basis $$(x^i)$$가 유일하게 존재한다. 표기를 절약하기 위해 $$U(\mathfrak{g})$$의 원소 $$c_\rho=\sum_i x_i x^i$$와 그 $$\End(V)$$에서의 상을 같은 기호로 적고, 문맥에 따라 둘을 구별한다. 아래 [명제 3](#prop3)에서 보듯 이 원소는 기저의 선택에 의존하지 않으며, $$\rho(\mathfrak{g})$$ 전체와 교환한다. $$\sl_2$$의 표준 표현에서 $$\beta(x,y)=\tr(xy)$$에 대한 dual basis를 계산하면 $$c_\rho$$가 [§보편 포락 대수, ⁋예시 12](/ko/math/lie_theory/universal_enveloping_algebra#ex12)의 $$\Omega$$와 (스칼라 배를 무시하고) 일치함을 확인할 수 있다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> [정의 2](#def2)의 Casimir element $$\rho(c_\rho)$$는 기저 $$(x_i)$$의 선택에 의존하지 않으며, 임의의 $$x\in\mathfrak{g}$$에 대하여 $$[\rho(x),\rho(c_\rho)]=0$$이다. 곧 $$\rho(c_\rho)$$는 $$\rho(\mathfrak{g})$$의 모든 원소와 교환하는 $$\mathfrak{g}$$-equivariant endomorphism이다. 나아가

$$\tr\bigl(\rho(c_\rho)\bigr)=\dim\mathfrak{g}$$

이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

먼저 trace를 계산한다. $$\rho(c_\rho)=\sum_i\rho(x_i)\rho(x^i)$$이므로 trace의 선형성에서

$$\tr\bigl(\rho(c_\rho)\bigr)=\sum_{i=1}^{n}\tr\bigl(\rho(x_i)\rho(x^i)\bigr)=\sum_{i=1}^{n}\beta(x_i,x^i)=\sum_{i=1}^{n}\delta_i^i=n=\dim\mathfrak{g}$$

를 얻는다.

기저 독립성과 $$\rho(\mathfrak{g})$$와의 교환성을 보이기 위해, $$x\in\mathfrak{g}$$를 고정하고 그 adjoint 작용을 두 dual basis로 전개한다. $$[x,x_i]=\sum_j a_{ij}x_j$$, $$[x,x^i]=\sum_j b_{ij}x^j$$로 쓰면, $$\beta$$의 invariance에서

$$a_{ik}=\beta\bigl([x,x_i],x^k\bigr)=-\beta\bigl(x_i,[x,x^k]\bigr)=-b_{ki}$$

가 성립한다 (양변에서 $$\beta(x_i,x^k)=\delta_i^k$$의 계수를 비교). 이제 $$U(\mathfrak{g})$$ 안에서 commutator $$[\,\cdot\,,\,\cdot\,]$$가 Leibniz 규칙을 만족함을 써서

$$\begin{aligned}
[x,c_\rho]&=\sum_{i}[x,x_i x^i]=\sum_i\bigl([x,x_i]x^i+x_i[x,x^i]\bigr)\\
&=\sum_{i,j}a_{ij}\,x_j x^i+\sum_{i,j}b_{ij}\,x_i x^j\\
&=\sum_{i,j}a_{ij}\,x_j x^i-\sum_{i,j}a_{ji}\,x_i x^j
\end{aligned}$$

을 얻는데, 둘째 합에서 첨자 $$i,j$$의 이름을 맞바꾸면 두 합이 정확히 상쇄되어 $$[x,c_\rho]=0$$이다. 여기에서 $$[x,x_i x^i]$$의 commutator는 $$U(\mathfrak{g})$$ 안의 결합 곱에 대한 것이며, $$\rho$$가 결합대수 준동형 $$U(\mathfrak{g})\rightarrow\End(V)$$로 올라가므로 ([§보편 포락 대수, ⁋명제 4](/ko/math/lie_theory/universal_enveloping_algebra#prop4)) 이를 $$\rho$$로 보내면 $$[\rho(x),\rho(c_\rho)]=\rho([x,c_\rho])=0$$이 된다.

기저 독립성은 다음과 같이 본다. $$\rho(c_\rho)$$를 다른 기저 $$(y_i)$$와 그 dual basis $$(y^i)$$로 구성한 원소를 $$\rho(c'_\rho)$$라 하면, 두 기저 사이의 변환행렬과 그 dual 변환행렬이 서로 transpose-inverse 관계이므로 $$\sum_i x_i\otimes x^i=\sum_i y_i\otimes y^i$$가 $$\mathfrak{g}\otimes\mathfrak{g}$$ 안에서 같은 원소임이 따라온다. 이는 $$\beta$$가 정하는 동형 $$\mathfrak{g}\cong\mathfrak{g}^\ast$$ 아래에서 $$\sum_i x_i\otimes x^i$$가 항등사상 $$\id_{\mathfrak{g}}\in\mathfrak{g}\otimes\mathfrak{g}^\ast\cong\End(\mathfrak{g})$$에 대응하는 canonical element라는 사실의 표현이다. 곱사상 $$\mathfrak{g}\otimes\mathfrak{g}\rightarrow U(\mathfrak{g})$$로 보내면 $$c_\rho=c'_\rho$$이고, 따라서 $$\rho(c_\rho)$$는 기저에 의존하지 않는다.

</details>

$$\rho(c_\rho)$$가 $$\rho(\mathfrak{g})$$ 전체와 교환한다는 것은, $$V$$ 위의 모든 $$\mathfrak{g}$$-부분표현이 $$\rho(c_\rho)$$에 대해 불변이고 $$\rho(c_\rho)$$가 $$\mathfrak{g}$$-equivariant라는 뜻이다. 따라서 $$V$$가 기약이면 Schur의 보조정리에 의해 $$\rho(c_\rho)$$는 스칼라로 작용하며, 그 스칼라는 trace를 차원으로 나눈 $$\dim\mathfrak{g}/\dim V$$로 결정된다. 특히 $$V\neq 0$$인 기약 표현에서 이 스칼라는 $$\dim\mathfrak{g}/\dim V\neq 0$$이므로 $$\rho(c_\rho)$$는 가역이다. 이 가역성이 다음 절에서 완전열을 분할하는 데에 결정적으로 쓰인다.

<div class="remark" markdown="1">

<ins id="rmk4">**참고 4**</ins> $$\rho$$가 faithful이 아닐 때에는 $$\ker\rho\neq 0$$이고, 위 trace 계산에서 $$\dim\mathfrak{g}$$ 대신 faithful한 몫 $$\mathfrak{g}/\ker\rho$$의 차원이 나타난다. 이 경우에도 $$\mathfrak{g}/\ker\rho$$ 위의 trace form으로 같은 구성을 하거나, 혹은 항상 nondegenerate인 Killing form $$\kappa$$를 $$\beta$$ 대신 사용하여 Casimir element를 정의할 수 있다. 어느 경우든 [명제 3](#prop3)의 교환성과 trace의 비자명성($$\tr\rho(c_\rho)\neq 0$$ 단 $$\rho(\mathfrak{g})\neq 0$$)이 유지되며, 아래의 정리는 그 두 성질만을 사용한다.

</div>

## 1차원 몫의 분할과 Whitehead 보조정리

완전가약성은 본질적으로 모든 짧은 완전열 $$0\rightarrow W\rightarrow V\rightarrow V/W\rightarrow 0$$이 분할된다는 것과 동치이다. 분할의 가장 핵심적인 경우는 몫 $$V/W$$가 $$1$$차원 자명 표현일 때이며, 이 경우를 Casimir element로 직접 다루는 것이 다음 보조정리이다. 일반적인 경우는 표준적인 $$\Hom$$-공간 trick으로 이 경우에 환원된다.

먼저 자명 표현으로의 사상에 관한 한 가지 관찰을 둔다. $$\mathfrak{g}$$가 semisimple이면 $$\mathfrak{g}=[\mathfrak{g},\mathfrak{g}]$$이고, 따라서 $$\mathfrak{g}$$에서 abelian Lie algebra인 $$1$$차원 자명 표현 $$\gl(k)=k$$로 가는 표현은 모두 $$0$$이다. 곧 $$1$$차원 표현 위에서 $$\mathfrak{g}$$는 자명하게 작용한다. ($$[\mathfrak{g},\mathfrak{g}]=\mathfrak{g}$$인 것은 [§Killing 형식과 Cartan 판정법, ⁋정리 10](/ko/math/lie_theory/killing_form_and_cartan_criterion#thm10)의 simple ideal 분해에서 각 simple 성분이 $$[\mathfrak{g}_i,\mathfrak{g}_i]=\mathfrak{g}_i$$를 만족하는 데에서 따라온다.)

<div class="proposition" markdown="1">

<ins id="lem5">**보조정리 5**</ins> $$V$$가 $$\mathfrak{g}$$의 표현이고 $$W\subseteq V$$가 codimension $$1$$의 부분표현이며, 몫 $$V/W$$ 위에서 $$\mathfrak{g}$$가 자명하게 작용한다고 하자. 그럼 $$V$$의 $$1$$차원 부분표현 $$L$$이 존재하여

$$V=W\oplus L$$

이 $$\mathfrak{g}$$-불변 직합이 된다. 곧 완전열 $$0\rightarrow W\rightarrow V\rightarrow V/W\rightarrow 0$$이 분할된다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

표현을 정의하는 사상을 $$\rho:\mathfrak{g}\rightarrow\gl(V)$$라 한다. $$V/W$$ 위에서 $$\mathfrak{g}$$가 자명하게 작용하므로, 임의의 $$x\in\mathfrak{g}$$에 대하여 $$\rho(x)V\subseteq W$$이고, 특히 $$\rho(x)W\subseteq W$$이다. $$\dim W$$에 대한 귀납법으로 $$W$$가 기약인 경우로 환원한 뒤, 기약인 경우를 Casimir element로 처리한다.

먼저 $$W$$가 기약인 경우를 보인다. $$W$$ 위에서 $$\mathfrak{g}$$가 자명하게 작용하면 $$V$$ 위에서도 $$\mathfrak{g}$$가 nilpotent하게만 작용하여 ($$\rho(x)V\subseteq W$$이고 $$\rho(x)W=0$$이므로 $$\rho(x)^2=0$$) $$\rho(\mathfrak{g})=[\rho(\mathfrak{g}),\rho(\mathfrak{g})]$$의 원소들의 trace가 $$0$$인 한편 이들은 nilpotent이고, $$\rho$$의 상이 $$\mathfrak{g}$$의 몫이라 semisimple이므로 abelian 성분이 없어 $$\rho=0$$이 되어 임의의 $$1$$차원 보충 $$L$$이 분할을 준다. 그러므로 $$W$$ 위에서 $$\mathfrak{g}$$가 비자명하게 작용하는 경우, 곧 $$\rho\vert_W$$가 $$0$$이 아닌 기약 표현인 경우만 다루면 된다.

이 경우 표현 $$\rho:\mathfrak{g}\rightarrow\gl(V)$$의 Casimir element $$c=\rho(c_\rho)$$를 생각한다 ([정의 2](#def2), [참고 4](#rmk4)). [명제 3](#prop3)에 의해 $$c$$는 $$\rho(\mathfrak{g})$$와 교환하므로 $$\ker c$$와 $$\im c$$는 모두 $$V$$의 부분표현이다. $$\mathfrak{g}$$는 $$V/W\cong k$$ 위에서 자명하게 작용하므로 $$c$$도 $$V/W$$ 위에서 $$0$$으로 작용하고, 따라서 $$c(V)\subseteq W$$이다. 한편 $$W$$가 $$0$$이 아닌 기약 표현이므로 [명제 3](#prop3) 이후의 논의에 의해 $$c\vert_W$$는 $$0$$이 아닌 스칼라배, 곧 $$W$$ 위에서 가역이다. 그러므로 $$c:V\rightarrow W$$는 전사이고, $$\dim V=\dim W+1$$에서 $$\ker c$$는 $$1$$차원이며 $$\ker c\cap W=0$$이다. $$L=\ker c$$로 두면 $$L$$은 $$\mathfrak{g}$$-불변인 $$1$$차원 부분표현이고 $$V=W\oplus L$$이다.

이제 $$W$$가 기약이 아닌 일반적인 경우를 $$\dim W$$에 대한 귀납법으로 처리한다. $$W$$가 $$0$$이 아닌 진부분표현 $$W'\subsetneq W$$를 가지면, 몫 표현 $$V/W'$$을 생각한다. $$W/W'$$은 $$V/W'$$의 codimension $$1$$ 부분표현이고 $$(V/W')/(W/W')\cong V/W$$ 위에서 $$\mathfrak{g}$$가 자명하게 작용하므로, $$\dim(W/W')<\dim W$$에 대한 귀납 가정에서 $$\mathfrak{g}$$-불변 직합 $$V/W'=(W/W')\oplus(\widetilde{L}/W')$$이 존재한다. 여기에서 $$\widetilde{L}$$은 $$W'$$을 포함하고 $$\dim\widetilde{L}=\dim W'+1$$인 $$V$$의 부분표현이다. 그럼 $$W'$$은 $$\widetilde{L}$$의 codimension $$1$$ 부분표현이고 $$\widetilde{L}/W'$$ 위에서 $$\mathfrak{g}$$가 자명하게 작용하므로, 다시 $$\dim W'<\dim W$$에 대한 귀납 가정에서 $$\mathfrak{g}$$-불변 직합 $$\widetilde{L}=W'\oplus L$$, $$\dim L=1$$이 존재한다. 이 $$L$$이 구하는 보충이다. 실제로 $$L\subseteq\widetilde{L}$$이고 $$L\cap W'=0$$이며, $$\widetilde{L}/W'$$이 $$V/W'$$에서 $$W/W'$$과 직합을 이루므로 $$L\cap W\subseteq\widetilde{L}\cap W=W'$$과 $$L\cap W'=0$$에서 $$L\cap W=0$$이고, 차원을 세면 $$V=W\oplus L$$이다.

</details>

위 보조정리가 다루는 것은 몫이 자명 표현인 특별한 경우뿐이지만, 임의의 짧은 완전열의 분할은 $$\Hom$$ 공간 위의 작용을 통해 이 경우로 환원된다. 두 표현 $$V,W$$에 대하여 벡터공간 $$\Hom_k(V,W)$$는 $$(x\cdot f)(v)=\rho_W(x)f(v)-f\bigl(\rho_V(x)v\bigr)$$로 정의되는 자연스러운 $$\mathfrak{g}$$-표현 구조를 가지며, 이 작용에 대해 $$f$$가 불변, 곧 $$x\cdot f=0$$인 것과 $$f$$가 $$\mathfrak{g}$$-equivariant인 것이 동치이다. 이 관찰이 다음 정리, 곧 Whitehead 보조정리의 표현론적 형태로 이어진다.

<div class="proposition" markdown="1">

<ins id="thm6">**정리 6 (Whitehead 보조정리)**</ins> $$\mathfrak{g}$$가 semisimple이고 $$V$$가 $$\mathfrak{g}$$의 표현이라 하자. $$W\subseteq V$$가 부분표현이면, $$\mathfrak{g}$$-equivariant projection $$\pi:V\rightarrow W$$, 곧 $$\pi\vert_W=\id_W$$인 $$\mathfrak{g}$$-사상 $$\pi$$가 존재한다. 동치로, 완전열 $$0\rightarrow W\rightarrow V\rightarrow V/W\rightarrow 0$$은 분할된다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\mathcal{H}=\Hom_k(V,W)$$ 위에 위에서 서술한 $$\mathfrak{g}$$-작용을 준다. 그 부분공간들

$$\begin{aligned}
\mathcal{V}&=\{f\in\mathcal{H}\mid f\vert_W=\lambda\cdot\id_W\text{ for some }\lambda\in k\},\\
\mathcal{W}&=\{f\in\mathcal{H}\mid f\vert_W=0\}
\end{aligned}$$

를 생각한다. $$f\vert_W$$가 $$\id_W$$의 스칼라배라는 조건과 $$0$$이라는 조건은 모두 $$\mathfrak{g}$$-작용에 대해 닫혀 있어 $$\mathcal{V},\mathcal{W}$$는 부분표현이고, $$\mathcal{W}\subseteq\mathcal{V}$$이다. $$f\mapsto\lambda$$로 주어지는 사상 $$\mathcal{V}\rightarrow k$$은 전사이고 그 핵이 $$\mathcal{W}$$이므로 $$\mathcal{V}/\mathcal{W}\cong k$$는 $$1$$차원이다. 더구나 이 몫 위에서 $$\mathfrak{g}$$는 자명하게 작용한다. 임의의 $$f\in\mathcal{V}$$($$f\vert_W=\lambda\id_W$$)와 $$x\in\mathfrak{g}$$, $$w\in W$$에 대하여

$$(x\cdot f)(w)=\rho_W(x)f(w)-f\bigl(\rho_V(x)w\bigr)=\lambda\,\rho_W(x)w-\lambda\,\rho_W(x)w=0$$

이므로 ($$W$$가 부분표현이라 $$\rho_V(x)w=\rho_W(x)w$$) $$x\cdot f\in\mathcal{W}$$, 곧 $$x$$의 작용이 $$\mathcal{V}$$를 $$\mathcal{W}$$ 안으로 보낸다.

따라서 $$\mathcal{W}\subseteq\mathcal{V}$$는 codimension $$1$$의 부분표현이고 몫 위에서 $$\mathfrak{g}$$가 자명하게 작용하므로, [보조정리 5](#lem5)에 의해 $$\mathfrak{g}$$-불변 직합 $$\mathcal{V}=\mathcal{W}\oplus L$$, $$\dim L=1$$이 존재한다. $$L$$의 생성원 $$f_0$$를 그 위에서 $$\mathfrak{g}$$가 자명하게 작용하도록, 곧 $$x\cdot f_0=0$$이 모든 $$x$$에 대해 성립하도록 택할 수 있고, $$f_0\notin\mathcal{W}$$이므로 $$f_0\vert_W=\lambda\id_W$$에서 $$\lambda\neq 0$$이다. $$\pi=\lambda^{-1}f_0$$로 두면 $$\pi\vert_W=\id_W$$이고, $$x\cdot\pi=0$$은 정확히 $$\pi$$가 $$\mathfrak{g}$$-equivariant라는 진술이다. 이 $$\pi$$는 $$V$$를 $$W$$ 위로 보내는 $$\mathfrak{g}$$-사상 projection이고, $$\ker\pi$$는 $$\pi$$가 equivariant이므로 부분표현이며 $$V=W\oplus\ker\pi$$가 분할을 준다.

</details>

[정리 6](#thm6)에서 $$\pi$$가 $$\mathfrak{g}$$-equivariant이므로 $$\ker\pi$$는 $$V$$의 부분표현이고, $$\pi\vert_W=\id_W$$에서 $$W\cap\ker\pi=0$$, 차원 비교로 $$V=W\oplus\ker\pi$$가 따라온다. 곧 임의의 부분표현 $$W$$는 $$\mathfrak{g}$$-불변 보충을 갖는다. 이 한 문장이 다음 절의 완전가약성을 즉시 함의한다.

## Weyl 완전가약성 정리

이제 짧은 완전열의 분할로부터 표현이 기약 표현들의 직합으로 분해됨을 차원에 대한 귀납법으로 얻는다.

<div class="proposition" markdown="1">

<ins id="thm7">**정리 7 (Weyl 완전가약성 정리)**</ins> $$\mathfrak{g}$$가 $$k$$ 위의 유한차원 semisimple Lie algebra이면, $$\mathfrak{g}$$의 모든 유한차원 표현은 *completely reducible<sub>완전가약</sub>*이다. 곧 임의의 유한차원 표현 $$V$$는 기약 부분표현들의 직합으로 분해된다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\dim V$$에 대한 귀납법으로 보인다. $$V=0$$이면 빈 직합으로서 자명하다. $$V\neq 0$$이라 하자. $$V$$ 자신이 기약이면 분해는 $$V$$ 한 항으로 이루어지므로 끝이다. 그렇지 않으면 $$0\neq W\subsetneq V$$인 부분표현 $$W$$가 존재한다. [정리 6](#thm6)에 의해 $$\mathfrak{g}$$-불변 보충 $$W'$$이 존재하여 $$V=W\oplus W'$$이다. $$W$$와 $$W'$$은 모두 $$0$$이 아닌 진부분표현이므로 $$\dim W,\dim W'<\dim V$$이고, 귀납 가정에 의해 각각 기약 부분표현들의 직합으로 분해된다. 두 분해를 합치면 $$V$$가 기약 부분표현들의 직합이 된다.

</details>

이 정리는 $$\sl_2$$에 대해 이미 얻었던 결과 ([§sl₂의 표현론, ⁋정리 9](/ko/math/lie_theory/representations_of_sl2#thm9))를 임의의 semisimple Lie algebra로 일반화한다. $$\sl_2$$의 경우 명시적 Casimir element $$\Omega$$와 highest weight 이론으로 직접 분해를 읽어낼 수 있었던 반면, 일반적인 경우에는 nondegenerate invariant form의 dual basis로 만든 Casimir element가 같은 역할을 추상적으로 수행한다. 두 증명의 골격은 동일하다. Casimir element가 자명 표현 위에서 $$0$$, 비자명 기약 표현 위에서 가역 스칼라로 작용한다는 산술이 codimension $$1$$ 완전열을 분할하고, 그로부터 모든 완전열의 분할과 완전가약성이 차례로 따라온다.

완전가약성의 직접적인 귀결로, semisimple Lie algebra가 자기 자신 위에 작용하는 adjoint representation도 완전가약이며, 이것이 [§Killing 형식과 Cartan 판정법, ⁋정리 10](/ko/math/lie_theory/killing_form_and_cartan_criterion#thm10)에서 얻은 simple ideal 분해를 표현론의 언어로 다시 본 것이다.

<div class="proposition" markdown="1">

<ins id="cor8">**따름정리 8**</ins> $$\mathfrak{g}$$가 semisimple이면, adjoint representation $$\ad:\mathfrak{g}\rightarrow\gl(\mathfrak{g})$$는 완전가약이다. 그 기약 성분은 정확히 [§Killing 형식과 Cartan 판정법, ⁋정리 10](/ko/math/lie_theory/killing_form_and_cartan_criterion#thm10)의 simple ideal 분해 $$\mathfrak{g}=\mathfrak{g}_1\oplus\cdots\oplus\mathfrak{g}_r$$의 각 $$\mathfrak{g}_i$$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[정리 7](#thm7)을 표현 $$\ad:\mathfrak{g}\rightarrow\gl(\mathfrak{g})$$에 적용하면 $$\mathfrak{g}$$가 adjoint action에 대한 기약 부분표현들의 직합으로 분해된다. adjoint action에 대한 부분표현이란 정확히 $$\ad(\mathfrak{g})$$-불변 부분공간, 곧 $$\mathfrak{g}$$의 ideal이며, 그것이 기약이라는 것은 $$0$$이 아닌 진부분 ideal을 갖지 않는다는 것이다. abelian이 아닌 ideal 가운데 그러한 것이 simple ideal이므로, 기약 성분들은 simple ideal이다. (자명 표현으로 나타나는 abelian 성분이 있다면 그것은 $$\mathfrak{g}$$의 $$0$$이 아닌 abelian, 따라서 solvable인 ideal이 되어 semisimple성에 모순이므로 존재하지 않는다.)

따라서 분해의 각 성분은 simple ideal이고, [§Killing 형식과 Cartan 판정법, ⁋정리 10](/ko/math/lie_theory/killing_form_and_cartan_criterion#thm10)에 의해 $$\mathfrak{g}$$의 simple ideal들은 유일하게 결정되므로, adjoint representation의 기약 분해는 simple ideal 분해 $$\mathfrak{g}=\mathfrak{g}_1\oplus\cdots\oplus\mathfrak{g}_r$$과 일치한다.

</details>

Weyl의 정리는 semisimple Lie algebra의 표현론을 기약 표현의 분류 문제로 환원한다. 임의의 표현은 그 안에 나타나는 기약 표현들과 각각의 multiplicity로 완전히 결정되며, 따라서 남은 과제는 기약 표현 자체를 분류하는 것이다.

---

**참고문헌**

**[Hum]** J. E. Humphreys, *Introduction to Lie algebras and representation theory*, Graduate Texts in Mathematics, Springer, 1972.  
**[Kna]** A. W. Knapp, *Lie groups beyond an introduction*, 2nd ed., Progress in Mathematics, Birkhäuser, 2002.  
**[FH]** W. Fulton and J. Harris, *Representation theory: a first course*, Graduate Texts in Mathematics, Springer, 1991.  
