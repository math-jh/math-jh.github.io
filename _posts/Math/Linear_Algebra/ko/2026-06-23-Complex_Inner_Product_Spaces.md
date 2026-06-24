---
title: "복소내적공간"
description: "복소벡터공간 위에 conjugate-symmetric한 Hermitian 내적을 정의하고, 코시-슈바르츠 부등식과 Gram-Schmidt 과정이 그대로 성립함을 본다. 나아가 켤레전치로 주어지는 adjoint와 내적을 보존하는 unitary 행렬을 다룬다."
excerpt: "복소수 위에서 정의된 Hermitian 내적"

categories: [Math / Linear Algebra]
permalink: /ko/math/linear_algebra/complex_inner_product_spaces
sidebar: 
    nav: "linear_algebra-ko"


date: 2026-06-23

weight: 118

published: false

---

## 복소내적과 노름

[§내적공간](/ko/math/linear_algebra/inner_product_spaces)에서 우리는 $$\mathbb{R}$$-벡터공간 위의 내적을 정의하였다. 내적의 핵심 조건은 $$\langle v,v\rangle\geq 0$$이라는 positive-definiteness이며, 이는 $$\mathbb{K}$$에 대소관계가 있어야 하므로 일반적인 field에서는 곧바로 옮겨지지 않는다. 특히 $$\mathbb{C}$$ 위에서 $$\langle v,w\rangle=\sum_i v_iw_i$$를 그대로 쓰면 $$\langle v,v\rangle=\sum_i v_i^2$$이 복소수가 되어 부호를 말할 수 없다. 해결책은 한쪽 변수에 켤레복소수를 취하는 것이다. $$\sum_i\bar v_iv_i=\sum_i\lvert v_i\rvert^2$$은 언제나 음이 아닌 실수이기 때문이다. 이렇게 한 변수에 대해 conjugate-linear가 되도록 수정한 내적을 *Hermitian inner product*이라 부르며, 이 글에서는 이를 갖춘 $$\mathbb{C}$$-벡터공간 위에서 [§내적공간](/ko/math/linear_algebra/inner_product_spaces)의 이론이 어떻게 옮겨지는지를 살펴본다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $$\mathbb{C}$$-벡터공간 $$V$$ 위의 함수 $$\langle-,-\rangle:V\times V\rightarrow\mathbb{C}$$가 *Hermitian inner product<sub>에르미트 내적</sub>*라는 것은 다음을 만족하는 것이다.

1. (Conjugate-symmetry) 임의의 $$v,w\in V$$에 대하여 $$\langle w,v\rangle=\overline{\langle v,w\rangle}$$;
2. (Linearity on second argument) 임의의 $$v,w,w'\in V$$와 $$\alpha\in\mathbb{C}$$에 대하여 $$\langle v,w+w'\rangle=\langle v,w\rangle+\langle v,w'\rangle$$이고 $$\langle v,\alpha w\rangle=\alpha\langle v,w\rangle$$;
3. (Positive-definiteness) 임의의 $$v\in V$$에 대하여 $$\langle v,v\rangle\geq 0$$이고, 등호는 오직 $$v=0$$일 때만 성립한다.

이러한 $$\langle-,-\rangle$$이 주어진 $$V$$를 *복소내적공간<sub>complex inner product space</sub>*이라 부른다.

</div>

조건 1에서 $$v=w$$로 두면 $$\langle v,v\rangle=\overline{\langle v,v\rangle}$$이므로 $$\langle v,v\rangle$$은 항상 실수이고, 따라서 셋째 조건의 부등호가 말이 된다. 둘째 조건의 경우, 정의에 의해 이 내적은 둘째 변수에 대해서는 linear이지만 첫째 변수에 대해서는 conjugate-linear인데, 실제로 조건 1과 2를 결합하면

$$\langle \alpha v,w\rangle=\overline{\langle w,\alpha v\rangle}=\overline{\alpha\langle w,v\rangle}=\bar\alpha\overline{\langle w,v\rangle}=\bar\alpha\langle v,w\rangle$$

