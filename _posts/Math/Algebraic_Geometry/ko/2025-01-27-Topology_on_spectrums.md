---

title: "스펙트럼의 위상구조"
excerpt: ""

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/topology_of_spectrums
header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Topology_of_spectrums.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_geometry-ko"

date: 2025-01-27
last_modified_at: 2025-01-27
weight: 1

---

<div class="remark" markdown="1">

이 카테고리의 모든 글들에서 ring은 commutative ring (with unity)를 의미한다. 

</div>

이번 글에서 우리는 대수기하학의 가장 기본적인 대상인 스펙트럼을 정의한다. 스펙트럼은 적당한 structure sheaf가 주어져 있는 위상공간으로, 우리는 우선 이번 글에서 이를 집합으로서 정의하고, 그 위에 위상을 정의할 것이다. 그 후, 다음 글에서는 $\Spec A$ 위에 structure sheaf를 정의하게 된다. 

## 집합으로서의 $\Spec A$

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Ring $A$에 대하여, $\Spec A$는 $A$의 모든 prime ideal들의 모임이고, 이를 $A$의 *spectrum<sub>스펙트럼</sub>*이라 부른다. 

</div>

이제 ring homomorphism $\phi: A \rightarrow B$가 주어졌다 하자. 그럼 [\[대수적 구조\] §분수체, ⁋명제 9](/ko/math/algebraic_structures/field_of_fractions#prop9)에 의하여, 다음의 함수 

$$\Spec\phi: \Spec B \rightarrow \Spec A;\qquad \mathfrak{q}\mapsto \phi^{-1}(\mathfrak{q})$$

가 잘 정의된다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 위에서 정의한 $\Spec: \cRing^\op \rightarrow \Set$은 functor이다. 

</div>

즉, $\Spec(\phi\circ\psi)=(\Spec\psi)\circ(\Spec\phi)$이고 $\Spec(\id_A)=\id_{\Spec A}$이며, 그 증명 또한 어렵지 않다. 

## 위상공간으로서의 $\Spec A$

이제 우리는 $\Spec A$ 위에 적절한 위상구조를 정의하자.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Ring $A$와 그 spectrum $\Spec A$를 고정하자. $A$의 임의의 부분집합 $S$에 대하여, $\Spec A$의 부분집합 $Z(S)$을 다음 식

$$Z(S)=\{\mathfrak{p}\in\Spec A: S\subseteq \mathfrak{p}\}$$

으로 정의한다. 

</div>

그럼 몇 가지 사실을 쉽게 증명할 수 있다. 우선, $Z$는 inclusion-reversing이다. 즉, 만일 $A$의 두 부분집합 $S_1\subseteq S_2$가 주어졌다면,

$$Z(S_1)=\{\mathfrak{p}\in\Spec A: S_1\subseteq \mathfrak{p}\}\supseteq \{\mathfrak{p}\in\Spec A: S_2\subseteq \mathfrak{p}\}=Z(S_2)$$

이다. 그러나 위의 포함관계는 strict가 아닐 수도 있다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> Ring $A$와 그 spectrum $\Spec A$를 고정하자. $A$의 임의의 부분집합 $S$, 그리고 $S$에 의해 생성되는 $A$의 ideal $(S)$에 대하여, $Z(S)=Z((S))$이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

자명하게 $S\subseteq (S)$이므로, 포함관계 $Z((S))\subseteq Z(S)$는 위의 논의로부터 자명하다. 따라서 반대방향을 증명하면 충분하다. $Z(S)$의 임의의 원소 $\mathfrak{p}$가 주어졌다 하자. 즉 $S\subseteq \mathfrak{p}$이다. 그런데 $A$의 부분집합 $\mathfrak{p}$에 의해 생성되는 ideal은 자기 자신이므로, 이로부터 $(S)\subseteq (\mathfrak{p})=\mathfrak{p}$임을 안다.

</details>

뿐만 아니라, $A$의 두 *ideal* $\mathfrak{a}\_1\subseteq \mathfrak{a}\_2$에 대해서도, 포함관계 $Z(\mathfrak{a}\_1)\supseteq Z(\mathfrak{a}\_2)$는 일반적으로 등호가 될 수도 있다. 

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> Ring $A$와 그 spectrum $\Spec A$를 고정하자. $A$의 임의의 ideal $\mathfrak{a}$와 그 radical $\sqrt{\mathfrak{a}}$에 대하여, $Z(\mathfrak{a})=Z(\sqrt{\mathfrak{a}})$이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

역시 마찬가지로 포함관계 $\mathfrak{a}\subseteq \sqrt{\mathfrak{a}}$로부터 $Z(\sqrt{\mathfrak{a}})\subseteq Z(\mathfrak{a})$임은 자명하다. 거꾸로 임의의 $\mathfrak{p}\in Z(\mathfrak{a})$에 대하여, [\[가환대수학\] §국소화의 성질들, ⁋따름정리 8](/ko/math/commutative_algebra/properties_of_localization#cor8)를 사용하면

$$\sqrt{\mathfrak{a}}=\bigcap_\text{\scriptsize$\mathfrak{q}$ a prime containing $\mathfrak{a}$}\mathfrak{q}\subseteq \mathfrak{p}$$

이므로 $\mathfrak{p}\in Z(\sqrt{\mathfrak{a}})$임을 안다. 

</details>

$\Spec A$ 위에 위상구조를 정의할 때 가장 중요한 것은 다음의 보조정리다. 

<div class="proposition" markdown="1">

<ins id="lem6">**보조정리 6**</ins> 다음이 성립한다.

1. $A$의 임의의 ideal $\mathfrak{a},\mathfrak{b}$에 대하여, $Z(\mathfrak{ab})=Z(\mathfrak{a})\cup Z(\mathfrak{b})$가 성립한다.
2. $A$의 ideal들의 모임 $\\{\mathfrak{a}\_i\\}$에 대하여, $Z(\sum \mathfrak{a}\_i)=\bigcap Z(\mathfrak{a}\_i)$가 성립한다.
3. $A$의 임의의 ideal $\mathfrak{a},\mathfrak{b}$에 대하여, $Z(\mathfrak{a})\subseteq Z(\mathfrak{b})\iff \sqrt{\mathfrak{a}}\supseteq \sqrt{\mathfrak{b}}$이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

1. $\mathfrak{a}$ 혹은 $\mathfrak{b}$를 포함하는 prime ideal $\mathfrak{p}$는 그보다 작은 ideal $\mathfrak{ab}$ 또한 포함하는 것이 자명하므로, 반대방향 포함관계만 보이면 충분하다. $\mathfrak{p}\supset \mathfrak{ab}$라 가정하자. 만일 $\mathfrak{p}\not\supseteq \mathfrak{b}$라 하면, $b\not\in \mathfrak{p}$인 $\mathfrak{b}$의 원소 $b$를 찾을 수 있다. 한편, 임의의 $a\in \mathfrak{a}$에 대하여, $ab\in \mathfrak{ab}\subseteq \mathfrak{p}$이고, 앞선 가정에 의해 $b\not\in \mathfrak{p}$이므로 반드시 $a\in \mathfrak{p}$이고 따라서 $a\subseteq \mathfrak{p}$가 성립한다.
2. 이는 $\sum \mathfrak{a}_i$가 ideal들 $\mathfrak{a}_i$ 각각을 모두 포함하는 ideal 중 가장 작은 것으로 정의되므로 자명하다.
3. [\[가환대수학\] §국소화의 성질들, ⁋따름정리 8](/ko/math/commutative_algebra/properties_of_localization#cor8).

</details>

그럼 [\[위상수학\] §집합의 내부, 폐포, 경계, ⁋명제 2](/ko/math/topology/other_concepts#prop2)에 의하여, $Z(\mathfrak{a})$들을 닫힌집합으로 갖는 유일한 위상 $\mathcal{T}$가 존재하여 $\Spec A$를 위상공간으로 만들어준다. 

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> 위와 같이 정의된 $\Spec A$의 위상을 *Zariski topology<sub>자리스키 위상</sub>*이라 부른다.

</div>

앞서 우리는 [명제 2](#prop2)에서 $\Spec$을 functor $\Spec: \cRing^\op \rightarrow \Set$으로 취급할 수 있음을 살펴보았다. 뿐만 아니라, $\Spec$은 $\cRing^\op$에서 $\Top$으로의 functor이기도 하다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> Ring $A$의 spectrum $\Spec A$ 위에 [정의 7](#def7)의 위상구조를 주면, [명제 2](#prop2)의 functor $\Spec: \cRing^\op \rightarrow \Top$은 functor이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[명제 2](#prop2)에서 추가로 보여야 할 것은 임의의 ring homomorphism $\phi: A \rightarrow B$가 주어졌을 때, $\Spec \phi: \Spec B \rightarrow \Spec A$가 <em_ko>연속</em_ko>함수라는 것이다. 따라서 $\Spec A$의 임의의 닫힌집합을 가져왔을 때, 이 닫힌집합의 $\Spec\phi$에 의한 preimage도 $\Spec B$에서의 닫힌집합임을 보이면 충분하다. ([\[위상수학\] §집합의 내부, 폐포, 경계, ⁋명제 2](/ko/math/topology/other_concepts#prop2))

한편 $\Spec A$의 임의의 닫힌집합은 모두 $Z(\mathfrak{a})$의 꼴이고, $\Spec B$의 닫힌집합은 모두 $Z(\mathfrak{b})$의 꼴이므로 이를 보이기 위해서는 임의의 $A$의 ideal $\mathfrak{a}$가 주어질 때마다 다음의 식

$$(\Spec\phi)^{-1}(Z(\mathfrak{a}))=Z(\mathfrak{b})$$

을 만족하는 $B$의 ideal $\mathfrak{b}$가 존재함을 보이면 충분하다. 우리의 주장은 다음의 식

$$(\Spec\phi)^{-1}(Z(\mathfrak{a}))=Z(\phi(\mathfrak{a}))$$

이 성립한다는 것이다. 그럼 $\phi(\mathfrak{a})$로 생성되는 ideal이 위의 식을 만족하므로 증명이 완료된다. 

우선 $\mathfrak{q}\in\Spec B$가 좌변에 속한다 하자. 즉 $(\Spec\phi)(\mathfrak{q})=\phi^{-1}(\mathfrak{q})\in Z(\mathfrak{a})$가 성립한다. 그럼 $\mathfrak{a}\subseteq \phi^{-1}(\mathfrak{q})$인 것으로부터 $\phi(\mathfrak{a})\subseteq \mathfrak{q}$이므로 $\mathfrak{q}\in Z(\phi(\mathfrak{a}))$이 성립한다.

거꾸로 $\mathfrak{q}\in\Spec B$가 우변에 속한다 하자. 그럼 $\phi(\mathfrak{a})\subseteq \mathfrak{q}$인 것으로부터, 다음의 포함관계

$$\mathfrak{a}\subseteq \phi^{-1}(\phi(\mathfrak{a}))\subseteq\phi^{-1}(\mathfrak{q})=(\Spec\phi)(\mathfrak{q})$$

를 얻고 이것이 곧 $(\Spec\phi)(\mathfrak{q})\in Z(\mathfrak{a})$, 즉 $\mathfrak{q}\in (\Spec\phi)^{-1}(Z(\mathfrak{a}))$임을 증명한다. 

</details>

우리가 앞으로 사용할 두 가지의 중요한 ring homomorphism은 quotient $\pi:A \rightarrow A/\mathfrak{a}$와 localization $\epsilon: A \rightarrow S^{-1}A$이다. ([\[가환대수학\] §기본 개념들, ⁋명제 11](/ko/math/commutative_algebra/basic_notions#prop11) 그리고 [\[가환대수학\] §국소화, ⁋명제 8](/ko/math/commutative_algebra/localization#prop8))

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> 위에서 정의한 $\pi:A \rightarrow A/\mathfrak{a}$와 $\epsilon: A \rightarrow S^{-1}A$에 대해 다음이 성립한다.

1. $\Spec\pi$와 $\Spec\epsilon$은 모두 injective이며, 이들은 각자의 image로의 homeomorphism을 정의한다.
2. $\Spec\pi$의 $\Spec A$에서의 image는 닫힌집합이다.
3. 만일 어떠한 $f\in A$에 대하여 $S=\\{1,f,f^2,\ldots\\}$라면, $\Spec \epsilon$의 $\Spec A$에서의 image는 열린집합이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

첫 번째 결과는 앞서 언급한 두 명제 [\[가환대수학\] §기본 개념들, ⁋명제 11](/ko/math/commutative_algebra/basic_notions#prop11) 그리고 [\[가환대수학\] §국소화, ⁋명제 8](/ko/math/commutative_algebra/localization#prop8)의 결과이다. 두 번째 결과의 경우, $\Spec\pi$의 $\Spec A$에서의 image는 정확히 $Z(\mathfrak{a})$이다. 마지막으로 셋째 결과의 경우, $\Spec\epsilon$의 원소들은 $f$를 포함하지 않는 prime ideal들의 모임이고 이들은 $\Spec A\setminus Z(f)$으로 쓸 수 있다. 

</details>

위상공간으로서 $\Spec A$의 base가 존재하는 것은 당연하지만, 우리는 이 base 또한 $A$의 대수적인 구조와 모종의 관계가 있기를 바란다. 다음을 정의하자.

<div class="definition" markdown="1">

<ins id="def10">**정의 10**</ins> Ring $A$의 임의의 원소 $f\in A$에 대하여, $V(f)$의 $\Spec A$에서의 complement $\Spec A\setminus Z(f)$를 $D(f)$라 적는다. 이러한 꼴의 열린집합을 *principal open set*이라 부른다. 

</div>

<div class="proposition" markdown="1">

<ins id="lem11">**보조정리 11**</ins> Principal open set들의 모임은 $\Spec A$의 base를 이룬다. ([\[위상수학\] §위상공간의 기저, ⁋정의 1](/ko/math/topology/topological_bases#def1))

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 열린집합 $\Spec A \setminus Z(S)$에 대하여, [보조정리 6](#lem6)의 둘째 결과을 활용하면 다음의 계산

$$\Spec A\setminus Z(S)=\Spec A\setminus Z\left(\sum_{f\in S} (f)\right)=\Spec A\setminus\left(\bigcap_{f\in S}Z(f)\right)=\bigcup_{f\in S} (\Spec A\setminus Z(f))=\bigcup_{f\in S} D(f)$$

이 성립한다. 

</details>

그럼 이 보조정리와 유사한 계산을 통해 $D(fg)=D(f)\cap D(g)$임을 확인할 수 있다. 다만, 이 계산은 [보조정리 6](#lem6)의 첫째 결과를 사용하므로, 일반적으로 무한한 index에 대해 확장할 수는 없다. 

## 갈루아 대응

정의에 의해 $Z$는 $A$의 ideal을 받아 $\Spec A$의 닫힌집합을 내놓는 함수이다. 거꾸로 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="def12">**정의 12**</ins> 임의의 부분집합 $T\subseteq \Spec A$에 대하여, 

$$I(T)=\{f\in A:\text{$f\in \mathfrak{p}$ for all $\mathfrak{p}\in T$}\}=\bigcap_\text{\scriptsize$\mathfrak{p}$ a prime in $T$} \mathfrak{p}$$

으로 정의한다.

</div>

그럼 $I(T)$는 ideal들의 교집합이므로 ideal이다. 뿐만 아니라, 만일 $T_1\subseteq T_2$라면 $I(T_2)\subseteq I(T_1)$임이 자명하다. 

이제 [정의 3](#def3)과 [정의 12](#def12)을 종합하면, 우리는 두 ordered set $\mathcal{P}(A)$, $\mathcal{P}(\Spec A)$ 사이의 두 함수 

$$Z: \mathcal{P}(A) \rightarrow \mathcal{P}(\Spec A);\quad S\mapsto Z(S),\qquad I: \mathcal{P}(\Spec A) \rightarrow \mathcal{P}(A);\quad T\mapsto I(T)$$

을 정의했다. 그럼 임의의 $S\in \mathcal{P}(A)$와 임의의 $T\in \mathcal{P}(\Spec A)$에 대하여,

$$T\subseteq Z(S)\iff\text{$\mathfrak{p}\in Z(S)$ for all $\mathfrak{p}\in T$}\iff\text{$f\in \mathfrak{p}$ for all $f\in S$ and all $\mathfrak{p}\in T$}\iff S\subseteq I(T)$$

이므로, $(Z, I)$는 $\mathcal{P}(A)$와 $\mathcal{P}(\Spec A)$ 사이의 antitone Galois connection을 정의한다. ([\[집합론\] §필터와 아이디얼, 갈루아 대응, ⁋정의 6](/ko/math/set_theory/filter_and_ideal#def6)) 따라서, 다음의 두 식

$$Z(I(Z(S)))=Z(S),\qquad I(Z(I(T)))=I(T)$$

이 모든 $S\in \mathcal{P}(A)$와 임의의 $T\in \mathcal{P}(\Spec A)$에 대해 성립한다. 

이제 두 closure operator $IZ: \mathcal{P}(A) \rightarrow \mathcal{P}(A)$, $ZI: \mathcal{P}(\Spec A) \rightarrow \mathcal{P}(\Spec A)$를 생각하자. 

<div class="proposition" markdown="1">

<ins id="prop13">**명제 13**</ins> Closure operator $IZ: \mathcal{P}(A) \rightarrow \mathcal{P}(A)$, $ZI: \mathcal{P}(\Spec A) \rightarrow \mathcal{P}(\Spec A)$에 대하여, 다음이 성립한다.

1. $IZ(S)=\sqrt{(S)}$
2. $ZI(T)=\cl(T)$

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

1. 이는 다음의 식
    
    $$I(Z(S))=I(Z((S)))=\bigcap_\text{\scriptsize$\mathfrak{p}$ a prime in $Z((S))$} \mathfrak{p}=\bigcap_\text{\scriptsize$\mathfrak{p}$ a prime containing $(S)$} \mathfrak{p}=\sqrt{(S)}$$

    으로부터 자명하다.
2. 이는 다음의 식
    
    $$\cl(T)
    =\bigcap_\text{\scriptsize $Z(S)\supseteq T$} Z(S)
    =\bigcap_\text{\scriptsize $S\subseteq I(T)$} Z(S)
    =Z\left(\sum_\text{\scriptsize $S\subseteq I(T)$}(S)\right)
    =Z(I(T))$$

    으로부터 자명하다.

</details>

즉, 다음을 얻는다.

<div class="proposition" markdown="1">

<ins id="thm14">**정리 14**</ins> Ring $A$의 radical ideal들과, $\Spec A$의 닫힌집합들 사이의 Galois correspondence가 존재한다. 

</div>

## 고전적인 대수기하학

다음 글에서 structure sheaf를 정의하기 전에, 간략하게 고전적인 대수기하학을 살펴보는 것이 도움이 된다. 남은 부분에서 우리는 algebraically closed field $\mathbb{k}$를 고정한다. 그럼 field $\mathbb{k}$ 위에 정의된 *affine $n$-space<sub>아핀공간</sub>*는 다음 집합

$$\mathbb{A}_\mathbb{k}^n=\{(x_1,\ldots, x_n)ㅣ x_1,\ldots, x_n\in \mathbb{k}\}$$

을 의미한다. 이 때, $\mathbb{A}_\mathbb{k}^n$의 각 원소 $x=(x_1,\ldots, x_n)$을 *점<sub>point</sub>*라 하고, 각각의 $x_i$들을 $x$의 *$i$번째 좌표<sub>$i$-th coordinate</sub>*라 부른다. 

이제 $\mathbb{k}$를 계수로 갖는 다항식들로 이루어진 polynomial ring $A=\mathbb{k}[\x_1,\ldots,\x_n]$를 생각하자. 그럼 임의의 $x=(x_1,\ldots, x_n)\in \mathbb{A}\_\mathbb{k}^n$에 대하여, $A$의 ideal $\mathfrak{m}_x$를

$$\mathfrak{m}_x=(\x_1-x_1,\ldots, \x_n-x_n)\subseteq \mathbb{k}[\x_1,\ldots, \x_n]$$

으로 정의할 수 있으며 [\[가환대수학\] §영점정리](/ko/math/commutative_algebra/nullstellensatz)에서 우리는 이것이 $A=\mathbb{k}[\x_1,\ldots, \x_n]$의 *모든* maximal ideal이라는 것을 증명했다. 

그럼 임의의 $f\in A$를 다음의 식

$$\mathbb{A}_\mathbb{k}^n \rightarrow \mathbb{k};\qquad (x_1,\ldots, x_n)\mapsto f(x_1,\ldots, x_n)$$

을 통해 $\mathbb{A}\_\mathbb{k}^n$에서 $\mathbb{k}$로의 함수로 취급할 수 있다. 이제 $A$의 임의의 부분집합 $T$에 대하여, $\mathbb{A}\_\mathbb{k}^n$의 부분집합 $Z(T)$를 다음의 식

$$Z(T)=\{(x_1,\ldots, x_n): \text{$f(x_1,\ldots, x_n)=0$ for all $f\in T$}\}$$

으로 정의하자. 즉 $Z(T)$는 $\mathbb{A}_\mathbb{k}^n$ 위에 정의된 함수들의 모임 $T$의 공통근들으로 생각할 수 있다. 

한편, 부분집합 $T$로 생성되는 $A$의 ideal $\mathfrak{a}$를 생각하면, $Z(T)=Z(\mathfrak{a})$임이 자명하다. 한편 $A$는 noetherian이므로 ([##ref##](Hilbert_basis_thm)) 이러한 $\mathfrak{a}$는 유한히 많은 원소들 $f_1,\ldots, f_r$로 생성될 수 있고 따라서 임의의 $Z(T)$는 항상 유한히 많은 함수들의 공통근들의 모임으로 쓸 수 있다. 