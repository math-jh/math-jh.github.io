---
title: "Semisimple module"
description: "Simple module들의 직합으로 분해되는 semisimple module을 정의하고, 세 가지 동치 특징(합·직합·모든 submodule이 direct summand)을 Zorn 보조정리로 증명한다. Isotypic 성분에 의한 canonical 분해와, 유한 직합 분해의 유일성을 Schur 보조정리로부터 유도한다."
excerpt: "Semisimple module의 동치 특징, isotypic 분해, 그리고 분해의 유일성"

categories: [Math / Ring Theory]
permalink: /ko/math/ring_theory/semisimple_modules
sidebar: 
    nav: "ring_theory-ko"

date: 2026-07-05

weight: 7

published: false

---

[\[가환대수학\] §조르단-횔더 정리, ⁋정의 1](/ko/math/commutative_algebra/Jordan-Holder_theorem#def1)에서 우리는 simple module을 살펴보았다. Simple module은 $0$이 아니면서 자명한 submodule만을 갖는 module로, composition series를 통해 일반적인 module을 쌓아 올리는 구성 블록의 역할을 한다. 그러나 composition series가 주는 쌓임은 일반적으로 서로 얽혀 있어서, 주어진 module을 simple module들의 직합으로 되돌릴 수는 없다. 이 글에서는 그러한 얽힘이 전혀 없는 module, 곧 simple module들의 직합으로 분해되는 semisimple module을 다룬다. 이들의 세 가지 동치 특징을 증명하고, 같은 isomorphism class의 인자들을 모은 isotypic 분해가 canonical하다는 것과, 유한 직합 분해가 본질적으로 유일하다는 것을 보인다. 이 이론은 이후 semisimple ring의 구조 정리로 이어진다.

이 글에서 ring $R$은 항등원을 갖는, commutative이라 가정하지 않는 ring이며, module은 언제나 left module이다.

## Semisimple module의 정의

::: 정의 1
$R$-module $M$이 적당한 simple submodule들의 family $(S_i)_{i\in I}$에 대하여

$$M=\bigoplus_{i\in I}S_i$$

로 표현될 수 있을 때, $M$을 *semisimple module<sub>반단순 가군</sub>*이라 부른다.
:::

Index 집합 $I$가 공집합인 경우도 허용하므로 $0$은 semisimple module이다. 또 정의에서 직합은 internal direct sum, 즉 $M$의 submodule들의 합이 직합을 이루는 것을 말한다.

::: 예시 2
1. Division ring $D$를 자기 자신 위의 left module로 보면, $D$의 submodule은 left ideal이고, nonzero left ideal $I$는 $0\neq x\in I$에 대해 $1=x^{-1}x\in I$이므로 $I=D$이다. 즉 $D$는 simple $D$-module이다. 일반적으로 $D$ 위의 벡터 space $V$는 기저 $B$를 갖고 (field의 경우와 동일한 Zorn 논증), $V=\bigoplus_{b\in B}Db$는 simple submodule들의 direct sum이므로 $V$는 semisimple이다.
2. $\mathbb{Z}$-module $\mathbb{Z}/6\mathbb{Z}\cong\mathbb{Z}/2\mathbb{Z}\oplus\mathbb{Z}/3\mathbb{Z}$은 semisimple이다. 각 인자는 소수 개의 원소를 갖는 abelian group이므로 proper nonzero subgroup을 가질 수 없어 simple이다.
3. 반면 $\mathbb{Z}$ 자신은 semisimple이 아니다. $\mathbb{Z}$의 두 nonzero submodule $m\mathbb{Z}$, $n\mathbb{Z}$은 언제나 $mn\neq 0$을 공유하므로 $\mathbb{Z}$는 simple submodule을 하나도 갖지 않는다. $\mathbb{Z}/4\mathbb{Z}$ 또한 semisimple이 아닌데, 유일한 proper nonzero submodule $2\mathbb{Z}/4\mathbb{Z}$가 직합의 인자가 될 수 없기 때문이다.
:::

Semisimple module의 유용성은 대부분 다음 보조정리에서 나온다. 이는 simple submodule들의 합이 주어지면, 임의의 submodule을 그 합의 일부로 언제나 보완할 수 있다는 것이다.

::: 보조정리 3
$M=\sum_{i\in I}S_i$가 simple submodule들의 (직합일 필요는 없는) 합이라 하고, $N$을 $M$의 submodule이라 하자. 그럼 적당한 $J\subseteq I$가 존재하여

$$M=N\oplus\bigoplus_{j\in J}S_j$$

이다.
:::
::: 증명
합 $N+\sum_{j\in J}S_j$가 direct sum이 되도록 하는 부분집합 $J\subseteq I$들의 모임을 $\mathcal{J}$라 하자. 공집합이 속하므로 $\mathcal{J}$는 비어 있지 않다. $\mathcal{J}$의 chain이 주어지면 그 합집합에서의 직합 조건은 언제나 유한개의 원소만 관여하므로, 합집합 또한 $\mathcal{J}$에 속한다. 따라서 Zorn 보조정리에 의해 $\mathcal{J}$는 maximal element $J$를 갖는다. $M'=N\oplus\bigoplus_{j\in J}S_j$로 두자.

이제 임의의 $i\in I$에 대하여 $S_i\subseteq M'$임을 주장한다. 만일 $S_i\not\subseteq M'$이라면 $S_i\cap M'$은 $S_i$의 proper submodule이고, $S_i$가 simple이므로 $S_i\cap M'=0$이다. 그럼 합 $N+\sum_{j\in J}S_j+S_i$가 다시 direct sum이 되어 $J\cup\{i\}\in\mathcal{J}$이고, 이는 $J$의 최대성에 모순이다. 따라서 모든 $S_i$가 $M'$에 포함되고, $M=N+\sum_{i\in I}S_i\subseteq M'$이므로 $M=M'$이다.
:::

이 보조정리로부터 semisimple module의 세 가지 동치 특징이 한꺼번에 얻어진다.

::: 정리 4
$R$-module $M$에 대하여 다음이 모두 동치이다.

1. $M$은 simple submodule들의 합이다.
2. $M$은 semisimple이다. 즉 simple submodule들의 direct sum이다.
3. $M$의 모든 submodule은 direct summand이다.
:::
::: 증명
$1\implies 2$는 [보조정리 3](#lem3)을 $N=0$에 적용하면 되고, $2\implies 1$은 자명하며, $1\implies 3$은 다시 [보조정리 3](#lem3) 그 자체이다. 남은 것은 $3\implies 1$이고, 이를 세 단계로 보인다.

우선 성질 3이 submodule에 유전됨을 확인한다. $N$이 $M$의 submodule이고 $L$이 $N$의 submodule이라 하자. 가정에 의해 $M=L\oplus C$인 submodule $C$가 존재한다. 임의의 $n\in N$을 $n=l+c$로 쓰면 $l\in L\subseteq N$이므로 $c=n-l\in N\cap C$이고, 따라서 $N=L+(N\cap C)$이다. 한편 $L\cap(N\cap C)\subseteq L\cap C=0$이므로 이 합은 직합이고, $L$은 $N$의 direct summand이다.

다음으로 $M$의 임의의 nonzero submodule $N$이 simple submodule을 포함함을 보인다. $0\neq x\in N$을 택하고 cyclic submodule $Rx\subseteq N$을 생각하자. $Rx$의 submodule 중 $x$를 포함하지 않는 것들의 모임은 $0$을 포함하므로 비어 있지 않고, chain의 합집합 또한 $x$를 포함하지 않으므로 Zorn 보조정리에 의해 maximal element $K$가 존재한다. $K$를 진포함하는 $Rx$의 submodule은 최대성에 의해 $x$를 포함하므로 $Rx$ 전체와 같고, 따라서 $K$는 $Rx$의 maximal proper submodule이다. 첫 단계에 의해 $Rx$ 또한 성질 3을 가지므로 $Rx=K\oplus S$인 submodule $S$가 존재하고, $S\cong Rx/K$이다. $Rx/K$의 submodule은 $K$와 $Rx$ 사이의 submodule과 대응되는데 $K$가 maximal이므로 $Rx/K$는 simple이다. 즉 $S$는 $N$에 포함된 simple submodule이다.

마지막으로 $M$의 모든 simple submodule의 합을 $N_0$이라 하자. 성질 3에 의해 $M=N_0\oplus C$인 $C$가 존재한다. 만일 $C\neq 0$이라면 둘째 단계에 의해 $C$는 simple submodule $S$를 포함하고, $S$는 $M$의 simple submodule이므로 $S\subseteq N_0\cap C=0$이 되어 모순이다. 따라서 $C=0$이고 $M=N_0$은 simple submodule들의 합이다.
:::

조건 3은 $M$을 가운데 항으로 갖는 모든 short exact sequence가 split한다는 말과 같다. 즉 semisimple module 위에서는 extension 문제가 완전히 자명해진다. 또 조건 1은 semisimple module들의 임의의 합과 직합이 다시 semisimple임을 바로 보여 주는데, simple submodule들의 합들의 합은 여전히 simple submodule들의 합이기 때문이다.

::: 따름정리 5
Semisimple module $M$의 모든 submodule과 quotient는 semisimple이다.
:::
::: 증명
먼저 quotient의 경우를 보자. $\pi:M\rightarrow M/N$을 canonical projection이라 하고 $M=\sum_{i\in I}S_i$를 simple들의 합으로 쓰면 $M/N=\sum_{i\in I}\pi(S_i)$이다. 각 $i$에 대하여 $\pi(S_i)\cong S_i/(S_i\cap N)$인데, $S_i$가 simple이므로 $S_i\cap N$은 $0$이거나 $S_i$이고, 따라서 $\pi(S_i)$는 $S_i$와 isomorphic하거나 $0$이다. 즉 $M/N$은 simple submodule들의 합이고 [정리 4](#thm4)에 의해 semisimple이다.

Submodule $N$의 경우, [보조정리 3](#lem3)에 의해 $M=N\oplus\bigoplus_{j\in J}S_j$인 $J$가 존재하므로 $N\cong M/\bigoplus_{j\in J}S_j$이고, 방금 보인 quotient의 경우로 환원된다.
:::

## Isotypic 분해

[예시 2](#ex2)의 벡터 space에서 보듯 semisimple module의 direct sum 분해는 기저의 선택만큼이나 유일하지 않다. 그러나 서로 isomorphic한 인자들을 한데 모으면 분해는 canonical해진다. 이를 정확히 하기 위해 먼저 simple submodule들의 합 안에 어떤 simple submodule들이 살 수 있는지를 확인한다.

::: 보조정리 6
$M=\sum_{i\in I}S_i$가 simple submodule들의 합이라 하자. 그럼 $M$의 임의의 simple submodule $U$는 적당한 $i\in I$에 대하여 $S_i$와 isomorphic하다.
:::
::: 증명
[보조정리 3](#lem3)을 $N=U$에 적용하면 $M=U\oplus\bigoplus_{j\in J}S_j$인 $J$가 존재한다. $p:M\rightarrow U$를 이 분해에 대한 projection이라 하자. $U=p(M)=\sum_{i\in I}p(S_i)$이고 $U\neq 0$이므로 $p(S_i)\neq 0$인 $i$가 존재한다. 그럼 $p$의 제한 $S_i\rightarrow U$는 simple module 사이의 nonzero homomorphism이므로 [§Division ring, ⁋보조정리 10](/ko/math/ring_theory/division_rings#lem10)에 의해 isomorphism이다.
:::

::: 정의 7
Simple $R$-module $S$에 대하여, $R$-module $M$의 *$S$-isotypic component<sub>등형 성분</sub>* $M_S$는 $S$와 isomorphic한 $M$의 simple submodule 전부의 합으로 정의한다.
:::

정의에서 $M_S$는 $S$의 isomorphism class에만 의존한다. $S$와 isomorphic한 simple submodule이 없다면 $M_S=0$이다. 임의의 semisimple module은 그 정의에 의해 isotypic component들의 합이 되는데, 다음 명제는 이 합이 사실 직합이며 module의 구조만으로 결정되는 canonical한 분해임을 보여 준다.

::: 명제 8
Semisimple module $M$, $N$에 대하여 다음이 성립한다.

1. Simple module들의 isomorphism class 대표들 $S$에 대하여 $M=\bigoplus_{[S]}M_S$이다.
2. 임의의 $R$-module homomorphism $f:M\rightarrow N$은 $f(M_S)\subseteq N_S$를 만족한다.
:::
::: 증명
2를 먼저 보인다. $T$가 $S$와 isomorphic한 $M$의 simple submodule이라 하자. $f(T)\cong T/(T\cap\ker f)$는 $T$가 simple이므로 $0$이거나 $T\cong S$와 isomorphic하고, 어느 경우에도 $f(T)\subseteq N_S$이다. $M_S$는 이러한 $T$들의 합이므로 $f(M_S)\subseteq N_S$이다.

이제 1을 보인다. $M$의 semisimple 분해의 각 인자는 자신의 isomorphism class에 대응하는 isotypic component에 포함되므로 $M=\sum_{[S]}M_S$이다. 직합임을 보이기 위해, 고정된 class $[S]$에 대하여 $W=M_S\cap\sum_{[T]\neq[S]}M_T$가 $0$임을 확인하면 충분하다. $W$는 semisimple module $M$의 submodule이므로 [따름정리 5](#cor5)에 의해 semisimple이고, 만일 $W\neq 0$이라면 simple submodule $U\subseteq W$가 존재한다. $U$는 $S$-type simple들의 합 $M_S$에 포함되므로 [보조정리 6](#lem6)에 의해 $U\cong S$이다. 그러나 $U$는 동시에 $S$와 isomorphic하지 않은 simple들의 합 $\sum_{[T]\neq[S]}M_T$에도 포함되므로, 다시 [보조정리 6](#lem6)에 의해 $U$는 어떤 $T\not\cong S$와 isomorphic해야 하고 이는 모순이다. 따라서 $W=0$이다.
:::

명제의 둘째 결과는 isotypic 분해가 canonical하다는 말의 정확한 내용이다. 임의의 endomorphism이 각 isotypic component를 보존하므로, 이 분해는 직합 인자의 선택과 무관하게 $M$의 module 구조만으로 결정된다.

## 분해의 유일성

Semisimple 분해에서 인자들 자체는 유일하지 않지만, 각 isomorphism class가 등장하는 횟수는 유일하다. 유한 direct sum의 경우 이는 다음과 같이 정확해진다.

::: 명제 9
Simple module들 $S_1,\ldots,S_n$과 $T_1,\ldots,T_m$에 대하여 $\bigoplus_{a=1}^nS_a\cong\bigoplus_{b=1}^mT_b$라면 $n=m$이고, 적당한 permutation $\sigma$에 대하여 모든 $a$에서 $S_a\cong T_{\sigma(a)}$이다.
:::
::: 증명
$n$에 대한 induction으로 보인다. $n=0$이면 좌변이 $0$이므로 우변도 $0$이고 $m=0$이다.

$n\geq 1$이라 하고 $\varphi:\bigoplus_aS_a\rightarrow\bigoplus_bT_b$를 isomorphism이라 하자. $\varphi(S_1)\neq 0$이므로 projection $\pi_b:\bigoplus T_b\rightarrow T_b$ 중 $\pi_b\vert_{\varphi(S_1)}\neq 0$인 $b$가 존재하고, 재배열하여 $b=1$이라 하자. $N=\varphi(S_1)$으로 두면 $N\cong S_1$은 simple이고, $\pi_1\vert_N:N\rightarrow T_1$은 simple module 사이의 nonzero homomorphism이므로 [§Division ring, ⁋보조정리 10](/ko/math/ring_theory/division_rings#lem10)에 의해 isomorphism이다. 특히 $S_1\cong T_1$이다.

이제 $\bigoplus_bT_b=N\oplus(T_2\oplus\cdots\oplus T_m)$임을 주장한다. $N\cap(T_2\oplus\cdots\oplus T_m)=N\cap\ker\pi_1=\ker(\pi_1\vert_N)=0$이다. 또 임의의 $t\in\bigoplus T_b$에 대하여 $x=(\pi_1\vert_N)^{-1}(\pi_1(t))\in N$으로 두면 $t-x\in\ker\pi_1=T_2\oplus\cdots\oplus T_m$이므로 합이 전체가 된다. 따라서

$$T_2\oplus\cdots\oplus T_m\cong\Big(\bigoplus_bT_b\Big)/N\cong\Big(\bigoplus_aS_a\Big)/S_1\cong S_2\oplus\cdots\oplus S_n$$

이고, 가운데 isomorphism은 $\varphi(S_1)=N$이므로 $\varphi$가 유도하는 것이다. Induction 가정에 의해 $n-1=m-1$이고 나머지 인자들이 대응되므로, $S_1\cong T_1$과 합쳐 증명이 끝난다.
:::

즉 유한개의 simple module의 direct sum은 그 인자들의 isomorphism class와 중복도를 (순서를 무시하면) 완전히 결정한다. [명제 8](#prop8)의 isotypic 분해와 함께 쓰면, 유한개의 simple의 직합인 semisimple module은 각 class $[S]$의 중복도 자료만으로 분류된다. 이 유일성은 semisimple ring의 구조 정리에서 행렬 크기와 division ring의 유일성을 담당하게 된다.

---

**참고문헌**

**[DF]** D. S. Dummit and R. M. Foote, *Abstract algebra*, 3rd ed., Wiley, 2004.

**[Lam]** T. Y. Lam, *A first course in noncommutative rings*, 2nd ed., Graduate Texts in Mathematics 131, Springer, 2001.
