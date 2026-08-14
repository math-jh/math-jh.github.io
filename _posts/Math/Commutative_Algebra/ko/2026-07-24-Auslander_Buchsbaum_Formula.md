---
title: "Auslander-Buchsbaum 공식"
description: "Noetherian local ring 위에서 finite projective dimension을 갖는 module의 projective dimension과 depth의 합이 ring의 depth와 같다는 Auslander-Buchsbaum 공식을 depth에 대한 귀납법으로 증명하고, regular local ring과 Cohen-Macaulay module에 대한 귀결을 살펴본다."
excerpt: "pd M + depth M = depth A와 그 응용"

categories: [Math / Commutative Algebra]
permalink: /ko/math/commutative_algebra/auslander_buchsbaum_formula
sidebar: 
    nav: "commutative_algebra-ko"

date: 2026-07-24
weight: 27
published: false
drift_needed: true

---

[§호몰로지 차원](/ko/math/commutative_algebra/homological_dimension)에서 우리는 Noetherian local ring 위의 finitely generated module에 대하여 minimal free resolution을 세우고 projective dimension을 residue field와의 Tor가 소멸하지 않는 가장 높은 차수로 읽어내었으며, [§Depth](/ko/math/commutative_algebra/depth)에서는 maximal regular sequence의 길이로 depth를 정의하였다. 이 글은 이 두 불변량이 서로 독립적이지 않다는 Auslander--Buchsbaum 공식

$$\pd_A M+\operatorname{depth}M=\operatorname{depth}A$$

을 증명한다. 여기서 $(A,\mathfrak{m})$은 Noetherian local ring이고 $M\neq 0$은 $\pd_A M<\infty$를 만족하는 finitely generated $A$-module이다. 증명 뒤에는 이 공식이 regular local ring 위의 module과 Cohen--Macaulay module에 대해 주는 즉각적인 귀결들, 그리고 finite projective dimension 가정이 왜 필수적인지를 보이는 예시가 이어진다.

## 준비: regular 원소와 최소 자유 분해

공식의 증명은 $\operatorname{depth}A$에 대한 귀납법으로 진행된다. $\operatorname{depth}A\geq 1$이고 $\operatorname{depth}M\geq 1$이면 $A$와 $M$을 동시에 non-zerodivisor로 갖는 원소 $x$를 $\mathfrak{m}$에서 뽑아 $A/xA$로 내려가는데, 이때 depth는 [§Depth](/ko/math/commutative_algebra/depth)의 결과로 정확히 $1$씩 줄어드는 반면 projective dimension은 변하지 않아야 공식의 양변이 나란히 감소한다. Projective dimension이 보존되는 이유는 minimal free resolution이 $x$로 나누는 조작 아래에서 그 계수를 그대로 유지하기 때문이며, 이 절에서는 먼저 이 사실과, free module의 depth가 ring의 depth와 같다는 기초적인 관찰을 확립한다.

::: 명제 1
Noetherian local ring $(A,\mathfrak{m})$ 위의 $0$이 아닌 finitely generated free module $F$에 대하여 $\operatorname{depth}F=\operatorname{depth}A$이다.
:::
::: 증명
$F\neq 0$이 finitely generated free이므로 적당한 $r\geq 1$에 대하여 $F\cong A^{\oplus r}$이다. $\kappa=A/\mathfrak{m}$의 projective resolution $P_\bullet$을 하나 고정하면, $\Hom_A(-,-)$이 둘째 변수의 유한한 direct sum과 commute하고 cohomology 또한 유한한 direct sum과 commute하므로, 각각의 $i$에 대하여

$$\Ext_A^i(\kappa,A^{\oplus r})=H^i(\Hom_A(P_\bullet,A^{\oplus r}))=H^i(\Hom_A(P_\bullet,A))^{\oplus r}=\Ext_A^i(\kappa,A)^{\oplus r}$$

