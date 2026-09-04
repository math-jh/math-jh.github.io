---
title: "아핀스킴"
description: "환의 스펙트럼 위에 구조층을 정의하여 아핀스킴을 구성하고, locally ringed space와 그 사상의 정의를 다룬다."
excerpt: "Ring의 spectrum 위 structure sheaf로 정의되는 affine scheme"

categories: [Math / Scheme Theory]
permalink: /ko/math/scheme_theory/affine_schemes
sidebar: 
    nav: "scheme_theory-ko"

date: 2025-01-27
weight: 3

---


위상공간 위에 정의된 sheaf의 예시 중 가장 기본적인 것은 위상공간 위에 정의된 연속함수들의 모임이며, 우리가 정의할 $\mathcal{O}_{\Spec A}$ 또한 비슷하며, 그 차이는 연속함수들 대신 *regular function*들을 생각한다는 것이다. 

## Locally ringed space

기본적으로 위상공간 위에 정의된 sheaf에 대해서는 [\[위상수학\] §층](/ko/math/topology/sheaves)에서 이미 다루었지만, $\Spec A$에 정의할 structure sheaf를 서술하기에는 해당 글의 정의는 다소 불충분하다. 

::: 정의 1
위상공간 $X$와, 그 위에 정의된 $\cRing$-valued sheaf $\mathcal{O}_X$의 pair $(X,\mathcal{O}_X)$를 *ringed space<sub>환 달린 공간</sub>*라 부른다. 만일 $X$의 임의의 점 $x$에 대하여, $x$에서의 stalk $\mathcal{O}_{X,x}$가 항상 local ring이라면 이 pair $(X, \mathcal{O}_X)$를 *locally ringed space<sub>국소적 환 달린 공간</sub>*라 부른다. 
:::

