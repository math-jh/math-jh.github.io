---
title: "아핀다양체"
excerpt: "Affine varieties and their basic properties"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/affine_varieties
sidebar:
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Affine_Varieties.png
    overlay_filter: 0.5

date: 2026-03-11
last_modified_at: 2026-03-12
weight: 1

---

대수기하학에서 우리의 목표는 다항식으로 정의되는 기하적 대상들을 연구하는 것이다. 구체적으로, field $$\mathbb{K}$$와 자연수 $$n$$이 주어졌을 때, 우리는 다음의 식

$$V(f)= \{(x_1, \ldots, x_n) \in \mathbb{A}^n \mid f(x_1, \ldots, x_n) = 0\},\qquad f\in \mathbb{K}[\x_1,\ldots, \x_n]$$

으로 주어지는 집합들에 관심이 있다. 이는 $$\mathbb{K}^n$$에서 다항식 $$f$$의 근들의 모임이다. 일반적으로 $$\mathbb{K}=\mathbb{C}$$로 두며, 이러한 가정에서 특히 좋은 것은 $$\mathbb{C}$$이 algebraically closed라는 사실이다. 그러나, 대부분의 경우 이렇게 가정하는 것이 큰 도움이 되지는 않으므로 우리는 더 일반적인 세팅을 사용하기로 한다. 또, 혼동을 방지하기 위하여 다항식 $$f$$의 변수는 정자 $$\x$$와 같은 식으로 표기할 것이다.

## 아핀다양체의 정의

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Field $$\mathbb{K}$$ 위에 정의된 *affine $n$-space<sub>$n$차원 아핀공간</sub>* $$\mathbb{A}^n_\mathbb{K}$$는 $$n$$차원 벡터공간 $$\mathbb{K}^n$$을 의미한다.

</div>

맥락상 $$\mathbb{K}$$를 생략해도 될 때는 $$\mathbb{A}^n$$과 같이 적는다. 우리는 affine space

$$\mathbb{A}^n=\{(x_1,\ldots, x_n)\mid x_i\in \mathbb{K}\}$$

의 원소를 *점<sub>point</sub>*이라 부르고, 각각의 좌표 $$x_i$$를 *$i$번째 좌표*라 부른다. 위에서 언급했듯, 우리가 살펴볼 기하적인 대상들은 다항식 $$f\in \mathbb{K}[\x_1,\ldots, \x_n]$$의 zero set $$V(f)$$로 나타나는 대상들이다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 다항식 $$f_1, \ldots, f_k \in \mathbb{K}[\x_1, \ldots, \x_n]$$에 대하여, 이들이 정의하는 *affine variety<sub>아핀다양체</sub>* $$V(f_1, \ldots, f_k)$$를

$$V(f_1, \ldots, f_k) = \{x=(x_1, \ldots, x_n) \in \mathbb{A}^n \mid f_1(x) = \cdots = f_k(x) = 0\}$$

으로 정의한다.

</div>

즉, 아핀다양체는 여러 다항식들 $$f_1,\ldots, f_k$$의 common zero들의 모임이다. 더 일반적으로, $$\mathbb{K}[\x_1,\ldots, \x_n]$$의 부분집합 $$S$$에 대하여 $$V(S)$$를 위의 정의와 비슷하게 정의할 수 있으며, 그럼 정의에 의해 $$S$$로 생성되는 $$\mathbb{K}[\x_1,\ldots, \x_n]$$의 ideal $$(S)$$는 식

$$V(S)=V((S))$$

을 만족한다. 따라서 우리는 ideal $$\mathfrak{a}$$들이 정의하는 affine variety들만 신경써도 된다.

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> 우리가 아는 대다수의 기하학적인 대상들은 다항식으로 나타나므로, 이들이 모두 affine variety의 예시가 된다.

