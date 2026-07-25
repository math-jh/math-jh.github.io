---
title: "단사가군과 Matlis 쌍대성"
description: "Noetherian ring 위에서 injective module을 essential extension과 injective hull로 분석하여 indecomposable injective를 prime마다의 injective hull로 분류하고, local ring에서 injective dimension을 residue field와의 Ext로 읽어낸 뒤 Matlis duality를 확립한다."
excerpt: "Injective hull의 구조론과 Matlis duality"

categories: [Math / Commutative Algebra]
permalink: /ko/math/commutative_algebra/matlis_duality
sidebar: 
    nav: "commutative_algebra-ko"

date: 2026-07-24
weight: 31
published: false
drift_needed: true

---

우리는 이미 임의의 $A$-module이 injective module에 embed된다는 것을 알고 있다. ([\[호몰로지 대수학\] §분해, ⁋명제 5](/ko/math/homological_algebra/resolutions#prop5)) 그러나 이 embedding은 크기에 대한 아무런 통제가 없어, 주어진 module을 가장 경제적으로 담는 injective module이 무엇인지는 말해주지 않는다. 이 글에서 우리는 먼저 그러한 최소의 injective embedding인 injective hull을 essential extension의 언어로 세운다. 이어 $A$가 Noetherian일 때 injective hull이 prime ideal마다 하나씩 대응되는 indecomposable injective module들의 direct sum으로 모든 injective module을 분해한다는 Matlis의 구조정리를 증명하고, Noetherian local ring에서 injective dimension을 residue field와의 $\Ext$로 읽어내는 판정을 얻는다. 마지막으로 residue field의 injective hull이 completion과 맞물리는 Matlis duality를 확립한다.

## Essential extension과 injective hull

임의의 $A$-module $M$은 어떤 injective module에 포함되지만, 그러한 injective module 가운데 가장 작은 것을 고를 수 있는지가 문제이다. 이를 재기 위해 우리는 포함관계가 module의 정보를 잃지 않는 상황을 정식화한다.

::: 정의 1
$A$-module $E$와 그 submodule $M\subseteq E$에 대하여, $M$이 $E$의 *essential submodule*이라는 것, 곧 $E$가 $M$의 *essential extension*이라는 것은 $E$의 $0$이 아닌 임의의 submodule $N$이 $M$과 자명하지 않게 만나는 것, 즉
$$0\neq N\subseteq E\implies N\cap M\neq 0$$
이 성립하는 것이다.
:::

이 조건은 $E$의 어떤 원소도 $M$으로부터 완전히 떨어져 있지 않다는 것을 뜻한다. $0\neq x\in E$이면 cyclic submodule $Ax$가 $M$과 만나므로, 적당한 $a\in A$에 대하여 $0\neq ax\in M$이 성립한다. 정의로부터 몇 가지 기본 성질이 바로 따라온다. $M\subseteq E$가 essential이고 $M\subseteq F\subseteq E$인 중간 module $F$가 주어지면, $F$의 $0$이 아닌 submodule은 $E$의 submodule로서 $M$과 만나므로 $M\subseteq F$가 essential이고, 또 $E$의 $0$이 아닌 submodule $N$은 $N\cap M\subseteq N\cap F$를 통해 $F$와 만나므로 $F\subseteq E$도 essential이다. 거꾸로 $M\subseteq F$와 $F\subseteq E$가 모두 essential이면, $E$의 $0$이 아닌 submodule $N$에 대하여 $N\cap F\neq 0$이고 다시 $(N\cap F)\cap M\neq 0$이므로 $M\subseteq E$ 또한 essential이다. 즉 essential성은 중간 단계에 대하여 전이적이다.

Injective module은 이 개념을 통해 내부적으로 특징지어진다.

::: 보조정리 2
$A$-module $E$가 injective인 것은 $E$가 자기 자신 외의 essential extension을 갖지 않는 것, 곧 $E\subseteq F$가 essential extension이면 항상 $F=E$인 것과 동치이다.
:::
::: 증명
$E$가 injective라 하고 $E\subseteq F$가 essential extension이라 하자. Injective module의 정의에 의하여 identity $\id_E:E\rightarrow E$는 inclusion $E\hookrightarrow F$를 따라 $r:F\rightarrow E$로 확장되며, $r$을 $E$에 제한하면 $\id_E$이므로 $F=E\oplus\ker r$이다. 그럼 $\ker r$은 $E$와 $0$으로 만나는 submodule인데, $E\subseteq F$가 essential이므로 $\ker r=0$, 곧 $F=E$이다.

거꾸로 $E$가 proper essential extension을 갖지 않는다 하자. [\[호몰로지 대수학\] §분해, ⁋명제 5](/ko/math/homological_algebra/resolutions#prop5)에 의하여 injective module $I$와 embedding $E\hookrightarrow I$가 존재한다. 이제 $N\cap E=0$을 만족하는 $I$의 submodule $N$들의 모임을 생각하면, 이는 포함관계에 대하여 inductive하므로 [\[집합론\] §선택공리, ⁋정리 4](/ko/math/set_theory/axiom_of_choice#thm4)에 의하여 maximal인 $N$이 존재한다. 합성 $E\hookrightarrow I\rightarrow I/N$은 kernel이 $E\cap N=0$이므로 embedding이고, 우리는 $E\subseteq I/N$이 essential임을 주장한다. $I/N$의 $0$이 아닌 submodule은 $N\subsetneq L$인 $L$에 대하여 $L/N$ 꼴인데, $N$의 maximality에 의하여 $L\cap E\neq 0$이고, $0\neq e\in L\cap E$는 $E\cap N=0$으로부터 $e\notin N$이므로 $I/N$에서 $0$이 아닌 상을 가지며 이 상은 $(L/N)\cap E$에 속한다. 따라서 $E\subseteq I/N$은 essential이고, 가정에 의하여 이 essential extension은 자명해야 하므로 $E=I/N$이다. 이는 $I=E\oplus N$을 뜻하여 $E$가 injective module $I$의 direct summand이 되므로, $\Hom_A(-,I)\cong\Hom_A(-,E)\oplus\Hom_A(-,N)$의 좌변이 exact인 것으로부터 그 direct factor $\Hom_A(-,E)$ 또한 exact이고, 곧 $E$는 injective이다.
:::

위 증명의 마지막 논증은 injective module의 direct summand이 다시 injective라는 사실을 담고 있으며, 앞으로 여러 번 쓰인다. 이제 [보조정리 2](#lem2)를 이용하여 임의의 module을 담는 최소의 injective module을 만든다.

::: 정리 3
임의의 $A$-module $M$에 대하여, $M$의 essential extension이면서 injective인 module $E(M)$이 존재하며, $M$을 고정하는 isomorphism을 제외하면 유일하다. 이를 $M$의 *injective hull*이라 부른다.
:::
::: 증명
존재성을 보이자. [\[호몰로지 대수학\] §분해, ⁋명제 5](/ko/math/homological_algebra/resolutions#prop5)에 의하여 injective module $I$와 embedding $M\hookrightarrow I$를 택한다. $M\subseteq E\subseteq I$이면서 $M\subseteq E$가 essential인 submodule $E$들의 모임을 생각하면, 이러한 essential extension들의 chain의 합집합은 다시 essential extension이므로 (합집합의 $0$이 아닌 원소는 chain의 한 항에 속하고 그곳에서 $M$과 만난다) 이 모임은 inductive하고, [\[집합론\] §선택공리, ⁋정리 4](/ko/math/set_theory/axiom_of_choice#thm4)에 의하여 maximal인 essential extension $E\subseteq I$가 존재한다.

$E$가 proper essential extension을 갖지 않음을 보이면 [보조정리 2](#lem2)에 의하여 $E$가 injective가 된다. $E\subseteq F$가 essential extension이라 하자. $I$가 injective이므로 inclusion $E\hookrightarrow I$는 $E\hookrightarrow F$를 따라 $\varphi:F\rightarrow I$로 확장되며, $\ker\varphi$는 $E$와 $0$으로 만나 essential성에 의하여 $0$이므로 $\varphi$는 embedding이다. 그럼 $M\subseteq E\subseteq\varphi(F)$인데 $M\subseteq E$가 essential이고 $E\subseteq\varphi(F)$가 essential이므로 (뒤의 것은 $E\subseteq F$의 essential성을 $\varphi$로 옮긴 것이다) $M\subseteq\varphi(F)$는 $I$ 안의 essential extension이고, $E$의 maximality에 의하여 $\varphi(F)=E$, 곧 $F=E$이다. 따라서 $E$는 injective이며 $M$의 essential extension이다.

유일성을 보이자. $E,E'$이 모두 $M$의 injective hull이라 하자. $E'$이 injective이므로 inclusion $M\hookrightarrow E'$은 $M\hookrightarrow E$를 따라 $\phi:E\rightarrow E'$로 확장되고, $\ker\phi$는 $M$과 $0$으로 만나 $M\subseteq E$의 essential성에 의하여 $0$이므로 $\phi$는 embedding이다. $\phi(E)\cong E$는 injective이므로 $E'$의 direct summand이어서 $E'=\phi(E)\oplus C$인 $C$가 있는데, $M\subseteq\phi(E)$이고 $C\cap\phi(E)=0$이므로 $C\cap M=0$이며, $M\subseteq E'$의 essential성에 의하여 $C=0$이다. 따라서 $\phi:E\rightarrow E'$은 $M$을 고정하는 isomorphism이다.
:::

Injective hull $E(M)$은 $M$을 담는 injective module 가운데 가장 작은 것으로, $M\hookrightarrow E(M)$이 essential이라는 것이 그 최소성을 표현한다. 이후 우리의 관심은 $A$가 Noetherian일 때 이 injective hull들이 injective module 전체를 조립하는 벽돌이 된다는 데 있다. 그 조립에는 injective module의 무한 direct sum이 다시 injective라는 성질이 필요하며, 이는 정확히 Noetherian 조건에서 성립한다.

::: 명제 4
$A$가 Noetherian ring이면, 임의의 (무한할 수 있는) 집합의 injective $A$-module들의 direct sum은 injective이다.
:::
::: 증명
injective module들의 족 $(E_\lambda)_{\lambda\in\Lambda}$을 고정하고 $E=\bigoplus_\lambda E_\lambda$라 하자. [§호몰로지 차원, ⁋보조정리 4](/ko/math/commutative_algebra/homological_dimension#lem4)에 의하여, $A$의 임의의 ideal $I$와 $A$-linear map $f:I\rightarrow E$가 $A$로 확장됨을 보이면 충분하다. $A$가 Noetherian이므로 $I$는 유한히 많은 원소 $a_1,\ldots,a_r$로 생성되고 ([§기본 개념들, ⁋정리 3](/ko/math/commutative_algebra/basic_notions#thm3)), 각 $f(a_i)$는 유한한 첨자에서만 $0$이 아닌 성분을 가지므로 그 상 $f(I)$는 적당한 유한 부분집합 $F\subseteq\Lambda$에 대하여 $\bigoplus_{\lambda\in F}E_\lambda$에 들어간다. 유한 direct sum $\bigoplus_{\lambda\in F}E_\lambda$은 injective module들의 유한 direct sum이므로 injective이고, 따라서 $f:I\rightarrow\bigoplus_{\lambda\in F}E_\lambda$은 $\tilde{f}:A\rightarrow\bigoplus_{\lambda\in F}E_\lambda$로 확장된다. 이를 $E$로의 inclusion과 합성하면 $f$의 $A$로의 확장을 얻는다.
:::

## Noetherian 환 위의 indecomposable 단사가군

이하 이 절과 다음 절에서 $A$는 Noetherian ring이다. 우리는 각 prime ideal $\mathfrak{p}$가 하나의 injective hull $E(A/\mathfrak{p})$를 낳으며, 이들이 더 이상 쪼갤 수 없는 벽돌임을 본다. 그 열쇠는 essential extension이 associated prime을 보존한다는 관찰이다.

::: 보조정리 5
Noetherian ring $A$의 prime ideal $\mathfrak{p}$에 대하여, injective hull $E(A/\mathfrak{p})$는 $\Ass E(A/\mathfrak{p})=\{\mathfrak{p}\}$를 만족하며 indecomposable이다.
:::
::: 증명
먼저 essential extension $M\subseteq E$에 대하여 $\Ass E=\Ass M$임을 보인다. [§동반소아이디얼, ⁋보조정리 5](/ko/math/commutative_algebra/associated_primes#lem5)에 의하여 $\Ass M\subseteq\Ass E$이므로 반대 포함을 보이면 된다. $\mathfrak{q}\in\Ass E$이면 $\ann(x)=\mathfrak{q}$인 $x\in E$가 있어 $Ax\cong A/\mathfrak{q}$이다. $Ax\neq 0$이고 $M\subseteq E$가 essential이므로 $Ax\cap M\neq 0$이고, $0\neq y\in Ax\cap M$을 택하면 $Ax\cong A/\mathfrak{q}$가 integral domain이므로 그 $0$이 아닌 원소 $y$의 annihilator는 $\ann(y)=\mathfrak{q}$이다. 그럼 $y\in M$으로부터 $\mathfrak{q}\in\Ass M$이므로 $\Ass E\subseteq\Ass M$이다.

이제 $A/\mathfrak{p}$가 integral domain이므로 그 $0$이 아닌 임의의 원소의 annihilator가 $\mathfrak{p}$임에서 $\Ass(A/\mathfrak{p})=\{\mathfrak{p}\}$이고, $A/\mathfrak{p}\subseteq E(A/\mathfrak{p})$가 essential extension이므로 방금 보인 것에 의하여 $\Ass E(A/\mathfrak{p})=\{\mathfrak{p}\}$이다.

Indecomposability를 보이자. $E(A/\mathfrak{p})=E_1\oplus E_2$이고 $E_1,E_2$가 모두 $0$이 아니라 하자. $A/\mathfrak{p}\subseteq E(A/\mathfrak{p})$가 essential이므로 $E_1\cap(A/\mathfrak{p})$와 $E_2\cap(A/\mathfrak{p})$는 모두 $0$이 아니다. 이 둘은 domain $A/\mathfrak{p}$의 $0$이 아닌 ideal이므로 그 곱이 $0$이 아니고, 곱은 교집합에 포함되므로 $\left(E_1\cap(A/\mathfrak{p})\right)\cap\left(E_2\cap(A/\mathfrak{p})\right)\neq 0$이다. 그런데 이 교집합은 $E_1\cap E_2=0$에 들어가므로 모순이다. 따라서 $E(A/\mathfrak{p})$는 indecomposable이다.
:::

$\Ass E(A/\mathfrak{p})=\{\mathfrak{p}\}$는 서로 다른 prime에서 나온 injective hull들이 서로 isomorphic하지 않음을 뜻한다. 이제 이들이 모든 injective module을 남김없이 조립한다.

::: 정리 6 (Matlis 구조정리)
Noetherian ring $A$ 위의 임의의 injective module $E$는 적당한 prime ideal들의 족 $(\mathfrak{p}_\lambda)_{\lambda\in\Lambda}$에 대하여
$$E\cong\bigoplus_{\lambda\in\Lambda}E(A/\mathfrak{p}_\lambda)$$
로 분해된다.
:::
::: 증명
$E=0$이면 빈 족으로 자명하므로 $E\neq 0$이라 하자. 먼저 $0$이 아닌 $A$-module $C$에 대하여 $\Ass C\neq\emptyset$임을 관찰한다. $0\neq x\in C$을 택하면 $Ax\cong A/\ann(x)$는 $0$이 아닌 finitely generated module이므로 [§동반소아이디얼, ⁋정리 7](/ko/math/commutative_algebra/associated_primes#thm7)에 의하여 $\Ass(Ax)\neq\emptyset$이고, [§동반소아이디얼, ⁋보조정리 5](/ko/math/commutative_algebra/associated_primes#lem5)에 의하여 $\Ass(Ax)\subseteq\Ass C$이다. 또, $C$가 injective이고 $\mathfrak{q}\in\Ass C$이면 embedding $A/\mathfrak{q}\hookrightarrow C$를 essential extension $A/\mathfrak{q}\subseteq E(A/\mathfrak{q})$를 따라 $E(A/\mathfrak{q})\rightarrow C$로 확장할 수 있고, 이 확장의 kernel은 $A/\mathfrak{q}$와 $0$으로 만나 essential성에 의하여 $0$이므로 $E(A/\mathfrak{q})\hookrightarrow C$를 얻는다.

이제 $E$의 submodule들의 족 $(F_\lambda)_{\lambda\in\Lambda}$ 가운데, 각 $F_\lambda$가 어떤 prime $\mathfrak{p}_\lambda$에 대하여 $F_\lambda\cong E(A/\mathfrak{p}_\lambda)$이고 이들의 합이 direct sum $\bigoplus_\lambda F_\lambda$을 이루는 것들의 모임 $\mathcal{S}$를 생각한다. direct sum을 이룬다는 조건은 유한 개의 성분들 사이의 조건이므로 $\mathcal{S}$의 chain의 합집합에서도 유지되어 $\mathcal{S}$는 inductive하고, 위의 관찰에서 얻은 $E(A/\mathfrak{p})\hookrightarrow E$ 하나로 이루어진 족이 $\mathcal{S}$에 속하므로 $\mathcal{S}$는 공집합이 아니다. [\[집합론\] §선택공리, ⁋정리 4](/ko/math/set_theory/axiom_of_choice#thm4)에 의하여 maximal인 족 $(F_\lambda)_{\lambda\in\Lambda}$이 존재하고, $S=\bigoplus_\lambda F_\lambda\subseteq E$라 하자.

[명제 4](#prop4)에 의하여 $S$는 injective이므로 inclusion $S\hookrightarrow E$은 split하여 $E=S\oplus C$인 submodule $C$가 존재한다. 만일 $C\neq 0$이라면 위의 관찰에 의하여 $\mathfrak{q}\in\Ass C$가 존재하고, $C$는 injective module $E$의 direct summand이므로 injective이어서 embedding $E(A/\mathfrak{q})\hookrightarrow C$를 얻는다. $E=S\oplus C$이므로 $S\cap E(A/\mathfrak{q})\subseteq S\cap C=0$이고, 따라서 족 $(F_\lambda)_\lambda$에 $E(A/\mathfrak{q})$를 덧붙인 것도 $\mathcal{S}$에 속하여 maximality에 모순이다. 그러므로 $C=0$이고 $E=S=\bigoplus_\lambda E(A/\mathfrak{p}_\lambda)$이다.
:::

## Local ring 위의 단사차원 판정

이 절에서 $(A,\mathfrak{m},\kappa)$는 residue field $\kappa=A/\mathfrak{m}$을 갖는 Noetherian local ring이고 $M\neq 0$은 finitely generated $A$-module이다. [§호몰로지 차원, ⁋명제 11](/ko/math/commutative_algebra/homological_dimension#prop11)에서 우리는 finitely generated module의 projective dimension이 오직 residue field와의 $\Tor$로 통제됨을 보았다. 다음 명제는 이에 정확히 대응하는, injective dimension을 residue field로 읽어내는 판정이다.

::: 명제 7
Noetherian local ring $(A,\mathfrak{m},\kappa)$ 위의 $0$이 아닌 finitely generated $A$-module $M$에 대하여
$$\operatorname{injdim}_A M=\sup\{i\mid\Ext_A^i(\kappa,M)\neq 0\}$$
이 성립한다.
:::
::: 증명
$s=\sup\{i\mid\Ext_A^i(\kappa,M)\neq 0\}$으로 둔다.

먼저 $s\leq\operatorname{injdim}_A M$을 보인다. $\operatorname{injdim}_A M=m<\infty$이라 하면 [§호몰로지 차원, ⁋명제 3](/ko/math/commutative_algebra/homological_dimension#prop3)에 의하여 모든 $A$-module $N$과 $i>m$에 대하여 $\Ext_A^i(N,M)=0$이고, 특히 $N=\kappa$에서 $\Ext_A^i(\kappa,M)=0$이 $i>m$에서 성립하므로 $s\leq m$이다. 따라서 $s\leq\operatorname{injdim}_A M$이며, 이로부터 $s=\infty$인 경우에는 $\operatorname{injdim}_A M=\infty$가 되어 등식이 성립한다.

이제 $s=n<\infty$이라 하고 $\operatorname{injdim}_A M\leq n$을 보인다. [§호몰로지 차원, ⁋따름정리 5](/ko/math/commutative_algebra/homological_dimension#cor5)에 의하여 $A$의 모든 ideal $I$에 대하여 $\Ext_A^{n+1}(A/I,M)=0$임을 보이면 충분하다. 우리는 우선 다음 주장을 보인다.

> $A$의 임의의 prime ideal $\mathfrak{p}$와 임의의 $j>n$에 대하여 $\Ext_A^j(A/\mathfrak{p},M)=0$이다.

이를 위해, 적당한 $j>n$에 대하여 $\Ext_A^j(A/\mathfrak{p},M)\neq 0$인 prime $\mathfrak{p}$들의 모임 $\mathcal{T}$가 공집합임을 보인다. $\mathcal{T}\neq\emptyset$이라 가정하면, $A$가 Noetherian이므로 $\mathcal{T}$는 포함관계에 대한 maximal element $\mathfrak{p}_0$을 갖는다. ([§기본 개념들, ⁋정리 3](/ko/math/commutative_algebra/basic_notions#thm3)) 만일 $\mathfrak{p}_0=\mathfrak{m}$이라면 적당한 $j>n$에서 $\Ext_A^j(\kappa,M)\neq 0$이 되어 $n=s$의 정의에 모순이므로, $\mathfrak{p}_0\subsetneq\mathfrak{m}$이고 $x\in\mathfrak{m}\setminus\mathfrak{p}_0$을 택할 수 있다. $A/\mathfrak{p}_0$은 integral domain이고 $x$의 상이 $0$이 아니므로 곱하기 $x$는 $A/\mathfrak{p}_0$ 위에서 injective이며, 다음의 short exact sequence
$$0\rightarrow A/\mathfrak{p}_0\overset{x}{\longrightarrow}A/\mathfrak{p}_0\rightarrow A/(\mathfrak{p}_0+(x))\rightarrow 0$$
을 얻는다. [§동반소아이디얼, ⁋보조정리 6](/ko/math/commutative_algebra/associated_primes#lem6)에 의하여 $A/(\mathfrak{p}_0+(x))$는 subquotient가 $A/\mathfrak{q}$ 꼴인 filtration을 가지며, 각 $\mathfrak{q}$는 $\mathfrak{p}_0+(x)$를 포함하므로 $x\in\mathfrak{q}\setminus\mathfrak{p}_0$, 곧 $\mathfrak{q}\supsetneq\mathfrak{p}_0$이다. $\mathfrak{p}_0$의 maximality에 의하여 이러한 $\mathfrak{q}$는 $\mathcal{T}$에 속하지 않으므로 $j>n$에서 $\Ext_A^j(A/\mathfrak{q},M)=0$이고, filtration의 short exact sequence들에 $\Hom_A(-,M)$의 long exact sequence를 적용하면 $j>n$에서 $\Ext_A^j(A/(\mathfrak{p}_0+(x)),M)=0$을 얻는다.

이제 위의 short exact sequence에 $\Hom_A(-,M)$을 취한 long exact sequence
$$\cdots\rightarrow\Ext_A^j(A/(\mathfrak{p}_0+(x)),M)\rightarrow\Ext_A^j(A/\mathfrak{p}_0,M)\overset{x}{\longrightarrow}\Ext_A^j(A/\mathfrak{p}_0,M)\rightarrow\Ext_A^{j+1}(A/(\mathfrak{p}_0+(x)),M)\rightarrow\cdots$$
에서 가운데 map은 곱하기 $x$가 유도하는 것이므로 $\Ext_A^j(A/\mathfrak{p}_0,M)$ 위의 스칼라 곱 $x$이다. $j>n$이면 $j$와 $j+1$이 모두 $n$보다 크므로 양옆의 항이 $0$이고, 따라서 곱하기 $x:\Ext_A^j(A/\mathfrak{p}_0,M)\rightarrow\Ext_A^j(A/\mathfrak{p}_0,M)$은 isomorphism, 특히 surjective이다. $A$가 Noetherian이므로 $A/\mathfrak{p}_0$은 finitely generated free module들의 resolution을 가지며, 따라서 $\Ext_A^j(A/\mathfrak{p}_0,M)$은 finitely generated $A$-module이다. ([§Depth, ⁋정리 7](/ko/math/commutative_algebra/depth#thm7)의 증명에서와 같은 논증이다.) $x\in\mathfrak{m}$이 이 module 위에 surjective하게 작용하므로 [§정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)에 의하여 $j>n$에서 $\Ext_A^j(A/\mathfrak{p}_0,M)=0$이다. 이는 $\mathfrak{p}_0\in\mathcal{T}$에 모순이므로 $\mathcal{T}=\emptyset$이며, 위의 주장을 얻는다.

마지막으로 임의의 ideal $I$에 대하여 $A/I$는 finitely generated $A$-module이므로 [§동반소아이디얼, ⁋보조정리 6](/ko/math/commutative_algebra/associated_primes#lem6)에 의하여 subquotient가 $A/\mathfrak{p}_k$ 꼴인 filtration $0=N_0\subsetneq\cdots\subsetneq N_r=A/I$를 가지며, 위의 주장에 의하여 각 $\Ext_A^{n+1}(A/\mathfrak{p}_k,M)=0$이다. Filtration의 short exact sequence들과 $\Hom_A(-,M)$의 long exact sequence로부터 $k$에 대한 귀납법으로 $\Ext_A^{n+1}(A/I,M)=0$을 얻는다. 따라서 [§호몰로지 차원, ⁋따름정리 5](/ko/math/commutative_algebra/homological_dimension#cor5)에 의하여 $\operatorname{injdim}_A M\leq n=s$이며, 앞서 보인 $s\leq\operatorname{injdim}_A M$과 종합하여 등식을 얻는다.
:::

[명제 7](#prop7)은 injective dimension을 오직 residue field 하나와의 $\Ext$의 소멸 차수로 읽어내며, 이는 projective dimension을 residue field와의 $\Tor$로 읽는 [§호몰로지 차원, ⁋명제 11](/ko/math/commutative_algebra/homological_dimension#prop11)에 대응하는 쌍대에 해당한다. 특히 $\operatorname{injdim}_A A<\infty$인 local ring, 곧 다음 글에서 다룰 Gorenstein ring의 이론에서 이 판정이 기초가 된다.

## Matlis duality

이 절에서 $(A,\mathfrak{m},\kappa)$는 Noetherian local ring이고, $E=E(\kappa)$는 residue field의 injective hull이다. 우리는 functor
$$D(-)=\Hom_A(-,E)$$
를 고정한다. $E$가 injective이므로 $D$는 exact contravariant functor이다. 이 절의 목표는 $D$가 유한 길이 module 위에서 완벽한 duality를 이루며, $E$의 endomorphism ring이 $A$의 completion임을 보이는 것이다.

::: 보조정리 8
$\Hom_A(\kappa,E)\cong\kappa$이다. 곧 $D(\kappa)\cong\kappa$이다.
:::
::: 증명
$\Hom_A(\kappa,E)=\Hom_A(A/\mathfrak{m},E)$은 $\mathfrak{m}$에 의하여 소멸되는 $E$의 원소들의 module $(0:_E\mathfrak{m})=\{x\in E\mid\mathfrak{m}x=0\}$과 자연스럽게 동일시되며, 이는 $\kappa$-벡터공간이다. $E=E(\kappa)$가 $\kappa$의 essential extension이므로 $\kappa$는 $(0:_E\mathfrak{m})$에 포함된다. 거꾸로 $0\neq x\in(0:_E\mathfrak{m})$이면 $\ann(x)\supseteq\mathfrak{m}$이고 $x\neq 0$이므로 $\ann(x)=\mathfrak{m}$, 곧 $Ax\cong\kappa$는 simple이다. $Ax\neq 0$과 $\kappa\subseteq E$의 essential성에 의하여 $Ax\cap\kappa\neq 0$인데, $Ax$와 $\kappa$가 모두 simple이므로 이 교집합은 둘 다와 같아 $x\in Ax=\kappa$이다. 따라서 $(0:_E\mathfrak{m})=\kappa$이고 $\Hom_A(\kappa,E)\cong\kappa$이다.
:::

이 계산은 $E$의 socle $(0:_E\mathfrak{m})$이 정확히 $\kappa$ 하나로 이루어짐을 말해준다. 이를 출발점으로 하여 유한 길이 module에 대한 duality를 세운다.

::: 명제 9
유한 길이 $A$-module $M$에 대하여 다음이 성립한다.

1. $D(M)$도 유한 길이이며 $\length D(M)=\length M$이다.
2. 자연스러운 evaluation map $M\rightarrow D(D(M))$은 isomorphism이다.
:::
::: 증명
$\length M$에 대한 귀납법으로 증명한다. $\length M=1$이면 $M$은 simple module이고, $A$가 local ring이므로 그 annihilator인 maximal ideal은 $\mathfrak{m}$이어서 $M\cong\kappa$이다. ([§조르단-횔더 정리, ⁋정의 1](/ko/math/commutative_algebra/Jordan-Holder_theorem#def1)) 그럼 [보조정리 8](#lem8)에 의하여 $\length D(\kappa)=\length\kappa=1$이다. 또, evaluation map $\kappa\rightarrow D(D(\kappa))$은 simple module 사이의 map인데, $0\neq x\in\kappa$에 대하여 inclusion $\kappa\hookrightarrow E$이 $D(\kappa)$의 원소로서 $x$에서 $0$이 아닌 값을 주므로 이 evaluation map은 $0$이 아니고, 따라서 injective이다. 양변이 길이 $1$이므로 이는 isomorphism이다.

이제 $\length M=\ell\geq 2$이라 하고 주장이 길이 $\ell$ 미만의 module들에 대하여 성립한다고 가정하자. $M$의 simple submodule $S\cong\kappa$를 택하면 ([§조르단-횔더 정리, ⁋정의 2](/ko/math/commutative_algebra/Jordan-Holder_theorem#def2)) short exact sequence $0\rightarrow S\rightarrow M\rightarrow M/S\rightarrow 0$을 얻고, $\length(M/S)=\ell-1$이다. $D$가 exact이므로
$$0\rightarrow D(M/S)\rightarrow D(M)\rightarrow D(S)\rightarrow 0$$
이 exact이고, 귀납적 가정과 [보조정리 8](#lem8)에 의하여 $\length D(M/S)=\ell-1$, $\length D(S)=1$이므로 [§힐베르트-사무엘 함수, ⁋보조정리 3](/ko/math/commutative_algebra/hilbert-samuel_function#lem3)의 길이의 가법성에 의하여 $\length D(M)=\ell$이다. 여기에 $D$를 다시 취하면 exact sequence
$$0\rightarrow D(D(S))\rightarrow D(D(M))\rightarrow D(D(M/S))\rightarrow 0$$
을 얻으며, evaluation map의 naturality에 의하여 이 sequence는 원래의 short exact sequence와 evaluation map들을 세로줄로 하는 commutative diagram을 이룬다. $S$와 $M/S$에서의 evaluation map은 귀납적 가정에 의하여 isomorphism이므로, [\[호몰로지 대수학\] §Diagram chasing, ⁋따름정리 3](/ko/math/homological_algebra/diagram_chasing#cor3)의 short five lemma에 의하여 가운데의 $M\rightarrow D(D(M))$ 또한 isomorphism이다.
:::

유한 길이 module에서의 이 duality를 $E$ 자신의 구조와 잇기 위해, $E$가 유한 길이 조각들의 합집합임을 확인한다.

::: 보조정리 10
$E$의 임의의 원소는 $\mathfrak{m}$의 어떤 거듭제곱에 의하여 소멸된다. 곧
$$E=\bigcup_{n\geq 1}(0:_E\mathfrak{m}^n)$$
이 성립한다.
:::
::: 증명
$0\neq x\in E$을 택하고 cyclic submodule $Ax\subseteq E$을 생각한다. [보조정리 5](#lem5)에 의하여 $\Ass E=\Ass E(\kappa)=\{\mathfrak{m}\}$이고, [§동반소아이디얼, ⁋보조정리 5](/ko/math/commutative_algebra/associated_primes#lem5)에 의하여 $\Ass(Ax)\subseteq\Ass E=\{\mathfrak{m}\}$이며, $Ax\neq 0$이므로 $\Ass(Ax)=\{\mathfrak{m}\}$이다. 그럼 $\ann(Ax)$를 포함하는 prime 가운데 극소인 것들은 모두 $\Ass(Ax)$에 속하므로 ([§동반소아이디얼, ⁋정리 7](/ko/math/commutative_algebra/associated_primes#thm7)) $\ann(Ax)$를 포함하는 prime은 $\mathfrak{m}$ 하나뿐이고, 따라서 [§조르단-횔더 정리, ⁋따름정리 6](/ko/math/commutative_algebra/Jordan-Holder_theorem#cor6)에 의하여 $Ax$는 유한 길이를 갖는다. 유한 길이 module에서 감소열 $Ax\supseteq\mathfrak{m}Ax\supseteq\mathfrak{m}^2Ax\supseteq\cdots$은 매 단계에서 길이가 진성으로 줄거나 $0$에 도달하므로 적당한 $k$에서 $\mathfrak{m}^kAx=0$이 되고, 곧 $x\in(0:_E\mathfrak{m}^k)$이다.
:::

각각의 $n$에 대하여 $(0:_E\mathfrak{m}^n)=\Hom_A(A/\mathfrak{m}^n,E)=D(A/\mathfrak{m}^n)$이며, $A/\mathfrak{m}^n$이 유한 길이 module이므로 [명제 9](#prop9)에 의하여 $(0:_E\mathfrak{m}^n)$ 또한 길이 $\length(A/\mathfrak{m}^n)$의 유한 길이 module이다. 이제 $E$의 endomorphism ring을 계산한다.

::: 정리 11
Noetherian local ring $(A,\mathfrak{m},\kappa)$와 그 residue field의 injective hull $E=E(\kappa)$에 대하여
$$\Hom_A(E,E)\cong\widehat{A}$$
이 성립한다. 여기서 $\widehat{A}=\varprojlim_n A/\mathfrak{m}^n$은 $A$의 $\mathfrak{m}$진 completion이다. ([§완비화, ⁋정의 1](/ko/math/commutative_algebra/completion#def1))
:::
::: 증명
$E_n=(0:_E\mathfrak{m}^n)$으로 두면 [보조정리 10](#lem10)에 의하여 $E=\bigcup_n E_n$이다. $\varphi\in\Hom_A(E,E)$이면 $x\in E_n$에 대하여 $\mathfrak{m}^n\varphi(x)=\varphi(\mathfrak{m}^nx)=0$이므로 $\varphi(E_n)\subseteq E_n$이다. $E$가 증가하는 $E_n$들의 합집합이므로, $\varphi$를 각 $E_n$으로 제한하는 것은 isomorphism
$$\Hom_A(E,E)\overset{\sim}{\longrightarrow}\varprojlim_n\Hom_A(E_n,E)$$
을 준다. 이는 합집합의 universal property, 곧 $E_n$들 위에서 서로 호환되는 map들의 족이 $E$ 전체 위의 map과 일대일로 대응한다는 사실이다. 한편 $E_n$이 $\mathfrak{m}^n$에 의하여 소멸되므로 임의의 $\Hom_A(E_n,E)$의 상은 $(0:_E\mathfrak{m}^n)=E_n$에 들어가고, 따라서
$$\Hom_A(E_n,E)=D(E_n)=D(D(A/\mathfrak{m}^n))\cong A/\mathfrak{m}^n$$
이다. 마지막 isomorphism은 유한 길이 module $A/\mathfrak{m}^n$에 [명제 9](#prop9)를 적용한 것이며, evaluation map의 naturality에 의하여 $m\leq n$에서의 제한사상 $D(E_n)\rightarrow D(E_m)$은 canonical projection $A/\mathfrak{m}^n\rightarrow A/\mathfrak{m}^m$에 대응한다. 그러므로
$$\Hom_A(E,E)\cong\varprojlim_n D(E_n)\cong\varprojlim_n A/\mathfrak{m}^n=\widehat{A}$$
이다.
:::

$A$가 완비이면 $\widehat{A}=A$이므로, 이 경우 $\Hom_A(E,E)\cong A$이다. 곧 완비 local ring에서 residue field의 injective hull의 endomorphism은 모두 $A$의 원소에 의한 곱으로 주어진다. 다음 두 예시는 이 이론을 고전적인 상황에서 구체화한다.

::: 예시 12
$\mathbb{Z}$의 prime $(p)$에서의 localization $A=\mathbb{Z}_{(p)}$를 생각하자. 이는 maximal ideal $\mathfrak{m}=p\mathbb{Z}_{(p)}$와 residue field $\kappa=A/\mathfrak{m}\cong\mathbb{Z}/p$를 갖는 DVR이다. 우리는 Prüfer $p$-group
$$E:=\mathbb{Q}/\mathbb{Z}_{(p)}=\{a/p^n+\mathbb{Z}_{(p)}\mid a\in\mathbb{Z},\ n\geq 0\}$$
이 $E(\kappa)$임을 보인다. 여기서 $\mathbb{Z}_{(p)}$가 $p$ 이외의 모든 소수를 unit으로 가지므로 $\mathbb{Q}/\mathbb{Z}_{(p)}$의 임의의 원소가 위와 같이 적힌다.

우선 PID 위에서 divisible module과 injective module이 일치함을 관찰한다. PID의 $0$이 아닌 ideal은 $(a)$ 꼴이고 $a$가 non-zerodivisor이므로 $(a)\cong A$이며, 따라서 $A$-linear map $f:(a)\rightarrow E$는 $f(a)=e$로 결정되고 $f$가 $A$로 확장되는 것은 $e\in aE$인 것과 동치이다. $E$가 divisible, 곧 모든 $0\neq a$에 대하여 $aE=E$이면 이 조건이 항상 성립하므로 [§호몰로지 차원, ⁋보조정리 4](/ko/math/commutative_algebra/homological_dimension#lem4)에 의하여 $E$는 injective이다. 그런데 $E=\mathbb{Q}/\mathbb{Z}_{(p)}$는 divisible인데, unit은 자명하게 $E$ 위에서 가역이고 곱하기 $p$는 $a/p^n=p\cdot(a/p^{n+1})$에 의하여 surjective이기 때문이다. 따라서 $E$는 injective이다.

다음으로 $E$가 $\kappa$의 essential extension임을 본다. $E$의 $0$이 아닌 진성 submodule은 $(0:_E p^n)\cong\mathbb{Z}/p^n$ 꼴의 유한 cyclic module들이며, 이들과 $E$ 자신은 모두 socle $(0:_E p)=\{a/p+\mathbb{Z}_{(p)}\}\cong\kappa$를 포함한다. 따라서 $\kappa\subseteq E$는 essential이고, [정리 3](#thm3)의 유일성에 의하여 $E\cong E(\kappa)$이다. 끝으로 [정리 11](#thm11)에 의하여
$$\Hom_A(E,E)\cong\widehat{A}=\varprojlim_n\mathbb{Z}/p^n=\mathbb{Z}_p$$
이며, 이는 $p$진 정수들의 ring이다.
:::

::: 예시 13
Field $\mathbb{K}$ 위의 formal power series ring $A=\mathbb{K}[[\x]]$을 생각하자. 이는 maximal ideal $(\x)$와 residue field $\kappa\cong\mathbb{K}$를 갖는 complete DVR이며, 그 $0$이 아닌 ideal은 $(\x^n)$ 꼴이다. ([§정칙국소환, ⁋명제 6](/ko/math/commutative_algebra/regular_local_rings#prop6)) 우리는 Laurent series field $\mathbb{K}((\x))=\Frac(\mathbb{K}[[\x]])$의 quotient
$$E:=\mathbb{K}((\x))/\mathbb{K}[[\x]]$$
이 $E(\kappa)$임을 보인다. $E$의 원소는 유한한 주부 $\sum_{i=1}^{m}a_i\x^{-i}$의 class로 표현되며, 각각은 $\x^m$에 의하여 소멸된다.

$E$는 divisible이다. 임의의 원소는 $\x$에 의하여 나누어지는데, $\sum_i a_i\x^{-i}=\x\cdot\sum_i a_i\x^{-i-1}$이기 때문이고, unit은 $E$ 위에서 가역이므로 $A$의 $0$이 아닌 원소 $\x^n u$에 의한 곱은 모두 surjective이다. 따라서 [예시 12](#ex12)에서와 같은 Baer 판정법에 의하여 $E$는 injective이다. 또, $E$의 submodule들은 사슬
$$(0:_E\x)\subseteq(0:_E\x^2)\subseteq\cdots,\qquad(0:_E\x^n)\cong\mathbb{K}[[\x]]/(\x^n)$$
을 이루며 어느 것이든 socle $(0:_E\x)=\{a\x^{-1}+\mathbb{K}[[\x]]\}\cong\kappa$를 포함하므로, $\kappa\subseteq E$는 essential이고 $E\cong E(\kappa)$이다. 여기서 $(0:_E\x^n)=\Hom_A(A/(\x^n),E)=D(A/(\x^n))$은 길이 $n$의 module로서 [명제 9](#prop9)의 계산과 부합한다. 끝으로 $A=\mathbb{K}[[\x]]$가 완비이므로 [정리 11](#thm11)에 의하여
$$\Hom_A(E,E)\cong\widehat{A}=A=\mathbb{K}[[\x]]$$
이다.
:::

Injective dimension이 유한한 local ring의 이론이 다음 글의 주제이다.

---

**참고문헌**

**[BH]** W. Bruns, J. Herzog. *Cohen-Macaulay Rings*. Cambridge University Press, 1993.

**[Eis]** David Eisenbud. *Commutative Algebra: with a view toward algebraic geometry*. Springer, 1995.

**[Mat]** Hideyuki Matsumura. *Commutative Ring Theory*. Cambridge University Press, 1986.

**[Stacks]** The Stacks Project Authors. *The Stacks Project*. [https://stacks.math.columbia.edu](https://stacks.math.columbia.edu).

---
