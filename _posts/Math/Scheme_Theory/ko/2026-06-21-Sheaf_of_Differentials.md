---
title: "Kähler 미분과 여접층"
description: "A-대수의 Kähler 미분 가군과 보편 도분을 상기하고, 추이 완전열과 conormal 완전열을 도입한다. 이어서 scheme 사상의 여접층을 대각선의 conormal로 정의하고 affine 위에서 연관층의 gluing과 일치함을 보이며, tangent sheaf와 Zariski 접공간, affine space 및 사영공간의 Euler 완전열을 다룬다. 마지막으로 여접층의 top exterior power로 canonical sheaf를 정의하고 사영공간에서 계산한 뒤 Serre 쌍대성을 진술한다."
excerpt: "Kähler differentials, the cotangent sheaf Ω_{X/S}, the tangent sheaf, the Euler sequence on P^n, and the canonical sheaf"

categories: [Math / Scheme Theory]
permalink: /ko/math/scheme_theory/sheaf_of_differentials
sidebar: 
    nav: "scheme_theory-ko"

date: 2026-06-21
weight: 19

published: false
drift_needed: true
---

Algebraic variety나 manifold 위에서 differential form은 tangent space와 그 쌍대를 통해 기하학을 해석학적으로 다루는 도구이다. Scheme의 세계에서는 좌표나 극한을 직접 쓸 수 없으므로, 미분을 순수하게 대수적으로 정의해야 한다. 그 출발점은 Kähler 미분 module로, 이는 Leibniz rule을 만족하는 도분 가운데 가장 보편적인 것을 표현한다. ([\[가환대수학\] §미분, ⁋정의 3](/ko/math/commutative_algebra/differentials#def3)) 이번 글에서는 우선 affine 수준에서 Kähler 미분 module과 그에 딸린 두 exact sequence를 상기한 뒤, 이를 scheme morphism $f:X \rightarrow S$에 대해 sheaf로 옮긴 *cotangent sheaf* $\Omega_{X/S}$를 정의한다. 이 sheaf는 affine 위에서 Kähler 미분 module의 associated sheaf를 붙인 것이자, 동시에 대각선 morphism의 conormal로도 얻어진다. 이로부터 tangent sheaf와 Zariski tangent space, 그리고 affine space와 projective space 위의 미분층의 구조를 살펴보고, 마지막으로 $\Omega_{X/k}$가 locally free일 때 그 top exterior power로 얻어지는 canonical sheaf $\omega_X$를 정의하여 사영공간에서 계산한 뒤 Serre duality를 진술한다.

## Kähler 미분 가군과 완전열

먼저 affine 수준에서의 미분을 상기한다. Ring $A$와 $A$-algebra $B$에 대하여, $B$의 $A$에 대한 *Kähler differential module* $\Omega_{B/A}$와 *universal $A$-derivation* $d:B \rightarrow \Omega_{B/A}$가 정의된다. ([\[가환대수학\] §미분, ⁋정의 3](/ko/math/commutative_algebra/differentials#def3)) 이는 $A$-derivation들의 functor $\Der_A(B, -)$를 표현하는 $B$-module로서, 임의의 $B$-module $M$에 대하여 자연스러운 isomorphism

$$\Der_A(B, M)\cong \Hom_B(\Omega_{B/A}, M)$$

이 성립한다. ([\[가환대수학\] §미분, ⁋보조정리 2](/ko/math/commutative_algebra/differentials#lem2)) 즉 $\Omega_{B/A}$는 원소들 $db$ ($b\in B$)로 생성되며, $d(xy)=xdy+ydx$와 $A$-선형성을 relation으로 가지는 $B$-module이다.

Scheme morphism으로 옮기기에 앞서, $\Omega$가 ring의 합성과 quotient에 대해 가지는 두 가지 functorial한 exact sequence를 정리해 둔다. 이들은 이후 cotangent sheaf의 국소적 거동을 통제하는 핵심 도구이다. 첫째는 ring들의 합성 $A \rightarrow B \rightarrow C$에 대한 추이 exact sequence이다.

::: 명제 1 (추이 exact sequence)
$A$-algebra $B$와 $B$-algebra $C$가 주어졌다 하자. 합성 $A \rightarrow B \rightarrow C$를 통해 $C$를 $A$-algebra로 보면, $C$-module들의 sequence

$$\Omega_{B/A}\otimes_BC \longrightarrow \Omega_{C/A} \longrightarrow \Omega_{C/B} \longrightarrow 0$$

은 exact이다.
:::
::: 증명
이는 [\[가환대수학\] §미분, ⁋명제 5](/ko/math/commutative_algebra/differentials#prop5)에서 $E=B$, $E'=C$, 그리고 base ring을 $A$로 두어 얻어지는 cotangent sequence 그 자체이다. 첫째 morphism은 universal derivation $d_{C/A}$를 $B$에서 온 원소들로 제한하여 base change한 $\Omega'_{\varphi/A}:\Omega_{B/A}\otimes_BC \rightarrow \Omega_{C/A}$이며, 둘째 morphism은 functoriality로 유도되는 $\Omega_\varphi:\Omega_{C/A} \rightarrow \Omega_{C/B}$이다. 인용한 명제에 의하여 이 sequence는 exact이다.
:::

이 exact sequence는 미분이 "두 단계의 확장"을 어떻게 누적하는지를 보여준다. $\Omega_{C/B}$는 $B$에서 온 좌표를 상수로 본 미분이므로, $\Omega_{C/A}$에서 $B$ 방향의 미분 $\Omega_{B/A}\otimes_BC$의 image를 quotient한 것이 $\Omega_{C/B}$가 된다. 둘째는 $C$가 $B$의 quotient로 주어질 때의 exact sequence로, conormal exact sequence라 불린다.

::: 명제 2 (Conormal exact sequence)
$A$-algebra $B$의 ideal $\mathfrak{a}$에 대하여 $C=B/\mathfrak{a}$라 하자. 그럼 $C$-module들의 sequence

$$\mathfrak{a}/\mathfrak{a}^2 \overset{\bar{d}}{\longrightarrow} \Omega_{B/A}\otimes_BC \longrightarrow \Omega_{C/A} \longrightarrow 0$$

은 exact이며, 첫째 morphism $\bar{d}$는 $f+\mathfrak{a}^2\mapsto df\otimes 1$로 주어진다.
:::
::: 증명
Surjection $\varphi:B \rightarrow C=B/\mathfrak{a}$에 [\[가환대수학\] §미분, ⁋명제 6](/ko/math/commutative_algebra/differentials#prop6)을 적용하면, $K=\ker\varphi=\mathfrak{a}$이므로 주어진 sequence를 그대로 얻는다. 첫째 morphism $\bar{d}:\mathfrak{a}/\mathfrak{a}^2 \rightarrow \Omega_{B/A}\otimes_BC$는 $d_{B/A}\vert_\mathfrak{a}$를 base change한 뒤 $\mathfrak{a}^2$을 kernel에 포함시켜 유도한 것으로, 인용한 명제의 증명에서 보았듯 $f+\mathfrak{a}^2\mapsto df\otimes 1$로 주어진다.
:::

여기서 $C=B/\mathfrak{a}$를 closed subscheme으로 생각하면, $\mathfrak{a}/\mathfrak{a}^2$은 그 *conormal module*에 해당한다. 즉 $\mathfrak{a}$가 정의하는 부분다양체의 법선 방향을 ideal의 일차항 $\mathfrak{a}/\mathfrak{a}^2$이 담고 있으며, conormal exact sequence는 부분다양체 위의 미분 $\Omega_{C/A}$를 ambient의 미분 $\Omega_{B/A}\otimes_BC$에서 법선 방향을 잘라내어 얻는다는 것을 말한다. 이 두 exact sequence는 모두 $\otimes_B C$나 quotient에 대해 자연스러우므로, affine open에서 affine open으로 제한하더라도 그대로 유지되며, 이것이 다음 절에서 미분층을 gluing할 수 있게 하는 형식적 근거이다.

## Cotangent sheaf

이제 scheme morphism $f:X \rightarrow S$에 대해 미분을 sheaf로 정의한다. 직관적으로 $\Omega_{X/S}$는 각 affine open 위에서 Kähler 미분 module의 associated sheaf $\widetilde{\Omega_{B/A}}$이어야 하며, 이를 모든 affine open에 걸쳐 자연스럽게 붙인 것이다. 다만 단순히 붙이는 것만으로는 well-defined임이 자명하지 않으므로, 대각선 morphism을 이용한 좌표 독립적인 정의를 함께 제시하고 둘이 일치함을 본다. 먼저 affine 위에서의 국소 모형을 명시한다.

$S=\Spec A$, $X=\Spec B$이고 $f$가 ring homomorphism $A \rightarrow B$로부터 올 때, $\Omega_{B/A}$는 $B$-module이므로 associated sheaf $\widetilde{\Omega_{B/A}}$를 정의한다. ([§준연접층, ⁋정의 4](/ko/math/scheme_theory/quasicoherent_sheaves#def4)) 이 associated sheaf는 affine open을 더 작은 principal open으로 줄여도 호환되는데, 임의의 $g\in B$에 대하여 localization과 Kähler 미분이 commute하므로

$$\Omega_{B_g/A}\cong (\Omega_{B/A})_g$$

이고, 따라서 [§준연접층, ⁋명제 5](/ko/math/scheme_theory/quasicoherent_sheaves#prop5)에 의하여 $\widetilde{\Omega_{B/A}}\vert_{D(g)}\cong \widetilde{\Omega_{B_g/A}}$가 성립한다. 이렇듯 국소 모형들이 restriction에 대해 일관되므로, 이들을 붙여 $X$ 전체 위의 quasi-coherent sheaf를 얻는다. 좌표에 의존하지 않는 정의는 대각선 morphism을 통한 것이다.

::: 정의 3
Scheme morphism $f:X \rightarrow S$에 대하여, [§값매김환, ⁋정의 3](/ko/math/scheme_theory/valuative_criteria#def3)의 대각선 morphism $\Delta:X \rightarrow X\times_SX$을 생각하자. $\Delta$의 image의 ideal sheaf를 $\mathcal{I}$라 할 때, $X$ 위의 *cotangent sheaf<sub>여접층</sub>* 혹은 *sheaf of relative differentials<sub>상대 미분층</sub>* $\Omega_{X/S}$를 conormal sheaf

$$\Omega_{X/S}=\Delta^\ast\bigl(\mathcal{I}/\mathcal{I}^2\bigr)$$

로 정의한다. 여기에서 $\Delta^\ast$는 pullback이다. ([§준연접층, ⁋정의 14](/ko/math/scheme_theory/quasicoherent_sheaves#def14))
:::

이 정의에서 $\mathcal{I}/\mathcal{I}^2$은 $\Delta(X)$ 위의 sheaf로 볼 수 있고, $\Delta$가 $X$를 그 image와 동일시하므로 $\Delta^\ast$를 통해 $X$ 위의 sheaf로 끌어온 것이다. 대각선의 ideal sheaf를 conormal로 취하는 것은 affine 수준에서 $B\otimes_AB \rightarrow B$의 kernel $\mathfrak{a}$를 $\mathfrak{a}/\mathfrak{a}^2$로 보는 것에 대응하며, 다음 명제가 이 좌표 독립적 정의와 앞서의 국소 모형이 일치함을 보장한다.

::: 명제 4
Scheme morphism $f:X \rightarrow S$에 대하여, $\Omega_{X/S}$는 $X$ 위의 quasi-coherent sheaf이다. 더욱이 $U=\Spec B\subseteq X$와 $V=\Spec A\subseteq S$가 $f(U)\subseteq V$인 affine open subset들이면

$$\Omega_{X/S}\vert_U\cong \widetilde{\Omega_{B/A}}$$

가 성립한다.
:::
::: 증명
먼저 affine morphism $f:\Spec B \rightarrow \Spec A$의 경우에 [정의 3](#def3)을 계산한다. 이 경우 $X\times_SX=\Spec(B\otimes_AB)$이고 ([§올곱, ⁋보조정리 2](/ko/math/scheme_theory/fiber_products#lem2)), 대각선 morphism $\Delta$는 곱사상 $\mu:B\otimes_AB \rightarrow B$, $b\otimes b'\mapsto bb'$로부터 온다. $\mathfrak{a}=\ker\mu$라 하면 $\Delta$의 image의 ideal sheaf는 $\widetilde{\mathfrak{a}}$이고, [§준연접층, ⁋명제 6](/ko/math/scheme_theory/quasicoherent_sheaves#prop6)의 exactness로부터 $\mathcal{I}/\mathcal{I}^2\cong \widetilde{\mathfrak{a}/\mathfrak{a}^2}$이다.

이제 $B$-module로서

$$\mathfrak{a}/\mathfrak{a}^2\cong \Omega_{B/A}$$

임을 보인다. Morphism $\mathfrak{a}/\mathfrak{a}^2 \rightarrow \Omega_{B/A}$를 $b\otimes 1-1\otimes b\mapsto db$로 정의하고, 역사상 $\Omega_{B/A} \rightarrow \mathfrak{a}/\mathfrak{a}^2$을 universal derivation으로부터 얻는다. 구체적으로 $\delta:B \rightarrow \mathfrak{a}/\mathfrak{a}^2$를 $\delta(b)=(b\otimes 1-1\otimes b)+\mathfrak{a}^2$로 정의하면, 임의의 $b, b'\in B$에 대하여 $B\otimes_AB$ 안에서

$$\begin{aligned}
(bb'\otimes 1-1\otimes bb')&=(b\otimes 1-1\otimes b)(1\otimes b')+(b'\otimes 1-1\otimes b')(b\otimes 1)\\
&\equiv b'(b\otimes 1-1\otimes b)+b(b'\otimes 1-1\otimes b')\pmod{\mathfrak{a}^2}
\end{aligned}$$

이 성립하므로 ($\mathfrak{a}/\mathfrak{a}^2$ 위에서 $b\otimes 1$과 $1\otimes b$가 같은 action을 하므로) $\delta$는 $A$-derivation이다. 따라서 universal property에 의하여 $\Omega_{B/A} \rightarrow \mathfrak{a}/\mathfrak{a}^2$이 유도되고, 두 morphism이 서로 역임은 generator 위에서 확인된다. ($db\mapsto \delta(b)\mapsto db$이고 $\mathfrak{a}/\mathfrak{a}^2$은 $\delta(b)$들로 생성된다.) 그러므로

$$\Omega_{\Spec B/\Spec A}=\Delta^\ast\widetilde{\mathfrak{a}/\mathfrak{a}^2}\cong \widetilde{\mathfrak{a}/\mathfrak{a}^2}\cong \widetilde{\Omega_{B/A}}$$

이고, 특히 affine 위에서 $\Omega_{X/S}$는 associated sheaf이므로 quasi-coherent sheaf이다. ($\Delta^\ast$는 $\Delta$가 closed immersion일 때 $\Delta(X)$ 위의 sheaf를 그 위에서 동일시하여 끌어오는 것이므로 module은 그대로 $\mathfrak{a}/\mathfrak{a}^2$이다.)

일반적인 $f$의 경우, $U=\Spec B\subseteq X$와 $V=\Spec A\subseteq S$가 $f(U)\subseteq V$인 affine open이면 $\Delta(U)\subseteq U\times_VU$이고 이는 $X\times_SX$의 open subset이다. 대각선의 ideal sheaf를 이 open 위로 제한하면 다시 곱사상 $B\otimes_AB \rightarrow B$의 kernel이 되므로, 위의 계산에 의하여 $\Omega_{X/S}\vert_U\cong \widetilde{\Omega_{B/A}}$이다. 이러한 affine open들이 $X$를 덮고, 그 위에서 associated sheaf이므로 $\Omega_{X/S}$는 quasi-coherent sheaf이다. ([§준연접층, ⁋정리 10](/ko/math/scheme_theory/quasicoherent_sheaves#thm10))
:::

따라서 cotangent sheaf는 두 정의가 일치하며, 실용적으로는 [명제 4](#prop4)에 따라 affine open 위에서 $\widetilde{\Omega_{B/A}}$로 계산하면 된다. 앞 절의 두 exact sequence도 associated sheaf functor의 exactness를 통해 sheaf 수준으로 곧바로 옮겨진다. 가령 scheme morphism들의 합성 $X \rightarrow Y \rightarrow S$에 대하여, 각 affine open 위에서 [명제 1](#prop1)을 associated sheaf로 옮기면 $\mathcal{O}_X$-module층들의 exact sequence

$$g^\ast\Omega_{Y/S} \longrightarrow \Omega_{X/S} \longrightarrow \Omega_{X/Y} \longrightarrow 0$$

을 얻으며 (단 $g:X \rightarrow Y$), closed subscheme $X\hookrightarrow Y$가 ideal sheaf $\mathcal{J}$로 주어질 때 [명제 2](#prop2)를 옮기면 conormal exact sequence

$$\mathcal{J}/\mathcal{J}^2 \longrightarrow \Omega_{Y/S}\vert_X \longrightarrow \Omega_{X/S} \longrightarrow 0$$

을 얻는다. 이 두 exact sequence는 미분층을 실제로 계산하는 표준 도구이다.

## Tangent sheaf와 Zariski 접공간

Cotangent sheaf의 쌍대를 취하면 tangent vector들의 sheaf를 얻는다. 이는 variety 위에서 tangent bundle에 해당하는 대수기하학적 대상이다.

::: 정의 5
Scheme morphism $f:X \rightarrow S$에 대하여, $X$의 *tangent sheaf<sub>접층</sub>*를

$$\mathcal{T}_{X/S}=\sHom_{\mathcal{O}_X}(\Omega_{X/S}, \mathcal{O}_X)$$

로 정의한다. ([§준연접층, ⁋정의 2](/ko/math/scheme_theory/quasicoherent_sheaves#def2))
:::

$\Omega_{X/S}$가 affine open 위에서 $\widetilde{\Omega_{B/A}}$이므로, 같은 open 위에서 $\mathcal{T}_{X/S}$의 section은 $\Hom_B(\Omega_{B/A}, B)\cong \Der_A(B, B)$, 즉 $B$의 $A$-derivation들이다. 따라서 tangent sheaf의 section은 미분 연산자, 곧 벡터장에 해당한다. $\Omega_{X/S}$가 locally free일 때 $\mathcal{T}_{X/S}$는 그 dual locally free sheaf이지만 ([§준연접층, ⁋정의 12](/ko/math/scheme_theory/quasicoherent_sheaves#def12)), 일반적으로는 $\sHom$이 정확한 쌍대를 주지 않을 수 있으므로 두 sheaf가 서로의 dual이 되는 것은 locally free인 경우에 한한다.

한 점에서의 tangent space는 cotangent sheaf의 fiber를 residue field 위에서 쌍대화하여 얻는다. Field $k$ 위의 scheme $X$의 점 $x$에 대하여, residue field를 $\kappa(x)$라 하면 ([§스킴, ⁋정의 5](/ko/math/scheme_theory/schemes#def5)) cotangent sheaf의 fiber $\Omega_{X/k}\otimes_{\mathcal{O}_X}\kappa(x)$가 정의된다.

::: 정의 6
Field $k$ 위의 scheme $X$와 그 점 $x\in X$에 대하여, $x$에서의 *Zariski tangent space<sub>자리스키 접공간</sub>*를

$$T_xX=\bigl(\Omega_{X/k}\otimes_{\mathcal{O}_X}\kappa(x)\bigr)^\vee=\Hom_{\kappa(x)}\bigl(\Omega_{X/k}\otimes_{\mathcal{O}_X}\kappa(x), \kappa(x)\bigr)$$

로 정의한다.
:::

이 정의는 local ring의 maximal ideal을 통한 친숙한 묘사와 일치한다. $x$가 residue field $\kappa(x)=k$를 가지는 점, 곧 $k$-rational point이고 $(\mathcal{O}_{X,x}, \mathfrak{m}_x)$가 그 local ring일 때, conormal exact sequence를 stalk에서 분석하면 $\Omega_{X/k}\otimes \kappa(x)\cong \mathfrak{m}_x/\mathfrak{m}_x^2$이 성립한다. 따라서 Zariski tangent space는 $(\mathfrak{m}_x/\mathfrak{m}_x^2)^\vee$, 즉 cotangent space $\mathfrak{m}_x/\mathfrak{m}_x^2$의 쌍대이다. 한 점에서의 차원 $\dim_{\kappa(x)}T_xX$가 그 점의 국소적 차원 $\dim \mathcal{O}_{X,x}$과 같은지 여부가 그 점이 nonsingular한지를 가르는 기준이 되며, 일반적으로는 $\dim_{\kappa(x)}T_xX\geq \dim \mathcal{O}_{X,x}$이다.

Regular local ring의 cotangent space $\mathfrak{m}/\mathfrak{m}^2$이 정확히 차원만큼의 dimension을 가진다는 사실은 ([\[가환대수학\] §정칙국소환](/ko/math/commutative_algebra/regular_local_rings)) 이 부등식이 등호가 되는 경우와 직접 연결된다. 모든 점에서 등호가 성립하여 $\Omega_{X/k}$가 locally free가 되는 경우가 smoothness에 해당하지만, $\Omega$의 국소자유성과 regularity의 정확한 관계는 별도의 논의를 요한다.

## Affine space와 사영공간의 미분층

미분층의 가장 기본적인 예시는 affine space이며, 이는 polynomial ring의 미분이 자유 module임을 그대로 옮긴 것이다.

::: 명제 7
임의의 scheme $S$에 대하여, affine space $\mathbb{A}^n_S$의 cotangent sheaf $\Omega_{\mathbb{A}^n_S/S}$는 rank $n$의 free sheaf

$$\Omega_{\mathbb{A}^n_S/S}\cong \mathcal{O}_{\mathbb{A}^n_S}^{\oplus n}$$

이며, $d\x_1,\ldots, d\x_n$을 기저로 가진다.
:::
::: 증명
문제가 $S$ 위에서 국소적이므로 $S=\Spec A$인 경우만 보이면 충분하다. 이 때 $\mathbb{A}^n_S=\Spec A[\x_1,\ldots, \x_n]$이고 $B=A[\x_1,\ldots, \x_n]$이라 하자. [명제 4](#prop4)에 의하여 $\Omega_{\mathbb{A}^n_S/S}\cong \widetilde{\Omega_{B/A}}$이므로 $\Omega_{B/A}$가 $d\x_1,\ldots, d\x_n$을 기저로 하는 자유 $B$-module임을 보이면 된다.

$\Omega_{B/A}$는 정의에 의하여 원소들 $df$ ($f\in B$)로 생성되는데, $d$가 $A$-derivation이므로 임의의 다항식 $f$에 대하여 chain rule

$$df=\sum_{i=1}^n\frac{\partial f}{\partial \x_i}d\x_i$$

가 성립한다. 따라서 $\Omega_{B/A}$는 $d\x_1,\ldots, d\x_n$으로 생성된다. 한편 이들이 $B$ 위에서 일차독립임을 보이기 위해, 각 $j$에 대하여 $j$번째 편미분 $\partial/\partial \x_j:B \rightarrow B$가 $A$-derivation임을 이용한다. 이는 universal property에 의하여 $B$-linear map $\partial_j:\Omega_{B/A} \rightarrow B$를 유도하며 $\partial_j(d\x_i)=\delta_{ij}$이므로, $\sum_i b_i d\x_i=0$이면 $\partial_j$를 적용하여 $b_j=0$을 얻는다. 그러므로 $d\x_1,\ldots, d\x_n$은 자유 기저이고 $\Omega_{B/A}\cong B^{\oplus n}$이다.
:::

이렇듯 affine space 위에서 미분층은 좌표함수의 미분이 자유 기저를 이루는 trivial bundle이다. Projective space로 넘어가면 상황이 더 흥미로워지는데, $\mathbb{P}^n$의 cotangent sheaf는 자유롭지 않지만 twisting sheaf들 사이의 short exact sequence, 곧 Euler exact sequence로 표현된다.

::: 정리 8 (Euler exact sequence)
Field $k$ 위의 projective space $\mathbb{P}^n=\mathbb{P}^n_k$에 대하여, $\mathcal{O}_{\mathbb{P}^n}$-module층들의 short exact sequence

$$0 \longrightarrow \Omega_{\mathbb{P}^n/k} \longrightarrow \mathcal{O}_{\mathbb{P}^n}(-1)^{\oplus(n+1)} \longrightarrow \mathcal{O}_{\mathbb{P}^n} \longrightarrow 0$$

이 존재한다.
:::
::: 증명
$\mathbb{P}^n=\Proj A_\bullet$, $A_\bullet=k[\x_0,\ldots, \x_n]$이라 하고 ([§사영공간과 Proj 구성, ⁋예시 12](/ko/math/scheme_theory/projective_schemes#ex12)) 표준 affine open $U_i=D_+(\x_i)$ 위에서 작업한다. $U_i$ 위에서 좌표는 $y^{(i)}_j=\x_j/\x_i$ ($j\neq i$)이며, $\Omega_{\mathbb{P}^n/k}\vert_{U_i}$는 [명제 7](#prop7)에 의하여 $d y^{(i)}_j$ ($j\neq i$)를 자유 기저로 하는 rank $n$의 자유 sheaf이다.

오른쪽 morphism $\mathcal{O}(-1)^{\oplus(n+1)} \rightarrow \mathcal{O}$를 정의하자. $\mathcal{O}(-1)^{\oplus(n+1)}$의 standard basis를 $e_0,\ldots, e_n$이라 할 때, 이 morphism을 $e_j\mapsto \x_j$로 정의한다. 여기에서 $\x_j$는 $\mathcal{O}(-1) \rightarrow \mathcal{O}$, 곧 $\mathcal{O} \rightarrow \mathcal{O}(1)$의 전역 section으로서 $\mathcal{O}(-1)$을 $\mathcal{O}$로 보내는 곱이다. 각 $U_i$ 위에서 $\x_i$가 가역이므로 이 morphism은 surjective이다.

이제 kernel을 계산하여 그것이 $\Omega_{\mathbb{P}^n/k}$임을 보인다. $U_i$ 위에서 $\mathcal{O}(-1)$을 $\x_i^{-1}$로 trivialize하면 위 morphism은 $(a_0,\ldots, a_n)\mapsto \sum_j a_j (\x_j/\x_i)$로 주어지고, 그 kernel은 $\sum_j a_j d(\x_j/\x_i)=0$를 만족하는 관계와 동일한 rank $n$의 자유 module이 된다. 구체적으로 morphism $\Omega_{\mathbb{P}^n/k}\vert_{U_i} \rightarrow \mathcal{O}(-1)^{\oplus(n+1)}\vert_{U_i}$을

$$d\Bigl(\frac{\x_j}{\x_i}\Bigr)\longmapsto \frac{1}{\x_i}\Bigl(e_j-\frac{\x_j}{\x_i}e_i\Bigr)$$

로 정의하면, 이 morphism의 image는 정확히 $\sum_j \x_j(\cdot)=0$의 kernel과 일치한다. 이 국소적 정의는 $U_i\cap U_j$ 위에서 좌표 변환과 호환되어 ($d(\x_l/\x_i)$와 $d(\x_l/\x_j)$의 변환이 $\x_i, \x_j$의 곱으로 상쇄되므로) 전역적인 morphism $\Omega_{\mathbb{P}^n/k} \rightarrow \mathcal{O}(-1)^{\oplus(n+1)}$로 붙는다. 따라서 주어진 sequence는 각 $U_i$ 위에서 exact이고, exactness는 국소적 성질이므로 전역적으로 short exact sequence를 이룬다.
:::

Euler exact sequence는 projective space 위의 미분기하를 떠받치는 가장 기본적인 관계이다. 가령 tangent sheaf $\mathcal{T}_{\mathbb{P}^n}$은 Euler exact sequence를 쌍대화한 $0 \rightarrow \mathcal{O} \rightarrow \mathcal{O}(1)^{\oplus(n+1)} \rightarrow \mathcal{T}_{\mathbb{P}^n} \rightarrow 0$로 주어지며, 다음 절에서는 같은 exact sequence의 determinant를 취하여 $\mathbb{P}^n$의 canonical sheaf를 계산한다.

## Canonical sheaf

Cotangent sheaf가 locally free일 때, 그 top exterior power는 rank $1$의 sheaf, 곧 invertible sheaf가 된다. 이렇게 얻어지는 단 하나의 invertible sheaf가 $X$의 기하를 상당 부분 통제하며, variety의 세계에서 이는 cotangent bundle의 top exterior power로 정의한 canonical line bundle에 해당한다. ([\[대수다양체\] §표준선다발, ⁋정의 5](/ko/math/algebraic_varieties/canonical_bundle#def5)) Scheme 위에서도 같은 구성이 그대로 작동하므로, 먼저 sheaf의 exterior power를 정리해 둔다.

$\mathcal{O}_X$-module층 $\mathcal{F}$와 정수 $r\geq 0$에 대하여, 각 열린집합 $U$에 $\mathcal{O}_X(U)$-module의 exterior power $\bigwedge^r_{\mathcal{O}_X(U)}\bigl(\mathcal{F}(U)\bigr)$를 대응시키는 presheaf의 sheafification을 $\bigwedge^r\mathcal{F}$로 적는다. ([\[다중선형대수학\] §텐서대수, ⁋정의 10](/ko/math/multilinear_algebra/tensor_algebras#def10)) Exterior power는 scalar 확장과 commute하므로 ([\[다중선형대수학\] §텐서대수, ⁋명제 14](/ko/math/multilinear_algebra/tensor_algebras#prop14)), 특히 $A$-module $M$과 $g\in A$에 대하여 $\bigl(\bigwedge^rM\bigr)_g\cong \bigwedge^r(M_g)$이다. 여기에서와 아래에서 인용하는 exterior algebra의 성질들은 인용처에서 characteristic이 $2$가 아니라는 가정 아래 놓인 alternating map의 논의 뒤에 서술되어 있으나, $\bigwedge$가 ideal $\langle x\otimes x\rangle$에 의한 quotient로 정의된 덕에 characteristic과 무관하게 성립하므로 임의의 $\mathcal{O}_X(U)$에 그대로 적용된다. 따라서 $U=\Spec A$ 위에서 $\mathcal{F}\vert_U\cong\widetilde M$이면 국소 모형들이 restriction과 호환되어

$$\bigl(\bigwedge\nolimits^r\mathcal{F}\bigr)\big\vert_U\cong \widetilde{\bigwedge\nolimits^rM}$$

이 성립하고 ([§준연접층, ⁋명제 5](/ko/math/scheme_theory/quasicoherent_sheaves#prop5)), 그러므로 quasi-coherent sheaf의 exterior power는 다시 quasi-coherent sheaf이다.

특히 $\mathcal{E}$가 rank $n$의 locally free sheaf이면 ([§준연접층, ⁋정의 12](/ko/math/scheme_theory/quasicoherent_sheaves#def12)), $\mathcal{E}\vert_U\cong\mathcal{O}_U^{\oplus n}$인 열린집합 $U$ 위에서 $\bigwedge^r\mathcal{E}\vert_U$는 기저 $e_1,\ldots, e_n$으로부터 만들어지는 $e_J$ ($\lvert J\rvert=r$)들을 기저로 가지므로 ([\[다중선형대수학\] §텐서대수, ⁋명제 13](/ko/math/multilinear_algebra/tensor_algebras#prop13)) rank $\binom{n}{r}$의 자유 sheaf이다. 즉 $\bigwedge^r\mathcal{E}$는 다시 locally free sheaf이며, $r=n$인 경우에는 rank $1$, 곧 invertible sheaf가 된다. 이 마지막 경우를 $\mathcal{E}$의 *determinant*라 부르고 $\det\mathcal{E}=\bigwedge^n\mathcal{E}$로 적는다.

::: 정의 9
Field $k$ 위의 scheme $X$에 대하여 cotangent sheaf $\Omega_{X/k}$가 rank $n$의 locally free sheaf라 하자. 그럼 $X$의 *canonical sheaf* $\omega_X$를 top exterior power

$$\omega_X=\bigwedge\nolimits^n\Omega_{X/k}=\det\Omega_{X/k}$$

로 정의한다.
:::

앞의 관찰에 의하여 $\omega_X$는 invertible sheaf이다. 더 일반적으로 scheme morphism $f:X \rightarrow S$에 대하여 $\Omega_{X/S}$가 rank $n$의 locally free sheaf일 때 relative canonical sheaf $\omega_{X/S}=\det\Omega_{X/S}$를 같은 식으로 정의하며, $S=\Spec k$인 경우가 위의 정의이다. $\Omega_{X/k}$의 국소자유성이라는 가정은 [정의 6](#def6) 이후에 언급한 nonsingularity 조건과 맞닿아 있으나, 둘의 정확한 관계는 그곳에서 유보해 둔 대로 $k$와 $X$에 대한 추가 가정을 요구한다. $k$가 algebraically closed이고 $X$가 $k$ 위의 irreducible한 separated finite type scheme인 경우에는, $\Omega_{X/k}$가 locally free sheaf인 것이 $X$의 모든 closed point $x$에서 $\dim_{\kappa(x)}T_xX=\dim\mathcal{O}_{X,x}$가 성립하는 것과 동치이며 그 때 rank $n$은 $X$의 차원과 일치한다. ([§차원, ⁋정의 1](/ko/math/scheme_theory/dimension#def1)) 여기에서 점을 closed point로 제한하는 것은 필수적인데, 가령 $X=\mathbb{A}^1_k$의 generic point $\eta$에서는 $\Omega_{X/k}$가 자유임에도 $\Omega_{X/k}\otimes\kappa(\eta)\cong\Omega_{k(\x)/k}$가 $1$차원인 반면 $\dim\mathcal{O}_{X,\eta}=0$이기 때문이다. 또 $k$가 perfect가 아니면 rank와 차원의 일치 자체가 깨지는데, $k=\mathbb{F}_p(\x)$ 위의 $X=\Spec k(\x^{1/p})$는 차원이 $0$인 regular scheme이지만 $\Omega_{X/k}$는 rank $1$의 자유 sheaf이다. 반대로 $\Omega_{X/k}$가 locally free가 아니면 top exterior power가 invertible sheaf가 되지 않으므로 위의 정의는 그대로 쓰이지 않으며, 그러한 scheme까지 포괄하려면 *dualizing sheaf*를 따로 도입해야 한다.

Canonical sheaf를 실제로 계산할 때 쓰는 도구는 determinant가 short exact sequence를 따라 tensor product로 분해된다는 사실이다.

::: 명제 10
Scheme $X$ 위의 locally free sheaf들의 short exact sequence

$$0 \longrightarrow \mathcal{E}' \longrightarrow \mathcal{E} \longrightarrow \mathcal{E}'' \longrightarrow 0$$

이 주어지고 $\mathcal{E}'$과 $\mathcal{E}''$의 rank가 각각 $r$과 $s$라 하자. 그럼 $\mathcal{E}$는 rank $r+s$의 locally free sheaf이며, isomorphism

$$\det\mathcal{E}\cong \det\mathcal{E}'\otimes_{\mathcal{O}_X}\det\mathcal{E}''$$

이 존재한다.
:::
::: 증명
먼저 rank를 확인한다. $\mathcal{E}''$이 locally free이므로 각 점은 $\mathcal{E}''\vert_U\cong\mathcal{O}_U^{\oplus s}$이고 $\mathcal{E}'\vert_U\cong\mathcal{O}_U^{\oplus r}$인 열린근방 $U$를 가진다. Sheaf의 surjection은 stalk에서만 전사이므로 기저 section들의 lift를 얻으려면 $U$를 한 번 더 줄여야 하는데, 기저가 유한하므로 각 기저 section이 $\mathcal{E}$의 section으로 올라가는 더 작은 열린근방을 유한 번 교차하면 된다. 그렇게 줄인 $U$ 위에서 $\mathcal{E}''\vert_U$의 기저 section들을 $\mathcal{E}\vert_U$로 들어올리면 surjection $\mathcal{E}\vert_U \rightarrow \mathcal{E}''\vert_U$의 splitting을 얻으므로 $\mathcal{E}\vert_U\cong\mathcal{E}'\vert_U\oplus\mathcal{O}_U^{\oplus s}\cong\mathcal{O}_U^{\oplus(r+s)}$이고, 따라서 $\mathcal{E}$는 rank $r+s$의 locally free sheaf이다.

이제 morphism

$$\varphi:\det\mathcal{E}'\otimes_{\mathcal{O}_X}\det\mathcal{E}'' \longrightarrow \det\mathcal{E}$$

를 구성한다. 열린집합 $V$ 위의 section $\omega'\in(\det\mathcal{E}')(V)$과 $\bar t_1\wedge\cdots\wedge\bar t_s\in(\det\mathcal{E}'')(V)$이 주어졌을 때, $V$를 충분히 줄여 각 $\bar t_i$를 $t_i\in\mathcal{E}(V)$로 들어올린 뒤

$$\varphi\bigl(\omega'\otimes(\bar t_1\wedge\cdots\wedge\bar t_s)\bigr)=\omega'\wedge t_1\wedge\cdots\wedge t_s$$

로 정의한다. 여기에서 좌변의 $\omega'$은 inclusion $\mathcal{E}'\hookrightarrow\mathcal{E}$가 유도하는 $\det\mathcal{E}' \rightarrow \bigwedge^r\mathcal{E}$를 통해 옮긴 section을 뜻한다. 이 값은 lift의 선택에 무관한데, 두 lift의 차는 $\mathcal{E}'$의 section이므로 $t_i$를 $t_i+a_i$ ($a_i\in\mathcal{E}'(V)$)로 바꿀 때 생기는 차이가 적어도 하나의 $a_i$를 인수로 가지는 항들의 합이고, 위의 국소 splitting에서 $\omega'$이 $\mathcal{E}'\vert_V$의 기저 $f_1,\ldots, f_r$에 대해 $f_1\wedge\cdots\wedge f_r$의 배수인 반면 $a_i$는 $f_j$들의 $\mathcal{O}_V$-일차결합이므로, 그러한 항은 어떤 $f_j$를 두 번 포함하여 $0$이 되기 때문이다. 그러므로 국소적으로 정의된 $\varphi$들은 겹치는 부분에서 일치하며 전역적인 morphism으로 붙는다.

$\varphi$가 isomorphism임은 국소적으로 확인하면 충분하다. 위의 $U$ 위에서 $\mathcal{E}'\vert_U$의 기저를 $f_1,\ldots, f_r$이라 하고 $\mathcal{E}''\vert_U$의 기저 $\bar g_1,\ldots, \bar g_s$의 lift를 $g_1,\ldots, g_s$라 하면, splitting에 의하여 $f_1,\ldots, f_r, g_1,\ldots, g_s$는 $\mathcal{E}\vert_U$의 기저이다. [\[다중선형대수학\] §텐서대수, ⁋명제 13](/ko/math/multilinear_algebra/tensor_algebras#prop13)에 의하여 $\det\mathcal{E}\vert_U$는 $f_1\wedge\cdots\wedge f_r\wedge g_1\wedge\cdots\wedge g_s$를 기저로 하는 rank $1$ 자유 sheaf이고, 마찬가지로 $(\det\mathcal{E}'\otimes\det\mathcal{E}'')\vert_U$는 $(f_1\wedge\cdots\wedge f_r)\otimes(\bar g_1\wedge\cdots\wedge\bar g_s)$를 기저로 한다. $\varphi$는 후자의 기저를 전자의 기저로 보내므로 $U$ 위에서 isomorphism이며, 따라서 전역적으로도 isomorphism이다.
:::

이를 Euler exact sequence에 적용하면 사영공간의 canonical sheaf가 곧바로 계산된다.

::: 예시 11
Field $k$ 위의 사영공간 $\mathbb{P}^n$을 생각하자. [정리 8](#thm8)의 증명에서 보았듯 $\Omega_{\mathbb{P}^n/k}$는 각 $U_i=D_+(\x_i)$ 위에서 $dy^{(i)}_j$ ($j\neq i$)를 기저로 하는 rank $n$의 자유 sheaf이므로 locally free이고, 따라서 $\omega_{\mathbb{P}^n}$이 정의된다. Euler exact sequence의 세 항 $\Omega_{\mathbb{P}^n/k}$, $\mathcal{O}(-1)^{\oplus(n+1)}$, $\mathcal{O}_{\mathbb{P}^n}$의 rank는 각각 $n$, $n+1$, $1$이므로, [명제 10](#prop10)에 의하여

$$\det\bigl(\mathcal{O}(-1)^{\oplus(n+1)}\bigr)\cong \omega_{\mathbb{P}^n}\otimes_{\mathcal{O}_{\mathbb{P}^n}}\det\mathcal{O}_{\mathbb{P}^n}\cong\omega_{\mathbb{P}^n}$$

이 성립한다. 좌변을 계산하기 위해 $\mathcal{O}(-1)\vert_{U_i}$의 generator $\x_i^{-1}$을 택하고 ([§스킴의 층 코호몰로지, ⁋정의 5](/ko/math/scheme_theory/sheaf_cohomology_of_schemes#def5)) $\mathcal{O}(-1)^{\oplus(n+1)}$의 standard basis를 $e_0,\ldots, e_n$이라 하면, $\det(\mathcal{O}(-1)^{\oplus(n+1)})\vert_{U_i}$는

$$(\x_i^{-1}e_0)\wedge\cdots\wedge(\x_i^{-1}e_n)=\x_i^{-n-1}(e_0\wedge\cdots\wedge e_n)$$

을 generator로 가진다. $U_i\cap U_j$ 위에서 $U_i$ 쪽 generator는 $U_j$ 쪽 generator의 $(\x_j/\x_i)^{n+1}$배이고, $\mathcal{O}(-n-1)$의 국소 generator $\x_i^{-n-1}$과 $\x_j^{-n-1}$ 사이에도 같은 관계가 성립한다. 즉 두 invertible sheaf는 같은 gluing 자료로 주어지므로

$$\det\bigl(\mathcal{O}(-1)^{\oplus(n+1)}\bigr)\cong\mathcal{O}(-1)^{\otimes(n+1)}\cong\mathcal{O}_{\mathbb{P}^n}(-n-1)$$

이고, 결국

$$\omega_{\mathbb{P}^n}\cong\mathcal{O}_{\mathbb{P}^n}(-n-1)$$

을 얻는다. 이는 variety 위에서 $n$-form의 transition function으로 수행한 계산과 일치한다. ([\[대수다양체\] §표준선다발, ⁋예시 8](/ko/math/algebraic_varieties/canonical_bundle#ex8))
:::

Canonical sheaf가 다른 invertible sheaf들 가운데 특별한 위치를 차지하는 까닭은, 그것이 cohomology 사이의 duality를 매개한다는 데 있다. 위상수학에서 fundamental class가 Poincaré duality를 주었듯, projective scheme 위에서는 $\omega_X$가 그 역할을 맡는다.

::: 정리 12 (Serre duality)
Algebraically closed field $k$ 위의 $n$차원 integral projective scheme $X$에 대하여 ([§사영공간의 닫힌 부분스킴, ⁋정의 7](/ko/math/scheme_theory/closed_subschemes_of_projective_spaces#def7), [§스킴의 대수구조, §§축소스킴과 정역스킴](/ko/math/scheme_theory/algebra_of_schemes#축소스킴과-정역스킴)) $\Omega_{X/k}$가 rank $n$의 locally free sheaf라 하자. 그럼 $X$ 위의 임의의 locally free sheaf $\mathcal{E}$와 $0\leq i\leq n$에 대하여 isomorphism

$$H^i(X, \mathcal{E})\cong H^{n-i}\bigl(X, \omega_X\otimes_{\mathcal{O}_X}\mathcal{E}^\vee\bigr)^\ast$$

이 존재한다. 여기에서 $\mathcal{E}^\vee=\sHom_{\mathcal{O}_X}(\mathcal{E}, \mathcal{O}_X)$이고, $(-)^\ast$는 유한차원 $k$-벡터공간의 쌍대이다. ([§스킴의 층 코호몰로지, ⁋정리 7](/ko/math/scheme_theory/sheaf_cohomology_of_schemes#thm7))
:::

이 정리의 증명은 trace map의 구성과 그 normalization, 그리고 finite morphism을 따라 duality를 옮기는 논증을 요구하여 이 글의 범위를 넘어서므로, [\[대수다양체\] §세르 쌍대성](/ko/math/algebraic_varieties/serre_duality)에 위임한다. 그곳에서는 먼저 $\mathbb{P}^n$ 위에서 isomorphism $H^n(\mathbb{P}^n, \omega_{\mathbb{P}^n})\cong k$이 정하는 trace map과 cup product로 pairing을 만들어 그것이 perfect pairing임을 보이고 ([\[대수다양체\] §세르 쌍대성, ⁋명제 2](/ko/math/algebraic_varieties/serre_duality#prop2)), 이어서 finite surjective morphism $X \rightarrow \mathbb{P}^n$을 따라 이를 일반의 $X$로 옮긴다. 이 morphism은 Noether normalization의 사영 판, 곧 일반적 위치의 linear projection에서 오는 것이며, affine 판인 [§차원, ⁋정리 9](/ko/math/scheme_theory/dimension#thm9)가 직접 주는 것은 아니다. 우리가 여기에서 가져다 쓰는 것은 그 결과인 isomorphism 자체이다.

$X=\mathbb{P}^n$과 $\mathcal{E}=\mathcal{O}(d)$인 경우에 [정리 12](#thm12)가 주장하는 바는 [예시 11](#ex11)에 의하여 isomorphism $H^i(\mathbb{P}^n, \mathcal{O}(d))\cong H^{n-i}(\mathbb{P}^n, \mathcal{O}(-d-n-1))^\ast$이며, 이는 이미 계산된 cohomology와 일치한다. 실제로 $i=0$이고 $d\geq 0$이면 좌변은 degree $d$의 homogeneous polynomial들이 이루는 $\binom{n+d}{n}$차원 공간이고, 우변의 $H^n(\mathbb{P}^n, \mathcal{O}(-d-n-1))$은 $\x_0^{-1},\ldots, \x_n^{-1}$들의 degree $d$ 부분이므로 역시 $\binom{n+d}{n}$차원이다. ([§스킴의 층 코호몰로지, ⁋정리 6](/ko/math/scheme_theory/sheaf_cohomology_of_schemes#thm6))

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate Texts in Mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundations of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).  
**[Eis]** D. Eisenbud, *Commutative algebra: with a view toward algebraic geometry*. Springer, 1995.  
**[Stacks]** The Stacks Project Authors, *The Stacks Project*. Available [online](https://stacks.math.columbia.edu/).
