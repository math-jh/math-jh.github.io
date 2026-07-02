---
title: "Verdier 쌍대성"
description: "Dualizing complex와 Verdier 쌍대 함자를 도입하고, Rf_!와 f^!의 수반에서 나오는 Verdier 쌍대성 정리를 진술하여 다양체의 Poincaré 쌍대성을 특수한 경우로 회복한다."
excerpt: "The dualizing complex, the Verdier dual D_X, and Poincaré duality as a special case"

categories: [Math / Sheaf Theory]
permalink: /ko/math/sheaf_theory/verdier_duality
sidebar: 
    nav: "sheaf_theory-ko"

date: 2026-07-01
last_modified_at: 2026-07-01
weight: 3

published: false

---

[§고유 받음과 여섯 함자](/ko/math/sheaf_theory/six_functors)에서 우리는 콤팩트 받침을 따르는 고유 받음 $$Rf_!$$과 그 오른쪽 수반인 예외 역상 $$f^!$$을 도입하여, $$Rf_\ast$$, $$Lf^\ast$$, $$\otimes^L$$, $$R\mathcal{H}om$$과 함께 여섯 함자 형식을 완성하였다. 그 글의 도입부에서 예고하였듯이, 이 형식을 세운 가장 큰 동기는 비콤팩트 공간과 특이점을 가진 공간에까지 Poincaré 쌍대성을 확장하는 데 있다. 이 글에서 우리는 그 확장을 완성하는 정리, 곧 *Verdier 쌍대성<sub>Verdier duality</sub>*을 진술하고 증명한다.

고전적인 Poincaré 쌍대성은 방향지어진 닫힌 $$n$$차원 다양체 $$M$$에 대해 $$H^p(M) \cong H_{n-p}(M)$$이라는 cohomology와 homology 사이의 동형으로 나타나며, 그 경계를 가진 형태인 Poincaré–Lefschetz 쌍대성은 콤팩트 받침을 허용하여 비콤팩트 다양체로 일부 확장된다. 그러나 이 고전적 진술은 두 방향에서 한계를 가진다. 첫째, 그것은 상수 계수 또는 국소계 계수에 대해서만 진술되며 임의의 sheaf complex의 cohomology를 다루지 못한다. 둘째, 그것은 다양체, 즉 모든 점이 $$\mathbb{R}^n$$과 국소적으로 위상동형인 공간에 대해서만 성립하며, 특이점을 가진 공간에서는 그대로 무너진다. Verdier 쌍대성은 이 두 한계를 한꺼번에 해소한다. 그 핵심은 다양체의 fundamental class가 떠맡던 역할을 한 점으로의 사상 $$a_X: X \to \{\ast\}$$에 대한 $$f^!$$이 대신하도록 만드는 것이다. $$a_X^!$$이 상수 sheaf에 주는 값을 *dualizing complex*라 부르고, 이것을 축으로 한 내부 Hom이 쌍대성을 매개한다.

이 글 전체에서 공간과 사상에 대한 가정은 [§고유 받음과 여섯 함자](/ko/math/sheaf_theory/six_functors)와 같다. 즉 위상공간은 locally compact Hausdorff이고 유한한 cohomological dimension을 가지며, 사상은 separated인 연속함수로 한정한다. 계수로는, 별도의 언급이 없으면 고정된 field $$k$$를 택하여 $$\mathcal{O}_X = k_X$$인 sheaf of $$k$$-vector space를 다룬다. 이는 앞 글이 $$\mathbb{Z}$$ 계수로 진술한 것과 다른 선택인데, field 위에서는 dual $$(-)^\vee = R\mathcal{H}om(-, k)$$이 higher Ext 항을 만들지 않아 쌍대성이 cohomology 차원에서 군더더기 없이 진술되기 때문이다. $$\mathbb{Z}$$ 계수에서의 보정은 적절한 곳에서 언급한다.

## Dualizing complex

