---
title: "가상류의 교차이론"
description: "Regular embedding의 Gysin morphism과 그 refined 판본을 deformation to the normal cone으로 구성하고, excess intersection formula와 functoriality를 거쳐 두 virtual class를 smooth base 위의 대각선으로 교차시키는 연산을 얻는다."
excerpt: "Refined Gysin homomorphisms, excess intersection, and diagonal intersection of virtual classes over a smooth base"

categories: [Math / Gromov-Witten Theory]
permalink: /ko/math/gromov-witten_theory/intersection_theory_of_virtual_classes
sidebar: 
    nav: "gromov-witten_theory-ko"

date: 2026-09-18

weight: 5

---

Gromov-Witten 이론에서는 virtual class들을 서로 교차시켜야 하는 일이 계속 생긴다. 두 moduli $M_1,M_2$가 공통의 공간 $S$로 가는 map을 가질 때, 두 조건을 동시에 만족하는 대상들의 moduli는 fiber product $M_1\times_SM_2$이고, 우리는 $[M_1]^\vir$과 $[M_2]^\vir$로부터 이 fiber product 위의 class를 얻고자 한다. ([§Perfect obstruction theory, ⁋명제 3](/ko/math/gromov-witten_theory/perfect_obstruction_theory#prop3){: data-lid="4munh" })

[\[대수다양체\] §교차곱](/ko/math/algebraic_varieties/intersection_product){: data-lid="8i3l7" }에서 우리는 두 class의 intersection product를 하는 법을 살펴보았으나, 우리 경우에는 대부분의 공간이 smooth가 아니므로 이것이 잘 정의되지 않는다. 만일 $S$가 smooth하고 두 map이 proper라면 우리는 그 대안으로 두 class를 $S$로 pushforward한 후 교차시킬 수 있겠지만, 그 결과는 $S$의 class이므로 우리가 원하는 결과가 아니다. 때문에 우리는 [\[스택\] §Deligne–Mumford 스택 위의 적분, §§곱공간과 대각선 교차](/ko/math/stacks/integration_on_deligne_mumford_stacks#곱공간과-대각선-교차){: data-lid="qj2hs" }에서 증명 없이 받아들인 refined Gysin pullback을 엄밀하게 정의해야 한다. 

Chow group은 scheme 위에서는 [\[대수다양체\] §저우 군, ⁋정의 5](/ko/math/algebraic_varieties/chow_groups#def5){: data-lid="sjvhy" }의 것을, stack 위에서는 [\[스택\] §Deligne–Mumford 스택 위의 적분](/ko/math/stacks/integration_on_deligne_mumford_stacks){: data-lid="34uzj" }의 $\mathbb{Q}$-계수 버전을 가리키며, 첨자를 생략하고 $A_k$로 적는다.

## Gysin morphism

Gysin morphism을 정의하려면 normal cone이 필요하다. 우리는 이를 [\[대수다양체\] §교차곱, §§Deformation to Normal Cone](/ko/math/algebraic_varieties/intersection_product#deformation-to-normal-cone){: data-lid="j4g18" }에서 이미 살펴보았으므로, 여기서는 이후에 필요한 만큼 간략히 복습한다.

Closed embedding $i:W\hookrightarrow X$와 $W$의 ideal sheaf $\mathcal{I}$에 대하여, $i$의 *normal cone*은

$$C_{W/X}=\Spec_W\Bigl(\bigoplus_{n\geq0}\mathcal{I}^n/\mathcal{I}^{n+1}\Bigr)$$

으로 정의된다. 여기서 $\mathcal{I}/\mathcal{I}^2$은 $W$ 위에서 사라지는 함수들의 일차 부분, 곧 $W$에 수직인 방향의 linear coordinate들이며 직관적으로 이는 각 $w\in W$에서 $W$를 벗어나는 방향들을 모은 것이다. 한편 $\mathcal{I}^n/\mathcal{I}^{n+1}$은 $\mathcal{I}/\mathcal{I}^2$의 원소들의 곱으로 생성되므로 graded algebra의 surjection

$$\Sym(\mathcal{I}/\mathcal{I}^2)\rightarrow\bigoplus_{n\geq0}\mathcal{I}^n/\mathcal{I}^{n+1}$$

이 존재한다. 이 때, ambient space $\Spec_W\Sym(\mathcal{I}/\mathcal{I}^2)$는 각 점 $w\in W$에서 $W$를 벗어나는 방향들로 만들어지는 <em-ko>벡터공간</em-ko> $(\mathcal{I}/\mathcal{I}^2\otimes k(w))^\vee$으로, 만일 $\mathcal{I}/\mathcal{I}^2$가 locally free라면 이러한 fiber들의 모임이 vector bundle을 이루므로 이를 *normal bundle*이라 부른다. 

Normal bundle과 normal cone의 차이는, 위에서 강조한 것과 같이, normal bundle은 각 점 $w \in W$에서 $W$를 벗어나는 방향들로 만들어지는 <em-ko>벡터공간</em-ko>이므로 각 벡터들의 일차결합이 자기 자신 안으로 다시 들어와야 한다는 것에 있다. 반면 normal cone은 점 $w$에서 $W$를 벗어나는 방향들만 모은 것이므로, 이들의 일차결합이 다시 자기 자신 안으로 들어올 필요는 없다. 직관적으로 normal cone은 정확히 우리가 보고자 하는 방향들만 모아둔 normal bundle의 subset이며, 정의에 의해 normal cone은 스칼라배에 대해서 닫혀 있으므로 이 벡터공간 안에 cone을 이룬다. 이 cone이 어떻게 주어지는지를 확인하기 위해 closed subscheme 구조를 확인해 보자. Surjection

$$\Sym(\mathcal{I}/\mathcal{I}^2)\rightarrow\bigoplus_{n\geq0}\mathcal{I}^n/\mathcal{I}^{n+1}$$

의 $n$차 kernel은 linear coordinate들의 $n$차 homogeneous polynomial 가운데 $\mathcal{I}^{n+1}$에 떨어지는 것들, 곧 $X$가 $W$ 근방에서 만족하는 방정식의 최저차항들이며, 이 방정식들이 ambient space의 각 fiber에서 $X$가 최저차 근사에서 뻗어 나가지 않는 방향들을 잘라낸다. 가령 $X=\{\x\y=0\}\subset\mathbb{A}^2$이고 $W$가 원점이면 normal bundle의 fiber는 $\x,\y$를 coordinate로 하는 $2$차원 벡터공간이지만, $\x\y$가 $\mathcal{I}^3$에 떨어지므로 $\bigoplus_n\mathcal{I}^n/\mathcal{I}^{n+1}\cong\mathbb{C}[\x,\y]/(\x\y)$이고 normal cone은 두 직선 $\{\x\y=0\}$이다. 

이제 만일 $i$가 codimension $d$의 regular embedding이라면 ([\[스킴\] §완전교차, ⁋정의 1](/ko/math/scheme_theory/complete_intersections#def1){: data-lid="ramli" }), $\mathcal{I}/\mathcal{I}^2$이 $W$ 위의 rank $d$ locally free sheaf이고 ([\[스킴\] §완전교차, ⁋명제 5](/ko/math/scheme_theory/complete_intersections#prop5){: data-lid="bhh8c" }) regular sequence로 생성된 ideal에 대하여 위의 surjection이 isomorphism이므로, 여분의 방정식이 없어 $C_{W/X}$는 rank $d$ normal bundle $N_{W/X}=\Spec_W\Sym(\mathcal{I}/\mathcal{I}^2)$ 전체와 같아진다. 더 일반적으로, morphism $g:X'\rightarrow X$와 $W'=X'\times_XW$에 대하여 $W'$의 ideal sheaf는 $\mathcal{I}$가 $X'$에서 생성하는 ideal이므로, 같은 surjection에 의하여 $C_{W'/X'}$는 $g^\ast N_{W/X}$의 closed subcone을 정의한다. 특히 closed subvariety $V\subseteq X$에 대하여 $C_{W\cap V/V}$는 $C_{W/X}$의 closed subcone이다.

임의의 $k$-dimensional subvariety $V\subseteq X$에 대하여, $C_{W\cap V/V}$는 pure dimension $k$를 갖는 것을 확인할 수 있으므로, 특히 fundamental class $[C_{W\cap V/V}]\in A_k(C_{W/X})$가 존재한다. $A_k(X)$는 $k$-dimensional subvariety들의 class $[V]$로 생성되므로, 대응 $[V]\mapsto[C_{W\cap V/V}]$로 group homomorphism

$$\sigma:A_k(X)\rightarrow A_k(C_{W/X})$$

를 정의하고, 이를 $i$에 대한 *specialization*이라 부른다. 한편 $N_{W/X}\rightarrow W$이 vector bundle이므로, flat pullback ([\[대수다양체\] §저우 군, ⁋명제 7](/ko/math/algebraic_varieties/chow_groups#prop7){: data-lid="iklbh" })

$$p^\ast:A_{k-d}(W)\rightarrow A_k(N_{W/X})$$

이 존재하며, 이는 homotopy invariance에 의하여 isomorphism이다. ([\[대수다양체\] §저우 군, ⁋예시 9](/ko/math/algebraic_varieties/chow_groups#ex9){: data-lid="o8yhs" }) 이 두 morphism을 합성하면 우리가 원하는 연산을 얻는다.

::: 정의 1
Codimension $d$ regular embedding $i:W\hookrightarrow X$와 $N=N_{W/X}$에 대하여, $i$의 *Gysin morphism<sub>귀진 사상</sub>*

$$i^!:A_k(X)\rightarrow A_{k-d}(W)$$

를 specialization과 flat pullback의 역의 합성 $i^!:=(p^\ast)^{-1}\circ\sigma$로 정의한다.
:::

기하적으로 $i^!\alpha$는 $\alpha\in A_k(X)$를 $W$와 교차시켜 그 결과를 $W$ 위의 class로 기록한 것이다. Specialization이 $\alpha$를 $W$ 방향의 normal cone (이 경우에는 normal bundle)의 class로 볼 수 있게 해 주며, 이 때 flat pullback의 역, 즉 zero section과 이 cycle의 intersection을 하는 것이 우리가 원하는 결과를 주는 것이다.

그런데 $\sigma$는 generator $[V]$의 representative $V$를 골라 정의했으므로, 이것이 $A_k(X)$ 위에서 잘 정의되려면 rational equivalence를 보존해야 한다. 이는 식만 보아서는 자명하지 않은데, 서로 rationally equivalent한 두 cycle의 normal cone들이 왜 rationally equivalent해야 하는지가 정의에 드러나 있지 않기 때문이다. 또 우리는 $C_{W\cap V/V}$가 pure dimension $k$를 갖는다는 사실도 아직 보이지 않았다. 이를 보장하는 것이 [\[대수다양체\] §교차곱, ⁋명제 9](/ko/math/algebraic_varieties/intersection_product#prop9){: data-lid="fbo0m" }의 deformation to the normal cone이다.

::: 명제 2
Closed embedding $i:W\hookrightarrow X$에 대하여 다음이 성립한다.

1. 모든 $k$차원 subvariety $V\subseteq X$에 대하여 $C_{W\cap V/V}$는 pure dimension $k$를 갖는다.
2. Specialization $\sigma$는 rational equivalence를 보존한다.

따라서 $\sigma:A_k(X)\rightarrow A_k(C_{W/X})$는 잘 정의된 group homomorphism이고, 특히 [정의 1](#def1){: data-lid="zbr11" }의 $i^!$은 잘 정의된다.
:::

::: 증명
먼저 deformation to the normal cone을 scheme 위에서 구성한다. $X$가 affine이고 $\mathcal{I}$가 ideal $I\subseteq A$에 대응할 때, 변수 $t$에 대한 graded algebra

$$\widetilde{A}=\bigoplus_{n\in\mathbb{Z}}I^nt^{-n}\subseteq A[t,t^{-1}],\qquad I^n=A\quad(n\leq0)$$

를 생각하자. 이는 $A[t]$ 위의 algebra이고 $A[t,t^{-1}]$의 subring이므로 $\mathbb{C}[t]$의 $0$이 아닌 원소에 대해 torsion-free이며, PID 위의 torsion-free module은 flat이므로 $M=\Spec\widetilde{A}$는 $\mathbb{A}^1=\Spec\mathbb{C}[t]$ 위에서 flat이다. 또 $\widetilde{A}[t^{-1}]=A[t,t^{-1}]$이고 $\widetilde{A}/(t)\cong\bigoplus_{n\geq0}I^n/I^{n+1}$이며, $\widetilde{A}$에서 $(A/I)[t]$로 가는 surjection이 $n>0$인 성분을 $0$으로, $n\leq0$인 성분 $At^{-n}$을 $(A/I)t^{-n}$으로 보낸다. 이 구성은 affine open 위에서 서로 붙으므로 일반적인 $X$ 위에서도 잘 정의된다.

여기서 핵심적인 사실은 $M\rightarrow\mathbb{A}^1$은 flat family라는 것으로, 각 점 $t\in \mathbb{A}^1$에서의 fiber는

$$M_t\cong X\quad(t\neq0),\qquad M_0\cong C_{W/X}$$

로 주어진다. 즉, $M$은 $X$가 $t\rightarrow0$에 따라 normal cone $C_{W/X}$로 퇴화하는 flat family로 생각할 수 있다. 더 구체적으로, $M$에서 $t\neq0$인 부분은 정확히 $X\times(\mathbb{A}^1\setminus\{0\})$으로 주어지며, 이 때 $W$를 closed subscheme $W\times\mathbb{A}^1\subseteq M$으로 각 fiber에 넣어주면 이는 $t\neq 0$인 fiber에서는 $X$ 안에 들어있는 $W$ 자신이 되며, $t=0$에서는 $C_{W/X}$의 zero section이 된다.

이제 이 과정에서 $k$차원 subvariety $V\subseteq X$가 어디로 가는지를 확인해야 한다. Closed embedding $W\cap V\hookrightarrow V$에 대해서도 위와 같이 deformation to the normal cone을 구성하여 얻은 family를 $M_V\rightarrow\mathbb{A}^1$이라 하자. 만일 $V$가 affine이고 그 coordinate ring이 $A$의 quotient $B$이면, $W\cap V$의 ideal은 $IB$이고

$$M_V=\Spec\Bigl(\bigoplus_{n\in\mathbb{Z}}(IB)^nt^{-n}\Bigr)$$

로 주어지며, 이 때 $I^n\rightarrow(IB)^n$이 surjective이므로 이 algebra는 $\widetilde{A}$의 quotient이다. 즉 $M_V$는 $M$의 closed subscheme이다. 또, 위의 algebra는 integral domain $B[t,t^{-1}]$의 subring이므로 $M_V$도 integral이다. 이제 $M_V$에서 $t\neq0$인 부분은 $V\times(\mathbb{A}^1\setminus\{0\})$이므로, $M_V$ 전체는 이 부분에 $M$ 안에서의 closure를 취해 얻을 수 있으며, 따라서 $M_V$는 dimension $k+1$을 갖는다. 곧 $M_V$는 $V$가 $X$와 함께 움직이며 남기는 자취이고, 그 $t=0$ fiber인 $C_{W\cap V/V}$가 $V$의 극한이다. 마지막으로 이 극한은 $(k+1)$차원 variety $M_V$ 위에서 identically zero가 아닌 함수 $t$의 zero locus이므로, [\[가환대수학\] §차원, ⁋정리 6](/ko/math/commutative_algebra/Krull_dimension#thm6){: data-lid="r0p5b" }에 의하여 그 모든 irreducible component는 dimension $k$를 갖는다. 따라서 $C_{W\cap V/V}$는 pure dimension $k$이고, 이것이 첫째 주장이다.

이제 둘째 주장, 곧 $\sigma$가 rational equivalence를 보존함을 보이자. 이를 위해 $\sigma$를 각각 Chow group 위에서 이미 잘 정의된 세 연산의 합성으로 표현한다. 첫째 연산은 projection $X\times(\mathbb{A}^1\setminus\{0\})\rightarrow X$에 의한 flat pullback

$$A_k(X)\rightarrow A_{k+1}(X\times(\mathbb{A}^1\setminus\{0\}))$$

으로, $[V]$를 $[V\times(\mathbb{A}^1\setminus\{0\})]$로 보낸다. 둘째 연산은 $M$에서 open subset $X\times(\mathbb{A}^1\setminus\{0\})$으로의 restriction을 거꾸로 올라가는 것이다. [\[대수다양체\] §저우 군, ⁋명제 8](/ko/math/algebraic_varieties/chow_groups#prop8){: data-lid="i8ed9" }의 localization exact sequence

$$A_{k+1}(M_0)\rightarrow A_{k+1}(M)\rightarrow A_{k+1}(X\times(\mathbb{A}^1\setminus\{0\}))\rightarrow0$$

에 의하여 이 restriction은 surjective이고 그 kernel은 $M_0$에서 오는 class들이다. 따라서 $X\times(\mathbb{A}^1\setminus\{0\})$ 위의 class는 $M$ 위의 class로 들어올릴 수 있으며, 그 lift의 자유도는 $M_0$에서 오는 class에 담긴다. 약간의 계산을 통해 $[V\times(\mathbb{A}^1\setminus\{0\})]$의 lift로 $[M_V]$를 택할 수 있다는 것을 확인할 수 있다. 마지막 연산은 principal Cartier divisor $M_0=\{t=0\}$과의 교차 $A_{k+1}(M)\rightarrow A_k(M_0)$이다. 이 연산은 rational equivalence를 보존하며, 둘째 연산의 모호함을 없애 준다. $M_0$ 위에 놓인 class와 $M_0$의 교차는 line bundle $\mathcal{O}_M(M_0)$의 first Chern class를 cap하는 것인데, $M_0$가 함수 $t$의 zero locus이므로 이 line bundle은 trivial하기 때문이다.

따라서 세 연산의 합성

$$A_k(X)\rightarrow A_k(M_0)=A_k(C_{W/X})$$

은 lift의 선택과 무관하며, Chow group 사이의 group homomorphism으로 잘 정의된다. 이제 이것이 $\sigma$와 같다는 것을 보이기 위해서는 마지막 단계에서 $[M_V]$가 어디로 가는지만 보면 충분하다. 우리는 $M_V$가 integral이고 그 위에서 $t$가 identically zero가 아닌 것을 알고 있으므로, $M_0$와 $[M_V]$의 교차는 $M_V$ 위에서 $t$의 zero scheme, 곧 $M_V$의 $t=0$ fiber $C_{W\cap V/V}$의 class가 된다.
:::

[정의 1](#def1){: data-lid="i9evw" }의 연산은 $X$ 자신 위의 class를 $W$로 자르는 것이다. 문제는 우리가 실제로 교차시키려는 class는 대개 $X$ 위에 있지 않다는 것으로, 가령 도입부에서 살펴본 예시에서 우리가 원하는 것은 두 moduli $M_1,M_2$가 공통의 공간 $S$로 가는 map을 가질 때 fiber product $M_1\times_SM_2$ 위의 class였다. 이 fiber product는 $M_1\times M_2$를 $S\times S$의 diagonal의 preimage로 자른

$$(M_1\times M_2)\times_{S\times S}S=\{(m_1,m_2,s)\mid(f_1(m_1),f_2(m_2))=(s,s)\}=\{(m_1,m_2)\mid f_1(m_1)=f_2(m_2)\}=M_1\times_SM_2$$

으로 생각할 수 있는데, 우리가 잘라내야 할 class는 $M_1\times M_2$ 위에 있는 반면, 이를 잘라줄 공간은 $S\times S$ 안의 diagonal이므로 위의 [정의 1](#def1){: data-lid="jpk5o" }이 그대로는 적용되지 않는다. 그 대신, 우리는 morphism $M_1\times M_2\rightarrow S\times S$을 가지고 있으므로 위의 construction이 이 morphism을 경유하도록 할 수 있다. 

이를 일반적으로 적기 위해 $i:W\hookrightarrow X$를 codimension $d$ regular embedding, $N=N_{W/X}$를 그 normal bundle이라 하고, 임의의 morphism $g:X'\rightarrow X$에 대하여 fiber product

$$W'=X'\times_XW=g^{-1}(W)$$

를 생각하자. 여기서 $W'\hookrightarrow X'$은 closed embedding이지만 regular embedding일 필요는 없으므로 위의 구성에서 $N_{W'/X'}$가 bundle로서 잘 정의되지는 않지만, 앞서 본 것처럼 normal cone $C_{W'/X'}$는 $W'$ 위의 rank $d$ vector bundle $g^\ast N$의 closed subcone이므로 이를 사용하면 충분하다. 즉 $X'$ 위의 class를 [명제 2](#prop2){: data-lid="1s02i" }의 specialization으로 $C_{W'/X'}$의 class로 보낸 뒤 $g^\ast N$의 class로 보고, $p:g^\ast N\rightarrow W'$의 flat pullback isomorphism

$$p^\ast:A_{k-d}(W')\rightarrow A_k(g^\ast N)$$

의 역, 곧 $g^\ast N$의 zero section과의 intersection으로 $W'$ 위에 내려 $W'$ 위의 class를 얻을 수 있다.

::: 정의 3
위의 상황에서 $i$의 *refined Gysin morphism<sub>정련된 귀진 사상</sub>*

$$i^!:A_k(X')\rightarrow A_{k-d}(W')$$

를 $W'\hookrightarrow X'$에 대한 specialization과 $g^\ast N\rightarrow W'$의 flat pullback의 역의 합성으로 정의한다.
:::

정의의 핵심은 결과 class가 실제 preimage $W'$ 위에 살면서 차원은 여전히 기대값 $k-d$를 유지한다는 것이다. 특히 $W'$이 기대 차원보다 클 때에도 이 연산은 잘 정의된 $(k-d)$차원 class를 준다.

[§Perfect obstruction theory, §§벡터다발의 zero locus](/ko/math/gromov-witten_theory/perfect_obstruction_theory#벡터다발의-zero-locus){: data-lid="8fhy4" }에서 보았듯, virtual class의 원형은 다음과 같다. Smooth한 공간 위의 rank $r$ vector bundle $E\rightarrow V$가 주어졌다 하고, 그 section $s:V\rightarrow E$이 주어졌다 하자. 이 section의 zero locus를 $Z(s)$라 하고, $E$의 zero section을 $0_E: V\hookrightarrow E$라 하면 우리가 기대하는 class는 normal cone $C_{Z/V}$를 $E\vert_Z$ 안에 넣은 후 zero section으로 잘라 만들어진 class이다. 즉, 이 construction은 정확히 [정의 3](#def3){: data-lid="brunk" }에서

$$X=E,\quad X'=W=V,\quad g=s: V\rightarrow E,\quad i=0_E: V\rightarrow E$$

을 입력으로 넣은 경우이다. 이 때, $E$의 total space $\Spec_V\Sym(E^\vee)$에서 zero section $0_E$는 정확히 fiber 방향의 linear coordinate들이 모두 사라지는 조건으로 주어지므로, 이는 degree $1$ 이상인 부분을 모두 $0$으로 보내는 map $\Sym(E^\vee)\rightarrow\mathcal{O}_V$으로 주어진다. 즉 $0_E$는 codimension $r$ regular embedding으로, 그 conormal sheaf는 $E^\vee$, 그리고 normal bundle은 $(E^\vee)^\vee=E$가 되어 $N=E$이고 $d=r$이다. 

그럼 이 상황에서 

$$W'=s^{-1}(0_E(V))=Z,\qquad g^\ast N=E\vert_Z$$

이므로 [정의 3](#def3){: data-lid="7v7s1" } 이전에 살펴본 것처럼 $C_{Z/V}$가 $E\vert_Z$ 안에 들어가게 된다. 구체적으로, zero section이 degree $1$ 부분을 $0$으로 보내는 algebra map에 대응하듯, section $s$는 degree $1$ 부분이 $s^\vee:E^\vee\rightarrow\mathcal{O}_V$인 algebra map $\Sym(E^\vee)\rightarrow\mathcal{O}_V$에 대응한다. 국소적으로 $s=(s_1,\ldots,s_r)$이면 $s^\vee$는 $e_i\mapsto s_i$이다. $Z$는 두 section의 fiber product $V\times_{s,E,0_E}V$이므로 그 structure sheaf는 $\mathcal{O}_V$를 $s^\vee(e)-0=s^\vee(e)$ $(e\in E^\vee)$들로 나눈 것이고, 따라서 $Z$의 ideal sheaf는 $\mathcal{I}=s^\vee(E^\vee)$, 국소적으로 $(s_1,\ldots,s_r)$이다. 이로부터 surjection $E^\vee\vert_Z\rightarrow\mathcal{I}/\mathcal{I}^2$을 얻고, 이것이 closed embedding $C_{Z/V}\hookrightarrow E\vert_Z$를 준다. 따라서 [정의 3](#def3){: data-lid="0p60g" }을 vector bundle의 section에 적용하면 localized Euler class를 일반적인 cycle에 작용시키는 연산을 얻고, virtual class도 같은 방식으로 다룰 수 있게 된다. 이렇게 얻은 refined Gysin을

$$0^!_{E,s}:A_k(V)\rightarrow A_{k-r}(Z)$$

로 적는다. $0_E$는 $V$의 smoothness와 무관하게 regular embedding이므로 이는 임의의 $V$에서 정의되며, $j:Z\hookrightarrow V$에 대하여

$$j_\ast 0^!_{E,s}\gamma=c_r(E)\cap\gamma$$

이다. 곧 top Chern class 식은 $V$로 pushforward한 뒤에 성립하며, $0^!_{E,s}\gamma$ 자체는 그보다 정밀하게 $Z$ 위에 사는 class이다.

또, 정의에서 다음은 거의 자명하다.

::: 명제 4
Codimension $d$ regular embedding $i:W\hookrightarrow X$와 $N=N_{W/X}$에 대하여 다음이 성립한다.

1. $X$가 dimension $n$인 smooth variety이면 $i^![X]=[W]\in A_{n-d}(W)$이다.
2. 모든 $\beta\in A_\ast(W)$에 대하여 $i^!i_\ast\beta=c_d(N)\cap\beta$이다.
:::

## Excess intersection과 functoriality

[정의 3](#def3){: data-lid="jx958" }의 $i^!$은 $A_k(X')$에서 $A_{k-d}(W')$로 가므로, 그 결과는 $W'$의 실제 차원과 무관하게 언제나 차원 $k-d$의 class이다. $W'$이 이보다 클 때, 특히 $W'\hookrightarrow X'$이 $d$보다 작은 codimension의 regular embedding일 때에는 refined Gysin을 다음과 같이 구체적으로 계산할 수 있다.

::: 명제 5 (Excess intersection formula)
[정의 3](#def3){: data-lid="sxx6y" }의 상황에서 $i':W'\hookrightarrow X'$ 또한 codimension $d'$ regular embedding이고 그 normal bundle이 $N'$이라 하자. 그럼 $N'$은 $g^\ast N$의 subbundle이 되고 quotient

$$E:=g^\ast N/N'$$

는 $W'$ 위의 rank $e=d-d'$ vector bundle이다. 이 때 모든 $\alpha\in A_k(X')$에 대하여

$$i^!(\alpha)=c_e(E)\cap(i')^!(\alpha)$$

가 성립한다.
:::

Rank $e$인 $E$를 *excess bundle*이라 부른다. 곧 refined Gysin은 실제 교차 $(i')^!\alpha$에 excess bundle의 Euler class를 곱하는 보정을 자동으로 수행하며, $W'$이 정확히 기대 차원이면 $d'=d$이고 $e=0$이라 보정 없이 $i^!\alpha=(i')^!\alpha$가 된다. $g=i$인 극단에서는 $i'=\id_W$이므로 $E=N$이 되어 [명제 4](#prop4){: data-lid="wavpv" }의 self-intersection formula로 돌아간다.

::: 예시 6
$X=\mathbb{P}^2$과 하나의 line $W=L$을 잡으면 $i:L\hookrightarrow\mathbb{P}^2$은 codimension $1$ regular embedding이고, $L$의 ideal sheaf가 $\mathcal{O}_{\mathbb{P}^2}(-1)$이므로 conormal sheaf는 $\mathcal{O}_L(-1)$이고 $N_{L/\mathbb{P}^2}=\mathcal{O}_L(1)$이다. 이 세팅에서 두 가지 현상이 나타난다.

1. Smooth conic $Q$가 $L$과 한 점 $p$에서 접한다고 하고 $g:Q\hookrightarrow\mathbb{P}^2$을 그 embedding으로 두자. 그럼 $W'=g^{-1}(L)$은 scheme으로서 $Q$ 위의 length $2$ divisor $2p$이다. $W'$은 $Q$ 안의 Cartier divisor, 곧 codimension $1$ regular embedding이므로 $d'=d=1$이고 $e=0$이며, [명제 5](#prop5){: data-lid="tx3h8" }와 [명제 4](#prop4){: data-lid="6hhor" }에 의하여

   $$i^![Q]=(i')^![Q]=[W']=2[p]$$

   이다. 즉 [정의 3](#def3){: data-lid="divec" }의 결과는 실제 교차 $W'$의 class 자신이고, 그 degree

   $$\deg i^![Q]=L\cdot Q=2$$

   는 Bézout 수와 일치한다. ([\[대수다양체\] §베주 정리](/ko/math/algebraic_varieties/bezout_theorem){: data-lid="qysgj" }) 두 곡선이 $p$에서 transversal하지 않은데도 refined Gysin은 intersection number $2$를 접점 한 곳에 응축시킨 잘 정의된 class를 준다.

2. 이번에는 $X'=L$ 자신을 $g=i$로 놓아 $L$을 자기 자신과 교차시키자. 그럼 $W'=g^{-1}(L)=L$ 전체가 되어 기대 차원 $0$보다 큰 dimension $1$을 가지며, $i'=\id_L$이라 $d'=0$, $N'=0$이고 excess bundle은

   $$E=g^\ast N_{L/\mathbb{P}^2}=\mathcal{O}_L(1),\qquad e=1$$

   이 된다. [명제 5](#prop5){: data-lid="uitzj" }를 적용하면

   $$i^![L]=c_1(\mathcal{O}_L(1))\cap[L]=[\mathrm{pt}]$$

   로 self-intersection number $L\cdot L=1$을 얻는다. 초과된 $1$차원이 excess bundle의 Euler class로 정확히 흡수된 것이다.
:::

미분위상에서는 두 경우 모두 한쪽을 조금 perturb하여 transversal하게 만든 뒤 교차점을 세면 된다. 즉, 첫째 경우에서는 $L$을 살짝 밀어 $Q$와 서로 다른 두 점에서 만나게 하고, 둘째 경우에서는 $L$을 가까운 다른 line으로 옮기면 된다. 대수기하에서는 이렇게 자유롭게 움직일 여유가 없지만, refined Gysin은 아무것도 움직이지 않고 실제 교차 위에서 같은 답을 준다는 것이 바로 [예시 6](#ex6){: data-lid="zp7sb" }이 주는 직관이다. 

한편 이 연산이 쓸모 있으려면 morphism과도 잘 얽혀야 한다. Proper pushforward와의 호환은 우리가 [\[스택\] §Deligne–Mumford 스택 위의 적분, §§올을 따른 적분](/ko/math/stacks/integration_on_deligne_mumford_stacks#올을-따른-적분){: data-lid="g0iqe" }에서 fiber integration을 유도하며 이미 사용하였고, 여기에 덧붙일 것은 서로 다른 Gysin morphism들이 순서에 무관하다는 사실이다.

::: 명제 7
Regular embedding $i:W\hookrightarrow X$에 대하여 다음이 성립한다.

1. $g:X'\rightarrow X$가 flat이면 $i^!$은 flat pullback과 교환한다.
2. $j:V\hookrightarrow Y$가 또 하나의 regular embedding이면, 적절한 fiber product 위에서 $i^!j^!=j^!i^!$이다.
:::

두 번째 가환성은 여러 조건을 차례로 교차할 때 그 순서가 결과에 영향을 주지 않음을 보장하며, 아래에서 두 class를 대각선으로 교차시키는 연산의 결합법칙이 여기에서 나온다.

## Virtual class의 상대 교차

지금까지 우리는 scheme 위에서 Gysin morphism을 정의했지만, 우리가 실제로 궁금한 것은 stable map의 moduli, 곧 Deligne-Mumford stack 위에서의 Gysin morphism이다. 그러나 이를 위해 특별히 새로 필요한 것은 많지 않은데, $\mathbb{Q}$-계수 Chow group과 proper pushforward, 그리고 그 위에서 refined Gysin pullback이 구성되어 base change와 호환된다는 것을 [\[스택\] §Deligne–Mumford 스택 위의 적분](/ko/math/stacks/integration_on_deligne_mumford_stacks){: data-lid="t0m5w" }에서 이미 확보하였기 때문이다. 따라서 앞 절들의 $X,X',W,W'$ 자리에 moduli stack을 넣어도 모든 공식이 그대로 성립한다. 추가로 위 구성은 $i$가 embedding이라는 사실을 étale 국소적으로만 사용하므로, unramified이면서 étale 국소적으로 regular embedding인 morphism, 곧 *regular local immersion*에 대해서도 refined Gysin이 같은 방식으로 정의된다. 이러한 일반화가 반드시 필요한 이유는 stack $S$에 비자명한 automorphism이 있으면 대각선 $\Delta_S:S\rightarrow S\times S$는 embedding이 아니지만, $S$가 smooth이기만 하면 언제나 regular local immersion이기 때문이다.

이제 도입부의 상황으로 돌아가자. $S$를 pure dimension $s$인 smooth Deligne-Mumford stack, $M_1,M_2$를 Deligne-Mumford stack, $f_i:M_i\rightarrow S$를 morphism이라 하자. [정의 3](#def3){: data-lid="nk76p" } 앞에서 본 것처럼

$$M_1\times_SM_2=(M_1\times M_2)\times_{S\times S}S$$

이고 $\Delta_S$는 codimension $s$ regular local immersion이므로, [정의 3](#def3){: data-lid="cn7cd" }을 $i=\Delta_S$, $X'=M_1\times M_2$, $g=f_1\times f_2$로 두고 적용할 수 있다. 이 때 $W'=M_1\times_SM_2$이다.

::: 명제 8
위의 상황에서 class $\gamma_1\in A_{k_1}(M_1)$과 $\gamma_2\in A_{k_2}(M_2)$에 대하여 다음의 class

$$\Delta_S^!(\gamma_1\times\gamma_2)\in A_{k_1+k_2-s}(M_1\times_SM_2)$$

가 잘 정의된다. 여기서 $\gamma_1\times\gamma_2\in A_{k_1+k_2}(M_1\times M_2)$는 exterior product이다.
:::

이 명제는 base $S$가 smooth할 것을 요구하는데, stable map의 moduli는 일반적으로 smooth하지 않다. 실제로 쓰이는 smooth base로는 두 stable map을 marked point에서 붙일 때의 target $X$ 자신과, convex target $\mathbb{P}^N$에 대한 genus $0$ moduli가 있다. ([§안정사상들의 모듈라이 공간, ⁋명제 5](/ko/math/gromov-witten_theory/moduli_of_stable_maps#prop5){: data-lid="sexci" })

Exterior product $\gamma_1\times\gamma_2$는 $k_1+k_2$차원의 class이며, 이것을 codimension $s$ regular local immersion $\Delta_S$가 정의하는 Gysin morphism을 따라 교차시키면 차원이 $s$만큼 떨어져 결과는 $k_1+k_2-s$차원이 된다. 직관적으로 $\Delta_S^!(\gamma_1\times\gamma_2)$는 두 class를 $M_1$과 $M_2$가 $S$에서 같은 값을 갖는 궤적을 따라 교차시킨 것이다. [명제 7](#prop7){: data-lid="zj8u4" }의 commutativity에 의하여, 셋 이상의 인자에 대해서도 이 연산이 associative하다는 것을 보일 수 있다. 우리에게 친숙한 예시는 $M_1,M_2$가 모두 $S$의 closed substack이고 $\gamma_i$가 그 fundamental class인 경우로, 이 때 $\Delta_S^!(\gamma_1\times\gamma_2)$는 [\[스택\] §Deligne–Mumford 스택 위의 적분, ⁋명제 9](/ko/math/stacks/integration_on_deligne_mumford_stacks#prop9){: data-lid="jfsw8" }의 refined intersection class이다.

이제 $\Delta_S^!(\gamma_1\times\gamma_2)$가 실제로 무엇을 계산하는지 풀어 쓰자. 우리는 [정의 3](#def3){: data-lid="f5act" } 앞에서 다음 diagram이 cartesian임을 확인하였다.

{% diagram Math/Gromov_Witten_Theory/Intersection_Theory_of_Virtual_Classes-1.svg width="14.81em" alt="fiber product as the pullback of the diagonal" %}

즉 이는 [정의 3](#def3){: data-lid="qyn7v" }에서 

$$X=S\times S,\qquad W=S,\qquad X'=M_1\times M_2,\qquad W'=M_1\times_SM_2,\qquad i=\Delta_S, \qquad g=f_1\times f_2$$

인 경우이다. 이를 계산하기 위해 우선 étale local model 위에서 diagonal의 ideal sheaf $\mathcal{I}$를 보면, conormal sheaf $\mathcal{I}/\mathcal{I}^2$가 $\Omega_S$와 isomorphic하므로 $\Delta_S$의 normal bundle은 tangent bundle $T_S$로 나온다. 또, $W'=M_1\times_S M_2$에서 $S$로 가는 morphism $f_1\circ\pr_1=f_2\circ\pr_2$를 $f$라 하면, 이 계산으로부터 $g^\ast N=f^\ast T_S$이며 따라서 normal cone $C_{W'/M_1\times M_2}$는 이 vector bundle $f^\ast T_S$ 안에 있게 된다. ([정의 3](#def3){: data-lid="lpj6c" } 직전의 논의) 따라서 $\Delta_S^!(\gamma_1\times\gamma_2)$는 $\gamma_1\times\gamma_2$를 specialization으로 $A_{k_1+k_2}(C_{W'/M_1\times M_2})$의 class로 옮기고, 이를 $f^\ast T_S$ 안의 class로 본 뒤 zero section과 교차시켜 $A_{k_1+k_2-s}(W')$에 내린 것이다.

이를 국소적으로는 다음과 같이 볼 수 있다. 한 점 근방에서 $S$의 étale local model을 smooth scheme $U$와 finite group $G$에 대한 quotient $[U/G]$로 잡으면, $S\times S$의 étale local model은 $[U\times U/G\times G]$이고, 그 위에서 $\Delta_S$의 image는 각 $h\in G$의 graph $\{(u,hu)\}\subseteq U\times U$들의 union으로 주어진다. 이제 이들 중 하나를 택한 후, $U$의 smooth coordinates를 $\t_1,\ldots,\t_s$로 잡으면, 그 graph $\Gamma_h=\{(u_1,u_2):u_2=hu_1\}$은 그 근방에서 $s$개의 식 $\t_a(u_2)-\t_a(hu_1)=0$이 정의하는 공간이며, $\Gamma_h\cong U$가 smooth이므로 이는 regular sequence이다. 이를 $M_1\times M_2$의 해당 étale local model로 당기면 $s$개의 함수

$$\sigma_a(u,v)=\t_a(f_2(v))-\t_a(hf_1(u)),\qquad 1\leq a\leq s$$

를 얻고, 이들의 common zero locus가 고른 $h$에 대응하는 $W'$의 étale local model이다. 즉 국소적으로 $W'$은 $M_1\times M_2$ 위의 trivial rank $s$ vector bundle의 section $\sigma=(\sigma_1,\ldots,\sigma_s)$의 zero locus이다. 핵심적인 사실은 이 trivial bundle을 $W'$로 제한하면 $f^\ast T_S$와 같다는 것으로, 실제로 $\Gamma_h$의 ideal $\mathcal{I}$는 regular sequence $\t_a(u_2)-\t_a(hu_1)$들로 생성되므로 conormal sheaf $\mathcal{I}/\mathcal{I}^2$은 이들의 class를 basis로 갖는 free module이고, isomorphism $\mathcal{I}/\mathcal{I}^2\cong\Omega_S$에서 두 점의 coordinate 차이 $\t_a(u_2)-\t_a(hu_1)$의 class는 그 일차 근사인 $\dd{\t_a}$에 대응한다. 즉, normal bundle $T_S$를 $\dd{\t_a}$의 dual basis $\partial/\partial\t_a$로 trivialize하면, 이 trivialization에서 $\sigma$의 $a$번째 성분이 정확히 $\sigma_a$이다. 

위의 논의로부터 국소적으로 $\Delta_S^!$은 section $\sigma$에 대한 zero-section의 Gysin map이다. 만일 fiber product $W'=M_1\times_SM_2$를 정의하는 식들 $\sigma_1,\ldots,\sigma_s$가 regular sequence이면 $W'$은 $M_1\times M_2$ 안의 codimension $s$ regular embedding이고, normal cone은 vector bundle $f^\ast T_S$ 자체가 되어 $\Delta_S^![M_1\times M_2]$는 zero locus $W'$의 fundamental class가 될 것이다. 문제는 일반적으로 이렇게 pullback해온 식들이 regular sequence라는 보장이 없으므로, 이 가정이 깨지는 경우 normal cone은 vector bundle이 아닐 수 있게 되고 $W'$의 차원이 기대보다 클 수도 있으며, 이 때 실제 zero locus의 fundamental class 대신 위의 construction이 기대차원의 class를 주게 되는 것이다. 

::: 명제 9
[명제 8](#prop8){: data-lid="mpw1x" }의 상황에서 $M_2$가 pure dimensional이고 $f_2:M_2\to S$가 codimension $c$ regular embedding이면, 모든 $\gamma_1\in A_k(M_1)$에 대하여

$$\Delta_S^!(\gamma_1\times[M_2])=f_2^!\gamma_1\in A_{k-c}(M_1\times_SM_2)$$

이다. 여기서 우변은 $f_1:M_1\to S$를 따른 $f_2$의 refined Gysin morphism이다.
:::

::: 증명
$\id\times f_2:M_1\times M_2\to M_1\times S$는 codimension $c$ regular embedding이고, $S$가 smooth이므로 [명제 4](#prop4){: data-lid="boaut" }에서 $f_2^![S]=[M_2]$이다. 따라서 $\gamma_1\times[M_2]=(\id\times f_2)^!(\gamma_1\times[S])$이다. 한편 $\Delta_S$를 $M_1\times S$로 당기면 $f_1$의 graph $M_1\to M_1\times S$가 되는데, 이는 $S$가 smooth이므로 codimension $s$ regular local immersion이고 excess가 없으므로 $\Delta_S^!(\gamma_1\times[S])=\gamma_1$이다. 이제 [명제 7](#prop7){: data-lid="6b1uo" }을 사용하여 $\Delta_S^!$과 $(\id\times f_2)^!$의 순서를 바꾸면

$$\Delta_S^!(\gamma_1\times[M_2])=\Delta_S^!(\id\times f_2)^!(\gamma_1\times[S])=f_2^!\Delta_S^!(\gamma_1\times[S])=f_2^!\gamma_1$$

을 얻는다.
:::

일반적으로 $f_2$는 regular embedding이 아니므로 $M_2$의 defining equation으로 $M_1$을 직접 자를 수 없고, 그래서 $S$가 smooth하기만 하면 언제나 regular local immersion인 diagonal $\Delta_S$로 대신 자르는 것으로 생각할 수 있다. 반면 [명제 9](#prop9){: data-lid="2ldtg" }는 $f_2:M_2\rightarrow S$가 이미 regular embedding이면 diagonal을 거칠 필요 없이, $M_2$의 defining equation으로 $M_1$을 직접 자른 $f_2^!\gamma_1$이 같은 class를 준다는 것이다. 

한편 [명제 8](#prop8){: data-lid="u9xv3" }에 virtual class $\gamma_i=[M_i]^\vir$를 넣으면

$$\Delta_S^!\bigl([M_1]^\vir\times[M_2]^\vir\bigr)\in A_\ast(M_1\times_SM_2)$$

가 fiber product 위의 기대 차원 class를 정의한다. 한쪽에는 virtual class를, 다른 쪽에는 ordinary fundamental class를 넣어도 된다. 다만 fiber product가 그 자체로 moduli라서 따로 POT와 VFC를 갖는 경우, 그 VFC가 이 class와 같은지는 별개의 문제이다. 가령 두 stable map을 붙여 얻는 moduli의 VFC가 두 VFC의 이러한 교차와 같다는 비교에는 두 obstruction theory의 compatibility를 따로 확인해야 한다.

---

**참고문헌**

**[V]** A. Vistoli, *Intersection theory on algebraic stacks and on their moduli spaces*, Invent. Math. **97** (1989), 613–670.
