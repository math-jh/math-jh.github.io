---
title: "복소내적공간"
description: "복소벡터공간 위에 conjugate-symmetric한 Hermitian 내적을 정의하고, 코시-슈바르츠 부등식과 Gram-Schmidt 과정이 그대로 성립함을 본다. 나아가 켤레전치로 주어지는 adjoint와 내적을 보존하는 unitary matrix를 다루고, 이들을 결합해 가역행렬의 QR 분해를 증명한다."
excerpt: "복소수 위에서 정의된 Hermitian 내적"

categories: [Math / Linear Algebra]
permalink: /ko/math/linear_algebra/complex_inner_product_spaces
sidebar: 
    nav: "linear_algebra-ko"


date: 2026-06-23

weight: 22



---

## 복소내적과 노름

[§내적공간](/ko/math/linear_algebra/inner_product_spaces)에서 우리는 $\mathbb{R}$-벡터공간 위의 내적을 정의하였다. 내적의 핵심 조건은 $\langle v,v\rangle\geq 0$이라는 positive-definiteness이며, 이는 $\mathbb{K}$에 대소관계가 있어야 하므로 일반적인 field에서는 곧바로 옮겨지지 않는다. 특히 $\mathbb{C}$ 위에서 $\langle v,w\rangle=\sum_i v_iw_i$를 그대로 쓰면 $\langle v,v\rangle=\sum_i v_i^2$이 복소수가 되어 부호를 말할 수 없다. 해결책은 한쪽 변수에 켤레복소수를 취하는 것이다. $\sum_i\bar v_iv_i=\sum_i\lvert v_i\rvert^2$은 언제나 음이 아닌 실수이기 때문이다. 이렇게 한 변수에 대해 conjugate-linear가 되도록 수정한 내적을 *Hermitian inner product*라 부르며, 이 글에서는 이를 갖춘 $\mathbb{C}$-벡터공간 위에서 [§내적공간](/ko/math/linear_algebra/inner_product_spaces)의 이론이 어떻게 옮겨지는지를 살펴본다.

::: 정의 1
$\mathbb{C}$-벡터공간 $V$ 위의 함수 $\langle-,-\rangle:V\times V\rightarrow\mathbb{C}$가 *Hermitian inner product<sub>에르미트 내적</sub>*라는 것은 다음을 만족하는 것이다.

1. (Conjugate-symmetry) 임의의 $v,w\in V$에 대하여 $\langle w,v\rangle=\overline{\langle v,w\rangle}$;
2. (Linearity on second argument) 임의의 $v,w,w'\in V$와 $\alpha\in\mathbb{C}$에 대하여 $\langle v,w+w'\rangle=\langle v,w\rangle+\langle v,w'\rangle$이고 $\langle v,\alpha w\rangle=\alpha\langle v,w\rangle$;
3. (Positive-definiteness) 임의의 $v\in V$에 대하여 $\langle v,v\rangle\geq 0$이고, 등호는 오직 $v=0$일 때만 성립한다.

이러한 $\langle-,-\rangle$이 주어진 $V$를 *복소내적공간<sub>complex inner product space</sub>*이라 부른다.
:::

조건 1에서 $v=w$로 두면 $\langle v,v\rangle=\overline{\langle v,v\rangle}$이므로 $\langle v,v\rangle$은 항상 실수이고, 따라서 셋째 조건의 부등호가 말이 된다. 둘째 조건의 경우, 정의에 의해 이 내적은 둘째 변수에 대해서는 linear이지만 첫째 변수에 대해서는 conjugate-linear인데, 실제로 조건 1과 2를 결합하면

$$\langle \alpha v,w\rangle=\overline{\langle w,\alpha v\rangle}=\overline{\alpha\langle w,v\rangle}=\bar\alpha\overline{\langle w,v\rangle}=\bar\alpha\langle v,w\rangle$$

이 되어 첫째 변수에서 스칼라가 켤레와 함께 빠져나온다. 이렇게 한 변수에 linear, 다른 변수에 conjugate-linear인 형식을 *sesquilinear form*이라 부른다. 둘째 변수를 linear로 두는 것은 약속의 문제로, 수학 문헌에서는 첫째 변수를 linear로 두는 관례가 흔하다.

