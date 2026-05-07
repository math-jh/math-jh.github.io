---
title: "Hirzebruch-Riemann-Roch"
permalink: /ko/math/algebraic_varieties/hirzebruch_riemann_roch
excerpt: "Hirzebruch-Riemann-Roch 정리와 그 특수한 경우들"
categories: [Math / Algebraic Varieties]
sidebar:
    nav: "algebraic_varieties-ko"
header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Hirzebruch_Riemann_Roch.png
    overlay_filter: 0.5
date: 2026-05-07
last_modified_at: 2026-05-07
weight: 24
---

Riemann-Roch 정리는 algebraic geometry의 핵심 정리 중 하나로, 주어진 다양체 위의 sheaf의 cohomology에 대한 정보를 그 다양체의 기하학적 불변량으로 계산하는 공식을 제공한다. Curve에서의 classical Riemann-Roch 정리는 divisor의 degree와 curve의 genus만을 사용하여 Euler characteristic을 계산하며, surface로의 일반화에서는 intersection number가 추가적으로 등장한다. Hirzebruch는 이러한 저차원의 결과들을 통일적인 공식으로 일반화하여, 임의의 차원을 갖는 smooth projective variety 위의 coherent sheaf에 대한 Riemann-Roch 공식을 얻었다. 본 글에서는 이 **Hirzebruch-Riemann-Roch (HRR)** 정리를 서술하고, 저차원으로의 환원, 증명의 개요, 그리고 구체적인 계산 예시를 다룬다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Smooth projective variety $X$ 위의 coherent sheaf $\mathcal{F}$에 대하여, 그 **Euler characteristic** $\chi(X,\mathcal{F})$를

$$\chi(X,\mathcal{F})=\sum_{i\geq 0}(-1)^i\dim H^i(X,\mathcal{F})$$

으로 정의한다. 우리는 대개 $X$가 projective이고 $\mathcal{F}$가 coherent이므로 각 cohomology group이 finite dimensional이며, $i>\dim X$에서는 소멸하므로 위의 합은 유한합이다.

</div>

HRR 정리의 좌변은 바로 이 Euler characteristic이며, 우변은 $X$의 intersection theory 위에서의 적분으로 주어진다. 이를 위해서는 Chern character와 Todd class라는 두 가지 characteristic class가 필요하다. 이들의 정의와 성질은 [§Todd Class](/ko/math/algebraic_varieties/todd_class)에서 자세히 다루었으므로, 본 글에서는 필요한 최소한의 사실만을 상기시킨다.

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2 (Hirzebruch-Riemann-Roch)**</ins> Algebraically closed field 위의 smooth projective variety $X$와 그 위의 coherent sheaf $\mathcal{F}$에 대하여 다음이 성립한다.

$$\chi(X,\mathcal{F})=\int_X\operatorname{ch}(\mathcal{F})\cdot\operatorname{td}(T_X)$$

여기서 $\operatorname{ch}(\mathcal{F})$는 $\mathcal{F}$의 Chern character, $\operatorname{td}(T_X)$는 tangent bundle $T_X$의 Todd class이며, $\int_X$는 Chow group $A_{\dim X}(X)$ (또는 cohomology $H^{2\dim X}(X,\mathbb{Q})$) 위의 degree map을 의미한다.

</div>

