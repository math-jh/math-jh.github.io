---
title: "준연접층"
description: "스킴의 구조층 위에 정의되는 가군층을 도입하고, affine scheme 위에서 가군의 연관층이 가군 범주와 준연접층 범주 사이의 동치를 주는 것을 보인다. 이를 통해 준연접성이 affine-local property임을 확인하고 ideal sheaf, locally free sheaf, pullback과 pushforward를 다룬다."
excerpt: "Sheaf of O_X-modules, the equivalence M↦M̃ on affine schemes, and quasi-coherence"

categories: [Math / Scheme Theory]
permalink: /ko/math/scheme_theory/quasicoherent_sheaves
sidebar: 
    nav: "scheme_theory-ko"

date: 2026-06-21
weight: 17

published: false
---

스킴 $$X$$의 structure sheaf $$\mathcal{O}_X$$는 그 자체로 환들의 sheaf이지만, 우리는 종종 $$\mathcal{O}_X$$ 위에서 정의된 가군들의 sheaf를 다루어야 한다. 가령 affine scheme $$\Spec A$$ 위에서 우리가 관심을 가지는 대상들, 즉 $$A$$-가군 $$M$$은 $$\Spec A$$ 위의 sheaf로 변환되어야 자연스럽게 기하학과 연결되며, ideal sheaf나 line bundle 또한 이러한 sheaf의 예시이다. 그러나 임의의 $$\mathcal{O}_X$$-가군층은 너무 거칠어서 affine 위에서의 대수적인 정보로 환원되지 않는다. 이번 글에서는 affine 위에서 가군으로부터 직접 만들어지는 sheaf를 정의하고, 이로부터 *quasi-coherent sheaf*의 개념을 도입한다. 핵심은 affine scheme 위에서 가군과 그 연관층이 본질적으로 같은 정보를 담는다는 것이며, 이로부터 준연접성이 affine-local property임을 얻는다.

## $$\mathcal{O}_X$$-가군층

