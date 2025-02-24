---

title: "몫환, 환 동형사상"
excerpt: "Quotient ring과 ring isomorphism theorems"

categories: [Math / Algebraic Structures]
permalink: /ko/math/algebraic_structures/quotient_rings
header:
    overlay_image: /assets/images/Math/Algebraic_Structures/Quotient_rings.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_structures-ko"

date: 2024-05-05
last_modified_at: 2024-05-05
weight: 102

---

이번 글에서 우리는 quotient ring의 개념을 정의한다. [§몫군](/ko/math/algebraic_structures/quotient_groups)을 정의할 때를 떠올려보면, group $G$의 임의의 subgroup $H$에 대해 $G/H$는 집합으로서는 항상 정의되지만 이것이 항상 group의 구조를 갖는 것은 아니었고, 이를 위해서는 $H$가 normal subgroup이라는 조건이 필요했다. 마찬가지로 ring $A$와 subring $S$에 대하여 $A/S$가 항상 ring structure를 갖는 것은 아니다. 

## 몫환의 정의

우선 $A$와 $S$의 곱셈 구조를 잊어버리면 $S$가 $A$의 subgroup이다. 그런데 $A$가 abelian group이므로, $A/S$에 abelian group 구조가 존재한다. 이 위에 ring 구조가 정의되기 위해서는 곱셈 구조에도 비슷한 성질이 성립해야 한다. 즉 $A/S$의 임의의 두 원소 $\alpha+S$, $\alpha'+S$에 대하여 이들의 곱

$$(\alpha+S)(\alpha'+S)\overset{?}{=}\alpha\alpha'+S$$

이 위와 같이 정의되어야 한다. 한편, 임의의 $xx'\in S$에 대하여

$$(\alpha+x)(\alpha'+x')=\alpha\alpha'+x\alpha'+\alpha x'+xx'$$

이고, $xx'\in S$이므로 위의 식이 성립하기 위해서는 $x\alpha',\alpha x'\in S$가 항상 성립해야 한다. 즉, $S$의 원소 $x$에 대하여, 임의의 $\alpha\in A$를 가져왔을 때 $\alpha x\in S$도, $x\alpha\in S$도 성립해야 하므로, $S$가 $A$의 two-sided ideal이어야 한다. 이 논의로부터 다음을 얻는다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Ring $A$와 two-sided ideal $\mathfrak{a}$가 주어졌다 하자. 위와 같이 정의된 ring $A/\mathfrak{a}$를 *$\mathfrak{a}$에 의한 $A$의 quotient ring<sub>몫환</sub>*이라 부른다.

</div>

그럼 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> Ring $A$와 two-sided ideal $\mathfrak{a}$에 대하여 다음이 성립한다.

1. $\alpha\mapsto \alpha+\mathfrak{a}$로 정의된 함수 $\pi:A\rightarrow A/\mathfrak{a}$는 ring homomorphism이다.
2. Ring homomorphism $\phi:A \rightarrow B$에 대하여, 만일 $\phi(\mathfrak{a})=\\{0\\}$이라면 $A/\mathfrak{a}$에서 $B$로 가는 유일한 $\bar{\phi}$가 존재하여 $\phi=\bar{\phi}\circ\pi$가 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

1. $\pi$가 덧셈에 대해 abelian group homomorphism을 정의한다는 것은 [§몫군](/ko/math/algebraic_structures/quotient_groups)의 결과로부터 자명하다. $\pi$가 곱셈을 보존하는 것 또한 위의 논의로부터 자명하며, 따라서 $1+\mathfrak{a}$가 $A/\mathfrak{a}$의 $1$이 되는 것을 확인할 수 있다.
2. 우선 $\phi$를 abelian group homomorphism으로 생각하자. 그럼 주어진 조건에 의하여 $A$의 subgroup $\mathfrak{a}$가 $\ker \phi$에 포함되므로, $A/\mathfrak{a}$에서 $B$로 가는 유일한 *group* homomorphism $\bar{\phi}:A/\mathfrak{a}\rightarrow B$가 존재하여 $\phi=\bar{\phi}\circ\pi$가 성립한다. ([§동형사상, ⁋명제 3](/ko/math/algebraic_structures/isomorphism_theorems#prop3]))  
    이제 $A/\mathfrak{a}$의 두 원소 $\alpha+\mathfrak{a}, \beta+\mathfrak{a}$를 임의로 택하자. 그럼

    $$(\alpha+\mathfrak{a})(\beta+\mathfrak{a})=\alpha\beta+\mathfrak{a}=\pi(\alpha\beta)$$

    이므로, 다음 식

    $$\bar{\phi}((\alpha+\mathfrak{a})(\beta+\mathfrak{a}))=\bar{\phi}(\pi(\alpha)\pi(\beta))=\bar{\phi}(\pi(\alpha\beta))=\phi(\alpha\beta)=\phi(\alpha)\phi(\beta)=\bar{\phi}(\pi(\alpha))\bar{\phi}(\pi(\beta))=\bar{\phi}(\alpha+\mathfrak{a})\bar{\phi}(\beta+\mathfrak{a})$$

    에 의해 $\bar{\phi}$는 곱셈을 보존한다. 비슷하게 $\bar{\phi}(1+\mathfrak{a})=\bar{\phi}(\pi(1))=\phi(1)=1$로부터 $\bar{\phi}$는 $1$을 $1$로 보낸다. 

</details>

다음 정리는 [§동형사상](/ko/math/algebraic_structures/isomorphism_theorems)의 ring homomorphism 버전이라 할 수 있다.

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3**</ins> Ring homomorphism $\phi:A \rightarrow B$와 kernel $\ker \phi$, 그리고 image $\im\phi$에 대하여, 다음이 성립한다.

1. $\ker \phi$는 $A$의 two-sided ideal이며, $\alpha+\ker \phi \mapsto \phi(\alpha)$가 잘 정의된 isomorphism $A/\ker \phi \rightarrow \im \phi$을 정의한다.
2. $A$의 subring $S$에 대하여, $S+\ker \phi=\{\alpha+x\mid\alpha\in S, x\in\ker \phi\}$는 $A$의 subring이고, $S\cap\ker \phi$는 $S$의 two-sided ideal이 되며, isomorphism $(S+\ker \phi)/\ker \phi\cong S/(S\cap \ker f)$이 존재한다. 
3. $A$의 두 two-sided ideal $\mathfrak{a}, \mathfrak{b}$가 $\mathfrak{b}\subseteq \mathfrak{a}$를 만족한다면, $\mathfrak{a}/\mathfrak{b}$는 $A/\mathfrak{b}$의 two-sided ideal이고 $(A/\mathfrak{b})/(\mathfrak{a}/\mathfrak{b})\cong A/\mathfrak{a}$이 성립한다.
4. $A$의 two-sided ideal $\mathfrak{a}$에 대하여, $A/\mathfrak{a}$의 two-sided ideal의 집합과, $\mathfrak{a}$를 포함하는 $A$의 ideal들의 집합 사이의 inclusion-preserving bijection이 존재한다.

</div>

이에 대한 증명은 앞선 [명제 2](#prop2)와 마찬가지로 [§동형사상](/ko/math/algebraic_structures/isomorphism_theorems)에서 다루었던 것과 거의 동일하게 진행하되, 얻어지는 group homomorphism이 실제로 ring homomorphism 또한 된다는 것만 보이면 된다. 

---

**참고문헌**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  

---