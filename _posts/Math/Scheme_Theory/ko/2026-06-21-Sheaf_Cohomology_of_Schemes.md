---
title: "스킴의 층 코호몰로지"
description: '대수다양체 위에서 도입한 층 코호몰로지를 임의의 스킴 위의 준연접층으로 끌어올린다. Abelian sheaf 범주의 유도 함자로서의 정의와 affine 덮개에 대한 Čech 코호몰로지를 다루고, affine scheme 위 준연접층의 소멸 정리로부터 separated scheme 위에서 두 코호몰로지가 일치함을 보인다. 사영공간 위 $$\mathcal{O}(d)$$의 코호몰로지를 재계산하고, Noetherian projective scheme 위 연접층의 유한성과 Serre vanishing을 증명한다. 이어 ample invertible sheaf를 higher cohomology의 소멸로 특징짓는 Serre의 판정법을 얻고, Euler characteristic과 Hilbert polynomial을 도입하여 사영 부분스킴의 degree를 정의한다.'
excerpt: "Cohomology of quasi-coherent sheaves, Serre vanishing, the cohomological criterion for ampleness, and Hilbert polynomials"

categories: [Math / Scheme Theory]
permalink: /ko/math/scheme_theory/sheaf_cohomology_of_schemes
sidebar: 
    nav: "scheme_theory-ko"

date: 2026-06-21
weight: 18

published: false
drift_needed: true
---

우리는 [\[대수다양체\] §층 코호몰로지](/ko/math/algebraic_varieties/sheaf_cohomology)에서 (quasi-projective) variety 위의 quasi-coherent sheaf에 대한 sheaf cohomology를 derived functor로 정의하고, Čech cohomology와의 비교 및 Leray 정리를 통해 이를 계산하는 방법을 살펴보았다. 이제 우리는 quasi-coherent sheaf를 scheme의 언어로 정리하였으므로, 같은 일을 scheme에서도 할 수 있다. 핵심적인 것은 이전 [\[대수다양체\] §층 코호몰로지](/ko/math/algebraic_varieties/sheaf_cohomology)에서의 quasi-projective 가정은 과도한 것이라는 것으로, seperatedness와 affine scheme 위에서의 vanishing theorem을 보이고 나면 해당 글과 마찬가지의 결과들을 증명할 수 있다. 

이전 몇 개의 글과 마찬가지로, 이번 글의 목표는 이미 [\[대수다양체\] §층 코호몰로지](/ko/math/algebraic_varieties/sheaf_cohomology)에서 다룬 내용을 scheme으로 올리는 것이며, 몇몇 계산은 직접 수행하기도 하지만, 대부분의 계산은 해당 글들에 맡겨두고 이 언어로 번역하는 작업이 주가 될 것이다. 

## 유도함자로서의 코호몰로지

Scheme $X$ 위에서도 abelian group들의 sheaf들의 category $\Sh(X)$는 abelian category이며 enough injective를 가진다. 따라서 [\[대수다양체\] §층 코호몰로지](/ko/math/algebraic_varieties/sheaf_cohomology)에서와 동일한 방식으로 global section functor의 derived functor를 정의할 수 있다. 우리의 주된 관심은 항상 quasi-coherent sheaf이지만, 그곳에서와 마찬가지로 injective resolution은 $\Sh(X)$ 안에서 잡는다는 점에 유의하자.

