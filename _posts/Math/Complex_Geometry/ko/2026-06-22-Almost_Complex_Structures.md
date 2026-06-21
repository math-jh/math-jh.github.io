---
title: "거의 복소구조"
description: "실벡터다발의 자기준동형 J로서 J²=-id를 만족하는 거의 복소구조를 정의하고, 복소다양체의 표준 J가 그 예임을 보인다. J의 ±i 고유공간 분해로 복소화 접다발을 (1,0)·(0,1) 부분으로 나누고 (p,q)-형식의 분해를 얻는다. Nijenhuis 텐서로 적분가능성을 특징짓고, 그 소멸이 복소구조의 존재와 동치라는 Newlander–Nirenberg 정리를 서술한다."
excerpt: "거의 복소구조, J²=-id, 거의 복소다양체, 복소화 접다발, T^{1,0}, (p,q)-형식, 적분가능성, Nijenhuis 텐서, involutive 분포, Newlander–Nirenberg 정리, S^6, S^4"

categories: [Math / Complex Geometry]
permalink: /ko/math/complex_geometry/almost_complex_structures
sidebar:
    nav: "complex_geometry-ko"

date: 2026-06-22
weight: 2

published: false
---

복소다양체는 정칙 전이함수를 갖는 좌표계로 정의되었고, 그 강성의 거의 모든 출처가 이 정칙성이었다 ([§복소다양체, ⁋정의 3](/ko/math/complex_geometry/complex_manifolds#def3)). 그러나 복소구조가 접공간 수준에서 무엇을 하는지는 좌표계의 언어만으로는 잘 보이지 않는다. 각 점에서 정칙좌표 $$z_j = x_j + i y_j$$의 곱셈 $$i$$는 실 접공간 $$T_p M$$ 위의 한 선형사상, 곧 $$\partial/\partial x_j$$를 $$\partial/\partial y_j$$로, $$\partial/\partial y_j$$를 $$-\partial/\partial x_j$$로 보내는 사상으로 나타난다. 이 사상을 $$J_p$$라 하면 $$J_p^2 = -\id$$이고, 점이 변할 때 $$J_p$$는 매끄럽게 변한다. 이렇게 추출된 자료 $$J$$가 거의 복소구조이다.

이 글의 목표는 거의 복소구조를 복소구조와 독립적으로 정의하고, 복소구조에서 오는 $$J$$가 이를 만족함을 보인 뒤, 거꾸로 어떤 $$J$$가 복소구조에서 오는가 하는 *적분가능성* 물음에 답하는 것이다. 답의 핵심은 Nijenhuis 텐서의 소멸이며, 이것이 복소구조의 존재와 동치라는 Newlander–Nirenberg 정리가 이 글의 정점이다. 거의 복소구조는 복소구조보다 약하므로 위상적 제약만으로 존재 여부가 갈리는 일도 있으며, 짝수차원이라도 거의 복소구조를 전혀 갖지 못하는 다양체가 있다는 사실도 함께 다룬다.

## 거의 복소구조

거의 복소구조는 접다발 위에서 곱셈 $$i$$를 흉내내는 다발 사상이다. 어떤 좌표계도 전제하지 않고, 오직 $$J^2 = -\id$$이라는 대수적 조건만으로 규정된다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 매끄러운 다양체 $$M$$ 위의 *almost complex structure<sub>거의 복소구조</sub>*란 실 벡터다발 자기준동형사상 $$J : TM \to TM$$로서, 각 점 $$p$$에서의 제한 $$J_p : T_p M \to T_p M$$이 모두

$$
J_p^2 = -\id_{T_p M}
$$

을 만족하는 것이다. 거의 복소구조를 갖춘 다양체 $$(M, J)$$를 *almost complex manifold<sub>거의 복소다양체</sub>*라 한다.

</div>

여기서 $$J$$가 벡터다발 사상이라는 것은 $$J$$가 항등사상을 덮는 매끄러운 사상이며 각 fiber에서 $$\mathbb{R}$$-선형이라는 뜻이다 ([\[미분다양체\] §벡터장, ⁋정의 1](/ko/math/manifolds/vector_fields#def1)의 단면 개념과 같은 수준의 매끄러움이다). 조건 $$J_p^2 = -\id$$은 각 접공간 $$T_p M$$을 $$\mathbb{C}$$-벡터공간으로 만든다. 곧 스칼라 곱

$$
(a + bi) \cdot v = a v + b\, J_p v \qquad (a, b \in \mathbb{R},\ v \in T_p M)
$$

이 잘 정의되고, $$i \cdot v = J_p v$$이다. 이 $$\mathbb{C}$$-벡터공간 구조에서 실차원과 복소차원의 관계를 따지면 거의 복소다양체의 차원에 즉각적인 제약이 나온다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 거의 복소다양체 $$(M, J)$$의 실차원은 짝수이다. 더 정확히, $$\dim_{\mathbb{R}} M = 2n$$이면 각 $$T_p M$$은 $$J_p$$를 통해 복소차원 $$n$$의 $$\mathbb{C}$$-벡터공간이 된다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

위에서 본 대로 $$J_p^2 = -\id$$이면 $$(a+bi)\cdot v = av + b J_p v$$가 $$T_p M$$ 위에 $$\mathbb{C}$$-벡터공간 구조를 준다. 실제로 결합법칙을 확인하면, $$i \cdot (i \cdot v) = J_p(J_p v) = -v = (i \cdot i) \cdot v$$이고 나머지 공리는 $$\mathbb{R}$$-선형성에서 따라온다. 따라서 $$T_p M$$은 $$\mathbb{C}$$ 위의 벡터공간이다. 이 $$\mathbb{C}$$-벡터공간을 $$\mathbb{R}$$ 위로 다시 보면 실차원이 복소차원의 두 배이므로, $$\dim_{\mathbb{R}} T_p M = 2 \dim_{\mathbb{C}} T_p M$$이다. 따라서 실차원은 짝수 $$2n$$이고 복소차원은 $$n$$이다.

</details>

짝수차원은 필요조건일 뿐 충분조건이 아니다. 이 글의 마지막에서 보듯 $$S^4$$처럼 짝수차원이면서도 거의 복소구조를 전혀 갖지 못하는 다양체가 있다. 우선은 거의 복소구조의 가장 중요한 출처, 곧 복소다양체로부터 표준적으로 유도되는 $$J$$를 구성한다.

## 복소다양체의 표준 거의 복소구조

복소다양체 $$M$$은 실차원 $$2n$$의 매끄러운 다양체이기도 하다. 정칙좌표 $$z_j = x_j + i y_j$$가 주는 실좌표 $$(x_1, y_1, \ldots, x_n, y_n)$$에서, 곱셈 $$i$$를 접공간 위의 선형사상으로 옮긴 것이 표준 거의 복소구조이다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> $$M$$을 복소다양체라 하고, 각 점 $$p$$에서 정칙좌표 $$z_j = x_j + i y_j$$에 대하여 $$T_p M$$ 위의 선형사상 $$J_p$$를

$$
J_p\!\left( \frac{\partial}{\partial x_j} \right) = \frac{\partial}{\partial y_j}, \qquad
J_p\!\left( \frac{\partial}{\partial y_j} \right) = -\frac{\partial}{\partial x_j}
$$

로 정의하자. 그러면 $$J = (J_p)_p$$는 $$M$$ 위의 거의 복소구조이며, 정칙좌표의 선택에 무관하게 잘 정의된다. 이를 복소구조의 *standard almost complex structure<sub>표준 거의 복소구조</sub>*라 한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

먼저 한 좌표계 안에서 $$J_p^2 = -\id$$임을 확인하자. 정의에서

$$
J_p^2\!\left( \frac{\partial}{\partial x_j} \right) = J_p\!\left( \frac{\partial}{\partial y_j} \right) = -\frac{\partial}{\partial x_j}, \qquad
J_p^2\!\left( \frac{\partial}{\partial y_j} \right) = J_p\!\left( -\frac{\partial}{\partial x_j} \right) = -\frac{\partial}{\partial y_j}
$$

이므로 기저 위에서 $$J_p^2 = -\id$$이고, 선형성으로 $$T_p M$$ 전체에서 성립한다. 매끄러움은 $$J$$의 성분이 좌표기저에 대해 상수($$0$$ 또는 $$\pm 1$$)이므로 자명하다.

좌표 무관성을 보인다. 다른 정칙좌표 $$w_k = u_k + i v_k$$를 잡자. Wirtinger 미분으로 표현하면, $$J_p$$는 $$\partial/\partial z_j = \frac{1}{2}(\partial/\partial x_j - i\, \partial/\partial y_j)$$에 대하여

$$
J_p\!\left( \frac{\partial}{\partial z_j} \right) = i\, \frac{\partial}{\partial z_j}, \qquad
J_p\!\left( \frac{\partial}{\partial \bar{z}_j} \right) = -i\, \frac{\partial}{\partial \bar{z}_j}
$$

으로 작용한다. 실제로 $$J_p(\partial/\partial z_j) = \frac{1}{2}(J_p \partial/\partial x_j - i J_p \partial/\partial y_j) = \frac{1}{2}(\partial/\partial y_j + i\, \partial/\partial x_j) = i \cdot \frac{1}{2}(\partial/\partial x_j - i\, \partial/\partial y_j)$$이다. 전이함수 $$w = w(z)$$가 정칙이므로 Cauchy–Riemann 조건 $$\partial w_k / \partial \bar{z}_j = 0$$이 성립하고, 연쇄법칙에 의해 $$\partial/\partial z_j = \sum_k (\partial w_k/\partial z_j)\, \partial/\partial w_k$$로서 $$\partial/\partial w_k$$들만의 일차결합이 된다. 곧 $$J_p$$가 곱셈 $$i$$로 작용하는 부분공간 $$\span_{\mathbb{C}}\{\partial/\partial z_j\}$$은 좌표에 무관하게 같은 부분공간이고, 그 켤레도 마찬가지다. 따라서 $$J_p$$는 두 좌표계에서 같은 선형사상이다.

</details>

이 $$J$$가 곱셈 $$i$$를 그대로 옮긴 것임은 작용 $$J_p(\partial/\partial z_j) = i\, \partial/\partial z_j$$에서 분명하다. 거의 복소구조는 이렇게 복소다양체마다 표준적으로 따라오는 자료이지만, 그 역은 자명하지 않다. 임의로 주어진 거의 복소구조 $$J$$가 어떤 복소다양체의 표준 거의 복소구조와 일치하는가 하는 물음이 적분가능성 문제이며, 이를 정식화하려면 $$J$$의 고유공간 분해를 먼저 손에 쥐어야 한다.

## 복소화 접다발의 분해

거의 복소구조 $$J$$는 실 접공간 위의 사상이라 $$\pm i$$ 같은 복소 고유값을 직접 다룰 수 없다. 접공간을 복소화하면 $$J$$가 대각화되어 $$\pm i$$ 고유공간으로 갈라지고, 이 분해가 (p,q)-형식 분해의 출발점이 된다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> 거의 복소다양체 $$(M, J)$$의 점 $$p$$에서 *complexified tangent space<sub>복소화 접공간</sub>*를 $$T_p^{\mathbb{C}} M = T_p M \otimes_{\mathbb{R}} \mathbb{C}$$라 하고, $$J_p$$를 $$\mathbb{C}$$-선형으로 확장한 사상 (여전히 $$J_p$$로 적는다) 의 $$+i$$ 고유공간과 $$-i$$ 고유공간을 각각

$$
T_p^{1,0} M = \{ v \in T_p^{\mathbb{C}} M \mid J_p v = i v \}, \qquad
T_p^{0,1} M = \{ v \in T_p^{\mathbb{C}} M \mid J_p v = -i v \}
$$

으로 정의한다. $$T_p^{1,0} M$$의 벡터를 *(1,0)-vector*, $$T_p^{0,1} M$$의 벡터를 *(0,1)-vector*라 한다.

</div>

확장된 $$J_p$$도 $$J_p^2 = -\id$$을 만족하므로 그 최소다항식은 $$X^2 + 1 = (X-i)(X+i)$$를 나누고, 두 근 $$\pm i$$가 서로 다르므로 $$J_p$$는 대각화가능하다. 따라서 직합 분해

$$
T_p^{\mathbb{C}} M = T_p^{1,0} M \oplus T_p^{0,1} M
$$

이 성립한다. $$T_p^{\mathbb{C}} M$$ 위의 복소켤레 $$\overline{v \otimes \lambda} = v \otimes \bar{\lambda}$$는 $$J_p$$와 가환이 아니라 반가환($$J_p \bar{v} = \overline{J_p v}$$를 쓰면 $$+i$$ 고유벡터의 켤레는 $$-i$$ 고유벡터)이므로, 켤레는 두 고유공간을 맞바꾼다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> 복소켤레는 $$\overline{T_p^{1,0} M} = T_p^{0,1} M$$을 만족한다. 따라서 두 부분공간은 같은 복소차원 $$n$$을 가진다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$v \in T_p^{1,0} M$$이면 $$J_p v = i v$$이다. $$J_p$$는 실 사상의 복소선형 확장이므로 켤레와 교환한다는 의미에서 $$J_p \bar{v} = \overline{J_p v} = \overline{i v} = -i \bar{v}$$이다. 따라서 $$\bar{v} \in T_p^{0,1} M$$이고 $$\overline{T_p^{1,0} M} \subseteq T_p^{0,1} M$$이다. 켤레는 대합($$\bar{\bar{v}} = v$$)이므로 반대 포함도 같은 논법으로 성립하여 $$\overline{T_p^{1,0} M} = T_p^{0,1} M$$이다. 켤레는 $$\mathbb{R}$$-선형 동형이므로 두 부분공간의 복소차원이 같고, 그 합이 $$\dim_{\mathbb{C}} T_p^{\mathbb{C}} M = 2n$$이므로 각각 $$n$$이다.

</details>

복소다양체의 표준 거의 복소구조에 대해서는 이 추상적 분해가 정칙접공간과 정확히 일치한다. 명제 3의 증명에서 $$J_p(\partial/\partial z_j) = i\, \partial/\partial z_j$$이고 $$J_p(\partial/\partial \bar{z}_j) = -i\, \partial/\partial \bar{z}_j$$임을 보았으므로,

$$
T_p^{1,0} M = \span_{\mathbb{C}}\left\{ \frac{\partial}{\partial z_1}, \ldots, \frac{\partial}{\partial z_n} \right\}, \qquad
T_p^{0,1} M = \span_{\mathbb{C}}\left\{ \frac{\partial}{\partial \bar{z}_1}, \ldots, \frac{\partial}{\partial \bar{z}_n} \right\}
$$

이 되어, 복소다양체에서 좌표로 도입했던 정칙·반정칙 접공간 ([§복소다양체, ⁋정의 10](/ko/math/complex_geometry/complex_manifolds#def10)) 과 일치한다. 거의 복소구조의 언어는 이 분해를 좌표 없이, 고유공간으로 규정한다.

쌍대 쪽에서도 같은 분해가 일어난다. 복소화 여접공간 $$T_p^{\ast\mathbb{C}} M = T_p^\ast M \otimes_{\mathbb{R}} \mathbb{C}$$ 위에 $$J_p$$의 전치를 작용시키면, $$+i$$ 고유공간 $$\Lambda^{1,0}_p$$과 $$-i$$ 고유공간 $$\Lambda^{0,1}_p$$으로 갈라진다. $$\Lambda^{1,0}_p$$은 $$T_p^{0,1} M$$ 위에서 소멸하는 (1,0)-covector들, $$\Lambda^{0,1}_p$$은 $$T_p^{1,0} M$$ 위에서 소멸하는 (0,1)-covector들로 이루어진다. 표준 거의 복소구조에서는 $$\Lambda^{1,0}_p = \span_{\mathbb{C}}\{dz_j\}$$, $$\Lambda^{0,1}_p = \span_{\mathbb{C}}\{d\bar{z}_j\}$$이다.

## (p,q)-형식

여접공간의 분해를 외대수로 끌어올리면 복소화 미분형식이 차수별로 정밀하게 갈라진다. 이 (p,q)-분해는 적분가능성을 미분형식의 언어로 옮기는 데 쓰이며, 더 나아가 Dolbeault 이론 전체의 무대가 된다.

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> 거의 복소다양체 $$(M, J)$$ 위의 복소화 미분형식의 다발을 $$\Lambda^k_{\mathbb{C}} = \bigwedge^k (T^\ast M) \otimes_{\mathbb{R}} \mathbb{C}$$라 하자. 음이 아닌 정수 $$p, q$$에 대하여 *(p,q)-form<sub>(p,q)-형식</sub>*의 다발 $$\Lambda^{p,q}$$을 각 점에서

$$
\Lambda^{p,q}_p = \left( \bigwedge\nolimits^p \Lambda^{1,0}_p \right) \wedge \left( \bigwedge\nolimits^q \Lambda^{0,1}_p \right)
$$

으로 정의한다. $$\Lambda^{p,q}$$의 매끄러운 단면 전체를 $$\Omega^{p,q}(M)$$으로 적는다.

</div>

말하자면 $$(p,q)$$-형식은 (1,0)-covector $$p$$개와 (0,1)-covector $$q$$개를 wedge한 것들의 $$\mathbb{C}$$-선형결합이다. 표준 거의 복소구조에서는 국소적으로

$$
\Omega^{p,q}(M) \ni \omega = \sum_{\lvert I \rvert = p,\ \lvert J \rvert = q} f_{IJ}\, dz_{i_1} \wedge \cdots \wedge dz_{i_p} \wedge d\bar{z}_{j_1} \wedge \cdots \wedge d\bar{z}_{j_q}
$$

꼴로 적힌다. 여기서 $$I = (i_1 < \cdots < i_p)$$, $$J = (j_1 < \cdots < j_q)$$는 증가 다중지표이고 $$f_{IJ}$$는 매끄러운 복소함수이다. $$\bigwedge^p \Lambda^{1,0}$$의 복소차원이 $$\binom{n}{p}$$, $$\bigwedge^q \Lambda^{0,1}$$의 복소차원이 $$\binom{n}{q}$$이므로 $$\Lambda^{p,q}$$의 fiber 복소차원은 $$\binom{n}{p}\binom{n}{q}$$이다.

이 자료가 복소화 미분형식 전체를 차수별로 분해한다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> 거의 복소다양체 $$(M, J)$$에서 복소화 $$k$$-형식의 다발은 직합

$$
\bigwedge\nolimits^k (T^\ast M) \otimes_{\mathbb{R}} \mathbb{C} = \bigoplus_{p + q = k} \Lambda^{p,q}
$$

으로 분해된다. 단면 수준에서 $$\Omega^k(M) \otimes_{\mathbb{R}} \mathbb{C} = \bigoplus_{p+q=k} \Omega^{p,q}(M)$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

각 점 $$p$$에서 [명제 5](#prop5)의 쌍대 버전으로 $$T_p^{\ast\mathbb{C}} M = \Lambda^{1,0}_p \oplus \Lambda^{0,1}_p$$이다 (여접공간 위의 $$J_p$$ 전치도 $$\pm i$$ 고유공간 분해를 가진다). 직합으로 분해된 벡터공간 $$W = W' \oplus W''$$의 외대수는

$$
\bigwedge\nolimits^k W = \bigoplus_{p+q=k} \left( \bigwedge\nolimits^p W' \right) \wedge \left( \bigwedge\nolimits^q W'' \right)
$$

으로 분해된다 (외대수의 보편성에서 따라오는 표준 동형이다). $$W = T_p^{\ast\mathbb{C}} M$$, $$W' = \Lambda^{1,0}_p$$, $$W'' = \Lambda^{0,1}_p$$에 적용하면 우변의 $$(p,q)$$-항이 정확히 $$\Lambda^{p,q}_p$$이므로 점별 분해를 얻는다. 이 분해가 점에 대해 매끄럽게 변하므로 다발의 직합 분해가 되고 ([\[미분다양체\] §미분형식, ⁋정의 1](/ko/math/manifolds/differential_forms#def1)의 $$\Omega^k$$를 복소화한 것이다), 단면을 취하면 $$\Omega^k(M)\otimes\mathbb{C}$$의 분해가 된다.

</details>

이 분해 자체는 임의의 거의 복소구조에서 성립하므로, 거의 복소구조만 있으면 (p,q)-형식을 말할 수 있다. 그러나 외미분 $$d$$가 이 분해와 어떻게 어울리는가는 거의 복소구조가 적분가능한지에 달려 있다. 적분가능성이 바로 이 어긋남을 재는 척도이며, 다음 절에서 그 정밀한 동치들을 세운다.

## 적분가능성과 Nijenhuis 텐서

복소다양체의 표준 거의 복소구조 $$J$$에 대해서는 $$T^{1,0} M$$이 좌표 벡터장 $$\partial/\partial z_j$$들로 생성되고, 이들의 Lie bracket이 다시 $$\partial/\partial z_k$$들의 결합이므로 $$T^{1,0} M$$이 Lie bracket에 대해 닫힌다. 거꾸로 이 닫힘성이 $$J$$가 복소구조에서 옴을 보장하는가 하는 물음이 적분가능성이다. 먼저 적분가능성을 정의하고, 그것을 Lie bracket 닫힘성과 동치인 텐서 조건으로 옮긴다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> 거의 복소다양체 $$(M, J)$$의 거의 복소구조 $$J$$가 *integrable<sub>적분가능</sub>*하다는 것은, $$M$$ 위에 복소다양체 구조가 존재하여 그 표준 거의 복소구조 ([명제 3](#prop3)) 가 $$J$$와 일치하는 것이다.

</div>

적분가능성은 정의상 복소구조의 존재라는 대역적 조건이지만, 놀랍게도 순전히 국소적인 미분 조건으로 판정된다. 그 판정량이 Nijenhuis 텐서이다. (1,0)-벡터장들의 Lie bracket이 다시 (1,0)이 되는가, 곧 분포 $$T^{1,0} M$$이 *involutive<sub>대합적</sub>* 한가를 재기 위해, 켤레로 닫힌 실 형식의 양으로 옮긴 것이 Nijenhuis 텐서이다.

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> 거의 복소다양체 $$(M, J)$$의 *Nijenhuis tensor<sub>Nijenhuis 텐서</sub>* $$N_J$$는 두 벡터장 $$X, Y \in \mathfrak{X}(M)$$에 대하여

$$
N_J(X, Y) = [X, Y] + J[JX, Y] + J[X, JY] - [JX, JY]
$$

으로 정의되는 $$\mathfrak{X}(M) \times \mathfrak{X}(M) \to \mathfrak{X}(M)$$ 사상이다. 여기서 $$[-,-]$$은 벡터장의 Lie bracket이다 ([\[미분다양체\] §리 미분, ⁋정의 5](/ko/math/manifolds/Lie_derivative#def5)).

</div>

표현식에 Lie bracket이 들어 있어 처음에는 미분연산자처럼 보이지만, 실제로는 함수에 대해 $$C^\infty(M)$$-쌍선형이어서 각 점에서의 값이 그 점에서의 $$X_p, Y_p$$에만 의존한다. 곧 $$N_J$$는 진짜 텐서이다.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> Nijenhuis 텐서 $$N_J$$는 두 변수 모두에서 $$C^\infty(M)$$-선형이고 반대칭이다. 따라서 각 점 $$p$$에서 $$N_J(X, Y)\vert_p$$는 $$X_p, Y_p$$에만 의존하는 $$(2,1)$$-텐서를 정의한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

반대칭 $$N_J(X,Y) = -N_J(Y,X)$$은 Lie bracket의 반대칭성에서 항별로 즉시 따라온다. $$C^\infty(M)$$-선형성은 첫 변수에서 보이면 충분하다 (반대칭으로 둘째도 따라온다). $$f \in C^\infty(M)$$에 대하여 Lie bracket의 곱규칙 $$[fX, Y] = f[X,Y] - (Yf) X$$을 각 항에 적용한다. 네 항을 전개하면

$$
\begin{aligned}
[fX, Y] &= f[X,Y] - (Yf)\, X, \\
J[J(fX), Y] = J[fJX, Y] &= f\, J[JX, Y] - (Yf)\, J(JX) = f\, J[JX,Y] + (Yf)\, X, \\
J[fX, JY] &= f\, J[X, JY] - ((JY)f)\, JX, \\
[J(fX), JY] = [fJX, JY] &= f\, [JX, JY] - ((JY)f)\, JX
\end{aligned}
$$

이다. 둘째 줄에서 $$J(JX) = -X$$를 썼다. 이제 $$N_J(fX, Y) = [fX,Y] + J[J(fX),Y] + J[fX, JY] - [J(fX), JY]$$에 대입하면, $$f$$가 곱해진 항들의 합은 정확히 $$f\, N_J(X,Y)$$이고, 미분이 떨어진 보정항들은

$$
-(Yf) X + (Yf) X - ((JY)f) JX + ((JY)f) JX = 0
$$

으로 상쇄된다. 따라서 $$N_J(fX, Y) = f\, N_J(X, Y)$$이다. 덧셈 보존은 Lie bracket의 가법성에서 명백하므로 $$N_J$$는 $$C^\infty(M)$$-선형이고, 점별로 결정되는 텐서이다.

</details>

이제 핵심 동치를 세운다. Nijenhuis 텐서의 소멸은 (1,0)-분포의 대합성과 같은 내용이며, 이는 다시 외미분이 (p,q)-분해를 한 칸 어긋남까지만 흩뜨린다는 형식 조건과 같다.

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> 거의 복소다양체 $$(M, J)$$에 대하여 다음 세 조건은 서로 동치이다.

1. $$N_J = 0$$.
2. $$T^{1,0} M$$이 *involutive*하다. 곧 임의의 (1,0)-벡터장 $$Z, W$$에 대하여 $$[Z, W]$$도 다시 (1,0)-벡터장이다.
3. $$d(\Omega^{1,0}(M)) \subseteq \Omega^{2,0}(M) \oplus \Omega^{1,1}(M)$$.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

(1) ⟺ (2)를 보인다. 임의의 실 벡터장 $$X$$에 대하여 $$Z = X - i J X$$로 두면 $$J Z = J X + i X = i(X - iJX) = i Z$$이므로 $$Z \in T^{1,0} M$$이고, 모든 (1,0)-벡터장은 이런 꼴이다 ($$T^{1,0}$$으로의 사영이 $$X \mapsto \frac12(X - iJX)$$이므로). 두 (1,0)-벡터장 $$Z = X - iJX$$, $$W = Y - iJY$$의 Lie bracket을 전개하면

$$
[Z, W] = [X, Y] - [JX, JY] - i\big( [JX, Y] + [X, JY] \big).
$$

$$[Z,W]$$가 다시 (1,0)이려면 $$J[Z,W] = i[Z,W]$$, 동치로 $$[Z,W]$$의 (0,1)-성분이 $$0$$이어야 한다. $$[Z,W]$$의 (0,1)-성분은 $$\frac12([Z,W] + i J[Z,W])$$이고, 직접 계산하면

$$
[Z,W] + iJ[Z,W] = N_J(X,Y) + i J\, N_J(X,Y)
$$

가 성립한다 (위 $$[Z,W]$$ 전개식에 $$J$$를 작용시키고 $$N_J$$의 정의식과 맞춰 보면 항들이 정확히 떨어진다). 따라서 $$[Z,W]$$가 (1,0)이 될 필요충분조건은 $$N_J(X,Y) + iJ N_J(X,Y) = 0$$이고, $$N_J$$는 실 벡터장이므로 이는 $$N_J(X,Y) = 0$$과 동치이다. $$X, Y$$가 임의였으므로 (1) ⟺ (2)이다.

(2) ⟺ (3)을 보인다. 실 벡터장에 대한 외미분의 항등식

$$
d\alpha(U, V) = U(\alpha(V)) - V(\alpha(U)) - \alpha([U, V])
$$

을 (1,0)-형식 $$\alpha \in \Omega^{1,0}(M)$$과 두 (0,1)-벡터장 $$\bar{Z}, \bar{W}$$에 적용하자. $$\alpha$$는 (0,1)-벡터장 위에서 소멸하므로 $$\alpha(\bar{Z}) = \alpha(\bar{W}) = 0$$이고, 따라서

$$
d\alpha(\bar{Z}, \bar{W}) = -\alpha([\bar{Z}, \bar{W}]).
$$

$$d\alpha$$의 (0,2)-성분이 $$0$$이라는 것은 모든 (1,0)-형식 $$\alpha$$와 모든 (0,1)-벡터장 쌍에 대해 좌변이 $$0$$이라는 것과 같고, 위 식에서 이는 $$[\bar{Z}, \bar{W}]$$에 (1,0)-성분이 없다는 것, 곧 $$[\bar Z, \bar W]$$가 다시 (0,1)이라는 것과 동치이다. 켤레를 취하면 이는 $$T^{1,0}M$$의 involutivity와 같다. 한편 $$d\alpha$$는 $$2$$-형식이므로 (2,0)+(1,1)+(0,2)로 분해되며, $$d(\Omega^{1,0}) \subseteq \Omega^{2,0}\oplus\Omega^{1,1}$$은 정확히 (0,2)-성분의 소멸을 뜻한다. 따라서 (2) ⟺ (3)이다.

</details>

이로써 적분가능성의 후보 판정량이 갖춰졌다. 조건 (2)는 적분가능성과 곧바로 이어진다. 만약 $$J$$가 복소구조에서 온다면 $$T^{1,0} M$$이 $$\partial/\partial z_j$$들로 생성되고 $$[\partial/\partial z_j, \partial/\partial z_k] = 0$$이므로 involutive하다. 곧 적분가능성은 $$N_J = 0$$을 함의한다. 진짜 깊이는 그 역, 곧 $$N_J = 0$$이 복소구조의 존재를 보장한다는 데 있으며, 이것이 Newlander–Nirenberg 정리이다.

## Newlander–Nirenberg 정리

분포의 involutivity가 적분다양체를 낳는다는 것은 실 영역에서 Frobenius 정리의 내용이다. 그러나 $$T^{1,0} M$$은 복소 분포이고 그 적분다양체가 정칙좌표를 주어야 하므로, 실 Frobenius 정리만으로는 부족하다. Newlander와 Nirenberg는 매끄러운 경우에 대해 이 정칙 적분가능성이 정확히 $$N_J = 0$$과 동치임을 증명했다.

<div class="proposition" markdown="1">

<ins id="thm12">**정리 12 (Newlander–Nirenberg)**</ins> 거의 복소다양체 $$(M, J)$$의 거의 복소구조 $$J$$가 적분가능할 필요충분조건은 $$N_J = 0$$이다. 곧 $$N_J = 0$$이면 $$M$$ 위에 유일한 복소다양체 구조가 존재하여 그 표준 거의 복소구조가 $$J$$와 일치한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

필요성은 이미 보았다. $$J$$가 복소구조에서 오면 [명제 11](#prop11)의 조건 (2)가 성립하고, 동치인 (1)에 의해 $$N_J = 0$$이다.

충분성이 정리의 본체이며 증명은 길고 해석적이므로 핵심 구조만 적는다. $$N_J = 0$$이라 가정하면 [명제 11](#prop11)에 의해 복소 분포 $$T^{1,0} M$$이 involutive하다. 보이고자 하는 바는 각 점 둘레에 국소 복소좌표 $$z_1, \ldots, z_n$$이 존재하여 $$d z_j$$들이 $$\Lambda^{1,0}$$을 점별 생성하는 것, 동치로 정칙함수처럼 행동하는 좌표 $$z_j$$ (곧 $$\bar{Z} z_j = 0$$이 모든 (0,1)-벡터장 $$\bar{Z}$$에 대해 성립) 가 충분히 많이 존재하는 것이다.

실해석적($$C^\omega$$) 경우에는 이것이 복소화 Frobenius 정리로 곧장 따라온다. 계수를 복소수로 확장한 holomorphic 영역에서 involutive 복소 분포는 적분다양체를 가지며, 이 적분다양체들의 횡단 좌표가 바라던 $$z_j$$를 준다. 이 논법은 Cauchy–Kovalevskaya 정리에 기대므로 해석성을 본질적으로 쓴다.

매끄러운($$C^\infty$$) 경우에는 해석성이 없어 위 논법이 작동하지 않으며, 이것이 Newlander–Nirenberg의 진짜 기여이다. 차원에 대한 귀납과 편미분방정식계의 풀이를 결합하여, $$N_J = 0$$이라는 적분가능성 조건이 보장하는 상삼각 구조 아래에서 비선형 $$\bar\partial$$-형 방정식 $$\bar{Z} z_j = 0$$의 충분히 많은 해를 국소적으로 구성한다. 원논문은 비선형 타원계의 선형화와 Newlander–Nirenberg 추정으로 이 해의 존재와 정칙 의존성을 얻는다. 이렇게 얻은 좌표 $$z_j$$들의 전이함수는 $$\bar\partial z_j = 0$$을 만족하므로 정칙이고, 따라서 이 좌표들이 $$M$$ 위에 복소다양체 구조를 정의한다. 구성에서 $$d z_j$$가 $$\Lambda^{1,0}$$을 생성하므로 그 표준 거의 복소구조는 $$J$$와 일치한다.

유일성은 두 복소구조가 같은 $$J$$를 주면 두 좌표계의 전이함수가 양쪽 모두에서 $$\bar\partial$$를 죽여 정칙이 되고, 따라서 두 복소구조가 양립가능하다는 데서 따라온다.

</details>

이 정리는 거의 복소다양체의 미분기하와 복소다양체의 정칙기하 사이를 잇는 다리이다. 적분가능성이라는 대역적·해석적 조건이 Nijenhuis 텐서라는 점별 텐서의 소멸로 환원되므로, 주어진 $$J$$가 복소구조에서 오는지를 국소 계산만으로 판정할 수 있다. 실차원 $$2$$에서는 $$N_J$$가 반대칭 $$(2,1)$$-텐서인데 $$\binom{2}{2} = 1$$차원 입력 공간에서 반대칭성이 강하여 $$N_J$$가 항상 $$0$$이 된다. 곧 모든 거의 복소구조가 적분가능하며, 향위 곡면(orientable surface) 위의 거의 복소구조는 언제나 복소구조, 곧 리만 곡면 구조를 준다. 차원이 올라가면 $$N_J \neq 0$$인 거의 복소구조가 풍부하게 나타나, 적분가능성이 진정한 제약이 된다.

## 예시

가장 단순한 예는 평탄한 경우이다.

<div class="example" markdown="1">

<ins id="ex13">**예시 13 ($$\mathbb{R}^{2n} = \mathbb{C}^n$$의 표준 $$J$$)**</ins> $$\mathbb{R}^{2n}$$에 좌표 $$(x_1, y_1, \ldots, x_n, y_n)$$를 주고

$$
J_0\!\left( \frac{\partial}{\partial x_j} \right) = \frac{\partial}{\partial y_j}, \qquad
J_0\!\left( \frac{\partial}{\partial y_j} \right) = -\frac{\partial}{\partial x_j}
$$

으로 상수계수 거의 복소구조 $$J_0$$를 정의하면, 이는 동일시 $$z_j = x_j + i y_j$$로 $$\mathbb{R}^{2n} = \mathbb{C}^n$$에 준 복소구조의 표준 $$J$$이다. $$J_0$$의 성분이 상수이므로 모든 Lie bracket이 소멸하여 $$N_{J_0} = 0$$이고, 따라서 적분가능하다. 이는 $$\mathbb{C}^n$$이 복소다양체라는 사실의 거의 복소구조 버전이다.

</div>

콤팩트한 예로 가장 기본적인 것은 리만 구면이다.

<div class="example" markdown="1">

<ins id="ex14">**예시 14 ($$S^2 \cong \mathbb{CP}^1$$)**</ins> $$2$$차원 구면 $$S^2$$는 복소다양체 $$\mathbb{CP}^1$$의 바탕 매끄러운 다양체이며 ([§복소다양체, ⁋예시 9](/ko/math/complex_geometry/complex_manifolds#ex9)), 그 표준 거의 복소구조는 적분가능하다. 더 일반적으로 위 정리 12 직후의 관찰에 따라, $$S^2$$ 위의 임의의 거의 복소구조는 실차원 $$2$$이므로 $$N_J = 0$$을 자동으로 만족하여 적분가능하다. 따라서 $$S^2$$ 위의 모든 거의 복소구조는 어떤 리만 곡면 구조에서 온다.

</div>

적분불가능성이 처음 본격적으로 나타나는 것은 $$S^6$$이다.

<div class="example" markdown="1">

<ins id="ex15">**예시 15 ($$S^6$$의 octonion 거의 복소구조)**</ins> $$6$$차원 구면 $$S^6$$는 거의 복소구조를 가진다. 이를 octonion $$\mathbb{O}$$의 곱셈으로부터 다음과 같이 구성한다. $$\mathbb{O}$$의 순허수부 $$\Img \mathbb{O} \cong \mathbb{R}^7$$ 안의 단위구면이 $$S^6$$이고, 점 $$p \in S^6$$에서의 접공간 $$T_p S^6$$은 $$p$$에 직교하는 $$\Img \mathbb{O}$$의 부분공간이다. 여기서 $$J_p(v) = p \cdot v$$ (octonion 곱) 로 정의하면 $$J_p^2(v) = p \cdot (p \cdot v) = -v$$가 octonion 항등식에서 따라오므로 $$J_p^2 = -\id$$이고, $$J$$는 거의 복소구조이다. 그러나 이 표준 거의 복소구조는 *적분불가능*하다. 곧 $$N_J \neq 0$$이며, 직접 계산으로 octonion의 비결합성이 정확히 $$N_J$$의 비소멸로 나타남을 확인할 수 있다. 한편 $$S^6$$ 위에 (이 $$J$$와는 다른) 적분가능 거의 복소구조, 곧 복소다양체 구조가 아예 존재하는가 하는 물음은 오랫동안 미해결 문제로 남아 있다.

</div>

마지막으로 거의 복소구조의 존재 자체가 위상적 제약을 받는다는 사실을 짚는다. 짝수차원은 명제 2에 따라 필요조건이지만 충분하지 않다.

<div class="example" markdown="1">

<ins id="ex16">**예시 16 ($$S^4$$에는 거의 복소구조가 없다)**</ins> $$4$$차원 구면 $$S^4$$는 짝수차원이지만 거의 복소구조를 전혀 갖지 못한다. 거의 복소구조 $$J$$가 있으면 접다발 $$TS^4$$이 복소 벡터다발 구조를 가져 Chern class가 정의되고, 특히 실 Pontryagin·Euler class가 Chern class로 표현되어야 한다. 그러나 $$S^4$$의 코호몰로지 ([\[대수적 위상수학\] §코호몰로지](/ko/math/algebraic_topology/cohomology)) 는 차수 $$0$$과 $$4$$에만 자명하지 않은 부분을 가지므로 중간 차수의 Chern class가 들어설 자리가 없고, Euler 수 $$\chi(S^4) = 2$$와 서명 $$\sigma(S^4) = 0$$이 거의 복소다양체가 만족해야 하는 관계식 $$c_1^2 = 2\chi + 3\sigma$$와 양립하지 못한다. $$S^4$$에서는 좌변이 $$0$$이어야 하는데 우변은 $$4$$이므로 모순이다. 따라서 $$S^4$$ 위에는 거의 복소구조가 없으며, 거의 복소구조의 존재는 순수한 위상적 장애를 동반한다.

</div>

이 마지막 두 예는 거의 복소구조의 위계를 보여준다. $$S^4$$는 거의 복소구조조차 갖지 못하고, $$S^6$$는 거의 복소구조는 갖지만 그 표준적인 것이 적분가능하지 않으며 (복소구조의 존재 여부는 미결), $$S^2$$는 거의 복소구조가 언제나 적분가능하다. 거의 복소구조에서 복소구조로 가는 다리가 Newlander–Nirenberg 정리이고, 그 다리를 건널 수 있는지를 가르는 척도가 Nijenhuis 텐서이다. 적분가능한 거의 복소구조 위에서 외미분이 (p,q)-분해와 맞물려 $$\partial$$와 $$\bar\partial$$로 갈라지는 정밀한 구조는 Dolbeault 코호몰로지에서 본격적으로 다룬다.

---

**참고문헌**

**[Huybrechts]** D. Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005.

**[Griffiths–Harris]** P. Griffiths and J. Harris, *Principles of Algebraic Geometry*, Wiley, 1978.

**[Kobayashi–Nomizu]** S. Kobayashi and K. Nomizu, *Foundations of Differential Geometry, Vol. II*, Wiley, 1969.

**[Newlander–Nirenberg]** A. Newlander and L. Nirenberg, *Complex analytic coordinates in almost complex manifolds*, Ann. of Math. **65** (1957), 391–404.

**[Moroianu]** A. Moroianu, *Lectures on Kähler Geometry*, Cambridge University Press, 2007.
