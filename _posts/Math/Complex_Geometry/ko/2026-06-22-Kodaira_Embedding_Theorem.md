---
title: "Kodaira 매장정리"
description: "정칙 선다발 위의 Hermitian 계량과 Chern 접속에서 곡률 형식과 제1 Chern 류를 세우고, 곡률이 Kähler 형식이 되는 양의 선다발을 정의한다. Kodaira 소멸정리를 해석적으로 서술하고, 콤팩트 복소다양체가 양의 선다발을 가지면 그 거듭제곱의 전역단면으로 사영공간에 매장됨을 보이는 Kodaira 매장정리를 다룬다. 따름정리로 정수 Kähler 류를 가진 콤팩트 복소다양체(Hodge 다양체)가 사영적임을 끌어내고, 복소사영공간·복소토러스·K3 곡면을 예로 든다."
excerpt: "Hermitian 선다발, Chern 접속, 곡률 형식, 제1 Chern 류, 양의 선다발, Kähler 곡률, Kodaira 소멸정리, Bochner–Kodaira–Nakano, very ample, Kodaira 매장정리, Hodge 다양체, 정수 Kähler 류, Chow 정리, 복소토러스, abelian variety, K3 곡면"

categories: [Math / Complex Geometry]
permalink: /ko/math/complex_geometry/kodaira_embedding_theorem
sidebar:
    nav: "complex_geometry-ko"

date: 2026-06-22
weight: 6

published: false
---

