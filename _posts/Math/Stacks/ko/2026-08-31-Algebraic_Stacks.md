---
title: "Algebraic stack과 quotient stack"
description: "대각선의 표현가능성과 매끄러운 atlas로 algebraic stack(Artin·Deligne–Mumford)을 정의하고, 군작용의 quotient stack [X/G]와 BG=[pt/G]를 구성하여 그 기하적 의미를 다룬다."
excerpt: "Algebraic (Artin / Deligne–Mumford) stacks via atlases, and the quotient stack [X/G]"

categories: [Math / Stacks]
permalink: /ko/math/stacks/algebraic_stacks
sidebar: 
    nav: "stacks-ko"

date: 2026-08-31
weight: 3

published: false

---

앞선 글에서 우리는 기존에 생각하던 naive한 moduli problem을 $\Grpd$-valued functor로 만들어서, 각 대상 $T$ 위에 $T$-family들과 그들 사이의 isomorphism으로 이루어진 groupoid $\mathcal{X}(T)$를 대응시켰다. 기존 (점함자)와 마찬가지로 우리는 이를 $\mathcal{X}$의 $T$-point들의 모임으로 생각할 것이지만, 우선 해결해야 할 문제들이 몇 가지 있었는데, 그 중 하나는 morphism $u: T'\rightarrow T$에 대한 pullback이 unique isomorphism까지만 정해지므로, 실제 pullback functor $u^\ast: \mathcal{X}(T)\rightarrow \mathcal{X}(T')$를 써 주기 위해서는 각각의 pullback의 representative를 고르는 선택, 즉 cleavage가 필요했다는 것이다. 때문에 합성가능한 morphism $T''\overset{v}{\rightarrow}T'\overset{u}{\rightarrow}T$에 대하여, pullback을 하는 두 경로가 다를 수 있었고 이를 해결하기 위해 우리는 canonical isomorphism

$$v^\ast u^\ast x\xrightarrow{\sim}(u\circ v)^\ast x$$

