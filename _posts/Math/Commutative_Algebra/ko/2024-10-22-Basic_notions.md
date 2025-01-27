---

title: "기본 개념들"
excerpt: ""

categories: [Math / Commutative Algebra]
permalink: /ko/math/commutative_algebra/basic_notions
header:
    overlay_image: /assets/images/Math/Commutative_Algebra/Basic_notions.png
    overlay_filter: 0.5
sidebar: 
    nav: "commutative_algebra-ko"

date: 2024-10-22
last_modified_at: 2024-10-22
weight: 1

---

이 카테고리의 모든 글에서 등장하는 ring은 commutative ring이다. 또, 임의의 $A$-algebra는 항상 commutative associative unital $A$-algebra인 것으로 생각한다. 

## 기본 정의들

이 카테고리에서는 commutative ring $A$와 그 위에 정의된 module $M$에 대해 살펴본다. Ring $A$의 임의의 ideal $\mathfrak{a}$는 항상 $A$-module로 생각할 수 있으므로 많은 경우 우리는 $A$-module에 대한 이론을 전개하게 된다. 앞서 [\[대수적 구조\]](/ko/algebraic_structures/) 카테고리의 글들에서는 혼동을 방지하기 위해 $A$-module $M$의 원소를 $x,y,\ldots$으로, $A$의 원소를 $\alpha,\beta,\ldots$로 썼었는데, $\mathfrak{a}$도 $A$-module로 생각하면 이와 같이 표기법을 구분하는 것이 오히려 더 혼란을 주게 되므로, 이 카테고리에서는 이와 같은 구분을 하지 않는다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 임의의 $A$-module $M$에 대하여, $M$의 *annihilator<sub>소멸자</sub>* $\ann(M)$을 다음 식

$$\ann(M)=\{a\in A: aM=0\}$$

으로 정의한다. 

</div>

한편, ring $A$의 두 ideal $\mathfrak{a},\mathfrak{b}$에 대하여 *ideal quotient<sub>아이디얼 몫</sub>* $(\mathfrak{a}:\mathfrak{b})$를 다음 식

$$(\mathfrak{a}:\mathfrak{b})=\{a\in A: a\mathfrak{b}\subseteq \mathfrak{a}\}$$

으로 정의하고, 비슷하게 $A$-module $M$의 두 submodule $N_1,N_2$에 대하여는

$$(N_1:N_2)=\{a\in A: aN_2\subseteq N_1\}$$

으로 정의한다. Ideal quotient $(\mathfrak{a}:\mathfrak{b})$는 대략적으로 $\mathfrak{a}/\mathfrak{b}$ 정도로 생각할 수 있으며, 임의의 $A$-module $M$에 대하여 $\ann(M)=(0:M)$이다. 

