---
title: "스킴의 층 코호몰로지"
description: '대수다양체 위에서 도입한 층 코호몰로지를 임의의 스킴 위의 준연접층으로 끌어올린다. Abelian sheaf 범주의 유도 함자로서의 정의와 affine 덮개에 대한 Čech 코호몰로지를 다루고, affine scheme 위 준연접층의 소멸 정리로부터 separated scheme 위에서 두 코호몰로지가 일치함을 보인다. 사영공간 위 $$\mathcal{O}(d)$$의 코호몰로지를 재계산하고, Noetherian projective scheme 위 연접층의 유한성과 Serre vanishing을 증명한다.'
excerpt: "Cohomology of quasi-coherent sheaves, Serre's affine vanishing, and Serre vanishing on projective schemes"

categories: [Math / Scheme Theory]
permalink: /ko/math/scheme_theory/sheaf_cohomology_of_schemes
sidebar: 
    nav: "scheme_theory-ko"

date: 2026-06-21
weight: 18

published: false
---

우리는 [\[대수다양체\] §층 코호몰로지](/ko/math/algebraic_varieties/sheaf_cohomology)에서 quasi-projective variety 위의 quasi-coherent sheaf에 대한 층 코호몰로지를 유도 함자로 정의하고, Čech 코호몰로지와의 비교 및 Leray 정리를 통해 이를 계산하는 방법을 살펴보았다. 그곳의 논증은 사실상 quasi-projective라는 가정을 거의 사용하지 않으며, separated 조건과 affine 위의 소멸 정리만으로 작동한다. 이제 우리는 [§준연접층](/ko/math/scheme_theory/quasicoherent_sheaves)에서 임의의 scheme 위로 끌어올린 준연접층의 언어를 갖추었으므로, 층 코호몰로지 또한 임의의 scheme 위로 옮겨 다시 정립할 수 있다. 이 글에서 우리는 그 정의를 scheme 수준에서 다시 적고, **Serre의 아핀 소멸 정리**가 affine scheme 위에서 준연접층의 higher cohomology를 죽인다는 것을 증명하며, 이를 토대로 사영공간 위의 line bundle $$\mathcal{O}(d)$$의 코호몰로지를 재계산한다. 마지막으로 Noetherian projective scheme 위에서 연접층의 코호몰로지가 유한차원이라는 것과, 충분히 twist하면 higher cohomology가 소멸한다는 Serre vanishing을 다룬다.

## 유도 함자로서의 코호몰로지

