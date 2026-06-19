---
title: "스펙트럼 정리"
description: "실내적공간 위의 자기수반작용소를 정의하고, 그 고윳값이 모두 실수임을 보인다. 나아가 자기수반작용소가 항상 고유벡터들로 이루어진 정규직교기저를 가짐을 증명하여, 실대칭행렬의 직교대각화를 확립한다."
excerpt: "자기수반작용소의 직교대각화"

categories: [Math / Linear Algebra]
permalink: /ko/math/linear_algebra/spectral_theorem
sidebar: 
    nav: "linear_algebra-ko"


date: 2026-06-19

weight: 119

published: false

---

우리는 [§고유공간분해](/ko/math/linear_algebra/eigenspace_decomposition)에서 어떤 행렬이 대각화 가능한지를 살펴보았다. 내적공간 위에서는 더 강한 질문을 던질 수 있다. 어떤 linear operator가 단순히 대각화될 뿐만 아니라, 고유벡터들이 서로 직교하도록, 즉 정규직교기저를 통해 대각화될 수 있는가? 이 글에서는 이 질문에 대한 답이 자기수반작용소라는 것을 보인다. 우리는 [§내적공간](/ko/math/linear_algebra/inner_product_spaces)을 따라 $$\mathbb{R}$$-내적공간 위에서 이론을 전개한다. 

## 자기수반작용소