비콤팩트하거나 특이한 공간에서 Poincaré 쌍대성을 끌어내려면, 다양체에서 fundamental class $$[M] \in H_n(M)$$이 cap product를 통해 수행하던 역할을 대체할 대상이 필요하다. 다양체의 경우 [§고유 받음과 여섯 함자, ⁋정리 7](/ko/math/sheaf_theory/six_functors#thm7)이 알려 주듯 $$a_X^! k \cong k_X[n]$$이며, 차수 이동 $$[n]$$이 바로 fundamental class의 차원 정보를 담는다. 일반적인 공간에서는 $$a_X^! k$$이 더 이상 shift된 상수 sheaf가 아니지만, 그것이 쌍대성을 매개하는 객체로서의 역할은 그대로 유지한다. 우리는 이 객체를 다음과 같이 명명한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 위상공간 $$X$$의 구조 사상 $$a_X: X \to \{\ast\}$$에 대해, $$\{\ast\}$$ 위의 계수 $$k$$의 예외 역상
$$\omega_X := a_X^! k$$
을 $$X$$의 *dualizing complex<sub>쌍대화 복합체</sub>*라 부른다. 여기서 $$a_X^!$$은 [§고유 받음과 여섯 함자, ⁋정의 6](/ko/math/sheaf_theory/six_functors#def6)에서 정의한 $$R(a_X)_!$$의 오른쪽 수반이다.

</div>

$$\omega_X$$는 일반적으로 한 차수에 집중되지 않는 $$D(\Sh(X))$$의 대상이며, 그 cohomology sheaf $$\mathcal{H}^{-i}(\omega_X)$$의 stalk는 $$X$$의 국소적인 Borel–Moore homology를 계산한다. 이 해석은 [예시 10](#ex10)에서 구체적으로 확인한다. 한편 $$X$$가 방향지어진 $$n$$차원 위상다양체이면 [§고유 받음과 여섯 함자, ⁋정리 7](/ko/math/sheaf_theory/six_functors#thm7)을 $$Y = \{\ast\}$$에 적용하여 $$\omega_X \cong k_X[n]$$을 얻는데, 이 특수한 경우가 곧 Poincaré 쌍대성의 sheaf 차원 표현이며 [정리 9](#thm9)에서 다룬다.

dualizing complex를 축으로 삼아 sheaf complex 하나하나에 그 "쌍대"를 대응시키는 함자를 정의한다. 이는 [§층의 유도 범주와 유도 함자, ⁋정의 7](/ko/math/sheaf_theory/derived_category_of_sheaves#def7)의 derived sheaf-Hom $$R\mathcal{H}om$$의 둘째 변수에 $$\omega_X$$를 고정한 것이다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> $$X$$ 위의 *Verdier 쌍대 함자<sub>Verdier dual functor</sub>* $$\mathbf{D}_X: D(\Sh(X))^{\op} \to D(\Sh(X))$$를
$$\mathbf{D}_X(\mathcal{F}^\bullet) := R\mathcal{H}om(\mathcal{F}^\bullet, \omega_X)$$
로 정의한다. $$\mathbf{D}_X(\mathcal{F}^\bullet)$$을 $$\mathcal{F}^\bullet$$의 *Verdier dual*이라 부른다.

</div>

정의에서 $$\mathcal{F}^\bullet = k_X$$로 두면 $$\mathbf{D}_X(k_X) = R\mathcal{H}om(k_X, \omega_X) \cong \omega_X$$이므로, 상수 sheaf의 Verdier dual이 dualizing complex 자신이다. 또 점 $$\{\ast\}$$ 위에서는 $$a_{\{\ast\}} = \id$$이므로 $$\omega_{\{\ast\}} = k$$이고, 따라서 점 위에서 $$\mathbf{D}_{\{\ast\}}(\mathcal{F}^\bullet) = R\Hom_k(\mathcal{F}^\bullet, k) = (\mathcal{F}^\bullet)^\vee$$이 통상적인 $$k$$-vector space complex의 dual로 환원된다. 이것이 $$\mathbf{D}_X$$를 "쌍대"라 부르는 근거이며, 아래에서 이 점별 dual이 콤팩트 받침 cohomology를 통해 대역적 cohomology와 짝지어짐을 본다.

쌍대 함자가 잘 행동하기 위해 먼저 확인할 형식적 성질은, dualizing complex가 열린 부분공간으로의 제한과 호환된다는 사실이다. 이는 $$\omega_X$$가 본질적으로 국소적인 객체임을 말하며, [예시 10](#ex10)의 stalk 계산을 정당화한다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> 열린 매장 $$j: U \hookrightarrow X$$에 대해 $$j^{-1}\omega_X \cong \omega_U$$이 성립한다. 즉 dualizing complex의 열린집합으로의 제한은 그 열린집합의 dualizing complex이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$a_U = a_X \circ j$$이므로 [§고유 받음과 여섯 함자, ⁋명제 5](/ko/math/sheaf_theory/six_functors#prop5)의 합성 동형의 수반 형태에 의해 $$\omega_U = a_U^! k = (a_X j)^! k \cong j^! a_X^! k = j^! \omega_X$$이다. 따라서 열린 매장 $$j$$에 대해 $$j^! \cong j^{-1}$$임을 보이면 된다. 열린 매장은 fiber가 $$0$$차원이고 국소적으로 항등 사상이므로 topological submersion of relative dimension $$0$$이며, 그 fiber는 표준적으로 방향지어진 한 점이다. 따라서 [§고유 받음과 여섯 함자, ⁋정리 7](/ko/math/sheaf_theory/six_functors#thm7)에서 $$d = 0$$, $$\operatorname{or}_{U/X} \cong k_U$$인 경우에 해당하여 $$j^! \mathcal{G}^\bullet \cong j^{-1}\mathcal{G}^\bullet[0] = j^{-1}\mathcal{G}^\bullet$$을 얻는다. 이를 $$\mathcal{G}^\bullet = \omega_X$$에 적용하면 $$j^{-1}\omega_X \cong \omega_U$$이다.

</details>

같은 논증은 닫힌 매장에는 적용되지 않는다. 닫힌 매장 $$i: Z \hookrightarrow X$$에 대해 $$i^! \omega_X \cong \omega_Z$$은 여전히 성립하지만 ($$a_Z = a_X i$$이므로), 통상적 제한 $$i^{-1}\omega_X$$는 일반적으로 $$\omega_Z$$과 다르며 바로 이 차이가 특이점에서의 비자명한 현상을 만든다. 이 점은 [예시 10](#ex10)에서 분명해진다.

## Verdier 쌍대성 정리

이제 이 글의 중심 정리를 진술한다. Verdier 쌍대성은 [§고유 받음과 여섯 함자, ⁋정의 6](/ko/math/sheaf_theory/six_functors#def6)의 $$(Rf_!, f^!)$$ 수반을 내부 Hom의 차원으로 끌어올린 것으로, 앞 글에서 확보한 모든 형식, 즉 두 adjunction과 projection formula가 한 줄의 동형으로 결집하는 지점이다. 진술은 두 층위로 주어진다. 먼저 $$Y$$ 위의 sheaf complex로서의 동형을 주는 국소적 형태이고, 거기에 전역 단면을 취해 얻는 대역적 형태이다.

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4 (Verdier 쌍대성)**</ins> Compactifiable map $$f: X \to Y$$와 $$\mathcal{F}^\bullet \in D(\Sh(X))$$, $$\mathcal{G}^\bullet \in D(\Sh(Y))$$에 대해 $$Y$$ 위의 자연스러운 동형
$$Rf_\ast R\mathcal{H}om(\mathcal{F}^\bullet, f^! \mathcal{G}^\bullet) \cong R\mathcal{H}om(Rf_! \mathcal{F}^\bullet, \mathcal{G}^\bullet)$$
이 성립한다. 전역 단면 $$R\Gamma(Y, -)$$을 취하면 대역적 형태
$$R\Hom_X(\mathcal{F}^\bullet, f^! \mathcal{G}^\bullet) \cong R\Hom_Y(Rf_! \mathcal{F}^\bullet, \mathcal{G}^\bullet)$$
을 얻는다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

국소적 형태를 Yoneda 논법으로 증명한다. 임의의 $$\mathcal{H}^\bullet \in D(\Sh(Y))$$에 대해 좌변과의 morphism 집합을 변형한다.
$$\begin{aligned}
\Hom_{D(Y)}\big(\mathcal{H}^\bullet, Rf_\ast R\mathcal{H}om(\mathcal{F}^\bullet, f^!\mathcal{G}^\bullet)\big)
&\cong \Hom_{D(X)}\big(f^{-1}\mathcal{H}^\bullet, R\mathcal{H}om(\mathcal{F}^\bullet, f^!\mathcal{G}^\bullet)\big) \\
&\cong \Hom_{D(X)}\big(f^{-1}\mathcal{H}^\bullet \otimes^L \mathcal{F}^\bullet, f^!\mathcal{G}^\bullet\big) \\
&\cong \Hom_{D(Y)}\big(Rf_!(f^{-1}\mathcal{H}^\bullet \otimes^L \mathcal{F}^\bullet), \mathcal{G}^\bullet\big) \\
&\cong \Hom_{D(Y)}\big(\mathcal{H}^\bullet \otimes^L Rf_!\mathcal{F}^\bullet, \mathcal{G}^\bullet\big) \\
&\cong \Hom_{D(Y)}\big(\mathcal{H}^\bullet, R\mathcal{H}om(Rf_!\mathcal{F}^\bullet, \mathcal{G}^\bullet)\big).
\end{aligned}$$
첫째 동형은 [§층의 유도 범주와 유도 함자, ⁋정리 9](/ko/math/sheaf_theory/derived_category_of_sheaves#thm9)의 $$(f^{-1}, Rf_\ast)$$ 수반이고, 둘째와 다섯째 동형은 [§층의 유도 범주와 유도 함자, ⁋명제 8](/ko/math/sheaf_theory/derived_category_of_sheaves#prop8)의 tensor-hom adjunction이며, 셋째 동형은 [§고유 받음과 여섯 함자, ⁋정의 6](/ko/math/sheaf_theory/six_functors#def6)의 $$(Rf_!, f^!)$$ 수반이고, 넷째 동형은 [§고유 받음과 여섯 함자, ⁋정리 9](/ko/math/sheaf_theory/six_functors#thm9)의 projection formula이다. 모든 자연 동형이 $$\mathcal{H}^\bullet$$에 함자적이므로 Yoneda 보조정리에 의해 양 끝의 대상이 동형이고, 이것이 국소적 형태이다.

대역적 형태는 국소적 형태에 $$R\Gamma(Y, -)$$을 적용하여 얻는다. $$a_Y \circ f = a_X$$이므로 [§층의 유도 범주와 유도 함자, ⁋정리 10](/ko/math/sheaf_theory/derived_category_of_sheaves#thm10)의 합성 동형에 의해 $$R\Gamma(Y, Rf_\ast(-)) = R\Gamma(X, -)$$이고, [§층의 유도 범주와 유도 함자, ⁋명제 8](/ko/math/sheaf_theory/derived_category_of_sheaves#prop8) 직후의 서술에 따라 $$R\Hom = R\Gamma \circ R\mathcal{H}om$$이므로, 좌변은 $$R\Gamma(X, R\mathcal{H}om(\mathcal{F}^\bullet, f^!\mathcal{G}^\bullet)) = R\Hom_X(\mathcal{F}^\bullet, f^!\mathcal{G}^\bullet)$$이고 우변은 $$R\Hom_Y(Rf_!\mathcal{F}^\bullet, \mathcal{G}^\bullet)$$이다.

</details>

대역적 형태에서 $$f = a_X: X \to \{\ast\}$$, $$\mathcal{G}^\bullet = k$$로 특수화하면 dualizing complex의 정의가 곧바로 작동하여, $$\mathbf{D}_X$$의 전역 cohomology가 콤팩트 받침 cohomology의 dual임을 얻는다. 이것이 Verdier 쌍대성의 가장 자주 인용되는 형태이다.

<div class="proposition" markdown="1">

<ins id="cor5">**따름정리 5**</ins> 임의의 $$\mathcal{F}^\bullet \in D(\Sh(X))$$에 대해 자연스러운 동형
$$R\Gamma(X, \mathbf{D}_X \mathcal{F}^\bullet) \cong R\Gamma_c(X, \mathcal{F}^\bullet)^\vee$$
이 성립한다. 특히 cohomology 차원에서 각 $$j$$에 대해
$$H^j(X, \mathbf{D}_X \mathcal{F}^\bullet) \cong H^{-j}_c(X, \mathcal{F}^\bullet)^\vee$$
이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[정리 4](#thm4)의 대역적 형태에서 $$f = a_X$$, $$\mathcal{G}^\bullet = k$$로 둔다. 우변은
$$R\Hom_{\{\ast\}}(R(a_X)_! \mathcal{F}^\bullet, k) = R\Hom_k(R\Gamma_c(X, \mathcal{F}^\bullet), k) = R\Gamma_c(X, \mathcal{F}^\bullet)^\vee$$
인데, 여기서 $$R(a_X)_! = R\Gamma_c(X, -)$$은 [§고유 받음과 여섯 함자, ⁋정의 11](/ko/math/sheaf_theory/six_functors#def11)이고 dual은 $$(-)^\vee = R\Hom_k(-, k)$$이다. 좌변은 $$a_X^! k = \omega_X$$이므로
$$R\Hom_X(\mathcal{F}^\bullet, a_X^! k) = R\Hom_X(\mathcal{F}^\bullet, \omega_X) = R\Gamma(X, R\mathcal{H}om(\mathcal{F}^\bullet, \omega_X)) = R\Gamma(X, \mathbf{D}_X \mathcal{F}^\bullet)$$
이다. 두 변을 같게 두면 첫 동형이 성립한다. cohomology 차원의 식은, field $$k$$ 위에서 dual functor $$R\Hom_k(-, k)$$이 exact하여 $$H^j(C^\bullet{}^\vee) = (H^{-j}(C^\bullet))^\vee$$이 성립하므로 얻어진다.

</details>

cohomological 형태 $$H^j(X, \mathbf{D}_X \mathcal{F}) \cong H^{-j}_c(X, \mathcal{F})^\vee$$이 모든 sheaf complex에 대해 성립한다는 점이 고전적 Poincaré 쌍대성을 넘어서는 일반성이다. 우변의 콤팩트 받침 cohomology가 차수의 부호를 뒤집어 좌변의 통상적 cohomology와 짝지어진다. field $$k$$를 택한 것이 결정적인데, $$\mathbb{Z}$$ 계수에서는 $$R\Hom_\mathbb{Z}(-, \mathbb{Z})$$이 $$\Ext^1_\mathbb{Z}$$ 항을 만들어 universal coefficient 보정이 붙으므로 위의 깔끔한 차수별 동형 대신 짧은 완전열이 끼어든다.

## Constructible complex와 biduality

[따름정리 5](#cor5)는 임의의 $$\mathcal{F}^\bullet$$에 대해 성립하지만, $$\mathbf{D}_X$$가 진정한 의미의 쌍대성, 즉 두 번 적용하면 항등으로 돌아오는 involution이 되려면 대상을 적절히 제한해야 한다. 임의의 sheaf complex는 너무 거칠어서 $$\mathbf{D}_X \mathbf{D}_X \mathcal{F}^\bullet$$이 $$\mathcal{F}^\bullet$$으로 돌아오지 않을 수 있다. 올바른 정의역은 위상적으로 잘 통제된 complex, 곧 constructible complex이다.

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> 위상공간 $$X$$의 *stratification<sub>층화</sub>*은 국소 유한한 locally closed 부분공간들의 분할 $$X = \bigsqcup_\alpha S_\alpha$$로서, 각 $$\overline{S_\alpha}$$가 다른 stratum들의 합집합이 되는 것을 말한다. 유계 complex $$\mathcal{F}^\bullet \in D^b(\Sh(X))$$가 *constructible<sub>구성가능</sub>*하다는 것은 어떤 stratification $$\{S_\alpha\}$$가 존재하여, 모든 $$j$$와 모든 $$\alpha$$에 대해 cohomology sheaf의 제한 $$\mathcal{H}^j(\mathcal{F}^\bullet)\vert_{S_\alpha}$$이 유한 rank의 locally constant sheaf가 되는 것이다. Constructible complex들이 이루는 $$D^b(\Sh(X))$$의 충만한 부분삼각범주를 $$D^b_c(X)$$로 적는다.

</div>

직관적으로 constructible complex는 공간을 유한히 많은 조각으로 잘랐을 때 각 조각 위에서 국소상수가 되는 complex이다. 상수 sheaf $$k_X$$ (전체를 한 stratum으로), 닫힌 부분다양체에 받침을 가진 상수 sheaf, 그리고 [예시 10](#ex10)에서 다룰 특이공간의 dualizing complex가 모두 이 부류에 속한다. 우리가 가정한 공간 위에서 $$D^b_c(X)$$는 여섯 함자 모두에 대해 닫혀 있으며, 특히 $$\omega_X \in D^b_c(X)$$이고 $$\mathbf{D}_X$$가 $$D^b_c(X)$$를 자기 자신으로 보낸다. 이 사실의 증명은 stratification에 대한 귀납과 [§고유 받음과 여섯 함자, ⁋정리 10](/ko/math/sheaf_theory/six_functors#thm10)의 recollement triangle을 사용하며, 그 자체로 상당한 분량이므로 여기서는 결과만 인용하고 [KS]의 §3.4와 [Dim]의 §4를 참조한다.

<div class="proposition" markdown="1">

<ins id="thm7">**정리 7 (biduality)**</ins> $$\mathcal{F}^\bullet \in D^b_c(X)$$에 대해 자연스러운 동형
$$\mathcal{F}^\bullet \xrightarrow{\ \sim\ } \mathbf{D}_X \mathbf{D}_X \mathcal{F}^\bullet$$
이 성립한다. 따라서 $$\mathbf{D}_X: D^b_c(X)^{\op} \to D^b_c(X)$$는 삼각범주의 anti-equivalence이며 $$\mathbf{D}_X^2 \cong \id$$이다.

</div>
<details class="proof" markdown="1">
<summary>증명 (개요)</summary>

자연 사상 $$\mathcal{F}^\bullet \to \mathbf{D}_X \mathbf{D}_X \mathcal{F}^\bullet$$은 tensor-hom adjunction의 evaluation, 즉 $$\mathcal{F}^\bullet \otimes^L R\mathcal{H}om(\mathcal{F}^\bullet, \omega_X) \to \omega_X$$에 대응하는 사상으로 표준적으로 존재한다 ([§층의 유도 범주와 유도 함자, ⁋명제 8](/ko/math/sheaf_theory/derived_category_of_sheaves#prop8)). 이것이 동형임을 보이는 것이 핵심이며, 동형 여부는 [§층의 유도 범주와 유도 함자, ⁋명제 1](/ko/math/sheaf_theory/derived_category_of_sheaves#prop1)의 stalk 판정에 의해 국소적인 문제이다. Stratification에 대한 귀납으로 환원되는데, 가장 낮은 차원의 stratum은 다양체이므로 그 위에서는 $$\omega$$가 shift된 국소계가 되어 ([§고유 받음과 여섯 함자, ⁋정리 7](/ko/math/sheaf_theory/six_functors#thm7)) biduality가 유한차원 vector space의 표준 동형 $$V \cong (V^\vee)^\vee$$으로 귀착되고, 이는 $$\mathcal{H}^j(\mathcal{F}^\bullet)$$의 stalk가 유한 rank라는 constructibility 가정에서 성립한다. 높은 차원의 stratum으로는 [§고유 받음과 여섯 함자, ⁋정리 10](/ko/math/sheaf_theory/six_functors#thm10)의 recollement triangle을 따라 $$\mathbf{D}_X$$가 두 변을 동형으로 보냄을 이어 올린다. 유한 rank 조건이 빠지면 $$V \cong (V^\vee)^\vee$$이 깨지므로 constructibility는 필수적이다. 자세한 논증은 [KS]의 Proposition 3.4.3을 따른다.

</details>

biduality가 성립하면 $$\mathbf{D}_X$$는 다른 다섯 함자와의 호환 관계를 통해 그들을 짝지어 교환한다. 다음 명제는 Verdier 쌍대성의 형식적 귀결로서, $$\mathbf{D}$$가 $$Rf_\ast$$와 $$Rf_!$$을, 그리고 $$Lf^\ast$$와 $$f^!$$을 서로 맞바꾼다는 것을 말한다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> Compactifiable map $$f: X \to Y$$와 $$\mathcal{F}^\bullet \in D^b_c(X)$$, $$\mathcal{G}^\bullet \in D^b_c(Y)$$에 대해 자연스러운 동형
$$\mathbf{D}_Y(Rf_! \mathcal{F}^\bullet) \cong Rf_\ast(\mathbf{D}_X \mathcal{F}^\bullet), \qquad f^!(\mathbf{D}_Y \mathcal{G}^\bullet) \cong \mathbf{D}_X(f^{-1}\mathcal{G}^\bullet)$$
이 성립한다. biduality와 결합하면 이로부터 $$Rf_! \cong \mathbf{D}_Y Rf_\ast \mathbf{D}_X$$와 $$f^! \cong \mathbf{D}_X f^{-1} \mathbf{D}_Y$$을 얻는다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

첫 동형은 [정리 4](#thm4)의 국소적 형태에서 $$\mathcal{G}^\bullet$$를 $$\omega_Y$$로 둔 경우이다. 그러면 좌변은 $$Rf_\ast R\mathcal{H}om(\mathcal{F}^\bullet, f^!\omega_Y)$$인데, $$a_Y f = a_X$$이므로 $$f^! \omega_Y = f^! a_Y^! k = (a_Y f)^! k = a_X^! k = \omega_X$$이고, 따라서 좌변은 $$Rf_\ast R\mathcal{H}om(\mathcal{F}^\bullet, \omega_X) = Rf_\ast(\mathbf{D}_X \mathcal{F}^\bullet)$$이다. 우변은 $$R\mathcal{H}om(Rf_!\mathcal{F}^\bullet, \omega_Y) = \mathbf{D}_Y(Rf_!\mathcal{F}^\bullet)$$이다. 이로써 첫 동형이 성립한다.

둘째 동형은 첫 동형과 $$\mathbf{D}$$의 anti-equivalence를 결합한 Yoneda 논법으로 얻는다. 임의의 $$\mathcal{F}^\bullet \in D^b_c(X)$$에 대해
$$\begin{aligned}
\Hom_{D(X)}\big(\mathcal{F}^\bullet, \mathbf{D}_X f^{-1}\mathbf{D}_Y\mathcal{G}^\bullet\big)
&\cong \Hom_{D(X)}\big(f^{-1}\mathbf{D}_Y\mathcal{G}^\bullet, \mathbf{D}_X\mathcal{F}^\bullet\big) \\
&\cong \Hom_{D(Y)}\big(\mathbf{D}_Y\mathcal{G}^\bullet, Rf_\ast \mathbf{D}_X\mathcal{F}^\bullet\big) \\
&\cong \Hom_{D(Y)}\big(\mathbf{D}_Y\mathcal{G}^\bullet, \mathbf{D}_Y Rf_!\mathcal{F}^\bullet\big) \\
&\cong \Hom_{D(Y)}\big(Rf_!\mathcal{F}^\bullet, \mathcal{G}^\bullet\big) \\
&\cong \Hom_{D(X)}\big(\mathcal{F}^\bullet, f^!\mathcal{G}^\bullet\big)
\end{aligned}$$
이다. 첫째와 넷째 동형은 $$\mathbf{D}_X$$와 $$\mathbf{D}_Y$$가 $$D^b_c$$ 위에서 contravariant equivalence라는 [정리 7](#thm7)의 귀결이고, 둘째 동형은 [§층의 유도 범주와 유도 함자, ⁋정리 9](/ko/math/sheaf_theory/derived_category_of_sheaves#thm9)의 $$(f^{-1}, Rf_\ast)$$ 수반이며, 셋째 동형은 방금 증명한 첫 동형, 다섯째 동형은 [§고유 받음과 여섯 함자, ⁋정의 6](/ko/math/sheaf_theory/six_functors#def6)의 $$(Rf_!, f^!)$$ 수반이다. Yoneda 보조정리에 의해 $$\mathbf{D}_X f^{-1}\mathbf{D}_Y\mathcal{G}^\bullet \cong f^!\mathcal{G}^\bullet$$이고, $$\mathcal{G}^\bullet$$을 $$\mathbf{D}_Y\mathcal{G}^\bullet$$으로 바꾼 뒤 [정리 7](#thm7)의 $$\mathbf{D}_Y^2 \cong \id$$을 쓰면 $$f^!\mathbf{D}_Y\mathcal{G}^\bullet \cong \mathbf{D}_X f^{-1}\mathcal{G}^\bullet$$을 얻는다. 끝의 두 식은 양변에 $$\mathbf{D}$$를 적용하고 다시 $$\mathbf{D}^2 \cong \id$$을 쓰면 따라 나온다.

</details>

명제는 여섯 함자가 $$\mathbf{D}$$ 아래에서 둘씩 짝을 이룬다는 구조를 드러낸다. $$Rf_\ast$$와 $$Rf_!$$이 한 쌍, $$Lf^\ast = f^{-1}$$과 $$f^!$$이 한 쌍이다. 이 대칭은 여섯 함자 형식이 단지 함자들의 모음이 아니라 쌍대성을 내장한 구조임을 보여 주며, perverse sheaf 이론에서 self-dual 객체를 다룰 때 본질적인 역할을 한다.

## Poincaré 쌍대성의 회복

이제 가장 고전적인 경우로 돌아가, Verdier 쌍대성이 다양체의 Poincaré 쌍대성을 특수한 경우로 포함함을 확인한다. 관건은 다양체에서 dualizing complex가 shift된 상수 sheaf로 단순화된다는 [정의 1](#def1) 직후의 관찰이다.

<div class="proposition" markdown="1">

<ins id="thm9">**정리 9 (Poincaré 쌍대성)**</ins> $$X$$가 connected oriented $$n$$차원 위상다양체이면 $$\omega_X \cong k_X[n]$$이고, 각 $$p$$에 대해 자연스러운 동형
$$H^p(X, k) \cong H^{n-p}_c(X, k)^\vee$$
이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$a_X: X \to \{\ast\}$$은 fiber가 $$X$$ 자신인 $$n$$차원 topological submersion이고, $$X$$가 방향지어졌으므로 상대 orientation sheaf는 $$\operatorname{or}_{X/\{\ast\}} \cong k_X$$이다 ([\[대수적 위상수학\] §푸앵카레 쌍대성, ⁋정의 1](/ko/math/algebraic_topology/Poincare_duality#def1)의 orientation sheaf가 자명한 경우). 따라서 [§고유 받음과 여섯 함자, ⁋정리 7](/ko/math/sheaf_theory/six_functors#thm7)에 의해
$$\omega_X = a_X^! k \cong a_X^{-1} k \otimes \operatorname{or}_{X/\{\ast\}}[n] \cong k_X[n]$$
이다. 그러면 $$\mathbf{D}_X k_X = R\mathcal{H}om(k_X, \omega_X) \cong \omega_X \cong k_X[n]$$이다. [따름정리 5](#cor5)를 $$\mathcal{F}^\bullet = k_X$$에 적용하면
$$H^j(X, \mathbf{D}_X k_X) \cong H^{-j}_c(X, k)^\vee$$
인데, 좌변은 $$H^j(X, k_X[n]) = H^{j+n}(X, k)$$이다. $$p = j + n$$으로 치환하면 $$-j = n - p$$이므로 $$H^p(X, k) \cong H^{n-p}_c(X, k)^\vee$$을 얻는다.

</details>

이 동형을 [\[대수적 위상수학\] §푸앵카레 쌍대성, ⁋정리 11](/ko/math/algebraic_topology/Poincare_duality#thm11)의 고전적 진술과 대조하는 것이 유익하다. 그 정리는 방향지어진 콤팩트 $$n$$차원 다양체 $$M$$에 대해 fundamental class와의 cap product가 동형 $$H^p(M; A) \cong H_{n-p}(M; A)$$을 준다고 말한다. $$M$$이 콤팩트이면 [§고유 받음과 여섯 함자, ⁋따름정리 4](/ko/math/sheaf_theory/six_functors#cor4)에 의해 $$H^{n-p}_c(M, k) = H^{n-p}(M, k)$$이고, field $$k$$ 위에서 universal coefficient에 의해 $$H^{n-p}(M, k)^\vee \cong H_{n-p}(M, k)$$이므로, [정리 9](#thm9)의 우변은 $$H_{n-p}(M, k)$$으로 정리되어 고전적 형태와 정확히 일치한다. 두 진술의 차이는 도달하는 경로에 있다. 고전적 증명은 fundamental class라는 기하학적 cycle을 cap product로 작용시키는 반면, Verdier 쌍대성은 같은 동형을 $$a_X^! k \cong k_X[n]$$이라는 함자적 사실로부터 끌어낸다. 후자는 콤팩트성을 요구하지 않으며 ($$H_c$$가 그 역할을 흡수한다) 상수 계수에 국한되지 않으므로, 임의의 국소계나 더 일반적인 constructible complex로 그대로 확장된다.

비콤팩트 경우의 구체적 점검으로 $$X = \mathbb{R}^n$$을 보면, [§고유 받음과 여섯 함자, ⁋예시 12](/ko/math/sheaf_theory/six_functors#ex12)에서 계산한 $$H^{n-p}_c(\mathbb{R}^n, k) \cong k$$ ($$p = 0$$일 때, 즉 $$n - p = n$$일 때) 외에는 $$0$$이라는 결과와, $$H^p(\mathbb{R}^n, k) \cong k$$ ($$p = 0$$), 그 외 $$0$$이라는 가축성이 [정리 9](#thm9)의 동형 $$H^0 \cong (H^n_c)^\vee$$을 통해 정확히 맞아떨어진다. 콤팩트성을 콤팩트 받침 cohomology가 대신함을 보여 주는 가장 단순한 사례이다.

## 특이공간에서의 dualizing complex

Verdier 쌍대성 자체는 [정리 4](#thm4)에서 보았듯 다양체 가정 없이 성립한다. 그러나 [정리 9](#thm9)의 결정적 단순화, 곧 $$\omega_X \cong k_X[n]$$은 다양체에서만 성립한다. 특이점이 있는 공간에서는 dualizing complex가 shift된 상수 sheaf가 아니며, 바로 이 사실이 특이공간의 cohomology가 Poincaré 쌍대성을 만족하지 못하는 근원이자 intersection cohomology가 필요해지는 출발점이다. 가장 기본적인 특이점인 node에서 이를 구체적으로 계산한다.

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> 복소 평면곡선의 node $$X = \{(x, y) \in \mathbb{C}^2 : xy = 0\}$$를 생각하자. 이는 두 복소직선 $$\{x = 0\}$$과 $$\{y = 0\}$$이 원점 $$0$$에서 만나는 공간으로, 실 $$2$$차원이며 $$0$$을 제외하면 매끄럽다. 우리는 dualizing complex $$\omega_X$$의 원점에서의 stalk cohomology가
$$\mathcal{H}^{-2}(\omega_X)_0 \cong k^2, \qquad \mathcal{H}^{-1}(\omega_X)_0 \cong k$$
임을 보인다. 이는 $$2$$차원 다양체라면 가졌을 $$\omega \cong k_X[2]$$의 stalk, 즉 $$\mathcal{H}^{-2} \cong k$$, $$\mathcal{H}^{-1} \cong 0$$과 다르다.

</div>

계산은 [명제 3](#prop3)에 기반한 국소적 묘사에서 출발한다. dualizing complex의 stalk는 작은 열린근방의 쌍대성으로 표현되는데, [명제 3](#prop3)에 의해 열린근방 $$U \ni 0$$ 위에서 $$\omega_X\vert_U = \omega_U$$이므로
$$\mathcal{H}^j(\omega_X)_0 = \varinjlim_{U \ni 0} H^j(U, \omega_U) = \varinjlim_{U \ni 0} H^j(U, \mathbf{D}_U k_U)$$
이고, [따름정리 5](#cor5)를 $$U$$ 위에서 $$\mathcal{F}^\bullet = k_U$$에 적용하면 $$H^j(U, \mathbf{D}_U k_U) \cong H^{-j}_c(U, k)^\vee$$이다. 따라서 충분히 작은 원뿔형 근방 $$U$$에 대한 콤팩트 받침 cohomology $$H^\bullet_c(U, k)$$을 계산하면 된다. (이 colimit은 원뿔형 근방들의 cofinal 계열 위에서 안정화되며, 그 극한값이 곧 stalk이다. 이 사실은 $$\mathcal{H}^{-i}(\omega_X)_0 \cong H^{BM}_i(U)$$, 즉 dualizing complex의 stalk가 국소 Borel–Moore homology라는 표준적 해석의 한 형태이다.)

원점의 작은 근방 $$U$$는 두 복소직선 각각에서의 작은 원판 $$\{x = 0, \lvert y\rvert < \varepsilon\}$$과 $$\{y = 0, \lvert x\rvert < \varepsilon\}$$이 원점에서 한 점으로 붙은 공간, 곧 두 개의 열린 $$2$$-원판을 중심에서 접합한 공간이다. 그 link는 두 원 $$S^1 \sqcup S^1$$이다. $$H^\bullet_c(U, k)$$을 계산하기 위해 닫힌집합 $$\{0\}$$과 열린 보충집합 $$V = U \setminus \{0\}$$에 대한 [§고유 받음과 여섯 함자, ⁋정리 10](/ko/math/sheaf_theory/six_functors#thm10)의 첫째 recollement triangle에 $$R\Gamma_c(U, -)$$을 적용한다. 보충집합 $$V$$는 두 개의 punctured disk, 즉 두 개의 $$S^1 \times \mathbb{R}$$의 disjoint union이다. 각 $$S^1 \times \mathbb{R}$$은 방향지어진 $$2$$차원 다양체이므로 [정리 9](#thm9)에 의해 $$H^q_c(S^1 \times \mathbb{R}, k) \cong H^{2-q}(S^1 \times \mathbb{R}, k)^\vee \cong H^{2-q}(S^1, k)^\vee$$ ($$\mathbb{R}$$이 가축이므로 Künneth에 의해 $$H^\bullet(S^1 \times \mathbb{R}) \cong H^\bullet(S^1)$$)이고, 이는 $$q = 1$$과 $$q = 2$$에서 각각 $$k$$, 그 외에는 $$0$$이다. 따라서 두 성분을 합하여
$$H^1_c(V, k) \cong k^2, \qquad H^2_c(V, k) \cong k^2$$
이고 나머지 차수는 $$0$$이다. 한편 $$H^q_c(\{0\}, k) = H^q(\{0\}, k)$$은 $$q = 0$$에서 $$k$$, 그 외 $$0$$이다.

recollement triangle이 주는 long exact sequence
$$\cdots \to H^q_c(V) \to H^q_c(U) \to H^q(\{0\}) \to H^{q+1}_c(V) \to \cdots$$
를 차수별로 읽는다. $$U$$가 연결이고 콤팩트하지 않으므로 $$H^0_c(U) = 0$$이며, 따라서 $$q = 0$$ 부분
$$0 = H^0_c(V) \to H^0_c(U) = 0 \to H^0(\{0\}) = k \xrightarrow{\delta} H^1_c(V) = k^2 \to H^1_c(U) \to H^1(\{0\}) = 0$$
에서 연결 사상 $$\delta$$가 단사이고, $$H^1_c(U) = \operatorname{coker}\delta \cong k^2 / k \cong k$$이다. 한편 $$q \geq 1$$ 부분에서 $$H^1(\{0\}) = 0 \to H^2_c(V) = k^2 \to H^2_c(U) \to H^2(\{0\}) = 0$$이므로 $$H^2_c(U) \cong k^2$$이다. 정리하면 $$H^1_c(U, k) \cong k$$, $$H^2_c(U, k) \cong k^2$$이고 그 외는 $$0$$이다. (검산으로 콤팩트 받침 Euler 지표는 $$\chi_c(U) = \chi_c(V) + \chi_c(\{0\})$$에서 $$\chi_c(S^1 \times \mathbb{R}) = 0$$이므로 $$\chi_c(U) = 0 + 1 = 1$$이고, $$-\dim H^1_c + \dim H^2_c = -1 + 2 = 1$$과 일치한다.)

이제 stalk 공식 $$\mathcal{H}^j(\omega_X)_0 \cong H^{-j}_c(U, k)^\vee$$에 대입하면 $$\mathcal{H}^{-2}(\omega_X)_0 \cong H^2_c(U)^\vee \cong k^2$$, $$\mathcal{H}^{-1}(\omega_X)_0 \cong H^1_c(U)^\vee \cong k$$을 얻어 [예시 10](#ex10)의 주장이 확인된다. 최고차 stalk $$\mathcal{H}^{-2}(\omega_X)_0 \cong k^2$$의 차원 $$2$$는 node를 지나는 국소 분지(branch)의 수와 정확히 일치하며, $$0$$이어야 할 $$\mathcal{H}^{-1}(\omega_X)_0$$에 추가로 나타나는 $$k$$가 특이점이 만들어 내는 잉여 항이다. 매끄러운 다양체였다면 [정리 9](#thm9)에 의해 $$\omega_X$$이 한 차수에 집중되었을 것이나, node에서는 두 차수에 퍼진다.

<div class="remark" markdown="1">

<ins id="rmk11">**참고 11**</ins> [예시 10](#ex10)이 보여 주는 현상은 특이공간의 cohomology 이론을 다시 설계해야 할 필요를 시사한다. $$\omega_X$$가 shift된 상수 sheaf가 아니므로 $$\mathbf{D}_X k_X = \omega_X \not\cong k_X[n]$$이고, 따라서 [정리 9](#thm9)의 유도가 무너져 통상적 cohomology $$H^\bullet(X)$$은 더 이상 Poincaré 쌍대성을 만족하지 않는다. 이를 복구하려면 $$k_X$$를 대신할, 그 자체로 self-dual에 가까운 constructible complex를 찾아야 한다. 그러한 complex를 stratification에 적합한 "중간" 받음과 절단으로 구성하여 특이공간에서 Poincaré 쌍대성을 회복하는 것이 intersection cohomology와 그 sheaf 차원 정식화의 출발점이며, 이는 constructible complex의 추가 구조를 다룬 뒤에 본격적으로 전개된다.

</div>

---

**참고문헌**

**[KS]** M. Kashiwara, P. Schapira, *Sheaves on manifolds*, Springer, 1990.

**[Iv]** B. Iversen, *Cohomology of sheaves*, Springer, 1986.

**[Dim]** A. Dimca, *Sheaves in topology*, Springer, 2004.

**[Ver]** J.-L. Verdier, *Dualité dans la cohomologie des espaces localement compacts*, Séminaire Bourbaki, 1965–1966.
