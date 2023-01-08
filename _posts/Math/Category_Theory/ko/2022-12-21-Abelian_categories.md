---

title: "아벨 카테고리"
excerpt: "아벨 카테고리"

categories: [Math / Category Theory]
permalink: /ko/math/category_theory/abelian_categories
header:
    overlay_image: /assets/images/Math/Category_Theory/Abelian_categories.png
    overlay_filter: 0.5
sidebar: 
    nav: "category_theory-ko"

date: 2022-12-21
last_modified_at: 2022-12-21
weight: 4

---

아벨 카테고리의 개념은 [호몰로지 대수학](/ko/homological_algebra/)에서 자주 쓰이지만, 우선은 범주론 카테고리에 두었다. 아벨 카테고리를 정의할 때 그 원형은 $\Ab$, 더 일반적으로는 $\lmod{R}$인데, 여기에는 product나 coproduct, kernel과 cokernel 등이 잘 정의되며, 뿐만 아니라 morphism들의 모임이 자연스러운 abelian group의 구조를 갖는다. 

## 기본개념들

### Product and coproduct

수학적인 구조들에서 우리는 대상들의 곱과 그 dual을 이미 universal property를 통해 정의하였으므로, 다음 정의는 이미 익숙한 것이다.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 카테고리 $\mathcal{A}$의 대상들의 family $(A\_i)\_{i\in I}$에 대하여, 이들의 *곱<sub>product</sub>*은 다음의 universal property를 만족하는 대상 $\prod\_{i\in I}A\_i$과 morphism들 $(\pr\_i:\prod A\_i\rightarrow A\_i)\_{i\in I}$을 의미한다.

> 임의의 $B\in\obj(\mathcal{A})$와, morphism들의 family $(f\_i:B\rightarrow A\_i)\_{i\in I}$가 주어졌다면, 다음 diagram을 commute하도록 하는 morphism $f:B\rightarrow A$가 유일하게 존재한다.
>
> ![universal_property_of_product](/assets/images/Category_Theory/Abelian_categories-1.png){:width="251.4px" class="invert" .align-center}

비슷하게, 이들 family의 *쌍대곱<sub>coproduct</sub>*은 다음 diagram에 해당하는 universal property로 정의되는 대상과 morphism들을 의미한다.

![universal_property_of_coproduct](/assets/images/Category_Theory/Abelian_categories-2.png){:width="251.4px" class="invert" .align-center}

</div>

일반적인 카테고리의 일반적인 family가 product나 coproduct를 항상 가질 필요는 없지만, 만약 위의 universal property를 만족하는 쌍이 존재한다면 isomorphism에 대해 유일하게 존재한다는 것을 안다. 

### Initial object와 final object, zero object

Kernel과 cokernel의 universal property를 살펴보기 위해서는 우선 $0$이 무엇인지부터 정의해야 한다.

<div class="definition" markdown="1">

<ins id="df2">**정의 2**</ins> 카테고리 $\mathcal{A}$를 생각하자.

- 대상 $I$가 *initial<sub>시작 대상</sub>*이라는 것은 임의의 $A\in\obj(\mathcal{A})$에 대하여, 유일한 $I\rightarrow A$가 반드시 존재하는 것이다. 
- 대상 $F$가 *final<sub>끝 대상</sub>*이라는 것은 임의의 $A\in\obj(\mathcal{A})$에 대하여, 유일한 $A\rightarrow F$가 반드시 존재하는 것이다.
- 어떠한 대상 $Z\in\obj(\mathcal{A})$가 initial인 동시에 final이라면, $Z$를 *zero object<sub>영 대상</sub>*라 부른다.

</div>

$\mathbf{Set}$은 initial object를 갖지 않고, 따라서 zero object도 갖지 않는다. 한편 $\mathbf{Group}$에서는 trivial group $\\{e\\}$가 zero object가 되고, $\lmod{R}$에서는 zero module $0$이 zero object가 된다.

