---
title: "복소 스펙트럼 정리"
description: "복소내적공간 위에서 self-adjoint operator를 일반화한 normal operator를 정의하고, normal operator가 정확히 orthonormal basis로 대각화되는 작용소임을 증명한다. self-adjoint operator의 실고윳값과 unitary operator의 단위원 고윳값을 특수한 경우로 얻는다."
excerpt: "normal operator의 unitary 대각화"

categories: [Math / Linear Algebra]
permalink: /ko/math/linear_algebra/complex_spectral_theorem
sidebar: 
    nav: "linear_algebra-ko"


date: 2026-06-25

weight: 121

drift_needed: true

published: false

---

[§스펙트럼 정리](/ko/math/linear_algebra/spectral_theorem)에서 우리는 $$\mathbb{R}$$-내적공간 위의 self-adjoint operator가 정확히 orthonormal basis로 대각화됨을 보았으며, 그 과정에서 필수적으로 $$\mathbb{C}$$로 올라가야 했었다. 이제 우리는 복소수 행렬들에 대해 spectral theorem이 어떠한 정리를 주는지를 살펴본다. 

## 자기수반작용소와 정규작용소

우선 첫 단계는 실수의 경우와 똑같이 자기 자신과 adjoint가 일치하는 operator에 이름을 붙여주는 것이다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 복소내적공간 $$V$$ 위의 linear operator $$L:V\rightarrow V$$가 *self-adjoint<sub>자기수반</sub>*, 또는 *Hermitian*이라는 것은 $$L=L^\ast$$인 것, 즉 모든 $$v,w\in V$$에 대하여 $$\langle Lv,w\rangle=\langle v,Lw\rangle$$인 것이다.

</div>

즉, 이는 내적이 주는 isomorphism을 통해 $$V^\ast$$를 $$V$$로 옮겨왔을 때, dual operator $$L^\ast: V^\ast\rightarrow V^\ast$$가 $$V$$로 번역된 것이 곧 자기자신이라는 것이다. 실수행렬의 경우, 이는 symmetric matrix로 나왔으나 복소수의 경우 이것이 conjugate-tranpose matrix로 나온다는 점만 다르다. 다소 헷갈릴 수 있는 지점은 $$L^\ast$$가 이제 conjugate-transpose이자 dual map을 나타내는 표기가 된다는 것이지만, 위에서 살펴봤듯 complex inner product space가 주는 isomorphism을 통해 $$V$$와 $$V^\ast$$를 같은 것으로 보면 이들 둘이 실제로 같아지므로 큰 해는 없다. 

실수에서와 다른 점 중 하나는 이제 self-adjoint operator들만이 orthonormal basis로 대각화되는 것이 <em-ko>아니라는</em-ko> 것으로, 이를 위해서는 다음 정의와 같이 일반화를 해야 한다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 복소내적공간 $$V$$ 위의 linear operator $$L:V\rightarrow V$$가 *normal operator<sub>정규작용소</sub>*라는 것은

$$LL^\ast=L^\ast L$$

이 성립하는 것이다.

</div>

