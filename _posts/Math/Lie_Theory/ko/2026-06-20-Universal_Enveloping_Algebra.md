---
title: "보편 포락 대수"
description: "Lie algebra의 보편 포락 대수 U(g)를 텐서대수의 몫으로 정의하고, 그 보편 성질과 표준 여과, 그리고 Poincaré–Birkhoff–Witt 정리를 증명한다."
excerpt: "Universal enveloping algebra와 PBW 정리"

categories: [Math / Lie Theory]
permalink: /ko/math/lie_theory/universal_enveloping_algebra
sidebar: 
    nav: "Lie_theory-ko"

date: 2026-06-20
weight: 7

published: false

---

Lie algebra $$\mathfrak{g}$$의 표현론은 본질적으로 결합대수의 가군 이론으로 환원된다. 그 환원을 가능하게 하는 대상이 *universal enveloping algebra*이며, 이는 $$\mathfrak{g}$$의 Lie bracket을 결합대수의 commutator로 실현하는 가장 보편적인 결합대수이다. 이 글에서 우리는 이 대수를 텐서대수의 몫으로 정의하고, 그 보편 성질을 서술한 뒤, 표준 여과<sub>filtration</sub>를 통해 얻어지는 associated graded가 대칭대수와 동형임을 주장하는 Poincaré–Birkhoff–Witt 정리를 증명한다. 이 정리는 자연스러운 사상 $$\mathfrak{g}\rightarrow U(\mathfrak{g})$$가 단사임을 즉시 함의하며, 반단순 Lie algebra의 표현론 전체의 기초가 된다.

