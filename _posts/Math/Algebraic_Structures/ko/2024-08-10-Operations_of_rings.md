---

title: "환의 곱, 쌍대곱, 텐서곱"
excerpt: ""

categories: [Math / Algebraic Structures]
permalink: /ko/math/algebraic_structures/operations_of_rings
header:
    overlay_image: /assets/images/Math/Algebraic_Structures/Operations_of_rings.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_structures-ko"

date: 2024-08-10
last_modified_at: 2024-08-10
weight: 103

---

이제 우리는 ring들의 product와 coproduct를 정의한다. 

## 환들의 곱

환들의 곱의 경우는 어렵지 않게 정의할 수 있다. Ring들의 family $(A\_i)\_{i\in I}$가 주어졌다 하자. 그럼 abelian group의 product $\prod\_{i\in I}A\_i$가 잘 정의된다. 한편 $A\_i$ 위에 곱셈구조를 주는 $\mu\_i: A\_i\otimes A\_i \rightarrow A\_i$는 bilinear map $A\_i\times A\_i \rightarrow A\_i$와 같고, 이를 통해 집합들 사이의 함수

$$\left(\prod_{i\in I} A_i\right)\times\left(\prod_{i\in I} A_i\right) \cong \prod_{i\in I} (A_i\times A_i) \overset{\prod \mu_i}{\longrightarrow} \prod_{i\in I}A_i$$

를 정의할 수 있다.

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1**</ins> 위와 같이 정의된 함수는 abelian group $\left(\prod A\_i\right)\times\left(\prod A\_i\right)$에서 $\prod A\_i$로의 bilinear map이며, 따라서 abelian group homomorphism $\left(\prod A_i\right)\otimes\left(\prod A_i\right) \rightarrow \prod A\_i$를 유도한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

위의 함수를 직접 원소로 나타내면, $\prod A\_i$의 원소들은 순서쌍 $(a\_i)\_{i\in I}$의 꼴이며, 두 원소 $(a\_i)\_{i\in I}, (b\_i)\_{i\in I}\in \prod A\_i$에 대해 이들 둘을 위 함수에 넣은 결과는

$$(a_i)_{i\in I}(b_i)_{i\in I}=(a_ib_i)_{i\in I}$$

을 통해 곱셈이 주어지게 된다. 즉 주어진 함수는 두 원소의 성분별로 곱셈을 하는 함수이다. 이제 bilinearity 또한 성분별로 확인할 수 있다. 

</details>

이를 통해 $\prod A_i$ 또한 ring의 구조를 갖는다. 이 때, 이 ring의 덧셈에 대한 항등원은 모든 성분이 $0$인 원소이고 곱셈에 대한 항등원은 모든 성분이 $1$인 원소이다. 한편 임의의 두 ring homomorphism $f,g:A \rightarrow B$에 대하여, 

$$\Eq(f,g)=\{x\in A: f(x)=g(x)\}$$

으로 정의하면 임의의 $x,y\in\Eq(f,g)$에 대하여

$$f(xy)=f(x)f(y)=g(x)g(y)=g(xy)$$

이므로 $xy\in\Eq(f,g)$이다. 즉 $\Eq(f,g)$는 $A$의 subring이며, 이것이 $\Ring$에서 $f,g$의 equalizer를 정의한다. 이로부터 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2**</ins> Category $\Ring$은 complete이다. 

</div>

## 환들의 쌍대곱

한편 ring들의 coproduct를 정의하기 위해서는 약간의 노력이 필요하다. 이는 본질적으로 ring의 곱셈 연산이 commutative하지 않기 때문으로, $\Grp$에서 쌍대곱을 정의할 때도 비슷한 문제가 있었다. 이를 극복하기 위해 우리는 [§자유곱](/ko/math/algebraic_structures/free_products)에서 꽤나 귀찮은 방식으로 free product를 정의했어야 했다. Ring에서도 마찬가지 방식으로 coproduct를 정의할 수 있지만, 앞으로의 논의에 이것이 쓰일 일은 없으므로 다음과 같이 명제로 남겨두기만 한다. 

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> 임의의 ring들의 family $(A\_i)\_{i\in I}$에 대하여, 이들의 coproduct가 존재한다. 

</div>

한편 임의의 두 ring homomorphism $f,g:A \rightarrow B$이 주어졌다 하자. $B$의 ideal $\mathfrak{b}$를 $f(x)-g(x)$들로 생성되는 two-sided ideal이라 하면 $B/\mathfrak{b}$가 잘 정의된다. 그럼 [§군 동형사상, ⁋명제 8](/ko/math/algebraic_structures/isomorphism_theorems#prop8)과 동일한 증명을 통해 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> 위와 같은 상황에서, $\CoEq(f,g)=B/\mathfrak{b}$는 $f,g$의 coequalizer를 정의한다.

</div>

따라서 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5**</ins> Category $\Ring$은 bicomplete category이다.

</div>

## 환들의 텐서곱

마지막으로 $\Ring$에서의 tensor product $\otimes$를 정의한다. 이를 위해서는 임의의 두 ring $A,B$에 대하여, abelian group $A\otimes B$ 위에 곱셈구조, 즉 다음의 abelian group homomorphism

$$(A\otimes B)\otimes(A\otimes B) \rightarrow A\otimes B$$

를 정의하면 충분하다. 그런데 tensor product의 associatvity와 commutativity에 의하여, 

$$(A\otimes B)\otimes(A\otimes B)\cong (A\otimes A)\otimes (B\otimes B)$$

가 성립하고, 따라서 $\mu_A:A\otimes A \rightarrow A$와 $\mu_B: B\otimes B$가 $A\otimes B$ 위의 곱셈

$$(A\otimes B)\otimes(A\otimes B)\cong (A\otimes A)\otimes (B\otimes B)\overset{\mu_A\otimes\mu_B}{\longrightarrow} A\otimes B$$

을 정의한다.

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> 임의의 ring $A,B$에 대하여, 위와 같이 정의된 ring $A\otimes B$를 이들의 *tensor product*라 부른다. 

</div>

이를 통해 category $\Ring$이 symmetric monoidal category $(\Ring,\otimes, \mathbb{Z})$를 이룬다는 것을 확인할 수 있다. 명시적으로 $A\otimes B$ 위의 곱셈은

$$(a\otimes b)(a'\otimes b')=aa'\otimes bb'$$

를 통해 정의된다. 