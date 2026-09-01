---
title: "Algebraic stack과 quotient stack"
description: "대각선의 표현가능성과 매끄러운 atlas로 algebraic stack(Artin·Deligne–Mumford)을 정의하고, 군작용의 quotient stack [U/G]와 BG=[pt/G]를 구성하여 그 기하적 의미를 다룬다."
excerpt: "Algebraic (Artin / Deligne–Mumford) stacks via atlases, and the quotient stack [U/G]"

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

이를 위해 어떠한 데이터가 필요한지 살펴보자. 두 stack morphism $f: \mathcal{X}\rightarrow \mathcal{Z}$와 $g:\mathcal{Y}\rightarrow \mathcal{Z}$에 대하여, [\[스킴\] §점함자, ⁋명제 7](/ko/math/scheme_theory/functor_of_points#prop7)을 생각하면 stack morphism의 fiber product를 정의하기 위해서는 각 $T$마다 fiber product를

$$\mathcal{X}(T)\times_{\mathcal{Z}(T)}\mathcal{Y}(T)$$

로 정의해주면 된다. Scheme에서의 fiber product를 정의할 때는 $X(T)\times_{Z(T)}Y(T)$를, <em-ko>집합</em-ko> $Z(T)$ 안에서 $f_T(x)=g_T(y)$를 만족하는 원소들로 잡았으나, 이제 $\mathcal{Z}(T)$가 groupoid인 이상 이 조건을 isomorphism으로 내려야 한다. 이는 [§스택, ⁋명제 6](/ko/math/stacks/fibered_categories_and_stacks#prop6) 직후에 살펴본 상황과 정확히 동일한 상황으로, 점 $x\in \mathcal{X}(T)$를 groupoid 사이의 functor $x:\ast\rightarrow \mathcal{X}(T)$로 본다면 $f_T(x)$와 $g_T(y)$는 두 groupoid 사이의 functor

$$f(x),g(y): \ast\rightarrow \mathcal{Z}(T)$$

가 되며, 이 두 functor 사이의 $2$-morphism이 $\mathcal{Z}(T)$ 안에서의 morphism, 더 정확히는, $\mathcal{Z}(T)$가 groupoid이므로 isomorphism $f(x)\rightarrow g(y)$로 번역된다. 

일반적으로 $2$-category에서 commuting 조건을 생각할 때는 $2$-commutative 조건을 주로 생각한다. 예를 들어 다음 triangle을 생각하자.

![2-commutative triangle](/assets/images/Math/Stacks/Algebraic_Stacks-2.svg){:style="width:12.05em" class="invert" .align-center}

이 triangle이 $2$-commutative하다는 것은 세 $1$-morphism $p,q,r$와 함께 합성 $q\circ p$와 $r$을 잇는 invertible $2$-morphism

$$\alpha:q\circ p\Rightarrow r$$

가 지정되었다는 뜻이다. 따라서 이 diagram의 자료는 $(p,q,r,\alpha)$로 주어진다. 이를 지금의 상황에 적용하면 다음 diagram을 얻는다.

![stack의 2-commutative cone](/assets/images/Math/Stacks/Algebraic_Stacks-3.svg){:style="width:14.89em" class="invert" .align-center}

그림 중앙의 $\alpha$는 $\mathcal{X}(T)$와 $\mathcal{Y}(T)$ 사이에 놓여 있으며, 두 경로가 주는 합성 $f\circ x,g\circ y:\ast\rightarrow\mathcal{Z}(T)$을 잇는 $2$-morphism을 나타낸다. 이를 위에서 살펴본 $\mathcal{Z}(T)$에서의 morphism의 언어로 옮겨오면, 이 cone의 자료는 triple

$$(x,y,\alpha),\qquad \alpha:f(x)\xrightarrow{\sim}g(y)$$

로 주어지는 것을 알 수 있다. 즉, $f(x)$에서 $g(y)$로의 isomorphism을 명시적으로 기억해주어야 한다. 따라서 다음과 같이 정의한다.

::: 정의 1
Site $\mathcal{C}$ 위의 CFG들의 morphism $f:\mathcal{X}\rightarrow\mathcal{Z}$과 $g:\mathcal{Y}\rightarrow\mathcal{Z}$이 주어졌다 하자. 이들의 *2-fiber product<sub>2-올곱</sub>* $\mathcal{X}\times_\mathcal{Z}\mathcal{Y}$은 다음 category이다. 그 대상은 어떤 $T\in\mathcal{C}$에 대한 $x\in\mathcal{X}(T)$, $y\in\mathcal{Y}(T)$와 $\mathcal{Z}(T)$의 isomorphism

$$\alpha: f(x)\xrightarrow{\ \sim\ }g(y)$$

으로 이루어진 triple $(x,y,\alpha)$이다. $T$ 위의 $(x,y,\alpha)$에서 $T'$ 위의 $(x',y',\alpha')$로의 morphism은 같은 morphism $h:T\rightarrow T'$ 위에 놓이는 morphism들의 쌍 $(a:x\rightarrow x',b:y\rightarrow y')$으로서 $\mathcal{Z}$에서

$$\alpha'\circ f(a)=g(b)\circ\alpha$$

을 만족하는 것이다. 항등 morphism과 합성은 각 성분에서 정의한다.
:::

사영 $(x,y,\alpha)\mapsto T$과 $(a,b)\mapsto h$은 functor $\mathcal{X}\times_\mathcal{Z}\mathcal{Y}\rightarrow\mathcal{C}$를 정의한다. $\mathcal{X}$와 $\mathcal{Y}$에서 cartesian lift들을 성분별로 고르면 $\alpha$는 위의 compatibility condition에 의해 함께 pullback되므로, 이 사영은 $\mathcal{X}\times_\mathcal{Z}\mathcal{Y}$을 CFG로 만든다. 이 CFG에는 두 projection functor $\pr_\mathcal{X}:(x,y,\alpha)\mapsto x$과 $\pr_\mathcal{Y}:(x,y,\alpha)\mapsto y$, 그리고 $\alpha$가 주는 natural isomorphism $f\circ\pr_\mathcal{X}\cong g\circ\pr_\mathcal{Y}$이 있다. 일반적으로 임의의 CFG $\mathcal{T}$에 대하여 morphism $\mathcal{T}\rightarrow\mathcal{X}\times_\mathcal{Z}\mathcal{Y}$을 주는 것은 morphism $a:\mathcal{T}\rightarrow\mathcal{X}$, $b:\mathcal{T}\rightarrow\mathcal{Y}$와 2-isomorphism $\beta:f\circ a\cong g\circ b$을 주는 것과 동치이며, 이것이 2-fiber product의 2-categorical universal property이다.

위의 정의는 CFG로서의 2-fiber product를 선언한 것에 불과하므로, stack의 2-범주 안에서 이것이 실제로 존재함을 보이려면 별도의 논증이 필요하다. 이는 각 성분의 descent datum을 붙임으로써 얻어진다.

::: 명제 2
Site $(\mathcal{C},\tau)$ 위의 stack morphism $f:\mathcal{X}\rightarrow\mathcal{Z}$과 $g:\mathcal{Y}\rightarrow\mathcal{Z}$에 대하여, 2-fiber product $\mathcal{X}\times_\mathcal{Z}\mathcal{Y}$은 stack이다.
:::

이후로 $\mathcal{X}\times_\mathcal{Z}\mathcal{Y}$을 단순히 stack의 *fiber product*라 부르며, stack들 사이의 commutative diagram은 항상 $2$-isomorphism으로 채워진 것으로 이해한다. 

## 대수적 공간

이제 우리는 예고한 것과 같이 stack 위에 대수기하학적 성질들을 부여한다. 혹은 이미 scheme에서 다뤘듯, 이는 stack morphism에 대수기하학적 성질을 부여하는 것으로 해결할 수 있다. 우리 전략은 fiber product를 이용하는 것이며, 이것이 이번 글의 첫 정의가 stack들의 fiber product였던 이유이다.

Scheme morphism의 대부분의 성질 $P$는 base change에 대하여 닫혀있다. 즉, 임의의 $f:X\rightarrow Y$가 성질 $P$를 갖는다면, 임의의 scheme $T$와 morphism $T\rightarrow Y$에 대한 base change morphism $f_T:X\times_YT\rightarrow T$ 또한 그러하다. 거꾸로 만일 $f_T$가 <em-ko>모든</em-ko> scheme $T$와 morphism $T\rightarrow Y$에 대해 성질 $P$를 만족한다면, $T=Y$이고 $T\rightarrow Y$가 $\id_Y$인 경우로 두어 $f_T=f$가 성질 $P$를 갖는다는 것을 알 수 있다.

우리는 이를 아이디어 삼아 stack morphism $f:\mathcal{X}\rightarrow \mathcal{Y}$의 성질을 scheme morphism의 성질과 base change를 사용하여 정의할 것이다. 즉, 아이디어는 임의의 scheme $T$와 morphism $T\rightarrow \mathcal{Y}$에 대하여, base change $f_T:\mathcal{X}\times_\mathcal{Y}T\rightarrow T$가 scheme morphism이고 *scheme morphism의 성질* $P$를 가지면, $f$가 *stack morphism의 성질* $P$를 가진다고 정의하는 것이다.

문제는 base change의 source $\mathcal{X}\times_\mathcal{Y}T$가 scheme인 것만을 허용하면 그 범위가 지나치게 좁다는 것이다. 그렇다고 임의의 stack까지 허용하면 $f_T$를 더 이상 scheme morphism의 언어로 통제할 수 없으므로 이 전략 자체가 불가능하다. 따라서 우리는 $\mathcal{X}\times_\mathcal{Y}T$가 scheme에서 아주 조금 넓어진, 여전히 scheme-theoretic geometry를 적용할 수 있는 대상에 머무르기를 요구하며, 그 대상이 바로 *algebraic space*이다.

::: 정의 3
Site $(\Sch, \et)$ ([§그로텐디크 위상, ⁋예시 8](/ko/math/stacks/grothendieck_topology#ex8)) 위의 sheaf $F:\Sch^\op \rightarrow \Set$이 *algebraic space<sub>대수적 공간</sub>*라는 것은 다음 두 조건을 만족하는 것이다.

1. (Representability) Diagonal morphism $F \rightarrow F\times F$이 scheme에 의해 representable하다. 즉 임의의 scheme $T$과 $T \rightarrow F\times F$에 대하여 $F\times_{F\times F}T$이 scheme이다.
2. (Étale atlas) Scheme $U$과 representable étale morphism $U \rightarrow F$가 존재하며, 이 morphism은 sheaf의 epimorphism이다.
:::

첫째 조건은 앞서 설명한 아이디어와 거의 유사한 것으로, 이를 위와 같이 이름붙이면 우리의 나중 전략은 stack morphism을 algebraic space로 represent되는 것만을 본다는 식으로 줄여 말할 수 있을 것이다.

둘째 조건의 morphism $U\rightarrow F$를 $F$의 *étale atlas*라 부른다. 직관적으로 이는 scheme $U$가 $F$를 완전하게 덮으며, 이 겹침을 기록하는 동치관계로 $U$를 나누면 $F$가 복원된다는 것이다. 이를 더 구체적으로 쓰기 위해 두 scheme $R, U$와 이들 사이의 두 morphism $f,g:R\rightarrow U$가 주어졌다 하자. 만일 임의의 scheme $T$에 대하여, $(f,g): R(T)\rightarrow U(T)\times U(T)$가 injective이고, 그 image가 $U(T)$ 위에 equivalence relation을 정의하면 우리는 이 데이터 $R\rightrightarrows U$이 scheme들 사이의 equivalence relation이라 부른다. 이제 $R=U\times_F U$로 두고 $f=\pr_1$, $g=\pr_2$이라 두면, 우선 첫째 조건에 의해 $R$은 scheme이며, $R(T)$의 원소는 $F(T)$에서 같은 image를 갖는 두 점 $u_1,u_2\in U(T)$의 쌍으로, 이 데이터 $R\rightrightarrows U$은 scheme들의 동치관계이다. 또, $f,g$는 $U\rightarrow F$의 base change이므로 étale morphism이다. 이로부터 $U$는 $F$를 덮는 scheme chart를 제공하고, $R$은 이 chart의 중복을 어떻게 식별해야 하는지를 기록하는 것이며, 이로부터 $F$는 sheaf quotient $U/R$로 복원된다. 국소적으로는 임의의 scheme $T$와 점 $x\in F(T)$에 대하여 $U\rightarrow F$를 $x:T\rightarrow F$를 따라 base change하면 étale surjection $U\times_F T\rightarrow T$을 얻고, 이로부터 $F$의 어떠한 étale covering $\{T_i\rightarrow T\}$이 존재하여, 이 위에서 각 $x\vert_{T_i}$가 $U(T_i)$의 점으로 lift되도록 할 수 있다. 이런 의미에서 $F$는 $U$로 étale-locally 덮이며, 그 overlap을 $R$이 기록하는 것이다. 

정의에 의해 모든 scheme은 algebraic space이므로 이는 scheme의 일반화이며, 이들은 normal 혹은 quasi-projective 등의 가정 아래에서 흔히 일치한다. 우리는 이에 대한 이론을 자세히 전개하는 대신, 이것이 scheme의 약한 일반화라는 정도만 기억하고 우리의 원래 목표로 돌아가기로 한다. 

## 표현가능 사상

이제 stack morphism $f:\mathcal{X}\rightarrow\mathcal{Y}$에 scheme morphism의 성질을 부여하려면, 먼저 $\mathcal{Y}$의 임의의 scheme-valued point $y: T\rightarrow \mathcal{Y}$에서 $f$를 base change한 다음의 morphism

$$f_T: \mathcal{X}\times_\mathcal{Y}T\rightarrow T$$

가 위에서 설명한 것과 같이 algebraic space들 사이의 morphism으로 나타나야 한다. 이제 모든 $y$에 대하여 위의 식의 source $\mathcal{X}\times_\mathcal{Y}T$가 algebraic space일 것을 요구하는 것이 stack morphism $f$의 *representability<sub>표현가능성</sub>*이다. 

Algebraic space는 scheme의 약한 일반화로서, scheme morphism의 성질 $P$를 algebraic space의 성질 $P$로 옮겨오는 것이 대부분 가능하다. 이제 이 성질 $P$를 stack으로 올리기 위해서는 다음의 두 가지 성질이 필요하다. 

1. 성질 $P$는 임의의 base change에 대하여 닫혀있어야 한다. 
2. 성질 $P$는 fppf-local on target이다. 

첫째 조건은 자명한 것이며, 둘째 조건은 우리가 관심을 갖는 대상들이 fppf-local하게 쓰인다는 점에서 요구되는 성질로, 앞으로 우리는 일반적인 맥락에서 *stack*이라 하면 fppf site (링크) $(\Sch, \fppf)$ 위에서의 stack인 것으로 생각한다. 임의의 scheme $S$는 항상 stack으로 취급할 수 있으므로, stack $\mathcal{X}$가 $S$-stack이라는 것이 말이 되며, $S$-stack들 사이의 morphism이나 이 위의 두 대상의 곱 $\mathcal{X}\times_X \mathcal{Y}$ 등이 잘 정의되고, 이것이 fppf site $(\Sch_{/S}, \fppf)$ 위에 정의된 stack과 정의에 의해 같은 것임을 알 수 있다. 

$\fppf$ site의 필요성은 이미 scheme 단계에서부터 어느정도 예고되었다. 예를 들어 [\[스킴\] §군 스킴, ⁋예시 15](/ko/math/scheme_theory/group_schemes#ex15)에서 $\mathbb{G}_m$-torsor는 Zariski-locally trivial하였지만, 이미 해당 예시에서 이것이 Hilbert theorem 90에 의한 특수한 현상임을 언급하였으며, 실제로 해당 예시의 첫째 예시인 $\mathbb{Z}/2$-torsor $\Spec\mathbb{C}\rightarrow\Spec\mathbb{R}$는 fppf-locally trivial하면서도 Zariski-locally trivial하지 않았다. 이러한 이유로 stack을 $\fppf$ site 위에서 정의된 것으로 약속한다면, stack의 object를 fppf covering 위에서 local trivialization한 뒤 $f_T$의 성질을 검사하고 그 결과를 $T$로 내리려면, $P$가 fppf-local on target이어야 한다.

::: 정의 4
위의 조건을 만족하는 algebraic space의 morphism에 대한 성질 $P$가 주어졌다고 하자. Representable stack morphism $f:\mathcal{X}\rightarrow\mathcal{Y}$가 *성질 $P$를 가진다*는 것은, 임의의 scheme $T$와 morphism $y:T\rightarrow\mathcal{Y}$에 대하여 base change $f_T:\mathcal{X}\times_\mathcal{Y}T\rightarrow T$가 algebraic space의 morphism으로서 $P$를 갖는 것이다.
:::

$P$가 될 수 있는 성질의 목록은 다음과 같다.

> open embedding, closed embedding, quasi-compact, quasi-separated, affine, finite, integral, locally of finite type, finite type, quasi-finite, locally of finite presentation, finite presentation, flat, smooth, unramified, étale, surjective, separated, proper, ...

중요한 예외는 projective와 quasi-projective이다. 이들은 base change에 대하여 닫혀있고 algebraic space의 morphism에 대해서도 정의되지만, Zariski-local on target조차 아니므로 위의 fppf descent를 통한 방법으로는 stack morphism의 성질로 올릴 수 없고, relative ample line bundle의 존재나 projective bundle로의 immersion 등을 통해 별도로 정의하여야 한다.

Algebraic space의 정의에서 diagonal morphism의 representability가 두 점이 일치하는 locus를 scheme으로 다룰 수 있게 하였듯, stack에서도 diagonal morphism은 두 object 사이의 isomorphism을 기하적으로 다루는 역할을 한다. Scheme의 diagonal morphism $\Delta:X\rightarrow X\times_S X$을 두 morphism $a,b:T\rightarrow X$을 따라 base change하면 둘이 일치하는 locus $\Eq(a,b)$이 나온다. Stack에서는 일치 대신 isomorphism을 기억하므로, 그 자리에 $\rIsom$이 등장한다.

::: 명제 5
$S$-stack $\mathcal{X}$, $S$-scheme $T$와 두 object $x_1,x_2\in\mathcal{X}(T)$에 대하여, discrete CFG $\rIsom_T(x_1,x_2)$와 diagonal morphism $\Delta: \mathcal{X}\rightarrow\mathcal{X}\times_S\mathcal{X}$가 정의하는 fiber product 사이의 natural equivalence

$$\mathcal{X}\times_{\mathcal{X}\times_S \mathcal{X}}T\simeq \rIsom_T(x_1,x_2)$$

가 있다. 특히 다음 세 조건은 동치이다.

1. $\Delta:\mathcal{X}\rightarrow\mathcal{X}\times_S\mathcal{X}$이 representable하다.
2. 임의의 $S$-scheme $T$와 $x_1,x_2\in\mathcal{X}(T)$에 대하여 $\rIsom_T(x_1,x_2)$가 algebraic space이다.
3. 임의의 $S$-scheme $T$와 $x\in\mathcal{X}(T)$에 대하여 morphism $x:T\rightarrow\mathcal{X}$이 representable하다.
:::
::: 증명
우선 [정의 1](#def1)을 적용하면 $\mathcal{X}\times_{\mathcal{X}\times_S\mathcal{X}}T$의 $T'$-object는 $S$-morphism들

$$t: T' \rightarrow T, \qquad x: T'\rightarrow \mathcal{X}$$

그리고 $\mathcal{X}\times_S\mathcal{X}$에서의 isomorphism $\alpha: \Delta\circ x\rightarrow (x_1, x_2)\circ t$에 의해 정의되는 것이며, 이 때 fiber product의 base scheme이 $\mathcal{X}\times_S\mathcal{X}$이므로 $\alpha$는 더 명시적으로 두 개의 isomorphism 

$$a: x\rightarrow x_1\circ t=x_1\vert_{T'}, \qquad b:x\rightarrow x_2\circ t=x_2\vert_{T'}$$

에 대하여 $\alpha=(a,b)$의 꼴로 쓸 수 있다. 이제 이 데이터 $(t,x,a,b)$를 $b\circ a^{-1}:x_1\vert_{T'}\xrightarrow{\sim}x_2\vert_{T'}$로 보내면 이것이 functor

$$\mathcal{X}\times_{\mathcal{X}\times_S \mathcal{X}}T\rightarrow \rIsom_T(x_1,x_2)$$

를 정의한다.

우리 주장은 이 functor가 natural equivalence라는 것이다. 이를 확인하기 위해 우선 $\mathcal{X}\times_{\mathcal{X}\times_S \mathcal{X}}T$의 두 데이터 $(t,x,a,b)$와 $(t',x',a',b')$가 $\rIsom_T(x_1,x_2)$의 같은 object로 보내진다고 가정하자. 이 CFG는 discrete이므로 $t=t'$이고

$$b\circ a^{-1}=b'\circ(a')^{-1}$$

이다. 이제 isomorphism

$$c=(a')^{-1}\circ a:x\xrightarrow{\sim}x'$$

을 생각하면 $a'\circ c=a$이고, 위의 등식으로부터

$$b'\circ c=b'\circ(a')^{-1}\circ a=b\circ a^{-1}\circ a=b$$

을 얻는다. 따라서 $c$는 $\id_t$와 함께 fiber product의 compatibility condition을 만족하므로 $(t,x,a,b)$에서 $(t,x',a',b')$로의 morphism을 정의한다. 거꾸로 그러한 morphism은 $a'\circ c=a$를 만족해야 하므로 반드시 $c=(a')^{-1}\circ a$이며, 따라서 유일하다. 즉, 이 functor는 fully faithful하다. 한편 임의의 $\beta:x_1\vert_{T'}\xrightarrow{\sim}x_2\vert_{T'}$는 $(t,x,a,b)=(t,x_1\vert_{T'},\id,\beta)$에서 오므로 이 functor는 essentially surjective이다. 이 구성이 pullback과 호환되므로 위의 natural equivalence를 얻는다. 

이제 첫째 조건과 둘째 조건이 동치임은 위에서 만든 natural equivalence에 의해 자명하다. 이제 첫째 조건을 가정하고 셋째 조건을 보인다. 이를 위해 첫째 조건을 가정하고 $S$-scheme들로부터의 두 morphism $x:T\rightarrow\mathcal{X}$과 $y:T'\rightarrow\mathcal{X}$을 잡자. 그럼 isomorphism

$$T\times_\mathcal{X}T'\cong(T\times_S T')\times_{\mathcal{X}\times_S\mathcal{X},\Delta}\mathcal{X}$$

에서 우변은 $\Delta$의 base change이므로 algebraic space이다. 따라서 $x:T\rightarrow\mathcal{X}$이 representable하고 셋째 조건이 성립한다.

마지막으로 셋째 조건을 가정하고 들째 조건을 보인다. 우선 임의의 $x_1,x_2\in\mathcal{X}(T)$에 대하여, $x_1:T\rightarrow\mathcal{X}$이 representable하므로 $T\times_{x_1,\mathcal{X},x_2}T$은 algebraic space이다. 이 fiber product에서는 $T$로 가는 두 morphism이 서로 다를 수 있는데, diagonal morphism $\Delta_T:T\rightarrow T\times_S T$을 따라 base change하면 이들을 같게 제한한다. 따라서 natural isomorphism

$$\rIsom_T(x_1,x_2)\cong(T\times_{x_1,\mathcal{X},x_2}T)\times_{T\times_S T,\Delta_T}T$$

을 얻고, 우변은 algebraic space의 base change이므로 algebraic space이다. 따라서 둘째 조건이 성립한다.
:::

Isomorphism sheaf $\rIsom_T(x_1, x_2)$에서 특히 $x_1=x_2=x$인 경우, 한 object $x\in\mathcal{X}(T)$에 대하여 group sheaf $\rAut_T(x)=\rIsom_T(x,x)$를 $x$의 *stabilizer*라 부른다. 이들 stabilizer들을 $\mathcal{X}$ 위에서 한꺼번에 모은 것이 다음의 $2$-fiber product

$$\mathcal{I}_\mathcal{X}:=\mathcal{X}\times_{\mathcal{X}\times_S\mathcal{X}}\mathcal{X}$$

으로 정의되는 *inertia stack*이다. 즉, inertia stack의 $T$-object는 쌍 $(x,\alpha)$, $x\in\mathcal{X}(T)$, $\alpha\in\rAut_T(x)$이며, projection $\mathcal{I}_\mathcal{X}\rightarrow\mathcal{X}$의 $x$ 위의 fiber가 바로 $\rAut_T(x)$이다.

## Algebraic stack과 Deligne–Mumford stack

[정의 3](#def3)에서 우리는 set-valued sheaf $F$의 diagonal이 scheme에 의해 representable하고, scheme으로부터의 étale surjective atlas $U\rightarrow F$가 존재하는 $(\Sch, \et)$ 위의 sheaf를 algebraic space로 정의하였다. 이 정의를 한 층 올려 fppf site 위의 groupoid-valued stack $\mathcal{X}$을 생각하고, 예고한대로 diagonal이 scheme 대신 algebraic space에 의해 representable할 것을 요구하면 *Deligne–Mumford stack*의 정의가 된다.

::: 정의 6
Site $(\Sch_{/S}, \fppf)$ 위의 stack $\mathcal{X}$ (base scheme $S$ 위)이 *Deligne–Mumford stack<sub>들리뉴-멈퍼드 스택</sub>* (간단히 *DM stack*)이라는 것은 다음 두 조건을 만족하는 것이다.

1. (Representability) Diagonal morphism $\Delta:\mathcal{X} \rightarrow \mathcal{X}\times_S \mathcal{X}$이 algebraic space에 의해 representable하다.
2. (Étale atlas) Scheme $U$과 representable étale morphism $\pi: U \rightarrow \mathcal{X}$이 존재하며, 이 morphism은 sheaf의 epimorphism (곧 surjective)이다. 이 $\pi$를 $\mathcal{X}$의 *atlas<sub>아틀라스</sub>* (또는 *presentation*)라 부른다.

더 일반적으로, 조건 2에서 étale morphism 대신 smooth morphism을 허용하여 얻어지는 stack을 *algebraic stack* 또는 *Artin stack<sub>아틴 스택</sub>*이라 부른다. ([\[스킴\] §매끄러운 사상과 에탈 사상, ⁋정의 11](/ko/math/scheme_theory/smooth_and_etale_morphisms#def11))
:::

Atlas는 algebraic space에서와 마찬가지로 stack $\mathcal{X}$을 scheme $U$로 덮는 방법이다. DM stack에서는 étale atlas를 사용하므로 그 geometric fiber들이 discrete하고 relative dimension이 $0$이다. Artin stack에서는 smooth atlas를 허용하며, smooth fiber가 양의 차원을 가질 수 있다는 의미에서 $\mathcal{X}$을 더 두꺼운 scheme으로 덮는다.

만일 stack의 atlas $\pi:U\rightarrow\mathcal{X}$의 relative dimension이 $d$이면 $\dim\mathcal{X}=\dim U-d$로 정의하며, 이는 atlas의 선택에 의존하지 않는다. DM stack에서는 $d=0$이고 stabilizer가 unramified하므로 automorphism의 infinitesimal direction이 없다. 반면 Artin stack에서는 $d$가 양수일 수 있고, atlas fiber의 양의 차원에는 각 점의 positive-dimensional stabilizer가 주는 automorphism direction도 함께 담길 수 있다. 이런 의미에서 DM stack은 점들이 discrete stabilizer만큼 포개지는 경우를, Artin stack은 양의 차원의 automorphism family를 따라 포개지는 경우까지 허용한다.

엄밀하게는, algebraic stack $\mathcal{X}$에 대하여 다음 세 조건이 동치이다.

1. $\mathcal{X}$이 DM stack이다.
2. Diagonal morphism $\Delta:\mathcal{X} \rightarrow \mathcal{X}\times_S \mathcal{X}$이 unramified하다. ([\[스킴\] §매끄러운 사상과 에탈 사상, ⁋정의 9](/ko/math/scheme_theory/smooth_and_etale_morphisms#def9))
3. 모든 geometric point $x:\Spec\mathbb{K}\rightarrow\mathcal{X}$의 stabilizer $\rAut_\mathbb{K}(x)$가 $\mathbb{K}$ 위에서 unramified하다.

통상적인 finite-type, quasi-separated 상황에서는 이 stabilizer들이 finite type이고 quasi-compact이므로, DM 조건 아래에서 finite étale group scheme이 된다. 특히 characteristic $0$에서는 모든 finite group scheme이 étale이므로, finite stabilizer를 갖는다는 조건만으로 DM 조건이 따라온다.

## Quotient stack의 구성

우리는 앞선 섹션의 [정의 6](#def6)에서 DM stack을 정의하고, 이것이 algebraic space와 갖는 공통점을 강조했으나, 이것을 실제로 stack으로 만드는 중요한 차이, 즉 이것이 $\Grpd$-valued functor라는 사실은 아직 충분히 짚고 넘어가지 않았다. 이 차이가 가장 명확하게 드러나는 것은 (étale) atlas이다. 정의에 의해 algebraic space 혹은 DM stack의 atlas는 scheme $U$에서 해당 대상으로 가는 surjective morphism이 된다. 그럼 이 morphism이 동일시하는 $U$의 점들을 같은 것으로 취급하여 $U$의 quotient space를 생각하면 이 대상이 되어야 할 것이다. 

차이는 이 <em-ko>같은 것으로 취급</em-ko>하는 부분에 있다. Algebraic space는 $\Set$-valued functor로서 두 점이 같은 것이 정말로 같은 것이지만, DM stack에서는 $\Grpd$-valued functor로서 두 점을 잇는 isomorphism까지 기억하여 이들을 구분한다. 이를 더 명시적으로 쓰자면, 우리는 algebraic space에서는 다음의 식

$$R(T)=(U\times_X U)(T)=\{(f,g)\in U(T)\times U(T)\mid p\circ  f=p\circ g\}$$

을 통해 정의되는 $R$을 atlas $p: U\rightarrow X$가 정의하는 동치관계로 생각하고, 이것으로 $U$를 나눈 것을 $X$로 생각하게 된다. 이 때 $R$은 두 scheme의 fiber product로서 scheme인 반면, DM stack을 정의하는 atlas의 경우 이 $R$이 $U\times_\mathcal{X} U$, 즉 stack이 되므로 nontrivial한 automorphism이 살아있게 된다. 

이렇게 nontrivial한 automorphism을 각 $T$-point에서 담는 group이 stabilizer $\rAut_T(x)$이므로, 우리는 거꾸로 어떤 $S$-scheme $U$ 위에 group scheme $G$가 작용할 때 이 action으로 $U$를 나누어 stack을 얻어낼 생각을 할 수 있다. 우리는 이러한 대상을 이미 scheme에서도, stack에서도 정의하였으며 ([§스택, ⁋정의 17](/ko/math/stacks/fibered_categories_and_stacks#def17)) 이러한 상황을 다음과 같이 정의할 수 있다. 

::: 정의 7
위의 자료에 대하여 *quotient stack<sub>몫 스택</sub>* $[U/G]$은 다음 CFG이다. $T\in \Sch/S$ 위의 대상은 쌍 $(P, \varphi)$로서

1. $P \rightarrow T$은 $G$-torsor(principal $G$-bundle)이고,
2. $\varphi:P\rightarrow U$는 $G$-equivariant morphism, 곧 $\varphi(g\cdot p)=g\cdot\varphi(p)$을 만족하는 morphism

이다. $(P,\varphi)$에서 $(P',\varphi')$로의 morphism은 $G$-torsor의 morphism $\psi:P\rightarrow P'$으로서 $\varphi'\circ\psi=\varphi$인 것이다 (이러한 $\psi$은 자동으로 isomorphism이다). Base change에 의한 pullback이 cartesian morphism을 주어 사영 $(P,\varphi)\mapsto T$이 이를 CFG로 만든다. $U=S$에 $G$이 자명하게 작용하는 경우 $[S/G]=\bB G$이며, 이를 *classifying stack*이라 부른다.
:::

$[U/G]$의 한 점 $(P,\varphi)$은 "$T$ 위에서 $G$만큼 비틀린 채 $U$로 사상하는 data"이다. Torsor $P$이 자명한 경우, 곧 $P=G\times_ST$(left translation action)인 경우 equivariant morphism $\varphi:G\times_ST\rightarrow U$는 $\varphi(g,t)=g\cdot\varphi(e,t)$으로 단위절단에서의 값 $a:=\varphi(e,-):T\rightarrow U$에 의해 완전히 결정된다. 즉 자명한 torsor 위의 자료는 단순히 $U$의 한 점 $a\in U(T)$과 같다. 이 관찰이 atlas의 출발점이다. 한편 $\bB G$은 $U=S$라서 equivariant morphism이 유일하므로 $\bB G(T)$은 정확히 $T$ 위의 $G$-torsor들의 groupoid이고, 그 automorphism은 $G(T)$이다. $\bB G$은 고전적으로 위상공간의 classifying space $BG$이 맡던 역할, 곧 $G$-bundle을 분류하는 보편 대상의 역할을 대수기하에서 수행한다.

[§스택, ⁋정리 18](/ko/math/stacks/fibered_categories_and_stacks#thm18)에서 $\bB\mathbb{G}_m$이 stack임을 line bundle의 descent로 보았듯, $[U/G]$이 stack인 것은 torsor와 equivariant morphism이 모두 fppf covering에 대한 effective descent를 만족하기 때문이다. Torsor는 fppf-locally trivial하고, equivariant morphism은 $U$로의 morphism이므로 representable sheaf의 section으로서 붙는다. 우리는 이 stack 성질을 전제하고 ([명제 2](#prop2)과 같은 성분별 descent 논증이 그대로 적용된다) 곧바로 대수성으로 나아간다. 먼저 atlas를 구성한다.

::: 명제 8
Morphism $\pi:U\rightarrow[U/G]$을, $T$-점 $a\in U(T)$에 자명한 torsor와 그것이 결정하는 equivariant morphism을 대응시키는 것으로 정의하면, 곧

$$\pi(a)=\bigl(G\times_S T,\ \varphi_a\bigr),\qquad \varphi_a(g, t)=g\cdot a(t),$$

이는 stack의 morphism이며 sheaf의 epimorphism, 곧 전사이다.
:::
::: 증명
$\pi$이 함자적임은 $a$의 base change가 자명 torsor의 base change와 호환됨에서 따른다. $\pi$이 전사임을 본다. 임의의 $(P,\varphi)\in[U/G](T)$에 대하여, $P$은 $G$-torsor이므로 [§스택, ⁋정의 17](/ko/math/stacks/fibered_categories_and_stacks#def17)에 의해 fppf covering $\{T_i\rightarrow T\}$ 위에서 자명해진다. 곧 각 $T_i$ 위에서 section $s_i\in P(T_i)$이 존재하여 $g\mapsto g\cdot s_i$가 $G\times_ST_i\xrightarrow{\sim}P\vert_{T_i}$을 준다. 이 trivialization 아래 $(P,\varphi)\vert_{T_i}$는 $a_i:=\varphi(s_i)\in U(T_i)$가 결정하는 $\pi(a_i)$과 isomorphic하다. 따라서 $(P,\varphi)$은 covering $\{T_i\rightarrow T\}$ 위에서 $\pi$의 image에 locally 들어가며, 이는 sheaf의 epimorphism의 정의 그대로이다. 그러므로 $\pi$은 전사이다.
:::

[명제 8](#prop8)의 $\pi$이 atlas의 후보이다. 그것이 representable하고 smooth함을 보이려면 그 base change를 계산해야 하는데, 가장 중요한 것이 $\pi$ 자신을 따른 base change, 곧 $U\times_{[U/G]}U$이다. 이 계산이 quotient stack의 groupoid presentation을 드러낸다.

::: 명제 9
[명제 8](#prop8)의 atlas $\pi:U\rightarrow[U/G]$에 대하여 표준적인 동형

$$U\times_{[U/G]}U\cong G\times_SU$$

이 있으며, 두 사영 $\pr_1,\pr_2:U\times_{[U/G]}U\rightarrow U$는 이 동형 아래 각각 작용 $\sigma:(g,u)\mapsto g\cdot u$와 사영 $(g,u)\mapsto u$에 대응한다. 따라서 $[U/G]$은 groupoid presentation $G\times_SU\rightrightarrows U$를 가진다.
:::
::: 증명
[정의 1](#def1)에 의해 $(U\times_{[U/G]}U)(T)$의 대상은 삼중쌍 $(a,b,\psi)$로서 $a,b\in U(T)$이고 $\psi:\pi(a)\xrightarrow{\sim}\pi(b)$은 $[U/G](T)$의 isomorphism이다. $\pi(a)=(G_T,\varphi_a)$, $\pi(b)=(G_T,\varphi_b)$ ($G_T=G\times_ST$)이므로 $\psi$은 자명 torsor $G_T$의 automorphism으로서 $\varphi_b\circ\psi=\varphi_a$을 만족하는 것이다. Left translation torsor $G_T$의 좌-equivariant automorphism은 정확히 right translation $\psi_g:h\mapsto hg$ ($g\in G(T)$)이며, 이로써 $\psi\leftrightarrow g\in G(T)$의 대응을 얻는다. ([§스택, ⁋정의 17](/ko/math/stacks/fibered_categories_and_stacks#def17)) 조건 $\varphi_b\circ\psi_g=\varphi_a$은 모든 $(h,t)$에 대하여

$$\varphi_b(hg, t)=hg\cdot b(t)\overset{!}{=}h\cdot a(t)=\varphi_a(h, t)$$

을 요구하고, $h=e$을 대입하면 $g\cdot b(t)=a(t)$, 곧 $a=g\cdot b$(작용 $\sigma$의 의미)과 동치이다 (역으로 이 등식이면 모든 $h$에 대해 성립한다). 그러므로 $(a,b,\psi)$은 쌍 $(g,b)\in(G\times_SU)(T)$($a=g\cdot b$으로 결정됨)과 일대일로 대응하며, 이 대응은 $T$에 대해 함자적이고 morphism과 호환된다. 따라서 $U\times_{[U/G]}U\cong G\times_SU$이다.

이 동형 아래 $\pr_2(a,b,\psi)=b$은 $(g,b)\mapsto b$, 곧 사영이고, $\pr_1(a,b,\psi)=a=g\cdot b$은 $(g,b)\mapsto g\cdot b$, 곧 작용 $\sigma$이다. 두 morphism $\sigma,\pr_2:G\times_SU\rightrightarrows U$가 $[U/G]$의 groupoid presentation을 이룬다.
:::

{% diagram Math/Stacks/Algebraic_Stacks-1.svg width="10.10em" alt="atlas의 base change" %}

[명제 9](#prop9)는 $[U/G]$을 작용 groupoid의 stack quotient로 다시 보여준다. Scheme의 groupoid $G\times_SU\rightrightarrows U$ (source는 사영, target은 작용)은 orbit과 stabilizer를 함께 기록하며, $[U/G]$은 이 groupoid를 stack 차원에서 나눈 것이다. 일반적으로 source와 target이 smooth한 groupoid object $R\rightrightarrows U$로부터 algebraic stack $[U/R]$을 얻는데, quotient stack은 $R=G\times_SU$인 특수한 경우이다. 이제 이 presentation으로부터 $[U/G]$의 대수성을 끌어낸다.

## Quotient stack의 대수성

::: 정리 10
$G$이 base scheme $S$ 위의 flat·separated·smooth group scheme이고 $U$가 $S$-scheme으로서 $G$의 작용을 받는다 하자. 그럼 quotient stack $[U/G]$은 algebraic stack이며, [명제 8](#prop8)의 $\pi:U\rightarrow[U/G]$가 atlas이다. 나아가 다음이 성립한다.

1. $U$가 $S$ 위에서 separated이면 $[U/G]$의 diagonal이 separated morphism으로 representable하다. 나아가 $[U/G]$이 separated인 것은 작용 morphism $G\times_SU\rightarrow U\times_SU$, $(g,u)\mapsto(g\cdot u,u)$가 proper인 것과 동치이다.
2. 모든 geometric point의 stabilizer가 finite étale이면 (가령 $G$이 finite étale하거나, characteristic $0$에서 작용이 finite stabilizer를 가지면) $[U/G]$은 DM stack이다.
:::
::: 증명
**Diagonal의 representability.** [명제 5](#prop5)에 의해 임의의 scheme $T$과 $(P,\varphi),(P',\varphi')\in[U/G](T)$에 대하여 $\rIsom_T((P,\varphi),(P',\varphi'))$이 representable함을 보이면 된다. $P,P'$이 자명해지는 fppf covering 위에서 이 sheaf는 $g\cdot a'=a$을 만족하는 $g\in G_T$들의 모임, 곧 morphism $(g\mapsto(g\cdot a',a)):G_T\rightarrow U\times_SU$와 diagonal $U\rightarrow U\times_SU$의 fiber product로 represent된다. 이 local presentation들은 descent datum을 따라 붙어 algebraic space를 이룬다. $U$가 separated이면 diagonal이 closed embedding이고 $G_T\rightarrow T$도 separated이므로 $\rIsom\rightarrow T$은 separated morphism이다.

**Smooth atlas.** [명제 8](#prop8)에 의해 $\pi:U\rightarrow[U/G]$은 전사이고 [명제 5](#prop5)에 의해 representable하다. 임의의 $T\rightarrow[U/G]$에 대한 base change $U\times_{[U/G]}T\rightarrow T$은 $P$가 자명해지는 fppf covering 위에서 [명제 9](#prop9)에 의해 사영 $(G\times_SU)\times_UT_i\rightarrow T_i$와 isomorphic하다. $G$가 $S$ 위에서 smooth하므로 이 사영은 smooth surjective이고, smoothness와 surjectivity의 fppf-locality에 의해 $\pi$은 smooth atlas이다. 이로써 $[U/G]$은 algebraic stack이다.

**DM 판정.** 모든 geometric point의 stabilizer가 finite étale하면 앞서 본 판정 조건에 의해 $[U/G]$은 DM stack이다. 특히 $G$이 finite étale group scheme이면 $\pi:U\rightarrow[U/G]$ 자체가 relative dimension $0$인 étale morphism이므로 $U$가 곧 étale atlas가 된다.
:::

[정리 10](#thm10)은 group scheme의 작용이 자동으로 algebraic stack을 낳음을 보장한다. Diagonal의 representability는 isomorphism 조건이 $G$ 안에서 algebraic subspace로 잘려 나옴에서, atlas의 smoothness는 $\pi$의 base change가 사영 $G\times_SU\rightarrow U$라는 점에서 따라온다. 이 두 사실은 모두 [명제 9](#prop9)의 groupoid presentation으로 환원된다.

순진한 quotient와의 관계는 작용의 자유로움에 달려 있다. 만일 $G$이 $U$에 자유롭게(stabilizer가 자명하게) 작용하면 [명제 9](#prop9)의 $\rIsom$이 많아야 한원소가 되어 $[U/G]$의 diagonal이 monomorphism이고, 이때 $[U/G]$은 fiber에 automorphism이 없는 stack, 곧 algebraic space가 되어 $G\times_SU\rightrightarrows U$의 fppf quotient인 *coarse quotient* $U/G$와 일치한다. 작용이 자유롭지 않으면 각 점에 stabilizer가 남아 $[U/G]$은 진정한 stack이 되며, 이때에도 점의 isomorphism class를 뭉갠 coarse moduli space $U/G$ (존재할 경우)로 가는 자연스러운 morphism $[U/G]\rightarrow U/G$가 있으나 이는 stabilizer 정보를 잃는다. 다음 절의 $[\mathbb{A}^1/\mathbb{G}_m]$이 이 손실을 선명히 보여준다.

## 예시

가장 기본적인 예는 $U=S$인 classifying stack이다. 이는 [§스택, ⁋정의 17](/ko/math/stacks/fibered_categories_and_stacks#def17)에서 도입한 $\bB G$이 사실 algebraic stack임을 [정리 10](#thm10)으로 확인하는 것이다.

::: 예시 11 ($\bB\mathbb{G}_m$과 $\bB(\mathbb{Z}/n)$)
Base를 field $\mathbb{K}$로 둔다.

1. $\bB\mathbb{G}_m=[\Spec \mathbb{K}/\mathbb{G}_m]$은 algebraic stack이다. $\mathbb{G}_m$이 affine·smooth하므로 ([\[스킴\] §군 스킴, §§군 스킴](/ko/math/scheme_theory/group_schemes#군-스킴)) [정리 10](#thm10)이 적용되고, atlas는 $\Spec \mathbb{K} \rightarrow \bB\mathbb{G}_m$이며 그 base change는 $\mathbb{G}_m \rightrightarrows \Spec \mathbb{K}$이다. $\bB\mathbb{G}_m(T)$은 $T$ 위의 line bundle들의 groupoid이고 ([§스택, ⁋정리 18](/ko/math/stacks/fibered_categories_and_stacks#thm18)), 한 점의 stabilizer는 $\mathbb{G}_m$이다. Stabilizer가 $1$차원이라 infinitesimal deformation을 가지므로 $\bB\mathbb{G}_m$은 DM이 아닌 Artin stack이며, 그 차원은 $\dim \Spec \mathbb{K}-\dim \mathbb{G}_m=0-1=-1$이다. 음의 차원은 stabilizer가 점보다 "더 큰" algebraic stack의 특징이다.

2. $\mathbb{Z}/n$을 상수 group scheme으로 볼 때 $\bB(\mathbb{Z}/n)=[\Spec \mathbb{K}/(\mathbb{Z}/n)]$은 DM stack이다. $\mathbb{Z}/n$은 유한 étale하므로 ([\[스킴\] §매끄러운 사상과 에탈 사상, ⁋예시 14](/ko/math/scheme_theory/smooth_and_etale_morphisms#ex14)에서 분리 확대가 étale함과 같은 이유로 상수군은 étale하다) atlas $\Spec \mathbb{K} \rightarrow \bB(\mathbb{Z}/n)$이 étale 전사이고 ([정리 10](#thm10)의 DM 판정), 그 base change는 $n$개의 점의 disjoint union $\mathbb{Z}/n\times \Spec \mathbb{K}\rightrightarrows \Spec \mathbb{K}$이다. $\bB(\mathbb{Z}/n)(T)$은 $T$ 위의 $\mathbb{Z}/n$-torsor, 곧 degree $n$의 cyclic étale covering의 groupoid이며, 한 점의 stabilizer는 finite group $\mathbb{Z}/n$이다. $\ch\mathbb{K}\nmid n$이면 $\mu_n$ 또한 유한 étale하여 $\bB(\mathbb{Z}/n)$과 $\bB\mu_n$이 모두 DM이지만, $\ch\mathbb{K}\mid n$이면 $\mu_n$이 비환원이 되어 $\bB\mu_n$은 (DM이 아닌) Artin stack이 되는 반면 상수군 $\bB(\mathbb{Z}/n)$은 여전히 DM이다. 이 분리가 characteristic $p$에서 étale·infinitesimal stabilizer의 차이를 드러낸다.
:::

다음은 stabilizer가 점마다 도약하는 작용의 표준적인 예로, coarse quotient가 잃어버리는 정보를 stack이 어떻게 보존하는지를 보여준다.

::: 예시 12 ($[\mathbb{A}^1/\mathbb{G}_m]$)
Field $\mathbb{K}$ 위에서 $\mathbb{G}_m$이 affine line $\mathbb{A}^1$에 스칼라 배 $t\cdot x=tx$으로 작용한다 하자. 작용의 orbit은 둘뿐이다. 원점 $\{0\}$은 fixed point이라 한 orbit을 이루고, 여집합 $\mathbb{A}^1\setminus\{0\}=\mathbb{G}_m$은 $\mathbb{G}_m$이 단순추이적으로 작용하는 한 orbit이다. 따라서 위상적인 quotient $\mathbb{A}^1/\mathbb{G}_m$은 두 점(열린 orbit과 원점)으로 이루어지며 열린 orbit의 closure가 원점을 포함한다.

Ring의 불변량으로 계산한 categorical quotient, 곧 affine GIT quotient $\Spec(\Gamma(\mathbb{A}^1, \mathcal{O})^{\mathbb{G}_m})$을 취하면 $\mathbb{K}[\x]^{\mathbb{G}_m}=\mathbb{K}$이므로 ([§Cox 구성과 GIT quotient, ⁋명제 3](/ko/math/toric_geometry/cox_construction#prop3)), 닫히지 않은 궤적을 닫힌 궤적과 구별하지 못하고 한 점 $\Spec \mathbb{K}$으로 뭉개버린다.

반면 quotient stack $[\mathbb{A}^1/\mathbb{G}_m]$은 이 두 orbit의 서로 다른 stabilizer를 모두 온전히 기억한다. [정리 10](#thm10)에 의해 이는 $1$차원 affine scheme $\mathbb{A}^1$을 $1$차원 group $\mathbb{G}_m$으로 나눈 algebraic stack으로, $\dim[\mathbb{A}^1/\mathbb{G}_m]=1-1=0$이다. 그 점은 정확히 두 개이다.

1. 열린 점: 열린 orbit $\mathbb{G}_m\hookrightarrow \mathbb{A}^1$ 위에서 작용이 자유로우므로 $[\mathbb{G}_m/\mathbb{G}_m]\cong \Spec \mathbb{K}$이고, 이는 stabilizer가 자명한 열린 점 $\Spec \mathbb{K}\hookrightarrow [\mathbb{A}^1/\mathbb{G}_m]$을 이룬다.

2. closed point: 원점 $\{0\}=\Spec \mathbb{K}$은 $\mathbb{G}_m$이 자명하게 작용하는 fixed point이므로 $[\{0\}/\mathbb{G}_m]=\bB\mathbb{G}_m$이고, 이는 stabilizer $\mathbb{G}_m$을 가진 closed point이다. ([예시 11](#ex11))

즉 $[\mathbb{A}^1/\mathbb{G}_m]$은 한 개의 열린 점과, 그 closure에 놓인 $\bB\mathbb{G}_m$ 한 점으로 이루어진다. 불변량에 기반한 categorical/GIT quotient $\Spec \mathbb{K}$이 두 점을 하나로 뭉갠 데 반해, stack은 원점의 stabilizer $\mathbb{G}_m$을 closed point에 붙은 $\bB\mathbb{G}_m$으로 정확히 기록한다. Stabilizer가 양의 차원을 가지므로 이 stack은 DM이 아닌 Artin stack이다.
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
