---
title: "등각사상과 Möbius 변환"
description: "정칙이고 도함수가 0이 아닌 사상이 각과 방향을 보존하는 등각사상임을 밝히고, 확장복소평면의 자기동형군을 이루는 Möbius 변환을 다룬다. 원-직선의 보존, 교차비의 불변성, 세 점을 세 점으로 보내는 유일성을 증명하고, 단위원판의 자기동형사상을 Schwarz 보조정리로 분류한 뒤 Cayley 변환으로 상반평면과 잇는다."
excerpt: "등각사상, Möbius 변환, PSL(2,ℂ), 교차비, 원-직선 보존, 단위원판 자기동형, Schwarz–Pick, Cayley 변환"

categories: [Math / Complex Analysis]
permalink: /ko/math/complex_analysis/conformal_maps
sidebar: 
    nav: "complex_analysis-ko"

date: 2026-06-21
weight: 11

published: false
---

정칙함수의 미분이 한 점에서 평면을 회전·확대하는 닮음변환이라는 사실은 ([§정칙함수, ⁋정리 5](/ko/math/complex_analysis/holomorphic_functions#thm5)) 이미 정칙성의 대수적 핵심으로 드러난 바 있다. 회전·확대는 길이의 비를 바꿀 수는 있어도 두 방향이 이루는 각은 건드리지 못하므로, 도함수가 $$0$$이 아닌 정칙함수는 곡선들이 만나는 각을 크기와 방향까지 보존한다. 이렇게 각을 보존하는 사상을 등각사상이라 하며, 복소해석학을 평면기하의 변환이론으로 읽는 관점이 여기서 시작된다. 이 글에서는 먼저 정칙성과 등각성이 본질적으로 같은 조건임을 밝히고, 가장 단순하면서도 가장 풍부한 등각사상의 모임인 Möbius 변환을 다룬다. Möbius 변환은 확장복소평면 ([§복소수와 복소평면, ⁋정의 13](/ko/math/complex_analysis/complex_numbers#def13)) 전체의 정칙 자기동형사상을 이루며, 원과 직선을 원과 직선으로 보내고 교차비라는 양을 불변으로 남긴다. 끝으로 이를 단위원판과 상반평면의 자기동형사상을 분류하는 데 적용한다.

## 등각성

곡선이 한 점에서 이루는 각이라는 개념부터 정확히 한다. 점 $$z_0$$을 지나는 매끄러운 곡선 $$\gamma(t)$$ ($$\gamma(t_0) = z_0$$, $$\gamma'(t_0) \neq 0$$) 의 그 점에서의 접벡터는 복소수 $$\gamma'(t_0)$$이고, 그 편각 $$\arg \gamma'(t_0)$$이 곡선이 그 점에서 향하는 방향을 준다. 두 곡선 $$\gamma_1, \gamma_2$$이 $$z_0$$에서 이루는 각은 두 접벡터의 편각의 차 $$\arg \gamma_2'(t_0) - \arg \gamma_1'(t_0)$$로 정의되며, 부호까지 포함한 이 차가 방향이 매겨진 각이다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 열린집합 $$\Omega \subseteq \mathbb{C}$$ 위의 사상 $$f : \Omega \to \mathbb{C}$$가 점 $$z_0$$에서 *conformal<sub>등각</sub>*하다는 것은, $$z_0$$을 지나는 임의의 두 매끄러운 곡선이 $$z_0$$에서 이루는 (방향이 매겨진) 각이 그 상곡선들이 $$f(z_0)$$에서 이루는 각과 같은 것을 뜻한다. $$f$$가 $$\Omega$$의 모든 점에서 등각하면 $$f$$를 $$\Omega$$ 위의 *등각사상<sub>conformal map</sub>*이라 한다.

</div>

등각성은 각의 크기뿐 아니라 회전의 방향까지 보존할 것을 요구한다는 점이 핵심이다. 가령 켤레사상 $$z \mapsto \bar z$$는 모든 각의 크기를 보존하지만 방향을 뒤집으므로 (반사이므로) 위의 정의에서는 등각으로 치지 않는다. 이 방향성의 요구가 정칙성과 정확히 맞물리며, 다음 명제가 그 동치를 정식으로 적는다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> $$\Omega \subseteq \mathbb{C}$$가 열려 있고 $$f : \Omega \to \mathbb{C}$$가 $$z_0$$에서 복소미분가능하다고 하자. 그러면 $$f$$가 $$z_0$$에서 등각인 것은 $$f'(z_0) \neq 0$$인 것과 동치이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

먼저 $$f'(z_0) \neq 0$$이라 하자. $$z_0$$을 지나는 매끄러운 곡선 $$\gamma(t)$$ ($$\gamma(t_0) = z_0$$, $$\gamma'(t_0) \neq 0$$) 에 대하여 상곡선 $$(f \circ \gamma)(t) = f(\gamma(t))$$의 접벡터는 연쇄법칙 ([§정칙함수, ⁋명제 3](/ko/math/complex_analysis/holomorphic_functions#prop3)) 에 의해

$$(f \circ \gamma)'(t_0) = f'(z_0)\,\gamma'(t_0)$$

이다. $$f'(z_0) \neq 0$$이고 $$\gamma'(t_0) \neq 0$$이므로 이 접벡터도 $$0$$이 아니고, 그 편각은

$$\arg (f \circ \gamma)'(t_0) = \arg f'(z_0) + \arg \gamma'(t_0) \pmod{2\pi}$$

이다 ([§복소수와 복소평면, ⁋명제 6](/ko/math/complex_analysis/complex_numbers#prop6)). 곧 상곡선의 접벡터의 편각은 원곡선의 접벡터의 편각에 일정한 양 $$\arg f'(z_0)$$을 더한 것이다. 두 곡선 $$\gamma_1, \gamma_2$$에 대해 이 덧셈이 똑같이 일어나므로, 편각의 차

$$\arg (f \circ \gamma_2)'(t_0) - \arg (f \circ \gamma_1)'(t_0) = \arg \gamma_2'(t_0) - \arg \gamma_1'(t_0)$$

이 보존된다. 따라서 $$f$$는 $$z_0$$에서 방향이 매겨진 각을 보존하여 등각이다.

역으로 $$f'(z_0) = 0$$이라 하자. 그러면 위의 접벡터 공식에서 모든 매끄러운 곡선에 대해 $$(f \circ \gamma)'(t_0) = f'(z_0)\gamma'(t_0) = 0$$이 되어, 상곡선의 일차 접벡터가 소멸한다. 이때 상곡선이 $$f(z_0)$$에서 향하는 방향은 일차항이 아니라 처음으로 살아남는 고차항으로 결정되는데, 가령 $$f(z) = z^m$$ ($$m \geq 2$$) 을 $$z_0 = 0$$에서 보면 $$\arg f(z) = m \arg z$$이므로 원점에서 만나는 두 방향이 이루는 각이 $$f$$에 의해 $$m$$배로 늘어난다. 따라서 각이 보존되지 않아 $$f$$는 $$z_0$$에서 등각이 아니다.

</details>

명제 2는 등각성이라는 기하적 성질이 "정칙이고 도함수가 $$0$$이 아니다"라는 해석적 조건과 완전히 같음을 말한다. 도함수가 소멸하는 점, 곧 $$f'(z_0) = 0$$인 점은 *임계점<sub>critical point</sub>*이라 부르며, 그 점에서는 위수에 따라 각이 정수배로 확대되어 등각성이 깨진다. 영역 전체에서 도함수가 결코 $$0$$이 되지 않는 정칙함수는 따라서 각 점에서 무한소적으로 닮음변환처럼 행동하며, 작은 도형을 형태를 유지한 채 회전·확대해 옮긴다. 정칙인 전단사사상은 항상 이런 등각사상이 되는데, 이는 단엽 정칙함수의 도함수가 어디서도 $$0$$이 아니라는 사실의 귀결이다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> $$\Omega \subseteq \mathbb{C}$$가 열려 있고 $$f : \Omega \to \mathbb{C}$$가 정칙인 단사사상이라 하자. 그러면 $$\Omega$$의 모든 점에서 $$f'(z) \neq 0$$이고, 따라서 $$f$$는 $$\Omega$$ 위의 등각사상이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

어떤 $$z_0 \in \Omega$$에서 $$f'(z_0) = 0$$이라 가정하고 모순을 이끈다. $$w_0 = f(z_0)$$이라 두면 함수 $$g(z) = f(z) - w_0$$은 $$z_0$$에서 영점을 가지는데, $$g'(z_0) = f'(z_0) = 0$$이므로 그 영점의 위수 $$m$$은 $$m \geq 2$$이다 ([§영점과 일치정리, ⁋명제 2](/ko/math/complex_analysis/zeros_and_identity_theorem#prop2)의 인수분해에서 첫 비영 계수가 $$m \geq 2$$차이므로). 한편 비상수 정칙함수가 위수 $$m$$인 영점 근방에서 국소적으로 $$m$$겹 덮개처럼 행동한다는 사실에 의하면, $$w_0$$에 충분히 가까운 $$0$$이 아닌 모든 값 $$w$$에 대해 방정식 $$g(z) = w - w_0$$, 곧 $$f(z) = w$$이 $$z_0$$의 작은 구멍낸 근방 안에서 서로 다른 $$m$$개의 해를 가진다. $$m \geq 2$$이므로 이는 $$z_0$$ 근방에서 $$f$$가 같은 값을 두 번 이상 취함을 뜻하여 $$f$$의 단사성에 어긋난다. 따라서 모든 점에서 $$f'(z) \neq 0$$이고, 명제 2에 의해 $$f$$는 등각사상이다.

</details>

명제 3은 위수 $$m$$인 영점 근방에서 정칙함수가 $$m$$겹으로 값을 취한다는 국소적 사상정리를 이용한다. 이 사실 자체는 영점의 위수와 편각원리에서 따라 나오며, 비상수 정칙함수가 열린사상이라는 명제와 같은 뿌리를 가진다. 명제 3이 말하는 바는, 정칙인 전단사사상이 곧 등각동형사상이라는 것이다. 두 영역 사이의 정칙 전단사사상의 존재 여부를 묻는 등각동치 문제가 복소해석학의 한 중심 주제가 되는 까닭이 여기에 있다. 이제 그러한 사상의 가장 기본적인 공급원을 살핀다.

## Möbius 변환

가장 단순한 등각사상은 일차식의 비로 적히는 사상이다. 이들은 평면 전체가 아니라 확장복소평면 $$\widehat{\mathbb{C}}$$ ([§복소수와 복소평면, ⁋정의 13](/ko/math/complex_analysis/complex_numbers#def13)) 의 자기동형사상으로 보아야 그 구조가 온전히 드러난다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> 복소수 $$a, b, c, d$$가 $$ad - bc \neq 0$$을 만족할 때, 사상

$$T(z) = \frac{az + b}{cz + d}$$

을 *Möbius transformation<sub>뫼비우스 변환</sub>* 혹은 *일차분수변환<sub>linear fractional transformation</sub>*이라 한다. 이를 $$\widehat{\mathbb{C}}$$ 위의 사상으로 보아, $$c \neq 0$$이면 $$T(-d/c) = \infty$$, $$T(\infty) = a/c$$로, $$c = 0$$이면 $$T(\infty) = \infty$$로 약속한다.

</div>

조건 $$ad - bc \neq 0$$은 분자와 분모가 상수배로 같아져 $$T$$가 상수사상으로 퇴화하는 것을 막는다. 실제로 $$ad - bc = 0$$이면 $$(a, b)$$와 $$(c, d)$$가 비례하여 $$T$$가 정의역 전체에서 한 값으로 일정해진다. 미분하면

$$T'(z) = \frac{a(cz + d) - c(az + b)}{(cz + d)^2} = \frac{ad - bc}{(cz + d)^2}$$

이므로, $$ad - bc \neq 0$$인 한 $$T'$$는 분모가 정의되는 모든 점에서 $$0$$이 아니다. 따라서 Möbius 변환은 그 정칙영역에서 명제 2에 의해 등각사상이다. $$\infty$$를 포함한 거동까지 합쳐 보면 Möbius 변환은 $$\widehat{\mathbb{C}}$$ 전체의 자기동형사상이 되며, 이들이 군을 이룸을 행렬과의 대응으로 가장 깔끔하게 본다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> Möbius 변환 전체의 모임은 사상의 합성에 대하여 군을 이룬다. 행렬 $$\begin{pmatrix} a & b \\ c & d \end{pmatrix} \in \mathrm{GL}(2, \mathbb{C})$$에 Möbius 변환 $$z \mapsto (az+b)/(cz+d)$$를 대응시키는 사상은 군의 준동형사상이며, 그 핵은 $$0$$이 아닌 스칼라배의 항등행렬들 $$\{\lambda I : \lambda \in \mathbb{C}^\times\}$$이다. 따라서 Möbius 변환군은

$$\mathrm{PGL}(2, \mathbb{C}) = \mathrm{GL}(2, \mathbb{C}) / \{\lambda I\} \cong \mathrm{PSL}(2, \mathbb{C})$$

와 동형이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

두 행렬 $$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$$, $$A' = \begin{pmatrix} a' & b' \\ c' & d' \end{pmatrix}$$에 대응하는 Möbius 변환을 각각 $$T_A, T_{A'}$$라 하자. 합성 $$T_A \circ T_{A'}$$을 직접 계산하면

$$T_A(T_{A'}(z)) = \frac{a \cdot \frac{a'z + b'}{c'z + d'} + b}{c \cdot \frac{a'z + b'}{c'z + d'} + d} = \frac{a(a'z + b') + b(c'z + d')}{c(a'z + b') + d(c'z + d')} = \frac{(aa' + bc')z + (ab' + bd')}{(ca' + dc')z + (cb' + dd')}$$

인데, 마지막 식의 계수들이 정확히 곱행렬

$$AA' = \begin{pmatrix} aa' + bc' & ab' + bd' \\ ca' + dc' & cb' + dd' \end{pmatrix}$$

의 성분이다. 따라서 $$T_A \circ T_{A'} = T_{AA'}$$이고, 이는 행렬곱이 사상합성과 어울림을 뜻한다 (이 계산은 $$\infty$$를 포함한 점들에서도 극한으로 정합적이다). 특히 합성이 다시 Möbius 변환이고, $$\det(AA') = \det A \det A' \neq 0$$으로 비퇴화 조건이 보존된다. 항등행렬 $$I$$는 항등사상 $$T_I(z) = z$$를 주고, $$A$$의 역행렬 $$A^{-1}$$이 $$T_A$$의 역사상을 주므로 ($$T_A \circ T_{A^{-1}} = T_I$$) Möbius 변환 전체가 군을 이룬다.

대응 $$A \mapsto T_A$$이 준동형사상임은 위에서 보았다. 그 핵을 구한다. $$T_A(z) = z$$이 모든 $$z$$에서 성립하려면 $$az + b = z(cz + d)$$, 곧 $$cz^2 + (d - a)z - b = 0$$이 모든 $$z$$에서 성립해야 하므로 $$c = 0$$, $$b = 0$$, $$a = d$$이다. 곧 $$A = aI$$ ($$a \neq 0$$) 꼴이다. 역으로 그러한 $$A$$는 항등사상을 준다. 따라서 핵은 $$\{\lambda I : \lambda \in \mathbb{C}^\times\}$$이고, 준동형정리에 의해 Möbius 변환군은 $$\mathrm{GL}(2, \mathbb{C})/\{\lambda I\} = \mathrm{PGL}(2, \mathbb{C})$$와 동형이다. 한편 임의의 $$A \in \mathrm{GL}(2, \mathbb{C})$$는 $$\mu^2 = \det A$$인 $$\mu$$로 나누어 $$A/\mu \in \mathrm{SL}(2, \mathbb{C})$$로 만들 수 있고 이것이 같은 Möbius 변환을 주므로, $$\mathrm{PGL}(2, \mathbb{C})$$는 $$\mathrm{SL}(2, \mathbb{C})$$을 그 중심 $$\{\pm I\}$$로 나눈 $$\mathrm{PSL}(2, \mathbb{C})$$와 동형이다.

</details>

명제 5는 Möbius 변환의 합성이 행렬곱으로 번역됨을 말하며, 이로써 일차분수변환의 대수가 $$2 \times 2$$ 가역행렬의 대수로 환원된다. 행렬과 그 스칼라배가 같은 변환을 주므로, 변환을 행렬로 다룰 때는 언제든 $$\det A = 1$$이 되도록 정규화할 수 있다. 군 $$\mathrm{PSL}(2, \mathbb{C})$$이 정확히 $$\widehat{\mathbb{C}}$$의 모든 정칙 자기동형사상을 이룬다는 사실까지 알려져 있는데, 그 증명은 무한대에서의 거동 분석을 요구하므로 여기서는 Möbius 변환이 자기동형사상임을 확인하는 데 그친다. Möbius 변환의 구조를 더 들여다보기 위해, 임의의 변환이 몇 가지 기본 변환의 합성으로 쪼개짐을 본다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> 임의의 Möbius 변환은 평행이동 $$z \mapsto z + \beta$$, 확대·회전 $$z \mapsto \alpha z$$ ($$\alpha \neq 0$$), 반전 $$z \mapsto 1/z$$의 합성으로 표현된다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$T(z) = (az + b)/(cz + d)$$를 본다. $$c = 0$$이면 $$d \neq 0$$이고 $$T(z) = (a/d)z + (b/d)$$이므로, 확대·회전 $$z \mapsto (a/d)z$$ 다음에 평행이동 $$z \mapsto z + b/d$$를 합성한 것이다.

$$c \neq 0$$이면 분자를 분모로 나누는 항등식

$$T(z) = \frac{az + b}{cz + d} = \frac{a}{c} + \frac{b - \frac{ad}{c}}{cz + d} = \frac{a}{c} - \frac{ad - bc}{c}\cdot\frac{1}{cz + d}$$

을 쓴다. 이는 다음 합성으로 읽힌다. 먼저 $$z_1 = cz + d$$ (확대·회전 $$z \mapsto cz$$와 평행이동 $$z \mapsto z + d$$의 합성), 다음 $$z_2 = 1/z_1$$ (반전), 다음 $$z_3 = -\frac{ad - bc}{c} z_2$$ (확대·회전), 끝으로 $$z_4 = z_3 + a/c$$ (평행이동) 을 차례로 적용하면 $$z_4 = T(z)$$이다. 각 단계가 세 종류의 기본 변환 가운데 하나이므로 증명이 끝난다.

</details>

이 분해는 Möbius 변환의 기하적 성질을 기본 변환들로부터 조립하게 해 준다. 평행이동과 확대·회전이 직선을 직선으로, 원을 원으로 보냄은 자명하므로, 비자명한 부분은 반전 $$z \mapsto 1/z$$의 거동뿐이다. 다음 명제가 그 핵심을 담는다.

<div class="proposition" markdown="1">

<ins id="thm7">**정리 7**</ins> 모든 Möbius 변환은 $$\widehat{\mathbb{C}}$$에서 *원-직선<sub>circle or line</sub>*을 원-직선으로 보낸다. 곧 평면의 원과 직선을 통틀어 부르면, 임의의 Möbius 변환은 그러한 도형 하나를 다시 그러한 도형 하나로 옮긴다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

평면의 원과 직선은 실수 $$A, C$$와 복소수 $$B$$가 $$\lvert B\rvert^2 > AC$$를 만족할 때의 방정식

$$A\,\lvert z\rvert^2 + \overline{B}z + B\bar{z} + C = 0 \tag{$\ast$}$$

으로 한꺼번에 적힌다. 실제로 $$z = x + iy$$로 풀어 쓰면 이는 $$A(x^2 + y^2) + 2\Real(\overline{B}z) + C = 0$$ 꼴의 실방정식이고, $$A \neq 0$$이면 (완전제곱으로 정리하여) 원을, $$A = 0$$이면 직선을 나타낸다. 조건 $$\lvert B\rvert^2 > AC$$은 그 자취가 공집합이나 한 점이 아니라 진짜 원 또는 직선이 되도록 보장한다.

명제 6에 의해 임의의 Möbius 변환이 평행이동, 확대·회전, 반전의 합성이므로, 이 세 기본 변환 각각이 $$(\ast)$$ 꼴 방정식을 다시 $$(\ast)$$ 꼴로 보냄을 보이면 충분하다. 평행이동 $$z \mapsto z + \beta$$와 확대·회전 $$z \mapsto \alpha z$$은 직선을 직선으로, 원을 원으로 보냄이 기하적으로 분명하고 방정식 차원에서도 $$(\ast)$$ 꼴이 보존된다. 반전 $$w = 1/z$$, 곧 $$z = 1/w$$를 $$(\ast)$$에 대입하면

$$A\,\frac{1}{\lvert w\rvert^2} + \overline{B}\,\frac{1}{w} + B\,\frac{1}{\bar w} + C = 0$$

이고, 양변에 $$\lvert w\rvert^2 = w\bar w$$를 곱하면

$$A + \overline{B}\,\bar w + B\,w + C\,\lvert w\rvert^2 = 0, \qquad \text{곧}\quad C\,\lvert w\rvert^2 + B w + \overline{B}\,\bar w + A = 0$$

이 된다. 이는 다시 $$(\ast)$$ 꼴이며 ($$A, C$$의 역할과 $$B, \overline B$$의 역할이 바뀌었을 뿐이고, 판별식 $$\lvert B\rvert^2 > CA = AC$$은 그대로이다), 따라서 반전도 원-직선을 원-직선으로 보낸다. 세 기본 변환이 모두 $$(\ast)$$ 꼴을 보존하므로 그 합성인 임의의 Möbius 변환도 그러하다.

</details>

정리 7은 원과 직선을 한데 묶어 다루는 관점이 Möbius 변환에 본질적임을 보여 준다. $$\widehat{\mathbb{C}}$$에서는 직선이 $$\infty$$를 지나는 "원"으로 자연스럽게 편입되므로, 원-직선이란 곧 Riemann 구면 위의 (입체사영을 통한) 진짜 원에 대응한다. 반전이 직선을 원으로 또는 원을 직선으로 바꿀 수 있음에 유의해야 한다. 가령 원점을 지나는 직선은 $$A = C = 0$$인 경우인데, 반전 후 방정식에서 상수항이 $$A = 0$$으로 남아 여전히 직선이지만, 원점을 지나지 않는 직선 ($$A = 0$$, $$C \neq 0$$) 은 반전 후 $$C\lvert w\rvert^2$$ 항이 살아나 원이 된다.

## 교차비와 세 점 결정

Möbius 변환은 세 점의 상을 지정하는 것만으로 완전히 결정된다. 이 유일성을 떠받치는 양이 교차비이며, 그것이 모든 Möbius 변환 아래 불변이라는 사실이 출발점이다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> $$\widehat{\mathbb{C}}$$의 서로 다른 네 점 $$z_1, z_2, z_3, z_4$$에 대하여 그 *교차비<sub>cross-ratio</sub>*를

$$(z_1, z_2; z_3, z_4) = \frac{(z_1 - z_3)(z_2 - z_4)}{(z_1 - z_4)(z_2 - z_3)}$$

로 정의한다. 네 점 가운데 하나가 $$\infty$$이면, 그 점이 들어간 두 차의 비를 $$1$$로 두어 얻는 극한값으로 정의한다.

</div>

가령 $$z_4 = \infty$$이면 위 정의에서 $$(z_2 - z_4)/(z_1 - z_4) \to 1$$이므로 $$(z_1, z_2; z_3, \infty) = (z_1 - z_3)/(z_2 - z_3)$$이다. 교차비는 네 점의 순서에 의존하며, 우리는 위의 순서 약속을 고정해 쓴다. 이 양의 결정적 성질은 Möbius 변환에 대한 불변성이다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> 임의의 Möbius 변환 $$T$$와 $$\widehat{\mathbb{C}}$$의 서로 다른 네 점 $$z_1, z_2, z_3, z_4$$에 대하여

$$(Tz_1, Tz_2; Tz_3, Tz_4) = (z_1, z_2; z_3, z_4)$$

이다. 곧 교차비는 Möbius 변환 아래 불변이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

명제 6에 의해 $$T$$가 평행이동, 확대·회전, 반전의 합성이므로, 이 세 기본 변환 각각이 교차비를 보존함을 보이면 합성인 $$T$$도 보존한다. 두 점 $$z, w$$의 차에 대한 거동을 보면 충분하다. 평행이동 $$T(z) = z + \beta$$에 대해서는 $$Tz - Tw = (z + \beta) - (w + \beta) = z - w$$이므로 정의 8의 네 차가 모두 그대로이고 교차비가 불변이다. 확대·회전 $$T(z) = \alpha z$$에 대해서는 $$Tz - Tw = \alpha(z - w)$$이므로 네 차에 각각 $$\alpha$$가 곱해지는데, 교차비는 두 차의 곱을 다른 두 차의 곱으로 나눈 것이라 $$\alpha$$가 분자·분모에서 상쇄되어 불변이다. 반전 $$T(z) = 1/z$$에 대해서는

$$Tz_i - Tz_j = \frac{1}{z_i} - \frac{1}{z_j} = \frac{z_j - z_i}{z_i z_j}$$

이므로, 교차비의 네 차에 이를 대입하면

$$\frac{(Tz_1 - Tz_3)(Tz_2 - Tz_4)}{(Tz_1 - Tz_4)(Tz_2 - Tz_3)} = \frac{\frac{(z_3 - z_1)(z_4 - z_2)}{z_1 z_3 z_2 z_4}}{\frac{(z_4 - z_1)(z_3 - z_2)}{z_1 z_4 z_2 z_3}} = \frac{(z_3 - z_1)(z_4 - z_2)}{(z_4 - z_1)(z_3 - z_2)} = (z_1, z_2; z_3, z_4)$$

이다. 분모의 좌표 곱 $$z_1 z_2 z_3 z_4$$이 분자·분모에서 똑같이 나타나 상쇄되고, 각 차의 부호 반전 $$z_j - z_i = -(z_i - z_j)$$이 분자와 분모에서 두 번씩 일어나 상쇄되었다. $$\infty$$가 끼는 경우는 정의 8의 극한 약속과 양립하도록 같은 계산이 극한으로 이어진다. 세 기본 변환이 모두 교차비를 보존하므로 그 합성인 $$T$$도 보존한다.

</details>

명제 9의 불변성은 Möbius 변환이 세 점으로 결정된다는 다음 정리로 곧장 이어진다. 서로 다른 세 점을 서로 다른 세 점으로 보내는 변환이 정확히 하나라는 이 사실은, 교차비를 매개로 그 변환을 명시적으로 적게까지 해 준다.

<div class="proposition" markdown="1">

<ins id="thm10">**정리 10 (세 점 결정)**</ins> $$\widehat{\mathbb{C}}$$의 서로 다른 세 점 $$z_1, z_2, z_3$$과 서로 다른 세 점 $$w_1, w_2, w_3$$이 주어지면, $$T(z_i) = w_i$$ ($$i = 1, 2, 3$$) 인 Möbius 변환 $$T$$가 유일하게 존재한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

먼저 존재성을 본다. 서로 다른 세 점 $$z_1, z_2, z_3$$을 각각 $$0, 1, \infty$$로 보내는 변환을 교차비로 적을 수 있다. 사상

$$S(z) = (z, z_2; z_1, z_3) = \frac{(z - z_1)(z_2 - z_3)}{(z - z_3)(z_2 - z_1)}$$

는 $$z$$에 대한 일차분수변환이고, $$z_2 - z_3, z_2 - z_1$$이 $$0$$이 아닌 상수이므로 비퇴화이다. 대입하면 $$S(z_1) = 0$$, $$S(z_2) = 1$$, $$S(z_3) = \infty$$이다 ($$z_3$$에서 분모가 $$0$$이 된다). 마찬가지로 $$w_1, w_2, w_3$$을 $$0, 1, \infty$$로 보내는 $$S'(w) = (w, w_2; w_1, w_3)$$을 잡으면, 합성 $$T = S'^{-1} \circ S$$이 Möbius 변환이고 $$T(z_i) = S'^{-1}(S(z_i)) = S'^{-1}(\{0, 1, \infty\}\text{의 해당 점}) = w_i$$이다.

유일성을 본다. $$T, \widetilde T$$가 모두 세 점을 같은 상으로 보낸다고 하면, $$U = \widetilde T^{-1} \circ T$$은 Möbius 변환이고 $$z_1, z_2, z_3$$을 모두 고정한다. Möbius 변환이 서로 다른 세 고정점을 가지면 항등사상임을 보이면 된다. $$U(z) = (az + b)/(cz + d)$$가 점 $$z_0$$을 고정하면 $$az_0 + b = z_0(cz_0 + d)$$, 곧 $$cz_0^2 + (d - a)z_0 - b = 0$$이다. 이 이차방정식 (만일 $$c \neq 0$$) 은 많아야 두 해를 가지므로, 유한한 고정점이 셋 이상이려면 $$c = 0$$이어야 한다. 그러면 식은 $$(d - a)z_0 = b$$라는 일차식이 되어, $$d \neq a$$이면 고정점이 하나뿐이고 ($$\infty$$ 포함 둘), $$b \neq 0$$이고 $$d = a$$이면 유한 고정점이 없다. 서로 다른 유한 고정점이 셋 (또는 둘 이상이면서 $$\infty$$도 고정) 이려면 $$c = 0$$, $$d = a$$, $$b = 0$$이어야 하고, 이는 $$U(z) = z$$, 곧 항등사상이다. 따라서 $$\widetilde T^{-1} \circ T = \mathrm{id}$$이고 $$T = \widetilde T$$이다.

</details>

정리 10은 Möbius 변환을 다루는 실용적 도구를 준다. 두 영역의 경계 위 세 점의 대응을 지정하면 변환이 유일하게 정해지므로, 경계를 맞추는 등각사상을 명시적으로 구성할 수 있다. 증명에 등장한 사상 $$z \mapsto (z, z_2; z_1, z_3)$$은 $$z_1, z_2, z_3$$을 $$0, 1, \infty$$로 보내는 표준화 변환이며, 임의의 세 점을 다루는 문제를 이 표준 삼점으로 환원하는 데 거듭 쓰인다. 또 정리 7과 결합하면, 세 점이 한 원-직선 위에 있을 때 그 상 세 점이 결정하는 원-직선으로 전체가 옮겨진다는 사실을 얻어, 원-직선을 원하는 원-직선으로 포개는 변환을 세 점만으로 지정할 수 있다.

## 단위원판의 자기동형사상

Möbius 변환 가운데 단위원판 $$\mathbb{D} = \{z : \lvert z\rvert < 1\}$$을 자기 자신으로 보내는 것들을 가려내면, 단위원판의 정칙 자기동형사상 전체가 드러난다. 한 점 $$a \in \mathbb{D}$$를 원점으로 옮기는 특정한 Möbius 변환에서 출발한다.

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> $$a \in \mathbb{D}$$에 대하여 사상

$$\varphi_a(z) = \frac{z - a}{1 - \bar a z}$$

는 $$\mathbb{D}$$를 $$\mathbb{D}$$로 보내는 전단사 Möbius 변환이며, $$\varphi_a(a) = 0$$, $$\varphi_a(0) = -a$$이고 그 역사상은 $$\varphi_{-a}$$이다. 또 단위원 $$\lvert z\rvert = 1$$을 단위원으로 보낸다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\varphi_a$$는 분자·분모가 일차식이고 행렬식이 $$1 \cdot 1 - (-a)(-\bar a) = 1 - \lvert a\rvert^2 \neq 0$$ ($$\lvert a\rvert < 1$$이므로) 이라 비퇴화 Möbius 변환이다. 먼저 단위원 위에서의 절댓값을 본다. $$\lvert z\rvert = 1$$이면 $$z\bar z = 1$$이므로

$$\lvert 1 - \bar a z\rvert = \lvert \bar z\rvert\,\lvert 1 - \bar a z\rvert = \lvert \bar z(1 - \bar a z)\rvert = \lvert \bar z - \bar a\rvert = \lvert \overline{z - a}\rvert = \lvert z - a\rvert$$

이다 (둘째 등호에서 $$\lvert \bar z\rvert = \lvert z\rvert = 1$$을 썼다). 따라서 $$\lvert z\rvert = 1$$이면 $$\lvert \varphi_a(z)\rvert = \lvert z - a\rvert / \lvert 1 - \bar a z\rvert = 1$$이므로, $$\varphi_a$$은 단위원을 단위원으로 보낸다.

이제 $$\varphi_a$$이 $$\mathbb{D}$$를 $$\mathbb{D}$$로 보냄을 본다. $$\varphi_a$$은 단위원에서 분모 $$1 - \bar a z$$가 $$0$$이 되지 않으므로 ($$\lvert z\rvert \leq 1$$, $$\lvert a\rvert < 1$$이면 $$\lvert \bar a z\rvert < 1$$) 닫힌 원판 $$\overline{\mathbb{D}}$$에서 연속이고 내부에서 정칙이다. 경계 $$\lvert z\rvert = 1$$에서 $$\lvert \varphi_a\rvert = 1$$임을 방금 보였고, 내부의 한 점 $$z = a$$에서 $$\varphi_a(a) = 0$$이라 $$\lvert \varphi_a(a)\rvert = 0 < 1$$이다. 따라서 연속인 $$\lvert \varphi_a\rvert$$이 경계에서 $$1$$, 내부 한 점에서 $$1$$ 미만이므로, 최대절댓값 원리 ([§영점과 일치정리, ⁋따름정리 6](/ko/math/complex_analysis/zeros_and_identity_theorem#cor6)) 에 의해 $$\mathbb{D}$$ 전체에서 $$\lvert \varphi_a(z)\rvert < 1$$이다 (내부에서 $$1$$에 이르면 상수가 되어야 하나 $$\varphi_a$$은 비상수이다). 곧 $$\varphi_a(\mathbb{D}) \subseteq \mathbb{D}$$이다.

끝으로 역사상을 계산한다. $$\varphi_{-a}(z) = (z + a)/(1 + \bar a z)$$인데, 직접 합성하면

$$\varphi_{-a}(\varphi_a(z)) = \frac{\frac{z - a}{1 - \bar a z} + a}{1 + \bar a \cdot \frac{z - a}{1 - \bar a z}} = \frac{(z - a) + a(1 - \bar a z)}{(1 - \bar a z) + \bar a(z - a)} = \frac{z(1 - \lvert a\rvert^2)}{1 - \lvert a\rvert^2} = z$$

이다. 따라서 $$\varphi_{-a} = \varphi_a^{-1}$$이고, 특히 $$\varphi_a$$은 $$\mathbb{D}$$ 위의 전단사이다 (그 역도 같은 논법으로 $$\mathbb{D}$$를 $$\mathbb{D}$$로 보낸다). $$\varphi_a(0) = (0 - a)/(1 - 0) = -a$$임은 대입으로 즉시 나온다.

</details>

사상 $$\varphi_a$$은 단위원판의 자기동형사상을 다룰 때 가장 기본이 되는 벽돌이다. 그것은 임의로 주어진 내부의 한 점 $$a$$를 중심 $$0$$으로 끌어오면서 단위원판 구조를 보존하므로, 원점을 특별한 위치로 옮겨 문제를 단순화하는 데 쓰인다. 여기에 회전을 합성하면 단위원판의 모든 정칙 자기동형사상이 나온다는 것이 다음 정리이며, 그 증명은 원점을 고정하는 자기동형사상이 회전뿐이라는 Schwarz 보조정리의 귀결 ([§영점과 일치정리, ⁋예시 8](/ko/math/complex_analysis/zeros_and_identity_theorem#ex8)) 을 핵심으로 쓴다.

<div class="proposition" markdown="1">

<ins id="thm12">**정리 12 (단위원판의 자기동형사상)**</ins> $$f : \mathbb{D} \to \mathbb{D}$$가 정칙 전단사이고 그 역사상도 정칙이라 하자. 그러면 어떤 $$a \in \mathbb{D}$$와 실수 $$\theta$$가 있어

$$f(z) = e^{i\theta}\,\frac{z - a}{1 - \bar a z} = e^{i\theta}\,\varphi_a(z)$$

이다. 역으로 이 꼴의 모든 사상은 $$\mathbb{D}$$의 정칙 자기동형사상이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$f$$가 $$\mathbb{D}$$의 정칙 자기동형사상이라 하자. $$a = f^{-1}(0) \in \mathbb{D}$$이라 두고 $$g = f \circ \varphi_a^{-1} = f \circ \varphi_{-a}$$를 생각한다. 명제 11에 의해 $$\varphi_{-a}$$이 $$\mathbb{D}$$의 자기동형사상이므로 $$g$$도 $$\mathbb{D}$$의 정칙 자기동형사상이고, $$\varphi_{-a}(0) = a$$이므로

$$g(0) = f(\varphi_{-a}(0)) = f(a) = 0$$

이다. 곧 $$g$$는 원점을 고정하는 $$\mathbb{D}$$의 정칙 자기동형사상이다. 원점을 고정하는 단위원판의 자기동형사상이 회전뿐이므로 ([§영점과 일치정리, ⁋예시 8](/ko/math/complex_analysis/zeros_and_identity_theorem#ex8)), 어떤 실수 $$\theta$$에 대해 $$g(z) = e^{i\theta} z$$이다. 따라서

$$f = g \circ \varphi_a, \qquad f(z) = e^{i\theta}\,\varphi_a(z) = e^{i\theta}\,\frac{z - a}{1 - \bar a z}$$

이다.

역으로 $$f(z) = e^{i\theta}\varphi_a(z)$$ 꼴이면, $$\varphi_a$$이 $$\mathbb{D}$$의 자기동형사상이고 ([명제 11](#prop11)) 회전 $$z \mapsto e^{i\theta}z$$도 그러하므로, 그 합성인 $$f$$도 $$\mathbb{D}$$의 정칙 자기동형사상이다.

</details>

정리 12는 단위원판의 정칙 자기동형사상 전체가 두 매개변수, 곧 $$a \in \mathbb{D}$$와 회전각 $$\theta$$로 매개됨을 말한다. 이 자기동형사상들은 모두 Möbius 변환이므로 단위원판의 자기동형군은 $$\mathrm{PSL}(2, \mathbb{C})$$의 한 부분군이며, 그 안에서 단위원을 보존하는 변환들로 이루어진다. 같은 분류는 단위원판 위의 정칙사상이 자연스러운 거리를 늘리지 않는다는 정량적 결과로 이어지는데, 이것이 Schwarz–Pick 정리이다.

<div class="proposition" markdown="1">

<ins id="thm13">**정리 13 (Schwarz–Pick)**</ins> $$f : \mathbb{D} \to \mathbb{D}$$가 정칙이라 하자. 그러면 모든 $$z, w \in \mathbb{D}$$에 대하여

$$\left\lvert \frac{f(z) - f(w)}{1 - \overline{f(w)}\,f(z)} \right\rvert \leq \left\lvert \frac{z - w}{1 - \bar w z} \right\rvert$$

이고, 또 모든 $$z \in \mathbb{D}$$에 대하여

$$\frac{\lvert f'(z)\rvert}{1 - \lvert f(z)\rvert^2} \leq \frac{1}{1 - \lvert z\rvert^2}$$

이다. 어느 한 부등식에서 한 점이라도 등호가 성립하면 $$f$$는 $$\mathbb{D}$$의 자기동형사상이고 두 부등식이 모든 점에서 등호가 된다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$w \in \mathbb{D}$$를 고정하고 보조사상

$$F = \varphi_{f(w)} \circ f \circ \varphi_{-w} = \varphi_{f(w)} \circ f \circ \varphi_w^{-1}$$

을 생각한다. 명제 11에 의해 $$\varphi_{-w}$$과 $$\varphi_{f(w)}$$이 $$\mathbb{D}$$를 $$\mathbb{D}$$로 보내고 $$f$$도 그러하므로 $$F : \mathbb{D} \to \mathbb{D}$$은 정칙이다. 또 $$\varphi_{-w}(0) = w$$이므로

$$F(0) = \varphi_{f(w)}(f(\varphi_{-w}(0))) = \varphi_{f(w)}(f(w)) = 0$$

이다 ($$\varphi_{f(w)}$$이 $$f(w)$$를 $$0$$으로 보내므로). 곧 $$F$$는 원점을 고정하는 $$\mathbb{D} \to \mathbb{D}$$ 정칙사상이라, Schwarz 보조정리 ([§영점과 일치정리, ⁋정리 7](/ko/math/complex_analysis/zeros_and_identity_theorem#thm7)) 에 의해 모든 $$\zeta \in \mathbb{D}$$에서 $$\lvert F(\zeta)\rvert \leq \lvert \zeta\rvert$$이고 $$\lvert F'(0)\rvert \leq 1$$이다.

이제 $$\zeta = \varphi_w(z)$$를 대입한다. 정의상 $$\zeta = (z - w)/(1 - \bar w z)$$이고, $$\varphi_{-w} = \varphi_w^{-1}$$이므로 $$\varphi_{-w}(\zeta) = z$$, 따라서

$$F(\zeta) = \varphi_{f(w)}(f(z)) = \frac{f(z) - f(w)}{1 - \overline{f(w)}\,f(z)}$$

이다. 부등식 $$\lvert F(\zeta)\rvert \leq \lvert \zeta\rvert$$을 이 두 표현으로 적으면 첫 부등식

$$\left\lvert \frac{f(z) - f(w)}{1 - \overline{f(w)}\,f(z)} \right\rvert \leq \left\lvert \frac{z - w}{1 - \bar w z} \right\rvert$$

을 얻는다. 미분형은 이 부등식에서 $$z \to w$$의 극한을 취해 나온다. 좌변을 $$\lvert z - w\rvert$$로 나누고 $$z \to w$$로 보내면, 좌변의 분자 차분비는 $$\lvert f'(w)\rvert$$로, 분모는 $$1 - \lvert f(w)\rvert^2$$로 가고 (분모에서 $$\overline{f(w)}f(z) \to \lvert f(w)\rvert^2$$), 우변은 $$1/(1 - \lvert w\rvert^2)$$로 가므로

$$\frac{\lvert f'(w)\rvert}{1 - \lvert f(w)\rvert^2} \leq \frac{1}{1 - \lvert w\rvert^2}$$

이다. $$w \in \mathbb{D}$$이 임의였으므로 둘째 부등식이 모든 점에서 성립한다.

등호의 경우를 본다. 첫 부등식이 어떤 $$z_0 \neq w$$에서 등호이면 $$\lvert F(\zeta_0)\rvert = \lvert \zeta_0\rvert$$ ($$\zeta_0 = \varphi_w(z_0) \neq 0$$) 이고, 둘째 부등식이 어떤 점에서 등호이면 그 점에 대응하는 $$w$$에서 $$\lvert F'(0)\rvert = 1$$이다. 어느 경우든 Schwarz 보조정리의 등호조건 ([§영점과 일치정리, ⁋정리 7](/ko/math/complex_analysis/zeros_and_identity_theorem#thm7)) 에 의해 어떤 $$\lambda$$ ($$\lvert \lambda\rvert = 1$$) 가 있어 $$F(\zeta) = \lambda \zeta$$이다. 그러면 $$F$$가 $$\mathbb{D}$$의 자기동형사상이고, $$f = \varphi_{f(w)}^{-1} \circ F \circ \varphi_w$$도 자기동형사상들의 합성이라 자기동형사상이다. 이때 위의 두 부등식은 $$\lvert F(\zeta)\rvert = \lvert \zeta\rvert$$, $$\lvert F'(0)\rvert = 1$$로부터 모든 점에서 등호가 된다.

</details>

Schwarz–Pick 정리는 Schwarz 보조정리를 원점이라는 특정 점에 매이지 않게 풀어낸 형태이다. 좌변의 양

$$\rho(z, w) = \left\lvert \frac{z - w}{1 - \bar w z} \right\rvert$$

은 단위원판 위의 두 점 사이의 *유사쌍곡거리<sub>pseudo-hyperbolic distance</sub>*라 불리며, 정리 13의 첫 부등식은 임의의 정칙사상 $$f : \mathbb{D} \to \mathbb{D}$$이 이 거리를 늘리지 않음을 뜻한다. 미분형은 같은 사실을 무한소 수준에서 적은 것으로, 단위원판에 $$ds = \lvert dz\rvert/(1 - \lvert z\rvert^2)$$ 꼴의 거리 (쌍곡거리) 를 줄 때 정칙사상이 그 거리를 늘리지 않으며, 자기동형사상일 때만 정확히 보존한다는 진술이다. 등호가 자기동형사상에서만 성립한다는 사실은 단위원판의 자기동형군이 이 쌍곡거리의 등거리변환군과 정확히 일치함을 시사한다.

## 상반평면과 Cayley 변환

단위원판과 더불어 자주 등장하는 표준영역이 상반평면이다. 이 둘은 한 Möbius 변환으로 등각동형이며, 그 변환을 Cayley 변환이라 한다. 상반평면을 $$\mathbb{H} = \{z \in \mathbb{C} : \Img z > 0\}$$으로 적는다.

<div class="proposition" markdown="1">

<ins id="thm14">**정리 14 (Cayley 변환)**</ins> Möbius 변환

$$C(z) = \frac{z - i}{z + i}$$

은 상반평면 $$\mathbb{H}$$를 단위원판 $$\mathbb{D}$$로 보내는 등각동형사상이며, 그 역사상은

$$C^{-1}(w) = i\,\frac{1 + w}{1 - w}$$

이다. 곧 $$C$$는 $$\mathbb{H}$$와 $$\mathbb{D}$$ 사이의 정칙 전단사이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$C(z) = (z - i)/(z + i)$$은 행렬식이 $$1 \cdot i - (-i) \cdot 1 = 2i \neq 0$$이라 비퇴화 Möbius 변환이다. 먼저 $$C$$가 $$\mathbb{H}$$를 $$\mathbb{D}$$로 보냄을 본다. $$z \in \mathbb{C}$$에 대해 $$\lvert C(z)\rvert < 1$$인 것은 $$\lvert z - i\rvert < \lvert z + i\rvert$$인 것, 곧 $$z$$가 점 $$i$$에 점 $$-i$$보다 더 가까운 것과 동치이다. 두 점 $$\pm i$$의 수직이등분선이 실축이고 $$i$$가 상반평면에 있으므로, $$z$$가 $$i$$에 더 가까운 것은 정확히 $$\Img z > 0$$, 곧 $$z \in \mathbb{H}$$인 것과 동치이다. 대수적으로도 $$z = x + iy$$로 두면

$$\lvert z + i\rvert^2 - \lvert z - i\rvert^2 = (x^2 + (y+1)^2) - (x^2 + (y-1)^2) = 4y$$

이므로 $$\lvert C(z)\rvert < 1 \iff \lvert z - i\rvert^2 < \lvert z + i\rvert^2 \iff 4y > 0 \iff \Img z > 0$$이다. 따라서 $$C(\mathbb{H}) \subseteq \mathbb{D}$$이다. 같은 계산에서 $$4y = 0$$, 곧 $$z$$가 실축 위에 있는 것이 $$\lvert C(z)\rvert = 1$$과 동치이므로, $$C$$는 실축 (그리고 $$\infty$$) 을 단위원으로 보낸다.

다음으로 역사상을 구한다. $$w = (z - i)/(z + i)$$을 $$z$$에 대해 푼다. $$w(z + i) = z - i$$에서 $$wz + wi = z - i$$, 곧 $$z(w - 1) = -i - wi = -i(1 + w)$$이므로

$$z = \frac{-i(1 + w)}{w - 1} = \frac{i(1 + w)}{1 - w} = i\,\frac{1 + w}{1 - w}$$

이다. 이것이 $$C^{-1}$$이며 다시 Möbius 변환이다. $$C$$가 $$\mathbb{H}$$를 $$\mathbb{D}$$ 안으로 보내고 $$C^{-1}$$이 그 역을 주므로 ($$C^{-1}(C(z)) = z$$), $$C$$는 $$\mathbb{H}$$와 $$\mathbb{D}$$ 사이의 전단사이고, $$C^{-1}(\mathbb{D}) \subseteq \mathbb{H}$$임도 같은 거리 논법으로 ($$\lvert w\rvert < 1$$이 $$\Img C^{-1}(w) > 0$$과 동치임을 확인하여) 따라 나온다. Möbius 변환은 정칙이므로 ([명제 2 다음의 관찰](#prop2)) $$C$$는 $$\mathbb{H}$$와 $$\mathbb{D}$$ 사이의 등각동형사상이다.

</details>

Cayley 변환은 상반평면 위의 문제를 단위원판 위의 문제로, 또는 그 역으로 옮기는 사전 역할을 한다. 가령 정리 12의 단위원판 자기동형사상 분류를 $$C$$로 옮기면, 상반평면의 정칙 자기동형사상이 정확히 실계수 Möbius 변환

$$z \mapsto \frac{\alpha z + \beta}{\gamma z + \delta}, \qquad \alpha, \beta, \gamma, \delta \in \mathbb{R},\ \alpha\delta - \beta\gamma > 0$$

들, 곧 $$\mathrm{PSL}(2, \mathbb{R})$$의 원소들임을 얻는다. 단위원이 실축에 대응하고 단위원판의 쌍곡거리가 상반평면의 쌍곡거리로 옮겨지므로, 두 영역은 등각기하의 관점에서 완전히 같은 대상의 두 모형이 된다. 상반평면 모형은 경계가 직선 (실축) 이라 계산이 간편할 때가 많고, 단위원판 모형은 자기동형사상 $$\varphi_a$$의 대칭성이 드러나 분류에 유리하여, 문제에 따라 Cayley 변환으로 오가며 둘을 함께 쓴다.

---

**참고문헌**

**[Ahl]** L.V. Ahlfors, *Complex analysis*, 3rd ed., McGraw–Hill, 1979.

**[Con]** J.B. Conway, *Functions of one complex variable I*, 2nd ed., Graduate Texts in Mathematics 11, Springer, 1978.

**[SS]** E.M. Stein, R. Shakarchi, *Complex analysis*, Princeton Lectures in Analysis II, Princeton University Press, 2003.
</content>
</invoke>
