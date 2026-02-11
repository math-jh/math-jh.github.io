---

title: "대칭군"
excerpt: ""

categories: [Math / Group Theory]
permalink: /ko/math/group_theory/symmetric_groups
header:
    overlay_image: /assets/images/Math/Group_Theory/Symmetric_groups.png
    overlay_filter: 0.5
sidebar: 
    nav: "group_theory-ko"

date: 2025-03-29
last_modified_at: 2025-03-29
weight: 1

---

[대수적 구조](/ko/algebraic_structures) 카테고리에서 우리는 다양한 대수적인 구조들이 갖는 공통적인 성질에 관심이 있었는데, 이러한 방식은 대수적인 이론들이 어떻게 전개되는지를 전체적인 관점에서 조망하기에는 좋지만 실제로 특정한 군을 계산하거나 하는 등의 세부적인 부분을 살펴볼 때에는 좋지 않다. 때문에 이 카테고리의 글에서 우리는 [대수적 구조](/ko/algebraic_structures) 카테고리에서 다루지 않은 group의 성질들에 대해 살펴본다. 

## 대칭군

[군론](/ko/group_theory) 카테고리에서 처음으로 살펴볼 것은 특정한 group들이다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 집합 $[n]=\\{1,\ldots, n\\}$에 대하여, $[n]$의 $\Set$에서의 automorphism group $\Aut([n])$을 *symmetric group<sub>대칭군</sub>*이라 부르고 $S_n$으로 적는다.  

</div>

즉 $S_n$의 원소들은 집합 $[n]$에서 $[n]$으로 가는 전단사함수들이며, $S_n$의 연산은 함수의 합성으로 주어진다. $S_n$의 원소들은 *permutation*이라 부른다.

Permutation $\sigma: [n] \rightarrow [n]$이 주어졌다 하고, 집합 $[n]$의 $n+1$개의 원소들

$$1=\sigma^0(1), \quad\sigma(1)=\sigma^1(1),\quad\sigma^2(1),\quad\cdots, \quad\sigma^n(1)\tag{$\ast$}$$

을 생각하자. 비둘기집 원리에 의하여 서로 다른 적당한 두 정수 $0\leq k_1,k_2\leq n$가 존재하여 $\sigma^{k_1}(1)=\sigma^{k_2}(1)$이 성립하고, 편의상 $k_1< k_2$라 하면 이로부터 $\sigma^{k_2-k_1}(1)=0$임을 안다. 뿐만 아니라, $\sigma^k(1)=1$을 만족하는 가장 작은 자연수 $k$를 생각하면, 위의 결과로부터 $k\leq n$이며, 이를 바탕으로 다음의 표기

$$(1\quad \sigma(1)\quad \sigma(1)\quad\cdots\quad\sigma^{k-1}(1))$$

를 생각할 수 있다. 정의에 의해 이 표기는 $1$을 $\sigma(1)$로, $\sigma(1)$을 $\sigma^2(1)$로, $\ldots$, $\sigma^{k-2}(1)$을 $\sigma^{k-1}(1)$로, 그리고 $\sigma^{k-1}(1)$을 $\sigma^k(1)=1$로 보내는 함수를 의미하며, 더 일반적으로

$$(a_1\quad a_2\quad\cdots\quad a_{k})$$

은 $a_1$을 $a_2$로, $\ldots$, $a_{k-1}$을 $a_{k}$로, 그리고 $a_k$을 $a_1$로 보내고 나머지 원소들은 건드리지 않는 함수를 의미하며, 이를 길이 $k$의 *cycle*이라 부른다. 그럼 두 cycle $\sigma$, $\tau$에 대하여, $\sigma\tau$는 함수 $\sigma$와 $\tau$의 합성 $\sigma\circ\tau$를 의미한다. 

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> 예를 들어 $S_3$의 원소 $\sigma=(1\;2\;3)$를 생각하자. 이 함수는 $1$을 $2$로, $2$를 $3$으로, 그리고 $3$을 $1$로 보내는 함수이다. 한편, 다음의 합성

$$\tau_1\tau_2=(2\;3)(1\;3)$$

