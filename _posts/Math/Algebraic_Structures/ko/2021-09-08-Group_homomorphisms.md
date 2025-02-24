---

title: "군 준동형사상"
excerpt: "군 준동형사상의 정의와 성질들, 군 준동형사상의 핵과 상"

categories: [Math / Algebraic Structures]
permalink: /ko/math/algebraic_structures/group_homomorphisms
header:
    overlay_image: /assets/images/Math/Algebraic_Structures/Group_homomorphisms.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_structures-ko"
    
date: 2021-09-08
last_modified_at: 2022-11-30
weight: 4

---

당분간 우리는 group의 성질들을 탐구한다. 따라서 group들 사이의 group homomorphism도 간단히 homomorphism이라고만 칭하기로 한다.

[§대수적 구조, ⁋정의 6](/ko/math/algebraic_structures/algebraic_structures#def6)으로부터 (group) isomorphism 또한 정의할 수 있는데, 이 정의와 [\[집합론\] §함수들 사이의 연산, ⁋명제 4](/ko/math/set_theory/operation_of_functions#prop4)로부터 임의의 isomorphism은 반드시 전단사함수여야 함이 자명하다. 많은 경우에는 그 역 또한 성립한다.

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1**</ins> 임의의 magma homomorphism $f:A\rightarrow A'$가 isomorphism인 것은 $f$가 전단사인 것과 동치이다. 

만일 $A$가 항등원 $e$를 갖고, $f:A\rightarrow A'$가 전단사함수라면 $f(e)$는 $A'$의 항등원이며, 따라서 $f^{-1}$은 $A'$의 항등원을 $A$의 항등원으로 보내는 magma homomorphism이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

반대쪽 방향만 보이면 충분하다. $f$는 전단사이므로, 함수로써 역함수 $f^{-1}:G'\rightarrow G$가 존재한다. 만일 $f^{-1}$이 homomorphism이기만 하다면, 정의에 의해 $f$는 isomorphism이 될 것이다.

임의의 $y, y'\in  A'$를 택하자. 그럼 $f$는 전단사이므로, 적당한 $x$, $x'$가 유일하게 존재하여 $f(x)=y$이고 $f(x')=y'$이다. 이제

$$f^{-1}(yy')=f^{-1}(f(x)f(x'))=f^{-1}(f(xx'))=xx'=f^{-1}(y)f^{-1}(y')$$

이므로, $f^{-1}$은 homomorphism이고 따라서 $f$는 isomorphism이다. 

한편 $f:A\rightarrow A'$가 전단사함수라면, 임의의 $y\in A'$에 대하여 $f(x)=y$를 만족하는 유일한 $x\in A$가 존재한다. 이제

$$y=f(x)=f(xe)=f(x)f(e),\qquad y=f(x)=f(ex)=f(e)f(x)$$

이므로 $f(e)$는 $A'$의 항등원이다.

</details>

## 준동형사상의 equalizer

다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> Group homomorphism $f,g:G \rightarrow H$가 주어졌다 하자. 그럼

$$\Eq(f,g)=\{x\in G\mid f(x)=g(x)\}$$

은 $G$의 subgroup이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

만일 $x,y\in \Eq(f,g)$라면,

$$f(xy^{-1})=f(x)f(y)^{-1}=g(x)g(y)^{-1}=g(xy^{-1})$$

이므로 $xy^{-1}\in\Eq(f,g)$이다. 따라서 [§반군, 모노이드, 군, ⁋명제 15](/ko/math/algebraic_structures/groups#prop15)에 의해 원하는 결과를 얻는다. 

</details>

이렇게 정의한 $i:\Eq(f,g)\rightarrow G$는 다음과 같은 성질을 가진다.

> 만일 group homomorphism $j:G' \rightarrow G$가 $f\circ j=g\circ j$를 만족한다면, 유일한 homomorphism $j': G' \rightarrow G$가 존재하여 $i\circ j'=j$이다.

이는 정의에 의해 $j$의 image가 $\Eq(f,g)$에 포함되기 때문이다. 따라서 $\Grp$의 임의의 morphism은 equalizer를 갖는다. ([\[범주론\] §극한, ⁋예시 7](/ko/math/category_theory/limits#ex7)) 사실 $\Grp$의 임의의 morphism은 coequalizer 또한 갖지만, 이를 정의하기 위해서는 normal subgroup과 quotient group을 먼저 정의해야 한다. 

## 준동형사상의 kernel과 image

Group $\\{e\\}$는 category $\Grp$의 zero object이다. 따라서 임의의 group $G,H$에 대하여 zero map $e:G \rightarrow H$가 합성 $G\rightarrow\\{e\\}\rightarrow H$로 정의된다. 

한편, group homomorphism $f$가 단사함수라는 것은 다음과 같이 표현할 수 있다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> Homomorphism $f:G\rightarrow G'$가 단사함수인 것은 $f^{-1}(e')=\\{e\\}$인 것과 동치이다.

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

<ins id="def4">**정의 4**</ins> Homomorphism $f:G\rightarrow G'$의 *kernel<sub>핵</sub>*을 집합 $f^{-1}(e')$으로 정의하고, $\ker f$로 적는다.

</div>

그럼 $f^{-1}(e')$는 단순한 집합일 뿐만 아니라, $G$의 subgroup이 된다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> 임의의 homomorphism $f:G\rightarrow G'$에 대하여, $\ker f$는 $G$의 subgroup이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

정의에 의해 $\ker f=\Eq(f,e)$이다.

</details>

한편, 우리는 임의의 magma homomorphism $f:A\rightarrow A'$이 주어졌을 때, 그 image $\im f$이 $A'$의 부분마그마가 되는 것을 확인했다. ([§대수적 구조, ⁋정의 8](/ko/math/algebraic_structures/algebraic_structures#def8) 이전의 계산) 그러나 일반적으로 group의 부분마그마는 subgroup일 필요가 없으므로, 다음의 명제는 별도로 증명해야 한다. 

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> 임의의 homomorphism $f:G\rightarrow G'$에 대하여, $\im f$는 $G'$의 subgroup이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$\im f$가 $G'$의 부분마그마인 것은 이미 알고 있으므로, [§반군, 모노이드, 군, ⁋명제 15](/ko/math/algebraic_structures/groups#prop15)를 이용하면 $\im f$가 역원을 취하는 것에 대해 닫혀있음만 보이면 된다. $y\in\im f$라 하고, $x\in G$가 $f(x)=y$를 만족한다 하자. 그럼

$$f(x^{-1})=f(x)^{-1}=y^{-1}$$

로부터 $y^{-1}\in\im f$임을 안다.

</details>


---

**참고문헌**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  

---

[^1]: 지저분한 notation을 피하기 위해 $a\ker f$ 대신 $\bar{a}$로 적었다.
