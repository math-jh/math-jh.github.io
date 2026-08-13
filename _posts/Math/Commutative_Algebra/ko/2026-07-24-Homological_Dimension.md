---
title: "호몰로지 차원"
description: "Module의 projective dimension과 injective dimension, 그리고 global dimension을 정의하고, Noetherian local ring의 최소 자유 분해 이론으로 regular local ring의 global dimension이 차원과 같음을 보인 뒤, Hilbert syzygy 정리로 다항식환의 global dimension이 변수의 개수와 같음을 증명한다."
excerpt: "Projective/injective/global dimension과 Hilbert syzygy 정리"

categories: [Math / Commutative Algebra]
permalink: /ko/math/commutative_algebra/homological_dimension
sidebar: 
    nav: "commutative_algebra-ko"

date: 2026-07-24
weight: 26
published: false
drift_needed: true

---

[\[호몰로지 대수학\] §Ext와 Tor](/ko/math/homological_algebra/ext_and_tor)의 마지막에서 우리는 field $\mathbb{K}$ 위의 polynomial ring $\mathbb{K}[\x_1,\ldots, \x_n]$의 Koszul complex를 계산하며, 이 계산이 나중에 이 ring의 global dimension이 $n$임을 보이는 데 쓰인다고 예고하였다. 이 글은 그 약속을 이행한다. 우리는 module의 projective dimension과 injective dimension을 정의하고, 이들의 supremum으로 ring의 global dimension을 도입한다. 이어 Noetherian local ring에서 최소 자유 분해의 이론을 세워 global dimension을 Tor의 소멸 차수로 읽어내고, 이를 통해 regular local ring의 global dimension이 그 Krull 차원과 같음을 확인한다. 마지막으로 변수를 하나 더할 때 global dimension이 어떻게 변하는지 추적하여 Hilbert syzygy 정리를 증명한다.

## 사영차원과 단사차원

