---
title: "Todd Class"
permalink: /ko/math/algebraic_varieties/todd_class
excerpt: "Todd class와 Chern character, HRR 정리의 좌변"
categories: [Math / Algebraic Varieties]
sidebar: { nav: "algebraic_varieties-ko" }
header: { overlay_image: /assets/images/Math/Algebraic_Varieties/Todd_Class.png, overlay_filter: 0.5 }
date: 2026-05-07
last_modified_at: 2026-05-07
weight: 23
published: false
---

**Hirzebruch-Riemann-Roch (HRR)** 정리는 smooth projective variety $X$ 위의 vector bundle $E$에 대하여, 그 Euler characteristic $\chi(X,E)$를 $X$의 intersection theory 위에서 적분으로 표현한다. 구체적으로 HRR 정리는

$$\chi(X,E)=\int_X \operatorname{ch}(E)\cdot\operatorname{td}(T_X)$$

의 형태를 갖는다. 여기서 우변을 구성하는 두 가지 핵심적인 불변량이 바로 **Chern character** $\operatorname{ch}(E)$와 **Todd class** $\operatorname{td}(T_X)$이다. 본 글에서는 이들의 정의, 기본 성질, 그리고 저차원에서의 명시적인 계산을 다룬다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1 (Chern character)**</ins> Vector bundle $E$가 Chern roots $x_1,\ldots,x_r$을 갖는다고 하자. 그러면 $E$의 **Chern character** $\operatorname{ch}(E)$는

$$\operatorname{ch}(E)=\sum_{i=1}^r e^{x_i}$$

으로 정의된다. 여기서 $e^{x_i}$는 $1+x_i+\frac{x_i^2}{2!}+\frac{x_i^3}{3!}+\cdots$의 형태로 전개되는 formal power series이다.

</div>

Chern character는 Chern roots에 대한 대칭 함수이므로, Chern class $c_i(E)$들의 다항식으로 표현할 수 있다. 실제로 $e^{x_i}$를 전개하고 $k$차 동차 성분을 모으면,

$$\operatorname{ch}(E)=\operatorname{rk}(E)+c_1(E)+\frac{c_1(E)^2-2c_2(E)}{2}+\frac{c_1(E)^3-3c_1(E)c_2(E)+3c_3(E)}{6}+\cdots$$

을 얻는다. 앞의 몇 항만 확인하면, $e^{x_i}$의 전개에서 0차 항은 $\sum 1 = r = \operatorname{rk}(E)$이고, 1차 항은 $\sum x_i = c_1(E)$이며, 2차 항은 $\frac{1}{2}\sum x_i^2$이다. 한편 $(\sum x_i)^2 = \sum x_i^2 + 2\sum_{i<j} x_i x_j$이므로 $c_1^2 - 2c_2 = \sum x_i^2$이 성립하여 위의 식이 따라온다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> Vector bundle들의 short exact sequence

$$0\longrightarrow E'\longrightarrow E\longrightarrow E''\longrightarrow 0$$

에 대하여 다음이 성립한다.

