---
title: "고유 받음과 여섯 함자"
description: "콤팩트 받침을 따른 고유 받음 Rf_!와 그 오른쪽 수반 f^!를 도입하여 Rf_*·Lf^*·⊗^L·RHom과 함께 여섯 함자 형식을 완성하고, proper base change와 projection formula를 다룬다."
excerpt: "Rf_! and f^!, the six-functor formalism, proper base change, and the projection formula"

categories: [Math / Sheaf Theory]
permalink: /ko/math/sheaf_theory/six_functors
sidebar: 
    nav: "sheaf_theory-ko"

date: 2026-07-01
last_modified_at: 2026-07-01
weight: 2

published: false

---

[§층의 유도 범주와 유도 함자](/ko/math/sheaf_theory/derived_category_of_sheaves)에서 우리는 위상공간 $$X$$ 위의 sheaf가 이루는 abelian category $$\Sh(X)$$가 충분한 injective를 가짐을 확인하고, 그 유도 범주 $$D(\Sh(X))$$ 위에서 네 개의 유도 함자 $$Rf_\ast$$, $$Lf^\ast$$, $$\otimes^L$$, $$R\Hom$$을 정의하였다. 이들은 sheaf 이론의 functoriality를 derived 차원에서 정돈하며, $$(Lf^\ast, Rf_\ast)$$ adjunction과 합성 동형 $$R(gf)_\ast \cong Rg_\ast Rf_\ast$$로 Leray spectral sequence를 한 줄로 회복한다.

그러나 이 네 함자만으로는 sheaf 이론에서 가장 강력한 구조적 결과인 duality에 도달하지 못한다. 그 근본적인 이유는 $$Rf_\ast$$가 콤팩트 받침을 보지 못한다는 데 있다. 한 점으로의 사상 $$a_X: X \to \{\ast\}$$에 대해 $$R(a_X)_\ast = R\Gamma(X, -)$$는 임의의 단면을 세는 통상적인 cohomology를 주지만, 비콤팩트 공간 위에서 Poincaré duality를 진술하려면 받침이 콤팩트한 단면만을 세는 cohomology, 즉 콤팩트 받침 cohomology $$R\Gamma_c$$가 필요하다. 예컨대 실 직선 $$\mathbb{R}$$ 위의 상수 sheaf $$\mathbb{Z}_\mathbb{R}$$는 $$H^0(\mathbb{R}, \mathbb{Z}) = \mathbb{Z}$$로 차수 $$0$$에 집중되지만, 그 콤팩트 받침 cohomology는 뒤에서 보듯 차수 $$1$$에 집중되어 $$1$$차원 다양체의 Poincaré duality를 구현한다.

이 글에서 우리는 콤팩트 받침을 따르는 *고유 받음<sub>proper direct image</sub>* $$Rf_!$$와 그 오른쪽 수반인 *예외 역상<sub>exceptional inverse image</sub>* $$f^!$$를 도입한다. $$Rf_\ast$$, $$Rf_!$$, $$Lf^\ast$$, $$f^!$$, $$\otimes^L$$, $$R\Hom$$의 여섯 함자와 그들 사이의 두 adjunction, proper base change, projection formula가 이루는 구조를 *six-functor formalism<sub>여섯 함자 형식</sub>*이라 부르며, 이것이 Verdier duality를 비롯한 sheaf 이론의 핵심 정리들이 작동하는 무대이다. 추상적 derived category와 앞의 네 함자는 [§층의 유도 범주와 유도 함자](/ko/math/sheaf_theory/derived_category_of_sheaves)에서 세웠으므로 여기서는 인용하고, 새로운 두 함자 $$Rf_!$$와 $$f^!$$의 구성과 그들이 완성하는 형식에 집중한다.

