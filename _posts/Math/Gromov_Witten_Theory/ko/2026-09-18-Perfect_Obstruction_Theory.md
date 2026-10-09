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

대수기하학에서 공간의 국소적인 기하학은 점에서의 tangent space와, 그 안에서 공간을 잘라내는 방정식들의 관계로 이해된다. 일반적인 smooth point에서는 점 근방이 tangent space와 같은 차원을 갖지만, singular point에서는 tangent space, 즉 $1$차 미분이 공간을 온전히 복원하지 못해서 그 tangent space가 실제 공간보다 더 큰 공간의 역할을 한다. 때문에 이러한 곳에서는 $2$차 이상의 고차항이 tangent space를 잘라내서 원래의 공간을 결정하도록 해야 한다. 이러한 고차 방정식들이 $r$개의 독립적인 구속조건으로 작동한다면 기대 차원은 tangent space의 차원보다 $r$만큼 작지만, 방정식들이 서로 종속이 되거나 무력화되면 차원을 기대만큼 깎지 못해 실제 차원이 이 기대치를 초과할 수 있다.

예를 들어, $\mathbb{A}^3$ 안에서 두 방정식 $\x\y=0$, $\x\z=0$으로 정의되는 공간 $X=Z(\x\y,\x\z)$를 생각하자. 이 방정식은 두 개의 방정식으로 정의되므로, 우리가 기대하는 차원은 $3-2=1$이지만, 이를 실제로 그려보면 $\x=0$을 만족하는 곳, 즉 $\y\z$-평면과, $\y,\z$가 동시에 $0$이 되는 곳, 즉 $\x$축의 합집합이 된다. 이 그림에서 $\x$축 부분은 세 미지수에서 두 방정식이 온전히 작동하여 차원을 깎아내리므로 $1$차원의 공간이 되지만, $\y\z$-평면에서는 이 방정식이 차원을 하나밖에 깎지 못해 실제 차원이 기대 차원보다 하나 부풀어오른다. 뿐만 아니라 이 두 성분이 만나는 원점에서는 방정식의 $1$차 도함수가 모두 $0$이 되므로, tangent space의 차원마저 $3$차원이 된다. 

