---
title: "그로모프-위튼 불변량"
description: "Convex target 위의 genus 0 Gromov-Witten invariant를 정의하고, point mapping·string·divisor·splitting 공리와 boundary divisor의 linear equivalence로부터 사영평면의 유리곡선 수에 대한 Kontsevich 공식을 유도한다."
excerpt: "Genus-0 GW invariants of convex targets, their axioms, and Kontsevich's formula"

categories: [Math / Gromov-Witten Theory]
permalink: /ko/math/gromov-witten_theory/gromov-witten_invariants
sidebar: 
    nav: "gromov-witten_theory-ko"

date: 2026-09-15
weight: 3

---

앞선 글에서는 stable map들의 moduli를 구성하였다. 이제 이 공간 위에서 곡선이 주어진 점이나 subvariety를 지나야 한다는 조건을 표현하고, 그 조건들을 동시에 만족하는 곡선을 세어 보자. 이 조건은 evaluation map으로 당겨온 cohomology class로 표현되며, 이들의 곱을 moduli 위에서 적분한 값이 Gromov-Witten invariant이다.

이 글에서는 convex target에 대한 genus $0$ Gromov-Witten invariant를 정의하고, 그 기본 성질들이 moduli의 기하로부터 어떻게 나오는지 살펴본다. Marked point를 잊는 morphism은 string axiom과 divisor axiom을 주며, domain이 두 조각으로 갈라지는 boundary는 splitting axiom과 WDVV equation를 준다. 이 성질들은 서로 다른 조건과 degree에 대한 불변량들을 연결하므로, 정의에서 주어진 moduli 위의 적분을 실제로 계산하는 데 쓰인다.

우리는 이전 글에서 시작한 [FP]를 따라 이 성질들을 전개하고, 그 응용으로서 $\mathbb{P}^2$ 안의 general point $3d-1$개를 지나는 degree $d$ rational curve의 개수 $N_d$를 계산하는 Kontsevish formula를 유도하며 이 흐름을 마친다. 이 수는 Gromov-Witten invariant로 표현되며, 위에서 예고한 성질들을 이용하면 낮은 degree의 값으로부터 재귀적으로 계산할 수 있다.

## 그로모프-위튼 불변량

우리는 stable curve의 $i$번째 marked point가 subvariety $\Gamma_i\subseteq X$를 지난다는 incidence condition을 evaluation map $\ev_i:\overline{\mathcal{M}}_{0,n}(X,\beta)\rightarrow X$를 통해 moduli stack $\overline{\mathcal{M}}_{0,n}(X,\beta)$ 위의 cohomology class $\ev_i^\ast[\Gamma_i]$로 옮겨서 계산한다. 직관적으로 이들의 곱은 이러한 condition들을 모두 만족하는 class에 해당하므로, 이들의 곱을 moduli 전체에서 적분하면 모든 조건을 동시에 만족하는 stable map의 개수에 해당하는 수를 얻는다. 

