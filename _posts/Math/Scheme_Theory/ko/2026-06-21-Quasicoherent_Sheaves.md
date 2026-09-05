---
title: "준연접층"
description: "스킴의 구조층 위에 정의되는 가군층을 도입하고, affine scheme 위에서 가군의 연관층이 가군 범주와 준연접층 범주 사이의 동치를 주는 것을 보인다. 이를 통해 준연접성이 affine-local property임을 확인하고 locally free sheaf, pullback과 pushforward, 그리고 closed subscheme의 ideal sheaf를 다룬다."
excerpt: "Sheaf of O_X-modules, the equivalence on affine schemes, and quasi-coherence"

categories: [Math / Scheme Theory]
permalink: /ko/math/scheme_theory/quasicoherent_sheaves
sidebar: 
    nav: "scheme_theory-ko"

date: 2026-06-21
weight: 16
drift_needed: true

---

Scheme $X$의 structure sheaf $\mathcal{O}_X$는 그 자체로 ring들의 sheaf이지만, 우리는 종종 $\mathcal{O}_X$ 위에서 정의된 module들의 sheaf를 다루어야 한다. 가령 affine scheme $\Spec A$ 위에서 우리가 관심을 가지는 대상들, 즉 $A$-module $M$은 $\Spec A$ 위의 sheaf로 변환되어야 자연스럽게 기하학과 연결되며, ideal sheaf나 line bundle 또한 이러한 sheaf의 예시이다. 그러나 임의의 $\mathcal{O}_X$-module은 너무 거칠어서 affine 위에서의 대수적인 정보로 환원되지 않는다. 이번 글에서는 affine 위에서 module로부터 직접 만들어지는 sheaf를 정의하고, 이로부터 *quasi-coherent sheaf*의 개념을 도입한다. 

## $\mathcal{O}_X$-module