[§내적공간, §§직교행렬](/ko/math/linear_algebra/inner_product_spaces#직교행렬)에서 우리는 $$\mathbb{R}$$-내적공간 $$V$$ 위의 linear operator $$L:V\rightarrow V$$에 대하여 그 adjoint $$L^t$$가 

$$\langle Lv,w\rangle=\langle v,L^tw\rangle\qquad\text{for all $v,w\in V$}$$

을 만족하도록 정의됨을 보았다. 자기 자신과 adjoint가 일치하는 operator가 우리의 관심 대상이다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $$\mathbb{R}$$-내적공간 $$V$$ 위의 linear operator $$L:V\rightarrow V$$가 *자기수반<sub>self-adjoint</sub>*이라는 것은 $$L=L^t$$인 것, 즉 

$$\langle Lv,w\rangle=\langle v,Lw\rangle$$

이 모든 $$v,w\in V$$에 대해 성립하는 것이다.

</div>

자기수반작용소는 정규직교기저에 대한 행렬표현을 통해 알아보는 것이 가장 편하다. $$\mathcal{B}=\{e_1,\ldots, e_n\}$$이 $$V$$의 정규직교기저라 하고 $$A=[L]_\mathcal{B}^\mathcal{B}$$라 하자. 그럼 $$Le_i=\sum_k A_{ki}e_k$$이므로 $$\langle Le_i,e_j\rangle=A_{ji}$$이다. 따라서 

$$A_{ji}=\langle Le_i,e_j\rangle=\langle e_i,L^te_j\rangle=\langle L^te_j,e_i\rangle=[L^t]_{ij}$$

이 성립하여, 정규직교기저에 대한 adjoint의 행렬표현은 원래 행렬표현의 transpose이다. 즉 $$L$$이 자기수반인 것은 그 행렬표현 $$A$$가 대칭행렬, 즉 $$A=A^t$$인 것과 동치이다. 

## 고윳값의 실수성

자기수반작용소의 대각화에서 핵심이 되는 사실은, 실대칭행렬의 고윳값이 항상 실수라는 것이다. 

<div class="proposition" markdown="1">

<ins id="lem2">**보조정리 2**</ins> 실대칭행렬 $$A$$의 모든 고윳값은 실수이다. 즉 $$A$$의 특성다항식의 모든 근은 실수이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$A$$를 $$\mathbb{C}$$ 위의 행렬로 보면, 대수학의 기본정리 ([§특성다항식, ⁋정리 8](/ko/math/linear_algebra/characteristic_polynomial#thm8))에 의하여 $$A$$의 특성다항식은 $$\mathbb{C}$$에서 근 $$\lambda$$를 가지며, 이에 해당하는 영이 아닌 $$z\in\mathbb{C}^n$$가 존재하여 $$Az=\lambda z$$이다. $$z$$의 각 성분을 켤레복소수로 바꾼 벡터를 $$\bar z$$라 적고, 다음의 복소수

$$s=\bar z^tAz$$

를 생각하자. 한 편으로는 $$Az=\lambda z$$이므로 

$$s=\bar z^t(\lambda z)=\lambda(\bar z^tz)=\lambda\sum_{i=1}^n\lvert z_i\rvert^2$$

이다. 다른 한 편으로, $$s$$는 $$1\times 1$$ 행렬이므로 자기 자신의 transpose와 같고, $$A$$가 실대칭행렬이므로 $$A=A^t=\bar A$$임을 이용하면 그 켤레복소수는 

$$\bar s=\overline{\bar z^tAz}=z^t\bar A\bar z=z^tA\bar z=(z^tA\bar z)^t=\bar z^tA^tz=\bar z^tAz=s$$

이다. 즉 $$s$$는 실수이다. 그런데 $$\sum_i\lvert z_i\rvert^2$$은 $$z\neq 0$$이므로 양의 실수이고, $$s=\lambda\sum_i\lvert z_i\rvert^2$$이 실수이므로 $$\lambda$$ 또한 실수여야 한다.

</details>

<div class="remark" markdown="1">

<ins id="rmk3">**참고 3**</ins> 위 증명에서 사용한 $$\bar z^tz=\sum_i\lvert z_i\rvert^2$$은 $$\mathbb{C}^n$$ 위의 표준적인 *Hermitian 내적*이다. 우리는 실내적공간만을 다루고 있으므로 복소내적을 본격적으로 도입하지는 않았으며, 위 증명에서는 이를 단지 계산을 위한 도구로만 사용하였다. 복소내적공간 위에서의 일반적인 이론은 [참고 11](#rmk11)에서 간략히 언급한다. 

</div>

이로부터 자기수반작용소가 항상 고유벡터를 가짐을 안다. 

<div class="proposition" markdown="1">

<ins id="cor4">**따름정리 4**</ins> $$0$$이 아닌 $$\mathbb{R}$$-내적공간 $$V$$ 위의 자기수반작용소 $$L:V\rightarrow V$$는 항상 고유벡터를 가진다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$V$$의 정규직교기저를 택하면 $$L$$의 행렬표현 $$A$$는 실대칭행렬이다. $$\dim V\geq 1$$이므로 $$A$$의 특성다항식은 차수가 $$1$$ 이상이고, 대수학의 기본정리에 의하여 $$\mathbb{C}$$에서 근을 가진다. [보조정리 2](#lem2)에 의하여 이 근은 실수이므로, $$A$$는 실수인 고윳값 $$\lambda$$를 가진다. 그럼 $$\lambda I-A$$가 singular이므로 $$(\lambda I-A)v=0$$을 만족하는 영이 아닌 $$v\in\mathbb{R}^n$$이 존재하고, 이것이 $$L$$의 고유벡터이다. 

</details>

## 스펙트럼 정리

남은 핵심은 자기수반작용소가 불변부분공간의 직교여공간을 다시 불변으로 남긴다는 사실이다. 

<div class="proposition" markdown="1">

<ins id="lem5">**보조정리 5**</ins> $$\mathbb{R}$$-내적공간 $$V$$ 위의 자기수반작용소 $$L:V\rightarrow V$$와, $$L(U)\subseteq U$$를 만족하는 부분공간 $$U\leq V$$에 대하여, $$L(U^\perp)\subseteq U^\perp$$이 성립한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $$w\in U^\perp$$를 택하자. 임의의 $$u\in U$$에 대하여 $$L$$이 자기수반이므로 

$$\langle Lw,u\rangle=\langle w,Lu\rangle$$

이고, $$L(U)\subseteq U$$이므로 $$Lu\in U$$이며 $$w\in U^\perp$$이므로 $$\langle w,Lu\rangle=0$$이다. 즉 $$\langle Lw,u\rangle=0$$이 모든 $$u\in U$$에 대해 성립하므로 $$Lw\in U^\perp$$이다. 

</details>

이제 스펙트럼 정리를 증명할 준비가 되었다. 

<div class="proposition" markdown="1">

<ins id="thm6">**정리 6 (스펙트럼 정리)**</ins> $$\mathbb{R}$$-내적공간 $$V$$ 위의 자기수반작용소 $$L:V\rightarrow V$$에 대하여, $$L$$의 고유벡터들로 이루어진 $$V$$의 정규직교기저가 존재한다. 특히 이 고윳값들은 모두 실수이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\dim V$$에 대한 귀납법으로 증명한다. $$\dim V=0$$인 경우는 보일 것이 없다. $$\dim V\geq 1$$이라 하면, [따름정리 4](#cor4)에 의하여 $$L$$은 고유벡터를 가지며, 이를 크기로 나누어 $$\lVert v_1\rVert=1$$인 고유벡터 $$v_1$$을 얻을 수 있다. 그 고윳값 $$\lambda_1$$은 [보조정리 2](#lem2)에 의해 실수이다. 

$$U=\span v_1$$이라 하면 $$L(U)\subseteq U$$이므로 [보조정리 5](#lem5)에 의하여 $$L(U^\perp)\subseteq U^\perp$$이다. 한편 [§내적공간, ⁋정리 9](/ko/math/linear_algebra/inner_product_spaces#thm9) 이후의 논의에서 보았듯 $$V=U\oplus U^\perp$$이고 $$\dim U^\perp=\dim V-1$$이다. 또 $$U^\perp$$로 제한한 $$L\vert_{U^\perp}:U^\perp\rightarrow U^\perp$$은 임의의 $$w,w'\in U^\perp$$에 대하여 $$\langle Lw,w'\rangle=\langle w,Lw'\rangle$$을 그대로 만족하므로 $$U^\perp$$ 위에서 다시 자기수반이다. 따라서 귀납적 가정에 의하여 $$L\vert_{U^\perp}$$의 고유벡터들로 이루어진 $$U^\perp$$의 정규직교기저 $$\{v_2,\ldots, v_n\}$$이 존재한다. 

이 벡터들은 모두 $$L$$의 고유벡터이기도 하며, $$v_1\in U$$이고 $$v_2,\ldots, v_n\in U^\perp$$이므로 $$v_1$$은 나머지와 직교한다. 따라서 $$\{v_1,v_2,\ldots, v_n\}$$은 $$L$$의 고유벡터들로 이루어진 $$V$$의 정규직교기저이다. 

</details>

행렬의 언어로 옮기면 스펙트럼 정리는 실대칭행렬의 직교대각화를 의미한다. 

<div class="proposition" markdown="1">

<ins id="cor7">**따름정리 7**</ins> 임의의 실대칭행렬 $$A$$에 대하여, 적당한 orthogonal matrix $$Q$$와 실대각행렬 $$D$$가 존재하여 

$$A=QDQ^t$$

이 성립한다. 이 때 $$D$$의 대각성분은 $$A$$의 고윳값들이고, $$Q$$의 열들은 이에 대응되는 정규직교인 고유벡터들이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$A$$를 $$\mathbb{R}^n$$ 위의 자기수반작용소로 보면, [정리 6](#thm6)에 의하여 $$A$$의 고유벡터들로 이루어진 정규직교기저 $$\{v_1,\ldots, v_n\}$$이 존재한다. $$Av_i=\lambda_iv_i$$라 하고, $$v_i$$를 열로 갖는 행렬 $$Q=(v_1\mid\cdots\mid v_n)$$을 생각하자. $$Q$$의 열들이 정규직교이므로 $$Q$$는 orthogonal matrix이다. ([§내적공간, ⁋정의 7](/ko/math/linear_algebra/inner_product_spaces#def7)) 그럼 

$$AQ=(Av_1\mid\cdots\mid Av_n)=(\lambda_1v_1\mid\cdots\mid\lambda_nv_n)=QD$$

이고, 여기서 $$D=\diag(\lambda_1,\ldots,\lambda_n)$$이다. 양변에 오른쪽에서 $$Q^t=Q^{-1}$$을 곱하면 $$A=QDQ^t$$를 얻는다. 

</details>

스펙트럼 정리는 또한 서로 다른 고윳값에 해당하는 고유공간들이 자동으로 직교함을 보여준다. 

<div class="proposition" markdown="1">

<ins id="cor8">**따름정리 8**</ins> $$\mathbb{R}$$-내적공간 $$V$$ 위의 자기수반작용소 $$L$$의 서로 다른 두 고윳값 $$\lambda\neq\mu$$와 이에 해당하는 고유벡터 $$v,w$$에 대하여, $$\langle v,w\rangle=0$$이다. 따라서 $$V$$는 고유공간들의 직교하는 direct sum으로 분해된다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$L$$이 자기수반이므로 

$$\lambda\langle v,w\rangle=\langle Lv,w\rangle=\langle v,Lw\rangle=\mu\langle v,w\rangle$$

이고, 따라서 $$(\lambda-\mu)\langle v,w\rangle=0$$이다. $$\lambda\neq\mu$$이므로 $$\langle v,w\rangle=0$$이다. [정리 6](#thm6)의 정규직교기저를 같은 고윳값을 갖는 것들끼리 묶으면 각 고유공간의 정규직교기저를 얻으며, 방금 보인 직교성에 의해 서로 다른 고유공간들은 직교한다. 

</details>

## 양의 정부호 작용소

자기수반작용소 가운데 고윳값이 모두 양수인 것들은 따로 이름을 붙일 만하다. 이들은 다음 글에서 특이값 분해를 다룰 때 핵심적으로 쓰인다. 

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> $$\mathbb{R}$$-내적공간 $$V$$ 위의 자기수반작용소 $$L:V\rightarrow V$$이 *양의 준정부호<sub>positive semidefinite</sub>*라는 것은 모든 $$v\in V$$에 대하여 $$\langle Lv,v\rangle\geq 0$$인 것이고, *양의 정부호<sub>positive definite</sub>*라는 것은 모든 $$0\neq v\in V$$에 대하여 $$\langle Lv,v\rangle> 0$$인 것이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> $$\mathbb{R}$$-내적공간 $$V$$ 위의 자기수반작용소 $$L$$이 양의 준정부호인 것은 $$L$$의 모든 고윳값이 $$0$$ 이상인 것과 동치이고, 양의 정부호인 것은 $$L$$의 모든 고윳값이 양수인 것과 동치이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[정리 6](#thm6)에 의하여 $$L$$의 고유벡터들로 이루어진 정규직교기저 $$\{v_1,\ldots, v_n\}$$을 택하고, $$Lv_i=\lambda_iv_i$$라 하자. 임의의 $$v=\sum_i a_iv_i$$에 대하여 

$$\langle Lv,v\rangle=\left\langle\sum_i a_i\lambda_iv_i,\sum_j a_jv_j\right\rangle=\sum_i\lambda_ia_i^2$$

이다. 마지막 등호는 $$\langle v_i,v_j\rangle=\delta_{ij}$$인 것으로부터 따라온다. 만일 모든 $$\lambda_i\geq 0$$이라면 이 값은 항상 $$0$$ 이상이고, 거꾸로 어떤 $$\lambda_i<0$$이라면 $$v=v_i$$에 대하여 $$\langle Lv_i,v_i\rangle=\lambda_i<0$$이다. 따라서 양의 준정부호성과 모든 고윳값이 $$0$$ 이상인 것이 동치이다. $$0\neq v$$에 대하여 $$\sum_i\lambda_ia_i^2>0$$인 것과 모든 $$\lambda_i>0$$인 것이 동치임도 같은 방식으로 확인되므로 양의 정부호성에 대한 주장도 성립한다. 

</details>

<div class="remark" markdown="1">

<ins id="rmk11">**참고 11**</ins> 복소내적공간, 즉 $$\mathbb{C}^n$$ 위의 Hermitian 내적 $$\langle z,w\rangle=\sum_i\bar z_iw_i$$를 갖춘 공간 위에서는 더 넓은 종류의 작용소가 직교대각화된다. 이 경우 adjoint $$L^\ast$$는 켤레transpose로 주어지며, $$LL^\ast=L^\ast L$$을 만족하는 *정규작용소<sub>normal operator</sub>*가 정확히 정규직교기저로 대각화되는 작용소이다. 자기수반작용소($$L=L^\ast$$, Hermitian)와 유니터리작용소($$LL^\ast=I$$)는 모두 정규작용소의 특수한 경우이다. 이 복소판 스펙트럼 정리를 전개하기 위해서는 복소내적공간의 이론이 필요하며, 여기서는 다루지 않는다. 

</div>

---

**참고문헌**

**[Axl]** S. Axler, *Linear algebra done right*, 3rd ed., Undergraduate Texts in Mathematics, Springer, 2015.  
**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.  
**[Lee]** 이인석, *선형대수와 군*, 서울대학교 출판문화원, 2005.

---
