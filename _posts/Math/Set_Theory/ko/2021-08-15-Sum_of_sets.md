---

title: "집합의 합"
excerpt: "집합들 사이의 합 (분리합집합)"

categories: [Math / Set Theory]
permalink: /ko/math/set_theory/sum_of_sets
header:
    overlay_image: /assets/images/Math/Set_Theory/Sum_of_sets.png
    overlay_filter: 0.5
sidebar: 
    nav: "set_theory-ko"

date: 2021-08-15
last_modified_at: 2022-11-25
weight: 9

---

## Covering

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Family $(A\_i)\_{i\in I}$가 집합 $A$의 *covering<sub>덮개</sub>*이라는 것은 $A=\bigcup\_{i\in I} A\_i$임을 뜻한다. $A$의 두 covering $(A\_i)\_{i\in I}$와 $(A'\_j)\_{j\in J}$에 대하여, $(A'_j)\_{j\in J}$가 $(A_i)\_{i\in I}$보다 *finer<sub>섬세</sub>*하다는 것은 임의의 $j\in J$에 대하여, $A'\_j\subseteq A\_i$를 만족하는 $i\in I$가 존재하는 것이다.

</div>

집합 $A$의 covering $(A\_i)\_{i\in I}$이 주어졌다 하자. 그럼 임의의 함수 $f:B \rightarrow A$에 대하여, $B$의 부분집합들의 family $(f^{-1}(A\_i))\_{i\in I}$는 $B$의 covering이 된다. 이를 $(A\_i)$의 $f$에 의한 preimage라 부른다. 임의의 함수 $g:A\rightarrow C$에 대하여는 $C$의 부분집합들의 family $(g(A\_i))\_{i\in I}$가 $C$의 covering이 될 필요는 없지만, 만일 $g$가 전사함수라면 이들이 $C$를 덮는다. 이를 전사함수 $g$에 의한 $(A\_i)$의 image라 부른다. 


<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins>  집합 $A$와 그 covering $(A_i)\_{i\in I}$를 생각하고, 임의의 집합 $B$를 택하자.

1. 함수 $f,g:A\rightarrow B$가 임의의 $i\in I$가 주어질 때마다 $f\|\_{A\_i}=g\|\_{A\_i}$를 만족한다 하자. 그럼 $f=g$이다. 
2. 함수들의 family $(f\_i:A\_i\rightarrow B)\_{i\in I}$가 다음의 조건
    
    $$f_i|_{A_i\cap A_j}=f_j|_{A_i\cap A_j}$$

    를 만족한다면, 모든 $f_i$를 확장하는 함수 $f:A\rightarrow B$가 존재한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

우선 첫 번째 주장을 보이기 위해 임의의 $x\in A$가 주어졌다고 하자. $(A_i)\_{i\in I}$가 $A$를 덮으므로, 어떤 $i\in I$가 존재하여 $x\in A_i$이다. 이제

$$f(x)=(f|_{A_i})(x)=(g|_{A_i})(x)=g(x)$$

이므로 첫 번째 주장이 성립한다.

두 번째 주장의 경우, 주어진 함수들 $f\_i=(F\_i,A\_i,B)$를 사용하여 $F=\bigcup F\_i$를 만들고, 새로운 triple $f=(F,A,B)$를 생각하자. 그럼 $\pr\_1F=A$임이 자명하며, 따라서 $f$가 함수임을 보이기 위해서는 임의의 $x\in A$에 대하여 $(x,y)\in F$가 참이도록 하는 $y$가 유일함을 보이면 충분하다.