이 되어 첫째 변수에서 스칼라가 켤레와 함께 빠져나온다. 이렇게 한 변수에 linear, 다른 변수에 conjugate-linear인 형식을 *sesquilinear form*라 부른다. 둘째 변수를 linear로 두는 것은 약속의 문제로, 물리학에서는 첫째 변수를 linear로 두는 관례가 흔하다.

가장 기본적인 예시는 $$\mathbb{C}^n$$ 위의 *standard Hermitian inner product*

$$\langle v,w\rangle=\sum_{i=1}^n\bar v_iw_i=\bar v^tw$$

이다. 여기서 conjugate-symmetry는 $$\overline{\bar v^tw}=v^t\bar w=\overline{w}^{\,t}v$$로부터, 둘째 변수의 linearity는 행렬곱의 성질로부터 곧바로 따라오며, $$\langle v,v\rangle=\sum_i\lvert v_i\rvert^2$$이 $$v\neq 0$$일 때 양수이므로 positive-definite이다.

한편, 셋째 조건에 의해 $$\langle v,v\rangle$$이 음이 아닌 실수이므로, 실수의 경우와 똑같이 벡터의 크기를 정의할 수 있다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 복소내적공간 $$V$$ 위의 *norm<sub>노름</sub>* $$\lVert-\rVert:V\rightarrow\mathbb{R}$$을 다음의 식

$$\lVert v\rVert=\sqrt{\langle v,v\rangle}$$

으로 정의한다.

</div>

그러나, 실수의 경우와 달리 내적 자체는 복소수 값을 가지므로, 노름의 성질을 확인할 때 켤레가 끼어든다. 우선 임의의 $$v,w\in V$$에 대하여 $$\langle v,w\rangle$$과 $$\langle w,v\rangle=\overline{\langle v,w\rangle}$$의 합은 실수부의 두 배, 즉 $$\langle v,w\rangle+\langle w,v\rangle=2\Real\langle v,w\rangle$$이다. 이를 이용하면

$$\lVert v+w\rVert^2=\langle v+w,v+w\rangle=\lVert v\rVert^2+2\Real\langle v,w\rangle+\lVert w\rVert^2$$

을 얻는다. 코시-슈바르츠 부등식은 이 전개의 핵심 도구이다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3 (Cauchy-Schwarz)**</ins> 복소내적공간 $$V$$의 임의의 벡터 $$v,w$$에 대하여

$$\lvert\langle v,w\rangle\rvert\leq\lVert v\rVert\lVert w\rVert$$

이 성립한다. 등호는 $$v,w$$가 일차종속일 때, 그리고 그 때에만 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$w=0$$이면 양변이 모두 $$0$$이므로 성립한다. $$w\neq 0$$이라 하고

$$\lambda=\frac{\langle w,v\rangle}{\langle w,w\rangle}$$

으로 두자. 그럼 $$\langle w,v-\lambda w\rangle=\langle w,v\rangle-\lambda\langle w,w\rangle=0$$이므로 $$v-\lambda w$$는 $$w$$와 직교한다. 따라서 $$v=\lambda w+(v-\lambda w)$$를 대입하면

$$0\leq\lVert v-\lambda w\rVert^2=\langle v-\lambda w,v-\lambda w\rangle=\lVert v\rVert^2-\bar\lambda\langle w,v\rangle=\lVert v\rVert^2-\frac{\lvert\langle v,w\rangle\rvert^2}{\lVert w\rVert^2}$$

을 얻는다. 마지막 등호는 

$$\bar\lambda\langle w,v\rangle=\frac{\overline{\langle w,v\rangle}\langle w,v\rangle}{\lVert w\rVert^2}=\frac{\lvert\langle w,v\rangle\rvert^2}{\lVert w\rVert^2}$$

이고 $$\lvert\langle w,v\rangle\rvert=\lvert\langle v,w\rangle\rvert$$인 것으로부터 따라온다. 양변을 정리하면 $$\lvert\langle v,w\rangle\rvert^2\leq\lVert v\rVert^2\lVert w\rVert^2$$이고, 등호는 정확히 $$v-\lambda w=0$$, 즉 $$v,w$$가 일차종속일 때 성립한다.

