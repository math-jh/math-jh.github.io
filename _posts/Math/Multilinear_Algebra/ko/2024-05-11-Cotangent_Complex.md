---
title: "코탄젠트 복합체"
description: "켈러 미분의 conormal sequence를 왼쪽으로 연장하는 naive cotangent complex를 정의하고, 그 호몰로지가 표현의 선택과 무관함을 살펴본다."
excerpt: "Kähler 미분의 cotangent complex로의 확장"

categories: [Math / Multilinear Algebra]
permalink: /ko/math/multilinear_algebra/cotangent_complex
sidebar: 
    nav: "multilinear_algebra-ko"

date: 2024-05-11
last_modified_at: 2026-06-11

weight: 122

published: false

---

[§미분가군, ⁋명제 14](/ko/math/multilinear_algebra/differential_modules#prop14)에서 우리는 commutative $$A$$-algebra들의 surjection $$u:E \rightarrow E'$$와 그 kernel $$\mathfrak{I}$$에 대하여, conormal sequence

$$\mathfrak{I}/\mathfrak{I}^2\overset{\overline{d}}{\longrightarrow}\Omega_{E/A}\otimes_EE'\longrightarrow\Omega_{E'/A}\longrightarrow0$$

이 exact라는 것을 살펴보았다. 이 sequence는 오른쪽 끝에서만 exact이며, 일반적으로 $$\overline{d}$$는 injective가 아니다. 자연스러운 질문은 $$\overline{d}$$의 kernel이 어떤 의미를 갖는지, 그리고 이 sequence를 왼쪽으로 연장할 수 있는지이다. 이번 글에서는 이 질문에 대한 첫 번째 답인 *naive cotangent complex*를 살펴본다. 이번 글에서 $$A$$는 commutative ring, $$E$$는 commutative $$A$$-algebra이다.

## Naive cotangent complex

