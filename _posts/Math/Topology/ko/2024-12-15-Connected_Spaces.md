---
title: "연결공간"
description: "위상수학에서 연결공간의 정의와 성질을 다룬다. 연속함수에 의해 연결성이 보존되고, 교차하는 연결집합들의 합집합도 연결임을 증명한다."
excerpt: "Connected space와 path-connected, connected component"

categories: [Math / Topology]
permalink: /ko/math/topology/connected_spaces
sidebar: 
    nav: "topology-ko"

date: 2024-12-15
weight: 19

---

이제 우리는 위상수학에서 중요한 개념 중 하나인 연결성에 대해 살펴본다.

::: 정의 1
위상공간 $X$가 *connected space<sub>연결공간</sub>*라는 것은 $X$가 두 개의 서로소인 비어있지 않은 열린집합의 합집합으로 나타날 수 없는 것이다. 더 일반적으로, $X$의 부분집합 $A$가 connected라는 것은 $A$에 subspace topology를 준 것이 connected인 것이다.
:::

즉 어떤 위상공간 $X$가 disconnected라는 것은 두 개의 서로소인 비어있지 않은 열린집합 $U,V$가 존재하여 $X=U\cup V$로 나타나는 것이다. 이 경우 $U$와 $V$는 서로의 여집합이므로 이들은 모두 열린집합인 동시에 닫힌집합이고, 따라서 위의 조건에서 열린집합을 닫힌집합으로 바꾸어 적어도 같은 개념을 얻는다는 것을 안다. 한편 부분집합 $A\subseteq X$의 경우, subspace topology의 정의를 풀어쓰면 $A$가 disconnected라는 것은 $X$의 두 열린집합 $U,V$가 존재하여

$$A=(U\cap A)\cup (V\cap A),\qquad U\cap V\cap A=\emptyset$$

이며 $U\cap A$와 $V\cap A$가 모두 비어있지 않은 것이다.

::: 명제 2
Connected set $A\subseteq X$에 대해서, $A\subseteq B \subseteq \cl(A)$를 만족하는 $B$는 connected이다.
:::
::: 증명
주어진 상황에서, 

$$\cl_B(A)=B\cap \cl_X(A)=B$$