그럼 특히 self-adjoint operator는 $$LL^\ast=L^2=L^\ast L$$이므로 normal operator이고, unitary operator 또한 그러하다. ([§복소내적공간, ⁋정의 5](/ko/math/linear_algebra/complex_inner_product_spaces#def5)) 뿐만 아니라, $$L^\ast=-L$$을 만족하는 *skew-Hermitian* operator도 $$LL^\ast=-L^2=L^\ast L$$이므로 normal operator이며, 이렇듯 normal operator는 여러 특수한 경우들을 포함하는 넓은 부류이며, 이 글의 목표는 이들이 정확히 orthonormal basis로 대각화되는 operator임을 보이는 것이다.

## Schur 분해

복소내적공간 위에서는 임의의 linear operator라도 orthonormal basis에 대해 upper triangular matrix와 닮아있음을 보일 수 있다. 이것이 Schur decomposition이며, normal operator의 경우 이 upper triangular matrix가 자동으로 대각이 되어 복소 스펙트럼 정리를 되돌려준다.

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3 (Schur)**</ins> 복소내적공간 $$V$$ 위의 임의의 linear operator $$L:V\rightarrow V$$에 대하여, $$L$$의 행렬표현이 upper triangular matrix가 되도록 하는 $$V$$의 orthonormal basis가 존재한다. 행렬의 언어로는, 임의의 $$A\in\Mat_n(\mathbb{C})$$에 대하여 적당한 unitary matrix $$U$$와 upper triangular matrix $$T$$가 존재하여 $$A=UTU^\ast$$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\dim V$$에 대한 귀납법으로 진행한다. 우리는 $$V$$의 orthonormal basis $$\{e_1,\ldots,e_n\}$$이 존재하여 각 $$j$$에 대해 $$Le_j\in\span(e_1,\ldots,e_j)$$임을 보여야 한다. $$\dim V\leq 1$$인 경우는 자명하므로, $$\dim V=n\geq 2$$라 하자.

$$L^\ast$$의 특성다항식은 차수가 $$1$$ 이상이므로 [§특성다항식, ⁋정리 8](/ko/math/linear_algebra/characteristic_polynomial#thm8)에 의하여 근을 가지고, 따라서 $$L^\ast$$은 $$\lVert e_n\rVert=1$$인 고유벡터 $$e_n$$을 가진다. 이제 $$V$$에서 $$e_n$$이 span하는 직선의 complement $$W=(\span e_n)^\perp$$를 생각하자. 그럼

$$\langle Lw,e_n\rangle=\langle w,L^\ast e_n\rangle=\langle w,\mu e_n\rangle=\mu\langle w,e_n\rangle=0$$

이므로 $$Lw\in W$$이다. 즉, $$W$$는 $$L$$에 대해 닫혀있으며, 이로부터 $$L\vert_W$$를 $$W$$ 위에 정의된 linear operator로 볼 수 있고, 이제 귀납적 가정에 의해
 $$W$$의 orthonormal basis $$\{e_1,\ldots,e_{n-1}\}$$이 존재하여 각 $$j\leq n-1$$에 대해 $$Le_j\in\span(e_1,\ldots,e_j)$$이다.

그럼 $$\{e_1,\ldots,e_n\}$$은 $$V$$의 orthonormal basis이고, $$j<n$$에 대해서는 $$Le_j\in\span(e_1,\ldots,e_j)$$이며 $$j=n$$에 대해서는 $$Le_n\in V=\span(e_1,\ldots,e_n)$$이 자명하게 성립한다. 즉 이 기저에 대한 $$L$$의 행렬표현은 upper triangular matrix가 된다. 이 기저의 벡터들을 열로 갖는 행렬을 $$U$$라 하면 $$U$$는 unitary이고 ([§복소내적공간, ⁋정의 5](/ko/math/linear_algebra/complex_inner_product_spaces#def5)) $$U^\ast AU=T$$가 upper triangular이므로 $$A=UTU^\ast$$이다.

</details>

Upper triangular matrix $$T$$는 $$A$$와 닮음이므로 같은 특성다항식을 가지며, upper triangular matrix의 특성다항식은 $$\prod_i(\x-T_{ii})$$이므로 $$T$$의 대각성분 $$T_{11},\ldots,T_{nn}$$은 정확히 $$A$$의 고윳값들을 중복도까지 담는다. Schur 분해는 임의의 복소행렬이 unitary transformation만으로 고윳값들을 대각선에 드러낼 수 있음을 말한다.

만일 추가로 주어진 행렬이 normal이었다면, 이 upper triangular matrix가 추가로 대각행렬이 된다.

<div class="proposition" markdown="1">

<ins id="cor4">**따름정리 4**</ins> Normal matrix $$A\in\Mat_n(\mathbb{C})$$는 unitary matrix로 대각화된다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[정리 3](#thm3)에 의하여 $$A=UTU^\ast$$이고 $$T$$는 upper triangular이도록 할 수 있으며, 우리가 보여야 할 것은 만일 $$A$$가 normal이라면 $$T$$가 diagonal인 것을 보이는 것이다. 

다. $$A$$가 normal matrix이고 $$U$$가 unitary이므로 $$T=U^\ast AU$$ 또한 normal matrix이다. upper triangular이면서 normal인 $$T$$가 대각임을 $$T$$의 행에 대한 귀납법으로 보인다.

$$T$$가 upper triangular이므로 $$T$$의 첫째 열은 $$(T_{11},0,\ldots,0)^t$$이고, 따라서 $$\lVert Te_1\rVert^2=\lvert T_{11}\rvert^2$$이다. 한편 $$T^\ast$$의 첫째 열은 $$T$$의 첫째 행의 켤레이므로 $$\lVert T^\ast e_1\rVert^2=\sum_{j}\lvert T_{1j}\rvert^2$$이다. $$T$$가 normal이므로

$$\lVert Te_1\rVert^2=\langle Te_1,Te_1\rangle=\langle e_1,T^\ast Te_1\rangle=\langle e_1,TT^\ast e_1\rangle=\langle T^\ast e_1,T^\ast e_1\rangle=\lVert T^\ast e_1\rVert^2$$

이고, 따라서 $$\lvert T_{11}\rvert^2=\sum_{j}\lvert T_{1j}\rvert^2$$이므로 $$j>1$$에 대해 $$T_{1j}=0$$이다. 즉 첫째 행은 대각성분을 제외하면 모두 $$0$$이다. 그럼 $$T$$의 둘째 행 이하는 첫째 행·열을 떼어 낸 $$(n-1)\times(n-1)$$ upper triangular normal matrix를 이루므로, 귀납적으로 그것도 대각이 되어 $$T$$ 전체가 대각이다. 따라서 $$A=UTU^\ast$$은 unitary diagonalization이다.

</details>

Schur 분해는 [§조르당 표준형](/ko/math/linear_algebra/Jordan_canonical_form)과 좋은 대조를 이룬다. 조르당 표준형은 일반적으로 unitary가 아닌 기저변환을 써서 행렬을 표준적인 block 형태로 만드는 반면, Schur 분해는 기저변환을 unitary로 제한하는 대신 표준형을 포기하고 upper triangular 형태에 만족한다. 후자는 orthonormality이 보존되어 수치적으로 안정적이라는 장점이 있어 응용에서 자주 쓰인다.

## 복소 스펙트럼 정리

Normal matrix의 unitary 대각화는 Schur 분해의 직접적 결과이다. 더 정밀하게, normal operator가 정확히 orthonormal basis로 대각화되는 operator임을 보인다.

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5 (복소 스펙트럼 정리)**</ins> 복소내적공간 $$V$$ 위의 linear operator $$L:V\rightarrow V$$가 normal operator인 것은, $$L$$의 고유벡터들로 이루어진 $$V$$의 orthonormal basis가 존재하는 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

($$\Rightarrow$$) [따름정리 4](#cor4)에 의하여 $$L$$은 orthonormal basis로 대각화된다.

($$\Leftarrow$$) $$L$$의 고유벡터들로 이루어진 orthonormal basis $$\{v_1,\ldots,v_n\}$$이 존재하여 $$Lv_i=\lambda_i v_i$$라 하자. [§복소내적공간, ⁋명제 4](/ko/math/linear_algebra/complex_inner_product_spaces#prop4)에 의해, 이 기저에 대한 $$L^\ast$$의 행렬표현은 $$\diag(\bar\lambda_1,\ldots,\bar\lambda_n)$$이다. 두 대각행렬은 가환이므로 $$LL^\ast=L^\ast L$$이고, 따라서 $$L$$은 normal operator이다.

</details>

행렬의 언어로 옮기면 정리는 normal matrix의 unitary diagonalization에 대한 이야기이다.

<div class="proposition" markdown="1">

<ins id="cor6">**따름정리 6**</ins> 행렬 $$A\in\Mat_n(\mathbb{C})$$가 normal matrix인 것은, 적당한 unitary matrix $$U$$와 대각행렬 $$D$$가 존재하여

$$A=UDU^\ast$$

이 성립하는 것과 동치이다. 이 때 $$D$$의 대각성분은 $$A$$의 고윳값들이고, $$U$$의 열들은 이에 대응되는 orthonormal eigenvector들이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$A$$를 $$\mathbb{C}^n$$ 위의 normal operator로 보면, [정리 5](#thm5)에 의하여 $$A$$의 고유벡터들로 이루어진 orthonormal basis $$\{v_1,\ldots,v_n\}$$이 존재한다. $$Av_i=\lambda_iv_i$$라 하고 $$v_i$$를 열로 갖는 행렬 $$U=(v_1\mid\cdots\mid v_n)$$을 생각하면, 열들이 orthonormal이므로 $$U$$는 unitary matrix이다. ([§복소내적공간, ⁋정의 5](/ko/math/linear_algebra/complex_inner_product_spaces#def5)) 그럼

$$AU=(\lambda_1v_1\mid\cdots\mid\lambda_nv_n)=UD$$

이고, 오른쪽에서 $$U^\ast=U^{-1}$$을 곱하면 $$A=UDU^\ast$$를 얻는다. 거꾸로 $$A=UDU^\ast$$이면 대각행렬 $$D$$가 $$D^\ast=\bar D$$와 가환이므로

$$AA^\ast=UDU^\ast UD^\ast U^\ast=UDD^\ast U^\ast=UD^\ast DU^\ast=A^\ast A$$

가 되어 $$A$$는 normal matrix이다.

</details>

## 특수한 경우

self-adjoint operator와 unitary operator는 normal operator이므로 [정리 5](#thm5)에 의하여 모두 orthonormal basis로 대각화된다. 두 경우 고윳값이 특별한 위치에 놓인다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> 복소내적공간 위의 self-adjoint operator의 모든 고윳값은 실수이고, unitary operator의 모든 고윳값은 절댓값이 $$1$$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$L$$이 self-adjoint이고 $$Lv=\lambda v$$, $$v\neq 0$$이라 하자. $$\langle Lv,v\rangle$$을 두 가지로 계산하면, 둘째 변수의 linearity로부터 $$\langle v,Lv\rangle=\langle v,\lambda v\rangle=\lambda\lVert v\rVert^2$$이고 $$L=L^\ast$$이므로 $$\langle Lv,v\rangle=\langle v,L^\ast v\rangle=\langle v,Lv\rangle=\lambda\lVert v\rVert^2$$이다. 한편 첫째 변수의 conjugate-linearity로부터

$$\langle Lv,v\rangle=\langle\lambda v,v\rangle=\bar\lambda\lVert v\rVert^2$$

이다. 두 식을 비교하면 $$\lambda\lVert v\rVert^2=\bar\lambda\lVert v\rVert^2$$이고 $$\lVert v\rVert^2>0$$이므로 $$\lambda=\bar\lambda$$, 즉 $$\lambda$$는 실수이다.

$$L$$이 unitary이고 $$Lv=\lambda v$$, $$v\neq 0$$이라 하자. unitary operator는 내적을 보존하므로

$$\lVert v\rVert^2=\langle Lv,Lv\rangle=\langle\lambda v,\lambda v\rangle=\bar\lambda\lambda\lVert v\rVert^2=\lvert\lambda\rvert^2\lVert v\rVert^2$$

이고, $$\lVert v\rVert^2>0$$이므로 $$\lvert\lambda\rvert^2=1$$, 즉 $$\lvert\lambda\rvert=1$$이다.

</details>

<div class="remark" markdown="1">

<ins id="rmk8">**참고 8**</ins> 복소 스펙트럼 정리는 실수판 ([§스펙트럼 정리, ⁋정리 5](/ko/math/linear_algebra/spectral_theorem#thm5))을 특수한 경우로 포함한다. 실대칭행렬 $$A$$는 성분이 실수이므로 $$A^\ast=\bar A^t=A^t=A$$가 되어 Hermitian 행렬이고, 따라서 [명제 7](#prop7)에 의하여 그 고윳값은 모두 실수이다. 실수 고윳값 $$\lambda$$에 대하여 $$\lambda I-A$$는 실행렬이므로 그 kernel에서 실벡터인 고유벡터를 택할 수 있고, 이로부터 실내적공간 위에서의 직교대각화가 따라온다. 실수판에서 실대칭행렬의 고윳값이 실수임을 보일 때 ([§스펙트럼 정리, ⁋보조정리 2](/ko/math/linear_algebra/spectral_theorem#lem2)) $$\mathbb{C}^n$$ 위의 Hermitian 내적을 "계산을 위한 도구"로만 끌어다 썼던 것은, 바로 이 [명제 7](#prop7)의 self-adjoint 고윳값의 실수성을 미리 사용한 것이었다.

</div>

---

**참고문헌**

**[Axl]** S. Axler, *Linear algebra done right*, 3rd ed., Undergraduate Texts in Mathematics, Springer, 2015.  
**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.  
**[Lee]** 이인석, *선형대수와 군*, 서울대학교 출판문화원, 2005.

---
