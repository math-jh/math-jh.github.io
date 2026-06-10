---
title: "대수의 직접곱, 직합, 텐서곱"
description: "가환환 위의 대수들의 직접곱, 직합, 텐서곱에 자연스럽게 부여되는 대수 구조와 그 성질을 다룬다."
excerpt: "Algebra의 product, direct sum, tensor product 구조"

categories: [Math / Algebraic Structures]
permalink: /ko/math/algebraic_structures/operations_of_algebras
sidebar: 
    nav: "algebraic_structures-ko"

date: 2024-10-07
last_modified_at: 2026-06-11
weight: 302
published: false

---

우리는 [§가군의 직접곱과 직합, 텐서곱](/ko/math/algebraic_structures/operations_of_modules)에서 가군들의 연산을, [§환의 곱, 쌍대곱, 텐서곱](/ko/math/algebraic_structures/operations_of_rings)에서 환들의 연산을 살펴보았다. $$A$$-algebra는 $$A$$-module 위에 bilinear한 곱셈을 추가한 구조이므로 ([§대수, ⁋정의 1](/ko/math/algebraic_structures/algebras#def1)), 가군의 단계에서 정의된 연산들 위에 곱셈이 잘 따라오는지를 확인하는 것이 이번 글의 내용이다. [§대수](/ko/math/algebraic_structures/algebras)에서와 마찬가지로 $$A$$는 항상 commutative ring이다.

## 대수의 직접곱과 직합

$$A$$-algebra들의 family $$(E_i)_{i\in I}$$가 주어졌다 하자. 그럼 우선 $$A$$-module로서의 direct product $$\prod_{i\in I}E_i$$를 생각할 수 있고, 이 위에 성분별 곱셈을 주는 것이 자연스럽다.

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1**</ins> $$A$$-algebra들의 family $$(E_i)_{i\in I}$$에 대하여, $$A$$-module $$\prod_{i\in I}E_i$$ 위에 다음의 식

$$(x_i)_{i\in I}\,(y_i)_{i\in I}=(x_iy_i)_{i\in I}$$

으로 곱셈을 정의하면 $$\prod_{i\in I}E_i$$는 $$A$$-algebra가 된다. 또, 모든 $$E_i$$들이 associative (resp. commutative, unital)라면 $$\prod_{i\in I}E_i$$도 그러하다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

위의 곱셈이 $$A$$-bilinear인 것을 보여야 한다. 임의의 $$\alpha\in A$$와 $$x=(x_i),y=(y_i),z=(z_i)\in\prod E_i$$에 대하여, 각 성분에서 $$E_i$$의 곱셈이 $$A$$-bilinear이므로

$$\bigl((\alpha x+y)z\bigr)_i=(\alpha x_i+y_i)z_i=\alpha(x_iz_i)+y_iz_i=\bigl(\alpha(xz)+yz\bigr)_i$$

이고, 둘째 변수에 대해서도 마찬가지이다. 결합법칙과 교환법칙은 성분별로 확인되며, 모든 $$E_i$$가 항등원 $$1_{E_i}$$를 갖는다면 $$(1_{E_i})_{i\in I}$$가 $$\prod E_i$$의 항등원이 된다.

</details>

이렇게 얻어진 $$A$$-algebra를 $$E_i$$들의 *직접곱<sub>direct product</sub>*이라 부른다. 곱셈을 성분별로 정의했으므로 canonical projection들 $$\pr_i:\prod E_i \rightarrow E_i$$는 $$A$$-algebra homomorphism이고, 실제로 직접곱은 $$A$$-algebra들과 $$A$$-algebra homomorphism들의 category에서의 product이다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 임의의 $$A$$-algebra $$F$$와 $$A$$-algebra homomorphism들 $$u_i:F \rightarrow E_i$$가 주어졌다 하자. 그럼 $$\pr_i\circ u=u_i$$가 모든 $$i$$에 대해 성립하도록 하는 유일한 $$A$$-algebra homomorphism $$u:F \rightarrow \prod_{i\in I}E_i$$가 존재한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$A$$-module의 단계에서 product의 universal property에 의하여 ([§가군의 직접곱과 직합, 텐서곱, ⁋정리 1](/ko/math/algebraic_structures/operations_of_modules#thm1)) 조건을 만족하는 유일한 $$A$$-linear map $$u:F \rightarrow\prod E_i$$, 즉 $$u(x)=(u_i(x))_{i\in I}$$가 존재한다. 이것이 곱셈을 보존하는 것은 각각의 $$u_i$$가 곱셈을 보존한다는 것으로부터

$$u(xy)=(u_i(xy))_{i\in I}=(u_i(x)u_i(y))_{i\in I}=u(x)u(y)$$

이기 때문이다.

</details>

한편 $$A$$-module로서의 direct sum $$\bigoplus_{i\in I}E_i\subseteq \prod_{i\in I}E_i$$를 생각하면, finitely supported인 두 원소의 성분별 곱은 다시 finitely supported이므로 $$\bigoplus_{i\in I}E_i$$는 직접곱의 subalgebra가 된다. ([§대수, ⁋정의 9](/ko/math/algebraic_structures/algebras#def9)) 이렇게 얻어진 $$A$$-algebra를 $$E_i$$들의 *직합<sub>direct sum</sub>*이라 부른다.

<div class="remark" markdown="1">

<ins id="rmk3">**참고 3**</ins> 가군의 경우와 달리, 대수의 직합은 categorical한 의미를 잃는다는 점에 주의해야 한다. 우선 $$I$$가 무한집합이고 무한히 많은 $$E_i$$들이 $$0$$이 아닌 unital algebra라면, 직합의 항등원이 될 수 있는 유일한 후보 $$(1_{E_i})_{i\in I}$$가 finitely supported가 아니므로 $$\bigoplus E_i$$는 unital이 아니다. 또, canonical injection $$E_j \rightarrow \bigoplus E_i$$는 (unital algebra들의 category에서) 항등원을 항등원으로 보내지 않으므로, 직합은 가군에서와 달리 coproduct가 되지 않는다. 실제로 commutative unital $$A$$-algebra들의 coproduct는 아래에서 살펴볼 텐서곱으로 주어진다.

</div>

## 대수의 텐서곱

이제 두 $$A$$-algebra $$E,E'$$의 텐서곱을 살펴보자. $$A$$-module $$E\otimes_AE'$$ 위에 우리가 원하는 곱셈은 다음의 식

$$(x\otimes x')(y\otimes y')=xy\otimes x'y'\tag{1}$$

으로 주어지는 것이지만, $$E\otimes_AE'$$의 원소가 $$x\otimes x'$$ 꼴의 원소들의 합으로 유일하게 표현되는 것은 아니므로 이 식이 잘 정의된 $$A$$-bilinear map을 주는지 확인해야 한다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> 두 $$A$$-algebra $$E,E'$$에 대하여, 식 $$(1)$$을 만족하는 $$A$$-bilinear map $$\mu:(E\otimes_AE')\times(E\otimes_AE') \rightarrow E\otimes_AE'$$이 유일하게 존재한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $$(y,y')\in E\times E'$$를 고정하자. 그럼 함수

$$E\times E' \rightarrow E\otimes_AE';\qquad (x,x')\mapsto xy\otimes x'y'$$

은 $$E,E'$$의 곱셈이 각 변수에 대해 $$A$$-linear이므로 $$A$$-bilinear이고, 따라서 텐서곱의 universal property ([§가군의 직접곱과 직합, 텐서곱, ⁋명제 8](/ko/math/algebraic_structures/operations_of_modules#prop8))에 의하여 $$x\otimes x'\mapsto xy\otimes x'y'$$이도록 하는 유일한 $$A$$-linear map $$m_{(y,y')}:E\otimes_AE' \rightarrow E\otimes_AE'$$을 유도한다.

이제 대응 $$(y,y')\mapsto m_{(y,y')}$$를 생각하면, 이는 $$E\times E'$$에서 $$\End_{\lMod{A}}(E\otimes_AE')$$로 가는 함수이며, 다시 곱셈의 bilinearity에 의해 $$A$$-bilinear이다. 가령

$$m_{(\alpha y+z,y')}(x\otimes x')=x(\alpha y+z)\otimes x'y'=\alpha(xy\otimes x'y')+xz\otimes x'y'=\bigl(\alpha m_{(y,y')}+m_{(z,y')}\bigr)(x\otimes x')$$

이 생성원들 위에서 성립하므로 $$m_{(\alpha y+z,y')}=\alpha m_{(y,y')}+m_{(z,y')}$$이다. 따라서 한 번 더 universal property를 적용하면 $$y\otimes y'\mapsto m_{(y,y')}$$이도록 하는 $$A$$-linear map $$\tilde{m}:E\otimes_AE' \rightarrow \End_{\lMod{A}}(E\otimes_AE')$$을 얻는다. 이제

$$\mu(s,t)=\tilde{m}(t)(s)$$

로 정의하면 $$\mu$$는 각 변수에 대해 $$A$$-linear이고, 생성원들 위에서 식 $$(1)$$을 만족한다. 유일성은 $$E\otimes_AE'$$이 $$x\otimes x'$$ 꼴의 원소들로 생성된다는 것으로부터 자명하다.

</details>

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> 두 $$A$$-algebra $$E,E'$$에 대하여, [명제 4](#prop4)의 곱셈이 주어진 $$A$$-algebra $$E\otimes_AE'$$을 $$E$$와 $$E'$$의 *tensor product<sub>텐서곱</sub>*이라 부른다.

</div>

직접곱에서와 마찬가지로, 텐서곱은 두 대수의 성질을 그대로 물려받는다. $$E,E'$$이 모두 associative라면 생성원들 위에서

$$\bigl((x\otimes x')(y\otimes y')\bigr)(z\otimes z')=(xy)z\otimes (x'y')z'=x(yz)\otimes x'(y'z')=(x\otimes x')\bigl((y\otimes y')(z\otimes z')\bigr)$$

이므로 $$E\otimes_AE'$$도 associative이고, 같은 방식으로 $$E,E'$$이 commutative라면 $$E\otimes_AE'$$도 commutative이다. 또 $$E,E'$$이 unital이라면 $$1_E\otimes 1_{E'}$$이 $$E\otimes_AE'$$의 항등원이 된다. 특히 $$E,E'$$이 associative unital이라면 두 $$A$$-algebra homomorphism

$$\iota:E \rightarrow E\otimes_AE';\quad x\mapsto x\otimes 1_{E'},\qquad \iota':E' \rightarrow E\otimes_AE';\quad x'\mapsto 1_E\otimes x'$$

이 정의되며, 이들의 image는 서로 commute한다. 즉 $$(x\otimes 1)(1\otimes x')=x\otimes x'=(1\otimes x')(x\otimes 1)$$이다.

[참고 3](#rmk3)에서 언급한 것과 같이, commutative unital algebra들의 category에서 텐서곱은 coproduct의 역할을 한다. 이는 [§환의 곱, 쌍대곱, 텐서곱, §§환들의 텐서곱](/ko/math/algebraic_structures/operations_of_rings#환들의-텐서곱)에서 살펴본 환들의 텐서곱 이야기를 $$A$$ 위로 옮긴 것이다.

<div class="proposition" markdown="1">

<ins id="thm6">**정리 6**</ins> Commutative unital $$A$$-algebra $$E,E'$$과, 임의의 commutative unital $$A$$-algebra $$F$$, 그리고 unital $$A$$-algebra homomorphism들 $$u:E \rightarrow F$$, $$u':E' \rightarrow F$$가 주어졌다 하자. 그럼 $$w\circ\iota=u$$, $$w\circ\iota'=u'$$을 만족하는 유일한 unital $$A$$-algebra homomorphism $$w:E\otimes_AE' \rightarrow F$$가 존재한다. 즉, $$E\otimes_AE'$$은 commutative unital $$A$$-algebra들의 category에서 $$E$$와 $$E'$$의 coproduct이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

함수 $$E\times E' \rightarrow F$$를 $$(x,x')\mapsto u(x)u'(x')$$으로 정의하면 이는 $$A$$-bilinear이므로, $$w(x\otimes x')=u(x)u'(x')$$이도록 하는 유일한 $$A$$-linear map $$w:E\otimes_AE' \rightarrow F$$가 존재한다. $$w$$가 곱셈을 보존하는 것은 생성원들 위에서 확인하면 충분한데,

$$w\bigl((x\otimes x')(y\otimes y')\bigr)=w(xy\otimes x'y')=u(xy)u'(x'y')=u(x)u(y)u'(x')u'(y')=u(x)u'(x')u(y)u'(y')=w(x\otimes x')w(y\otimes y')$$

이고, 네 번째 등식에서 $$F$$가 commutative라는 가정이 사용되었다. 또 $$w(1_E\otimes 1_{E'})=u(1_E)u'(1_{E'})=1_F$$이며, $$w\circ\iota=u$$와 $$w\circ\iota'=u'$$은 정의로부터 자명하다.

유일성을 보이자. $$w'$$이 같은 조건을 만족한다면, 임의의 생성원에 대하여

$$w'(x\otimes x')=w'\bigl((x\otimes 1_{E'})(1_E\otimes x')\bigr)=w'(\iota(x))w'(\iota'(x'))=u(x)u'(x')=w(x\otimes x')$$

이므로 $$w'=w$$이다.

</details>

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> Polynomial algebra들의 텐서곱은 변수들을 합친 polynomial algebra이다. 즉

$$A[\x]\otimes_AA[\y]\cong A[\x,\y]$$

이 성립한다. 이는 [§대수, ⁋명제 8](/ko/math/algebraic_structures/algebras#prop8)에서 살펴본 functor $$A[-]:\Set \rightarrow \cAlg{A}$$가 left adjoint라는 사실로부터 나온다. Left adjoint는 colimit을 보존하므로, 한 점 집합들의 (집합에서의) coproduct $$\{\x\}\sqcup\{\y\}=\{\x,\y\}$$를 $$\cAlg{A}$$에서의 coproduct로 보내고, [정리 6](#thm6)에 의하여 이는 정확히 텐서곱이기 때문이다. 물론 두 isomorphism $$\x\otimes 1\mapsto \x$$, $$1\otimes \y\mapsto \y$$를 직접 확인할 수도 있다.

</div>

---

**참고문헌**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  

---
