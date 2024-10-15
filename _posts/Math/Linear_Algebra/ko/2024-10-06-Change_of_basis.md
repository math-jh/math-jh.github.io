---

title: "기저변환"
excerpt: ""

categories: [Math / Linear Algebra]
permalink: /ko/math/linear_algebra/change_of_basis
header:
    overlay_image: /assets/images/Math/multilinear_Algebra/Change_of_basis.png
    overlay_filter: 0.5
sidebar: 
    nav: "linear_algebra-ko"

date: 2024-10-06
last_modified_at: 2024-10-06
weight: 8

---

## 정사각행렬

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $I\times I$ 행렬을 *정사각행렬<sub>square matrix</sub>*이라 부른다. 이들의 모임을 $\Mat_I(A)$로 적는다.

</div>

특별히 $I$가 유한집합이고 $A$가 commutative일 경우, $\Mat_{n}(A)$는 특별한 성질을 갖는데, 이 대상은 $A$-module일 뿐만 아니라 그 위에 정의된 곱셈 또한 가지고 있다. 즉 $\Mat_{n}(A)$는 $A$-algebra이다. 

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 이러한 상황에서 $\Mat_n(A)$는 unital associative algebra이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$\Mat_n(A)$가 associative $A$-algebra인 것은 [§행렬, §§행렬의 곱셈](/ko/math/linear_algebra/matrices#행렬의-곱셈)에서부터 자명하다. $\Mat_n(A)$의 곱셈에 대한 항등원은 다음의 항등행렬

$$I_n=\begin{pmatrix}1&0&\cdots&0\\0&1&\cdots&0\\\vdots&\vdots&\ddots&\vdots\\0&0&\cdots&1\end{pmatrix}$$

임을 확인할 수 있다. 

</details>

$M_n(A)$는 canonical basis $(E_{ij})$를 갖는데, 이들에 대해 structure constant를 생각해보면 다음 식

$$E_{ij}E_{jk}=\delta_{jh}E_{ik}$$

으로 적어줄 수 있다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> $\Mat_n(A)$의 원소들 가운데 곱셈에 대한 역원이 존재하는 것들을 모아 $\GL_n(A)$로 적는다. 

</div>

Free $A$-module $M$의 basis $\mathcal{B}=(e\_i)\_{i\in I}$를 고정하고, $\lvert I\rvert=n$이라 하자. 그럼 임의의 $u\in \End_{\lMod{A}}(M)$에 대하여, $\[u\]\_{\mathcal{B}}^\mathcal{B}\in\Mat\_n(A)$이며, 만일 $u$가 isomorphism이라면 [§행렬과 선형사상, ⁋따름정리 4](/ko/math/linear_algebra/matrices_and_linear_maps#lem4)에 의하여 $\[u\]_{\mathcal{B}}^\mathcal{B}\in\GL_n(A)$이다. 그럼 [§쌍대공간, ⁋명제 5](/ko/math/linear_algebra/dual_spaces#prop5)와 [§행렬과 선형사상, ⁋명제 5](/ko/math/linear_algebra/matrices_and_linear_maps#prop5)에 의하여 다음 식

$$\bigl([u^{-1}]_{\mathcal{B}}^\mathcal{B}\bigr)^t=\bigl(\bigl[u^\ast\bigr]_{\mathcal{B}^\ast}^{\mathcal{B}^\ast}\bigr)^{-1}$$

이 성립한다. 

## 기저변환

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> 임의의 $A$-module $M$과 $M$의 유한한 basis $\mathcal{B}=(e\_i)\_{i\in I}$가 주어졌다 하자. 그럼 다음 식

$$e_i'=\sum_{j=1}^n a_{ji}e_i,\qquad 1\leq i\leq n$$

이 $M$의 basis가 되는 것과, 정사각행렬 $(a_{ji})$의 역행렬이 존재하는 것이 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

주어진 행렬 $(a_{ji})$는 단순히 다음의 식

$$u:e_i\mapsto e_i'=\sum_{j=1}^n a_{ji}e_i$$

으로 정의되는 linear map $u\in\End_{\lMod{A}}(M)$의 $\mathcal{B}$에 대한 행렬표현 $\[u\]\_{\mathcal{B}}^\mathcal{B}\in\Mat\_n(A)$이다. 이제 이 행렬이 역행렬을 갖는 것은 $u$가 isomorphism인 것과 동치이고, 이는 $(u(e_i))_{i\in I}$가 $M$의 basis가 되는 것과 동치이다. 

</details>

위의 증명과는 반대로, 행렬 $(a_{ji})$를 identity map $\id_M:M \rightarrow M$을 서로 다른 basis에 대해 행렬표현을 한 것으로 생각할 수도 있다. Basis $(e_i')$를 $\mathcal{B}'$로 쓰기로 하자. 그럼 

$$\id_M(e_i')=\sum_{j=1}^n a_{ji}e_i$$

이므로, 

$$([\id_M]^{\mathcal{B}'}_\mathcal{B})=(\langle \id_M(e_i'), e_j^\ast\rangle)_{(j,i)\in J\times I}=(a_{ji})_{(j,i)\in J\times I}$$

이다. 이러한 관점에서 이 행렬을 $\mathcal{B}'$에서 $\mathcal{B}$로의 *기저변환 행렬<sub>change-of-basis matrix</sub>*이라 부르기도 한다. 

더 일반적으로 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> 두 $A$-module $M,N$과, 이들의 유한한 basis $\mathcal{B}=(e\_i)\_{i\in I}$, $\mathcal{C}=(f\_j)\_{j\in J}$가 각각 주어졌다 하자. $M$, $N$의 또 다른 basis $\mathcal{B}'=(e\_i')\_{i\in I}$, $\mathcal{C}'=(f\_j')\_{j\in J}$에 대하여, 다음의 식

$$[u]_{\mathcal{C}'}^{\mathcal{B}'}=[\id_N]^\mathcal{C}_{\mathcal{C}'}[u]^\mathcal{B}_\mathcal{C}[\id_M]^{\mathcal{B}'}_{\mathcal{B}}$$

이 성립한다.

</div>

## 닮은 행렬

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> 두 $m\times n$ 행렬 $X, X'$가 *equivalent<sub>동치인 행렬</sub>*이라는 것은 정사각행렬 $P\in\GL_m(A)$와 $Q\in\GL_n(A)$가 존재하여 $X'=PXQ$이도록 할 수 있는 것을 뜻한다. 

</div>

[\[기초선형대수학\] §기저변환, ⁋정의 2](/ko/math/basic_linear_algebra/change_of_basis#def2) 이전의 논의와 같은 맥락에서, equivalent matrix보다는 더 세밀한 다음의 동치관계를 생각하는 것이 좋다.

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> 두 $n\times n$ 행렬 $X, X'$가 *similar<sub>닮은 행렬</sub>*이라는 것은 정사각행렬 $P\in\GL_n(A)$가 존재하여 $X'=PXP^{-1}$이도록 할 수 있는 것을 뜻한다. 

</div>

그럼 위의 [명제 5](#prop5)에서 $M=N$, $\mathcal{B}=\mathcal{C}$, $\mathcal{B}'=\mathcal{C}'$로 두면, $\End_\rMod{A}(M)$의 원소 $u$를 서로 다른 basis를 통해 행렬표현한 것은 서로 similar함임을 안다. 

