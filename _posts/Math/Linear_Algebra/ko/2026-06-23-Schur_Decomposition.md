---
title: "Schur 분해"
description: "복소내적공간 위의 임의의 linear operator가 적절한 정규직교기저에 대해 상삼각행렬로 표현됨을 보인다. 이로부터 정규작용소가 대각화된다는 복소 스펙트럼 정리를 다시 얻는다."
excerpt: "임의의 복소행렬의 유니터리 상삼각화"

categories: [Math / Linear Algebra]
permalink: /ko/math/linear_algebra/schur_decomposition
sidebar: 
    nav: "linear_algebra-ko"


date: 2026-06-23

weight: 122

drift_needed: true

published: false

---

[§복소 스펙트럼 정리](/ko/math/linear_algebra/complex_spectral_theorem)에서 우리는 정규작용소가 정확히 정규직교기저로 대각화됨을 보았다. 정규작용소가 아닌 일반적인 operator는 대각화되지 않을 수 있지만, $$\mathbb{C}$$ 위에서는 그보다 약한 형태, 즉 정규직교기저에 대한 *상삼각화*는 항상 가능하다. 이것이 Schur 분해이며, 정규작용소의 경우 이 상삼각행렬이 자동으로 대각이 되어 복소 스펙트럼 정리를 되돌려준다.

## Schur 분해

핵심은 대수학의 기본정리가 항상 고유벡터를 공급한다는 것과, 한 고유벡터의 직교여공간이 불변으로 남는다는 것이다. 다만 $$L$$의 고유벡터가 아니라 $$L^\ast$$의 고유벡터를 택해야 직교여공간이 $$L$$에 대해 불변이 된다.

<div class="proposition" markdown="1">

<ins id="thm1">**정리 1 (Schur 분해)**</ins> 복소내적공간 $$V$$ 위의 임의의 linear operator $$L:V\rightarrow V$$에 대하여, $$L$$의 행렬표현이 상삼각행렬이 되도록 하는 $$V$$의 정규직교기저가 존재한다. 행렬의 언어로는, 임의의 $$A\in\Mat_n(\mathbb{C})$$에 대하여 적당한 unitary matrix $$U$$와 상삼각행렬 $$T$$가 존재하여 $$A=UTU^\ast$$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\dim V$$에 대한 귀납법으로 정규직교기저 $$\{e_1,\ldots,e_n\}$$이 존재하여 각 $$j$$에 대해 $$Le_j\in\span(e_1,\ldots,e_j)$$임을 보인다. $$\dim V\leq 1$$인 경우는 자명하다. $$\dim V=n\geq 2$$라 하자.

