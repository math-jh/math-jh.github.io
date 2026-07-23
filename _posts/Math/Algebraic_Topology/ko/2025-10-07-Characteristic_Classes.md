---
title: "벡터다발의 특성류"
description: "oriented 벡터다발의 오일러 특성류에서 출발하여 Thom 동형과 Gysin 완전열을 거쳐 천 특성류와 폰트랴긴 특성류를 정의한다."
excerpt: "오일러·천·폰트랴긴 특성류"

categories: [Math / Algebraic Topology]
permalink: /ko/math/algebraic_topology/characteristic_classes
sidebar: 
    nav: "algebraic_topology-ko"

date: 2025-10-07
weight: 11


---

## 오일러 특성류

지금까지 우리는 $\mathbb{Z}/2$-coefficient를 사용하여 orientability의 문제를 효과적으로 피해왔다. 이제 우리는 orientation까지 고려하기로 한다. $\mathbb{Z}/2$-coefficient에서는 부호를 구별할 수 없어 모든 fiber가 자동으로 "방향"을 가졌지만, $\mathbb{Z}$-coefficient로 넘어가면 $1$과 $-1$이 분명히 다른 원소가 되므로 각 fiber에 방향을 일관되게 줄 수 있는지가 문제가 되고, 그것이 가능한 경우 top Stiefel-Whitney class $w_n$을 정수로 들어올린 더 섬세한 불변량이 나타난다. 이것이 Euler class이다.

::: 정의 1
Rank $n$ vector bundle $p:E\rightarrow B$의 *orientation<sub>방향</sub>*이란, 각 fiber $p^{-1}(x)$에 방향, 즉 $H^n(p^{-1}(x), p^{-1}(x)\setminus 0;\mathbb{Z})\cong\mathbb{Z}$의 한 generator $u_x$의 선택을 각 local trivialization에서 연속적으로 부여하는 것이다. 이러한 방향이 존재하는 bundle을 *oriented vector bundle*이라 한다.
:::

방향을 주는 것은 크게 세 가지로 생각할 수 있다. 우선 첫째로, 우리는 일반적으로 vector bundle $E\rightarrow B$가 주어지면, zero section $0:B\rightarrow E$를 통해 $B$가 $E$에 들어있는 것으로 생각한다. 그럼 위의 정의에서 relative cohomology $H^n(p^{-1}(x), p^{-1}(x)\setminus 0;\mathbb{Z})$은 그 자체로는 fiber의 원점, 즉 base $B$의 해당하는 점에 $+$ 혹은 $-$라는 데이터를 붙여둔 것이다.

이는 미분기하학 등에서는 다음과 같이 해석된다. Fiber $p^{-1}(x)\cong\mathbb{R}^n$에서 원점을 뺀 것이 구면 $S^{n-1}$으로 deformation retract되므로 pair의 long exact sequence로부터 다음 isomorphism

$$H^n(p^{-1}(x), p^{-1}(x)\setminus 0;\mathbb{Z})\cong \widetilde{H}^{n-1}(S^{n-1};\mathbb{Z})\cong\mathbb{Z}$$

이 존재하는 것을 안다. 미분기하학에서 다양체의 top dimensional cohomology는 volume form을 담고 있고, 이것이 곧 방향을 결정하는 것으로 생각하므로 이는 $S^{n-1}$이라는, 우리가 잘 알고 있는 공간의 방향을 사용해서 vector bundle의 방향을 주는 것으로 생각할 수 있다. 

