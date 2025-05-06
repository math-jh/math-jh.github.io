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

이는 임의의 $f\in \overline{\mathbb{K}}[\x]$가 주어졌을 때, $f$는 $\Omega[\x]$의 원소로 볼 수도 있으므로 $\Omega$가 algebraically closed라는 가정으로부터 $f$의 $\Omega$에서의 한 근을 찾을 수 있고, 이 근이 $\overline{\mathbb{K}}$에 속해야 하기 때문이다. 

다음 사실은 소수가 무한하다는 유클리드의 증명으로부터 거의 자명하다. 

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> 임의의 algebraically closed field는 무한하다. 

</div>

즉, 다항식 $1+\prod_{a\in\Omega}(\x-a)$를 생각하면 된다. 

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



</details>

뿐만 아니라, splitting extension은 다음과 같은 센스에서 유일하다. 

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> Field $\mathbb{K}$와 다항식들 $f_i\in \mathbb{K}[\x]$이 주어졌다 하고, extension $\Omega/\mathbb{K}$를 고정하자. 만일 두 subextension $\mathbb{L}_1$, $\mathbb{L}_2$가 이들의 splitting extension이라면, $\mathbb{L}_1=\mathbb{L}_2$이다. 

</div>