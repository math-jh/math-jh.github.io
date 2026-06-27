---
title: "스펙트럼 정리"
description: "실내적공간 위의 self-adjoint operator를 정의하고, 그 고윳값이 모두 실수임을 보인다. 나아가 self-adjoint operator가 항상 고유벡터들로 이루어진 orthonormal basis를 가짐을 증명하여, 실수 대칭행렬의 직교대각화를 확립한다."
excerpt: "self-adjoint operator의 직교대각화"

categories: [Math / Linear Algebra]
permalink: /ko/math/linear_algebra/spectral_theorem
sidebar: 
    nav: "linear_algebra-ko"


date: 2026-06-25

weight: 120

---

우리는 [§고유공간분해](/ko/math/linear_algebra/eigenspace_decomposition)에서 어떤 행렬이 대각화 가능한지를 살펴보았다. 추가적으로 공간 위에 내적이 주어져 있다면 이 고유벡터들이 서로 직교하도록, 즉 orthonormal basis를 통해 대각화될 수 있는지를 탐구할 수 있다. 

이 글에서는 이 질문에 대한 답이 self-adjoint operator라는 것을 보인다. [§내적공간](/ko/math/linear_algebra/inner_product_spaces)에서 살펴보았듯, 본질적으로 내적은 base field에 의존하는 부분이 크므로 우리는 이 정리 또한 base field가 $$\mathbb{R}$$과 $$\mathbb{C}$$인 경우로 각각 나누어, 후자의 경우는 [§복소 스펙트럼 정리](/ko/math/linear_algebra/complex_spectral_theorem)에서 별도로 다루기로 한다. 

## 자기수반작용소

[§내적공간](/ko/math/linear_algebra/inner_product_spaces)에서 우리는 $$\mathbb{R}$$-내적공간 $$V$$ 위의 linear operator $$L:V\rightarrow V$$의 adjoint $$L^t:V\rightarrow V$$를, 내적이 주는 동형 $$V\cong V^\ast$$를 통해 dual $$L^\ast$$를 번역한 operator로 정의하였다. 이는 임의의 $$v,w\in V$$에 대하여 $$\langle Lv,w\rangle=\langle v,L^t w\rangle$$을 만족하는 유일한 operator이다. 우리는 자기 자신의 adjoint와 일치하는 operator에 특별히 주목한다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $$\mathbb{R}$$-내적공간 $$V$$ 위의 linear operator $$L:V\rightarrow V$$가 *self-adjoint<sub>자기수반</sub>*이라는 것은 $$L=L^t$$인 것, 즉 

$$\langle Lv,w\rangle=\langle v,Lw\rangle$$

이 모든 $$v,w\in V$$에 대해 성립하는 것이다.

</div>

## 고윳값의 실수성

Self-adjoint operator의 대각화에서 핵심이 되는 사실은, (실수) symmetric matrix의 고윳값이 항상 실수라는 것이다. 

<div class="proposition" markdown="1">

