---
title: "Kähler 다양체"
description: "복소다양체 위에서 J와 양립하는 Hermitian 계량과 그 동반 기본형식 ω를 정의하고, ω가 닫힘(dω=0)이라는 Kähler 조건을 도입한다. Kähler 조건이 Levi-Civita 접속에 대한 J의 평행성, 국소 표준 osculation, 국소 Kähler 퍼텐셜과 동치임을 보이고, ℂ^n·복소토러스·Fubini–Study 계량을 갖춘 ℂP^n이 Kähler임을 확인한다. Kähler 다양체가 사교다양체이며 콤팩트 Kähler의 짝수 코호몰로지가 비자명함을 유도하고, Kähler 항등식을 서술한다."
excerpt: "Hermitian 계량, J-불변 리만계량, 기본형식, Kähler 조건, dω=0, ∇J=0, Kähler 퍼텐셜, Fubini–Study 계량, CP^n, 복소토러스, 사영다양체, Kähler⟹symplectic, b_2≥1, Kähler 항등식"

categories: [Math / Complex Geometry]
permalink: /ko/math/complex_geometry/kahler_manifolds
sidebar:
    nav: "complex_geometry-ko"

date: 2026-06-22
weight: 4

published: false
---

복소다양체는 접공간 수준에서 곱셈 $$i$$를 흉내내는 거의 복소구조 $$J$$를 표준적으로 갖추며, 그 적분가능성이 정칙기하 전체를 떠받쳤다 ([§거의 복소구조, ⁋명제 3](/ko/math/complex_geometry/almost_complex_structures#prop3)). 한편 매끄러운 다양체 위에 길이와 각을 재는 리만 계량을 얹으면 미분기하의 풍부한 도구가 따라온다 ([\[리만기하학\] §리만 계량, ⁋정의 1](/ko/math/riemannian_geometry/Riemannian_metric#def1)). 복소다양체 위에서 이 두 구조, 곧 복소구조 $$J$$와 리만 계량 $$g$$를 양립시키면 어떤 일이 일어나는가가 이 글의 출발점이다.

양립의 가장 자연스러운 요구는 $$J$$가 $$g$$에 대한 등거리변환이 되는 것, 곧 $$g(JX, JY) = g(X, Y)$$이다. 이러한 계량을 Hermitian 계량이라 하며, 여기서 동반 $$2$$-형식 $$\omega(X, Y) = g(JX, Y)$$가 자연히 따라온다. 이 $$\omega$$가 닫힌형식일 때, 곧 $$d\omega = 0$$일 때 우리는 그 다양체를 Kähler 다양체라 부른다. 이 한 줄의 닫힘조건이 복소기하·리만기하·사교기하 세 구조를 동시에 묶어내며, 그로부터 흘러나오는 강성이 콤팩트 복소다양체론의 중심을 이룬다. 이 글의 목표는 Hermitian 계량과 기본형식을 세우고, Kähler 조건의 여러 동치 특성화를 증명하며, $$\mathbb{C}^n$$과 $$\mathbb{CP}^n$$을 비롯한 표준 예시에서 Kähler 구조를 확인하고, Kähler 다양체가 사교다양체임과 콤팩트 Kähler 다양체의 위상적 귀결을 끌어내는 것이다.

## Hermitian 계량과 기본형식

복소다양체 $$X$$ 위의 리만 계량 가운데 복소구조와 어울리는 것을 골라낸다. 양립의 기준은 $$J$$가 각 접공간에서 등거리변환이 되는 것이다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 복소다양체 $$(X, J)$$ 위의 리만 계량 $$g$$가 *Hermitian metric<sub>Hermitian 계량</sub>*이라는 것은, 모든 점에서 모든 접벡터 $$X, Y$$에 대하여

$$
g(JX, JY) = g(X, Y)
$$

가 성립하는 것이다. 곧 $$J$$가 각 접공간에서 $$g$$-등거리변환인 것이다. 이러한 $$g$$를 갖춘 $$(X, J, g)$$를 *Hermitian manifold<sub>Hermitian 다양체</sub>*라 한다.

</div>

조건 $$g(JX, JY) = g(X, Y)$$를 *$$J$$-invariance<sub>$J$-불변성</sub>* 라 부른다. 임의의 리만 계량 $$g_0$$가 주어지면 $$g(X, Y) = \frac{1}{2}\big( g_0(X, Y) + g_0(JX, JY) \big)$$로 평균을 취해 언제나 Hermitian 계량을 만들 수 있으므로, 모든 복소다양체는 Hermitian 계량을 가진다. Hermitian 조건은 $$g$$에 대한 제약일 뿐 추가 적분가능성을 요구하지 않으며, 그 자체로는 Kähler 조건보다 약하다.

$$J$$-불변 계량에는 반대칭 $$2$$-형식이 한 쌍으로 따라붙는다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Hermitian 다양체 $$(X, J, g)$$의 *fundamental form<sub>기본형식</sub>* $$\omega$$를 두 접벡터 $$X, Y$$에 대하여

$$
\omega(X, Y) = g(JX, Y)
$$

로 정의한다. 또 복소값 쌍선형형식 $$h = g - i\omega$$를 $$(X, J, g)$$의 *Hermitian form<sub>Hermitian 형식</sub>*이라 한다.

</div>

기본형식이 반대칭임은 $$J$$-불변성에서 나온다. $$\omega(Y, X) = g(JY, X) = g(J(JY), JX) = g(-Y, JX) = -g(JX, Y) = -\omega(X, Y)$$이므로 $$\omega$$는 반대칭 $$2$$-형식, 곧 미분 $$2$$-형식이다. 더 나아가 $$\omega$$는 $$J$$-불변이다. $$\omega(JX, JY) = g(J^2 X, JY) = g(-X, JY) = -g(JY, X) = -\omega(Y,X) = \omega(X,Y)$$이기 때문이다. $$J$$-불변 $$2$$-형식은 $$(1,1)$$-형식이 되며 ([§거의 복소구조, ⁋정의 6](/ko/math/complex_geometry/almost_complex_structures#def6)의 차수분해에서 $$J$$-불변성이 $$(2,0)$$·$$(0,2)$$-성분의 소멸을 강제한다), 따라서 $$\omega$$는 실 $$(1,1)$$-형식이다. 한편 $$h = g - i\omega$$는 $$T^{1,0}X$$ 위에서 Hermitian 내적의 역할을 한다. 곧 $$h(X, Y) = g(X,Y) - i\, g(JX, Y)$$로서 첫 변수에 $$\mathbb{C}$$-선형, 둘째에 반선형인 양의 Hermitian 형식이 되며, 이 점이 "Hermitian"이라는 이름의 근거이다.

기본형식을 국소좌표로 적으면 계량의 성분이 직접 드러난다. 정칙좌표 $$z_1, \ldots, z_n$$에서 Hermitian 계량의 $$T^{1,0}X$$-성분을

$$
g_{j\bar{k}} = h\!\left( \frac{\partial}{\partial z_j}, \frac{\partial}{\partial z_k} \right) = 2\, g\!\left( \frac{\partial}{\partial z_j}, \frac{\partial}{\partial \bar{z}_k} \right)
$$

로 두면 (여기서 $$g$$는 복소화 접공간 위로 $$\mathbb{C}$$-쌍선형 확장한 것이다), 기본형식은

$$
\omega = \frac{i}{2} \sum_{j, k} g_{j\bar{k}}\, dz_j \wedge d\bar{z}_k
$$

로 표현된다. 행렬 $$(g_{j\bar{k}})$$는 각 점에서 양의 정부호 Hermitian 행렬이며, $$\omega$$가 실형식이라는 것은 $$\overline{g_{j\bar{k}}} = g_{k\bar{j}}$$와 동치이다. 이 좌표 표현이 다음 절의 Kähler 조건을 계량 성분의 미분에 대한 대칭조건으로 옮기는 발판이 된다.

## Kähler 조건

Hermitian 조건만으로는 복소구조와 계량이 일차적으로만 맞물린다. 둘이 이차까지, 곧 미분 수준에서 완전히 양립하려면 기본형식이 닫혀야 한다. 이것이 Kähler 조건이다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Hermitian 다양체 $$(X, J, g)$$가 *Kähler manifold<sub>Kähler 다양체</sub>*라는 것은 그 기본형식 $$\omega$$가 닫힌형식인 것, 곧

$$
d\omega = 0
$$

인 것이다. 이때 $$g$$를 *Kähler metric<sub>Kähler 계량</sub>*, $$\omega$$를 *Kähler form<sub>Kähler 형식</sub>*이라 한다.

</div>

조건 $$d\omega = 0$$은 $$\omega$$가 de Rham 코호몰로지류 $$[\omega] \in H^2(X, \mathbb{R})$$를 정의하게 하며, 이 류를 $$X$$의 *Kähler class<sub>Kähler 류</sub>*라 한다. 모든 복소다양체가 Hermitian 계량을 갖는 것과 달리, Kähler 계량의 존재는 진정한 제약이다. 아래에서 보듯 콤팩트 Kähler 다양체는 짝수 차수의 코호몰로지가 모두 비자명해야 하므로, 이 조건을 어기는 콤팩트 복소다양체는 Kähler 계량을 전혀 가질 수 없다.

좌표에서 Kähler 조건은 계량 성분의 미분에 대한 깔끔한 대칭으로 번역된다. 기본형식 $$\omega = \frac{i}{2}\sum g_{j\bar{k}}\, dz_j \wedge d\bar{z}_k$$에 외미분을 적용하면 $$d = \partial + \bar\partial$$ ([§Dolbeault 코호몰로지, ⁋명제 2](/ko/math/complex_geometry/dolbeault_cohomology#prop2))에 의해 $$d\omega$$는 $$(2,1)$$-성분 $$\partial\omega$$와 $$(1,2)$$-성분 $$\bar\partial\omega$$로 갈라진다. $$\omega$$가 실형식이므로 $$\partial\omega = 0$$과 $$\bar\partial\omega = 0$$은 켤레로 동치이고, 따라서 $$d\omega = 0$$은 $$\partial\omega = 0$$ 하나와 동치이다. 이를 좌표로 풀면 다음 명제가 된다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> Hermitian 다양체 $$(X, J, g)$$에 대하여, 기본형식을 $$\omega = \frac{i}{2}\sum_{j,k} g_{j\bar{k}}\, dz_j \wedge d\bar{z}_k$$로 쓸 때 다음이 동치이다.

1. $$\omega$$는 Kähler 형식이다. 곧 $$d\omega = 0$$.
2. 모든 $$j, k, l$$에 대하여 $$\dfrac{\partial g_{j\bar{k}}}{\partial z_l} = \dfrac{\partial g_{l\bar{k}}}{\partial z_j}$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$dz_j, d\bar{z}_k$$가 닫혀 있으므로 $$\partial\omega$$는 계수의 $$\partial$$-미분에서만 나온다.

$$
\partial\omega = \frac{i}{2} \sum_{j,k,l} \frac{\partial g_{j\bar{k}}}{\partial z_l}\, dz_l \wedge dz_j \wedge d\bar{z}_k.
$$

이 $$(2,1)$$-형식이 $$0$$이라는 것은, 각 고정된 $$k$$에 대하여 $$dz_l \wedge dz_j$$의 계수가 모두 $$0$$이라는 것이다. $$dz_l \wedge dz_j = -dz_j \wedge dz_l$$이므로, $$l, j$$에 대한 반대칭화에서 살아남는 부분이 소멸할 조건은

$$
\frac{\partial g_{j\bar{k}}}{\partial z_l} - \frac{\partial g_{l\bar{k}}}{\partial z_j} = 0
$$

이 모든 $$j, k, l$$에 대해 성립하는 것이다. 곧 (2)이다. 한편 위에서 보았듯 $$\omega$$가 실형식이므로 $$\bar\partial\omega = \overline{\partial\omega}$$이고, 따라서 $$\partial\omega = 0$$이면 $$\bar\partial\omega = 0$$이 따라와 $$d\omega = \partial\omega + \bar\partial\omega = 0$$이 된다. 역으로 $$d\omega = 0$$이면 차수분해의 직합성으로 $$\partial\omega = 0$$이다. 따라서 (1) ⟺ (2)이다.

</details>

조건 (2)는 $$g_{j\bar{k}}$$가 단일한 실 함수의 이차 혼합 미분으로 표현될 수 있게 한다는 점에서 결정적이다. $$\partial g_{j\bar{k}}/\partial z_l$$이 $$j$$와 $$l$$에 대칭이면, $$g_{j\bar{k}}$$가 $$z_j$$에 대한 어떤 함수의 미분처럼 행동하여 국소적으로 $$g_{j\bar{k}} = 2\,\partial^2\varphi / \partial z_j \partial \bar{z}_k$$ 꼴의 잠재함수 $$\varphi$$가 존재하게 된다. 이 국소 퍼텐셜의 정확한 형태가 Kähler 조건의 또 다른 동치 특성화이며, 다음 절에서 정식화한다.

## 동치 특성화

Kähler 조건은 표면상 기본형식의 닫힘이라는 사교적 조건이지만, 그 내용은 복소구조와 리만 계량이 일차 미분 수준에서 완전히 양립한다는 데 있다. 이를 여러 관점에서 본 동치조건들로 묶는다.

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5 (Kähler 동치조건)**</ins> Hermitian 다양체 $$(X, J, g)$$에 대하여 다음 네 조건이 서로 동치이다. 여기서 $$\nabla$$는 $$g$$의 Levi-Civita 접속이다 ([\[리만기하학\] §레비-치비타 접속, ⁋정리 4](/ko/math/riemannian_geometry/Levi-Civita_connection#thm4)).

1. $$\omega$$가 닫힘이다. 곧 $$d\omega = 0$$ (Kähler 조건).
2. $$J$$가 $$\nabla$$에 대해 평행하다. 곧 $$\nabla J = 0$$.
3. 각 점 $$p$$에서 정칙좌표를 적절히 골라 $$g_{j\bar{k}}(p) = \delta_{jk}$$이고 모든 일차 미분 $$\partial g_{j\bar{k}}/\partial z_l$$과 $$\partial g_{j\bar{k}}/\partial \bar{z}_l$$이 $$p$$에서 소멸한다. 곧 계량이 $$p$$에서 표준 Hermitian 계량과 이차까지 일치한다.
4. 국소적으로 실값 함수 $$\varphi$$가 존재하여 $$\omega = i\, \partial\bar\partial\varphi$$이다. 곧 $$g_{j\bar{k}} = 2\,\dfrac{\partial^2\varphi}{\partial z_j \partial\bar{z}_k}$$.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

(1) ⟺ (4)를 먼저 보인다. (4) ⟹ (1)은 $$\bar\partial\partial = -\partial\bar\partial$$ ([§Dolbeault 코호몰로지, ⁋명제 3](/ko/math/complex_geometry/dolbeault_cohomology#prop3))와 $$\partial^2 = \bar\partial^2 = 0$$에서 따라온다. $$\omega = i\partial\bar\partial\varphi$$이면

$$
d\omega = (\partial + \bar\partial)(i\partial\bar\partial\varphi) = i\partial^2\bar\partial\varphi + i\bar\partial\partial\bar\partial\varphi = 0 + i\bar\partial\partial\bar\partial\varphi
$$

이고, $$\bar\partial\partial = -\partial\bar\partial$$와 $$\bar\partial^2 = 0$$으로 $$\bar\partial\partial\bar\partial\varphi = -\partial\bar\partial\bar\partial\varphi = 0$$이므로 $$d\omega = 0$$이다. 또 $$i\partial\bar\partial\varphi = i\sum_{j,k}(\partial^2\varphi/\partial z_j\partial\bar{z}_k)\, dz_j \wedge d\bar{z}_k$$이므로, 계수를 $$\frac{i}{2}g_{j\bar{k}}$$와 맞추면 $$\frac{i}{2}g_{j\bar{k}} = i\,\partial^2\varphi/\partial z_j\partial\bar{z}_k$$, 곧 $$g_{j\bar{k}} = 2\,\partial^2\varphi/\partial z_j\partial\bar{z}_k$$이다.

역으로 (1) ⟹ (4)는 [명제 4](#prop4)의 조건 (2)에서 나온다. $$d\omega = 0$$이면 $$\partial g_{j\bar{k}}/\partial z_l$$이 $$j, l$$에 대칭이고, 켤레를 취하면 $$\partial g_{j\bar{k}}/\partial\bar{z}_l$$이 $$k, l$$에 대칭이다. 이 대칭성 아래에서, $$(0,1)$$-형식 $$\eta = \frac{i}{2}\sum_{j,k} g_{j\bar{k}}\, z_j$$ 꼴의 풀이를 폴리디스크에서 $$\bar\partial$$-Poincaré 보조정리 ([§Dolbeault 코호몰로지, ⁋보조정리 6](/ko/math/complex_geometry/dolbeault_cohomology#lem6))로 구성하여 $$\omega = d\beta$$인 실 $$1$$-형식 $$\beta$$를 얻고, $$\beta$$의 $$(1,0)$$·$$(0,1)$$-성분을 다시 $$\bar\partial$$·$$\partial$$-Poincaré로 풀면 실값 함수 $$\varphi$$로서 $$\omega = i\partial\bar\partial\varphi$$가 국소적으로 성립한다. 구체적으로, $$d\omega = 0$$인 실 $$(1,1)$$-형식은 국소적으로 $$\omega = d\beta = (\partial + \bar\partial)(\beta^{1,0} + \beta^{0,1})$$로 쓰이고, 차수별로 $$\partial\beta^{1,0} = 0$$, $$\bar\partial\beta^{0,1} = 0$$, $$\omega = \partial\beta^{0,1} + \bar\partial\beta^{1,0}$$이 된다. $$\partial$$-Poincaré로 $$\beta^{1,0} = \partial f$$, $$\bar\partial$$-Poincaré로 $$\beta^{0,1} = \bar\partial h$$ ($$h = \bar{f}$$로 택할 수 있다)를 얻으면 $$\omega = \partial\bar\partial h + \bar\partial\partial f = \bar\partial\partial(f - h)$$이고, $$\varphi = i(f - h)$$를 실값이 되도록 조정하면 $$\omega = i\partial\bar\partial\varphi$$이다.

(1) ⟺ (3)을 본다. (3) ⟹ (1)은 즉각적이다. 점 $$p$$에서 계량의 일차 미분이 모두 소멸하면, [명제 4](#prop4)의 조건 (2) $$\partial g_{j\bar{k}}/\partial z_l = \partial g_{l\bar{k}}/\partial z_j$$가 $$p$$에서 양변 $$0$$으로 성립하므로 $$d\omega$$가 $$p$$에서 소멸한다. $$p$$가 임의였으므로 $$d\omega = 0$$이다. (1) ⟹ (3)은 (4)를 거친다. (4)에 의해 국소 퍼텐셜 $$\varphi$$가 존재하므로, $$p$$를 원점으로 하는 정칙좌표에서 $$\varphi$$의 Taylor 전개를 정칙 좌표변환으로 정규화한다. $$\varphi = \varphi(p) + 2\Real\big(\text{정칙항}\big) + \sum_{j,k} g_{j\bar{k}}(p)\, z_j\bar{z}_k + (\text{삼차 이상})$$에서, 정칙항은 $$\partial\bar\partial$$로 죽으므로 무시할 수 있고, 이차항의 Hermitian 부분을 표준형으로 보내는 $$\mathbb{C}$$-선형 좌표변환으로 $$g_{j\bar{k}}(p) = \delta_{jk}$$를 만든다. 남은 삼차 이상 항 가운데 $$z_j z_k \bar{z}_l$$ 꼴의 혼합 삼차항을 정칙 이차 좌표변환 $$z_j \mapsto z_j + (\text{이차 정칙})$$으로 흡수하면 $$g_{j\bar{k}}$$의 일차 미분이 $$p$$에서 모두 소멸한다. 이 정규화가 가능한 것이 바로 Kähler 조건이며, 이렇게 얻은 좌표를 *normal coordinate*라 한다.

(2) ⟺ (1)을 본다. Levi-Civita 접속은 계량과 호환되고 비틀림이 없다. $$g$$가 Hermitian이므로 $$\omega(X, Y) = g(JX, Y)$$이고, $$\nabla g = 0$$이므로 $$\nabla\omega$$와 $$\nabla J$$는 $$\nabla\omega(X; Y, Z) = g((\nabla_X J)Y, Z)$$로 직접 이어진다. 따라서 $$\nabla J = 0$$은 $$\nabla\omega = 0$$과 동치이고, $$\nabla\omega = 0$$이면 특히 $$\omega$$의 반대칭화인 $$d\omega$$가 소멸한다 ($$d\omega(X,Y,Z) = \sum_{\text{cyc}} (\nabla_X\omega)(Y,Z)$$, 비틀림이 없으므로). 곧 (2) ⟹ (1)이다. 역의 함의 (1) ⟹ (2)가 Kähler 기하의 핵심이며, 다음과 같이 본다. $$\nabla\omega$$는 $$g$$, $$J$$, $$d\omega$$, 그리고 $$N_J$$ (Nijenhuis 텐서)로 대수적으로 표현되는데, $$X$$가 복소다양체라 $$N_J = 0$$ ([§거의 복소구조, ⁋정리 12](/ko/math/complex_geometry/almost_complex_structures#thm12))이고 가정에서 $$d\omega = 0$$이므로 $$\nabla\omega = 0$$이 따라온다. 정밀하게는, 비틀림 없는 Levi-Civita 접속에 대하여 $$2\, g\big((\nabla_X J)Y, Z\big)$$가 기본형식의 외미분값 $$d\omega(X, Y, Z)$$·$$d\omega(X, JY, JZ)$$와 Nijenhuis 항 $$g\big(N_J(Y, Z), JX\big)$$의 일차결합으로 표현된다 (각 항의 계수는 $$\omega$$와 $$N_J$$의 부호 규약에 따라 정해진다). $$X$$가 복소다양체라 $$N_J = 0$$이고 가정에서 $$d\omega = 0$$이므로 이 결합의 모든 항이 소멸하여 $$(\nabla_X J)Y = 0$$, 곧 $$\nabla J = 0$$을 얻는다.

</details>

이 네 동치조건은 Kähler 다양체를 보는 네 가지 시점을 준다. 조건 (1)은 사교적, (2)는 리만적, (3)은 국소 해석적, (4)는 복소 해석적 시점이다. 특히 (3)은 Kähler 다양체가 각 점에서 평탄한 $$\mathbb{C}^n$$과 이차까지 구별되지 않음을 뜻하며, 이 "이차 osculation"이 Kähler 항등식과 같은 강력한 국소 공식들이 성립하는 근거이다. 조건 (2)는 holonomy 군이 $$U(n)$$ 안에 들어감을 뜻하여, Kähler 다양체를 holonomy 관점에서 특징짓는다. 조건 (4)의 국소 퍼텐셜 $$\varphi$$를 *Kähler potential<sub>Kähler 퍼텐셜</sub>* 이라 부르며, 다음 절의 Fubini–Study 계량 구성에서 핵심 도구가 된다.

## 예시

가장 단순한 Kähler 다양체는 평탄한 $$\mathbb{C}^n$$이다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6 ($$\mathbb{C}^n$$의 표준 Kähler 구조)**</ins> $$\mathbb{C}^n$$에 표준 좌표 $$z_1, \ldots, z_n$$과 표준 Hermitian 계량 $$g_{j\bar{k}} = \delta_{jk}$$를 주면, 기본형식은

$$
\omega_0 = \frac{i}{2} \sum_{j=1}^n dz_j \wedge d\bar{z}_j = \sum_{j=1}^n dx_j \wedge dy_j
$$

이다 ($$z_j = x_j + iy_j$$). 계수가 상수이므로 $$d\omega_0 = 0$$이고, 따라서 $$\mathbb{C}^n$$은 Kähler 다양체이다. Kähler 퍼텐셜은 $$\varphi = \frac{1}{2}\lvert z \rvert^2 = \frac{1}{2}\sum_j z_j\bar{z}_j$$로, $$\partial^2\varphi/\partial z_j\partial\bar{z}_k = \frac{1}{2}\delta_{jk}$$를 주어 $$\omega_0 = i\partial\bar\partial\varphi$$를 확인한다. 또 $$\omega_0$$는 정확히 $$\mathbb{R}^{2n}$$의 표준 사교형식이다 ([\[사교기하학\] §사교다양체, ⁋정의 1](/ko/math/symplectic_geometry/symplectic_manifold#def1)).

</div>

다음으로 격자 몫에서 평탄한 콤팩트 예시가 나온다.

<div class="example" markdown="1">

<ins id="ex7">**예시 7 (복소토러스)**</ins> 격자 $$\Lambda \subseteq \mathbb{C}^n$$에 의한 복소토러스 $$T = \mathbb{C}^n/\Lambda$$ ([§복소다양체, ⁋예시 7](/ko/math/complex_geometry/complex_manifolds#ex7))는 Kähler 다양체이다. $$\mathbb{C}^n$$의 표준 Kähler 형식 $$\omega_0 = \frac{i}{2}\sum dz_j \wedge d\bar{z}_j$$가 평행이동 $$z \mapsto z + \lambda$$에 대해 불변이므로 (계수가 상수이고 $$dz_j$$가 평행이동 불변), $$\omega_0$$는 몫 $$T$$ 위의 잘 정의된 $$2$$-형식으로 내려가고, 상수계수라 여전히 닫힌형식이다. 따라서 모든 복소토러스는 평탄한 Kähler 계량을 가진다. 차원 $$1$$에서는 이것이 타원곡선의 평탄 계량이고, 높은 차원에서는 복소토러스가 사영적이지 않을 수 있음에도 ([§복소다양체, ⁋예시 7](/ko/math/complex_geometry/complex_manifolds#ex7)) Kähler 계량은 언제나 존재한다. 곧 Kähler는 사영성보다 약한 조건이다.

</div>

가장 중요한 콤팩트 예시는 Fubini–Study 계량을 갖춘 복소사영공간이다.

<div class="example" markdown="1">

<ins id="ex8">**예시 8 ($$\mathbb{CP}^n$$의 Fubini–Study 계량)**</ins> 복소사영공간 $$\mathbb{CP}^n$$ ([§복소다양체, ⁋예시 6](/ko/math/complex_geometry/complex_manifolds#ex6))에 다음과 같이 Kähler 형식을 준다. 표준 열린집합 $$U_i = \{z_i \neq 0\}$$ 위에서 국소 함수

$$
\varphi_i = \log \lVert z \rVert^2 = \log\left( \sum_{j=0}^n \lvert z_j \rvert^2 \right)
$$

를 두고 (여기서 $$z = (z_0, \ldots, z_n)$$는 임의의 동차좌표 대표원이며, $$U_i$$ 위에서는 비동차좌표 $$w_j = z_j/z_i$$로 $$\varphi_i = \log(1 + \sum_{j \neq i}\lvert w_j\rvert^2)$$로 적힌다),

$$
\omega_{\mathrm{FS}} = \frac{i}{2\pi}\, \partial\bar\partial \log \lVert z \rVert^2
$$

로 정의되는 $$2$$-형식을 *Fubini–Study form<sub>Fubini–Study 형식</sub>*이라 한다. 이는 $$\mathbb{CP}^n$$ 전체에서 잘 정의된 Kähler 형식이며, 그 계량 $$g_{\mathrm{FS}}$$를 *Fubini–Study metric<sub>Fubini–Study 계량</sub>*이라 한다.

</div>

이 정의의 정당성을 차례로 확인한다. 먼저 $$\omega_{\mathrm{FS}}$$가 좌표 무관하게 잘 정의됨을 본다. 다른 대표원 $$z' = \lambda z$$ ($$\lambda$$는 영점 없는 정칙함수) 를 택하면 $$\log\lVert z'\rVert^2 = \log\lVert z\rVert^2 + \log\lambda + \log\bar\lambda$$이고, $$\log\lambda$$는 정칙이라 $$\bar\partial\log\lambda = 0$$이므로 $$\partial\bar\partial\log\lambda = 0$$, 마찬가지로 $$\log\bar\lambda$$는 반정칙이라 $$\partial\log\bar\lambda = 0$$이다. 따라서 $$\partial\bar\partial\log\lVert z'\rVert^2 = \partial\bar\partial\log\lVert z\rVert^2$$로, 서로 다른 차트의 퍼텐셜이 정칙·반정칙 함수만큼 차이가 나 $$\partial\bar\partial$$ 아래에서 같은 형식을 준다. 다음으로 $$d\omega_{\mathrm{FS}} = 0$$은 [정리 5](#thm5)의 조건 (4)에서 즉시 따라온다. $$\omega_{\mathrm{FS}}$$가 국소적으로 $$\frac{1}{2\pi}i\partial\bar\partial\varphi_i$$ 꼴이므로 Kähler 형식이다. 양의 정부호성, 곧 대응 계량 $$g_{\mathrm{FS}}$$가 리만 계량이 됨은 $$U_i$$의 비동차좌표에서

$$
g_{j\bar{k}} = \frac{1}{\pi}\frac{\partial^2}{\partial w_j \partial\bar{w}_k}\log\Big(1 + \textstyle\sum_l \lvert w_l\rvert^2\Big) = \frac{1}{\pi}\,\frac{(1 + \lvert w\rvert^2)\delta_{jk} - \bar{w}_j w_k}{(1 + \lvert w\rvert^2)^2}
$$

가 각 점에서 양의 정부호 Hermitian 행렬임을 직접 계산해 확인된다 (Cauchy–Schwarz 부등식이 정부호성을 준다). 마지막으로 $$\omega_{\mathrm{FS}}$$는 사영변환 $$\mathrm{PU}(n+1)$$의 작용에 불변이다. $$U(n+1)$$의 작용이 $$\lVert z\rVert^2$$를 보존하므로 퍼텐셜 $$\log\lVert z\rVert^2$$가 불변이고, 따라서 $$\omega_{\mathrm{FS}}$$가 불변이다. 이 균질성 덕분에 $$\mathbb{CP}^n$$은 한 점에서의 값으로 전부 결정되는 등질 Kähler 다양체가 된다.

Fubini–Study 계량의 정규화 상수 $$1/2\pi$$는 Kähler 류가 정수 코호몰로지류가 되도록 맞춘 것이다. $$\mathbb{CP}^1$$의 경우 $$\int_{\mathbb{CP}^1}\omega_{\mathrm{FS}} = 1$$이 되어 $$[\omega_{\mathrm{FS}}]$$가 $$H^2(\mathbb{CP}^n, \mathbb{Z})$$의 생성원이 된다. 이 정수성이 Fubini–Study 계량을 사영매장과 잇는 다리이다.

복소사영공간이 Kähler라는 사실은 곧바로 그 부분다양체로 전파된다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> Kähler 다양체 $$(X, J, g)$$의 복소 부분다양체 $$Y \subseteq X$$는 유도 계량에 대해 다시 Kähler 다양체이다. 특히 매끄러운 사영다양체 ([\[대수다양체\] §사영다양체, ⁋정의 1](/ko/math/algebraic_varieties/projective_varieties#def1))는 모두 Kähler 다양체이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\iota : Y \hookrightarrow X$$를 포함사상이라 하자. $$Y$$가 복소 부분다양체이므로 그 복소구조 $$J_Y$$는 $$J$$의 제한이고, $$Y$$ 위의 유도 계량 $$g_Y = \iota^\ast g$$는 $$g$$가 $$J$$-불변이므로 $$J_Y$$-불변이다. 곧 $$g_Y$$는 $$Y$$ 위의 Hermitian 계량이다. $$Y$$의 기본형식 $$\omega_Y$$는 $$\omega_Y(U, V) = g_Y(J_Y U, V) = g(JU, V) = \omega(U, V)$$ ($$U, V \in TY$$)이므로, $$\omega_Y = \iota^\ast\omega$$, 곧 $$X$$의 Kähler 형식의 당김이다. 외미분은 당김과 교환하므로

$$
d\omega_Y = d(\iota^\ast\omega) = \iota^\ast(d\omega) = \iota^\ast 0 = 0
$$

이다. 따라서 $$\omega_Y$$는 닫힌형식이고 $$Y$$는 Kähler 다양체이다.

특히 매끄러운 사영다양체 $$Y \subseteq \mathbb{CP}^n$$은 Fubini–Study 계량을 갖춘 Kähler 다양체 $$\mathbb{CP}^n$$ ([예시 8](#ex8))의 복소 부분다양체이므로, 위 논법에 의해 유도된 Fubini–Study 계량에 대해 Kähler 다양체이다.

</details>

이 명제는 Kähler 다양체의 세계가 얼마나 넓은지를 보여준다. 사영대수기하의 모든 매끄러운 대상, 곧 곡선·곡면·고차원 사영다양체가 자동으로 Kähler 구조를 가지므로, Kähler 기하는 복소대수기하 전체를 포괄하는 해석적 틀이 된다. 동시에 복소토러스의 비사영적 예시 ([예시 7](#ex7))가 보여주듯 Kähler는 사영보다 진정으로 넓어, 대수기하 바깥의 콤팩트 복소다양체까지 담는다.

## 사교구조와 위상적 귀결

Kähler 형식 $$\omega$$는 닫힌 $$2$$-형식이면서 동시에 각 점에서 비퇴화이다. 이 두 성질이 Kähler 다양체를 사교다양체로 만든다.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> Kähler 다양체 $$(X, J, g)$$의 Kähler 형식 $$\omega$$는 사교형식이다. 곧 $$(X, \omega)$$는 사교다양체이다. 더 나아가 $$\omega^n / n!$$은 $$X$$의 리만 부피형식과 일치하며, 따라서 $$\omega^n$$은 어디서도 소멸하지 않는다 ($$n = \dim_{\mathbb{C}} X$$).

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

사교형식이려면 $$\omega$$가 닫혀 있고 각 점에서 비퇴화여야 한다 ([\[사교기하학\] §사교다양체, ⁋정의 1](/ko/math/symplectic_geometry/symplectic_manifold#def1)). 닫힘은 Kähler 조건 그 자체이다. 비퇴화는 점별 계산이다. 점 $$p$$에서 정규좌표 ([정리 5](#thm5)의 (3))를 택하면 $$\omega_p = \frac{i}{2}\sum_j dz_j \wedge d\bar{z}_j = \sum_j dx_j \wedge dy_j$$로 표준 사교형식과 일치하고, 이는 비퇴화이다. 정규좌표를 쓰지 않더라도, $$\omega_p(X, Y) = g_p(JX, Y)$$에서 $$g_p$$가 양의 정부호이고 $$J$$가 가역이므로, $$\omega_p(X, \cdot) = 0$$이면 $$g_p(JX, \cdot) = 0$$, 곧 $$JX = 0$$, 곧 $$X = 0$$이다. 따라서 $$\omega_p$$는 비퇴화이다.

부피형식과의 일치를 본다. 점 $$p$$의 정규좌표 $$z_j = x_j + iy_j$$에서 $$\omega_p = \sum_j dx_j \wedge dy_j$$이므로

$$
\frac{\omega_p^n}{n!} = \frac{1}{n!}\Big(\sum_j dx_j \wedge dy_j\Big)^n = dx_1 \wedge dy_1 \wedge \cdots \wedge dx_n \wedge dy_n
$$

이다 (서로 다른 $$j$$의 $$dx_j \wedge dy_j$$들이 교환하고 같은 인자의 제곱이 소멸하므로, $$n$$제곱의 전개에서 모든 인자를 한 번씩 쓴 항만 $$n!$$개 살아남는다). 한편 $$g_p$$가 정규좌표에서 표준 유클리드 계량 $$\sum_j(dx_j^2 + dy_j^2)$$과 일치하므로 그 리만 부피형식도 $$dx_1 \wedge dy_1 \wedge \cdots \wedge dx_n \wedge dy_n$$이다. 둘이 같으므로 $$\omega^n/n!$$은 부피형식이고, 부피형식은 어디서도 소멸하지 않으므로 $$\omega^n$$도 그러하다.

</details>

이로써 Kähler 다양체는 복소·리만·사교의 세 구조를 한 몸에 갖춘 대상이 된다. 다만 역방향, 곧 사교다양체가 언제나 Kähler 다양체인 것은 아니다. 사교 조건은 비퇴화 닫힌 $$2$$-형식만 요구하며 양립하는 복소구조나 그 적분가능성을 보장하지 않으므로, Kähler가 아닌 콤팩트 사교다양체 (예컨대 Kodaira–Thurston 다양체) 가 존재한다. 곧 "Kähler ⟹ symplectic"은 성립하지만 그 역은 거짓이다.

콤팩트성을 더하면 $$\omega^n$$의 비소멸이 코호몰로지에 위상적 흔적을 남긴다.

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> $$X$$가 콤팩트 연결 Kähler 다양체이고 $$n = \dim_{\mathbb{C}} X$$이면, 모든 $$1 \leq k \leq n$$에 대하여 코호몰로지류 $$[\omega^k] \in H^{2k}(X, \mathbb{R})$$는 $$0$$이 아니다. 특히 Betti 수에 대해 $$b_{2k}(X) \geq 1$$이고, 따라서 $$b_2(X) \geq 1$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\omega$$가 닫혀 있으므로 $$\omega^k$$도 닫혀 있고 ($$d(\omega^k) = k\, d\omega \wedge \omega^{k-1} = 0$$) 코호몰로지류 $$[\omega^k] \in H^{2k}(X, \mathbb{R})$$를 정의한다. 이 류가 $$0$$이 아님을 보이기 위해, 그 거듭제곱을 끝까지 올린 $$[\omega^n]$$을 적분한다. [명제 10](#prop10)에 의해 $$\omega^n/n!$$은 부피형식이므로 $$\omega^n$$은 양의 부피형식의 양의 상수배이고, $$X$$가 콤팩트이므로

$$
\int_X \omega^n = n! \int_X \frac{\omega^n}{n!} = n! \cdot \mathrm{vol}(X) > 0
$$

이다. 만약 어떤 $$k$$에 대해 $$[\omega^k] = 0$$, 곧 $$\omega^k = d\eta$$인 $$\eta$$가 존재한다면, $$\omega^n = \omega^k \wedge \omega^{n-k} = d\eta \wedge \omega^{n-k} = d(\eta \wedge \omega^{n-k})$$ ($$\omega^{n-k}$$가 닫혀 있으므로) 로 $$\omega^n$$이 완전형식이 된다. 그러면 Stokes 정리에 의해 경계 없는 콤팩트 $$X$$에서 $$\int_X \omega^n = \int_X d(\eta \wedge \omega^{n-k}) = 0$$이 되어 위 부등식 $$\int_X\omega^n > 0$$과 모순이다. 따라서 모든 $$1 \leq k \leq n$$에 대해 $$[\omega^k] \neq 0$$이다.

$$[\omega^k] \neq 0$$이면 $$H^{2k}(X, \mathbb{R}) \neq 0$$이므로 $$b_{2k}(X) = \dim_{\mathbb{R}} H^{2k}(X, \mathbb{R}) \geq 1$$이다. $$k = 1$$로 두면 $$b_2(X) \geq 1$$이다.

</details>

이 명제는 콤팩트 Kähler 다양체에 대한 가장 기본적이고 강력한 위상적 장애를 준다. $$b_2 = 0$$인 콤팩트 복소다양체는 결코 Kähler 계량을 가질 수 없으며, 더 일반적으로 짝수 차수 Betti 수가 모두 양수여야 한다는 제약이 따른다. 예컨대 Hopf 곡면 $$S^1 \times S^3$$는 콤팩트 복소다양체이지만 $$b_2 = 0$$이므로 Kähler 계량을 전혀 갖지 못한다. 짝수 차수뿐 아니라 홀수 차수 Betti 수에 대해서도 콤팩트 Kähler 다양체는 강한 제약을 받으며, 그 정밀한 형태는 계량과 코호몰로지를 잇는 별도의 이론에서 드러난다.

## Kähler 항등식

Kähler 조건 (2) $$\nabla J = 0$$, 곧 복소구조가 계량과 미분 수준까지 양립한다는 사실은, $$\partial$$·$$\bar\partial$$와 그 형식 수반작용소들이 만족하는 일련의 교환관계를 낳는다. 이를 Kähler 항등식이라 하며, 콤팩트 Kähler 다양체의 해석적 이론 전체가 여기서 출발한다. 먼저 관여하는 작용소들을 정리한다. Hermitian 계량은 각 형식 공간 $$\Omega^{p,q}$$에 점별 Hermitian 내적을 주고, 콤팩트 $$X$$ 위에서 이를 적분하여 $$L^2$$-내적 $$\langle\alpha, \beta\rangle = \int_X \alpha \wedge \ast\bar\beta$$를 얻는다. 이 내적에 대한 $$\partial$$·$$\bar\partial$$의 형식 수반작용소를 $$\partial^\ast$$·$$\bar\partial^\ast$$로 적는다. 또 Kähler 형식과의 wedge 곱 $$L : \alpha \mapsto \omega \wedge \alpha$$와 그 수반작용소 $$\Lambda = L^\ast$$ (*contraction*)를 둔다.

<div class="proposition" markdown="1">

<ins id="thm12">**정리 12 (Kähler 항등식)**</ins> $$(X, J, g)$$가 Kähler 다양체이면, $$\Omega^{p,q}(X)$$ 위에서 다음 교환관계가 성립한다.

$$
[\Lambda, \bar\partial] = -i\, \partial^\ast, \qquad [\Lambda, \partial] = i\, \bar\partial^\ast.
$$

여기서 $$[A, B] = AB - BA$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

핵심은 두 항등식이 평탄한 $$\mathbb{C}^n$$의 표준 Kähler 구조에서 성립함을 보이고, 그 다음 일반 Kähler 다양체로 옮기는 것이다.

평탄한 경우, 곧 $$X = \mathbb{C}^n$$에 표준 계량 ([예시 6](#ex6))을 주면 $$L$$, $$\Lambda$$, $$\partial$$, $$\bar\partial$$, $$\partial^\ast$$, $$\bar\partial^\ast$$가 모두 상수계수 작용소이고, $$dz_j \wedge$$·$$d\bar{z}_j\wedge$$와 그 contraction의 대수적 교환관계를 직접 계산하여 $$[\Lambda, \bar\partial] = -i\partial^\ast$$와 $$[\Lambda, \partial] = i\bar\partial^\ast$$를 확인한다. 이는 외대수와 그 내적이 만드는 유한차원 선형대수 항등식이며, 미분이 아니라 계수 함수의 일차 미분과 wedge·contraction의 결합으로 환원된다.

일반 Kähler 다양체에서는 [정리 5](#thm5)의 조건 (3)을 쓴다. 임의의 점 $$p$$에서 정규좌표를 택하면 계량이 $$p$$에서 표준 Hermitian 계량과 이차까지 일치하므로, $$L$$, $$\Lambda$$와 $$\partial$$, $$\bar\partial$$, 그리고 그 수반작용소들이 $$p$$에서 평탄한 경우와 같은 일차 자료를 가진다. 위 항등식은 작용소들의 일차 미분 정보만으로 결정되는 일차 관계식이므로, $$p$$에서 평탄한 모델의 항등식이 그대로 성립한다. $$p$$가 임의였으므로 항등식이 $$X$$ 전체에서 성립한다. 정규좌표가 존재한다는 것, 곧 계량을 한 점에서 이차까지 표준형으로 만들 수 있다는 것이 바로 Kähler 조건이며, 이것이 평탄 모델에서 일반 다양체로 항등식을 전파하는 다리이다.

</details>

이 항등식들은 표면상 작은 교환관계이지만, 그 귀결은 콤팩트 Kähler 다양체의 코호몰로지 구조 전체를 규정한다. $$\partial$$·$$\bar\partial$$·$$d$$에 딸린 Laplace 작용소들이 Kähler 항등식을 통해 서로 상수배로 묶이며, 이로부터 조화형식의 차수분해와 Hodge 수의 대칭이 따라온다. 곧 [§Dolbeault 코호몰로지, ⁋정의 4](/ko/math/complex_geometry/dolbeault_cohomology#def4)의 Dolbeault 코호몰로지가 콤팩트 Kähler 다양체에서 de Rham 코호몰로지를 차수별로 쪼개는 분해를 낳는다. 이 분해와 그것이 콤팩트 Kähler 다양체의 위상에 부과하는 제약은 별도의 이론을 이룬다. 여기서는 Kähler 조건이 그러한 해석적 강성의 출발점인 교환관계를 어떻게 보장하는지를 확인하는 데서 멈춘다.

---

**참고문헌**

**[Huybrechts]** D. Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005.

**[Griffiths–Harris]** P. Griffiths and J. Harris, *Principles of Algebraic Geometry*, Wiley, 1978.

**[Moroianu]** A. Moroianu, *Lectures on Kähler Geometry*, Cambridge University Press, 2007.

**[Wells]** R. O. Wells, *Differential Analysis on Complex Manifolds*, 3rd ed., Springer, 2008.

**[Ballmann]** W. Ballmann, *Lectures on Kähler Manifolds*, European Mathematical Society, 2006.
