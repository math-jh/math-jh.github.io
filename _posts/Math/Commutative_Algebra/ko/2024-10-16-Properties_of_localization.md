---

title: "국소화의 성질들"
excerpt: ""

categories: [Math / Commutative Algebra]
permalink: /ko/math/commutative_algebra/properties_of_localization
header:
    overlay_image: /assets/images/Math/Commutative_Algebra/Properties_of_localization.png
    overlay_filter: 0.5
sidebar: 
    nav: "commutative_algebra-ko"

date: 2024-10-16
last_modified_at: 2024-10-16
weight: 2

---

이제 우리는 국소화의 추가적인 성질들에 대해 살펴본다. 이 글의 첫 번째 목표는 앞선 글에서 살펴본 가군의 국소화와 환의 국소화 사이에 밀접한 관계가 있다는 것을 증명하는 것이다. 이 글에서 ring $A$, $A$의 multiplicative subset $S$와 $A$-module $M$을 고정한다. 

## 국소화와 Hom, tensor

우선 보조정리 하나를 증명하며 시작한다. $A$-module homomorphism $S^{-1}A\times_A M \rightarrow  S^{-1}M$을 $(r/u, x)\mapsto rx/u$으로 정의하면 이는 $A$-bilinear map이고, 따라서 $A$-linear map $S^{-1}A\otimes_A M \rightarrow S^{-1}M$을 유도한다. ([\[대수적 구조\] §가군의 직접곱과 직합, 텐서곱, ⁋정리 5](/ko/math/algebraic_structures/operations_of_modules#def5)) 

<div class="proposition" markdown="1">

<ins id="lem1">**보조정리 1**</ins> 위에서 정의한 $A$-linear map은 isomorphism이 된다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

역함수를 만들어주면 충분하다. 이를 위해 우선 $M\times S$에서 $S^{-1}A\otimes_AM$으로의 함수를

$$(x,s)\mapsto \frac{1}{s}\otimes x$$

으로 정의하자. 그럼 이 함수는 $S^{-1}M$에서 $S^{-1}A\otimes_AM$으로의 잘 정의된 $A$-linear map을 정의한다. 이를 살펴보기 위해서는 이 함수가 $M\times S$ 위에 정의된 equivalence relation에 대해 잘 행동하는 것을 보이면 충분하다. 따라서 $(x,s)\sim (x',s')$를 만족하는 $M\times S$의 두 원소가 주어졌다 하자. 그럼 적당한 $t\in S$가 존재하여 $tsx'=ts'x$가 성립하며, 이로부터

$$\frac{1}{tss'}\otimes ts'x=\frac{1}{tss'}\otimes tsx'$$

가 성립한다. 그런데 $ts',ts\in A$이므로, 좌변과 우변의 $ts'$와 $ts$를 각각 $\otimes$의 왼쪽으로 넘겨주면

$$\frac{1}{s}\otimes x=\frac{1}{s'}\otimes x'$$

를 얻는다. 이 함수가 $A$-linear map이며 위에서 정의한 $S^{-1}A\otimes_A M \rightarrow S^{-1}M$의 역함수임은 자명하다.

</details>

따라서 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> $S^{-1}A$는 flat $A$-module이다. ([\[다중선형대수학\] §사영가군, 단사가군, 평탄가군, ⁋정의 7](/ko/math/multilinear_algebra/various_modules#def7))

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 injective $A$-linear map $u:M \rightarrow M'$이 주어졌다 하고, $u\otimes_AS^{-1}A$이 injective인 것을 보여야 한다. 그런데 [보조정리 1](#lem1)에 의해, 이는 linear map $S^{-1}M \rightarrow S^{-1}M'$이 injective인 것을 보이면 충분하다. 어떠한 $x/s\in S^{-1}M$에 대하여, 이를 $S^{-1}M'$으로 보낸 원소인 $u(x)/s$가 $S^{-1}M'$에서 $0$이라 하자. 그럼 $u(x)/s=0/1$로부터 적당한 $t\in S$가 존재하여 

$$tu(x)=u(tx)=0$$

이 성립하고, $u$가 injective이므로 $M$에서 $tx=0$이어야 한다. 그럼 $S^{-1}M$에서

$$\frac{x}{s}=\frac{tx}{ts}=\frac{0}{ts}=0$$

이므로 원하는 결과를 얻는다.

</details>

한편 다음 보조정리가 성립한다.

<div class="proposition" markdown="1">

<ins id="lem3">**보조정리 3**</ins> $A$-module $M$과, $A$의 maximal ideal $\mathfrak{m}$에서의 localization $\epsilon_\mathfrak{m}:M \rightarrow M_\mathfrak{m}$을 생각하자. 그럼 $M$의 원소 $x$가 $0$인 것은, <em_ko>모든</em_ko> $A$의 maximal ideal $\mathfrak{m}$에 대하여 위에서 정의한 $\epsilon_\mathfrak{m}$이 $\epsilon_\mathfrak{m}(x)=0$을 만족하는 것이 동치이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

한쪽 방향은 자명하므로 반대쪽만 보이면 충분하다. 고정된 maximal ideal $\mathfrak{m}$에 대하여 $\epsilon_\mathfrak{m}(x)=0$이 성립한다 하자. 이는 $\ann(x)$가 $\mathfrak{m}$에 포함되지 않는 것과 동치이다. 그럼 주어진 조건에 의하여, $\ann(x)$는 <em_ko>모든</em_ko> $A$의 maximal ideal에 포함되지 않는 ideal이고, 이러한 ideal은 오직 $A$ 자기 자신 뿐이다. 즉 $\ann(x)=A$이고 이로써 증명이 완료된다.

</details>

따라서 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $A$-linear map $u:M \rightarrow N$이 monomorphism (resp. epimorphism, isomorphism)인 것은 임의의 maximal ideal $\mathfrak{m}$에 대하여 $u_\mathfrak{m}: M_\mathfrak{m} \rightarrow N_\mathfrak{m}$이 그러한 것과 동치이다.

</div>

이에 대한 증명은 [보조정리 3](#cor3)를 kernel과 cokernel에 대해 적용하면 충분하다. 

다음 정리는 앞으로 종종 사용될 것이므로, 증명은 신경쓰지 않더라도 결과는 기억해두는 것이 좋다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> Ring $A$와 $A$-algebra $E$를 고정하자. 그럼 임의의 $A$-module $M,N$에 대하여 다음의 $E$-module homomorphism

$$\alpha: E\otimes_A\Hom_A(M,N) \rightarrow\Hom_E(E\otimes_A M, E\otimes_AN);\qquad (1\otimes f)\mapsto \id_E\otimes_A f$$

이 잘 정의된다. 특히 만일 $E$가 flat $A$-module이고 $M$이 finitely presented라면 $\alpha$는 isomorphism이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$\alpha$가 잘 정의된다는 것은 자명하다. 이제 $E$가 flat $A$-module이고 $M=A$라 하자. 그럼 주어진

$$\alpha: E\otimes_A\Hom_A(A, N) \rightarrow\Hom_E(E\otimes_AM, E\otimes_AN)$$

은 사실 다음의 commutative diagram

![simplest_case](/assets/images/Math/Commutative_Algebra/Properties_of_localization-1.png){:width="450px" class="invert" .align-center}

에 넣을 수 있으므로 주어진 명제가 성립한다. 여기서 수직 방향 함수는 각각 isomorphism 

$$\Hom_A(A,N)\cong N,\qquad \Hom_E(E\otimes_A,E\otimes_AN)\cong\Hom_E(E,E\otimes_AN)\cong E\otimes_AN$$

에서 온 것들이다. 그 후, $\Hom$과 $\otimes$는 유한한 direct sum과 commute하므로 이 명제는 flat $A$-module $E$와 임의의 finitely generated free $A$-module $M$에 대해서도 성립하며, 마지막으로 $M$이 finitely presented인 경우는 다음의 free presentation

$$F \rightarrow G \rightarrow M \rightarrow 0$$

을 잡은 후, 다음의 commutative diagram

![general_case](/assets/images/Math/Commutative_Algebra/Properties_of_localization-2.png){:width="942px" class="invert" .align-center}

에 four lemma를 사용하면 충분하다. 

</details>

## 가군들의 chain

우리는 앞서 noetherian ring을 ascending chain condition을 만족하는 ring으로 정의했는데, 비슷하게 artinian ring은 descending chain condition을 만족하는 ring으로 정의된다. 즉 임의의 ideal들의 descending chain

$$\mathfrak{a}_0\supseteq \mathfrak{a}_1\supseteq\cdots$$

이 주어진다면 적당한 $k$가 존재하여 $\mathfrak{a}\_k$ 이후의 ideal들은 모두 $\mathfrak{a}\_k$와 같아야 한다. 

위의 chain condition을 더 일반화하기 위해 다음을 정의한다. 

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> $A$-module $M$이 *simple<sub>단순</sub>*이라는 것은 $M\neq 0$이며, $M$의 submodule이 오직 $0$과 $M$ 뿐인 것이다.

</div>

Simple module은 반드시 하나의 원소 $x\in M$으로 생성되어야 함이 자명하지만 $\mathbb{Z}/6\mathbb{Z}$를 생각하면 그 역은 성립하지 않는다. 한편 simple module $M$이 $x$로 생성된다면, $A$-module homomorphism $A \rightarrow M$을 $1\mapsto x$로 주면 isomorphism

$$A/\ann(M)=A/\ann(x)\cong M$$

을 얻는다. 만일 $\ann(M)$이 maximal ideal이 아니라면, $\ann(M)$을 포함하는 $A$의 maximal ideal $\mathfrak{m}$에 대하여 $\mathfrak{m}/\ann(M)$이 $M$의 submodule이 될 것이므로 $\ann(M)$은 반드시 $A$의 maximal ideal이 되어야 함도 자명하다. 

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> $A$-module $M$을 고정하자. $M$의 submodule들의 decreasing sequence

$$M=M_0\supsetneq M_1\supsetneq \cdots\supsetneq M_n=0$$

을 길이 $n$의 chain이라 부른다. 이 chain이 *composition series<sub>합성열</sub>*이라는 것은 모든 $k$에 대하여 $M_k/M_{k+1}$이 simple module인 것이다. 이러한 composition series들의 길이 중 가장 작은 것을 $M$의 *length<sub>길이</sub>*라 부르고 $\length(M)$으로 적는다. 만일 $M$의 composition series가 존재하지 않는다면 $\length(M)=\infty$로 정의한다. 

</div>

그럼 다음 정리는 module 버전의 Jordan-Hölder 정리라 할 수 있다. 

<div class="proposition" markdown="1">

<ins id="thm8">**정리 8**</ins> $A$-module $M$이 유한한 composition series를 갖는 것은 $M$이 artinian인 동시에 noetherian인 것과 동치이다. 이 조건이 만족되어 길이 $n$짜리 composition series

$$M=M_0\supsetneq M_1\supsetneq \cdots\supsetneq M_n=0$$

가 주어졌다 하자. 그럼 다음이 성립한다. 

1. 길이가 $n$ 이하인 $M$의 임의의 submodule들의 chain들은 모두 composition series로의 refinement를 갖는다. 
2. $M_k/M_{k+1}\cong A/\mathfrak{m}$이도록 하는 $k$가 존재하는 maximal ideal들의 모임에 대하여, isomorphism $M\cong\bigoplus_{\mathfrak{m}}M_\mathfrak{m}$이 존재한다. 
3. 만일 어떤 $k$에 대하여 $\mathfrak{p}^k$가 $M$을 annihilate한다면 $M=M_\mathfrak{p}$이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $M$이 artinian인 동시에 noetherian이라 하자. 우선 $M$이 noetherian이라는 조건으로부터 $M$의 적당한 maximal proper submodule $M_1$을 찾을 수 있다. 한편 noetherian module의 submodule은 반드시 noetherian이어야 함이 자명하므로, 이를 반복하여 $M_k$의 maximal proper submodule $M_{k+1}$을 찾을 수 있다. 그런데 이렇게 정의한 chain 

$$M=M_0\supsetneq M_1\supsetneq \cdots$$

은 artinian 조건으로부터 그 길이가 유한하며, $M_{k+1}$이 $M_k$의 maximal proper submodule인 것으로부터 이 chain이 composition series임을 안다. 

첫 번째 결과는 Jordan-Hölder 정리와 동일하게 증명하므로 별도로 증명하지 않는다. 이제 이를 받아들이고 나면, 임의의 chain이 주어질 때마다 이 chain을 composition series로 refine할 수 있고, 따라서 앞선 동치관계의 반대 방향까지 보일 수 있다.

이제 두 번째 결과를 보인다. 주어진 chain의 유한성으로부터 조건을 만족하는 maximal ideal들 또한 유한하다는 것을 알고, 따라서 $\bigoplus_\mathfrak{m} M_\mathfrak{m}$은 $\prod_\mathfrak{m} M_\mathfrak{m}$으로 볼 수 있으며 이 때 주어진 함수는 $M \rightarrow M_\mathfrak{m}$들에 direct product의 universal property를 적용하여 얻어진다. 이 함수가 isomorphism이 된다는 것을 보이려면 [명제 4](#prop4)를 적용하여 maximal ideal에서의 localization을 보면 충분하다. 

이를 위해 우선 $M\cong R/\mathfrak{m}$이라면 임의의 maximal ideal $\mathfrak{m}'$에 대하여

$$M_{\mathfrak{m}'}=\begin{cases}M&\text{if $\mathfrak{m}=\mathfrak{m}'$,}\\0&\text{otherwise.}\end{cases}$$

이다. 이로부터 $M$의 composition series

$$M=M_0\supsetneq M_1\supsetneq \cdots\supsetneq M_n=0$$

가 주어졌다면, 이를 maximal ideal $\mathfrak{m}$에서 localization을 하면 

$$M_\mathfrak{m}=(M_0)_\mathfrak{m}\supsetneq (M_1)_\mathfrak{m}\supsetneq \cdots\supsetneq (M_n)_\mathfrak{m}=0$$

을 얻는다. 그런데 localization functor가 exact functor인 것과 ([명제 2](#prop2)) 방금 전의 계산을 종합하면, 

$$(M_k)_\mathfrak{m}/(M_{k+1})_\mathfrak{m}\cong (M_k/M_{k+1})_\mathfrak{m}=\begin{cases}M_k/M_{k+1}&\text{if $M_k/M_{k+1}\cong A/\mathfrak{m}$,}\\0&\text{otherwise}\end{cases}$$

이 성립한다. 이로부터 두 번째 결과를 얻으며, 세 번째 결과는 위의 계산과 유사하게 증명할 수 있다.

</details>

## 아틴환과 뇌터환의 성질들

다음 두 정리는 분량의 문제로 증명을 생략한다. 

<div class="proposition" markdown="1">

<ins id="thm9">**정리 9**</ins> Ring $A$에 대해 다음이 모두 동치이다.

1. $A$가 noetherian이고 임의의 prime ideal이 maximal이다.
2. $A$는 $A$-module로서 유한한 길이를 갖는다.
3. $A$는 artinian이다.

</div>

이로부터 임의의 artinian ring은 local artinian ring들의 유한한 product임을 보일 수 있다. Noetherian ring에 대해서는 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="thm10">**정리 10**</ins> Noetherian ring $A$에 대하여, $A$가 domain들의 유한한 product인 것은 $A$의 임의의 maximal ideal에 대하여 $A_\mathfrak{m}$이 domain인 것과 동치이다.

</div>