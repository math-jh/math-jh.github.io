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


---

우리는 [\[대수다양체\] §층 코호몰로지](/ko/math/algebraic_varieties/sheaf_cohomology)에서 (quasi-projective) variety 위의 sheaf cohomology를 derived functor로 정의하고, Čech cohomology와의 비교 및 Leray 정리를 통해 quasi-coherent sheaf의 cohomology를 계산하는 방법을 살펴보았다. 이제 우리는 quasi-coherent sheaf를 scheme의 언어로 정리하였으므로, 같은 일을 scheme에서도 할 수 있다. 핵심적인 것은 위 글에서의 quasi-projective 가정은 과도한 것이라는 것으로, separatedness와 affine scheme 위 quasi-coherent sheaf의 vanishing theorem을 보이고 나면 해당 글과 마찬가지의 결과들을 증명할 수 있다. 

이전 몇 개의 글과 마찬가지로, 이번 글의 목표는 이미 [\[대수다양체\] §층 코호몰로지](/ko/math/algebraic_varieties/sheaf_cohomology)에서 다룬 내용을 scheme으로 올리는 것이며, 몇몇 계산은 직접 수행하기도 하지만, 대부분의 계산은 해당 글들에 맡겨두고 이 언어로 번역하는 작업이 주가 될 것이다. 

## 유도함자로서의 코호몰로지

Scheme $X$ 위에서도 abelian group들의 sheaf들의 category $\Sh(X)$는 abelian category이며 enough injective를 가진다. 따라서 [\[대수다양체\] §층 코호몰로지](/ko/math/algebraic_varieties/sheaf_cohomology)에서와 동일한 방식으로 global section functor의 derived functor를 정의할 수 있다. 그곳에서와 마찬가지로 우리의 주된 관심은 항상 quasi-coherent sheaf이지만, 정의도 resolution도 $\Sh(X)$ 안에서 이루어진다. 

