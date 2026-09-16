---
title: "Deligne–Mumford 스택 위의 적분"
description: "복소수체 위의 Deligne–Mumford stack에서 Chow group과 proper pushforward를 통해 stabilizer 가중치와 적분을 정의하고, projection formula, fiber integration, refined Gysin pullback을 살펴본다."
excerpt: "Rational Chow groups, proper pushforward, and integration on Deligne–Mumford stacks"

categories: [Math / Stacks]
permalink: /ko/math/stacks/integration_on_deligne_mumford_stacks
sidebar:
    nav: "stacks-ko"

date: 2026-09-16
weight: 6

---

이제 우리는 stack 위의 적분을 정의한다. 직관적으로 stack의 점은 automorphism group $G$를 가져 점이 $\lvert G\rvert$번 중복되는 효과를 내므로, 적분에서는 $1/\lvert G\rvert$의 보정이 필요하다. 이번 글에서 다룰 proper finite type Deligne–Mumford stack에서는 geometric stabilizer가 finite하므로 이러한 가중치가 잘 정의된다.

한편 pure dimensional algebraic stack에서 fundamental cycle 자체는 properness와 관계없이 정의되지만, 우리가 적분을 하려는 이유는 이를 structure morphism을 따라 한 점으로 pushforward하여 수치적인 degree를 얻기 위해서이다. 또,  smooth stack에서는 Chow cohomology와 Chow homology가 fundamental class와의 cap product를 통해 서로 대응하므로, cohomological notation을 사용해 적분을 다루기에도 편리하다. 따라서 이번 글에서 등장하는 모든 stack은 $\mathbb{C}$ 위의 smooth proper connected Deligne–Mumford stack을 의미한다. 

## 스택의 저우 군