한편 우리는 [\[다중선형대수학\] §완전열, ⁋명제 7](/ko/math/multilinear_algebra/exact_sequences#prop7)에서 유용한 두 개의 short exact sequence를 살펴보았는데, 여기에 다음의 short exact sequence

$$0 \longrightarrow A/(\mathfrak{a}:(a)) \overset{a}{\longrightarrow} A/\mathfrak{a}\longrightarrow A/(\mathfrak{a}+(a)) \longrightarrow 0$$

을 추가하여 기억할 가치가 있다. 첫 번째 함수 $A/(\mathfrak{a}:(a)) \rightarrow A/\mathfrak{a}$는 다음의 식

$$x+(\mathfrak{a}:(a))\mapsto ax+\mathfrak{a}$$

로 주어지며, 이것이 잘 정의된다는 것은

$$y\in (\mathfrak{a}:(a))\iff ay\in \mathfrak{a}$$

인 것으로부터 자명하다. 이제 두 번째 함수 $A/\mathfrak{a} \rightarrow A/(\mathfrak{a}+(a))$는 다음의 식

$$x+\mathfrak{a}\mapsto x+(\mathfrak{a}+(a))$$

으로 정의되며, 이것이 surjective이고 그 kernel이 정확히 $a+\mathfrak{a}$로 생성되는 $A/\mathfrak{a}$의 submodule인 것을 확인할 수 있다.

## Finiteness condition

많은 경우 우리는 어떤 종류의 유한성을 가정하게 된다. 가령 [\[다중선형대수학\]](/ko/multilinear_algebra)의 글들에서 우리는 주어진 module이 finitely generated $A$-module임을 가정하고, basis를 택함으로써 많은 계산을 행렬의 계산으로 줄일 수 있었다. 비슷한 맥락에서 우리가 자주 사용할 유한성의 개념들을 정의한다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 임의의 $A$-module $M$이 *ascending chain condition<sub>오름사슬조건</sub>*을 만족한다는 것은 $M$의 임의의 submodule들의 increasing sequence

$$M_0\subseteq M_1\subseteq M_2\subseteq\cdots$$

가 주어질 때마다, 적당한 $k$가 존재하여 $M_k=M_{k+1}=\cdots$인 것이다. 비슷하게 $M$이 *descending chain condition<sub>내림사슬조건</sub>*을 만족한다는 것은 $M$의 임의의 submodule들의 decreasing sequence

$$M_0\supseteq M_1\supseteq M_2\supseteq\cdots$$

가 주어질 때마다, 적당한 $k$가 존재하여 $M_k=M_{k+1}=\cdots$인 것이다. Ascending chain condition을 만족하는 $A$-module $M$을 *noetherian<sub>뇌터가군</sub>*이라 부른다. Descending chain condition을 만족하는 $A$-module $M$을 *artinian<sub>아틴가군</sub>*이라 부른다. 임의의 ring $A$가 noetherian 혹은 artinian인 것은 $A$가 자기 자신 위에서의 module로서 noetherian 혹은 artinian인 것이다.

</div>

그럼 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3**</ins> 임의의 $A$-module $M$에 대하여 다음이 모두 동치이다.

1. $M$이 noetherian이다.
2. $M$의 임의의 submodule이 finitely generated이다.
3. 임의의 $M$의 submodule들의 모임은 항상 포함관계에 대한 maximal element를 갖는다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 1번 조건을 가정하고 2번 조건을 보인다. 결론에 반하여 $M$이 finitely generated가 아닌 submodule $N$을 갖는다 가정하자. 그럼 $N$의 임의의 원소 $x_0\neq 0$을 택할 수 있으며, $N$이 finitely generated가 아니라는 사실로부터 $N\neq \langle x_1\rangle$이므로 $x_2\in N\setminus \langle x_1\rangle$을 택할 수 있다. 이를 계속 반복하여 $N$의 submodule들의 increasing sequence
  
$$\langle x_1\rangle\subsetneq \langle x_2\rangle\subsetneq\cdots$$

를 얻으며, 이들은 $M$의 submodule이기도 하므로 $M$이 noetherian이라는 가정에 모순이다.

이제 2번 조건을 가정하고 1번 조건을 보인다. $M$의 submodule들의 ascending chain

$$M_0\subseteq M_1\subseteq M_2\subseteq\cdots$$

이 주어졌다 하고 $M'=\bigcup M_k$라 하면 $M'$은 finitely generated이므로 $M'=\langle x_1,\ldots, x_n\rangle$이라 하자. 그럼 이제 각각의 $i$에 대하여, $k\_i$를 $x\_i\in N\_{k\_i}$가 성립하도록 잡을 수 있고 이제 이러한 $k_i$들 중 가장 큰 것은 반드시 $M'$과 같게 된다.

이제 1번 조건과 3번 조건이 동치임을 보인다. 우선 1번 조건이 만족된다면 이는 $M$의 임의의 submodule들의 모임이 주어질 때마다 ACC에 의하여 [\[집합론\] §선택공리, ⁋정리 4](/ko/math/set_theory/axiom_of_choice#thm4)의 전제조건이 만족되므로 3번이 성립하는 것이 자명하다. 거꾸로 3번 조건을 만족할 경우, $M$의 submodule들의 ascending chain

$$M_0\subseteq M_1\subseteq M_2\subseteq\cdots$$

이 주어졌을 때 이들 모임의 maximal element가 존재해야 하므로 1번 조건이 성립한다. 

</details>

따라서 noetherian module의 임의의 submodule 또한 noetherian임이 자명하다. 뿐만 아니라 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> Noetherian $A$-module $M$에 대하여, 임의의 quotient $M/N$ 또한 noetherian이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$M/N$의 임의의 submodule은 $M$의 적당한 submodule $L$에 대하여 $L/N$의 꼴이고, 이제 $L$이 finitely generated이며 canonical surjection에 의하여 $L$의 generator들이 $L/N$을 generate하므로 자명하다.

</details>

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> 임의의 $A$-module $M$과 임의의 submodule $N$에 대하여, $M$이 noetherian인 것과 $N,M/N$이 모두 noetherian인 것이 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

한쪽 방향은 이미 증명하였다. 따라서 $N, M/N$이 noetherian이라 가정하고 $M$이 noetherian임을 보이면 충분하다. $M$의 임의의 submodule $L$을 고정하자. 그럼 $L$의 $M/N$에서의 image $L/N$은 finitely generated이며, $L\cap N$ 또한 $N$의 submodul이므로 finitely generated이다. 이제 $x_1,\ldots, x_m\in L$을 $L/N$으로 보낸 것이 $L/N$의 generator가 된다 하고, $y_1,\ldots, y_n\in L\cap N$이 $L\cap N$의 generator라 하자. 그럼 임의의 $x\in L$에 대하여 

$$x\equiv \alpha_1x_1+\cdots+\alpha_m x_m\pmod{N}$$

이도록 하는 $\alpha_i\in A$들이 존재한다. 따라서 

$$x-\sum \alpha_i x_i\in L\cap N$$

이고, 이를 다시 $L\cap N$의 generator를 이용하여 적어주면 원하는 결과를 얻는다.

</details>

따라서 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="cor6">**따름정리 6**</ins> Ring $A$와 두 noetherian $A$-module $M,N$에 대하여, $M\oplus N$은 noetherian $A$-module이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[명제 5](#prop5)를 $M\oplus N$과 그 submodule $M\oplus 0\cong M$에 대해 적용하면 된다.

</details>

[\[다중선형대수학\]](/ko/multilinear_algebra) 카테고리에서 살펴보았던 finitely generated $A$-module의 조건은 다음의 exact sequence

$$A^{\oplus n} \rightarrow M \rightarrow 0$$

이 존재한다는 것이고, 이 때 $A^{\oplus n}$의 basis의 image $x_1,\ldots, x_n$가 $M$을 generate하게 된다. 그러나 일반적으로 $M$을

$$M=\langle x_1,\ldots, x_n\mid \text{relations on $x_i$}\rangle$$

으로 적었을 때, $x_i$들에 대한 relation은 무한히 많을 수 있다. 이들 relation은 surjection $A^{\oplus n} \rightarrow M$의 kernel에 의해 결정되므로, 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> $A$-module $M$이 *finitely presented<sub>유한표시가군</sub>*라는 것은 적당한 $m,n$이 존재하여 다음의 exact sequence

$$A^{\oplus m} \rightarrow A^{\oplus n} \rightarrow M \rightarrow 0$$

이 존재하는 것이다. 

</div>

일반적으로 finitely presented module은 finitely generated이지만, 그 역은 성립하지 않는다. 하지만 임의의 noetherian ring $A$에 대해서는 두 개념이 일치한다. 이는 만일 $M$이 finitely generated $A$-module이라면, 다음의 exact sequence

$$0\longrightarrow\ker u \longrightarrow A^{\oplus n} \overset{u}{\longrightarrow} M \longrightarrow 0$$

를 얻고, 한편 $A^{\oplus n}$은 [따름정리 6](#cor6)에 의하여 noetherian이며 따라서 그 submodule $\ker u$는 finitely generated이다. 이제

$$A^{\oplus m} \rightarrow \ker u \rightarrow 0$$

을 생각한 후, 합성 $A^{\oplus m} \rightarrow \ker \rightarrow A^{\oplus n}$을 사용하면 다음의 exact sequence

$$A^{\oplus m} \rightarrow A^{\oplus n} \rightarrow M \rightarrow 0$$

을 얻는다. 한편 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> $A$-module $M$이 *coherent module<sub>연접가군</sub>*이라는 것은 $M$이 finitely generated이고, 임의의 $A$-linear map $A^{\oplus n} \rightarrow M$이 주어질 때마다 이 linear map의 kernel이 finitely generated인 것이다.

</div>

그럼 다음 명제가 자명하다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> Noetherian ring $A$와 $A$-module $M$에 대하여, 다음이 모두 동치이다.

1. $M$이 finitely generated이다.
2. $M$이 finitely presented이다.
3. $M$이 coherent이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

1번 조건과 2번 조건이 동치인 것은 이미 살펴보았다. 또, 정의에 의해 coherent $A$-module은 항상 finitely generated이다. 따라서 $M$이 finitely generated인 것을 가정하고 $M$이 coherent라는 것을 보이면 충분하다. 이는 임의의 $A$-linear map $A^{\oplus n}\rightarrow M$이 주어졌을 때, 이 linear map의 kernel은 $A^{\oplus n}$의 submodule이고, 여기에 [명제 5](#prop5)를 적용하여 얻어진다.

</details>

## 소아이디얼

마지막으로 우리는 [\[대수적 구조\] §분수체, ⁋명제 8](/ko/math/algebraic_structures/field_of_fractions#prop8)에서 정의한 *prime ideal*의 개념이 필요하다. 

<div class="definition" markdown="1">

<ins id="def10">**정의 10**</ins> Ring $A$의 ideal $\mathfrak{p}\subsetneq A$가 *prime ideal*이라는 것은, 만일 $ab\in \mathfrak{p}$라면 반드시 $a\in \mathfrak{p}$이거나 $b\in \mathfrak{p}$가 성립하는 것이다.

</div>

그럼 우리는 [\[대수적 구조\] §몫환, 환 동형사상, ⁋정리 3](/ko/math/algebraic_structures/quotient_rings#thm3)의 넷째 결과를 더 다듬어서 다음을 보일 수 있다.

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> Ring $A$의 임의의 ideal $\mathfrak{a}$에 대하여, $A/\mathfrak{a}$의 prime ideal과, $A$의 prime ideal 중 $\mathfrak{a}$을 포함하는 것들 사이의 일대일대응이 존재한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[\[대수적 구조\] §몫환, 환 동형사상, ⁋정리 3](/ko/math/algebraic_structures/quotient_rings#thm3)의 셋째 결과에 의하여, $\mathfrak{a}\subseteq \mathfrak{p}\subseteq A$에 대하여

$$A/\mathfrak{p}\cong \frac{A/\mathfrak{a}}{\mathfrak{p}/\mathfrak{a}}$$

이 성립하며, 그 후 [\[대수적 구조\] §분수체, ⁋명제 8](/ko/math/algebraic_structures/field_of_fractions#prop8)의 동치조건을 사용하면 된다. 

</details>

---

**참고문헌**

**[Eis]** David Eisenbud. *Commutative Algebra: with a view toward algebraic geometry*. Springer, 1995.

---