</details>

이로부터 삼각부등식이 따라온다. 위에서 구한 $$\lVert v+w\rVert^2=\lVert v\rVert^2+2\Real\langle v,w\rangle+\lVert w\rVert^2$$에서 $$\Real\langle v,w\rangle\leq\lvert\langle v,w\rangle\rvert\leq\lVert v\rVert\lVert w\rVert$$을 적용하면

$$\lVert v+w\rVert^2\leq\lVert v\rVert^2+2\lVert v\rVert\lVert w\rVert+\lVert w\rVert^2=(\lVert v\rVert+\lVert w\rVert)^2$$

이 되어 $$\lVert v+w\rVert\leq\lVert v\rVert+\lVert w\rVert$$을 얻는다. $$\lVert\alpha v\rVert=\lvert\alpha\rvert\lVert v\rVert$$은 $$\langle\alpha v,\alpha v\rangle=\bar\alpha\alpha\langle v,v\rangle=\lvert\alpha\rvert^2\lVert v\rVert^2$$로부터 자명하므로, $$\lVert-\rVert$$은 실제로 노름이다. ([§내적공간, ⁋정의 2](/ko/math/linear_algebra/inner_product_spaces#def2))

## 정규직교기저

실수의 경우와 마찬가지로, 복소내적공간에서도 두 벡터 $$v,w$$가 $$\langle v,w\rangle=0$$을 만족할 때 서로 직교한다고 하며, 크기가 모두 $$1$$이고 서로 직교하는 기저를 orthonormal basis라 부른다. 이 때도 실수의 경우와 마찬가지로 Gram-Schmidt 과정이 그대로 작동하는데, 실제로 기저 $$\{x_1,\ldots,x_n\}$$이 주어졌을 때 $$\hat x_1=x_1$$로 두고

$$\hat x_k=x_k-\sum_{i=1}^{k-1}\frac{\langle\hat x_i,x_k\rangle}{\langle\hat x_i,\hat x_i\rangle}\hat x_i$$

로 정의하면, $$\langle\hat x_j,\hat x_k\rangle=0$$ ($$j<k$$)이 귀납적으로 확인되어 $$\{\hat x_1,\ldots,\hat x_n\}$$이 orthogonal basis가 된다. 다소 신경써야 할 것은 분자가 $$\langle\hat x_i,x_k\rangle$$이고 $$\langle x_k,\hat x_i\rangle$$이 아니라는 것으로, 사영이 올바른 방향으로 빠지려면 $$\hat x_i$$를 첫째 변수, 즉 conjugate-linear한 쪽에 두어야 한다. 

$$\mathcal{B}=\{x_1,\ldots,x_n\}$$이 orthonormal basis이면, 임의의 $$v=\sum_iv_ix_i$$의 계수는 $$\langle x_i,-\rangle$$을 취하여

$$\langle x_i,v\rangle=\sum_jv_j\langle x_i,x_j\rangle=v_i$$

로 얻어진다. 즉

$$v=\sum_{i=1}^n\langle x_i,v\rangle x_i$$

이다. 둘째 변수가 linear이므로 계수를 뽑을 때 $$\langle x_i,v\rangle$$의 순서가 중요하며, $$\langle v,x_i\rangle$$을 쓰면 그 켤레가 나온다.

부분공간으로의 직교분해 또한 그대로 성립한다. 복소내적공간 $$V$$의 부분공간 $$U\leq V$$에 대하여, 내적을 $$U$$로 제한한 것이 다시 Hermitian 내적이므로 $$U$$는 orthonormal basis $$\{x_1,\ldots,x_k\}$$를 가지며, 이를 포함하는 $$V$$의 orthonormal basis로 확장할 수 있다. $$U^\perp=\{v\in V:\langle u,v\rangle=0\text{ for all }u\in U\}$$로 두면

$$V=U\oplus U^\perp,\qquad\dim U^\perp=\dim V-\dim U$$

가 성립한다.

## 수반작용소와 유니터리행렬

복소내적공간 $$V$$ 위의 linear operator $$L:V\rightarrow V$$에 대하여, 실수의 경우와 마찬가지로 그 *adjoint* $$L^\ast$$를

$$\langle Lv,w\rangle=\langle v,L^\ast w\rangle\qquad\text{for all }v,w\in V$$

를 만족하는 유일한 operator로 정의한다. orthonormal basis에 대한 행렬표현을 통해 $$L^\ast$$의 정체를 알 수 있다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $$\mathcal{B}=\{e_1,\ldots,e_n\}$$이 복소내적공간 $$V$$의 orthonormal basis이고 $$A=[L]_\mathcal{B}^\mathcal{B}$$라 하면, $$L^\ast$$의 행렬표현은 $$A$$의 *conjugate transpose<sub>켤레전치</sub>* $$A^\ast=\bar A^t$$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$Le_i=\sum_kA_{ki}e_k$$이므로 $$\langle e_j,Le_i\rangle=\sum_kA_{ki}\langle e_j,e_k\rangle=A_{ji}$$이다. 그럼 adjoint의 정의와 conjugate-symmetry로부터

$$[L^\ast]_{ij}=\langle e_i,L^\ast e_j\rangle=\langle Le_i,e_j\rangle=\overline{\langle e_j,Le_i\rangle}=\overline{A_{ji}}$$

이 되어, $$L^\ast$$의 행렬표현의 $$(i,j)$$성분은 $$\overline{A_{ji}}$$, 즉 $$A^\ast=\bar A^t$$이다.

</details>

즉, 실수내적공간에서 adjoint가 transpose로 주어졌던 것이 복소내적공간에서는 켤레전치로 바뀌는 것이다. 

한편 내적을 보존하는 operator는 실수의 경우 orthogonal matrix로 표현되었다. 복소의 경우 이에 대응하는 것이 unitary matrix이다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> 행렬 $$U\in\Mat_n(\mathbb{C})$$가 *unitary matrix<sub>유니터리 행렬</sub>*라는 것은

$$U^\ast U=UU^\ast=I$$

가 성립하는 것이다. 복소내적공간 위의 operator $$L$$이 $$L^\ast L=I$$를 만족할 때 *unitary operator<sub>유니터리 작용소</sub>*라 부른다.

</div>

[§동형사상, ⁋정리 7](/ko/math/linear_algebra/isomorphic_vector_spaces#thm7)로부터 $$U^\ast U=I$$이면 자동으로 $$UU^\ast=I$$임을 알 수 있으므로, 한쪽 조건만으로 충분하다. unitary operator는 정확히 내적을 보존하는 operator이다. 실제로 $$L$$이 내적을 보존하면 임의의 $$v,w$$에 대하여 $$\langle v,w\rangle=\langle Lv,Lw\rangle=\langle v,L^\ast Lw\rangle$$이 모든 $$v$$에 대해 성립하므로 $$L^\ast L=I$$이고, 거꾸로 $$L^\ast L=I$$이면

$$\langle Lv,Lw\rangle=\langle v,L^\ast Lw\rangle=\langle v,w\rangle$$

이 되어 내적을 보존한다. 두 orthonormal basis 사이의 기저변환행렬이 항상 unitary matrix가 된다는 것도 실수의 경우와 똑같은 계산으로 확인되며, 다만 conjugate-symmetry 때문에 한쪽 기저변환행렬이 다른 쪽의 켤레전치가 된다. 이 unitary 행렬과 켤레전치 adjoint가 self-adjoint operator를 일반화한 normal operator의 스펙트럼 정리를 전개하는 토대가 된다.

---

**참고문헌**

**[Axl]** S. Axler, *Linear algebra done right*, 3rd ed., Undergraduate Texts in Mathematics, Springer, 2015.  
**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.  
**[Lee]** 이인석, *선형대수와 군*, 서울대학교 출판문화원, 2005.

---
