---

title: "선형사상"
excerpt: "선형사상의 정의와 예시"

categories: [Math / Linear Algebra]
permalink: /ko/math/linear_algebra/linear_map
sidebar: 
    nav: "linear_algebra-ko"

header:
    overlay_image: /assets/images/Linear_algebra/Linear_map.png
    overlay_filter: 0.5

date: 2021-10-13
last_modified_at: 2022-08-01

weight: 7
---
<div class="notice--warning" markdown="1">

이 글은 현재 수정중입니다.

이 글은 예전에 쓴 글로, 서술 방향이 마음에 들지 않거나 표기법이 마음에 들지 않아 전체적으로 수정이 진행중입니다. 읽으실 때 참고해주세요.

</div>


보편적으로 수학자들은 어떤 대상을 정의하고 나면, 그 대상들 사이의 함수를 정의해야 편히 잠들 수 있다. 우리는 이번 글에서 벡터공간들 간의 함수, 즉 *선형사상*을 정의한다.

## 선형사상

물론 벡터공간은 어찌되었건 집합 위에 추가적인 구조 (스칼라곱, 벡터들 사이의 합)이 주어진 것이므로, 집합 간의 함수가 존재한다. 하지만 우리가 *벡터공간들 간의* 함수라고 이야기하려면 이것만으로는 부족하고, 이들 구조를 함수가 보존해야 할 것이다. 즉,

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 체 $F$와, 두 $F$-벡터공간 $V,W$가 주어졌다 하자. 함수 $L:V\rightarrow W$가 *선형사상*이라는 것은, 

1. 임의의 $\alpha\in F$와 $v\in V$에 대해 $L(\alpha v)=\alpha L(v)$이고,
2. 임의의 $v_1,v_2\in V$에 대해 $L(v_1+v_2)=L(v_1)+L(v_2)$

가 모두 성립하는 것이다.

</div>

정의로부터 따라나오는 성질들이 몇 가지 있다.

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> 두 $F$-벡터공간 $V,W$와 선형사상 $L:V\rightarrow W$에 대하여,

1. $L(0)=0$.
2. 임의의 $v\in V$에 대하여 $L(-v)=-L(v)$.
3. 임의의 $u,v\in V$에 대하여 $L(u-v)=L(u)-L(v)$.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

