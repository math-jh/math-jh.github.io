---
title: "국소적 옹골공간과 일점 옹골화"
description: "점마다 compact neighborhood를 갖는 국소적 옹골공간을 정의하고 그 성질을 다룬 뒤, 한 점을 더해 compact 공간을 얻는 일점(Alexandroff) 옹골화를 구성하여 그 보편성과 Hausdorff 판정을 증명한다."
excerpt: "Locally compact spaces and the one-point (Alexandroff) compactification"

categories: [Math / Topology]
permalink: /ko/math/topology/locally_compact_spaces
sidebar: 
    nav: "topology-ko"

date: 2026-07-01
last_modified_at: 2026-07-01
weight: 16.5

published: false

---

## 국소적 옹골공간

Compactness는 위상공간이 지닐 수 있는 성질 가운데 가장 강력한 것에 속하지만, 정작 우리가 다루는 많은 공간은 compact가 아니다. Euclidean space $$\mathbb{R}^n$$은 유계가 아니어서 compact가 아니고, 위상다양체 역시 국소적으로만 Euclidean space를 닮았을 뿐 전체로는 compact일 이유가 없다. ([§옹골성, ⁋정의 9](/ko/math/topology/compactness#def9)) 그럼에도 이러한 공간들은 각 점 주위에서만큼은 compact 공간처럼 행동한다. 우리는 이 국소적인 성질을 분리해 내어, 전역적 compactness가 없는 공간에서도 compact 공간의 논증을 국소적으로 되살리고자 한다. 더 나아가 이러한 공간에 단 하나의 점을 더하는 것만으로 compact 공간을 얻을 수 있음을 보게 될 것이다.

우리는 이 개념을 [§옹골성, ⁋정의 3](/ko/math/topology/compactness#def3)에서 이미 도입한 바 있으며, 이 글의 출발점으로 삼기 위해 여기에 다시 적는다.

::: 정의 1
위상공간 $$X$$가 점 $$x\in X$$에서 *locally compact<sub>국소적으로 옹골</sub>*라는 것은 $$x$$를 포함하는 $$X$$의 compact neighborhood가 존재하는 것이다. $$X$$가 모든 점에서 locally compact일 때 $$X$$를 *locally compact space<sub>국소적 옹골공간</sub>*이라 부른다. Locally compact이며 Hausdorff인 공간을 줄여 *LCH space*라 적기로 한다.
:::

여기에서 $$x$$의 neighborhood란 $$x$$를 포함하는 열린집합을 다시 품는 부분집합을 뜻하므로, compact neighborhood는 반드시 열린집합일 필요가 없다. 예컨대 $$\mathbb{R}$$에서 닫힌구간 $$[-1,1]$$은 $$0$$의 compact neighborhood이지만 열린집합은 아니다. 이처럼 정의는 compact인 근방 하나의 존재만을 요구하는 약한 형태이지만, 공간이 Hausdorff이면 이 조건이 훨씬 다루기 쉬운 형태로 다시 서술된다.

::: 명제 2
Hausdorff space $$X$$의 점 $$x$$에 대하여 다음 두 조건은 동치이다.

1. $$X$$는 $$x$$에서 locally compact이다.
2. $$x$$의 임의의 열린근방 $$V$$에 대하여, 열린집합 $$W$$가 존재하여 $$x\in W$$, $$\cl(W)\subseteq V$$이며 $$\cl(W)$$가 compact이다.
:::
::: 증명
둘째 조건에서 $$V=X$$로 두면 $$\cl(W)$$가 $$x$$를 품는 열린집합 $$W$$를 포함하는 compact 집합이 되어 $$x$$의 compact neighborhood를 이루므로, 둘째 조건은 첫째 조건을 함의한다.

거꾸로 $$X$$가 $$x$$에서 locally compact라 하고 $$x$$의 열린근방 $$V$$가 주어졌다 하자. $$x$$의 compact neighborhood $$K$$를 잡고 $$U=\interior(K)$$라 두면 $$U$$는 $$x$$를 품는 열린집합이며 $$U\subseteq K$$이다. 이제 $$V$$를 $$V\cap U$$로 바꾸어 처음부터 $$V\subseteq U\subseteq K$$라 가정하여도 무방하다. 더 작은 $$V$$에 대해 결론을 얻으면 원래의 $$V$$에 대해서도 결론이 성립하기 때문이다.

$$K$$는 compact Hausdorff space이므로 regular space이다. ([§옹골공간, ⁋보조정리 6](/ko/math/topology/compact_spaces#lem6)) 한편 $$V\subseteq K$$는 $$X$$의 열린집합이므로 부분공간 $$K$$에서도 열린집합이고, 따라서 $$K\setminus V$$는 $$K$$의 닫힌집합으로서 $$x$$를 포함하지 않는다. $$K$$의 regularity를 점 $$x$$와 닫힌집합 $$K\setminus V$$에 적용하면, $$K$$에서 열린 서로소인 두 집합 $$P\ni x$$와 $$Q\supseteq K\setminus V$$를 얻는다. $$P\subseteq K\setminus Q\subseteq V$$이고 $$K\setminus Q$$는 $$K$$의 닫힌집합이므로 $$\cl_K(P)\subseteq K\setminus Q\subseteq V$$이다.

이제 $$W=P\cap U$$라 두자. $$P$$는 $$K$$에서 열린집합이고 $$U$$는 $$X$$의 열린집합이며 $$U\subseteq K$$이므로 $$W$$는 $$X$$에서 열린집합이고 $$x\in W$$이다. $$W\subseteq U\subseteq K$$이고 $$K$$는 $$X$$의 닫힌집합이므로 ([§옹골공간, ⁋따름정리 5](/ko/math/topology/compact_spaces#cor5)) $$\cl(W)\subseteq K$$이다. 따라서 $$\cl(W)=\cl(W)\cap K=\cl_K(W)\subseteq\cl_K(P)\subseteq V$$이다. 끝으로 $$\cl(W)$$는 compact 집합 $$K$$의 닫힌 부분집합이므로 compact이다. ([§옹골공간, ⁋보조정리 3](/ko/math/topology/compact_spaces#lem3)) 이로써 둘째 조건이 성립한다.
:::

[명제 2](#prop2)의 둘째 조건은 LCH space에서 각 점이 compact closure를 갖는 열린집합들로 이루어진 neighborhood basis를 가진다는 것으로 읽을 수 있다. 이는 앞으로 국소적 논증을 펼칠 때마다 반복적으로 사용되며, 일점 옹골화의 Hausdorff성을 판정할 때에도 핵심적인 역할을 한다. 또한 이 성질로부터 임의의 LCH space가 regular임이 곧바로 따르는데, 점 $$x$$와 이를 포함하지 않는 닫힌집합 $$C$$가 주어지면 $$V=X\setminus C$$에 둘째 조건을 적용하여 얻은 $$W$$와 $$X\setminus\cl(W)$$가 $$x$$와 $$C$$를 분리하기 때문이다.

가장 기본적인 예로 Euclidean space $$\mathbb{R}^n$$이 LCH임을 들 수 있다. 임의의 점 $$x$$에 대하여 닫힌 공 $$\{y\mid\lVert y-x\rVert\leq 1\}$$은 Heine–Borel 정리에 의해 compact이고 열린 공을 품으므로 $$x$$의 compact neighborhood를 이루며, $$\mathbb{R}^n$$이 Hausdorff임은 이미 알고 있다. 마찬가지로 임의의 discrete space도 LCH인데, 각 점 $$x$$에 대하여 한원소집합 $$\{x\}$$이 열린 유한집합으로서 compact neighborhood가 되고 discrete space는 Hausdorff이기 때문이다. 조금 덜 자명한 예는 위상다양체이다.

::: 예시 3
임의의 topological manifold $$M$$은 LCH space이다. ([§옹골성, ⁋정의 9](/ko/math/topology/compactness#def9)) 정의상 $$M$$은 Hausdorff이며, 각 점 $$x$$는 $$\mathbb{R}^n$$의 열린집합과 homeomorphic한 열린근방 $$U$$를 가진다. 그 homeomorphism 아래에서 $$x$$에 대응하는 점은 $$\mathbb{R}^n$$에서 compact neighborhood를 가지므로 ($$\mathbb{R}^n$$이 LCH이기 때문이다), 이를 $$U$$로 되끌어 오면 $$x$$의 compact neighborhood를 얻는다.
:::

Locally compact이라는 조건은 얼핏 매우 약해 보이지만 결코 자동으로 주어지는 것은 아니다. 다음은 국소적 옹골공간이 아닌 대표적인 예이다.

::: 예시 4
유리수 공간 $$\mathbb{Q}$$는 $$\mathbb{R}$$의 부분공간으로서 어떤 점에서도 locally compact가 아니다. 대칭성에 의해 $$0$$에서 그렇지 않음을 보이면 충분하다. 결론에 반하여 $$0$$의 compact neighborhood $$K\subseteq\mathbb{Q}$$가 존재한다 하자. 그럼 $$K$$는 $$0$$을 품는 열린집합을 포함하므로 어떤 $$\delta>0$$에 대하여 $$\mathbb{Q}\cap(-\delta,\delta)\subseteq K$$이고, $$0<r<\delta$$를 하나 고정하면 $$\mathbb{Q}\cap[-r,r]\subseteq K$$이다.

Compactness는 부분공간이 놓인 주변 공간과 무관한 내재적 성질이므로 $$K$$는 $$\mathbb{R}$$의 부분공간으로서도 compact이고, $$\mathbb{R}$$이 Hausdorff이므로 $$K$$는 $$\mathbb{R}$$의 닫힌집합이다. ([§옹골공간, ⁋따름정리 5](/ko/math/topology/compact_spaces#cor5)) 그런데 $$\mathbb{R}$$에서 $$\mathbb{Q}\cap[-r,r]$$의 closure는 $$[-r,r]$$ 전체이므로, $$K$$가 닫힌집합이면서 $$\mathbb{Q}\cap[-r,r]$$을 포함한다는 사실로부터 $$[-r,r]\subseteq K$$를 얻는다. 이는 $$K\subseteq\mathbb{Q}$$이면서 $$[-r,r]$$이 무리수를 포함한다는 사실에 모순이다.
:::

국소적 옹골성은 적당한 부분공간으로 유전된다. 다만 임의의 부분공간이 아니라 열린집합이거나 닫힌집합인 부분공간에 한하여 그러하다.

::: 명제 5
LCH space $$X$$의 열린 부분공간과 닫힌 부분공간은 모두 LCH space이다.
:::
::: 증명
Hausdorff space의 부분공간은 다시 Hausdorff이므로 국소적 옹골성만 확인하면 된다.

먼저 $$A\subseteq X$$가 열린집합이라 하고 $$x\in A$$가 주어졌다 하자. $$A$$는 $$x$$의 $$X$$에서의 열린근방이므로 [명제 2](#prop2)의 둘째 조건에 의하여 $$X$$의 열린집합 $$W$$가 존재하여 $$x\in W$$이고 $$\cl_X(W)\subseteq A$$이며 $$\cl_X(W)$$가 compact이다. $$\cl_X(W)\subseteq A$$이므로 $$A$$에서의 closure $$\cl_A(W)$$는 $$\cl_X(W)$$와 같고, 이는 compact이면서 $$A$$에서 열린 $$W$$를 포함하므로 $$x$$의 $$A$$에서의 compact neighborhood이다.

이제 $$A\subseteq X$$가 닫힌집합이라 하고 $$x\in A$$가 주어졌다 하자. $$X$$에서 $$x$$의 compact neighborhood $$K$$를 잡고, $$x$$를 품는 $$X$$의 열린집합 $$U\subseteq K$$를 택한다. 그럼 $$K\cap A$$는 compact 집합 $$K$$의 닫힌 부분집합이므로 compact이고 ([§옹골공간, ⁋보조정리 3](/ko/math/topology/compact_spaces#lem3)), $$U\cap A$$는 $$A$$에서 열린집합으로서 $$x$$를 품고 $$K\cap A$$에 포함되므로 $$K\cap A$$는 $$x$$의 $$A$$에서의 compact neighborhood이다.
:::

## 일점 옹골화의 구성

Compact가 아닌 공간을 compact로 만드는 가장 경제적인 방법은 부족한 부분을 단 하나의 점으로 메우는 것이다. 직관적으로는 $$\mathbb{R}$$의 양끝으로 달아나는 점들을 하나의 무한원점으로 모아 원을 만드는 것과 같다. 이러한 옹골화의 존재와 유일성은 LCH space에 대하여 이미 [§옹골성, ⁋정리 4](/ko/math/topology/compactness#thm4)에서 증명한 바 있다. 여기에서는 같은 결과를 임의의 위상공간에 통하는 명시적 구성으로 다시 이끌어 내고, 그 구성이 언제 Hausdorff 공간을 낳는지까지 규명하여 그 정리를 정련한다. 우리는 이 구성을 임의의 위상공간에 대해 정식화한다.

::: 정의 6
위상공간 $$X$$가 주어졌다 하자. $$X$$에 속하지 않는 새로운 점 하나를 $$\infty$$라 적고 집합 $$X^+=X\cup\{\infty\}$$을 생각한다. $$X^+$$의 부분집합 가운데 다음 두 종류를 열린집합으로 선언한다. 첫째로 $$X$$의 열린집합 $$U$$, 둘째로 $$X$$에서 compact이며 닫힌 부분집합 $$C$$에 대한 $$X^+\setminus C$$이다. 이렇게 얻은 위상공간 $$X^+$$를 $$X$$의 *one-point compactification<sub>일점 옹골화</sub>*, 또는 *Alexandroff compactification*이라 부른다.
:::

이 선언이 실제로 [§열린집합, ⁋정의 1](/ko/math/topology/open_sets#def1)의 위상 공리를 만족함을 확인해야 한다. 공집합은 $$X$$의 열린집합이므로 첫째 종류에 속하고, 공집합은 compact이며 닫힌집합이므로 $$X^+=X^+\setminus\emptyset$$은 둘째 종류에 속한다. 두 열린집합의 교집합에 대해서는 세 경우를 따진다. 첫째 종류 둘의 교집합은 $$X$$의 열린집합이다. 둘째 종류 둘의 교집합은 $$(X^+\setminus C)\cap(X^+\setminus D)=X^+\setminus(C\cup D)$$이고 $$C\cup D$$가 compact인 닫힌집합이므로 다시 둘째 종류이다. 서로 다른 종류의 교집합은 $$U\cap(X^+\setminus C)=U\cap(X\setminus C)$$이며 $$C$$가 닫힌집합이므로 $$X\setminus C$$가 열린집합이 되어 $$X$$의 열린집합, 곧 첫째 종류이다. 임의의 합집합에 대해서도 마찬가지로, 첫째 종류들의 합집합은 열린집합이고, 둘째 종류들의 합집합 $$\bigcup_\alpha(X^+\setminus C_\alpha)=X^+\setminus\bigcap_\alpha C_\alpha$$은 $$\bigcap_\alpha C_\alpha$$가 어떤 $$C_\alpha$$의 닫힌 부분집합으로서 compact이므로 ([§옹골공간, ⁋보조정리 3](/ko/math/topology/compact_spaces#lem3)) 둘째 종류이며, 두 종류가 섞인 합집합은 $$U\cup(X^+\setminus C)=X^+\setminus(C\cap(X\setminus U))$$인데 $$C\cap(X\setminus U)$$가 compact인 닫힌집합이므로 둘째 종류이다.

이 위상에서 $$X$$가 $$X^+$$에 어떻게 놓이는지를 먼저 정리한다.

::: 명제 7
포함사상 $$X\hookrightarrow X^+$$는 열린 매장, 곧 $$X$$를 $$X^+$$의 열린 부분공간으로 놓는 homeomorphism이다. 또한 $$X$$가 $$X^+$$에서 조밀할 필요충분조건은 $$X$$가 compact가 아닌 것이다.
:::
::: 증명
$$X$$는 $$X$$의 열린집합이므로 [정의 6](#def6)의 첫째 종류로서 $$X^+$$의 열린집합이다. $$X^+$$의 열린집합을 $$X$$와 교차시키면, 첫째 종류 $$U$$에 대해서는 $$U\cap X=U$$이고 둘째 종류 $$X^+\setminus C$$에 대해서는 $$(X^+\setminus C)\cap X=X\setminus C$$인데 둘 다 $$X$$의 열린집합이며, 거꾸로 $$X$$의 임의의 열린집합은 첫째 종류로서 $$X^+$$에서 열린집합이다. 따라서 $$X$$ 위의 부분공간 위상은 원래의 위상과 일치하고, 포함사상은 열린 부분공간 위로의 homeomorphism이다.

$$\{\infty\}=X^+\setminus X$$는 열린집합 $$X$$의 여집합이므로 닫힌집합이다. $$X$$가 조밀하다는 것은 $$\infty\in\cl(X)$$인 것, 곧 $$\infty$$의 임의의 열린근방이 $$X$$와 만나는 것과 같다. $$\infty$$를 품는 열린집합은 반드시 둘째 종류 $$X^+\setminus C$$이며, 이것이 $$X$$와 만나는 것은 $$X\setminus C\neq\emptyset$$, 곧 $$C\neq X$$인 것과 같다. 따라서 $$X$$가 조밀하지 않을 필요충분조건은 어떤 compact인 닫힌집합 $$C$$에 대해 $$C=X$$인 것, 곧 $$X$$ 자신이 compact인 것이다.
:::

$$X$$가 compact인 경우에는 $$X$$ 자체가 compact이며 닫힌집합이므로 $$\{\infty\}=X^+\setminus X$$가 열린집합이 되어 $$\infty$$가 고립점이 된다. 이 경우 $$X^+$$는 $$X$$에 고립된 한 점을 덧붙인 것에 지나지 않아 흥미롭지 않다. 일점 옹골화가 본래 의도한 역할을 하는 것은 $$X$$가 compact가 아닐 때이며, 이때 $$\infty$$는 $$X$$ 바깥으로 달아나는 모든 방향의 극한점 노릇을 한다.

::: 정리 8
임의의 위상공간 $$X$$에 대하여 $$X^+$$는 compact이다.
:::
::: 증명
$$X^+$$의 임의의 open covering $$(O_i)_{i\in I}$$이 주어졌다 하자. $$\infty$$를 덮는 열린집합 $$O_j$$가 적어도 하나 존재하며, 이는 반드시 둘째 종류이므로 $$X$$의 compact인 닫힌집합 $$C$$에 대해 $$O_j=X^+\setminus C$$로 적을 수 있다. 나머지 $$(O_i)_{i\neq j}$$은 $$C\subseteq X^+\setminus O_j$$을 덮어야 하며, 각 $$O_i\cap X$$는 $$X$$의 열린집합이므로 $$(O_i\cap X)_{i\neq j}$$은 $$C$$의 $$X$$에서의 open covering이다. $$C$$가 compact이므로 유한한 $$J\subseteq I\setminus\{j\}$$을 택하여 $$C\subseteq\bigcup_{i\in J}(O_i\cap X)\subseteq\bigcup_{i\in J}O_i$$이도록 할 수 있다. ([§옹골공간, ⁋명제 2](/ko/math/topology/compact_spaces#prop2)) 그럼 $$(O_i)_{i\in J\cup\{j\}}$$이 $$X^+$$를 덮는 finite subcover이다.
:::

## Hausdorff 판정과 보편성

일점 옹골화는 어떤 공간에 대해서도 compact 공간을 낳지만, 그 결과가 다시 Hausdorff가 되는지는 별개의 문제이다. 예컨대 $$\mathbb{Q}^+$$은 compact이지만 Hausdorff가 아니다. 다음 정리는 $$X^+$$가 Hausdorff가 되는 조건이 정확히 앞서 정의한 국소적 옹골성임을 밝힌다.

::: 정리 9
위상공간 $$X$$에 대하여 $$X^+$$가 Hausdorff space일 필요충분조건은 $$X$$가 LCH space인 것이다.
:::
::: 증명
먼저 $$X^+$$가 Hausdorff라 하자. 부분공간 $$X$$는 Hausdorff space의 부분공간이므로 Hausdorff이다. 국소적 옹골성을 보이기 위해 $$x\in X$$를 고정하면, $$X^+$$의 Hausdorff성에 의해 $$x$$와 $$\infty$$를 분리하는 서로소인 열린집합 $$U\ni x$$와 $$W\ni\infty$$가 존재한다. $$W$$는 $$\infty$$를 품으므로 둘째 종류이고, 따라서 $$X$$의 compact인 닫힌집합 $$C$$에 대해 $$W=X^+\setminus C$$이다. $$U\cap W=\emptyset$$으로부터 $$U\subseteq C$$이고, $$U$$는 $$\infty$$를 품지 않으므로 $$X$$에 포함되는 열린집합이다. 따라서 $$C$$는 $$x$$를 품는 열린집합 $$U$$를 포함하는 compact 집합, 곧 $$x$$의 compact neighborhood이며 $$X$$는 $$x$$에서 locally compact이다.

거꾸로 $$X$$가 LCH라 하자. $$X^+$$의 서로 다른 두 점을 분리해야 한다. 두 점이 모두 $$X$$에 속하면 $$X$$가 Hausdorff이므로 이들을 $$X$$에서 분리하는 서로소인 열린집합을 얻고, 이들은 [정의 6](#def6)의 첫째 종류로서 $$X^+$$에서도 열린집합이다. 남은 경우는 한 점이 $$x\in X$$이고 다른 한 점이 $$\infty$$인 경우이다. $$X$$가 Hausdorff이므로 [명제 2](#prop2)에 의하여 $$x$$의 열린근방 $$U$$가 존재하여 $$K=\cl(U)$$가 compact이다. $$X$$가 Hausdorff이므로 $$K$$는 닫힌집합이고 ([§옹골공간, ⁋따름정리 5](/ko/math/topology/compact_spaces#cor5)), 따라서 $$X^+\setminus K$$는 $$\infty$$를 품는 둘째 종류의 열린집합이다. $$U\subseteq K$$이므로 $$U$$와 $$X^+\setminus K$$는 서로소이며 각각 $$x$$와 $$\infty$$를 분리한다.
:::

[정리 8](#thm8)과 [정리 9](#thm9)를 합치면, $$X$$가 LCH space일 때 $$X^+$$는 compact Hausdorff space가 되고 [명제 7](#prop7)에 의해 $$X$$는 그 안에 열린 부분공간으로 매장된다. 특히 $$X$$가 compact가 아니라면 이 매장은 조밀하다. 이는 [§옹골성, ⁋정리 4](/ko/math/topology/compactness#thm4)에서 이미 증명한 Alexandroff 정리의 존재 부분에 해당하며, 여기에서는 이를 임의의 $$X$$에 통하는 명시적 구성으로 다시 얻은 것이다. 남은 것은 이러한 옹골화가 본질적으로 유일하다는 사실이며, 이는 다음의 보편성으로 정식화된다.

::: 정리 10
LCH space $$X$$가 주어졌다 하자. compact Hausdorff space $$Y$$와 점 $$p\in Y$$, 그리고 homeomorphism $$\varphi:X\to Y\setminus\{p\}$$이 주어졌다 하면, 유일한 homeomorphism $$h:X^+\to Y$$가 존재하여 $$X$$ 위에서 $$h=\varphi$$이고 $$h(\infty)=p$$이다.
:::
::: 증명
$$\varphi$$를 통해 $$X$$와 $$Y\setminus\{p\}$$을 동일시하고, $$X$$를 $$Y$$의 부분집합으로 본다. $$Y$$가 Hausdorff이므로 $$\{p\}$$는 $$Y$$의 닫힌집합이고, 따라서 $$X=Y\setminus\{p\}$$는 $$Y$$의 열린 부분공간이다. 즉 $$X$$의 위상은 $$Y$$로부터 유도된 부분공간 위상과 일치한다.

이제 $$Y$$의 열린집합이 정확히 $$X^+$$의 열린집합과 대응함을 보인다. $$Y$$의 열린집합 $$O$$가 $$p$$를 포함하지 않으면 $$O\subseteq X$$이고 $$X$$가 $$Y$$의 열린 부분공간이므로 $$O$$는 $$X$$의 열린집합, 곧 [정의 6](#def6)의 첫째 종류이다. 거꾸로 $$X$$의 열린집합은 $$X$$가 $$Y$$에서 열린집합이므로 $$Y$$의 열린집합이다. 한편 $$Y$$의 열린집합 $$O$$가 $$p$$를 포함하면 $$Y\setminus O$$는 compact 공간 $$Y$$의 닫힌집합이므로 compact이고 ([§옹골공간, ⁋보조정리 3](/ko/math/topology/compact_spaces#lem3)), $$Y\setminus O\subseteq X$$이며 $$Y$$에서 닫힌집합이므로 $$X$$에서도 닫힌집합이다. 따라서 $$O=X^+\setminus(Y\setminus O)$$은 $$X$$의 compact인 닫힌집합의 여집합, 곧 둘째 종류이다. 거꾸로 $$X$$의 compact인 닫힌집합 $$C$$에 대하여 $$C$$는 $$Y$$에서도 compact이고 $$Y$$가 Hausdorff이므로 닫힌집합이어서 ([§옹골공간, ⁋따름정리 5](/ko/math/topology/compact_spaces#cor5)) $$Y\setminus C$$는 $$p$$를 품는 $$Y$$의 열린집합이다.

그러므로 $$p$$를 $$\infty$$와 동일시하는 집합 사이의 대응 $$h:X^+\to Y$$는 열린집합을 열린집합으로, 그 역도 마찬가지로 대응시키는 전단사이며, 따라서 homeomorphism이다. $$h$$는 $$X$$ 위에서 $$\varphi$$와 일치하고 $$\infty$$를 $$p$$로 보내야 하므로 유일하다.
:::

[정리 10](#thm10)은 LCH space $$X$$에 한 점을 더해 compact Hausdorff space를 만드는 방법이 위상동형을 무시하면 오직 하나뿐임을 말한다. 이는 [§옹골성, ⁋정리 4](/ko/math/topology/compactness#thm4)의 유일성 부분을 보편성의 언어로 다시 서술한 것이다. 이 유일성 덕분에 우리는 이후 $$X^+$$를 그 구체적 구성과 무관하게 다룰 수 있고, 실제 계산에서는 임의의 편리한 compact Hausdorff 모델을 골라 $$X^+$$와 동일시하면 된다.

![일점 옹골화의 보편성](/assets/images/Math/Topology/Locally_Compact_Spaces-1.svg){:style="width:6.23em" class="invert" .align-center}

::: 참고 11
일점 옹골화는 Hausdorff 옹골화 가운데 가장 작은 것으로 특징지어진다. Compact가 아닌 LCH space $$X$$의 *Hausdorff 옹골화*란 $$X$$를 조밀한 부분공간으로 품는 compact Hausdorff space를 말하는데, 이러한 임의의 옹골화에서 출발하여 $$X$$ 바깥의 점들을 모두 하나로 뭉개면 $$X^+$$로 향하는 연속인 전사가 유일하게 얻어진다. 이 사실의 증명에는 LCH space가 Hausdorff space에 조밀하게 매장되면 항상 열린 부분공간이 된다는 관찰이 필요하며, 자세한 논증은 표준적인 문헌을 따른다. **[Mun]** 반대편 극단에는 완전정칙 공간이 가질 수 있는 가장 큰 Hausdorff 옹골화인 *Stone–Čech compactification*이 있으나, 이는 별도의 구성을 요구하므로 여기에서는 이름만 언급한다.
:::

## 일점 옹골화의 예

가장 익숙한 예는 Euclidean space의 일점 옹골화가 구면이 된다는 사실이다.

::: 예시 12
$$n$$-구면 $$S^n=\{x\in\mathbb{R}^{n+1}\mid\lVert x\rVert=1\}$$의 북극 $$N=(0,\ldots,0,1)$$을 생각하자. Stereographic projection

$$\sigma:S^n\setminus\{N\}\to\mathbb{R}^n,\qquad \sigma(x_1,\ldots,x_{n+1})=\frac{1}{1-x_{n+1}}(x_1,\ldots,x_n)$$

은 $$S^n\setminus\{N\}$$과 $$\mathbb{R}^n$$ 사이의 homeomorphism임이 잘 알려져 있다. $$S^n$$은 $$\mathbb{R}^{n+1}$$의 닫힌 유계 부분집합이므로 Heine–Borel 정리에 의해 compact이고, 부분공간으로서 Hausdorff이다. 따라서 $$S^n$$은 compact Hausdorff space이고 $$N$$이라는 한 점을 제거한 것이 $$\mathbb{R}^n$$과 homeomorphic하므로, [정리 10](#thm10)에 의하여 유일한 homeomorphism

$$(\mathbb{R}^n)^+\cong S^n$$

이 성립하며 무한원점 $$\infty$$가 북극 $$N$$에 대응한다. 특히 $$(\mathbb{R})^+$$은 원 $$S^1$$이다.
:::

Discrete space의 일점 옹골화는 수렴하는 점열이라는 매우 구체적인 그림을 준다.

::: 예시 13
자연수 집합 $$\mathbb{N}=\{1,2,3,\ldots\}$$에 discrete topology를 주자. 이는 discrete space로서 LCH이므로 [정리 9](#thm9)에 의하여 $$\mathbb{N}^+$$은 compact Hausdorff space이다. Discrete space에서 compact인 부분집합은 유한집합뿐이므로, $$\mathbb{N}^+$$에서 $$\infty$$의 열린근방은 유한집합의 여집합, 곧 $$\infty$$를 품는 cofinite set이다. 이는 정확히 $$\mathbb{N}$$의 점열이 $$\infty$$로 수렴한다는 것이 그 점열이 임의의 유한집합을 결국 벗어난다는 것과 같음을 뜻한다.

이 공간은 실수 안의 익숙한 집합으로 실현된다. 함수

$$f:\mathbb{N}^+\to\mathbb{R},\qquad f(n)=\frac1n\quad(n\in\mathbb{N}),\qquad f(\infty)=0$$

을 생각하면, $$f$$는 $$\mathbb{N}^+$$과 $$\{0\}\cup\{1/n\mid n\geq 1\}$$ 사이의 전단사이다. 각 $$n\in\mathbb{N}$$은 $$\mathbb{N}^+$$에서 고립점이고 그 상 $$1/n$$도 $$\{0\}\cup\{1/n\}$$에서 고립점이며, $$\infty$$의 cofinite 근방이 $$0$$의 근방으로 옮겨지므로 $$f$$는 연속이다. 정의역이 compact이고 공역이 Hausdorff이므로 [§옹골공간, ⁋명제 9](/ko/math/topology/compact_spaces#prop9)에 의하여 $$f$$는 homeomorphism이다. 즉 $$\mathbb{N}^+$$은 하나의 극한점을 지닌 수렴하는 점열과 위상동형이다.
:::

## 완전정칙성

일점 옹골화는 존재론적 도구에 그치지 않고 LCH space의 내적 성질을 규명하는 데에도 쓰인다. Compact Hausdorff space는 normal이므로 ([§옹골공간, ⁋명제 7](/ko/math/topology/compact_spaces#prop7)) Urysohn 보조정리를 통해 풍부한 연속함수를 지니는데, 이 성질이 열린 부분공간을 거쳐 LCH space로 유전됨을 보인다.

::: 따름정리 14
임의의 LCH space는 completely regular이다. 따라서 임의의 LCH space는 Tychonoff space이다. ([§하우스도르프 공간, ⁋정의 3](/ko/math/topology/Hausdorff_spaces#def3))
:::
::: 증명
먼저 임의의 compact Hausdorff space $$Y$$가 completely regular임을 보인다. 점 $$p\in Y$$와 이를 포함하지 않는 닫힌집합 $$C\subseteq Y$$가 주어졌다 하자. $$Y$$는 Hausdorff이므로 $$T_1$$이고 따라서 $$\{p\}$$는 닫힌집합이며, $$\{p\}$$와 $$C$$는 서로소인 두 닫힌집합이다. $$Y$$는 normal이므로 ([§옹골공간, ⁋명제 7](/ko/math/topology/compact_spaces#prop7)) Urysohn 보조정리에 의하여 연속함수 $$g:Y\to[0,1]$$이 존재하여 $$\{p\}$$에서 $$0$$, $$C$$에서 $$1$$의 값을 갖는다. ([§Urysohn 보조정리와 Tietze 확장정리, ⁋정리 2](/ko/math/topology/urysohn_and_tietze#thm2)) 이는 곧 $$p$$와 $$C$$가 연속함수로 분리가능함을 뜻하므로 $$Y$$는 completely regular이다.

이제 $$X$$가 LCH라 하자. [정리 8](#thm8)과 [정리 9](#thm9)에 의하여 $$X^+$$는 compact Hausdorff space이므로 위에서 본 대로 completely regular이다. $$X$$는 [명제 7](#prop7)에 의해 $$X^+$$의 부분공간이다. 완전정칙성은 부분공간으로 유전됨을 보이자. $$x\in X$$와 이를 포함하지 않는 $$X$$의 닫힌집합 $$C$$가 주어지면, 부분공간의 닫힌집합의 성질에 의해 $$X^+$$의 닫힌집합 $$C'$$이 존재하여 $$C=C'\cap X$$이다. $$x\in X$$이고 $$x\notin C$$이므로 $$x\notin C'$$이며, $$X^+$$가 completely regular이므로 연속함수 $$g:X^+\to[0,1]$$이 존재하여 $$g(x)=0$$이고 $$C'$$에서 $$1$$의 값을 갖는다. $$g$$를 $$X$$로 제한한 $$g\vert_X$$는 연속함수로서 $$x$$와 $$C\subseteq C'$$을 분리하므로 $$X$$는 completely regular이다. 끝으로 $$X$$는 Hausdorff이므로 $$T_0$$이고, 따라서 $$X$$는 Tychonoff space이다.
:::

[따름정리 14](#cor14)는 LCH space 위에서 서로 다른 점을 가르거나 점과 닫힌집합을 가르는 연속함수를 언제나 얻을 수 있음을 보장한다. 이는 국소적 옹골공간이 해석학적 대상으로서 얼마나 잘 행동하는지를 말해 주는 기본적인 사실이며, 국소적으로 정의된 자료를 연속함수의 도움으로 전역적으로 이어 붙이는 여러 구성의 출발점이 된다.

---

**참고문헌**

**[Mun]** J. R. Munkres, *Topology*, 2nd ed., Prentice Hall, 2000.

**[Wil]** S. Willard, *General Topology*, Addison-Wesley, 1970.

**[Kel]** J. L. Kelley, *General Topology*, Springer, 1975.