우리는 이미 [§안정사상들의 모듈라이 공간, ⁋명제 5](/ko/math/gromov-witten_theory/moduli_of_stable_maps#prop5){: data-lid="5omgf" data-relation="required" reviewed="" }에서 $\overline{\mathcal{M}}_{0,n}(X,\beta)$는 smooth proper Deligne–Mumford stack인 것을 살펴보았다. 따라서 특히 [\[스택\] §Deligne–Mumford 스택 위의 적분, ⁋정의 4](/ko/math/stacks/integration_on_deligne_mumford_stacks#def4){: data-lid="7zvbr" data-relation="required" reviewed="" }이 잘 적용된다. 

::: 정의 1
주어진 cohomology class $\gamma_1,\ldots,\gamma_n\in H^\ast(X,\mathbb{Q})$에 대하여, *Gromov-Witten invariant<sub>그로모프-위튼 불변량</sub>*을

$$\langle\gamma_1,\ldots,\gamma_n\rangle_{0,n,\beta}=\int_{\overline{\mathcal{M}}_{0,n}(X,\beta)}\ev_1^\ast\gamma_1\smile\cdots\smile\ev_n^\ast\gamma_n$$

으로 정의한다.
:::

예를 들어, [\[스택\] §Deligne–Mumford 스택 위의 적분, ⁋보조정리 3](/ko/math/stacks/integration_on_deligne_mumford_stacks#lem3){: data-lid="e9fi8" data-relation="required" reviewed="" }에서 살펴본 것과 같이, 일반적으로 위 식의 값은 유리수가 나온다. 

뿐만 아니라, 정의로부터 바로 나오는 사실이 몇 가지 있다. 우선 일반적으로 두 insertion $\gamma_i,\gamma_j$를 교환할 때는

$$(-1)^{\deg\gamma_i\deg\gamma_j}$$

의 Koszul sign이 생긴다. 하지만 우리 경우에는 cycle class map을 통해

$$A^k(X)_\mathbb{Q}\rightarrow H^{2k}(X, \mathbb{Q})$$

을 통해 얻어지는 class들에만 관심있으므로, 이하의 공리들은 모든 $\gamma_i$가 even degree인 경우에 서술한다. 특히 불변량은 insertion의 순서에 의존하지 않는다.

한편, 각 $\gamma_i$가 homogeneous일 때 피적분식의 degree가 moduli stack의 (virtual) dimension과 맞지 않으면 불변량은 $0$이다. 따라서 genus $0$의 primary Gromov-Witten invariant가 $0$이 아닐 수 있으려면 반드시

$$\vdim_\mathbb{C}\overline{\mathcal{M}}_{0,n}(X,\beta)=\sum_{i=1}^n\codim\gamma_i=\int_\beta c_1(T_X)+\dim X+n-3$$

이어야 한다. 

이제 $N_d$를 Gromov-Witten invariant로 나타내자. $X=\mathbb{P}^2$이라 하고 line의 class를 $h\in H^2(\mathbb{P}^2)$로 적으면 $h^2$은 점의 class이다. Degree $d$인 curve class를 간단히 $d$로 적으면, $c_1(T_{\mathbb{P}^2})=3h$이므로

$$\vdim\overline{\mathcal{M}}_{0,n}(\mathbb{P}^2,d)=3d-1+n$$

이 성립한다. 이 때, 한 점을 지난다는 조건은 codimension $2$이므로, 위에서 살펴본 것과 같이 $n$개의 점 조건과 virtual dimension이 맞으려면 $2n=3d-1+n$, 즉 $n=3d-1$이어야 한다. 따라서 자연스럽게

$$N_d=\langle h^2,\ldots,h^2\rangle_{0,3d-1,d}$$

를 얻는다. 

실제로 $3d-1$개의 점 $q_1,\ldots,q_{3d-1}\in\mathbb{P}^2$를 general하게 잡으면, 이 점 조건을 만족하는 stable map은 boundary나 multiple cover에 놓이지 않는다. 따라서 evaluation map의 한 점 위 fiber의 각 점은 $(\mathbb{P}^1,p_1,\ldots,p_{3d-1},\mu)$의 꼴로, $\mu:\mathbb{P}^1\rightarrow\mathbb{P}^2$는 그 image와 birational하다. 또, general point condition 아래에서는 각 $q_i$가 image curve의 smooth point에 놓이므로 $\mu(p_i)=q_i$를 만족하는 marked point $p_i$도 유일하게 결정된다. 특히 이러한 stable map은 nontrivial automorphism을 갖지 않으며, 각 general evaluation fiber는 reduced이므로 이 stable map은 stack-theoretic weight나 intersection multiplicity 없이 정확히 multiplicity $1$로 세어진다.

이제 stable map에 그 image curve $\mu(\mathbb{P}^1)$를 대응시키면, 이는 $q_1,\ldots,q_{3d-1}$을 지나는 degree $d$ rational plane curve가 되며 반대로 이러한 curve $C\subset\mathbb{P}^2$가 주어지면, 그 normalization

$$\mathbb{P}^1\rightarrow C\hookrightarrow\mathbb{P}^2$$

과 각 $q_i$의 unique preimage를 marked point로 잡아 stable map을 복원할 수 있다. 따라서 general point condition 아래에서 evaluation fiber의 점들과 $q_1,\ldots,q_{3d-1}$을 지나는 degree $d$ rational plane curve들은 일대일 대응하고, 각 점이 multiplicity $1$로 세어지므로 $N_d=\langle h^2,\ldots,h^2\rangle_{0,3d-1,d}$가 성립한다.

우선 우리는 가장 간단한 예시로 다음을 계산한다. 

::: 명제 2
$n\geq3$에 대하여, $\overline{\mathcal{M}}_{0,n}(X,0)\cong\overline{\mathcal{M}}_{0,n}\times X$이고,

$$\langle\gamma_1,\ldots,\gamma_n\rangle_{0,n,0}=\begin{cases}\displaystyle\int_X\gamma_1\smile\gamma_2\smile\gamma_3&(n=3)\\0&(n\geq4)\end{cases}$$

이다.
:::
::: 증명
$\beta=0$인 stable map은 domain을 한 점 $x\in X$로 보내는 constant map이므로, 남는 자료는 $n$-pointed stable curve $(C,p_1,\ldots,p_n)$와 점 $x$뿐이다. 따라서 $\overline{\mathcal{M}}_{0,n}(X,0)\cong\overline{\mathcal{M}}_{0,n}\times X$이며, 이 isomorphism 아래 모든 $\ev_i$는 둘째 성분으로의 projection $\mathrm{pr}_X$가 된다. 그럼

$$\ev_1^\ast\gamma_1\smile\cdots\smile\ev_n^\ast\gamma_n=\mathrm{pr}_X^\ast(\gamma_1\smile\cdots\smile\gamma_n)$$

이고, [\[스택\] §Deligne–Mumford 스택 위의 적분, §§곱공간과 대각선 교차](/ko/math/stacks/integration_on_deligne_mumford_stacks#곱공간과-대각선-교차){: data-lid="v64ai" data-relation="required" reviewed="" }의 곱의 적분 공식에 의하여 이를 $\overline{\mathcal{M}}_{0,n}\times X$ 위에서 적분하면 

$$\left(\int_{\overline{\mathcal{M}}_{0,n}}1\right)\left(\int_X\gamma_1\smile\cdots\smile\gamma_n\right)$$

이다. 이제 첫째 인자는 $\dim\overline{\mathcal{M}}_{0,n}=n-3>0$인 $n\geq4$에서 $0$이고, $n=3$에서는 $\overline{\mathcal{M}}_{0,3}$이 한 점이므로 $1$이다.
:::

## 그로모프-위튼 불변량의 공리들

이제 우리는 위에서 정의한 Gromov-Witten invariant가 만족해야 할 공리들을 하나씩 살펴본다. 먼저 stable map의 moduli 사이에는 마지막 marked point를 잊고 필요한 경우 domain을 다시 stabilize하는 forgetful morphism

$$\pi:\overline{\mathcal{M}}_{0,n+1}(X,\beta)\rightarrow\overline{\mathcal{M}}_{0,n}(X,\beta)$$

이 존재한다.

앞선 글에서 보았듯 이 morphism은 universal curve의 역할을 한다. 실제로 stable map $(C,p_1,\ldots,p_n,\mu)$을 하나 고정하면, 그 위의 fiber는 마지막 marked point $p_{n+1}$이 움직이는 domain $C$로 생각할 수 있다. 다른 말로 하면, $(n+1)$번째 evaluation map을 이 fiber에 제한하면 원래의 map

$$\ev_{n+1}\vert_C=\mu:C\rightarrow X$$

를 얻는다.

한편 $i\leq n$인 기존 marked point들의 evaluation 값은 마지막 marked point를 잊어도 변하지 않는다. 실제로 stabilization 과정에서 점으로 갈 수 있는 component는 $\mu$가 constant인 component뿐이므로, 그러한 component가 수축되더라도 기존 marked point의 image는 그대로 유지된다. 따라서

$$\ev_i^{(n+1)}=\ev_i^{(n)}\circ\pi,\qquad i=1,\ldots,n$$

가 성립한다. 이하에서는 혼동의 여지가 없을 때 위첨자를 생략하여 간단히 $\ev_i=\ev_i\circ\pi$로 적는다.

이제 마지막 marked point에 class $1\in H^0(X)$을 얹는 것은 그 점에 아무 조건도 걸지 않는다는 뜻이므로, 나머지 조건을 만족하는 stable map이 있다면 새 marked point를 domain 위에서 자유롭게 움직여 $1$차원 family의 해를 얻게 되며, 이러한 이유로 Gromov-Witten invariant를 계산할 때 차원이 맞지 않아 그 값이 $0$이 된다. 이것이 문제가 될 수 있는 경우는 moduli space가 stability로 인해 불연속적으로 행동할 수 있는 $\beta=0$이고 $n\leq 2$인 경우들 뿐이며, 이를 형식적으로 적으면 다음과 같다. 

::: 명제 3 (String axiom)
$\beta\neq0$이거나 $n\geq3$이면

$$\langle\gamma_1,\ldots,\gamma_n,1\rangle_{0,n+1,\beta}=0$$

이다.
:::
::: 증명
가정에 의하여 $\overline{\mathcal{M}}_{0,n}(X,\beta)$이 정의되므로 $\pi$를 쓸 수 있다. $\ev_i=\ev_i\circ\pi$와 [\[스택\] §Deligne–Mumford 스택 위의 적분, ⁋명제 7](/ko/math/stacks/integration_on_deligne_mumford_stacks#prop7){: data-lid="4bxwp" data-relation="required" reviewed="" }에 의하여

$$\langle\gamma_1,\ldots,\gamma_n,1\rangle_{0,n+1,\beta}=\int_{\overline{\mathcal{M}}_{0,n+1}(X,\beta)}\pi^\ast\Bigl(\prod_{i=1}^n\ev_i^\ast\gamma_i\Bigr)=\int_{\overline{\mathcal{M}}_{0,n}(X,\beta)}\pi_\ast(1)\smile\prod_{i=1}^n\ev_i^\ast\gamma_i$$

이다. 그런데 $\pi$는 relative dimension $1$의 morphism이므로 fundamental class의 pushforward $\pi_\ast(1)$은 degree $-2$의 class가 되어 $0$이다.
:::

한편, 위의 증명을 살펴보면 결국 적분을 $0$으로 만드는 것은 $\pi_\ast (1)$이므로, 이번에는 $1$ 대신 마지막 marked point에 divisor $D$의 class를 얹으면 $\pi_\ast(\ev_{n+1}^\ast D)$가 degree $0$의 class가 되어 적분이 올바른 차원에서 행해지게 된다. 즉 다음을 얻는다. 

::: 명제 4 (Divisor axiom)
$D\in H^2(X,\mathbb{Q})$이고 $\beta\neq0$이면

$$\langle\gamma_1,\ldots,\gamma_n,D\rangle_{0,n+1,\beta}=\left(\int_\beta D\right)\langle\gamma_1,\ldots,\gamma_n\rangle_{0,n,\beta}$$

이다.
:::
::: 증명
$\pi$는 proper flat representable family of nodal curves이므로 [\[스택\] §Deligne–Mumford 스택 위의 적분, ⁋명제 8](/ko/math/stacks/integration_on_deligne_mumford_stacks#prop8){: data-lid="mf2jg" data-relation="required" reviewed="" }에 의하여 $\pi_\ast(\ev_{n+1}^\ast D)$의 값은 scheme fiber 위의 적분으로 계산되고, stable map $(C,p_\bullet,\mu)$ 위의 fiber에서 $\ev_{n+1}$은 $\mu$이므로 그 값은

$$\int_C\mu^\ast D=\int_{\mu_\ast[C]}D=\int_\beta D$$

이다. 따라서 $\pi_\ast(\ev_{n+1}^\ast D)$는 fiber에 무관한 상수 $\int_\beta D$이고, 이를 [명제 3](#prop3){: data-lid="y5lor" data-relation="required" }의 증명과 같은 projection formula 계산에 대입하면 남는 적분이 $\langle\gamma_1,\ldots,\gamma_n\rangle_{0,n,\beta}$이다.
:::

위의 결과들은 모두 forgetful morphism으로부터 나오는 것이었으나, moduli space에 풍부한 조합론적 데이터를 주는 것은 boundary 구조였다. Marked point 집합의 분할 $\{1,\ldots,n\}=A\sqcup B$와 effective class의 분해 $\beta=\beta_1+\beta_2$에 대하여, domain이 node 하나에서 갈라지고 $A$와 $\beta_1$과 $B$와 $\beta_2$가 각각의 조각에 놓이는 stable map들의 locus를 $D(A,B;\beta_1,\beta_2)$로 적는다. 

그럼 이렇게 얻어진 $D(A, B; \beta_1, \beta_2)$가 전체 moduli space의 codimension $1$ locus, 즉 divisor가 된다. 두 조각에는 이름이 없으므로 $D(A,B;\beta_1,\beta_2)$와 $D(B,A;\beta_2,\beta_1)$은 같은 divisor이며, 전체 moduli space의 boundary는 이러한 divisor들의 합집합이고 이들이 stack 위에서 étale-local하게 normal crossing을 이룬다는 것이 알려져 있다. 

이제 $A$와 $B$가 모두 공집합이 아닐 때 각 성분은 [§안정사상들의 모듈라이 공간, §§안정사상들의 모듈라이 공간](/ko/math/gromov-witten_theory/moduli_of_stable_maps#안정사상들의-모듈라이-공간){: data-lid="qcz34" data-relation="required" }의 gluing morphism

$$\overline{\mathcal{M}}_{0,A\cup\{\bullet\}}(X,\beta_1)\times_X\overline{\mathcal{M}}_{0,B\cup\{\bullet\}}(X,\beta_2)\rightarrow\overline{\mathcal{M}}_{0,n}(X,\beta)$$

의 image이고, 두 조각을 구별할 수 있으므로 이 morphism은 image로의 isomorphism이다. 즉 두 조각이 node에서 붙어 있다는 조건은 위 fiber product에 따르면 $(\ev_\bullet,\ev_\bullet)$이 diagonal $\Delta_X\subseteq X\times X$로 간다는 조건으로 해석할 수 있다.

한편 우리는 이미 [\[스택\] §Deligne–Mumford 스택 위의 적분, ⁋명제 9](/ko/math/stacks/integration_on_deligne_mumford_stacks#prop9){: data-lid="9wmoh" data-relation="required" reviewed="" }에서, 이러한 상황에서의 refined class를 계산하는 방법을 살펴보았다. 두 조각의 moduli를 $M_A=\overline{\mathcal{M}}_{0,A\cup\{\bullet\}}(X,\beta_1)$, $M_B=\overline{\mathcal{M}}_{0,B\cup\{\bullet\}}(X,\beta_2)$로 적으면, convex target에서는 이 교차에 여분의 성분이 생기지 않으므로 $D(A,B;\beta_1,\beta_2)$ 위에서 $\prod_i\ev_i^\ast\gamma_i$를 적분하는 것은 refined fundamental class에 대한 적분

$$\int_{M_A\times M_B}\Bigl(\prod_{a\in A}\ev_a^\ast\gamma_a\otimes\prod_{b\in B}\ev_b^\ast\gamma_b\Bigr)\smile(\ev_\bullet,\ev_\bullet)^\ast[\Delta_X]$$

를 계산하는 것과 같다.

이를 계산하기 위해 $H^\ast(X,\mathbb{Q})$의 homogeneous basis $T_0,\ldots,T_m$과, Poincaré dual basis $T^0,\ldots,T^m$을 고정하자. 이하 $H^{\mathrm{odd}}(X)=0$인 경우만 생각한다. 그럼 diagonal의 class는 

$$[\Delta_X]=\sum_kT_k\otimes T^k$$

로 분해할 수 있으며, 이를 사용해서 위의 적분을 $M_A$ 위의 적분과 $M_B$ 위의 적분으로 갈라놓을 수 있다. 물론 이 때 $M_A$와 $M_B$는 stability condition을 만족한다고 가정한다. 

::: 명제 5 (Splitting axiom)
Stability condition을 만족하는 데이터 $(A,B;\beta_1,\beta_2)$에 대하여 $A,B$가 공집합이 아니면

$$\int_{D(A,B;\beta_1,\beta_2)}\prod_{i=1}^n\ev_i^\ast\gamma_i=\sum_k\langle\gamma_A,T_k\rangle_{0,\lvert A\rvert+1,\beta_1}\langle T^k,\gamma_B\rangle_{0,\lvert B\rvert+1,\beta_2}$$

이 성립한다.
:::

물론 우변의 합 내부에서 있는 각 성분은 올바른 차원에서만 $0$이 아니므로 이 조건까지 포함하에 식을 쓸 수는 있겠지만, 그것이 필수는 아니므로 이 형태를 유지하기로 한다.  

위의 계산은 smooth domain을 갖는 stable map이 이미 한 번 <em-ko>부러진</em-ko> 상태, 즉 domain이 nodal curve로 한 번 퇴화한 상태에서 적분값을 계산하는 방법을 보여준다. 그런데 smooth domain을 갖는 stable map을 이러한 식으로 퇴화시키는 방법은 하나가 아니다. 가장 작은 경우로 marked point 네 개, $\{1,2,3,4\}$가 주어졌다 했을 때, 이를 두 조각으로 나누는 방법은 

$$\{1,2\}\sqcup\{3,4\},\qquad \{1,3\}\sqcup\{2,4\},\qquad \{1,4\}\sqcup\{2,3\}$$

의 셋이 있으며 이렇게 도달한 boundary들은 성분의 구성이 서로 전혀 다르다는 것을 이미 설명하였다. 그럼에도 불구하고 이들이 up to linear equivalence에 대해서는 차이나지 않는다는 것이 우리의 다음 결과이다. 

주장은 네 개의 marked point를 갖는 stable map의 domain에 대한 것이므로 moduli $\overline{\mathcal{M}}_{0,4}$에서만 확인해도 된다. Smooth curve $\mathbb{P}^1$ 위의 네 점의 위치를 택하는 방법은, automorphism $\PGL_2$을 고려한 후에는, 세 점 $p_1,p_2,p_3$을 $0,1,\infty$로 고정한 후 $p_4$의 위치를 자유롭게 결정하는 것과 정확히 같다. 그럼 이제 위에서 살펴본 세 가지 분할 방법은 이 네 번째 점이 $p_1,p_2,p_3$ 중 하나와 충돌하는 극한이 되며, $p_4$의 위치는 $\overline{\mathcal{M}}_{0,4}\cong\mathbb{P}^1$의 좌표이므로 이렇게 $p_4$를 움직이는 것이 정확히 이 서로 다른 configuration을 이어주는 linear equivalence가 된다. 

이제 이 논증은 임의의 $n\geq 4$짜리 moduli space $\overline{\mathcal{M}}_{0,n}(X,\beta)$에서, 관심있는 네 개의 점을 택하여 해당 점들에서 적용할 수 있다. 서술의 편의상 처음 네 점을 우리의 관심대상이라 하고 위의 논의의 결과를 적으면 다음과 같다. 

::: 명제 6 (WDVV equation)
$n\geq4$와 $\gamma_1,\ldots,\gamma_n\in H^{\mathrm{even}}(X,\mathbb{Q})$에 대하여

$$\sum_{\substack{A\ni1,2\\ B\ni3,4\\ \beta_1+\beta_2=\beta}}\sum_k\langle\gamma_A,T_k\rangle_{0,\lvert A\rvert+1,\beta_1}\langle T^k,\gamma_B\rangle_{0,\lvert B\rvert+1,\beta_2}=\sum_{\substack{A\ni1,3\\ B\ni2,4\\ \beta_1+\beta_2=\beta}}\sum_k\langle\gamma_A,T_k\rangle_{0,\lvert A\rvert+1,\beta_1}\langle T^k,\gamma_B\rangle_{0,\lvert B\rvert+1,\beta_2}=\sum_{\substack{A\ni1,4\\ B\ni2,3\\ \beta_1+\beta_2=\beta}}\ldots$$

이 성립한다.
:::

::: 증명
$X$로 가는 map을 잊고, domain curve를 stabilize한 뒤 처음 네 marked point만 남기면 morphism

$$\phi:\overline{\mathcal{M}}_{0,n}(X,\beta)\rightarrow\overline{\mathcal{M}}_{0,4}$$

를 얻는다. Boundary point $\{1,2\}\sqcup\{3,4\}$의 preimage는 $A\ni1,2$, $B\ni3,4$인 $D(A,B;\beta_1,\beta_2)$들의 합집합이고, 각 성분의 일반적인 점 근처에서 그 node의 smoothing parameter가 양쪽에서 같은 국소좌표를 주므로 이 preimage는 multiplicity $1$로 나타난다. 따라서 위에서 설명한 linear equivalence를 $\phi^\ast$로 당겨오면

$$\sum_{\substack{A\ni1,2, B\ni3,4\\ \beta_1+\beta_2=\beta}}D(A,B;\beta_1,\beta_2)\sim\sum_{\substack{A\ni1,3, B\ni2,4\\ \beta_1+\beta_2=\beta}}D(A,B;\beta_1,\beta_2)$$

이다. 이제 양변에 $\prod_i\ev_i^\ast\gamma_i$를 곱해 적분하면 두 값이 같고, 각 항에서 $A,B$는 모두 marked point를 둘 이상 포함하므로 [명제 5](#prop5){: data-lid="0m7u6" data-relation="required" }를 적용하면 주장의 양변을 얻는다.
:::

## Kontsevich 공식

이 글의 도입부에서 설명했듯 우리의 목표는 $N_d$를 구하는 것이다. 이를 위해 우리는 genus $0$ Gromov-Witten invariant가 실제로 이 값을 담아내는 것을 보았고, 이 Gromov-Witten invariant가 갖는 성질 또한 확인하였으므로 남은 것은 식을 유도하는 것 뿐이다. 

우리 상황에서 $X=\mathbb{P}^2$이고, $T_0=1$, $T_1=h$, $T_2=h^2$로 두면 $T^k=T_{2-k}$이다. 핵심적인 아이디어는 [명제 6](#prop6){: data-lid="9d28y" data-relation="required" }을 사용하여 이 값을 recursive하게 식으로 써 주는 것이다. 이를 위해서는 incidence condition이 부여하는 $3d-1$개 중 하나를 덜 사용해야 하고, 이렇게 하나의 점을 뺐을 때 적분의 degree가 맞아서 $0$ 아닌 값이 나오기 위해서는 직선 두 개를 넣어주어야 한다. 즉 우리는 점 $3d-2$개와 직선 $2$개에 대한 incidence condition이 주어진, $n=3d$개의 marked point를 갖는 moduli 위의 class를 생각한다. [명제 6](#prop6){: data-lid="a8kwg" data-relation="required" }을 사용하기 위해, 이 직선 두 개를 앞쪽에 넣어 insertion class들을

$$\gamma_1=\gamma_2=h^2,\qquad\gamma_3=\gamma_4=h,\qquad\gamma_5=\cdots=\gamma_n=h^2$$

으로 두자. 그럼 실제로 codimension의 합은 $2(3d-2)+2=6d-2$이고 이것이 $\vdim\overline{\mathcal{M}}_{0,3d}(\mathbb{P}^2,d)-1=6d-2$와 같다는 것을 확인할 수 있다.

::: 정리 7 (Kontsevich)
$d\geq2$에 대하여

$$N_d=\sum_{\substack{d_1+d_2=d\\ d_1,d_2\geq1}}N_{d_1}N_{d_2}\left[d_1^2d_2^2\binom{3d-4}{3d_1-2}-d_1^3d_2\binom{3d-4}{3d_1-1}\right]$$

이 성립한다.
:::
::: 증명
위에서 말한 것과 같이 이 세팅에 [명제 6](#prop6){: data-lid="lhuki" data-relation="required" }을 적용한다. 나머지 marked point의 집합 $S=\{5,\ldots,n\}$은 $3d-4$개의 원소를 가지며, 분할 $A\sqcup B$는 처음의 네 점짜리 집합의 분할에 나머지 점들의 집합 $S$의 분할 $S_1\sqcup S_2$를 얹는 것으로 정해진다. 

우선 식의 좌변을 $A=\{1,2\}\sqcup S_1$, $B=\{3,4\}\sqcup S_2$, degree를 $d_1+d_2=d$로 나눈 것으로 두면, 각 summand는 

$$\langle h^2,h^2,(h^2)_{S_1},T_k\rangle_{0,\lvert A\rvert+1,d_1}\langle T_{2-k},h,h,(h^2)_{S_2}\rangle_{0,\lvert B\rvert+1,d_2}$$

의 꼴이다.  

만일 $d_1=0$이라면, [명제 2](#prop2){: data-lid="uzmtm" data-relation="required" }에 의해 첫째 인자가 $0$이 아니기 위해서는 반드시 $S_1=\emptyset$이어야 한다. 그런데 이 경우에도 첫째 인자가 차원 문제로

$$\int h^2\smile h^2\smile T_k=0$$

이 되므로 $d_1=0$인 경우는 이 합에서 기여하는 바가 없다. 만일 $d_2=0$이라면, 마찬가지 이유로 $S_2=\emptyset$이어야 한다. 차이는 이 경우엔 $0$ 아닌 항이 나온다는 것으로, 우선 둘째 인자가 $0$이 아니기 위해서는 적분

$$\int T_{2-k}\smile h\smile h$$

이 $0$이 아니어야 하므로 반드시 $k=2$여야 한다. 뿐만 아니라, $k=2$인 경우의 첫째 인자를 계산하면, $T_2$가 point class이므로 이 값은 정확히 우리가 구하고자 하는 $N_d$이다. 즉 $d_2=0$인 경우는 [명제 6](#prop6){: data-lid="jvr2t" data-relation="required" }의 좌변에서 정확히 $N_d$로 기여하고, $d_1=0$인 경우는 이 좌변에서 어떠한 기여도 없다. 

이제 나머지 경우, 즉 $d_1,d_2$가 모두 $0$이 아닌 경우를 보자. 그럼 [명제 3](#prop3){: data-lid="w7b4c" data-relation="required" }에 의하여 $k=0$이 기여하는 부분과 $k=2$가 기여하는 부분이 사라지므로 남는 것은 $k=1$에 대한 항 뿐이다. 역시 이 경우의 차원 조건을 맞춰주면, 첫째 인자의 차원 조건으로부터

$$4+2\lvert S_1\rvert+1=3d_1+2+\lvert S_1\rvert$$

이므로 $\lvert S_1\rvert=3d_1-3$여야 하고, 이 때의 값은 [명제 4](#prop4){: data-lid="ybjc8" data-relation="required" }에 의하여 $d_1N_{d_1}$이다. 이 때, $\lvert S_1\rvert=3d_1-3$인 것은 $\lvert S_2\rvert=3d_2-1$일 것을 강제하며, 이 상황에서 둘째 인자는 [명제 4](#prop4){: data-lid="l70dv" data-relation="required" }를 세 번 적용하여 $d_2^3N_{d_2}$이 된다. 이제 집합 $S_1$을 고르는 방법은 $\binom{3d-4}{3d_1-3}$가지이므로 좌변은

$$N_d+\sum_{\substack{d_1+d_2=d\\ d_1,d_2\geq1}}d_1d_2^3\binom{3d-4}{3d_1-3}N_{d_1}N_{d_2}$$

가 된다.

남은 것은 우변으로, $A=\{1,3\}\sqcup S_1$, $B=\{2,4\}\sqcup S_2$인 경우를 보자. 이 경우, 위에서 살펴본 것과 비슷하게 각 summand는

$$\langle h^2,h,(h^2)_{S_1},T_k\rangle_{0,\lvert A\rvert+1,d_1}\langle T_{2-k},h^2,h,(h^2)_{S_2}\rangle_{0,\lvert B\rvert+1,d_2}$$

으로 나온다. 만일 $d_1=0$이면 첫째 인자가 

$$\int h^2\smile h\smile T_k=0$$

이고, $d_2=0$일 때도 같은 계산으로 둘째 인자가 $0$이 되므로 합에 기여하는 것은 $d_1,d_2\neq 0$인 경우 뿐이다. 이 경우, 좌변에서의 계산과 마찬가지로 $k=1$에 대한 부분만 남으며, 차원 조건이 $\lvert S_1\rvert=3d_1-2$와 $\lvert S_2\rvert=3d_2-2$를 강제한다. 이제 각각의 인자에 [명제 4](#prop4){: data-lid="oqs4h" data-relation="required" }를 두 번씩 적용하면 첫째 인자는 $d_1^2N_{d_1}$, 둘째 인자는 $d_2^2N_{d_2}$가 나오고, 따라서 $S_1$을 택하는 경우의 수까지 포함하면 우변은

$$\sum_{\substack{d_1+d_2=d\\ d_1,d_2\geq1}}d_1^2d_2^2\binom{3d-4}{3d_1-2}N_{d_1}N_{d_2}$$

이다. 이제 양변을 비교하면 주장한 식을 얻는다. 
:::

이 글 전체는 $X$가 convex여서 $\overline{\mathcal{M}}_{0,n}(X,\beta)$이 기대 차원을 갖는 smooth stack이고 따라서 virtual fundamental class가 통상적인 fundamental class와 일치한다는 사실에 전적으로 의존하였다. 반면 일반적인 target이나 positive genus에서는 moduli가 기대 차원보다 큰 성분을 가질 수 있으므로, [정의 1](#def1){: data-lid="5tj19" data-relation="required" }의 fundamental class를 virtual fundamental class로 대체해야 한다.

---

**참고문헌**

**[FP]** W. Fulton, R. Pandharipande, *Notes on stable maps and quantum cohomology*, in Algebraic Geometry — Santa Cruz 1995, Proc. Sympos. Pure Math. **62**, Part 2, AMS, 1997, pp. 45–96.  
**[CK]** D. A. Cox, S. Katz, *Mirror Symmetry and Algebraic Geometry*, Mathematical Surveys and Monographs **68**, AMS, 1999.
