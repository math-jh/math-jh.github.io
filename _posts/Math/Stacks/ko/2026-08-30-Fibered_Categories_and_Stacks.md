---
title: "스택"
description: "Moduli 문제가 집합이 아니라 groupoid를 값으로 가짐을 동기로, base 위의 fibered category와 groupoid에 의한 fibration을 정의하고, site 위에서 descent가 성립하는 stack의 개념을 faithfully flat descent의 일반화로 도입한다."
excerpt: "Groupoids, categories fibered in groupoids, descent, and the definition of a stack"

categories: [Math / Stacks]
permalink: /ko/math/stacks/fibered_categories_and_stacks
sidebar: 
    nav: "stacks-ko"

date: 2026-08-30
weight: 2


---

우리가 다룰 stack은 본질적으로 moduli problem에서 온 것으로, 이러한 문제의 대표적인 예시는 [\[대수적 위상수학\] §분류공간, ⁋정리 8](/ko/math/algebraic_topology/classifying_spaces#thm8)에서 살펴본, 위상공간 $X$ 위의 principal $G$-bundle, 혹은 rank $r$의 vector bundle 등을 분류하는 문제이다. 우리가 [\[스킴\] §점함자](/ko/math/scheme_theory/functor_of_points)에서 도입한 functor of points의 관점으로 얻는 가장 좋은 사실은 이 문제의 대수기하학적 형태에서 이러한 종류의 대응

$$F:\Sch^\op\rightarrow \Set;\qquad T\mapsto \{\text{principal $G$-bundles over $T$}\}$$

을 functor 그 자체로 생각한 후, 이 functor가 실제로 scheme에 의해 represent되는지를 살펴볼 수 있다는 것이다. 그러나 이 식 자체는 잘 정의된 functor가 아닌데, 핵심적인 이유는 이 대응의 functoriality를 보이기 위해서는 morphism $f:Y\rightarrow X$에 대한 bundle의 pullback $f^\ast P$를 이용하여 $X$ 위의 bundle을 $Y$ 위로 옮겨와야 하지만, pullback bundle 자체가 태생부터 unique isomorphism에 대해서만 유일하게 결정되기 때문이다.

위상수학에서 이를 해결하는 방식은 간단했다. 위와 같은 naive한 대응 대신, $\hTop$에서 모든 것을 해결한다. 즉 다음의 대응

$$X\mapsto \{\text{principal $G$-bundles over $X$}\}/{\cong}$$

을 생각하면 된다. 그럼 이 이론의 중요한 결과는 $G$의 classifying space $\B G$ 위에 universal bundle $\E G\rightarrow\B G$가 존재하며, 이를 pullback하는 대응이 전단사

$$[X,\B G]\xrightarrow{\sim}\{\text{principal $G$-bundles over $X$}\}/{\cong};\qquad [f]\mapsto[f^\ast\E G]$$

를 준다는 것이었다. 이를 작동하게 하는 것이 $\E G$가 contractible이라는 조건으로, 두 classifying map의 pullback이 isomorphic하면 그 bundle에서 $\E G$로 가는 두 $G$-equivariant map이 homotopic하고, 따라서 두 classifying map도 homotopic하다. 즉 이 분류정리는 bundle isomorphism과 morphism 사이의 homotopy를 각각 동치관계로 죽인 뒤 얻은 두 집합이 같다는 명제이다.

문제는 대수기하학의 언어는 위상수학의 언어보다 rigid하여 이와 같이 homotopy를 담아줄 수 없다는 것에 있다. 이에 대한 해결책은 isomorphism을 죽이지 않고 모두 살려두는 것이며, 이로 인해 moduli functor $F$는 이제 $\Set$-valued가 아닌 $\Grpd$-valued가 된다.

## 준군

우선 다음 정의를 기억하자.

::: 정의 1
Category $\mathcal{G}$가 *groupoid<sub>준군</sub>*라는 것은 $\mathcal{G}$의 모든 morphism이 isomorphism인 것이다. ([\[범주론\] §범주, ⁋정의 11](/ko/math/category_theory/categories#def11))
:::

[\[범주론\] §범주, ⁋정의 10](/ko/math/category_theory/categories#def10)에서 우리는 모든 morphism이 isomorphism이고, 대상이 하나뿐인 category를 group으로 정의했다. 따라서 groupoid $\mathcal{G}$의 한 대상 $x\in \mathcal{G}$에 대하여 $\Aut_\mathcal{G}(x)=\Hom_\mathcal{G}(x, x)$은 합성에 대하여 group을 이루며, 이를 $x$의 *automorphism group*이라 부른다. Groupoid들을 대상으로, 그들 사이의 functor를 morphism으로 하는 category를 $\Grpd$로 적는다.

이와 같이 groupoid는 group의 일반화로 볼 수 있으나, 이것이 전부는 아니다. 우리에게 유용한 관점은 이것이 집합의 일반화로 볼 수도 있다는 것으로, 임의의 집합은 morphism이 항등사상 뿐인 category로 볼 수 있기 때문이다. 그럼 groupoid $\mathcal{G}$는 집합과 마찬가지로 여러 개의 대상을 가지지만, 그 사이의 isomorphism 구조 또한 가지고 있는 대상이다.

도입부에서 살펴본 예시에서, 고정된 공간 $X$ 위의 principal $G$-bundle들을 모두 모아둔 것이 groupoid 구조에 해당한다. 그럼 여기에서 isomorphism class를 취해 하나씩의 representative만 남겨둔 것은 groupoid $\mathcal{G}$의 skeleton $\sk\mathcal{G}$를 하나 고르는 것에 해당한다. 즉 $\sk \mathcal{G}$는 $\mathcal{G}$의 isomorphism class들의 모임과 같다. 한편 skeleton은 full subcategory이므로 각 representative $x$의 automorphism group $\Aut_\mathcal{G}(x)$를 그대로 보존하는데, 이들 automorphism의 정보까지 잊고 나면 discrete groupoid, 즉 집합이 얻어지게 되는 것이다.

::: 예시 2
다음은 우리가 자세히 살펴볼 groupoid의 예시들이다.

1. 고정된 scheme $T$에 대하여, $T$ 위의 line bundle들을 대상으로 하고 line bundle 사이의 $\mathcal{O}_T$-module들 사이의 isomorphism을 morphism으로 하는 category는 groupoid이며, 각 대상 $\mathcal{L}$의 automorphism group은 $\Aut(\mathcal{L})=\Gamma(T, \mathcal{O}_T)^\ast=\mathbb{G}_m(T)$이다. 그럼 위와 같은 식으로 이 groupoid의 isomorphism class들의 집합을 얻어내면 그것이 정확히 Picard group $\Pic(T)$가 되며, 이는 automorphism group $\mathbb{G}_m(T)$의 정보를 잊어버리는 것이다.
2. 또 다른 친숙한 예시는 위상공간 $X$의 *fundamental groupoid* $\Pi_1(X)$이다. ([\[대수적 위상수학\] §호모토피, ⁋정의 11](/ko/math/algebraic_topology/homotopy#def11)) 이는 점을 대상으로, path의 homotopy class를 morphism으로 하는 category이며, 이 때 한 점에서의 automorphism group이 정확히 fundamental group $\pi_1(X,x)$가 된다.
3. 우리의 이야기 흐름에서 자명한 예시로, 임의의 functor $F:\mathcal{C}^\op \rightarrow \Set$은 각 $T$에 discrete groupoid $F(T)$을 주는 특수한 경우이다. 즉, $\Set$-valued functor는 $\Grpd$-valued functor의 특수한 예시이다.
:::

특히 첫째 예시가 우리가 주로 살펴볼 대상이다. 일반적으로 $\Pic(T)$에는 nontrivial line bundle $\mathcal{L}$이 있을 수 있지만, line bundle의 정의에 의하여 $\mathcal{L}$은 locally trivial하다. [\[스킴\] §충실평탄하강, ⁋정리 11](/ko/math/scheme_theory/faithfully_flat_descent#thm11)에서 보았듯, covering 위의 local trivial line bundle들과 겹침 위에서 이들을 잇는 isomorphism들을 descent datum으로 주면 effective descent에 의하여 하나의 global line bundle이 얻어진다. [\[스킴\] §군 스킴, ⁋예시 15](/ko/math/scheme_theory/group_schemes#ex15)의 $\mathbb{G}_m$-torsor를 붙이는 transition data가 바로 이러한 isomorphism들이다. 따라서 모두 locally trivial해 보이는 line bundle들을 구별하려면 이 isomorphism들을 잊지 않고 기록해야 한다.

## 유사함자

한편 도입부에서 살펴봤던 principal $G$-bundle들의 moduli functor $F$를 생각하면, 이 functor가 내놓은 집합을 isomorphism class로 내려야 했던 직관적인 이유는 pullback 때문이었다. 이는 functor의 target을 $\Grpd$-valued로 올린다고 해결되는 일이 아니다. 따라서 우리는 $F$의 functoriality를 엄밀한 의미에서 얻기 위해서는 그 functoriality를 주는 pullback

$$f^\ast=F(f): F(V)\rightarrow F(U)$$

을 잘 정의해야 하며, 바꿔 말하면 각각의 $f: U\rightarrow V$와 $V$ 위의 대상이 주어졌을 때, 그 pullback representation을 일관적으로 골라주는 <em-ko>선택</em-ko>을 해 주어야 한다. 그리고, 이러한 선택을 어떻게 하든 두 morphism의 합성

$$U\overset{f}{\longrightarrow}V\overset{g}{\longrightarrow}W$$

에 대한 pullback은 이제 더 이상 두 pullback의 합성과 같지 <em-ko>않고</em-ko>, 오직 이 둘 사이의 isomorphism 

$$\varepsilon_{f, g}: f^\ast g^\ast P \xRightarrow{\sim} (g\circ f)^\ast P$$

이 존재하는 정도로 만족해야 한다. Pseudofunctor의 아이디어는 이들 모두를 자료로 받고, 이들이 모순없는 데이터를 정의하기를 요구하는 것이다. 

::: 정의 3
Category $\mathcal{C}$ 위의 *pseudofunctor<sub>유사함자</sub>* $F:\mathcal{C}^\op \rightarrow \Grpd$는 다음 자료로 이루어진다.

1. 각 대상 $U\in \mathcal{C}$에 대응되는 groupoid $F(U)$,
2. 각 morphism $f: U \rightarrow V$마다 대응되는 functor $f^\ast: F(V) \rightarrow F(U)$,
3. 각 합성가능한 쌍 $U\overset{f}{\longrightarrow}V\overset{g}{\longrightarrow}W$마다 정의된 natural isomorphism 
    
    $$\varepsilon_{f, g}: f^\ast\circ g^\ast \xRightarrow{\sim} (g\circ f)^\ast,$$

    그리고 각각의 대상 $U$마다 정의된 natural isomorphism

    $$\eta_U:\id_{F(U)}\xRightarrow{\sim}(\id_U)^\ast.$$

이들이 만족해야 하는 compatibility condition은 다음과 같다. 

> 세 morphism $U\overset{f}{\longrightarrow}V\overset{g}{\longrightarrow}W\overset{h}{\longrightarrow}Z$에 대하여
> 
> $$\varepsilon_{f, h\circ g}\circ(\id_{f^\ast}\ast \varepsilon_{g, h})=\varepsilon_{g\circ f, h}\circ(\varepsilon_{f, g}\ast \id_{h^\ast})$$
> 
> 이 성립하고, 임의의 morphism $f: U\rightarrow V$에 대하여
> 
> $$\varepsilon_{f, \id_V}\circ(\id_{f^\ast}\ast \eta_V)=\id_{f^\ast},\qquad \varepsilon_{\id_U, f}\circ(\eta_U\ast \id_{f^\ast})=\id_{f^\ast}$$
> 
> 이 성립한다.
:::

정의 3의 자료들과 조건들은 다음과 같이 다이어그램으로 시각화할 수 있다. 우선 조건 3의 natural isomorphism $\varepsilon_{f,g}$와 $\eta_U$는 각각 다음의 diagram이 나타내는 두 path 사이의 2-morphism으로 나타난다.

{% diagram Math/Stacks/Fibered_Categories_and_Stacks-1.svg width="29.13em" alt="합성 동형과 항등 동형" %}

Compatibility에서 등장하는 $\ast$는 $2$-morphism들의 horizontal composition으로, 예를 들어 첫째 등식은 다음의 diagram

{% diagram Math/Stacks/Fibered_Categories_and_Stacks-2.svg width="17.76em" alt="결합 정합성" %}

이 commute함을 뜻하고, 둘째 등식은 다음의 diagram

{% diagram Math/Stacks/Fibered_Categories_and_Stacks-3.svg width="25.28em" alt="unit coherence" %}

들이 각각 commute함을 뜻하는 것이다. 만일 모든 $\varepsilon_{f, g}$와 $\eta_U$이 항등사상이라면, $F$는 pseudofunctor에 그치지 않고  통상적인 functor $\mathcal{C}^\op \rightarrow \Grpd$이 되며, 이 경우를 *strict* functor라 부른다. 

결국 정의는 다소 복잡하고 길지만 핵심적인 관찰은 위에서 살펴봤듯 각 $f: U\rightarrow V$와 대상마다 구체적인 pullback을 고르는 선택을 추가적인 데이터로 넣는다는 것이며, 이러한 선택은 *cleavage*라 부른다. 

## 준군값 올범주

Pseudofunctor는 presheaf $\mathcal{C}^\op\rightarrow \Set$을 일반화하는 개념이라는 점에서 친숙하지만, 이를 본격적인 계산에 활용하려면 챙겨야 할 isomorphism만 벌써 두 종류가 있다. 이번 섹션에서 다룰 category fibered over groupoid는 본질적으로 이와 동등한 데이터를 담은 대상이지만, 위와 같이 isomorphism들의 선택을 하나하나 기억하는 대신 이를 Cartesian diagram 안에 숨겨둔다.

기본적인 아이디어는 다음과 같다. 앞서 우리는 각 대상 $U$마다 groupoid $F(U)$을 따로 두었는데, 이 대신 모든 $F(U)$의 대상을 하나의 category $\mathcal{F}$에 모은다. 여기에서 원래의 $F(U)$들을 복원하기 위해서는 각 대상이 어떤 $U$ 위에 놓이는지를 보는 projection functor $P: \mathcal{F}\rightarrow \mathcal{C}$가 필요하다. 이 관점의 핵심 아이디어는 pullback $f^\ast$가 $\mathcal{F}$에서의 *Cartesian morphism*으로 들어간다는 것으로, 이 Cartesian morphism의 universal property가 바로 위에서의 isomorphism의 선택을 숨겨두고 있는 데이터이다.

::: 정의 4
Functor $P:\mathcal{F}\rightarrow \mathcal{C}$를 고정하자. $\mathcal{F}$의 morphism $\varphi: \xi\rightarrow \eta$가 $\mathcal{C}$의 morphism $f: U\rightarrow V$의 *lift*라는 것은 $P(\varphi)=f$인 것이다. 이 때 $f$의 lift $\varphi$가 *cartesian morphism<sub>데카르트 사상</sub>* (혹은 *cartesian lift*)이라는 것은 다음의 universal property를 만족하는 것이다.

> $\mathcal{F}$의 임의의 대상 $\zeta$와 morphism $\psi:\zeta \rightarrow \eta$, 그리고 $h: P(\zeta)\rightarrow U$가 $f\circ h=P(\psi)$를 만족할 때마다, $h$의 lift이자 $\varphi\circ \chi=\psi$를 만족하는 morphism $\chi:\zeta \rightarrow \xi$가 유일하게 존재한다.
:::

이는 대략적으로 다음의 diagram을 생각하면 cartesian morphism이라는 이름이 정당함을 알 수 있다.

{% diagram Math/Stacks/Fibered_Categories_and_Stacks-4.svg width="14.13em" alt="cartesian morphism의 보편성" %}

그럼 이 Cartesian morphism의 보편성은 이 조건을 만족하는 $\xi$가 존재한다면 unique isomorphism에 대해 유일하게 결정되며, 이러한 방식으로 $\varepsilon$과 $\eta$를 숨겨둔 것이다. 그럼 우리는 이 $\xi$을 $f^\ast \eta$로 적고 $\eta$의 $f$를 따른 *pullback*이라 부른다. 이제 모든 morphism이 이런 pullback으로 분해되고 각 fiber가 groupoid가 되도록 요구하면 *category fibered in groupoids*의 개념을 얻는다.

::: 정의 5
Functor $P:\mathcal{F} \rightarrow \mathcal{C}$가 *category fibered in groupoids<sub>준군값 올범주</sub>*라는 것은 다음 두 조건을 만족하는 것이다.

1. 임의의 morphism $f: U \rightarrow V$와 $V$ 위의 대상 $\eta$에 대하여, $f$의 lift이자 공역이 $\eta$인 cartesian morphism $\varphi:\xi \rightarrow \eta$이 존재한다.
2. $\mathcal{F}$의 모든 morphism이 cartesian이다.

이 때, 대상 $U\in \mathcal{C}$에 대하여, $U$ 위에 놓인 대상들과 $\id_U$의 lift인 morphism들로 이루어진 $\mathcal{F}$의 subcategory를 $U$ 위의 *fiber<sub>올</sub>* $\mathcal{F}(U)$라 부른다.
:::

각 morphism $f:U\rightarrow V$와 대상 $\eta\in\mathcal{F}(V)$에 대하여 cartesian lift $f^\ast\eta\rightarrow\eta$을 하나씩 고르는 것을 *cleavage*라 부른다. Cleavage는 보편성에 의해 isomorphism까지 유일한 pullback들 가운데 실제 대표를 일관되게 골라 pullback functor를 정의하기 위한 선택이다.

::: 명제 6
CFG $P:\mathcal{F} \rightarrow \mathcal{C}$에 대하여, 다음이 성립한다.

1. 각 fiber $\mathcal{F}(U)$은 groupoid이다.
2. Cleavage를 하나 고르면 각 morphism $f:U\rightarrow V$에 대하여 functor $f^\ast:\mathcal{F}(V) \rightarrow \mathcal{F}(U)$이 정의되며, 다른 선택은 이 functor를 canonical natural isomorphism을 제외하고 바꾸지 않는다. 나아가 합성가능한 $U\xrightarrow{f}V\xrightarrow{g}W$에 대하여 canonical natural isomorphism $f^\ast\circ g^\ast\cong(g\circ f)^\ast$이 있다.
:::
::: 증명
1. 우선 $\alpha:\xi \rightarrow \eta$이 $\id_U$의 lift인 morphism이라 하자. $\mathcal{F}$의 모든 morphism이 cartesian이므로 $\alpha$는 cartesian morphism이다. 따라서 cartesian morphism의 보편성을 $\psi=\id_\eta$와 $h=\id_U$에 적용하면 $\alpha\circ \theta=\id_\eta$이고 $P(\theta)=\id_U$인 $\theta:\eta \rightarrow \xi$이 유일하게 존재하여 $\alpha$의 오른쪽 역사상을 얻는다. 같은 방식으로 $\theta$ 또한 cartesian morphism이므로, 보편성을 적용하면 $\theta\circ \theta'=\id_\xi$이고 $P(\theta')=\id_U$인 $\theta':\xi \rightarrow \eta$을 얻는다. 이제 $\alpha\circ \theta=\id_\eta$으로부터

    $$\alpha=(\alpha\circ \theta)\circ \theta'=\theta'$$

    이므로 $\alpha$와 $\theta$는 서로의 역이다. 즉 $\mathcal{F}(U)$의 모든 morphism이 가역이므로 $\mathcal{F}(U)$은 groupoid이다.

2. Cleavage를 고정하자. 그럼 우선 $\eta\in \mathcal{F}(V)$마다 cartesian lift $\varphi_\eta:f^\ast \eta\rightarrow\eta$가 주어져 있다. 이제 $\mathcal{F}(V)$의 morphism $\beta:\eta \rightarrow \eta'$에 대하여, 합성 $\beta\circ \varphi_\eta:f^\ast \eta \rightarrow \eta'$과 $\eta$의 cartesian morphism $\varphi_{\eta'}:f^\ast \eta' \rightarrow \eta'$ 및 $h=\id_U$에 cartesian morphism의 universal property를 적용하면 $\varphi_{\eta'}\circ \theta=\beta\circ \varphi_\eta$이고 $P(\theta)=\id_U$인 $\theta:f^\ast \eta \rightarrow f^\ast \eta'$이 유일하게 정해지고, 따라서 이를 $f^\ast\beta$로 정의할 수 있다. 그럼 유일성에 의해 $f^\ast(\beta'\circ \beta)=f^\ast \beta'\circ f^\ast \beta$과 $f^\ast \id=\id$임을 쉽게 보일 수 있으므로 $f^\ast$은 functor이다.

    만일 위에서 다른 cleavage $\widetilde{\varphi}_\eta:\widetilde{f^\ast \eta}\rightarrow\eta$을 골랐다면, 두 cartesian morphism의 universal property로 $\widetilde{f^\ast \eta}\cong f^\ast \eta$인 isomorphism이 $\eta$에 대하여 자연스럽게 존재한다.

    마지막으로 $f^\ast g^\ast \eta \rightarrow g^\ast \eta \rightarrow \eta$의 합성은 $g\circ f$ 위에 놓인 cartesian morphism이고 $(g\circ f)^\ast \eta \rightarrow \eta$ 또한 그러하므로, universal property에 의해 isomorphism $f^\ast g^\ast \eta\cong(g\circ f)^\ast \eta$을 얻는다.
:::

즉, CFG가 주어지면 cleavage를 통해 pseudofunctor를 재현해낼 수 있으며, 이는 cleavage의 선택에 대해 오직 canonical natural isomorphism만큼만 다르다. 우리 주장은 거꾸로 pseudofunctor가 CFG를 주고, 따라서 두 데이터는 정확히 같은 정보를 담고 있다는 것이다. 이 양방향 대응을 정밀하게 진술하기 위해 먼저 CFG 사이의 morphism을 정의한다.

::: 정의 7
두 CFG $P:\mathcal{F} \rightarrow \mathcal{C}$과 $Q:\mathcal{G} \rightarrow \mathcal{C}$ 사이의 *morphism*은 $Q\circ G=P$을 만족하는 functor $G:\mathcal{F} \rightarrow \mathcal{G}$이다. 두 morphism $G, G':\mathcal{F} \rightarrow \mathcal{G}$ 사이의 *2-morphism*은 natural transformation $\alpha: G\Rightarrow G'$으로서 각 성분 $\alpha_\xi$이 $\id_{P(\xi)}$ 위에 놓이는 것이다.
:::

그럼 우선 CFG들 사이의 morphism은 cartesian morphism을 cartesian morphism으로 보낸다는 것을 쉽게 확인할 수 있다. 또, 위 정의에 의해 CFG들의 category는 2-category를 이룬다. 위의 조건에서 $2$-morphism의 각 성분이 $\id$ 위에 놓인다는 조건은 그것이 어떤 fiber $\mathcal{G}(U)$ 안의 morphism이라는 것으로, 특히 $\mathcal{G}(U)$가 [명제 6](#prop6)에 의해 groupoid이므로 $2$-morphism은 항상 natural isomorphism이 된다. 그럼 다음이 성립한다.

::: 정리 8 (Grothendieck)
Category $\mathcal{C}$ 위의 CFG들이 이루는 2-category와 pseudofunctor $\mathcal{C}^\op \rightarrow \Grpd$들이 이루는 2-category는 2-equivalent하다.
:::

우리는 이에 대한 증명은 생략하지만, pseudofunctor $F$에 대응되는 *Grothendieck construction* $\int_\mathcal{C}F$ 자체는 이미 친숙한 것이다. ([\[범주론\] §표현가능한 함자, ⁋정의 7](/ko/math/category_theory/representable_functors#def7)) 이 category의 대상은 $U\in \mathcal{C}$, $x\in F(U)$의 pair $(U, x)$이고, $(U, x)$에서 $(V, y)$로의 morphism은 $f: U \rightarrow V$, $\alpha: x\xrightarrow{\sim}f^\ast y$ in $F(U)$의 pair $(f, \alpha)$이며, projection $(U, x)\mapsto U$이 이를 CFG로 만든다.

어쨌든 [정리 8](#thm8)에 의하여 우리는 "base category 위에서 변하는 groupoid"를 pseudofunctor로도, CFG로도 자유롭게 기술할 수 있다. 이후로는 두 언어를 맥락에 따라 섞어 쓰며, 특히 정의는 CFG로 깔끔하게 하되 구체적 계산은 pseudofunctor의 pullback $f^\ast$과 $x\vert_V$ 같은 표기로 수행한다. 다음 예시들이 이 글의 주요 대상이다.

::: 예시 9
1. 고정된 대상 $X\in \mathcal{C}$에 대하여 slice category $\mathcal{C}_{/X}$에 projection $P:(T \rightarrow X)\mapsto T$를 준 구조는 CFG이다. 이 때, $T$ 위의 fiber $\mathcal{C}_{/X}(T)$는 그 정의에 의해 morphism들의 집합 $\Hom_\mathcal{C}(T, X)$를 discrete groupoid로 본 것이며, 이는 functor of points $h_X$에 대응하는 CFG이다.

2. Scheme $T$와 그 위의 quasi-coherent sheaf $\mathcal{F}$로 이루어진 pair들 $(T, \mathcal{F})$를 대상으로 갖는 category $\mathcal{QCoh}$를 생각한다. 이 때 두 대상 $(T, \mathcal{F})$에서 $(T', \mathcal{F}')$로의 morphism은 $f: T \rightarrow T'$와 quasi-coherent sheaf들 사이의 isomorphism $\alpha: \mathcal{F}\xrightarrow{\sim}f^\ast \mathcal{F}'$의 pair $(f, \alpha)$으로 주어진다. 여기에 projection $(T, \mathcal{F})\mapsto T$를 주면 이는 CFG가 되며, $T$ 위의 fiber $\mathcal{QCoh}(T)$는 $T$ 위의 quasi-coherent sheaf들의 groupoid $\QCoh(T)$가 된다. 여기서 $\QCoh(T)$는 isomorphism만 morphism으로 취한 것이다. 

3. 도입부에서 살펴본 principal $G$-bundle의 예시와 비슷하게, 우리는 어떤 기하학적 대상의 $T$-family들을 대상으로 하고, 이 family들 사이의 isomorphism을 morphism으로 갖는 category를 생각한 후 위의 두 경우와 마찬가지로 projection을 주면 CFG를 얻는다. 이러한 상황을 *moduli problem*이라 부른다. 
:::

## 하강

도입부에서처럼 moduli problem을 set-valued presheaf $F$로 적으면, 이를 <em-ko>푸는</em-ko> 것은 $F$와 naturally isomorphic한 functor of points $h_X$를 갖는 기하학적 대상 $X$를 찾는 것이다. 우리는 지금까지 이 target을 $\Grpd$로 바꾸어 family와 그 사이의 isomorphism을 모두 기억하는 언어를 마련했지만, 이것만으로 representability나 local-to-global 성질이 보장되지는 않는다.

이 섹션에서 우리는 이러한 representability 문제가 moduli functor가 sheaf가 되는 것과 밀접한 관련이 있다는 것을 보인다. Sheaf condition을 말하려면 먼저 base category에 topology를 주어야 한다. 지금까지의 정의에는 topology가 쓰이지 않았으므로, covering 위의 compatible한 대상과 isomorphism이 global 대상으로 붙는다는 보장은 없다. Stack은 CFG에 [§그로텐디크 위상, ⁋정의 6](/ko/math/stacks/grothendieck_topology#def6)의 covering에 대한 descent 조건을 부과한 $\Grpd$-valued sheaf이다. 

이 섹션에서 $(\mathcal{C}, \tau)$은 site이고, 위상은 covering family $\{U_i \rightarrow U\}$로 주어지는 pretopology로 기술하기로 한다. ([§그로텐디크 위상, ⁋정의 4](/ko/math/stacks/grothendieck_topology#def4)) 또, CFG를 다룰 때는 $P:\mathcal{F} \rightarrow \mathcal{C}$의 cleavage를 하나 고정하여 $f: V\rightarrow U$의 pullback $f^\ast$과 restriction $x\vert_V=f^\ast x$을 사용한다.

::: 정의 10
CFG $P:\mathcal{F} \rightarrow \mathcal{C}$와 대상 $U\in \mathcal{C}$, 그리고 두 대상 $x, y\in \mathcal{F}(U)$이 주어졌다 하자. $U$ 위의 *Isom presheaf<sub>Isom 준층</sub>*는 다음의 대응

$$\rIsom_U(x, y):(\mathcal{C}_{/U})^\op \rightarrow \Set;\qquad (f: V \rightarrow U)\mapsto \Hom_{\mathcal{F}(V)}(f^\ast x, f^\ast y)$$

으로 정의된, slice site $\mathcal{C}_{/U}$ 위의 presheaf이다.
:::

이 presheaf에서 $\mathcal{C}_{/U}$의 morphism $g: W \rightarrow V$에 대한 restriction map은 pullback $g^\ast$과 isomorphism $g^\ast f^\ast\cong(f\circ g)^\ast$으로 유도된다. 구체적으로 $V$ 위의 isomorphism $\beta: f^\ast x\xrightarrow{\sim}f^\ast y$을 $W$로 restrict하면

$$g^\ast\beta: g^\ast f^\ast x\rightarrow g^\ast f^\ast y$$

을 얻는다. 이는 $g^\ast$이 functor이므로 isomorphism이고, 양 끝을 $g^\ast f^\ast\cong(f\circ g)^\ast$으로 identify하면 $\rIsom_U(x,y)(W)$의 원소가 된다.

앞서 설명한 전략에서 CFG는 $\Grpd$-valued presheaf에 해당하므로, 이를 $\Grpd$-valued sheaf로 만들려면 covering 위의 local fiber groupoid들을 하나의 global fiber groupoid로 붙일 수 있어야 한다. Groupoid는 대상과 그 사이의 isomorphism들로 이루어지므로, 여기에는 morphism을 붙이는 문제와 대상을 붙이는 문제가 함께 들어 있다.

먼저 morphism을 붙이는 문제를 생각하자. 고정된 두 대상 $x,y\in\mathcal{F}(U)$에 대하여, $\rIsom_U(x,y)$은 이 둘의 restriction 사이에 존재하는 local isomorphism들을 모은 presheaf이다. 여기서는 local isomorphism들의 source와 target이 이미 global 대상 $x,y$의 restriction으로 주어져 있다. 이 presheaf가 sheaf라는 것은 covering 위에서 주어진 local isomorphism들이 overlap에서 일치할 때 유일한 global isomorphism으로 붙는다는 뜻이다. 이것이 morphism에 대한 descent이며, [\[스킴\] §충실평탄하강, ⁋정리 6](/ko/math/scheme_theory/faithfully_flat_descent#thm6)의 categorical equivalence에서는 full faithfulness에 해당한다.

대상을 붙이는 문제에서는 global 대상이 미리 주어져 있지 않다. 따라서 각 $U_i$ 위의 대상 $x_i$뿐 아니라 overlap $U_{ij}$ 위에서 이들을 identify하는 isomorphism $\varphi_{ij}$도 함께 주어야 한다. 이들은  $x_i$들을 어떻게 붙일지를 지정하는 자료이며, 이들이 cocycle 조건을 만족할 때 얻는 것이 descent datum이다. 이 descent datum이 실제 global 대상의 restriction으로부터 오는지를 묻는 것이 대상에 대한 effective descent이고, 위 categorical equivalence에서는 essential surjectivity에 해당한다. Full faithfulness만으로 essential surjectivity가 따라오지는 않으므로, morphism을 붙일 수 있다는 사실만으로 대상을 붙일 수 있는 것은 아니다. 이는 [\[스킴\] §충실평탄하강, ⁋정의 4](/ko/math/scheme_theory/faithfully_flat_descent#def4)의 descent datum을 임의의 CFG로 옮긴 것이다.

이를 위해 다음 정의에서 사용할 표기를 고정하자. 주어진 covering family $\{f_i: U_i \rightarrow U\}_{i\in I}$에 대하여,

$$U_{ij}=U_i\times_U U_j,\qquad U_{ijk}=U_i\times_U U_j\times_U U_k$$

등과 같이 적고, projection $\pr: U_{ij} \rightarrow U_i$ 등을 따른 pullback을 $\vert_{U_{ij}}$로 표기하자. 

::: 정의 11
CFG $P:\mathcal{F} \rightarrow \mathcal{C}$과 covering family $\{f_i: U_i \rightarrow U\}_{i\in I}$이 주어졌다 하자. 이 covering에 대한 *descent datum<sub>하강 자료</sub>*은 다음으로 이루어진다.

1. 각 $i$마다 정의된 대상 $x_i\in \mathcal{F}(U_i)$,
2. 각 쌍 $(i, j)$마다 정의된 $\mathcal{F}(U_{ij})$의 isomorphism $\varphi_{ij}: x_j\vert_{U_{ij}}\xrightarrow{\sim}x_i\vert_{U_{ij}}$,

으로서 $U_{ijk}$ 위에서 *cocycle 조건* $\varphi_{ik}\vert_{U_{ijk}}=\varphi_{ij}\vert_{U_{ijk}}\circ \varphi_{jk}\vert_{U_{ijk}}$을 만족하는 것이다. 
:::

Scheme에서의 descent와 마찬가지로, 만일 어떤 대상 $x\in \mathcal{F}(U)$와 isomorphism $\psi_i: x\vert_{U_i}\rightarrow x_i$들이 존재하여, 각각의 $U_{ij}$ 위에서 $\varphi_{ij}\circ(\psi_j\vert_{U_{ij}})=\psi_i\vert_{U_{ij}}$이 성립하도록 할 수 있다면 이를 *effective* descent라 부른다. 즉 descent datum을 통해 이들을 이어붙였을 때 실제로 존재하는 원소 $x$가 얻어지는 것이다. Faithfully flat descent에서는 module에 대한 descent datum이 항상 effective였지만 ([\[스킴\] §충실평탄하강, ⁋정리 6](/ko/math/scheme_theory/faithfully_flat_descent#thm6)), 일반적인 CFG에서는 effectivity가 별도의 조건이다. 이 두 조건을 합하여 stack을 정의한다.

::: 정의 12
Site $(\mathcal{C}, \tau)$ 위의 CFG $P:\mathcal{F} \rightarrow \mathcal{C}$에 대하여,

1. $\mathcal{F}$이 *prestack<sub>준스택</sub>*이라는 것은, 임의의 $U$과 $x, y\in \mathcal{F}(U)$에 대하여 presheaf $\rIsom_U(x, y)$이 $\mathcal{C}_{/U}$ 위의 sheaf인 것이다. ([§그로텐디크 위상, ⁋정의 9](/ko/math/stacks/grothendieck_topology#def9))
2. $\mathcal{F}$이 *stack<sub>스택</sub>*이라는 것은, $\mathcal{F}$이 prestack이고 동시에 임의의 covering family에 대한 모든 descent datum이 effective인 것이다.
:::

이미 설명한 것과 같이, prestack 조건은 morphism들이 서로 붙는다는 것을 의미하며, stack 조건은 여기에 더해 대상을 붙여 effective descent를 더한 것으로 생각할 수 있다. Discrete fiber, 곧 집합 값 functor의 경우 stack 조건은 익숙한 sheaf 조건으로 정확히 환원된다. 이것이 stack을 sheaf의 일반화로 보는 관점을 정당화한다.

::: 명제 13
CFG $P:\mathcal{F} \rightarrow \mathcal{C}$의 모든 fiber $\mathcal{F}(U)$이 discrete groupoid라 하자. 그럼 $\mathcal{F}$은 어떤 presheaf $F:\mathcal{C}^\op \rightarrow \Set$에 대응하며, 이 때 $\mathcal{F}$이 prestack인 것은 $F$이 separated presheaf인 것과, $\mathcal{F}$이 stack인 것은 $F$이 sheaf인 것과 동치이다.
:::
::: 증명
Fiber가 discrete이므로 [정리 8](#thm8)의 pseudofunctor는 strict functor $F:\mathcal{C}^\op \rightarrow \Set$ ($\Set$을 discrete groupoid의 category로 본 것)이다. 두 대상 $x, y\in \mathcal{F}(U)=F(U)$에 대하여 $\Hom_{\mathcal{F}(V)}(x\vert_V, y\vert_V)$은 $x\vert_V=y\vert_V$이면 한원소 집합, 아니면 공집합이다. 따라서 $\rIsom_U(x, y)$이 sheaf라는 것은, $x, y$이 한 covering의 각 $U_i$ 위에서 일치하면 (그리고 겹침 조건이 공허하게 성립하면) $U$ 위에서 일치한다는 것, 즉 $F$의 amalgamation의 유일성이다. ([§그로텐디크 위상, ⁋정의 9](/ko/math/stacks/grothendieck_topology#def9))

다음으로 effective descent를 본다. Discrete fiber에서 isomorphism $\varphi_{ij}$은 모두 항등사상일 수밖에 없으므로, descent datum은 단지 $x_i\vert_{U_{ij}}=x_j\vert_{U_{ij}}$을 만족하는 족 $(x_i)$, 곧 $F$의 matching family이다. 그 effectivity는 amalgamation $x\in F(U)$의 존재성과 같다. 따라서 모든 descent datum이 effective인 것은 $F$의 모든 matching family가 amalgamation을 가지는 것이고, prestack 조건과 합하면 정확히 sheaf 조건이다. ([§그로텐디크 위상, ⁋명제 10](/ko/math/stacks/grothendieck_topology#prop10))
:::

그럼 우리 흐름에서 중요한 다음의 따름정리를 얻는다. 

::: 따름정리 14
Site $(\mathcal{C}, \tau)$가 subcanonical이라 하자. 그럼 임의의 대상 $X\in\mathcal{C}$에 대하여 functor of points $h_X$은 sheaf이고, 이에 대응하는 representable CFG $\mathcal{C}_{/X}$은 stack이다.
:::
::: 증명
Subcanonical이라는 것은 모든 representable presheaf $h_X$이 sheaf라는 뜻이다. 따라서 [예시 9](#ex9)의 $\mathcal{C}_{/X}$에 [명제 13](#prop13)을 적용하면 된다.
:::

[§그로텐디크 위상, ⁋정리 14](/ko/math/stacks/grothendieck_topology#thm14)에 의해, 위 따름정리는 특히 fpqc site에 적용된다. 즉 임의의 scheme에서 만들어진 functor of points는 sheaf이며, 이에 대응하는 CFG는 stack이 된다. 더 일반적으로, [명제 13](#prop13)에 의하여 set-valued presheaf $F$가 sheaf이면 각 $F(U)$를 discrete groupoid로 보아 stack을 얻는다. 즉 automorphism이 없는 moduli problem에서는 우리가 지금까지 살펴본 결과들이 거의 공짜로 적용된다. 

## 스택의 예시

이제 구체적인 stack을 구성한다. 가장 기본적인 예는 [예시 9](#ex9)의 quasi-coherent sheaf CFG이며, 그것이 stack이라는 사실은 faithfully flat descent를 그대로 옮긴 것이다.

::: 정리 15
Base site를 $\Sch$ (또는 $\Sch_{/S}$) 위의 fpqc site로 둔다. ([\[스킴\] §충실평탄하강, ⁋정의 9](/ko/math/scheme_theory/faithfully_flat_descent#def9)) 그럼 [예시 9](#ex9)의 quasi-coherent sheaf CFG $\mathcal{QCoh}$은 stack이다.
:::
::: 증명
Prestack 조건과 effectivity를 차례로 faithfully flat descent로 환원한다. 두 조건 모두 fpqc covering에 대한 것이고, quasi-compact 조건으로 finite subcover을 모아 disjoint union을 취하면 단일 affine faithfully flat morphism $\Spec B \rightarrow \Spec A$인 경우로 환원된다.

우선 prestack 조건을 보이자. $T=\Spec A$ 위의 두 quasi-coherent sheaf $\mathcal{F}, \mathcal{G}$, 즉 두 $A$-module $M, N$에 대하여, presheaf $\rIsom_T(\mathcal{F}, \mathcal{G})$이 sheaf임을 보여야 한다. 이를 위해서는 homomorphism presheaf 

$$(\Spec A' \rightarrow \Spec A)\mapsto \Hom_{A'}(M\otimes_A A', N\otimes_A A')$$

이 sheaf임을 보이면 충분하다. Isomorphism은 양방향 homomorphism이 합성하여 항등이 되는 조건으로 잘라낸 subsheaf이기 때문이다. 그런데 faithfully flat descent functor $\rMod{A} \rightarrow \Desc(B/A)$이 categorical equivalence이므로 ([\[스킴\] §충실평탄하강, ⁋정리 6](/ko/math/scheme_theory/faithfully_flat_descent#thm6)), 특히 fully faithful이다. ([\[범주론\] §함자, ⁋정의 10](/ko/math/category_theory/functors#def10)) Full faithfulness가 정확히 homomorphism이 covering $\{\Spec B \rightarrow \Spec A\}$ 위에서 유일하게 내려온다는 것, 즉 $\Hom$ presheaf의 sheaf 조건을 준다.

Effectivity를 보자. Covering family $\{T_i \rightarrow T\}$ 위의 descent datum은 각 $T_i$ 위의 quasi-coherent sheaf $\mathcal{F}_i$과 $T_{ij}$ 위의 cocycle isomorphism $\varphi_{ij}$의 자료이다. 이는 정확히 quasi-coherent sheaf의 descent datum이며, quasi-coherent sheaf가 fpqc 위상에 대하여 effective descent를 가지므로 ([\[스킴\] §충실평탄하강, ⁋정리 11](/ko/math/scheme_theory/faithfully_flat_descent#thm11)) $T$ 위의 quasi-coherent sheaf $\mathcal{F}$과 isomorphism $\mathcal{F}\vert_{T_i}\cong \mathcal{F}_i$으로 유일하게 붙는다. 따라서 모든 descent datum이 effective이고, prestack 조건과 합하여 $\mathcal{QCoh}$은 stack이다.
:::

[정리 15](#thm15)는 우리가 위에서 살펴본 원칙을 다시 한 번 명시적으로 보여준다. 즉 prestack 조건은 [\[스킴\] §충실평탄하강, ⁋정리 6](/ko/math/scheme_theory/faithfully_flat_descent#thm6)의 full faithfulness로, effectivity는 [\[스킴\] §충실평탄하강, ⁋정리 11](/ko/math/scheme_theory/faithfully_flat_descent#thm11)의 effective descent로 각각 환원된다. 

한편, 모든 CFG가 stack인 것은 아니므로, prestack을 stack으로 보편적으로 보완하는 조작이 필요하다. 이것이 [§그로텐디크 위상, ⁋정리 12](/ko/math/stacks/grothendieck_topology#thm12)의 sheafification의 stack 판본인 stackification이다.

::: 정리 16 (Stackification)
Site $(\mathcal{C}, \tau)$ 위의 임의의 CFG $\mathcal{F}$에 대하여, stack $\mathcal{F}^a$과 morphism $\iota:\mathcal{F} \rightarrow \mathcal{F}^a$이 존재하여 다음 보편성을 가진다. 임의의 stack $\mathcal{G}$에 대하여 $\iota$와의 합성

$$\Hom(\mathcal{F}^a, \mathcal{G})\xrightarrow{\ \sim\ }\Hom(\mathcal{F}, \mathcal{G})$$

이 category의 equivalence이다. 즉 stack의 2-category는 CFG의 2-category에 reflective하게 들어가며, $\iota$이 그 unit이다.
:::

이 또한 그 원본인 [§그로텐디크 위상, ⁋정리 12](/ko/math/stacks/grothendieck_topology#thm12)와 마찬가지로 증명이 꽤나 길어서 생략하기로 한다. 어쨌든 이는 sheafification adjunction의 2-category 버전이며, sheafification이 presheaf를 sheaf로 보내는 left adjoint였듯 stackification은 CFG를 stack으로 보내는 2-categorical reflection이라는 것이 핵심 내용이다. 이 조작 덕분에 우리는 moduli problem을 우선 CFG로 자유롭게 적은 뒤, 필요하면 stackify하여 descent가 성립하는 대상으로 바꿀 수 있다.

한편 우리는 도입부의 예시를 마무리할 때가 되었다. 

::: 정의 17
Site $(\mathcal{C}, \tau)$ 위의 sheaf of groups $G$와 object $T\in \mathcal{C}$가 주어졌다고 하자. $T$ 위의 *$G$-torsor* (또는 *principal $G$-bundle*)란, $\mathcal{C}_{/T}$ 위의 sheaf $P$와 left action $G\vert_T\times P \rightarrow P$으로서, 어떤 covering $\{T_i \rightarrow T\}$ 위에서 $G\vert_{T_i}$-equivariant isomorphism

$$P\vert_{T_i}\cong G\vert_{T_i}$$

을 갖는 것이다. 여기서 오른쪽에는 $G\vert_{T_i}$의 left translation action을 준다. 두 $G$-torsor 사이의 morphism은 $G$-equivariant sheaf morphism이며, $T$ 위의 $G$-torsor들은 groupoid $\bB G(T)$을 이룬다. 대응 $T\mapsto \bB G(T)$이 정의하는 CFG를 *classifying stack<sub>분류 스택</sub>* $\bB G$로 적는다.
:::

Local trivialization $P\vert_{T_i}\cong G\vert_{T_i}$들의 비교는 $T_{ij}$ 위의 $G$-값 transition 자료 $g_{ij}\in G(T_{ij})$을 낳고, 이것이 cocycle을 이룬다. Trivial torsor $G\vert_T$는 $\bB G(T)$의 object이며, 그 automorphism group은 $\Aut_{\bB G(T)}(G\vert_T)\cong G(T)$이다. 즉 $\bB G$은 trivial torsor 위에서도 group $G$을 automorphism으로 기억하며, $\bB G(T)$의 isomorphism class들은 $H^1(T, G)$으로 분류된다. 가장 중요한 경우가 $G=\mathbb{G}_m$이며, 이것이 [예시 2](#ex2)에서 예고한 line bundle의 분류이다.

::: 정리 18
$\Sch$ (또는 $\Sch_{/S}$) 위의 fpqc site에서, $\mathbb{G}_m$-torsor의 classifying stack $\bB\mathbb{G}_m$은 $T$ 위의 line bundle들의 groupoid $\mathcal{L}(T)$을 fiber로 하는 CFG와 동치이며, 이 CFG는 stack이다.
:::
::: 증명
먼저 $\mathbb{G}_m$-torsor와 line bundle의 동치는 [\[스킴\] §군 스킴, ⁋예시 15](/ko/math/scheme_theory/group_schemes#ex15)에서 보았다. 이 때 frame torsor construction 아래 line bundle 사이의 isomorphism과 frame torsor 사이의 $\mathbb{G}_m$-equivariant isomorphism이 서로 대응하며, 이 대응은 base change와 호환된다. 따라서 각 $T$에서 groupoid $\bB\mathbb{G}_m(T)$과 $\mathcal{L}(T)$이 동치이고, 두 CFG도 동치이다.

이제 line bundle CFG $\mathcal{L}$이 stack임을 보인다. 이는 invertible sheaf만을 대상으로 하는 $\mathcal{QCoh}$의 full sub-CFG이다. 따라서 두 line bundle $\mathcal{E}, \mathcal{F}\in\mathcal{L}(T)$ 사이의 Isom presheaf는 $\mathcal{QCoh}$에서 계산한 $\rIsom_T(\mathcal{E}, \mathcal{F})$와 같다. [정리 15](#thm15)에 의해 이 presheaf가 sheaf이므로 $\mathcal{L}$은 prestack이다.

다음으로 object descent를 확인한다. Covering family $\{T_i \rightarrow T\}$ 위의 line bundle $\mathcal{L}_i$들과 overlap 위의 isomorphism $\varphi_{ij}$들이 descent datum을 이룬다고 하자. [정리 15](#thm15)에 의해 이 datum을 실현하는 quasi-coherent sheaf $\mathcal{F}$와 isomorphism $\mathcal{F}\vert_{T_i}\cong \mathcal{L}_i$들이 존재한다. [\[스킴\] §충실평탄하강, ⁋명제 7](/ko/math/scheme_theory/faithfully_flat_descent#prop7)에 의해 locally free of rank $1$인 성질은 fpqc covering을 따라 내려오므로 $\mathcal{F}$도 invertible하다. 따라서 모든 descent datum이 $\mathcal{L}(T)$ 안에서 effective이고, $\mathcal{L}\cong \bB\mathbb{G}_m$은 stack이다.
:::

---

**참고문헌**

**[FGA]** B. Fantechi, L. Göttsche, L. Illusie, S. Kleiman, N. Nitsure, A. Vistoli, *Fundamental algebraic geometry: Grothendieck's FGA explained*. Mathematical Surveys and Monographs, American Mathematical Society, 2005.  
**[Stacks]** The Stacks Project Authors, *The Stacks Project*. Available [online](https://stacks.math.columbia.edu/).