$y,y'\in B$가 $(x,y)\in F$, $(x,y')\in F$를 만족한다 하자. 그럼 $(x,y)\in F\_i$, $(x,y')\in F\_j$이도록 하는 $i,j$가 각각 존재한다. 이제 

$$y=(f_i)(x)=(f_i|_{A_i\cap A_j})(x)=(f_j|_{A_i\cap A_j})(x)=(f_j)(x)=y'$$

이므로 둘째 주장 또한 성립한다.

</details>

위의 명제의 2번을 만족하는 함수 $f$는 첫째 주장에 의하여 유일하다는 것이 자명하다. 또, 특별히 $A\_i\cap A\_j$가 모든 $i,j$에 대하여 성립한다면 둘째 주장의 전제조건이 항상 만족된다. 이를 다음과 같이 정의한다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 집합 $A$와 $B$가 *서로소<sub>disjoint</sub>*라는 것은 $A\cap B=\emptyset$인 것이다. 더 일반적으로, $(A_i)\_{i\in I}$가 *쌍마다 서로소<sub>pairwise disjoint</sub>*라는 것은 임의의 $i, j\in I$에 대하여 $i\neq j$라면 $A_i\cap A_j=\emptyset$인 것이다.

</div>

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> 집합 $A$의 *분할<sub>partition</sub>*은 $A$의 쌍마다 서로소인 covering을 뜻한다.

</div>

일반적으로 이 family의 구성원 중 $\emptyset$은 어떠한 역할도 하지 않으므로, 분할이라고 하면 모든 구성원이 공집합이 아님을 전제로 한다. 

## 집합의 합

<div class="proposition" markdown="1">

<ins id="p53">**명제 5**</ins> $(A_i)\_{i\in I}$가 어떤 집합들의 family라 하자. 그럼 어떠한 집합 $S$가 존재하여, 

- $S$는 쌍마다 서로소인 family $(S\_i)\_{i\in I}$들의 합집합이며, 
- 모든 $i\in I$에 대하여 $A_i$에서 $S_i$로의 전단사함수가 존재한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$S_i$를 <phrase>$x\in A_i$를 만족하는 $(x, i)$들로 이루어진 집합</phrase>이라 하자. 그럼 $(S_i)\_{i\in I}$는 쌍마다 서로소이다. 또, 각각의 $i$에 대하여 $x\mapsto (x,i)$는 $A_i$에서 $S_i$로의 전단사함수가 된다. 따라서 $S=\bigcup\_{i\in I} S_i$가 주어진 조건을 만족한다.

</details>

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> 위의 조건을 만족하는 $S$를 family $(A_i)\_{i\in I}$들의 *합<sub>sum</sub>*이라 하며, $\sum\_{i\in I} A_i$로 적는다.

</div>

이 집합을 종종 *분리합집합<sub>disjoint union</sub>*이라 부르고, $\bigsqcup_{i\in I} A_i$으로 적기도 한다. 다음 명제를 보면 이 이름도 꽤나 그럴싸해 보인다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> 쌍마다 서로소인 family $(A_i)\_{i\in I}$를 생각하자. 이들의 합집합을 $A$, 합을 $S$라 하면 $A$와 $S$ 간의 전단사함수가 존재한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$f_i:A_i\rightarrow S_i$가 [명제 5](#prop5)의 조건을 만족하는 전단사함수라면, [명제 2](#prop2)를 통해 $(f_i)\_{i\in I}$를 $\bigcup\_{i\in I} A_i=A$로 확장하면 된다.

</details>

이를 집합의 합이라고 부르는 것에 대한 직관은 나중에 나온다. ([§Cardinal, ⁋정의 6](/ko/math/set_theory/cardinals#def6))

## Universal property

[정의 6](#def6)에서 우리가 언급하지 않은 사실이 있다. 집합들의 family $(A_i)$들의 합 $X$는 유일하지 않다는 것이다. [명제 5](#prop5)의 조건을 만족하는 집합은 무수히 많다. 예를 들어 해당 명제의 증명에서는 $S$를 $(x,i)$들의 집합으로 두었는데, $(i,x)$들의 집합으로 두어도 합의 정의를 만족한다는 것을 알 수 있다. 때문에 엄밀히 말하자면 $A_i$들의 합을 $\sum A_i$로 적는 것은 잘 정의된 표현이 아니다.

우선 다음과 같이 합의 *universal property<sub>보편성질</sub>*를 살펴보자.

<div class="proposition" markdown="1">

<ins id="thm8">**정리 8 (Universal property of sum)**</ins> 집합들의 family $(A_i)$와 [명제 5](#prop5)에서 정의한 집합 $S$, 그리고 단사함수들 $\iota_i:A_i\rightarrow S$가 주어졌다 하자. 그럼, 또 다른 어떤 집합 $B$와, $f_i:A_i\rightarrow B$들이 주어질 때마다, 이에 해당하는 유일한 $f:S\rightarrow B$가 존재하여 $f_i=f\circ\iota_i$가 성립한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선, 이러한 함수 $f$가 (존재한다면) 유일하다는 것을 보이자. 이를 위해서는 임의의 $x\in S$에 대하여, 그 함숫값 $f(x)$가 항상 유일하게 결정된다는 것을 보이면 충분하다. $S$는 쌍마다 서로소인 family $(S_i)$들의 합집합이므로, $x\in S_i$이도록 하는 유일한 $i\in I$가 존재한다. 그럼 $\iota_i:A_i\rightarrow S_i$가 전단사함수이므로, 또 다시 $A_i$의 유일한 원소 $x_i$가 존재하여 $\iota_i(x_i)=x$이도록 할 수 있다. 이제,

$$f(x)=f(\iota_i(x_i))=(f\circ\iota_i)(x_i)=f_i(x_i)$$

이므로, $x$에서의 함숫값 $f(x)$는 반드시 $f_i(x_i)$와 같아야 하고 따라서 $f$는 유일하게 결정된다.

이제 유일성 증명에서 힌트를 얻어, 함수 $f$의 존재성을 보이자. $f(x)$를 위의 식과 같이 $f_i(x_i)$로 <em_ko>정의</em_ko>하고, $f$가 실제로 함수가 된다는 것을 증명하면 된다. 예를 들어, 이렇게 정의하면 $f$는 모든 $S$의 원소에 대해 정의가 될 것이며, 또 하나의 $x$는 위에서 이야기한 것과 같이 오직 하나의 함숫값만을 지정한다.

</details>


많은 경우에 [명제 5](#prop5)의 증명에 등장한 집합 $S$를 $A_i$들의 합이라 정의하지만, 사실 이는 주객이 전도된 정의다. 우리가 많은 분야들에서 $S$를 $A_i$들의 합으로 생각하는 이유는 표기법 상의 편리함 때문이지, $S$라는 집합 자체가 특별한 의미를 가져서가 아니다. 합의 성질은 집합 $S$에서 나오는 것이 아니라, 위의 universal property에서 나온다.

따라서 애초에 다음과 같이 정의를 해 버릴 수도 있다.

<div class="definition" markdown="1">

<ins id="def6-1">**정의 6$'$**</ins> 주어진 집합들의 family $(A_i)$의 *합*은 다음과 같은 조건
 
> 임의의 집합 $B$와 $f_i:A_i\rightarrow B$가 주어질 때마다, 유일한 함수 $f:\sum A_i\rightarrow B$가 존재하여 $f_i=f\circ\iota_i$가 성립한다.

![universal_property_of_sum](/assets/images/Math/Set_Theory/Sum_of_sets-1.png){:style="width:12em" class="invert" .align-center}

을 만족하는 집합 $\sum A_i$와 $\iota_i:A_i\rightarrow \sum A_i$들의 모임이다.

</div>

물론 이를 정의로 쓰기 위해서는 universal property를 만족하는 대상이 적어도 하나 존재한다는 것은 보여줘야 한다. 그리고 [정리 8](#thm8)이 정확히 그런 역할을 해 준다. 

우리는 앞서 $\sum A_i$라는 집합이 엄밀한 의미에서는 잘 정의되지 않는다는 것을 언급했다. 하지만 이러한 집합 자체는 잘 정의되지 않더라도, 이러한 집합들이 여럿 주어진다면 이들 사이의 전단사함수가 존재한다. 이런 상황을 *전단사함수에 대하여 유일하다<sub>unique up to bijection</sub>*고 말한다. [정의 6$'$](#def6-1)으로부터 집합의 합은 전단사함수에 대하여 유일하다는 것을 보일 수 있다. 

<div class="proposition" markdown="1">

<ins id="cor9">**따름정리 9**</ins> 집합들의 family $(A_i)$에 대하여, $\sum A_i$는 전단사함수에 대하여 유일하다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

두 개의 합 $S$, $S'$가 주어졌다 하고, $A_i$에서 $S$, $S'$로의 단사함수들을 각각 $\iota_i$, $\iota_i'$라 하자. 우선, 함수 $\iota_i':A_i\rightarrow Y$에 대하여, $S$의 universal property를 적용하면 유일한 $\phi':S\rightarrow S'$가 존재하여 $\iota_i'=\phi'\circ\iota_i$이도록 할 수 있다. 이와 비슷하게, 함수 $\iota_i$들에 $S'$의 universal property를 적용하면, 또 다시 유일한 $\phi:S'\rightarrow S$가 존재하여 $\iota_i=\phi\circ\iota_i'$이도록 할 수 있다. 그럼

$$\iota_i'=\phi'\circ\iota_i=\phi'\circ(\phi\circ\iota_i')=(\phi'\circ\phi)\circ\iota_i'$$

이다. 한편, 함수들 $\iota_i':A_i\rightarrow S'$에 이번에는 $S'$의 universal property를 적용하자. 그럼 어떤 유일한 함수 $\psi:S'\rightarrow S'$가 존재하여 $\iota_i'=\psi\circ\iota_i'$를 만족한다. 이는 당연히 $\psi=\id\_{S'}$에 의해 만족되는 식이므로, 유일성에 의해 이 식을 만족하는 모든 함수 $\psi$들은 $\id\_{S'}$와 같다. 따라서 $\phi'\circ\phi=\id\_{S'}$이고, $\id\_{S'}$는 전단사이므로 $\phi'$는 전사함수, $\phi$는 단사함수이다. ([§Retraction과 section, ⁋명제 3](/ko/math/set_theory/retraction_and_section#prop3))

마찬가지로, $\phi\circ\phi'=\id\_S$임을 보일 수 있고, 이로 인해 $\phi$는 전사함수, $\phi'$는 단사함수다. 즉, 이들은 각각 전단사함수가 되므로 $S$와 $S'$ 사이의 전단사함수가 존재한다. 

</details>


---
**참고문헌**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---

