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

를 정의할 수 있다. 직관적으로 이는 non-transversal section $s$를 올바르게 흔들어줬으면 나왔을 class를 실제로 흔들지 않고도 대수적으로 적어 둔 것으로 이해할 수 있다. 또 Euler class $e(E)$는 $E$의 top Chern class $c_r(E)$이므로, localized Euler class를 $X$로 보낸 class는 $Z(s)$의 모양이나 section $s$와 무관하게 $c_r(E)\cap[X]$로 계산된다.

::: 예시 1
$X=\mathbb{P}^2$, $E=\mathcal{O}(1)^{\oplus2}$를 보자. 그럼 section $s=(\ell_1,\ell_2)$가 두 일차식으로 주어지므로, 위의 그림에서 $Z(s)$는 기대 차원이 $0$이 된다. 실제로 이는 두 직선의 교점인 한 점이고, 그 class의 degree는

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

으로 정의되었으며, 이는 직관적으로 $X$를 $Z$의 normal 방향으로 무한히 확대했을 때 $Z$ 위에 남는 모양으로 생각할 수 있다. 이 때 위 명제의 내용은 $t\neq0$에서의 fiber가 $X$이고 $t=0$에서의 fiber가 $C_{Z/X}$인 $\mathbb{A}^1$ 위의 family가 존재한다는 것, 곧 $X$를 $Z$를 따라 $C_{Z/X}$로 degenerate시킬 수 있다는 것으로, 이 degeneration 때문에 $C_{Z/X}$는 $Z$의 모양과 무관하게 pure dimension $\dim X$를 갖는다. 만일 $Z\hookrightarrow X$가 regular embedding이라면 $C_{Z/X}$는 normal bundle과 같지만, 일반적으로는 그 fiber가 vector space가 아닌 cone으로 주어진다.

이제 $E$를 국소적으로 trivialize하여 $s=(s_1,\ldots,s_r)$로 적자. 그럼 $\mathcal{I}=(s_1,\ldots,s_r)$이므로, $s$와의 pairing $s^\vee:E^\vee\rightarrow\mathcal{O}_X$의 image가 정확히 $\mathcal{I}$이고, 이를 $Z$로 제한하면 surjection $E^\vee\vert_Z\twoheadrightarrow\mathcal{I}/\mathcal{I}^2$을 얻으므로 $C_{Z/X}$는 $E\vert_Z$의 closed subcone이 된다.

이제 zero section $0_E:Z\hookrightarrow E\vert_Z$에 대한 Gysin map을 이 cone에 취하여

$$e(E,s)=0_E^![C_{Z/X}]\in A_{\dim X-r}(Z)$$

로 localized Euler class를 정의한다. 위에서 $C_{Z/X}$는 $X$를 $Z$의 normal 방향으로 무한히 확대한 모양이었고, 이를 $s$를 통해 $E\vert_Z$ 안에 넣으면 그 $x\in Z$ 위의 fiber는 $x$에서 $Z$ 밖으로 조금 나갔을 때 $s$가 갖게 되는 값들의 방향을 $E_x$ 안에 모은 것이 된다. 그럼 $0_E^![C_{Z/X}]$의 역할은 $E\vert_Z$의 zero section과 이 cone을 교차시키는 것으로서, 직관적으로는 zero section을 일반적인 section으로 흔들어준 뒤 cone과의 교집합을 보는 것이다. 만일 $s$가 점 $x$에서 transversal하다면, cone의 fiber가 $E_x$ 전체가 되며 따라서 이러한 경우 $Z$가 그대로 나오게 된다. 문제는 $s$가 transversal하지 않은 점으로, 이러한 경우 cone의 fiber가 $E_x$를 전부 채우지 못하며, 일반적인 section의 값이 이렇게 남는 부분에 놓이는 점들은 교집합에서 빠져 $Z$가 깎이게 된다. 이때 cone은 각 점에서 $\dd{s}_x$의 image 방향은 항상 다 채우므로, 채우지 못하고 남을 수 있는 것은 obstruction space $\coker(\dd{s}_x)$ 방향뿐이며, 그 안에서 cone의 모양을 정하는 것이 Kuranishi map $\kappa$이다. 위의 차원 계산은 이러한 방식으로 깎여나가는 정도가 정확히 $Z$가 기대보다 부푼 정도가 되어, 이들이 서로를 상쇄한다는 것이며 따라서 $e(E,s)$는 기대 차원의 class가 되는 것이다. 

