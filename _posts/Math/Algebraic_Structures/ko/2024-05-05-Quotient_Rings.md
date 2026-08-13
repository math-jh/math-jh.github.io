---
title: "몫환, 환 동형사상"
description: "몫환은 ring과 two-sided ideal로 구성되며, ring homomorphism의 보편 성질을 만족한다. 임의의 ring homomorphism에 대해 induced homomorphism의 존재와 유일성이 성립한다."
excerpt: "Quotient ring과 ring isomorphism theorems"

categories: [Math / Algebraic Structures]
permalink: /ko/math/algebraic_structures/quotient_rings
sidebar: 
    nav: "algebraic_structures-ko"

date: 2024-05-05
weight: 102
drift_needed: true

---

이번 글에서 우리는 quotient ring의 개념을 정의한다. [§몫군](/ko/math/algebraic_structures/quotient_groups)을 정의할 때를 떠올려보면, group $G$의 임의의 subgroup $H$에 대해 $G/H$는 집합으로서는 항상 정의되지만 이것이 항상 group의 구조를 갖는 것은 아니었고, 이를 위해서는 $H$가 normal subgroup이라는 조건이 필요했다. 마찬가지로 ring $A$에 대해서도 quotient를 정의할 수 있는 방식은 제한되어 있다.

## 몫환의 정의

우선 $A$가 abelian group이고 $S$가 그 subgroup이라면 $A/S$에 abelian group 구조가 존재한다. 이 위에 ring 구조가 정의되기 위해서는 곱셈 구조에도 비슷한 성질이 성립해야 한다. 즉 $A/S$의 임의의 두 원소 $\alpha+S$, $\alpha'+S$에 대하여 이들의 곱

$$(\alpha+S)(\alpha'+S)\overset{?}{=}\alpha\alpha'+S$$

이 위와 같이 정의되어야 한다. 한편, 임의의 $x,x'\in S$에 대하여

$$(\alpha+x)(\alpha'+x')=\alpha\alpha'+x\alpha'+\alpha x'+xx'$$

이므로, 위의 식이 성립하기 위해서는 $x\alpha'+\alpha x'+xx'\in S$가 항상 성립해야 한다. 특히 $x'=0$으로 두면 임의의 $\alpha'\in A$에 대하여 $x\alpha'\in S$여야 하고, $x=0$으로 두면 임의의 $\alpha\in A$에 대하여 $\alpha x'\in S$여야 한다. 즉 $S$가 $A$의 two-sided ideal이어야 한다. 거꾸로 $S$가 two-sided ideal이라면 세 항 $x\alpha'$, $\alpha x'$, $xx'$이 모두 $S$에 속하므로 위의 곱셈은 representative의 선택과 무관하게 잘 정의된다. 이 논의로부터 다음을 얻는다.

::: 정의 1
Ring $A$와 two-sided ideal $\mathfrak{a}$가 주어졌다 하자. 위와 같이 정의된 ring $A/\mathfrak{a}$를 *$\mathfrak{a}$에 의한 $A$의 quotient ring<sub>몫환</sub>*이라 부른다.
:::

그럼 다음이 성립한다.

::: 명제 2
Ring $A$와 two-sided ideal $\mathfrak{a}$에 대하여 다음이 성립한다.

1. $\alpha\mapsto \alpha+\mathfrak{a}$로 정의된 함수 $\pi:A\rightarrow A/\mathfrak{a}$는 ring homomorphism이다.
2. Ring homomorphism $\phi:A \rightarrow B$에 대하여, 만일 $\phi(\mathfrak{a})=\{0\}$이라면 $A/\mathfrak{a}$에서 $B$로 가는 유일한 ring homomorphism $\bar{\phi}$가 존재하여 $\phi=\bar{\phi}\circ\pi$가 성립한다.
:::
::: 증명
1. $\pi$가 덧셈에 대해 abelian group homomorphism을 정의한다는 것은 [§몫군](/ko/math/algebraic_structures/quotient_groups)의 결과이다. $\pi$가 곱셈을 보존하는 것은 다음 계산
  
    $$\pi(\alpha)\pi(\alpha')=(\alpha+\mathfrak{a})(\alpha'+\mathfrak{a})=\alpha\alpha'+\mathfrak{a}=\pi(\alpha\alpha')$$
    
    에서 얻어지며, 이 때 $1+\mathfrak{a}$가 $A/\mathfrak{a}$의 $1$이 되는 것을 확인할 수 있다.