핵심 아이디어는 $$E$$를 가장 다루기 쉬운 algebra, 즉 polynomial algebra의 quotient로 표현하는 것이다. $$E$$의 생성집합 $$(t_s)_{s\in S}$$를 아무거나 택하면 (가령 $$E$$ 전체), [\[대수적 구조\] §대수, ⁋명제 8](/ko/math/algebraic_structures/algebras#prop8)의 adjunction에 의하여 $$\x_s\mapsto t_s$$로 정의되는 surjective $$A$$-algebra homomorphism

$$p: R=A[\x_s]_{s\in S}\longrightarrow E$$

가 존재한다. 이러한 $$p$$를 $$E$$의 *presentation<sub>표현</sub>*이라 부르고, $$\mathfrak{I}=\ker p$$라 적자.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Presentation $$p:R \rightarrow E$$에 대하여, $$p$$의 *naive cotangent complex* $$\operatorname{NL}(p)$$는 conormal sequence의 왼쪽 두 항으로 이루어진 $$E$$-module들의 two-term complex

$$\operatorname{NL}(p)=\Bigl[\,\mathfrak{I}/\mathfrak{I}^2\overset{\overline{d}}{\longrightarrow}\Omega_{R/A}\otimes_RE\,\Bigr]$$

를 뜻한다. 여기서 $$\mathfrak{I}/\mathfrak{I}^2$$는 degree $$1$$, $$\Omega_{R/A}\otimes_RE$$는 degree $$0$$에 둔다.

</div>

즉 $$\operatorname{NL}(p)$$는 두 개의 항만 $$0$$이 아닌 chain complex이고 ([\[호몰로지 대수학\] §호몰로지](/ko/math/homological_algebra/homology)), 그 homology는

$$H_0\bigl(\operatorname{NL}(p)\bigr)=\coker\overline{d},\qquad H_1\bigl(\operatorname{NL}(p)\bigr)=\ker\overline{d}$$

뿐이다. [§미분가군, ⁋예시 10](/ko/math/multilinear_algebra/differential_modules#ex10)에서 살펴본 것과 같이 $$\Omega_{R/A}$$는 $$d\x_s$$들을 basis로 갖는 free $$R$$-module이므로, $$\operatorname{NL}(p)$$의 degree $$0$$ 항은 free $$E$$-module이다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 임의의 presentation $$p:R \rightarrow E$$에 대하여, canonical isomorphism

$$H_0\bigl(\operatorname{NL}(p)\bigr)\cong\Omega_{E/A}$$

이 존재한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[§미분가군, ⁋명제 14](/ko/math/multilinear_algebra/differential_modules#prop14)의 conormal sequence

$$\mathfrak{I}/\mathfrak{I}^2\overset{\overline{d}}{\longrightarrow}\Omega_{R/A}\otimes_RE\overset{\Omega_0(p)}{\longrightarrow}\Omega_{E/A}\longrightarrow0$$

에서 $$\Omega_0(p)$$가 surjective이고 그 kernel이 $$\im\overline{d}$$이므로, first isomorphism theorem에 의하여 $$\coker\overline{d}\cong\Omega_{E/A}$$이다.

</details>

즉 $$H_0$$는 presentation에 의존하지 않고 항상 Kähler differential module을 복원한다. 따라서 새로운 정보는 $$H_1(\operatorname{NL}(p))$$에 들어있으며, 이것이 conormal sequence의 왼쪽 끝에서의 exactness의 실패를 측정한다. 물론 이 이야기가 의미를 가지려면 $$H_1$$ 또한 presentation의 선택에 의존하지 않아야 한다.

## 표현의 선택과 무관성

두 presentation을 비교하기 위해 우선 다음을 관찰하자. 두 presentation $$p:R=A[\x_s]_{s\in S} \rightarrow E$$, $$p':R'=A[\y_t]_{t\in T} \rightarrow E$$가 주어졌다 하면, 각각의 $$s\in S$$마다 $$p'$$가 surjective이므로 $$p'(g_s)=p(\x_s)$$이도록 하는 $$g_s\in R'$$을 택할 수 있고, $$\x_s\mapsto g_s$$는 $$p'\circ\varphi=p$$를 만족하는 $$A$$-algebra homomorphism $$\varphi:R \rightarrow R'$$을 유도한다. 그럼 $$\varphi(\mathfrak{I})\subseteq\mathfrak{I}'$$이므로 $$\varphi$$는 두 complex 사이의 morphism

$$\operatorname{NL}(\varphi):\operatorname{NL}(p) \rightarrow \operatorname{NL}(p');\qquad \overline{f}\mapsto\overline{\varphi(f)},\quad d\x_s\otimes1\mapsto d\varphi(\x_s)\otimes1$$

을 유도한다. 사각형이 commute하는 것은 식 $$d\varphi(f)=\sum_s\varphi(\partial f/\partial\x_s)\,d\varphi(\x_s)$$로부터 확인된다.

<div class="proposition" markdown="1">

<ins id="lem3">**보조정리 3**</ins> 위의 상황에서, $$p'\circ\varphi=p=p'\circ\psi$$를 만족하는 두 $$A$$-algebra homomorphism $$\varphi,\psi:R \rightarrow R'$$이 주어졌다 하자. 그럼 임의의 $$f\in R$$에 대하여 다음의 식

$$\varphi(f)-\psi(f)\equiv\sum_{s\in S}\varphi\left(\frac{\partial f}{\partial \x_s}\right)\bigl(\varphi(\x_s)-\psi(\x_s)\bigr)\pmod{\mathfrak{I}'^2}$$

이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $$p'(\varphi(f)-\psi(f))=p(f)-p(f)=0$$이므로 $$\varphi(f)-\psi(f)\in\mathfrak{I}'$$이고, 마찬가지 이유로 위의 합동식의 양변이 모두 $$\mathfrak{I}'$$의 원소이므로 식이 말이 된다. 주어진 식을 만족하는 $$f$$들의 모임을 $$P$$라 하자. $$P$$가 $$A$$의 원소들을 포함하고 (양변이 모두 $$0$$이다), 각각의 변수 $$\x_s$$를 포함하며 ($$\partial\x_s/\partial\x_{s'}$$는 $$s=s'$$일 때 $$1$$, 아닐 때 $$0$$이다), $$A$$-linear combination에 대해 닫혀있는 것은 자명하다. 따라서 $$P$$가 곱셈에 대해 닫혀있는 것만 보이면 $$P=R$$이다.

$$f,g\in P$$라 하고, 편의상 $$\alpha=\varphi(f)-\psi(f)$$, $$\beta=\varphi(g)-\psi(g)\in\mathfrak{I}'$$라 적자. 그럼

$$\varphi(fg)-\psi(fg)=\varphi(f)\varphi(g)-\psi(f)\psi(g)=\varphi(f)\beta+\psi(f)\alpha+\alpha\beta-\alpha\beta=\varphi(f)\beta+\varphi(g)\alpha-\alpha\beta$$

인데, 마지막 등식은 $$\psi(f)\alpha=\varphi(f)\alpha-\alpha^2$$와 같은 식으로 정리한 것이며 $$\alpha^2,\alpha\beta\in\mathfrak{I}'^2$$이므로

$$\varphi(fg)-\psi(fg)\equiv\varphi(f)\beta+\varphi(g)\alpha\pmod{\mathfrak{I}'^2}$$

이다. 이제 $$f,g\in P$$라는 가정을 $$\alpha,\beta$$에 대입하고 Leibniz rule $$\partial(fg)/\partial\x_s=f\,(\partial g/\partial\x_s)+g\,(\partial f/\partial\x_s)$$를 사용하면, $$\mathfrak{I}'$$의 원소들끼리의 곱이 $$\mathfrak{I}'^2$$에서 사라진다는 것으로부터 $$fg\in P$$를 얻는다.

</details>

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> [보조정리 3](#lem3)의 상황에서, 두 morphism $$\operatorname{NL}(\varphi),\operatorname{NL}(\psi):\operatorname{NL}(p) \rightarrow \operatorname{NL}(p')$$은 chain homotopic이다. 특히 이들이 유도하는 homology의 morphism들은 일치한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\Omega_{R/A}\otimes_RE$$가 $$d\x_s\otimes1$$들을 basis로 갖는 free $$E$$-module이므로, $$E$$-linear map

$$h:\Omega_{R/A}\otimes_RE \rightarrow \mathfrak{I}'/\mathfrak{I}'^2;\qquad d\x_s\otimes1\mapsto\overline{\varphi(\x_s)-\psi(\x_s)}$$

이 잘 정의된다. 여기서 $$\varphi(\x_s)-\psi(\x_s)\in\mathfrak{I}'$$인 것은 [보조정리 3](#lem3)의 증명에서 보았고, $$\mathfrak{I}'/\mathfrak{I}'^2$$의 $$E$$-module 구조는 [§미분가군, ⁋명제 14](/ko/math/multilinear_algebra/differential_modules#prop14) 직전의 논의에서와 같다. 이제 $$h$$가 $$\operatorname{NL}(\varphi)-\operatorname{NL}(\psi)$$의 chain homotopy임을 보인다.

우선 degree $$0$$에서, 생성원 $$d\x_s\otimes 1$$에 대하여

$$\overline{d}'\bigl(h(d\x_s\otimes1)\bigr)=d\bigl(\varphi(\x_s)-\psi(\x_s)\bigr)\otimes1=\bigl(\operatorname{NL}(\varphi)-\operatorname{NL}(\psi)\bigr)(d\x_s\otimes1)$$

이다. 다음으로 degree $$1$$에서, 임의의 $$f\in\mathfrak{I}$$에 대하여 $$df=\sum_s(\partial f/\partial\x_s)\,d\x_s$$이므로

$$h\bigl(\overline{d}(\overline{f})\bigr)=\sum_sp\left(\frac{\partial f}{\partial\x_s}\right)\cdot\overline{\varphi(\x_s)-\psi(\x_s)}=\overline{\sum_s\varphi\left(\frac{\partial f}{\partial\x_s}\right)\bigl(\varphi(\x_s)-\psi(\x_s)\bigr)}$$

이다. 마지막 등식은 $$\mathfrak{I}'/\mathfrak{I}'^2$$ 위에서 $$E=R'/\mathfrak{I}'$$의 작용이 $$p'$$를 통해 주어지고 $$p'\circ\varphi=p$$이기 때문이다. 그럼 [보조정리 3](#lem3)에 의하여 이는 $$\overline{\varphi(f)-\psi(f)}=\bigl(\operatorname{NL}(\varphi)-\operatorname{NL}(\psi)\bigr)(\overline{f})$$와 같다. 따라서 $$h$$는 chain homotopy이고, chain homotopic한 morphism들이 같은 homology morphism을 유도하는 것은 [\[호몰로지 대수학\] §호몰로지](/ko/math/homological_algebra/homology)에서 살펴보았다.

</details>

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5**</ins> 두 presentation $$p:R \rightarrow E$$, $$p':R' \rightarrow E$$에 대하여, complex들 $$\operatorname{NL}(p)$$와 $$\operatorname{NL}(p')$$은 homotopy equivalent이다. 특히 canonical isomorphism

$$H_i\bigl(\operatorname{NL}(p)\bigr)\cong H_i\bigl(\operatorname{NL}(p')\bigr),\qquad i=0,1$$

이 존재한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

위에서 살펴본 것과 같이 $$p'\circ\varphi=p$$이도록 하는 $$\varphi:R \rightarrow R'$$과 $$p\circ\varphi'=p'$$이도록 하는 $$\varphi':R' \rightarrow R$$을 택하자. 그럼 $$\varphi'\circ\varphi$$와 $$\id_R$$은 모두 $$p\circ(\varphi'\circ\varphi)=p=p\circ\id_R$$을 만족하므로 [명제 4](#prop4)에 의하여

$$\operatorname{NL}(\varphi')\circ\operatorname{NL}(\varphi)=\operatorname{NL}(\varphi'\circ\varphi)\simeq\operatorname{NL}(\id_R)=\id_{\operatorname{NL}(p)}$$

이고, 대칭적으로 $$\operatorname{NL}(\varphi)\circ\operatorname{NL}(\varphi')\simeq\id_{\operatorname{NL}(p')}$$이다. 즉 $$\operatorname{NL}(\varphi)$$는 homotopy equivalence이고, homology에 isomorphism을 유도한다. 이 isomorphism이 canonical한 것은, $$\varphi$$의 다른 선택이 [명제 4](#prop4)에 의해 같은 homology morphism을 유도하기 때문이다.

</details>

따라서 우리는 presentation의 선택을 잊고, homotopy equivalence를 무시한다는 단서 하에 $$\operatorname{NL}_{E/A}$$라 적을 수 있다. 그 homology

$$H_0(\operatorname{NL}_{E/A})\cong\Omega_{E/A},\qquad H_1(\operatorname{NL}_{E/A})$$

는 $$A$$-algebra $$E$$의 invariant가 된다. $$H_1$$이 측정하는 것이 무엇인지 다음 예시에서 살펴보자.

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> 하나의 다항식으로 표현되는 algebra $$E=A[\x]/(f)$$를 생각하자. 여기서 $$f$$는 $$A[\x]$$의 nonzerodivisor라 가정한다. Presentation $$p:R=A[\x] \rightarrow E$$에 대하여 $$\mathfrak{I}=(f)$$이고, $$f$$가 nonzerodivisor이므로 $$\mathfrak{I}/\mathfrak{I}^2$$는 $$\overline{f}$$를 basis로 갖는 free $$E$$-module이다. 실제로 $$af\in(f^2)$$라면 $$af=bf^2$$로부터 $$a=bf\in(f)$$이다. 따라서

$$\operatorname{NL}_{E/A}=\Bigl[\,E\overline{f}\overset{\overline{d}}{\longrightarrow}E\,d\x\,\Bigr],\qquad \overline{d}(\overline{f})=\overline{Df}\,d\x$$

이다. 여기서 $$Df$$는 $$f$$의 derivative이다. 그럼

$$H_0(\operatorname{NL}_{E/A})=\Omega_{E/A}\cong E/(\overline{Df}),\qquad H_1(\operatorname{NL}_{E/A})\cong\ann_E(\overline{Df})$$

이다. 가령 $$A=\mathbb{K}$$가 characteristic이 $$2$$가 아닌 field이고 $$f=\x^2$$이라면 $$\overline{Df}=2\overline{\x}$$이므로 $$H_1\cong\ann_E(2\overline{\x})=(\overline{\x})\neq0$$이다. 반면 $$f$$와 $$Df$$가 $$A[\x]$$에서 서로소인 경우, 즉 $$f$$가 separable polynomial인 경우에는 $$\overline{Df}$$가 $$E$$의 unit이 되어 $$H_0=H_1=0$$이다. 즉 $$H_1$$은 $$\Omega_{E/A}$$만으로는 보이지 않는, presentation의 relation들이 갖는 중복도에 대한 정보를 담고 있다.

</div>

<div class="remark" markdown="1">

<ins id="rmk7">**참고 7**</ins> Naive cotangent complex는 이름 그대로 더 정교한 대상의 그림자이다. Quillen과 André는 polynomial algebra에 의한 한 번의 presentation 대신 simplicial resolution을 사용하여, 모든 degree에서 homology를 갖는 *cotangent complex* $$L_{E/A}$$를 정의하였다. 이 complex의 degree $$0,1$$ 부분이 정확히 위에서 정의한 $$\operatorname{NL}_{E/A}$$이다. 이러한 호모토피 이론적인 구성은 이 카테고리의 범위를 벗어나므로, 여기서는 두 항짜리 절단인 $$\operatorname{NL}_{E/A}$$로 만족하기로 한다.

</div>

---

**참고문헌**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  
**[Stacks]** The Stacks project authors, *The Stacks project*, [stacks.math.columbia.edu](https://stacks.math.columbia.edu), Tag 00S0.

---