콤팩트 Kähler 다양체는 복소·리만·사교의 세 구조를 한 몸에 갖춘 풍부한 대상이지만 ([§Kähler 다양체, ⁋정의 3](/ko/math/complex_geometry/kahler_manifolds#def3)), 그 자체로는 대수기하의 대상이 아니다. 모든 매끄러운 사영다양체가 Kähler 다양체임은 보았으나 ([§Kähler 다양체, ⁋명제 9](/ko/math/complex_geometry/kahler_manifolds#prop9)), 그 역, 곧 어떤 콤팩트 복소다양체가 사영공간 $$\mathbb{CP}^N$$ 안으로 정칙매장되어 사영다양체가 되는가는 전혀 자명하지 않다. 복소토러스 가운데 일부만 사영적이고 ([§복소다양체, ⁋예시 7](/ko/math/complex_geometry/complex_manifolds#ex7)) 나머지는 Kähler이면서도 사영공간에 결코 들어가지 못한다는 사실이, 이 물음이 진짜 내용을 담고 있음을 말해 준다. 이 글의 주제는 그 판정을 완전히 해결하는 Kodaira의 정리이다. 답은 한 줄로 요약된다. 콤팩트 복소다양체가 사영적인 것은 그 위에 *양의 선다발*이 존재하는 것과 동치이다.

양의 선다발이란 정칙 선다발 가운데 그 곡률이 Kähler 형식이 되는 것을 말한다. 곧 사영성이라는 대역적·대수적 성질이, 선다발에 얹은 계량의 곡률이라는 국소·미분기하적 양정치성으로 환원된다. 이 환원을 가능하게 하는 두 기둥이 있다. 하나는 양의 선다발 위에서 고차 코호몰로지가 사라진다는 Kodaira 소멸정리이고, 다른 하나는 그 소멸을 충분히 큰 거듭제곱 $$L^{\otimes k}$$에 반복 적용하여 전역단면이 점을 분리하고 접벡터를 분리하도록 만드는 매장 논법이다. 우리는 먼저 선다발 위의 Hermitian 계량과 Chern 접속에서 곡률과 제1 Chern 류를 세우고, 양의 선다발을 정의한 뒤, Kodaira 소멸정리와 매장정리를 차례로 서술하며, 마지막으로 정수 Kähler 류를 가진 다양체가 사영적이라는 따름정리와 그 예시들을 다룬다.

## Hermitian 선다발과 Chern 접속

정칙 선다발은 그 자체로 미분기하적 양을 갖지 않으며, 곡률을 말하려면 먼저 fiber에 길이를 재는 계량을 얹어야 한다. 복소다양체 $$X$$ 위의 정칙 선다발 $$L$$이란 각 점의 fiber가 복소 1차원 벡터공간이고 전이함수가 정칙인 복소 선다발이다 ([\[대수다양체\] §선다발과 벡터다발, ⁋정의 1](/ko/math/algebraic_varieties/line_bundles#def1)). 여기에 fiber마다 매끄럽게 변하는 Hermitian 내적을 주는 것이 출발점이다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 복소다양체 $$X$$ 위의 정칙 선다발 $$L$$의 *Hermitian metric<sub>Hermitian 계량</sub>* $$h$$란, 각 점 $$x \in X$$의 fiber $$L_x$$ 위에 Hermitian 내적 $$h_x : L_x \times L_x \to \mathbb{C}$$를 매끄럽게 주는 것이다. 곧 국소 정칙틀 $$e$$ ($$L\vert_U$$의 영점 없는 정칙 단면) 에 대하여 양의 함수

$$
h(e, e) = e^{-\varphi}, \qquad \varphi \in C^\infty(U, \mathbb{R})
$$

가 정해지고, 두 단면 $$s = f e$$, $$t = g e$$의 내적이 $$h(s, t) = f \bar{g}\, e^{-\varphi}$$로 주어지는 것이다. 이러한 $$h$$를 갖춘 $$(L, h)$$를 *Hermitian line bundle<sub>Hermitian 선다발</sub>*이라 한다.

</div>

국소 정칙틀 $$e$$를 바꾸면 $$e' = u\, e$$ ($$u$$는 영점 없는 정칙함수) 이고, $$h(e', e') = \lvert u \rvert^2 h(e, e)$$이므로 퍼텐셜은 $$\varphi' = \varphi - \log\lvert u \rvert^2$$로 변한다. 따라서 $$\varphi$$ 자체는 대역적으로 정의되지 않지만, 그 변환이 정칙·반정칙 함수의 합 $$\log\lvert u\rvert^2 = \log u + \log\bar{u}$$만큼이라는 점이 결정적이다. 이 변환항은 $$\partial\bar\partial$$ 아래에서 소멸하므로, $$\partial\bar\partial\varphi$$가 틀의 선택과 무관한 대역적 $$(1,1)$$-형식을 정의하게 된다. 모든 복소다양체 위의 모든 정칙 선다발은 단위분할로 국소 계량을 이어붙여 Hermitian 계량을 가지므로, $$h$$의 존재 자체는 제약이 아니다. 제약은 그로부터 나오는 곡률의 양정치성에 있다.

Hermitian 계량은 단면을 미분하는 표준적인 방법, 곧 계량과 정칙구조에 모두 어울리는 접속을 유일하게 결정한다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2 (Chern 접속)**</ins> Hermitian 선다발 $$(L, h)$$ 위에 다음 두 조건을 만족하는 접속 $$\nabla$$가 유일하게 존재한다.

1. $$\nabla$$는 $$h$$와 호환된다. 곧 임의의 단면 $$s, t$$에 대하여 $$d\,h(s, t) = h(\nabla s, t) + h(s, \nabla t)$$이다.
2. $$\nabla$$의 $$(0,1)$$-성분은 정칙구조의 $$\bar\partial$$ 작용소와 일치한다. 곧 $$\nabla^{0,1} = \bar\partial$$이다.

이 $$\nabla$$를 $$(L, h)$$의 *Chern connection<sub>Chern 접속</sub>*이라 한다. 국소 정칙틀 $$e$$에서 $$h(e,e) = e^{-\varphi}$$일 때 그 접속형식은 $$\theta = \partial\log h(e, e) = -\partial\varphi$$로 주어진다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

국소 정칙틀 $$e$$를 고정하고 접속을 $$\nabla e = \theta \otimes e$$로 적으면, $$\theta$$는 $$U$$ 위의 복소값 $$1$$-형식이며 $$\nabla$$를 결정한다. 조건 (2)는 $$\nabla e$$의 $$(0,1)$$-성분이 $$\bar\partial e = 0$$ ($$e$$가 정칙이므로) 임을 요구하므로, $$\theta$$는 $$(1,0)$$-형식이어야 한다. 조건 (1)을 $$s = t = e$$에 적용하면

$$
d\, h(e, e) = h(\nabla e, e) + h(e, \nabla e) = \theta\, h(e,e) + \bar\theta\, h(e,e)
$$

이다. 좌변 $$d\,h(e,e) = (\partial + \bar\partial) h(e,e)$$를 $$(1,0)$$-성분과 $$(0,1)$$-성분으로 갈라 비교하면, $$\theta$$가 $$(1,0)$$-형식이고 $$\bar\theta$$가 $$(0,1)$$-형식이므로

$$
\partial\, h(e,e) = \theta\, h(e,e), \qquad \bar\partial\, h(e,e) = \bar\theta\, h(e,e)
$$

가 따라온다. 첫 식에서 $$\theta = \dfrac{\partial\, h(e,e)}{h(e,e)} = \partial\log h(e,e)$$로 $$\theta$$가 유일하게 결정되고, 둘째 식은 그 켤레로 자동으로 성립한다. $$h(e,e) = e^{-\varphi}$$이면 $$\theta = \partial(-\varphi) = -\partial\varphi$$이다. 역으로 이렇게 정의한 $$\theta$$가 두 조건을 모두 만족함은 위 계산을 거꾸로 읽으면 된다. 틀을 $$e' = u e$$로 바꾸면 $$\theta' = \partial\log(\lvert u\rvert^2 h(e,e)) = \theta + \partial\log u$$로 변환하는데, 이는 정확히 접속형식의 게이지 변환 법칙이므로 국소 정의들이 하나의 대역적 접속 $$\nabla$$로 이어붙는다.

</details>

Chern 접속의 곡률은 접속형식의 외미분으로 주어지며, 선다발이므로 그 값은 행렬이 아니라 스칼라값 $$2$$-형식이 된다. 곡률 $$\Theta = d\theta$$를 계산하면, $$\theta = -\partial\varphi$$이므로

$$
\Theta = d(-\partial\varphi) = -(\partial + \bar\partial)\partial\varphi = -\bar\partial\partial\varphi = \partial\bar\partial\varphi
$$

이다 ($$\partial^2 = 0$$, $$\bar\partial\partial = -\partial\bar\partial$$를 사용). 곧 곡률은 퍼텐셜의 $$\partial\bar\partial$$로, 정확히 앞서 관찰한 틀-불변 형식이다. 다음 정의에서 이를 대역적 곡률 형식으로 정식화한다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Hermitian 선다발 $$(L, h)$$의 Chern 접속의 *curvature form<sub>곡률 형식</sub>* $$\Theta = \Theta(L, h)$$를, 국소 정칙틀 $$e$$에서 $$h(e,e) = e^{-\varphi}$$일 때

$$
\Theta = \partial\bar\partial\varphi = -\partial\bar\partial\log h(e, e)
$$

로 정의되는 대역적 $$2$$-형식이라 한다. 이는 순허수 $$(1,1)$$-형식이며 (실함수 $$\varphi$$에 대해 $$\overline{\partial\bar\partial\varphi} = -\partial\bar\partial\varphi$$이므로), 여기에 $$\frac{i}{2\pi}$$를 곱해 실형식으로 정규화한 $$L$$의 *first Chern form<sub>제1 Chern 형식</sub>*을

$$
c_1(L, h) = \frac{i}{2\pi}\,\Theta
$$

로 정의한다.

</div>

곡률 $$\Theta$$가 틀의 선택과 무관함은 퍼텐셜 변환항 $$\log\lvert u\rvert^2$$가 $$\partial\bar\partial$$로 소멸하기 때문이고, $$\Theta$$가 닫힌 $$(1,1)$$-형식임은 그 정의 $$\Theta = \partial\bar\partial\varphi$$에서 직접 따라온다 ($$d\Theta = (\partial + \bar\partial)\partial\bar\partial\varphi = 0$$). $$\Theta$$ 자체는 $$\overline{\partial\bar\partial\varphi} = \bar\partial\partial\bar\varphi = -\partial\bar\partial\varphi$$로 순허수이지만, $$\frac{i}{2\pi}$$ 정규화를 거친 $$c_1(L,h)$$는 닫힌 실 $$(1,1)$$-형식이 된다. 결정적으로, 제1 Chern 형식의 de Rham 류는 계량 $$h$$의 선택과 무관하다. 두 계량 $$h$$, $$h'$$의 비 $$h'/h = e^{-\psi}$$는 대역적 양함수 $$e^{-\psi}$$로 주어지므로 두 곡률의 차가 $$\Theta' - \Theta = \partial\bar\partial\psi = d(\bar\partial\psi)$$로 완전형식이 되어, 코호몰로지류

$$
c_1(L) = [c_1(L, h)] = \left[ \frac{i}{2\pi}\Theta \right] \in H^2(X, \mathbb{R})
$$

가 잘 정의된다. 이 류 $$c_1(L)$$이 선다발 $$L$$의 *제1 Chern 류*이며, 이는 대수기하·위상수학에서 정수계수로 정의되는 제1 Chern 류 ([\[대수다양체\] §천 특성류, ⁋정의 1](/ko/math/algebraic_varieties/chern_classes#def1)) 와 일치한다. 곧 $$c_1(L)$$은 $$H^2(X, \mathbb{Z})$$ ([\[대수적 위상수학\] §코호몰로지, ⁋정의 2](/ko/math/algebraic_topology/cohomology#def2)) 의 상에 놓이는 정수류이며, 그 실수 대표를 곡률로 실현하는 것이 위 공식이다.

## 양의 선다발

곡률에서 만든 실 $$(1,1)$$-형식 $$\omega_L = \frac{i}{2\pi}\Theta$$는 각 점에서 Hermitian 형식을 정의하므로, 그것이 양정치인지를 물을 수 있다. 이 양정치성이 선다발의 사영기하적 성질 전부를 좌우한다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> 콤팩트 복소다양체 $$X$$ 위의 정칙 선다발 $$L$$이 *positive<sub>양의</sub>*라는 것은, 어떤 Hermitian 계량 $$h$$가 존재하여 그 곡률 형식 $$\Theta(L, h)$$로부터 얻는 실 $$(1,1)$$-형식

$$
\omega_L = \frac{i}{2\pi}\,\Theta(L, h)
$$

가 양정치인 것이다. 곧 국소 정칙틀에서 $$\Theta = \partial\bar\partial\varphi = \sum_{j,k} \varphi_{j\bar{k}}\, dz_j \wedge d\bar{z}_k$$로 쓸 때, 각 점에서 Hermitian 행렬 $$(\varphi_{j\bar{k}})$$가 양의 정부호인 것이다. 이때 $$c_1(L)$$을 *positive class<sub>양의 류</sub>*라 부른다.

</div>

양의 선다발의 정의는 곧 곡률 형식이 Kähler 형식이라는 조건이다. $$\omega_L = \frac{i}{2\pi}\Theta$$는 닫힌 실 $$(1,1)$$-형식이고, 양정치성은 그것이 비퇴화일 뿐 아니라 양의 Hermitian 계량 $$g_{j\bar{k}} = \varphi_{j\bar{k}}$$를 정의함을 뜻한다. 따라서 $$L$$이 양의 선다발이면 $$\omega_L$$은 $$X$$ 위의 Kähler 형식이 되고, 그 Kähler 류 $$[\omega_L] = c_1(L)$$은 양의 류이자 정수류이다. 역으로 어떤 Kähler 형식 $$\omega$$가 $$c_1(L)$$을 대표하면, $$\partial\bar\partial$$-보조정리로 그 류 안에서 곡률 형식과 일치하는 대표를 골라 양의 계량을 구성할 수 있다. 곧 양의 선다발의 존재는 다음 세 조건의 동치로 정리된다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> 콤팩트 복소다양체 $$X$$ 위의 정칙 선다발 $$L$$에 대하여 다음이 동치이다.

1. $$L$$은 양의 선다발이다.
2. $$c_1(L)$$을 대표하는 양의 $$(1,1)$$-형식 $$\omega = \frac{i}{2\pi}\Theta(L, h)$$가 존재한다.
3. $$L$$의 어떤 계량에 대한 곡률 형식 $$\frac{i}{2\pi}\Theta(L, h)$$가 $$X$$ 위의 Kähler 형식이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

(1) ⟺ (2)는 정의의 재진술이다. [정의 4](#def4)에서 $$L$$이 양이라는 것은 어떤 $$h$$의 곡률로 만든 $$\omega_L = \frac{i}{2\pi}\Theta(L,h)$$가 양정치인 것이고, 이 $$\omega_L$$이 [정의 3](#def3)의 $$c_1(L)$$을 대표하므로 곧 (2)이다.

(2) ⟺ (3)을 본다. $$\omega = \frac{i}{2\pi}\Theta(L, h)$$는 [정의 3](#def3) 직후에 본 바와 같이 닫힌 실 $$(1,1)$$-형식이다 ($$\Theta = \partial\bar\partial\varphi$$이므로 $$d\omega = 0$$). 따라서 $$\omega$$가 양정치라는 조건은, 닫힌 실 $$(1,1)$$-형식이 양정치라는 것, 곧 그것이 정의하는 Hermitian 계량 $$g_{j\bar{k}} = \varphi_{j\bar{k}}$$가 리만 계량이고 그 기본형식이 $$\omega$$인 것과 같다. 닫힘과 양정치를 모두 갖춘 실 $$(1,1)$$-형식은 정확히 Kähler 형식이므로 ([§Kähler 다양체, ⁋정의 3](/ko/math/complex_geometry/kahler_manifolds#def3)), (2)와 (3)은 동치이다. 곧 $$L$$이 양이라는 것은 그 곡률을 Kähler 형식으로 만드는 계량이 존재한다는 것과 같다.

</details>

이 명제가 양의 선다발과 Kähler 기하를 잇는 다리이다. 양의 선다발을 갖는 콤팩트 복소다양체는 자동으로 Kähler 다양체이며, 그 Kähler 류는 $$H^2(X, \mathbb{Z})$$ 안에 놓이는 정수류이다. 거꾸로 이 정수성이 매장정리의 핵심이다. 정수 Kähler 류는 어떤 선다발의 제1 Chern 류로 실현되고, 그 선다발이 바로 사영매장을 만들어 내는 양의 선다발이 된다. 가장 단순한 예는 복소사영공간의 초평면다발이다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6 ($$\mathbb{CP}^n$$의 $$\mathcal{O}(1)$$)**</ins> 복소사영공간 $$\mathbb{CP}^n$$ ([§복소다양체, ⁋예시 6](/ko/math/complex_geometry/complex_manifolds#ex6)) 위의 초평면다발 $$\mathcal{O}(1)$$ ([\[대수다양체\] §선다발과 벡터다발, ⁋예시 12](/ko/math/algebraic_varieties/line_bundles#ex12))을 생각하자. 그 쌍대인 tautological bundle $$\mathcal{O}(-1)$$에 표준 Hermitian 계량 $$h([z])(v, v) = \lVert v \rVert^2$$ ($$v \in \mathcal{O}(-1)_{[z]} \subseteq \mathbb{C}^{n+1}$$이 직선 위의 벡터) 를 주면, 그 쌍대계량을 $$\mathcal{O}(1)$$에 얹었을 때 곡률 형식이

$$
\frac{i}{2\pi}\Theta(\mathcal{O}(1), h) = \omega_{\mathrm{FS}}
$$

로 정확히 Fubini–Study 형식 ([§Kähler 다양체, ⁋예시 8](/ko/math/complex_geometry/kahler_manifolds#ex8))이 된다. $$\omega_{\mathrm{FS}}$$는 양정치 Kähler 형식이므로 $$\mathcal{O}(1)$$은 양의 선다발이고, $$c_1(\mathcal{O}(1)) = [\omega_{\mathrm{FS}}]$$는 $$H^2(\mathbb{CP}^n, \mathbb{Z})$$의 생성원이다. 곧 $$\mathbb{CP}^n$$은 양의 선다발을 가지며, 항등 매장 $$\mathbb{CP}^n \hookrightarrow \mathbb{CP}^n$$이 $$\mathcal{O}(1)$$의 전역단면(동차좌표 $$z_0, \ldots, z_n$$)으로 주어진다는 점에서 매장정리의 결론을 자명하게 실현한다.

</div>

## Kodaira 소멸정리

매장정리의 첫째 기둥은 양의 선다발 위에서 고차 코호몰로지가 사라진다는 소멸정리이다. 이는 정칙 선다발의 전역단면을 충분히 확보하기 위한 도구이며, 그 해석적 증명은 곡률의 양정치성을 코호몰로지의 소멸로 바꾸는 Bochner 유형의 항등식에서 나온다.

<div class="proposition" markdown="1">

<ins id="thm7">**정리 7 (Kodaira 소멸정리)**</ins> $$X$$를 복소차원 $$n$$의 콤팩트 복소다양체, $$L$$을 $$X$$ 위의 양의 선다발이라 하자. $$K_X = \Omega^n_X$$를 표준선다발 ([\[대수다양체\] §표준선다발, ⁋정의 5](/ko/math/algebraic_varieties/canonical_bundle#def5)) 이라 하면, 모든 $$q > 0$$에 대하여

$$
H^q(X, K_X \otimes L) = 0
$$

이 성립한다. 동치로, $$\Omega^n_X \otimes L$$의 값을 갖는 모든 $$q > 0$$차 Dolbeault 코호몰로지가 소멸한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

증명의 해석적 핵심만 서술하고 타원작용소 이론의 표준 결과는 인용한다. $$L$$이 양이므로 [명제 5](#prop5)에 의해 $$X$$는 곡률 형식 $$\omega = \frac{i}{2\pi}\Theta(L, h)$$를 Kähler 형식으로 갖는다. $$K_X \otimes L$$의 값을 갖는 $$(0, q)$$-형식 공간 위에서 $$\bar\partial$$-Laplace 작용소 $$\Delta_{\bar\partial} = \bar\partial\bar\partial^\ast + \bar\partial^\ast\bar\partial$$를 생각하면, Hodge 정리의 선다발 판본 ([§Hodge 이론, ⁋정리 6](/ko/math/complex_geometry/hodge_theory#thm6) 직후에 서술한 $$\bar\partial$$-Hodge 정리를 선다발 계수로 일반화한 것) 에 의해 $$H^q(X, K_X \otimes L) \cong \mathcal{H}^{n,q}(X, L)$$로 조화형식 공간과 동형이다. 따라서 $$q > 0$$에서 $$(n, q)$$-차 조화형식이 $$0$$임을 보이면 된다.

여기서 결정적 입력은 *Bochner–Kodaira–Nakano 항등식*이다. 두 Laplace 작용소 $$\Delta_{\bar\partial}$$와 $$\Delta_\partial$$의 차가 곡률 작용소로 표현되어,

$$
\Delta_{\bar\partial} = \Delta_\partial + [i\Theta(L, h), \Lambda]
$$

가 성립한다 (여기서 $$\Lambda$$는 Kähler 형식과의 wedge 곱 $$L_\omega$$의 수반작용소 ([§Kähler 다양체, ⁋정리 12](/ko/math/complex_geometry/kahler_manifolds#thm12))). $$(n, q)$$-형식 $$\alpha$$가 조화이면 $$\Delta_{\bar\partial}\alpha = 0$$이고, 위 항등식을 $$\alpha$$와의 $$L^2$$-내적에 적용하면

$$
0 = (\Delta_{\bar\partial}\alpha, \alpha) = \lVert \partial^\ast\alpha \rVert^2 + \lVert \partial\alpha \rVert^2 + \big( [i\Theta, \Lambda]\alpha, \alpha \big)
$$

를 얻는다. 마지막 곡률항은 $$L$$이 양의 선다발이라 $$i\Theta = 2\pi\,\omega_L$$이 양정치 $$(1,1)$$-형식이므로, $$(n, q)$$-형식($$q > 0$$) 위에서 양의 작용소가 된다. 곧 점별로 $$([i\Theta, \Lambda]\alpha, \alpha) \geq c\, q\, \lvert \alpha \rvert^2$$ ($$c > 0$$은 곡률의 최소 고윳값에서 오는 상수) 라는 Nakano 양정치 부등식이 성립한다. 그러면 위 등식의 우변은 음이 아닌 세 항의 합인데 그 합이 $$0$$이므로, 특히 곡률항이 $$0$$이고 따라서 $$\alpha = 0$$이다. $$q > 0$$인 모든 조화 $$(n, q)$$-형식이 $$0$$이므로 $$H^q(X, K_X \otimes L) = 0$$이다.

</details>

이 소멸정리는 양의 선다발 $$L$$을 점점 더 큰 거듭제곱 $$L^{\otimes k}$$로 비틀면 더욱 강력해진다. $$L$$이 양이면 $$L^{\otimes k}$$의 곡률이 $$k\Theta$$로 $$k$$배 양정치이므로, $$L^{\otimes k}$$도 양의 선다발이고 소멸정리가 그대로 적용된다. 표준선다발과의 텐서를 떼어내기 위해 $$L^{\otimes k} \otimes K_X^{-1}$$에 적용하면, $$k$$가 충분히 클 때 $$L^{\otimes k} \otimes K_X^{-1}$$도 여전히 양이므로 $$H^q(X, K_X \otimes (L^{\otimes k} \otimes K_X^{-1})) = H^q(X, L^{\otimes k}) = 0$$ ($$q > 0$$) 이 따라온다. 이 고차 코호몰로지의 소멸이 전역단면의 풍부함을 보장하는 메커니즘이며, 매장 논법의 기관차가 된다. 한편 이 정리는 매끄러운 사영다양체에 대한 대수적 Kodaira 소멸정리 ([\[대수다양체\] §고다이라 소멸정리, ⁋명제 1](/ko/math/algebraic_varieties/kodaira_vanishing#prop1)) 와 같은 결론을 주며, 그쪽이 Serre 쌍대를 거친 대수적 판본인 반면 여기서는 곡률과 조화형식을 통한 해석적 판본이다.

## Kodaira 매장정리

이제 주정리를 서술한다. 매장정리의 둘째 기둥은 소멸정리를 반복 적용하여 $$L^{\otimes k}$$ ($$k \gg 0$$) 의 전역단면이 사영매장을 정의하도록 만드는 것이다. 전역단면 공간을 $$\Gamma(X, L^{\otimes k})$$ ([\[대수다양체\] §선다발과 벡터다발, ⁋정의 15](/ko/math/algebraic_varieties/line_bundles#def15)) 라 하고, 기저 $$s_0, \ldots, s_N$$을 택하면 사상

$$
\Phi_k : X \dashrightarrow \mathbb{CP}^N, \qquad x \mapsto [s_0(x) : \cdots : s_N(x)]
$$

가 단면들이 동시에 소멸하지 않는 점들에서 정의된다. 이 $$\Phi_k$$가 모든 점에서 잘 정의되고(기저점 없음), 단사이며(점 분리), 도함수가 단사(접벡터 분리)일 때 $$\Phi_k$$는 정칙매장이 되고 $$L^{\otimes k}$$을 *very ample<sub>매우 풍부한</sub>* 선다발이라 부른다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> 콤팩트 복소다양체 $$X$$ 위의 정칙 선다발 $$M$$이 *very ample<sub>매우 풍부한</sub>*이라는 것은, 전역단면들의 기저 $$s_0, \ldots, s_N \in \Gamma(X, M)$$로 정의되는 사상 $$\Phi_M : X \to \mathbb{CP}^N$$이 정칙매장인 것, 곧 다음 세 조건을 만족하는 것이다.

1. *기저점 없음<sub>base-point freeness</sub>*: 각 점 $$x$$에서 어떤 $$s_i$$가 $$s_i(x) \neq 0$$이다. 따라서 $$\Phi_M$$이 $$X$$ 전체에서 정의된다.
2. *점 분리<sub>separation of points</sub>*: $$x \neq y$$이면 어떤 단면이 $$s(x) = 0$$, $$s(y) \neq 0$$이 되어 $$\Phi_M(x) \neq \Phi_M(y)$$이다.
3. *접벡터 분리<sub>separation of tangent vectors</sub>*: 각 점 $$x$$에서 $$\Phi_M$$의 미분 $$d\Phi_M\vert_x$$가 단사이다.

</div>

세 조건은 정확히 $$\Phi_M$$이 정칙 단사 몰입, 곧 콤팩트성과 함께 정칙매장이 되기 위한 요구이다. (1)은 사상이 어디서나 정의되게 하고, (2)는 단사성을, (3)은 몰입성을 보장한다. $$X$$가 콤팩트이므로 단사 몰입은 곧 위상적 매장이고, 정칙 단사 몰입은 닫힌 복소 부분다양체로의 매장이 된다. 따라서 $$M$$이 very ample이면 $$X$$는 $$\Phi_M$$을 통해 $$\mathbb{CP}^N$$의 매끄러운 닫힌 부분다양체로 실현되어 사영다양체 ([\[대수다양체\] §사영다양체, ⁋정의 1](/ko/math/algebraic_varieties/projective_varieties#def1)) 가 된다. 세 분리 조건 각각을 단면의 존재로 환원하면, 그 단면의 존재가 다름 아닌 고차 코호몰로지의 소멸에서 나온다는 것이 매장정리 증명의 골자이다.

<div class="proposition" markdown="1">

<ins id="thm9">**정리 9 (Kodaira 매장정리)**</ins> $$X$$를 콤팩트 복소다양체라 하자. $$X$$ 위에 양의 선다발 $$L$$이 존재하면, 충분히 큰 모든 $$k$$에 대하여 $$L^{\otimes k}$$은 very ample이다. 따라서 $$\Phi_{L^{\otimes k}} : X \hookrightarrow \mathbb{CP}^N$$이 정칙매장이고, $$X$$는 사영다양체이다. 역으로 사영다양체는 양의 선다발($$\mathbb{CP}^N$$의 $$\mathcal{O}(1)$$의 제한)을 가진다. 곧 콤팩트 복소다양체 $$X$$가 사영적인 것은 $$X$$ 위에 양의 선다발이 존재하는 것과 동치이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

역방향부터 본다. $$X \subseteq \mathbb{CP}^N$$이 매끄러운 사영다양체이면, [예시 6](#ex6)에서 $$\mathcal{O}(1)$$이 $$\mathbb{CP}^N$$ 위의 양의 선다발이므로 그 제한 $$\mathcal{O}(1)\vert_X$$도 Fubini–Study 형식의 제한을 곡률로 가져 양정치이다 ([§Kähler 다양체, ⁋명제 9](/ko/math/complex_geometry/kahler_manifolds#prop9)의 유도 Kähler 형식이 양정치). 따라서 $$X$$는 양의 선다발을 가진다.

정방향이 본질적인 내용이며, 핵심 단계만 제시한다. 목표는 충분히 큰 $$k$$에서 $$L^{\otimes k}$$이 [정의 8](#def8)의 세 조건을 만족함을 보이는 것이고, 세 조건 모두 적절한 전역단면의 존재로 환원된 뒤 [정리 7](#thm7)의 소멸로 해결된다.

*점 분리.* 서로 다른 두 점 $$x, y \in X$$를 분리하려면, $$s(x) = 0$$이고 $$s(y) \neq 0$$인 단면 $$s \in \Gamma(X, L^{\otimes k})$$를 찾으면 된다. 두 점에서 동시에 소멸하는 단면들의 부분공간을 보기 위해, $$x, y$$를 blow up한 $$\pi : \widetilde{X} \to X$$를 도입하고 그 예외인자를 $$E_x, E_y$$라 하자. blow-up의 표준선다발 변화 공식 ([\[대수다양체\] §표준선다발, ⁋명제 12](/ko/math/algebraic_varieties/canonical_bundle#prop12)) 에 의해, $$\pi^\ast L^{\otimes k} \otimes \mathcal{O}(-E_x - E_y) \otimes K_{\widetilde{X}}^{-1}$$이 $$k \gg 0$$에서 여전히 양이 되도록 할 수 있다. 그러면 [정리 7](#thm7)을 $$\widetilde{X}$$ 위에서 적용하여 $$H^1(\widetilde{X}, \pi^\ast L^{\otimes k} \otimes \mathcal{O}(-E_x - E_y)) = 0$$을 얻고, 이 $$H^1$$의 소멸이 제한사상

$$
\Gamma(X, L^{\otimes k}) \longrightarrow L^{\otimes k}_x \oplus L^{\otimes k}_y
$$

의 전사성을 준다. 곧 두 fiber에서의 값을 독립적으로 처방하는 단면이 존재하여 $$x, y$$가 분리된다. 같은 논법에서 한 점 $$x$$만 처방하면 *기저점 없음*이 따라온다.

*접벡터 분리.* 한 점 $$x$$에서 $$\Phi_{L^{\otimes k}}$$의 미분이 단사이려면, $$x$$에서 $$1$$차까지 소멸하는 단면(곧 $$s(x) = 0$$이고 $$ds(x) = 0$$) 과 $$0$$차에서만 소멸하는 단면($$s(x) = 0$$, $$ds(x) \neq 0$$) 을 구별할 수 있어야 한다. 이는 $$x$$를 blow up하여 예외인자 $$E$$ 위에서 $$\mathcal{O}(-2E)$$ 류를 비트는 같은 소멸 논법으로, 제한사상 $$\Gamma(X, L^{\otimes k}) \to L^{\otimes k}_x \otimes (\mathcal{O}_X / \mathfrak{m}_x^2)$$ ($$\mathfrak{m}_x$$는 $$x$$의 극대 아이디얼) 의 전사성으로 환원되고, 다시 $$H^1$$의 소멸이 이를 보장한다.

세 조건이 모두 충분히 큰 $$k$$에서 성립하고, 콤팩트성으로 그 $$k$$를 $$x, y$$에 무관하게 한꺼번에 택할 수 있으므로, $$L^{\otimes k}$$은 very ample이다. 따라서 $$\Phi_{L^{\otimes k}} : X \hookrightarrow \mathbb{CP}^N$$이 정칙매장이고 $$X$$는 사영다양체이다. 기술적 세부, 특히 blow-up 위에서 양성을 유지하는 $$k$$의 존재와 $$H^1$$-소멸에서 전사성으로 가는 정확한 long exact sequence 논증은 인용에 맡긴다.

</details>

이 정리에서 반드시 강조할 점은 매장을 주는 것이 $$L$$ 자체가 아니라 그 충분히 큰 거듭제곱 $$L^{\otimes k}$$이라는 것이다. $$L$$의 전역단면은 매장을 정의하기에 너무 적을 수 있으며, $$k$$를 키워 곡률을 $$k$$배로 양정치화해야 소멸정리가 충분한 단면을 공급한다. 마찬가지로 매장 $$\Phi_{L^{\otimes k}}$$이 들어가는 사영공간의 차원 $$N = \dim\Gamma(X, L^{\otimes k}) - 1$$도 $$k$$에 따라 커진다. 정리의 결론은 어떤 $$k$$와 어떤 $$N$$에 대해 매장이 존재한다는 것이지, 미리 정한 작은 $$N$$이나 $$L$$ 자체로 된다는 것이 아니다. 이 정리는 미분기하적 조건(곡률의 양정치성)에서 대수기하적 결론(사영성)을 끌어내며, 복소해석과 대수기하를 잇는 다리로서 콤팩트 복소다양체론의 정점에 놓인다.

## Hodge 다양체와 Chow 정리

매장정리의 가정인 양의 선다발의 존재는, 코호몰로지의 언어로 정수 Kähler 류의 존재로 번역된다. 이것이 정리를 위상적으로 검출 가능한 형태로 바꾸어 준다.

<div class="definition" markdown="1">

<ins id="def10">**정의 10**</ins> 콤팩트 복소다양체 $$X$$ 위의 Kähler 형식 $$\omega$$의 Kähler 류 $$[\omega] \in H^2(X, \mathbb{R})$$가 정수 코호몰로지의 상에 놓일 때, 곧

$$
[\omega] \in \Img\big( H^2(X, \mathbb{Z}) \to H^2(X, \mathbb{R}) \big)
$$

일 때, $$\omega$$를 *integral Kähler form<sub>정수 Kähler 형식</sub>*, 그 류를 *integral Kähler class<sub>정수 Kähler 류</sub>*라 한다. 정수 Kähler 류를 적어도 하나 갖는 콤팩트 복소다양체를 *Hodge manifold<sub>Hodge 다양체</sub>*라 한다.

</div>

정수 Kähler 류의 조건은 양의 선다발의 존재와 정확히 같은 내용이다. 제1 Chern 류 사상 $$c_1 : \Pic(X) \to H^2(X, \mathbb{Z})$$의 상은 정확히 정칙 선다발로 실현되는 정수류 전체이며, Kähler 류가 정수류라는 것은 그것이 어떤 선다발 $$L$$의 $$c_1(L)$$로 표현된다는 것이다. 그 $$L$$의 곡률을 Kähler 형식과 맞추면 $$L$$이 양의 선다발이 된다. 따라서 정수 Kähler 류의 존재와 양의 선다발의 존재가 동치이고, 매장정리는 다음 따름정리로 다시 쓰인다.

<div class="proposition" markdown="1">

<ins id="cor11">**따름정리 11 (Kodaira 판정)**</ins> 콤팩트 복소다양체 $$X$$가 Hodge 다양체이면, 곧 정수 Kähler 류를 가지면, $$X$$는 사영다양체이다. 따라서 콤팩트 복소다양체가 사영적인 것은 그것이 Hodge 다양체인 것과 동치이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$X$$가 정수 Kähler 류 $$[\omega] \in H^2(X, \mathbb{Z})$$를 갖는다고 하자. 콤팩트 Kähler 다양체에서 Hodge 분해 ([§Hodge 이론, ⁋정리 9](/ko/math/complex_geometry/hodge_theory#thm9)) 에 의해 $$H^2(X, \mathbb{C}) = H^{2,0} \oplus H^{1,1} \oplus H^{0,2}$$이고, Kähler 형식 $$\omega$$는 실 $$(1,1)$$-형식이므로 그 류는 $$H^{1,1}(X) \cap H^2(X, \mathbb{Z})$$에 놓인다. Lefschetz의 $$(1,1)$$-류 정리에 의해 이러한 정수 $$(1,1)$$-류는 모두 어떤 정칙 선다발 $$L$$의 제1 Chern 류 $$c_1(L)$$로 실현된다 (지수열 $$0 \to \mathbb{Z} \to \mathcal{O}_X \to \mathcal{O}_X^\ast \to 0$$의 연결사상 $$H^1(X, \mathcal{O}_X^\ast) = \Pic(X) \to H^2(X, \mathbb{Z})$$의 상이 정확히 $$H^{1,1} \cap H^2(X, \mathbb{Z})$$이다). 곧 $$c_1(L) = [\omega]$$인 $$L$$이 존재한다.

이제 $$\omega$$가 $$c_1(L)$$을 대표하는 양의 $$(1,1)$$-형식이므로, [명제 5](#prop5)에 의해 $$L$$은 양의 선다발이다. [정리 9](#thm9)를 적용하면 $$X$$는 사영다양체이다. 역으로 사영다양체는 $$\mathcal{O}(1)$$의 제한으로 양의 선다발을 가지고, 그 Kähler 류 $$[\omega_{\mathrm{FS}}\vert_X] = c_1(\mathcal{O}(1)\vert_X)$$가 정수류이므로 Hodge 다양체이다.

</details>

이 따름정리가 Kodaira 정리의 가장 쓰기 좋은 형태이다. 콤팩트 복소다양체가 사영적인지를 묻는 대신, 그 위에 정수 Kähler 류가 있는지만 확인하면 된다. 그런데 사영적이라는 결론에는 아직 미세한 간격이 있다. 매장 $$X \hookrightarrow \mathbb{CP}^N$$이 주는 것은 $$X$$가 $$\mathbb{CP}^N$$의 닫힌 복소 *해석적* 부분다양체라는 것이지, 곧바로 다항식으로 정의되는 대수적 부분다양체라는 것은 아니다. 이 간격을 메우는 것이 Chow의 정리이다.

<div class="proposition" markdown="1">

<ins id="thm12">**정리 12 (Chow)**</ins> 복소사영공간 $$\mathbb{CP}^N$$의 닫힌 복소 해석적 부분집합은 모두 대수적이다. 곧 유한 개의 동차다항식의 공통 영점으로 주어진다. 따라서 $$\mathbb{CP}^N$$에 정칙매장된 콤팩트 복소다양체는 매끄러운 사영대수다양체이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

핵심만 서술한다. $$Z \subseteq \mathbb{CP}^N$$을 닫힌 복소 해석적 부분집합이라 하고, 그 아핀 뿔 $$\widehat{Z} \subseteq \mathbb{C}^{N+1}$$을 원점을 포함하는 원뿔로 잡으면 $$\widehat{Z}$$는 $$\mathbb{C}^{N+1}$$의 닫힌 해석적 부분집합이다. 원점에서 $$\widehat{Z}$$를 정의하는 정칙함수들의 멱급수를 동차성분으로 전개하면, $$\widehat{Z}$$가 원뿔(스칼라곱에 닫힘)이라는 사실에서 각 동차성분이 다시 $$\widehat{Z}$$ 위에서 소멸함을 보일 수 있다. 곧 $$\widehat{Z}$$의 아이디얼이 동차다항식들로 생성된다. 더 정밀하게는, 콤팩트 복소다양체 위의 유리형 함수체가 초월차수 유한한 대수적 함수체라는 Siegel 정리, 또는 한 변수 정칙함수의 영점 집적과 $$\mathbb{CP}^N$$의 콤팩트성을 결합한 고전적 논법으로, $$Z$$의 국소 정의함수들이 대역적 동차다항식으로 대체됨을 얻는다. 따라서 $$Z = Z(F_1, \ldots, F_r)$$로 동차다항식의 공통 영점이 되어 $$Z$$가 사영대수적 집합 ([\[대수다양체\] §사영다양체, ⁋정의 3](/ko/math/algebraic_varieties/projective_varieties#def3)) 이다. $$Z$$가 매끄러운 복소 부분다양체이면 그 대수적 실현도 매끄러운 사영대수다양체이다. 완전한 증명은 인용에 맡긴다.

</details>

Chow 정리와 매장정리를 합치면 결론이 깔끔해진다. Hodge 다양체는 어떤 $$\mathbb{CP}^N$$에 정칙매장되고, Chow 정리에 의해 그 상은 동차다항식으로 정의되는 매끄러운 사영대수다양체이다. 곧 사영 복소다양체와 사영대수다양체가 같은 대상이 되어, 복소해석적으로 정의된 Hodge 다양체가 순수 대수기하의 대상으로 옮겨진다. 이것이 콤팩트 Kähler 다양체와 사영대수다양체 사이의 경계를 정확히 그어 주는 GAGA적 결론이다.

## 예시

Kodaira 판정의 힘은 사영성과 비사영성을 가르는 구체적인 예에서 드러난다. 가장 먼저 보았던 복소사영공간은 자명한 양의 예이다.

<div class="example" markdown="1">

<ins id="ex13">**예시 13 ($$\mathbb{CP}^n$$과 그 부분다양체)**</ins> [예시 6](#ex6)에서 $$\mathbb{CP}^n$$은 양의 선다발 $$\mathcal{O}(1)$$을 가지므로 [정리 9](#thm9)에 의해 사영적이다. 이는 동어반복에 가깝지만, 그 부분다양체로 가면 내용이 생긴다. $$\mathbb{CP}^n$$의 매끄러운 닫힌 복소 부분다양체 $$Y$$는 $$\mathcal{O}(1)\vert_Y$$를 양의 선다발로 물려받으므로 ([§Kähler 다양체, ⁋명제 9](/ko/math/complex_geometry/kahler_manifolds#prop9)), 다시 사영적이다. 곧 사영공간의 매끄러운 해석적 부분다양체는 전부 사영대수다양체이며, 이는 Chow 정리 ([정리 12](#thm12)) 의 한 특수경우이기도 하다.

</div>

대조적인 예가 복소토러스이다. 모든 복소토러스는 Kähler이지만 ([§Kähler 다양체, ⁋예시 7](/ko/math/complex_geometry/kahler_manifolds#ex7)), 사영적인 것은 그 가운데 일부뿐이다.

<div class="example" markdown="1">

<ins id="ex14">**예시 14 (복소토러스와 abelian variety)**</ins> 격자 $$\Lambda \subseteq \mathbb{C}^n$$에 의한 복소토러스 $$T = \mathbb{C}^n/\Lambda$$ ([§복소다양체, ⁋예시 7](/ko/math/complex_geometry/complex_manifolds#ex7))를 생각하자. $$T$$가 사영적이려면 [따름정리 11](#cor11)에 의해 정수 Kähler 류를 가져야 하는데, $$T$$ 위의 평행이동 불변 Kähler 형식은 $$\mathbb{C}^n$$ 위의 양의 정부호 Hermitian 형식 $$H$$로 주어지고, 그 류가 정수류인 것은 $$H$$의 허수부 $$\Img H$$가 격자 $$\Lambda$$ 위에서 정수값을 갖고 $$\Lambda \times \Lambda$$ 위에서 정수 반대칭형식을 이루는 것과 동치이다. 이 조건이 *Riemann bilinear relations<sub>Riemann 쌍선형 관계</sub>*이다. Riemann 관계를 만족하는 양의 정부호 $$H$$가 존재할 때, 그리고 오직 그때 $$T$$는 사영적이며 이러한 $$T$$를 *abelian variety<sub>아벨 다양체</sub>*라 한다.

차원 $$n = 1$$에서는 모든 격자가 Riemann 관계를 만족하므로 모든 복소토러스가 타원곡선으로 사영적이다. 그러나 $$n \geq 2$$에서는 일반적인 격자 $$\Lambda$$가 Riemann 관계를 만족하는 $$H$$를 전혀 허용하지 않는다. 정수 반대칭형식과 양정치 Hermitian 형식을 동시에 맞추는 것은 격자의 주기에 대한 비자명한 산술적 제약이며, 일반적인 $$\Lambda$$는 이를 어긴다. 따라서 *generic 복소토러스*는 양의 선다발을 갖지 않아 사영적이지 않다. 이것이 Kähler이면서 사영적이지 않은 콤팩트 복소다양체의 가장 표준적인 예이며, Kodaira 판정이 빈 정리가 아님을 보여 준다.

</div>

마지막으로 사영성과 비사영성이 한 부류 안에서 갈리는 더 미묘한 예가 K3 곡면이다.

<div class="example" markdown="1">

<ins id="ex15">**예시 15 (K3 곡면)**</ins> 복소차원 $$2$$의 콤팩트 복소다양체 가운데 표준선다발이 자명하고($$K_X \cong \mathcal{O}_X$$) 첫 Betti 수가 $$0$$인 단일연결 곡면을 *K3 surface<sub>K3 곡면</sub>*라 한다 (사영적인 경우의 정의는 [\[대수다양체\] §K3 Surfaces, ⁋정의 1](/ko/math/algebraic_varieties/k3_surfaces#def1)). 모든 K3 곡면은 Kähler 다양체이지만, 모든 K3 곡면이 사영적인 것은 아니다. K3 곡면 위에는 $$H^2(X, \mathbb{Z})$$ 안에 $$(1,1)$$-류로 놓이는 정수류, 곧 Néron–Severi 격자가 있고, 그 안에 양의 자기교차를 갖는 류가 존재할 때 [따름정리 11](#cor11)에 의해 그 곡면이 사영적이 된다. Generic K3 곡면은 $$H^{1,1}$$과 $$H^2(X, \mathbb{Z})$$의 교집합이 자명하여 정수 Kähler 류를 갖지 못해 비사영이고, 주기를 특수화하면 정수 $$(1,1)$$-류가 나타나 사영 K3 곡면이 된다. 곧 K3 곡면의 사영성은 주기에 대한 가산개 조건으로, 사영 K3는 비사영 K3로 이루어진 연속체 안에서 조밀하지만 측도 $$0$$인 부분을 이룬다. 이는 Kodaira 판정이 한 변형족 안에서 사영성을 정밀하게 가려내는 방식을 보여 주는 예이다.

</div>

세 예시는 Kodaira 정리의 내용을 단계적으로 드러낸다. $$\mathbb{CP}^n$$과 그 부분다양체는 정리의 충분성을 자명하게 실현하고, 복소토러스는 Kähler와 사영 사이의 진정한 간격을 양의 선다발의 부재로 설명하며, K3 곡면은 그 간격이 한 다양체족 안에서 주기의 산술로 갈린다는 것을 보여 준다. 이들을 관통하는 원리는 한결같다. 콤팩트 복소다양체의 사영성은 곡률이 Kähler가 되는 양의 선다발, 동치로 정수 Kähler 류의 존재로 완전히 결정된다.

---

**참고문헌**

**[Griffiths–Harris]** P. Griffiths and J. Harris, *Principles of Algebraic Geometry*, Wiley, 1978.

**[Huybrechts]** D. Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005.

**[Wells]** R. O. Wells, *Differential Analysis on Complex Manifolds*, 3rd ed., Springer, 2008.

**[Demailly]** J.-P. Demailly, *Complex Analytic and Differential Geometry*, 2012.

**[Voisin]** C. Voisin, *Hodge Theory and Complex Algebraic Geometry I*, Cambridge University Press, 2002.
