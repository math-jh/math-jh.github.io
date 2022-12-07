---

title: "대칭대수와 외대수"
excerpt: "대칭대수와 외대수의 정의, universal property와 성질들"

categories: [Math / Tensor algebra]
permalink: /ko/math/tensor_algebra/symmetric_and_exterior_algebras
header:
    overlay_image: /assets/images/Tensor_algebra/Symmetric_and_exterior_algebras.png
    overlay_filter: 0.5
sidebar: 
    nav: "tensor_algebra-ko"

date: 2022-12-06
last_modified_at: 2022-12-06
weight: 4

---

## 대칭대수와 외대수

Tensor algebra $\mathcal{T}(M)$은 그 자체로도 흥미로운 대수적 대상이지만, 특별히 $\mathcal{T}(M)$에서 만들어지는 두 quotient algebra 구조가 중요하다. 

우선 임의의 $x,y\in M$에 대해, commutator $x\otimes y-y\otimes x$으로 생성되는 two-sided ideal $\mathfrak{a}$를 생각하자. 특히 $\mathfrak{a}$는 차수 2짜리 homogeneous element들로 생성되므로, [§등급대수, 보조정리 2](/ko/math/tensor_algebra/graded_homomorphism#lem2)에 의해 $\mathfrak{a}$는 graded ideal이고 따라서 $\mathcal{T}(M)/\mathfrak{a}$는 graded algebra 구조를 갖는다. 

이번에는 임의의 $x\in M$에 대하여, $x\otimes x$들로 생성되는 two-sided ideal $\mathfrak{b}$를 생각하자. 그럼 마찬가지로 $\mathfrak{b}$는 차수 2짜리 homogeneous element들로 생성되므로 graded ideal이다. 따라서 $\mathcal{T}(M)/\mathfrak{b}$ 또한 graded algebra 구조를 갖는다.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 위의 논의에서, quotient algebra $\mathcal{T}(M)/\mathfrak{a}$를 $M$의 *symmetric algebra<sub>대칭대수</sub>*, 그리고 $\mathcal{T}(M)/\mathfrak{b}$를 $M$의 *exterior algebra<sub>외대수</sub>*라 부른다. $M$의 symmetric algebra는 $\mathcal{S}(M)$, 그리고 $M$의 exterior algebra는 $\bigwedge(M)$으로 표기한다.

</div>

## 대칭대수

편의상 quotient map $\mathcal{T}(M)\rightarrow\mathcal{T}(M)/\mathfrak{a}=\mathcal{S}(M)$을 $p$로 표기하고, $p\circ\iota:M\rightarrow \mathcal{S}(M)$을 $q$로 표기하자. 

### 대칭대수의 universal property 

다음은 symmetric algebra $\mathcal{S}(M)$의 가장 기초적인 성질이다.

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> $\mathcal{S}(M)$은 commutative algebra이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $x,y\in M$에 대하여, 

$$q(x)q(y)-q(y)q(x)=(p\circ\iota)(x)(p\circ\iota)(y)-(p\circ\iota)(y)(p\circ\iota)(x)=p(\iota(x)\iota(y)-\iota(y)\iota(x))=0$$

가 성립한다. 한편 $\mathcal{S}(M)$은 $q(x)$들로 생성되고, 이러한 원소들이 모두 commute하므로 원하는 명제가 성립한다.

</details>

뿐만 아니라, 다음의 universal property로부터 $\mathcal{S}(M)$을 이러한 성질을 갖는 가장 작은 $A$-algebra로 생각할 수도 있다.

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3**</ins> $A$-module $M$을 고정하고, $A$-algebra $E$로의 $A$-module homomorphism $f:M\rightarrow E$가 모든 $x,y\in M$에 대해 $f(x)f(y)=f(y)f(x)$를 만족한다 하자. 그럼 다음 diagram을 commute하도록 하는 유일한 $A$-algebra homomorphism $\tilde{f}:\mathcal{S}(M)\rightarrow E$가 존재한다.

![universal_property_of_symmetric_algebra](/assets/images/Tensor_algebra/Symmetric_and_exterior_algebra-1.png){:width="164.55px" class="invert" .align-center}

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[명제 2](#pp2)의 증명과 같이, $\mathcal{S}(M)$들은 $q(x)$들로 생성되므로 $\tilde{f}$는 유일해야 한다는 것이 자명하다. 따라서 존재성만 증명하면 충분하다. 

Tensor algebra $\mathcal{T}(M)$의 universal property에 의하여, 다음 diagram을 commute하도록 하는 유일한 $A$-algebra homomorphism $\mathcal{T}(M)\rightarrow E$가 존재한다. 

![universal_property_of_tensor_algebra](/assets/images/Tensor_algebra/Symmetric_and_exterior_algebra-2.png){:width="166.95px" class="invert" .align-center}

그런데 주어진 조건 $f(x)f(y)-f(y)f(x)=0$에 의해 이 함수의 kernel이 $\mathfrak{a}$를 포함하므로, 다음의 diagram

![first_isomorphism](/assets/images/Tensor_algebra/Symmetric_and_exterior_algebra-3.png){:width="182.25px" class="invert" .align-center}

을 commute하도록 하는 유일한 $\mathcal{T}(M)/\mathfrak{a}\rightarrow E$가 존재한다. 이로부터 원하는 결과를 얻는다.

</details>

다음 따름정리들은 universal property로부터 쉽게 유도할 수 있다.

<div class="proposition" markdown="1">

<ins id="crl4">**따름정리 4**</ins> 임의의 $A$-module homomorphism $u:M \rightarrow N$에 대하여, 다음 diagram

![Functoriality_of_symmetric_algebra](/assets/images/Tensor_algebra/Symmetric_and_exterior_algebra-4.png){:width="192px" class="invert" .align-center}

을 commute하도록 하는 유일한 $A$-algebra homomorphism $\mathcal{S}(u)$이 존재한다.

</div>

<div class="proposition" markdown="1">

<ins id="crl5">**따름정리 5**</ins> [따름정리 4](#crl4)에서 정의된 $\mathcal{S}(u)$는 합성을 보존한다. 즉 $\mathcal{S}(v\circ u)=\mathcal{S}(v)\circ\mathcal{S}(u)$가 성립한다.

</div>

### Change of base ring

이제 tensor algebra때와 마찬가지로 스칼라들이 변했을 때 $\mathcal{S}(M)$이 어떻게 변하는지를 살펴본다. 우선 ring homomorphism $\rho:A \rightarrow A'$가 주어졌다 하고, $A$-module $M$, $A'$-module $M'$이 주어졌다 하자. $M'$과 $\mathcal{S}\_{A'}(M')$ 각각을 $A$-module과 $A$-algebra로 생각하면, canonical map $q\_{M'}:M'\rightarrow\mathcal{S}\_{A'}(M')$ 또한 $A$-module homomorphism으로 생각할 수 있다. 

이제 임의의 $A$-module homomorphism $u:M \rightarrow M'$에 대하여, $q\_{M'}\circ u$ 또한 $A$-module homomorphism이고, $q\_{M'}$의 성질로부터 [정리 3](#thm3)의 조건

$$(q_{M'}\circ u)(x)(q_{M'}\circ u)(y)=(q_{M'}\circ u)(y)(q_{M'}\circ u)(x)\qquad\text{for all $x,y\in M'$}$$

이 만족되는 것을 알 수 있다. 이제 symmetric algebra의 universal property로부터 $A$-module들의 diagram

![Restriction_of_scalars](/assets/images/Tensor_algebra/Symmetric_and_exterior_algebra-5.png){:width="231.75px" class="invert" .align-center}

이 commute하도록 하는 유일한 $\mathcal{S}\_A(M)\rightarrow\mathcal{S}\_{A'}(M')$이 존재한다. 약간의 abuse of notation을 통해 이 또한 $\mathcal{S}(u)$로 표기한다.

거꾸로 임의의 $A$-module $M$에 대하여, $A'\otimes_AM$은 자연스러운 $A'$-module 구조를 갖는다. 이 module의 symmetric algebra $\mathcal{S}_{A'}(A'\otimes_AM)$을 생각하면, 다음의 $A'$-module homomorphism

$${\operatorname{id}_{A'}}\otimes q_M:A'\otimes_AM\rightarrow A'\otimes_A\mathcal{S}_A(M)$$

은 임의의 $a'\otimes x,b'\otimes y\in A'\otimes_AM$에 대하여

$$\begin{aligned}({\operatorname{id}_{A'}}\otimes q_M)(a'\otimes x)({\operatorname{id}_{A'}}\otimes q_M)(b'\otimes y)&=(a'\otimes q_M(x))(b'\otimes q_M(y))\\
&=(a'b')\otimes (q_M(x)q_M(y))\\
&=(b'a')\otimes (q_M(y)q_M(x))\\
&=(a'\otimes q_M(x))(b'\otimes q_M(y))\\
&=({\operatorname{id}_{A'}}\otimes q_M)(b'\otimes y)({\operatorname{id}_{A'}}\otimes q_M)(a'\otimes x)\end{aligned}$$

을 만족하고, 따라서 $A'\otimes_AM$의 모든 원소에 대하여 [정리 3](#thm3)의 조건이 만족된다. 이로부터 유일한 $A'$-module homomorphism $\mathcal{S}_{A'}(A'\otimes_AM)\rightarrow A'\otimes_A\mathcal{S}_A(M)$을 얻는다.

![Extension_of_scalars](/assets/images/Tensor_algebra/Symmetric_and_exterior_algebra-6.png){:width="306px" class="invert" .align-center}

다음 명제는 [§텐서대수, 대칭대수와 외대수, 명제 6](/ko/math/tensor_algebra/tensor_algebra#pp6)과 마찬가지로 증명할 수 있으며, universal property를 보이기 위해서는 위와 같은 방식으로 $q$를 사용하면 된다.
<div class="proposition" markdown="1">

<ins id="pp6">**명제 6**</ins> 위에서 정의한 $\mathcal{S}_{A'}(A'\otimes_AM)\rightarrow A'\otimes_A\mathcal{S}_A(M)$는 isomorphism이다.

</div>

### 직합의 대칭대수

[§텐서대수, 대칭대수와 외대수](/ko/math/tensor_algebra/tensor_algebra)에서도 $\mathcal{T}(M)$에 대하여 다음 명제와 비슷한 명제를 만들 수 있었을 것이나, 우변이 더 복잡하고 식 자체로는 별 의미가 없어 다루지 않았던 것이다.

<div class="proposition" markdown="1">

<ins id="pp7">**명제 7**</ins> $A$-module들의 유한한 family $(M\_i)\_{1\leq i\leq n}$가 주어졌다 하자. 그럼 $M=\bigoplus M\_i$에 대하여, 

$$\mathcal{S}(M)\cong\bigotimes_{i=1}^n\mathcal{S}(M_i)$$

이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Direct sum으로의 canonical injection $\iota\_i:M\_i\rightarrow M$에 대하여, $\mathcal{S}(\iota\_i):\mathcal{S}(M\_i)\rightarrow\mathcal{S}(M)$들이 잘 정의된다. 또, $\mathcal{S}(M)$이 commutative algebra이므로

$$\mathcal{S}(M_1)\times\cdots\times\mathcal{S}(M_n)\rightarrow\mathcal{S}(M)$$

를 $\mathcal{S}(\iota_1)\times\cdots\times\mathcal{S}(\iota_n)$으로 정의해도 문제가 생기지 않는다. 따라서 tensor product의 universal property에 의하여 

$$\bigotimes_{i=1}^n\mathcal{S}(M_i)\rightarrow \mathcal{S}(M)$$

이 잘 정의된다. 

이제 이 함수의 역함수를 만들어야 한다. 우선 각각의 $i$에 대하여, canonical map들의 합성

$$M_i\rightarrow\mathcal{S}(M_i)\rightarrow\bigotimes_{i=1}^n \mathcal{S}(M_i)$$

을 생각할 수 있다. 이제 direct sum의 universal property로부터

$$\bigoplus_{i=1}^n M_i=M\rightarrow\bigotimes_{i=1}^n\mathcal{S}(M_i)$$

를 얻는다. 이제 $\bigotimes\mathcal{S}(M_i)$는 commutative algebra이므로 [정리 2](#thm2)의 조건이 자명하게 성립하고, 따라서 이로부터 

$$\mathcal{S}(M)\rightarrow\bigotimes_{i=1}^n\mathcal{S}(M_i)$$

를 얻는다.

</details>

## 외대수

위에서 증명한 명제들을 외대수에 대해서도 반복할 수 있다. 증명은 모두 대칭대수와 비슷하므로 생략하기로 한다. Exterior algebra로의 canonical map은 symmetric algebra와 마찬가지로 canonical map들의 합성

$$M\rightarrow \mathcal{T}(M)\rightarrow\mathcal{T}(M)/\mathfrak{b}=\bigwedge(M)$$

으로 주어지며, 불필요한 문자낭비를 막기 위해 이 함수에 대한 별도의 문자를 지정하지는 않기로 한다.

### 외대수의 universal property

<div class="proposition" markdown="1">

<ins id="pp8">**명제 8**</ins> $A$-module $M$을 고정하고, $A$-algebra $E$로의 $A$-module homomorphism $f:M\rightarrow E$가 모든 $x\in M$에 대해 $f(x)^2=0$를 만족한다 하자. 그럼 다음 diagram을 commute하도록 하는 유일한 $A$-algebra homomorphism $\tilde{f}:\bigwedge(M)\rightarrow E$가 존재한다.

![Universal_property_of_exterior_algebra](/assets/images/Tensor_algebra/Symmetric_and_exterior_algebra-7.png){:width="167.7px" class="invert" .align-center}

</div>

<div class="proposition" markdown="1">

<ins id="crl9">**따름정리 9**</ins> 임의의 $A$-module homomorphism $u:M \rightarrow N$에 대하여, 다음 diagram

![Functoriality_of_exterior_algebra](/assets/images/Tensor_algebra/Symmetric_and_exterior_algebra-8.png){:width="207.9px" class="invert" .align-center}

을 commute하도록 하는 유일한 $A$-algebra homomorphism $\bigwedge(u)$이 존재한다.

</div>

<div class="proposition" markdown="1">

<ins id="crl10">**따름정리 10**</ins> [따름정리 9](#crl9)에서 정의된 $\mathcal{S}(u)$는 합성을 보존한다. 즉 $\mathcal{S}(v\circ u)=\mathcal{S}(v)\circ\mathcal{S}(u)$가 성립한다.

</div>

### Change of base ring

위에서 다룬 대칭대수의 [Change of base ring](/ko/math/tensor_algebra/symmetric_algebra#change-of-base-ring)과 같은 상황을 가정하자. 그럼 다음 $A$-module들의 diagram

![Restriction_of_scalars](/assets/images/Tensor_algebra/Symmetric_and_exterior_algebra-9.png){:width="241.35px" class="invert" .align-center}

을 commute하도록 하는 $\bigwedge(u):\bigwedge\nolimits_A(M)\rightarrow\bigwedge\nolimits_{A'}(M')$이 존재한다. 또, [명제 6](#pp6)과 비슷하게 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="pp11">**명제 11**</ins> 두 ring $A,A'$, 그리고 $A$-module $M$에 대하여

$$\bigwedge\nolimits_{A'}(A'\otimes_AM)\cong A'\otimes_A\bigwedge\nolimits_A(M)$$

이 성립한다.

</div>

### 직합의 외대수

마지막으로 다음 명제 또한 성립한다.

<div class="proposition" markdown="1">

<ins id="pp12">**명제 12**</ins> $A$-module들의 유한한 family $(M\_i)\_{1\leq i\leq n}$가 주어졌다 하자. 그럼 $M=\bigoplus M\_i$에 대하여, 

$$\bigwedge(M)\cong\bigotimes_{i=1}^n\bigwedge(M_i)$$

이 성립한다.

</div>