우리의 주장은 $\Spec A$에 적당한 structure sheaf $\mathcal{O}_{\Spec A}$를 정의하여 $(\Spec A, \mathcal{O}_{\Spec A})$를 locally ringed space로 만들 수 있고, 이렇게 정의된 $\Spec$은 [§스펙트럼, ⁋명제 2](/ko/math/scheme_theory/spectrums#prop2) 혹은 [§스펙트럼, ⁋명제 8](/ko/math/scheme_theory/spectrums#prop8)과 같은 functoriality를 갖는다는 것이다. 이를 수학적으로 적기 위해서는 우선 locally ringed space들 사이의 morphism을 정의해야 한다. 

::: 정의 2
두 ringed space $(X, \mathcal{O}_X)$, $(Y, \mathcal{O}_Y)$에 대하여, 이들 사이의 morphism은 연속함수 $\varphi:X \rightarrow Y$와 $\Sh(Y;\cRing)$에서의 morphism $\varphi^\sharp:\mathcal{O}_Y \rightarrow \varphi_\ast \mathcal{O}_X$의 pair를 의미한다. 

두 locally ringed space $(X, \mathcal{O}_X)$, $(Y, \mathcal{O}_Y)$ 사이의 morphism은 ringed space로서의 morphism $(\varphi,\varphi^\sharp)$이, 추가적으로 각각의 $x\in X$에 대하여 local homomorphism $\varphi_x^\sharp:\mathcal{O}_{Y,\varphi(x)} \rightarrow \mathcal{O}_{X,x}$를 유도하는 것이다. 
:::

## $\Spec A$ 위에 정의된 대수적인 함수들

이제 $\mathcal{O}_{\Spec A}$를 정의해야 한다. 이는 이 글의 서두에서 언급한 것과 같이, $\Spec A$ 위에 정의된 대수적인 함수들의 sheaf이며, 이는 정확히 [\[대수다양체\] §아핀다양체, ⁋정의 14](/ko/math/algebraic_varieties/affine_varieties#def14)의 일반화이다. 

이 논의를 scheme으로 일반화하자. 우선 $A$의 원소는 algebraic variety에서와 마찬가지로 함수 $f$로 생각한다. 그럼 이 때 $f$의 점 $\mathfrak{p}\in\Spec A$에서의 <em-ko>함숫값</em-ko>은 canonical projection $\pi: A \rightarrow A/\mathfrak{p}$에 의한 $f$의 image이다. 그럼 특히 $f$가 점 $\mathfrak{p}$에서 $0$이 된다는 것은

$$f\equiv 0\pmod{\mathfrak{p}}\iff f\in \mathfrak{p}\iff \mathfrak{p}\in Z(f)$$

이다. 즉 $Z(f)$는 $f=0$인 점들의 모임으로 이해할 수 있으며, 그 여집합인 principal open set $D(f)$는 $f\neq 0$인 점들의 모임으로 이해할 수 있다. 

이러한 관점에서 우리는 $\Spec A$의 <em-ko>대수적인 함수들</em-ko>이 무엇인지 묘사할 수 있다. [\[대수다양체\] §아핀다양체, ⁋정의 14](/ko/math/algebraic_varieties/affine_varieties#def14)와 마찬가지로, 이들은 각 점의 적당한 근방에서 그 근방에서 $0$이 되지 않는 함수를 분모로 갖는 유리함수의 꼴로 나타나는 함수들이라 정의하면 된다. 여기에서 이 조건이 국소적인 것임에 주의해야 한다. 열린집합 전체를 정의역으로 하는 하나의 분수 표현은 일반적으로 존재하지 않으며, 이는 아래에서 실제로 정의를 내리는 principal open set에서만 보장된다.

이제 principal open set $D(f)$가 주어졌다 하자. 그럼 $D(f)$ 전체에서 하나의 유리함수 $g/h$의 꼴로 나타나는 함수들만 생각하면, 그 분모에 들어갈 수 있는 함수 $h$들은 $D(f)\subseteq D(h)$를 만족해야 한다. 

::: 보조정리 3
고정된 원소 $f\in A$에 대하여, 

$$S(f)=\{h\in A\mid D(f)\subseteq D(h)\}$$

으로 정의하자. 그럼 $S(f)$는 $A$의 multiplicative subset이다. 
:::
::: 증명
우선 $D(1)=\Spec A$이므로 $S(f)$가 empty product $1$을 포함하는 것은 자명하다. 이제 만일 $h_1,h_2\in S(f)$라면, 다음의 식

$$D(h_1h_2)=\Spec A\setminus Z(h_1h_2)=\Spec A\setminus (Z(h_1)\cup Z(h_2))=(\Spec A\setminus Z(h_1))\cap (\Spec A\setminus Z(h_2))=D(h_1)\cap D(h_2)$$

으로부터 $D(f)\subseteq D(h_1)\cap D(h_2)=D(h_1h_2)$임을 안다. 이 식은 단지 [\[대수적 구조\] §분수체, ⁋명제 8](/ko/math/algebraic_structures/field_of_fractions#prop8)을 기하학적으로 설명한 것에 불과하다. 
:::

이제 $\Spec A$의 부분집합 $D(f)$ 위에 정의된 대수적인 함수들의 모임을 $S(f)^{-1}A$로 정의해야 함이 직관적이며, 실제로 그렇게 정의할 것이다. 그 전에 우리는 다음 보조정리를 보인다. 

::: 보조정리 4
$D(f)\subseteq D(h)$가 성립하는 것은 적당한 $n\geq 1$이 존재하여 $f^n\in (h)$인 것과 동치이다.  
:::
::: 증명
$D(f)\subseteq D(h)$인 것은 $Z(h)\subseteq Z(f)$인 것과 동치이고, 이는 [§스펙트럼, ⁋보조정리 6](/ko/math/scheme_theory/spectrums#lem6)의 셋째 결과에 의하여 $\sqrt{(f)}\subseteq \sqrt{(h)}$인 것과 동치이다. 

만일 $\sqrt{(f)}\subseteq \sqrt{(h)}$라면, $(f)\subseteq \sqrt{(f)}\subseteq \sqrt{(h)}$로부터 $f\in \sqrt{(h)}$이고, 따라서 적당한 $n\geq 1$이 존재하여 $f^n\in (h)$여야 함을 안다. 거꾸로 적당한 $n\geq 1$이 존재하여 $f^n\in (h)$라면 $f\in \sqrt{(h)}$로부터 $(f)\subseteq \sqrt{(h)}$이고, 따라서

$$\sqrt{(f)}\subseteq\sqrt{\sqrt{(h)}}=\sqrt{(h)}$$

이다. 
:::

이 보조정리를 활용하면 $S(f)^{-1}A$를 더 깔끔한 방식으로 표현할 수 있다. 

::: 보조정리 5
임의의 $f\in A$에 대하여, 다음의 isomorphism 

$$S(f)^{-1}A\cong S_f^{-1}A$$

이 존재한다. 뿐만 아니라, 만일 $S(g)\subseteq S(f)$라면 다음의 diagram

{% diagram frozen/a212f2a0/Math/Scheme_Theory/Affine_Schemes-1.svg width="10.55em" alt="localizations" %}

이 commute한다.
:::
::: 증명
우선 canonical morphism들을 $\epsilon(f): A \rightarrow S(f)^{-1}A$, $\epsilon_f:A \rightarrow S_f^{-1}A$으로 표기하기로 하자. 그럼 임의의 $n\geq 1$에 대하여 $D(f)=D(f^n)$이므로 $S_f\subseteq S(f)$이고, 따라서 $S_f$의 $\epsilon(f)$에 의한 image는 모두 $S(f)^{-1}A$의 unit이다. 거꾸로 임의의 $h\in S(f)$에 대하여, [보조정리 4](#lem4)에 의하여 $f^n=ah$를 만족하는 $n\geq 1$과 $a\in A$가 존재하므로

$$\frac{h}{1}\frac{a}{f^n}=1\qquad\text{in $S_f^{-1}A$}$$

이고, 즉 $S(f)$의 $\epsilon_f$에 의한 image 또한 모두 $S_f^{-1}A$의 unit이다. 따라서 [\[가환대수학\] §국소화, ⁋명제 6](/ko/math/commutative_algebra/localization#prop6)에 의하여 두 사상

$$\overline{\epsilon_f}: S(f)^{-1}A \rightarrow S_f^{-1}A,\qquad \overline{\epsilon(f)}: S_f^{-1}A \rightarrow S(f)^{-1}A$$

이 각각 $\overline{\epsilon_f}\circ\epsilon(f)=\epsilon_f$와 $\overline{\epsilon(f)}\circ\epsilon_f=\epsilon(f)$를 만족하도록 유일하게 존재한다. 그럼 두 합성 $\overline{\epsilon(f)}\circ\overline{\epsilon_f}$와 $\overline{\epsilon_f}\circ\overline{\epsilon(f)}$는 각각 $\epsilon(f)$와 $\epsilon_f$를 extend하므로, 같은 유일성에 의하여 항등사상이다. 즉 이 둘은 서로의 역함수이며, 이로부터 주장의 isomorphism을 얻는다. 

이제 $S(g)\subseteq S(f)$라 하자. 그럼 $S(g)$의 원소들은 $\epsilon(f)$와 $\epsilon_f$ 모두에 의하여 unit으로 옮겨지고, $S_g\subseteq S(g)$이므로 다시 [\[가환대수학\] §국소화, ⁋명제 6](/ko/math/commutative_algebra/localization#prop6)에 의하여 $\epsilon(f)$와 $\epsilon_f$를 각각 extend하는 두 사상

$$\widehat{\epsilon(f)}:S(g)^{-1}A \rightarrow S(f)^{-1}A,\qquad \widecheck{\epsilon_f}: S_g^{-1}A \rightarrow S_f^{-1}A$$

이 유일하게 존재하며, 이들이 주장의 diagram의 나머지 두 변이다. 이제 두 합성 $\widecheck{\epsilon_f}\circ\overline{\epsilon_g}$와 $\overline{\epsilon_f}\circ\widehat{\epsilon(f)}$는 모두 $\epsilon(g)$와 합성하면 $\epsilon_f$가 되므로, 같은 유일성에 의하여 서로 같다. 
:::

따라서, $D(f)$ 위에 정의된 대수적인 함수들은 $S_f^{-1}A$의 원소인 것으로 생각하여도 충분하다. 앞선 글에서 우리는 편의상 $S_f^{-1}A$를 $A_f$로 표기하기로 하였다.

::: 보조정리 6
$\Spec A$의 base $\{D(f)\}_{f\in A}$들에 대하여, 각각의 $f_i\in A$마다

$$\mathcal{F}(D(f_i))=S(f_i)^{-1}A\cong A_{f_i}$$

으로 정의하자. 또, $D(f_i)\subseteq D(f_j)$를 만족하는 $f_i,f_j\in A$마다 restriction map

$$\rho_{ji}: S(f_j)^{-1}(A) \rightarrow S(f_i)^{-1}(A)$$

을 canonical morphism $A\rightarrow S(f_i)^{-1}(A)$에 [\[가환대수학\] §국소화, ⁋명제 6](/ko/math/commutative_algebra/localization#prop6)을 적용하여 얻어지는 함수로 정의하자. 그럼 이들 데이터는 [\[위상수학\] §층, ⁋명제 8](/ko/math/topology/sheaves#prop8)의 두 조건을 만족하고, 따라서 $\mathcal{F}$를 확장하는 $\Spec A$의 ($\cRing$-valued) sheaf가 유일하게 결정된다. 
:::
::: 증명
$\rho_{ji}$들이 [\[위상수학\] §준층, ⁋정의 2](/ko/math/topology/presheaves#def2)의 restriction map의 조건을 만족하는 것은 [\[가환대수학\] §국소화, ⁋명제 6](/ko/math/commutative_algebra/localization#prop6)의 universal property로부터 자명하다. 여기에서 $\rho_{ji}: S(f_j)^{-1}(A) \rightarrow S(f_i)^{-1}(A)$는, [보조정리 5](#lem5)에 의하여, 단순히 $S(f_j)^{-1}(A)$의 원소를 다음의 꼴

$$g/h,\qquad\text{where $h\in S(f_j)$}\tag{$\ast$}$$

로 나타냈을 때, 다음 식

$$h\in S(f_j)\iff D(f_j)\subseteq D(h)\implies D(f_i)\subseteq D(h)\iff h\in S(f_i)$$

로부터 ($\ast$)를 $S(f_i)^{-1}(A)$의 원소로도 볼 수 있으므로 이 과정을 통해 $g/h\in S(f_j)^{-1}(A)$를 $g/h\in S(f_i)^{-1}(A)$로 이해하는 함수이다.

이제 [\[위상수학\] §층, ⁋명제 8](/ko/math/topology/sheaves#prop8)의 두 조건을 증명한다. 표기의 편의를 위해 $D(f)=\Spec A_f$이므로, $A$를 $A_f$로 바꾸고 나면 $f=1$인 경우만 생각하면 충분하다. $\Spec A=\bigcup_{i\in I}D(f_i)$를 만족하는 $f_i\in A$들을 고정하자. 

우선 첫째 조건을 보이기 위해, 원소 $s\in A$가 모든 $i\in I$에 대해 $S(f_i)^{-1}A$에서 $s=0$를 만족한다 하고, $s$가 $A$의 원소로서도 $0$이 됨을 보이자. 그럼 [§스펙트럼, ⁋보조정리 12](/ko/math/scheme_theory/spectrums#lem12)에 의해 $(f_i)$의 원소들 중 $\Spec A=\bigcup_{i=1}^n D(f_i)$이도록 하는 $f_1,\ldots, f_n$을 택할 수 있고, 가정에 의해 모든 $i=1,\ldots, n$에 대해 다음의 식

$$f_i^{m_i}s=0$$

을 만족하는 $m_i\geq 1$들이 존재한다. 한편 [§스펙트럼, ⁋보조정리 11](/ko/math/scheme_theory/spectrums#lem11) 이후의 계산으로부터 $D(f_i^{m_i})=D(f_i)$가 모든 $i$에 대해 성립하므로,

$$\Spec A=\bigcup_{i=1}^n D(f_i^{m_i})$$

이고, 이로부터 $1=\sum_{i=1}^n a_i f_i^{m_i}$이도록 하는 $a_i\in A$들이 존재한다. (참고: [§스펙트럼, ⁋보조정리 12](/ko/math/scheme_theory/spectrums#lem12)의 증명, 혹은 [\[가환대수학\] §정수적 확장, ⁋명제 15](/ko/math/commutative_algebra/integral_extension#prop15)의 증명)

따라서

$$s=1s=\left(\sum_{i=1}^n a_i f_i^{m_i}\right)s=\sum_{i=1}^n a_i (f_i^{m_i}s)=0$$

이다. 

이제 둘째 조건을 보이기 위해, 각각의 $i$마다 $S(f_i)^{-1}A$의 원소 $s_i=a_i/f_i^{m_i}$가 존재하여, 각각의 $i,j$마다

$$\frac{a_i}{f_i^{m_i}}=\frac{a_j}{f_j^{m_j}}\quad\text{ in $D(f_i)\cap D(f_j)=D(f_if_j)$}$$

이도록 할 수 있다. 여기에서 $a/1=af_i/f_i$이므로 모든 $i$에 대하여 $m_i\geq 1$이도록 택할 수 있다. 그런데 $D(f_i)=D(f_i^{m_i})$이고 $D(f_j)=D(f_j^{m_j})$이므로

$$D(f_if_j)=D(f_i)\cap D(f_j)=D(f_i^{m_i})\cap D(f_j^{m_j})=D(f_i^{m_i}f_j^{m_j})$$

이고, 따라서 적당한 $N_{ij}$가 존재하여

$$(f_i^{m_i}f_j^{m_j})^{N_{ij}}(a_if_j^{m_j}-a_jf_i^{m_i})=0$$

이도록 할 수 있다. $N=\max_{i,j}\{N_{ij}\}$라 하여 

$$(f_i^{m_i}f_j^{m_j})^N(a_if_j^{m_j}-a_jf_i^{m_i})=0$$

즉,

$$a_if_i^{Nm_i}f_j^{Nm_j+m_j}=a_jf_j^{Nm_j}f_i^{Nm_i+m_i}$$

를 얻자. 그럼 주어진 가정

$$\Spec A=\bigcup_{i=1}^n D(f_i)=\bigcup_{i=1}^n D(f_i^{Nm_i+m_i})$$

로부터 우리는 적당한 $b_i\in A$들이 존재하여

$$1=\sum_{i=1}^n b_if_i^{Nm_i+m_i}$$

이도록 할 수 있다. 이제 $s=\sum_{i=1}^n b_ia_i f_i^{Nm_i}$라 하면,

$$sf_j^{Nm_j+m_j}=\sum_{i=1}^n b_ia_i f_i^{Nm_i} f_j^{Nm_j+m_j}=\sum_{i=1}^nb_ia_jf_j^{Nm_j}f_i^{Nm_i+m_i}=a_jf_j^{Nm_j}$$

이므로 $f_j^{Nm_j}(sf_j^{m_j}-a_j)=0$이 모든 $j$에 대해 성립하고, 따라서 $D(f_j)$에서

$$\frac{s}{1}=\frac{a_j}{f_j^{m_j}}$$

이다. 이로부터 원하는 $s$를 얻는다. 

만일 $I$가 무한집합일 경우, $\Spec A=\bigcup_{j\in J} D(f_j)$를 만족하는 $I$의 유한한 부분집합 $J=\{1,\ldots, n\}$을 택하여 위와 같이 반복하여 $s\in \mathcal{F}(\Spec A)$를 얻은 후 이것이 $\alpha\in I\setminus J$인 $D(f_\alpha)$에서도 $s_\alpha=s\vert_{D(f_\alpha)}$를 만족함을 보이면 된다. 이를 보이기 위해 유한집합

$$J\cup\{\alpha\}=\{1,2,\ldots, n,\alpha\}\subseteq I$$

에 대해서도 위와 같은 과정을 반복하여 $s'\in \mathcal{F}(\Spec A)$를 얻자. 그럼 $s$와 $s'$는 정의에 의해 $i=1,\ldots, n$마다 $s\vert_{D(f_i)}=s'\vert_{D(f_i)}$를 만족하고 $\Spec A=\bigcup D(f_i)$이므로, 위에서 보인 [\[위상수학\] §층, ⁋명제 8](/ko/math/topology/sheaves#prop8)의 첫째 조건에 의해 $s=s'$임을 알고 이로부터 

$$s\vert_{D(f_\alpha)}=s'\vert_{D(f_\alpha)}=s_\alpha$$

임을 안다. 이것이 모든 $\alpha$에 대해 성립하므로 $s$는 임의의 $D(f_\alpha)$로 제한했을 때도 $s_\alpha$가 된다. 
:::

::: 정의 7
[보조정리 6](#lem6)에 의해 정의되는 $\Spec A$ 위의 sheaf를 $\mathcal{O}_{\Spec A}$로 쓰고, 이를 *structure sheaf<sub>구조층</sub>*라 부른다. 
:::

이 정의는 principal open set에서만 이루어졌지만, $D(f)$들이 $\Spec A$의 base이므로 임의의 열린집합 $U$에서의 section들은 [\[위상수학\] §층, ⁋명제 8](/ko/math/topology/sheaves#prop8)의 확장을 통해 결정된다. 즉 $\mathcal{O}_{\Spec A}(U)$의 원소는 $U$를 덮는 $D(f)$들 위에서 $g/h$의 꼴로 주어지고 교집합에서 서로 일치하는 데이터들이며, 이것이 앞서 말한 국소적인 정의에 해당한다. 

그럼 $(\Spec A,\mathcal{O}_{\Spec A})$는 locally ringed space 이다. 

::: 보조정리 8
$(\Spec A,\mathcal{O}_{\Spec A})$와 임의의 점 $\mathfrak{p}\in \Spec A$에 대하여, isomorphism

$$A_\mathfrak{p}\cong \mathcal{O}_{\Spec A, \mathfrak{p}}=\varinjlim_\text{\scriptsize $U\ni\mathfrak{p}$ open} \mathcal{O}_{\Spec A}(U)$$

이 존재한다. 뿐만 아니라, $\mathfrak{p}\in D(f)$를 만족하는 임의의 $f\in A$에 대하여, 다음의 diagram

{% diagram Math/Scheme_Theory/Affine_Schemes-7.svg width="14.55em" alt="stalk_and_localization-1" %}

이 commute한다. 
:::
::: 증명
[§스펙트럼, ⁋보조정리 11](/ko/math/scheme_theory/spectrums#lem11)에 의하여 $D(f)$들이 $\Spec A$의 base이므로, [\[위상수학\] §위상공간의 기저, ⁋명제 5](/ko/math/topology/topological_bases#prop5)에 의하여 

$$\mathcal{O}_{\Spec A, \mathfrak{p}}=\varinjlim_{D(f)\ni\mathfrak{p}} \mathcal{O}_{\Spec A}(D(f))$$

이 성립한다. 한편 $\mathfrak{p}\in D(f)\iff f\not\in \mathfrak{p}$이므로, 우리는 다음의 diagram

{% diagram frozen/a212f2a0/Math/Scheme_Theory/Affine_Schemes-8.svg width="37.01em" alt="stalk_and_localization-2" %}

을 얻고, 따라서 주어진 isomorphism을 보이는 것은 단순히 다음의 대수적인 isomorphism

$$A_\mathfrak{p}\cong \varinjlim_{\mathfrak{p}\not\ni f} A_f\tag{$\ast\ast$}$$

을 보이는 것과 같고, 이는 [\[가환대수학\] §국소화, ⁋명제 6](/ko/math/commutative_algebra/localization#prop6)의 universal property와 direct limit의 universal property를 각각 사용하면 된다. 주장의 diagram은 isomorphism ($\ast\ast$)을 통해 위의 diagram에서 $\varinjlim A_f$를 $A_\mathfrak{p}$로 바꾸어주면 된다. 
:::

이제 드디어 $\Spec$의 functoriality를 우리가 원하는 형태로 적을 준비가 되었다. 

::: 명제 9
대응 $A\mapsto (\Spec A, \mathcal{O}_{\Spec A})$는 functor $\Spec: \cRing^\op \rightarrow \LRS$를 정의한다. 
:::
::: 증명
우리는 이미 ring homomorphism $\phi: A \rightarrow B$가 연속함수 $\Spec\phi: \Spec B \rightarrow \Spec A$를 유도하는 것을 안다. ([§스펙트럼, ⁋명제 8](/ko/math/scheme_theory/spectrums#prop8)) 따라서 

$$(\Spec\phi)^\sharp: \mathcal{O}_{\Spec A} \rightarrow (\Spec\phi)_\ast \mathcal{O}_{\Spec B}$$

를 묘사하면 충분하다. 이를 위해서는 principal open set에서의 함수

$$(\Spec\phi)^\sharp(D(f)): \mathcal{O}_{\Spec A}(D(f)) \rightarrow \mathcal{O}_{\Spec B}((\Spec \phi)^{-1}(D(f)))$$

를 보면 된다. 한편 [§스펙트럼, ⁋명제 8](/ko/math/scheme_theory/spectrums#prop8)의 증명에서

$$(\Spec\phi)^{-1}(Z(f))=Z(\phi(f))$$

이므로

$$(\Spec\phi)^{-1}(D(f))=D(\phi(f))$$

임을 안다. 따라서, structure sheaf의 정의에 의하여 $(\Spec\phi)^\sharp(D(f))$를 정의하는 것은

$$A_f \rightarrow B_{\phi(f)}$$

를 정의하는 것과 같고, 이는 합성

$$A \overset{\phi}{\longrightarrow}B \overset{\epsilon}{\longrightarrow} B_{\phi(f)}$$

에 [\[가환대수학\] §국소화, ⁋명제 6](/ko/math/commutative_algebra/localization#prop6)을 적용하여 얻어진다. 물론 이렇게 정의된 사상들이 restriction map과 가환함을 보여야 한다. $D(g)\subseteq D(f)$라 하면 $D(\phi(g))\subseteq D(\phi(f))$이고, 두 합성

$$A_f \longrightarrow B_{\phi(f)} \longrightarrow B_{\phi(g)},\qquad A_f \longrightarrow A_g \longrightarrow B_{\phi(g)}$$

은 모두 $\epsilon_f$와 합성하면 $A \rightarrow B \rightarrow B_{\phi(g)}$가 되므로, 위의 유일성에 의하여 서로 같다.

이제 임의의 열린집합 $U\subseteq \Spec A$와 $s\in \mathcal{O}_{\Spec A}(U)$에 대하여, $U$에 포함되는 principal open set $D(f)$들마다 section $(\Spec\phi)^\sharp(D(f))(s\vert_{D(f)})$을 생각하자. 두 principal open set의 교집합 $D(f)\cap D(g)=D(fg)$ 또한 principal open set이므로, 위의 가환성으로부터 이 section들은 교집합 위에서 서로 일치하고, 따라서 sheaf $(\Spec\phi)_\ast\mathcal{O}_{\Spec B}$의 gluability axiom과 identity axiom에 의하여 이들은 유일한 $(\Spec\phi)^\sharp(U)(s)$로 붙는다. 이렇게 정의된 $(\Spec\phi)^\sharp(U)$가 ring homomorphism이며 restriction map과 가환하는 것 또한 identity axiom으로부터 얻어지고, 따라서 우리는 sheaf morphism $(\Spec\phi)^\sharp$을 얻는다.

이상에서 $(\Spec\phi, (\Spec\phi)^\sharp): (\Spec B, \mathcal{O}_{\Spec B}) \rightarrow (\Spec A, \mathcal{O}_{\Spec A})$가 ringed space들 사이의 morphism인 것을 안다. 이제 이것이 locally ringed space들 사이의 morphism임을 보이기 위해서는 임의의 $\mathfrak{q}\in \Spec B$에 대하여

$$(\Spec\phi)^\sharp_\mathfrak{q}:\mathcal{O}_{\Spec A, (\Spec \phi)(\mathfrak{q})} \rightarrow\mathcal{O}_{\Spec B, \mathfrak{q}}$$

이 local homomorphism이면 된다. 그런데 $(\Spec \phi)(\mathfrak{q})=\phi^{-1}(\mathfrak{q})$이고, 따라서 [보조정리 8](#lem8)에 의하여 $(\Spec\phi)^\sharp_\mathfrak{q}$는 $A_{\phi^{-1}(\mathfrak{q})}$에서 $B_{\mathfrak{q}}$로의 ring homomorphism이며 이는 $A_{\phi^{-1}(\mathfrak{q})}$의 유일한 maximal ideal $\phi^{-1}(\mathfrak{q})A_{\phi^{-1}(\mathfrak{q})}$를 $B_\mathfrak{q}$의 유일한 maximal ideal $\mathfrak{q}B_\mathfrak{q}$로 보낸다. 

마지막으로 functoriality를 확인하자. 점 사이의 사상에 대해서는 이미 [§스펙트럼, ⁋명제 2](/ko/math/scheme_theory/spectrums#prop2)에서 확인하였으므로 structure sheaf 쪽만 보면 된다. $\phi=\id_A$인 경우 위의 구성은 각각의 $D(f)$마다 $\epsilon_f$를 extend하는 유일한 사상 $A_f \rightarrow A_f$를 주고 이는 항등사상이므로, $\Spec(\id_A)=\id$이다. 또 두 ring homomorphism $\phi: A \rightarrow B$와 $\psi: B \rightarrow C$에 대하여, $\Spec(\psi\circ\phi)^\sharp(D(f))$는 합성 $A \rightarrow C \rightarrow C_{\psi(\phi(f))}$를 확장하는 유일한 사상이고 합성 $A_f \rightarrow B_{\phi(f)} \rightarrow C_{\psi(\phi(f))}$ 또한 같은 사상을 확장하므로, 유일성에 의하여 이 둘은 같다. 두 sheaf morphism이 base 위에서 일치하므로 $\Spec(\psi\circ\phi)=(\Spec\phi)\circ(\Spec\psi)$이다. 
:::

## 아핀스킴

::: 정의 10
[명제 9](#prop9)의 functor $\Spec:\cRing^\op \rightarrow \LRS$의 essential image를 *affine scheme<sub>아핀스킴</sub>*으로 정의한다. 
:::

Affine scheme들의 category를 $\AffSch$로 적는다. 그럼 functor $\Spec:\cRing^\op \rightarrow \AffSch$는 그 정의에 의해 essentially surjective이다. ([\[범주론\] §자연변환, ⁋정리 5](/ko/math/category_theory/natural_transformations#thm5)) 또, 만일 $(\varphi, \varphi^\sharp): (\Spec B, \mathcal{O}_{\Spec B}) \rightarrow (\Spec A, \mathcal{O}_{\Spec A})$이 어떠한 ring homomorphism $\phi$로부터 유도된 것이라면, [명제 9](#prop9)의 증명에서 $1=f\in A$로 잡으면

$$\varphi^\sharp(D(1))= \bigl(A \overset{\phi}{\longrightarrow} B \overset{\id_B}{\longrightarrow} B_{\phi(1)}=B\bigr)=\phi$$

이므로, 이 functor는 반드시 faithful이다. 뿐만 아니라 다음이 성립한다.

::: 명제 11
Functor $\Spec: \cRing^\op \rightarrow \LRS$는 fully faithful이다. 
:::
::: 증명
 임의의 두 affine scheme $(X, \mathcal{O}_{X})$, $(Y, \mathcal{O}_{Y})$와 이들 사이의 morphism

$$(X, \mathcal{O}_{X}) \rightarrow (Y, \mathcal{O}_{Y})$$

이 주어졌다 하면, isomorphism $(\Spec B, \mathcal{O}_{\Spec B})\cong (X, \mathcal{O}_X)$, $(\Spec A, \mathcal{O}_{\Spec A})\cong (Y, \mathcal{O}_Y)$을 통해 이를 두 spectrum들 사이의 (locally ringed space로서의) morphism 

$$(\varphi, \varphi^\sharp): (\Spec B, \mathcal{O}_{\Spec B}) \rightarrow (\Spec A, \mathcal{O}_{\Spec A})$$

으로 볼 수 있다. 따라서 이 locally ringed space들 사이의 morphism이 적당한 ring homomorphism $\phi$로부터 나오는 것을 증명하면 충분하다. $\Spec$이 faithful이라는 위의 증명에서 힌트를 얻어,

$$\phi=\varphi^\sharp(D(1)):A \rightarrow B$$

를 통해 ring homomorphism $\phi:A \rightarrow B$를 정의하면 이제 주장을 완성하기 위해서는 $\Spec\phi=(\varphi,\varphi^\sharp)$임을 보여야 한다. 우선 임의의 $\mathfrak{q}\in \Spec B$에 대하여

$$(\Spec \phi)(\mathfrak{q})=\phi^{-1}(\mathfrak{q})=\varphi(\mathfrak{q})$$

임을 보이자. 우선 [보조정리 8](#lem8)에서 $f=1$로 두면 우리는 다음의 diagram

{% diagram frozen/a212f2a0/Math/Scheme_Theory/Affine_Schemes-9.svg width="39.41em" alt="faithful" %}

을 얻는다. 이 diagram에서 수직방향 함수들은 모두 isomorphism들이고, 다음의 면

{% diagram Math/Scheme_Theory/Affine_Schemes-10.svg width="13.26em" alt="commuting_square" %}

을 제외한 모든 면들은 commuting square임을 알고 있다. 따라서 위의 diagram에서 $A \rightarrow \mathcal{O}_{\Spec B, \mathfrak{q}}$는 어떤 함수를 타고 가도 동일하게 결정되며, 이 함수에 [\[가환대수학\] §국소화, ⁋명제 6](/ko/math/commutative_algebra/localization#prop6)를 적용하면 $A_{\varphi(\mathfrak{q})} \rightarrow \mathcal{O}_{\Spec B, \mathfrak{q}}$가 유일하게 결정된다. 이로부터 위의 diagram의 <em-ko>모든</em-ko> 면들이 commuting square인 것을 안다. 즉, $\phi_\mathfrak{q}:A_{\varphi(\mathfrak{q})}\rightarrow B_\mathfrak{q}$도 local homomorphism이고, 따라서 $\phi^{-1}(\mathfrak{q})=\varphi(\mathfrak{q})$임을 안다. 

이제 두 sheaf morphism이 같다는 것을 보이자. $\varphi^\sharp$이 restriction map과 commute하므로 임의의 $f\in A$에 대하여

$$\varphi^\sharp(D(f))\circ\epsilon_f=\epsilon_{\phi(f)}\circ\phi$$

가 성립한다. 그런데 [명제 9](#prop9)의 구성에서 $(\Spec\phi)^\sharp(D(f))$는 정확히 이 식을 만족하는 유일한 사상이었으므로, [\[가환대수학\] §국소화, ⁋명제 6](/ko/math/commutative_algebra/localization#prop6)의 유일성에 의하여 $\varphi^\sharp(D(f))=(\Spec\phi)^\sharp(D(f))$이다. 두 sheaf morphism이 base $\{D(f)\}_{f\in A}$ 위에서 일치하므로, $\varphi_\ast\mathcal{O}_{\Spec B}$의 identity axiom에 의하여 $\varphi^\sharp=(\Spec\phi)^\sharp$이다. 
:::

따라서 $\Spec$을 $\cRing$에서 $\AffSch$로의 contravariant functor로 보면 $\Spec$은 두 category $\cRing^\op$와 $\AffSch$ 사이의 categorical equivalence이다. 뿐만 아니라, [명제 11](#prop11)에 의해 $\AffSch$는 $\LRS$의 full subcategory이다. 

한편 임의의 spectrum $(\Spec A, \mathcal{O}_{\Spec A})$에 대하여, 우리는 정의에 의해 

$$\mathcal{O}_{\Spec A}(\Spec A)=\mathcal{O}_{\Spec A}(D(1))\cong A$$

임을 안다. 만일 locally ringed space $(X, \mathcal{O}_X)$가 affine scheme이었다면, 마찬가지 방식으로 $\mathcal{O}_X(X)$를 살펴보아 $(X, \mathcal{O}_X)$가 어떠한 ring의 spectrum과 isomorphic한지 알 수 있다. 즉, affine scheme $(X, \mathcal{O}_X)$에 대하여 $A=\mathcal{O}_X(X)$라 하면 $(X, \mathcal{O}_X)\cong (\Spec A, \mathcal{O}_{\Spec A})$가 성립한다. 더 일반적으로 다음을 정의한다.

::: 정의 12
*Global section functor<sub>전역 단면 함자</sub>* $\Gamma:\LRS \rightarrow \cRing^\op$를, 임의의 locally ringed space $(X, \mathcal{O}_X)$에 대하여 대응

$$X\mapsto \Gamma(X, \mathcal{O}_X)=\mathcal{O}_X(X)$$

로, 그리고 임의의 morphism $(\varphi,\varphi^\sharp):(X,\mathcal{O}_X) \rightarrow (Y, \mathcal{O}_Y)$에 대하여

$$\Gamma(\varphi,\varphi^\sharp)=\varphi^\sharp(Y):\Gamma(Y, \mathcal{O}_Y) \rightarrow (\varphi_\ast\mathcal{O}_X)(Y)=\Gamma(X, \mathcal{O}_X)$$

로 정의한다.[^1] 
:::

여기에서 $\varphi^\sharp(Y)$는 $\cRing$에서 $\Gamma(Y)$로부터 $\Gamma(X)$로 가는 사상이므로, 우리는 이를 $\cRing^\op$에서의 사상 $\Gamma(X) \rightarrow \Gamma(Y)$로 읽을 수 있다. 이 대응이 항등사상과 합성을 보존하는 것은 ringed space들 사이의 morphism의 합성이 $\varphi^\sharp$들의 합성으로 주어지는 것에서 따라오므로, 이는 실제로 functor가 된다.

한편 [명제 11](#prop11)의 증명에서 주목할 만한 사실은 $(X, \mathcal{O}_X)$가 affine scheme이라는 가정은 필요가 없다는 사실이다. 즉, $(X, \mathcal{O}_X)\cong(\Spec B, \mathcal{O}_{\Spec B})$라는 가정을 버리고 [명제 11](#prop11)의 diagram 대신 다음의 diagram

{% diagram frozen/a212f2a0/Math/Scheme_Theory/Affine_Schemes-11.svg width="34.92em" alt="adjoint" %}

을 사용하여도 비슷한 논증을 해 나갈 수 있으며, 이 때 결론의 $B$는 $\Gamma(X, \mathcal{O}_X)$로 바뀌게 된다. 어차피 $\mathcal{O}_X$는 $X$에 의해 결정되는 데이터이므로, 이를 간략히 $\Gamma(X)$로만 표기하면 이로부터 다음의 정리를 얻는다.

::: 정리 13
임의의 locally ringed space $(X, \mathcal{O}_X)$와 ring $A$에 대하여, 다음의 natural isomorphism

$$\Hom_\LRS(X, \Spec A)\cong \Hom_{\cRing^\op}(\Gamma(X), A)=\Hom_{\cRing}(A, \Gamma(X))$$

이 존재한다. 즉, global section functor $\Gamma: \LRS \rightarrow \cRing^\op$는 $\Spec$ functor $\Spec:\cRing^\op \rightarrow \LRS$의 left adjoint이다. 
:::
::: 증명
[보조정리 6](#lem6)의 isomorphism $\mathcal{O}_{\Spec A}(D(f))\cong A_f$를 통해 $\mathcal{O}_{\Spec A}(\Spec A)=\mathcal{O}_{\Spec A}(D(1))$을 $A$와 동일시하기로 하자. 그럼 이 동일시 하에서 $\mathcal{O}_{\Spec A}$의 restriction map $\mathcal{O}_{\Spec A}(\Spec A) \rightarrow \mathcal{O}_{\Spec A}(D(f))$은 canonical morphism $\epsilon_f: A \rightarrow A_f$이다. 

우선 두 대응 $\Phi$와 $\Psi$를 정의한 후, 이들이 서로의 역임을 보인다. Locally ringed space들 사이의 morphism $(\varphi,\varphi^\sharp): X \rightarrow \Spec A$가 주어졌다 하면, $\varphi^\sharp$를 열린집합 $\Spec A$에서 계산하여 ring homomorphism

$$\Phi(\varphi,\varphi^\sharp)=\varphi^\sharp(\Spec A): A=\mathcal{O}_{\Spec A}(\Spec A) \rightarrow (\varphi_\ast\mathcal{O}_X)(\Spec A)=\mathcal{O}_X(X)=\Gamma(X)$$

를 얻는다. 

거꾸로 ring homomorphism $\phi:A \rightarrow \Gamma(X)$가 주어졌다 하자. 각각의 $x\in X$마다 $\phi$와 germ을 취하는 함수 $\Gamma(X) \rightarrow \mathcal{O}_{X,x}$를 합성하여 얻어지는 ring homomorphism을 $\phi_x:A \rightarrow \mathcal{O}_{X,x}$라 적자. 즉 $\phi_x(a)=\phi(a)_x$이다. 이제 $(X,\mathcal{O}_X)$가 locally ringed space이므로 $\mathcal{O}_{X,x}$는 유일한 maximal ideal $\mathfrak{m}_x$를 갖는 local ring이고, 따라서 [\[대수적 구조\] §분수체, ⁋명제 9](/ko/math/algebraic_structures/field_of_fractions#prop9)에 의하여

$$\varphi(x)=\phi_x^{-1}(\mathfrak{m}_x)$$

는 $A$의 prime ideal, 즉 $\Spec A$의 점이다. 

이렇게 정의된 함수 $\varphi: X \rightarrow \Spec A$가 연속임을 보이자. 이를 위해 임의의 $s\in \Gamma(X)$에 대하여 

$$X_s=\{x\in X\mid \text{$s_x\not\in \mathfrak{m}_x$}\}$$

이 $X$의 열린집합임을 보인다. [\[가환대수학\] §국소화, ⁋명제 2](/ko/math/commutative_algebra/localization#prop2)에 의하여 local ring $\mathcal{O}_{X,x}$의 non-unit들을 모두 모아둔 것이 $\mathfrak{m}_x$이므로, $x\in X_s$인 것은 $s_x$가 $\mathcal{O}_{X,x}$의 unit인 것과 동치이다. 이제 $x\in X_s$라 하면 $s_xt=1$을 만족하는 $t\in \mathcal{O}_{X,x}$가 존재하고, $x$의 적당한 열린근방 $W$와 $t$를 대표하는 section $u\in \mathcal{O}_X(W)$를 택하면 $(s\vert_Wu)_x=1_x$이므로, 필요하다면 $W$를 더 작게 잡아 $\mathcal{O}_X(W)$에서 $s\vert_Wu=1$이도록 할 수 있다. 그럼 임의의 $y\in W$에 대하여 $s_yu_y=1$이므로 $s_y$는 $\mathcal{O}_{X,y}$의 unit이고, 따라서 $W\subseteq X_s$이다. 즉 $X_s$는 열린집합이다. 

한편 임의의 $f\in A$에 대하여

$$\varphi^{-1}(D(f))=\{x\in X\mid f\not\in \varphi(x)\}=\{x\in X\mid \phi(f)_x\not\in \mathfrak{m}_x\}=X_{\phi(f)}$$

이고, principal open set들이 $\Spec A$의 base를 이루므로 ([§스펙트럼, ⁋보조정리 11](/ko/math/scheme_theory/spectrums#lem11)) $\varphi$는 연속함수이다. 

이제 sheaf morphism $\varphi^\sharp: \mathcal{O}_{\Spec A} \rightarrow \varphi_\ast \mathcal{O}_X$를 정의한다. 각각의 $f\in A$마다 $V_f=\varphi^{-1}(D(f))=X_{\phi(f)}$라 하고, $\phi$와 restriction map을 합성하여 얻어지는 ring homomorphism을

$$\theta_f: A\overset{\phi}{\longrightarrow} \Gamma(X) \longrightarrow \mathcal{O}_X(V_f)$$

라 적자. 우리의 주장은 $\theta_f(f)=\phi(f)\vert_{V_f}$가 $\mathcal{O}_X(V_f)$의 unit이라는 것이다. 실제로 $V_f$의 정의에 의하여 임의의 $y\in V_f$마다 $\phi(f)_y$는 $\mathcal{O}_{X,y}$의 unit이므로, 위의 논증을 반복하면 $y$의 열린근방 $W_y\subseteq V_f$와 $u_y\in \mathcal{O}_X(W_y)$가 존재하여 $\phi(f)\vert_{W_y}u_y=1$이도록 할 수 있다. 그럼 교집합 $W_y\cap W_{y'}$ 위에서 $u_y$와 $u_{y'}$의 restriction은 모두 $\phi(f)\vert_{W_y\cap W_{y'}}$의 곱셈에 대한 역원이므로 서로 같고, 따라서 [\[위상수학\] §층, ⁋정의 1](/ko/math/topology/sheaves#def1)의 gluability axiom에 의하여 이들은 하나의 $u\in \mathcal{O}_X(V_f)$로 붙는다. 이제 $\phi(f)\vert_{V_f}u$와 $1$은 각각의 $W_y$로 제한하면 서로 같으므로, identity axiom에 의하여 $\phi(f)\vert_{V_f}u=1$이다. 

특히 $\theta_f$는 multiplicative subset $S_f=\{1,f,f^2,\ldots\}$의 원소들을 모두 $\mathcal{O}_X(V_f)$의 unit으로 보내므로, [\[가환대수학\] §국소화, ⁋명제 6](/ko/math/commutative_algebra/localization#prop6)에 의하여

$$\varphi^\sharp(D(f))\circ \epsilon_f=\theta_f$$

를 만족하는 ring homomorphism

$$\varphi^\sharp(D(f)): A_f=\mathcal{O}_{\Spec A}(D(f)) \rightarrow \mathcal{O}_X(V_f)=(\varphi_\ast\mathcal{O}_X)(D(f))$$

가 유일하게 존재한다. 만일 $D(g)\subseteq D(f)$라면 $V_g\subseteq V_f$이고, 두 합성

$$A_f \overset{\varphi^\sharp(D(f))}{\longrightarrow} \mathcal{O}_X(V_f) \longrightarrow \mathcal{O}_X(V_g),\qquad A_f \longrightarrow A_g \overset{\varphi^\sharp(D(g))}{\longrightarrow} \mathcal{O}_X(V_g)$$

은 모두 $\epsilon_f$와 합성하면 $\theta_g$가 되므로, 다시 [\[가환대수학\] §국소화, ⁋명제 6](/ko/math/commutative_algebra/localization#prop6)의 유일성에 의하여 서로 같다. 즉 $\varphi^\sharp(D(f))$들은 restriction map과 가환한다. 

그럼 [명제 9](#prop9)의 증명에서와 같이, base 위에서 이렇게 주어진 사상들은 $\varphi_\ast\mathcal{O}_X$의 gluability axiom과 identity axiom에 의하여 sheaf morphism $\varphi^\sharp$으로 유일하게 확장된다. 

마지막으로 $(\varphi,\varphi^\sharp)$가 locally ringed space들 사이의 morphism임을 보이자. 임의의 $x\in X$와 $\mathfrak{p}=\varphi(x)$에 대하여, [보조정리 8](#lem8)에 의하여 $\mathcal{O}_{\Spec A,\mathfrak{p}}\cong A_\mathfrak{p}$이며 이 동일시 하에서 $\varphi^\sharp$이 유도하는 stalk 사이의 morphism $\varphi_x^\sharp: A_\mathfrak{p} \rightarrow \mathcal{O}_{X,x}$는, 식 $\varphi^\sharp(D(f))\circ\epsilon_f=\theta_f$의 양변에 $x$에서의 germ을 취하면

$$\varphi^\sharp_x\circ\epsilon=\phi_x$$

를 만족함을 알 수 있다. 여기에서 $\epsilon: A \rightarrow A_\mathfrak{p}$는 canonical morphism이다. 이제 임의의 $a/s\in A_\mathfrak{p}$에 대하여 $s\not\in \mathfrak{p}=\phi_x^{-1}(\mathfrak{m}_x)$이므로 $\phi_x(s)$는 unit이고, 따라서

$$\varphi_x^\sharp(a/s)=\phi_x(a)\phi_x(s)^{-1}$$

이 성립한다. 특히 $a\in \mathfrak{p}$라면 $\phi_x(a)\in \mathfrak{m}_x$이므로 $\varphi_x^\sharp(a/s)\in \mathfrak{m}_x$이고, 즉 ideal $(\varphi_x^\sharp)^{-1}(\mathfrak{m}_x)$는 $\mathfrak{p}A_\mathfrak{p}$를 포함한다. 한편 $\varphi_x^\sharp(1)=1\not\in \mathfrak{m}_x$이므로 이 ideal은 $A_\mathfrak{p}$ 전체가 아니며, $\mathfrak{p}A_\mathfrak{p}$가 $A_\mathfrak{p}$의 유일한 maximal ideal이므로 ([\[가환대수학\] §국소화, ⁋명제 8](/ko/math/commutative_algebra/localization#prop8))

$$(\varphi_x^\sharp)^{-1}(\mathfrak{m}_x)=\mathfrak{p}A_\mathfrak{p}$$

이다. 즉 $\varphi_x^\sharp$는 local homomorphism이고, [정의 2](#def2)에 의하여 $\Psi(\phi)=(\varphi,\varphi^\sharp)$는 locally ringed space들 사이의 morphism이다. 

이제 $\Phi$와 $\Psi$가 서로의 역임을 보이자. 우선 $\Psi(\phi)=(\varphi,\varphi^\sharp)$에 대하여, $f=1$로 두면 $D(1)=\Spec A$, $V_1=X$이고 $\epsilon_1=\id_A$이므로 위의 construction은

$$\Phi(\Psi(\phi))=\varphi^\sharp(\Spec A)=\theta_1=\phi$$

를 준다. 

거꾸로 locally ringed space들 사이의 morphism $(\varphi,\varphi^\sharp): X \rightarrow \Spec A$가 주어졌다 하고, $\phi=\Phi(\varphi,\varphi^\sharp)=\varphi^\sharp(\Spec A)$, 그리고 $\Psi(\phi)=(\varphi',(\varphi')^\sharp)$라 하자. 임의의 $x\in X$에 대하여, $\varphi^\sharp$이 restriction map과 가환하므로 $\varphi^\sharp$이 유도하는 stalk 사이의 morphism $\varphi_x^\sharp: \mathcal{O}_{\Spec A, \varphi(x)}\cong A_{\varphi(x)} \rightarrow \mathcal{O}_{X,x}$는 $\varphi_x^\sharp\circ\epsilon=\phi_x$를 만족하며, 여기에서 $\epsilon: A \rightarrow A_{\varphi(x)}$가 canonical morphism인 것은 [보조정리 8](#lem8)로부터 얻어진다. 한편 $(\varphi,\varphi^\sharp)$가 locally ringed space들 사이의 morphism이므로 $\varphi_x^\sharp$는 local homomorphism이고, 즉 ideal $(\varphi_x^\sharp)^{-1}(\mathfrak{m}_x)$는 $\varphi(x)A_{\varphi(x)}$를 포함하는 proper ideal, 즉 $\varphi(x)A_{\varphi(x)}$ 자기 자신이다. 따라서 [\[가환대수학\] §국소화, ⁋명제 8](/ko/math/commutative_algebra/localization#prop8)에 의하여

$$\varphi'(x)=\phi_x^{-1}(\mathfrak{m}_x)=\epsilon^{-1}\left((\varphi_x^\sharp)^{-1}(\mathfrak{m}_x)\right)=\epsilon^{-1}\left(\varphi(x)A_{\varphi(x)}\right)=\varphi(x)$$

를 얻고, 두 연속함수 $\varphi$와 $\varphi'$은 같다. 이제 $\varphi^\sharp$이 restriction map과 가환하는 것으로부터 임의의 $f\in A$에 대하여

$$\varphi^\sharp(D(f))\circ\epsilon_f=\theta_f$$

가 성립하고, 이는 정확히 $(\varphi')^\sharp(D(f))$를 정의한 식이므로 [\[가환대수학\] §국소화, ⁋명제 6](/ko/math/commutative_algebra/localization#prop6)의 유일성에 의하여 $\varphi^\sharp(D(f))=(\varphi')^\sharp(D(f))$이다. 두 sheaf morphism이 base $\{D(f)\}_{f\in A}$ 위에서 일치하므로, $\varphi_\ast\mathcal{O}_X$의 identity axiom에 의하여 $\varphi^\sharp=(\varphi')^\sharp$이고 따라서 $\Psi(\Phi(\varphi,\varphi^\sharp))=(\varphi,\varphi^\sharp)$이다. 

마지막으로 이 전단사가 natural임을 확인하자. Locally ringed space들 사이의 morphism $\psi: X' \rightarrow X$가 주어지면, 합성 $(\varphi\circ\psi)^\sharp$을 $\Spec A$에서 계산한 것은 $\psi^\sharp(X)\circ\varphi^\sharp(\Spec A)$이므로

$$\Phi(\varphi\circ\psi)=\Gamma(\psi)\circ\Phi(\varphi)$$

이다. 또 ring homomorphism $\theta: A \rightarrow A'$가 주어지면, [명제 9](#prop9)의 construction에서 $f=1$로 두었을 때 $(\Spec\theta)^\sharp(\Spec A)=\theta$이므로 임의의 $\varphi: X \rightarrow \Spec A'$에 대하여

$$\Phi((\Spec\theta)\circ\varphi)=\Phi(\varphi)\circ\theta$$

이다. 즉 주어진 전단사는 $X$와 $A$ 모두에 대해 natural하며, 이로부터 주장의 natural isomorphism을 얻는다. 
:::

---
**참고문헌**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).

---

[^1]: 일반적으로 우리는 임의의 $X$ 위의 sheaf $\mathcal{F}$에 대해 $\mathcal{F}(X)$를 $\Gamma(X, \mathcal{F})$로 표기한다. 