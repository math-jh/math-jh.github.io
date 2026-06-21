---
title: "Kähler 미분과 여접층"
description: "A-대수의 Kähler 미분 가군과 보편 도분을 상기하고, 추이 완전열과 conormal 완전열을 도입한다. 이어서 scheme 사상의 여접층을 대각선의 conormal로 정의하고 affine 위에서 연관층의 gluing과 일치함을 보이며, tangent sheaf와 Zariski 접공간, affine space 및 사영공간의 Euler 완전열을 다룬다."
excerpt: "Kähler differentials, the cotangent sheaf Ω_{X/S}, the tangent sheaf, and the Euler sequence on P^n"

categories: [Math / Scheme Theory]
permalink: /ko/math/scheme_theory/sheaf_of_differentials
sidebar: 
    nav: "scheme_theory-ko"

date: 2026-06-21
weight: 19

published: false
---

대수다양체나 manifold 위에서 미분형식은 접공간과 그 쌍대를 통해 기하학을 해석학적으로 다루는 도구이다. Scheme의 세계에서는 좌표나 극한을 직접 쓸 수 없으므로, 미분을 순수하게 대수적으로 정의해야 한다. 그 출발점은 Kähler 미분 가군으로, 이는 Leibniz rule을 만족하는 도분 가운데 가장 보편적인 것을 표현한다. ([\[가환대수학\] §미분, ⁋정의 3](/ko/math/commutative_algebra/differentials#def3)) 이번 글에서는 우선 affine 수준에서 Kähler 미분 가군과 그에 딸린 두 완전열을 상기한 뒤, 이를 scheme 사상 $$f:X \rightarrow S$$에 대해 sheaf로 옮긴 *cotangent sheaf* $$\Omega_{X/S}$$를 정의한다. 이 sheaf는 affine 위에서 Kähler 미분 가군의 연관층을 붙인 것이자, 동시에 대각선 사상의 conormal로도 얻어진다. 이로부터 tangent sheaf와 Zariski 접공간, 그리고 affine space와 사영공간 위의 미분층의 구조를 살펴본다.

## Kähler 미분 가군과 완전열

먼저 affine 수준에서의 미분을 상기한다. Ring $$A$$와 $$A$$-대수 $$B$$에 대하여, $$B$$의 $$A$$에 대한 *Kähler differential module* $$\Omega_{B/A}$$와 *universal $$A$$-derivation* $$d:B \rightarrow \Omega_{B/A}$$가 정의된다. ([\[가환대수학\] §미분, ⁋정의 3](/ko/math/commutative_algebra/differentials#def3)) 이는 $$A$$-derivation들의 functor $$\Der_A(B, -)$$를 표현하는 $$B$$-가군으로서, 임의의 $$B$$-가군 $$M$$에 대하여 자연스러운 동형사상

$$\Der_A(B, M)\cong \Hom_B(\Omega_{B/A}, M)$$

이 성립한다. ([\[가환대수학\] §미분, ⁋보조정리 2](/ko/math/commutative_algebra/differentials#lem2)) 즉 $$\Omega_{B/A}$$는 원소들 $$db$$ ($$b\in B$$)로 생성되며, $$d(xy)=x\,dy+y\,dx$$와 $$A$$-선형성을 relation으로 가지는 $$B$$-가군이다.

scheme 사상으로 옮기기에 앞서, $$\Omega$$가 환의 합성과 quotient에 대해 가지는 두 가지 functorial한 완전열을 정리해 둔다. 이들은 이후 cotangent sheaf의 국소적 거동을 통제하는 핵심 도구이다. 첫째는 환들의 합성 $$A \rightarrow B \rightarrow C$$에 대한 추이 완전열이다.

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1 (추이 완전열)**</ins> $$A$$-대수 $$B$$와 $$B$$-대수 $$C$$가 주어졌다 하자. 합성 $$A \rightarrow B \rightarrow C$$를 통해 $$C$$를 $$A$$-대수로 보면, $$C$$-가군들의 sequence

$$\Omega_{B/A}\otimes_BC \longrightarrow \Omega_{C/A} \longrightarrow \Omega_{C/B} \longrightarrow 0$$

은 exact이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

이는 [\[가환대수학\] §미분, ⁋명제 5](/ko/math/commutative_algebra/differentials#prop5)에서 $$E=B$$, $$E'=C$$, 그리고 base ring을 $$A$$로 두어 얻어지는 cotangent sequence 그 자체이다. 첫째 사상은 universal derivation $$d_{C/A}$$를 $$B$$에서 온 원소들로 제한하여 base change한 $$\Omega'_{\varphi/A}:\Omega_{B/A}\otimes_BC \rightarrow \Omega_{C/A}$$이며, 둘째 사상은 functoriality로 유도되는 $$\Omega_\varphi:\Omega_{C/A} \rightarrow \Omega_{C/B}$$이다. 인용한 명제에 의하여 이 sequence는 exact이다.

</details>

이 완전열은 미분이 "두 단계의 확장"을 어떻게 누적하는지를 보여준다. $$\Omega_{C/B}$$는 $$B$$에서 온 좌표를 상수로 본 미분이므로, $$\Omega_{C/A}$$에서 $$B$$ 방향의 미분 $$\Omega_{B/A}\otimes_BC$$의 image를 quotient한 것이 $$\Omega_{C/B}$$가 된다. 둘째는 $$C$$가 $$B$$의 quotient로 주어질 때의 완전열로, conormal 완전열이라 불린다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2 (Conormal 완전열)**</ins> $$A$$-대수 $$B$$의 ideal $$I$$에 대하여 $$C=B/I$$라 하자. 그럼 $$C$$-가군들의 sequence

$$I/I^2 \overset{\bar{d}}{\longrightarrow} \Omega_{B/A}\otimes_BC \longrightarrow \Omega_{C/A} \longrightarrow 0$$

은 exact이며, 첫째 사상 $$\bar{d}$$는 $$f+I^2\mapsto df\otimes 1$$로 주어진다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

surjection $$\varphi:B \rightarrow C=B/I$$에 [\[가환대수학\] §미분, ⁋명제 6](/ko/math/commutative_algebra/differentials#prop6)을 적용하면, $$K=\ker\varphi=I$$이므로 주어진 sequence를 그대로 얻는다. 첫째 사상 $$\bar{d}:I/I^2 \rightarrow \Omega_{B/A}\otimes_BC$$는 $$d_{B/A}\vert_I$$를 base change한 뒤 $$I^2$$을 kernel에 포함시켜 유도한 것으로, 인용한 명제의 증명에서 보았듯 $$f+I^2\mapsto df\otimes 1$$로 주어진다.

</details>

여기서 $$C=B/I$$를 닫힌 부분 scheme으로 생각하면, $$I/I^2$$은 그 *conormal module*에 해당한다. 즉 $$I$$가 정의하는 부분다양체의 법선 방향을 ideal의 일차항 $$I/I^2$$이 담고 있으며, conormal 완전열은 부분다양체 위의 미분 $$\Omega_{C/A}$$를 ambient의 미분 $$\Omega_{B/A}\otimes_BC$$에서 법선 방향을 잘라내어 얻는다는 것을 말한다. 이 두 완전열은 모두 $$\otimes_B C$$나 quotient에 대해 자연스러우므로, affine open에서 affine open으로 제한하더라도 그대로 유지되며, 이것이 다음 절에서 미분층을 gluing할 수 있게 하는 형식적 근거이다.

## Cotangent sheaf

이제 scheme 사상 $$f:X \rightarrow S$$에 대해 미분을 sheaf로 정의한다. 직관적으로 $$\Omega_{X/S}$$는 각 affine open 위에서 Kähler 미분 가군의 연관층 $$\widetilde{\Omega_{B/A}}$$이어야 하며, 이를 모든 affine open에 걸쳐 자연스럽게 붙인 것이다. 다만 단순히 붙이는 것만으로는 well-defined임이 자명하지 않으므로, 대각선 사상을 이용한 좌표 독립적인 정의를 함께 제시하고 둘이 일치함을 본다. 먼저 affine 위에서의 국소 모형을 명시한다.

$$S=\Spec A$$, $$X=\Spec B$$이고 $$f$$가 ring homomorphism $$A \rightarrow B$$로부터 올 때, $$\Omega_{B/A}$$는 $$B$$-가군이므로 연관층 $$\widetilde{\Omega_{B/A}}$$를 정의한다. ([§준연접층, ⁋정의 4](/ko/math/scheme_theory/quasicoherent_sheaves#def4)) 이 연관층은 affine open을 더 작은 principal open으로 줄여도 호환되는데, 임의의 $$g\in B$$에 대하여 localization과 Kähler 미분이 commute하므로

$$\Omega_{B_g/A}\cong (\Omega_{B/A})_g$$

이고, 따라서 [§준연접층, ⁋명제 5](/ko/math/scheme_theory/quasicoherent_sheaves#prop5)에 의하여 $$\widetilde{\Omega_{B/A}}\vert_{D(g)}\cong \widetilde{\Omega_{B_g/A}}$$가 성립한다. 이렇듯 국소 모형들이 제한에 대해 일관되므로, 이들을 붙여 $$X$$ 전체 위의 준연접층을 얻는다. 좌표에 의존하지 않는 정의는 대각선 사상을 통한 것이다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Scheme 사상 $$f:X \rightarrow S$$에 대하여, 대각선 사상 $$\Delta:X \rightarrow X\times_SX$$ ([§값매김환, ⁋정의 3](/ko/math/scheme_theory/valuative_criteria#def3))을 생각하자. $$\Delta$$의 image의 ideal sheaf를 $$\mathcal{I}$$라 할 때, $$X$$ 위의 *cotangent sheaf<sub>여접층</sub>* 혹은 *sheaf of relative differentials* $$\Omega_{X/S}$$를 conormal sheaf

$$\Omega_{X/S}=\Delta^\ast\bigl(\mathcal{I}/\mathcal{I}^2\bigr)$$

로 정의한다. 여기에서 $$\Delta^\ast$$는 pullback이다. ([§준연접층, ⁋정의 17](/ko/math/scheme_theory/quasicoherent_sheaves#def17))

</div>

이 정의에서 $$\mathcal{I}/\mathcal{I}^2$$은 $$\Delta(X)$$ 위의 sheaf로 볼 수 있고, $$\Delta$$가 $$X$$를 그 image와 동일시하므로 $$\Delta^\ast$$를 통해 $$X$$ 위의 sheaf로 끌어온 것이다. 대각선의 ideal sheaf를 conormal로 취하는 것은 affine 수준에서 $$B\otimes_AB \rightarrow B$$의 kernel $$I$$를 $$I/I^2$$로 보는 것에 대응하며, 다음 명제가 이 좌표 독립적 정의와 앞서의 국소 모형이 일치함을 보장한다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> Scheme 사상 $$f:X \rightarrow S$$에 대하여, $$\Omega_{X/S}$$는 $$X$$ 위의 준연접층이다. 더욱이 $$U=\Spec B\subseteq X$$와 $$V=\Spec A\subseteq S$$가 $$f(U)\subseteq V$$인 affine open subset들이면

$$\Omega_{X/S}\vert_U\cong \widetilde{\Omega_{B/A}}$$

가 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

먼저 affine 사상 $$f:\Spec B \rightarrow \Spec A$$의 경우에 [정의 3](#def3)을 계산한다. 이 경우 $$X\times_SX=\Spec(B\otimes_AB)$$이고 ([§올곱, ⁋보조정리 2](/ko/math/scheme_theory/fiber_products#lem2)), 대각선 사상 $$\Delta$$는 곱사상 $$\mu:B\otimes_AB \rightarrow B$$, $$b\otimes b'\mapsto bb'$$로부터 온다. $$I=\ker\mu$$라 하면 $$\Delta$$의 image의 ideal sheaf는 $$\widetilde I$$이고, [§준연접층, ⁋명제 6](/ko/math/scheme_theory/quasicoherent_sheaves#prop6)의 exactness로부터 $$\mathcal{I}/\mathcal{I}^2\cong \widetilde{I/I^2}$$이다.

이제 $$B$$-가군으로서

$$I/I^2\cong \Omega_{B/A}$$

임을 보인다. 사상 $$I/I^2 \rightarrow \Omega_{B/A}$$를 $$b\otimes 1-1\otimes b\mapsto db$$로 정의하고, 역사상 $$\Omega_{B/A} \rightarrow I/I^2$$을 universal derivation으로부터 얻는다. 구체적으로 $$\delta:B \rightarrow I/I^2$$를 $$\delta(b)=(b\otimes 1-1\otimes b)+I^2$$로 정의하면, 임의의 $$b, b'\in B$$에 대하여 $$B\otimes_AB$$ 안에서

$$\begin{aligned}
(bb'\otimes 1-1\otimes bb')&=(b\otimes 1-1\otimes b)(1\otimes b')+(b'\otimes 1-1\otimes b')(b\otimes 1)\\
&\equiv b'\,(b\otimes 1-1\otimes b)+b\,(b'\otimes 1-1\otimes b')\pmod{I^2}
\end{aligned}$$

이 성립하므로 ($$I/I^2$$ 위에서 $$b\otimes 1$$과 $$1\otimes b$$가 같은 작용을 하므로) $$\delta$$는 $$A$$-derivation이다. 따라서 universal property에 의하여 $$\Omega_{B/A} \rightarrow I/I^2$$이 유도되고, 두 사상이 서로 역임은 생성원 위에서 확인된다. ($$db\mapsto \delta(b)\mapsto db$$이고 $$I/I^2$$은 $$\delta(b)$$들로 생성된다.) 그러므로

$$\Omega_{\Spec B/\Spec A}=\Delta^\ast\widetilde{I/I^2}\cong \widetilde{I/I^2}\cong \widetilde{\Omega_{B/A}}$$

이고, 특히 affine 위에서 $$\Omega_{X/S}$$는 연관층이므로 준연접층이다. ($$\Delta^\ast$$는 $$\Delta$$가 closed immersion일 때 $$\Delta(X)$$ 위의 sheaf를 그 위에서 동일시하여 끌어오는 것이므로 가군은 그대로 $$I/I^2$$이다.)

일반적인 $$f$$의 경우, $$U=\Spec B\subseteq X$$와 $$V=\Spec A\subseteq S$$가 $$f(U)\subseteq V$$인 affine open이면 $$\Delta(U)\subseteq U\times_VU$$이고 이는 $$X\times_SX$$의 open subset이다. 대각선의 ideal sheaf를 이 open 위로 제한하면 다시 곱사상 $$B\otimes_AB \rightarrow B$$의 kernel이 되므로, 위의 계산에 의하여 $$\Omega_{X/S}\vert_U\cong \widetilde{\Omega_{B/A}}$$이다. 이러한 affine open들이 $$X$$를 덮고, 그 위에서 연관층이므로 $$\Omega_{X/S}$$는 준연접층이다. ([§준연접층, ⁋정리 10](/ko/math/scheme_theory/quasicoherent_sheaves#thm10))

</details>

따라서 cotangent sheaf는 두 정의가 일치하며, 실용적으로는 [명제 4](#prop4)에 따라 affine open 위에서 $$\widetilde{\Omega_{B/A}}$$로 계산하면 된다. 앞 절의 두 완전열도 연관층 functor의 exactness를 통해 sheaf 수준으로 곧바로 옮겨진다. 가령 scheme 사상들의 합성 $$X \rightarrow Y \rightarrow S$$에 대하여, 각 affine open 위에서 [명제 1](#prop1)을 연관층으로 옮기면 $$\mathcal{O}_X$$-가군층들의 완전열

$$g^\ast\Omega_{Y/S} \longrightarrow \Omega_{X/S} \longrightarrow \Omega_{X/Y} \longrightarrow 0$$

을 얻으며 (단 $$g:X \rightarrow Y$$), 닫힌 부분 scheme $$X\hookrightarrow Y$$가 ideal sheaf $$\mathcal{J}$$로 주어질 때 [명제 2](#prop2)를 옮기면 conormal 완전열

$$\mathcal{J}/\mathcal{J}^2 \longrightarrow \Omega_{Y/S}\vert_X \longrightarrow \Omega_{X/S} \longrightarrow 0$$

을 얻는다. 이 두 완전열은 미분층을 실제로 계산하는 표준 도구이다.

## Tangent sheaf와 Zariski 접공간

cotangent sheaf의 쌍대를 취하면 접벡터들의 sheaf를 얻는다. 이는 다양체 위에서 접다발에 해당하는 대수기하학적 대상이다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Scheme 사상 $$f:X \rightarrow S$$에 대하여, $$X$$의 *tangent sheaf<sub>접층</sub>*를

$$\mathcal{T}_{X/S}=\sHom_{\mathcal{O}_X}(\Omega_{X/S}, \mathcal{O}_X)$$

로 정의한다. ([§준연접층, ⁋정의 2](/ko/math/scheme_theory/quasicoherent_sheaves#def2))

</div>

$$\Omega_{X/S}$$가 affine open 위에서 $$\widetilde{\Omega_{B/A}}$$이므로, 같은 open 위에서 $$\mathcal{T}_{X/S}$$의 section은 $$\Hom_B(\Omega_{B/A}, B)\cong \Der_A(B, B)$$, 즉 $$B$$의 $$A$$-derivation들이다. 따라서 tangent sheaf의 section은 미분 연산자, 곧 벡터장에 해당한다. $$\Omega_{X/S}$$가 locally free일 때 $$\mathcal{T}_{X/S}$$는 그 dual locally free sheaf이지만 ([§준연접층, ⁋정의 15](/ko/math/scheme_theory/quasicoherent_sheaves#def15)), 일반적으로는 $$\sHom$$이 정확한 쌍대를 주지 않을 수 있으므로 두 sheaf가 서로의 dual이 되는 것은 locally free인 경우에 한한다.

한 점에서의 접공간은 cotangent sheaf의 fiber를 잉여류체 위에서 쌍대화하여 얻는다. Field $$k$$ 위의 scheme $$X$$의 점 $$x$$에 대하여, 잉여류체를 $$\kappa(x)$$라 하면 ([§스킴, ⁋정의 5](/ko/math/scheme_theory/schemes#def5)) cotangent sheaf의 fiber $$\Omega_{X/k}\otimes_{\mathcal{O}_X}\kappa(x)$$가 정의된다.

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> Field $$k$$ 위의 scheme $$X$$와 그 점 $$x\in X$$에 대하여, $$x$$에서의 *Zariski tangent space<sub>자리스키 접공간</sub>*를

$$T_xX=\bigl(\Omega_{X/k}\otimes_{\mathcal{O}_X}\kappa(x)\bigr)^\vee=\Hom_{\kappa(x)}\bigl(\Omega_{X/k}\otimes_{\mathcal{O}_X}\kappa(x), \kappa(x)\bigr)$$

로 정의한다.

</div>

이 정의는 국소환의 maximal ideal을 통한 친숙한 묘사와 일치한다. $$x$$가 잉여류체 $$\kappa(x)=k$$를 가지는 점, 곧 $$k$$-rational point이고 $$(\mathcal{O}_{X,x}, \mathfrak{m}_x)$$가 그 국소환일 때, conormal 완전열을 stalk에서 분석하면 $$\Omega_{X/k}\otimes \kappa(x)\cong \mathfrak{m}_x/\mathfrak{m}_x^2$$이 성립한다. 따라서 Zariski 접공간은 $$(\mathfrak{m}_x/\mathfrak{m}_x^2)^\vee$$, 즉 cotangent space $$\mathfrak{m}_x/\mathfrak{m}_x^2$$의 쌍대이다. 한 점에서의 차원 $$\dim_{\kappa(x)}T_xX$$가 그 점의 국소적 차원 $$\dim \mathcal{O}_{X,x}$$과 같은지 여부가 그 점이 nonsingular한지를 가르는 기준이 되며, 일반적으로는 $$\dim_{\kappa(x)}T_xX\geq \dim \mathcal{O}_{X,x}$$이다.

regular local ring의 cotangent space $$\mathfrak{m}/\mathfrak{m}^2$$이 정확히 차원만큼의 dimension을 가진다는 사실은 ([\[가환대수학\] §정칙국소환](/ko/math/commutative_algebra/regular_local_rings)) 이 부등식이 등호가 되는 경우와 직접 연결된다. 모든 점에서 등호가 성립하여 $$\Omega_{X/k}$$가 locally free가 되는 경우가 smoothness에 해당하지만, $$\Omega$$의 국소자유성과 regularity의 정확한 관계는 별도의 논의를 요한다.

## Affine space와 사영공간의 미분층

미분층의 가장 기본적인 예시는 affine space이며, 이는 다항식환의 미분이 자유 가군임을 그대로 옮긴 것이다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> 임의의 scheme $$S$$에 대하여, affine space $$\mathbb{A}^n_S$$의 cotangent sheaf $$\Omega_{\mathbb{A}^n_S/S}$$는 rank $$n$$의 free sheaf

$$\Omega_{\mathbb{A}^n_S/S}\cong \mathcal{O}_{\mathbb{A}^n_S}^{\oplus n}$$

이며, $$d\x_1,\ldots, d\x_n$$을 기저로 가진다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

문제가 $$S$$ 위에서 국소적이므로 $$S=\Spec A$$인 경우만 보이면 충분하다. 이 때 $$\mathbb{A}^n_S=\Spec A[\x_1,\ldots, \x_n]$$이고 $$B=A[\x_1,\ldots, \x_n]$$이라 하자. [명제 4](#prop4)에 의하여 $$\Omega_{\mathbb{A}^n_S/S}\cong \widetilde{\Omega_{B/A}}$$이므로 $$\Omega_{B/A}$$가 $$d\x_1,\ldots, d\x_n$$을 기저로 하는 자유 $$B$$-가군임을 보이면 된다.

$$\Omega_{B/A}$$는 정의에 의하여 원소들 $$df$$ ($$f\in B$$)로 생성되는데, $$d$$가 $$A$$-derivation이므로 임의의 다항식 $$f$$에 대하여 chain rule

$$df=\sum_{i=1}^n\frac{\partial f}{\partial \x_i}\,d\x_i$$

가 성립한다. 따라서 $$\Omega_{B/A}$$는 $$d\x_1,\ldots, d\x_n$$으로 생성된다. 한편 이들이 $$B$$ 위에서 일차독립임을 보이기 위해, 각 $$j$$에 대하여 $$j$$번째 편미분 $$\partial/\partial \x_j:B \rightarrow B$$가 $$A$$-derivation임을 이용한다. 이는 universal property에 의하여 $$B$$-linear map $$\partial_j:\Omega_{B/A} \rightarrow B$$를 유도하며 $$\partial_j(d\x_i)=\delta_{ij}$$이므로, $$\sum_i b_i\,d\x_i=0$$이면 $$\partial_j$$를 적용하여 $$b_j=0$$을 얻는다. 그러므로 $$d\x_1,\ldots, d\x_n$$은 자유 기저이고 $$\Omega_{B/A}\cong B^{\oplus n}$$이다.

</details>

이렇듯 affine space 위에서 미분층은 좌표함수의 미분이 자유 기저를 이루는 trivial bundle이다. 사영공간으로 넘어가면 상황이 더 흥미로워지는데, $$\mathbb{P}^n$$의 cotangent sheaf는 자유롭지 않지만 twisting sheaf들 사이의 짧은 완전열, 곧 Euler 완전열로 표현된다.

<div class="proposition" markdown="1">

<ins id="thm8">**정리 8 (Euler 완전열)**</ins> Field $$k$$ 위의 사영공간 $$\mathbb{P}^n=\mathbb{P}^n_k$$에 대하여, $$\mathcal{O}_{\mathbb{P}^n}$$-가군층들의 짧은 완전열

$$0 \longrightarrow \Omega_{\mathbb{P}^n/k} \longrightarrow \mathcal{O}_{\mathbb{P}^n}(-1)^{\oplus(n+1)} \longrightarrow \mathcal{O}_{\mathbb{P}^n} \longrightarrow 0$$

이 존재한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\mathbb{P}^n=\Proj S$$, $$S=k[\x_0,\ldots, \x_n]$$이라 하고 ([§사영스킴, ⁋예시 12](/ko/math/scheme_theory/projective_schemes#ex12)) 표준 affine open $$U_i=D_+(\x_i)$$ 위에서 작업한다. $$U_i$$ 위에서 좌표는 $$y^{(i)}_j=\x_j/\x_i$$ ($$j\neq i$$)이며, $$\Omega_{\mathbb{P}^n/k}\vert_{U_i}$$는 [명제 7](#prop7)에 의하여 $$d y^{(i)}_j$$ ($$j\neq i$$)를 자유 기저로 하는 rank $$n$$의 자유 sheaf이다.

오른쪽 사상 $$\mathcal{O}(-1)^{\oplus(n+1)} \rightarrow \mathcal{O}$$를 정의하자. $$\mathcal{O}(-1)^{\oplus(n+1)}$$의 표준 기저를 $$e_0,\ldots, e_n$$이라 할 때, 이 사상을 $$e_j\mapsto \x_j$$로 정의한다. 여기에서 $$\x_j$$는 $$\mathcal{O}(-1) \rightarrow \mathcal{O}$$, 곧 $$\mathcal{O} \rightarrow \mathcal{O}(1)$$의 전역 section으로서 $$\mathcal{O}(-1)$$을 $$\mathcal{O}$$로 보내는 곱이다. 각 $$U_i$$ 위에서 $$\x_i$$가 가역이므로 이 사상은 surjective이다.

이제 kernel을 계산하여 그것이 $$\Omega_{\mathbb{P}^n/k}$$임을 보인다. $$U_i$$ 위에서 $$\mathcal{O}(-1)$$을 $$\x_i^{-1}$$로 trivialize하면 위 사상은 $$(a_0,\ldots, a_n)\mapsto \sum_j a_j (\x_j/\x_i)$$로 주어지고, 그 kernel은 $$\sum_j a_j\,d(\x_j/\x_i)=0$$를 만족하는 관계와 동일한 rank $$n$$의 자유 가군이 된다. 구체적으로 사상 $$\Omega_{\mathbb{P}^n/k}\vert_{U_i} \rightarrow \mathcal{O}(-1)^{\oplus(n+1)}\vert_{U_i}$$을

$$d\Bigl(\frac{\x_j}{\x_i}\Bigr)\longmapsto \frac{1}{\x_i}\Bigl(e_j-\frac{\x_j}{\x_i}e_i\Bigr)$$

로 정의하면, 이 사상의 image는 정확히 $$\sum_j \x_j(\cdot)=0$$의 kernel과 일치한다. 이 국소적 정의는 $$U_i\cap U_j$$ 위에서 좌표 변환과 호환되어 ($$d(\x_l/\x_i)$$와 $$d(\x_l/\x_j)$$의 변환이 $$\x_i, \x_j$$의 곱으로 상쇄되므로) 전역적인 사상 $$\Omega_{\mathbb{P}^n/k} \rightarrow \mathcal{O}(-1)^{\oplus(n+1)}$$로 붙는다. 따라서 주어진 sequence는 각 $$U_i$$ 위에서 exact이고, exactness는 국소적 성질이므로 전역적으로 짧은 완전열을 이룬다.

</details>

Euler 완전열은 사영공간 위의 미분기하를 떠받치는 가장 기본적인 관계이다. 이로부터 가령 $$\mathbb{P}^n$$의 canonical sheaf $$\omega_{\mathbb{P}^n}=\bigwedge^n\Omega_{\mathbb{P}^n/k}\cong \mathcal{O}_{\mathbb{P}^n}(-n-1)$$를 완전열의 determinant를 취하여 계산할 수 있으며, 이는 사영공간이 음의 곡률을 가진다는 사실의 대수적 표현이다. 또 tangent sheaf $$\mathcal{T}_{\mathbb{P}^n}$$은 Euler 완전열을 쌍대화한 $$0 \rightarrow \mathcal{O} \rightarrow \mathcal{O}(1)^{\oplus(n+1)} \rightarrow \mathcal{T}_{\mathbb{P}^n} \rightarrow 0$$로 주어진다.

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate Texts in Mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundations of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).  
**[Eis]** D. Eisenbud, *Commutative algebra: with a view toward algebraic geometry*. Springer, 1995.  
**[Stacks]** The Stacks Project Authors, *The Stacks Project*. Available [online](https://stacks.math.columbia.edu/).
