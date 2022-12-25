---

title: "기수들 사이의 연산"
excerpt: "Cardinal number의 연산"

categories: [Math / Set Theory]
permalink: /ko/math/set_theory/operation_of_cardinals
header:
    overlay_image: /assets/images/Set_theory/Operation_of_cardinals.png
    overlay_filter: 0.5
sidebar: 
    nav: "set_theory-ko"

date: 2021-09-04
last_modified_at: 2022-11-29
weight: 25

---

## Cardinal 사이의 연산

이제 약속한 대로 cardinal들 간의 연산을 정의하자.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> $(\mathfrak{a}\_i)\_{i\in I}$가 cardinal들의 family라 하자. 집합 $\mathfrak{a}\_i$들의 곱 (resp. 합)의 cardinal을 이들의 *cardinal product*(resp. *cardinal sum*)이라 부르고 $\prod\_{i\in I}\mathfrak{a}\_i$ (resp. $\sum\_{i\in I}\mathfrak{a}_i$)로 적는다.

</div>

우리가 처음 집합의 합을 정의할 때, 굳이 분리합집합이라는 직관적인 이름을 놔두고 합이라는 용어를 쓴 이유가 여기에 있다.

우선, 위 정의들은 잘 정의되어있다. 만일 $A_i$와 $\mathfrak{a}\_i$가 equipotent하다면, $\prod\_{i\in I} A_i$와 $\prod\_{i\in I}\mathfrak{a}\_i$ 사이에도 bijection이 존재하기 때문이다. 이 연산들을 가지고 있다면 합과 곱의 성질들이 다음과 같이 cardinal간의 연산의 성질로 바뀌게 된다.

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> $(\mathfrak{a}\_i)\_{i\in I}$가 cardinal들의 family이고, $f$가 $K$에서 $I$로의 bijection이라 하자. 그럼 

$$\sum_{k\in K}\mathfrak{a}_{f(k)}=\sum_{i\in I}\mathfrak{a}_i,\quad \prod_{k\in K}\mathfrak{a}_{f(k)}=\prod_{i\in I}\mathfrak{a}_i$$ 

이다. 또, 만일 $(J_l)\_{l\in L}$가 $I$의 partition이라면 

$$\sum_{i\in I}\mathfrak{a}_{i}=\sum_{l\in L}\sum_{i\in J_l}\mathfrak{a}_i,\quad \prod_{i\in I}\mathfrak{a}_{i}=\prod_{l\in L}\prod_{i\in J_l}\mathfrak{a}_i$$

