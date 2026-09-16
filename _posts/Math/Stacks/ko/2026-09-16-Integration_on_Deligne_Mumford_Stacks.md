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

published: false
---

이제 우리는 stack 위의 적분을 정의한다. 직관적으로 stack의 점은 automorphism group $G$를 가져 점이 $\lvert G\rvert$번 중복되는 효과를 내므로, 적분에서는 $1/\lvert G\rvert$의 보정이 필요하다. 이번 글에서 다룰 proper finite type Deligne–Mumford stack에서는 geometric stabilizer가 finite하므로 이러한 가중치가 잘 정의된다.

한편 pure dimensional algebraic stack에서 fundamental cycle 자체는 properness와 관계없이 정의되지만, 우리가 적분을 하려는 이유는 이를 structure morphism을 따라 한 점으로 pushforward하여 수치적인 degree를 얻기 위해서이다. 또,  smooth stack에서는 Chow cohomology와 Chow homology가 fundamental class와의 cap product를 통해 서로 대응하므로, cohomological notation을 사용해 적분을 다루기에도 편리하다. 따라서 이번 글에서 등장하는 모든 stack은 $\mathbb{C}$ 위의 smooth proper connected Deligne–Mumford stack을 의미한다. 

## Chow group과 proper pushforward

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


## Zero-cycle의 degree

일반적인 scheme에서 cycle의 degree나 적분이 한 점으로 가는 structure morphism의 proper pushforward이듯, Deligne–Mumford stack 위의 적분 또한 본질적으로 구조사상 $p:\mathcal{X}\rightarrow\Spec\mathbb{C}$에 의한 proper pushforward 그 자체이다. Target의 zero-dimensional Chow group은

$$A_0(\Spec\mathbb{C})_\mathbb{Q}=\mathbb{Q}[\Spec\mathbb{C}]\cong\mathbb{Q}$$

이므로, proper pushforward는 곧바로 *degree map*

$$\deg:=p_\ast:A_0(\mathcal{X})_\mathbb{Q}\longrightarrow\mathbb{Q}$$