이므로 $A$는 $B$의 dense subset이다. ([§부분공간, ⁋명제 5](/ko/math/topology/subspaces#prop5)) 이제 결론에 반하여 $B$의 서로소인 두 열린집합 $U,V$가 존재하여 $U\cup V=B$라 하자. 그럼 $A$는 $B$의 dense subset이므로 $U\cap A, V\cap A$는 모두 공집합이 아니며 $U\cap V\cap A=\emptyset$이다. 이는 $A$가 connected라는 가정에 모순이다. 
:::

또, 직관적으로 다음 명제 또한 납득할 만하다.

::: 명제 3
Connected set들의 family $(A_i)$에 대하여, 만일 임의의 $i,j$마다 $A_i\cap A_j\neq\emptyset$이 성립한다면 $A=\bigcup A_i$도 connected이다. 
:::
::: 증명
결론에 반하여 두 열린집합 $U,V$가 존재하여 두 조건

$$A=(U\cap A)\cup (V\cap A),\qquad U\cap V\cap A=\emptyset$$

이 성립한다 가정하자. 우선 임의의 $i$에 대하여, $A_i$는 connected이므로 두 식 $A_i\subseteq U$ 혹은 $A_i\subseteq V$ 중 정확히 하나만이 성립해야 한다. 한편, 만일 $A_i\subseteq U$이고 $A_j\subseteq V$라면

$$A_i\cap A_j\subseteq (U\cap A)\cap (V\cap A)=U\cap V\cap A=\emptyset$$

가 되어 모순이므로 $A_i$들은 모두 동시에 $U$에 속하거나 동시에 $V$에 속해야 한다. 그럼 $U\cap A=\emptyset$이거나 $V\cap A=\emptyset$이어야 한다. 
:::

## 연결집합의 성질들

연결성은 연속함수에 의해 보존되는 성질이다.

::: 명제 4
임의의 연속함수 $f:X \rightarrow Y$와 $X$의 connected subset $A\subseteq X$에 대하여, $f(A)$도 connected이다. 
:::
::: 증명
결론에 반하여 $f(A)$가 connected가 아니라 하고, 

$$f(A)=(V_1\cap f(A))\cup (V_2\cap f(A)), \qquad V_1\cap V_2\cap f(A)=\emptyset$$

이도록 하는 $Y$의 열린집합 $V_1,V_2$를 택하자. 그럼 $f^{-1}(V_1),f^{-1}(V_2)$는 $X$의 열린집합이며, 

$$A=(A\cap f^{-1}(V_1))\cup (A\cap f^{-1}(V_2)),\qquad f^{-1}(V_1)\cap f^{-1}(V_2)\cap A=\emptyset$$

이다. 이제 $A$가 connected라는 가정으로부터 $V_1\cap f(A)=\emptyset$이거나 $V_2\cap f(A)=\emptyset$이어야 한다는 것을 안다. 
:::

이로부터 다음 따름정리를 얻는다.

::: 따름정리 5
Connected space의 quotient space는 connected이다.
:::
::: 증명
Connected space $X$ 위에 동치관계 $R$이 주어졌다 하자. Canonical projection $p:X \rightarrow X/R$은 연속인 전사함수이다. ([§몫공간, ⁋정의 3](/ko/math/topology/quotient_spaces#def3)) 따라서 [명제 4](#prop4)에 의하여 $X/R=p(X)$ 또한 connected이다.
:::

또, 다음이 성립한다.

::: 명제 6
Connected space들의 product는 connected이다. 거꾸로, 비어있지 않은 product가 connected라면 각각의 성분들도 connected이다.
:::
::: 증명
뒤쪽 방향은 product가 비어있지 않다면 $\pr_i$가 전사함수이므로, $\pr_i$에 대해 [명제 4](#prop4)를 사용하면 된다. 

따라서 각각의 $X_i$들이 connected라 하고, 결론에 반하여 $X=\prod X_i$가 connected가 아니라 하자. $X=U\cup V$이고 $U\cap V=\emptyset$, $U,V\neq\emptyset$이라 하면 

$$f(x)=\begin{cases}1&\text{if $x\in U$}\\0&\text{if $x\in V$}\end{cases}$$

으로 정의한 함수 $f:X \rightarrow \{0,1\}$은 연속이다. (여기서 $\{0,1\}$은 discrete topology가 주어진 공간이다.) 

이제 원소 $a=(a_i)\in X$를 고정하고, $\iota_i: X_i \rightarrow X$를 $i$번째 성분만 $x$이고, 나머지 성분은 $a$로부터 받아오는 함수로 정하자. 이 때 $a$ 자리에는 $X$의 임의의 점을 base point로 두어 같은 방식으로 $\iota_i$를 정의할 수 있다. 그럼 $\iota_i$는 각 성분함수가 항등함수이거나 상수함수이므로 연속이고 ([§곱공간, ⁋명제 2](/ko/math/topology/product_spaces#prop2)), $f\circ\iota_i$는 $X_i$에서 $\{0,1\}$로의 연속함수이며, $X_i$가 connected라는 가정으로부터 $f\circ\iota_i$는 상수함수여야 하는 것을 안다. 따라서 귀납법에 의하여, 유한 개를 제외한 성분이 모두 $a$와 같은 $X$의 점 $x$들은 $f(x)=f(a)$를 만족해야 한다는 것을 안다. 이러한 점들은 $X$의 dense subset이므로, $f$는 $X$ 전체에서 상수함수여야 하고 이는 모순이다. 
:::

## 연결성분

한편 고정된 $x\in X$에 대하여, $x$를 포함하는 connected set들의 모임은 [명제 3](#prop3)의 전제조건을 만족하고 따라서 $x$를 포함하는 가장 큰 connected set이 말이 된다.

::: 정의 7
$X$의 점 $x\in X$를 포함하는 *connected component<sub>연결성분</sub>*는 $x$를 포함하는 $X$의 connected subset 중 가장 큰 것이다. 만일 $X$의 임의의 점 $x$를 포함하는 connected component가 항상 $\{x\}$ 자기자신이라면 $X$를 *totally disconnected<sub>전비연결</sub>*라 부른다.
:::

정의에 의하여, 만일 $X$가 connected라면 $X$는 유일한 connected component를 갖는다. 더 일반적으로 임의의 $X$는 connected component들의 합집합

$$X=\bigcup_{i\in I} U_i$$

으로 나타낼 수 있다. 한편 [명제 2](#prop2)에 의하여 각각의 $U_i$들은 반드시 닫힌집합이어야 한다. 만일 $I$가 유한집합이라면, $U_i$들은 모두 열린집합인 동시에 닫힌집합이어야 함을 안다. 물론 이는 무한히 많은 connected component에 대해서는 적용되지 않지만, 임의의 위상공간의 clopen set은 반드시 connected component들의 union으로 나타나야한다. 만일 그렇지 않고 어떠한 connected component $C$가 clopen set $A$와 만나면서 동시에 $A$의 여집합과도 만난다면 $C\cap A$와 $C\setminus A$가 $C$를 나누는 두 열린집합이 될 것이기 때문이다. 

뿐만 아니라 다음이 성립한다.

::: 명제 8
위상공간 $X$ 위에 동치관계 $\sim$을

$$x\sim y\iff \text{$x$ and $y$ lie in the same component}$$

로 정의하자. 그럼 $X/{\sim}$은 totally disconnected이다.
:::
::: 증명
$p:X \rightarrow X/{\sim}$을 canonical projection이라 하자. Quotient space의 정의에 의하여 $X/{\sim}$의 부분집합 $S$가 열린집합인 것은 $p^{-1}(S)$가 $X$의 열린집합인 것과 동치이다. ([§몫공간, ⁋정의 3](/ko/math/topology/quotient_spaces#def3)) 여집합을 취하면, $X/{\sim}$의 부분집합 $S$가 닫힌집합인 것 또한 $p^{-1}(S)$가 $X$의 닫힌집합인 것과 동치임을 안다.

이제 $X/{\sim}$의 임의의 connected component $C$가 한점집합임을 보이면 된다. 우선 $p^{-1}(C)$가 connected임을 보이자. [명제 2](#prop2)에 의하여 connected component는 언제나 닫힌집합이므로 $C$는 $X/{\sim}$의 닫힌집합이고, 위의 관찰에 의하여 $p^{-1}(C)$는 $X$의 닫힌집합이다. 결론에 반하여 $p^{-1}(C)$가 서로소인 비어있지 않은 두 닫힌집합 $Z_1,Z_2$의 합집합으로 나타난다 하자. $p^{-1}(C)$가 $X$의 닫힌집합이므로 $Z_1,Z_2$ 또한 $X$의 닫힌집합이다. ([§부분공간, ⁋보조정리 3](/ko/math/topology/subspaces#lem3)) 한편 임의의 $c\in C$에 대하여 $p^{-1}(c)$는 $X$의 connected component이고, 두 집합 $Z_1\cap p^{-1}(c)$와 $Z_2\cap p^{-1}(c)$는 connected set $p^{-1}(c)$를 서로소인 두 닫힌집합으로 나누므로 이 중 하나는 반드시 공집합이어야 한다. 즉 각각의 $p^{-1}(c)$는 $Z_1$과 $Z_2$ 중 정확히 하나에 통째로 포함된다. 그럼 $p^{-1}(c)\subseteq Z_1$이도록 하는 $c$들의 모임을 $C_1$, $p^{-1}(c)\subseteq Z_2$이도록 하는 $c$들의 모임을 $C_2$라 할 때 $C_1,C_2$는 서로소이고 $C=C_1\cup C_2$이며 $p^{-1}(C_i)=Z_i$이다. 첫 문단의 관찰에 의하여 $C_1,C_2$는 모두 $X/{\sim}$의 비어있지 않은 닫힌집합이고, 이는 $C$가 connected라는 것에 모순이다.

따라서 $p^{-1}(C)$는 connected이며, $p$가 전사함수이므로 비어있지 않다. 한 점 $x\in p^{-1}(C)$를 택하고 $x$의 connected component를 $K$라 하면, $p^{-1}(C)$는 $x$를 포함하는 connected set이므로 $p^{-1}(C)\subseteq K$이다. 거꾸로 $p^{-1}(C)$는 $\sim$의 equivalence class들의 합집합이고 $x$의 equivalence class가 곧 $K$이므로 $K\subseteq p^{-1}(C)$이다. 그러므로 $p^{-1}(C)=K$이고, $p$가 전사함수이므로 $C=p(p^{-1}(C))=p(K)$는 한 점이다.
:::

## 국소연결공간

지금까지 살펴본 connectedness는 공간 전체에 대한 성질이었으나, 많은 경우 우리는 이러한 성질이 각 점 주위에서도 성립하는지에 관심이 있다.

::: 정의 9
위상공간 $X$가 점 $x\in X$에서 *locally connected<sub>국소연결</sub>*이라는 것은 $x$의 임의의 근방 $U$가 주어질 때마다, $U$에 속하는 $x$의 connected neighborhood가 존재하는 것이다. 모든 점에서 locally connected인 공간을 간단히 locally connected space라 부른다. 
:::

그럼 다음이 성립한다.

::: 명제 10
$X$가 locally connected인 것과, $X$의 각 열린집합의 component가 항상 open인 것이 동치이다. 
:::
::: 증명
우선 $X$가 locally connected라 하자. 열린집합 $U$와 $U$의 connected component $C$가 주어졌다 하고, $x\in C$를 택하자. $U$는 $x$의 근방이므로, 가정에 의하여 $U$에 속하는 $x$의 connected neighborhood $N$이 존재한다. 그럼 $N$은 $x$를 포함하는 $U$의 connected subset이므로 $N\subseteq C$이고, $N$이 $x$의 근방이므로 $C$ 또한 $x$의 근방이다. $x$는 $C$의 임의의 점이었으므로, [§열린집합, ⁋명제 5](/ko/math/topology/open_sets#prop5)에 의하여 $C$는 열린집합이다.

거꾸로 $X$의 각 열린집합의 component가 항상 열린집합이라 하자. 점 $x\in X$와 $x$의 근방 $U$가 주어지면, 근방의 정의에 의하여 $x$의 열린근방 $V$가 존재하여 $V\subseteq U$이다. 이제 $V$의 connected component 중 $x$를 포함하는 것을 $C$라 하면, 가정에 의하여 $C$는 열린집합이고, 따라서 $C$는 $U$에 속하는 $x$의 connected neighborhood이다. 그러므로 $X$는 locally connected이다.
:::

특히 $X$가 locally connected라면 $X$ 자신의 connected component들은 모두 열린집합이다. 각 component의 여집합은 나머지 component들의 합집합이므로, 이 경우 connected component들은 모두 열린집합인 동시에 닫힌집합이 된다. 이는 일반적인 위상공간의 connected component가 닫힌집합이기만 한 것과 대비되는 결과이다.

## 경로연결공간

Connectedness는 공간을 두 조각으로 가르는 분할이 존재하지 않는다는 소극적인 조건으로 정의되었다. 한편 공간이 한 덩어리라는 직관을 적극적인 방식으로 옮길 수도 있는데, 이는 공간의 임의의 두 점을 공간 안에서 연속적으로 잇는 것이 가능해야 한다는 조건이다. 이를 정식화하면 다음의 정의를 얻는다.

::: 정의 11
위상공간 $X$에 대하여, 연속함수 $\gamma:[0,1]\rightarrow X$를 $\gamma(0)$에서 $\gamma(1)$로 가는 $X$의 *path<sub>경로</sub>*라 부른다. $X$가 *path-connected<sub>경로연결</sub>*라는 것은 임의의 두 점 $x,y\in X$에 대하여 $x$에서 $y$로 가는 path가 존재하는 것이다.
:::

[정의 1](#def1)에서와 마찬가지로 부분집합 $A\subseteq X$가 path-connected라는 것은 $A$에 subspace topology를 준 것이 path-connected인 것이며, 이는 곧 $A$의 임의의 두 점을 image가 $A$에 포함되는 path로 이을 수 있다는 것이다. 가령 $\mathbb{R}^n$의 부분집합 $A$가 임의의 두 점 $x,y\in A$에 대하여 이들을 잇는 선분을 통째로 포함한다면 $A$는 path-connected인데, 선분의 parametrization $\gamma(t)=(1-t)x+ty$는 각 성분함수 $t\mapsto(1-t)x_i+ty_i$가 연속이므로 연속함수이고 ([§곱공간, ⁋명제 2](/ko/math/topology/product_spaces#prop2)), 공역을 $A$로 제한하여도 연속이기 때문이다. ([§부분공간, §§부분공간과 연속함수](/ko/math/topology/subspaces#부분공간과-연속함수)) 특히 $\mathbb{R}^n$ 자신은 path-connected이다.

Path-connectedness와 connectedness 사이의 관계는 path의 정의역인 닫힌구간 $[0,1]$을 거쳐 성립한다. 우선 닫힌구간이 connected임을 보이는데, 이는 비어있지 않고 bounded above인 $\mathbb{R}$의 부분집합이 언제나 supremum을 갖는다는 실수의 완비성에 기대는 결과이다. ([\[집합론\] §순서집합의 원소들, ⁋정의 6](/ko/math/set_theory/elements_in_ordered_set#def6))

::: 보조정리 12
임의의 실수 $a\leq b$에 대하여, 닫힌구간 $[a,b]$는 $\mathbb{R}$의 connected subset이다.
:::
::: 증명
결론에 반하여 $\mathbb{R}$의 두 열린집합 $U,V$가 존재하여

$$[a,b]=(U\cap[a,b])\cup(V\cap[a,b]),\qquad U\cap V\cap[a,b]=\emptyset$$

이며 $U\cap[a,b]$와 $V\cap[a,b]$가 모두 비어있지 않다고 하자. 일반성을 잃지 않고 $b\in V$라 하자. 집합 $U\cap[a,b]$는 비어있지 않고 $b$가 upper bound이므로, 실수의 완비성에 의하여 supremum $s=\sup(U\cap[a,b])$가 존재하며 $a\leq s\leq b$이다.

우선 $s\in U$라 하자. $b\in V$이고 $U\cap V\cap[a,b]=\emptyset$이므로 $s\neq b$, 즉 $s<b$이다. $U$가 열린집합이므로 적당한 $\epsilon>0$에 대하여 열린구간 $(s-\epsilon,s+\epsilon)$은 $U$에 포함된다. 그럼 $s<t<\min(s+\epsilon,b)$인 $t$를 택하면 $t\in U\cap[a,b]$이므로, $s$가 $U\cap[a,b]$의 upper bound라는 것에 모순이다.

이제 $s\in V$라 하자. 마찬가지로 적당한 $\epsilon>0$에 대하여 $(s-\epsilon,s+\epsilon)\subseteq V$이다. 임의의 $t\in U\cap[a,b]$는 $t\leq s$를 만족하며, $U\cap V\cap[a,b]=\emptyset$이므로 $t\in(s-\epsilon,s]$일 수는 없고, 따라서 $t\leq s-\epsilon$이다. 즉 $s-\epsilon$ 또한 $U\cap[a,b]$의 upper bound이고, 이는 $s$가 least upper bound라는 것에 모순이다.

$s\in[a,b]\subseteq U\cup V$이므로 두 경우 중 하나는 반드시 일어나고, 어느 쪽이든 모순이므로 $[a,b]$는 connected이다.
:::

그럼 위의 직관대로, path-connectedness가 connectedness보다 강한 조건이라는 것을 보일 수 있다.

::: 명제 13
Path-connected space는 connected이다.
:::
::: 증명
결론에 반하여 path-connected space $X$가 connected가 아니라 하고, 서로소인 비어있지 않은 두 열린집합 $U,V$에 대하여 $X=U\cup V$라 하자. 각각 $x\in U$, $y\in V$를 택하면 가정에 의하여 $x$에서 $y$로 가는 path $\gamma:[0,1]\rightarrow X$가 존재한다. [보조정리 12](#lem12)와 [명제 4](#prop4)에 의하여 $\gamma([0,1])$은 connected이다. 그러나 $U\cap\gamma([0,1])$과 $V\cap\gamma([0,1])$은 각각 $x$와 $y$를 포함하므로 비어있지 않고, $\gamma([0,1])\subseteq U\cup V$이며 $U\cap V\cap\gamma([0,1])=\emptyset$이므로 이는 $\gamma([0,1])$이 connected라는 것에 모순이다.
:::

특히 $\mathbb{R}^n$은 connected이다. 그러나 이 명제의 역은 성립하지 않는다. 다음 예시는 connected이지만 path-connected가 아닌 공간의 고전적인 예이다.

::: 예시 14
평면 $\mathbb{R}^2$의 두 부분집합

$$S=\{(x,\sin(1/x))\mid 0<x\leq 1\},\qquad T=S\cup(\{0\}\times[-1,1])$$

을 생각하자. 즉 $T$는 곡선 $S$에, $S$의 진동이 쌓이는 세로 선분을 붙인 것이다. $T$를 *topologist's sine curve<sub>위상수학자의 사인곡선</sub>*라 부르는데, 우리는 $T$가 connected이지만 path-connected는 아니라는 것을 보인다.

우선 $T$가 connected임을 보이자. 함수 $\phi:(0,1]\rightarrow\mathbb{R}^2$을 $\phi(x)=(x,\sin(1/x))$으로 정의하면 두 성분함수가 모두 연속이므로 $\phi$는 연속이다. ([§곱공간, ⁋명제 2](/ko/math/topology/product_spaces#prop2)) 한편 $(0,1]=\bigcup_{n\geq 1}[1/n,1]$이고, 각각의 $[1/n,1]$은 [보조정리 12](#lem12)에 의하여 connected이며 이들이 모두 $1$을 포함하므로 [명제 3](#prop3)에 의하여 $(0,1]$은 connected이다. 따라서 $S=\phi((0,1])$도 connected이다. ([명제 4](#prop4))

다음으로 $\{0\}\times[-1,1]\subseteq\cl(S)$임을 확인하자. $y\in[-1,1]$이 주어졌다 하고 $\sin\theta_0=y$인 $\theta_0\in[\pi/2,5\pi/2]$를 택하면, 각 자연수 $n$마다 $x_n=1/(\theta_0+2\pi n)$은 $(0,1]$에 속하고 $\sin(1/x_n)=\sin\theta_0=y$이므로 $(x_n,y)\in S$이다. 점 $(0,y)$의 임의의 근방은 적당한 $\epsilon>0$에 대하여 열린 공 $\{z\in\mathbb{R}^2: \lVert z-(0,y)\rVert<\epsilon\}$을 포함하는데, $(x_n,y)$와 $(0,y)$ 사이의 거리는 $x_n$이고 $n$을 충분히 크게 잡으면 $x_n<\epsilon$이므로 이 근방은 반드시 $S$와 만난다. 따라서 $(0,y)\in\cl(S)$이다. ([§집합의 내부, 폐포, 경계, ⁋명제 6](/ko/math/topology/other_concepts#prop6)) 그럼 $S\subseteq T\subseteq\cl(S)$이므로, [명제 2](#prop2)에 의하여 $T$는 connected이다.

이제 $T$가 path-connected가 아님을 보이자. 결론에 반하여 $\gamma(0)\in\{0\}\times[-1,1]$이고 $\gamma(1)\in S$인 path $\gamma:[0,1]\rightarrow T$가 존재한다고 하자. $\gamma$의 두 성분함수를 $u=\pr_1\circ\gamma$, $v=\pr_2\circ\gamma$라 하면 이들은 연속함수의 합성이므로 연속이다. $T$의 점 가운데 첫째 성분이 양수인 것은 정확히 $S$의 점들이므로, $u(t)>0$인 $t$에서는 $v(t)=\sin(1/u(t))$이다.

집합 $P=\{t\in[0,1]\mid u(t)>0\}$은 $1$을 포함하므로 비어있지 않고 $0$이 lower bound이므로, 실수의 완비성에 의하여 infimum $t_0=\inf P$가 존재한다. 우선 $u(t_0)=0$임을 확인하자. $\gamma(0)$의 첫째 성분이 $0$이므로 만일 $t_0=0$이라면 곧바로 $u(t_0)=0$이다. $t_0>0$인 경우, 만일 $u(t_0)>0$이라면 $u$의 연속성에 의하여 $u^{-1}((0,\infty))$이 $t_0$의 열린근방을 포함하므로 $t_0$보다 작은 점 $t$에서도 $u(t)>0$이 되어, $t_0$가 $P$의 lower bound라는 것에 모순이다. 그러므로 $u(t_0)=0$이고 $\gamma(t_0)\in\{0\}\times[-1,1]$이다.

$\gamma$가 $t_0$에서 연속이므로, 반지름 $1/2$의 열린 공 $B=\{z\in\mathbb{R}^2:\lVert z-\gamma(t_0)\rVert<1/2\}$에 대하여 $\gamma^{-1}(B\cap T)$는 $t_0$의 열린근방을 포함하고, 따라서 적당한 $\delta>0$이 존재하여 $t\in[t_0,t_0+\delta)$이면 $\lVert\gamma(t)-\gamma(t_0)\rVert<1/2$이다. 한편 $t_0$가 $P$의 infimum이므로 $[t_0,t_0+\delta)$ 안에 $P$의 원소 $t_1$이 존재하고, $u(t_0)=0$이므로 $t_0<t_1$이다. 이제 $a=u(t_1)>0$이라 적자. [보조정리 12](#lem12)와 [명제 4](#prop4)에 의하여 $u([t_0,t_1])$는 connected이다. 만일 $0<c<a$인 어떤 실수 $c$가 $u([t_0,t_1])$에 속하지 않는다면, 두 열린집합 $(-\infty,c)$와 $(c,\infty)$는 $u([t_0,t_1])$를 분할하며 각각 $u(t_0)=0$과 $u(t_1)=a$를 포함하여 비어있지 않으므로 모순이다. 따라서 $[0,a]\subseteq u([t_0,t_1])$이다.

이제 자연수 $k$를 충분히 크게 잡으면 두 수 $2/((4k+1)\pi)$와 $2/((4k-1)\pi)$는 모두 $(0,a]$에 속하고, 따라서 $u(t')=2/((4k+1)\pi)$, $u(t'')=2/((4k-1)\pi)$이도록 하는 $t',t''\in[t_0,t_1]$이 존재한다. 첫째 성분이 양수이므로 $\gamma(t')$와 $\gamma(t'')$는 $S$의 점이고, 둘째 성분은 각각

$$v(t')=\sin((4k+1)\pi/2)=1,\qquad v(t'')=\sin((4k-1)\pi/2)=-1$$

이다. 그러나 $t',t''\in[t_0,t_0+\delta)$이므로 삼각부등식에 의하여

$$\lVert\gamma(t')-\gamma(t'')\rVert\leq\lVert\gamma(t')-\gamma(t_0)\rVert+\lVert\gamma(t_0)-\gamma(t'')\rVert<1$$

인 반면, 두 점의 둘째 성분의 차만 보아도 $\lVert\gamma(t')-\gamma(t'')\rVert\geq 2$이다. 이는 모순이므로, $T$는 connected이지만 path-connected는 아니다.
:::

---

**참고문헌**

**[Bou]** N. Bourbaki, <i>General Topology</i>. Elements of mathematics. Springer, 1995.