그러나 역시 벡터공간에 방향을 주는 가장 친숙한 방법은 기준이 되는 ordered basis를 하나 잡고, 다른 ordered basis는 기준 basis로의 change of basis 행렬식이 음수이면 음의 방향으로 정렬되어있다 선언하는 것이다. 문제는 이와 같은 정의는 과하게 많은 정보를 담고 있다는 것으로, 실제로 우리가 보는 것은 change of basis의 $\det$의 부호뿐이다. 이러한 관점은 앞서 [§슈티펠-휘트니 특성류, §§체흐 코호몰로지](/ko/math/algebraic_topology/stiefel_whitney_classes#체흐-코호몰로지)에서 설명한 Čech cohomology와 긴밀하게 연결된다. 즉, 우리는 임의의 vector bundle을 trivializing open cover $\{U_i\}$와 $U_{ij}$ 위의 transition function들 $g_{ij}: U_{ij}\rightarrow \GL(n;\mathbb{R})$로 정의했었는데, 이렇게 $\det$의 부호 중 하나를 택하는 것은 structure group을 $\GL(n;\mathbb{R})$에서 $\GL^+(n;\mathbb{R})$로 줄이는 것과 같다. 즉, transition function을 통해 한 chart에서 다른 chart로 넘어갈 때 determinant가 음수인 것, 즉 방향이 뒤바뀌는 것이 허용되지 않게 되며, 이 제한이 non-orientable vector bundle들을 걸러주는 것이다. 

이것이 언제 가능한지는 앞서 본 $\pi_0(\GL(n;\mathbb{R}))\cong \mathbb{Z}/2$가 알려준다. 즉, 각 transition function에서 방향에 관련된 정보로 남는 것은 $\det g_{ij}$의 부호 $\varepsilon_{ij}=\operatorname{sgn}\det g_{ij}:U_{ij}\rightarrow \{\pm 1\}$뿐이며, 이 때 이들을 이어붙인 class $[\varepsilon_{ij}]\in H^1(B;\mathbb{Z}/2)$가 $\GL^+$로의 축소에 대한 obstruction이 된다. 이 class가 정확히 $w_1(E)$이며 ([§슈티펠-휘트니 특성류, ⁋정의 5](/ko/math/algebraic_topology/stiefel_whitney_classes#def5)), 이는 앞서 $H^1(M;\mathbb{Z}/2)$가 covering space의 방향 정보를 담았던 것의 rank $n$ 버전으로 생각하면 된다. 즉, $E$가 orientable인 것은 정확히 $w_1(E)=0$인 것과 동치이다. 

앞으로 이 절에서 다루는 bundle은 모두 oriented인 것으로 가정한다. 이렇게 방향이 주어지면 fiber마다 흩어져 있던 generator $u_x$들이 하나의 cohomology class로 묶인다.

::: 정리 2 (Thom isomorphism)
Oriented rank $n$ vector bundle $p:E\rightarrow B$에 대하여 $E_0=E\setminus 0(B)$를 zero section을 제거한 부분공간이라 하자. 그럼 유일한 *Thom class* $u\in H^n(E, E_0;\mathbb{Z})$가 존재하여, 각 $x\in B$에 대해 $u$를 $(p^{-1}(x), p^{-1}(x)\setminus 0)$로 제한한 것이 $u_x$이다. 더 나아가, cup product와 pullback의 합성

$$H^k(B;\mathbb{Z})\xrightarrow{\ \cong\ }H^{k+n}(E, E_0;\mathbb{Z}),\qquad \alpha\longmapsto p^\ast\alpha\smile u$$

는 모든 $k$에 대하여 isomorphism이다.
:::

::: 증명
핵심만 적으면, $E$가 trivial bundle $B\times\mathbb{R}^n$일 경우 pair $(E, E_0)=(B\times\mathbb{R}^n, B\times(\mathbb{R}^n\setminus 0))$이고, Künneth formula의 relative 버전에 의하여

$$H^{k+n}(B\times\mathbb{R}^n, B\times(\mathbb{R}^n\setminus 0))\cong H^k(B)\otimes H^n(\mathbb{R}^n,\mathbb{R}^n\setminus 0)$$

이다. 그런데 우변의 둘째 인자는 $\mathbb{Z}$이고, 그 generator가 fiber의 방향 $u_x$이다. 우리가 원하는 class는 이 경우에는 $u=1\otimes u_x$로 두면 충분하며, 일반적인 경우는 trivializing open cover를 잡아 Mayer-Vietoris로 이들 isomorphism들을 이어붙이면 된다. 자세한 증명은 [MS]의 10장에 맡겨둔다.
:::

Thom class는 vector bundle $E$의 zero section 근방에 집중된 fiber 방향의 cohomology class로 이해할 수 있다. 그럼 위의 isomorphism은 $B$에 살고 있는 cohomology class $\alpha$를 $E$의 fiber 방향으로 늘려준 후 $u$와 곱해주는 것이며, 이것이 isomorphism이 된다는 것이 위 정리의 주장이다. 혹은 [§푸앵카레 쌍대성, ⁋예시 16](/ko/math/algebraic_topology/Poincare_duality#ex16)의 관점에서 보면, $u$는 zero section의 (relative) Poincaré dual로서, 위 isomorphism은 $\alpha$가 정의하는 homology class를 fiber를 따라 늘린 후, 이를 zero section과 곱하여 원래대로 돌아오는 (그러나 homology class가 이제 total space의 homology group에 살게 된) 상황으로 생각할 수 있다.

이 Thom class를 다시 base로 끌어내리면 Euler class를 얻는다.

::: 정의 3
Oriented rank $n$ vector bundle $E\rightarrow B$의 *Euler class<sub>오일러 특성류</sub>* $e(E)\in H^n(B;\mathbb{Z})$를, zero section $0:B\rightarrow E$와 [정리 2](#thm2)의 Thom class $u$에 대하여

$$e(E)=0^\ast\bigl(j^\ast u\bigr)$$

로 정의한다. 여기서 $j^\ast:H^n(E, E_0)\rightarrow H^n(E)$는 pair에서 $E$ 전체로 가는 restriction이다. 
:::

그럼 $0^\ast:H^n(E)\rightarrow H^n(B)$는 $p$가 homotopy equivalence이므로 isomorphism이다. 

위에서 우리는 Thom class가 zero section의 Poincaré dual이라는 것을 설명하였다. 그럼 Euler class $e(E)$는 이를 다시 zero section 위로 restrict한 것으로, 즉 다시 Poincaré dual로 보면 zero section을 generic section으로 살짝 밀어준 후 원래의 zero section과 intersection을 취한 것, 곧 zero section의 self-intersection이며, 이는 generic section의 vanishing locus로 생각할 수 있다. 이 직관을 엄밀하게 적으면 다음과 같다. 

::: 명제 4
Euler class는 다음을 만족한다.

1. (Naturality) 임의의 $f:B'\rightarrow B$에 대하여 $e(f^\ast E)=f^\ast e(E)$이다.
2. (Whitney) 두 oriented bundle에 대하여 $e(E\oplus F)=e(E)\smile e(F)$이다.
3. (Vanishing) $E$가 어디서도 $0$이 되지 않는 section을 가지면 $e(E)=0$이다. 특히 trivial bundle은 $e=0$이다.
4. (Mod 2 환원) $e(E)$의 $\mathbb{Z}/2$-환원은 [§슈티펠-휘트니 특성류, ⁋정의 5](/ko/math/algebraic_topology/stiefel_whitney_classes#def5)의 top Stiefel-Whitney class $w_n(E)$이다.
5. (방향 반전) 방향을 뒤집으면 $e(E)$의 부호가 바뀐다. 따라서 $n$이 홀수이면 $2e(E)=0$이다.
:::
::: 증명
(1)은 Thom class가 pullback과 호환되는 데서, (2)는 두 bundle의 Thom class의 external product가 Whitney sum의 Thom class가 되는 데서 나온다 ([MS] §9–10).

(3)을 보자. 어디서도 $0$이 아닌 section $s':B\rightarrow E_0$이 존재한다 하자. 직선 homotopy $t\mapsto t\cdot s'$는 $E$ 안에서 zero section $0$과 $s'$를 잇는 homotopy이므로 $0^\ast=s'^\ast:H^n(E)\rightarrow H^n(B)$이다. 한편 $s'$은 $i:E_0\hookrightarrow E$를 거쳐 가는데, pair의 long exact sequence에서 합성 $H^n(E, E_0)\xrightarrow{j^\ast}H^n(E)\xrightarrow{i^\ast}H^n(E_0)$이 $0$이므로 $i^\ast(j^\ast u)=0$, 곧 $j^\ast u$가 $E_0$ 위에서 소멸한다. $s'$이 $E_0$를 거치므로 $s'^\ast(j^\ast u)=0$이고, 따라서 $e(E)=0^\ast(j^\ast u)=s'^\ast(j^\ast u)=0$이다.

(4)는 Thom class의 $\mathbb{Z}/2$-환원이 정확히 Stiefel-Whitney class를 정의하는 Thom class이기 때문이며 ([MS] §8), restriction이 환원과 교환하므로 $e(E)\bmod 2=w_n(E)$이다. (5)에서 fiber마다 방향을 뒤집으면 모든 $u_x$의 부호가 바뀌어 $u\mapsto -u$, 따라서 $e\mapsto -e$이다. $n$이 홀수이면 fiber의 반사 $v\mapsto -v$가 행렬식 $(-1)^n=-1$로 방향을 뒤집는 bundle automorphism을 주므로, 이 automorphism이 $e=-e$를 강제하여 $2e(E)=0$이다.
:::

[명제 4](#prop4)의 다섯 성질은 모두 앞서 본 그림, 곧 $e(E)$가 generic section의 zero locus를 부호까지 담아 적은 Poincaré dual이라는 데서 읽힌다. 다소 형식적인 앞의 두 조건을 제외하면, 나머지 셋은 부호와 obstruction의 이야기이다.

가령 셋째 조건은 만일 어디서도 $0$이 아닌 section이 있으면 generic section도 영점 없이 고를 수 있어 self-intersection이 없어지고, 따라서 $e(E)=0$이 된다는 것이다. 주의할만한 그림은 $S^1$ 위에 trivial line bundle을 두 번 꼬아 붙인 것으로, 이 bundle의 generic section은 zero section과 두 번 만나지만, 만나는 방향이 서로 반대이므로 이들이 상쇄되어 $0$이 된다.

넷째 주장의 경우, $\mathbb{Z}$ 위에서는 generic section의 zero locus를 부호까지 세지만 $\mathbb{Z}/2$로 내리면 그 부호를 잊는다는 것이다. 그럼 부호 없이 센 영점 개수가 정확히 top Stiefel-Whitney class $w_n$이므로, $e(E)$는 $w_n$을 부호까지 기억하도록 정수로 들어올린 것이고, 그 역과정이 mod $2$를 취하는 것이다. 

다섯째 주장의 경우, 방향을 뒤집으면 모든 영점의 부호가 함께 뒤집혀 $e\mapsto -e$가 되고, 특히 $n$이 홀수이면 fiber마다의 반사 $v\mapsto -v$가 행렬식 $(-1)^n=-1$로 방향을 뒤집는 bundle automorphism이라 $e=-e$를 강제하므로 $2e(E)=0$, 곧 홀수 rank oriented bundle의 Euler class는 언제나 2-torsion이라는 것을 곧바로 얻을 수 있다.

Euler class라는 이름은 그것이 재는 양에서 온다. $M$이 closed oriented $n$-manifold이고 $E=TM$이 그 tangent bundle이면, $e(TM)$을 [§푸앵카레 쌍대성, ⁋정의 10](/ko/math/algebraic_topology/Poincare_duality#def10)의 fundamental class $[M]$ 위에서 evaluate한 값이 정확히 Euler characteristic 

$$\rchi(M)=\int_{[M]} e(TM)$$

이다. 즉, Euler class는 이 bundle이 nonvanishing section을 허락하는지, 그러지 못한다면 얼마나 방해하는지를 재는 obstruction이며, tangent bundle의 경우 그 답이 위상적 불변량 $\rchi(M)$으로 나타났던 것이다.

이를 $S^2$에서 구체적으로 확인해 보자. 가령 [§사상의 차수와 Brouwer·Lefschetz 고정점 정리, ⁋정리 8](/ko/math/algebraic_topology/degree_and_fixed_point_theorems#thm8)으로부터 우리는 $TS^2$의 임의의 section은 항상 $0$이 되는 곳이 있다는 것을 안다. 예를 들어, $S^2$이 다음의 식

$$S^2=\{(x,y,z): x^2+y^2+z^2=1\}$$

으로 $\mathbb{R}^3$에 들어있다 하고, 이 위에 정의된 높이함수 $z$를 생각하자. 그럼 이 $z$의 gradient vector $\nabla z$는 tangent bundle로의 section

$$(\nabla z)_{(x,y,z)}=(-xz,-yz,x^2+y^2)$$

으로 주어지며, 실제로 이 section은 $(x,y,z)=(0,0,\pm 1)$인 곳에서 $0$이 되는 것을 안다. 이 section이 zero section과 transverse하게 만나고, 두 교점이 모두 양의 방향으로 만나는 것을 확인할 수 있으므로 Euler class는 $2\in H^2(S^2; \mathbb{Z})$가 되어야 한다. 실제로 우리가 잘 알고 있는 Euler characteristic의 계산을 활용하면 $\rchi(S^2)=2$임을 구할 수 있으므로 이것이 실제로 우리의 직관을 뒷받침하는 것을 확인할 수 있다. 

## 천 특성류

지금까지의 Stiefel-Whitney class와 Euler class는 모두 real vector bundle의 불변량이었다. 우리는 이제 complex vector bundle 위로 관심을 돌린다. 물론 임의의 complex vector space는 실수부와 허수부를 분리하여 real vector space로 볼 수 있지만, complex vector space들 사이의 자연스러운 morphism은 $\GL(2n;\mathbb{R})$이 아닌 $\GL(n;\mathbb{C})$이기 때문에 이 차이가 많은 것들을 바꾼다.

가령 $\GL(2n;\mathbb{R})$은 connected가 아니지만, $\GL(n;\mathbb{C})$는 connected이므로 임의의 complex vector bundle은 항상 orientable이다. 직관적으로 이는 한 fiber $V\cong\mathbb{C}^n$에서 일어나는 일만 보아도 충분한데, 이 fiber에 대한 (complex) basis

$$v_1,\ldots,v_n$$

를 잡으면, isomorphism $\mathbb{C}^n\cong \mathbb{R}^{2n}$은 자연스럽게 real basis 

$$v_1,iv_1,\ldots,v_n,iv_n$$

를 준다. 우리의 주장은 complex basis를 다르게 잡았을 때도 이 방향이 보존된다는 것으로, 이는 두 basis를 잇는 행렬 $A\in\GL(n;\mathbb{C})$를 real linear map으로 보면 그 실수 행렬식이

$$\det\nolimits_{\mathbb{R}}(A)=\lvert\det\nolimits_{\mathbb{C}}(A)\rvert^2>0$$

이기 때문이다. 가령, 가장 단순한 $n=1$의 경우 $z=a+bi$의 곱셈은 실수 행렬로 보면 

$$\begin{pmatrix}a&-b\\ b&a\end{pmatrix}$$

이고 그 행렬식은 $a^2+b^2>0$이며, 일반적인 $A$도 이러한 방식으로 행렬식이 항상 양수가 되게 된다. 즉, complex vector space의 change of basis는 항상 방향을 보존하므로, $V$에 (real vector space로서는) 표준적인 방향이 존재하며, 우리가 위에서 한 계산이 실은 정확히 $\GL(n;\mathbb{C})\subset \GL^+(2n; \mathbb{R})$이라는 것이다. 

특히 임의의 complex vector bundle에는 Euler class가 표준적으로 잘 정의된다. 뿐만 아니라, 여기서는 Euler class 외에 추가적인 불변량 또한 존재한다. 예를 들어 complex vector bundle $E$와 그 켤레 $\bar{E}$는 underlying real vector bundle로는 같지만, 이는 complex vector bundle로서는 일반적으로 다른 bundle이며, 우리가 정의할 *Chern class*들이 이 둘을 구별할 수 있다. 

Chern class는 top Chern class에서는 $c_n=e(E_\mathbb{R})$를 만족하므로, Euler class를 확장하는 characteristic class로 생각할 수 있다. 이를 정의하는 방법은 여러 갈래가 있다. 미분기하에서는 connection의 곡률에서 Chern–Weil 이론으로 끌어내고, 혹은 Stiefel-Whitney에서 그러했듯 공리적인 접근을 할 수도 있다. (물론 이 경우 존재성이 별도의 명제로서 증명되어야 한다.) 우리는 [MS]를 따라 Chern class를 Euler class, 즉 top Chern class로부터 한 단계씩 내려오며 정의하기로 한다. 이 과정에서 필요한 것이 [정리 5](#thm5)의 *Gysin exact sequence*이다. 

이를 서술하기 위해 우선 다음을 정의하자. Base $B$가 paracompact이면 partition of unity로 $E$의 각 fiber에 내적을 주는 fiber metric을 잡을 수 있고, 그럼 길이 $1$인 vector들의 모임

$$S(E)=\{v\in E:\lvert v\rvert=1\}$$

이 fiber $S^{n-1}$을 갖는 fiber bundle이 된다. 이를 $E$의 *sphere bundle<sub>구면다발</sub>*이라 하고, 같은 방식으로 

$$D(E)=\{v\in E:\lvert v\rvert\leq 1\}$$

을 fiber가 disk $D^n$인 *disk bundle<sub>원판다발</sub>*이라 한다. 우리는 편의상 metric을 사용했지만, 이는 필수적인 것은 아니며 중요한 것은 zero section을 뺀 공간 $E_0=E\setminus 0(B)$에 대하여, 이 pair $(D(E), S(E))$가 $(E, E_0)$와 homotopy equivalent하다는 것이다. 이는 우선 $D(E)$ 바깥을 [§호몰로지의 계산, ⁋정리 2](/ko/math/algebraic_topology/computation_of_homology#thm2)를 이용하여

$$H^\ast(E, E_0)\cong H^\ast\bigl(D(E), D(E)\setminus 0(B)\bigr)$$

를 얻은 후, radial retraction을 적용하여

$$(E, E_0)\simeq (D(E), S(E))$$

를 얻어내면 된다. 그럼 이를 사용하면 다음을 얻는다.

::: 정리 5 (Gysin exact sequence)
Oriented rank $n$ vector bundle $E\rightarrow B$의 sphere bundle $\pi:S(E)\rightarrow B$에 대하여, 다음의 long exact sequence

$$\cdots\rightarrow H^{k-n}(B)\xrightarrow{\ \smile e\ }H^k(B)\xrightarrow{\ \pi^\ast\ }H^k(S(E))\xrightarrow{\ \pi_!\ }H^{k-n+1}(B)\rightarrow H^{k+1}(B)\rightarrow\cdots$$

가 존재한다. 여기서 $e=e(E)$는 Euler class, $\pi^\ast$는 pullback, $\pi_!$는 fiber를 따른 적분이다.
:::

::: 증명
Pair $(D(E), S(E))$의 cohomology long exact sequence

$$\cdots\rightarrow H^k(D(E), S(E))\rightarrow H^k(D(E))\rightarrow H^k(S(E))\xrightarrow{\ \delta\ }H^{k+1}(D(E), S(E))\rightarrow\cdots$$

를 보자. 그럼 우선 첫째 항은 [정리 2](#thm2)를 사용하여 

$$H^k(D(E), S(E))\cong H^k(E, E_0)\cong H^{k-n}(B)$$

이며, 둘째 항의 경우 retraction을 통해 $H^k(D(E))\cong H^k(B)$를 얻는다. 이와 같은 identification을 통해 다음의 commutative diagram

![pair cohomology 완전열과 Gysin 완전열](/assets/images/Math/Algebraic_Topology/Characteristic_Classes-1.svg){:style="width:40.87em" class="invert" .align-center}

을 얻을 수 있으며, 이 때 둘째 열의 map들은 수직 방향의 isomorphism을 따라 위쪽 exact sequence의 map들을 옮겨온 것이다. 구체적으로, 첫째 morphism $H^{k-n}(B)\rightarrow H^k(B)$를 따라가 보자. Thom isomorphism $\Phi:\alpha\mapsto p^\ast\alpha\smile u$로 $\alpha\in H^{k-n}(B)$를 $H^k(E, E_0)$로 올린 뒤 위 행의 첫 morphism $j^\ast$를 합성하면

$$j^\ast\Phi(\alpha)=j^\ast(p^\ast\alpha\smile u)=p^\ast\alpha\smile j^\ast u$$

이다. 여기서 둘째 등호는 $j^\ast$가 relative cohomology ring의 homomorphism이라 cup product를 보존한다는 것, 곧 $j^\ast p^\ast\alpha=p^\ast\alpha$을 쓴 것이며, 이는 직관적으로 $p^\ast\alpha$는 이미 $H^\ast(E)$ 위에 살고 있으므로 당연하다. 이제 이를 다시 수직방향 identification $H^k(E)\cong H^k(B)$을 통해 내리면 되는데, 이는 zero section $0:B\hookrightarrow E$ ($p\circ 0=\mathrm{id}$)를 통해 이루어지므로

$$0^\ast(p^\ast\alpha\smile j^\ast u)=0^\ast p^\ast\alpha\smile 0^\ast j^\ast u=\alpha\smile e(E)$$

가 된다. ([정의 3](#def3)) 비슷하게, 둘째 map $H^k(D(E))=H^k(B)\rightarrow H^k(S(E))$는 restriction, 곧 $\pi^\ast$인 것을 알 수 있으며, Gysin map $\pi_!$는 connecting homomorphism $\delta$를 Thom isomorphism $H^{k+1}(D(E), S(E))\cong H^{k-n+1}(B)$로 옮긴 것이다.
:::

세 번째 morphism $\pi_!:H^k(S(E))\rightarrow H^{k-n+1}(B)$는 조금 특별한 성질을 갖는다. 보통 연속사상 $\pi:S(E)\rightarrow B$가 cohomology에 주는 자연스러운 morphism은 pullback $\pi^\ast:H^\ast(B)\rightarrow H^\ast(S(E))$로, $\pi$의 역방향이며 degree를 보존한다. 반면 $\pi_!$는 $\pi$와 같은 방향으로 가면서 degree를 $(n-1)$만큼 낮추는데, 이와 같이 연속함수에 의해 마땅히 유도되어야 할 방향의 반대방향으로 거스르는 morphism을 *wrong way map*이라 하고 첨자 $!$를 붙여 표기하는 것이 관례이다.

이 morphism의 직관은 [정리 2](#thm2)를 뒤집는 데 있다. Thom isomorphism $\alpha\mapsto p^\ast\alpha\smile u$가 base의 class $\alpha$를 fiber 위 각 점에 복사($p^\ast\alpha$)한 뒤 fiber 방향 class $u$를 곱해 degree를 올리는, fiber 방향으로의 lift였다면, $\pi_!$는 그 역이라고 생각하면 된다. 즉 $S(E)$의 class를 base 방향 성분과 fiber 방향 성분으로 보면, fiber 방향 성분은 각 fiber $S^{n-1}$을 따라 적분해 밖으로 빼고 (그래서 fiber 차원 $n-1$만큼 degree가 깎인다), 남은 base 방향 class는 그대로 돌려놓는 것이다. 이 성질을 수학적으로 엄밀하게 적은 것이 바로 *projection formula*

$$\pi_!(\pi^\ast\alpha\smile\beta)=\alpha\smile\pi_!\beta,\qquad \alpha\in H^\ast(B), \quad\beta\in H^\ast(S(E))$$

이다. 

이를 실제로 사용하기 위해 위에서 살펴본 $S^2$의 tangent bundle $TS^2$를 보자. 그럼 Gysin sequence에서 

$$\smile e:H^0(S^2)\rightarrow H^2(S^2)$$ 

는 $\times 2$ map으로 주어지며, 그 cokernel $\mathbb{Z}/2$가 sphere bundle $S(TS^2)$의 $H^2$에 torsion으로 나타난다. 반면 $S^2$의 trivial bundle $E$로 시작했다면, 이 부분은 $\mathbb{Z}$였을 것이므로, Euler class가 sphere bundle을 product로부터 밀어낸 흔적이 바로 이 torsion에 담겨있는 것이다. 

이제 이로부터 Chern class를 정의하자. 핵심적인 사실은 $k<n-1$이면 

$$H^{k-n}(B)=H^{k-n+1}(B)=0$$

이므로 $\pi^\ast:H^k(B)\rightarrow H^k(S(E))$가 isomorphism이라는 것이다. 즉, sphere bundle의 cohomology는 낮은 차원에서는 정확히 base의 cohomology와 일치하며, 그 이후부터는 base의 cohomology에서 오는 것에 더해 Euler class가 추가적인 기여를 한다. 

계속 살펴보았던 deleted total space $E_0=E\setminus 0(B)$를 생각하자. $E_0$의 한 점은 base의 한 점 $x\in B$와, 이 점에서의 $E$의 fiber $E_x$의 *nonzero* $v\in E_x$의 순서쌍이다. 이제 $E_0$ 위에 *tautological bundle* $\pi_0^\ast E$를 정의하자. 이는 vector bundle $E\rightarrow B$를 projection map $\pi_0:E_0\rightarrow B$를 따라 pullback하여 얻어진 vector bundle이며, 그 정체는 각각의 점 $(x,v)\in E_0$마다 fiber $(\pi_0^\ast E)_{(x,v)}= E_x$를 갖는 vector bundle이다. 즉 $v$는 각각의 점 $(x,v)$에서 fiber로 붙어있는 벡터공간의 원소이기도 하며, nonzero이므로 이 벡터공간 안에서 1차원 부분공간 $\langle v\rangle$을 정의한다. 이제 $E_0$의 모든 점마다 이러한 방식으로 직선을 붙여 line bundle $L\rightarrow E_0$을 만들고, 이것이 $\pi_0^\ast E$ 안에서 정의하는 quotient $(\pi_0^\ast E)/L\rightarrow E_0$을 생각할 수 있다. 이는 각 점 $(x,v)$에서 fiber $E_x/\langle v\rangle$을 갖는 $E_0$ 위의 canonical complex rank $(n-1)$ bundle이며, fiber마다 Hermitian 내적을 주면 $v$의 orthogonal complement $v^\perp\subseteq E_x$로도 실현된다. ([\[선형대수학\] §복소내적공간, ⁋명제 4](/ko/math/linear_algebra/complex_inner_product_spaces#prop4)) 두 실현이 canonically isomorphic하므로, 앞으로 이 rank $(n-1)$ bundle을 표기의 편의상 $L^\perp$로 쓴다.

이제 <em-ko>complex</em-ko> vector bundle $E$가 주어졌다 하고, 이를 (oriented) real vector bundle로 본 것을 $E_\mathbb{R}$로 표기하자. 만일 $E$가 complex dimension $n$이라면 $E_\mathbb{R}$은 real dimension $2n$이다. 그럼 $E_0$는 $E_{\mathbb{R}}$의 sphere bundle $S(E_{\mathbb{R}})$와 homotopy equivalent하므로 [정리 5](#thm5)에 의해

$$\cdots\rightarrow H^{k-2n}(B)\xrightarrow{\ \smile e\ }H^k(B)\xrightarrow{\ \pi_0^\ast\ }H^k(E_0)\rightarrow H^{k-2n+1}(B)\rightarrow\cdots$$

이 성립하고, 위에서 살펴본 것과 같이 $k\leq 2n-2$이면 양 끝의 $H^{k-2n}(B)$와 $H^{k-2n+1}(B)$가 모두 음의 degree라 $0$이므로, $\pi_0^\ast:H^k(B)\rightarrow H^k(E_0)$는 isomorphism이다.

::: 정의 6
Complex rank $n$ vector bundle $E\rightarrow B$의 *Chern class<sub>천 특성류</sub>* $c_i(E)\in H^{2i}(B;\mathbb{Z})$를 vector bundle의 rank $n$에 대해 귀납적으로 다음과 같이 정의한다.

우선 $c_0(E)=1$이고, $i>n$이면 $c_i(E)=0$이며, 

$$c_n(E)=e(E_{\mathbb{R}})\in H^{2n}(B;\mathbb{Z})$$

로 둔다. $0<i<n$에 대해서는, 위에서 살펴본 $L^\perp$는 rank $(n-1)$ vector bundle로서 그 Chern class들이 귀납적 가정에 의해 이미 다 정의되어 있으므로, 이들을 isomorphism $\pi_0^\ast:H^{2i}(B)\rightarrow H^{2i}(E_0)$을 통해 옮겨와

$$\pi_0^\ast c_i(E)=c_i(L^\perp)$$

를 만족하는 (유일한) $c_i(E)\in H^{2i}(B)$들을 $E$의 $i$번째 Chern class로 정의한다. 이들을 모두 더한 $c(E)=1+c_1(E)+\cdots+c_n(E)\in H^\bullet(B;\mathbb{Z})$를 *total Chern class<sub>전체 천 특성류</sub>*라 한다.
:::

다른 상황에서와 마찬가지로, 그 정의만큼 중요한 것은 이것이 만족하는 다음의 특징들이다. 

::: 명제 7
Chern class는 다음을 만족한다.

1. (Naturality) 임의의 $f:B'\rightarrow B$에 대하여 $c(f^\ast E)=f^\ast c(E)$이다.
2. $c_0(E)=1$이고, $i>\rank_{\mathbb{C}}E$이면 $c_i(E)=0$이다.
3. (최고차) $c_n(E)=e(E_{\mathbb{R}})$이며, 따라서 $E$가 nonzero section을 가지면 $c_n(E)=0$이다.
:::

::: 증명
둘째 조건과 셋째 조건은 $c_n=e(E_{\mathbb{R}})$의 vanishing을 [명제 4](#prop4)의 셋째 조건을 사용하기만 하면 정의로부터 바로 오는 것이다. 

첫째 조건은 $n$에 대한 귀납으로 보인다. $c_n$의 naturality는 Euler class의 naturality로부터 온다. ([명제 4](#prop4)의 첫째 조건) $0<i<n$에서는 $f$가 deleted space와 complement bundle, 그리고 Gysin sequence 전체와 호환되는 bundle map $E_0'\rightarrow E_0$을 유도하고, 그 위에서 $f^\ast(L^\perp)\cong(f^\ast L)^\perp$이므로 귀납가정과 $\pi_0^\ast$의 naturality로부터 $c_i$의 naturality가 따라온다.
:::

즉 Chern class는 Stiefel-Whitney class와 비슷한 종류의 공리적인 성질을 만족한다. ([§슈티펠-휘트니 특성류, ⁋정의 5](/ko/math/algebraic_topology/stiefel_whitney_classes#def5)) 우리는 Stiefel-Whitney class의 존재성을 보이기 위해 real infinite Grassmannian $\Gr(k,\mathbb{R}^\infty)$를 생각한 후, 여기서의 cohomology class를 원래의 공간으로 pullback해와서 이들이 Stiefel-Whitney class의 공리적 조건을 만족함을 보였었는데, Chern class에 대해서도 비슷한 종류의 construction이 가능하다. 

::: 예시 8
[§슈티펠-휘트니 특성류, ⁋예시 3](/ko/math/algebraic_topology/stiefel_whitney_classes#ex3)의 real tautological line bundle의 complex analogue로, $\CP^\infty=\Gr(1,\mathbb{C}^\infty)$ 위의 tautological complex line bundle $\gamma$를 생각하자. 그럼 $\gamma$의 sphere bundle은 $\mathbb{C}^\infty$의 단위구 $S^\infty$이며 이는 contractible이므로[^1] 모든 $k>0$에 대해 $H^k(S^\infty)=0$이다. 따라서, [정리 5](#thm5)에 의해 $H^1(\CP^\infty)=0$이고 

$$\smile c_1(\gamma):H^{k-2}(\CP^\infty)\rightarrow H^k(\CP^\infty)$$

이 $k\geq 2$에서 isomorphism이다. 이제 $H^0(\CP^\infty)=\mathbb{Z}$에서 출발하면 $c_1(\gamma)$가 $H^2(\CP^\infty;\mathbb{Z})\cong\mathbb{Z}$의 generator이며, 

$$H^\bullet(\CP^\infty;\mathbb{Z})=\mathbb{Z}[c_1(\gamma)]$$

임을 얻는다. 

이는 [§슈티펠-휘트니 특성류, §§그라스만 다양체](/ko/math/algebraic_topology/stiefel_whitney_classes#그라스만-다양체)에서 real bundle에 대해 본 것과 같이, 이 $\gamma$는 complex line bundle의 *universal family*이다. 곧 임의의 complex line bundle이 $\gamma$의 pullback으로 유일하게 얻어지므로, first Chern class는 일대일 대응

$$\{B\text{ 위의 complex line bundle}\}/\cong\ \xrightarrow{\ c_1\ }\ H^2(B;\mathbb{Z})$$

를 주며, 이는 tensor product를 덧셈으로 보내는 group isomorphism이다. 곧 complex line bundle의 모든 정보가 $c_1$ 하나에 담겨있게 된다.
:::

더 일반적으로 real Grassmannian의 자리를 complex Grassmannian $\Gr(k,\mathbb{C}^\infty)$이 대신하고, 그 cohomology ring은

$$H^\bullet(\Gr(k,\mathbb{C}^\infty);\mathbb{Z})=\mathbb{Z}[c_1,\ldots,c_k]$$

으로 universal bundle의 Chern class들이 생성하는 polynomial ring이 되며, 우리는 이러한 종류의 계산을 조만간 다시 살펴보게 될 것이다. 

한편, Stiefel-Whitney class가 Whitney 합 공식을 따랐던 것처럼, 여기서도 Chern class가 같은 공식을 만족하는 것을 기대하는 것이 자연스러울 것이다. 이를 실제로 증명하는 핵심 스텝은  [§사영다발과 Leray–Hirsch 정리, ⁋정리 5](/ko/math/algebraic_topology/projective_bundles#thm5)인데, 이 정리의 증명은 지금까지의 논의로도 충분히 가능하지만 오직 스토리의 흐름을 위해 이를 다음 글로 따로 묶어둔다. 

::: 정리 9 (Whitney sum formula)
두 complex vector bundle $E,E'\rightarrow B$에 대하여

$$c(E\oplus E')=c(E)\smile c(E')$$

가 성립한다. 즉, 모든 $k$에 대하여 

$$c_k(E\oplus E')=\sum_{i+j=k}c_i(E)\smile c_j(E')$$

이다.
:::

::: 증명
[§사영다발과 Leray–Hirsch 정리, ⁋정리 5](/ko/math/algebraic_topology/projective_bundles#thm5)에 의하여, pullback $\rho^\ast:H^\bullet(B)\hookrightarrow H^\bullet(F(E))$이 단사이면서 $\rho^\ast E$를 complex line bundle들의 Whitney sum $L_1\oplus\cdots\oplus L_n$으로 쪼개는 연속함수 $\rho:F(E)\rightarrow B$가 존재한다. Naturality와 $\rho^\ast$의 단사성에 의해 공식은 모든 bundle을 line bundle들의 합으로 가정하고 증명해도 충분하다.

그럼 line bundle들의 합에 대하여

$$c(L_1\oplus\cdots\oplus L_n)=\prod_{i=1}^n\bigl(1+c_1(L_i)\bigr)$$

임을 보이면 충분하다. 핵심은 두 line bundle $L,L'$에 대한 두 등식 

$$c_1(L\oplus L')=c_1(L)+c_1(L'),\qquad c_2(L\oplus L')=c_1(L)\smile c_1(L')$$

이다. 둘째 등식은 임의의 base 위에서 바로 얻어진다. [정의 6](#def6)에 의하여 rank $2$ bundle의 최고차항은 

$$c_2(L\oplus L')=e\bigl((L\oplus L')_{\mathbb{R}}\bigr)$$

인데, [명제 4](#prop4)의 둘째 결과에 의하여 이는 $e(L_{\mathbb{R}})\smile e(L'_{\mathbb{R}})=c_1(L)\smile c_1(L')$과 같기 때문이다.

첫째 등식을 위해 우선 임의의 rank $n$ complex vector bundle $E$와 trivial line bundle $\varepsilon^1$에 대하여 다음 식

$$c(E\oplus\varepsilon^1)=c(E)$$

가 성립함을 보이자. $E'=E\oplus\varepsilon^1$이라 하면, trivial 성분에서 상수 $1$을 취하는 section $s(x)=(0,1)$은 어디서도 $0$이 아니므로 section $s:B\rightarrow E'_0$을 주며 $\pi_0\circ s=\mathrm{id}$이다. 이제 각 점에서 $(0,1)$의 orthogonal complement는 정확히 $E$의 fiber이므로 $s^\ast(E'^\perp)\cong E$이고, 따라서 $0<i\leq n$에 대하여 [정의 6](#def6)의 식 $\pi_0^\ast c_i(E')=c_i(E'^\perp)$에 $s^\ast$를 적용하면 [명제 7](#prop7)의 naturality로부터

$$c_i(E')=s^\ast\pi_0^\ast c_i(E')=s^\ast c_i(E'^\perp)=c_i(s^\ast E'^\perp)=c_i(E)$$

를 얻는다. 최고차 $c_{n+1}(E')=e(E'_{\mathbb{R}})$는 어디서도 $0$이 아닌 section이 존재하므로 [명제 4](#prop4)의 (3)에 의하여 $0$이며, 이는 $c_{n+1}(E)=0$과 일치한다.

한편, [예시 8](#ex8)에서 보았듯 $\gamma$가 complex line bundle의 universal family이므로, 임의의 base $B$ 위의 두 line bundle $L,L'$은 각각 base의 morphism $f_1,f_2:B\rightarrow\CP^\infty$를 따른 pullback $f_1^\ast\gamma$, $f_2^\ast\gamma$이다. 이제

$$f=(f_1, f_2): B\rightarrow \CP^\infty\times\CP^\infty$$

로 두면, 우리는 base들 사이에 다음의 commutative diagram

![분류사상 분해](/assets/images/Math/Algebraic_Topology/Characteristic_Classes-2.svg){:style="width:20.62em" class="invert" .align-center}

을 얻고, 따라서 $B$ 위의 $L, L'$에서의 식

$$c_1(L\oplus L')=c_1(L)+c_1(L')$$

즉

$$c_1(f^\ast(\pi_1^\ast\gamma \oplus \pi_2^\ast\gamma))=c_1(f_1^\ast\gamma)+c_1(f_2^\ast\gamma)$$

를 보이는 것은, [명제 7](#prop7)의 첫째 결과에 의해,

$$c_1(\pi_1^\ast\gamma\oplus \pi_2^\ast\gamma)=c_1(\pi_1^\ast\gamma)+c_1(\pi_2^\ast\gamma)$$

를 보이는 것과 같다. 즉, 우리는 $\CP^\infty\times\CP^\infty$ 위의 임의의 두 line bundle $L_1, L_2$에 대해 위 식이 성립하는 것을 보이면 충분하다. 

이를 위해 우선 [§코호몰로지, ⁋따름정리 10](/ko/math/algebraic_topology/cohomology#cor10)에 의해 

$$H^2(\CP^\infty\times\CP^\infty;\mathbb{Z})\cong H^2(\CP^\infty;\mathbb{Z})\oplus H^2(\CP^\infty;\mathbb{Z})$$

임을 관찰하자. 즉, inclusion $j_1:z\mapsto(z,q)$, $j_2:z\mapsto(q,z)$을 통해 restriction map $j_1^\ast$, $j_2^\ast$를 정의하면 이들이 각각의 성분을 읽어줄 수 있다. 한편 우리는 위에서 trivial line bundle에 대해서는 원하는 식이 성립함을 보았고, $j_1^\ast L_2$와 $j_2^\ast L_1$은 trivial이므로

$$j_1^\ast c_1(L_1\oplus L_2)=c_1(\gamma\oplus\varepsilon^1)=c_1(\gamma)=j_1^\ast\bigl(c_1(L_1)+c_1(L_2)\bigr)$$

과, 비슷한 식이 $j_2^\ast$에 대해서도 성립한다. 즉, 

$$c_1(L_1\oplus L_2)=c_1(L_1)+c_1(L_2)$$

이며, 위에서 보았듯 여기에 naturality를 더하면 임의의 $L,L'$에 대해서도 성립한다. 
:::

앞서 우리는 complex vector bundle $E$와 그 켤레 $\bar{E}$, 곧 같은 underlying real bundle에 scalar 곱을 $z\cdot v=\bar{z}v$로 뒤틀어 준 bundle을 Chern class가 구별할 수 있다고 하였다. 이제 이 주장을 정확하게 만들 수 있다.

::: 명제 10
Complex vector bundle $E\rightarrow B$의 켤레 $\bar{E}$에 대하여, 모든 $i$에 대해

$$c_i(\bar{E})=(-1)^ic_i(E)$$

가 성립한다.
:::
::: 증명
우선 line bundle $L$의 경우를 보자. [정의 6](#def6)에 의하여 $c_1(L)=e(L_{\mathbb{R}})$인데, $L$과 $\bar{L}$은 underlying real bundle이 같고 표준 방향만 서로 반대이다. 실제로 fiber의 nonzero vector $v$에 대하여 $L$의 표준 방향은 ordered basis $(v,iv)$가 주는 것이고, $\bar{L}$에서는 $i$가 $v$를 $-iv$로 보내므로 표준 방향은 $(v,-iv)$가 주는 것인데, 두 basis 사이의 change of basis 행렬식이 $-1$이다. 따라서 [명제 4](#prop4)의 (5)에 의하여 $c_1(\bar{L})=-c_1(L)$이다.

일반적인 경우 또한 위의 증명과 마찬가지로 splitting principle을 사용하면 된다. 
:::

가령 [예시 8](#ex8)의 tautological bundle $\gamma$는 $c_1(\gamma)$가 $H^2(\CP^\infty;\mathbb{Z})\cong\mathbb{Z}$의 generator라 $c_1(\bar{\gamma})=-c_1(\gamma)\neq c_1(\gamma)$이고, 따라서 $\gamma\not\cong\bar{\gamma}$이다. 물론 이 구별에는 한계가 있어서, 홀수 Chern class가 모두 $2$-torsion이거나 $0$인 bundle의 켤레는 Chern class만으로는 구별되지 않지만 여전히 Chern class가 real bundle보다는 풍부한 정보를 갖고 있음을 확인할 수 있다.

한편 지금까지의 예시는 모두 line bundle이었으므로, rank가 높은 bundle에서 [정리 9](#thm9)이 실제 계산에 어떻게 쓰이는지를 보여주는 예시를 하나 보기로 한다.

::: 예시 11
이번 글에서 우리는 유한차원 complex projective space $\CP^n=\Gr(1,\mathbb{C}^{n+1})$의 tangent bundle의 total Chern class를 계산한다. 

이를 위해 우선 이 위에 정의된 tautological line bundle $\gamma\subseteq\CP^n\times\mathbb{C}^{n+1}$을 생각하자. 이는 [예시 8](#ex8)의 universal line bundle $\gamma$를 $\CP^n\hookrightarrow\CP^\infty$으로 제한한 것이며, cell 구조가 짝수 차원에만 있으므로 restriction $H^k(\CP^\infty;\mathbb{Z})\rightarrow H^k(\CP^n;\mathbb{Z})$은 $k\leq 2n$에서 isomorphism이다. 따라서 [명제 10](#prop10)에 따라 $\x=c_1(\bar{\gamma})=-c_1(\gamma)$로 두면

$$H^\bullet(\CP^n;\mathbb{Z})=\mathbb{Z}[\x]/(\x^{n+1})$$

이다.

이제 tangent bundle을 보자. 이 공간의 한 점 $\ell\in\CP^n$은 직선 $\ell\subseteq\mathbb{C}^{n+1}$이고, Hermitian 내적을 고정하면 $\ell$에 가까운 직선들은 linear map $\ell\rightarrow\ell^\perp$들의 graph로 유일하게 나타난다. 곧 fiber별 $\mathbb{C}$-linear map들의 bundle을 $\Hom$으로 적으면

$$T\CP^n\cong\Hom(\gamma,\gamma^\perp)$$

이다. 여기에 trivial line bundle $\Hom(\gamma,\gamma)$를 Whitney sum하면

$$T\CP^n\oplus\Hom(\gamma,\gamma)\cong\Hom(\gamma,\gamma^\perp\oplus\gamma)\cong\Hom(\gamma,\varepsilon^{n+1})\cong\Hom(\gamma,\varepsilon^1)^{\oplus(n+1)}$$

이다. 여기서 $\varepsilon^{n+1}$은 rank $n+1$ trivial bundle이다. 따라서, 우변의 $\Hom(\gamma, \varepsilon^1)$을 $\overline{\gamma}$와 identify하면 [정리 9](#thm9)로부터 다음의 식

$$c(T\CP^n)=c\bigl(T\CP^n\oplus\Hom(\gamma,\gamma)\bigr)=c(\bar{\gamma})^{n+1}=(1+\x)^{n+1}$$

을 얻으며, 이를 전개하면 $H^\bullet(\CP^n)=\mathbb{Z}[\x]/(\x^{n+1})$이므로 

$$c(T\CP^n)=(n+1)\x^n+\cdots +1$$

임을 안다. 
:::

## 폰트랴긴 특성류

Real vector bundle에 대해서도 $\mathbb{Z}$-coefficient의 불변량을 complex Chern class를 거쳐 얻을 수 있다.

::: 정의 12
Real vector bundle $E\rightarrow B$의 *Pontryagin class<sub>폰트랴긴 특성류</sub>* $p_i(E)\in H^{4i}(B;\mathbb{Z})$를, complexification $E\otimes_{\mathbb{R}}\mathbb{C}$의 Chern class로

$$p_i(E)=(-1)^i c_{2i}(E\otimes_{\mathbb{R}}\mathbb{C})$$

로 정의한다.
:::

Complexification $E\otimes_{\mathbb{R}}\mathbb{C}$는 $v\otimes z\mapsto v\otimes\bar{z}$를 통해 그 켤레 $\overline{E\otimes\mathbb{C}}$와 isomorphic하다. 그럼 [명제 10](#prop10)에 의하여 $c_{2i+1}(E\otimes\mathbb{C})=-c_{2i+1}(E\otimes\mathbb{C})$, 곧 홀수 Chern class들은 모두 $2$-torsion이 되어 ($2c_{2i+1}=0$) 본질적으로 유의미한 정보를 담지 못한다. 이때문에 우리는 짝수 자리의 (부호가 있는) Chern class만 사용하여 $i$번째 class를 정의하고, 또 Chern class는 본질적으로 자기 번호의 두 배의 index의 cohomology class에 살고 있으므로 Pontryagin class는 $H^{4i}(B;\mathbb{Z})$에 살게 된다. 직관적으로 이는 Stiefel-Whitney class가 $\mathbb{Z}/2$에서 하던 일을 (complex vector bundle로 넘어가지 않고) $\mathbb{Z}$-coefficient로 가져온 것이자, Chern class가 complex vector bundle에서 하던 일을 real vector bundle로 가지고 내려온 것으로 생각할 수 있다. 

기본적인 성질들 역시 complexification을 따라 Chern class로부터 내려온다. Total Pontryagin class는 $p(E)=1+p_1(E)+p_2(E)+\cdots$로 적는다.

::: 명제 13
Real vector bundle $E,F\rightarrow B$에 대하여 다음이 성립한다.

1. (Naturality) 임의의 $f:B'\rightarrow B$에 대하여 $p(f^\ast E)=f^\ast p(E)$이다.
2. (Whitney) $2\bigl(p(E\oplus F)-p(E)\smile p(F)\bigr)=0$이다. 특히 $H^\bullet(B;\mathbb{Z})$에 $2$-torsion이 없으면 $p(E\oplus F)=p(E)\smile p(F)$이다.
3. Complex vector bundle $E$에 대하여 $E_{\mathbb{R}}\otimes_{\mathbb{R}}\mathbb{C}\cong E\oplus\bar{E}$이며, 따라서 $p_i(E_{\mathbb{R}})$는 $E$의 Chern class들의 다항식이다. 가령 $p_1(E_{\mathbb{R}})=c_1(E)^2-2c_2(E)$이다.
:::
::: 증명
(1)은 complexification이 pullback과 교환하고 [명제 7](#prop7)의 naturality에서 즉시 나온다. (2)도 $(E\oplus F)\otimes\mathbb{C}\cong(E\otimes\mathbb{C})\oplus(F\otimes\mathbb{C})$에 [정리 9](#thm9)를 적용하면 되는데, [정의 12](#def12) 아래 관찰대로 홀수 Chern class가 모두 $2$-torsion이므로 이들이 낀 항은 $2$를 곱하면 소멸하고, 남는 짝수항이 $p(E)\smile p(F)$를 준다.

(3)만 약간의 계산이 필요하다. $E_{\mathbb{R}}\otimes\mathbb{C}$으로 complexify하면, 이 과정에서 complex structure는 $J\in \End(E)$로 나오며, 그 고유값은 $\pm i$이다. 이제 이를 $\mathbb{C}$-linear로 확장하면 그 $\pm i$ 고유공간 분해가 $E_{\mathbb{R}}\otimes\mathbb{C}\cong E\oplus\bar{E}$를 준다. 그럼 이제 [정리 9](#thm9)와 [명제 10](#prop10)으로 $c_2(E_{\mathbb{R}}\otimes\mathbb{C})=c_2(E\oplus\bar{E})=2c_2(E)-c_1(E)^2$이므로 이를 Pontryagin class로 가지고 오면 원하는 결과를 얻는다.
:::

---

**참고문헌**

**[MS]** J. W. Milnor and J. D. Stasheff, *Characteristic Classes*, Annals of Mathematics Studies 76, Princeton University Press, 1974.

**[BT]** R. Bott and L. W. Tu, *Differential Forms in Algebraic Topology*, Springer, 1982.

**[Hat]** A. Hatcher, *Vector Bundles and K-Theory*, online notes, 2017.

---
[^1]: $S^\infty$을 $\mathbb{C}^\infty=\bigcup_n\mathbb{C}^n$의 단위구로 보자. Shift morphism $T(x_1,x_2,\ldots)=(0,x_1,x_2,\ldots)$에 대하여, 벡터를 $v\mapsto v/\lvert v\rvert$로 정규화한 두 직선 homotopy $x\mapsto\bigl((1-t)x+tT(x)\bigr)/\lvert(1-t)x+tT(x)\rvert$과 $x\mapsto\bigl((1-t)T(x)+te_1\bigr)/\lvert(1-t)T(x)+te_1\rvert$이 각각 항등사상을 $T$로, 그리고 $T$를 상수사상 $x\mapsto e_1=(1,0,\ldots)$으로 잇는다. 두 분모 모두 $0$이 되지 않는데, 앞의 것은 $x$와 $T(x)$의 좌표가 한 칸 어긋나 $(1-t)x+tT(x)=0$이 $x=0$을 강제하고, 뒤의 것은 합의 첫 좌표가 $t$라 $0$이려면 $t=0$이어야 하며 그럼 $T(x)=0$, 곧 $x=0$이기 때문이다. 이 둘을 이으면 $S^\infty$이 한 점으로 수축한다. 