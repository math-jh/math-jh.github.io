---

title: "행렬식의 존재성과 유일성"
excerpt: "행렬식의 존재성, 유일성 증명, 계산방법"

categories: [Math / Linear Algebra]
permalink: /ko/math/linear_algebra/existence_and_uniqueness_of_determinant
sidebar: 
    nav: "linear_algebra-ko"

header:
    overlay_image: /assets/images/Math/Linear_Algebra/Existence_and_uniqueness_of_determinant.png
    overlay_filter: 0.5

date: 2022-08-12
last_modified_at: 2022-08-12

weight: 21

---

## 대칭군

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 집합 $\\{1,\ldots, n\\}$에서 자기 자신으로의 모든 전단사함수들의 모임을 *symmetric group<sub>대칭군</sub>*이라 부르고, $S_n$으로 표기한다. $S_n$의 원소들을 *permutation<sub>치환</sub>*이라 부른다.

</div>

$S_n$의 원소들은 함수의 합성에 대하여 group을 이루며, 이 때의 항등원은 $\id$이며 함수 $\sigma\in S_n$의 역원은 역함수 $\sigma^{-1}$이다.

$S_n$의 원소들 중, $\id$ 다음으로 간단한 것은 $\\{1,\ldots, n\\}$의 원소들 중 두 개를 골라 이 둘의 위치를 바꾸는 함수이다. 예를 들어 $i,j\in \\{1,\ldots, n\\}$에 대하여 다음의 식

$$\sigma(k)=\begin{cases}i&\text{if $k=j$,}\\j&\text{if $k=i$,}\\k&\text{otherwise.}\end{cases}$$

으로 정의된 함수가 그러하다. 이러한 함수들을 *transposition<sub>호환</sub>*이라 부른다. 

$S_n$의 모든 원소들은 항상 transposition들의 유한한 합성으로 나타날 수 있다는 것이 잘 알려져 있다. 임의의 원소 $\sigma\in S_n$가 주어졌다 하고, 다음의 식과 같이 $\sigma$를 transposition들의 합성으로 나타내는 방법 두 가지가 주어졌다 하자.

$$\sigma=\tau_1\circ\tau_2\circ\cdots\circ\tau_n=\tau_1'\circ\tau_2'\circ\cdots\circ\tau_m'.$$

일반적으로 $m$과 $n$이 같을 필요는 없으나, $m,n$이 홀수인지 짝수인지의 여부는 항상 동일하다. 만일 이 숫자가 짝수일 경우, $\sigma$를 *even permutation<sub>짝치환</sub>*이라 부르고, 홀수라면 *odd permutation<sub>홀치환</sub>*이라 부른다. 그럼 함수 $\sgn:S_n\rightarrow\\{-1,1\\}$을 다음의 식

$$\sgn(\sigma)=\begin{cases}1&\text{if $\sigma$ is even}\\-1&\text{if $\sigma$ is odd}\end{cases}$$

으로 정의할 수 있다. 이 함수는 group homomorphism이 된다. 즉, 임의의 $\sigma,\sigma'\in S_n$에 대하여 

$$\sgn(\sigma\circ\sigma')=\sgn(\sigma)\sgn(\sigma')$$

이 성립한다.

임의의 alternating multilinear map $f:(F^n)^n\rightarrow F$가 주어졌다 하자. 그럼 $\sgn$의 정의에 의하여, 

$$f(v_1,v_2,\ldots, v_n)=\sgn(\sigma)f(v_{\sigma(1)},v_{\sigma(2)},\ldots, v_{\sigma(n)})$$

이 성립한다는 것을 알 수 있다.

## 행렬식의 존재성과 유일성

<div class="proposition" markdown="1">

