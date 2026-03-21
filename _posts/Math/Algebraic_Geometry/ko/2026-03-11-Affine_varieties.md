---
title: "아핀다양체"
excerpt: "Affine varieties and their basic properties"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/affine_varieties
sidebar:
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Affine_Zarieties.png
    overlay_filter: 0.5

date: 2026-03-11
last_modified_at: 2026-03-18
weight: 1

---

대수기하학에서 우리의 목표는 다항식으로 정의되는 기하적 대상들을 연구하는 것이다. 구체적으로, field $$\mathbb{K}$$와 자연수 $$n$$이 주어졌을 때, 우리는 다음의 식

$$Z(f)= \{(x_1, \ldots, x_n) \in \mathbb{A}^n \mid f(x_1, \ldots, x_n) = 0\},\qquad f\in \mathbb{K}[\x_1,\ldots, \x_n]$$

으로 주어지는 집합들에 관심이 있다. 이는 $$\mathbb{K}^n$$에서 다항식 $$f$$의 근들의 모임이다. 일반적으로 $$\mathbb{K}=\mathbb{C}$$로 두며, 이러한 가정에서 특히 좋은 것은 $$\mathbb{C}$$이 [algebraically closed](/ko/math/general/algebraically_closed_field)라는 사실이다. 그러나, 대부분의 경우 이렇게 가정하는 것이 큰 도움이 되지는 않으므로 우리는 더 일반적인 세팅을 사용하기로 한다. 또, 혼동을 방지하기 위하여 다항식 $$f$$의 변수는 정자 $$\x$$와 같은 식으로 표기할 것이다.

## 아핀다양체의 정의

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Field $$\mathbb{K}$$ 위에 정의된 *affine $n$-space<sub>$n$차원 아핀공간</sub>* $$\mathbb{A}^n_\mathbb{K}$$는 $$n$$차원 벡터공간 $$\mathbb{K}^n$$을 의미한다.

</div>

맥락상 $$\mathbb{K}$$를 생략해도 될 때는 $$\mathbb{A}^n$$과 같이 적는다. 우리는 affine space

$$\mathbb{A}^n=\{(x_1,\ldots, x_n)\mid x_i\in \mathbb{K}\}$$

의 원소를 *점<sub>point</sub>*이라 부르고, 각각의 좌표 $$x_i$$를 *$i$번째 좌표*라 부른다. 위에서 언급했듯, 우리가 살펴볼 기하적인 대상들은 다항식 $$f\in \mathbb{K}[\x_1,\ldots, \x_n]$$의 zero set $$Z(f)$$로 나타나는 대상들이다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 다항식 $$f_1, \ldots, f_k \in \mathbb{K}[\x_1, \ldots, \x_n]$$에 대하여, 이들이 정의하는 *affine algebraic set<sub>아핀 대수적 집합</sub>* $$Z(f_1, \ldots, f_k)$$를

$$Z(f_1, \ldots, f_k) = \{x=(x_1, \ldots, x_n) \in \mathbb{A}^n \mid f_1(x) = \cdots = f_k(x) = 0\}$$

으로 정의한다. Affine algebraic set들 가운데 그보다 더 작은 affine algebraic set들의 합집합으로 나타나지 않는 것들을 *affine variety<sub>아핀다양체</sub>*라 부른다.

</div>

즉, affine algebraic set은 여러 다항식들 $$f_1,\ldots, f_k$$의 common zero들의 모임이다. 더 일반적으로, $$\mathbb{K}[\x_1,\ldots, \x_n]$$의 부분집합 $$S$$에 대하여 $$Z(S)$$를 위의 정의와 비슷하게 정의할 수 있으며, 그럼 정의에 의해 $$S$$로 생성되는 $$\mathbb{K}[\x_1,\ldots, \x_n]$$의 ideal $$(S)$$는 식

$$Z(S)=Z((S))$$

을 만족한다. 따라서 우리는 ideal $$\mathfrak{a}$$들이 정의하는 affine algebraic set들만 신경써도 된다.