Scheme $$X$$ 위에서도 abelian group들의 sheaf 범주 $$\Sh(X)$$는 abelian category이며 enough injective를 가진다. 따라서 [\[대수다양체\] §층 코호몰로지](/ko/math/algebraic_varieties/sheaf_cohomology)에서와 동일한 방식으로 global section functor의 유도 함자를 정의할 수 있다. 우리의 주된 관심은 항상 준연접층이지만, injective resolution은 $$\Sh(X)$$ 안에서 잡는다는 점에 유의한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Scheme $$X$$ 위의 $$\mathcal{O}_X$$-가군층 $$\mathcal{F}$$에 대하여, global section functor $$\Gamma(X, -):\Sh(X) \rightarrow \Ab$$의 right derived functor ([\[호몰로지 대수학\] §유도함자, ⁋정의 9](/ko/math/homological_algebra/derived_functors#def9))를 취하여 $$i$$번째 *sheaf cohomology<sub>층 코호몰로지</sub>*를

$$H^i(X, \mathcal{F})=R^i\Gamma(X, -)(\mathcal{F})=\frac{\ker\bigl(\Gamma(X, \mathcal{I}^i) \rightarrow \Gamma(X, \mathcal{I}^{i+1})\bigr)}{\im\bigl(\Gamma(X, \mathcal{I}^{i-1}) \rightarrow \Gamma(X, \mathcal{I}^i)\bigr)}$$

으로 정의한다. 여기에서 $$0 \rightarrow \mathcal{F} \rightarrow \mathcal{I}^\bullet$$은 $$\Sh(X)$$에서의 injective resolution이다.

</div>

이 정의는 [\[대수다양체\] §층 코호몰로지, ⁋정의 1](/ko/math/algebraic_varieties/sheaf_cohomology#def1)을 임의의 scheme 위로 옮긴 것에 불과하며, $$\mathcal{I}^\bullet$$의 선택에 무관함을 비롯한 형식적 성질은 모두 homological algebra의 표준 논증으로부터 따라온다. 특히 $$H^0(X, \mathcal{F})=\Gamma(X, \mathcal{F})$$이고, sheaf의 short exact sequence는 long exact sequence를 유도한다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> $$\mathcal{O}_X$$-가군층의 short exact sequence

$$0 \rightarrow \mathcal{F}' \rightarrow \mathcal{F} \rightarrow \mathcal{F}'' \rightarrow 0$$

에 대하여, long exact sequence

$$0 \rightarrow H^0(X, \mathcal{F}') \rightarrow H^0(X, \mathcal{F}) \rightarrow H^0(X, \mathcal{F}'') \xrightarrow{\delta} H^1(X, \mathcal{F}') \rightarrow H^1(X, \mathcal{F}) \rightarrow \cdots$$

이 존재한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\Gamma(X, -)$$는 left exact functor이고 $$\Sh(X)$$는 enough injective를 가지므로, right derived functor가 정의하는 $$\delta$$-functor의 long exact sequence가 그대로 성립한다. ([\[호몰로지 대수학\] §유도함자, ⁋명제 8](/ko/math/homological_algebra/derived_functors#prop8))

</details>

[\[대수다양체\] §층 코호몰로지](/ko/math/algebraic_varieties/sheaf_cohomology)에서 도입한 Čech 코호몰로지의 정의 또한 그대로 옮겨진다. Scheme $$X$$의 open cover $$\mathcal{U}=\{U_i\}_{i\in I}$$와 sheaf $$\mathcal{F}$$에 대하여, Čech complex $$\check C^\bullet(\mathcal{U}, \mathcal{F})$$와 그 코호몰로지 $$\check H^p(\mathcal{U}, \mathcal{F})$$는 ([\[대수다양체\] §층 코호몰로지, ⁋정의 3](/ko/math/algebraic_varieties/sheaf_cohomology#def3), [\[대수다양체\] §층 코호몰로지, ⁋정의 4](/ko/math/algebraic_varieties/sheaf_cohomology#def4)) 위상공간 수준의 정의이므로 scheme 위에서도 곧바로 의미를 가진다. 우리의 목표는 좋은 덮개에 대하여 Čech 코호몰로지가 [정의 1](#def1)의 유도 함자 코호몰로지와 일치함을 보이는 것이며, 그 핵심에는 affine scheme 위의 소멸 정리가 있다.

## Serre의 아핀 소멸 정리

[\[대수다양체\] §층 코호몰로지, ⁋명제 12](/ko/math/algebraic_varieties/sheaf_cohomology#prop12)는 affine variety 위에서 quasi-coherent sheaf의 higher cohomology가 소멸한다는 것이었다. 이를 임의의 affine scheme $$\Spec A$$ 위로 끌어올린 것이 다음의 Serre 소멸 정리이며, scheme 코호몰로지 이론 전체의 토대가 된다.

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3 (Serre의 아핀 소멸)**</ins> Affine scheme $$X=\Spec A$$와 그 위의 준연접층 $$\mathcal{F}=\widetilde M$$에 대하여,

$$H^i(X, \mathcal{F})=0 \qquad (i>0)$$

이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[§준연접층, ⁋정리 9](/ko/math/scheme_theory/quasicoherent_sheaves#thm9)에 의하여 $$\QCoh(\Spec A)$$는 $$\Mod(A)$$와 동치이므로, $$\mathcal{F}=\widetilde M$$인 $$A$$-가군 $$M$$이 존재한다. $$\Mod(A)$$는 enough injective를 가지므로 $$M$$의 injective resolution

$$0 \rightarrow M \rightarrow I^0 \rightarrow I^1 \rightarrow \cdots$$

을 잡자. 연관층 functor $$\widetilde{(-)}$$는 exact이므로 ([§준연접층, ⁋명제 6](/ko/math/scheme_theory/quasicoherent_sheaves#prop6)),

$$0 \rightarrow \widetilde M \rightarrow \widetilde{I^0} \rightarrow \widetilde{I^1} \rightarrow \cdots$$

은 $$\Spec A$$ 위의 sheaf의 resolution이다. 우리의 주장은 각각의 $$\widetilde{I^k}$$이 $$\Gamma(\Spec A, -)$$-acyclic이라는 것이며, 이것이 성립하면 [\[대수다양체\] §층 코호몰로지, ⁋명제 17](/ko/math/algebraic_varieties/sheaf_cohomology#prop17)의 acyclic resolution 논증에 의하여

$$H^i(\Spec A, \widetilde M)\cong H^i\bigl(\Gamma(\Spec A, \widetilde{I^\bullet})\bigr)=H^i(I^\bullet)$$

을 얻는다. 그런데 $$I^\bullet$$은 $$M$$의 injective resolution이므로 $$\Gamma(\Spec A, \widetilde{I^k})=I^k$$이고, $$M \rightarrow I^\bullet$$은 quasi-isomorphism이므로 우변의 코호몰로지는 $$i>0$$에서 모두 소멸한다. 따라서 $$H^i(\Spec A, \widetilde M)=0$$ ($$i>0$$)이다.

남은 것은 injective $$A$$-가군 $$I$$의 연관층 $$\widetilde I$$이 acyclic이라는 것이다. 이를 위해 우리는 $$\widetilde I$$이 flasque임을 보이며, flasque sheaf가 $$\Gamma(X, -)$$-acyclic이라는 것은 이미 알고 있다. ([\[대수다양체\] §층 코호몰로지, ⁋명제 16](/ko/math/algebraic_varieties/sheaf_cohomology#prop16)) Flasque임을 보이는 것은 noetherian 가정 아래에서 가장 명료하므로 그 경우를 먼저 다룬다. $$A$$가 noetherian ring이라 하자. 임의의 principal open set $$D(f)\subseteq \Spec A$$에 대하여, restriction map은 [§준연접층, ⁋명제 5](/ko/math/scheme_theory/quasicoherent_sheaves#prop5)에 의하여 localization $$I \rightarrow I_f$$이다. 그런데 noetherian ring 위에서 injective 가군의 localization은 다시 injective이며, 더 일반적으로 임의의 열린집합 $$U=\Spec A\setminus V(\mathfrak{a})$$에 대하여 restriction $$\widetilde I(\Spec A)=I\to\widetilde I(U)$$이 surjective임을 본다. 준연접층의 단면을 local cohomology와 잇는 완전열
$$I\longrightarrow\widetilde I(U)\longrightarrow H^1_{\mathfrak{a}}(I)\longrightarrow 0$$
이 성립하는데, 여기서 $$H^i_{\mathfrak{a}}(M)=\varinjlim_n\Ext^i_A(A/\mathfrak{a}^n,M)$$이다. $$I$$가 injective이므로 모든 $$n$$에서 $$\Ext^1_A(A/\mathfrak{a}^n,I)=0$$이어서 $$H^1_{\mathfrak{a}}(I)=0$$이고, 따라서 위 restriction이 surjective이다. 같은 논증이 임의의 열린집합에 적용되므로 $$\widetilde I$$은 flasque이다 (Hartshorne III.3.4).

$$A$$가 noetherian이 아닌 경우에는, $$\Spec A$$의 임의의 open cover에 대하여 Čech complex $$\check C^\bullet(\mathcal{U}, \widetilde M)$$이 exact하다는 것을 직접 보이는 방식으로 같은 결론에 도달할 수 있다. 핵심은 affine scheme 위에서 준연접층의 단면이 모두 localization으로 주어지므로, principal open set들로 이루어진 cover에 대한 Čech complex가 가군 $$M$$의 분해로 환원되어 $$p>0$$에서 사라진다는 것이다. 어느 경우든 $$\widetilde I$$의 acyclicity가 성립한다.

</details>

[정리 3](#thm3)의 핵심은 affine scheme이 코호몰로지의 관점에서 "단순한" 공간이라는 것이다. 즉 affine 위에서는 준연접층의 정보가 모두 $$H^0$$, 곧 그 global section 가군에 담겨 있으며, higher cohomology는 어떠한 새로운 정보도 주지 않는다. 이는 위상공간이 Čech 코호몰로지의 관점에서 contractible한 것에 대응하는 대수기하학적 현상이다.

이로부터 곧바로 affine 덮개에 대한 Leray 정리를 scheme 수준에서 얻는다. [\[대수다양체\] §층 코호몰로지, ⁋정리 11](/ko/math/algebraic_varieties/sheaf_cohomology#thm11)은 cover $$\mathcal{U}$$의 모든 유한 교집합 위에서 $$\mathcal{F}$$가 acyclic이면 $$\check H^p(\mathcal{U}, \mathcal{F})\cong H^p(X, \mathcal{F})$$임을 주는데, 이는 위상공간 수준의 정리이므로 scheme 위에서도 그대로 적용된다.

<div class="proposition" markdown="1">

<ins id="cor4">**따름정리 4**</ins> Separated scheme $$X$$ ([§값매김환, ⁋정의 3](/ko/math/scheme_theory/valuative_criteria#def3))와 그 위의 준연접층 $$\mathcal{F}$$, 그리고 affine open cover $$\mathcal{U}=\{U_i\}$$에 대하여, 모든 $$p$$에 대해

$$\check H^p(\mathcal{U}, \mathcal{F})\cong H^p(X, \mathcal{F})$$

이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[\[대수다양체\] §층 코호몰로지, ⁋정리 11](/ko/math/algebraic_varieties/sheaf_cohomology#thm11)에 의하여, $$\mathcal{U}$$의 임의의 유한 교집합 $$U_{i_0}\cap\cdots\cap U_{i_p}$$ 위에서 $$\mathcal{F}$$가 acyclic임을 보이면 충분하다. $$X$$가 separated이므로 diagonal morphism $$\Delta:X \rightarrow X\times_{\Spec \mathbb{Z}}X$$이 closed immersion이고, 따라서 임의의 두 affine open subset $$U_i, U_j$$의 교집합 $$U_i\cap U_j$$는 다시 affine이다. 실제로 $$U_i\cap U_j$$는 fiber product $$U_i\times_X U_j$$이며, 이는 affine scheme $$U_i\times_{\Spec \mathbb{Z}}U_j$$의 closed subscheme $$\Delta^{-1}(U_i\times U_j)$$와 동형이므로 affine이다. 같은 논증을 반복하면 유한 교집합 $$U_{i_0}\cap\cdots\cap U_{i_p}$$ 또한 affine scheme이다. 그럼 $$\mathcal{F}$$의 이 위로의 제한은 affine scheme 위의 준연접층이므로 [정리 3](#thm3)에 의하여 acyclic이고, 따라서 [\[대수다양체\] §층 코호몰로지, ⁋정리 11](/ko/math/algebraic_varieties/sheaf_cohomology#thm11)의 전제가 충족된다.

</details>

따라서 separated scheme 위에서는 affine 덮개 하나를 잡아 Čech complex만 계산하면 유도 함자 코호몰로지가 그대로 얻어진다. Affine scheme 사이의 morphism은 항상 separated이고 ([§값매김환, ⁋보조정리 5](/ko/math/scheme_theory/valuative_criteria#lem5)), $$\mathbb{P}^n$$을 비롯한 projective scheme 또한 separated이므로, 우리가 실제로 다루는 대부분의 scheme에서 이 비교가 작동한다.

## 사영공간 위의 line bundle

이제 affine 덮개에 대한 Čech 계산을 사용하여 사영공간 위의 line bundle $$\mathcal{O}(d)$$의 코호몰로지를 scheme 수준에서 다룬다. 우선 $$\mathcal{O}(d)$$를 graded 가군의 언어로 정의한다. 환 $$A$$ 위의 사영공간은 $$\mathbb{P}^n_A=\Proj A[\x_0,\ldots, \x_n]$$이며 ([§사영스킴, ⁋정의 1](/ko/math/scheme_theory/projective_schemes#def1)), 이는 standard affine cover $$\mathcal{U}=\{D_+(\x_i)\}_{i=0}^n$$을 가진다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> $$S=A[\x_0,\ldots, \x_n]$$을 standard grading을 가진 graded ring이라 하고, $$S(d)$$를 $$S(d)_m=S_{d+m}$$으로 grading을 옮긴 graded $$S$$-가군이라 하자. 그럼 standard affine cover $$\mathcal{U}=\{D_+(\x_i)\}$$ 위에서 각각의 $$D_+(\x_i)=\Spec S_{(\x_i)}$$에

$$\mathcal{O}(d)(D_+(\x_i))=\bigl(S(d)_{\x_i}\bigr)_0=\x_i^d\cdot S_{(\x_i)}$$

을 대응시키고, 겹치는 부분 위에서 자연스러운 동일시로 붙여 얻는 $$\mathbb{P}^n_A$$ 위의 invertible sheaf를 *twisting sheaf<sub>꼬임층</sub>* $$\mathcal{O}(d)$$라 부른다.

</div>

여기에서 $$S_{(\x_i)}$$은 $$S_{\x_i}$$의 degree $$0$$ 부분이며, $$\x_i^d\cdot S_{(\x_i)}$$은 $$S_{\x_i}$$ 안에서 degree $$d$$인 원소들의 모임이다. 각 chart 위에서 $$\mathcal{O}(d)\vert_{D_+(\x_i)}$$은 $$\x_i^d$$를 생성원으로 하는 자유 $$S_{(\x_i)}$$-가군이므로 rank $$1$$ free이고, 따라서 $$\mathcal{O}(d)$$는 invertible sheaf이다. ([§준연접층, ⁋정의 15](/ko/math/scheme_theory/quasicoherent_sheaves#def15)) $$d=0$$인 경우 $$\mathcal{O}(0)=\mathcal{O}_{\mathbb{P}^n_A}$$이고, $$\mathcal{O}(d)\otimes\mathcal{O}(e)\cong\mathcal{O}(d+e)$$가 성립하므로 $$\mathcal{O}(d)\cong\mathcal{O}(1)^{\otimes d}$$이다. 이 정의는 [\[대수다양체\] §사영공간의 코호몰로지](/ko/math/algebraic_varieties/cohomology_of_projective_spaces)에서 variety 위의 $$\mathcal{O}(d)$$를 chart별 section으로 기술한 것과 정확히 일치한다.

이제 코호몰로지를 계산한다. $$\mathbb{P}^n_A$$은 separated이므로 [따름정리 4](#cor4)에 의해 standard affine cover에 대한 Čech complex를 계산하면 충분하다. 그 결과는 variety의 경우와 형태가 동일하다.

<div class="proposition" markdown="1">

<ins id="thm6">**정리 6 (Bott)**</ins> 환 $$A$$ 위의 사영공간 $$\mathbb{P}^n_A$$의 line bundle $$\mathcal{O}(d)$$의 코호몰로지는

$$H^q(\mathbb{P}^n_A, \mathcal{O}(d))=\begin{cases}A[\x_0,\ldots, \x_n]_d & q=0,\ d\geq 0 \\ A[\x_0^{-1},\ldots, \x_n^{-1}]_{-d-n-1} & q=n,\ d\leq -n-1 \\ 0 & \text{otherwise}\end{cases}$$

로 주어진다. 특히 $$0<q<n$$에서는 모든 $$d$$에 대해 소멸한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\mathbb{P}^n_A$$이 separated scheme이므로 [따름정리 4](#cor4)에 의하여 standard affine cover $$\mathcal{U}=\{D_+(\x_i)\}$$에 대한 Čech 코호몰로지가 곧 유도 함자 코호몰로지이다. 그런데 이 Čech complex는 [\[대수다양체\] §사영공간의 코호몰로지, ⁋명제 1](/ko/math/algebraic_varieties/cohomology_of_projective_spaces#prop1)의 증명에 등장하는 것과 글자 그대로 같다. 즉 각 교집합 $$D_+(\x_{i_0}\cdots\x_{i_p})$$ 위에서 $$\mathcal{O}(d)$$의 section은 $$\x_{i_0},\ldots, \x_{i_p}$$만을 분모로 허용하는 $$d$$차 monomial들

$$\x_0^{a_0}\cdots\x_n^{a_n}, \qquad \sum_{j=0}^n a_j=d,\quad a_j\geq 0\ \text{for}\ j\not\in\{i_0,\ldots, i_p\}$$

로 $$A$$ 위에서 생성되며, coboundary map 또한 동일한 교대합 공식으로 주어진다. variety의 경우 계수체 $$\mathbb{K}$$ 위에서 진행한 계산은 사실 어떤 base ring $$A$$ 위에서든 monomial 단위로 동일하게 작동하므로, 그 증명을 $$A$$-계수로 그대로 읽으면 위의 결과를 얻는다. 구체적으로 $$n=1$$에서는 Čech complex $$0 \rightarrow \check C^0 \xrightarrow{\delta} \check C^1 \rightarrow 0$$의 $$\ker\delta$$가 $$d\geq 0$$일 때 $$A[\x_0,\x_1]_d$$이고 $$\coker\delta$$가 $$d\leq -2$$일 때 두 지수가 모두 음수인 $$d$$차 monomial들로 생성됨을 직접 확인하며, 일반적인 $$n$$은 hyperplane $$\{\x_n=0\}$$이 주는 short exact sequence

$$0 \rightarrow \mathcal{O}(d-1)\xrightarrow{\times\x_n}\mathcal{O}(d) \rightarrow \mathcal{O}(d)\vert_{\mathbb{P}^{n-1}_A} \rightarrow 0$$

의 long exact sequence ([명제 2](#prop2))를 사용한 $$n$$에 대한 귀납으로 처리한다. 중간 차원에서의 소멸과 top 차원에서의 $$\coker$$ 계산이 모두 variety의 경우와 일치한다.

마지막으로 $$q=n$$, $$d\leq -n-1$$에서 얻어지는 공간이 표기 $$A[\x_0^{-1},\ldots, \x_n^{-1}]_{-d-n-1}$$로 적히는 이유는 [\[대수다양체\] §사영공간의 코호몰로지, ⁋명제 1](/ko/math/algebraic_varieties/cohomology_of_projective_spaces#prop1) 직후의 설명과 동일하다. 즉 모든 지수가 $$-1$$ 이하인 $$d$$차 monomial들을 $$\y_j=\x_j^{-1}$$로 치환하면 $$\lvert d\rvert-(n+1)=-d-n-1$$차의 "음의 차수" monomial 공간이 된다.

</details>

[정리 6](#thm6)에서 $$d\geq 0$$일 때 $$H^0(\mathbb{P}^n_A, \mathcal{O}(d))=A[\x_0,\ldots, \x_n]_d$$이 degree $$d$$ 동차다항식들의 free $$A$$-가군이라는 것은 $$\mathcal{O}(d)$$의 global section이 곧 $$S_d$$임을 다시 확인해 준다. 또 양 끝 차원 $$H^0$$와 $$H^n$$ 사이에는 Serre duality

$$H^n(\mathbb{P}^n_A, \mathcal{O}(d))\cong H^0(\mathbb{P}^n_A, \mathcal{O}(-d-n-1))^\vee$$

의 그림자가 보인다. 실제로 $$A=\mathbb{K}$$가 field일 때 $$H^n(\mathbb{P}^n, \mathcal{O}(d))$$의 차원은 $$\dim H^0(\mathbb{P}^n, \mathcal{O}(-d-n-1))$$과 같으며, 이는 canonical bundle이 $$\mathcal{O}(-n-1)$$이라는 사실의 반영이다. 한편 모든 중간 코호몰로지 $$H^q$$ ($$0<q<n$$)이 소멸한다는 것은 사영공간이 코호몰로지의 관점에서 매우 단순한 공간임을 보여주며, 이는 다음 절에서 일반적인 연접층의 코호몰로지를 통제하는 출발점이 된다.

## Noetherian projective scheme 위의 연접층

이제 임의의 Noetherian projective scheme $$X$$와 그 위의 연접층 $$\mathcal{F}$$ ([§준연접층, ⁋정의 11](/ko/math/scheme_theory/quasicoherent_sheaves#def11))에 대하여, 코호몰로지의 두 가지 근본적 성질을 다룬다. 하나는 각 $$H^i(X, \mathcal{F})$$이 유한차원이라는 것이고, 다른 하나는 충분히 twist하면 higher cohomology가 소멸한다는 Serre vanishing이다. Projective scheme $$X$$는 어떤 사영공간 $$\mathbb{P}^n_{\mathbb{K}}$$의 closed subscheme이며, 그 위에 $$\mathcal{O}_X(1)=\mathcal{O}_{\mathbb{P}^n}(1)\vert_X$$을 twisting을 위한 ample line bundle로 사용한다. 연접층 $$\mathcal{F}$$에 대해 $$\mathcal{F}(d)=\mathcal{F}\otimes_{\mathcal{O}_X}\mathcal{O}_X(d)$$로 적는다.

먼저 closed immersion을 따라 코호몰로지가 보존된다는 관찰이 핵심이다. Closed immersion $$\iota:X\hookrightarrow\mathbb{P}^n_{\mathbb{K}}$$은 affine 사상이므로, pushforward $$\iota_\ast$$가 affine 위에서 정확하고 higher direct image를 만들지 않아 $$H^i(X, \mathcal{F})\cong H^i(\mathbb{P}^n, \iota_\ast\mathcal{F})$$이 성립한다. 따라서 두 성질 모두 $$X=\mathbb{P}^n_{\mathbb{K}}$$인 경우로 환원된다.

<div class="proposition" markdown="1">

<ins id="thm7">**정리 7**</ins> Field $$\mathbb{K}$$ 위의 Noetherian projective scheme $$X$$와 그 위의 연접층 $$\mathcal{F}$$에 대하여, 각 $$H^i(X, \mathcal{F})$$은 유한차원 $$\mathbb{K}$$-벡터공간이며, 충분히 큰 $$i$$에 대해서는 $$0$$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

위에서 관찰하였듯 closed immersion $$\iota:X\hookrightarrow\mathbb{P}^n_{\mathbb{K}}$$을 통해 $$H^i(X, \mathcal{F})\cong H^i(\mathbb{P}^n, \iota_\ast\mathcal{F})$$이고, $$\iota_\ast\mathcal{F}$$은 $$\mathbb{P}^n$$ 위의 연접층이므로 ([§준연접층, ⁋정리 19](/ko/math/scheme_theory/quasicoherent_sheaves#thm19)에 의해 준연접이고 finite type 또한 보존된다) $$X=\mathbb{P}^n_{\mathbb{K}}$$이라 가정해도 된다.

이제 $$\mathbb{P}^n$$ 위의 연접층 $$\mathcal{F}$$에 대하여 cohomological dimension $$n$$, 즉 $$i>n$$에서 $$H^i=0$$임을 먼저 본다. $$\mathbb{P}^n$$은 $$n+1$$개의 affine 열린집합 $$D_+(\x_i)$$로 덮이므로, 이 cover에 대한 Čech complex $$\check C^\bullet$$은 $$p>n$$에서 $$\check C^p=0$$이다. ([따름정리 4](#cor4)) 따라서 $$H^i(\mathbb{P}^n, \mathcal{F})=\check H^i=0$$ ($$i>n$$)이다.

유한차원성은 $$i$$에 대한 내림차순 귀납으로 보인다. $$i>n$$인 경우는 위에서 $$0$$이므로 자명하다. 임의의 연접층 $$\mathcal{F}$$에 대하여, 적당한 $$d\gg 0$$에 대해 $$\mathcal{F}(d)$$이 globally generated이므로 ([\[대수다양체\] §사영공간의 코호몰로지, ⁋정의 6](/ko/math/algebraic_varieties/cohomology_of_projective_spaces#def6) 이후 논증) 유한 개의 global section이 surjection

$$\mathcal{O}_{\mathbb{P}^n}^{\oplus r} \twoheadrightarrow \mathcal{F}(d)$$

을 주고, 이를 $$\mathcal{O}(-d)$$로 twist하면 $$\mathcal{O}(-d)^{\oplus r}\twoheadrightarrow\mathcal{F}$$을 얻는다. 그 kernel $$\mathcal{G}$$ 또한 연접층이므로 ($$\mathbb{P}^n$$이 Noetherian이라 kernel이 finite type을 유지한다) short exact sequence

$$0 \rightarrow \mathcal{G} \rightarrow \mathcal{O}(-d)^{\oplus r} \rightarrow \mathcal{F} \rightarrow 0$$

의 long exact sequence ([명제 2](#prop2))에서

$$H^i(\mathbb{P}^n, \mathcal{O}(-d)^{\oplus r}) \rightarrow H^i(\mathbb{P}^n, \mathcal{F}) \rightarrow H^{i+1}(\mathbb{P}^n, \mathcal{G})$$

을 본다. 좌변은 [정리 6](#thm6)에 의하여 유한차원이고, 우변은 귀납 가정에 의하여 유한차원이므로 ($$i+1$$에서의 유한차원성), 가운데 항 $$H^i(\mathbb{P}^n, \mathcal{F})$$ 또한 유한차원이다. 이로써 모든 $$i$$에 대한 유한차원성을 얻는다.

</details>

[정리 7](#thm7)은 projective scheme 위의 연접층이 좋은 유한성을 가짐을 보장한다. 이는 affine 위의 finitely generated 가군에 대한 유한성이 코호몰로지 수준에서 사영적 상황으로 옮겨진 것이며, Euler characteristic ([\[대수다양체\] §사영공간의 코호몰로지, ⁋정의 2](/ko/math/algebraic_varieties/cohomology_of_projective_spaces#def2))과 같은 불변량이 잘 정의되는 근거가 된다. 위 증명의 귀납에 사용한 globally generated 성질과 twist 후의 소멸은 다음 Serre vanishing에서 정량적으로 다시 등장한다.

<div class="proposition" markdown="1">

<ins id="thm8">**정리 8 (Serre Vanishing)**</ins> Field $$\mathbb{K}$$ 위의 Noetherian projective scheme $$X$$와 ample line bundle $$\mathcal{O}_X(1)$$, 그리고 연접층 $$\mathcal{F}$$에 대하여, 충분히 큰 $$d\gg 0$$에 대해

$$H^i(X, \mathcal{F}(d))=0 \qquad (i>0)$$

이 성립한다. 더욱이 이러한 $$d$$에 대해 $$\mathcal{F}(d)$$은 globally generated이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[정리 7](#thm7)에서와 같이 closed immersion $$\iota:X\hookrightarrow\mathbb{P}^n_{\mathbb{K}}$$을 통해 $$X=\mathbb{P}^n_{\mathbb{K}}$$이고 $$\mathcal{O}_X(1)=\mathcal{O}(1)$$인 경우로 환원한다. 이 환원이 정당한 것은 $$\iota$$가 closed immersion이라 $$\iota_\ast(\mathcal{F}(d))\cong(\iota_\ast\mathcal{F})(d)$$이고 ($$\mathcal{O}_X(1)=\iota^\ast\mathcal{O}(1)$$이므로 projection formula로부터), 코호몰로지가 $$\iota_\ast$$ 아래에서 보존되기 때문이다.

먼저 $$\mathcal{F}(d)$$이 $$d\gg0$$에서 globally generated임을 본다. $$S=\mathbb{K}[\x_0,\ldots, \x_n]$$로 두고 graded $$S$$-가군 $$\Gamma_\ast(\mathcal{F})=\bigoplus_{m\in\mathbb{Z}}\Gamma(\mathbb{P}^n, \mathcal{F}(m))$$을 생각하면, 각 표준 affine $$D_+(\x_j)$$ 위에서 $$\Gamma(D_+(\x_j), \mathcal{F})$$은 degree $$0$$ localization $$\Gamma_\ast(\mathcal{F})_{(\x_j)}$$이고 이는 $$S_{(\x_j)}$$ 위의 finitely generated 가군이다. 각 generator를 $$m_k/\x_j^{e_k}$$ 꼴로 적고 $$d_0=\max_{j,k}e_k$$로 두면, $$\x_j^{d_0-e_k}$$를 곱한 $$m_k\cdot\x_j^{d_0-e_k}\in\Gamma(\mathbb{P}^n, \mathcal{F}(d_0))$$들이 $$D_+(\x_j)$$ 위에서 $$\mathcal{F}(d_0)$$의 stalk를 생성한다. $$j$$에 대해 최댓값을 취하면 $$\mathcal{F}(d_0)$$이 globally generated이고, $$d\geq d_0$$이면 $$\mathcal{F}(d)=\mathcal{F}(d_0)\otimes\mathcal{O}(d-d_0)$$ 또한 globally generated이다.

이제 vanishing을 $$i$$에 대한 내림차순 귀납으로 본다. $$i>n$$에서는 [정리 7](#thm7)의 cohomological dimension에 의해 $$H^i=0$$이다. 임의의 $$i\geq1$$에 대하여, globally generated 성질로부터 surjection $$\mathcal{O}^{\oplus r}\twoheadrightarrow\mathcal{F}(d_0)$$을 잡고 kernel $$\mathcal{K}$$를 연접층으로 하여 short exact sequence

$$0 \rightarrow \mathcal{K} \rightarrow \mathcal{O}^{\oplus r} \rightarrow \mathcal{F}(d_0) \rightarrow 0$$

을 얻자. 이를 $$\mathcal{O}(d-d_0)$$로 twist하면

$$0 \rightarrow \mathcal{K}(d-d_0) \rightarrow \mathcal{O}(d-d_0)^{\oplus r} \rightarrow \mathcal{F}(d) \rightarrow 0$$

이고, 그 long exact sequence ([명제 2](#prop2))에서

$$H^i(\mathbb{P}^n, \mathcal{O}(d-d_0)^{\oplus r}) \rightarrow H^i(\mathbb{P}^n, \mathcal{F}(d)) \rightarrow H^{i+1}(\mathbb{P}^n, \mathcal{K}(d-d_0))$$

을 본다. 좌변은 [정리 6](#thm6)에 의하여 $$d-d_0\gg0$$이고 $$i>0$$이면 $$0$$이다. 우변은 귀납 가정을 $$\mathcal{K}$$에 적용한 것으로, $$i+1$$에서의 vanishing이 충분히 큰 twist에 대해 성립한다. 따라서 충분히 큰 $$d$$에 대해 가운데 항 $$H^i(\mathbb{P}^n, \mathcal{F}(d))$$이 양쪽에서 끼여 소멸한다. $$i$$가 $$1$$부터 $$n$$까지 유한하므로, 모든 $$i>0$$에 대한 vanishing을 동시에 보장하는 공통의 $$d_1$$을 잡을 수 있고, $$d\geq d_1$$에서 $$H^i(\mathbb{P}^n, \mathcal{F}(d))=0$$ ($$i>0$$)이다.

</details>

[정리 8](#thm8)은 [\[대수다양체\] §사영공간의 코호몰로지, ⁋명제 4](/ko/math/algebraic_varieties/cohomology_of_projective_spaces#prop4)의 Serre vanishing을 scheme 수준으로 옮긴 것으로, 그 증명의 골격은 line bundle의 코호몰로지를 아는 $$\mathbb{P}^n$$으로 환원한 뒤 연접층을 free sheaf의 quotient로 분해하여 dimension shifting을 반복하는 것이다. 정성적으로 이 정리는 임의의 연접층이 충분히 양의 방향으로 twist되면 사영공간 위의 line bundle처럼 "고차 정보가 사라지는" 단계에 도달함을 말해 준다. 함께 얻은 global generation은 twist된 sheaf가 global section만으로 완전히 생성됨을 뜻하며, 이는 연접층을 free sheaf의 resolution으로 표현하는 출발점이 되어 projective scheme 위의 호몰로지적 대수의 토대를 이룬다.

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic geometry*, Graduate Texts in Mathematics, Springer, 1977. (Chapter III.1–5)  
**[Vak]** R. Vakil, *The rising sea: Foundations of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/). (Chapter 18)  
**[EGA]** A. Grothendieck and J. Dieudonné, *Éléments de géométrie algébrique III*, Publ. Math. IHÉS, 1961.  
**[Stacks]** The Stacks Project Authors, *The Stacks Project*. Available [online](https://stacks.math.columbia.edu/).