<ins id="lem2">**보조정리 2**</ins> [§행렬식, ⁋정의 4](/ko/math/linear_algebra/determinant#def4)을 만족하는 함수 $D$는 유일하게 존재한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$f$가 alternating linear map이라 하자. 임의의 $v_1,\ldots, v_n\in V$에 대하여, 만일

$$v_i=v_1^ie_1+\cdots v_n^ie_n,\qquad i=1,\ldots, n$$

이라 하면

$$\begin{aligned}f(v_1,\ldots, v_n)&=\sum_{i_1=1}^nv_{i_1}^1f(e_{i_1},v_2,\ldots, v_n)\\
&=\sum_{i_1,i_2=1}^n v_{i_1}^1v_{i_2}^2f(e_{i_1},e_{i_2},v_3,\ldots, v_n)\\&=\cdots\\&=\sum_{i_1,\ldots, i_n=1}^nv_{i_1}^1v_{i_2}^2\ldots, v_{i_n}^nf(e_{i_1},\ldots, e_{i_n})\end{aligned}$$

이 성립한다. [§행렬식, ⁋명제 3](/ko/math/linear_algebra/determinant#prop3)에 의하여, $i_1,\ldots, i_n$들 중 같은 것이 존재한다면 $f(e_{i_1},\ldots,e_{i_n})$의 값은 항상 0이 되므로, 우변의 식은 

$$f(v_1,\ldots, v_n)=\sum_{\sigma\in S_n}v^1_{\sigma(1)}v^2_{\sigma(2)}\cdots v^n_{\sigma(n)}f(e_{\sigma(1)},\ldots, e_{\sigma(n)})$$

이 된다. 앞서 살펴본 $\sgn$의 성질에 의하여 이는 다시

$$f(v_1,\ldots, v_n)=\sum_{\sigma\in S_n}\sgn(\sigma)v^1_{\sigma(1)}v^2_{\sigma(2)}\cdots v^n_{\sigma(n)}f(e_1,e_2,\ldots, e_n)\tag{1}$$

과 같다. 따라서, 만일 $D,D'$가 행렬식의 정의를 만족하는 두 함수라면

$$D(e_1,\ldots, e_n)=D'(e_1,\ldots, e_n)=1$$

이므로 식 (1)에 의해 $D=D'$가 반드시 성립해야 한다. 

존재성의 경우, 마찬가지로 식 (1)에서 힌트를 얻어

$$D(v_1,\ldots, v_n)=\sum_{\sigma\in S_n}\sgn(\sigma)v^1_{\sigma(1)}v^2_{\sigma(2)}\cdots v^n_{\sigma(n)}$$

으로 정의한 후 $D$가 실제로 alternating multilinear map이 된다는 것을 보이면 된다. 이는 단순히 위의 계산을 반대방향으로 반복하는 것이므로 생략한다.

</details>

따라서 행렬식이 잘 정의되며, 이를 $\det$으로 적는다. 위 명제의 증명과정에서 우리는 행렬식 $\det A$를 식으로 얻어냈다. 즉, 행렬 $A$의 $i$번째 열벡터를 $A_i$로 표기하면 $A_i$의 $j$번째 성분은 $A_{ji}$와 같고, 따라서 

$$\det A=\sum_{\sigma\in S_n}\sgn(\sigma)A_{\sigma(1)1}A_{\sigma(2)2}\cdots A_{\sigma(n)n}\tag{2}$$

이 된다. 가령 $n=2$인 경우, $S_2$의 두 원소는 $\id$, 그리고 $1$과 $2$의 위치를 바꾸는 함수 $\sigma$이므로 행렬식은

$$\det A=\sum_{\sigma\in S_n}\sgn(\sigma)A_{\sigma(1)1}A_{\sigma(2)2}\cdots A_{\sigma(n)n}=\sgn(\id)A_{11}A_{22}+\sgn(\sigma)A_{21}A_{12}=A_{11}A_{22}-A_{21}A_{12}$$

이 된다. 일반적으로 $n$이 클 경우 이 식을 이용해서 행렬식의 값을 직접 계산하는 것은 번거롭지만, 행렬식에 관한 여러가지 성질을 증명할 때는 위의 식이 많은 도움이 된다.

<div class="proposition" markdown="1">

<ins id="cor4">**따름정리 4**</ins> 임의의 행렬 $A\in\Mat_n(F)$에 대하여, $\det(A^t)=\det A$가 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선, transposition들 $\tau_i$에 대하여 $\sigma=\tau_1\circ\ldots\tau_k$라면 $\sigma^{-1}=\tau_k^{-1}\circ\cdots\circ\tau_1^{-1}$이므로 $\sgn(\sigma)=\sgn(\sigma^{-1})$가 항상 성립한다. 이제 $A^t$의 정의로부터 $A_{ij}=(A^t)_{ji}$이고,

$$\det(A^t)=\sum_{\sigma\in S_n}\sgn(\sigma)A_{1\sigma(1)}\cdots A_{n\sigma(n)}=\sum_{\sigma\in S_n}\sgn(\sigma^{-1})A_{\sigma^{-1}(1)1}\cdots A_{\sigma^{-1}(n)n}$$

이므로 원하는 결과를 얻는다.

</details>

또, 위의 식으로부터 우리는 행렬식이 곱셈을 보존한다는 것을 알 수 있다.

<div class="proposition" markdown="1">

<ins id="lem5">**보조정리 5**</ins> 임의의 행렬 $A,B\in\Mat_n(F)$에 대하여, $\det(AB)=\det(A)\det(B)$가 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

행렬 $AB$의 $i,j$ 성분은 다음의 식

$$(AB)_{ij}=\sum_{k=1}^nA_{ik}B_{kj}$$

을 통해 얻어진다. 따라서, 

$$\begin{aligned}\det(AB)&=\det((AB)_1, (AB)_2,\ldots, (AB)_n)\\&=\sum_{\sigma\in S_n}\sgn(\sigma)(AB)_{\sigma(1)1}(AB)_{\sigma(2)2}\cdots(AB)_{\sigma(n)n}\\&=\sum_{\sigma\in S_n}\sgn(\sigma)\left(\sum_{i_1=1}^nA_{\sigma(1)i_1}B_{i_11}\right)\cdots\left(\sum_{i_n=1}^nA_{\sigma(n)i_n}B_{i_nn}\right)\\&=\sum_{\sigma\in S_n}\sum_{i_1,\ldots, i_n=1}^n\sgn(\sigma)A_{\sigma(1)i_1}\cdots A_{\sigma(n)i_n}B_{i_11}\cdots B_{i_nn}\\&=\sum_{i_1,\ldots, i_n=1}^nB_{i_11}\cdots B_{i_nn}\left(\sum_{\sigma\in S_n}\sgn(\sigma)A_{\sigma(1)1}\cdots A_{\sigma(n)n}\right)\\&=\sum_{i_1,\ldots, i_n=1}^n\det(A_{i_1},\ldots, A_{i_n})B_{i_11}\cdots B_{i_nn}\end{aligned}$$

이제 $\tau\in S_n$을 다음의 식

$$\tau(1)=i_1,\ldots, \tau(n)=i_n$$

을 만족하는 원소라고 정의하면, 위의 식의 우변은 다시

$$\sum_{\tau\in S_n}\sgn(\tau)\det(A)B_{\tau(1)1}\cdots B_{\tau(n)n}=\det(A)\det(B)$$

가 되므로, 증명이 완료된다.

</details>

우리는 이전 글에서 행렬 $A$가 가역인 것과 $\det A\neq 0$이 동치라는 것을 기하학적으로 설명했다. 방금 전의 [보조정리 5](#lem5)를 이용하면 이를 엄밀하게 증명할 수 있다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> 임의의 행렬 $A\in\Mat_n(F)$에 대하여, $\det A\neq 0$인 것과 $A$가 가역인 것이 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

선형대수학의 기본정리로부터, $A$가 가역인 것은 $A$에 의해 정의되는 linear map $L_A:F^n\rightarrow F^n$이 가역인 것과 동치라는 것을 안다. $F^n$은 유한차원이므로 이는 다시 $L_A$가 surjective인 것과 동치이고, 이는 $\col(A)$의 basis인 열벡터들 $A_1,\ldots, A_n$들이 일차독립인 것과 동치이다. 만일 $A_1,\ldots, A_n$들이 일차독립이 아니라면 [§행렬식, ⁋명제 3](/ko/math/linear_algebra/determinant#prop3)에 의하여 $\det A=0$이 된다. 즉, $\det A\neq 0$이라면 $A$는 가역이다.

거꾸로 $A$가 가역이라 가정하자. 그럼 다음의 식

$$1=\det(I)=\det(A^{-1}A)=\det(A^{-1})\det(A)\tag{3}$$

으로부터 $\det A\neq 0$임을 안다.

</details>

위의 명제의 증명에서 등장한 식 (3)으로부터 다음 따름정리를 얻는다.

<div class="proposition" markdown="1">

<ins id="cor7">**따름정리 7**</ins> 가역행렬 $A\in\Mat_n(F)$에 대하여 $\det(A^{-1})=(\det A)^{-1}$이 성립한다.

</div>

## 삼각행렬과 행렬식

앞서 살펴본 공식은 행렬식을 구하기 위해 $n!$개의 수를 계산해야 하므로 비효율적이다. 그러나 특정한 경우에는 이 공식이 유용하게 적용된다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> 행렬 $A\in\Mat\_n(F)$이 *상삼각행렬<sub>upper triangular matrix</sub>*이라는 것은 $i>j$일 때마다 $A_{ij}=0$인 것이다. 비슷하게, $i < j$일 때마다 $A\_{ij}=0$이라면 $A$를 *하삼각행렬<sub>lower triangular matrix</sub>*이라 부르고, 상삼각행렬과 하삼각행렬을 합쳐 간단히 *삼각행렬<sub>triangular matrix</sub>*이라 부른다.

한편, 행렬 $A$의 성분들 $A\_{ii}$를 $A$의 *대각성분*이라 하고, 만일 $i\neq j$일 때마다 $A\_{ij}=0$이라면 $A$를 *대각행렬<sub>diagonal matrix</sub>*이라 부른다. 

</div>

특별히 모든 $n\times n$ 행사다리꼴행렬은 모두 상삼각행렬이다. ([§가우스 소거법, ⁋정의 2](/ko/math/linear_algebra/Gaussian_elimination#def2))


<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> 임의의 삼각행렬 $A$에 대하여, $\det(A)$는 대각성분들의 곱과 같다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

위에서 살펴본 행렬식의 공식

$$\det A=\sum_{\sigma\in S_n}\sgn(\sigma)A_{\sigma(1)1}A_{\sigma(2)2}\cdots A_{\sigma(n)n}$$

을 다시 한 번 살펴보자. 임의의 $\sigma\in S_n$에 대하여, $\sigma$는 전단사함수이므로 만일 $\sigma(i)>i$인 $i$가 존재한다면 반드시 $\sigma(j)<j$인 $j$가 존재해야 한다. 따라서 위의 식에서 더해지는 값들은 $\sigma=\id$인 경우를 제외하면 항상 0이 된다. 

</details>

[§가우스 소거법](/ko/math/linear_algebra/Gaussian_elimination)에 의해 임의의 행렬은 기본행연산을 반복하여 행사다리꼴행렬로 바꿀 수 있다. 임의의 행사다리꼴행렬은 모두 상삼각행렬이므로, 위의 명제를 통하면 이렇게 얻어진 행사다리꼴행렬의 행렬식을 매우 쉽게 구할 수 있다. 한편 기본행연산을 적용하는 것은 기본행렬들을 곱하는 것과 같다. 따라서, 만일 행렬 $A$로부터 기본행연산 $E_1,\ldots, E_k$를 반복하여 행사다리꼴행렬 $A'$를 얻었다면, 

$$A'=E_kE_{k-1}\cdots E_1 A$$

이므로 

$$\det(A')=\det(E_k)\det(E_{k-1})\cdots\det(E_1)\det(A)$$

가 된다. 따라서 기본행렬들 $E\_{i,j}$, $E'\_{i,r}$, $E''\_{i,j,r}$의 행렬식을 살펴보자. 우선 $E\_{i,j}$와 $E'\_{i,r}$의 경우, 행렬식의 정의로부터 

$$\det E_{i,j}=-1,\quad \det E'_{i,r}=r$$

이라는 것을 쉽게 알 수 있다. 또, $E''\_{i,j,r}$은 반드시 삼각행렬이고, 대각성분의 곱이 1이므로 $\det E''\_{i,j,r}=1$이 성립한다. 

## Block matrix의 행렬식

한편, 행렬식의 공식 (2)를 이용하면 우리는 블록행렬의 행렬식 또한 구할 수 있다. 

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> $A\in\Mat_k(F)$이고 $I$가 $l\times l$ 항등행렬이라 하자. 그럼 다음의 블록행렬

$$\begin{pmatrix}A&O\\O&I\end{pmatrix}$$

의 행렬식의 값은 $\det A$와 같다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[명제 9](#prop9)의 증명과 거의 동일하다. 식 (2)을 통해 주어진 행렬의 행렬식을 계산하면

$$\det \begin{pmatrix}A&O\\O&I\end{pmatrix}=\sum_{\sigma\in S_{k+l}}\sgn(\sigma)A_{\sigma(1)1}A_{\sigma(2)2}\cdots A_{\sigma(k)k}B_{\sigma(k+1)(k+1)}\cdots B_{\sigma(k+l)(k+l)}$$

과 같다. 여기서 $B_{k+i}$는 $k+i$번째 성분만 $1$이고, 나머지 성분은 모두 $0$인 $F^{k+l}$의 원소이다. 그럼 

$$\sigma(k+1)=k+1,\ldots,\sigma(k+l)=k+1$$

이 아닌 이상 우변에서 더해지는 값은 항상 0이 되고, 따라서 뒤의 $l$개가 고정되는 $\sigma$에 대해서만 합을 계산하면 된다. 즉 주어진 행렬의 행렬식은 정확히 식 (2)와 동일하게 되어 주어진 명제가 성립한다. 

</details>

<div class="proposition" markdown="1">

<ins id="cor11">**따름정리 11**</ins> $A\in\Mat\_k(F),B\in\Mat\_l(F), C\in\Mat\_{l\times k}(F)$에 대하여, 다음의 블록행렬

$$\begin{pmatrix}A&O\\C&B\end{pmatrix}$$

의 행렬식은 $\det A\det B$와 같다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

다음의 식

$$\begin{pmatrix}A&O\\C&B\end{pmatrix}=\begin{pmatrix}A&O\\O&E\end{pmatrix}\begin{pmatrix}I&O\\O&I\end{pmatrix}\begin{pmatrix}I&O\\O&B\end{pmatrix}$$

과 [명제 10](#prop10), 그리고 [보조정리 5](#lem5)에 의해 자명하다. 마지막 행렬의 경우, $l$번의 행 바꿈 후 $l$번의 열 바꿈을 하여 $2l$번의 부호 변경이 생겨 주어진 행렬의 행렬식이 $\det B$와 같게 된다.

</details>

어렵지 않게 위의 결과들을 귀납적으로 확장할 수 있다. 즉

$$\det\begin{pmatrix}A_{11}&A_{12}&\cdots&A_{1n}\\O&A_{22}&\cdots&A_{2n}\\\vdots&\vdots&\ddots&\vdots\\O&O&\cdots&A_{nn}\end{pmatrix}=\det A_{11}\det A_{22}\cdots\det A_{nn}$$

이 성립한다. 다만 블록행렬로 표현하였을 때 삼각행렬이 되지 않는 경우에는 비슷한 결과가 성립하지 <em_ko>않는다</em_ko>. 예컨대 다음 블록행렬

$$\begin{pmatrix}A&B\\C&D\end{pmatrix}$$

의 행렬식의 값은 일반적으로 $\det A\det D-\det B\det C$와는 다르다.


## 라플라스 전개

$n$차 정사각행렬 $A$가 주어졌을 때, $A$의 행렬식을 가장 쉽게 구할 수 있는 방법 중 하나는 지금부터 소개할 라플라스 전개를 사용하는 것이다. 이를 위해서는 정의가 필요하다.

<div class="definition" markdown="1">

<ins id="def12">**정의 12**</ins> 행렬 $A\in\Mat_n(F)$이 주어졌다 하자. $1\leq i,j\leq n$에 대하여, $A^{(i,j)}$는 행렬 $A$의 $i$행, $j$열을 없애서 얻어지는 $(n-1)$차 정사각행렬이다.  

</div>

라플라스 전개는 $A$의 행렬식을 $\det A^{(i,j)}$들에 대한 식으로 나타내어준다. 

<div class="proposition" markdown="1">

<ins id="thm13">**정리 13**</ins> 임의의 행렬 $A\in\Mat_n(F)$과, 임의의 $1\leq i\leq n$에 대하여 다음의 식

$$\det A=\sum_{j=1}^n(-1)^{i+j}A_{ij}\det (A^{(i,j)})$$

이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $i,j$를 고정하자. $A$에서 $i$번째 행을 모두 $0$으로 바꾸되, 오직 $j$번째 성분만을 남겨둔 행렬을 $B_j$라 하자. 그 후, 행의 순서를 $i-1$번 바꾸어 $i$행을 첫째 행으로 올리고, 열의 순서를 $j-1$번 바꾸어 $j$열을 첫째 열로 가져와서 그 행렬을 $B_j'$라 하자. 그럼

$$B_j'=\begin{pmatrix}A_{ij}&0&\cdots&0\\A_{1j}&&&\\\vdots&&A^{(i,j)}&\\A_{nj}&&&\end{pmatrix}$$

이다. 이제 [명제 10](#prop10)에 의하여 이 행렬의 행렬식은 $A_{ij}\det A^{(i,j)}$와 같고, 따라서

$$\det B_j=(-1)^{i+j-2}\det B_j'=(-1)^{i+j-2}A_{ij}\det A^{(i,j)}=(-1)^{i+j}A_{ij}\det A^{(i,j)}$$

이다. 한편, $i$번째 열에 대한 multilinearity를 사용하면 $B_j$들의 행렬식의 합은 $A$의 행렬식과 같으므로 원하는 식

$$\det A=\sum_{j=1}^n\det B_j=\sum_{j=1}^n (-1)^{i+j}A_{ij}\det A^{(i,j)}$$

을 얻는다.

</details>

---

**참고문헌**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.

---