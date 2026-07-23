---
title: "뇌터 정규화"
description: "뇌터 정규화 보조정리를 다루며, 가환대수에서 유한 생성 대수의 다항식환 위 구조를 보장하는 핵심 정리와 그 증명을 살펴본다."
excerpt: "유한생성 algebra의 Noether normalization 정리와 응용"

categories: [Math / Commutative Algebra]
permalink: /ko/math/commutative_algebra/noether_normalization
sidebar: 
    nav: "commutative_algebra-ko"

date: 2025-03-23
weight: 21
published: false
drift_needed: true

---

## 뇌터 정규화

이번 글의 목표는 다음의 정리를 보이고, 이에 따른 결과들을 살펴보는 것이다. 

::: 정리 1 (Noether normalization lemma)
Finitely generated $d$-dimensional $\mathbb{K}$-algebra $A$에 대하여, 다음의 부등식

$$d_1>d_2>\cdots>d_m>0$$

을 만족하는 자연수들과, $\dim \mathfrak{a}_i=d_i$를 만족하는 $A$의 ideal들의 descending chain

$$\mathfrak{a}_1\subset \mathfrak{a}_2\subset\cdots\subset \mathfrak{a}_m$$

이 주어졌다 하자. 그럼 $A$의 적당한 subring $B\cong \mathbb{K}[\x_1,\ldots, \x_d]$가 존재하여, $A$가 $B$-module로서 finitely generated이고 다음 식

$$\mathfrak{a}_i\cap B=(\x_{d_i+1},\ldots, \x_d)\qquad\text{for $i=1,\ldots, m$}$$

이 성립하도록 할 수 있다. 
:::

이는 다음의 보조정리를 사용하여 보일 수 있으며, 이에 대한 증명은 생략하기로 한다. 

::: 보조정리 2
Field $\mathbb{K}$와, non-constant polynomial $f\in B=\mathbb{K}[\x_1,\ldots, \x_r]$이 주어졌다 하자. 그럼 적당한 원소들 $\x_1',\ldots, \x_{r-1}'\in B$가 존재하여, 원소들 $\x_1',\ldots, \x_{r-1}', f$로 생성된 $B$의 $\mathbb{K}$-subalgebra를 $B'$라 했을 때 $B$가 finitely generated $B'$-module이도록 할 수 있다. 뿐만 아니라, 이들 원소들은 다음과 같이 택할 수 있다.

1. 충분히 큰 정수 $e$에 대하여, $\x_i'=\x_i-\x_r^{e}$으로 택할 수 있다. 
2. 만일 $\mathbb{K}$가 infinite field라면, 적당한 $a_i\in \mathbb{K}$들에 대해 $\x_i'=\x_i-a_i\x_r$로 택할 수 있다. 
:::

