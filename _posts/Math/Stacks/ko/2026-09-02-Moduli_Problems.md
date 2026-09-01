---
title: "Moduli 문제: fine moduli와 coarse moduli"
description: "Moduli 문제를 functor·stack으로 정식화하고, universal family를 갖는 fine moduli space의 표현가능성과 automorphism으로 인한 장애, 그리고 coarse moduli space와 moduli stack의 역할을 다룬다."
excerpt: "Moduli functors, fine vs coarse moduli spaces, and why the moduli stack is the right object"

categories: [Math / Stacks]
permalink: /ko/math/stacks/moduli_problems
sidebar: 
    nav: "stacks-ko"

date: 2026-09-02
weight: 4

published: false

---

기하학의 많은 문제는 "주어진 종류의 대상을 모두 분류하라"는 형태를 띤다. Genus $g$의 smooth projective curve, 고정된 variety 위의 일정한 rank의 vector bundle, projective space 안의 일정한 Hilbert 다항식을 가진 subscheme 따위가 그러하다. 이러한 분류 문제에서 우리가 바라는 것은 단순히 isomorphism class들의 집합을 나열하는 일이 아니라, 그 isomorphism class들이 어떻게 **연속적으로 변형되는지**를 담는 기하적 대상, 곧 *moduli space*를 구성하는 일이다. 한 점이 한 isomorphism class에 대응하고, 그 점들이 모인 공간의 기하가 변형의 기하를 반영하기를 우리는 원한다.

이 글에서는 분류 문제를 functor의 언어로 정식화하고, 그 functor를 표현하는 이상적인 답인 fine moduli space의 정의와 그것이 실제로 존재하는 비자명한 예들을 살펴본다. 이어서 분류 대상이 비자명한 automorphism을 가질 때 fine moduli가 어떻게 원리적으로 막히는지를 분석하고, 그 장애를 우회하는 두 가지 길, 곧 automorphism을 기억하는 moduli stack과 isomorphism class만을 남기는 coarse moduli space를 도입한다. 마지막으로 타원곡선의 moduli $\mathcal{M}_{1, 1}$을 중심 예로 삼아, 같은 분류 문제가 stack 수준에서는 universal family를 가지지만 coarse 공간인 $j$-직선 위에서는 가지지 못하는 까닭을 정밀하게 설명한다.

## Moduli 문제와 moduli functor

분류 문제를 정식화하는 핵심 착상은, 고정된 한 base 위에서 대상을 분류하는 대신, 가능한 모든 base $T$에 대하여 동시에 *$T$로 매개변수화된 족*을 분류하는 것이다. 한 점만이 아니라 임의의 test scheme $T$ 위의 족 전체를 다루어야, isomorphism class들이 어떻게 변형되는지가 자료에 담긴다. 이때 한 분류 문제는 각 $T$에 그 위의 족들을 대응시키는 규칙, 곧 functor로 압축된다.