이 글 전체에서 $$k$$는 고정된 체이고, $$\mathfrak{g}$$는 $$k$$ 위에 정의된 Lie algebra이다. ([§리 군, ⁋정의 8](/ko/math/lie_theory/Lie_groups#def8)) Lie algebra의 정의는 임의의 체 위에서 동일하게 주어지므로, 우리는 기반 체를 $$k$$로 일반화하여 사용한다.

## 결합대수의 commutator

임의의 결합대수에는 그 곱셈으로부터 자연스럽게 Lie bracket이 정의된다. 보편 포락 대수의 정의는 이 관찰에서 출발한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $$k$$ 위의 결합 단위 대수 $$A$$에 대하여, 다음의 식

$$[a,b]=ab-ba$$

으로 정의되는 연산 $$[-,-]:A\times A\rightarrow A$$을 $$A$$의 *commutator<sub>교환자</sub>*라 부른다.

</div>

이 연산이 anticommutativity와 Jacobi identity를 만족하는 것은 직접 계산으로 확인된다. 실제로 $$[a,b]=ab-ba=-(ba-ab)=-[b,a]$$이며, 임의의 $$a,b,c\in A$$에 대하여

$$\begin{aligned}
[[a,b],c]+[[b,c],a]+[[c,a],b]&=(ab-ba)c-c(ab-ba)\\
&\quad+(bc-cb)a-a(bc-cb)\\
&\quad+(ca-ac)b-b(ca-ac)
\end{aligned}$$

의 우변을 전개하면 여섯 개의 양항과 여섯 개의 음항이 모두 상쇄되어 $$0$$이 된다. 따라서 commutator는 $$A$$의 바탕 벡터공간 위에 Lie algebra 구조를 정의한다. 이렇게 얻어진 Lie algebra를 $$A_{\mathrm{Lie}}$$로 표기하기로 한다. 대응 $$A\mapsto A_{\mathrm{Lie}}$$는 결합 단위 대수에서 Lie algebra로 가는 함자이며, 우리가 정의할 보편 포락 대수는 정확히 이 함자의 left adjoint를 실현한다.

이 함자가 어떤 대상을 보내는지를 살펴보는 가장 단순한 예시는 자기준동형 대수이다. 벡터공간 $$V$$에 대하여 $$\End_k(V)$$는 합성을 곱셈으로 갖는 결합 단위 대수이며, 그 commutator로 얻어지는 Lie algebra를 $$\mathfrak{gl}(V)$$로 표기한다. $$\mathfrak{g}$$의 *representation*이란 Lie algebra 준동형 $$\mathfrak{g}\rightarrow\mathfrak{gl}(V)$$, 곧 $$\mathfrak{g}\rightarrow\End_k(V)_{\mathrm{Lie}}$$를 뜻한다.

## 보편 포락 대수의 정의

이제 우리는 $$\mathfrak{g}$$의 Lie bracket을 commutator로 강제하는 결합대수를 구성한다. $$\mathfrak{g}$$를 단순한 벡터공간으로 보고 그 텐서대수 $$\T(\mathfrak{g})$$를 취하면 ([\[다중선형대수학\] §텐서대수, ⁋정의 1](/ko/math/multilinear_algebra/tensor_algebras#def1)), 이는 $$\mathfrak{g}$$로 생성되는 자유 결합대수이다. 여기에서 $$x\otimes y-y\otimes x$$가 $$[x,y]$$와 일치하도록 적절한 이데알로 몫을 취한다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Lie algebra $$\mathfrak{g}$$에 대하여, 텐서대수 $$\T(\mathfrak{g})$$의 two-sided ideal

$$\mathfrak{I}=\langle\, x\otimes y-y\otimes x-[x,y]\,\mid\, x,y\in\mathfrak{g}\,\rangle$$

을 생각하자. 몫대수

$$U(\mathfrak{g})=\T(\mathfrak{g})/\mathfrak{I}$$

를 $$\mathfrak{g}$$의 *universal enveloping algebra<sub>보편 포락 대수</sub>*라 부른다. 합성 $$\mathfrak{g}=\T^1(\mathfrak{g})\hookrightarrow\T(\mathfrak{g})\twoheadrightarrow U(\mathfrak{g})$$로 얻어지는 $$k$$-linear map을 $$\iota:\mathfrak{g}\rightarrow U(\mathfrak{g})$$로 표기한다.

</div>

생성원 $$x\otimes y-y\otimes x-[x,y]$$는 텐서대수의 degree $$2$$ 성분과 degree $$1$$ 성분이 섞인 비동차<sub>inhomogeneous</sub> 원소이므로, $$\mathfrak{I}$$는 동차 이데알이 아니다. 이는 대칭대수나 외대수를 정의할 때 사용한 동차 이데알 ([\[다중선형대수학\] §텐서대수, ⁋정의 5](/ko/math/multilinear_algebra/tensor_algebras#def5))과의 결정적인 차이이며, 따라서 $$U(\mathfrak{g})$$는 grading을 갖지 않는다. 그 대신 $$U(\mathfrak{g})$$는 아래 [정의 6](#def6)에서 보듯 자연스러운 여과를 가지며, PBW 정리의 핵심은 이 여과의 associated graded가 대칭대수와 동형이라는 데에 있다.

$$U(\mathfrak{g})$$에서 $$\iota(x)\iota(y)-\iota(y)\iota(x)=\iota([x,y])$$가 성립함을 강조해 둔다. 정의에 의하여 $$x\otimes y-y\otimes x-[x,y]\in\mathfrak{I}$$이므로 몫에서 이 원소는 $$0$$이 되고, $$\iota$$가 $$\T^1$$에서의 사상이라는 점을 함께 쓰면 위 등식을 얻는다. 표기의 번거로움을 피하기 위해, 이후 $$\iota$$를 생략하고 $$\mathfrak{g}$$의 원소와 그 $$U(\mathfrak{g})$$에서의 상을 같은 기호로 적으며, $$U(\mathfrak{g})$$에서의 곱은 병치<sub>juxtaposition</sub>로 적는다. 이 표기 하에서 위의 관계는 $$U(\mathfrak{g})$$ 안에서

$$xy-yx=[x,y]\qquad\text{for all $x,y\in\mathfrak{g}$}$$

로 적힌다. 다만 이 시점에서 $$\iota$$가 단사인지는 아직 알 수 없으며, 이는 PBW 정리의 따름정리로 비로소 확립된다. ([따름정리 11](#cor11))

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> $$\mathfrak{g}$$가 abelian Lie algebra, 곧 모든 $$x,y$$에 대하여 $$[x,y]=0$$인 경우를 생각하자. 이 때 $$\mathfrak{I}$$의 생성원은 $$x\otimes y-y\otimes x$$가 되며, 이는 정확히 대칭대수 $$\S(\mathfrak{g})$$를 정의하는 이데알의 생성원이다. 따라서

$$U(\mathfrak{g})\cong\S(\mathfrak{g})$$

이고, $$\mathfrak{g}$$의 기저를 고정하면 이는 다항식 대수 $$k[\x_i]_{i\in I}$$가 된다. ([\[다중선형대수학\] §텐서대수, ⁋명제 8](/ko/math/multilinear_algebra/tensor_algebras#prop8)) 즉 abelian인 경우 보편 포락 대수는 가환대수이며, PBW 정리는 이 동형이 일반적인 $$\mathfrak{g}$$에 대해서도 그 associated graded 수준에서 성립함을 주장하는 것으로 이해할 수 있다.

</div>

## 보편 성질

$$U(\mathfrak{g})$$라는 이름의 "보편"은 다음 성질에서 비롯한다. $$\mathfrak{g}$$에서 임의의 결합대수로 가는 Lie algebra 준동형은 모두 $$\iota$$를 통해 유일하게 인수분해된다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> 임의의 $$k$$ 위의 결합 단위 대수 $$A$$와 Lie algebra 준동형 $$f:\mathfrak{g}\rightarrow A_{\mathrm{Lie}}$$에 대하여, 다음 도식

$$\iota:\mathfrak{g}\rightarrow U(\mathfrak{g}),\qquad f=\bar{f}\circ\iota$$

을 만족하는 결합 단위 대수 준동형 $$\bar{f}:U(\mathfrak{g})\rightarrow A$$가 유일하게 존재한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$f$$를 단순히 벡터공간 사이의 $$k$$-linear map으로 보면, 텐서대수의 보편 성질 ([\[다중선형대수학\] §텐서대수, ⁋명제 2](/ko/math/multilinear_algebra/tensor_algebras#prop2))에 의하여 결합 단위 대수 준동형 $$\tilde{f}:\T(\mathfrak{g})\rightarrow A$$가 유일하게 존재하여 $$\T^1(\mathfrak{g})=\mathfrak{g}$$ 위에서 $$\tilde{f}=f$$이도록 할 수 있다. 이제 $$\tilde{f}$$가 이데알 $$\mathfrak{I}$$를 $$0$$으로 보냄을 보이면 충분하다. $$\mathfrak{I}$$는 $$x\otimes y-y\otimes x-[x,y]$$ 꼴의 원소들로 생성되는 two-sided ideal이므로, 이 생성원들이 $$\ker\tilde{f}$$에 속함을 확인하면 된다. 임의의 $$x,y\in\mathfrak{g}$$에 대하여

$$\tilde{f}(x\otimes y-y\otimes x-[x,y])=f(x)f(y)-f(y)f(x)-f([x,y])=[f(x),f(y)]_A-f([x,y])$$

인데, $$f$$가 Lie algebra 준동형이라는 가정에서 우변이 $$0$$이다. 따라서 $$\mathfrak{I}\subseteq\ker\tilde{f}$$이고, 몫대수의 보편 성질에 의하여 $$\tilde{f}$$는 결합 단위 대수 준동형 $$\bar{f}:U(\mathfrak{g})\rightarrow A$$로 유일하게 내려간다. 구성에 의하여 $$\bar{f}\circ\iota=f$$이다.

유일성은 $$U(\mathfrak{g})$$가 $$\iota(\mathfrak{g})$$로 생성된다는 사실에서 따라온다. $$U(\mathfrak{g})$$는 $$\T(\mathfrak{g})$$의 몫이고 $$\T(\mathfrak{g})$$는 $$\T^1(\mathfrak{g})=\mathfrak{g}$$로 생성되므로, $$\iota(\mathfrak{g})$$ 위에서의 값이 일치하는 두 결합 단위 대수 준동형은 같다. $$\bar{f}\circ\iota=f$$가 $$\iota(\mathfrak{g})$$ 위에서의 값을 결정하므로 $$\bar{f}$$는 유일하다.

</details>

명제 4는 대응 $$f\mapsto\bar{f}$$가 자연스러운 전단사

$$\Hom_{\mathbf{Lie}_k}(\mathfrak{g},A_{\mathrm{Lie}})\cong\Hom_{\mathbf{Alg}_k}(U(\mathfrak{g}),A)$$

를 정의한다는 것으로 다시 쓸 수 있다. 즉 함자 $$U:\mathbf{Lie}_k\rightarrow\mathbf{Alg}_k$$는 commutator 함자 $$(-)_{\mathrm{Lie}}:\mathbf{Alg}_k\rightarrow\mathbf{Lie}_k$$의 left adjoint이며, $$\iota$$는 이 adjunction의 unit이다. 이 동형의 한 가지 직접적인 귀결로, $$\mathfrak{g}$$의 representation $$\mathfrak{g}\rightarrow\End_k(V)_{\mathrm{Lie}}$$들은 정확히 결합대수 준동형 $$U(\mathfrak{g})\rightarrow\End_k(V)$$들, 곧 $$U(\mathfrak{g})$$-가군 구조들과 일대일로 대응한다. 이것이 $$\mathfrak{g}$$의 표현론을 결합대수 $$U(\mathfrak{g})$$의 가군 이론으로 옮기는 다리이다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> Lie algebra 준동형 $$\phi:\mathfrak{g}\rightarrow\mathfrak{h}$$에 대하여, 다음 도식

$$\iota_{\mathfrak{h}}\circ\phi=U(\phi)\circ\iota_{\mathfrak{g}}$$

을 만족하는 결합 단위 대수 준동형 $$U(\phi):U(\mathfrak{g})\rightarrow U(\mathfrak{h})$$가 유일하게 존재하며, 이 대응은 $$U$$를 함자로 만든다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

합성 $$\iota_{\mathfrak{h}}\circ\phi:\mathfrak{g}\rightarrow U(\mathfrak{h})_{\mathrm{Lie}}$$는 Lie algebra 준동형의 합성이므로 다시 Lie algebra 준동형이다. 따라서 [명제 4](#prop4)를 $$A=U(\mathfrak{h})$$, $$f=\iota_{\mathfrak{h}}\circ\phi$$에 적용하면, $$U(\phi)\circ\iota_{\mathfrak{g}}=\iota_{\mathfrak{h}}\circ\phi$$를 만족하는 결합 단위 대수 준동형 $$U(\phi):U(\mathfrak{g})\rightarrow U(\mathfrak{h})$$가 유일하게 존재한다. 함자성은 보편 성질의 유일성 부분에서 따라온다. $$\id_{\mathfrak{g}}$$에 대응되는 $$U(\id_{\mathfrak{g}})$$와 항등사상 $$\id_{U(\mathfrak{g})}$$은 모두 $$\iota_{\mathfrak{g}}$$를 $$\iota_{\mathfrak{g}}$$로 보내므로 유일성에 의해 같고, 두 Lie algebra 준동형 $$\phi,\psi$$에 대하여 $$U(\psi)\circ U(\phi)$$와 $$U(\psi\circ\phi)$$도 같은 방식으로 일치한다.

</details>

## 표준 여과와 associated graded

$$U(\mathfrak{g})$$는 grading을 갖지 않지만, 텐서대수의 grading이 남긴 흔적으로서 여과를 갖는다. 이 여과의 associated graded를 분석하는 것이 PBW 정리로 가는 길이다.

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> 각 정수 $$n\geq 0$$에 대하여, $$U(\mathfrak{g})$$의 부분공간 $$U_n$$을 텐서대수의 부분공간 $$\bigoplus_{m\leq n}\T^m(\mathfrak{g})$$의 몫사상 $$\T(\mathfrak{g})\twoheadrightarrow U(\mathfrak{g})$$에 의한 상으로 정의한다. 즉

$$U_n=\im\Bigl(\textstyle\bigoplus_{m\leq n}\T^m(\mathfrak{g})\longrightarrow U(\mathfrak{g})\Bigr)$$

이다. 이 부분공간들의 증가열 $$U_0\subseteq U_1\subseteq U_2\subseteq\cdots$$을 $$U(\mathfrak{g})$$의 *canonical filtration<sub>표준 여과</sub>*이라 부른다.

</div>

정의에서 $$U_0=k\cdot 1$$이고 $$U_1=k\cdot 1+\iota(\mathfrak{g})$$이며, $$U_n$$은 $$\mathfrak{g}$$의 원소들의 길이 $$n$$ 이하의 곱들로 이루어진 부분공간이다. 합집합 $$\bigcup_{n\geq 0}U_n$$은 $$U(\mathfrak{g})$$ 전체이다. 이 여과가 대수 구조와 양립함은 다음으로 정리된다. 텐서대수의 곱이 degree를 더하므로, 몫에서

$$U_m\cdot U_n\subseteq U_{m+n}$$

이 성립한다. 즉 $$\bigl(U_n\bigr)_{n\geq 0}$$은 $$U(\mathfrak{g})$$를 여과 대수로 만든다.

핵심적인 관찰은 관계식 $$xy-yx=[x,y]$$가 여과의 관점에서 commutator의 degree를 떨어뜨린다는 것이다. $$x,y\in\mathfrak{g}\subseteq U_1$$이면 $$xy,yx\in U_2$$이지만 그 차 $$xy-yx=[x,y]$$는 $$U_1$$에 속한다. 일반적으로 $$a\in U_m$$, $$b\in U_n$$에 대하여 $$ab-ba\in U_{m+n-1}$$이 성립하며, 이는 아래 [보조정리 8](#lem8)에서 정밀하게 다룬다. 이로부터 associated graded는 가환임이 예상된다.

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> 표준 여과 $$\bigl(U_n\bigr)$$에 대한 *associated graded* 대수를

$$\gr U(\mathfrak{g})=\bigoplus_{n\geq 0}U_n/U_{n-1}$$

으로 정의한다. 여기에서 관례상 $$U_{-1}=0$$으로 둔다. $$\gr U(\mathfrak{g})$$의 곱은 $$a\in U_m$$, $$b\in U_n$$의 상 $$\bar{a}\in U_m/U_{m-1}$$, $$\bar{b}\in U_n/U_{n-1}$$에 대하여 $$\bar{a}\cdot\bar{b}=\overline{ab}\in U_{m+n}/U_{m+n-1}$$로 주어진다.

</div>

이 곱이 잘 정의됨은 $$U_m\cdot U_n\subseteq U_{m+n}$$과, $$a$$를 $$U_{m-1}$$의 원소만큼 바꾸면 $$ab$$가 $$U_{m+n-1}$$의 원소만큼 바뀐다는 사실에서 따라온다. $$\gr U(\mathfrak{g})$$는 $$\mathbb{N}$$-graded 결합 단위 대수이다.

<div class="proposition" markdown="1">

<ins id="lem8">**보조정리 8**</ins> $$\gr U(\mathfrak{g})$$는 가환대수이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\gr U(\mathfrak{g})$$가 $$U_1/U_0$$의 상으로 생성되므로, degree $$1$$ 동차원소들이 서로 가환임을 보이면 충분하다. $$x,y\in\mathfrak{g}\subseteq U_1$$에 대하여, 이들의 $$U_1/U_0$$에서의 상을 $$\bar{x},\bar{y}$$라 하자. 그럼 $$\gr U(\mathfrak{g})$$에서

$$\bar{x}\bar{y}-\bar{y}\bar{x}=\overline{xy-yx}\in U_2/U_1$$

인데, $$U(\mathfrak{g})$$에서 $$xy-yx=[x,y]\in\mathfrak{g}\subseteq U_1$$이므로 $$xy-yx$$의 $$U_2/U_1$$에서의 상은 $$0$$이다. 따라서 $$\bar{x}\bar{y}=\bar{y}\bar{x}$$이고, 생성원들이 서로 가환이므로 $$\gr U(\mathfrak{g})$$ 전체가 가환이다.

</details>

$$\gr U(\mathfrak{g})$$가 가환이고 $$\mathfrak{g}$$의 상으로 생성되므로, 대칭대수의 보편 성질 ([\[다중선형대수학\] §텐서대수, ⁋명제 6](/ko/math/multilinear_algebra/tensor_algebras#prop6))에 의하여 자연스러운 결합대수 준동형이 하나 정해진다. $$\mathfrak{g}$$를 $$U_1/U_0\subseteq\gr U(\mathfrak{g})$$로 보내는 $$k$$-linear map은 가환대수로 들어가므로, 유일한 결합대수 준동형

$$\omega:\S(\mathfrak{g})\longrightarrow\gr U(\mathfrak{g})$$

로 확장되며, 이는 grading을 보존한다. $$\gr U(\mathfrak{g})$$가 degree $$1$$ 부분으로 생성되므로 $$\omega$$는 전사이다. PBW 정리의 본질은 $$\omega$$가 동형이라는 것, 곧 단사이기도 하다는 데에 있다.

## Poincaré–Birkhoff–Witt 정리

이제 $$\mathfrak{g}$$의 기저를 고정하고, 그 기저의 순서를 따라 정렬된 단항식들이 $$U(\mathfrak{g})$$의 기저를 이룬다는 정리를 서술한다. 기저의 첨자 집합 $$I$$ 위에 전순서 $$\leq$$를 하나 고정한다.

<div class="proposition" markdown="1">

<ins id="thm9">**정리 9 (Poincaré–Birkhoff–Witt)**</ins> $$\mathfrak{g}$$가 전순서가 주어진 첨자 집합 $$I$$에 대한 기저 $$\bigl(x_i\bigr)_{i\in I}$$를 갖는다 하자. 그럼 정렬된 단항식들

$$x_{i_1}x_{i_2}\cdots x_{i_n},\qquad i_1\leq i_2\leq\cdots\leq i_n,\quad n\geq 0$$

들의 모임은 $$U(\mathfrak{g})$$의 $$k$$-기저를 이룬다. 여기에서 $$n=0$$인 경우 빈 곱은 단위원 $$1$$로 약속한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

정렬된 단항식들이 $$U(\mathfrak{g})$$를 생성함을 먼저 보인다. $$U(\mathfrak{g})$$는 $$\iota(\mathfrak{g})$$로 생성되므로, 임의의 단항식 $$x_{i_1}\cdots x_{i_n}$$ (첨자가 정렬되지 않은 것도 포함)들의 일차결합으로 표현된다. 정렬되지 않은 단항식이 등장하면, 인접한 두 인자 중 $$i_j>i_{j+1}$$인 곳에서 관계식

$$x_{i_j}x_{i_{j+1}}=x_{i_{j+1}}x_{i_j}+[x_{i_j},x_{i_{j+1}}]$$

을 적용한다. 우변의 첫 항은 그 두 인자가 정렬된 단항식이고, 둘째 항 $$[x_{i_j},x_{i_{j+1}}]\in\mathfrak{g}$$는 길이가 $$1$$만큼 줄어든 단항식이다. 각 단항식에 대하여 정렬 위반의 정도를 재는 적당한 자연수, 가령 길이가 같은 단항식들에 대해서는 역위<sub>inversion</sub>의 수를, 길이가 다른 단항식들에 대해서는 먼저 길이를 비교하는 식의 well-ordering을 도입하면, 위 교환을 반복할 때마다 이 값이 엄밀히 감소한다. 따라서 유한 번의 적용 뒤에는 모든 단항식이 정렬된 것이 되며, 정렬된 단항식들이 $$U(\mathfrak{g})$$를 생성한다.

남은 것은 일차독립성이다. 이를 위해 우리는 $$\S(\mathfrak{g})$$ 위에 $$\mathfrak{g}$$의 작용을 구성하여, $$U(\mathfrak{g})$$가 $$\S(\mathfrak{g})$$ 위에 작용하도록 만든다. $$\S(\mathfrak{g})$$는 정렬된 단항식

$$z_S=x_{i_1}x_{i_2}\cdots x_{i_n},\qquad S=(i_1\leq i_2\leq\cdots\leq i_n)$$

들을 기저로 갖는 다항식 대수이다. ([\[다중선형대수학\] §텐서대수, ⁋명제 8](/ko/math/multilinear_algebra/tensor_algebras#prop8)) 여기에서 $$S$$는 $$I$$의 원소들로 이루어진 비내림차순<sub>nondecreasing</sub> 유한열을 가리킨다. 우리는 다음 두 조건을 만족하는 $$k$$-linear 작용 $$x_i\cdot(-):\S(\mathfrak{g})\rightarrow\S(\mathfrak{g})$$들을 구성하고자 한다.

1. $$i\leq S$$ ($$i$$가 $$S$$의 모든 첨자 이하)인 경우 $$x_i\cdot z_S=z_{(i,S)}$$, 곧 $$i$$를 맨 앞에 덧붙인 정렬된 단항식이다.
2. 임의의 $$i,j\in I$$와 $$s\in\S(\mathfrak{g})$$에 대하여 $$x_i\cdot(x_j\cdot s)-x_j\cdot(x_i\cdot s)=[x_i,x_j]\cdot s$$이 성립한다.

여기에서 $$[x_i,x_j]\cdot s$$는 $$[x_i,x_j]=\sum_l c_{ij}^l x_l$$로 전개한 뒤 각 $$x_l\cdot s$$의 일차결합으로 정의한다. 작용을 $$z_S$$의 길이 $$n=\lvert S\rvert$$에 대한 귀납법으로 정의한다. $$x_i\cdot z_S$$를, $$i\leq S$$이면 조건 1로 정의하고, 그렇지 않으면 $$S=(j,S')$$ ($$j<i$$이고 $$j\leq S'$$)로 쓴 뒤

$$x_i\cdot z_S=x_j\cdot(x_i\cdot z_{S'})+[x_i,x_j]\cdot z_{S'}$$

로 정의한다. 우변의 $$x_i\cdot z_{S'}$$은 길이 $$n-1$$짜리 원소에 대한 작용이라 귀납 가정으로 이미 정의되어 있고, 그 결과에 $$x_j$$를 작용시키는 것 또한, $$x_i\cdot z_{S'}$$을 기저 $$z_T$$들로 전개했을 때 각 $$T$$의 길이가 $$n-1$$ 이하이므로 다시 귀납 가정 안에 든다. $$[x_i,x_j]\cdot z_{S'}$$도 길이 $$n-1$$짜리에 대한 작용이다. 이 정의가 조건 1을 만족함은 구성에서 자명하다.

이제 조건 2가 모든 $$i,j$$와 모든 기저원소 $$z_S$$에 대하여 성립함을 $$\lvert S\rvert$$에 대한 귀납법으로 확인한다. 대칭성에 의해 $$i>j$$인 경우만 보면 되고, $$i=j$$이면 좌변이 자명히 $$0$$이며 $$[x_i,x_i]=0$$이다. $$i>j$$이고 $$j\leq S$$인 경우, 작용의 정의가 정확히 $$x_i\cdot(x_j\cdot z_S)=x_j\cdot(x_i\cdot z_S)+[x_i,x_j]\cdot z_S$$가 되도록 위에서 $$x_i\cdot z_{(j,S)}$$을 정의하였으므로 조건 2가 성립한다. $$j\leq S$$가 아닌 일반적인 경우는 $$S=(l,S')$$ ($$l\leq S'$$, $$l<j<i$$)로 쓰고, $$x_l$$을 한 칸 끄집어낸 뒤 길이 $$n-1$$인 $$S'$$에 대한 귀납 가정과 $$\mathfrak{g}$$의 Jacobi identity를 사용하여 정리하면 얻어진다. Jacobi identity가 들어가는 곳은 세 첨자 $$i,j,l$$에 대한 이중 commutator들이 상쇄되어야 하는 부분이며, 이는 $$\mathfrak{g}$$가 Lie algebra라는 가정 ([§리 군, ⁋정의 8](/ko/math/lie_theory/Lie_groups#def8))이 사용되는 유일한 지점이다.

조건 2가 확립되면, 대응 $$x_i\mapsto\bigl(s\mapsto x_i\cdot s\bigr)$$은 $$\mathfrak{g}$$에서 $$\End_k(\S(\mathfrak{g}))_{\mathrm{Lie}}$$로의 Lie algebra 준동형이다. 실제로 조건 2가 바로 $$[x_i,x_j]$$의 작용이 작용들의 commutator와 일치한다는 진술이고, $$\bigl(x_i\bigr)$$가 $$\mathfrak{g}$$의 기저이므로 이는 $$\mathfrak{g}$$ 전체에서의 Lie algebra 준동형으로 확장된다. [명제 4](#prop4)에 의하여 이는 결합대수 준동형, 곧 $$U(\mathfrak{g})$$-가군 구조

$$\rho:U(\mathfrak{g})\longrightarrow\End_k(\S(\mathfrak{g}))$$

로 유일하게 올라간다. 이제 임의의 정렬된 단항식 $$x_{i_1}\cdots x_{i_n}$$ ($$i_1\leq\cdots\leq i_n$$)에 대하여, 이를 $$\rho$$를 통해 $$1\in\S(\mathfrak{g})$$에 작용시키면 조건 1을 반복 적용하여

$$\rho(x_{i_1}\cdots x_{i_n})(1)=x_{i_1}\cdot\bigl(x_{i_2}\cdot(\cdots(x_{i_n}\cdot 1))\bigr)=z_{(i_1,\ldots,i_n)}$$

을 얻는다. 만일 정렬된 단항식들 사이에 비자명한 일차관계 $$\sum_S\lambda_S\,x_{i_1^S}\cdots x_{i_{n_S}^S}=0$$이 $$U(\mathfrak{g})$$에서 성립한다면, 양변에 $$\rho(-)(1)$$을 적용하여 $$\sum_S\lambda_S\,z_S=0$$을 $$\S(\mathfrak{g})$$에서 얻는데, $$z_S$$들은 $$\S(\mathfrak{g})$$의 기저이므로 모든 $$\lambda_S=0$$이다. 따라서 정렬된 단항식들은 일차독립이며, 생성성과 합쳐 $$U(\mathfrak{g})$$의 기저를 이룬다.

</details>

위 증명에서 구성한 작용 $$\rho$$는 $$\S(\mathfrak{g})$$를 $$U(\mathfrak{g})$$-가군으로 만들며, $$1\in\S(\mathfrak{g})$$를 사용하면 $$U(\mathfrak{g})$$에서 $$\S(\mathfrak{g})$$로의 $$k$$-linear 동형 $$u\mapsto\rho(u)(1)$$을 정의한다. 이 동형이 정렬된 단항식 기저를 정렬된 단항식 기저로 보낸다는 점이 일차독립성 논증의 핵심이었다. 정리 9를 associated graded의 언어로 옮기면 다음을 얻는다.

<div class="proposition" markdown="1">

<ins id="thm10">**정리 10**</ins> [정의 7](#def7) 이후 구성한 자연스러운 전사 준동형

$$\omega:\S(\mathfrak{g})\longrightarrow\gr U(\mathfrak{g})$$

는 graded 결합대수의 동형이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\omega$$가 전사임은 [보조정리 8](#lem8) 이후 이미 확인하였으므로 단사임을 보이면 된다. 각 degree $$n$$에서 $$\omega$$가 단사임을 보이면 충분하다. $$\S^n(\mathfrak{g})$$는 길이 정확히 $$n$$인 정렬된 단항식 $$z_S$$ ($$\lvert S\rvert=n$$)들을 기저로 갖고, $$\omega$$는 이를 $$x_{i_1}\cdots x_{i_n}$$의 $$U_n/U_{n-1}$$에서의 상으로 보낸다. degree $$n$$ 성분에서 $$\sum_{\lvert S\rvert=n}\lambda_S\,\omega(z_S)=0$$이라 하면, 이는 $$U_n/U_{n-1}$$에서의 관계, 곧

$$\sum_{\lvert S\rvert=n}\lambda_S\,x_{i_1^S}\cdots x_{i_n^S}\in U_{n-1}$$

을 뜻한다. $$U_{n-1}$$은 길이 $$n-1$$ 이하의 정렬된 단항식들로 생성되므로, 위 식을 옮기면 길이 $$n$$인 정렬된 단항식들과 길이 $$n-1$$ 이하의 정렬된 단항식들 사이의 일차관계가 된다. [정리 9](#thm9)에 의하여 $$U(\mathfrak{g})$$의 모든 정렬된 단항식은 일차독립이므로, 특히 길이 $$n$$짜리 계수들 $$\lambda_S$$는 모두 $$0$$이어야 한다. 따라서 $$\omega$$는 각 degree에서 단사이고, 전체로서 동형이다.

</details>

정리 9와 정리 10은 동일한 사실의 두 표현이다. 정렬된 단항식이 $$U(\mathfrak{g})$$의 기저를 이룬다는 진술은, 여과의 각 층 $$U_n/U_{n-1}$$이 길이 $$n$$짜리 정렬 단항식으로 정확히 생성된다는 것이고, 이는 $$\gr U(\mathfrak{g})$$가 $$\S(\mathfrak{g})$$와 동형이라는 것과 같다. 어느 형태로 쓰든 본질적인 내용은 commutator 관계 $$xy-yx=[x,y]$$가 $$U(\mathfrak{g})$$를 $$\S(\mathfrak{g})$$보다 "작게" 만들지 않는다는 것이며, 그 증명은 Jacobi identity가 무모순성을 보장하는 데에 의존한다.

가장 자주 인용되는 따름정리는 $$\iota$$의 단사성이다. 이는 일견 당연해 보이지만, $$U(\mathfrak{g})$$가 비자명한 관계로 몫을 취해 얻어졌으므로 선험적으로 보장되지 않는다.

<div class="proposition" markdown="1">

<ins id="cor11">**따름정리 11**</ins> 표준 사상 $$\iota:\mathfrak{g}\rightarrow U(\mathfrak{g})$$은 단사이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\iota(\mathfrak{g})$$는 길이 $$1$$인 정렬된 단항식 $$x_i$$들로 생성되며, $$x\in\mathfrak{g}$$를 기저로 $$x=\sum_i a_i x_i$$로 쓰면 $$\iota(x)=\sum_i a_i\, x_i$$이다. [정리 9](#thm9)에 의하여 길이 $$1$$짜리 정렬 단항식 $$x_i$$들은 $$U(\mathfrak{g})$$ 안에서 일차독립이므로, $$\iota(x)=0$$이면 모든 $$a_i=0$$, 곧 $$x=0$$이다. 따라서 $$\iota$$는 단사이다.

</details>

따름정리 11에 의하여 우리는 $$\mathfrak{g}$$를 $$U(\mathfrak{g})$$의 부분공간으로, 더 정확히는 $$U_1/U_0$$과 동일시되는 부분으로 취급할 수 있으며, 이것이 앞서 $$\iota$$를 생략하고 $$\mathfrak{g}\subseteq U(\mathfrak{g})$$로 적은 표기를 정당화한다. 또한 PBW 정리는 $$U(\mathfrak{g})$$의 크기에 대한 구체적인 정보를 준다. $$\mathfrak{g}$$가 유한차원 $$d$$이면, $$U_n/U_{n-1}\cong\S^n(\mathfrak{g})$$의 차원은 $$\binom{n+d-1}{d-1}$$이고, $$U_n$$의 차원은 $$\binom{n+d}{d}$$이다. 또 한 가지 따름정리로, $$\mathfrak{h}\subseteq\mathfrak{g}$$가 부분 Lie algebra이면 포함사상이 유도하는 $$U(\mathfrak{h})\rightarrow U(\mathfrak{g})$$는 단사이다. 이는 $$\mathfrak{h}$$의 기저를 $$\mathfrak{g}$$의 기저로 확장하고 그 순서가 $$\mathfrak{h}$$의 원소들을 앞에 두도록 하면, $$\mathfrak{h}$$의 정렬 단항식이 $$\mathfrak{g}$$의 정렬 단항식 가운데 일부로서 일차독립이기 때문이다.

## 예시: $$U(\sl_2)$$

PBW 정리가 주는 구체적인 그림을 보기 위해 $$\sl_2=\sl(2;k)$$의 보편 포락 대수를 살펴본다. $$\sl_2$$는 traceless $$2\times 2$$ 행렬들의 Lie algebra이며 ([§리 군, ⁋명제 12](/ko/math/lie_theory/Lie_groups#prop12)), 표준 기저

$$h=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad e=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad f=\begin{pmatrix}0&0\\1&0\end{pmatrix}$$

와 commutation relation

$$[h,e]=2e,\quad [h,f]=-2f,\quad [e,f]=h$$

을 갖는다. 이 commutation relation은 $$\sl_2$$의 표현론에서 핵심적인 역할을 하며, $$e,f$$는 각각 weight을 올리고 내리는 raising, lowering operator로 작용한다. ([§근계, ⁋정의 8](/ko/math/lie_theory/root_systems#def8)) 따라서 $$U(\sl_2)$$는 세 생성원 $$e,f,h$$와 관계식

$$he-eh=2e,\qquad hf-fh=-2f,\qquad ef-fe=h$$

로 표시되는 결합대수이다. 첨자에 순서 $$f<h<e$$를 주면, PBW 정리에 의하여 정렬된 단항식

$$f^a\,h^b\,e^c,\qquad a,b,c\geq 0$$

들이 $$U(\sl_2)$$의 기저를 이룬다. 위의 세 관계식은 임의의 단항식을 이 정렬된 꼴로 다시 쓰는 재작성 규칙을 정확히 제공하며, 가령 $$eh$$는 $$he-2e=he-2e$$로, 곧 $$h,e$$를 정렬한 항과 길이가 줄어든 항의 합으로 환원된다.

이 대수의 중심에는 특별한 원소가 하나 존재한다.

<div class="example" markdown="1">

<ins id="ex12">**예시 12**</ins> $$U(\sl_2)$$의 원소

$$\Omega=ef+fe+\tfrac{1}{2}h^2$$

를 *Casimir element*라 부른다. 이 원소는 $$U(\sl_2)$$의 중심에 속한다. 곧 $$\Omega e=e\Omega$$, $$\Omega f=f\Omega$$, $$\Omega h=h\Omega$$이 모두 성립한다.

</div>

실제로 $$\Omega$$가 $$e$$와 가환임을 확인해 보자. 관계식 $$[e,f]=h$$, $$[h,e]=2e$$를 사용하면 $$U(\sl_2)$$ 안에서

$$\begin{aligned}
[\Omega,e]&=[ef,e]+[fe,e]+\tfrac{1}{2}[h^2,e]\\
&=e[f,e]+[fe,e]+\tfrac{1}{2}\bigl(h[h,e]+[h,e]h\bigr)\\
&=-eh+\bigl(f[e,e]+[f,e]e\bigr)+\tfrac{1}{2}\bigl(2he+2eh\bigr)\\
&=-eh-he+he+eh=0
\end{aligned}$$

을 얻는다. 여기에서 $$[ef,e]=e[f,e]+[e,e]f=e(-h)=-eh$$, $$[fe,e]=[f,e]e=-he$$, 그리고 $$[h^2,e]=h[h,e]+[h,e]h=2he+2eh$$를 사용하였다. 같은 방식으로 $$[\Omega,f]=0$$과 $$[\Omega,h]=0$$도 확인되며, $$e,f,h$$가 $$U(\sl_2)$$를 생성하므로 $$\Omega$$는 중심에 속한다. PBW 기저의 관점에서 $$\Omega$$는 정렬 단항식들의 일차결합

$$\Omega=2fe+h+\tfrac{1}{2}h^2$$

으로 다시 쓸 수 있는데, 이는 $$ef=fe+h$$를 사용해 $$ef+fe=2fe+h$$로 정렬한 것이다. 이 Casimir element는 $$\sl_2$$의 유한차원 표현 분류 ([§근계, ⁋정의 8](/ko/math/lie_theory/root_systems#def8))에서 각 기약 표현 위에 스칼라로 작용하여, 표현을 구별하는 불변량의 역할을 한다.

---

**참고문헌**

**[Bou]** N. Bourbaki, *Lie groups and Lie algebras, Chapters 1–3*, Springer, 1989.  
**[Dix]** J. Dixmier, *Enveloping algebras*, Graduate Studies in Mathematics, American Mathematical Society, 1996.  
**[Hum]** J. E. Humphreys, *Introduction to Lie algebras and representation theory*, Graduate Texts in Mathematics, Springer, 1972.  

---