[\[대수다양체\] §저우 군, ⁋정의 5](/ko/math/algebraic_varieties/chow_groups#def5){: data-relation="required" }에서 우리는 variety의 algebraic cycle들을 rational equivalence로 나누어 Chow group을 정의하였다. Deligne–Mumford stack에서도 같은 방식으로 cycle과 rational equivalence를 정의할 수 있다. $k$차원 integral closed substack $\mathcal{V}\subseteq\mathcal{X}$들의 formal $\mathbb{Q}$-linear combination으로 이루어진 vector space를

$$Z_k(\mathcal{X})_\mathbb{Q}$$

라 하자. $(k+1)$-차원 integral closed substack $\mathcal{W}\subseteq\mathcal{X}$와 rational function $f\in K(\mathcal{W})^\times$가 주는 principal divisor들로 생성되는 부분공간을 $R_k(\mathcal{X})_\mathbb{Q}$라 하면, *rational Chow group*을

$$A_k(\mathcal{X})_\mathbb{Q}:=Z_k(\mathcal{X})_\mathbb{Q}/R_k(\mathcal{X})_\mathbb{Q}$$

로 정의한다. 이제 stack 위의 적분과 그 과정에서 나오는 $1/\lvert G\rvert$는 [\[대수다양체\] §저우 군, ⁋명제 6](/ko/math/algebraic_varieties/chow_groups#prop6){: data-relation="required" }의 proper pushforward를 stack으로 확장한 다음의 정의로부터 자연스럽게 도출된다.

::: 정의 1
두 Deligne-Mumford stack $\mathcal{X}, \mathcal{Y}$와 이 사이의 proper morphism $f: \mathcal{X}\rightarrow \mathcal{Y}$가 주어졌다 하자. $\mathcal{X}$의 $k$차원 integral closed substack $\mathcal{V}$와, $f$에 의한 $\mathcal{V}$의 image의 closure $\mathcal{W}=\cl f(\mathcal{V})$에 대하여 다음과 같이 정의한다. 

1. 만일 $\dim\mathcal{W}<\dim\mathcal{V}$이면 $f_\ast[\mathcal{V}]=0$으로 정의한다.
2. $\dim\mathcal{W}=\dim\mathcal{V}$의 경우, $\mathcal{V},\mathcal{W}$ coarse moduli space $V,W$와 이들의 generic stabilizer의 order $e_\mathcal{V},e_\mathcal{W}$에 대하여

   $$f_\ast[\mathcal{V}]:=[K(V):K(W)]\frac{e_\mathcal{W}}{e_\mathcal{V}}[\mathcal{W}]$$

   로 정의한다.

이를 linear하게 확장한 것이 rational equivalence를 보존하므로 pushforward $f_\ast:A_k(\mathcal{X})_\mathbb{Q}\longrightarrow A_k(\mathcal{Y})_\mathbb{Q}$를 정의한다.
:::

[\[대수다양체\] §저우 군, ⁋명제 6](/ko/math/algebraic_varieties/chow_groups#prop6){: data-relation="required" }에서는 같은 차원의 integral subvariety $V\rightarrow W$에 대한 pushforward가 단순히

$$[V]\longmapsto [K(V):K(W)][W]$$

로 주어졌던 것을 기억하자. 위 정의는 바로 이 공식을 Deligne–Mumford stack으로 확장한 것으로, 차이는 generic stabilizer의 비율 $e_{\mathcal W}/e_{\mathcal V}$이 추가된다는 점이다. 이는 근본적으로 [§고유스택, ⁋명제 4](/ko/math/stacks/proper_stacks#prop4) 직후에 살펴보았듯 coarse moduli에서 scheme-theoretic하게 보이는 degree와, stack이 고유하게 가지고 있는 automorphism 정보가 분리해서 보이는 것으로, 이런 이유에서 곱

$$[K(V):K(W)]\frac{e_{\mathcal W}}{e_{\mathcal V}}$$

을 $f$의 stack-theoretic generic degree라고 생각할 수 있다. 이러한 이유로 stack에서는 rational coefficient가 자연스럽게 나타나게 되는 것이다. 그럼 이렇게 정의한 pushforward의 성질은 다음의 functoriality이다. 

::: 명제 2 (Functoriality)
Deligne–Mumford stack들 사이의 proper morphism $f:\mathcal{X}\rightarrow\mathcal{Y}$와 $g:\mathcal{Y}\rightarrow\mathcal{Z}$에 대하여

$$(g\circ f)_\ast=g_\ast\circ f_\ast$$

가 성립한다.
:::

일반적인 scheme에서 적분은 fundamental class와 cap product를 해서 degree를 $0$으로 맞춘 후, 이를 structure morphism을 통해 proper pushforward로 보내 그 값을 얻어내는 과정이다. 이제 stack의 경우, target의 zero-dimensional (rational coefficient) Chow group은

$$A_0(\Spec\mathbb{C})_\mathbb{Q}=\mathbb{Q}[\Spec\mathbb{C}]\cong\mathbb{Q}$$

이 되며, proper pushforward는 곧바로 *degree map*

$$\deg:=p_\ast:A_0(\mathcal{X})_\mathbb{Q}\longrightarrow\mathbb{Q}$$

을 정의한다. 그럼 다음이 성립한다.

::: 보조정리 3
$\mathcal{Z}\subseteq\mathcal{X}$를 $0$-dimensional integral closed substack이라 하고, 그 유일한 geometric point를 $x$라 하자. 그러면

$$\deg[\mathcal{Z}]=\frac{1}{\lvert\Aut(x)\rvert}$$

이다.
:::

::: 증명
$\mathcal{Z}$는 $0$-dimensional integral proper stack이므로 그 coarse moduli space는 한 점 $\Spec\mathbb{C}$이고, $\mathcal{Z}\cong[\Spec\mathbb{C}/\Aut(x)]$이다. 따라서 구조사상 $p:\mathcal{Z}\rightarrow\Spec\mathbb{C}$에 [정의 1](#def1){: data-relation="required" }을 적용하면 coarse function field degree는 $1$, source의 generic stabilizer order는 $\lvert\Aut(x)\rvert$, target의 stabilizer order는 $1$이다. 그러므로

$$p_\ast[\mathcal{Z}]=\frac{1}{\lvert\Aut(x)\rvert}[\Spec\mathbb{C}]$$

이다.
:::

## 적분

일반적으로 pure $d$-dimensional stack $\mathcal{X}$에는 fundamental cycle $[\mathcal{X}]\in A_d(\mathcal{X})_\mathbb{Q}$이 존재한다는 것이 알려져 있다. 추가로, 만일 $\mathcal{X}$가 smooth이면 fundamental class와의 cap product에 의하여 Chow cohomology와 Chow homology 사이에 identification

$$A^k(\mathcal{X})_\mathbb{Q}\xrightarrow{\sim} A_{d-k}(\mathcal{X})_\mathbb{Q},\qquad\alpha\longmapsto\alpha\cap[\mathcal{X}]$$

이 존재한다. 따라서 top codimension class는 자연스럽게 zero-cycle을 결정하고, 이를 degree map으로 보낸 것을 이 cohomology class의 적분으로 정의할 수 있다.

::: 정의 4
Smooth proper Deligne–Mumford stack $\mathcal{X}$ of pure dimension $d$를 생각하자. Top class $\alpha\in A^d(\mathcal{X})_\mathbb{Q}$의 *적분*을

$$\int_\mathcal{X}\alpha:=\deg(\alpha\cap[\mathcal{X}])=p_\ast(\alpha\cap[\mathcal{X}])\in\mathbb{Q}$$

로 정의한다.
:::

우리는 위의 [보조정리 3](#lem3)에서 바로 이 degree map $\deg$에 automorphism에서 나오는 성분 $1/\lvert G\rvert$가 개입함을 보였다. 우선 이를 구체적인 예시에서 확인하.

::: 예시 5
Smooth proper variety $U$에 finite group $G$가 작용한다 하고, quotient stack $\mathcal{X}=\mathcal{X}$를 생각하자. 그럼 atlas $p:U\rightarrow \mathcal{X}$를 이용하여 이 위의 적분을 써줄 수 있다. 즉, $d=\dim U$라 하면, 임의의 $\alpha\in A^d(\mathcal{X})_\mathbb{Q}$에 대하여

$$\int_{\mathcal{X}}\alpha=\frac{1}{\lvert G\rvert}\int_U p^\ast\alpha$$

가 성립한다. 이를 직접 확인하기 위해 $\alpha$에 대응하는 zero-cycle을

$$z=\alpha\cap[\mathcal{X}]=\sum_i m_i[\mathcal{Z}_i]$$

라 하면, 각 $0$-dimensional integral closed substack $\mathcal{Z}_i$의 geometric point를 $x_i$라 하고 그 stabilizer를 $G_i=\Aut(x_i)$라 하면, [보조정리 3](#lem3){: data-relation="required" }에 의하여 $\deg[\mathcal{Z}_i]=1/\lvert G_i\rvert$이 성립한다. 

한편 $x_i$를 $U$의 한 점 $u_i$로 나타내면 $p$에 의한 $\mathcal{Z}_i$의 pullback은 $u_i$의 $G$-orbit에 대응한다. 이 때 orbit-stabilizer formula에 의하여 이 orbit은 $\lvert G\rvert/\lvert G_i\rvert$개의 서로 다른 점으로 이루어지며, 이 때 각 점들은 scheme $U$의 점이므로 각각 degree $1$을 가진다. 따라서

$$\deg\bigl(p^\ast[\mathcal{Z}_i]\bigr)=\frac{\lvert G\rvert}{\lvert G_i\rvert}=\lvert G\rvert\deg[\mathcal{Z}_i]$$

이 성립하며, 이를 각 항에 적용하여 합하면 

$$\deg(p^\ast z)=\lvert G\rvert\deg z$$

를 얻는다. $p$는 flat하므로 $p^\ast z=p^\ast\alpha\cap[U]$이고, 따라서

$$\int_U p^\ast\alpha=\lvert G\rvert\int_{\mathcal{X}}\alpha$$

가 성립한다. 
:::

비슷하게 coarse moduli space와 전체 stack에서의 적분 또한 다음과 같이 비교할 수 있다. 

::: 예시 6
$\pi:\mathcal{X}\rightarrow X$를 coarse moduli morphism이라 하고, $\mathcal{X}$의 generic stabilizer의 order를 $e$라 하자. 그러면

$$\pi_\ast[\mathcal{X}]=\frac{1}{e}[X]$$

가 성립한다. 실제로 coarse moduli morphism $\pi$가 coarse space 사이에 유도하는 morphism은 $\mathrm{id}_X$이므로 function field degree는 $1$이다. 한편 source $\mathcal{X}$의 generic stabilizer order는 $e$이고 target $X$는 algebraic space (혹은 scheme)이므로 stabilizer가 trivial하다. 따라서 [정의 1](#def1){: data-relation="required" }에 의해

$$\pi_\ast[\mathcal{X}]=1\cdot\frac{1}{e}[X]=\frac{1}{e}[X]$$

를 얻는다. 즉 coarse moduli space에서는 보이지 않는 generic stabilizer가 fundamental cycle의 pushforward에서 정확히 $1/e$의 가중치로 나타난다.
:::

## 올을 따른 적분

한편, 위에서 설명했듯 적분은 structure morphism을 따른 proper pushforward이므로, 이를 임의의 proper morphism으로 확장할 수 있다. 이를 위해 smooth proper Deligne-Mumford stack 사이의 proper morphism $f:\mathcal{X}\rightarrow\mathcal{Y}$을 생각하자. $\dim\mathcal{X}=m$, $\dim\mathcal{Y}=n$이라 하고 relative dimension을 $r=m-n$이라 하자. Smoothness를 사용하여 homology class를 cohomology class로 바꿔주면, 위의 proper pushforward는 

$$f_\ast:A^k(\mathcal{X})_\mathbb{Q}\longrightarrow A^{k-r}(\mathcal{Y})_\mathbb{Q}$$

로 쓸 수 있다. 즉 우리는 cohomology class $\alpha$에 대하여, $f_\ast \alpha$를 다음 식

$$(f_\ast\alpha)\cap[\mathcal{Y}]:=f_\ast(\alpha\cap[\mathcal{X}])$$

로 정의한다. 그럼 다음의 projection formula가 성립한다. ([\[대수다양체\] §교차곱, ⁋명제 14](/ko/math/algebraic_varieties/intersection_product#prop14){: data-relation="required" })

::: 명제 7 (Projection formula)
위와 같은 상황에서, 임의의 $\alpha\in A^\ast(\mathcal{X})_\mathbb{Q}$, $\beta\in A^\ast(\mathcal{Y})_\mathbb{Q}$에 대하여

$$f_\ast(\alpha\cdot f^\ast\beta)=f_\ast\alpha\cdot\beta$$

가 성립한다. 특히 양변이 top degree가 되는 경우

$$\int_\mathcal{X}\alpha\cdot f^\ast\beta=\int_\mathcal{Y}f_\ast\alpha\cdot\beta$$

이다.
:::

직관적으로 이는 integration along fiber지만, 이를 실제로 fiber 위에서의 적분으로 해석하기 위해서는 base의 한 점으로 주어진 class를 제한하는 연산, 즉 Gysin map이 필요하다. Codimension $c$인 closed regular embedding $i:Z\hookrightarrow Y$와 morphism $g:V\rightarrow Y$가 주어졌다고 하자. Cartesian square

$$W=V\times_Y Z$$

에서 induced closed embedding을 $i':W\hookrightarrow V$라 하면 *refined* Gysin pullback

$$i^!:A_k(V)_\mathbb{Q}\longrightarrow A_{k-c}(W)_\mathbb{Q}$$

이 정의되는 것이 알려져 있다. 이는 일반적인 Gysin pullback에 더하여, proper pushforward와 base change에 대하여 호환된다. 구체적으로 codimension $c$인 closed regular embedding $i:Z\hookrightarrow Y$와 proper morphism $g:V\rightarrow Y$가 주어지고,

$$W=V\times_Y Z$$

라 하자. 이때 $i':W\hookrightarrow V$와 $g':W\rightarrow Z$를 fiber product에서 유도되는 morphism이라 하면

$$i^!g_\ast=g'_\ast{i'}^!$$

가 성립한다.

이를 proper family $f:\mathcal{C}\rightarrow\mathcal{M}$와 base의 한 점 $y\rightarrow\mathcal{M}$에 적용하면, $f_\ast$한 class를 $y$에서 제한하는 것은 먼저 fiber $\mathcal{C}_y$로 제한한 뒤 $f_y:\mathcal{C}_y\rightarrow y$를 따라 pushforward하는 것과 같아진다. 따라서 proper pushforward를 실제 fiber 위의 적분과 비교하는 다음의 fiber integration 공식을 얻는다.

::: 명제 8 (Fiber integration)
$f:\mathcal{C}\rightarrow\mathcal{M}$을 relative dimension $1$인 proper flat representable morphism이라 하고, $\mathcal{C},\mathcal{M}$을 smooth proper Deligne-Mumford stack이라 하자. 또한 $\mathcal{M}$은 connected라고 가정하자.

그러면 $\alpha\in A^1(\mathcal{C})_\mathbb{Q}$에 대하여

$$f_\ast\alpha\in A^0(\mathcal{M})_\mathbb{Q}$$

이고, geometric point $y:\Spec\mathbb{C}\rightarrow\mathcal{M}$에서 그 값은 fiber 위의 degree

$$\left.f_\ast\alpha\right|_y=\deg\bigl(\alpha|_{\mathcal{C}_y}\cap[\mathcal{C}_y]\bigr)$$

로 주어진다. 특히

$$f_\ast1=0$$

이다.

또 $X$가 smooth projective variety이고 $h:\mathcal{C}\rightarrow X$가 모든 geometric fiber에서 같은 curve class $\beta\in A_1(X)_\mathbb{Q}$를 나타낼 때, $D\in A^1(X)_\mathbb{Q}$이면

$$f_\ast h^\ast D=(D\cdot\beta)1$$

이다.
:::
::: 증명
Refined Gysin base change를 étale-local하게 적용하면

$$\left.f_\ast\alpha\right\vert_y=(f_y)_\ast\bigl(\alpha\vert_{\mathcal{C}_y}\cap[\mathcal{C}_y]\bigr)$$

를 얻는다. 여기서 $f$가 flat이므로 fiber에 대한 refined Gysin pullback은 fundamental class $[\mathcal{C}_y]$를 준다. 우변은 $f_y:\mathcal{C}_y\rightarrow\Spec\mathbb{C}$에 의한 zero-cycle의 pushforward이므로

$$\left.f_\ast\alpha\right|_y=\deg\bigl(\alpha|_{\mathcal{C}_y}\cap[\mathcal{C}_y]\bigr)$$

이다. 한편 relative dimension이 $1$이므로 $f_\ast1\in A^{-1}(\mathcal{M})_\mathbb{Q}=0$이다. 또한 각 fiber에서 $h^\ast D$의 degree가 $D\cdot\beta$이므로

$$f_\ast h^\ast D=(D\cdot\beta)1$$

을 얻는다.
:::

$f$가 representable이므로 geometric fiber $\mathcal{C}_y$는 algebraic space이다. 특히 moduli of curves에서 나타나는 경우에는 proper nodal curve가 된다. 따라서 위 fiber degree에는 stack stabilizer에서 오는 별도의 분모가 새로 나타나지 않는다. Reducible fiber의 경우에는 fundamental cycle $[\mathcal{C}_y]$가 각 irreducible component를 그 scheme-theoretic multiplicity와 함께 센다.

## 곱공간과 대각선 교차

이제 우리는 몇 가지 유용한 공식을 소개하며 이 글을 맞춘다. 두 stack 위에서 서로 독립적으로 주어진 intersection은 product 위에서 함께 다룰 수 있다. Smooth proper Deligne-Mumford stack $\mathcal{X},\mathcal{Y}$와 top-degree class $\alpha\in A^{\dim\mathcal{X}}(\mathcal{X})_\mathbb{Q}$, $\beta\in A^{\dim\mathcal{Y}}(\mathcal{Y})_\mathbb{Q}$에 대하여 external product와 degree의 multiplicativity로부터

$$\int_{\mathcal{X}\times\mathcal{Y}}\pr_\mathcal{X}^\ast\alpha\cdot\pr_\mathcal{Y}^\ast\beta=\left(\int_\mathcal{X}\alpha\right)\left(\int_\mathcal{Y}\beta\right)$$

를 얻는다. 즉 서로 독립적인 두 조건에 대한 적분은 product 위에서 각 적분의 곱으로 분리된다. 

위와 같이 두 stack을 단순히 함께 고려할 때에는 product를 사용하지만, 두 morphism을 같은 base 위에서 비교하려면 fiber product를 사용해야 한다. 이를 위해 morphism

$$u:\mathcal{M}\rightarrow X,\qquad v:\mathcal{N}\rightarrow X$$

이 주어졌다고 하자. 그럼 fiber product

$$\mathcal{Z}=\mathcal{M}\times_X\mathcal{N}$$

는 두 morphism의 image가 $X$에서 일치하는 부분을 나타내며, 이 fiber product는 diagonal을 이용하여 ordinary product 안의 intersection으로 표현할 수 있다. 이를 위해

$$(u,v):\mathcal{M}\times\mathcal{N}\longrightarrow X\times X$$

를 생각하면

$$\mathcal{M}\times_X\mathcal{N}=(\mathcal{M}\times\mathcal{N})\times_{X\times X}X$$

이며, 여기서 $X\rightarrow X\times X$는 diagonal $\Delta_X$이다. 즉, 직관적으로 fiber product를 형성하는 것은 $\mathcal{M}\times\mathcal{N}$을 diagonal $\Delta_X$와 base change하여 intersect하는 것으로 볼 수 있으며, 우리는 이러한 상황에서 사용하기 위해 앞에서 이미 refined Gysin pullback을 정의하였다. 즉, diagonal $\Delta_X$는 codimension $d$인 closed regular embedding이므로 앞에서 정의한 refined Gysin pullback을 적용할 수 있으며, 이를 통해 

$$[\mathcal{Z}]_\Delta:=\Delta_X^!\bigl([\mathcal{M}]\times[\mathcal{N}]\bigr)\in A_{\dim\mathcal{M}+\dim\mathcal{N}-d}(\mathcal{Z})_\mathbb{Q}$$

를 정의할 수 있다. 이를 $\mathcal{Z}$의 *refined intersection class*라 부른다. 

::: 명제 9 (대각선 교차 공식)
위의 상황에서, $j:\mathcal{Z}\rightarrow\mathcal{M}\times\mathcal{N}$을 자연스러운 closed immersion이라 하자. 그러면

$$j_\ast[\mathcal{Z}]_\Delta=(u,v)^\ast[\Delta_X]\cap\bigl([\mathcal{M}]\times[\mathcal{N}]\bigr)$$

가 성립한다. 따라서 적절한 codimension의 $\eta\in A^\ast(\mathcal{M}\times\mathcal{N})_\mathbb{Q}$에 대하여

$$\deg\bigl(j^\ast\eta\cap[\mathcal{Z}]_\Delta\bigr)=\int_{\mathcal{M}\times\mathcal{N}}\eta\cdot(u,v)^\ast[\Delta_X]$$

이다.

:::

이에 대한 증명으로는, refined Gysin pullback과 proper pushforward의 compatibility에 의해 첫 번째 식이 성립하고, 두 번째 식은 projection formula를 적용하면 바로 따른다. 즉 fiber product $\mathcal{Z}$ 위에서의 intersection은 product $\mathcal{M}\times\mathcal{N}$ 위에서 diagonal class를 하나 더 곱하는 계산으로 바꿀 수 있다.

앞에서는 diagonal $\Delta_X\hookrightarrow X\times X$을 따라 fiber product를 형성하여 두 morphism의 값이 일치한다는 조건을 intersection으로 표현하였다. 비슷한 방법으로 우리는 $X$의 부분공간을 통과한다는 조건에도 이러한 방식을 적용할 수 있다. 

Smooth Cartier divisor $i_D:D\hookrightarrow X$와 morphism $u:\mathcal{M}\rightarrow X$가 주어졌다고 하자. Fiber product

$$\mathcal{Z}_D:=\mathcal{M}\times_XD$$

는 $\mathcal{M}$의 점 가운데 그 image가 $D$ 위에 놓이는 부분을 나타낸다. 즉 $\mathcal{Z}_D$는 geometric condition

$$u(m)\in D$$

를 부과하여 얻어지는 locus이다. 

이제 위와 같은 방식을 적용하기 위해, $j_D:\mathcal{Z}_D\rightarrow\mathcal{M}$을 자연스러운 closed immersion이라 하자. 그럼 $D\hookrightarrow X$는 codimension $1$인 regular embedding이므로 refined Gysin pullback에 의해 다음의 refined intersection class

$$[\mathcal{Z}_D]_D:=i_D^![\mathcal{M}]$$

가 정의된다. 이를 $\mathcal{M}$으로 pushforward하면

$$j_{D\ast}[\mathcal{Z}_D]_D=u^\ast[D]\cap[\mathcal{M}]$$

를 얻으며, Cartier divisor의 class는 $[D]=c_1(\mathcal{O}_X(D))$이므로 이를

$$j_{D\ast}[\mathcal{Z}_D]_D=u^\ast c_1(\mathcal{O}_X(D))\cap[\mathcal{M}]$$

로도 쓸 수 있다.

따라서 적절한 class $\alpha\in A^\ast(\mathcal{M})_\mathbb{Q}$에 대하여

$$\deg\bigl(j_D^\ast\alpha\cap[\mathcal{Z}_D]_D\bigr)=\int_\mathcal{M}\alpha\cdot u^\ast[D]$$

이다. 즉, $u(m)\in D$라는 geometric condition을 직접 fiber product 위에서 다루는 대신, $\mathcal{M}$ 위에서 divisor class $u^\ast[D]$와 intersect하는 것으로 바꾸어 계산할 수 있다.

---

**참고문헌**

**[Vis]** A. Vistoli, *Intersection theory on algebraic stacks and on their moduli spaces*, Invent. Math. **97** (1989), 613–670.

**[Kre]** A. Kresch, *Cycle construction for Artin stacks*, Invent. Math. **138** (1999), 495–536.
