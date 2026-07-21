---
title: "Perverse 층"
description: "t-구조의 개념을 도입하고 constructible 유도 범주 위의 middle perversity t-구조를 정의하여, Verdier 쌍대성에 대해 자기쌍대인 abelian 범주인 perverse 층과 IC 층, 분해정리를 다룬다."
excerpt: "t-structures, the perverse t-structure, perverse sheaves, IC sheaves, and the decomposition theorem"

categories: [Math / Sheaf Theory]
permalink: /ko/math/sheaf_theory/perverse_sheaves
sidebar: 
    nav: "sheaf_theory-ko"

date: 2026-07-01
last_modified_at: 2026-07-01
weight: 4

published: false

---

[§Verdier 쌍대성](/ko/math/sheaf_theory/verdier_duality)에서 우리는 임의의 사상에 대해 작동하는 Verdier 쌍대 functor $\mathbf{D}_X = R\mathcal{H}om(-, \omega_X)$를 도입하고, constructible complex 위에서 그것이 $\mathbf{D}_X^2 \cong \id$인 anti-equivalence임을 확인하였다. 그 글의 마지막에서 본 node $X = \{xy = 0\} \subseteq \mathbb{C}^2$의 dualizing complex 계산은 특이공간에서 일어나는 결정적인 현상을 드러냈다. ([§Verdier 쌍대성, ⁋예시 10](/ko/math/sheaf_theory/verdier_duality#ex10)) smooth variety에서는 $\omega_X \cong k_X[n]$이어서 상수 sheaf의 shift $k_X[n]$이 Verdier 쌍대성 아래 자기 자신으로 돌아오지만, singular point가 있으면 $\omega_X$가 더 이상 shift된 상수 sheaf가 아니므로 $\mathbf{D}_X(k_X) = \omega_X \not\cong k_X[n]$이고, 따라서 통상적 cohomology가 Poincaré 쌍대성을 잃는다.

이 글의 목표는 이 결함을 구조적으로 해소하는 것이다. 우리는 constructible 유도 범주 $D^b_c(X)$ 안에서, $\mathbf{D}_X$에 대해 자기쌍대이면서 abelian 범주를 이루는 충만한 부분범주를 찾고자 한다. 그러한 범주의 대상은 상수 sheaf의 단순한 shift가 아니라 singular point에 맞추어 "중간"으로 절단된 complex이며, 그 가운데 자기쌍대인 단순 대상이 바로 intersection cohomology를 계산하는 IC 층이다. 이 부분범주를 *perverse 층<sub>perverse sheaf</sub>*의 범주라 부른다. 그것을 정의하는 도구는 triangulated 범주 위의 새로운 종류의 절단 구조인 t-structure이며, perverse 층의 범주는 한 특정한 t-structure의 heart로 나타난다.

이 글 전체에서 $X$는 complex algebraic variety 또는 복소해석공간이고, 계수는 고정된 field $k$를 택한다. $\dim$은 항상 복소 차원을 가리킨다. 이는 [§Verdier 쌍대성](/ko/math/sheaf_theory/verdier_duality)이 실 위상 차원으로 shift를 적었던 것과 다른 규약인데, perverse 층의 middle perversity는 복소 차원으로 normalize할 때 Verdier 쌍대성과 군더더기 없이 맞아떨어지기 때문이다. 복소 $n$차원 smooth variety는 실 $2n$차원이므로 [§Verdier 쌍대성, ⁋정리 9](/ko/math/sheaf_theory/verdier_duality#thm9)의 $\omega_X \cong k_X[2n]$이 성립하고, 따라서 $\mathbf{D}_X(k_X[n]) \cong k_X[2n][-n] = k_X[n]$이 되어 복소 차원만큼 shift한 $k_X[n]$이 자기쌍대가 된다. 이 normalization이 아래 perverse t-structure의 핵심 규약이다.

## t-structure의 정의

Triangulated 범주는 그 자체로 abelian 범주가 아니다. ([\[호몰로지 대수학\] §유도카테고리, ⁋정의 11](/ko/math/homological_algebra/derived_categories#def11)) 유도 범주 $D(\mathcal{A})$에는 kernel과 cokernel이 없고, 대신 distinguished triangle이 short exact sequence의 역할을 대신한다. 그러나 $D(\mathcal{A})$에는 원래의 abelian 범주 $\mathcal{A}$가 차수 $0$에 집중된 complex로 다시 박혀 있으며, 임의의 complex에서 그 cohomology object $H^i \in \mathcal{A}$를 뽑아내는 functor가 있다. T-structure는 이 "어느 차수에 놓여 있는가"라는 정보와 "cohomology를 뽑아 abelian 범주로 떨어뜨리는" 조작을 임의의 triangulated 범주 위에서 공리화한 것이다.

::: 정의 1
Triangulated 범주 $\mathcal{T}$ 위의 *t-structure<sub>t-구조</sub>*는 충만한 부분범주들의 쌍 $(\mathcal{T}^{\leq 0}, \mathcal{T}^{\geq 0})$로서, $\mathcal{T}^{\leq n} := \mathcal{T}^{\leq 0}[-n]$, $\mathcal{T}^{\geq n} := \mathcal{T}^{\geq 0}[-n]$으로 적을 때 다음 세 조건을 만족하는 것이다.

1. (포함) $\mathcal{T}^{\leq 0} \subseteq \mathcal{T}^{\leq 1}$이고 $\mathcal{T}^{\geq 1} \subseteq \mathcal{T}^{\geq 0}$이다.
2. (직교성) $X \in \mathcal{T}^{\leq 0}$, $Y \in \mathcal{T}^{\geq 1}$이면 $\Hom_{\mathcal{T}}(X, Y) = 0$이다.
3. (절단 삼각형) 임의의 $X \in \mathcal{T}$에 대해 distinguished triangle
$$A \longrightarrow X \longrightarrow B \xrightarrow{+1}$$
이 존재하여 $A \in \mathcal{T}^{\leq 0}$, $B \in \mathcal{T}^{\geq 1}$이다.
:::

직관적으로 $\mathcal{T}^{\leq 0}$은 "차수 $0$ 이하에 놓인" 대상들, $\mathcal{T}^{\geq 0}$은 "차수 $0$ 이상에 놓인" 대상들의 모임이다. Shift $[-n]$이 complex를 $n$칸 뒤로 밀므로 ([\[호몰로지 대수학\] §유도카테고리, ⁋정의 4](/ko/math/homological_algebra/derived_categories#def4)), $\mathcal{T}^{\leq n} = \mathcal{T}^{\leq 0}[-n]$은 "차수 $n$ 이하"를 뜻하고 첫째 조건은 $\mathcal{T}^{\leq 0} \subseteq \mathcal{T}^{\leq 1} \subseteq \cdots$, $\cdots \subseteq \mathcal{T}^{\geq 1} \subseteq \mathcal{T}^{\geq 0}$이라는 단조성을 말한다. 둘째 조건은 낮은 차수의 대상에서 더 높은 차수의 대상으로 가는 사상이 없다는 것이며, 셋째 조건은 임의의 대상을 낮은 부분 $A$와 높은 부분 $B$로 쪼개는 삼각형의 존재를 보장한다. 이 삼각형은 사실 유일하며, 그로부터 절단 functor가 나온다.

::: 명제 2
$(\mathcal{T}^{\leq 0}, \mathcal{T}^{\geq 0})$이 t-structure이면 포함 functor $\mathcal{T}^{\leq n} \hookrightarrow \mathcal{T}$는 오른쪽 수반 $\tau_{\leq n}: \mathcal{T} \rightarrow \mathcal{T}^{\leq n}$을, 포함 functor $\mathcal{T}^{\geq n} \hookrightarrow \mathcal{T}$는 왼쪽 수반 $\tau_{\geq n}: \mathcal{T} \rightarrow \mathcal{T}^{\geq n}$을 가진다. 각 $X$에 대해 [정의 1](#def1)의 절단 삼각형은 유일하게 결정되며 $X$에 functorial하고, 표준적으로
$$\tau_{\leq 0} X \longrightarrow X \longrightarrow \tau_{\geq 1} X \xrightarrow{+1}$$
의 형태이다.
:::
::: 증명
$X \in \mathcal{T}$에 [정의 1](#def1)의 셋째 조건을 적용해 삼각형 $A \rightarrow X \rightarrow B \xrightarrow{+1}$, $A \in \mathcal{T}^{\leq 0}$, $B \in \mathcal{T}^{\geq 1}$을 택한다. 임의의 $A' \in \mathcal{T}^{\leq 0}$에 대해 이 삼각형에 $\Hom_{\mathcal{T}}(A', -)$을 적용하면 long exact sequence
$$\Hom(A', B[-1]) \rightarrow \Hom(A', A) \rightarrow \Hom(A', X) \rightarrow \Hom(A', B)$$
를 얻는다. $B \in \mathcal{T}^{\geq 1}$이고 $B[-1] \in \mathcal{T}^{\geq 2} \subseteq \mathcal{T}^{\geq 1}$이므로 직교성에 의해 양 끝 항이 $0$이고, 따라서
$$\Hom_{\mathcal{T}}(A', A) \xrightarrow{\ \sim\ } \Hom_{\mathcal{T}}(A', X)$$
이 모든 $A' \in \mathcal{T}^{\leq 0}$에 대해 성립한다. 이것이 바로 $A$가 포함 functor에 대한 $X$의 오른쪽 수반의 값임을 뜻하므로 $\tau_{\leq 0} X := A$로 둔다. 수반의 보편성에 의해 $A$는 유일한 동형을 제외하고 결정되고, 같은 보편성이 사상 $X \rightarrow X'$에 대한 $\tau_{\leq 0} X \rightarrow \tau_{\leq 0} X'$을 유일하게 주므로 functoriality가 따른다. 삼각형의 셋째 꼭짓점 $B$는 처음 두 사상의 cone으로 결정되므로 [\[호몰로지 대수학\] §유도카테고리, ⁋정의 11](/ko/math/homological_algebra/derived_categories#def11)의 (TR1)에 의해 $\tau_{\geq 1} X := B$ 역시 유일하게 결정되고, symmetric인 논증으로 $\tau_{\geq 1}$이 포함 functor의 왼쪽 수반이 된다. 일반 차수 $n$에 대한 결과는 shift $[-n]$을 적용하여 얻는다. 더 자세한 논증은 [BBD]의 Proposition 1.3.3을 따른다.
:::

절단 functor $\tau_{\leq n}$, $\tau_{\geq n}$이 갖추어졌으니, 이제 abelian 범주에서 cohomology를 뽑던 조작을 일반화할 수 있다. 두 절단을 합성하여 한 차수에 집중된 부분만을 추려내는 것이다.

::: 정의 3
t-structure $(\mathcal{T}^{\leq 0}, \mathcal{T}^{\geq 0})$의 *heart<sub>심장</sub>*는 충만한 부분범주
$$\mathcal{C} := \mathcal{T}^{\leq 0} \cap \mathcal{T}^{\geq 0}$$
이다. 또 *cohomology functor<sub>코호몰로지 함자</sub>* $H^0: \mathcal{T} \rightarrow \mathcal{C}$를
$$H^0 := \tau_{\leq 0} \circ \tau_{\geq 0} \cong \tau_{\geq 0} \circ \tau_{\leq 0}$$
으로 정의하고, $n \in \mathbb{Z}$에 대해 $H^n(X) := H^0(X[n])$으로 적는다.
:::

정의에서 두 절단의 합성이 순서에 무관함, 즉 $\tau_{\leq 0}\tau_{\geq 0} \cong \tau_{\geq 0}\tau_{\leq 0}$임은 절단 functor들의 형식적 성질에서 따라 나오며 ([BBD]의 Proposition 1.3.5), 그 공통의 값이 $\mathcal{C}$에 속한다. Heart $\mathcal{C}$가 단순한 부분범주가 아니라 abelian 범주를 이룬다는 것이 t-structure 이론의 핵심 정리이다.

::: 정리 4
t-structure의 heart $\mathcal{C}$는 abelian 범주이며, cohomology functor $H^0: \mathcal{T} \rightarrow \mathcal{C}$는 cohomological functor이다. 즉 distinguished triangle $X \rightarrow Y \rightarrow Z \xrightarrow{+1}$에 대해 long exact sequence
$$\cdots \rightarrow H^n(X) \rightarrow H^n(Y) \rightarrow H^n(Z) \rightarrow H^{n+1}(X) \rightarrow \cdots$$
이 $\mathcal{C}$ 안에서 성립한다.
:::
::: 증명
핵심은 $\mathcal{C}$ 안의 사상 $f: X \rightarrow Y$에 대한 kernel과 cokernel을 절단으로 구성하는 것이다. $\mathcal{T}$ 안에서 $f$를 distinguished triangle $X \xrightarrow{f} Y \rightarrow C \xrightarrow{+1}$로 채우면 [\[호몰로지 대수학\] §유도카테고리, ⁋정의 11](/ko/math/homological_algebra/derived_categories#def11)의 (TR1)에 의해 $X, Y \in \mathcal{C} \subseteq \mathcal{T}^{\geq 0}$이므로 $C \in \mathcal{T}^{\geq -1}$이고 마찬가지로 $C \in \mathcal{T}^{\leq 0}$이다. 그러면 $\mathcal{C}$ 안에서
$$\ker f := H^{-1}(C) = \tau_{\leq 0}(C[-1]), \qquad \operatorname{coker} f := H^0(C) = \tau_{\geq 0}(C)$$
으로 둘 수 있고, 직교성을 써서 이들이 kernel과 cokernel의 보편 성질을 만족함을 확인한다. Abelian 범주의 나머지 공리, 곧 모든 monomorphism이 자기 cokernel의 kernel이라는 등의 성질도 절단과 직교성의 결합으로 따라 나온다. Cohomology functor가 cohomological임은, $H^0$이 절단의 합성이고 절단이 distinguished triangle을 적절히 절단된 삼각형으로 보낸다는 사실에서 나온다. 완전한 증명은 [BBD]의 Théorème 1.3.6에 있다.
:::

t-structure가 추상적으로 무엇을 포착하는지는 가장 기본적인 예에서 분명해진다. 유도 범주 $D(\mathcal{A})$에는 원래의 abelian 범주 $\mathcal{A}$를 heart로 회복하는 t-structure가 있다.

::: 예시 5
abelian 범주 $\mathcal{A}$의 유도 범주 $D(\mathcal{A})$ 위에서
$$D^{\leq 0}(\mathcal{A}) := \{ C^\bullet : H^i(C^\bullet) = 0 \text{ for } i > 0 \}, \qquad D^{\geq 0}(\mathcal{A}) := \{ C^\bullet : H^i(C^\bullet) = 0 \text{ for } i < 0 \}$$
으로 두면 $(D^{\leq 0}, D^{\geq 0})$은 t-structure이며, 이를 *standard t-structure*라 부른다. 그 heart는 $\mathcal{A}$ (정확히는 $A \mapsto A[0]$로 박힌 충만한 부분범주)이고, cohomology functor $H^0$은 complex의 통상적 $0$차 cohomology object이다.
:::

세 공리를 점검한다. 포함 조건은 cohomology의 소멸 범위가 넓어지는 단조성이므로 자명하게 성립한다. 직교성은 $C^\bullet \in D^{\leq 0}$, $D^\bullet \in D^{\geq 1}$일 때 $\Hom_{D(\mathcal{A})}(C^\bullet, D^\bullet) = 0$임을 말하는데, $D^\bullet$을 차수 $\geq 1$에 놓인 $K$-injective resolution으로 바꾸고 $C^\bullet$의 cohomology가 차수 $\leq 0$에 갇혀 있음을 쓰면, chain map과 homotopy가 모두 차수 어긋남으로 소멸하여 derived 범주에서의 사상이 $0$이 된다. 절단 삼각형은 good truncation
$$\tau_{\leq 0} C^\bullet = (\cdots \rightarrow C^{-1} \rightarrow \ker d^0 \rightarrow 0), \qquad \tau_{\geq 1} C^\bullet = (0 \rightarrow \operatorname{im} d^0 \rightarrow C^1 \rightarrow \cdots)$$
이 주는 short exact sequence에서 나온다. Heart는 $H^i = 0$ ($i \neq 0$)인 complex들, 곧 한 차수에 집중된 complex들이고 이는 $\mathcal{A}$와 동치이다. 이 standard t-structure 위에서 [정리 4](#thm4)는 [\[호몰로지 대수학\] §유도카테고리, ⁋정의 11](/ko/math/homological_algebra/derived_categories#def11)의 삼각범주 공리가 주는 사실, 곧 $\mathcal{A}$가 abelian 범주이고 distinguished triangle이 cohomology long exact sequence를 준다는 것을 그대로 재생산한다. Perverse 층의 이론은 같은 유도 범주 위에 standard t-structure와 *다른* t-structure를 얹고, 그 heart로 새로운 abelian 범주를 얻는 데에 있다.

## Perverse (middle) t-structure

이제 무대를 constructible 유도 범주로 옮긴다. $X$ 위의 bounded constructible complex들이 이루는 충만한 삼각부분범주 $D^b_c(X)$는 [§Verdier 쌍대성, ⁋정의 6](/ko/math/sheaf_theory/verdier_duality#def6)에서 정의하였고, 그것이 여섯 functor와 Verdier 쌍대 functor $\mathbf{D}_X$ 모두에 대해 닫혀 있음을 그 글에서 확인하였다. Standard t-structure의 support는 cohomology sheaf $\mathcal{H}^i(\mathcal{F})$가 어느 차수에서 살아 있는지만 보지만, constructible 세계에서는 각 $\mathcal{H}^i$가 받침을 갖는 부분다양체의 *차원*이라는 추가 정보가 있다. Middle perversity t-structure는 차수와 차원을 한꺼번에 묶어, "cohomology가 높은 차수로 갈수록 받침이 그만큼 작아질 것"을 요구한다.

::: 정의 6
$\mathcal{F}^\bullet \in D^b_c(X)$의 cohomology sheaf의 받침을 $\operatorname{supp}\mathcal{H}^i(\mathcal{F}^\bullet) := \overline{\{x \in X : \mathcal{H}^i(\mathcal{F}^\bullet)_x \neq 0\}}$로 적는다. *perverse t-structure<sub>perverse t-구조</sub>* (middle perversity)를 다음 충만한 부분범주들로 정의한다.
$$
{}^{p}D^{\leq 0}(X) := \{ \mathcal{F}^\bullet : \dim \operatorname{supp}\mathcal{H}^i(\mathcal{F}^\bullet) \leq -i \text{ for all } i \},
$$
$$
{}^{p}D^{\geq 0}(X) := \{ \mathcal{F}^\bullet : \mathbf{D}_X \mathcal{F}^\bullet \in {}^{p}D^{\leq 0}(X) \}.
$$
첫째 조건을 *support 조건*, 둘째를 정의하는 $\dim \operatorname{supp}\mathcal{H}^i(\mathbf{D}_X \mathcal{F}^\bullet) \leq -i$를 *cosupport 조건*이라 부른다. 이 t-structure의 heart
$$\operatorname{Perv}(X) := {}^{p}D^{\leq 0}(X) \cap {}^{p}D^{\geq 0}(X)$$
의 대상을 $X$ 위의 *perverse 층<sub>perverse sheaf</sub>*이라 부른다.
:::

support 조건은 차수 $i$가 커질수록 받침의 차원이 $-i$ 이하로 줄어들기를 요구하며, 특히 $i > 0$이면 $\dim \operatorname{supp}\mathcal{H}^i \leq -i < 0$이므로 $\mathcal{H}^i = 0$이다. 따라서 ${}^{p}D^{\leq 0}$의 대상은 차수 $\leq 0$에 집중되고, 받침이 $d$차원인 곳에서는 차수 $-d$까지만 cohomology를 가질 수 있다. Cosupport 조건은 이 제약을 $\mathbf{D}_X$로 옮긴 것으로, biduality $\mathbf{D}_X^2 \cong \id$ ([§Verdier 쌍대성, ⁋정리 7](/ko/math/sheaf_theory/verdier_duality#thm7)) 덕분에 두 조건이 $\mathbf{D}_X$ 아래에서 정확히 맞교환된다. smooth 연결 $n$차원 variety $X$ 위의 rank 유한 local system $L$에 대해 $L[n]$을 보면, $\mathcal{H}^{-n}(L[n]) = L$의 받침이 $X$ 전체이므로 $\dim X = n \leq -(-n) = n$이 등호로 성립하고 다른 차수의 cohomology가 없어 support 조건을 만족하며, $\mathbf{D}_X(L[n]) \cong L^\vee[n]$ 역시 같은 이유로 support 조건을 만족하므로 $L[n] \in \operatorname{Perv}(X)$이다. 이것이 이름의 "middle"이 가리키는 normalization이다.

::: 정리 7
$({}^{p}D^{\leq 0}(X), {}^{p}D^{\geq 0}(X))$은 $D^b_c(X)$ 위의 bounded t-structure이다. 따라서 $\operatorname{Perv}(X)$은 abelian 범주이고, 그 위의 cohomology functor ${}^{p}\mathcal{H}^i: D^b_c(X) \rightarrow \operatorname{Perv}(X)$이 정의된다. 또한 Verdier 쌍대 functor는 $\mathbf{D}_X({}^{p}D^{\leq 0}) = {}^{p}D^{\geq 0}$, $\mathbf{D}_X({}^{p}D^{\geq 0}) = {}^{p}D^{\leq 0}$을 만족하므로 $\operatorname{Perv}(X)$을 자기 자신으로 보내며, $\operatorname{Perv}(X)$은 noetherian이자 artinian, 즉 모든 대상이 유한 길이를 가진다.
:::
::: 증명
t-structure 공리 가운데 포함 조건과 직교성은 차원의 단조성과 [§Verdier 쌍대성, ⁋따름정리 5](/ko/math/sheaf_theory/verdier_duality#cor5)의 쌍대성을 써서 직접 확인된다. 비자명한 부분은 절단 삼각형의 존재, 곧 임의의 $\mathcal{F}^\bullet \in D^b_c(X)$를 ${}^{p}\tau_{\leq 0}\mathcal{F}^\bullet \rightarrow \mathcal{F}^\bullet \rightarrow {}^{p}\tau_{\geq 1}\mathcal{F}^\bullet \xrightarrow{+1}$로 쪼개는 perverse 절단 functor의 구성이다. 이는 stratification에 대한 귀납으로 이루어지는데, 한 stratum을 closed embedding $i$와 open embedding $j$로 분해하고 ([§고유 받음과 여섯 함자, ⁋정리 10](/ko/math/sheaf_theory/six_functors#thm10)의 recollement) 열린 부분 위에서 standard 절단을 차원만큼 shift하여 적용한 뒤, $i_\ast, i^!, j_!, Rj_\ast$의 t-완전성을 이용해 닫힌 부분으로 이어 붙인다. Cosupport 조건이 $\mathbf{D}_X$로 정의되었으므로 $\mathbf{D}_X$가 두 부분범주를 맞교환함은 정의상 즉각적이고, biduality로 양방향이 성립한다. 유한 길이성은 constructible complex가 유한 stratification에 종속되고 각 stratum 위의 local system이 유한 rank라는 사실에서, 길이에 대한 귀납으로 얻어진다. 완전한 구성은 [BBD]의 §2.1, 특히 Théorème 2.1.1과 [KS]의 §10.2를 따른다.
:::

[정리 7](#thm7)이 보장하는 self-duality가 perverse 층 이론의 출발 동기를 정확히 실현한다. $\mathbf{D}_X$가 $\operatorname{Perv}(X)$을 보존하므로, perverse 층 가운데 $\mathbf{D}_X \mathcal{F} \cong \mathcal{F}$인 자기쌍대 대상을 논할 수 있고, 그러한 대상의 hypercohomology가 Poincaré 쌍대성을 만족하게 된다. 가장 단순한 경우를 점검하자.

::: 예시 8
한 점 $X = \{\ast\}$ 위에서는 $D^b_c(\{\ast\}) = D^b(\operatorname{Vec}^{fd}_k)$ (유한차원 $k$-벡터공간의 bounded 유도 범주)이고, $\dim\{\ast\} = 0$이므로 perverse t-structure는 standard t-structure와 일치한다. 따라서
$$\operatorname{Perv}(\{\ast\}) \cong \operatorname{Vec}^{fd}_k$$
이며, perverse 층은 한 차수 $0$에 놓인 유한차원 벡터공간이다. 한편 smooth 연결 $n$차원 variety $X$ 위에서는, [정의 6](#def6) 직후에 보았듯 local system의 shift $L[n]$이 perverse 층이며, $L$이 자기쌍대 ($L \cong L^\vee$)이면 $\mathbf{D}_X(L[n]) \cong L^\vee[n] \cong L[n]$이 자기쌍대 perverse 층이다.
:::

[예시 8](#ex8)의 smooth한 경우와 대조적으로, 특이공간에서는 상수 sheaf의 shift가 자기쌍대성을 잃는다.

::: 참고 9
[§Verdier 쌍대성, ⁋예시 10](/ko/math/sheaf_theory/verdier_duality#ex10)의 node $X = \{xy = 0\}$ (복소 $1$차원)에서 $k_X[1]$을 생각하면, $\mathbf{D}_X(k_X[1]) \cong \omega_X[-1]$인데 $\omega_X$가 원점에서 두 차수에 퍼진 잉여 stalk를 가지므로 $\mathbf{D}_X(k_X[1]) \not\cong k_X[1]$이다. 즉 smooth variety였다면 자기쌍대였을 $k_X[\dim]$이 singular point 때문에 자기쌍대성을 잃는다. 이 결함을 메우는 자기쌍대 perverse 층이 다음 절의 IC 층이며, node의 경우 그것은 두 분지 각각의 $k[1]$의 direct sum으로 분해되어 $k_X[1]$과는 원점 stalk가 다르다.
:::

## IC 층과 intermediate extension

[정리 7](#thm7)에 의해 $\operatorname{Perv}(X)$은 유한 길이의 abelian 범주이므로, Jordan–Hölder 의미에서 그 단순 대상이 모든 perverse 층의 구성 벽돌이 된다. 우리는 이 단순 대상을 명시적으로 구성한다. 그 도구는 열린 부분 위의 perverse 층을 전체로 "중간만큼" 연장하는 functor이다. 두 극단적 연장인 $j_!$과 $Rj_\ast$은 일반적으로 perverse 층을 perverse 층으로 보내지 않지만, 그 perverse cohomology 사이의 자연 사상의 상을 취하면 perverse 층이 되며 이것이 중간 연장이다.

::: 정의 10
Open embedding $j: U \hookrightarrow X$와 perverse 층 $\mathcal{F} \in \operatorname{Perv}(U)$에 대해, 표준 사상 $j_! \mathcal{F} \rightarrow Rj_\ast \mathcal{F}$에 perverse cohomology ${}^{p}\mathcal{H}^0$을 적용하여 얻는 $\operatorname{Perv}(X)$ 안의 사상의 상
$$j_{!\ast} \mathcal{F} := \operatorname{im}\big({}^{p}\mathcal{H}^0(j_! \mathcal{F}) \longrightarrow {}^{p}\mathcal{H}^0(Rj_\ast \mathcal{F})\big)$$
을 $\mathcal{F}$의 *intermediate extension<sub>중간 연장</sub>*이라 부른다. 나아가 irreducible 닫힌 부분다양체 $Z \subseteq X$ (복소 차원 $d$)와 그 smooth한 조밀 열린 부분 $U_Z \subseteq Z$ 위의 local system $L$에 대해, open embedding $j: U_Z \hookrightarrow Z$와 closed embedding $i_Z: Z \hookrightarrow X$를 두고
$$\operatorname{IC}_Z(L) := (i_Z)_\ast j_{!\ast}(L[d]) \in \operatorname{Perv}(X)$$
을 $(Z, L)$의 *intersection cohomology 층* 또는 *IC 층*이라 부른다.
:::

정의에서 $L[d]$는 smooth $d$차원 variety $U_Z$ 위의 perverse 층이고 ([예시 8](#ex8)), closed embedding에 대한 $(i_Z)_\ast$은 perverse 층을 perverse 층으로 보내는 t-완전 functor이므로 $\operatorname{IC}_Z(L)$은 $X$ 위의 perverse 층이다. 받침은 $Z$이며, $Z$의 smooth한 부분으로 제한하면 $L[d]$로 돌아온다. $X$ 자신이 irreducible이고 $L$이 자명한 rank $1$ local system이면 $\operatorname{IC}_X := \operatorname{IC}_X(k_{U})$로 적고, 이것이 $X$의 intersection cohomology를 계산하는 complex이다. smooth한 $X$에서는 $U = X$, $j = \id$이므로 $\operatorname{IC}_X = k_X[\dim X]$이 되어 [예시 8](#ex8)의 상수 sheaf shift로 환원된다.

Intermediate extension의 결정적 성질은 그것이 열린 부분 위의 자료를 닫힌 부분으로 "과잉도 부족도 없이" 연장한다는 것이며, 이를 부분대상과 quotient object의 받침으로 특징짓는다.

::: 명제 11
Open embedding $j: U \hookrightarrow X$, 닫힌 보충 $i: Z = X \setminus U \hookrightarrow X$와 $\mathcal{F} \in \operatorname{Perv}(U)$에 대해 다음이 성립한다.

1. $j_{!\ast}\mathcal{F}$는 $j^{-1}(j_{!\ast}\mathcal{F}) \cong \mathcal{F}$인 $\operatorname{Perv}(X)$의 대상 가운데, $Z$에 받침을 가진 $0$ 아닌 부분대상도 quotient object도 가지지 않는 유일한 것이다.
2. Verdier 쌍대성과 교환한다. 즉 $\mathbf{D}_X(j_{!\ast}\mathcal{F}) \cong j_{!\ast}(\mathbf{D}_U \mathcal{F})$이다. 특히 $L$이 자기쌍대 local system이면 $\operatorname{IC}_Z(L)$은 자기쌍대 perverse 층이다.
:::
::: 증명
(1) $j_{!\ast}\mathcal{F}$를 상으로 정의했으므로 $j_!$ 쪽에서 오는 표준 사상은 전사, $Rj_\ast$ 쪽으로 가는 사상은 단사이다. 만약 $j_{!\ast}\mathcal{F}$가 $Z$에 받침을 가진 $0$ 아닌 부분대상 $\mathcal{S}$를 가진다면, $\mathcal{S} = i_\ast i^{-1}\mathcal{S}$이고 이는 ${}^{p}\mathcal{H}^0(Rj_\ast\mathcal{F})$로 가는 단사를 통해 살아남아야 하는데, [§고유 받음과 여섯 함자, ⁋정리 10](/ko/math/sheaf_theory/six_functors#thm10)이 주는 recollement의 t-완전성 분석에서 $Rj_\ast$로의 단사가 $Z$-받침 부분대상을 죽이므로 모순이다. Quotient object에 대해서는 $j_!$로부터의 전사와 같은 논증을 쌍대로 적용한다. 유일성은 두 조건 (부분대상·quotient object의 부재)을 동시에 만족하는 연장이 표준 사상의 상과 일치할 수밖에 없음을 보여 얻는다.

(2) Verdier 쌍대성은 [§Verdier 쌍대성, ⁋명제 8](/ko/math/sheaf_theory/verdier_duality#prop8)에 의해 $j_!$과 $Rj_\ast$을 맞교환하고 $j^{-1}$을 보존하므로, 사상 $j_!\mathcal{F} \rightarrow Rj_\ast\mathcal{F}$에 $\mathbf{D}_X$를 적용하면 $\mathbf{D}_U\mathcal{F}$에 대한 같은 종류의 사상 $j_!(\mathbf{D}_U\mathcal{F}) \rightarrow Rj_\ast(\mathbf{D}_U\mathcal{F})$이 (방향을 보존한 채) 나온다. $\mathbf{D}_X$가 anti-equivalence이므로 상의 $\mathbf{D}_X$는 $\mathbf{D}_X$의 상이고, 따라서 $\mathbf{D}_X(j_{!\ast}\mathcal{F}) \cong j_{!\ast}(\mathbf{D}_U\mathcal{F})$이다. smooth $d$차원 $U_Z$ 위에서 $\mathbf{D}_{U_Z}(L[d]) \cong L^\vee[d]$이므로, $L \cong L^\vee$이면 $\operatorname{IC}_Z(L)$이 자기쌍대이다. 자세한 논증은 [BBD]의 §2.1.9–2.1.11을 따른다.
:::

[명제 11](#prop11)의 첫째 성질이 단순성을 함의한다. $Z$에 받침을 가진 부분대상도 quotient object도 없는 perverse 층은, local system $L$이 irreducible이면 더 쪼갤 수 없다. 이로부터 $\operatorname{Perv}(X)$의 단순 대상이 완전히 분류된다.

::: 정리 12
$\operatorname{Perv}(X)$의 단순 대상은 정확히, irreducible 닫힌 부분다양체 $Z \subseteq X$와 그 smooth한 조밀 열린 부분 위의 irreducible local system $L$의 쌍 $(Z, L)$에 대한 IC 층 $\operatorname{IC}_Z(L)$들이다. 서로 다른 쌍 $(Z, L)$ (단, $L$은 동형을 제외)은 서로 isomorphic하지 않은 단순 대상을 주며, 이로써 단순 대상이 $(Z, L)$로 완전히 분류된다.
:::
::: 증명
$L$이 irreducible이면 $\operatorname{IC}_Z(L)$이 단순함을 보인다. $0 \neq \mathcal{G} \subsetneq \operatorname{IC}_Z(L)$인 부분대상이 있다면, 받침이 $Z$이므로 smooth한 열린 부분 $U_Z$로 제한한 $j^{-1}\mathcal{G}$는 $L[d]$의 부분대상이고 $L$의 irreducibility에 의해 $0$ 또는 $L[d]$이다. $j^{-1}\mathcal{G} = 0$이면 $\mathcal{G}$가 $Z$의 더 작은 닫힌 부분에 받침을 가지므로 [명제 11](#prop11)의 첫째 성질에 어긋나고, $j^{-1}\mathcal{G} = L[d]$이면 quotient $\operatorname{IC}_Z(L)/\mathcal{G}$가 그 작은 닫힌 부분에 받침을 가져 다시 어긋난다. 따라서 $\operatorname{IC}_Z(L)$은 단순하다. 역으로 임의의 단순 perverse 층 $\mathcal{S}$를 잡아 그 받침 $Z = \operatorname{supp}\mathcal{S}$ (irreducible임을 보일 수 있다)와 smooth한 조밀 열린 부분 $U_Z$ 위로의 제한을 보면, 그 제한이 어떤 irreducible local system $L$의 shift $L[d]$이고 $\mathcal{S} = \operatorname{IC}_Z(L)$임이 [명제 11](#prop11)의 유일성에서 따라 나온다. 완전한 논증은 [BBD]의 Théorème 4.3.1을 따른다.
:::

[정리 12](#thm12)와 [정리 7](#thm7)의 유한 길이성을 결합하면, $X$ 위의 모든 perverse 층은 IC 층들의 유한 번 반복된 extension으로 얻어진다. 즉 IC 층이 perverse 층의 범주의 단순 대상 전체를 이룬다. 이 사실이 perverse 층을 특이공간의 cohomology 이론의 자연스러운 계수로 만든다. $\operatorname{IC}_X$의 hypercohomology $H^k(X, \operatorname{IC}_X)$이 곧 $X$의 intersection cohomology이며, [명제 11](#prop11)의 자기쌍대성에 의해 ($k_{U}$가 자기쌍대이므로) [§Verdier 쌍대성, ⁋따름정리 5](/ko/math/sheaf_theory/verdier_duality#cor5)를 통해 특이 $X$에서도 Poincaré 쌍대성을 회복한다.

## 분해정리

IC 층의 위력이 가장 극적으로 드러나는 곳이 proper 사상에 대한 받음의 거동이다. Smooth projective variety 사이의 proper 사상에서 받음 $Rf_\ast$이 IC 층을 어떻게 분해하는지를 기술하는 것이 Beilinson–Bernstein–Deligne–Gabber의 분해정리이며, 이는 Deligne의 projective variety에 대한 spectral sequence 퇴화 정리와 hard Lefschetz 정리를 perverse 층의 언어로 통합하고 특이공간으로까지 확장한 결과이다.

::: 정리 13 (분해정리)
$f: X \rightarrow Y$를 complex algebraic variety 사이의 proper 사상이라 하자. 그럼 $D^b_c(Y)$ 안에서 자연스러운 direct sum 분해
$$Rf_\ast \operatorname{IC}_X \cong \bigoplus_{i \in \mathbb{Z}} {}^{p}\mathcal{H}^i(Rf_\ast \operatorname{IC}_X)[-i]$$
이 성립하며, 각 perverse cohomology ${}^{p}\mathcal{H}^i(Rf_\ast \operatorname{IC}_X)$은 반단순 perverse 층, 즉 유한히 많은 IC 층 $\operatorname{IC}_Z(L)$ (단, $Z \subseteq Y$ irreducible 닫힌, $L$ 반단순 local system)의 direct sum이다. 더 일반적으로, $\operatorname{IC}_X$ 자리에 반단순 local system을 계수로 가지는 IC 층 $\operatorname{IC}_X(L_X)$을 넣어도 같은 결론이 성립한다.
:::
::: 증명
원래의 증명 ([BBD])은 정리를 표수 $p$의 유한체 위로 환원한다. 그곳에서 $\operatorname{IC}_X$은 Frobenius에 대해 *순수*하고 (weight가 한 값에 집중), Gabber의 순수성 정리에 의해 $Rf_\ast$이 순수성을 보존하므로, 순수 complex가 자신의 perverse cohomology의 shift들의 direct sum으로 갈라진다는 weight 논증이 작동한다. 그 뒤 $\ell$-진 sheaf의 결과를 비교 정리로 복소해석 위로 옮긴다. 이후 de Cataldo–Migliorini는 같은 정리에 순수 Hodge 이론과 relative hard Lefschetz를 결합한 직접적인 증명을 주었고 ([dCM]), Saito의 mixed Hodge module 이론은 또 다른 경로를 제공한다. 어느 증명에서나 핵심은 $\operatorname{IC}_X$의 *순수성*과 proper 받음이 그것을 보존한다는 사실, 그리고 relative hard Lefschetz가 주는 Lefschetz 분해이다. 분량과 사용하는 기계가 이 글의 범위를 넘으므로 [BBD]의 Théorème 6.2.5와 [dCM]의 주 정리를 참조한다.
:::

분해정리는 통상적 sheaf 이론에서는 기대할 수 없는 강력한 강직성을 말한다. 일반적으로 $Rf_\ast$은 perverse cohomology의 shift들로 direct sum 분해되지 않으며 비자명한 extension으로 엮여 있다. 분해정리는 입력이 순수 대상 (IC 층)이고 사상이 proper일 때 이 extension이 모두 갈라져, 받음이 단순 perverse 층들의 shift된 direct sum으로 완전히 분해됨을 보장한다. 이 분해는 받침에 따라 항을 모으면 받침 부분다양체 위의 intersection cohomology 항들의 합으로 정리되며, 특이 받침에 놓인 항들이 사상 $f$의 특이 fiber가 만드는 cohomology를 정확히 포착한다. 이 분해가 cohomological Hall 대수, flop 공식, Springer 이론 등 여러 기하학적 논증의 토대가 된다.

## 근방·소멸 cycle과 disk 위의 perverse 층

Perverse 층의 범주를 구체적으로 손에 쥐는 가장 효과적인 방법은 그것을 선형대수적 자료로 번역하는 것이다. 가장 단순하지만 비자명한 경우, 곧 disk 위에서 한 점을 따라 stratify한 경우에 이 번역이 완전히 이루어지며, 그 번역의 두 축이 근방 cycle과 소멸 cycle functor이다. 이 functor들은 한 regular function $f$의 특이 fiber 근처에서 perverse 층이 어떻게 변하는지를 측정한다.

::: 정의 14
Regular function $f: X \rightarrow \mathbb{C}$와 특이 fiber $X_0 = f^{-1}(0)$, closed embedding $i: X_0 \hookrightarrow X$를 생각하자. 표준적으로 정의되는 functor
$$\psi_f, \phi_f : D^b_c(X) \rightarrow D^b_c(X_0)$$
을 각각 *근방 cycle<sub>nearby cycle</sub>* functor와 *소멸 cycle<sub>vanishing cycle</sub>* functor라 부른다 ($\psi_f \mathcal{F}$의 stalk는 $x \in X_0$에서의 Milnor fiber cohomology를 계산한다). 그 perverse normalization을
$$\Psi_f := \psi_f[-1], \qquad \Phi_f := \phi_f[-1]$$
로 둔다.
:::

근방 cycle은 $f$의 일반 fiber를 특이 fiber 쪽으로 극한을 취해 얻는 complex이고, 소멸 cycle은 일반 fiber와 특이 fiber의 차이를 재는 complex이다. 두 functor는 distinguished triangle $i^{-1}\mathcal{F} \rightarrow \psi_f\mathcal{F} \rightarrow \phi_f\mathcal{F} \xrightarrow{+1}$로 엮이며, 이로부터 표준 사상 $\operatorname{can}: \Psi_f\mathcal{F} \rightarrow \Phi_f\mathcal{F}$과 그 짝인 *variation* 사상 $\operatorname{var}: \Phi_f\mathcal{F} \rightarrow \Psi_f\mathcal{F}$이 나온다. 일반 fiber의 monodromy automorphism $T$는 $\Psi_f\mathcal{F}$ 위에 작용하며 그 단멱부분이 $T - \id = \operatorname{var} \circ \operatorname{can}$으로 인수분해된다. Perverse normalization $\Psi_f, \Phi_f$이 결정적인데, 이들은 perverse t-완전, 곧 $\operatorname{Perv}(X) \rightarrow \operatorname{Perv}(X_0)$을 정의하며 ([KS], [Dim]), Verdier 쌍대성과도 교환한다. 이제 가장 단순한 경우인 disk에서 이 자료가 perverse 층을 완전히 결정함을 본다.

::: 정리 15
$\Delta \subseteq \mathbb{C}$를 원점을 포함한 disk라 하고, 좌표함수 $f(z) = z$에 대한 stratification $\{0\} \sqcup \Delta^\ast$ ($\Delta^\ast = \Delta \setminus \{0\}$)을 생각하자. 이 stratification에 종속된 perverse 층의 범주 $\operatorname{Perv}(\Delta, 0)$은, 다음 자료의 범주 $\mathcal{Q}$와 동치이다.

1. 유한차원 $k$-벡터공간의 쌍 $\Psi, \Phi$,
2. 선형사상 $\operatorname{can}: \Psi \rightarrow \Phi$과 $\operatorname{var}: \Phi \rightarrow \Psi$,

단, $T_\Psi := \id_\Psi + \operatorname{var} \circ \operatorname{can}$이 가역 (동치로 $\id_\Phi + \operatorname{can} \circ \operatorname{var}$이 가역)이라는 조건을 만족한다. 이 동치 아래 $\Psi = \Psi_f$ (근방 cycle, 곧 $\Delta^\ast$ 위 local system의 stalk)이고 $\Phi = \Phi_f$ (소멸 cycle)이며, $T_\Psi$은 monodromy action이다.
:::
::: 증명
Beilinson의 gluing 구성이 핵심이다. Open embedding $j: \Delta^\ast \hookrightarrow \Delta$과 closed embedding $i: \{0\} \hookrightarrow \Delta$에 대해 [§고유 받음과 여섯 함자, ⁋정리 10](/ko/math/sheaf_theory/six_functors#thm10)이 주는 recollement는, $\Delta^\ast$ 위의 perverse 층 (rank 유한 local system의 shift)과 $\{0\}$ 위의 perverse 층 (벡터공간), 그리고 둘을 잇는 사상 자료로부터 $\Delta$ 위의 perverse 층을 복원한다. $\Delta^\ast$ 위의 perverse 층은 그 monodromy 표현, 곧 $T_\Psi$이 작용하는 벡터공간 $\Psi$로 주어지고, 잇는 자료가 정확히 소멸 cycle 공간 $\Phi$과 $\operatorname{can}, \operatorname{var}$이다. Perverse 조건이 정확히 $T_\Psi$의 가역성 (monodromy가 automorphism이라는 것)으로 번역되며, 이는 $\Psi_f$이 generic stalk로서 잘 정의되기 위한 조건이다. 자세한 구성은 [Dim]의 §4.2와 [Ach]의 제4장을 따른다. 한편 부호 규약은 문헌마다 달라 $T_\Psi = \id - \operatorname{var}\circ\operatorname{can}$로 적기도 한다.
:::

[정리 15](#thm15)는 disk 위의 perverse 층 이론을 완전히 선형대수로 환원한다. 동치 아래 단순 대상과 표준 functor가 어떤 자료에 대응하는지를 구체적으로 계산해 보면 intermediate extension의 기제가 투명해진다.

::: 예시 16
$\Delta^\ast$ 위의 rank $r$ local system $L$의 monodromy를 $T: V \rightarrow V$ ($V = k^r$)이라 하자. $\Delta^\ast$가 smooth한 복소 $1$차원이므로 $L[1]$이 그 위의 perverse 층이다. [정리 15](#thm15)의 동치 아래 세 가지 표준 연장이 다음 자료에 대응한다.

1. $j_!(L[1]) \ \leftrightarrow\ (\Psi, \Phi, \operatorname{can}, \operatorname{var}) = (V, V, \id_V, T - \id)$,
2. $Rj_\ast(L[1]) \ \leftrightarrow\ (V, V, T - \id, \id_V)$,
3. $j_{!\ast}(L[1]) = \operatorname{IC}_\Delta(L) \ \leftrightarrow\ (V, \operatorname{im}(T - \id), T - \id, \hookrightarrow)$.
:::

세 자료 모두 $T_\Psi = \id + \operatorname{var}\circ\operatorname{can} = T$이 되어 [정리 15](#thm15)의 가역성 조건을 만족함을 즉시 확인할 수 있다 (monodromy $T$는 자동으로 automorphism이다). 표준 사상 $j_!(L[1]) \rightarrow Rj_\ast(L[1])$은 자료의 사상 $(\id_V, T - \id): (V, V, \id, T-\id) \rightarrow (V, V, T-\id, \id)$으로 나타나고 ($\Psi$ 위에서는 항등, $\Phi$ 위에서는 $T - \id$), 그 상이 바로 셋째 자료
$$\big(V,\ \operatorname{im}(T - \id),\ \operatorname{can} = (T - \id)\ \text{(전사)},\ \operatorname{var} = \text{포함}\big)$$
으로, 곧 $\operatorname{can}$이 전사이고 $\operatorname{var}$이 단사인 intermediate extension이다. 이는 [명제 11](#prop11)이 추상적으로 기술한 "$Z = \{0\}$에 받침을 가진 부분대상·quotient object의 부재"를 선형대수로 본 것인데, $\{0\}$에 받침을 가진 자료는 $\Psi = 0$인 것 ($\Phi$만 있는 skyscraper)이고, $\operatorname{can}$ 전사성이 그러한 quotient object를, $\operatorname{var}$ 단사성이 그러한 부분대상을 배제한다. 실제로 stalk와 costalk는 $i^{-1}M$이 complex $[\Psi \xrightarrow{\operatorname{can}} \Phi]$로, $i^! M$이 $[\Phi \xrightarrow{\operatorname{var}} \Psi]$로 계산되므로, $\operatorname{can}$이 isomorphic하면 $i^{-1} = 0$ (extension by zero, 곧 $j_!$)이고 $\operatorname{var}$이 isomorphic하면 $i^! = 0$ (곧 $Rj_\ast$)임이 위 자료와 일관된다.

monodromy가 자명한 특수한 경우 $T = \id$ (상수 sheaf $k_{\Delta^\ast}$)에서는 $T - \id = 0$이므로 $\operatorname{im}(T - \id) = 0$이고, 따라서 $\operatorname{IC}_\Delta(k) \leftrightarrow (V, 0, 0, 0)$, 곧 소멸 cycle이 없는 자료가 되어 $j_{!\ast}(k_{\Delta^\ast}[1]) = k_\Delta[1]$이 [예시 8](#ex8)의 smooth한 경우로 환원된다. 반면 $j_!$과 $Rj_\ast$은 이때 $\Phi = V \neq 0$인 자료를 주어, 원점에서 $V$만큼의 잉여를 가진 채 perverse 층으로 남는다. 이 잉여가 [참고 9](#rmk9)에서 본 특이공간의 잉여 stalk와 같은 종류의 현상이며, intermediate extension이 그것을 정확히 깎아 내어 자기쌍대 대상을 만든다.

---

**참고문헌**

**[BBD]** A. Beilinson, J. Bernstein, P. Deligne, *Faisceaux pervers*, Astérisque **100**, Société Mathématique de France, 1982.

**[KS]** M. Kashiwara, P. Schapira, *Sheaves on manifolds*, Springer, 1990.

**[dCM]** M. A. de Cataldo, L. Migliorini, *The decomposition theorem, perverse sheaves and the topology of algebraic maps*, Bulletin of the American Mathematical Society **46** (2009).

**[Ach]** P. Achar, *Perverse sheaves and applications to representation theory*, American Mathematical Society, 2021.

**[Dim]** A. Dimca, *Sheaves in topology*, Springer, 2004.
