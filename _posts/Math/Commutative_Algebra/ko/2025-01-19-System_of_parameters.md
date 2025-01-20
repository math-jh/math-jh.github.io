---

title: "매개계"
excerpt: ""

categories: [Math / Commutative Algebra]
permalink: /ko/math/commutative_algebra/system_of_parameters
header:
    overlay_image: /assets/images/Math/Commutative_Algebra/System_of_parameters.png
    overlay_filter: 0.5
sidebar: 
    nav: "commutative_algebra-ko"

date: 2025-01-19
last_modified_at: 2025-01-19
weight: 17

---

## System of parameters

앞선 글에서 살펴본 [§차원, ⁋정리 7](/ko/math/commutative_algebra/Krull_dimension#thm7)과 [§차원, ⁋따름정리 8](/ko/math/commutative_algebra/Krull_dimension#cor8)을 종합하면 다음과 같다.

<div class="proposition" markdown="1">

<ins id="cor1">**따름정리 1**</ins> Noetherian local ring $(A, \mathfrak{m})$이 주어졌다 하자. 그럼 $\dim A$는 다음의 조건

> 충분히 큰 $n$에 대하여, 항상 $\mathfrak{m}^n\subseteq (a_1,\ldots, a_d)$이도록 하는 $d$개의 원소 $a_1,\ldots, a_d$가 존재한다. 

이 성립하도록 하는 $d$ 가운데 가장 작은 것이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $\mathfrak{m}^n\subseteq (a_1,\ldots, a_d)$라 가정하자. 그럼 [§조르단-횔더 정리, ⁋따름정리 8](/ko/math/commutative_algebra/Jordan-Holder_theorem#cor8)에 의하여 $\mathfrak{m}$은 $(a_1,\ldots, a_d)$를 포함하는 prime ideal 중 minimal한 것이다. 따라서 [§차원, ⁋정리 7](/ko/math/commutative_algebra/Krull_dimension#thm7)에 의하여 $\codim \mathfrak{m}\leq d$가 성립한다. 

반대로 $(A,\mathfrak{m})$이 $\dim A=d$를 만족한다 하자. 그럼 정의에 의하여, 길이 $d$의 supremum은 $\mathfrak{m}$에서 시작하는 prime ideal들의 chain에서 나오므로, 정확히 $\codim \mathfrak{m}$과 같다. 따라서, [§차원, ⁋따름정리 8](/ko/math/commutative_algebra/Krull_dimension#cor8)을 사용하면 $\mathfrak{m}$이 ideal $(a_1,\ldots, a_d)$를 포함하는 것 중 minimal한 prime이도록 할 수 있다. 그럼 $\mathfrak{m}$은 $A/(a_1,\ldots, a_d)$에서 유일한 prime ideal이 되므로, 이것이 정확히 $A/(a_1,\ldots, a_d)$의 nilradical이 되어야 하고 ([§국소화의 성질들, ⁋따름정리 8](/ko/math/commutative_algebra//ko/math/commutative_algebra/properties_of_localization#cor8)) 따라서 원하는 결과를 얻는다. 

</details>

이제 다음을 정의한다. 

<div class="definition" markdown="1">

<ins id="prop-def2">**명제--정의 2**</ins> $(A,\mathfrak{m})$이 Krull dimension $d$의 local noetherian ring이라 하자. 그럼 $A$의 원소들의 family $a_1,\ldots, a_d$, 그리고 $\mathfrak{a}=(a_1,\ldots, a_d)$에 대하여, 다음이 모두 동치이다.

1. $\mathfrak{m}$이 $\mathfrak{a}$를 포함하는 prime ideal들 중 minimal하다.
2. $\mathfrak{m}=\sqrt{\mathfrak{a}}$이 성립한다.
3. $\mathfrak{m}$의 어떠한 거듭제곱이 $\mathfrak{a}$에 속한다. 
4. $\mathfrak{a}$가 $\mathfrak{m}$-primary ideal이다. 

이 조건이 성립한다면, $a_1,\ldots, a_d$들을 $A$의 *system of parameters<sub>매개계</sub>*라 부르고, $\mathfrak{a}$를 *parameter ideal*이라 부른다.

더 일반적으로, rank $d$의 finitely generated $A$-module $M$에 대하여, $A$-module $M/\mathfrak{a}M$이 유한한 길이를 갖도록 하는 $a_1,\ldots, a_d$들을 $A$의 *system of parameters*라 부르고, $\mathfrak{a}$를 $M$의 *parameter ideal*이라 부른다. 

</div>

이들 조건이 모두 동치임을 보이는 것은 앞선 글과 위의 따름정리에서 이미 해왔던 것이다. 한편, local ring $(A, \mathfrak{m})$에 대하여 

$$d=\dim A=\codim \mathfrak{m}$$

이므로, $A$의 parameter ideal $\mathfrak{a}$는 [§차원, ⁋정리 7](/ko/math/commutative_algebra/Krull_dimension#thm7)에 의하여 반드시 $d$개 이상의 원소로만 생성될 수 있다. 

$A$-module $M$의 parameter ideal $\mathfrak{a}$의 경우, 우리는 [§조르단-횔더 정리, ⁋따름정리 6](/ko/math/commutative_algebra/Jordan-Holder_theorem#cor6)의 첫째 조건과 둘째 조건 사이의 동치에 의해 $M/\mathfrak{a}M$이 유한한 길이를 갖는 것과, $\mathfrak{m}$의 충분히 큰 거듭제곱이 항상 $M/\mathfrak{a}M$을 annihilate하는 것이 동치인 것을 안다. 즉 $\mathfrak{m}^k M \subseteq \mathfrak{a}M$이 성립해야 하고, 이로부터 $A$ 자기자신을 $A$-module로 보았을 때 두 정의가 서로 합치하는 것을 안다. 비슷한 방법으로 우리가 앞서 살펴봤던 ring의 ideal과 차원 사이의 들에 대한 결과를 module의 parameter ideal에 대한 결과로 옮겨올 수 있는데, 이를 위해서 우선 다음의 간단한 보조정리들이 필요하다.

<div class="proposition" markdown="1">

<ins id="lem3">**보조정리 3**</ins> Noetherian ring $A$와 finitely generated $A$-module $M$, 그리고 $A$의 ideal $\mathfrak{a}$에 대하여, 다음 등식

$$\sqrt{\ann(M/\mathfrak{a}M)}=\sqrt{\mathfrak{a}+\ann(M)}$$

이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[§국소화의 성질들, ⁋따름정리 8](/ko/math/commutative_algebra//ko/math/commutative_algebra/properties_of_localization#cor8)에 의하여 $\ann(M/\mathfrak{a}M)$을 포함하는 prime ideal들의 집합과 $\mathfrak{a}+\ann(M)$을 포함하는 prime ideal들의 집합이 정확히 동일하다는 것을 보이면 충분하다. 이제 prime ideal $\mathfrak{p}$가 $\ann(M/\mathfrak{a}M)$을 포함하는 것은 [§국소화, ⁋명제 5](/ko/math/commutative_algebra/localization#prop5)에 의하여 $(M/\mathfrak{a}M)\_\mathfrak{p}\neq 0$인 것과 동치이다. 그럼 $(M/\mathfrak{a}M)\_\mathfrak{p}=M\_\mathfrak{p}/\mathfrak{a}M\_\mathfrak{p}\neq 0$인 것은, [§정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)에 의하여, $M\_\mathfrak{p}\neq 0$이고 $\mathfrak{a}A\_\mathfrak{p}\subseteq \mathfrak{p}A\_\mathfrak{p}$인 것과 동치이다. 이는 다시 [§국소화의 성질들, ⁋따름정리 8](/ko/math/commutative_algebra//ko/math/commutative_algebra/properties_of_localization#cor8)에 의하여, $\mathfrak{p}\supseteq \ann(M)$이고 $\mathfrak{p}\supseteq \mathfrak{a}$인 것, 즉 $\mathfrak{p}\supseteq \mathfrak{a}+\ann(M)$인 것과 동치이므로 원하는 결과를 얻는다. 

</details>

또, 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="lem4">**보조정리 4**</ins> $A$-module들의 short exact sequence

$$0 \rightarrow M' \overset{u}{\longrightarrow} M \overset{v}{\longrightarrow} M'' \rightarrow  0$$

에 대하여, $\ann(M)\subseteq \ann(M')\cap \ann(M'')$이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$a\in\ann(M)$이라 하면, 임의의 $x'\in M'$에 대하여 $u(ax')=au(x')=0$이고, $u$는 injective이므로 $ax'=0$이다. 비슷하게, 임의의 $x''\in M''$에 대하여, $v(x)=x''$를 만족하는 $x\in M$을 찾을 수 있고 그럼 $ax''=av(x)=v(ax)=0$이다. 이로부터 원하는 결과를 얻는다. 

</details>

그럼 다음 명제를 증명할 수 있다. 

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> Noetherian local ring $(A,\mathfrak{m})$과 그 ideal $\mathfrak{a}$, 그리고 finitely generated $A$-module $M$에 대하여 다음이 성립한다.

1. 다음이 모두 동치이다.
  - $\mathfrak{a}$가 $M$의 parameter ideal이다. 
  - 충분히 큰 $n$에 대하여, 항상 $(\mathfrak{a}+\ann(M))\supseteq \mathfrak{m}^n$이 성립한다.
  - $\mathfrak{a}$는 $A/\ann(M)$의 parameter ideal이다.
2. $A$-module들의 short exact sequence 
    
    $$0 \rightarrow M' \rightarrow M \rightarrow M'' \rightarrow 0$$

    에 대하여, $\mathfrak{a}$가 $M$의 parameter ideal인 것과, $\mathfrak{a}$가 $M',M''$의 parameter ideal인 것이 동치이다.
3. $\dim M$은 $d$개의 원소로 생성되는 $M$의 parameter가 존재하도록 하는 자연수 $d$ 중 가장 작은 것이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



1. 첫 번째 동치는 정의이며, 두 번째 동치를 보이기 위해서는 우선 $\mathfrak{a}+\ann(M)$이 $\mathfrak{m}$의 거듭제곱을 포함하는 것과 $\sqrt{\mathfrak{a}+\ann(M)}=\mathfrak{m}$인 것이 동치이므로, 다음의 식
    
    $$\ann\left(\frac{A/\ann(M)}{\mathfrak{a}(A/\ann(M))}\right)=\mathfrak{a}+\ann(M)$$

    의 양 변에 radical을 취하면 원하는 결과를 얻는다. 
2. $\mathfrak{a}$가 $M$의 parameter ideal이라 하자. 그럼 $\ann(M)\subseteq \ann(M')\cap \ann(M'')$이므로 $\mathfrak{a}$가 이들의 parameter ideal인 것이 자명하다. 거꾸로 $A/\mathfrak{a}\otimes-$를 취해 얻어지는 다음의 exact sequence
    
    $$M'/\mathfrak{a}M' \rightarrow M/ \mathfrak{a}M \rightarrow M''/\mathfrak{a}M'' \rightarrow 0$$

    로부터, 만일 $M'/\mathfrak{a}M'$과 $M''/\mathfrak{a}M''$이 유한한 길이를 갖는다면 $M/\mathfrak{a}M$ 또한 그래야 한다는 것을 안다.
3. 정의에 의하여 $\dim M=\dim A/\ann(M)$이므로 첫째 결과와 [§차원, ⁋따름정리 8](/ko/math/commutative_algebra/Krull_dimension#cor8)로부터 자명하다. 

</details>

<div class="proposition" markdown="1">

<ins id="cor6">**따름정리 6**</ins> Noetherian local ring $(A, \mathfrak{m})$과 finitely generated $A$-module $M$이 주어졌다 하자. 그럼 임의의 $a\in \mathfrak{m}$에 대하여,

$$\dim M/ aM \geq \dim M-1$$

이 성립한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

정의에 의하여, $\dim M/aM=d$라는 것은 ring $A/\ann(M/aM)$의 차원이 $d$라는 것이고, [명제 3](#prop3)의 첫째 결과로부터, $M/aM$의 system of parameters $a_1,\ldots, a_d\in A$가 존재한다는 것을 안다. 따라서 $M/(a, a_1,\ldots, a_d)M$ 또한 유한한 길이를 가지고, ideal $(a,a_1,\ldots, a_d)$가 parameter ideal이 된다. 

</details>

---

**참고문헌**

**[Eis]** David Eisenbud. *Commutative Algebra: with a view toward algebraic geometry*. Springer, 1995. 

---