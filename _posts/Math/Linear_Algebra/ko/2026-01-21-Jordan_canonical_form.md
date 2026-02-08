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

우리의 핵심 관찰은, 고유공간 $E_\lambda(A)$는 그 차원이 부족하지만, [보조정리 1](#lem1)을 $L=A-\lambda I$에 사용하여 이 공간을 늘려가다 보면 "맞는 차원"을 얻게 된다는 것이다. 

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> 다음의 행렬

$$A=\begin{pmatrix}1&1&1\\0&1&1\\0&0&1\end{pmatrix}$$

을 생각하자. 우리는 앞선 글에서 이 행렬의 특성다항식은 $(\x-1)^3=0$이지만 (즉 유일한 고유값 $1$의 대수적 중복도가 $3$이지만) 이에 해당하는 고유공간 $E_1(A)$는 벡터 $(1,0,0)$으로 생성되는 $1$차원 공간임을 보았다. 

이제 linear operator

$$A-1I=\begin{pmatrix}0&1&1\\0&0&1\\0&0&0\end{pmatrix}$$

에 위의 보조정리를 적용해보자. 언급한 것과 같이 

$$\ker (A-I)=\span \{(1,0,0)\}$$

이다. 그런데 높은 차수의 계산을 수행해보면,

$$(A-I)^2=\begin{pmatrix}0&0&1\\0&0&0\\0&0&0\end{pmatrix}$$

이므로

$$\ker(A-I)^2=\span \{(1,0,0), (0,1,0)\}$$

그리고

$$(A-I)^3=\begin{pmatrix}0&0&0\\0&0&0\\0&0&0\end{pmatrix}$$

이므로

$$\ker (A-I)^3=\span \{(1,0,0), (0,1,0), (0,0,1)\}$$

임을 안다. 

</div>

직관이라 이름붙이기는 다소 거창하지만, 적어도 이 예시의 경우에서는 앞서 말한 관찰이 잘 성립한다는 것을 확인할 수 있다. 이제 본격적인 이야기를 위해 다음 정의를 도입하자. 

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 유한차원 벡터공간 $V$ 위에 정의된 linear operator $A$와 $A$의 한 eigenvalue $\lambda$에 대하여, $A$의 $\lambda$에 대한 *generalized eigenspace*를 다음의 식

$$G_\lambda(A)=\left\{v\in V\mid (A-\lambda I)^kv=0\text{ for some $k\geq 0$}\right\}$$

으로 정의한다. 

</div>

그럼 우리는 [보조정리 1](#lem1)로부터 다음을 얻는다.

<div class="proposition" markdown="1">

<ins id="cor4">**따름정리 4**</ins> 유한차원 벡터공간 $V$ 위에 정의된 linear operator $A:V\rightarrow V$과 그 eigenvalue $\lambda$에 대하여, 적당한 양의 정수 $k$가 존재하여 $G_\lambda(A)=\ker(A-\lambda I)^k$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[보조정리 1](#lem1)을 linear operator $A-\lambda I$에 적용하면, 

$$\ker(A-\lambda I)^k=\ker(A-\lambda I)^{k+1}=\cdots$$

를 만족하는 $k$가 존재한다. 한편, $v\in G_\lambda(A)$가 주어질 때마다, 정의에 의하여 다음의 식

$$(A-\lambda I)^lv=0$$

을 만족하는 $l$이 존재한다. 그런데 $k'=\max (k,l)$로 잡으면 $k'\geq l$인 것으로부터

$$(A-\lambda I)^{k'}v =0$$

임을 안다. 즉 $v\in\ker (A-\lambda I)^{k'}$이다. 그런데 $k$의 정의에 의하여 $\ker(A-\lambda I)^k=\ker(A-\lambda I)^{k'}$이고 이로부터 $v\in \ker (A-\lambda I)^k$이다. ($k'$는 $v$에 의존하지만, $k$는 그렇지 않다.) 포함관계 $\ker (A-\lambda I)^k\subset G_\lambda(A)$은 자명하므로 원하는 결과를 얻는다. 

</details>

직관적으로 generalized eigenspace들은 진짜 고유벡터들 뿐만 아니라, linear operator $(A-\lambda I)$를 거듭해서 적용했을 때 결국 $0$이 되는 벡터들을 포함하는 공간이다. 

## 일차분해정리

본격적인 결과를 소개하기 전에 [§고유공간분해, ⁋명제 11](/ko/math/linear_algebra/eigenspace_decomposition#prop11)의 증명을 간단히 요약해보자. $A$의 diagonalizability를 보이기 위해, 우리는 고정된 고유값 $\lambda$에 대하여 다음 식

$$\ker(A-\lambda I)=\ker(A-\lambda I)^2$$

이 성립하는 것을 가정하고, 그럼 [§고유공간분해, ⁋보조정리 10](/ko/math/linear_algebra/eigenspace_decomposition#lem10)에 의하여 

$$\ker (A-\lambda I)\cap \im (A-\lambda I)=\{0\}$$

이므로 반드시 $V=\ker (A-\lambda I)\oplus \im(A-\lambda I)$ 꼴로 나타낼 수 있다는 것을 보았다. 그럼 $\im (A-\lambda I)$가 $A$-invariant가 되어 $A$를 이 위의 linear operator로 볼 수 있고 그 때 ([§고유공간분해, ⁋명제 4](/ko/math/linear_algebra/eigenspace_decomposition#prop4)에 의해 $E_\lambda(A)\cap E_\mu(A)=\\{0\\}$이므로) 고유값--고유벡터가 맞아떨어지므로 이를 귀납적으로 반복하여 고유공간분해를 얻는 것이 증명의 요지였다. 

이제 위의 관점에서 [정의 3](#def3)을 어떻게 활용할지를 생각해보면, 우리는 임의의 linear operator $L$과

$$\ker L^k=\ker L^{k+1}=\cdots$$

을 만족하는 $k$에 대하여 다음 식

$$\ker L^k=\ker L^{2k}$$

이 성립하는 것을 알고있다. 바꿔말하면, $L^k:V \rightarrow V$에 대하여 [§고유공간분해, ⁋보조정리 10](/ko/math/linear_algebra/eigenspace_decomposition#lem10)의 전제가 만족되는 것이다. 이를 $L=A-\lambda I$에 적용하여 귀납법의 첫 단계----즉, direct sum decomposition $V=\ker (A-\lambda I)^k \oplus \im (A-\lambda I)^k$를 얻을 수 있다. [§고유공간분해, ⁋명제 11](/ko/math/linear_algebra/eigenspace_decomposition#prop11)의 증명에서와 마찬가지로 이를

$$V=G_\lambda(A)\oplus W_\lambda(A)$$

으로 쓰자. 그럼 $W_\lambda(A)$가 $A$-invariant이고 따라서 $A\vert_{W_\lambda(A)}$가 linear operator $A\vert_{W_\lambda(A)}:W_\lambda(A)\rightarrow W_\lambda(A)$을 정의하는 것 까지는 자명하다. 다소 신경써야 할 부분은 다음 보조정리이다. 

<div class="proposition" markdown="1">

<ins id="lem5">**보조정리 5**</ins> 유한차원 벡터공간 $V$ 위에 정의된 linear operator $A:V\rightarrow V$와 $A$의 서로 다른 두 eigenvalue $\lambda, \mu$에 대하여, $G_\lambda(A)\cap G_\mu(A)=\\{0\\}$이 성립한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

먼저 $v\in G_{\lambda_i}(L)\cap G_{\lambda_j}(L)$이고 $v\neq 0$이라 가정하자. [따름정리 4](#cor4)로부터 다음 두 식

$$G_{\lambda_i}(L)=\ker(L-\lambda_i I)^{k_i},\qquad G_{\lambda_j}(L)=\ker(L-\lambda_j I)^{k_j}$$

을 만족하는 정수 $k_i, k_j$가 존재한다. 

이제 정수 $p_i$를 $(L-\lambda_iI)^kv=0$을 만족하는 $k$ 중 가장 작은 것이라 하자. 그럼 다음의 식

$$(L-\lambda_iI)^{p_i}v=0\implies L(L-\lambda_iI)^{p_i-1}v=\lambda_i(L-\lambda_iI)^{p_i-1}v$$

으로부터 $w=(L-\lambda_iI)^{p_i-1}v\neq 0$는 $L$의 고유값 $\lambda_i$에 해당하는 고유벡터임을 안다. 한편 $v\in G_{\lambda_j}(L)$이므로 $(L-\lambda_j I)^{k_j}v=0$이고, $(L-\lambda_i I)$와 $(L-\lambda_j I)$는 commute하므로

$$(L-\lambda_j I)^{k_j}w=(L-\lambda_j I)^{k_j}(L-\lambda_i I)^{p_i}v=(L-\lambda_i I)^{p_i}(L-\lambda_j I)^{k_j}v=0$$

이다. 즉 $w\in G_{\lambda_j}(L)$이므로, $w$는 고유값 $\lambda_i$에 해당하는 고유벡터인 동시에 $G_{\lambda_j}(L)$에 속하는 벡터가 된다. 

이것이 불가능함을 보이자. 우선 $w\in G_{\lambda_j}(L)$이므로, 그 정의에 의해 $(L-\lambda_jI)^kw=0$이도록 하는 정수 $k$가 존재한다. (가령, $k=k_j$가 이를 만족하는 것을 위에서 보았다.) 이러한 조건을 만족하는 정수 $k$ 중 가장 작은 것을 $p_j$라 하면, 최소성에 의해 $w'=(L-\lambda_jI)^{p_j-1}w\neq 0$이고

$$0=(L-\lambda_jI)^{p_j}w=(L-\lambda_jI)w'$$

이므로 $w'$는 고유값 $\lambda_j$에 해당하는 고유벡터이다. 한편 $w$가 고유값 $\lambda_i$에 해당하는 고유벡터이므로, 다음 식

$$Lw'=L(L-\lambda_jI)^{p_j-1}w=(L-\lambda_jI)^{p_j-1}Lw=(L-\lambda_jI)^{p_j-1}\lambda_iw=\lambda_i (L-\lambda_jI)^{p_j-1}w_\lambda w'$$

으로부터 $w'$ 또한 $\lambda_i$에 해당하는 고유벡터임을 안다. 이는 [§고유공간분해, ⁋명제 4](/ko/math/linear_algebra/eigenspace_decomposition#prop4)에 모순이므로 귀류법에 의하여 $i\neq j$일 때 $G_{\lambda_i}(L)\cap G_{\lambda_j}(L)=\\{0\\}$임을 안다. 

</details>

그러므로 앞선 분해

$$V=G_\lambda(A)\oplus W_\lambda(A)$$

와 linear operator를 제한한 $A\vert_{W_\lambda(A)}: W_\lambda(A)\rightarrow W_\lambda(A)$를 생각하면 이 linear operator의 eigenvalue는 정확하게 $A$의 eigenvalue 중 $\lambda$가 아닌 것들에 해당하는 것들이다. 즉 귀납법이 잘 작동하고, 따라서 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="thm6">**정리 6 (제1분해정리)**</ins> 유한차원 벡터공간 $V$ 위에 정의된 linear operator $A:V\rightarrow V$에 대하여, $A$의 모든 eigenvalue들을 $\lambda_1,\ldots,\lambda_m$이라 하자. 그럼 다음의 direct sum decomposition

$$V=G_{\lambda_1}(A)\oplus G_{\lambda_2}(A)\oplus\cdots\oplus G_{\lambda_m}(A)$$

가 성립한다. 

</div>

## 조르당 표준형

이제 각각의 $\lambda$에 대하여, 우리는 $G_\lambda(A)$의 차원을 계산해줘야 한다. Linear operator $A:V \rightarrow V$가 주어졌다 하고, 그 특성다항식

$$p_A(\x)=\prod_{\lambda\in\sigma(A)}(\x-\lambda)^{d_\lambda}$$

가 주어졌다 하자. 여기서 $d_\lambda$는 $\lambda$의 algebraic multiplicity이고, $\sum d_\lambda$는 $p_A$의 차수인 $\dim V$와 같다. 그런데 우리는 위의 분해로부터 다음의 식

$$p_A(\x)=\prod_{\lambda\in\sigma(A)} p_{G_\lambda(A)}(\x)$$

을 얻는다. ([§행렬식의 존재성과 유일성, ⁋정리 11](/ko/math/linear_algebra/existence_and_uniqueness_of_determinant#cor11)) 우리는 [보조정리 5](#lem5)에서 $G_\lambda(A)$로 $A$를 제한했을 때 고유값은 오직 $\lambda$ 뿐인 것을 확인하였으므로 각각의 $p_{G_\lambda(A)}(\x)$는 오직 $\x-\lambda$만을 인수로 가져야한다. 따라서, 위의 두 식이 같기 위해서는 $p_{G_\lambda(A)}(\x)$가 정확히 $d_\lambda$차 다항식 

$$p_{G_\lambda(A)}(\x)=(\x-\lambda)^{d_\lambda}$$

이어야 하는 것을 알고 이로부터 $\dim G_\lambda(A)=d_\lambda$임을 안다. 

따라서, 우리는 지금까지 임의의 linear operator $A:V \rightarrow V$에 대하여 다음의 분해

$$V=\bigoplus_{\lambda\in\sigma(A)}G_\lambda(A)$$

가 성립하며, 뿐만 아니라 각각의 $\lambda$에 대하여 $\dim G_\lambda(A)$가 우리가 기대하는 차원, 즉 $A$의 특성다항식에서 $\lambda$의 대수적 중복도와 맞아떨어지는 것을 확인한 것이다. 그렇다면 우리에게 남아있는 일은 $V$의 적당한 basis를 찾아 [§고유공간분해, ⁋명제 7](/ko/math/linear_algebra/eigenspace_decomposition#prop7)와 유사한 형태로 임의의 행렬을 표현하는 일이다. 

여기에서 유용하게 쓰이는 사실은 linear operator $A:V\rightarrow V$의 임의의 고유값 $\lambda\in \sigma(A)$에 대하여, generalized eigenspace $G_\lambda(A)$로 제한하였을 때 linear operator

$$N_\lambda:=(A-\lambda I)\vert_{G_\lambda(A)}: G_\lambda(A)\rightarrow G_\lambda(A)$$

가 nilpotent operator라는 사실이다. 

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> 벡터공간 $V$ 위에 정의된 linear operator $N:V \rightarrow V$가 *nilpotent<sub>멱영</sub>*라는 것은 적당한 정수 $k$가 존재하여 $N^k\equiv 0$을 만족하는 것이다. 이러한 $k$ 중 가장 작은 것을 $N$의 *(nilpotency) index<sub>멱영지수</sub>*라 부른다. 

</div>

즉, 만일 우리가 임의의 nilpotent operator의 표준형을 구할 수 있다면 우리는 전체 행렬 $A$ 또한 표준형으로 나타낼 수 있게 된다. 

Index $k$의 nilpotent operator $N: V\rightarrow V$가 주어졌다 하자. 그럼 적당한 $v\in V$가 존재하여 $N^{k-1}v\neq 0$이다. 이 벡터를 이용하면 우리는 [보조정리 1](#lem1)에서 포함관계가 strict하다는 것도 보일 수 있는데, $N^{k-i}v\in \ker N^i$이지만 $N^{k-1}v\not\in\ker N^{i-1}$이기 때문이다. 바꾸어 말하자면 $v, Nv, \ldots, N^{k-1}v$는 모두 다른 원소들이다. 더 일반적으로 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="lem8">**보조정리 8**</ins> 벡터공간 $V$ 위에 정의된 linear operator $N: V\rightarrow V$와 벡터 $v$가 $N^kv=0$과 $N^{k-1}v\neq 0$을 만족한다 하자. 그럼 다음의 벡터들

$$v, \quad Nv, \quad\cdots,\quad N^{k-1}v$$

은 linearly independent이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

다음 식

$$a_0v+a_1 Nv+\cdots a_{k-1}N^{k-1}v=0$$

이 성립한다 가정하자. 양 변에 $N^{k-1}$을 취하면 $N^k=0$인 것으로부터 $a_0N^{k-1}v=0$임을 안다. 그런데 가정에 의하여 $N^{k-1}v\neq 0$이므로 반드시 $a_0=0$이므로 

$$a_1Nv+\cdots a_{k-1}N^{k-1}v=0$$

이다. 다시 양 변에 $N^{k-2}$을 취하면 $a_1=0$을 얻고, 이를 반복하면 원하는 결과를 얻는다. 

</details>

즉 $k$개의 벡터들 $v, Nv, \ldots, N^{k-1}v$은 $V$의 $k$차원 부분공간 (이러한 꼴의 부분공간을 $v$가 정의하는 *cyclic subspace*라 부른다.) $U$의 basis가 된다. 이 특정한 basis가 흥미로운 이유는, $N\vert_U$를 이 basis $N^{k-1}v, \ldots, Nv, v$에 대하여 행렬로 표현해보면

$$\begin{pmatrix}0&1&0&\cdots&0\\ 0&0&1&\cdots&0\\\vdots&\vdots&\vdots&\ddots&\vdots\\ 0&0&0&\cdots&1\\ 0&0&0&\cdots&0\end{pmatrix}\tag{1}$$

이 되기 때문이다. 이를 nilpotent operator의 표준형으로 삼는 것이 우리의 아이디어이다. 

즉, 임의의 벡터공간 $V$와 그 위에 정의된 nilpotent operator $N$이 주어졌을 때, 이를 cyclic subspace들의 direct sum으로 나타내는 것이 우리에게 주어진 일이다. 

<div class="proposition" markdown="1">

<ins id="thm9">**정리 9 (Cyclic decomposition theorem 혹은, 제2분해정리)**</ins> 임의의 벡터공간 $V$와 그 위에 정의된 nilpotent operator $N: V\rightarrow V$에 대하여, cyclic subspace로의 decomposition

$$V=U_1\oplus \cdots\oplus U_e$$

이 존재한다. 

</div>

이 정리에 대한 증명은 다음과 같다. $N$의 nilpotency index를 $k_1$이라 하고 $N^{k_1}v_1=0$이지만 $N^{k_1-1}v_1\neq 0$인 벡터 $v_1$를 택하자. 이 벡터가 정의하는 cyclic subspace

$$U_1=\span (N^{k_1-1}v_1, \cdots, Nv_1, v_1)$$

을 생각하자. 만일 $U_1=V$라면 더 이상 증명할 것이 없다. 그렇지 않다면 우리는 $V=U_1\oplus W_1$이도록 하는 *$T$-invariant* subspace $W_1$을 찾는다. $N$이 $W_1$ 위에서도 nilpotent인 것은 자명하므로, $N\vert_{W_1}$의 nilpotency index $k_2$를 잡고, $N^{k_2}v_2=0$이지만 $N^{k_2-1}v_2\neq 0$이도록 하는 $v_2$를 잡을 수 있다. 이제 다시 다음의 cyclic subspace

$$U_2=\span (N^{k-2-1}v_2, \cdots, Nv_2, v_2)$$

를 얻고, 다시 $U_2$의 $T$-invariant complement를 얻는 과정을 반복해나가다 보면 원하는 decomposition을 얻는다. 

이 증명에서 가장 핵심적인 부분은 $U$의 complement $W$를 $T$-invariant가 되도록 잡을 수 있다는 것이다. 

<div class="proposition" markdown="1">

<ins id="lem9">**보조정리 9**</ins> 임의의 벡터공간 $V$와 그 위에서 정의된 index $k$의 nilpotent operator $N$을 생각하고, $N^{k-1}v\neq 0$을 만족하는 벡터 $v$를 택하자. 그럼 $v$가 생성하는 cyclic subspace 

$$U=\span(v, Nv, \ldots, N^{k-1}v)$$

에 대하여, $V=U\oplus W$이도록 하는 $T$-invariant space $W$가 존재한다. 

</div>

이에 대한 증명은 $N$의 nilpotency index에 대한 귀납법을 쓰면 되지만, 증명이 다소 귀찮은 감이 있어 생략하기로 한다. 

어쨌든 이러한 과정을 거치고 나면 우리는 임의의 nilpotent operator $N$를 위의 식 (1) 형태의 direct sum (즉, 위의 행렬들이 대각성분에 있는 block diagonal matrix들)으로 나타낼 수 있음을 안다. $N$이 나오게 된 것은 generalized eigenspace $G_\lambda(A)$ 위에서의 nilpotent operator $A-\lambda I$ 때문이었으므로, 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="def10">**정의 10**</ins> 크기 $k$의 *Jordan block* $J_k(\lambda)$를 다음의 $k\times k$ 행렬

$$J_k(\lambda)=\begin{pmatrix}\lambda&1&0&\cdots&0\\0&\lambda&1&\cdots&0\\\vdots&\vdots&\ddots&\ddots&\vdots\\0&0&\cdots&\lambda&1\\0&0&\cdots&0&\lambda\end{pmatrix}$$

로 정의한다. 

</div>

그럼 [정리 6](#thm6)과 [정리 8](#thm8)을 합치면 다음의 정리를 얻는다. 

<div class="proposition" markdown="1">

<ins id="thm11">**정리 11 (Jordan canonical form)**</ins> 유한차원 벡터공간 $V$ 위에 정의된 임의의 linear operator $A:V\rightarrow V$에 대하여, $V$의 적당한 basis를 선택하면 $A$의 행렬 표현이 다음의 형태를 갖는다:

$$J=\begin{pmatrix}J_{k_1}(\lambda_1)&0&\cdots&0\\0&J_{k_2}(\lambda_2)&\cdots&0\\\vdots&\vdots&\ddots&\vdots\\0&0&\cdots&J_{k_m}(\lambda_m)\end{pmatrix}$$

여기서 각 $J_{k_i}(\lambda_i)$는 Jordan block이다. 이러한 형태의 행렬을 $A$의 *Jordan canonical form<sub>조르당 표준형</sub>*이라 한다.

</div>

<div class="example" markdown="1">

<ins id="ex12">**예시 12**</ins> [예시 2](#ex2)의 행렬

$$A=\begin{pmatrix}1&1&1\\0&1&1\\0&0&1\end{pmatrix}$$

의 Jordan canonical form을 구해보자. $A$의 유일한 eigenvalue는 $\lambda=1$이고,

$$A-I=\begin{pmatrix}0&1&1\\0&0&1\\0&0&0\end{pmatrix}$$

이며

$$\ker(A-I)=\span\{(1,0,0)\},\quad \ker(A-I)^2=\span\{(1,0,0),(0,1,0)\},\quad \ker(A-I)^3=\mathbb{R}^3$$

임을 이미 계산하였다. 즉 $A$에 [정리 6](#thm6)을 적용한 것은 그냥 $V=G_1(A)$이 된다. 

이제 $G_1(A)$ 위에서 [정리 8](#thm8)을 적용해야 한다. 앞서 살펴본 것과 같이 $(A-I)^3=0$이지만 $(A-I)^2\neq 0$이며, 실제로 $v=(0,0,1)$이 $(A-I)^2 v\neq 0$을 만족하는 것을 안다. 그럼 

$$v=(0,0,1), (A-I)v=(1,1,0), (A-I)^2v=(1,0,0)$$

이며 이들이 $G_1(A)$를 생성한다. 

</div>

조르당 표준형의 유일성은 Jordan block들의 크기가 $\dim\ker N^k-\dim\ker N^{k-1}$에 의해 결정된다는 사실로부터 따라온다. 이는 basis의 선택과 무관하므로, Jordan canonical form은 Jordan block들의 순서를 제외하고는 유일하게 결정된다.

---

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011. 
**[Lee]** 이인석, *선형대수와 군*, 서울대학교 출판문화원, 2005.

---

[^1]: $V_1$의 complement $W_1$을 $T$-invariant가 되도록 할 수 있다는 것이 이 증명에서 가장 비자명한 부분이며 이는 귀납법을 통해 직접 보여야 한다. 
