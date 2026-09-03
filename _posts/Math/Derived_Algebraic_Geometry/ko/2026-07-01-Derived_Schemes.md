---
title: "Derived scheme과 derived stack"
description: "Animated 가환환을 이어붙여 derived scheme을 정의하고 그 truncation이 고전적 스킴임을 본 뒤, animated 환 위의 étale 하강 함자로서의 derived stack, 여접 복합체 L_X, quasi-smooth 사상과 유도 올곱이 주는 virtual 구조를 다룬다."
excerpt: "Derived schemes/stacks, the cotangent complex L_X, quasi-smooth maps, and derived fiber products"

categories: [Math / Derived Algebraic Geometry]
permalink: /ko/math/derived_algebraic_geometry/derived_schemes
sidebar: 
    nav: "derived_algebraic_geometry-ko"

date: 2026-07-01
last_modified_at: 2026-07-01
weight: 3

published: false

---

고전적 대수기하는 commutative ring을 국소적 재료로 삼아 affine scheme을 만들고, 이들을 이어붙여 scheme을 세운다. ([\[스킴\] §스킴, ⁋정의 1](/ko/math/scheme_theory/schemes#def1)) 이 이어붙이기가 낳는 가장 중요한 구성 가운데 하나가 올곱, 곧 두 부분다양체의 교차이다. 그러나 고전적 교차는 두 variety가 횡단적(transverse)일 때에만 올바른 답을 준다. 횡단적이지 않으면, 가령 서로 접하거나 예상보다 큰 차원에서 겹치면, scheme으로서의 교차 $\Spec(B\otimes_AC)$는 excess intersection을 놓치고 중복도나 초과 차원을 뭉갠다. 이 결함의 뿌리는 tensor product $\otimes$이 non-exact하다는 데 있으며, 우리는 이미 이를 유도 tensor product $\otimes^{\mathbb{L}}$으로 교정하는 법을 보았다. ([§Simplicial 가환환과 animation, ⁋명제 8](/ko/math/derived_algebraic_geometry/animated_rings#prop8))

이 글의 목표는 그 국소적 교정을 대역적 기하로 승격하는 것이다. 곧 우리는 animated commutative ring을 국소 재료로 삼아 *derived scheme*을 이어붙이고, 그 위에서 올곱이 자동으로 유도 올곱 $X\times_Z^hY$이 되도록 한다. 이렇게 하면 고전적으로 비횡단적이거나 초과 차원인 교차조차 올바른 virtual 차원과 virtual 중복도를 나른다. 이어서 우리는 animated ring 위의 functor로서 derived stack을 정의하고, 여접 복합체 $L_X$와 접복합체 $T_X$를 대역화하며, quasi-smooth morphism과 그것이 주는 virtual 구조를 확립한다. 이하에서 $k$는 field이고, 별다른 언급이 없으면 모든 것은 $k$ 위에서 생각한다. Animated commutative ring들의 $\infty$-범주를 $\operatorname{Ani}=\operatorname{Ani}(\mathrm{CRing}_k)$로 ([§Simplicial 가환환과 animation, ⁋정의 4](/ko/math/derived_algebraic_geometry/animated_rings#def4)), $\infty$-groupoid들, 곧 space들의 $\infty$-범주를 $\mathcal{S}$로 적는다.

## Affine derived scheme과 derived Spec

고전적 affine scheme은 commutative ring $A$에 반변적으로 대응하는 $\Spec A$였고, 그 본질은 점functor $h_{\Spec A}=\Hom_{\Sch}(-,\Spec A)$가 test scheme 위에서 어떻게 보이는가에 있었다. ([\[스킴\] §스킴 사이의 사상, ⁋정의 9](/ko/math/scheme_theory/morphism_of_schemes#def9)) Derived 세계에서 우리는 이 그림을 그대로 옮기되, commutative ring을 animated commutative ring으로, 집합값 functor를 space값 functor로 바꾼다.

::: 정의 1
Animated commutative ring $R\in \operatorname{Ani}$에 대하여, 그 *affine derived scheme* $\Spec R$은 $\operatorname{Ani}^\op$의 대상으로서의 $R$이며, 그 *점functor*는

$$h_{\Spec R}=\operatorname{Map}_{\operatorname{Ani}}(R,-):\operatorname{Ani}\longrightarrow \mathcal{S}$$

로 주어지는, animated ring 위의 space값 functor이다. 여기서 $\operatorname{Map}_{\operatorname{Ani}}(R,S)$은 $\operatorname{Ani}$의 mapping space이다. Affine derived scheme들의 $\infty$-범주를 $\mathrm{dAff}=\operatorname{Ani}^\op$로 적는다.
:::

곧 $\Spec$은 정의상 반변 동치 $\operatorname{Ani}\overset{\sim}{\rightarrow}\mathrm{dAff}^\op$이며, 이는 고전적 반변 동치 "commutative ring $\leftrightarrow$ affine scheme"의 유도 판본이다. 이 대상에 위상공간과 structure sheaf를 입히는 방식은 고전적인 경우와 평행하다. Animated ring $R$의 밑에 깔린 고전적 ring은 $\pi_0(R)$이므로 ([§Simplicial 가환환과 animation, ⁋명제 6](/ko/math/derived_algebraic_geometry/animated_rings#prop6)), $\Spec R$의 밑공간은 고전적 spectrum $\lvert\Spec R\rvert=\Spec \pi_0(R)$의 위상공간으로 두고, 그 위에 각 basic open $D(f)$ ($f\in \pi_0(R)$)에서 localization $R[1/f]$를 값으로 갖는 animated ring의 sheaf $\mathcal{O}_{\Spec R}$을 얹는다.

::: 명제 2
Animated ring $R$에 대하여, 위상공간 $\lvert\Spec R\rvert=\Spec \pi_0(R)$ 위에 animated ring의 sheaf $\mathcal{O}_{\Spec R}$이 존재하여 다음을 만족한다.

1. 각 $f\in \pi_0(R)$에 대하여 $\mathcal{O}_{\Spec R}(D(f))\simeq R[1/f]$이다.
2. 각 $i\geq0$에 대하여 sheaf $\pi_i\mathcal{O}_{\Spec R}$은 고전적 scheme $\Spec \pi_0(R)$ 위의 quasi-coherent sheaf이며, $D(f)$ 위에서 $\pi_i(R)[1/f]=\pi_i(R)\otimes_{\pi_0(R)}\pi_0(R)[1/f]$과 일치한다.

특히 $\pi_0\mathcal{O}_{\Spec R}$은 고전적 structure sheaf $\mathcal{O}_{\Spec \pi_0(R)}$과 같다.
:::
::: 증명
Localization $R\mapsto R[1/f]$는 $\operatorname{Ani}$에서 유도 localization, 곧 $f$의 lift를 주는 $k[\x]\rightarrow R$을 따라 취한 $R\otimes_{k[\x]}^{\mathbb{L}}k[\x,\x^{-1}]$로 잘 정의되는데, $k[\x,\x^{-1}]$이 $k[\x]$ 위에서 flat하므로 유도 tensor product가 higher Tor를 낳지 않아 ([§Simplicial 가환환과 animation, ⁋명제 8](/ko/math/derived_algebraic_geometry/animated_rings#prop8)) $\pi_i(R[1/f])=\pi_i(R)[1/f]$이다. 따라서 $D(f)\mapsto R[1/f]$의 대응은 basic open들의 교차 $D(fg)=D(f)\cap D(g)$ 위에서 정합적이며, 고전적 structure sheaf가 basis 위의 자료로부터 접착되던 것과 같은 논증으로 ([\[스킴\] §스킴, ⁋보조정리 9](/ko/math/scheme_theory/schemes#lem9)) $\lvert\Spec R\rvert$ 위의 sheaf $\mathcal{O}_{\Spec R}$을 준다. 각 $\pi_i(R)$은 $\pi_0(R)$-module이므로 ([§Simplicial 가환환과 animation, ⁋명제 6](/ko/math/derived_algebraic_geometry/animated_rings#prop6)) 그 sheafification $\pi_i\mathcal{O}_{\Spec R}$은 $\Spec \pi_0(R)$ 위의 quasi-coherent sheaf가 된다. $i=0$일 때 $\pi_0(R[1/f])=\pi_0(R)[1/f]$이므로 $\pi_0\mathcal{O}_{\Spec R}$은 고전적 structure sheaf이다.
:::

[명제 2](#prop2)는 affine derived scheme을 국소적으로 ring이 얹힌 공간으로 실현한다. 밑공간과 $\pi_0$-sheaf는 고전적 scheme $\Spec \pi_0(R)$의 그것과 정확히 같고, 새로운 정보는 오직 higher homotopy sheaf $\pi_i\mathcal{O}_{\Spec R}$ ($i\geq1$)에 담긴다. 이 sheaf들이 $\Spec \pi_0(R)$ 위의 quasi-coherent sheaf로서 "고전적 그림자 위에 얹힌 유도 두께"를 이룬다. 이제 이 국소 모형을 이어붙인다.

## Derived scheme과 truncation

고전적 scheme이 affine scheme으로 국소적으로 덮인 locally ringed space였듯, derived scheme은 affine derived scheme으로 국소적으로 덮인, animated ring의 sheaf를 가진 공간이다.

::: 정의 3
*derived scheme<sub>유도 스킴</sub>*이란, 위상공간 $X$와 그 위의 animated commutative ring의 sheaf $\mathcal{O}_X$의 쌍 $(X,\mathcal{O}_X)$으로서, 임의의 점 $x\in X$가 열린근방 $U$를 가져 $(U,\mathcal{O}_X\vert_U)$이 어떤 animated ring $R$의 affine derived scheme $\Spec R$과 동치가 되는 것을 뜻한다. Derived scheme 사이의 morphism은 국소적으로 ring이 얹힌 공간으로서의 morphism, 곧 연속사상 $f:X\rightarrow Y$과 sheaf의 morphism $f^\sharp:\mathcal{O}_Y\rightarrow f_\ast\mathcal{O}_X$의 쌍으로 정의한다. Derived scheme들의 $\infty$-범주를 $\mathrm{dSch}$로 적는다.
:::

정의는 고전적 scheme의 정의와 글자 그대로 평행하며, 유일한 차이는 structure sheaf의 값이 commutative ring이 아니라 animated commutative ring이라는 것이다. ([\[스킴\] §스킴, ⁋정의 1](/ko/math/scheme_theory/schemes#def1)) 국소 모형이 $\Spec R$이므로, derived scheme의 밑공간은 국소적으로 $\Spec \pi_0(R)$의 위상을 가지며, 이들을 이어붙인 고전적 scheme이 자연스럽게 딸려 나온다. 이것을 truncation이라 부른다.

::: 명제 4
Derived scheme $X=(X,\mathcal{O}_X)$에 대하여, 쌍

$$t_0(X)=(X,\pi_0\mathcal{O}_X)$$

은 고전적 scheme이며, 이를 $X$의 *classical truncation<sub>고전적 절단</sub>*이라 부른다. 각 $i\geq1$에 대하여 $\pi_i\mathcal{O}_X$은 $t_0(X)$ 위의 quasi-coherent sheaf이다. 나아가 truncation functor $t_0:\mathrm{dSch}\rightarrow \Sch$은 오른쪽 수반을 가지는 포함

$$\iota:\Sch\hookrightarrow \mathrm{dSch}$$

의 왼쪽 역, 곧 $t_0\circ \iota\simeq \id_{\Sch}$이며, 이 포함은 완전 충실하다. 곧 고전적 scheme은 정확히 $\pi_i\mathcal{O}_X=0$ ($i\geq1$)인 discrete한 derived scheme이다.
:::
::: 증명
국소적으로 $X=\Spec R$이면 [명제 2](#prop2)에 의하여 $(X,\pi_0\mathcal{O}_X)=\Spec \pi_0(R)$이 고전적 affine scheme이고 $\pi_i\mathcal{O}_X$이 그 위의 quasi-coherent sheaf이다. 이 국소 기술이 접착과 호환되므로 $t_0(X)$이 고전적 scheme이 되고 $\pi_i\mathcal{O}_X$이 대역적으로 quasi-coherent sheaf가 된다. 포함 $\iota$은 고전적 ring $A$를 discrete animated ring으로 보아 $\Spec A$을 만드는 것으로, discrete 대상이 $\operatorname{Ani}$에 완전 충실하게 들어가므로 ([§Simplicial 가환환과 animation, ⁋명제 6](/ko/math/derived_algebraic_geometry/animated_rings#prop6)) $\iota$도 완전 충실하다. $t_0(\iota(A))=\pi_0(A)=A$이므로 $t_0\circ \iota\simeq \id$이며, 수반 $\operatorname{Map}_{\mathrm{dSch}}(\iota Y,X)\simeq \operatorname{Map}_{\Sch}(Y,t_0X)$은 discrete 대상으로부터의 사상 공간이 $\pi_0$만 보는 데서 나온다.
:::

[명제 4](#prop4)는 derived scheme이 고전적 scheme의 진정한 확장임을 확립한다. $t_0(X)$은 옛 scheme을 그대로 복원하고, $\pi_{\geq1}\mathcal{O}_X$은 그 위에 얹힌 유도 정보이며, 이 유도 정보가 소멸하는 경우가 정확히 고전적 scheme이다. 앞으로 우리는 discrete derived scheme과 고전적 scheme을 같은 것으로 취급하고, 포함 $\iota$을 표기에서 생략한다. 유도 정보가 실제로 비지 않는 가장 단순한 예가 한 점의 유도 자기교차이다.

::: 예시 5 (유도 점)
$\mathbb{A}^1=\Spec k[\x]$ 안에서 원점 $\{0\}=\Spec k$ ($k=k[\x]/(\x)$)을 자기 자신과 유도적으로 겹친 affine derived scheme

$$Z=\Spec\bigl(k\otimes_{k[\x]}^{\mathbb{L}}k\bigr)$$

을 생각한다. [§Simplicial 가환환과 animation, ⁋예시 9](/ko/math/derived_algebraic_geometry/animated_rings#ex9)의 Koszul 계산에 의하여

$$\pi_n\bigl(k\otimes_{k[\x]}^{\mathbb{L}}k\bigr)=\Tor_n^{k[\x]}(k,k)=\begin{cases}k&n=0,1\\0&n\geq2\end{cases}$$

이다. 따라서 $Z$의 밑공간은 한 점이고, 그 truncation은 고전적 교차 $t_0(Z)=\Spec(k\otimes_{k[\x]}k)=\Spec k$, 곧 원점 한 점이다. 그러나 $\pi_1\mathcal{O}_Z=k\neq0$이라, $Z$은 고전적으로 한 점으로 보이는 자리에 degree $1$의 유도 두께를 하나 얹은, discrete하지 않은 derived scheme이다. 이 $\pi_1$이 affine 직선 안에서 원점을 자기 자신과 겹칠 때의 excess를 기록하며, 뒤에서 이것이 virtual dimension $-1$의 유도 올곱임을 본다. ([예시 18](#ex18)에서 같은 현상을 곡선 차원에서 다시 만난다.)
:::

## Derived stack

Scheme을 점functor로 바라보면 그것은 $\Sch^\op\rightarrow \Set$의 representable functor였고, stack은 그 집합값을 groupoid값으로 넓히고 하강 조건을 부과하여 얻어졌다. Derived 세계에서 우리는 이 두 단계를 동시에 유도화한다. 밑범주를 animated ring으로, 값을 space로 바꾸고, 하강을 $\infty$-범주적 하강, 곧 hyperdescent로 요구하는 것이다.

::: 정의 6
*derived prestack*이란 $\infty$-functor $F:\operatorname{Ani}\rightarrow \mathcal{S}$이다. Derived prestack $F$이 *derived stack<sub>유도 스택</sub>*이라는 것은, animated ring $R$의 임의의 étale covering $\{R\rightarrow R_i\}$과 그 Čech nerve $R_\bullet$에 대하여 자연스러운 morphism

$$F(R)\overset{\sim}{\longrightarrow}\lim_{[n]\in \Delta}F(R_n)$$

이 동치인 것, 곧 $F$이 étale 위상에 대하여 hyperdescent를 만족하는 것을 뜻한다. Derived stack들의 $\infty$-범주를 $\mathrm{dSt}$로 적는다.
:::

여기서 limit은 cosimplicial diagram 위의 homotopy limit이며, 이것이 고전적 stack의 하강 조건, 곧 두 겹 겹침에서의 cocycle 조건을 모든 degree의 겹침으로 정합적으로 확장한 것이다. ([\[Stacks\] §그로텐디크 위상, ⁋예시 8](/ko/math/stacks/grothendieck_topology#ex8)과 [\[Stacks\] §그로텐디크 위상, ⁋정의 9](/ko/math/stacks/grothendieck_topology#def9)의 site 위 sheaf 조건을 space값으로 승격한 것이다.) 값을 truncated groupoid로 제한하고 밑을 discrete ring으로 제한하면 고전적 stack의 정의가 정확히 되살아난다. Fpqc 위상이 subcanonical이어서 representable functor가 모두 sheaf였듯 ([\[Stacks\] §그로텐디크 위상, ⁋정리 14](/ko/math/stacks/grothendieck_topology#thm14)), affine derived scheme의 점functor는 자동으로 derived stack이며, 이로써 $\mathrm{dSch}$이 $\mathrm{dSt}$에 완전 충실하게 들어간다.

::: 명제 7
Yoneda embedding $X\mapsto \operatorname{Map}_{\mathrm{dSch}}(-,X)\vert_{\mathrm{dAff}}$은 완전 충실한 포함 $\mathrm{dSch}\hookrightarrow \mathrm{dSt}$을 주며, derived scheme과 (뒤에서 정의할) geometric derived stack에 대하여 truncation functor $t_0$이 이들의 밑에 깔린 고전적 scheme·algebraic stack을 준다. 특히 고전적 algebraic stack은 discrete ring 위에서 truncated groupoid값을 갖는 derived stack으로서 $\mathrm{dSt}$에 완전 충실하게 들어간다.
:::
::: 증명
점functor가 étale hyperdescent를 만족함은 [명제 2](#prop2)의 localization이 étale localization으로 확장되고 fpqc 하강이 étale 하강을 함의하기 때문이며, 이는 [\[Stacks\] §그로텐디크 위상, ⁋정리 14](/ko/math/stacks/grothendieck_topology#thm14)의 유도 판본이다. 완전 충실성은 Yoneda 보조정리의 $\infty$-범주 판본에서 나온다. ([\[범주론\] §표현가능한 함자, ⁋정리 4](/ko/math/category_theory/representable_functors#thm4)의 space값 승격) 고전적 algebraic stack $\mathcal{X}$을 derived stack으로 보려면, 그 functor를 discrete ring에 제한하고 groupoid를 $1$-truncated space로 보면 되며, hyperdescent가 $1$-truncated sheaf에서 통상적 stack 하강으로 환원됨을 확인하면 된다. ([\[Stacks\] §대수적 스택, ⁋정의 6](/ko/math/stacks/algebraic_stacks#def6)) 자세한 논증은 ([TV], [Lur, SAG])에 있다.
:::

Derived stack 가운데 기하를 논할 수 있는 부류는 고전적 경우와 마찬가지로 atlas로 가려낸다. 다만 atlas의 source가 derived scheme이고, 차원·매끄러움은 유도 판본으로 읽는다.

::: 정의 8
Derived stack $\mathcal{X}$이 *geometric* (또는 *derived Artin stack<sub>유도 아틴 스택</sub>*)이라는 것은, 그 대각선이 representable하고, derived scheme $U$으로부터의 smooth surjective morphism $u:U\rightarrow \mathcal{X}$, 곧 *atlas*가 존재하는 것을 뜻한다. Atlas를 étale 전사로 잡을 수 있으면 $\mathcal{X}$을 *derived Deligne–Mumford stack*이라 부른다.
:::

이는 고전적 algebraic stack의 정의를 derived scheme을 국소 모형으로 삼아 옮긴 것이다. ([\[Stacks\] §대수적 스택, ⁋정의 6](/ko/math/stacks/algebraic_stacks#def6)) 여기서 morphism $u:U\rightarrow \mathcal{X}$의 smooth·étale 성질은 뒤에서 여접 복합체로 특징짓는데, 곧 상대 여접 복합체 $L_u$이 degree $0$에 집중된 locally free sheaf인 경우가 smooth이다. Atlas가 있으면 $\mathcal{X}$의 truncation $t_0(\mathcal{X})$은 atlas의 truncation $t_0(U)$을 atlas로 갖는 고전적 algebraic stack이 되어, geometric derived stack이 고전적 algebraic stack 위에 얹힌 유도 두께임이 다시 확인된다. 가장 기본적인 예는 고전적 stack 자체가 discrete derived stack으로 들어앉는 경우이다.

::: 예시 9 (분류 stack $\mathbf{B}G$)
$G$을 $k$ 위의 smooth affine group scheme이라 하자. Derived stack $\mathbf{B}G$을, animated ring $R$에 $\Spec \pi_0(R)$ 위의 $G$-torsor들의 groupoid를 대응시키는 functor로 정의한다. $G$이 smooth하므로 그 atlas $\Spec k\rightarrow \mathbf{B}G$은 smooth 전사이고, 그 base change는 $G\rightrightarrows \Spec k$이라 $\mathbf{B}G$은 geometric derived stack이다. 이 경우 구조가 discrete ring 위에서 정해지므로 $\mathbf{B}G$은 사실 고전적 algebraic stack $\mathbf{B}G$과 같고 ([\[Stacks\] §대수적 스택, ⁋정의 7](/ko/math/stacks/algebraic_stacks#def7)에서 $X=\Spec k$인 quotient stack), $t_0(\mathbf{B}G)=\mathbf{B}G$은 자기 자신이다. 곧 순전히 stack 방향의 대칭(automorphism $G$)만으로는 유도 두께가 생기지 않는다. 유도 정보는 대신 $G$이 작용하는 대상 쪽에서, 예컨대 $G$-action을 받는 derived scheme의 유도 올곱을 quotient한 $[Z/G]$에서 나타난다. 이러한 유도 올곱을 다음 두 절에서 다룬다.
:::

## 여접 복합체와 접복합체

Derived scheme과 derived stack 위에서 미분 기하를 하려면, 각 affine 조각에서 이미 세운 여접 복합체 $L_{R/k}$을 대역적 대상으로 이어붙여야 한다. ([§Simplicial 가환환과 animation, ⁋정의 10](/ko/math/derived_algebraic_geometry/animated_rings#def10)) 여접 복합체는 localization과 étale morphism에 대하여 잘 행동하므로 이 접착은 곧바로 가능하다.

::: 정의 10
Derived scheme의 morphism $f:X\rightarrow Y$에 대하여, 각 affine slice $\Spec R\subseteq X$이 $\Spec S\subseteq Y$ 위로 갈 때의 여접 복합체 $L_{R/S}$을 이어붙여 얻는 $\mathcal{O}_X$-module의 sheaf를 $f$의 *상대 여접 복합체<sub>relative cotangent complex</sub>* $L_f=L_{X/Y}\in \QCoh(X)$이라 한다. $Y=\Spec k$일 때 이를 $X$의 *절대 여접 복합체* $L_X=L_{X/k}$이라 적는다. $L_X$의 $\mathcal{O}_X$-쌍대

$$T_X=L_X^\vee=\mathcal{R}\mathcal{H}om_{\mathcal{O}_X}(L_X,\mathcal{O}_X)$$

을 $X$의 *접복합체<sub>tangent complex</sub>*라 부른다. Geometric derived stack $\mathcal{X}$에 대해서는 atlas $u:U\rightarrow \mathcal{X}$을 따라 pullback한 $u^\ast L_{\mathcal{X}}$이 삼각형 $u^\ast L_{\mathcal{X}}\rightarrow L_U\rightarrow L_{U/\mathcal{X}}$을 채우도록 하는 유일한 대상으로 $L_{\mathcal{X}}$을 정의한다.
:::

접착이 잘 정의됨은 여접 복합체가 étale morphism에 대하여 소멸하고 localization과 교환한다는 사실, 곧 étale $R\rightarrow R'$에 대하여 $L_{R'/R}\simeq0$이고 $L_{R/k}\otimes_R R'\simeq L_{R'/k}$이라는 데서 나온다. ([§Simplicial 가환환과 animation, ⁋명제 14](/ko/math/derived_algebraic_geometry/animated_rings#prop14)의 매끄러움 판정과 추이 삼각형이 이를 준다.) Affine 경우 $X=\Spec R$이면 $L_X$은 단순히 $L_{R/k}$의 sheafification이고, $X$이 smooth한 고전적 scheme이면 $L_X\simeq \Omega_X$이 degree $0$에 집중된 locally free sheaf이다. Stack의 경우 atlas 삼각형에서 $L_{U/\mathcal{X}}$이 atlas morphism의 상대 여접 복합체이므로, $\mathcal{X}$이 smooth할 때 $L_{\mathcal{X}}$은 degree $0$의 접방향과 함께 stack 방향에서 오는 음의 degree 항, 곧 $\mathbf{B}G$ 유형의 automorphism이 주는 $\mathfrak{g}^\vee[-1]$ 꼴의 항을 가질 수 있다.

::: 명제 11
여접 복합체는 다음을 만족한다.

1. (추이 삼각형) morphism의 합성 $X\xrightarrow{f}Y\xrightarrow{g}Z$에 대하여 $\QCoh(X)$ 안의 삼각형

$$f^\ast L_{Y/Z}\longrightarrow L_{X/Z}\longrightarrow L_{X/Y}\longrightarrow f^\ast L_{Y/Z}[1]$$

이 존재한다.

2. (base change) derived scheme의 유도 올곱 $X'=X\times_Y^hY'$과 그 projection $g:X'\rightarrow X$에 대하여 $L_{X'/Y'}\simeq g^\ast L_{X/Y}$이다.
:::
::: 증명
두 성질은 모두 affine 국소적이며, 그 국소 형태가 각각 [§Simplicial 가환환과 animation, ⁋정리 12](/ko/math/derived_algebraic_geometry/animated_rings#thm12)과, 유도 tensor product에 대한 base change invariance이다. Affine 국소적으로 $X=\Spec B$, $Y=\Spec A$, $Y'=\Spec A'$이면 $X'=\Spec(B\otimes_A^{\mathbb{L}}A')$이고, 여접 복합체가 유도 tensor product와 교환하여 $L_{(B\otimes_A^{\mathbb{L}}A')/A'}\simeq L_{B/A}\otimes_B^{\mathbb{L}}(B\otimes_A^{\mathbb{L}}A')$이 됨은 free simplicial 분해를 base change하여 직접 확인된다. 이 국소 동형들이 [정의 10](#def10)의 접착과 호환되므로 대역적으로 성립한다. 자세한 논증은 ([Ill], [Lur, SAG])에 있다.
:::

추이 삼각형과 base change는 여접 복합체를 계산 가능한 대상으로 만들며, 특히 base change invariance는 유도 올곱 위의 여접 복합체가 원래 morphism의 여접 복합체를 그대로 물려받음을 말한다. 이 두 성질이 다음 절에서 quasi-smooth morphism이 유도 올곱에 대하여 닫혀 있음을 보장한다.

## Quasi-smooth 사상과 virtual dimension

Smooth morphism은 여접 복합체가 degree $0$의 locally free sheaf인 경우였다. ([§Simplicial 가환환과 animation, ⁋명제 14](/ko/math/derived_algebraic_geometry/animated_rings#prop14)) 이를 degree $1$까지 허용하여 한 단계 넓힌 것이 quasi-smooth morphism이며, derived algebraic geometry에서 virtual 구조를 나르는 morphism의 부류가 정확히 이것이다.

::: 정의 12
Derived scheme(또는 geometric derived stack)의 morphism $f:X\rightarrow Y$이 *quasi-smooth<sub>유사매끄러움</sub>*하다는 것은, $f$이 유한표현이고 상대 여접 복합체 $L_f$이 perfect이며 그 Tor-amplitude가 $[-1,0]$에 놓이는 것, 곧 $L_f$이 국소적으로

$$L_f\simeq\bigl[E_1\longrightarrow E_0\bigr],\qquad E_0\text{ (degree }0),\quad E_1\text{ (degree }1)$$

의 꼴로 두 항의 locally free sheaf로 표현되는 것을 뜻한다. 이때 $f$의 *virtual 상대차원<sub>virtual relative dimension</sub>*을 $L_f$의 K-이론적 계수

$$\operatorname{vdim}(f)=\rank E_0-\rank E_1$$

으로 정의하고, $X$이 $\Spec k$ 위에서 quasi-smooth할 때 $\operatorname{vdim}(X)=\operatorname{vdim}(X/k)$을 $X$의 *virtual dimension*이라 부른다.
:::

Tor-amplitude $[-1,0]$은 cohomological 규약의 표현이며, 우리가 쓰는 connective(homological) 규약에서는 $L_f$이 degree $0,1$의 두 항에 집중됨을 뜻한다. Degree $0$의 $E_0$은 smooth 접방향, 곧 Kähler differential에 해당하고, degree $1$의 $E_1$은 conormal orientation, 곧 방정식이 만드는 장애에 해당한다. 이 degree $1$ 방향이 변형이론에서 변형의 연장을 막는 장애가 사는 자리이며, quasi-smooth morphism은 그 장애가 여접 복합체 한 단계 안에 완전히 담기는 morphism이다. ([\[스킴\] §변형이론과 여접 복합체, ⁋정리 9](/ko/math/scheme_theory/deformation_theory#thm9)) 그러므로 $\operatorname{vdim}(f)$은 "접방향의 수에서 방정식의 수를 뺀 것"으로, 고전적 codimension 계산의 유도 판본이다. 이 정의가 실제로 무엇을 재는지는 고전적 lci 및 regular embedding과의 관계에서 분명해진다.

::: 명제 13
$f:X\rightarrow Y$을 derived scheme의 morphism이라 하자.

1. $f$이 quasi-smooth한 것은, 국소적으로 $f$이 smooth morphism과 regular embedding의 합성으로 인수분해되는 것, 곧 $Y$ 위의 smooth $Y$-scheme $P$의 vector bundle $E$의 절단 $s$의 *유도 영점자리*

$$X\simeq Z(s)=P\times_{E}^hP$$

로 국소적으로 표현되는 것과 동치이다. 여기서 두 morphism $P\rightrightarrows E$은 각각 영절단과 $s$이다.

2. $f$이 quasi-smooth이면 그 truncation $t_0(f):t_0(X)\rightarrow t_0(Y)$은 국소적으로 smooth morphism 위에서 $r$개의 방정식으로 잘린 것이며, 이 방정식들이 regular sequence를 이룰 때 고전적 lci morphism이 된다. 이 조건은 $f$이 discrete할 (곧 $X$이 고전적 scheme일) 필요충분조건인 $\pi_1(\mathcal{O}_X)=0$과 동치이다.

3. Quasi-smooth morphism은 임의의 base change에 대하여 닫혀 있고, virtual 상대차원을 보존한다. 곧 $f$이 quasi-smooth이고 $Y'\rightarrow Y$이 임의의 morphism이면 $f':X\times_Y^hY'\rightarrow Y'$도 quasi-smooth이며 $\operatorname{vdim}(f')=\operatorname{vdim}(f)$이다.
:::
::: 증명
**(1)** 절단 $s:P\rightarrow E$의 유도 영점자리 $Z(s)=P\times_E^hP$은 국소적으로 $E$을 rank $r$의 자명 다발로 놓아 $s=(s_1,\ldots,s_r)$으로 쓰면 $\mathcal{O}_{Z(s)}=\operatorname{Kos}(\mathcal{O}_P;s_1,\ldots,s_r)$, 곧 $s_i$들에 대한 Koszul 복합체이다. Embedding $Z(s)\hookrightarrow P$의 여접 복합체는 [명제 11](#prop11)의 base change로 계산되어 $L_{Z(s)/P}\simeq(E^\vee\vert_{Z(s)})[1]$, 곧 degree $1$에 집중된 locally free sheaf이다. $P$이 $Y$ 위에서 smooth하므로 $L_{P/Y}$은 degree $0$의 locally free sheaf이고, [명제 11](#prop11)의 추이 삼각형이 $L_{X/Y}$을 degree $0,1$의 두 항으로 준다. 따라서 $Z(s)$은 quasi-smooth이다. 역으로 $f$이 quasi-smooth이면 $L_f\simeq[E_1\rightarrow E_0]$의 $E_0$을 실현하는 smooth 인수 $P$을 국소적으로 잡고, $E_1$을 실현하는 절단 $s$을 그 위에서 택하여 위 인수분해를 얻는다. 세부는 ([Kha], [Lur, SAG])에 있다.

**(2)** $X=Z(s)$이면 $t_0(X)=\{s=0\}$은 $P$의 고전적 영점자리이고, 이는 국소적으로 $r$개의 방정식으로 잘린 것이며, 그 방정식들이 regular sequence를 이룰 때 고전적 lci가 된다. $X$이 discrete함은 $s_1,\ldots,s_r$이 regular sequence를 이루어 Koszul 복합체가 $\pi_0$에 집중되는 것, 곧 $\pi_1(\mathcal{O}_X)=0$인 것과 동치이다. Regular sequence가 아니면 Koszul homology가 $\pi_{\geq1}\mathcal{O}_X\neq0$을 낳아 $X$은 discrete하지 않다.

**(3)** Base change 안정성은 유도 올곱이 여접 복합체를 pullback으로 보존하고 ([명제 11](#prop11)의 base change), pullback이 perfect 복합체의 Tor-amplitude를 넓히지 않으며 locally free sheaf의 rank를 보존하는 데서 따른다. 따라서 $L_{f'}\simeq g^\ast L_f$이 다시 Tor-amplitude $[-1,0]$이고 $\operatorname{vdim}$이 rank로 정해지므로 보존된다.
:::

[명제 13](#prop13)은 quasi-smooth morphism이 고전적 lci를 유도 세계로 정확히 확장한 것임을 밝힌다. 고전적 lci morphism은 regular sequence로 잘린 것이었고, quasi-smooth morphism은 그 regularity 조건을 떼어 낸 것, 곧 아무 절단의 유도 영점자리이다. Regular sequence이면 유도 영점자리가 discrete하여 고전적 영점자리와 일치하고, regular sequence가 아니면 Koszul homology가 $\pi_{\geq1}$로 살아남아 초과분을 기록한다. 이 초과분이야말로 유도 기하가 붙드는 정보이며, 그 자연스러운 무대가 유도 올곱이다.

## Derived 올곱과 virtual 구조

고전적 scheme의 올곱은 두 morphism이 base 위에서 같아지는 점들을 모으는 limit이었고, affine에서는 tensor product $B\otimes_AC$으로 주어졌다. ([\[스킴\] §올곱, ⁋정리 8](/ko/math/scheme_theory/fiber_products#thm8)) Derived 올곱은 이 limit을 homotopy limit으로, tensor product를 유도 tensor product로 바꾼 것이다.

::: 정의 14
Derived scheme(또는 derived stack)의 morphism $X\xrightarrow{f}Z\xleftarrow{g}Y$에 대하여, 그 *유도 올곱<sub>derived fiber product</sub>* $X\times_Z^hY$은 $\mathrm{dSch}$(또는 $\mathrm{dSt}$)에서의 homotopy pullback, 곧 functor

$$R\mapsto h_X(R)\times_{h_Z(R)}^hh_Y(R)$$

을 표현하는 derived scheme이다. Affine에서 $X=\Spec B$, $Y=\Spec C$, $Z=\Spec A$이면

$$X\times_Z^hY=\Spec\bigl(B\otimes_A^{\mathbb{L}}C\bigr)$$

으로 실현된다.
:::

곧 유도 올곱은 국소적으로 유도 tensor product를 취하는 것이며, ([§Simplicial 가환환과 animation, ⁋정의 7](/ko/math/derived_algebraic_geometry/animated_rings#def7)의 homotopy pushout을 반변으로 옮긴 것) 그 존재와 접착은 유도 tensor product가 localization·étale morphism과 교환한다는 사실로 보장된다. 고전적 올곱과의 관계, 그리고 그것이 나르는 virtual 구조는 다음 명제가 요약한다.

::: 명제 15
$X\xrightarrow{f}Z\xleftarrow{g}Y$을 derived scheme의 morphism이라 하고 $W=X\times_Z^hY$이라 하자.

1. Truncation은 고전적 올곱을 준다.

$$t_0(W)\cong t_0(X)\times_{t_0(Z)}t_0(Y)$$

$X,Y,Z$이 고전적 scheme인 affine 경우 $\pi_0\mathcal{O}_W=B\otimes_AC$이고, higher homotopy는 $\pi_n\mathcal{O}_W=\Tor_n^A(B,C)$이 초과분을 기록한다.

2. $f$이 quasi-smooth이면 그 base change인 projection $W\rightarrow Y$도 quasi-smooth이고 $\operatorname{vdim}(W/Y)=\operatorname{vdim}(f)$이다. 특히 $X,Y,Z$이 각각 차원 $d_X,d_Y,d_Z$의 smooth 고전적 variety이고 $f,g$이 closed embedding이면 $W$은 quasi-smooth이며

$$\operatorname{vdim}(W)=d_X+d_Y-d_Z$$

이다. 이 virtual 차원이 고전적으로 기대되는 교차 차원과 정확히 일치한다.

3. 위 상황에서 $W$은 $t_0(W)$ 위의 *virtual fundamental class* $[W]^{\mathrm{vir}}\in \CH_{\operatorname{vdim}(W)}(t_0(W))$을 낳으며, $Z$이 smooth이고 교차가 proper이면 그 pushforward가 고전적 교차곱 $[X]\cdot[Y]$을 계산한다. 특히 교차가 isolated point $p$에서 일어나면 그 국소 중복도는 Serre의 Tor 공식

$$i_p(X,Y)=\sum_{n\geq0}(-1)^n\operatorname{length}\pi_n(\mathcal{O}_{W,p})=\sum_{n\geq0}(-1)^n\operatorname{length}\Tor_n^{\mathcal{O}_{Z,p}}(\mathcal{O}_{X,p},\mathcal{O}_{Y,p})$$

으로 주어진다.
:::
::: 증명
**(1)** $\pi_0$이 유도 tensor product를 고전적 tensor product로 truncate하므로 ([§Simplicial 가환환과 animation, ⁋명제 8](/ko/math/derived_algebraic_geometry/animated_rings#prop8)) $\pi_0\mathcal{O}_W=B\otimes_AC$이고, $t_0$이 $\pi_0$-sheaf만 보므로 $t_0(W)$이 고전적 올곱이다. Higher homotopy $\pi_n\mathcal{O}_W=\Tor_n^A(B,C)$도 같은 명제이다.

**(2)** Quasi-smooth의 base change 안정성과 virtual 상대차원 보존은 [명제 13](#prop13)의 셋째 항이다. $X,Y$이 smooth $Z$-scheme(closed embedding)이면 $f$의 상대 여접 복합체는 conormal orientation $N_{X/Z}^\vee[1]$과 접방향의 조합이 되어 $\operatorname{vdim}(f)=d_X-d_Z$이고, base change로 $\operatorname{vdim}(W/Y)=d_X-d_Z$, 따라서 $\operatorname{vdim}(W)=d_Y+(d_X-d_Z)$이다.

**(3)** $W$이 quasi-smooth이므로 그 여접 복합체의 절단이 $t_0(W)$ 위에 perfect obstruction 이론 $L_W\vert_{t_0(W)}\rightarrow L_{t_0(W)}$을 주고, 이 자료로부터 intrinsic normal cone을 obstruction 다발의 전체 공간 안으로 끊어 virtual fundamental class $[W]^{\mathrm{vir}}$을 얻는다. $Z$이 smooth이고 교차가 proper이면 이 class의 pushforward가 교차곱의 정의와 일치함은 deformation to the normal cone과 대조하여 나온다. ([\[대수다양체\] §교차곱, ⁋정의 1](/ko/math/algebraic_varieties/intersection_product#def1)) isolated point $p$에서는 $[W]^{\mathrm{vir}}$의 길이가 $\mathcal{O}_{W,p}$의 Euler characteristic $\sum(-1)^n\operatorname{length}\pi_n$이고, $\pi_n=\Tor_n^A(B,C)$이므로 Serre의 Tor 공식과 일치한다. 완전한 논증은 ([TV], [Kha])에 있다.
:::

[명제 15](#prop15)가 이 글의 핵심이다. 고전적 올곱은 $\pi_0$만 보아 교차의 초과분을 뭉갰지만, 유도 올곱은 그 초과분을 $\Tor$로 정확히 붙들어 virtual 차원과 virtual class로 번역한다. Serre가 intersection multiplicity를 $\Tor$의 교대합으로 정의해야 했던 이유가 여기서 기하적으로 설명된다. 그 교대합이 바로 유도 올곱 $\mathcal{O}_W$의 Euler characteristic인 것이다. 이 virtual class 형식은 Gromov–Witten 이론에서 stable map들의 moduli space가 기대차원보다 클 때, 그 위의 virtual fundamental class로 불변량을 정의하는 데 쓰이는 것과 같은 구조이며, 유도 기하는 그러한 moduli를 quasi-smooth derived stack으로 실현하여 이 class를 자연스럽게 공급한다.

::: 참고 16 (유도 loop space)
유도 올곱의 stack 차원 판본이 유도 loop space이다. Derived scheme $X$의 대각선 $\Delta:X\rightarrow X\times X$을 자기 자신과 유도적으로 겹친

$$\mathcal{L}X=X\times_{X\times X}^hX$$

을 $X$의 *유도 loop space*라 부른다. $X$이 smooth하면 $\Delta$이 regular embedding이고, [명제 11](#prop11)의 base change로 $L_{\mathcal{L}X/X}\simeq T_X^\vee[1]=\Omega_X[1]$이 되어 $\mathcal{L}X$이 quasi-smooth이며, 그 structure sheaf의 homotopy는 Hochschild–Kostant–Rosenberg 동형에 의하여

$$\pi_n\mathcal{O}_{\mathcal{L}X}\cong\Omega_X^n$$

으로 differential form들을 준다. 곧 고전적으로 $t_0(\mathcal{L}X)=X$은 대각선의 image 그대로이지만, 유도 두께 $\pi_{\geq1}$이 de Rham 형식 전체를 실어 나른다. 이는 유도 자기교차가 순수 대수적 대상(여기서는 differential form)을 어떻게 기하적으로 부활시키는지 보여주는 표준적인 예이다.
:::

## 예시: 유도 교차의 계산

이제 세 가지 구체적 교차로 위 이론을 검증한다. 첫째는 이미 [예시 5](#ex5)에서 만난 한 점의 유도 자기교차로, 이번에는 그것을 유도 올곱으로 다시 읽는다. Affine 직선 $\mathbb{A}^1$ 안에서 원점 $\{0\}$은 차원 $0$의 smooth 부분다양체이고, 그 유도 자기교차

$$Z=\{0\}\times_{\mathbb{A}^1}^h\{0\}=\Spec\bigl(k\otimes_{k[\x]}^{\mathbb{L}}k\bigr)$$

은 [명제 15](#prop15)에 의하여 virtual dimension

$$\operatorname{vdim}(Z)=0+0-1=-1$$

의 quasi-smooth derived scheme이다. $t_0(Z)$은 한 점이지만, $\pi_1\mathcal{O}_Z=k\neq0$이 이 음의 virtual 차원을 실현한다. 곧 두 점이 직선 위에서 일반적으로 만나지 않아 기대 intersection number가 $0$이라는 사실이, Serre 공식 $\operatorname{length}\pi_0-\operatorname{length}\pi_1=1-1=0$으로 정확히 나온다. 고전적 올곱이 이를 "한 점"으로 뭉갠 자리에서, 유도 올곱은 $-1$차원의 virtual 구조를 붙든다.

::: 예시 17 (derived critical locus)
Smooth variety $U=\mathbb{A}^n=\Spec k[\x_1,\ldots,\x_n]$ 위의 함수 $f\in \mathcal{O}(U)$에 대하여, 그 미분 $\dd{f}$은 cotangent 다발 $\Omega_U\cong \mathcal{O}_U^n$의 절단 $(\partial f/\partial \x_1,\ldots,\partial f/\partial \x_n)$이다. $f$의 *derived critical locus<sub>유도 임계점 자리</sub>* $\operatorname{Crit}(f)$을 $\dd{f}$의 유도 영점자리로 정의한다.

$$\operatorname{Crit}(f)=Z(\dd{f})=U\times_{\Omega_U}^hU$$

[명제 13](#prop13)에 의하여 이는 rank $n$ 다발의 절단의 유도 영점자리이므로 quasi-smooth이고 $\operatorname{vdim}=n-n=0$이며, 그 structure sheaf는 편미분들에 대한 Koszul 복합체

$$\mathcal{O}_{\operatorname{Crit}(f)}=\operatorname{Kos}\bigl(k[\x_1,\ldots,\x_n];\partial_1f,\ldots,\partial_nf\bigr)$$

이다. $t_0(\operatorname{Crit}(f))=\Spec k[\x]/(\partial_1f,\ldots,\partial_nf)$은 고전적 critical point scheme, 곧 Jacobian ring의 spectrum이다. 편미분들이 regular sequence를 이루면 (가령 isolated 비축퇴 critical point) Koszul 복합체가 $\pi_0$에 집중되어 유도 구조가 고전적 구조와 같지만, regular sequence가 아니면 higher homotopy가 살아난다. 예컨대 $n=2$, $f=\x_1^2\x_2$이면 $\partial_1f=2\x_1\x_2$, $\partial_2f=\x_1^2$이 공통 인수 $\x_1$을 가져 regular sequence가 아니므로, Koszul homology $\pi_1\mathcal{O}_{\operatorname{Crit}(f)}\neq0$이 critical point 자리의 비축소성을 유도적으로 검출한다. $\operatorname{Crit}(f)$의 접복합체 $T_{\operatorname{Crit}(f)}$은 Hessian이 대칭이라는 사실 때문에 여접 복합체와 자기쌍대적이며, 이 self-duality가 derived critical locus 위의 $(-1)$-shifted symplectic 구조로 정착된다.
:::

::: 예시 18 (평면 위 두 곡선의 비횡단 교차)
$\mathbb{A}^2=\Spec k[\x,\y]$ 안에서 두 곡선 $V=\{\y=0\}$과 $W=\{\y=\x^2\}$을 생각하자. 이들은 원점에서 접하며, 고전적 intersection multiplicity는 $i_0(V,W)=2$이다. ([\[대수다양체\] §교차곱, ⁋정의 1](/ko/math/algebraic_varieties/intersection_product#def1)) 유도 올곱

$$V\times_{\mathbb{A}^2}^hW=\Spec\bigl(k[\x,\y]/(\y)\otimes_{k[\x,\y]}^{\mathbb{L}}k[\x,\y]/(\y-\x^2)\bigr)$$

을 계산한다. $V\cong \Spec k[\x]$ 위에서 $W$을 자르는 방정식 $\y-\x^2$은 $-\x^2$으로 내려오는데, 이는 $k[\x]$의 nonzerodivisor이므로 유도 tensor product가 discrete하여 ([§Simplicial 가환환과 animation, ⁋명제 8](/ko/math/derived_algebraic_geometry/animated_rings#prop8))

$$\pi_0=k[\x]/(\x^2)\quad(\text{length }2),\qquad \pi_n=0\quad(n\geq1)$$

이다. 곧 [명제 15](#prop15)에 따라 $V\times_{\mathbb{A}^2}^hW$은 virtual dimension $1+1-2=0$의 quasi-smooth derived scheme이고, higher homotopy가 없어 유도 교차가 고전적 교차 $\Spec k[\x]/(\x^2)$과 일치하며, 그 virtual class의 길이 $2$가 접촉 중복도 $2$를 정확히 준다. 비횡단적이지만 두 곡선이 공통 성분을 갖지 않아 proper하게 만나는 이 상황에서는, 초과 정보가 higher homotopy가 아니라 $\pi_0$의 nilpotent 두께로 나타난다.

반면 두 곡선이 아예 겹치는 자기교차 $V\times_{\mathbb{A}^2}^hV$에서는 초과분이 higher homotopy로 옮겨간다. $V$을 자르는 방정식 $\y$이 $k[\x]$ 위에서 $0$으로 내려오므로, Koszul 계산이

$$\pi_0=k[\x]=\mathcal{O}_V,\qquad \pi_1=k[\x]\cong N_{V/\mathbb{A}^2}\quad(\text{자명 normal bundle}),\qquad \pi_{\geq2}=0$$

을 준다. 이제 $t_0=V$은 차원 $1$이라 virtual dimension $1+1-2=0$을 초과하며, 그 초과 차원 $1$이 $\pi_1=\mathcal{O}_V$으로 정확히 기록된다. Virtual class는 $[V\times_{\mathbb{A}^2}^hV]^{\mathrm{vir}}=e(N_{V/\mathbb{A}^2})\cap[V]$, 곧 normal bundle의 Euler class인데, $\mathbb{A}^2$ 안에서 $V$의 normal bundle이 자명하여 $e(N_{V/\mathbb{A}^2})=0$이므로 $V\cdot V=0$이다. 이는 곡선이 affine 평면 안에서 자기 자신으로부터 자유롭게 이동할 수 있어 self-intersection number가 $0$이라는 고전적 사실의 유도적 실현이며, [예시 5](#ex5)의 점 차원 현상이 곡선 차원에서 반복된 것이다.
:::

이 세 예시는 유도 올곱이 세 가지 초과 현상을 하나의 언어로 붙듦을 보여준다. [예시 5](#ex5)의 낮은 차원에서의 음의 virtual dimension, [예시 17](#ex17)의 regular sequence 실패가 낳는 higher homotopy, 그리고 [예시 18](#ex18)의 자기교차의 초과 차원이 그것이다. 고전적 올곱이 $\pi_0$만 보아 이 정보들을 잃던 자리에서, animated ring을 이어붙여 세운 derived scheme과 그 위의 유도 올곱은 virtual 차원과 virtual class를 통해 교차의 참된 기하를 복원한다. 이것이 derived algebraic geometry가 고전 intersection theory에 주는 가장 직접적인 기여이다.

---

**참고문헌**

**[TV]** B. Toën, G. Vezzosi, *Homotopical algebraic geometry II: geometric stacks and applications*, Memoirs of the American Mathematical Society 193, 2008.  
**[Toë]** B. Toën, *Derived algebraic geometry*, EMS Surveys in Mathematical Sciences 1 (2014), 153–240.  
**[Lur, SAG]** J. Lurie, *Spectral algebraic geometry*, [www.math.ias.edu/~lurie](https://www.math.ias.edu/~lurie).  
**[Kha]** A. A. Khan, *Lectures on derived algebraic geometry*, [www.preschema.com](https://www.preschema.com).  
**[Ill]** L. Illusie, *Complexe cotangent et déformations I, II*, Lecture Notes in Mathematics 239, 283, Springer, 1971–1972.  
**[Stacks]** The Stacks project authors, *The Stacks project*, [stacks.math.columbia.edu](https://stacks.math.columbia.edu).