::: 정의 1
한 *moduli 문제<sub>moduli problem</sub>*는 다음 자료로 이루어진다. 각 scheme $T$에 대하여 "$T$ 위의 족"이라 부르는 대상들의 모임이 주어지고, 그 사이의 isomorphism이 지정되어 groupoid $\mathcal{M}(T)$를 이루며, 각 morphism $f: T' \rightarrow T$에 대하여 족을 $T'$으로 끌어당기는 pullback functor $f^\ast:\mathcal{M}(T) \rightarrow \mathcal{M}(T')$이 주어진다. 이 자료가 정합성 조건을 만족하여 pseudofunctor

$$\mathcal{M}:\Sch^\op \rightarrow \Grpd$$

를 이룰 때, 이를 그 moduli 문제의 *moduli functor<sub>모듈라이 함자</sub>*라 부른다. ([§스택, ⁋정의 3](/ko/math/stacks/fibered_categories_and_stacks#def3)) 각 fiber groupoid $\mathcal{M}(T)$의 isomorphism class만을 취하여 얻는 set-값 functor

$$\underline{M}:\Sch^\op \rightarrow \Set,\qquad \underline{M}(T)=\obj \mathcal{M}(T)/\cong$$

를 그 moduli 문제의 *coarse moduli functor<sub>성긴 모듈라이 함자</sub>* 또는 *set-값 moduli functor*라 부른다.
:::

여기에서 "족"이 정확히 무엇인지는 분류 문제마다 다르다. Genus $g$ 곡선의 분류에서는 $T$ 위의 족이란 smooth projective morphism $X \rightarrow T$로서 모든 기하적 fiber가 genus $g$의 곡선인 것이고, 고정된 variety $X$ 위의 vector bundle의 분류에서는 $X\times T$ 위의 rank $r$ vector bundle이며, section을 가진 타원곡선의 분류에서는 section을 가진 genus $1$의 smooth projective curve의 족이다. 어느 경우든 pullback은 morphism $f: T' \rightarrow T$에 대한 fiber product를 통한 base change로 주어지고, 정합성 자료는 base change가 합성과 canonical isomorphism으로 호환된다는 것에서 나온다. 이 정합성이 등호가 아니라 canonical isomorphism으로만 성립하기 때문에 $\mathcal{M}$은 진짜 pseudofunctor이며, 동치인 fibered category의 언어로 다루는 편이 자연스럽다. ([§스택, §§유사함자](/ko/math/stacks/fibered_categories_and_stacks#유사함자))

두 functor $\mathcal{M}$과 $\underline{M}$의 차이가 이 글 전체의 주제이다. Groupoid-값 functor $\mathcal{M}$은 각 족의 automorphism을 자료로 기억하는 반면, set-값 functor $\underline{M}$은 isomorphism class만 남겨 automorphism 정보를 버린다. 분류 대상이 비자명한 automorphism을 가질 때 이 둘은 본질적으로 다르며, 바로 그 차이가 fine moduli space의 존재를 좌우한다. 우선은 automorphism이 문제되지 않는 상황, 곧 $\underline{M}$이 충분한 정보를 담는 경우부터 다룬다.

## Fine moduli space와 universal family

이상적인 답은 moduli 문제를 표현하는 scheme이다. 곧 isomorphism class들이 한 scheme $M$의 점들과 일대일대응할 뿐 아니라, $M$ 위에 단 하나의 "보편적인 족"이 놓여 있어 임의의 족이 그것의 pullback으로 유일하게 얻어지는 상황이다. 이를 functor의 언어로 옮기면 representability가 된다.

::: 정의 2
Moduli 문제의 set-값 moduli functor $\underline{M}:\Sch^\op \rightarrow \Set$가 scheme $M$에 의하여 *representable*할 때, 곧 natural isomorphism

$$\underline{M}\cong \Hom_{\Sch}(-, M)$$

이 존재할 때, $M$을 그 문제의 *fine moduli space<sub>섬세한 모듈라이 공간</sub>*라 부른다. 이 natural isomorphism 아래에서 항등사상 $\id_M\in \Hom_\Sch(M, M)$에 대응하는 원소

$$\mathcal{U}\in \underline{M}(M)$$

을 *universal family<sub>보편족</sub>*라 부른다.
:::

이 정의는 representable functor의 universal element를 그대로 옮긴 것이다. ([\[범주론\] §표현가능한 함자, ⁋정의 5](/ko/math/category_theory/representable_functors#def5)) Universal family $\mathcal{U}$이 갖는 보편성은 다음과 같이 풀린다. 임의의 scheme $T$와 그 위의 족 $X\in \underline{M}(T)$에 대하여, natural isomorphism의 한 성분 $\underline{M}(T)\cong \Hom_\Sch(T, M)$이 $X$에 유일한 morphism $f_X: T \rightarrow M$을 대응시키며, Yoneda의 naturality에 의하여 이 $f_X$은 정확히

$$X\cong f_X^\ast \mathcal{U}$$

을 만족하는 유일한 morphism이다. 곧 $M$ 위의 모든 족은 universal family를 끌어당겨 단 한 가지 방식으로 얻어지며, $f_X$을 $X$의 *classifying morphism*이라 부른다. Representability는 또한 $\Sch^\op$ 위의 functor로서 $\underline{M}$의 category of elements가 initial object $(M, \mathcal{U})$을 가진다는 것과 동치이고 ([\[범주론\] §표현가능한 함자, ⁋명제 8](/ko/math/category_theory/representable_functors#prop8)), 따라서 fine moduli space는 존재할 경우 유일한 isomorphism을 통해 유일하게 결정된다.

Fine moduli가 실제로 존재하는 비자명한 예는 분류 대상에 충분한 강성 자료, 곧 rigidify하는 추가 구조를 얹은 경우에서 나온다. Projective space와 Grassmannian이 대표적이다.

::: 예시 3 (Projective space)
Projective space $\mathbb{P}^n$은 다음 moduli 문제의 fine moduli space이다. $T$ 위의 족을, $T$ 위의 line bundle $\mathcal{L}$과 이를 globally generate하는 $n+1$개의 section $s_0,\ldots, s_n\in \Gamma(T, \mathcal{L})$의 자료 $(\mathcal{L}, s_0,\ldots, s_n)$의 isomorphism class로 정의한다. 여기에서 두 자료가 isomorphic이라는 것은 section들을 옮기는 line bundle의 isomorphism이 존재하는 것이다. 이 functor는 $\mathbb{P}^n$에 의하여 표현되며, universal family는 twisting sheaf $\mathcal{O}_{\mathbb{P}^n}(1)$과 그 coordinate section $\x_0,\ldots, \x_n$이다. ([\[스킴\] §점함자, ⁋정리 5](/ko/math/scheme_theory/functor_of_points#thm5))
:::

이 예에서 결정적인 것은, 분류되는 자료 $(\mathcal{L}, s_0,\ldots, s_n)$이 비자명한 automorphism을 가지지 않는다는 점이다. Line bundle $\mathcal{L}$ 자체는 scalar multiplication에 의한 $\mathbb{G}_m$만큼의 automorphism을 가지지만, globally generate하는 section들을 고정하면 그 section을 보존하는 line bundle automorphism은 항등사상뿐이다. Section이라는 강성 자료가 automorphism을 죽인 덕분에 set-값 functor가 곧바로 representable해진 것이며, 이것이 fine moduli가 존재하는 전형적인 구조이다.

::: 예시 4 (Grassmannian)
Grassmannian $\Gr(k, n)$은 다음 moduli 문제의 fine moduli space이다. $T$ 위의 족을, trivial bundle의 rank $k$ locally free quotient bundle

$$\mathcal{O}_T^n\twoheadrightarrow \mathcal{Q},\qquad \mathcal{Q}\text{ is locally free of rank } k$$

의 isomorphism class로 정의한다. 여기에서 두 quotient bundle이 isomorphic이라는 것은 두 quotient map을 commute하게 하는 $\mathcal{O}_T$-module isomorphism $\mathcal{Q}\cong \mathcal{Q}'$이 존재하는 것이다. 이 functor는 $\Gr(k, n)$에 의하여 표현되며, universal family는 Grassmannian 위의 universal quotient bundle $\mathcal{O}^n\twoheadrightarrow \mathcal{Q}^{\mathrm{univ}}$이다. ([\[스킴\] §점함자, ⁋예시 6](/ko/math/scheme_theory/functor_of_points#ex6)) $T=\Spec \mathbb{K}$가 field 위의 한 점일 때 rank $k$ quotient space $\mathbb{K}^n\twoheadrightarrow Q$은 그 kernel인 $(n-k)$차원 부분공간과 일대일대응하므로, $\Gr(k, n)(\mathbb{K})$은 $\mathbb{K}^n$의 $(n-k)$차원 부분공간들의 집합과 일치한다. 부분공간을 직접 분류하는 [\[대수다양체\] §그라스만 다양체, ⁋정의 1](/ko/math/algebraic_varieties/grassmannians#def1)의 관례에서 이 집합은 $\Gr(n-k, n)$에 해당하며, rank $k$ quotient bundle의 moduli로서 정의한 $\Gr(k, n)$은 kernel을 취하는 대응을 통해 그것과 동일시된다.
:::

예시 4 역시 강성의 메커니즘을 따른다. 분류되는 자료는 quotient bundle $\mathcal{Q}$ 자체가 아니라 고정된 $\mathcal{O}_T^n$으로부터의 surjection $\mathcal{O}_T^n\twoheadrightarrow \mathcal{Q}$이고, 이 surjection과 commute하는 automorphism은 항등사상뿐이다. Ambient trivial bundle을 고정한 것이 여기에서의 강성 자료이며, 그 kernel을 취하여 얻는 subbundle $\mathcal{S}\subseteq \mathcal{O}_T^n$의 자료도 같은 이유로 똑같이 강하다. $k=1$인 경우 rank $1$ quotient bundle을 분류하는 일은 예시 3의 projective space $\mathbb{P}^{n-1}$로 환원되며, 실제로 $\mathcal{O}_T^n\twoheadrightarrow \mathcal{L}$을 주는 것은 $\mathcal{L}$의 globally generate하는 section $n$개를 주는 것과 같다. 이 두 예는 fine moduli가 가능한 분류 문제의 공통 구조, 곧 분류 대상이 비자명한 automorphism을 가지지 않도록 자료를 rigidify한 구조를 보여준다.

## Automorphism으로 인한 장애

앞 절의 예들이 작동한 까닭이 강성에 있었다면, 강성이 깨진 문제, 곧 분류 대상이 비자명한 automorphism을 본질적으로 가지는 문제에서는 fine moduli가 어떻게 되는지를 물어야 한다. 결론은 부정적이다. 비자명한 automorphism은 isomorphism class가 같으면서도 서로 다른 *비자명한 등질 족*을 만들어내며, 이것이 representability를 정면으로 막는다.

핵심은 다음 관찰이다. Fine moduli space가 존재한다면 set-값 moduli functor $\underline{M}$은 representable functor $\Hom_\Sch(-, M)$과 isomorphic이고, representable functor는 fpqc topology(따라서 그보다 거친 étale·Zariski topology)에 대한 sheaf이다. 이는 faithfully flat descent의 표준적 귀결로, affine한 $M=\Spec R$의 경우 global section presheaf $T\mapsto \Gamma(T, \mathcal{O}_T)$이 fpqc sheaf라는 [\[스킴\] §충실평탄하강, ⁋정리 10](/ko/math/scheme_theory/faithfully_flat_descent#thm10)으로부터 $\Hom_\Sch(-, \Spec R)=\Hom_{\mathrm{Ring}}(R, \Gamma(-, \mathcal{O}))$을 통해 따라오고, 일반적인 $M$은 affine open으로 덮어 접합하여 얻는다. 즉 한 scheme으로 가는 morphism들은 covering 위에서 정합적으로 주어지면 유일하게 이어 붙는다. 그러므로 $\underline{M}$이 sheaf가 아니면 fine moduli는 존재할 수 없다. 비자명한 automorphism은 정확히 이 sheaf 조건의 분리성, 곧 "covering 위에서 같은 족은 원래 같다"는 부분을 깨뜨린다.

::: 명제 5
한 moduli 문제에 대하여, 어떤 scheme $T$와 그 위의 surjective étale covering $S \rightarrow T$, 그리고 족 $X\in \mathcal{M}(T)$이 존재하여 다음을 만족한다고 하자. 어떤 고정된 대상 $E$에 대하여 $S$로 끌어당기면 $X\times_T S\cong E\times S$이지만 ($X$이 *isotrivial<sub>등질</sub>*하지만), $X$이 $T$ 위에서 상수 족 $E\times T$과 isomorphic이 아니다. 그럼 이 문제는 fine moduli space를 가지지 않는다.
:::
::: 증명
Fine moduli space $M$이 존재한다고 가정하고 모순을 이끈다. [정의 2](#def2)에 의하여 set-값 moduli functor는 representable functor $\underline{M}\cong \Hom_\Sch(-, M)$이고, 위에서 확인한 대로 이는 fpqc 위상에 대한 sheaf, 따라서 그보다 거친 étale 위상에 대해서도 sheaf이다. Sheaf의 조건 가운데 분리성은, 임의의 covering $S \rightarrow T$에 대하여 restriction map

$$\underline{M}(T) \rightarrow \underline{M}(S)$$

이 단사인 것이다.

이제 가정의 두 족 $X$과 $E\times T$을 $\underline{M}(T)$의 원소로 본다. $S$로 끌어당기면 $X\times_T S\cong E\times S\cong (E\times T)\times_T S$이므로, 두 isomorphism class는 $\underline{M}(S)$에서 같은 원소로 보내진다. 그러나 가정에 의하여 $X$과 $E\times T$은 $T$ 위에서 isomorphic이 아니므로 $\underline{M}(T)$에서 서로 다른 원소이다. 이는 restriction map $\underline{M}(T) \rightarrow \underline{M}(S)$의 단사성에 모순이다. 따라서 $\underline{M}$은 분리된 presheaf조차 될 수 없고, representable할 수 없으므로 fine moduli space는 존재하지 않는다.
:::

명제 5의 가정에 등장하는 비자명한 등질 족은, 분류 대상 $E$이 비자명한 automorphism group $\Aut(E)$을 가질 때 그 group의 비자명한 torsor로부터 만들어진다. Order $d$의 automorphism $\sigma\in \Aut(E)$과 degree $d$의 cyclic étale covering $S \rightarrow T$이 (곧 비자명한 $\mathbb{Z}/d$-torsor, [§스택, ⁋정의 17](/ko/math/stacks/fibered_categories_and_stacks#def17)) 주어지면, $\mathbb{Z}/d$을 $E$에는 $\sigma$로 $S$에는 deck transformation으로 대각작용시켜 얻는 quotient

$$X=(E\times S)/(\mathbb{Z}/d) \rightarrow S/(\mathbb{Z}/d)=T$$

이 그러한 족이다. $S$로 끌어당기면 $X\times_T S\cong E\times S$이 되어 등질이며, 이 torsor를 $\mathbb{Z}/d \rightarrow \Aut(E)$, $1\mapsto \sigma$을 따라 밀어낸 $\Aut(E)$-torsor가 비자명하면 $X$은 상수 족과 isomorphic이 아니다. 이는 sheaf 조건의 분리성이 깨지는 모습 그 자체이다. 두 족 $X$과 $E\times T$이 covering $S \rightarrow T$ 위에서 isomorphic이 되지만 $T$ 위에서는 isomorphic이 아니므로, $\underline{M}(T) \rightarrow \underline{M}(S)$이 단사가 아니어서 $\underline{M}$은 separated presheaf조차 되지 못한다. ([§스택, ⁋명제 13](/ko/math/stacks/fibered_categories_and_stacks#prop13))

이 구성에서 결정적인 것은 밀어낸 $\Aut(E)$-torsor의 비자명성이며, 이는 automorphism이 비자명하다는 것만으로는 따라오지 않는다. Field $\mathbb{K}$ 위의 비자명한 $\mu_2$-torsor를 포함 $\mu_2\subseteq \mathbb{G}_m$을 따라 밀어내면, [\[체론\] §갈루아 군의 성질들, ⁋정리 7](/ko/math/field_theory/properties_of_galois_extensions#thm7)에 의하여 $\mathbb{K}$ 위의 $\mathbb{G}_m$-torsor가 모두 자명하므로 그 image는 trivial torsor가 된다. 곧 fine moduli를 막는 것은 automorphism의 존재 자체가 아니라 그것이 실제로 비자명한 form을 낳는다는 사실이고, 그 비자명성은 분류 문제마다 확인해야 한다. 타원곡선에서는 그것이 언제나 가능하다.

::: 예시 6 (타원곡선에 fine moduli가 없음)
Section을 가진 타원곡선 $(E, 0)$은 항상 비자명한 automorphism $[-1]:(\x, \y)\mapsto(\x, -\y)$을 가지며, 이는 section $0$을 고정하는 order $2$의 automorphism이다. 곧 모든 타원곡선에 대하여 $\{\pm 1\}\cong \mathbb{Z}/2\subseteq \Aut(E, 0)$이다. 따라서 $\sigma=[-1]$, $d=2$으로 위의 구성을 적용한다. Characteristic $0$의 field $k$ 위에서 타원곡선 $E:\y^2=\x^3+a\x+b$ ($ab\neq 0$)을 고정하고, $T=\Spec k(t)$과 그 이차확대 $S=\Spec k(t)[\sqrt{t}]$으로 두자. $t$은 $k(t)$의 제곱이 아니므로 $S \rightarrow T$은 비자명한 $\mathbb{Z}/2$-torsor이다. 이때 위의 quotient $X=(E\times S)/(\mathbb{Z}/2)$은 $E$의 *이차 twist* $\y^2=\x^3+t^2a\x+t^3b$이며, $X\times_T S\cong E\times S$이지만 $T$ 위에서는 상수 족과 isomorphic이 아니다. 실제로 $T$ 위의 isomorphism은 좌표변환 $(\x, \y)\mapsto(c^2\x, c^3\y)$의 꼴이어서 $c^4=t^2$과 $c^6=t^3$, 곧 $c^2=t$을 요구하는데, 그러한 $c\in k(t)^\times$은 없다. [명제 5](#prop5)에 의하여 section을 가진 타원곡선의 moduli 문제는 fine moduli space를 가지지 않는다. 이 twist는 $j$-불변량을 바꾸지 않으므로, 기하적 isomorphism class를 점으로 갖는 $\mathbb{A}^1_j$ 위에도 보편 타원곡선은 놓일 수 없다.
:::

예시 6은 강성이 깨진 분류 문제의 전형이다. Projective space나 Grassmannian에서는 추가 자료가 automorphism을 죽여 set-값 functor가 곧바로 sheaf였던 반면, 타원곡선에서는 section을 고정하더라도 $[-1]$이 살아남아 functor가 sheaf가 되지 못한다. 그렇다면 우리는 둘 중 하나를 선택해야 한다. Automorphism을 자료로 그대로 안고 가는 더 정교한 기하적 대상으로 옮겨 가거나, automorphism을 포기하고 isomorphism class만 담는 가장 좋은 scheme 근사를 찾는 것이다. 이 두 길이 다음 절의 주제이다.

## 두 가지 보정: moduli stack과 coarse moduli space

첫 번째 보정은 set-값 functor $\underline{M}$ 대신 groupoid-값 functor $\mathcal{M}$ 자체를 기하적 대상으로 삼는 것이다. 명제 5의 장애가 isomorphism class로 뭉개면서 automorphism 정보를 버린 데서 비롯되었으므로, 그 정보를 끝까지 들고 가면 장애가 사라진다. [정의 1](#def1)의 $\mathcal{M}$을 fibered category로 보고 그것이 stack임을 확인한 뒤, 적절한 대수성 조건을 부과한 것이 바로 *moduli stack*이다.

::: 정의 7
한 moduli 문제의 moduli functor $\mathcal{M}:\Sch^\op \rightarrow \Grpd$이, 대응하는 fibered category로서 site $(\Sch, \mathrm{fppf})$ 위의 stack이고 ([§스택, ⁋정의 12](/ko/math/stacks/fibered_categories_and_stacks#def12)) 나아가 algebraic stack일 때 ([§대수적 스택, ⁋정의 6](/ko/math/stacks/algebraic_stacks#def6)), 이를 그 문제의 *moduli stack<sub>모듈라이 스택</sub>*이라 부른다. 이 stack이 Deligne–Mumford stack인 것은 diagonal $\Delta:\mathcal{M} \rightarrow \mathcal{M}\times\mathcal{M}$이 unramified한 것, 곧 모든 geometric point의 stabilizer가 unramified한 것과 동치이며, 그러한 조건 없이는 Deligne–Mumford가 아닌 Artin stack에 머문다.
:::

Moduli stack 위에는 언제나 universal family가 존재한다. Set-값 functor에서는 universal family가 항등사상의 image로 정의되었듯이 ([정의 2](#def2)), stack에서는 항등 morphism $\id_\mathcal{M}:\mathcal{M} \rightarrow \mathcal{M}$ 자체가 $\mathcal{M}$ 위의 universal family를 주며, automorphism을 fiber groupoid가 그대로 기억하므로 명제 5의 모순이 일어나지 않는다. 비자명한 등질 족 $X \rightarrow T$은 stack의 점들의 morphism으로 정확히 구별되고, classifying morphism $T \rightarrow \mathcal{M}$이 더 이상 상수가 아니라 그 twist를 식별하는 비자명한 자료가 된다. 이것이 stack이 "moduli 문제의 올바른 대상"인 까닭이다.

두 번째 보정은 stack을 포기하고 algebraic space의 세계에 머무르되, isomorphism class만을 담는 가장 좋은 근사를 찾는 것이다. Algebraic space는 그 자체로 $(\Sch, \et)$ 위의 sheaf이므로 ([§대수적 스택, ⁋정의 3](/ko/math/stacks/algebraic_stacks#def3)) $\underline{M}$과 같은 세계에 놓이며, scheme은 그 특수한 경우이다.

::: 정의 8
한 moduli 문제의 set-값 moduli functor $\underline{M}:\Sch^\op \rightarrow \Set$에 대하여, algebraic space $M$과 natural transformation $\Phi:\underline{M} \rightarrow M$의 쌍이 *coarse moduli space<sub>성긴 모듈라이 공간</sub>*라는 것은 다음 두 조건을 만족하는 것이다.

1. (보편성) 임의의 algebraic space $N$과 natural transformation $\Psi:\underline{M} \rightarrow N$에 대하여, $\Psi=\pi\circ \Phi$을 만족하는 morphism $\pi: M \rightarrow N$이 유일하게 존재한다. 곧 $\Phi$은 algebraic space로 가는 natural transformation들 가운데 initial object이다.

2. (기하적 점에서의 전단사) 임의의 algebraically closed field $\mathbb{K}$에 대하여, $\Phi$의 성분 $\Phi(\Spec \mathbb{K}):\underline{M}(\Spec \mathbb{K}) \rightarrow M(\mathbb{K})$이 전단사이다.
:::

조건 1은 $M$이 isomorphism class들을 담는 algebraic space 가운데 가장 보편적인 것, 곧 $\underline{M}$에서 algebraic space로 가는 모든 morphism이 $M$을 거쳐 가도록 하는 초기 대상임을 말한다. 조건 2는 $M$의 algebraically closed field 위의 점들이 정확히 분류 대상의 기하적 isomorphism class와 일대일대응함을 보장하여, $M$이 적어도 집합 수준에서는 올바른 매개변수 공간임을 확정한다. Fine moduli space는 자동으로 coarse moduli space이지만 ($\Phi$이 isomorphism이면 두 조건이 자명히 성립한다), 그 역은 성립하지 않는다. Coarse moduli space는 일반적으로 universal family를 가지지 않으며, 두 조건이 보장하는 것은 점들의 대응과 보편성뿐이다. 보편성에 의하여 coarse moduli space는 존재하면 유일한 isomorphism을 통해 유일하게 결정된다.

Coarse moduli space의 존재는 자명하지 않다. 그 일반적 존재를 보장하는 것이 Keel–Mori 정리로, moduli stack의 언어로 가장 깔끔하게 서술된다.

::: 정리 9 (Keel–Mori)
$\mathcal{M}$이 Noetherian base 위에서 locally of finite type인 algebraic stack이고, 그 inertia stack $I_\mathcal{M}=\mathcal{M}\times_{\mathcal{M}\times\mathcal{M}}\mathcal{M} \rightarrow \mathcal{M}$이 유한이라 하자. 그럼 $\mathcal{M}$의 coarse moduli space $\pi:\mathcal{M} \rightarrow M$이 존재한다. 여기에서 $M$은 algebraic space이고, $\pi$은 proper이며 기하적 점들의 isomorphism class 집합과 $M$의 기하적 점들 사이의 전단사를 유도한다. 특히 분리된 finite type Deligne–Mumford stack은 coarse moduli space를 가진다.
:::

여기에서 inertia stack $I_\mathcal{M} \rightarrow \mathcal{M}$은 각 geometric point 위에 그 stabilizer group scheme을 fiber로 얹는 stack이고, 그것이 유한하다는 것은 이 morphism이 finite morphism이라는 뜻이다. 증명은 이 글의 범위를 넘으므로 결론만 가져다 쓰고, 대신 그 가정이 어디에서 필요한지를 본다.

Stabilizer가 양의 차원을 가지는 stack은 이 정리의 적용 범위 밖이다. [§대수적 스택, ⁋예시 11](/ko/math/stacks/algebraic_stacks#ex11)의 $\bB\mathbb{G}_m$과 [§대수적 스택, ⁋예시 12](/ko/math/stacks/algebraic_stacks#ex12)의 $[\mathbb{A}^1/\mathbb{G}_m]$이 그러하다. 가령 $[\mathbb{A}^1/\mathbb{G}_m]$에서는 invariant ring이 $k[\x]^{\mathbb{G}_m}=k$이어서 algebraic space로 가는 임의의 natural transformation이 열린 orbit과 원점을 한 점으로 보내므로, [정의 8](#def8)의 둘째 조건이 깨져 그 뜻의 coarse moduli space가 아예 존재하지 않는다. 반면 분리된 finite type Deligne–Mumford stack에서는 diagonal이 proper이면서 unramified이므로 finite이고, inertia는 그 diagonal을 자기 자신을 따라 base change한 것이므로 함께 유한해진다. 다음 절의 타원곡선 moduli가 바로 이 상황에 해당한다.

## 타원곡선의 moduli $\mathcal{M}_{1, 1}$

앞서 도입한 두 보정을 한 예에서 동시에 관찰하기에 가장 좋은 대상이 section을 가진 타원곡선의 moduli $\mathcal{M}_{1,1}$이다. 이제 이 stack의 quotient presentation을 구성하고, automorphism 구조와 coarse moduli space를 정밀하게 분석한다.

Characteristic $0$의 algebraically closed field $k$ 위에서 section을 가진 타원곡선은 Weierstrass 방정식

$$\y^2=\x^3+a\x+b,\qquad \Delta=-16(4a^3+27b^2)\neq 0$$

으로 주어지고, 두 방정식이 같은 타원곡선을 정의하는 것은 좌표변환 $(\x, \y)\mapsto(\lambda^2 \x, \lambda^3 \y)$ ($\lambda\in \mathbb{G}_m$)으로 옮겨지는 것과 같다. 이 변환은 계수에 $\lambda\cdot(a, b)=(\lambda^4 a, \lambda^6 b)$으로 작용하므로, $\mathcal{M}_{1, 1}$은 quotient stack

$$\mathcal{M}_{1, 1}\cong \bigl[\{(a, b)\mid\Delta\neq 0\}\big/\mathbb{G}_m\bigr]$$

으로 실현된다. 한 점 $(a, b)$의 stabilizer는 $\lambda^4 a=a$, $\lambda^6 b=b$을 만족하는 $\lambda$들의 group이며, 이는 정확히 그 점이 나타내는 타원곡선 $(E, 0)$의 automorphism group $\Aut(E, 0)$과 일치한다.

이 stabilizer를 경우별로 계산하면 다음과 같다. $j$-불변량은

$$j=1728\frac{4a^3}{4a^3+27b^2}$$

으로 주어지고, $\mathbb{A}^1_j$의 좌표를 이룬다. 일반적인 점에서는 $a, b$이 모두 $0$이 아니어서 $\lambda^4=\lambda^6=1$, 곧 $\lambda^2=1$이 되어 stabilizer는 $\mu_2=\{\pm 1\}$이며, 이는 모든 타원곡선에 공통인 $[-1]$ automorphism에 대응한다. 특수한 두 점에서 이 stabilizer가 도약한다. $j=1728$ ($b=0$, 곧 $\y^2=\x^3+a\x$)에서는 $\lambda^4=1$만 요구되어 stabilizer가 $\mu_4$으로 커지고, $j=0$ ($a=0$, 곧 $\y^2=\x^3+b$)에서는 $\lambda^6=1$만 요구되어 $\mu_6$으로 커진다. $k$이 algebraically closed이므로 $\mu_n\cong \mathbb{Z}/n$이고, 곧

$$\Aut(E, 0)\cong \begin{cases}\mathbb{Z}/6 & j=0,\\ \mathbb{Z}/4 & j=1728,\\ \mathbb{Z}/2 & \text{otherwise}\end{cases}$$

이다. 공통의 $\mu_2$은 모든 $\Aut(E, 0)$의 center에 놓이므로 어느 점도 stabilizer를 잃지 않고, $j=0$과 $j=1728$에서는 그 공통 $\mu_2$을 넘어 automorphism이 각각 지수 $3$과 $2$만큼 더 커진다 ($\mu_6/\mu_2\cong \mathbb{Z}/3$, $\mu_4/\mu_2\cong \mathbb{Z}/2$). Stabilizer가 모두 유한하므로 $\mathcal{M}_{1, 1}$은 Deligne–Mumford stack이다. ([§대수적 스택, ⁋정리 10](/ko/math/stacks/algebraic_stacks#thm10))

::: 예시 10 ($j$-직선과 universal family의 부재)
$j$-불변량은 natural transformation $\Phi:\underline{M}_{1, 1} \rightarrow \mathbb{A}^1_j$을 주며, 이 쌍 $(\mathbb{A}^1_j, \Phi)$이 $\mathcal{M}_{1, 1}$의 coarse moduli space이다. 실제로 $\mathcal{M}_{1, 1}$은 분리된 finite type Deligne–Mumford stack이므로 [정리 9](#thm9)에 의하여 coarse moduli space를 가지며, algebraically closed field 위에서 타원곡선의 isomorphism class가 $j$-불변량으로 완전히 결정되므로 [정의 8](#def8)의 둘째 조건이 성립하여 그 coarse 공간은 $\mathbb{A}^1_j$이다. 그러나 $\mathbb{A}^1_j$ 위에는 보편 타원곡선이 존재하지 않는다. 만일 존재한다면 $\mathbb{A}^1_j$이 fine moduli space가 되어 [명제 5](#prop5)에 위배되기 때문이다. 곧 모든 타원곡선이 갖는 $[-1]$ automorphism이 [예시 6](#ex6)의 비자명한 이차 twist를 낳고, 이 twist는 $j$가 상수인 비자명한 등질 족이어서 $\mathbb{A}^1_j$로의 classifying morphism이 그것을 식별하지 못한다. 반면 stack $\mathcal{M}_{1, 1}$ 위에서는 항등 morphism이 보편 타원곡선을 주며, 이 twist는 $T \rightarrow \mathcal{M}_{1, 1}$의 비자명한 자료로 정확히 구별된다.
:::

예시 10은 fine, coarse, stack의 세 층위를 한눈에 보여준다. $\mathbb{A}^1_j$은 기하적 isomorphism class를 점으로 올바르게 담지만 universal family를 잃은 coarse moduli space이고, $\mathcal{M}_{1, 1}$은 automorphism을 기억하여 universal family를 회복한 moduli stack이며, 둘을 잇는 morphism $\mathcal{M}_{1, 1} \rightarrow \mathbb{A}^1_j$이 정확히 stabilizer 정보를 잊는 coarse morphism이다. $j=0$과 $j=1728$에서 stack은 더 큰 automorphism group을 가진 "더 무거운" 점을 두는 반면 coarse 공간은 평범한 점만을 두며, 이 차이가 두 대상이 다른 본질적인 이유이다.

## Moduli of curves와 vector bundle moduli

타원곡선 다음으로 자연스러운 일반화는 genus $g$ 곡선의 moduli이다. $g\geq 2$인 smooth projective curve의 moduli stack $\mathcal{M}_g$과, 거기에 서로 다른 $n$개의 marked point를 더한 $\mathcal{M}_{g, n}$은 모두 분리된 finite type Deligne–Mumford stack이며, 따라서 [정리 9](#thm9)에 의하여 coarse moduli space $M_g$, $M_{g, n}$을 가진다. 이들이 Deligne–Mumford인 까닭은, $2g-2+n>0$인 $n$-pointed genus $g$ curve의 automorphism group scheme이 항상 유한하고 unramified하다는 사실에 있다. $\mathcal{M}_g$의 차원은 $3g-3$이며, Deligne와 Mumford는 stable curve를 더해 $\mathcal{M}_g$을 proper한 stack $\overline{\mathcal{M}}_g$으로 compactify할 수 있음을 보였다. 이 정밀한 구성과 그 기하는 별도의 깊은 이론을 이루므로 여기에서는 언급에 그친다.

또 다른 방향은 고정된 projective variety $X$ 위의 vector bundle 또는 coherent sheaf의 moduli이다. 이 경우 두 가지 어려움이 동시에 등장한다. 하나는 boundedness이다. Vector bundle 전체를 분류하려 하면 그 isomorphism class들이 bounded가 되지 않아 finite type 대상으로 매개변수화되지 않는다. 가령 $\mathbb{P}^1$ 위의 line bundle $\mathcal{O}(d)$는 rank $1$이라 모두 stable이지만 $d$이 $\mathbb{Z}$ 전체를 훑으면 어떤 finite type 족에도 담기지 않으므로, stability만으로는 boundedness가 나오지 않는다. Polarization을 고정하고 Hilbert 다항식 (곡선 위에서는 rank와 degree)을 함께 고정한 뒤 *stability*라 부르는 조건을 얹어 대상을 semistable sheaf로 제한해야 비로소 bounded인 족이 얻어진다. 다른 하나는 automorphism으로, stability는 이것을 없애 주지 않는다. Stable bundle조차 scalar automorphism $\mathbb{G}_m$을 그대로 가지므로 이 moduli는 fine이 되지 못하고, coarse moduli space 또는 moduli stack의 수준에서 서술된다. 구성 자체는 적절한 Quot scheme 위에서 group action의 geometric invariant theory quotient를 취하는 방식으로 이루어지며, stability의 선택에 따라 결과로 얻는 moduli 공간이 달라진다. Stability와 GIT의 전개는 이 글의 범위를 넘으므로 다른 글로 미룬다.

---

**참고문헌**

**[GIT]** D. Mumford, J. Fogarty, F. Kirwan, *Geometric invariant theory*, 3rd ed., Springer, 1994.  
**[FGA]** B. Fantechi, L. Göttsche, L. Illusie, S. L. Kleiman, N. Nitsure, A. Vistoli, *Fundamental algebraic geometry: Grothendieck's FGA explained*, American Mathematical Society, 2005.  
**[HM]** J. Harris, I. Morrison, *Moduli of curves*, Springer, 1998.  
**[Stacks]** The Stacks Project Authors, *The Stacks Project*, https://stacks.math.columbia.edu.
