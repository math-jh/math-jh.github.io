---

title: "행렬과 선형사상"
excerpt: ""

categories: [Math / Multilinear Algebra]
permalink: /ko/math/multilinear_algebra/matrices_and_linear_maps
header:
    overlay_image: /assets/images/Math/multilinear_Algebra/Matrices_and_linear_maps.png
    overlay_filter: 0.5
sidebar: 
    nav: "multilinear_algebra-ko"

date: 2024-09-05
last_modified_at: 2024-09-19
weight: 7

---

## 좌표표현

이제 우리는 행렬과 linear map 사이의 관계를 살펴본다. 이는 [\[선형대수학\] §선형대수학의 기본정리, ⁋정리 5](/ko/math/linear_algebra/ftla#thm5)의 일반화라 생각할 수 있다. 편의를 위해 

Free $A$-module $M$이 주어졌다 하고, $M$의 basis $\mathcal{B}=(e\_i)\_{i\in I}$를 고정하자. 그럼 임의의 $x\in M$은 

$$x=\sum_{i\in I} x_i e_i,\qquad x_i\in A$$

으로 쓸 수 있으며, 이렇게 일차결합으로 나타냈을 때 $e_i$들의 계수에 해당하는 $x_i$들로 이루어진 열벡터 $(x\_{i0})\_{(i,0)\in I\times\\{0\\}}$를 $x$의 *$\mathcal{B}$에 대한 좌표표현*이라 부르고 $[x]_\mathcal{B}$로 적는다. 한편 coordinate form을 사용하면 $x_i$를 복잡한 설명 없이 식 

$$x_i=\langle x,e_i^\ast\rangle\tag{1}$$

으로 적을 수 있는 것도 눈여겨 볼 만하다. ([§쌍대공간, ⁋정의 6](/ko/math/multilinear_algebra/dual_spaces#def6))

## 선형사상의 행렬표현

남은 글에서 우리는 두 free $A$-module $M,N$이 주어졌다 하고, 이들의 basis $\mathcal{B}=(e\_i)\_{i\in I}$, $\mathcal{C}=(f\_j)\_{j\in J}$를 고정한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 위와 같은 상황에서, 임의의 $A$-linear map $u:M \rightarrow N$이 주어졌다 하자. 그럼 $u$의 *행렬표현*은 다음의 행렬

$$[u]_\mathcal{C}^\mathcal{B}=(f_j^\ast(u(e_i)))_{(j,i)\in J\times I}=(\langle u(e_i), f_j^\ast\rangle)_{(j,i)\in J\times I}$$

을 의미한다. 

</div>

그럼 우선 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> Linear map $u:M \rightarrow N$의 행렬표현 $[u]\_\mathcal{C}^\mathcal{B}$의 $i$번째 열은 $u(e\_i)$의 $\mathcal{C}$에 대한 좌표표현 $[u(e\_i)]\_\mathcal{C}$와 같다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

정의에 의하여 $[u]\_\mathcal{C}^\mathcal{B}$의 $i$번째 열은 다음 식

$$(f_j^\ast(u(e_i)))_{j\in J}=(\langle u(e_i), f_j^\ast\rangle)_{j\in J}$$

으로 주어진다. 이제 이 열벡터의 $j$번째 성분은 앞선 식 (1)에 의하여, 정확히 $u(e_i)$를 basis $\mathcal{C}$에 대해 일차결합으로 나타났을 때 $f_j$의 계수와 같다. 

</details>

만일 또 다른 $A$-linear map $v:M \rightarrow N$이 주어졌다면

$$[u+v]_\mathcal{C}^\mathcal{B}=[u]_\mathcal{C}^\mathcal{B}+[v]_\mathcal{C}^\mathcal{B}$$

가 성립하는 것을 확인할 수 있다. 또, 만일 $\alpha$가 $A$의 center에 포함된다면 $\alpha u$는 $A$-linear map이며, 이 $A$-linear map의 행렬표현은

$$[\alpha u]_\mathcal{C}^\mathcal{B}=\alpha[u]_\mathcal{C}^\mathcal{B}$$

로 주어지는 것을 알 수 있다. 요약하자면 $u\mapsto [u]\_\mathcal{C}^\mathcal{B}$는 $\Hom\_{\lMod{A}}(M,N)$에서 $\Mat\_{J\times I}(A)$로의 $Z(A)$-module homomorphism이다. 이 $Z(A)$-linear map은 injective인데, 이는 $u=0$인 것과 모든 $i\in I$에 대하여 $u(e_i)=0$인 것이 서로 동치이기 때문이다. 한편, 만일 $J$가 유한집합이라면 $\Mat_{J\times I}(A)$의 임의의 원소 $(x_{ji})$에 대하여, $u\in\Hom_\lMod{A}$를 다음 식

$$u(e_i)=\sum_{j\in J} \langle u(e_i),f_j^\ast\rangle f_j$$

으로 정의하여 위의 $Z(A)$-linear map의 inverse를 만들 수 있으므로 이것이 $Z(A)$-isomorphism이 된다.

## 행렬표현의 곱

우리는 앞서 두 행렬의 곱을 정의하는 방법을 살펴보았다. [\[선형대수학\] §선형대수학의 기본정리, ⁋정리 5](/ko/math/linear_algebra/ftla#thm5)와 마찬가지로, 이들 행렬의 곱은 선형사상의 합성에 대응된다. 우선 다음 명제를 보이자.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> 만일 $I,J$가 유한집합이라면 임의의 linear map $u:M \rightarrow N$과 $x\in M$에 대하여 다음 식

$$[u(x)]_\mathcal{C}=[u]_\mathcal{C}^\mathcal{B}[x]_\mathcal{B}$$

이 성립한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우변의 식은 열벡터가 나오는 것을 확인할 수 있으며, 이 때 [§행렬, §§행렬의 곱셈](/ko/math/multilinear_algebra/matrices#행렬의-곱셈)의 식 (2)에 의하여, 우변의 식의 $j$번째 성분은 

$$\left([u]_\mathcal{C}^\mathcal{B}[x]_\mathcal{B}\right)_{j0}=\sum_{i\in I}\left([u]_\mathcal{C}^\mathcal{B}\right)_{ji}\left([x]_\mathcal{B}\right)_{i0}=\sum_{i\in I}\left\langle u(e_i),f_j^\ast\right\rangle \left\langle x,e_i^\ast\right\rangle$$

와 같다. 한편 좌변을 살펴보면 $x=\sum_{i\in I}x_i e_i$이므로, $[u(x)]_\mathcal{C}$의 $j$번째 성분이

$$\langle u(x),f_j^\ast\rangle=\left\langle u\left(\sum_{i\in I} x_i e_i\right), f_j^\ast\right\rangle=\left\langle \sum_{i\in I} x_i u(e_i), f_j^\ast\right\rangle=\sum_{i\in I}x_i\langle u(e_i),f_j^\ast\rangle=\sum_{i\in I}\left\langle u(e_i),f_j^\ast\right\rangle \left\langle x,e_i^\ast\right\rangle$$

가 되어 원하는 결과를 얻는다.

</details>

이를 [명제 2](#prop2)와 합치면 다음 결과를 얻는다.

<div class="proposition" markdown="1">

<ins id="cor4">**따름정리 4**</ins> 세 $A$-module $M,N,L$이 주어졌다 하고, 유한한 basis $\mathcal{B}=(e\_i)\_{i\in I},\mathcal{C}=(f\_j)\_{j\in J},\mathcal{D}=(g\_k)\_{k\in K}$를 고정하자. 그럼 임의의 linear map $u:M \rightarrow N$, $v:N \rightarrow L$에 대하여, 다음 식

$$[v \circ u]_\mathcal{D}^\mathcal{B}=[v]_\mathcal{D}^\mathcal{C}[u]_\mathcal{C}^\mathcal{B}$$

이 성립한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $x\in M$에 대하여,

$$[v \circ u]_\mathcal{D}^\mathcal{B}[x]_\mathcal{B}=[(v \circ u)(x)]_\mathcal{D}=[(v(u(x))]_\mathcal{D}=[v]_\mathcal{D}^\mathcal{C}[u(x)]_\mathcal{C}=[v]_\mathcal{D}^\mathcal{C}[u]_\mathcal{C}^\mathcal{B}[x]_\mathcal{B}$$

이므로, $Z(A)$-isomorphism $\Mat_{K\times I}(A)\cong\Hom_\lMod{A}(M,L)$로부터 원하는 결과를 얻는다. 

</details>

## 행렬표현의 전치

한편, 전치행렬 또한 선형사상에서 대응되는 개념을 갖는다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> 만일 $I,J$가 유한집합이라면 임의의 linear map $u:M \rightarrow N$에 대하여 다음 식

$$\left([u]_\mathcal{C}^\mathcal{B}\right)^t=\left[u^\ast\right]_{\mathcal{B}^\ast}^{\mathcal{C}^\ast}$$

이 성립한다. 여기서 $\mathcal{B}^\ast$와 $\mathcal{C}^\ast$는 각각 $\mathcal{B},\mathcal{C}$의 dual basis이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[§쌍대공간, ⁋명제 8](/ko/math/multilinear_algebra/dual_spaces#prop8)에 의하여 $M$과 $M^{\ast\ast}$를 같은 것으로 취급할 수 있고, 이 때 $\mathcal{B}$는 $\mathcal{B}^\ast$의 dual basis $\mathcal{B}^{\ast\ast}$에 대응되게 된다. 이제

$$\left(\left[u^\ast\right]_{\mathcal{B}^\ast}^{\mathcal{C}^\ast}\right)_{ji}=\langle u^\ast(f_j^\ast), e_i^{\ast\ast}\rangle=\langle e_i, u^\ast(f^\ast)\rangle=\langle u(e_i), f_j^\ast\rangle=\left([u]_\mathcal{C}^\mathcal{B}\right)_{ij}=\left(\left([u]_\mathcal{C}^\mathcal{B}\right)^t\right)_{ji} $$

이므로 원하는 결과를 얻는다.

</details>

## 행렬표현과 trace

앞서 우리는 [§Hom과 텐서곱, ⁋정의 4](/ko/math/multilinear_algebra/hom_and_tensor#def4)에서 linear map의 trace를 정의하였다. 이번에는 임의의 $n\times n$ 행렬 $X$에 대하여, $X$의 trace를 다음 식

$$\tr(X)=\sum_{i=1}^n x_{ii}$$

으로 정의하자. 그럼 임의의 $u\in\End_\rMod{A}(M)$에 대하여, basis $\mathcal{B}=(e\_i)\_{1\leq i\leq n}$를 고정하고 $[u]\_\mathcal{B}^\mathcal{B}$를 생각하면

$$\tr([u]_\mathcal{B}^\mathcal{B})=\sum_{i=1}^n ([u]_\mathcal{B}^\mathcal{B})_{ii}=\sum_{i=1}^n\langle u(e_i), e_i^\ast\rangle$$

이다. 한편 자명한 이유로

$$u(x)=\sum_{i=1}^n \langle x, e_i^\ast\rangle u(e_i)$$

이므로 $\tr(u)=\tr([u]_\mathcal{B}^\mathcal{B})$를 얻는다. 이로부터 $X\in\Mat_{m\times n}(A)$, $Y\in\Mat_{n\times m}(A)$에 대하여 

$$\tr(XY)=\tr(YX)$$

이 성립한다.

## 블록행렬

마지막으로 우리는 더 일반적으로 두 free $A$-module $M,N$이 각각 submodule들의 direct sum

$$M=\bigoplus_{i\in I}M_i,\qquad N=\bigoplus_{j\in J} N_j$$

의 꼴로 쓰여지는 경우를 생각한다. 특별히 $M_i$, $N_j$들 모두가 $A$라면 위에서의 상황과 동일한 상황이 된다. 그럼 임의의 $x$를

$$x=\sum_{i\in I} x_i,\qquad x_i\in M_i$$

의 꼴로 유일하게 적을 수 있으며, 이 decomposition에 대한 $x$의 좌표표현을

$$[x]_I=(x_{i0})_{i\in I}$$

으로 정의한다. 또, 임의의 $A$-linear map $u: M \rightarrow N$에 대하여

$$u(x_i)=\sum_{j\in J} u_{ji}(x_i),\qquad u_{ji}(x_i)\in N_j$$

으로 적고 나면 다음의 행렬

$$[u]^I_J=(u_{ji})_{(j,i)\in J\times I}$$

이 잘 정의된다. 이 행렬은 다음의 ring

$$H=\bigoplus_{(j,i)\in J\times I}\Hom_{\lMod{A}}(M_i,N_j)$$

위에 정의된 $J\times I$ 행렬로 생각할 수 있다.

이러한 일반화를 하여도 위에서 살펴본 모든 명제들이 그대로 성립함을 확인할 수 있다. 특히 행렬의 곱이 주목할 만한데, $I,J$가 모두 유한하고, 여기에 더해 각각의 $M_i$와 $N_j$들이 유한한 basis $\mathcal{B}\_i$, $\mathcal{C}\_j$들을 갖는다 하자. 그럼 이들의 basis를 모두 모아둔 것들이 각각 $M$과 $N$의 basis $\mathcal{B},\mathcal{C}$를 이룬다. 그럼 이 basis에 대해 linear map $u:M \rightarrow N$을 행렬로 나타낸 것은, 위의 $[u]\_J^I$에서 각각의 성분 $u_{ji}$들을 basis $\mathcal{B}\_i$, $\mathcal{C}\_j$에 대해 행렬로 나타낸 것을 대입한 행렬과 같음을 확인할 수 있으며, 이것이 행렬의 곱에 대해 유의미하게 행동한다. 즉, 또 다른 direct sum $L=\bigoplus\_{k\in K} L\_k$와, basis $\mathcal{D}=\bigcup \mathcal{D}\_k$에 대하여 $v:N \rightarrow L$을 마찬가지 방식으로 써 보면, $v\circ u$의 basis $\mathcal{B}, \mathcal{D}$에 대한 행렬표현은 다음의 행렬

$$\sum_{j\in J}[v_{kj}]_{\mathcal{D}_k}^{\mathcal{C}_j}[u_{ji}]_{\mathcal{C}_j}^{\mathcal{B}_i}$$

이 $(k,i)$ 성분에 들어있는 행렬이 된다. 