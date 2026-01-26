---

title: "조르당 표준형"
excerpt: ""

categories: [Math / Linear Algebra]
permalink: /ko/math/linear_algebra/Jordan_canonical_form
header:
    overlay_image: /assets/images/Math/Linear_Algebra/Primary_decomposition_theorem.png
    overlay_filter: 0.5
sidebar: 
    nav: "linear_algebra-ko"

date: 2026-01-21
last_modified_at: 2026-01-21
weight: 17

---

## 일반화된 고유공간

앞서 우리는 diagonalizable operator $A$가 주어질 때마다 주어진 공간을 eigenspace들로 분해하여 이 위에서는 $A$가 스칼라곱처럼 행동하도록 할 수 있음을 보았다. 그러나 [§고유공간분해, ⁋명제 6](/ko/math/linear_algebra/eigenspace_decomposition#prop6)에서 살펴봤듯, 설령 $\mathbb{K}$가 algebraically closed field라 가정하여도 (그리고, 해당 명제 이후에 살펴봤듯 우리는 항상 이를 가정할 것이다.) 모든 linear operator가 항상 diagonalizable인 것은 아니다. 

[§고유공간분해, ⁋명제 6](/ko/math/linear_algebra/eigenspace_decomposition#prop6)의 둘째 조건은 $A$의 어떤 고유값 $\lambda$에 대하여, $\lambda$의 기하적 중복도가 $\lambda$의 대수적 중복도보다 작을 때 발생한다는 것을 알려준다. ([§고유공간분해, ⁋명제 5](/ko/math/linear_algebra/eigenspace_decomposition#prop5)) 즉, 직관적으로 다음의 벡터공간

$$E_\lambda(A)=\ker(A-\lambda I)$$

이 <em_ko>너무 작은</em_ko> 것이다. 다음 보조정리는 이를 해결할만한 실마리를 준다. 

<div class="proposition" markdown="1">

<ins id="lem1">**보조정리 1**</ins> 유한차원 벡터공간 $V$ 위에 정의된 임의의 linear operator $L:V\rightarrow V$이 주어졌다 하자. 표기의 편의를 위하여 $L^0=\id_V$라 하면, 다음 filtration

$$0=\ker L^0\subsetneq \ker L^1\subsetneq \ker L^2\subsetneq \cdots \subsetneq \ker L^{k-1}\subsetneq \ker L^k=\ker L^{k+1}$$

이 존재한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 임의의 $i$에 대하여 만일 $v\in \ker L^{i}$가 성립한다면, 

$$L^{i+1}v=L(L^iv)=L(0)=0$$

이므로 $\ker L^i\subseteq \ker L^{i+1}$인 것이 당연하다. 한편 $V$가 유한차원이므로 이 filtration은 언젠가는 증가하기를 멈춰야 한다. 우리가 보여야 할 것은 만일 $\ker L^k=\ker L^{k+1}$이라면, 이 이후의 항들은 <em_ko>모두</em_ko> $\ker L^k$와 같다는 것이다. 이를 위해, $k$가 $\ker L^k=\ker L^{k+1}$을 만족하는 정수 중 가장 작은 것이라 하자. 그럼 그 정의에 의하여 $\ker L^k=\ker L^{k+1}$이며, 우리는 이를 base step으로 삼아 귀납적으로 $\ker L^k=\ker L^{k+j}$가 모든 $j$에 대해 성립하는 것을 보일 수 있다. 즉, $\ker L^k=\ker L^{k+j}$가 성립함을 가정하고 $\ker L^k=\ker L^{k+j+1}$임을 보이자. 이를 위해서는 $\ker L^{k+j+1}\subseteq \ker L^k$임을 보이면 충분하다. 이제 임의의 $v\in \ker L^{k+j+1}$에 대하여, 우리는 $Lv\in \ker L^{k+j}=\ker L^k$임을 알고 있으므로 다음의 계산

$$L^{k+1}v=L^k(Lv)=0\implies v\in \ker L^{k+1}$$

과 base step $\ker L^k=\ker L^{k+1}$로부터 원하는 결과를 얻는다. 

</details>

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> 다음의 행렬

$$A=\begin{pmatrix}1&1&1\\0&1&1\\0&0&1\end{pmatrix}$$

을 생각하자. 우리는 앞선 글에서 이 행렬의 특성다항식은 $(\x-1)^3=0$이지만 (즉 유일한 고유값 $1$의 대수적 중복도가 $3$이지만) 이에 해당하는 고유공간 $E_1(A)$는 벡터 $(1,0,0)$으로 생성되는 $1$차원 공간임을 보았다. 

이제 linear operator

$$A-1I=\begin{pmatrix}0&1&1\\0&0&1\\0&0&0\end{pmatrix}$$

에 위의 보조정리를 적용해보자. 언급한 것과 같이 

$$\ker (A-I)=\span \{(1,0,0)\}$$

이다. 그런데 높은 차수의 계산을 수행해보면,

$$\ker(A-I)^2=\ker \begin{pmatrix}0&0&1\\0&0&0\\0&0&0\end{pmatrix}\span \{(1,0,0), (0,1,0)\}$$

그리고

$$\ker (A-I)^3=\ker \begin{pmatrix}0&0&0\\0&0&0\\0&0&0\end{pmatrix}=\span \{(1,0,0), (0,1,0), (0,0,1)\}$$

임을 안다. 

</div>

즉, 위의 예시에서 고유공간 $\ker (A-I)$ 자체는 그 차원이 부족하지만, [보조정리 1](#lem1)을 사용하여 이 공간을 늘려가다 보면 "맞는 차원"을 얻게 된다. 이를 엄밀하게 서술하기 위해서는 몇가지 준비가 필요하다. 

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 유한차원 벡터공간 $V$ 위에 정의된 linear operator $L$와 $L$의 한 eigenvalue $\lambda$에 대하여, $L$의 $\lambda$에 대한 *generalized eigenspace*를 다음의 식

$$G_\lambda(L)=\left\{v\in V\mid (L-\lambda I)^kv=0\text{ for some $k\geq 0$}\right\}$$

으로 정의한다. 

</div>

그럼 우리가 보이고 싶은 것은, 당연히, *임의의* linear operator $L:V \rightarrow V$를 generalized eigenspace들의 direct sum으로 분해할 수 있다는 것이며 이는 참이다. 한편, 우리는 [보조정리 1](#lem1)로부터 다음을 얻는다.

<div class="proposition" markdown="1">

<ins id="cor4">**따름정리 4**</ins> 유한차원 벡터공간 $V$ 위에 정의된 linear operator $L:V\rightarrow V$과 그 eigenvalue $\lambda$에 대하여, 적당한 양의 정수 $k$가 존재하여 $G_\lambda(L)=\ker(L-\lambda I)^k$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[보조정리 1](#lem1)을 linear operator $L-\lambda I$에 적용하면, 

$$\ker(L-\lambda I)^k=\ker(L-\lambda I)^{k+1}=\cdots$$

를 만족하는 $k$가 존재한다. 한편 정의에 의해 임의의 $v\in G_\lambda(L)$에 대하여, $(L-\lambda I)^m v=0$을 만족하는 $m$이 존재하는데, $k' =\max(k,m)$이라 하면 $(L-\lambda I)^{k'}v=0$이고 $k'\geq k$이므로 $v\in \ker(L-\lambda I)^{k'}=\ker(L-\lambda I)^k$이다.

</details>

## 일차분해정리

이제 우리의 주요 정리를 증명할 준비가 되었다.

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5 (일차분해정리)**</ins> 유한차원 벡터공간 $V$ 위에 정의된 linear operator $L:V\rightarrow V$에 대하여, $L$의 모든 eigenvalue들을 $\lambda_1,\ldots,\lambda_m$이라 하자. 그럼 다음의 직합분해

$$V=G_{\lambda_1}(L)\oplus G_{\lambda_2}(L)\oplus\cdots\oplus G_{\lambda_m}(L)$$

가 성립한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 각 $G_{\lambda_i}(L)$이 $V$의 부분공간임은 자명하다. $L$의 특성다항식을 

$$p_L(\mathbf{x})=\prod_{i=1}^m (\mathbf{x}-\lambda_i)^{m_i}$$

라 하자. 여기서 $m_i$는 $\lambda_i$의 대수적 중복도이고 $\sum_{i=1}^m m_i=\dim V$이다.

**1단계: 서로 다른 generalized eigenspace의 교집합**

$i\neq j$일 때 $G_{\lambda_i}(L)\cap G_{\lambda_j}(L)=\{0\}$임을 보이자. $v\in G_{\lambda_i}(L)\cap G_{\lambda_j}(L)$이고 $v\neq 0$이라 가정하자. [따름정리 4](#cor4)로부터 $(L-\lambda_i I)^{k_i}v=0$과 $(L-\lambda_j I)^{k_j}v=0$을 만족하는 정수 $k_i, k_j$가 존재한다. 

$p$를 $(L-\lambda_i I)^{k_i}v=0$을 만족하는 최소 음이 아닌 정수라 하면, $w=(L-\lambda_i I)^p v$는 $Lw=\lambda_i w$를 만족하는 영이 아닌 벡터, 즉 고유값 $\lambda_i$에 대응하는 고유벡터이다.

한편 $v\in G_{\lambda_j}(L)$이므로 $(L-\lambda_j I)^{k_j}v=0$이고, $(L-\lambda_i I)$와 $(L-\lambda_j I)$는 commute하므로

$$(L-\lambda_j I)^{k_j}w=(L-\lambda_j I)^{k_j}(L-\lambda_i I)^p v=(L-\lambda_i I)^p(L-\lambda_j I)^{k_j}v=0$$

이다. 따라서 $w\in \ker(L-\lambda_j I)^{k_j}=G_{\lambda_j}(L)$이다. 그런데 $w$는 고유값 $\lambda_i$에 대응하는 고유벡터이면서 동시에 $G_{\lambda_j}(L)$에 속한다. 

만약 $v'\in G_{\lambda_j}(L)$이고 $(L-\lambda_j I)^s v'=0$이면, 어떤 최소 양의 정수 $q$ 이전의 단계에서 $(L-\lambda_j I)^{q-1}v'\neq 0$이고 $(L-\lambda_j I)^q v'=0$이다. 즉 $(L-\lambda_j I)^{q-1}v'$는 고유값 $\lambda_j$에 대응하는 고유벡터이다. 따라서 generalized eigenspace의 모든 벡터는 같은 고유값에만 대응하는 고유벡터를 생성하므로, $w$가 고유값 $\lambda_i$에 대응하면서 동시에 $G_{\lambda_j}(L)$에 속할 수 없다. 이는 모순이므로 $v=0$이어야 한다.

**2단계: generalized eigenvector의 선형독립성**

서로 다른 generalized eigenspace에서 각각 뽑은 벡터들의 모임은 일차독립임을 보이자. 귀납법을 사용한다.

기저 단계: $m=1$일 때 당연하다.

귀납 단계: $m$개의 distinct eigenvalue들에 대해 성립한다고 가정하고, $m+1$개에 대해 보이자.

$v_i \in G_{\lambda_i}(L)$ ($i=1,\ldots,m+1$)에 대해 

$$v_1+v_2+\cdots+v_{m+1}=0$$

이라 하자. $(L-\lambda_{m+1}I)^{k_{m+1}}$을 양변에 작용시키면 ($G_{\lambda_{m+1}}(L)=\ker(L-\lambda_{m+1}I)^{k_{m+1}}$),

$$(L-\lambda_{m+1}I)^{k_{m+1}}v_{m+1}=0$$

이고, $i\leq m$에 대해

$$(L-\lambda_{m+1}I)^{k_{m+1}}v_i \in G_{\lambda_i}(L)$$

이다 ($G_{\lambda_i}(L)$은 $L$-invariant이므로 $(L-\lambda_{m+1}I)^{k_{m+1}}$에도 invariant). 따라서

$$(L-\lambda_{m+1}I)^{k_{m+1}}v_1 + \cdots + (L-\lambda_{m+1}I)^{k_{m+1}}v_m=0$$

귀납 가정에 의해 $(L-\lambda_{m+1}I)^{k_{m+1}}v_i=0$ for all $i\leq m$. 이는 $v_i\in G_{\lambda_i}(L)\cap G_{\lambda_{m+1}}(L)$이며, 1단계에서 보인 바에 따라 $v_i=0$ for all $i\leq m$. 따라서 $v_{m+1}=0$도 얻어진다.

**3단계: 차원 계산 및 직합분해**

$[따름정리 4](#cor4)로부터 각 $i$에 대해 적당한 $k_i$가 존재하여 $G_{\lambda_i}(L)=\ker(L-\lambda_i I)^{k_i}$이다. 이제 generalized eigenspace 위의 $(L-\lambda_i I)$의 작용을 이용하여 차원을 계산한다.

$G_{\lambda_i}(L)$의 basis를 선택하고 이를 다음과 같이 구성할 수 있다: 부분공간들의 filtration

$$0=\ker(L-\lambda_i I)^0 \subsetneq \ker(L-\lambda_i I)^1 \subsetneq \cdots \subsetneq \ker(L-\lambda_i I)^{k_i}=G_{\lambda_i}(L)$$

에 대해, 각 $j=1,\ldots,k_i$마다 $\ker(L-\lambda_i I)^j/\ker(L-\lambda_i I)^{j-1}$의 basis를 택하고 이를 lift한 벡터들로부터 Jordan chain을 구성한다. 이렇게 하면 $G_{\lambda_i}(L)$의 basis의 개수는 정확히 $\dim G_{\lambda_i}(L)$이다.

한편, $G_{\lambda_i}(L)$ 위에서만 보면 $(L-\lambda_i I)$는 nilpotent이므로, [명제 7](#prop7)에 의해 적당한 $N_i$에 대해 $(L-\lambda_i I)^{N_i}|_{G_{\lambda_i}(L)}=0$이다. 

우리는 $\dim G_{\lambda_i}(L)=m_i$임을 보여야 한다. $L$의 제한 $L|_{G_{\lambda_i}(L)}$을 생각하면, 이는 $G_{\lambda_i}(L)$ 위의 linear operator이며, $\lambda_i$만이 eigenvalue이다. 이 제한의 특성다항식을 $\chi_i(\mathbf{x})$라 하면,

$$p_L(\mathbf{x})=\chi_1(\mathbf{x})\chi_2(\mathbf{x})\cdots\chi_m(\mathbf{x})$$

이고 (2단계의 일차독립성과 직합), 각 $\chi_i(\mathbf{x})$의 차수는 $\dim G_{\lambda_i}(L)$이다. 

$\chi_i(\mathbf{x})$의 유일한 근이 $\lambda_i$이고 중복도가 $\dim G_{\lambda_i}(L)$이므로,

$$\chi_i(\mathbf{x})=(\mathbf{x}-\lambda_i)^{\dim G_{\lambda_i}(L)}$$

이다. 한편 $p_L(\mathbf{x})=\prod_{i=1}^m (\mathbf{x}-\lambda_i)^{m_i}$이므로, 다항식의 유일 인수분해에 의해

$$\dim G_{\lambda_i}(L)=m_i$$

따라서 

$$\sum_{i=1}^m \dim G_{\lambda_i}(L)=\sum_{i=1}^m m_i=\dim V$$

이고, 2단계의 일차독립성과 함께 이는 직합분해

$$V=\bigoplus_{i=1}^m G_{\lambda_i}(L)$$

를 의미한다.

</details>

일차분해정리의 중요한 결과는 generalized eigenspace $G_\lambda(L)$ 위에서 $L-\lambda I$가 nilpotent operator가 된다는 것이다.

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> Linear operator $N:V\rightarrow V$이 *nilpotent<sub>멱영</sub>*이라는 것은 적당한 양의 정수 $k$에 대하여 $N^k=0$인 것이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> 일차분해정리의 상황에서, 각 $G_{\lambda_i}(L)$ 위에서 $L-\lambda_i I$는 nilpotent operator이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[따름정리 4](#cor4)로부터 적당한 $k$에 대해 $G_{\lambda_i}(L)=\ker(L-\lambda_i I)^k$이므로, 임의의 $v\in G_{\lambda_i}(L)$에 대해 $(L-\lambda_i I)^k v=0$이다.

</details>

## 조르당 블록

이제 우리의 문제는 nilpotent operator의 "표준형"을 찾는 것으로 귀착된다. 

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> 크기 $k$의 *Jordan block* $J_k(\lambda)$는 다음과 같은 $k\times k$ 행렬이다:

$$J_k(\lambda)=\begin{pmatrix}\lambda&1&0&\cdots&0\\0&\lambda&1&\cdots&0\\\vdots&\vdots&\ddots&\ddots&\vdots\\0&0&\cdots&\lambda&1\\0&0&\cdots&0&\lambda\end{pmatrix}$$

즉, 대각선 위 원소들은 모두 $\lambda$이고, 대각선 바로 위(superdiagonal)의 원소들은 모두 $1$이며, 나머지는 모두 $0$이다.

</div>

<div class="example" markdown="1">

<ins id="ex9">**예시 9**</ins> 크기 $3$인 Jordan block $J_3(2)$는 다음과 같다:

$$J_3(2)=\begin{pmatrix}2&1&0\\0&2&1\\0&0&2\end{pmatrix}$$

</div>

Jordan block의 중요한 성질은 다음과 같다.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> $J_k(\lambda)-\lambda I_k$는 nilpotent이며, $(J_k(\lambda)-\lambda I_k)^k=0$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$N=J_k(\lambda)-\lambda I_k$라 하면,

$$N=\begin{pmatrix}0&1&0&\cdots&0\\0&0&1&\cdots&0\\\vdots&\vdots&\ddots&\ddots&\vdots\\0&0&\cdots&0&1\\0&0&\cdots&0&0\end{pmatrix}$$

이다. 직접 계산하면 $N^2$는 superdiagonal에서 한 칸 더 위의 대각선에만 $1$이 있고, 일반적으로 $N^i$는 $i$번째 위 대각선에만 $1$이 있다. 따라서 $N^k=0$이다.

</details>

## 조르당 표준형의 존재

이제 우리의 주요 정리를 서술할 수 있다.

<div class="proposition" markdown="1">

<ins id="thm11">**정리 11 (조르당 표준형)**</ins> 유한차원 벡터공간 $V$ 위에 정의된 임의의 linear operator $L:V\rightarrow V$에 대하여, $V$의 적당한 basis를 선택하면 $L$의 행렬 표현이 다음의 형태를 갖는다:

$$J=\begin{pmatrix}J_{k_1}(\lambda_1)&0&\cdots&0\\0&J_{k_2}(\lambda_2)&\cdots&0\\\vdots&\vdots&\ddots&\vdots\\0&0&\cdots&J_{k_m}(\lambda_m)\end{pmatrix}$$

여기서 각 $J_{k_i}(\lambda_i)$는 Jordan block이다. 이러한 형태의 행렬을 $L$의 *Jordan canonical form<sub>조르당 표준형</sub>*이라 한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[정리 5](#thm5)로부터 $V=\bigoplus_{i=1}^m G_{\lambda_i}(L)$이고, 각 $G_{\lambda_i}(L)$ 위에서 $L-\lambda_i I$는 nilpotent이다. 따라서 각 generalized eigenspace에서 적당한 basis를 택하면, 그 basis에 대한 $L$의 행렬 표현이 Jordan block들의 직합으로 나타난다는 것을 보이면 충분하다.

Nilpotent operator $N:W\rightarrow W$에 대한 Jordan form을 구성하자. [보조정리 1](#lem1)로부터

$$0=\ker N^0\subsetneq\ker N^1\subsetneq\cdots\subsetneq\ker N^{k-1}\subsetneq\ker N^k=W$$

인 filtration이 존재한다. 이제 다음과 같이 basis를 구성한다:

1. $\ker N^k/\ker N^{k-1}$의 basis를 택하고, 이를 $W$로 lift한 벡터들을 $v_1,\ldots, v_r$이라 하자.
2. 이 벡터들에 $N$을 반복적으로 적용하여 만든 벡터들

$$v_i, Nv_i, N^2v_i,\ldots, N^{k-1}v_i$$

을 생각하자. 이들은 Jordan block에 대응되는 basis를 이룬다.

3. 이 과정을 각 $\ker N^j/\ker N^{j-1}$에 대해 반복하면 $W$ 전체의 basis를 얻는다.

이렇게 구성된 basis에 대해 $N$의 행렬 표현은 Jordan block들의 직합이 된다. $L=N+\lambda I$이므로, $L$의 행렬 표현은 각 Jordan block $J_k(0)$을 $J_k(\lambda)$로 바꾼 형태가 된다.

</details>

<div class="example" markdown="1">

<ins id="ex12">**예시 12**</ins> [예시 2](#ex2)의 행렬

$$A=\begin{pmatrix}1&1&1\\0&1&1\\0&0&1\end{pmatrix}$$

의 Jordan canonical form을 구해보자. $A$의 유일한 eigenvalue는 $\lambda=1$이고,

$$A-I=\begin{pmatrix}0&1&1\\0&0&1\\0&0&0\end{pmatrix}$$

이다. 우리는 이미 다음을 알고 있다:

$$\ker(A-I)=\span\{(1,0,0)\},\quad \ker(A-I)^2=\span\{(1,0,0),(0,1,0)\},\quad \ker(A-I)^3=\mathbb{R}^3$$

$(A-I)^3=0$이지만 $(A-I)^2\neq 0$이므로, 가장 긴 Jordan chain의 길이는 $3$이다. $\ker(A-I)^3/\ker(A-I)^2$의 basis로 $(0,0,1)$의 coset을 택하면, Jordan chain

$$(0,0,1), (A-I)(0,0,1)=(0,1,0), (A-I)^2(0,0,1)=(1,0,0)$$

을 얻는다. 따라서 basis $\{(0,0,1),(0,1,0),(1,0,0)\}$에 대한 $A$의 행렬 표현은

$$J=\begin{pmatrix}1&1&0\\0&1&1\\0&0&1\end{pmatrix}=J_3(1)$$

이다. 실제로 변환 행렬을

$$P=\begin{pmatrix}0&0&1\\0&1&0\\1&0&0\end{pmatrix}$$

이라 하면, $P^{-1}AP=J$가 성립함을 확인할 수 있다.

</div>

조르당 표준형의 유일성은 Jordan block들의 크기가 $\dim\ker N^k-\dim\ker N^{k-1}$에 의해 결정된다는 사실로부터 따라온다. 이는 basis의 선택과 무관하므로, Jordan canonical form은 Jordan block들의 순서를 제외하고는 유일하게 결정된다.

---

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.  
**[Lee]** 이인석, *선형대수와 군*, 서울대학교 출판문화원, 2005.

---
