---
title: "대수의 직접곱, 직합, 텐서곱"
description: "가환환 위의 대수들의 직접곱, 직합, 텐서곱에 자연스럽게 부여되는 대수 구조와 그 성질을 다룬다."
excerpt: "Algebra의 product, direct sum, tensor product 구조"

categories: [Math / Algebraic Structures]
permalink: /ko/math/algebraic_structures/operations_of_algebras
sidebar: 
    nav: "algebraic_structures-ko"

date: 2024-10-07
weight: 302

---

우리는 [§가군의 직접곱과 직합, 텐서곱](/ko/math/algebraic_structures/operations_of_modules)에서 가군들의 연산을, [§환의 곱, 쌍대곱, 텐서곱](/ko/math/algebraic_structures/operations_of_rings)에서 ring들의 연산을 살펴보았다. $A$-algebra는 $A$-module 위에 bilinear한 곱셈을 추가한 구조이므로 ([§대수, ⁋정의 1](/ko/math/algebraic_structures/algebras#def1)), 가군의 단계에서 정의된 연산들 위에 곱셈이 잘 따라오는지를 확인하는 것이 이번 글의 내용이다. [§대수](/ko/math/algebraic_structures/algebras)에서와 마찬가지로 $A$는 항상 commutative ring이다.

## 대수의 직접곱과 직합

$A$-algebra들의 family $(E_i)_{i\in I}$가 주어졌다 하자. 그럼 우선 $A$-module로서의 direct product $\prod_{i\in I}E_i$를 생각할 수 있고, 이 위에 성분별 곱셈을 주는 것이 자연스럽다.

::: 명제 1
$A$-algebra들의 family $(E_i)_{i\in I}$에 대하여, $A$-module $\prod_{i\in I}E_i$ 위에 다음의 식

$$(x_i)_{i\in I}(y_i)_{i\in I}=(x_iy_i)_{i\in I}$$

으로 곱셈을 정의하면 $\prod_{i\in I}E_i$는 $A$-algebra가 된다. 또, 모든 $E_i$들이 associative (resp. commutative, unital)라면 $\prod_{i\in I}E_i$도 그러하다.
:::
::: 증명
위의 곱셈이 $A$-bilinear인 것을 보여야 한다. 임의의 $\alpha\in A$와 $x=(x_i),y=(y_i),z=(z_i)\in\prod E_i$에 대하여, 각 성분에서 $E_i$의 곱셈이 $A$-bilinear이므로

$$\bigl((\alpha x+y)z\bigr)_i=(\alpha x_i+y_i)z_i=\alpha(x_iz_i)+y_iz_i=\bigl(\alpha(xz)+yz\bigr)_i$$

이고, 둘째 변수에 대해서도 마찬가지이다. 결합법칙과 교환법칙은 성분별로 확인되며, 모든 $E_i$가 항등원 $1_{E_i}$를 갖는다면 $(1_{E_i})_{i\in I}$가 $\prod E_i$의 항등원이 된다.
:::

이를 다음과 같이 이름붙인다. 

::: 정의 2
[명제 1](#prop1)에서 정의된 곱셈이 주어진 $A$-algebra $\prod_{i\in I}E_i$를 $E_i$들의 *direct product<sub>직접곱</sub>*이라 부른다. Canonical projection $\pr_i:\prod E_i \rightarrow E_i$들은 모두 $A$-algebra homomorphism이다.
:::

그럼 이렇게 정의한 direct product는 $A$-algebra들의 category에서의 product이다, 즉, 다음의 universal property가 성립한다. 

::: 명제 3
임의의 $A$-algebra $F$와 $A$-algebra homomorphism들 $u_i:F \rightarrow E_i$가 주어졌다 하자. 그럼 $\pr_i\circ u=u_i$가 모든 $i$에 대해 성립하도록 하는 유일한 $A$-algebra homomorphism $u:F \rightarrow \prod_{i\in I}E_i$가 존재한다.
:::
::: 증명
$A$-module의 단계에서 product의 universal property에 의하여 ([§가군의 직접곱과 직합, 텐서곱, ⁋정리 1](/ko/math/algebraic_structures/operations_of_modules#thm1)) 조건을 만족하는 유일한 $A$-linear map $u:F \rightarrow\prod E_i$, 즉 $u(x)=(u_i(x))_{i\in I}$가 존재한다. 이것이 곱셈을 보존하는 것은 각각의 $u_i$가 곱셈을 보존한다는 것으로부터

$$u(xy)=(u_i(xy))_{i\in I}=(u_i(x)u_i(y))_{i\in I}=u(x)u(y)$$

이기 때문이다.
:::

한편, 우리는 다른 algebraic structure들에서 했던 것처럼 다음의 subalgebra를 생각할 수 있다. 

::: 명제 4
$A$-module direct sum $\bigoplus_{i\in I}E_i\subseteq\prod_{i\in I}E_i$는 direct product의 곱셈을 제한하면 그 subalgebra, 곧 $A$-algebra가 된다.
:::
::: 증명
$\bigoplus E_i$의 두 원소 $(x_i),(y_i)$는 각각 finitely supported이므로, 성분별 곱 $(x_iy_i)$에서 $i$번째 성분이 $0$이 아닌 $i$는 $x_i\neq 0$이며 $y_i\neq 0$인 $i$들의 합집합 안에 든다. 이는 유한집합이므로 $(x_iy_i)$도 finitely supported이고, 따라서 $\bigoplus E_i$는 곱셈에 대해 닫혀 $\prod E_i$의 subalgebra이다. ([§대수, ⁋정의 9](/ko/math/algebraic_structures/algebras#def9))
:::

::: 정의 5
[명제 4](#prop4)의 곱셈이 주어진 $A$-algebra $\bigoplus_{i\in I}E_i$를 $E_i$들의 *direct sum<sub>직합</sub>*이라 부른다.
:::

주의할 것은 이것이 $A$-algebra의 category에서의 coproduct가 <em-ko>아니라는</em-ko> 것이다. 즉 canonical injection $\iota_j:E_j\hookrightarrow\bigoplus E_i$는 $A$-algebra homomorphism이며, 집합으로서 [정의 5](#def5)의 집합은 $A$-module로서의 direct sum과 같은 집합이지만 이들 데이터가 universal property를 만족하지는 않는다. 가령 $E_1=E_2=A$이고, 

$$f_i: E_i\rightarrow A$$

각각이 $\id_A$로 주어진 상황을 생각해보자. $E_1\oplus E_2$가 coproduct이기 위해서는 다음의 diagram

![coproduct](/assets/images/Math/Algebraic_Structures/Operations_of_Algebras-1.svg){:style="width:13.63em" class="invert" .align-center}

을 commute하도록 하는 $f: E_1\oplus E_2\rightarrow A$가 존재해야 한다. 그런데 임의의 $(a,b)\in E_1\oplus E_2$에 대하여, 

$$f\bigl((a,b)\bigr)=f\bigl((a,0)+(0,b)\bigr)=f\bigl((a,0)\bigr)+f\bigl((0,b)\bigr)=(f\circ i_1)(a)+(f\circ i_2)(b)=a+b$$

여야 하는데, 다음의 두 계산

$$f\bigl((a,b)(c,d)\bigr)=ac+bd\neq (a+b)(c+d)=f(a,b)f(c,d)$$

에 의해 $f$는 곱셈을 보존하지 못한다. 

## 대수의 텐서곱

Commutative $A$-algebra들의 category에서 올바른 coproduct의 개념을 주는 것은 tensor product이다. 기본적으로 이는 $A$-module $E\otimes_AE'$ ([§가군의 직접곱과 직합, 텐서곱, ⁋정리 6](/ko/math/algebraic_structures/operations_of_modules#thm6)) 위에 곱셈을 적당히 정의하여 얻어지는 $A$-algebra로, 우리가 원하는 곱셈은 다음의 식

$$(x\otimes x')(y\otimes y')=xy\otimes x'y'\tag{1}$$

으로 주어지는 것이다. 그러나 일반적으로 $E\otimes_AE'$의 원소가 $x\otimes x'$ 꼴의 원소들의 합으로 유일하게 표현되는 것은 아니므로 이 식이 잘 정의된 $A$-bilinear map을 주는지부터 확인해야 한다.

::: 명제 6
두 $A$-algebra $E,E'$에 대하여, 식 $(1)$을 만족하는 $A$-bilinear map $\mu:(E\otimes_AE')\times(E\otimes_AE') \rightarrow E\otimes_AE'$이 유일하게 존재한다.
:::
::: 증명
우선 $(y,y')\in E\times E'$를 고정하자. 그럼 함수

$$E\times E' \rightarrow E\otimes_AE';\qquad (x,x')\mapsto xy\otimes x'y'$$

은 $E,E'$의 곱셈이 각 변수에 대해 $A$-linear이므로 $A$-bilinear이고, 따라서 [§가군의 직접곱과 직합, 텐서곱, ⁋명제 8](/ko/math/algebraic_structures/operations_of_modules#prop8)의 universal property에 의하여 $x\otimes x'\mapsto xy\otimes x'y'$이도록 하는 유일한 $A$-linear map $m_{(y,y')}:E\otimes_AE' \rightarrow E\otimes_AE'$을 유도한다.

이제 대응 $(y,y')\mapsto m_{(y,y')}$를 생각하면, 이는 $E\times E'$에서 $\End_{\lMod{A}}(E\otimes_AE')$로 가는 함수이며, 다시 곱셈의 bilinearity에 의해 $A$-bilinear이다. 가령

$$m_{(\alpha y+z,y')}(x\otimes x')=x(\alpha y+z)\otimes x'y'=\alpha(xy\otimes x'y')+xz\otimes x'y'=\bigl(\alpha m_{(y,y')}+m_{(z,y')}\bigr)(x\otimes x')$$

이 generator들 위에서 성립하므로 $m_{(\alpha y+z,y')}=\alpha m_{(y,y')}+m_{(z,y')}$이다. 따라서 한 번 더 universal property를 적용하면 $y\otimes y'\mapsto m_{(y,y')}$이도록 하는 $A$-linear map $\tilde{m}:E\otimes_AE' \rightarrow \End_{\lMod{A}}(E\otimes_AE')$을 얻는다. 이제

$$\mu(s,t)=\tilde{m}(t)(s)$$

로 정의하면 $\mu$는 각 변수에 대해 $A$-linear이고, generator들 위에서 식 $(1)$을 만족한다. 유일성은 $E\otimes_AE'$이 $x\otimes x'$ 꼴의 원소들로 생성된다는 것으로부터 자명하다.
:::

::: 정의 7
두 $A$-algebra $E,E'$에 대하여, [명제 6](#prop6)의 곱셈이 주어진 $A$-algebra $E\otimes_AE'$을 $E$와 $E'$의 *tensor product<sub>텐서곱</sub>*이라 부른다.
:::

Direct product에서와 마찬가지로, tensor product는 두 대수의 성질을 그대로 물려받는다. 가령 $E,E'$이 모두 associative라면 generator들 위에서

$$\bigl((x\otimes x')(y\otimes y')\bigr)(z\otimes z')=(xy)z\otimes (x'y')z'=x(yz)\otimes x'(y'z')=(x\otimes x')\bigl((y\otimes y')(z\otimes z')\bigr)$$

이므로 $E\otimes_AE'$도 associative이고, 같은 방식으로 $E,E'$이 commutative라면 $E\otimes_AE'$도 commutative이다. 또 $E,E'$이 unital이라면 $1_E\otimes 1_{E'}$이 $E\otimes_AE'$의 항등원이 된다. 특히 $E,E'$이 associative unital이라면 두 $A$-algebra homomorphism

$$\iota:E \rightarrow E\otimes_AE';\quad x\mapsto x\otimes 1_{E'},\qquad \iota':E' \rightarrow E\otimes_AE';\quad x'\mapsto 1_E\otimes x'$$

이 정의되며, 이들의 image는 서로 commute한다. 즉 $(x\otimes 1)(1\otimes x')=x\otimes x'=(1\otimes x')(x\otimes 1)$이다. 

우리가 처음 도입했던 것과 같이, tensor product는 commutative $A$-algebra들의 category에서 coproduct가 된다. 이를 설명하는 것이 다음의 정리이다. 

::: 정리 8
Commutative $A$-algebra $E,E'$과, 임의의 commutative $A$-algebra $F$, 그리고 $A$-algebra homomorphism들 $u:E \rightarrow F$, $u':E' \rightarrow F$가 주어졌다 하자. 그럼 $w\circ\iota=u$, $w\circ\iota'=u'$을 만족하는 유일한 $A$-algebra homomorphism $w:E\otimes_AE' \rightarrow F$가 존재한다. 
:::
::: 증명
함수 $E\times E' \rightarrow F$를 $(x,x')\mapsto u(x)u'(x')$으로 정의하면 이는 $A$-bilinear이므로, $w(x\otimes x')=u(x)u'(x')$이도록 하는 유일한 $A$-linear map $w:E\otimes_AE' \rightarrow F$가 존재한다. $w$가 곱셈을 보존하는 것은 generator들 위에서 확인하면 충분한데,

$$w\bigl((x\otimes x')(y\otimes y')\bigr)=w(xy\otimes x'y')=u(xy)u'(x'y')=u(x)u(y)u'(x')u'(y')=u(x)u'(x')u(y)u'(y')=w(x\otimes x')w(y\otimes y')$$

이고, 네 번째 등식에서 $F$가 commutative라는 가정이 사용되었다. 또 $w(1_E\otimes 1_{E'})=u(1_E)u'(1_{E'})=1_F$이며, $w\circ\iota=u$와 $w\circ\iota'=u'$은 정의로부터 자명하다.

유일성을 보이자. $w'$이 같은 조건을 만족한다면, 임의의 generator에 대하여

$$w'(x\otimes x')=w'\bigl((x\otimes 1_{E'})(1_E\otimes x')\bigr)=w'(\iota(x))w'(\iota'(x'))=u(x)u'(x')=w(x\otimes x')$$

이므로 $w'=w$이다.
:::

즉, $E\otimes_AE'$은 commutative $A$-algebra들의 category에서 $E$와 $E'$의 coproduct이다.

::: 예시 9
Polynomial algebra들의 tensor product는 변수들을 합친 polynomial algebra이다. 즉

$$A[\x]\otimes_AA[\y]\cong A[\x,\y]$$

이 성립한다. 이는 [§대수, ⁋명제 8](/ko/math/algebraic_structures/algebras#prop8)에서 살펴본 functor $A[-]:\Set \rightarrow \cAlg{A}$가 left adjoint라는 사실로부터 나온다. Left adjoint는 colimit을 보존하므로, 한 점 집합들의 (집합에서의) coproduct $\{\x\}\sqcup\{\y\}=\{\x,\y\}$를 $\cAlg{A}$에서의 coproduct로 보내고, [정리 8](#thm8)에 의하여 이는 정확히 tensor product이기 때문이다. 물론 두 isomorphism $\x\otimes 1\mapsto \x$, $1\otimes \y\mapsto \y$를 직접 확인할 수도 있다.
:::

---

**참고문헌**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  

---