가장 기본적인 예시는 $\mathbb{C}^n$ 위의 *standard Hermitian inner product*

$$\langle v,w\rangle=\sum_{i=1}^n\bar v_iw_i=\bar v^tw$$

이다. 여기서 conjugate-symmetry는 $\overline{\bar v^tw}=v^t\bar w=\overline{w}^tv$로부터, 둘째 변수의 linearity는 행렬곱의 성질로부터 곧바로 따라오며, $\langle v,v\rangle=\sum_i\lvert v_i\rvert^2$이 $v\neq 0$일 때 양수이므로 positive-definite이다.

한편, 셋째 조건에 의해 $\langle v,v\rangle$이 음이 아닌 실수이므로, 실수의 경우와 똑같이 벡터의 크기를 정의할 수 있다.

::: 정의 2
복소내적공간 $V$ 위의 *norm<sub>노름</sub>* $\lVert-\rVert:V\rightarrow\mathbb{R}$을 다음의 식

$$\lVert v\rVert=\sqrt{\langle v,v\rangle}$$

으로 정의한다.
:::

그러나, 실수의 경우와 달리 내적 자체는 복소수 값을 가지므로, norm의 성질을 확인할 때 켤레가 끼어든다. 우선 임의의 $v,w\in V$에 대하여 $\langle v,w\rangle$과 $\langle w,v\rangle=\overline{\langle v,w\rangle}$의 합은 실수부의 두 배, 즉 $\langle v,w\rangle+\langle w,v\rangle=2\Real\langle v,w\rangle$이다. 이를 이용하면

$$\lVert v+w\rVert^2=\langle v+w,v+w\rangle=\lVert v\rVert^2+2\Real\langle v,w\rangle+\lVert w\rVert^2$$

을 얻는다. Cauchy-Schwarz 부등식은 이 전개의 핵심 도구이다.

::: 명제 3 (Cauchy-Schwarz)
복소내적공간 $V$의 임의의 벡터 $v,w$에 대하여

$$\lvert\langle v,w\rangle\rvert\leq\lVert v\rVert\lVert w\rVert$$

이 성립한다. 등호는 $v,w$가 일차종속일 때, 그리고 그 때에만 성립한다.
:::
::: 증명
$w=0$이면 양변이 모두 $0$이므로 성립한다. $w\neq 0$이라 하고

$$\lambda=\frac{\langle w,v\rangle}{\langle w,w\rangle}$$

으로 두자. 그럼 $\langle w,v-\lambda w\rangle=\langle w,v\rangle-\lambda\langle w,w\rangle=0$이므로 $v-\lambda w$는 $w$와 직교한다. 따라서 $v=\lambda w+(v-\lambda w)$를 대입하면

$$0\leq\lVert v-\lambda w\rVert^2=\langle v-\lambda w,v-\lambda w\rangle=\lVert v\rVert^2-\bar\lambda\langle w,v\rangle=\lVert v\rVert^2-\frac{\lvert\langle v,w\rangle\rvert^2}{\lVert w\rVert^2}$$

을 얻는다. 마지막 등호는 

$$\bar\lambda\langle w,v\rangle=\frac{\overline{\langle w,v\rangle}\langle w,v\rangle}{\lVert w\rVert^2}=\frac{\lvert\langle w,v\rangle\rvert^2}{\lVert w\rVert^2}$$

이고 $\lvert\langle w,v\rangle\rvert=\lvert\langle v,w\rangle\rvert$인 것으로부터 따라온다. 양변을 정리하면 $\lvert\langle v,w\rangle\rvert^2\leq\lVert v\rVert^2\lVert w\rVert^2$이고, 등호는 정확히 $v-\lambda w=0$, 즉 $v,w$가 일차종속일 때 성립한다.
:::

이로부터 삼각부등식이 따라온다. 위에서 구한 $\lVert v+w\rVert^2=\lVert v\rVert^2+2\Real\langle v,w\rangle+\lVert w\rVert^2$에서 $\Real\langle v,w\rangle\leq\lvert\langle v,w\rangle\rvert\leq\lVert v\rVert\lVert w\rVert$을 적용하면

$$\lVert v+w\rVert^2\leq\lVert v\rVert^2+2\lVert v\rVert\lVert w\rVert+\lVert w\rVert^2=(\lVert v\rVert+\lVert w\rVert)^2$$