카테고리 $\mathcal{A}$가 zero object를 갖는다고 하자. 그럼 임의의 $A,B\in\obj(\mathcal{A})$에 대하여 $A\rightarrow 0$과 $0\rightarrow B$가 유일하게 결정되며 따라서 $\Mor\_\mathcal{A}(A,B)$에는 이들의 합성 $0_{AB}:A\rightarrow 0\rightarrow B$가 존재한다. 이를 *zero map<sub>영 사상</sub>*이라 부른다.

### Kernel과 cokernel

이제 $0$을 정의하였으므로, kernel과 cokernel을 정의할 수 있다. 

<div class="definition" markdown="1">

<ins id="df3">**정의 3**</ins> Zero object를 갖는 category $\mathcal{A}$의 두 대상 $A,B$ 사이의 morphism $f:A\rightarrow B$를 생각하자.

- Morphism $i:K\rightarrow A$가 $f$의 *kernel<sub>핵</sub>*이라는 것은 $f\circ i=0$이며, 다음의 universal property를 만족하는 것이다.
    > 임의의 $j:Z\rightarrow A$가 $f\circ j=0$을 만족한다면, 다음 diagram을 commute하도록 하는 유일한 morphism $Z\rightarrow K$가 항상 존재한다.
    >
    > ![universal_property_of_kernel](/assets/images/Math/Category_Theory/Abelian_categories-3.png){:width="209.55px" class="invert" .align-center}
- 비슷하게, $f$의 *cokernel<sub>여핵</sub>*은 다음 diagram에 해당하는 universal property를 만족하는 morphism $p:B\rightarrow C$로 정의된다.

![universal_property_of_cokernel](/assets/images/Math/Category_Theory/Abelian_categories-4.png){:width="206.7px" class="invert" .align-center}

</div>

정의에 의하여 kernel은 항상 monomorphism이고 cokernel은 항상 epimorphism이 된다.

## Additive category

