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

이번 글에서 우리는 quotient ring의 개념을 정의한다. [§몫군](/ko/math/algebraic_structures/quotient_groups)을 정의할 때를 떠올려보면, group $G$의 임의의 subgroup $H$에 대해 $G/H$는 집합으로서는 항상 정의되지만 이것이 항상 group의 구조를 갖는 것은 아니었고, 이를 위해서는 $H$가 normal subgroup이라는 조건이 필요했다. 마찬가지로 ring $A$와 subring $B$에 대하여 $A/B$가 항상 ring structure를 갖는 것은 아니다. 

## 몫환의 정의

우선 $A$와 $B$의 곱셈 구조를 잊어버리면 $B$가 $A$의 subgroup이다. 그런데 $A$가 abelian group이므로, $B$는 사실 $A$의 *abelian* subgroup이고 따라서 $A/B$에 group 구조가 존재한다. 이 위에 ring 구조가 정의되기 위해서는 곱셈 구조에도 비슷한 성질이 성립해야 한다. 즉 $A/B$의 임의의 두 원소 $a+B$, $a'+B$에 대하여 이들의 곱

$$(a+B)(a'+B)\overset{?}{=}aa'+B$$

이 위와 같이 정의되어야 한다. 임의의 $b,b'\in B$에 대하여

$$(a+b)(a'+b')=aa'+ba'+ab'+bb'$$

이고, $bb'\in B$이므로 위의 식이 성립하기 위해서는 $ba',ab'\in B$가 항상 성립해야 한다. 즉, $B$의 원소 $b$에 대하여, 임의의 $a\in A$를 가져왔을 때 $ab\in B$도, $ba\in B$도 성립해야 하므로, $B$가 $A$의 two-sided ideal이어야 한다. 이 논의로부터 다음을 얻는다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Ring $A$와 two-sided ideal $\mathfrak{a}$가 주어졌다 하자. 위와 같이 정의된 ring $A/\mathfrak{a}$를 *$\mathfrak{a}$에 의한 $A$의 quotient ring<sub>몫환</sub>*이라 부른다.

</div>

그럼 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> Ring $A$와 two-sided ideal $\mathfrak{a}$에 대하여 다음이 성립한다.

1. $a\mapsto a+\mathfrak{a}$로 정의된 함수 $\pi:A\rightarrow A/\mathfrak{a}$는 ring homomorphism이다.
2. Ring homomorphism $f:A \rightarrow B$에 대하여, 만일 $f(\mathfrak{a})=\\{0\\}$이라면 $A/\mathfrak{a}$에서 $B$로 가는 유일한 $\bar{f}$가 존재하여 $f=\bar{f}\circ\pi$가 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

1. $\pi$가 덧셈에 대해 abelian group homomorphism을 정의한다는 것은 [§몫군](/ko/math/algebraic_structures/quotient_groups)의 결과로부터 자명하다. $\pi$가 곱셈을 보존하는 것 또한 위의 논의로부터 자명하며, 따라서 $1+\mathfrak{a}$가 $A/\mathfrak{a}$의 $1$이 되는 것을 확인할 수 있다.
2. 우선 $f$를 abelian group homomorphism으로 생각하자. 그럼 주어진 조건에 의하여 $A$의 subgroup $\mathfrak{a}$가 $\ker f$에 포함되므로, $A/\mathfrak{a}$에서 $B$로 가는 유일한 *group* homomorphism $\bar{f}:A/\mathfrak{a}\rightarrow B$가 존재하여. ([§동형사상, ⁋명제 3](/ko/math/algebraic_structures/isomorphism_theorems#prop3])) $f=\bar{f}\circ\pi$가 성립한다.  
    이제 $A/\mathfrak{a}$의 두 원소 $x+\mathfrak{a}, y+\mathfrak{a}$를 임의로 택하자. 그럼

    $$(x+\mathfrak{a})(y+\mathfrak{a})=xy+\mathfrak{a}=\pi(xy)$$

    이므로, 다음 식

    $$\bar{f}((x+\mathfrak{a})(y+\mathfrak{a}))=\bar{f}(\pi(x)\pi(y))=\bar{f}(\pi(xy))=f(xy)=f(x)f(y)=\bar{f}(\pi(x))\bar{f}(\pi(y))=\bar{f}(x+\mathfrak{a})\bar{f}(y+\mathfrak{a})$$

    에 의해 $\bar{f}$는 곱셈을 보존한다. 비슷하게 $\bar{f}(1+\mathfrak{a})=\bar{f}(\pi(1))=f(1)=1$로부터 $\bar{f}$는 $1$을 $1$로 보낸다. 

</details>

다음 정리는 [§동형사상](/ko/math/algebraic_structures/isomorphism_theorems)의 ring homomorphism 버전이라 할 수 있다.

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3**</ins> Ring homomorphism $f:A \rightarrow B$와 kernel $\ker f$에 대하여, 다음이 성립한다.

1. $\ker f$는 $A$의 two-sided ideal이며, $a+\ker f \mapsto f(a)$가 잘 정의된 isomorphism $A/\ker f \rightarrow \im f$을 정의한다.
2. $A$의 subring $A'$에 대하여, $A'+\ker f=\{a'+x:a'\in A', x\in\ker f\}$는 $A$의 subring이고, $A'\cap\ker f$는 $A'$의 two-sided ideal이 되며, isomorphism $(A'+\ker f)/\ker f\cong A'/(A'\cap \ker f)$이 존재한다. 
3. $A$의 두 two-sided ideal $\mathfrak{a}, \mathfrak{b}$가 $\mathfrak{b}\subseteq \mathfrak{a}$를 만족한다면, $\mathfrak{a}/\mathfrak{b}$는 $A/\mathfrak{b}$의 two-sided ideal이고 $(A/\mathfrak{b})/(\mathfrak{a}/\mathfrak{b})\cong A/\mathfrak{a}$이 성립한다.
4. $A$의 two-sided ideal $\mathfrak{a}$에 대하여, $A/\mathfrak{a}$의 two-sided ideal의 집합과, $\mathfrak{a}$를 포함하는 $A$의 ideal들의 집합 사이의 inclusion-preserving bijection이 존재한다.

</div>

이에 대한 증명은 [§동형사상](/ko/math/algebraic_structures/isomorphism_theorems)에서 다루었던 것과 거의 동일하므로 생략한다. 

---

**참고문헌**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  

---