이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[§집합의 합, ⁋명제 7](/ko/math/set_theory/sum_of_sets#pp7)에 의하여 우리는 cardinal들의 합을 mutually disjoint family의 합집합으로 취급할 수 있다. 이제, 첫 번째 식들은 각각 [§합집합과 교집합, ⁋명제 4](/ko/math/set_theory/union_and_intersection#pp4), [§집합의 곱, ⁋명제 5](/ko/math/set_theory/product_of_sets#pp5)의 결과들이며, 두 번째 식들은 [§합집합과 교집합, ⁋명제 5](/ko/math/set_theory/union_and_intersection#pp5)와 [§곱집합의 성질, ⁋명제 3](/ko/math/set_theory/property_of_products#pp3)의 결과들이다.

</details>

<div class="proposition" markdown="1">

<ins id="pp3">**명제 3**</ins> $(\mathfrak{a}\_i)\_{i\in I}$가 cardinal들의 family이고, $J$ (resp. $K$)가 $I$의 부분집합 중 다음의 식 $\mathfrak{a}\_i=\mathbf{0}$ for all $i\not\in J$ (resp. $\mathfrak{a}\_i=\mathbf{1}$ for all $i\not\in K$)을 만족하는 부분집합이라 하자. 그럼 

$$\sum_{i\in I}\mathfrak{a}_i=\sum_{i\in J}\mathfrak{a}_i,\quad \prod_{i\in I}\mathfrak{a}_i=\prod_{i\in K}\mathfrak{a}_i$$

가 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

공집합과 합집합을 하는 것과, 원소 하나짜리 집합과 곱을 하는 것은 cadrinal에 영향을 미치지 않는다. ($x\mapsto (x,i)$가 $A$에서 $A\times\{i\}$로의 bijection을 정의한다)

</details>

그리고, 이렇게 자명한 결과들 외에도, 곱과 합집합 사이의 분배법칙 ([§곱집합의 성질, ⁋명제 7](/ko/math/set_theory/property_of_products#pp7))를 이용하면 다음의 명제를 얻는다. 

<div class="proposition" markdown="1">

<ins id="pp4">**명제 4**</ins> Cardinal들의 double-index가 주어진 family $((\mathfrak{a}\_{j,k})\_{j\in J_k})\_{k\in K}$에 대하여, $I=\prod\_{k\in K}J_k$라 하면 

$$\prod_{k\in K}\left(\sum_{j\in J_k}\mathfrak{a}_{j,k}\right)=\sum_{f\in I}\left(\prod_{k\in K}\mathfrak{a}_{k, f(k)}\right)$$

가 성립한다.
</div>

특별히, 위의 명제들을 유한한 경우에만 생각한다면 

- 두 개의 집합 $A$, $B$의 합집합을 하는 순서는 상관이 없으므로 $\mathfrak{a}+\mathfrak{b}=\mathfrak{b}+\mathfrak{a}$, 그리고 $A\times B$와 $B\times A$ 사이의 자연스러운 전단사함수가 존재하므로 $\mathfrak{a}\mathfrak{b}=\mathfrak{b}\mathfrak{a}$.
- 집합의 합과 곱의 결합법칙에 의하여, $\mathfrak{a}+(\mathfrak{b}+\mathfrak{c})=(\mathfrak{a}+\mathfrak{b})+\mathfrak{c}$이고 $\mathfrak{a}(\mathfrak{b}\mathfrak{c})=(\mathfrak{a}\mathfrak{b})\mathfrak{c}$
- 마지막으로, 분배법칙을 유한한 경우에 다시 쓰면 $\mathfrak{a}(\mathfrak{b}+\mathfrak{c})=\mathfrak{a}\mathfrak{c}+\mathfrak{a}\mathfrak{b}$.

등의 결과를 얻는다. 한편, 임의의 집합은 singleton들의 합으로 쓰여질 수 있으므로 (즉 $B=\bigcup\_{x\in B}\\{x\\}$가 항상 성립하므로) $I$가 cardinal $\mathfrak{b}$를 갖는 집합이라면

$$\mathfrak{b}=\sum_{i\in I} \mathfrak{c}_i,\qquad \mathfrak{c}_i=1\text{ for all $i\in I$}$$

을 얻고, 양 변에 $\mathfrak{a}$를 곱하여 앞선 [명제 4](#pp4)를 적용하면

$$\mathfrak{a}\mathfrak{b}=\mathfrak{a}\left(\sum_{i\in I}\mathfrak{c}_i\right)=\sum_{i\in I}\mathfrak{a}\mathfrak{c}_i=\sum_{i\in I}\mathfrak{a}$$

을 얻는다. 

<div class="proposition" markdown="1">

<ins id="pp5">**명제 5**</ins> $(\mathfrak{a}\_i)\_{i\in I}$가 cardinal들의 family라 하자. 그럼 $\prod\_{i\in I}\mathfrak{a}\_i\neq \mathbf{0}$인 것은 모든 $i\in I$에 대하여 $\mathfrak{a}_i\neq \mathbf{0}$인 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[§순서쌍, ⁋명제 10](/ko/math/set_theory/ordered_pair#pp10)의 임의의 product로의 확장. 증명도 동일하게 하면 된다.

</details>

<div class="proposition" markdown="1">

<ins id="pp6">**명제 6**</ins> 만일 $\mathfrak{a}$와 $\mathfrak{b}$가 $\mathfrak{a}+\mathbf{1}=\mathfrak{b}+\mathbf{1}$를 만족하는 cardinal들이라면, $\mathfrak{a}=\mathfrak{b}$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$X$가 cardinal $\mathfrak{a}+\mathbf{1}=\mathfrak{b}+\mathbf{1}$짜리 집합이라 하자. 그럼 집합 $X$의 cardinal $\mathfrak{a}$와 $\mathfrak{b}$짜리 부분집합이 존재하여, $X\setminus A$와 $X\setminus B$가 singleton이다. $X\setminus A=\{a\}$, $X\setminus B=\{b\}$라 하고, $A$에서 $B$로의 bijection을 

$$f(x)=\begin{cases}a&\text{if }x=b\\ x&\text{otherwise}\end{cases}$$ 

로 정의하면 된다.

</details>

우리는 심지어 cardinal들 간의 지수관계까지 정의할 수 있다. 함수들의 집합 $B^A$를 이용하면 된다.

<div class="definition" markdown="1">

<ins id="df7">**정의 7**</ins> $\mathfrak{a}$와 $\mathfrak{b}$가 cardinal이라 하자. $\mathfrak{b}$에서 $\mathfrak{a}$로의 함수들의 집합의 cardinal를 $\mathfrak{b}^\mathfrak{a}$로 적는다.

</div>

물론 엄밀히 말하자면 $\mathfrak{b}^\mathfrak{a}$의 equivalence class의 representative는 위의 함수들의 집합과 다를 수도 있으므로 약간의 abuse of notation이 있지만[^2] 문맥상 명확하므로 이렇게 쓰기로 한다.

<div class="proposition" markdown="1">

<ins id="pp8">**명제 8**</ins> $\mathfrak{a}$와 $\mathfrak{b}$가 cardinal이고 $I$가 $\card I=\mathfrak{b}$를 만족하는 집합이라 하자. 만일 모든 $i\in I$에 대하여 $\mathfrak{a}\_i=\mathfrak{a}$라면 $\mathfrak{a}^\mathfrak{b}=\prod_{i\in I}\mathfrak{a}_i$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$B^A$와 $\Fun(A,B)$ 간의 bijection이 존재하므로 자명하다.

</details>

Cardinal $\mathbf{0}$과 $\mathbf{1}$에 대한 성질들, 예컨대 $\mathfrak{a}^\mathbf{0}=\mathbf{1}$, $\mathfrak{a}^\mathbf{1}=\mathfrak{a}$, $\mathbf{1}^\mathfrak{a}=\mathbf{1}$, $\mathbf{0}^\mathfrak{a}=\mathbf{0}$ 등등은 쉽게 증명할 수 있다. 여기에서 가장 중요한 정리들 중 하나는 다음의 정리이다.

<div class="proposition" markdown="1">

<ins id="pp9">**명제 9**</ins> $A$가 집합이고 $\mathfrak{a}$가 그 cardinal이라 하자. 그럼 $\mathcal{P}(A)$의 cardinal는 $\mathbf{2}^\mathfrak{a}$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$\mathbf{2}=\\{\alpha, \beta\\}$가 cardinal이라 하자. 임의의 $X\in\mathcal{P}(A)$에 대하여, 만약 $x\in X$라면 $x\mapsto\alpha$이고, 그렇지 않을 때에는 $x\mapsto\beta$인 함수 $f_X:A\rightarrow \mathbf{2}$가 존재한다. 반대로 임의의 함수 $f:A\rightarrow \mathbf{2}$에 대하여, $f^{-1}(\alpha)$가 $\mathcal{P}(A)$의 원소를 하나 지정한다.

</details>

다음은 Cantor의 유명한 정리. 

<div class="proposition" markdown="1">

<ins id="pp10">**명제 10 (Cantor)**</ins> 임의의 cardinal $\mathfrak{a}$에 대하여 $\mathbf{2}^\mathfrak{a}>\mathfrak{a}$가 항상 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$x\mapsto \\{x\\}$가 $\mathfrak{a}$에서 멱집합으로의 단사함수이이므로, $\mathfrak{a}\leq \mathbf{2}^\mathfrak{a}$임은 자명하다. 따라서 $\mathfrak{a}\neq\mathbf{2}^\mathfrak{a}$임만 보이자. 즉, 임의의 함수 $f:\mathfrak{a}\rightarrow\mathcal{P}(\mathfrak{a})$에 대하여, $\mathfrak{a}$의 image 밖에 항상 어떤 원소가 존재한다는 걸 보이면 된다.

$X$가 $x\not\in f(x)$를 만족하는 모든 $x\in\mathfrak{a}$들의 집합이라 하자. 만일 $x\in X$라면, $x\not\in f(x)$이고 따라서 $f(x)\neq X$이며, 반대로 $x\not\in X$라면 $x\in f(x)$이므로 다시 $f(x)\neq X$이다. 따라서 $X\not\in f(\mathfrak{a})$이므로 증명이 완료되었다. 

</details>

만약 $\mathfrak{a}$가 유한집합이라면, $\mathfrak{a}$와 $\mathbf{2}^\mathfrak{a}$ 사이에는 항상 어떤 cardinal이 존재한다. 그런데 무한대인 경우에는 이것이 그렇게 자명하지 않다. 예를 들어, 자연수집합 $\mathbb{N}$의 크기보다, $\mathbb{N}$의 멱집합의 크기가 더 큰 것은 위의 명제에 의해 자명하지만 그 둘 사이에 어떠한 cardinal이 있을것인지는 쉽게 예측할 수 없다.

더 엄밀하게 쓰자면, 우리는 $\aleph_0,\aleph_1,\ldots$를 initial ordinal들로 정의했었다. 만일, 다음의 식

$$\beth_0=\aleph_0,\quad \beth_{\alpha+1}=\mathbf{2}^{\beth_\alpha}$$

으로 새로운 ordinal들의 열을 만든다면, $\beth_1$은 $\beth_0=\aleph_0$보다 확실하게 크므로, $\aleph$의 정의에 의해 $\aleph_1$보다 크거나 같다. 즉 $\aleph_1\leq \beth_1$이다. Cantor는 실수집합 $\mathbb{R}$의 크기가 $\beth_1$과 같다는 것을 증명하고는, 사실 $\aleph_1=\beth_1$이라는 *연속체 가설* (*continuum hypothesis*)을 제안했다. 이 가설이 맞다면, 실수는 자연수 바로 다음 크기를 갖는 집합이 된다. 더 일반적으로, $\aleph_\alpha=\beth_\alpha$가 성립한다는 것이 일반화된 연속체 가설이다. 

이 가설은 제안된 이후 미해결 문제로 남아있다가, Gödel과 Cohen에 의해 이 가설은 ZFC 공리계 상에서 증명도, 반증도 하지 못한다는 것이 증명되었다. 괴델이 비교적 일찍 ZFC 공리계 상에서 CH는 반증이 불가능하다라는 것을 증명하였으며, 이후 Cohen이 ZFC 공리계 상에서 CH는 증명이 불가능하다는 것을 증명했다.   


---

**참고문헌** 

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---