우선 일반적인 ringed space $$(X, \mathcal{O}_X)$$ ([§아핀스킴, ⁋정의 1](/ko/math/scheme_theory/affine_schemes#def1)) 위에서 가군들의 sheaf를 정의한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Ringed space $$(X, \mathcal{O}_X)$$ 위의 abelian group들의 sheaf $$\mathcal{F}$$가 *$$\mathcal{O}_X$$-module<sub>$$\mathcal{O}_X$$-가군층</sub>*이라는 것은, 임의의 열린집합 $$U$$에 대하여 $$\mathcal{F}(U)$$가 $$\mathcal{O}_X(U)$$-가군의 구조를 가지며, 이 가군 구조가 restriction map과 호환되는 것이다. 즉 $$V\subseteq U$$와 $$a\in \mathcal{O}_X(U)$$, $$s\in \mathcal{F}(U)$$에 대하여 $$(a\cdot s)\vert_V=(a\vert_V)\cdot (s\vert_V)$$가 성립하는 것이다. 두 $$\mathcal{O}_X$$-가군층 $$\mathcal{F}, \mathcal{G}$$ 사이의 *morphism*은 sheaf 사이의 morphism $$\varphi:\mathcal{F} \rightarrow \mathcal{G}$$ 가운데, 각각의 $$U$$에 대하여 $$\varphi(U):\mathcal{F}(U) \rightarrow \mathcal{G}(U)$$가 $$\mathcal{O}_X(U)$$-가군 준동형사상인 것이다.

</div>

즉 scalar 곱을 먼저 한 뒤 제한하는 것과 제한을 먼저 한 뒤 scalar 곱을 하는 것이 일치한다는 것이다. $$X$$ 위의 $$\mathcal{O}_X$$-가군층들과 그 사이의 morphism들은 category를 이루며, 이를 $$\Mod(\mathcal{O}_X)$$로 적는다. 가장 기본적인 예시는 $$\mathcal{O}_X$$ 자기 자신으로, 이는 각각의 $$\mathcal{O}_X(U)$$를 그 위의 rank $$1$$ free 가군으로 보아 얻어지는 $$\mathcal{O}_X$$-가군층이다.

$$\mathcal{O}_X$$-가군층은 stalk 수준에서도 가군 구조를 물려받는다. 임의의 $$x\in X$$에 대하여 stalk $$\mathcal{F}_x=\varinjlim_{U\ni x}\mathcal{F}(U)$$는 $$\mathcal{O}_{X,x}=\varinjlim_{U\ni x}\mathcal{O}_X(U)$$ 위의 가군이 되는데, 이는 direct limit이 $$\Mod$$에서 가군 구조와 호환되기 때문이다.

일반적인 가군 위에서의 선형대수적 연산들은 $$\mathcal{O}_X$$-가군층에 그대로 옮겨진다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 두 $$\mathcal{O}_X$$-가군층 $$\mathcal{F}, \mathcal{G}$$에 대하여,

1. *direct sum* $$\mathcal{F}\oplus \mathcal{G}$$는 열린집합마다 $$U\mapsto \mathcal{F}(U)\oplus \mathcal{G}(U)$$로 주어지는 $$\mathcal{O}_X$$-가군층이다.
2. *tensor product* $$\mathcal{F}\otimes_{\mathcal{O}_X}\mathcal{G}$$는 presheaf $$U\mapsto \mathcal{F}(U)\otimes_{\mathcal{O}_X(U)}\mathcal{G}(U)$$의 sheafification이다.
3. *sheaf Hom* $$\sHom_{\mathcal{O}_X}(\mathcal{F}, \mathcal{G})$$는 열린집합마다 $$U\mapsto \Hom_{\mathcal{O}_X\vert_U}(\mathcal{F}\vert_U, \mathcal{G}\vert_U)$$로 주어지는 $$\mathcal{O}_X$$-가군층이다.

</div>

위에서 direct sum의 경우는 열린집합마다의 대응이 곧바로 sheaf를 이루지만, tensor product의 경우 presheaf $$U\mapsto \mathcal{F}(U)\otimes_{\mathcal{O}_X(U)}\mathcal{G}(U)$$가 sheaf 조건을 만족하지 않을 수 있어 sheafification이 필요하다. ([\[위상수학\] §준층, ⁋정의 2](/ko/math/topology/presheaves#def2) 이후 sheafification) 반면 sheaf Hom의 경우는, 두 sheaf 사이의 morphism들이 본래 sheaf 조건을 만족하므로 sheafification 없이 곧바로 sheaf가 된다. Sheaf Hom $$\sHom_{\mathcal{O}_X}(\mathcal{F}, \mathcal{G})$$의 global section은 $$\Hom_{\mathcal{O}_X}(\mathcal{F}, \mathcal{G})$$이며, 특히 $$\sHom_{\mathcal{O}_X}(\mathcal{O}_X, \mathcal{F})\cong \mathcal{F}$$가 성립한다.

이렇듯 $$\mathcal{O}_X$$-가군층은 일반적인 가군과 비슷한 형식적 성질을 가지지만, 그 자체로는 너무 일반적이어서 affine 위의 대수적인 정보로 환원되지 않는다. 우리가 실제로 다루고자 하는 것은 affine 위에서 가군으로부터 직접 만들어지는 sheaf들이다.

## Affine scheme 위의 연관층

이제 affine scheme $$\Spec A$$를 고정하고, $$A$$-가군 $$M$$이 주어졌다 하자. 우리는 $$M$$으로부터 $$\Spec A$$ 위의 $$\mathcal{O}_{\Spec A}$$-가군층을 만들고자 한다. 그 구성은 structure sheaf $$\mathcal{O}_{\Spec A}$$의 구성을 그대로 본뜬 것이다. Structure sheaf가 principal open set $$D(f)$$ 위에서 localization $$A_f$$로 주어졌듯, 우리는 가군의 localization $$M_f=S_f^{-1}M$$을 같은 방식으로 붙인다. ([§아핀스킴, ⁋보조정리 6](/ko/math/scheme_theory/affine_schemes#lem6))

<div class="proposition" markdown="1">

<ins id="lem3">**보조정리 3**</ins> $$A$$-가군 $$M$$에 대하여, $$\Spec A$$의 base $$\{D(f)\}_{f\in A}$$ 위에서

$$\widetilde M(D(f))=M_f$$

으로 정의하고, $$D(f)\subseteq D(g)$$에 대한 restriction map을 canonical localization map $$M_g \rightarrow M_f$$로 정의하자. 그럼 이 데이터는 [§아핀스킴, ⁋보조정리 6](/ko/math/scheme_theory/affine_schemes#lem6)의 두 조건을 만족하여 $$\Spec A$$ 위의 sheaf로 유일하게 확장되며, 이는 $$\mathcal{O}_{\Spec A}$$-가군층이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $$D(f)\subseteq D(g)$$일 때 restriction map이 잘 정의됨을 본다. [§아핀스킴, ⁋보조정리 5](/ko/math/scheme_theory/affine_schemes#lem5)와 같은 논증으로, $$D(f)\subseteq D(g)$$인 것은 $$g$$의 image가 $$A_f$$의 unit인 것과 동치이므로, $$A_g$$의 universal property로부터 $$M_g=M\otimes_A A_g \rightarrow M\otimes_A A_f=M_f$$가 유일하게 결정된다. 이 map이 [\[위상수학\] §준층, ⁋정의 2](/ko/math/topology/presheaves#def2)의 restriction 조건을 만족함은 localization의 functoriality로부터 자명하다.

이제 [§아핀스킴, ⁋보조정리 6](/ko/math/scheme_theory/affine_schemes#lem6)의 두 sheaf 조건을 보인다. 그 증명은 [§아핀스킴, ⁋보조정리 6](/ko/math/scheme_theory/affine_schemes#lem6)의 증명을 그대로 따라가되, 등장하는 환 $$A$$를 가군 $$M$$으로 바꾸어 읽으면 된다. 구체적으로 $$\Spec A=\bigcup_{i\in I}D(f_i)$$를 고정하자. 분리성을 보이기 위해 원소 $$s\in M$$이 모든 $$M_{f_i}$$에서 $$0$$이라 하면, 각각의 $$i$$마다 $$f_i^{m_i}s=0$$인 $$m_i$$가 존재하고, $$\Spec A=\bigcup D(f_i^{m_i})$$로부터 $$1=\sum a_i f_i^{m_i}$$인 $$a_i\in A$$들을 잡으면

$$s=\Bigl(\sum_i a_if_i^{m_i}\Bigr)s=\sum_i a_i(f_i^{m_i}s)=0$$

이다. 접합성의 경우, 각 $$D(f_i)$$ 위에서 주어진 section들 $$s_i=a_i/f_i^{m_i}\in M_{f_i}$$가 겹치는 부분에서 일치하면, [§아핀스킴, ⁋보조정리 6](/ko/math/scheme_theory/affine_schemes#lem6)의 증명에서와 동일하게 $$1=\sum b_i a_i f_i^{Nm_i+m_i}$$ 꼴의 partition of unity를 사용하여 $$s=\sum b_i a_i f_i^{Nm_i}\in M$$이 모든 $$D(f_i)$$ 위에서 $$s_i$$로 제한됨을 확인한다. 이 논증에서 $$A$$의 곱셈을 $$M$$ 위로의 scalar 작용으로 바꾼 것을 제외하면 모든 계산이 동일하다.

마지막으로 각 $$\widetilde M(D(f))=M_f$$는 $$\mathcal{O}_{\Spec A}(D(f))=A_f$$ 위의 가군이고, restriction map이 scalar 작용과 호환되므로 $$\widetilde M$$은 $$\mathcal{O}_{\Spec A}$$-가군층이다.

</details>

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> $$A$$-가군 $$M$$에 대하여, [보조정리 3](#lem3)으로 정의되는 $$\Spec A$$ 위의 $$\mathcal{O}_{\Spec A}$$-가군층 $$\widetilde M$$을 $$M$$의 *associated sheaf<sub>연관층</sub>*라 부른다.

</div>

정의에 의하여 $$\widetilde A=\mathcal{O}_{\Spec A}$$이며, $$\widetilde M$$의 global section은 $$\widetilde M(\Spec A)=\widetilde M(D(1))=M_1=M$$이다. 다음 명제는 연관층이 structure sheaf와 같은 국소적 성질을 가짐을 보여주며, 이는 [§아핀스킴, ⁋보조정리 8](/ko/math/scheme_theory/affine_schemes#lem8)의 가군 버전이다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> $$A$$-가군 $$M$$에 대하여, 다음이 성립한다.

1. 임의의 $$\mathfrak{p}\in \Spec A$$에 대하여 stalk $$\widetilde M_\mathfrak{p}\cong M_\mathfrak{p}$$이다.
2. 임의의 $$f\in A$$에 대하여 $$\widetilde M\vert_{D(f)}\cong \widetilde{M_f}$$이다. 여기에서 우변은 $$\Spec A_f\cong D(f)$$ 위의 $$A_f$$-가군 $$M_f$$의 연관층이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

첫째 결과의 경우, $$D(f)$$들이 $$\Spec A$$의 base이므로 ([\[위상수학\] §위상공간의 기저, ⁋명제 5](/ko/math/topology/topological_bases#prop5))

$$\widetilde M_\mathfrak{p}=\varinjlim_{D(f)\ni \mathfrak{p}}\widetilde M(D(f))=\varinjlim_{f\not\in \mathfrak{p}}M_f$$

이다. 한편 [§아핀스킴, ⁋보조정리 8](/ko/math/scheme_theory/affine_schemes#lem8)의 증명에서 $$\varinjlim_{f\not\in \mathfrak{p}}A_f\cong A_\mathfrak{p}$$를 보인 것과 동일하게, localization과 direct limit의 universal property로부터 $$\varinjlim_{f\not\in \mathfrak{p}}M_f\cong M_\mathfrak{p}$$를 얻는다.

둘째 결과의 경우, [§스킴, ⁋보조정리 2](/ko/math/scheme_theory/schemes#lem2)에 의하여 $$D(f)\cong \Spec A_f$$이고, 이 동형 아래에서 $$\Spec A_f$$의 principal open set은 $$g\in A$$에 대한 $$D(fg)$$의 꼴이다. 그럼

$$\widetilde M\vert_{D(f)}(D(fg))=\widetilde M(D(fg))=M_{fg}\cong (M_f)_g=\widetilde{M_f}(D(g))$$

이고, 이 동형들이 restriction map과 호환되므로 base 위에서 두 sheaf가 일치하며 따라서 $$\widetilde M\vert_{D(f)}\cong \widetilde{M_f}$$이다.

</details>

특히 첫째 결과로부터 $$\widetilde M$$의 stalk은 모두 $$M$$의 localization으로 주어지므로, $$\widetilde M$$은 $$M$$의 국소적인 거동을 전부 담고 있다. 이는 다음 절에서 $$M\mapsto \widetilde M$$이 범주의 동치를 이룬다는 사실의 토대가 된다.

## 동치 정리

이제 우리는 affine scheme 위에서 가군의 연관층을 취하는 대응이 가군 범주와 적절한 sheaf 범주 사이의 동치를 준다는 것을 보인다. 우선 이 대응이 functor이며 exact임을 확인한다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> 대응 $$M\mapsto \widetilde M$$은 functor $$\widetilde{(-)}:\Mod(A) \rightarrow \Mod(\mathcal{O}_{\Spec A})$$를 정의하며, 이는 exact이다. 즉 $$A$$-가군의 short exact sequence

$$0 \rightarrow M' \rightarrow M \rightarrow M'' \rightarrow 0$$

는 $$\mathcal{O}_{\Spec A}$$-가군층의 short exact sequence

$$0 \rightarrow \widetilde{M'} \rightarrow \widetilde M \rightarrow \widetilde{M''} \rightarrow 0$$

를 유도한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$A$$-가군 준동형사상 $$\phi:M \rightarrow N$$이 주어지면, 각각의 $$f\in A$$마다 localization $$\phi_f:M_f \rightarrow N_f$$가 유도되고, 이들은 restriction map과 호환되므로 sheaf 사이의 morphism $$\widetilde\phi:\widetilde M \rightarrow \widetilde N$$을 정의한다. 이 대응이 합성과 항등사상을 보존함은 localization의 functoriality로부터 자명하므로 $$\widetilde{(-)}$$는 functor이다.

Exactness를 보이기 위해, sheaf 사이의 sequence가 exact인 것은 모든 stalk에서 exact인 것과 동치임을 사용한다. [명제 5](#prop5)에 의하여 임의의 $$\mathfrak{p}$$에서 stalk를 취하면 주어진 sequence는

$$0 \rightarrow M'_\mathfrak{p} \rightarrow M_\mathfrak{p} \rightarrow M''_\mathfrak{p} \rightarrow 0$$

가 되며, localization은 exact functor이므로 ([\[가환대수학\] §국소화의 성질들, ⁋명제 2](/ko/math/commutative_algebra/properties_of_localization#prop2)) 이 sequence는 exact이다. 따라서 stalk 수준에서 exact이고, 이로부터 sheaf 수준에서도 exact이다.

</details>

연관층 functor는 tensor product 및 localization과도 호환된다. 즉 $$\widetilde{M\otimes_A N}\cong \widetilde M\otimes_{\mathcal{O}_{\Spec A}}\widetilde N$$이고, 임의의 $$f$$에 대하여 [명제 5](#prop5)에서 본 $$\widetilde M\vert_{D(f)}\cong \widetilde{M_f}$$가 성립한다. 첫째 호환성은 양변의 stalk이 모두 $$(M\otimes_A N)_\mathfrak{p}\cong M_\mathfrak{p}\otimes_{A_\mathfrak{p}}N_\mathfrak{p}$$로 일치함으로부터 따라온다.

이제 동치 정리의 한 방향을 위해 우리는 임의의 $$\mathcal{O}_{\Spec A}$$-가군층이 어떻게 가군으로부터 복원되는지를 알아야 한다. 다음 정리가 핵심이다.

<div class="proposition" markdown="1">

<ins id="thm7">**정리 7**</ins> Affine scheme $$\Spec A$$ 위에서, 다음의 자연스러운 동형사상

$$\Hom_{\mathcal{O}_{\Spec A}}(\widetilde M, \widetilde N)\cong \Hom_A(M, N)$$

이 임의의 $$A$$-가군 $$M, N$$에 대하여 성립한다. 즉 functor $$\widetilde{(-)}:\Mod(A) \rightarrow \Mod(\mathcal{O}_{\Spec A})$$는 fully faithful이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

대응 $$\phi\mapsto \widetilde\phi$$는 [명제 6](#prop6)에 의하여 $$\Hom_A(M, N) \rightarrow \Hom_{\mathcal{O}_{\Spec A}}(\widetilde M, \widetilde N)$$를 준다. 거꾸로 morphism $$\psi:\widetilde M \rightarrow \widetilde N$$이 주어지면, global section 위에서

$$\psi(\Spec A):\widetilde M(\Spec A)=M \rightarrow N=\widetilde N(\Spec A)$$

를 취하여 $$A$$-가군 준동형사상 $$\phi=\psi(\Spec A)$$를 얻는다. 이 두 대응이 서로 역임을 보이면 충분하다.

우선 $$\phi\in \Hom_A(M, N)$$에서 출발하면 $$\widetilde\phi$$의 global section은 정의에 의해 다시 $$\phi$$이므로 한 방향은 자명하다. 거꾸로 $$\psi:\widetilde M \rightarrow \widetilde N$$이 주어졌다 하고 $$\phi=\psi(\Spec A)$$라 하자. 우리는 $$\widetilde \phi=\psi$$임을 보여야 하며, 두 morphism이 일치하는 것은 base $$\{D(f)\}$$ 위에서 일치하는 것으로 충분하다. 임의의 $$f\in A$$에 대하여, $$\psi$$가 sheaf morphism이므로 다음 diagram

![localization square](/assets/images/Math/Scheme_Theory/Quasicoherent_Sheaves-1.svg){:style="width:6.60em" class="invert" .align-center}

이 commute하며, 여기에서 세로 사상은 localization map이다. 한편 $$\psi(D(f))$$는 $$A_f$$-가군 준동형사상이므로 윗줄의 $$\phi$$와 commute한다는 조건과 $$A_f$$-선형성에 의해 임의의 $$m/f^n\in M_f$$에 대하여

$$\psi(D(f))\Bigl(\frac{m}{f^n}\Bigr)=\frac{1}{f^n}\psi(D(f))\Bigl(\frac{m}{1}\Bigr)=\frac{1}{f^n}\frac{\phi(m)}{1}=\frac{\phi(m)}{f^n}=\widetilde\phi(D(f))\Bigl(\frac{m}{f^n}\Bigr)$$

으로 완전히 결정된다. 따라서 $$\psi(D(f))=\widetilde\phi(D(f))$$가 모든 $$f$$에 대해 성립하고, 이로부터 $$\psi=\widetilde\phi$$이다.

</details>

[정리 7](#thm7)은 연관층 functor가 fully faithful임을 보여주지만, 동치를 얻으려면 모든 $$\mathcal{O}_{\Spec A}$$-가군층이 연관층의 꼴인 것은 아니라는 점에 유의해야 한다. 실제로 affine 위에서도 연관층이 아닌 $$\mathcal{O}_{\Spec A}$$-가군층이 존재한다. 따라서 우리는 연관층의 꼴로 나타나는 sheaf만을 골라내어, 그 위에서 동치를 진술해야 한다. 이것이 다음 정의의 동기이다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> Scheme $$X$$ 위의 $$\mathcal{O}_X$$-가군층 $$\mathcal{F}$$가 *quasi-coherent sheaf<sub>준연접층</sub>*라는 것은, 임의의 $$x\in X$$에 대하여 $$x$$의 affine open neighborhood $$U\cong \Spec A$$가 존재하여 적당한 $$A$$-가군 $$M$$에 대해 $$\mathcal{F}\vert_U\cong \widetilde M$$이도록 할 수 있는 것이다.

</div>

$$X$$ 위의 준연접층들과 그 사이의 morphism들은 $$\Mod(\mathcal{O}_X)$$의 full subcategory를 이루며, 이를 $$\QCoh(X)$$로 적는다. 정의에 의하여 준연접성은 국소적인 조건이며, 특히 affine scheme 위에서는 연관층들이 곧 준연접층이다. 이로부터 [정리 7](#thm7)을 affine 위의 동치로 끌어올릴 수 있다.

<div class="proposition" markdown="1">

<ins id="thm9">**정리 9**</ins> Affine scheme $$\Spec A$$에 대하여, functor

$$\widetilde{(-)}:\Mod(A) \rightarrow \QCoh(\Spec A)$$

는 categorical equivalence이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[정리 7](#thm7)에 의하여 $$\widetilde{(-)}$$는 fully faithful이므로, ([\[범주론\] §자연변환, ⁋정리 5](/ko/math/category_theory/natural_transformations#thm5)) essentially surjective임을 보이면 충분하다. 즉 임의의 준연접층 $$\mathcal{F}\in \QCoh(\Spec A)$$가 적당한 $$A$$-가군의 연관층과 동형임을 보여야 한다.

$$M=\mathcal{F}(\Spec A)$$라 하고, 우리는 $$\mathcal{F}\cong \widetilde M$$임을 주장한다. Restriction map들로부터 각각의 $$f\in A$$마다 $$M=\mathcal{F}(\Spec A) \rightarrow \mathcal{F}(D(f))$$가 유도되고, 이 상이 $$f$$의 작용에 대해 invertible하므로 $$A_f$$의 universal property에 의해 $$A_f$$-가군 준동형사상

$$\theta_f:M_f \rightarrow \mathcal{F}(D(f))$$

가 결정된다. 이들은 base $$\{D(f)\}$$ 위에서 morphism $$\theta:\widetilde M \rightarrow \mathcal{F}$$를 정의하므로, $$\theta$$가 stalk마다 동형임을 보이면 된다.

이를 위해 $$\mathcal{F}$$의 준연접성을 사용한다. 각 점 $$\mathfrak{p}$$에 대하여 $$\mathfrak{p}\in D(g)$$이고 $$\mathcal{F}\vert_{D(g)}\cong \widetilde N$$인 적당한 $$g$$와 $$A_g$$-가군 $$N$$이 존재한다. ([정의 8](#def8)에서 affine open neighborhood를 principal open set으로 줄일 수 있는 것은 이들이 base이기 때문이다.) 그럼 $$N=\mathcal{F}(D(g))$$이고, [명제 5](#prop5)에 의하여 $$D(g)$$ 위로 제한된 $$\theta$$는 $$\widetilde{M_g} \rightarrow \widetilde N$$의 꼴이다. 한편 $$M_g=\mathcal{F}(\Spec A)_g$$와 $$N=\mathcal{F}(D(g))$$ 사이의 사상은, $$\mathcal{F}\vert_{D(g)}\cong \widetilde N$$가 준연접층이므로 [정리 7](#thm7)의 논증에 의해 동형이다. 따라서 $$\theta$$는 각 $$D(g)$$ 위에서 동형이고, 이로부터 모든 stalk에서 동형이므로 $$\theta:\widetilde M \rightarrow \mathcal{F}$$는 sheaf의 동형사상이다.

</details>

[정리 9](#thm9)는 affine scheme 위에서 준연접층을 다루는 것이 곧 가군을 다루는 것과 같음을 말해준다. 즉 $$\Spec A$$ 위의 모든 준연접층은 그 global section 가군 $$M=\Gamma(\Spec A, \mathcal{F})$$으로 완전히 복원되며, 이 대응은 [명제 6](#prop6)의 exactness와 위에서 언급한 tensor product 호환성을 통해 가군의 대수와 sheaf의 대수를 일치시킨다.

## 준연접성의 affine-local 성질

정의에 의하면 준연접성을 확인하려면 각 점마다 적절한 affine open neighborhood를 찾아 그 위에서 연관층임을 보여야 한다. 그러나 실제로는 임의의 affine open subset 위에서 연관층이 되는 것이 자동으로 따라온다. 즉 준연접성은 affine-local property이다.

<div class="proposition" markdown="1">

<ins id="thm10">**정리 10**</ins> Scheme $$X$$ 위의 $$\mathcal{O}_X$$-가군층 $$\mathcal{F}$$에 대하여 다음이 동치이다.

1. $$\mathcal{F}$$는 준연접층이다.
2. $$X$$의 모든 affine open subset $$U\cong \Spec A$$에 대하여, $$A$$-가군 $$M_U=\mathcal{F}(U)$$가 존재하여 $$\mathcal{F}\vert_U\cong \widetilde{M_U}$$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

둘째 조건이 첫째 조건을 함의하는 것은 [정의 8](#def8)로부터 자명하므로 그 역을 보인다. $$\mathcal{F}$$가 준연접층이라 하고, 임의의 affine open subset $$U=\Spec A$$를 고정하자. 우리는 $$\mathcal{F}\vert_U$$가 $$\Spec A$$ 위의 준연접층임을 보이면 [정리 9](#thm9)에 의해 $$\mathcal{F}\vert_U\cong \widetilde{M_U}$$ (단, $$M_U=\mathcal{F}(U)$$)가 따라온다.

$$\mathcal{F}$$의 준연접성에 의하여 $$U$$의 각 점 $$x$$마다 ($$X$$에서의) affine open neighborhood $$V\cong \Spec B$$와 $$B$$-가군 $$N$$이 존재하여 $$\mathcal{F}\vert_V\cong \widetilde N$$이다. [§스킴, ⁋보조정리 3](/ko/math/scheme_theory/schemes#lem3)의 증명에서와 같이, $$U\cap V$$는 $$U$$ 안에서 principal open set들 $$D(f)$$ ($$f\in A$$)로 덮이며, 또 $$V$$ 안에서도 principal open set $$D(g)$$ ($$g\in B$$)로 덮인다. 이 둘을 동시에 만족하도록 충분히 작게 잡으면, $$x$$를 포함하고 $$U$$와 $$V$$ 양쪽의 principal open set이 되는 affine open $$W=\Spec A_f=\Spec B_g$$를 얻는다.

이제 $$\mathcal{F}\vert_V\cong \widetilde N$$이므로 [명제 5](#prop5)에 의하여 $$\mathcal{F}\vert_W\cong \widetilde N\vert_{D(g)}\cong \widetilde{N_g}$$이고, $$W=\Spec A_f$$로 보면 이는 $$A_f$$-가군 $$N_g$$의 연관층이다. 따라서 $$U=\Spec A$$의 각 점은 $$\mathcal{F}\vert_U$$가 연관층이 되는 principal open neighborhood를 가지며, 이로부터 $$\mathcal{F}\vert_U$$는 $$\Spec A$$ 위의 준연접층이다.

</details>

따라서 어떤 한 affine cover 위에서 연관층임을 확인하는 것만으로 준연접성이 보장되며, 그 결과 모든 affine open subset 위에서 자동으로 연관층이 된다. 이 affine-locality 덕분에 준연접층에 대한 많은 명제들은 affine 위에서의 가군 명제로 환원하여 증명할 수 있다.

준연접층 가운데 특히 affine 위에서 finitely generated 가군 또는 finitely presented 가군에 대응하는 것들을 따로 구별한다. 이는 Noetherian 가정 아래에서 가장 잘 작동한다.

<div class="definition" markdown="1">

<ins id="def11">**정의 11**</ins> Scheme $$X$$ 위의 준연접층 $$\mathcal{F}$$가 *finite type<sub>유한형</sub>*이라는 것은, 각 점이 affine open neighborhood $$U\cong \Spec A$$를 가져 $$\mathcal{F}\vert_U\cong \widetilde M$$이고 $$M$$이 finitely generated $$A$$-가군인 것이다. 만일 추가로 모든 affine open 위에서 $$M$$이 finitely presented 가군이 되도록 할 수 있다면, $$\mathcal{F}$$를 *coherent sheaf<sub>연접층</sub>*라 부른다.

</div>

Locally Noetherian scheme 위에서는 finitely generated와 finitely presented가 일치하므로, 이 경우 연접층은 곧 finite type 준연접층이다. $$X$$ 위의 연접층들은 $$\QCoh(X)$$의 full subcategory $$\Coh(X)$$를 이룬다. 가장 단순한 예시는 $$\mathcal{O}_X$$ 자기 자신으로, 이는 affine 위에서 $$\widetilde A$$이고 $$A$$는 자기 자신 위의 free 가군이므로 연접층이다.

## Ideal sheaf와 closed subscheme

준연접층의 중요한 예시로 ideal sheaf가 있다. Affine scheme $$\Spec A$$에서 ideal $$I\subseteq A$$는 그 자체로 $$A$$-가군이므로 연관층 $$\widetilde I$$를 정의하며, 이는 $$\mathcal{O}_{\Spec A}=\widetilde A$$의 부분 sheaf이다. 일반적인 scheme 위에서는 이를 다음과 같이 정의한다.

<div class="definition" markdown="1">

<ins id="def12">**정의 12**</ins> Scheme $$X$$ 위의 준연접층 $$\mathcal{I}$$가 *ideal sheaf<sub>아이디얼층</sub>*라는 것은, $$\mathcal{I}$$가 $$\mathcal{O}_X$$의 부분 $$\mathcal{O}_X$$-가군층인 것이다. 즉 각각의 열린집합 $$U$$에 대하여 $$\mathcal{I}(U)$$가 환 $$\mathcal{O}_X(U)$$의 ideal이며, restriction map과 호환되는 것이다.

</div>

Ideal sheaf는 자연스럽게 $$X$$의 닫힌 부분집합과 그 위의 scheme 구조를 결정한다. Affine 위에서 ideal $$I\subseteq A$$는 quotient ring $$A/I$$를 정의하며, $$\Spec A/I$$는 $$Z(I)\subseteq \Spec A$$ 위의 affine scheme이다. ([§스펙트럼](/ko/math/scheme_theory/spectrums)) 이를 붙여 다음을 얻는다.

<div class="proposition" markdown="1">

<ins id="prop13">**명제 13**</ins> Scheme $$X$$ 위의 ideal sheaf $$\mathcal{I}$$에 대하여, quotient sheaf $$\mathcal{O}_X/\mathcal{I}$$의 support

$$Y=\supp(\mathcal{O}_X/\mathcal{I})=\{x\in X\mid (\mathcal{O}_X/\mathcal{I})_x\neq 0\}$$

는 $$X$$의 닫힌 부분집합이며, $$(Y, (\mathcal{O}_X/\mathcal{I})\vert_Y)$$는 scheme이다. 더욱이 inclusion $$\iota:Y\hookrightarrow X$$는 scheme들 사이의 morphism이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

문제가 국소적이므로 $$X=\Spec A$$인 경우만 보이면 충분하다. [정리 9](#thm9)에 의하여 $$\mathcal{I}=\widetilde I$$인 ideal $$I\subseteq A$$가 존재한다. 그럼 [명제 6](#prop6)의 exactness로부터 short exact sequence

$$0 \rightarrow \widetilde I \rightarrow \widetilde A \rightarrow \widetilde{A/I} \rightarrow 0$$

를 얻으므로 $$\mathcal{O}_X/\mathcal{I}\cong \widetilde{A/I}$$이다. 이 sheaf의 stalk은 $$\mathfrak{p}$$에서 $$(A/I)_\mathfrak{p}$$이며, 이것이 $$0$$이 아닌 것은 $$\mathfrak{p}\supseteq I$$인 것과 동치이므로 ([\[가환대수학\] §국소화, ⁋명제 8](/ko/math/commutative_algebra/localization#prop8))

$$Y=\{\mathfrak{p}\mid \mathfrak{p}\supseteq I\}=Z(I)$$

이고, 이는 [§스펙트럼](/ko/math/scheme_theory/spectrums)에서 본 바와 같이 닫힌집합이다. 한편 canonical projection $$A \rightarrow A/I$$는 [§스펙트럼, ⁋명제 9](/ko/math/scheme_theory/spectrums#prop9)에 의하여 homeomorphism $$\Spec A/I\cong Z(I)$$를 주며, 이 위에서 $$(\mathcal{O}_X/\mathcal{I})\vert_Y\cong \mathcal{O}_{\Spec A/I}$$이므로 $$(Y, (\mathcal{O}_X/\mathcal{I})\vert_Y)\cong (\Spec A/I, \mathcal{O}_{\Spec A/I})$$는 affine scheme이다. 마지막으로 ring homomorphism $$A \rightarrow A/I$$가 유도하는 ([§아핀스킴, ⁋명제 9](/ko/math/scheme_theory/affine_schemes#prop9)) scheme morphism이 곧 inclusion $$\iota$$이다.

</details>

<div class="definition" markdown="1">

<ins id="def14">**정의 14**</ins> [명제 13](#prop13)에서 얻어지는 scheme $$(Y, \mathcal{O}_Y)$$ (단, $$\mathcal{O}_Y=(\mathcal{O}_X/\mathcal{I})\vert_Y$$)와 inclusion morphism $$\iota:Y\hookrightarrow X$$를 ideal sheaf $$\mathcal{I}$$가 정의하는 *closed subscheme<sub>닫힌 부분스킴</sub>*이라 부른다.

</div>

따라서 ideal sheaf와 closed subscheme은 서로 대응된다. Affine 위에서 이 대응은 ideal $$I\subseteq A$$와 quotient $$A/I$$ 사이의 대응에 다름 아니며, 특히 같은 닫힌 부분집합 $$Z(I)$$ 위에 서로 다른 scheme 구조를 줄 수 있다는 점이 중요하다. 예를 들어 $$I=(\x)$$와 $$I'=(\x^2)$$는 $$\mathbb{A}^1_\mathbb{K}$$ 위에서 같은 닫힌집합 $$\{0\}$$을 정의하지만, $$A/I=\mathbb{K}$$와 $$A/I'=\mathbb{K}[\x]/(\x^2)$$는 서로 다른 scheme 구조를 주며 후자는 nilpotent를 가진다.

## Locally free sheaf와 invertible sheaf

준연접층 가운데 국소적으로 free 가군에 대응하는 것들은 vector bundle의 대수기하학적 대응물로서 특히 중요하다.

<div class="definition" markdown="1">

<ins id="def15">**정의 15**</ins> Scheme $$X$$ 위의 $$\mathcal{O}_X$$-가군층 $$\mathcal{E}$$가 *locally free sheaf of rank $$r$$*라는 것은, 각 점 $$x\in X$$의 열린근방 $$U$$가 존재하여 $$\mathcal{E}\vert_U\cong \mathcal{O}_U^{\oplus r}$$인 것이다. Rank $$1$$인 locally free sheaf를 *invertible sheaf*라 부른다.

</div>

Locally free sheaf는 항상 준연접층이다. 실제로 각 점의 근방을 affine $$\Spec A$$로 줄이면 $$\mathcal{E}\vert_{\Spec A}\cong \mathcal{O}_{\Spec A}^{\oplus r}=\widetilde{A^{\oplus r}}$$이므로, 이는 free 가군 $$A^{\oplus r}$$의 연관층이다. 더욱이 finite rank이면 $$A^{\oplus r}$$이 finitely presented이므로 locally free sheaf는 연접층이기도 하다.

[\[대수다양체\] §선다발과 벡터다발, ⁋정의 23](/ko/math/algebraic_varieties/line_bundles#def23)에서 우리는 variety 위의 rank $$r$$ vector bundle을 정의하고, 그 section sheaf가 국소적으로 $$\mathcal{O}_X^{\oplus r}$$과 동형임을 보았다. ([\[대수다양체\] §선다발과 벡터다발, ⁋명제 5](/ko/math/algebraic_varieties/line_bundles#prop5)) Scheme의 언어에서 locally free sheaf는 정확히 이 vector bundle의 section sheaf에 대응하며, 특히 invertible sheaf는 line bundle에 대응한다. ([\[대수다양체\] §선다발과 벡터다발, ⁋정의 4](/ko/math/algebraic_varieties/line_bundles#def4)) 이름이 알려주듯, invertible sheaf는 tensor product에 대한 역원을 가진다.

<div class="proposition" markdown="1">

<ins id="prop16">**명제 16**</ins> Invertible sheaf $$\mathcal{L}$$에 대하여, $$\mathcal{L}^\vee=\sHom_{\mathcal{O}_X}(\mathcal{L}, \mathcal{O}_X)$$ 또한 invertible sheaf이며, $$\mathcal{L}\otimes_{\mathcal{O}_X}\mathcal{L}^\vee\cong \mathcal{O}_X$$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

문제가 국소적이므로 $$\mathcal{L}\vert_U\cong \mathcal{O}_U$$인 열린집합 $$U$$ 위에서 확인하면 충분하다. 그 위에서

$$\mathcal{L}^\vee\vert_U=\sHom_{\mathcal{O}_U}(\mathcal{O}_U, \mathcal{O}_U)\cong \mathcal{O}_U$$

이므로 $$\mathcal{L}^\vee$$는 invertible sheaf이다. 또한 $$U$$ 위에서

$$(\mathcal{L}\otimes_{\mathcal{O}_X}\mathcal{L}^\vee)\vert_U\cong \mathcal{O}_U\otimes_{\mathcal{O}_U}\mathcal{O}_U\cong \mathcal{O}_U$$

이고, 이 국소적 동형들이 자연스럽게 정의된 evaluation 사상 $$\mathcal{L}\otimes_{\mathcal{O}_X}\mathcal{L}^\vee \rightarrow \mathcal{O}_X$$로부터 오므로 ($$s\otimes \phi\mapsto \phi(s)$$) 이들이 붙어 전역적인 동형 $$\mathcal{L}\otimes_{\mathcal{O}_X}\mathcal{L}^\vee\cong \mathcal{O}_X$$를 준다.

</details>

따라서 invertible sheaf들은 tensor product를 연산으로 하여 group을 이루며, 항등원은 $$\mathcal{O}_X$$, $$\mathcal{L}$$의 역원은 $$\mathcal{L}^\vee$$이다. 이는 [\[대수다양체\] §선다발과 벡터다발, ⁋정의 9](/ko/math/algebraic_varieties/line_bundles#def9)에서 정의한 Picard group $$\Pic(X)$$의 scheme 버전이다.

## Pullback과 pushforward

마지막으로 scheme morphism을 따라 준연접층을 옮기는 두 연산을 살펴본다. Morphism $$f:X \rightarrow Y$$가 주어질 때, $$Y$$ 위의 sheaf를 $$X$$로 당기는 pullback과 $$X$$ 위의 sheaf를 $$Y$$로 미는 pushforward를 정의한다.

<div class="definition" markdown="1">

<ins id="def17">**정의 17**</ins> Scheme morphism $$f:X \rightarrow Y$$가 주어졌다 하자.

1. $$X$$ 위의 $$\mathcal{O}_X$$-가군층 $$\mathcal{F}$$에 대하여, *pushforward* $$f_\ast \mathcal{F}$$는 열린집합마다 $$V\mapsto \mathcal{F}(f^{-1}(V))$$로 주어지는 $$Y$$ 위의 $$\mathcal{O}_Y$$-가군층이다. 그 가군 구조는 morphism의 sheaf 사상 $$f^\sharp:\mathcal{O}_Y \rightarrow f_\ast \mathcal{O}_X$$을 통해 주어진다.
2. $$Y$$ 위의 $$\mathcal{O}_Y$$-가군층 $$\mathcal{G}$$에 대하여, *pullback* $$f^\ast \mathcal{G}$$는 다음 식

    $$f^\ast \mathcal{G}=f^{-1}\mathcal{G}\otimes_{f^{-1}\mathcal{O}_Y}\mathcal{O}_X$$

    으로 주어지는 $$X$$ 위의 $$\mathcal{O}_X$$-가군층이다. 여기에서 $$f^{-1}$$은 sheaf의 inverse image이다.

</div>

Pushforward의 경우 $$f_\ast \mathcal{F}(V)=\mathcal{F}(f^{-1}(V))$$가 sheaf 조건을 만족하는 것은 $$\mathcal{F}$$가 sheaf이기 때문이며, 그 가군 구조는 $$\mathcal{O}_Y(V) \rightarrow \mathcal{O}_X(f^{-1}(V))$$를 통해 scalar 작용을 옮긴 것이다. Pullback의 경우 inverse image sheaf $$f^{-1}\mathcal{G}$$는 $$f^{-1}\mathcal{O}_Y$$ 위의 가군이지만, $$\mathcal{O}_X$$와 tensor하여 $$\mathcal{O}_X$$ 위의 가군으로 만들어준 것이다. 이 두 연산은 affine 위에서 가군의 친숙한 연산으로 환원된다. $$f$$가 affine scheme들 사이의 morphism $$\Spec B \rightarrow \Spec A$$, 즉 ring homomorphism $$\phi:A \rightarrow B$$로부터 온다면, ([§아핀스킴, ⁋정리 13](/ko/math/scheme_theory/affine_schemes#thm13)) $$A$$-가군 $$M$$의 pullback은 base change $$\widetilde{M\otimes_A B}$$이고, $$B$$-가군 $$N$$의 pushforward는 $$N$$을 $$\phi$$를 통해 $$A$$-가군으로 본 restriction of scalars $$\widetilde{ {}_A N}$$이다.

이제 자연스러운 질문은 이 두 연산이 준연접성을 보존하는가이다. Pullback의 경우는 항상 보존되지만, pushforward의 경우는 추가 조건이 필요하다.

<div class="proposition" markdown="1">

<ins id="prop18">**명제 18**</ins> Scheme morphism $$f:X \rightarrow Y$$와 $$Y$$ 위의 준연접층 $$\mathcal{G}$$에 대하여, pullback $$f^\ast \mathcal{G}$$는 $$X$$ 위의 준연접층이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

준연접성이 affine-local property이므로 ([정리 10](#thm10)), $$X=\Spec B$$, $$Y=\Spec A$$인 경우에 대해 보이면 충분하다. 이 때 $$f$$는 ring homomorphism $$\phi:A \rightarrow B$$로부터 오며 ([§아핀스킴, ⁋명제 11](/ko/math/scheme_theory/affine_schemes#prop11)), $$\mathcal{G}=\widetilde M$$인 $$A$$-가군 $$M$$이 존재한다. ([정리 9](#thm9))

우리는 $$f^\ast \widetilde M\cong \widetilde{M\otimes_A B}$$임을 주장한다. 이를 보이기 위해 stalk을 비교한다. 임의의 $$\mathfrak{q}\in \Spec B$$와 $$\mathfrak{p}=\phi^{-1}(\mathfrak{q})$$에 대하여, inverse image와 tensor product가 stalk과 호환되므로

$$(f^\ast \widetilde M)_\mathfrak{q}=(f^{-1}\widetilde M)_\mathfrak{q}\otimes_{(f^{-1}\mathcal{O}_A)_\mathfrak{q}}\mathcal{O}_{B,\mathfrak{q}}\cong \widetilde M_\mathfrak{p}\otimes_{A_\mathfrak{p}}B_\mathfrak{q}\cong M_\mathfrak{p}\otimes_{A_\mathfrak{p}}B_\mathfrak{q}$$

이고, ([명제 5](#prop5)) 한편 base change 가군의 stalk은

$$(\widetilde{M\otimes_A B})_\mathfrak{q}=(M\otimes_A B)_\mathfrak{q}\cong M\otimes_A B_\mathfrak{q}\cong M_\mathfrak{p}\otimes_{A_\mathfrak{p}}B_\mathfrak{q}$$

이다. 이 동형들이 자연스러우므로 sheaf의 동형 $$f^\ast \widetilde M\cong \widetilde{M\otimes_A B}$$를 얻고, 따라서 $$f^\ast \mathcal{G}$$는 연관층이며 준연접층이다.

</details>

Pushforward의 경우 준연접성이 보존되려면 morphism이 quasi-compact이고 quasi-separated여야 한다. 이는 $$f_\ast \mathcal{F}(V)=\mathcal{F}(f^{-1}(V))$$를 affine 위에서 계산할 때, $$f^{-1}(V)$$를 유한히 많은 affine으로 덮고 그 교집합 또한 통제할 수 있어야 localization과 호환되는 가군 구조를 얻기 때문이다.

<div class="proposition" markdown="1">

<ins id="thm19">**정리 19**</ins> Quasi-compact이고 quasi-separated인 scheme morphism $$f:X \rightarrow Y$$와 $$X$$ 위의 준연접층 $$\mathcal{F}$$에 대하여, pushforward $$f_\ast \mathcal{F}$$는 $$Y$$ 위의 준연접층이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

준연접성이 affine-local property이므로 ([정리 10](#thm10)) $$Y=\Spec A$$인 경우만 보이면 충분하다. 이 때 $$f$$가 quasi-compact이므로 $$X$$는 유한히 많은 affine open subset $$U_i=\Spec B_i$$ ($$i=1,\ldots, n$$)으로 덮인다. 또 $$f$$가 quasi-separated이므로 각 $$U_i\cap U_j$$ 또한 유한히 많은 affine open $$U_{ijk}=\Spec C_{ijk}$$로 덮인다.

이제 $$M=\Gamma(X, \mathcal{F})=f_\ast \mathcal{F}(\Spec A)$$라 하고 $$f_\ast \mathcal{F}\cong \widetilde M$$임을 보이자. 그러려면 각 $$D(g)\subseteq \Spec A$$에 대하여 $$f_\ast \mathcal{F}(D(g))\cong M_g$$임을 확인하면 된다. 정의에 의하여 $$f_\ast \mathcal{F}(D(g))=\mathcal{F}(f^{-1}(D(g)))$$이며, sheaf 조건 ([§아핀스킴, ⁋보조정리 6](/ko/math/scheme_theory/affine_schemes#lem6) 이후 일반 sheaf의 sheaf axiom)으로부터 다음 equalizer

$$\mathcal{F}(f^{-1}(D(g)))=\ker\Bigl(\prod_i \mathcal{F}(U_i\cap f^{-1}(D(g))) \rightrightarrows \prod_{i,j,k}\mathcal{F}(U_{ijk}\cap f^{-1}(D(g)))\Bigr)$$

를 얻는다. 한편 $$U_i\cap f^{-1}(D(g))=\Spec (B_i)_{g}$$ 꼴의 principal open set이고, $$\mathcal{F}\vert_{U_i}$$가 준연접층이므로 $$\mathcal{F}(U_i)=N_i$$라 하면 [명제 5](#prop5)에 의하여

$$\mathcal{F}(U_i\cap f^{-1}(D(g)))=(N_i)_g\cong \mathcal{F}(U_i)\otimes_A A_g$$

이고, 같은 식이 $$U_{ijk}$$에 대해서도 성립한다. Localization $$(-)\otimes_A A_g$$은 exact functor이므로 ([\[가환대수학\] §국소화의 성질들, ⁋명제 2](/ko/math/commutative_algebra/properties_of_localization#prop2)) 위 equalizer와 commute하며, 유한 곱 위에서 정의되었으므로

$$\mathcal{F}(f^{-1}(D(g)))\cong \ker\Bigl(\prod_i N_i \rightrightarrows \prod_{i,j,k}\mathcal{F}(U_{ijk})\Bigr)\otimes_A A_g=M\otimes_A A_g=M_g$$

를 얻는다. 여기에서 유한성은 곱과 localization을 교환하는 데 본질적으로 사용되었으며, 이것이 quasi-compactness와 quasi-separatedness가 필요한 이유이다. 따라서 $$f_\ast \mathcal{F}(D(g))\cong M_g$$가 모든 $$g$$에 대해 성립하므로 $$f_\ast \mathcal{F}\cong \widetilde M$$이고, 이는 준연접층이다.

</details>

[정리 19](#thm19)의 quasi-compact, quasi-separated 조건은 본질적이다. 가령 무한히 많은 affine을 붙여야 하는 morphism에서는 $$f^{-1}(D(g))$$ 위의 section을 계산할 때 무한 곱이 등장하여 localization과의 교환이 깨질 수 있다. 한편 Noetherian scheme들 사이의 morphism이나, 특히 affine scheme들 사이의 morphism은 항상 이 조건을 만족하므로, 실용적으로 자주 마주치는 상황에서는 pushforward가 준연접성을 보존한다.

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate Texts in Mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundations of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).  
**[GW]** U. Görtz and T. Wedhorn, *Algebraic geometry I: Schemes*. Springer, 2020.  
**[Stacks]** The Stacks Project Authors, *The Stacks Project*. Available [online](https://stacks.math.columbia.edu/).