$$\operatorname{ch}(E)=\operatorname{ch}(E')+\operatorname{ch}(E'').$$

또한 임의의 두 vector bundle $E$, $F$에 대하여

$$\operatorname{ch}(E\otimes F)=\operatorname{ch}(E)\cdot\operatorname{ch}(F)$$

가 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Splitting principle에 의해, 적당한 base change 후에는 $E'$, $E''$가 각각 Chern roots $\{x_i'\}$, $\{x_j''\}$를 갖는 complete flag로 분핸된다. 그러면 $E$의 Chern roots는 $\{x_i'\}\cup\{x_j''\}$가 되므로,

$$\operatorname{ch}(E)=\sum_i e^{x_i'}+\sum_j e^{x_j''}=\operatorname{ch}(E')+\operatorname{ch}(E'')$$

가 즉각적으로 얻어진다. 두 번째 식에 대해서는, $E$와 $F$의 Chern roots가 각각 $\{x_i\}$, $\{y_j\}$라 할 때 $E\otimes F$의 Chern roots는 $\{x_i+y_j\}$이다. 따라서

$$\operatorname{ch}(E\otimes F)=\sum_{i,j} e^{x_i+y_j}=\left(\sum_i e^{x_i}\right)\left(\sum_j e^{y_j}\right)=\operatorname{ch}(E)\cdot\operatorname{ch}(F)$$

가 성립한다. $\square$

</details>

명제 [2](#prop2)의 첫 번째 성질은 Chern character를 Grothendieck group $K_0(X)$ 위에서 잘 정의된 가군 동형사상

$$\operatorname{ch}: K_0(X)\longrightarrow A^\bullet(X)\otimes_\mathbb{Z}\mathbb{Q}$$

으로 확장시킨다. 여기서 $A^\bullet(X)$는 $X$의 Chow ring이다.

다음으로 Todd class를 정의한다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3 (Todd class)**</ins> Vector bundle $E$가 Chern roots $x_1,\ldots,x_r$을 갖는다고 하자. 그러면 $E$의 **Todd class** $\operatorname{td}(E)$는

$$\operatorname{td}(E)=\prod_{i=1}^r \frac{x_i}{1-e^{-x_i}}$$

으로 정의된다. 여기서 $\frac{x}{1-e^{-x}}$는 $1+\frac{1}{2}x+\frac{1}{12}x^2-\frac{1}{720}x^4+\cdots$로 전개되는 formal power series이다.

</div>

Todd class 역시 Chern roots에 대한 대칭 함수이므로 Chern class들의 다항식으로 나타난다. 구체적으로 전개하면,

$$\operatorname{td}(E)=1+\frac{c_1(E)}{2}+\frac{c_1(E)^2+c_2(E)}{12}+\frac{c_1(E)c_2(E)}{24}+\frac{-c_1(E)^4+4c_1(E)^2c_2(E)+c_1(E)c_3(E)+3c_2(E)^2-c_4(E)}{720}+\cdots$$

이다. 이 계수들은 Bernoulli 수와 깊은 관련이 있다. 즉,

$$\frac{x}{1-e^{-x}}=1+\frac{1}{2}x+\sum_{k=1}^\infty (-1)^{k-1}\frac{B_{2k}}{(2k)!}x^{2k}$$

으로 전개되며, $B_2=1/6$, $B_4=-1/30$, $B_6=1/42$ 등이 그에 해당한다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> Vector bundle들의 short exact sequence

$$0\longrightarrow E'\longrightarrow E\longrightarrow E''\longrightarrow 0$$

에 대하여 다음이 성립한다.

$$\operatorname{td}(E)=\operatorname{td}(E')\cdot\operatorname{td}(E'').$$

특히 $\operatorname{td}(E\oplus F)=\operatorname{td}(E)\cdot\operatorname{td}(F)$가 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Splitting principle에 의해 $E'$의 Chern roots를 $\{x_i'\}$, $E''$의 Chern roots를 $\{x_j''\}$라 하면 $E$의 Chern roots는 $\{x_i'\}\cup\{x_j''\}$이다. 따라서

$$\operatorname{td}(E)=\prod_i \frac{x_i'}{1-e^{-x_i'}}\cdot\prod_j \frac{x_j''}{1-e^{-x_j''}}=\operatorname{td}(E')\cdot\operatorname{td}(E'')$$

가 성립한다. 직접합의 경우 $0\rightarrow E\rightarrow E\oplus F\rightarrow F\rightarrow 0$이 exact sequence이므로 동일한 결론이 따른다. $\square$

</details>

Smooth projective variety $X$에 대하여, 그 **Todd class** $\operatorname{td}(X)$는 tangent bundle $T_X$의 Todd class로 정의한다. 즉 $\operatorname{td}(X)=\operatorname{td}(T_X)$이다. HRR 정리의 우변은 $\operatorname{ch}(E)\cdot\operatorname{td}(T_X)$이며, 이는 Chow ring (또는 cohomology ring) 위에서의 곱셈이다. $X$가 $n$-dimensional일 때, 적분 $\int_X$는 $A^n(X)\otimes\mathbb{Q}$ (또는 $H^{2n}(X,\mathbb{Q})$) 위의 degree map을 의미하므로, HRR 공식의 우변은 $\operatorname{ch}(E)\cdot\operatorname{td}(T_X)$의 $n$-차 동차 성분을 취한 후 적분한 값이다.

이제 저차원의 구체적인 예시를 살펴본다.

<div class="example" markdown="1">

<ins id="ex5">**예시 5 (곡선)**</ins> Smooth projective curve $X$의 차원은 $n=1$이다. 이때 tangent bundle $T_X$의 rank는 1이므로 단 하나의 Chern root $x_1$만 존재한다. $c_1(T_X)=-K_X$이므로,

$$\operatorname{td}(T_X)=\frac{x_1}{1-e^{-x_1}}=1+\frac{x_1}{2}+\cdots=1+\frac{1}{2}c_1(T_X)=1-\frac{1}{2}K_X$$

이다. 한편 line bundle $\mathscr{L}$에 대하여 $\operatorname{ch}(\mathscr{L})=1+c_1(\mathscr{L})$이므로,

$$\operatorname{ch}(\mathscr{L})\cdot\operatorname{td}(T_X)=(1+c_1(\mathscr{L}))\left(1-\frac{1}{2}K_X\right)$$

의 1차 성분은 $c_1(\mathscr{L})-\frac{1}{2}K_X$이다. 따라서

$$\chi(X,\mathscr{L})=\int_X c_1(\mathscr{L})-\frac{1}{2}K_X=\deg(\mathscr{L})+1-g$$

가 되어, classical Riemann-Roch theorem이 복원된다. ([§곡선에서의 리만-로흐 정리](/ko/math/algebraic_varieties/riemann_roch_theorem) 참조)

</div>

<div class="example" markdown="1">

<ins id="ex6">**예시 6 (곡면)**</ins> Smooth projective surface $X$의 차원은 $n=2$이다. $T_X$의 Chern roots를 $x_1, x_2$라 하면,

$$\operatorname{td}(T_X)=\frac{x_1}{1-e^{-x_1}}\cdot\frac{x_2}{1-e^{-x_2}}$$

이다. 각 factor를 2차까지 전개하면

$$\left(1+\frac{x_1}{2}+\frac{x_1^2}{12}\right)\left(1+\frac{x_2}{2}+\frac{x_2^2}{12}\right)=1+\frac{x_1+x_2}{2}+\frac{x_1^2+x_2^2+3x_1x_2}{12}$$

이다. 여기서 $c_1=x_1+x_2$, $c_2=x_1x_2$이고 $x_1^2+x_2^2=c_1^2-2c_2$이므로,

$$\operatorname{td}(T_X)=1+\frac{c_1}{2}+\frac{c_1^2+c_2}{12}$$

을 얻는다. ([§곡면에서의 리만-로흐 정리](/ko/math/algebraic_varieties/riemann_roch_surfaces) 참조)

</div>

<div class="example" markdown="1">

<ins id="ex7">**예시 7 (사영공간)**</ins> Projective space $\mathbb{P}^n$에 대하여, Euler exact sequence

$$0\longrightarrow\mathscr{O}_{\mathbb{P}^n}\longrightarrow\mathscr{O}_{\mathbb{P}^n}(1)^{\oplus(n+1)}\longrightarrow T_{\mathbb{P}^n}\longrightarrow 0$$

으로부터 $c(T_{\mathbb{P}^n})=(1+h)^{n+1}$이며, 따라서 $T_{\mathbb{P}^n}$의 Chern roots는 hyperplane class $h$가 $n+1$번 중복되어 나타난다. 따라서

$$\operatorname{td}(T_{\mathbb{P}^n})=\left(\frac{h}{1-e^{-h}}\right)^{n+1}$$

이다. 이는 $\mathbb{P}^n$의 Chow ring $A^\bullet(\mathbb{P}^n)\cong\mathbb{Z}[h]/(h^{n+1})$ 위에서, $h^{n+1}=0$이므로 적당한 차수에서 truncate된 formal power series로 이해된다. 예를 들어 $n=2$의 경우,

$$\left(\frac{h}{1-e^{-h}}\right)^3=\left(1+\frac{h}{2}+\frac{h^2}{12}\right)^3=1+\frac{3h}{2}+h^2$$

이고, $c_1(T_{\mathbb{P}^2})=3h$, $c_2(T_{\mathbb{P}^2})=3h^2$이므로 $\frac{c_1^2+c_2}{12}=\frac{9+3}{12}h^2=h^2$임을 확인할 수 있다.

</div>

앞서 살펴본 바와 같이, Chern character와 Todd class는 모두 Chern roots를 이용하여 formal power series의 형태로 정의된다. 이들은 splitting principle에 의해 well-defined이며, 각각 $K$-이론에서 Chow ring으로의 homomorphism과 vector bundle의 직접합에 대한 multiplicative class를 제공한다. HRR 정리의 좌변 $\operatorname{ch}(E)\cdot\operatorname{td}(T_X)$는 이 두 불변량의 곱으로, 차원에 따른 각 성분이 classical Riemann-Roch formula의 다양한 일반화로 환원됨을 보였다.

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic geometry*, Springer, 1977.

**[Ful]** W. Fulton, *Intersection Theory*, Springer, 1984.

**[Hir]** F. Hirzebruch, *Topological Methods in Algebraic Geometry*, Springer, 1966.
