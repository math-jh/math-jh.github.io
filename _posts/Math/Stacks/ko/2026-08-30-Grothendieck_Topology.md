---
title: "Grothendieck 위상과 site"
description: "위상공간의 열린 덮개 개념을 범주 위의 covering으로 추상화하여 Grothendieck 위상과 site를 정의하고, site 위의 presheaf·sheaf와 sheafification, étale·fppf·fpqc 위상의 예시를 다룬다."
excerpt: "Grothendieck topologies, sites, sheaves on a site, and the étale/fppf/fpqc examples"

categories: [Math / Stacks]
permalink: /ko/math/stacks/grothendieck_topology
sidebar: 
    nav: "stacks-ko"

date: 2026-08-30
weight: 1

published: false

---

위상공간 위의 sheaf는 open cover 위의 국소적인 자료를 대역적인 자료로 붙이는 장치이다. ([\[위상수학\] §층, ⁋정의 1](/ko/math/topology/sheaves#def1)) Algebraic geometry에서는 Zariski open cover만으로 faithfully flat morphism을 따른 하강을 포착할 수 없으므로, covering을 범주의 morphism으로 추상화해야 한다. ([\[스킴\] §충실평탄하강, ⁋정의 9](/ko/math/scheme_theory/faithfully_flat_descent#def9)) 앞선 글에서는 이 구조를 covering family로 주어지는 pretopology의 형태로 사용하였다. 이 글에서는 이를 sieve로 주어진 Grothendieck 위상과 구별하고, site 위의 sheaf와 sheafification을 전개한 뒤 étale·fppf·fpqc 위상과 subcanonical 조건을 살펴본다.

이 언어가 stack 이론의 첫 단계에 놓이는 까닭은 gluing 자체가 stack에서 처음 나타나기 때문은 아니다. Scheme도 affine scheme들을 open overlap의 isomorphism으로 붙여 구성하므로 이미 Zariski descent를 사용한다. 다만 open embedding으로 이루어진 이 gluing에서는 overlap이 실제 open subscheme이고, descent가 underlying topological space와 structure sheaf의 gluing에 흡수된다. 반면 moduli problem의 local object들은 overlap 위에서 문자 그대로 같기보다 isomorphic하며 nontrivial automorphism을 가질 수 있고, covering morphism도 embedding일 필요가 없다. 따라서 stack을 정의하려면 먼저 어떤 morphism을 covering으로 인정하는지와 그 위에서 자료가 내려오는 조건을 분리하여 명시해야 한다. 이 글은 그 Set-valued 형태를 정리하고, 이후 stack은 Set을 object와 isomorphism으로 이루어진 groupoid로 바꾸어 같은 descent 조건을 확장한다.

## Sieve와 covering sieve

위상공간 $X$의 열린집합 $U$를 덮는다는 것은 열린집합들의 모임 $\{U_i\}$로 $U=\bigcup U_i$가 되는 것이다. 이를 범주의 언어로 옮길 때 가장 먼저 마주치는 어려움은, 일반적인 범주에는 "합집합"이나 "포함관계"가 없고 오직 morphism만이 있다는 점이다. 열린포함 $U_i\hookrightarrow U$를 morphism으로 받아들이면, covering은 공역이 $U$인 morphism들의 모임 $\{U_i \rightarrow U\}$으로 표현된다. 그런데 어떤 morphism이 이 covering을 "통과"하는가, 즉 어떤 $V \rightarrow U$가 covering으로부터 인수분해되는가 하는 정보를 함께 다루는 편이 위상의 공리를 진술하기에 편리하다. 이를 담는 개념이 sieve이다.

이하에서 $\mathcal{C}$는 고정된 범주이고, $U$는 그 대상이다.

::: 정의 1
대상 $U\in \mathcal{C}$ 위의 *sieve<sub>체</sub>*란, 공역이 $U$인 morphism들의 모임 $S$로서 합성에 대해 닫혀 있는 것이다. 즉 $(f: V \rightarrow U)\in S$이고 $g: W \rightarrow V$가 임의의 morphism이면 $(f\circ g: W \rightarrow U)\in S$이다. Morphism $g: V \rightarrow U$와 $U$ 위의 sieve $S$에 대하여, $V$ 위의 *pullback sieve<sub>당김 체</sub>*를

$$g^\ast S=\{h: W \rightarrow V\mid g\circ h\in S\}$$

으로 정의한다.
:::

Sieve는 representable presheaf $h_U=\Hom_\mathcal{C}(-, U)$의 subfunctor와 같은 것으로 보아도 좋다. 실제로 $S$가 $U$ 위의 sieve라면, 각 대상 $V$에 subset $S(V)=\{f: V \rightarrow U\mid f\in S\}\subseteq \Hom_\mathcal{C}(V, U)$을 대응시키는 것이 $h_U$의 subfunctor를 이루며, 합성에 대해 닫혀 있다는 조건이 정확히 이것이 functorial임을 보장한다. ([\[범주론\] §표현가능한 함자, ⁋정의 1](/ko/math/category_theory/representable_functors#def1)) Pullback sieve $g^\ast S$는 이 관점에서 $h_g: h_V \rightarrow h_U$를 따른 subfunctor $S\subseteq h_U$의 preimage이며, $g^\ast S$가 다시 sieve임은 정의로부터 곧바로 확인된다. 가장 큰 sieve는 $U$로 가는 모든 morphism의 모임 $t_U=\{f\mid \operatorname{cod} f=U\}=h_U$로, 이를 $U$ 위의 *maximal sieve*라 부른다.

공역이 $U$인 morphism들의 모임 $\{f_i: U_i \rightarrow U\}_{i\in I}$이 주어지면, 이를 포함하는 가장 작은 sieve가 존재한다. 그것은 어떤 $f_i$를 통해 인수분해되는 morphism들의 모임

$$\langle f_i\rangle=\{f: V \rightarrow U\mid f=f_i\circ g\text{ for some }i\in I\text{ and }g: V \rightarrow U_i\}$$

이며, 이를 $\{f_i\}$가 *생성하는 sieve*라 부른다. 우리는 곧 "covering"를 이러한 covering family로 줄 수도 있고, 그것이 생성하는 covering sieve로 줄 수도 있음을 보게 된다. 먼저 sieve를 이용한 정의를 제시한다.

::: 정의 2
범주 $\mathcal{C}$ 위의 *Grothendieck topology*이란, 각 대상 $U\in \mathcal{C}$에 $U$ 위의 sieve들의 모임 $J(U)$을 대응시키는 것으로서, 그 원소를 *covering sieve<sub>덮개 체</sub>*라 부르며 다음 세 조건을 만족하는 것이다.

1. (Maximality) 임의의 $U$에 대하여 maximal sieve $t_U$는 $J(U)$에 속한다.
2. (Stability) $S\in J(U)$이고 $g: V \rightarrow U$가 임의의 morphism이면 $g^\ast S\in J(V)$이다.
3. (Transitivity) $S\in J(U)$이고, $R$이 $U$ 위의 sieve로서 모든 $(f: V \rightarrow U)\in S$에 대하여 $f^\ast R\in J(V)$를 만족하면 $R\in J(U)$이다.

이 자료를 $\tau$로 적기도 하며, $J(U)$를 $\tau(U)$로도 쓴다.
:::

세 조건은 위상공간의 open cover가 만족하던 성질을 정확히 추상화한 것이다. Maximality는 $U$가 그 자신을 자명하게 덮는다는 것이고, stability는 covering을 임의의 morphism으로 당겨도 여전히 covering이라는 것으로 위상공간에서 $\{U_i\}$가 $U$를 덮을 때 $\{U_i\cap V\}$가 $V$를 덮는 사실에 대응한다. Transitivity는 "covering의 covering은 covering"이라는 국소성이다. 즉 $S$의 각 마디 위에서 $R$이 covering임이 확인되면 $R$ 자체가 covering이라는 것으로, 어떤 성질을 covering 위에서 국소적으로 검사할 수 있게 해준다. 이 세 조건만으로 sheaf 이론을 전개하기에 충분하나, 실제 예시를 구성할 때는 sieve보다 covering family를 직접 다루는 편이 자연스럽다. 이를 위한 동치 자료가 pretopology이다.

## Covering family와 pretopology

Algebraic geometry의 예시들에서 covering은 거의 항상 $\{U_i \rightarrow U\}$ 꼴의 사상족으로 주어지며, stability 조건은 이 족을 base change하는 것, 즉 fiber product를 취하는 것으로 표현된다. ([\[범주론\] §극한, ⁋예시 8](/ko/math/category_theory/limits#ex8)) 따라서 fiber product가 존재하는 범주에서는 sieve를 거치지 않고 covering family만으로 위상을 기술할 수 있다.

::: 정의 3
Fiber product를 가지는 범주 $\mathcal{C}$ 위의 *Grothendieck pretopology<sub>그로텐디크 준위상</sub>*란, 각 대상 $U$에 공역이 $U$인 사상족 $\{f_i: U_i \rightarrow U\}_{i\in I}$들의 모임을 대응시키는 것으로서, 그 원소를 *covering family<sub>덮개족</sub>*라 부르며 다음 세 조건을 만족하는 것이다.

1. (Isomorphism) $f: V \rightarrow U$가 isomorphism이면 한원소 족 $\{f: V \rightarrow U\}$은 covering family이다.
2. (Base change) $\{f_i: U_i \rightarrow U\}$가 covering family이고 $g: V \rightarrow U$가 임의의 morphism이면, projection $\{\operatorname{pr}_2: U_i\times_U V \rightarrow V\}$ 또한 covering family이다.
3. (Transitivity) $\{f_i: U_i \rightarrow U\}$가 covering family이고, 각 $i$마다 $\{g_{ij}: U_{ij} \rightarrow U_i\}_{j\in J_i}$가 covering family이면, 합성족 $\{f_i\circ g_{ij}: U_{ij} \rightarrow U\}_{i, j}$ 또한 covering family이다.
:::

이 covering family 자료는 [\[스킴\] §충실평탄하강, ⁋정의 8](/ko/math/scheme_theory/faithfully_flat_descent#def8)에서 Grothendieck topology라 부른 것과 같다. 그 글은 sieve를 쓰지 않고 covering family만으로 sheaf 조건을 진술하므로 두 자료를 구별할 필요가 없었으며, 이 글에서는 sieve로 주어진 것을 위상, covering family로 주어진 것을 pretopology라 불러 구별한다. Pretopology는 위상보다 다루기 쉬운 대신 같은 위상을 여러 pretopology가 줄 수 있다는 점에서 위상보다 정밀하지 않은 자료이다. Pretopology가 주어지면, 그것이 생성하는 covering family를 포함하는 sieve를 covering sieve로 선언함으로써 위상을 얻는다.

::: 명제 4
$\mathcal{C}$ 위의 Grothendieck pretopology $\operatorname{Cov}$가 주어졌다 하자. 각 $U$에 대하여, $U$ 위의 sieve $S$가 $J(U)$에 속함을 "어떤 covering family $\{f_i: U_i \rightarrow U\}\in \operatorname{Cov}(U)$가 존재하여 $\langle f_i\rangle\subseteq S$인 것"으로 정의하면, $J$는 $\mathcal{C}$ 위의 Grothendieck 위상이다.
:::
::: 증명
[정의 2](#def2)의 세 조건을 차례로 확인한다.

Maximality. $\id_U: U \rightarrow U$는 isomorphism이므로 [정의 3](#def3)의 첫째 조건에 의하여 $\{\id_U\}$은 covering family이고, 그것이 생성하는 sieve는 maximal sieve $t_U$ 자신이다. 따라서 $t_U\in J(U)$이다.

Stability. $S\in J(U)$이면 $\langle f_i\rangle\subseteq S$인 covering family $\{f_i: U_i \rightarrow U\}$가 있다. 임의의 $g: V \rightarrow U$에 대하여 base change 조건으로 $\{\operatorname{pr}_2: U_i\times_U V \rightarrow V\}$은 covering family이며, 이것이 생성하는 sieve가 $g^\ast S$에 포함됨을 보이면 된다. $\operatorname{pr}_2: U_i\times_U V \rightarrow V$를 통해 인수분해되는 임의의 $h: W \rightarrow V$에 대하여, $g\circ h$는 $g\circ \operatorname{pr}_2=f_i\circ \operatorname{pr}_1$를 거쳐 $f_i$로 인수분해되므로 $g\circ h\in \langle f_i\rangle\subseteq S$, 즉 $h\in g^\ast S$이다. 따라서 $g^\ast S\in J(V)$이다.

Transitivity. $S\in J(U)$이고, $U$ 위의 sieve $R$이 모든 $(f: V \rightarrow U)\in S$에 대하여 $f^\ast R\in J(V)$를 만족한다 하자. $\langle f_i\rangle\subseteq S$인 covering family $\{f_i: U_i \rightarrow U\}$를 잡으면, 각 $f_i\in S$이므로 $f_i^\ast R\in J(U_i)$이고, 따라서 $\langle g_{ij}\rangle\subseteq f_i^\ast R$인 covering family $\{g_{ij}: U_{ij} \rightarrow U_i\}$가 있다. $g_{ij}\in f_i^\ast R$이라는 것은 $f_i\circ g_{ij}\in R$이라는 뜻이므로, transitivity 조건으로 얻은 covering family $\{f_i\circ g_{ij}: U_{ij} \rightarrow U\}$의 모든 원소가 $R$에 속한다. 그것이 생성하는 sieve가 $R$에 포함되므로 $R\in J(U)$이다.
:::

[명제 4](#prop4)로 얻은 위상에서 covering sieve은 곧 어떤 covering family를 "포함하는" sieve이며, 따라서 sheaf 조건처럼 covering sieve 전체에 대해 진술되는 성질도 generating covering family만으로 검사할 수 있게 된다. 이 환원은 다음 절의 sheaf 조건에서 본질적으로 사용된다. 한편 서로 다른 두 pretopology가 같은 위상을 생성할 수 있는데, 가령 한 affine scheme의 모든 principal open으로 이루어진 covering과 모든 finite affine open cover는 같은 Zariski 위상을 준다.

::: 정의 5
범주 $\mathcal{C}$와 그 위의 Grothendieck topology $\tau$의 쌍 $(\mathcal{C}, \tau)$을 *site<sub>사이트</sub>*라 부른다. 위상이 pretopology로 주어진 경우에도 ([명제 4](#prop4)로 얻는 위상을 통해) 그 쌍을 site라 부른다.
:::

엄밀하게는 sheaf의 값을 이루는 곱과 limit이 잘 존재하도록 $\mathcal{C}$가 작은 범주이거나 적절한 집합론적 크기 조건을 만족할 것을 요구하지만, 이 글에서는 이러한 set-theoretic 문제를 다루지 않고 필요한 곱과 limit이 존재한다고 전제한다. 이제 구체적인 site의 예시들을 살펴본다.

## Site의 예시

가장 기본이 되는 예시는 위상공간의 열린집합들이 이루는 site이며, 이것이 고전적인 sheaf 개념을 그대로 회복함을 먼저 확인한다.

::: 예시 6 (위상공간의 site)
위상공간 $X$에 대하여, 대상이 $X$의 열린집합이고 morphism이 포함관계 $V\subseteq U$인 부분순서 범주를 $\Op(X)$라 하자. 이 범주에서 fiber product는 교집합 $U\cap V$로 주어진다. 각 열린집합 $U$ 위의 covering family를 통상적인 open cover $\{U_i\hookrightarrow U\}$ ($U=\bigcup_i U_i$)로 정의하면 이는 pretopology를 이룬다. Isomorphism 조건은 $U=U$ 자신이 $U$를 덮음이고, base change 조건은 $\{U_i\cap V\}$가 $V$를 덮음이며, transitivity는 covering의 세분이 다시 covering임이다. 이렇게 얻은 site $(\Op(X), \tau)$ 위의 sheaf는 정확히 $X$ 위의 고전적인 sheaf와 같다. ([\[위상수학\] §층, ⁋정의 1](/ko/math/topology/sheaves#def1))
:::

[예시 6](#ex6)에서 covering family $\{U_i\hookrightarrow U\}$가 생성하는 covering sieve은 어떤 $U_i$ 안에 포함되는 열린집합 전체로 이루어진 sieve이며, 이는 $\{U_i\}$가 위상공간으로서 $U$를 덮는다는 정보와 동치이다. 이 site의 특징은 모든 morphism이 monomorphism(포함)이라는 점인데, 일반적인 site에서는 covering의 morphism이 단사일 필요가 없고, 바로 이 점이 다음의 algebraic geometry 예시들을 고전적 위상과 구별짓는다.

::: 예시 7 (Zariski site)
Scheme $X$에 대하여 두 가지 site가 있다. *작은 Zariski site* $X_{\Zar}$는 대상이 $X$의 열린집합(open subscheme)이고 morphism이 열린포함이며, covering family가 open cover인 site로, 이는 위상공간 $X$의 site $\Op(X)$와 본질적으로 같다. *큰 Zariski site*는 slice 범주 $\Sch/X$를 밑범주로 삼고, $X$-scheme들의 족 $\{U_i \rightarrow T\}$이 각 $U_i \rightarrow T$가 open embedding이고 합 $\coprod U_i \rightarrow T$가 전사일 때 covering family로 선언한 site이다. 큰 site는 $X$ 위의 모든 scheme을 동시에 다루므로 functorially 정의된 대상의 sheaf 성질을 논하기에 적합하다.
:::

작은 Zariski site는 열린집합이 너무 적어서, 가령 모든 점의 잔여체가 같은 경우조차 구별하지 못하는 등의 한계를 가진다. 이를 극복하기 위해 열린포함보다 넓은 종류의 morphism을 covering으로 허용하는 것이 다음의 étale 위상이다.

::: 예시 8 (étale site)
Scheme $X$의 *작은 étale site* $X_{\et}$는 대상이 étale morphism $U \rightarrow X$이고, morphism이 그 위의 $X$-morphism이며 (étale morphism 사이의 $X$-morphism은 자동으로 étale이다), covering family가 jointly surjective한 étale morphism족 $\{U_i \rightarrow U\}$인 site이다. ([\[스킴\] §매끄러운 사상과 에탈 사상, ⁋정의 11](/ko/math/scheme_theory/smooth_and_etale_morphisms#def11)) 더 일반적으로 *큰 étale site*는 $\Sch/X$ 위에서 jointly surjective한 étale morphism족을 covering family로 삼는다. 두 경우 모두 base change 조건은 étale morphism이 base change에 대해 닫혀 있음으로부터, transitivity는 étale morphism의 합성이 étale임으로부터 따른다.
:::

[예시 8](#ex8)의 covering에서 morphism $U_i \rightarrow U$은 더 이상 단사가 아니며, fiber가 여러 점을 가질 수 있다. 가령 유한 분리 가능한 체확대 $\Spec L \rightarrow \Spec K$나, 밑에서 $n$이 가역일 때 multiplicative group의 $n$제곱 morphism은 étale covering의 전형적인 예이다. 이렇게 단사가 아닌 covering을 허용하기에 étale site의 sheaf 조건은 두 겹 겹침 $U_i\times_U U_i$가 대각선 $U_i$에 그치지 않는 비자명한 자료를 담게 되고, 이것이 étale cohomology가 Zariski cohomology보다 풍부한 근본 이유이다. étale보다 더 넓은 flat morphism을 covering으로 삼으면 fppf와 fpqc 위상을 얻는다.

::: 예시 9 (fppf와 fpqc site)
밑범주를 $\Sch$ (또는 $\Sch/S$)로 둔다. 사상족 $\{f_i: U_i \rightarrow U\}$이 *fppf covering family*라는 것은 각 $f_i$가 flat이고 locally of finite presentation이며 합 $\coprod U_i \rightarrow U$가 전사인 것이다 (이름은 *fidèlement plat de présentation finie*에서 온다). 더 넓게, $\{f_i: U_i \rightarrow U\}$이 *fpqc covering family*라는 것은 각 $f_i$가 flat이고, $\coprod U_i \rightarrow U$가 전사이며, $U$의 각 affine open이 유한히 많은 $U_i$의 affine open들의 상으로 덮이는 quasi-compact 조건을 만족하는 것이다. ([\[스킴\] §충실평탄하강, ⁋정의 9](/ko/math/scheme_theory/faithfully_flat_descent#def9)) 두 경우 모두 flatness와 전사성이 base change·합성에 대해 보존되므로 pretopology를 이루며, fppf covering은 항상 fpqc covering이다.
:::

이로써 Zariski $\subseteq$ étale $\subseteq$ fppf $\subseteq$ fpqc의 순서로 점점 더 많은 covering을 허용하는 위상들의 위계를 얻는다. 위상이 미세해질수록(더 많은 covering을 가질수록) sheaf 조건은 강해지고 sheaf의 수는 줄어드는 대신, 하강과 cohomology가 풍부해진다. 특히 fpqc 위상은 한 affine scheme $\Spec A$를 단일한 faithfully flat morphism $\Spec B \rightarrow \Spec A$로 덮는 것을 허용하며, 이것이 faithfully flat descent가 fpqc sheaf 조건으로 번역되는 지점이다.

## Site 위의 presheaf와 sheaf

Site 위의 presheaf는 밑범주 위의 contravariant functor에 다름 아니다. 위상공간의 경우 presheaf가 $\Op(X)^\op \rightarrow \Set$ 꼴의 functor였던 것을 임의의 밑범주로 일반화한 것이다.

::: 정의 10
Site $(\mathcal{C}, \tau)$ 위의 *presheaf*란 contravariant functor $F:\mathcal{C}^\op \rightarrow \Set$이며, presheaf morphism은 natural transformation이다. 이들이 이루는 functor 범주를 $\PSh(\mathcal{C})$로 적는다. $U$ 위의 covering sieve $S\in J(U)$에 대하여, $F$의 $S$ 위의 *matching family<sub>정합족</sub>*란, 각 $(f: V \rightarrow U)\in S$마다 원소 $x_f\in F(V)$를 지정하되 임의의 $g: W \rightarrow V$에 대하여

$$F(g)(x_f)=x_{f\circ g}$$

를 만족하는 족 $(x_f)_{f\in S}$이다. 원소 $x\in F(U)$가 이 matching family의 *amalgamation<sub>접합</sub>*이라는 것은 모든 $(f: V \rightarrow U)\in S$에 대하여 $F(f)(x)=x_f$인 것이다. 이제 presheaf $F$가

1. *separated presheaf<sub>분리 준층</sub>*라는 것은 임의의 covering sieve 위의 matching family가 많아야 하나의 amalgamation을 가지는 것이고,
2. *sheaf<sub>층</sub>*라는 것은 임의의 covering sieve 위의 matching family가 정확히 하나의 amalgamation을 가지는 것이다.

Sheaf들이 이루는 $\PSh(\mathcal{C})$의 full subcategory를 $\Sh(\mathcal{C}; \tau)$로 적는다.
:::

Matching family는 covering sieve의 각 마디 위에 정합적으로 주어진 국소 자료이고, amalgamation은 그것을 $U$ 전체로 붙인 대역 자료이다. Separated 조건은 붙인 결과가 유일함(identity axiom)을, sheaf 조건은 그것이 항상 존재함(gluability)을 추가한다. 이 sieve 형태의 정의는 임의의 위상에 대해 작동하지만, 위상이 pretopology로 주어진 경우 matching family는 covering family 위의 자료로 다시 쓸 수 있고, sheaf 조건은 익숙한 equalizer 형태가 된다.

::: 명제 11
위상 $\tau$가 pretopology $\operatorname{Cov}$로 [명제 4](#prop4)와 같이 주어졌다 하자. Presheaf $F:\mathcal{C}^\op \rightarrow \Set$가 sheaf인 것은, 모든 covering family $\{f_i: U_i \rightarrow U\}\in \operatorname{Cov}(U)$에 대하여 다음 도식

$$F(U) \xrightarrow{\ e\ } \prod_i F(U_i) \underset{q}{\overset{p}{\rightrightarrows}} \prod_{i, j} F(U_i\times_U U_j)$$

이 equalizer인 것과 동치이다. 여기에서 $e(x)=(F(f_i)(x))_i$이고, 두 morphism $p, q$는 각각 두 projection $\operatorname{pr}_1: U_i\times_U U_j \rightarrow U_i$와 $\operatorname{pr}_2: U_i\times_U U_j \rightarrow U_j$를 따른 restriction $p((s_i)_i)=(F(\operatorname{pr}_1)(s_i))_{i, j}$, $q((s_i)_i)=(F(\operatorname{pr}_2)(s_j))_{i, j}$이다. $F$가 separated인 것은 같은 도식에서 $e$가 단사인 것과 동치이다.
:::
::: 증명
Generating covering sieve $S=\langle f_i\rangle$ 위의 matching family와 위 equalizer의 자료가 일대일로 대응함을 보이면 충분하다.

$S$ 위의 matching family $(x_f)_{f\in S}$가 주어지면, 특히 각 $f_i\in S$에 대한 $s_i=x_{f_i}\in F(U_i)$들의 족 $(s_i)\in \prod_i F(U_i)$을 얻는다. 두 projection $\operatorname{pr}_1: U_i\times_U U_j \rightarrow U_i$와 $\operatorname{pr}_2: U_i\times_U U_j \rightarrow U_j$에 각각 $f_i$와 $f_j$를 합성한 $f_i\circ \operatorname{pr}_1=f_j\circ \operatorname{pr}_2$은 같은 morphism이고 $S$에 속하므로, matching 조건을 $g=\operatorname{pr}_1$과 $g=\operatorname{pr}_2$에 각각 적용하면

$$F(\operatorname{pr}_1)(s_i)=x_{f_i\circ \operatorname{pr}_1}=x_{f_j\circ \operatorname{pr}_2}=F(\operatorname{pr}_2)(s_j)$$

이므로 $p((s_i))=q((s_i))$, 즉 $(s_i)$는 $p, q$의 equalizer에 속한다.

역으로 $p((s_i))=q((s_i))$인 $(s_i)\in \prod_i F(U_i)$이 주어지면, $S$ 위의 matching family를 다음과 같이 정의한다. $f\in S$이면 $f=f_i\circ g$인 $i$와 $g: V \rightarrow U_i$가 있으므로 $x_f=F(g)(s_i)$로 둔다. 이것이 well-defined임, 즉 $f=f_i\circ g=f_j\circ g'$인 두 인수분해에서 같은 값을 줌은 $(g, g'): V \rightarrow U_i\times_U U_j$로 묶은 뒤 $p((s_i))=q((s_i))$의 $(i, j)$-성분을 $F(g, g')$로 당겨 $F(g)(s_i)=F(g')(s_j)$를 얻음으로써 확인된다. 이 대응이 matching family 조건을 만족함과, 두 구성이 서로 역임은 정의로부터 직접 따른다.

따라서 amalgamation $x\in F(U)$의 존재·유일성은 정확히 $e$가 equalizer로의 전단사임과 같다. Sheaf 조건은 amalgamation의 존재와 유일성이므로 $e$가 equalizer 위로의 전단사, 즉 위 도식이 equalizer인 것과 동치이고, separated 조건은 유일성뿐이므로 $e$가 단사인 것과 동치이다.

마지막으로 $J(U)$의 covering sieve $S'$은 generating covering sieve $\langle f_i\rangle$을 포함할 뿐 그와 같을 필요는 없으므로, $S'$ 위의 matching family를 $\langle f_i\rangle$로 제한하여 얻은 $x$가 $S'$ 전체의 amalgamation임을 확인해야 한다. 임의의 $(f: V \rightarrow U)\in S'$에 대하여 base change한 covering family $\{\operatorname{pr}_2: U_i\times_U V \rightarrow V\}$을 잡으면 $f\circ \operatorname{pr}_2=f_i\circ \operatorname{pr}_1\in \langle f_i\rangle$이므로 $F(\operatorname{pr}_2)(F(f)(x))=x_{f\circ \operatorname{pr}_2}=F(\operatorname{pr}_2)(x_f)$이고, 이 covering family에 대한 $e$의 단사성으로 $F(f)(x)=x_f$를 얻는다.
:::

[명제 11](#prop11)은 site 위의 sheaf 조건이 위상공간 위의 그것과 형식적으로 동일함을 보여준다. ([\[위상수학\] §층, ⁋정의 1](/ko/math/topology/sheaves#def1)) 다만 두 겹 겹침이 교집합 $U_i\cap U_j$ 대신 fiber product $U_i\times_U U_j$로 바뀐다. 위상공간에서는 covering의 morphism이 모두 단사여서 $U_i\times_U U_i=U_i$이지만, étale이나 fpqc covering에서는 $U_i\times_U U_i$이 $U_i$보다 클 수 있고, 바로 이 차이가 비단사 covering 위의 하강을 가능하게 한다. 특히 단일 morphism으로 이루어진 fpqc covering $\{\Spec B \rightarrow \Spec A\}$에 대해서는 이 equalizer가 faithfully flat descent의 Amitsur 정확열로 환원되는데, 이는 아래에서 다시 다룬다.

이제 presheaf가 sheaf가 아닌 전형적인 예를 보고, 이를 통해 sheafification의 필요를 동기화한다.

::: 예시 12 (sheaf가 아닌 separated presheaf)
$X$가 비어 있지 않은 두 connected 열린집합의 disjoint union $X=U_1\sqcup U_2$인 위상공간이라 하고, 원소가 둘 이상인 집합 $A$에 대하여 상수 presheaf $\underline{A}^{\mathrm{pre}}$를 비어 있지 않은 열린집합 $V$에는 $\underline{A}^{\mathrm{pre}}(V)=A$로, 빈 열린집합에는 $\underline{A}^{\mathrm{pre}}(\emptyset)=\{\ast\}$ (한원소 집합)으로 두고, 비어 있지 않은 열린집합 사이의 restriction을 항등으로 정의하자. Covering $\{U_1, U_2\}$를 생각하면 $U_1\cap U_2=\emptyset$이고 [명제 11](#prop11)의 equalizer에서 겹침을 담는 항이 $\underline{A}^{\mathrm{pre}}(\emptyset)=\{\ast\}$이라 한원소 집합이므로 겹침 조건이 공허하고, 따라서 서로 다른 $a_1, a_2\in A$를 각각 $U_1, U_2$ 위의 자료로 택한 것이 matching family를 이룬다. 그러나 이를 붙인 $X$ 위의 원소는 $\underline{A}^{\mathrm{pre}}(X)=A$의 한 원소여야 하는데 그것이 $U_1$과 $U_2$ 위에서 동시에 $a_1, a_2$로 restrict될 수는 없으므로 amalgamation이 존재하지 않는다. 한편 두 원소가 모든 $U_i$ 위에서 일치하면 같으므로 이 presheaf는 separated이다. 그 sheafification은 locally constant 함수의 sheaf $\underline{A}$로, $\underline{A}(X)=A\times A$이다.
:::

[예시 12](#ex12)는 separated와 sheaf의 차이를 분명히 보여준다. 자료를 비정합적으로 붙이려는 시도가 실패하는 것이 아니라, 정합적인 국소 자료조차 붙일 대역 자료가 presheaf 안에 없는 것이다. Sheafification은 이러한 결손을 보편적인 방식으로 보충하여 presheaf에 가장 가까운 sheaf를 부여하는 조작이며, site 위에서는 plus construction으로 구성된다.

## Sheafification과 plus construction

위상공간 위에서 우리는 sheafification을 forgetful functor의 left adjoint로 특징지었고, 그 존재를 compatible germ들의 sheaf로 직접 구성하였다. ([\[위상수학\] §층, ⁋정의 5](/ko/math/topology/sheaves#def5)) 일반적인 site에는 "점"이나 "stalk"이 없으므로 germ을 이용한 구성은 불가능하고, 대신 모든 covering에 걸친 colimit을 취하는 plus construction을 사용한다.

::: 정의 13
Presheaf $F:\mathcal{C}^\op \rightarrow \Set$와 대상 $U$에 대하여, $U$ 위의 covering sieve들의 모임을 역포함 $S'\subseteq S\Rightarrow S\preceq S'$으로 순서지으면, stability와 transitivity에 의해 이는 filtered preorder를 이룬다. 각 covering sieve $S$에 $S$ 위의 matching family들의 집합 $\operatorname{Match}(S, F)$을 대응시키고, 세분 $S\preceq S'$에 matching family의 restriction을 대응시키면 filtered diagram을 얻으며, 그 colimit

$$F^+(U)=\varinjlim_{S\in J(U)}\operatorname{Match}(S, F)$$

을 $F$의 *plus construction<sub>plus 구성</sub>*이라 부른다. $U\mapsto F^+(U)$은 presheaf를 이루며, maximal sieve 위의 matching family가 $F(U)$의 원소와 같으므로 자연스러운 morphism $F \rightarrow F^+$이 있다.
:::

직관적으로 $F^+(U)$의 원소는 "어떤 covering 위에서 정합적으로 주어진 국소 자료"를, 더 미세한 covering으로 옮겨도 같아지는 것들끼리 동일시한 것이다. 두 matching family가 공통의 세분 위에서 일치하면 같은 원소로 본다는 것이 colimit의 의미이며, 이로써 amalgamation의 유일성 결손(separated 실패)이 교정된다. Pretopology의 언어로는 $F^+(U)$이 covering $\{U_i \rightarrow U\}$들에 걸친 Čech 영차 cohomology

$$\check{H}^0(\{U_i \rightarrow U\}, F)=\operatorname{eq}\Big(\prod_i F(U_i)\rightrightarrows \prod_{i, j}F(U_i\times_U U_j)\Big)$$

의 filtered colimit이다. 다음 정리가 이 구성의 핵심 성질이다.

::: 정리 14
임의의 presheaf $F$에 대하여 다음이 성립한다.

1. $F^+$은 separated presheaf이다.
2. $F$가 separated이면 $F^+$은 sheaf이다. 따라서 $F^{++}=(F^+)^+$은 항상 sheaf이다.
3. 대응 $a(F)=F^{++}$은 forgetful functor $\iota:\Sh(\mathcal{C}; \tau)\hookrightarrow \PSh(\mathcal{C})$의 left adjoint이며, 자연스러운 morphism $F \rightarrow F^{++}$이 그 unit이다. 즉 임의의 sheaf $G$에 대하여

$$\Hom_{\Sh}(F^{++}, G)\cong \Hom_{\PSh}(F, G)$$

이 성립한다. 나아가 $a$는 finite limit을 보존한다.
:::

이 정리는 plus construction의 표준 성질로 받아들이며, 자세한 증명은 [Stacks]나 [MM]을 참조한다.

[정리 14](#thm14)는 [\[위상수학\] §층, ⁋정의 5](/ko/math/topology/sheaves#def5)에서 다룬 sheafification adjunction을 임의의 site로 확장한다. Left adjoint $a$가 finite limit을 보존한다는 사실은 특히 중요한데, 이로부터 sheaf 범주가 위상공간의 sheaf 범주와 같은 종류의 좋은 구조를 가짐이 따라온다.

::: 참고 15
Site $(\mathcal{C}, \tau)$ 위의 sheaf 범주 $\Sh(\mathcal{C}; \tau)$를 *Grothendieck topos<sub>그로텐디크 토포스</sub>*라 부른다. 이는 작은 site 위의 sheaf 범주와 동치인 범주로 정의되며, 모든 작은 limit과 colimit을 가지고, cartesian closed이며, subobject classifier를 가지는 등 집합 범주 $\Set$이 누리는 형식적 성질의 대부분을 공유한다. $\Set$ 자신은 한원소 위상공간(또는 trivial site) 위의 sheaf 범주로서 가장 단순한 topos이다. Topos 이론은 그 자체로 방대한 주제이므로 여기에서는 정의를 언급하는 데 그치고, 이후 stack의 맥락에서 필요한 만큼만 다룬다.
:::

## Subcanonical 위상과 representable presheaf

Site 위의 sheaf 이론이 scheme 이론과 만나는 결정적인 지점은, 밑범주의 대상이 정의하는 representable presheaf가 그 위상에 대해 sheaf인가 하는 물음이다. 이것이 성립하면 대상 $X$를 그 functor of points $h_X$와 동일시하여 sheaf 범주 안의 한 대상으로 다룰 수 있고, scheme의 functorial 정의가 sheaf의 언어로 정당화된다. ([\[범주론\] §표현가능한 함자, ⁋정의 1](/ko/math/category_theory/representable_functors#def1))

::: 정의 16
Site $(\mathcal{C}, \tau)$가 *subcanonical<sub>준표준</sub>*이라는 것은, 모든 대상 $X\in \mathcal{C}$에 대하여 representable presheaf $h_X=\Hom_\mathcal{C}(-, X)$이 $\tau$-sheaf인 것이다. Subcanonical 위상들 가운데 가장 미세한 것이 존재하며 이를 *canonical topology<sub>표준 위상</sub>*라 부른다. 즉 어떤 위상이 subcanonical인 것은 그것이 canonical topology보다 거칠거나 같은 것이다.
:::

Subcanonical 조건은 [명제 11](#prop11)을 통해 구체적으로 진술된다. $h_X$가 sheaf라는 것은, 각 covering family $\{U_i \rightarrow U\}$에 대하여 $U$에서 $X$로 가는 morphism이 그 covering 위에서 정합적으로 주어진 morphism들로부터 유일하게 붙는다는 것, 즉

$$\Hom(U, X) \rightarrow \prod_i \Hom(U_i, X)\rightrightarrows \prod_{i, j}\Hom(U_i\times_U U_j, X)$$

이 equalizer라는 것이다. 이는 morphism의 하강 조건에 다름 아니다. Zariski나 étale 위상에서 이것이 성립함은 morphism이 covering 위에서 국소적으로 정해진다는 익숙한 사실이지만, fpqc처럼 거친 covering에 대해서는 결코 자명하지 않으며, 그 성립은 faithfully flat descent의 한 형태이다.

::: 정리 17
$\Sch$ (또는 $\Sch/S$) 위의 fpqc 위상은 subcanonical이다. 즉 임의의 scheme $X$에 대하여 functor of points $h_X=\Hom_{\Sch}(-, X)$은 fpqc sheaf이다. 따라서 Zariski·étale·fppf 위상에서도 모든 representable presheaf는 sheaf이다.
:::
::: 증명
[명제 11](#prop11)에 의하여, fpqc covering $\{U_i \rightarrow U\}$에 대한 equalizer 조건을 확인하면 된다. Representable presheaf는 Zariski sheaf이고, 모든 fpqc covering은 $U$의 affine open 위에서 단일 faithfully flat affine covering으로 세분할 수 있다. 따라서 $U=\Spec A$이고 covering이 $\pi:\Spec B \rightarrow \Spec A$인 경우로 환원된다. 이 때 $\Spec B\times_{\Spec A}\Spec B=\Spec(B\otimes_A B)$이므로, 보여야 할 것은

$$\Hom(\Spec A, X) \rightarrow \Hom(\Spec B, X)\rightrightarrows \Hom(\Spec(B\otimes_A B), X)$$

이 equalizer라는 것이다.

먼저 $X=\Spec R$이 affine인 경우, 이 도식은 ring homomorphism의 도식

$$\Hom_{\Ring}(R, A) \rightarrow \Hom_{\Ring}(R, B)\rightrightarrows \Hom_{\Ring}(R, B\otimes_A B)$$

이다. Faithful flatness로 sequence $0 \rightarrow A \rightarrow B \rightrightarrows B\otimes_A B$이 정확하므로 ([\[스킴\] §충실평탄하강, ⁋보조정리 3](/ko/math/scheme_theory/faithfully_flat_descent#lem3)), 즉 $A$가 $d^0, d^1: B \rightrightarrows B\otimes_A B$의 equalizer이므로, $\Hom_{\Ring}(R, -)$을 적용하면 $\varphi: R \rightarrow B$가 $d^0\circ \varphi=d^1\circ \varphi$를 만족하는 것과 $\varphi$가 유일하게 $R \rightarrow A$를 거쳐 인수분해되는 것이 동치임을 얻는다. 이것이 곧 위 equalizer이다. 이는 structure sheaf $\mathcal{O}$이 fpqc sheaf임을 보이는 [\[스킴\] §충실평탄하강, ⁋정리 10](/ko/math/scheme_theory/faithfully_flat_descent#thm10)과 평행한 논증으로, $\Hom_{\Ring}(R, -)$이 같은 Amitsur equalizer를 보존한다는 데에서 따른다.

일반적인 $X$에 대하여, morphism $g:\Spec B\rightarrow X$가 두 projection $\operatorname{pr}_1,\operatorname{pr}_2:\Spec(B\otimes_A B)\rightrightarrows\Spec B$에 대해 $g\circ\operatorname{pr}_1=g\circ\operatorname{pr}_2$를 만족한다고 하자. Faithfully flat morphism $\pi$는 universally submersive이므로, $g$의 underlying continuous map은 유일한 continuous map $h:\Spec A\rightarrow X$로 내려온다. 각 $p\in\Spec A$에 대하여 $h(p)$를 포함하는 affine open $W=\Spec R\subseteq X$를 택하고 $p\in D(a)\subseteq h^{-1}(W)$인 principal open을 잡자. $\pi^{-1}(D(a))=\Spec B_a$ 위에서 $g$는 ring homomorphism $R\rightarrow B_a$를 주고, cocycle 조건에 의하여 그 image는 $B_a\rightrightarrows B_a\otimes_{A_a}B_a$의 equalizer $A_a$에 속한다. 따라서 $g$는 $D(a)$ 위에서 유일한 morphism $D(a)\rightarrow W\rightarrow X$로 내려오며, 이 local morphism들은 같은 affine equalizer 논증으로 overlap에서 일치하므로 유일한 morphism $\Spec A\rightarrow X$로 붙는다. 따라서 $h_X$은 fpqc sheaf이다. Fpqc보다 거친 위상의 covering은 fpqc covering이므로 이들에 대해서도 sheaf 조건이 따라온다.
:::

[정리 17](#thm17)이 stack 이론으로 가는 길을 연다. Scheme $X$를 그 functor of points $h_X:\Sch^\op \rightarrow \Set$과 동일시하면 ([\[범주론\] §표현가능한 함자, ⁋정리 4](/ko/math/category_theory/representable_functors#thm4)), scheme은 fpqc site $\Sch$ 위의 sheaf 가운데 특별한 것, 즉 적절한 representability 조건을 만족하는 sheaf로 자리매김한다. Functorially 정의된 moduli 문제 $F:\Sch^\op \rightarrow \Set$이 scheme을 표현하는지를 묻는 일은, 먼저 $F$가 fpqc sheaf인지를 확인하고 ([\[스킴\] §충실평탄하강, ⁋정리 10](/ko/math/scheme_theory/faithfully_flat_descent#thm10)의 하강 논증과 같은 방식으로) 이어 그것이 국소적으로 representable한지를 보는 두 단계로 나뉜다. Stack은 이 그림에서 sheaf의 값을 집합 대신 groupoid로 확장하여, 점들이 비자명한 automorphism을 가지는 moduli 문제까지 포착하는 일반화이다. 그 정의와 전개는 이후의 글로 미룬다.

## $\mathbb{G}_a$의 sheaf 성질

마지막으로 [정리 17](#thm17)의 특수한 경우에서 Amitsur 정확열이 sheaf 조건으로 번역되는 과정을 확인한다.

::: 예시 18 ($\mathbb{G}_a$는 fpqc sheaf)
$\mathbb{G}_a=\Spec \mathbb{Z}[\x]=\mathbb{A}^1$의 functor of points은 각 scheme $T$에 대역 절단의 가법군

$$\mathbb{G}_a(T)=\Hom_{\Sch}(T, \mathbb{A}^1)=\Gamma(T, \mathcal{O}_T)$$

을 대응시킨다. ([\[스킴\] §점함자, ⁋명제 1](/ko/math/scheme_theory/functor_of_points#prop1)) 단일 fpqc covering $\{\Spec B \rightarrow \Spec A\}$에 대한 sheaf 조건은

$$A \rightarrow B \rightrightarrows B\otimes_A B$$

이 equalizer라는 것이다. 두 morphism은 $b\mapsto b\otimes 1$과 $b\mapsto 1\otimes b$이며, faithful flatness로 $0 \rightarrow A \rightarrow B \xrightarrow{d^1-d^0} B\otimes_A B$가 정확하다. ([\[스킴\] §충실평탄하강, ⁋보조정리 3](/ko/math/scheme_theory/faithfully_flat_descent#lem3)) 따라서 $A=\{b\in B\mid b\otimes 1=1\otimes b\}$이고, $\mathbb{G}_a(\Spec A)=A$는 covering 위의 정합 자료로부터 복원된다.
:::

---

**참고문헌**

**[Vis]** A. Vistoli, *Notes on Grothendieck topologies, fibered categories and descent theory*. In *Fundamental algebraic geometry: Grothendieck's FGA explained*, Mathematical Surveys and Monographs, American Mathematical Society, 2005.  
**[Stacks]** The Stacks Project Authors, *The Stacks Project*. Available [online](https://stacks.math.columbia.edu/).  
**[SGA4]** M. Artin, A. Grothendieck, J.-L. Verdier, *Théorie des topos et cohomologie étale des schémas (SGA 4)*. Lecture Notes in Mathematics 269, 270, 305, Springer, 1972–1973.  
**[MM]** S. Mac Lane, I. Moerdijk, *Sheaves in geometry and logic: A first introduction to topos theory*. Universitext, Springer, 1994.