그럼 [정리 1](#thm1)의 증명은 다음과 같다. 

::: 증명 (정리 1)
우선 $A$가 finitely generated $\mathbb{K}$-algebra이므로 $A=\mathbb{K}[\y_1,\ldots, \y_r]/\mathfrak{a}$라 적을 수 있다. 그럼 주어진 조건을 만족하는 ideal들의 chain이 주어졌다 하면, 이들의 $\mathbb{K}[\y_1,\ldots, \y_r]$에서의 preimage들로 이루어진 chain

$$\tilde{\mathfrak{a}}_1\subset \tilde{\mathfrak{a}}_2\subset\cdots\subset  \tilde{\mathfrak{a}}_m$$

를 생각한 후 $\mathfrak{a}_0=\mathfrak{a}$를 끼워넣어 이를 $\mathbb{K}[\y_1,\ldots, \y_r]$에서의 ideal들의 descending chain

$$\mathfrak{a}\subset \tilde{\mathfrak{a}}_1\subset \tilde{\mathfrak{a}}_2\subset\cdots\subset  \tilde{\mathfrak{a}}_m$$

으로 볼 수 있으므로 주어진 주장을 polynomial ring $A=\mathbb{K}[\y_1,\ldots, \y_r]$에 대해서만 보이면 충분하다. 이 경우, [§매개계, ⁋따름정리 11](/ko/math/commutative_algebra/system_of_parameters#cor11)에 의하여 $r=d$여야 한다. 

이제 정리의 원소들 $\x_i$들을 만들기 위해 우리는 우선 $\x_i'=\y_i$로 두고, 이들을 바꿔가며 주어진 조건을 만족하는 $\x_d$들을 찾을 것이다. 이를 위해 다음의 두 조건

1. $A$는 finitely generated $B_e=\mathbb{K}[\x_1',\ldots, \x_e',\x_{e+1},\ldots, \x_d]$-module이다. 
2. 각각의 $i$에 대하여 $\mathfrak{a}_i\cap B_e\supset(\x_m,\ldots, \x_d)$이 성립한다. 여기서 $m=\max(d_i+1, e+1)$이다. 

을 만족하는 원소들 $\x_1',\ldots, \x_e', \x_{e+1},\ldots, \x_d$들이 주어졌다 하고, 이로부터 새로운 원소들 $\x_1',\ldots, \x_{e-1}'$ 그리고 $\x_e$를 찾아 위의 조건이 그대로 유지되도록 할 수 있다는 것을 보인다. 그럼 이 과정을 반복하여 마지막으로 얻어진 $B=B_{d_m}$이 원하는 조건을 만족한다는 것은 둘째 조건의 포함관계가 사실 등식이라는 것을 보이면 자명하며, 이는 양 변에 있는 $B$의 두 ideal들의 차원을 생각하면 당연하다. 

이제 이 귀납법을 완성하기 위해, $d\geq e>d_m$을 만족하는 $e$에 대하여, 위의 두 조건을 만족하는 $\x_1',\ldots, \x_e', \x_{e+1},\ldots, \x_d$들이 주어졌다 하고, $i$가 $e>d_i$를 만족하는 것들 중 가장 작은 index라 가정하자. 그럼

$$\mathfrak{a}_i\cap \mathbb{K}[\x_1',\ldots, \x_e']\neq 0$$

이다. 만일 이 교집합이 $0$이라 가정하면, 둘째 조건에 의해 

$$\mathfrak{a}_i\cap B_e\supseteq (\x_{e+1},\ldots, \x_d)$$

이 성립하는데, 좌변의 ideal은 $d_i$-차원이고, 우변의 ideal의 차원은 $e$가 되어 모순이기 때문이다. 이제 $\x_e$를 위의 교집합에 속하는 아무 nonzero polynomial로 잡은 후, [보조정리 2](#lem2)를 사용하여 새로운 원소들 $\x_1',\ldots, \x_{e-1}'$들도 새로운 원소로 교체해주면 된다.
:::

## 결과들

[정리 1](#thm1)은 다음의 결과를 준다.

::: 정리 3
Ring $A$가 integral domain이고, finitely generated $\mathbb{K}$-algebra라 하자. 그럼 $\dim A=\trdeg_\mathbb{K}\Frac(A)$이다.
:::

[정리 3](#thm3)은 quotient를 취한 상황으로 자연스럽게 일반화되어, 다음의 *차원 공식<sub>dimension formula</sub>*을 준다.

::: 정리 4
Finitely generated $\mathbb{K}$-algebra domain $A$와 그 prime ideal $\mathfrak{p}$에 대하여 다음이 성립한다.

$$\dim A/\mathfrak{p}+\operatorname{ht}\mathfrak{p}=\dim A$$
:::
::: 증명
부등식 $\dim A/\mathfrak{p}+\operatorname{ht}\mathfrak{p}\leq\dim A$는 임의의 ring에 대하여 성립하므로 ([§차원, ⁋정의 2](/ko/math/commutative_algebra/Krull_dimension#def2)), 반대 부등식만 보이면 된다. $n=\dim A$, $d=\dim A/\mathfrak{p}=\dim\mathfrak{p}$라 두자. [정리 1](#thm1)을 $A$의 ideal $\mathfrak{a}_1=\mathfrak{p}$ 하나로 이루어진 chain에 적용하면, $A$의 subring $B\cong\mathbb{K}[\x_1,\ldots, \x_n]$이 존재하여 $A$가 finitely generated $B$-module이고 $\mathfrak{p}\cap B=(\x_{d+1},\ldots, \x_n)$을 만족한다. 그럼 $B\hookrightarrow A$가 integral extension이므로 [\[가환대수학\] §정수적 확장과 아이디얼, ⁋명제 1](/ko/math/commutative_algebra/lying_over_and_going_up#prop1)과 [따름정리 4](/ko/math/commutative_algebra/lying_over_and_going_up#cor4)에 의하여 $\operatorname{ht}_A\mathfrak{p}=\operatorname{ht}_B(\mathfrak{p}\cap B)$이다.

이제 polynomial ring $B=\mathbb{K}[\x_1,\ldots, \x_n]$에서 ideal $(\x_{d+1},\ldots, \x_n)$의 height를 계산하자. chain

$$(0)\subset(\x_n)\subset(\x_{n-1},\x_n)\subset\cdots\subset(\x_{d+1},\ldots, \x_n)$$

은 이 ideal의 height가 적어도 $n-d$임을 보여주며, 몫환 $B/(\x_{d+1},\ldots, \x_n)\cong\mathbb{K}[\x_1,\ldots, \x_d]$가 $d$차원이므로 ([§매개계, ⁋따름정리 11](/ko/math/commutative_algebra/system_of_parameters#cor11)) 부등식 $\dim+\operatorname{ht}\leq n$으로 height는 기껏해야 $n-d$이다. 따라서 $\operatorname{ht}_B(\x_{d+1},\ldots, \x_n)=n-d$이며, 결국 $\operatorname{ht}\mathfrak{p}=n-d=\dim A-\dim A/\mathfrak{p}$이다.
:::

## 제네릭 자유성

지금까지는 base가 field인 상황을 다루었다. 이를 Noetherian integral domain $A$로 넓히면 finite type $A$-algebra $B$와 그 위의 finitely generated module $M$이 $A$-module로서 free일 이유는 없다. 그러나 $A$의 $0$이 아닌 원소 하나를 뒤집는 것만으로 언제나 free로 만들 수 있다는 것이 다음의 결과이며, localization $A_a$가 $A$와 같은 field of fractions를 가지므로 이는 free성이 generic하게 성립한다는 뜻이다.

::: 정리 5 (Grothendieck의 generic freeness)
Noetherian integral domain $A$와 finite type $A$-algebra $B$, 그리고 finitely generated $B$-module $M$이 주어졌다 하자. 그럼 $0$이 아닌 $a\in A$가 존재하여 $M_a$가 free $A_a$-module이 된다.
:::
::: 증명
$B$는 Noetherian integral domain $A$ 위의 finite type 대수이므로 [§기본 개념들, ⁋정리 12](/ko/math/commutative_algebra/basic_notions#thm12)에 의하여 Noetherian ring이다.

먼저 [§동반소아이디얼, ⁋보조정리 6](/ko/math/commutative_algebra/associated_primes#lem6)을 $B$와 $M$에 적용하는 dévissage로 문제를 줄인다. 이를 적용하면 filtration

$$0=M_0\subseteq M_1\subseteq\cdots\subseteq M_n=M,\qquad M_i/M_{i-1}\cong B/\mathfrak{q}_i$$

를 얻는다. 각 $B/\mathfrak{q}_i$에 대하여 결론이 성립한다 하고 그 원소들의 곱을 $a$라 하면, exact sequence

$$0 \longrightarrow (M_{i-1})_a \longrightarrow (M_i)_a \longrightarrow (B/\mathfrak{q}_i)_a \longrightarrow 0$$

의 오른쪽 항이 free module이므로 이 exact sequence는 split하고, $i$에 대한 귀납법으로 $(M_i)_a$가 모두 free $A_a$-module이 된다. 따라서 $M=B/\mathfrak{q}$인 경우, 즉 $B$를 $B/\mathfrak{q}$로 바꾸어 $B$가 integral domain이고 $M=B$인 경우만 보이면 충분하다.

$\varphi: A \rightarrow B$의 kernel이 $0$이 아닌 경우는 곧바로 처리된다. 이때 $0\neq a\in \ker \varphi$를 택하면 $B_a=B\otimes_AA_a$에서 $\varphi(a)=0$이면서 $a$가 unit이므로 $B_a=0$이고, 이는 rank $0$의 free module이다. 따라서 $A\subseteq B$라 가정해도 좋다.

이제 $K=\Frac(A)$라 하면 $B\otimes_AK$는 $A\setminus\{0\}$에서의 $B$의 localization이므로 $0$이 아닌 integral domain이며, $K$ 위의 finite type 대수이다. 남은 주장을 $d=\dim (B\otimes_AK)$에 대한 귀납법으로 보인다.

[정리 1](#thm1)을 ideal의 chain 없이 적용하면 algebraically independent한 원소들 $y_1,\ldots, y_d\in B\otimes_AK$가 존재하여 $B\otimes_AK$가 $K[y_1,\ldots,y_d]$ 위의 finite module이다. 각 $y_i$에 $A$의 $0$이 아닌 원소를 곱해도 대수적 독립성과 유한성은 유지되므로, 처음부터 $y_i\in B$라 가정해도 좋다.

$B$를 $A$-algebra로서 생성하는 원소를 $b_1,\ldots, b_m$이라 하면 각 $b_j$는 $K[y_1,\ldots,y_d]$ 위에서 integral하다. 이 정수 방정식들에 등장하는 계수는 유한개이므로, 그 분모를 모두 없애는 $0\neq a_0\in A$를 택할 수 있다. 그럼 각 $b_j$는

$$C=A_{a_0}[y_1,\ldots, y_d]$$

위에서 integral하고, 따라서 $B_{a_0}$는 finite $C$-module이다. 여기에서 $y_i$들이 $K$ 위에서 대수적으로 독립이므로 $C$는 $A_{a_0}$ 위의 polynomial ring이며, 특히 free $A_{a_0}$-module이다.

이제 dévissage를 Noetherian ring $C$와 finite $C$-module $B_{a_0}$에 다시 적용하면, quotient가 $C/\mathfrak{p}$ 꼴인 finite filtration을 얻는다. 따라서 각 $C/\mathfrak{p}$에 대하여 결론을 보이면 충분하다.

귀납의 기저는 $d=0$인 경우이다. 이때 $C=A_{a_0}$이므로 위의 dévissage가 주는 quotient는 $A_{a_0}/\mathfrak{p}$ 꼴이고, $\mathfrak{p}=0$이면 free module이며 $\mathfrak{p}\neq 0$이면 $\mathfrak{p}$의 $0$이 아닌 원소를 뒤집어 $0$으로 만들 수 있다.

이제 $d>0$이라 하자. $\mathfrak{p}=0$이면 $C$ 자신이 free $A_{a_0}$-module이므로 볼 것이 없다. $\mathfrak{p}\neq 0$이라 하자. 만일 $\mathfrak{p}\cap A_{a_0}\neq 0$이면 그 안의 $0$이 아닌 원소 $a_1$을 택했을 때 $(C/\mathfrak{p})_{a_1}=0$이므로 결론이 성립한다. 그렇지 않다면 $S=A_{a_0}\setminus\{0\}$에 대하여 $S^{-1}C=K[y_1,\ldots,y_d]$이고 $\mathfrak{p}\cap S=\emptyset$이므로, $\mathfrak{p}K[y_1,\ldots,y_d]$는 $K[y_1,\ldots,y_d]$의 $0$이 아닌 prime ideal이다. 이제

$$(C/\mathfrak{p})\otimes_{A_{a_0}}K=K[y_1,\ldots,y_d]/\mathfrak{p}K[y_1,\ldots,y_d]$$

인데, $0\neq g\in \mathfrak{p}K[y_1,\ldots,y_d]$를 택하면 이 quotient ring에서 $y_1,\ldots,y_d$의 image들은 $g=0$이라는 대수적 관계를 만족하므로 대수적으로 독립일 수 없다. 그런데 이 quotient ring은 이들 image로 생성되는 $K$-algebra이므로 그 field of fractions의 초월차수는 $d$보다 작고, [정리 3](#thm3)에 의하여

$$\dim\big((C/\mathfrak{p})\otimes_{A_{a_0}}K\big)<d$$

이다. $A_{a_0}$ 또한 $K$를 field of fractions로 갖는 Noetherian integral domain이고 $C/\mathfrak{p}$는 그 위의 finite type integral domain이므로, 귀납가정을 적용하면 $0\neq a_\mathfrak{p}\in A_{a_0}$가 존재하여 $(C/\mathfrak{p})_{a_\mathfrak{p}}$가 free $(A_{a_0})_{a_\mathfrak{p}}$-module이다. 필요하다면 $a_0$의 거듭제곱을 곱하여 $a_\mathfrak{p}\in A$로 볼 수 있다.

Filtration에 등장하는 유한개의 $\mathfrak{p}$들에 대한 $a_\mathfrak{p}$와 $a_0$의 곱을 $a$로 두면 $B_a=(B_{a_0})_a$는 free $A_a$-module이다.
:::

증명에서 결정적인 것은 두 가지이다. 하나는 dévissage로 $M$을 $B/\mathfrak{q}$ 꼴의 quotient들로 분해하여 문제를 domain의 경우로 옮기는 것이고, 다른 하나는 [정리 1](#thm1)로 $B$를 $A_{a_0}$ 위의 polynomial ring 위에서 finite하게 만든 뒤 [정리 3](#thm3)의 차원 계산으로 초월차수를 떨어뜨려 귀납을 돌리는 것이다. Free module은 flat이므로 [정리 5](#thm5)는 flatness가 generic하게 성립한다는 진술로도 읽히며, 이 형태가 대수기하에서 finite type morphism이 base의 조밀한 열린집합 위에서 flat이 된다는 사실과 finite type morphism의 image가 constructible이라는 Chevalley의 정리를 준다.