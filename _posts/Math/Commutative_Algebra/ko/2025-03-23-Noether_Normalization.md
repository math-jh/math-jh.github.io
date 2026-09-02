---
title: "뇌터 정규화"
description: "뇌터 정규화 보조정리를 다루며, 가환대수에서 유한 생성 대수의 다항식환 위 구조를 보장하는 핵심 정리와 그 증명을 살펴본다."
excerpt: "유한생성 algebra의 Noether normalization 정리와 응용"

categories: [Math / Commutative Algebra]
permalink: /ko/math/commutative_algebra/noether_normalization
sidebar: 
    nav: "commutative_algebra-ko"

date: 2025-03-23
weight: 22
drift_needed: true

---

## 뇌터 정규화

이번 글의 목표는 다음의 정리를 보이고, 이에 따른 결과들을 살펴보는 것이다. 

::: 정리 1 (Noether normalization lemma)
Finitely generated $d$-dimensional $\mathbb{K}$-algebra $A$에 대하여, 다음의 부등식

$$d_1>d_2>\cdots>d_m\geq 0$$

을 만족하는 음이 아닌 정수들과, $\dim \mathfrak{a}_i=d_i$를 만족하는 $A$의 ideal들의 descending chain

$$\mathfrak{a}_1\subseteq \mathfrak{a}_2\subseteq\cdots\subseteq \mathfrak{a}_m$$

이 주어졌다 하자. 그럼 $A$의 적당한 subring $B\cong \mathbb{K}[\x_1,\ldots, \x_d]$가 존재하여, $A$가 $B$-module로서 finitely generated이고 다음 식

$$\mathfrak{a}_i\cap B=(\x_{d_i+1},\ldots, \x_d)\qquad\text{for $i=1,\ldots, m$}$$

이 성립하도록 할 수 있다. 
:::

이는 다음의 보조정리를 사용하여 보일 수 있으며, 이에 대한 증명은 생략하기로 한다. 

::: 보조정리 2
Field $\mathbb{K}$와, non-constant polynomial $f\in B=\mathbb{K}[\x_1,\ldots, \x_r]$이 주어졌다 하자. 그럼 적당한 원소들 $\x_1',\ldots, \x_{r-1}'\in B$가 존재하여, 원소들 $\x_1',\ldots, \x_{r-1}', f$로 생성된 $B$의 $\mathbb{K}$-subalgebra를 $B'$라 했을 때 $B$가 finitely generated $B'$-module이도록 할 수 있다. 뿐만 아니라, 이들 원소들은 다음과 같이 택할 수 있다.

1. 충분히 큰 정수 $e$에 대하여, $\x_i'=\x_i-\x_r^{e^i}$으로 택할 수 있다. 
2. 만일 $\mathbb{K}$가 infinite field라면, 적당한 $a_i\in \mathbb{K}$들에 대해 $\x_i'=\x_i-a_i\x_r$로 택할 수 있다. 
:::