::: 정의 1
Scheme $X$ 위의 $\mathcal{O}_X$-module $\mathcal{F}$에 대하여, global section functor $\Gamma(X, -):\Sh(X) \rightarrow \Ab$의 right derived functor를 ([\[호몰로지 대수학\] §유도함자, ⁋정의 9](/ko/math/homological_algebra/derived_functors#def9)) 취하여 $i$번째 *sheaf cohomology<sub>층 코호몰로지</sub>*를

$$H^i(X, \mathcal{F})=R^i\Gamma(X, -)(\mathcal{F})=\frac{\ker\bigl(\Gamma(X, \mathcal{I}^i) \rightarrow \Gamma(X, \mathcal{I}^{i+1})\bigr)}{\im\bigl(\Gamma(X, \mathcal{I}^{i-1}) \rightarrow \Gamma(X, \mathcal{I}^i)\bigr)}$$

으로 정의한다. 여기에서 $0 \rightarrow \mathcal{F} \rightarrow \mathcal{I}^\bullet$은 $\Sh(X)$에서의 injective resolution이다.
:::

이 정의는 [\[대수다양체\] §층 코호몰로지, ⁋정의 1](/ko/math/algebraic_varieties/sheaf_cohomology#def1)을 임의의 scheme 위로 옮긴 것에 불과하며, $\mathcal{I}^\bullet$의 선택에 무관함을 비롯한 형식적 성질은 모두 homological algebra의 표준 논증으로부터 따라온다. 특히 $H^0(X, \mathcal{F})=\Gamma(X, \mathcal{F})$이고, sheaf의 short exact sequence는 long exact sequence를 유도한다. 여기에서 $\mathcal{O}_X$-module들의 category 안에서 injective resolution을 잡아도 같은 값이 얻어지는데, injective $\mathcal{O}_X$-module 또한 flasque이고 ([\[대수다양체\] §층 코호몰로지, ⁋보조정리 9](/ko/math/algebraic_varieties/sheaf_cohomology#lem9)의 증명에서 $i^U_!\mathbb{Z}_U$를 $i^U_!(\mathcal{O}_X\vert_U)$로 바꾸면 된다), flasque sheaf는 $\Gamma(X, -)$-acyclic이므로 ([\[대수다양체\] §층 코호몰로지, ⁋명제 16](/ko/math/algebraic_varieties/sheaf_cohomology#prop16)) 그러한 resolution이 $\Sh(X)$에서는 acyclic resolution이 되기 때문이다. ([\[대수다양체\] §층 코호몰로지, ⁋명제 17](/ko/math/algebraic_varieties/sheaf_cohomology#prop17))

::: 명제 2
$\mathcal{O}_X$-module의 short exact sequence

$$0 \rightarrow \mathcal{F}' \rightarrow \mathcal{F} \rightarrow \mathcal{F}'' \rightarrow 0$$

에 대하여, long exact sequence

$$0 \rightarrow H^0(X, \mathcal{F}') \rightarrow H^0(X, \mathcal{F}) \rightarrow H^0(X, \mathcal{F}'') \xrightarrow{\delta} H^1(X, \mathcal{F}') \rightarrow H^1(X, \mathcal{F}) \rightarrow \cdots$$

이 존재한다.
:::
::: 증명
$\Gamma(X, -)$는 left exact functor이고 $\Sh(X)$는 enough injective를 가지므로, right derived functor가 정의하는 $\delta$-functor의 long exact sequence가 그대로 성립한다. (이는 [\[호몰로지 대수학\] §유도함자, ⁋명제 8](/ko/math/homological_algebra/derived_functors#prop8)의 쌍대 명제에 의한다.)
:::

[\[대수다양체\] §층 코호몰로지](/ko/math/algebraic_varieties/sheaf_cohomology)에서 도입한 Čech cohomology의 정의 또한 그대로 옮겨진다. Scheme $X$의 open cover $\mathcal{U}=\{U_i\}_{i\in I}$와 sheaf $\mathcal{F}$에 대하여, Čech complex $\check C^\bullet(\mathcal{U}, \mathcal{F})$와 그 cohomology $\check H^p(\mathcal{U}, \mathcal{F})$는 ([\[대수다양체\] §층 코호몰로지, ⁋정의 3](/ko/math/algebraic_varieties/sheaf_cohomology#def3), [\[대수다양체\] §층 코호몰로지, ⁋정의 4](/ko/math/algebraic_varieties/sheaf_cohomology#def4)) 위상공간 수준의 정의이므로 scheme 위에서도 곧바로 의미를 가진다. 우리의 목표는 좋은 covering에 대하여 Čech cohomology가 [정의 1](#def1)의 derived functor cohomology와 일치함을 보이는 것이며, 그 핵심에는 affine scheme 위의 소멸 정리가 있다.

## Serre의 affine 소멸 정리

[\[대수다양체\] §층 코호몰로지, ⁋명제 12](/ko/math/algebraic_varieties/sheaf_cohomology#prop12)는 affine variety 위에서 quasi-coherent sheaf의 higher cohomology가 소멸한다는 것이었다. 이를 임의의 affine scheme $\Spec A$ 위로 끌어올린 것이 다음의 Serre 소멸 정리이며, scheme cohomology 이론 전체의 토대가 된다.

::: 정리 3 (Serre의 affine 소멸)
Affine scheme $X=\Spec A$와 그 위의 quasi-coherent sheaf $\mathcal{F}=\widetilde M$에 대하여,

$$H^i(X, \mathcal{F})=0 \qquad (i>0)$$

이 성립한다.
:::
::: 증명
[§준연접층, ⁋정리 9](/ko/math/scheme_theory/quasicoherent_sheaves#thm9)에 의하여 $\QCoh(\Spec A)$는 $\rMod{A}$와 동치이므로, $\mathcal{F}=\widetilde M$인 $A$-module $M$이 존재한다. $\rMod{A}$는 enough injective를 가지므로 $M$의 injective resolution

$$0 \rightarrow M \rightarrow I^0 \rightarrow I^1 \rightarrow \cdots$$

을 잡자. associated sheaf functor $\widetilde{(-)}$는 exact이므로 ([§준연접층, ⁋명제 6](/ko/math/scheme_theory/quasicoherent_sheaves#prop6)),

$$0 \rightarrow \widetilde M \rightarrow \widetilde{I^0} \rightarrow \widetilde{I^1} \rightarrow \cdots$$

은 $\Spec A$ 위의 sheaf의 resolution이다. 우리의 주장은 각각의 $\widetilde{I^k}$이 $\Gamma(\Spec A, -)$-acyclic이라는 것이며, 이것이 성립하면 [\[대수다양체\] §층 코호몰로지, ⁋명제 17](/ko/math/algebraic_varieties/sheaf_cohomology#prop17)의 acyclic resolution 논증에 의하여

$$H^i(\Spec A, \widetilde M)\cong H^i\bigl(\Gamma(\Spec A, \widetilde{I^\bullet})\bigr)=H^i(I^\bullet)$$

을 얻는다. 여기에서 두 번째 등식은 associated sheaf의 global section이 원래의 module이라는 것에서 따라오며 ([§준연접층, ⁋정의 4](/ko/math/scheme_theory/quasicoherent_sheaves#def4)), $M \rightarrow I^\bullet$이 quasi-isomorphism이므로 우변의 cohomology는 $i>0$에서 모두 소멸한다. 따라서 $H^i(\Spec A, \widetilde M)=0$ ($i>0$)이다.

남은 것은 injective $A$-module $I$의 associated sheaf $\widetilde I$이 acyclic이라는 것이다. 이를 위해 우리는 $\widetilde I$이 flasque임을 보이며, flasque sheaf가 $\Gamma(X, -)$-acyclic이라는 것은 이미 알고 있다. ([\[대수다양체\] §층 코호몰로지, ⁋명제 16](/ko/math/algebraic_varieties/sheaf_cohomology#prop16)) Flasque임을 보이는 것은 Noetherian 가정 아래에서 가장 명료하므로 그 경우를 먼저 다룬다. $A$가 Noetherian ring이라 하자. $\Spec A$의 열린집합은 모두 $U=\Spec A\setminus V(\mathfrak{a})$의 꼴이므로, 각각에 대하여 restriction $\widetilde I(\Spec A)=I\rightarrow\widetilde I(U)$이 surjective임을 보이면 된다. Quasi-coherent sheaf의 section을 local cohomology와 잇는 exact sequence

$$I\longrightarrow\widetilde I(U)\longrightarrow H^1_{\mathfrak{a}}(I)\longrightarrow 0$$

이 성립하는데, 여기서 $H^i_{\mathfrak{a}}(M)=\varinjlim_n\Ext^i_A(A/\mathfrak{a}^n,M)$이다. $I$가 injective이므로 모든 $n$에서 $\Ext^1_A(A/\mathfrak{a}^n,I)=0$이어서 $H^1_{\mathfrak{a}}(I)=0$이고, 따라서 위 restriction이 surjective이다. 그럼 임의의 두 열린집합 $V\subseteq U$에 대하여 $I \rightarrow \widetilde I(V)$이 $\widetilde I(U)$를 지나 인수분해되므로 $\widetilde I(U) \rightarrow \widetilde I(V)$ 또한 surjective이고, 곧 $\widetilde I$은 flasque이다 (Hartshorne III.3.4).

$A$가 Noetherian이 아닌 경우에도 결론은 그대로 성립하지만, injective module을 경유하는 위의 논증은 통하지 않는다. 이때에는 principal open set들로 이루어진 cover에 대한 Čech complex $\check C^\bullet(\mathcal{U}, \widetilde M)$이 $p>0$에서 exact함을 직접 보인 뒤, 이러한 cover들이 $\Spec A$의 위상의 기저를 이룬다는 것으로부터 derived functor cohomology로 옮기는 별개의 논증이 필요하다. 이는 이 글의 범위를 벗어나므로 여기에서는 증명을 생략하고 [Stacks]에 위임하며, 그 소멸 결과만을 가져다 쓴다. 이하에서 Noetherian 가정 없는 형태가 실제로 필요한 곳은 임의의 ring $A$ 위의 사영공간을 다루는 [정리 6](#thm6)뿐이다.
:::

[정리 3](#thm3)의 핵심은 affine scheme이 cohomology의 관점에서 "단순한" 공간이라는 것이다. 즉 affine 위에서는 quasi-coherent sheaf의 정보가 모두 $H^0$, 곧 그 global section module에 담겨 있으며, higher cohomology는 어떠한 새로운 정보도 주지 않는다. 이는 위상공간이 Čech cohomology의 관점에서 contractible한 것에 대응하는 대수기하학적 현상이다.

이로부터 곧바로 affine covering에 대한 Leray 정리를 scheme 수준에서 얻는다. [\[대수다양체\] §층 코호몰로지, ⁋정리 11](/ko/math/algebraic_varieties/sheaf_cohomology#thm11)은 cover $\mathcal{U}$의 모든 유한 교집합 위에서 $\mathcal{F}$가 acyclic이면 $\check H^p(\mathcal{U}, \mathcal{F})\cong H^p(X, \mathcal{F})$임을 주는데, 이는 위상공간 수준의 정리이므로 scheme 위에서도 그대로 적용된다.

::: 따름정리 4
Separated scheme $X$와 ([§값매김환, ⁋정의 3](/ko/math/scheme_theory/valuative_criteria#def3)) 그 위의 quasi-coherent sheaf $\mathcal{F}$, 그리고 affine open cover $\mathcal{U}=\{U_i\}$에 대하여, 모든 $p$에 대해

$$\check H^p(\mathcal{U}, \mathcal{F})\cong H^p(X, \mathcal{F})$$

이 성립한다.
:::
::: 증명
[\[대수다양체\] §층 코호몰로지, ⁋정리 11](/ko/math/algebraic_varieties/sheaf_cohomology#thm11)에 의하여, $\mathcal{U}$의 임의의 유한 교집합 $U_{i_0}\cap\cdots\cap U_{i_p}$ 위에서 $\mathcal{F}$가 acyclic임을 보이면 충분하다. $X$가 separated이므로 diagonal morphism $\Delta:X \rightarrow X\times_{\Spec \mathbb{Z}}X$이 closed immersion이고, 따라서 임의의 두 affine open subset $U_i, U_j$의 교집합 $U_i\cap U_j$는 다시 affine이다. 실제로 $U_i\cap U_j$는 fiber product $U_i\times_X U_j$이며, 이는 affine scheme $U_i\times_{\Spec \mathbb{Z}}U_j$의 closed subscheme $\Delta^{-1}(U_i\times U_j)$와 동형이므로 affine이다. 같은 논증을 반복하면 유한 교집합 $U_{i_0}\cap\cdots\cap U_{i_p}$ 또한 affine scheme이다. 그럼 $\mathcal{F}$의 이 위로의 restriction은 affine scheme 위의 quasi-coherent sheaf이므로 [정리 3](#thm3)에 의하여 acyclic이고, 따라서 [\[대수다양체\] §층 코호몰로지, ⁋정리 11](/ko/math/algebraic_varieties/sheaf_cohomology#thm11)의 전제가 충족된다.
:::

따라서 separated scheme 위에서는 affine covering 하나를 잡아 Čech complex만 계산하면 derived functor cohomology가 그대로 얻어진다. Affine scheme 사이의 morphism은 항상 separated이고 ([§값매김환, ⁋보조정리 5](/ko/math/scheme_theory/valuative_criteria#lem5)), $\mathbb{P}^n$을 비롯한 projective scheme 또한 separated이므로, 우리가 실제로 다루는 대부분의 scheme에서 이 비교가 작동한다.

## 사영공간 위의 line bundle

이제 affine covering에 대한 Čech 계산을 사용하여 사영공간 위의 line bundle $\mathcal{O}(d)$의 cohomology를 scheme 수준에서 다룬다. 우선 $\mathcal{O}(d)$를 graded module의 언어로 정의한다. Ring $A$ 위의 사영공간은 $\mathbb{P}^n_A=\Proj A[\x_0,\ldots, \x_n]$이며 ([§사영공간과 Proj 구성, ⁋정의 1](/ko/math/scheme_theory/projective_schemes#def1)), 이는 standard affine cover $\mathcal{U}=\{D_+(\x_i)\}_{i=0}^n$을 가진다.

::: 정의 5
$S=A[\x_0,\ldots, \x_n]$을 standard grading을 가진 graded ring이라 하고, $S(d)$를 $S(d)_m=S_{d+m}$으로 grading을 옮긴 graded $S$-module이라 하자. 그럼 standard affine cover $\mathcal{U}=\{D_+(\x_i)\}$ 위에서 각각의 $D_+(\x_i)=\Spec S_{(\x_i)}$에

$$\mathcal{O}(d)(D_+(\x_i))=\bigl(S(d)_{\x_i}\bigr)_0=\x_i^d\cdot S_{(\x_i)}$$

을 대응시키고, 겹치는 부분 위에서 자연스러운 동일시로 붙여 얻는 $\mathbb{P}^n_A$ 위의 invertible sheaf를 *twisting sheaf<sub>꼬임층</sub>* $\mathcal{O}(d)$라 부른다.
:::

여기에서 $S_{(\x_i)}$은 $S_{\x_i}$의 degree $0$ 부분이며, $\x_i^d\cdot S_{(\x_i)}$은 $S_{\x_i}$ 안에서 degree $d$인 원소들의 모임이다. 각 chart 위에서 $\mathcal{O}(d)\vert_{D_+(\x_i)}$은 $\x_i^d$를 generator로 하는 자유 $S_{(\x_i)}$-module이므로 rank $1$ free이고, 따라서 $\mathcal{O}(d)$는 invertible sheaf이다. ([§준연접층, ⁋정의 12](/ko/math/scheme_theory/quasicoherent_sheaves#def12)) $d=0$인 경우 $\mathcal{O}(0)=\mathcal{O}_{\mathbb{P}^n_A}$이고, $\mathcal{O}(d)\otimes\mathcal{O}(e)\cong\mathcal{O}(d+e)$가 성립하므로 $\mathcal{O}(d)\cong\mathcal{O}(1)^{\otimes d}$이다. 이 정의는 [\[대수다양체\] §사영공간의 코호몰로지](/ko/math/algebraic_varieties/cohomology_of_projective_spaces)에서 variety 위의 $\mathcal{O}(d)$를 chart별 section으로 기술한 것과 정확히 일치한다.

이제 cohomology를 계산한다. $\mathbb{P}^n_A$은 separated이므로 [따름정리 4](#cor4)에 의해 standard affine cover에 대한 Čech complex를 계산하면 충분하다. 그 결과는 variety의 경우와 형태가 동일하다.

::: 정리 6 (Bott)
Ring $A$ 위의 사영공간 $\mathbb{P}^n_A$의 line bundle $\mathcal{O}(d)$의 cohomology는

$$H^q(\mathbb{P}^n_A, \mathcal{O}(d))=\begin{cases}A[\x_0,\ldots, \x_n]_d & q=0,\ d\geq 0 \\ A[\x_0^{-1},\ldots, \x_n^{-1}]_{-d-n-1} & q=n,\ d\leq -n-1 \\ 0 & \text{otherwise}\end{cases}$$

로 주어진다. 특히 $0<q<n$에서는 모든 $d$에 대해 소멸한다.
:::
::: 증명
$\mathbb{P}^n_A$이 separated scheme이므로 [따름정리 4](#cor4)에 의하여 standard affine cover $\mathcal{U}=\{D_+(\x_i)\}$에 대한 Čech cohomology가 곧 derived functor cohomology이다. 그런데 이 Čech complex는 [\[대수다양체\] §사영공간의 코호몰로지, ⁋명제 1](/ko/math/algebraic_varieties/cohomology_of_projective_spaces#prop1)의 증명에 등장하는 것과 글자 그대로 같다. 즉 각 교집합 $D_+(\x_{i_0}\cdots\x_{i_p})$ 위에서 $\mathcal{O}(d)$의 section은 $\x_{i_0},\ldots, \x_{i_p}$만을 분모로 허용하는 $d$차 monomial들

$$\x_0^{a_0}\cdots\x_n^{a_n}, \qquad \sum_{j=0}^n a_j=d,\quad a_j\geq 0\ \text{for}\ j\not\in\{i_0,\ldots, i_p\}$$

로 $A$ 위에서 생성되며, coboundary map 또한 동일한 교대합 공식으로 주어진다. Variety의 경우 계수체 $\mathbb{K}$ 위에서 진행한 계산은 사실 어떤 base ring $A$ 위에서든 monomial 단위로 동일하게 작동하므로, 그 증명을 $A$-계수로 그대로 읽으면 위의 결과를 얻는다. 구체적으로 $n=1$에서는 Čech complex $0 \rightarrow \check C^0 \xrightarrow{\delta} \check C^1 \rightarrow 0$의 $\ker\delta$가 $d\geq 0$일 때 $A[\x_0,\x_1]_d$이고 $\coker\delta$가 $d\leq -2$일 때 두 지수가 모두 음수인 $d$차 monomial들로 생성됨을 직접 확인하며, 일반적인 $n$은 hyperplane $\{\x_n=0\}$이 주는 short exact sequence

$$0 \rightarrow \mathcal{O}(d-1)\xrightarrow{\times\x_n}\mathcal{O}(d) \rightarrow \mathcal{O}(d)\vert_{\mathbb{P}^{n-1}_A} \rightarrow 0$$

의 long exact sequence를 ([명제 2](#prop2)) 사용한 $n$에 대한 귀납으로 처리한다. 중간 차원에서의 소멸과 top 차원에서의 $\coker$ 계산이 모두 variety의 경우와 일치한다.

마지막으로 $q=n$, $d\leq -n-1$에서 얻어지는 공간이 표기 $A[\x_0^{-1},\ldots, \x_n^{-1}]_{-d-n-1}$로 적히는 이유는 [\[대수다양체\] §사영공간의 코호몰로지, ⁋명제 1](/ko/math/algebraic_varieties/cohomology_of_projective_spaces#prop1) 직후의 설명과 동일하다. 즉 모든 지수가 $-1$ 이하인 $d$차 monomial들을 $\y_j=\x_j^{-1}$로 치환하면 $\lvert d\rvert-(n+1)=-d-n-1$차의 "음의 degree" monomial 공간이 된다.
:::

[정리 6](#thm6)에서 $d\geq 0$일 때 $H^0(\mathbb{P}^n_A, \mathcal{O}(d))=A[\x_0,\ldots, \x_n]_d$이 degree $d$ homogeneous polynomial들의 free $A$-module이라는 것은 $\mathcal{O}(d)$의 global section이 곧 $S_d$임을 다시 확인해 준다. 또 양 끝 차원 $H^0$와 $H^n$ 사이에는 Serre duality

$$H^n(\mathbb{P}^n_A, \mathcal{O}(d))\cong H^0(\mathbb{P}^n_A, \mathcal{O}(-d-n-1))^\vee$$

의 그림자가 보인다. 실제로 $A=\mathbb{K}$가 field일 때 $H^n(\mathbb{P}^n, \mathcal{O}(d))$의 차원은 $\dim H^0(\mathbb{P}^n, \mathcal{O}(-d-n-1))$과 같으며, 이는 canonical bundle이 $\mathcal{O}(-n-1)$이라는 사실의 반영이다. 한편 모든 중간 cohomology $H^q$ ($0<q<n$)이 소멸한다는 것은 사영공간이 cohomology의 관점에서 매우 단순한 공간임을 보여주며, 이는 다음 절에서 일반적인 coherent sheaf의 cohomology를 통제하는 출발점이 된다.

## Noetherian projective scheme 위의 연접층

이제 임의의 Noetherian projective scheme $X$와 그 위의 coherent sheaf ([§준연접층, ⁋정의 11](/ko/math/scheme_theory/quasicoherent_sheaves#def11)) $\mathcal{F}$에 대하여, cohomology의 두 가지 근본적 성질을 다룬다. 하나는 각 $H^i(X, \mathcal{F})$이 유한차원이라는 것이고, 다른 하나는 충분히 twist하면 higher cohomology가 소멸한다는 Serre vanishing이다. Projective scheme $X$는 어떤 사영공간 $\mathbb{P}^n_{\mathbb{K}}$의 closed subscheme이며, 그 위에 $\mathcal{O}_X(1)=\mathcal{O}_{\mathbb{P}^n}(1)\vert_X$을 twisting을 위한 line bundle로 사용한다. 좌표들의 restriction $\x_0\vert_X,\ldots, \x_n\vert_X$이 $\mathcal{O}_X(1)$을 globally generate하고 이들이 정의하는 morphism이 곧 포함사상 $X\hookrightarrow\mathbb{P}^n_\mathbb{K}$이므로, $\mathcal{O}_X(1)$은 very ample invertible sheaf이다. ([§인자와 선형계, ⁋정의 17](/ko/math/scheme_theory/divisors_and_linear_systems#def17)) Coherent sheaf $\mathcal{F}$에 대해 $\mathcal{F}(d)=\mathcal{F}\otimes_{\mathcal{O}_X}\mathcal{O}_X(d)$로 적는다.

먼저 closed immersion을 따라 cohomology가 보존된다는 관찰이 핵심이다. Closed embedding $\iota:X\hookrightarrow\mathbb{P}^n_{\mathbb{K}}$은 affine 사상이므로, pushforward $\iota_\ast$가 affine 위에서 정확하고 higher direct image를 만들지 않아 $H^i(X, \mathcal{F})\cong H^i(\mathbb{P}^n, \iota_\ast\mathcal{F})$이 성립한다. 따라서 두 성질 모두 $X=\mathbb{P}^n_{\mathbb{K}}$인 경우로 환원된다.

::: 정리 7
Field $\mathbb{K}$ 위의 Noetherian projective scheme $X$와 그 위의 coherent sheaf $\mathcal{F}$에 대하여, 각 $H^i(X, \mathcal{F})$은 유한차원 $\mathbb{K}$-벡터공간이며, 충분히 큰 $i$에 대해서는 $0$이다.
:::
::: 증명
위에서 관찰하였듯 closed immersion $\iota:X\hookrightarrow\mathbb{P}^n_{\mathbb{K}}$을 통해 $H^i(X, \mathcal{F})\cong H^i(\mathbb{P}^n, \iota_\ast\mathcal{F})$이고, $\iota_\ast\mathcal{F}$은 $\mathbb{P}^n$ 위의 coherent sheaf이므로 ([§준연접층, ⁋정리 16](/ko/math/scheme_theory/quasicoherent_sheaves#thm16)에 의해 준연접이고 finite type 또한 보존된다) $X=\mathbb{P}^n_{\mathbb{K}}$이라 가정해도 된다.

이제 $\mathbb{P}^n$ 위의 coherent sheaf $\mathcal{F}$에 대하여 cohomological dimension $n$, 즉 $i>n$에서 $H^i=0$임을 먼저 본다. $\mathbb{P}^n$은 $n+1$개의 affine 열린집합 $D_+(\x_i)$로 덮이므로, 이 cover에 대한 Čech complex $\check C^\bullet$은 $p>n$에서 $\check C^p=0$이다. ([따름정리 4](#cor4)) 따라서 $H^i(\mathbb{P}^n, \mathcal{F})=\check H^i=0$ ($i>n$)이다.

유한차원성은 $i$에 대한 내림차순 귀납으로 보인다. $i>n$인 경우는 위에서 $0$이므로 자명하다. 임의의 coherent sheaf $\mathcal{F}$에 대하여, 적당한 $d\gg 0$에 대해 $\mathcal{F}(d)$이 globally generated이므로 ([\[대수다양체\] §사영공간의 코호몰로지, ⁋정의 6](/ko/math/algebraic_varieties/cohomology_of_projective_spaces#def6) 이후 논증) 유한 개의 global section이 surjection

$$\mathcal{O}_{\mathbb{P}^n}^{\oplus r} \twoheadrightarrow \mathcal{F}(d)$$

을 주고, 이를 $\mathcal{O}(-d)$로 twist하면 $\mathcal{O}(-d)^{\oplus r}\twoheadrightarrow\mathcal{F}$을 얻는다. 그 kernel $\mathcal{G}$ 또한 coherent sheaf이므로 ($\mathbb{P}^n$이 Noetherian이라 kernel이 finite type을 유지한다) short exact sequence

$$0 \rightarrow \mathcal{G} \rightarrow \mathcal{O}(-d)^{\oplus r} \rightarrow \mathcal{F} \rightarrow 0$$

의 long exact sequence에서 ([명제 2](#prop2))

$$H^i(\mathbb{P}^n, \mathcal{O}(-d)^{\oplus r}) \rightarrow H^i(\mathbb{P}^n, \mathcal{F}) \rightarrow H^{i+1}(\mathbb{P}^n, \mathcal{G})$$

을 본다. 좌변은 [정리 6](#thm6)에 의하여 유한차원이고, 우변은 귀납 가정에 의하여 유한차원이므로 ($i+1$에서의 유한차원성), 가운데 항 $H^i(\mathbb{P}^n, \mathcal{F})$ 또한 유한차원이다. 이로써 모든 $i$에 대한 유한차원성을 얻는다.
:::

[정리 7](#thm7)은 projective scheme 위의 coherent sheaf가 좋은 유한성을 가짐을 보장한다. 이는 affine 위의 finitely generated module에 대한 유한성이 cohomology 수준에서 사영적 상황으로 옮겨진 것이며, [\[대수다양체\] §사영공간의 코호몰로지, ⁋정의 2](/ko/math/algebraic_varieties/cohomology_of_projective_spaces#def2)의 Euler characteristic과 같은 불변량이 잘 정의되는 근거가 된다. 위 증명의 귀납에 사용한 globally generated 성질과 twist 후의 소멸은 다음 Serre vanishing에서 정량적으로 다시 등장한다.

::: 정리 8 (Serre Vanishing)
Field $\mathbb{K}$ 위의 Noetherian projective scheme $X$와 closed immersion $X\hookrightarrow\mathbb{P}^n_\mathbb{K}$이 주는 very ample line bundle $\mathcal{O}_X(1)$ ([§인자와 선형계, ⁋정의 17](/ko/math/scheme_theory/divisors_and_linear_systems#def17)), 그리고 coherent sheaf $\mathcal{F}$에 대하여, 충분히 큰 $d\gg 0$에 대해

$$H^i(X, \mathcal{F}(d))=0 \qquad (i>0)$$

이 성립한다. 더욱이 이러한 $d$에 대해 $\mathcal{F}(d)$은 globally generated이다.
:::
::: 증명
[정리 7](#thm7)에서와 같이 closed immersion $\iota:X\hookrightarrow\mathbb{P}^n_{\mathbb{K}}$을 통해 $X=\mathbb{P}^n_{\mathbb{K}}$이고 $\mathcal{O}_X(1)=\mathcal{O}(1)$인 경우로 환원한다. 이 환원이 정당한 것은 $\iota$가 closed immersion이라 $\iota_\ast(\mathcal{F}(d))\cong(\iota_\ast\mathcal{F})(d)$이고 ($\mathcal{O}_X(1)=\iota^\ast\mathcal{O}(1)$이므로 projection formula로부터), cohomology가 $\iota_\ast$ 아래에서 보존되기 때문이다.

먼저 $\mathcal{F}(d)$이 $d\gg0$에서 globally generated임을 본다. $S=\mathbb{K}[\x_0,\ldots, \x_n]$로 두고 graded $S$-module $\Gamma_\ast(\mathcal{F})=\bigoplus_{m\in\mathbb{Z}}\Gamma(\mathbb{P}^n, \mathcal{F}(m))$을 생각하면, 각 표준 affine $D_+(\x_j)$ 위에서 $\Gamma(D_+(\x_j), \mathcal{F})$은 degree $0$ localization $\Gamma_\ast(\mathcal{F})_{(\x_j)}$이고 이는 $S_{(\x_j)}$ 위의 finitely generated module이다. 각 generator를 $m_k/\x_j^{e_k}$ 꼴로 적고 $d_0=\max_{j,k}e_k$로 두면, $\x_j^{d_0-e_k}$를 곱한 $m_k\cdot\x_j^{d_0-e_k}\in\Gamma(\mathbb{P}^n, \mathcal{F}(d_0))$들이 $D_+(\x_j)$ 위에서 $\mathcal{F}(d_0)$의 stalk를 생성한다. $j$에 대해 최댓값을 취하면 $\mathcal{F}(d_0)$이 globally generated이고, $d\geq d_0$이면 $\mathcal{F}(d)=\mathcal{F}(d_0)\otimes\mathcal{O}(d-d_0)$ 또한 globally generated이다.

이제 vanishing을 $i$에 대한 내림차순 귀납으로 본다. $i>n$에서는 [정리 7](#thm7)의 cohomological dimension에 의해 $H^i=0$이다. 임의의 $i\geq1$에 대하여, globally generated 성질로부터 surjection $\mathcal{O}^{\oplus r}\twoheadrightarrow\mathcal{F}(d_0)$을 잡고 kernel $\mathcal{K}$를 coherent sheaf로 하여 short exact sequence

$$0 \rightarrow \mathcal{K} \rightarrow \mathcal{O}^{\oplus r} \rightarrow \mathcal{F}(d_0) \rightarrow 0$$

을 얻자. 이를 $\mathcal{O}(d-d_0)$로 twist하면

$$0 \rightarrow \mathcal{K}(d-d_0) \rightarrow \mathcal{O}(d-d_0)^{\oplus r} \rightarrow \mathcal{F}(d) \rightarrow 0$$

이고, 그 long exact sequence에서 ([명제 2](#prop2))

$$H^i(\mathbb{P}^n, \mathcal{O}(d-d_0)^{\oplus r}) \rightarrow H^i(\mathbb{P}^n, \mathcal{F}(d)) \rightarrow H^{i+1}(\mathbb{P}^n, \mathcal{K}(d-d_0))$$

을 본다. 좌변은 [정리 6](#thm6)에 의하여 $d-d_0\gg0$이고 $i>0$이면 $0$이다. 우변은 귀납 가정을 $\mathcal{K}$에 적용한 것으로, $i+1$에서의 vanishing이 충분히 큰 twist에 대해 성립한다. 따라서 충분히 큰 $d$에 대해 가운데 항 $H^i(\mathbb{P}^n, \mathcal{F}(d))$이 양쪽에서 끼여 소멸한다. $i$가 $1$부터 $n$까지 유한하므로, 모든 $i>0$에 대한 vanishing을 동시에 보장하는 공통의 $d_1$을 잡을 수 있고, $d\geq d_1$에서 $H^i(\mathbb{P}^n, \mathcal{F}(d))=0$ ($i>0$)이다.
:::

[정리 8](#thm8)은 [\[대수다양체\] §사영공간의 코호몰로지, ⁋명제 4](/ko/math/algebraic_varieties/cohomology_of_projective_spaces#prop4)의 Serre vanishing을 scheme 수준으로 옮긴 것으로, 그 증명의 골격은 line bundle의 cohomology를 아는 $\mathbb{P}^n$으로 환원한 뒤 coherent sheaf를 free sheaf의 quotient로 분해하여 dimension shifting을 반복하는 것이다. 정성적으로 이 정리는 임의의 coherent sheaf가 충분히 양의 방향으로 twist되면 사영공간 위의 line bundle처럼 "고차 정보가 사라지는" 단계에 도달함을 말해 준다. 함께 얻은 global generation은 twist된 sheaf가 global section만으로 완전히 생성됨을 뜻하며, 이는 coherent sheaf를 free sheaf의 resolution으로 표현하는 출발점이 되어 projective scheme 위의 homology적 대수의 토대를 이룬다.

## Ampleness의 코호몰로지 판정

[정리 8](#thm8)의 증명에서 실제로 사용한 것은 $\mathcal{O}_X(1)$이 $X$를 사영공간 안으로 넣는 embedding에서 온다는 것, 곧 very ample이라는 것뿐이었다. 반면 [§인자와 선형계](/ko/math/scheme_theory/divisors_and_linear_systems)에서 정의한 ampleness는 사영공간을 전혀 언급하지 않고 오직 twist 후의 global generation만을 요구하는 조건이었다. 이 절에서 우리는 두 조건이 거듭제곱을 허용하면 일치한다는 것과, ampleness가 higher cohomology의 소멸만으로 판정된다는 Serre의 결과를 다룬다.

::: 따름정리 9
Field $\mathbb{K}$ 위의 Noetherian projective scheme $X$ 위의 very ample invertible sheaf $\mathcal{L}$은 ample이다. ([§인자와 선형계, ⁋정의 18](/ko/math/scheme_theory/divisors_and_linear_systems#def18))
:::
::: 증명
$\mathcal{L}$이 very ample이므로 이를 globally generate하는 유한 개의 절단이 locally closed embedding $\iota:X \rightarrow \mathbb{P}^N_\mathbb{K}$를 정의하고 $\mathcal{L}\cong\iota^\ast\mathcal{O}(1)$이다. $X$가 $\mathbb{K}$ 위에서 projective이므로 $\iota(X)$는 닫힌집합이며 ([§값매김환, ⁋따름정리 16](/ko/math/scheme_theory/valuative_criteria#cor16)), 따라서 $\iota$는 closed immersion이다. 그럼 $\mathcal{L}$은 [정리 8](#thm8)에서 $\mathcal{O}_X(1)$이 맡은 역할을 그대로 할 수 있으므로, 임의의 coherent sheaf $\mathcal{F}$에 대하여 충분히 큰 모든 $d$에서 $\mathcal{F}\otimes\mathcal{L}^{\otimes d}$은 globally generated이다. 이것이 ampleness의 정의이다.
:::

역방향은 그대로 성립하지 않는다. Ample invertible sheaf는 절단이 부족하여 embedding을 주지 못할 수 있고, 이를 해소하려면 여러 번 tensor하여 절단을 늘려야 한다. 다음 정리는 그것이 언제나 가능함을 말해준다.

::: 정리 10
Field $\mathbb{K}$ 위의 Noetherian projective scheme $X$ 위의 invertible sheaf $\mathcal{L}$에 대하여, $\mathcal{L}$이 ample인 것과 적당한 $m>0$에 대하여 $\mathcal{L}^{\otimes m}$이 very ample인 것은 서로 동치이다.
:::
::: 증명
$\mathcal{L}^{\otimes m}$이 very ample이라 하자. [따름정리 9](#cor9)에 의하여 $\mathcal{L}^{\otimes m}$은 ample이고, [§인자와 선형계, ⁋명제 19](/ko/math/scheme_theory/divisors_and_linear_systems#prop19)의 2번에 의하여 $\mathcal{L}$ 또한 ample이다.

거꾸로 $\mathcal{L}$이 ample이라 하자. Closed point $x\in X$를 고정하고, $\mathcal{L}$이 trivialize되는 affine open neighborhood $U\ni x$를 잡자. $Y=X\setminus U$에 reduced closed subscheme 구조를 주어 그 ideal sheaf $\mathcal{I}_Y$를 생각하면 이는 coherent sheaf이므로, ampleness에 의하여 적당한 $n>0$에 대해 $\mathcal{I}_Y\otimes\mathcal{L}^{\otimes n}$은 globally generated이다. $x\notin Y$이므로 $(\mathcal{I}_Y)_x=\mathcal{O}_{X,x}$이고, 따라서 $x$에서 소멸하지 않는 절단 $s\in\Gamma(X, \mathcal{I}_Y\otimes\mathcal{L}^{\otimes n})\subseteq\Gamma(X, \mathcal{L}^{\otimes n})$이 존재한다. 이 $s$는 $Y$ 위에서 소멸하므로 $s$가 stalk를 생성하는 점들의 열린집합 $X_s$는 ([§인자와 선형계, §§Ample invertible sheaf](/ko/math/scheme_theory/divisors_and_linear_systems#ample-invertible-sheaf)) $U$에 포함되고, $U$ 위에서 $\mathcal{L}^{\otimes n}$을 trivialize하면 $s$는 함수 $f\in\Gamma(U, \mathcal{O}_X)$에 대응하여 $X_s=D(f)$는 affine이다.

$X$가 $\mathbb{K}$ 위에서 finite type이므로 각 affine chart의 coordinate ring은 Jacobson ring이고 ([\[가환대수학\] §영점정리, ⁋정리 4](/ko/math/commutative_algebra/nullstellensatz#thm4)), 따라서 $X$의 공집합이 아닌 닫힌집합은 언제나 $X$의 closed point를 포함한다. 곧 closed point들에서 얻은 위의 열린집합들의 합집합은 여집합이 closed point를 갖지 않는 닫힌집합이라 $X$ 전체이며, $X$가 quasi-compact이므로 그 가운데 유한 개 $X_{s_1},\ldots, X_{s_k}$만으로도 $X$를 덮는다. 여기에서 $s_i\in\Gamma(X, \mathcal{L}^{\otimes n_i})$라 하고 $m$을 $n_i$들의 최소공배수라 하자. 임의의 $e\geq1$에 대해 $X_{s^e}=X_s$이므로 $s_i$를 $s_i^{m/n_i}$로 바꾸면 cover를 유지한 채 모든 $i$에 대해 $s_i\in\Gamma(X, \mathcal{L}^{\otimes m})$이라 가정할 수 있다. 또 $X$가 $\mathbb{K}$ 위에서 finite type이므로 각각의 $B_i=\Gamma(X_{s_i}, \mathcal{O}_X)$는 finitely generated $\mathbb{K}$-대수이고, 그 generator $b_{i1},\ldots, b_{ir_i}$를 택하자.

이제 충분히 큰 공통의 $N$에 대하여 $s_i^Nb_{ij}$가 $X$ 전체의 절단 $t_{ij}\in\Gamma(X, \mathcal{L}^{\otimes mN})$으로 연장됨을 본다. $\mathcal{L}^{\otimes m}$이 trivialize되는 유한 개의 affine open subset $V_1,\ldots, V_p$로 $X$를 덮고 각각의 $V_l=\Spec A_l$ 위에서 trivialization을 하나 고정하면, $s_i$는 함수 $g_l\in A_l$에 대응하고 $X_{s_i}\cap V_l=D(g_l)$이다. 그럼 $b_{ij}$의 $D(g_l)$로의 restriction은 $(A_l)_{g_l}$의 원소이므로 $g_l$의 충분히 큰 거듭제곱을 곱하면 $A_l$의 원소가 되고, 유한 개의 $l$과 $j$에 대해 지수의 최댓값 $N_0$을 취하면 각각의 $V_l$ 위에서 $s_i^{N_0}b_{ij}$가 $\mathcal{L}^{\otimes mN_0}$의 절단으로 연장된다. 서로 다른 두 chart 위의 연장은 $X_{s_i}\cap V_l\cap V_{l'}$ 위에서 일치하므로, 남은 것은 그 차를 겹침 전체에서 죽이는 일이다. $X$가 Noetherian이라 $V_l\cap V_{l'}$은 유한 개의 affine open subset $\Spec C$로 덮이는데, 그 각각의 위에서 $\mathcal{L}^{\otimes mN_0}$을 trivialize하면 두 연장의 차는 $C$의 원소 $h$가 되고 $s_i$에 대응하는 함수 $g\in C$에 대해 $h$의 $D(g)$로의 restriction이 $0$이므로 $C_g$에서 $h=0$, 곧 적당한 지수 $c$에 대해 $g^ch=0$이다. 이러한 유한 개의 지수의 최댓값을 $N_0$에 더해 $N$으로 두면 $s_i^Nb_{ij}$의 chart별 연장들이 모든 겹침 위에서 일치하고, 따라서 이들이 붙어 원하는 global section $t_{ij}\in\Gamma(X, \mathcal{L}^{\otimes mN})$을 준다.

이제 절단들 $s_1^N,\ldots, s_k^N$과 $t_{ij}$들을 함께 생각하자. $X_{s_i^N}=X_{s_i}$들이 $X$를 덮으므로 이들은 $\mathcal{L}^{\otimes mN}$을 globally generate하고, 따라서 morphism $\varphi:X \rightarrow \mathbb{P}^M_\mathbb{K}$를 정의한다. ([§인자와 선형계, §§Ample invertible sheaf](/ko/math/scheme_theory/divisors_and_linear_systems#ample-invertible-sheaf)) $s_i^N$에 대응하는 좌표가 소멸하지 않는 standard chart를 $V_i\subseteq\mathbb{P}^M_\mathbb{K}$라 하면 $\varphi^{-1}(V_i)=X_{s_i}$이고, $\varphi$의 구성에 의하여 $\varphi\vert_{X_{s_i}}:X_{s_i} \rightarrow V_i$는 좌표를 $t_{ij}/s_i^N=b_{ij}$로 보내는 ring homomorphism에 대응한다. $b_{ij}$들이 $B_i$를 생성하므로 이 homomorphism은 surjective이고, 따라서 $\varphi\vert_{X_{s_i}}$는 closed immersion이다. ([§아핀스킴, ⁋정리 13](/ko/math/scheme_theory/affine_schemes#thm13), [§닫힌 부분스킴, ⁋명제 3](/ko/math/scheme_theory/closed_subschemes#prop3)) Closed immersion인 것은 target에 대해 국소적인 조건이므로 $\varphi$는 열린집합 $\bigcup_iV_i$ 위로의 closed immersion, 곧 locally closed embedding이며 $\mathcal{L}^{\otimes mN}\cong\varphi^\ast\mathcal{O}(1)$은 very ample이다.
:::

[정리 10](#thm10)은 ampleness가 $\mathcal{L}$ 하나가 아니라 그 거듭제곱들이 함께 결정하는 성질임을 다시 확인해 준다. 실제로 [§인자와 선형계, ⁋명제 19](/ko/math/scheme_theory/divisors_and_linear_systems#prop19)의 2번은 ampleness가 거듭제곱을 취하여도 변하지 않는다고 말하는데, very ampleness는 그렇지 않으므로 두 개념 사이의 간극은 정확히 이 거듭제곱만큼이다. 이제 [정리 8](#thm8)과 합치면 ampleness를 cohomology만으로 읽어낼 수 있다.

::: 정리 11 (Serre의 판정법)
Field $\mathbb{K}$ 위의 Noetherian projective scheme $X$ 위의 invertible sheaf $\mathcal{L}$에 대하여 다음 두 조건은 서로 동치이다.

1. $\mathcal{L}$은 ample이다.
2. 임의의 coherent sheaf $\mathcal{F}$에 대하여 적당한 $n_0$가 존재하여, 모든 $i>0$과 $n\geq n_0$에 대해 $H^i(X, \mathcal{F}\otimes_{\mathcal{O}_X}\mathcal{L}^{\otimes n})=0$이다.
:::
::: 증명
1번을 가정하자. [정리 10](#thm10)에 의하여 적당한 $m>0$에 대해 $\mathcal{L}^{\otimes m}$이 very ample이므로, 이것이 주는 closed immersion을 통해 [정리 8](#thm8)을 $\mathcal{L}^{\otimes m}$을 twisting sheaf로 삼아 적용할 수 있다. 유한 개의 coherent sheaf $\mathcal{F}\otimes\mathcal{L}^{\otimes q}$ ($q=0,1,\ldots, m-1$) 각각에 이를 적용하면, $p\geq p_q$인 모든 $p$에 대해

$$H^i\bigl(X, \mathcal{F}\otimes\mathcal{L}^{\otimes q}\otimes(\mathcal{L}^{\otimes m})^{\otimes p}\bigr)=0 \qquad (i>0)$$

이도록 하는 $p_q$를 얻는다. $n_0=m(\max_qp_q+1)$로 두면 $n\geq n_0$인 임의의 $n$은 $n=q+mp$ ($0\leq q<m$, $p\geq p_q$)의 꼴로 적히므로 원하는 소멸을 얻는다.

거꾸로 2번을 가정하고 coherent sheaf $\mathcal{F}$를 고정하자. Closed point $P\in X$의 ideal sheaf를 $\mathcal{I}_P$라 하고 $\mathcal{I}_P\mathcal{F}$를 $\mathcal{I}_P\otimes\mathcal{F} \rightarrow \mathcal{F}$의 image라 하면, quotient $\mathcal{F}/\mathcal{I}_P\mathcal{F}$은 $P$에 놓인 skyscraper sheaf로서 그 값이 $\mathcal{F}_P\otimes_{\mathcal{O}_{X,P}}\kappa(P)$이다. $\mathcal{L}^{\otimes n}$이 invertible이므로 이를 텐서하여도 exactness가 보존되고, 가정을 coherent sheaf $\mathcal{I}_P\mathcal{F}$에 적용하면 적당한 $n_1$이 존재하여 $n\geq n_1$마다 $H^1(X, \mathcal{I}_P\mathcal{F}\otimes\mathcal{L}^{\otimes n})=0$이다. 그럼 [명제 2](#prop2)의 long exact sequence에 의하여

$$\Gamma(X, \mathcal{F}\otimes\mathcal{L}^{\otimes n}) \longrightarrow (\mathcal{F}\otimes\mathcal{L}^{\otimes n})_P\otimes_{\mathcal{O}_{X,P}}\kappa(P) \longrightarrow 0$$

이 exact이다. Stalk $(\mathcal{F}\otimes\mathcal{L}^{\otimes n})_P$는 Noetherian local ring $\mathcal{O}_{X,P}$ 위의 finitely generated module이므로, [\[가환대수학\] §정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)의 2번에 의하여 유한 개의 global section의 germ이 이 stalk를 생성한다. 그 절단들이 정의하는 $\mathcal{O}_X^{\oplus c} \rightarrow \mathcal{F}\otimes\mathcal{L}^{\otimes n}$의 cokernel은 coherent sheaf이고 그 stalk가 $P$에서 $0$이므로, coherent sheaf의 support가 닫혀 있다는 것에서 $P$의 어떤 열린근방 위에서 $\mathcal{F}\otimes\mathcal{L}^{\otimes n}$은 globally generated이다.

이 논증은 $n\geq n_1$인 모든 $n$에서 성립하되 열린근방이 $n$에 따라 달라지므로, 이를 하나로 묶어야 한다. 위의 논증을 $\mathcal{F}=\mathcal{O}_X$에 적용하면 적당한 $m\geq1$이 존재하여 $\mathcal{L}^{\otimes m}$과 $\mathcal{L}^{\otimes(m+1)}$이 모두 $P$에서 global section들로 생성되므로, 두 열린근방의 교집합 $W$ 위에서 둘 다 globally generated이다. Globally generated인 두 module의 tensor product는 stalk의 generator들의 tensor를 보면 다시 globally generated이므로, $a,b\geq0$에 대하여 $\mathcal{L}^{\otimes(am+b(m+1))}$은 $W$ 위에서 globally generated이다. $m$과 $m+1$이 서로소이므로 $k\geq m^2$인 모든 정수 $k$가 $am+b(m+1)$의 꼴로 적히고, 곧 $W$ 위에서는 $k\geq m^2$인 모든 $k$에 대해 $\mathcal{L}^{\otimes k}$이 globally generated이다. 한편 $\mathcal{F}$ 자신에 대해 $n_2\geq n_1$을 하나 택하면 $\mathcal{F}\otimes\mathcal{L}^{\otimes n_2}$은 $P$의 어떤 열린근방 $V$ 위에서 globally generated이므로, $W\cap V$ 위에서는 $n\geq n_2+m^2$인 모든 $n$에 대해

$$\mathcal{F}\otimes\mathcal{L}^{\otimes n}\cong(\mathcal{F}\otimes\mathcal{L}^{\otimes n_2})\otimes\mathcal{L}^{\otimes(n-n_2)}$$

이 globally generated이다.

마지막으로 $X$가 $\mathbb{K}$ 위에서 finite type이므로 각 affine chart의 coordinate ring은 Jacobson ring이고 ([\[가환대수학\] §영점정리, ⁋정리 4](/ko/math/commutative_algebra/nullstellensatz#thm4)), 따라서 $X$의 공집합 아닌 닫힌집합은 언제나 $X$의 closed point를 포함한다. 곧 closed point들에서 얻은 위의 열린근방들은 $X$ 전체를 덮으며, $X$가 quasi-compact이므로 유한 개 $P_1,\ldots, P_r$의 것만으로 덮인다. 각각에 대응하는 하한들의 최댓값을 $n_0$로 두면 $n\geq n_0$마다 $\mathcal{F}\otimes\mathcal{L}^{\otimes n}$은 $X$ 전체에서 globally generated이므로 $\mathcal{L}$은 ample이다.
:::

[정리 11](#thm11)의 2번은 사영공간으로의 embedding을 전혀 언급하지 않으므로, 구체적인 절단을 다루지 않고도 line bundle의 양성을 확인할 수 있는 도구가 된다. 소멸을 요구한 것은 $i>0$ 전체이지만 증명에서 실제로 쓰인 것은 $H^1$의 소멸뿐이며, 이는 $H^1$이 절단의 확장을 막는 유일한 장애물이라는 사실의 반영이다.

## Euler characteristic과 Hilbert polynomial

[정리 7](#thm7)에 의하여 projective scheme 위의 coherent sheaf는 유한 개의 유한차원 cohomology만을 가지므로, 그 차원들의 교대합을 취할 수 있다.

::: 정의 12
Field $\mathbb{K}$ 위의 Noetherian projective scheme $X$와 그 위의 coherent sheaf $\mathcal{F}$에 대하여, $\mathcal{F}$의 *Euler characteristic<sub>오일러 지표</sub>*을 다음의 식

$$\rchi(X, \mathcal{F})=\sum_{i\geq 0}(-1)^i\dim_\mathbb{K}H^i(X, \mathcal{F})$$

으로 정의한다.
:::

[정리 7](#thm7)에 의하여 우변은 유한합이고 각 항이 유한하므로 $\rchi(X, \mathcal{F})$는 정수이며, $X$가 문맥에서 분명할 때에는 $\rchi(\mathcal{F})$로 줄여 적는다. 이는 [\[대수다양체\] §사영공간의 코호몰로지, ⁋정의 2](/ko/math/algebraic_varieties/cohomology_of_projective_spaces#def2)를 scheme 위로 옮긴 것이다. 개별 차원 $\dim_\mathbb{K}H^i(X, \mathcal{F})$는 sheaf를 조금만 움직여도 뛸 수 있지만 그 교대합은 훨씬 안정적인데, 그 근원은 다음의 가법성이다.

::: 명제 13
Field $\mathbb{K}$ 위의 Noetherian projective scheme $X$ 위의 coherent sheaf들에 대하여 다음이 성립한다.

1. Short exact sequence $0 \rightarrow \mathcal{F}' \rightarrow \mathcal{F} \rightarrow \mathcal{F}'' \rightarrow 0$에 대하여 $\rchi(\mathcal{F})=\rchi(\mathcal{F}')+\rchi(\mathcal{F}'')$이다.
2. 유한 exact sequence $0 \rightarrow \mathcal{F}_k \rightarrow \cdots \rightarrow \mathcal{F}_1 \rightarrow \mathcal{F}_0 \rightarrow 0$에 대하여 $\sum_{j=0}^k(-1)^j\rchi(\mathcal{F}_j)=0$이다.
:::
::: 증명
먼저 유한차원 벡터공간들의 exact sequence $0 \rightarrow V_0 \rightarrow V_1 \rightarrow \cdots \rightarrow V_t \rightarrow 0$을 보자. $j$번째 선형사상의 rank를 $r_j$라 하면 ($r_{-1}=r_t=0$) exactness가 $\dim V_j=r_{j-1}+r_j$를 주므로, 교대합 $\sum_j(-1)^j\dim V_j$에서 이웃한 항들이 서로 소거되어 $0$이 된다.

1번의 경우 [명제 2](#prop2)가 주는 long exact sequence

$$0 \rightarrow H^0(X, \mathcal{F}') \rightarrow H^0(X, \mathcal{F}) \rightarrow H^0(X, \mathcal{F}'') \rightarrow H^1(X, \mathcal{F}') \rightarrow \cdots$$

는 [정리 7](#thm7)에 의하여 유한차원 벡터공간들로 이루어져 있고 충분히 큰 차수에서 끊기므로 유한하다. 위의 관찰을 적용하면 세 sheaf의 cohomology 차원들의 교대합이 $0$이 되고, 부호를 정리하면 원하는 식이다.

2번의 경우 $j\geq1$에 대하여 $\mathcal{Z}_j=\ker(\mathcal{F}_j \rightarrow \mathcal{F}_{j-1})$로 두고 $\mathcal{Z}_0=\mathcal{F}_0$이라 하자. Coherent sheaf들 사이의 morphism의 kernel은 다시 coherent sheaf이므로 각각의 $\mathcal{Z}_j$은 coherent sheaf이고, exactness에 의하여 $\mathcal{Z}_k=0$이며 각각의 $j\geq1$에 대해 short exact sequence

$$0 \rightarrow \mathcal{Z}_j \rightarrow \mathcal{F}_j \rightarrow \mathcal{Z}_{j-1} \rightarrow 0$$

을 얻는다. 여기에 1번을 적용하여 얻은 $\rchi(\mathcal{F}_j)=\rchi(\mathcal{Z}_j)+\rchi(\mathcal{Z}_{j-1})$을 부호를 번갈아 더하면 중간항이 모두 소거되어 $\sum_{j=1}^k(-1)^j\rchi(\mathcal{F}_j)=-\rchi(\mathcal{Z}_0)=-\rchi(\mathcal{F}_0)$을 얻는다.
:::

특히 coherent sheaf $\mathcal{F}$가 유한 resolution $0 \rightarrow \mathcal{E}_k \rightarrow \cdots \rightarrow \mathcal{E}_0 \rightarrow \mathcal{F} \rightarrow 0$을 가지면 [명제 13](#prop13)의 2번에서 $\rchi(\mathcal{F})=\sum_{j=0}^k(-1)^j\rchi(\mathcal{E}_j)$을 얻는다. 이것이 Euler characteristic을 실제로 계산하는 표준적인 경로이며, 그 출발점은 사영공간 위의 line bundle이다.

::: 따름정리 14
Field $\mathbb{K}$ 위의 사영공간 $\mathbb{P}^n_\mathbb{K}$와 임의의 정수 $d$에 대하여

$$\rchi(\mathbb{P}^n_\mathbb{K}, \mathcal{O}(d))=\binom{n+d}{n}$$

이 성립한다. 여기에서 $\binom{n+d}{n}$은 다항식 $t(t-1)\cdots(t-n+1)/n!$의 $t=n+d$에서의 값으로 읽는다.
:::
::: 증명
[정리 6](#thm6)에서 $A=\mathbb{K}$로 두면 세 경우로 나뉜다. $d\geq0$이면 $H^0$만 남고 그 차원은 $n+1$개의 변수의 degree $d$ monomial의 개수 $\binom{n+d}{n}$이다. $-n\leq d\leq-1$이면 모든 cohomology가 소멸하며, 이 범위에서 $t=n+d$는 $0$과 $n-1$ 사이의 정수이므로 곱 $t(t-1)\cdots(t-n+1)$의 인수 가운데 하나가 $0$이 되어 $\binom{n+d}{n}=0$이다. $d\leq -n-1$이면 $H^n$만 남고 그 차원은 모든 지수가 음인 $d$차 monomial의 개수 $\binom{-d-1}{n}$이므로

$$\rchi(\mathbb{P}^n_\mathbb{K}, \mathcal{O}(d))=(-1)^n\binom{-d-1}{n}=\binom{n+d}{n}$$

이다. 마지막 등식은 $t=n+d$에 대해 $t(t-1)\cdots(t-n+1)=(-1)^n(n-t-1)(n-t-2)\cdots(-t)$인 것에서 얻어진다.
:::

이 값은 $d$에 대한 degree $n$의 다항식이며, [\[대수다양체\] §사영공간의 코호몰로지, ⁋따름정리 3](/ko/math/algebraic_varieties/cohomology_of_projective_spaces#cor3)의 variety 판본과 일치한다. 곧 $\mathcal{O}(d)$를 twist해 나갈 때 cohomology의 교대합은 개별 cohomology가 겪는 세 국면과 무관하게 하나의 다항식을 따라간다. 이것이 일반적인 coherent sheaf에서도 성립한다는 것이 다음 정리이며, 이를 진술하기 위해 coherent sheaf $\mathcal{F}$의 *support*를 $\operatorname{Supp}\mathcal{F}=\{x\in X\mid \mathcal{F}_x\neq0\}$으로 정의한다. Affine chart 위에서 이는 대응하는 module의 annihilator ideal의 zero set이므로 닫힌집합이다.

::: 정리 15 (Hilbert)
Field $\mathbb{K}$ 위의 사영공간 $\mathbb{P}^n_\mathbb{K}$의 closed subscheme $X$와 그 위의 coherent sheaf $\mathcal{F}$에 대하여, 유일한 numerical polynomial $P_\mathcal{F}$가 존재하여 ([\[가환대수학\] §힐베르트-사무엘 함수, ⁋정의 1](/ko/math/commutative_algebra/hilbert-samuel_function#def1)) 모든 정수 $d$에 대해

$$\rchi(\mathcal{F}(d))=P_\mathcal{F}(d)$$

이 성립한다. 뿐만 아니라 $\mathcal{F}\neq0$이면 $P_\mathcal{F}$의 degree는 $\dim\operatorname{Supp}\mathcal{F}$와 같고, 충분히 큰 $d$에 대해서는 $P_\mathcal{F}(d)=\dim_\mathbb{K}\Gamma(X, \mathcal{F}(d))$이다.
:::
::: 증명
마지막 주장은 [정리 8](#thm8)에서 곧바로 얻어진다. 충분히 큰 $d$에서 $H^i(X, \mathcal{F}(d))=0$ ($i>0$)이므로 교대합에 $H^0$만 남기 때문이다. 유일성은 서로 다른 두 다항식이 무한히 많은 정수에서 일치할 수 없다는 것에서 따라온다.

먼저 $X=\mathbb{P}^n_\mathbb{K}$인 경우로 환원한다. [정리 7](#thm7) 직전에 관찰한 대로 closed immersion $\iota:X\hookrightarrow\mathbb{P}^n_\mathbb{K}$에 대하여 $H^i(X, \mathcal{F}(d))\cong H^i(\mathbb{P}^n, (\iota_\ast\mathcal{F})(d))$이고 $\operatorname{Supp}\iota_\ast\mathcal{F}=\iota(\operatorname{Supp}\mathcal{F})$이므로, $\mathcal{F}$를 $\iota_\ast\mathcal{F}$로 바꾸어도 무방하다.

다음으로 $\mathbb{K}$가 무한체라 가정하여도 됨을 본다. 무한체로의 확대 $\mathbb{L}\supseteq\mathbb{K}$를 잡고 $\mathbb{P}^n_\mathbb{L} \rightarrow \mathbb{P}^n_\mathbb{K}$를 따라 $\mathcal{F}$를 끌어올리자. Standard affine cover에 대한 Čech complex는 계수를 확대한 $\check C^\bullet(\mathcal{U}, \mathcal{F})\otimes_\mathbb{K}\mathbb{L}$이고 $-\otimes_\mathbb{K}\mathbb{L}$은 exact이므로, [따름정리 4](#cor4)에 의하여 $\dim_\mathbb{L}H^i(\mathbb{P}^n_\mathbb{L}, \mathcal{F}_\mathbb{L}(d))=\dim_\mathbb{K}H^i(\mathbb{P}^n_\mathbb{K}, \mathcal{F}(d))$이다. 또 finite type scheme의 차원은 계수를 확대하여도 변하지 않으므로 support의 차원도 보존된다. 이는 affine chart $\Spec A$ 위에서 다음의 순서로 확인한다. $A$의 minimal prime들을 $\mathfrak{p}_1,\ldots, \mathfrak{p}_s$라 하면 $A \rightarrow \prod_kA/\mathfrak{p}_k$의 kernel은 nilradical이고 그 image는 $\prod_kA/\mathfrak{p}_k$ 안에서 integral인데, nilpotent는 spectrum을 바꾸지 않고 integral extension은 차원을 보존하므로 ([§차원, ⁋명제 5](/ko/math/scheme_theory/dimension#prop5)) $\dim A=\max_k\dim A/\mathfrak{p}_k$이다. $\mathbb{L}$이 $\mathbb{K}$ 위에서 flat이므로 이 ring homomorphism은 base change 후에도 nilpotent kernel과 integral image를 유지하여, 같은 등식이 $A\otimes_\mathbb{K}\mathbb{L}$에 대해서도 성립한다. 한편 각각의 $A/\mathfrak{p}_k$는 finitely generated $\mathbb{K}$-대수인 integral domain이므로 확대 이전에 [§차원, ⁋정리 9](/ko/math/scheme_theory/dimension#thm9)를 적용하여 injective한 finite ring homomorphism $\mathbb{K}[x_1,\ldots, x_{n_k}]\hookrightarrow A/\mathfrak{p}_k$를 얻을 수 있고, 이를 $\mathbb{L}$로 base change한 $\mathbb{L}[x_1,\ldots, x_{n_k}]\hookrightarrow(A/\mathfrak{p}_k)\otimes_\mathbb{K}\mathbb{L}$ 또한 injective이고 finite이므로 다시 [§차원, ⁋명제 5](/ko/math/scheme_theory/dimension#prop5)에 의하여 양변의 차원이 $n_k=\dim A/\mathfrak{p}_k$로 같다. 확대 후의 $A\otimes_\mathbb{K}\mathbb{L}$은 domain이 아닐 수 있어 Noether normalization을 확대된 계수 위에서 새로 적용할 수는 없으므로, 이처럼 확대 이전에 잡은 ring homomorphism을 base change하는 순서를 따라야 한다. 따라서 처음부터 $\mathbb{K}$가 무한체라 두어도 된다.

이제 $r=\dim\operatorname{Supp}\mathcal{F}$에 대한 귀납법을 쓴다. $\mathcal{F}=0$이면 모든 cohomology가 소멸하므로 $P_\mathcal{F}=0$이다. $\mathcal{F}\neq0$이라 하고 $S=\mathbb{K}[\x_0,\ldots, \x_n]$이라 하자. 각각의 chart $D_+(\x_j)=\Spec S_{(\x_j)}$ 위에서 $\mathcal{F}$는 finitely generated module $M_j$에 대응하며 ([§준연접층, ⁋정리 10](/ko/math/scheme_theory/quasicoherent_sheaves#thm10), [§준연접층, ⁋정의 11](/ko/math/scheme_theory/quasicoherent_sheaves#def11)), 각각의 $\Ass M_j$는 유한집합이다. ([\[가환대수학\] §동반소아이디얼, ⁋정리 7](/ko/math/commutative_algebra/associated_primes#thm7)의 1번) 이들에 대응하는 $\mathbb{P}^n$의 점을 모두 모으면 유한 개이고, 각각은 irrelevant ideal을 포함하지 않는 homogeneous prime ideal $\mathfrak{p}_1,\ldots, \mathfrak{p}_t\subseteq S$를 준다. $\mathfrak{p}_k$가 homogeneous이므로 $S_1\subseteq\mathfrak{p}_k$이면 $\mathfrak{p}_k$가 irrelevant ideal을 포함하게 되고, 따라서 각각의 $\mathfrak{p}_k\cap S_1$은 $S_1$의 진부분공간이다. 한편 $\mathbb{K}$가 무한체이므로 벡터공간 $S_1$은 유한 개의 진부분공간의 합집합이 될 수 없다. 실제로 그러한 덮개가 존재한다면 덮개가 최소인 것을 택하고 첫 번째 부분공간에만 속하는 $u$와 그 부분공간에 속하지 않는 $v$를 잡으면, 무한히 많은 $v+\lambda u$ 가운데 어느 것도 첫 번째 부분공간에 속하지 않으므로 그 중 둘이 같은 다른 부분공간에 들어가고, 그 차가 $u$의 배수이므로 $u$가 그 부분공간에 속하게 되어 모순이다. 따라서 어떠한 $\mathfrak{p}_k$에도 속하지 않는 $\ell\in S_1$이 존재한다.

곱하기 $\ell$은 morphism $\mathcal{F}(-1) \rightarrow \mathcal{F}$을 주며, chart $D_+(\x_j)$ 위에서 이는 $M_j$ 위의 $\ell/\x_j$ 배이다. $\ell/\x_j$는 $M_j$의 어떠한 associated prime에도 속하지 않으므로 $M_j$의 zerodivisor가 아니고 ([\[가환대수학\] §동반소아이디얼, ⁋정리 7](/ko/math/commutative_algebra/associated_primes#thm7)의 2번), 따라서 이 morphism은 injective이다. 그 cokernel을 $\mathcal{F}''$이라 하면 각각의 $d$에 대해 short exact sequence

$$0 \rightarrow \mathcal{F}(d-1) \rightarrow \mathcal{F}(d) \rightarrow \mathcal{F}''(d) \rightarrow 0$$

을 얻고, $\operatorname{Supp}\mathcal{F}''=\operatorname{Supp}\mathcal{F}\cap V_+(\ell)$이다. ([§사영공간의 닫힌 부분스킴, ⁋명제 1](/ko/math/scheme_theory/closed_subschemes_of_projective_spaces#prop1))

Minimal prime은 언제나 associated prime이므로 $\ell$은 $\operatorname{Supp}\mathcal{F}$의 어떠한 irreducible component 위에서도 항등적으로 소멸하지 않는다. 각각의 component $Z$에 reduced 구조를 주고 그 교집합의 차원을 재어 보자. $Z$가 irreducible이고 $\mathbb{K}$ 위에서 finite type이므로 $Z$와 만나는 각각의 chart에 대하여 $Z\cap D_+(\x_j)=\Spec A_j$의 $A_j$는 finitely generated $\mathbb{K}$-대수인 integral domain이고 그 fraction field는 chart와 무관하게 $Z$의 function field이다. 따라서 [§차원, ⁋명제 10](/ko/math/scheme_theory/dimension#prop10)에 의하여 $\dim A_j$는 모든 chart에서 같으며, [§차원, ⁋명제 2](/ko/math/scheme_theory/dimension#prop2)에 의하여 이 공통값이 $\dim Z$이다.

$\dim Z=0$인 경우 $Z$는 한 점이고 그 위에서 $\ell$이 소멸하지 않으므로 $Z\cap V_+(\ell)=\emptyset$이다. $\dim Z\geq1$인 경우에는 거꾸로 $Z\cap V_+(\ell)\neq\emptyset$인데, 만일 만나지 않는다면 $Z$는 affine scheme $D_+(\ell)$의 closed subscheme이 되어 affine이고, 그럼 $A=\Gamma(Z, \mathcal{O}_Z)$는 [정리 7](#thm7)에 의하여 유한차원 $\mathbb{K}$-벡터공간이면서 $Z$가 integral이므로 integral domain인데, $0\neq a\in A$마다 곱하기 $a$가 단사인 $\mathbb{K}$-선형사상이라 유한차원성에 의하여 전사이므로 $A$가 field가 되어 $\dim Z=0$이기 때문이다. 그럼 $Z\cap V_+(\ell)$의 한 점을 포함하는 chart $D_+(\x_j)$를 택하면 $\ell/\x_j\in A_j$는 위에서 본 대로 $0$이 아니고 그 점에서 소멸하므로 unit도 아니어서, [§차원, ⁋명제 11](/ko/math/scheme_theory/dimension#prop11)에 의하여 $\dim\bigl(Z\cap V_+(\ell)\cap D_+(\x_j)\bigr)=\dim A_j-1=\dim Z-1$이다. $Z\cap V_+(\ell)$과 만나는 모든 chart에서 같은 값이 얻어지므로 [§차원, ⁋명제 2](/ko/math/scheme_theory/dimension#prop2)에 의하여 $\dim(Z\cap V_+(\ell))=\dim Z-1$이다.

따라서 $r=0$이면 모든 component가 $V_+(\ell)$과 만나지 않아 $\mathcal{F}''=0$이고, $r\geq1$이면 차원이 $r$인 component에서 $r-1$이 얻어져 $\dim\operatorname{Supp}\mathcal{F}''=r-1$이다.

귀납적 가정에 의하여 $\rchi(\mathcal{F}''(d))$는 모든 $d$에서 어떤 numerical polynomial $Q$와 일치하며, $r=0$이면 $Q=0$이고 $r\geq1$이면 $\deg Q=r-1$이다. [명제 13](#prop13)의 1번에 의하여 모든 정수 $d$에 대해 $\rchi(\mathcal{F}(d))-\rchi(\mathcal{F}(d-1))=Q(d)$이므로, $g(d)=\rchi(\mathcal{F}(d))$로 두면 $g(d+1)-g(d)=Q(d+1)$은 numerical polynomial이다. 그럼 [\[가환대수학\] §힐베르트-사무엘 함수, ⁋보조정리 2](/ko/math/commutative_algebra/hilbert-samuel_function#lem2)의 둘째 결과에 의하여 충분히 큰 $d$에서 $g$와 일치하는 numerical polynomial $P$가 존재하고, 그 구성에 의하여 $P(d+1)-P(d)=Q(d+1)$이 다항식으로서 성립하며, $Q\neq0$이면 $\deg P=\deg Q+1$이다. 다항식 등식이 성립하므로 $d$를 하나씩 내리며

$$g(d)=g(d+1)-Q(d+1)=P(d+1)-Q(d+1)=P(d)$$

를 얻어, $g$와 $P$는 모든 정수에서 일치한다.

남은 것은 degree이다. $r\geq1$이면 $\deg P=\deg Q+1=r$이다. $r=0$이면 $Q=0$이므로 $P$는 상수이고, [정리 8](#thm8)에 의하여 충분히 큰 $d$에서 $\mathcal{F}(d)$이 globally generated이며 $\mathcal{F}\neq0$이므로 $\Gamma(X, \mathcal{F}(d))\neq0$이다. 곧 마지막 주장에 의하여 $P>0$이고 $\deg P=0=r$이다.
:::

이 다항식 $P_\mathcal{F}$를 $\mathcal{F}$의 *Hilbert polynomial<sub>힐베르트 다항식</sub>*이라 부른다. [따름정리 14](#cor14)는 $\mathcal{F}=\mathcal{O}_{\mathbb{P}^n}$인 경우로서 $P_{\mathcal{O}_{\mathbb{P}^n}}(t)=\binom{n+t}{n}$이고 그 degree는 $\dim\mathbb{P}^n=n$이다. [정리 15](#thm15)의 마지막 주장은 이 다항식이 충분히 큰 degree에서는 $\mathcal{F}(d)$의 global section이 이루는 공간의 차원을 재고 있음을 말해주며, 이것이 고전적으로 homogeneous coordinate ring의 Hilbert function을 통해 Hilbert polynomial을 도입하던 관점과 이어지는 지점이다. ([\[가환대수학\] §힐베르트-사무엘 함수, ⁋정의 4](/ko/math/commutative_algebra/hilbert-samuel_function#def4)) 특히 $\mathcal{F}=\mathcal{O}_X$인 경우 이 다항식은 $X$ 자신의 불변량이 된다.

::: 정의 16
Field $\mathbb{K}$ 위의 사영공간 $\mathbb{P}^n_\mathbb{K}$의 공집합이 아닌 $r$차원 closed subscheme $X$에 대하여, Hilbert polynomial $P_{\mathcal{O}_X}$의 최고차항 계수를 $a_r$이라 하자. 그럼 $X$의 *degree<sub>차수</sub>*를

$$\deg X=r!\cdot a_r$$

로 정의하고, $X$의 *arithmetic genus<sub>산술종수</sub>*를 $p_a(X)=(-1)^r\bigl(P_{\mathcal{O}_X}(0)-1\bigr)$로 정의한다.
:::

$\operatorname{Supp}\mathcal{O}_X=X$이므로 [정리 15](#thm15)에 의하여 $P_{\mathcal{O}_X}$의 degree는 정확히 $r$이고, 충분히 큰 $d$에서 $P_{\mathcal{O}_X}(d)=\dim_\mathbb{K}\Gamma(X, \mathcal{O}_X(d))>0$이므로 $a_r$은 양수이다. 또 numerical polynomial을 이항계수들의 정수계수 결합으로 적으면 ([\[가환대수학\] §힐베르트-사무엘 함수, ⁋보조정리 2](/ko/math/commutative_algebra/hilbert-samuel_function#lem2)의 첫째 결과) 최고차항 계수에 $r!$을 곱한 값이 정수임을 알 수 있다. 곧 $\deg X$는 양의 정수이다. 한편 $P_{\mathcal{O}_X}(0)=\rchi(\mathcal{O}_X)$이므로 arithmetic genus는 structure sheaf의 Euler characteristic을 다시 적은 것이며, 부호 $(-1)^r$은 곡선의 경우 $p_a=1-\rchi(\mathcal{O}_X)$가 되도록 맞춘 것이다.

가장 단순한 예시는 사영공간 자신이다. [따름정리 14](#cor14)에서 $P_{\mathcal{O}_{\mathbb{P}^n}}(t)=\binom{n+t}{n}$이므로 최고차항 계수는 $1/n!$이고 따라서 $\deg\mathbb{P}^n_\mathbb{K}=1$이며, $P_{\mathcal{O}_{\mathbb{P}^n}}(0)=1$에서 $p_a(\mathbb{P}^n_\mathbb{K})=0$이다. 다음으로 degree $e$의 homogeneous polynomial $f$가 정의하는 hypersurface $X=V_+(f)\subseteq\mathbb{P}^n_\mathbb{K}$를 보자. ([§사영공간의 닫힌 부분스킴, ⁋예시 2](/ko/math/scheme_theory/closed_subschemes_of_projective_spaces#ex2)) $S$가 integral domain이므로 곱하기 $f$는 각 chart 위에서 injective이고, 따라서 short exact sequence

$$0 \rightarrow \mathcal{O}_{\mathbb{P}^n}(-e)\overset{\times f}{\longrightarrow}\mathcal{O}_{\mathbb{P}^n} \rightarrow \mathcal{O}_X \rightarrow 0$$

을 얻는다. 이를 $\mathcal{O}(d)$로 twist한 뒤 [명제 13](#prop13)의 1번과 [따름정리 14](#cor14)를 적용하면

$$P_{\mathcal{O}_X}(t)=\binom{n+t}{n}-\binom{n+t-e}{n}$$

이다. 우변에서 $t^n$의 항은 소거되고 $t^{n-1}$의 계수는 $e/(n-1)!$이 남으므로, $\dim X=n-1$과 함께 $\deg X=e$를 얻는다. 곧 hypersurface의 degree가 정의 다항식의 degree라는 고전적인 사실이 Hilbert polynomial의 언어로 다시 얻어진다.

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic geometry*, Graduate Texts in Mathematics, Springer, 1977. (Chapter III.1–5)  
**[Vak]** R. Vakil, *The rising sea: Foundations of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/). (Chapter 18)  
**[EGA]** A. Grothendieck and J. Dieudonné, *Éléments de géométrie algébrique III*, Publ. Math. IHÉS, 1961.  
**[Stacks]** The Stacks Project Authors, *The Stacks Project*. Available [online](https://stacks.math.columbia.edu/).
