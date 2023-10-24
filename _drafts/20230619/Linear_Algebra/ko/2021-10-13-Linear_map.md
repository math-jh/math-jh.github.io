---

title: "선형사상"
excerpt: "선형사상의 정의와 예시"

categories: [Math / Linear Algebra]
permalink: /ko/math/linear_algebra/linear_map
sidebar: 
    nav: "linear_algebra-ko"

header:
    overlay_image: /assets/images/Math/Linear_Algebra/Linear_map.png
    overlay_filter: 0.5

date: 2021-10-13
last_modified_at: 2022-08-01

weight: 7

---

이번 글에서는 벡터공간들 간의 함수, 즉 *선형사상*을 정의한다.

## 선형사상

벡터공간은 기본적으로 집합이기 때문에 두 벡터공간 $V,W$ 사이의 함수가 집합들 간의 함수로서 존재한다. 그러나 벡터공간의 경우, 일반적인 집합과는 다르게 원소들 간의 덧셈과, $F$의 원소에 의한 스칼라곱이 정의되므로 우리는 벡터공간들 사이의 (집합으로서의) 함수들 가운데 이들 연산을 보존하는 함수들에만 관심이 있다.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 두 $F$-벡터공간 $V,W$가 주어졌다 하자. 함수 $L:V\rightarrow W$가 *linear map<sub>선형사상</sub>*이라는 것은, 

1. 임의의 $\alpha\in F$와 $v\in V$에 대해 $L(\alpha v)=\alpha L(v)$이고,
2. 임의의 $v_1,v_2\in V$에 대해 $L(v_1+v_2)=L(v_1)+L(v_2)$

가 모두 성립하는 것이다.

</div>

다음 명제들은 거의 정의로부터 자명하다.

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> 두 $F$-벡터공간 $V,W$와 linear map $L:V\rightarrow W$에 대하여,

