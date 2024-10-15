---

title: "역행렬 (작성중)"
excerpt: "역행렬의 계산"

categories: [Math / Basic Linear Algebra]
permalink: /ko/math/basic_linear_algebra/inverse_matrix
sidebar: 
    nav: "basic_linear_algebra-ko"

header:
    overlay_image: /assets/images/Math/Basic_Linear_Algebra/Inverse_matrix.png
    overlay_filter: 0.5

date: 2022-08-19
last_modified_at: 2022-08-19

weight: 22

---

우리는 지금까지의 논의로부터 임의의 정사각행렬 $A$가 역행렬을 갖는 것은 $\det A\neq 0$인 것과 동치인 것을 알고, 또 행렬식 $\det A$를 쉽게 계산하는 법 또한 알고있다. 그러나 이는 $A$의 역행렬이 정확히 어떤 모양인지를 알려주지는 않는다. 이번 글에서는 $A$의 역행렬을 직접 계산하는 과정을 살펴본다. 

우선 다음의 간단한 보조정리를 보이자.

<div class="proposition" markdown="1">

<ins id="lem1">**보조정리 1**</ins> 행렬 $A\in\Mat_n(\mathbb{k})$에 대하여, 다음 세 조건이 모두 동치이다.

1. $A$가 가역이다.
2. 적당한 $B\in\Mat_n(\mathbb{k})$가 존재하여 $AB=I$이다.
3. 적당한 $B\in\Mat_n(\mathbb{k})$가 존재하여 $BA=I$이다.

뿐만 아니라 둘째, 셋째 조건이 성립할 경우 $B=A^{-1}$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

첫 번째 조건이 각각 두 번째와 세 번째를 함의하는 것은 자명하므로, 반대방향만 보이면 충분하다. 

우선 적당한 $B\in\Mat_n(\mathbb{k})$가 존재하여 $AB=I$가 성립한다고 가정하자. 그럼 선형대수학의 기본정리에 의하여 

$$L_A\circ L_B=\id_{\mathbb{k}^n}$$

이 성립한다. 이제 $\id_{\mathbb{k}^n}$이 전단사함수라는 것으로부터 $L_A:\mathbb{k}^n\rightarrow \mathbb{k}^n$이 전사함수라는 것을 안다. ([\[집합론\] §Retraction과 section, ⁋명제 3](/ko/math/set_theory/retraction_and_section#prop3)) 따라서 다음의 식 ([§동형사상, ⁋정리 7](/ko/math/basic_linear_algebra/isomorphic_vector_spaces#thm7))

$$\rank L_A+\nullity L_A=\dim \mathbb{k}^n=n$$

으로부터 $\nullity L_A=0$임을 안다. 즉 $L_A$는 단사함수이기도 하고, 따라서 $L_A$는 전단사함수이고 행렬 $A$는 가역이다. 이제 식 $AB=I$의 양 변의 왼쪽에 $A^{-1}$을 곱하면 $B=A^{-1}$을 얻는다.

비슷하게 셋째 조건이 첫째 조건을 함의한다는 것을 증명할 수 있다.  

</details>

$n\times n$ 가역행렬 $B$가 주어졌다 하자. $B$를 $\mathbb{k}^n$에서 $\mathbb{k}^n$으로의 linear map으로 생각하면, $B$는 $\mathbb{k}^n$의 basis $e_1,\ldots, e_n$을 어디로 옮기는지에 의해 완전하게 결정된다. 따라서 행렬 $A^{-1}$를 계산하기 위해서는 $A^{-1}$이 basis $e_i$를 어디로 옮기는지를 알면 된다. 이 값을 벡터 $v_i$라 하면, 행렬 $A$는 $(v\_1\|v\_2\|\cdots\|v\_n)$으로 주어질 것이며, 이 때 각각의 $v_i$들은 다음의 식

$$v_i=A^{-1}e_i\iff Av_i=e_i$$

으로 정의된다. 이 식을 풀기 위해 가우스 소거법을 적용하되, 이를 각 $i$마다 적용하는 대신 다음의 *첨가행렬*을 이용하면 더 빠르게 계산할 수 있다.

img

---

**참고문헌**

**[Lee]** 이인석, *선형대수와 군*, 서울대학교 출판문화원, 2005.

---