---
title: "특이값 분해"
description: "임의의 실행렬에 대해 그 전치와의 곱의 스펙트럼 분해로부터 특이값을 정의하고, orthogonal matrix와 diagonal matrix의 곱으로의 특이값 분해를 구성한다. 나아가 이를 통해 일반적인 유사역행렬을 정의한다."
excerpt: "임의의 실행렬의 직교 분해"

categories: [Math / Linear Algebra]
permalink: /ko/math/linear_algebra/singular_value_decomposition
sidebar: 
    nav: "linear_algebra-ko"


date: 2026-06-19

weight: 123

published: false

---

우리가 지금까지 다룬 도구들은 모두 $$n\times n$$ 행렬, 즉 linear operator에 적용되는 것들로, 일반적인 $$m\times n$$ 행렬은 정사각행렬이 아니므로 eigenvalue나 대각화를 직접 말할 수 없다. 이 글에서는 임의의 실행렬을 두 orthogonal matrix와 하나의 diagonal matrix의 곱으로 분해하는 특이값 분해를 다룬다. 그 출발점은, 임의의 $$A$$에 대하여 $$A^tA$$이 항상 실수 symmetric matrix가 되어 스펙트럼 정리를 적용할 수 있다는 관찰이다. 

## 특이값 분해

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1**</ins> 임의의 행렬 $$A\in\Mat_{m\times n}(\mathbb{R})$$에 대하여, $$A^tA\in\Mat_n(\mathbb{R})$$은 positive semidefinite인 self-adjoint operator이다. 특히 $$A^tA$$의 모든 고윳값은 $$0$$ 이상의 실수이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$(A^tA)^t=A^t(A^t)^t=A^tA$$이므로 $$A^tA$$은 symmetric matrix, 즉 $$\mathbb{R}^n$$ 위의 self-adjoint operator이다. 또 임의의 $$v\in\mathbb{R}^n$$에 대하여 

$$\langle A^tAv,v\rangle=\langle Av,Av\rangle=\lVert Av\rVert^2\geq 0$$

