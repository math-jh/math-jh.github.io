---
title: "Fibered category와 stack"
description: "Moduli 문제가 집합이 아니라 groupoid를 값으로 가짐을 동기로, base 위의 fibered category와 groupoid에 의한 fibration을 정의하고, site 위에서 descent가 성립하는 stack의 개념을 faithfully flat descent의 일반화로 도입한다."
excerpt: "Groupoids, categories fibered in groupoids, descent, and the definition of a stack"

categories: [Math / Stacks]
permalink: /ko/math/stacks/fibered_categories_and_stacks
sidebar: 
    nav: "stacks-ko"

date: 2026-08-30
weight: 2

published: false

---

우리가 다룰 stack은 본질적으로 moduli problem에서 온 것으로, 이러한 문제의 대표적인 예시는 [\[대수적 위상수학\] §분류공간, ⁋정리 8](/ko/math/algebraic_topology/classifying_spaces#thm8)에서 살펴본, 위상공간 $X$ 위의 principal $G$-bundle, 혹은 rank $r$의 vector bundle 등을 분류하는 문제이다. 우리가 [\[스킴\] §점함자](/ko/math/scheme_theory/functor_of_points)에서 도입한 functor of points의 관점으로 얻는 가장 좋은 사실은 이 문제의 대수기하학적 형태에서 이러한 종류의 대응

$$T\mapsto F(T): \Sch^\op\rightarrow \Set;\qquad T\mapsto \{\text{principal $G$-bundles over $T$}\}$$

을 functor 그 자체로 생각한 후, 이 functor가 실제로 scheme에 의해 represent되는지를 살펴볼 수 있다는 것이다. 그러나 이 식 자체는 잘 정의된 functor가 아닌데, 핵심적인 이유는 이 사상의 functoriality를 보이기 위해서는 사상 $f:Y\rightarrow X$에 대한 bundle의 pullback $f^\ast P$를 이용하여 $X$ 위의 bundle을 $Y$ 위로 옮겨와야 하지만, pullback bundle 자체가 태생부터 unique isomorphism에 대해서만 유일하게 결정되기 때문이다.

위상수학에서 이를 해결하는 방식은 간단했다. 위와 같은 naive한 대응 대신, $\hTop$에서 모든 것을 해결한다. 즉 다음의 대응

$$X\mapsto \{\text{principal $G$-bundles over $X$}\}/{\cong}$$

을 생각하면 된다. 그럼 이 이론의 중요한 결과는 $G$의 classifying space $\B G$ 위에 universal bundle $\E G\rightarrow\B G$가 존재하며, 이를 pullback하는 대응이 전단사

$$[X,\B G]\xrightarrow{\sim}\{\text{principal $G$-bundles over $X$}\}/{\cong};\qquad [f]\mapsto[f^\ast\E G]$$

를 준다는 것이었다. 이를 작동하게 하는 것이 $\E G$가 contractible이라는 조건으로, 두 classifying map의 pullback이 isomorphic하면 그 bundle에서 $\E G$로 가는 두 $G$-equivariant map이 homotopic하고, 따라서 두 classifying map도 homotopic하다. 즉 이 분류정리는 bundle isomorphism과 사상 사이의 homotopy를 각각 동치관계로 죽인 뒤 얻은 두 집합이 같다는 명제이다.

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
2. 또 다른 친숙한 예시는 위상공간 $X$의 *fundamental groupoid* $\Pi_1(X)$이다. ([\[대수적 위상수학\] §호모토피, ⁋정의 11](/ko/math/algebraic_topology/homotopy#def11)) 이는 점을 대상으로, 경로의 homotopy class를 morphism으로 하는 category이며, 이 때 한 점에서의 automorphism group이 정확히 fundamental group $\pi_1(X,x)$가 된다.
3. 우리의 이야기 흐럼에서 자명한 예시로, 임의의 functor $F:\mathcal{C}^\op \rightarrow \Set$은 각 $T$에 discrete groupoid $F(T)$을 주는 특수한 경우이다. 즉, $\Set$-valued functor는 $\Grpd$-valued functor의 특수한 예시이다.
:::

특히 첫째 예시가 우리가 주로 살펴볼 대상이다. 일반적으로 $\Pic(T)$에서는 nontrivial line bundle $\mathcal{L}$이 있을 수 있지만, line bundle의 정의에 의하여 $\mathcal{L}$도 <em-ko>국소적으로는</em-ko> trivial line bundle과 isomorphic했다. [\[스킴\] §충실평탄하강, ⁋정리 11](/ko/math/scheme_theory/faithfully_flat_descent#thm11)에서 우리는 이러한 isomorphism까지도 함께 기록하여 nontrivial line bundle을 얻어냈어야 했으며, 이 단계에서부터 이미 isomorphism을 잊지 않고 기록하는 것이 중요했다. 

## 유사함자

Base category 위에서 변하는 groupoid를 적는 가장 직접적인 방법은 각 대상에 groupoid를, 각 morphism에 pullback functor를 대응시키는 것이다. 그러나 scheme의 pullback이 그렇듯, 두 morphism의 합성에 대한 pullback은 각 pullback의 합성과 *같지* 않고 단지 자연스럽게 *동형*일 뿐이다. 가령 $(g\circ f)^\ast \mathcal{L}$과 $f^\ast g^\ast \mathcal{L}$은 표준적인 동형을 가지지만 동일한 sheaf는 아니다. 이 동형들을 자료의 일부로 명시하고 그들이 정합적임을 요구하는 것이 pseudofunctor이다.

::: 정의 3
Category $\mathcal{C}$ 위의 *pseudofunctor<sub>유사함자</sub>* $F:\mathcal{C}^\op \rightarrow \Grpd$는 다음 자료로 이루어진다.

1. 각 대상 $U\in \mathcal{C}$에 groupoid $F(U)$,
2. 각 morphism $f: U \rightarrow V$에 functor $f^\ast: F(V) \rightarrow F(U)$,
3. 각 합성가능한 쌍 $U\xrightarrow{f}V\xrightarrow{g}W$에 natural isomorphism $\varepsilon_{f, g}: f^\ast\circ g^\ast \xRightarrow{\sim}(g\circ f)^\ast$, 그리고 각 대상 $U$에 natural isomorphism $\eta_U:\id_{F(U)}\xRightarrow{\sim}(\id_U)^\ast$.

이 자료는 다음 정합성 조건을 만족해야 한다. 세 morphism $U\xrightarrow{f}V\xrightarrow{g}W\xrightarrow{h}Z$에 대하여

$$\varepsilon_{f, h\circ g}\circ(\id_{f^\ast}\ast \varepsilon_{g, h})=\varepsilon_{g\circ f, h}\circ(\varepsilon_{f, g}\ast \id_{h^\ast})$$

이 성립하고 (결합 정합성), $\varepsilon_{\id, g}$와 $\varepsilon_{f, \id}$이 각각 $\eta$로 표현되는 unit 정합성이 성립한다.
:::

여기에서 $\ast$은 natural transformation의 *수평 합성*이다. Functor $F, G:\mathcal{D} \rightarrow \mathcal{E}$과 $F', G':\mathcal{C} \rightarrow \mathcal{D}$, 그리고 natural transformation $\beta: F\Rightarrow G$, $\alpha: F'\Rightarrow G'$에 대하여 수평 합성 $\beta\ast \alpha: F\circ F'\Rightarrow G\circ G'$은 각 성분 $(\beta\ast \alpha)_C=G\alpha_C\circ \beta_{F'C}=\beta_{G'C}\circ F\alpha_C$ ($\beta$의 naturality로 두 합성이 일치한다)으로 정의되며, 한쪽이 항등 natural transformation이면 functor에 의한 whiskering으로 환원된다. 결합 정합성은 네 단계 합성의 두 가지 괄호 묶기에서 얻는 동형이 일치함을 요구하는 것으로, 위상수학의 homotopy 정합성과 같은 종류의 조건이다. 만일 모든 $\varepsilon_{f, g}$와 $\eta_U$이 항등사상이면 $F$는 통상적인 functor $\mathcal{C}^\op \rightarrow \Grpd$이 되며, 이 경우를 *strict* functor라 부른다.

Strictification에 의해 모든 pseudofunctor를 strict functor와 naturally equivalent한 대상으로 바꿀 수 있지만, 기하학적 pullback은 합성과 equality가 아니라 canonical isomorphism으로 호환되므로 여기에서는 자연스럽게 주어지는 pseudo 구조를 유지한다.

## 준군값 올범주

Pseudofunctor가 정합성 자료를 명시하는 데 비해, fibered category는 그것을 보편성 안에 숨긴다. 발상은 다음과 같다. 각 $U$ 위의 groupoid $F(U)$을 따로 두는 대신, 모든 $F(U)$의 대상을 한 category $\mathcal{F}$에 모으고, 각 대상이 어느 $U$ 위에 놓이는지를 functor $p:\mathcal{F} \rightarrow \mathcal{C}$로 기록한다. Pullback $f^\ast$은 $\mathcal{F}$ 안의 특별한 morphism, 곧 cartesian morphism으로 나타난다.

::: 정의 4
Functor $p:\mathcal{F} \rightarrow \mathcal{C}$가 주어졌다 하자. $\mathcal{F}$의 morphism $\varphi:\xi \rightarrow \eta$이 $f=p(\varphi): U \rightarrow V$ *위에 놓인다*고 하고, $\varphi$가 *cartesian<sub>데카르트</sub> 사상*이라는 것은 다음 보편성을 만족하는 것이다. $\mathcal{F}$의 임의의 대상 $\zeta$와 morphism $\psi:\zeta \rightarrow \eta$, 그리고 $p(\zeta)\xrightarrow{h}U$로서 $f\circ h=p(\psi)$인 임의의 $h$에 대하여, $p(\chi)=h$이고 $\varphi\circ \chi=\psi$인 morphism $\chi:\zeta \rightarrow \xi$이 유일하게 존재한다.
:::

{% diagram Math/Stacks/Fibered_Categories_and_Stacks-1.svg width="7.32em" alt="cartesian morphism의 보편성" %}

Cartesian morphism은 $\eta$의 $f$를 따른 "가장 효율적인 pullback"이다. 보편성은 $\eta$를 향한 모든 morphism이 $\varphi$를 유일하게 거쳐 인수분해됨을 말하므로, 그러한 $\xi$이 존재한다면 표준 동형을 제외하고 유일하다. 이 $\xi$을 $f^\ast \eta$로 적고 $\eta$의 $f$를 따른 *pullback*이라 부른다. 이제 모든 morphism이 이런 pullback으로 분해되고 각 fiber가 groupoid가 되도록 요구한다.

::: 정의 5
Functor $p:\mathcal{F} \rightarrow \mathcal{C}$가 *category fibered in groupoids* (이하 *CFG*)라는 것은 다음 두 조건을 만족하는 것이다.

1. (Lift 존재) 임의의 morphism $f: U \rightarrow V$와 $V$ 위의 대상 $\eta$에 대하여, $f$ 위에 놓이며 공역이 $\eta$인 cartesian morphism $\varphi:\xi \rightarrow \eta$이 존재한다.
2. (모든 morphism이 cartesian) $\mathcal{F}$의 모든 morphism이 cartesian이다.
:::

이 정의는 다음의 보다 검사하기 쉬운 형태와 동치이다. $p:\mathcal{F} \rightarrow \mathcal{C}$이 CFG인 것은 (1) 위의 lift 존재 조건과, (2$'$) 임의의 두 morphism $\varphi:\xi \rightarrow \eta$, $\psi:\zeta \rightarrow \eta$과 $p(\zeta)\xrightarrow{h}p(\xi)$로서 $p(\varphi)\circ h=p(\psi)$인 것에 대하여 $p(\theta)=h$이고 $\varphi\circ \theta=\psi$인 $\theta:\zeta \rightarrow \xi$이 유일하게 존재하는 조건을 함께 만족하는 것이다. 조건 (2$'$)이 정확히 "모든 morphism이 cartesian"의 풀어쓴 형태이다. 한 대상 $U\in \mathcal{C}$에 대하여, $U$ 위에 놓인 대상들과 $\id_U$ 위에 놓인 morphism들로 이루어진 $\mathcal{F}$의 subcategory를 $U$ 위의 *fiber<sub>올</sub>* $\mathcal{F}(U)$ ($\mathcal{F}_U$로도 적는다)라 부른다.

각 morphism $f:U\rightarrow V$와 대상 $\eta\in\mathcal{F}(V)$에 대하여 cartesian lift $f^\ast\eta\rightarrow\eta$을 하나씩 고르는 것을 *cleavage*라 부른다. Cleavage는 보편성에 의해 isomorphism까지 유일한 pullback들 가운데 실제 대표를 일관되게 골라 pullback functor를 정의하기 위한 선택이다.

::: 명제 6
$p:\mathcal{F} \rightarrow \mathcal{C}$이 CFG라 하자. 그럼 다음이 성립한다.

1. 각 fiber $\mathcal{F}(U)$은 groupoid이다.
2. Cleavage를 하나 고르면 각 morphism $f:U\rightarrow V$에 대하여 functor $f^\ast:\mathcal{F}(V) \rightarrow \mathcal{F}(U)$이 정의되며, 다른 선택은 이 functor를 표준 natural isomorphism을 제외하고 바꾸지 않는다. 나아가 합성가능한 $U\xrightarrow{f}V\xrightarrow{g}W$에 대하여 표준 natural isomorphism $f^\ast\circ g^\ast\cong(g\circ f)^\ast$이 있다.
:::
::: 증명
(1) $\alpha:\xi \rightarrow \eta$이 $\id_U$ 위에 놓인 morphism이라 하자. 조건 (2$'$)을 $\varphi=\alpha$, $\psi=\id_\eta$, $h=\id_U$에 적용하면 $\alpha\circ \theta=\id_\eta$이고 $p(\theta)=\id_U$인 $\theta:\eta \rightarrow \xi$이 유일하게 있어, $\alpha$의 오른쪽 역사상을 얻는다. 같은 보편성을 $\theta$에 적용하면 $\theta\circ \theta'=\id_\xi$이고 $p(\theta')=\id_U$인 $\theta':\xi \rightarrow \eta$을 얻는데, $\alpha\circ \theta=\id_\eta$으로부터 $\alpha=(\alpha\circ \theta)\circ \theta'=\theta'$이므로 $\theta\circ \alpha=\theta\circ \theta'=\id_\xi$이다. 따라서 $\alpha$는 $\theta$을 역사상으로 가지는 isomorphism이다. 따라서 $\mathcal{F}(U)$의 모든 morphism이 가역, 즉 $\mathcal{F}(U)$은 groupoid이다.

(2) $\eta\in \mathcal{F}(V)$마다 cartesian lift $f^\ast \eta\xrightarrow{\varphi_\eta}\eta$을 고른다. $\mathcal{F}(V)$의 morphism $\beta:\eta \rightarrow \eta'$에 대하여, $\beta\circ \varphi_\eta:f^\ast \eta \rightarrow \eta'$과 cartesian morphism $\varphi_{\eta'}:f^\ast \eta' \rightarrow \eta'$ 및 $h=\id_U$에 (2$'$)을 적용하면 $\varphi_{\eta'}\circ \theta=\beta\circ \varphi_\eta$인 $\theta:f^\ast \eta \rightarrow f^\ast \eta'$이 유일하게 정해진다. 이를 $f^\ast \beta$로 두면 유일성으로부터 $f^\ast(\beta'\circ \beta)=f^\ast \beta'\circ f^\ast \beta$과 $f^\ast \id=\id$이 따르므로 $f^\ast$은 functor이다. 다른 cleavage $\widetilde{f^\ast \eta}\xrightarrow{\widetilde{\varphi}_\eta}\eta$을 골랐다면, 두 cartesian morphism의 보편성으로 $\widetilde{f^\ast \eta}\cong f^\ast \eta$인 표준 동형이 $\eta$에 대하여 자연스럽게 존재한다. 끝으로 $f^\ast g^\ast \eta \rightarrow g^\ast \eta \rightarrow \eta$의 합성은 $g\circ f$ 위에 놓인 cartesian morphism이고 (cartesian morphism의 합성이 cartesian임은 보편성을 두 번 적용하여 곧 확인된다), $(g\circ f)^\ast \eta \rightarrow \eta$ 또한 그러하므로, 보편성에 의해 표준 동형 $f^\ast g^\ast \eta\cong(g\circ f)^\ast \eta$을 얻는다.
:::

[명제 6](#prop6)은 CFG가 정확히 [정의 3](#def3)의 pseudofunctor 자료를 보편성으로 재생함을 보여준다. Cleavage를 고르면 fiber $U\mapsto \mathcal{F}(U)$과 pullback $f^\ast$, 그리고 합성 동형 $\varepsilon_{f, g}: f^\ast g^\ast\cong(g\circ f)^\ast$이 모두 나오며, 이들이 [정의 3](#def3)의 정합성 조건을 만족함은 cartesian morphism의 유일성으로부터 자동으로 따라온다. 역으로 pseudofunctor가 주어지면 그 대상들을 모아 CFG를 만들 수 있다. 이 양방향 대응을 정밀하게 진술하기 위해 먼저 CFG 사이의 morphism을 정의한다.

::: 정의 7
두 CFG $p:\mathcal{F} \rightarrow \mathcal{C}$과 $q:\mathcal{G} \rightarrow \mathcal{C}$ 사이의 *morphism*은 $q\circ G=p$을 만족하는 functor $G:\mathcal{F} \rightarrow \mathcal{G}$이다 (이러한 functor는 자동으로 cartesian morphism을 cartesian morphism으로 보낸다). 두 morphism $G, G':\mathcal{F} \rightarrow \mathcal{G}$ 사이의 *2-morphism*은 natural transformation $\alpha: G\Rightarrow G'$으로서 각 성분 $\alpha_\xi$이 $\id_{p(\xi)}$ 위에 놓이는 것이다. 이로써 CFG들은 $\mathcal{C}$ 위에서 2-category를 이룬다.
:::

2-morphism의 각 성분이 $\id$ 위에 놓인다는 조건은, 그것이 어떤 fiber $\mathcal{G}(U)$ 안의 morphism임을 뜻한다. [명제 6](#prop6)에 의해 fiber가 groupoid이므로 이 natural transformation은 자동으로 natural isomorphism이다. 따라서 CFG 사이의 2-morphism은 항상 가역이며, 두 morphism $G, G'$ 사이에 2-morphism이 있으면 둘은 본질적으로 같다. 이 2-category 구조 위에서 pseudofunctor와의 동치가 진술된다.

::: 정리 8 (Grothendieck construction)
Category $\mathcal{C}$ 위의 CFG들이 이루는 2-category와 pseudofunctor $\mathcal{C}^\op \rightarrow \Grpd$들이 이루는 2-category는 2-equivalent하다. 구체적으로 pseudofunctor $F$로부터 다음 *Grothendieck construction* $\int_\mathcal{C}F$을 얻는다. 그 대상은 쌍 $(U, x)$ ($U\in \mathcal{C}$, $x\in F(U)$)이고, $(U, x)$에서 $(V, y)$로의 morphism은 쌍 $(f, \alpha)$ ($f: U \rightarrow V$, $\alpha: x\xrightarrow{\sim}f^\ast y$ in $F(U)$)이며, 사영 $(U, x)\mapsto U$이 이를 CFG로 만든다.
:::
::: 증명
전개가 길어 두 방향의 구성과 그것이 서로 역임의 골자만 제시한다. 자세한 논증은 [Vis] 또는 [Stacks]를 참조하라.

CFG에서 pseudofunctor로 가는 방향은 [명제 6](#prop6)이다. Cleavage를 고르면 $U\mapsto \mathcal{F}(U)$, $f\mapsto f^\ast$, $\varepsilon_{f, g}$이 정해지고 정합성이 보편성으로 따라온다.

역방향이 위 진술의 $\int_\mathcal{C}F$이다. $(f, \alpha):(U, x) \rightarrow (V, y)$과 $(g, \beta):(V, y) \rightarrow (W, z)$의 합성은 $(g\circ f, \gamma)$로 정의하되, $\gamma$은 $x\xrightarrow{\alpha}f^\ast y\xrightarrow{f^\ast \beta}f^\ast g^\ast z\xrightarrow{\varepsilon_{f, g}}(g\circ f)^\ast z$의 합성이다. $\varepsilon$의 정합성이 이 합성의 결합법칙을 보장한다. 사영 $\int_\mathcal{C}F \rightarrow \mathcal{C}$, $(U, x)\mapsto U$에 대하여, morphism $(f, \alpha)$이 cartesian인 것은 $\alpha$이 isomorphism인 것과 동치인데 정의상 모든 $\alpha$이 isomorphism이므로 [정의 5](#def5)의 두 조건이 성립한다. Fiber $(\int_\mathcal{C}F)(U)$은 $F(U)$과 동형이다.

두 구성이 서로 2-equivalence의 역임은, CFG $\mathcal{F}$에서 cleavage로 얻은 pseudofunctor의 Grothendieck construction이 $\mathcal{F}$과 표준적으로 동치이고 ($(U, x)\mapsto x$), 그 역도 마찬가지임을 확인하는 것으로 따라온다. 이 동치는 cleavage의 선택에 의존하지 않는다.
:::

[정리 8](#thm8)에 의하여 우리는 "base category 위에서 변하는 groupoid"를 pseudofunctor로도, CFG로도 자유롭게 기술할 수 있다. 이후로는 두 언어를 맥락에 따라 섞어 쓰며, 특히 정의는 CFG로 깔끔하게 하되 구체적 계산은 pseudofunctor의 pullback $f^\ast$과 $x\vert_V$ 같은 표기로 수행한다. 다음 예시들이 이 글의 주요 대상이다.

::: 예시 9
Base category를 $\mathcal{C}=\Sch$ (또는 고정된 base 위의 $\Sch/S$)로 둔다.

1. (Representable CFG) 대상 $X\in \mathcal{C}$에 대하여 slice category $\mathcal{C}/X$을 사영 $(T \rightarrow X)\mapsto T$과 함께 보면 CFG이다. $T$ 위의 fiber는 morphism 집합 $\Hom_\mathcal{C}(T, X)$을 discrete groupoid로 본 것이며, 이는 functor of points $h_X$에 대응하는 CFG이다. ([\[범주론\] §표현가능한 함자, ⁋정리 4](/ko/math/category_theory/representable_functors#thm4))

2. (quasi-coherent sheaf의 CFG) 대상이 쌍 $(T, \mathcal{F})$ ($T\in \Sch$, $\mathcal{F}$은 $T$ 위의 quasi-coherent sheaf)이고, $(T, \mathcal{F})$에서 $(T', \mathcal{F}')$로의 morphism이 쌍 $(f, \alpha)$ ($f: T \rightarrow T'$, $\alpha: \mathcal{F}\xrightarrow{\sim}f^\ast \mathcal{F}'$은 isomorphism)인 category를 $\mathcal{QC}$로 적는다. ([\[스킴\] §준연접층, ⁋정의 8](/ko/math/scheme_theory/quasicoherent_sheaves#def8)) 사영 $(T, \mathcal{F})\mapsto T$에 대하여 $T$ 위의 fiber는 $T$ 위의 quasi-coherent sheaf들의 groupoid $\QCoh(T)$ (isomorphism만 morphism으로 취한 것)이고, pullback functor는 $f^\ast$이다. ([\[스킴\] §준연접층, ⁋명제 15](/ko/math/scheme_theory/quasicoherent_sheaves#prop15))

3. (Moduli CFG) 어떤 기하학적 대상의 "$T$-족"을 대상으로, 족 사이의 동형을 morphism으로 하면 일반적으로 CFG를 얻는다. 가령 smooth 사영곡선의 $T$-족들과 그 동형이 이루는 CFG $\mathcal{M}_g$이 그러하다. 족의 pullback이 base change로 주어지므로 cartesian morphism이 자연히 정의된다.
:::

[예시 9](#ex9)의 첫째 항은 집합 값 functor가 CFG의 특수한 경우, 곧 fiber가 discrete인 경우임을 보여준다. 셋째 항이 stack 이론의 본래 동기인 moduli 문제이며, 둘째 항은 그 가장 기본적이고 다루기 좋은 형태이다. 이들이 단지 CFG에 그치지 않고 site의 covering을 따라 자료가 붙는 좋은 대상, 곧 stack이 되려면 추가 조건이 필요하다. 그 조건을 정식화하는 것이 다음 절이다.

## 하강

지금까지의 정의에는 base category의 위상이 전혀 쓰이지 않았다. CFG는 순수하게 category-theoretic인 자료이다. Stack은 여기에 [§그로텐디크 위상, ⁋정의 6](/ko/math/stacks/grothendieck_topology#def6)의 covering을 따라 morphism과 대상이 국소에서 대역으로 붙는다는 sheaf 조건을 부과한 것이다. 이는 두 단계로 나뉜다. 먼저 morphism이 붙는 조건 (prestack)을, 이어 대상이 붙는 조건 (stack)을 요구한다. Morphism이 붙는다는 것을 정식화하기 위해 두 대상 사이의 isomorphism이 이루는 presheaf를 도입한다.

이하에서 $(\mathcal{C}, \tau)$은 site이고, 위상은 covering family $\{U_i \rightarrow U\}$로 주어지는 pretopology로 기술한다. ([§그로텐디크 위상, ⁋정의 4](/ko/math/stacks/grothendieck_topology#def4)) CFG $p:\mathcal{F} \rightarrow \mathcal{C}$의 cleavage를 하나 고정하여 pullback $f^\ast$과 restriction $x\vert_V=f^\ast x$ (단, $f: V \rightarrow U$)을 사용한다.

::: 정의 10
CFG $p:\mathcal{F} \rightarrow \mathcal{C}$과 대상 $U\in \mathcal{C}$, 그리고 두 대상 $x, y\in \mathcal{F}(U)$이 주어졌다 하자. $U$ 위의 *Isom presheaf<sub>Isom 준층</sub>*

$$\rIsom_U(x, y):(\mathcal{C}/U)^\op \rightarrow \Set;\qquad (f: V \rightarrow U)\mapsto \Hom_{\mathcal{F}(V)}(f^\ast x, f^\ast y)$$

은 slice site $\mathcal{C}/U$ 위의 presheaf이다. Morphism $g: W \rightarrow V$ (단, $V, W$은 $U$ 위에 있다)에 대한 restriction은 pullback functor $g^\ast$과 합성 동형 $g^\ast f^\ast\cong(f\circ g)^\ast$이 유도하는 morphism이다.
:::

각 fiber가 groupoid이므로 ([명제 6](#prop6)) $\rIsom_U(x, y)$의 값은 모두 isomorphism들의 집합이고, $x=y$이면 이는 automorphism의 presheaf $\rAut_U(x)$이다. 직관적으로 이 presheaf는 "$x$와 $y$을 잇는 동형이 $U$ 위에서 어떻게 변하는가"를 기록한다. Morphism이 국소에서 대역으로 붙는다는 것은 정확히 이 presheaf가 sheaf라는 것이다. 다음으로 대상이 붙는 조건을 위해 descent datum을 정의한다. 이는 [\[스킴\] §충실평탄하강, ⁋정의 4](/ko/math/scheme_theory/faithfully_flat_descent#def4)의 descent datum을 임의의 CFG로 옮긴 것이다.

::: 정의 11
CFG $p:\mathcal{F} \rightarrow \mathcal{C}$과 covering family $\{f_i: U_i \rightarrow U\}_{i\in I}$이 주어졌다 하자. $U_{ij}=U_i\times_U U_j$, $U_{ijk}=U_i\times_U U_j\times_U U_k$로 적고, 사영 $\pr: U_{ij} \rightarrow U_i$ 등을 따른 pullback을 $\vert_{U_{ij}}$로 표기한다. ([\[범주론\] §극한, ⁋예시 8](/ko/math/category_theory/limits#ex8)) 이 covering에 대한 *descent datum<sub>하강 자료</sub>*은 다음으로 이루어진다.

1. 각 $i$마다 대상 $x_i\in \mathcal{F}(U_i)$,
2. 각 쌍 $(i, j)$마다 $\mathcal{F}(U_{ij})$의 isomorphism $\varphi_{ij}: x_j\vert_{U_{ij}}\xrightarrow{\sim}x_i\vert_{U_{ij}}$,

으로서 $U_{ijk}$ 위에서 *cocycle 조건* $\varphi_{ik}\vert_{U_{ijk}}=\varphi_{ij}\vert_{U_{ijk}}\circ \varphi_{jk}\vert_{U_{ijk}}$을 만족하는 것이다 (각 $\varphi$을 적절한 사영을 따라 $U_{ijk}$로 pullback한 것으로 이해한다). 이 descent datum이 *effective<sub>실효적</sub>*라는 것은, 대상 $x\in \mathcal{F}(U)$과 isomorphism $\psi_i: x\vert_{U_i}\xrightarrow{\sim}x_i$들이 존재하여 $U_{ij}$ 위에서 $\varphi_{ij}\circ(\psi_j\vert_{U_{ij}})=\psi_i\vert_{U_{ij}}$이 성립하는 것이다.
:::

Cocycle 조건은 세 겹 겹침 $U_{ijk}$ 위에서 세 동형 $\varphi_{ij}, \varphi_{jk}, \varphi_{ik}$이 모순 없이 합성됨을 요구하며, 이는 sheaf를 open covering에서 붙일 때 transition 함수가 만족하던 cocycle 관계의 직접적 일반화이다. Effectivity는 이 국소 자료 $(x_i, \varphi_{ij})$이 실제로 어떤 대역 대상 $x\in \mathcal{F}(U)$의 restriction으로부터 옴을 뜻한다. Faithfully flat descent에서 module에 대한 descent datum이 항상 effective였던 [\[스킴\] §충실평탄하강, ⁋정리 6](/ko/math/scheme_theory/faithfully_flat_descent#thm6)과 달리, 일반적인 CFG에서는 effectivity가 별도의 조건이다. 이 두 조건을 합하여 stack을 정의한다.

::: 정의 12
Site $(\mathcal{C}, \tau)$ 위의 CFG $p:\mathcal{F} \rightarrow \mathcal{C}$에 대하여,

1. $\mathcal{F}$이 *prestack<sub>준스택</sub>*이라는 것은, 임의의 $U$과 $x, y\in \mathcal{F}(U)$에 대하여 presheaf $\rIsom_U(x, y)$이 $\mathcal{C}/U$ 위의 sheaf인 것이다. ([§그로텐디크 위상, ⁋정의 9](/ko/math/stacks/grothendieck_topology#def9))
2. $\mathcal{F}$이 *stack<sub>스택</sub>*이라는 것은, $\mathcal{F}$이 prestack이고 동시에 임의의 covering family에 대한 모든 descent datum이 effective인 것이다.
:::

Prestack 조건은 "morphism이 붙는다"는 것이다. Covering $\{U_i \rightarrow U\}$ 위에서 정합적으로 주어진 isomorphism들 $x\vert_{U_i}\cong y\vert_{U_i}$이 두 겹 겹침에서 일치하면 $U$ 전체의 동형 $x\cong y$으로 유일하게 붙는다는 것이며, 이는 $\rIsom_U(x, y)$의 sheaf 조건에 다름 아니다. ([§그로텐디크 위상, ⁋명제 10](/ko/math/stacks/grothendieck_topology#prop10)) Stack 조건은 여기에 "대상이 붙는다", 곧 effective descent를 더한 것이다. 정의상 stack은 prestack이고, prestack은 다시 CFG이다. Faithfully flat descent 전체가 이 정의 한 줄로 요약된다. Prestack 조건은 morphism의 descent, 곧 faithfully flat morphism을 따른 morphism의 유일성이고, effectivity는 [\[스킴\] §충실평탄하강, ⁋정리 11](/ko/math/scheme_theory/faithfully_flat_descent#thm11)의 effective descent, 즉 대상의 descent이다.

Discrete fiber, 곧 집합 값 functor의 경우 stack 조건은 익숙한 sheaf 조건으로 정확히 환원된다. 이것이 stack을 sheaf의 일반화로 보는 관점을 정당화한다.

::: 명제 13
CFG $p:\mathcal{F} \rightarrow \mathcal{C}$의 모든 fiber $\mathcal{F}(U)$이 discrete groupoid라 하자. 그럼 $\mathcal{F}$은 어떤 presheaf $F:\mathcal{C}^\op \rightarrow \Set$ ([정리 8](#thm8)을 통해 $F(U)=\obj \mathcal{F}(U)$)에 대응하며, 이 때 $\mathcal{F}$이 prestack인 것은 $F$이 separated presheaf인 것과, $\mathcal{F}$이 stack인 것은 $F$이 sheaf인 것과 동치이다.
:::
::: 증명
Fiber가 discrete이므로 [정리 8](#thm8)의 pseudofunctor는 strict functor $F:\mathcal{C}^\op \rightarrow \Set$ ($\Set$을 discrete groupoid의 category로 본 것)이다. 두 대상 $x, y\in \mathcal{F}(U)=F(U)$에 대하여 $\Hom_{\mathcal{F}(V)}(x\vert_V, y\vert_V)$은 $x\vert_V=y\vert_V$이면 한원소 집합, 아니면 공집합이다. 따라서 $\rIsom_U(x, y)$이 sheaf라는 것은, $x, y$이 한 covering의 각 $U_i$ 위에서 일치하면 (그리고 겹침 조건이 공허하게 성립하면) $U$ 위에서 일치한다는 것, 즉 $F$의 amalgamation 유일성 (separatedness)이다. ([§그로텐디크 위상, ⁋정의 9](/ko/math/stacks/grothendieck_topology#def9))

다음으로 effective descent를 본다. Discrete fiber에서 isomorphism $\varphi_{ij}$은 모두 항등사상일 수밖에 없으므로, descent datum은 단지 $x_i\vert_{U_{ij}}=x_j\vert_{U_{ij}}$을 만족하는 족 $(x_i)$, 곧 $F$의 matching family이다. 그 effectivity는 amalgamation $x\in F(U)$의 존재이다. 따라서 모든 descent datum이 effective인 것은 $F$의 모든 matching family가 amalgamation을 가지는 것이고, prestack 조건과 합하면 정확히 sheaf 조건이다. ([§그로텐디크 위상, ⁋명제 10](/ko/math/stacks/grothendieck_topology#prop10))
:::

[명제 13](#prop13)에 의하여 sheaf of sets는 정확히 automorphism이 자명한 stack이다. Scheme $X$의 functor of points $h_X$은 fpqc sheaf이므로 ([§그로텐디크 위상, ⁋정리 14](/ko/math/stacks/grothendieck_topology#thm14)), [예시 9](#ex9)의 representable CFG $\mathcal{C}/X$은 stack이다. 즉 모든 scheme은 fpqc site 위의 stack으로 자리매김하며, stack 이론은 scheme과 sheaf의 세계를 automorphism을 가지는 대상까지 넓힌 것이다. 이 그림에서 [정의 12](#def12)의 prestack 조건은 representability 검증의 첫 단계 (functor가 sheaf인지)에 정확히 대응한다.

## 스택의 예시

이제 구체적인 stack을 구성한다. 가장 기본적인 예는 [예시 9](#ex9)의 quasi-coherent sheaf CFG이며, 그것이 stack이라는 사실은 faithfully flat descent를 그대로 옮긴 것이다.

::: 정리 14
Base site를 $\Sch$ (또는 $\Sch/S$) 위의 fpqc site로 둔다. ([\[스킴\] §충실평탄하강, ⁋정의 9](/ko/math/scheme_theory/faithfully_flat_descent#def9)) 그럼 [예시 9](#ex9)의 quasi-coherent sheaf CFG $\mathcal{QC}$은 stack이다.
:::
::: 증명
Prestack 조건과 effectivity를 차례로 faithfully flat descent로 환원한다. 두 조건 모두 fpqc covering에 대한 것이고, quasi-compact 조건으로 유한 subcovering을 모아 disjoint union을 취하면 ([\[스킴\] §충실평탄하강, ⁋정의 9](/ko/math/scheme_theory/faithfully_flat_descent#def9)) 단일 affine faithfully flat morphism $\Spec B \rightarrow \Spec A$인 경우로 환원된다.

Prestack. $T=\Spec A$ 위의 두 quasi-coherent sheaf $\mathcal{F}, \mathcal{G}$, 곧 두 $A$-module $M, N$에 대하여, presheaf $\rIsom_T(\mathcal{F}, \mathcal{G})$이 sheaf임을 보여야 한다. 이는 그 부분presheaf의 모집합인 homomorphism presheaf $(\Spec A' \rightarrow \Spec A)\mapsto \Hom_{A'}(M\otimes_A A', N\otimes_A A')$이 sheaf임을 보이면 충분하다. Isomorphism은 양방향 homomorphism이 합성하여 항등이 되는 조건으로 잘라낸 부분sheaf이기 때문이다. 그런데 faithfully flat descent functor $\rMod{A} \rightarrow \Desc(B/A)$이 categorical equivalence이므로 ([\[스킴\] §충실평탄하강, ⁋정리 6](/ko/math/scheme_theory/faithfully_flat_descent#thm6)), 특히 fully faithful이다. ([\[범주론\] §함자, ⁋정의 10](/ko/math/category_theory/functors#def10)) Fully faithfulness가 정확히 homomorphism이 covering $\{\Spec B \rightarrow \Spec A\}$ 위에서 유일하게 내려옴, 곧 $\Hom$ presheaf의 sheaf 조건을 준다.

Effectivity. Covering family $\{T_i \rightarrow T\}$ 위의 descent datum은 각 $T_i$ 위의 quasi-coherent sheaf $\mathcal{F}_i$과 $T_{ij}$ 위의 cocycle 동형 $\varphi_{ij}$의 자료이다. 이는 정확히 quasi-coherent sheaf의 descent datum이며, quasi-coherent sheaf가 fpqc 위상에 대하여 effective descent를 가지므로 ([\[스킴\] §충실평탄하강, ⁋정리 11](/ko/math/scheme_theory/faithfully_flat_descent#thm11)) $T$ 위의 quasi-coherent sheaf $\mathcal{F}$과 동형 $\mathcal{F}\vert_{T_i}\cong \mathcal{F}_i$으로 유일하게 붙는다. 따라서 모든 descent datum이 effective이고, prestack 조건과 합하여 $\mathcal{QC}$은 stack이다.
:::

[정리 14](#thm14)은 stack의 정의가 faithfully flat descent의 재포장임을 명시적으로 보여준다. Prestack 조건은 [\[스킴\] §충실평탄하강, ⁋정리 6](/ko/math/scheme_theory/faithfully_flat_descent#thm6)의 fully faithfulness로, effectivity는 essential surjectivity, 곧 [\[스킴\] §충실평탄하강, ⁋정리 11](/ko/math/scheme_theory/faithfully_flat_descent#thm11)의 effective descent로 각각 환원된다. ([\[범주론\] §자연변환, ⁋정리 5](/ko/math/category_theory/natural_transformations#thm5)) 모든 CFG가 stack인 것은 아니므로, prestack을 stack으로 보편적으로 보완하는 조작이 필요하다. 이것이 [§그로텐디크 위상, ⁋정리 12](/ko/math/stacks/grothendieck_topology#thm12)의 sheafification의 stack 판본인 stackification이다.

::: 정리 15 (stackification)
Site $(\mathcal{C}, \tau)$ 위의 임의의 CFG $\mathcal{F}$에 대하여, stack $\mathcal{F}^a$과 morphism $\iota:\mathcal{F} \rightarrow \mathcal{F}^a$이 존재하여 다음 보편성을 가진다. 임의의 stack $\mathcal{G}$에 대하여 $\iota$와의 합성

$$\Hom(\mathcal{F}^a, \mathcal{G})\xrightarrow{\ \sim\ }\Hom(\mathcal{F}, \mathcal{G})$$

이 category의 equivalence이다. 즉 stack의 2-category는 CFG의 2-category에 reflective하게 들어가며, $\iota$이 그 unit이다.
:::
::: 증명
구성은 sheafification의 plus construction을 두 단계로 적용하는 것과 평행하며, 전개가 길어 골자만 적는다. 자세한 논증은 [Stacks] 또는 [Vis]를 참조하라.

먼저 $\mathcal{F}$을 prestack으로 만든다. 각 $\rIsom_U(x, y)$을 [§그로텐디크 위상, ⁋정리 12](/ko/math/stacks/grothendieck_topology#thm12)의 sheafification으로 대체하여 morphism이 붙도록 강제하면 prestack $\mathcal{F}^{\pre}$과 $\mathcal{F} \rightarrow \mathcal{F}^{\pre}$을 얻는다. 다음으로 effective descent를 보충한다. $\mathcal{F}^{\pre}$의 대상은 그대로 두되, 각 covering 위의 descent datum을 새로운 대상으로 형식적으로 추가하여 stack $\mathcal{F}^a$을 만든다. 구체적으로 $\mathcal{F}^a(U)$의 대상은 "$U$의 어떤 covering 위에서 정의된 $\mathcal{F}^{\pre}$의 descent datum"이고, 더 미세한 covering으로 옮겨 같아지는 것들을 동일시한다. Prestack 조건이 이 추가된 대상들 사이의 morphism이 잘 정의되고 cocycle을 통해 정합적임을 보장하며, 그 결과 $\mathcal{F}^a$의 모든 descent datum이 effective가 된다.

보편성은 다음에서 따른다. $\mathcal{G}$이 stack이면 $\mathcal{G}$의 $\rIsom$이 이미 sheaf이므로 $\mathcal{F} \rightarrow \mathcal{G}$은 prestack 단계를 유일하게 (동치를 제외하고) 거치고, $\mathcal{G}$의 effectivity가 추가된 descent datum 대상들을 $\mathcal{G}$의 실제 대상으로 유일하게 보내므로 $\mathcal{F}^a \rightarrow \mathcal{G}$으로 유일하게 확장된다. 이것이 Hom category의 equivalence를 준다.
:::

[정리 15](#thm15)은 [§그로텐디크 위상, ⁋정리 12](/ko/math/stacks/grothendieck_topology#thm12)의 sheafification adjunction의 2-category 판본이다. Sheafification이 presheaf를 sheaf로 보내는 left adjoint였듯, stackification은 CFG를 stack으로 보내는 2-categorical reflection이다. 이 조작 덕분에 우리는 moduli 문제를 우선 CFG로 자유롭게 적은 뒤, 필요하면 stackify하여 descent가 성립하는 대상으로 바꿀 수 있다. 다음 예시가 그 전형이다.

이제 group이 작용하는 대상의 분류 stack을 구성한다. 그 기본 단위가 torsor이다. Site 위의 sheaf of group $G$ (즉 $\Sh(\mathcal{C}; \tau)$의 group object)에 대하여, $G$-torsor는 group bundle의 sheaf적 일반화이다.

::: 정의 16
Site $(\mathcal{C}, \tau)$ 위의 sheaf of group $G$에 대하여, 대상 $T\in \mathcal{C}$ 위의 *$G$-torsor* (또는 *principal $G$-bundle*)란, $\mathcal{C}/T$ 위의 sheaf $P$과 $G\vert_T$의 좌작용 $G\vert_T\times P \rightarrow P$으로서 다음을 만족하는 것이다.

1. (국소 비공) morphism $P \rightarrow \ast$ (종대상으로의 morphism)이 sheaf의 epimorphism이다. 즉 어떤 covering $\{T_i \rightarrow T\}$이 있어 각 $P(T_i)\neq \emptyset$이다.
2. (단순추이성) morphism $G\vert_T\times P \rightarrow P\times P$, $(g, p)\mapsto(g\cdot p, p)$이 sheaf의 isomorphism이다.

두 $G$-torsor 사이의 morphism은 $G$-동변 sheaf morphism이며 (이는 자동으로 isomorphism이다), $T$ 위의 $G$-torsor들은 groupoid $\bB G(T)$을 이룬다. 대응 $T\mapsto \bB G(T)$이 정의하는 CFG를 *classifying stack<sub>분류 스택</sub>* $\bB G$로 적는다.
:::

두 조건은 $P$이 국소적으로 $G$ 자신과 같음, 곧 어떤 covering 위에서 $P\vert_{T_i}\cong G\vert_{T_i}$ ($G$의 left translation action)임과 동치이다. 실제로 조건 1로 각 $T_i$ 위에 절단 $s_i\in P(T_i)$을 잡으면, 조건 2가 $g\mapsto g\cdot s_i$이 동형 $G\vert_{T_i}\xrightarrow{\sim}P\vert_{T_i}$임을 준다. 두 절단의 비교는 $T_{ij}$ 위의 $G$-값 transition 자료 $g_{ij}\in G(T_{ij})$을 낳고, 이것이 cocycle을 이룬다. $\bB G$의 한 점의 automorphism group은 $\Aut(P)\cong G(T)$이므로 ($P$이 자명한 경우), $\bB G$은 자명한 대상 하나에 group $G$이 automorphism으로 붙은 stack, 곧 $\bB G(T)$의 isomorphism class는 $H^1(T, G)$으로 분류된다. 가장 중요한 경우가 $G=\mathbb{G}_m$이며, 이것이 [예시 2](#ex2)에서 예고한 line bundle의 분류이다.

분류 문제를 집합으로 다루려는 순진한 시도가 왜 실패하는지를 $\mathbb{G}_m$에서 명확히 볼 수 있다. Isomorphism class만 기억하는 presheaf $T\mapsto \Pic(T)$은 sheaf가 아니다. 두 line bundle은 한 covering의 각 조각 위에서 동형이어도 ($\Pic(T_i)$에서 같은 류) 대역적으로 동형이 아닐 수 있는데 ($\Pic(T)$에서 다른 류), 이는 국소 동형들 $\psi_i$을 붙이는 데 필요한 transition 자료가 집합 $\Pic$에는 담기지 않기 때문이다. 그 transition 자료가 바로 automorphism $\mathbb{G}_m(T_{ij})$의 원소이며, isomorphism class로 뭉개는 순간 사라진다. 따라서 line bundle은 sheaf로는 분류되지 않고 stack $\bB\mathbb{G}_m$으로 분류된다. 이 stack이 실제로 stack 조건을 만족함을 line bundle의 descent로 확인하는 것이 마지막 정리이다.

::: 정리 17
$\Sch$ (또는 $\Sch/S$) 위의 fpqc site에서, $\mathbb{G}_m$-torsor의 classifying stack $\bB\mathbb{G}_m$은 $T$ 위의 line bundle들의 groupoid $\mathcal{L}(T)$을 fiber로 하는 CFG와 동치이며, 이 CFG는 stack이다.
:::
::: 증명
먼저 $\mathbb{G}_m$-torsor와 line bundle의 동치를 본다. $T$ 위의 [\[스킴\] §준연접층, ⁋정의 12](/ko/math/scheme_theory/quasicoherent_sheaves#def12)의 invertible sheaf $\mathcal{L}$에 대하여, 그 frame들의 sheaf

$$P_\mathcal{L}=\rIsom_{\mathcal{O}}(\mathcal{O}_T, \mathcal{L})$$

을 두면, $\mathbb{G}_m=\rAut(\mathcal{O}_T)$이 합성으로 $P_\mathcal{L}$에 단순추이적으로 작용한다. $\mathcal{L}$이 국소적으로 $\mathcal{O}_T$과 동형이므로 ([\[스킴\] §준연접층, ⁋정의 12](/ko/math/scheme_theory/quasicoherent_sheaves#def12)) $P_\mathcal{L} \rightarrow \ast$은 국소적으로 절단을 가져 [정의 16](#def16)의 두 조건을 만족하고, 따라서 $P_\mathcal{L}$은 $\mathbb{G}_m$-torsor이다. 역으로 $\mathbb{G}_m$-torsor $P$에 대하여 결합 line bundle $\mathcal{L}_P=(P\times \mathbb{A}^1)/\mathbb{G}_m$ ($t$이 $(p, v)$을 $(t\cdot p, t^{-1}v)$으로 보내는 작용에 대한 quotient)을 두면 invertible sheaf를 얻는다. 두 대응이 서로 quasi-inverse이며 isomorphism과 호환되므로 ([\[범주론\] §자연변환, ⁋정의 2](/ko/math/category_theory/natural_transformations#def2)), groupoid $\bB\mathbb{G}_m(T)$과 $\mathcal{L}(T)$은 동치이고, 따라서 두 CFG가 동치이다.

이제 $\mathcal{L}$이 stack임을 본다. $\mathcal{L}$은 [정리 14](#thm14)의 quasi-coherent sheaf stack $\mathcal{QC}$의 충만한 부분 CFG로, invertible sheaf만을 대상으로 취한 것이다.

Prestack. 두 invertible sheaf $\mathcal{L}, \mathcal{M}$에 대하여 $\rIsom_T(\mathcal{L}, \mathcal{M})$은 $\mathcal{QC}$의 $\rIsom$의 부분presheaf이고, 후자가 sheaf이므로 ([정리 14](#thm14)의 prestack 부분) 전자가 sheaf임을 보이려면 그것이 닫힌 부분sheaf 조건으로 잘라짐을 확인하면 된다. $\mathcal{O}_T$-module층 morphism $\mathcal{L} \rightarrow \mathcal{M}$이 동형인지는 국소적으로 검사되는 조건이므로 ([\[위상수학\] §층, ⁋명제 4](/ko/math/topology/sheaves#prop4)), $\rIsom$은 $\rHom$의 sheaf 부분대상이고 sheaf이다.

Effective descent. Covering family $\{T_i \rightarrow T\}$ 위에 invertible sheaf $\mathcal{L}_i$들과 cocycle 동형 $\varphi_{ij}$의 descent datum이 주어졌다 하자. 이를 quasi-coherent sheaf의 descent datum으로 보면, $\mathcal{QC}$이 stack이므로 ([정리 14](#thm14)) $T$ 위의 quasi-coherent sheaf $\mathcal{L}$과 $\mathcal{L}\vert_{T_i}\cong \mathcal{L}_i$으로 유일하게 붙는다. 남은 것은 이 $\mathcal{L}$이 invertible임을 보이는 것이다. "Invertible" (rank 1 locally free)은 fpqc faithfully flat base change에 대하여 내려오는 성질이므로 ([\[스킴\] §충실평탄하강, ⁋명제 7](/ko/math/scheme_theory/faithfully_flat_descent#prop7)의 locally free of finite rank descent), $\mathcal{L}\vert_{T_i}=\mathcal{L}_i$이 각각 invertible이고 $\{T_i \rightarrow T\}$이 covering이므로 $\mathcal{L}$도 invertible이다. 따라서 descent datum이 $\mathcal{L}(T)$ 안에서 effective이고, prestack 조건과 합하여 $\mathcal{L}\cong \bB\mathbb{G}_m$은 stack이다.
:::

[정리 17](#thm17)은 stack 이론의 출발점을 압축한다. Line bundle은 isomorphism class의 집합 $\Pic$으로는 sheaf로 분류되지 않지만, automorphism $\mathbb{G}_m$을 함께 기억하는 groupoid 값 functor로 보면 stack $\bB\mathbb{G}_m$으로 완벽히 분류된다. 그 stack 성질은 [정리 14](#thm14)의 quasi-coherent sheaf descent에서 invertible이라는 국소 성질이 faithfully flat base change로 내려온다는 [\[스킴\] §충실평탄하강, ⁋명제 7](/ko/math/scheme_theory/faithfully_flat_descent#prop7)을 더하여 따라온다. 더 일반적인 group $G$에 대한 $\bB G$이나 [예시 9](#ex9)의 moduli CFG $\mathcal{M}_g$이 stack인지, 나아가 그것이 algebraic stack이라는 더 강한 기하학적 조건을 만족하는지는 같은 descent 원리를 토대로 이후의 글에서 전개한다.

---

**참고문헌**

**[Vis]** A. Vistoli, *Notes on Grothendieck topologies, fibered categories and descent theory*. In *Fundamental algebraic geometry: Grothendieck's FGA explained*, Mathematical Surveys and Monographs, American Mathematical Society, 2005.  
**[Ols]** M. Olsson, *Algebraic spaces and stacks*. American Mathematical Society Colloquium Publications, 2016.  
**[FGA]** B. Fantechi, L. Göttsche, L. Illusie, S. Kleiman, N. Nitsure, A. Vistoli, *Fundamental algebraic geometry: Grothendieck's FGA explained*. Mathematical Surveys and Monographs, American Mathematical Society, 2005.  
**[Stacks]** The Stacks Project Authors, *The Stacks Project*. Available [online](https://stacks.math.columbia.edu/).
