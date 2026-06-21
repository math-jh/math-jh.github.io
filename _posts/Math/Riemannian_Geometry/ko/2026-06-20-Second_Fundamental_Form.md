---
title: "제2기본형식"
description: "주변 Riemannian manifold에 매장된 submanifold 위에서, 주변 공변미분의 접-법 분해로부터 Gauss 공식과 제2기본형식을 도입한다. Weingarten 사상과 Weingarten 방정식, 내재적 곡률과 주변 곡률을 잇는 Gauss 방정식, 평균곡률을 다루고, 측지선과 가속도의 관계 및 구면의 제2기본형식 계산으로 마무리한다."
excerpt: "주변 공변미분의 법성분으로서의 제2기본형식과 Gauss 방정식"

categories: [Math / Riemannian Geometry]
permalink: /ko/math/riemannian_geometry/second_fundamental_form
sidebar: 
    nav: "riemannian_geometry-ko"

date: 2026-06-20
weight: 7
published: false

---

[§리만 계량, §§Normal bundle](/ko/math/riemannian_geometry/Riemannian_metric#normal-bundle)에서 우리는 Riemannian manifold $$(\bar M, \bar g)$$의 submanifold $$M$$ 위에 제한 metric $$g = \iota^\ast \bar g$$를 주고, 각 점에서 접공간 $$T_p M$$의 직교여공간으로 normal bundle $$NM$$을 정의했다. 이 글에서는 이러한 매장이 $$M$$에 부여하는 *외재적<sub>extrinsic</sub>* 기하를 다룬다. 핵심 도구는 주변 공간 $$\bar M$$의 Levi-Civita 접속 $$\bar\nabla$$를 접성분과 법성분으로 쪼개는 일이며, 그 법성분이 곧 *제2기본형식*이다. 이를 통해 우리는 $$M$$의 내재적 곡률과 $$\bar M$$의 곡률을 잇는 Gauss 방정식을 얻고, [§측지선, ⁋예시 9](/ko/math/riemannian_geometry/geodesics#ex9)에서 구면의 대원이 측지선임을 보일 때 사용한 "주변 가속도를 접공간으로 정사영"하는 논증의 일반적 배경을 마련한다.

이 글 전체에서 $$M \subseteq \bar M$$은 매장된 submanifold이고, $$\bar g$$는 $$\bar M$$의 Riemannian metric, $$g = \iota^\ast \bar g$$는 그 제한이며, $$\bar\nabla, \nabla$$는 각각 $$(\bar M, \bar g)$$와 $$(M, g)$$의 Levi-Civita 접속을 가리킨다. 또 $$X, Y, Z, W$$ 등은 $$M$$ 위의 vector field를 가리키며, 필요할 때 이를 $$\bar M$$ 위로 확장하여 $$\bar\nabla_X Y$$ 등을 계산한다. $$d\iota$$를 통한 동일시 $$T_p M \subseteq T_p \bar M$$은 따로 명시하지 않고 사용한다.

## 접-법 분해와 Gauss 공식

각 점 $$p \in M$$에서 $$T_p \bar M$$은 직교분해 $$T_p \bar M = T_p M \oplus N_p M$$을 갖는다. 따라서 임의의 $$v \in T_p \bar M$$은 접성분 $$v^\top \in T_p M$$과 법성분 $$v^\perp \in N_p M$$의 합으로 유일하게 쓰이며, 이 분해는 $$p$$에 매끄럽게 의존한다. 우리는 이 점별 분해를 $$M$$ 위의 vector field에 적용한다. $$M$$ 위의 두 vector field $$X, Y$$를 $$\bar M$$ 위로 확장하여 $$\bar\nabla_X Y$$를 계산하면, 이는 $$M$$의 점에서 $$T \bar M$$의 단면이 되고, 이를 접성분과 법성분으로 나눌 수 있다.

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1**</ins> $$M$$ 위의 vector field $$X, Y$$에 대해, $$M$$의 점에서 평가한 $$\bar\nabla_X Y$$의 접성분 $$(\bar\nabla_X Y)^\top$$은 $$X, Y$$를 $$\bar M$$ 위로 확장하는 방식에 의존하지 않으며, 제한 metric $$g$$의 Levi-Civita 접속 $$\nabla$$와 일치한다. 즉

$$\nabla_X Y = (\bar\nabla_X Y)^\top$$

이 성립한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

함수 $$\nabla' : \mathfrak{X}(M) \times \mathfrak{X}(M) \to \mathfrak{X}(M)$$을 $$\nabla'_X Y := (\bar\nabla_X Y)^\top$$로 정의하자. 먼저 이것이 well-defined임을, 즉 확장에 무관함을 보인다. [§접속, ⁋명제 2](/ko/math/riemannian_geometry/connection#prop2)에 의해 $$(\bar\nabla_X Y)_p$$는 $$X_p \in T_p M \subseteq T_p \bar M$$과 $$p$$ 근방에서의 $$Y$$의 값에만 의존하는데, $$Y$$를 $$M$$ 위에서만 알아도 $$X_p \in T_p M$$ 방향의 미분은 $$M$$ 위에서의 $$Y$$의 값만으로 결정된다. 따라서 $$(\bar\nabla_X Y)_p$$는 확장에 무관하며 그 접성분도 그러하다.

이제 $$\nabla'$$이 $$g$$의 Levi-Civita 접속임을 [§레비-치비타 접속, ⁋정리 4](/ko/math/riemannian_geometry/Levi-Civita_connection#thm4)의 유일성을 이용해 보인다. 먼저 $$\nabla'$$이 $$TM$$ 위의 connection임을 확인하자. 접성분을 취하는 사상 $$(\cdot)^\top : T\bar M\vert_M \to TM$$은 fiber별 선형사상이므로, $$\bar\nabla$$이 첫 인수에 대해 $$C^\infty(M)$$-linear, 둘째 인수에 대해 $$\mathbb{R}$$-linear이고 라이프니츠 법칙 $$\bar\nabla_X(fY) = f \bar\nabla_X Y + (Xf) Y$$를 만족하는 데서, $$\nabla'$$도 같은 성질을 물려받는다. 라이프니츠 법칙의 경우 $$(\bar\nabla_X(fY))^\top = (f\bar\nabla_X Y + (Xf)Y)^\top = f(\bar\nabla_X Y)^\top + (Xf) Y^\top = f \nabla'_X Y + (Xf) Y$$인데, 마지막에서 $$Y$$가 $$M$$에 접하므로 $$Y^\top = Y$$임을 썼다. 따라서 $$\nabla'$$은 connection이다.

다음으로 $$\nabla'$$이 $$g$$와 compatible이다. $$\bar\nabla$$이 $$\bar g$$와 compatible이므로 $$M$$에 접하는 $$X, Y, Z$$에 대해

$$X\langle Y, Z\rangle_{\bar g} = \langle \bar\nabla_X Y, Z\rangle_{\bar g} + \langle Y, \bar\nabla_X Z\rangle_{\bar g}$$

이고, $$Z$$가 $$M$$에 접하므로 $$\langle \bar\nabla_X Y, Z\rangle_{\bar g} = \langle (\bar\nabla_X Y)^\top, Z\rangle_{\bar g} = \langle \nabla'_X Y, Z\rangle_g$$이며 (법성분은 $$Z$$와 직교한다), 마찬가지로 $$\langle Y, \bar\nabla_X Z\rangle_{\bar g} = \langle Y, \nabla'_X Z\rangle_g$$이다. $$M$$ 위에서 $$\langle Y, Z\rangle_{\bar g} = \langle Y, Z\rangle_g$$이므로 $$X\langle Y, Z\rangle_g = \langle \nabla'_X Y, Z\rangle_g + \langle Y, \nabla'_X Z\rangle_g$$, 즉 $$\nabla'$$은 $$g$$와 compatible이다 ([§레비-치비타 접속, ⁋정의 1](/ko/math/riemannian_geometry/Levi-Civita_connection#def1)).

마지막으로 $$\nabla'$$은 torsion-free이다. $$\bar\nabla$$이 torsion-free이므로 $$\bar\nabla_X Y - \bar\nabla_Y X = [X, Y]$$인데, $$X, Y$$가 $$M$$에 접하면 그 Lie bracket $$[X, Y]$$도 $$M$$에 접하므로 (submanifold의 접 vector field들은 bracket에 닫혀 있다) 이미 접 vector이다. 양변의 접성분을 취하면

$$\nabla'_X Y - \nabla'_Y X = (\bar\nabla_X Y)^\top - (\bar\nabla_Y X)^\top = ([X, Y])^\top = [X, Y]$$

가 되어 $$\nabla'$$의 torsion이 소멸한다 ([§레비-치비타 접속, ⁋정의 3](/ko/math/riemannian_geometry/Levi-Civita_connection#def3)). 따라서 $$\nabla'$$은 $$g$$와 compatible한 torsion-free connection이고, 리만 기하학의 기본 정리의 유일성에 의해 $$\nabla' = \nabla$$이다.

</details>

[명제 1](#prop1)은 제한 metric의 내재적 접속 $$\nabla$$이 주변 접속 $$\bar\nabla$$의 접성분으로 깔끔하게 회복됨을 말해 준다. 그렇다면 남는 것은 법성분이며, 이것이 우리가 다룰 새로운 자료이다. 주변 미분 $$\bar\nabla_X Y$$을 접성분과 법성분으로 쪼갠

$$\bar\nabla_X Y = (\bar\nabla_X Y)^\top + (\bar\nabla_X Y)^\perp = \nabla_X Y + (\bar\nabla_X Y)^\perp$$

이라는 분해를 *Gauss 공식<sub>Gauss formula</sub>*이라 부른다. 그 법성분에 이름을 붙인다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 매장된 submanifold $$M \subseteq \bar M$$에 대해, $$M$$ 위의 vector field $$X, Y$$의 *second fundamental form<sub>제2기본형식</sub>* $$\mathrm{II}(X, Y)$$는 주변 미분의 법성분

$$\mathrm{II}(X, Y) := (\bar\nabla_X Y)^\perp = \bar\nabla_X Y - \nabla_X Y$$

로 정의된다. 이는 $$M$$ 위의 normal bundle $$NM$$의 단면에 값을 갖는다.

</div>

기호 $$\mathrm{II}$$는 고전적인 곡면론에서 *제1기본형식*이라 부르는 제한 metric $$g$$에 이어 등장하는 두 번째 자료라는 데서 비롯한 표기이다. Gauss 공식은 이제 $$\bar\nabla_X Y = \nabla_X Y + \mathrm{II}(X, Y)$$로 다시 적힌다. 정의에서 $$\mathrm{II}(X, Y)$$는 $$M$$ 위에서 *법선 방향*만을 측정하므로, $$M$$이 $$\bar M$$ 안에서 얼마나 휘어 있는지를 나타내는 외재적 양이다. 다음 명제는 이 자료가 실제로는 $$X, Y$$에 대해 점별로 결정되는 대칭 텐서임을 보인다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> [정의 2](#def2)의 제2기본형식 $$\mathrm{II}$$는 다음 성질을 갖는다.

1. $$\mathrm{II}$$는 두 인수 모두에 대해 $$C^\infty(M)$$-linear이다. 따라서 $$\mathrm{II}(X, Y)_p$$는 $$X_p, Y_p \in T_p M$$에만 의존하며, $$\mathrm{II}$$는 $$NM$$-값을 갖는 $$M$$ 위의 대칭 $$(0, 2)$$-tensor이다.
2. $$\mathrm{II}$$는 대칭이다. 즉 $$\mathrm{II}(X, Y) = \mathrm{II}(Y, X)$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

먼저 대칭성을 보인다. $$\bar\nabla$$과 $$\nabla$$이 모두 torsion-free이므로 $$\bar\nabla_X Y - \bar\nabla_Y X = [X, Y] = \nabla_X Y - \nabla_Y X$$이고, 따라서

$$\mathrm{II}(X, Y) - \mathrm{II}(Y, X) = (\bar\nabla_X Y - \nabla_X Y) - (\bar\nabla_Y X - \nabla_Y X) = (\bar\nabla_X Y - \bar\nabla_Y X) - (\nabla_X Y - \nabla_Y X) = [X, Y] - [X, Y] = 0$$

이다.

다음으로 $$C^\infty(M)$$-linearity를 보인다. 첫 인수에 대해서는 $$\bar\nabla$$과 $$\nabla$$이 모두 첫 인수에 $$C^\infty(M)$$-linear이므로 그 차인 $$\mathrm{II}$$도 그러하다. 둘째 인수에 대해서는, $$f \in C^\infty(M)$$에 대해 두 접속의 라이프니츠 법칙을 적용하면

$$\mathrm{II}(X, fY) = \bar\nabla_X(fY) - \nabla_X(fY) = \bigl(f\bar\nabla_X Y + (Xf) Y\bigr) - \bigl(f\nabla_X Y + (Xf) Y\bigr) = f(\bar\nabla_X Y - \nabla_X Y) = f\, \mathrm{II}(X, Y)$$

가 되어 $$(Xf) Y$$항이 상쇄된다. 따라서 둘째 인수에 대해서도 $$C^\infty(M)$$-linear이다. 두 인수 모두에 $$C^\infty(M)$$-linear이므로 텐서성 판정 (각 인수의 점별 의존성)에 의해 $$\mathrm{II}(X, Y)_p$$는 $$X_p, Y_p$$에만 의존하며, $$\mathrm{II}$$는 $$NM$$-값 대칭 $$(0, 2)$$-tensor이다.

</details>

[명제 3](#prop3)에서 $$\mathrm{II}$$가 텐서임이 중요하다. 정의에는 $$X, Y$$를 $$\bar M$$ 위로 확장하는 절차가 들어 있지만, 결과는 확장과 무관하게 $$T_p M$$의 두 vector $$X_p, Y_p$$에만 의존한다. 이로써 우리는 $$\mathrm{II}_p : T_p M \times T_p M \to N_p M$$을 각 점에서의 대칭 쌍선형사상으로 다룰 수 있다.

## Weingarten 사상

제2기본형식은 normal bundle에 값을 갖는다. 한 법벡터 방향을 고정하여 이를 접공간 위의 자기준동형사상으로 바꾸면 다루기가 편해진다. 이를 위해 법선 방향의 미분을 도입한다. $$M$$ 위의 법벡터장 $$N$$, 즉 $$NM$$의 단면과 접 vector field $$X$$에 대해 주변 미분 $$\bar\nabla_X N$$을 계산하면, 이는 다시 접성분과 법성분으로 쪼개진다. 그 접성분이 다음 사상을 준다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> $$M \subseteq \bar M$$의 점 $$p$$에서 법벡터 $$\nu \in N_p M$$이 주어졌다 하자. $$\nu$$를 $$p$$ 근방에서 매끄러운 법벡터장 $$N$$으로 확장할 때, 점 $$p$$에서의 *Weingarten 사상<sub>Weingarten map</sub>* 혹은 *shape operator* $$S_\nu : T_p M \to T_p M$$은 다음의 식

$$S_\nu(X) := -(\bar\nabla_X N)^\top$$

으로 정의된다.

</div>

부호 앞의 음수는 관례적 선택이며, 아래 [명제 5](#prop5)에서 보듯 $$S_\nu$$를 제2기본형식과 곧장 연결하기 위한 것이다. 정의가 확장 $$N$$에 무관하다는 사실은 그 명제의 증명에서 함께 확인된다. 다음 명제는 Weingarten 사상이 제2기본형식과 metric을 통해 짝지어진다는 *Weingarten 방정식*이다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5 (Weingarten 방정식)**</ins> 법벡터 $$\nu \in N_p M$$과 $$X, Y \in T_p M$$에 대해 다음의 식

$$\langle S_\nu(X), Y\rangle = \langle \mathrm{II}(X, Y), \nu\rangle$$

이 성립한다. 특히 좌변이 확장 $$N$$에 무관하므로 [정의 4](#def4)의 $$S_\nu$$는 well-defined이며, $$S_\nu$$는 $$T_p M$$ 위의 self-adjoint 선형사상이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$X, Y$$를 $$M$$ 위의 접 vector field로, $$N$$을 $$M$$ 근방의 법벡터장으로 잡자. $$Y$$가 $$M$$에 접하고 $$N$$이 법선이므로 $$\langle Y, N\rangle_{\bar g} = 0$$이 $$M$$ 위에서 항등적으로 성립한다. 양변을 $$X$$로 미분하고 $$\bar\nabla$$의 metric-compatibility를 적용하면

$$0 = X\langle Y, N\rangle_{\bar g} = \langle \bar\nabla_X Y, N\rangle_{\bar g} + \langle Y, \bar\nabla_X N\rangle_{\bar g}$$

를 얻는다. 첫 항에서 $$N$$이 법선이므로 $$\langle \bar\nabla_X Y, N\rangle_{\bar g} = \langle (\bar\nabla_X Y)^\perp, N\rangle_{\bar g} = \langle \mathrm{II}(X, Y), N\rangle_{\bar g}$$이고, 둘째 항에서 $$Y$$가 접하므로 $$\langle Y, \bar\nabla_X N\rangle_{\bar g} = \langle Y, (\bar\nabla_X N)^\top\rangle_{\bar g} = -\langle Y, S_\nu(X)\rangle_{\bar g}$$이다. 따라서

$$0 = \langle \mathrm{II}(X, Y), N\rangle_{\bar g} - \langle S_\nu(X), Y\rangle_{\bar g}$$

가 되어 점 $$p$$에서 $$\langle S_\nu(X), Y\rangle = \langle \mathrm{II}(X, Y), \nu\rangle$$를 얻는다. 우변은 확장 $$N$$을 전혀 포함하지 않으므로 좌변 $$\langle S_\nu(X), Y\rangle$$도 모든 $$Y$$에 대해 확장과 무관하며, 따라서 $$S_\nu(X)$$ 자체가 확장과 무관하게 결정된다. 끝으로 [명제 3](#prop3)의 대칭성으로부터 $$\langle S_\nu(X), Y\rangle = \langle \mathrm{II}(X, Y), \nu\rangle = \langle \mathrm{II}(Y, X), \nu\rangle = \langle S_\nu(Y), X\rangle$$이므로 $$S_\nu$$는 self-adjoint이다.

</details>

Weingarten 방정식은 제2기본형식 $$\mathrm{II}$$와 Weingarten 사상 $$S_\nu$$가 본질적으로 같은 자료의 두 표현임을 말해 준다. $$\mathrm{II}$$는 두 접 vector를 받아 법벡터를 내놓고, $$S_\nu$$는 법선 방향 $$\nu$$를 하나 고정한 뒤 접 vector를 받아 접 vector를 내놓는다. $$S_\nu$$가 self-adjoint이므로 직교대각화가 가능하며, 그 고윳값들을 $$\nu$$ 방향의 *principal curvature<sub>주곡률</sub>*, 고유 vector들이 펼치는 방향을 *principal direction<sub>주방향</sub>*이라 부른다. Codimension이 $$1$$인 hypersurface의 경우 각 점에서 법선 방향이 (부호를 빼면) 하나뿐이므로 $$S_\nu$$ 하나가 외재적 곡률 정보를 모두 담는다.

## Gauss 방정식

제2기본형식의 가장 중요한 귀결은 $$M$$의 내재적 곡률과 $$\bar M$$의 곡률 사이의 관계이다. [§리만 곡률, ⁋정의 2](/ko/math/riemannian_geometry/curvature#def2)에서 곡률 텐서를 $$R(X, Y) Z = \nabla_X \nabla_Y Z - \nabla_Y \nabla_X Z - \nabla_{[X, Y]} Z$$로 정의했음을 상기하자. $$\bar M$$의 곡률 텐서 $$\bar R$$도 같은 식으로 $$\bar\nabla$$으로부터 정의된다. 이 둘의 차이가 정확히 제2기본형식의 이차식으로 통제된다.

<div class="proposition" markdown="1">

<ins id="thm6">**정리 6 (Gauss 방정식)**</ins> 매장된 submanifold $$M \subseteq \bar M$$ 위의 접 vector field $$X, Y, Z, W$$에 대해 다음의 식

$$\langle \bar R(X, Y) Z, W\rangle = \langle R(X, Y) Z, W\rangle + \langle \mathrm{II}(X, Z), \mathrm{II}(Y, W)\rangle - \langle \mathrm{II}(Y, Z), \mathrm{II}(X, W)\rangle$$

이 성립한다. 여기서 $$R, \bar R$$은 각각 $$(M, g)$$와 $$(\bar M, \bar g)$$의 곡률 텐서이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

계산의 편의를 위해 점 $$p$$의 한 근방에서 $$[X, Y] = 0$$이 되도록 $$X, Y$$를 잡아도 일반성을 잃지 않는다. 실제로 곡률 텐서가 [§리만 곡률, ⁋명제 3](/ko/math/riemannian_geometry/curvature#prop3)에 의해 텐서이고 $$\mathrm{II}$$도 텐서이므로, 등식의 양변은 $$X_p, Y_p, Z_p, W_p$$에만 의존하며, 주어진 vector들을 좌표 vector field로 확장해 $$[X, Y] = 0$$이 되도록 할 수 있기 때문이다. 이때 $$R(X, Y)Z = \nabla_X \nabla_Y Z - \nabla_Y \nabla_X Z$$이고 $$\bar R(X, Y)Z = \bar\nabla_X \bar\nabla_Y Z - \bar\nabla_Y \bar\nabla_X Z$$이다.

Gauss 공식 $$\bar\nabla_Y Z = \nabla_Y Z + \mathrm{II}(Y, Z)$$을 한 번 적용하고, 여기에 다시 $$\bar\nabla_X$$을 적용하자. $$\nabla_Y Z$$은 $$M$$에 접하는 vector field이므로 Gauss 공식을 다시 적용할 수 있고, $$\mathrm{II}(Y, Z)$$은 법벡터장이므로 그 미분에는 Weingarten 사상이 등장한다. $$\mathrm{II}(Y, Z)$$을 법선 방향으로 보면 [정의 4](#def4)에 의해 $$\bar\nabla_X \mathrm{II}(Y, Z) = -S_{\mathrm{II}(Y, Z)}(X) + (\bar\nabla_X \mathrm{II}(Y, Z))^\perp$$이다. 이를 모아 쓰면

$$\bar\nabla_X \bar\nabla_Y Z = \nabla_X \nabla_Y Z + \mathrm{II}(X, \nabla_Y Z) - S_{\mathrm{II}(Y, Z)}(X) + (\bar\nabla_X \mathrm{II}(Y, Z))^\perp$$

이 된다. 이제 양변에 접 vector field $$W$$와의 내적을 취하면, $$W$$가 접하므로 법성분 $$\mathrm{II}(X, \nabla_Y Z)$$와 $$(\bar\nabla_X \mathrm{II}(Y, Z))^\perp$$는 사라지고

$$\langle \bar\nabla_X \bar\nabla_Y Z, W\rangle = \langle \nabla_X \nabla_Y Z, W\rangle - \langle S_{\mathrm{II}(Y, Z)}(X), W\rangle$$

만 남는다. Weingarten 방정식 [명제 5](#prop5)로 마지막 항을 $$\langle S_{\mathrm{II}(Y, Z)}(X), W\rangle = \langle \mathrm{II}(X, W), \mathrm{II}(Y, Z)\rangle$$로 바꾸면

$$\langle \bar\nabla_X \bar\nabla_Y Z, W\rangle = \langle \nabla_X \nabla_Y Z, W\rangle - \langle \mathrm{II}(X, W), \mathrm{II}(Y, Z)\rangle$$

이다. $$X$$와 $$Y$$의 역할을 바꾼 식을 빼면, $$[X, Y] = 0$$이므로

$$\begin{aligned}
\langle \bar R(X, Y) Z, W\rangle &= \langle \bar\nabla_X \bar\nabla_Y Z - \bar\nabla_Y \bar\nabla_X Z, W\rangle \\
&= \langle \nabla_X \nabla_Y Z - \nabla_Y \nabla_X Z, W\rangle - \langle \mathrm{II}(X, W), \mathrm{II}(Y, Z)\rangle + \langle \mathrm{II}(Y, W), \mathrm{II}(X, Z)\rangle \\
&= \langle R(X, Y) Z, W\rangle + \langle \mathrm{II}(X, Z), \mathrm{II}(Y, W)\rangle - \langle \mathrm{II}(Y, Z), \mathrm{II}(X, W)\rangle
\end{aligned}$$

을 얻는다.

</details>

Gauss 방정식은 $$M$$의 내재적 곡률 $$R$$이 주변 곡률 $$\bar R$$로부터 제2기본형식의 이차식만큼의 보정을 거쳐 결정됨을 말한다. 특히 주변 공간이 평탄한 경우, 즉 $$\bar M = \mathbb{R}^{n+1}$$이고 $$\bar R = 0$$인 경우에는 $$M$$의 모든 곡률이 순전히 제2기본형식으로부터 나온다. 이것이 Gauss의 *Theorema Egregium*의 일반적 형태로, 곡면의 Gauss 곡률이 주변 공간에 어떻게 매장되었는지가 아니라 제1기본형식만으로 결정되는 *내재적* 양이라는 사실의 고차원 일반화이다.

<div class="remark" markdown="1">

<ins id="rmk7">**참고 7**</ins> [§리만 곡률, ⁋명제 5](/ko/math/riemannian_geometry/curvature#prop5)에서 정의한 sectional curvature의 언어로 Gauss 방정식을 다시 읽으면 더 기하학적인 형태를 얻는다. $$M$$의 한 점에서 정규직교 vector $$X, Y \in T_p M$$이 펼치는 평면의 sectional curvature $$K(X, Y)$$와 같은 평면을 $$\bar M$$ 안에서 본 $$\bar K(X, Y)$$ 사이에

$$K(X, Y) = \bar K(X, Y) + \langle \mathrm{II}(X, X), \mathrm{II}(Y, Y)\rangle - \lvert \mathrm{II}(X, Y)\rvert^2$$

이 성립한다. 이는 [정리 6](#thm6)에 $$Z = Y, W = X$$를 대입하고 $$\langle R(X, Y) Y, X\rangle = K(X, Y)$$ ($$X, Y$$가 정규직교일 때)를 쓴 것이다.

</div>

## 평균곡률

제2기본형식은 점별로 대칭 쌍선형사상이므로, 그 trace를 취해 한 법벡터를 얻을 수 있다. 이는 $$M$$이 평균적으로 어느 법선 방향으로 휘어 있는지를 나타낸다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> $$\dim M = m$$인 매장된 submanifold $$M \subseteq \bar M$$의 점 $$p$$에서 $$T_p M$$의 정규직교기저 $$e_1, \ldots, e_m$$을 잡자. 점 $$p$$에서의 *mean curvature vector<sub>평균곡률 vector</sub>* $$H$$는 제2기본형식의 trace

$$H := \sum_{i=1}^m \mathrm{II}(e_i, e_i) \in N_p M$$

로 정의된다.

</div>

$$\mathrm{II}$$가 텐서이고 trace가 기저 선택에 무관하므로 $$H$$는 well-defined인 법벡터이다. 문헌에 따라 평균을 취해 $$\frac{1}{m} \sum_i \mathrm{II}(e_i, e_i)$$를 평균곡률로 정의하기도 하나, 우리는 trace 자체를 택한다. Hypersurface의 경우 법선 방향 $$\nu$$를 고정하면 $$H = (\operatorname{tr} S_\nu)\, \nu$$이며, $$\operatorname{tr} S_\nu$$는 주곡률들의 합이다. 평균곡률이 항등적으로 $$0$$인 submanifold를 *minimal submanifold<sub>극소 submanifold</sub>*라 부르는데, 이는 부피 범함수의 임계점이라는 변분적 의미를 가지며 비누막의 형상 등으로 나타난다.

## 측지선과의 관계

제2기본형식은 [§측지선, ⁋예시 9](/ko/math/riemannian_geometry/geodesics#ex9)에서 구면의 대원을 다룰 때 암묵적으로 사용한 "주변 가속도의 접성분"이라는 개념을 정확히 메운다. $$M$$ 위의 곡선 $$\gamma$$의 주변 가속도 $$\bar D_t \dot\gamma$$와 내재적 가속도 $$D_t \dot\gamma$$ 사이의 간격이 곧 제2기본형식이다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> 매장된 submanifold $$M \subseteq \bar M$$ 위의 곡선 $$\gamma : I \to M$$에 대해, $$\gamma$$를 $$\bar M$$의 곡선으로 본 주변 가속도 $$\bar D_t \dot\gamma$$는

$$\bar D_t \dot\gamma = D_t \dot\gamma + \mathrm{II}(\dot\gamma, \dot\gamma)$$

로 분해된다. 여기서 $$D_t, \bar D_t$$는 각각 $$\nabla, \bar\nabla$$이 $$\gamma$$를 따라 유도하는 covariant derivative이다. 따라서 $$\gamma$$가 $$M$$의 측지선인 것은 주변 가속도 $$\bar D_t \dot\gamma$$가 매 점에서 $$M$$에 법선인 것과 동치이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

[명제 1](#prop1)과 [정의 2](#def2)는 vector field에 대한 Gauss 공식 $$\bar\nabla_X Y = \nabla_X Y + \mathrm{II}(X, Y)$$를 준다. 이 공식은 곡선 $$\gamma$$를 따른 covariant derivative로 그대로 옮겨진다. 즉 곡선 $$\gamma$$ 위의 접 vector field $$V$$에 대해 $$\bar D_t V = D_t V + \mathrm{II}(\dot\gamma, V)$$가 성립하는데, 이는 양변이 $$\bar M$$의 접속과 $$M$$의 접속을 곡선을 따라 표현한 것이며 좌표 계산으로 $$\mathrm{II}$$가 $$\dot\gamma$$와 $$V$$의 점별 값에만 의존한다는 [명제 3](#prop3)을 적용해 얻어진다. 특히 $$V = \dot\gamma$$로 두면

$$\bar D_t \dot\gamma = D_t \dot\gamma + \mathrm{II}(\dot\gamma, \dot\gamma)$$

이며, 우변에서 $$D_t \dot\gamma$$는 $$M$$에 접하고 $$\mathrm{II}(\dot\gamma, \dot\gamma)$$는 법선이므로 이것이 정확히 $$\bar D_t \dot\gamma$$의 접-법 분해이다.

$$\gamma$$가 $$M$$의 측지선인 것은 [§측지선, ⁋정의 4](/ko/math/riemannian_geometry/geodesics#def4)에 의해 $$D_t \dot\gamma = 0$$인 것, 즉 위 분해의 접성분이 소멸하는 것과 동치이다. 접성분이 소멸하는 것은 $$\bar D_t \dot\gamma = \mathrm{II}(\dot\gamma, \dot\gamma)$$가 법선인 것과 동치이므로, $$\gamma$$가 측지선인 것과 주변 가속도가 매 점에서 법선인 것이 동치이다.

</details>

[명제 9](#prop9)는 측지선의 외재적 특징을 분명히 한다. $$M$$의 측지선이란 "$$M$$ 안에서는 가속도가 없으나 $$\bar M$$ 안에서는 $$M$$을 벗어나지 않으려 법선 방향으로만 휘는" 곡선이다. $$\bar M = \mathbb{R}^{n+1}$$인 경우 주변 가속도 $$\bar D_t \dot\gamma$$는 보통의 이계 도함수 $$\ddot\gamma$$이므로, $$\gamma$$가 측지선인 것은 $$\ddot\gamma$$가 매 점에서 $$M$$에 법선인 것과 같다. 이것이 [§측지선, ⁋예시 9](/ko/math/riemannian_geometry/geodesics#ex9)에서 사용한 판정법이다.

이 관점을 구면에 적용해 제2기본형식을 명시적으로 계산하자.

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> 단위 구면 $$S^n \subseteq \mathbb{R}^{n+1}$$에 표준 매장으로 유도되는 round metric을 주자. 점 $$p \in S^n$$에서의 바깥 단위 법벡터는 위치벡터 $$\nu = p$$ 자신이다. 우리는 $$S^n$$의 제2기본형식이

$$\mathrm{II}(X, Y) = -\langle X, Y\rangle\, \nu$$

임을 보인다. 점 $$p$$를 지나는 접 vector $$X, Y \in T_p S^n$$을 잡고, $$\nu(q) = q$$를 $$\mathbb{R}^{n+1}$$ 전체에서의 법벡터장으로 확장하자 (단위 구면 위에서 $$\lvert q\rvert = 1$$이므로 이 확장은 $$S^n$$ 위에서 단위 법벡터장이다). 평탄한 $$\mathbb{R}^{n+1}$$의 Levi-Civita 접속은 [§레비-치비타 접속, ⁋예시 7](/ko/math/riemannian_geometry/Levi-Civita_connection#ex7)에 의해 성분별 미분이므로, $$\nu(q) = q = (q^1, \ldots, q^{n+1})$$의 $$X$$ 방향 미분은

$$\bar\nabla_X \nu = X$$

이다 ($$q^i$$의 미분이 $$X$$의 $$i$$번째 성분이다). 이 vector $$X$$는 $$T_p S^n$$에 접하므로 그 접성분은 $$X$$ 자신이고, 따라서 Weingarten 사상은

$$S_\nu(X) = -(\bar\nabla_X \nu)^\top = -X$$

이다. 이제 Weingarten 방정식 [명제 5](#prop5)에 의해 임의의 $$Y \in T_p S^n$$에 대해

$$\langle \mathrm{II}(X, Y), \nu\rangle = \langle S_\nu(X), Y\rangle = \langle -X, Y\rangle = -\langle X, Y\rangle$$

이다. $$\mathrm{II}(X, Y)$$는 법선이고 $$\nu$$가 단위 법벡터로 normal bundle의 fiber $$N_p S^n$$을 한 줄로 펼치므로, 위 식은 $$\mathrm{II}(X, Y) = -\langle X, Y\rangle\, \nu$$를 준다.

이로부터 곡선의 주변 가속도가 [명제 9](#prop9)를 통해 곧장 회복된다. 단위 속력 곡선 $$\gamma$$에 대해 $$\mathrm{II}(\dot\gamma, \dot\gamma) = -\langle \dot\gamma, \dot\gamma\rangle\, \nu = -\nu = -\gamma$$이므로, $$\gamma$$가 측지선이면 $$\bar D_t \dot\gamma = \ddot\gamma = \mathrm{II}(\dot\gamma, \dot\gamma) = -\gamma$$, 즉 [§측지선, ⁋예시 9](/ko/math/riemannian_geometry/geodesics#ex9)에서 대원에 대해 직접 계산한 $$\ddot\gamma = -\gamma$$를 다시 얻는다. 또한 평균곡률은 $$T_p S^n$$의 정규직교기저 $$e_1, \ldots, e_n$$에 대해 $$H = \sum_{i=1}^n \mathrm{II}(e_i, e_i) = -\sum_{i=1}^n \langle e_i, e_i\rangle\, \nu = -n\, \nu$$이므로 $$S^n$$은 극소 submanifold가 아니다.

</div>

마지막으로 Gauss 방정식 [정리 6](#thm6)을 구면에 적용하면 그 곡률이 회복된다. $$\bar M = \mathbb{R}^{n+1}$$이 평탄하여 $$\bar R = 0$$이므로, 정규직교 $$X, Y \in T_p S^n$$에 대해 [참고 7](#rmk7)의 식은

$$K(X, Y) = 0 + \langle \mathrm{II}(X, X), \mathrm{II}(Y, Y)\rangle - \lvert \mathrm{II}(X, Y)\rvert^2 = \langle -\langle X, X\rangle \nu, -\langle Y, Y\rangle \nu\rangle - \lvert -\langle X, Y\rangle \nu\rvert^2 = 1 \cdot 1 - 0 = 1$$

이 되어, 단위 구면 $$S^n$$의 모든 sectional curvature가 $$+1$$임을 외재적 계산만으로 확인한다. 여기서 $$\langle X, X\rangle = \langle Y, Y\rangle = 1$$, $$\langle X, Y\rangle = 0$$, $$\lvert \nu\rvert = 1$$을 사용했다.

---

**참고문헌**

**[Lee]** John M. Lee, *Introduction to Riemannian Manifolds*, Graduate Texts in Mathematics, Springer, 2019.

**[dC]** Manfredo P. do Carmo, *Riemannian Geometry*, Birkhäuser, 1992.

---