을 생각하자. 그럼 우선 $\tau_2$에 의해 $1$은 $3$으로, $2$는 $2$로, $3$은 $1$로 옮겨진다. 이후 $\tau_1$에 의하여 (원래 $1$이었던) $3$은 $2$로, $2$는 $3$으로 옮겨지므로 $\tau_1\tau_2$는 $1$을 $2$로, $2$를 $3$으로, $3$을 $1$로 보낸다. 즉 함수로서 $\sigma=\tau_1\tau_2$이다. 한편 다음의 합성

$$\tau_2\tau_1=(1\;3)(2\;3)$$

을 생각하면, $1$은 $3$으로, $2$는 $1$로, $3$은 $2$로 옮겨지는 것을 안다. 즉 $\tau_1\tau_2\neq\tau_2\tau_1$이다. 

</div>

$S_n$의 원소들의 합성은 함수의 합성이고, 일반적으로 함수의 합성은 교환법칙을 만족하지 않으므로 위의 예시는 예상했던 것이다. 그러나 특수한 경우, 어떠한 두 함수들은 commute할 수도 있다. 

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Permutation $\sigma_1,\ldots\sigma_r\in S_n$가 *disjoint<sub>서로소</sub>*라는 것은 만일 어떠한 $i$가 $\sigma_i(k)\neq k$를 만족한다면, 다른 모든 $j\neq i$에 대하여는 $\sigma_j(k)=k$인 것이다. 

</div>

그럼 임의의 disjoint permutation들 $\sigma_1,\ldots\sigma_r\in S_n$의 곱은 이들의 순서에 의존하지 않음이 자명하다. 뿐만 아니라 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $S_n$의 임의의 non-identity permutation은 disjoint cycle들의 곱으로 나타낼 수 있다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

집합 $[n]$ 위의 equivalence realtion $\sim$을

$$i\sim j\iff \sigma^m(i)=j\text{ for some $m$}$$

으로 정의하고, 그 quotient set을

$$[n]/{\sim}=\{C_1, \ldots, C_r\}$$

이라 하자. 이제 각각의 $1\leq k\leq r$에 대하여 다음의 식

$$\sigma_k(i)=\begin{cases}\sigma(x)&\text{if $x\in C_k$}\\x&\text{otherwise}\end{cases}$$

으로 정의하면 이들은 disjoint cycle이며 그 곱이 $\sigma$가 된다. 

</details>

이러한 방식으로 임의의 permutation을 disjoint cycle들의 곱으로 나타낸다면 그 장점 중 하나는 permutation $\sigma$의 order가 쉽게 보인다는 것이다. 즉, $\sigma=\sigma\_1\cdots\sigma\_r$이라 한다면 $\sigma$의 order는 $\sigma\_1,\ldots, \sigma\_r$들의 order의 최소공배수와 같으며, cycle들 $\sigma_1,\ldots, \sigma\_r$의 order는, 당연히 이들 각각의 길이와 같다. 

