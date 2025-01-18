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
2. $A$는 $A$-module로서 유한한 length를 갖는다.
3. $A$는 artinian이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 첫째 조건을 가정하고 둘째 조건을 보이자. 결론에 반하여 $A$가 첫째 조건을 만족하지만, finite length가 아니라 하자. 이제 $\mathfrak{a}$를 $A/\mathfrak{a}$가 finite length가 아니도록 하는 $A$의 ideal들 중 maximal인 것이라 하자. 그럼 만일 $ab\in \mathfrak{a}$이고 $a\not\in \mathfrak{a}$라면, 다음의 short exact sequence

$$0\longrightarrow A/(\mathfrak{a}:a)\overset{a}{\longrightarrow}A/\mathfrak{a}\longrightarrow A/(\mathfrak{a}+(a))\longrightarrow 0$$

을 생각할 수 있다. ([§기본 개념들, §§기본 정의들](/ko/math/commutative_algebra/basic_notions#기본-정의들)) 이제 $\mathfrak{a}+(a)$는 $\mathfrak{a}$를 strict하게 포함하는 ideal이므로, 정의에 의해 $A/(\mathfrak{a}+(a))$는 finite length여야 한다. 한편 정의로부터 $\mathfrak{a}\subseteq (\mathfrak{a}:(a))$인데, 만일 $b\not\in \mathfrak{a}$라면 $\mathfrak{a}\subsetneq (\mathfrak{a}:(a))$가 되므로, 마찬가지로 $\mathfrak{a}$의 정의에 의해 $A/(\mathfrak{a}:a)$는 finite lenngth여야 한다. 따라서 이들 composition series들을 통해 $A/\mathfrak{a}$의 composition series를 얻고, 이는 $A$가 finite length가 아니라는 가정에 모순이므로 $b\in \mathfrak{a}$이다. 즉 $\mathfrak{a}$는 prime ideal이다. 이제 1번 조건의 가정에 의해 $\mathfrak{a}$는 maximal이므로, $A/\mathfrak{a}$는 field이고 이는 $A/\mathfrak{a}$가 finite length가 아니라는 가정에 다시 모순이므로 원하는 결과를 얻는다.

이제 둘째 조건을 가정하면 셋째 조건은 [정리 3](#thm3)으로부터 자명하다. 따라서 셋째 조건을 가정하고 첫째 조건을 보이면 충분하다. 이를 위해 $A$의 maximal ideal들의 곱으로 얻어지는 ideal들의 모임을 생각하자. 그럼 $A$가 artinian이므로, 이 모임에서의 minimal한 ideal $\mathfrak{a}$가 존재한다. 그럼 $\mathfrak{a}=0$이고, 따라서 zero ideal은 maximal ideal들의 곱 $0=\mathfrak{m}\_1\cdots\mathfrak{m}\_k$으로 적을 수 있다. 

이 주장을 보이기 위해 우선, 임의의 maximal ideal $\mathfrak{m}$에 대하여, $\mathfrak{a}$의 minimality는 임의의 maximal ideal $\mathfrak{m}$에 대하여 $\mathfrak{m}\mathfrak{a}=\mathfrak{a}$인 것을 의미한다는 것을 관찰하자. 즉, $\mathfrak{a}\subseteq \mathfrak{m}$이다. 비슷한 논리로 $\mathfrak{a}^2$는 maximal ideal들의 곱이므로 $\mathfrak{a}^2=\mathfrak{a}$도 성립한다. 이제 결론에 반하여 $\mathfrak{a}\neq 0$이라 가정하면, $\mathfrak{a}\mathfrak{b}\neq 0$이도록 하는 ideal이 존재하며, 다시 $A$가 artinian이라는 가정으로부터 $\mathfrak{b}$를 이러한 성질을 만족하는 ideal들 중 minimal한 것으로 택할 수 있다. 그럼

$$(\mathfrak{b}\mathfrak{a})\mathfrak{a}=\mathfrak{b}\mathfrak{a}^2=\mathfrak{b}\mathfrak{a}\neq 0$$

이므로, $\mathfrak{b}$의 minimality로부터 $\mathfrak{b}\mathfrak{a}=\mathfrak{b}$여야 함을 안다.

이제 $\mathfrak{b}$의 정의로부터, 적당한 $y\in \mathfrak{b}$에 대해 $y \mathfrak{a}\neq 0$이여야 함을 알고, $\mathfrak{b}$의 minimality로부터 $\mathfrak{b}=(y)$여야 함을 안다. 이제 위의 등식 $\mathfrak{b}\mathfrak{a}=\mathfrak{b}$로부터 적당한 $x\in \mathfrak{a}$에 대하여 $xy=y$가 성립해야 함을 안다. 즉, $(1-x)y=0$이어야 한다. 그런데 $x\in \mathfrak{a}$이고, $\mathfrak{a}$는 임의의 maximal ideal에 포함되므로 $1-x$는 어떠한 maximal ideal에도 포함되지 않는다. 즉 $1-x$는 unit이며, 이로부터 $y=0$이고 이는 $\mathfrak{b}$의 정의에 모순이다. 즉, $\mathfrak{a}=0$이고 따라서 zero ideal을 maximal ideal들의 곱 $0=\mathfrak{m}\_1\cdots\mathfrak{m}\_k$으로 적을 수 있다. 

이제 각각의 $l=1,\ldots, k-1$에 대하여, $\mathfrak{m}\_1\cdots\mathfrak{m}\_l/\mathfrak{m}\_1\cdots\mathfrak{m}\_{l+1}$을 $A/\mathfrak{m}\_{l+1}$-vector space로 보면 이 vector space의 submodule은 $\mathfrak{a}/\mathfrak{m}\_1\cdots\mathfrak{m}\_{l+1}$ 꼴의 submodule, 즉 $A$의 ideal 중 $\mathfrak{m}\_1\cdots\mathfrak{m}\_{l+1}$를 포함하는 ideal로 생각할 수 있으며, $A$는 artinian이므로 이로부터 $\mathfrak{m}\_1\cdots\mathfrak{m}\_l/\mathfrak{m}\_1\cdots\mathfrak{m}\_{l+1}$가 유한차원임을 안다. 이제 이들을 모두 모아두면 $A$의 composition series를 얻고, 따라서 [정리 3](#thm3)에 의해 $A$는 noetherian이다. 

남은 조건을 보이기 위해 $A$의 임의의 prime ideal $\mathfrak{p}$를 택하면,

$$\mathfrak{m}_1\cdots\mathfrak{m}_k=0\subseteq \mathfrak{p}$$

인 것으로부터 어떠한 $l$에 대해서는 $\mathfrak{m}\_l\subseteq \mathfrak{p}$가 성립해야 함을 알고 따라서 $\mathfrak{m}\_l=\mathfrak{p}$이다. 이로부터 첫째 조건이 모두 성립한다.

</details>

이로부터 임의의 artinian ring은 local artinian ring들의 유한한 product임을 보일 수 있다. Noetherian ring에 대해서는 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5**</ins> Noetherian ring $A$에 대하여, $A$가 domain들의 유한한 product인 것은 $A$의 임의의 maximal ideal에 대하여 $A_\mathfrak{m}$이 domain인 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $A$가 domain의 유한한 product $A=\prod A_i$라 하자. 그럼 $A$의 임의의 prime ideal은 $A_i$의 unit $e_i$를 포함할 수 없으므로 multiplicative subset에 들어가며, 이 원소 $e_i$는 $i\neq j$를 만족하는 $A_j$를 annihilate하므로 $A=(A_i)_\mathfrak{p}$이 성립한다. ([§국소화, ⁋명제 5](/ko/math/commutative_algebra/localization#prop5))

거꾸로 $A$의 임의의 maximal ideal $\mathfrak{m}$에서의 localization이 domain이라 가정하고, $\\{\mathfrak{q}\_i\\}$를 $A$의 prime ideal들 중 minimal한 것이라 하자. 그럼 다음 글에서 증명할 [§동반소아이디얼, ⁋정리 7](/ko/math/commutative_algebra/associated_primes#thm7)에 의하여 $\\{\mathfrak{q}\_i\\}$는 유한집합이며, 이를 받아들이고 나면 $A$에서 유한히 많은 domain들의 direct product로의 자연스러운 map

$$A \rightarrow \prod_{i\in I} A/\mathfrak{q}_i$$

이 존재한다. 이제 이 map이 isomorphism임을 보이자. 이는 [§국소화의 성질들, ⁋명제 4](/ko/math/commutative_algebra/properties_of_localization#prop4)에 의하여 임의의 maximal ideal에서 localization을 하여 다음의 map

$$A_\mathfrak{m} \rightarrow \left(\prod_{i\in I} A/\mathfrak{q}_i\right)_\mathfrak{m}$$

이 isomorphism임을 보이면 충분하다. 한편, [§국소화, ⁋명제 8](/ko/math/commutative_algebra/localization#prop8)에 의하여 $A$의 minimal prime ideal 중 $\mathfrak{m}$에 속하는 것과, $A_\mathfrak{m}$의 minimal prime ideal 사이의 일대일 대응이 존재한다. 그런데 가정에 의하여 $A_\mathfrak{m}$은 domain이므로, $A_\mathfrak{m}$은 유일한 minimal prime ideal $(0)$을 가지고, 따라서 $\mathfrak{q}_i$ 중 오직 하나만이 $\mathfrak{m}$에 속한다. 이제 이로부터

$$\left(\prod_{i\in I} A/\mathfrak{q}_i\right)_\mathfrak{m}=(A/\mathfrak{q}_i)_\mathfrak{m}=A_\mathfrak{m}$$

이므로, 위의 map이 isomorphism이 된다.

</details>

<div class="proposition" markdown="1">

<ins id="cor6">**따름정리 6**</ins> Noetherian ring $A$와 finiely generated $A$-module $M$에 대하여, 다음이 모두 동치이다. 

1. $M$이 유한한 길이를 갖는다.
2. 적당한 maximal ideal들의 곱 $\prod_{i=1}^n \mathfrak{m}\_i$가 $M$을 annihilate한다.
3. $\ann(M)$을 포함하는 prime ideal들이 maximal이다.
4. $A/\ann(M)$이 Artinian이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 첫째 조건을 가정하면 [정리 3](#thm3)의 두 번째와 세 번째 결과로부터 두 번째 조건이 성립하는 것이 자명하다. 이제 두 번째 조건을 가정하자. 그럼 $\ann(M)$을 포함하는 임의의 prime ideal $\mathfrak{p}$에 대하여, $\mathfrak{p}\supseteq\prod \mathfrak{m}\_i$이므로 어떠한 $i$에 대하여 $\mathfrak{p}\supseteq \mathfrak{m}_i$이고, 따라서 $\mathfrak{p}=\mathfrak{m} 
_i$이다. 세 번째 조건이 네 번째 조건을 함의하는 것은 [정리 4](#thm4)의 첫째 조건과 셋째 조건의 동치이며, 마지막으로 네 번째 조건을 가정하면 $A/\ann(M)$은 [정리 4](#thm4)의 둘째 조건으로 인해 $A/\ann(M)$-module로서 유한한 길이를 가지고, $M$은 finitely generated $A/\ann(M)$-module이므로 원하는 결과를 얻는다. 

</details>

그럼 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="cor7">**따름정리 7**</ins> Noetherian ring $A$와 finitely generated $A$-module $M$, 그리고 $\ann(M)$을 포함하는 prime ideal $\mathfrak{p}$를 고정하자. 그럼 $A\_\mathfrak{p}$-module로서 $M\_\mathfrak{p}$가 유한한 길이를 갖는 것과 $\mathfrak{p}$가 $\ann(M)$을 포함하는 prime들 중 minimal인 것이 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

만일 $\mathfrak{p}$가 $\ann(M)$을 포함하는 minimal prime ideal이라면, $A\_\mathfrak{p}$-module $M\_\mathfrak{p}$는 유한한 길이를 갖는다. 이는 localization $A\_\mathfrak{p}$를 생각하면, $A\_\mathfrak{p}$의 prime ideal들은 [§국소화, ⁋명제 8](/ko/math/commutative_algebra/localization#prop8)에 의해 $\mathfrak{p}$에 속하는 prime ideal들인데, 그럼 $\mathfrak{p}$의 minimality로부터 $\ann(M)A\_\mathfrak{p}$를 포함하는 prime ideal은 오직 $\mathfrak{p}A\_\mathfrak{p}$ 뿐이고 이는 local ring $A\_\mathfrak{p}$의 (유일한) maximal ideal이기 때문이다. 

거꾸로 $M\_\mathfrak{p}$이 유한한 길이를 갖는 $A\_\mathfrak{p}$-module이라 하면, [따름정리 6](#cor6)에 의해 $M\_\mathfrak{p}$의 annihilator $\ann(M)A\_\mathfrak{p}$를 포함하는 prime ideal들은 모두 maximal이고, 이들은 다시 [§국소화, ⁋명제 8](/ko/math/commutative_algebra/localization#prop8)을 통해 $\ann(M)$을 포함하며 $\mathfrak{p}$에 포함된 prime ideal과 일대일대응이 있으므로 위의 논증을 뒤집으면 된다.

</details>

특별히 $A$의 임의의 ideal $\mathfrak{a}$에 대하여, $A$-module $A/\mathfrak{a}$를 생각하면 $\ann(A/\mathfrak{a})=\mathfrak{a}$가 되며, 이로부터 다음을 얻는다.

<div class="proposition" markdown="1">

<ins id="cor8">**따름정리 8**</ins> Noetherian ring $A$와 임의의 ideal $\mathfrak{a}$, 그리고 $\mathfrak{a}$를 포함하는 prime ideal $\mathfrak{p}$에 대하여, 다음이 모두 동치이다.

1. $\mathfrak{p}$는 $\mathfrak{a}$를 포함하는 prime ideal들 중 minimal이다.
2. $A\_\mathfrak{p}/\mathfrak{a}A\_\mathfrak{p}$가 artinian이다.
3. Localization $A\_\mathfrak{p}$ 안에서, 충분히 큰 $n$에 대하여 항상 $(\mathfrak{p}A_\mathfrak{p})^n\subseteq \mathfrak{a}A\_\mathfrak{p}$이 성립한다. 

</div>

---

**참고문헌**

**[Eis]** David Eisenbud. *Commutative Algebra: with a view toward algebraic geometry*. Springer, 1995.

---