그리고 이들이 만족해야 할 coherence condition들을 추가적인 정보로 기억했어야 했으며 그렇게 얻어진 대상이 *pseudofunctor* $\mathcal{X}:\mathcal{C}^\op\rightarrow\Grpd$였다. ([§스택, ⁋정의 3](/ko/math/stacks/fibered_categories_and_stacks#def3)) 개념적으로 이 pseudofunctor들은 모든 $T$-point들 $\mathcal{X}(T)$들과, 위에서 추가한 별도 정보들에 의해 결정되어야 하는 것이므로, $T\in \mathcal{C}$마다 위의 pseudofunctor가 주는 $\mathcal{X}(T)\in \Grpd$의 정보 (그리고 auxiliary data)를 모두 알고 있다면 이것이 담고 싶은 정보를 모두 담은 것이라 할 수 있으며 이러한 관점에서 우리는 CFG $\mathcal{F}\rightarrow \mathcal{C}$를 정의했다. ([§스택, ⁋정의 5](/ko/math/stacks/fibered_categories_and_stacks#def5)) 이 두 관점 사이를 이동하는 것을 정당화해주는 것은 [§스택, ⁋정리 8](/ko/math/stacks/fibered_categories_and_stacks#thm8)로, 해당 결과에서 우리는 pseudofunctor들과 CFG들은 각각 $2$-category를 이루며, 실제로 우리는 이 두 $2$-category가 $2$-equivalent하다는 것을 보였다.

그럼 이제 stack은 원래 category $\mathcal{C}$에 위상구조를 부여하여 site로 만들고, 그 위상구조가 정의하는 descent, 정확하게는 $2$-category 의미에서의 descent를 통해 붙는 대상이다. 즉 stack을 정의하기 위해서는 covering을 따라 morphism들을 유일하게 붙이고, compatible한 local object들을 붙이는 과정이 필요하며, 이러한 관점에서 stack은 site 위의 $\Grpd$-valued (2-categorical) sheaf라 정의할 수 있었다. ([§스택, ⁋정의 12](/ko/math/stacks/fibered_categories_and_stacks#def12))

이러한 관점에서, stack의 morphism $f:\mathcal{X}\rightarrow\mathcal{Y}$은 pseudofunctor 사이의 pseudonatural transformation이다. 이는 각 $T$마다 functor $f_T:\mathcal{X}(T)\rightarrow\mathcal{Y}(T)$를 주고, 각 $u:T'\rightarrow T$마다 natural isomorphism

$$f_{T'}(u^\ast x)\xrightarrow{\sim}u^\ast f_T(x)$$

을 주어 pullback과 호환되게 하는 자료이다. 두 stack morphism 사이의 2-morphism은 이 functor들을 잇고 pullback coherence와 호환되는 natural transformation이다. CFG의 언어에서는 각각 base 위의 functor와 natural transformation으로 표현된다. ([§스택, ⁋정의 7](/ko/math/stacks/fibered_categories_and_stacks#def7))

Stack의 descent 조건은 local data를 global 대상으로 붙일 수 있음을 보장하지만, scheme이나 algebraic space와 같은 local model을 주지는 않는다. 따라서 dimension, tangent space, smoothness 등의 개념을 아직 익숙한 대수기하의 언어로 논할 수 없다. 이번 글의 목표는 stack 가운데 이러한 기하를 갖는 algebraic stack을 가려내는 것이다.

## Stack의 올곱

Stack의 기하를 논하기 위해 가장 먼저 필요한 것은 fiber product이다. Scheme에서도 base change에 대해 잘 행동하는 성질들을 좋은 기하학적 성질로 보았듯, stack 사이의 morphism에 대해서도 base change를 정의해야 한다. 문제는 $\Sch$ 혹은 $\Sch_{/S}$와는 달리, $\Stk$은 $2$-category이므로 이 위에서의 fiber product 또한 $2$-fiber product로 정의해야 한다는 것이다. 

이를 위해 어떠한 데이터가 필요한지 살펴보자. 두 stack morphism $f: \mathcal{X}\rightarrow \mathcal{Z}$와 $g:\mathcal{Y}\rightarrow \mathcal{Z}$에 대하여, [\[스킴\] §점함자, ⁋명제 7](/ko/math/scheme_theory/functor_of_points#prop7)을 생각하면 stack morphism의 fiber product를 정의하기 위해서는 각 $T$마다 fiber product

$$\mathcal{X}(T)\times_{\mathcal{Z}(T)}\mathcal{Y}(T)$$

를 정의하고 이를 descent로 붙이면 된다. Scheme에서의 fiber product를 정의할 때는 $X(T)\times_{Z(T)}Y(T)$를, <em-ko>집합</em-ko> $Z(T)$ 안에서 $f_T(x)=g_T(y)$를 만족하는 원소들로 잡았으나, 이제 $\mathcal{Z}(T)$가 groupoid인 이상 이 조건을 isomorphism으로 내려야 한다. 이는 [§스택, ⁋명제 6](/ko/math/stacks/fibered_categories_and_stacks#prop6) 직후에 살펴본 상황과 정확히 동일한 상황으로, 점 $x\in \mathcal{X}(T)$를 groupoid 사이의 functor $x:\ast\rightarrow \mathcal{X}(T)$로 본다면 $f_T(x)$와 $g_T(y)$는 두 groupoid 사이의 functor

$$f(x),g(y): \ast\rightarrow \mathcal{Z}(T)$$

가 되며, 이 두 functor 사이의 $2$-morphism이 $\mathcal{Z}(T)$ 안에서의 morphism, 더 정확히는, $\mathcal{Z}(T)$가 groupoid이므로 isomorphism $f(x)\rightarrow g(y)$로 번역된다. 

일반적으로 $2$-category에서 commuting 조건을 생각할 때는 $2$-commutative 조건을 주로 생각한다. $2$-category에서의 diagram

(cone 그림)

이 $2$-commutative하다는 것은 commuting diagram은 세 개의 $1$-morphism 뿐만 아니라 ?와 ?을 잇는 $2$-morphism $\alpha$에 대한 정보까지 포함하는 triple (식)으로 나오게 된다. 


Scheme의 fiber product에 대응하는 개념이 stack의 *2-fiber product*이다. ([\[스킴\] §올곱, ⁋정리 8](/ko/math/scheme_theory/fiber_products#thm8))

Stack의 morphism $f:\mathcal{X}\rightarrow\mathcal{Z}$과 $g:\mathcal{Y}\rightarrow\mathcal{Z}$이 주어졌다고 하자. Scheme에서는 $x\in\mathcal{X}(T)$과 $y\in\mathcal{Y}(T)$에 대하여 $f(x)=g(y)$을 요구하면 충분하다. 그러나 stack에서는 $f(x)$와 $g(y)$도 groupoid $\mathcal{Z}(T)$의 대상이므로, 이 literal equality는 representative나 pseudofunctor의 presentation을 바꾸면 보존되지 않는다. 따라서 두 대상을 비교하는 intrinsic한 자료는 equality가 아니라 isomorphism

$$\alpha:f(x)\xrightarrow{\sim}g(y)$$

이다. 이 $\alpha$는 pullback coherence와는 다른 새로운 자료로, 일반적으로 canonical하지도 않고 주어진 $x$와 $y$에 대해 존재하지 않을 수도 있으며, 존재하더라도 automorphism만큼 여러 개일 수 있다. 그러므로 단지 $f(x)$와 $g(y)$이 isomorphic하다고 요구해서는 충분하지 않고, 구체적인 $\alpha$까지 점의 자료로 기억해야 한다.

앞에서 살펴본 pseudonaturality는 이렇게 고른 $\alpha$를 base change할 때 사용된다. Morphism $u:T'\rightarrow T$을 따라 $(x,y,\alpha)$를 pullback하면 두 image 사이의 isomorphism은

$$f(u^\ast x)\cong u^\ast f(x)\xrightarrow{u^\ast\alpha}u^\ast g(y)\cong g(u^\ast y)$$

으로 운반된다. 즉 stack morphism의 coherence는 $\alpha$를 만들어 주는 것이 아니라, 새로 고른 $\alpha$가 base change와 호환되도록 옮겨 준다. 가령 base scheme $S$ 위의 group $G$에 대하여 trivial torsor가 주는 morphism $S\rightarrow\mathbf{B}G$를 두 번 취하면

$$S\times_{\mathbf{B}G}S\cong G$$

이며, 우변의 $G$은 두 trivial torsor 사이에서 가능한 $\alpha$들을 기록한다. 이것이 stack의 fiber product에서 equality 대신 isomorphism 자체를 자료로 넣어야 하는 이유이다.

::: 정의 1
Site $\mathcal{C}$ 위의 CFG들의 morphism $f:\mathcal{X} \rightarrow \mathcal{Z}$과 $g:\mathcal{Y} \rightarrow \mathcal{Z}$이 주어졌다 하자. 이들의 *2-fiber product<sub>2-올곱</sub>* $\mathcal{X}\times_\mathcal{Z}\mathcal{Y}$은 다음 CFG이다. $T\in \mathcal{C}$ 위의 대상은 삼중쌍 $(x, y, \alpha)$로서, $x\in \mathcal{X}(T)$, $y\in \mathcal{Y}(T)$이고

$$\alpha: f(x)\xrightarrow{\ \sim\ }g(y)$$

이 $\mathcal{Z}(T)$의 isomorphism인 것이다. $(x, y, \alpha)$에서 $(x', y', \alpha')$로의 morphism은 morphism 쌍 $(u: x \rightarrow x', v: y \rightarrow y')$으로서 $\mathcal{Z}(T)$에서 $\alpha'\circ f(u)=g(v)\circ \alpha$을 만족하는 것이다. 사영 $(x, y, \alpha)\mapsto T$이 이를 CFG로 만든다.
:::

세 사영 functor $\operatorname{pr}_\mathcal{X}:(x, y, \alpha)\mapsto x$과 $\operatorname{pr}_\mathcal{Y}:(x, y, \alpha)\mapsto y$, 그리고 $\alpha$ 자신이 주는 natural isomorphism $f\circ \operatorname{pr}_\mathcal{X}\cong g\circ \operatorname{pr}_\mathcal{Y}$이 함께 2-fiber product의 자료를 이룬다. 여기에서 사각형의 가환성이 등호가 아니라 2-isomorphism $\alpha$으로 채워진다는 점이 핵심이다. 이 자료는 다음의 2-범주적 보편성을 가진다. 임의의 CFG $\mathcal{T}$과 morphism $a:\mathcal{T} \rightarrow \mathcal{X}$, $b:\mathcal{T} \rightarrow \mathcal{Y}$, 그리고 2-isomorphism $\beta: f\circ a\cong g\circ b$이 주어지면, morphism $h:\mathcal{T} \rightarrow \mathcal{X}\times_\mathcal{Z}\mathcal{Y}$이 본질적으로 유일하게 존재하여 $\operatorname{pr}_\mathcal{X}\circ h\cong a$, $\operatorname{pr}_\mathcal{Y}\circ h\cong b$이고 이 동형들이 $\beta$와 $\alpha$를 정합적으로 잇는다.

::: 명제 2
$\mathcal{X}, \mathcal{Y}, \mathcal{Z}$이 site $(\mathcal{C}, \tau)$ 위의 stack이면 [정의 1](#def1)의 $\mathcal{X}\times_\mathcal{Z}\mathcal{Y}$도 stack이며, 위의 2-보편성을 만족한다.
:::

이는 covering $\{T_i \rightarrow T\}$ 위의 descent datum이 $\mathcal{X}, \mathcal{Y}$의 descent datum과 $\mathcal{Z}$의 isomorphism presheaf $\operatorname{\underline{Isom}}$의 절단으로 분해되어, 각 stack 성질로부터 유일하게 붙는다는 사실에서 성분별로 따라온다. ([§스택, ⁋정의 10, 12](/ko/math/stacks/fibered_categories_and_stacks#def10))

[명제 2](#prop2)에 의하여 stack의 2-범주는 2-fiber product를 가진다. 이후로 $\mathcal{X}\times_\mathcal{Z}\mathcal{Y}$을 단순히 stack의 *fiber product*라 부르고, 가환사각형이라 하면 언제나 2-isomorphism으로 채워진 것으로 이해한다. 특히 base $S$가 scheme(또는 종대상)이면 $\mathcal{X}\times_S \mathcal{Y}$은 곱 stack이며, 그 $T$-점은 $(x, y)\in \mathcal{X}(T)\times \mathcal{Y}(T)$ ($S$ 위에서의 호환은 자동)이다.

## 표현가능 사상과 대수적 공간

Stack을 기하학적으로 만드는 첫 단계는 그 morphism 가운데 "scheme적인" 것을 가려내는 일이다. Morphism $f:\mathcal{X} \rightarrow \mathcal{Y}$이 representable하다는 것은, $\mathcal{Y}$의 임의의 scheme 값 점을 따라 $f$를 base change하면 통상적인 기하학적 대상이 나온다는 뜻이다.

::: 정의 3
Stack의 morphism $f:\mathcal{X} \rightarrow \mathcal{Y}$이 *representable<sub>표현가능</sub>*하다는 것은, 임의의 scheme $T$과 morphism $T \rightarrow \mathcal{Y}$ (즉 $y\in \mathcal{Y}(T)$)에 대하여 fiber product $\mathcal{X}\times_\mathcal{Y}T$이 algebraic space인 것이다 ([정의 4](#def4)). Scheme(또는 algebraic space)의 morphism에 대한 성질 $P$가 base change에 대하여 안정적이고 target에 대하여 fppf-국소적일 때, representable morphism $f$이 *성질 $P$을 가진다*는 것은 모든 그러한 base change $\mathcal{X}\times_\mathcal{Y}T \rightarrow T$이 algebraic space의 morphism으로서 $P$을 만족하는 것이다.
:::

이 정의는 $f$의 기하학적 성질(매끄러움, étale, flat, 전사, 분리, 유한 등)을 전부 algebraic space의 morphism에 대한 통상적 성질로 환원한다. 가령 representable morphism $f$이 *smooth surjective*라는 것은 모든 base change $\mathcal{X}\times_\mathcal{Y}T \rightarrow T$이 smooth하고 전사인 것이다. ([\[스킴\] §매끄러운 사상과 에탈 사상, ⁋정의 1](/ko/math/scheme_theory/smooth_and_etale_morphisms#def1)) Target에 대한 fppf-국소성 덕분에, 뒤에서 보듯 이러한 성질은 단 하나의 좋은 base change(atlas를 따른 것)에서 검사해도 충분하다.

Representability의 target이 되는 algebraic space는 scheme보다 약간 넓은 부류로, scheme을 étale 동치관계로 나눈 quotient이다. Scheme의 fppf quotient가 항상 scheme이 되지는 않지만 étale 동치관계에 의한 quotient는 algebraic space의 범위 안에 머무르며, 이 부류는 scheme과 거의 같은 기하를 누리면서 하강에 대해 닫혀 있다.

::: 정의 4
Site $(\Sch, \mathrm{\acute{e}t})$ ([§그로텐디크 위상, ⁋예시 8](/ko/math/stacks/grothendieck_topology#ex8)) 위의 sheaf $F:\Sch^\op \rightarrow \Set$이 *algebraic space<sub>대수적 공간</sub>*라는 것은 다음 두 조건을 만족하는 것이다.

1. (representable 대각선) diagonal morphism $F \rightarrow F\times F$이 scheme에 의해 representable하다. 즉 임의의 scheme $T$과 $T \rightarrow F\times F$에 대하여 $F\times_{F\times F}T$이 scheme이다.
2. (étale atlas) scheme $U$과 étale surjective morphism $U \rightarrow F$ (sheaf의 epimorphism이며 representable étale)이 존재한다.
:::

조건 1은 두 점의 일치 궤적 $U\times_F U\subseteq U\times U$이 scheme임을 보장하며, 이로써 algebraic space는 정확히 scheme $U$을 étale 동치관계 $R=U\times_F U\rightrightarrows U$으로 나눈 quotient $U/R$으로 실현된다. 모든 scheme은 algebraic space이고($U=F$, 대각선이 locally closed embedding), 두 부류는 정규(normal) 또는 quasi-projective 등의 가정 아래 흔히 일치한다. 우리는 algebraic space를 대각선의 representability에서 "scheme보다 한 단계 약한 target"으로 사용할 뿐이며, 그 이론을 본격적으로 전개하지 않는다. 자세한 내용은 [Ols]나 [Stacks]를 참조하라. 이하에서 "representable"은 별도 언급이 없는 한 algebraic space에 의한 representability를 뜻한다.

## 대각선의 표현가능성

Algebraic stack의 정의에서 대각선이 차지하는 위치를 이해하려면, 대각선의 base change가 무엇인지 먼저 계산해야 한다. Scheme에서 대각선 $\Delta:X \rightarrow X\times_S X$을 두 morphism $a, b: T \rightarrow X$을 따라 base change하면 둘이 일치하는 궤적 $\operatorname{Eq}(a, b)$이 나온다. Stack에서는 일치 대신 isomorphism을 기억하므로, 그 자리에 $\operatorname{\underline{Isom}}$이 등장한다.

::: 명제 5
$\mathcal{X}$이 base scheme $S$ 위의 stack이라 하자. 다음이 성립한다.

1. 임의의 scheme $T$과 $(x, y)\in \mathcal{X}(T)\times \mathcal{X}(T)$, 곧 morphism $(x, y): T \rightarrow \mathcal{X}\times_S \mathcal{X}$에 대하여, 대각선 $\Delta:\mathcal{X} \rightarrow \mathcal{X}\times_S \mathcal{X}$을 따른 base change에 natural isomorphism

$$\mathcal{X}\times_{\mathcal{X}\times_S \mathcal{X}}T\cong \operatorname{\underline{Isom}}_T(x, y)$$

이 있다. 따라서 $\Delta$이 representable한 것은 모든 $\operatorname{\underline{Isom}}_T(x, y)$이 algebraic space에 의해 representable한 것과 동치이다.

2. $\Delta$이 representable하면, scheme $T$로부터의 임의의 morphism $T \rightarrow \mathcal{X}$이 representable하다.
:::
::: 증명
(1) [정의 1](#def1)을 적용한다. $\mathcal{X}\times_{\mathcal{X}\times_S \mathcal{X}}T$의 $T'$-점은 $\xi\in \mathcal{X}(T')$, $T'$-점 $t: T' \rightarrow T$, 그리고 $\mathcal{X}\times_S \mathcal{X}$에서의 isomorphism $\Delta(\xi)=(\xi, \xi)\xrightarrow{\sim}(x, y)\vert_{T'}=(x\vert_{T'}, y\vert_{T'})$의 자료이다. 마지막 isomorphism은 두 성분의 isomorphism쌍 $\xi\xrightarrow{\sim}x\vert_{T'}$과 $\xi\xrightarrow{\sim}y\vert_{T'}$이며, 둘을 합성하면 $x\vert_{T'}\xrightarrow{\sim}y\vert_{T'}$, 곧 $\operatorname{\underline{Isom}}_T(x, y)(T'\xrightarrow{t}T)$의 원소를 얻는다. 역으로 그러한 isomorphism $\beta$이 주어지면 $\xi=x\vert_{T'}$과 쌍 $(\id, \beta)$을 취해 위 자료를 복원한다. 이 대응이 함자적이고 가역이므로 두 CFG가 동치이다. 따라서 $\Delta$의 모든 base change가 $\operatorname{\underline{Isom}}$이며, $\Delta$의 representability는 모든 $\operatorname{\underline{Isom}}_T(x, y)$의 representability와 같다.

(2) Morphism $T \rightarrow \mathcal{X}$과 임의의 scheme $T'$로부터의 morphism $T' \rightarrow \mathcal{X}$이 주어졌다 하자. $T\times_\mathcal{X}T'$이 algebraic space임을 보이면 된다. 곱 $T\times_S T' \rightarrow \mathcal{X}\times_S \mathcal{X}$을 두 점 $(x, y)$ (단, $x$은 $T \rightarrow \mathcal{X}$의 $T\times_S T'$로의 restriction, $y$은 $T'$ 쪽의 restriction)으로 보면, 표준적인 graph 동형

$$T\times_\mathcal{X}T'\cong(T\times_S T')\times_{\mathcal{X}\times_S \mathcal{X}, \Delta}\mathcal{X}$$

이 성립한다. 우변은 $\Delta$을 morphism $T\times_S T' \rightarrow \mathcal{X}\times_S \mathcal{X}$을 따라 base change한 것이고, $T\times_S T'$이 scheme이므로 (1)에 의해 representable, 곧 algebraic space이다. 따라서 $T\times_\mathcal{X}T'$이 algebraic space이고 $T \rightarrow \mathcal{X}$이 representable하다.
:::

[명제 5](#prop5)이 대각선 조건의 기하학적 의미를 밝힌다. 대각선이 representable하다는 것은 두 대상 $x, y$ 사이의 isomorphism들이 algebraic space를 이룬다는 것, 곧 두 점의 비교가 통상적인 기하의 범위에서 일어난다는 것이다. 특히 한 대상의 automorphism들 $\operatorname{\underline{Aut}}_T(x)=\operatorname{\underline{Isom}}_T(x, x)$이 $T$ 위의 group algebraic space가 되며, 이것이 stack의 점에 붙은 *stabilizer*(또는 *inertia*)이다. 둘째 항은 대각선이 representable하기만 하면 scheme(나아가 algebraic space)으로부터의 모든 morphism이 자동으로 representable함을 말한다. 따라서 다음 절에서 atlas $U \rightarrow \mathcal{X}$의 매끄러움·전사성을 논할 때 그 morphism이 representable함을 따로 요구할 필요가 없다.

## Algebraic stack과 Deligne–Mumford stack

이제 기하학적 stack을 정의한다. 두 조건은 [명제 5](#prop5)에서 분석한 대각선의 representability와, scheme으로부터의 smooth surjective atlas의 존재이다.

::: 정의 6
Site $(\Sch, \mathrm{fppf})$ 위의 stack $\mathcal{X}$ (base scheme $S$ 위)이 *algebraic stack* 또는 *Artin stack<sub>아틴 스택</sub>*이라는 것은 다음 두 조건을 만족하는 것이다.

1. (representable 대각선) 대각선 $\Delta:\mathcal{X} \rightarrow \mathcal{X}\times_S \mathcal{X}$이 algebraic space에 의해 representable하다.
2. (smooth atlas) scheme $U$과 representable smooth surjective morphism $\pi: U \rightarrow \mathcal{X}$이 존재한다. 이 $\pi$을 $\mathcal{X}$의 *atlas<sub>아틀라스</sub>* (또는 *presentation*)라 부른다.

나아가 $\mathcal{X}$이 *Deligne–Mumford stack<sub>들리뉴-멈퍼드 스택</sub>* (이하 *DM stack*)이라는 것은, 조건 2의 atlas $\pi: U \rightarrow \mathcal{X}$을 smooth 대신 *étale* 전사로 잡을 수 있는 것이다. ([\[스킴\] §매끄러운 사상과 에탈 사상, ⁋정의 11](/ko/math/scheme_theory/smooth_and_etale_morphisms#def11))
:::

조건 1에 의해 atlas morphism $\pi$은 자동으로 representable하므로 ([명제 5](#prop5)) 그 매끄러움·전사성이 [정의 3](#def3)의 의미로 잘 정의된다. Atlas는 scheme이 coordinate chart로 덮이는 것의 stack 판본으로, $\mathcal{X}$ 위의 기하학적 성질을 $U$ 위에서 검사하게 한다. 가령 $\mathcal{X}$의 차원은 $\dim \mathcal{X}=\dim U-d$ ($d$은 $\pi$의 relative dimension)로 정의되며, 이는 atlas의 선택에 의존하지 않는다. Smooth morphism이 flat하고 smooth fiber를 가지므로 smooth atlas는 stack을 "두꺼운" scheme으로 덮는 셈이고, 이때 fiber의 양의 차원에는 각 점에 붙은 stabilizer의 차원이 함께 담긴다.

DM stack과 Artin stack의 차이는 정확히 이 stabilizer가 양의 차원을 가질 수 있는지에 있다. Étale atlas는 relative dimension $0$의 atlas이므로, DM stack에서는 각 점의 automorphism group이 유한하고 infinitesimal deformation을 갖지 않는다.

엄밀하게는, algebraic stack $\mathcal{X}$에 대하여 다음 세 조건이 동치임이 잘 알려져 있다 ([\[스킴\] §매끄러운 사상과 에탈 사상, ⁋정리 15](/ko/math/scheme_theory/smooth_and_etale_morphisms#thm15)).

1. $\mathcal{X}$이 DM stack이다.
2. 대각선 $\Delta:\mathcal{X} \rightarrow \mathcal{X}\times_S \mathcal{X}$이 unramified하다. ([\[스킴\] §매끄러운 사상과 에탈 사상, ⁋정의 9](/ko/math/scheme_theory/smooth_and_etale_morphisms#def9))
3. 모든 geometric point의 stabilizer group scheme $\operatorname{\underline{Aut}}$이 finite group scheme이자 unramified(곧 finite étale)하다.

특히 base가 characteristic $0$의 field이면, Cartier 정리에 의해 모든 finite type group scheme이 smooth하므로 조건 3은 *stabilizer가 finite group*이라는 친숙한 기하학적 조건으로 귀결된다. 반면 characteristic $p$에서는 stabilizer가 위상적으로 유한이어도 $\mu_p$처럼 infinitesimal deformation을 가지는 비환원 group scheme이 될 수 있어 DM이 아닌 Artin stack이 된다. 즉 DM stack은 본질적으로 "각 점의 stabilizer가 유한하고 이산적인" algebraic stack이다.

문헌에 따라 정의의 형태가 조금씩 다르다. 원래 Deligne–Mumford의 정의는 unramified 대각선을 출발점으로 삼았고, Artin은 smooth atlas를 채택하였다. [정의 6](#def6)은 atlas의 존재를 일차 정의로 두고 대각선 조건을 동치로 다루는 [Stacks]·[Ols]의 통상적 서술을 따른 것이다. 또한 대각선이 representable하면서 *quasi-compact·분리*임을 추가로 요구하는 저자도 많으나, 이는 대상의 좋은 성질을 보장하기 위한 기술적 가정이므로 여기에서는 representability만을 정의에 포함한다.

## Quotient stack의 구성

앞선 논의에서 algebraic stack의 각 점에는 stabilizer(automorphism group)가 붙어 있음을 확인하였다. 그렇다면 거꾸로 **처음부터 어떤 대수군 $G$가 공간 $X$ 전체에 작용하여 각 점에 stabilizer를 부여하는 상황**을 생각하는 것이 가장 자연스럽다.

Group $G$이 scheme $X$에 작용할 때, 순진한 quotient $X/G$은 흔히 scheme으로 존재하지 않거나 작용의 stabilizer 정보를 잃는다. 이를 stack 차원에서 올바르게 다루는 것이 quotient stack $[X/G]$이며, 그 점은 $X$로 가는 equivariant morphism으로 *비틀린* torsor들이다. 이는 분류 stack $\mathbf{B}G$을 $X$-값 자료로 확장한 것이다 ([§스택, ⁋정의 17](/ko/math/stacks/fibered_categories_and_stacks#def17)).

이하에서 $G$은 base scheme $S$ 위의 flat·분리 group scheme이고 ([\[스킴\] §군 스킴, ⁋정의 1](/ko/math/scheme_theory/group_schemes#def1)), $X$은 $S$-scheme으로서 $G$의 좌작용 $\sigma: G\times_S X \rightarrow X$을 받는다 하자. Torsor는 [§스택, ⁋정의 17](/ko/math/stacks/fibered_categories_and_stacks#def17)의 left action convention을 따른다.

::: 정의 7
위의 자료에 대하여 *quotient stack<sub>몫 스택</sub>* $[X/G]$은 다음 CFG이다. $T\in \Sch/S$ 위의 대상은 쌍 $(P, \varphi)$로서

1. $P \rightarrow T$은 $G$-torsor(principal $G$-bundle)이고,
2. $\varphi: P \rightarrow X$은 $G$-equivariant morphism, 곧 $\varphi(g\cdot p)=g\cdot \varphi(p)$을 만족하는 morphism

이다. $(P, \varphi)$에서 $(P', \varphi')$로의 morphism은 $G$-torsor의 morphism $\psi: P \rightarrow P'$으로서 $\varphi'\circ \psi=\varphi$인 것이다 (이러한 $\psi$은 자동으로 isomorphism이다). Base change에 의한 pullback이 cartesian morphism을 주어 사영 $(P, \varphi)\mapsto T$이 이를 CFG로 만든다. $X=S$에 $G$이 자명하게 작용하는 경우 $[S/G]=\mathbf{B}G$이며, 이를 *classifying stack*이라 부른다.
:::

$[X/G]$의 한 점 $(P, \varphi)$은 "$T$ 위에서 $G$만큼 비틀린 채 $X$로 사상하는 자료"이다. Torsor $P$이 자명한 경우, 곧 $P=G\times_S T$(left translation action)인 경우 equivariant morphism $\varphi: G\times_S T \rightarrow X$은 $\varphi(g, t)=g\cdot \varphi(e, t)$으로 단위절단에서의 값 $a:=\varphi(e, -): T \rightarrow X$에 의해 완전히 결정된다. 즉 자명한 torsor 위의 자료는 단순히 $X$의 한 점 $a\in X(T)$과 같다. 이 관찰이 atlas의 출발점이다. 한편 $\mathbf{B}G$은 $X=S$이라 equivariant morphism이 유일하므로 $\mathbf{B}G(T)$은 정확히 $T$ 위의 $G$-torsor들의 groupoid이고, 그 automorphism은 $G(T)$이다. $\mathbf{B}G$이 고전적으로 위상공간의 classifying space $BG$이 맡던 역할, 곧 $G$-bundle을 분류하는 보편 대상의 역할을 대수기하에서 수행한다.

[§스택, ⁋정리 18](/ko/math/stacks/fibered_categories_and_stacks#thm18)에서 $\mathbf{B}\mathbb{G}_m$이 stack임을 line bundle 하강으로 보았듯, $[X/G]$이 stack임은 torsor와 equivariant morphism이 모두 fppf covering을 따라 하강한다는 사실에서 따른다. Torsor는 fppf-국소적으로 자명하고 그 descent datum이 effective하며, equivariant morphism은 $X$로의 morphism이므로 representable sheaf의 절단으로서 하강한다. 우리는 이 stack 성질을 전제하고 ([명제 2](#prop2)과 같은 성분별 하강 논증이 그대로 적용된다) 곧바로 대수성으로 나아간다. 먼저 atlas를 구성한다.

::: 명제 8
Morphism $\pi: X \rightarrow [X/G]$을, $T$-점 $a\in X(T)$에 자명한 torsor와 그것이 결정하는 equivariant morphism을 대응시키는 것으로 정의하면, 곧

$$\pi(a)=\bigl(G\times_S T,\ \varphi_a\bigr),\qquad \varphi_a(g, t)=g\cdot a(t),$$

이는 stack의 morphism이며 sheaf의 epimorphism, 곧 전사이다.
:::
::: 증명
$\pi$이 함자적임은 $a$의 base change가 자명 torsor의 base change와 호환됨에서 따른다. $\pi$이 전사임을 본다. 임의의 $(P, \varphi)\in [X/G](T)$에 대하여, $P$은 $G$-torsor이므로 [§스택, ⁋정의 17](/ko/math/stacks/fibered_categories_and_stacks#def17)에 의해 fppf covering $\{T_i \rightarrow T\}$ 위에서 자명해진다. 곧 각 $T_i$ 위에서 절단 $s_i\in P(T_i)$이 존재하여 $g\mapsto g\cdot s_i$이 $G\times_S T_i\xrightarrow{\sim}P\vert_{T_i}$을 준다. 이 trivialization 아래 $(P, \varphi)\vert_{T_i}$은 $a_i:=\varphi(s_i)\in X(T_i)$이 결정하는 $\pi(a_i)$과 동형이다. 따라서 $(P, \varphi)$은 covering $\{T_i \rightarrow T\}$ 위에서 $\pi$의 image에 국소적으로 들어가며, 이는 sheaf의 epimorphism의 정의 그대로이다. 그러므로 $\pi$은 전사이다.
:::

[명제 8](#prop8)의 $\pi$이 atlas의 후보이다. 그것이 representable하고 smooth함을 보이려면 그 base change를 계산해야 하는데, 가장 중요한 것이 $\pi$ 자신을 따른 base change, 곧 $X\times_{[X/G]}X$이다. 이 계산이 quotient stack의 groupoid presentation을 드러낸다.

::: 명제 9
[명제 8](#prop8)의 atlas $\pi: X \rightarrow [X/G]$에 대하여 표준적인 동형

$$X\times_{[X/G]}X\cong G\times_S X$$

이 있으며, 두 사영 $\operatorname{pr}_1, \operatorname{pr}_2: X\times_{[X/G]}X \rightarrow X$은 이 동형 아래 각각 작용 $\sigma:(g, x)\mapsto g\cdot x$과 사영 $(g, x)\mapsto x$에 대응한다. 따라서 $[X/G]$은 groupoid presentation $G\times_S X\rightrightarrows X$을 가진다.
:::
::: 증명
[정의 1](#def1)에 의해 $(X\times_{[X/G]}X)(T)$의 대상은 삼중쌍 $(a, b, \psi)$로서 $a, b\in X(T)$이고 $\psi:\pi(a)\xrightarrow{\sim}\pi(b)$은 $[X/G](T)$의 isomorphism이다. $\pi(a)=(G_T, \varphi_a)$, $\pi(b)=(G_T, \varphi_b)$ ($G_T=G\times_S T$)이므로 $\psi$은 자명 torsor $G_T$의 automorphism으로서 $\varphi_b\circ \psi=\varphi_a$을 만족하는 것이다. Left translation torsor $G_T$의 좌-equivariant automorphism은 정확히 right translation $\psi_g: h\mapsto hg$ ($g\in G(T)$)이며, 이로써 $\psi\leftrightarrow g\in G(T)$의 대응을 얻는다. ([§스택, ⁋정의 17](/ko/math/stacks/fibered_categories_and_stacks#def17)) 조건 $\varphi_b\circ \psi_g=\varphi_a$은 모든 $(h, t)$에 대하여

$$\varphi_b(hg, t)=hg\cdot b(t)\overset{!}{=}h\cdot a(t)=\varphi_a(h, t)$$

을 요구하고, $h=e$을 대입하면 $g\cdot b(t)=a(t)$, 곧 $a=g\cdot b$(작용 $\sigma$의 의미)과 동치이다 (역으로 이 등식이면 모든 $h$에 대해 성립한다). 그러므로 $(a, b, \psi)$은 쌍 $(g, b)\in(G\times_S X)(T)$($a=g\cdot b$으로 결정됨)과 일대일로 대응하며, 이 대응은 $T$에 대해 함자적이고 morphism과 호환된다. 따라서 $X\times_{[X/G]}X\cong G\times_S X$이다.

이 동형 아래 $\operatorname{pr}_2(a, b, \psi)=b$은 $(g, b)\mapsto b$, 곧 사영이고, $\operatorname{pr}_1(a, b, \psi)=a=g\cdot b$은 $(g, b)\mapsto g\cdot b$, 곧 작용 $\sigma$이다. 두 morphism $\sigma, \operatorname{pr}_2: G\times_S X\rightrightarrows X$이 $[X/G]$의 groupoid presentation을 이룬다.
:::

{% diagram Math/Stacks/Algebraic_Stacks-1.svg width="10.32em" alt="atlas의 base change" %}

[명제 9](#prop9)는 $[X/G]$을 작용 groupoid의 stack quotient로 다시 보여준다. Scheme의 groupoid $G\times_S X\rightrightarrows X$ (source는 사영, target은 작용)은 작용의 "fiber"를 부호화하며, $[X/G]$은 이 groupoid를 stack 차원에서 나눈 것이다. 일반적으로 source·target이 smooth(각각 flat)한 groupoid object $R\rightrightarrows U$로부터 algebraic stack $[U/R]$을 얻는데, quotient stack은 $R=G\times_S X$, $U=X$인 특수한 경우이다. 이제 이 presentation으로부터 $[X/G]$의 대수성을 끌어낸다.

## Quotient stack의 대수성

::: 정리 10
$G$이 base scheme $S$ 위의 flat·분리·smooth group scheme이고 $X$이 $S$-scheme에 $G$의 작용을 받는다 하자. 그럼 quotient stack $[X/G]$은 algebraic stack이며, [명제 8](#prop8)의 $\pi: X \rightarrow [X/G]$이 atlas이다. 나아가 다음이 성립한다.

1. $X$이 $S$ 위에서 분리하면 $[X/G]$의 대각선이 분리 morphism으로 representable하다. 나아가 $[X/G]$이 분리하는 것은 작용 morphism $G\times_S X \rightarrow X\times_S X$, $(g, x)\mapsto(g\cdot x, x)$이 proper인 것과 동치이다.
2. 모든 geometric point의 stabilizer가 유한·étale하면 (가령 $G$이 유한 étale하거나, characteristic $0$에서 작용이 finite stabilizer를 가지면) $[X/G]$은 DM stack이다.
:::
::: 증명
**대각선의 representability.** [명제 5](#prop5)에 의해 임의의 scheme $T$과 $(P, \varphi), (P', \varphi')\in [X/G](T)$에 대하여 $\operatorname{\underline{Isom}}_T((P, \varphi), (P', \varphi'))$이 representable함을 보이면 된다. $P, P'$이 자명해지는 fppf covering 위에서 이 sheaf는 $g\cdot a'=a$을 만족하는 $g\in G_T$들의 모임, 곧 사상 $(g\mapsto(g\cdot a', a)): G_T \rightarrow X\times_S X$과 $X$의 대각선 $X \rightarrow X\times_S X$의 fiber product이다. Scheme의 대각선이 항상 locally closed embedding이므로 그 base change인 $\operatorname{\underline{Isom}}$은 $G_T$의 locally closed subscheme으로 representable하다. $X$가 분리되어 있으면 $X$의 대각선이 closed embedding이므로 $\operatorname{\underline{Isom}}\rightarrow T$은 분리 사상이 된다.

**smooth atlas.** [명제 8](#prop8)에 의해 $\pi: X \rightarrow [X/G]$은 전사이고 [명제 5](#prop5)에 의해 representable하다. 임의의 $T \rightarrow [X/G]$에 대한 base change $X\times_{[X/G]}T \rightarrow T$은 $P$가 자명해지는 fppf covering 위에서 [명제 9](#prop9)에 의해 사영 $(G\times_S X)\times_X T_i \rightarrow T_i$과 동형이다. $G$가 $S$ 위에서 smooth하므로 이 사영은 smooth 전사이고, 매끄러움과 전사성의 fppf-국소성에 의해 $\pi$은 smooth atlas이다. 이로써 $[X/G]$은 algebraic stack이다.

**DM 판정.** 모든 geometric point의 stabilizer가 finite étale하면 앞서 본 판정 조건에 의해 $[X/G]$은 DM stack이다. 특히 $G$이 finite étale group scheme이면 $\pi: X \rightarrow [X/G]$ 자체가 relative dimension $0$인 étale morphism이므로 $X$가 곧 étale atlas가 된다.
:::

[정리 10](#thm10)은 algebraic group의 작용이 자동으로 algebraic stack을 낳음을 보장한다. 대각선의 representability는 isomorphism 조건이 $G$ 안에서 subscheme으로 잘려 나옴에서, atlas의 매끄러움은 $\pi$의 base change가 사영 $G\times_S X \rightarrow X$이라는 점에서 따라온다. 이 두 사실은 모두 [명제 9](#prop9)의 groupoid presentation으로 환원된다.

순진한 quotient와의 관계는 작용의 자유로움에 달려 있다. 만일 $G$이 $X$에 자유롭게(stabilizer가 자명하게) 작용하면 [명제 9](#prop9)의 $\operatorname{\underline{Isom}}$이 많아야 한원소가 되어 $[X/G]$의 대각선이 monomorphism이고, 이때 $[X/G]$은 fiber에 automorphism이 없는 stack, 곧 algebraic space가 되어 $G\times_S X\rightrightarrows X$의 (fppf) quotient인 *coarse quotient* $X/G$과 일치한다. 작용이 자유롭지 않으면 각 점에 stabilizer가 남아 $[X/G]$은 진정한 stack이 되며, 이때에도 점의 isomorphism class를 뭉갠 coarse moduli space $X/G$ (존재할 경우)로 가는 자연스러운 morphism $[X/G] \rightarrow X/G$이 있으나 이는 stabilizer 정보를 잃는다. 다음 절의 $[\mathbb{A}^1/\mathbb{G}_m]$이 이 손실을 선명히 보여준다.

## 예시

가장 기본적인 예는 $X=S$인 분류 stack이다. 이는 [§스택, ⁋정의 17](/ko/math/stacks/fibered_categories_and_stacks#def17)에서 도입한 $\mathbf{B}G$이 사실 algebraic stack임을 [정리 10](#thm10)으로 확인하는 것이다.

::: 예시 11 ($\mathbf{B}\mathbb{G}_m$과 $\mathbf{B}(\mathbb{Z}/n)$)
Base를 field $\mathbb{K}$로 둔다.

1. $\mathbf{B}\mathbb{G}_m=[\Spec \mathbb{K}/\mathbb{G}_m]$은 algebraic stack이다. $\mathbb{G}_m$이 affine·smooth하므로 ([\[스킴\] §군 스킴, §§군 스킴](/ko/math/scheme_theory/group_schemes#군-스킴)) [정리 10](#thm10)이 적용되고, atlas는 $\Spec \mathbb{K} \rightarrow \mathbf{B}\mathbb{G}_m$이며 그 base change는 $\mathbb{G}_m \rightrightarrows \Spec \mathbb{K}$이다. $\mathbf{B}\mathbb{G}_m(T)$은 $T$ 위의 line bundle들의 groupoid이고 ([§스택, ⁋정리 18](/ko/math/stacks/fibered_categories_and_stacks#thm18)), 한 점의 stabilizer는 $\mathbb{G}_m$이다. Stabilizer가 $1$차원이라 infinitesimal deformation을 가지므로 $\mathbf{B}\mathbb{G}_m$은 DM이 아닌 Artin stack이며, 그 차원은 $\dim \Spec \mathbb{K}-\dim \mathbb{G}_m=0-1=-1$이다. 음의 차원은 stabilizer가 점보다 "더 큰" algebraic stack의 특징이다.

2. $\mathbb{Z}/n$을 상수 group scheme으로 볼 때 $\mathbf{B}(\mathbb{Z}/n)=[\Spec \mathbb{K}/(\mathbb{Z}/n)]$은 DM stack이다. $\mathbb{Z}/n$은 유한 étale하므로 ([\[스킴\] §매끄러운 사상과 에탈 사상, ⁋예시 14](/ko/math/scheme_theory/smooth_and_etale_morphisms#ex14)에서 분리 확대가 étale함과 같은 이유로 상수군은 étale하다) atlas $\Spec \mathbb{K} \rightarrow \mathbf{B}(\mathbb{Z}/n)$이 étale 전사이고 ([정리 10](#thm10)의 DM 판정), 그 base change는 $n$개의 점의 disjoint union $\mathbb{Z}/n\times \Spec \mathbb{K}\rightrightarrows \Spec \mathbb{K}$이다. $\mathbf{B}(\mathbb{Z}/n)(T)$은 $T$ 위의 $\mathbb{Z}/n$-torsor, 곧 degree $n$의 cyclic étale covering의 groupoid이며, 한 점의 stabilizer는 finite group $\mathbb{Z}/n$이다. $\operatorname{char}\mathbb{K}\nmid n$이면 $\mu_n$ 또한 유한 étale하여 $\mathbf{B}(\mathbb{Z}/n)$과 $\mathbf{B}\mu_n$이 모두 DM이지만, $\operatorname{char}\mathbb{K}\mid n$이면 $\mu_n$이 비환원이 되어 $\mathbf{B}\mu_n$은 (DM이 아닌) Artin stack이 되는 반면 상수군 $\mathbf{B}(\mathbb{Z}/n)$은 여전히 DM이다. 이 분리가 characteristic $p$에서 étale·infinitesimal stabilizer의 차이를 드러낸다.
:::

다음은 stabilizer가 점마다 도약하는 작용의 표준적인 예로, coarse quotient가 잃어버리는 정보를 stack이 어떻게 보존하는지를 보여준다.

::: 예시 12 ($[\mathbb{A}^1/\mathbb{G}_m]$)
Field $\mathbb{K}$ 위에서 $\mathbb{G}_m$이 affine line $\mathbb{A}^1$에 스칼라 배 $t\cdot x=tx$으로 작용한다 하자. 작용의 orbit은 둘뿐이다. 원점 $\{0\}$은 fixed point이라 한 orbit을 이루고, 여집합 $\mathbb{A}^1\setminus\{0\}=\mathbb{G}_m$은 $\mathbb{G}_m$이 단순추이적으로 작용하는 한 orbit이다. 따라서 위상적인 quotient $\mathbb{A}^1/\mathbb{G}_m$은 두 점(열린 orbit과 원점)으로 이루어지며 열린 orbit의 closure가 원점을 포함한다.

Ring의 불변량으로 계산한 categorical quotient, 곧 affine GIT quotient $\Spec(\Gamma(\mathbb{A}^1, \mathcal{O})^{\mathbb{G}_m})$을 취하면 $\mathbb{K}[\x]^{\mathbb{G}_m}=\mathbb{K}$이므로 ([§Cox 구성과 GIT quotient, ⁋명제 3](/ko/math/toric_geometry/cox_construction#prop3)), 닫히지 않은 궤적을 닫힌 궤적과 구별하지 못하고 한 점 $\Spec \mathbb{K}$으로 뭉개버린다.

반면 quotient stack $[\mathbb{A}^1/\mathbb{G}_m]$은 이 두 orbit의 서로 다른 stabilizer를 모두 온전히 기억한다. [정리 10](#thm10)에 의해 이는 $1$차원 affine scheme $\mathbb{A}^1$을 $1$차원 group $\mathbb{G}_m$으로 나눈 algebraic stack으로, $\dim[\mathbb{A}^1/\mathbb{G}_m]=1-1=0$이다. 그 점은 정확히 두 개이다.

1. 열린 점: 열린 orbit $\mathbb{G}_m\hookrightarrow \mathbb{A}^1$ 위에서 작용이 자유로우므로 $[\mathbb{G}_m/\mathbb{G}_m]\cong \Spec \mathbb{K}$이고, 이는 stabilizer가 자명한 열린 점 $\Spec \mathbb{K}\hookrightarrow [\mathbb{A}^1/\mathbb{G}_m]$을 이룬다.

2. closed point: 원점 $\{0\}=\Spec \mathbb{K}$은 $\mathbb{G}_m$이 자명하게 작용하는 fixed point이므로 $[\{0\}/\mathbb{G}_m]=\mathbf{B}\mathbb{G}_m$이고, 이는 stabilizer $\mathbb{G}_m$을 가진 closed point이다. ([예시 11](#ex11))

즉 $[\mathbb{A}^1/\mathbb{G}_m]$은 한 개의 열린 점과, 그 closure에 놓인 $\mathbf{B}\mathbb{G}_m$ 한 점으로 이루어진다. 불변량에 기반한 categorical/GIT quotient $\Spec \mathbb{K}$이 두 점을 하나로 뭉갠 데 반해, stack은 원점의 stabilizer $\mathbb{G}_m$을 closed point에 붙은 $\mathbf{B}\mathbb{G}_m$으로 정확히 기록한다. Stabilizer가 양의 차원을 가지므로 이 stack은 DM이 아닌 Artin stack이다.
:::

마지막으로 stack 이론의 본래 동기였던 moduli 문제로 돌아간다. 타원곡선의 moduli는 quotient 꼴로 실현되는 DM stack의 대표적인 예이다.

::: 예시 13 (타원곡선의 moduli $\mathcal{M}_{1, 1}$)
Base에 따라, $T$ 위의 *타원곡선*(절단을 가진 종수 $1$의 smooth 사영곡선)들의 $T$-족과 그 isomorphism이 이루는 CFG를 $\mathcal{M}_{1, 1}$로 적는다. 이는 stack이며, characteristic $0$(또는 $2, 3$을 뒤집은 base) 위에서 Weierstrass 방정식 $y^2=x^3+ax+b$의 계수 $(a, b)$ ($\Delta=-16(4a^3+27b^2)\neq 0$)에 좌표변환군이 작용하는 quotient

$$\mathcal{M}_{1, 1}\cong \bigl[\{(a, b)\mid\Delta\neq 0\}\big/\mathbb{G}_m\bigr]$$

으로 실현된다. 여기에서 $\mathbb{G}_m$은 $\lambda\cdot(a, b)=(\lambda^4 a, \lambda^6 b)$으로 작용하며 (Weierstrass 다항식에서 $a, b$에 각각 weight $4, 6$을 부여), 이 작용은 finite stabilizer를 가진다. 일반적인 점의 stabilizer는 $\{\pm 1\}=\mathbb{Z}/2$ ($(x, y)\mapsto(x, -y)$, 곧 $[-1]$ automorphism)이고, $j=0$과 $j=1728$의 특수 타원곡선에서 각각 $\mathbb{Z}/6$, $\mathbb{Z}/4$으로 도약한다. Stabilizer가 모두 유한하므로 [정리 10](#thm10)에 의해 $\mathcal{M}_{1, 1}$은 DM stack이며, 그 coarse moduli space는 $j$-불변량이 주는 affine line $\mathbb{A}^1_j$이다. Stack $\mathcal{M}_{1, 1}$이 coarse 공간 $\mathbb{A}^1_j$과 다른 까닭은 정확히 모든 타원곡선이 적어도 $\mathbb{Z}/2$의 automorphism을 가져, 점마다 비자명한 stabilizer가 붙기 때문이다. 이 stack의 정밀한 구성과 그 automorphism 구조는 다음 글에서 다룬다.
:::

[예시 13](#ex13)은 moduli 문제가 왜 stack을 요구하는지를 다시 확인한다. 타원곡선은 모두 $[-1]$ automorphism을 가지므로 그 isomorphism class의 집합 $\mathbb{A}^1_j$만으로는 보편 족을 가질 수 없고 ([§스택, ⁋예시 2](/ko/math/stacks/fibered_categories_and_stacks#ex2)에서 line bundle이 $\Pic$만으로 분류되지 않던 것과 같은 이유), automorphism을 기억하는 DM stack $\mathcal{M}_{1, 1}$에 이르러 비로소 보편 타원곡선이 존재한다. Quotient stack과 algebraic stack의 언어가 이러한 moduli를 다루는 정확한 틀을 제공한다.

---

**참고문헌**

**[Ols]** M. Olsson, *Algebraic spaces and stacks*. American Mathematical Society Colloquium Publications, 2016.  
**[LMB]** G. Laumon, L. Moret-Bailly, *Champs algébriques*. Ergebnisse der Mathematik und ihrer Grenzgebiete, Springer, 2000.  
**[FGA]** B. Fantechi, L. Göttsche, L. Illusie, S. Kleiman, N. Nitsure, A. Vistoli, *Fundamental algebraic geometry: Grothendieck's FGA explained*. Mathematical Surveys and Monographs, American Mathematical Society, 2005.  
**[Stacks]** The Stacks Project Authors, *The Stacks Project*. Available [online](https://stacks.math.columbia.edu/).