이다. $r\geq 1$이므로 $\Ext_A^i(\kappa,A^{\oplus r})=0$인 것은 $\Ext_A^i(\kappa,A)=0$인 것과 동치이다. 그럼 [§Depth, ⁋정리 2](/ko/math/commutative_algebra/depth#thm2)가 주는 표현 $\operatorname{depth}X=\min\{i\mid \Ext_A^i(\kappa,X)\neq 0\}$을 $X=F$와 $X=A$에 각각 적용하여

$$\operatorname{depth}F=\min\{i\mid \Ext_A^i(\kappa,A)^{\oplus r}\neq 0\}=\min\{i\mid \Ext_A^i(\kappa,A)\neq 0\}=\operatorname{depth}A$$

를 얻는다.
:::

특히 $A$가 자기 자신 위의 module로서 갖는 depth는 $0$이 아닌 임의의 free module로 그대로 옮겨지며, 이는 아래 공식의 증명에서 $M$이 free일 때의 경우를 처리한다. 이제 $\mathfrak{m}$의 원소로 나누는 조작이 minimal free resolution과 projective dimension, depth에 미치는 영향을 한꺼번에 정리한다.

::: 보조정리 2
Noetherian local ring $(A,\mathfrak{m})$과 $0$이 아닌 finitely generated $A$-module $M$이 주어졌다 하고, $x\in\mathfrak{m}$이 $A$-regular이면서 동시에 $M$-regular라 하자. $\overline{A}=A/xA$와 $\overline{M}=M/xM$으로 두면, $\overline{A}$는 maximal ideal $\overline{\mathfrak{m}}=\mathfrak{m}/xA$와 residue field $\kappa$를 갖는 Noetherian local ring이고 $\overline{M}\neq 0$은 finitely generated $\overline{A}$-module이며, 다음이 성립한다.

1. $M$의 minimal free resolution $F_\bullet$에 대하여 $F_\bullet\otimes_A\overline{A}$는 $\overline{M}$의 $\overline{A}$ 위 minimal free resolution이다.
2. $\pd_{\overline{A}}\overline{M}=\pd_A M$이다.
3. $\operatorname{depth}_{\overline{A}}\overline{M}=\operatorname{depth}_A M-1$이다.
:::
::: 증명
$x\in\mathfrak{m}$이 non-unit이므로 $xA\neq A$이고, 따라서 $\overline{A}$는 유일한 maximal ideal $\overline{\mathfrak{m}}=\mathfrak{m}/xA$를 갖는 Noetherian local ring이며 그 residue field는 $\overline{A}/\overline{\mathfrak{m}}=A/\mathfrak{m}=\kappa$이다. 또 $x\in\mathfrak{m}$이고 $M\neq 0$이므로 [§정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)에 의하여 $\overline{M}=M/xM\neq 0$이고, 이는 finitely generated $A$-module의 quotient이므로 finitely generated $\overline{A}$-module이다.

(1) $F_\bullet$이 $M$의 projective resolution이므로 [\[호몰로지 대수학\] §Ext와 Tor, ⁋정의 2](/ko/math/homological_algebra/ext_and_tor#def2)에 의하여 $H_i(F_\bullet\otimes_A\overline{A})=\Tor_i^A(M,A/xA)$이다. 여기에 [\[호몰로지 대수학\] §Ext와 Tor, ⁋명제 4](/ko/math/homological_algebra/ext_and_tor#prop4)의 Tor 대칭성을 쓰면 $\Tor_i^A(M,A/xA)\cong\Tor_i^A(A/xA,M)$이고, $x$가 $A$-regular이므로 [§코쥴 복합체, ⁋따름정리 8](/ko/math/commutative_algebra/koszul_complex#cor8)에 의하여 이는 다시 Koszul homology $H_i(x;M)$과 isomorphic하다. 그런데 $x$가 $M$-regular이므로 [§코쥴 복합체, ⁋정리 7](/ko/math/commutative_algebra/koszul_complex#thm7)에 의하여 $i\geq 1$에서 $H_i(x;M)=0$이고, [§코쥴 복합체, ⁋명제 2](/ko/math/commutative_algebra/koszul_complex#prop2)에 의하여 $H_0(x;M)=M/xM=\overline{M}$이다. 따라서 $F_\bullet\otimes_A\overline{A}$는 $i\geq 1$에서 homology가 소멸하고 $H_0$이 $\overline{M}$인 complex, 곧 $\overline{M}$의 $\overline{A}$ 위 free resolution이다. 각 $F_i\otimes_A\overline{A}$는 $F_i$가 finitely generated free $A$-module이므로 finitely generated free $\overline{A}$-module이고, minimality는 $d_i(F_i)\subseteq\mathfrak{m}F_{i-1}$로부터 $(d_i\otimes\id)(F_i\otimes_A\overline{A})\subseteq\mathfrak{m}(F_{i-1}\otimes_A\overline{A})=\overline{\mathfrak{m}}(F_{i-1}\otimes_A\overline{A})$이 따라오므로 보존된다.

(2) [§호몰로지 차원, ⁋명제 10](/ko/math/commutative_algebra/homological_dimension#prop10)에 의하여 minimal free resolution의 계수의 rank는 residue field와의 Tor로 결정된다. 이를 (1)이 준 $\overline{M}$의 minimal free resolution $F_\bullet\otimes_A\overline{A}$에 적용하면

$$\Tor_i^{\overline{A}}(\overline{M},\kappa)\cong(F_i\otimes_A\overline{A})\otimes_{\overline{A}}\kappa\cong F_i\otimes_A\kappa\cong\Tor_i^A(M,\kappa)$$

이므로 $\overline{M}$의 $\overline{A}$ 위 Betti number는 $M$의 $A$ 위 Betti number와 각 차수에서 일치한다. Projective dimension은 [§호몰로지 차원, ⁋명제 11](/ko/math/commutative_algebra/homological_dimension#prop11)에 의하여 residue field와의 Tor가 소멸하지 않는 가장 높은 차수이므로 $\pd_{\overline{A}}\overline{M}=\pd_A M$이다.

(3) 먼저 $\overline{M}$을 $A$-module로 볼 때의 depth와 $\overline{A}$-module로 볼 때의 depth가 일치함을 본다. $A$의 원소 $y\in\mathfrak{m}$이 $\overline{M}$ 위에 유도하는 곱하기 $y$는, $\overline{M}$의 $A$-작용이 $\overline{A}$를 거치므로 그 image $\overline{y}\in\overline{\mathfrak{m}}$이 유도하는 곱하기 $\overline{y}$와 완전히 같다. 그럼 $\mathfrak{m}$의 원소는 그 image를 통해서만 $\overline{M}$에 작용하고 $\mathfrak{m}\to\overline{\mathfrak{m}}$이 surjective이므로, $\overline{\mathfrak{m}}$ 안의 임의의 $\overline{M}$-sequence는 representative를 골라 $\mathfrak{m}$ 안의 것으로 들어올릴 수 있고 거꾸로 $\mathfrak{m}$ 안의 $\overline{M}$-sequence는 image를 취해 $\overline{\mathfrak{m}}$ 안의 것이 된다. 각 단계의 quotient $\overline{M}/(y_1,\ldots,y_j)\overline{M}$과 그 위의 곱하기 작용이 두 관점에서 동일하므로 이 대응은 maximality와 길이를 보존하고, 따라서 $\operatorname{depth}_A\overline{M}=\operatorname{depth}_{\overline{A}}\overline{M}$이다. 마지막으로 $x\in\mathfrak{m}$이 $M$-regular이므로 [§Depth, ⁋따름정리 4](/ko/math/commutative_algebra/depth#cor4)의 둘째 결과를 $I=\mathfrak{m}$에 적용하면 $\operatorname{depth}_A(M/xM)=\operatorname{depth}_A M-1$이고, 종합하면 $\operatorname{depth}_{\overline{A}}\overline{M}=\operatorname{depth}_A M-1$을 얻는다.
:::

## Auslander-Buchsbaum 공식

이제 주된 정리를 증명한다. 증명은 $\operatorname{depth}A$에 대한 귀납법이며, [보조정리 2](#lem2)가 $\operatorname{depth}A$를 하나 줄이는 환원 단계를 제공한다.

::: 정리 3 (Auslander--Buchsbaum)
Noetherian local ring $(A,\mathfrak{m},\kappa)$ 위의 $0$이 아닌 finitely generated $A$-module $M$이 $\pd_A M<\infty$를 만족하면

$$\pd_A M+\operatorname{depth}M=\operatorname{depth}A$$

이 성립한다.
:::
::: 증명
$\delta=\operatorname{depth}A$에 대한 귀납법으로, $\operatorname{depth}A=\delta$인 모든 Noetherian local ring과 그 위의 $\pd<\infty$인 $0$이 아닌 finitely generated module에 대하여 공식이 성립함을 보인다.

$\delta=0$인 경우, 먼저 $\pd_A M=0$임을 보인다. 결론에 반하여 $p=\pd_A M\geq 1$이라 하고 $M$의 minimal free resolution

$$0\rightarrow F_p\overset{d_p}{\longrightarrow} F_{p-1}\rightarrow\cdots\rightarrow F_0\overset{\epsilon}{\longrightarrow} M\rightarrow 0$$

을 택하자. 그 길이가 정확히 $p$인 것은 [§호몰로지 차원, ⁋명제 11](/ko/math/commutative_algebra/homological_dimension#prop11)에 의한 것이다. Resolution의 exactness에 의하여 $d_p$는 injective이고, minimality에 의하여 $d_p(F_p)\subseteq\mathfrak{m}F_{p-1}$이다. 한편 $\operatorname{depth}A=0$이므로 [§Depth, ⁋정리 2](/ko/math/commutative_algebra/depth#thm2)에 의하여 $\Hom_A(\kappa,A)\neq 0$이고, 따라서 $\mathfrak{m}s=0$을 만족하는 $0\neq s\in A$가 존재한다. 그럼

$$d_p(sF_p)=sd_p(F_p)\subseteq s\mathfrak{m}F_{p-1}=(s\mathfrak{m})F_{p-1}=0$$

이므로 $d_p$의 injectivity로부터 $sF_p=0$이다. 그런데 $F_p\neq 0$은 free이므로 $sF_p=0$은 $s=0$을 강제하여 모순이다. 따라서 $\pd_A M=0$이고, 다시 [§호몰로지 차원, ⁋명제 11](/ko/math/commutative_algebra/homological_dimension#prop11)에 의하여 minimal free resolution이 $F_0$에서 끝나 $M\cong F_0$은 free이다. 그럼 [명제 1](#prop1)에 의하여 $\operatorname{depth}M=\operatorname{depth}A$이고, $\pd_A M=0$이므로 공식이 성립한다.

이제 $\delta\geq 1$이라 하고, $\operatorname{depth}$가 $\delta-1$인 모든 Noetherian local ring에 대하여 공식이 성립한다고 가정하자. $M$의 depth에 따라 두 경우로 나눈다.

먼저 $\operatorname{depth}M\geq 1$인 경우를 다룬다. $A$의 zerodivisor 전체는 $\bigcup_{\mathfrak{p}\in\Ass A}\mathfrak{p}$이고 $M$의 zerodivisor 전체는 $\bigcup_{\mathfrak{p}\in\Ass M}\mathfrak{p}$이다. ([§동반소아이디얼, ⁋정리 7](/ko/math/commutative_algebra/associated_primes#thm7)) $\operatorname{depth}A\geq 1$과 $\operatorname{depth}M\geq 1$이므로 [§Depth, ⁋따름정리 4](/ko/math/commutative_algebra/depth#cor4)의 첫째 결과에 의하여 $\mathfrak{m}$은 $\Ass A$의 어떤 원소에도, $\Ass M$의 어떤 원소에도 포함되지 않는다. $\Ass A$와 $\Ass M$은 유한집합이므로 ([§동반소아이디얼, ⁋정리 7](/ko/math/commutative_algebra/associated_primes#thm7)) [§동반소아이디얼, ⁋보조정리 2](/ko/math/commutative_algebra/associated_primes#lem2)에 의하여 $\mathfrak{m}\subseteq\bigcup_{\mathfrak{p}\in\Ass A\cup\Ass M}\mathfrak{p}$일 수 없고, 따라서 $\Ass A\cup\Ass M$의 어떤 prime에도 속하지 않는 $x\in\mathfrak{m}$이 존재한다. 이러한 $x$는 $A$-regular이면서 $M$-regular이다.

[보조정리 2](#lem2)를 이 $x$에 적용하면 $\overline{A}=A/xA$와 $\overline{M}=M/xM$에 대하여 $\pd_{\overline{A}}\overline{M}=\pd_A M<\infty$이고 $\operatorname{depth}_{\overline{A}}\overline{M}=\operatorname{depth}M-1$이며, 같은 보조정리를 $M=A$의 경우에 적용하면 $\operatorname{depth}\overline{A}=\operatorname{depth}A-1=\delta-1$이다. $\operatorname{depth}\overline{A}=\delta-1$이므로 귀납적 가정을 $\overline{A}$ 위의 $\overline{M}$에 적용하여

$$\pd_A M+(\operatorname{depth}M-1)=\pd_{\overline{A}}\overline{M}+\operatorname{depth}_{\overline{A}}\overline{M}=\operatorname{depth}\overline{A}=\operatorname{depth}A-1$$

을 얻고, 양변에 $1$을 더하면 $\pd_A M+\operatorname{depth}M=\operatorname{depth}A$이다.

다음으로 $\operatorname{depth}M=0$인 경우를 다룬다. 만일 $M$이 free라면 [명제 1](#prop1)에 의하여 $\operatorname{depth}M=\operatorname{depth}A=\delta\geq 1$이 되어 $\operatorname{depth}M=0$에 모순이므로 $M$은 free가 아니고, 따라서 $\pd_A M\geq 1$이다. $M$의 minimal free resolution의 첫 단계에서 얻어지는 short exact sequence

$$0\rightarrow M'\rightarrow F_0\overset{\epsilon}{\longrightarrow} M\rightarrow 0,\qquad M'=\ker\epsilon$$

을 생각하자. Minimality에 의하여 $M'\subseteq\mathfrak{m}F_0$이고, $M$이 free가 아니므로 $M'\neq 0$이다. Resolution의 나머지 $\cdots\rightarrow F_2\rightarrow F_1\rightarrow M'\rightarrow 0$은 $M'$의 minimal free resolution이므로 $\pd_A M'=\pd_A M-1$이다.

이제 [§Depth, ⁋명제 10](/ko/math/commutative_algebra/depth#prop10)의 부등식들을 이 short exact sequence에 적용한다. $F_0$은 free이므로 [명제 1](#prop1)에 의하여 $\operatorname{depth}F_0=\operatorname{depth}A=\delta$이다. 둘째 부등식에서

$$\operatorname{depth}M'\geq\min(\operatorname{depth}F_0,\operatorname{depth}M+1)=\min(\delta,1)=1$$

이고, 셋째 부등식에서

$$0=\operatorname{depth}M\geq\min(\operatorname{depth}M'-1,\operatorname{depth}F_0)=\min(\operatorname{depth}M'-1,\delta)$$

인데 $\delta\geq 1>0$이므로 이 최솟값은 $\operatorname{depth}M'-1$이어야 하고, 따라서 $\operatorname{depth}M'\leq 1$이다. 종합하면 $\operatorname{depth}M'=1$이다.

$\operatorname{depth}M'=1\geq 1$이므로 앞의 경우의 논증을 $M'$에 적용할 수 있다. 그 논증은 depth가 $\delta-1$인 ring에 대한 귀납적 가정만을 사용하고 지금 증명하는 depth $\delta$에서의 주장을 끌어오지 않으므로, $M'$에 적용하는 것은 순환이 아니다. 그럼 $\pd_A M'+\operatorname{depth}M'=\operatorname{depth}A$이고, $\pd_A M'=\pd_A M-1$과 $\operatorname{depth}M'=1$, $\operatorname{depth}M=0$을 대입하면

$$\pd_A M+\operatorname{depth}M=(\pd_A M'+1)+0=\operatorname{depth}A$$

을 얻는다.
:::

공식은 $\pd_A M\geq 0$과 결합하여 $\operatorname{depth}M\leq\operatorname{depth}A$를 즉시 주며, [§Depth, ⁋따름정리 8](/ko/math/commutative_algebra/depth#cor8)의 $\operatorname{depth}A\leq\dim A$와 종합하면 finite projective dimension을 갖는 module은 언제나 $\operatorname{depth}M\leq\operatorname{depth}A\leq\dim A$를 만족한다. 한편 $\pd_A M<\infty$라는 가정은 공식이 성립하기 위한 필수 조건이며, 이를 떼어내면 [예시 7](#ex7)에서 보듯 등식이 깨진다. 공식의 첫 응용으로 projective dimension의 크기와, depth가 $0$일 때의 경직성을 얻는다.

::: 따름정리 4
Noetherian local ring $(A,\mathfrak{m})$에 대하여 다음이 성립한다.

1. $0$이 아닌 finitely generated $A$-module $M$이 $\pd_A M<\infty$이면 $\pd_A M\leq\operatorname{depth}A$이다.
2. $\operatorname{depth}A=0$이면 $\pd_A M<\infty$인 $0$이 아닌 finitely generated $A$-module $M$은 모두 free이다. 특히 Artinian local ring 위에서 finite projective dimension을 갖는 module은 모두 free이다.
:::
::: 증명
첫째 결과는 [정리 3](#thm3)과 $\operatorname{depth}M\geq 0$으로부터 $\pd_A M=\operatorname{depth}A-\operatorname{depth}M\leq\operatorname{depth}A$이다. 둘째 결과의 경우, $\operatorname{depth}A=0$이면 첫째 결과에 의하여 $\pd_A M\leq 0$, 곧 $\pd_A M=0$이므로 [§호몰로지 차원, ⁋명제 11](/ko/math/commutative_algebra/homological_dimension#prop11)에 의하여 minimal free resolution이 $F_0$에서 끝나 $M\cong F_0$은 free이다. Artinian local ring $(A,\mathfrak{m})$은 [§조르단-횔더 정리, ⁋정리 4](/ko/math/commutative_algebra/Jordan-Holder_theorem#thm4)에 의하여 모든 prime ideal이 maximal이므로 $\dim A=0$이고, [§Depth, ⁋따름정리 8](/ko/math/commutative_algebra/depth#cor8)에 의하여 $\operatorname{depth}A\leq\dim A=0$이 되어 앞의 경우에 해당한다.
:::

Regular local ring에서는 모든 module이 finite projective dimension을 가지므로 공식이 아무런 유한성 가정 없이 적용되고, projective dimension이 depth만으로 완전히 결정된다.

::: 따름정리 5
$d$차원 regular local ring $(A,\mathfrak{m})$ 위의 $0$이 아닌 finitely generated $A$-module $M$은 언제나 $\pd_A M<\infty$이고

$$\pd_A M=d-\operatorname{depth}M$$

이다. 특히 $M$이 Cohen--Macaulay module이면 $\pd_A M=d-\dim M$이다.
:::
::: 증명
[§호몰로지 차원, ⁋명제 13](/ko/math/commutative_algebra/homological_dimension#prop13)에 의하여 $\operatorname{gldim}A=d$이므로 임의의 $M$에 대하여 $\pd_A M\leq d<\infty$이다. 또 $A$는 [§Cohen-Macaulay 환, ⁋따름정리 5](/ko/math/commutative_algebra/cohen_macaulay_rings#cor5)에 의하여 Cohen--Macaulay이므로 $\operatorname{depth}A=\dim A=d$이고, [정리 3](#thm3)에 의하여 $\pd_A M=\operatorname{depth}A-\operatorname{depth}M=d-\operatorname{depth}M$이다. $M$이 Cohen--Macaulay module이면 [§Cohen-Macaulay 환, ⁋정의 1](/ko/math/commutative_algebra/cohen_macaulay_rings#def1)에 의하여 $\operatorname{depth}M=\dim M$이므로 $\pd_A M=d-\dim M$을 얻는다.
:::

## 예시

첫 예시는 공식을 구체적인 module에 대해 확인하고, 그 값을 depth의 직접 계산과 대조한다.

::: 예시 6
Field $\mathbb{K}$에 대하여 $2$차원 regular local ring $A=\mathbb{K}[[\x,\y]]$와 그 maximal ideal $\mathfrak{m}=(\x,\y)$를 생각하자. $A$는 integral domain이므로 곱하기 $\x$는 $A$ 위에서 injective이고, $A/(\x)\cong\mathbb{K}[[\y]]$에서 $\y$의 image가 non-zerodivisor이므로 $\x,\y$는 $A$-sequence이다. 따라서 [§코쥴 복합체, ⁋따름정리 8](/ko/math/commutative_algebra/koszul_complex#cor8)에 의하여 Koszul complex $K(\x,\y)$는 $A/\mathfrak{m}=\kappa$의 free resolution이며, 그 첫 syzygy를 떼면 다음의 exact sequence

$$0\rightarrow A\overset{d_2}{\longrightarrow} A^{\oplus 2}\overset{d_1}{\longrightarrow}\mathfrak{m}\rightarrow 0,\qquad d_2(1)=(-\y,\x),\quad d_1(a,b)=a\x+b\y$$

을 얻는다. 두 differential의 성분이 모두 $\mathfrak{m}$에 속하므로 이는 $\mathfrak{m}$의 minimal free resolution이고, $F_2=0$이므로 $\pd_A\mathfrak{m}=1$이다. $A$가 regular local ring이라 $\operatorname{depth}A=\dim A=2$이므로 [정리 3](#thm3)에 의하여

$$\operatorname{depth}\mathfrak{m}=\operatorname{depth}A-\pd_A\mathfrak{m}=2-1=1$$

이다.

이를 직접 확인해 보자. $A$가 domain이고 $\mathfrak{m}\subseteq A$이므로 곱하기 $\x$는 $\mathfrak{m}$ 위에서 injective이고, [§Depth, ⁋따름정리 4](/ko/math/commutative_algebra/depth#cor4)의 둘째 결과에 의하여 $\operatorname{depth}\mathfrak{m}=\operatorname{depth}(\mathfrak{m}/\x\mathfrak{m})+1$이다. $\mathfrak{m}/\x\mathfrak{m}$에서 $\x$의 class를 $\overline{\x}$라 하면, $\x\in\x\mathfrak{m}=(\x^2,\x\y)$일 경우 $\x=\x(a\x+b\y)$로부터 domain에서 $1=a\x+b\y\in\mathfrak{m}$이 되어 모순이므로 $\overline{\x}\neq 0$이다. 한편 $\x\cdot\overline{\x}=\x^2\in\x\mathfrak{m}$과 $\y\cdot\overline{\x}=\x\y\in\x\mathfrak{m}$으로부터 $\mathfrak{m}\overline{\x}=0$이므로 $\ann(\overline{\x})=\mathfrak{m}$이 되어 $\mathfrak{m}\in\Ass(\mathfrak{m}/\x\mathfrak{m})$이다. 따라서 [§Depth, ⁋따름정리 4](/ko/math/commutative_algebra/depth#cor4)의 첫째 결과에 의하여 $\operatorname{depth}(\mathfrak{m}/\x\mathfrak{m})=0$이고, $\operatorname{depth}\mathfrak{m}=0+1=1$로 공식과 부합한다.
:::

다음 예시는 $\pd_A M<\infty$라는 가정을 떼면 공식이 실패한다는 것을, projective dimension이 infinite module로 보여준다.

::: 예시 7
Field $\mathbb{K}$에 대하여 $A=\mathbb{K}[[\x,\y]]/(\x\y)$를 생각하자. 이는 [§Depth, ⁋예시 11](/ko/math/commutative_algebra/depth#ex11)에서 살펴본 것처럼 $\operatorname{depth}A=1=\dim A$인 Cohen--Macaulay local ring이다. $\x,\y$의 image를 각각 $\overline{\x},\overline{\y}$로 적고 $M=A/(\overline{\x})$를 생각하자.

$A$에서 곱하기 $\overline{\x}$의 kernel을 계산한다. $f\in\mathbb{K}[[\x,\y]]$에 대하여 $\x f\in(\x\y)$인 것은 $\x f=\x\y g$인 $g$가 존재하는 것, 곧 domain에서 $\x$를 소거하여 $f\in(\y)$인 것과 동치이다. 따라서 $\ker(\cdot\overline{\x})=(\overline{\y})$이고, 같은 계산으로 $\ker(\cdot\overline{\y})=(\overline{\x})$이다. $\epsilon:A\rightarrow M$의 kernel이 $\overline{\x}A=(\overline{\x})$이므로 이 kernel들의 계산을 이어 붙이면 주기 $2$의 free resolution

$$\cdots\overset{\cdot\overline{\y}}{\longrightarrow}A\overset{\cdot\overline{\x}}{\longrightarrow}A\overset{\cdot\overline{\y}}{\longrightarrow}A\overset{\cdot\overline{\x}}{\longrightarrow}A\overset{\epsilon}{\longrightarrow}M\rightarrow 0$$

을 얻는다. 모든 differential이 $\overline{\x}$ 또는 $\overline{\y}$의 곱하기이고 이들은 $\mathfrak{m}=(\overline{\x},\overline{\y})$에 속하므로 이 resolution은 minimal이며, 모든 $i$에서 $F_i=A\neq 0$이라 Betti number가 전부 $1$이다. 따라서 [§호몰로지 차원, ⁋명제 11](/ko/math/commutative_algebra/homological_dimension#prop11)에 의하여 $\pd_A M=\infty$이다.

한편 $M=A/(\overline{\x})\cong\mathbb{K}[[\x,\y]]/(\x\y,\x)=\mathbb{K}[[\x,\y]]/(\x)\cong\mathbb{K}[[\y]]$는 $1$차원 integral domain이고 그 위에서 곱하기 $\overline{\y}$가 injective이므로 $\operatorname{depth}_A M\geq 1$이며, [§Depth, ⁋따름정리 8](/ko/math/commutative_algebra/depth#cor8)에 의하여 $\operatorname{depth}M\leq\dim M=1$이므로 $\operatorname{depth}M=1$이다. 만일 [정리 3](#thm3)의 공식이 $M$에 대해 성립한다면 $\pd_A M=\operatorname{depth}A-\operatorname{depth}M=1-1=0$이 되어 $M$이 free여야 한다. 그러나 $\overline{\x}\neq 0$이 $\ann_A(M)=(\overline{\x})$의 원소이므로 $M$의 annihilator는 $0$이 아니고, $A\neq 0$인 free module의 annihilator는 $0$이므로 $M$은 free가 아니다. 이 모순은 $\pd_A M<\infty$라는 가정이 공식에서 생략될 수 없음을 보여준다.
:::

모든 finitely generated module이 finite projective dimension을 갖는 Noetherian local ring이 정확히 regular local ring이라는 특징화가 다음 글의 주제이다.

---

**참고문헌**

**[BH]** W. Bruns, J. Herzog. *Cohen-Macaulay Rings*. Cambridge University Press, 1993.  
**[Eis]** David Eisenbud. *Commutative Algebra: with a view toward algebraic geometry*. Springer, 1995.  
**[Mat]** Hideyuki Matsumura. *Commutative Ring Theory*. Cambridge University Press, 1986.  
**[Wei]** Charles A. Weibel. *An Introduction to Homological Algebra*. Cambridge University Press, 1994.

---
