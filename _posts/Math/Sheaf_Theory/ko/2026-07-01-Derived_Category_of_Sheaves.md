---
title: "층의 유도 범주와 유도 함자"
description: "공간 위 층의 abelian 범주가 충분한 injective를 가짐을 확인하고, 그 유도 범주에서 Rf_*·Lf^*·⊗^L·RHom을 정의하여 층 코호몰로지와 Leray 스펙트럼 열을 유도함자의 언어로 통합한다."
excerpt: "D(Sh(X)), the derived functors Rf_*, Lf^*, ⊗^L, RHom, and their adjunctions"

categories: [Math / Sheaf Theory]
permalink: /ko/math/sheaf_theory/derived_category_of_sheaves
sidebar: 
    nav: "sheaf_theory-ko"

date: 2026-07-01
last_modified_at: 2026-07-01
weight: 1

published: false

---

우리는 [\[대수다양체\] §층 코호몰로지, ⁋정의 1](/ko/math/algebraic_varieties/sheaf_cohomology#def1)에서 sheaf cohomology $$H^i(X, \mathcal{F})$$를 global section functor $$\Gamma(X, -)$$의 right derived functor로 정의하였다. 같은 글의 후반부에서 우리는 continuous map $$f: X \to Y$$를 따라 left exact functor $$f_\ast: \Sh(X) \to \Sh(Y)$$의 right derived functor인 higher direct image $$R^q f_\ast$$를 도입하였고, 이들을 묶는 Leray spectral sequence $$E_2^{p,q} = H^p(Y, R^q f_\ast \mathcal{F}) \Rightarrow H^{p+q}(X, \mathcal{F})$$를 살펴보았다. ([\[대수다양체\] §층 코호몰로지, ⁋명제 19](/ko/math/algebraic_varieties/sheaf_cohomology#prop19))

이러한 결과들은 각각 개별적인 $$R^q$$들의 모임으로 진술되지만, 실제 사용에서는 $$f_\ast$$, $$f^{-1}$$, $$\otimes$$, $$\mathcal{H}om$$ 등 여러 functor를 합성하고 그들 사이의 관계를 다루어야 한다. 개별 cohomology $$R^q$$의 차원에서는 이러한 합성이 spectral sequence를 거쳐야만 기술되며, adjunction 같은 구조적 관계도 직접적으로 드러나지 않는다. [\[호몰로지 대수학\] §유도카테고리](/ko/math/homological_algebra/derived_categories)에서 우리는 abelian category $$\mathcal{A}$$에 대해 derived category $$D(\mathcal{A})$$를 구성하고, left/right derived functor $$LF$$, $$RF$$를 $$K$$-projective/$$K$$-injective resolution 위에서 단일한 functor로 정의하였다. 이 글에서 우리는 그 추상적 기계를 $$\mathcal{A} = \Sh(X)$$의 경우에 적용하여, sheaf cohomology와 higher direct image를 $$R\Gamma$$, $$Rf_\ast$$라는 단일한 유도 함자로 통합하고, $$Lf^\ast$$, $$\otimes^L$$, $$R\Hom$$을 함께 정의한다. 그 후 derived adjunction과 Grothendieck의 합성 함자 정리를 통해 Leray spectral sequence가 단 하나의 동형 $$R(gf)_\ast \cong Rg_\ast Rf_\ast$$로부터 따라 나옴을 본다.

추상적 derived category의 구성 자체, 즉 $$D(\mathcal{A})$$, $$K$$-injective/$$K$$-projective resolution, $$RF$$/$$LF$$의 정의, triangulated 구조, 그리고 derived adjunction은 [\[호몰로지 대수학\] §유도카테고리](/ko/math/homological_algebra/derived_categories)에서 이미 다루었으므로 여기서 다시 세우지 않고 인용한다. 우리의 과제는 $$\Sh(X)$$가 그 기계를 가동하기 위한 전제 조건, 즉 abelian category이며 충분한 injective를 가진다는 사실을 확인하고, 그 위에서 구체적인 sheaf 함자들의 유도 버전을 정리하는 것이다.

## $$\Sh(X)$$의 abelian 구조

이 글에서 $$X$$는 위상공간이고, $$\Sh(X) = \Sh(X, \Ab)$$는 $$X$$ 위의 abelian group들의 sheaf로 이루어진 category를 뜻한다. 더 일반적으로 $$\mathcal{O}_X$$가 $$X$$ 위의 ring들의 sheaf일 때 ([\[위상수학\] §준층, ⁋예시 14](/ko/math/topology/presheaves#ex14)), $$\mathcal{O}_X$$-module들의 category를 $$\operatorname{Mod}(\mathcal{O}_X)$$로 적는다. $$\mathcal{O}_X = \mathbb{Z}_X$$, 즉 $$\mathbb{Z}$$를 stalk로 갖는 constant sheaf로 두면 $$\operatorname{Mod}(\mathbb{Z}_X) = \Sh(X, \Ab)$$이므로, abelian group의 sheaf는 ringed space $$(X, \mathbb{Z}_X)$$ 위의 module의 특수한 경우이다.

derived category를 세우기 위해서는 우선 작업 대상이 abelian category여야 한다. Sheaf morphism의 kernel은 presheaf 차원의 kernel이 곧바로 sheaf가 되어 별다른 조작 없이 정의되지만 ([\[위상수학\] §준층, ⁋정의 16](/ko/math/topology/presheaves#def16)), image와 cokernel은 presheaf 단계에서 sheaf 조건을 만족하지 않아 sheafification을 거쳐야 한다는 점이 핵심이다. ([\[위상수학\] §층, ⁋정의 5](/ko/math/topology/sheaves#def5))

::: 명제 1
$$\Sh(X, \Ab)$$와 $$\operatorname{Mod}(\mathcal{O}_X)$$는 abelian category이다. 이때 sheaf morphism $$\phi: \mathcal{F} \to \mathcal{G}$$의 kernel, cokernel, image는 stalk 차원에서
$$(\ker \phi)_x = \ker(\phi_x), \qquad (\operatorname{coker} \phi)_x = \operatorname{coker}(\phi_x), \qquad (\im \phi)_x = \im(\phi_x)$$
로 주어진다.
:::
::: 증명
Sheaf morphism $$\phi$$의 presheaf 차원 kernel $$U \mapsto \ker(\phi(U))$$는 그 자체로 sheaf이며, 따라서 sheaf morphism의 kernel은 이 presheaf kernel로 정의한다 ([\[위상수학\] §층, ⁋정의 7](/ko/math/topology/sheaves#def7)). 이는 sheaf 공리가 국소적으로 단면을 이어붙이는 조건이기 때문이다. 호환되는 국소 단면 $$s_i \in \ker(\phi(U_i))$$가 주어지면 $$\mathcal{F}$$가 sheaf이므로 이들은 유일한 $$s \in \mathcal{F}(U)$$로 이어붙고, $$\phi(U)(s)$$는 각 $$U_i$$ 위에서 $$\phi(U_i)(s_i) = 0$$으로 제한되므로 $$\mathcal{G}$$의 separatedness에 의해 $$\phi(U)(s) = 0$$, 즉 $$s \in \ker(\phi(U))$$이다. Cokernel과 image는 presheaf 차원의 $$U \mapsto \operatorname{coker}(\phi(U))$$, $$U \mapsto \im(\phi(U))$$를 sheafify하여 정의한다. Sheafification은 stalk를 보존하고 ([\[위상수학\] §층, ⁋정의 5](/ko/math/topology/sheaves#def5) 직후의 universal property로부터 $$(\mathcal{P}^\dagger)_x = \mathcal{P}_x$$) stalk functor $$\mathcal{F} \mapsto \mathcal{F}_x$$는 exact하므로, 위의 stalk 공식이 따라 나온다.

이제 abelian category의 공리를 확인하자. $$\Sh(X)$$는 additive category이고 모든 morphism이 kernel과 cokernel을 가진다. 임의의 monomorphism이 자신의 image의 kernel이고 임의의 epimorphism이 자신의 coimage의 cokernel이라는 조건은 stalk에서 확인하면 되는데, $$\mathbb{Z}$$-module(또는 $$\mathcal{O}_{X,x}$$-module)의 category가 abelian이므로 각 stalk에서 성립하고, sheaf morphism의 동형은 stalk 동형으로 판정되므로 ([\[위상수학\] §층, ⁋명제 4](/ko/math/topology/sheaves#prop4)) sheaf 차원에서도 성립한다. $$\operatorname{Mod}(\mathcal{O}_X)$$의 경우도 동일하다.
:::

명제의 stalk 공식은 sheaf의 short exact sequence를 stalk 차원에서 점검할 수 있게 해 주는, 앞으로 반복적으로 쓰일 도구이다. 특히 sequence $$0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$$이 exact인 것은 각 점 $$x$$에서 $$0 \to \mathcal{F}'_x \to \mathcal{F}_x \to \mathcal{F}''_x \to 0$$이 exact인 것과 동치이다. 한편 global section functor $$\Gamma(X, -)$$가 left exact이지만 일반적으로 right exact가 아니라는 사실이 바로 sheaf cohomology가 비자명해지는 근원이며, 이 글의 모든 유도 함자가 측정하는 대상이다.

## 충분한 injective의 존재

Derived category 위에서 right derived functor $$RF$$를 정의하려면 $$\mathcal{A}$$가 충분한 injective를 가져야 한다 ([\[호몰로지 대수학\] §유도카테고리, ⁋정의 8](/ko/math/homological_algebra/derived_categories#def8)). 즉 모든 대상이 어떤 injective object 안으로 단사적으로 들어가야 한다. Module category에서는 이 사실이 표준적이지만, sheaf의 경우에는 별도의 논증이 필요하다. 다음은 Grothendieck이 Tôhoku 논문에서 정립한 일반 정리의 특수한 경우이다.

::: 정리 2 (Grothendieck)
$$\Sh(X, \Ab)$$와 $$\operatorname{Mod}(\mathcal{O}_X)$$는 충분한 injective를 가진다.
:::
::: 증명
$$\operatorname{Mod}(\mathcal{O}_X)$$에 대해 증명하면 $$\mathcal{O}_X = \mathbb{Z}_X$$의 경우로 $$\Sh(X, \Ab)$$가 따라 나온다. 구체적인 embedding을 구성한다. $$\mathcal{F} \in \operatorname{Mod}(\mathcal{O}_X)$$가 주어졌다 하자. 각 점 $$x \in X$$에서 stalk $$\mathcal{F}_x$$는 $$\mathcal{O}_{X,x}$$-module이고, module category는 충분한 injective를 가지므로 injective $$\mathcal{O}_{X,x}$$-module $$I_x$$와 단사 $$\mathcal{F}_x \hookrightarrow I_x$$를 택할 수 있다.

각 $$x$$에 대해 inclusion $$i_x: \{x\} \hookrightarrow X$$를 따라 skyscraper sheaf $$(i_x)_\ast I_x$$를 만들고 ([\[위상수학\] §준층, ⁋예시 5](/ko/math/topology/presheaves#ex5)), 이들의 곱
$$\mathcal{I} = \prod_{x \in X} (i_x)_\ast I_x$$
를 생각하자. Adjunction $$(i_x^{-1}, (i_x)_\ast)$$에서 $$i_x^{-1} \mathcal{G} = \mathcal{G}_x$$이므로 ([\[위상수학\] §층, ⁋예시 13](/ko/math/topology/sheaves#ex13)), 임의의 $$\mathcal{G}$$에 대해
$$\Hom_{\operatorname{Mod}(\mathcal{O}_X)}(\mathcal{G}, (i_x)_\ast I_x) \cong \Hom_{\mathcal{O}_{X,x}}(\mathcal{G}_x, I_x)$$
가 성립한다. 이 adjunction 동형의 우변에서 right adjoint $$(i_x)_\ast$$는 exact functor $$i_x^{-1}$$의 right adjoint이므로 injective object를 보존하고, $$I_x$$가 injective이므로 $$(i_x)_\ast I_x$$는 injective $$\mathcal{O}_X$$-module이다. Injective object의 곱은 injective이므로 $$\mathcal{I}$$도 injective이다.

마지막으로 단사 $$\mathcal{F} \hookrightarrow \mathcal{I}$$를 구성한다. 각 $$x$$마다 위 adjunction에 의해 합성 $$\mathcal{F}_x \hookrightarrow I_x$$는 sheaf morphism $$\mathcal{F} \to (i_x)_\ast I_x$$에 대응하고, 이들을 모아 $$\mathcal{F} \to \mathcal{I}$$를 얻는다. 이 morphism이 단사임은 stalk를 점 $$y$$에서 보아 확인한다. 곱 $$\mathcal{I} = \prod_x (i_x)_\ast I_x$$에는 $$y$$ 성분으로의 사영 $$\mathcal{I} \to (i_y)_\ast I_y$$가 있고, skyscraper sheaf의 stalk가 $$((i_y)_\ast I_y)_y = I_y$$이므로 이 사영의 stalk를 $$y$$에서 취하면 사상 $$\mathcal{I}_y \to I_y$$를 얻는다. 합성 $$\mathcal{F}_y \to \mathcal{I}_y \to I_y$$는 구성에 의해 처음에 택한 단사 $$\mathcal{F}_y \hookrightarrow I_y$$와 일치하므로 $$\mathcal{F}_y \to \mathcal{I}_y$$ 또한 단사이고, 모든 $$y$$에서 stalk가 단사이므로 [명제 1](#prop1)에 의해 $$\mathcal{F} \to \mathcal{I}$$는 monomorphism이다.
:::

이 정리로부터 $$\Sh(X)$$ 위에서 $$D(\mathcal{A})$$의 모든 추상적 기계를 가동할 수 있게 된다. 특히 bounded below derived category $$D^+(\Sh(X))$$의 임의의 complex는 $$K$$-injective resolution을 가지며 ([\[호몰로지 대수학\] §유도카테고리, ⁋명제 7](/ko/math/homological_algebra/derived_categories#prop7) 직후의 서술), 따라서 임의의 left exact functor의 right derived functor가 정의된다.

::: 따름정리 3
위상공간 $$X$$에 대해 $$D^+(\Sh(X))$$ 위의 right derived functor
$$R\Gamma(X, -): D^+(\Sh(X)) \to D^+(\Ab), \qquad Rf_\ast: D^+(\Sh(X)) \to D^+(\Sh(Y))$$
가 존재한다. 여기서 $$f: X \to Y$$는 continuous map이다. 한 점으로의 사상 $$a_X: X \to \{\ast\}$$에 대해 $$\Sh(\{\ast\}) = \Ab$$이고 $$(a_X)_\ast = \Gamma(X, -)$$이므로, $$R\Gamma(X, -) = R(a_X)_\ast$$이다.
:::
::: 증명
$$\Gamma(X, -)$$와 $$f_\ast$$는 모두 left exact functor이다. $$f_\ast$$의 left exactness는 그것이 exact functor $$f^{-1}$$의 right adjoint이기 때문이고 ([\[위상수학\] §층, ⁋보조정리 11](/ko/math/topology/sheaves#lem11)), $$\Gamma(X, -) = (a_X)_\ast$$는 그 특수한 경우이다. [정리 2](#thm2)에 의해 $$\Sh(X)$$가 충분한 injective를 가지므로, [\[호몰로지 대수학\] §유도카테고리, ⁋정의 8](/ko/math/homological_algebra/derived_categories#def8)의 right derived functor 구성이 그대로 적용된다. $$\{\ast\}$$ 위의 sheaf는 그 유일한 열린집합 $$\{\ast\}$$ 위의 단면, 즉 하나의 abelian group으로 결정되므로 $$\Sh(\{\ast\}) = \Ab$$이고, 정의에 의해 $$(a_X)_\ast \mathcal{F} = \mathcal{F}(X) = \Gamma(X, \mathcal{F})$$이다.
:::

[\[호몰로지 대수학\] §유도카테고리, ⁋정의 8](/ko/math/homological_algebra/derived_categories#def8) 직후에서 보았듯이, 대상 $$\mathcal{F} \in \Sh(X)$$를 $$\mathcal{F}[0] \in D^+(\Sh(X))$$로 볼 때 cohomology를 취하면 고전적인 유도 함자가 복원된다. 즉
$$H^i(R\Gamma(X, \mathcal{F})) = H^i(X, \mathcal{F}), \qquad H^q(Rf_\ast \mathcal{F}) = R^q f_\ast \mathcal{F}$$
가 성립하며, 우변은 각각 [\[대수다양체\] §층 코호몰로지, ⁋정의 1](/ko/math/algebraic_varieties/sheaf_cohomology#def1)의 sheaf cohomology와 그 글 후반부의 higher direct image이다. 이로써 $$Rf_\ast \mathcal{F}$$는 모든 $$R^q f_\ast \mathcal{F}$$를 한 complex의 cohomology로 묶어 담는 단일한 대상이 된다.

## Acyclic 분해를 통한 계산

$$K$$-injective resolution은 존재가 보장되지만 명시적으로 다루기 어렵다. 실제 계산에서는 더 다루기 쉬운 acyclic resolution을 쓴다. [\[대수다양체\] §층 코호몰로지, ⁋명제 16](/ko/math/algebraic_varieties/sheaf_cohomology#prop16)에서 flasque sheaf가 $$\Gamma(X, -)$$-acyclic임을 보았고, [\[대수다양체\] §층 코호몰로지, ⁋명제 15](/ko/math/algebraic_varieties/sheaf_cohomology#prop15)에서 Godement resolution이 표준적인 flasque resolution을 제공함을 보았다. 다음 명제는 이 acyclic 분해가 derived category 차원에서도 $$Rf_\ast$$를 올바르게 계산함을 확인한다.

::: 명제 4
Continuous map $$f: X \to Y$$와 sheaf $$\mathcal{F} \in \Sh(X)$$가 주어졌다 하자. $$\mathcal{F} \to \mathcal{A}^\bullet$$이 $$f_\ast$$-acyclic sheaf들로 이루어진 resolution, 즉 모든 항 $$\mathcal{A}^k$$가 $$R^q f_\ast \mathcal{A}^k = 0$$ ($$q > 0$$)을 만족하는 resolution이라면, derived category에서
$$Rf_\ast \mathcal{F} \cong f_\ast \mathcal{A}^\bullet$$
이 성립한다. 특히 flasque resolution은 이 조건을 만족한다.
:::
::: 증명
이는 추상적 사실의 적용이다. $$\mathcal{A}^\bullet$$이 $$f_\ast$$-acyclic 항으로 이루어진 complex이면, $$\mathcal{F}$$의 $$K$$-injective resolution $$\mathcal{I}^\bullet$$에 대해 $$f_\ast$$를 적용한 두 complex $$f_\ast \mathcal{A}^\bullet$$과 $$f_\ast \mathcal{I}^\bullet$$이 quasi-isomorphic함을 보이면 된다. Injective sheaf는 flasque이고 ([\[대수다양체\] §층 코호몰로지, ⁋보조정리 9](/ko/math/algebraic_varieties/sheaf_cohomology#lem9)), flasque sheaf는 $$f_\ast$$-acyclic이다. 후자는 다음과 같이 확인된다. 임의의 열린집합 $$V \subset Y$$에 대해 $$(R^q f_\ast \mathcal{F})$$는 presheaf $$V \mapsto H^q(f^{-1}(V), \mathcal{F})$$의 sheafification이며, $$\mathcal{F}$$가 flasque이면 $$\mathcal{F}\vert_{f^{-1}(V)}$$도 flasque이므로 모든 $$q > 0$$에 대해 $$H^q(f^{-1}(V), \mathcal{F}) = 0$$이고 ([\[대수다양체\] §층 코호몰로지, ⁋명제 16](/ko/math/algebraic_varieties/sheaf_cohomology#prop16)), 따라서 $$R^q f_\ast \mathcal{F} = 0$$이다.

두 acyclic resolution이 같은 결과를 준다는 것은 [\[대수다양체\] §층 코호몰로지, ⁋명제 17](/ko/math/algebraic_varieties/sheaf_cohomology#prop17)의 acyclic resolution 정리를 hyper-derived functor 차원으로 끌어올린 것으로, $$f_\ast \mathcal{A}^\bullet$$과 $$f_\ast \mathcal{I}^\bullet$$ 사이의 비교 morphism이 Cartan-Eilenberg resolution을 매개로 quasi-isomorphism이 됨을 보이면 된다. 핵심은 각 항이 $$f_\ast$$-acyclic이라는 사실이며, 자세한 spectral sequence 비교는 [\[대수다양체\] §층 코호몰로지, ⁋정의 18](/ko/math/algebraic_varieties/sheaf_cohomology#def18) 이후의 논증을 따른다.
:::

이 명제는 앞으로의 구체적 계산에서 핵심적이다. $$Rf_\ast \mathcal{F}$$를 구하려면 $$\mathcal{F}$$의 다루기 쉬운 acyclic resolution을 잡고 $$f_\ast$$를 항별로 적용하기만 하면 된다. 가장 표준적인 선택은 Godement resolution이지만, 문제의 기하에 맞는 다른 flasque 혹은 acyclic resolution이 있으면 그것을 쓰는 편이 효율적이다. 글 끝의 예시에서 우리는 torus 위에서 이러한 계산을 직접 수행한다.

## 역상과 유도 당김

Direct image $$f_\ast$$와 달리, inverse image $$f^{-1}: \Sh(Y) \to \Sh(X)$$는 derived 과정을 거칠 필요가 없다. 이는 $$f^{-1}$$이 exact functor이기 때문이다.

::: 명제 5
Continuous map $$f: X \to Y$$에 대해 $$f^{-1}: \Sh(Y) \to \Sh(X)$$는 exact functor이며, 따라서 그것이 유도하는 $$D(\Sh(Y)) \to D(\Sh(X))$$는 derivation 없이 곧바로 정의되고 $$Lf^{-1} = f^{-1} = Rf^{-1}$$이다.
:::
::: 증명
$$f^{-1}$$은 stalk를 보존한다. 정확히는 임의의 sheaf $$\mathcal{G} \in \Sh(Y)$$와 점 $$x \in X$$에 대해 $$(f^{-1}\mathcal{G})_x \cong \mathcal{G}_{f(x)}$$이다. 이는 $$f^{-1}\mathcal{G}$$가 presheaf $$U \mapsto \varinjlim_{V \supseteq f(U)} \mathcal{G}(V)$$의 sheafification으로 정의되는 것 ([\[위상수학\] §층, ⁋정의 10](/ko/math/topology/sheaves#def10) 및 그 구성식)으로부터, stalk를 취하면 $$f(x)$$를 포함하는 열린집합들에 대한 colimit가 되어 $$\mathcal{G}_{f(x)}$$가 되기 때문이다. Stalk functor $$\mathcal{G} \mapsto \mathcal{G}_{f(x)}$$는 exact하므로 ([명제 1](#prop1)의 stalk 판정), $$f^{-1}$$은 short exact sequence를 short exact sequence로 보낸다. Exact functor는 quasi-isomorphism을 보존하므로 $$D(\Sh(Y)) \to D(\Sh(X))$$로 곧바로 내려가며, derived functor의 정의에서 resolution이 불필요해 $$Lf^{-1} = f^{-1} = Rf^{-1}$$이다.
:::

$$\Sh(X, \Ab)$$ 수준에서는 이것으로 충분하지만, ringed space의 경우에는 더 미묘한 점이 있다. $$f: (X, \mathcal{O}_X) \to (Y, \mathcal{O}_Y)$$가 ringed space 사이의 morphism일 때, $$\mathcal{O}_Y$$-module의 당김은 단순한 $$f^{-1}$$이 아니라 $$f^{-1}\mathcal{O}_Y$$-module을 $$\mathcal{O}_X$$-module로 확장하는 단계를 포함한다.

::: 정의 6
Ringed space 사이의 morphism $$f: (X, \mathcal{O}_X) \to (Y, \mathcal{O}_Y)$$가 주어졌다 하자. $$\mathcal{O}_Y$$-module $$\mathcal{G}$$의 *module pullback<sub>가군 당김</sub>* $$f^\ast \mathcal{G}$$를
$$f^\ast \mathcal{G} = \mathcal{O}_X \otimes_{f^{-1}\mathcal{O}_Y} f^{-1}\mathcal{G}$$
로 정의한다. 여기서 morphism의 정의에 포함된 ring sheaf homomorphism $$f^{-1}\mathcal{O}_Y \to \mathcal{O}_X$$를 통해 $$\mathcal{O}_X$$를 $$f^{-1}\mathcal{O}_Y$$-algebra로 본다. 이 $$f^\ast$$의 left derived functor를 *derived pullback* $$Lf^\ast$$라 부른다.
:::

$$f^\ast$$는 right exact functor $$\mathcal{O}_X \otimes_{f^{-1}\mathcal{O}_Y} (-)$$와 exact functor $$f^{-1}$$의 합성이므로 right exact이며, $$(f^\ast, f_\ast)$$는 $$\operatorname{Mod}(\mathcal{O}_Y)$$와 $$\operatorname{Mod}(\mathcal{O}_X)$$ 사이의 adjoint pair를 이룬다. $$Lf^\ast$$를 정의할 때의 미묘함은 $$\operatorname{Mod}(\mathcal{O}_X)$$가 일반적으로 충분한 projective를 갖지 않는다는 데 있다. 그 대신 충분한 flat object를 가지며, derived tensor의 계산에는 flat resolution이면 충분하다. 따라서 $$Lf^\ast$$는 $$f^\ast$$를 $$f^{-1}\mathcal{O}_Y$$-flat한 항으로 이루어진 resolution 위에서 계산하여 정의하고, 유계가 아닌 complex의 경우에는 Spaltenstein의 $$K$$-flat resolution을 사용한다. 이렇게 정의한 $$Lf^\ast$$는 $$D^-(\operatorname{Mod}(\mathcal{O}_Y)) \to D^-(\operatorname{Mod}(\mathcal{O}_X))$$로 잘 정의되며, 그 cohomology $$H^{-i}(Lf^\ast \mathcal{G})$$는 module 차원의 higher Tor sheaf로 해석된다.

abelian group sheaf만 다룰 때, 즉 $$\mathcal{O}_X = \mathbb{Z}_X$$, $$\mathcal{O}_Y = \mathbb{Z}_Y$$이고 $$f^{-1}\mathbb{Z}_Y = \mathbb{Z}_X$$인 경우에는 $$f^\ast = f^{-1}$$이 되어 [명제 5](#prop5)에 의해 $$Lf^\ast = f^{-1}$$로 환원되며 별도의 derivation이 필요 없다. Module pullback의 비자명한 derived 구조는 ring sheaf가 점마다 비자명하게 변할 때, 즉 scheme이나 복소 다양체 위의 coherent sheaf를 다룰 때에 본격적으로 나타난다.

## 유도 텐서곱과 유도 Hom

Sheaf의 tensor product $$\mathcal{F} \otimes_{\mathcal{O}_X} \mathcal{G}$$와 sheaf-Hom $$\mathcal{H}om_{\mathcal{O}_X}(\mathcal{F}, \mathcal{G})$$는 각각 presheaf $$U \mapsto \mathcal{F}(U) \otimes_{\mathcal{O}_X(U)} \mathcal{G}(U)$$의 sheafification과, 이미 sheaf인 $$U \mapsto \Hom_{\mathcal{O}_U}(\mathcal{F}\vert_U, \mathcal{G}\vert_U)$$로 정의된다 ([\[위상수학\] §준층, ⁋예시 12](/ko/math/topology/presheaves#ex12)). 이들도 exact하지 않으므로 derived 버전을 가진다.

::: 정의 7
Ringed space $$(X, \mathcal{O}_X)$$ 위에서 다음을 정의한다.

1. 고정된 complex $$\mathcal{G}^\bullet$$에 대해 right exact functor $$(-) \otimes_{\mathcal{O}_X} \mathcal{G}^\bullet$$의 left derived functor를 *derived tensor product* $$\mathcal{F}^\bullet \otimes^L_{\mathcal{O}_X} \mathcal{G}^\bullet$$로 적는다. 이는 $$\mathcal{F}^\bullet$$(또는 $$\mathcal{G}^\bullet$$)의 flat resolution 위에서 계산한다.
2. 고정된 complex $$\mathcal{F}^\bullet$$에 대해 left exact functor $$\mathcal{H}om_{\mathcal{O}_X}(\mathcal{F}^\bullet, -)$$의 right derived functor를 *derived sheaf-Hom* $$R\mathcal{H}om_{\mathcal{O}_X}(\mathcal{F}^\bullet, \mathcal{G}^\bullet)$$로 적는다. 이는 $$\mathcal{G}^\bullet$$의 injective resolution 위에서 계산한다.
:::

이 두 함자는 [\[호몰로지 대수학\] §유도카테고리, ⁋명제 10](/ko/math/homological_algebra/derived_categories#prop10)에서 추상적으로 정의한 $$R\Hom$$과 $$\otimes^L$$의 sheaf 차원 버전이며, 같은 명제와 그 직후 서술에 의해 그 cohomology가 고전적 유도 함자를 복원한다. 구체적으로 sheaf 차원에서
$$\mathcal{E}xt^i_{\mathcal{O}_X}(\mathcal{F}, \mathcal{G}) = H^i(R\mathcal{H}om_{\mathcal{O}_X}(\mathcal{F}, \mathcal{G})), \qquad \mathcal{T}or^{\mathcal{O}_X}_i(\mathcal{F}, \mathcal{G}) = H^{-i}(\mathcal{F} \otimes^L_{\mathcal{O}_X} \mathcal{G})$$
가 성립하며, 우변의 $$\mathcal{E}xt$$와 $$\mathcal{T}or$$는 sheaf-valued local 유도 함자이다. 한편 hom-tensor adjunction은 derived 차원으로 올라가서도 유지된다.

::: 명제 8
Ringed space $$(X, \mathcal{O}_X)$$ 위의 complex $$\mathcal{F}^\bullet, \mathcal{G}^\bullet, \mathcal{H}^\bullet \in D(\operatorname{Mod}(\mathcal{O}_X))$$에 대해 derived tensor-hom adjunction
$$R\mathcal{H}om_{\mathcal{O}_X}(\mathcal{F}^\bullet \otimes^L_{\mathcal{O}_X} \mathcal{G}^\bullet, \mathcal{H}^\bullet) \cong R\mathcal{H}om_{\mathcal{O}_X}(\mathcal{F}^\bullet, R\mathcal{H}om_{\mathcal{O}_X}(\mathcal{G}^\bullet, \mathcal{H}^\bullet))$$
이 성립한다.
:::
::: 증명
이는 [\[호몰로지 대수학\] §유도카테고리, ⁋명제 13](/ko/math/homological_algebra/derived_categories#prop13)의 derived adjunction을 $$F = (-) \otimes_{\mathcal{O}_X} \mathcal{G}^\bullet$$ (right exact)와 $$G = \mathcal{H}om_{\mathcal{O}_X}(\mathcal{G}^\bullet, -)$$ (left exact)에 적용한 것이다. 미유도 차원에서 tensor-hom adjunction $$\mathcal{H}om(\mathcal{A} \otimes \mathcal{G}, \mathcal{H}) \cong \mathcal{H}om(\mathcal{A}, \mathcal{H}om(\mathcal{G}, \mathcal{H}))$$이 성립하고, $$\mathcal{F}^\bullet$$를 $$K$$-flat resolution으로, $$\mathcal{H}^\bullet$$를 $$K$$-injective resolution으로 대체하면 좌변과 우변이 각각 derived 함자를 계산하면서 동형이 유지된다. 핵심은 $$K$$-flat complex와 $$\mathcal{G}^\bullet$$의 tensor가 다시 derived tensor를 올바르게 계산하고, $$K$$-injective complex로의 $$\mathcal{H}om$$이 derived sheaf-Hom을 올바르게 계산한다는 데 있다.
:::

명제는 sheaf-Hom의 전역 단면을 취하면 $$R\Hom_{\mathcal{O}_X}(\mathcal{F}^\bullet, \mathcal{G}^\bullet) = R\Gamma(X, R\mathcal{H}om_{\mathcal{O}_X}(\mathcal{F}^\bullet, \mathcal{G}^\bullet))$$의 형태로 global derived Hom과 연결되며, 그 cohomology가 sheaf의 $$\Ext$$-group $$\Ext^i_{\mathcal{O}_X}(\mathcal{F}, \mathcal{G})$$를 준다. Local $$\mathcal{E}xt$$ sheaf와 global $$\Ext$$ group 사이의 관계는 $$R\Gamma$$를 사이에 끼운 합성 함자의 spectral sequence, 즉 local-to-global $$\Ext$$ spectral sequence로 나타나는데, 이는 다음 절의 합성 정리의 한 사례이다.

## 유도 수반과 합성

이제 derived category 차원에서 sheaf 함자들이 이루는 adjunction을 정리한다. 미유도 차원의 adjoint pair $$(f^{-1}, f_\ast)$$와 $$(f^\ast, f_\ast)$$를 [\[호몰로지 대수학\] §유도카테고리, ⁋명제 13](/ko/math/homological_algebra/derived_categories#prop13)에 통과시키면 다음을 얻는다.

::: 정리 9
Continuous map $$f: X \to Y$$에 대해 다음의 derived adjunction이 성립한다.

1. $$\Sh(-, \Ab)$$ 차원에서 $$(f^{-1}, Rf_\ast)$$는 adjoint pair이다. 즉 $$\mathcal{F}^\bullet \in D^+(\Sh(X))$$, $$\mathcal{G}^\bullet \in D^-(\Sh(Y))$$에 대해
$$\Hom_{D(\Sh(X))}(f^{-1}\mathcal{G}^\bullet, \mathcal{F}^\bullet) \cong \Hom_{D(\Sh(Y))}(\mathcal{G}^\bullet, Rf_\ast \mathcal{F}^\bullet)$$
이 성립한다.
2. Ringed space morphism $$f: (X, \mathcal{O}_X) \to (Y, \mathcal{O}_Y)$$에 대해 $$(Lf^\ast, Rf_\ast)$$는 adjoint pair이다. 즉 $$\mathcal{F}^\bullet \in D^+(\operatorname{Mod}(\mathcal{O}_X))$$, $$\mathcal{G}^\bullet \in D^-(\operatorname{Mod}(\mathcal{O}_Y))$$에 대해
$$\Hom_{D(\operatorname{Mod}(\mathcal{O}_X))}(Lf^\ast \mathcal{G}^\bullet, \mathcal{F}^\bullet) \cong \Hom_{D(\operatorname{Mod}(\mathcal{O}_Y))}(\mathcal{G}^\bullet, Rf_\ast \mathcal{F}^\bullet)$$
이 성립한다.
:::
::: 증명
두 경우 모두 [\[호몰로지 대수학\] §유도카테고리, ⁋명제 13](/ko/math/homological_algebra/derived_categories#prop13)의 직접 적용이다. 첫 번째 경우, $$f^{-1}$$은 exact (right exact)이고 $$f_\ast$$는 left exact이며 $$(f^{-1}, f_\ast)$$는 adjoint pair이다 ([\[위상수학\] §층, ⁋보조정리 11](/ko/math/topology/sheaves#lem11)). $$f^{-1}$$이 exact하므로 [명제 5](#prop5)에 의해 $$Lf^{-1} = f^{-1}$$이고, 인용한 derived adjunction이 $$Lf^{-1} = f^{-1}$$과 $$Rf_\ast$$ 사이의 adjunction으로 환원된다. 두 번째 경우, $$f^\ast$$는 right exact이고 $$f_\ast$$는 left exact이며 $$(f^\ast, f_\ast)$$가 adjoint pair이므로 ([정의 6](#def6) 직후), 같은 명제에 의해 $$(Lf^\ast, Rf_\ast)$$가 adjoint pair이다.
:::

이 adjunction은 sheaf 이론의 기본적인 functoriality를 derived 차원에서 한 줄로 정리한다. 특히 $$f: X \to \{\ast\}$$의 경우 [따름정리 3](#cor3)에 의해 $$Rf_\ast = R\Gamma(X, -)$$이고, $$f^{-1}$$은 abelian group $$A$$를 constant sheaf $$A_X$$로 보내므로, adjunction의 첫 부분은 $$\Hom_{D(\Ab)}(A, R\Gamma(X, \mathcal{F}^\bullet)) \cong \Hom_{D(\Sh(X))}(A_X, \mathcal{F}^\bullet)$$의 형태가 되어, constant sheaf로부터의 morphism이 cohomology를 계산하는 통로임을 derived 차원에서 보여 준다.

derived category로 옮긴 가장 큰 이득은 합성에서 드러난다. 미유도 차원에서 $$(gf)_\ast = g_\ast f_\ast$$는 자명하지만, 그 유도 버전의 관계는 spectral sequence를 거쳐야만 기술된다. Derived category에서는 이것이 단일한 동형으로 정리된다.

::: 정리 10 (Grothendieck 합성 함자 정리)
Continuous map $$f: X \to Y$$, $$g: Y \to Z$$에 대해 $$D^+(\Sh(X))$$ 위에서 자연스러운 동형
$$R(g f)_\ast \cong Rg_\ast \circ Rf_\ast$$
가 성립한다. 같은 동형이 ringed space 사이의 사상에 대한 $$\operatorname{Mod}(\mathcal{O}_X)$$ 차원에서도 성립한다.
:::
::: 증명
핵심은 $$f_\ast$$가 injective sheaf를 $$g_\ast$$-acyclic sheaf로 보낸다는 사실이다. $$f_\ast$$는 exact functor $$f^{-1}$$의 right adjoint이므로 injective object를 injective object로 보낸다. 즉 $$\mathcal{I}$$가 injective이면 $$f_\ast \mathcal{I}$$도 injective이고, injective sheaf는 flasque이며 ([\[대수다양체\] §층 코호몰로지, ⁋보조정리 9](/ko/math/algebraic_varieties/sheaf_cohomology#lem9)) flasque sheaf는 $$g_\ast$$-acyclic이다 ([명제 4](#prop4)의 증명).

이제 $$\mathcal{F}^\bullet \in D^+(\Sh(X))$$의 $$K$$-injective resolution $$\mathcal{I}^\bullet$$을 택하자. 정의에 의해 $$Rf_\ast \mathcal{F}^\bullet = f_\ast \mathcal{I}^\bullet$$이다. $$f_\ast \mathcal{I}^\bullet$$은 $$g_\ast$$-acyclic 항으로 이루어진 complex이므로 [명제 4](#prop4)에 의해 $$g_\ast$$에 적용하여 $$Rg_\ast(f_\ast \mathcal{I}^\bullet) = g_\ast f_\ast \mathcal{I}^\bullet$$을 얻는다. 한편 $$(gf)_\ast = g_\ast f_\ast$$이고 $$\mathcal{I}^\bullet$$은 $$(gf)_\ast$$를 계산하는 데 쓸 수 있는 $$K$$-injective resolution이므로 $$R(gf)_\ast \mathcal{F}^\bullet = (gf)_\ast \mathcal{I}^\bullet = g_\ast f_\ast \mathcal{I}^\bullet$$이다. 따라서
$$R(gf)_\ast \mathcal{F}^\bullet = g_\ast f_\ast \mathcal{I}^\bullet = Rg_\ast(f_\ast \mathcal{I}^\bullet) = Rg_\ast Rf_\ast \mathcal{F}^\bullet$$
이 성립한다. Ringed space 차원도 동일하다.
:::

이 동형은 단일한 등식이지만, 양변의 cohomology를 취하면 곧바로 Leray spectral sequence를 회복한다. $$Rg_\ast \circ Rf_\ast$$의 cohomology를 계산하는 표준적 도구가 두 derived functor의 합성에 대한 Grothendieck spectral sequence이며, 그 $$E_2$$ page는
$$E_2^{p,q} = R^p g_\ast (R^q f_\ast \mathcal{F}) \Rightarrow R^{p+q}(gf)_\ast \mathcal{F}$$
이다. 특히 $$Z = \{\ast\}$$로 두면 $$R^p g_\ast = H^p(Y, -)$$, $$R^{p+q}(gf)_\ast = H^{p+q}(X, -)$$가 되어
$$E_2^{p,q} = H^p(Y, R^q f_\ast \mathcal{F}) \Rightarrow H^{p+q}(X, \mathcal{F})$$
를 얻는다. 이것이 바로 [\[대수다양체\] §층 코호몰로지, ⁋명제 19](/ko/math/algebraic_varieties/sheaf_cohomology#prop19)에서 Cartan-Eilenberg resolution을 통해 직접 구성하였던 Leray spectral sequence이다. Derived category의 관점에서 보면 Leray spectral sequence는 독립된 정리가 아니라 합성 동형 $$R(gf)_\ast \cong Rg_\ast Rf_\ast$$의 cohomology를 계산하는 한 가지 방법일 뿐이다. 같은 논법을 $$R\Gamma(X, R\mathcal{H}om(\mathcal{F}, \mathcal{G}))$$에 적용하면 local-to-global $$\Ext$$ spectral sequence $$E_2^{p,q} = H^p(X, \mathcal{E}xt^q(\mathcal{F}, \mathcal{G})) \Rightarrow \Ext^{p+q}(\mathcal{F}, \mathcal{G})$$를 같은 방식으로 얻는다.

## Torus 위의 유도 당김과 Leray 분해

지금까지의 기계를 구체적인 계산으로 점검한다. 가장 단순하면서도 비자명한 $$R^1$$을 드러내는 예로 원과 torus 위의 constant sheaf를 다룬다. $$\mathbb{Z}_X$$로 stalk $$\mathbb{Z}$$를 갖는 constant sheaf를 적는다.

::: 예시 11
원 $$S^1$$ 위의 constant sheaf $$\mathbb{Z}_{S^1}$$의 cohomology를 구하고, 이로부터 torus $$T^2 = S^1 \times S^1$$의 cohomology를 Leray spectral sequence로 복원한다.
:::

먼저 $$a: S^1 \to \{\ast\}$$에 대한 $$R\Gamma(S^1, \mathbb{Z}_{S^1}) = Ra_\ast \mathbb{Z}_{S^1}$$을 계산한다. $$S^1$$을 두 호 $$U, V$$로 덮자. 각각은 열린 구간과 위상동형이고 $$U \cap V$$는 서로소인 두 호 $$W_1 \sqcup W_2$$이며, $$U$$, $$V$$, $$W_1$$, $$W_2$$는 모두 가축이라 그 위에서 $$\mathbb{Z}$$ 계수 cohomology가 차수 $$0$$에 집중된다. 이 덮개에 대한 Čech complex를 적으면 ([\[대수다양체\] §층 코호몰로지, ⁋정의 3](/ko/math/algebraic_varieties/sheaf_cohomology#def3))
$$\check{C}^0 = \mathbb{Z}_U \oplus \mathbb{Z}_V = \mathbb{Z}^2, \qquad \check{C}^1 = \mathbb{Z}_{W_1} \oplus \mathbb{Z}_{W_2} = \mathbb{Z}^2$$
이고 그 이상은 $$0$$이다. Coboundary $$d: \mathbb{Z}^2 \to \mathbb{Z}^2$$는 $$(s_U, s_V) \mapsto (s_V - s_U, s_V - s_U)$$로, $$W_1$$과 $$W_2$$ 두 성분에서 같은 차 $$s_V - s_U$$를 준다. 따라서
$$\ker d = \{(s_U, s_V): s_U = s_V\} \cong \mathbb{Z}, \qquad \operatorname{coker} d = \mathbb{Z}^2 / \{(t, t): t \in \mathbb{Z}\} \cong \mathbb{Z}$$
이고, 덮개의 각 성분이 acyclic이므로 ([\[대수다양체\] §층 코호몰로지, ⁋정리 11](/ko/math/algebraic_varieties/sheaf_cohomology#thm11)) 이 Čech cohomology가 sheaf cohomology와 일치한다. 그러므로
$$H^0(S^1, \mathbb{Z}_{S^1}) = \mathbb{Z}, \qquad H^1(S^1, \mathbb{Z}_{S^1}) = \mathbb{Z}, \qquad H^i = 0 \quad (i \geq 2)$$
이고, derived category에서 $$Ra_\ast \mathbb{Z}_{S^1}$$은 cohomology가 차수 $$0$$과 $$1$$에서 각각 $$\mathbb{Z}$$인 complex이다. 비자명한 $$R^1$$의 출현은 $$S^1$$이 단일한 가축 열린집합으로 덮이지 않는다는 위상적 사실, 즉 $$d$$의 cokernel이 비자명하다는 데서 직접 비롯한다.

이제 사영 $$p: T^2 = S^1 \times S^1 \to S^1$$, $$(x, y) \mapsto x$$를 따라 $$Rp_\ast \mathbb{Z}_{T^2}$$를 계산한다. $$R^q p_\ast \mathbb{Z}_{T^2}$$는 presheaf $$V \mapsto H^q(p^{-1}(V), \mathbb{Z})$$의 sheafification이다. $$V \subset S^1$$이 충분히 작은 호이면 $$p^{-1}(V) = V \times S^1$$이고, $$V$$가 가축이므로 $$H^q(V \times S^1, \mathbb{Z}) = H^q(S^1, \mathbb{Z})$$이다. 따라서 stalk 차원에서
$$(R^0 p_\ast \mathbb{Z}_{T^2})_x = \mathbb{Z}, \qquad (R^1 p_\ast \mathbb{Z}_{T^2})_x = \mathbb{Z}, \qquad (R^q p_\ast \mathbb{Z}_{T^2})_x = 0 \quad (q \geq 2)$$
이고, $$p$$가 $$S^1 \times S^1 \to S^1$$인 곱사상이라 fiber 방향의 monodromy가 없으므로 이 stalk들이 모여 다시 constant sheaf를 이룬다. 즉
$$R^0 p_\ast \mathbb{Z}_{T^2} \cong \mathbb{Z}_{S^1}, \qquad R^1 p_\ast \mathbb{Z}_{T^2} \cong \mathbb{Z}_{S^1}$$
이다. 이 비자명한 $$R^1 p_\ast = \mathbb{Z}_{S^1}$$이 fiber $$S^1$$의 첫 cohomology를 base 위에 기억하는 sheaf이다.

이 두 결과를 Leray spectral sequence $$E_2^{p,q} = H^p(S^1, R^q p_\ast \mathbb{Z}_{T^2}) \Rightarrow H^{p+q}(T^2, \mathbb{Z})$$에 넣는다. 위에서 구한 $$R^q p_\ast$$와 $$S^1$$의 cohomology에 의해 비자명한 $$E_2$$ 항은
$$E_2^{0,0} = H^0(S^1, \mathbb{Z}_{S^1}) = \mathbb{Z}, \quad E_2^{1,0} = H^1(S^1, \mathbb{Z}_{S^1}) = \mathbb{Z}, \quad E_2^{0,1} = H^0(S^1, \mathbb{Z}_{S^1}) = \mathbb{Z}, \quad E_2^{1,1} = H^1(S^1, \mathbb{Z}_{S^1}) = \mathbb{Z}$$
의 네 개이고 나머지는 모두 $$0$$이다. $$E_2$$ page가 $$p, q \in \{0, 1\}$$의 정사각형에 집중되어 있으므로 차수 차이가 $$2$$ 이상인 미분 $$d_2: E_2^{p,q} \to E_2^{p+2, q-1}$$은 시작 항이나 도착 항 중 하나가 항상 $$0$$이라 모두 영사상이다. 따라서 spectral sequence는 $$E_2$$에서 degenerate하고 $$E_\infty = E_2$$이다. 각 전체 차수 $$n = p + q$$별로 항들을 모으면
$$H^0(T^2, \mathbb{Z}) = E_\infty^{0,0} = \mathbb{Z}, \qquad H^1(T^2, \mathbb{Z}) = E_\infty^{1,0} \oplus E_\infty^{0,1} = \mathbb{Z}^2, \qquad H^2(T^2, \mathbb{Z}) = E_\infty^{1,1} = \mathbb{Z}$$
를 얻는다. 등급 군의 확장이 자유 $$\mathbb{Z}$$-module 사이의 것이라 분열되므로 $$H^1$$이 두 항의 직합이 된다. 이는 torus의 well-known한 cohomology $$H^\ast(T^2, \mathbb{Z}) = (\mathbb{Z}, \mathbb{Z}^2, \mathbb{Z})$$와 일치하며, derived pushforward $$Rp_\ast \mathbb{Z}_{T^2}$$가 fiber와 base의 cohomology를 어떻게 결합하는지를 명시적으로 보여 준다.

이 계산에서 fibration이 곱구조라 monodromy가 없었기에 $$R^1 p_\ast$$가 constant sheaf가 되었지만, Klein bottle처럼 fiber가 부호를 바꾸며 붙는 비자명한 $$S^1$$-bundle에서는 $$R^1 p_\ast$$가 비자명한 monodromy를 갖는 rank $$1$$ local system이 되어 $$H^1$$의 계산이 달라진다. Derived pushforward $$Rp_\ast$$는 이러한 fiber 위의 비틀림 정보를 base 위의 sheaf로 충실히 기록한다.

---

**참고문헌**

**[KS]** M. Kashiwara, P. Schapira, *Sheaves on manifolds*, Springer, 1990.

**[Dim]** A. Dimca, *Sheaves in topology*, Springer, 2004.

**[GM]** S. I. Gelfand, Y. I. Manin, *Methods of homological algebra*, Springer, 2003.

**[Stacks]** The Stacks Project Authors, *The Stacks Project*, https://stacks.math.columbia.edu.