이 되어 $\lVert v+w\rVert\leq\lVert v\rVert+\lVert w\rVert$을 얻는다. $\lVert\alpha v\rVert=\lvert\alpha\rvert\lVert v\rVert$은 $\langle\alpha v,\alpha v\rangle=\bar\alpha\alpha\langle v,v\rangle=\lvert\alpha\rvert^2\lVert v\rVert^2$로부터 자명하므로, $\lVert-\rVert$은 실제로 norm이다. ([§내적공간, ⁋정의 2](/ko/math/linear_algebra/inner_product_spaces#def2))

## Orthonormal basis

실수의 경우와 마찬가지로, 복소내적공간에서도 두 벡터 $v,w$가 $\langle v,w\rangle=0$을 만족할 때 서로 직교한다고 하며, 크기가 모두 $1$이고 서로 직교하는 basis를 orthonormal basis라 부른다. 이 때도 실수의 경우와 마찬가지로 Gram-Schmidt 과정이 그대로 작동하는데, 실제로 basis $\{x_1,\ldots,x_n\}$이 주어졌을 때 $\hat x_1=x_1$로 두고

$$\hat x_k=x_k-\sum_{i=1}^{k-1}\frac{\langle\hat x_i,x_k\rangle}{\langle\hat x_i,\hat x_i\rangle}\hat x_i$$

로 정의하면, $\langle\hat x_j,\hat x_k\rangle=0$ ($j<k$)이 귀납적으로 확인되어 $\{\hat x_1,\ldots,\hat x_n\}$이 orthogonal basis가 된다. 다소 신경써야 할 것은 분자가 $\langle\hat x_i,x_k\rangle$이고 $\langle x_k,\hat x_i\rangle$이 아니라는 것으로, 사영이 올바른 방향으로 빠지려면 $\hat x_i$를 첫째 변수, 즉 conjugate-linear한 쪽에 두어야 한다. 

$\mathcal{B}=\{x_1,\ldots,x_n\}$이 orthonormal basis이면, 임의의 $v=\sum_iv_ix_i$의 계수는 $\langle x_i,-\rangle$을 취하여

$$\langle x_i,v\rangle=\sum_jv_j\langle x_i,x_j\rangle=v_i$$

로 얻어진다. 즉

$$v=\sum_{i=1}^n\langle x_i,v\rangle x_i$$

이다. 둘째 변수가 linear이므로 계수를 뽑을 때 $\langle x_i,v\rangle$의 순서가 중요하며, $\langle v,x_i\rangle$을 쓰면 그 켤레가 나온다.

부분공간으로의 직교분해 또한 그대로 성립한다. 복소내적공간 $V$의 부분공간 $U\leq V$에 대하여, 내적을 $U$로 제한한 것이 다시 Hermitian 내적이므로 $U$는 orthonormal basis $\{x_1,\ldots,x_k\}$를 가지며, 이를 포함하는 $V$의 orthonormal basis로 확장할 수 있다. $U^\perp=\{v\in V\mid\langle u,v\rangle=0\text{ for all }u\in U\}$로 두자.

::: 명제 4
복소내적공간 $V$의 임의의 부분공간 $U\leq V$에 대하여

$$V=U\oplus U^\perp,\qquad\dim U^\perp=\dim V-\dim U$$

이 성립한다. 나아가 [§몫공간, ⁋정의 3](/ko/math/linear_algebra/quotient_space#def3)의 natural projection $p:V\rightarrow V/U$을 $U^\perp$로 제한한 $p\vert_{U^\perp}:U^\perp\rightarrow V/U$은 isomorphism이며, 따라서 $U^\perp$은 quotient space $V/U$을 표준적으로 실현한다.
:::
::: 증명
위에서 $V$의 orthonormal basis $\{x_1,\ldots,x_n\}$을 $U$의 것 $\{x_1,\ldots,x_k\}$로부터 확장했으므로, 나머지 $\{x_{k+1},\ldots,x_n\}$은 $U$와 직교하여 $U^\perp$을 span한다. 따라서 $V=U\oplus U^\perp$이고 $\dim U^\perp=\dim V-\dim U$이다. 그럼 $\ker p=U$이므로 $p\vert_{U^\perp}$의 kernel은 $U^\perp\cap U=\{0\}$이라 단사이고, $V=U+U^\perp$이라 전사이므로 isomorphism이다.
:::

여기서 positive-definiteness가 결정적이다. 내적이 positive-definite이면 $U\cap U^\perp$의 임의의 원소 $u$는 $\langle u,u\rangle=0$을 만족해 $u=0$이므로, 모든 부분공간 $U$가 $U\cap U^\perp=\{0\}$을 자동으로 만족한다. 일반적인 symmetric bilinear form에서는 이 직교분해와 표준동형이 부분공간의 non-degeneracy를 요구하지만 ([§쌍선형형식, ⁋명제 9](/ko/math/linear_algebra/bilinear_form#prop9)), Hermitian 내적을 포함한 positive-definite인 경우에는 아무 조건 없이 성립하는 것이다.

## 수반작용소와 unitary matrix

복소내적공간 $V$ 위의 linear operator $L:V\rightarrow V$에 대하여, 실수의 경우와 마찬가지로 그 *adjoint* $L^\ast$를

$$\langle Lv,w\rangle=\langle v,L^\ast w\rangle\qquad\text{for all }v,w\in V$$

를 만족하는 유일한 operator로 정의한다. 이러한 operator의 존재는 orthonormal basis $\{x_1,\ldots,x_n\}$을 잡아 $L^\ast w=\sum_i\langle Lx_i,w\rangle x_i$로 두면 확인되는데, 이는 $\langle Lx_i,w\rangle$이 $w$에 대해 linear이므로 $L^\ast$이 linear이고, $\langle Lv,w\rangle$과 $\langle v,L^\ast w\rangle$이 모두 $v$에 대해 conjugate-linear이면서 $v=x_j$에서 일치하기 때문이며, 유일성은 positive-definiteness로부터 따라온다. Orthonormal basis에 대한 행렬표현을 통해 $L^\ast$의 정체를 알 수 있다.

::: 명제 5
$\mathcal{B}=\{e_1,\ldots,e_n\}$이 복소내적공간 $V$의 orthonormal basis이고 $A=[L]_\mathcal{B}^\mathcal{B}$라 하면, $L^\ast$의 행렬표현은 $A$의 *conjugate transpose<sub>켤레전치</sub>* $A^\ast=\bar A^t$이다.
:::
::: 증명
$Le_i=\sum_kA_{ki}e_k$이므로 $\langle e_j,Le_i\rangle=\sum_kA_{ki}\langle e_j,e_k\rangle=A_{ji}$이다. 그럼 adjoint의 정의와 conjugate-symmetry로부터

$$[L^\ast]_{ij}=\langle e_i,L^\ast e_j\rangle=\langle Le_i,e_j\rangle=\overline{\langle e_j,Le_i\rangle}=\overline{A_{ji}}$$

이 되어, $L^\ast$의 행렬표현의 $(i,j)$성분은 $\overline{A_{ji}}$, 즉 $A^\ast=\bar A^t$이다.
:::

즉, 실수내적공간에서 adjoint가 transpose로 주어졌던 것이 복소내적공간에서는 conjugate transpose로 바뀌는 것이다. 

한편 내적을 보존하는 operator는 실수의 경우 orthogonal matrix로 표현되었다. 복소의 경우 이에 대응하는 것이 unitary matrix이다.

::: 정의 6
행렬 $U\in\Mat_n(\mathbb{C})$가 *unitary matrix<sub>unitary matrix</sub>*라는 것은

$$U^\ast U=UU^\ast=I$$

가 성립하는 것이다. 복소내적공간 위의 operator $L$이 $L^\ast L=I$를 만족할 때 *unitary operator<sub>unitary operator</sub>*라 부른다.
:::

[§동형사상, ⁋정리 7](/ko/math/linear_algebra/isomorphic_vector_spaces#thm7)로부터 $U^\ast U=I$이면 자동으로 $UU^\ast=I$임을 알 수 있으므로, 한쪽 조건만으로 충분하다. Unitary operator는 정확히 내적을 보존하는 operator이다. 실제로 $L$이 내적을 보존하면 임의의 $v,w$에 대하여 $\langle v,w\rangle=\langle Lv,Lw\rangle=\langle v,L^\ast Lw\rangle$이 모든 $v$에 대해 성립하므로 $L^\ast L=I$이고, 거꾸로 $L^\ast L=I$이면

$$\langle Lv,Lw\rangle=\langle v,L^\ast Lw\rangle=\langle v,w\rangle$$

이 되어 내적을 보존한다. 두 orthonormal basis 사이의 change of basis matrix가 항상 unitary matrix가 된다는 것도 실수의 경우와 똑같은 계산으로 확인되며, 다만 conjugate-symmetry 때문에 한쪽 change of basis matrix가 다른 쪽의 conjugate transpose가 된다. 이 unitary matrix와 conjugate transpose adjoint가 self-adjoint operator를 일반화한 normal operator의 spectrum 정리를 전개하는 토대가 된다.

## QR 분해

Gram-Schmidt 과정과 unitary matrix를 결합하면 가역행렬의 표준적인 분해 하나가 따라나온다. 가역행렬 $A\in\Mat_n(\mathbb{C})$의 열 $a_1,\ldots,a_n$은 $\mathbb{C}^n$의 basis를 이루므로 여기에 Gram-Schmidt 과정을 적용할 수 있는데, 이 과정에서 $k$번째 벡터는 처음 $k$개의 열만을 사용해 만들어진다. 따라서 직교화의 결과를 원래의 열들과 비교하는 행렬은 upper triangular일 수밖에 없으며, 이를 정리하면 다음을 얻는다.

::: 명제 7 (QR 분해)
임의의 가역행렬 $A\in\Mat_n(\mathbb{C})$는 unitary matrix $Q$와, 대각성분이 모두 양의 실수인 upper triangular matrix $R$의 곱

$$A=QR$$

로 유일하게 분해된다.
:::
::: 증명
$A$가 가역이므로 그 열 $a_1,\ldots,a_n$은 $\mathbb{C}^n$의 basis이다. 여기에 standard Hermitian inner product에 대한 Gram-Schmidt 과정을 적용하여 orthogonal basis $\hat a_1,\ldots,\hat a_n$을 얻고, $q_k=\hat a_k/\lVert\hat a_k\rVert$로 normalize하자. Gram-Schmidt의 식을 $a_k$에 대해 풀어 적으면

$$a_k=\hat a_k+\sum_{i=1}^{k-1}\frac{\langle\hat a_i,a_k\rangle}{\langle\hat a_i,\hat a_i\rangle}\hat a_i=\lVert\hat a_k\rVert q_k+\sum_{i=1}^{k-1}\langle q_i,a_k\rangle q_i$$

이다. 그러므로 $q_1,\ldots,q_n$을 열로 갖는 행렬을 $Q$라 하고, 행렬 $R$을

$$R_{kk}=\lVert\hat a_k\rVert,\qquad R_{ik}=\langle q_i,a_k\rangle\quad(i<k),\qquad R_{ik}=0\quad(i>k)$$

로 정의하면 위 식은 정확히 $A=QR$이 된다. $Q$의 열들이 orthonormal basis를 이루므로 $(Q^\ast Q)_{ij}=\langle q_i,q_j\rangle$은 $i=j$일 때 $1$, 그 외에는 $0$이 되어 $Q^\ast Q=I$, 곧 $Q$는 unitary matrix이고, $R$은 대각성분이 $\lVert\hat a_k\rVert>0$인 upper triangular matrix이다.

유일성을 보이기 위해 $A=Q_1R_1=Q_2R_2$가 조건을 만족하는 두 분해라 하고 $T=Q_2^\ast Q_1=R_2R_1^{-1}$로 두자. 우선 upper triangular 가역행렬은 정확히 각 $k=1,\ldots,n$마다 부분공간 $\span(e_1,\ldots,e_k)$을 자기 자신 위로 보내는 가역행렬이므로, 이러한 행렬들의 역행렬과 곱은 다시 upper triangular이다. 또 두 triangular matrix의 곱의 대각성분은 대각성분끼리의 곱이므로, $R_1^{-1}$의 대각성분은 $(R_1)_{kk}^{-1}$이고 $T=R_2R_1^{-1}$의 대각성분은 $(R_2)_{kk}/(R_1)_{kk}$, 곧 모두 양의 실수이다. 한편 $T=Q_2^\ast Q_1$은 unitary matrix들의 곱이므로 unitary이고, 따라서 $T^{-1}=T^\ast$인데, 좌변은 upper triangular matrix의 역행렬이라 upper triangular이고 우변은 upper triangular matrix의 conjugate transpose라 lower triangular이다. 그러므로 $T^{-1}$, 따라서 $T$는 diagonal matrix이다. Unitary diagonal matrix의 대각성분은 크기가 $1$이어야 하는데 $T$의 대각성분은 양의 실수이므로 모두 $1$이고, 곧 $T=I$이다. 이는 $Q_1=Q_2$, $R_1=R_2$를 뜻한다.
:::

이 분해를 *QR 분해<sub>QR decomposition</sub>*라 부르며, 증명이 보여주듯 이는 Gram-Schmidt 과정을 행렬의 언어로 옮겨 적은 것이다. $Q$의 열에는 직교화의 결과가, $R$에는 그 과정에 사용된 계수들이 기록된다. 특히 $A$의 열들이 이미 orthonormal이라면, 즉 $A$가 이미 unitary matrix라면 분해는 $Q=A$, $R=I$로 퇴화한다. 같은 증명이 실수의 경우에도 그대로 작동하여, 임의의 가역행렬 $A\in\Mat_n(\mathbb{R})$는 [§내적공간, §§직교행렬](/ko/math/linear_algebra/inner_product_spaces#직교행렬)의 orthogonal matrix와 대각성분이 모두 양의 실수인 upper triangular matrix의 곱으로 유일하게 분해되며, 위 증명의 모든 단계가 $A$의 성분들에 대한 사칙연산과 내적, norm만으로 이루어져 있으므로 두 인자 $Q,R$은 $A$에 연속적으로 의존한다.

한편 Gram-Schmidt 과정 대신 반사를 사용해 같은 분해에 도달할 수도 있다. 벡터 $0\neq v\in\mathbb{C}^n$에 대하여 *Householder reflection<sub>하우스홀더 반사</sub>*

$$H_v=I-2\frac{vv^\ast}{v^\ast v}$$

는 $H_v^\ast=H_v$와 $H_v^2=I$를 만족하므로 unitary matrix이며, $v^\perp$의 벡터를 고정하고 $v$를 $-v$로 보내는, 곧 hyperplane $v^\perp$에 대한 반사이다. 크기가 같고 $\langle y,x\rangle$이 실수인 두 벡터 $x\neq y$에 대하여 $v=x-y$로 두면 $H_vx=y$가 되는 것을 직접 계산으로 확인할 수 있으므로, 가역행렬 $A$의 첫 열 $a_1$에 대해 $\lvert\alpha\rvert=\lVert a_1\rVert$이고 $\langle\alpha e_1,a_1\rangle$이 실수가 되도록 $\alpha$를 잡으면 $a_1$을 $\alpha e_1$로 보내는 Householder reflection $H_1$을 얻는다. 이때 조건을 만족하는 $\alpha$는 부호만 다른 둘이므로 그중 $\alpha e_1\neq a_1$인 쪽을 골라 $v=a_1-\alpha e_1\neq 0$을 보장한다. 그럼 $H_1A$의 첫 열이 $e_1$ 방향으로 정렬되고, 남은 오른쪽 아래 블록에 같은 과정을 반복하면 (아래 블록의 반사는 앞쪽 좌표를 고정하는 $\mathbb{C}^n$의 반사로 확장된다) $H_{n-1}\cdots H_1A$가 upper triangular matrix가 된다. 즉 $Q=H_1\cdots H_{n-1}$로 두면 $A=QR$인데, 이렇게 얻은 $R$의 대각성분은 크기 $1$인 복소수 배만큼 양의 실수에서 어긋날 수 있으므로, diagonal unitary matrix로 보정하면 [명제 7](#prop7)의 꼴을 회수한다. 이 구성은 부동소수점 연산에서 Gram-Schmidt 과정보다 수치적으로 안정적이므로, 수치적인 계산에서 $QR$ 분해를 구하는 표준적인 방법으로 쓰인다.

---

**참고문헌**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.  
**[Lee]** 이인석, *선형대수와 군*, 서울대학교 출판문화원, 2005.

---