을 정의한다. 스택의 점에 붙는 $1/\lvert G\rvert$ 가중치 역시 외부에서 인위적으로 부여하는 것이 아니라, [정의 1](#def1){: data-relation="required" }의 proper pushforward가 한 점으로 갈 때 stabilizer ratio를 계산하면서 자연스럽게 유도된다.

::: 따름정리 3 (Zero-cycle의 stabilizer 가중치)
$\mathcal{Z}\subseteq\mathcal{X}$를 $0$-dimensional integral closed substack이라 하고, 그 generic stabilizer의 order를 $e_\mathcal{Z}$라 하자. 그러면

$$\deg[\mathcal{Z}]=\frac{1}{e_\mathcal{Z}}$$

이다. 따라서 $z=\sum_i m_i[\mathcal{Z}_i]\in Z_0(\mathcal{X})_\mathbb{Q}$이면

$$\deg z=\sum_i\frac{m_i}{e_{\mathcal{Z}_i}}$$

이다. 특히 $\mathcal{Z}$의 유일한 geometric point를 $x$라 하면 $e_\mathcal{Z}=\lvert\Aut(x)\rvert$이므로, 이러한 zero-dimensional cycle을 약식으로 $[x]$라 쓸 때

$$\deg[x]=\frac{1}{\lvert\Aut(x)\rvert}$$

이다.
:::

::: 증명
$\mathcal{Z}$는 $0$-dimensional integral proper stack이므로 그 coarse moduli space는 $\Spec\mathbb{C}$이다. 따라서 구조사상 $p:\mathcal{Z}\rightarrow\Spec\mathbb{C}$에 [정의 1](#def1){: data-relation="required" }을 적용하면 coarse function field degree는 $1$, source의 generic stabilizer order는 $e_\mathcal{Z}$, target의 stabilizer order는 $1$이다. 따라서

$$p_\ast[\mathcal{Z}]=\frac{1}{e_\mathcal{Z}}[\Spec\mathbb{C}]$$

이다. 나머지는 linearity로부터 즉시 따른다.
:::

이 식에서 multiplicity $m_i$와 stabilizer 가중치 $1/e_{\mathcal{Z}_i}$는 서로 다른 정보를 나타낸다. Scheme-theoretic intersection에서 생기는 length나 intersection multiplicity는 $m_i$에 들어가고, 그 점의 automorphism은 $e_{\mathcal{Z}_i}$에 들어간다.

## Smooth proper stack 위의 적분

Pure $d$-dimensional stack $\mathcal{X}$에는 fundamental cycle $[\mathcal{X}]\in A_d(\mathcal{X})_\mathbb{Q}$이 있다. $\mathcal{X}$가 smooth이면 fundamental class와의 cap product에 의하여 Chow cohomology와 Chow homology 사이에

$$A^k(\mathcal{X})_\mathbb{Q}\xrightarrow{\sim} A_{d-k}(\mathcal{X})_\mathbb{Q},\qquad\alpha\longmapsto\alpha\cap[\mathcal{X}]$$

라는 identification을 얻는다. 따라서 top codimension class는 자연스럽게 zero-cycle을 결정하고, 앞에서 정의한 degree를 적용할 수 있다.

::: 정의 4 (적분)
$\mathcal{X}$를 smooth proper Deligne–Mumford stack of pure dimension $d$라 하자. Top Chow class $\alpha\in A^d(\mathcal{X})_\mathbb{Q}$의 *적분*을

$$\int_\mathcal{X}\alpha:=\deg(\alpha\cap[\mathcal{X}])=p_\ast(\alpha\cap[\mathcal{X}])\in\mathbb{Q}$$

로 정의한다.
:::

따라서 stack 위의 적분은 별도의 위상수학적 normalization을 추가하여 정의되는 것이 아니다. Proper pushforward 자체에 이미 stabilizer의 비율이 들어 있고, 적분은 그것을 top-dimensional intersection에 적용한 것에 불과하다.

::: 명제 5 (Quotient와 coarse space의 적분)
1. 연결된 smooth proper variety $U$에 finite group $G$가 작용하고 $p:U\rightarrow[U/G]$를 quotient morphism이라 하자. 그러면 임의의 $\alpha\in A^{\dim U}([U/G])_\mathbb{Q}$에 대하여

   $$\int_{[U/G]}\alpha=\frac{1}{\lvert G\rvert}\int_U p^\ast\alpha$$

   이다. 특히 한 점에 $G$가 trivial하게 작용하는 경우 $\int_{[\Spec\mathbb{C}/G]}1=1/\lvert G\rvert$이다.
2. $\mathcal{X}$를 connected integral proper Deligne–Mumford stack이라 하고 $\pi:\mathcal{X}\rightarrow X$를 coarse moduli morphism, generic stabilizer order를 $e$라 하자. Coarse moduli space $X$는 일반적으로 singularity를 가지므로 cohomology class는 operational Chow cohomology class $\beta\in A_{\mathrm{op}}^d(X)_\mathbb{Q}$로 잡는다. 이때

   $$\pi_\ast[\mathcal{X}]=\frac{1}{e}[X]$$

   이며,

   $$\int_\mathcal{X}\pi^\ast\beta=\frac{1}{e}\int_X\beta$$

   이다. (여기서 $\int_X\beta:=\deg(\beta\cap[X])$이다.)
:::

::: 증명
1. $p:U\rightarrow[U/G]$는 stack의 의미에서 finite flat $G$-torsor이며 degree가 $\lvert G\rvert$이다. 따라서 $p_\ast[U]=\lvert G\rvert[[U/G]]$이다. Projection formula를 이용하면

   $$\begin{aligned}\int_U p^\ast\alpha&=\deg(p^\ast\alpha\cap[U])\\&=\deg\bigl(\alpha\cap p_\ast[U]\bigr)\\&=\lvert G\rvert\deg\bigl(\alpha\cap[[U/G]]\bigr)\\&=\lvert G\rvert\int_{[U/G]}\alpha\end{aligned}$$

   를 얻는다.
2. Coarse moduli morphism이 coarse space에 유도하는 morphism은 $X\rightarrow X$라는 항등 morphism이므로 function field degree는 $1$이다. Source의 generic stabilizer order는 $e$, target algebraic space의 generic stabilizer order는 $1$이므로 [정의 1](#def1){: data-relation="required" }에 의해 $\pi_\ast[\mathcal{X}]=\frac{1}{e}[X]$이다. $X$가 singularity를 갖더라도 operational class $\beta\in A_{\mathrm{op}}^d(X)_\mathbb{Q}$는 arbitrary pullback $\pi^\ast\beta$와 projection formula $\pi_\ast(\pi^\ast\beta\cap[\mathcal{X}])=\beta\cap\pi_\ast[\mathcal{X}]$를 만족하므로

   $$\int_\mathcal{X}\pi^\ast\beta=\deg(\pi^\ast\beta\cap[\mathcal{X}])=\deg(\beta\cap\pi_\ast[\mathcal{X}])=\frac{1}{e}\deg(\beta\cap[X])=\frac{1}{e}\int_X\beta$$

   를 얻는다.
:::

따라서 generic stabilizer가 trivial한 경우에는 fundamental cycle 수준에서 stack과 coarse space 사이에 추가적인 rational factor가 나타나지 않는다. 반면 generic stabilizer가 nontrivial하면 그 order가 전체 적분의 normalization에 직접 반영된다.

## Proper pushforward와 fiber integration

이제 smooth proper Deligne–Mumford stack 사이의 proper morphism $f:\mathcal{X}\rightarrow\mathcal{Y}$을 생각하자. $\dim\mathcal{X}=m$, $\dim\mathcal{Y}=n$이라 하고 relative dimension을 $r=m-n$이라 하자.

Smoothness에 의해 Chow cohomology와 homology를 fundamental class를 통해 식별하면 proper pushforward는 codimension notation에서

$$f_\ast:A^k(\mathcal{X})_\mathbb{Q}\longrightarrow A^{k-r}(\mathcal{Y})_\mathbb{Q}$$

로 쓸 수 있다. 정확히는 $f_\ast\alpha$를 $(f_\ast\alpha)\cap[\mathcal{Y}]:=f_\ast(\alpha\cap[\mathcal{X}])$로 정의한다.

::: 명제 6 (Projection formula와 fiber integration)
위의 $f$에 대하여 다음이 성립한다.
1. *Projection formula*: 임의의 $\alpha\in A^\ast(\mathcal{X})_\mathbb{Q}$, $\beta\in A^\ast(\mathcal{Y})_\mathbb{Q}$에 대하여

   $$f_\ast(\alpha\cdot f^\ast\beta)=f_\ast\alpha\cdot\beta$$

   이며, complementary degree에 대하여 $\int_\mathcal{X}\alpha\cdot f^\ast\beta=\int_\mathcal{Y}f_\ast\alpha\cdot\beta$이다.
2. *Fiber integration*: $f:\mathcal{C}\rightarrow\mathcal{M}$을 relative dimension $1$인 proper flat representable morphism이라 하고, $\mathcal{C},\mathcal{M}$을 smooth proper Deligne–Mumford stack이라 하자 ($\mathcal{M}$은 connected). 그러면 $\alpha\in A^1(\mathcal{C})_\mathbb{Q}$에 대하여 $f_\ast\alpha\in A^0(\mathcal{M})_\mathbb{Q}$이고, geometric point $y:\Spec\mathbb{C}\rightarrow\mathcal{M}$에서 그 값은 fiber 위의 degree

   $$\left.f_\ast\alpha\right\vert_y=\deg\bigl(\alpha\vert_{\mathcal{C}_y}\cap[\mathcal{C}_y]\bigr)$$

   로 주어진다. 특히 $f_\ast 1=0$이며, $X$가 smooth projective variety이고 $h:\mathcal{C}\rightarrow X$가 모든 geometric fiber에서 같은 curve class $\beta\in A_1(X)_\mathbb{Q}$를 나타낼 때 $D\in A^1(X)_\mathbb{Q}$이면

   $$f_\ast h^\ast D=(D\cdot\beta)1$$

   이다.
:::

::: 증명
1. Cycle-level proper pushforward와 Chow cohomology의 cap product는 projection formula

   $$f_\ast\bigl((\alpha\cap[\mathcal{X}])\cap f^\ast\beta\bigr)=f_\ast(\alpha\cap[\mathcal{X}])\cap\beta$$

   를 만족한다. Smoothness를 이용하여 이를 Chow cohomology notation으로 옮기면 첫째 식을 얻는다. $\mathcal{Y}$의 구조사상을 $q:\mathcal{Y}\rightarrow\Spec\mathbb{C}$라 하면 $\mathcal{X}$의 구조사상은 $q\circ f$이므로 proper pushforward의 functoriality에 의해 적분 보존 식도 성립한다.
2. Point inclusion $i_y:\Spec\mathbb{C}\rightarrow\mathcal{M}$는 flat morphism이 아니지만, $\mathcal{M}$이 smooth하므로 codimension $m=\dim\mathcal{M}$인 closed regular embedding이다. 다음 절의 regular embedding refined Gysin pullback과 proper pushforward의 base change compatibility $i_y^! f_\ast=(f_y)_\ast {i'_y}^!$에 의하여 fiber restriction은

   $$i_y^! f_\ast(\alpha\cap[\mathcal{C}])=(f_y)_\ast\bigl(\alpha\vert_{\mathcal{C}_y}\cap[\mathcal{C}_y]\bigr)$$

   로 계산된다. $f_y:\mathcal{C}_y\rightarrow\Spec\mathbb{C}$는 proper curve의 구조사상이므로 이는 정확히 fiber 위 zero-cycle의 degree이다. Relative dimension이 $1$이므로 $f_\ast 1\in A^{-1}(\mathcal{M})_\mathbb{Q}=0$이고, 각 fiber에서 $\deg(h\vert_{\mathcal{C}_y}^\ast D\cap[\mathcal{C}_y])=D\cdot\beta$이므로 $f_\ast h^\ast D=(D\cdot\beta)1$을 얻는다.
:::

Representability 때문에 geometric fiber $\mathcal{C}_y$는 algebraic space이며, moduli of curves에서 나타나는 일반적인 경우에는 proper nodal curve이다. 따라서 위 fiber degree에는 stack stabilizer에 의한 별도의 분모가 새로 생기지 않는다. Node나 여러 irreducible component가 있을 경우에는 ordinary fundamental cycle이 그 component들을 scheme-theoretic multiplicity와 함께 센다.

## 곱과 diagonal의 refined intersection

두 stack 위의 독립적인 intersection은 product 위에서 서로 곱해진다. Moduli problem을 diagonal을 따라 붙이거나 incidence condition을 부여하기 위해서는 regular embedding의 *refined Gysin pullback*

$$i^!:A_k(V)_\mathbb{Q}\longrightarrow A_{k-c}(W)_\mathbb{Q}$$

이 핵심 역할을 한다. ([Vis, §3], [Kre, §2])

::: 명제 7 (Refined Gysin과 diagonal 분해)
1. **Product integration**: Smooth proper Deligne–Mumford stack $\mathcal{X},\mathcal{Y}$와 top-degree class $\alpha\in A^{\dim\mathcal{X}}(\mathcal{X})_\mathbb{Q}$, $\beta\in A^{\dim\mathcal{Y}}(\mathcal{Y})_\mathbb{Q}$에 대하여

   $$\int_{\mathcal{X}\times\mathcal{Y}}\pr_\mathcal{X}^\ast\alpha\cdot\pr_\mathcal{Y}^\ast\beta=\left(\int_\mathcal{X}\alpha\right)\left(\int_\mathcal{Y}\beta\right)$$

   이다.
2. **Diagonal refined Gysin formula**: Smooth $d$-dimensional variety $X$와 smooth proper Deligne–Mumford stack $\mathcal{M},\mathcal{N}$ 및 morphism $u:\mathcal{M}\rightarrow X$, $v:\mathcal{N}\rightarrow X$를 잡자. Fiber product를 $\mathcal{Z}=\mathcal{M}\times_X\mathcal{N}$이라 하고 $j:\mathcal{Z}\rightarrow\mathcal{M}\times\mathcal{N}$을 자연스러운 closed immersion이라 하자. Diagonal $\Delta_X:X\hookrightarrow X\times X$는 codimension $d$인 closed regular embedding이므로, refined Gysin pullback은 $\mathcal{Z}$의 refined intersection class

   $$[\mathcal{Z}]_\Delta:=\Delta_X^!\bigl([\mathcal{M}]\times[\mathcal{N}]\bigr)\in A_{\dim\mathcal{M}+\dim\mathcal{N}-d}(\mathcal{Z})_\mathbb{Q}$$

   를 정의하며, $j_\ast[\mathcal{Z}]_\Delta=(u,v)^\ast[\Delta_X]\cap\bigl([\mathcal{M}]\times[\mathcal{N}]\bigr)$이 성립한다. 따라서 적절한 codimension의 $\eta\in A^\ast(\mathcal{M}\times\mathcal{N})_\mathbb{Q}$에 대하여

   $$\deg\bigl(j^\ast\eta\cap[\mathcal{Z}]_\Delta\bigr)=\int_{\mathcal{M}\times\mathcal{N}}\eta\cdot(u,v)^\ast[\Delta_X]$$

   이다. 특히 $(u,v)$가 diagonal과 transverse한 경우에는 $[\mathcal{Z}]_\Delta=[\mathcal{Z}]$이다.
3. **Divisor incidence**: Smooth Cartier divisor $D\hookrightarrow X$에 대하여 $\mathcal{Z}_D=\mathcal{M}\times_X D$라 하면 refined intersection class $[\mathcal{Z}_D]_D:=i_D^![\mathcal{M}]$이 정의되고, $j_\ast[\mathcal{Z}_D]_D=u^\ast[D]\cap[\mathcal{M}]=u^\ast c_1(\mathcal{O}_X(D))\cap[\mathcal{M}]$ 및

   $$\deg\bigl(j^\ast\alpha\cap[\mathcal{Z}_D]_D\bigr)=\int_\mathcal{M}\alpha\cdot u^\ast[D]$$

   가 성립한다.
:::

::: 증명
1. External product와 proper pushforward의 compatibility로부터 즉시 따른다. Stack의 stabilizer 가중치는 각 factor에서 이미 degree map에 들어 있으므로 product에서도 자동으로 곱해진다.
2. Refined Gysin과 proper pushforward의 호환성에 의해 $j_\ast\Delta_X^!([\mathcal{M}]\times[\mathcal{N}])=(u,v)^\ast[\Delta_X]\cap([\mathcal{M}]\times[\mathcal{N}])$이 성립하며, projection formula에 의해 적분 공식이 얻어진다. Transverse할 때 ordinary fundamental cycle과 일치함은 Gysin map의 기본 성질이다.
3. $D\hookrightarrow X$는 codimension $1$ closed regular embedding이므로 2번의 특수한 경우로 즉시 성립한다.
:::

지금까지의 논의는 모두 rational Chow group 안에서 이루어졌다. 특히 stack 위의 $1/\lvert\Aut(x)\rvert$ 가중치는 별도로 부여한 convention이 아니라 proper pushforward의 stack-theoretic degree에서 자연스럽게 발생한다. 이후 moduli problem에서 ordinary fundamental cycle을 virtual fundamental class로 대체하거나 arbitrary cohomology class를 insertion으로 사용하는 경우에도 이 intersection-theoretic 구조가 기본 토대가 된다.

---

**참고문헌**

**[Vis]** A. Vistoli, *Intersection theory on algebraic stacks and on their moduli spaces*, Invent. Math. **97** (1989), 613–670.

**[Kre]** A. Kresch, *Cycle construction for Artin stacks*, Invent. Math. **138** (1999), 495–536.