2. 우선 $\phi$를 abelian group homomorphism으로 생각하자. 그럼 주어진 조건에 의하여 $A$의 subgroup $\mathfrak{a}$가 $\ker \phi$에 포함되므로, $A/\mathfrak{a}$에서 $B$로 가는 유일한 *group* homomorphism $\bar{\phi}:A/\mathfrak{a}\rightarrow B$가 존재하여 $\phi=\bar{\phi}\circ\pi$가 성립한다. ([§군 동형사상, ⁋명제 3](/ko/math/algebraic_structures/isomorphism_theorems#prop3))  
    이제 $A/\mathfrak{a}$의 두 원소 $\alpha+\mathfrak{a}, \beta+\mathfrak{a}$를 임의로 택하자. 그럼

    $$(\alpha+\mathfrak{a})(\beta+\mathfrak{a})=\alpha\beta+\mathfrak{a}=\pi(\alpha\beta)$$

    이므로, 다음 식

    $$\bar{\phi}((\alpha+\mathfrak{a})(\beta+\mathfrak{a}))=\bar{\phi}(\pi(\alpha)\pi(\beta))=\bar{\phi}(\pi(\alpha\beta))=\phi(\alpha\beta)=\phi(\alpha)\phi(\beta)=\bar{\phi}(\pi(\alpha))\bar{\phi}(\pi(\beta))=\bar{\phi}(\alpha+\mathfrak{a})\bar{\phi}(\beta+\mathfrak{a})$$

    에 의해 $\bar{\phi}$는 곱셈을 보존한다. 비슷하게 $\bar{\phi}(1+\mathfrak{a})=\bar{\phi}(\pi(1))=\phi(1)=1$로부터 $\bar{\phi}$는 $1$을 $1$로 보낸다. 
:::

다음 정리는 [§군 동형사상](/ko/math/algebraic_structures/isomorphism_theorems)의 ring homomorphism 버전이라 할 수 있다.

::: 정리 3
Ring homomorphism $\phi:A \rightarrow B$와 kernel $\ker \phi$, 그리고 image $\im\phi$에 대하여, 다음이 성립한다.

1. $\ker \phi$는 $A$의 two-sided ideal이며, $\alpha+\ker \phi \mapsto \phi(\alpha)$가 잘 정의된 isomorphism $A/\ker \phi \rightarrow \im \phi$을 정의한다.
2. $A$의 subring $S$에 대하여, $S+\ker \phi=\{\alpha+x\mid\alpha\in S, x\in\ker \phi\}$는 $A$의 subring이고, $S\cap\ker \phi$는 $S$의 two-sided ideal이 되며, isomorphism $(S+\ker \phi)/\ker \phi\cong S/(S\cap \ker \phi)$이 존재한다. 
3. $A$의 두 two-sided ideal $\mathfrak{a}, \mathfrak{b}$가 $\mathfrak{b}\subseteq \mathfrak{a}$를 만족한다면, $\mathfrak{a}/\mathfrak{b}$는 $A/\mathfrak{b}$의 two-sided ideal이고 $(A/\mathfrak{b})/(\mathfrak{a}/\mathfrak{b})\cong A/\mathfrak{a}$이 성립한다.
4. $A$의 two-sided ideal $\mathfrak{a}$에 대하여, $A/\mathfrak{a}$의 two-sided ideal의 집합과, $\mathfrak{a}$를 포함하는 $A$의 two-sided ideal들의 집합 사이의 inclusion-preserving bijection이 존재한다.
:::
::: 증명
1번과 3번은 [§군 동형사상](/ko/math/algebraic_structures/isomorphism_theorems)에서 다루었던 것과 거의 동일하게 진행하되, 거기서 얻어지는 group homomorphism이 실제로 ring homomorphism 또한 된다는 것을 [명제 2](#prop2)의 2번과 같은 방식으로 확인하면 된다.

2번의 경우, $S+\ker \phi$가 덧셈에 대한 subgroup이라는 것은 group의 경우와 같다. 임의의 $\alpha,\alpha'\in S$와 $x,x'\in\ker \phi$에 대하여

$$(\alpha+x)(\alpha'+x')=\alpha\alpha'+(x\alpha'+\alpha x'+xx')$$

에서 $\alpha\alpha'\in S$이고, 1번에 의해 $\ker \phi$가 two-sided ideal이므로 괄호 안의 세 항이 모두 $\ker \phi$에 속한다. 여기에 $1\in S$를 더하면 $S+\ker \phi$가 $A$의 subring임을 얻는다. 또 $S\cap\ker \phi$는 $S$의 덧셈에 대한 subgroup이고, 임의의 $\alpha\in S$와 $y\in S\cap\ker \phi$에 대하여 $\alpha y$와 $y\alpha$가 $S$와 $\ker \phi$ 모두에 속하므로 이는 $S$의 two-sided ideal이다. 이제 합성

$$S\hookrightarrow S+\ker \phi\longrightarrow (S+\ker \phi)/\ker \phi$$

을 생각하면 이는 전사이고 그 kernel이 $S\cap\ker \phi$이므로, 1번을 적용하여 원하는 isomorphism을 얻는다.

4번의 두 대응 $\bar{\mathfrak{b}}\mapsto\pi^{-1}(\bar{\mathfrak{b}})$와 $\mathfrak{b}\mapsto\pi(\mathfrak{b})$가 서로의 역이며 포함관계를 보존한다는 것은 [§군 동형사상, ⁋정리 7](/ko/math/algebraic_structures/isomorphism_theorems#thm7)에 따른 것이다. 남는 것은 이 대응이 two-sided ideal을 two-sided ideal로 보낸다는 것이다. 우선 임의의 $\alpha\in A$와 $x\in\pi^{-1}(\bar{\mathfrak{b}})$에 대하여 ,

$$\pi(\alpha x)=\pi(\alpha)\pi(x)\in\bar{\mathfrak{b}}$$

이므로 $\alpha x\in\pi^{-1}(\bar{\mathfrak{b}})$가 되어 $\pi^{-1}(\bar{\mathfrak{b}})$는 왼쪽에서의 곱셈에 대해 닫혀있다. 비슷하게, $\pi$가 전사이므로 $A/\mathfrak{a}$의 임의의 원소는 $\pi(\alpha)$의 꼴이며 따라서 

$$\pi(\alpha)\pi(x)=\pi(\alpha x)\in\pi(\mathfrak{b})$$

이므로 이로부터 $\bar{\mathfrak{b}}$가 왼쪽에서의 곱셈에 대해 닫혀있음을 확인할 수 있다. 오른쪽에서 곱하는 경우도 같은 방식으로 보일 수 있으며, 따라서 이들은 two-sided ideal이다.
:::

---

**참고문헌**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  

---