---
title: "Theorema Egregium"
description: "곡면의 Gauss 곡률을 shape operator의 행렬식 곧 두 주곡률의 곱으로 정의하고, 이것이 제1·제2 기본형식의 행렬식 비와 같음을 보인다. Gauss 방정식을 평탄한 주변 공간에 적용해 Gauss 곡률이 제1기본형식만으로 결정되는 내재불변량임을 증명하는 Gauss의 Theorema Egregium을 다루고, Brioschi 공식, 구면을 평면으로 등거리 전개할 수 없다는 따름정리와 지도제작 왜곡을 논한다."
excerpt: "Gauss 곡률의 내재성, Gauss 방정식, Brioschi 공식, 등거리 불변량"

categories: [Math / Riemannian Geometry]
permalink: /ko/math/riemannian_geometry/theorema_egregium
sidebar: 
    nav: "riemannian_geometry-ko"

date: 2026-06-21
weight: 8

published: false
---

곡면 $$M \subseteq \mathbb{R}^3$$의 Gauss 곡률은 본래 외재적인 양으로 정의된다. 각 점에서 곡면이 주변 공간 안에서 법선 방향으로 얼마나 휘는지를 재는 shape operator의 행렬식이 곧 Gauss 곡률이며, 이는 곡면이 $$\mathbb{R}^3$$ 안에 어떻게 놓여 있는지에 의존하는 듯 보인다. 그런데 Gauss가 1827년에 발견한 *놀라운 정리<sub>Theorema Egregium</sub>*는 이 양이 실제로는 곡면 위의 거리, 즉 제1기본형식만으로 결정되는 *내재적* 불변량이라고 말한다. 따라서 Gauss 곡률은 곡면을 휘거나 구부려도 길이를 보존하는 한 변하지 않는다. 이 글에서는 [§제2기본형식, ⁋정리 6](/ko/math/riemannian_geometry/second_fundamental_form#thm6)에서 일반 submanifold에 대해 증명한 Gauss 방정식을 곡면의 경우에 적용하여 이 사실을 증명한다.

이 글 전체에서 $$M \subseteq \mathbb{R}^3$$은 매장된 2차원 곡면이고, $$g = \iota^\ast \bar g$$는 표준 Euclid metric $$\bar g$$의 제한이며, $$\nabla, \bar\nabla$$는 각각 $$(M, g)$$와 $$\mathbb{R}^3$$의 Levi-Civita 접속이다. $$M$$의 codimension이 $$1$$이므로 각 점 $$p$$에서 단위 법벡터 $$\nu$$는 부호를 빼면 유일하고, 이에 대응하는 shape operator $$S_\nu : T_p M \to T_p M$$ ([§제2기본형식, ⁋정의 4](/ko/math/riemannian_geometry/second_fundamental_form#def4))를 단순히 $$S$$로 적는다.

## 곡면의 Gauss 곡률

[§제2기본형식, ⁋명제 5](/ko/math/riemannian_geometry/second_fundamental_form#prop5)에서 보았듯 shape operator $$S$$는 $$T_p M$$ 위의 self-adjoint 선형사상이므로 실수 고윳값 $$k_1, k_2$$를 가지며 직교대각화된다. 이 고윳값들이 $$\nu$$ 방향의 principal curvature이다. 곡면이 주변 공간 안에서 휘는 정도를 한 수로 요약하는 가장 자연스러운 방법은 이 두 주곡률의 곱을 취하는 것이며, 이것이 Gauss 곡률이다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 곡면 $$M \subseteq \mathbb{R}^3$$의 점 $$p$$에서, 단위 법벡터 $$\nu$$에 대응하는 shape operator $$S$$의 두 principal curvature를 $$k_1, k_2$$라 하자. $$p$$에서의 *Gauss 곡률<sub>Gauss curvature</sub>* $$K$$는

$$K := \det S = k_1 k_2$$

로 정의된다.

</div>

행렬식은 기저 선택에 무관하므로 $$K$$는 well-defined이다. 법벡터 $$\nu$$를 반대 방향 $$-\nu$$로 바꾸면 [§제2기본형식, ⁋정의 4](/ko/math/riemannian_geometry/second_fundamental_form#def4)의 정의에서 $$S$$가 $$-S$$로 바뀌어 두 주곡률이 모두 부호를 바꾸므로, 그 곱인 $$K$$는 법벡터의 방향 선택에 무관하다. 이는 평균곡률 $$\tr S = k_1 + k_2$$가 법선 방향에 따라 부호를 바꾸는 것과 대조된다. $$K > 0$$인 점에서는 두 주곡률이 같은 부호여서 곡면이 한쪽으로 볼록하게 휘고 (구면, 타원면), $$K < 0$$인 점에서는 두 주곡률이 반대 부호여서 안장 모양을 이루며 (쌍곡포물면), $$K = 0$$인 점에서는 적어도 한 방향으로 곡면이 직선처럼 펴진다 (원기둥, 평면).

Gauss 곡률을 두 기본형식의 좌표 표현으로 적으면 고전적 곡면론의 공식을 얻는다. 곡면의 국소 매개화 $$\mathbf{x}(u, v)$$를 잡고, 제1기본형식 $$g$$와 제2기본형식 $$\mathrm{II}$$ ([§제2기본형식, ⁋정의 2](/ko/math/riemannian_geometry/second_fundamental_form#def2))의 성분을

$$\mathrm{I} = \begin{pmatrix} E & F \\ F & G \end{pmatrix}, \qquad \mathrm{II} = \begin{pmatrix} L & M \\ M & N \end{pmatrix}$$

로 적자. 여기서 $$E = \langle \mathbf{x}_u, \mathbf{x}_u\rangle$$, $$F = \langle \mathbf{x}_u, \mathbf{x}_v\rangle$$, $$G = \langle \mathbf{x}_v, \mathbf{x}_v\rangle$$이고 $$L = \langle \mathrm{II}(\partial_u, \partial_u), \nu\rangle$$ 등이다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 위 표기에서 곡면 $$M \subseteq \mathbb{R}^3$$의 Gauss 곡률은

$$K = \frac{\det \mathrm{II}}{\det \mathrm{I}} = \frac{LN - M^2}{EG - F^2}$$

로 주어진다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

좌표 기저 $$\partial_u, \partial_v$$에서 Weingarten 방정식 ([§제2기본형식, ⁋명제 5](/ko/math/riemannian_geometry/second_fundamental_form#prop5)) $$\langle S(\partial_i), \partial_j\rangle = \langle \mathrm{II}(\partial_i, \partial_j), \nu\rangle$$을 행렬로 옮긴다. $$S$$의 좌표 행렬을 $$[S]$$라 하면, $$S(\partial_i) = \sum_k [S]^k{}_i \partial_k$$이므로 좌변은 $$\sum_k [S]^k{}_i \langle \partial_k, \partial_j\rangle = \sum_k \mathrm{I}_{jk} [S]^k{}_i$$이고, 우변은 $$\mathrm{II}_{ij}$$이다. 따라서 행렬 등식

$$\mathrm{I} \, [S] = \mathrm{II}, \qquad \text{즉} \quad [S] = \mathrm{I}^{-1} \mathrm{II}$$

가 성립한다. 양변의 행렬식을 취하면

$$K = \det S = \det([S]) = \det(\mathrm{I}^{-1} \mathrm{II}) = \frac{\det \mathrm{II}}{\det \mathrm{I}} = \frac{LN - M^2}{EG - F^2}$$

를 얻는다. 마지막에서 $$\det \mathrm{I} = EG - F^2 > 0$$ (제1기본형식이 양의 정부호이므로)임을 사용했다.

</details>

[명제 2](#prop2)의 우변은 외재적인 자료로 적혀 있다. 분자 $$\det \mathrm{II}$$는 곡면이 주변 공간 안에서 휘는 방식을 담은 제2기본형식의 행렬식이며, 이 자체로는 매장에 의존하는 양이다. Gauss의 정리가 주장하는 바는 이 비 $$\det \mathrm{II} / \det \mathrm{I}$$가 결국 분모의 제1기본형식만으로 결정된다는 사실이다.

## Theorema Egregium

Gauss 곡률이 내재적임을 보이는 열쇠는 [§제2기본형식, ⁋정리 6](/ko/math/riemannian_geometry/second_fundamental_form#thm6)의 Gauss 방정식이다. 그 식은 곡면의 내재적 곡률 텐서 $$R$$과 주변 곡률 $$\bar R$$, 그리고 제2기본형식의 이차식을 잇는다. 주변 공간이 평탄한 $$\mathbb{R}^3$$이면 $$\bar R = 0$$이므로 제2기본형식의 이차식이 통째로 내재적 곡률 $$R$$로 표현되고, 그로부터 $$\det \mathrm{II}$$가 내재적 자료가 된다.

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3 (Theorema Egregium)**</ins> 곡면 $$M \subseteq \mathbb{R}^3$$의 Gauss 곡률 $$K$$는 점 $$p$$에서 정규직교기저 $$\{e_1, e_2\}$$를 잡을 때

$$K = \langle R(e_1, e_2) e_2, e_1\rangle$$

로 주어진다. 우변은 제1기본형식 $$g$$로부터 그 Levi-Civita 접속을 거쳐 정의되는 내재적 양이므로, $$K$$는 곡면의 매장이 아니라 제1기본형식만으로 결정되는 내재불변량이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\bar M = \mathbb{R}^3$$이 평탄하여 $$\bar R = 0$$이므로, Gauss 방정식 ([§제2기본형식, ⁋정리 6](/ko/math/riemannian_geometry/second_fundamental_form#thm6))은 정규직교 vector $$e_1, e_2 \in T_p M$$에 대해

$$0 = \langle R(e_1, e_2) e_2, e_1\rangle + \langle \mathrm{II}(e_1, e_2), \mathrm{II}(e_2, e_1)\rangle - \langle \mathrm{II}(e_2, e_2), \mathrm{II}(e_1, e_1)\rangle$$

를 준다. ($$X = e_1, Y = e_2, Z = e_2, W = e_1$$을 대입했다.) 따라서

$$\langle R(e_1, e_2) e_2, e_1\rangle = \langle \mathrm{II}(e_1, e_1), \mathrm{II}(e_2, e_2)\rangle - \lvert \mathrm{II}(e_1, e_2)\rvert^2$$

이다. 이제 우변을 shape operator로 다시 쓴다. Codimension이 $$1$$이므로 모든 제2기본형식 값은 단위 법벡터 $$\nu$$의 스칼라배이고, Weingarten 방정식에 의해 $$\langle \mathrm{II}(e_i, e_j), \nu\rangle = \langle S(e_i), e_j\rangle =: h_{ij}$$이다. 그러면 $$\mathrm{II}(e_i, e_j) = h_{ij}\, \nu$$이고 $$\lvert \nu\rvert = 1$$이므로

$$\langle \mathrm{II}(e_1, e_1), \mathrm{II}(e_2, e_2)\rangle - \lvert \mathrm{II}(e_1, e_2)\rvert^2 = h_{11} h_{22} - h_{12}^2 = \det[h_{ij}]$$

이다. 정규직교기저 $$\{e_1, e_2\}$$에서 $$[h_{ij}] = [\langle S(e_i), e_j\rangle]$$는 $$S$$의 행렬 그 자체이므로 $$\det[h_{ij}] = \det S = K$$이다 ([정의 1](#def1)). 따라서

$$\langle R(e_1, e_2) e_2, e_1\rangle = K$$

를 얻는다. 좌변은 $$g$$의 Levi-Civita 접속의 곡률 텐서 $$R$$ ([§리만 곡률, ⁋정의 2](/ko/math/riemannian_geometry/curvature#def2))만으로 적혀 있고, $$R$$은 $$g$$로부터 내재적으로 정의되므로 $$K$$도 그러하다.

</details>

[정리 3](#thm3)의 좌변 $$K = \det \mathrm{II} / \det \mathrm{I}$$는 외재적으로, 우변 $$\langle R(e_1, e_2) e_2, e_1\rangle$$는 내재적으로 적힌 같은 수이다. 이 등식이 정리의 핵심이다. 정의에서 $$K$$는 제2기본형식을 통해 곡면이 $$\mathbb{R}^3$$ 안에서 어떻게 휘는지에 의존하는 듯 보이지만, Gauss 방정식이 그 휘는 정보를 내재적 곡률 $$R$$로 흡수해 버린다. 곡면을 $$\mathbb{R}^3$$ 안에서 다르게 매장하더라도 길이를 보존하는 한 제1기본형식 $$g$$가 같고, 따라서 $$R$$도 같으며, 결국 $$K$$도 같다.

우변은 [§리만 곡률, ⁋명제 5](/ko/math/riemannian_geometry/curvature#prop5)의 대칭성을 갖춘 곡률 텐서를 정규직교 평면 $$\{e_1, e_2\}$$ 위에서 평가한 것으로, 이는 정확히 그 평면의 sectional curvature이다. 2차원 곡면에서는 각 점의 접평면이 유일하므로 sectional curvature가 한 수로 결정되고, 그것이 바로 Gauss 곡률이다. 따라서 2차원에서 Gauss 곡률과 sectional curvature는 같은 양의 두 이름이다.

<div class="remark" markdown="1">

<ins id="rmk4">**참고 4**</ins> [정리 3](#thm3)의 우변이 제1기본형식만으로 적힌다는 사실은 좌표 공식으로도 명시할 수 있다. 곡률 텐서 $$R$$의 성분은 제1기본형식 $$E, F, G$$와 그 1·2계 편미분으로 이루어진 Christoffel 기호로 표현되므로, Gauss 곡률은 $$E, F, G$$와 그 편미분만의 함수가 된다. 이를 명시적으로 적은 것이 *Brioschi 공식<sub>Brioschi formula</sub>*

$$K = \frac{\det \begin{pmatrix} -\tfrac12 E_{vv} + F_{uv} - \tfrac12 G_{uu} & \tfrac12 E_u & F_u - \tfrac12 E_v \\ F_v - \tfrac12 G_u & E & F \\ \tfrac12 G_v & F & G \end{pmatrix} - \det \begin{pmatrix} 0 & \tfrac12 E_v & \tfrac12 G_u \\ \tfrac12 E_v & E & F \\ \tfrac12 G_u & F & G \end{pmatrix}}{(EG - F^2)^2}$$

이다. 우변에 제2기본형식 $$L, M, N$$이 전혀 나타나지 않는다는 점이 Theorema Egregium을 좌표 차원에서 다시 확인해 준다. 직교 매개화 ($$F = 0$$)에서는 이 식이 훨씬 간단해져

$$K = -\frac{1}{2\sqrt{EG}}\left( \partial_u \frac{G_u}{\sqrt{EG}} + \partial_v \frac{E_v}{\sqrt{EG}} \right)$$

가 된다.

</div>

## 등거리 불변성과 따름정리

Theorema Egregium의 본래 의미는 Gauss 곡률이 *국소 등거리변형*에 불변이라는 것이다. 두 곡면 사이의 미분동형사상이 제1기본형식을 보존할 때 이를 *국소 등거리<sub>local isometry</sub>*라 부르는데, [정리 3](#thm3)에 의해 곡률 텐서는 제1기본형식만으로 결정되므로 국소 등거리는 Gauss 곡률을 점별로 보존한다.

<div class="proposition" markdown="1">

<ins id="cor5">**따름정리 5**</ins> $$\varphi : M \to M'$$이 곡면 사이의 국소 등거리이면, 즉 $$\varphi^\ast g' = g$$이면, 모든 점 $$p \in M$$에서 $$K_M(p) = K_{M'}(\varphi(p))$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\varphi$$가 제1기본형식을 보존하므로 그 Levi-Civita 접속과 곡률 텐서도 보존한다. 구체적으로 $$\varphi^\ast g' = g$$이면 리만 기하학의 기본 정리의 유일성에 의해 $$\varphi$$는 두 곡면의 Levi-Civita 접속을 대응시키고, 따라서 [§리만 곡률, ⁋정의 2](/ko/math/riemannian_geometry/curvature#def2)의 곡률 텐서도 대응시켜 $$\varphi_\ast(R_p(X, Y)Z) = R'_{\varphi(p)}(\varphi_\ast X, \varphi_\ast Y)\varphi_\ast Z$$를 만족한다. $$\varphi_\ast$$가 내적을 보존하므로 정규직교기저 $$\{e_1, e_2\} \subseteq T_p M$$은 정규직교기저 $$\{\varphi_\ast e_1, \varphi_\ast e_2\} \subseteq T_{\varphi(p)} M'$$로 옮겨지고, [정리 3](#thm3)에 의해

$$K_M(p) = \langle R(e_1, e_2) e_2, e_1\rangle = \langle R'(\varphi_\ast e_1, \varphi_\ast e_2)\varphi_\ast e_2, \varphi_\ast e_1\rangle = K_{M'}(\varphi(p))$$

이다.

</details>

이 따름정리의 가장 유명한 귀결은 구면을 평면 위에 펼칠 수 없다는 사실이다.

<div class="proposition" markdown="1">

<ins id="cor6">**따름정리 6**</ins> 단위 구면 $$S^2 \subseteq \mathbb{R}^3$$의 어떤 열린 영역도 평면 $$\mathbb{R}^2$$의 열린 영역과 국소 등거리가 아니다. 즉 구면의 일부를 길이를 보존하며 평면 위에 펼칠 수 없다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

[§제2기본형식, ⁋예시 10](/ko/math/riemannian_geometry/second_fundamental_form#ex10)에서 단위 구면 $$S^2$$의 모든 점에서 sectional curvature가 $$+1$$임을 계산했고, 2차원에서 이는 Gauss 곡률과 같으므로 $$S^2$$ 위에서 $$K \equiv 1$$이다. 한편 평면 $$\mathbb{R}^2$$는 표준 평탄 metric을 가지므로 곡률 텐서가 항등적으로 $$0$$, 즉 $$K \equiv 0$$이다. 만약 구면의 어떤 열린 영역 $$U$$가 평면의 열린 영역과 국소 등거리라면 [따름정리 5](#cor5)에 의해 $$U$$ 위에서 $$K \equiv 0$$이어야 하는데, 이는 $$K \equiv 1$$과 모순이다.

</details>

[따름정리 6](#cor6)은 지도제작이 본질적으로 안고 있는 왜곡의 수학적 근원이다. 구면인 지구의 한 조각을 평면 지도 위에 옮기는 어떤 방법도 모든 거리를 동시에 보존할 수는 없으며, 따라서 면적, 각도, 거리 가운데 적어도 하나는 반드시 왜곡된다. Mercator 도법은 각도를 보존하는 대신 고위도의 면적을 크게 부풀리고, 정적 도법은 면적을 보존하는 대신 모양을 일그러뜨린다. 어느 경우에도 Gauss 곡률 $$1$$과 $$0$$의 불일치를 등거리로 메울 수는 없기 때문에 완벽한 평면 지도는 존재하지 않는다.

반대로 Gauss 곡률이 $$0$$인 곡면은 평면으로 펼칠 수 있다. 원기둥과 원뿔은 한 주곡률이 $$0$$이어서 $$K \equiv 0$$이고, 실제로 종이를 휘어 만들 수 있으므로 평면의 일부와 국소 등거리이다. 이런 곡면을 *developable surface<sub>전개가능 곡면</sub>*라 부른다. Theorema Egregium은 이처럼 어떤 곡면이 평면으로 전개 가능한지를 외재적 모양이 아니라 내재적 곡률 $$K$$가 가른다는 사실을 분명히 한다.

---

**참고문헌**

**[dC]** Manfredo P. do Carmo, *Differential Geometry of Curves and Surfaces*, Prentice-Hall, 1976.

**[Lee]** John M. Lee, *Introduction to Riemannian Manifolds*, Graduate Texts in Mathematics, Springer, 2019.

**[Bri]** F. Brioschi, *Sur quelques formules relatives à la théorie des surfaces*, 1852.