1,2는 선형사상의 정의와 [§Basic definition, 명제 7](/ko/math/linear_algebra/basic_definition#pp7), 그리고 그 이후의 $(-1)v=-v$로부터 자명하다. 3번은 선형사상의 정의와 2번을 적용하면 된다.

</details>

<div class="proposition" markdown="1">

<ins id="pp3">**명제 3**</ins> 두 $F$-벡터공간 $V,W$와 선형사상 $L:V\rightarrow W$에 대하여,

$$L\left(\sum_{i\in I}\alpha_i v_i\right)=\sum_{i\in I}\alpha_i L(v_i),\qquad\text{$(\alpha_i)$ finitely supported.}$$

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$\operatorname{supp}(\alpha_i)$의 cardinality에 대한 귀납법으로 자명.

</details>

<div class="proposition" markdown="1">

<ins id="pp4">**명제 4**</ins> 세 $F$-벡터공간 $U,V,W$와 선형사상들 $L_1:U\rightarrow V$, $L_2:V\rightarrow W$에 대하여, $L_2\circ L_1:U\rightarrow W$는 선형사상이 된다.

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

<ins id="df5">**정의 5**</ins> 두 $F$-벡터공간 $V,W$와 선형사상 $L:V\rightarrow W$에 대하여,

1. $L(v_1)=L(v_2)$일 때마다 $v_1=v_2$라면, $L$을 *injective*라 부른다.
2. 임의의 $w\in W$에 대해 $L(v)=w$를 만족하는 $v\in L$이 존재한다면, $L$이 *surjective*하다고 한다. 

</div>

일반적으로 injection이나 surjection을 다룰 때 사용할 수 있는 도구는 위의 정의가 거의 전부지만, 지금 상황과 같이 다루는 대상이 단순한 집합이 아니라 어떠한 연산이 주어진 경우, 대수적인 도구도 사용할 수 있다.

<div class="definition" markdown="1">

<ins id="df6">**정의 6**</ins> 두 $F$-벡터공간 $V,W$와 선형사상 $L:V\rightarrow W$에 대하여, $L$의 *kernel* $\ker L$은 다음의 식

$$\ker L=\{v\in V: L(v)=0\}$$

으로 정의되는 집합이다. 또, $L$의 *image* $\operatorname{im}L$는 다음의 식

$$\operatorname{im}L=\{w\in W: L(v)=w\text{ for some $v\in V$}\}$$

으로 정의되는 집합이다.

</div>

어렵지 않게 다음을 확인할 수 있다.

<div class="proposition" markdown="1">

<ins id="pp7">**명제 7**</ins> 두 $F$-벡터공간 $V,W$와 선형사상 $L:V\rightarrow W$에 대하여, $\ker L\leq V$이고 $\operatorname{im}L\leq W$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $\ker L$은 $V$의 부분공간이다. 임의의 $\alpha\in F$, $v\in\ker L$에 대하여

$$L(\alpha v)=\alpha L(v)=\alpha\cdot 0=0$$

이고, 마찬가지로 임의의 $v_1$, $v_2\in \ker L$에 대하여 

$$L(v_1+v_2)=L(v_1)+L(v_2)=0+0=0$$

이므로 $\alpha v\in\ker L$, $v_1+v_2\in\ker L$이 성립하기 때문이다.

이와 비슷하게, $\operatorname{im}L$은 $W$의 부분공간이다. 임의의 $w,w_1,w_2\in W$와 $\alpha\in F$를 택해오면, 정의에 의해

$$L(v)=w,\quad L(v_1)=w_1,\quad L(v_2)=w_2$$

를 만족하는 $v,v_1,v_2\in V$가 존재하며 따라서

$$\alpha w=\alpha L(v)=L(\alpha v)\in\operatorname{im}L$$

그리고

$$w_1+w_2=L(v_1)+L(v_2)=L(v_1+v_2)\in \operatorname{im}L$$

이기 때문이다.

</details>

이들 $\ker L$과 $\operatorname{im}L$은 다음과 같은 관점에서, injection과 surjection을 표현하는 좋은 도구이다.

<div class="proposition" markdown="1">

<ins id="pp8">**명제 8**</ins> 두 $F$-벡터공간 $V,W$와 선형사상 $L:V\rightarrow W$에 대하여, 

1. $L$이 injective인 것은 $\ker L=\\{0\\}$인 것과 동치이고,
2. $L$이 surjective인 것은 $\operatorname{im}L=W$인 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

사실 2번 같은 경우는 그냥 정의고, 1번만 보이면 충분하다. 또, 만약 $L$이 injective라면, $L(v)=0$을 만족하는 $v$는 유일해야 하고, [명제 2](#pp2)에 의해 $0$은 이 식을 만족하므로 $\ker L=\\{0\\}$이어야 한다. 따라서, 보여야 할 것은 다음의 implication

> $\ker L=\\{0\\}\implies\text{$L$ injective}$

뿐이다. $L(v_1)=L(v_2)$인 $v_1,v_2\in V$가 주어졌다 가정하자. 그럼 다시 [명제 3](#pp3)에 의하여,

$$0=L(v_1)-L(v_2)=L(v_1-v_2)$$

이므로 $v_1-v_2\in\ker L$이다. $\ker L=\\{0\\}$이므로, $v_1-v_2=0$이고 따라서 $L$은 injective.

</details>

이 명제의 관점에서 보자면, $\ker L$이라는 공간은 $L$이 얼마나 injection에 가까운지를 ($\ker L$이 작을수록 injection에 가깝다), 그리고 $\operatorname{im}L$은 $L$이 얼마나 surjection에 가까운지를 ($\operatorname{im}L$이 $W$에 가까울수록 surjection에 가깝다) 나타내주는 공간이라 할 수 있다. 

<div class="proposition" markdown="1">

<ins id="crl9">**따름정리 9**</ins> 두 $F$-벡터공간 $V,W$와 선형사상 $L:V\rightarrow W$가 주어졌다 하자.

1. 만약 $L$이 injective라면, 임의의 일차독립인 부분집합 $S\subset V$에 대하여 $L(S)$ 또한 $W$에서 일차독립이다.
2. 만약 $L$이 surjective라면, $\operatorname{span}S=V$를 만족하는 $S\subset V$에 대해, $L(S)$ 또한 $\operatorname{span}L(S)=W$를 만족한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



1. $L(s)$들에 대하여, 만일

    $$\sum_{s\in S}\alpha_s L(s)=0,\qquad\text{$(\alpha_s)$ finitely supported}$$

    라면, [명제 3](#pp3)에 의해

    $$0=L\left(\sum_{s\in S}\alpha_ss\right)$$

    이므로, 앞선 명제에 의해 $\sum_{s\in S}\alpha_ss=0$이어야 한다. 이제, $S$는 일차독립인 부분집합이므로, $\alpha_s=0$이 모든 $s\in S$에 대해 성립해야 한다.

2. 임의의 $w\in W$가 주어졌다 하자. 그럼 $\operatorname{im}L=W$이므로, 적당한 $v\in V$가 존재하여 $L(v)=w$이다. 이제 $\operatorname{span}S=V$이므로, 적당한 스칼라들의 finitely supported family $(\alpha_s)_{s\in S}$가 존재하여,

    $$v=\sum_{s\in S}\alpha_ss$$
    
    가 성립하고, 양 변에 $L$을 취한 후 [명제 3](#pp3)을 적용하면
    
    $$w=L(v)=L\left(\sum_{s\in S}\alpha_ss\right)=\sum_{s\in S}\alpha_s L(s)$$
    
    가 성립한다. 따라서, 우리는 임의의 $w\in W$를 $L(S)$의 원소들의 일차결합으로 표현하였으므로 $\operatorname{span}L(S)=W$가 성립한다.
 
</details>

사실 위 따름정리의 두 주장은 각각 역 또한 성립하고, 그 증명도 어렵지 않지만 우리가 이들을 사용할 일은 없어서 남겨두었다.

## 선형사상의 예시들

이제 선형사상들의 예시를 좀 살펴보자.

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> 임의의 $F$-벡터공간 $V$와 $W$에 대하여, 다음의 식

$$L(v)=0\text{ for all $v\in V$}$$

으로 정의된 $L:V\rightarrow W$는 선형사상이 된다. 이 경우, $\operatorname{im}L=\\{0\\}$이고 $\ker L=V$이다.

</div>

이 경우, 이 함수 자체를 $0$으로 표기하기도 하지만, 아직 이 표기를 소개하지 않았기 때문에 별 특색 없는 $L$로 적었다. 조금 덜 자명한 예시는 다음과 같다.

<div class="example" markdown="1">

<ins id="ex11">**예시 11**</ins> 임의의 $F$-벡터공간 $V$와, $W\leq V$가 주어졌다 하자. 다음의 식

$$\iota(w)=w\text{ for all $w\in W$}$$

으로 정의된 $\iota:W\rightarrow W$는 선형사상이다. 이번에는 $\operatorname{im}\iota=W$이고, $\ker \iota=\\{0\\}$이다. 즉, $L$은 injective이다.

</div>

여기서 $\iota$는 inclusion을 나타내는 데에 주로 쓰이는 문자다. 

<div class="example" markdown="1">

<ins id="ex12">**예시 12**</ins> 임의의 $F$-벡터공간 $V$, $W$와, 그들의 곱 $V\times W$를 생각하자. 그럼 다음의 식

$$\operatorname{pr}_1((v,w))=v$$

으로 정의된 $\operatorname{pr}_1:V\times W\rightarrow V$는 선형사상이 된다. $\operatorname{im}\operatorname{pr}_1=V$이고, 

$$\ker \operatorname{pr}_1=\{(0,w):w\in W\}$$

임을 쉽게 확인할 수 있다. 물론, 비슷하게 $\operatorname{pr}_2:V\times W\rightarrow W$를 정의할 수도 있으며, $n$개의 순서쌍으로 이를 확장할 수도 있다. 특히, Euclidean $n$-space $F^n$에 대하여, 

$$\operatorname{pr}_i((a_1,\ldots, a_n))=a_i$$

으로 정의된 $\operatorname{pr}_i:F^n\rightarrow F$도 선형사상이 된다.

</div>

$\operatorname{pr}$은 projection의 머릿글자. 많은 책에서는 간단히 $p$, 혹은 $\pi$와 같이 쓴다.

<div class="example" markdown="1">

<ins id="ex13">**예시 13**</ins> $F[\mathrm{x}]$ 위에 정의된 함수 $D:F[\mathrm{x}]\rightarrow F[\mathrm{x}]$를 다음의 식

$$D\left(\sum_{i=0}^\infty a_i\mathrm{x}^i\right)=\sum_{i=1}^\infty ia_i\mathrm{x}^{i-1}$$

으로 정의하자. 그럼 $D$는 선형사상이고, $\operatorname{im} D= F[\mathrm{x}]$이다. 또, $\ker D$는 모든 constant polynomial들의 모임이다. 

</div>

마지막 예시는 우리 이야기를 새롭게 이어나갈 motivation을 준다.

<div class="example" markdown="1">

<ins id="ex14">**예시 14**</ins> 임의의 $n$차원 $F$-벡터공간 $V$가 주어졌다 하고, $B=\\{b_1,\ldots, b_n\\}$이 $V$의 기저라 하자. 즉 임의의 $v\in V$에 대하여, 

$$v=\sum_{i=1}^n v_i b_i$$

이도록 하는 스칼라들의 family $(v_i)_{i\in I}$가 항상 존재하며, 유일하게 결정된다. (우리는 이 표현을 $[v]_B$로 적기로 했었다.) 따라서, 함수 $L:V\rightarrow F^n$을 식 $v\mapsto (v_1,v_2,\ldots, v_n)\in F^n$으로 정의할 수 있다.

그럼 $L$은 선형사상이다. 임의의 $v,w\in V$에 대하여,

$$v=\sum_{i=1}^n v_i b_i,\quad w=\sum_{i=1}^n w_i b_i$$

이라 하면, 임의의 $\alpha\in F$에 대하여

$$\alpha L(v)=\alpha(v_1,v_2,\ldots,v_n)=(\alpha v_1,\alpha v_2,\ldots,\alpha v_n)$$

인데,

$$\alpha v=\alpha\sum_{i=1}^nv_i b_i=\sum_{i=1}^n\alpha v_i b_i$$

이므로 $L(\alpha v)$의 값은 $\alpha L(v)$의 값과 동일하다. 마찬가지로, $L(v)+L(w)$와 $L(v+w)$의 값을 비교해보면

$$L(v)+L(w)=(v_1+w_1,v_2+w_2,\ldots,v_n+w_n)=L(v+w)$$

가 성립한다.

$\ker L$은 $B$가 선형독립이므로 $\\{0\\}$이 된다. 한편, 임의의 $(\alpha_1,\ldots,\alpha_n)\in F^n$에 대하여 다음의 일차결합

$$\sum_{i=1}^n\alpha_i b_i$$

은 당연히 $V$에 속하므로, $L$은 surjective이다. 

</div>

## 동형인 벡터공간

앞선 [예시 14](#ex14)의 선형사상 $L$은, 복잡하게 쓰긴 했지만 결국은 $v\mapsto [v]_B$이다. $[v]_B$라는 것은 $v$와 다른 어떤 새로운 벡터가 아니라 단순히 $v$를 표현하는 방법 중 하나일 뿐이므로, 그 전의 예시들과는 다르게 $L$은 뭔가 특별한 점이 있어야 할 것 같다.

<div class="definition" markdown="1">

<ins id="df15">**정의 15**</ins> 두 $F$-벡터공간 $V,W$에 대하여, 선형사상 $L:V\rightarrow W$이 *동형사상*이라는 것은 $L$이 bijection인 것이다. 즉, $L$이 injective인 동시에 surjective인 것이다.  
만일 두 $F$-벡터공간 $V$, $W$ 사이에 동형사상이 존재한다면, $V$와 $W$가 *동형*이라고 하고, $V\cong W$로 표기한다.

</div>

우리는 동형인 두 벡터공간들을 사실상 같은 것으로 취급한다. 수학적으로 이야기해서, 어떠한 대상들을 같게 본다는 것은 이들을 모아둔 모임에 동치관계를 주는 것과 같다. 

<div class="proposition" markdown="1">

<ins id="pp16">**명제 16**</ins> [정의 15](#df15)의 관계 $\cong$는 동치관계이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

즉, $\cong$이 reflexive, symmetric, transitive함을 보여야 한다.

1. 우선 임의의 $F$-벡터공간 $V$에 대하여 $V\cong V$임은 자명하다. $\operatorname{id}_V:V\rightarrow V$가 $V$에서 $V$로의 동형사상이 되기 때문이다.
2. $\cong$이 symmetric인 것을 보이기 위해, $V\cong W$라 하자. 즉, $V$에서 $W$로의 동형사상 $L:V\rightarrow W$가 존재한다. $L$은 bijection이므로, 함수로서 $L^{-1}$이 존재하고, 이 때 $L^{-1}$ 또한 마찬가지로 bijection이다. 따라서 $L^{-1}$이 선형사상인 것을 보이는 것만으로 충분하다.  
    우선 임의의 $\alpha\in F$, $w\in W$에 대하여, $L^{-1}(\alpha w)=\alpha L^{-1}(w)$임을 보여야 한다. 그런데 $L$은 bijection이므로, 임의의 $w\in W$에 대하여 $L(v)=w$이도록 하는 $v\in V$가 유일하게 존재하고, 이 때 $L(\alpha v)=\alpha L(v)=\alpha w$이다. 따라서

    $$L^{-1}(\alpha w)=L^{-1}(L(\alpha v))=\alpha v=L^{-1}(w).$$

    이와 비슷하게 $L^{-1}(w_1+w_2)=L^{-1}(w_1)+L^{-1}(w_2)$ 또한 보일 수 있다. 
3. 마지막으로 $U\cong V$, $V\cong W$라 하자. Transitivity는 $U\cong W$임을 뜻한다. 이를 확인하기 위해 $U$에서 $W$로 가는 동형사상을 만들어야 하는데, 우리는 이미 두 동형사상 $L_1:U\rightarrow V$, $L_2:V\rightarrow W$를 갖고 있고, 두 선형사상의 합성은 선형사상이며, 두 bijection의 합성은 bijection이므로 증명 끝.

</details>

앞선 증명 중 다음의 명제는 따로 언급할만한 가치가 있다.

<div class="proposition" markdown="1">

<ins id="lem17">**보조정리 17**</ins> 두 $F$-벡터공간 $V$, $W$에 대하여 $L:V\rightarrow W$가 동형사상이라 하자. 그럼 $L$의 역함수 $L^{-1}$이 존재하며, $L^{-1}$은 선형사상이다.

</div>

$\cong$가 동치관계라는 사실은 기계적으로 증명되는 것이긴 하지만, 다음의 놀라운(!) 따름정리를 준다.

<div class="proposition" markdown="1">

<ins id="crl18">**따름정리 18**</ins> 두 $n$차원 $F$-벡터공간은 항상 동형이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[에시 14](#ex14)에서, 우리는 임의의 $n$차원 벡터공간 $V$에 대하여, $v\mapsto [v]\_B$가 동형사상인 것을 확인했다. 또 다른 $n$차원 벡터공간 $W$에 대해서도, $w\mapsto [w]_{B'}$ ($B'$는 $W$의 어떤 기저) 또한 동형사상이 될 것이므로, 이제 $\cong$의 transitivity에 의해 $V\cong W$이다.

</details>

물론 이 역 또한 성립한다.

<div class="proposition" markdown="1">

<ins id="pp19">**명제 19**</ins> 두 동형인 $F$-벡터공간 $V$, $W$와, 동형사상 $L:V\rightarrow W$가 주어졌다 하자. 만약 $B$가 $V$의 기저라면, $L(B)$도 $V$의 기저가 된다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[따름정리 9](#crl9).

</details>

## Rank-nullity theorem

앞선 [따름정리 18](#crl18)과 [명제 19](#pp19)는 두 벡터공간이 동형인지를 결정하는 유일한 요인이 차원임을 보여준다. 한편, 주어진 선형사상 $L$에 대하여 $\ker L$과 $\operatorname{im}L$들은 각각 $L$이 injective/surjective로부터 얼마나 떨어져있는지를 측정해주는 공간이었다. 아주 거칠게 이야기하자면, 어차피 공간을 결정지어주는 유일한 인자는 차원 뿐이므로, $\ker L$과 $\operatorname{im}L$을 모두 보는 대신, 이들의 차원만 봐도 대충 비슷한 양의 정보를 얻을 수 있어야 한다.

<div class="definition" markdown="1">

<ins id="df20">**정의 20**</ins> 두 $F$-벡터공간 $V,W$와 선형사상 $L:V\rightarrow W$이 주어졌다 하자. 그럼 

1. $\dim\ker L$을 $L$의 *nullity*라 하고, $\operatorname{null} L$로 표기한다.
2. $\dim\operatorname{im}L$을 $L$의 *rank*라 하고, $\operatorname{rank}L$로 표기한다.

</div>

다음 두 명제들은 새로 번호를 붙이기도 아깝다.

1. $L$이 injective인 것은 $\operatorname{null}L=0$인 것과 동치이다.
2. $L$이 surjective인 것은 $\operatorname{rank}L=\dim W$인 것과 동치이다.

뿐만 아니라, 다음의 정리가 성립한다.

<div class="proposition" markdown="1">

<ins id="thm21">**정리 21 (Rank-nullity theorem)**</ins> 두 $F$-벡터공간 $V,W$와 선형사상 $L:V\rightarrow W$이 주어졌다 하자. 그럼 다음의 식 

$$\operatorname{rank}L+\operatorname{null}L=\operatorname{dim}V$$

이 항상 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

편의를 위해 $\dim V=n$, $\operatorname{null} L=k$라 적자. 다음 두 경우는 자명하다.

1. 만일 $n=k$라면, $\ker L$은 $V$와 같은 차원을 가지는 부분공간이므로 $\ker L=V$가 성립한다. 따라서 $L$은 zero map이고, $\operatorname{im} L=0$이므로 $\operatorname{rank} L=0$이 되어 정리가 성립한다. 
2. 이와 비슷하게 만일 $k=0$이라면 $\ker L=0$이므로 $L$은 injection이다. 따라서 codomain을 $W$에서 $\operatorname{im} L$로 제한한다면 $L$은 $V$와 $\operatorname{im} L$ 사이의 bijective한 선형사상이 된다. 따라서 $\dim V=\dim\operatorname{im} L=\operatorname{rank} L$이 된다.

이제 $0&lt;k&lt;n$인 경우만 보이면 충분하다. $\left\\{b_1,b_2,\ldots, b_k\right\\}$가 $\ker L$의 기저라 하자. 그럼 이들은 일차독립인 $V$의 subset이므로, 우리는 이 집합을 확장하여 $V$의 기저 $\left\\{b_1,b_2,\ldots, b_k,b_{k+1},\ldots, b_n\right\\}$을 만들 수 있다. 우리는 $\left\\{L(b_{k+1}), L(b_{k+2}), \ldots, L(b_n)\right\\}$이 $\operatorname{im} L$의 기저가 됨을 보일 것이다.

우선 이 집합은 일차독립인데, 만일 

$$\alpha_{k+1}L(b_{k+1})+\alpha_{k+2}L(b_{k+2})+\cdots+\alpha_nL(b_n)=0$$

이 성립한다면 선형성에 의해 $L(\sum_{i=k+1}^n \alpha_i b_i)=0$이므로 $\sum_{i=k+1}^n\alpha_ib_i\in\ker L$이고, 따라서 어떤 $\alpha_1$, $\alpha_2$, $\ldots$, $\alpha_k$에 대하여

$$\sum_{i=k+1}^n\alpha_ib_i=\alpha_1b_1+\alpha_2b_2+\cdots+\alpha_kb_k$$

혹은

$$\alpha_1b_1+\alpha_2b_2+\cdots+\alpha_kb_k-\alpha_{k+1}b_{k+1}-\cdots-\alpha_nb_n=0$$

에서 $\left\\{b_1,b_2,\ldots, b_k,b_{k+1},\ldots, b_n\right\\}$가 일차독립이므로 $\alpha_1=\alpha_2=\cdots=\alpha_n=0$ (따라서 $\alpha_{k+1}=\alpha_{k+2}=\cdots=\alpha_n=0$)이 되기 때문이다.

또, 이 집합은 $\operatorname{im} L$을 생성한다. 임의의 $w\in \operatorname{im} L$이 주어졌다고 하자. 그럼 $L(v)=w$인 $v\in V$가 존재한다. $v=\sum_{i=1}^n \alpha_ib_i$라 하면, 

$$u=L\left(\sum_{i=1}^n\alpha_i b_i\right)=L\left(\sum_{i=1}^k\alpha_i b_i\right)+L\left(\sum_{i=k+1}^n\alpha_i b_i\right)=\sum_{i=k+1}^n\alpha_i L(b_i)$$

가 성립하기 때문이다.

이상에서 $\operatorname{rank} L=\dim\operatorname{im} L=n-k=\dim V-\operatorname{null} L$이므로, 정리의 식이 성립한다.

</details>

특히, 두 동형인 벡터공간은 반드시 같은 차원을 가져야 함을 알 수 있다. $L:V\rightarrow W$가 동형사상이라면, $\operatorname{null}L=0$이고 $\operatorname{rank}L=\dim W$인데, 그럼 위의 정리가 

$$\dim V=\operatorname{rank}L+\operatorname{null}L=\dim W+0=\dim W$$

임을 보여주기 때문이다. 이 관찰과 [따름정리 18](#crl18)을 보면, 두 벡터공간이 동형인 것은 정확하게 두 벡터공간의 차원이 같다는 것과 동일한 말이라는 것을 알 수 있다. [^1]

---
**Reference**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.
---

[^1]: 사실 이는 [따름정리 9](#crl9)에서 바로 유도되는 성질이기는 하다.
