---
title: "반단순가군"
description: "Simple module들의 직합으로 분해되는 semisimple module을 정의하고, 세 가지 동치 특징(합·직합·모든 submodule이 direct summand)을 Zorn 보조정리로 증명한다. Isotypic 성분에 의한 canonical 분해와, 유한 직합 분해의 유일성을 Schur 보조정리로부터 유도한다."
excerpt: "Semisimple module의 동치 특징, isotypic decomposition, 그리고 분해의 유일성"

categories: [Math / Ring Theory]
permalink: /ko/math/ring_theory/semisimple_modules
sidebar: 
    nav: "ring_theory-ko"

date: 2026-09-13

weight: 7
---

이 글에서 ring $A$는 항등원을 갖는, commutative라 가정하지 않는 ring이며, module은 언제나 left module이다.

## Semisimple module의 정의

우리는 [§나눗셈환, §§단순 가군의 자기사상환](/ko/math/ring_theory/division_rings#단순-가군의-자기사상환){: data-lid="don6w" data-relation="weak" }에서 간단하게 simple module을 정의하였으며, 이 글의 주제는 이와 연관된 주제들을 자세히 살펴보는 것이다. 따라서 우선 다음의 정의를 (정식으로) 내리자.

::: 정의 1
$0$이 아닌 $A$-module $M$이 $0$과 $M$ 이외의 submodule을 갖지 않을 때, $M$을 *simple module<sub>단순가군</sub>*이라 부른다.
:::

그러나 일반적으로 simple module에 대해서는 할 이야기가 별로 없으므로, 우리는 더 일반적으로 다음을 정의한다.

::: 정의 2
$A$-module $M$이 적당한 simple submodule들의 family $(S_i)_{i\in I}$에 대하여

$$M=\bigoplus_{i\in I}S_i$$

로 표현될 수 있을 때, $M$을 *semisimple module<sub>반단순 가군</sub>*이라 부른다.
:::

Index set $I$가 공집합인 경우, 관례적으로 이는 $0$으로 정의되며, 따라서 정의상 $0$은 semisimple module이다. 

::: 예시 3
Division ring $D$를 자기 자신 위의 left module로 보면 [\[대수적 구조\] §분수체, ⁋명제 4](/ko/math/algebraic_structures/field_of_fractions#prop4){: data-lid="ge4aq" data-relation="required" }에 의해 $D$는 simple $D$-module이다. 일반적으로 $D$ 위의 벡터공간 $V$는 basis $B$를 가지므로, 이를 사용하여 $V=\bigoplus_{b\in B}Db$로 나타내면 division ring 위의 벡터공간은 semisimple $D$-module이라는 것을 안다.
:::

직관적으로 simple module은 module을 분해할 수 있는 가장 작은 단위이며, 이 직관은 다음 보조정리에 녹아있다. 

::: 보조정리 4
$M=\sum_{i\in I}S_i$가 simple submodule들의 합이라 하고, $N$을 $M$의 submodule이라 하자. 그럼 적당한 $J\subseteq I$가 존재하여

$$M=N\oplus\bigoplus_{j\in J}S_j$$

이다.
:::
::: 증명
우선 $N+\sum_{j\in J}S_j$가 direct sum이 되도록 하는 subset $J\subseteq I$들의 모임을 $\mathcal{J}$라 하자. 그럼 자명하게 $\emptyset\in \mathcal{J}$이며, direct sum 조건에 관여하는 것은 유한개의 원소들 뿐이므로, $\mathcal{J}$의 임의의 chain이 주어졌을 때 그 합집합 또한 $\mathcal{J}$에 속한다. 따라서 [\[집합론\] §선택공리, ⁋정리 4](/ko/math/set_theory/axiom_of_choice#thm4){: data-lid="5jb59" data-relation="required" }에 의해 $\mathcal{J}$는 maximal element $J$를 갖는다. $M'=N\oplus\bigoplus_{j\in J}S_j$로 두자.

우리 주장은 임의의 $i\in I$에 대하여 $S_i\subseteq M'$이고, 따라서

$$M=N+\sum_{i\in I}S_i\subseteq M'$$

이 되어 $M=M'$이라는 것이다. 결론에 반하여 $S_i\not\subseteq M'$인 $S_i$가 존재한다 하자. 그럼 $S_i$의 simplicity에 의하여 $S_i\cap M'=0$이므로, 합 $N+\sum_{j\in J}S_j+S_i$가 다시 direct sum이 된다. ([\[다중선형대수학\] §완전열, ⁋명제 6](/ko/math/multilinear_algebra/exact_sequences#prop6){: data-lid="5ih46" data-relation="required" }) 따라서 $J\cup\{i\}\in\mathcal{J}$이고, 이는 $J$의 maximality에 모순이므로 이러한 $i$는 존재할 수 없다. 
:::

이 보조정리로부터 semisimple module을 다음과 같이 특정지을 수 있게 된다.

::: 정리 5
$A$-module $M$에 대하여 다음이 모두 동치이다.

1. $M$은 simple submodule들의 합이다.
2. $M$은 semisimple이다. 즉 simple submodule들의 direct sum이다.
3. $M$의 모든 submodule은 direct summand이다.
:::
::: 증명
첫째 주장이 둘째 주장과 셋째 주장을 함의하는 것은 [보조정리 4](#lem4){: data-lid="lf4v4" data-relation="required" }의 결과이며, 둘째 주장이 첫째 주장을 함의하는 것은 자명하다. 따라서 셋째 주장이 첫째 주장을 함의하는 것만 보이면 충분하다. 

우선 우리는 셋째 성질이 $M$의 임의의 submodule로 내려간다는 것을 확인한다. 이를 위해 $M$의 submodule $N$을 고정하고, $N$의 임의의 submodule $L$이 주어졌다 하자. 그럼 $M$에 대한 가정으로부터 $M=L\oplus C$인 $M$의 submodule $C$가 존재한다. 그럼 이제 임의의 $n\in N$에 대하여, 이 direct sum decomposition은 $n=l+c$인 $l\in L$과 $c\in C$를 유일하게 결정한다. 이제 $c=n-l\in N\cap C$이므로 $N=L+(N\cap C)$이고, 뿐만 아니라

$$L\cap(N\cap C)\subseteq L\cap C=0$$

이므로 이 합은 direct sum이다. 

다음 주장은 $M$의 임의의 nonzero submodule $N$이 simple submodule을 항상 포함한다는 것이다. 이를 위해 $N$의 임의의 nonzero element $x\in N$을 택하고, 이것이 생성하는 cyclic submodule $Ax\subseteq N$을 생각하자. 그럼 $Ax$의 submodule 중, $x$를 포함하지 <em-ko>않는</em-ko> 것들의 모임은 [\[집합론\] §선택공리, ⁋정리 4](/ko/math/set_theory/axiom_of_choice#thm4){: data-lid="eax1z" data-relation="required" }의 전제조건을 만족하고, 따라서 이들 중 maximal한 $K$가 존재한다. 한편, $K$를 strict하게 포함하는 $Ax$의 submodule은 $K$의 maximality에 의해 반드시 $x$를 포함하므로 $Ax$와 같게 되고, 따라서 $K$는 $Ax$의 maximal proper submodule이다. 이제 $M$의 submodule $Ax$에 셋째 조건을 적용하면 $Ax=K\oplus S$인 submodule $S$가 존재하며, 그럼 $S\cong Ax/K$이므로 다시 $K$의 maximality에 의하여 이는 simple이다. 

이제 마지막으로 $M$의 모든 simple submodule들의 합을 $N_0$라 하면, 다시 셋째 조건에 의해 $M=N_0\oplus C$를 만족하는 $C$가 존재한다. 만일 $C\neq 0$이라면 이는 simple submodule을 포함하므로 $N_0$의 정의에 모순이고, 따라서 $C=0$이며 $M=N_0$은 simple submodule들의 합이다. 
:::

그럼 특히 셋째 조건에 의하여 semisimple module을 가운데 항으로 갖는 $A$-module들의 short exact sequence는 항상 split-exact이다. 다음 따름정리는 이에 대한 역으로, semisimple module의 모든 submodule과 quotient가 semisimple이라는 것이다. 

::: 따름정리 6
Semisimple module $M$의 모든 submodule과 quotient는 semisimple이다.
:::
::: 증명
Quotient $M/N$의 경우, canonical projection $\pr: M\rightarrow M/N$에 대하여, $M$을 simple module들의 합 $M=\sum S_i$로 쓰면 $M/N=\sum \pr(S_i)$이고 $\pr(S_i)\cong S_i/(S_i\cap N)$이므로 $S_i$가 simple이라는 가정으로부터 따라나온다. 

Submodule의 경우, $M$의 임의의 submodule $N$에 대하여 [보조정리 4](#lem4){: data-lid="qxdbu" data-relation="required" }에 의해 $M=N\oplus\bigoplus_{j\in J}S_j$인 $J$가 존재하므로 $N\cong M/\bigoplus_{j\in J}S_j$이고, quotient에 대한 주장으로부터 증명이 완료된다.
:::

## Isotypic decomposition

Semisimple module은 그 정의에 의해 direct sum decomposition $M=\bigoplus S_i$를 가지지만, 일반적으로 이는 유일하지 않다. 그러나 서로 isomorphic한 summand들을 같은 것으로 취급하면 이 표현은 유일하며, 이를 증명하기 위해서는 우선 simple submodule들의 합 안에 어떠한 simple submodule들이 살 수 있는지를 확인한다.

::: 보조정리 7
Semisimple module $M$과 그 direct sum decomposition $M=\bigoplus S_i$를 고정하자. $M$의 임의의 simple submodule $U$에 대하여, $U\cong S_i$이도록 하는 $i\in I$가 존재한다. 
:::
::: 증명
주어진 direct sum decomposition이 주는 canonical projection $\pr_i: M\rightarrow S_i$에 대하여, $U\neq 0$이므로 $\pr_i(U)\neq 0$인 $i$가 존재한다. 이제 $\pr_i\vert_U: U\rightarrow S_i$는 simple module 사이의 nonzero homomorphism이므로, [§나눗셈환, ⁋보조정리 10](/ko/math/ring_theory/division_rings#lem10){: data-lid="ckge3" data-relation="required" }에 의해 isomorphism이다. 
:::

이를 다음과 같이 이름붙인다.

::: 정의 8
Simple $A$-module $S$에 대하여, $A$-module $M$의 *$S$-isotypic component<sub>등형 성분</sub>* $M_S$는 $S$와 isomorphic한 $M$의 simple submodule 전부의 합으로 정의한다.
:::

그럼 다음이 성립한다.

::: 명제 9
Semisimple module $M$, $N$에 대하여 다음이 성립한다.

1. Simple module의 isomorphism class에 대해 $M=\bigoplus M_S$이다.
2. 임의의 $A$-module homomorphism $f:M\rightarrow N$은 $f(M_S)\subseteq N_S$를 만족한다.
:::
::: 증명
둘째 결과를 먼저 보인다. $T$가 $S$와 isomorphic한 $M$의 simple submodule이라 하자. $f(T)\cong T/(T\cap\ker f)$는 $T$가 simple이므로 $0$이거나 $S$와 isomorphic하고, 어느 경우에도 $f(T)\subseteq N_S$이다. $M_S$는 이러한 $T$들의 합이므로 $f(M_S)\subseteq N_S$이다.

이제 첫째 결과를 보인다. Semisimple module $M$의 direct sum 분해 $M=\bigoplus_{i\in I}S_i$를 고르고 canonical projection $\pr_i:M\rightarrow S_i$를 생각하자. 위의 결과에 의해 $\pr_i(M_S)\subseteq (S_i)_S$인데, $S_i$는 simple이므로 $S_i\cong S$이면 $(S_i)_S=S_i$이고 그렇지 않으면 $(S_i)_S=0$이다. 따라서 $M_S=\bigoplus_{S_i\cong S}S_i$이고,

$$M=\bigoplus M_S$$

를 얻는다.
:::

이 분해에서, direct summand들 자체는 유일하지 않지만, [명제 9](#prop9){: data-lid="ynv0t" data-relation="weak" }와 [§나눗셈환, ⁋보조정리 10](/ko/math/ring_theory/division_rings#lem10){: data-lid="ay08k" data-relation="weak" }을 결합하면 각 isomorphism class가 등장하는 횟수는 유일함을 알 수 있다. 

::: 명제 10
Simple module들 $S_1,\ldots,S_n$과 $T_1,\ldots,T_m$에 대하여 $\bigoplus_{a=1}^nS_a\cong\bigoplus_{b=1}^mT_b$라면 $n=m$이고, 적당한 permutation $\sigma$에 대하여 모든 $a$에서 $S_a\cong T_{\sigma(a)}$이다.
:::
::: 증명
$M=\bigoplus_{a=1}^nS_a\cong\bigoplus_{b=1}^mT_b$라 하자. [명제 9](#prop9){: data-lid="vnadg" data-relation="required" }에 의해 각 simple module $S$의 isotypic component는

$$M_S=\bigoplus_{S_a\cong S}S_a\cong\bigoplus_{T_b\cong S}T_b$$

이므로, $S_a\cong S$인 인자의 개수를 $n_S$, $T_b\cong S$인 인자의 개수를 $m_S$라 두면 $S^{\oplus n_S}\cong S^{\oplus m_S}$이다. 이제 [§나눗셈환, ⁋보조정리 10](/ko/math/ring_theory/division_rings#lem10){: data-lid="ud5nx" data-relation="required" }에 의해 $D=\End_A(S)$는 division ring이고, $\Hom_A(S, -)$를 취하면

$$D^{n_S}\cong\Hom_A(S, S^{\oplus n_S})\cong\Hom_A(S, S^{\oplus m_S})\cong D^{m_S}$$

이다. $D$-vector space의 차원의 유일성에 의해 $n_S=m_S$이고, 이 등식이 모든 isomorphism class $S$에 대해 성립하므로 $n=\sum n_S=\sum m_S=m$이며 적당한 permutation $\sigma$에 대하여 $S_a\cong T_{\sigma(a)}$이다.
:::

---

**참고문헌**

**[DF]** D. S. Dummit and R. M. Foote, *Abstract algebra*, 3rd ed., Wiley, 2004.  
**[Lam]** T. Y. Lam, *A first course in noncommutative rings*, 2nd ed., Graduate Texts in Mathematics 131, Springer, 2001.