[\[호몰로지 대수학\] §분해, ⁋명제 3](/ko/math/homological_algebra/resolutions#prop3)과 [⁋명제 4](/ko/math/homological_algebra/resolutions#prop4)에 의하여 임의의 $A$-module $M$은 projective resolution을 가진다. 그러나 이 분해가 유한한 길이에서 끝나는지, 끝난다면 얼마나 짧아질 수 있는지는 $M$마다 다르며, 이 최소 길이는 $M$의 중요한 불변량이 된다. 우리는 이를 다음과 같이 정의한다.

::: 정의 1
$A$-module $M$에 대하여 다음을 정의한다.

1. $M$의 *projective dimension<sub>사영차원</sub>* $\pd_A M$은 $M$의 projective resolution의 최소 길이이다. 즉 $0 \rightarrow P_n \rightarrow \cdots \rightarrow P_0 \rightarrow M \rightarrow 0$이 exact이도록 하는 projective module들 $P_0,\ldots, P_n$이 존재하는 가장 작은 $n$이며, 그러한 유한 분해가 없으면 $\pd_A M=\infty$이다.
2. $M$의 *injective dimension<sub>단사차원</sub>*은 injective resolution의 최소 길이로 쌍대적으로 정의하며, $\operatorname{injdim}_A M$으로 적는다.
:::

Projective dimension은 $\pd$로 적고, injective dimension에는 $\operatorname{injdim}$을 쓴다. 관례적인 표기 $\operatorname{id}$는 identity morphism과 겹치므로 피한다. 정의에 의하여 $\pd_A M=0$인 것은 $M$이 projective module인 것과 동치이고, 마찬가지로 $\operatorname{injdim}_A M=0$인 것은 $M$이 injective module인 것과 동치이다.

이 불변량들을 다루는 기본 도구는 $\Ext$의 long exact sequence이다. $\Ext_A^i(M,-)$은 left exact functor $\Hom_A(M,-)$의 right derived functor이므로 ([\[호몰로지 대수학\] §Ext와 Tor, ⁋정의 1](/ko/math/homological_algebra/ext_and_tor#def1), [\[호몰로지 대수학\] §유도함자, ⁋정의 9](/ko/math/homological_algebra/derived_functors#def9)), cohomological $\delta$-functor로서 둘째 변수의 short exact sequence마다 long exact sequence를 유도한다. ([\[호몰로지 대수학\] §유도함자, ⁋정의 1](/ko/math/homological_algebra/derived_functors#def1)) 또, [\[호몰로지 대수학\] §Ext와 Tor, ⁋명제 3](/ko/math/homological_algebra/ext_and_tor#prop3)의 balancing에 의하여 $\Ext$는 첫째 변수의 projective resolution으로도 계산되므로, 첫째 변수의 short exact sequence $0 \rightarrow M' \rightarrow M \rightarrow M'' \rightarrow 0$ 또한 long exact sequence
$$\cdots \rightarrow \Ext_A^i(M'',N) \rightarrow \Ext_A^i(M,N) \rightarrow \Ext_A^i(M',N) \rightarrow \Ext_A^{i+1}(M'',N) \rightarrow \cdots$$
를 유도한다.

Projective dimension을 $\Ext$로 특징짓기 위해 syzygy를 도입한다. Projective resolution $\cdots \rightarrow P_1 \overset{d_1}{\longrightarrow} P_0 \overset{\epsilon}{\longrightarrow} M \rightarrow 0$이 주어지면, $\Omega^0 M=M$으로 두고 각각의 $i\geq 0$에 대하여 $\Omega^{i+1}M=\ker(P_i \rightarrow \Omega^i M)$으로 정의한다. 그럼 $\Omega^1 M=\ker\epsilon$이고 $i\geq 1$에서 $\Omega^{i+1}M=\ker d_i$이며, 각각의 $i$에 대하여 short exact sequence
$$0 \rightarrow \Omega^{i+1}M \rightarrow P_i \rightarrow \Omega^i M \rightarrow 0$$
을 얻는다. $\Omega^n M$을 (선택한 resolution에 대한) $M$의 *$n$번째 syzygy*라 부른다.

::: 명제 2
$A$-module $M$과 정수 $n\geq 0$에 대하여 다음이 모두 동치이다.

1. $\pd_A M\leq n$이다.
2. 모든 $A$-module $N$과 $i>n$에 대하여 $\Ext_A^i(M,N)=0$이다.
3. 모든 $A$-module $N$에 대하여 $\Ext_A^{n+1}(M,N)=0$이다.
4. $M$의 임의의 projective resolution에 대하여, 그 $n$번째 syzygy $\Omega^n M$은 projective이다.
:::
::: 증명
(4)$\Rightarrow$(1)을 보이자. 어떤 projective resolution에서 $\Omega^n M$이 projective라면, syzygy의 short exact sequence들을 이어 붙여 얻는
$$0 \rightarrow \Omega^n M \rightarrow P_{n-1} \rightarrow \cdots \rightarrow P_0 \rightarrow M \rightarrow 0$$
은 길이 $n$ 이하의 projective resolution이므로 $\pd_A M\leq n$이다. $n=0$인 경우 이는 $\Omega^0 M=M$이 projective라는 것으로, 곧 $\pd_A M\leq 0$이다.

(1)$\Rightarrow$(2)를 보이자. $\pd_A M\leq n$이면 길이 $n$ 이하의 projective resolution $P_\bullet$이 존재하여 $P_i=0$이 $i>n$에서 성립한다. [\[호몰로지 대수학\] §Ext와 Tor, ⁋명제 3](/ko/math/homological_algebra/ext_and_tor#prop3)에 의하여 $\Ext_A^i(M,N)=H^i(\Hom_A(P_\bullet,N))$이므로, $i>n$에서 이 cochain complex의 항이 $0$이 되어 $\Ext_A^i(M,N)=0$이다.

(2)$\Rightarrow$(3)은 자명하다.

(3)$\Rightarrow$(4)를 보이자. 임의의 projective resolution을 고정하고 그 $n$번째 syzygy $\Omega^n M$을 생각하자. Syzygy의 short exact sequence $0 \rightarrow \Omega^{i+1}M \rightarrow P_i \rightarrow \Omega^i M \rightarrow 0$에 $\Hom_A(-,N)$의 long exact sequence를 적용하면, $P_i$가 projective이므로 $j\geq 1$에서 $\Ext_A^j(P_i,N)=\Ext_A^{j+1}(P_i,N)=0$이고 따라서
$$\Ext_A^j(\Omega^{i+1}M,N)\cong \Ext_A^{j+1}(\Omega^i M,N)$$
이다. 이를 $j=1$에서 시작하여 반복하면
$$\Ext_A^1(\Omega^n M,N)\cong \Ext_A^2(\Omega^{n-1}M,N)\cong\cdots\cong \Ext_A^{n+1}(\Omega^0 M,N)=\Ext_A^{n+1}(M,N)$$
을 얻는다. 그럼 가정 (3)에 의하여 모든 $N$에 대하여 $\Ext_A^1(\Omega^n M,N)=0$이다.

이제 $\Ext_A^1(K,-)$이 항등적으로 $0$인 module $K$가 projective임을 보이면 $\Omega^n M$이 projective라는 결론을 얻는다. [\[다중선형대수학\] §기저, ⁋명제 2](/ko/math/multilinear_algebra/basis_of_free_modules#prop2)에 의하여 free module $P$로부터의 surjection $P \rightarrow K$가 존재하며, 그 kernel을 $L$이라 하면 short exact sequence $0 \rightarrow L \rightarrow P \rightarrow K \rightarrow 0$을 얻는다. 여기에 $\Hom_A(K,-)$의 long exact sequence를 적용하면
$$\Hom_A(K,P) \rightarrow \Hom_A(K,K) \rightarrow \Ext_A^1(K,L)=0$$
이 되어 $\Hom_A(K,P) \rightarrow \Hom_A(K,K)$이 surjective이다. 따라서 $\id_K$의 preimage $s:K \rightarrow P$가 존재하여 $P \rightarrow K$와의 합성이 $\id_K$가 되므로 이 short exact sequence는 split하고, $K$는 free module $P$의 direct summand이다. 그럼 [\[다중선형대수학\] §사영가군, 단사가군, 평탄가군, ⁋명제 4](/ko/math/multilinear_algebra/various_modules#prop4)에 의하여 $K$는 projective이다.
:::

Injective dimension에 대해서도 완전히 쌍대적인 특징화가 성립한다. Injective resolution $0 \rightarrow M \rightarrow I^0 \rightarrow I^1 \rightarrow \cdots$이 주어지면, $\Sigma^0 M=M$으로 두고 각각의 $n\geq 1$에 대하여 $n$번째 *cosyzygy* $\Sigma^n M=\coker(I^{n-2} \rightarrow I^{n-1})$을 정의한다. 여기서 $I^{-1}=M$으로 약속하면 $\Sigma^1 M=\coker(M \rightarrow I^0)$이고, 각각의 $n\geq 0$에 대하여 short exact sequence $0 \rightarrow \Sigma^n M \rightarrow I^n \rightarrow \Sigma^{n+1}M \rightarrow 0$을 얻는다.

::: 명제 3
$A$-module $M$과 정수 $n\geq 0$에 대하여 다음이 모두 동치이다.

1. $\operatorname{injdim}_A M\leq n$이다.
2. 모든 $A$-module $N$과 $i>n$에 대하여 $\Ext_A^i(N,M)=0$이다.
3. 모든 $A$-module $N$에 대하여 $\Ext_A^{n+1}(N,M)=0$이다.
4. $M$의 임의의 injective resolution에 대하여, 그 $n$번째 cosyzygy $\Sigma^n M$은 injective이다.
:::
::: 증명
[명제 2](#prop2)의 증명에서 projective resolution을 injective resolution으로, syzygy $\Omega$를 cosyzygy $\Sigma$로, 그리고 $\Hom_A(-,N)$의 long exact sequence를 $\Hom_A(N,-)$의 것으로 바꾸면 (1)$\Rightarrow$(2)$\Rightarrow$(3)$\Rightarrow$(4)$\Rightarrow$(1)의 논증이 그대로 성립한다. Cosyzygy의 short exact sequence로부터 얻는 dimension shifting은 이번에는 둘째 변수에서 일어나 $\Ext_A^1(N,\Sigma^n M)\cong \Ext_A^{n+1}(N,M)$을 준다.

유일하게 쌍대화가 자명하지 않은 단계는 (3)$\Rightarrow$(4)에서 쓰이는 다음 사실이다. $\Ext_A^1(-,K)$이 항등적으로 $0$이면 $K$는 injective이다. 이를 보이기 위해 [\[호몰로지 대수학\] §분해, ⁋명제 5](/ko/math/homological_algebra/resolutions#prop5)로부터 $K$를 injective module $E$에 포함시켜 short exact sequence $0 \rightarrow K \rightarrow E \rightarrow Q \rightarrow 0$을 얻자. $\Hom_A(-,K)$의 long exact sequence
$$\Hom_A(E,K) \rightarrow \Hom_A(K,K) \rightarrow \Ext_A^1(Q,K)=0$$
에서 $\id_K$가 $r:E \rightarrow K$로 lift되므로 이 short exact sequence는 split하고, $K$는 injective module $E$의 direct summand이다. 그럼 $\Hom_A(-,E)\cong\Hom_A(-,K)\oplus\Hom_A(-,Q')$ (단 $E\cong K\oplus Q'$)에서 좌변이 exact functor이므로 그 direct factor인 $\Hom_A(-,K)$ 또한 exact이고, 따라서 $K$는 injective이다.
:::

Injective module을 판정하는 데에는 다음의 고전적인 기준이 유용하다.

::: 보조정리 4 (Baer 판정법)
$A$-module $E$가 injective인 것은, $A$의 임의의 ideal $I$와 $A$-linear map $f:I \rightarrow E$가 항상 $A$로 확장되는 것과 동치이다.
:::
::: 증명
$E$가 injective라면 inclusion $I \hookrightarrow A$가 유도하는 $\Hom_A(A,E) \rightarrow \Hom_A(I,E)$이 surjective이므로 ([\[다중선형대수학\] §사영가군, 단사가군, 평탄가군, ⁋정의 3](/ko/math/multilinear_algebra/various_modules#def3)), 임의의 $f:I \rightarrow E$는 $A$로 확장된다.

거꾸로 확장 조건을 가정하고 $E$가 injective임을 보이자. Injective의 정의에 의하여, 임의의 injection $N \hookrightarrow M$과 $A$-linear map $g:N \rightarrow E$가 주어질 때 이를 $M$으로 확장하면 충분하다. $N\subseteq N'\subseteq M$이고 $g$를 확장하는 $A$-linear map $g':N' \rightarrow E$인 쌍 $(N',g')$들의 모임에 확장에 의한 순서를 주면, totally ordered subset의 upper bound는 그 합집합 위에서의 확장으로 주어지므로 이 모임은 inductive하다. [\[집합론\] §선택공리, ⁋정리 4](/ko/math/set_theory/axiom_of_choice#thm4)에 의하여 maximal element $(N',g')$가 존재한다.

$N'=M$임을 보이면 된다. 만일 $N'\neq M$이라면 $x\in M\setminus N'$을 택하고 $I=\{a\in A\mid ax\in N'\}$이라 하자. 이는 $A$의 ideal이며, $a\mapsto g'(ax)$로 정의되는 $A$-linear map $f:I \rightarrow E$는 가정에 의하여 $A$로 확장되므로 $e=\tilde{f}(1)\in E$가 존재하여 모든 $a\in I$에 대하여 $g'(ax)=ae$이다. 이제
$$g'':N'+Ax \rightarrow E;\qquad g''(n'+ax)=g'(n')+ae$$
를 정의하면 이는 well-defined이다. 실제로 $n'+ax=0$이라면 $ax=-n'\in N'$이므로 $a\in I$이고, $g'(n')=g'(-ax)=-g'(ax)=-ae$가 되어 $g'(n')+ae=0$이기 때문이다. 그럼 $g''$은 $g'$의 진성 확장이 되어 $(N',g')$의 maximality에 모순이므로 $N'=M$이다.
:::

Baer 판정법과 [명제 3](#prop3)의 dimension shifting을 종합하면, injective dimension을 판정할 때 둘째 변수를 quotient $A/I$로 제한할 수 있다.

::: 따름정리 5
$A$-module $E$와 정수 $n\geq 0$에 대하여, $\operatorname{injdim}_A E\leq n$인 것은 $A$의 모든 ideal $I$에 대하여 $\Ext_A^{n+1}(A/I,E)=0$인 것과 동치이다.
:::
::: 증명
$\operatorname{injdim}_A E\leq n$이면 [명제 3](#prop3)에 의하여 모든 $N$에 대하여 $\Ext_A^{n+1}(N,E)=0$이므로, 특히 $N=A/I$에서 성립한다.

거꾸로 모든 ideal $I$에 대하여 $\Ext_A^{n+1}(A/I,E)=0$이라 하자. $E$의 injective resolution을 하나 고정하고 그 $n$번째 cosyzygy $\Sigma^n E$를 생각하면, [명제 3](#prop3)의 증명에서 본 dimension shifting에 의하여 모든 ideal $I$에 대하여
$$\Ext_A^1(A/I,\Sigma^n E)\cong \Ext_A^{n+1}(A/I,E)=0$$
이다. 이제 $\Sigma^n E$가 injective임을 [보조정리 4](#lem4)로 확인한다. Ideal $I$와 $A$-linear map $f:I \rightarrow \Sigma^n E$가 주어졌다 하면, short exact sequence $0 \rightarrow I \rightarrow A \rightarrow A/I \rightarrow 0$에 $\Hom_A(-,\Sigma^n E)$의 long exact sequence를 적용하여
$$\Hom_A(A,\Sigma^n E) \rightarrow \Hom_A(I,\Sigma^n E) \rightarrow \Ext_A^1(A/I,\Sigma^n E)=0$$
을 얻으므로 $f$는 $A$로 확장된다. 따라서 [보조정리 4](#lem4)에 의하여 $\Sigma^n E$는 injective이고, [명제 3](#prop3)에 의하여 $\operatorname{injdim}_A E\leq n$이다.
:::

이제 ring 전체에 걸친 불변량을 정의한다.

::: 정의 6
Ring $A$의 *global dimension<sub>대역차원</sub>* $\operatorname{gldim}A$를 모든 $A$-module $M$에 대한 $\pd_A M$의 supremum으로 정의한다.
:::

정의에 의하여 $\operatorname{gldim}A\leq n$인 것은 모든 $A$-module의 projective dimension이 $n$ 이하인 것과 동치이며, $\operatorname{gldim}A=0$인 것은 $A$의 모든 module이 projective인 것과 동치이다. 이 값은 겉보기에 모든 module을 훑어야 계산되는 것처럼 보이지만, 사실 훨씬 작은 자료로 결정된다.

::: 명제 7 (Auslander)
Ring $A$에 대하여
$$\operatorname{gldim}A=\sup_M\operatorname{injdim}_A M=\sup_I \pd_A(A/I)$$
가 성립한다. 여기서 첫째 supremum은 모든 $A$-module $M$에 대한 것이고, 둘째 supremum은 $A$의 모든 ideal $I$에 대한 것이다.
:::
::: 증명
임의의 정수 $n\geq 0$에 대하여 다음 세 조건이 동치임을 보이면 세 supremum이 일치한다.

1. $\operatorname{gldim}A\leq n$이다.
2. 모든 $A$-module $N$에 대하여 $\operatorname{injdim}_A N\leq n$이다.
3. 모든 ideal $I$에 대하여 $\pd_A(A/I)\leq n$이다.

(1)$\Rightarrow$(3)은 $A/I$가 하나의 $A$-module이므로 자명하다.

(3)$\Rightarrow$(2)를 보이자. 각각의 ideal $I$에 대하여 $\pd_A(A/I)\leq n$이므로 [명제 2](#prop2)에 의하여 모든 $A$-module $N$에 대하여 $\Ext_A^{n+1}(A/I,N)=0$이다. 그럼 [따름정리 5](#cor5)에 의하여 임의의 $N$에 대하여 $\operatorname{injdim}_A N\leq n$이다.

(2)$\Rightarrow$(1)을 보이자. 모든 $N$에 대하여 $\operatorname{injdim}_A N\leq n$이면 [명제 3](#prop3)에 의하여 모든 $A$-module $M,N$에 대하여 $\Ext_A^{n+1}(M,N)=0$이고, 따라서 [명제 2](#prop2)에 의하여 모든 $M$에 대하여 $\pd_A M\leq n$, 곧 $\operatorname{gldim}A\leq n$이다.
:::

## Local ring 위의 최소 자유 분해

이제 $(A,\mathfrak{m},\kappa)$를 residue field $\kappa=A/\mathfrak{m}$을 갖는 Noetherian local ring이라 하고, $M$을 finitely generated $A$-module이라 하자. 이 상황에서는 free resolution을 가장 경제적으로 고를 수 있으며, 그 크기가 곧 projective dimension을 읽어낸다.

::: 정의 8
위와 같은 상황에서 free resolution
$$\cdots \rightarrow F_1 \overset{d_1}{\longrightarrow} F_0 \overset{\epsilon}{\longrightarrow} M \rightarrow 0$$
(각 $F_i$는 finitely generated free $A$-module)이 *minimal*이라는 것은 모든 $i\geq 1$에 대하여 $d_i(F_i)\subseteq \mathfrak{m}F_{i-1}$이 성립하는 것이다.
:::

이 조건의 $i=1$인 경우는 $\ker\epsilon=d_1(F_1)\subseteq \mathfrak{m}F_0$을 뜻하므로, $\epsilon\otimes_A\kappa: F_0\otimes_A\kappa \rightarrow M\otimes_A\kappa$은 kernel이 $0$인 surjection, 곧 isomorphism이 된다. 즉 $F_0$의 basis는 $M$의 minimal generating set에 대응한다. 최소성이 뜻하는 바는 분해의 각 단계에서 새로 도입하는 generator에 군더더기가 없다는 것이며, 이러한 분해는 언제나 존재한다.

::: 명제 9
Noetherian local ring $(A,\mathfrak{m},\kappa)$ 위의 finitely generated $A$-module $M$은 minimal free resolution을 갖는다.
:::
::: 증명
$M$의 minimal generating set, 즉 $\kappa$-벡터공간 $M/\mathfrak{m}M$의 basis로 image가 내려가는 원소들 $x_1,\ldots, x_r\in M$을 택하자. [§정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)에 의하여 이들은 $M$을 생성하므로, $F_0=A^{\oplus r}$과 $e_i\mapsto x_i$로 정의된 surjection $\epsilon:F_0 \rightarrow M$을 얻는다.

이제 $\ker\epsilon\subseteq \mathfrak{m}F_0$임을 확인하자. $\sum a_i e_i\in\ker\epsilon$이라면 $\sum a_i x_i=0$이고, 이를 $M/\mathfrak{m}M$에서 읽으면 $\sum \bar{a}_i \bar{x}_i=0$인데, $\bar{x}_i$들이 $\kappa$ 위에서 linearly independent이므로 모든 $\bar{a}_i=0$, 곧 $a_i\in\mathfrak{m}$이다. $A$가 Noetherian이고 $F_0$가 finitely generated free이므로 $F_0$은 Noetherian module이고 ([§기본 개념들, ⁋따름정리 6](/ko/math/commutative_algebra/basic_notions#cor6)), 따라서 그 submodule $\ker\epsilon$은 finitely generated이다. ([§기본 개념들, ⁋정리 3](/ko/math/commutative_algebra/basic_notions#thm3))

같은 논증을 $M$ 대신 $\ker\epsilon$에 적용하면 finitely generated free module $F_1$과 surjection $F_1 \rightarrow \ker\epsilon$을 얻는데, $\ker\epsilon\subseteq \mathfrak{m}F_0$이므로 이를 $F_0$으로의 map $d_1$으로 보면 $d_1(F_1)=\ker\epsilon\subseteq \mathfrak{m}F_0$이다. 이 과정을 반복하면 각 단계에서 $d_i(F_i)\subseteq \mathfrak{m}F_{i-1}$을 만족하는 minimal free resolution을 얻는다.
:::

Minimal free resolution의 결정적인 성질은 그 계수 $F_i$의 rank가 Tor로 직접 읽힌다는 것이다.

::: 명제 10
Noetherian local ring $(A,\mathfrak{m},\kappa)$ 위의 finitely generated $A$-module $M$과 그 minimal free resolution $F_\bullet$에 대하여, 각각의 $i$에서
$$\Tor_i^A(M,\kappa)\cong F_i\otimes_A\kappa$$
이 성립한다. 특히 $\operatorname{rank}F_i=\dim_\kappa\Tor_i^A(M,\kappa)$이며, 이 값은 minimal free resolution의 선택에 의존하지 않는다.
:::
::: 증명
$F_\bullet$은 free이므로 projective resolution이고, 따라서 [\[호몰로지 대수학\] §Ext와 Tor, ⁋정의 2](/ko/math/homological_algebra/ext_and_tor#def2)에 의하여 $\Tor_i^A(M,\kappa)=H_i(F_\bullet\otimes_A\kappa)$이다. 이 complex의 differential은 $d_i\otimes\id_\kappa: F_i\otimes_A\kappa \rightarrow F_{i-1}\otimes_A\kappa$인데, $F_{i-1}\otimes_A\kappa=F_{i-1}/\mathfrak{m}F_{i-1}$이고 최소성에 의하여 $d_i(F_i)\subseteq \mathfrak{m}F_{i-1}$이므로 이 map은 $0$이다. 따라서 $F_\bullet\otimes_A\kappa$의 모든 differential이 $0$이 되어
$$\Tor_i^A(M,\kappa)=F_i\otimes_A\kappa$$
이다. $F_i$가 rank $r_i$의 free module이므로 $F_i\otimes_A\kappa\cong \kappa^{r_i}$이고, 이로부터 $r_i=\dim_\kappa\Tor_i^A(M,\kappa)$을 얻는다. 우변은 $F_\bullet$과 무관한 양이므로 rank $r_i$ 또한 그러하다.
:::

이 불변량 $\beta_i(M)=\dim_\kappa\Tor_i^A(M,\kappa)$을 $M$의 *$i$번째 Betti number*라 부른다. [명제 10](#prop10)은 minimal free resolution이 rank의 수준에서 유일함을 말해주며, 동시에 projective dimension을 Betti number의 소멸로 번역할 수 있게 한다.

::: 명제 11
Noetherian local ring $(A,\mathfrak{m},\kappa)$ 위의 finitely generated $A$-module $M$에 대하여
$$\pd_A M=\sup\{i\mid \Tor_i^A(M,\kappa)\neq 0\}$$
이 성립한다.
:::
::: 증명
$M$의 minimal free resolution $F_\bullet$을 고정하고 $\ell=\sup\{i\mid F_i\neq 0\}$이라 하자. $F_i$는 local ring 위의 finitely generated free module이므로 [§정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)에 의하여 $F_i\otimes_A\kappa=0$인 것은 $F_i=0$인 것과 동치이고, [명제 10](#prop10)과 종합하면 $\Tor_i^A(M,\kappa)\neq 0$인 것이 $F_i\neq 0$인 것과 동치이다. 따라서 $\sup\{i\mid \Tor_i^A(M,\kappa)\neq 0\}=\ell$이다.

$\ell<\infty$인 경우 $0 \rightarrow F_\ell \rightarrow \cdots \rightarrow F_0 \rightarrow M \rightarrow 0$은 길이 $\ell$의 free resolution이므로 $\pd_A M\leq \ell$이다. 거꾸로 $\Tor_i^A(M,\kappa)\neq 0$이면 $\pd_A M\geq i$인데, 만일 $\pd_A M<i$라면 길이 $\pd_A M$의 projective resolution으로 $\Tor_i^A(M,\kappa)$을 계산하여 $0$을 얻어 모순이기 때문이다. 그러므로 $\pd_A M\geq \ell$이며, 두 부등식을 합하면 $\pd_A M=\ell$이다. $\ell=\infty$인 경우에도 임의의 $i$에 대하여 $\Tor_i^A(M,\kappa)\neq 0$인 $i$가 얼마든지 크게 존재하므로 $\pd_A M=\infty=\ell$이다.
:::

여기서 residue field $\kappa$의 역할이 두드러진다. [명제 11](#prop11)은 임의의 finitely generated module의 projective dimension을 오직 $\kappa$와의 Tor만으로 통제하므로, global dimension이 $\kappa$ 하나로 결정된다는 것을 예고한다.

::: 따름정리 12
Noetherian local ring $(A,\mathfrak{m},\kappa)$에 대하여 $\operatorname{gldim}A=\pd_A\kappa$가 성립한다.
:::
::: 증명
$\pd_A\kappa\leq \operatorname{gldim}A$는 자명하므로 반대 부등식을 보이면 된다. $\pd_A\kappa=n<\infty$라 하고 $\kappa$의 길이 $n$짜리 projective resolution $Q_\bullet$을 택하자. 임의의 $A$-module $M$에 대하여 [\[호몰로지 대수학\] §Ext와 Tor, ⁋명제 4](/ko/math/homological_algebra/ext_and_tor#prop4)에 의하여 $\Tor_i^A(M,\kappa)=H_i(M\otimes_A Q_\bullet)$을 $Q_\bullet$으로도 계산할 수 있으므로, $i>n$에서 $\Tor_i^A(M,\kappa)=0$이다. 그럼 finitely generated $M$에 대하여 [명제 11](#prop11)로부터 $\pd_A M\leq n$이다.

한편 [명제 7](#prop7)에 의하여 $\operatorname{gldim}A=\sup_I \pd_A(A/I)$이고, 각 $A/I$는 cyclic이므로 finitely generated이다. 따라서 방금 얻은 부등식으로부터 $\pd_A(A/I)\leq n$이 모든 ideal $I$에 대하여 성립하고, $\operatorname{gldim}A\leq n=\pd_A\kappa$이다. $\pd_A\kappa=\infty$인 경우에는 $\operatorname{gldim}A\geq \pd_A\kappa=\infty$이므로 등식이 성립한다.
:::

이 따름정리를 regular local ring에 적용하면, 앞선 글에서 계산한 Tor가 곧바로 global dimension을 준다.

::: 명제 13
$d$차원의 regular local ring $(A,\mathfrak{m},\kappa)$에 대하여 $\operatorname{gldim}A=d$이다.
:::
::: 증명
[§코쥴 복합체, ⁋예시 12](/ko/math/commutative_algebra/koszul_complex#ex12)에서 우리는
$$\Tor_i^A(\kappa,\kappa)\cong {\bigwedge}^i_\kappa(\mathfrak{m}/\mathfrak{m}^2)$$
임을 보았다. $A$가 regular local ring이므로 ([§차원, ⁋정의 12](/ko/math/commutative_algebra/Krull_dimension#def12)) 같은 예시에서 $\dim_\kappa(\mathfrak{m}/\mathfrak{m}^2)=d$임을 확인하였고, 따라서 $\Tor_d^A(\kappa,\kappa)\cong\kappa\neq 0$이고 $i>d$에서 $\Tor_i^A(\kappa,\kappa)=0$이다. 따라서 [명제 11](#prop11)에 의하여 $\pd_A\kappa=d$이고, [따름정리 12](#cor12)에 의하여 $\operatorname{gldim}A=\pd_A\kappa=d$이다.
:::

## Hilbert syzygy 정리

Polynomial ring $\mathbb{K}[\x_1,\ldots, \x_n]$은 local ring이 아니므로 위의 최소 자유 분해 기계를 직접 적용할 수 없다. 대신 우리는 ring에 변수를 하나 더할 때 global dimension이 어떻게 변하는지를 추적한다. 이때 중심이 되는 것은 $A[\x]$-module을 $A$ 위의 자료로 되돌리는 다음의 exact sequence이다.

::: 보조정리 14
Ring $A$와 $A[\x]$-module $M$이 주어졌다 하자. $M$을 $A$-module로 보고 $M[\x]=A[\x]\otimes_A M$이라 하면, 다음의 $A[\x]$-module들의 short exact sequence
$$0 \rightarrow M[\x] \overset{\psi}{\longrightarrow} M[\x] \overset{\rho}{\longrightarrow} M \rightarrow 0$$
이 존재한다. 여기서 $\psi(f\otimes m)=\x f\otimes m-f\otimes \x m$이고 $\rho(f\otimes m)=fm$이며, $\x m$은 $M$ 위의 $A[\x]$-작용을 뜻한다.
:::
::: 증명
[\[다중선형대수학\] §행렬식, ⁋명제 7](/ko/math/multilinear_algebra/determinants#prop7)은 finitely generated free module과 그 위의 endomorphism에 대하여 같은 구성이 right exact sequence를 줌을 보였다. 여기서는 일반적인 $A[\x]$-module $M$에 대하여 완전성 전체를 자족적으로 증명한다.

$A[\x]$-module $M[\x]=A[\x]\otimes_A M$의 구조는 왼쪽 factor $A[\x]$에서 온다. 우선 $\rho$가 $A[\x]$-linear이고 surjective임을 보자. $\rho(1\otimes m)=m$이므로 surjective이고, 임의의 $g\in A[\x]$에 대하여 $\rho(g(f\otimes m))=\rho(gf\otimes m)=(gf)m=g(fm)=g\rho(f\otimes m)$이다. 다음으로 $\psi$가 $A[\x]$-linear임을 보면, $\x$가 $A[\x]$의 중심에 있으므로
$$\psi(gf\otimes m)=\x gf\otimes m-gf\otimes \x m=g(\x f\otimes m-f\otimes \x m)=g\psi(f\otimes m)$$
이다. 또 $\rho\psi=0$인데, $M$이 $A[\x]$-module이므로 $f\otimes \x m$의 image $f(\x m)=(\x f)m$과 $\x f\otimes m$의 image $(\x f)m$이 같아
$$\rho\psi(f\otimes m)=(\x f)m-f(\x m)=(\x f)m-(\x f)m=0$$
이기 때문이다.

이제 $A[\x]$가 basis $\{\x^k\}_{k\geq 0}$을 갖는 free $A$-module이므로 $M[\x]=\bigoplus_{k\geq 0}\x^k\otimes M$으로 분해됨을 사용한다. $\ker\rho\subseteq \im\psi$를 보이기 위해, $\psi(\x^k\otimes m)=\x^{k+1}\otimes m-\x^k\otimes \x m$으로부터 $\im\psi$를 법으로 하여
$$\x^{k+1}\otimes m\equiv \x^k\otimes \x m\pmod{\im\psi}$$
임에 주목하면, 이를 반복하여 임의의 $k$에 대하여 $\x^k\otimes m\equiv 1\otimes \x^k m\pmod{\im\psi}$을 얻는다. 따라서 $z=\sum_k \x^k\otimes m_k$에 대하여
$$z\equiv \sum_k 1\otimes \x^k m_k=1\otimes\Big(\sum_k \x^k m_k\Big)=1\otimes \rho(z)\pmod{\im\psi}$$
이고, $z\in\ker\rho$이면 $\rho(z)=0$이 되어 $z\in\im\psi$이다.

마지막으로 $\psi$가 injective임을 보인다. $z=\sum_{k=0}^N \x^k\otimes m_k\neq 0$이고 $m_N\neq 0$이라 하자. 그럼
$$\psi(z)=\sum_{k=0}^N \x^{k+1}\otimes m_k-\sum_{k=0}^N \x^k\otimes \x m_k$$
인데, 위의 direct sum 분해에서 degree $N+1$ 성분은 첫째 합의 $\x^{N+1}\otimes m_N$ 뿐이며 이는 $m_N\neq 0$이므로 $0$이 아니다. 따라서 $\psi(z)\neq 0$이다.
:::

변수를 더하는 조작이 projective dimension을 얼마나 늘리는지는 다음의 표준적인 부등식들로 통제된다.

::: 보조정리 15
다음이 성립한다.

1. Ring homomorphism $A \rightarrow B$가 $B$를 flat $A$-module로 만든다면, 임의의 $A$-module $N$에 대하여 $\pd_B(B\otimes_A N)\leq \pd_A N$이다.
2. $A$-module들의 short exact sequence $0 \rightarrow N' \rightarrow N \rightarrow N'' \rightarrow 0$에 대하여 $\pd_A N''\leq \max(\pd_A N,\pd_A N'+1)$이다.
:::
::: 증명
첫째 결과를 보자. $\pd_A N=\infty$이면 보일 것이 없으므로 $\pd_A N=n<\infty$이라 하고, $N$의 길이 $n$짜리 projective resolution $0 \rightarrow P_n \rightarrow \cdots \rightarrow P_0 \rightarrow N \rightarrow 0$을 택하자. $B$가 flat $A$-module이므로 ([\[다중선형대수학\] §사영가군, 단사가군, 평탄가군, ⁋정의 7](/ko/math/multilinear_algebra/various_modules#def7)) 여기에 $B\otimes_A-$를 취해도 exactness가 보존되어
$$0 \rightarrow B\otimes_A P_n \rightarrow \cdots \rightarrow B\otimes_A P_0 \rightarrow B\otimes_A N \rightarrow 0$$
이 exact이다. 각 $P_i$는 free module $A^{(J)}$의 direct summand이므로 ([\[다중선형대수학\] §사영가군, 단사가군, 평탄가군, ⁋명제 4](/ko/math/multilinear_algebra/various_modules#prop4)), $B\otimes_A P_i$는 $B\otimes_A A^{(J)}\cong B^{(J)}$의 direct summand가 되어 projective $B$-module이다. 따라서 위의 열은 $B\otimes_A N$의 길이 $n$ 이하의 projective resolution이 되어 $\pd_B(B\otimes_A N)\leq n$이다.

둘째 결과를 보자. $n=\max(\pd_A N,\pd_A N'+1)$이라 하고 임의의 $A$-module $L$을 고정하자. 주어진 short exact sequence에 $\Hom_A(-,L)$의 long exact sequence를 적용하면
$$\Ext_A^{i-1}(N',L) \rightarrow \Ext_A^i(N'',L) \rightarrow \Ext_A^i(N,L)$$
을 얻는다. $i>n$이면 $i>\pd_A N$이므로 [명제 2](#prop2)에 의하여 $\Ext_A^i(N,L)=0$이고, $i-1>\pd_A N'$이므로 마찬가지로 $\Ext_A^{i-1}(N',L)=0$이다. 그럼 가운데 항 $\Ext_A^i(N'',L)$은 양옆이 $0$인 자리에 놓여 $0$이며, $L$이 임의였으므로 다시 [명제 2](#prop2)에 의하여 $\pd_A N''\leq n$이다.
:::

::: 정리 16
임의의 ring $A$에 대하여 $\operatorname{gldim}A[\x]\leq \operatorname{gldim}A+1$이 성립한다.
:::
::: 증명
$\operatorname{gldim}A=\infty$이면 보일 것이 없으므로 $g=\operatorname{gldim}A<\infty$이라 하자. 임의의 $A[\x]$-module $M$에 대하여 [보조정리 14](#lem14)의 short exact sequence
$$0 \rightarrow M[\x] \rightarrow M[\x] \rightarrow M \rightarrow 0$$
에 [보조정리 15](#lem15)의 둘째 결과를 적용하면
$$\pd_{A[\x]}M\leq \max\big(\pd_{A[\x]}M[\x],\ \pd_{A[\x]}M[\x]+1\big)=\pd_{A[\x]}M[\x]+1$$
이다. 한편 $A[\x]$는 free, 따라서 flat $A$-module이고 $M[\x]=A[\x]\otimes_A M$이므로, [보조정리 15](#lem15)의 첫째 결과에 의하여
$$\pd_{A[\x]}M[\x]\leq \pd_A M\leq \operatorname{gldim}A=g$$
이다. 여기서 $\pd_A M$은 $M$을 $A$-module로 본 것이다. 두 부등식을 합하면 $\pd_{A[\x]}M\leq g+1$이며, $M$이 임의였으므로 $\operatorname{gldim}A[\x]\leq g+1$이다.
:::

::: 정리 17 (Hilbert syzygy theorem)
Field $\mathbb{K}$에 대하여 $\operatorname{gldim}\mathbb{K}[\x_1,\ldots, \x_n]=n$이다.
:::
::: 증명
우선 부등식 $\operatorname{gldim}\mathbb{K}[\x_1,\ldots, \x_n]\leq n$을 $n$에 대한 귀납법으로 보인다. $\mathbb{K}$ 위의 module은 벡터공간이므로 모두 free, 따라서 projective이고, 이로부터 $\operatorname{gldim}\mathbb{K}=0$이다. 이제 $\mathbb{K}[\x_1,\ldots, \x_n]=\mathbb{K}[\x_1,\ldots, \x_{n-1}][\x_n]$으로 보면 [정리 16](#thm16)과 귀납적 가정에 의하여
$$\operatorname{gldim}\mathbb{K}[\x_1,\ldots, \x_n]\leq \operatorname{gldim}\mathbb{K}[\x_1,\ldots, \x_{n-1}]+1\leq (n-1)+1=n$$
이다.

반대 부등식을 위해 $A=\mathbb{K}[\x_1,\ldots, \x_n]$으로 두고 $\kappa=A/(\x_1,\ldots, \x_n)\cong \mathbb{K}$을 $A$-module로 보자. [\[호몰로지 대수학\] §Ext와 Tor, §§예시](/ko/math/homological_algebra/ext_and_tor#예시)에서 우리는 Koszul complex를 통해
$$\Tor_i^A(\mathbb{K},\mathbb{K})\cong {\bigwedge}^i_\mathbb{K}(\mathbb{K}^n)$$
임을 계산하였으며, 특히 $\Tor_n^A(\mathbb{K},\mathbb{K})\cong {\bigwedge}^n_\mathbb{K}(\mathbb{K}^n)\cong \mathbb{K}\neq 0$이다. 그럼 $\pd_A\mathbb{K}\geq n$인데, 만일 $\pd_A\mathbb{K}<n$이라면 길이 $n$ 미만의 projective resolution으로 $\Tor_n^A(\mathbb{K},\mathbb{K})$을 계산하여 $0$을 얻어 모순이기 때문이다. 따라서 $\operatorname{gldim}A\geq \pd_A\mathbb{K}\geq n$이고, 앞의 부등식과 종합하여 $\operatorname{gldim}A=n$을 얻는다.
:::

Local ring에서 finitely generated module의 projective dimension을 depth와 잇는 Auslander--Buchsbaum 공식이 이 이야기의 다음 장을 이룬다.

---

**참고문헌**

**[Eis]** David Eisenbud. *Commutative Algebra: with a view toward algebraic geometry*. Springer, 1995.  
**[Mat]** Hideyuki Matsumura. *Commutative Ring Theory*. Cambridge University Press, 1986.  
**[Wei]** Charles A. Weibel. *An Introduction to Homological Algebra*. Cambridge University Press, 1994.

---