[§안정사상들의 모듈라이 공간, ⁋명제 4](/ko/math/gromov-witten_theory/moduli_of_stable_maps#prop4){: data-lid="31q1v" }에서 우리가 계산한 virtual dimension은 바로 이런 직관을 담아내던, <em-ko>올바른</em-ko> 차원이었다. Stable map moduli에서 tangent space는 stable map이 움직이는 방향, 즉 stable map의 deformation space가 되며 $T^2$가 이를 잘라내는 방정식의 역할을 하게 된다는 것이 정의

$$\vdim=\dim T^1(C,p_\bullet,\mu)-\dim T^2(C,p_\bullet,\mu)$$

의 의미였다. 해당 명제에서 우리는 이 virtual dimension이 stable map의 선택에 의존하지 않고 모든 점에서 $g,n,\beta$만으로 결정되는 것은 이미 보았지만, 위에서 살펴본 것과 같은 이유로 이것이 실제 차원이 된다는 보장은 없다. 즉 $\dim T^1$과 $\dim T^2$이 각각 바뀌면서 그 차이만 맞춰주게 되며, 이 과정에서는 당연히 위와 같은 일이 자주 일어나게 된다.

한편 moduli space의 실제 차원 $\dim\overline{\mathcal{M}}_{g,n}(X,\beta)$을 한 점에서의 국소 차원으로 읽으면, 이는 그 점에서의 tangent space의 차원 $\dim T^1$보다 작거나 같으며, 이러한 결손을 잡아내는 보정항으로 사용하고자 한 것이 $\dim T^2$를 도입한 것이기는 하지만 이것이 실제 결손을 측정하는 것은 아니었다. 실제로 차이가 나는 부분은

$$\dim\overline{\mathcal{M}}_{g,n}(X,\beta)-\vdim=\dim T^2-\bigl(\dim T^1-\dim\overline{\mathcal{M}}_{g,n}(X,\beta)\bigr)$$

으로 쓸 수 있으며, 이때 $\dim T^1-\dim\overline{\mathcal{M}}_{g,n}(X,\beta)$은 항상 음이 아니며, 이 수가 $\dim T^2$의 차원을 죽여준다면 virtual dimension과 실제 차원이 같아지게 된다. 이러한 상황에서, 만일 $T^2$의 차원이 $0$이라면 $\dim T^1-\dim\overline{\mathcal{M}}_{g,n}(X,\beta)$의 값이 강제로 $0$이 되고 위의 결손 또한 $0$이 되므로 moduli space는 smooth가 된다. 그러나 $T^2$가 살아있어도 $\dim T^1-\dim\overline{\mathcal{M}}_{g,n}(X,\beta)$가 이를 완벽하게 상쇄한다면 역시 두 차원이 맞게 된다. 

이를 실제 moduli space에서 보기 위해 $X$를 smooth projective variety, $\dim X=d$라 하고 $\beta=0$, $g=1$, $n\geq1$을 택하자. Class $0$의 stable map $\mu:C\rightarrow X$는 각 component를 한 점으로 보내는 constant map이고, stability 때문에 domain은 stable curve여야 하므로 남는 자료는 $n$-pointed genus $1$ stable curve와, 이 curve가 어디로 옮겨지는지를 담는 함숫값 $\mu(C)\in X$뿐이다. 따라서

$$\overline{\mathcal{M}}_{1,n}(X,0)\cong\overline{\mathcal{M}}_{1,n}\times X$$

이고 그 차원은 $(3\cdot1-3+n)+d=n+d$이다. 이는 위의 virtual dimension 공식이 주는 $\vdim=0+(d-3)(1-1)+n=n$와는 다른 것으로, 우리 주장은 이것이 실제로 위에서 살펴본 계산에서 나온다는 것이다. Constant map에서는 $\mu^\ast T_X=\mathcal{O}_C\otimes T_{X,\mu(C)}$가 trivial bundle이므로

$$H^1(C,\mu^\ast T_X)=H^1(C,\mathcal{O}_C)\otimes T_{X,\mu(C)}$$

이고, $g=1$에서 $\dim H^1(C,\mathcal{O}_C)=1$이므로 이 공간은 $d$차원이다. 나아가 constant map에서는 $\dd{\mu}=0$이므로 $T^2\cong H^1(C,\mu^\ast T_X)$이고, moduli 자체가 smooth하므로 결손항 $\dim T^1-\dim\overline{\mathcal{M}}_{1,n}(X,0)$도 $0$이다. 따라서 초과분 $\dim\overline{\mathcal{M}}_{1,n}(X,0)-\vdim$은 결손항의 상쇄 없이 정확히 $\dim T^2=d$로 나타난 것이다.

우리 글의 목표는 이렇게 차원이 맞지 않더라도, 적분을 가능하게 해 주는 기대 차원의 class인 *virtual fundamental class<sub>가상 기본류</sub>*

$$[\overline{\mathcal{M}}_{g,n}(X,\beta)]^\vir\in A_{\vdim}(\overline{\mathcal{M}}_{g,n}(X,\beta))$$

를 구성하는 것으로, 이는 [BF]를 따라 *perfect obstruction theory*라 불리는 자료에서 얻을 수 있다.

## 벡터다발의 zero locus

이제 우리는 위의 언어를 더 기하학적인 방식으로 올린다. 이를 위해 ambient space 역할을 할 $T^1$은 smooth variety $X$로, $T^2$는 그 위의 vector bundle $E$로 올리며, 이 때 obstruction의 방정식은 이것의 section $s\in \Gamma(X, E)$가 되어, 우리의 moduli space는 이러한 smooth variety $X$ 위에 section들의 locus가 정의하는 common locus가 된다. 

따라서 우리는 이러한 상황을 간략하게 복습한다. Smooth variety $X$ 위에 rank $r$의 vector bundle $E$와 section $s\in\Gamma(X,E)$가 주어져 있다 하고

$$Z(s)=\{x\in X\mid s(x)=0\}$$

을 그 zero locus라 하자. 만일 $s$가 zero section과 transversal하게 만나면 $Z(s)$는 기대했던 codimension $r$의 smooth subvariety이고 그 fundamental class는 Euler class $e(E)\cap[X]$와 일치한다. 만일 section $s$가 transversal하게 만나지 않아 $Z(s)$의 codimension이 $r$보다 작다면 그 fundamental class $[Z(s)]$는 기대 차원의 class가 아니지만, 그럼에도 불구하고 이 모델에서는 $X$에서의 class $e(E)\cap[X]$가 존재하며, 우리는 이를 Gysin map을 통해 $Z(s)$ 위의 cycle로 가져올 수 있다. Normal cone $C_{Z(s)/X}$는 $E\vert_{Z(s)}$의 closed subcone으로 자연스럽게 포함되므로, zero section $0_E: Z(s)\hookrightarrow E\vert_{Z(s)}$에 대한 Gysin map $0_E^!$를 cone에 취하여 $Z(s)$ 위의 올바른 기대 차원 $\dim X-r$의 class

$$e(E,s)=0_E^![C_{Z(s)/X}]\in A_{\dim X-r}(Z(s))$$

를 정의할 수 있으며 이를 *localized Euler class*라 부른다. 직관적으로 이는 non-transversal section $s$를 올바르게 흔들어줬으면 나왔을 class를 실제로 흔들지 않고도 대수적으로 적어 둔 것으로 이해할 수 있다.

::: 예시 1
$X=\mathbb{P}^2$, $E=\mathcal{O}(1)^{\oplus2}$를 보자. 그럼 section $s=(\ell_1,\ell_2)$가 두 일차식으로 주어지므로, 위의 그림에서 $Z(s)$는 기대차원이 $0$이 된다. 실제로 이는 두 직선의 교점인 한 점이고, 그 class의 degree는

$$\int_{\mathbb{P}^2}e(E)=\int_{\mathbb{P}^2}c_1(\mathcal{O}(1))^2=1$$

이다. 그러나 non-transversal section, 가령 극단적으로 $s\equiv0$을 택하면 $Z(s)=\mathbb{P}^2$ 전체가 되어 실제 차원이 기대 차원을 $2$만큼 초과한다. 그럼에도 localized Euler class를 $X$로 보낸 class는 section이 아니라 bundle만으로 결정되며,

$$e(E)\cap[\mathbb{P}^2]=c_2(\mathcal{O}(1)^{\oplus2})\cap[\mathbb{P}^2]$$

로 여전히 degree $1$의 point class를 준다. ([\[대수다양체\] §교차곱, ⁋예시 11](/ko/math/algebraic_varieties/intersection_product#ex11){: data-lid="9kgj4" })
:::

우리는 deformation space $T^1$과 obstruction space $T^2$을 담기 위해 이와 같이 smooth variety $X$와 vector bundle $E$를 만들었으며, 이 섹션에서 우리 목표는 이를 엄밀하게 만드는 것이다. 고정된 $x\in X$에 대하여, 이를 흔드는 모든 방향이 담겨있는 벡터공간이 $X$의 tangent space $T_{X,x}$이며, 각 점의 fiber $E_x$가 obstruction space가 된다. 

한편 $Z(s)$의 한 점 $x$가 주어졌을 때, 이 점을 흔들었을 때도 여전히 $Z(s)$ 안에 머물러야 한다는 조건이 바로 $Z(s)$의 deformation 방향을 결정한다. 즉 tangent vector $v\in T_{X,x}$ 방향으로의 무한소 이동 $x+\epsilon v$에 대하여

$$s(x+\epsilon v)=s(x)+\epsilon\dd{s}(v)=\epsilon\dd{s}(v)$$

이므로, 이 일차 변화율 $\dd{s}(v)=0$ 조건이 만족되어야 그 결과가 $Z(s)$ 안에 머무를 수 있다. 따라서 $\dd{s}$의 kernel인 $\ker(\dd{s})$가 $Z(s)$의 실제 tangent space이자 deformation 방향을 이루며, 반대로 $E_x$ 안에서 $\dd{s}$의 image가 채우지 못한 나머지 방향들, 곧 cokernel $\coker(\dd{s})$는 section을 $0$으로 유지하도록 통제할 수 없는 방향들이며, 이것이 바로 $Z(s)$의 실제 obstruction space가 된다.

이를 요약하면, $Z(s)$의 국소 deformation과 obstruction 자료는 그 미분 $\dd{s}$가 tangent space $T^1$과 obstruction $T^2$를 이어 주는 tangent 방향의 complex

$$\Bigl[\at{0}{T_X\vert_{Z(s)}}\xrightarrow{\ \dd{s}\ }\at{1}{E\vert_{Z(s)}}\Bigr]$$

에 온전히 담겨 있으며, 보편적으로 대수기하학에서 우리는 cotangent 방향을 살펴보므로 이 complex를 dualize하여 degree $-1$과 $0$에 놓이는 complex로 적으면

$$E^\bullet=\Bigl[\at{-1}{E^\vee\vert_{Z(s)}}\xrightarrow{\ (\dd{s})^\vee\ }\at{0}{\Omega_X\vert_{Z(s)}}\Bigr]$$

을 얻는다. 이제 이 complex에 $R\Hom(-,\mathcal{O}_{Z(s)})$을 적용하여 원래의 tangent 방향을 복원하면, $0$차 cohomology와 $1$차 cohomology

$$h^0((E^\bullet)^\vee)=\ker(\dd{s}),\qquad h^1((E^\bullet)^\vee)=\coker(T_X\vert_{Z(s)}\rightarrow E\vert_{Z(s)})$$

가 실제 tangent space와 obstruction space를 준다. 

핵심적인 관찰은, 여기서 [예시 1](#ex1){: data-lid="fkmo8" }처럼 tangent space가 기대보다 부풀더라도 obstruction 역시 같은 크기로 늘어나므로, 둘의 차이

$$\dim h^0((E^\bullet)^\vee)-\dim h^1((E^\bullet)^\vee)=\dim X-\rank E$$

는 항상 virtual dimension $\vdim$으로 보존된다는 것이다. 즉, 실제 moduli space가 얼마나 나쁘게 행동하든, 위에서 정의한 Gysin map은 항상 정확히 $\dim X-\rank E$ 차원, 즉 올바른 차원의 virtual class를 뽑아주게 된다. 

## Perfect obstruction theory

이제 위의 논의를 어떻게 적용해야 하는지는 명확하다. 즉 일반적인 stack $M$은 cotangent complex $\LL_M$을 가지며, 우리는 이 중 deformation과 obstruction이 잡히는 truncation $\tau_{\geq -1}\LL_M$을 보면 된다. ([\[스킴\] §변형이론과 여접 복합체, §§변형의 장애와 고차 변형이론](/ko/math/scheme_theory/deformation_theory#변형의-장애와-고차-변형이론){: data-lid="0fpnl" }) 이제 만일 étale-local하게 $M$이 smooth variety $X$ 안의 closed subscheme으로 표현되고, 그 ideal sheaf가 $\mathcal{I}$라 하면 이 truncation은 다음의 꼴

$$\tau_{\geq-1}\LL_M=\Bigl[\at{-1}{\mathcal{I}/\mathcal{I}^2}\xrightarrow{\ \dd{\ }}\at{0}{\Omega_X\vert_M}\Bigr]$$

이 된다. 문제는 일반적인 $M$에서 $\mathcal{I}/\mathcal{I}^2$은 vector bundle이 아니라는 것으로, $\tau_{\geq-1}\LL_M$ 자체만으로는 zero section이나 Gysin map을 정의할 수 없다. 때문에 우리는 이 정보를 모두 담을 수 있는 실제 vector bundle들의 two-term complex를 생각해야 하며, 이것이 바로 다음의 정의이다. 

::: 정의 2 (Behrend–Fantechi)
$M$을 Deligne–Mumford stack이라 하자. $M$ 위의 *perfect obstruction theory<sub>완전 장애 이론</sub>*란 국소적으로 vector bundle 두 항의 complex $[E^{-1}\rightarrow E^0]$과 quasi-isomorphic한 complex $E^\bullet$과 morphism

$$\phi:E^\bullet\longrightarrow\tau_{\geq-1}\LL_M$$

의 쌍으로서, $h^0(\phi)$가 isomorphism이고 $h^{-1}(\phi)$가 surjection인 것을 말한다.
:::

이 정의에서, 우선 $h^0(\phi)$가 isomorphism이라는 것은 $E^\bullet$의 $0$차 항이 $M$의 deformation을 정확히 재현한다는 뜻이다. 수정이 필요했던 부분은 원래 $\mathcal{I}/\mathcal{I}^2$ 쪽이 들어있던 $-1$항으로, 여기에서 $h^{-1}(\phi)$가 surjection이라는 것은 $E^\bullet$의 $-1$차 항이 $M$의 obstruction을 <em-ko>빠짐없이</em-ko> 지배한다는 뜻이다. 즉, $E^\bullet$ 쪽에 실제보다 많은 obstruction이 있는 것은 허용되지만 하나라도 빠뜨리는 것은 허용되지 않으며, 이 구조가 기대 차원의 class를 골라낼 여유를 준다. 

위에서 살펴본 $Z(s)\hookrightarrow X$에 의해 만들어진 complex

$$E^\bullet=\Bigl[\at{-1}{E^\vee\vert_{Z(s)}}\xrightarrow{\ (\dd{s})^\vee\ }\at{0}{\Omega_X\vert_{Z(s)}}\Bigr]$$

에서 truncation 

$$\tau_{\geq-1}\LL_{Z(s)}=[\at{-1}{\mathcal{I}/\mathcal{I}^2}\rightarrow\at{0}{\Omega_X\vert_{Z(s)}}]$$

으로 가는 morphism $\phi:E^\bullet\rightarrow\tau_{\geq-1}\LL_{Z(s)}$는 다음의 diagram

{% diagram Math/Gromov_Witten_Theory/Perfect_Obstruction_Theory-1.svg width="10.88em" alt="morphism from the local complex to the truncated cotangent complex" %}

으로 주어지는 것이다. 특히 degree $-1$에서는 section $s$와의 pairing $s^\vee:E^\vee\rightarrow\mathcal{O}_X$를 $\mathcal{I}/\mathcal{I}^2$으로 내린 것으로 정의되는 것이며, 이는 $s^\vee$의 image가 정확히 $\mathcal{I}$이므로 surjection이 되기 때문에 이 complex는 실제로 perfect obstruction theory가 된다. 

이제 이렇게 주어진 perfect obstruction theory로부터 virtual fundamental class를 정의하자. 통상적인 intersection theory에서 closed embedding $Z(s)\hookrightarrow X$가 주어졌을 때, deformation to the normal cone은 $X$를 normal cone $C_{Z(s)/X}$로 변형하여 intersection product와 Gysin map을 정의할 수 있게 해 준다. ([\[대수다양체\] §교차곱, ⁋명제 9](/ko/math/algebraic_varieties/intersection_product#prop9){: data-lid="7fg7b" }) [BF]의 핵심적인 결과는 이것이 명시적인 embedding이 주어지지 않은 상태에서 intrinsic한 방식으로 얻을 수 있는 *intrinsic normal cone* $\mathfrak{c}_M=[C_{Z(s)/X}/T_X\vert_{Z(s)}]$의 구성으로, 위에서의 perfect obstruction theory $\phi$는 이를 vector bundle stack $\mathfrak{E}=h^1/h^0((E^\bullet)^\vee)$ 안으로의 closed embedding

$$\mathfrak{c}_M\hookrightarrow\mathfrak{E}=[E_1/E_0]$$

으로 실현해 준다. 여기서 $E_i=(E^{-i})^\vee$이다. 덕분에 우리는 일반적인 intersection theory와 마찬가지로 $\mathfrak{E}$의 zero section에 대한 Gysin pullback을 사용해 virtual class

$$[M]^\vir=0^!_{E^\bullet}[\mathfrak{c}_M]\in A_{\rank E^\bullet}(M)$$

를 정의할 수 있게 된다. 그 성질은 다음과 같다.

::: 명제 3
Deligne–Mumford stack $M$ 위의 perfect obstruction theory $\phi:E^\bullet\rightarrow\tau_{\geq-1}\LL_M$에 대하여, virtual class $[M]^\vir=0^!_{E^\bullet}[\mathfrak{c}_M]$은 다음을 만족한다.

1. $[M]^\vir$은 virtual dimension $\vdim=\rank E^\bullet=\rank E^0-\rank E^{-1}$의 cycle이다.
2. $M$이 flat family의 fiber로 주어지고 $\phi$가 family 위의 perfect obstruction theory와 compatible하면, $[M]^\vir$은 family의 virtual class를 fiber로 Gysin pullback한 것이다. 특히 $[M]^\vir$은 family 안에서의 deformation에 대해 불변이다.
3. $h^1((E^\bullet)^\vee)=0$이면 $M$은 smooth하고 $[M]^\vir=[M]$은 보통의 fundamental class이다.
:::

## 안정사상들의 가상 기본류

이제 stable map들의 moduli stack $M=\overline{\mathcal{M}}_{g,n}(X,\beta)$ 위에 perfect obstruction theory를 구성하자. 이를 위해 우리는 target $X$의 tangent space $T_X$를

$$\pi:\mathcal{C}\rightarrow M,\qquad\mu:\mathcal{C}\rightarrow X$$

를 사용하여 가지고 온다. 즉 $T_X$를 $\mu$를 사용하여 pullback해온 후, 이를 다시 $R\pi_\ast$를 사용하여 밀어내린 $R\pi_\ast\mu^\ast T_X$를 사용하는 것이다. 이 때 곡선의 차원이 $1$이므로 higher direct image $R^i\pi_\ast$는 $i=0,1$에서만 살아남게 되며, 따라서 이 complex는 정확히 degree $0$과 $1$에 놓이는 two-term complex가 되고 각 점에서 $H^0(C,\mu^\ast T_X)$와 $H^1(C,\mu^\ast T_X)$를 그 cohomology로 복원한다. 

따라서 위에서 얻은 $R\pi_\ast\mu^\ast T_X$의 dual $E^\bullet=(R\pi_\ast\mu^\ast T_X)^\vee$는 $[-1,0]$ amplitude의 complex로, 우리가 원하는 perfect obstruction theory의 후보가 된다. 다만 이는 domain curve $(C,p_\bullet)$을 고정한 채 map $\mu$만을 변형하는 자료이므로, prestable curve들의 moduli stack $\mathfrak{M}_{g,n}$으로 가는 morphism $q:M\rightarrow\mathfrak{M}_{g,n}$에 대한 relative perfect obstruction theory를 이룬다. 여기서 우리를 도와주는 것은 base stack $\mathfrak{M}_{g,n}$이 smooth하다는 것으로, 직관적으로 이는 node를 펼 때는 어떠한 obstruction도 없기 때문이다. 즉 $\mathfrak{M}_{g,n}$에는 perfect obstruction theory 없이도 이미 (진짜) fundamental class가 있고, 이를 relative perfect obstruction theory로 가져올 수 있다. 

::: 명제 4 (Behrend)
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

::: 예시 5
$X$가 convex인 경우 모든 genus $0$ stable map에서 $H^1(C,\mu^\ast T_X)=0$이므로 ([§안정사상들의 모듈라이 공간, ⁋명제 5](/ko/math/gromov-witten_theory/moduli_of_stable_maps#prop5){: data-lid="c4h5h" }) obstruction space가 $h^1((E^\bullet)^\vee)=R^1\pi_\ast\mu^\ast T_X=0$이다. 이제 위에서 살펴본 것과 마찬가지 이유로, $\mathfrak{M}_{0,n}$의 smoothness에 의해 absolute obstruction 또한 $h^1(((E')^\bullet)^\vee)=0$이 되므로, [명제 3](#prop3){: data-lid="vrq63" }의 (3)에 의해

$$[\overline{\mathcal{M}}_{0,n}(X,\beta)]^\vir=[\overline{\mathcal{M}}_{0,n}(X,\beta)]$$

이 되어 virtual class가 보통의 fundamental class와 일치한다. $X=\mathbb{P}^r$와 Grassmannian, 일반적인 flag variety $G/P$가 모두 이 경우에 해당하며, 여기에서의 genus $0$ curve counting은 smooth moduli의 (진짜) fundamental class에 대한 적분과 동일하게 나오며, 이것이 이전 글의 계산을 정당화한다. 
:::

[§그로모프-위튼 불변량, ⁋정의 1](/ko/math/gromov-witten_theory/gromov-witten_invariants#def1){: data-lid="gt4df" }에서 우리는 fundamental class $[\overline{\mathcal{M}}_{0,n}(X,\beta)]$가 존재하는 경우에 대해서만 정의하였으나, 이 fundamental class만 virtual fundamental class로 바꿔주면 convex 가정 없이도 임의의 smooth projective target $X$에 대한 genus $0$ Gromov-Witten invariant를 정의할 수 있으며, convex 가정 하에서 이 두 정의가 같은 것은 위의 [예시 5](#ex5){: data-lid="bt6x3" }에 의해 자명하다. 그럼 이 정의 하에서, virtual class가 forgetful morphism 및 gluing morphism에 대해 잘 행동하는 것을 확인할 수 있으므로 [§그로모프-위튼 불변량, §§그로모프-위튼 불변량의 공리들](/ko/math/gromov-witten_theory/gromov-witten_invariants#그로모프-위튼-불변량의-공리들){: data-lid="huqbc" }의 string·divisor·splitting 공리와 WDVV 관계도 해당 적분들을 virtual class에 대한 적분으로 해석하면 그대로 성립한다.

::: 예시 6
반대편 극단으로 도입에서 본 constant map의 moduli $\overline{\mathcal{M}}_{1,n}(X,0)\cong\overline{\mathcal{M}}_{1,n}\times X$을 살펴보자. 여기서는 obstruction이 통째로 살아있다는 것이 우리의 도입부의 주장이었으므로, 이제 엄밀한 언어로 이를 다시 계산하자. 

두 projection을 각각 $p_1:\overline{\mathcal{M}}_{1,n}\times X\rightarrow\overline{\mathcal{M}}_{1,n}$, $p_2:\overline{\mathcal{M}}_{1,n}\times X\rightarrow X$라 하자. Constant map에서는 곡선 위의 모든 점이 $X$의 같은 점으로 대응되므로, universal evaluation map $\mu:\mathcal{C}\rightarrow X$는 projection $p_2$와 universal curve $\pi:\mathcal{C}\rightarrow M$의 합성

$$\mu=p_2\circ\pi$$

로 분해된다. 따라서 target tangent bundle의 pullback은 $\mu^\ast T_X\cong\pi^\ast p_2^\ast T_X$가 되고, 이를 $M$ 위로 밀어내리면 projection formula에 의해

$$R^1\pi_\ast\mu^\ast T_X\cong(R^1\pi_\ast\mathcal{O}_{\mathcal{C}})\otimes p_2^\ast T_X$$

를 얻는다. 여기서 $\overline{\mathcal{M}}_{1,n}$ 위의 genus $1$ universal curve에 Serre duality $H^1(C,\mathcal{O}_C)\cong H^0(C,\omega_C)^\vee$를 family로 적용하면 $R^1\pi_\ast\mathcal{O}_{\mathcal{C}}$는 rank $1$짜리 bundle $p_1^\ast(\pi_\ast\omega_{\mathcal{C}})^\vee$와 같아진다. 따라서 obstruction bundle은

$$h^1(((E')^\bullet)^\vee)\cong R^1\pi_\ast\mu^\ast T_X\cong p_1^\ast(\pi_\ast\omega_{\mathcal{C}})^\vee\otimes p_2^\ast T_X$$

가 된다. 실제로 각 점 $((C,p_\bullet),x)$에서 상수사상 $\mu$에 의한 pullback은 $\mu^\ast T_X\cong\mathcal{O}_C\otimes T_x X$로 자명해지므로, 이 점에서의 obstruction 공간은

$$H^1(C,\mu^\ast T_X)\cong H^1(C,\mathcal{O}_C)\otimes T_x X$$

가 된다. $C$가 genus $1$ 곡선이므로 $\dim H^1(C,\mathcal{O}_C)=1$이고, 따라서 이 bundle의 rank는 $\dim X=d$가 되어 moduli의 실제 차원 $\dim(\overline{\mathcal{M}}_{1,n}\times X)=n+d$와 가상 차원 $\vdim=n$ 사이의 초과 차원 $d$와 정확히 일치한다. 한편 prestable curve들의 moduli stack $\mathfrak{M}_{1,n}$은 smooth이므로 open condition인 stability를 부과한 (open) substack $\overline{\mathcal{M}}_{1,n}$ 역시 smooth하며, 여기에 target $X$의 smoothness까지 사용하면 moduli stack $\overline{\mathcal{M}}_{1,n}\times X$ 전체가 smooth가 된다. 이제 이 위에 정의된 obstruction $h^1(((E')^\bullet)^\vee)$ 또한 vector bundle이므로, [예시 1](#ex1){: data-lid="1f2tf" }의 $s\equiv0$인 local model이 그대로 적용되어

$$[\overline{\mathcal{M}}_{1,n}(X,0)]^\vir=e(p_1^\ast(\pi_\ast\omega_{\mathcal{C}})^\vee\otimes p_2^\ast T_X)\cap[\overline{\mathcal{M}}_{1,n}\times X]$$

가 된다. $(n+d)$차원 공간 위에서 Euler class와의 cap product로 차원 $n$의 class를 복원한 것으로, [예시 1](#ex1){: data-lid="m97nc" }의 $s\equiv0$인 상황을 stable map moduli에서 재연한 셈이다.
:::

## Zero locus의 가상 기본류

[§§벡터다발의 zero locus](#벡터다발의-zero-locus){: data-lid="1un49" }의 국소 모형에서 ambient는 smooth variety였다. 그러나 이 모형이 실제로 쓰이는 상황에서는 ambient 자신이 obstruction을 갖는 moduli인 경우가 많다. 가령 smooth projective variety $P$ 안의 smooth subvariety $Y$가 vector bundle $V$의 section $s$의 zero locus로 주어지면, $Y$로 가는 stable map은 $P$로 가는 stable map $f$ 가운데 $f^\ast s=0$인 것이다. 모든 genus $0$ stable map에 대해 $H^1(C,f^\ast V)=0$이면 $\pi_\ast\mu^\ast V$는 $P$의 genus $0$ moduli 위의 vector bundle이고, $Y$의 moduli는 그 section $f\mapsto f^\ast s$의 zero locus가 된다. 두 moduli는 모두 [명제 4](#prop4){: data-lid="3nmml" }의 virtual class를 가지므로, 자연스러운 질문은 [예시 1](#ex1){: data-lid="fn474" }에서처럼 둘이 Euler class로 이어지는지의 여부일 것이다. Stable map의 moduli는 $\mathfrak{M}_{g,n}$에 상대적인 perfect obstruction theory를 가지므로 처음부터 상대적인 형태로 적는다.

::: 명제 7 (Kim–Kresch–Pantev)
$\mathfrak{M}$을 locally finite type이고 pure dimensional인 smooth Artin stack, $q:M\rightarrow\mathfrak{M}$을 finite type Deligne–Mumford stack $M$에서의 morphism, $\phi:E^\bullet\rightarrow\LL_{M/\mathfrak{M}}$을 relative perfect obstruction theory라 하자. $M$ 위의 rank $r$ vector bundle $V$와 section $s$에 대하여 $i:Z=Z(s)\hookrightarrow M$을 그 zero locus라 하고, $Z$ 위의 relative perfect obstruction theory $\phi_Z:E_Z^\bullet\rightarrow\LL_{Z/\mathfrak{M}}$이 distinguished triangle

$$i^\ast E^\bullet\longrightarrow E_Z^\bullet\longrightarrow V^\vee\vert_Z[1]\longrightarrow i^\ast E^\bullet[1]$$

에 들어가며, 이 triangle이 cotangent complex의 triangle $i^\ast\LL_{M/\mathfrak{M}}\rightarrow\LL_{Z/\mathfrak{M}}\rightarrow\LL_{Z/M}\rightarrow i^\ast\LL_{M/\mathfrak{M}}[1]$과 $\phi$, $\phi_Z$, 그리고 $s$가 주는 $V^\vee\vert_Z[1]\rightarrow\LL_{Z/M}$으로 compatible하다고 하자. 그럼

$$[Z]^\vir=0^!_{V,s}[M]^\vir,\qquad i_\ast[Z]^\vir=c_r(V)\cap[M]^\vir$$

이다. 여기서 $0^!_{V,s}$는 zero section의 refined Gysin map을 section $s$를 따라 적용한 것, 곧 [§§벡터다발의 zero locus](#벡터다발의-zero-locus){: data-lid="6g4xw" }에서 localized Euler class를 만든 연산이다.
:::

이는 [KKP, Theorem 1]을 zero section $0_V:M\rightarrow V$에 적용한 것이다. 이 정리는 relative perfect obstruction theory를 갖는 두 stack이 local complete intersection morphism $v$를 따라 cartesian하게 놓이고 두 obstruction theory가 cotangent complex의 triangle과 compatible하면, $v$의 refined Gysin map이 한쪽의 virtual class를 다른 쪽의 virtual class로 보낸다는 것이다. 지금의 경우 cartesian square는 $s$와 $0_V$의 fiber product $Z=M\times_VM$이고, $0_V$의 cotangent complex를 $Z$로 당긴 것이 $V^\vee\vert_Z[1]$이므로 위의 triangle이 정확히 그 compatibility 조건이 된다. [BF, Proposition 7.5]는 global resolution을 가정하고 $v$가 smooth하거나 $v$의 source와 target이 모두 base 위에서 smooth한 경우에 같은 등식을 주는데, zero section에 대해 뒤의 조건은 $M$이 $\mathfrak{M}$ 위에서 smooth하다는 것이다. [KKP, Theorem 1]은 이러한 가정 없이 base의 pure dimensionality와 $v$가 local complete intersection morphism이라는 것만을 요구하며, [KKP]는 이를 [BF, Proposition 7.5]를 강화한 것으로 소개한다. Base의 smoothness는 $\mathfrak{M}$ 상대 perfect obstruction theory로 정의한 virtual class가 [명제 4](#prop4){: data-lid="qmcty" }에서처럼 유도한 absolute perfect obstruction theory의 virtual class와 같다는 데에 쓰인다. ([KKP, Proposition 3]) 둘째 등식은 refined Gysin map에 대한 공식 $i_\ast0^!_{V,s}\gamma=c_r(V)\cap\gamma$를 $\gamma=[M]^\vir$에 적용한 것이고, 이 공식은 [§가상류의 교차이론, ⁋정의 3](/ko/math/gromov-witten_theory/intersection_theory_of_virtual_classes#def3){: data-lid="oggvg" } 뒤에서 다룬다.

명제는 $E_Z^\bullet$을 가정으로 둔다. 일반적인 $(M,E^\bullet)$에서 이러한 $E_Z^\bullet$을 만들려면 $s$가 주는 $V^\vee\vert_Z[1]\rightarrow\LL_{Z/M}$과 cotangent complex의 triangle의 connecting map을 합성한 $V^\vee\vert_Z\rightarrow i^\ast\LL_{M/\mathfrak{M}}$을 $\phi$를 따라 $i^\ast E^\bullet$으로 들어 올려야 하는데, 그 obstruction은 $\phi$의 cone의 hypercohomology에 있어서 local하게만 사라지고 global하게는 자동이 아니다. 그래서 $E_Z^\bullet$은 경우마다 구성하며, 아래 [예시 8](#ex8){: data-lid="zy2k0" }에서는 universal curve 위의 vector bundle의 short exact sequence에 $R\pi_\ast$를 취해 이를 얻는다. 가장 간단한 경우는 $q$가 smooth한 경우이다. 이때는 $E^\bullet=\Omega_{M/\mathfrak{M}}$으로 둘 수 있고,

$$E_Z^\bullet=\Bigl[\at{-1}{V^\vee\vert_Z}\xrightarrow{\ (\dd{s})^\vee\ }\at{0}{\Omega_{M/\mathfrak{M}}\vert_Z}\Bigr]$$

이 $Z$의 relative perfect obstruction theory이다. $\tau_{\geq-1}\LL_{Z/\mathfrak{M}}=[\mathcal{I}/\mathcal{I}^2\rightarrow\Omega_{M/\mathfrak{M}}\vert_Z]$이고 $V^\vee\vert_Z\rightarrow\mathcal{I}/\mathcal{I}^2$이 surjective이므로, $h^0$에서는 isomorphism이고 $h^{-1}$에서는 surjective이다. 위의 triangle은 이 two-term complex의 stupid truncation이 주는 것이다. 이는 [§§벡터다발의 zero locus](#벡터다발의-zero-locus){: data-lid="xf6gi" }의 구성을 $\mathfrak{M}$ 위에서 상대적으로 한 것이다.

[명제 7](#prop7){: data-lid="nny9k" }의 triangle은 각 점에서 $Z$와 $M$의 tangent space와 obstruction space를 이어 준다. 점 $z\in Z$에서의 derived fiber를 $(\cdot)\vert_z$로 적으면, 위 triangle의 dual $V\vert_Z[-1]\rightarrow(E_Z^\bullet)^\vee\rightarrow i^\ast(E^\bullet)^\vee\rightarrow V\vert_Z$의 derived fiber의 cohomology에서 long exact sequence

$$0\rightarrow h^0((E_Z^\bullet)^\vee\vert_z)\rightarrow h^0((E^\bullet)^\vee\vert_z)\xrightarrow{\dd{s}}V_z\rightarrow h^1((E_Z^\bullet)^\vee\vert_z)\rightarrow h^1((E^\bullet)^\vee\vert_z)\rightarrow0$$

을 얻는다. $(E_Z^\bullet)^\vee\vert_z$와 $(E^\bullet)^\vee\vert_z$의 $h^0$과 $h^1$은 각각 $z$에서 $Z$와 $M$의 relative tangent space와 obstruction space이고, 가운데 map은 relative tangent 방향에 대한 $s$의 미분이다. [§§벡터다발의 zero locus](#벡터다발의-zero-locus){: data-lid="6eerh" }에서 $\ker(\dd{s})$와 $\coker(\dd{s})$로 적은 것에 ambient의 obstruction $h^1((E^\bullet)^\vee\vert_z)$이 더해진 꼴이다. 따라서 $M$이 $z$에서 $\mathfrak{M}$ 상대로 unobstructed이고 $\dd{s}$가 $z$에서 surjective이면 $Z$도 $z$에서 $\mathfrak{M}$ 상대로 unobstructed이다. 이때 $h^1((E_Z^\bullet)^\vee)$은 amplitude $[0,1]$인 perfect complex의 top cohomology이므로 Nakayama lemma에 의해 $z$의 근방에서 $0$이고, 그 근방에서 $Z\rightarrow\mathfrak{M}$은 smooth하다. ([BF, Proposition 7.3]) 같은 논증으로 $M$도 $z$ 근방에서 $\mathfrak{M}$ 위에서 smooth하고, $\dd{s}$가 surjective이므로 $Z$는 그 근방에서 $M$의 codimension $r$ smooth substack이다. 반대로 $\dd{s}$가 surjective가 아니면 그 cokernel이 그대로 $Z$의 obstruction으로 남는다.

같은 논증을 뒤집으면, $Z$가 smooth하지 않은 점에서는 obstruction이 $0$일 수 없다. 만일 점 $z$에서 relative obstruction이 $0$이라면 위와 같이 그 근방에서 $Z\rightarrow\mathfrak{M}$이 smooth하고, $\mathfrak{M}$이 smooth하므로 $Z$도 smooth해야 하기 때문이다. Absolute perfect obstruction theory에 대해서도 같다. 이는 perfect obstruction theory의 선택과도 무관하다. 어떤 absolute perfect obstruction theory의 obstruction space도 intrinsic obstruction space $\Ext^1(\LL_Z\vert_z,\mathbb{C})$를 포함하고 ([KKP, §3]), 이 공간은 $Z$가 $z$에서 smooth하지 않으면 $0$이 아니기 때문이다. 특히 $Z$가 어떤 irreducible component $D$의 generic point에서 non-reduced이면, smooth locus는 open이고 smooth한 곳은 reduced이므로 $Z$는 $D$의 어느 점에서도 smooth하지 않고, 따라서 $D$의 모든 점에서 relative하게도 absolute하게도 obstructed이다. 이때 obstructed인 것은 scheme으로서의 $Z$이고, reduced structure를 준 $D$ 자체는 generic point에서 smooth하다.

::: 예시 8
$Y\subset\mathbb{P}^4$를 smooth quintic threefold, 곧 $\mathcal{O}(5)$의 section $s$의 zero locus라 하고 $Y$ 위의 직선을 세자. $\mathcal{O}(5)$는 globally generated이므로 genus $0$ stable map $f:C\rightarrow\mathbb{P}^4$로 당긴 line bundle은 모든 component에서 음이 아닌 degree를 갖고, 따라서 $H^1(C,f^\ast\mathcal{O}(5))=0$이다. 그럼 cohomology와 base change에 의해 $\mathcal{V}_d=\pi_\ast\mu^\ast\mathcal{O}(5)$는 $\overline{\mathcal{M}}_{0,0}(\mathbb{P}^4,d)$ 위의 rank $5d+1$ vector bundle이고, $s$는 그 section $\widetilde{s}([f])=f^\ast s$를 준다. Stable map이 $Y$로 들어간다는 것은 $f^\ast s=0$이라는 것이므로 $Z(\widetilde{s})$는 $Y$로 가는 stable map들의 moduli이고, Lefschetz hyperplane theorem에 의해 $H_2(Y)\rightarrow H_2(\mathbb{P}^4)$가 isomorphism이므로 이는 $\overline{\mathcal{M}}_{0,0}(Y,d)$ 하나이다.

[명제 7](#prop7){: data-lid="5llwo" }의 compatibility는 normal bundle sequence $0\rightarrow T_Y\rightarrow T_{\mathbb{P}^4}\vert_Y\rightarrow\mathcal{O}(5)\vert_Y\rightarrow0$에서 온다. 이를 universal map으로 당기고 $R\pi_\ast$를 취한 뒤 dual을 취하면 $\overline{\mathcal{M}}_{0,0}(Y,d)$ 위의 triangle

$$i^\ast(R\pi_\ast\mu^\ast T_{\mathbb{P}^4})^\vee\longrightarrow(R\pi_\ast\mu^\ast T_Y)^\vee\longrightarrow i^\ast\mathcal{V}_d^\vee[1]\longrightarrow i^\ast(R\pi_\ast\mu^\ast T_{\mathbb{P}^4})^\vee[1]$$

을 얻고, 처음 두 항은 [명제 4](#prop4){: data-lid="65y3n" }의 relative perfect obstruction theory들이다. [KKP]는 이 triangle이 cotangent complex의 triangle과 compatible하다고 적고 여기에 [명제 7](#prop7){: data-lid="ycr9q" }을 적용한다. $\mathbb{P}^4$는 convex이므로 [예시 5](#ex5){: data-lid="4mh66" }에 의해 ambient의 virtual class는 fundamental class이고, 따라서

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
