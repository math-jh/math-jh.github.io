---

title: "동형사상"
excerpt: "서로 동등한 벡터공간들"

categories: [Math / Linear Algebra]
permalink: /ko/math/linear_algebra/isomorphic_vector_spaces
sidebar: 
    nav: "linear_algebra-ko"

header:
    overlay_image: /assets/images/Linear_algebra/Linear_map.png
    overlay_filter: 0.5

date: 2022-08-02
last_modified_at: 2022-08-01

weight: 8
---

## 동형인 벡터공간

앞선 글의 마지막 [예시](/ko/math/linear_algebra/linear_map#ex14)에서 정의한 linear map은 $v\mapsto [v]_B$이다. 

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