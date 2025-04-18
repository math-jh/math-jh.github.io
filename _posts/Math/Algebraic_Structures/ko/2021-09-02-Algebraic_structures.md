---

title: "대수적 구조"
excerpt: "집합 위에 정의된 이항연산"

categories: [Math / Algebraic Structures]
permalink: /ko/math/algebraic_structures/algebraic_structures
header:
    overlay_image: /assets/images/Math/Algebraic_Structures/Algebraic_structures.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_structures-ko"

date: 2021-09-02
last_modified_at: 2022-11-29
weight: 1

---

[대수적 구조](/ko/algebraic_structures) 카테고리에서 우리는 group과 ring을 정의하고, 이들의 기본적인 성질들을 탐구한다. 이들은 집합 위에 이항연산의 구조를 추가하여 얻어지는데, group은 하나의 연산을, ring은 두 개의 연산을 추가하여 얻어지는 구조이다. 이들에 추가적으로 ring의 action을 주면 module과 algebra를 얻는다. 이들 대수적 구조 외에 갈루아 이론이나 tensor algebra 등은 별도의 카테고리로 분리하였다.

## 이항연산

이번 글에서 우리는 이항연산이 하나 주어져 있는 대수적 구조인 *마그마*를 살펴본다. 이 구조는 너무 적은 정보를 가지고 있어서 앞으로 사용할 일은 없지만, 앞으로 새로운 대수적 구조를 정의할 때마다 이번 글에서 정의할 부분구조나 몫구조 등을 생각하게 된다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 집합 $A$에 대하여, $A\times A$에서 $A$로의 함수 $\star$를 *이항연산*이라 부른다. 이항연산이 주어져 있는 집합을 *마그마*라 부른다.

</div>

이항연산 $\star$의 함수값 $\star(x,y)$는 $x\ast y$로 줄여쓴다. 마그마는 집합 $A$ 뿐만 아니라 그 위에 정의된 연산까지도 포함하는 구조이므로, 문맥상 명확할 경우를 제외하면 마그마를 나타낼 때에는 $(A,\star)$와 같이 연산과 집합을 모두 표기해준다.

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> 임의의 집합 $X$에 대하여, $(\mathcal{P}(X),\cup)$과 $(\mathcal{P}(X),\cap)$은 모두 마그마이다.

$\mathbb{N}$ 위에 정의된 연산 $x-y$ 또한 이항연산이므로, $(\mathbb{N}, -)$ 또한 마그마이다.

</div>

두 마그마 $(\mathcal{P}(X),\cup)$과 $\mathcal{P}(X),\cap)$에서는 다음의 식

$$A\cup(B\cup C)=(A\cup B)\cup C,\qquad A\cap(B\cap C)=(A\cap B)\cap C$$

이 모든 $A,B,C\in\mathcal{P}(X)$에 대해 성립한다. 반면

$$4-(1-2)=5\neq 1=(4-1)-2$$

이므로 $(\mathbb{N},-)$에서는 이러한 성질이 성립하지 않는다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 마그마 $(A,\star)$에 대하여, 임의의 $x$, $y$, $z\in A$에 대해 다음의 식

$$x\star(y\star z)=(x\star y)\star z$$

가 항상 성립하다면, $\star$가 *결합법칙을 만족한다<sub>associative</sub>*고 하고, 마그마 $A$를 *결합법칙을 만족하는 마그마<sub>associative magma</sub>*라 부른다.

</div>

만일 $\star$가 결합법칙을 만족한다면, 표현 $x\star y\star z$을 두 가지 방법으로 계산하여도

$$(x\star y)\star z=x\star(y\star z)$$

이므로 혼동의 여지 없이 $x\star y\star z$가 명확한 의미를 갖는다. 이는 diagram으로 나타내면 다음 diagram

![associativity](/assets/images/Math/Algebraic_Structures/Algebraic_structures-1.png){:style="width:11em" class="invert" .align-center}

이 commute한다는 의미이다. 한편, 앞선 연산들은 또 다른 차이점이 있다. 

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> 마그마 $(A, \star)$에 대하여, 만일 임의의 $x,y\in A$에 대해 다음의 식

$$x\star y=y\star x$$

가 항상 성립한다면, $\star$가 *교환법칙을 만족한다<sub>commutative</sub>*고 하고, 마그마 $A$를 *교환법칙을 만족하는 마그마<sub>commutative magma</sub>*라 부른다.

</div>

교솬법칙은 다음의 diagram

![commutativity](/assets/images/Math/Algebraic_Structures/Algebraic_structures-2.png){:style="width:13em" class="invert" .align-center}

