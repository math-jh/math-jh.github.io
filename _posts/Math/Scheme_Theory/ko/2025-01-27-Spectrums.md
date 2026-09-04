---
title: "스펙트럼"
description: "환의 소 아이들로 구성된 스펙트럼을 집합으로 정의하고, 위의 위상 구조를 부여하여 위상공간으로 만드는 과정을 다룬다."
excerpt: "가환환의 prime spectrum과 Zariski topology"

categories: [Math / Scheme Theory]
permalink: /ko/math/scheme_theory/spectrums
sidebar: 
    nav: "scheme_theory-ko"

date: 2025-01-27
weight: 2


---

::: remark 참고 {#rmk}
이 category의 모든 글들에서 ring은 commutative ring (with unity)를 의미한다. 
:::

이번 글에서 우리는 algebraic geometry의 가장 기본적인 대상인 spectrum을 정의한다. Spectrum은 적당한 structure sheaf가 주어져 있는 위상공간으로, 우리는 우선 이번 글에서 이를 집합으로서 정의하고, 그 위에 위상을 정의할 것이다. 그 후, 다음 글에서는 $\Spec A$ 위에 structure sheaf를 정의하게 된다. 

## 집합으로서의 $\Spec A$

::: 정의 1
Ring $A$에 대하여, $\Spec A$는 $A$의 모든 prime ideal들의 모임이고, 이를 $A$의 *spectrum<sub>스펙트럼</sub>*이라 부른다. 
:::

이제 ring homomorphism $\phi: A \rightarrow B$가 주어졌다 하자. 그럼 [\[대수적 구조\] §분수체, ⁋명제 9](/ko/math/algebraic_structures/field_of_fractions#prop9)에 의하여, 다음의 함수 

$$\Spec\phi: \Spec B \rightarrow \Spec A;\qquad \mathfrak{q}\mapsto \phi^{-1}(\mathfrak{q})$$

가 잘 정의된다.

::: 명제 2
위에서 정의한 $\Spec: \cRing^\op \rightarrow \Set$은 functor이다. 
:::

즉, $\Spec(\phi\circ\psi)=(\Spec\psi)\circ(\Spec\phi)$이고 $\Spec(\id_A)=\id_{\Spec A}$이며, 그 증명 또한 어렵지 않다. 

## 위상공간으로서의 $\Spec A$

이제 우리는 $\Spec A$ 위에 적절한 위상구조를 정의하자.

::: 정의 3
Ring $A$와 그 spectrum $\Spec A$를 고정하자. $A$의 임의의 부분집합 $S$에 대하여, $\Spec A$의 부분집합 $Z(S)$을 다음 식

$$Z(S)=\{\mathfrak{p}\in\Spec A\mid S\subseteq \mathfrak{p}\}$$

으로 정의한다. 
:::

그럼 몇 가지 사실을 쉽게 증명할 수 있다. 우선, $Z$는 inclusion-reversing이다. 즉, 만일 $A$의 두 부분집합 $S_1\subseteq S_2$가 주어졌다면,

$$Z(S_1)=\{\mathfrak{p}\in\Spec A\mid S_1\subseteq \mathfrak{p}\}\supseteq \{\mathfrak{p}\in\Spec A\mid S_2\subseteq \mathfrak{p}\}=Z(S_2)$$

이다. 그러나 위의 포함관계는 strict가 아닐 수도 있다.

::: 명제 4
Ring $A$와 그 spectrum $\Spec A$를 고정하자. $A$의 임의의 부분집합 $S$, 그리고 $S$에 의해 생성되는 $A$의 ideal $(S)$에 대하여, $Z(S)=Z((S))$이다. 
:::
::: 증명
자명하게 $S\subseteq (S)$이므로, 포함관계 $Z((S))\subseteq Z(S)$는 위의 논의로부터 자명하다. 따라서 반대방향을 증명하면 충분하다. $Z(S)$의 임의의 원소 $\mathfrak{p}$가 주어졌다 하자. 즉 $S\subseteq \mathfrak{p}$이다. 그런데 $A$의 부분집합 $\mathfrak{p}$에 의해 생성되는 ideal은 자기 자신이므로, 이로부터 $(S)\subseteq (\mathfrak{p})=\mathfrak{p}$임을 안다.
:::

뿐만 아니라, $A$의 두 *ideal* $\mathfrak{a}_1\subseteq \mathfrak{a}_2$에 대해서도, 포함관계 $Z(\mathfrak{a}_1)\supseteq Z(\mathfrak{a}_2)$는 일반적으로 등호가 될 수도 있다. 

::: 명제 5
Ring $A$와 그 spectrum $\Spec A$를 고정하자. $A$의 임의의 ideal $\mathfrak{a}$와 그 radical $\sqrt{\mathfrak{a}}$에 대하여, $Z(\mathfrak{a})=Z(\sqrt{\mathfrak{a}})$이 성립한다.
:::
::: 증명
역시 마찬가지로 포함관계 $\mathfrak{a}\subseteq \sqrt{\mathfrak{a}}$로부터 $Z(\sqrt{\mathfrak{a}})\subseteq Z(\mathfrak{a})$임은 자명하다. 거꾸로 임의의 $\mathfrak{p}\in Z(\mathfrak{a})$에 대하여, [\[가환대수학\] §국소화의 성질들, ⁋따름정리 8](/ko/math/commutative_algebra/properties_of_localization#cor8)를 사용하면

$$\sqrt{\mathfrak{a}}=\bigcap_\text{\scriptsize$\mathfrak{q}$ a prime containing $\mathfrak{a}$}\mathfrak{q}\subseteq \mathfrak{p}$$

이므로 $\mathfrak{p}\in Z(\sqrt{\mathfrak{a}})$임을 안다. 
:::

$\Spec A$ 위에 위상구조를 정의할 때 가장 중요한 것은 다음의 보조정리다. 

::: 보조정리 6
다음이 성립한다.

1. $A$의 임의의 ideal $\mathfrak{a},\mathfrak{b}$에 대하여, $Z(\mathfrak{ab})=Z(\mathfrak{a})\cup Z(\mathfrak{b})$가 성립한다.
2. $A$의 ideal들의 모임 $\{\mathfrak{a}_i\}$에 대하여, $Z(\sum \mathfrak{a}_i)=\bigcap Z(\mathfrak{a}_i)$가 성립한다.
3. $A$의 임의의 ideal $\mathfrak{a},\mathfrak{b}$에 대하여, $Z(\mathfrak{a})\subseteq Z(\mathfrak{b})\iff \sqrt{\mathfrak{a}}\supseteq \sqrt{\mathfrak{b}}$이 성립한다.
:::
::: 증명
1. $\mathfrak{a}$ 혹은 $\mathfrak{b}$를 포함하는 prime ideal $\mathfrak{p}$는 그보다 작은 ideal $\mathfrak{ab}$ 또한 포함하는 것이 자명하므로, 반대방향 포함관계만 보이면 충분하다. $\mathfrak{p}\supseteq \mathfrak{ab}$라 가정하자. 만일 $\mathfrak{p}\not\supseteq \mathfrak{b}$라 하면, $b\not\in \mathfrak{p}$인 $\mathfrak{b}$의 원소 $b$를 찾을 수 있다. 한편, 임의의 $a\in \mathfrak{a}$에 대하여, $ab\in \mathfrak{ab}\subseteq \mathfrak{p}$이고, 앞선 가정에 의해 $b\not\in \mathfrak{p}$이므로 반드시 $a\in \mathfrak{p}$이고 따라서 $\mathfrak{a}\subseteq \mathfrak{p}$가 성립한다.
2. 이는 $\sum \mathfrak{a}_i$가 ideal들 $\mathfrak{a}_i$ 각각을 모두 포함하는 ideal 중 가장 작은 것으로 정의되므로 자명하다.
3. [\[가환대수학\] §국소화의 성질들, ⁋따름정리 8](/ko/math/commutative_algebra/properties_of_localization#cor8).
:::

그럼 [\[위상수학\] §집합의 내부, 폐포, 경계, ⁋명제 2](/ko/math/topology/other_concepts#prop2)에 의하여, $Z(\mathfrak{a})$들을 닫힌집합으로 갖는 유일한 위상 $\mathcal{T}$가 존재하여 $\Spec A$를 위상공간으로 만들어준다. 

::: 정의 7
위와 같이 정의된 $\Spec A$의 위상을 *Zariski topology<sub>자리스키 위상</sub>*이라 부른다.
:::

Zariski topology는 일반적으로 우리가 좋다고 생각했던 위상이 아니다. 가령 임의의 integral domain $A$에 대하여, $(0)$은 그 자체로 prime ideal이며, 여기에 포함된 $A$의 공집합이 아닌 부분집합도 $(0)$ 뿐이다. 즉, $(0)\in\Spec A$를 포함하는 닫힌집합은 오직 $Z(0)=\Spec A$ 뿐이며, 따라서 $A$가 field가 아닌 이상 한점집합 $\{(0)\}$은 닫힌집합이 아니다. 특히 Zariski topology는 일반적으로 Hausdorff space가 아니다. 그러나 이 category의 글들에서 논의를 진행해 나갈수록 우리는 이 구조에서 친숙한 기하학적인 개념들을 발견하게 될 것이다. 

앞서 우리는 [명제 2](#prop2)에서 $\Spec$을 functor $\Spec: \cRing^\op \rightarrow \Set$으로 취급할 수 있음을 살펴보았다. 뿐만 아니라, $\Spec$은 $\cRing^\op$에서 $\Top$으로의 functor이기도 하다.

::: 명제 8
Ring $A$의 spectrum $\Spec A$ 위에 [정의 7](#def7)의 위상구조를 주면, [명제 2](#prop2)의 functor $\Spec: \cRing^\op \rightarrow \Top$은 functor이다. 
:::
::: 증명
[명제 2](#prop2)에서 추가로 보여야 할 것은 임의의 ring homomorphism $\phi: A \rightarrow B$가 주어졌을 때, $\Spec \phi: \Spec B \rightarrow \Spec A$가 <em-ko>연속</em-ko>함수라는 것이다. 따라서 $\Spec A$의 임의의 닫힌집합을 가져왔을 때, 이 닫힌집합의 $\Spec\phi$에 의한 preimage도 $\Spec B$에서의 닫힌집합임을 보이면 충분하다. ([\[위상수학\] §연속함수, ⁋정리 4](/ko/math/topology/continuous_functions#thm4)의 셋째 조건)

한편 $\Spec A$의 임의의 닫힌집합은 모두 $Z(\mathfrak{a})$의 꼴이고, $\Spec B$의 닫힌집합은 모두 $Z(\mathfrak{b})$의 꼴이므로 이를 보이기 위해서는 임의의 $A$의 ideal $\mathfrak{a}$가 주어질 때마다 다음의 식

$$(\Spec\phi)^{-1}(Z(\mathfrak{a}))=Z(\mathfrak{b})$$

을 만족하는 $B$의 ideal $\mathfrak{b}$가 존재함을 보이면 충분하다. 우리의 주장은 다음의 식

$$(\Spec\phi)^{-1}(Z(\mathfrak{a}))=Z(\phi(\mathfrak{a}))$$

이 성립한다는 것이다. 그럼 $\phi(\mathfrak{a})$로 생성되는 ideal이 위의 식을 만족하므로 증명이 완료된다. 

우선 $\mathfrak{q}\in\Spec B$가 좌변에 속한다 하자. 즉 $(\Spec\phi)(\mathfrak{q})=\phi^{-1}(\mathfrak{q})\in Z(\mathfrak{a})$가 성립한다. 그럼 $\mathfrak{a}\subseteq \phi^{-1}(\mathfrak{q})$인 것으로부터 $\phi(\mathfrak{a})\subseteq \mathfrak{q}$이므로 $\mathfrak{q}\in Z(\phi(\mathfrak{a}))$이 성립한다.

거꾸로 $\mathfrak{q}\in\Spec B$가 우변에 속한다 하자. 그럼 $\phi(\mathfrak{a})\subseteq \mathfrak{q}$인 것으로부터, 다음의 포함관계

$$\mathfrak{a}\subseteq \phi^{-1}(\phi(\mathfrak{a}))\subseteq\phi^{-1}(\mathfrak{q})=(\Spec\phi)(\mathfrak{q})$$

를 얻고 이것이 곧 $(\Spec\phi)(\mathfrak{q})\in Z(\mathfrak{a})$, 즉 $\mathfrak{q}\in (\Spec\phi)^{-1}(Z(\mathfrak{a}))$임을 증명한다. 
:::

우리가 앞으로 사용할 두 가지의 중요한 ring homomorphism은 quotient $\pi:A \rightarrow A/\mathfrak{a}$와 localization $\epsilon: A \rightarrow S^{-1}A$이다. ([\[가환대수학\] §기본 개념들, ⁋명제 11](/ko/math/commutative_algebra/basic_notions#prop11) 그리고 [\[가환대수학\] §국소화, ⁋명제 8](/ko/math/commutative_algebra/localization#prop8))

::: 명제 9
위에서 정의한 $\pi:A \rightarrow A/\mathfrak{a}$와 $\epsilon: A \rightarrow S^{-1}A$에 대해 다음이 성립한다.

1. $\Spec\pi$와 $\Spec\epsilon$은 모두 injective이며, 이들은 각자의 image로의 homeomorphism을 정의한다.
2. $\Spec\pi$의 $\Spec A$에서의 image는 닫힌집합이다.
3. 만일 어떠한 $f\in A$에 대하여 $S=\{1,f,f^2,\ldots\}$라면, $\Spec \epsilon$의 $\Spec A$에서의 image는 열린집합이다.
:::
::: 증명
첫 번째 결과에서 $\Spec\pi$와 $\Spec\epsilon$이 injective인 것은 앞서 언급한 두 명제 [\[가환대수학\] §기본 개념들, ⁋명제 11](/ko/math/commutative_algebra/basic_notions#prop11) 그리고 [\[가환대수학\] §국소화, ⁋명제 8](/ko/math/commutative_algebra/localization#prop8)의 결과이다. 두 사상은 [명제 8](#prop8)에 의하여 연속이므로, 남은 것은 이들의 역함수가 연속이라는 것, 즉 두 사상이 각자의 image 위로 닫힌집합을 닫힌집합으로 옮긴다는 것이다. 이는 임의의 ideal $\mathfrak{b}\supseteq \mathfrak{a}$와 $S^{-1}A$의 임의의 ideal $J$에 대한 다음의 두 식

$$(\Spec\pi)\left(Z_{A/\mathfrak{a}}(\mathfrak{b}/\mathfrak{a})\right)=Z_A(\mathfrak{b}),\qquad (\Spec\epsilon)\left(Z_{S^{-1}A}(J)\right)=Z_A(\epsilon^{-1}J)\cap \im(\Spec\epsilon)$$

으로부터 얻어지는데, 첫째 식은 $\mathfrak{q}\supseteq \mathfrak{b}/\mathfrak{a}$와 $\pi^{-1}(\mathfrak{q})\supseteq \mathfrak{b}$가 동치인 것에서, 둘째 식은 $S^{-1}A$의 모든 ideal이 $J=\epsilon(\epsilon^{-1}J)\cdot S^{-1}A$를 만족하는 것에서 따라온다. 두 번째 결과의 경우, $\Spec\pi$의 $\Spec A$에서의 image는 정확히 $Z(\mathfrak{a})$이다. 마지막으로 셋째 결과의 경우, $\Spec\epsilon$의 image의 원소들은 $f$를 포함하지 않는 prime ideal들의 모임이고 이들은 $\Spec A\setminus Z(f)$으로 쓸 수 있다. 
:::

위상공간으로서 $\Spec A$의 base가 존재하는 것은 당연하지만, 우리는 이 base 또한 $A$의 대수적인 구조와 모종의 관계가 있기를 바란다. 다음을 정의하자.

::: 정의 10
Ring $A$의 임의의 원소 $f\in A$에 대하여, $Z(f)$의 $\Spec A$에서의 complement $\Spec A\setminus Z(f)$를 $D(f)$라 적는다. 이러한 꼴의 열린집합을 *principal open set*이라 부른다. 
:::

이제 임의의 $f\in A$에 대하여, $S_f=\{1,f,f^2,\ldots\}$라 하고 $A_f=S_f^{-1}A$로 정의하자. 그럼 [명제 9](#prop9)에 의하여 $\Spec A_f$의 $\Spec \epsilon$에 의한 $\Spec A$에서의 image는 열린집합이다. 그럼 이 열린집합이 정확히 $D(f)$와 집합으로서 같은 것은

$$\mathfrak{p}\not\in Z(f)\iff (f)\not\subseteq \mathfrak{p} \iff f\not\in \mathfrak{p}\iff f^k\not\in \mathfrak{p}\text{ for all $k\geq 0$}\iff S_f\cap \mathfrak{p}=\emptyset$$

와 [\[가환대수학\] §국소화, ⁋명제 8](/ko/math/commutative_algebra/localization#prop8)에 의해 자명하다. 뿐만 아니라, $D(f)$가 $\Spec A_f$와 같은 위상구조를 갖는다는 것 또한 [명제 9](#prop9)의 첫 번째 결과로부터 얻어진다. 

::: 보조정리 11
Principal open set들의 모임은 $\Spec A$의 base를 이룬다. ([\[위상수학\] §위상공간의 기저, ⁋정의 1](/ko/math/topology/topological_bases#def1))
:::
::: 증명
임의의 열린집합 $\Spec A \setminus Z(S)$에 대하여, [보조정리 6](#lem6)의 둘째 결과를 활용하면 다음의 계산

$$\Spec A\setminus Z(S)=\Spec A\setminus Z\left(\sum_{f\in S} (f)\right)=\Spec A\setminus\left(\bigcap_{f\in S}Z(f)\right)=\bigcup_{f\in S} (\Spec A\setminus Z(f))=\bigcup_{f\in S} D(f)$$

이 성립한다. 
:::

그럼 이 보조정리와 유사한 계산을 통해 $D(fg)=D(f)\cap D(g)$임을 확인할 수 있다. 다만, 이 계산은 [보조정리 6](#lem6)의 첫째 결과를 사용하므로, 일반적으로 무한한 index에 대해 확장할 수는 없다. 

이와 별개로, 우리는 $\Spec A$가 항상 [\[위상수학\] §옹골공간, ⁋정의 1](/ko/math/topology/compact_spaces#def1)의 조건을 만족한다는 것을 보일 수 있다. 그러나 일반적으로 우리가 compact space에 기대하는 많은 성질들은 Hausdorff 조건 또한 요구하는 경우가 많고 ([\[위상수학\] §옹골공간, §§옹골 하우스도르프 공간](/ko/math/topology/compact_spaces#옹골-하우스도르프-공간)) Zariski topology는 일반적으로 Hausdorff space가 되지 않으므로, 우리는 이를 *quasi-compact<sub>준옹골</sub>*라 부르기로 한다. 

::: 보조정리 12
$\Spec A$는 위상공간으로서 quasi-compact space이다. 
:::
::: 증명
[보조정리 11](#lem11)로부터 우리는 $\Spec A$를 덮는 principal open set들의 모임 $\{D(f_i)\}_{i\in I}$이 주어질 때마다, $I$의 유한한 부분집합 $J$가 존재하여 여전히 $\Spec A=\bigcup_{j\in J} D(f_j)$임을 보이면 된다. 

주어진 가정 $\Spec A=\bigcup_{i\in I} D(f_i)$로부터 우리는

$$\emptyset=\Spec A\setminus\bigcup_{i\in I} D(f_i)=\bigcap_{i\in I}(\Spec A\setminus D(f_i))=\bigcap_{i\in I} Z(f_i)$$

임을 안다. 한편, [보조정리 6](#lem6)으로부터

$$\emptyset=\bigcap_{i\in I} Z(f_i)=Z\left(\sum_{i\in I}(f_i)\right)$$

이고, 만일 $\sum (f_i)$가 $A$의 proper ideal이라면 이를 포함하는 maximal ideal이 $\bigcap_{i\in I} Z(f_i)$의 원소가 될 것이므로, 위의 식은 $\sum(f_i)=(1)$과 동치이다. 이제 $1\in\sum(f_i)$이므로, 적당한 유한집합 $J\subseteq I$와 $A$의 원소들의 family $(a_j)_{j\in J}$가 존재하여 $\sum_{j\in J} a_jf_j=1$이도록 할 수 있다. 즉

$$Z\left(\sum_{j\in J} (f_j)\right)=\emptyset$$

이고, 이로부터 위의 계산들을 거꾸로 뒤집으면 원하는 결과를 얻는다. 
:::


## 갈루아 대응

정의에 의해 $Z$는 $A$의 ideal을 받아 $\Spec A$의 닫힌집합을 내놓는 함수이다. 거꾸로 다음을 정의한다.

::: 정의 13
임의의 부분집합 $T\subseteq \Spec A$에 대하여, 

$$I(T)=\{f\in A\mid\text{$f\in \mathfrak{p}$ for all $\mathfrak{p}\in T$}\}=\bigcap_\text{\scriptsize$\mathfrak{p}$ a prime in $T$} \mathfrak{p}$$

으로 정의한다.
:::

그럼 $I(T)$는 ideal들의 교집합이므로 ideal이다. 뿐만 아니라, 만일 $T_1\subseteq T_2$라면 $I(T_2)\subseteq I(T_1)$임이 자명하다. 

이제 [정의 3](#def3)과 [정의 13](#def13)을 종합하면, 우리는 두 ordered set $\mathcal{P}(A)$, $\mathcal{P}(\Spec A)$ 사이의 두 함수 

$$Z: \mathcal{P}(A) \rightarrow \mathcal{P}(\Spec A);\quad S\mapsto Z(S),\qquad I: \mathcal{P}(\Spec A) \rightarrow \mathcal{P}(A);\quad T\mapsto I(T)$$

을 정의했다. 그럼 임의의 $S\in \mathcal{P}(A)$와 임의의 $T\in \mathcal{P}(\Spec A)$에 대하여,

$$T\subseteq Z(S)\iff\text{$\mathfrak{p}\in Z(S)$ for all $\mathfrak{p}\in T$}\iff\text{$f\in \mathfrak{p}$ for all $f\in S$ and all $\mathfrak{p}\in T$}\iff S\subseteq I(T)$$

이므로, $(Z, I)$는 $\mathcal{P}(A)$와 $\mathcal{P}(\Spec A)$ 사이의 antitone Galois connection을 정의한다. ([\[집합론\] §필터와 아이디얼, 갈루아 대응, ⁋정의 6](/ko/math/set_theory/filter_and_ideal#def6)) 따라서, 다음의 두 식

$$Z(I(Z(S)))=Z(S),\qquad I(Z(I(T)))=I(T)$$

이 모든 $S\in \mathcal{P}(A)$와 임의의 $T\in \mathcal{P}(\Spec A)$에 대해 성립한다. 

이제 두 closure operator $IZ: \mathcal{P}(A) \rightarrow \mathcal{P}(A)$, $ZI: \mathcal{P}(\Spec A) \rightarrow \mathcal{P}(\Spec A)$를 생각하자. 

::: 명제 14
Closure operator $IZ: \mathcal{P}(A) \rightarrow \mathcal{P}(A)$, $ZI: \mathcal{P}(\Spec A) \rightarrow \mathcal{P}(\Spec A)$에 대하여, 다음이 성립한다.

1. $IZ(S)=\sqrt{(S)}$
2. $ZI(T)=\cl(T)$
:::
::: 증명
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
:::

즉, 다음을 얻는다.

::: 정리 15
Ring $A$의 radical ideal들과, $\Spec A$의 닫힌집합들 사이의 Galois correspondence가 존재한다. 
:::

이 대응에서 다소 헷갈릴 수 있는 것은 $A$의 임의의 prime ideal은 항상 radical ideal이므로, ring $A$의 radical ideal들의 모임은 항상 (집합으로서) $\Spec A$를 포함한다. 

::: 명제 16
Ring $A$의 prime ideal들과, $\Spec A$의 irreducible closed subset들 사이의 Galois correspondence가 존재한다.
:::
::: 증명
즉 임의의 prime ideal $\mathfrak{p}$에 대하여 $Z(\mathfrak{p})$가 irreducible인 것과, 임의의 irreducible closed subset $Y$에 대하여 $I(Y)$가 prime ideal인 것을 보여야 한다.

우선 $I(\{\mathfrak{p}\})=\mathfrak{p}$이므로 [명제 14](#prop14)의 둘째 결과는 다음의 식

$$Z(\mathfrak{p})=Z(I(\{\mathfrak{p}\}))=\cl(\{\mathfrak{p}\})$$

을 준다. 그런데 한점집합은 항상 irreducible이고 irreducible subset의 closure 또한 irreducible이므로, $Z(\mathfrak{p})$는 irreducible이다. 즉 $\mathfrak{p}$는 $Z(\mathfrak{p})$의 generic point이다.

거꾸로 임의의 irreducible closed subset $Y$에 대하여, $I(Y)$가 prime ideal이라는 것을 보여야 한다. 우선 $Y$가 닫힌집합이므로 [정리 15](#thm15)와 [명제 5](#prop5)에 의하여 $Y=Z(\mathfrak{a})$이도록 하는 radical ideal $\mathfrak{a}$가 존재한다. 그럼 $\mathfrak{a}=IZ(\mathfrak{a})=I(Y)$가 prime인 것을 보이면 충분하다. 이 때 $Y$는 irreducible이므로 공집합이 아니고, 따라서 $\mathfrak{a}=I(Y)$는 $Y$의 원소인 prime ideal에 포함되어 proper ideal이다. ([\[위상수학\] §차원, ⁋정의 6](/ko/math/topology/dimension#def6)) 

이를 위해 $fg\in \mathfrak{a}$라 하고, $\Spec A$의 두 열린집합 $D(f), D(g)$를 생각하면 

$$(D(f)\cap Y)\cap (D(g)\cap Y)=D(f)\cap D(g)\cap Y=D(fg)\cap Y$$

가 공집합이어야 함을 안다. 그런데 $D(f)\cap Y$와 $D(g)\cap Y$는 irreducible closed set $Y$의 두 열린집합이므로, 이것이 성립하기 위해서는 둘 중 하나가 공집합이어야 한다. ([\[위상수학\] §차원, ⁋명제 7](/ko/math/topology/dimension#prop7)) 한편 임의의 $h\in A$에 대하여 $D(h)\cap Y=\emptyset$인 것은 $Y$의 모든 원소가 $h$를 포함한다는 것, 즉 $h\in I(Y)=\mathfrak{a}$인 것과 동치이다. 이로부터 $f\in \mathfrak{a}$ 혹은 $g\in \mathfrak{a}$가 성립해야 함을 알고, 따라서 $\mathfrak{a}$는 prime ideal이다. 
:::

특히, prime ideal $\mathfrak{p}$에 대하여 $\mathfrak{q}\subsetneq \mathfrak{p}$를 만족하는 prime ideal이 없다면, 즉 $\mathfrak{p}$가 *minimal* prime ideal이라면 $Z(\mathfrak{p})$는 irreducible closed subset들 가운데 포함관계에 대해 maximal인 것, 즉 irreducible component가 된다. 이로부터 다음을 얻는다.

::: 따름정리 17
Ring $A$의 minimal prime ideal들과 $\Spec A$의 irreducible component 사이의 Galois correspondence가 존재한다. 
:::
::: 증명
[명제 14](#prop14)에 의하여 임의의 prime ideal $\mathfrak{p}$에 대해서는 $IZ(\mathfrak{p})=\sqrt{\mathfrak{p}}=\mathfrak{p}$이고, $\Spec A$의 임의의 닫힌집합 $Y$에 대해서는 $ZI(Y)=\cl(Y)=Y$이므로, $Z$와 $I$는 서로 역이 되는 대응이다. 따라서 [명제 16](#prop16)에 의하여 $\mathfrak{p}\mapsto Z(\mathfrak{p})$는 $A$의 prime ideal들과 $\Spec A$의 irreducible closed subset들 사이의 전단사이며, 그 역은 $Y\mapsto I(Y)$이다. 뿐만 아니라 두 prime ideal $\mathfrak{p},\mathfrak{q}$에 [보조정리 6](#lem6)의 셋째 결과를 적용하면 

$$Z(\mathfrak{q})\subseteq Z(\mathfrak{p})\iff \sqrt{\mathfrak{q}}\supseteq \sqrt{\mathfrak{p}}\iff \mathfrak{q}\supseteq \mathfrak{p}$$

이므로 이 전단사는 포함관계를 뒤집는다.

한편 [\[위상수학\] §차원, ⁋정의 9](/ko/math/topology/dimension#def9)에 의하여 $\Spec A$의 irreducible component는 irreducible subset들 가운데 maximal인 것이고, irreducible set의 closure는 다시 irreducible이므로 이들은 항상 닫힌집합이다. 거꾸로 irreducible closed subset들 가운데 maximal인 $Y$가 주어졌다 하고, $Y$를 포함하는 임의의 irreducible subset $S$를 생각하자. 그럼 $\cl(S)$는 $Y$를 포함하는 irreducible closed subset이므로 $Y$의 maximality에 의하여 $\cl(S)=Y$이고, 따라서 $S\subseteq Y$, 즉 $S=Y$이다. 이상에서 $\Spec A$의 irreducible component들은 정확히 irreducible closed subset들 가운데 포함관계에 대해 maximal인 것들이다.

이제 위의 전단사가 포함관계를 뒤집으므로, 이는 prime ideal들 가운데 minimal인 것들, 즉 minimal prime ideal들과, irreducible closed subset들 가운데 maximal인 것들, 즉 $\Spec A$의 irreducible component들을 서로 대응시킨다. 
:::

---
**참고문헌**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).

---