이므로 $$A^tA$$은 positive semidefinite이다. ([§스펙트럼 정리, ⁋정의 8](/ko/math/linear_algebra/spectral_theorem#def8)) 따라서 [§스펙트럼 정리, ⁋명제 9](/ko/math/linear_algebra/spectral_theorem#prop9)에 의하여 $$A^tA$$의 모든 고윳값은 $$0$$ 이상이다.

</details>

고윳값이 음이 아니므로 그 제곱근을 취할 수 있다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 행렬 $$A\in\Mat_{m\times n}(\mathbb{R})$$에 대하여, $$A^tA$$의 고윳값들을 중복도를 고려하여 $$\sigma_1^2\geq\sigma_2^2\geq\cdots\geq\sigma_n^2\geq 0$$이라 적을 때, 음이 아닌 실수 $$\sigma_i=\sqrt{\sigma_i^2}$$들을 $$A$$의 *특이값<sub>singular value</sub>*이라 부른다. 

</div>

이제 본 정리를 증명한다. 

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3 (특이값 분해)**</ins> 임의의 행렬 $$A\in\Mat_{m\times n}(\mathbb{R})$$에 대하여, orthogonal matrix $$U\in\Mat_m(\mathbb{R})$$, $$V\in\Mat_n(\mathbb{R})$$과, $$(i,i)$$ 성분이 $$A$$의 특이값 $$\sigma_i$$이고 나머지 성분이 $$0$$인 $$m\times n$$ diagonal matrix $$\Sigma$$가 존재하여 

$$A=U\Sigma V^t$$

이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[명제 1](#prop1)에 의하여 $$A^tA$$은 self-adjoint이므로, [§스펙트럼 정리, ⁋정리 5](/ko/math/linear_algebra/spectral_theorem#thm5)에 의하여 $$A^tA$$의 고유벡터들로 이루어진 $$\mathbb{R}^n$$의 orthonormal basis $$\{v_1,\ldots, v_n\}$$이 존재한다. 고윳값을 $$\sigma_1^2\geq\cdots\geq\sigma_n^2\geq 0$$의 순서로 두고, $$\sigma_1,\ldots,\sigma_r$$이 양수이고 $$\sigma_{r+1}=\cdots=\sigma_n=0$$이라 하자. 즉 $$A^tAv_i=\sigma_i^2v_i$$이다.

각 $$1\leq i\leq r$$에 대하여 

$$u_i=\frac{1}{\sigma_i}Av_i\in\mathbb{R}^m$$

으로 정의하자. 그럼 $$1\leq i,j\leq r$$에 대하여 

$$\langle u_i,u_j\rangle=\frac{1}{\sigma_i\sigma_j}\langle Av_i,Av_j\rangle=\frac{1}{\sigma_i\sigma_j}\langle A^tAv_i,v_j\rangle=\frac{\sigma_i^2}{\sigma_i\sigma_j}\langle v_i,v_j\rangle=\frac{\sigma_i}{\sigma_j}\delta_{ij}=\delta_{ij}$$

이므로 $$\{u_1,\ldots, u_r\}$$은 $$\mathbb{R}^m$$의 orthonormal set이다. 이를 확장하여 $$\mathbb{R}^m$$의 orthonormal basis $$\{u_1,\ldots, u_m\}$$을 얻을 수 있다. ([§내적공간, §§정규직교기저](/ko/math/linear_algebra/inner_product_spaces#정규직교기저)) 

한편 $$r<i\leq n$$에 대하여는 

$$\lVert Av_i\rVert^2=\langle Av_i,Av_i\rangle=\langle A^tAv_i,v_i\rangle=\sigma_i^2\langle v_i,v_i\rangle=0$$

이므로 $$Av_i=0$$이다. 이제 $$u_i$$를 열로 갖는 $$U=(u_1\mid\cdots\mid u_m)$$과 $$v_i$$를 열로 갖는 $$V=(v_1\mid\cdots\mid v_n)$$을 정의하면, 두 행렬 모두 열이 orthonormal이므로 orthogonal matrix이다. $$\Sigma$$를 $$(i,i)$$ 성분이 $$\sigma_i$$ ($$1\leq i\leq r$$)이고 나머지가 $$0$$인 $$m\times n$$ diagonal matrix라 하면, $$AV$$와 $$U\Sigma$$의 $$i$$번째 열을 비교할 때 $$1\leq i\leq r$$에 대해서는 

$$Av_i=\sigma_iu_i$$

이고 $$U\Sigma$$의 $$i$$번째 열 또한 $$\sigma_iu_i$$이며, $$i>r$$에 대해서는 $$Av_i=0$$이고 $$\Sigma$$의 $$i$$번째 열이 $$0$$이므로 $$U\Sigma$$의 $$i$$번째 열도 $$0$$이다. 따라서 $$AV=U\Sigma$$이고, $$V$$가 orthogonal이므로 양변에 오른쪽에서 $$V^t=V^{-1}$$을 곱하면 $$A=U\Sigma V^t$$를 얻는다.

</details>

특이값 분해는 행렬의 rank를 특이값의 언어로 다시 표현해준다. 

<div class="proposition" markdown="1">

<ins id="cor4">**따름정리 4**</ins> 행렬 $$A\in\Mat_{m\times n}(\mathbb{R})$$의 rank는 $$0$$이 아닌 특이값의 개수와 같다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$A=U\Sigma V^t$$에서 $$U,V$$은 가역이므로 $$\rank A=\rank\Sigma$$이다. $$\Sigma$$의 $$0$$이 아닌 성분은 양의 특이값 $$\sigma_1,\ldots,\sigma_r$$ 뿐이고 이들은 서로 다른 행과 열에 놓이므로, $$\Sigma$$의 $$0$$이 아닌 열은 정확히 $$r$$개로 일차독립이다. 따라서 $$\rank A=r$$이다.

</details>

## 일반적인 유사역행렬

[§최소제곱법, ⁋정의 7](/ko/math/linear_algebra/least_squares_method#def7)에서 우리는 $$A$$가 full column rank이거나 full row rank일 때 유사역행렬을 정의하였고, 일반적인 경우의 정의는 특이값 분해를 이용한다고 예고하였다. 이제 그 정의를 제시한다. 

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> 행렬 $$A\in\Mat_{m\times n}(\mathbb{R})$$의 특이값 분해 $$A=U\Sigma V^t$$가 주어졌다 하자. $$\Sigma$$의 양의 특이값 $$\sigma_i$$들에 대하여, $$(i,i)$$ 성분이 $$1/\sigma_i$$이고 나머지가 $$0$$인 $$n\times m$$ diagonal matrix를 $$\Sigma^+$$이라 하자. 그럼 $$A$$의 *유사역행렬<sub>Moore-Penrose pseudoinverse</sub>*을 

$$A^+=V\Sigma^+U^t$$

으로 정의한다. 

</div>

이 정의가 [§최소제곱법, ⁋정의 7](/ko/math/linear_algebra/least_squares_method#def7)의 정의와 모순되지 않으며, 특이값 분해의 선택에 의존하지 않음을 확인해야 한다. 이는 다음 명제로부터 따라온다. 

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> [정의 5](#def5)의 행렬 $$A^+$$은 다음의 네 조건

$$AA^+A=A,\quad A^+AA^+=A^+,\quad (AA^+)^t=AA^+,\quad (A^+A)^t=A^+A$$

을 모두 만족한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\Sigma\Sigma^+$$은 $$(i,i)$$ 성분이 $$1\leq i\leq r$$일 때 $$1$$이고 나머지가 $$0$$인 $$m\times m$$ diagonal matrix이며, $$\Sigma^+\Sigma$$은 같은 방식으로 정의된 $$n\times n$$ diagonal matrix이다. 이들은 모두 symmetric이고, $$\Sigma\Sigma^+\Sigma=\Sigma$$, $$\Sigma^+\Sigma\Sigma^+=\Sigma^+$$임을 성분별로 직접 확인할 수 있다. 이제 $$A=U\Sigma V^t$$, $$A^+=V\Sigma^+U^t$$과 $$U^tU=I$$, $$V^tV=I$$을 이용하면

$$AA^+=U\Sigma V^tV\Sigma^+U^t=U(\Sigma\Sigma^+)U^t,\qquad A^+A=V(\Sigma^+\Sigma)V^t$$

이다. $$\Sigma\Sigma^+$$과 $$\Sigma^+\Sigma$$이 symmetric이므로 $$AA^+$$과 $$A^+A$$ 또한 symmetric이고, 이로써 셋째와 넷째 조건이 성립한다. 또 

$$AA^+A=U(\Sigma\Sigma^+)U^tU\Sigma V^t=U(\Sigma\Sigma^+\Sigma)V^t=U\Sigma V^t=A$$

이고, 같은 방식으로 

$$A^+AA^+=V(\Sigma^+\Sigma)V^tV\Sigma^+U^t=V(\Sigma^+\Sigma\Sigma^+)U^t=V\Sigma^+U^t=A^+$$

이므로 첫째와 둘째 조건도 성립한다.

</details>

[§최소제곱법](/ko/math/linear_algebra/least_squares_method)에서 언급하였듯 위 네 조건은 $$A^+$$을 유일하게 결정하므로, [정의 5](#def5)의 $$A^+$$은 특이값 분해의 선택과 무관하게 잘 정의된다. 뿐만 아니라 이는 full rank인 경우의 정의를 확장한다. 예를 들어 $$A$$가 full column rank라면 $$A^tA$$이 가역이고, 행렬 $$(A^tA)^{-1}A^t$$이 

$$\bigl((A^tA)^{-1}A^t\bigr)A=I_n,\qquad A\bigl((A^tA)^{-1}A^t\bigr)=A(A^tA)^{-1}A^t$$

으로부터 위 네 조건을 모두 만족함을 직접 확인할 수 있다. ($$A^tA$$이 symmetric이므로 그 역행렬도 symmetric이어서 $$A(A^tA)^{-1}A^t$$은 symmetric이다.) 따라서 유일성에 의하여 $$A^+=(A^tA)^{-1}A^t$$이고, 이는 [§최소제곱법, ⁋정의 7](/ko/math/linear_algebra/least_squares_method#def7)의 식과 일치한다. Full row rank인 경우도 마찬가지이다. 

<div class="remark" markdown="1">

<ins id="rmk7">**참고 7**</ins> 특이값 분해 $$A=U\Sigma V^t$$은 기하학적으로 임의의 linear map $$A$$가 orthonormal basis에 대한 회전 혹은 반사, 각 축으로의 $$\sigma_i$$배 확대, 그리고 또 다른 회전 혹은 반사의 합성으로 분해됨을 의미한다. $$V$$의 열 $$v_i$$를 *오른쪽 특이벡터*, $$U$$의 열 $$u_i$$를 *왼쪽 특이벡터*라 부르며, 이들은 각각 $$A^tA$$과 $$AA^t$$의 고유벡터이다. 가장 큰 몇 개의 특이값만 남기고 나머지를 $$0$$으로 두면 $$A$$를 낮은 rank의 행렬로 근사할 수 있는데, 이 근사가 여러 자연스러운 의미에서 최적이라는 사실이 특이값 분해를 응용에서 특히 유용하게 만든다. 

</div>

---

**참고문헌**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.  
**[TB]** L.N. Trefethen and D. Bau, *Numerical linear algebra*, SIAM, 1997.  
**[Str]** G. Strang, *Linear algebra and its applications*, 4th ed., Cengage Learning, 2006.

---