::: 정의 1
Scheme $X$ 위의 sheaf $\mathcal{F}$에 대하여, global section functor $\Gamma(X, -):\Sh(X) \rightarrow \Ab$의 right derived functor를 ([\[호몰로지 대수학\] §유도함자, ⁋정의 9](/ko/math/homological_algebra/derived_functors#def9)) 취하여 $i$번째 *sheaf cohomology<sub>층 코호몰로지</sub>*를

$$H^i(X, \mathcal{F})=R^i\Gamma(X, -)(\mathcal{F})=\frac{\ker\bigl(\Gamma(X, \mathcal{I}^i) \rightarrow \Gamma(X, \mathcal{I}^{i+1})\bigr)}{\im\bigl(\Gamma(X, \mathcal{I}^{i-1}) \rightarrow \Gamma(X, \mathcal{I}^i)\bigr)}$$

으로 정의한다. 여기에서 $0 \rightarrow \mathcal{F} \rightarrow \mathcal{I}^\bullet$은 $\Sh(X)$에서의 injective resolution이다.
:::

이 정의는 [\[대수다양체\] §층 코호몰로지, ⁋정의 1](/ko/math/algebraic_varieties/sheaf_cohomology#def1)을 임의의 scheme 위로 옮긴 것에 불과하며, 이 정의가 $\mathcal{I}^\bullet$의 선택에 무관하다는 사실을 비롯한 형식적 성질은 모두 homological algebra의 표준적인 논증으로부터 따라온다. 특히 $H^0(X, \mathcal{F})=\Gamma(X, \mathcal{F})$이고, sheaf의 short exact sequence는 long exact sequence를 유도한다.

한편 $\Gamma(X, -)$가 $\Sh(X)$ 위의 functor이므로 $H^i(X, \mathcal{F})$는 일단 abelian group으로만 얻어지지만, $\mathcal{F}$가 $\mathcal{O}_X$-module인 경우에는 여기에 $\Gamma(X, \mathcal{O}_X)$-module 구조가 얹힌다. 각각의 $a\in\Gamma(X, \mathcal{O}_X)$에 대하여, $a$를 곱하는 것이 $\mathcal{F}$의 $\Sh(X)$에서의 endomorphism이므로 cohomology의 functoriality가 $H^i(X, \mathcal{F})$ 위의 endomorphism을 주고, 이 대응이 곱셈을 보존한다. 여기에 $R^i\Gamma(X, -)$가 additive functor라는 것을 더하면 $a\mapsto H^i(m_a)$가 덧셈까지 보존하므로 ring homomorphism $\Gamma(X, \mathcal{O}_X) \rightarrow \End_\mathbb{Z}\bigl(H^i(X, \mathcal{F})\bigr)$이 되어, 원하는 module 구조를 얻는다.

::: 명제 2
Sheaf의 short exact sequence

$$0 \rightarrow \mathcal{F}' \rightarrow \mathcal{F} \rightarrow \mathcal{F}'' \rightarrow 0$$

에 대하여, long exact sequence

$$0 \rightarrow H^0(X, \mathcal{F}') \rightarrow H^0(X, \mathcal{F}) \rightarrow H^0(X, \mathcal{F}'') \xrightarrow{\delta} H^1(X, \mathcal{F}') \rightarrow H^1(X, \mathcal{F}) \rightarrow \cdots$$

이 존재한다.
:::
::: 증명
$\Gamma(X, -)$는 left exact functor이고 $\Sh(X)$는 enough injective를 가지므로, right derived functor가 정의하는 $\delta$-functor의 long exact sequence가 그대로 성립한다.
:::

## 아핀스킴의 코호몰로지

한편 우리는 [\[대수다양체\] §층 코호몰로지](/ko/math/algebraic_varieties/sheaf_cohomology)에서 Čech cohomology 또한 도입하였는데, 이는 사실 위상공간 수준의 정의이므로 scheme 위에서도 아무것도 바꿀 필요 없이 그대로 작동한다. 해당 글에서와 마찬가지로, sheaf cohomology의 정의는 [정의 1](#def1)이 그 본질을 정확히 담고 있지만, 이를 실제로 사용하기 위해서는 Čech cohomology로 옮겨오는 것이 보통이다. 이를 가능하게 했던 결과는 [\[대수다양체\] §층 코호몰로지, ⁋명제 12](/ko/math/algebraic_varieties/sheaf_cohomology#prop12)로, affine variety 위에서 quasi-coherent sheaf의 higher cohomology가 소멸한다는 결과였다. 이 명제의 scheme 버전은 다음과 같다. 

::: 정리 3 (Serre)
Noetherian ring $A$가 정의하는 affine scheme $X=\Spec A$와 그 위의 quasi-coherent sheaf $\mathcal{F}=\widetilde M$에 대하여,

$$H^i(X, \mathcal{F})=0 \qquad (i>0)$$

이 성립한다.
:::
::: 증명
[§준연접층, ⁋정리 9](/ko/math/scheme_theory/quasicoherent_sheaves#thm9)에 의하여 $\QCoh(\Spec A)$는 $\rMod{A}$와 동치이므로, $\mathcal{F}=\widetilde M$인 $A$-module $M$이 존재한다. $\rMod{A}$는 enough injective를 가지므로 $M$의 injective resolution

$$0 \rightarrow M \rightarrow I^0 \rightarrow I^1 \rightarrow \cdots$$

을 잡자. associated sheaf functor $\widetilde{(-)}$는 exact이므로 ([§준연접층, ⁋명제 6](/ko/math/scheme_theory/quasicoherent_sheaves#prop6)),

$$0 \rightarrow \widetilde M \rightarrow \widetilde{I^0} \rightarrow \widetilde{I^1} \rightarrow \cdots$$

은 $\Spec A$ 위의 sheaf의 resolution이다. 우리의 주장은 각각의 $\widetilde{I^k}$이 $\Gamma(\Spec A, -)$-acyclic이라는 것이며, 이것이 성립하면 [\[대수다양체\] §층 코호몰로지, ⁋명제 17](/ko/math/algebraic_varieties/sheaf_cohomology#prop17)에 의하여

$$H^i(\Spec A, \widetilde M)\cong H^i\bigl(\Gamma(\Spec A, \widetilde{I^\bullet})\bigr)=H^i(I^\bullet)$$

을 얻는다. 여기에서 두 번째 등식은 associated sheaf의 global section이 원래의 module이라는 것에서 따라오며 ([§준연접층, ⁋정의 4](/ko/math/scheme_theory/quasicoherent_sheaves#def4)), $M \rightarrow I^\bullet$이 quasi-isomorphism이므로 우변의 cohomology는 $i>0$에서 모두 소멸한다. 따라서 $H^i(\Spec A, \widetilde M)=0$ ($i>0$)이다.

남은 것은 injective $A$-module $I$의 associated sheaf $\widetilde I$이 acyclic이라는 것이다. 이를 위해 우리는 $\widetilde I$이 flasque임을 보인다. ([\[대수다양체\] §층 코호몰로지, ⁋명제 16](/ko/math/algebraic_varieties/sheaf_cohomology#prop16)) $\Spec A$의 열린집합은 모두 $U=\Spec A\setminus Z(\mathfrak{a})$의 꼴이므로, 각각에 대하여 restriction $\widetilde I(\Spec A)=I\rightarrow\widetilde I(U)$이 surjective임을 보이면 된다. Quasi-coherent sheaf의 section을 local cohomology와 잇는 exact sequence

$$I\longrightarrow\widetilde I(U)\longrightarrow H^1_{\mathfrak{a}}(I)\longrightarrow 0$$

이 성립하는데, 여기서 $H^i_{\mathfrak{a}}(M)=\varinjlim_n\Ext^i_A(A/\mathfrak{a}^n,M)$이다. $I$가 injective이므로 모든 $n$에서 $\Ext^1_A(A/\mathfrak{a}^n,I)=0$이어서 $H^1_{\mathfrak{a}}(I)=0$이고, 따라서 위 restriction이 surjective이다. 그럼 임의의 두 열린집합 $V\subseteq U$에 대하여 $I \rightarrow \widetilde I(V)$이 $\widetilde I(U)$를 지나 인수분해되므로 $\widetilde I(U) \rightarrow \widetilde I(V)$ 또한 surjective이고, 곧 $\widetilde I$은 flasque이다.
:::

[정리 3](#thm3)에서 Noetherian 가정은 증명의 편의를 위한 것으로, 실은 그 결과는 임의의 ring $A$에 대하여 성립한다. 다만 이는 이 글의 범위를 벗어나므로 증명은 싣지 않고, Noetherian 가정 없이 진술되는 아래의 [따름정리 4](#cor4)와 임의의 ring 위의 projective space를 다루는 [정리 6](#thm6)에서만 이 일반적인 형태를 사용한다.

어쨌든 이 정리의 핵심은 affine scheme이 cohomology의 관점에서 <em-ko>단순한</em-ko> 공간이라는 것이다. 즉 affine 위에서는 quasi-coherent sheaf의 정보가 모두 $H^0$, 곧 그 global section module에 담겨 있으며, higher cohomology는 어떠한 새로운 정보도 주지 않는다. 이는 위상공간이 Čech cohomology의 관점에서 contractible한 것에 대응하는 대수기하학적 현상이다.

이로부터 곧바로 affine covering에 대한 Leray theorem을 scheme 수준에서 얻는다. [\[대수다양체\] §층 코호몰로지, ⁋정리 11](/ko/math/algebraic_varieties/sheaf_cohomology#thm11)은 cover $\mathcal{U}$의 모든 유한 교집합 위에서 $\mathcal{F}$가 acyclic이면 $\check H^p(\mathcal{U}, \mathcal{F})\cong H^p(X, \mathcal{F})$임을 주는데, 이는 위상공간 수준의 정리이므로 scheme 위에서도 그대로 적용된다. 여기서 더할 가정은 affine들의 교집합이 다시 affine이 되도록 하는 조건인 separatedness 뿐이다. ([§값매김환, ⁋정의 3](/ko/math/scheme_theory/valuative_criteria#def3))

::: 따름정리 4
Separated scheme $X$와 그 위의 quasi-coherent sheaf $\mathcal{F}$, 그리고 affine open cover $\mathcal{U}=\{U_i\}$에 대하여, 모든 $p$에 대해

$$\check H^p(\mathcal{U}, \mathcal{F})\cong H^p(X, \mathcal{F})$$

이 성립한다.
:::
::: 증명
[\[대수다양체\] §층 코호몰로지, ⁋정리 11](/ko/math/algebraic_varieties/sheaf_cohomology#thm11)에 의하여, $\mathcal{U}$의 임의의 유한 교집합 $U_{i_0}\cap\cdots\cap U_{i_p}$ 위에서 $\mathcal{F}$가 acyclic임을 보이면 충분하다. $X$가 separated이므로 diagonal morphism $\Delta:X \rightarrow X\times_{\Spec \mathbb{Z}}X$이 closed embedding이고, 따라서 임의의 두 affine open subset $U_i, U_j$의 교집합 $U_i\cap U_j$는 다시 affine이다. 실제로 $U_i\cap U_j$는 fiber product $U_i\times_X U_j$이며, 이는 affine scheme $U_i\times_{\Spec \mathbb{Z}}U_j$의 closed subscheme $\Delta^{-1}(U_i\times U_j)$와 isomorphic하므로 affine이다. 같은 논증을 반복하면 유한 교집합 $U_{i_0}\cap\cdots\cap U_{i_p}$ 또한 affine scheme이다. 그럼 $\mathcal{F}$의 이 위로의 restriction은 affine scheme 위의 quasi-coherent sheaf이므로 [정리 3](#thm3)에 의하여 acyclic이고, 따라서 [\[대수다양체\] §층 코호몰로지, ⁋정리 11](/ko/math/algebraic_varieties/sheaf_cohomology#thm11)의 전제가 충족된다.
:::

따라서 separated scheme 위에서는 affine covering 하나를 잡아 Čech complex만 계산하면 derived functor cohomology가 그대로 얻어진다. Affine scheme 사이의 morphism은 항상 separated이고 ([§값매김환, ⁋보조정리 5](/ko/math/scheme_theory/valuative_criteria#lem5)), $\mathbb{P}^n$을 비롯한 projective scheme 또한 separated이므로, 우리가 실제로 다루는 대부분의 scheme에서 이 따름정리가 작동한다.

## 사영공간 위의 선다발

이제 affine covering에 대한 Čech 계산을 사용하여 projective space 위의 line bundle $\mathcal{O}(d)$의 cohomology를 scheme 수준에서 다룬다. Ring $A$ 위의 projective space를 *graded* ring $A[\x_0,\ldots, \x_n]$을 사용하여 $\mathbb{P}^n_A=\Proj A[\x_0,\ldots, \x_n]$로 정의했듯, ([§사영공간과 Proj 구성, ⁋정의 1](/ko/math/scheme_theory/projective_schemes#def1)), 우선 $\mathcal{O}(d)$를 graded module의 언어로 정의해야 한다. 

::: 정의 5
Standard grading이 주어진 $S_\bullet=A[\x_0,\ldots, \x_n]$가 주어졌다 하고, $S(d)$를 $S_\bullet$의 degree $d$-shift, 즉

$$S(d)_m=S_{d+m}$$

으로 degree가 주어진 graded $S_\bullet$-module이라 하자. 그럼 $\mathbb{P}_A^n=\Proj S_\bullet$의 standard affine cover 

$$\mathcal{U}=\{D_+(\x_i)=\Spec S_{(\x_i)}\}$$

의 각각의 chart 위에서, localization $S(d)_{\x_i}$의 degree $0$ 부분

$$M_i=\bigl(S(d)_{\x_i}\bigr)_0=\x_i^d\cdot S_{(\x_i)}$$

을 $S_{(\x_i)}$-module로 보아 정의한 associated sheaf $\widetilde{M_i}$를 정의하고, 이들이 겹치는 부분 위에서 자연스러운 identification을 통해 붙여 얻는 $\mathbb{P}^n_A$ 위의 quasi-coherent sheaf를 *twisting sheaf<sub>꼬임층</sub>* $\mathcal{O}(d)$라 부른다.
:::

[\[대수다양체\] §선다발과 벡터다발, ⁋예시 12](/ko/math/algebraic_varieties/line_bundles#ex12)에서 우리는 $\x_i\neq 0$인 standard open set $D_+(\x_i)$마다 trivialization $\phi_i(s)=s\cdot\x_i^{-d}$을 지정하고, 겹치는 부분에서 두 trivialization을 비교해 얻는 transition function $(\x_i/\x_j)^d$들을 데이터로 삼아 $\mathcal{O}(d)$를 기술하였다. 이 기술에서 $D_+(\x_i)$ 위의 section들이 이루는 공간은 $\x_i^d\cdot\mathcal{O}(D_+(\x_i))$였다. 위의 [정의 5](#def5)는 이 마지막 공간 자체를 사용해 이를 다시 정의한 것으로, $D_+(\x_i)$의 coordinate ring $S_{(\x_i)}$ 위의 module $M_i=\x_i^d\cdot S_{(\x_i)}$를 직접 사용한 것이다. 이 두 데이터가 동일하다는 것은 [§준연접층, ⁋정의 4](/ko/math/scheme_theory/quasicoherent_sheaves#def4)을 사용하여, [정의 5](#def5)에서의 section이 정확히 $\mathcal{O}(d)(D_+(\x_i))=M_i$으로 나온다는 것을 확인하면 된다. 여기에서 $S(d)$로 grading을 옮긴 것은 $S_{\x_i}$의 degree $d$ 부분을 각 chart가 함수로 채택하는 degree $0$ 부분으로 옮겨 적기 위한 표기이다.

[\[대수다양체\] §선다발과 벡터다발, ⁋예시 12](/ko/math/algebraic_varieties/line_bundles#ex12)에서 살펴보았듯, 우리의 기본적인 문제의식은 projective space의 closed subscheme들을 표현하려면 degree $d$ homogeneous polynomial들이 필요하지만, 이들은 기본적으로 그 zero set만 잘 정의되고, 함숫값 자체는 잘 정의되지 않기 때문에 실제 함수로 볼 수 없다는 것이다. 이를 해결하는 방식 중 하나는 각각의 coordinate $\x_i$가 $0$이 되지 않는 열린집합 $D_+(\x_i)$을 택한 후, 이 polynomial을 $\x_i^d$로 나누면 이것이 degree $0$이 되어 이 열린집합 위의 함수로 취급하는 것이다. 다만 이는 각각의 chart $D_+(\x_i)$마다 canonical하지 않은 trivialization을 하나씩 고른 것이며, chart마다 다른 선택을 한 이들이 겹치는 부분에서 호환되지 않으므로 여전히 이들은 $\mathcal{O}_{\mathbb{P}^n_A}$의 global section이 되지는 못한다. 그러나 위와 같이 $\mathcal{O}(d)$를 정의하면 이 <em-ko>함수</em-ko>들을 chart마다 모아 놓은 것이 이 sheaf의 global section이 되며, 그 section이 처음의 polynomial 자신이 된다. 또 $M_i$가 $\x_i^d$를 generator로 하는 rank $1$ free $S_{(\x_i)}$-module이어서 transition function $(\x_i/\x_j)^d$들이 가역이므로, 이 sheaf는 invertible sheaf이며 ([§준연접층, ⁋정의 12](/ko/math/scheme_theory/quasicoherent_sheaves#def12)) 따라서 line bundle $\mathcal{O}(d)$로 해석할 수도 있다. 한편 이렇게 chart마다의 데이터와 겹치는 부분에서의 비교로 대상을 기술하는 방식은 그대로 Čech complex의 재료이기도 하다. 따라서 이 데이터들의 gluing은 정확히 $\mathcal{O}(d)$의 (Čech) cohomology에 의해 결정된다. 

::: 정리 6 (Bott)
Ring $A$ 위의 projective space $\mathbb{P}^n_A$의 line bundle $\mathcal{O}(d)$의 cohomology는

$$H^q(\mathbb{P}^n_A, \mathcal{O}(d))=\begin{cases}A[\x_0,\ldots, \x_n]_d & q=0,\ d\geq 0 \\ A[\x_0^{-1},\ldots, \x_n^{-1}]_{-d-n-1} & q=n,\ d\leq -n-1 \\ 0 & \text{otherwise}\end{cases}$$

로 주어진다. 특히 $0<q<n$에서는 모든 $d$에 대해 소멸한다.
:::
::: 증명
$\mathbb{P}^n_A$이 separated scheme이므로 [따름정리 4](#cor4)에 의하여 standard affine cover $\mathcal{U}=\{D_+(\x_i)\}$에 대한 Čech cohomology가 곧 derived functor cohomology이다. 그런데 이 Čech complex는 [\[대수다양체\] §사영공간의 코호몰로지, ⁋명제 1](/ko/math/algebraic_varieties/cohomology_of_projective_spaces#prop1)의 증명에 등장하는 것과 글자 그대로 같다. 즉 각 교집합 $D_+(\x_{i_0}\cdots\x_{i_p})$ 위에서 $\mathcal{O}(d)$의 section은 $\x_{i_0},\ldots, \x_{i_p}$만을 분모로 허용하는 $d$차 monomial들

$$\x_0^{a_0}\cdots\x_n^{a_n}, \qquad \sum_{j=0}^n a_j=d,\quad a_j\geq 0\ \text{for}\ j\not\in\{i_0,\ldots, i_p\}$$

로 $A$ 위에서 생성되며, coboundary map 또한 동일한 교대합 공식으로 주어진다. 그곳의 증명은 coboundary map이 monomial의 지수벡터 $a=(a_0,\ldots, a_n)$을 바꾸지 않는다는 것에서 출발하여 Čech complex를 $a$마다의 부분복합체로 쪼갠다. 지수가 음수인 자리들의 집합을 $N_{<0}(a)$라 하면 위의 조건은 $\x^a$가 $D_+(\x_{i_0}\cdots\x_{i_p})$ 위에서 regular한 것이 $N_{<0}(a)\subseteq\{i_0,\ldots, i_p\}$와 동치라는 말이므로, $a$에 대응하는 부분복합체는 $N_{<0}(a)$를 포함하는 첨자 부분집합들이 이루는 simplex의 cochain complex가 된다. 그럼 $N_{<0}(a)$가 공집합인 경우 $q=0$에만, 전체집합인 경우 $q=n$에만 기여하고 그 사이인 경우에는 아무것도 기여하지 않아 세 경우가 한 번에 나온다. 이 논증은 계수가 체라는 것을 전혀 쓰지 않고 각 부분복합체가 자유 $A$-module들로 이루어진다는 것만 쓰므로, 그 증명을 $A$-계수로 그대로 읽으면 위의 결과를 얻는다.

마지막으로 $q=n$, $d\leq -n-1$에서 얻어지는 공간이 표기 $A[\x_0^{-1},\ldots, \x_n^{-1}]_{-d-n-1}$로 적히는 이유는 [\[대수다양체\] §사영공간의 코호몰로지, ⁋명제 1](/ko/math/algebraic_varieties/cohomology_of_projective_spaces#prop1) 직후의 설명과 동일하다. 즉 모든 지수가 $-1$ 이하인 $d$차 monomial들을 $\y_j=\x_j^{-1}$로 치환하면 모든 지수가 $1$ 이상인 $\lvert d\rvert$차 monomial들이 되고, 여기에서 공통인수 $\y_0\cdots\y_n$을 덜어내면 $\lvert d\rvert-(n+1)=-d-n-1$차의 "음의 degree" monomial 공간과 일대일로 대응한다.
:::

## Noetherian projective scheme 위의 연접층

이제 우리는 더 일반적으로 Noetherian projective scheme $X$와 그 위의 coherent sheaf  $\mathcal{F}$의 sheaf cohomology를 살펴본다. 핵심적인 결과는 두 개로, 하나는 각각의 $H^i(X, \mathcal{F})$가 유한차원이라는 것이고, 다른 하나는 $\mathcal{F}$를 충분히 twist하면 higher cohomology가 소멸한다는 Serre vanishing이다. 

이를 위해 사용할 도구 중 하나는 projective scheme 위에 정의된 line bundle $\mathcal{O}_X(1)$의 존재이다. Projective scheme $X$는 정의에 의하여 closed embedding $\iota: X\hookrightarrow \mathbb{P}^n$을 주며, 이를 사용하여 $\mathbb{P}^n$의 line bundle $\mathcal{O}_{\mathbb{P}^n}(1)$을 pullback해와서

$$\mathcal{O}_X(1)=\mathcal{O}_{\mathbb{P}^n}(1)\vert_X=\iota^\ast \mathcal{O}_{\mathbb{P}^n}(1)$$

을 정의할 수 있다. 이 때 좌표들의 restriction $\x_0\vert_X,\ldots, \x_n\vert_X$이 $\mathcal{O}_X(1)$을 globally generate하고 이들이 정의하는 morphism이 곧 포함사상 $X\hookrightarrow\mathbb{P}^n_\mathbb{K}$이므로, 위의 line bundle이 사실상 이 embedding 그 자체라고 보아도 무방하다. 즉 $\mathcal{O}_X(1)$은 very ample invertible sheaf이며 ([§인자와 선형계, ⁋정의 17](/ko/math/scheme_theory/divisors_and_linear_systems#def17)) 이 때 임의의 coherent sheaf $\mathcal{F}$에 대해 $\mathcal{F}(d)=\mathcal{F}\otimes_{\mathcal{O}_X}\mathcal{O}_X(d)$로 적는다.

핵심적인 관찰은 closed embedding $\iota:X\hookrightarrow\mathbb{P}^n$을 따라 cohomology가 보존된다는 것, 곧 $X$ 위의 임의의 quasi-coherent sheaf $\mathcal{F}$에 대하여

$$H^i(X, \mathcal{F})\cong H^i(\mathbb{P}^n, \iota_\ast\mathcal{F})\tag{$\ast$}$$

이 성립한다는 것이다. 이는 양변을 계산하는 Čech complex가 같은 complex이기 때문이다. 실제로, closed embedding은 affine morphism이므로 ([§닫힌 부분스킴, ⁋명제 3](/ko/math/scheme_theory/closed_subschemes#prop3)) 각 $U_i=\iota^{-1}(D_+(\x_i))$는 affine scheme이고 $\{U_i\}$는 $X$의 affine open cover이다. 한편 pushforward의 정의에 의하여,

$$(\iota_\ast\mathcal{F})(D_+(\x_{i_0}\cdots\x_{i_p}))=\mathcal{F}\bigl(\iota^{-1}(D_+(\x_{i_0})\cap\cdots\cap D_+(\x_{i_p}))\bigr)=\mathcal{F}(U_{i_0}\cap\cdots\cap U_{i_p})$$

이고 restriction map 또한 서로 대응되므로, $\{U_i\}$에 대한 $\mathcal{F}$의 Čech complex와 $\mathcal{U}$에 대한 $\iota_\ast\mathcal{F}$의 Čech complex는 동일한 complex이다. 그런데 $X$와 $\mathbb{P}^n$은 모두 projective scheme이라 separated이고 $\iota_\ast\mathcal{F}$ 또한 quasi-coherent이므로 ([§준연접층, ⁋정리 16](/ko/math/scheme_theory/quasicoherent_sheaves#thm16)), [따름정리 4](#cor4)에 의하여 이 하나의 complex의 cohomology가 양변을 동시에 계산하며, 이로써 위의 isomorphism을 얻는다.

아래의 두 정리는 모두 coherent sheaf를 충분히 twist하면 global section만으로 생성된다는 사실에서 출발하므로, 이를 먼저 확립한다.

::: 보조정리 7
Field $\mathbb{K}$ 위의 projective space $\mathbb{P}^n_\mathbb{K}$ 위의 coherent sheaf $\mathcal{F}$에 대하여, 충분히 큰 $d\gg 0$에 대해 $\mathcal{F}(d)$은 globally generated이다.
:::
::: 증명
$S_\bullet=\mathbb{K}[\x_0,\ldots, \x_n]$로 두고 graded $S_\bullet$-module

$$\Gamma_\ast(\mathcal{F})=\bigoplus_{m\in\mathbb{Z}}\Gamma(\mathbb{P}^n, \mathcal{F}(m))$$

을 생각하자. 우리는 우선 각 standard affine chart 위에서의 등식

$$\Gamma(D_+(\x_j), \mathcal{F})=\Gamma_\ast(\mathcal{F})_{(\x_j)}$$

을 보인다. 즉, $D_+(\x_j)$ 위의 section이 모두 global twisted section에서 온다는 것을 보여야 하며, 이는 $D_+(\x_j)$ 위의 임의의 section이 주어졌을 때, $\x_j$의 충분히 큰 거듭제곱을 곱하면 이것이 $\mathbb{P}^n$의 global section으로부터 나온다는 것이다.

이는 chart마다 따로 확인한 뒤 붙이는 방식으로 얻어진다. 표기를 줄여 $U_i=D_+(\x_i)$로 적자. $s\in\Gamma(U_j, \mathcal{F})$를 고정하고 각각의 $i$를 보면, $U_i\cap U_j$는 $U_i=\Spec S_{(\x_i)}$에서 $\x_j/\x_i$를 뒤집어 얻어지는 principal open set이므로 [§준연접층, ⁋명제 5](/ko/math/scheme_theory/quasicoherent_sheaves#prop5)로부터

$$\Gamma(U_i\cap U_j, \mathcal{F})=\Gamma(U_i, \mathcal{F})_{\x_j/\x_i}$$

를 얻는다. 즉 $s\vert_{U_i\cap U_j}$는 적당한 $e_i\geq0$과 $t_i\in\Gamma(U_i, \mathcal{F})$에 대하여 $t_i\vert_{U_i\cap U_j}$를 $(\x_j/\x_i)^{e_i}$로 나눈 것이고, 따라서 양변에 $\x_i^{e_i}(\x_j/\x_i)^{e_i}=\x_j^{e_i}$를 곱하면

$$\x_j^{e_i}\cdot s\vert_{U_i\cap U_j}=(\x_i^{e_i}t_i)\vert_{U_i\cap U_j}$$

가 된다. 그럼 이 식의 양변은 $\mathcal{F}(e_i)$의 section이고, 우변은 $U_i$ 전체에서 정의된 section $\x_i^{e_i}t_i\in\Gamma(U_i, \mathcal{F}(e_i))$를 제한한 것이며 따라서 $\x_j^{e_i}s$가 $U_i$ 위로 extend된다. 이제 이러한 chart는 유한개이므로, $e=\max e_i$로 두고

$$u_i=\x_j^{e-e_i}\x_i^{e_i}t_i\in\Gamma(U_i, \mathcal{F}(e))$$

로 두면 모든 $i$에 대하여 $u_i\vert_{U_i\cap U_j}=\x_j^es\vert_{U_i\cap U_j}$이다. 남는 것은 서로 다른 두 chart에서 얻은 $u_i$와 $u_{i'}$이 $U_i\cap U_{i'}$ 위에서 일치하는지, 즉 cocycle condition인데, 이들의 차는 $U_i\cap U_{i'}\cap U_j$ 위에서 $0$이고 이 열린집합 또한 $U_i\cap U_{i'}$에서 $\x_j$의 비를 뒤집어 얻어지므로, 위와 같은 localization 등식에 의하여 $\x_j$의 적당한 거듭제곱이 그 차를 소멸시킨다. 다시 이러한 쌍들이 유한개이므로, 충분히 큰 공통된 정수 $f$를 잡으면 $\x_j^fu_i$들이 서로 일치하여 하나의 $t\in\Gamma(\mathbb{P}^n, \mathcal{F}(e+f))$로 붙으며, $t\vert_{U_j}=\x_j^{e+f}s$이 된다.

거꾸로 $t\in\Gamma(\mathbb{P}^n, \mathcal{F}(m))$에 대한 $t/\x_j^m$이 $U_j$ 위에서 $0$이라 하자. 그럼 각각의 $i$에 대하여 $t\vert_{U_i}$의 $U_i\cap U_j$로의 restriction이 $0$이므로, 위의 localization 등식에 의하여 $(\x_j/\x_i)^{q_i}t\vert_{U_i}=0$인 $q_i$가 존재한다. Chart가 유한개이므로 $q=\max q_i$로 두면 $\x_j^qt=0$이고, 따라서 $t/\x_j^m$은 $\Gamma_\ast(\mathcal{F})_{(\x_j)}$에서 이미 $0$이다. 이로써 위의 등식이 성립한다.

이제 우변의 $\Gamma_\ast(\mathcal{F})_{(\x_j)}$은 $S_{(\x_j)}$ 위의 finitely generated module이므로, 각각의 chart마다 그 generator들을

$$m_{jk}/\x_j^{e_{jk}},\qquad m_{jk}\in\Gamma(\mathbb{P}^n, \mathcal{F}(e_{jk}))$$

꼴로 적을 수 있다. Chart도 generator도 유한개이므로 $d_0=\max_{j,k}e_{jk}$가 잘 정의되며, 그럼 각각의 generator $m_{jk}$에 $\x_j^{d_0-e_{jk}}$를 곱한 $m_{jk}\x_j^{d_0-e_{jk}}\in\Gamma(\mathbb{P}^n, \mathcal{F}(d_0))$들이 각각의 $D_+(\x_j)$ 위에서 $\mathcal{F}(d_0)$의 stalk를 생성한다. 이 chart들이 $\mathbb{P}^n$을 덮으므로 $\mathcal{F}(d_0)$은 globally generated이며, $d\geq d_0$이면 $\mathcal{F}(d)=\mathcal{F}(d_0)\otimes\mathcal{O}(d-d_0)$ 또한 globally generated이다.
:::

::: 정리 8
Field $\mathbb{K}$ 위의 Noetherian projective scheme $X$와 그 위의 coherent sheaf $\mathcal{F}$에 대하여, 각 $H^i(X, \mathcal{F})$은 유한차원 $\mathbb{K}$-벡터공간이며, 충분히 큰 $i$에 대해서는 $0$이다.
:::
::: 증명
위의 isomorphism $(\ast)$에 의하여 quasi-coherent sheaf $\iota_\ast\mathcal{F}$이 ([§준연접층, ⁋정리 16](/ko/math/scheme_theory/quasicoherent_sheaves#thm16)) $\mathbb{P}^n$ 위의 coherent sheaf임만 확인하면 $X=\mathbb{P}^n_{\mathbb{K}}$이라 가정해도 된다. 이를 위해서는 finite type 조건만 affine-local하게 체크하면 되는데, 이는 $\iota$가 closed embedding이므로 각 chart 위에서 $\iota_\ast\mathcal{F}$은 $A$-algebra $A/I$ 위의 finitely generated module을 $A$-module로 본 것이고, $A \rightarrow A/I$가 전사이므로 $A/I$ 위의 generator를 $A$로 들어올리면 같은 원소들이 $A$ 위에서도 생성하기 때문이다.

따라서 $\mathbb{P}^n$ 위의 coherent sheaf $\mathcal{F}$에 대한 명제만 보이면 충분하다. 우선 충분히 큰 cohomological dimension $i>n$에서 $H^i=0$인데, 이는 $\mathbb{P}^n$이 $n+1$개의 열린집합으로 덮이므로 그 Čech complex 단계에서 이미 이 항들이 $0$이기 때문이다. 

이제 나머지 항들에 대한 유한성을 $i$에 대한 내림차순 귀납으로 보인다. 이미 위에서 큰 dimension에 대해서는 이것이 $0$임을 보였으므로, 귀납단계만 보이면 충분하다. 임의의 coherent sheaf $\mathcal{F}$에 대하여, [보조정리 7](#lem7)에 의하여 적당한 $d\gg 0$에서 $\mathcal{F}(d)$이 globally generated이므로 유한 개의 global section이 surjection

$$\mathcal{O}_{\mathbb{P}^n}^{\oplus r} \twoheadrightarrow \mathcal{F}(d)$$

을 주고, 이를 $\mathcal{O}(-d)$로 twist하면 $\mathcal{O}(-d)^{\oplus r}\twoheadrightarrow\mathcal{F}$을 얻는다. $\mathbb{P}^n$이 Noetherian이므로 각 affine chart 위에서 finitely generated module의 submodule은 다시 finitely generated이고 ([\[가환대수학\] §기본 개념들, ⁋정리 3](/ko/math/commutative_algebra/basic_notions#thm3)), 따라서 그 kernel $\mathcal{K}$ 또한 finite type, 곧 coherent sheaf이다. 그럼 coherent sheaf들의 short exact sequence

$$0 \rightarrow \mathcal{K} \rightarrow \mathcal{O}(-d)^{\oplus r} \rightarrow \mathcal{F} \rightarrow 0$$

의 long exact sequence에서

$$H^i(\mathbb{P}^n, \mathcal{O}(-d)^{\oplus r}) \rightarrow H^i(\mathbb{P}^n, \mathcal{F}) \rightarrow H^{i+1}(\mathbb{P}^n, \mathcal{K})$$

을 보면, 좌변은 [정리 6](#thm6)에 의하여 유한차원이고, 우변은 귀납가정에 의하여 유한차원이므로, 가운데 항 $H^i(\mathbb{P}^n, \mathcal{F})$ 또한 유한차원이다. 
:::

위 증명의 핵심적인 논증은 coherent sheaf를 충분히 twist하여 globally generated로 만든 뒤, 이를 free sheaf로 덮는 것이다. 그럼 이로부터 $\mathbb{P}^n$의 cohomology의 유한성이 long exact seqeunce를 따라 옮겨가서 정리의 주장을 주었다. 그런데 [정리 6](#thm6)은 모든 차수에서 cohomology가 finite dimension이라는 것 뿐만 아니라, 높은 차수의 cohomology는 아예 소멸한다는 것까지 보여주므로, 이 방향으로 논증을 전개하면 다음 결과를 얻는다. 

::: 정리 9 (Serre Vanishing)
Field $\mathbb{K}$ 위의 Noetherian projective scheme $X$와 그 위의 coherent sheaf $\mathcal{F}$에 대하여, 충분히 큰 $d\gg 0$에 대해

$$H^i(X, \mathcal{F}(d))=0 \qquad (i>0)$$

이 성립한다. 더욱이 이러한 $d$에 대해 $\mathcal{F}(d)$은 globally generated이다.
:::
::: 증명
[정리 8](#thm8)에서와 같이 $(\ast)$에 의하여 $X=\mathbb{P}^n_{\mathbb{K}}$이고 $\mathcal{O}_X(1)=\mathcal{O}(1)$인 경우로 환원할 수 있다. 명제가 twisting을 포함하므로, 이를 위해 추가로 필요한 등식은 

$$\iota_\ast(\mathcal{F}(d))\cong(\iota_\ast\mathcal{F})(d)$$ 

이며 이는 $\mathcal{O}_X(1)=\iota^\ast\mathcal{O}(1)$이므로 [§준연접층, ⁋명제 17](/ko/math/scheme_theory/quasicoherent_sheaves#prop17)으로부터 바로 따라나온다.

이 환원 아래에서 global generation 또한 함께 옮겨진다. Closed embedding을 따라 $x\in X$에서 $(\iota_\ast\mathcal{G})_{\iota(x)}=\mathcal{G}_x$이고 $\Gamma(\mathbb{P}^n, \iota_\ast\mathcal{G})=\Gamma(X, \mathcal{G})$이므로, $(\iota_\ast\mathcal{F})(d)$가 globally generated이면 $\mathcal{F}(d)$ 또한 그러하기 때문이다. 그럼 [보조정리 7](#lem7)이 $d\geq d_0$마다 $\mathcal{F}(d)$을 globally generated로 만드는 $d_0$을 주므로, 남은 것은 vanishing뿐이다.

이제 남은 것은 vanishing으로, 이는 [정리 8](#thm8)과 마찬가지로 $i$에 대한 내림차순 귀납으로 본다. $i>n$에서는 chart의 개수로부터 $H^i=0$이므로 귀납단계만 보이면 충분하다. 임의의 $i\geq1$에 대하여, globally generated 성질로부터 surjection $\mathcal{O}^{\oplus r}\twoheadrightarrow\mathcal{F}(d_0)$을 잡아서 다음의 short exact sequence

$$0 \rightarrow \mathcal{K} \rightarrow \mathcal{O}^{\oplus r} \rightarrow \mathcal{F}(d_0) \rightarrow 0$$

을 얻을 수 있다. 여기서 $\mathcal{K}$는 이 surjection의 kernel이며 [정리 8](#thm8)의 증명과 같은 이유로 coherent sheaf이다. 이제 이를 $\mathcal{O}(d-d_0)$로 twist하면

$$0 \rightarrow \mathcal{K}(d-d_0) \rightarrow \mathcal{O}(d-d_0)^{\oplus r} \rightarrow \mathcal{F}(d) \rightarrow 0$$

이고, 이것이 주는 long exact sequence

$$H^i(\mathbb{P}^n, \mathcal{O}(d-d_0)^{\oplus r}) \rightarrow H^i(\mathbb{P}^n, \mathcal{F}(d)) \rightarrow H^{i+1}(\mathbb{P}^n, \mathcal{K}(d-d_0))$$

을 보자. 좌변은 [정리 6](#thm6)에 의하여 $d-d_0\gg0$이고 $i>0$이면 $0$이다. 우변은 귀납 가정을 $\mathcal{K}$에 적용한 것으로, $i+1$에서의 vanishing이 충분히 큰 twist에 대해 성립한다. 따라서 $d$가 이 둘을 모두 $0$으로 만들만큼 크다면 가운데 항 $H^i(\mathbb{P}^n, \mathcal{F}(d))$이 소멸한다. 이제 $i$가 $1$부터 $n$까지 유한하므로, 모든 $i>0$에 대한 vanishing을 동시에 보장하는 공통의 $d_1$을 잡을 수 있고, $d\geq d_1$에서 $H^i(\mathbb{P}^n, \mathcal{F}(d))=0$ ($i>0$)이다.
:::

이는 [\[대수다양체\] §사영공간의 코호몰로지, ⁋명제 7](/ko/math/algebraic_varieties/cohomology_of_projective_spaces#prop7)의 Serre vanishing을 scheme 수준으로 옮긴 것이다. 함께 얻은 global generation은 임의의 coherent sheaf를 $\mathcal{O}(-d)$들의 finite direct sum의 quotient로 적을 수 있게 해 주므로, 이를 되풀이하면 이러한 sheaf들에 의한 resolution을 얻는다.

## Ampleness의 코호몰로지 판정

한편, 앞선 섹션의 결과들을 보이기 위해 중요하게 사용한 사실은 $\mathcal{O}_X(1)$이 $X$를 projective space 안으로 넣는 embedding에서 온다는 것, 곧 very ample이라는 것이었다. 우리는 이미 [\[대수다양체\] §선형계, ⁋정의 10](/ko/math/algebraic_varieties/linear_systems#def10)으로부터 very ampleness와 ampleness가 밀접한 관련이 있는 것을 알고 있으며, 따라서 [§인자와 선형계](/ko/math/scheme_theory/divisors_and_linear_systems)에서 정의한 (scheme 버전의) ampleness 또한 이와 관련있을 것이다. 우선 다음이 성립한다.

::: 따름정리 10
Field $\mathbb{K}$ 위의 Noetherian projective scheme $X$ 위의 very ample invertible sheaf $\mathcal{L}$은 ample이다. ([§인자와 선형계, ⁋정의 18](/ko/math/scheme_theory/divisors_and_linear_systems#def18))
:::
::: 증명
$\mathcal{L}$이 very ample이므로 이를 globally generate하는 유한 개의 section이 locally closed embedding $\iota:X \rightarrow \mathbb{P}^N_\mathbb{K}$를 정의하고 $\mathcal{L}\cong\iota^\ast\mathcal{O}(1)$이다. ([§인자와 선형계, §§Ample invertible sheaf](/ko/math/scheme_theory/divisors_and_linear_systems#ample-invertible-sheaf)) $X$가 $\mathbb{K}$ 위에서 projective이므로 $\iota(X)$는 닫힌집합이며 ([§값매김환, ⁋따름정리 16](/ko/math/scheme_theory/valuative_criteria#cor16)), 따라서 $\iota$는 closed embedding이다. 그럼 $\mathcal{L}$은 [정리 9](#thm9)에서 $\mathcal{O}_X(1)$이 맡은 역할을 그대로 할 수 있으므로, 임의의 coherent sheaf $\mathcal{F}$에 대하여 충분히 큰 모든 $d$에서 $\mathcal{F}\otimes\mathcal{L}^{\otimes d}$은 globally generated이다. 이것이 ampleness의 정의이다.
:::

그러나 이 따름정리의 역방향은 성립하지 않는다. Ample invertible sheaf는 section이 부족하여 embedding을 주지 못할 수 있고, 이를 해소하려면 여러 번 tensor하여 section을 늘려야 한다. 다음 정리는 그것이 언제나 가능함을 말해준다.

::: 정리 11
Field $\mathbb{K}$ 위의 Noetherian projective scheme $X$ 위의 invertible sheaf $\mathcal{L}$에 대하여, $\mathcal{L}$이 ample인 것과 적당한 $m>0$에 대하여 $\mathcal{L}^{\otimes m}$이 very ample인 것은 서로 동치이다.
:::
::: 증명
$\mathcal{L}^{\otimes m}$이 very ample이라 하자. [따름정리 10](#cor10)에 의하여 $\mathcal{L}^{\otimes m}$은 ample이고, [§인자와 선형계, ⁋명제 19](/ko/math/scheme_theory/divisors_and_linear_systems#prop19)의 둘째 결과에 의하여 $\mathcal{L}$ 또한 ample이다.

거꾸로 $\mathcal{L}$이 ample이라 하자. 우리는 $\mathcal{L}$의 적당한 거듭제곱의 global section들이 정의하는 locally closed embedding을 만들어야 한다. 정의에 의해 $\mathcal{L}$의 적당한 거듭제곱이 globally generated이며 이러한 section들은 언제나 morphism $X \rightarrow \mathbb{P}^M$을 주므로 우리가 실제로 보여야 할 것은 이 morphism이 embedding을 준다는 것이다. 

$\mathcal{L}^{\otimes k}$을 globally generate하는 section들 $s_0,\ldots, s_M\in\Gamma(X, \mathcal{L}^{\otimes k})$이 주는 morphism $\varphi:X \rightarrow \mathbb{P}^M$을 생각하자. 이는 $\mathbb{P}^M$의 좌표 $\x_i$를 $s_i$로 pullback하는 morphism으로, 이로부터 standard chart $D_+(\x_i)$의 preimage는 정확히 $s_i$가 소멸하지 않는 열린집합 $X_{s_i}$이 된다. 그럼 morphism이 closed embedding이 되는 것은 target에서 local한 성질이므로, 우리는 다음의 morphism들

$$\varphi\vert_{X_{s_i}}: X_{s_i} \rightarrow D_+(\x_i)$$

이 closed embedding임을 보이면 된다. 우리 주장은 위의 section들을 아주 잘 택하면 $X_{s_i}$가 affine scheme이 되어, 위의 closed embedding이 affine scheme 사이의 morphism이고, 따라서 이 판정이 그에 대응되는 ring homomorphism의 전사성으로 내려온다는 것이다. 이 때, $D_+(\x_i)$의 coordinate ring은 ratio들 $\x_j/\x_i$들이 생성하는 polynomial ring이고, $\varphi\vert_{X_{s_i}}$에 대응하는 ring homomorphism은 이를 $s_j/s_i\in\Gamma(X_{s_i}, \mathcal{O}_X)$로 보내므로, 전사성은 이 비들이 $\Gamma(X_{s_i}, \mathcal{O}_X)$를 $\mathbb{K}$-대수로서 생성한다는 것과 같다.

따라서 우리의 첫 번째 목표는 $\mathcal{L}^{\otimes k}$을 globally generate하는 section들 가운데, $X_{s_i}$들이 모두 affine이도록 하는 것들을 찾는 것이다. 이를 위해 우리는 각각의 closed point $x\in X$마다 $x$를 품으면서 affine인 $X_s$를 하나씩 만들 것이다. 우선 $x$를 포함하는 $\mathcal{L}$의 trivializing open affine neighborhood $U$를 택하자. 만일 적당한 section $s$가 $X_s\subseteq U$를 만족한다면 $X_s$가 affine인 것은 $X_s$를 $U$ 안에서 함수 $s$가 정의하는 principal open set으로 보면 바로 얻어지므로, 우리가 찾아야 할 $s$는 $x$에서 non-vanishing이면서 $Y=X\setminus U$에서는 identically zero인 section이다.  

이를 위해 $Y$에 reduced closed subscheme 구조를 준 후, 그 ideal sheaf $\mathcal{I}_Y$를 생각하자. 이는 $\mathcal{O}_X \rightarrow \iota_\ast\mathcal{O}_Y$의 kernel이므로 quasi-coherent이고, 각각의 affine chart $\Spec A$ 위에서는 $A$의 ideal에 대응한다. 그런데 $X$가 Noetherian이라 $A$ 또한 그러하여 이 ideal이 finitely generated이므로 ([\[가환대수학\] §기본 개념들, ⁋정리 3](/ko/math/commutative_algebra/basic_notions#thm3)), $\mathcal{I}_Y$는 coherent sheaf이다. 따라서, $\mathcal{L}$의 ampleness로부터 적당한 $n>0$에 대해 $\mathcal{I}_Y\otimes\mathcal{L}^{\otimes n}$이 globally generated임을 안다. 이 때, $x\not\in Y$이므로  $(\mathcal{I}_Y)_x=\mathcal{O}_{X,x}$이고, 따라서 $x$에서 소멸하지 않는 section $s\in\Gamma(X, \mathcal{I}_Y\otimes\mathcal{L}^{\otimes n})\subseteq\Gamma(X, \mathcal{L}^{\otimes n})$이 존재하고, 이로부터 각각의 closed point마다 이를 포함하는 affine open set $X_s$를 택할 수 있다. 뿐만 아니라, $X$가 $\mathbb{K}$ 위에서 finite type이므로 각 affine chart의 coordinate ring은 Jacobson ring이고 ([\[가환대수학\] §영점정리, ⁋정리 4](/ko/math/commutative_algebra/nullstellensatz#thm4)), 따라서 $X$의 공집합이 아닌 닫힌집합은 언제나 $X$의 closed point를 포함한다. 즉, closed point들에서 얻은 위의 열린집합들의 합집합은 여집합이 closed point를 갖지 않는 닫힌집합이라 $X$ 전체이며, $X$가 quasi-compact이므로 그 가운데 유한 개 $X_{s_1},\ldots, X_{s_q}$만으로도 $X$를 덮는다. 다만 이들은 각각 $s_i\in\Gamma(X, \mathcal{L}^{\otimes n_i})$로 지수가 서로 다른 sheaf에서 얻어졌으므로, 함께 하나의 morphism을 정의하려면 같은 sheaf의 section이 되도록 지수를 이들의 최소공배수 $m$으로 맞추고, $s_i$들을 $s_i^{m/n_i}$으로 바꾸어 $s_i\in \Gamma(X, \mathcal{L}^{\otimes m})$이도록 해야 하며, 이 과정은 임의의 $e\geq1$에 대해 $X_{s^e}=X_s$이므로 정당화된다. 

이제  $X_{s_i}$가 affine이고 $X$가 $\mathbb{K}$ 위에서 finite type이므로 각각의 $B_i=\Gamma(X_{s_i}, \mathcal{O}_X)$는 finitely generated $\mathbb{K}$-algebra이며, 그 generator $b_{i1},\ldots, b_{ir_i}$들을 택할 수 있다. 이제 우리의 주장은 

$$b_{ij}=t_{ij}/s_i^N, \qquad t_{ij}\in\Gamma(X, \mathcal{L}^{\otimes mN})$$

이 성립하도록 하는 공통의 $N$과 global section $t_{ij}$들이 존재하여, $s_1^N,\ldots, s_q^N$들과 $t_{ij}$들이 $\mathcal{L}^{\otimes mN}$을 globally generate하도록 할 수 있다는 것이다. 만일 이것이 성립한다면, 이들이 $s_i^N$의 chart 위에서 주는 ratio 중 $t_{ij}/s_i^N=b_{ij}$가 있으므로 우리가 원하는 전사성, 즉 affine scheme으로 제한했을 때 $\varphi$가 closed embedding이 된다는 사실이 증명될 것이다. 이 때 확인하는 chart는 $s_i^N$에 대응하는 것들뿐이지만 $X_{s_i}$들이 $X$를 덮으므로, 이는 $\varphi$가 이 chart들의 합집합으로의 closed embedding, 곧 locally closed embedding이라는 뜻이다.

이를 위해 $\mathcal{L}^{\otimes m}$의 trivializing affine open cover $V_1,\ldots, V_p$를 택하고 각각의 $V_l=\Spec A_l$ 위에서 trivialization을 하나 고정하면, $s_i$는 함수 $g_{il}\in A_l$에 대응하고 $X_{s_i}\cap V_l=D(g_{il})$이다. 그럼 $X_{s_i}$ 위의 함수들 $b_{ij}$의 $D(g_{il})$로의 restriction은 $(A_l)_{g_{il}}$의 원소이므로, $g_{il}$의 적당한 거듭제곱을 곱하면 $A_l$의 원소가 되며, 이때의 지수는 $i$와 $j$, $l$에 대해 유한 개이므로 그 최댓값 $N_0$을 취하면 모든 $l$에 대해 $s_i^{N_0}b_{ij}$가 $V_l$ 위에서 $\mathcal{L}^{\otimes mN_0}$의 section으로 extend되도록 할 수 있다. 이제 남은 것은 이들을 붙여 global section $t_{ij}$로 만들 수 있다는 것을 보이는 것이다. 

이를 위해 두 chart $V_l$과 $V_{l'}$에서 얻은 extension을 보면, 이들은 $X_{s_i}\cap V_l\cap V_{l'}$ 위에서 일치하지만 이것이 $V_l\cap V_{l'}$ 전체에서 일치할 이유는 없다. 이를 해결하기 위해 $\mathcal{L}^{\otimes m}$과 $\mathcal{L}^{\otimes mN_0}$을 동시에 trivialize하는 affine open cover를 잡고, 이들이 $V_l\cap V_{l'}$을 덮도록 하자. $X$가 Noetherian이므로, 이러한 affine open set들이 유한히 많도록 할 수 있다. 그럼 이러한 affine open set $\Spec C$ 위에서, $s_i$는 함수 $g\in C$에 대응하며, $V_l$과 $V_{l'}$에서의 두 extension의 차는 $D(g)$ 위에서 소멸하는 원소 $h\in C$가 된다. 그럼 $C_g$에서 $h=0$이므로 적당한 지수 $c$에 대해 $g^ch=0$이고, 곧 두 extension에 $s_i^c$를 곱하면 $V_l\cap V_{l'}$ 전체에서 일치한다. 이러한 지수 또한 유한 개이므로 그 최댓값 $c_0$을 취하여 $N=N_0+c_0$으로 두면, $s_i^{N_0}b_{ij}$의 chart별 extension에 $s_i^{c_0}$을 곱한 것들이 서로 일치하여 하나의 $t_{ij}\in\Gamma(X, \mathcal{L}^{\otimes mN})$으로 붙으며, 구성에 의하여 $t_{ij}$의 $X_{s_i}$로의 restriction은 $s_i^Nb_{ij}$이고, 이 때 이들이 $\mathcal{L}^{\otimes mN}$을 globally generate하는 것은 이미 $X_{s_i}$가 $X$를 덮으므로 자명하다. 
:::

[§인자와 선형계, ⁋명제 19](/ko/math/scheme_theory/divisors_and_linear_systems#prop19)의 2번에 의하여 $\mathcal{L}$이 ample인 것은 임의의 $m\geq1$에 대해 $\mathcal{L}^{\otimes m}$이 ample인 것과 동치이므로, [정리 11](#thm11)은 두 개념의 차이가 오직 거듭제곱을 취하는 것에서만 온다는 것을 말해준다. 여기에 [정리 9](#thm9)을 더하면 ampleness를 cohomology의 소멸만으로 판정할 수 있다.

::: 정리 12 (Serre criterion)
Field $\mathbb{K}$ 위의 Noetherian projective scheme $X$ 위의 invertible sheaf $\mathcal{L}$에 대하여 다음 두 조건은 서로 동치이다.

1. $\mathcal{L}$은 ample이다.
2. 임의의 coherent sheaf $\mathcal{F}$에 대하여 적당한 $n_0$가 존재하여, 모든 $i>0$과 $n\geq n_0$에 대해 $H^i(X, \mathcal{F}\otimes_{\mathcal{O}_X}\mathcal{L}^{\otimes n})=0$이다.
:::
::: 증명
첫째 조건이 둘째 조건을 함의하는 방향이 쉬우므로, 이를 먼저 살펴보자. $\mathcal{L}$이 ample이라면 [정리 11](#thm11)에 의하여 적당한 $m>0$에 대해 $\mathcal{L}^{\otimes m}$이 very ample이다. 그럼 [따름정리 10](#cor10)의 증명에서와 같이 $\mathcal{L}^{\otimes m}$이 정의하는 embedding은 closed embedding이므로, $\mathcal{L}^{\otimes m}$을 twisting sheaf로 삼아 [정리 9](#thm9)을 적용할 수 있다. 특히 유한 개의 coherent sheaf

$$\mathcal{F}\otimes\mathcal{L}^{\otimes q},\qquad q=0,1,\ldots, m-1$$

각각에 이를 적용하면, 각각의 $q$마다 $p_q$들이 존재하여, $p>p_q$인 모든 $p$에 대해

$$H^i\bigl(X, \mathcal{F}\otimes\mathcal{L}^{\otimes q}\otimes(\mathcal{L}^{\otimes m})^{\otimes p}\bigr)=0 \qquad (i>0)$$

이도록 할 수 있다. 이제 $n_0=m(\max p_q+1)$로 두면, 임의의 $n\geq n_0$는

$$n\geq n_0>m p_q+ q$$

를 모든 $q$에 대해 만족하므로 원하는 결과를 얻는다. 

따라서 이 정리의 핵심은 둘째 조건을 가정하고 첫째 조건을 보이는 것이다. 즉, 임의의 coherent sheaf $\mathcal{F}$를 고정하고, 충분히 큰 모든 $n$에 대해 $\mathcal{F}\otimes\mathcal{L}^{\otimes n}$이 globally generated라는 것을 보여야 한다. 

우선 closed point $x\in X$를 하나 고정하고, $\{x\}$에 reduced closed subscheme 구조를 주어 얻은 ideal sheaf를 $\mathcal{I}_x$라 하자. 즉 $\mathcal{I}_x$는 closed embedding $\iota:\{x\} \rightarrow X$가 주는 $\mathcal{O}_X \rightarrow \iota_\ast\mathcal{O}_{\{x\}}$의 kernel이고 ([§닫힌 부분스킴, ⁋정의 5](/ko/math/scheme_theory/closed_subschemes#def5)) $x$가 closed point이므로, $\{x\}$와 만나지 않는 열린집합 $U$에서는 $(\iota_\ast\mathcal{O}_{\{x\}})(U)=\mathcal{O}_{\{x\}}(U\cap\{x\})=0$이라 열린집합 $X\setminus \{x\}$ 위에서는 깔끔하게 $\mathcal{I}_x=\mathcal{O}_X$이다. 이제 $\mathcal{I}_x\mathcal{F}$를 multiplication map $\mathcal{I}_x\otimes\mathcal{F} \rightarrow \mathcal{F}$의 image라 하면, 그럼 각각의 affine chart $\Spec A$ 위에서 $\mathcal{I}_x$와 $\mathcal{F}$는 ideal $I\subseteq A$와 finitely generated $A$-module $M$에 대응하고 associated sheaf functor가 exact이므로 ([§준연접층, ⁋명제 6](/ko/math/scheme_theory/quasicoherent_sheaves#prop6)), $\mathcal{I}_x\mathcal{F}$는 chart마다 submodule $IM\subseteq M$의 associated sheaf이다. 이때 $X$가 Noetherian이라 $IM$ 또한 finitely generated이므로 ([\[가환대수학\] §기본 개념들, ⁋정리 3](/ko/math/commutative_algebra/basic_notions#thm3)), $\mathcal{I}_x\mathcal{F}$는 coherent sheaf이다. 그럼 short exact sequence

$$0 \rightarrow \mathcal{I}_x\mathcal{F} \rightarrow \mathcal{F} \rightarrow \mathcal{F}/\mathcal{I}_x\mathcal{F} \rightarrow 0$$

를 얻는다. 그런데 위의 계산에서, 우리는 이미 $\mathcal{I}_x$가 $\{x\}$ 바깥에서는 $\mathcal{O}_X$ 전체가 되는 것을 살펴보았고, 따라서 마지막 항 $\mathcal{F}/\mathcal{I}_x\mathcal{F}$의 stalk은 $x$ 바깥에서 소멸하며, $x$에서는 $\mathcal{I}_x$가 reduced structure의 ideal sheaf이므로 정확히 

$$(\mathcal{F}/\mathcal{I}_x\mathcal{F})_x=\mathcal{F}_x/\mathfrak{m}_x\mathcal{F}_x=\mathcal{F}_x\otimes_{\mathcal{O}_{X,x}}\kappa(x)$$

인 $x$ 위의 skyscraper sheaf이다. 이제 위 exact sequence에 $\mathcal{L}^{\otimes n}$을 텐서하면, 이것이 invertible이라 local하게는 $\mathcal{O}_X$와 isomorphic하고, 따라서 exactness가 보존되어

$$0 \rightarrow \mathcal{I}_x\mathcal{F}\otimes\mathcal{L}^{\otimes n} \rightarrow \mathcal{F}\otimes\mathcal{L}^{\otimes n} \rightarrow (\mathcal{F}/\mathcal{I}_x\mathcal{F})\otimes\mathcal{L}^{\otimes n} \rightarrow 0$$

또한 exact이며, 마지막 항은 값이 

$$(\mathcal{F}\otimes\mathcal{L}^{\otimes n})_x\otimes_{\mathcal{O}_{X,x}}\kappa(x)$$

인 $x$ 위의 skyscraper sheaf로 변한다. 이제 주어진 가정을 coherent sheaf $\mathcal{I}_x\mathcal{F}$에 적용하면 적당한 $n_1$이 존재하여 $n\geq n_1$마다 $H^1(X, \mathcal{I}_x\mathcal{F}\otimes\mathcal{L}^{\otimes n})=0$이므로, long exact sequence의 일부

$$\Gamma(X, \mathcal{F}\otimes\mathcal{L}^{\otimes n}) \longrightarrow (\mathcal{F}\otimes\mathcal{L}^{\otimes n})_x\otimes_{\mathcal{O}_{X,x}}\kappa(x) \longrightarrow 0$$

이 exact이다. 즉, $\mathcal{F}\otimes\mathcal{L}^{\otimes n}$의 global section들이 $x$에서의 fiber를 남김없이 준다. 이로부터 $x$의 근방에서의 global generation을 얻는다.

실제로 stalk $M=(\mathcal{F}\otimes\mathcal{L}^{\otimes n})_x$는 Noetherian local ring $\mathcal{O}_{X,x}$ 위의 finitely generated module이고 위 skyscraper sheaf의 fiber가 $M/\mathfrak{m}_xM$이므로, 유한 개의 global section $s_1,\ldots, s_c$를 그 germ들이 $M/\mathfrak{m}_xM$을 생성하도록 택할 수 있고, [\[가환대수학\] §정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)의 둘째 결과에 의하여 이들은 $M$ 자체를 생성한다. 그럼 $s_1,\ldots, s_c$가 정의하는 $\mathcal{O}_X^{\oplus c} \rightarrow \mathcal{F}\otimes\mathcal{L}^{\otimes n}$의 cokernel $\mathcal{Q}$는 coherent sheaf이면서 $\mathcal{Q}_x=0$을 만족한다. 여기서 $x$를 포함하는 affine 열린집합 $\Spec A$를 잡아 그 위에서 $\mathcal{Q}$에 대응하는 finitely generated $A$-module을 $N$, $x$에 대응하는 prime ideal을 $\mathfrak{p}$라 하면 $N_\mathfrak{p}=0$이므로 $N$의 각 generator를 소멸시키는 $\mathfrak{p}$ 밖의 원소가 존재하고, $N$의 generator가 유한 개이므로 이렇게 얻은 원소들의 곱을 $f$라 두면 $N_f=0$이다. 곧 $\mathcal{Q}$는 $x$의 열린근방 $D(f)$ 위에서 소멸하며, 이는 $\mathcal{F}\otimes\mathcal{L}^{\otimes n}$이 $D(f)$ 위에서 $s_1,\ldots, s_c$로 생성된다는 뜻이다.

즉, 우리는 각각의 closed point $x$마다 열린근방 $D(f)$가 존재하여, $D(f)$의 각 점에서 $\mathcal{F}\otimes\mathcal{L}^{\otimes n}$이 globally generated이도록 할 수 있음을 확인하였다. 다소 미묘한 것은 이 $D(f)$의 정의가 $n$마다 달라진다는 것으로, 정리의 증명을 끝마치기 위해서는 충분히 큰 모든 $n$에서 동시에 작동하는 하나의 근방이 필요하므로 본격적인 논증 이전에 고정된 근방 위에서 $\mathcal{L}$의 지수를 키울 방법을 찾아야 한다. 이를 위해 지금까지의 논증을 $\mathcal{F}=\mathcal{O}_X$에 적용하면 적당한 $e\geq1$에 대하여 $\mathcal{L}^{\otimes e}$과 $\mathcal{L}^{\otimes(e+1)}$이 각각 $x$의 어떤 열린근방 위에서 globally generated이고, 두 근방의 교집합 $W$ 위에서는 둘 다 그러하다. Globally generated인 두 sheaf의 tensor product는 stalk의 generator들의 tensor들에 의해 다시 globally generated이므로, $a,b\geq0$에 대하여 $\mathcal{L}^{\otimes(ae+b(e+1))}$은 $W$ 위에서 globally generated이다. 그런데 $k\geq e^2$인 정수 $k$를 $e$로 나눈 몫을 $s$, 나머지를 $b$라 하면 $s\geq e>b\geq0$이므로 $a=s-b$가 음이 아니고 $ae+b(e+1)=se+b=k$이니, $W$ 위에서는 $k\geq e^2$인 모든 $k$에 대하여 $\mathcal{L}^{\otimes k}$이 globally generated이다. 이제 $\mathcal{F}$ 자신으로 돌아와 $n_2\geq n_1$을 하나 택하면 $\mathcal{F}\otimes\mathcal{L}^{\otimes n_2}$이 $x$의 어떤 열린근방 $V$ 위에서 globally generated이므로, $n\geq n_2+e^2$인 모든 $n$에 대하여

$$\mathcal{F}\otimes\mathcal{L}^{\otimes n}\cong(\mathcal{F}\otimes\mathcal{L}^{\otimes n_2})\otimes\mathcal{L}^{\otimes(n-n_2)}$$

은 $W\cap V$ 위에서 globally generated이다. 곧 각각의 closed point $x$마다 열린근방 $U_x=W\cap V$와 하한 $n_x=n_2+e^2$을 얻어, $n\geq n_x$이면 $\mathcal{F}\otimes\mathcal{L}^{\otimes n}$이 $U_x$ 위에서 globally generated이도록 할 수 있다.

이제 남은 것은 이 근방들로 $X$를 덮는 것으로, [정리 11](#thm11)의 증명에서 보았듯 $X$가 $\mathbb{K}$ 위에서 finite type이라 각 affine chart의 coordinate ring이 Jacobson ring이므로, $X$의 공집합이 아닌 닫힌집합은 언제나 closed point를 포함한다. 따라서 $U_x$들의 합집합은 여집합이 closed point를 갖지 않는 닫힌집합이라 $X$ 전체이며, $X$가 quasi-compact이므로 유한 개의 $U_{x_1},\ldots, U_{x_r}$만으로도 $X$를 덮는다. 그럼 $n_0=\max_jn_{x_j}$로 두면 $n\geq n_0$마다 $\mathcal{F}\otimes\mathcal{L}^{\otimes n}$은 $X$의 모든 점에서 global section들로 생성되고, $\mathcal{F}$가 임의의 coherent sheaf였으므로 $\mathcal{L}$은 ample이다.
:::

증명에서 눈여겨볼만한 사실은 [정리 12](#thm12)이 조건으로 요구한 것은 $i>0$ 전체의 소멸이지만 2번으로부터 1번을 얻는 과정에서 실제로 쓰인 것은 $H^1$의 소멸뿐이라는 것으로, 이는 quotient sheaf의 section을 global section으로 들어올리는 것을 가로막는 장애물이 long exact sequence의 $H^1$ 항에 놓이기 때문이다.

## Euler characteristic과 Hilbert polynomial

[정리 8](#thm8)에 의하여 projective scheme 위의 coherent sheaf는 유한 개의 유한차원 cohomology만을 가지므로, 그 차원들의 교대합을 취할 수 있다.

::: 정의 13
Field $\mathbb{K}$ 위의 Noetherian projective scheme $X$와 그 위의 coherent sheaf $\mathcal{F}$에 대하여, $\mathcal{F}$의 *Euler characteristic<sub>오일러 지표</sub>*을 다음의 식

$$\rchi(X, \mathcal{F})=\sum_{i\geq 0}(-1)^i\dim_\mathbb{K}H^i(X, \mathcal{F})$$

으로 정의한다.
:::

[정리 8](#thm8)에 의하여 우변은 유한합이고 각 항이 유한하므로 $\rchi(X, \mathcal{F})$는 정수이며, $X$가 문맥에서 분명할 때에는 $\rchi(\mathcal{F})$로 줄여 적는다. 이는 [\[대수다양체\] §사영공간의 코호몰로지, ⁋정의 2](/ko/math/algebraic_varieties/cohomology_of_projective_spaces#def2)를 scheme 위로 옮긴 것이다. 개별 차원 $\dim_\mathbb{K}H^i(X, \mathcal{F})$는 sheaf를 조금만 움직여도 뛸 수 있지만 그 교대합은 훨씬 안정적인데, 그 근원은 다음의 가법성이다.

::: 명제 14
Field $\mathbb{K}$ 위의 Noetherian projective scheme $X$ 위의 coherent sheaf들에 대하여 다음이 성립한다.

1. Short exact sequence $0 \rightarrow \mathcal{F}' \rightarrow \mathcal{F} \rightarrow \mathcal{F}'' \rightarrow 0$에 대하여 $\rchi(\mathcal{F})=\rchi(\mathcal{F}')+\rchi(\mathcal{F}'')$이다.
2. 유한 exact sequence $0 \rightarrow \mathcal{F}_k \rightarrow \cdots \rightarrow \mathcal{F}_1 \rightarrow \mathcal{F}_0 \rightarrow 0$에 대하여 $\sum_{j=0}^k(-1)^j\rchi(\mathcal{F}_j)=0$이다.
:::
::: 증명
먼저 유한차원 벡터공간들의 exact sequence $0 \rightarrow V_0 \rightarrow V_1 \rightarrow \cdots \rightarrow V_t \rightarrow 0$을 보자. $j$번째 선형사상의 rank를 $r_j$라 하면 ($r_{-1}=r_t=0$) exactness가 $\dim V_j=r_{j-1}+r_j$를 주므로, 교대합 $\sum_j(-1)^j\dim V_j$에서 이웃한 항들이 서로 소거되어 $0$이 된다.

1번의 경우 [명제 2](#prop2)가 주는 long exact sequence

$$0 \rightarrow H^0(X, \mathcal{F}') \rightarrow H^0(X, \mathcal{F}) \rightarrow H^0(X, \mathcal{F}'') \rightarrow H^1(X, \mathcal{F}') \rightarrow \cdots$$

는 [정리 8](#thm8)에 의하여 유한차원 벡터공간들로 이루어져 있고 충분히 큰 차수에서 끊기므로 유한하다. 위의 관찰을 적용하면 세 sheaf의 cohomology 차원들의 교대합이 $0$이 되고, 부호를 정리하면 원하는 식이다.

2번의 경우 $j\geq1$에 대하여 $\mathcal{Z}_j=\ker(\mathcal{F}_j \rightarrow \mathcal{F}_{j-1})$로 두고 $\mathcal{Z}_0=\mathcal{F}_0$이라 하자. Coherent sheaf들 사이의 morphism의 kernel은 다시 coherent sheaf이므로 각각의 $\mathcal{Z}_j$은 coherent sheaf이고, exactness에 의하여 $\mathcal{Z}_k=0$이며 각각의 $j\geq1$에 대해 short exact sequence

$$0 \rightarrow \mathcal{Z}_j \rightarrow \mathcal{F}_j \rightarrow \mathcal{Z}_{j-1} \rightarrow 0$$

을 얻는다. 여기에 1번을 적용하여 얻은 $\rchi(\mathcal{F}_j)=\rchi(\mathcal{Z}_j)+\rchi(\mathcal{Z}_{j-1})$을 부호를 번갈아 더하면 중간항이 모두 소거되어 $\sum_{j=1}^k(-1)^j\rchi(\mathcal{F}_j)=-\rchi(\mathcal{Z}_0)=-\rchi(\mathcal{F}_0)$을 얻는다.
:::

특히 coherent sheaf $\mathcal{F}$가 유한 resolution $0 \rightarrow \mathcal{E}_k \rightarrow \cdots \rightarrow \mathcal{E}_0 \rightarrow \mathcal{F} \rightarrow 0$을 가지면 [명제 14](#prop14)의 2번에서 $\rchi(\mathcal{F})=\sum_{j=0}^k(-1)^j\rchi(\mathcal{E}_j)$을 얻는다. 이것이 Euler characteristic을 실제로 계산하는 표준적인 경로이며, 그 출발점은 projective space 위의 line bundle이다.

::: 따름정리 15
Field $\mathbb{K}$ 위의 projective space $\mathbb{P}^n_\mathbb{K}$와 임의의 정수 $d$에 대하여

$$\rchi(\mathbb{P}^n_\mathbb{K}, \mathcal{O}(d))=\binom{n+d}{n}$$

이 성립한다. 여기에서 $\binom{n+d}{n}$은 다항식 $t(t-1)\cdots(t-n+1)/n!$의 $t=n+d$에서의 값으로 읽는다.
:::
::: 증명
[정리 6](#thm6)에서 $A=\mathbb{K}$로 두면 세 경우로 나뉜다. $d\geq0$이면 $H^0$만 남고 그 차원은 $n+1$개의 변수의 degree $d$ monomial의 개수 $\binom{n+d}{n}$이다. $-n\leq d\leq-1$이면 모든 cohomology가 소멸하며, 이 범위에서 $t=n+d$는 $0$과 $n-1$ 사이의 정수이므로 곱 $t(t-1)\cdots(t-n+1)$의 인수 가운데 하나가 $0$이 되어 $\binom{n+d}{n}=0$이다. $d\leq -n-1$이면 $H^n$만 남고 그 차원은 모든 지수가 음인 $d$차 monomial의 개수 $\binom{-d-1}{n}$이므로

$$\rchi(\mathbb{P}^n_\mathbb{K}, \mathcal{O}(d))=(-1)^n\binom{-d-1}{n}=\binom{n+d}{n}$$

이다. 마지막 등식은 $t=n+d$에 대해 $t(t-1)\cdots(t-n+1)=(-1)^n(n-t-1)(n-t-2)\cdots(-t)$인 것에서 얻어진다.
:::

이 값은 $d$에 대한 degree $n$의 다항식이며, [\[대수다양체\] §사영공간의 코호몰로지, ⁋따름정리 3](/ko/math/algebraic_varieties/cohomology_of_projective_spaces#cor3)의 variety 판본과 일치한다. 곧 $\mathcal{O}(d)$를 twist해 나갈 때 cohomology의 교대합은 개별 cohomology가 겪는 세 국면과 무관하게 하나의 다항식을 따라간다. 이것이 일반적인 coherent sheaf에서도 성립한다는 것이 다음 정리이며, 이를 진술하기 위해 coherent sheaf $\mathcal{F}$의 *support*를 $\supp\mathcal{F}=\{x\in X\mid \mathcal{F}_x\neq0\}$으로 정의한다. Affine chart 위에서 이는 대응하는 module의 annihilator ideal의 zero set이므로 닫힌집합이다.

::: 정리 16 (Hilbert)
Field $\mathbb{K}$ 위의 projective space $\mathbb{P}^n_\mathbb{K}$의 closed subscheme $X$와 그 위의 coherent sheaf $\mathcal{F}$에 대하여, 유일한 numerical polynomial $P_\mathcal{F}$가 존재하여 ([\[가환대수학\] §힐베르트-사무엘 함수, ⁋정의 1](/ko/math/commutative_algebra/hilbert-samuel_function#def1)) 모든 정수 $d$에 대해

$$\rchi(\mathcal{F}(d))=P_\mathcal{F}(d)$$

이 성립한다. 뿐만 아니라 $\mathcal{F}\neq0$이면 $P_\mathcal{F}$의 degree는 $\dim\supp\mathcal{F}$와 같고, 충분히 큰 $d$에 대해서는 $P_\mathcal{F}(d)=\dim_\mathbb{K}\Gamma(X, \mathcal{F}(d))$이다.
:::
::: 증명
마지막 주장은 [정리 9](#thm9)에서 곧바로 얻어진다. 충분히 큰 $d$에서 $H^i(X, \mathcal{F}(d))=0$ ($i>0$)이므로 교대합에 $H^0$만 남기 때문이다. 유일성은 서로 다른 두 다항식이 무한히 많은 정수에서 일치할 수 없다는 것에서 따라온다.

먼저 $X=\mathbb{P}^n_\mathbb{K}$인 경우로 환원한다. Closed embedding $\iota:X\hookrightarrow\mathbb{P}^n_\mathbb{K}$에 대하여, [정리 8](#thm8) 직전의 isomorphism $(\ast)$을 [정리 9](#thm9)의 증명에서 본 등식 $\iota_\ast(\mathcal{F}(d))\cong(\iota_\ast\mathcal{F})(d)$과 결합하면 $H^i(X, \mathcal{F}(d))\cong H^i(\mathbb{P}^n, (\iota_\ast\mathcal{F})(d))$이고 $\supp\iota_\ast\mathcal{F}=\iota(\supp\mathcal{F})$이므로, [정리 8](#thm8)의 증명에서 보았듯 coherent인 $\iota_\ast\mathcal{F}$로 $\mathcal{F}$를 바꾸어도 무방하다.

뿐만 아니라, 우리는 field $\mathbb{K}$가 *infinite* field라 가정해도 된다. 정리의 결론이 cohomology의 차원들과 $\supp\mathcal{F}$의 차원만으로 진술되므로, 이를 보이기 위해서는 infinite field로의 extension $\mathbb{K}\hookrightarrow \mathbb{L}$에 대하여 이 두 불변량들이 보존된다는 것을 보이면 된다. 우선 cohomology의 차원의 경우, standard affine cover에 대한 Čech complex는 계수만 바꿔준 $\check C^\bullet(\mathcal{U}, \mathcal{F})\otimes_\mathbb{K}\mathbb{L}$이고 $-\otimes_\mathbb{K}\mathbb{L}$은 exact이므로, [따름정리 4](#cor4)에 의하여 $\dim_\mathbb{L}H^i(\mathbb{P}^n_\mathbb{L}, \mathcal{F}_\mathbb{L}(d))=\dim_\mathbb{K}H^i(\mathbb{P}^n_\mathbb{K}, \mathcal{F}(d))$이다. Support의 차원의 경우, 우리는 우선 support 자체가 field extension과 호환됨을 본다. 각각의 affine chart $\Spec A$ 위에서 $\mathcal{F}$에 대응하는 finitely generated module $M$의 generator $m_1,\ldots, m_r$를 잡으면, $\ann M$은 $a\mapsto(am_1,\ldots, am_r)$로 주어지는 $A \rightarrow M^{\oplus r}$의 kernel이다. ([\[가환대수학\] §기본 개념들, ⁋정의 1](/ko/math/commutative_algebra/basic_notions#def1)) 그런데 $m_k\otimes1$들이 $M\otimes_\mathbb{K}\mathbb{L}$을 생성하고 $-\otimes_\mathbb{K}\mathbb{L}$이 kernel을 보존하므로 $\ann(M\otimes_\mathbb{K}\mathbb{L})=(\ann M)\otimes_\mathbb{K}\mathbb{L}$이고, 따라서 $\supp\mathcal{F}$가 chart마다 $\Spec(A/\ann M)$이면 $\supp\mathcal{F}_\mathbb{L}$은 chart마다 $\Spec\bigl((A/\ann M)\otimes_\mathbb{K}\mathbb{L}\bigr)$로 주어진다. 이제 finitely generated $\mathbb{K}$-algebra의 차원은 field extension에 의해 변하지 않으므로 ([\[가환대수학\] §뇌터 정규화, ⁋명제 5](/ko/math/commutative_algebra/noether_normalization#prop5)) 이 두 불변량이 보존되고 따라서 처음부터 $\mathbb{K}$가 무한체라 두어도 된다.

이제 증명의 전체 구도는 [정리 8](#thm8)과 [정리 9](#thm9)의 증명에서 쓴 dévissage와 같아서, short exact sequence

$$0 \rightarrow \mathcal{F}(-1) \rightarrow \mathcal{F} \rightarrow \mathcal{F}'' \rightarrow 0\tag{$\ast\ast$}$$

를 만들어 원하는 성질을 이를 따라 옮기는 것이다. 여기서 $\mathcal{F}(-1) \rightarrow \mathcal{F}$은 homogeneous coordinate ring $S_\bullet=\mathbb{K}[\x_0,\ldots, \x_n]$의 degree $1$ 원소 $\ell\in S_1$을 곱하는 morphism이고, $\mathcal{F}''$은 그 cokernel으로, 직관적으로 이는 $\mathcal{F}$를 hyperplane $V_+(\ell)$ 위로 제한한 것, 곧 $\mathcal{F}$의 hyperplane section이다. 다른 점은 앞선 정리들의 증명이 coherent sheaf를 free sheaf로 덮은 후 long exact sequence 계산으로 귀납을 돌렸다면, 우리는 [명제 14](#prop14)의 additivity를 사용하여 support의 차원 $r=\dim\supp \mathcal{F}$에 대한 귀납을 돌린다는 것이다. 

우선 이러한 short exact sequence가 존재하려면 $\ell$을 임의로 잡을 수는 없다. 문제가 되는 것은 $\times \ell$의 단사성으로, 만일 $\ell$이 $\mathcal{F}$의 어떤 associated prime, 곧 $0$이 아닌 section $m$의 annihilator로 나타나는 prime $\mathfrak{p}=\ann(m)$에 속한다면 $\ell m=0$이 되어 단사성이 깨지기 때문이다. 거꾸로 zerodivisor 전체가 associated prime들의 합집합이므로 단사성을 막는 것은 이들뿐이다. 기하적으로 점 $\mathfrak{p}$가 hyperplane $V_+(\ell)$ 위에 놓이는 것이 곧 $\ell\in\mathfrak{p}$이므로, 이 조건은 $V_+(\ell)$이 $\mathcal{F}$의 associated prime들이 주는 유한 개의 점 중 어느 것도 지나지 않는다는 말과 같다. 이 점들 가운데에는 $\supp\mathcal{F}$의 각 irreducible component의 generic point가 들어 있으므로 ([§스킴의 대수구조, §§동반소아이디얼](/ko/math/scheme_theory/algebra_of_schemes#동반소아이디얼)), 그러한 hyperplane은 $\supp\mathcal{F}$의 어떤 component도 통째로 포함하지 않고 각각과 진부분집합에서만 만난다. 따라서 $\ell$은 $\mathcal{F}$의 associated prime들이 주는 점을 모두 피해야 하며, 우리의 아이디어는 associated prime들은 유한히 많지만 $\mathbb{K}$가 infinite이도록 두었으므로 이를 사용하는 것이다.  

$\mathcal{F}=0$이면 모든 cohomology가 소멸하므로 정리 자체가 자명하다. 따라서 $\mathcal{F}\neq0$이라 하자. 각각의 chart $D_+(\x_j)=\Spec S_{(\x_j)}$ 위에서 $\mathcal{F}$는 finitely generated module $M_j$에 대응하며 ([§준연접층, ⁋정리 10](/ko/math/scheme_theory/quasicoherent_sheaves#thm10), [§준연접층, ⁋정의 11](/ko/math/scheme_theory/quasicoherent_sheaves#def11)), 각각의 $\Ass M_j$는 유한집합이다. ([\[가환대수학\] §동반소아이디얼, ⁋정리 7](/ko/math/commutative_algebra/associated_primes#thm7)의 1번) 이들에 대응하는 $\mathbb{P}^n$의 점을 모두 모으면 유한 개이고, 각각은 irrelevant ideal을 포함하지 않는 homogeneous prime ideal $\mathfrak{p}_1,\ldots, \mathfrak{p}_t\subseteq S$를 준다. $\mathfrak{p}_k$가 homogeneous이므로, 만일 $S_1\subseteq\mathfrak{p}_k$이면 $\mathfrak{p}_k$가 irrelevant ideal을 포함하게 되고, 따라서 각각의 $\mathfrak{p}_k\cap S_1$은 $S_1$의 진부분공간이다. 한편 $\mathbb{K}$가 무한체이므로 벡터공간 $S_1$은 유한 개의 진부분공간의 합집합이 될 수 없고, 따라서 어떠한 $\mathfrak{p}_k$에도 속하지 않는 $\ell\in S_1$이 존재한다.

이렇게 택한 $\ell$이 피하는 것은 $S$의 homogeneous prime $\mathfrak{p}_k$들인 반면, short exact sequence 단사성을 막는 것은 각 chart 위에서의 associated prime들이므로, 우리는 이 조건을 [§사영공간과 Proj 구성, ⁋보조정리 8](/ko/math/scheme_theory/projective_schemes#lem8)의 대응을 따라 $S_{(\x_j)}$ 쪽으로 옮겨야 한다. $\ell$을 곱하는 morphism $\mathcal{F}(-1) \rightarrow \mathcal{F}$을 chart $D_+(\x_j)$ 위에서 보면, 이는 $M_j$의 각 원소에 $\ell/\x_j$을 곱하는 것으로 작용한다. 우리의 주장은 이 원소 $\ell/\x_j$가 $M_j$의 zerodivisor가 아니고 따라서 단사성이 보장된다는 것으로, 이를 위해서는 $\ell/\x_j$가 $M_j$의 어떠한 associated prime에도 속하지 않는다는 것을 보여야 한다. ([\[가환대수학\] §동반소아이디얼, ⁋정리 7](/ko/math/commutative_algebra/associated_primes#thm7)의 2번) 실제로 $M_j$의 각 associated prime은 $D_+(\x_j)$에 놓인 어떤 $\mathfrak{p}_k$가 이 대응으로 주는 prime $\mathfrak{p}_kS_{\x_j}\cap S_{(\x_j)}$인데, 만일 $\ell/\x_j$가 이러한 prime에 속한다면 $\ell=\x_j\cdot(\ell/\x_j)$이 $\mathfrak{p}_kS_{\x_j}\cap S=\mathfrak{p}_k$에 속하게 되어 $\ell$의 선택에 모순이다. 따라서 이 morphism은 injective이다. 그 cokernel을 $\mathcal{F}''$이라 하면 각각의 $d$에 대해 short exact sequence

$$0 \rightarrow \mathcal{F}(d-1) \rightarrow \mathcal{F}(d) \rightarrow \mathcal{F}''(d) \rightarrow 0$$

을 얻고, $\supp\mathcal{F}''=\supp\mathcal{F}\cap V_+(\ell)$이다. 실제로 점 $\mathfrak{p}$에서의 stalk를 보면 $\mathcal{F}''_\mathfrak{p}=\mathcal{F}_\mathfrak{p}/\ell\mathcal{F}_\mathfrak{p}$인데, $\ell\notin\mathfrak{p}$이면 $\ell$이 local ring의 unit이라 이것이 $0$이고, $\ell\in\mathfrak{p}$이면서 $\mathcal{F}_\mathfrak{p}\neq0$이면 [\[가환대수학\] §정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)의 1번에 의하여 $\mathcal{F}_\mathfrak{p}/\ell\mathcal{F}_\mathfrak{p}\neq0$이기 때문이다.

이제 예고한대로 나머지는 이렇게 얻어진 short exact sequence ($\ast\ast$)를 사용하여, 차원에 대한 귀납법을 적용하는 것이다. 이를 위해서는 우선 hyperplane section이 실제로 support의 차원을 정확히 하나 떨어뜨린다는 것을 보여야 한다. Minimal prime은 언제나 associated prime이므로 $\ell$은 $\supp\mathcal{F}$의 어떠한 irreducible component 위에서도 항등적으로 소멸하지 않는다. 각각의 component $Z$에 reduced 구조를 주고 그 교집합의 차원을 재어 보면, $Z$가 irreducible이고 $\mathbb{K}$ 위에서 finite type이므로 $Z$와 만나는 각각의 chart에 대하여 $Z\cap D_+(\x_j)=\Spec A_j$의 $A_j$는 finitely generated $\mathbb{K}$-algebra인 integral domain이고 그 fraction field는 chart와 무관하게 $Z$의 function field이다. 즉, [§차원, ⁋명제 10](/ko/math/scheme_theory/dimension#prop10)에 의하여 $\dim A_j$는 모든 chart에서 같으며, [§차원, ⁋명제 2](/ko/math/scheme_theory/dimension#prop2)에 의하여 이 공통값이 $\dim Z$이다. $\dim Z=0$인 경우 $Z$는 한 점이고 그 위에서 $\ell$이 소멸하지 않으므로 $Z\cap V_+(\ell)=\emptyset$이며, 거꾸로 $Z\cap V_+(\ell)= \emptyset$이라면 반드시 $\dim Z=0$이어야 한다. 이는 $Z$는 affine scheme $D_+(\ell)$의 closed subscheme으로서 affine인데, 그 coordinate ring은 [정리 8](#thm8)에 의하여 유한차원 $\mathbb{K}$-벡터공간이자 $Z$의 integrality에 의해 integral domain이므로 [\[체론\] §대수적 확장, ⁋명제 3](/ko/math/field_theory/algebraic_extensions#prop3)에 의하여 field이기 때문이다. 따라서 만일 $\dim Z\geq 1$이라면 $Z\cap V_+(\ell)$가 공집합이 아니고, 따라서 이 집합의 한 점을 포함하는 chart $D_+(\x_j)$를 택하면 $\ell/\x_j\in A_j$는 $0$이 아니고 그 점에서 소멸하므로 unit도 아니어서, [§차원, ⁋명제 12](/ko/math/scheme_theory/dimension#prop12)에 의하여 

$$\dim\bigl(Z\cap V_+(\ell)\cap D_+(\x_j)\bigr)=\dim A_j-1=\dim Z-1$$

이다. 이 값은 $Z\cap V_+(\ell)$과 만나는 모든 chart에서 동일하므로 [§차원, ⁋명제 2](/ko/math/scheme_theory/dimension#prop2)에 의하여 $\dim(Z\cap V_+(\ell))=\dim Z-1$이다. 즉, 만일 $r=0$이면 모든 component가 $V_+(\ell)$과 만나지 않아 $\mathcal{F}''=0$이고, $r\geq1$이면 차원이 $r$인 component에서 $r-1$이 얻어져 $\dim\supp\mathcal{F}''=r-1$이다.

이제 실제로 귀납법을 돌린다. 우선 $r=0$인 경우를 보자. 이 경우 $\mathcal{F}''=0$이므로 ($\ast\ast$)를 $d$만큼 twist한 short exact sequence는 isomorphism $\mathcal{F}(d-1)\cong\mathcal{F}(d)$를 주고, 따라서 $g(d)=\rchi(\mathcal{F}(d))$로 두면 $g$는 $d$에 무관한 상수이다. 이 상수를 $P$라 하면 $P$는 모든 정수 $d$에서 $\rchi(\mathcal{F}(d))=P(d)$를 만족하는 numerical polynomial이다. 또, [정리 9](#thm9)에 의하여 충분히 큰 $d$에서 $\mathcal{F}(d)$이 globally generated이며 $\mathcal{F}\neq0$이므로 $\Gamma(X, \mathcal{F}(d))\neq0$이고, 곧 마지막 주장에 의하여 $P>0$이므로 $\deg P=0=r$이다.

이제 $r\geq1$이라 하고, support의 차원이 $r-1$인 경우에 대하여 정리가 성립한다고 가정하자. 위에서 본 대로 $\dim\supp\mathcal{F}''=r-1$이고 특히 $\mathcal{F}''\neq0$이므로, 귀납적 가정에 의하여 $\rchi(\mathcal{F}''(d))$는 모든 $d$에서 어떤 numerical polynomial $Q$와 일치하며 $\deg Q=r-1$이다. [명제 14](#prop14)의 1번에 의하여 모든 정수 $d$에 대해 $g(d)-g(d-1)=Q(d)$이므로 $g(d+1)-g(d)=Q(d+1)$은 numerical polynomial이고, 그럼 [\[가환대수학\] §힐베르트-사무엘 함수, ⁋보조정리 2](/ko/math/commutative_algebra/hilbert-samuel_function#lem2)의 둘째 결과에 의하여 충분히 큰 $d$에서 $g$와 일치하는 numerical polynomial $P$가 존재한다. 이때 $\deg Q=r-1\geq0$에서 $Q\neq0$이므로 $\deg P=\deg Q+1=r$이다. 충분히 큰 $d$에서는 $P(d+1)-P(d)=g(d+1)-g(d)=Q(d+1)$이므로 이 등식은 다항식으로서도 성립하고, 따라서 $d$를 하나씩 내리며

$$g(d)=g(d+1)-Q(d+1)=P(d+1)-Q(d+1)=P(d)$$

를 얻어 $g$와 $P$는 모든 정수에서 일치한다.
:::

이 다항식 $P_\mathcal{F}$를 $\mathcal{F}$의 *Hilbert polynomial<sub>힐베르트 다항식</sub>*이라 부른다. [따름정리 15](#cor15)는 $\mathcal{F}=\mathcal{O}_{\mathbb{P}^n}$인 경우로서 $P_{\mathcal{O}_{\mathbb{P}^n}}(t)=\binom{n+t}{n}$이고 그 degree는 $\dim\mathbb{P}^n=n$이다. [정리 16](#thm16)의 마지막 주장은 이 다항식이 충분히 큰 degree에서는 $\mathcal{F}(d)$의 global section이 이루는 공간의 차원을 재고 있음을 말해주며, 이것이 고전적으로 homogeneous coordinate ring의 Hilbert function을 통해 Hilbert polynomial을 도입하던 관점과 이어지는 지점이다. ([\[가환대수학\] §힐베르트-사무엘 함수, ⁋정의 4](/ko/math/commutative_algebra/hilbert-samuel_function#def4)) 특히 $\mathcal{F}=\mathcal{O}_X$인 경우 이 다항식은 $X$ 자신의 불변량이 된다.

::: 정의 17
Field $\mathbb{K}$ 위의 projective space $\mathbb{P}^n_\mathbb{K}$의 공집합이 아닌 $r$차원 closed subscheme $X$에 대하여, Hilbert polynomial $P_{\mathcal{O}_X}$의 최고차항 계수를 $a_r$이라 하자. 그럼 $X$의 *degree<sub>차수</sub>*를

$$\deg X=r!\cdot a_r$$

로 정의하고, $X$의 *arithmetic genus<sub>산술종수</sub>*를 $p_a(X)=(-1)^r\bigl(P_{\mathcal{O}_X}(0)-1\bigr)$로 정의한다.
:::

여기서 $\supp\mathcal{O}_X=X$이므로 [정리 16](#thm16)에 의하여 $P_{\mathcal{O}_X}$는 $r$차식이고, 충분히 큰 $d$에서 $P_{\mathcal{O}_X}(d)=\dim_\mathbb{K}\Gamma(X, \mathcal{O}_X(d))>0$이므로 $a_r$은 양수이다. 또 numerical polynomial을 이항계수들의 정수계수 결합으로 적으면 ([\[가환대수학\] §힐베르트-사무엘 함수, ⁋보조정리 2](/ko/math/commutative_algebra/hilbert-samuel_function#lem2)의 첫째 결과) 최고차항 계수에 $r!$을 곱한 값이 정수임을 알 수 있다. 즉, $\deg X$는 양의 정수이다. 한편 $P_{\mathcal{O}_X}(0)=\rchi(\mathcal{O}_X)$이므로 arithmetic genus는 structure sheaf의 Euler characteristic을 다시 적은 것이며, 부호 $(-1)^r$은 곡선의 경우 우리가 이미 알고 있는 정의 $p_a=1-\rchi(\mathcal{O}_X)$가 되도록 맞춘 것이다.

가장 단순한 예시는 projective space 자신이다. [따름정리 15](#cor15)에서 $P_{\mathcal{O}_{\mathbb{P}^n}}(t)=\binom{n+t}{n}$이므로 최고차항 계수는 $1/n!$이고 따라서 $\deg\mathbb{P}^n_\mathbb{K}=1$이며, $P_{\mathcal{O}_{\mathbb{P}^n}}(0)=1$에서 $p_a(\mathbb{P}^n_\mathbb{K})=0$이다. 이보다 덜 자명한 예시로 positive degree $e$의 nonzero homogeneous polynomial $f$가 정의하는 hypersurface $X=V_+(f)\subseteq\mathbb{P}^n_\mathbb{K}$를 보자. $f$는 많아야 하나의 $j$에 대해서만 $\x_j^e$의 상수배일 수 있으므로, $n\geq1$이라면 $f$가 $\x_j^e$의 상수배가 아닌 chart $D_+(\x_j)$가 반드시 존재한다. 이 chart 위에서 $X$는 dehomogenization $f/\x_j^e$의 zero set인데, 이 원소가 $0$도 unit도 아니므로 그 zero set은 공집합이 아니고, 곧 $X$는 공집합이 아닌 closed subscheme이어서 [정의 17](#def17)을 적용할 수 있다. 이를 따라가보면 $\mathbb{K}[\x_0,\ldots, \x_n]$가 integral domain이므로 곱하기 $f$는 각 chart 위에서 injective이고, 따라서 short exact sequence

$$0 \rightarrow \mathcal{O}_{\mathbb{P}^n}(-e)\overset{\times f}{\longrightarrow}\mathcal{O}_{\mathbb{P}^n} \rightarrow \mathcal{O}_X \rightarrow 0$$

가 존재하며 이를 $\mathcal{O}(d)$로 twist한 뒤 [명제 14](#prop14)의 1번과 [따름정리 15](#cor15)를 적용하면

$$P_{\mathcal{O}_X}(t)=\binom{n+t}{n}-\binom{n+t-e}{n}$$

이다. 우변에서 $t^n$의 항은 소거되고 $t^{n-1}$의 계수는 $e/(n-1)!$이 남으므로, $\dim X=n-1$과 함께 $\deg X=e$를 얻는다. 즉, $\mathbb{P}^n$의 hypersurface의 degree는 이를 정의하는 다항식의 차수라는 고전적인 사실이 Hilbert polynomial의 언어로 다시 얻어진다.

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundations of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).
