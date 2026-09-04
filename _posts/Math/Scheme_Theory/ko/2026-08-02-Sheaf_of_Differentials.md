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

---

이제 우리는 미분의 개념을 정의한다. Algebraic variety나 scheme 위에서는 해석학적인 극한이 존재하지 않으므로, 이를 정의하기 위해서는 순수하게 대수적인 방식을 택해야 하며 그 출발점은 가환대수학에서 구성한 Kähler differential module이다. 이 글에서는 이를 scheme morphism의 cotangent sheaf로 붙이고, tangent sheaf와 Zariski tangent space, affine space와 projective space에서의 계산을 거쳐 canonical sheaf의 정의와 Serre duality의 진술까지 정리한다.

## 캘러 미분가군과 여접층

먼저 affine 수준의 대수적인 도구들을 기억해보자. Ring $A$와 $A$-algebra $B$에 대하여, $B$의 $A$에 대한 *Kähler differential module* $\Omega_{B/A}$와 *universal $A$-derivation* $d:B \rightarrow \Omega_{B/A}$가 정의된다. ([\[가환대수학\] §미분, ⁋정의 3](/ko/math/commutative_algebra/differentials#def3)) 이는 $A$-derivation들의 functor $\Der_A(B, -)$를 표현하는 $B$-module로서, 임의의 $B$-module $M$에 대하여 natural isomorphism

$$\Der_A(B, M)\cong \Hom_B(\Omega_{B/A}, M)$$

을 통해 characterize된다. ([\[가환대수학\] §미분, ⁋보조정리 2](/ko/math/commutative_algebra/differentials#lem2)) 즉, $\Omega_{B/A}$는 원소들 $\dd{b}$로 생성되며, Leibniz 법칙 $\dd{(xy)}=x\dd{y}+y\dd{x}$과 $A$-linearity를 relation으로 가지는 $B$-module이며, 직관적으로 $\Omega_{B/A}$는 $A$의 원소들은 상수로 생각하고, $B$의 각 원소들은 함수로 생각한 후 이에 따라 Leibniz 법칙을 요구하는 것으로 생각할 수 있다. 

위의 $B$-module은 $B$의 $A$-algebra 구조, 혹은 다른 말로 하면 ring homomorphism $A\rightarrow B$로부터 오는 것이므로, 이는 scheme morphism $\Spec B\rightarrow \Spec A$로 생각할 수 있다. 그럼 위에서 정의한 $B$-module $\Omega_{B/A}$는, scheme의 언어에서는 $\Spec B$ 위에 정의된 quasi-coherent sheaf $\widetilde{\Omega_{B/A}}$로 번역될 것이며, 일반적인 scheme morphism $\varphi:X\rightarrow S$에 대해서는 이들을 이어붙여 $\Omega_{X/S}$를 만들게 된다. ([§스킴 사이의 사상, ⁋명제 1](/ko/math/scheme_theory/morphism_of_schemes#prop1)) 그럼 위의 직관에 따르면, 이는 base $S$ 방향은 고정한채로, $\varphi:X\rightarrow S$의 fiber방향만 함수로 생각하여 미분을 한 것이라 생각할 수 있다. 

본격적인 이야기를 시작하기 전에 우리는 대수적인 도구들을 먼저 우리가 사용할 형태로 가져온다. Kähler differential module은 다음의 두 핵심적인 exact sequence들을 갖는다. 

::: 명제 1 (Cotangent exact sequence)
$A$-algebra $B$와 $B$-algebra $C$가 주어졌다 하자. 합성 $A \rightarrow B \rightarrow C$를 통해 $C$를 $A$-algebra로 보면, $C$-module들의 sequence

$$\Omega_{B/A}\otimes_BC \rightarrow \Omega_{C/A} \rightarrow \Omega_{C/B} \rightarrow 0$$

은 exact이다.
:::
::: 증명
이 exact sequence는 정확히 [\[가환대수학\] §미분, ⁋명제 8](/ko/math/commutative_algebra/differentials#prop8)에서 $E=B$, $E'=C$, 그리고 base ring을 $A$로 두어 얻어지는 cotangent sequence이다. 
:::

남은 하나의 exact sequence는 다음과 같다.

::: 명제 2 (Conormal exact sequence)
$A$-algebra $B$의 ideal $\mathfrak{a}$에 대하여 $C=B/\mathfrak{a}$라 하자. 그럼 $C$-module들의 sequence

$$\mathfrak{a}/\mathfrak{a}^2 \overset{\bar{d}}{\rightarrow} \Omega_{B/A}\otimes_BC \rightarrow \Omega_{C/A} \rightarrow 0$$

은 exact이며, 첫째 morphism $\bar{d}$는 $f+\mathfrak{a}^2\mapsto \dd{f}\otimes 1$로 주어진다.
:::
::: 증명
Surjection $\phi:B \rightarrow C=B/\mathfrak{a}$에 [\[가환대수학\] §미분, ⁋명제 9](/ko/math/commutative_algebra/differentials#prop9)를 적용하면 된다.
:::

위에서 언급한 것과 같이, 우리는 이들을 이어붙여 scheme morphism에 대한 Kähler differential을 정의해야 한다. 이는 본질적으로 base와 fiber쪽 각각을 affine으로 줄여야하므로, 우리는 이들 각각에 대한 gluing 조건이 필요하다. 

위에서 정의한 $\Omega$는 ring homomorphism들의 commutative square에 대하여 functorial하므로 ([\[가환대수학\] §미분, ⁋명제 6](/ko/math/commutative_algebra/differentials#prop6)), $A$-algebra homomorphism $B \rightarrow B'$는 canonical한 $B'$-linear map $\Omega_{B/A}\otimes_BB' \rightarrow \Omega_{B'/A}$를 유도하고 base의 변화 $A \rightarrow A'$는 canonical $B$-module homomorphism $\Omega_{B/A} \rightarrow \Omega_{B/A'}$를 유도한다. Gluing을 위해 필요한 것은 이들 canonical map들이 isomorphism이 되는 다음 경우들이다.

::: 명제 3
$A$-algebra $B$에 대하여 다음이 성립한다.

1. 임의의 $g\in B$에 대하여, canonical map은 $B_g$-module의 isomorphism $(\Omega_{B/A})_g\cong\Omega_{B_g/A}$를 준다.
2. $h\in A$의 image가 $B$에서 가역이어서 $B$를 $A_h$-algebra로 볼 수 있다면, canonical map은 isomorphism $\Omega_{B/A}\cong\Omega_{B/A_h}$를 준다.
:::
::: 증명
첫째 주장은 multiplicative subset $S=\{1, g, g^2,\ldots\}$에 대한 [\[가환대수학\] §미분, ⁋명제 7](/ko/math/commutative_algebra/differentials#prop7)이다. 그 진술의 좌변 $\Omega_{B/A}\otimes_BB_g$가 $(\Omega_{B/A})_g$와 같기 때문이다. ([\[가환대수학\] §국소화의 성질들, ⁋보조정리 1](/ko/math/commutative_algebra/properties_of_localization#lem1))

둘째 주장을 위해 [명제 1](#prop1)을 $A$-algebra $A_h$와 $A_h$-algebra $B$에 적용하면 $B$-module들의 exact sequence

$$\Omega_{A_h/A}\otimes_{A_h}B \rightarrow \Omega_{B/A} \rightarrow \Omega_{B/A_h} \rightarrow 0$$

을 얻는다. 그런데 universal derivation $d:A \rightarrow \Omega_{A/A}$는 Leibniz 법칙으로부터 

$$\dd{(1)}=\dd{(1\cdot 1)}=2\dd{(1)},$$

즉 $\dd{(1)}=0$을 만족하고 $A$-linear이므로 임의의 $a\in A$에 대하여 $\dd{a}=a\cdot \dd{(1)}=0$이며, 따라서 $\Omega_{A/A}=0$이다. 여기에 첫째 주장을 $B=A$와 $g=h$에 대하여 적용하면 $\Omega_{A_h/A}\cong(\Omega_{A/A})_h=0$이므로 위 sequence의 첫 항이 소멸하고, 남은 $\Omega_{B/A} \rightarrow \Omega_{B/A_h}$가 isomorphism이다.
:::

이제 $\varphi(U)\subseteq V$인 affine open subset들 $U=\Spec B\subseteq X$와 $V=\Spec A\subseteq S$마다 정의된 local model $\widetilde{\Omega_{B/A}}$를 이어붙여야 한다. 이러한 모양의 gluing은 [§올곱, ⁋정리 8](/ko/math/scheme_theory/fiber_products#thm8)에서 fiber product를 구성할 때 이미 거쳤으며, 그곳에서도 factor 쪽과 base 쪽의 축소를 각각 확인한 뒤 조각들을 이어붙였다. 

실제 gluing argument는 다음과 같다. 우선 $U$를 $g\in B$가 정의하는 principal open $D(g)$로 줄이면 [명제 3](#prop3)의 첫째 주장이

$$\Omega_{B_g/A}\cong (\Omega_{B/A})_g$$

를 주므로, [§준연접층, ⁋명제 5](/ko/math/scheme_theory/quasicoherent_sheaves#prop5)에 의하여 $\widetilde{\Omega_{B/A}}\vert_{D(g)}\cong \widetilde{\Omega_{B_g/A}}$가 성립한다. Base 쪽을 줄이는 것도 마찬가지로, $V$를 $\varphi(U)\subseteq D(h)$인 principal open $D(h)=\Spec A_h$ ($h\in A$)로 바꾸면 $h$의 image가 $B$의 어떤 prime ideal에도 속하지 않아 가역이므로, [명제 3](#prop3)의 둘째 주장에 의하여 $\Omega_{B/A}\cong\Omega_{B/A_h}$가 되어 local model이 변하지 않기 때문이다. 이들이 모두 functoriality에서 온 canonical한 isomorphism이므로, 두 chart가 겹치는 부분을 양쪽에서 principal인 열린집합들로 덮어 local model들을 canonical하게 identify할 수 있고 이 identification들은 triple intersection 위에서 cocycle condition을 만족한다. 즉 다음 정의가 $X$ 위의 sheaf를 유일하게 결정한다. ([\[위상수학\] §층, ⁋명제 8](/ko/math/topology/sheaves#prop8))

::: 정의 4
Scheme morphism $\varphi:X \rightarrow S$에 대하여, $X$ 위의 *cotangent sheaf<sub>여접층</sub>* 혹은 *sheaf of relative differentials<sub>상대 미분층</sub>* $\Omega_{X/S}$를, $\varphi(U)\subseteq V$인 affine open subset들 $U=\Spec B\subseteq X$와 $V=\Spec A\subseteq S$마다

$$\Omega_{X/S}\vert_U=\widetilde{\Omega_{B/A}}$$

로 두어 얻어지는 $\mathcal{O}_X$-module로 정의한다. ([§준연접층, ⁋정의 4](/ko/math/scheme_theory/quasicoherent_sheaves#def4))
:::

이렇게 정의된 $\Omega_{X/S}$가 무엇을 재는지는 $\varphi$를 $S$로 parametrize된 family로 보고 base를 바꾸어 볼 때 드러난다. 이를 위한 도구는 $\Omega_{X/S}$가 base change에 대하여 잘 행동한다는 것이다. 

::: 명제 5 (Base change)
$A$-algebra $B$와 $A$-algebra $A'$에 대하여 $B'=B\otimes_AA'$라 하자. 그럼 canonical한 $B'$-module isomorphism

$$\Omega_{B'/A'}\cong\Omega_{B/A}\otimes_BB'$$

이 성립한다.
:::
::: 증명
임의의 $B'$-module $M$에 대하여, $A'$-derivation $D:B' \rightarrow M$을 $B$ 위로 제한하면 $A$-derivation $B \rightarrow M$을 얻는다. 거꾸로 임의의 $A$-derivation $D_0:B \rightarrow M$은 Leibniz 법칙에 의하여 $b\otimes a'\mapsto a'D_0(b)$로 유일하게 확장되므로, 이 제한은 $\Der_{A'}(B', M)\cong\Der_A(B, M)$을 준다. 그런데 [\[가환대수학\] §미분, ⁋보조정리 2](/ko/math/commutative_algebra/differentials#lem2)에 의하여 이 isomorphism의 좌변은 $\Hom_{B'}(\Omega_{B'/A'}, M)$이고, 우변은 

$$\Hom_B(\Omega_{B/A}, M)\cong\Hom_{B'}(\Omega_{B/A}\otimes_BB', M)$$

이므로 ([\[대수적 구조\] §스칼라의 변환, ⁋명제 6](/ko/math/algebraic_structures/change_of_base_ring#prop6)), 두 $B'$-module이 같은 functor의 representative이므로 canonical하게 isomorphic하다. ([\[범주론\] §표현가능한 함자, ⁋명제 8](/ko/math/category_theory/representable_functors#prop8))
:::

양변이 affine open 위의 값으로 결정되고 그 identification이 universal derivation에서 오는 canonical한 것이므로, 이 isomorphism은 scheme 수준으로 붙는다. 즉 morphism $S' \rightarrow S$에 대하여 $X'=X\times_SS'$와 projection $\pi:X' \rightarrow X$를 두면 $\Omega_{X'/S'}\cong \pi^\ast\Omega_{X/S}$가 성립한다. 특히 점 $s\in S$에 대하여 $S'=\Spec\kappa(s)$로 두면 $X'$은 $s$ 위의 fiber $X_s$이므로 ([§올곱, ⁋정의 12](/ko/math/scheme_theory/fiber_products#def12)), 이 fiber가 $X$로 들어가는 canonical morphism을 $\iota:X_s \rightarrow X$라 할 때

$$\iota^\ast\Omega_{X/S}\cong\Omega_{X_s/\kappa(s)}$$

를 얻는다. 가장 단순한 예로 $S=\Spec \mathbb{K}[\x]$와 $X=\Spec \mathbb{K}[\x, \y]$에 대하여 첫 좌표로의 projection $X \rightarrow S$를 생각하면, $\Omega_{X/S}$는 $\dd{\y}$를 기저로 하는 rank $1$의 free module이다. ([\[가환대수학\] §미분, ⁋명제 5](/ko/math/commutative_algebra/differentials#prop5))

Family가 자명하지 않을 때에는 $\Omega_{X/S}$가 fiber의 기하까지 기록한다. $A=\mathbb{K}[t]$와 $B=\mathbb{K}[t, \x, \y]/(\x\y-t)$에 대하여 $\varphi:X=\Spec B \rightarrow S=\Spec A$를 생각하자. 그럼 관계식이 $t=\x\y$를 주므로 $B\cong \mathbb{K}[\x, \y]$이고 $X$ 자체는 affine plane이다. 그러나 이를 제대로 보기 위해서는 $\varphi$가 $X$를 어떻게 family로 만드는지 보는 것이 좋다. 구체적으로 $a\in \mathbb{K}$가 $0$이 아닐 때 $t=a$ 위의 fiber $X_a$는 쌍곡선 $\x\y=a$이지만, $t=0$ 위의 fiber $X_0$는 이것이 degenerate하여 두 직선 $\x\y=0$이 된다. 

이제 이들이 $\Omega_{X/S}$에 어떻게 나타나는지 보자. $B$는 $A[\x, \y]$를 ideal $\mathfrak{a}=(\x\y-t)$로 나눈 것이므로, [명제 2](#prop2)를 $A$-algebra $A[\x, \y]$와 그 ideal $\mathfrak{a}$에 적용하면 $B$-module들의 exact sequence

$$\mathfrak{a}/\mathfrak{a}^2 \overset{\bar{d}}{\rightarrow} \Omega_{A[\x, \y]/A}\otimes_{A[\x, \y]}B \rightarrow \Omega_{B/A} \rightarrow 0$$

을 얻는다. 가운데 항의 $\Omega_{A[\x, \y]/A}$는 $\dd{\x}$와 $\dd{\y}$를 기저로 하는 free module이므로 ([\[가환대수학\] §미분, ⁋명제 5](/ko/math/commutative_algebra/differentials#prop5)) 이 항은 $B\dd{\x}\oplus B\dd{\y}$이고, $\mathfrak{a}$가 $\x\y-t$ 하나로 생성되므로 그 quotient $\mathfrak{a}/\mathfrak{a}^2$ 역시 마찬가지이다. 이제 $t\in A$에서 $\dd{t}=0$임을 쓰면 $\bar{d}(\x\y-t)=\x \dd{\y}+\y \dd{\x}$이므로, 관계식은 이것 하나뿐이며

$$\Omega_{B/A}\cong\bigl(B\dd{\x}\oplus B\dd{\y}\bigr)/(\x \dd{\y}+\y \dd{\x})$$

이다. 그럼 각 fiber 위에서 이 관계식이 어떻게 풀리는지를 볼 수 있다. 우선 $t=a$ 위에서는 $\x$가 가역이므로 관계식이 $\dd{\y}=-(\y/\x)\dd{\x}$가 되어, $\Omega_{X_a/\mathbb{K}}$는 $\dd{\x}$를 기저로 하는 rank $1$의 free module이다. 반면 원점에서의 fiber $X_0$ 위에서는 상황이 조금 달라지는데, 이 경우 (원점이 아닌) $x$축 위에 있는 점 $q$는 $\mathfrak{m}_q$가 $\x$를 포함하지 않고, 거꾸로 $y$축 위에 있는 점 $q$는 $\mathfrak{m}_q$가 $\y$를 포함하지 않으므로 이 경우 모두 관계식이 $\kappa(q)$ 위에서 자명하지 않다. 즉, $\Omega_{X/S}\otimes\kappa(q)$가 $1$차원이 된다. 두 직선이 만나는 원점 $p$에서는 $\x$와 $\y$가 모두 $\mathfrak{m}_p$에 속하여 위의 관계식이 소멸하므로 $\Omega_{X/S}\otimes\kappa(p)$는 $\dd{\x}$와 $\dd{\y}$가 생성하는 $2$차원 vector space가 된다. 곧 fiber $\Omega_{X/S}\otimes\kappa(q)$의 차원은 두 직선이 만나는 점에서만 $1$에서 $2$로 뛰며, 이는 $X$ 위에서 $\mathbb{K}$에 대한 미분만을 취한 $\Omega_{X/\mathbb{K}}$가 rank $2$의 free module이라는 사실에서는 보이지 않는 정보이다.

위의 정의는 계산에 곧바로 쓸 수 있지만, 그 정의에 chart의 선택이 필요하다. 좌표에 의존하지 않는 묘사는 이미 대수적인 수준에서 얻어졌는데, [\[가환대수학\] §미분, ⁋명제 4](/ko/math/commutative_algebra/differentials#prop4)가 multiplication $m:B\otimes_AB \rightarrow B$의 kernel $\mathfrak{I}$에 대하여 canonical isomorphism $\mathfrak{I}/\mathfrak{I}^2\cong\Omega_{B/A}$를 주기 때문이다. 이를 기하적으로 번역하면 $\Spec(B\otimes_AB)$는 $\Spec B$의 $\Spec A$ 위에서의 fiber product이고 ([§올곱, ⁋보조정리 2](/ko/math/scheme_theory/fiber_products#lem2)) $m$에 대응되는 것은 diagonal morphism $\Delta$이므로, $\mathfrak{I}$는 $\Delta$의 ideal이고 $\mathfrak{I}/\mathfrak{I}^2$은 그 conormal module이다. 곧 $\Delta$의 1차 근방에서 미분을 읽어낸 것이며, 이를 scheme 위로 옮기면 chart를 고르지 않는 $\Omega_{X/S}$의 묘사를 얻는다. 

::: 명제 6
Separated morphism ([§값매김환, ⁋정의 3](/ko/math/scheme_theory/valuative_criteria#def3)) $\varphi:X \rightarrow S$에 대하여, diagonal morphism $\Delta:X \rightarrow X\times_SX$은 closed embedding이므로 그 image는 $X\times_SX$의 closed subscheme을 정의한다. 이 closed subscheme의 ideal sheaf를 $\mathcal{I}$라 할 때, conormal sheaf와의 isomorphism

$$\Omega_{X/S}\cong\Delta^\ast\bigl(\mathcal{I}/\mathcal{I}^2\bigr)$$

가 성립한다. 여기에서 $\Delta^\ast$는 pullback이다. ([§준연접층, ⁋정의 14](/ko/math/scheme_theory/quasicoherent_sheaves#def14))
:::
::: 증명
양변 모두 affine chart 위에서의 값으로 결정되므로, 위에서 $\Omega_{X/S}$를 정의했을 때와 마찬가지로 affine open chart $U,V$를 잡고 그 위에서 두 sheaf가 canonical하게 identify된다는 것을 보이면 충분하다. 먼저 affine morphism $\varphi:\Spec B \rightarrow \Spec A$의 경우에 $\Delta^\ast(\mathcal{I}/\mathcal{I}^2)$을 계산한다. 위에서 살펴보았듯, 이 경우 $X\times_SX=\Spec(B\otimes_AB)$이고, diagonal morphism $\Delta$는 multiplication $m:B\otimes_AB \rightarrow B$, $b\otimes b'\mapsto bb'$로부터 온다. 이제 $\mathfrak{a}=\ker m$라 하면 $\Delta$의 image의 ideal sheaf는 $\widetilde{\mathfrak{a}}$이고, [§준연접층, ⁋명제 6](/ko/math/scheme_theory/quasicoherent_sheaves#prop6)의 exactness로부터 $\mathcal{I}/\mathcal{I}^2\cong \widetilde{\mathfrak{a}/\mathfrak{a}^2}$이다.

이제 $B$-module로서 $\mathfrak{a}/\mathfrak{a}^2\cong \Omega_{B/A}$임을 보이자. 이를 위해 먼저 $A$-bilinear map $(b, c)\mapsto c\dd{b}$가 유도하는 $A$-linear map

$$\theta:B\otimes_AB \rightarrow \Omega_{B/A};\qquad b\otimes c\mapsto c\dd{b}$$

를 생각한다. 그럼 임의의 $b, b', c, c'\in B$에 대하여

$$\begin{aligned}
\theta\bigl((b\otimes c)(b'\otimes c')\bigr)&=cc'\dd{(bb')}=bcc'\dd{b}'+b'cc'\dd{b}\\
&=m(b\otimes c)\theta(b'\otimes c')+m(b'\otimes c')\theta(b\otimes c)
\end{aligned}$$

이고 양변이 두 인자 각각에 대하여 additive이므로, 임의의 $u, v\in B\otimes_AB$에 대하여 $\theta(uv)=m(u)\theta(v)+m(v)\theta(u)$가 성립한다. 특히 $u, v\in\mathfrak{a}=\ker m$이면 우변이 사라지므로 $\theta(\mathfrak{a}^2)=0$이고, 따라서 $\theta$는 $\mathfrak{a}/\mathfrak{a}^2 \rightarrow \Omega_{B/A}$로 내려가며 이 map은 $b\otimes 1-1\otimes b$를 $\dd{b}$로 보낸다.

거꾸로 $\delta:B \rightarrow \mathfrak{a}/\mathfrak{a}^2$를 $\delta(b)=(b\otimes 1-1\otimes b)+\mathfrak{a}^2$로 정의하면, 임의의 $b, b'\in B$에 대하여 $B\otimes_AB$ 안에서

$$\begin{aligned}
(bb'\otimes 1-1\otimes bb')&=(b\otimes 1-1\otimes b)(1\otimes b')+(b'\otimes 1-1\otimes b')(b\otimes 1)\\
&\equiv b'(b\otimes 1-1\otimes b)+b(b'\otimes 1-1\otimes b')\pmod{\mathfrak{a}^2}
\end{aligned}$$

이 성립하므로 $\delta$는 $A$-derivation이다. 따라서 universal property에 의하여 $\Omega_{B/A} \rightarrow \mathfrak{a}/\mathfrak{a}^2$이 유도되고, $\mathfrak{a}$가 $b\otimes 1-1\otimes b$ 꼴의 원소들로 생성되며 $\Omega_{B/A}$가 $\dd{b}$들로 생성되므로 이것이 $\theta$의 역임은 generator 위에서 확인된다.

한편 $R=B\otimes_AB$라 두면 $\Delta$는 surjection $m:R \rightarrow R/\mathfrak{a}\cong B$로부터 오는 closed immersion이므로, affine 위에서 pullback $\Delta^\ast$가 하는 일은 $R$-module에 $-\otimes_RB$를 적용하는 것이다. 그런데 $\mathfrak{a}$가 $\mathfrak{a}/\mathfrak{a}^2$를 소멸시켜 그 $R$-module 구조가 이미 $R/\mathfrak{a}=B$를 통해 주어지므로 $(\mathfrak{a}/\mathfrak{a}^2)\otimes_RB\cong \mathfrak{a}/\mathfrak{a}^2$이고, 따라서 다음의 isomorphism

$$\Delta^\ast\widetilde{\mathfrak{a}/\mathfrak{a}^2}\cong \widetilde{\mathfrak{a}/\mathfrak{a}^2}\cong \widetilde{\Omega_{B/A}}$$

을 얻는다. 여기에서 맨 왼쪽의 $\widetilde{(-)}$는 $\Spec R$ 위의, 나머지 둘은 $\Spec B$ 위의 associated sheaf이다. 

일반적인 $\varphi$의 경우, $U=\Spec B\subseteq X$와 $V=\Spec A\subseteq S$가 $\varphi(U)\subseteq V$인 affine open이면 $\Delta(U)\subseteq U\times_VU$이고 이는 $X\times_SX$의 open subset이다. Diagonal의 ideal sheaf를 이 open 위로 제한하면 다시 multiplication $B\otimes_AB \rightarrow B$의 kernel이 되므로, 위의 계산이 그대로 적용되어 $\Delta^\ast(\mathcal{I}/\mathcal{I}^2)\vert_U\cong \widetilde{\Omega_{B/A}}=\Omega_{X/S}\vert_U$이다. 이 identification은 universal derivation으로부터 canonical하게 만들어진 것이므로 chart를 줄이거나 바꾸어도 서로 일치하며, 따라서 하나의 global isomorphism으로 붙는다.
:::

위의 증명에서 보듯이 $\mathcal{I}/\mathcal{I}^2$은 $\Delta(X)$ 위의 sheaf로서, $\Delta$가 $X$를 그 image와 동일시하므로 $\Delta^\ast$를 통해 $X$ 위의 sheaf로 끌어온 것으로, 실제 계산을 할 때 우리는 [정의 4](#def4)에 따라 affine open 위에서 $\widetilde{\Omega_{B/A}}$로 계산하겠지만 위의 명제가 이 sheaf의 좌표에 의존하지 않는 묘사를 준다. 

앞 절의 두 exact sequence도 associated sheaf functor의 exactness를 통해 sheaf 수준으로 곧바로 옮겨진다. ([§준연접층, ⁋명제 6](/ko/math/scheme_theory/quasicoherent_sheaves#prop6)) Scheme morphism들의 합성 $X \rightarrow S' \rightarrow S$와 그 첫 morphism $\psi: X \rightarrow S'$에 대하여, 각 affine open 위에서 [명제 1](#prop1)을 associated sheaf로 옮기면 $\mathcal{O}_X$-module들의 exact sequence

$$\psi^\ast\Omega_{S'/S} \rightarrow \Omega_{X/S} \rightarrow \Omega_{X/S'} \rightarrow 0$$

을 얻으며, closed immersion $\iota:Z\hookrightarrow Y$가 ideal sheaf $\mathcal{J}$로 주어질 때 [명제 2](#prop2)를 옮기면 conormal exact sequence

$$\mathcal{J}/\mathcal{J}^2 \rightarrow \iota^\ast\Omega_{Y/S} \rightarrow \Omega_{Z/S} \rightarrow 0$$

을 얻는다. 가운데 항은 $Y$ 위의 sheaf를 $\iota$를 따라 $Z$로 끌어온 pullback이며, 첫 항의 $\mathcal{J}/\mathcal{J}^2$ 또한 $Z$ 위의 sheaf로 읽어야 한다. 이는 [§닫힌 부분스킴, ⁋정의 5](/ko/math/scheme_theory/closed_subschemes#def5)에 의해 $\mathcal{O}_Y/\mathcal{J}\cong \iota_\ast \mathcal{O}_Z$이고, $\mathcal{J}$가 quotient $\mathcal{J}/\mathcal{J}^2$를 소멸시켜 그 $\mathcal{O}_Y$-module 구조가 이미 $\mathcal{O}_Y/\mathcal{J}$를 통해 주어지기 때문에 가능하다. 실제로 affine open subset $\Spec B\subseteq Y$와 그 image를 담는 $\Spec A\subseteq S$, 그리고 $\mathfrak{a}=\mathcal{J}(\Spec B)$와 $C=B/\mathfrak{a}$에 대하여 세 항은 각각 $\mathfrak{a}/\mathfrak{a}^2$과 $\Omega_{B/A}\otimes_BC$, $\Omega_{C/A}$의 associated sheaf가 되어 [명제 2](#prop2)의 sequence로 돌아간다. 

이 두 exact sequence는 미분층을 계산하는 표준 도구이므로, 위에서 이들을 도입하며 소개한 대수적 직관을 기하적으로 옮겨보자. 우리는 이미 $\Omega_{X/S}$가 base 방향을 고정한 채 fiber 방향만 함수로 생각하여 진행하는 미분이었다. 첫째 exact sequence를 살펴보기 위해 우선 $S'\rightarrow S$가 $s'$를 $s$로 보낸다 하면 $X_{s'}$는 항상 $X_s$에 속한다. 즉, 이 상황에서는 $S'$ 위에서 재는 방향이 더 좁으며 따라서 $\Omega_{X/S'}$가 $\Omega_{X/S}$의 quotient로 주어지고, 이 때 지워지는 부분은 $\psi^\ast \Omega_{S'/S}$의 image이다. 

둘째 exact sequence에서 $\mathcal{J}/\mathcal{J}^2$은 $Z$의 conormal sheaf이고, 그 dual이 $Z$가 $Y$ 안에서 가지는 normal bundle (정확히는 normal sheaf)에 해당한다. $S=\Spec A$, $Y=\Spec A[\x_1,\ldots, \x_n]$이고 $\mathcal{J}$가 $f_1,\ldots, f_r$로 생성되면 $\iota^\ast\Omega_{Y/S}$가 $\dd{\x_1},\ldots, \dd{\x_n}$을 기저로 가지고 $\bar{d}$가 $f_j\mapsto\sum_i(\partial f_j/\partial \x_i)\dd{\x_i}$이므로, 이 morphism을 그 기저로 적은 행렬이 곧 Jacobian $(\partial f_j/\partial \x_i)$이다. 즉 $Z$ 위의 미분은 ambient의 미분에서 방정식들의 미분이 생성하는 부분, 곧 $Z$에 수직인 방향을 quotient하여 얻어지며, 한 점에서 이를 dualize하면 [\[대수다양체\] §접공간과 매끄러움, ⁋명제 2](/ko/math/algebraic_varieties/tangent_spaces_and_smoothness#prop2)의 묘사로 돌아온다.

## Tangent sheaf와 Zariski 접공간

Cotangent sheaf의 dual을 취하면 tangent vector들의 sheaf를 얻는다. 이는 variety 위에서 tangent bundle에 해당하는 대상이다.

::: 정의 7
Scheme morphism $\varphi:X \rightarrow S$에 대하여, $X$의 *tangent sheaf<sub>접층</sub>*를

$$\mathcal{T}_{X/S}=\sHom_{\mathcal{O}_X}(\Omega_{X/S}, \mathcal{O}_X)$$

로 정의한다. ([§준연접층, ⁋정의 2](/ko/math/scheme_theory/quasicoherent_sheaves#def2))
:::

이 정의가 하는 일을 보기 위해 다시 affine case를 보자. $X=\Spec B$와 $S=\Spec A$에 대하여 [정의 4](#def4)는 $\Omega_{X/S}=\widetilde{\Omega_{B/A}}$를 준다. 이것으로 만들어진 $\sHom$의 global section은 $\mathcal{O}_X$-module homomorphism들이므로, $\mathcal{T}_{X/S}$의 global section은 $\Hom_{\mathcal{O}_X}(\widetilde{\Omega_{B/A}}, \widetilde B)\cong\Hom_B(\Omega_{B/A}, B)$이고 ([§준연접층, ⁋정리 7](/ko/math/scheme_theory/quasicoherent_sheaves#thm7)), 따라서 정의로부터

$$\mathcal{T}_{X/S}(X)\cong \Der_A(B, B)$$

를 얻는다. ([\[가환대수학\] §미분, ⁋보조정리 2](/ko/math/commutative_algebra/differentials#lem2)) 같은 계산을 principal open $D(g)$ 위에서 반복하면 [명제 3](#prop3)의 첫째 주장에 의하여 $\Der_A(B_g, B_g)$가 나오므로, $\mathcal{T}_{X/S}$는 $B$의 $A$-derivation들을 국소적으로 모아 놓은 sheaf이며 이들을 붙이면 일반적인 경우 또한 얻는다. 

$\Omega_{B/A}$는 정의에 의해 $1$차 differential form에 해당한다. 그럼 위에서 정의한 $\Der_A(B,B)$는 이것의 dual, 즉 tangent vector에 해당하는 것이다. 구체적으로 임의의 함수 $b\in B$가 주어졌을 때, $\Der_A(B,B)$의 원소 $D$는 그 미분값 $D(b)$를 주며, universal property 아래에서 이 대응은 $\dd{b}\mapsto D(b)$로 정해지는 $B$-linear map $\Omega_{B/A} \rightarrow B$와 같은 것이다. ([\[가환대수학\] §미분, ⁋보조정리 2](/ko/math/commutative_algebra/differentials#lem2)) 즉 $\Der_A(B, B)$는 정의상 $\Omega_{B/A}$의 dual module $\Hom_B(\Omega_{B/A}, B)$이고, 두 module 사이에는 $B$-bilinear pairing

$$\langle -, -\rangle:\Omega_{B/A}\times \Der_A(B, B) \rightarrow B; \qquad \langle \dd{b}, D\rangle=D(b)$$

이 존재한다. 이 때 $\Omega_{B/A}$가 $\dd{b}$ 꼴의 원소들로 생성되므로 이 pairing은 위의 식만으로 결정되며, $D$를 고정하고 $b$를 움직이면 $D$가 정하는 방향으로 함수들을 미분하는 연산을 얻고 거꾸로 $b$를 고정하고 $D$를 움직이면 $\dd{b}$가 각 방향마다 $b$의 변화율을 대응시키는 함수가 된다. 이는 미분다양체 위에서 벡터장이 함수에 그 도함수를 대응시키고 $1$차 differential form이 벡터장을 대입받아 함수를 내놓는 것과 같은 구조이다. 이 pairing이 dual basis를 주는 모습은 $B=A[\x_1,\ldots, \x_n]$에서 곧바로 보인다. 이 경우 $\Omega_{B/A}$는 $\dd{\x_1},\ldots, \dd{\x_n}$을 기저로 하는 free module이고 ([\[가환대수학\] §미분, ⁋명제 5](/ko/math/commutative_algebra/differentials#prop5)), $A$-derivation $D$는 $A$-linearity와 Leibniz 법칙에 의하여 $\x_i$에서의 값 $D(\x_i)$들로 완전히 결정되며 이들을 dual basis를 사용하여 적으면 $D=\sum_iD(\x_i)\partial/\partial \x_i$로 적힌다.

한편 $\Omega_{B/A}$가 free module일 때에는 이렇게 두 module이 서로의 dual이 되지만, 일반적으로는 dual을 취하며 정보가 사라진다. 앞서 본 $A=\mathbb{K}[t]$와 $B=\mathbb{K}[t, \x, \y]/(\x\y-t)$의 경우 $A$-derivation은 $t$를 죽여야 하므로 $\x D(\y)+\y D(\x)=0$을 만족해야 하고, $B\cong \mathbb{K}[\x, \y]$에서 이 방정식의 해는 $w\in B$에 대한 $D(\x)=\x w$와 $D(\y)=-\y w$뿐이다. 즉 $\Der_A(B, B)$는 $\x\partial/\partial \x-\y\partial/\partial \y$를 기저로 하는 rank $1$의 free module로, 원점에서 rank가 $2$로 뛰던 $\Omega_{B/A}$와 달리 어디에서나 rank가 $1$이다. 그러므로 $\mathcal{T}_{X/S}$에서 $\Omega_{X/S}$를 되찾을 수는 없으며, universal property 등의 형식적인 정의 뿐만 아니라 이러한 정보의 차이가 cotangent sheaf를 더 자연스러운 것으로 만든다. 

이 때문에 한 점에서의 tangent space를 계산할 때도 주의가 필요하다. $\mathbb{K}$-scheme $X$의 점 $x$에 대하여, residue field를 $\kappa(x)$라 하면 ([§스킴, ⁋정의 5](/ko/math/scheme_theory/schemes#def5)) cotangent sheaf의 fiber $\Omega_{X/\mathbb{K}}\otimes_{\mathcal{O}_X}\kappa(x)$를 생각할 수 있다. Dual을 먼저 취한 후 fiber를 취하여 얻어지는 fiber

$$\mathcal{T}_{X/\mathbb{K}}\otimes_{\mathcal{O}_X}\kappa(x)$$

를 생각하면, canonical map 

$$\mathcal{T}_{X/\mathbb{K}}\otimes_{\mathcal{O}_X}\kappa(x) \rightarrow \bigl(\Omega_{X/\mathbb{K}}\otimes_{\mathcal{O}_X}\kappa(x)\bigr)^\vee$$

은 항상 존재하며 $\Omega_{X/\mathbb{K}}$가 $x$ 근방에서 locally free이면 이는 isomorphism이지만, 일반적으로 이는 단사도 전사도 아니다. 앞서 본 $\x\y=t$의 family가 그 차이를 보여주는데, $\mathcal{T}_{X/S}$는 $\x\partial/\partial \x-\y\partial/\partial \y$가 생성하는 rank $1$의 free module이라 원점 $p$에서의 fiber가 $1$차원이지만, 이 derivation 자체가 $p$에서 소멸하므로 위의 canonical map은 zero map이 되고, 반면 $\Omega_{X/S}\otimes\kappa(p)$의 dual은 fiber $X_0$의 원점에서의 tangent space인 $2$차원 vector space이다. 

따라서 이 두 정의 중 올바른 것은 다음의 정의이다.

::: 정의 8
Field $\mathbb{K}$ 위의 scheme $X$와 그 점 $x\in X$에 대하여, $x$에서의 *Zariski tangent space<sub>자리스키 접공간</sub>*를

$$T_xX=\bigl(\Omega_{X/\mathbb{K}}\otimes_{\mathcal{O}_X}\kappa(x)\bigr)^\vee=\Hom_{\kappa(x)}\bigl(\Omega_{X/\mathbb{K}}\otimes_{\mathcal{O}_X}\kappa(x), \kappa(x)\bigr)$$

로 정의한다.
:::

이 정의는 variety 위에서 local ring의 maximal ideal로 주었던 묘사와 일치한다. ([\[대수다양체\] §접공간과 매끄러움, ⁋정의 1](/ko/math/algebraic_varieties/tangent_spaces_and_smoothness#def1)) $x$가 residue field $\kappa(x)=\mathbb{K}$를 가지는 점, 곧 $\mathbb{K}$-rational point이고 $(\mathcal{O}_{X,x}, \mathfrak{m}_x)$가 그 local ring이라 하자. Conormal exact sequence를 stalk에서 분석하면 canonical map $\mathfrak{m}_x/\mathfrak{m}_x^2 \rightarrow \Omega_{X/\mathbb{K}}\otimes\kappa(x)$가 전사임을 얻는데, 이 sequence는 왼쪽에서 exact일 이유가 없으므로 단사성은 다른 곳에서 와야 한다. 그것을 주는 것이 $\mathbb{K}$-rational이라는 가정으로, 이 경우 $\mathcal{O}_{X,x} \rightarrow \kappa(x)=\mathbb{K}$가 $\mathbb{K}$-algebra homomorphism으로서 갈라지므로 $f\mapsto (f-\bar f)+\mathfrak{m}_x^2$가 $\mathbb{K}$-derivation이 되어 위 map의 역을 유도하고, 따라서 $\Omega_{X/\mathbb{K}}\otimes \kappa(x)\cong \mathfrak{m}_x/\mathfrak{m}_x^2$이 성립한다. 그럼 Zariski tangent space는 $(\mathfrak{m}_x/\mathfrak{m}_x^2)^\vee$, 즉 cotangent space $\mathfrak{m}_x/\mathfrak{m}_x^2$의 쌍대이다. 한 점에서의 차원 $\dim_{\kappa(x)}T_xX$가 그 점의 국소적 차원 $\dim \mathcal{O}_{X,x}$과 같은지 여부가 그 점이 nonsingular한지를 가르는 기준이 되며, $\mathcal{O}_{X,x}$가 Noetherian이면 일반적으로 $\dim_{\kappa(x)}T_xX\geq \dim \mathcal{O}_{X,x}$이다.

## 아핀공간과 사영공간의 미분층

우선 우리의 가장 단순한 예시는 다음과 같다. 

::: 명제 9
Ring $A$에 대하여, affine space $\mathbb{A}^n_A=\Spec A[\x_1,\ldots, \x_n]$의 cotangent sheaf $\Omega_{\mathbb{A}^n_A/A}$는 rank $n$의 free sheaf

$$\Omega_{\mathbb{A}^n_A/A}\cong \mathcal{O}_{\mathbb{A}^n_A}^{\oplus n}$$

이며, $\dd{\x_1},\ldots, \dd{\x_n}$을 기저로 가진다.
:::
::: 증명
$B=A[\x_1,\ldots, \x_n]$이라 하자. [정의 4](#def4)에 의하여 $\Omega_{\mathbb{A}^n_A/A}\cong \widetilde{\Omega_{B/A}}$이므로 $\Omega_{B/A}$가 $\dd{\x_1},\ldots, \dd{\x_n}$을 기저로 하는 free $B$-module임을 보이면 된다.

$\Omega_{B/A}$는 정의에 의하여 원소들 $\dd{f}$ ($f\in B$)로 생성되는데, $d$가 $A$-derivation이므로 임의의 다항식 $f$에 대하여 chain rule

$$\dd{f}=\sum_{i=1}^n\frac{\partial f}{\partial \x_i}\dd{\x_i}$$

가 성립한다. 따라서 $\Omega_{B/A}$는 $\dd{\x_1},\ldots, \dd{\x_n}$으로 생성된다. 한편 이들이 $B$ 위에서 일차독립임을 보이기 위해, 각 $j$에 대하여 $j$번째 편미분 $\partial/\partial \x_j:B \rightarrow B$가 $A$-derivation임을 이용한다. 이는 universal property에 의하여 $B$-linear map $\partial_j:\Omega_{B/A} \rightarrow B$를 유도하며 $\partial_j(\dd{\x_i})=\delta_{ij}$이므로, $\sum_i b_i \dd{\x_i}=0$이면 $\partial_j$를 적용하여 $b_j=0$을 얻는다. 그러므로 $\dd{\x_1},\ldots, \dd{\x_n}$은 자유 기저이고 $\Omega_{B/A}\cong B^{\oplus n}$이다.
:::

Base가 affine이 아니어도 마찬가지의 결과가 성립한다. 임의의 scheme $S$는 유일한 방식으로 $\Spec \mathbb{Z}$ 위의 scheme이므로, $S$ 위의 *relative affine space*를 base change

$$\mathbb{A}^n_S=\Spec \mathbb{Z}[\x_1,\ldots, \x_n]\times_{\Spec \mathbb{Z}}S$$

로 정의할 수 있고, 그럼 $S$의 affine open subset $\Spec A$ 위에서 이것이 주는 것은 $\mathbb{A}^n_A$이다. ([§올곱, ⁋예시 9](/ko/math/scheme_theory/fiber_products#ex9)) 그런데 [정의 4](#def4)에 의하여 cotangent sheaf는 base의 affine open subset마다의 local model로 결정되므로, 각 chart에 위의 명제를 적용하면 $\Omega_{\mathbb{A}^n_S/S}\cong \mathcal{O}_{\mathbb{A}^n_S}^{\oplus n}$을 얻는다.

즉, affine space 위에서 cotangent sheaf는 좌표함수의 미분이 basis를 이루는 trivial bundle이다. Projective space로 넘어가면 상황이 더 흥미로워지는데, $\mathbb{P}^n$의 cotangent sheaf는 더 이상 free는 아니지만 twisting sheaf들 사이의 short exact sequence, 곧 Euler exact sequence로 표현된다.

::: 정리 10 (Euler exact sequence)
Ring $A$ 위의 projective space $\mathbb{P}^n_A=\Proj A[\x_0,\ldots, \x_n]$에 대하여 ([§사영공간과 Proj 구성, ⁋정의 1](/ko/math/scheme_theory/projective_schemes#def1)), $\mathcal{O}_{\mathbb{P}^n_A}$-module들의 short exact sequence

$$0 \rightarrow \Omega_{\mathbb{P}^n_A/A} \rightarrow \mathcal{O}_{\mathbb{P}^n_A}(-1)^{\oplus(n+1)} \rightarrow \mathcal{O}_{\mathbb{P}^n_A} \rightarrow 0$$

이 존재한다.
:::
::: 증명
표기의 편의를 위해 $\mathbb{P}^n=\mathbb{P}^n_A$로 줄여 적고 standard affine open $U_i=D_+(\x_i)\cong \Spec A[\x_0,\ldots, \x_n]_{(\x_i)}$ 위에서 작업한다. 이 coordinate ring은 $\y^{(i)}_j=\x_j/\x_i$ ($j\neq i$)를 변수로 하는 $n$변수 polynomial ring이므로 $U_i$는 $A$ 위의 affine space $\mathbb{A}^n_A$이고, 따라서 $\Omega_{\mathbb{P}^n/A}\vert_{U_i}$는 [명제 9](#prop9)에 의하여 $\dd{\y}^{(i)}_j$ ($j\neq i$)를 basis로 하는 rank $n$ free sheaf이다.

우선 morphism $\mathcal{O}(-1)^{\oplus(n+1)} \rightarrow \mathcal{O}$를 정의하자. $\mathcal{O}(-1)$의 section에 $\x_i$를 곱하면 $\mathcal{O}$로 가게 되며, 이러한 방식으로 다음의 morphism

$$\mathcal{O}_{\mathbb{P}^n_A}(-1)^{\oplus(n+1)}\rightarrow \mathcal{O}_{\mathbb{P}^n_A};\qquad (s_0,\ldots, s_n)=\sum_{j=0}^n s_je_j\mapsto \sum_{j=0}^n s_j\x_j\tag{$\ast$}$$

을 생각하면 각각의 $U_i$ 위에서 $\x_i^{-1}e_i$가 $1$로 옮겨가므로 이는 surjective이다.

이제 exact sequence를 완성하기 위해 kernel을 계산하자. 각각의 $U_i$ 위에서 $\mathcal{O}(-1)$을 $\x_i^{-1}$로 trivialize하면 위 morphism은 

$$(s_0,\ldots, s_n)\mapsto \sum_j s_j (\x_j/\x_i)$$

로 주어지므로, 그 kernel은 $\sum_j s_j(\x_j/\x_i)=0$을 만족하는 $(s_0,\ldots, s_n)$들로 이루어진다. 이 때, $i$번째 성분의 계수는 $\x_i/\x_i=1$이므로 다른 성분들로부터 $s_i$가 유일하게 결정되며, 나머지 $s_j$들은 자유롭게 움직일 수 있다. 즉 kernel은 $j\neq i$인 $s_j$들이 자유롭게 움직이는 rank $n$ free module이다.

이제 $U_i$ 위에서 morphism $\Omega_{\mathbb{P}^n/A}\vert_{U_i} \rightarrow \mathcal{O}(-1)^{\oplus(n+1)}\vert_{U_i}$을

$$d\Bigl(\frac{\x_j}{\x_i}\Bigr)\longmapsto \frac{1}{\x_i}\Bigl(e_j-\frac{\x_j}{\x_i}e_i\Bigr)$$

로 정의하면, 우변을 $(\ast)$로 보낸 값이 

$$\frac{1}{\x_i}\left(\x_j-\frac{\x_j}{\x_i}\x_i\right)=0$$

이므로 그 image는 방금 계산한 kernel 안에 있다. 또 양쪽 모두 $j\neq i$로 첨자가 매겨진 rank $n$ free module이고 basis가 basis로 옮겨지므로, 위 morphism의 image가 정확히 ($\ast$)의 kernel과 일치한다. 이렇게 국소적으로 정의한 morphism들은 $U_i\cap U_k$ 위에서 서로 일치하는데, 실제로 두 식 

$$\frac{\x_l}{\x_i}=\frac{\x_l}{\x_k}\cdot\frac{\x_k}{\x_i},\qquad d\Bigl(\frac{\x_k}{\x_i}\Bigr)=-\Bigl(\frac{\x_k}{\x_i}\Bigr)^2d\Bigl(\frac{\x_i}{\x_k}\Bigr)$$

를 써서 $\dd{(\x_l/\x_i)}$를 $U_k$ 쪽 기저로 전개한 뒤 위의 대응을 적용하면 $e_k$ 항이 상쇄되어 $\x_i^{-2}(\x_ie_l-\x_le_i)$를 얻으므로, $U_i$ 쪽 값과 같다. 그러므로 이들은 global한 morphism $\Omega_{\mathbb{P}^n/A} \rightarrow \mathcal{O}(-1)^{\oplus(n+1)}$로 붙어서 exact sequence를 만들고, exactness는 local property이므로 이들이 sheaf의 short exact sequence를 이룬다.
:::

[명제 9](#prop9)에서와 같이 base를 임의의 scheme으로 올릴 수도 있다. $\mathbb{P}^n_S=\mathbb{P}^n_\mathbb{Z}\times_{\Spec \mathbb{Z}}S$와 그 projection $\pi:\mathbb{P}^n_S \rightarrow \mathbb{P}^n_\mathbb{Z}$에 대하여 $\mathcal{O}_{\mathbb{P}^n_S}(d)=\pi^\ast\mathcal{O}_{\mathbb{P}^n_\mathbb{Z}}(d)$로 정의하면, 각 chart 위의 generator $\x_i^d$와 transition function $(\x_i/\x_j)^d$가 그대로 옮겨간다. 특히 이는 base가 affine일 때에는 [§스킴의 층 코호몰로지, ⁋정의 5](/ko/math/scheme_theory/sheaf_cohomology_of_schemes#def5)의 twisting sheaf와 일치하며, 또 [명제 5](#prop5)에 의하여 $\Omega_{\mathbb{P}^n_S/S}\cong\pi^\ast\Omega_{\mathbb{P}^n_\mathbb{Z}/\mathbb{Z}}$이다. 한편 [정리 10](#thm10)을 $A=\mathbb{Z}$에 적용하여 얻는 sequence

$$0 \rightarrow \Omega_{\mathbb{P}^n_\mathbb{Z}/\mathbb{Z}} \rightarrow \mathcal{O}_{\mathbb{P}^n_\mathbb{Z}}(-1)^{\oplus(n+1)} \rightarrow \mathcal{O}_{\mathbb{P}^n_\mathbb{Z}} \rightarrow 0$$

를 생각하면, 우리는 이미 위의 증명에서 $\Omega_{\mathbb{P}^n_\mathbb{Z}/\mathbb{Z}}$가 각 $U_i$ 위에서 rank $n$ free sheaf인 것을 확인하였고, 나머지 두 개의 sheaf 또한 정의에 의하여 locally free이고, 특히 마지막 $\mathcal{O}_{\mathbb{P}^n_\mathbb{Z}}$의 경우 free이므로 projective이며 ([\[다중선형대수학\] §사영가군, 단사가군, 평탄가군, ⁋명제 4](/ko/math/multilinear_algebra/various_modules#prop4)), 따라서 각 $U_i$ 위에서 이 sequence는 split한다. ([\[다중선형대수학\] §완전열, ⁋명제 10](/ko/math/multilinear_algebra/exact_sequences#prop10)) 그런데 split exact sequence는 additive functor가 보존하고 exactness는 local property이므로, $\pi^\ast$를 취하면 임의의 scheme $S$에 대하여 Euler exact sequence

$$0 \rightarrow \Omega_{\mathbb{P}^n_S/S} \rightarrow \mathcal{O}_{\mathbb{P}^n_S}(-1)^{\oplus(n+1)} \rightarrow \mathcal{O}_{\mathbb{P}^n_S} \rightarrow 0$$

을 얻는다.

## Canonical sheaf

Cotangent sheaf가 locally free일 때, 그 top exterior power는 rank $1$의 sheaf, 곧 invertible sheaf가 된다. 이렇게 얻어지는 단 하나의 invertible sheaf가 $X$의 기하를 상당 부분 통제하며, variety의 세계에서 이는 cotangent bundle의 top exterior power로 정의한 canonical line bundle에 해당한다. ([\[대수다양체\] §표준선다발, ⁋정의 5](/ko/math/algebraic_varieties/canonical_bundle#def5)) 우리는 scheme의 경우에도 이미 $\mathcal{O}_X$-module의 exterior power $\bigwedge^r\mathcal{F}$를 열린집합마다의 exterior power를 sheafification하여 정의하였고 ([§준연접층, ⁋정의 2](/ko/math/scheme_theory/quasicoherent_sheaves#def2)), 이것이 quasi-coherence를 보존하며 rank $n$의 locally free sheaf $\mathcal{E}$에 대하여 $\bigwedge^r\mathcal{E}$가 rank $\binom{n}{r}$의 locally free sheaf임을 보았다. 특히 $r=n$인 경우의 determinant $\det\mathcal{E}=\bigwedge^n\mathcal{E}$는 invertible sheaf이다. ([§준연접층, §§Locally free sheaf와 invertible sheaf](/ko/math/scheme_theory/quasicoherent_sheaves#locally-free-sheaf와-invertible-sheaf))

::: 정의 11
Field $\mathbb{K}$ 위의 scheme $X$에 대하여 cotangent sheaf $\Omega_{X/\mathbb{K}}$가 rank $n$의 locally free sheaf라 하자. 그럼 $X$의 *canonical sheaf* $\omega_X$를 top exterior power

$$\omega_X=\bigwedge\nolimits^n\Omega_{X/\mathbb{K}}=\det\Omega_{X/\mathbb{K}}$$

로 정의한다.
:::

앞의 관찰에 의하여 $\omega_X$는 invertible sheaf이다. 더 일반적으로 scheme morphism $\varphi:X \rightarrow S$에 대하여 $\Omega_{X/S}$가 rank $n$의 locally free sheaf일 때 *relative canonical sheaf* $\omega_{X/S}=\det\Omega_{X/S}$를 같은 식으로 정의하며, $S=\Spec \mathbb{K}$인 경우가 위와 같이 absolute case이다. 

Canonical sheaf를 실제로 계산할 때 쓰는 도구는 determinant가 short exact sequence를 따라 tensor product로 분해된다는 사실이다.

::: 명제 12
Scheme $X$ 위의 locally free sheaf들의 short exact sequence

$$0 \rightarrow \mathcal{E}' \rightarrow \mathcal{E} \rightarrow \mathcal{E}'' \rightarrow 0$$

이 주어지고 $\mathcal{E}'$과 $\mathcal{E}''$의 rank가 각각 $r$과 $s$라 하자. 그럼 $\mathcal{E}$는 rank $r+s$의 locally free sheaf이며, isomorphism

$$\det\mathcal{E}\cong \det\mathcal{E}'\otimes_{\mathcal{O}_X}\det\mathcal{E}''$$

이 존재한다.
:::
::: 증명
먼저 rank를 확인한다. $\mathcal{E}''$이 locally free이므로 각 점은 $\mathcal{E}''\vert_U\cong\mathcal{O}_U^{\oplus s}$이고 $\mathcal{E}'\vert_U\cong\mathcal{O}_U^{\oplus r}$인 열린근방 $U$를 가진다. Sheaf의 surjection이 보장하는 것은 stalk 수준의 전사뿐이므로, $\mathcal{E}''\vert_U$의 각 기저 section을 $\mathcal{E}$의 section으로 들어올리려면 $U$를 더 줄여야 한다. 기저가 유한하므로, 각 section이 올라가는 열린근방들을 교차하여 그러한 $U$를 다시 얻는다. 그렇게 줄인 $U$ 위에서 $\mathcal{E}''\vert_U$의 기저 section들을 $\mathcal{E}\vert_U$로 들어올리면 surjection $\mathcal{E}\vert_U \rightarrow \mathcal{E}''\vert_U$의 splitting을 얻으므로 $\mathcal{E}\vert_U\cong\mathcal{E}'\vert_U\oplus\mathcal{O}_U^{\oplus s}\cong\mathcal{O}_U^{\oplus(r+s)}$이고, 따라서 $\mathcal{E}$는 rank $r+s$의 locally free sheaf이다.

이제 morphism

$$\lambda:\det\mathcal{E}'\otimes_{\mathcal{O}_X}\det\mathcal{E}'' \rightarrow \det\mathcal{E}$$

를 구성한다. 열린집합 $V$ 위의 section $\alpha\in(\det\mathcal{E}')(V)$과 $\bar t_1\wedge\cdots\wedge\bar t_s\in(\det\mathcal{E}'')(V)$이 주어졌을 때, $V$를 충분히 줄여 각 $\bar t_i$를 $t_i\in\mathcal{E}(V)$로 들어올린 뒤

$$\lambda\bigl(\alpha\otimes(\bar t_1\wedge\cdots\wedge\bar t_s)\bigr)=\alpha\wedge t_1\wedge\cdots\wedge t_s$$

로 정의한다. 여기에서 우변의 $\alpha$는 inclusion $\mathcal{E}'\hookrightarrow\mathcal{E}$가 유도하는 $\det\mathcal{E}' \rightarrow \bigwedge^r\mathcal{E}$를 통해 옮긴 section을 뜻한다. 이 값은 lift의 선택에 무관하다. 두 lift의 차가 $\mathcal{E}'$의 section이므로, $t_i$를 $t_i+a_i$ ($a_i\in\mathcal{E}'(V)$)로 바꿀 때 생기는 차이는 적어도 하나의 $a_i$를 인수로 가지는 항들의 합이다. 그런데 국소 splitting 위에서 $\alpha$는 $\mathcal{E}'\vert_V$의 기저 $f_1,\ldots, f_r$에 대한 $f_1\wedge\cdots\wedge f_r$의 배수이고 $a_i$는 $f_j$들의 $\mathcal{O}_V$-일차결합이므로, 그러한 항은 어떤 $f_j$를 두 번 포함하여 소멸한다. 그러므로 국소적으로 정의된 $\lambda$들은 겹치는 부분에서 일치하며 전역적인 morphism으로 붙는다.

$\lambda$가 isomorphism임은 국소적으로 확인하면 충분하다. 위의 $U$ 위에서 $\mathcal{E}'\vert_U$의 기저를 $f_1,\ldots, f_r$이라 하고 $\mathcal{E}''\vert_U$의 기저 $\bar g_1,\ldots, \bar g_s$의 lift를 $g_1,\ldots, g_s$라 하면, splitting에 의하여 $f_1,\ldots, f_r, g_1,\ldots, g_s$는 $\mathcal{E}\vert_U$의 기저이다. [\[다중선형대수학\] §텐서대수, ⁋명제 13](/ko/math/multilinear_algebra/tensor_algebras#prop13)에 의하여 $\det\mathcal{E}\vert_U$는 $f_1\wedge\cdots\wedge f_r\wedge g_1\wedge\cdots\wedge g_s$를 기저로 하는 rank $1$ free sheaf이고, 마찬가지로 $(\det\mathcal{E}'\otimes\det\mathcal{E}'')\vert_U$는 $(f_1\wedge\cdots\wedge f_r)\otimes(\bar g_1\wedge\cdots\wedge\bar g_s)$를 기저로 한다. $\lambda$는 후자의 기저를 전자의 기저로 보내므로 $U$ 위에서 isomorphism이며, 따라서 전역적으로도 isomorphism이다.
:::

이를 Euler exact sequence에 적용하면 projective space의 canonical sheaf가 곧바로 계산된다.

::: 예시 13
Field $\mathbb{K}$ 위의 projective space $\mathbb{P}^n$을 생각하자. [정리 10](#thm10)을 $A=\mathbb{K}$에 적용하면 Euler exact sequence를 얻으며, 그 증명에서 보았듯 $\Omega_{\mathbb{P}^n/\mathbb{K}}$는 각 $U_i=D_+(\x_i)$ 위에서 $\dd{\y}^{(i)}_j$ ($j\neq i$)를 기저로 하는 rank $n$의 free sheaf이므로 locally free이고, 따라서 $\omega_{\mathbb{P}^n}$이 정의된다. Euler exact sequence의 세 항 $\Omega_{\mathbb{P}^n/\mathbb{K}}$, $\mathcal{O}(-1)^{\oplus(n+1)}$, $\mathcal{O}_{\mathbb{P}^n}$의 rank는 각각 $n$, $n+1$, $1$이므로, [명제 12](#prop12)에 의하여

$$\det\bigl(\mathcal{O}(-1)^{\oplus(n+1)}\bigr)\cong \omega_{\mathbb{P}^n}\otimes_{\mathcal{O}_{\mathbb{P}^n}}\det\mathcal{O}_{\mathbb{P}^n}\cong\omega_{\mathbb{P}^n}$$

이 성립한다. 같은 명제를 direct sum에 반복 적용하면 좌변은 $\mathcal{O}(-1)^{\otimes(n+1)}$이고, $\mathcal{O}(d)$의 transition function이 $(\x_i/\x_j)^d$이므로 ([§스킴의 층 코호몰로지, ⁋정의 5](/ko/math/scheme_theory/sheaf_cohomology_of_schemes#def5) 뒤의 기술) 이는 $\mathcal{O}_{\mathbb{P}^n}(-n-1)$이다. 그러므로

$$\omega_{\mathbb{P}^n}\cong\mathcal{O}_{\mathbb{P}^n}(-n-1)$$

을 얻는다. 이는 variety 위에서 $n$-form의 transition function으로 수행한 계산과 일치한다. ([\[대수다양체\] §표준선다발, ⁋예시 8](/ko/math/algebraic_varieties/canonical_bundle#ex8))
:::

Canonical sheaf가 다른 invertible sheaf들 가운데 특별한 위치를 차지하는 까닭은, 그것이 cohomology 사이의 duality를 매개한다는 데 있다. 위상수학에서 fundamental class가 Poincaré duality를 주었듯, projective scheme 위에서는 $\omega_X$가 그 역할을 맡는다.

::: 정리 14 (Serre duality)
Algebraically closed field $\mathbb{K}$ 위의 $n$차원 integral projective scheme $X$에 대하여 ([§사영공간의 닫힌 부분스킴, ⁋정의 7](/ko/math/scheme_theory/closed_subschemes_of_projective_spaces#def7), [§스킴의 대수구조, §§축소스킴과 정역스킴](/ko/math/scheme_theory/algebra_of_schemes#축소스킴과-정역스킴)) $\Omega_{X/\mathbb{K}}$가 rank $n$의 locally free sheaf라 하자. 그럼 $X$ 위의 임의의 locally free sheaf $\mathcal{E}$와 $0\leq i\leq n$에 대하여 isomorphism

$$H^i(X, \mathcal{E})\cong H^{n-i}\bigl(X, \omega_X\otimes_{\mathcal{O}_X}\mathcal{E}^\vee\bigr)^\ast$$

이 존재한다. 여기에서 $\mathcal{E}^\vee=\sHom_{\mathcal{O}_X}(\mathcal{E}, \mathcal{O}_X)$이고, $(-)^\ast$는 유한차원 $\mathbb{K}$-벡터공간의 쌍대이다. ([§스킴의 층 코호몰로지, ⁋정리 8](/ko/math/scheme_theory/sheaf_cohomology_of_schemes#thm8))
:::

이 정리의 증명은 $\mathbb{P}^n$ 위에서 trace map과 cup product로 만든 pairing이 perfect pairing임을 보인 뒤 이를 finite surjective morphism을 따라 일반의 $X$로 옮기는 논증을 사용하는데, 구체적인 증명은 이 글의 범위를 넘어서므로 [\[대수다양체\] §세르 쌍대성, §§사영공간에서의 세르 쌍대성](/ko/math/algebraic_varieties/serre_duality#사영공간에서의-세르-쌍대성)에 위임하기로 한다. 

한편 위의 논의에서 우리는 $\Omega_{X/\mathbb{K}}$가 locally free이기를 요구하였는데, 만일 이것이 성립하지 않는다면 rank가 일정하지 않아 top exterior power를 고를 근거부터가 없어지게 된다. 이와 같은 종류의 일반화 또한 [\[대수다양체\] §세르 쌍대성, §§세르 쌍대성의 일반화](/ko/math/algebraic_varieties/serre_duality#세르-쌍대성의-일반화)에서 이미 다룬 것으로, 이 경우 정리의 isomorphism을 $\Ext$로 끌어올리고 별도의 dualizing sheaf를 도입했어야 했다. 또, 우리가 보편적으로 관심을 갖는 대상은 $\mathbb{K}=\mathbb{C}$인 경우들이므로 상대적으로 덜 중요하기는 하지만, $\mathbb{K}$가 perfect field가 아니라면 $\Omega_{X/\mathbb{K}}$의 rank와 $X$의 차원이 달라지는 문제가 생길 수 있다는 사실 자체는 기억해둘 가치가 있다. 일반적으로 $\Omega_{X/S}$의 locally free 가정은 만일 $\varphi:X\rightarrow S$가 *smooth*라면 자동으로 성립하게 되는데, 이를 살펴보는 것이 [§매끄러운 사상과 étale 사상](/ko/math/scheme_theory/smooth_and_etale_morphisms)의 목표이다. 

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate Texts in Mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundations of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).  
**[Eis]** D. Eisenbud, *Commutative algebra: with a view toward algebraic geometry*. Springer, 1995.  
**[Stacks]** The Stacks Project Authors, *The Stacks Project*. Available [online](https://stacks.math.columbia.edu/).