한편, 길이 $2$의 cycle을 *transposition*이라 부르자. 이는 단지 이 cycle에 등장하는 두 숫자만 서로 바꿔주는 함수이다. 그럼 위의 명제에 의해 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="cor5">**따름정리 5**</ins> $S_n$의 임의의 permutation은 transposition들의 곱으로 나타낼 수 있다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[명제 4](#prop4)에 의하여 임의의 cycle이 transposition들의 곱으로 나타난다는 것만 증명하면 충분하다. 

$$(k_1\;k_2\;\cdots\;k_r)=(k_{r-1}\;k_r)(k_{r-2}\;k_r)\cdots(k_2\;k_r)(k_1\;k_r).$$

</details>

한편, $S_n$의 모든 원소를 나타내기 위해서는 단 두 개의 원소면 충분하다. 

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> $S_n$의 모든 원소는 $(1\;2)$와 $(1\;2\;\cdots\;n)$의 곱으로 나타낼 수 있다.

</div>
      
이를 증명하기 위해서 우선 다음을 살펴보자. 

<div class="proposition" markdown="1">

<ins id="lem7">**보조정리 7**</ins> $\sigma\in S_n$라 하자. 그럼 $\sigma(1\;2)\sigma^{-1}=(\sigma(1)\;\sigma(2))$이 성립한다.

</div>

물론, $1$과 $2$는 다른 어떠한 수로 교체해도 상관없다.

<details class="proof--alone" markdown="1">
<summary>증명</summary>

우선 임의의 $i\geq 3$에 대하여, $\sigma(1\;2)\sigma^{-1}(\sigma(i))$의 값을 생각해보자. 그럼 $\sigma(i)$는 우선 $\sigma^{-1}(\sigma(i))=i$로 먼저 옮겨진다. $i\geq 3$이므로, 이 값은 $(1\;2)$를 통해서는 변하지 않고 바로 그 다음의 $\sigma$로 인해 $\sigma(i)$로 돌아간다. 즉, $i\geq 3$인 $\sigma(i)$들은 모두 이 변환에 대해 불변이므로, 우리는 $\sigma(1)$과 $\sigma(2)$의 값만 살펴보면 된다.

$\sigma(1)$은 우선 $\sigma^{-1}$을 통해 $1$로 옮겨진다. 그 후, $(1\;2)$에서 이 값은 $2$가 된 후 $\sigma$에서 마지막으로 $\sigma(2)$가 되고, 결과적으로 $\sigma(1)$은 $\sigma(2)$로 옮겨진다. 마찬가지로 $\sigma(2)$는 $\sigma(1)$로 옮겨진다는 것을 보일 수 있다.

따라서 $\sigma(1\;2)\sigma^{-1}=(\sigma(1)\;\sigma(2))$가 성립한다.

</details>

[보조정리 7](#lem7)에 $\sigma=(1\;2\;\cdots\;n)$, $(1\;2\;\cdots\;n)^2$, $\ldots$를 대입하다보면, 우리는 $(2\;3)$, $(3\;4)$, $\ldots$를 얻는다. 한편, 임의의 $(a\;b)$에 대하여, 일반성을 잃지 않고 $a&lt;b$라 한다면

$$\begin{aligned}
    (a\;b)&=(a\;a+1)(a+1\;b)(a\;a+1)\\
    &=(a\;a+1)(a+1\;a+2)(a+2\;b)(a+1\;a+2)(a\;a+1)\\
    &=\cdots\\
    &=(a\;a+1)(a+1\;a+2)\cdots(b-1\;b)\cdots(a+1\;a+2)(a\;a+1)
\end{aligned}$$

와 같이, $(a\;b)$는 $(i\;i+1)$ 형태의 cycle들의 곱으로 나타날 수 있다. 따라서 $(1\;2)$과 $(1\;2\;\cdots\;n)$를 이용하면 임의의 $(a\;b)$를 만들 수 있다. 그런데, 임의의 cycle $(a_1\;a_2\;\cdots\;a_k)$에 대해 다음의 식

$$(a_1\;a_2\;\cdots\;a_k)=(a_1\;a_2)(a_2\;a_3)\cdots(a_{k-1}\;a_k)$$

이 성립하므로, $(1\;2)$과 $(1\;2\;\cdots\;n)$은 모든 cycle을 만들 수 있고, 따라서 $S_n$의 임의의 원소도 만들 수 있으므로 [명제 6](#prop6)이 성립한다.

<div class="proposition" markdown="1">

<ins id="thm8">**정리 8 (Cayley)**</ins> 임의의 finite group $G$에 대하여, 적당한 자연수 $n$이 존재하여 $G$를 $S_n$의 어떤 subgroup과 isomorphic하도록 할 수 있다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

바꿔 말하자면, $\iota:G\rightarrow S_n$인 적당한 inclusion homomorphism $\iota$를 찾으면 된다. Group $G$의 각 원소 $g$에 대하여, 다음의 *left translation map*

$$L_g: G\rightarrow G,\qquad x\mapsto gx$$

을 정의하자. 그럼 cancellation law에 의하여 $L_g$는 injective homomorphism이다. 한편, 임의의 $x\in G$에 대하여, 

$$x=g(g^{-1}x)=L_g(g^{-1}x)$$

이므로, $L_g$는 surjective homomorphism이기도 하다. 즉, $L_g$는 $G$ 위에서 정의된 automorphism이 된다. $\lvert G\rvert=n$이라 하자. 그럼 $G$ 위에 정의된 automorphism은 집합 $G$ 위에 정의된 bijection이기도 하므로, $L_g$들은 모두 $S_n$들의 원소로 볼 수도 있다. 이제 $T:G\rightarrow S_n$을 다음의 식

$$T(g)=L_g$$ 

으로 정의하면, 임의의 $x\in G$에 대하여

$$T(gh)(x)=L_{gh}(x)=(gh)x=g(h(x))=(T_g\circ T_h)(x)$$

가 성립한다. 즉, $T$는 group homomorphism이다. 어렵지 않게 $T$가 injective라는 것도 확인할 수 있으므로, 원하는 결과를 얻는다.  

</details>

## 교대군

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> $S_n$의 각 원소 $\sigma$에 대하여, $i&lt;j$이지만 $\sigma(i)>\sigma(j)$인 pair $(i,j)$들을 *inversion*이라 부른다. 만약 inversion의 갯수가 홀수개라면, $\sigma$를 *odd permutation*이라 부르고, inversion의 갯수가 짝수개라면 $\sigma$를 *even permutation*이라 부른다. 

</div>

예를 들어, identity permutation은 inversion의 갯수가 0개이므로 even permutation이고, $(1\;2)$는 해당 조건을 만족하는 pair가 $(1,2)$밖에 없으므로 odd permutation이다. Dummit과 Hungerford 등을 포함한 많은 대수 책들은 이 정의 대신, even permutation을 

> 짝수 개의 transposition들의 곱으로 표현할 수 있는 permutation

으로 정의한다. 방금 우리의 정의에 비해 이 정의가 강점을 갖는 것은, 예를 들어 even permutation과 even permutation의 곱이 even이고 odd permutation과 even permutation의 곱이 odd인 성질 등등이 더 직관적으로 보인다는 것이다. 하지만 방금 우리의 정의와는 다르게 parity (즉, $\sigma$가 even인지 odd인지)가 잘 정의된다는 것이 명백하지 않다. 때문에 이 두 정의를 모두 들고 가는 것이 편리하다. 이들 책에서는 그래서 다음 보조정리를 통해, 해당 정의가 방금 우리가 정의한 [정의 9](#def9)과 동일하다는 것을 보인다. 

<div class="proposition" markdown="1">

<ins id="lem10">**보조정리 10**</ins> $\sigma$가 even permutation인 것은 $\sigma$가 짝수개의 transposition들의 곱으로 나타날 수 있는 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$n$개의 variable $x_1,\ldots, x_n$에 대하여, *Vandermonde polynomial* $\Delta$를 다음의 식

$$\Delta=\prod_{1\leq i< j\leq n}(x_i-x_j)$$

로 정의하자. $\Delta$는 $i&lt; j$를 만족하는 모든 pair $(i,j)$에 해당하는 term $(x_i-x_j)$들의 곱으로만 이루어진 polynomial이라는 것을 쉽게 관찰할 수 있다. 이제 $\Delta$에 precomposition을 적용해 $\sigma(\Delta)$를 만들자. 즉

$$\sigma(\Delta)=\prod_{1\leq i< j\leq n}(x_{\sigma(i)}-x_{\sigma(j)})$$

이다. 그럼 각각의 pair $(i,j)$에 대하여, term $(x_{\sigma(i)}-x_{\sigma(j)})$는 $\sigma(i)$와 $\sigma(j)$의 대소관계에 따라 

$$(x_{\sigma(i)}-x_{\sigma(j)})=\begin{cases}(x_{\sigma(i)}-x_{\sigma(j)})&\text{if $\sigma(i)<\sigma(j)$}\\-(x_{\sigma(j)}-x_{\sigma(i)})&\text{if $\sigma(i)>\sigma(j)$}\end{cases}\tag{1}$$

으로 바꾸어 쓸 수 있다. 또, $\sigma$는 bijection이므로, 이렇게 모든 term을 바꾸어 써 주면 $\sigma(\Delta)$는 부호만 제외하면 $\Delta$와 정확하게 같은 polynomial이 됨을 알 수 있다. 따라서 $\sgn(\sigma)=\sigma(\Delta)/\Delta$로 정의하면, $\sgn(\sigma)$는 정확하게 [정의 9](#def9)의 sense에서 정의된 $\sigma$의 parity가 된다.   

정의로부터, $\sigma$가 transposition이라면 $\sgn(\sigma)=-1$인 것은 자명하다. 따라서 만일 $\sgn$이 multiplicative하다는 것만 보인다면, 

$$\text{$\sigma$ odd}\iff\text{$\sgn(\sigma)=-1$}\iff\text{$\sigma$ is a product of odd number of permutation}$$ 

이 되므로 원하는 결과를 얻을 것이다. 두 permutation $\sigma$, $\tau$가 주어졌다 하자. $\sgn(\sigma\tau)$의 값을 계산해야 한다. $\tau$가 $k$개의 inversion을 갖는다 가정하자. 즉, $\sgn(\tau)=(-1)^k$이고, 이 $k$개의 $-1$들은 모두 식 (1)에서 나오는 factor들이다. 이제 $\sgn(\sigma\tau)$의 값을 계산하기 위해서는 우선

$$\prod_{1\leq i< j\leq n}(x_{\tau(i)}-x_{\tau(j)})=(-1)^k\Delta$$

의 양 변에 $(-1)^k$를 곱하여, 좌변의 각 term들을 원래대로 되돌려놓고 (즉, 이 상황에서 좌변은 곱셈 순서만 바뀐 $\Delta$이다), 이 원래대로 되돌아간 polynomial에 $\sigma$를 적용시켜주면 된다. 따라서, 만일 $\sigma$의 inversion의 갯수가 $l$개였다면, $\Delta$ 앞에 붙는 factor는 $(-1)^{k+l}$이었을 것이고, 이것이 곧 $\sgn$의 multiplicativity를 보장한다.
 
</details>

이 증명을 곰곰히 살펴보면, 우리가 만든 $\sgn$은 사실 단순한 map이 아니라, $S_n$에서 $\{\pm 1\}$로의 group homomorphism이라 할 수 있다. 그렇다면 $\ker(\sgn)$은 $S_n$의 normal subgroup이다.

<div class="definition" markdown="1">

<ins id="def11">**정의 11**</ins> 위에서 정의한 group homomorphism $\sgn$의 kernel을 *alternating group* of degree $n$이라 부르고, $A_n$으로 표기한다. 다른 말로 하자면, $A_n$은 모든 even permutation들의 모임이다.

</div>

한편 다음을 정의한다. 

<div class="definition" markdown="1">

<ins id="def12">**정의 12**</ins> Group $G$가 *simple*이라는 것은 $G$가 $\\{e\\}$와 자기 자신을 제외한 normal subgroup을 갖지 않는 것이다.

</div>

특기할만한 사실 중 하나는 $A_5$가 simple이라는 것이다. 

<div class="example" markdown="1">

<ins id="ex13">**예시 13**</ins> $A_5$는 simple이다. 이는 Sylow theorem을 사용하여 조금 더 고상하게 보일 수 있지만 $A_5$는 그렇게 큰 group은 아니므로 약간의 고생을 하면 현재 우리의 지식만으로도 이를 보일 수 있다. 

우선 $A_5$ 안의 permutation들은 다음과 같은 종류로 분류할 수 있다.

- 항등원 1개
- 3-cycle ($(123)=(2\;3)(1\;3)$의 형태): $20=\binom{5}{3}\cdot2$개
- 두 disjoint 2-cycle의 곱 ($(12)(34)$의 형태): $15=\binom{5}{2}\cdot\binom{3}{2}\cdot\frac{1}{2}$개
- 5-cycle ($(12345)=(4\;5)(3\;5)(2\;5)(1\;5)$의 형태): $24=4!$개

이들 네 종류의 permutation이 서로 다르다는 것은 각 원소들의 order를 보면 되고, 각 종류에 속하는 원소들이 서로 다른 것은 함수값을 직접 보면 된다. 

한편, 일반적으로 group $G$의 subgroup $N$이 normal subgroup이기 위해서는, 정확하게 정의에 의해 $N$이 inner automorphism에 의한 conjugacy class들의 합집합으로 나타나야 한다. 그런데 [보조정리 7](#lem7)을 사용하면, 위에서 3-cycle, 두 disjoint 2-cycle의 곱은 각각 conjugacy class들이 되며, $5$-cycle은 각각 원소 12개를 갖는 두 개의 conjugacy class들로 나뉜다는 것을 알 수 있다. 이제 $A_5$의 normal subgroup의 크기 $A_5$의 크기 $60$을 나눠야 하는데, 항등원을 포함하며 non-trivial한 conjugacy class들의 합집합으로는 $60$의 약수를 만들 수 없으므로 $A_5$는 non-trivial한 normal subgroup을 갖지 않는다. 

</div>

---
**Reference**

**[DF]** D.S. Dummit and R.M. Foote. Abstract Algebra. Wiley, 2003.

---