1. $L(0)=0$.
2. 임의의 $v\in V$에 대하여 $L(-v)=-L(v)$.
3. 임의의 $u,v\in V$에 대하여 $L(u-v)=L(u)-L(v)$.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Linear map은 스칼라곱을 보존하므로, 첫 번째와 두 번째 주장은 각각 [§벡터공간, ⁋명제 2](/ko/math/linear_algebra/vector_spaces#pp2), 그리고 [§벡터공간, ⁋따름정리 3](/ko/math/linear_algebra/vector_spaces#crl3)의 결과이다. 이제 linear map이 벡터의 덧셈을 보존하는 것과, 둘째 주장으로부터

$$L(u-v)=L\bigl(u+(-v)\bigr)=L(u)+L(-v)=L(u)+\bigl(-L(v)\bigr)=L(u)-L(v)$$

가 되어 셋째 주장 또한 성립한다.

</details>

<div class="proposition" markdown="1">

<ins id="pp3">**명제 3**</ins> 두 $F$-벡터공간 $V,W$와 linear map $L:V\rightarrow W$, 스칼라들 $\alpha_1,\ldots,\alpha_n$과 $V$의 벡터들 $v_1,\ldots, v_n$에 대하여

$$L\left(\sum_{i=1}^k\alpha_i v_i\right)=\sum_{i=1}^kL(\alpha_iv_i)$$

이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$k$에 대한 귀납법에 의하여 자명하다.

</details>

함수의 합성은 함수가 되듯이, linear map의 합성 또한 linear map이 된다. 뿐만 아니라, 나중에 확인하겠지만 linear map이 역함수를 갖는다면 역함수는 자동으로 linear map이 된다. 

<div class="proposition" markdown="1">

<ins id="pp4">**명제 4**</ins> 세 $F$-벡터공간 $U,V,W$와 linear map들 $L_1:U\rightarrow V$, $L_2:V\rightarrow W$에 대하여, $L_2\circ L_1:U\rightarrow W$는 linear이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $\alpha\in F$, $u\in U$에 대하여

$$(L_2\circ L_1)(\alpha u)=L_2(L_1(\alpha u))=L_2(\alpha L_1(u))=\alpha(L_2(L_1(u)))=\alpha(L_2\circ L_1)(u)$$

비슷하게, 벡터들 사이의 합에 대해서도 $(L_2\circ L_1)(u_1+u_2)=(L_2\circ L_1)(u_1)+(L_2\circ L_1)(u_2)$가 성립하는 것을 증명할 수 있다. 
</details>

## 선형사상의 kernel과 image

이제 다음을 정의하자.

<div class="definition" markdown="1">

<ins id="df5">**정의 5**</ins> 두 $F$-벡터공간 $V,W$와 linear map $L:V\rightarrow W$에 대하여,

1. $L(v_1)=L(v_2)$일 때마다 $v_1=v_2$라면, $L$이 *단사<sub>injective</sub>*라 힌다.
2. 임의의 $w\in W$에 대해 $L(v)=w$를 만족하는 $v\in L$이 존재한다면, $L$이 *전사<sub>surjective</sub>*라 한다. 

</div>

일반적으로 단사함수 혹은 전사함수를 다룰 때 사용할 수 있는 도구는 위의 정의가 거의 전부지만, 지금 상황과 같이 다루는 대상이 단순한 집합이 아니라 어떠한 연산이 주어진 경우, 대수적인 도구도 사용할 수 있다.

<div class="definition" markdown="1">

<ins id="df6">**정의 6**</ins> 두 $F$-벡터공간 $V,W$와 linear map $L:V\rightarrow W$에 대하여, $L$의 *kernel<sub>핵</sub>* $\ker L$은 다음의 식

$$\ker L=\{v\in V\mid L(v)=0\}$$

으로 정의되는 집합이다. 또, $L$의 *image<sub>상</sub>* $\im L$는 다음의 식

$$\im L=\{w\in W\mid L(v)=w\text{ for some $v\in V$}\}$$

으로 정의되는 집합이다.

</div>

어렵지 않게 다음을 확인할 수 있다.

<div class="proposition" markdown="1">

<ins id="pp7">**명제 7**</ins> 두 $F$-벡터공간 $V,W$와 linear map $L:V\rightarrow W$에 대하여, $\ker L\leq V$이고 $\im L\leq W$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $\ker L$은 $V$의 부분공간이다. 임의의 $\alpha\in F$, $v\in\ker L$에 대하여

$$L(\alpha v)=\alpha L(v)=\alpha\cdot 0=0$$

이고, 마찬가지로 임의의 $v_1$, $v_2\in \ker L$에 대하여 

$$L(v_1+v_2)=L(v_1)+L(v_2)=0+0=0$$

이므로 $\alpha v\in\ker L$, $v_1+v_2\in\ker L$이 성립하기 때문이다.

이와 비슷하게, $\im L$은 $W$의 부분공간이다. 임의의 $w,w_1,w_2\in W$와 $\alpha\in F$를 택해오면, 정의에 의해

$$L(v)=w,\quad L(v_1)=w_1,\quad L(v_2)=w_2$$

를 만족하는 $v,v_1,v_2\in V$가 존재하며 따라서

$$\alpha w=\alpha L(v)=L(\alpha v)\in\im L$$

그리고

$$w_1+w_2=L(v_1)+L(v_2)=L(v_1+v_2)\in \im L$$

이기 때문이다.

</details>

이제 이들 $\ker L$과 $\im L$을 통해 $L$이 injective인지, surjective인지를 확인할 수 있다.

<div class="proposition" markdown="1">

<ins id="pp8">**명제 8**</ins> 두 $F$-벡터공간 $V,W$와 linear map $L:V\rightarrow W$에 대하여, 

1. $L$이 단사인 것은 $\ker L=\\{0\\}$인 것과 동치이고,
2. $L$이 전사인 것은 $\im L=W$인 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

둘째 주장은 동어반복이다.

만약 $L$이 단사라면 $L(v)=0$을 만족하는 $v$는 유일해야 하고, [명제 2](#pp2)에 의해 $0$은 이 식을 만족하므로 $\ker L=\\{0\\}$이어야 한다. 따라서 첫째 주장 중에서도 다음의 명제

> $\ker L=\\{0\\}\implies\text{$L$ injective}$

만 보이면 충분하다. $L(v_1)=L(v_2)$인 $v_1,v_2\in V$가 주어졌다 가정하자. 그럼 다시 [명제 3](#pp3)에 의하여,

$$0=L(v_1)-L(v_2)=L(v_1-v_2)$$

이므로 $v_1-v_2\in\ker L$이다. $\ker L=\\{0\\}$이므로, $v_1-v_2=0$이고 따라서 $L$은 단사가 된다.

</details>

덜 엄밀하게 이야기하자면 $\ker L$이 작으면 작을수록 $L$은 단사함수에 가깝고, $\im L$이 크면 클수록 $L$은 전사함수에 가깝다.

<div class="proposition" markdown="1">

<ins id="crl9">**따름정리 9**</ins> 두 $F$-벡터공간 $V,W$와 linear map $L:V\rightarrow W$가 주어졌다 하자.

1. 만약 $L$이 단사라면, 임의의 일차독립인 부분집합 $S\subset V$에 대하여 $L(S)$ 또한 $W$에서 일차독립이다.
2. 만약 $L$이 전사라면, $\span S=V$를 만족하는 $S\subset V$에 대해, $L(S)$ 또한 $\span L(S)=W$를 만족한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

1. $L(S)$의 원소들 $L(x_1),\ldots, L(x_k)$들에 대하여, 만일

    $$\sum_{i=1}^k\alpha_i L(x_i)=0$$

    라면, [명제 3](#pp3)에 의해

    $$0=L\left(\sum_{i=1}^k\alpha_ix_i\right)$$

    이므로, 앞선 명제에 의해 $\sum\alpha_ix_i=0$이어야 한다. 이제, $S$는 일차독립인 부분집합이므로, $\alpha_i=0$이 모든 $i$에 대해 성립한다.

2. 임의의 $w\in W$가 주어졌다 하자. 그럼 $\im L=W$이므로, 적당한 $v\in V$가 존재하여 $L(v)=w$이다. 한편, $\span S=V$이므로 $v$를 $S$의 원소들의 일차결합

    $$v=\sum_{i=1}^n\alpha_ix_i$$
    
    으로 나타낼 수 있다. 양 변에 $L$을 취한 후 [명제 3](#pp3)을 적용하면
    
    $$w=L(v)=L\left(\sum_{i=1}^n\alpha_ix_i\right)=\sum_{i=1}^n\alpha_i L(x_i)$$
    
    가 성립한다. 즉 임의의 $w\in W$는 $L(S)$의 원소들의 일차결합으로 표현할 수 있다.
 
</details>

사실 위 따름정리의 두 주장은 각각 역 또한 성립하고, 그 증명도 어렵지 않지만 우리가 이들을 사용할 일은 없어서 남겨두었다.

## 선형사상의 예시들

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> 임의의 $F$-벡터공간 $V$와 $W$에 대하여, 다음의 식

$$L(v)=0\text{ for all $v\in V$}$$

으로 정의된 $L:V\rightarrow W$는 linear다. 이 경우, $\im L=\\{0\\}$이고 $\ker L=V$이다.

</div>

위의 예시에서 정의된 함수 자체를 $0$으로 표기하기도 한다. 이 표기는 덧셈에 대한 항등원 $0$과 혼동을 일으킬 수도 있지만, 이 함수는 <em_ko>실제로</em_ko> 적당한 벡터공간에서의 항등원이 된다. 이에 대한 증명은 어렵지 않지만 나중으로 미뤄둔다.

<div class="example" markdown="1">

<ins id="ex11">**예시 11**</ins> 임의의 $F$-벡터공간 $V$와, $W\leq V$가 주어졌다 하자. 다음의 식

$$\iota(w)=w\text{ for all $w\in W$}$$

으로 정의된 $\iota:W\rightarrow V$는 linear map이다. 이번에는 $\im\iota=W$이고, $\ker \iota=\\{0\\}$이다. 즉, $L$은 단사함수이다.

</div>

위의 예시에서 특별히 $W=V$인 경우 $L$은 항등함수 $\id_V$와 같게 된다. ([\[집합론\] §함수들 사이의 연산, ⁋예시 4](/ko/math/set_theory/operation_of_functions#ex4)) 

<div class="example" markdown="1">

<ins id="ex12">**예시 12**</ins> 임의의 $F$-벡터공간 $V$, $W$와, 그들의 곱 $V\times W$를 생각하자. 그럼 다음의 식

$$\pr_1((v,w))=v$$

으로 정의된 $\pr_1:V\times W\rightarrow V$는 linear map이 된다. $\im\pr_1=V$이고, 

$$\ker \pr_1=\{(0,w)\mid w\in W\}$$

임을 쉽게 확인할 수 있다. 물론, 비슷하게 $\pr_2:V\times W\rightarrow W$를 정의할 수도 있으며, $n$개의 순서쌍으로 이를 확장할 수도 있다. 특히, 유클리드 공간 $F^n$에 대하여, 

$$\pr_i((a_1,\ldots, a_n))=a_i$$

으로 정의된 $\pr_i:F^n\rightarrow F$도 linear다.

</div>

$\pr$은 projection의 머릿글자로, 간단히 $p$, 혹은 $\pi$와 같이 쓰기도 한다.

<div class="example" markdown="1">

<ins id="ex13">**예시 13**</ins> $F[\x]$ 위에 정의된 함수 $D:F[\x]\rightarrow F[\x]$를 다음의 식

$$D\left(\sum_{i=0}^\infty a_i\x^i\right)=\sum_{i=1}^\infty ia_i\x^{i-1}$$

으로 정의하자. (여기서 $(a_i)$는 finitely supported이다.) 그럼 $D$는 linear이고, $\im D= F[\x]$이다. 또, $\ker D$는 모든 constant polynomial들의 모임이다. 

</div>

마지막 예시는 단순한 예시일 뿐만 아니라, 다음 글에서 살펴볼 isomorphism의 원형이라 생각할 수 있다.

<div class="example" markdown="1">

<ins id="ex14">**예시 14**</ins> 임의의 $n$차원 $F$-벡터공간 $V$가 주어졌다 하고, $\mathcal{B}=\\{x_1,\ldots, x_n\\}$이 $V$의 basis라 하자. 즉 임의의 $v\in V$에 대하여, 

$$v=\sum_{i=1}^n v_i x_i$$

이도록 하는 스칼라들 $v_1,\ldots, v_n$이 항상 존재하며, 유일하게 결정된다. 따라서, 함수 $L:V\rightarrow F^n$을 식 $v\mapsto (v_1,v_2,\ldots, v_n)\in F^n$으로 정의할 수 있다.

그럼 $L$은 linear다. 임의의 $v,w\in V$에 대하여,

$$v=\sum_{i=1}^n v_i x_i,\quad w=\sum_{i=1}^n w_i x_i$$

이라 하면, 임의의 $\alpha\in F$에 대하여

$$\alpha L(v)=\alpha(v_1,v_2,\ldots,v_n)=(\alpha v_1,\alpha v_2,\ldots,\alpha v_n)$$

인데,

$$\alpha v=\alpha\sum_{i=1}^nv_i x_i=\sum_{i=1}^n\alpha v_i x_i$$

이므로 $L(\alpha v)$의 값은 $\alpha L(v)$의 값과 동일하다. 마찬가지로, $L(v)+L(w)$와 $L(v+w)$의 값을 비교해보면

$$L(v)+L(w)=(v_1+w_1,v_2+w_2,\ldots,v_n+w_n)=L(v+w)$$

가 성립한다.

$\ker L$은 $\mathcal{B}$가 일차독립이므로 $\\{0\\}$이 된다. 한편, 임의의 $(\alpha_1,\ldots,\alpha_n)\in F^n$에 대하여 다음의 일차결합

$$\sum_{i=1}^n\alpha_i x_i$$

은 당연히 $V$에 속하므로, $L$은 단사함수이다. 

</div>


---

**참고문헌**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.

---
