---
title: "그로텐디크 위상"
description: "위상공간의 open cover 개념을 category 위의 covering으로 추상화하여 Grothendieck topology와 site를 정의하고, site 위의 presheaf·sheaf와 sheafification, étale·fppf·fpqc topology의 예시를 다룬다."
excerpt: "Grothendieck topologies, sites, sheaves on a site, and the étale/fppf/fpqc examples"

categories: [Math / Stacks]
permalink: /ko/math/stacks/grothendieck_topology
sidebar: 
    nav: "stacks-ko"

date: 2026-08-30
weight: 1

published: false

---

대수기하학에서 우리는 scheme을 정의하기 위해 우선 affine scheme이 무엇인지 정의하고, 이를 붙여 일반적인 scheme을 정의했다. 이는 [\[스킴\] §충실평탄하강, ⁋정의 4](/ko/math/scheme_theory/faithfully_flat_descent#def4)의 언어를 빌리자면 open embedding을 사용하여 정의된 *Zariski open cover*를 이용한 descent를 생각하는 것으로, 해당 글에서 살펴보았듯 descent는 이 <em-ko>붙이는</em-ko> 과정에서 필요한 것을 형식적인 언어로 풀어낸 것이다. 이 언어에서 가장 눈에 띄는 것은 descent datum이 그 입력으로 isomorphism $\Phi$를 요구한다는 것으로, scheme을 구성한 뒤에는 서로 isomorphic했던 두 overlap의 image가 실제로 같은 intersection이 되므로 이 gluing datum이 눈에 잘 보이지 않았던 것이다.

이와 같이 local data를 정확하게 붙이려면, 먼저 어떤 morphism들의 family를 covering으로 인정하고 그 위의 compatible data가 언제 유일한 global data로 내려오는지를 분리해 적어야 한다. 전자는 우리가 [\[스킴\] §충실평탄하강, ⁋정의 8](/ko/math/scheme_theory/faithfully_flat_descent#def8)에서 살펴본 Grothendieck pretopology에서 이미 일반화했던 것이며, 후자는 sheaf condition을 통해 나타나는 것이다. 이 시리즈의 첫 글인 이번 글에서는 이 과정에 집중하여, 이후 stack을 정의하기 위한 언어를 마련한다.

## Sieve와 covering sieve

[\[스킴\] §충실평탄하강, ⁋정의 8](/ko/math/scheme_theory/faithfully_flat_descent#def8)에서와 마찬가지로 우리는 $U$가 target인 morphism들의 모임을 $U$의 covering이라 선언할 것이다. 이와 같이 정의하기 위해서는 필연적으로 어떠한 covering이 다른 covering보다 finer하다는 것이 어떤 의미인지를 설명해야 한다. 즉 주어진 $V\rightarrow U$가 $U$ 위의 covering을 이루는 원소라 할 때, 어떤 $W\rightarrow U$가 이를 factor through하는 것이 어떤 것인지를 설명해야 한다. 

::: 정의 1
Category $\mathcal{C}$와 대상 $U\in \mathcal{C}$에 대하여, $U$ 위의 *sieve<sub>체</sub>*는 다음 조건을 만족하는 morphism들의 모임 $\mathcal{S}$이다. 

1. $\mathcal{S}$의 임의의 원소들의 target은 $U$이다. 
2. $\mathcal{S}$의 임의의 원소 $f: V\rightarrow U$에 대하여, 임의의 morphism $g:W\rightarrow V$가 주어질 때마다 $f\circ g: W\rightarrow U$ 또한 $\mathcal{S}$의 원소이다. 
:::

즉, sieve는 representable presheaf $h_U=\Hom_\mathcal{C}(-, U): \mathcal{C}^\op\rightarrow \Set$의 subfunctor이다. 실제로 $\mathcal{S}$가 $U$ 위의 sieve라면, 각 대상 $V$에 subset 

$$\mathcal{S}(V)=\{f: V \rightarrow U\mid f\in \mathcal{S}\}\subseteq \Hom_\mathcal{C}(V, U)$$

을 대응시키는 것이 $h_U$의 subfunctor $\mathcal{S}$를 이루며, morphism $g:W\rightarrow V$가 주어졌을 때 $\mathcal{S}(g)$는 

$$\mathcal{S}(g):\mathcal{S}(V)\rightarrow \mathcal{S}(W);\qquad f\mapsto f\circ g$$

로 주어지게 된다. 거꾸로 이러한 성질을 만족하는 functor, 즉 $h_U$의 subfunctor가 주어지면 이는 sieve의 조건을 만족하며, 따라서 sieve는 정확히 $h_U$의 subfunctor가 된다. 이러한 관점에서 *maximal* sieve는 이들 중 가장 큰 것, 즉 $h_U$ 그 자체가 주는 sieve로 정의되며 이는 단순히 $U$로 가는 모든 morphism들의 모임이다. 

한편 target이 $U$인 morphism들의 family $\{f_i: U_i \rightarrow U\}_{i\in I}$가 주어지면, 이를 포함하는 가장 작은 sieve가 존재하며, 이는 $f_i$들에 모든 가능한 morphism들을 합성한 모임, 즉 

$$\langle f_i\rangle=\{f: V \rightarrow U\mid f=f_i\circ g\text{ for some }i\in I\text{ and }g: V \rightarrow U_i\}$$

이다. 이를 $\{f_i\}$가 생성하는 sieve라 부른다. 이제 sieve를 다른 대상으로 당겨오는 pullback 연산을 정의한다.

::: 정의 2
Morphism $g: V \rightarrow U$와 $U$ 위의 sieve $\mathcal{S}$에 대하여, $V$ 위의 *pullback sieve<sub>당김 체</sub>* $g^\ast \mathcal{S}$를

$$g^\ast \mathcal{S}=\{h: W \rightarrow V\mid g\circ h\in \mathcal{S}\}$$

으로 정의한다.
:::

위에서 살펴본 subfunctor의 관점에서 pullback sieve $g^\ast \mathcal{S}$는 natural transformation $h_g: h_V \rightarrow h_U$를 따른 subfunctor $\mathcal{S}\subseteq h_U$의 preimage에 해당하며, $g^\ast \mathcal{S}$가 다시 $V$ 위의 sieve임은 정의로부터 곧바로 확인된다. 

이제 이들을 사용하면 다음과 같이 정의할 수 있다. 

::: 정의 3
Category $\mathcal{C}$ 위의 *Grothendieck topology<sub>그로텐디크 위상</sub>* $\tau$란, 각 대상 $U\in \mathcal{C}$에 $U$ 위의 sieve들의 모임 $\tau(U)$을 대응시키는 것으로서, 그 원소를 *covering sieve<sub>덮개 체</sub>*라 부르며 다음 세 조건을 만족하는 것이다.

1. (Maximality) 임의의 $U$에 대하여 maximal sieve $t_U$는 $\tau(U)$에 속한다.
2. (Stability) $\mathcal{S}\in \tau(U)$이고 $g: V \rightarrow U$가 임의의 morphism이면 $g^\ast \mathcal{S}\in \tau(V)$이다.
3. (Transitivity) $\mathcal{S}\in \tau(U)$이고, $\mathcal{R}$이 $U$ 위의 sieve로서 모든 $(f: V \rightarrow U)\in \mathcal{S}$에 대하여 $f^\ast \mathcal{R}\in \tau(V)$를 만족하면 $\mathcal{R}\in \tau(U)$이다.
:::

세 조건은 위상공간의 open cover가 만족하던 성질을 정확히 추상화한 것이다. Maximality는 $U$가 그 자신을 자명하게 덮는다는 것이고, stability는 위상공간에서 $\{U_i\}$가 $U$를 덮을 때 $\{U_i\cap V\}$가 $V$를 덮는 사실에 대응한다. Transitivity는 그 이름에서 알 수 있듯, covering의 covering이 다시 covering이 된다는 것이다. 

## Covering family와 pretopology

위에서 살펴본 sieve와 Grothendieck topology의 개념은 아주 일반적인 것으로, 임의의 category에 적용할 수 있는 것이지만 대수기하학의 예시들에서 둘째 조건의 pullback sieve는 더 좋은 대상, 즉 fiber product로 나타난다. 이와 같이 fiber product가 존재하는 category에서는 sieve의 언어 없이 다음과 같이 정의할 수 있다. 

::: 정의 4
Fiber product를 가지는 category $\mathcal{C}$ 위의 *Grothendieck pretopology<sub>그로텐디크 준위상</sub>*란, 각 대상 $U$에 target이 $U$인 morphism들의 *covering family* $\{f_i: U_i \rightarrow U\}_{i\in I}$들의 모임을 대응시키는 것으로, 이 대응은 다음 세 조건을 만족한다. 

1. (Isomorphism) $f: V \rightarrow U$가 isomorphism이면 하나의 원소로 이루어진 집합 $\{f: V \rightarrow U\}$은 covering family이다.
2. (Base change) $\{f_i: U_i \rightarrow U\}$가 covering family이고 $g: V \rightarrow U$가 임의의 morphism이면, 이를 base change하여 얻은 $\{\pr_2: U_i\times_U V \rightarrow V\}$ 또한 covering family이다.
3. (Transitivity) $\{f_i: U_i \rightarrow U\}$가 covering family이고, 각 $i$마다 $\{g_{ij}: U_{ij} \rightarrow U_i\}_{j\in J_i}$가 covering family이면, 합성으로 얻어진 $\{f_i\circ g_{ij}: U_{ij} \rightarrow U\}_{i, j}$ 또한 covering family이다.
:::

Fiber product가 존재하는 category에서는 굳이 거대한 sieve 전체를 다루지 않고 이처럼 다루기 쉬운 covering family들만으로도 Grothendieck topology를 온전히 복원해낼 수 있는 충분한 정보를 담고 있다. 실제로 pretopology가 주어지면 covering family들이 생성하는 sieve를 포함하는 sieve들을 covering sieve로 선언함으로써 항상 유일한 Grothendieck topology를 얻을 수 있으며, 이를 보장하는 것이 다음의 명제이다.

::: 명제 5
$\mathcal{C}$ 위의 Grothendieck pretopology $\Cov$가 주어졌다 하자. 각 $U$에 대하여, $U$ 위의 sieve $\mathcal{S}$가 $\tau(U)$에 속함을 "어떤 covering family $\{f_i: U_i \rightarrow U\}\in \Cov(U)$가 존재하여 $\langle f_i\rangle\subseteq \mathcal{S}$인 것"으로 정의하면, $\tau$는 $\mathcal{C}$ 위의 Grothendieck topology이다.
:::
::: 증명
[정의 3](#def3)의 세 조건을 차례로 확인한다. 

1. Maximality의 경우, $\id_U: U \rightarrow U$는 isomorphism이므로 [정의 4](#def4)의 첫째 조건에 의하여 $\{\id_U\}$은 covering family이고, 그것이 생성하는 sieve는 maximal sieve $t_U$ 자신이다. 따라서 $t_U\in \tau(U)$이다. 
2. Stability의 경우, 만일 $\mathcal{S}\in \tau(U)$이면 $\langle f_i\rangle\subseteq \mathcal{S}$인 covering family $\{f_i: U_i \rightarrow U\}$가 존재한다. 임의의 $g: V \rightarrow U$에 대하여 base change 조건으로 $\{\pr_2: U_i\times_U V \rightarrow V\}$은 covering family이며, 이것이 생성하는 sieve가 $g^\ast \mathcal{S}$에 포함됨을 보이면 된다. $\pr_2: U_i\times_U V \rightarrow V$를 통해 인수분해되는 임의의 $h: W \rightarrow V$에 대하여, $g\circ h$는 $g\circ \pr_2=f_i\circ \pr_1$를 거쳐 $f_i$로 인수분해되므로 $g\circ h\in \langle f_i\rangle\subseteq \mathcal{S}$, 즉 $h\in g^\ast \mathcal{S}$이다. 따라서 $g^\ast \mathcal{S}\in \tau(V)$이다.
3. 마지막으로 transitivity를 보이기 위해 $\mathcal{S}\in \tau(U)$이고 $U$ 위의 sieve $\mathcal{R}$이 모든 $(f: V \rightarrow U)\in \mathcal{S}$에 대하여 $f^\ast \mathcal{R}\in \tau(V)$를 만족한다 하자. $\langle f_i\rangle\subseteq \mathcal{S}$인 covering family $\{f_i: U_i \rightarrow U\}$를 잡으면, 각 $f_i\in \mathcal{S}$이므로 $f_i^\ast \mathcal{R}\in \tau(U_i)$이고, 따라서 $\langle g_{ij}\rangle\subseteq f_i^\ast \mathcal{R}$인 covering family $\{g_{ij}: U_{ij} \rightarrow U_i\}$가 있다. $g_{ij}\in f_i^\ast \mathcal{R}$이라는 것은 $f_i\circ g_{ij}\in \mathcal{R}$이라는 뜻이므로, transitivity 조건으로 얻은 covering family $\{f_i\circ g_{ij}: U_{ij} \rightarrow U\}$의 모든 원소가 $\mathcal{R}$에 속한다. 그것이 생성하는 sieve가 $\mathcal{R}$에 포함되므로 $\mathcal{R}\in \tau(U)$이다.
:::

즉, covering family가 주어지면 이것을 <em-ko>포함하는</em-ko> covering sieve를 만들 수 있으며, 이를 통해 두 가지 개념 사이를 자유롭게 이동할 수 있다. 다소 주의할 것은 당연하게도 서로 다른 두 Grothendieck pretopology가 같은 Grothendieck topology를 생성할 수 있다는 것으로, 가령 한 affine scheme의 모든 principal open으로 이루어진 covering과 모든 finite affine open cover는 같은 Zariski topology를 준다.

::: 정의 6
Category $\mathcal{C}$와 그 위의 Grothendieck topology $\tau$의 쌍 $(\mathcal{C}, \tau)$을 *site<sub>사이트</sub>*라 부른다. 
:::

만일 category $\mathcal{C}$가 fiber product를 가지고, 그 위에 Grothendieck pretopology가 주어진다면 이 정보는 $\mathcal{C}$ 위에 유일한 방식으로 Grothendieck topology을 정의하므로, 이와 같은 경우에도 이 데이터를 site라 부른다. 언제나와 같이 이를 엄밀하게 적기 위해서는 sheaf의 값을 이루는 곱과 limit이 잘 존재하도록 $\mathcal{C}$가 small category라는 가정 등, 적절한 집합론적 크기 조건을 만족할 것을 요구하지만, 이 글에서는 이러한 문제를 다루지 않고 필요한 곱과 limit이 존재한다고 전제한다. 

## Site의 예시

Site의 개념은 갑자기 생겨난 것은 아니며, 우리가 이미 알고 있는 대상들을 포함하는 개념들이다. 가장 기본이 되는 예시는 위상공간의 open set들이 이루는 site이다.

::: 예시 7 (위상공간)
위상공간 $X$와 $X$의 open set들의 category $\Open(X)$를 생각하면, 이 category는 교집합이 fiber product의 universal property를 만족하는 것을 쉽게 확인할 수 있다. 따라서 각 open set $U$ 위의 covering family를 $U$의 통상적인 open cover, 즉 $\bigcup U_i=U$를 만족하는 open set들의 inclusion $\{U_i\hookrightarrow U\}$으로 정의하면 이것이 pretopology를 이룬다. 이 예시에서 [정의 4](#def4)의 세 조건이 번역되는 방식을 살펴보면 이들 각 조건의 의미를 더 쉽게 이해할 수 있는데, 첫째 조건은 $U$ 자신이 $U$를 덮는다는 조건이며, base change 조건은 $\{U_i\}$가 $U$의 covering이고 $V$가 $U$의 open subset이라면 $\{U_i\cap V\}$는 $V$의 covering임을 의미한다. 마지막 transitivity는 앞서 설명했듯 covering의 covering이 다시 covering이 된다는 의미이다. 
:::

그러나 역시 우리에게 흥미로운 예시는 다음의 scheme 위의 위상들이다. 논의의 편의를 위해, 공통의 공역을 갖는 morphism들의 family $\{f_i: U_i \rightarrow U\}$가 $\bigcup f_i(U_i)=U$를 만족한다면 이들을 *jointly surjective*라 부르자. 

::: 예시 8 (대수기하학)
우리는 이미 descent를 다루며 scheme 위에 정의된 여러가지 covering을 다루었다. 이 예시에서는 이들이 정의하는 site를 살펴본다. Scheme $X$를 고정하자.

1. 우선 scheme $X$ 위에 정의된 *small Zariski site* $X_\Zar$는 그 대상이 $X$의 open subscheme들이고, morphism이 open embedding으로 주어졌으며 covering family가 일반적인 open cover로 주어진 site이다. 어차피 $X$의 위상구조 자체가 Zariski topology로 주어진 것이므로, 이는 본질적으로 [예시 7](#ex7)의 특수한 경우이다. 다음 예시들을 위해 이를 더 형식적인 언어로 바꾸면, $X_\Zar$는 target이 $X$인 open embedding을 대상으로 갖는 category이며, 임의의 대상 $U\rightarrow X$에 대하여, $U$의 covering family는 jointly surjective이며 open embedding인 $X$-morphism들의 family $\{U_i\rightarrow U\}$이다. 한편 우리는 *big Zariski site* $(\Sch_{/X})_{\Zar}$ 또한 정의할 수 있다. 이는 $X_\Zar$의 대상만 <em-ko>임의의</em-ko> $U\rightarrow X$로 바꾼 것으로, 여전히 고정된 $U$의 covering family들은 jointly surjective이며 open embedding인 $X$-morphism들의 family $\{U_i\rightarrow U\}$이다.
2. 위와 비슷하게 *small étale site* $X_\et$를 정의한다. 즉 $X_\et$는 target이 $X$인 étale morphism들을 대상으로 갖는 category이며, 각각의 $U$에 대한 covering family들은 jointly surjective이며 étale인 $X$-morphism들의 family $\{U_i\rightarrow U\}$이다. *Big étale site* 또한 비슷하게 정의되는 것으로, small étale site의 정의에서 각 대상들만 target을 $X$로 갖는 étale morphism들 대신 target을 $X$로 갖는 임의의 morphism들 (즉 임의의 $X$-scheme들)로 바꾼 것이다. 
3. 비슷하게 fppf site와 fpqc site를 정의할 수 있으나, 다소 주의할 것은 small site의 경우 기대대로 작동하지는 않는다는 것이다. 이는 본질적으로 $U, V$가 모두 $X$ 위에서 flat하더라도 $U\rightarrow W$가 flat일 필요는 없어서 fiber product $U\times_WV$ 등이 $X$ 위에서 flat이 아닐 수 있게 되어, 언어가 깔끔하게 떨어지지 않기 때문이다. 다행히 우리가 관심을 가질 대상들은 big site들로, 여기서는 어차피 이러한 걱정을 하게 될 필요가 없으므로 별 문제가 일어나지 않는다. 따라서 고정된 $X$에 대하여, $X$의 (big) *fppf site* $(\Sch_{/X})_\fppf$는 대상이 $X$-scheme들이며, 각각의 $U$에 대한 covering family들은 jointly surjective이며 fppf인 $X$-morphism들의 family $\{U_i\rightarrow U\}$이다. 
4. $X$의 (big) *fpqc site* $(\Sch_{/X})_\fpqc$의 경우, 마찬가지로 big fpqc site만 본다는 것은 동일하지만 covering family의 조건을 쓸 때 주의해야 한다. 이는 fppf morphism과 다르게 fpqc covering의 경우 [\[스킴\] §충실평탄하강, ⁋정의 9](/ko/math/scheme_theory/faithfully_flat_descent#def9)에서 보았듯, quasi-compact 조건이 morphism들 각각에 걸리는 것이 아니라 family 자체에 걸리는 것이기 때문이다. 즉 

Fppf의 경우 flat하고 locally of finite presentation인 morphism이 open이므로 joint surjectivity만으로 충분하지만, fpqc에서는 finite presentation 조건을 버리므로 jointly surjective인 flat morphism들의 family라는 것만으로는 충분하지 않다. 대신 각 $f_i: U_i\rightarrow U$가 flat이고, 임의의 affine open $V\subseteq U$에 대하여 유한히 많은 affine open $W_j\subseteq U_{i_j}$를 골라 $V=\bigcup_j f_{i_j}(W_j)$로 쓸 수 있을 것을 요구한다. 즉 fpqc의 quasi-compact 조건은 각 morphism에 따로 부과되는 것이 아니라 covering family 전체에 이 affine-local한 형태로 부과된다.
:::

이제 이러한 site 위에서 정의되는 presheaf와 sheaf의 개념을 다룬다.

## Site 위의 presheaf와 sheaf

Site 위의 presheaf는 underlying category 위의 contravariant functor에 다름 아니다. 위상공간의 경우 presheaf가 $\Open(X)^\op \rightarrow \Set$ 꼴의 functor였던 것을 임의의 underlying category로 일반화한 것이다.

::: 정의 9
Site $(\mathcal{C}, \tau)$ 위의 *presheaf*란 contravariant functor $F:\mathcal{C}^\op \rightarrow \Set$이며, presheaf morphism은 natural transformation이다. 이들이 이루는 functor category를 $\PSh(\mathcal{C})$로 적는다. $U$ 위의 covering sieve $\mathcal{S}\in \tau(U)$에 대하여, $F$의 $\mathcal{S}$ 위의 *matching family<sub>정합족</sub>*란, 각 $(f: V \rightarrow U)\in \mathcal{S}$마다 원소 $x_f\in F(V)$를 지정하되 임의의 $g: W \rightarrow V$에 대하여

$$F(g)(x_f)=x_{f\circ g}$$

를 만족하는 족 $(x_f)_{f\in S}$이다. 원소 $x\in F(U)$가 이 matching family의 *amalgamation<sub>접합</sub>*이라는 것은 모든 $(f: V \rightarrow U)\in S$에 대하여 $F(f)(x)=x_f$인 것이다. 이제 presheaf $F$가

1. *separated presheaf<sub>분리 준층</sub>*라는 것은 임의의 covering sieve 위의 matching family가 많아야 하나의 amalgamation을 가지는 것이고,
2. *sheaf<sub>층</sub>*라는 것은 임의의 covering sieve 위의 matching family가 정확히 하나의 amalgamation을 가지는 것이다.

Sheaf들이 이루는 $\PSh(\mathcal{C})$의 full subcategory를 $\Sh(\mathcal{C}; \tau)$로 적는다.
:::

Matching family는 covering sieve의 각 마디 위에 정합적으로 주어진 국소 자료이고, amalgamation은 그것을 $U$ 전체로 붙인 대역 자료이다. Separated 조건은 붙인 결과가 유일함을, sheaf 조건은 그것이 항상 존재함을 추가한다. 이 sieve 형태의 정의는 임의의 위상에 대해 작동하지만, 위상이 pretopology로 주어진 경우 matching family는 covering family 위의 자료로 다시 쓸 수 있고, sheaf 조건은 익숙한 equalizer 형태가 된다.

::: 명제 10
위상 $\tau$가 pretopology $\Cov$로 [명제 5](#prop5)와 같이 주어졌다 하자. Presheaf $F:\mathcal{C}^\op \rightarrow \Set$가 sheaf인 것은, 모든 covering family $\{f_i: U_i \rightarrow U\}\in \Cov(U)$에 대하여 다음 diagram

$$F(U) \xrightarrow{\ e\ } \prod_i F(U_i) \underset{q}{\overset{p}{\rightrightarrows}} \prod_{i, j} F(U_i\times_U U_j)$$

이 equalizer인 것과 동치이다. 여기에서 $e(x)=(F(f_i)(x))_i$이고, 두 morphism $p, q$는 각각 두 projection $\pr_1: U_i\times_U U_j \rightarrow U_i$와 $\pr_2: U_i\times_U U_j \rightarrow U_j$를 따른 restriction $p((s_i)_i)=(F(\pr_1)(s_i))_{i, j}$, $q((s_i)_i)=(F(\pr_2)(s_j))_{i, j}$이다. $F$가 separated인 것은 같은 diagram에서 $e$가 단사인 것과 동치이다.
:::
::: 증명
Generating covering sieve $S=\langle f_i\rangle$ 위의 matching family와 위 equalizer의 자료가 일대일로 대응함을 보이면 충분하다.

$S$ 위의 matching family $(x_f)_{f\in S}$가 주어지면, 특히 각 $f_i\in S$에 대한 $s_i=x_{f_i}\in F(U_i)$들의 족 $(s_i)\in \prod_i F(U_i)$을 얻는다. 두 projection $\pr_1: U_i\times_U U_j \rightarrow U_i$와 $\pr_2: U_i\times_U U_j \rightarrow U_j$에 각각 $f_i$와 $f_j$를 합성한 $f_i\circ \pr_1=f_j\circ \pr_2$은 같은 morphism이고 $S$에 속하므로, matching 조건을 $g=\pr_1$과 $g=\pr_2$에 각각 적용하면

$$F(\pr_1)(s_i)=x_{f_i\circ \pr_1}=x_{f_j\circ \pr_2}=F(\pr_2)(s_j)$$

이므로 $p((s_i))=q((s_i))$, 즉 $(s_i)$는 $p, q$의 equalizer에 속한다.

역으로 $p((s_i))=q((s_i))$인 $(s_i)\in \prod_i F(U_i)$이 주어지면, $S$ 위의 matching family를 다음과 같이 정의한다. $f\in S$이면 $f=f_i\circ g$인 $i$와 $g: V \rightarrow U_i$가 있으므로 $x_f=F(g)(s_i)$로 둔다. 이것이 well-defined임, 즉 $f=f_i\circ g=f_j\circ g'$인 두 인수분해에서 같은 값을 줌은 $(g, g'): V \rightarrow U_i\times_U U_j$로 묶은 뒤 $p((s_i))=q((s_i))$의 $(i, j)$-성분을 $F(g, g')$로 당겨 $F(g)(s_i)=F(g')(s_j)$를 얻음으로써 확인된다. 이 대응이 matching family 조건을 만족함과, 두 구성이 서로 역임은 정의로부터 직접 따른다.

따라서 amalgamation $x\in F(U)$의 존재·유일성은 정확히 $e$가 equalizer로의 전단사임과 같다. Sheaf 조건은 amalgamation의 존재와 유일성이므로 $e$가 equalizer 위로의 전단사, 즉 위 diagram이 equalizer인 것과 동치이고, separated 조건은 유일성뿐이므로 $e$가 단사인 것과 동치이다.

마지막으로 $\tau(U)$의 covering sieve $\mathcal{S}'$은 generating covering sieve $\langle f_i\rangle$을 포함할 뿐 그와 같을 필요는 없으므로, $\mathcal{S}'$ 위의 matching family를 $\langle f_i\rangle$로 제한하여 얻은 $x$가 $\mathcal{S}'$ 전체의 amalgamation임을 확인해야 한다. 임의의 $(f: V \rightarrow U)\in \mathcal{S}'$에 대하여 base change한 covering family $\{\pr_2: U_i\times_U V \rightarrow V\}$을 잡으면 $f\circ \pr_2=f_i\circ \pr_1\in \langle f_i\rangle$이므로 $F(\pr_2)(F(f)(x))=x_{f\circ \pr_2}=F(\pr_2)(x_f)$이고, 이 covering family에 대한 $e$의 단사성으로 $F(f)(x)=x_f$를 얻는다.
:::

[명제 10](#prop10)은 site 위의 sheaf 조건이 위상공간 위의 그것과 형식적으로 동일함을 보여준다. ([\[위상수학\] §층, ⁋정의 1](/ko/math/topology/sheaves#def1)) 다만 두 겹 겹침이 교집합 $U_i\cap U_j$ 대신 fiber product $U_i\times_U U_j$로 바뀐다. 위상공간에서는 covering의 morphism이 모두 monomorphism이어서 $U_i\times_U U_i=U_i$이지만, étale이나 fpqc covering에서는 $U_i\times_U U_i$이 $U_i$보다 클 수 있고, 바로 이 차이가 비단사 covering 위의 descent를 가능하게 한다. 특히 단일 morphism으로 이루어진 fpqc covering $\{\Spec B \rightarrow \Spec A\}$에 대해서는 이 equalizer가 faithfully flat descent의 Amitsur exact sequence로 환원되는데, 이는 아래에서 다시 다룬다.

이제 presheaf가 sheaf가 아닌 전형적인 예를 보고, 이를 통해 sheafification의 필요를 동기화한다.

::: 예시 11 (sheaf가 아닌 separated presheaf)
$X$가 공집합이 아닌 두 connected open subset들의 disjoint union $X=U_1\sqcup U_2$인 위상공간이라 하고, 원소가 둘 이상인 집합 $A$에 대하여 상수 presheaf $\underline{A}^{\mathrm{pre}}$를 $V\neq\emptyset$에는 $\underline{A}^{\mathrm{pre}}(V)=A$로, $\underline{A}^{\mathrm{pre}}(\emptyset)=\{\ast\}$로 두고, 공집합이 아닌 open subset 사이의 restriction을 identity로 정의하자. Covering $\{U_1, U_2\}$를 생각하면 $U_1\cap U_2=\emptyset$이고 [명제 10](#prop10)의 equalizer에서 겹침을 담는 항이 $\underline{A}^{\mathrm{pre}}(\emptyset)=\{\ast\}$이므로 겹침 조건이 공허하고, 따라서 서로 다른 $a_1, a_2\in A$를 각각 $U_1, U_2$ 위의 자료로 택한 것이 matching family를 이룬다. 그러나 이를 붙인 $X$ 위의 원소는 $\underline{A}^{\mathrm{pre}}(X)=A$의 한 원소여야 하는데 그것이 $U_1$과 $U_2$ 위에서 동시에 $a_1, a_2$로 restrict될 수는 없으므로 amalgamation이 존재하지 않는다. 한편 두 원소가 모든 $U_i$ 위에서 일치하면 같으므로 이 presheaf는 separated이다. 그 sheafification은 locally constant function들의 sheaf $\underline{A}$로, $\underline{A}(X)=A\times A$이다.
:::

[예시 11](#ex11)은 separated와 sheaf의 차이를 분명히 보여준다. 자료를 비정합적으로 붙이려는 시도가 실패하는 것이 아니라, 정합적인 국소 자료조차 붙일 대역 자료가 presheaf 안에 없는 것이다. Sheafification은 이러한 결손을 보편적인 방식으로 보충하여 presheaf에 가장 가까운 sheaf를 부여하는 조작이며, site 위에서는 plus construction으로 구성된다.

## Sheafification과 plus construction

위상공간 위에서 우리는 sheafification을 forgetful functor의 left adjoint로 특징지었고, 그 존재를 compatible germ들의 sheaf로 직접 구성하였다. ([\[위상수학\] §층, ⁋정의 5](/ko/math/topology/sheaves#def5)) 일반적인 site에는 점이나 stalk이 없으므로 germ을 이용한 구성은 불가능하고, 대신 모든 covering에 걸친 colimit을 취하는 plus construction을 사용한다.

::: 정의 12
Presheaf $F:\mathcal{C}^\op \rightarrow \Set$와 대상 $U$에 대하여, $U$ 위의 covering sieve들의 모임을 역포함 $\mathcal{S}'\subseteq \mathcal{S}\Rightarrow \mathcal{S}\preceq \mathcal{S}'$으로 순서지으면, stability와 transitivity에 의해 이는 filtered preorder를 이룬다. 각 covering sieve $\mathcal{S}$에 $\mathcal{S}$ 위의 matching family들의 집합 $\operatorname{Match}(\mathcal{S}, F)$을 대응시키고, 세분 $\mathcal{S}\preceq \mathcal{S}'$에 matching family의 restriction을 대응시키면 filtered diagram을 얻으며, 그 colimit

$$F^+(U)=\varinjlim_{\mathcal{S}\in \tau(U)}\operatorname{Match}(\mathcal{S}, F)$$

을 $F$의 *plus construction<sub>plus 구성</sub>*이라 부른다. $U\mapsto F^+(U)$은 presheaf를 이루며, maximal sieve 위의 matching family가 $F(U)$의 원소와 같으므로 자연스러운 morphism $F \rightarrow F^+$이 있다.
:::

직관적으로 $F^+(U)$의 원소는 어떤 covering 위에서 정합적으로 주어진 국소 자료를, 더 미세한 covering으로 옮겨도 같아지는 것들끼리 동일시한 것이다. 두 matching family가 공통의 세분 위에서 일치하면 같은 원소로 본다는 것이 colimit의 의미이며, 이로써 amalgamation의 유일성 결손이 교정된다. Pretopology의 언어로는 $F^+(U)$이 covering $\{U_i \rightarrow U\}$들에 걸친 Čech 영차 cohomology

$$\check{H}^0(\{U_i \rightarrow U\}, F)=\operatorname{eq}\Big(\prod_i F(U_i)\rightrightarrows \prod_{i, j}F(U_i\times_U U_j)\Big)$$

의 filtered colimit이다. 다음 정리가 이 구성의 핵심 성질이다.

::: 정리 13
임의의 presheaf $F$에 대하여 다음이 성립한다.

1. $F^+$은 separated presheaf이다.
2. $F$가 separated이면 $F^+$은 sheaf이다. 따라서 $F^{++}=(F^+)^+$은 항상 sheaf이다.
3. 대응 $a(F)=F^{++}$은 forgetful functor $\iota:\Sh(\mathcal{C}; \tau)\hookrightarrow \PSh(\mathcal{C})$의 left adjoint이며, 자연스러운 morphism $F \rightarrow F^{++}$이 그 unit이다. 즉 임의의 sheaf $G$에 대하여

$$\Hom_{\Sh}(F^{++}, G)\cong \Hom_{\PSh}(F, G)$$

이 성립한다. 나아가 $a$는 finite limit을 보존한다.
:::

이 정리는 plus construction의 표준 성질로 받아들이며, 자세한 증명은 [Stacks]나 [MM]을 참조한다.

[정리 13](#thm13)는 [\[위상수학\] §층, ⁋정의 5](/ko/math/topology/sheaves#def5)에서 다룬 sheafification adjunction을 임의의 site로 확장한다. Left adjoint $a$가 finite limit을 보존한다는 사실은 특히 중요한데, 이로부터 sheaf category가 위상공간의 sheaf category와 같은 종류의 좋은 구조를 가짐이 따라온다.

Site $(\mathcal{C}, \tau)$ 위의 sheaf category $\Sh(\mathcal{C}; \tau)$를 *Grothendieck topos<sub>그로텐디크 토포스</sub>*라 부른다. 이는 작은 site 위의 sheaf category와 동치인 category로 정의되며, 모든 작은 limit과 colimit을 가지고, cartesian closed이며, subobject classifier를 가지는 등 집합들의 category $\Set$이 누리는 대부분의 형식적 성질을 공유한다. $\Set$ 자신은 한원소 위상공간 위의 sheaf category로서 가장 단순한 topos이다. Topos 이론은 그 자체로 방대한 주제이므로 여기에서는 정의를 언급하는 데 그치고, 이후 stack의 맥락에서 필요한 만큼만 다룬다.

## Subcanonical 위상과 representable presheaf

Site 위의 sheaf 이론이 scheme 이론과 만나는 결정적인 지점은, underlying category의 대상이 정의하는 representable presheaf가 그 위상에 대해 sheaf인가 하는 물음이다. 이것이 성립하면 대상 $X$를 그 functor of points $h_X$와 동일시하여 sheaf category 안의 한 대상으로 다룰 수 있고, scheme의 functorial 정의가 sheaf의 언어로 정당화된다. ([\[범주론\] §표현가능한 함자, ⁋정의 1](/ko/math/category_theory/representable_functors#def1))

::: 정의 14
Site $(\mathcal{C}, \tau)$가 *subcanonical<sub>준표준</sub>*이라는 것은, 모든 대상 $X\in \mathcal{C}$에 대하여 representable presheaf $h_X=\Hom_\mathcal{C}(-, X)$이 $\tau$-sheaf인 것이다. Subcanonical 위상들 가운데 가장 미세한 것이 존재하며 이를 *canonical topology<sub>표준 위상</sub>*라 부른다. 즉 어떤 위상이 subcanonical인 것은 그것이 canonical topology보다 거칠거나 같은 것이다.
:::

Subcanonical 조건은 [명제 10](#prop10)를 통해 구체적으로 진술된다. $h_X$가 sheaf라는 것은, 각 covering family $\{U_i \rightarrow U\}$에 대하여 $U$에서 $X$로 가는 morphism이 그 covering 위에서 정합적으로 주어진 morphism들로부터 유일하게 붙는다는 것, 즉

$$\Hom(U, X) \rightarrow \prod_i \Hom(U_i, X)\rightrightarrows \prod_{i, j}\Hom(U_i\times_U U_j, X)$$

이 equalizer라는 것이다. 이는 morphism의 descent 조건에 다름 아니다. Zariski나 étale 위상에서 이것이 성립함은 morphism이 covering 위에서 국소적으로 정해진다는 익숙한 사실이지만, fpqc처럼 거친 covering에 대해서는 결코 자명하지 않으며, 그 성립은 faithfully flat descent의 한 형태이다.

::: 정리 15
$\Sch$ (혹은 $\Sch_{/S}$) 위의 fpqc 위상은 subcanonical이다. 즉 임의의 scheme $X$에 대하여 functor of points $h_X=\Hom_{\Sch}(-, X)$은 fpqc sheaf이다. 따라서 Zariski·étale·fppf 위상에서도 모든 representable presheaf는 sheaf이다.
:::
::: 증명
[명제 10](#prop10)에 의하여, fpqc covering $\{U_i \rightarrow U\}$에 대한 equalizer 조건을 확인하면 된다. Representable presheaf는 Zariski sheaf이고, 모든 fpqc covering은 $U$의 affine open 위에서 단일 faithfully flat affine covering으로 세분할 수 있다. 따라서 $U=\Spec A$이고 covering이 $\pi:\Spec B \rightarrow \Spec A$인 경우로 환원된다. 이 때 $\Spec B\times_{\Spec A}\Spec B=\Spec(B\otimes_A B)$이므로, 보여야 할 것은

$$\Hom(\Spec A, X) \rightarrow \Hom(\Spec B, X)\rightrightarrows \Hom(\Spec(B\otimes_A B), X)$$

이 equalizer라는 것이다.

먼저 $X=\Spec R$이 affine인 경우, 이 diagram은 ring homomorphism의 diagram

$$\Hom_{\Ring}(R, A) \rightarrow \Hom_{\Ring}(R, B)\rightrightarrows \Hom_{\Ring}(R, B\otimes_A B)$$

이다. Faithful flatness로 sequence $0 \rightarrow A \rightarrow B \rightrightarrows B\otimes_A B$가 exact이므로 ([\[스킴\] §충실평탄하강, ⁋보조정리 3](/ko/math/scheme_theory/faithfully_flat_descent#lem3)), 즉 $A$가 $d^0, d^1: B \rightrightarrows B\otimes_A B$의 equalizer이므로, $\Hom_{\Ring}(R, -)$을 적용하면 $\varphi: R \rightarrow B$가 $d^0\circ \varphi=d^1\circ \varphi$를 만족하는 것과 $\varphi$가 유일하게 $R \rightarrow A$를 거쳐 인수분해되는 것이 동치임을 얻는다. 이것이 곧 위 equalizer이다. 이는 structure sheaf $\mathcal{O}$이 fpqc sheaf임을 보이는 [\[스킴\] §충실평탄하강, ⁋정리 10](/ko/math/scheme_theory/faithfully_flat_descent#thm10)의 descent 논증과 평행한 논증으로, $\Hom_{\Ring}(R, -)$이 같은 Amitsur equalizer를 보존한다는 데에서 따른다.

일반적인 $X$에 대하여, morphism $g:\Spec B\rightarrow X$가 두 projection $\pr_1,\pr_2:\Spec(B\otimes_A B)\rightrightarrows\Spec B$에 대해 $g\circ\pr_1=g\circ\pr_2$를 만족한다고 하자. Faithfully flat morphism $\pi$는 universally submersive이므로, $g$의 underlying continuous map은 유일한 continuous map $h:\Spec A\rightarrow X$로 내려온다. 각 $p\in\Spec A$에 대하여 $h(p)$를 포함하는 affine open $W=\Spec R\subseteq X$를 택하고 $p\in D(a)\subseteq h^{-1}(W)$인 principal open을 잡자. $\pi^{-1}(D(a))=\Spec B_a$ 위에서 $g$는 ring homomorphism $R\rightarrow B_a$를 주고, cocycle 조건에 의하여 그 image는 $B_a\rightrightarrows B_a\otimes_{A_a}B_a$의 equalizer $A_a$에 속한다. 따라서 $g$는 $D(a)$ 위에서 유일한 morphism $D(a)\rightarrow W\rightarrow X$로 내려오며, 이 local morphism들은 같은 affine equalizer 논증으로 overlap에서 일치하므로 유일한 morphism $\Spec A\rightarrow X$로 붙는다. 따라서 $h_X$은 fpqc sheaf이다. Fpqc보다 거친 위상의 covering은 fpqc covering이므로 이들에 대해서도 sheaf 조건이 따라온다.
:::

[정리 15](#thm15)가 stack 이론으로 가는 길을 연다. Scheme $X$를 그 functor of points $h_X:\Sch^\op \rightarrow \Set$과 동일시하면 ([\[범주론\] §표현가능한 함자, ⁋정리 4](/ko/math/category_theory/representable_functors#thm4)), scheme은 fpqc site $\Sch$ 위의 sheaf 가운데 특별한 것, 즉 적절한 representability 조건을 만족하는 sheaf로 자리매김한다. Functorially 정의된 moduli 문제 $F:\Sch^\op \rightarrow \Set$이 scheme을 표현하는지를 묻는 일은, 먼저 $F$가 fpqc sheaf인지를 확인하고 ([\[스킴\] §충실평탄하강, ⁋정리 10](/ko/math/scheme_theory/faithfully_flat_descent#thm10)의 descent 논증과 같은 방식으로) 이어 그것이 국소적으로 representable한지를 보는 두 단계로 나뉜다. Stack은 이 그림에서 sheaf의 값을 집합 대신 groupoid로 확장하여, 점들이 비자명한 automorphism을 가지는 moduli 문제까지 포착하는 일반화이다. 그 정의와 전개는 이후의 글로 미룬다.

## $\mathbb{G}_a$의 sheaf 성질

마지막으로 [정리 15](#thm15)의 특수한 경우에서 Amitsur exact sequence가 sheaf 조건으로 번역되는 과정을 확인한다.

::: 예시 16 ($\mathbb{G}_a$는 fpqc sheaf)
$\mathbb{G}_a=\Spec \mathbb{Z}[\x]=\mathbb{A}^1$의 functor of points은 각 scheme $T$에 global section들의 additive group

$$\mathbb{G}_a(T)=\Hom_{\Sch}(T, \mathbb{A}^1)=\Gamma(T, \mathcal{O}_T)$$

을 대응시킨다. ([\[스킴\] §점함자, ⁋명제 1](/ko/math/scheme_theory/functor_of_points#prop1)) 단일 fpqc covering $\{\Spec B \rightarrow \Spec A\}$에 대한 sheaf 조건은

$$A \rightarrow B \rightrightarrows B\otimes_A B$$

이 equalizer라는 것이다. 두 morphism은 $b\mapsto b\otimes 1$과 $b\mapsto 1\otimes b$이며, faithful flatness로 $0 \rightarrow A \rightarrow B \xrightarrow{d^1-d^0} B\otimes_A B$가 exact이다. ([\[스킴\] §충실평탄하강, ⁋보조정리 3](/ko/math/scheme_theory/faithfully_flat_descent#lem3)) 따라서 $A=\{b\in B\mid b\otimes 1=1\otimes b\}$이고, $\mathbb{G}_a(\Spec A)=A$는 covering 위의 matching family로부터 복원된다.
:::

---

**참고문헌**

**[Vis]** A. Vistoli, *Notes on Grothendieck topologies, fibered categories and descent theory*. In *Fundamental algebraic geometry: Grothendieck's FGA explained*, Mathematical Surveys and Monographs, American Mathematical Society, 2005.  
**[Stacks]** The Stacks Project Authors, *The Stacks Project*. Available [online](https://stacks.math.columbia.edu/).  
**[SGA4]** M. Artin, A. Grothendieck, J.-L. Verdier, *Théorie des topos et cohomologie étale des schémas (SGA 4)*. Lecture Notes in Mathematics 269, 270, 305, Springer, 1972–1973.  
**[MM]** S. Mac Lane, I. Moerdijk, *Sheaves in geometry and logic: A first introduction to topos theory*. Universitext, Springer, 1994.