이 commute한다는 의미이다. 여기서 $\sigma$는 $(x,y)\mapsto (y,x)$로 정의된 함수이다. 

일반적으로 교환법칙이 성립하더라도 결합법칙은 성립하지 않을 수 있고, 거꾸로 결합법칙이 성립하더라도 교환법칙이 성립하지 않을 수도 있다.

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> 마그마들의 family $(A_i, \star_i)_{i\in I}$를 생각하자. 그럼

$$\prod_{i\in I} (A_i\times A_i)\cong\left(\prod_{i\in I} A_i\right)\times\left(\prod_{i\in I}A_i\right)$$

이므로 ([\[집합론\] §곱집합의 성질, ⁋명제 3](/ko/math/set_theory/property_of_products#prop3)), 함수

$$\prod_{i\in I}\star_i:\prod_{i\in I} (A_i\times A_i) \rightarrow \prod_{i\in I} A_i$$

를 $\left(\prod_{i\in I} A_i\right)\times\left(\prod_{i\in I}A_i\right)$에서 $\left(\prod_{i\in I} A_i\right)\times\left(\prod_{i\in I}A_i\right)$로의 함수로 볼 수 있다. ([\[집합론\] §곱집합의 성질, ⁋정의 4](/ko/math/set_theory/property_of_products#def4)) 따라서 $\prod A_i$는 $\star=\prod\star_i$에 대해 마그마 구조를 갖는다. 이렇게 얻어지는 마그마 $(\prod A_i, \star)$를 *곱<sub>product magma</sub>*이라고 부른다. 

위의 두 diagram들을 모든 $i\in I$에 대하여 곱하면, 만일 $\star_i$들이 모두 교환법칙을 만족하거나, 모두 결합법칙을 만족한다면 $\star$ 또한 그렇다는 것을 알 수 있다. 

</div>

## 준동형사상과 부분구조

두 마그마 $A$, $A'$가 주어졌다 하자. 집합으로서 이들 사이에는 함수 $f:A\rightarrow A'$가 존재하지만, 이들은 단순한 집합이 아니라 이항연산이 추가된 대수적인 구조이므로 함수 또한 이항연산을 보존하는 것이 자연스럽다.

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> 두 마그마 $(A,\star)$, $(A',\star')$ 사이의 함수 $f:A\rightarrow A'$가 다음의 식

$$f(x\star y)=f(x)\star'f(y)$$

을 모든 $x$, $y\in A$에 대해 만족한다면, 이 함수 $f$를 *homomorphism<sub>준동형사상</sub>*, 강조가 필요할 때는 *magma homomorphism<sub>마그마 준동형사상</sub>*이라 부른다. 만약 또 다른 homomorphism $g:A'\rightarrow A$가 존재하여 

$$g\circ f=\id_A,\qquad f\circ g=\id_{A'}$$

가 성립한다면, $f$와 $g$가 서로의 *역<sub>inverse</sub>*이라 부르고, $f$와 $g$를 *isomorphism<sub>동형사상</sub>*이라 부른다. 이 때, $A$와 $A'$는 *isomorphic<sub>동형</sub>*하다고 부르고, 기호로 $A\cong A'$와 같이 표기한다.

</div>

어렵지 않게 전단사인 magma homomorphism은 magma isomorphism이라는 것을 안다. 또, 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> Magma homomorphism $f:A_1\rightarrow A_2$, $g:A_2\rightarrow A_3$에 대하여 합성 $g\circ f$는 magma homomorphism이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $x,y\in A_1$에 대하여,

$$(g\circ f)(x\star_1 y)=g(f(x\star_1y))=g(f(x)\star_2f(y))=g(f(x))\star_3g(f(y))=(g\circ f)(x)\star_3(g\circ f)(y)$$

이 성립한다.

</details>

따라서 magma들을 대상으로, magma homomorphism을 morphism으로 갖는 cartesian monoidal category $\Magma$가 존재한다.

대수학에서는 $f$의 image를 $f(A)$ 대신 $\im f$와 같이 적는 것이 보통이다. 임의의 $w,z\in\im f$를 택하자. 그럼 어떤 $x,y\in A$가 존재하여 $w=f(x)$이고, $z=f(y)$이다. 이제

$$w\star'z=f(x)\star'f(y)=f(x\star y)$$

이고, $x\star y\in A$이므로, $w\star'z\in\im f$가 성립한다.

이와 같이 연산에 대해 닫혀있는 마그마의 부분집합을 다음과 같이 정의한다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> 마그마 $(A,\star)$에 대하여, 만일 $A$의 어떤 부분집합 $S$가 $\star$에 대해 닫혀있다면, $S$를 $A$의 *부분마그마<sub>submagma</sub>*라고 부른다.

</div>

그럼 마그마 $(A,\star)$와 부분마그마들의 family $(S\_i)\_{i\in I}$에 대하여, 교집합 $S=\bigcap S\_i$ 또한 부분마그마가 되는 것은 자명하다. 임의의 $a,b\in S$를 택하면, 모든 $i$에 대해 $a,b\in S\_i$인 것으로부터 $a\star b\in S\_i$인 것을 얻고, 따라서 $a\star b\in S$이기 때문이다.

## 몫구조

집합 위에는 동치관계가 존재하므로, 마그마 위에도 동치관계를 정의할 수 있다. 그러나 함수와 마찬가지로, 모든 동치관계들이 우리의 관심의 대상인 것은 아니다.

마그마 $A$와 동치관계 $R$에 대하여 $x\equiv x'\pmod{R}$, $y\equiv y'\pmod{R}$가 성립한다 가정하자. $x$와 $x'$, 그리고 $y$와 $y'$가 $R$에 의해 같은 원소로 취급되고 있으므로, 다음의 식

$$x\star y\equiv x'\star y'\pmod{R}$$

을 기대하는 것이 합리적이다. 하지만 $R$에 어떤 조건도 걸려있지 않다면 이 식이 성립할 이유가 없다. 따라서, 다음과 같은 조건을 추가로 정의한다.

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> 마그마 $(A,\star)$ 위에 동치관계 $R$이 정의되었다고 하자. 임의의 $a\in A$에 대하여

$$x\equiv x'\implies a\star x\equiv a\star x'$$

을 만족한다면, $R$이 $\star$와 *left compatible*하다고 말한다. 비슷하게 만일 

$$x\equiv x'\implies x\star a\equiv x'\star a$$

가 모든 $a$에 대하여 성립한다면, $R$이 $\star$와 *right compatible*하다고 말한다. Left compatible인 동시에 right compatible인 동치관계를 간단히 *compatible*하다고 한다.
</div>

물론 위의 식에서 $\equiv$는 항상 관계 $R$에 대한 것을 뜻한다.

$R$이 동치관계라면 집합으로써 *몫집합* $A/R$이 잘 정의된다는 것은 이미 집합론에서 살펴본 적이 있다. ([\[집합론\] §동치관계, ⁋정의 4](/ko/math/set_theory/equivalence_relations#def4)) 집합 $A/R$ 위의 연산 $\tiny\char\"2606$을 정의하기 위한 가장 자연스러운 시도는

$$[x]\mathbin{\tiny\char"2606}[y]=[x\star y]$$

이다. 그러나 이 식이 의미를 갖기 위해서는, equivalence class $[x]$의 대표원소를 $x$ 대신 $x'$로 택하더라도 $[x]\mathbin{\tiny\char\"2606}[y]$의 값이 잘 정의되어야 한다. 즉, 다음의 식

$$[x\star y]=[x]\mathbin{\tiny\char"2606}[y]=[x'\star y]$$

가 성립해야 한다. 이 식은

$$x'\star y\equiv x\star y\mod R$$

로 바꾸어 쓸 수 있고, 앞선 정의를 따르자면 이는 정확히 $R$이 연산과 *right* compatible해야 한다는 의미다. 마찬가지 논리로, $[y]$의 대표원소의 선택에도 연산 $\mathbin{\tiny\char\"2606}$의 값이 변하지 않아야 하므로 $R$은 연산과 *left* compatible이어야 한다.

이를 정리하여 다음의 정의를 얻는다.

<div class="definition" markdown="1">

<ins id="def10">**정의 10**</ins> 마그마 $(A,\star)$ 위에 $\star$와 compatible한 동치관계 $R$이 주어졌다 하자. 위와 같이 얻어지는 마그마 $(A/R,\mathbin{\tiny\char\"2606})$을 *몫마그마<sub>quotient magma</sub>*라 부른다.

</div>

만일 $\star$가 결합법칙 혹은 교환법칙을 만족하면 $\mathbin{\tiny\char\"2606}$ 또한 그러하다는 것을 쉽게 확인할 수 있다. 위의 construction에서는 구별을 위해 $\star$와 $\mathbin{\tiny\char\"2606}$를 다르게 표기하였으나, 이들은 문맥상 쉽게 구별할 수 있으므로 몫마그마에서의 연산 또한 $\star$와 같이 적는 것이 보통이다.

---

**참고문헌**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  

---