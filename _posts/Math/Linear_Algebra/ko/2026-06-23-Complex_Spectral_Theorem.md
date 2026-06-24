---
title: "복소 스펙트럼 정리"
description: "복소내적공간 위에서 self-adjoint operator를 일반화한 normal operator를 정의하고, normal operator가 정확히 orthonormal basis로 대각화되는 작용소임을 증명한다. self-adjoint operator의 실고윳값과 unitary operator의 단위원 고윳값을 특수한 경우로 얻는다."
excerpt: "normal operator의 unitary 대각화"

categories: [Math / Linear Algebra]
permalink: /ko/math/linear_algebra/complex_spectral_theorem
sidebar: 
    nav: "linear_algebra-ko"


date: 2026-06-23

weight: 121

drift_needed: true

published: false

---

[§스펙트럼 정리](/ko/math/linear_algebra/spectral_theorem)에서 우리는 $$\mathbb{R}$$-내적공간 위의 self-adjoint operator가 정확히 orthonormal basis로 대각화됨을 보았다. 그 증명의 출발점은 실대칭행렬의 고윳값이 모두 실수라는 사실이었고, 이는 대각화의 걸림돌이 고윳값의 존재가 아니라 고윳값이 실수인지였음을 뜻한다.

$$\mathbb{C}$$ 위에서는 사정이 다르다. 대수학의 기본정리에 의하여 임의의 operator는 항상 고윳값을 가지므로, 고윳값의 존재나 실수성은 더 이상 문제가 되지 않는다. 그 결과 orthonormal basis로 대각화되는 작용소의 범위가 self-adjoint operator보다 넓어지며, 이 글에서는 그 정확한 범위가 *normal operator*임을 보인다. 우리는 [§복소내적공간](/ko/math/linear_algebra/complex_inner_product_spaces)을 따라 복소내적공간 위에서 이론을 전개한다.

## 자기수반작용소와 정규작용소

