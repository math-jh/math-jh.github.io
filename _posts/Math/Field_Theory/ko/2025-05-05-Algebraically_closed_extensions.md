---

title: "대수적 폐포"
excerpt: ""

categories: [Math / Field Theory]
permalink: /ko/math/field_theory/algebraically_closed_extensions
header:
    overlay_image: /assets/images/Math/Field_Theory/Algebraically_closed_extensions.png
    overlay_filter: 0.5
sidebar: 
    nav: "field_theory-ko"

date: 2025-05-05
last_modified_at: 2025-05-05
weight: 3

---

우리는 앞선 글에서 algebraic extension이 어떠한 것인지를 정의했다. 우선 다음 명제를 보자.

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1**</ins> Field $\mathbb{K}$에 대하여 다음이 모두 동치이다. 

1. $\mathbb{K}[\x]$의 임의의 non-constant polynomial은 항상 일차식들의 곱으로 나타난다. 
2. $\mathbb{K}[\x]$의 임의의 non-constant polynomial은 항상 적어도 하나의 근을 갖는다. 
3. $\mathbb{K}[\x]$의 irreducible polynomial은 일차식 뿐이다. 
4. $\mathbb{K}$의 임의의 algebraic extension은 항상 degree $1$이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 첫째 조건과 둘째 조건이 동치임은 자명하다. 만일 첫째 조건이 성립한다면 셋째 조건이 성립하는 것은 자명하다. 또, [\[환론\] §다항식환, ⁋명제 6](/ko/math/ring_theory/polynomial_rings#prop6)에 의하여 $\mathbb{K}[\x]$의 임의의 원소는 irreducible polynomial의 곱으로 나타낼 수 있고, 일차식은 자명한 이유로 $\mathbb{K}$ 안에서 근을 가지므로 셋째 조건이 둘째 조건을 함의한다. 따라서 첫째 조건부터 셋째 조건까지가 모두 동치이다.

이제 셋째 조건과 넷째 조건이 동치임을 보이자. 우선 셋째 조건이 성립한다 가정하면, 우리는 algebraic extension $\mathbb{L}/\matbb{K}$의 임의의 원소 $x$의 minimal polynomial이 irreducible이므로 ([§대수적 확장, ⁋정리 15](/ko/math/field_theory/algebraic_extensions#thm15)) 셋째 조건으로부터 이 minimal polynomial이 일차식이어야 함을 안다. 

이제 넷째 조건을 가정하자. $\mathbb{K}[\x]$의 irreducible polynomial $f$에 대하여, $\mathbb{K}[\x]/(f)$를 생각하면 이는 $\mathbb{K}$의 degree $n$ algebraic extension이다. 우리는 이 extension의 degree가 $1$이어야 함을 가정하고 있으므로, 셋째 조건이 얻어진다. 

</details>

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 위의 동치조건을 만족하는 field $\mathbb{K}$를 *algebraically closed field<sub>대수적으로 닫힌 체</sub>*라 부른다. 

</div>

만일 field extension $\Omega/\mathbb{K}$에 대하여, $\Omega$의 원소 중 $\mathbb{K}$에 대해 algebraic 한 것들이 모두 $\mathbb{K}$에 속한다면 $\mathbb{K}$가 $\Omega$에서 *relatively algebraically closed field<sub>상대적으로 대수적으로 닫힌 체</sub>*라 부른다. 일반적으로 relatively algebraically closed field는 algebraically closed일 필요가 없지만, 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> Algebraically closed field $\Omega$와 subfield $\mathbb{K}$에 대하여, $\mathbb{K}$의 $\Omega$에서의 relative algebraic closure $\overline{\mathbb{K}}$는 algebraically closed field이다. 

</div>

이는 임의의 $f\in \overline{\mathbb{K}}[\x]$가 주어졌을 때, $f$는 $\Omega[\x]$의 원소로 볼 수도 있으므로 $\Omega$가 algebraically closed라는 가정으로부터 $f$의 $\Omega$에서의 한 근을 찾을 수 있고, 이 근이 $\overline{\mathbb{K}}$에 속해야 하기 때문이다. 다음 사실은 소수가 무한하다는 유클리드의 증명을 활용한 것이다. 

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> 임의의 algebraically closed field는 무한하다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

결론에 반하여 $\Omega$가 finite algebraically closed field라 하고, 다음의 다항식

$$1+\prod_{a\in \Omega}(\x-a)$$

을 생각하자. 이 다항식은 어떠한 $a$도 근으로 갖지 않는다. 

</details>

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5**</ins> Algebraic extension $\mathbb{L}/\mathbb{K}$가 주어졌다 하고, $\Omega$가 $\mathbb{K}$의 algebraically closed  extension이라 하자. 그럼 $\mathbb{L}/\mathbb{K}$에서 $\Omega/\mathbb{K}$로의 morphism이 존재한다. 

</div>

이에 대한 증명은 [§대수적 확장, ⁋명제 8](/ko/math/field_theory/algebraic_extensions#prop8)로부터 자명하다. 

## 분해확대체

위에서 살펴본 algebraically closed extension을 constructive하게 얻어낼 생각을 해 보면, 우리는 다음의 정의를 해야 함을 안다. 

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> Field $\mathbb{K}$와 다항식들 $f_i\in \mathbb{K}[\x]$에 대하여, 이들 다항식들의 *splitting extension<sub>분해확대체</sub>*는 다음의 조건을 만족하는 field extension $\mathbb{L}/\mathbb{K}$이다. 

1. 모든 $f_i$들이 $\mathbb{L}[\x]$에서 일차식의 곱으로 인수분해된다.  
2. 각각의 $i$에 대하여, $R_i$를 $\mathbb{L}$에서 $f_i$들의 근들이 모임이라 하면 $\mathbb{L}=\mathbb{K}(\bigcup R_i)$이다. 

</div>

그럼 splitting extension의 존재성을 증명해야 한다. 

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> Field $\mathbb{K}$와 다항식들 $f_i\in \mathbb{K}[\x]$에 대하여, 이들 다항식들의 splitting extension이 존재한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Algebraic extension을 할 때는 어차피 다항식의 근만이 중요하므로, 주어진 다항식들 $f_i$들이 모두 monic polynomial이라 가정하여도 된다. 각각의 $f_i$가 degree $d_i$ monic polynomial이라 하자. 그럼 [\[다중선형대수학\] §대칭텐서, ⁋명제 13](/ko/math/multilinear_algebra/symmetric_tensors#prop13)에 의하여, 각각의 $i$마다 다음의 두 조건

1. $A_i$는 $\mathbb{K}$-algebra로서 $\xi_{i,1},\ldots, \xi_{i, d_i}$에 의해 생성된다. 
2. $A_i[\x]$에서 $f_i(\x)=\prod_{k=1}^{d_i} (\x-\xi_{i,k})$이 성립한다. 

을 만족하는 $\mathbb{K}$-algebra $A_i$, 원소들 $\xi_{i,1},\ldots, \xi_{i, d_i}\in A_i$를 잡아줄 수 있다. 

이제 이들을 이용하여 $\mathbb{K}$의 extension을 만들어야 한다. 

$$A=\bigotimes_{i\in I} A_i$$

이라 하면, Krull theorem에 의하여 $A$의 maximal ideal $\mathfrak{m}$이 존재하므로 $\mathbb{L}=A/\mathfrak{m}$이라 할 수 있으며, 이것이 원하는 splitting extension을 준다. 

</details>

뿐만 아니라, splitting extension은 다음과 같은 센스에서 유일하다. 

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> Field $\mathbb{K}$와 다항식들 $f_i\in \mathbb{K}[\x]$이 주어졌다 하고, extension $\Omega/\mathbb{K}$를 고정하자. 만일 두 subextension $\mathbb{L}_1$, $\mathbb{L}_2$가 이들의 splitting extension이라면, $\mathbb{L}_1=\mathbb{L}_2$이다. 

</div>

## 대수적 폐포

이제 다음을 정의한다. 

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> Field $\mathbb{K}$의 *algebraic closure*는 $\mathbb{K}$의 algebraic extension 중 그 자체로 algebraically closed인 것을 뜻한다. 

</div>

Algebraic closure의 존재성을 보이기 위해서 $\mathbb{K}[\x]$의 모든 (non-constant) 다항식들의 splitting field $\Omega$를 생각하는 것이 자연스러울 것이다. 그러나 $\Omega$가 algebraically closed임을 보이려면, $\mathbb{K}$에서 넣어준 근들을 계수로 갖는 다항식의 근들 또한 다시 $\Omega$에 속한다는 것을 보여야 하므로 이는 그렇기게 간단하지는 않다. 다음 명제는 이러한 상황을 고민할 필요가 없다는 것을 보여준다. 

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> Algebraic extension $\Omega/\mathbb{K}$가 algebraically closed인 것은 $\mathbb{K}[\x]$의 임의의 non-constant polynomial이 $\Omega[\x]$ 안에서 일차식의 곱으로 인수분해되는 것과 동치이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

당연히 한쪽 방향만 보이면 충분하다. 이를 위해 $\Omega$의 임의의 algebraic extension $\Omega'$를 잡고, $x\in\Omega'$라 하자. 우리는 $x\in \Omega$임을 보여야 한다. 우선 $x$는 $\Omega$에 대해 algebraic이고, $\Omega/\mathbb{K}$가 algebraic이므로 $x$는 $\mathbb{K}$에 대해서도 algebraic이다. 이제 $u\in \mathbb{K}[\x]$를 $x$의 minimal polynomial이라 하면, $u$는 $\Omega[\x]$에서 일차식들의 곱으로 쪼개지며 따라서 $x\in \Omega$이다. 

</details>

따라서, 주어진 field $\mathbb{K}$의 algebraic closure를 찾기 위해서는 $\mathbb{K}$의 임의의 non-constant polynomial들의 splitting field를 생각하면 된다. 이는 [명제 8](#prop8)에 의해 반드시 유일하다. 

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> Field $\mathbb{K}$의 algebraic extension $\Omega/\mathbb{K}$에 대하여 다음이 성립한다.

1. 만일 $\Omega$가 algebraically closed라면, $\mathbb{K}$의 임의의 algebraic extension은 $\Omega/\mathbb{K}$의 어떠한 subextension과 isomorphic하다.
2. 거꾸로, 만일 $\mathbb{K}$의 임의의 finite degree algebraic extension이 $\Omega$의 subextension과 isomorphic하다면 $\Omega$는 algebraically closed이다. 

</div>

따라서 $\mathbb{K}$의 algebraic closure는 isomorphism에 대해 유일하게 존재한다. 이를 $\bar{\mathbb{K}}$로 적는다. 

## 제곱근 확장

Field $\mathbb{K}$의 characteristic이 $0$인 경우 우리는 $\mathbb{K}$의 characteristic exponent가 1이라 정의하였고, 그 외 $\mathbb{K}$의 characteristic exponent는 $\char \mathbb{K}$와 같은 것으로 두었다. 다음 글에서 