우선 일반적인 ringed space $(X, \mathcal{O}_X)$ ([§아핀스킴, ⁋정의 1](/ko/math/scheme_theory/affine_schemes#def1)) 위에서 module들의 sheaf를 정의한다.

::: 정의 1
Ringed space $(X, \mathcal{O}_X)$ 위의 abelian group들의 sheaf $\mathcal{F}$가 *$\mathcal{O}_X$-module<sub>$\mathcal{O}_X$-가군층</sub>*이라는 것은, 임의의 열린집합 $U$에 대하여 $\mathcal{F}(U)$가 $\mathcal{O}_X(U)$-module의 구조를 가지며, 이 module 구조가 restriction map과 호환되는 것이다. 즉 $V\subseteq U$와 $a\in \mathcal{O}_X(U)$, $s\in \mathcal{F}(U)$에 대하여 

$$(a\cdot s)\vert_V=(a\vert_V)\cdot (s\vert_V)$$

가 성립하는 것이다. 두 $\mathcal{O}_X$-module $\mathcal{F}, \mathcal{G}$ 사이의 *morphism*은 sheaf 사이의 morphism $\varphi:\mathcal{F} \rightarrow \mathcal{G}$ 가운데, 각각의 $U$에 대하여 $\varphi(U):\mathcal{F}(U) \rightarrow \mathcal{G}(U)$가 $\mathcal{O}_X(U)$-module homomorphism인 것이다.
:::

즉 스칼라곱을 먼저 한 뒤 제한하는 것과 restriction을 먼저 한 뒤 스칼라곱을 하는 것이 일치한다는 것이 $\mathcal{O}_X$-module이며, 이 스칼라곱을 유지하는 것이 $\mathcal{O}_X$-module의 morphism이다. 이 데이터들은 $\mathcal{O}_X$-module들의 category를 이루며, 이를 $\rMod{\mathcal{O}_X}$로 적는다. 가장 기본적인 예시는 $\mathcal{O}_X$ 자기 자신으로, 이는 각각의 $\mathcal{O}_X(U)$를 그 위의 rank $1$ free module로 보아 얻어지는 $\mathcal{O}_X$-module이다. 뿐만 아니라 $\mathcal{O}_X$-module은 stalk 수준에서도 module 구조를 물려받는다. 즉, 임의의 $x\in X$에 대하여 stalk $\mathcal{F}_x=\varinjlim\mathcal{F}(U)$는 $\mathcal{O}_{X,x}=\varinjlim\mathcal{O}_X(U)$ 위의 module이 된다.

한편, 일반적인 module 위에서의 선형대수적 연산들은 $\mathcal{O}_X$-module에 그대로 옮겨진다.

::: 정의 2
두 $\mathcal{O}_X$-module $\mathcal{F}, \mathcal{G}$와 정수 $r\geq 0$에 대하여,

1. *Direct sum* $\mathcal{F}\oplus \mathcal{G}$는 열린집합마다 $U\mapsto \mathcal{F}(U)\oplus \mathcal{G}(U)$로 주어지는 $\mathcal{O}_X$-module이다.
2. *Tensor product* $\mathcal{F}\otimes_{\mathcal{O}_X}\mathcal{G}$는 presheaf $U\mapsto \mathcal{F}(U)\otimes_{\mathcal{O}_X(U)}\mathcal{G}(U)$의 sheafification이다.
3. *Sheaf Hom<sub>층 $\Hom$</sub>* $\sHom_{\mathcal{O}_X}(\mathcal{F}, \mathcal{G})$는 열린집합마다 $U\mapsto \Hom_{\mathcal{O}_X\vert_U}(\mathcal{F}\vert_U, \mathcal{G}\vert_U)$로 주어지는 $\mathcal{O}_X$-module이다.
4. *Exterior power* $\bigwedge^r\mathcal{F}$는 presheaf $U\mapsto \bigwedge^r_{\mathcal{O}_X(U)}\bigl(\mathcal{F}(U)\bigr)$의 sheafification이다. ([\[다중선형대수학\] §텐서대수, ⁋정의 10](/ko/math/multilinear_algebra/tensor_algebras#def10))
:::

위에서 direct sum과 sheaf Hom의 경우는 열린집합마다의 대응이 곧바로 sheaf를 이루지만, tensor product의 경우 presheaf 

$$U\mapsto \mathcal{F}(U)\otimes_{\mathcal{O}_X(U)}\mathcal{G}(U)$$

가 sheaf 조건을 만족하지 않을 수 있어 sheafification으로 정의하였다. ([\[위상수학\] §준층, ⁋정의 2](/ko/math/topology/presheaves#def2)) Exterior power도 같은 이유로 sheafification이 필요하다. Sheaf Hom $\sHom_{\mathcal{O}_X}(\mathcal{F}, \mathcal{G})$의 global section은 $\Hom_{\mathcal{O}_X}(\mathcal{F}, \mathcal{G})$이며, 특히 $\sHom_{\mathcal{O}_X}(\mathcal{O}_X, \mathcal{F})\cong \mathcal{F}$가 성립한다.

[정의 2](#def2)의 목록들은 앞으로 쓰게 될 것들일 뿐, module 위의 선형대수적 구성은 어느 것이나 같은 방식으로 옮겨진다. 곧 각 열린집합에서 $\mathcal{O}_X(U)$-module에 그 구성을 적용한 뒤, 얻어진 presheaf가 sheaf가 아니면 sheafification을 취하면 된다. 가령 tensor power $\mathcal{F}^{\otimes r}$과 symmetric power $\Sym^r\mathcal{F}$, 그리고 이들을 모두 모은 tensor algebra $\T(\mathcal{F})$와 symmetric algebra $\S(\mathcal{F})$, exterior algebra $\bigwedge\mathcal{F}$가 그러하며 ([\[다중선형대수학\] §텐서대수, ⁋정의 1](/ko/math/multilinear_algebra/tensor_algebras#def1)), 임의의 첨자집합에 대한 direct sum과 direct product도 마찬가지이다. 이렇듯 $\mathcal{O}_X$-module은 일반적인 module과 비슷한 형식적 성질을 가지지만, 그 자체로는 너무 일반적이어서 affine 위에서 대수적인 정보로 환원되지 않는다. 우리가 실제로 다루고자 하는 것은 affine 위에서 module로부터 직접 만들어지는 sheaf들이다.

## Affine scheme 위의 associated sheaf

이제 affine scheme $\Spec A$를 고정하고, $A$-module $M$이 주어졌다 하자. 우리는 $M$으로부터 $\Spec A$ 위의 $\mathcal{O}_{\Spec A}$-module을 만들고자 한다. 그 구성은 structure sheaf $\mathcal{O}_{\Spec A}$의 구성을 그대로 본뜬 것으로, structure sheaf가 principal open set $D(f)$ 위에서 localization $A_f$로 주어졌듯, module의 localization $M_f=S_f^{-1}M$을 같은 방식으로 붙인다. ([§아핀스킴, ⁋보조정리 6](/ko/math/scheme_theory/affine_schemes#lem6))

::: 보조정리 3
$A$-module $M$에 대하여, $\Spec A$의 base $\{D(f)\}_{f\in A}$ 위에서

$$\widetilde M(D(f))=M_f$$

으로 정의하고, $D(f)\subseteq D(g)$에 대한 restriction map을 canonical localization map $M_g \rightarrow M_f$로 정의하자. 그럼 이 데이터는 [\[위상수학\] §층, ⁋명제 8](/ko/math/topology/sheaves#prop8)의 두 조건을 만족하여 $\Spec A$ 위의 sheaf로 유일하게 확장되며, 이는 $\mathcal{O}_{\Spec A}$-module이다.
:::
::: 증명
우선 $D(f)\subseteq D(g)$일 때 restriction map이 잘 정의됨을 본다. [§아핀스킴, ⁋보조정리 5](/ko/math/scheme_theory/affine_schemes#lem5)와 같은 논증으로, $D(f)\subseteq D(g)$인 것은 $g$의 image가 $A_f$의 unit인 것과 동치이므로, $A_g$의 universal property로부터 $M_g=M\otimes_A A_g \rightarrow M\otimes_A A_f=M_f$가 유일하게 결정된다. 이 map이 [\[위상수학\] §준층, ⁋정의 2](/ko/math/topology/presheaves#def2)의 restriction 조건을 만족함은 localization의 functoriality로부터 자명하다.

이제 [\[위상수학\] §층, ⁋명제 8](/ko/math/topology/sheaves#prop8)의 두 sheaf 조건을 보인다. 그 증명은 [§아핀스킴, ⁋보조정리 6](/ko/math/scheme_theory/affine_schemes#lem6)의 증명을 그대로 따라가되, 등장하는 ring $A$를 module $M$으로 바꾸어 읽으면 된다. 구체적으로 $\Spec A=\bigcup_{i\in I}D(f_i)$를 고정하자. 분리성을 보이기 위해 원소 $s\in M$이 모든 $M_{f_i}$에서 $0$이라 하면, 각각의 $i$마다 $f_i^{m_i}s=0$인 $m_i$가 존재하고, $\Spec A=\bigcup D(f_i^{m_i})$로부터 $1=\sum a_i f_i^{m_i}$인 $a_i\in A$들을 잡으면

$$s=\Bigl(\sum_i a_if_i^{m_i}\Bigr)s=\sum_i a_i(f_i^{m_i}s)=0$$

이다. 접합성의 경우, 각 $D(f_i)$ 위에서 주어진 section들 $s_i=a_i/f_i^{m_i}\in M_{f_i}$가 겹치는 부분에서 일치하면, [§아핀스킴, ⁋보조정리 6](/ko/math/scheme_theory/affine_schemes#lem6)의 증명에서와 동일하게 $1=\sum b_i a_i f_i^{Nm_i+m_i}$ 꼴의 partition of unity를 사용하여 $s=\sum b_i a_i f_i^{Nm_i}\in M$이 모든 $D(f_i)$ 위에서 $s_i$로 제한됨을 확인한다. 이 논증에서 $A$의 곱셈을 $M$ 위로의 scalar action으로 바꾼 것을 제외하면 모든 계산이 동일하다.

마지막으로 각 $\widetilde M(D(f))=M_f$는 $\mathcal{O}_{\Spec A}(D(f))=A_f$ 위의 module이고, restriction map이 scalar action과 호환되므로 $\widetilde M$은 $\mathcal{O}_{\Spec A}$-module이다.
:::

::: 정의 4
$A$-module $M$에 대하여, [보조정리 3](#lem3)으로 정의되는 $\Spec A$ 위의 $\mathcal{O}_{\Spec A}$-module $\widetilde M$을 $M$의 *associated sheaf<sub>연관층</sub>*라 부른다.
:::

정의에 의하여 $\widetilde A=\mathcal{O}_{\Spec A}$이며, $\widetilde M$의 global section은 $\widetilde M(\Spec A)=\widetilde M(D(1))=M_1=M$이다. 다음 명제는 associated sheaf가 structure sheaf와 같은 국소적 성질을 가짐을 보여주며, 이는 [§아핀스킴, ⁋보조정리 8](/ko/math/scheme_theory/affine_schemes#lem8)의 module 버전이다.

::: 명제 5
$A$-module $M$에 대하여, 다음이 성립한다.

1. 임의의 $\mathfrak{p}\in \Spec A$에 대하여 stalk $\widetilde M_\mathfrak{p}\cong M_\mathfrak{p}$이다.
2. 임의의 $f\in A$에 대하여 $\widetilde M\vert_{D(f)}\cong \widetilde{M_f}$이다. 여기에서 우변은 $\Spec A_f\cong D(f)$ 위의 $A_f$-module $M_f$의 associated sheaf이다.
:::
::: 증명
첫째 결과의 경우, $D(f)$들이 $\Spec A$의 base이므로 ([\[위상수학\] §위상공간의 기저, ⁋명제 5](/ko/math/topology/topological_bases#prop5))

$$\widetilde M_\mathfrak{p}=\varinjlim_{D(f)\ni \mathfrak{p}}\widetilde M(D(f))=\varinjlim_{f\not\in \mathfrak{p}}M_f$$

이다. 한편 [§아핀스킴, ⁋보조정리 8](/ko/math/scheme_theory/affine_schemes#lem8)의 증명에서 $\varinjlim_{f\not\in \mathfrak{p}}A_f\cong A_\mathfrak{p}$를 보인 것과 동일하게, localization과 direct limit의 universal property로부터 $\varinjlim_{f\not\in \mathfrak{p}}M_f\cong M_\mathfrak{p}$를 얻는다.

둘째 결과의 경우, [§스킴, ⁋보조정리 2](/ko/math/scheme_theory/schemes#lem2)에 의하여 $D(f)\cong \Spec A_f$이고, 이 isomorphism 아래에서 $\Spec A_f$의 principal open set은 $g\in A$에 대한 $D(fg)$의 꼴이다. 그럼

$$\widetilde M\vert_{D(f)}(D(fg))=\widetilde M(D(fg))=M_{fg}\cong (M_f)_g=\widetilde{M_f}(D(g))$$

이고, 이 isomorphism들이 restriction map과 호환되므로 base 위에서 두 sheaf가 일치하며 따라서 $\widetilde M\vert_{D(f)}\cong \widetilde{M_f}$이다.
:::

특히 첫째 결과로부터 $\widetilde M$의 stalk은 모두 $M$의 localization으로 주어지므로, $\widetilde M$은 $M$의 국소적인 정보를 전부 담고 있다. 

## Categorical equivalence

이제 우리는 affine scheme 위에서 module의 associated sheaf를 취하는 대응이 module의 범주와 적절한 sheaf 범주 사이의 동치를 준다는 것을 보인다. 우선 이 대응이 exact functor임을 확인한다.

::: 명제 6
대응 $M\mapsto \widetilde M$은 functor $\widetilde{(-)}:\rMod{A} \rightarrow \rMod{\mathcal{O}_{\Spec A}}$를 정의하며, 이는 exact이다. 즉 $A$-module의 short exact sequence

$$0 \rightarrow M' \rightarrow M \rightarrow M'' \rightarrow 0$$

는 $\mathcal{O}_{\Spec A}$-module의 short exact sequence

$$0 \rightarrow \widetilde{M'} \rightarrow \widetilde M \rightarrow \widetilde{M''} \rightarrow 0$$

를 유도한다.
:::
::: 증명
$A$-module homomorphism $\phi:M \rightarrow N$이 주어지면, 각각의 $f\in A$마다 localization $\phi_f:M_f \rightarrow N_f$가 유도되고, 이들은 restriction map과 호환되므로 sheaf 사이의 morphism $\widetilde\phi:\widetilde M \rightarrow \widetilde N$을 정의한다. 이 대응이 합성과 항등사상을 보존함은 localization의 functoriality로부터 자명하므로 $\widetilde{(-)}$는 functor이다.

Exactness를 보이기 위해, sheaf 사이의 sequence가 exact인 것은 모든 stalk에서 exact인 것과 동치임을 사용한다. [명제 5](#prop5)에 의하여 임의의 $\mathfrak{p}$에서 stalk를 취하면 주어진 sequence는

$$0 \rightarrow M'_\mathfrak{p} \rightarrow M_\mathfrak{p} \rightarrow M''_\mathfrak{p} \rightarrow 0$$

가 되며, localization은 exact functor이므로 ([\[가환대수학\] §국소화의 성질들, ⁋명제 2](/ko/math/commutative_algebra/properties_of_localization#prop2)) 이 sequence는 exact이다. 따라서 stalk 수준에서 exact이고, 이로부터 sheaf 수준에서도 exact이다.
:::

Associated sheaf functor는 tensor product 및 localization과도 호환된다. 즉 $\widetilde{M\otimes_A N}\cong \widetilde M\otimes_{\mathcal{O}_{\Spec A}}\widetilde N$이고, 임의의 $f$에 대하여 [명제 5](#prop5)에서 본 $\widetilde M\vert_{D(f)}\cong \widetilde{M_f}$가 성립한다. 첫째 호환성은 양변의 stalk이 모두 $(M\otimes_A N)_\mathfrak{p}\cong M_\mathfrak{p}\otimes_{A_\mathfrak{p}}N_\mathfrak{p}$로 일치함으로부터 따라온다.

이제 이번 절의 결과인 categorical equivalence의 한 방향을 위해 우리는 임의의 $\mathcal{O}_{\Spec A}$-module이 어떻게 module로부터 복원되는지를 알아야 한다. 다음 정리가 핵심이다.

::: 정리 7
Affine scheme $\Spec A$ 위에서, 다음의 자연스러운 isomorphism

$$\Hom_{\mathcal{O}_{\Spec A}}(\widetilde M, \widetilde N)\cong \Hom_A(M, N)$$

이 임의의 $A$-module $M, N$에 대하여 성립한다. 즉 functor $\widetilde{(-)}:\rMod{A} \rightarrow \rMod{\mathcal{O}_{\Spec A}}$는 fully faithful이다.
:::
::: 증명
대응 $\phi\mapsto \widetilde\phi$는 [명제 6](#prop6)에 의하여 $\Hom_A(M, N) \rightarrow \Hom_{\mathcal{O}_{\Spec A}}(\widetilde M, \widetilde N)$를 준다. 거꾸로 morphism $\psi:\widetilde M \rightarrow \widetilde N$이 주어지면, global section 위에서

$$\psi(\Spec A):\widetilde M(\Spec A)=M \rightarrow N=\widetilde N(\Spec A)$$

를 취하여 $A$-module homomorphism $\phi=\psi(\Spec A)$를 얻는다. 이 두 대응이 서로 역임을 보이면 충분하다.

우선 $\phi\in \Hom_A(M, N)$에서 출발하면 $\widetilde\phi$의 global section은 정의에 의해 다시 $\phi$이므로 한 방향은 자명하다. 거꾸로 $\psi:\widetilde M \rightarrow \widetilde N$이 주어졌다 하고 $\phi=\psi(\Spec A)$라 하자. 우리는 $\widetilde \phi=\psi$임을 보여야 하며, 두 morphism이 일치하는 것은 base $\{D(f)\}$ 위에서 일치하는 것으로 충분하다. 임의의 $f\in A$에 대하여, $\psi$가 sheaf morphism이므로 다음 diagram

{% diagram Math/Scheme_Theory/Quasicoherent_Sheaves-1.svg width="6.60em" alt="localization square" %}

이 commute하며, 여기에서 세로 morphism은 localization map이다. 한편 $\psi(D(f))$는 $A_f$-module homomorphism이므로 윗줄의 $\phi$와 commute한다는 조건과 $A_f$-선형성에 의해 임의의 $m/f^n\in M_f$에 대하여

$$\psi(D(f))\Bigl(\frac{m}{f^n}\Bigr)=\frac{1}{f^n}\psi(D(f))\Bigl(\frac{m}{1}\Bigr)=\frac{1}{f^n}\frac{\phi(m)}{1}=\frac{\phi(m)}{f^n}=\widetilde\phi(D(f))\Bigl(\frac{m}{f^n}\Bigr)$$

으로 완전히 결정된다. 따라서 $\psi(D(f))=\widetilde\phi(D(f))$가 모든 $f$에 대해 성립하고, 이로부터 $\psi=\widetilde\phi$이다.
:::

[정리 7](#thm7)은 associated sheaf functor가 fully faithful임을 보여준다. 그러나 모든 $\mathcal{O}_{\Spec A}$-module이 associated sheaf의 꼴은 아니므로, 올바른 종류의 categorical equivalence를 얻기 위해서는 sheaf들의 category 쪽에서 적당한 제한이 필요하다. 

::: 정의 8
Scheme $X$ 위의 $\mathcal{O}_X$-module $\mathcal{F}$가 *quasi-coherent sheaf<sub>준연접층</sub>*라는 것은, 임의의 $x\in X$에 대하여 $x$의 affine open neighborhood $U\cong \Spec A$가 존재하여 적당한 $A$-module $M$에 대해 $\mathcal{F}\vert_U\cong \widetilde M$이도록 할 수 있는 것이다.
:::

즉 정의에 의해 quasi-coherent sheaf는 국소적으로 associated sheaf로 나타나는 것들이다. $X$ 위의 quasi-coherent sheaf들과 그 사이의 morphism들은 $\rMod{\mathcal{O}_X}$의 full subcategory를 이루며, 이를 $\QCoh(X)$로 적는다. 이로부터 [정리 7](#thm7)을 affine 위의 동치로 끌어올릴 수 있다.

::: 정리 9
Affine scheme $\Spec A$에 대하여, functor

$$\widetilde{(-)}:\rMod{A} \rightarrow \QCoh(\Spec A)$$

는 categorical equivalence이다.
:::
::: 증명
[정리 7](#thm7)에 의하여 $\widetilde{(-)}$는 fully faithful이므로, ([\[범주론\] §자연변환, ⁋정리 5](/ko/math/category_theory/natural_transformations#thm5)) essentially surjective임을 보이면 충분하다. 즉 임의의 quasi-coherent sheaf $\mathcal{F}\in \QCoh(\Spec A)$가 적당한 $A$-module의 associated sheaf와 isomorphic함을 보여야 한다.

$M=\mathcal{F}(\Spec A)$라 하고, 우리는 $\mathcal{F}\cong \widetilde M$임을 주장한다. Restriction map들로부터 각각의 $f\in A$마다 $M=\mathcal{F}(\Spec A) \rightarrow \mathcal{F}(D(f))$가 유도되고, 이 image가 $f$의 action에 대해 invertible하므로 $A_f$의 universal property에 의해 $A_f$-module homomorphism

$$\theta_f:M_f \rightarrow \mathcal{F}(D(f))$$

가 결정된다. 이들은 base $\{D(f)\}$ 위에서 morphism $\theta:\widetilde M \rightarrow \mathcal{F}$를 정의하므로, $\theta$가 stalk마다 isomorphic함을 보이면 된다.

이를 위해 $\mathcal{F}$의 quasi-coherence를 사용한다. 각 점 $\mathfrak{p}$에 대하여 $\mathfrak{p}\in D(g)$이고 $\mathcal{F}\vert_{D(g)}\cong \widetilde N$인 적당한 $g$와 $A_g$-module $N$이 존재한다. 이 때 [정의 8](#def8)에서 affine open neighborhood를 principal open set으로 줄일 수 있는 것은, [§스킴, ⁋보조정리 3](/ko/math/scheme_theory/schemes#lem3)의 증명에서와 같이 그 neighborhood 안에서 $\Spec A$의 principal open set이면서 동시에 그 neighborhood 자신의 principal open set이기도 한 근방을 잡을 수 있고, 그 위에서 [명제 5](#prop5)의 둘째 결과에 의하여 다시 associated sheaf가 되기 때문이다. 그럼 $N=\mathcal{F}(D(g))$이고, [명제 5](#prop5)에 의하여 $D(g)$ 위로 제한된 $\theta$는 $\widetilde{M_g} \rightarrow \widetilde N$의 꼴이다. 두 associated sheaf 사이의 morphism은 [정리 7](#thm7)에 의해 그 global section morphism으로 결정되므로, 이 restriction이 isomorphic한 것은 자연스러운 localization morphism $M_g=\mathcal{F}(\Spec A)_g \rightarrow \mathcal{F}(D(g))=N$이 isomorphic한 것과 같다. 이제 이 morphism이 isomorphic함을 확인한다. $\Spec A$가 quasi-compact이므로 그 위에서 $\mathcal{F}$가 associated sheaf가 되는 유한 개의 principal open $D(h_1),\ldots,D(h_m)$으로 $\Spec A$를 덮을 수 있고, sheaf 조건은 exact sequence

$$0 \rightarrow \mathcal{F}(\Spec A) \rightarrow \prod_i \mathcal{F}(D(h_i)) \rightarrow \prod_{i,j}\mathcal{F}(D(h_ih_j))$$

을 준다. 각 $D(h_i)$·$D(h_ih_j)$ 위에서 $\mathcal{F}$가 associated sheaf이라 그 section은 $A$-module이고 곱이 유한하므로, 완전한 localization $(-)\otimes_A A_g$은 이 열의 완전성을 보존할 뿐 아니라 곱을 통과한다. 그 결과 위 열을 $g$에서 localize한 것은 covering $\{D(h_ig)\}$에 대한 $D(g)$ 위의 sheaf 조건과 정확히 일치하는 exact sequence가 되어 $M_g\cong \mathcal{F}(D(g))=N$을 얻는다. 여기서 $\Spec A$의 quasi-compactness가 finite covering을 보장하는 데 본질적으로 쓰였다. 따라서 $\theta$는 각 $D(g)$ 위에서 isomorphic하고, 이로부터 모든 stalk에서 isomorphic하므로 $\theta:\widetilde M \rightarrow \mathcal{F}$는 sheaf의 isomorphism이다.
:::

[정리 9](#thm9)는 affine scheme 위에서 quasi-coherent sheaf를 다루는 것이 곧 module을 다루는 것과 같음을 말해준다. 즉 $\Spec A$ 위의 모든 quasi-coherent sheaf는 그 global section module $M=\Gamma(\Spec A, \mathcal{F})$으로 완전히 복원되며, 이 대응은 [명제 6](#prop6)의 exactness와 위에서 언급한 tensor product와의 호환성을 통해 module의 대수와 sheaf의 대수를 일치시킨다.

## Quasi-coherence의 affine-local 성질

[정의 8](#def8)이 요구하는 것은 각 점마다 적절한 affine open neighborhood를 하나 찾아 그 위에서 associated sheaf임을 확인하는 것뿐이다. 그런데 다음 정리가 보여주듯 이 조건은 훨씬 강한 성질, 곧 $X$의 임의의 affine open subset 위에서 associated sheaf가 된다는 것을 함의한다. 이러한 의미에서 quasi-coherence는 affine-local property이다.

::: 정리 10
Scheme $X$ 위의 $\mathcal{O}_X$-module $\mathcal{F}$에 대하여 다음이 동치이다.

1. $\mathcal{F}$는 quasi-coherent sheaf이다.
2. $X$의 모든 affine open subset $U\cong \Spec A$에 대하여, $A$-module $M_U=\mathcal{F}(U)$의 associated sheaf가 $\mathcal{F}\vert_U\cong \widetilde{M_U}$를 준다.
:::
::: 증명
둘째 조건이 첫째 조건을 함의하는 것은 [정의 8](#def8)로부터 자명하므로 그 역을 보인다. $\mathcal{F}$가 quasi-coherent sheaf라 하고, 임의의 affine open subset $U=\Spec A$를 고정하자. 우리는 $\mathcal{F}\vert_U$가 $\Spec A$ 위의 quasi-coherent sheaf임을 보이면 [정리 9](#thm9)에 의해 $\mathcal{F}\vert_U\cong \widetilde{M_U}$ (단, $M_U=\mathcal{F}(U)$)가 따라온다.

$\mathcal{F}$의 quasi-coherence에 의하여 $U$의 각 점 $x$마다 ($X$에서의) affine open neighborhood $V\cong \Spec B$와 $B$-module $N$이 존재하여 $\mathcal{F}\vert_V\cong \widetilde N$이다. [§스킴, ⁋보조정리 3](/ko/math/scheme_theory/schemes#lem3)의 증명에서와 같이, $U\cap V$는 $U$ 안에서 principal open set들 $D(f)$ ($f\in A$)로 덮이며, 또 $V$ 안에서도 principal open set $D(g)$ ($g\in B$)로 덮인다. 이 둘을 동시에 만족하도록 충분히 작게 잡으면, $x$를 포함하고 $U$와 $V$ 양쪽의 principal open set이 되는 affine open $W=\Spec A_f=\Spec B_g$를 얻는다.

이제 $\mathcal{F}\vert_V\cong \widetilde N$이므로 [명제 5](#prop5)에 의하여 $\mathcal{F}\vert_W\cong \widetilde N\vert_{D(g)}\cong \widetilde{N_g}$이고, $W=\Spec A_f$로 보면 이는 $A_f$-module $N_g$의 associated sheaf이다. 따라서 $U=\Spec A$의 각 점은 $\mathcal{F}\vert_U$가 associated sheaf가 되는 principal open neighborhood를 가지며, 이로부터 $\mathcal{F}\vert_U$는 $\Spec A$ 위의 quasi-coherent sheaf이다.
:::

따라서 어떤 한 affine cover 위에서 associated sheaf임을 확인하는 것만으로 quasi-coherence가 보장되며, 그 결과 모든 affine open subset 위에서 자동으로 associated sheaf가 된다. 이 affine-locality 덕분에 quasi-coherent sheaf에 대한 많은 명제들은 associated sheaf에 대한 명제로 환원하여 증명할 수 있다.

Quasi-coherent sheaf 가운데 특히 affine 위에서 finitely generated module 또는 finitely presented module에 대응하는 것들을 따로 구별한다. 이는 Noetherian 가정 아래에서 가장 잘 작동한다.

::: 정의 11
Scheme $X$ 위의 quasi-coherent sheaf $\mathcal{F}$가 *finite type<sub>유한형</sub>*이라는 것은, 각 점이 affine open neighborhood $U\cong \Spec A$를 가져 $\mathcal{F}\vert_U\cong \widetilde M$이고 $M$이 finitely generated $A$-module인 것이다. 만일 추가로 각 점이 이러한 affine open neighborhood를 가지며 이들 각각에서 $M$을 finitely presented $A$-module로 잡을 수 있다면, $\mathcal{F}$를 *coherent sheaf<sub>연접층</sub>*라 부른다.
:::

Locally Noetherian scheme 위에서는 finitely generated와 finitely presented가 일치하므로, 이 경우 coherent sheaf는 곧 finite type quasi-coherent sheaf이다. $X$ 위의 coherent sheaves는 $\QCoh(X)$의 full subcategory $\Coh(X)$를 이룬다. 가장 단순한 예시는 $\mathcal{O}_X$ 자기 자신으로, 이는 affine 위에서 $\widetilde A$이고 $A$는 자기 자신 위의 free module이므로 coherent sheaf이다.

Finite type 조건은 한 점에서의 생성을 그 근방으로 퍼뜨린다. $\mathcal{F}$가 finite type이고 [정의 11](#def11)이 주는 affine open neighborhood $U=\Spec A$ 위에서 $\mathcal{F}\vert_U\cong\widetilde M$이라 하자. 점 $x\in U$에 대응하는 prime을 $\mathfrak{p}$라 할 때 $m_1,\ldots, m_r\in M$의 image가 stalk $M_\mathfrak{p}$를 생성한다 하면, $N=M/\sum_iAm_i$는 finitely generated이면서 $N_\mathfrak{p}=0$이므로 $N$의 각 generator를 소멸시키는 $\mathfrak{p}$ 밖의 원소가 존재하고, $\mathfrak{p}$가 prime이라 이들의 곱 $f$ 또한 $\mathfrak{p}$에 속하지 않아 $fN=0$에서 $N_f=0$이다. 곧 stalk을 생성하는 section들은 언제나 그 점의 근방 $D(f)$ 위에서 $\mathcal{F}$ 전체를 생성한다.

## Locally free sheaf와 invertible sheaf

Quasi-coherent sheaf 가운데 국소적으로 free module에 대응하는 것들은 vector bundle의 대수기하학적 대응물로서 특히 중요하다.

::: 정의 12
Scheme $X$ 위의 $\mathcal{O}_X$-module $\mathcal{E}$가 *locally free sheaf of rank $r$<sub>랭크 $r$ 국소 자유층</sub>*라는 것은, 각 점 $x\in X$의 열린근방 $U$가 존재하여 $\mathcal{E}\vert_U\cong \mathcal{O}_U^{\oplus r}$인 것이다. Rank $1$인 locally free sheaf를 *invertible sheaf<sub>가역층</sub>*라 부른다.
:::

Locally free sheaf는 항상 quasi-coherent sheaf이다. 실제로 각 점의 근방을 affine $\Spec A$로 줄이면 $\mathcal{E}\vert_{\Spec A}\cong \mathcal{O}_{\Spec A}^{\oplus r}=\widetilde{A^{\oplus r}}$이므로, 이는 free module $A^{\oplus r}$의 associated sheaf이다. 더욱이 finite rank이면 $A^{\oplus r}$이 finitely presented이므로 locally free sheaf는 coherent sheaf이기도 하다.

[\[대수다양체\] §선다발과 벡터다발, ⁋정의 23](/ko/math/algebraic_varieties/line_bundles#def23)에서 우리는 variety 위의 rank $r$ vector bundle을 local trivialization의 데이터로 정의하였고, rank $1$의 경우 그 section sheaf가 invertible sheaf임을 보았다. ([\[대수다양체\] §선다발과 벡터다발, ⁋명제 5](/ko/math/algebraic_varieties/line_bundles#prop5)) 일반적인 rank에서도 local trivialization이 section sheaf를 각 $U_i$ 위에서 $\mathcal{O}_{U_i}^{\oplus r}$로 만들어 주므로, scheme의 언어에서 locally free sheaf는 정확히 이 vector bundle의 section sheaf에 대응하며 특히 invertible sheaf는 line bundle에 대응한다. ([\[대수다양체\] §선다발과 벡터다발, ⁋정의 1](/ko/math/algebraic_varieties/line_bundles#def1)) 이름이 알려주듯, invertible sheaf는 tensor product에 대한 역원을 가진다.

Vector bundle의 각 점 위의 fiber에 해당하는 것도 sheaf의 언어로 그대로 옮겨진다. $\mathcal{O}_X$-module $\mathcal{F}$와 점 $x\in X$에 대하여, [§스킴](/ko/math/scheme_theory/schemes)에서 정의한 residue field $\kappa(x)=\mathcal{O}_{X,x}/\mathfrak{m}_x$를 사용하여 $\mathcal{F}$의 $x$에서의 *fiber*를

$$\mathcal{F}\otimes\kappa(x)=\mathcal{F}_x\otimes_{\mathcal{O}_{X,x}}\kappa(x)=\mathcal{F}_x/\mathfrak{m}_x\mathcal{F}_x$$

로 정의한다. 이는 stalk과 구별되는 대상인데, stalk $\mathcal{F}_x$가 $x$ 주위의 germ을 모두 기억하는 $\mathcal{O}_{X,x}$-module인 데 반해 fiber는 그것을 maximal ideal로 내려 그 점에서의 값만 남긴 $\kappa(x)$-vector space이기 때문이다. 가령 $\mathcal{O}_X$의 stalk은 local ring $\mathcal{O}_{X,x}$ 전체이지만 그 fiber는 $\kappa(x)$이며, $\mathcal{E}$가 rank $r$의 locally free sheaf이면 이를 trivialize하는 근방 위에서 stalk이 $\mathcal{O}_{X,x}^{\oplus r}$이고 fiber가 $\kappa(x)^{\oplus r}$이 되어 대응하는 vector bundle의 $x$ 위 fiber를 그대로 준다. 물론 일반적인 quasi-coherent sheaf에서는 fiber의 차원이 점을 옮겨다닐 때 변할 수 있으며, affine 위의 finitely generated module에 대하여 이 차원이 upper semicontinuous하다는 것이 [§평탄사상, ⁋명제 22](/ko/math/scheme_theory/flat_morphisms#prop22)이다.

::: 명제 13
Invertible sheaf $\mathcal{L}$에 대하여, $\mathcal{L}^\vee=\sHom_{\mathcal{O}_X}(\mathcal{L}, \mathcal{O}_X)$ 또한 invertible sheaf이며, $\mathcal{L}\otimes_{\mathcal{O}_X}\mathcal{L}^\vee\cong \mathcal{O}_X$이다.
:::
::: 증명
문제가 국소적이므로 $\mathcal{L}\vert_U\cong \mathcal{O}_U$인 열린집합 $U$ 위에서 확인하면 충분하다. 그 위에서

$$\mathcal{L}^\vee\vert_U=\sHom_{\mathcal{O}_U}(\mathcal{O}_U, \mathcal{O}_U)\cong \mathcal{O}_U$$

이므로 $\mathcal{L}^\vee$는 invertible sheaf이다. 또한 $U$ 위에서

$$(\mathcal{L}\otimes_{\mathcal{O}_X}\mathcal{L}^\vee)\vert_U\cong \mathcal{O}_U\otimes_{\mathcal{O}_U}\mathcal{O}_U\cong \mathcal{O}_U$$

이고, 이 국소적 isomorphism들이 자연스럽게 정의된 evaluation morphism $\mathcal{L}\otimes_{\mathcal{O}_X}\mathcal{L}^\vee \rightarrow \mathcal{O}_X$로부터 오므로 ($s\otimes \phi\mapsto \phi(s)$) 이들이 붙어 전역적인 isomorphism $\mathcal{L}\otimes_{\mathcal{O}_X}\mathcal{L}^\vee\cong \mathcal{O}_X$를 준다.
:::

따라서 invertible sheaf들은 tensor product를 연산으로 하여 group을 이루며, 항등원은 $\mathcal{O}_X$, $\mathcal{L}$의 역원은 $\mathcal{L}^\vee$이다. 이는 [\[대수다양체\] §선다발과 벡터다발, ⁋정의 9](/ko/math/algebraic_varieties/line_bundles#def9)에서 정의한 Picard group $\Pic(X)$의 scheme 버전이다.

Invertible sheaf를 얻는 가장 중요한 방법 중 하나는 locally free sheaf에 exterior power를 취하는 것이다. 우선 exterior power는 base change와 commute하므로 ([\[다중선형대수학\] §텐서대수, ⁋명제 14](/ko/math/multilinear_algebra/tensor_algebras#prop14)) $A$-module $M$과 $g\in A$에 대하여 $\bigl(\bigwedge^rM\bigr)_g\cong \bigwedge^r(M_g)$이고, 따라서 $U=\Spec A$ 위에서 $\mathcal{F}\vert_U\cong \widetilde M$이면 local model들이 restriction과 호환되어

$$\bigl(\bigwedge\nolimits^r\mathcal{F}\bigr)\big\vert_U\cong \widetilde{\bigwedge\nolimits^rM}$$

이 성립한다. ([명제 5](#prop5)) 그러므로 quasi-coherent sheaf의 exterior power는 다시 quasi-coherent sheaf이다. 

특히 $\mathcal{E}$가 rank $n$의 locally free sheaf이면, $\mathcal{E}\vert_U\cong \mathcal{O}_U^{\oplus n}$인 열린집합 $U$ 위에서 $\bigwedge^r\mathcal{E}\vert_U$는 basis $e_1,\ldots, e_n$으로부터 만들어지는 $e_J$ ($\lvert J\rvert=r$)들을 basis로 가지므로 ([\[다중선형대수학\] §텐서대수, ⁋명제 13](/ko/math/multilinear_algebra/tensor_algebras#prop13)) rank $\binom{n}{r}$ free sheaf이다. 즉 $\bigwedge^r\mathcal{E}$는 다시 locally free sheaf이며, $r=n$인 경우에는 rank $1$, 곧 invertible sheaf가 된다. 이 마지막 경우를 $\mathcal{E}$의 *determinant*라 부르고 $\det\mathcal{E}=\bigwedge^n\mathcal{E}$로 적는다. 그러므로 rank $n$의 locally free sheaf는 그 determinant를 통해 $\Pic(X)$의 원소를 하나 정한다.

## Pullback과 pushforward

이제 scheme morphism을 따라 quasi-coherent sheaf를 옮기는 두 연산을 살펴본다. Morphism $\varphi:X \rightarrow Y$가 주어질 때, $Y$ 위의 sheaf를 $X$로 당기는 pullback과 $X$ 위의 sheaf를 $Y$로 미는 pushforward를 정의한다.

::: 정의 14
Scheme morphism $\varphi:X \rightarrow Y$가 주어졌다 하자.

1. $X$ 위의 $\mathcal{O}_X$-module $\mathcal{F}$에 대하여, *pushforward* $\varphi_\ast \mathcal{F}$는 열린집합마다 $V\mapsto \mathcal{F}(\varphi^{-1}(V))$로 주어지는 $Y$ 위의 $\mathcal{O}_Y$-module이다. ([\[위상수학\] §준층, ⁋예시 8](/ko/math/topology/presheaves#ex8)) 그 module 구조는 morphism의 sheaf morphism $\varphi^\sharp:\mathcal{O}_Y \rightarrow \varphi_\ast \mathcal{O}_X$을 통해 주어진다.
2. $Y$ 위의 $\mathcal{O}_Y$-module $\mathcal{G}$에 대하여, *pullback* $\varphi^\ast \mathcal{G}$는 다음 식

    $$\varphi^\ast \mathcal{G}=\varphi^{-1}\mathcal{G}\otimes_{\varphi^{-1}\mathcal{O}_Y}\mathcal{O}_X$$

    으로 주어지는 $X$ 위의 $\mathcal{O}_X$-module이다. 여기에서 $\varphi^{-1}$은 [\[위상수학\] §층, ⁋정의 10](/ko/math/topology/sheaves#def10)의 inverse image sheaf이다.
:::

두 연산 모두 affine 위에서는 module의 친숙한 연산으로 환원된다. $\varphi$가 affine scheme들 사이의 morphism $\Spec B \rightarrow \Spec A$, 즉 ring homomorphism $\phi:A \rightarrow B$로부터 온다면, $A$-module $M$의 pullback은 extension of scalars $\widetilde{M\otimes_A B}$이고 $B$-module $N$의 pushforward는 restriction of scalars $\widetilde{\phi^\ast N}$이다. ([\[대수적 구조\] §스칼라의 변환, ⁋정의 1](/ko/math/algebraic_structures/change_of_base_ring#def1), [스칼라의 변환, ⁋정의 3](/ko/math/algebraic_structures/change_of_base_ring#def3)) 그럼 [\[대수적 구조\] §스칼라의 변환, ⁋명제 6](/ko/math/algebraic_structures/change_of_base_ring#prop6)의 adjoint $\phi_!\dashv \phi^\ast$가 그대로 $\varphi^\ast\dashv \varphi_\ast$로 옮겨진다.

이제 자연스러운 질문은 이 두 연산이 quasi-coherence를 보존하는가이며, 이에 대한 대답은 두 연산에 따라 갈린다. 즉 pullback의 경우는 항상 보존되지만, pushforward의 경우는 추가 조건이 필요하다. 직관적으로 이는 quasi-coherence가 affine chart 위에서는 free $\mathcal{O}_X$-module의 presentation 

$$\mathcal{O}^{(J)} \rightarrow \mathcal{O}^{(I)} \rightarrow \mathcal{F} \rightarrow 0$$ 

꼴로 나오는데, $\varphi^\ast$는 left adjoint이므로 direct sum과 cokernel을 보존하므로 이러한 presentation을 그대로 옮기는 반면 right adjoint인 $\varphi_\ast$는 그렇지 않기 때문이다.

::: 명제 15
Scheme morphism $\varphi:X \rightarrow Y$와 $Y$ 위의 quasi-coherent sheaf $\mathcal{G}$에 대하여, pullback $\varphi^\ast \mathcal{G}$는 $X$ 위의 quasi-coherent sheaf이다.
:::
::: 증명
quasi-coherence가 affine-local property이므로 ([정리 10](#thm10)), $X=\Spec B$, $Y=\Spec A$인 경우에 대해 보이면 충분하다. 이 때 $\varphi$는 ring homomorphism $\phi:A \rightarrow B$로부터 오며 ([§아핀스킴, ⁋명제 11](/ko/math/scheme_theory/affine_schemes#prop11)), $\mathcal{G}=\widetilde M$인 $A$-module $M$이 존재한다. ([정리 9](#thm9))

우리는 $\varphi^\ast \widetilde M\cong \widetilde{M\otimes_A B}$임을 주장한다. 이를 보이기 위해 stalk을 비교한다. 임의의 $\mathfrak{q}\in \Spec B$와 $\mathfrak{p}=\phi^{-1}(\mathfrak{q})$에 대하여, inverse image와 tensor product가 stalk과 호환되므로

$$(\varphi^\ast \widetilde M)_\mathfrak{q}=(\varphi^{-1}\widetilde M)_\mathfrak{q}\otimes_{(\varphi^{-1}\mathcal{O}_{\Spec A})_\mathfrak{q}}\mathcal{O}_{\Spec B,\mathfrak{q}}\cong \widetilde M_\mathfrak{p}\otimes_{A_\mathfrak{p}}B_\mathfrak{q}\cong M_\mathfrak{p}\otimes_{A_\mathfrak{p}}B_\mathfrak{q}$$

이고, ([명제 5](#prop5)) 한편 base change module의 stalk은

$$(\widetilde{M\otimes_A B})_\mathfrak{q}=(M\otimes_A B)_\mathfrak{q}\cong M\otimes_A B_\mathfrak{q}\cong M_\mathfrak{p}\otimes_{A_\mathfrak{p}}B_\mathfrak{q}$$

이다. 이 isomorphism들이 자연스러우므로 sheaf의 isomorphism $\varphi^\ast \widetilde M\cong \widetilde{M\otimes_A B}$를 얻고, 따라서 $\varphi^\ast \mathcal{G}$는 associated sheaf이며 quasi-coherent sheaf이다.
:::

Pushforward의 경우 quasi-coherence가 보존되려면 morphism이 quasi-compact이고 quasi-separated여야 한다. 이는 $\varphi_\ast \mathcal{F}(V)=\mathcal{F}(\varphi^{-1}(V))$를 affine 위에서 계산할 때, $\varphi^{-1}(V)$를 유한히 많은 affine으로 덮고 그 교집합 또한 통제할 수 있어야 localization과 호환되는 module 구조를 얻기 때문이다.

::: 정리 16
Quasi-compact이고 quasi-separated인 scheme morphism $\varphi:X \rightarrow Y$와 $X$ 위의 quasi-coherent sheaf $\mathcal{F}$에 대하여, pushforward $\varphi_\ast \mathcal{F}$는 $Y$ 위의 quasi-coherent sheaf이다.
:::
::: 증명
Quasi-coherence가 affine-local property이므로 ([정리 10](#thm10)) $Y=\Spec A$인 경우만 보이면 충분하다. 이 때 $\varphi$가 quasi-compact이므로 $X$는 유한히 많은 affine open subset $U_i=\Spec B_i$ ($i=1,\ldots, n$)으로 덮인다. 또 $\varphi$가 quasi-separated이므로 각 $U_i\cap U_j$ 또한 유한히 많은 affine open $U_{ijk}=\Spec C_{ijk}$로 덮인다.

이제 $M=\Gamma(X, \mathcal{F})=\varphi_\ast \mathcal{F}(\Spec A)$라 하고 $\varphi_\ast \mathcal{F}\cong \widetilde M$임을 보이자. 그러려면 각 $D(g)\subseteq \Spec A$에 대하여 $\varphi_\ast \mathcal{F}(D(g))\cong M_g$임을 확인하면 된다. 정의에 의하여 $\varphi_\ast \mathcal{F}(D(g))=\mathcal{F}(\varphi^{-1}(D(g)))$이며, sheaf 조건 ([§아핀스킴, ⁋보조정리 6](/ko/math/scheme_theory/affine_schemes#lem6) 이후 일반 sheaf의 sheaf axiom)으로부터 다음 equalizer

$$\mathcal{F}(\varphi^{-1}(D(g)))=\ker\Bigl(\prod_i \mathcal{F}(U_i\cap \varphi^{-1}(D(g))) \rightrightarrows \prod_{i,j,k}\mathcal{F}(U_{ijk}\cap \varphi^{-1}(D(g)))\Bigr)$$

를 얻는다. 한편 $U_i\cap \varphi^{-1}(D(g))=\Spec (B_i)_{g}$ 꼴의 principal open set이고, $\mathcal{F}\vert_{U_i}$가 quasi-coherent sheaf이므로 $\mathcal{F}(U_i)=N_i$라 하면 [명제 5](#prop5)에 의하여

$$\mathcal{F}(U_i\cap \varphi^{-1}(D(g)))=(N_i)_g\cong \mathcal{F}(U_i)\otimes_A A_g$$

이고, 같은 식이 $U_{ijk}$에 대해서도 성립한다. Localization $(-)\otimes_A A_g$은 exact functor이므로 ([\[가환대수학\] §국소화의 성질들, ⁋명제 2](/ko/math/commutative_algebra/properties_of_localization#prop2)) 위 equalizer와 commute하며, 유한 곱 위에서 정의되었으므로

$$\mathcal{F}(\varphi^{-1}(D(g)))\cong \ker\Bigl(\prod_i N_i \rightrightarrows \prod_{i,j,k}\mathcal{F}(U_{ijk})\Bigr)\otimes_A A_g=M\otimes_A A_g=M_g$$

를 얻는다. 여기에서 유한성은 곱과 localization이 commute하는 데 본질적으로 사용되었으며, 이것이 quasi-compactness와 quasi-separatedness가 필요한 이유이다. 따라서 $\varphi_\ast \mathcal{F}(D(g))\cong M_g$가 모든 $g$에 대해 성립하므로 $\varphi_\ast \mathcal{F}\cong \widetilde M$이고, 이는 quasi-coherent sheaf이다.
:::

[정리 16](#thm16)의 quasi-compact, quasi-separated 조건은 본질적이다. 가령 무한히 많은 affine을 붙여야 하는 morphism에서는 $\varphi^{-1}(D(g))$ 위의 section을 계산할 때 무한 곱이 등장하여 localization과 commute하지 않을 수 있다. 다만 Noetherian scheme들 사이의 morphism이나, 특히 affine scheme들 사이의 morphism은 항상 이 조건을 만족하므로, 실용적으로 자주 마주치는 상황에서는 pushforward가 quasi-coherence를 보존한다.

마지막으로 pushforward가 tensor product와 어떻게 호환되는지를 본다. 일반적으로 $\varphi_\ast$는 tensor product를 보존하지 않지만, 두 인자 가운데 하나가 base 위의 locally free sheaf를 당겨온 것이라면 그 인자를 $\varphi_\ast$ 밖으로 빼낼 수 있다.

::: 명제 17 (Projection formula)
Scheme morphism $\varphi:X \rightarrow Y$와 $X$ 위의 quasi-coherent sheaf $\mathcal{F}$, 그리고 $Y$ 위의 finite rank locally free sheaf $\mathcal{L}$에 대하여 ([정의 12](#def12)) isomorphism

$$\varphi_\ast(\mathcal{F}\otimes_{\mathcal{O}_X}\varphi^\ast \mathcal{L})\cong \varphi_\ast \mathcal{F}\otimes_{\mathcal{O}_Y}\mathcal{L}$$

이 성립한다.
:::
::: 증명
먼저 임의의 $\mathcal{O}_Y$-module $\mathcal{L}$에 대하여 자연스러운 사상을 만든다. [정의 14](#def14)의 pullback은 $\varphi^{-1}$과 $\mathcal{O}_X$로의 base change의 합성이므로 tensor product와 commute하며, 따라서 adjunction $\varphi^\ast\dashv \varphi_\ast$의 counit $\varepsilon:\varphi^\ast\varphi_\ast \mathcal{F} \rightarrow \mathcal{F}$과 함께

$$\varphi^\ast(\varphi_\ast \mathcal{F}\otimes \mathcal{L})\cong \varphi^\ast\varphi_\ast \mathcal{F}\otimes \varphi^\ast \mathcal{L}\xrightarrow{\varepsilon\otimes\id}\mathcal{F}\otimes \varphi^\ast \mathcal{L}$$

를 얻는다. 이 사상의 adjoint가 우리가 원하는 $\theta:\varphi_\ast \mathcal{F}\otimes \mathcal{L} \rightarrow \varphi_\ast(\mathcal{F}\otimes \varphi^\ast \mathcal{L})$이며, 이는 $\mathcal{L}$의 선택에 대해 natural하다.

이제 $\mathcal{L}$이 finite rank locally free일 때 $\theta$가 isomorphism임을 보인다. Pushforward는 base의 열린집합으로의 제한과 commute하므로, 곧 $\varphi_\ast \mathcal{G}\vert_V$는 $\varphi^{-1}(V) \rightarrow V$에 대한 pushforward이므로, isomorphism 여부는 $Y$를 덮는 열린집합들 위에서 확인하면 충분하다. 가정에 의하여 $\mathcal{L}\vert_V\cong \mathcal{O}_V^{\oplus r}$인 열린집합 $V$들이 $Y$를 덮고, 이러한 $V$ 위에서 $\varphi^\ast \mathcal{L}\cong \mathcal{O}^{\oplus r}$이다. 한편 tensor product는 finite direct sum과 commute하고, $\varphi_\ast$ 또한 right adjoint로서 finite product와 commute하므로 finite direct sum과 commute한다. ([\[범주론\] §수반함자, ⁋정리 9](/ko/math/category_theory/adjoints#thm9)) 따라서 $V$ 위에서 양변은 모두 $(\varphi_\ast \mathcal{F}\vert_V)^{\oplus r}$이고, $\theta$의 naturality에 의하여 이 identification 아래에서 $\theta$는 항등사상 $r$개의 direct sum이다. 곧 $\theta$는 각 $V$ 위에서 isomorphism이므로 isomorphism이다.
:::

[명제 17](#prop17)이 말하는 것은 $\varphi_\ast$가 abelian sheaf 수준의 연산에 그치지 않고 $\mathcal{O}_Y$-module 구조를 존중한다는 것이다. 이는 [\[대수적 위상수학\] §벡터다발의 특성류](/ko/math/algebraic_topology/characteristic_classes)에서 Gysin homomorphism $\pi_!$가 주는 등식

$$\pi_!(\pi^\ast\alpha\smile\beta)=\alpha\smile\pi_!\beta$$

의 대수기하 버전이며, 이들은 모두 base에서 당겨온 것은 pushforward 밖으로 빠져나온다는 공통된 아이디어로부터 오는 것이다.

## Ideal sheaf와 closed subscheme

Pushforward가 quasi-coherence를 보존한다는 사실의 가장 중요한 응용은 closed subscheme이 결정하는 ideal sheaf이다. Affine scheme $\Spec A$의 ideal $\mathfrak{a}\subseteq A$는 그 자체로 $A$-module이므로 associated sheaf $\widetilde{\mathfrak{a}}$를 정의하고, 이는 $\mathcal{O}_{\Spec A}=\widetilde A$의 subsheaf이다. 일반적인 scheme $X$의 closed embedding $\iota:Z \rightarrow X$가 정의하는 ideal sheaf $\mathcal{I}_{Z/X}=\ker\iota^\sharp$ 또한 각각의 affine open subset 위에서 ideal을 주지만 ([§닫힌 부분스킴, ⁋정의 5](/ko/math/scheme_theory/closed_subschemes#def5)), 이 ideal들이 localization과 호환되어 하나의 associated sheaf로 붙는지는 별개의 문제이다. [§닫힌 부분스킴, ⁋명제 6](/ko/math/scheme_theory/closed_subschemes#prop6)이 gluing을 위해 요구한 localization 조건이 바로 quasi-coherence이므로, 확인해야 할 것은 $\mathcal{I}_{Z/X}$가 quasi-coherent sheaf라는 것이다. 이는 [정리 16](#thm16)의 응용으로 얻어진다.

::: 명제 18
Closed embedding $\iota:Z \rightarrow X$에 대하여 ([§닫힌 부분스킴, ⁋정의 2](/ko/math/scheme_theory/closed_subschemes#def2)), $\iota_\ast \mathcal{O}_Z$와 ideal sheaf $\mathcal{I}_{Z/X}$는 모두 $X$ 위의 quasi-coherent sheaf이다.
:::
::: 증명
[정리 16](#thm16)의 세 가설 가운데 $\mathcal{O}_Z$가 $Z$ 위의 quasi-coherent sheaf라는 것은, 각 affine open subset $\Spec B\subseteq Z$ 위에서 $\mathcal{O}_Z\vert_{\Spec B}=\widetilde B$인 데에서 곧바로 따라온다. 따라서 $\iota$가 quasi-compact이고 quasi-separated임만 확인하면 된다. $X$의 affine open subset $U\cong \Spec A$를 고정하고 $W=\iota^{-1}(U)$라 하자. $\iota$는 연속함수로서 $Z$와 $X$의 닫힌집합 사이의 homeomorphism이므로, $W$는 $U$의 닫힌 부분집합 $C=\iota(Z)\cap U$와 homeomorphic하다. 그런데 affine scheme은 quasi-compact이고 ([§스펙트럼, ⁋보조정리 12](/ko/math/scheme_theory/spectrums#lem12)) quasi-compact space의 닫힌 부분집합은 quasi-compact이므로 $W$ 또한 quasi-compact이다. 즉 $\iota$는 quasi-compact morphism이다. ([§스킴 사상의 성질들, ⁋정의 2](/ko/math/scheme_theory/properties_of_scheme_morphisms#def2))

Quasi-separatedness도 $C$의 위상만으로 확인된다. $\{D(f)\}_{f\in A}$가 $U$의 base이므로 $C$의 임의의 열린집합은 $C\cap D(f)$들의 합집합이고, 각각의 $C\cap D(f)$는 quasi-compact space $D(f)\cong \Spec A_f$의 닫힌 부분집합이라 quasi-compact이다. 따라서 $C$의 quasi-compact 열린집합은 유한히 많은 $C\cap D(f)$의 합집합으로 쓸 수 있으며, 그러한 두 집합의 교집합은 $C\cap D(f)\cap D(g)=C\cap D(fg)$ 꼴들의 유한 합집합이 되어 다시 quasi-compact이다. 즉 $W$는 quasi-separated scheme이고, $U$가 임의의 affine open subset이었으므로 $\iota$는 quasi-separated morphism이다. ([§스킴 사상의 성질들, ⁋정의 5](/ko/math/scheme_theory/properties_of_scheme_morphisms#def5)) 이제 [정리 16](#thm16)에 의하여 $\iota_\ast \mathcal{O}_Z$는 $X$ 위의 quasi-coherent sheaf이다.

남은 것은 $\mathcal{I}_{Z/X}=\ker\iota^\sharp$이다. quasi-coherence가 affine-local이므로 ([정리 10](#thm10)) 위에서 고정한 $U=\Spec A$ 위에서 보이면 충분하다. $N=(\iota_\ast \mathcal{O}_Z)(U)$라 하면 [정리 10](#thm10)에 의하여 $(\iota_\ast \mathcal{O}_Z)\vert_U\cong \widetilde N$이고, 따라서 $\iota^\sharp$을 $U$로 제한한 것은 $\widetilde A \rightarrow \widetilde N$ 꼴의 morphism이므로 [정리 7](#thm7)에 의하여 적당한 $A$-module homomorphism $\phi:A \rightarrow N$의 associated sheaf $\widetilde\phi$이다. 그럼 두 short exact sequence

$$0 \rightarrow \ker\phi \rightarrow A \rightarrow \im\phi \rightarrow 0,\qquad 0 \rightarrow \im\phi \rightarrow N \rightarrow N/\im\phi \rightarrow 0$$

에 [명제 6](#prop6)을 적용하면 $\widetilde{\im\phi} \rightarrow \widetilde N$이 injective이고 $\widetilde{\ker\phi}=\ker(\widetilde A \rightarrow \widetilde{\im\phi})$이므로, 결국 $\ker\widetilde\phi=\widetilde{\ker\phi}$를 얻는다. 즉 $\mathcal{I}_{Z/X}\vert_U\cong \widetilde{\ker\phi}$는 associated sheaf이고, 이로부터 $\mathcal{I}_{Z/X}$는 quasi-coherent sheaf이다.
:::

이로써 $X$의 closed subscheme들은 $\mathcal{O}_X$의 quasi-coherent ideal sheaf, 곧 $\mathcal{O}_X$의 quasi-coherent 부분 $\mathcal{O}_X$-module과 정확히 대응한다. 한 방향은 [명제 18](#prop18)이 주며, 거꾸로 그러한 $\mathcal{I}$가 주어지면 각각의 affine open subset $\Spec A$에 대하여 $\mathcal{I}(\Spec A)$는 $A$의 ideal이고 [정리 10](#thm10)과 [보조정리 3](#lem3)에 의하여 $\mathcal{I}(D(f))\cong \mathcal{I}(\Spec A)_f$가 성립하므로, [§닫힌 부분스킴, ⁋명제 6](/ko/math/scheme_theory/closed_subschemes#prop6)에 의하여 $\mathcal{I}$는 $X$의 유일한 closed subscheme을 유도한다. 이 대응은 affine 위에서 ideal $\mathfrak{a}\subseteq A$와 quotient $A/\mathfrak{a}$ 사이의 대응에 다름 아니다. 또한 [명제 18](#prop18)은 [§닫힌 부분스킴, ⁋명제 3](/ko/math/scheme_theory/closed_subschemes#prop3)의 증명에서 증명 없이 사용한 사실이기도 하다. 

## Affine morphism과 relative spectrum

Closed embedding은 특정한 sheaf, 즉 $\mathcal{O}_X$의 ideal sheaf를 통해 완전하게 설명할 수 있었으며, 우리는 위에서 이 ideal sheaf가 quasi-coherent sheaf인 것을 살펴보았다. 이렇게 sheaf를 통해 완전하게 정해지는 morphism은 closed embedding 뿐이 아니며, 우리는 affine morphism 또한 이러한 방식의 표현을 갖는다는 것을 살펴볼 것이다. ([§스킴 사상의 성질들, ⁋정의 8](/ko/math/scheme_theory/properties_of_scheme_morphisms#def8)) 핵심적인 사실은 affine morphism $X\rightarrow S$를 정의하기 위해서는 $X$의 open affine subscheme들 (그리고 이들로부터 $S$로의 map들)을 붙여주면 된다는 것이다. 그런데 affine subscheme들은 정확하게 그 coordinate ring으로부터 완전하게 얻어지는 것이므로 우리는 이 ring들을 붙이는 문제를 대신 풀면 된다. 이 때 affine morphism $\varphi: X \rightarrow S$에 대하여 각각의 ring $\mathcal{O}_X(\varphi^{-1}(V))$는 structure morphism이 주는 $\mathcal{O}_S(V)$로부터의 ring homomorphism을 함께 가지므로 $\mathcal{O}_S(V)$-algebra이고, 따라서 이 데이터 전체는 $S$ 위의 sheaf $\varphi_\ast\mathcal{O}_X$ 하나와 그 algebra 구조로 정리된다.

::: 정의 19
Scheme $S$ 위의 $\mathcal{O}_S$-module $\mathcal{A}$가 *quasi-coherent $\mathcal{O}_S$-algebra*라는 것은, $\mathcal{A}$가 quasi-coherent sheaf이며 ([정의 8](#def8)) 각각의 열린집합 $V$마다 $\mathcal{A}(V)$가 가환 $\mathcal{O}_S(V)$-algebra의 구조를 가지고 restriction map이 algebra homomorphism인 것이다.
:::

위에서 설명한 것과 같이 affine morphism이 주어지면 항상 이러한 방식으로 quasi-coherent $\mathcal{O}_S$-algebra를 정의할 수 있다. 우리 주장은 이보다 강력한 것으로, 임의의 quasi-coherent $\mathcal{O}_S$-algebra는 언제나 이러한 방식으로 얻어진다는 것이다.

::: 정리 20
다음이 성립한다.

1. Affine morphism $\varphi: X \rightarrow S$에 대하여 $\varphi_\ast \mathcal{O}_X$는 quasi-coherent $\mathcal{O}_S$-algebra이며 $S$의 임의의 affine open subset $V$에 대하여 $\varphi^{-1}(V)\cong \Spec (\varphi_\ast \mathcal{O}_X)(V)$이다.
2. 임의의 quasi-coherent $\mathcal{O}_S$-algebra $\mathcal{A}$에 대하여, affine morphism $\varphi: X \rightarrow S$와 $\mathcal{O}_S$-algebra들의 isomorphism $\alpha:\mathcal{A}\xrightarrow{\sim} \varphi_\ast \mathcal{O}_X$가 존재한다. 이러한 triple $(X, \varphi, \alpha)$은 $\alpha$와 호환되는 unique isomorphism에 대하여 유일하다.
3. 두 affine morphism $\varphi: X \rightarrow S$와 $\varphi': Z \rightarrow S$에 대하여, $S$ 위의 morphism $X \rightarrow Z$를 주는 것은 $\mathcal{O}_S$-algebra들의 morphism $(\varphi')_\ast \mathcal{O}_Z \rightarrow \varphi_\ast \mathcal{O}_X$를 주는 것과 같다.
:::
::: 증명
첫째 주장부터 보인다. 우선 quasi-coherence를 보이기 위해 우리는 앞서와 마찬가지로 [정리 16](#thm16)을 사용한다. 우선 $S$의 affine open subset $V$에 대하여 $\varphi^{-1}(V)\cong \Spec A$는 affine scheme이므로 quasi-compact이다. ([§스펙트럼, ⁋보조정리 12](/ko/math/scheme_theory/spectrums#lem12)) 또, $\{D(f)\}$가 $\Spec A$의 base이므로 quasi-compact open set이 언제나 유한히 많은 $D(f)$의 합집합이고, $D(f)\cap D(g)=D(fg)$이므로 그러한 두 열린집합의 교집합이 다시 유한히 많은 $D(fg)$ 꼴의 합집합이 되므로 이들은 quasi-separated이다. 즉 $\varphi$는 quasi-compact, quasi-separated morphism이 되어 [정리 16](#thm16)을 적용할 수 있고 따라서 $\varphi_\ast \mathcal{O}_X$는 $S$ 위의 quasi-coherent sheaf이다. 이 위의 algebra 구조는 structure sheaf의 morphism $\varphi^\sharp:\mathcal{O}_S \rightarrow \varphi_\ast\mathcal{O}_X$으로 주어진다. 마지막으로 $V$가 affine open subset이면 $\varphi^{-1}(V)$ 자체가 affine scheme이므로, [§아핀스킴, ⁋보조정리 6](/ko/math/scheme_theory/affine_schemes#lem6)에 의하여 $\varphi^{-1}(V)\cong \Spec \mathcal{O}_X(\varphi^{-1}(V))=\Spec (\varphi_\ast \mathcal{O}_X)(V)$를 얻는다.

역시 핵심적인 것은 둘째 주장이다. 우선 존재성을 보이기 위해 $S$의 affine open covering $\{V_i=\Spec B_i\}$를 택하자. 이제 $A_i=\mathcal{A}(V_i)$라 하면 $\mathcal{A}$가 quasi-coherent이므로 [정리 10](#thm10)에 의하여 $\mathcal{A}\vert_{V_i}\cong \widetilde{A_i}$이다. 이제 $\mathcal{A}$의 $\mathcal{O}_S$-algebra 구조가 주는 ring homomorphism을 $\phi_i:B_i \rightarrow A_i$라 하면, $X_i=\Spec A_i$로 두어 $\phi_i$가 정의하는 scheme morphism $\varphi_i:X_i \rightarrow V_i$을 정의할 수 있다. 주장은 $X_{ij}=\varphi_i^{-1}(V_i\cap V_j)$들을 붙일 수 있다는 것이다. 이를 확인하기 위해 임의의 $x\in V_i\cap V_j$에 대하여, $V_i$와 $V_j$ 모두에서 principal open subset인 $x\in W\subseteq V_i\cap V_j$를 택하자. ([§스킴의 위상구조, ⁋보조정리 11](/ko/math/scheme_theory/topology_of_schemes#lem11)) $W$가 $V_i$ 안에서 $D(f)$ 꼴로 적힌다 하면, $\mathcal{A}\vert_{V_i}\cong \widetilde{A_i}$로부터 $\mathcal{A}(W)\cong (A_i)_{\phi_i(f)}$이고, $W$의 정의에 의해 $\varphi_i^{-1}(W)=D(\phi_i(f))$이므로

$$\varphi_i^{-1}(W)\cong \Spec (A_i)_{\phi_i(f)}\cong \Spec \mathcal{A}(W)\tag{$\ast$}$$

이 성립한다. 같은 계산이 $V_j$ 쪽에서도 성립하므로 canonical isomorphism $\varphi_i^{-1}(W)\cong \varphi_j^{-1}(W)$를 얻는다. 이 isomorphism은 $\mathcal{A}(W)$만으로 결정되므로, 이들은 자연스럽게 overlap 위에서 붙으며 cocycle condition을 만족한다. 즉 이들은 하나의 scheme $X$과 이 위의 morphism $\varphi: X\rightarrow S$로 붙는다. 이 때 각각의 $\varphi^{-1}(V_i)=X_i$가 affine이므로 [§스킴 사상의 성질들, ⁋명제 9](/ko/math/scheme_theory/properties_of_scheme_morphisms#prop9)에 의하여 $\varphi$는 affine morphism이고, identification $(\varphi_\ast\mathcal{O}_X)(V_i)=\Gamma(X_i,\mathcal{O}_{X_i})=A_i=\mathcal{A}(V_i)$이 restriction map과 호환되므로 이들은 $\mathcal{O}_S$-algebra들의 isomorphism $\alpha:\mathcal{A}\xrightarrow{\sim}\varphi_\ast\mathcal{O}_X$을 준다. 유일성 또한 본질적으로 $(\ast)$로부터 나오는 것으로, 두 triple $(X,\varphi,\alpha)$와 $(X',\varphi',\alpha')$이 조건을 만족한다면 이 계산에 의해 $S$의 임의의 affine open subset $V$에 대하여

$$\varphi^{-1}(V)\cong \Spec \mathcal{A}(V)\cong (\varphi')^{-1}(V)$$

이 성립해야 하기 때문에 얻어진다.

마지막 주장의 경우, $S$ 위의 morphism $\vartheta:X\rightarrow Z$가 주어지면 $S$의 affine open subset $V$마다 $\vartheta$는 morphism $\varphi^{-1}(V)\rightarrow (\varphi')^{-1}(V)$를 유도하고, 첫째 주장에 의하여 이 둘이 affine scheme이므로 이는 $\mathcal{O}_S(V)$-algebra homomorphism $((\varphi')_\ast\mathcal{O}_Z)(V)\rightarrow (\varphi_\ast\mathcal{O}_X)(V)$에 대응된다. 이들이 restriction map과 호환되므로 $\mathcal{O}_S$-algebra들의 morphism $(\varphi')_\ast\mathcal{O}_Z\rightarrow \varphi_\ast\mathcal{O}_X$를 얻는다. 거꾸로 이러한 morphism이 주어지면 같은 대응이 각 affine open subset 위에서 $\varphi^{-1}(V)\rightarrow (\varphi')^{-1}(V)$를 주고 이들은 overlap 위에서 일치하므로 [§스킴 사이의 사상, ⁋명제 1](/ko/math/scheme_theory/morphism_of_schemes#prop1)에 의하여 $S$ 위의 morphism $X\rightarrow Z$로 붙고, 이 두 구성이 서로의 역인 것은 affine 위에서 확인할 수 있다.
:::

즉 affine morphism은 $S$ 위의 quasi-coherent algebra와 정확히 같은 데이터이며, [정리 20](#thm20)의 셋째 주장은 이 대응이 morphism까지 보존한다는 것을 보여준다. 즉 $S$ 위의 affine scheme들의 category $\AffSch_{/S}$와 quasi-coherent $\mathcal{O}_S$-algebra들의 category 사이의 contravariant equivalenc가 존재한다. 이제 이 대응의 한쪽 방향에 이름을 붙인다.

::: 정의 21
Quasi-coherent $\mathcal{O}_S$-algebra $\mathcal{A}$에 대하여, [정리 20](#thm20)의 둘째 주장이 주는 affine morphism $\varphi:X\rightarrow S$의 정의역 $X$를 $\mathcal{A}$의 *relative spectrum*이라 부르고 $\rSpec_S(\mathcal{A})$로 적는다.
:::

직관적으로 이는 $\Spec$을 base 위로 올린 relative 버전으로, 특히 closed embedding $\iota:Z\rightarrow S$는 affine morphism이므로 ([§닫힌 부분스킴, ⁋명제 3](/ko/math/scheme_theory/closed_subschemes#prop3)) 같은 construction을 반본할 수 있다. 당연히 이렇게 얻어지는 algebra는 $\mathcal{O}_S/\mathcal{I}_{Z/S}$로, 즉 위에서 살펴본 ideal sheaf의 대응은 relative spectrum을 이 특수한 경우에 적용한 것이다.

뿐만 아니라 relative spectrum은 base change에 대해서도 잘 행동한다.

::: 명제 22
Scheme morphism $\varphi:S'\rightarrow S$와 quasi-coherent $\mathcal{O}_S$-algebra $\mathcal{A}$에 대하여, pullback $\varphi^\ast\mathcal{A}$는 quasi-coherent $\mathcal{O}_{S'}$-algebra이고

$$\rSpec_{S'}(\varphi^\ast\mathcal{A})\cong \rSpec_S(\mathcal{A})\times_SS'$$

이 성립한다.
:::
::: 증명
$\varphi^\ast\mathcal{A}$가 quasi-coherent sheaf인 것은 [명제 15](#prop15)이며, pullback이 tensor product와 compatible하므로 $\mathcal{A}$의 곱셈과 항등원을 pullback해와서 이 위에 $\mathcal{O}_{S'}$-algebra 구조를 줄 수 있다.

이제 $X=\rSpec_S(\mathcal{A})$라 하고 projection $p:X\times_SS'\rightarrow S'$를 생각하자. $\varphi(V')\subseteq V$인 affine open subset $V'=\Spec B'\subseteq S'$와 $V=\Spec B\subseteq S$의 쌍은 $S'$을 덮으며, $\varphi\vert_{V'}:V'\rightarrow V$에 대응하는 ring homomorphism을 $\phi:B\rightarrow B'$라 하자. 이러한 $V'$에 대하여 [§올곱, ⁋보조정리 3](/ko/math/scheme_theory/fiber_products#lem3)과 fiber product의 결합법칙으로부터

$$p^{-1}(V')\cong X\times_SV'\cong (X\times_SV)\times_VV'$$

이고, [§올곱, ⁋보조정리 3](/ko/math/scheme_theory/fiber_products#lem3)에 의하여 $X\times_SV$는 $V$의 preimage, 곧 [정리 20](#thm20)의 첫째 주장에 의하여 $\Spec \mathcal{A}(V)$이다. 따라서 [§올곱, ⁋보조정리 2](/ko/math/scheme_theory/fiber_products#lem2)에 의하여

$$p^{-1}(V')\cong \Spec \mathcal{A}(V)\times_{\Spec B}\Spec B'\cong \Spec (\mathcal{A}(V)\otimes_BB')$$

를 얻는다. 한편 [명제 15](#prop15)의 증명에 의하여 $(\varphi^\ast\mathcal{A})\vert_{V'}\cong \widetilde{\mathcal{A}(V)\otimes_BB'}$이므로, [정리 20](#thm20)의 첫째 주장에 의하여 $\rSpec_{S'}(\varphi^\ast\mathcal{A})$ 또한 $V'$ 위에서 $\Spec (\mathcal{A}(V)\otimes_BB')$이다. 이 isomorphism들은 모두 $\phi:B\rightarrow B'$과 $\mathcal{A}(V)$의 $B$-algebra 구조로부터 canonical하게 정해지므로 overlap 위에서 일치하여 $S'$ 위의 isomorphism으로 붙는다.
:::

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate Texts in Mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundations of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).