$$L^\ast$$의 행렬표현의 특성다항식은 차수가 $$1$$ 이상이므로 [§특성다항식, ⁋정리 8](/ko/math/linear_algebra/characteristic_polynomial#thm8)에 의하여 근을 가지고, 따라서 $$L^\ast$$은 $$\lVert e_n\rVert=1$$인 고유벡터 $$e_n$$을 가진다. $$L^\ast e_n=\mu e_n$$이라 하자. 이제 $$W=(\span e_n)^\perp$$이 $$L$$에 대해 불변임을 본다. 임의의 $$w\in W$$에 대하여 adjoint의 정의로부터

$$\langle Lw,e_n\rangle=\langle w,L^\ast e_n\rangle=\langle w,\mu e_n\rangle=\mu\langle w,e_n\rangle=0$$

이므로 $$Lw\in W$$이다. $$\dim W=n-1$$이므로 귀납적 가정을 $$L\vert_W$$에 적용하면, $$W$$의 정규직교기저 $$\{e_1,\ldots,e_{n-1}\}$$이 존재하여 각 $$j\leq n-1$$에 대해 $$Le_j\in\span(e_1,\ldots,e_j)$$이다.

그럼 $$\{e_1,\ldots,e_n\}$$은 $$V$$의 정규직교기저이고, $$j<n$$에 대해서는 $$Le_j\in\span(e_1,\ldots,e_j)$$이며 $$j=n$$에 대해서는 $$Le_n\in V=\span(e_1,\ldots,e_n)$$이 자명하게 성립한다. 즉 이 기저에 대한 $$L$$의 행렬표현은 상삼각행렬이다. 이 기저의 벡터들을 열로 갖는 행렬을 $$U$$라 하면 $$U$$는 unitary이고 ([§복소내적공간, ⁋정의 5](/ko/math/linear_algebra/complex_inner_product_spaces#def5)) $$U^\ast AU=T$$가 상삼각이므로 $$A=UTU^\ast$$이다.

</details>

상삼각행렬 $$T$$는 $$A$$와 닮음이므로 같은 특성다항식을 가지며, 상삼각행렬의 특성다항식은 $$\prod_i(\x-T_{ii})$$이므로 $$T$$의 대각성분 $$T_{11},\ldots,T_{nn}$$은 정확히 $$A$$의 고윳값들을 중복도까지 담는다. Schur 분해는 임의의 복소행렬이 유니터리 변환만으로 고윳값들을 대각선에 드러내도록 정리될 수 있음을 말한다.

## 정규작용소와의 관계

상삼각행렬이 추가로 정규행렬이면 곧바로 대각행렬이 된다. 이로부터 [§복소 스펙트럼 정리, ⁋정리 6](/ko/math/linear_algebra/complex_spectral_theorem#thm6)을 Schur 분해의 따름정리로 다시 얻는다.

<div class="proposition" markdown="1">

<ins id="cor2">**따름정리 2**</ins> 정규행렬 $$A\in\Mat_n(\mathbb{C})$$는 unitary matrix로 대각화된다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[정리 1](#thm1)에 의하여 $$A=UTU^\ast$$이고 $$T$$는 상삼각이다. $$A$$가 정규행렬이고 $$U$$가 unitary이므로 $$T=U^\ast AU$$ 또한 정규행렬이다. 상삼각이면서 정규인 $$T$$가 대각임을 $$T$$의 행에 대한 귀납법으로 보인다.

$$T$$가 상삼각이므로 $$T$$의 첫째 열은 $$(T_{11},0,\ldots,0)^t$$이고, 따라서 $$\lVert Te_1\rVert^2=\lvert T_{11}\rvert^2$$이다. 한편 $$T^\ast$$의 첫째 열은 $$T$$의 첫째 행의 켤레이므로 $$\lVert T^\ast e_1\rVert^2=\sum_{j}\lvert T_{1j}\rvert^2$$이다. $$T$$가 정규이면 [§복소 스펙트럼 정리, ⁋보조정리 3](/ko/math/linear_algebra/complex_spectral_theorem#lem3)에 의하여 $$\lVert Te_1\rVert=\lVert T^\ast e_1\rVert$$이므로

$$\lvert T_{11}\rvert^2=\sum_{j}\lvert T_{1j}\rvert^2$$

이고, 따라서 $$j>1$$에 대해 $$T_{1j}=0$$이다. 즉 첫째 행은 대각성분을 제외하면 모두 $$0$$이다. 그럼 $$T$$의 둘째 행 이하는 첫째 행·열을 떼어 낸 $$(n-1)\times(n-1)$$ 상삼각 정규행렬을 이루므로, 귀납적으로 그것도 대각이 되어 $$T$$ 전체가 대각이다. 따라서 $$A=UTU^\ast$$은 유니터리 대각화이다.

</details>

Schur 분해는 [§조르당 표준형](/ko/math/linear_algebra/Jordan_canonical_form)과 좋은 대조를 이룬다. 조르당 표준형은 일반적으로 유니터리가 아닌 기저변환을 써서 행렬을 표준적인 block 형태로 만드는 반면, Schur 분해는 기저변환을 유니터리로 제한하는 대신 표준형을 포기하고 상삼각 형태에 만족한다. 후자는 정규직교성이 보존되어 수치적으로 안정적이라는 장점이 있어 응용에서 자주 쓰인다.

---

**참고문헌**

**[Axl]** S. Axler, *Linear algebra done right*, 3rd ed., Undergraduate Texts in Mathematics, Springer, 2015.  
**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.  
**[Lee]** 이인석, *선형대수와 군*, 서울대학교 출판문화원, 2005.

---
