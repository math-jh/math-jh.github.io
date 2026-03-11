---

title: "표현가능한 함자"
excerpt: "Initial object, terminal object, representable functor"

categories: [Math / Category Theory]
permalink: /ko/math/category_theory/representable_functors
header:
    overlay_image: /assets/images/Math/Category_Theory/Representable_functors.png
    overlay_filter: 0.5
sidebar: 
    nav: "category_theory-ko"

date: 2023-06-22
last_modified_at: 2023-06-22
weight: 7

---

(Locally small) category $\mathcal{A}$의 임의의 대상 $A$는 두 functor 

$$\Hom_\mathcal{A}(A,-):\mathcal{A}\rightarrow\Set,\qquad \Hom_\mathcal{A}(-,A):\mathcal{A}\rightarrow\Set$$

를 정의하며, 첫 번째는 covariant functor, 두 번째는 contravariant functor가 된다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Category $\mathcal{A}$가 주어졌다 하자.

1. Covariant functor $F:\mathcal{A}\rightarrow\Set$이 *representable functor<sub>표현 가능한 함자</sub>*라는 것은 적당한 object $A\in\obj(\mathcal{A})$가 존재하여, $F$와 $\Hom_\mathcal{A}(A,-)$이 naturally isomorphic한 것이다.
2. Contravariant functor $F:\mathcal{A}\rightarrow\Set$이 *representable functor<sub>표현 가능한 함자</sub>*라는 것은 적당한 object $A\in\obj(\mathcal{A})$가 존재하여, $F$와 $\Hom_\mathcal{A}(-,A)$이 naturally isomorphic한 것이다.

임의의 functor $F$에 대하여, 위의 조건을 만족하는 $A\in\obj(\mathcal{A})$와 natural isomorphism의 선택을 $F$의 *representation<sub>표현</sub>*이라 부른다.

</div>

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> 가장 간단한 예시는 $\mathcal{A}=\Set$이고 $F$가 identity functor일 때이다. 이 경우, 임의의 singleton set $\ast$가 $\id_\Set$을 represent하는 것을 확인할 수 있다. 직관적으로 이는 임의의 집합 $A$에 대하여, $\ast$에서 $A$로의 함수 $f$는 그 image가 무엇인지를 통해 $A$의 원소와 일대일 대응관계에 있기 때문이다.

비슷하게 forgetful functor $U:\Grp \rightarrow \Set$은 $\mathbb{Z}$가 represent한다. 이는 $\Grp$의 임의의 group $G$에 대하여, $\mathbb{Z}$에서 $G$로의 group homomorphism $f$는 $\mathbb{Z}$의 generator $1$이 어디로 가는지에 따라 결정된다는 사실에서 알 수 있다.




</div>

더 일반적으로 다음 정리가 성립한다.

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3 (Yoneda)**</ins> 임의의 functor $F:\mathcal{A}\rightarrow\Set$과, 임의의 $A\in\obj(\mathcal{A})$에 대하여, 집합 사이의 bijection

$$\{\text{natural transformations from $\Hom_\mathcal{A}(A,-)$ to $F$}\}\rightarrow F(A);\qquad \alpha\mapsto \alpha_A(\id_A)$$

가 존재한다. 뿐만 아니라, 양 변을 $\mathcal{A}\times\Set^\mathcal{A}$에서 $\Set$으로의 functor로 생각하면 이 bijection은 $\mathcal{A}$와 $\Set^\mathcal{A}$ 각 성분에 대해 natural하다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>



---

**참고문헌**

**[Rie]** Emily Riehl. *Category Theory in Context*. Dover Publications, 2016.

---