가령 [예시 1](#ex1){: data-lid="qn2a2" }의 상황에서 $s=(\ell_1,0)$인 경우를 보자. 그럼 이것이 정의하는 locus는 직선 $Z(s)=\{\ell_1=0\}$이다. $Z(s)$ 바깥에서는 $\ell_1=0$ 조건이 사라지므로 $s$의 첫째 성분은 값을 가지게 될 수 있지만, 둘째 성분은 항등적으로 $0$이므로 여전히 $0$이다. 이 상황에서 cone은 $E\vert_{Z(s)}=\mathcal{O}_{Z(s)}(1)^{\oplus2}$의 첫째 성분이므로, zero section과의 교차는 첫째 성분 방향으로는 아무것도 깎지 않고 둘째 성분 $\mathcal{O}_{Z(s)}(1)$ 방향에서만 $Z(s)$를 깎는다. 즉 이 교차는 둘째 성분의 zero section으로 $Z(s)$를 자른 것과 같고, 따라서 $e(E,s)=c_1(\mathcal{O}_{Z(s)}(1))\cap[Z(s)]$이다. $Z(s)\cong\mathbb{P}^1$이므로 이는 degree $1$의 point class이다.

일반적으로 cone이 $E\vert_Z$의 subbundle $N_{Z/X}$인 경우, $e(E,s)$는 *excess bundle* $E\vert_Z/N_{Z/X}$의 top Chern class를 $[Z]$에 cap한 것으로 주어진다. $Z$가 local complete intersection인 곳에서는 $\mathcal{I}/\mathcal{I}^2$이 locally free이므로 cone이 normal bundle $N_{Z/X}$이고 항상 이 경우에 해당하며, [예시 1](#ex1){: data-lid="tis96" }의 $s\equiv0$과 transversal한 $s$가 그 양 극단이다. 전자에서는 cone이 zero section이어서 quotient가 $E$ 전체이므로 $e(E,s)=e(E)\cap[\mathbb{P}^2]$이고, 후자에서는 cone이 $E\vert_Z$ 전체여서 quotient가 $0$이므로 $e(E,s)=[Z]$이다. 

이 공식은 성분들이 만나거나 local complete intersection이 아닌 점에서는 보정이 필요하다. 이때 cone의 성분 하나를 $Z$로 내린 image의 closure, 즉 그 성분의 support를 $W$라 하면, 그 성분의 차원 $\dim X$는 $\dim W$와 fiber의 차원 $r$의 합을 넘을 수 없으므로 $\dim W\geq\dim X-r$이어야 한다. 즉 cone의 각 성분의 support는 기대 차원 이상의 subvariety이며, $Z$의 성분이 아니어도 된다. 또 $Z$가 local complete intersection이 아닌 점에서는 normal bundle의 closure가 subbundle이 되지 못할 수 있다. 다음은 normal cone이 zero section도 bundle 전체도 아니며 subbundle조차 아닌 예로, 이 경우에도 cone을 성분별로 나누어 각 성분을 zero section으로 자르면 $e(E,s)$를 계산할 수 있음을 보여 준다.

::: 예시 2
$X=\mathbb{P}^3$ 위의 $E=\mathcal{O}(2)^{\oplus2}$와 section $s=(\x_0\x_1,\x_0\x_2)$를 생각하자. 그럼 그 zero locus $Z=Z(s)$는 평면 $P=\{\x_0=0\}$과 직선 $L=\{\x_1=\x_2=0\}$의 합집합이고 둘은 한 점 $p=[0:0:0:1]$에서 만난다. 기대 차원은 $3-2=1$이고, localized Euler class $e(E,s)$를 $X$로 보낸 class는

$$c_2(E)\cap[\mathbb{P}^3]=4H^2\cap[\mathbb{P}^3]$$

이므로 degree $4$의 curve class이다. 

이제 localized Euler class $e(E,s)$가 어떻게 주어지는지 살펴보자. 이는 $A_1(Z)=A_1(P\cup L)$의 원소이며, 이 Chow group은 다음의 exact sequence

$$A_1(P\cap L)\rightarrow A_1(P)\oplus A_1(L)\rightarrow A_1(Z)\rightarrow0$$

에 의하여 $A_1(Z)\cong A_1(P)\oplus A_1(L)\cong\mathbb{Z}^2$임을 계산할 수 있다. 즉 $e(E,s)\in A_1(Z)$는 두 성분에서의 degree의 쌍 $(a,b)$로 결정되며 $a+b=4$이다.

이제 이 class를 직접 구하자. Normal cone $C=C_{Z/X}$은 $E\vert_Z$ 안의 pure dimension $3$의 closed subcone이다. 또, 위에서 살펴본 것과 같이 cone의 각 성분의 support는 expected dimension $1$ 이상이므로, support가 $\{p\}$인 부분은 없으며 따라서 $C$의 각 성분은 $Z\setminus\{p\}$ 위에서 계산한 후 closure를 취하면 얻어진다. 

우선 $L\setminus\{p\}$를 보면, 이 위에서 $\x_0$은 unit이므로 이를 정의하는 ideal은 $(\x_1,\x_2)$가 되며, 이는 codimension 2 complete intersection이므로 normal cone이 곧 normal bundle이 되며 그 rank는 $2$이다. 그런데 $E$의 rank 또한 $2$이므로, $E\vert_L$ 전체가 normal cone이 되어야 한다. 

비슷하게 $P\setminus\{p\}$ 근방에서는 $\x_1,\x_2$ 중 하나가 unit이므로 ideal이 $(\x_0)$이 되며, 이는 방정식 하나로 잘린 Cartier divisor이다. 일반적으로 Cartier divisor $D$의 normal cone은 항상 $N_{D/X}=\mathcal{O}_X(D)\vert_D$로 주어지므로 우리 상황에서 이는 line bundle $N_{P/X}=\mathcal{O}_P(1)$이다. 

이 line bundle이 $E\vert_P$ 안에 어떻게 놓이는지는 $s$를 $P$의 방정식 $\x_0$으로 나누어 보면 알 수 있다. $s=\x_0\cdot(\x_1,\x_2)$이므로 $P$ 바깥에서 $s$의 값은 $(\x_1,\x_2)$ 방향을 향하고, 따라서 $P\setminus\{p\}$의 각 점 $x$에서 cone의 fiber는 $E_x$ 안에서 $(\x_1(x),\x_2(x))$가 생성하는 직선이다. 이를 식으로 적으면, 

$$E^\vee\vert_P=\mathcal{O}_P(-2)^{\oplus2}\rightarrow\mathcal{I}_P/\mathcal{I}_P^2=\mathcal{O}_P(-1)$$

은 $E^\vee$의 두 basis를 $\x_0\x_1=\x_1\cdot\x_0$과 $\x_0\x_2=\x_2\cdot\x_0$으로 보내므로 $(\x_1,\x_2)$를 곱하는 map이고, 그 dual

$$N_{P/X}=\mathcal{O}_P(1)\xrightarrow{(\x_1,\x_2)}\mathcal{O}_P(2)^{\oplus2}=E\vert_P$$

가 cone을 $E\vert_P$ 안에 넣는 embedding이다.

이제 이렇게 구한 각 성분에 closure를 취하자. 이 과정에서 새로 얻어지는 점은 $p$ 위에만 있으므로 이 근처에서만 계산하면 충분하다. 따라서 $\x_3\neq0$인 affine chart에서 $\mathcal{O}(1)$과 $\mathcal{O}(2)$를 각각 $\x_3$과 $\x_3^2$으로 trivialize하여, $p$를 원점으로, $E$의 total space를 $\mathbb{C}^3\times\mathbb{C}^2$로 보자. 이 chart에서 $L$의 점은 $(x,0,0)$이고 $P$의 점은 $(0,y,z)$ 꼴이다. 우선 $L\setminus \{p\}$ 위의 cone은 $E\vert_L$ 전체로 주어졌으므로 이 부분은

$$C_L^\circ=\{(x,0,0)\mid x\neq0\}\times\mathbb{C}^2$$

로 표기할 수 있으며, $P$의 line bundle은 $(\x_1,\x_2)$로 주어지므로 

$$C_P^\circ=\{((0,y,z),\lambda(y,z))\mid(y,z)\neq(0,0),\lambda\in\mathbb{C}\}$$

가 된다. 이제 $C_L^\circ$은 closure를 취하면 정확히 $x=0$인 점을 더하여 $C_L=E\vert_L$로 나오며, $C_P$의 경우 위 집합을

$$C_P^\circ=\{((0,y,z),v)\mid zv_1-yv_2=0,(y,z)\neq (0,0)\}$$

으로 써 주면 그 closure가 

$$C_P=\{((0,y,z),v)\mid zv_1-yv_2=0\}$$

로 주어지는 것을 안다. 즉 $C_P$는 $p$ 위에서는 fiber $E_p$ 전체를 가진다. 전체 cone $C$의 class는 이렇게 구한 두 성분들의 합 $[C]=[C_P]+[C_L]$으로 나타난다. 따라서 이들 각각의 Gysin pullback을 계산하여 localized Euler class를 계산할 수 있다.

$C_L$은 vector bundle $E\vert_L$ 자신이므로 zero section으로 자르면 $0^![C_L]=[L]$이다. 계산이 필요한 것은 $C_P$ 쪽이다. 우선 $C_P$를 정의하는 조건 $zv_1-yv_2=0$을 homogeneous coordinate로 적으면, $C_P$는 map

$$\varphi:E\vert_P=\mathcal{O}_P(2)^{\oplus2}\rightarrow\mathcal{O}_P(3);\qquad(v_1,v_2)\mapsto\x_2v_1-\x_1v_2$$

의 kernel로 생각할 수 있으며, 이 때 $x\neq p$에서는 $(\x_2(x),-\x_1(x))\neq0$이므로 $\varphi_x$의 kernel은 $(\x_1(x),\x_2(x))$가 생성하는 직선이고, $x=p$에서는 $\varphi_p=0$이므로 kernel은 $E_p$ 전체이다. 이 데이터는 $E\vert_P$의 total space와 그 projection $\pi:E\vert_P\rightarrow P$를 사용하면, $\varphi$는 $E\vert_P$ 위의 line bundle $\pi^\ast \mathcal{O}_P(3)$의 section으로 생각할 수 있으며 이 section의 zero locus가 바로 $C_P$가 된다. 따라서 이는 total space 안의 Cartier divisor이며, 그 class는 line bundle의 $c_1$과 cap하여 다음의 식 

$$[C_P]=c_1(\pi^\ast\mathcal{O}_P(3))\cap[E\vert_P]=\pi^\ast(3H\cap[P])$$

과 같이 계산할 수 있다. 여기서 $c_1$은 flat pullback과 commute한다는 사실을 사용하였다. 이 때, zero section의 Gysin map은 flat pullback $\pi^\ast$의 역이므로 $0^![C_P]=3H\cap[P]$을 얻고, 따라서 $P$ 안의 직선을 $\ell$이라 하면

$$e(E,s)=3[\ell]+[L]\in A_1(Z)$$

임을 안다. 
:::

$c_2(E)\cap[\mathbb{P}^3]$은 총 degree가 $4$라는 것만을 알려주지만, localized Euler class는 이 $4$가 $Z$의 두 성분에 $3$과 $1$로 나뉘어 있다는 것까지 알려준다. 이 중 $1$은 기대 차원의 성분 $L$이 자기 자신 $[L]$로 기여한 것이고, $3$은 기대보다 한 차원 큰 평면 $P$에서 온 것이다. 이 $3$은 $P\setminus\{p\}$ 위의 excess bundle $E\vert_P/N_{P/X}\cong\mathcal{O}_P(3)$의 $c_1$, 곧 $4H-H$이다.

## Intrinsic normal cone

[예시 2](#ex2){: data-lid="3o76h" }의 계산에 쓰인 것은 $E\vert_Z$ 안의 normal cone $C_{Z/X}$ 하나였다. 그러나 일반적인 moduli $M$은 오직 étale-local하게만 smooth variety 안의 zero locus이며, 이 각각의 국소적인 표현들은 서로 다른 ambient space를 가지므로 normal cone이 잘 정의되지 않는다. 핵심적인 관찰은 normal cone 자체는 잘 정의되지 않더라도 class $0^![C_{Z/X}]$ 자체는 잘 정의된다는 것으로, 가령 $Z$를 $X\times\mathbb{A}^1$ 안의 $Z\times\{0\}$, 곧 $\pr_1^\ast E\oplus\mathcal{O}$의 section $(s,t)$의 zero locus로 보면 normal cone은 $C_{Z/X}\times\mathbb{A}^1$로 한 차원 커지지만 zero section으로 자른 class는 그대로이다. 이는 ambient space가 늘어난 tangent space 방향 $T_{\mathbb{A}^1}$이 cone과 bundle 양쪽에 똑같이 더해져 Gysin map을 계산할 때 그대로 상쇄되기 때문이다. 이로부터 우리는 cone을 ambient space의 tangent 방향으로 나눈 것이 본질적으로 유의미한 데이터일 것임을 추측할 수 있다. 

::: 명제 3
Scheme $Z$와 두 closed immersion $i:Z\hookrightarrow X$, $i':Z\hookrightarrow X'$, 그리고 smooth morphism $f:X'\rightarrow X$가 $f\circ i'=i$를 만족한다 하자. 그럼 normal cone들의 sequence

$$0\rightarrow (i')^\ast T_{X'/X}\rightarrow C_{Z/X'}\rightarrow C_{Z/X}\rightarrow0$$

은 exact이다. 즉 étale-local하게 $C_{Z/X'}\cong (i')^\ast T_{X'/X}\times C_{Z/X}$이고, $C_{Z/X'}\rightarrow C_{Z/X}$는 이 곱의 projection이다.
:::
::: 증명
주장은 étale-local하고, smooth morphism은 국소적으로 étale morphism $X'\rightarrow X\times\mathbb{A}^n$과 projection의 합성이며, normal cone은 ambient를 étale morphism으로 바꾸거나 $X\times\mathbb{A}^n$의 $X$ 위의 automorphism으로 옮겨도 변하지 않는다. 따라서 $X=\Spec A$가 affine이고 $X'=X\times\mathbb{A}^n$, $i'=i\times\{0\}$인 경우, 곧 $Z\times\{0\}\subset X\times\mathbb{A}^n$의 normal cone만 계산하면 된다. $Z$의 ideal을 $I\subseteq A$라 하면 $Z\times\{0\}$의 ideal은 $I'=I\cdot A[t_1,\ldots,t_n]+(t_1,\ldots,t_n)$이고, $A[t_1,\ldots,t_n]$을 monomial $t^\beta$들로 분해하면 $I'^k$의 $t^\beta$ 성분은 $I^{\max(k-\lvert\beta\rvert,0)}t^\beta$이다. 따라서

$$\bigoplus_{k\geq0}I'^k/I'^{k+1}\cong\Bigl(\bigoplus_{k\geq0}I^k/I^{k+1}\Bigr)[T_1,\ldots,T_n]$$

이고, 여기서 $T_j$는 $t_j$의 class이다. 곧 $C_{Z/X'}=C_{Z/X}\times\mathbb{A}^n$이며, 이 $\mathbb{A}^n$은 $Z$로 제한한 relative tangent bundle $(i')^\ast T_{X'/X}$이다.
:::

이 명제는 앞서 본 $X\times\mathbb{A}^1$의 현상이 일반적으로 일어난다는 것이다. 즉 ambient space $X$와 그 위에 smooth하게 얹힌 공간 $f:X'\rightarrow X$, 가령 projection $f:X\times\mathbb{A}^n\rightarrow X$가 있을 때, $Z$를 $X$의 부분공간으로 보았을 때의 normal cone $C_{Z/X}$와 $X'$의 부분공간으로 보았을 때의 normal cone $C_{Z/X'}$을 비교하면, $C_{Z/X'}$이 $C_{Z/X}$보다 커지는 정도는 정확히 relative tangent bundle $(i')^\ast T_{X'/X}$가 담고 있다는 것이다.

이제 위에서 설명한 것과 같이 cone을 tangent 방향으로 나누기 위해서는 tangent bundle이 cone 위에 작용해야 한다. Smooth scheme $W$의 closed subscheme $U$에 대하여 $\mathcal{I}/\mathcal{I}^2\rightarrow\Omega_W\vert_U$의 dual은 morphism $T_W\vert_U\rightarrow N_{U/W}$를 주며, 여기서 $N_{U/W}=\Spec_U\Sym(\mathcal{I}/\mathcal{I}^2)$은 normal cone $C_{U/W}$를 담는 normal sheaf이다. $N_{U/W}$는 fiber별로 덧셈을 갖는 abelian cone이므로, $T_W\vert_U$는 이 morphism을 통해 $N_{U/W}$ 위에 평행이동으로 작용한다.

::: 명제 4
Smooth scheme $W$의 closed subscheme $U$에 대하여, normal cone $C_{U/W}\subset N_{U/W}$는 $T_W\vert_U$의 평행이동에 대해 불변이다.
:::
::: 증명
$U$를 대각선을 거쳐 $W\times W$ 안에 넣고 두 projection $p_1,p_2:W\times W\rightarrow W$를 생각하자. 둘 다 smooth이므로 [명제 3](#prop3){: data-lid="tnoek" }을 각각에 적용할 수 있으며, normal sheaf에 대해서도 같은 exact sequence가 성립한다. 먼저 $p_1$에 대한 [명제 3](#prop3){: data-lid="h13fg" }으로 $N_{U/W\times W}\cong T_W\vert_U\times N_{U/W}$, $C_{U/W\times W}\cong T_W\vert_U\times C_{U/W}$로 동일시하자. 대각선 $W\rightarrow W\times W$가 주는 $N_{U/W}\rightarrow N_{U/W\times W}$는 $p_1$과 $p_2$가 유도하는 두 map 모두의 section이고, 이로부터 위의 동일시 아래에서 $p_2$가 유도하는 $N_{U/W\times W}\rightarrow N_{U/W}$가 $(v,n)\mapsto v+n$, 곧 $T_W\vert_U$의 작용임을 확인할 수 있다. 한편 $p_2$에 대한 [명제 3](#prop3){: data-lid="2bynq" }에서 $C_{U/W\times W}$의 image는 $C_{U/W}$이므로, $T_W\vert_U\times C_{U/W}$의 작용 아래 image는 $C_{U/W}$ 안에 있다.
:::

이제 우리는 intrinsic normal cone을 정의한다. 우선 Deligne–Mumford stack $M$의 *local embedding*이란 $M$의 étale chart, 곧 affine scheme $U$에서의 étale morphism $U\rightarrow M$과, 그 chart $U$를 smooth affine scheme $W$ 안에 넣는 closed embedding $U\hookrightarrow W$의 쌍을 말한다. $M$은 이러한 chart들로 덮이고 각 chart는 affine space 안에 넣을 수 있으므로, local embedding은 항상 존재한다. 

우리가 하려는 것은 각 chart에서 아무 local embedding $U\hookrightarrow W$를 잡아 그 normal cone $C_{U/W}$를 생각한 뒤, 이를 ambient의 tangent 방향으로 나눈 quotient stack $[C_{U/W}/T_W\vert_U]$를 취하는 것이다. 같은 chart $U$의 두 local embedding $U\hookrightarrow W$, $U\hookrightarrow W'$이 주어지면 $U\hookrightarrow W\times W'$이 둘을 함께 지배하고 두 projection이 smooth이므로, [명제 3](#prop3){: data-lid="s6lja" }과 [명제 4](#prop4){: data-lid="zle0a" }에 의하여 $T_{W\times W'/W}$ 방향을 먼저 나누어

$$[C_{U/W\times W'}/T_{W\times W'}\vert_U]\cong[C_{U/W}/T_W\vert_U]$$

를 얻고, $W'$에 대해서도 같으므로 잘 정의되며, 이는 normal sheaf에 대해서도 마찬가지이다. 따라서 이 quotient stack은 local embedding의 선택에 의존하지 않고 잘 정의되며, 이들을 붙이면 $M$ 위의 stack을 얻을 수 있다.

::: 정의 5
Deligne–Mumford stack $M$의 *intrinsic normal sheaf* $\mathfrak{N}_M$과 *intrinsic normal cone* $\mathfrak{c}_M\subset\mathfrak{N}_M$은 모든 local embedding $U\hookrightarrow W$에 대하여

$$\mathfrak{N}_M\vert_U=[N_{U/W}/T_W\vert_U],\qquad\mathfrak{c}_M\vert_U=[C_{U/W}/T_W\vert_U]$$

가 되도록 붙여서 얻은 stack이다.
:::

[정의 5](#def5){: data-lid="6z7ze" }에서 cone을 tangent 방향으로 나눈 것은 [§§벡터다발의 zero locus](#벡터다발의-zero-locus){: data-lid="kwjq5" }의 Kuranishi 그림과 같은 현상이다. 거기서 $\im(\dd{s}_x)$ 방향의 coordinate와 방정식이 짝지어 사라지고 $\dd{s}_x$의 kernel과 cokernel만 남았듯, local embedding을 바꿀 때 complex $[T_W\vert_U\rightarrow N_{U/W}]$의 두 항에 더해지는 방향도 서로 상쇄되어 ([명제 3](#prop3){: data-lid="kpude" }) tangent와 obstruction만 남는다.

이는 cotangent complex를 이용하여 다음과 같이 살펴볼 수도 있다. Stack $M$은 cotangent complex $\LL_M$을 가지며, 그 가운데 deformation과 obstruction이 잡히는 것은 truncation $\tau_{\geq-1}\LL_M$이다. ([\[스킴\] §변형이론과 여접 복합체, §§변형의 장애와 고차 변형이론](/ko/math/scheme_theory/deformation_theory#변형의-장애와-고차-변형이론){: data-lid="0fpnl" }) Local embedding $U\hookrightarrow W$에서 $U$의 ideal sheaf를 $\mathcal{I}$라 하면 이 truncation은

$$\tau_{\geq-1}\LL_M\vert_U=\Bigl[\at{-1}{\mathcal{I}/\mathcal{I}^2}\xrightarrow{\ \dd{\ }}\at{0}{\Omega_W\vert_U}\Bigr]$$

이 되고, 각 항을 abelian cone $\Spec_U\Sym(-)$로 바꾸는 dual을 $(-)^\vee$로 적으면 $(\tau_{\geq-1}\LL_M)^\vee\vert_U=[T_W\vert_U\rightarrow N_{U/W}]$, 곧 위의 complex가 된다. 이 상황에서 $T_W\vert_U$는 이 map을 통해 $N_{U/W}$에 평행이동으로 작용하므로 quotient stack $[N_{U/W}/T_W\vert_U]$가 정의되고, 이를 $h^1/h^0((\tau_{\geq-1}\LL_M)^\vee)$로 적는다. 이 표기에 대하여 [정의 5](#def5){: data-lid="6du8d" }는

$$\mathfrak{N}_M=h^1/h^0((\tau_{\geq-1}\LL_M)^\vee)$$

를 준다. 여기에서 우변은 local embedding과 무관하게 적어진 식이며, 이것이 다시 $\mathfrak{N}_M$이 embedding의 선택에 의존하지 않는다는 것을 보여 준다.

::: 명제 6
Intrinsic normal cone $\mathfrak{c}_M$은 pure dimension $0$이다.
:::
::: 증명
Local embedding $U\hookrightarrow W$에서 $W$가 pure dimension이라 하자. Normal cone $C_{U/W}$는 pure dimension $\dim W$이고, quotient map $C_{U/W}\rightarrow[C_{U/W}/T_W\vert_U]$는 $T_W\vert_U$-torsor이므로 relative dimension $\dim W$의 smooth surjection이다. 따라서 $\mathfrak{c}_M\vert_U$의 차원은 $\dim W-\dim W=0$이다.
:::

$M$이 smooth이면 $W=M$으로 잡을 수 있으므로 $\mathfrak{c}_M=[0/T_M]=\bB T_M$이고, 이 $0$은 그 차원 $\dim M-\dim M$이다. 즉 차원 $0$이라는 것은 $\mathfrak{c}_M$이 normal 방향을 tangent 방향만큼 나눈 것이라는 데에서 오며, 이 수가 아래에서 virtual dimension을 고정한다.

## Perfect obstruction theory

앞 절에서 intrinsic normal sheaf는 truncation $\tau_{\geq-1}\LL_M$으로 결정되었다. $M$이 vector bundle의 section의 zero locus $Z(s)\subset X$로 주어지는 경우 이 truncation은 

$$[\mathcal{I}/\mathcal{I}^2\rightarrow\Omega_X\vert_{Z(s)}]$$

이다. 여기서 $\mathcal{I}/\mathcal{I}^2$은 일반적으로 vector bundle이 아니지만, localized Euler class를 정의할 때 실제로 쓴 것은 surjection $s^\vee:E^\vee\vert_{Z(s)}\rightarrow\mathcal{I}/\mathcal{I}^2$으로 이를 덮는 vector bundle $E^\vee\vert_{Z(s)}$뿐이었다. 즉 $\mathcal{I}/\mathcal{I}^2$을 $E^\vee\vert_{Z(s)}$로 바꾼 complex

$$E^\bullet=\Bigl[\at{-1}{E^\vee\vert_{Z(s)}}\xrightarrow{\ (\dd{s})^\vee\ }\at{0}{\Omega_X\vert_{Z(s)}}\Bigr]$$

와 morphism $E^\bullet\rightarrow\tau_{\geq-1}\LL_{Z(s)}$를 보면 이 complex의 dual은 Kuranishi 그림의 complex 

$$[T_X\vert_{Z(s)}\xrightarrow{\dd{s}}E\vert_{Z(s)}]$$

이고, 그 cohomology

$$h^0((E^\bullet)^\vee)=\ker(\dd{s}),\qquad h^1((E^\bullet)^\vee)=\coker(T_X\vert_{Z(s)}\rightarrow E\vert_{Z(s)})$$

가 tangent space와 obstruction space를 준다. 일반적인 $M$에서 이러한 complex를 요구하는 것이 다음의 정의이다.

::: 정의 7 (Behrend–Fantechi)
$M$을 Deligne–Mumford stack이라 하자. $M$ 위의 *perfect obstruction theory<sub>완전 장애 이론</sub>*란 국소적으로 vector bundle 두 항의 complex $[E^{-1}\rightarrow E^0]$과 quasi-isomorphic한 complex $E^\bullet$과 morphism

$$\phi:E^\bullet\rightarrow\tau_{\geq-1}\LL_M$$

의 쌍으로서, $h^0(\phi)$가 isomorphism이고 $h^{-1}(\phi)$가 surjection인 것을 말한다.
:::

일반적으로 $\mathfrak{c}_M$을 담고 있는 $\mathfrak{N}_M$은 $\mathcal{I}/\mathcal{I}^2$이 vector bundle이 아니므로 일반적으로 vector bundle stack이 아니고, 따라서 그 안에서는 $\mathfrak{c}_M$을 zero section으로 자르는 등의 행동을 할 수 없다. 반면 perfect obstruction theory $E^\bullet$은 국소적으로 vector bundle들로 이루어져 있으므로, $\mathfrak{c}_M$을 $E^\bullet$이 정하는 vector bundle stack 안에 넣을 수 있다면 그 안에서 자를 수 있게 해 준다.

더 구체적으로, $\phi$의 dual은 morphism

$$\phi^\vee:\mathfrak{N}_M\rightarrow\mathfrak{E}=h^1/h^0((E^\bullet)^\vee)$$

를 유도하며, 국소적으로 $E^\bullet=[E^{-1}\rightarrow E^0]$이면 $E_i=(E^{-i})^\vee$에 대하여 $\mathfrak{E}=[E_1/E_0]$이다. 앞의 모형에서는 $\phi^{-1}=s^\vee$이므로 $\phi^\vee$는 normal cone을 $E\vert_{Z(s)}$ 안에 넣던 map $N_{Z(s)/X}\rightarrow E\vert_{Z(s)}$를 tangent 방향으로 나눈 것이다. 즉 $\mathfrak{N}_M$이 진짜 normal 방향을 진짜 tangent 방향으로 나눈 것이라면, $\mathfrak{E}$는 perfect obstruction theory가 내놓은 obstruction bundle $E_1$을 $E_0$로 나눈 것으로, 같은 역할을 하되 vector bundle로 이루어진 쪽이다. [정의 7](#def7){: data-lid="nb0iz" }의 두 조건은 바로 이 morphism이 $\mathfrak{N}_M$을, 따라서 $\mathfrak{c}_M$을 $\mathfrak{E}$ 안에 closed하게 넣는다는 것과 동치이며, 이것이 다음 정리이다. 이 정리는 [BF, Proposition 2.6]을 cotangent complex에 적용한 것으로, [BF, Theorem 4.5]의 일부이다.

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

이로부터 [정의 7](#def7){: data-lid="3zi1b" }의 두 조건을 점마다 읽을 수 있다. $h^0(\phi)$가 isomorphism이라는 것은 $E^\bullet$의 $0$차 항이 $M$의 deformation을 정확히 재현한다는 뜻이고, $h^{-1}(\phi)$가 surjection이라는 것은 $E^\bullet$의 $-1$차 항이 $M$의 obstruction을 <em-ko>빠짐없이</em-ko> 담는다는 뜻이다. 즉 $E^\bullet$ 쪽에 실제보다 많은 obstruction이 있는 것은 허용되지만 하나라도 빠뜨리는 것은 허용되지 않는다. 실제로 점 $p$에서 보면 $\phi^\vee$는 $M$의 $p$에서의 obstruction space $h^1((\tau_{\geq-1}\LL_M)^\vee\vert_p)$에서 $\phi$의 obstruction space $h^1((E^\bullet)^\vee\vert_p)$로 가는 injective map을 주므로, 어떤 perfect obstruction theory의 obstruction space도 $M$ 자신의 obstruction space를 포함한다. 특히 이 절의 처음에 $Z(s)\hookrightarrow X$로부터 만든 morphism $E^\bullet\rightarrow\tau_{\geq-1}\LL_{Z(s)}$는 degree $0$에서 $\Omega_X\vert_{Z(s)}$의 identity이고 degree $-1$에서 surjection $s^\vee$이므로, [정리 8](#thm8){: data-lid="y9tij" }의 증명에서 본 것처럼 실제로 perfect obstruction theory이다.

Perfect obstruction theory는 $M$만으로 정해지는 것이 아니라 $M$ 위에 추가로 주어지는 자료이며, 같은 $M$ 위에도 서로 다른 perfect obstruction theory가 있을 수 있다. 앞으로 정의할 virtual class는 이 선택에 의존한다.

::: 예시 9
$\mathbb{P}^2$ 안의 직선 $L=\{\x=0\}$을 두 가지 방식으로 zero locus로 표현하자. 하나는 $E=\mathcal{O}(1)^{\oplus2}$와 $s=(\x,\x)$이고, 다른 하나는 $E'=\mathcal{O}(1)\oplus\mathcal{O}(2)$와 $s'=(\x,\x^2)$이다. 두 ideal $(\x,\x)$와 $(\x,\x^2)$는 모두 $(\x)$이므로 $Z(s)=Z(s')=L$이다. 그러나 위에서 본 것처럼 두 표현은 $L$ 위에 서로 다른 두 perfect obstruction theory

$$E^\bullet=[E^\vee\vert_L\rightarrow\Omega_{\mathbb{P}^2}\vert_L],\qquad E'^\bullet=[E'^\vee\vert_L\rightarrow\Omega_{\mathbb{P}^2}\vert_L]$$

를 주며, 그 virtual dimension은 모두 $2-2=0$이다.
:::

즉 같은 scheme $L$ 위에 서로 다른 두 perfect obstruction theory가 있으며, 이들은 같은 intrinsic normal cone $\mathfrak{c}_L$을 서로 다른 $\mathfrak{E}$ 안에 넣는다. 다음 절에서 만드는 virtual class는 공간 $M$이 아니라 이렇게 고른 perfect obstruction theory로부터 나온다.

## 가상 기본류의 구성

Perfect obstruction theory $\phi:E^\bullet\rightarrow\tau_{\geq-1}\LL_M$이 주어지면 [정리 8](#thm8){: data-lid="3duhl" }에 의하여 pure dimension $0$의 closed substack

$$\mathfrak{c}_M\subset\mathfrak{N}_M\hookrightarrow\mathfrak{E}$$

를 얻으며, [BF]는 $\mathfrak{E}$ 안의 이 substack을 $\phi$의 *obstruction cone*이라 부른다. Virtual class는 obstruction cone을 $\mathfrak{E}$의 zero section으로 자른 것이다.

다만 $\mathfrak{E}$는 국소적으로 $[E_1/E_0]$, 곧 vector bundle $E_1$을 vector bundle $E_0$의 평행이동으로 나눈 것이므로, 각 점이 $E_0\rightarrow E_1$의 kernel이라는 벡터공간만큼의 automorphism을 갖는 Artin stack이다. 따라서 그 안에서 zero section으로 자르려면 Artin stack의 Chow group과 그 위의 Gysin map이 필요하다. 이를 피하기 위해 [BF]는 $E^\bullet$이 *global resolution*, 곧 전역적인 vector bundle들의 complex $F^\bullet=[F^{-1}\rightarrow F^0]$과의 isomorphism $F^\bullet\cong E^\bullet$을 갖는다고 가정한다. 이 때 $F_i=(F^{-i})^\vee$로 두면 $\mathfrak{E}=[F_1/F_0]$이고, quotient map $F_1\rightarrow\mathfrak{E}$는 fiber가 $F_0$인 smooth surjection이다. 따라서 $\mathfrak{c}_M$을 이 map으로 당기면 $M$ 위의 실제 vector bundle $F_1$ 안의 cone을 얻고, 이를 자르는 것은 Deligne–Mumford stack $M$ 위의 보통의 Gysin map으로 할 수 있다.

즉 [§§벡터다발의 zero locus](#벡터다발의-zero-locus){: data-lid="8efcp" }에서 normal cone $C_{Z/X}$가 하던 역할을 일반적인 $M$에서는 $\mathfrak{c}_M$이 하고, 이를 $F_1$로 끌어올리면 그 교차를 실제로 계산할 수 있다. 국소 모형에서는 $F_0=T_X\vert_Z$, $F_1=E\vert_Z$로 잡을 수 있고 $\mathfrak{c}_Z=[C_{Z/X}/T_X\vert_Z]$를 $E\vert_Z$로 끌어올린 것은 $C_{Z/X}$ 자신이므로, 이는 localized Euler class를 정의할 때 [예시 2](#ex2){: data-lid="nhbvj" }에서 한 일과 정확히 같다. 따라서 다음과 같이 정의하는 것이 자연스럽다.

::: 정의 10
Deligne–Mumford stack $M$ 위의 perfect obstruction theory $E^\bullet$이 global resolution $F^\bullet$을 갖는다 하자. Fiber product

$$C(F^\bullet)=\mathfrak{c}_M\times_{\mathfrak{E}}F_1\subset F_1$$

에 대하여, $M$의 *virtual fundamental class*를

$$[M]^\vir=0^!_{F_1}[C(F^\bullet)]$$

로 정의한다. 이를 $0^!_{E^\bullet}[\mathfrak{c}_M]$으로도 적는다.
:::

이 정의는 global resolution의 선택에 의존하지 않는다. ([BF, Proposition 5.3]) Virtual class는 $\mathfrak{E}$ 안의 obstruction cone을 zero section으로 자른 것이고, $F_1$은 이 교차를 vector bundle 위에서 계산하기 위해 고른, $\mathfrak{E}$를 덮는 vector bundle일 뿐이기 때문이다. 차원도 맞는다. $\mathfrak{c}_M$을 $F_1\rightarrow\mathfrak{E}$를 따라 당기면 차원이 그 fiber의 차원 $\rank F_0$만큼 올라가므로, [명제 6](#prop6){: data-lid="w91yv" }에 의해 $C(F^\bullet)$은 pure dimension $\rank F_0$이다. 이를 rank $\rank F_1$의 vector bundle의 zero section으로 자르면 차원이 $\rank F_1$만큼 떨어지므로

$$\dim[M]^\vir=\rank F_0-\rank F_1=\rank E^\bullet=\vdim$$

이다. 즉 virtual dimension은 차원 $0$의 cone을 relative dimension $-\vdim$의 vector bundle stack 안에서 zero section과 교차시킨 결과이며, 그 차원을 고정하는 것은 [명제 6](#prop6){: data-lid="o80lg" }의 purity이다.

이 정의에서 $\mathfrak{c}_M$은 $M$만으로 정해지므로, virtual class를 정하는 것은 $\mathfrak{c}_M$ 자체가 아니라 $\mathfrak{c}_M$이 $\mathfrak{E}$ 안에 놓이는 방식이고, 그것은 $\phi$가 정한다.

::: 예시 11
[예시 9](#ex9){: data-lid="thqsa" }의 두 perfect obstruction theory가 주는 virtual class를 계산하자. 위에서 본 것처럼 이들은 각각의 localized Euler class이다. $L$은 Cartier divisor이므로 normal cone은 두 경우 모두 같은 line bundle $N_{L/\mathbb{P}^2}=\mathcal{O}_L(1)$이고, 달라지는 것은 이 cone이 들어가는 곳이다. 각각 $E\vert_L$과 $E'\vert_L$ 안에 $\mathcal{I}/\mathcal{I}^2=\mathcal{O}_L(-1)$로 가는 map의 dual을 통해 놓이며, 첫째 경우에는 $E^\vee$의 두 basis가 모두 $\x$로 가므로 이 embedding은

$$N_{L/\mathbb{P}^2}\xrightarrow{(1,1)}\mathcal{O}_L(1)^{\oplus2}$$

이고, 둘째 경우에는 $\x^2\in\mathcal{I}^2$이므로

$$N_{L/\mathbb{P}^2}\xrightarrow{(1,0)}\mathcal{O}_L(1)\oplus\mathcal{O}_L(2)$$

이다. 둘 다 subbundle이므로 zero section으로 자르면 quotient line bundle의 $c_1$이 남고, 그 degree는 각각 $\deg\mathcal{O}_L(1)=1$과 $\deg\mathcal{O}_L(2)=2$이다. 이는 $c_2(E)=H^2$, $c_2(E')=2H^2$과도 맞는다. 즉 같은 scheme $L$ 위의 두 perfect obstruction theory는 같은 차원의 서로 다른 virtual class를 준다.

[예시 1](#ex1){: data-lid="7uho0" }의 $\mathbb{P}^2$에서도 같은 일이 일어난다. Smooth한 $\mathbb{P}^2$에 $\Omega_{\mathbb{P}^2}$ 자신을 perfect obstruction theory로 주면 $F_1=0$이므로 $C(F^\bullet)=\mathbb{P}^2$이고 virtual class는 $[\mathbb{P}^2]$이지만, $\mathcal{O}(1)^{\oplus2}$의 zero section $s\equiv0$으로 본 perfect obstruction theory는 차원이 $2$ 작은 point class를 준다.
:::

따라서 virtual class를 fundamental class를 대체하는 올바른 차원의 class라고 부를 때, 그 차원과 class를 고르는 것은 공간이 아니라 $\phi$이다.

지금까지의 perfect obstruction theory는 cotangent complex $\LL_M=\LL_{M/\Spec\mathbb{K}}$을 대상으로 한다. 우리는 base scheme $S$ 위에 정의된 $S$-scheme들을 생각하는 것처럼, perfect obstruction theory 또한 base $\mathfrak{B}$에 대한 relative 버전을 만들어줄 수 있다. 

Pure dimensional smooth Artin stack $\mathfrak{B}$가 주어졌다 하고, Deligne-Mumford stack $M$에서 $\mathfrak{B}$로의 structure morphism $q:M\rightarrow \mathfrak{B}$가 주어졌다 하자. 그럼 [정의 7](#def7){: data-lid="5uak4" }에서 $\tau_{\geq-1}\LL_M$을 $\tau_{\geq-1}\LL_{M/\mathfrak{B}}$로 바꾸어 $q$에 대한 *relative perfect obstruction theory*를 정의할 수 있다. 비슷하게, local embedding $U\hookrightarrow W$를 $W$가 $\mathfrak{B}$ 위에서 smooth하도록 잡고 [정의 5](#def5)에서 $T_W\vert_U$ 대신 relative tangent bundle $T_{W/\mathfrak{B}}\vert_U$로 나누어

$$\mathfrak{N}_{M/\mathfrak{B}}\vert_U=[N_{U/W}/T_{W/\mathfrak{B}}\vert_U],\qquad\mathfrak{c}_{M/\mathfrak{B}}\vert_U=[C_{U/W}/T_{W/\mathfrak{B}}\vert_U]$$

로 두면 *relative intrinsic normal sheaf* $\mathfrak{N}_{M/\mathfrak{B}}$와 *relative intrinsic normal cone* $\mathfrak{c}_{M/\mathfrak{B}}\subset\mathfrak{N}_{M/\mathfrak{B}}$를 얻는다. 그럼 이렇게 정의한 relative 버전에서도 [정리 8](#thm8){: data-lid="bdguf" }과 [정의 10](#def10){: data-lid="kzesu" }은 그대로 성립한다는 것을 보일 수 있다.

이 상황에서 다소 신경을 써 주어야 하는 것은 차원으로, $C_{U/W}$는 pure dimension $\dim W$이고 $T_{W/\mathfrak{B}}$의 rank는 $\dim W-\dim\mathfrak{B}$이므로, [명제 6](#prop6){: data-lid="8mnqd" }의 증명과 같이 차원을 세 보면 relative intrinsic normal cone $\mathfrak{c}_{M/\mathfrak{B}}$의 차원은 pure dimension $\dim\mathfrak{B}$이고, 따라서 virtual class $[M]^\vir$은 $A_{\dim\mathfrak{B}+\rank E^\bullet}(M)$에 놓이게 된다. 

다음은 perfect obstruction theory와 그것이 정하는 virtual class의 성질이다. 

::: 명제 12
Deligne–Mumford stack $M$ 위의 perfect obstruction theory $\phi:E^\bullet\rightarrow\tau_{\geq-1}\LL_M$에 대하여, virtual class $[M]^\vir=0^!_{E^\bullet}[\mathfrak{c}_M]$은 다음을 만족한다.

1. $[M]^\vir$은 virtual dimension $\vdim=\rank E^\bullet=\rank E^0-\rank E^{-1}$의 cycle이다.
2. $M$이 family의 fiber로 주어지고 $\phi$가 family 위의 perfect obstruction theory와 compatible하면, $[M]^\vir$은 family의 virtual class를 fiber로 Gysin pullback한 것이다. 특히 $[M]^\vir$은 family 안에서의 deformation에 대해 불변이다.
3. $h^1((E^\bullet)^\vee)=0$이면 $M$은 smooth하고 $[M]^\vir=[M]$은 보통의 fundamental class이다.
4. $M$이 smooth하고 $h^1((E^\bullet)^\vee)$가 rank $r$의 vector bundle이면 $[M]^\vir=c_r(h^1((E^\bullet)^\vee))\cap[M]$이다.
:::

첫째 주장은 이미 위에서 살펴보았다. 셋째 주장과 넷째 주장의 가정에서는 $M$의 smoothness로부터 $\mathfrak{c}_M=\bB T_M$이고, 따라서 $C(F^\bullet)$은 $F_0\rightarrow F_1$의 image가 된다. 셋째 주장의 가정에서는 이 image가 $F_1$ 전체가 되므로 $[M]$이 남게 되며, 넷째 주장의 가정에서는 이 image가 cokernel이 $h^1((E^\bullet)^\vee)$인 subbundle이므로, $h^1((E^\bullet)^\vee)$의 top Chern class가 남게 된다. 셋째와 넷째 주장은 smooth를 $\mathfrak{B}$ 위에서 smooth로 바꾸면 relative perfect obstruction theory에 대해서도 그대로 성립한다. ([BF, Proposition 7.3])

다소 설명이 필요한 것은 둘째 주장의 compatibility이다. 우선 둘째 주장을 식으로 엄밀하게 적기 위해 $\mathcal{X}$를 smooth variety $B$ 위의 Deligne–Mumford stack이라 하고, 점 $b\in B$에서의 fiber가 $M$이며 $i:M\hookrightarrow\mathcal{X}$라 하자. 그럼 $M\rightarrow\mathcal{X}\rightarrow\Spec\mathbb{K}$에 대하여 cotangent complex들 사이의 distinguished triangle

$$i^\ast\LL_{\mathcal{X}/\Spec\mathbb{K}}\rightarrow\LL_{M/\Spec\mathbb{K}}\rightarrow\LL_{M/\mathcal{X}}\rightarrow i^\ast\LL_{\mathcal{X}/\Spec\mathbb{K}}[1]$$

이 존재하던 것을 기억하자. $\mathcal{X}$ 안에서 $M$의 ideal sheaf를 $\mathcal{I}$라 하면 $i$가 closed embedding이므로 $h^0(\LL_{M/\mathcal{X}})=0$이고 $h^{-1}(\LL_{M/\mathcal{X}})=\mathcal{I}/\mathcal{I}^2$이며, 따라서 이 triangle은 [\[가환대수학\] §미분, ⁋명제 9](/ko/math/commutative_algebra/differentials#prop9)의 conormal sequence $\mathcal{I}/\mathcal{I}^2\rightarrow i^\ast\Omega_{\mathcal{X}}\rightarrow\Omega_M\rightarrow0$을 왼쪽으로 연장한 것이고 그 셋째 항은 $M$을 $\mathcal{X}$에서 잘라내는 방정식을 기록한다. 

그럼 이 상황에서, $\mathcal{X}$의 perfect obstruction theory $\phi_{\mathcal{X}}:E_{\mathcal{X}}^\bullet\rightarrow\tau_{\geq-1}\LL_{\mathcal{X}}$가 $M$의 perfect obstruction theory $\phi: E^\bullet \rightarrow \tau_{\geq-1}\LL_M$와 compatible하다는 것은 triangle 

$$i^\ast E_{\mathcal{X}}^\bullet\rightarrow E^\bullet\rightarrow\mathcal{O}_M^{\oplus\dim B}[1]\rightarrow i^\ast E_{\mathcal{X}}^\bullet[1]$$

이 존재하여 이것이 위의 triangle로 가는 morphism of triangles

{% diagram Math/Gromov_Witten_Theory/Perfect_Obstruction_Theory-2.svg width="26.17em" alt="compatibility as a morphism of triangles" %}

을 이룬다는 것이다. 여기서 셋째 항 $\mathcal{O}_M^{\oplus\dim B}[1]$과 셋째 vertical map은 cartesian diagram

{% diagram Math/Gromov_Witten_Theory/Perfect_Obstruction_Theory-3.svg width="6.34em" alt="the fiber over b as a cartesian square" %}

에서 오는 것이다. 즉, 셋째 vertical map은 위의 diagram이 유도하는 자연스러운 map $g^\ast\LL_{\{b\}/B}\rightarrow\LL_{M/\mathcal{X}}$으로, 여기에 다음 identification

$$g^\ast\LL_{\{b\}/B}=g^\ast(\mathfrak{m}_b/\mathfrak{m}_b^2)[1]\cong\mathcal{O}_M^{\oplus\dim B}[1],\qquad\mathfrak{m}_b=(t_1,\cdots,t_{\dim B})$$

을 적용한 것이다. $M=\mathcal{X}\times_B\{b\}$이므로 $\mathcal{I}$는 $\mathfrak{m}_b$를 당긴 것으로 생성되고, 따라서 이 map은 $h^{-1}$에서 surjective이다. 곧 윗줄의 triangle은 $M$의 perfect obstruction theory가 $\mathcal{X}$의 것을 $M$으로 당긴 것에 fiber의 normal 방향 $\mathcal{O}_M^{\oplus\dim B}$를 더한 것이라는 뜻이고, 셋째 vertical map의 surjectivity는 이렇게 더한 항이 $M$을 $\mathcal{X}$에서 잘라내는 방정식 $\mathcal{I}/\mathcal{I}^2$를 빠짐없이 덮는다는 뜻이다. 그럼 이 가정 하에서 둘째 주장은 $\{b\}\hookrightarrow B$의 refined Gysin map $i_b^!:A_k(\mathcal{X})\rightarrow A_{k-\dim B}(M)$에 대한 등식

$$[M]^\vir=i_b^![\mathcal{X}]^\vir$$

이다. 이 등식은 zero section의 Gysin map과 $i_b^!$의 순서를 바꾼 뒤, $i_b^!$가 $\mathcal{X}$의 cone의 class를 $M$의 cone의 class로 보낸다는 데서 나온다.

## 안정사상들의 가상 기본류

이제 stable map들의 moduli stack $M=\overline{\mathcal{M}}_{g,n}(X,\beta)$ 위에 perfect obstruction theory를 구성하자. 이를 위해 우리는 target $X$의 tangent space $T_X$를

$$\pi:\mathcal{C}\rightarrow M,\qquad\mu:\mathcal{C}\rightarrow X$$

를 사용하여 가지고 온다. 즉 $T_X$를 $\mu$를 사용하여 pullback해온 후, 이를 다시 $R\pi_\ast$를 사용하여 밀어내린 $R\pi_\ast\mu^\ast T_X$를 사용하는 것이다. 이 때 곡선의 차원이 $1$이므로 higher direct image $R^i\pi_\ast$는 $i=0,1$에서만 살아남게 되며, 따라서 이 complex는 정확히 degree $0$과 $1$에 놓이는 two-term complex가 되고 각 점에서 $H^0(C,\mu^\ast T_X)$와 $H^1(C,\mu^\ast T_X)$를 그 cohomology로 복원한다. 

따라서 위에서 얻은 $R\pi_\ast\mu^\ast T_X$의 dual $E^\bullet=(R\pi_\ast\mu^\ast T_X)^\vee$는 $[-1,0]$ amplitude의 complex로, 우리가 원하는 perfect obstruction theory의 후보가 된다. 다만 이는 domain curve $(C,p_\bullet)$을 고정한 채 map $\mu$만을 변형하는 자료이므로, prestable curve들의 moduli stack $\mathfrak{M}_{g,n}$으로 가는 morphism $q:M\rightarrow\mathfrak{M}_{g,n}$에 대한 relative perfect obstruction theory를 이룬다. 여기서 우리를 도와주는 것은 base stack $\mathfrak{M}_{g,n}$이 smooth하다는 것으로, 직관적으로 이는 node를 펼 때는 어떠한 obstruction도 없기 때문이다. 즉 $\mathfrak{M}_{g,n}$에는 perfect obstruction theory 없이도 이미 (진짜) fundamental class가 있고, 이를 relative perfect obstruction theory로 가져올 수 있다.

이때 relative perfect obstruction theory는 [명제 12](#prop12){: data-lid="av5wc" } 앞에서 정의한 것에서 $\mathfrak{B}=\mathfrak{M}_{g,n}$으로 둔 것이므로, virtual class는 $A_{\dim\mathfrak{M}_{g,n}+\rank E^\bullet}(M)$에 놓인다. 

::: 명제 13 (Behrend)
$M=\overline{\mathcal{M}}_{g,n}(X,\beta)$와 forgetful morphism $q:M\rightarrow\mathfrak{M}_{g,n}$에 대하여, 위의 complex $E^\bullet=(R\pi_\ast\mu^\ast T_X)^\vee$는 $q$에 대한 relative perfect obstruction theory $\phi:E^\bullet\rightarrow\LL_{M/\mathfrak{M}_{g,n}}$를 이룬다. 이는 $M$ 위의 (absolute) perfect obstruction theory $(E')^\bullet\rightarrow\tau_{\geq-1}\LL_M$을 유도하며, 이로부터 얻어지는 $M$의
 virtual class $[M]^\vir$의 차원은 virtual dimension

$$\vdim=\int_\beta c_1(T_X)+(\dim X-3)(1-g)+n$$

이다.
:::

위에서 살펴보았듯 relative complex $(R\pi_\ast\mu^\ast T_X)^\vee$가 relative perfect obstruction theory가 되므로, 실제로 보여야 할 것은 이로부터 absolute perfect obstruction theory를 얻는 과정이다. 즉 다음 diagram

{% diagram Math/Gromov_Witten_Theory/Perfect_Obstruction_Theory-4.svg width="26.48em" alt="absolute obstruction theory from the relative one" %}

에서 둘째 vertical map을 만들어야 하고, 이는 합성 $a:E^\bullet\xrightarrow{\phi}\LL_{M/\mathfrak{M}_{g,n}}\rightarrow q^\ast\LL_{\mathfrak{M}_{g,n}}[1]$에 대하여 $(E')^\bullet=\Cone(a)[-1]$로 정의하면 양 끝의 vertical map이 주어져 있으므로 자동으로 존재한다. 이렇게 얻은 $\phi'$이 $h^0$에서 isomorphism이고 $h^{-1}$에서 surjective라는 것은 five lemma에서 나온다. 이 때 base의 smoothness는 $q^\ast\LL_{\mathfrak{M}_{g,n}}$에 음의 degree 항이 없게 하고, $M$이 Deligne–Mumford stack이라는 것은 curve의 무한소 automorphism이 담긴 degree $1$ 항을 죽이므로, 둘이 함께 $(E')^\bullet$의 amplitude를 $[-1,0]$으로 지켜주어 이를 perfect obstruction theory로 만들게 된다. 

이 triangle은 relative obstruction과 absolute obstruction의 관계도 알려준다. Triangle을 dualize하여 점 $z=[(C,p_\bullet,\mu)]$에서의 derived fiber의 cohomology를 취하면, $M$이 Deligne–Mumford stack이고 $\mathfrak{M}_{g,n}$이 smooth하므로 양 끝이 $0$인 exact sequence

$$\begin{aligned}0&\rightarrow h^{-1}(q^\ast\LL_{\mathfrak{M}_{g,n}}^\vee\vert_z)\rightarrow h^0((E^\bullet)^\vee\vert_z)\rightarrow h^0(((E')^\bullet)^\vee\vert_z)\\&\rightarrow h^0(q^\ast\LL_{\mathfrak{M}_{g,n}}^\vee\vert_z)\rightarrow h^1((E^\bullet)^\vee\vert_z)\rightarrow h^1(((E')^\bullet)^\vee\vert_z)\rightarrow0\end{aligned}$$

을 얻는다. 각 항은 차례로 marked curve의 무한소 automorphism, $H^0(C,\mu^\ast T_X)$, $T^1$, marked curve의 deformation, $H^1(C,\mu^\ast T_X)$, $T^2$이고, 이는 [§안정사상들의 모듈라이 공간, ⁋명제 4](/ko/math/gromov-witten_theory/moduli_of_stable_maps#prop4){: data-lid="ydjrs" }의 exact sequence이다. 특히 relative obstruction $H^1(C,\mu^\ast T_X)$는 absolute obstruction $T^2$로 surjective하게 가고, 그 kernel은 curve의 deformation, 가령 node를 펴는 방향의 image이다. 따라서 relative하게 unobstructed인 점은 absolute하게도 unobstructed이다. 반대로 $H^1(C,\mu^\ast T_X)\neq0$이더라도 그 전체가 curve의 deformation의 image이면 $T^2=0$이므로, relative하게는 obstructed이지만 absolute하게는 unobstructed인 점이 있을 수 있다.

::: 예시 14
$X$가 convex인 경우 모든 genus $0$ stable map에서 $H^1(C,\mu^\ast T_X)=0$이므로 ([§안정사상들의 모듈라이 공간, ⁋명제 5](/ko/math/gromov-witten_theory/moduli_of_stable_maps#prop5){: data-lid="c4h5h" }) obstruction space가 $h^1((E^\bullet)^\vee)=R^1\pi_\ast\mu^\ast T_X=0$이다. 이제 위에서 살펴본 것과 마찬가지 이유로, $\mathfrak{M}_{0,n}$의 smoothness에 의해 absolute obstruction 또한 $h^1(((E')^\bullet)^\vee)=0$이 되므로, [명제 12](#prop12){: data-lid="vrq63" }의 (3)에 의해

$$[\overline{\mathcal{M}}_{0,n}(X,\beta)]^\vir=[\overline{\mathcal{M}}_{0,n}(X,\beta)]$$

이 되어 virtual class가 보통의 fundamental class와 일치한다. $X=\mathbb{P}^r$와 Grassmannian, 일반적인 flag variety $G/P$가 모두 이 경우에 해당하며, 여기에서의 genus $0$ curve counting은 smooth moduli의 (진짜) fundamental class에 대한 적분과 동일하게 나오며, 이것이 이전 글의 계산을 정당화한다. 
:::

[§그로모프-위튼 불변량, ⁋정의 1](/ko/math/gromov-witten_theory/gromov-witten_invariants#def1){: data-lid="gt4df" }에서 우리는 fundamental class $[\overline{\mathcal{M}}_{0,n}(X,\beta)]$가 존재하는 경우에 대해서만 정의하였으나, 이 fundamental class만 virtual fundamental class로 바꿔주면 convex 가정 없이도 임의의 smooth projective target $X$에 대한 genus $0$ Gromov-Witten invariant를 정의할 수 있으며, convex 가정 하에서 이 두 정의가 같은 것은 위의 [예시 14](#ex14){: data-lid="bt6x3" }에 의해 자명하다. 그럼 이 정의 하에서, virtual class가 forgetful morphism 및 gluing morphism에 대해 잘 행동하는 것을 확인할 수 있으므로 [§그로모프-위튼 불변량, §§그로모프-위튼 불변량의 공리들](/ko/math/gromov-witten_theory/gromov-witten_invariants#그로모프-위튼-불변량의-공리들){: data-lid="huqbc" }의 string·divisor·splitting 공리와 WDVV 관계도 해당 적분들을 virtual class에 대한 적분으로 해석하면 그대로 성립한다.

실제 moduli에서 [명제 12](#prop12)의 둘째 주장의 family는 base에 상대적인 perfect obstruction theory를 가지고 나온다. 가령 $X\times B$ 위의 vector bundle $E$의 section $\widetilde{s}$를 잡고 $s_b=\widetilde{s}\vert_{X\times\{b\}}$라 하면, family $\mathcal{X}=Z(\widetilde{s})$는 $B$ 상대 perfect obstruction theory $[E^\vee\vert_{\mathcal{X}}\rightarrow\Omega_{X\times B/B}\vert_{\mathcal{X}}]$를 가지며, 이를 fiber $M=Z(s_b)$로 당긴 것은 그대로 $M$의 perfect obstruction theory $[E^\vee\vert_M\rightarrow\Omega_X\vert_M]$이다. Target을 변형하는 stable map의 family에서도 $T_X$ 대신 target의 relative tangent bundle로 만든 [명제 13](#prop13)의 perfect obstruction theory가 같은 성질을 갖는다. 이처럼 $\mathcal{X}$의 $B$ 상대 perfect obstruction theory를 fiber로 당긴 것이 $M$의 perfect obstruction theory이면 compatibility는 저절로 성립하고, $[M]^\vir=i_b^![\mathcal{X}]^\vir$이다. ([BF, Proposition 7.2]) 이때 $\mathfrak{c}_M$은 $\mathfrak{c}_{\mathcal{X}/B}$를 $M$으로 제한한 것의 closed substack이지만 일반적으로 그 전체는 아니다. ([BF, Proposition 7.1])

## Zero locus의 가상 기본류

[§§벡터다발의 zero locus](#벡터다발의-zero-locus){: data-lid="1un49" }의 국소 모형에서 ambient는 smooth variety였다. 그러나 이 모형이 실제로 쓰이는 상황에서는 ambient 자신이 obstruction을 갖는 moduli인 경우가 많다. 가령 smooth projective variety $P$ 안의 smooth subvariety $Y$가 vector bundle $V$의 section $s$의 zero locus로 주어지면, $Y$로 가는 stable map은 $P$로 가는 stable map $f$ 가운데 $f^\ast s=0$인 것이다. 모든 genus $0$ stable map에 대해 $H^1(C,f^\ast V)=0$이면 $\pi_\ast\mu^\ast V$는 $P$의 genus $0$ moduli 위의 vector bundle이고, $Y$의 moduli는 그 section $f\mapsto f^\ast s$의 zero locus가 된다. 두 moduli는 모두 [명제 13](#prop13){: data-lid="3nmml" }의 virtual class를 가지므로, 자연스러운 질문은 [예시 1](#ex1){: data-lid="fn474" }에서처럼 둘이 Euler class로 이어지는지의 여부일 것이다. Stable map의 moduli는 $\mathfrak{M}_{g,n}$에 상대적인 perfect obstruction theory를 가지므로 처음부터 상대적인 형태로 적는다.

::: 명제 15 (Kim–Kresch–Pantev)
$\mathfrak{M}$을 locally finite type이고 pure dimensional인 smooth Artin stack, $q:M\rightarrow\mathfrak{M}$을 finite type Deligne–Mumford stack $M$에서의 morphism, $\phi:E^\bullet\rightarrow\LL_{M/\mathfrak{M}}$을 relative perfect obstruction theory라 하자. $M$ 위의 rank $r$ vector bundle $V$와 section $s$에 대하여 $i:Z=Z(s)\hookrightarrow M$을 그 zero locus라 하고, $Z$ 위의 relative perfect obstruction theory $\phi_Z:E_Z^\bullet\rightarrow\LL_{Z/\mathfrak{M}}$이 distinguished triangle

$$i^\ast E^\bullet\rightarrow E_Z^\bullet\rightarrow V^\vee\vert_Z[1]\rightarrow i^\ast E^\bullet[1]$$

에 들어가며, 이 triangle이 cotangent complex의 triangle $i^\ast\LL_{M/\mathfrak{M}}\rightarrow\LL_{Z/\mathfrak{M}}\rightarrow\LL_{Z/M}\rightarrow i^\ast\LL_{M/\mathfrak{M}}[1]$과 $\phi$, $\phi_Z$, 그리고 $s$가 주는 $V^\vee\vert_Z[1]\rightarrow\LL_{Z/M}$으로 compatible하다고 하자. 그럼

$$[Z]^\vir=0^!_{V,s}[M]^\vir,\qquad i_\ast[Z]^\vir=c_r(V)\cap[M]^\vir$$

이다. 여기서 $0^!_{V,s}$는 zero section의 refined Gysin map을 section $s$를 따라 적용한 것, 곧 [§§벡터다발의 zero locus](#벡터다발의-zero-locus){: data-lid="6g4xw" }에서 localized Euler class를 만든 연산이다.
:::

이는 [KKP, Theorem 1]을 zero section $0_V:M\rightarrow V$에 적용한 것이다. 이 정리는 relative perfect obstruction theory를 갖는 두 stack이 local complete intersection morphism $v$를 따라 cartesian하게 놓이고 두 obstruction theory가 cotangent complex의 triangle과 compatible하면, $v$의 refined Gysin map이 한쪽의 virtual class를 다른 쪽의 virtual class로 보낸다는 것이다. 지금의 경우 cartesian square는 $s$와 $0_V$의 fiber product $Z=M\times_VM$이고, $0_V$의 cotangent complex를 $Z$로 당긴 것이 $V^\vee\vert_Z[1]$이므로 위의 triangle이 정확히 그 compatibility 조건이 된다. [BF, Proposition 7.5]는 global resolution을 가정하고 $v$가 smooth하거나 $v$의 source와 target이 모두 base 위에서 smooth한 경우에 같은 등식을 주는데, zero section에 대해 뒤의 조건은 $M$이 $\mathfrak{M}$ 위에서 smooth하다는 것이다. [KKP, Theorem 1]은 이러한 가정 없이 base의 pure dimensionality와 $v$가 local complete intersection morphism이라는 것만을 요구하며, [KKP]는 이를 [BF, Proposition 7.5]를 강화한 것으로 소개한다. Base의 smoothness는 $\mathfrak{M}$ 상대 perfect obstruction theory로 정의한 virtual class가 [명제 13](#prop13){: data-lid="qmcty" }에서처럼 유도한 absolute perfect obstruction theory의 virtual class와 같다는 데에 쓰인다. ([KKP, Proposition 3]) 둘째 등식은 refined Gysin map에 대한 공식 $i_\ast0^!_{V,s}\gamma=c_r(V)\cap\gamma$를 $\gamma=[M]^\vir$에 적용한 것이다.

명제는 $E_Z^\bullet$을 가정으로 둔다. 일반적인 $(M,E^\bullet)$에서 이러한 $E_Z^\bullet$을 만들려면 $s$가 주는 $V^\vee\vert_Z[1]\rightarrow\LL_{Z/M}$과 cotangent complex의 triangle의 connecting map을 합성한 $V^\vee\vert_Z\rightarrow i^\ast\LL_{M/\mathfrak{M}}$을 $\phi$를 따라 $i^\ast E^\bullet$으로 들어 올려야 하는데, 그 obstruction은 $\phi$의 cone의 hypercohomology에 있어서 local하게만 사라지고 global하게는 자동이 아니다. 그래서 $E_Z^\bullet$은 경우마다 구성하며, 아래 [예시 16](#ex16){: data-lid="zy2k0" }에서는 universal curve 위의 vector bundle의 short exact sequence에 $R\pi_\ast$를 취해 이를 얻는다. 가장 간단한 경우는 $q$가 smooth한 경우이다. 이때는 $E^\bullet=\Omega_{M/\mathfrak{M}}$으로 둘 수 있고,

$$E_Z^\bullet=\Bigl[\at{-1}{V^\vee\vert_Z}\xrightarrow{\ (\dd{s})^\vee\ }\at{0}{\Omega_{M/\mathfrak{M}}\vert_Z}\Bigr]$$

이 $Z$의 relative perfect obstruction theory이다. $\tau_{\geq-1}\LL_{Z/\mathfrak{M}}=[\mathcal{I}/\mathcal{I}^2\rightarrow\Omega_{M/\mathfrak{M}}\vert_Z]$이고 $V^\vee\vert_Z\rightarrow\mathcal{I}/\mathcal{I}^2$이 surjective이므로, $h^0$에서는 isomorphism이고 $h^{-1}$에서는 surjective이다. 위의 triangle은 이 two-term complex의 stupid truncation이 주는 것이다. 이는 [§§벡터다발의 zero locus](#벡터다발의-zero-locus){: data-lid="xf6gi" }의 구성을 $\mathfrak{M}$ 위에서 상대적으로 한 것이다.

[명제 15](#prop15){: data-lid="nny9k" }의 triangle은 각 점에서 $Z$와 $M$의 tangent space와 obstruction space를 이어 준다. 점 $z\in Z$에서의 derived fiber를 $(\cdot)\vert_z$로 적으면, 위 triangle의 dual $V\vert_Z[-1]\rightarrow(E_Z^\bullet)^\vee\rightarrow i^\ast(E^\bullet)^\vee\rightarrow V\vert_Z$의 derived fiber의 cohomology에서 long exact sequence

$$0\rightarrow h^0((E_Z^\bullet)^\vee\vert_z)\rightarrow h^0((E^\bullet)^\vee\vert_z)\xrightarrow{\dd{s}}V_z\rightarrow h^1((E_Z^\bullet)^\vee\vert_z)\rightarrow h^1((E^\bullet)^\vee\vert_z)\rightarrow0$$

을 얻는다. $(E_Z^\bullet)^\vee\vert_z$와 $(E^\bullet)^\vee\vert_z$의 $h^0$과 $h^1$은 각각 $z$에서 $Z$와 $M$의 relative tangent space와 obstruction space이고, 가운데 map은 relative tangent 방향에 대한 $s$의 미분이다. [§§벡터다발의 zero locus](#벡터다발의-zero-locus){: data-lid="6eerh" }에서 $\ker(\dd{s})$와 $\coker(\dd{s})$로 적은 것에 ambient의 obstruction $h^1((E^\bullet)^\vee\vert_z)$이 더해진 꼴이다. 따라서 $M$이 $z$에서 $\mathfrak{M}$ 상대로 unobstructed이고 $\dd{s}$가 $z$에서 surjective이면 $Z$도 $z$에서 $\mathfrak{M}$ 상대로 unobstructed이다. 이때 $h^1((E_Z^\bullet)^\vee)$은 amplitude $[0,1]$인 perfect complex의 top cohomology이므로 Nakayama lemma에 의해 $z$의 근방에서 $0$이고, 그 근방에서 $Z\rightarrow\mathfrak{M}$은 smooth하다. ([BF, Proposition 7.3]) 같은 논증으로 $M$도 $z$ 근방에서 $\mathfrak{M}$ 위에서 smooth하고, $\dd{s}$가 surjective이므로 $Z$는 그 근방에서 $M$의 codimension $r$ smooth substack이다. 반대로 $\dd{s}$가 surjective가 아니면 그 cokernel이 그대로 $Z$의 obstruction으로 남는다.

같은 논증을 뒤집으면, $Z$가 smooth하지 않은 점에서는 obstruction이 $0$일 수 없다. 만일 점 $z$에서 relative obstruction이 $0$이라면 위와 같이 그 근방에서 $Z\rightarrow\mathfrak{M}$이 smooth하고, $\mathfrak{M}$이 smooth하므로 $Z$도 smooth해야 하기 때문이다. Absolute perfect obstruction theory에 대해서도 같다. 이는 perfect obstruction theory의 선택과도 무관하다. 어떤 absolute perfect obstruction theory의 obstruction space도 intrinsic obstruction space $\Ext^1(\LL_Z\vert_z,\mathbb{C})$를 포함하고 ([KKP, §3]), 이 공간은 $Z$가 $z$에서 smooth하지 않으면 $0$이 아니기 때문이다. 특히 $Z$가 어떤 irreducible component $D$의 generic point에서 non-reduced이면, smooth locus는 open이고 smooth한 곳은 reduced이므로 $Z$는 $D$의 어느 점에서도 smooth하지 않고, 따라서 $D$의 모든 점에서 relative하게도 absolute하게도 obstructed이다. 이때 obstructed인 것은 scheme으로서의 $Z$이고, reduced structure를 준 $D$ 자체는 generic point에서 smooth하다.

::: 예시 16
$Y\subset\mathbb{P}^4$를 smooth quintic threefold, 곧 $\mathcal{O}(5)$의 section $s$의 zero locus라 하고 $Y$ 위의 직선을 세자. $\mathcal{O}(5)$는 globally generated이므로 genus $0$ stable map $f:C\rightarrow\mathbb{P}^4$로 당긴 line bundle은 모든 component에서 음이 아닌 degree를 갖고, 따라서 $H^1(C,f^\ast\mathcal{O}(5))=0$이다. 그럼 cohomology와 base change에 의해 $\mathcal{V}_d=\pi_\ast\mu^\ast\mathcal{O}(5)$는 $\overline{\mathcal{M}}_{0,0}(\mathbb{P}^4,d)$ 위의 rank $5d+1$ vector bundle이고, $s$는 그 section $\widetilde{s}([f])=f^\ast s$를 준다. Stable map이 $Y$로 들어간다는 것은 $f^\ast s=0$이라는 것이므로 $Z(\widetilde{s})$는 $Y$로 가는 stable map들의 moduli이고, Lefschetz hyperplane theorem에 의해 $H_2(Y)\rightarrow H_2(\mathbb{P}^4)$가 isomorphism이므로 이는 $\overline{\mathcal{M}}_{0,0}(Y,d)$ 하나이다.

[명제 15](#prop15){: data-lid="5llwo" }의 compatibility는 normal bundle sequence $0\rightarrow T_Y\rightarrow T_{\mathbb{P}^4}\vert_Y\rightarrow\mathcal{O}(5)\vert_Y\rightarrow0$에서 온다. 이를 universal map으로 당기고 $R\pi_\ast$를 취한 뒤 dual을 취하면 $\overline{\mathcal{M}}_{0,0}(Y,d)$ 위의 triangle

$$i^\ast(R\pi_\ast\mu^\ast T_{\mathbb{P}^4})^\vee\rightarrow(R\pi_\ast\mu^\ast T_Y)^\vee\rightarrow i^\ast\mathcal{V}_d^\vee[1]\rightarrow i^\ast(R\pi_\ast\mu^\ast T_{\mathbb{P}^4})^\vee[1]$$

을 얻고, 처음 두 항은 [명제 13](#prop13){: data-lid="65y3n" }의 relative perfect obstruction theory들이다. [KKP]는 이 triangle이 cotangent complex의 triangle과 compatible하다고 적고 여기에 [명제 15](#prop15){: data-lid="ycr9q" }을 적용한다. $\mathbb{P}^4$는 convex이므로 [예시 14](#ex14){: data-lid="4mh66" }에 의해 ambient의 virtual class는 fundamental class이고, 따라서

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