그럼 [정리 1](#thm1)의 증명은 다음과 같다. 

::: 증명 (정리 1)
우선 $A$가 finitely generated $\mathbb{K}$-algebra이므로 $A=\mathbb{K}[\y_1,\ldots, \y_r]/\mathfrak{a}$라 적을 수 있다. 그럼 주어진 조건을 만족하는 ideal들의 chain이 주어졌다 하면, 이들의 $\mathbb{K}[\y_1,\ldots, \y_r]$에서의 preimage들로 이루어진 chain

$$\tilde{\mathfrak{a}}_1\subseteq \tilde{\mathfrak{a}}_2\subseteq\cdots\subseteq  \tilde{\mathfrak{a}}_m$$

를 생각한 후 $\mathfrak{a}_0=\mathfrak{a}$를 끼워넣어 이를 $\mathbb{K}[\y_1,\ldots, \y_r]$에서의 ideal들의 descending chain

$$\mathfrak{a}\subseteq \tilde{\mathfrak{a}}_1\subseteq \tilde{\mathfrak{a}}_2\subseteq\cdots\subseteq  \tilde{\mathfrak{a}}_m$$

으로 볼 수 있으므로 주어진 주장을 polynomial ring $A=\mathbb{K}[\y_1,\ldots, \y_r]$에 대해서만 보이면 충분하다. 이 때 새로 끼워넣은 $\mathfrak{a}_0$의 dimension은 $d_0=\dim \mathfrak{a}_0=\dim A$이고, 환원된 상황에서 정리의 $d$ 자리에 오는 것은 새로운 ambient ring의 dimension, 곧 [§매개계, ⁋따름정리 11](/ko/math/commutative_algebra/system_of_parameters#cor11)의 첫째 결과가 주는 $\dim \mathbb{K}[\y_1,\ldots, \y_r]=r$이다. 따라서 아래에서는 $d=r$로 두고, 원래의 $\dim A$는 $d_0$로 적는다. 만일 polynomial ring에서 주장이 성립한다면, 일반적인 결과는 다음과 같이 얻을 수 있다. $\mathbb{K}[\y_1,\ldots, \y_r]$의 subring $B\cong \mathbb{K}[\x_1,\ldots, \x_r]$이 존재하여 $\mathbb{K}[\y_1,\ldots, \y_r]$이 finitely generated $B$-module이고 $\mathfrak{a}_0\cap B=(\x_{d_0+1},\ldots, \x_r)$, $\tilde{\mathfrak{a}}_i\cap B=(\x_{d_i+1},\ldots, \x_r)$이 성립한다 하자. Quotient map을 $\pi:\mathbb{K}[\y_1,\ldots, \y_r] \rightarrow A$라 하고 $\bar{B}=\pi(B)$라 하면, $\pi$를 $B$로 제한한 것의 kernel이 $\mathfrak{a}_0\cap B$이므로 $\bar{B}\cong B/(\mathfrak{a}_0\cap B)\cong \mathbb{K}[\x_1,\ldots, \x_{d_0}]$이고, $\mathbb{K}[\y_1,\ldots, \y_r]$이 $B$ 위에서 finite이므로 그 quotient인 $A$는 $\bar{B}$ 위에서 finite이다. 또, $b\in B$에 대하여 $\pi(b)\in \mathfrak{a}_i$인 것과 $b\in \tilde{\mathfrak{a}}_i$인 것이 동치이므로 $\mathfrak{a}_i\cap \bar{B}=\pi(\tilde{\mathfrak{a}}_i\cap B)$이고, $\x_{d_0+1},\ldots, \x_r$이 모두 $\pi$의 kernel에 속하므로 이는 $(\pi(\x_{d_i+1}),\ldots, \pi(\x_{d_0}))$과 같다. 즉 $\bar{B}$가 원래의 $A$에 대해 정리가 요구하는 subring이다.

이제 정리의 원소들 $\x_i$들을 만들기 위해 우리는 우선 $\x_i'=\y_i$로 두고, 이들을 바꿔가며 주어진 조건을 만족하는 $\x_i$들을 찾을 것이다. 이를 위해 다음의 두 조건

1. $A$는 finitely generated $B_e=\mathbb{K}[\x_1',\ldots, \x_e',\x_{e+1},\ldots, \x_d]$-module이다. 
2. 각각의 $i$에 대하여 $\mathfrak{a}_i\cap B_e\supseteq(\x_k,\ldots, \x_d)$이 성립한다. 여기서 $k=\max(d_i+1, e+1)$이다. 

을 만족하는 원소들 $\x_1',\ldots, \x_e', \x_{e+1},\ldots, \x_d$들이 주어졌다 하고, 이로부터 새로운 원소들 $\x_1',\ldots, \x_{e-1}'$ 그리고 $\x_e$를 찾아 위의 조건이 그대로 유지되도록 할 수 있다는 것을 보인다. 그럼 이 과정을 반복하여 마지막으로 얻어진 $B=B_{d_m}$이 원하는 조건을 만족한다는 것은 둘째 조건의 포함관계가 사실 등식이라는 것을 보이면 되며, 이는 다음과 같다. 우선 $A$가 finitely generated $B$-module이므로 [§정수적 확장, ⁋보조정리 4](/ko/math/commutative_algebra/integral_extension#lem4)에 의하여 $B\hookrightarrow A$는 integral extension이고, 따라서 [§차원, ⁋명제 4](/ko/math/commutative_algebra/Krull_dimension#prop4)에 의하여 $\dim(\mathfrak{a}_i\cap B)=\dim \mathfrak{a}_i=d_i$이다. 한편 $B=B_{d_m}$에 대한 둘째 조건은 $\mathfrak{a}_i\cap B\supseteq(\x_{d_i+1},\ldots, \x_d)$이므로, $R=B/(\x_{d_i+1},\ldots, \x_d)\cong \mathbb{K}[\x_1,\ldots, \x_{d_i}]$에서의 $\mathfrak{a}_i\cap B$의 image를 $J$라 하면 $B/(\mathfrak{a}_i\cap B)\cong R/J$이고, 특히 $\dim R/J=d_i$이다. 그런데 $\dim \mathfrak{a}_i=d_i$이므로 $\mathfrak{a}_i$는 proper ideal이고 따라서 $J$ 또한 $R$의 proper ideal이므로, 만일 $J\neq 0$이라면 $J$에 속하는 $0$이 아닌 원소 $g$는 unit이 아닌, 곧 상수가 아닌 다항식이다. 이제 $J$를 포함하는 임의의 prime ideal $\mathfrak{p}$는 $g$를 포함하므로 $(g)$를 포함하는 minimal prime ideal 중 $\mathfrak{p}$에 포함되는 것 $\mathfrak{q}$를 가지며, [§차원, ⁋정리 6](/ko/math/commutative_algebra/Krull_dimension#thm6)에 의하여 $\codim \mathfrak{q}\leq 1$인데 $R$이 domain이고 $g\neq 0$이므로 $\mathfrak{q}\neq(0)$, 곧 $\codim \mathfrak{q}=1$이다. 그럼 부등식 $\dim \mathfrak{q}+\codim \mathfrak{q}\leq \dim R=d_i$로부터 ([§차원, ⁋정의 2](/ko/math/commutative_algebra/Krull_dimension#def2), [§매개계, ⁋따름정리 11](/ko/math/commutative_algebra/system_of_parameters#cor11)) $\dim R/\mathfrak{p}\leq \dim \mathfrak{q}\leq d_i-1$이고, 이러한 $\mathfrak{p}$들에 대한 supremum을 취하면 $\dim R/J\leq d_i-1$이 되어 모순이다. 따라서 $J=0$이고, 곧 $\mathfrak{a}_i\cap B=(\x_{d_i+1},\ldots, \x_d)$이다. 

이제 이 귀납법을 완성하기 위해, $d\geq e>d_m$을 만족하는 $e$에 대하여, 위의 두 조건을 만족하는 $\x_1',\ldots, \x_e', \x_{e+1},\ldots, \x_d$들이 주어졌다 하고, $i$가 $e>d_i$를 만족하는 것들 중 가장 작은 index라 가정하자. 그럼

$$\mathfrak{a}_i\cap \mathbb{K}[\x_1',\ldots, \x_e']\neq 0$$

이다. 만일 이 교집합이 $0$이라 가정하면, 둘째 조건에 의해 

$$\mathfrak{a}_i\cap B_e\supseteq (\x_{e+1},\ldots, \x_d)$$

이 성립하는데, 좌변의 ideal은 $d_i$-차원이고, 우변의 ideal의 차원은 $e$가 되어 모순이기 때문이다. 이제 $\x_e$를 위의 교집합에 속하는 아무 nonzero polynomial로 잡자. $\mathfrak{a}_i$가 proper ideal이므로 $\x_e$는 상수가 아니다. 여기서 $A$가 $B_e$ 위에서 finite이므로 [§차원, ⁋명제 4](/ko/math/commutative_algebra/Krull_dimension#prop4)에 의하여 $\dim B_e=\dim A=d$이고, $B_e$는 $d$개의 원소로 생성되는 $\mathbb{K}$-algebra이므로 $d$변수 polynomial ring의 quotient인데, $0$이 아닌 proper ideal로 quotient를 취하면 차원이 떨어진다는 앞의 논증에 의하여 이 quotient map의 kernel은 $0$이어야 한다. 즉 $\x_1',\ldots, \x_e',\x_{e+1},\ldots, \x_d$는 algebraically independent하고, 특히 $\mathbb{K}[\x_1',\ldots, \x_e']$가 polynomial ring이므로 여기에 $f=\x_e$로 두어 [보조정리 2](#lem2)를 적용할 수 있다. 그럼 새로운 원소들 $\x_1',\ldots, \x_{e-1}'$을 얻어 $\mathbb{K}[\x_1',\ldots, \x_e']$가 $\mathbb{K}[\x_1',\ldots, \x_{e-1}', \x_e]$ 위에서 finite이도록 할 수 있다.

이렇게 얻어진 $B_{e-1}=\mathbb{K}[\x_1',\ldots, \x_{e-1}',\x_e,\x_{e+1},\ldots, \x_d]$가 위의 두 조건을 그대로 만족한다는 것은 다음과 같이 확인된다. 첫째 조건의 경우, $B_e$가 $B_{e-1}$ 위에서 finite이고 $A$가 $B_e$ 위에서 finite이므로 $A$는 $B_{e-1}$ 위에서도 finite이다. 둘째 조건의 경우 $B_{e-1}$에 대해 요구되는 것은 $\mathfrak{a}_j\cap B_{e-1}\supseteq(\x_k,\ldots, \x_d)$, $k=\max(d_j+1, e)$이므로 $j\geq i$와 $j<i$를 나누어 보면 된다. 우선 $j\geq i$이면 $d_j\leq d_i<e$이므로 $k=e$이고, $\x_e\in \mathfrak{a}_i\subseteq \mathfrak{a}_j$이며 $\x_{e+1},\ldots, \x_d$는 $B_e$에 대한 둘째 조건에 의해 이미 $\mathfrak{a}_j$에 속하므로 원하는 포함관계를 얻는다. 반면 $j<i$이면 $i$가 $e>d_i$를 만족하는 가장 작은 index라는 것에서 $d_j\geq e$이므로 $k=d_j+1$이고, 이 때 요구되는 generator $\x_{d_j+1},\ldots, \x_d$들은 모두 이번 단계에서 건드리지 않은 변수 $\x_{e+1},\ldots, \x_d$ 중에 있어 $B_{e-1}$에 속하며, 이들이 $\mathfrak{a}_j$에 속한다는 것이 곧 $B_e$에 대한 둘째 조건이다.
:::

## 결과들

[정리 1](#thm1)은 다음의 결과를 준다.

::: 정리 3
Ring $A$가 integral domain이고, finitely generated $\mathbb{K}$-algebra라 하자. 그럼 $\dim A=\trdeg_\mathbb{K}\Frac(A)$이다.
:::

[정리 3](#thm3)은 quotient를 취한 상황으로 자연스럽게 일반화되어, 다음의 *차원 공식<sub>dimension formula</sub>*을 준다.

::: 정리 4
Finitely generated $\mathbb{K}$-algebra domain $A$와 그 prime ideal $\mathfrak{p}$에 대하여 다음이 성립한다.

$$\dim A/\mathfrak{p}+\codim\mathfrak{p}=\dim A$$
:::
::: 증명
부등식 $\dim A/\mathfrak{p}+\codim\mathfrak{p}\leq\dim A$는 임의의 ring에 대하여 성립하므로 ([§차원, ⁋정의 2](/ko/math/commutative_algebra/Krull_dimension#def2)), 반대 부등식만 보이면 된다. $n=\dim A$, $d=\dim A/\mathfrak{p}=\dim\mathfrak{p}$라 두자. [정리 1](#thm1)을 $A$의 ideal $\mathfrak{a}_1=\mathfrak{p}$ 하나로 이루어진 chain에 적용하면, $A$의 subring $B\cong\mathbb{K}[\x_1,\ldots, \x_n]$이 존재하여 $A$가 finitely generated $B$-module이고 $\mathfrak{p}\cap B=(\x_{d+1},\ldots, \x_n)$을 만족한다. 그럼 $B\hookrightarrow A$는 integral extension이다. 여기서 $\mathfrak{p}$에서 시작하는 $A$의 prime ideal들의 chain을 $B$로 contract하면 [§정수적 확장과 아이디얼, ⁋따름정리 4](/ko/math/commutative_algebra/lying_over_and_going_up#cor4)에 의하여 포함관계가 strict하게 유지되므로 $\codim_A\mathfrak{p}\leq\codim_B(\mathfrak{p}\cap B)$를 얻는다.

우리에게 필요한 반대 방향은 $\mathfrak{p}\cap B$에서 시작하는 $B$의 chain을 $\mathfrak{p}$ 아래로 들어올리는 것으로 going-down에 해당하는데, $B$는 polynomial ring이라 UFD이고 ([\[환론\] §다항식환, ⁋정리 16](/ko/math/ring_theory/polynomial_rings#thm16)) 따라서 normal domain이며 ([§정수적 확장, ⁋명제 9](/ko/math/commutative_algebra/integral_extension#prop9)) $A$는 가정에 의해 domain이므로, [§정수적 확장과 아이디얼, ⁋정리 6](/ko/math/commutative_algebra/lying_over_and_going_up#thm6)을 반복해서 적용하면 $\mathfrak{p}\cap B$ 아래의 chain이 주어질 때마다 그 위에 놓인 $\mathfrak{p}$ 아래의 chain을 얻는다. 이 chain의 원소들은 서로 다른 prime ideal로 contract되므로 다시 strict이며, 따라서 $\codim_A\mathfrak{p}=\codim_B(\mathfrak{p}\cap B)$이다.

이제 polynomial ring $B=\mathbb{K}[\x_1,\ldots, \x_n]$에서 ideal $(\x_{d+1},\ldots, \x_n)$의 height를 계산하자. Chain

$$(0)\subseteq(\x_n)\subseteq(\x_{n-1},\x_n)\subseteq\cdots\subseteq(\x_{d+1},\ldots, \x_n)$$

은 이 ideal의 height가 적어도 $n-d$임을 보여주며, quotient ring $B/(\x_{d+1},\ldots, \x_n)\cong\mathbb{K}[\x_1,\ldots, \x_d]$가 $d$차원이므로 ([§매개계, ⁋따름정리 11](/ko/math/commutative_algebra/system_of_parameters#cor11)) 부등식 $\dim+\codim\leq n$으로 height는 기껏해야 $n-d$이다. 따라서 $\codim_B(\x_{d+1},\ldots, \x_n)=n-d$이며, 결국 $\codim\mathfrak{p}=n-d=\dim A-\dim A/\mathfrak{p}$이다.
:::

한편 [정리 1](#thm1)이 주는 polynomial subring은 계수의 확대와 잘 호환되므로, finitely generated $\mathbb{K}$-algebra의 차원이 계수체를 키워도 변하지 않는다는 것 또한 얻어진다.

::: 명제 5
Field $\mathbb{K}$의 extension $\mathbb{K}\hookrightarrow \mathbb{L}$과 finitely generated $\mathbb{K}$-algebra $A$에 대하여 다음의 식

$$\dim(A\otimes_\mathbb{K}\mathbb{L})=\dim A$$

이 성립한다.
:::
::: 증명
$d=\dim A$라 하고, [정리 1](#thm1)을 ideal의 chain 없이 적용하여 $A$의 subring $B\cong\mathbb{K}[\x_1,\ldots, \x_d]$를 $A$가 finitely generated $B$-module이도록 택하자. 이제 $\mathbb{L}$은 $\mathbb{K}$-vector space이므로 free $\mathbb{K}$-module이고 따라서 flat이므로 ([\[다중선형대수학\] §사영가군, 단사가군, 평탄가군, ⁋정의 7](/ko/math/multilinear_algebra/various_modules#def7)), inclusion $B\hookrightarrow A$에 $-\otimes_\mathbb{K}\mathbb{L}$을 적용하여 얻어지는 ring homomorphism

$$B\otimes_\mathbb{K}\mathbb{L} \rightarrow A\otimes_\mathbb{K}\mathbb{L}$$

또한 injective이다. 여기서 $B\otimes_\mathbb{K}\mathbb{L}\cong\mathbb{L}[\x_1,\ldots, \x_d]$이고, $A$를 $B$-module로서 생성하는 원소들 $a_1,\ldots, a_r$에 대하여 $a_i\otimes 1$들이 $A\otimes_\mathbb{K}\mathbb{L}$을 $B\otimes_\mathbb{K}\mathbb{L}$-module로서 생성하므로, 이 injection은 finite이고 따라서 integral extension이다. ([§정수적 확장, ⁋보조정리 4](/ko/math/commutative_algebra/integral_extension#lem4))

그런데 integral homomorphism은 차원을 보존하므로 ([§차원, ⁋명제 4](/ko/math/commutative_algebra/Krull_dimension#prop4)) 다음의 식

$$\dim(A\otimes_\mathbb{K}\mathbb{L})=\dim\mathbb{L}[\x_1,\ldots, \x_d]=d$$

을 얻으며, 여기서 마지막 등식은 [§매개계, ⁋따름정리 11](/ko/math/commutative_algebra/system_of_parameters#cor11)이다.
:::

## 제네릭 자유성

지금까지는 base가 field인 상황을 다루었다. 이를 Noetherian integral domain $A$로 넓히면 finite type $A$-algebra $B$와 그 위의 finitely generated module $M$이 $A$-module로서 free일 이유는 없다. 그러나 $A$의 $0$이 아닌 원소 하나를 뒤집는 것만으로 언제나 free로 만들 수 있다는 것이 다음의 결과이며, localization $A_a$가 $A$와 같은 field of fractions를 가지므로 이는 free성이 generic하게 성립한다는 뜻이다.

::: 정리 6 (Grothendieck의 generic freeness)
Noetherian integral domain $A$와 finite type $A$-algebra $B$, 그리고 finitely generated $B$-module $M$이 주어졌다 하자. 그럼 $0$이 아닌 $a\in A$가 존재하여 $M_a$가 free $A_a$-module이 된다.
:::
::: 증명
$B$는 Noetherian integral domain $A$ 위의 finite type algebra이므로 [§기본 개념들, ⁋정리 12](/ko/math/commutative_algebra/basic_notions#thm12)에 의하여 Noetherian ring이다.

먼저 [§동반소아이디얼, ⁋보조정리 6](/ko/math/commutative_algebra/associated_primes#lem6)을 $B$와 $M$에 적용하는 dévissage로 문제를 줄인다. 이를 적용하면 filtration

$$0=M_0\subseteq M_1\subseteq\cdots\subseteq M_n=M,\qquad M_i/M_{i-1}\cong B/\mathfrak{q}_i$$

를 얻는다. 각 $B/\mathfrak{q}_i$에 대하여 결론이 성립한다 하고 그 원소들의 곱을 $a$라 하면, exact sequence

$$0 \longrightarrow (M_{i-1})_a \longrightarrow (M_i)_a \longrightarrow (B/\mathfrak{q}_i)_a \longrightarrow 0$$

의 오른쪽 항이 free module이므로 이 exact sequence는 split하고, $i$에 대한 귀납법으로 $(M_i)_a$가 모두 free $A_a$-module이 된다. 따라서 $M=B/\mathfrak{q}$인 경우, 즉 $B$를 $B/\mathfrak{q}$로 바꾸어 $B$가 integral domain이고 $M=B$인 경우만 보이면 충분하다.

$\varphi: A \rightarrow B$의 kernel이 $0$이 아닌 경우는 곧바로 처리된다. 이때 $0\neq a\in \ker \varphi$를 택하면 $B_a=B\otimes_AA_a$에서 $\varphi(a)=0$이면서 $a$가 unit이므로 $B_a=0$이고, 이는 rank $0$의 free module이다. 따라서 $A\subseteq B$라 가정해도 좋다.

이제 $K=\Frac(A)$라 하면 $B\otimes_AK$는 $A\setminus\{0\}$에서의 $B$의 localization이므로 $0$이 아닌 integral domain이며, $K$ 위의 finite type algebra이다. 남은 주장을 $d=\dim (B\otimes_AK)$에 대한 귀납법으로 보인다.

[정리 1](#thm1)을 ideal의 chain 없이 적용하면 algebraically independent한 원소들 $y_1,\ldots, y_d\in B\otimes_AK$가 존재하여 $B\otimes_AK$가 $K[y_1,\ldots,y_d]$ 위의 finite module이다. 각 $y_i$에 $A$의 $0$이 아닌 원소를 곱해도 대수적 독립성과 유한성은 유지되므로, 처음부터 $y_i\in B$라 가정해도 좋다.

$B$를 $A$-algebra로서 생성하는 원소를 $b_1,\ldots, b_m$이라 하면 각 $b_j$는 $K[y_1,\ldots,y_d]$ 위에서 integral하다. 이 정수 방정식들에 등장하는 계수는 유한개이므로, 그 분모를 모두 없애는 $0\neq a_0\in A$를 택할 수 있다. 그럼 각 $b_j$는

$$C=A_{a_0}[y_1,\ldots, y_d]$$

위에서 integral하고, 따라서 $B_{a_0}$는 finite $C$-module이다. 여기에서 $y_i$들이 $K$ 위에서 algebraically independent하므로 $C$는 $A_{a_0}$ 위의 polynomial ring이며, 특히 free $A_{a_0}$-module이다.

이제 dévissage를 Noetherian ring $C$와 finite $C$-module $B_{a_0}$에 다시 적용하면, quotient가 $C/\mathfrak{p}$ 꼴인 finite filtration을 얻는다. 따라서 각 $C/\mathfrak{p}$에 대하여 결론을 보이면 충분하다.

귀납의 기저는 $d=0$인 경우이다. 이때 $C=A_{a_0}$이므로 위의 dévissage가 주는 quotient는 $A_{a_0}/\mathfrak{p}$ 꼴이고, $\mathfrak{p}=0$이면 free module이며 $\mathfrak{p}\neq 0$이면 $\mathfrak{p}$의 $0$이 아닌 원소를 뒤집어 $0$으로 만들 수 있다.

이제 $d>0$이라 하자. $\mathfrak{p}=0$이면 $C$ 자신이 free $A_{a_0}$-module이므로 볼 것이 없다. $\mathfrak{p}\neq 0$이라 하자. 만일 $\mathfrak{p}\cap A_{a_0}\neq 0$이면 그 안의 $0$이 아닌 원소 $a_1$을 택했을 때 $(C/\mathfrak{p})_{a_1}=0$이므로 결론이 성립한다. 그렇지 않다면 $S=A_{a_0}\setminus\{0\}$에 대하여 $S^{-1}C=K[y_1,\ldots,y_d]$이고 $\mathfrak{p}\cap S=\emptyset$이므로, $\mathfrak{p}K[y_1,\ldots,y_d]$는 $K[y_1,\ldots,y_d]$의 $0$이 아닌 prime ideal이다. 이제

$$(C/\mathfrak{p})\otimes_{A_{a_0}}K=K[y_1,\ldots,y_d]/\mathfrak{p}K[y_1,\ldots,y_d]$$

인데, $0\neq g\in \mathfrak{p}K[y_1,\ldots,y_d]$를 택하면 이 quotient ring에서 $y_1,\ldots,y_d$의 image들은 $g=0$이라는 algebraic relation을 만족하므로 algebraically independent할 수 없다. 그런데 이 quotient ring은 이들 image로 생성되는 $K$-algebra이므로 그 field of fractions의 transcendence degree는 $d$보다 작고, [정리 3](#thm3)에 의하여

$$\dim\big((C/\mathfrak{p})\otimes_{A_{a_0}}K\big)<d$$

이다. $A_{a_0}$ 또한 $K$를 field of fractions로 갖는 Noetherian integral domain이고 $C/\mathfrak{p}$는 그 위의 finite type integral domain이므로, 귀납가정을 적용하면 $0\neq a_\mathfrak{p}\in A_{a_0}$가 존재하여 $(C/\mathfrak{p})_{a_\mathfrak{p}}$가 free $(A_{a_0})_{a_\mathfrak{p}}$-module이다. 필요하다면 $a_0$의 거듭제곱을 곱하여 $a_\mathfrak{p}\in A$로 볼 수 있다.

Filtration에 등장하는 유한개의 $\mathfrak{p}$들에 대한 $a_\mathfrak{p}$와 $a_0$의 곱을 $a$로 두면 $B_a=(B_{a_0})_a$는 free $A_a$-module이다.
:::

증명에서 결정적인 것은 두 가지이다. 하나는 dévissage로 $M$을 $B/\mathfrak{q}$ 꼴의 quotient들로 분해하여 문제를 domain의 경우로 옮기는 것이고, 다른 하나는 [정리 1](#thm1)로 $B$를 $A_{a_0}$ 위의 polynomial ring 위에서 finite하게 만든 뒤 [정리 3](#thm3)의 차원 계산으로 transcendence degree를 떨어뜨려 귀납을 돌리는 것이다. Free module은 flat이므로 [정리 6](#thm6)은 flatness가 generic하게 성립한다는 진술로도 읽히며, 이 형태가 대수기하에서 finite type morphism이 base의 조밀한 열린집합 위에서 flat이 된다는 사실과 finite type morphism의 image가 constructible이라는 Chevalley의 정리를 준다.

---

**참고문헌**

**[Eis]** David Eisenbud. *Commutative Algebra: with a view toward algebraic geometry*. Springer, 1995.
