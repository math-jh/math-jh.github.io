---

title: "준동형사상"
excerpt: "준동형사상의 정의와 성질들, 준동형사상의 핵과 상"

categories: [Math / Algebraic Structures]
permalink: /ko/math/algebraic_structures/group_homomorphisms
header:
    overlay_image: /assets/images/Algebraic_structures/Group_homomorphisms.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_structures-ko"
    
date: 2021-09-08
last_modified_at: 2022-11-30
weight: 4

---

## 준동형사상의 기본 성질들

[§준군, 모노이드, 군, ⁋정의 9](/ko/math/algebraic_structures/group#df9) 이후에 우리는 두 group $G,G'$ 사이의 임의의 magma homomorphism은 모두 group의 구조를 보존하는 것을 확인했다. 따라서 group homomorphism을 간단히 homomorphism이라 부르더라도 혼동의 여지가 없으므로, 이들을 구분할 필요가 없을 때에는 항상 간단한 이름으로 부르기로 한다.

<div class="proposition" markdown="1">

<ins id="pp1">**명제 1**</ins> 두 homomorphism의 합성 또한 homomorphism이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

두 homomorphism $f_1:G_0\rightarrow G_1$, $f_2:G_1\rightarrow G_2$가 주어졌다 하자. 그럼 임의의 $x, y\in G_0$에 대하여, 

$$(f_2\circ f_1)(xy)=f_2(f_1(xy))=f_2(f_1(x)f_1(y))=f_2(f_1(x))f_2(f_1(y))=(f_2\circ f_1)(x)(f_2\circ f_1)(y)$$

이므로 주어진 명제가 성립한다. 

</details>

또한, 항등함수가 homomorphism인 것은 증명할 것도 없이 자명하다. 한편 [§대수적 구조, ⁋정의 6](/ko/math/algebraic_structures/algebraic_structure#df6)으로부터 (group) isomorphism 또한 정의할 수 있는데, 이 정의와 [\[집합론\] §함수들 사이의 연산, ⁋명제 5](/ko/math/set_theory/operation_of_functions#pp5)로부터 임의의 isomorphism은 반드시 전단사함수여야 함이 자명하다. Group의 경우에는 그 역 또한 성립한다.

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> 임의의 homomorphism $f:G\rightarrow G'$가 isomorphism인 것은 $f$가 전단사인 것과 동치이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

반대쪽 방향만 보이면 충분하다. $f$는 전단사이므로, 함수로써 역함수 $f^{-1}:G'\rightarrow G$가 존재한다. 만일 $f^{-1}$이 homomorphism이기만 하다면, 정의에 의해 $f$는 isomorphism이 될 것이다.

임의의 $y, y'\in  G'$를 택하자. 그럼 $f$는 전단사이므로, 적당한 $x$, $x'$가 유일하게 존재하여 $f(x)=y$이고 $f(x')=y'$이다. 이제

$$f^{-1}(yy')=f^{-1}(f(x)f(x'))=f^{-1}(f(xx'))=xx'=f^{-1}(y)f^{-1}(y')$$

이므로, $f^{-1}$은 homomorphism이고 따라서 $f$는 isomorphism이다. 

</details>

## 준동형사상의 kernel과 image

앞서 우리는 임의의 magma homomorphism $f:A\rightarrow A'$이 주어졌을 때, 그 image $\im f$이 $A'$의 부분마그마가 되는 것을 확인했다. 일반적으로 group의 부분마그마는 subgroup일 필요가 없으므로, 다음의 명제는 별도로 증명해야 한다. 

<div class="proposition" markdown="1">

<ins id="pp3">**명제 3**</ins> 임의의 homomorphism $f:G\rightarrow G'$에 대하여, $\im f$는 $G'$의 subgroup이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$\im f$가 $G'$의 부분마그마인 것은 이미 알고 있으므로, [§준군, 모노이드, 군, ⁋명제 12](/ko/math/algebraic_structures/group#pp12)를 이용하면 $\im f$가 역원을 취하는 것에 대해 닫혀있음만 보이면 된다. $y\in\im f$라 하고, $x\in G$가 $f(x)=y$를 만족한다 하자. 그럼

$$f(x^{-1})=f(x)^{-1}=y^{-1}$$

로부터 $y^{-1}\in\im f$임을 안다.

</details>

앞서 언급한 것과 같이 group homomorphism $f:G\rightarrow G'$은 정의역과 공역이 모두 group이라는 것만 제외하면 magma homomorphism과 크게 다를 것이 없다. 그러나 이 작은 차이가 group homomorphism에 흥미로운 구조를 많이 주게 된다. 가령 $f$가 단사함수라는 것은 다음과 같이 표현할 수 있다.

<div class="proposition" markdown="1">

<ins id="pp4">**명제 4**</ins> Homomorphism $f:G\rightarrow G'$가 단사함수인 것은 $f^{-1}(e')=\\{e\\}$인 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$f$가 단사함수라면 $f^{-1}(e')=\\{e\\}$여야 하는 것은 자명하다.

거꾸로 $f^{-1}(e')=\\{e\\}$가 성립한다 가정하자. $f(x)=f(y)$를 만족하는 $x,y\in G$가 주어졌다 하면,

$$e'=f(x)f(y)^{-1}=f(xy^{-1})$$

이며, 가정에 의해 $xy^{-1}=e$이다. 이로부터 $x=y$임을 안다.

</details>

임의의 homomorphism $f:G\rightarrow G'$에 대하여, 위의 집합 $f^{-1}(e')$는 $f$가 단사함수로부터 얼마나 멀리 떨어져 있는지를 보여준다. 이 집합을 다음과 같이 부른다.

<div class="definition" markdown="1">

<ins id="df5">**정의 5**</ins> Homomorphism $f:G\rightarrow G'$의 *kernel<sub>핵</sub>*을 집합 $f^{-1}(e')$으로 정의하고, $\ker f$로 적는다.

</div>

그럼 $f^{-1}(e')$는 단순한 집합일 뿐만 아니라, $G$의 subgroup이 된다.

<div class="proposition" markdown="1">

<ins id="pp6">**명제 6**</ins> 임의의 homomorphism $f:G\rightarrow G'$에 대하여, $\ker f$는 $G$의 subgroup이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $a,b\in \ker f$에 대하여, 

$$f(ab^{-1})=f(a)f(b)^{-1}=e'(e')^{-1}=e'$$

이므로 $ab^{-1}\in\ker f$가 성립한다.

</details>



---

**참고문헌**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  

---

[^1]: 지저분한 notation을 피하기 위해 $a\ker f$ 대신 $\bar{a}$로 적었다.
