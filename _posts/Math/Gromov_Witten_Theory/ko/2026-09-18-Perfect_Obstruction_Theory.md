---
title: "Perfect obstruction theory"
description: "실제 차원이 virtual dimension을 초과하는 stable map moduli 위에서 기대 차원의 cycle을 복원하는 문제를, 벡터다발 section의 zero locus라는 국소 모형에서 시작하여 Behrend–Fantechi의 perfect obstruction theory와 intrinsic normal cone을 거쳐 virtual fundamental class의 구성으로 연결한다."
excerpt: "Perfect obstruction theory, virtual fundamental class, intrinsic normal cone, localized Euler class"

categories: [Math / Gromov-Witten Theory]
permalink: /ko/math/gromov-witten_theory/perfect_obstruction_theory
sidebar: 
    nav: "gromov-witten_theory-ko"

date: 2026-09-18

weight: 4
revising: true
drift_needed: true

---

우리는 [§마디 곡선의 변형, ⁋정의 8](/ko/math/gromov-witten_theory/deformations_of_nodal_curves#def8){: data-lid="n4okj" }의 prestable curve들의 moduli stack $\mathfrak{M}_{g,n}$이 차원 $3g-3+n$의 smooth algebraic stack임을 보았다. 이를 위해 핵심적인 사실은 prestable curve의 deformation이 unobstructed라는 것으로, 이것이 moduli stack의 smoothness를 보장했다. 

이와 대조되는 것은 [§안정사상들의 모듈라이 공간](/ko/math/gromov-witten_theory/moduli_of_stable_maps){: data-lid="crl4y" }에서 다룬 stable map들의 moduli $\overline{\mathcal{M}}_{g,n}(X,\beta)$이다. Stable map $(C,p_\bullet,\mu)$의 first-order deformation들이 이루는 deformation space를 $T^1$, $\overline{\mathcal{M}}_{g,n}(X,\beta)$의 étale atlas에서 이 stable map을 나타내는 점에서의 complete local ring을 $R$이라 하자. 그럼 이 점 근방의 formal neighborhood는 $\Spec R$로 주어지며, 이는 이 점을 $k$차까지 두껍게 한 infinitesimal neighborhood를 모든 $k$에 대해 모은 것이다. 이 때, stable map에는 infinitesimal automorphism이 없으므로 $T^1$은 이 점의 tangent space이고, $R$을 $(C,p_\bullet,\mu)$의 universal formal deformation의 base로 사용할 수 있다. 이제 $N=\dim T^1$이라 하고 $T^1$의 coordinate를 $\x_1,\ldots,\x_N$이라 하면, $T^1$의 원점에서의 formal neighborhood는

$$\Spec P,\qquad P=\mathbb{C}[[\x_1,\ldots,\x_N]]$$

으로 쓸 수 있으며, cotangent space에서 isomorphism인 surjection $P\rightarrow R$이 존재한다. 그 kernel을 $J$라 하면 $R=P/J$이고 $J\subseteq(\x_1,\ldots,\x_N)^2$이므로, 이 점의 formal neighborhood는 $T^1$의 원점의 formal neighborhood 안에서 이차 이상의 방정식들로 잘라낸, tangent space가 같은 closed subscheme으로 주어진다. 한편 $P$의 maximal ideal을 $\mathfrak{m}_P$라 하면 $P/\mathfrak{m}_PJ\rightarrow R$은 small extension이고, $\Spec R$에서 moduli로 가는 map을 이를 따라 extend하는 것의 obstruction은 $T^2\otimes_{\mathbb{C}}J/\mathfrak{m}_PJ$의 원소, 곧 linear map $(J/\mathfrak{m}_PJ)^\vee\rightarrow T^2$이며 이 map은 injective이다. 따라서 $J$는 많아야 $\dim T^2$개의 방정식으로 생성되며, 이것이 바로 virtual dimension

$$\vdim=\dim T^1-\dim T^2$$

의 정체였다. 우리가 Gromov-Witten invariant를 계산할 때는 $X$가 convex라는 가정 아래 $T^2=0$이어서 $\vdim$과 실제 차원이 같았다.

관점을 바꾸어 이 방정식들을 $T^2$에 값을 갖는 하나의 map으로 생각하자. $T^2$의 basis $e_1,\ldots,e_r$의 dual basis를 택하면, 이를 위의 injection의 dual $(T^2)^\vee\rightarrow J/\mathfrak{m}_PJ$로 보낼 수 있으며, 이를 $J$의 원소 $f_1,\ldots,f_r$로 lift하면 $f_1,\ldots,f_r$은 $J$를 생성한다. 따라서

$$\kappa=\sum_{i=1}^rf_ie_i:(T^1,0)\rightarrow(T^2,0)$$

로 두면, $\kappa$는 $T^1$의 coordinate에 대한 power series로서 $T^2$에 값을 갖고 상수항과 일차항이 없으며, $R=P/(f_1,\ldots,f_r)$이므로 $(C,p_\bullet,\mu)$를 나타내는 점의 formal neighborhood는 정확히 그 zero locus $\kappa^{-1}(0)$이다. 이 $\kappa$를 *Kuranishi map*이라 부른다. $\kappa$는 coordinate와 lift의 선택에 의존하지만 그 zero locus는 그렇지 않으며, 이차항 $\kappa_2$도 선택에 의존하지 않고 first-order deformation $v$를 이차까지 extend하는 것의 obstruction $\kappa_2(v)\in T^2$를 준다. 또 $\dim T^2$가 $J$를 생성하는 데 필요한 방정식의 개수보다 크면 그 차이만큼의 성분을 항등적으로 $0$으로 잡을 수 있고, 특히 $J=0$이면 $\kappa\equiv0$이다. 즉 각 점 근방에서 moduli는 deformation들의 공간 $T^1$을 obstruction들의 공간 $T^2$에 값을 갖는 방정식 $\kappa=0$으로 잘라낸 것이고, $\vdim$은 $\kappa$의 $\dim T^2$개의 성분이 독립적인 방정식으로 작동할 때 기대되는 차원이다.

그러나 $X$가 convex가 아니면 $T^2$가 사라지지 않아 실제 차원이 $\vdim$보다 커질 수 있으므로, 이 경우 Gromov-Witten invariant를 정의하려면 fundamental class 대신 차원 $\vdim$을 갖는 *virtual fundamental class<sub>가상 기본류</sub>*

$$[\overline{\mathcal{M}}_{g,n}(X,\beta)]^\vir\in A_{\vdim}(\overline{\mathcal{M}}_{g,n}(X,\beta))$$

가 필요하다. 핵심적인 아이디어는, 각 점 근방에서 moduli는 $\kappa$의 zero locus로 나타나므로, 이 zero locus의 차원이 기대와 다르더라도, 방정식들을 일반적인 위치로 흔들었을 때 얻어질 zero locus의 class를 구해주면 된다는 것이다. 문제는 이것이 한 점에서의 그림이라는 것으로, 일반적으로 $T^1$과 $T^2$의 차원은 점마다 jump하며 $\kappa$의 정의 자체도 coordinate 선택에 의존하므로 이들 점마다의 그림을 moduli 전체로 이어줄 자료가 필요하며, 이것이 이번 글에서 정의할 *intrinsic normal cone*이고, 이 cone을 vector bundle로 표현되는 공간 안에 넣어 주는 자료로서 *perfect obstruction theory*를 정의할 수 있다. 


## 벡터다발의 zero locus

위에서 마주한 문제는 Kuranishi map이 한 점에서의 그림이라는 것이었다. 우리는 일반적인 경우를 다루기 전에 우선 처음부터 전체에서 이러한 구조가 주어진 경우, 즉 smooth variety 위의 vector bundle의 section과 그 zero locus를 살펴본다. 

Smooth variety $X$ 위에 rank $r$의 vector bundle $E$와 section $s\in\Gamma(X,E)$가 주어져 있다 하고

$$Z(s)=\{x\in X\mid s(x)=0\}$$

을 그 zero locus라 하자. 만일 $s$가 zero section과 transversal하게 만나면 $Z(s)$는 기대했던 codimension $r$의 smooth subvariety이고 그 fundamental class는 Euler class $e(E)\cap[X]$와 일치한다. 만일 section $s$가 transversal하게 만나지 않아 $Z(s)$의 codimension이 $r$보다 작다면 그 fundamental class $[Z(s)]$는 기대 차원의 class가 아니지만, 그럼에도 불구하고 이 모델에서는 $X$에서의 class $e(E)\cap[X]$가 존재하며, $X$로 보내면 이 class가 되는 $Z(s)$ 위의 기대 차원 $\dim X-r$의 *localized Euler class*

$$e(E,s)\in A_{\dim X-r}(Z(s))$$

를 정의할 수 있다. 직관적으로 이는 non-transversal section $s$를 올바르게 흔들어줬으면 나왔을 class를 실제로 흔들지 않고도 대수적으로 적어 둔 것으로 이해할 수 있다.

::: 예시 1
$X=\mathbb{P}^2$, $E=\mathcal{O}(1)^{\oplus2}$를 보자. 그럼 section $s=(\ell_1,\ell_2)$가 두 일차식으로 주어지므로, 위의 그림에서 $Z(s)$는 기대차원이 $0$이 된다. 실제로 이는 두 직선의 교점인 한 점이고, 그 class의 degree는

$$\int_{\mathbb{P}^2}e(E)=\int_{\mathbb{P}^2}c_1(\mathcal{O}(1))^2=1$$

이다. 그러나 non-transversal section, 가령 극단적으로 $s\equiv0$을 택하면 $Z(s)=\mathbb{P}^2$ 전체가 되어 실제 차원이 기대 차원을 $2$만큼 초과한다. 그럼에도 localized Euler class를 $X$로 보낸 class는 section이 아니라 bundle만으로 결정되며,

$$e(E)\cap[\mathbb{P}^2]=c_2(\mathcal{O}(1)^{\oplus2})\cap[\mathbb{P}^2]$$

로 여전히 degree $1$의 point class를 준다. ([\[대수다양체\] §교차곱, ⁋예시 11](/ko/math/algebraic_varieties/intersection_product#ex11){: data-lid="9kgj4" })
:::

이 모형이 좋은 점은 각 점 $x\in Z(s)$에서의 Kuranishi 그림이 $s$ 자체로 주어진다는 것이다. 이를 확인하기 위해 $Z(s)$의 Kuranishi 그림을 보자. $Z(s)$의 한 점 $x$가 주어졌을 때, 이 점을 흔들었을 때도 여전히 $Z(s)$ 안에 머물러야 한다는 조건이 바로 $Z(s)$의 deformation 방향을 결정한다. 즉 tangent vector $v\in T_{X,x}$ 방향으로의 무한소 이동 $x+\epsilon v$에 대하여

$$s(x+\epsilon v)=s(x)+\epsilon\dd{s}(v)=\epsilon\dd{s}(v)$$

이므로, 이 일차 변화율 $\dd{s}(v)=0$ 조건이 만족되어야 그 결과가 $Z(s)$ 안에 머무를 수 있다. 따라서 $\dd{s}$의 kernel인 $\ker(\dd{s})$가 $Z(s)$의 실제 tangent space이자 deformation 방향을 이루며, 반대로 $E_x$ 안에서 $\dd{s}$의 image가 채우지 못한 나머지 방향들, 곧 cokernel $\coker(\dd{s})$는 section을 $0$으로 유지하도록 통제할 수 없는 방향들로 이것이 바로 $Z(s)$의 obstruction space가 된다. 

이제 이 두 공간을 잇는 Kuranishi map $\kappa$는 다음과 같이 정의된다. 우선 

$$T_{X,x}=K\oplus K',\qquad K=\ker(\dd{s}_x)$$

로 쪼개고, $x$ 근방에서 $E$를 trivialize하여 

$$E_x=I\oplus Q, \qquad I=\im(\dd{s}_x),\quad Q\cong\coker(\dd{s}_x)$$

로 쪼갠 뒤 이에 맞춰 $s=(s_I,s_Q)$로 적자. 그럼 $\dd{s}_x$를 $K'$으로 제한한 것은 $I$로의 isomorphism이므로 $s_I$의 Jacobian은 $x$에서 full rank이고, [\[스킴\] §매끄러운 사상과 에탈 사상, ⁋정리 4](/ko/math/scheme_theory/smooth_and_etale_morphisms#thm4){: data-lid="th3fe" }에 의하여 $s_I=0$은 $x$ 근방에서 tangent space가 $K$인 smooth subvariety를 정의한다. 따라서 $x$의 formal neighborhood에서 $K'$의 coordinate는 $K$의 coordinate에 대한 함수 $\psi$로 쓸 수 있으며, 이 때 이 subvariety는 $\psi$의 graph이고 그 tangent space가 $K$이므로 $\psi$는 일차항이 없다. 이를 남은 방정식 $s_Q$에 대입한

$$\kappa(y)=s_Q(y,\psi(y)):(\ker(\dd{s}_x),0)\rightarrow(\coker(\dd{s}_x),0)$$

은 $s(x)=0$이므로 상수항이 없고, $\dd{s}_x$가 $K$ 위에서 $0$이고 $\psi$에 일차항이 없으므로 일차항도 없다. 또 $x$의 formal neighborhood에서 $Z(s)$는 $s_I=s_Q=0$, 즉 $K$의 원점의 formal neighborhood 안의 $\kappa^{-1}(0)$으로 주어지므로 $\kappa$가 $x$에서의 Kuranishi map이다. 특히 $\dd{s}_x=0$이면 소거할 것이 없어 $s$를 $x$의 근방으로 제한한 것이 그대로 Kuranishi map이다. 따라서 점마다 Kuranishi map을 따로 잡아 붙일 필요 없이, $s$ 하나가 모든 점의 Kuranishi map 역할을 동시에 한다.

만일 $s$가 $Z(s)$의 모든 점에서 transversal하면 $\dd{s}_x$가 항상 surjective이므로 obstruction space가 사라지고, $Z(s)$는 기대 차원의 smooth subvariety이며 localized Euler class는 $[Z(s)]$ 자신이다. 핵심적인 관찰은, $s$가 transversal하지 않은 점에서 $\dd{s}_x$의 rank가 떨어져 [예시 1](#ex1){: data-lid="fkmo8" }의 $s\equiv0$처럼 tangent space가 기대보다 부풀더라도 obstruction space 역시 같은 크기로 늘어나므로, 둘의 차이

$$\dim\ker(\dd{s}_x)-\dim\coker(\dd{s}_x)=\dim X-\rank E$$

는 항상 일정하다는 것이다. 위의 소거에서 coordinate와 방정식이 같은 수만큼 짝지어 사라지기 때문이며, 이 값이 이 모형의 virtual dimension $\vdim$이다. 즉 $Z(s)$가 얼마나 나쁘게 행동하든, 각 점의 Kuranishi 그림이 기대하는 차원은 localized Euler class가 놓이는 차원 $\dim X-\rank E$와 같다. 

그러나 이 계산은 localized Euler class의 차원이 잘 맞아떨어진다는 것일 뿐, 실제로 그 class가 어떤 것인지를 알려주지는 않으며, 실제 정의는 별도로 해 주어야 한다. 핵심적인 도구는 [\[대수다양체\] §교차곱, ⁋명제 9](/ko/math/algebraic_varieties/intersection_product#prop9){: data-lid="brhx6" }이다. $Z=Z(s)$의 ideal sheaf를 $\mathcal{I}$라 하면 $Z$의 $X$ 안에서의 normal cone은

$$C_{Z/X}=\Spec_Z\bigoplus_{n\geq0}\mathcal{I}^n/\mathcal{I}^{n+1}$$

으로 정의되었으며, 이는 직관적으로 $X$를 $Z$의 normal 방향으로 무한히 확대했을 때 $Z$ 위에 남는 모양으로 생각할 수 있다. 그럼 위 명제의 내용은 $t\neq0$에서의 fiber가 $X$이고 $t=0$에서의 fiber가 $C_{Z/X}$인 $\mathbb{A}^1$ 위의 family가 존재한다는 것, 곧 $X$를 $Z$를 따라 $C_{Z/X}$로 degenerate시킬 수 있다는 것이다. 이 degeneration 때문에 $C_{Z/X}$는 $Z$의 모양과 무관하게 pure dimension $\dim X$를 갖는다. 이때 만일 $Z\hookrightarrow X$가 regular embedding이라면 $C_{Z/X}$는 normal bundle과 같지만, 일반적으로는 그 fiber가 vector space가 아닌 cone으로 주어진다.

이제 $E$를 국소적으로 trivialize하여 $s=(s_1,\ldots,s_r)$로 적으면 $\mathcal{I}=(s_1,\ldots,s_r)$이므로, $s$와의 pairing

$$s^\vee:E^\vee\rightarrow\mathcal{O}_X,\qquad\varphi\mapsto\varphi(s)$$

의 image가 $\mathcal{I}$이다. 실제로 trivialization의 basis를 $e_1,\ldots,e_r$, 그 dual basis를 $e_1^\vee,\ldots,e_r^\vee$라 하면 $s^\vee(e_i^\vee)=e_i^\vee(s)=s_i$이다. 이를 $Z$로 제한하면 surjection $E^\vee\vert_Z\twoheadrightarrow\mathcal{I}/\mathcal{I}^2$을 얻고, $\bigoplus_n\mathcal{I}^n/\mathcal{I}^{n+1}$은 degree $1$의 성분 $\mathcal{I}/\mathcal{I}^2$으로 생성되므로 이는 graded algebra의 surjection

$$\Sym(E^\vee\vert_Z)\twoheadrightarrow\Sym(\mathcal{I}/\mathcal{I}^2)\twoheadrightarrow\bigoplus_{n\geq0}\mathcal{I}^n/\mathcal{I}^{n+1}$$

으로 이어진다. 여기에 $\Spec_Z$를 취하면 closed embedding

$$C_{Z/X}\hookrightarrow N_{Z/X}=\Spec_Z\Sym(\mathcal{I}/\mathcal{I}^2)\hookrightarrow E\vert_Z$$

를 얻으므로 $C_{Z/X}$는 $E\vert_Z$의 closed subcone이 된다. 가운데의 $N_{Z/X}$는 $Z$가 regular embedding이면 normal bundle이고, 일반적으로는 각 fiber가 vector space이지만 그 차원이 점마다 달라질 수 있는 cone이다.

이제 zero section $0_E:Z\hookrightarrow E\vert_Z$에 대한 Gysin map을 cone에 취하여

$$e(E,s)=0_E^![C_{Z/X}]\in A_{\dim X-r}(Z)$$

로 localized Euler class를 정의한다. 차원이 $\dim X-r$이 되는 것은 pure dimension $\dim X$의 cone을 rank $r$의 bundle의 zero section으로 자르기 때문이며, 이것이 위에서 점마다 센 $\dim\ker(\dd{s}_x)-\dim\coker(\dd{s}_x)$의 전역적인 판본이다. 또 $e(E,s)$를 $X$로 보내면 $e(E)\cap[X]$이고, $s$를 일반적인 위치로 흔든 family $s_t$에 대해 $Z(s_t)$의 class가 $t\rightarrow0$에서 가는 극한은 $e(E,s)$이다. $X\times\mathbb{A}^1$ 위의 section $(s_t)_t$로 만든 localized Euler class를 $t=0$의 fiber로 Gysin pullback하는 것이 두 Gysin map의 순서를 바꾼 것과 같기 때문이다.

Cone이 이 class를 정할 수 있는 것은 그것이 각 점의 Kuranishi map을 기록하기 때문이며, 그 방식은 위의 소거에서 바로 보인다. 점 $x\in Z$에서 $s_I$의 미분은 $K'$ 위에서 isomorphism이므로, $x$의 formal neighborhood의 coordinate를 $K$의 coordinate $y$와 $s_I$의 성분들로 잡을 수 있다. 이 coordinate에서 $s_I=0$이 정의하는 subvariety는 $y$만의 공간이고 그 위에서 $s_Q$는 $\kappa(y)$이므로, $Z$의 ideal은 $s_I$의 성분들과 $\kappa(y)$의 성분들로 생성되며 두 묶음은 서로 다른 변수에 걸려 있다. 따라서 $\bigoplus_n\mathcal{I}^n/\mathcal{I}^{n+1}$은 $\kappa^{-1}(0)\subseteq K$의 normal cone의 graded algebra에 $s_I$의 성분들의 class를 polynomial variable로 붙인 것이 되고, $x$의 formal neighborhood에서

$$C_{Z/X}\cong I\times C_{\kappa^{-1}(0)/K}$$

를 얻는다. 즉 $\dd{s}_x$의 image 방향으로는 cone이 bundle과 같은 크기이고, 나머지 $Q$ 방향에서 cone의 모양을 정하는 것은 $\kappa$이다.

[예시 1](#ex1){: data-lid="tis96" }을 이 관점에서 다시 보면, $s\equiv0$일 때는 $\mathcal{I}=0$이어서 cone은 zero section 자신이고 $e(E,s)=e(E)\cap[\mathbb{P}^2]$이며, $s$가 transversal할 때는 cone이 $E\vert_Z$ 전체이고 $e(E,s)=[Z]$이다. 일반적으로 $Z$가 local complete intersection인 open set 위에서는 cone이 normal bundle $N_{Z/X}$와 같고, $\mathcal{I}/\mathcal{I}^2$이 locally free이므로 surjection $E^\vee\vert_Z\rightarrow\mathcal{I}/\mathcal{I}^2$의 dual은 $N_{Z/X}$를 $E\vert_Z$의 subbundle로 넣는다. Subbundle을 zero section으로 자르면 quotient의 top Chern class가 남으므로, 대략적으로 말해 $Z$의 smooth한 성분 가운데 기대 차원인 것은 자기 자신의 fundamental class를, 기대보다 큰 것은 *excess bundle* $E\vert_Z/N_{Z/X}$의 top Chern class를 기여하며, 성분들이 만나거나 local complete intersection이 아닌 점에서는 보정이 필요하다. 이때 cone의 성분 하나가 $Z$의 closed subvariety $W$ 위에 놓이면, 그 차원 $\dim X$는 $\dim W$와 fiber의 차원 $r$의 합을 넘을 수 없으므로 $\dim W\geq\dim X-r$이어야 한다. 즉 cone의 성분은 기대 차원 이상의 subvariety 위에만 놓이며, 그런 subvariety라면 $Z$의 성분이 아니어도 된다. 또 $Z$가 local complete intersection이 아닌 점에서는 normal bundle의 closure가 subbundle이 되지 못할 수 있다. 다음은 normal cone이 zero section도 bundle 전체도 아니며 subbundle조차 아닌 예이다.

::: 예시 2
$X=\mathbb{P}^3$ 위의 $E=\mathcal{O}(2)^{\oplus2}$와 section $s=(\x_0\x_1,\x_0\x_2)$를 생각하자. 이는 $\mathbb{A}^3$ 안의 $Z(\x\y,\x\z)$를 사영화한 것으로, $Z=Z(s)$는 평면 $P=\{\x_0=0\}$과 직선 $L=\{\x_1=\x_2=0\}$의 합집합이고 둘은 한 점 $p=[0:0:0:1]$에서 만난다. 기대 차원은 $3-2=1$이고, $X$로 보낸 class는

$$c_2(E)\cap[\mathbb{P}^3]=4H^2\cap[\mathbb{P}^3]$$

이므로 degree $4$의 곡선 class이다. 한편 $P\cap L$은 한 점이고 한 점의 $A_1$은 $0$이므로, 두 closed subscheme의 합집합에 대한 exact sequence $A_1(P\cap L)\rightarrow A_1(P)\oplus A_1(L)\rightarrow A_1(Z)\rightarrow0$에 의하여 $A_1(Z)\cong A_1(P)\oplus A_1(L)\cong\mathbb{Z}^2$이다. 즉 $e(E,s)\in A_1(Z)$는 두 성분에서의 degree의 쌍 $(a,b)$로 결정되며 $a+b=4$이다.

Normal cone $C=C_{Z/X}$은 $E\vert_Z$ 안의 pure dimension $3$의 closed subcone이다. 위에서 본 대로 그 성분은 $1$차원 이상의 subvariety 위에만 놓이므로 한 점 위에 놓일 수 없고, 따라서 $C$의 성분은 $P$ 위의 것과 $L$ 위의 것뿐이다. $L\setminus\{p\}$ 근방에서는 $\x_0$이 unit이므로 ideal이 $(\x_1,\x_2)$가 되어 $Z$는 codimension $2$의 complete intersection이고, 그곳의 normal cone은 $E\vert_L$ 전체이다. 따라서 $L$ 위의 성분은 $C_L=E\vert_L$이다. 반면 $P\setminus\{p\}$ 근방에서는 $\x_1,\x_2$ 중 하나가 unit이므로 ideal이 $(\x_0)$이 되어 $Z$는 Cartier divisor $P$이고, normal cone은 line bundle $N_{P/X}=\mathcal{O}_P(1)$이다. $P\setminus\{p\}$ 위에서 $Z$의 ideal은 $P$의 ideal $\mathcal{I}_P=(\x_0)$과 같으므로, 이것이 $E\vert_P$ 안에 놓이는 방식은 $E^\vee\vert_P=\mathcal{O}_P(-2)^{\oplus2}\rightarrow\mathcal{I}_P/\mathcal{I}_P^2=\mathcal{O}_P(-1)$에서 읽을 수 있다. 두 기저가 각각 $\x_0\x_1=\x_1\cdot\x_0$과 $\x_0\x_2=\x_2\cdot\x_0$으로 가므로 이 map은 $(\x_1,\x_2)$이고, 그 dual

$$N_{P/X}=\mathcal{O}_P(1)\xrightarrow{(\x_1,\x_2)}\mathcal{O}_P(2)^{\oplus2}=E\vert_P$$

가 그 embedding이다. 이 map은 $p$에서만 $0$이 되므로, $P$ 위의 성분 $C_P$는 $P\setminus\{p\}$ 위의 line subbundle의 closure이다. $p$로 다가가는 방향에 따라 이 line의 극한이 $E_p$의 모든 직선을 훑으므로, $C_P$는 $p$ 위에서 fiber $E_p$ 전체를 포함한다. 또 두 성분은 각각 $P\setminus\{p\}$와 $L\setminus\{p\}$ 위에서 reduced한 vector bundle이므로 multiplicity $1$로 나타나고, $[C]=[C_P]+[C_L]$이다.

$C_L$은 vector bundle $E\vert_L$ 자신이므로 zero section으로 자르면 $0^![C_L]=[L]$이다. $C_P$의 기여를 계산하기 위해 $P$를 $p$에서 blowup한 $\pi:\widetilde{P}\rightarrow P$와 그 exceptional divisor $e$를 잡자. $\x_1,\x_2$는 $p$의 ideal을 생성하므로 $\pi^\ast(\x_1,\x_2)$는 $e$를 따라 정확히 한 번 사라지고, 따라서 위의 map은 $\pi$로 당긴 뒤 line subbundle

$$\Lambda=\pi^\ast\mathcal{O}_P(1)\otimes\mathcal{O}_{\widetilde{P}}(e)\hookrightarrow\pi^\ast E\vert_P$$

를 거친다. $\Lambda$의 total space는 $C_P$로 proper하고 birational하게 가므로, zero section의 Gysin map이 proper pushforward와 호환된다는 것과 subbundle을 zero section으로 자르면 quotient의 top Chern class가 남는다는 것에 의하여

$$0^![C_P]=\pi_\ast\bigl(c_1(\pi^\ast E\vert_P/\Lambda)\cap[\widetilde{P}]\bigr)=\pi_\ast\bigl((3\pi^\ast H-e)\cap[\widetilde{P}]\bigr)=3H\cap[P]$$

이다. 마지막 등식은 $e$가 한 점으로 수축되어 $\pi_\ast[e]=0$이기 때문이다. 따라서 $P$ 안의 직선을 $\ell$이라 하면

$$e(E,s)=3[\ell]+[L]\in A_1(Z)$$

이고, 곧 $(a,b)=(3,1)$이다.

이 값은 section을 흔들어서도 얻을 수 있다. 일반적인 이차식 $f,g$에 대해 $s_t=(\x_0\x_1+tf,\x_0\x_2+tg)$로 두면, 일반적인 $t\neq0$에서 $Z(s_t)$는 두 이차곡면의 smooth complete intersection, 곧 degree $4$의 곡선이고 $e(E,s_t)=[Z(s_t)]$이다. $t\rightarrow0$에서 이 곡선이 어디로 가는지 보자. $P$ 근방에서 $\x_0=tu$로 두면 두 방정식은 $u\x_1+f=0$, $u\x_2+g=0$이 되고 $u$를 소거하면 $\x_1g-\x_2f=0$이므로, 극한은 평면 cubic $C_3=\{\x_0=\x_1g-\x_2f=0\}$을 포함한다. 반면 $P$에서 떨어진 곳에서는 $\x_0$이 $0$으로 가지 않으므로 $\x_1,\x_2\rightarrow0$이 되어 극한이 $L$에 놓인다. 극한 cycle의 총 degree가 $4$이고 $C_3$, $L$의 degree가 각각 $3$, $1$이므로 둘 다 multiplicity $1$로 나타나며, 극한은 $[C_3]+[L]$이다. $A_1(P)$에서 $[C_3]=3[\ell]$이므로 이는 위의 계산과 정확히 일치한다.

이 일치는 위에서 본 대로 두 Gysin map의 순서를 바꾼 데에서 오며, 이때 $X\times\mathbb{A}^1$ 안의 전체 zero locus는 극한 곡선들을 포함하는 성분 외에 $P\times\{0\}$이라는 $2$차원 성분을 갖지만, 이 성분은 $t=0$의 fiber 안에 통째로 들어 있어서 Gysin pullback에서 trivial line bundle의 Euler class가 곱해지므로 기여가 $0$이다.
:::

기대 차원의 성분 $L$은 자기 자신 $[L]$만을 기여하고, 나머지 $3$은 기대보다 한 차원 큰 평면 $P$가 기여한다. 평면의 기여는 대략 excess bundle $E\vert_P/N_{P/X}$의 $c_1$, 곧 $4H-H$이고, $N_{P/X}\rightarrow E\vert_P$가 subbundle이 되지 못하는 점 $p$에서의 보정은 blowup으로 계산된다. 이 경우에는 그 보정이 pushforward에서 사라진다. 특히 $c_2(E)\cap[\mathbb{P}^3]$은 총합 $4$만을 알지만, localized Euler class는 이 $4$가 $Z$의 두 성분에 $3$과 $1$로 나뉘어 있다는 것까지 기억한다. 이 예시에서는 $A_1(Z)$가 성분별로 갈라지므로 이 분해가 class 자체의 정보이지만, 일반적으로는 normal cone의 성분별 기여가 $A_\ast(Z(s))$의 canonical한 분해를 주지는 않는다.

## Intrinsic normal cone

[예시 2](#ex2){: data-lid="3o76h" }의 계산에 쓰인 것은 $E\vert_Z$ 안의 normal cone $C_{Z/X}$ 하나였다. 그러나 일반적인 moduli $M$은 하나의 smooth variety 안의 zero locus로 전역적으로 표현되지 않고, étale-local하게만 그러한 표현을 가지며, 그 국소 표현들은 서로 다른 ambient를 갖는다. 문제는 normal cone이 ambient에 의존한다는 것이다. 가령 $Z=Z(s)\subset X$를 $X\times\mathbb{A}^1$ 안의 $Z\times\{0\}$으로 보면, 이는 $\mathbb{A}^1$의 coordinate $t$에 대하여 $\pr_1^\ast E\oplus\mathcal{O}$의 section $(s,t)$의 zero locus이고, 그 normal cone은 $C_{Z/X}\times\mathbb{A}^1\subset E\vert_Z\oplus\mathcal{O}_Z$로 한 차원 커진다. 그럼에도 zero section으로 자른 class는 바뀌지 않는데, 늘어난 $\mathbb{A}^1$ 방향이 cone과 bundle 양쪽에 똑같이 더해져 Gysin map에서 그대로 상쇄되기 때문이다. 이 늘어난 방향은 정확히 ambient의 늘어난 tangent 방향 $T_{\mathbb{A}^1}$이며, 이는 cone 자체가 아니라 cone을 ambient의 tangent 방향으로 나눈 것만이 의미를 갖는다는 것을 시사한다. 이 절에서는 이를 엄밀하게 만든다.

::: 명제 3
Scheme $Z$와 두 closed immersion $i:Z\hookrightarrow Y$, $i':Z\hookrightarrow Y'$, 그리고 smooth morphism $f:Y'\rightarrow Y$가 $f\circ i'=i$를 만족한다 하자. 그럼 normal cone들의 sequence

$$0\rightarrow i'^\ast T_{Y'/Y}\rightarrow C_{Z/Y'}\rightarrow C_{Z/Y}\rightarrow0$$

은 exact이다. 즉 étale-local하게 $C_{Z/Y'}\cong i'^\ast T_{Y'/Y}\times C_{Z/Y}$이고, $C_{Z/Y'}\rightarrow C_{Z/Y}$는 이 곱의 projection이다.
:::

::: 증명
주장은 étale-local하고, smooth morphism은 국소적으로 étale morphism $Y'\rightarrow Y\times\mathbb{A}^n$과 projection의 합성이며, normal cone은 ambient를 étale morphism으로 바꾸거나 $Y\times\mathbb{A}^n$의 $Y$ 위의 automorphism으로 옮겨도 변하지 않는다. 따라서 $Y=\Spec A$가 affine이고 $Y'=Y\times\mathbb{A}^n$, $i'=i\times\{0\}$인 경우, 곧 $Z\times\{0\}\subset Y\times\mathbb{A}^n$의 normal cone만 계산하면 된다. $Z$의 ideal을 $I\subseteq A$라 하면 $Z\times\{0\}$의 ideal은 $I'=I\cdot A[t_1,\ldots,t_n]+(t_1,\ldots,t_n)$이고, $A[t_1,\ldots,t_n]$을 monomial $t^\beta$들로 분해하면 $I'^k$의 $t^\beta$ 성분은 $I^{\max(k-\lvert\beta\rvert,0)}t^\beta$이다. 따라서

$$\bigoplus_{k\geq0}I'^k/I'^{k+1}\cong\Bigl(\bigoplus_{k\geq0}I^k/I^{k+1}\Bigr)[T_1,\ldots,T_n]$$

이고, 여기서 $T_j$는 $t_j$의 class이다. 곧 $C_{Z/Y'}=C_{Z/Y}\times\mathbb{A}^n$이며, 이 $\mathbb{A}^n$은 $Z$로 제한한 relative tangent bundle $i'^\ast T_{Y'/Y}$이다.
:::

이 명제는 앞서 본 $X\times\mathbb{A}^1$의 현상이 일반적으로 일어난다는 것이다. 즉 ambient를 smooth하게 키우면 cone은 정확히 늘어난 relative tangent 방향만큼 커진다. 그럼 cone을 ambient의 tangent 방향으로 나누고 싶은데, 그러려면 먼저 tangent 방향이 cone 위에 작용해야 한다. Smooth scheme $W$의 closed subscheme $U$에 대하여 $\mathcal{I}/\mathcal{I}^2\rightarrow\Omega_W\vert_U$의 dual은 morphism $T_W\vert_U\rightarrow N_{U/W}$를 주며, 여기서 $N_{U/W}=\Spec_U\Sym(\mathcal{I}/\mathcal{I}^2)$은 normal cone $C_{U/W}$를 담는 normal sheaf이다. $N_{U/W}$는 fiber별로 덧셈을 갖는 abelian cone이므로, $T_W\vert_U$는 이 morphism을 통해 $N_{U/W}$ 위에 평행이동으로 작용한다.

::: 명제 4
Smooth scheme $W$의 closed subscheme $U$에 대하여, normal cone $C_{U/W}\subset N_{U/W}$는 $T_W\vert_U$의 평행이동에 대해 불변이다.
:::

::: 증명
$U$를 대각선을 거쳐 $W\times W$ 안에 넣고 두 projection $p_1,p_2:W\times W\rightarrow W$를 생각하자. 둘 다 smooth이므로 [명제 3](#prop3){: data-lid="tnoek" }을 각각에 적용할 수 있으며, normal sheaf에 대해서도 같은 exact sequence가 성립한다. 먼저 $p_1$에 대한 [명제 3](#prop3){: data-lid="h13fg" }으로 $N_{U/W\times W}\cong T_W\vert_U\times N_{U/W}$, $C_{U/W\times W}\cong T_W\vert_U\times C_{U/W}$로 동일시하자. 대각선 $W\rightarrow W\times W$가 주는 $N_{U/W}\rightarrow N_{U/W\times W}$는 $p_1$과 $p_2$가 유도하는 두 map 모두의 section이고, 이로부터 위의 동일시 아래에서 $p_2$가 유도하는 $N_{U/W\times W}\rightarrow N_{U/W}$가 $(v,n)\mapsto v+n$, 곧 $T_W\vert_U$의 작용임을 확인할 수 있다. 한편 $p_2$에 대한 [명제 3](#prop3){: data-lid="2bynq" }에서 $C_{U/W\times W}$의 image는 $C_{U/W}$이므로, $T_W\vert_U\times C_{U/W}$의 작용 아래 image는 $C_{U/W}$ 안에 있다.
:::

[예시 2](#ex2){: data-lid="jsjlc" }에서 확인해 보면, 국소 모형에서 $T_X\vert_Z$는 $\dd{s}$를 통해 $E\vert_Z$에 작용한다. $P\setminus\{p\}$ 위에서 $s=\x_0(\x_1,\x_2)$의 미분의 image는 $(\x_1,\x_2)$가 생성하는 line, 곧 $C_P$의 fiber이므로 $C_P$는 이 평행이동으로 보존되고, $L$ 위에서는 $C_L$이 $E\vert_L$ 전체이므로 자명하다.

이제 vector bundle $F$가 cone $C$에 평행이동으로 작용할 때 그 quotient stack을 $[C/F]$로 적자. Deligne–Mumford stack $M$의 *local embedding*이란 affine scheme $U$에서의 étale morphism $U\rightarrow M$과 smooth affine scheme $W$로의 closed immersion $U\hookrightarrow W$의 쌍을 말한다. 두 local embedding $U\hookrightarrow W$, $U\hookrightarrow W'$이 주어지면 $U\hookrightarrow W\times W'$이 둘을 함께 지배하고 두 projection이 smooth이므로, [명제 3](#prop3){: data-lid="s6lja" }과 [명제 4](#prop4){: data-lid="zle0a" }에 의하여 $T_{W\times W'/W}$ 방향을 먼저 나누어

$$[C_{U/W\times W'}/T_{W\times W'}\vert_U]\cong[C_{U/W}/T_W\vert_U]$$

를 얻고, $W'$에 대해서도 같다. Normal sheaf에 대해서도 마찬가지이다. 즉 normal cone을 ambient의 tangent bundle로 나눈 quotient stack은 local embedding의 선택에 의존하지 않으며, 이들을 붙여 $M$ 위의 stack을 얻는다.

::: 정의 5
Deligne–Mumford stack $M$의 *intrinsic normal sheaf* $\mathfrak{N}_M$과 *intrinsic normal cone* $\mathfrak{c}_M\subset\mathfrak{N}_M$은 모든 local embedding $U\hookrightarrow W$에 대하여

$$\mathfrak{N}_M\vert_U=[N_{U/W}/T_W\vert_U],\qquad\mathfrak{c}_M\vert_U=[C_{U/W}/T_W\vert_U]$$

가 되도록 붙여서 얻은 stack이다.
:::

Intrinsic normal sheaf는 cotangent complex만으로도 적을 수 있다. Stack $M$은 cotangent complex $\LL_M$을 가지며, 그 가운데 deformation과 obstruction이 잡히는 것은 truncation $\tau_{\geq-1}\LL_M$이다. ([\[스킴\] §변형이론과 여접 복합체, §§변형의 장애와 고차 변형이론](/ko/math/scheme_theory/deformation_theory#변형의-장애와-고차-변형이론){: data-lid="0fpnl" }) Local embedding $U\hookrightarrow W$에서 $U$의 ideal sheaf를 $\mathcal{I}$라 하면 이 truncation은

$$\tau_{\geq-1}\LL_M\vert_U=\Bigl[\at{-1}{\mathcal{I}/\mathcal{I}^2}\xrightarrow{\ \dd{\ }}\at{0}{\Omega_W\vert_U}\Bigr]$$

이 된다. 한편 degree $0,1$에 놓인 abelian cone들의 complex $[G^0\rightarrow G^1]$에 대해 quotient stack $[G^1/G^0]$을 $h^1/h^0$으로 적으면, 이 stack은 complex의 quasi-isomorphism class에만 의존한다. 위 truncation의 각 항을 abelian cone $\Spec_U\Sym(-)$로 바꾸면 그 dual은 $[T_W\vert_U\rightarrow N_{U/W}]$이므로, 이 의미의 dual을 $(-)^\vee$로 적으면 $\mathfrak{N}_M=h^1/h^0((\tau_{\geq-1}\LL_M)^\vee)$이다. $M$이 smooth이면 $W=M$으로 잡을 수 있으므로 $\mathfrak{c}_M=\mathfrak{N}_M=[0/T_M]=BT_M$이다. 더 일반적으로 $M$이 local complete intersection이면 normal cone이 normal bundle과 같으므로 $\mathfrak{c}_M=\mathfrak{N}_M$은 vector bundle stack이고, 역도 성립한다. 즉 $\mathfrak{c}_M$과 $\mathfrak{N}_M$의 차이는 $M$이 local complete intersection에서 벗어난 정도를 잰다.

::: 명제 6
Intrinsic normal cone $\mathfrak{c}_M$은 pure dimension $0$이다.
:::

::: 증명
Local embedding $U\hookrightarrow W$에서 $W$가 pure dimension이라 하자. Normal cone $C_{U/W}$는 pure dimension $\dim W$이고, quotient map $C_{U/W}\rightarrow[C_{U/W}/T_W\vert_U]$는 $T_W\vert_U$-torsor이므로 relative dimension $\dim W$의 smooth surjection이다. 따라서 $\mathfrak{c}_M\vert_U$의 차원은 $\dim W-\dim W=0$이다.
:::

$M$이 smooth인 경우를 보면 이 $0$은 $BT_M$의 차원 $\dim M-\dim M$이다. 즉 차원 $0$이라는 것은 $\mathfrak{c}_M$이 normal 방향을 tangent 방향만큼 나눈 것이라는 데에서 오며, 이 수가 아래에서 virtual dimension을 고정한다.

Intrinsic normal sheaf와 cone은 deformation theory의 의미도 갖는다. 점 $p\in M$ 근방의 local embedding을 $\mathcal{I}\subseteq\mathfrak{m}_p^2$가 되도록 잡으면 $p$에서 $T_W\vert_p\rightarrow N_{U/W}\vert_p$가 $0$이 되어, $\mathfrak{N}_M$의 $p$에서의 fiber는 벡터공간 $(\mathcal{I}/\mathfrak{m}_p\mathcal{I})^\vee$로 coarse하게 표현된다. 이는 $M$의 $p$에서의 obstruction space 가운데 가장 작은 것, 곧 universal obstruction space이며 ([BF, Lemma 4.6]), 그 모든 원소는 어떤 small extension의 obstruction으로 나타난다. 이 공간은 $\Ext^1(\LL_M\vert_p,k)$와 같다. Nakayama lemma에 의해 이 공간이 $0$인 것은 $p$ 근방에서 $\mathcal{I}=0$, 곧 $U=W$인 것과 동치이고, $\mathcal{I}\subseteq\mathfrak{m}_p^2$이므로 이는 $M$이 $p$에서 smooth한 것과 동치이다. 이 공간의 원소 가운데 curvilinear small extension, 곧 $p$를 지나는 jet $\Spec k[t]/(t^n)\rightarrow M$을 한 차수 늘리는 문제의 obstruction으로 나타나는 것은 정확히 $\mathfrak{c}_M$의 fiber의 원소들이다. ([BF, Proposition 4.7]) 즉 $\mathfrak{N}_M$이 가능한 obstruction 방향 전체라면, $\mathfrak{c}_M$은 $M$ 안의 곡선 조각을 늘리려 할 때 부딪히는 obstruction 방향들이다.

국소 모형 $Z=Z(s)\subset X$에서는 이 대응을 직접 볼 수 있다. 점 $p$를 지나는 jet $\gamma:\Spec k[t]/(t^n)\rightarrow Z$를 한 차수 늘리려면, $X$가 smooth하므로 먼저 $X$ 안에서 $\widetilde{\gamma}:\Spec k[t]/(t^{n+1})\rightarrow X$로 늘린 뒤 $s$가 사라지도록 고칠 수 있는지 보면 된다. $\gamma^\ast s=0$이므로 $\widetilde{\gamma}^\ast s=t^nc$인 $c\in E_p$가 있고, $\widetilde{\gamma}$를 $t^nv$ ($v\in T_{X,p}$)만큼 바꾸면 $c$는 $\dd{s}(v)$만큼 바뀌므로, 이 문제의 obstruction은 $E_p/\dd{s}(T_{X,p})$ 안의 $c$의 class이다. 한편 $\widetilde{\gamma}$를 arc $\Spec k[[t]]\rightarrow X$로 더 늘리면 $\mathcal{I}^j$의 원소는 그 위에서 $t^{nj}$로 나누어떨어지므로, $f\in\mathcal{I}^j$에 그 $t^{nj}$의 계수를 대응시키는 algebra map $\bigoplus_j\mathcal{I}^j/\mathcal{I}^{j+1}\rightarrow k$, 곧 $C_{Z/X}$의 $p$ 위의 점을 얻는다. 이 점을 $E^\vee\rightarrow\mathcal{I}/\mathcal{I}^2$을 거쳐 $E_p$ 안에서 보면 $c$이므로, $c$는 $C_{Z/X}$의 fiber에 속한다. 즉 곡선 조각을 늘릴 때의 obstruction은 $s$를 그 곡선을 따라 당긴 것의 $t^n$의 계수가 $E_p/\dd{s}(T_{X,p})$에서 갖는 class이고, normal cone은 이러한 계수들이 놓이는 곳이다. [예시 2](#ex2){: data-lid="zg3iy" }의 점 $p$에서는 $\x_3=1$인 affine 좌표에서 $\mathcal{I}=(\x_0\x_1,\x_0\x_2)\subseteq\mathfrak{m}_p^2$이므로 $p$에서 $\dd{s}=0$이고, 방향 $(a_0,a_1,a_2)$의 $1$차 jet $(a_0t,a_1t,a_2t)$, 곧 $n=2$인 경우에 $\widetilde{\gamma}^\ast s=t^2a_0(a_1,a_2)$이다. 따라서 $P$에도 $L$에도 접하지 않는 방향, 곧 $a_0\neq0$이고 $(a_1,a_2)\neq0$인 방향의 $1$차 jet은 $Z$ 안에서 $2$차로 늘어나지 않으며, 이러한 방향들의 obstruction $a_0(a_1,a_2)$는 $E_p$의 $0$이 아닌 모든 벡터를 지난다. 이는 $C_P$가 $p$ 위에서 fiber $E_p$ 전체를 포함한다는 [예시 2](#ex2){: data-lid="z7xf5" }의 계산과 맞는다.

## Perfect obstruction theory

[§§벡터다발의 zero locus](#벡터다발의-zero-locus){: data-lid="uemf3" }의 모형에서 $Z(s)$의 국소 deformation과 obstruction 자료는 그 미분 $\dd{s}$가 tangent space와 obstruction space를 이어 주는 tangent 방향의 complex

$$\Bigl[\at{0}{T_X\vert_{Z(s)}}\xrightarrow{\ \dd{s}\ }\at{1}{E\vert_{Z(s)}}\Bigr]$$

에 온전히 담겨 있었다. 보편적으로 대수기하학에서 우리는 cotangent 방향을 살펴보므로 이 complex를 dualize하여 degree $-1$과 $0$에 놓이는 complex로 적으면

$$E^\bullet=\Bigl[\at{-1}{E^\vee\vert_{Z(s)}}\xrightarrow{\ (\dd{s})^\vee\ }\at{0}{\Omega_X\vert_{Z(s)}}\Bigr]$$

을 얻고, 이 complex에 $R\Hom(-,\mathcal{O}_{Z(s)})$을 적용하여 원래의 tangent 방향을 복원하면 그 cohomology

$$h^0((E^\bullet)^\vee)=\ker(\dd{s}),\qquad h^1((E^\bullet)^\vee)=\coker(T_X\vert_{Z(s)}\rightarrow E\vert_{Z(s)})$$

가 tangent space와 obstruction space를 준다.

이 모형에서 intrinsic normal cone은 $\mathfrak{c}_{Z(s)}=[C_{Z(s)/X}/T_X\vert_{Z(s)}]$이고, 이는 위의 tangent 방향의 complex로 만든 vector bundle stack $[E\vert_{Z(s)}/T_X\vert_{Z(s)}]$ 안에 놓인다. Localized Euler class는 이 cone을 $E\vert_{Z(s)}$로 끌어올린 $C_{Z(s)/X}$를 zero section으로 자른 것이었다. 일반적인 $M$에서도 $\mathfrak{c}_M$은 $\mathfrak{N}_M=h^1/h^0((\tau_{\geq-1}\LL_M)^\vee)$ 안에 놓이지만, 문제는 일반적인 $M$에서 $\mathcal{I}/\mathcal{I}^2$은 vector bundle이 아니라는 것으로, $\mathfrak{N}_M$은 vector bundle stack이 아니어서 그 zero section이나 Gysin map을 정의할 수 없다. 때문에 우리는 이 정보를 모두 담을 수 있는 실제 vector bundle들의 two-term complex를 생각해야 하며, 이것이 바로 다음의 정의이다.

::: 정의 7 (Behrend–Fantechi)
$M$을 Deligne–Mumford stack이라 하자. $M$ 위의 *perfect obstruction theory<sub>완전 장애 이론</sub>*란 국소적으로 vector bundle 두 항의 complex $[E^{-1}\rightarrow E^0]$과 quasi-isomorphic한 complex $E^\bullet$과 morphism

$$\phi:E^\bullet\rightarrow\tau_{\geq-1}\LL_M$$

의 쌍으로서, $h^0(\phi)$가 isomorphism이고 $h^{-1}(\phi)$가 surjection인 것을 말한다.
:::

이 정의에서, 우선 $h^0(\phi)$가 isomorphism이라는 것은 $E^\bullet$의 $0$차 항이 $M$의 deformation을 정확히 재현한다는 뜻이다. 수정이 필요했던 부분은 원래 $\mathcal{I}/\mathcal{I}^2$ 쪽이 들어있던 $-1$항으로, 여기에서 $h^{-1}(\phi)$가 surjection이라는 것은 $E^\bullet$의 $-1$차 항이 $M$의 obstruction을 <em-ko>빠짐없이</em-ko> 지배한다는 뜻이다. 즉, $E^\bullet$ 쪽에 실제보다 많은 obstruction이 있는 것은 허용되지만 하나라도 빠뜨리는 것은 허용되지 않는다. 두 조건이 함께 성립한다는 것은 $M$의 intrinsic normal sheaf $\mathfrak{N}_M$, 곧 가능한 모든 obstruction 방향이 $E^\bullet$이 정하는 vector bundle stack 안에 closed하게 들어간다는 것과 동치이며, 이는 [정리 8](#thm8){: data-lid="4u3le" }에서 정확히 보인다.

정확히 말하면, $\phi$의 dual은 cone stack 사이의 morphism $\phi^\vee:\mathfrak{N}_M\rightarrow\mathfrak{E}=h^1/h^0((E^\bullet)^\vee)$를 유도하며, 국소적으로 $E^\bullet=[E^{-1}\rightarrow E^0]$이면 $E_i=(E^{-i})^\vee$에 대하여 $\mathfrak{E}=[E_1/E_0]$이다. 이는 $\tau_{\geq-1}\LL_M$으로부터 $\mathfrak{N}_M$을 얻은 것과 같은 구성이다. 다음 정리는 [BF, Proposition 2.6]을 cotangent complex에 적용한 것으로, [BF, Theorem 4.5]의 일부이다.

::: 정리 8 (Behrend–Fantechi)
Deligne–Mumford stack $M$ 위에서 국소적으로 vector bundle 두 항의 complex와 quasi-isomorphic한 $E^\bullet$과 morphism $\phi:E^\bullet\rightarrow\tau_{\geq-1}\LL_M$에 대하여 다음은 동치이다.

1. $h^0(\phi)$는 isomorphism이고 $h^{-1}(\phi)$는 surjection이다.
2. $\phi^\vee:\mathfrak{N}_M\rightarrow\mathfrak{E}$는 closed immersion이다.
:::

::: 증명
주장은 étale-local하므로 local embedding $U\hookrightarrow W$ 위에서 $\tau_{\geq-1}\LL_M\vert_U=[\mathcal{I}/\mathcal{I}^2\rightarrow\Omega_W\vert_U]$라 하자. 두 조건은 모두 $h^0(\phi)$가 surjective임을 함의한다. 첫째 조건에서는 자명하고, 둘째 조건에서는 closed immersion이 representable이며 $\phi^\vee$가 representable인 것은 $h^0(\phi)$가 surjective인 것과 동치이기 때문이다. ([BF, Proposition 2.5]) 이 경우 국소적으로, 필요하면 $W$를 $W\times\mathbb{A}^m$으로 키워서, $\phi$를 $E^0=\Omega_W\vert_U$이며 degree $0$의 성분이 identity인 chain map으로 표현할 수 있으므로 이 표현에서 보이면 충분하다. 그럼 $\phi$는 $\phi^{-1}:E^{-1}\rightarrow\mathcal{I}/\mathcal{I}^2$ 하나로 결정되고, 첫째 조건은 $\phi^{-1}$이 surjective라는 것과 동치이다.

실제로 $\phi^{-1}$이 surjective이면 두 complex에서 $\Omega_W\vert_U$로 가는 map의 image가 같으므로 $h^0(\phi)$는 isomorphism이다. 또 $\ker(\mathcal{I}/\mathcal{I}^2\rightarrow\Omega_W\vert_U)$의 원소의 $E^{-1}$에서의 lift는 자동으로 $\ker(E^{-1}\rightarrow\Omega_W\vert_U)$에 속하므로 $h^{-1}(\phi)$는 surjection이다. 역으로 첫째 조건을 가정하고 $b\in\mathcal{I}/\mathcal{I}^2$를 택하자. $h^0(\phi)$가 injective이므로 $\dd{b}$는 $E^{-1}$의 image에 속하고, 따라서 $\dd{b}=\dd{\phi^{-1}(a)}$인 $a\in E^{-1}$이 있다. 그럼 $b-\phi^{-1}(a)$는 $h^{-1}(\tau_{\geq-1}\LL_M\vert_U)$의 원소이므로, $h^{-1}(\phi)$가 surjective라는 것에서 $\ker(E^{-1}\rightarrow\Omega_W\vert_U)$의 원소 $a'$에 대해 $\phi^{-1}(a')$으로 쓸 수 있다. 곧 $b=\phi^{-1}(a+a')$이다.

이제 $\phi^{-1}:E^{-1}\rightarrow\mathcal{I}/\mathcal{I}^2$이 surjective라는 것은 $\Sym$을 취한 algebra map이 surjective라는 것, 곧

$$N_{U/W}=\Spec_U\Sym(\mathcal{I}/\mathcal{I}^2)\rightarrow\Spec_U\Sym(E^{-1})=E_1$$

이 closed immersion이라는 것과 동치이다. 이 map은 양쪽에 작용하는 같은 vector bundle $E_0=T_W\vert_U$의 작용과 호환되므로, quotient로 내려 $\mathfrak{N}_M\vert_U\rightarrow\mathfrak{E}\vert_U$가 closed immersion이라는 것과 동치이다.
:::

이로부터 [정의 7](#def7){: data-lid="3zi1b" }의 두 조건이 하는 일을 정확히 말할 수 있다. $h^0(\phi)$의 전사는 $\phi^\vee$가 representable이라는 것과 동치이며, 국소적으로는 $\mathfrak{E}$를 나누는 $E_0$를 $\mathfrak{N}_M$을 나누는 ambient의 tangent 방향 $T_W\vert_U$로 맞춘 정규형을 가능하게 한다. 이 정규형에서 $h^0(\phi)$의 단사와 $h^{-1}(\phi)$의 전사는 함께 $\phi^{-1}:E^{-1}\rightarrow\mathcal{I}/\mathcal{I}^2$의 전사와 동치이고, 이것이 normal sheaf, 곧 가능한 obstruction 방향 전체를 $E_1$ 안에 closed하게 넣는다. 점 $p$에서 보면 $\phi^\vee$는 앞 절에서 본 universal obstruction space $\Ext^1(\LL_M\vert_p,k)$에서 $\phi$의 obstruction space $h^1((E^\bullet)^\vee\vert_p)$로 가는 injective map을 주므로, 어떤 perfect obstruction theory의 obstruction space도 universal obstruction space를 포함한다.

이 절의 처음에 $Z(s)\hookrightarrow X$로부터 만든 complex $E^\bullet$에서 truncation

$$\tau_{\geq-1}\LL_{Z(s)}=[\at{-1}{\mathcal{I}/\mathcal{I}^2}\rightarrow\at{0}{\Omega_X\vert_{Z(s)}}]$$

으로 가는 morphism $\phi:E^\bullet\rightarrow\tau_{\geq-1}\LL_{Z(s)}$는 다음의 diagram

{% diagram Math/Gromov_Witten_Theory/Perfect_Obstruction_Theory-1.svg width="10.88em" alt="morphism from the local complex to the truncated cotangent complex" %}

으로 주어지는 것이다. 특히 degree $-1$에서는 section $s$와의 pairing $s^\vee:E^\vee\rightarrow\mathcal{O}_X$를 $\mathcal{I}/\mathcal{I}^2$으로 내린 것으로 정의되는 것이며, 이는 $s^\vee$의 image가 정확히 $\mathcal{I}$이므로 surjection이 되기 때문에 이 complex는 실제로 perfect obstruction theory가 된다.

Perfect obstruction theory는 $M$만으로 정해지는 것이 아니라 $M$ 위에 추가로 주어지는 자료이며, 같은 $M$ 위에도 서로 다른 perfect obstruction theory가 있을 수 있다. 앞으로 정의할 virtual class는 이 선택에 의존한다.

::: 예시 9
$\mathbb{P}^2$ 안의 직선 $L=\{\x=0\}$을 두 가지 방식으로 zero locus로 표현하자. 하나는 $E=\mathcal{O}(1)^{\oplus2}$와 $s=(\x,\x)$이고, 다른 하나는 $E'=\mathcal{O}(1)\oplus\mathcal{O}(2)$와 $s'=(\x,\x^2)$이다. 두 ideal $(\x,\x)$와 $(\x,\x^2)$는 모두 $(\x)$이므로 $Z(s)=Z(s')=L$이고, 위에서 본 것처럼 각각은 $L$ 위의 perfect obstruction theory를 주며 그 virtual dimension은 모두 $2-2=0$이다.

$L$은 Cartier divisor이므로 normal cone은 line bundle $N_{L/\mathbb{P}^2}=\mathcal{O}_L(1)$이고, 이것이 $E\vert_L$ 또는 $E'\vert_L$ 안에 놓이는 방식은 $\mathcal{I}/\mathcal{I}^2=\mathcal{O}_L(-1)$로 가는 map의 dual로 주어진다. 첫째 경우에는 두 기저가 모두 $\x$로 가므로 이 embedding은

$$N_{L/\mathbb{P}^2}\xrightarrow{(1,1)}\mathcal{O}_L(1)^{\oplus2}$$

이고, 둘째 경우에는 $\x^2\in\mathcal{I}^2$이므로

$$N_{L/\mathbb{P}^2}\xrightarrow{(1,0)}\mathcal{O}_L(1)\oplus\mathcal{O}_L(2)$$

이다. 둘 다 subbundle이므로 zero section으로 자르면 quotient line bundle의 $c_1$이 남고, 그 degree는 각각 $\deg\mathcal{O}_L(1)=1$과 $\deg\mathcal{O}_L(2)=2$이다. 이는 $c_2(E)=H^2$, $c_2(E')=2H^2$과도 맞는다.
:::

즉 같은 scheme $L$이 같은 차원의 서로 다른 두 class를 갖는다. 두 perfect obstruction theory는 같은 intrinsic normal cone $\mathfrak{c}_L$을 서로 다른 $\mathfrak{E}$ 안에 넣은 것이다. [예시 1](#ex1){: data-lid="42vb0" }도 같은 현상을 보여 준다. Smooth한 $\mathbb{P}^2$에는 $\Omega_{\mathbb{P}^2}$ 자신이라는 perfect obstruction theory가 있어 $[\mathbb{P}^2]$를 주지만, $\mathcal{O}(1)^{\oplus2}$의 zero section $s\equiv0$으로 본 perfect obstruction theory는 차원이 $2$ 작은 point class를 준다. 따라서 virtual class를 fundamental class를 대체하는 올바른 차원의 class라고 부를 때, 그 차원과 class를 고르는 것은 공간이 아니라 $\phi$이다. Stable map의 경우 이 선택은 [명제 12](#prop12){: data-lid="ilo5d" }의 $(R\pi_\ast\mu^\ast T_X)^\vee$로 고정되며, 서로 다른 moduli의 virtual class를 비교하려면 [명제 14](#prop14){: data-lid="5f8c5" }처럼 두 perfect obstruction theory의 compatibility를 따로 확인해야 하는 이유가 여기에 있다.

## 가상 기본류의 구성

Perfect obstruction theory $\phi:E^\bullet\rightarrow\tau_{\geq-1}\LL_M$이 주어지면 [정리 8](#thm8){: data-lid="3duhl" }에 의하여 pure dimension $0$의 closed substack

$$\mathfrak{c}_M\subset\mathfrak{N}_M\hookrightarrow\mathfrak{E}$$

를 얻으며, [BF]는 $\mathfrak{E}$ 안의 이 substack을 $\phi$의 *obstruction cone*이라 부른다. Virtual class는 obstruction cone을 $\mathfrak{E}$의 zero section으로 자른 것이다.

다만 $\mathfrak{E}$는 Artin stack이므로 그 zero section으로 Gysin map을 정의하려면 Artin stack의 Chow group이 필요하다. 이를 피하기 위해 [BF]는 $E^\bullet$이 *global resolution*, 곧 vector bundle들의 complex $F^\bullet=[F^{-1}\rightarrow F^0]$과의 isomorphism $F^\bullet\cong E^\bullet$을 갖는다고 가정한다. 이 때 $F_i=(F^{-i})^\vee$로 두면 $\mathfrak{E}=[F_1/F_0]$이고, $F_1$은 $\mathfrak{E}$를 덮는 실제 vector bundle이 된다.

::: 정의 10
Deligne–Mumford stack $M$ 위의 perfect obstruction theory $E^\bullet$이 global resolution $F^\bullet$을 갖는다 하자. Fiber product

$$C(F^\bullet)=\mathfrak{c}_M\times_{\mathfrak{E}}F_1\subset F_1$$

에 대하여, $M$의 *virtual fundamental class*를

$$[M]^\vir=0^!_{F_1}[C(F^\bullet)]$$

로 정의한다. 이를 $0^!_{E^\bullet}[\mathfrak{c}_M]$으로도 적는다.
:::

[§§벡터다발의 zero locus](#벡터다발의-zero-locus){: data-lid="70ezs" }의 국소 모형에서는 $F_0=T_X\vert_Z$, $F_1=E\vert_Z$이고 $C(F^\bullet)$은 $\mathfrak{c}_Z=[C_{Z/X}/T_X\vert_Z]$를 $E\vert_Z$로 끌어올린 것, 곧 $C_{Z/X}$ 자신이므로, [정의 10](#def10){: data-lid="o4y0p" }은 localized Euler class $e(E,s)$를 그대로 돌려준다. [예시 2](#ex2){: data-lid="nhbvj" }의 계산이 정확히 이 정의의 계산이었다.

차원은 다음과 같이 맞는다. $F_1\rightarrow\mathfrak{E}=[F_1/F_0]$은 $F_0$-torsor이므로 이를 당긴 $C(F^\bullet)\rightarrow\mathfrak{c}_M$도 relative dimension $\rank F_0$의 smooth surjection이고, [명제 6](#prop6){: data-lid="w91yv" }에 의해 $C(F^\bullet)$은 pure dimension $\rank F_0$이다. 이를 rank $\rank F_1$의 vector bundle의 zero section으로 자르면 차원이 $\rank F_1$만큼 떨어지므로

$$\dim[M]^\vir=\rank F_0-\rank F_1=\rank E^\bullet=\vdim$$

이다. 즉 virtual dimension은 차원 $0$의 cone을 relative dimension $-\vdim$의 vector bundle stack 안에서 zero section과 교차시킨 결과이며, 그 차원을 고정하는 것은 [명제 6](#prop6){: data-lid="o80lg" }의 purity이다.

Global resolution의 선택은 결과에 영향을 주지 않는다. ([BF, Proposition 5.3]) 위에서 본 대로 virtual class는 $\mathfrak{E}$ 안의 obstruction cone을 zero section으로 자른 것이고, $F_1$은 이 교차를 vector bundle 위에서 계산하기 위해 고른, $\mathfrak{E}$를 덮는 vector bundle일 뿐이다.

국소적으로 보면 $M$은 étale-local하게 어떤 smooth $W$ 위의 vector bundle의 section의 zero locus로 표현되고, 그곳에서 $[M]^\vir$은 그 section의 localized Euler class이다. 점 $p$ 근방에서는 $W$의 차원을 tangent space $h^0((E^\bullet)^\vee\vert_p)$의 차원으로, vector bundle의 rank를 $\phi$의 obstruction space $h^1((E^\bullet)^\vee\vert_p)$의 차원으로 잡을 수 있고, 이때 section의 미분은 $p$에서 $0$이다. 이러한 국소 표현의 section들은 서로 붙지 않지만, cone을 tangent 방향으로 나눈 $[C_{U/W}/T_W\vert_U]$는 [명제 3](#prop3){: data-lid="vpmbx" }과 [명제 4](#prop4){: data-lid="4opte" }에 의해 $\mathfrak{c}_M$으로 붙고, 그것이 정규형에서 $[E_1/T_W\vert_U]\cong\mathfrak{E}\vert_U$ 안에 놓이는 방식은 전역적으로 주어진 $\phi$가 정한다. Virtual fundamental class를 국소적인 localized Euler class들을 붙인 것이라고 할 때 그 정확한 뜻이 이것이다.

[예시 9](#ex9){: data-lid="sjvy4" }의 관찰을 극단까지 밀면 다음과 같다. Perfect obstruction theory $E^\bullet$에 $\mathcal{O}_M[1]$을 직합하고 $\phi$를 그 성분에서 $0$으로 연장해도 [정의 7](#def7){: data-lid="rtwgi" }의 두 조건은 그대로 유지되므로 다시 perfect obstruction theory를 얻는다. 이 때 $F_1$에 trivial line bundle이 더해지지만 cone은 그 방향으로 전혀 뻗지 않아 $C(F^\bullet)\times\{0\}$이 되고, 그 virtual class는 $c_1(\mathcal{O})\cap[M]^\vir=0$이다. 같은 $M$과 같은 $\mathfrak{c}_M$에서 class가 사라진 것이다.

이 구성은 base 위에서도 그대로 할 수 있다. $\mathfrak{B}$를 pure dimensional인 smooth Artin stack, $q:M\rightarrow\mathfrak{B}$를 Deligne–Mumford stack $M$에서의 morphism이라 하고, [정의 7](#def7){: data-lid="5uak4" }에서 $\tau_{\geq-1}\LL_M$을 $\tau_{\geq-1}\LL_{M/\mathfrak{B}}$로 바꾼 것을 $q$에 대한 *relative perfect obstruction theory*라 부르자. Local embedding $U\hookrightarrow W$를 $W$가 $\mathfrak{B}$ 위에서 smooth하도록 잡고 $T_W\vert_U$ 대신 relative tangent bundle $T_{W/\mathfrak{B}}\vert_U$로 나누면 *relative intrinsic normal cone* $\mathfrak{c}_{M/\mathfrak{B}}$를 얻으며, [정리 8](#thm8){: data-lid="bdguf" }과 [정의 10](#def10){: data-lid="kzesu" }은 그대로 성립한다. ([BF, §7]) 달라지는 것은 차원이다. $C_{U/W}$는 pure dimension $\dim W$이고 $T_{W/\mathfrak{B}}$의 rank는 $\dim W-\dim\mathfrak{B}$이므로, [명제 6](#prop6){: data-lid="8mnqd" }의 증명과 같은 차원 세기로 $\mathfrak{c}_{M/\mathfrak{B}}$는 pure dimension $\dim\mathfrak{B}$이고, virtual class $[M]^\vir$은 $A_{\dim\mathfrak{B}+\rank E^\bullet}(M)$에 놓인다. 아래 [명제 11](#prop11){: data-lid="av5wc" }의 (3)과 (4)도 smooth를 $\mathfrak{B}$ 위에서 smooth로 바꾸면 그대로 성립한다. ([BF, Proposition 7.3])

::: 명제 11
Deligne–Mumford stack $M$ 위의 perfect obstruction theory $\phi:E^\bullet\rightarrow\tau_{\geq-1}\LL_M$에 대하여, virtual class $[M]^\vir=0^!_{E^\bullet}[\mathfrak{c}_M]$은 다음을 만족한다.

1. $[M]^\vir$은 virtual dimension $\vdim=\rank E^\bullet=\rank E^0-\rank E^{-1}$의 cycle이다.
2. $M$이 flat family의 fiber로 주어지고 $\phi$가 family 위의 perfect obstruction theory와 compatible하면, $[M]^\vir$은 family의 virtual class를 fiber로 Gysin pullback한 것이다. 특히 $[M]^\vir$은 family 안에서의 deformation에 대해 불변이다.
3. $h^1((E^\bullet)^\vee)=0$이면 $M$은 smooth하고 $[M]^\vir=[M]$은 보통의 fundamental class이다.
4. $M$이 smooth하고 $h^1((E^\bullet)^\vee)$가 rank $r$의 vector bundle이면 $[M]^\vir=c_r(h^1((E^\bullet)^\vee))\cap[M]$이다.
:::

(1)은 위의 차원 세기이다. (3)과 (4)에서는 cone이 무엇인지 직접 볼 수 있다. $M$이 smooth이면 $\mathfrak{c}_M=BT_M$이므로 $C(F^\bullet)$은 $F_1$의 zero section의 $F_0$-orbit, 곧 $F_0\rightarrow F_1$의 image이다. (3)에서는 이 map이 surjective이므로 $C(F^\bullet)=F_1$이고, zero section으로 자르면 $[M]$이 남는다. (4)에서는 그 image가 cokernel $h^1((E^\bullet)^\vee)$가 vector bundle인 subbundle이므로, zero section으로 자르면 quotient의 top Chern class가 남는다. ([BF, Proposition 5.6]) 두 경우 모두 cone은 $F_1$의 subbundle이었고, [예시 2](#ex2){: data-lid="kqv83" }는 cone이 subbundle이 아닌 경우였다.

(2)의 compatible은 다음을 뜻한다. $\mathcal{X}$를 smooth variety $B$ 위의 Deligne–Mumford stack, $\phi_{\mathcal{X}}:E_{\mathcal{X}}^\bullet\rightarrow\tau_{\geq-1}\LL_{\mathcal{X}}$를 그 perfect obstruction theory, $M$을 점 $b\in B$ 위의 fiber, $i:M\hookrightarrow\mathcal{X}$라 하자. $\{b\}\hookrightarrow B$의 cotangent complex를 $M$으로 당기면 $\mathcal{O}_M^{\oplus\dim B}[1]$이고, $\phi$와 $\phi_{\mathcal{X}}$가 compatible하다는 것은 triangle $i^\ast E_{\mathcal{X}}^\bullet\rightarrow E^\bullet\rightarrow\mathcal{O}_M^{\oplus\dim B}[1]\rightarrow i^\ast E_{\mathcal{X}}^\bullet[1]$이 있어서 이것이 cotangent complex의 triangle $i^\ast\LL_{\mathcal{X}}\rightarrow\LL_M\rightarrow\LL_{M/\mathcal{X}}\rightarrow i^\ast\LL_{\mathcal{X}}[1]$로 가는 morphism of triangles를 이룬다는 것이다. ([BF, Definition 5.8, Proposition 5.10]) 이 자료는 $M$의 vector bundle stack을 $\mathcal{X}$의 것을 당긴 것과 normal 방향 $\mathcal{O}_M^{\oplus\dim B}$로 이루어진 short exact sequence에 넣어, 두 cone을 같은 곳에서 비교할 수 있게 해 준다. 한편 $\mathcal{X}$가 $B$ 상대 perfect obstruction theory를 가지면 이를 $M$으로 당긴 것이 $M$의 perfect obstruction theory이고, 이 두 perfect obstruction theory로 정의한 virtual class에 대해서는 $\mathcal{X}\rightarrow B$가 flat이 아니어도 $[M]^\vir=i_b^![\mathcal{X}]^\vir$이다. 여기서 $i_b^!$은 $\{b\}\hookrightarrow B$의 refined Gysin map이다. ([BF, Proposition 7.2]) $\{b\}\hookrightarrow B$ 대신 base를 smooth Artin stack 사이의 flat morphism이나 regular local immersion을 따라 바꾸어도, 바꾼 뒤의 total space가 Deligne–Mumford stack이면 같은 등식이 성립한다. 특히 $B$가 connected이고 $\mathcal{X}$가 $B$ 위에서 proper이면, $\mathcal{X}$ 위의 cohomology class를 $M$으로 제한하여 $[M]^\vir$ 위에서 적분한 값은 $b$에 의존하지 않는다.

국소 모형에서 이 등식은 [예시 2](#ex2){: data-lid="l5vhl" } 끝에서 본 것처럼 두 Gysin map의 순서를 바꾼 것이다. 그 예시의 family $\{(x,t)\in\mathbb{P}^3\times\mathbb{A}^1\mid s_t(x)=0\}\rightarrow\mathbb{A}^1$은 $t=0$의 fiber 안에 통째로 든 성분 $P\times\{0\}$ 때문에 flat이 아니고, 이 성분 위에서 family 쪽 normal cone은 $E\vert_P$ 전체이지만 fiber의 normal cone $C_P$는 그보다 한 차원 작다. 일반적으로도 base를 바꾸면 새 base 위의 relative intrinsic normal cone은 원래 cone을 당긴 것의 closed substack이고, 바꾸는 morphism이 flat이면 둘은 같지만 fiber로 제한하는 경우처럼 flat이 아니면 같지 않을 수 있다. ([BF, Proposition 7.1]) 따라서 등식은 cone을 fiber로 그대로 제한해서 얻는 것이 아니다. Family의 cone의 class를 $i_b^!$로 당긴 것이 fiber의 cone의 class와 rationally equivalent하고 ([BF, Proposition 7.2]), zero section의 Gysin map이 $i_b^!$와 교환하기 때문이다. [예시 2](#ex2){: data-lid="86gcf" }에서 $P\times\{0\}$ 위의 $E\vert_P$는 $i_0^!$에서 trivial line bundle의 Euler class가 곱해져 사라지는 부분이었다.

## 안정사상들의 가상 기본류

이제 stable map들의 moduli stack $M=\overline{\mathcal{M}}_{g,n}(X,\beta)$ 위에 perfect obstruction theory를 구성하자. 이를 위해 우리는 target $X$의 tangent space $T_X$를

$$\pi:\mathcal{C}\rightarrow M,\qquad\mu:\mathcal{C}\rightarrow X$$

를 사용하여 가지고 온다. 즉 $T_X$를 $\mu$를 사용하여 pullback해온 후, 이를 다시 $R\pi_\ast$를 사용하여 밀어내린 $R\pi_\ast\mu^\ast T_X$를 사용하는 것이다. 이 때 곡선의 차원이 $1$이므로 higher direct image $R^i\pi_\ast$는 $i=0,1$에서만 살아남게 되며, 따라서 이 complex는 정확히 degree $0$과 $1$에 놓이는 two-term complex가 되고 각 점에서 $H^0(C,\mu^\ast T_X)$와 $H^1(C,\mu^\ast T_X)$를 그 cohomology로 복원한다. 

따라서 위에서 얻은 $R\pi_\ast\mu^\ast T_X$의 dual $E^\bullet=(R\pi_\ast\mu^\ast T_X)^\vee$는 $[-1,0]$ amplitude의 complex로, 우리가 원하는 perfect obstruction theory의 후보가 된다. 다만 이는 domain curve $(C,p_\bullet)$을 고정한 채 map $\mu$만을 변형하는 자료이므로, prestable curve들의 moduli stack $\mathfrak{M}_{g,n}$으로 가는 morphism $q:M\rightarrow\mathfrak{M}_{g,n}$에 대한 relative perfect obstruction theory를 이룬다. 여기서 우리를 도와주는 것은 base stack $\mathfrak{M}_{g,n}$이 smooth하다는 것으로, 직관적으로 이는 node를 펼 때는 어떠한 obstruction도 없기 때문이다. 즉 $\mathfrak{M}_{g,n}$에는 perfect obstruction theory 없이도 이미 (진짜) fundamental class가 있고, 이를 relative perfect obstruction theory로 가져올 수 있다. 

::: 명제 12 (Behrend)
$M=\overline{\mathcal{M}}_{g,n}(X,\beta)$와 forgetful morphism $q:M\rightarrow\mathfrak{M}_{g,n}$에 대하여, 위의 complex $E^\bullet=(R\pi_\ast\mu^\ast T_X)^\vee$는 $q$에 대한 relative perfect obstruction theory $\phi:E^\bullet\rightarrow\LL_{M/\mathfrak{M}_{g,n}}$를 이룬다. 이는 $M$ 위의 (absolute) perfect obstruction theory $(E')^\bullet\rightarrow\tau_{\geq-1}\LL_M$을 유도하며, 이로부터 얻어지는 $M$의
 virtual class $[M]^\vir$의 차원은 virtual dimension

$$\vdim=\int_\beta c_1(T_X)+(\dim X-3)(1-g)+n$$

이다.
:::

이에 대한 증명 전략은 우선 target쪽에서 $T_X$로 만든 relative complex $(R\pi_\ast\mu^\ast T_X)^\vee$와 그 domain curve들이 속한 base stack $\mathfrak{M}_{g,n}$를 사용하여 이 둘이 이루는 distinguished triangle

$$q^\ast\LL_{\mathfrak{M}_{g,n}}\rightarrow (E')^\bullet\rightarrow E^\bullet\rightarrow q^\ast\LL_{\mathfrak{M}_{g,n}}[1]$$

을 만드는 것이다. 이 때 base의 smoothness는 $q^\ast\LL_{\mathfrak{M}_{g,n}}$에 음의 degree 항이 없게 하고, $M$이 Deligne–Mumford stack이라는 것은 curve의 무한소 automorphism이 담긴 degree $1$ 항을 죽이므로, 둘이 함께 $(E')^\bullet$의 amplitude를 $[-1,0]$으로 지켜주어 이를 perfect obstruction theory로 만들게 된다. 

이 triangle은 relative obstruction과 absolute obstruction의 관계도 알려준다. Triangle을 dualize하여 점 $z=[(C,p_\bullet,\mu)]$에서의 derived fiber의 cohomology를 취하면, $M$이 Deligne–Mumford stack이고 $\mathfrak{M}_{g,n}$이 smooth하므로 양 끝이 $0$인 exact sequence

$$\begin{aligned}0&\rightarrow h^{-1}(q^\ast\LL_{\mathfrak{M}_{g,n}}^\vee\vert_z)\rightarrow h^0((E^\bullet)^\vee\vert_z)\rightarrow h^0(((E')^\bullet)^\vee\vert_z)\\&\rightarrow h^0(q^\ast\LL_{\mathfrak{M}_{g,n}}^\vee\vert_z)\rightarrow h^1((E^\bullet)^\vee\vert_z)\rightarrow h^1(((E')^\bullet)^\vee\vert_z)\rightarrow0\end{aligned}$$

을 얻는다. 각 항은 차례로 marked curve의 무한소 automorphism, $H^0(C,\mu^\ast T_X)$, $T^1$, marked curve의 deformation, $H^1(C,\mu^\ast T_X)$, $T^2$이고, 이는 [§안정사상들의 모듈라이 공간, ⁋명제 4](/ko/math/gromov-witten_theory/moduli_of_stable_maps#prop4){: data-lid="ydjrs" }의 exact sequence이다. 특히 relative obstruction $H^1(C,\mu^\ast T_X)$는 absolute obstruction $T^2$로 surjective하게 가고, 그 kernel은 curve의 deformation, 가령 node를 펴는 방향의 image이다. 따라서 relative하게 unobstructed인 점은 absolute하게도 unobstructed이다. 반대로 $H^1(C,\mu^\ast T_X)\neq0$이더라도 그 전체가 curve의 deformation의 image이면 $T^2=0$이므로, relative하게는 obstructed이지만 absolute하게는 unobstructed인 점이 있을 수 있다.

::: 예시 13
$X$가 convex인 경우 모든 genus $0$ stable map에서 $H^1(C,\mu^\ast T_X)=0$이므로 ([§안정사상들의 모듈라이 공간, ⁋명제 5](/ko/math/gromov-witten_theory/moduli_of_stable_maps#prop5){: data-lid="c4h5h" }) obstruction space가 $h^1((E^\bullet)^\vee)=R^1\pi_\ast\mu^\ast T_X=0$이다. 이제 위에서 살펴본 것과 마찬가지 이유로, $\mathfrak{M}_{0,n}$의 smoothness에 의해 absolute obstruction 또한 $h^1(((E')^\bullet)^\vee)=0$이 되므로, [명제 11](#prop11){: data-lid="vrq63" }의 (3)에 의해

$$[\overline{\mathcal{M}}_{0,n}(X,\beta)]^\vir=[\overline{\mathcal{M}}_{0,n}(X,\beta)]$$

이 되어 virtual class가 보통의 fundamental class와 일치한다. $X=\mathbb{P}^r$와 Grassmannian, 일반적인 flag variety $G/P$가 모두 이 경우에 해당하며, 여기에서의 genus $0$ curve counting은 smooth moduli의 (진짜) fundamental class에 대한 적분과 동일하게 나오며, 이것이 이전 글의 계산을 정당화한다. 
:::

[§그로모프-위튼 불변량, ⁋정의 1](/ko/math/gromov-witten_theory/gromov-witten_invariants#def1){: data-lid="gt4df" }에서 우리는 fundamental class $[\overline{\mathcal{M}}_{0,n}(X,\beta)]$가 존재하는 경우에 대해서만 정의하였으나, 이 fundamental class만 virtual fundamental class로 바꿔주면 convex 가정 없이도 임의의 smooth projective target $X$에 대한 genus $0$ Gromov-Witten invariant를 정의할 수 있으며, convex 가정 하에서 이 두 정의가 같은 것은 위의 [예시 13](#ex13){: data-lid="bt6x3" }에 의해 자명하다. 그럼 이 정의 하에서, virtual class가 forgetful morphism 및 gluing morphism에 대해 잘 행동하는 것을 확인할 수 있으므로 [§그로모프-위튼 불변량, §§그로모프-위튼 불변량의 공리들](/ko/math/gromov-witten_theory/gromov-witten_invariants#그로모프-위튼-불변량의-공리들){: data-lid="huqbc" }의 string·divisor·splitting 공리와 WDVV 관계도 해당 적분들을 virtual class에 대한 적분으로 해석하면 그대로 성립한다.

## Zero locus의 가상 기본류

[§§벡터다발의 zero locus](#벡터다발의-zero-locus){: data-lid="1un49" }의 국소 모형에서 ambient는 smooth variety였다. 그러나 이 모형이 실제로 쓰이는 상황에서는 ambient 자신이 obstruction을 갖는 moduli인 경우가 많다. 가령 smooth projective variety $P$ 안의 smooth subvariety $Y$가 vector bundle $V$의 section $s$의 zero locus로 주어지면, $Y$로 가는 stable map은 $P$로 가는 stable map $f$ 가운데 $f^\ast s=0$인 것이다. 모든 genus $0$ stable map에 대해 $H^1(C,f^\ast V)=0$이면 $\pi_\ast\mu^\ast V$는 $P$의 genus $0$ moduli 위의 vector bundle이고, $Y$의 moduli는 그 section $f\mapsto f^\ast s$의 zero locus가 된다. 두 moduli는 모두 [명제 12](#prop12){: data-lid="3nmml" }의 virtual class를 가지므로, 자연스러운 질문은 [예시 1](#ex1){: data-lid="fn474" }에서처럼 둘이 Euler class로 이어지는지의 여부일 것이다. Stable map의 moduli는 $\mathfrak{M}_{g,n}$에 상대적인 perfect obstruction theory를 가지므로 처음부터 상대적인 형태로 적는다.

::: 명제 14 (Kim–Kresch–Pantev)
$\mathfrak{M}$을 locally finite type이고 pure dimensional인 smooth Artin stack, $q:M\rightarrow\mathfrak{M}$을 finite type Deligne–Mumford stack $M$에서의 morphism, $\phi:E^\bullet\rightarrow\LL_{M/\mathfrak{M}}$을 relative perfect obstruction theory라 하자. $M$ 위의 rank $r$ vector bundle $V$와 section $s$에 대하여 $i:Z=Z(s)\hookrightarrow M$을 그 zero locus라 하고, $Z$ 위의 relative perfect obstruction theory $\phi_Z:E_Z^\bullet\rightarrow\LL_{Z/\mathfrak{M}}$이 distinguished triangle

$$i^\ast E^\bullet\rightarrow E_Z^\bullet\rightarrow V^\vee\vert_Z[1]\rightarrow i^\ast E^\bullet[1]$$

에 들어가며, 이 triangle이 cotangent complex의 triangle $i^\ast\LL_{M/\mathfrak{M}}\rightarrow\LL_{Z/\mathfrak{M}}\rightarrow\LL_{Z/M}\rightarrow i^\ast\LL_{M/\mathfrak{M}}[1]$과 $\phi$, $\phi_Z$, 그리고 $s$가 주는 $V^\vee\vert_Z[1]\rightarrow\LL_{Z/M}$으로 compatible하다고 하자. 그럼

$$[Z]^\vir=0^!_{V,s}[M]^\vir,\qquad i_\ast[Z]^\vir=c_r(V)\cap[M]^\vir$$

이다. 여기서 $0^!_{V,s}$는 zero section의 refined Gysin map을 section $s$를 따라 적용한 것, 곧 [§§벡터다발의 zero locus](#벡터다발의-zero-locus){: data-lid="6g4xw" }에서 localized Euler class를 만든 연산이다.
:::

이는 [KKP, Theorem 1]을 zero section $0_V:M\rightarrow V$에 적용한 것이다. 이 정리는 relative perfect obstruction theory를 갖는 두 stack이 local complete intersection morphism $v$를 따라 cartesian하게 놓이고 두 obstruction theory가 cotangent complex의 triangle과 compatible하면, $v$의 refined Gysin map이 한쪽의 virtual class를 다른 쪽의 virtual class로 보낸다는 것이다. 지금의 경우 cartesian square는 $s$와 $0_V$의 fiber product $Z=M\times_VM$이고, $0_V$의 cotangent complex를 $Z$로 당긴 것이 $V^\vee\vert_Z[1]$이므로 위의 triangle이 정확히 그 compatibility 조건이 된다. [BF, Proposition 7.5]는 global resolution을 가정하고 $v$가 smooth하거나 $v$의 source와 target이 모두 base 위에서 smooth한 경우에 같은 등식을 주는데, zero section에 대해 뒤의 조건은 $M$이 $\mathfrak{M}$ 위에서 smooth하다는 것이다. [KKP, Theorem 1]은 이러한 가정 없이 base의 pure dimensionality와 $v$가 local complete intersection morphism이라는 것만을 요구하며, [KKP]는 이를 [BF, Proposition 7.5]를 강화한 것으로 소개한다. Base의 smoothness는 $\mathfrak{M}$ 상대 perfect obstruction theory로 정의한 virtual class가 [명제 12](#prop12){: data-lid="qmcty" }에서처럼 유도한 absolute perfect obstruction theory의 virtual class와 같다는 데에 쓰인다. ([KKP, Proposition 3]) 둘째 등식은 refined Gysin map에 대한 공식 $i_\ast0^!_{V,s}\gamma=c_r(V)\cap\gamma$를 $\gamma=[M]^\vir$에 적용한 것이다.

명제는 $E_Z^\bullet$을 가정으로 둔다. 일반적인 $(M,E^\bullet)$에서 이러한 $E_Z^\bullet$을 만들려면 $s$가 주는 $V^\vee\vert_Z[1]\rightarrow\LL_{Z/M}$과 cotangent complex의 triangle의 connecting map을 합성한 $V^\vee\vert_Z\rightarrow i^\ast\LL_{M/\mathfrak{M}}$을 $\phi$를 따라 $i^\ast E^\bullet$으로 들어 올려야 하는데, 그 obstruction은 $\phi$의 cone의 hypercohomology에 있어서 local하게만 사라지고 global하게는 자동이 아니다. 그래서 $E_Z^\bullet$은 경우마다 구성하며, 아래 [예시 15](#ex15){: data-lid="zy2k0" }에서는 universal curve 위의 vector bundle의 short exact sequence에 $R\pi_\ast$를 취해 이를 얻는다. 가장 간단한 경우는 $q$가 smooth한 경우이다. 이때는 $E^\bullet=\Omega_{M/\mathfrak{M}}$으로 둘 수 있고,

$$E_Z^\bullet=\Bigl[\at{-1}{V^\vee\vert_Z}\xrightarrow{\ (\dd{s})^\vee\ }\at{0}{\Omega_{M/\mathfrak{M}}\vert_Z}\Bigr]$$

이 $Z$의 relative perfect obstruction theory이다. $\tau_{\geq-1}\LL_{Z/\mathfrak{M}}=[\mathcal{I}/\mathcal{I}^2\rightarrow\Omega_{M/\mathfrak{M}}\vert_Z]$이고 $V^\vee\vert_Z\rightarrow\mathcal{I}/\mathcal{I}^2$이 surjective이므로, $h^0$에서는 isomorphism이고 $h^{-1}$에서는 surjective이다. 위의 triangle은 이 two-term complex의 stupid truncation이 주는 것이다. 이는 [§§벡터다발의 zero locus](#벡터다발의-zero-locus){: data-lid="xf6gi" }의 구성을 $\mathfrak{M}$ 위에서 상대적으로 한 것이다.

[명제 14](#prop14){: data-lid="nny9k" }의 triangle은 각 점에서 $Z$와 $M$의 tangent space와 obstruction space를 이어 준다. 점 $z\in Z$에서의 derived fiber를 $(\cdot)\vert_z$로 적으면, 위 triangle의 dual $V\vert_Z[-1]\rightarrow(E_Z^\bullet)^\vee\rightarrow i^\ast(E^\bullet)^\vee\rightarrow V\vert_Z$의 derived fiber의 cohomology에서 long exact sequence

$$0\rightarrow h^0((E_Z^\bullet)^\vee\vert_z)\rightarrow h^0((E^\bullet)^\vee\vert_z)\xrightarrow{\dd{s}}V_z\rightarrow h^1((E_Z^\bullet)^\vee\vert_z)\rightarrow h^1((E^\bullet)^\vee\vert_z)\rightarrow0$$

을 얻는다. $(E_Z^\bullet)^\vee\vert_z$와 $(E^\bullet)^\vee\vert_z$의 $h^0$과 $h^1$은 각각 $z$에서 $Z$와 $M$의 relative tangent space와 obstruction space이고, 가운데 map은 relative tangent 방향에 대한 $s$의 미분이다. [§§벡터다발의 zero locus](#벡터다발의-zero-locus){: data-lid="6eerh" }에서 $\ker(\dd{s})$와 $\coker(\dd{s})$로 적은 것에 ambient의 obstruction $h^1((E^\bullet)^\vee\vert_z)$이 더해진 꼴이다. 따라서 $M$이 $z$에서 $\mathfrak{M}$ 상대로 unobstructed이고 $\dd{s}$가 $z$에서 surjective이면 $Z$도 $z$에서 $\mathfrak{M}$ 상대로 unobstructed이다. 이때 $h^1((E_Z^\bullet)^\vee)$은 amplitude $[0,1]$인 perfect complex의 top cohomology이므로 Nakayama lemma에 의해 $z$의 근방에서 $0$이고, 그 근방에서 $Z\rightarrow\mathfrak{M}$은 smooth하다. ([BF, Proposition 7.3]) 같은 논증으로 $M$도 $z$ 근방에서 $\mathfrak{M}$ 위에서 smooth하고, $\dd{s}$가 surjective이므로 $Z$는 그 근방에서 $M$의 codimension $r$ smooth substack이다. 반대로 $\dd{s}$가 surjective가 아니면 그 cokernel이 그대로 $Z$의 obstruction으로 남는다.

같은 논증을 뒤집으면, $Z$가 smooth하지 않은 점에서는 obstruction이 $0$일 수 없다. 만일 점 $z$에서 relative obstruction이 $0$이라면 위와 같이 그 근방에서 $Z\rightarrow\mathfrak{M}$이 smooth하고, $\mathfrak{M}$이 smooth하므로 $Z$도 smooth해야 하기 때문이다. Absolute perfect obstruction theory에 대해서도 같다. 이는 perfect obstruction theory의 선택과도 무관하다. 어떤 absolute perfect obstruction theory의 obstruction space도 intrinsic obstruction space $\Ext^1(\LL_Z\vert_z,\mathbb{C})$를 포함하고 ([KKP, §3]), 이 공간은 $Z$가 $z$에서 smooth하지 않으면 $0$이 아니기 때문이다. 특히 $Z$가 어떤 irreducible component $D$의 generic point에서 non-reduced이면, smooth locus는 open이고 smooth한 곳은 reduced이므로 $Z$는 $D$의 어느 점에서도 smooth하지 않고, 따라서 $D$의 모든 점에서 relative하게도 absolute하게도 obstructed이다. 이때 obstructed인 것은 scheme으로서의 $Z$이고, reduced structure를 준 $D$ 자체는 generic point에서 smooth하다.

::: 예시 15
$Y\subset\mathbb{P}^4$를 smooth quintic threefold, 곧 $\mathcal{O}(5)$의 section $s$의 zero locus라 하고 $Y$ 위의 직선을 세자. $\mathcal{O}(5)$는 globally generated이므로 genus $0$ stable map $f:C\rightarrow\mathbb{P}^4$로 당긴 line bundle은 모든 component에서 음이 아닌 degree를 갖고, 따라서 $H^1(C,f^\ast\mathcal{O}(5))=0$이다. 그럼 cohomology와 base change에 의해 $\mathcal{V}_d=\pi_\ast\mu^\ast\mathcal{O}(5)$는 $\overline{\mathcal{M}}_{0,0}(\mathbb{P}^4,d)$ 위의 rank $5d+1$ vector bundle이고, $s$는 그 section $\widetilde{s}([f])=f^\ast s$를 준다. Stable map이 $Y$로 들어간다는 것은 $f^\ast s=0$이라는 것이므로 $Z(\widetilde{s})$는 $Y$로 가는 stable map들의 moduli이고, Lefschetz hyperplane theorem에 의해 $H_2(Y)\rightarrow H_2(\mathbb{P}^4)$가 isomorphism이므로 이는 $\overline{\mathcal{M}}_{0,0}(Y,d)$ 하나이다.

[명제 14](#prop14){: data-lid="5llwo" }의 compatibility는 normal bundle sequence $0\rightarrow T_Y\rightarrow T_{\mathbb{P}^4}\vert_Y\rightarrow\mathcal{O}(5)\vert_Y\rightarrow0$에서 온다. 이를 universal map으로 당기고 $R\pi_\ast$를 취한 뒤 dual을 취하면 $\overline{\mathcal{M}}_{0,0}(Y,d)$ 위의 triangle

$$i^\ast(R\pi_\ast\mu^\ast T_{\mathbb{P}^4})^\vee\rightarrow(R\pi_\ast\mu^\ast T_Y)^\vee\rightarrow i^\ast\mathcal{V}_d^\vee[1]\rightarrow i^\ast(R\pi_\ast\mu^\ast T_{\mathbb{P}^4})^\vee[1]$$

을 얻고, 처음 두 항은 [명제 12](#prop12){: data-lid="65y3n" }의 relative perfect obstruction theory들이다. [KKP]는 이 triangle이 cotangent complex의 triangle과 compatible하다고 적고 여기에 [명제 14](#prop14){: data-lid="ycr9q" }을 적용한다. $\mathbb{P}^4$는 convex이므로 [예시 13](#ex13){: data-lid="4mh66" }에 의해 ambient의 virtual class는 fundamental class이고, 따라서

$$i_\ast[\overline{\mathcal{M}}_{0,0}(Y,d)]^\vir=c_{5d+1}(\mathcal{V}_d)\cap[\overline{\mathcal{M}}_{0,0}(\mathbb{P}^4,d)]$$

이다. 차원은 $\dim\overline{\mathcal{M}}_{0,0}(\mathbb{P}^4,d)-(5d+1)=(5d+1)-(5d+1)=0$으로 맞고, 이는 $c_1(T_Y)=0$이어서 $\vdim\overline{\mathcal{M}}_{0,0}(Y,d)=0$인 것과 같다.

$d=1$이면 이 적분을 직접 계산할 수 있다. Degree $1$의 stable map은 직선으로의 isomorphism이므로 $\overline{\mathcal{M}}_{0,0}(\mathbb{P}^4,1)$은 $\mathbb{P}^4$ 안의 직선들의 Grassmannian $\Gr(2,5)$이고, 직선 $L=\mathbb{P}(W)$에서 $\mathcal{V}_1$의 fiber는 $H^0(L,\mathcal{O}(5))=\Sym^5W^\vee$이다. 즉 tautological subbundle을 $S$라 하면 $\mathcal{V}_1=\Sym^5S^\vee$이다. $S^\vee$의 Chern root를 $a,b$라 하면 $\Sym^5S^\vee$의 Chern root는 $ia+(5-i)b$ ($0\leq i\leq5$)이므로, $\sigma_1=a+b$, $\sigma_{11}=ab$로 적으면

$$\begin{aligned}c_6(\Sym^5S^\vee)&=\prod_{i=0}^5\bigl(ia+(5-i)b\bigr)=25\sigma_{11}(4\sigma_1^2+9\sigma_{11})(6\sigma_1^2+\sigma_{11})\\&=25\bigl(24\sigma_1^4\sigma_{11}+58\sigma_1^2\sigma_{11}^2+9\sigma_{11}^3\bigr)\end{aligned}$$

이다. Pieri 공식으로부터 $\int\sigma_1^4\sigma_{11}=2$, $\int\sigma_1^2\sigma_{11}^2=1$, $\int\sigma_{11}^3=1$이므로

$$\int_{[\overline{\mathcal{M}}_{0,0}(Y,1)]^\vir}1=25(48+58+9)=2875$$

이다. 일반적인 quintic threefold 위의 직선은 정확히 $2875$개이지만, 위의 계산은 그러한 일반성 가정 없이 virtual class의 degree로서 성립한다. $d\geq2$에서는 $Y$ 위의 직선 하나의 $d$-fold cover들만으로도 $\dim\overline{\mathcal{M}}_{0,0}(\mathbb{P}^1,d)=2d-2>0$차원의 family를 이루므로, 어떤 smooth quintic에서도 $\overline{\mathcal{M}}_{0,0}(Y,d)$는 기대 차원보다 크고 그 virtual class는 fundamental class로 주어지지 않는다. 이때 위의 등식이 virtual class의 degree를 계산하는 수단이 된다.
:::

---

**참고문헌**

**[BF]** K. Behrend, B. Fantechi, *The intrinsic normal cone*, Invent. Math. **128** (1997)  
**[B]** K. Behrend, *Gromov–Witten invariants in algebraic geometry*, Invent. Math. **127** (1997)  
**[KKP]** B. Kim, A. Kresch, T. Pantev, *Functoriality in intersection theory and a conjecture of Cox, Katz, and Lee*, J. Pure Appl. Algebra **179** (2003) <!-- TODO: 서지 확인 -->

<!-- TODO: 서지 확인. [BF]의 번호(Proposition 2.5, 2.6, Theorem 4.5, Lemma 4.6, Proposition 4.7, 5.3, 5.6, 7.3, 7.5)는 arXiv v1(로컬 PDF)에서 내용까지 확인했다. 출판본과의 번호 대조는 아직 하지 않았다. -->
