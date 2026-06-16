---
title: "행렬의 텐서곱"
description: "행렬의 텐서곱은 선형 사상의 텐서곱을 크로네커 곱으로 구현하는 행렬 연산이다. 텐서곱 위에서 유도되는 이 연산의 정의와 기본 성질을 정리한다."
excerpt: "Tensor product에 대응하는 Kronecker product 행렬연산"

categories: [Math / Multilinear Algebra]
permalink: /ko/math/multilinear_algebra/tensor_product_of_matrices
sidebar: 
    nav: "multilinear_algebra-ko"

date: 2024-10-06
weight: 9
published: false

---

[§행렬과 선형사상](/ko/math/multilinear_algebra/matrices_and_linear_maps)에서 우리는 free $$A$$-module들 사이의 linear map을 행렬로 표현하였고, linear map들의 합성이 행렬의 곱셈에 대응된다는 것을 살펴보았다. 한편 linear map들에 대해 우리가 할 수 있는 또 다른 연산으로 텐서곱이 있으므로, 이 연산이 행렬표현의 단계에서 어떤 행렬 연산으로 나타나는지 묻는 것이 자연스럽다. 이번 글에서는 그 답인 행렬의 텐서곱, 즉 Kronecker product를 살펴본다. 이번 글에서 $$A$$는 항상 commutative ring이다.

## 선형사상의 텐서곱

네 개의 $$A$$-module $$M,M',L,L'$$과 linear map들 $$u:M \rightarrow L$$, $$u':M' \rightarrow L'$$이 주어졌다 하자. 그럼 함수