정리 [2](#thm2)에서 우변의 $\operatorname{ch}(\mathcal{F})\cdot\operatorname{td}(T_X)$는 Chow ring $A^\bullet(X)\otimes_\mathbb{Z}\mathbb{Q}$ 위에서의 곱셈이며, $\int_X$는 이 곱의 $\dim X$차 동차 성분을 취한 후 그 degree를 적분하는 연산이다. 즉, $n=\dim X$일 때

$$\int_X\operatorname{ch}(\mathcal{F})\cdot\operatorname{td}(T_X)=\bigl[\operatorname{ch}(\mathcal{F})\cdot\operatorname{td}(T_X)\bigr]_n$$

으로, 여기서 $[\bullet]_n$는 $n$차 동차 성분을 의미한다.

## 저차원으로의 환원

HRR 정리는 임의의 차원에서 성립하는 보편적인 공식이지만, 저차원으로 낮추면 classical하게 알려진 Riemann-Roch 공식들로 환원된다. 이는 HRR 정리의 검증과 동시에, 고차원의 기하학이 저차원의 결과들을 어떻게 통합하는지를 보여준다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3 (곡선에서의 환원)**</ins> $X=C$를 genus $g$인 smooth projective curve라 하자. 임의의 divisor $D$에 대하여, HRR 정리는 classical Riemann-Roch 정리

$$\ell(D)-\ell(K_C-D)=\deg D+1-g$$

로 환원된다. 여기서 $K_C$는 canonical divisor이며, $\ell(D)=\dim H^0(C,\mathcal{O}_C(D))$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Curve $C$의 차원은 $n=1$이다. Line bundle $\mathscr{L}=\mathcal{O}_C(D)$에 대하여 Chern character는 $\operatorname{ch}(\mathscr{L})=1+c_1(\mathscr{L})$이고, tangent bundle $T_C$의 rank가 $1$이므로 [§Todd Class, ⁋예시 5](/ko/math/algebraic_varieties/todd_class#ex5)에 의해

$$\operatorname{td}(T_C)=1+\frac{1}{2}c_1(T_C)=1-\frac{1}{2}K_C$$

이다. 따라서

$$\operatorname{ch}(\mathscr{L})\cdot\operatorname{td}(T_C)=\left(1+c_1(\mathscr{L})\right)\left(1-\frac{1}{2}K_C\right)$$

의 $1$차 성분은 $c_1(\mathscr{L})-\frac{1}{2}K_C$이며, 이를 적분하면

$$\chi(C,\mathscr{L})=\int_C c_1(\mathscr{L})-\frac{1}{2}K_C=\deg(\mathscr{L})+1-g$$

이 된다. 한편 Euler characteristic의 정의와 Serre duality에 의해

$$\chi(C,\mathscr{L})=\dim H^0(C,\mathscr{L})-\dim H^1(C,\mathscr{L})=\ell(D)-\ell(K_C-D)$$

이므로 classical Riemann-Roch 정리 [§곡선에서의 리만-로흐 정리, ⁋명제 3](/ko/math/algebraic_varieties/riemann_roch_theorem#prop3)을 복원한다. $\square$

</details>

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4 (곡면에서의 환원)**</ins> $X=S$를 smooth projective surface라 하자. HRR 정리는 다음의 surface Riemann-Roch formula

$$\chi(S,\mathcal{O}_S(D))=\frac{1}{2}D\cdot(D-K_S)+\chi(\mathcal{O}_S)$$

로 환원되며, 특히 $\mathcal{F}=\mathcal{O}_S$를 대입하면 **Noether formula**

$$K_S^2+c_2(S)=12\chi(\mathcal{O}_S)$$

을 얻는다. 여기서 $D\cdot D$는 divisor의 self-intersection number, $K_S$는 canonical divisor, $c_2(S)$는 second Chern class이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Surface $S$의 차원은 $n=2$이다. Line bundle $\mathcal{O}_S(D)$에 대하여 Chern character는

$$\operatorname{ch}(\mathcal{O}_S(D))=1+D+\frac{D^2}{2}$$

이며, [§Todd Class, ⁋예시 6](/ko/math/algebraic_varieties/todd_class#ex6)에 의해 tangent bundle의 Todd class는

$$\operatorname{td}(T_S)=1+\frac{c_1(T_S)}{2}+\frac{c_1(T_S)^2+c_2(T_S)}{12}=1-\frac{K_S}{2}+\frac{K_S^2+c_2(S)}{12}$$

이다. 이들의 곱에서 $2$차 성분을 모으면

$$\bigl[\operatorname{ch}(\mathcal{O}_S(D))\cdot\operatorname{td}(T_S)\bigr]_2=\frac{D^2}{2}-\frac{D\cdot K_S}{2}+\frac{K_S^2+c_2(S)}{12}$$

이므로 HRR 정리에 의해

$$\chi(S,\mathcal{O}_S(D))=\frac{D\cdot(D-K_S)}{2}+\frac{K_S^2+c_2(S)}{12}$$

이 성립한다. 특히 $D=0$을 대입하면 $\chi(\mathcal{O}_S)=\frac{K_S^2+c_2(S)}{12}$이므로

$$K_S^2+c_2(S)=12\chi(\mathcal{O}_S)$$

를 얻는다. 이것이 바로 Noether formula이다. 이를 surface Riemann-Roch formula에 되돌리면

$$\chi(S,\mathcal{O}_S(D))=\frac{1}{2}D\cdot(D-K_S)+\chi(\mathcal{O}_S)$$

를 얻어 [§곡면에서의 리만-로흐 정리](/ko/math/algebraic_varieties/riemann_roch_surfaces)의 결과와 일치함을 확인한다. $\square$

</details>

## Grothendieck-Riemann-Roch 정리

Hirzebruch의 정리는 하나의 다양체 위에서의 Euler characteristic을 계산하는 공식이었다. Grothendieck는 이를 두 다양체 사이의 proper morphism에 대한 상대적 형태로 일반화하였다.

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5 (Grothendieck-Riemann-Roch)**</ins> Smooth projective variety들 사이의 proper morphism $f:X\rightarrow Y$와 $X$ 위의 coherent sheaf $\mathcal{F}$에 대하여 다음이 성립한다.

$$f_\ast\bigl(\operatorname{ch}(\mathcal{F})\cdot\operatorname{td}(T_X)\bigr)=\operatorname{ch}(Rf_\ast\mathcal{F})\cdot\operatorname{td}(T_Y)$$

여기서 $f_\ast:A^\bullet(X)\otimes\mathbb{Q}\rightarrow A^\bullet(Y)\otimes\mathbb{Q}$는 Chow group에서의 push-forward, $Rf_\ast\mathcal{F}$는 $\mathcal{F}$의 derived direct image이며, 이의 Chern character는 $\operatorname{ch}(Rf_\ast\mathcal{F})=\sum_i(-1)^i\operatorname{ch}(R^i f_\ast\mathcal{F})$로 정의된다.

</div>

정리 [5](#thm5)에서 $Y=\operatorname{Spec}(k)$로 두면, $f_\ast$는 적분 $\int_X$가 되고 $Rf_\ast\mathcal{F}$는 $H^\bullet(X,\mathcal{F})$를 나타내므로

$$\int_X\operatorname{ch}(\mathcal{F})\cdot\operatorname{td}(T_X)=\sum_i(-1)^i\dim H^i(X,\mathcal{F})=\chi(X,\mathcal{F})$$

이 되어 정리 [2](#thm2)의 HRR 공식이 특수한 경우로 얻어진다. 따라서 Grothendieck-Riemann-Roch 정리는 HRR 정리의 자연스러운 일반화이다.

## 증명 개요

HRR 정리의 완전한 증명은 상당한 기술적 준비를 필요로 하며, 특히 Grothendieck-Riemann-Roch 정리의 체계 내에서 이해된다. 본 절에서는 증명의 전략과 핵심적인 아이디어를 개괄한다.

증명의 출발점은 **Grothendieck group** $K_0(X)$이다. Smooth projective variety $X$ 위의 locally free coherent sheaf들의 isomorphism class로 생성되는 free abelian group에, short exact sequence $\mathcal{E}'\rightarrow\mathcal{E}\rightarrow\mathcal{E}''$마다 관계식 $[\mathcal{E}]=[\mathcal{E}']+[\mathcal{E}'']$를 부여하여 얻어지는 ring이 바로 $K_0(X)$이다. Smooth variety 위에서는 coherent sheaf가 locally free sheaf의 유한 해상계를 갖으므로, $K_0(X)$의 원소는 임의의 coherent sheaf의 class로 확장된다.

Chern character는 ring homomorphism

$$\operatorname{ch}:K_0(X)\longrightarrow A^\bullet(X)\otimes_\mathbb{Z}\mathbb{Q}$$

을 정의하며, Todd class는 vector bundle의 직접합에 대해 multiplicative이다. 이들을 조합하여

$$\tau_X(\mathcal{F})=\operatorname{ch}(\mathcal{F})\cdot\operatorname{td}(T_X)$$

으로 정의하면, GRR 정리는 $f:X\rightarrow Y$에 대하여

$$f_\ast\circ\tau_X=\tau_Y\circ f_!$$

가 성립함을 주장한다. 여기서 $f_!:K_0(X)\rightarrow K_0(Y)$는 $[\mathcal{F}]\mapsto\sum_i(-1)^i[R^i f_\ast\mathcal{F}]$로 주어지는 push-forward이다.

Grothendieck는 임의의 projective morphism을 두 가지 기본적인 경우로 분해할 수 있음을 보였다. 첫째는 projective bundle의 projection $\pi:\mathbb{P}(E)\rightarrow Y$이고, 둘째는 closed immersion $j:X\hookrightarrow Y$이다. Projective bundle의 경우에는 projective bundle formula를 사용하여 비교적 직접적으로 GRR을 검증할 수 있다.

Closed immersion의 경우가 핵심적인 어려움을 내포하는데, 이를 극복하는 기법이 바로 **deformation to the normal cone**이다. $j:X\hookrightarrow Y$를 closed immersion이라 하자. 그러면 $Y\times\mathbb{P}^1$을 $X\times\{0\}$에 대해 blow-up하여 얻어지는 다양체 $M$을 고려한다. 이 때 $M$은 $\mathbb{P}^1$ 위의 flat family를 이루며, $t\neq 0$인 fiber $M_t$는 $Y$와 isomorphic하고, $t=0$인 fiber $M_0$는 exceptional divisor $\mathbb{P}(N_{X/Y}\oplus\mathcal{O}_X)$와 blow-up $\widetilde{Y}$의 합으로 나타난다.

Deformation to the normal cone의 핵심은 다음과 같다. $X$를 $Y$에 embedded시킨 상황에서의 GRR 등식을, $X$를 자신의 normal bundle $N_{X/Y}$에 zero section으로 embedded시킨 훨씬 단순한 상황으로 **변형**할 수 있다는 것이다. Normal bundle에 대한 zero section embedding의 경우에는 Koszul complex를 사용한 명시적인 계산이 가능하며, 이로부터 closed immersion에 대한 GRR 등식을 유도한다. 이 과정에서 Chow ring에서의 **self-intersection formula**와 **excess intersection formula**가 본질적으로 사용된다.

이러한 기법들을 종합하여 Grothendieck는 GRR 정리를 증명하였고, 이로부터 $Y$가 점인 특수한 경우인 HRR 정리가 따른다. Fulton과 others는 이후 deformation to the normal cone을 보다 체계적으로 발전시켜, intersection theory의 근간을 이루는 일련의 결과들을 통합적으로 증명하였다.

## 예시: 사영공간 $\mathbb{P}^n$

Projective space는 그 기하학이 명시적으로 파악되어 있으므로, HRR 정리를 검증하고 Hilbert polynomial을 유도하기에 적합한 예시이다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6 ($\mathbb{P}^n$에서의 HRR)**</ins> $\mathbb{P}^n$ 위의 line bundle $\mathcal{O}_{\mathbb{P}^n}(d)$에 대하여 HRR 정리를 적용하면, $\mathbb{P}^n$의 Hilbert polynomial

$$\chi(\mathbb{P}^n,\mathcal{O}_{\mathbb{P}^n}(d))=\binom{n+d}{n}$$

이 유도된다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[§Todd Class, ⁋예시 7](/ko/math/algebraic_varieties/todd_class#ex7)에서 살펴보았듯이, $\mathbb{P}^n$의 Chow ring은 $A^\bullet(\mathbb{P}^n)\cong\mathbb{Z}[h]/(h^{n+1})$이며, tangent bundle의 total Chern class는 $c(T_{\mathbb{P}^n})=(1+h)^{n+1}$이다. 따라서 Chern roots는 모두 hyperplane class $h$이며,

$$\operatorname{td}(T_{\mathbb{P}^n})=\left(\frac{h}{1-e^{-h}}\right)^{n+1}$$

이다. 한편 line bundle $\mathcal{O}_{\mathbb{P}^n}(d)$의 Chern character는 $\operatorname{ch}(\mathcal{O}_{\mathbb{P}^n}(d))=e^{dh}$이므로,

$$\operatorname{ch}(\mathcal{O}_{\mathbb{P}^n}(d))\cdot\operatorname{td}(T_{\mathbb{P}^n})=e^{dh}\left(\frac{h}{1-e^{-h}}\right)^{n+1}$$

이다. HRR 정리에 의해 이것의 $n$차 성분을 취한 후 적분하면 $\chi(\mathbb{P}^n,\mathcal{O}_{\mathbb{P}^n}(d))$가 된다. 적분 $\int_{\mathbb{P}^n}$은 사실상 $h^n$의 계수를 추출하는 연산이므로, 우리는

$$\chi(\mathbb{P}^n,\mathcal{O}_{\mathbb{P}^n}(d))=\bigl[e^{dh}\cdot\operatorname{td}(T_{\mathbb{P}^n})\bigr]_n$$

를 계산해야 한다. Formal power series $\frac{h}{1-e^{-h}}$의 역수는 $\frac{1-e^{-h}}{h}$이며, 이는 Bernoulli 수와 관련이 있다. 보다 직접적인 계산을 위하여 우리는

$$e^{dh}\left(\frac{h}{1-e^{-h}}\right)^{n+1}=\frac{h^{n+1}e^{dh}}{(1-e^{-h})^{n+1}}$$

를 생각한다. $t=-h$로 치환하면

$$\frac{(-t)^{n+1}e^{-dt}}{(1-e^t)^{n+1}}=\frac{t^{n+1}e^{-dt}}{(e^t-1)^{n+1}}$$

이 된다. $(e^t-1)^{n+1}$의 전개와 $e^{-dt}$의 전개를 고려하여, $t^n$의 계수를 구하면 그 값이 $\chi(\mathbb{P}^n,\mathcal{O}_{\mathbb{P}^n}(d))$가 된다.

보다 간단한 접근법으로, $\frac{h}{1-e^{-h}}$를 $1+\frac{h}{2}+\frac{h^2}{12}-\cdots$로 전개하고 $e^{dh}$를 $1+dh+\frac{d^2h^2}{2!}+\cdots$로 전개한 뒤, $h^n$의 계수를 직접 모으는 방법도 있다. 예를 들어 $n=2$의 경우,

$$\operatorname{td}(T_{\mathbb{P}^2})=1+\frac{3h}{2}+h^2,\qquad \operatorname{ch}(\mathcal{O}_{\mathbb{P}^2}(d))=1+dh+\frac{d^2h^2}{2}$$

이므로

$$\chi(\mathbb{P}^2,\mathcal{O}_{\mathbb{P}^2}(d))=\frac{d^2}{2}+\frac{3d}{2}+1=\frac{(d+1)(d+2)}{2}=\binom{d+2}{2}$$

를 얻는다. 일반적으로는 residue theorem을 사용하거나, Todd class의 정의로부터 직접 계산하여 $\binom{n+d}{n}$이 됨을 확인할 수 있다. 이는 [§사영공간의 코호몰로지](/ko/math/algebraic_varieties/cohomology_of_projective_spaces)에서 직접 계산한 cohomology의 결과와 일치하며, 특히 $d\geq 0$일 때 $H^i(\mathbb{P}^n,\mathcal{O}_{\mathbb{P}^n}(d))=0$ for $i>0$이므로 $\chi$가 $h^0$와 일치하여 $\binom{n+d}{n}$이 됨을 알 수 있다. $\square$

</details>

예시 [6](#ex6)에서 얻어진 $\chi(\mathbb{P}^n,\mathcal{O}_{\mathbb{P}^n}(d))$는 $d$에 대한 $n$차 polynomial이며, 이를 $\mathbb{P}^n$ 위의 coherent sheaf에 대한 **Hilbert polynomial**의 원형으로 볼 수 있다. 임의의 coherent sheaf $\mathcal{F}$에 대하여 $d\gg 0$이면 Serre vanishing에 의해 $H^i(\mathbb{P}^n,\mathcal{F}(d))=0$ ($i>0$)이 되므로

$$P_{\mathcal{F}}(d)=\chi(\mathbb{P}^n,\mathcal{F}(d))$$

가 $\mathcal{F}$의 Hilbert polynomial이 된다. HRR 정리는 이 Hilbert polynomial을 Chern class와 Todd class의 곱으로 명시적으로 계산하는 방법을 제공한다.

## 예시: $\mathbb{P}^1\times\mathbb{P}^1$

Product of projective spaces는 두 개의 독립적인 projective line의 곱으로, 그 기하학이 각 요인의 기하학으로부터 직접적으로 결정되므로 HRR의 검증에 유용한 예시이다.

<div class="example" markdown="1">

<ins id="ex7">**예시 7 ($\mathbb{P}^1\times\mathbb{P}^1$에서의 HRR)**</ins> Product $Q=\mathbb{P}^1\times\mathbb{P}^1$ 위의 line bundle $\mathcal{O}_Q(a,b)=\pi_1^*\mathcal{O}_{\mathbb{P}^1}(a)\otimes\pi_2^*\mathcal{O}_{\mathbb{P}^1}(b)$에 대하여 HRR 정리를 적용하면

$$\chi(Q,\mathcal{O}_Q(a,b))=(a+1)(b+1)$$

이 성립한다. 특히 $a,b\geq 0$일 때 이는 $H^0(Q,\mathcal{O}_Q(a,b))$의 차원과 일치하며, 이는 bihomogeneous polynomial의 공간의 차원이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$Q=\mathbb{P}^1\times\mathbb{P}^1$의 Chow ring은

$$A^\bullet(Q)\cong\mathbb{Z}[h_1,h_2]/(h_1^2,h_2^2)$$

이며, 여기서 $h_1=\pi_1^*h$, $h_2=\pi_2^*h$이다. Tangent bundle은 $T_Q\cong\pi_1^*T_{\mathbb{P}^1}\oplus\pi_2^*T_{\mathbb{P}^1}$이므로, 각 요인의 $c(T_{\mathbb{P}^1})=1+2h$로부터

$$c(T_Q)=(1+2h_1)(1+2h_2)=1+2(h_1+h_2)+4h_1h_2$$

이다. 따라서 $c_1(T_Q)=2h_1+2h_2$, $c_2(T_Q)=4h_1h_2$이며, Todd class는

$$\operatorname{td}(T_Q)=1+\frac{c_1}{2}+\frac{c_1^2+c_2}{12}$$

이다. $h_1^2=h_2^2=0$이므로 $c_1^2=(2h_1+2h_2)^2=8h_1h_2$이고, 따라서

$$\frac{c_1^2+c_2}{12}=\frac{8h_1h_2+4h_1h_2}{12}=h_1h_2$$

이 되어

$$\operatorname{td}(T_Q)=1+(h_1+h_2)+h_1h_2$$

를 얻는다. 한편 $\mathcal{O}_Q(a,b)$의 Chern character는

$$\operatorname{ch}(\mathcal{O}_Q(a,b))=e^{ah_1+bh_2}=1+(ah_1+bh_2)+\frac{(ah_1+bh_2)^2}{2}=1+ah_1+bh_2+abh_1h_2$$

이다. 이들의 곱에서 $2$차 성분을 모으면

$$\bigl[\operatorname{ch}(\mathcal{O}_Q(a,b))\cdot\operatorname{td}(T_Q)\bigr]_2=ab\cdot h_1h_2+a\cdot h_1h_2+b\cdot h_1h_2+h_1h_2=(a+1)(b+1)h_1h_2$$

이다. $Q$ 위의 적분 $\int_Q$는 $h_1h_2$의 계수를 추출하는 것이며, $\deg(h_1h_2)=1$이므로

$$\chi(Q,\mathcal{O}_Q(a,b))=(a+1)(b+1)$$

을 얻는다. Künneth formula에 의해

$$H^i(Q,\mathcal{O}_Q(a,b))\cong\bigoplus_{j+k=i}H^j(\mathbb{P}^1,\mathcal{O}_{\mathbb{P}^1}(a))\otimes H^k(\mathbb{P}^1,\mathcal{O}_{\mathbb{P}^1}(b))$$

이므로, $a,b\geq 0$일 때 $H^0(\mathbb{P}^1,\mathcal{O}_{\mathbb{P}^1}(a))$의 차원은 $a+1$, $H^0(\mathbb{P}^1,\mathcal{O}_{\mathbb{P}^1}(b))$의 차원은 $b+1$이고 높은 차원의 cohomology는 소멸하므로 $h^0(\mathcal{O}_Q(a,b))=(a+1)(b+1)$이며 이는 Euler characteristic과 일치한다. $\square$

</details>

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic geometry*, Springer, 1977.

**[Ful]** W. Fulton, *Intersection Theory*, Springer, 1984.

**[Hir]** F. Hirzebruch, *Topological Methods in Algebraic Geometry*, Springer, 1966.

**[SGA6]** P. Berthelot, A. Grothendieck, L. Illusie, *Séminaire de Géométrie Algébrique du Bois Marie 1966/67 (SGA 6)*, Springer, 1971.