이제 아벨 카테고리를 정의할 준비를 거의 끝마쳤다. 서두에서 언급한 것과 같이, 아벨 카테고리의 중요한 성질 중 하나는 morphism들의 모임이 자연스러운 abelian group 구조를 갖는다는 것이다. 사실 [§카테고리, ⁋예시 2](/ko/math/category_theory/categories#ex2)에서 살펴본 대수적 구조들에서 $\Mor(A,B)$들은 단순한 집합[^1]이 아니라 그 위에 다음의 연산

$$(f\star g)(a)=f(a)\star g(a)\qquad\text{for all $a\in A$}$$

이 정의된 또 다른 대수적 구조이다. 특히 원래 카테고리의 대상들이 abelian group의 구조를 갖고 있었다면 위의 연산을 통해 $\Mor(A,B)$ 또한 abelian group의 구조를 갖는다.

<div class="definition" markdown="1">

<ins id="df4">**정의 4**</ins> 카테고리 $\mathcal{A}$가 *$\Ab$-카테고리*라는 것은 $\Mor_\mathcal{C}(A,B)$가 모두 abelian group의 구조를 갖고 있으며, 이 때 $(\Mor_\mathcal{C}(A,B),+)$가 합성에 대한 분배법칙을 만족하는 것이다. 즉, 임의의 $g_1,g_2\in\Mor_\mathcal{C}(B,C)$와, 임의의 $f:A\rightarrow B$ 혹은 $h:C\rightarrow D$에 대하여

$$(g_1+g_2)\circ f=g_1\circ f+g_2\circ f,\qquad h\circ(g_1+g_2)=h\circ g_1+h\circ g_2$$

이 모두 성립하는 것이다.

</div>

<div class="definition" markdown="1">

<ins id="df5">**정의 5**</ins> $\Ab$-카테고리 $\mathcal{A}$가 *additive category<sub>덧셈 카테고리</sub>*라는 것은 $\mathcal{A}$가 zero object를 가지고, 임의의 $A,B\in\obj(\mathcal{A})$에 대하여 그 곱 $A\times B$가 항상 존재하는 것이다.

</div>

이럴 경우, 우리는 $A$에서 $B$로의 morphism을 *homomorphism*이라 부르고 이들의 모임을 $\Hom_\mathcal{A}(A,B)$로 적는다. 두 additive category $\mathcal{A},\mathcal{B}$ 사이의 functor $F:\mathcal{A}\rightarrow\mathcal{B}$가 *additive functor<sub>덧셈함자</sub>*라는 것은 $F$가 abelian group $\Hom\_\mathcal{A}(A,B)$에서 $\Hom\_\mathcal{B}(FA,FB)$ 사이의 group homomorphism을 유도하는 것이다.

Additive category에서는 임의의 $A,B\in\obj(\mathcal{A})$에 대하여, *zero map<sub>영사상</sub>* $0\_{AB}:A\rightarrow B$가 $A\rightarrow 0\rightarrow B$로 정의된다. 이렇게 정의한 zero map은 물론 abelian group $\Hom\_\mathcal{A}(A,B)$의 덧셈에 대한 항등원이 된다.

<div class="proposition" markdown="1">

<ins id="pp6">**명제 6**</ins> 임의의 additive category $\mathcal{A}$와 두 대상 $A,B\in\obj(\mathcal{A})$에 대하여, 위에서 정의한 zero map $0_{AB}$는 $\Hom\_\mathcal{A}(A,B)$의 덧셈에 대한 항등원이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Zero object $0$에서 $B$로의 morphism $0\_{0B}$가 유일하게 존재한다. 따라서 $0\_{0B}+0\_{0B}=0\_{0B}$가 성립한다. 이제 주어진 명제는 다음의 식

$$0_{AB}+0_{AB}=0_{0B}\circ0_{A0}+0_{0B}\circ0_{A0}=(0_{0B}+0_{0B})\circ 0_{A0}=0_{0B}\circ 0_{A0}=0_{AB}$$

으로부터 자명하다.

</details>

## Abelian category

이제 abelian category를 정의할 수 있다.

<div class="definition" markdown="1">

<ins id="df7">**정의 7**</ins> Additive category $\mathcal{A}$가 *abelian category<sub>아벨 카테고리</sub>*라는 것은 다음 조건들이 추가로 성립하는 것이다.

1. 임의의 homomorphism이 kernel과 cokernel을 갖는다.
2. 임의의 monomorphism $f$는 $\coker f$의 kernel과 같다.
3. 임의의 epimorphism $f$는 $\ker f$의 cokernel과 같다.

</div>

Abelian category에서는 임의의 homomorphism $f:A\rightarrow B$에 대해 $f$의 kernel $i:\ker f\rightarrow A$와 cokernel $p:B\rightarrow \coker f$가 존재한다. 직관적으로 $\lmod{R}$에서 살펴보면, $i:\ker f\rightarrow A$는 $A$의 submodule $\ker f$의 $A$로의 canonical inclusion으로 생각할 수 있고, cokernel $p:B\rightarrow \coker f$는 canonical projection으로 생각할 수 있다. ([\[호몰로지 대수학\] §완전열, 명제 2](/ko/math/homological_algebra/exact_sequences#pp2))

임의의 abelian category $\mathcal{A}$에서, $f$의 *image*는 다음의 morphism

$$\ker(\coker f)\rightarrow\coker f$$

으로 정의된다. 이를 $\lmod{R}$에서 살펴보면 $f$의 cokernel은 canonical projection $p:B\rightarrow B/\im f$이고, 따라서 $\ker p=\ker(\coker f)$는 $\lmod{R}$에서 우리가 알고 있는 image의 개념과 잘 맞아떨어진다. 비슷하게, $f$의 *coimage*는 다음의 morphism

$$\coim(f)=\coker(\ker(f))$$

으로 정의한다.

일반적인 abelian category에서, monomorphism $f:A\rightarrow B$가 주어진다면 $\coker f$를 *quotient object*라 부르고 $B\rightarrow B/A$, 혹은 더 간단히 $B/A$라 표기한다. 이 또한 $\lmod{R}$에서는 자명한 것이다. 

<div class="example" markdown="1">

<ins id="ex8">**예시 8 (Homology)**</ins> Abelian category $\mathcal{A}$에서는 kernel과 image가 잘 정의되며, 이들의 quotient object로 호몰로지를 정의할 수 있고, 이것이 $0$이 된다는 것이 exactness이므로 $\mathcal{A}$에서 short exact sequence 또한 잘 정의된다. 즉 abelian category에서는 "diagram chasing"을 할 수 있다. 예컨대

$$C_{n+1}\overset{d_{n+1}}{\longrightarrow} C_n\overset{d_n}{\longrightarrow} C_{n-1}$$

이 $d_{n+1}\circ d_n=0$을 만족한다면, 다음의 diagram

![homology_in_abelilan_category](/assets/images/Math/Category_Theory/Abelian_categories-5.png){:width="390.75px" class="invert" .align-center}

을 따라 monomorphism $\im(d_{n+1})\rightarrow\ker(d_n)$을 정의할 수 있으며, 따라서 quotient $H_n(C)=\ker(d_n)/\im(d_{n+1})$이 잘 정의된다. 이 때 위의 chain complex가 $C_n$에서 *exact*라는 것은 $H_n(C)=0$인 것이다.

</div>

## Freyd-Mitchell embedding theorem

한편, 앞서 살펴본 것처럼 abelian category에서는 kernel, cokernel, image와 quotient 등이 모두 정의된다. 이로부터 $\lmod{R}$에서의 정리들이 모두 성립한다. 가령 first isomorphism theorem을 임의의 abelian category의 언어로 바꾸어 쓰자면, 

> 임의의 abelian category $\mathcal{A}$의 morphism $f:A\rightarrow B$가 주어졌다 하자. 그럼 $A/\ker f\cong \im f$가 성립한다.

와 같이 적을 수 있으며, 좌변은 $i:\ker f\rightarrow A$로부터 얻어지는 quotient object가 된다. 이러한 종류의 정리들은 모두 abelian category로 올릴 수 있고, 증명 또한 kernel과 cokernel의 universal property 등만 이용하여 진행할 수 있으나 그 증명은 다소 복잡하다. 

따라서, 일반적으로는 이러한 정리들을 일일히 보이는 대신 다음 정리를 사용한다. 

<div class="proposition" markdown="1">

<ins id="thm9">**정리 9 (Freyd-Mitchell embedding theorem)**</ins> 임의의 small abelian category $\mathcal{A}$에 대하여, 적당한 ring $R$과 fully faithful, exact functor $F:\mathcal{A}\rightarrow\lmod{R}$이 존재한다.

</div>

여기에서 functor $F$가 exact라는 것은 $\mathcal{A}$의 short exact sequence가 $\lmod{R}$의 short exact sequence로 옮겨진다는 것이다. 

---

**참고문헌**

**[Wei]** C.A. Weibel. *An Introduction to Homological Algebra*. Cambridge Studies in Advanced Mathematics. Cambridge University Press, 1995.  
**[Vak]** R. Vakil, *The rising sea: foundations of algebraic geometry*. 2015. Preprint. [링크](http://math.stanford.edu/~vakil/216blog/FOAGnov1817public.pdf)

---

[^1]: 이들이 실제로 집합이라는 것은 $B^A$가 집합이라는 사실로부터 자명하다. 따라서, 해당 예시에서 다룬 대수적 구조들의 카테고리는 모두 국소적으로 작은 카테고리이다. 