$$M\times M' \rightarrow L\otimes_AL';\qquad (x,x')\mapsto u(x)\otimes u'(x')$$

는 $$A$$-bilinear이므로, 텐서곱의 universal property ([\[대수적 구조\] §가군의 직접곱과 직합, 텐서곱, ⁋명제 8](/ko/math/algebraic_structures/operations_of_modules#prop8))에 의하여 다음 정의가 잘 정의된다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 위와 같은 상황에서, $$u$$와 $$u'$$의 *tensor product<sub>텐서곱</sub>* $$u\otimes u': M\otimes_AM' \rightarrow L\otimes_AL'$$은 다음 식

$$(u\otimes u')(x\otimes x')=u(x)\otimes u'(x')$$

을 만족하는 유일한 $$A$$-linear map이다.

</div>

이 정의는 $$\otimes_A$$를 두 변수의 functor로 보았을 때 morphism들에 대한 작용을 준 것이다. 실제로 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> Linear map들 $$v:N \rightarrow M$$, $$v':N' \rightarrow M'$$, $$u:M \rightarrow L$$, $$u':M' \rightarrow L'$$에 대하여 다음 식

$$(u\otimes u')\circ(v\otimes v')=(u\circ v)\otimes(u'\circ v'),\qquad \id_M\otimes\id_{M'}=\id_{M\otimes_AM'}$$

이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

양변 모두 $$A$$-linear map이므로 $$M\otimes_AM'$$ 혹은 $$N\otimes_AN'$$의 생성원들 위에서 일치하는 것만 확인하면 충분하다. 임의의 $$y\otimes y'\in N\otimes_AN'$$에 대하여

$$\bigl((u\otimes u')\circ(v\otimes v')\bigr)(y\otimes y')=(u\otimes u')\bigl(v(y)\otimes v'(y')\bigr)=u(v(y))\otimes u'(v'(y'))=\bigl((u\circ v)\otimes (u'\circ v')\bigr)(y\otimes y')$$

이고, $$(\id_M\otimes\id_{M'})(x\otimes x')=x\otimes x'$$이다.

</details>

## 텐서곱의 기저

행렬표현을 위해서는 $$M\otimes_AM'$$의 basis가 필요하다.

<div class="proposition" markdown="1">

<ins id="lem3">**보조정리 3**</ins> Free $$A$$-module $$M,M'$$의 basis $$\mathcal{B}=(e_i)_{i\in I}$$, $$\mathcal{B}'=(e'_{i'})_{i'\in I'}$$가 주어졌다 하자. 그럼 family

$$\mathcal{B}\otimes\mathcal{B}'=(e_i\otimes e'_{i'})_{(i,i')\in I\times I'}$$

는 $$M\otimes_AM'$$의 basis이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Basis의 정의에 의하여 isomorphism $$M\cong\bigoplus_{i\in I}A$$, $$M'\cong\bigoplus_{i'\in I'}A$$이 존재한다. 한편 [\[대수적 구조\] §가군의 직접곱과 직합, 텐서곱, ⁋정리 9](/ko/math/algebraic_structures/operations_of_modules#thm9)의 adjunction에 의하여 functor $$-\otimes_AN$$은 left adjoint이므로 colimit을, 특히 direct sum을 보존한다. 이를 두 변수에 대해 차례로 적용하면

$$M\otimes_AM'\cong\left(\bigoplus_{i\in I}A\right)\otimes_AM'\cong\bigoplus_{i\in I}(A\otimes_AM')\cong \bigoplus_{i\in I}\bigoplus_{i'\in I'}(A\otimes_AA)\cong\bigoplus_{(i,i')\in I\times I'}A$$

이다. 여기서 $$A\otimes_AA\cong A$$는 곱셈 $$a\otimes b\mapsto ab$$로 주어지는 isomorphism이다. 이 isomorphism들의 합성을 추적하면 $$e_i\otimes e'_{i'}$$는 정확히 $$(i,i')$$번째 성분의 $$1$$로 옮겨지므로, $$(e_i\otimes e'_{i'})_{(i,i')\in I\times I'}$$는 $$M\otimes_AM'$$의 basis이다.

</details>

## 행렬의 텐서곱

이제 행렬의 단계에서 텐서곱에 대응하는 연산을 정의하자. [§행렬, ⁋정의 1](/ko/math/multilinear_algebra/matrices#def1)에서 행렬의 index를 임의의 집합으로 허용해 두었으므로, 다음 정의는 자연스럽다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> 두 행렬 $$X=(x_{ji})\in\Mat_{J\times I}(A)$$, $$X'=(x'_{j'i'})\in\Mat_{J'\times I'}(A)$$에 대하여, 이들의 *tensor product<sub>텐서곱</sub>* 혹은 *Kronecker product<sub>크로네커 곱</sub>* $$X\otimes X'$$은 다음 식

$$(X\otimes X')_{(j,j'),(i,i')}=x_{ji}x'_{j'i'}$$

으로 정의된 $$(J\times J')\times (I\times I')$$ 행렬이다.

</div>

특별히 $$I,J,I',J'$$가 유한집합 $$\{1,\ldots,m\}$$ 꼴이라 하고 $$I\times I'$$, $$J\times J'$$에 사전식 순서를 주면, $$X\otimes X'$$은 $$X$$의 각 성분 $$x_{ji}$$ 자리에 블록 $$x_{ji}X'$$을 채워넣은 블록행렬

$$X\otimes X'=\begin{pmatrix}x_{11}X'&x_{12}X'&\cdots\\x_{21}X'&x_{22}X'&\cdots\\\vdots&\vdots&\ddots\end{pmatrix}$$

이 된다. 이것이 Kronecker product의 표준적인 표기이다.

이 연산이 실제로 linear map들의 텐서곱을 구현한다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> Free $$A$$-module들 $$M,M',L,L'$$의 basis $$\mathcal{B}=(e_i)_{i\in I}$$, $$\mathcal{B}'=(e'_{i'})_{i'\in I'}$$, $$\mathcal{C}=(f_j)_{j\in J}$$, $$\mathcal{C}'=(f'_{j'})_{j'\in J'}$$와 linear map들 $$u:M \rightarrow L$$, $$u':M' \rightarrow L'$$에 대하여 다음 식

$$[u\otimes u']_{\mathcal{C}\otimes\mathcal{C}'}^{\mathcal{B}\otimes\mathcal{B}'}=[u]_\mathcal{C}^\mathcal{B}\otimes[u']_{\mathcal{C}'}^{\mathcal{B}'}$$

이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$[u]_\mathcal{C}^\mathcal{B}=(x_{ji})$$, $$[u']_{\mathcal{C}'}^{\mathcal{B}'}=(x'_{j'i'})$$라 하자. 행렬표현의 정의 ([§행렬과 선형사상, ⁋정의 1](/ko/math/multilinear_algebra/matrices_and_linear_maps#def1))에 의하여

$$u(e_i)=\sum_{j\in J}x_{ji}f_j,\qquad u'(e'_{i'})=\sum_{j'\in J'}x'_{j'i'}f'_{j'}$$

이고, 따라서

$$(u\otimes u')(e_i\otimes e'_{i'})=u(e_i)\otimes u'(e'_{i'})=\sum_{(j,j')\in J\times J'}x_{ji}x'_{j'i'}\,(f_j\otimes f'_{j'})$$

이다. [보조정리 3](#lem3)에 의해 $$(f_j\otimes f'_{j'})$$들이 $$L\otimes_AL'$$의 basis이므로, $$[u\otimes u']_{\mathcal{C}\otimes\mathcal{C}'}^{\mathcal{B}\otimes\mathcal{B}'}$$의 $$\bigl((j,j'),(i,i')\bigr)$$ 성분은 $$x_{ji}x'_{j'i'}$$이고, 이는 정확히 $$[u]_\mathcal{C}^\mathcal{B}\otimes[u']_{\mathcal{C}'}^{\mathcal{B}'}$$의 해당 성분이다.

</details>

## 텐서곱의 성질

행렬의 텐서곱의 기본 성질들을 살펴보자. 가장 중요한 것은 행렬의 곱셈과의 호환성으로, *mixed product property*라 부르기도 한다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> 행렬 $$X\in\Mat_{K\times J}(A)$$, $$Y\in\Mat_{J\times I}(A)$$, $$X'\in\Mat_{K'\times J'}(A)$$, $$Y'\in\Mat_{J'\times I'}(A)$$가 주어졌다 하고, $$J,J'$$는 유한집합이라 하자. 그럼 다음 식

$$(X\otimes X')(Y\otimes Y')=(XY)\otimes(X'Y')$$

이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

좌변의 $$\bigl((k,k'),(i,i')\bigr)$$ 성분을 행렬 곱셈의 정의에 따라 계산하면

$$\sum_{(j,j')\in J\times J'}(X\otimes X')_{(k,k'),(j,j')}(Y\otimes Y')_{(j,j'),(i,i')}=\sum_{(j,j')\in J\times J'}x_{kj}x'_{k'j'}y_{ji}y'_{j'i'}=\left(\sum_{j\in J}x_{kj}y_{ji}\right)\left(\sum_{j'\in J'}x'_{k'j'}y'_{j'i'}\right)$$

이고, 이는 $$(XY)_{ki}(X'Y')_{k'i'}$$, 즉 우변의 해당 성분과 같다. 마지막 등식에서 $$A$$의 commutativity를 사용하였다.

</details>

물론 이 명제는 [명제 2](#prop2)와 [명제 5](#prop5), 그리고 합성의 행렬표현이 행렬곱이라는 사실 ([§행렬과 선형사상, ⁋따름정리 4](/ko/math/multilinear_algebra/matrices_and_linear_maps#cor4))을 조합하여 얻을 수도 있다. 이로부터 다음의 성질들이 따라나온다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> 행렬 $$X\in\Mat_{J\times I}(A)$$, $$X'\in\Mat_{J'\times I'}(A)$$에 대하여 다음이 성립한다.

1. $$(X\otimes X')^t=X^t\otimes X'^t$$.
2. $$I,I'$$가 유한집합이고 $$X,X'$$이 모두 invertible인 정사각행렬이라면, $$X\otimes X'$$도 invertible이고 $$(X\otimes X')^{-1}=X^{-1}\otimes X'^{-1}$$이다.
3. $$I,I'$$가 유한집합이고 $$X,X'$$이 정사각행렬이라면 $$\tr(X\otimes X')=\tr(X)\tr(X')$$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

첫째 식은 성분의 계산으로, transpose의 정의에 의하여

$$\bigl((X\otimes X')^t\bigr)_{(i,i'),(j,j')}=(X\otimes X')_{(j,j'),(i,i')}=x_{ji}x'_{j'i'}=(X^t)_{ij}(X'^t)_{i'j'}=(X^t\otimes X'^t)_{(i,i'),(j,j')}$$

이다.

둘째 주장을 보이자. 단위행렬들에 대하여 $$E_I\otimes E_{I'}=E_{I\times I'}$$인 것은 정의로부터 자명하다. 그럼 [명제 6](#prop6)에 의하여

$$(X\otimes X')(X^{-1}\otimes X'^{-1})=(XX^{-1})\otimes(X'X'^{-1})=E_I\otimes E_{I'}=E_{I\times I'}$$

이고, 반대 방향의 곱도 마찬가지이다.

마지막으로 trace를 계산하면

$$\tr(X\otimes X')=\sum_{(i,i')\in I\times I'}(X\otimes X')_{(i,i'),(i,i')}=\sum_{i\in I}\sum_{i'\in I'}x_{ii}x'_{i'i'}=\left(\sum_{i\in I}x_{ii}\right)\left(\sum_{i'\in I'}x'_{i'i'}\right)=\tr(X)\tr(X')$$

이다.

</details>

셋째 성질은 linear map의 단계에서 보면 $$\tr(u\otimes u')=\tr(u)\tr(u')$$이라는 것으로, trace가 행렬표현의 선택에 의존하지 않는다는 사실 ([§행렬과 선형사상, §§행렬표현과 trace](/ko/math/multilinear_algebra/matrices_and_linear_maps))과 [명제 5](#prop5)를 결합한 것이다.

---

**참고문헌**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  

---