[§복소내적공간, ⁋명제 4](/ko/math/linear_algebra/complex_inner_product_spaces#prop4)에서 orthonormal basis에 대한 adjoint의 행렬표현이 켤레전치임을 보았다. 실수의 경우와 똑같이 자기 자신과 adjoint가 일치하는 operator를 생각할 수 있다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 복소내적공간 $$V$$ 위의 linear operator $$L:V\rightarrow V$$가 *self-adjoint<sub>자기수반</sub>*, 또는 *Hermitian*이라는 것은 $$L=L^\ast$$인 것, 즉 모든 $$v,w\in V$$에 대하여 $$\langle Lv,w\rangle=\langle v,Lw\rangle$$인 것이다.

</div>

[§복소내적공간, ⁋명제 4](/ko/math/linear_algebra/complex_inner_product_spaces#prop4)에 의하여 $$L$$이 self-adjoint인 것은 그 행렬표현 $$A$$가 $$A=A^\ast=\bar A^t$$를 만족하는 것, 즉 *Hermitian 행렬*인 것과 동치이다. 그러나 실수의 경우와 달리, $$\mathbb{C}$$ 위에서는 self-adjoint이 아니면서도 orthonormal basis로 대각화되는 operator가 존재한다. 가령 unitary operator는 self-adjoint이 아니지만, 곧 보듯 대각화된다. 이들을 모두 포괄하는 조건은 $$L$$과 $$L^\ast$$가 가환이라는 것이다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 복소내적공간 $$V$$ 위의 linear operator $$L:V\rightarrow V$$가 *normal operator<sub>정규작용소</sub>*라는 것은

$$LL^\ast=L^\ast L$$

이 성립하는 것이다.

</div>

self-adjoint operator($$L=L^\ast$$)는 $$LL^\ast=L^2=L^\ast L$$이므로 normal operator이고, unitary operator($$L^\ast L=LL^\ast=I$$) 또한 normal operator이다. $$L^\ast=-L$$을 만족하는 *skew-Hermitian* operator도 $$LL^\ast=-L^2=L^\ast L$$이므로 normal operator이다. 이렇듯 normal operator는 self-adjoint·unitary·skew-Hermitian을 모두 특수한 경우로 포함하는 넓은 부류이며, 이 글의 목표는 이들이 정확히 orthonormal basis로 대각화되는 operator임을 보이는 것이다.

## 정규작용소의 고유벡터

normal operator의 핵심 성질은 $$L$$과 $$L^\ast$$가 벡터를 같은 크기로 보낸다는 것이다.

<div class="proposition" markdown="1">

<ins id="lem3">**보조정리 3**</ins> $$L$$이 복소내적공간 $$V$$ 위의 normal operator이면, 모든 $$v\in V$$에 대하여 $$\lVert Lv\rVert=\lVert L^\ast v\rVert$$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

adjoint의 정의와 $$(L^\ast)^\ast=L$$, 그리고 정규성 $$L^\ast L=LL^\ast$$을 차례로 쓰면

$$\lVert Lv\rVert^2=\langle Lv,Lv\rangle=\langle v,L^\ast Lv\rangle=\langle v,LL^\ast v\rangle=\langle L^\ast v,L^\ast v\rangle=\lVert L^\ast v\rVert^2$$

이다. 양변이 음이 아니므로 $$\lVert Lv\rVert=\lVert L^\ast v\rVert$$을 얻는다.

</details>

이로부터 normal operator의 고유벡터가 곧 그 adjoint의 고유벡터임이 따라온다.

<div class="proposition" markdown="1">

<ins id="cor4">**따름정리 4**</ins> $$L$$이 normal operator이고 $$\lambda\in\mathbb{C}$$일 때, $$v$$가 고윳값 $$\lambda$$를 갖는 $$L$$의 고유벡터인 것은 $$v$$가 고윳값 $$\bar\lambda$$를 갖는 $$L^\ast$$의 고유벡터인 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$L-\lambda I$$ 또한 normal operator이다. 실제로 $$(L-\lambda I)^\ast=L^\ast-\bar\lambda I$$이고

$$\begin{aligned}
(L-\lambda I)(L^\ast-\bar\lambda I)&=LL^\ast-\bar\lambda L-\lambda L^\ast+\lvert\lambda\rvert^2I,\\
(L^\ast-\bar\lambda I)(L-\lambda I)&=L^\ast L-\lambda L^\ast-\bar\lambda L+\lvert\lambda\rvert^2I
\end{aligned}$$

이 $$LL^\ast=L^\ast L$$ 덕분에 일치하기 때문이다. 따라서 [보조정리 3](#lem3)을 $$L-\lambda I$$에 적용하면

$$\lVert(L-\lambda I)v\rVert=\lVert(L-\lambda I)^\ast v\rVert=\lVert(L^\ast-\bar\lambda I)v\rVert$$

이고, 좌변이 $$0$$인 것과 우변이 $$0$$인 것이 동치이다. 즉 $$Lv=\lambda v$$인 것과 $$L^\ast v=\bar\lambda v$$인 것이 동치이다.

</details>

## 복소 스펙트럼 정리

실수의 경우와 마찬가지로, 핵심은 불변부분공간의 orthogonal complement이 다시 불변으로 남는다는 것이다. 다만 복소의 경우에는 $$L$$과 $$L^\ast$$ 양쪽에 대한 불변성을 함께 다루어야 한다.

<div class="proposition" markdown="1">

<ins id="lem5">**보조정리 5**</ins> $$L$$이 복소내적공간 $$V$$ 위의 normal operator이고, 부분공간 $$U\leq V$$가 $$L(U)\subseteq U$$와 $$L^\ast(U)\subseteq U$$를 모두 만족한다고 하자. 그럼 $$U^\perp$$ 또한 $$L$$과 $$L^\ast$$에 대해 불변이며, 제한 $$L\vert_{U^\perp}$$은 $$U^\perp$$ 위에서 다시 normal operator이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $$w\in U^\perp$$와 $$u\in U$$를 택하자. adjoint의 정의로부터 $$\langle Lw,u\rangle=\langle w,L^\ast u\rangle$$이고, $$L^\ast u\in U$$이며 $$w\in U^\perp$$이므로 이 값은 $$0$$이다. $$u\in U$$가 임의였으므로 $$Lw\in U^\perp$$이다. $$L$$과 $$L^\ast$$의 역할을 바꾸면 같은 논증으로 $$L^\ast w\in U^\perp$$이므로, $$U^\perp$$은 $$L$$과 $$L^\ast$$에 대해 불변이다.

이제 $$U^\perp$$ 위에서 $$L\vert_{U^\perp}$$의 adjoint를 생각하자. 임의의 $$w,w'\in U^\perp$$에 대하여 $$\langle Lw,w'\rangle=\langle w,L^\ast w'\rangle$$이고 $$L^\ast w'\in U^\perp$$이므로, $$U^\perp$$ 위에서 $$(L\vert_{U^\perp})^\ast=L^\ast\vert_{U^\perp}$$이다. $$L$$과 $$L^\ast$$가 $$V$$ 위에서 가환이므로 그 제한들도 $$U^\perp$$ 위에서 가환이고, 따라서 $$L\vert_{U^\perp}$$은 normal operator이다.

</details>

이제 복소 스펙트럼 정리를 증명할 준비가 되었다.

<div class="proposition" markdown="1">

<ins id="thm6">**정리 6 (복소 스펙트럼 정리)**</ins> 복소내적공간 $$V$$ 위의 linear operator $$L:V\rightarrow V$$가 normal operator인 것은, $$L$$의 고유벡터들로 이루어진 $$V$$의 orthonormal basis가 존재하는 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

먼저 normal operator가 orthonormal basis로 대각화됨을 $$\dim V$$에 대한 귀납법으로 보인다. $$\dim V=0$$인 경우는 보일 것이 없다. $$\dim V\geq 1$$이라 하자. $$L$$의 orthonormal basis에 대한 행렬표현의 특성다항식은 차수가 $$1$$ 이상이므로, [§특성다항식, ⁋정리 8](/ko/math/linear_algebra/characteristic_polynomial#thm8)에 의하여 $$\mathbb{C}$$에서 근 $$\lambda_1$$을 가지고, 따라서 $$L$$은 $$\lVert v_1\rVert=1$$인 고유벡터 $$v_1$$을 가진다.

[따름정리 4](#cor4)에 의하여 $$v_1$$은 $$L^\ast$$의 고유벡터이기도 하므로, $$U=\span v_1$$은 $$L$$과 $$L^\ast$$에 대해 모두 불변이다. [보조정리 5](#lem5)에 의하여 $$U^\perp$$ 또한 양쪽에 불변이고 $$L\vert_{U^\perp}$$은 normal operator이며, [§복소내적공간, §§정규직교기저](/ko/math/linear_algebra/complex_inner_product_spaces#정규직교기저)에서 보았듯 $$V=U\oplus U^\perp$$이고 $$\dim U^\perp=\dim V-1$$이다. 귀납적 가정에 의하여 $$L\vert_{U^\perp}$$의 고유벡터들로 이루어진 $$U^\perp$$의 orthonormal basis $$\{v_2,\ldots,v_n\}$$이 존재한다. 이들은 모두 $$L$$의 고유벡터이고, $$v_1\in U$$이 나머지 $$v_2,\ldots,v_n\in U^\perp$$과 직교하므로, $$\{v_1,\ldots,v_n\}$$은 $$L$$의 고유벡터들로 이루어진 $$V$$의 orthonormal basis이다.

거꾸로 $$L$$의 고유벡터들로 이루어진 orthonormal basis $$\{v_1,\ldots,v_n\}$$이 존재하여 $$Lv_i=\lambda_iv_i$$라 하자. [따름정리 4](#cor4)의 증명에서 본 대로, 정규성을 가정하지 않더라도 직교기저에 대한 행렬표현이 대각이면 그 켤레전치 또한 대각이다. 즉 이 기저에 대하여 $$L$$의 행렬표현은 $$D=\diag(\lambda_1,\ldots,\lambda_n)$$이고 $$L^\ast$$의 행렬표현은 $$\bar D=\diag(\bar\lambda_1,\ldots,\bar\lambda_n)$$이다. 두 대각행렬은 가환이므로 $$LL^\ast=L^\ast L$$이고, 따라서 $$L$$은 normal operator이다.

</details>

행렬의 언어로 옮기면 정리는 normal matrix의 unitary 대각화를 의미한다. 행렬 $$A$$가 $$AA^\ast=A^\ast A$$를 만족할 때 *normal matrix<sub>정규행렬</sub>*이라 부른다.

<div class="proposition" markdown="1">

<ins id="cor7">**따름정리 7**</ins> 행렬 $$A\in\Mat_n(\mathbb{C})$$가 normal matrix인 것은, 적당한 unitary matrix $$U$$와 대각행렬 $$D$$가 존재하여

$$A=UDU^\ast$$

이 성립하는 것과 동치이다. 이 때 $$D$$의 대각성분은 $$A$$의 고윳값들이고, $$U$$의 열들은 이에 대응되는 정규직교인 고유벡터들이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$A$$를 $$\mathbb{C}^n$$ 위의 normal operator로 보면, [정리 6](#thm6)에 의하여 $$A$$의 고유벡터들로 이루어진 orthonormal basis $$\{v_1,\ldots,v_n\}$$이 존재한다. $$Av_i=\lambda_iv_i$$라 하고 $$v_i$$를 열로 갖는 행렬 $$U=(v_1\mid\cdots\mid v_n)$$을 생각하면, 열들이 정규직교이므로 $$U$$는 unitary matrix이다. ([§복소내적공간, ⁋정의 5](/ko/math/linear_algebra/complex_inner_product_spaces#def5)) 그럼

$$AU=(\lambda_1v_1\mid\cdots\mid\lambda_nv_n)=UD$$

이고, 오른쪽에서 $$U^\ast=U^{-1}$$을 곱하면 $$A=UDU^\ast$$를 얻는다. 거꾸로 $$A=UDU^\ast$$이면 대각행렬 $$D$$가 $$D^\ast=\bar D$$와 가환이므로

$$AA^\ast=UDU^\ast UD^\ast U^\ast=UDD^\ast U^\ast=UD^\ast DU^\ast=A^\ast A$$

가 되어 $$A$$는 normal matrix이다.

</details>

## 특수한 경우

self-adjoint operator와 unitary operator는 normal operator이므로 [정리 6](#thm6)에 의하여 모두 orthonormal basis로 대각화된다. 두 경우 고윳값이 특별한 위치에 놓인다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> 복소내적공간 위의 self-adjoint operator의 모든 고윳값은 실수이고, unitary operator의 모든 고윳값은 절댓값이 $$1$$이다.

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

<ins id="rmk9">**참고 9**</ins> 복소 스펙트럼 정리는 실수판 ([§스펙트럼 정리, ⁋정리 6](/ko/math/linear_algebra/spectral_theorem#thm6))을 특수한 경우로 포함한다. 실대칭행렬 $$A$$는 성분이 실수이므로 $$A^\ast=\bar A^t=A^t=A$$가 되어 Hermitian 행렬이고, 따라서 [명제 8](#prop8)에 의하여 그 고윳값은 모두 실수이다. 실수 고윳값 $$\lambda$$에 대하여 $$\lambda I-A$$는 실행렬이므로 그 kernel에서 실벡터인 고유벡터를 택할 수 있고, 이로부터 실내적공간 위에서의 직교대각화가 따라온다. 실수판에서 실대칭행렬의 고윳값이 실수임을 보일 때 ([§스펙트럼 정리, ⁋보조정리 2](/ko/math/linear_algebra/spectral_theorem#lem2)) $$\mathbb{C}^n$$ 위의 Hermitian 내적을 "계산을 위한 도구"로만 끌어다 썼던 것은, 바로 이 [명제 8](#prop8)의 self-adjoint 고윳값의 실수성을 미리 사용한 것이었다.

</div>

---

**참고문헌**

**[Axl]** S. Axler, *Linear algebra done right*, 3rd ed., Undergraduate Texts in Mathematics, Springer, 2015.  
**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.  
**[Lee]** 이인석, *선형대수와 군*, 서울대학교 출판문화원, 2005.

---
