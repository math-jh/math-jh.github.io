---
title: "Deligne–Mumford 스택 위의 적분"
description: "복소수체 위의 Deligne–Mumford stack에서 Chow group과 proper pushforward를 통해 유리수 가중치와 적분을 정의하고, projection formula, fiber integration, refined Gysin 공식과 Gromov–Witten 이론을 위한 Betti cohomology 확장을 다룬다."
excerpt: "Rational Chow groups, proper pushforward, and integration on Deligne–Mumford stacks with applications to Gromov–Witten theory"

categories: [Math / Stacks]
permalink: /ko/math/stacks/integration_on_deligne_mumford_stacks
sidebar:
    nav: "stacks-ko"

date: 2026-09-16
weight: 6

published: false
---

이제 우리는 stack 위의 적분을 정의한다. 직관적으로 stack의 점은 automorphism group $G$를 가져 점이 $\lvert G\rvert$번 중복되는 효과를 내므로, 적분에서는 $1/\lvert G\rvert$의 보정이 필요하다. 이것이 의미가 있기 위해서는 우선 $\lvert G\rvert$가 유한해야 하므로, 적분은 [§대수적 스택, ⁋정의 6](/ko/math/stacks/algebraic_stacks#def6){: data-relation="required" }의 Deligne–Mumford stack 위에서 정의된다. Fundamental cycle $[\mathcal{X}]$ 자체는 임의의 pure-dimensional algebraic stack 위에 존재하지만, 이를 점으로 pushforward하여 수치적인 degree와 적분을 얻기 위해서는 properness가 필요하다. 또한 intersection product와 $A^p(\mathcal{X})_\mathbb{Q}\cong A_{d-p}(\mathcal{X})_\mathbb{Q}$ 같은 codimension 표기법을 단순하고 깨끗하게 쓰기 위해 smoothness를 가정한다. 따라서 이번 글에서는 $\mathbb{C}$ 위의 smooth proper connected Deligne–Mumford stack $\mathcal{X}$ (pure dimension $d$)를 중심으로 적분 이론을 전개한다.

## Chow group과 stack의 degree

Vistoli의 교차 이론에 따르면, Deligne–Mumford stack $\mathcal{X}$의 $k$-cycle group $Z_k(\mathcal{X})_\mathbb{Q}$는 $k$차원 integral closed substack $\mathcal{V}\subseteq\mathcal{X}$들로 생성되는 $\mathbb{Q}$-vector space로 정의된다. $(k+1)$차원 integral substack $\mathcal{W}$와 그 function field의 원소 $f\in K(\mathcal{W})^\ast$가 주는 divisor $\operatorname{div}(f)$들로 생성되는 부분공간을 $R_k(\mathcal{X})_\mathbb{Q}$라 할 때, *rational Chow group*은

$$A_k(\mathcal{X})_\mathbb{Q}:=Z_k(\mathcal{X})_\mathbb{Q}/R_k(\mathcal{X})_\mathbb{Q}$$

로 정의된다.

Stack 위의 적분과 $1/\lvert G\rvert$ 가중치는 별도의 인위적인 선언이 아니라, cycle 수준에서 정의되는 proper pushforward의 고유한 성질로부터 자연스럽게 도출된다.

::: 정의 1 (Proper pushforward)
$f:\mathcal{X}\rightarrow\mathcal{Y}$를 Deligne–Mumford stack들 사이의 proper morphism이라 하고, $\mathcal{V}\subseteq\mathcal{X}$를 $k$차원 integral closed substack이라 하자. Image의 closure를 $\mathcal{W}=\overline{f(\mathcal{V})}$라 두자.
1. $\dim\mathcal{W}<\dim\mathcal{V}$이면 $f_\ast[\mathcal{V}]:=0$으로 정의한다.
2. $\dim\mathcal{W}=\dim\mathcal{V}$이면 coarse moduli space 사이의 유도사상 $V\rightarrow W$는 generically finite이다. 이때 $\mathcal{V}$와 $\mathcal{W}$의 generic stabilizer order를 각각 $e_\mathcal{V}, e_\mathcal{W}$라 하고 coarse function field의 차수를 $[K(V):K(W)]$라 할 때,
   
   $$f_\ast[\mathcal{V}]:=[K(V):K(W)]\frac{e_\mathcal{W}}{e_\mathcal{V}}[\mathcal{W}]$$
   
   로 정의하고 linear하게 확장한다.
:::

이 정의에서 $e_\mathcal{W}/e_\mathcal{V}$라는 비율이 들어가는 이유는 stack-theoretic generic degree를 올바르게 세기 위함이다. $\mathcal{V}$ 위의 generic point의 stabilizer $G_\mathcal{V}$는 $f$에 의하여 target의 stabilizer $G_\mathcal{W}$로 단사되므로, fiber의 점 하나는 automorphism에 의해 $\lvert G_\mathcal{W}\rvert/\lvert G_\mathcal{V}\rvert$배만큼 두꺼워진 효과를 낸다. 이 정의는 proper pushforward의 functoriality $(g\circ f)_\ast=g_\ast\circ f_\ast$를 완벽하게 보존한다. ([Vis, Proposition 3.7])

이제 proper Deligne–Mumford stack $\mathcal{X}$의 구조사상 $p:\mathcal{X}\rightarrow\Spec\mathbb{C}$를 생각하자. Target $\Spec\mathbb{C}$의 Chow group은 $A_0(\Spec\mathbb{C})_\mathbb{Q}=\mathbb{Q}[\Spec\mathbb{C}]\cong\mathbb{Q}$이므로, proper pushforward는 곧바로 *degree map*

$$\deg:=p_\ast:A_0(\mathcal{X})_\mathbb{Q}\longrightarrow\mathbb{Q}$$

을 정의한다.

::: 따름정리 2 (Residual gerbe와 zero-cycle의 degree)
Geometric point $x:\Spec\mathbb{C}\rightarrow\mathcal{X}$의 stabilizer를 $G_x=\Aut(x)$라 하고 그 residual gerbe를 $\mathcal{G}_x\cong\bB G_x$라 하자.
1. $\deg[\mathcal{G}_x]=1/\lvert G_x\rvert$이다.
2. Zero-cycle $z=\sum_i m_i[\mathcal{G}_{x_i}]\in Z_0(\mathcal{X})_\mathbb{Q}$의 degree는
   
   $$\deg z=\sum_i\frac{m_i}{\lvert G_{x_i}\rvert}$$
   
   이다.
:::

::: 증명
Residual gerbe $\mathcal{G}_x\cong\bB G_x$의 구조사상 $p:\bB G_x\rightarrow\Spec\mathbb{C}$에 [정의 1](#def1){: data-relation="required" }을 적용한다. Coarse moduli space는 둘 다 점 $\Spec\mathbb{C}$이므로 function field degree는 $1$이다. Source의 generic stabilizer order는 $e_{\bB G_x}=\lvert G_x\rvert$이고, target $\Spec\mathbb{C}$의 generic stabilizer order는 $e_{\Spec\mathbb{C}}=1$이다. 따라서

$$\deg[\mathcal{G}_x]=p_\ast[\bB G_x]=1\cdot\frac{1}{\lvert G_x\rvert}[\Spec\mathbb{C}]=\frac{1}{\lvert G_x\rvert}$$

을 얻는다. 일반적인 zero-cycle에 대해서는 linearity에 의해 둘째 식이 성립한다.
:::

## Smooth proper stack 위의 적분

Pure $d$차원 Deligne–Mumford stack $\mathcal{X}$는 smooth하므로 fundamental cycle $[\mathcal{X}]\in A_d(\mathcal{X})_\mathbb{Q}$를 가지며, intersection product를 통해 codimension과 dimension 사이의 표준적인 isomorphism

$$A^k(\mathcal{X})_\mathbb{Q}\xrightarrow{\sim} A_{d-k}(\mathcal{X})_\mathbb{Q},\qquad \alpha\longmapsto\alpha\cap[\mathcal{X}]$$

을 얻는다. 따라서 top codimension class의 적분을 zero-cycle의 degree로 직접 정의할 수 있다.

::: 정의 3 (적분)
Smooth proper Deligne–Mumford stack $\mathcal{X}$ (pure dimension $d$) 위에서 top Chow class $\alpha\in A^d(\mathcal{X})_\mathbb{Q}$의 *적분*을

$$\int_\mathcal{X}\alpha:=\deg(\alpha\cap[\mathcal{X}])=p_\ast(\alpha\cap[\mathcal{X}])\in\mathbb{Q}$$

로 정의한다.
:::

이 정의는 복잡한 위상수학을 거치지 않고도 곧바로 성립하는 대수기하학적 정의이다. 이로부터 stack 적분의 가장 핵심적인 두 계산을 즉시 얻을 수 있다.

::: 명제 4 (Quotient와 coarse space의 적분)
1. 연결된 smooth proper variety $U$에 finite group $G$가 작용할 때, quotient morphism $p:U\rightarrow[U/G]$와 임의의 $\alpha\in A^{\dim U}([U/G])_\mathbb{Q}$에 대하여
   
   $$\int_{[U/G]}\alpha=\frac{1}{\lvert G\rvert}\int_U p^\ast\alpha$$
   
   이다. 특히 $\int_{\bB G}1=1/\lvert G\rvert$이다.
2. 연결된 smooth proper Deligne–Mumford stack $\mathcal{X}$의 coarse moduli morphism을 $\pi:\mathcal{X}\rightarrow X$라 하고 generic stabilizer order를 $e$라 하자. 임의의 $\beta\in A^d(X)_\mathbb{Q}$에 대하여
   
   $$\int_\mathcal{X}\pi^\ast\beta=\frac{1}{e}\int_X\beta$$
   
   이다.
:::

::: 증명
1. $p:U\rightarrow[U/G]$는 generic fiber가 $G$인 principal $G$-bundle이다. Coarse space 사이의 사상은 $U\rightarrow U/G$로서 degree가 $\lvert G\rvert/e$ (여기서 $e$는 generic stabilizer)이고, $[U/G]$의 generic stabilizer order는 $e$, $U$의 generic stabilizer order는 $1$이다. 따라서 [정의 1](#def1){: data-relation="required" }에 의하여
   
   $$p_\ast[U]=\frac{\lvert G\rvert}{e}\cdot\frac{e}{1}[[U/G]]=\lvert G\rvert[[U/G]]$$
   
   이다. Projection formula에 의하여
   
   $$\int_U p^\ast\alpha=\deg(p^\ast\alpha\cap[U])=\deg(\alpha\cap p_\ast[U])=\lvert G\rvert\deg(\alpha\cap[[U/G]])=\lvert G\rvert\int_{[U/G]}\alpha$$
   
   가 성립한다. $U=\Spec\mathbb{C}$, $\alpha=1$을 대입하면 $\int_{\bB G}1=1/\lvert G\rvert$을 얻는다.
2. $\pi:\mathcal{X}\rightarrow X$에 대하여 coarse space 사이의 사상은 항등사상 $X\rightarrow X$이므로 field degree는 $1$이다. Source의 generic stabilizer는 $e$, target $X$의 generic stabilizer는 $1$이므로 [정의 1](#def1){: data-relation="required" }에 의해
   
   $$\pi_\ast[\mathcal{X}]=1\cdot\frac{1}{e}[X]=\frac{1}{e}[X]$$
   
   이다. 따라서 $\int_\mathcal{X}\pi^\ast\beta=\deg(\pi^\ast\beta\cap[\mathcal{X}])=\deg(\beta\cap\pi_\ast[\mathcal{X}])=(1/e)\deg(\beta\cap[X])=(1/e)\int_X\beta$이다.
:::

## Proper pushforward와 fiber integration

두 smooth proper Deligne–Mumford stack 사이의 proper morphism $f:\mathcal{X}\rightarrow\mathcal{Y}$ (relative dimension $r=\dim\mathcal{X}-\dim\mathcal{Y}$)에 대하여, cycle pushforward는 codimension 표기에서

$$f_\ast:A^k(\mathcal{X})_\mathbb{Q}\longrightarrow A^{k-r}(\mathcal{Y})_\mathbb{Q}$$

를 준다.

::: 명제 5 (Projection formula와 fiber integration)
위의 $f$와 $\alpha\in A^\ast(\mathcal{X})_\mathbb{Q}$, $\beta\in A^\ast(\mathcal{Y})_\mathbb{Q}$에 대하여 다음이 성립한다.
1. **Projection formula**: $f_\ast(\alpha\cdot f^\ast\beta)=f_\ast\alpha\cdot\beta$.
2. **적분의 보존**: $\int_\mathcal{X}\alpha\cdot f^\ast\beta=\int_\mathcal{Y}f_\ast\alpha\cdot\beta$.
3. **Universal curve와 fiber integration**: $f:\mathcal{C}\rightarrow\mathcal{M}$이 smooth proper Deligne–Mumford stack들 사이의 relative dimension $1$인 flat representable family of nodal curves라 하자. $\alpha\in A^1(\mathcal{C})_\mathbb{Q}$에 대하여 $f_\ast\alpha\in A^0(\mathcal{M})_\mathbb{Q}$이며, 임의의 geometric point $y:\Spec\mathbb{C}\rightarrow\mathcal{M}$에서 그 값은 fiber cycle과의 교차 degree
   
   $$\left.f_\ast\alpha\right\vert_y=\deg\bigl(\alpha\vert_{\mathcal{C}_y}\cap[\mathcal{C}_y]\bigr)$$
   
   로 주어진다. 특히
   
   $$f_\ast 1=0$$
   
   이고, $h:\mathcal{C}\rightarrow X$가 모든 fiber를 같은 curve class $\beta\in A_1(X)_\mathbb{Q}$로 보내는 사상이고 $D\in A^1(X)_\mathbb{Q}$이면
   
   $$f_\ast h^\ast D=\left(\int_\beta D\right)1$$
   
   이다.
:::

::: 증명
1. [Vis, Proposition 3.7]에 의해 Chow group 위의 cap product와 proper pushforward는 projection formula $f_\ast(\alpha\cap f^\ast b)=f_\ast\alpha\cap b$를 만족한다. Smoothness에 의해 이를 Chow ring의 곱으로 옮기면 원하는 식이 된다.
2. $\mathcal{Y}$의 구조사상을 $q:\mathcal{Y}\rightarrow\Spec\mathbb{C}$라 하면 $p=q\circ f$이다. 1번에 의해
   
   $$\int_\mathcal{X}\alpha\cdot f^\ast\beta=p_\ast(\alpha\cdot f^\ast\beta\cap[\mathcal{X}])=q_\ast f_\ast(\alpha\cdot f^\ast\beta\cap[\mathcal{X}])=q_\ast(f_\ast\alpha\cdot\beta\cap[\mathcal{Y}])=\int_\mathcal{Y}f_\ast\alpha\cdot\beta$$
   
   가 된다.
3. Fiber square가 Tor-independent이므로, Chow theory의 proper pushforward와 flat pullback의 base change 호환성에 의하여 $y^\ast f_\ast\alpha=(f_y)_\ast(\alpha\vert_{\mathcal{C}_y})$이다. $f_y:\mathcal{C}_y\rightarrow\Spec\mathbb{C}$는 proper curve의 구조사상이므로 이는 정확히 fiber 위에서의 degree이다. $f_\ast 1\in A^{-1}(\mathcal{M})_\mathbb{Q}=0$이므로 $f_\ast 1=0$이고, $h^\ast D$의 각 fiber 제한은 $\mathcal{C}_y$ 위에서 degree $\int_\beta D$를 가지므로 $f_\ast h^\ast D=(\int_\beta D)1$을 얻는다.
:::

## Refined Gysin pullback과 교차

두 독립적인 moduli 공간의 곱에 대해서는 Chow external product와 degree map의 곱셈성에 의하여

$$\int_{\mathcal{X}\times\mathcal{Y}}\pr_\mathcal{X}^\ast\alpha\cdot\pr_\mathcal{Y}^\ast\beta=\left(\int_\mathcal{X}\alpha\right)\left(\int_\mathcal{Y}\beta\right)$$

가 성립한다.

Moduli 공간들을 diagonal을 따라 붙이거나 incidence 조건을 부여할 때에는 regular embedding의 *refined Gysin homomorphism*이 핵심 역할을 한다. Codimension $d$인 closed regular embedding $i:Z\hookrightarrow Y$와 임의의 사상 $f:V\rightarrow Y$에 대하여, fiber product $W=V\times_Y Z$로 가는 사상

$$i^!:A_k(V)_\mathbb{Q}\longrightarrow A_{k-d}(W)_\mathbb{Q}$$

이 정의된다. ([Vis, §3], [Kre, §2])

::: 명제 6 (Refined Gysin과 diagonal 분해)
Smooth projective variety $X$ (dimension $d$)와 smooth proper Deligne–Mumford stack $\mathcal{M},\mathcal{N}$ 및 사상 $u:\mathcal{M}\rightarrow X$, $v:\mathcal{N}\rightarrow X$를 잡자. Fiber product를 $\mathcal{Z}=\mathcal{M}\times_X\mathcal{N}$이라 하고 $j:\mathcal{Z}\hookrightarrow\mathcal{M}\times\mathcal{N}$을 자연스러운 embedding이라 하자.
1. Diagonal $\Delta_X:X\hookrightarrow X\times X$의 refined Gysin pullback은 $\mathcal{Z}$의 virtual fundamental cycle
   
   $$[\mathcal{Z}]^{\mathrm{vir}}:=\Delta_X^!([\mathcal{M}]\times[\mathcal{N}])\in A_{\dim\mathcal{M}+\dim\mathcal{N}-d}(\mathcal{Z})_\mathbb{Q}$$
   
   을 정의하며, $(u,v)$가 $\Delta_X$에 transverse하면 이는 ordinary fundamental cycle $[\mathcal{Z}]$와 일치한다.
2. $\mathcal{M}\times\mathcal{N}$ 위에서 $j_\ast[\mathcal{Z}]^{\mathrm{vir}}=(u,v)^\ast[\Delta_X]\cap([\mathcal{M}]\times[\mathcal{N}])$이 성립하며, 따라서 임의의 $\eta\in A^\ast(\mathcal{M}\times\mathcal{N})_\mathbb{Q}$에 대하여
   
   $$\int_{[\mathcal{Z}]^{\mathrm{vir}}}j^\ast\eta=\int_{\mathcal{M}\times\mathcal{N}}\eta\cdot(u,v)^\ast[\Delta_X]$$
   
   이다.
3. Smooth Cartier divisor $D\hookrightarrow X$에 대하여 $\mathcal{Z}'=\mathcal{M}\times_XD$라 하면, $j'_\ast[\mathcal{Z}']^{\mathrm{vir}}=u^\ast[D]=u^\ast c_1(\mathcal{O}_X(D))$이고
   
   $$\int_{[\mathcal{Z}']^{\mathrm{vir}}}{j'}^\ast\alpha=\int_\mathcal{M}\alpha\cdot u^\ast[D]$$
   
   이다.
:::

::: 증명
1. Diagonal $\Delta_X:X\hookrightarrow X\times X$는 smooth variety $X\times X$ 안의 codimension $d$인 closed regular embedding (normal bundle $T_X$)이다. 따라서 refined Gysin map $\Delta_X^!:A_\ast(\mathcal{M}\times\mathcal{N})_\mathbb{Q}\rightarrow A_{\ast-d}(\mathcal{Z})_\mathbb{Q}$가 직접 적용되어 $[\mathcal{Z}]^{\mathrm{vir}}$를 정의한다. Transverse할 때 ordinary cycle과 일치함은 Gysin map의 기본 성질이다.
2. Regular embedding의 refined Gysin과 proper pushforward의 가환성에 의해 $j_\ast\Delta_X^!([\mathcal{M}\times\mathcal{N}])=\Delta_X^\ast([\mathcal{M}\times\mathcal{N}])$이며, smooth ambient variety 위에서는 이것이 pullback class $(u,v)^\ast[\Delta_X]$와의 교차와 같다. [명제 5](#prop5){: data-relation="required" }의 projection formula를 적용하면 적분 공식이 얻어진다.
3. $D\hookrightarrow X$는 codimension $1$ closed regular embedding이므로 2번의 특수한 경우로 즉시 성립한다.
:::

## Gromov–Witten 이론과 Betti cohomology로의 확장

지금까지 구축한 적분 이론은 순수하게 대수기하학적인 Chow group $A_\ast(\mathcal{X})_\mathbb{Q}$ 위에서 완결된다. 그러나 Gromov–Witten 이론을 전개할 때에는 target variety $X$의 위상수학적 불변량, 즉 Betti cohomology $H^\ast(X,\mathbb{Q})$의 insertion들을 stack 위에 올려놓고 적분해야 한다.

$\mathbb{C}$ 위의 smooth proper Deligne–Mumford stack $\mathcal{X}$에 대하여, cycle class map

$$\mathrm{cl}:A^k(\mathcal{X})_\mathbb{Q}\longrightarrow H^{2k}(\mathcal{X}^{\mathrm{an}},\mathbb{Q})$$

은 Chow ring의 교차곱을 위상적 cup product로, Chow proper pushforward를 topological pushforward로 보낸다. 따라서 top-degree cohomology class $\alpha\in H^{2d}(\mathcal{X}^{\mathrm{an}},\mathbb{Q})$에 대해서도

$$\int_\mathcal{X}\alpha:=\langle\alpha,[\mathcal{X}]\rangle\in\mathbb{Q}$$

로 자연스럽게 확장되며, Chow 이론에서 얻은 모든 공식(안정자 가중치 $\int_{\bB G}1=1/\lvert G\rvert$, projection formula, fiber integration)이 Betti cohomology 수준에서도 그대로 유지된다.

특히 smooth projective variety $X$의 Betti cohomology $H^\ast(X,\mathbb{Q})$는 rational Poincaré duality를 만족하므로, homogeneous basis $\{T_a\}$와 그 dual basis $\{T^a\}$ ($\int_X T_a\smile T^b=\delta_a^b$)에 대하여 diagonal class의 Künneth 분해

$$[\Delta_X]=\sum_a(-1)^{\deg T_a}T_a\otimes T^a\in H^{2d}(X\times X,\mathbb{Q})$$

를 얻는다. 이를 [명제 6](#prop6){: data-relation="required" }의 Gysin 공식에 대입하면, stable map들의 moduli stack $\overline{\mathcal{M}}_{g,n}(X,\beta)$에서 node를 쪼개거나 붙이는 gluing morphism $q:\overline{\mathcal{M}}_{g_1,n_1+1}(X,\beta_1)\times_X\overline{\mathcal{M}}_{g_2,n_2+1}(X,\beta_2)\rightarrow\overline{\mathcal{M}}_{g,n}(X,\beta)$ 위의 적분이

$$\int_{[\mathcal{Z}]^{\mathrm{vir}}}q^\ast\eta=\sum_a(-1)^{\deg T_a}\left(\int_{\overline{\mathcal{M}}_{g_1,n_1+1}}\cdots\mathrm{ev}_{n_1+1}^\ast T_a\right)\left(\int_{\overline{\mathcal{M}}_{g_2,n_2+1}}\cdots\mathrm{ev}_{n_2+1}^\ast T^a\right)$$

와 같이 두 moduli 공간 위의 적분의 곱들의 합으로 분해된다. 이것이 바로 Gromov–Witten 불변량의 splitting axiom과 WDVV 방정식을 유도하는 대수기하학적 토대이다.

---

**참고문헌**

**[Vis]** A. Vistoli, *Intersection theory on algebraic stacks and on their moduli spaces*, Invent. Math. **97** (1989), 613–670.

**[Kre]** A. Kresch, *Cycle construction for Artin stacks*, Invent. Math. **138** (1999), 495–536.