<ins id="lem2">**보조정리 2**</ins> 실수 symmetric matrix $$A$$의 모든 고윳값은 실수이다. 즉 $$A$$의 특성다항식의 모든 근은 실수이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$A$$의 특성다항식은 실수를 계수로 갖는 $$n$$차 다항식이며, 대수학의 기본정리 ([§특성다항식, ⁋정리 8](/ko/math/linear_algebra/characteristic_polynomial#thm8))에 의하여, 이 다항식은 $$\mathbb{C}$$까지 포함하면 $$n$$개의 근 $$\lambda$$를 가진다. 

이제 이에 해당하는 eigenvector $$z\in\mathbb{C}^n$$를 생각하고, $$z$$의 각 성분을 켤레복소수로 바꾼 벡터를 $$\bar z$$라 하고, 다음의 복소수

$$s=\bar z^tAz$$

를 생각하자. 우선 $$Az=\lambda z$$이므로 

$$s=\bar z^t(\lambda z)=\lambda(\bar z^tz)=\lambda\sum_{i=1}^n\lvert z_i\rvert^2$$

이다. 다른 한편으로, $$s$$는 $$1\times 1$$ 행렬이므로 자기 자신의 transpose와 같고, $$A$$가 실수 symmetric matrix이므로 $$A=A^t=\bar A$$임을 이용하면 그 켤레복소수는 

$$\bar s=\overline{\bar z^tAz}=z^t\bar A\bar z=z^tA\bar z=(z^tA\bar z)^t=\bar z^tA^tz=\bar z^tAz=s$$

이므로, $$s$$는 실수이다. 그런데 $$\sum_i\lvert z_i\rvert^2$$은 $$z\neq 0$$이므로 양의 실수이고, 따라서 $$s=\lambda\sum_i\lvert z_i\rvert^2$$이 실수이려면 $$\lambda$$ 또한 실수여야 한다.

</details>

이 명제의 증명을 위해 $$\mathbb{C}$$로 다항식을 옮겨야만 하는 것은 필연적이며, 실제로 다음 글에서 우리는 복소수 버전의 스펙트럼 정리를 증명하게 될 것이다. 특히 이로부터 self-adjoint operator가 항상 고윳값을 (따라서 고유벡터를) 가짐을 안다. 

<div class="proposition" markdown="1">

<ins id="cor3">**따름정리 3**</ins> $$0$$이 아닌 $$\mathbb{R}$$-내적공간 $$V$$ 위의 self-adjoint operator $$L:V\rightarrow V$$는 항상 고유벡터를 가진다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$V$$의 orthonormal basis를 택하면 $$L$$의 행렬표현 $$A$$는 실수 symmetric matrix이다. $$\dim V\geq 1$$이므로 $$A$$의 특성다항식은 차수가 $$1$$ 이상이고, 대수학의 기본정리에 의하여 $$\mathbb{C}$$에서 근을 가진다. [보조정리 2](#lem2)에 의하여 이 근은 실수이므로, $$A$$는 실수인 고윳값 $$\lambda$$를 가진다. 그럼 $$\lambda I-A$$가 singular이므로 $$(\lambda I-A)v=0$$을 만족하는 영이 아닌 $$v\in\mathbb{R}^n$$이 존재하고, 이것이 $$L$$의 고유벡터이다. 

</details>

## 스펙트럼 정리

이제 우리는 self-adjoint operator $$L$$이 $$V$$의 부분공간 $$U$$를 보존한다면, 즉 $$L(U)\subseteq U$$가 성립한다면, 그 orthogonal complement도 이 operator에 대해 불변임을 증명한다. 이는, 당연히, 우리가 서두에서 제시했던 *orthogonal* basis를 순차적으로 구성하기 위해서는 필수적인 작업이다. 

<div class="proposition" markdown="1">

<ins id="lem4">**보조정리 4**</ins> $$\mathbb{R}$$-내적공간 $$V$$ 위의 self-adjoint operator $$L:V\rightarrow V$$와, $$L(U)\subseteq U$$를 만족하는 부분공간 $$U\leq V$$에 대하여, $$L(U^\perp)\subseteq U^\perp$$이 성립한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $$w\in U^\perp$$를 택하자. 임의의 $$u\in U$$에 대하여 $$L$$이 self-adjoint이므로 

$$\langle Lw,u\rangle=\langle w,Lu\rangle$$

이고, $$L(U)\subseteq U$$이므로 $$Lu\in U$$이며 $$w\in U^\perp$$이므로 $$\langle w,Lu\rangle=0$$이다. 즉 $$\langle Lw,u\rangle=0$$이 모든 $$u\in U$$에 대해 성립하므로 $$Lw\in U^\perp$$이다. 

</details>

이제 스펙트럼 정리를 증명할 준비가 되었다. 

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5 (스펙트럼 정리)**</ins> $$\mathbb{R}$$-내적공간 $$V$$ 위의 self-adjoint operator $$L:V\rightarrow V$$에 대하여, $$L$$의 고유벡터들로 이루어진 $$V$$의 orthonormal basis가 존재한다. 특히 이 고윳값들은 모두 실수이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\dim V$$에 대한 귀납법으로 증명한다. $$\dim V=0$$인 경우는 보일 것이 없다. $$\dim V\geq 1$$이라 하면, [따름정리 3](#cor3)에 의하여 $$L$$은 고유벡터를 가지며, 이를 크기로 나누어 $$\lVert v_1\rVert=1$$인 고유벡터 $$v_1$$을 얻을 수 있다. 그 고윳값 $$\lambda_1$$은 [보조정리 2](#lem2)에 의해 실수이다. 

$$U=\span v_1$$이라 하면 $$L(U)\subseteq U$$이므로 [보조정리 4](#lem4)에 의하여 $$L(U^\perp)\subseteq U^\perp$$이다. 한편 [§내적공간, ⁋정리 9](/ko/math/linear_algebra/inner_product_spaces#thm9) 이후의 논의에서 보았듯 $$V=U\oplus U^\perp$$이고 $$\dim U^\perp=\dim V-1$$이다. 또 $$U^\perp$$로 제한한 $$L\vert_{U^\perp}:U^\perp\rightarrow U^\perp$$은 임의의 $$w,w'\in U^\perp$$에 대하여 $$\langle Lw,w'\rangle=\langle w,Lw'\rangle$$을 그대로 만족하므로 $$U^\perp$$ 위에서 다시 self-adjoint이다. 따라서 귀납적 가정에 의하여 $$L\vert_{U^\perp}$$의 고유벡터들로 이루어진 $$U^\perp$$의 orthonormal basis $$\{v_2,\ldots, v_n\}$$이 존재한다. 

이 벡터들은 모두 $$L$$의 고유벡터이기도 하며, $$v_1\in U$$이고 $$v_2,\ldots, v_n\in U^\perp$$이므로 $$v_1$$은 나머지와 직교한다. 따라서 $$\{v_1,v_2,\ldots, v_n\}$$은 $$L$$의 고유벡터들로 이루어진 $$V$$의 orthonormal basis이다. 

</details>

행렬의 언어로 옮기면 스펙트럼 정리는 실수 대칭행렬의 직교대각화를 의미한다. 

<div class="proposition" markdown="1">

<ins id="cor6">**따름정리 6**</ins> 임의의 실수 대칭행렬 $$A$$에 대하여, 적당한 orthogonal matrix $$Q$$와 실수 대각행렬 $$D$$가 존재하여 

$$A=QDQ^t$$

이 성립한다. 이 때 $$D$$의 대각성분은 $$A$$의 고윳값들이고, $$Q$$의 열들은 이에 대응되는 orthonormal인 고유벡터들이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$A$$를 $$\mathbb{R}^n$$ 위의 self-adjoint operator로 보면, [정리 5](#thm5)에 의하여 $$A$$의 고유벡터들로 이루어진 orthonormal basis $$\{v_1,\ldots, v_n\}$$이 존재한다. $$Av_i=\lambda_iv_i$$라 하고, $$v_i$$를 열로 갖는 행렬 $$Q=(v_1\mid\cdots\mid v_n)$$을 생각하자. $$Q$$의 열들이 orthonormal이므로 $$Q$$는 orthogonal matrix이다. ([§내적공간, ⁋정의 7](/ko/math/linear_algebra/inner_product_spaces#def7)) 그럼 

$$AQ=(Av_1\mid\cdots\mid Av_n)=(\lambda_1v_1\mid\cdots\mid\lambda_nv_n)=QD$$

이고, 여기서 $$D=\diag(\lambda_1,\ldots,\lambda_n)$$이다. 양변에 오른쪽에서 $$Q^t=Q^{-1}$$을 곱하면 $$A=QDQ^t$$를 얻는다. 

</details>

스펙트럼 정리는 또한 서로 다른 고윳값에 해당하는 고유공간들이 자동으로 직교함을 보여준다. 

<div class="proposition" markdown="1">

<ins id="cor7">**따름정리 7**</ins> $$\mathbb{R}$$-내적공간 $$V$$ 위의 self-adjoint operator $$L$$의 서로 다른 두 고윳값 $$\lambda\neq\mu$$와 이에 해당하는 고유벡터 $$v,w$$에 대하여, $$\langle v,w\rangle=0$$이다. 따라서 $$V$$는 고유공간들의 직교하는 direct sum으로 분해된다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$L$$이 self-adjoint이므로 

$$\lambda\langle v,w\rangle=\langle Lv,w\rangle=\langle v,Lw\rangle=\mu\langle v,w\rangle$$

이고, 따라서 $$(\lambda-\mu)\langle v,w\rangle=0$$이다. $$\lambda\neq\mu$$이므로 $$\langle v,w\rangle=0$$이다. [정리 5](#thm5)의 orthonormal basis를 같은 고윳값을 갖는 것들끼리 묶으면 각 고유공간의 orthonormal basis를 얻으며, 방금 보인 직교성에 의해 서로 다른 고유공간들은 직교한다. 

</details>

## positive definite operator

Self-adjoint operator 가운데 고윳값이 모두 양수인 것들은 따로 이름을 붙일 만하다. 

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> $$\mathbb{R}$$-내적공간 $$V$$ 위의 self-adjoint operator $$L:V\rightarrow V$$이 *positive semidefinite<sub>positive semidefinite</sub>*라는 것은 모든 $$v\in V$$에 대하여 $$\langle Lv,v\rangle\geq 0$$인 것이고, *positive definite<sub>positive definite</sub>*라는 것은 모든 $$0\neq v\in V$$에 대하여 $$\langle Lv,v\rangle> 0$$인 것이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> $$\mathbb{R}$$-내적공간 $$V$$ 위의 self-adjoint operator $$L$$이 positive semidefinite인 것은 $$L$$의 모든 고윳값이 $$0$$ 이상인 것과 동치이고, positive definite인 것은 $$L$$의 모든 고윳값이 양수인 것과 동치이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[정리 5](#thm5)에 의하여 $$L$$의 고유벡터들로 이루어진 orthonormal basis $$\{v_1,\ldots, v_n\}$$을 택하고, $$Lv_i=\lambda_iv_i$$라 하자. 임의의 $$v=\sum_i a_iv_i$$에 대하여 

$$\langle Lv,v\rangle=\left\langle\sum_i a_i\lambda_iv_i,\sum_j a_jv_j\right\rangle=\sum_i\lambda_ia_i^2$$

이다. 마지막 등호는 $$\langle v_i,v_j\rangle=\delta_{ij}$$인 것으로부터 따라온다. 만일 모든 $$\lambda_i\geq 0$$이라면 이 값은 항상 $$0$$ 이상이고, 거꾸로 어떤 $$\lambda_i<0$$이라면 $$v=v_i$$에 대하여 $$\langle Lv_i,v_i\rangle=\lambda_i<0$$이다. 따라서 positive semidefiniteness와 모든 고윳값이 $$0$$ 이상인 것이 동치이다. $$0\neq v$$에 대하여 $$\sum_i\lambda_ia_i^2>0$$인 것과 모든 $$\lambda_i>0$$인 것이 동치임도 같은 방식으로 확인되므로 positive definiteness에 대한 주장도 성립한다. 

</details>

Positive definite operator의 행렬은 또한 삼각행렬을 통해 간결하게 분해된다. 사실 이 분해는 일반적인 정사각행렬의 LU 분해 ([§가우스 소거법, ⁋정의 8](/ko/math/linear_algebra/Gaussian_elimination#def8))가 symmetric positive definite matrix에 대해 더욱 단순해진 형태로, 오직 $$L$$만 계산하면 $$U$$ 부분은 자동으로 나온다는 점에서 계산량을 절반으로 줄인다.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10 (Cholesky 분해)**</ins> Positive definite인 실수 대칭행렬 $$A$$에 대하여, 대각성분이 모두 양수인 하삼각행렬 $$L$$이 유일하게 존재하여 $$A=LL^t$$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$A$$의 크기 $$n$$에 대한 귀납법으로 존재성을 보인다. $$n=1$$이면 $$A=(a)$$에서 positive definiteness로 $$a>0$$이므로 $$L=(\sqrt a)$$로 두면 된다. $$n\geq 2$$라 하고 $$A$$를

$$A=\begin{pmatrix}\alpha&b^t\\ b&A'\end{pmatrix}$$

으로 쪼개자. 여기서 $$\alpha=A_{11}>0$$은 positive definiteness로부터 양수이다. *Schur 여원* $$A''=A'-\alpha^{-1}bb^t$$ 또한 positive definite인데, 임의의 $$0\neq y\in\mathbb{R}^{n-1}$$에 대하여 $$x=-\alpha^{-1}(b^ty)$$로 두면

$$\begin{pmatrix}x&y^t\end{pmatrix}A\begin{pmatrix}x\\ y\end{pmatrix}=\alpha x^2+2x(b^ty)+y^tA'y=y^tA''y$$

이고 좌변이 $$A$$의 positive definiteness로 양수이기 때문이다. 귀납적 가정에 의하여 $$A''=L'L'^t$$인, 대각성분이 양수인 하삼각 $$L'$$이 존재하므로

$$L=\begin{pmatrix}\sqrt\alpha&0\\ \alpha^{-1/2}b&L'\end{pmatrix}$$

으로 두면

$$LL^t=\begin{pmatrix}\alpha&b^t\\ b&\alpha^{-1}bb^t+L'L'^t\end{pmatrix}=\begin{pmatrix}\alpha&b^t\\ b&A'\end{pmatrix}=A$$

이고 $$L$$의 대각성분은 모두 양수이다. 유일성은 첫 열이 $$\sqrt\alpha$$와 $$\alpha^{-1/2}b$$로 결정되고 $$L'$$이 귀납적으로 유일한 것으로부터 따라온다.

</details>


---

**참고문헌**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.  
**[Lee]** 이인석, *선형대수와 군*, 서울대학교 출판문화원, 2005.

---
