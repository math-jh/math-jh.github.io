---

title: "조르단-횔더 정리"
excerpt: ""

categories: [Math / Commutative Algebra]
permalink: /ko/math/commutative_algebra/Jordan-Holder_theorem
header:
    overlay_image: /assets/images/Math/Commutative_Algebra/Jordan-Holder_theorem.png
    overlay_filter: 0.5
sidebar: 
    nav: "commutative_algebra-ko"

date: 2024-10-22
last_modified_at: 2024-10-22
weight: 5

---


## Jordan-Hölder 정리

이제 다음을 정의한다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $A$-module $M$이 *simple<sub>단순</sub>*이라는 것은 $M\neq 0$이며, $M$의 submodule이 오직 $0$과 $M$ 뿐인 것이다.

</div>

Simple module은 반드시 하나의 원소 $x\in M$으로 생성되어야 함이 자명하지만 $\mathbb{Z}/6\mathbb{Z}$를 생각하면 그 역은 성립하지 않는다. 한편 simple module $M$이 $x$로 생성된다면, $A$-module homomorphism $A \rightarrow M$을 $1\mapsto x$로 주면 isomorphism

$$A/\ann(M)=A/\ann(x)\cong M$$

을 얻는다. 만일 $\ann(M)$이 maximal ideal이 아니라면, $\ann(M)$을 포함하는 $A$의 maximal ideal $\mathfrak{m}$에 대하여 $\mathfrak{m}/\ann(M)$이 $M$의 submodule이 될 것이므로 $\ann(M)$은 반드시 $A$의 maximal ideal이 되어야 함도 자명하다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> $A$-module $M$을 고정하자. $M$의 submodule들의 decreasing sequence

$$M=M_0\supsetneq M_1\supsetneq \cdots\supsetneq M_n=0$$

을 길이 $n$의 chain이라 부른다. 이 chain이 *composition series<sub>합성열</sub>*이라는 것은 모든 $k$에 대하여 $M_k/M_{k+1}$이 simple module인 것이다. 이러한 composition series들의 길이 중 가장 작은 것을 $M$의 *length<sub>길이</sub>*라 부르고 $\length(M)$으로 적는다. 만일 $M$의 composition series가 존재하지 않는다면 $\length(M)=\infty$로 정의한다. 

</div>

그럼 다음 정리는 module 버전의 Jordan-Hölder 정리라 할 수 있다. 

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3**</ins> $A$-module $M$이 유한한 composition series를 갖는 것은 $M$이 artinian인 동시에 noetherian인 것과 동치이다. 이 조건이 만족되어 길이 $n$짜리 composition series

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

이제 두 번째 결과를 보인다. 주어진 chain의 유한성으로부터 조건을 만족하는 maximal ideal들 또한 유한하다는 것을 알고, 따라서 $\bigoplus_\mathfrak{m} M_\mathfrak{m}$은 $\prod_\mathfrak{m} M_\mathfrak{m}$으로 볼 수 있으며 이 때 주어진 함수는 $M \rightarrow M_\mathfrak{m}$들에 direct product의 universal property를 적용하여 얻어진다. 이 함수가 isomorphism이 된다는 것을 보이려면 [§국소화의 성질들, ⁋명제 4](/ko/math/commutative_algebra/properties_of_localization#prop4)를 적용하여 maximal ideal에서의 localization을 보면 충분하다. 

이를 위해 우선 $M\cong R/\mathfrak{m}$이라면 임의의 maximal ideal $\mathfrak{m}'$에 대하여

$$M_{\mathfrak{m}'}=\begin{cases}M&\text{if $\mathfrak{m}=\mathfrak{m}'$,}\\0&\text{otherwise.}\end{cases}$$

이다. 이로부터 $M$의 composition series

$$M=M_0\supsetneq M_1\supsetneq \cdots\supsetneq M_n=0$$

가 주어졌다면, 이를 maximal ideal $\mathfrak{m}$에서 localization을 하면 

$$M_\mathfrak{m}=(M_0)_\mathfrak{m}\supsetneq (M_1)_\mathfrak{m}\supsetneq \cdots\supsetneq (M_n)_\mathfrak{m}=0$$

을 얻는다. 그런데 localization functor가 exact functor인 것과 ([§국소화의 성질들, ⁋명제 2](/ko/math/commutative_algebra/properties_of_localization#prop2)) 방금 전의 계산을 종합하면, 

$$(M_k)_\mathfrak{m}/(M_{k+1})_\mathfrak{m}\cong (M_k/M_{k+1})_\mathfrak{m}=\begin{cases}M_k/M_{k+1}&\text{if $M_k/M_{k+1}\cong A/\mathfrak{m}$,}\\0&\text{otherwise}\end{cases}$$

이 성립한다. 이로부터 두 번째 결과를 얻으며, 세 번째 결과는 위의 계산과 유사하게 증명할 수 있다.

</details>

## 아틴환과 뇌터환의 성질들

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4**</ins> Ring $A$에 대해 다음이 모두 동치이다.

1. $A$가 noetherian이고 임의의 prime ideal이 maximal이다.
2. $A$는 $A$-module로서 유한한 길이를 갖는다.
3. $A$는 artinian이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>

이로부터 임의의 artinian ring은 local artinian ring들의 유한한 product임을 보일 수 있다. Noetherian ring에 대해서는 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5**</ins> Noetherian ring $A$에 대하여, $A$가 domain들의 유한한 product인 것은 $A$의 임의의 maximal ideal에 대하여 $A_\mathfrak{m}$이 domain인 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>