이 글 전체에서 위상공간은 locally compact Hausdorff이고 가산 무한대를 가지며 유한한 cohomological dimension을 갖는 것으로 한정하고, 사상은 모두 연속인 separated map으로 한정한다. 이 조건들은 $$Rf_!$$가 유한한 cohomological amplitude를 가지고 잘 정의되도록 하는 표준적인 가설이다. 계수로는 별도의 언급이 없으면 abelian group의 sheaf, 즉 $$\mathcal{O}_X = \mathbb{Z}_X$$인 경우를 다루며, 이 경우 [§층의 유도 범주와 유도 함자, ⁋명제 5](/ko/math/sheaf_theory/derived_category_of_sheaves#prop5)에 의해 $$Lf^\ast = f^{-1}$$이 derivation 없이 정의된다.

## 고유 받음의 정의

직접상 $$f_\ast \mathcal{F}$$의 열린집합 $$V \subseteq Y$$ 위의 단면은 $$\mathcal{F}(f^{-1}(V))$$의 단면, 즉 $$f^{-1}(V)$$ 전체에서 정의된 단면이다. 고유 받음은 이 가운데 받침이 $$f$$에 대해 proper한 것만을 추려 내는 부분 함자로 정의되며, 받침의 proper성은 [§고유함수](/ko/math/topology/proper_maps)에서 다룬 universally closed 사상의 언어로 표현된다. 그러나 derived 차원에서 이 함자를 직접 다루기보다는, Deligne을 따라 사상을 콤팩트화하여 이미 가진 두 함자 $$j_!$$과 $$Rp_\ast$$의 합성으로 정의하는 편이 깔끔하다.

열린 매장 $$j: U \hookrightarrow X$$에 대한 extension by zero $$j_!: \Sh(U) \to \Sh(X)$$를 떠올리자. 이는 $$U$$ 위의 sheaf $$\mathcal{F}$$를 $$X \setminus U$$ 위에서 stalk $$0$$이 되도록 연장하는 함자로, $$j^{-1}$$의 왼쪽 수반이다. ([\[위상수학\] §층, ⁋예시 14](/ko/math/topology/sheaves#ex14)) $$j_!$$은 stalk를 보존하는 exact functor이므로 $$D(\Sh(U)) \to D(\Sh(X))$$로 곧바로 내려간다. 한편 proper map $$p$$, 즉 closed이며 모든 fiber가 compact인 사상에 대해서는 ([\[위상수학\] §고유함수, ⁋정리 6](/ko/math/topology/proper_maps#thm6)) $$Rp_\ast$$가 이미 정의되어 있다.

::: 정의 1
Separated map $$f: X \to Y$$가 *compactifiable*하다는 것은 열린 매장 $$j: X \hookrightarrow \overline{X}$$와 proper map $$p: \overline{X} \to Y$$가 존재하여 $$f = p \circ j$$로 분해되는 것이다. 이러한 분해 $$(j, p)$$를 $$f$$의 *compactification*이라 부른다. $$f$$의 compactification $$(j, p)$$가 주어졌을 때 *고유 받음<sub>proper direct image</sub>* $$Rf_!: D(\Sh(X)) \to D(\Sh(Y))$$를
$$Rf_! := Rp_\ast \circ j_!$$
로 정의한다.
:::

여기서 $$j_!$$은 exact이므로 derived할 필요가 없고 $$Rp_\ast$$만 $$p$$의 properness를 통해 통제되므로, $$Rf_!$$은 잘 정의된 함자이다. 우리가 다루는 locally compact Hausdorff 공간 사이의 separated map은 항상 compactifiable한데, 가장 기본적인 예로 $$f = a_X: X \to \{\ast\}$$의 경우 $$X$$의 one-point compactification $$\overline{X} = X \cup \{\infty\}$$을 택하면 $$j: X \hookrightarrow \overline{X}$$는 열린 매장이고 $$\overline{X}$$가 compact이므로 $$p: \overline{X} \to \{\ast\}$$는 proper이다. 일반적인 $$f$$에 대해서도 fiber별 one-point compactification을 이어 붙여 compactification을 얻는다. 정의가 의미를 가지려면 $$Rp_\ast \circ j_!$$이 compactification의 선택에 의존하지 않음을 보여야 하는데, 이는 proper map에 대한 base change 정리로부터 따라 나온다. 따라서 먼저 그 정리를 진술한다.

proper base change는 $$Rp_\ast$$를 fiber별로 계산할 수 있게 해 주는 정리로, 그 핵심은 proper map의 higher direct image의 stalk가 fiber 위의 cohomology로 주어진다는 사실이다. 다음 형태의 cartesian square를 생각하자. $$g: Y' \to Y$$가 임의의 연속함수이고 $$f: X \to Y$$가 주어졌을 때, fiber product $$X' = X \times_Y Y'$$와 사영 $$g': X' \to X$$, $$f': X' \to Y'$$를 둔다.

![고유 받음의 base change를 정의하는 cartesian square](/assets/images/Math/Sheaf_Theory/Six_Functors-1.svg){:style="width:6.59em" class="invert" .align-center}

::: 정리 2 (proper base change)
위의 cartesian square에서 $$f$$가 proper라 하자. 그럼 $$\mathcal{F}^\bullet \in D^+(\Sh(X))$$에 대해 자연스러운 동형
$$g^{-1} Rf_\ast \mathcal{F}^\bullet \cong Rf'_\ast (g')^{-1} \mathcal{F}^\bullet$$
이 성립한다. 특히 $$Y' = \{y\}$$를 한 점으로 두면 각 $$y \in Y$$에서 stalk 차원의 동형
$$(R^q f_\ast \mathcal{F})_y \cong H^q(f^{-1}(y), \mathcal{F}\vert_{f^{-1}(y)})$$
를 얻는다.
:::
::: 증명
핵심은 stalk 공식이며, 일반적인 base change 동형은 이로부터 양변의 stalk를 비교하여 따라 나온다. Higher direct image $$R^q f_\ast \mathcal{F}$$는 presheaf $$V \mapsto H^q(f^{-1}(V), \mathcal{F})$$의 sheafification이므로, 그 stalk는 $$y$$를 포함하는 열린집합 $$V$$들에 대한 colimit $$\varinjlim_V H^q(f^{-1}(V), \mathcal{F})$$이다. $$f$$가 proper이면 $$y$$의 fiber $$f^{-1}(y)$$가 compact이고 ([\[위상수학\] §고유함수, ⁋정리 6](/ko/math/topology/proper_maps#thm6)), $$Y$$가 locally compact Hausdorff이므로 $$f^{-1}(y)$$의 임의의 열린근방은 어떤 $$f^{-1}(V)$$를 포함한다. 이때 compact 받침에 대한 cohomology의 연속성, 즉 닫힌집합 $$f^{-1}(y) = \bigcap_V f^{-1}(\overline{V})$$ 위의 cohomology가 근방들의 cohomology의 colimit으로 주어진다는 사실에 의해 ([KS], Proposition 2.5.2)
$$\varinjlim_V H^q(f^{-1}(V), \mathcal{F}) \cong H^q(f^{-1}(y), \mathcal{F}\vert_{f^{-1}(y)})$$
가 성립한다. 이로써 stalk 공식이 증명된다.

일반적인 cartesian square에 대해서는 양변에 $$y' \in Y'$$에서 stalk를 취한다. 우변 $$Rf'_\ast (g')^{-1}\mathcal{F}$$의 stalk는 방금의 공식에 의해 $$f'^{-1}(y') = f^{-1}(g(y'))$$ 위의 cohomology이고, 좌변 $$g^{-1}Rf_\ast \mathcal{F}$$의 stalk는 $$(Rf_\ast \mathcal{F})_{g(y')}$$이므로 다시 같은 fiber 위의 cohomology이다. Fiber product의 정의에 의해 두 fiber가 위상동형이므로 두 stalk가 일치하고, 이 동형이 자연스러움을 확인하면 된다. 자세한 논증은 [KS]의 Proposition 2.6.7을 따른다.
:::

stalk 공식은 proper map에 대해서는 $$Rf_\ast$$를 fiber 위의 통상적 cohomology로 점별로 읽을 수 있음을 말한다. 이는 비proper map에서는 성립하지 않으며, 바로 이 fiber별 읽기 가능성이 고유 받음을 base change에 대해 잘 행동하게 만드는 근원이다. 이제 이 정리를 이용해 [정의 1](#def1)이 compactification의 선택에 무관함을 본다.

::: 명제 3
Compactifiable map $$f: X \to Y$$의 고유 받음 $$Rf_!$$은 compactification $$(j, p)$$의 선택에 의존하지 않는다.
:::
::: 증명
두 compactification $$f = p_1 j_1 = p_2 j_2$$가 주어졌다 하자. 먼저 한 compactification이 다른 것을 지배하는 경우, 즉 $$\overline{X}_1 \to \overline{X}_2$$인 proper map $$\pi$$가 있어 $$j_2 = \pi j_1$$, $$p_1 = p_2 \pi$$인 경우를 본다. 이때 받침이 $$X$$ 안에 proper하게 들어 있는 단면을 $$\overline{X}_2$$로 곧바로 연장하든($$j_2{}_!$$) $$\overline{X}_1$$을 거쳐 연장한 뒤 밀어내든($$R\pi_\ast j_1{}_!$$) 결과가 같다는 것이 핵심이며, 이는 $$\pi$$가 $$X$$ 위에서 동형이고 그 보충집합 위에서 proper이므로 [정리 2](#thm2)의 stalk 공식으로 확인된다. 보충집합 $$\overline{X}_2 \setminus X$$의 점 $$z$$에서 $$\pi^{-1}(z)$$ 위의 $$j_1{}_!(\cdots)$$의 단면은 받침이 $$X$$와 만나지 않아 $$0$$이므로, $$(R\pi_\ast j_1{}_! \mathcal{F})_z = 0 = (j_2{}_! \mathcal{F})_z$$이고, $$X$$ 위에서는 양변이 모두 $$\mathcal{F}$$이다. 따라서 $$j_2{}_! \cong R\pi_\ast j_1{}_!$$이고, $$Rp_2{}_\ast$$를 적용하면
$$Rp_2{}_\ast j_2{}_! \cong Rp_2{}_\ast R\pi_\ast j_1{}_! \cong R(p_2 \pi)_\ast j_1{}_! = Rp_1{}_\ast j_1{}_!$$
을 얻는다. 두 번째 동형은 [§층의 유도 범주와 유도 함자, ⁋정리 10](/ko/math/sheaf_theory/derived_category_of_sheaves#thm10)의 합성 정리이다.

일반적인 두 compactification에 대해서는 곱 $$\overline{X}_1 \times_Y \overline{X}_2$$ 안에서 $$X$$의 graph의 closure를 취하면 두 compactification을 동시에 지배하는 제3의 compactification을 얻으며, 위 경우를 두 번 적용해 $$Rp_1{}_\ast j_1{}_! \cong Rp_2{}_\ast j_2{}_!$$을 얻는다.
:::

이 명제로 $$Rf_!$$이 함자로서 잘 정의된다. 정의의 즉각적인 귀결로 proper map에 대해서는 고유 받음이 통상적인 받음과 일치한다.

::: 따름정리 4
$$f: X \to Y$$가 proper map이면 $$Rf_! \cong Rf_\ast$$이다.
:::
::: 증명
$$f$$ 자신이 proper이므로 항등 열린 매장 $$j = \id_X$$와 $$p = f$$로 이루어진 자명한 compactification $$f = f \circ \id_X$$을 택할 수 있다. $$\id_X{}_! = \id$$이므로 [명제 3](#prop3)에 의해 $$Rf_! = R f_\ast \circ \id = Rf_\ast$$이다.
:::

특히 $$X$$가 compact이면 $$a_X: X \to \{\ast\}$$가 proper이므로 $$R\Gamma_c(X, -) = R(a_X)_! = R(a_X)_\ast = R\Gamma(X, -)$$이 되어, compact 공간에서는 콤팩트 받침 cohomology와 통상적 cohomology가 일치한다. 두 cohomology의 차이는 오직 비콤팩트 공간에서 나타난다. 또한 고유 받음은 통상적 받음과 마찬가지로 합성에 대해 함자적으로 행동한다.

::: 명제 5
Compactifiable map $$f: X \to Y$$, $$g: Y \to Z$$에 대해 합성 $$gf$$도 compactifiable하며 자연스러운 동형
$$R(gf)_! \cong Rg_! \circ Rf_!$$
이 성립한다.
:::
::: 증명
$$f = p \circ j$$, $$g = q \circ k$$를 compactification이라 하자. $$j_!$$과 $$k_!$$, $$Rp_\ast$$과 $$Rq_\ast$$의 합성을 정리하면 되는데, 핵심은 proper map을 따른 받음과 열린 매장의 extension by zero를 교환하는 base change이다. $$X \to Y \to Z$$의 적절한 콤팩트화를 잡아 $$gf$$의 compactification을 구성하고, [정리 2](#thm2)에 의해 중간 단계의 $$Rp_\ast$$와 $$k_!$$이 교환됨을 쓰면, [§층의 유도 범주와 유도 함자, ⁋정리 10](/ko/math/sheaf_theory/derived_category_of_sheaves#thm10)의 합성 정리와 결합하여 $$R(gf)_! \cong Rg_! Rf_!$$을 얻는다. 자세한 구성은 [KS]의 Proposition 2.5.5와 [SGA4]의 해당 논의를 따른다.
:::

## 예외 역상 함자 $$f^!$$

고유 받음 $$Rf_!$$이 정의되었으니, 그 수반을 찾는 것이 다음 과제이다. $$Lf^\ast$$가 $$Rf_\ast$$의 왼쪽 수반이었던 것과 대칭적으로, $$Rf_!$$의 오른쪽 수반을 구하면 새로운 함자가 얻어진다. 통상적인 함자처럼 어떤 명시적 left exact functor의 right derived functor로 구성되는 것이 아니라, 오직 수반 관계로만 특징지어진다는 점이 이 함자의 특이성이다.

::: 정의 6
Compactifiable map $$f: X \to Y$$에 대해 $$Rf_!: D(\Sh(X)) \to D(\Sh(Y))$$의 오른쪽 수반을 *예외 역상<sub>exceptional inverse image</sub>* 또는 *twisted inverse image*라 부르고 $$f^!: D(\Sh(Y)) \to D(\Sh(X))$$로 적는다. 즉 $$\mathcal{F}^\bullet \in D(\Sh(X))$$, $$\mathcal{G}^\bullet \in D(\Sh(Y))$$에 대해 자연스러운 동형
$$\Hom_{D(\Sh(Y))}(Rf_! \mathcal{F}^\bullet, \mathcal{G}^\bullet) \cong \Hom_{D(\Sh(X))}(\mathcal{F}^\bullet, f^! \mathcal{G}^\bullet)$$
이 성립한다.
:::

$$f^!$$의 존재는 자명하지 않다. 오른쪽 수반이 존재하려면 $$Rf_!$$이 임의의 직합을 보존해야 하는데, $$j_!$$과 $$Rp_\ast$$(유한 cohomological dimension을 가진 proper $$p$$에 대한)가 모두 직합을 보존하므로 $$Rf_!$$도 그러하다. 우리가 가정한 공간들의 derived category는 compactly generated triangulated category이므로, Brown representability에 의해 직합을 보존하는 exact functor는 오른쪽 수반을 가진다. 따라서 $$f^!$$이 존재한다. 유계 derived category에 한정할 때에는 Kashiwara와 Schapira가 $$Rf_!$$의 유한 cohomological amplitude를 이용해 명시적 kernel로 $$f^!$$을 구성하였으며 ([KS], §3.1), 추상적 형식의 차원에서는 Scholze의 정리가 같은 결과를 준다 ([Sch]). 어느 구성에서나 $$f^!$$은 [정의 6](#def6)의 adjunction으로 유일하게 결정된다.

$$f^!$$은 일반적으로 $$f^{-1}$$과 전혀 다른 함자이다. 그러나 $$f$$가 적당히 매끄러운 경우, 두 함자는 받침 차원만큼의 shift와 orientation에 의한 비틀림을 빼면 일치한다. 이것이 Poincaré–Verdier duality의 국소적 형태이다.

::: 정리 7 (매끄러운 경우)
$$f: X \to Y$$가 fiber가 $$d$$차원 topological manifold인 topological submersion이라 하자. 그럼 rank $$1$$인 $$\mathbb{Z}$$-local system $$\operatorname{or}_{X/Y}$$ (상대 orientation sheaf)가 존재하여 임의의 $$\mathcal{G}^\bullet \in D(\Sh(Y))$$에 대해 자연스러운 동형
$$f^! \mathcal{G}^\bullet \cong f^{-1}\mathcal{G}^\bullet \otimes \operatorname{or}_{X/Y}[d]$$
이 성립한다. 특히 $$f$$의 fiber가 orientable하게 일관되게 방향지어지면 $$\operatorname{or}_{X/Y} \cong \mathbb{Z}_X$$이고 $$f^! \mathcal{G}^\bullet \cong f^{-1}\mathcal{G}^\bullet[d]$$이다.
:::
::: 증명
문제는 국소적이므로 $$Y$$ 위에서 $$f$$가 사영 $$\mathbb{R}^d \times Y \to Y$$인 경우로 환원되고, 다시 $$Y = \{\ast\}$$, 즉 $$a: \mathbb{R}^d \to \{\ast\}$$의 경우로 환원된다. 이때 $$a^! \mathbb{Z}$$는 정의상 $$Ra_!$$의 오른쪽 수반이 상수 sheaf에 주는 값이며, $$Ra_! \mathbb{Z}_{\mathbb{R}^d} = R\Gamma_c(\mathbb{R}^d, \mathbb{Z})$$가 차수 $$d$$에 집중되어 $$\mathbb{Z}[-d]$$임을 ([예시 12](#ex12)에서 직접 계산한다) 이용하면, adjunction에 의해 $$a^! \mathbb{Z} \cong \mathbb{Z}[d]$$를 얻는다. $$\mathbb{R}^d$$는 표준적으로 방향지어지므로 orientation 비틀림이 자명하다. 일반적인 manifold fiber에서는 국소 chart를 이어 붙일 때 방향의 부호가 rank $$1$$ local system $$\operatorname{or}_{X/Y}$$로 누적되며, 이를 통해 위의 국소 동형이 대역적 동형으로 정돈된다. 자세한 논증은 [KS]의 Proposition 3.3.2를 따른다.
:::

$$Y = \{\ast\}$$이고 $$X$$가 $$d$$차원 manifold인 특수한 경우, $$\omega_X := a_X^! \mathbb{Z} \cong \operatorname{or}_X[d]$$를 $$X$$의 *dualizing complex*라 부른다. $$X$$가 orientable하면 $$\omega_X \cong \mathbb{Z}_X[d]$$이며, 이 동형이 곧 manifold의 Poincaré duality를 sheaf 차원에서 진술하는 형태이다. 일반적인 (manifold가 아닐 수 있는) 공간에 대해서도 $$\omega_X = a_X^! \mathbb{Z}$$가 정의되어 dualizing complex의 역할을 하며, 이를 이용한 $$R\Hom(-, \omega_X)$$ 형태의 duality가 Verdier duality이다.

복소 다양체의 경우를 별도로 언급할 필요가 있다. $$f$$가 복소 상대 차원 $$m$$인 정칙 submersion이면 실 차원으로는 $$d = 2m$$이고, 복소 다양체는 표준적으로 방향지어지므로 $$\operatorname{or}_{X/Y} \cong \mathbb{Z}_X$$이며 $$f^! \mathcal{G}^\bullet \cong f^{-1}\mathcal{G}^\bullet[2m]$$이 된다. 차수 이동이 복소 차원의 두 배인 것은 이 글에서 다루는 cohomology가 실 위상 cohomology이기 때문이다.

## 여섯 함자 형식

이제 여섯 함자가 모두 갖추어졌다. Continuous map $$f: X \to Y$$에 대한 네 개의 함자 $$Lf^\ast = f^{-1}$$, $$Rf_\ast$$, $$Rf_!$$, $$f^!$$과, 각 공간 $$X$$ 위에서 내부적으로 정의되는 두 개의 함자 $$\otimes^L$$, $$R\Hom$$이 그것이다. 이들 사이의 가장 기본적인 관계는 두 쌍의 adjunction이다. 첫째 쌍 $$(Lf^\ast, Rf_\ast)$$은 [§층의 유도 범주와 유도 함자, ⁋정리 9](/ko/math/sheaf_theory/derived_category_of_sheaves#thm9)에서 이미 확립하였고, 둘째 쌍 $$(Rf_!, f^!)$$은 [정의 6](#def6)에서 정의에 의해 성립한다. 각 공간 위의 내부 adjunction $$(- \otimes^L \mathcal{G}, R\Hom(\mathcal{G}, -))$$은 [§층의 유도 범주와 유도 함자, ⁋명제 8](/ko/math/sheaf_theory/derived_category_of_sheaves#prop8)의 derived tensor-hom adjunction이다.

여섯 함자 형식의 위력은 이 함자들이 서로 다른 공간 사이를 오갈 때 호환되는 방식, 즉 base change와 projection formula에서 드러난다. 먼저 고유 받음이 임의의 base change와 교환한다는 것을 본다. 이것이 [정리 2](#thm2)를 비proper map까지 확장한 형태이며, $$Rf_!$$을 도입한 가장 큰 보상이다.

::: 정리 8 (고유 받음의 base change)
[정리 2](#thm2)와 같은 cartesian square $$X' = X \times_Y Y'$$가 사영 $$g': X' \to X$$, $$f': X' \to Y'$$와 함께 주어졌다 하자. $$f$$가 compactifiable이면 $$f'$$도 그러하며, 임의의 연속함수 $$g$$에 대해 자연스러운 동형
$$g^{-1} Rf_! \cong Rf'_! (g')^{-1}$$
이 성립한다. 동치로, $$\mathcal{F}^\bullet \in D(\Sh(X))$$의 고유 받음의 stalk는 각 $$y \in Y$$에서 fiber 위의 콤팩트 받침 cohomology
$$(Rf_! \mathcal{F}^\bullet)_y \cong R\Gamma_c(f^{-1}(y), \mathcal{F}^\bullet\vert_{f^{-1}(y)})$$
로 주어진다.
:::
::: 증명
$$f = p \circ j$$를 compactification이라 하자. Base change로 얻은 $$f' = p' \circ j'$$도 compactification이 되며, 여기서 $$j': X' \hookrightarrow \overline{X}'= \overline{X} \times_Y Y'$$, $$p': \overline{X}' \to Y'$$이다. 두 단계로 나누어 본다. 열린 매장의 extension by zero는 base change와 교환한다. 즉 cartesian square에서 $$(g')^{-1} j_! \cong j'_! (g'\vert_{X'})^{-1}$$인데, 이는 양변이 $$X'$$ 위에서 같은 sheaf이고 그 보충집합 위에서 모두 stalk $$0$$이므로 stalk 비교로 확인된다. 한편 proper $$p$$에 대한 base change는 [정리 2](#thm2)이다. [정리 2](#thm2)는 $$D^+(\Sh(X))$$에서 진술되었으나, 서두에서 가정한 유한 cohomological dimension에 의해 $$Rp_\ast$$가 유한 cohomological amplitude를 가지므로 그 base change 동형은 절단 논증을 통해 임의의 $$\mathcal{F}^\bullet \in D(\Sh(X))$$로 확장되고, 따라서 아래의 합성도 $$D(\Sh(X))$$ 전체에서 성립한다. 두 교환을 합성하면
$$g^{-1} Rf_! = g^{-1} Rp_\ast j_! \cong Rp'_\ast (g'')^{-1} j_! \cong Rp'_\ast j'_! (g')^{-1} = Rf'_! (g')^{-1}$$
을 얻는다. 여기서 $$g''$$은 $$\overline{X}' \to \overline{X}$$이다. Stalk 공식은 $$Y' = \{y\}$$로 둔 특수한 경우이며, 이때 $$Rf'_!$$은 fiber $$f^{-1}(y)$$의 구조 사상 $$a: f^{-1}(y) \to \{y\}$$에 대한 $$Ra_! = R\Gamma_c(f^{-1}(y), -)$$이다.
:::

stalk 공식 $$(Rf_! \mathcal{F})_y \cong R\Gamma_c(f^{-1}(y), \mathcal{F}\vert)$$은 고유 받음의 본질을 가장 직접적으로 드러낸다. 통상적 받음의 stalk가 작은 근방 위의 cohomology의 colimit이었던 데 반해, 고유 받음의 stalk는 fiber 위의 콤팩트 받침 cohomology 그 자체이며 근방으로 새어 나가는 정보가 없다. Base change 동형은 이 fiber별 묘사가 fiber product 아래에서 fiber가 보존된다는 위상적 사실의 직접적 귀결일 뿐이다. 이 점에서 $$Rf_!$$은 $$Rf_\ast$$보다 기하학적으로 다루기 쉽다.

다음으로 고유 받음과 tensor product 사이의 호환을 진술하는 projection formula를 본다. 이는 $$Rf_!$$이 $$Y$$ 위의 대상에 의한 tensor를 "통과시킨다"는 것으로, $$Rf_!$$이 $$D(\Sh(Y))$$-가군 함자임을 표현한다.

::: 정리 9 (projection formula)
Compactifiable map $$f: X \to Y$$와 $$\mathcal{F}^\bullet \in D(\Sh(X))$$, $$\mathcal{G}^\bullet \in D(\Sh(Y))$$에 대해 자연스러운 동형
$$Rf_!(\mathcal{F}^\bullet \otimes^L f^{-1}\mathcal{G}^\bullet) \cong Rf_! \mathcal{F}^\bullet \otimes^L \mathcal{G}^\bullet$$
이 성립한다.
:::
::: 증명
양변에 [정리 8](#thm8)의 stalk 공식을 적용하여 각 $$y \in Y$$에서 비교한다. 좌변의 stalk는
$$\big(Rf_!(\mathcal{F} \otimes^L f^{-1}\mathcal{G})\big)_y \cong R\Gamma_c\big(f^{-1}(y), (\mathcal{F} \otimes^L f^{-1}\mathcal{G})\vert_{f^{-1}(y)}\big)$$
인데, $$f^{-1}\mathcal{G}$$를 fiber로 제한하면 상수 계열, 즉 $$\mathcal{G}_y$$로 만들어진 상수 sheaf의 당김이 되므로 이는 $$R\Gamma_c(f^{-1}(y), \mathcal{F}\vert) \otimes^L \mathcal{G}_y$$와 동형이다. 여기서 콤팩트 받침 cohomology가 고정된 계수 complex $$\mathcal{G}_y$$에 대한 tensor를 통과시킨다는 사실을 썼다. 우변의 stalk는 $$\otimes^L$$이 stalk와 교환하므로 $$(Rf_! \mathcal{F})_y \otimes^L \mathcal{G}_y \cong R\Gamma_c(f^{-1}(y), \mathcal{F}\vert) \otimes^L \mathcal{G}_y$$이다. 두 stalk가 자연스럽게 일치하므로 [§층의 유도 범주와 유도 함자, ⁋명제 1](/ko/math/sheaf_theory/derived_category_of_sheaves#prop1)의 stalk 판정에 의해 동형이 성립한다. 자세히는 [KS]의 Proposition 2.5.13을 따른다.
:::

projection formula는 $$f^!$$에 대한 형태로도 옮겨 쓸 수 있다. 두 adjunction $$(Rf_!, f^!)$$과 tensor-hom adjunction을 결합하면 $$R\Hom(Rf_! \mathcal{F}, \mathcal{G}) \cong Rf_\ast R\Hom(\mathcal{F}, f^! \mathcal{G})$$이라는 대역적 Verdier duality가 나오는데, 이는 projection formula와 base change, 그리고 두 adjunction이 함께 작동하는 형식의 정점이다. 그 일반론은 이 글의 범위를 넘으므로 [KS]의 §3.1을 참조한다.

## 열린-닫힌 분해와 recollement

여섯 함자 형식이 가장 구체적으로 드러나는 상황은 공간을 열린 부분과 닫힌 부분으로 쪼갤 때이다. $$X$$의 닫힌 부분공간 $$i: Z \hookrightarrow X$$와 그 보충집합인 열린 부분공간 $$j: U = X \setminus Z \hookrightarrow X$$를 생각하자. 닫힌 매장 $$i$$는 proper이므로 [따름정리 4](#cor4)에 의해 $$i_! = i_\ast$$이고, 열린 매장 $$j$$에 대해서는 extension by zero $$j_!$$과 통상적 받음 $$Rj_\ast$$이 모두 있다. 이 사상들이 만들어 내는 함자들은 두 개의 distinguished triangle로 엮인다.

::: 정리 10 (recollement triangle)
위의 열린-닫힌 분해에서 임의의 $$\mathcal{F}^\bullet \in D(\Sh(X))$$에 대해 다음 두 distinguished triangle이 $$D(\Sh(X))$$ 안에서 자연스럽게 존재한다.
$$j_! j^{-1} \mathcal{F}^\bullet \longrightarrow \mathcal{F}^\bullet \longrightarrow i_\ast i^{-1} \mathcal{F}^\bullet \xrightarrow{+1}$$
$$i_\ast i^! \mathcal{F}^\bullet \longrightarrow \mathcal{F}^\bullet \longrightarrow Rj_\ast j^{-1} \mathcal{F}^\bullet \xrightarrow{+1}$$
:::
::: 증명
첫째 triangle은 sheaf의 short exact sequence
$$0 \longrightarrow j_! j^{-1} \mathcal{F} \longrightarrow \mathcal{F} \longrightarrow i_\ast i^{-1} \mathcal{F} \longrightarrow 0$$
에서 온다. 이 sequence의 exactness는 stalk에서 확인한다 ([§층의 유도 범주와 유도 함자, ⁋명제 1](/ko/math/sheaf_theory/derived_category_of_sheaves#prop1)). 점 $$x \in U$$에서는 $$(j_! j^{-1}\mathcal{F})_x = \mathcal{F}_x$$이고 $$(i_\ast i^{-1}\mathcal{F})_x = 0$$이므로 sequence가 $$0 \to \mathcal{F}_x \to \mathcal{F}_x \to 0 \to 0$$이 되어 exact이고, 점 $$x \in Z$$에서는 extension by zero의 정의에 의해 $$(j_! j^{-1}\mathcal{F})_x = 0$$이고 $$(i_\ast i^{-1}\mathcal{F})_x = \mathcal{F}_x$$이므로 $$0 \to 0 \to \mathcal{F}_x \to \mathcal{F}_x \to 0$$이 되어 exact이다. Abelian category의 short exact sequence는 derived category에서 distinguished triangle을 낳으므로 첫째 triangle이 성립한다.

둘째 triangle은 첫째 것과 쌍대이다. $$i^! \mathcal{F}$$는 $$i_\ast$$의 오른쪽 수반으로, 받침이 $$Z$$ 안에 놓인 단면을 추리는 함자 $$\Gamma_Z$$의 derived functor로 해석된다. 미유도 차원에서 left exact sequence
$$0 \longrightarrow \Gamma_Z \mathcal{F} \longrightarrow \mathcal{F} \longrightarrow j_\ast j^{-1}\mathcal{F}$$
가 있고, 이를 $$\mathcal{F}$$의 injective resolution 위에서 derived하면 마지막 항이 $$Rj_\ast j^{-1}\mathcal{F}$$로, 첫 항이 $$R\Gamma_Z \mathcal{F} = i_\ast i^! \mathcal{F}$$로 올라가 둘째 triangle을 얻는다. 자세한 논증은 [KS]의 §2.3 및 [Dim]의 §2.3을 따른다.
:::

두 triangle은 같은 분해를 서로 다른 방향에서 본 것이다. 첫째 triangle은 $$\mathcal{F}$$를 "열린 쪽에서 $$0$$으로 연장한 부분"과 "닫힌 쪽으로 제한한 부분"으로 쪼개고, 둘째 triangle은 "닫힌 쪽에 받침을 가진 부분"과 "열린 쪽으로 제한한 뒤 밀어낸 부분"으로 쪼갠다. 첫째 triangle에 $$R\Gamma(X, -)$$를 적용하면 콤팩트 받침 cohomology의 long exact sequence가 나오는데, 이를 활용하려면 먼저 콤팩트 받침 cohomology를 정식으로 정의해야 한다.

::: 정의 11
위상공간 $$X$$의 구조 사상 $$a_X: X \to \{\ast\}$$에 대해, $$\mathcal{F}^\bullet \in D(\Sh(X))$$의 *compactly supported cohomology<sub>콤팩트 받침 코호몰로지</sub>*를
$$R\Gamma_c(X, \mathcal{F}^\bullet) := R(a_X)_! \mathcal{F}^\bullet$$
로 정의하고, 그 cohomology를 $$H^k_c(X, \mathcal{F}^\bullet) := H^k(R\Gamma_c(X, \mathcal{F}^\bullet))$$로 적는다.
:::

[정의 1](#def1) 직후에 보았듯이 $$a_X$$의 compactification은 one-point compactification $$j: X \hookrightarrow \overline{X} = X \cup \{\infty\}$$으로 주어지므로, 콤팩트 받침 cohomology는
$$R\Gamma_c(X, \mathcal{F}) = R\Gamma(\overline{X}, j_! \mathcal{F})$$
로 계산된다. 즉 $$\mathcal{F}$$를 무한대 점에서 $$0$$이 되도록 연장한 뒤 compact 공간 $$\overline{X}$$ 위의 통상적 cohomology를 취하는 것이다. $$X$$가 이미 compact이면 [따름정리 4](#cor4)에 의해 $$R\Gamma_c = R\Gamma$$이고, 비콤팩트 공간에서 무한대 점의 추가가 두 cohomology의 차이를 만든다. 첫째 recollement triangle에서 $$Z = \{\infty\}$$, $$U = X$$로 두고 $$\overline{X}$$ 위에서 $$R\Gamma(\overline{X}, -)$$를 적용하면
$$\cdots \to H^k_c(X, \mathcal{F}) \to H^k(\overline{X}, \overline{\mathcal{F}}) \to H^k(\{\infty\}, \mathcal{F}_\infty) \to H^{k+1}_c(X, \mathcal{F}) \to \cdots$$
형태의 long exact sequence를 얻는데, 다음 절에서 이를 직접 활용한다.

## 콤팩트 받침 코호몰로지의 계산

지금까지의 형식을 구체적 계산으로 점검한다. 비콤팩트 공간 위의 상수 sheaf에 대해 $$R\Gamma$$와 $$R\Gamma_c$$가 어떻게 갈라지는지, 그리고 콤팩트화를 통해 $$R\Gamma_c$$가 어떻게 계산되는지를 보인다. 모든 계수는 $$\mathbb{Z}$$로 한다.

::: 예시 12
열린 구간 $$U = (0, 1)$$, 아핀 직선 $$\mathbb{A}^1 = \mathbb{C}$$, 사영 직선 $$\mathbb{P}^1$$ 위의 상수 sheaf의 콤팩트 받침 cohomology를 계산하고, 통상적 cohomology와 대조한다. 일반화로 $$\mathbb{R}^n$$에 대한 $$R\Gamma_c(\mathbb{R}^n, \mathbb{Z}) \cong \mathbb{Z}[-n]$$을 얻는다.
:::

먼저 열린 구간 $$U = (0, 1)$$을 다룬다. 통상적 cohomology는 $$U$$가 가축이므로 $$H^0(U, \mathbb{Z}) = \mathbb{Z}$$, $$H^k(U, \mathbb{Z}) = 0$$ ($$k \geq 1$$)으로 차수 $$0$$에 집중된다. 콤팩트 받침 cohomology를 계산하기 위해 콤팩트화 $$j: (0,1) \hookrightarrow [0,1]$$을 택하자. 이는 열린 매장이고 닫힌 보충집합은 두 끝점 $$\partial = \{0, 1\}$$, 곧 닫힌 매장 $$i: \{0,1\} \hookrightarrow [0,1]$$이다. 상수 sheaf $$\mathbb{Z}_{[0,1]}$$에 대한 첫째 recollement triangle ([정리 10](#thm10))
$$j_! \mathbb{Z}_U \longrightarrow \mathbb{Z}_{[0,1]} \longrightarrow i_\ast \mathbb{Z}_\partial \xrightarrow{+1}$$
에 $$R\Gamma([0,1], -)$$을 적용한다. $$[0,1]$$이 가축이므로 $$R\Gamma([0,1], \mathbb{Z}) = \mathbb{Z}$$ (차수 $$0$$)이고, $$R\Gamma([0,1], i_\ast \mathbb{Z}_\partial) = R\Gamma(\partial, \mathbb{Z}) = \mathbb{Z}^2$$ (차수 $$0$$)이다. 또 $$R\Gamma([0,1], j_! \mathbb{Z}_U) = R\Gamma_c(U, \mathbb{Z})$$이다. 따라서 long exact sequence는
$$0 \to H^0_c(U) \to H^0([0,1]) = \mathbb{Z} \xrightarrow{\rho} H^0(\partial) = \mathbb{Z}^2 \to H^1_c(U) \to H^1([0,1]) = 0$$
이 된다. 제한 사상 $$\rho$$는 대역적 상수 $$a$$를 두 끝점에서의 값 $$(a, a)$$로 보내는 대각 매장이므로 단사이고, 그 cokernel은 $$\mathbb{Z}^2 / \{(a,a)\} \cong \mathbb{Z}$$이다. 그러므로
$$H^0_c(U, \mathbb{Z}) = \ker \rho = 0, \qquad H^1_c(U, \mathbb{Z}) = \operatorname{coker} \rho \cong \mathbb{Z}$$
이고, $$R\Gamma_c((0,1), \mathbb{Z}) \cong \mathbb{Z}[-1]$$이 차수 $$1$$에 집중된다. 이는 통상적 cohomology가 차수 $$0$$에 있던 것과 정반대이며, $$1$$차원 (방향지어진) 다양체 $$U$$에 대한 Poincaré duality $$H^k_c(U) \cong H^{1-k}(U)^\vee$$를 그대로 구현한다.

이 계산은 곧바로 일반화된다. $$\mathbb{R} \cong (0,1)$$이므로 $$R\Gamma_c(\mathbb{R}, \mathbb{Z}) \cong \mathbb{Z}[-1]$$이고, Künneth 공식에 의해 $$R\Gamma_c$$가 곱에 대해 tensor로 행동하므로
$$R\Gamma_c(\mathbb{R}^n, \mathbb{Z}) \cong R\Gamma_c(\mathbb{R}, \mathbb{Z})^{\otimes n} \cong \mathbb{Z}[-n]$$
이 차수 $$n$$에 집중된다. 이 사실이 바로 [정리 7](#thm7)의 증명에서 $$a^! \mathbb{Z} \cong \mathbb{Z}[d]$$를 이끌어 낸 국소 계산이며, manifold의 dualizing complex가 $$\mathbb{Z}_X[d]$$인 근원이다.

이제 복소 직선들을 다룬다. 아핀 직선 $$\mathbb{A}^1 = \mathbb{C} \cong \mathbb{R}^2$$에 대해서는 위의 결과로부터 곧바로
$$R\Gamma_c(\mathbb{A}^1, \mathbb{Z}) \cong \mathbb{Z}[-2], \qquad H^0_c = H^1_c = 0, \quad H^2_c \cong \mathbb{Z}$$
이다. 한편 사영 직선 $$\mathbb{P}^1 \cong S^2$$는 compact이므로 [따름정리 4](#cor4)에 의해 $$R\Gamma_c(\mathbb{P}^1, \mathbb{Z}) = R\Gamma(\mathbb{P}^1, \mathbb{Z})$$이고, 이는 $$2$$차원 구면의 cohomology
$$H^0(\mathbb{P}^1, \mathbb{Z}) = \mathbb{Z}, \qquad H^1(\mathbb{P}^1, \mathbb{Z}) = 0, \qquad H^2(\mathbb{P}^1, \mathbb{Z}) = \mathbb{Z}$$
이다. 두 결과는 콤팩트화 $$\mathbb{P}^1 = \mathbb{A}^1 \cup \{\infty\}$$을 통한 recollement triangle로 일관되게 연결된다. 열린 매장 $$j: \mathbb{A}^1 \hookrightarrow \mathbb{P}^1$$과 닫힌 매장 $$i: \{\infty\} \hookrightarrow \mathbb{P}^1$$에 대한 triangle $$j_! \mathbb{Z}_{\mathbb{A}^1} \to \mathbb{Z}_{\mathbb{P}^1} \to i_\ast \mathbb{Z}_\infty \xrightarrow{+1}$$에 $$R\Gamma(\mathbb{P}^1, -)$$을 적용하면 long exact sequence
$$0 \to H^0_c(\mathbb{A}^1) \to H^0(\mathbb{P}^1) = \mathbb{Z} \xrightarrow{\rho} H^0(\{\infty\}) = \mathbb{Z} \to H^1_c(\mathbb{A}^1) \to H^1(\mathbb{P}^1) = 0$$
$$0 \to H^2_c(\mathbb{A}^1) \to H^2(\mathbb{P}^1) = \mathbb{Z} \to H^2(\{\infty\}) = 0$$
을 얻는다. 첫 줄의 제한 사상 $$\rho: \mathbb{Z} \to \mathbb{Z}$$는 대역적 상수를 한 점 $$\infty$$에서의 값으로 보내는 동형이므로 $$H^0_c(\mathbb{A}^1) = \ker \rho = 0$$, $$H^1_c(\mathbb{A}^1) = \operatorname{coker} \rho = 0$$이고, 둘째 줄에서 $$H^2_c(\mathbb{A}^1) \cong H^2(\mathbb{P}^1) = \mathbb{Z}$$이다. 이는 앞서 $$\mathbb{R}^2$$로부터 얻은 $$R\Gamma_c(\mathbb{A}^1, \mathbb{Z}) \cong \mathbb{Z}[-2]$$와 정확히 일치한다.

이 대조가 고유 받음의 역할을 선명하게 보여 준다. Compact한 $$\mathbb{P}^1$$에서는 $$Rf_! = Rf_\ast$$이어서 두 cohomology가 같지만, 비콤팩트한 $$\mathbb{A}^1$$에서는 $$H^0$$이 통상적 cohomology에서는 $$\mathbb{Z}$$였다가 콤팩트 받침 cohomology에서는 $$0$$으로 사라지고 대신 최고 차수 $$H^2_c$$가 $$\mathbb{Z}$$로 살아난다. 무한대 점을 추가하는 콤팩트화가 정확히 차수 $$0$$의 대역적 단면을 제거하고 최고 차수의 class를 생성하며, 이 메커니즘이 $$Rf_!$$과 그 수반 $$f^!$$을 통해 비콤팩트 공간의 Poincaré–Verdier duality를 떠받친다.

---

**참고문헌**

**[KS]** M. Kashiwara, P. Schapira, *Sheaves on manifolds*, Springer, 1990.

**[Dim]** A. Dimca, *Sheaves in topology*, Springer, 2004.

**[SGA4]** M. Artin, A. Grothendieck, J.-L. Verdier, *Théorie des topos et cohomologie étale des schémas (SGA 4)*, Springer, 1972–1973.

**[Sch]** P. Scholze, *Six-functor formalisms*, lecture notes.