1. $$\mathbb{A}^2$$ 안에서 정의된 affine variety $$V(\x^2+\y^2-1)$$을 생각하자. 정의에 의해, 이 집합은 식 $$\x^2+\y^2-1=0$$을 만족하는 $$\mathbb{A}^2$$의 점들의 모임이므로, 단위원을 나타낸다.
2. 일반적으로, 임의의 affine space $$\mathbb{A}^n$$와 임의의 다항식 $$f\in \mathbb{K}[\x_1,\ldots, \x_n]$$에 대하여, $$V(f)$$는 *초곡면<sub>hypersurface</sub>*을 정의한다.
3. 또 다른 중요한 예시로, $$\mathbb{A}^3$$ 위에 정의된 *twisted cubic*이 있다. 이는 $$\mathbb{A}^3$$ 위에 정의된 두 다항식 $$\y-\x^2$$, $$\z-\x^3$$으로 정의되는 곡선으로, 매개화 $$(t,t^2,t^3)$$을 통해 $$\mathbb{A}^1$$과 일대일로 대응된다.
4. Affine space $$\mathbb{A}^n$$ 자기자신과 공집합은 affine variety이다. 이는 $$V(0)=\mathbb{A}^n$$, $$V(1)=\emptyset$$으로부터 자명하다. 이는 [명제 4](#prop4)에서 Zariski topology를 정의할 때 중요하게 사용된다.

</div>

위의 예시에서 우리는 친숙한 기하학적 대상들이 모두 집합으로서는 affine variety로 쓰여질 수 있음을 보았다. 그러나 이를 기하학적 대상이라 생각하기 위해서는 그 위에 위상구조가 존재해야 한다. 우리의 유일한 도구는 다항식이므로, 이를 사용하여 위상구조를 정의할 것이다. 

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> 다음이 성립한다.

1. $$V(0) = \mathbb{A}^n$$,
2. $$V(1) = \emptyset$$,
3. $$\mathfrak{a} \subseteq \mathfrak{b} \implies V(\mathfrak{b}) \subseteq V(\mathfrak{a})$$,
4. $$\displaystyle\bigcap_{i\in I} V(\mathfrak{a}_i) = V\left(\sum_i \mathfrak{a}_i\right)$$,
5. $$V(\mathfrak{a}) \cup V(\mathfrak{b}) = V(\mathfrak{a} \cap \mathfrak{b}) = V(\mathfrak{a}\mathfrak{b})$$.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

처음 두 명제는 [예시 3](#ex3)에서 이미 살펴보았다. 

세 번째 결과를 증명하기 위해, $$\mathfrak{a}\subseteq \mathfrak{b}$$라 하고 $$x\in V(\mathfrak{b})$$라 하자. 그럼 모든 $$f \in \mathfrak{b}$$에 대해 $$f(x) = 0$$이고, $$\mathfrak{a} \subseteq \mathfrak{b}$$이므로 특히 모든 $$\mathfrak{a}$$의 원소에 대해서도 원하는 식이 성립한다.

네 번째 결과의 경우, 점 $$x$$가 모든 $$V(\mathfrak{a}_i)$$에 속한다는 것은 모든 $$i$$와 모든 $$f \in \mathfrak{a}_i$$에 대해 $$f(x) = 0$$이라는 것이다. 이는 $$\sum_\alpha I_\alpha$$의 모든 원소가 $$p$$에서 0이라는 것과 동치이다.

이제 마지막 주장을 보이자. 우선 $$x\in V(\mathfrak{a})\cup V(\mathfrak{b})$$라 하자. 그럼 $$x\in V(\mathfrak{a})$$이거나 $$x\in V(\mathfrak{b})$$이며, 어느 경우든 $$\mathfrak{a}\cap \mathfrak{b}$$의 모든 원소는 $$x$$에서 $$0$$이므로 $$x\in V(\mathfrak{a}\cap \mathfrak{b})$$이 성립한다.  
이제 $$x\in V(\mathfrak{a}\cap \mathfrak{b})$$라 하면, $$\mathfrak{a}\mathfrak{b}$$의 임의의 원소

$$f_1g_1+\cdots+ f_kg_k,\qquad f_i\in \mathfrak{a}, g_i\in \mathfrak{b}$$

를 $$x$$에서 계산한 것이 $$0$$이 되는 것은 자명하다.  
마지막으로 $$x\in V(\mathfrak{a}\mathfrak{b})$$라 하자. 만일 결론에 반하여 $$x\not\in V(\mathfrak{a})\cup V(\mathfrak{b})$$라면, 적당한 $$f\in \mathfrak{a}$$와 적당한 $$g\in \mathfrak{b}$$가 존재하여 $$f(x),g(x)\neq 0$$이다. 그런데, 만일 이것이 성립한다면 $$f(x)g(x)\neq 0$$이므로 $$x\in V(\mathfrak{a}\mathfrak{b})$$라는 가정에 모순이다. 

</details>

특히, 위의 명제는 만일 $$\mathbb{A}^n$$ 위에서 정의된 affine variety들을 닫힌집합이라고 선언한다면, [\[위상수학\] §집합의 내부, 폐포, 경계, ⁋명제 2](/ko/math/topology/other_concepts#prop2)의 조건들이 모두 만족되고 따라서 $$\mathbb{A}^n$$ 위의 위상구조가 유일하게 결정된다는 것을 보여준다. 이를 *Zariski topology<sub>자리스키 위상</sub>*이라 부른다. 그럼 정의에 의해 임의의 affine variety $$X$$는 적당한 affine space $$\mathbb{A}^n$$의 닫힌 부분집합이며, 우리는 $$\mathbb{A}^n$$에서 정의된 위상의 subspace topology를 통해 $$X$$에서의 위상을 정의할 수 있다. 

특별한 예시로 $$\mathbb{A}^1$$에서의 Zariski topology를 보면, $$\mathbb{K}$$의 임의의 원소는 일차식 $$\x-x$$의 zero set이므로 임의의 singleton은 닫힌집합이고, 따라서 임의의 유한집합은 닫힌집합이다. 그러나 $$\mathbb{K}[\x]$$의 임의의 원소는 많아야 유한 개의 근만을 가지므로, 이 위상구조 상에서는 ($$\mathbb{K}$$가 유한집합이 아닌 한) 무한한 원소를 가진 닫힌집합은 오직 $$\mathbb{K}$$ 자기자신 뿐이다. 즉 $$\mathbb{A}^1$$의 Zariski topology는 cofinite topology이며, 이로부터 우리는 Zariski topology가 Hausdorff일 필요가 없다는 것을 관찰할 수 있다. 

이제 우리는 Zariski topology의 열린집합들을 살펴보자.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> 다항식 $$f \in \mathbb{K}[\x_1, \ldots, \x_n]$$에 대하여, *principal open set* $$D(f)$$를

$$D(f) = \{x\in \mathbb{A}^n \mid f(x) \ne 0\} = \mathbb{A}^n \setminus V(f)$$

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

$$X\setminus U=V(\mathfrak{a})\cap X$$

이도록 할 수 있다. 따라서 

$$U = X \setminus (V(\mathfrak{a}) \cap X) = X \cap (\mathbb{A}^n \setminus V(\mathfrak{a}))$$

이다. 한편 $$\mathbb{A}^n \setminus V(\mathfrak{a})$$는 $$f \in \mathfrak{a}$$에 대해 $$f(x) \ne 0$$인 점들의 집합이므로

$$\mathbb{A}^n \setminus V(\mathfrak{a}) = \bigcup_{f \in \mathfrak{a}} D(f)$$

이다. 따라서 $$U = \bigcup_{f \in \mathfrak{a}} (D(f) \cap X)$$이다.

</details>

일반적으로 affine variety의 열린집합은 affine variety일 필요가 없으며, 실제로도 그렇지 않다. 그러나 affine variety의 principal open subset은 반드시 affine variety이다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> Affine variety $$X \subseteq \mathbb{A}^n$$과 다항식 $$f \in \mathbb{K}[\x_1, \ldots, \x_n]$$에 대하여, $$D(f) \cap X$$는 affine variety이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

적당한 ideal $$\mathfrak{a}$$를 택하여 $$X = V(\mathfrak{a})$$라 하자. 우리는 $$D(f) \cap X$$를 $$\mathbb{A}^{n+1}$$의 affine variety로 표현할 것이다. 이를 위해 $$\mathbb{A}^{n+1}$$을 나타내는 좌표들을 

$$\x_1,\ldots, \x_n,\y$$

라 하고, $$\mathbb{K}[\x_1,\ldots, \x_n,\y]$$의 ideal

$$\mathfrak{b}=\mathfrak{a}+(1-f\y)$$

을 생각하자. 그럼 

$$V(\mathfrak{b})=\{(x_1,\ldots, x_n, y)\in \mathbb{A}^{n+1}\mid x\in X, 1-f(x)y=0\}$$

이다. 이제 조건 $$1-f(x)y=0$$으로부터 $$f(x)\neq 0$$이고, $$y=1/f(x)$$임을 안다. 이로부터 다음의 bijection

$$(x_1,\ldots, x_n,y)\mapsto (x_1,\ldots, x_n)$$

을 얻는다. 

</details>

## 영점정리

[명제 4](#prop4)에서 살펴본 $$V$$는 대수적인 대상들, 즉 $$\mathbb{K}[\x_1,\ldots, \x_n]$$의 다항식들을 기하적인 대상들, 즉 이들 다항식들이 정의하는 zero set으로 보내준다. 거꾸로 우리는 기하적인 대상을 받아 대수적인 대상들을 대응시켜줄 수도 있다.

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
4. $$X \subseteq V(I(X))$$가 항상 성립한다.
5. $$I \subseteq I(V(I))$$가 항상 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

1. $$X \subseteq Y$$이고 $$f \in I(Y)$$라면, 모든 $$a \in Y$$에 대해 $$f(a) = 0$$이다. 특히 모든 $$a \in X$$에 대해 $$f(a) = 0$$이므로 $$f \in I(X)$$이다.
2. Vacuous truth.
3. $$\mathbb{K}$$가 무한하다면, 모든 점에서 0인 다항식은 영다항식뿐이다.
4. $$a \in X$$이고 $$f \in I(X)$$라면 $$f(a) = 0$$이다. 즉 $$a \in V(I(X))$$이다.
5. $$f \in I$$이고 $$a \in V(I)$$라면 $$f(a) = 0$$이다. 즉 $$f \in I(V(I))$$이다.

</details>

즉, $$V$$와 $$I$$는 antitone Galois connection을 정의한다. ([\[집합론\] §필터와 아이디얼, 갈루아 대응, ⁋정의 6](/ko/math/set_theory/filter_and_ideal#def6)) 따라서 두 operator의 합성 $$VI$$와 $$IV$$ 각각은 closure operator를 정의한다. $$VI$$의 경우, 이 closure는 실제로 Zariski topology에서의 closure가 된다. 이는 만일 $$X \subseteq Y = V(J)$$이면 $$I(V(J)) \subseteq I(X)$$이고, [명제 9](#prop9)의 5번 조건에서 $$J \subseteq I(V(J))$$이므로 $$VI(X) \subseteq V(J) = Y$$가 되어, $$VI(X)$$가 $$X$$를 포함하는 Zariski closed set 중 가장 작은 것이 되기 때문이다. $$IV$$의 경우에는 바로 보이지 않는데, 이를 위해서는 ideal의 radical 개념이 필요하다.

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

$$V(\mathfrak{a}^k)=V(\mathfrak{a}\cap\cdots\cap \mathfrak{a})=V(\mathfrak{a})$$

이므로, 어느정도 예견된 결과라고 할 수도 있다.

## Coordinate Ring

우리는 양방향의 대응 $$V$$, $$I$$가 담고 있는 철학을 더 확장시킬 수 있다. 구체적으로, $$\mathbb{A}^n$$의 기하학은 그 정의에 의해 $$\mathbb{K}[\x_1,\ldots, \x_n]$$의 원소들이 담고 있다. 역으로, $$\mathbb{A}^n$$의 임의의 점 $$x=(x_1,\ldots, x_n)$$를 받아 $i$번째 좌표를 내놓는 함수를 $$\x_i: x\mapsto x_i$$으로 생각할 수 있으며, 이러한 관점에서 $$\mathbb{K}[\x_1,\ldots, \x_n]$$의 모든 원소들을 $$\mathbb{A}^n$$ 위에 정의된 (다항식) 함수로 볼 수 있다. 

더 일반적으로 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="def11">**정의 11**</ins> Affine variety $$X = V(\mathfrak{a}) \subseteq \mathbb{A}^n$$의 *coordinate ring<sub>좌표환</sub>* $$\mathbb{K}[X]$$를

$$\mathbb{K}[X] = \mathbb{K}[\x_1, \ldots, \x_n] / I(X)=\mathbb{K}[\x_1, \ldots, \x_n] / \sqrt{\mathfrak{a}}$$

으로 정의한다. 이 원소들을 $$X$$ 위에 정의된 *regular function<sub>정칙함수</sub>*이라 부른다.

</div>

Coordinate ring $$\mathbb{K}[X]$$의 원소들은 위에서 살펴본 것과 비슷하게 $$X$$ 위에서 정의된 함수들로 생각할 수 있다. 구체적으로, 각 $$\bar{f} \in \mathbb{K}[X]$$는 함수 $$X \to \mathbb{K}$$, $$a \mapsto f(a)$$로 생각할 수 있다. 이것이 잘 정의되기 위해서는 $$\bar{f}$$의 representative에 상관없이 $$X$$의 모든 점에서 그 함숫값이 같아야 하는데, 어차피 $$\bar{f}$$에서 다른 representative를 택하는 것은 $$I(X)$$의 원소를 택하는 것이고 이들 함수들은 $$X$$ 위에서 identically zero이기 때문이다. 

<div class="example" markdown="1">

<ins id="ex12">**예시 12**</ins> [예시 3](#ex3)에서 살펴본 affine variety들의 경우, ideal들 $$(\x^2+\y^2-1)$$ 그리고 $$(\y-\x^2,\z-\x^3)$$은 radical임을 보일 수 있다. 따라서 단위원 $$X = V(\x^2+\y^2-1)$$의 coordinate ring은 $$\mathbb{K}[X] = \mathbb{K}[\x, \y]/(\x^2+\y^2-1)$$이고 twisted cubic $$C$$의 coordinate ring은 $$\mathbb{K}[C] = \mathbb{K}[\x, \y, \z]/(\y-\x^2, \z-\x^3) \cong \mathbb{K}[\x]$$이다.

그러나 일반적으로 초곡면 $$V(f)$$의 coordinate ring은 $$\mathbb{K}[V(f)] = \mathbb{K}[\x_1, \ldots, \x_n]/I(V(f)) = \mathbb{K}[\x_1, \ldots, \x_n]/\sqrt{(f)}$$이므로, coordinate ring을 계산할 때는 주어진 ideal이 radical인지를 판단하여야 한다.

</div>

## 아핀다양체 사이의 사상

이제 우리는 affine variety들 사이의 morphism을 정의한다. Affine variety들은 다항식으로 정의되는 기하학적 대상들이므로, 이들 사이의 함수 또한 다항식으로 나타나는 것들이어야 함이 타당하다.

<div class="definition" markdown="1">

<ins id="def13">**정의 13**</ins> 두 affine variety들 $$X \subseteq \mathbb{A}^n$$과 $$Y \subseteq \mathbb{A}^m$$ 사이의 함수 $$\varphi:X \rightarrow Y$$가 이들 사이의 *morphism<sub>사상</sub>* (또는 *regular map<sub>정칙사상</sub>*)이라는 것은 적절한 다항식 $$f_1, \ldots, f_m \in \mathbb{K}[\x_1, \ldots, \x_n]$$들이 존재하여

$$\varphi(a_1, \ldots, a_n) = (f_1(a), \ldots, f_m(a))$$

으로 나타낼 수 있는 것이다. 

</div>

예를 들어, 우리는 [예시 3](#ex3)에서 twisted cubic이 $$t\mapsto (t,t^2,t^3)$$을 통해 $$\mathbb{A}^1$$과 대응됨을 보였는데, 위의 정의는 이것이 affine variety들 사이의 morphism이라는 것을 보여준다.

<div class="proposition" markdown="1">

<ins id="prop13">**명제 13**</ins> Affine variety $$X$$와 다항식 $$g \in \mathbb{K}[\x_1, \ldots, \x_n]$$에 대하여, principal open set $$D(g) \cap X$$에서의 regular function들은

$$\mathbb{K}[X][1/\bar{g}] = \mathbb{K}[X, 1/\bar{g}]$$

의 원소들이다. 즉, $$D(g) \cap X$$에서의 regular function은 $$f/g^k$$ ($$f \in \mathbb{K}[X]$$, $$k \ge 0$$) 꼴로 표현된다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

[명제 7](#prop7)에서 $$D(g) \cap X$$가 affine variety임을 보였다. 구체적으로 $$D(g) \cap X \cong V(\mathfrak{a} + (1 - g\y)) \subseteq \mathbb{A}^{n+1}$$이다. 이 affine variety의 coordinate ring을 계산하면

$$\mathbb{K}[\x_1, \ldots, \x_n, \y] / (I(X) + (1 - g\y)) \cong \mathbb{K}[X][\y]/(1 - \bar{g}\y) \cong \mathbb{K}[X][1/\bar{g}]$$

이다. 여기서 마지막 동형은 $$\y \mapsto 1/\bar{g}$$로 주어진다.

</details>

<div class="misc" markdown="1">

<ins id="rmk14">**착각 14**</ins> 이 명제는 regular map을 국소적으로 다항식의 비율로 표현할 수 있음을 시사한다. 구체적으로, 함수 $$\varphi: X \to Y$$가 *각 점 $$p \in X$$마다* 적당한 열린근방 $$U \ni p$$와 다항식들 $$f_1, \ldots, f_m, g$$가 존재하여

$$\varphi(x) = \left(\frac{f_1(x)}{g(x)}, \ldots, \frac{f_m(x)}{g(x)}\right), \quad x \in U$$

으로 표현된다면, 이는 [정의 13](#def13)의 의미에서 regular map이다. 역으로, [정의 13](#def13)의 의미에서의 regular map은 항상 이러한 꼴로 국소 표현된다.

</div>

직관적으로 $$\mathbb{K}[X]$$들은 $$X$$ 위에 정의된 함수이므로, 만일 morphism $$X\rightarrow Y$$가 주어졌다면 이 morphism과의 합성을 통해 $$Y$$의 regular function들을 $$X$$로 옮겨올 수 있을 것이다.

<div class="proposition" markdown="1">

<ins id="prop15">**명제 15**</ins> Morphism $$\varphi: X \to Y$$는 coordinate ring homomorphism $$\varphi^\ast: \mathbb{K}[Y] \to \mathbb{K}[X]$$를 유도한다. 구체적으로, $$\bar{g} \in \mathbb{K}[Y]$$에 대하여

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

즉, morphism $$\varphi: X \to Y$$는 coordinate ring homomorphism $$\varphi^\ast: \mathbb{K}[Y] \to \mathbb{K}[X]$$를 유도한다. 이는 $$X\mapsto \mathbb{K}[X]$$가 affine variety들의 category에서 $$\Ring$$으로의 contravariant functor임을 의미한다.

한편 morphism의 개념을 정의했다면, 당연히 isomorphism의 개념이 존재한다.

<div class="definition" markdown="1">

<ins id="def15">**정의 15**</ins> Morphism $$\varphi: X \to Y$$가 *isomorphism<sub>동형사상</sub>*이라는 것은 역함수 $$\psi: Y \to X$$가 존재하여 $$\psi$$도 morphism인 것이다.

</div>

예를 들어, $$\mathbb{A}^1$$에서 twisted cubic $$C$$로의 morphism $$t\mapsto (t, t^2, t^3)$$은 isomorphism이다. 이는 $$(x,y,z)\mapsto x$$가 inverse를 정의하기 때문이다.

위에서 살펴봤듯, $$X\mapsto \mathbb{K}[X]$$는 affine variety들의 category에서 $$\Ring$$으로의 contravariant functor를 정의하므로, isomorphic한 affine variety들은 isomorphic한 coordinate ring을 갖는 것이 자명하다. 다음 명제는 그 역도 성립함을 보여준다.

<div class="proposition" markdown="1">

<ins id="prop16">**명제 16**</ins> Morphism $$\varphi: X \to Y$$가 isomorphism일 필요충분조건은 $$\varphi^\ast: \mathbb{K}[Y] \to \mathbb{K}[X]$$가 ring isomorphism인 것이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

반대방향만 보이면 충분하다. $$\varphi^\ast$$가 isomorphism이라 하자. 그럼 $$\psi^\ast = (\varphi^\ast)^{-1}: \mathbb{K}[X] \to \mathbb{K}[Y]$$가 존재한다.

이제 $$\psi^\ast$$로부터 morphism $$\theta: Y \to X$$를 정의하자.

$$\mathbb{K}[X] = \mathbb{K}[\x_1, \ldots, \x_n]/I(X)$$

의 각 원소 $$\bar{\x}_i$$에 대하여, $$\psi^\ast(\bar{\x}_i) \in \mathbb{K}[Y]$$를 생각할 수 있다. 이를 $$\bar{g}_i$$라 적고, 이들의 어떠한 representative들 $$g_i$$들을 생각하자. 그럼 $$\theta: Y \to \mathbb{A}^n$$을 $$\theta(y) = (g_1(y), \ldots, g_n(y))$$으로 정의할 수 있으며, $$\mathbb{K}[Y]$$의 정의에 의해 이는 representative $$g_i$$의 선택에 의존하지 않는다. 이제 $$\psi^\ast$$가 well-defined이므로 $$\theta(Y) \subseteq X$$이고, 따라서 $$\theta: Y \to X$$는 morphism이다. 나머지 부분은 단순 계산이다.

</details>

---

**참고문헌**

**[Har]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.
**[Ful]** W. Fulton, *Algebraic Curves*, 2008. (Available online)