일반적으로 공간 $$X$$가 *irreducible*이라는 것은 $$X$$가 proper open subset 두 개의 합집합으로 나타나지 않는다는 것이다. ([\[위상수학\] §차원, ⁋정의 6](/ko/math/topology/dimension#def6)) 따라서 우리의 정의는 irreducible affine algebraic set을 affine variety라고 부른다는 뜻이다. 이는 기하학적으로 하나의 연결된 대상을 다루기 위함이다.

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> 우리가 아는 대다수의 기하학적인 대상들은 다항식으로 나타나므로, 이들이 모두 affine variety의 예시가 된다.

1. $$\mathbb{A}^2$$ 안에서 정의된 affine variety $$Z(\x^2+\y^2-1)$$을 생각하자. 정의에 의해, 이 집합은 식 $$\x^2+\y^2-1=0$$을 만족하는 $$\mathbb{A}^2$$의 점들의 모임이므로, 단위원을 나타낸다.
2. 일반적으로, 임의의 affine space $$\mathbb{A}^n$$와 임의의 다항식 $$f\in \mathbb{K}[\x_1,\ldots, \x_n]$$에 대하여, $$Z(f)$$는 *초곡면<sub>hypersurface</sub>*을 정의한다.
3. 또 다른 중요한 예시로, $$\mathbb{A}^3$$ 위에 정의된 *twisted cubic*이 있다. 이는 $$\mathbb{A}^3$$ 위에 정의된 두 다항식 $$\y-\x^2$$, $$\z-\x^3$$으로 정의되는 곡선으로, 매개화 $$(t,t^2,t^3)$$을 통해 $$\mathbb{A}^1$$과 일대일로 대응된다.
4. Affine space $$\mathbb{A}^n$$ 자기자신과 공집합은 affine variety이다. 이는 $$Z(0)=\mathbb{A}^n$$, $$Z(1)=\emptyset$$으로부터 자명하다. 이는 [명제 4](#prop4)에서 Zariski topology를 정의할 때 중요하게 사용된다.

</div>

위의 예시에서 우리는 친숙한 기하학적 대상들이 모두 집합으로서는 affine algebraic set으로 쓰여질 수 있음을 보았다. 그러나 이를 기하학적 대상이라 생각하기 위해서는 그 위에 위상구조가 존재해야 한다. 우리의 유일한 도구는 다항식이므로, 이를 사용하여 위상구조를 정의할 것이다. 

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> 다음이 성립한다.

1. $$Z(0) = \mathbb{A}^n$$,
2. $$Z(1) = \emptyset$$,
3. $$\mathfrak{a} \subseteq \mathfrak{b} \implies Z(\mathfrak{b}) \subseteq Z(\mathfrak{a})$$,
4. $$\displaystyle\bigcap_{i\in I} Z(\mathfrak{a}_i) = Z\left(\sum_i \mathfrak{a}_i\right)$$,
5. $$Z(\mathfrak{a}) \cup Z(\mathfrak{b}) = Z(\mathfrak{a} \cap \mathfrak{b}) = Z(\mathfrak{a}\mathfrak{b})$$.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

처음 두 명제는 [예시 3](#ex3)에서 이미 살펴보았다. 

세 번째 결과를 증명하기 위해, $$\mathfrak{a}\subseteq \mathfrak{b}$$라 하고 $$x\in Z(\mathfrak{b})$$라 하자. 그럼 모든 $$f \in \mathfrak{b}$$에 대해 $$f(x) = 0$$이고, $$\mathfrak{a} \subseteq \mathfrak{b}$$이므로 특히 모든 $$\mathfrak{a}$$의 원소에 대해서도 원하는 식이 성립한다.

네 번째 결과의 경우, 점 $$x$$가 모든 $$Z(\mathfrak{a}_i)$$에 속한다는 것은 모든 $$i$$와 모든 $$f \in \mathfrak{a}_i$$에 대해 $$f(x) = 0$$이라는 것이다. 이는 $$\sum_\alpha I_\alpha$$의 모든 원소가 $$p$$에서 0이라는 것과 동치이다.

이제 마지막 주장을 보이자. 우선 $$x\in Z(\mathfrak{a})\cup Z(\mathfrak{b})$$라 하자. 그럼 $$x\in Z(\mathfrak{a})$$이거나 $$x\in Z(\mathfrak{b})$$이며, 어느 경우든 $$\mathfrak{a}\cap \mathfrak{b}$$의 모든 원소는 $$x$$에서 $$0$$이므로 $$x\in Z(\mathfrak{a}\cap \mathfrak{b})$$이 성립한다.  
이제 $$x\in Z(\mathfrak{a}\cap \mathfrak{b})$$라 하면, $$\mathfrak{a}\mathfrak{b}$$의 임의의 원소

$$f_1g_1+\cdots+ f_kg_k,\qquad f_i\in \mathfrak{a}, g_i\in \mathfrak{b}$$

를 $$x$$에서 계산한 것이 $$0$$이 되는 것은 자명하다.  
마지막으로 $$x\in Z(\mathfrak{a}\mathfrak{b})$$라 하자. 만일 결론에 반하여 $$x\not\in Z(\mathfrak{a})\cup Z(\mathfrak{b})$$라면, 적당한 $$f\in \mathfrak{a}$$와 적당한 $$g\in \mathfrak{b}$$가 존재하여 $$f(x),g(x)\neq 0$$이다. 그런데, 만일 이것이 성립한다면 $$f(x)g(x)\neq 0$$이므로 $$x\in Z(\mathfrak{a}\mathfrak{b})$$라는 가정에 모순이다. 

</details>

우선 위 명제의 마지막 결과는 $$Z(\mathfrak{a}\mathfrak{b})$$가 algebraic variety이기 위해서는 반드시 $$\mathfrak{a}=1$$이거나 $$\mathfrak{b}=1$$이어야 함을 보여준다. 이는 algebraic variety가 무엇인지를 대수적으로 살펴보는데 좋은 직관 중 하나가 된다.

그보다 중요한 것은 위의 명제에 의해, 만일 $$\mathbb{A}^n$$ 위에서 정의된 affine algebraic set들을 닫힌집합이라고 선언한다면, [\[위상수학\] §집합의 내부, 폐포, 경계, ⁋명제 2](/ko/math/topology/other_concepts#prop2)의 조건들이 모두 만족되고 따라서 $$\mathbb{A}^n$$ 위의 위상구조가 유일하게 결정된다는 것이다. 이를 *Zariski topology<sub>자리스키 위상</sub>*이라 부른다. 정의에 의해 임의의 affine variety $$X$$는 적당한 affine space $$\mathbb{A}^n$$의 닫힌 부분집합이며, 우리는 $$\mathbb{A}^n$$에서 정의된 위상의 subspace topology를 통해 $$X$$에서의 위상을 정의할 수 있다. 

특별한 예시로 $$\mathbb{A}^1$$에서의 Zariski topology를 보면, $$\mathbb{K}$$의 임의의 원소는 일차식 $$\x-x$$의 zero set이므로 임의의 singleton은 닫힌집합이고, 따라서 임의의 유한집합은 닫힌집합이다. 그러나 $$\mathbb{K}[\x]$$의 임의의 원소는 많아야 유한 개의 근만을 가지므로, 이 위상구조 상에서는 ($$\mathbb{K}$$가 유한집합이 아닌 한) 무한한 원소를 가진 닫힌집합은 오직 $$\mathbb{K}$$ 자기자신 뿐이다. 즉 $$\mathbb{A}^1$$의 Zariski topology는 cofinite topology이며, 이로부터 우리는 Zariski topology가 Hausdorff일 필요가 없다는 것을 관찰할 수 있다. 더 일반적으로 irreducible space는 Hausdorff가 될 수 없고, 우리의 정의에서 affine variety들은 모두 irreducible이므로 임의의 affine variety는 Hausdorff space가 아니다. ([\[위상수학\] §차원, ⁋명제 7](/ko/math/topology/dimension#prop7))

이제 우리는 Zariski topology의 열린집합들을 살펴보자.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> 다항식 $$f \in \mathbb{K}[\x_1, \ldots, \x_n]$$에 대하여, *principal open set* $$D(f)$$를

$$D(f) = \{x\in \mathbb{A}^n \mid f(x) \ne 0\} = \mathbb{A}^n \setminus Z(f)$$

으로 정의한다.

</div>

다음 명제는 principal open set들이 affine variety의 base를 이룬다는 것을 보여준다. ([\[위상수학\] §위상공간의 기저, ⁋정의 1](/ko/math/topology/topological_bases#def1))

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> Affine variety $$X \subseteq \mathbb{A}^n$$의 임의의 열린집합 $$U$$에 대하여,

$$U = \bigcup_i (D(f_i) \cap X)$$

을 만족하는 principal open set들의 family $$D(f_i)$$가 존재한다. 

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Zariski topology의 정의에 의하여, 적당한 ideal $$\mathfrak{a}\subset \mathbb{K}[\x_1,\ldots, \x_n]$$가 존재하여 

$$X\setminus U=Z(\mathfrak{a})\cap X$$

이도록 할 수 있다. 따라서 

$$U = X \setminus (Z(\mathfrak{a}) \cap X) = X \cap (\mathbb{A}^n \setminus Z(\mathfrak{a}))$$

이다. 한편 $$\mathbb{A}^n \setminus Z(\mathfrak{a})$$는 $$f \in \mathfrak{a}$$에 대해 $$f(x) \ne 0$$인 점들의 집합이므로

$$\mathbb{A}^n \setminus Z(\mathfrak{a}) = \bigcup_{f \in \mathfrak{a}} D(f)$$

이다. 따라서 $$U = \bigcup_{f \in \mathfrak{a}} (D(f) \cap X)$$이다.

</details>

일반적으로 affine variety의 열린집합은 affine variety일 필요가 없으며, 실제로도 그렇지 않다. 그러나 affine variety의 principal open subset은 반드시 affine variety이다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> Affine variety $$X \subseteq \mathbb{A}^n$$과 다항식 $$f \in \mathbb{K}[\x_1, \ldots, \x_n]$$에 대하여, $$D(f) \cap X$$는 affine variety이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

적당한 ideal $$\mathfrak{a}$$를 택하여 $$X = Z(\mathfrak{a})$$라 하자. 우리는 $$D(f) \cap X$$를 $$\mathbb{A}^{n+1}$$의 affine variety로 표현할 것이다. 이를 위해 $$\mathbb{A}^{n+1}$$을 나타내는 좌표들을 

$$\x_1,\ldots, \x_n,\y$$

라 하고, $$\mathbb{K}[\x_1,\ldots, \x_n,\y]$$의 ideal

$$\mathfrak{b}=\mathfrak{a}+(1-f\y)$$

을 생각하자. 그럼 

$$Z(\mathfrak{b})=\{(x_1,\ldots, x_n, y)\in \mathbb{A}^{n+1}\mid x\in X, 1-f(x)y=0\}$$

이다. 이제 조건 $$1-f(x)y=0$$으로부터 $$f(x)\neq 0$$이고, $$y=1/f(x)$$임을 안다. 이로부터 다음의 bijection

$$(x_1,\ldots, x_n,y)\mapsto (x_1,\ldots, x_n)$$

을 얻는다. 이것이 homeomorphism인 것은 자명하다. 

</details>

이쯤에서 짚고 넘어가야 할 사실은, affine variety에 대한 우리의 정의가 엄밀하게는 ambient space $$\mathbb{A}^n$$에 의존한다는 사실이다. 가령 $$\mathbb{A}^1$$의 principal open set $$D(\x)$$는, 위의 명제에 따르면, affine variety이다. 그러나 우리는 이미 $$\mathbb{A}^1$$의 Zariski topology는 cofinite topology임을 살펴보았고, 따라서 $$D(\x)$$는 $$\mathbb{K}[\x]$$ 안에서의 다항식의 zero set들로 정의될 수 없다. 실제로 [명제 7](#prop7)의 증명을 뜯어보면, $$D(\x)$$가 affine variety라는 사실은 isomorphism

$$D(\x)\cong Z(\x\y-1)\subseteq \mathbb{A}^2$$

에 의해 얻어지는 결과이다. 이러한 문제는 regular function을 이해할 때 우리를 다소 헷갈리게 할 수 있으므로, 해당 부분에서 이 문제를 다시 짚어보기로 한다.

## 영점정리

[명제 4](#prop4)에서 살펴본 $$Z$$는 대수적인 대상들, 즉 $$\mathbb{K}[\x_1,\ldots, \x_n]$$의 다항식들을 기하적인 대상들, 즉 이들 다항식들이 정의하는 zero set으로 보내준다. 거꾸로 우리는 기하적인 대상을 받아 대수적인 대상들을 대응시켜줄 수도 있다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> 임의의 부분집합 $$X \subseteq \mathbb{A}^n$$에 대하여, $$\mathbb{K}[\x_1,\ldots, \x_n]$$의 부분집합 $$I(X)$$를

$$I(X) = \{f \in \mathbb{K}[\x_1, \ldots, \x_n] \mid f(a) = 0 \text{ for all } a \in X\}$$

으로 정의한다.

</div>

그럼 임의의 부분집합 $$X$$에 대하여, $$I(X)$$는 $$\mathbb{K}[\x_1,\ldots, \x_n]$$의 ideal이 된다는 것이 자명하다. 뿐만 아니라 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> $$\mathbb{A}^n$$의 부분집합들 $$X,Y$$, $$\mathbb{K}[\x_1,\ldots, \x_n]$$의 임의의 부분집합 $$I$$에 대하여 다음이 성립한다.

1. $$X \subseteq Y$$라면 $$I(Y) \subseteq I(X)$$이다.
2. $$I(\emptyset) = \mathbb{K}[\x_1, \ldots, \x_n]$$이다.
3. $$\mathbb{K}$$가 무한하다면 $$I(\mathbb{A}^n) = (0)$$이다.
4. $$X \subseteq Z(I(X))$$가 항상 성립한다.
5. $$I \subseteq I(Z(I))$$가 항상 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

1. $$X \subseteq Y$$이고 $$f \in I(Y)$$라면, 모든 $$a \in Y$$에 대해 $$f(a) = 0$$이다. 특히 모든 $$a \in X$$에 대해 $$f(a) = 0$$이므로 $$f \in I(X)$$이다.
2. 자명하다.
3. $$\mathbb{K}$$가 무한하다면, 모든 점에서 0인 다항식은 영다항식뿐이다.
4. $$a \in X$$이고 $$f \in I(X)$$라면 $$f(a) = 0$$이다. 즉 $$a \in Z(I(X))$$이다.
5. $$f \in I$$이고 $$a \in Z(I)$$라면 $$f(a) = 0$$이다. 즉 $$f \in I(Z(I))$$이다.

</details>

즉, $$Z$$와 $$I$$는 antitone Galois connection을 정의한다. ([\[집합론\] §필터와 아이디얼, 갈루아 대응, ⁋정의 6](/ko/math/set_theory/filter_and_ideal#def6)) 따라서 두 operator의 합성 $$ZI$$와 $$IZ$$ 각각은 closure operator를 정의한다. $$ZI$$의 경우, 이 closure는 실제로 Zariski topology에서의 closure가 된다. 이는 만일 $$X \subseteq Y = Z(J)$$이면 $$I(Z(J)) \subseteq I(X)$$이고, [명제 9](#prop9)의 5번 조건에서 $$J \subseteq I(Z(J))$$이므로 $$ZI(X) \subseteq Z(J) = Y$$가 되어, $$ZI(X)$$가 $$X$$를 포함하는 Zariski closed set 중 가장 작은 것이 되기 때문이다. $$IZ$$의 경우에는 바로 보이지 않는데, 이를 위해서는 ideal의 radical 개념이 필요하다. ([\[가환대수학\] §국소화의 성질들, ⁋정리 8](/ko/math/commutative_algebra/properties_of_localization#cor8))

<div class="proposition" markdown="1">

<ins id="thm10">**정리 10 (Nullstellensatz)**</ins> Algebraically closed field $$\mathbb{K}$$와 ideal $$\mathfrak{a}\subseteq \mathbb{K}[\x_1,\ldots, \x_n]$$이 주어졌다 하자. 그럼 

$$I(Z(\mathfrak{a}))=\sqrt{\mathfrak{a}}$$

이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[\[가환대수학\] §영점정리, ⁋명제 6](/ko/math/commutative_algebra/nullstellensatz#prop6)

</details>

이는 넓게 본다면 이미 [명제 4](#prop4)의 5번 조건으로부터

$$Z(\mathfrak{a}^k)=Z(\mathfrak{a}\cap\cdots\cap \mathfrak{a})=Z(\mathfrak{a})$$

이므로, 어느정도 예견된 결과라고 할 수도 있다.

한편, $$\mathfrak{a}\subseteq \sqrt{\mathfrak{a}}$$가 임의의 ideal $$\mathfrak{a}$$에 대해 성립하므로 [명제 4](#prop4)의 셋째 조건으로부터 $$Z(\sqrt{\mathfrak{a}})\subseteq Z(\mathfrak{a})$$임을 안다. 그런데 정의에 의하여 임의의 $$f\in \sqrt{\mathfrak{a}}$$가 주어졌을 때, 적당한 $$r$$이 존재하여 $$f^r\in \mathfrak{a}$$이다. 따라서 $$x\in Z(\mathfrak{a})$$라면 $$Z(\sqrt{\mathfrak{a}})$$여야 하고 이로부터 $$Z(\mathfrak{a})=Z(\sqrt{\mathfrak{a}})$$임을 안다. 즉 ideal의 radical은 affine algebraic set을 ideal의 zero set으로 나타낼 때, 이 ideal을 얻어내는 표준적인 방법을 주는 것으로 생각할 수 있으며, 이들 사이의 차이를 구별하기 위해서는 *scheme*을 정의하면 된다. 

이제 [명제 4](#prop4)의 다섯번째 결과와 위의 결과를 종합하면, 우리는 $$Z(\mathfrak{a})$$가 algebraic variety이기 위해서는 $$\sqrt{\mathfrak{a}}$$가 prime ideal이어야 함을 알 수 있다. ([\[가환대수학\] §기본 개념들, ⁋정의 10](/ko/math/commutative_algebra/basic_notions#def10)) 즉, $$\mathbb{A}^n$$의 irreducible closed algebraic set들과 $$\mathbb{K}[\x_1,\ldots, \x_n]$$ 사이의 Galois correspondence가 존재한다. 

## 좌표환과 정칙성

우리는 양방향의 대응 $$Z$$, $$I$$가 담고 있는 철학을 더 확장시킬 수 있다. 구체적으로, $$\mathbb{A}^n$$의 기하학은 그 정의에 의해 $$\mathbb{K}[\x_1,\ldots, \x_n]$$의 원소들이 담고 있다. 역으로, $$\mathbb{A}^n$$의 임의의 점 $$x=(x_1,\ldots, x_n)$$를 받아 $i$번째 좌표를 내놓는 함수를 $$\x_i: x\mapsto x_i$$으로 생각할 수 있으며, 이러한 관점에서 $$\mathbb{K}[\x_1,\ldots, \x_n]$$의 모든 원소들을 $$\mathbb{A}^n$$ 위에 정의된 (다항식) 함수로 볼 수 있다. 

더 일반적으로 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="def11">**정의 11**</ins> Affine variety $$X = Z(\mathfrak{a}) \subseteq \mathbb{A}^n$$의 *coordinate ring<sub>좌표환</sub>* $$\mathbb{K}[X]$$를

$$\mathbb{K}[X] = \mathbb{K}[\x_1, \ldots, \x_n] / I(X)=\mathbb{K}[\x_1, \ldots, \x_n] / \sqrt{\mathfrak{a}}$$

으로 정의한다. 이 원소들을 $$X$$ 위에 정의된 *regular function<sub>정칙함수</sub>*이라 부른다.

</div>

Coordinate ring을 정의하는 이유는, 대수기하의 핵심 철학, 즉 기하학적 대상 $$X$$와 대수적 대상 $$\mathbb{K}[X]$$의 대응을 구현하기 위해서이다. $$X$$의 모든 기하학적 정보, 가령 점들, 다항식 함수들의 관계, 부분집합들의 포함 관계 등은 모두 $$\mathbb{K}[X]$$의 ring structure에 인코딩되며, 이는 나중에 affine variety들 사이의 morphism을 coordinate ring homomorphism으로 번역하는 기반이 된다. 

$$X$$가 어떤 다항식들의 영점으로 정의되었다면, $$\mathbb{K}[X]$$는 이러한 다항식 관계들을 factor out한 나머지 다항식 함수들의 모임이다. 위에서 살펴본 $$X=\mathbb{A}^n$$ 경우와 마찬가지로, $$\mathbb{K}[X]$$의 원소들은 $$X$$ 위에 정의된 함수로 생각할 수 있다. 구체적으로, $$\mathbb{K}[X]$$의 한 원소 $$\overline{f}\in \mathbb{K}[X]$$에 대하여, 다음 함수

$$X\rightarrow \mathbb{K};\qquad x\mapsto f(x)$$

는 잘 정의된 함수이다. 여기서 이 함수가 잘 정의되었다는 것은 $$\overline{f}$$의 representative의 선택에 관계없이 값 $$f(x)$$가 유일하다는 것이며 이는 정확하게 $$X$$가 $$I(X)$$의 zero set으로 정의되기 때문에 가능하다. 

이제 우리는 앞서 논의한 $$\mathbb{K}[\x_1,\ldots, \x_n]$$의 prime ideal들과 $$\mathbb{A}^n$$의 closed subvariety들 사이의 일대일 대응을 임의의 affine variety로 확장할 준비가 되었다. 

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins> Affine variety $$X \subseteq \mathbb{A}^n$$이 주어졌다 하자. 그럼 coordinate ring $$\mathbb{K}[X]$$의 prime ideal들과 $$X$$의 closed subvariety들 사이에는 다음과 같은 일대일대응이 존재한다.

1. Prime ideal $$\mathfrak{p} \subset \mathbb{K}[X]$$에 대하여, $$\tilde{\mathfrak{p}}$$를 $$\mathfrak{p}$$의 $$\mathbb{K}[\x_1, \ldots, \x_n]$$에서의 preimage라 하면, $$Z(\tilde{\mathfrak{p}}) \subseteq X$$는 $$X$$의 closed subvariety이다.
2. Closed subvariety $$Y \subseteq X$$에 대하여, $$I(Y)/I(X) \subset \mathbb{K}[X]$$는 prime ideal이다.

이들 사이의 대응 $$\mathfrak{p} \mapsto Z(\tilde{\mathfrak{p}})$$와 $$Y \mapsto I(Y)/I(X)$$는 서로 역대응이다.

</div>

이에 대한 증명은 본질적으로 fourth isomorphism theorem으로부터 자명하다. 

<div class="example" markdown="1">

<ins id="ex13">**예시 13**</ins> [예시 3](#ex3)에서 살펴본 affine variety들의 경우, ideal들 $$(\x^2+\y^2-1)$$ 그리고 $$(\y-\x^2,\z-\x^3)$$은 radical임을 보일 수 있다. 따라서 단위원 $$X = Z(\x^2+\y^2-1)$$의 coordinate ring은 $$\mathbb{K}[X] = \mathbb{K}[\x, \y]/(\x^2+\y^2-1)$$이고 twisted cubic $$C$$의 coordinate ring은 $$\mathbb{K}[C] = \mathbb{K}[\x, \y, \z]/(\y-\x^2, \z-\x^3) \cong \mathbb{K}[\x]$$이다.

그러나 일반적으로 초곡면 $$Z(f)$$의 coordinate ring은 $$\mathbb{K}[Z(f)] = \mathbb{K}[\x_1, \ldots, \x_n]/I(Z(f)) = \mathbb{K}[\x_1, \ldots, \x_n]/\sqrt{(f)}$$이므로, coordinate ring을 계산할 때는 주어진 ideal이 radical인지를 판단하여야 한다.

</div>

한편, 우리는 앞서 affine variety의 정의가 실은 (closed) embedding $$X\subseteq \mathbb{A}^n$$에 의존한다는 것을 지적하였는데, 그로 인한 문제가 여기에서도 발생한다. 해당 부분에서 사용한 $$\mathbb{A}^1$$의 principal open set $$X=D(\x)$$의 예시를 살펴보면, 이 affine variety의 올바른 coordinate ring은 $$\mathbb{A}^1$$의 부분집합으로서 계산하는 것이 아닌, $$\mathbb{A}^2$$의 부분집합 $$Z(\x\y-1)$$으로서 계산하여야 하고 그럼

$$\mathbb{K}[X]=\mathbb{K}[\x,\y]/(\x\y-1)\cong \mathbb{K}[\x,1/\x]$$

가 된다. 이를 염두에 두면 다음의 정의 또한 이해할 수 있다. 

<div class="definition" markdown="1">

<ins id="def14">**정의 14**</ins> 임의의 affine variety $$V\subseteq \mathbb{A}^k$$와 그 위에서 정의된 함수 $$f:V\rightarrow \mathbb{K}$$에 대하여, $$f$$가 점 $$p\in V$$에서 *regular*라는 것은 $$p$$의 적당한 열린근방 $$D(h)$$와 다항식 $$g$$가 존재하여, $$U$$ 위에서 $$f=g/h$$이 성립하는 것이다. 여기서 $$h$$는 $$U=D(h)$$ 위에서 $$0$$이 되지 않는 다항식이다. 

</div>

그럼 이 정의 하에서, 모든 점에서 regular인 함수를 regular function이라 부르는 것이 자연스러울 것이다. 이 두 정의 [정의 11](#def11)과 [정의 14](#def14)이 동치라는 것에 대한 증명은 다소 귀찮을 수 있으나, 본질적인 내용은 위에서 살펴본 예시에 들어있으므로 그 증명은 하지 않기로 한다. 증명의 핵심은 [정의 14](#def14)에서 [정의 11](#def11)을 얻어내는 것인데, 이는 각각의 $$D(h)$$에서 $$g/h$$꼴로 나타나는 함수들을 잘 붙이는 것으로부터 얻어진다. 

## 아핀다양체 사이의 사상

이제 우리는 affine variety들 사이의 morphism을 정의한다. Affine variety들은 다항식으로 정의되는 기하학적 대상들이므로, 이들 사이의 함수 또한 다항식으로 나타나는 것들이어야 함이 타당하다.

<div class="definition" markdown="1">

<ins id="def15">**정의 15**</ins> 두 affine variety들 $$X \subseteq \mathbb{A}^n$$과 $$Y \subseteq \mathbb{A}^m$$ 사이의 함수 $$\varphi:X \rightarrow Y$$가 이들 사이의 *morphism<sub>사상</sub>* (또는 *regular map<sub>정칙사상</sub>*)이라는 것은 적절한 다항식 $$f_1, \ldots, f_m \in \mathbb{K}[\x_1, \ldots, \x_n]$$들이 존재하여

$$\varphi(a_1, \ldots, a_n) = (f_1(a), \ldots, f_m(a))$$

으로 나타낼 수 있는 것이다. 

</div>

예를 들어, 우리는 [예시 3](#ex3)에서 twisted cubic이 $$t\mapsto (t,t^2,t^3)$$을 통해 $$\mathbb{A}^1$$과 대응됨을 보였는데, 위의 정의는 이것이 affine variety들 사이의 morphism이라는 것을 보여준다.

직관적으로 $$\mathbb{K}[X]$$들은 $$X$$ 위에 정의된 함수이므로, 만일 morphism $$X\rightarrow Y$$가 주어졌다면 이 morphism과의 합성을 통해 $$Y$$의 regular function들을 $$X$$로 옮겨올 수 있을 것이다. 이는 기하학적 사상에서 대수적 사상으로 가는 한 방향이다. 더 중요한 것은 그 역방향, 즉 coordinate ring homomorphism $$\mathbb{K}[Y]\rightarrow \mathbb{K}[X]$$가 주어졌을 때 이를 기하학적 morphism $$X\rightarrow Y$$로 복원할 수 있다는 사실이다.

<div class="proposition" markdown="1">

<ins id="prop16">**명제 16**</ins> Morphism $$\varphi: X \to Y$$는 coordinate ring homomorphism $$\varphi^\ast: \mathbb{K}[Y] \to \mathbb{K}[X]$$를 유도한다. 구체적으로, $$\bar{g} \in \mathbb{K}[Y]$$에 대하여

$$\varphi^\ast(\bar{g}) = \overline{g \circ \varphi}$$

이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

먼저 $$\varphi^\ast$$가 well-defined임을 보여야 한다. $$g, h \in \mathbb{K}[\y_1, \ldots, \y_m]$$가 $$Y$$ 위에서 같은 함수를 정의한다면, $$g - h \in I(Y)$$이다. $$\varphi(X) \subseteq Y$$이므로, 모든 $$a \in X$$에 대해

$$(g \circ \varphi)(a) - (h \circ \varphi)(a) = (g - h)(\varphi(a)) = 0$$

이다. 즉 $$g \circ \varphi - h \circ \varphi \in I(X)$$이고, 따라서 $$\overline{g \circ \varphi} = \overline{h \circ \varphi}$$이다.

이제 $$\varphi^\ast$$가 ring homomorphism임은 자명하다.

</details>

즉, morphism $$\varphi: X \to Y$$는 coordinate ring homomorphism $$\varphi^\ast: \mathbb{K}[Y] \to \mathbb{K}[X]$$를 유도한다. 이는 $$X\mapsto \mathbb{K}[X]$$가 affine variety들의 category에서 $$\Ring$$으로의 contravariant functor임을 의미한다. ([\[범주론\] §함자, ⁋정의 5](/ko/math/category_theory/functors#def5))

한편 morphism의 개념을 정의했다면, 당연히 isomorphism의 개념이 존재한다.

<div class="definition" markdown="1">

<ins id="def17">**정의 17**</ins> Morphism $$\varphi: X \to Y$$가 *isomorphism<sub>동형사상</sub>*이라는 것은 역함수 $$\psi: Y \to X$$가 존재하여 $$\psi$$도 morphism인 것이다.

</div>

예를 들어, $$\mathbb{A}^1$$에서 twisted cubic $$C$$로의 morphism $$t\mapsto (t, t^2, t^3)$$은 isomorphism이다. 이는 $$(x,y,z)\mapsto x$$가 inverse를 정의하기 때문이다.

위에서 살펴봤듯, $$X\mapsto \mathbb{K}[X]$$는 affine variety들의 category에서 $$\Ring$$으로의 contravariant functor를 정의하므로, isomorphic한 affine variety들은 isomorphic한 coordinate ring을 갖는 것이 자명하다. 다음 명제는 그 역도 성립함을 보여준다.

<div class="proposition" markdown="1">

<ins id="prop18">**명제 18**</ins> Morphism $$\varphi: X \to Y$$가 isomorphism일 필요충분조건은 $$\varphi^\ast: \mathbb{K}[Y] \to \mathbb{K}[X]$$가 ring isomorphism인 것이다.

</div>

[명제 16](#prop16)에서 우리는 morphism $$\varphi: X \to Y$$가 coordinate ring homomorphism $$\varphi^\ast: \mathbb{K}[Y] \to \mathbb{K}[X]$$를 유도함을 보았다. 직관적으로, $$\varphi^\ast$$는 $$Y$$ 위의 함수 $$g$$를 $$X$$ 위의 함수 $$g \circ \varphi$$로 대응시키는데, 이는 $$Y$$의 기하학적 정보를 $$X$$로 pullback하는 연산이다. 따라서 $$\varphi^\ast$$가 isomorphism이라면, 양쪽 coordinate ring의 함수들이 서로 완벽하게 대응하므로, 기하학적으로도 $$X$$와 $$Y$$의 구조가 본질적으로 같을 것이라는 기대가 자연스럽다. 다음 증명은 이 직관을 엄밀하게 구현한다.

<details class="proof--alone" markdown="1">
<summary>증명</summary>

반대방향만 보이면 충분하다. $$\varphi^\ast$$가 isomorphism이라 하자. 그럼 $$\psi^\ast = (\varphi^\ast)^{-1}: \mathbb{K}[X] \to \mathbb{K}[Y]$$가 존재한다.

이제 $$\psi^\ast$$로부터 morphism $$\theta: Y \to X$$를 정의하자.

$$\mathbb{K}[X] = \mathbb{K}[\x_1, \ldots, \x_n]/I(X)$$

의 각 원소 $$\bar{\x}_i$$에 대하여, $$\psi^\ast(\bar{\x}_i) \in \mathbb{K}[Y]$$를 생각할 수 있다. 이를 $$\bar{g}_i$$라 적고, 이들의 어떠한 representative들 $$g_i$$들을 생각하자. 그럼 $$\theta: Y \to \mathbb{A}^n$$을 $$\theta(y) = (g_1(y), \ldots, g_n(y))$$으로 정의할 수 있으며, $$\mathbb{K}[Y]$$의 정의에 의해 이는 representative $$g_i$$의 선택에 의존하지 않는다. 이제 $$\psi^\ast$$가 well-defined이므로 $$\theta(Y) \subseteq X$$이고, 따라서 $$\theta: Y \to X$$는 morphism이다. 나머지 부분은 단순 계산이다.

</details>

---

**참고문헌**

**[Har]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Zarieties in Projective Space*, Springer, 2013.  
**[Ful]** W. Fulton, *Algebraic Curves*, 2008. (Available online)
