---

title: "동형사상"
excerpt: "서로 동등한 벡터공간들"

categories: [Math / Basic Linear Algebra]
permalink: /ko/math/basic_linear_algebra/isomorphic_vector_spaces
sidebar: 
    nav: "basic_linear_algebra-ko"

header:
    overlay_image: /assets/images/Math/Basic_Linear_Algebra/Isomorphic_vector_spaces.png
    overlay_filter: 0.5

date: 2022-08-02
last_modified_at: 2022-08-01

weight: 10
---

수학에서 특정한 대상들을 정의한 후에는 보통 이들을 <em_ko>같은</em_ko> 것들끼리 묶어 분류하는 작업을 하게 된다. 예컨대 집합을 다룰 때는 크기가 같은 두 집합 $A,B$를 같은 것으로 취급하며, 이는 정의에 의하여 $A$와 $B$ 사이에 전단사함수가 존재한다는 것이다. 

물론 이를 그대로 벡터공간으로 가져올 수는 없다. 만일 집합으로서 같은 크기를 갖는 두 벡터공간을 같은 것으로 생각한다면, [\[집합론\] §자연수와 무한집합, ⁋따름정리 15](/ko/math/set_theory/natural_numbers#cor15)에 의하여 무한한 field $\mathbb{k}$ 위에서 정의된 유한차원 벡터공간들은 모두 같은 것으로 생각해야 한다. 또 일반적으로 함수는 벡터공간의 덧셈과 스칼라곱을 유지하지 않으므로 어쨌든 벡터공간을 다루기엔 부적절한 것은 분명하다.

## 동형인 벡터공간

따라서 우리는 다음과 같이 정의한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 두 $\mathbb{k}$-벡터공간 $V,W$와 linear map $L:V\rightarrow W$가 주어졌다 하자. 이 때 $L$이 *isomorphism<sub>동형사상</sub>*이라는 것은 또 다른 linear map $L':W\rightarrow V$가 존재하여 $L\circ L'=\id_W$이고 $L'\circ L=\id_V$인 것이다. 이렇게 $V$와 $W$ 사이의 isomorphism이 존재할 경우, $V,W$가 *isomorphic<sub>동형</sub>*하다 하고 이를 $V\cong W$로 나타낸다. 

</div>

정의에 의해 임의의 isomorphism은 두 집합 $V,W$ 사이의 전단사함수이다. 뿐만 아니라, 다음 보조정리에 의하여 그 역 또한 성립한다. 

<div class="proposition" markdown="1">

<ins id="lem2">**보조정리 2**</ins> 두 $\mathbb{k}$-벡터공간 $V$, $W$에 대하여 $L:V\rightarrow W$가 isomorphism이라 하자. 그럼 $L$의 역함수 $L^{-1}$이 존재하며, $L^{-1}$은 linear이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$L^{-1}$이 존재한다는 것은 집합론에서의 결과이며, 이 때 $L\circ L^{-1}=\id_W$이고 $L^{-1}\circ L=\id_V$이다. 

따라서 $L^{-1}$이 linear임만 보이면 충분하다. 우선 임의의 $\alpha\in\mathbb{k}$, $w\in W$에 대하여, $L^{-1}(\alpha w)=\alpha L^{-1}(w)$임을 보여야 한다. 임의의 $w\in W$에 대하여 $L(v)=w$이도록 하는 $v\in V$가 유일하게 존재하고, 이 때 $L(\alpha v)=\alpha L(v)=\alpha w$이다. 이제

$$L^{-1}(\alpha w)=L^{-1}(L(\alpha v))=\alpha v=\alpha L^{-1}(w).$$

이와 비슷하게 $L^{-1}(w_1+w_2)=L^{-1}(w_1)+L^{-1}(w_2)$ 또한 보일 수 있다. 

</details>

다음 명제는 [\[집합론\] §기수, ⁋정의 1](/ko/math/set_theory/cardinals#def1) 이후에 간략하게 언급한 것과 동일한 집합론적 문제가 있다. 즉, <phrase>모든 $\mathbb{k}$-벡터공간들의 모임</phrase>이 실제로 집합이 되는지가 불확실하지만 이는 더 이상 부연설명 없이 넘어가기로 한다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> [정의 1](#def1)의 관계 $\cong$는 동치관계이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

관계 $\cong$이 reflexive, symmetric, transitive함을 보여야 한다.

1. 우선 임의의 $\mathbb{k}$-벡터공간 $V$에 대하여 $V\cong V$임은 자명하다. $\id_V:V\rightarrow V$가 $V$에서 $V$로의 isomorphism이 되기 때문이다.
2. 앞선 [보조정리 2](#lem2)에 의해 $\cong$가 symmetric이라는 것이 자명하다.    
3. 마지막으로 $U\cong V$, $V\cong W$라 하자. 그럼 두 isomorphism $L_1:U\rightarrow V$, $L_2: V\rightarrow W$가 존재하여 

</details>

위 명제는 자명해보이지만, 모든 유한차원 $\mathbb{k}$-벡터공간을 분류하는 작업 중 덜 자명한 부분을 증명해준다.

<div class="proposition" markdown="1">

<ins id="cor4">**따름정리 4**</ins> 두 $n$차원 $\mathbb{k}$-벡터공간은 항상 isomorphic하다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[§선형사상, ⁋에시 14](/ko/math/basic_linear_algebra/linear_map#ex14)는 임의의 $n$차원 $\mathbb{k}$-벡터공간 $V$가 $V\cong \mathbb{k}^n$을 만족한다는 뜻이다. 또 다른 $n$차원 $\mathbb{k}$-벡터공간 $W$에 대하여도 $W\cong \mathbb{k}^n$이므로, $\cong$가 동치관계라는 것으로부터 $V\cong W$임을 안다.

</details>

물론 이 역 또한 성립하며, 따라서 유한차원 벡터공간의 구조를 결정하는 유일한 불변량은 벡터공간의 차원임을 알 수 있다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> 두 isomorphic한 $\mathbb{k}$-벡터공간 $V,W$와 isomorphism $L:V\rightarrow W$가 주어졌다 하자. 만약 $\mathcal{B}$가 $V$의 basis라면, $L(\mathcal{B})$도 $V$의 basis가 된다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[§선형사상, ⁋따름정리 9](/ko/math/basic_linear_algebra/linear_map#cor9).

</details>

## Rank-nullity theorem

한편, 주어진 linear map $L$에 대하여 $\ker L$과 $\im L$들은 각각 $L$이 단사함수, 전사함수로부터 얼마나 떨어져있는지를 측정해주는 공간이었다. 위에서 벡터공간을 결정짓는 유일한 불변량이 차원 뿐임을 살펴보았으므로 $\ker L$과 $\im L$을 모두 보는 대신, 이들의 차원만 봐도 충분하다.

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> 두 $\mathbb{k}$-벡터공간 $V,W$와 linear map $L:V\rightarrow W$이 주어졌다 하자. 그럼 

1. $\dim\ker L$을 $L$의 *nullity*라 하고, $\nullity L$로 표기한다.
2. $\dim\im L$을 $L$의 *rank*라 하고, $\rank L$로 표기한다.

</div>

다음 두 명제들은 새로 번호를 붙이기도 아깝다.

1. $L$이 단사인 것은 $\nullity L=0$인 것과 동치이다.
2. $L$이 전사인 것은 $\rank L=\dim W$인 것과 동치이다.

뿐만 아니라, 다음의 정리가 성립한다.

<div class="proposition" markdown="1">

<ins id="thm7">**정리 7 (Rank-nullity theorem)**</ins> 두 $\mathbb{k}$-벡터공간 $V,W$와 linear map $L:V\rightarrow W$이 주어졌다 하자. 그럼 다음의 식 

$$\rank L+\nullity L=\dim V$$

이 항상 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

편의를 위해 $\dim V=n$, $\nullity L=k$라 적자. 다음 두 경우는 자명하다.

1. 만일 $n=k$라면, $\ker L$은 $V$와 같은 차원을 가지는 부분공간이므로 $\ker L=V$가 성립한다. 따라서 $L=0$이고, $\im L=0$이므로 $\rank L=0$이 되어 정리가 성립한다. 
2. 이와 비슷하게 만일 $k=0$이라면 $\ker L=0$이므로 $L$은 단사다. 따라서 $L$의 공역을 $W$에서 $\im L$로 제한한다면 $L$은 $V$와 $\im L$ 사이의 전단사인 linear map이 된다. 따라서 $\dim V=\dim\im L=\rank L$이 된다.

이제 $0 < k < n$인 경우만 보이면 충분하다. $\left\\{x_1,x_2,\ldots,x_k\right\\}$가 $\ker L$의 basis라 하자. 이 집합은 $V$의 일차독립인 부분집합이므로, 이를 확장하여 $V$의 basis $\left\\{x_1,x_2,\ldots,x_k,x_{k+1},\ldots,x_n\right\\}$을 만들 수 있다. 그럼 집합 $\left\\{L(x_{k+1}),L(x_{k+2}),\ldots,L(x_n)\right\\}$이 $\im L$의 basis가 된다는 것을 다음과 같이 보일 수 있다.

우선 이 집합은 일차독립인데, 만일 

$$\alpha_{k+1}L(x_{k+1})+\alpha_{k+2}L(x_{k+2})+\cdots+\alpha_nL(x_n)=0$$

이 성립한다면 linearity에 의해 $L(\sum_{i=k+1}^n \alpha_i x_i)=0$이므로 $\sum_{i=k+1}^n\alpha_ix_i\in\ker L$이고, 따라서 어떤 $\alpha_1$, $\alpha_2$, $\ldots$, $\alpha_k$에 대하여

$$\sum_{i=k+1}^n\alpha_ix_i=\alpha_1x_1+\alpha_2x_2+\cdots+\alpha_kx_k$$

혹은

$$\alpha_1x_1+\alpha_2x_2+\cdots+\alpha_kx_k-\alpha_{k+1}x_{k+1}-\cdots-\alpha_nx_n=0$$

가 성립한다. 이제 $\left\\{x_1,x_2,\ldots,x_k,x_{k+1},\ldots,x_n\right\\}$가 일차독립이므로 $\alpha_1=\alpha_2=\cdots=\alpha_n=0$이어야 하고, 특히 $\alpha_{k+1}=\alpha_{k+2}=\cdots=\alpha_n=0$이 된다.

또, 이 집합은 $\im L$을 span한다. 임의의 $w\in \im L$이 주어졌다고 하자. 그럼 $L(v)=w$인 $v\in V$가 존재한다. $v=\sum_{i=1}^n \alpha_ix_i$라 하면, 

$$u=L\left(\sum_{i=1}^n\alpha_ix_i\right)=L\left(\sum_{i=1}^k\alpha_ix_i\right)+L\left(\sum_{i=k+1}^n\alpha_i x_i\right)=\sum_{i=k+1}^n\alpha_i L(x_i)$$

가 성립하기 때문이다.

이상에서 $\rank L=\dim\im L=n-k=\dim V-\nullity L$이므로, 정리의 식이 성립한다.

</details>

---

**참고문헌**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.

---