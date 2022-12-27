---

title: "아벨 카테고리"
excerpt: "아벨 카테고리"

categories: [Math / Category Theory]
permalink: /ko/math/category_theory/abelian_categories
header:
    overlay_image: /assets/images/Category_theory/Abelian_categories.png
    overlay_filter: 0.5
sidebar: 
    nav: "category_theory-ko"

date: 2022-12-21
last_modified_at: 2022-12-21
weight: 4

---

아벨 카테고리의 개념은 [호몰로지 대수학](/ko/homological_algebra/)에서 자주 쓰이지만, 우선은 범주론 카테고리에 두었다.

## Additive category

앞선 글에서 우리는 일반적인 카테고리를 정의했는데, [§카테고리, ⁋예시 2](/ko/math/category_theory/categories#ex2)에서 살펴본 대수적 구조들에서 $\Mor(A,B)$들은 단순한 집합[^1]이 아니라 그 위에 다음의 연산

$$(f\star g)(a)=f(a)\star g(a)\qquad\text{for all $a\in A$}$$

이 정의된 또 다른 대수적 구조이다. 특히 원래 카테고리의 대상들이 abelian group의 구조를 갖고 있었다면 위의 연산을 통해 $\Mor(A,B)$ 또한 abelian group의 구조를 갖는다.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 카테고리 $\mathcal{A}$가 *$\Ab$-카테고리*라는 것은 $\Mor_\mathcal{C}(A,B)$가 모두 abelian group의 구조를 갖고 있으며, 이 때 $(\Mor_\mathcal{C}(A,B),+)$가 합성에 대한 분배법칙을 만족하는 것이다. 즉, 임의의 $g_1,g_2\in\Mor_\mathcal{C}(B,C)$와, 임의의 $f:A\rightarrow B$ 혹은 $h:C\rightarrow D$에 대하여

$$(g_1+g_2)\circ f=g_1\circ f+g_2\circ f,\qquad h\circ(g_1+g_2)=h\circ g_1+h\circ g_2$$

이 모두 성립하는 것이다.

</div>

호몰로지 대수학을 하기 위해서 가장 필요한 것은 kernel과 cokernel이며, 또 종종 두 대상 사이의 곱 또한 필요하다. 우리는 다른 대수적 구조들에서도 두 대상들의 곱을 universal property를 사용하여 정의했으므로, 다음의 정의는 이미 친숙하다.

<div class="definition" markdown="1">

<ins id="df2">**정의 2**</ins> 카테고리 $\mathcal{A}$의 두 대상 $A_1,A_2\in\obj(\mathcal{A})$에 대하여, $A_1$과 $A_2$의 *곱<sub>product</sub>*은 다음과 같은 universal property를 만족하는 triple $(A\_1\times A\_2,\pr\_1,\pr\_2)$를 의미한다.

> 임의의 object $B\in\obj(\mathcal{A})$와 임의의 morphism $f_1:B\rightarrow A_1, f_2:B\rightarrow A_2$에 대하여, 다음의 diagram
>
> ![universal_property_of_product](/assets/images/Category_theory/Abelian_categories-1.png){:width="284.85px" class="invert" .align-center}
>
> 을 commute하도록 하는 $f:B\rightarrow A\_1\times A\_2$가 유일하게 존재한다.

</div>

Additive category 상에서는 product $A_1\times A_2$이 *coproduct*의 universal property 또한 만족한다는 것을 증명할 수 있다. 이러한 의미로 대상 $A_1\times A_2$를 사용할 때는 이를 $A_1\oplus A_2$로 표기한다. 

## Kernel과 cokernel

Kernel과 cokernel의 universal property를 살펴보기 위해서는 우선 $0$이 무엇인지부터 정의해야 한다.

<div class="definition" markdown="1">

<ins id="df3">**정의 3**</ins> 카테고리 $\mathcal{A}$의 대상 $I$가 *initial<sub>시작 대상</sub>*이라는 것은 임의의 $A\in\obj(\mathcal{A})$에 대하여, 유일한 $I\rightarrow A$가 반드시 존재하는 것이다. 또, 대상 $F$가 *final<sub>끝 대상</sub>*이라는 것은 임의의 $A\in\obj(\mathcal{A})$에 대하여, 유일한 $A\rightarrow F$가 반드시 존재하는 것이다.

만일 어떠한 대상 $Z\in\obj(\mathcal{A})$가 initial인 동시에 final이라면, $Z$를 *zero object<sub>영 대상</sub>*라 부른다.

</div>

$\mathbf{Set}$은 initial object를 갖지 않고, 따라서 zero object도 갖지 않는다. 한편 $\mathbf{Group}$에서는 trivial group $\\{e\\}$가 zero object가 된다.

<div class="definition" markdown="1">

<ins id="df4">**정의 4**</ins> $\Ab$-카테고리 $\mathcal{A}$가 *additive category<sub>덧셈 카테고리</sub>*라는 것은 $\mathcal{A}$가 zero object를 가지고, 임의의 $A,B\in\obj(\mathcal{A})$에 대하여 그 곱 $A\times B$가 항상 존재하는 것이다.

</div>

이럴 경우, 우리는 $A$에서 $B$로의 morphism을 *homomorphism*이라 부르고 이들의 모임을 $\Hom_\mathcal{A}(A,B)$로 적는다. 두 additive category $\mathcal{A},\mathcal{B}$ 사이의 functor $F:\mathcal{A}\rightarrow\mathcal{B}$가 *additive functor<sub>덧셈함자</sub>*라는 것은 $F$가 abelian group $\Hom\_\mathcal{A}(A,B)$에서 $\Hom\_\mathcal{B}(FA,FB)$ 사이의 group homomorphism을 유도하는 것이다.

Additive category에서는 임의의 $A,B\in\obj(\mathcal{A})$에 대하여, *zero map<sub>영사상</sub>* $0\_{AB}:A\rightarrow B$가 $A\rightarrow 0\rightarrow B$로 정의된다. 이렇게 정의한 zero map은 물론 abelian group $\Hom\_\mathcal{A}(A,B)$의 덧셈에 대한 항등원이 된다.

<div class="proposition" markdown="1">

<ins id="pp5">**명제 5**</ins> 임의의 additive category $\mathcal{A}$와 두 대상 $A,B\in\obj(\mathcal{A})$에 대하여, 위에서 정의한 zero map $0_{AB}$는 $\Hom\_\mathcal{A}(A,B)$의 덧셈에 대한 항등원이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Zero object $0$에서 $B$로의 morphism $0\_{0B}$가 유일하게 존재한다. 따라서 $0\_{0B}+0\_{0B}=0\_{0B}$가 성립한다. 이제 주어진 명제는 다음의 식

$$0_{AB}+0_{AB}=0_{0B}\circ0_{A0}+0_{0B}\circ0_{A0}=(0_{0B}+0_{0B})\circ 0_{A0}=0_{0B}\circ 0_{A0}=0_{AB}$$

으로부터 자명하다.

</details>

뿐만 아니라, 이 정보만으로 kernel과 cokernel에 대한 universal property도 만들 수 있다. 다음 정의는 zero object가 존재하는 모든 카테고리에서도 동일하게 적용되지만, 우리는 additive category에서만 사용한다.

<div class="definition" markdown="1">

<ins id="df6">**정의 6**</ins> Additive category $\mathcal{A}$의 두 대상 $A,B$ 사이의 homomorphism $f:A\rightarrow B$를 생각하자.

1. Homomorphism $i:K\rightarrow A$가 $f$의 *kernel<sub>핵</sub>*이라는 것은 $f\circ i=0$이며, 다음의 universal property를 만족하는 것이다.
    > 임의의 $j:Z\rightarrow A$가 $f\circ j=0$을 만족한다면, 다음 diagram을 commute하도록 하는 유일한 homomorphism $Z\rightarrow K$가 항상 존재한다.
    >
    > ![universal_property_of_kernel](/assets/images/Category_theory/Abelian_categories-2.png){:width="209.55px" class="invert" .align-center}
2. 비슷하게, $f$의 *cokernel<sub>여핵</sub>*은 다음 diagram에 해당하는 universal property를 만족하는 homomorphism $p:B\rightarrow C$로 정의된다.

![universal_property_of_cokernel](/assets/images/Category_theory/Abelian_categories-3.png){:width="206.7px" class="invert" .align-center}

</div>

## Abelian category

이제 abelian category를 정의할 수 있다.

<div class="definition" markdown="1">

<ins id="df7">**정의 7**</ins> Additive category $\mathcal{A}$가 *abelian category<sub>아벨 카테고리</sub>*라는 것은 다음 조건들이 추가로 성립하는 것이다.

1. 임의의 homomorphism이 kernel과 cokernel을 갖는다.
2. 임의의 monomorphism $f$는 $\coker f$의 kernel과 같다.
3. 임의의 epimorphism $f$는 $\ker f$의 cokernel과 같다.

</div>

[\[호몰로지 대수학\] §Diagram chasing, ⁋보조정리 4](/ko/math/homological_algebra/diagram_chasing#lem4)을 증명할 때에는 diagram에 등장하는 대상의 원소를 봅지 않고, 오직 universal property만을 이용하여 증명을 완료할 수 있었다. 이 보조정리 뿐만 아니라, [\[호몰로지 대수학\] §Diagram chasing](/ko/math/homological_algebra/diagram_chasing)에서 소개한 보조정리는 모두 abelian category $\mathcal{A}$에서도 증명할 수 있다.

이를 일일히 보이는 대신 다음 정리를 소개하며 글을 마친다.

<div class="proposition" markdown="1">

<ins id="thm8">**정리 8 (Freyd-Mitchell embedding theorem)**</ins> 임의의 small abelian category $\mathcal{A}$에 대하여, 적당한 ring $R$과 fully faithful, exact functor $F:\mathcal{A}\rightarrow\Mod{R}$이 존재한다.

</div>

---

**참고문헌**

**[Wei]** C.A. Weibel. *An Introduction to Homological Algebra*. Cambridge Studies in Advanced Mathematics. Cambridge University Press, 1995.  
**[Vak]** R. Vakil, *The rising sea: foundations of algebraic geometry*. 2015. Preprint. [링크](http://math.stanford.edu/~vakil/216blog/FOAGnov1817public.pdf)

---

[^1]: 이들이 실제로 집합이라는 것은 $B^A$가 집합이라는 사실로부터 자명하다. 따라서, 해당 예시에서 다룬 대수적 구조들의 카테고리는 모두 국소적으로 작은 카테고리이다. 