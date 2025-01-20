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

> 충분히 큰 $n$에 대하여, 항상 $\mathfrak{m}^n\subseteq (a_1,\ldots, a_d)$이도록 하는 $d$개의 원소 $a_1,\ldots, a\in \mathfrak{m}$가 존재한다. 

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

$a\in\ann(M)$이라 하면, 임의의 $x'\in M'$에 대하여 $u(ax')=au(x')=0$이고, $u$는 injective이므로 $ax'=0$가 되어 $a\in\ann(M')$이다.

비슷하게, 임의의 $x''\in M''$에 대하여, $v$가 surjective이므로 $v(x)=x''$를 만족하는 $x\in M$가 존재하고 그럼 $ax''=av(x)=v(ax)=0$이므로 $a\in\ann(M'')$이다. 

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

1. 우선 $\mathfrak{a}$가 $M$의 parameter ideal이라 가정하자. 그럼 [명제--정의 2](#prop-def2) 직후에 살펴본 논증에 의하여 $\mathfrak{m}$의 충분히 큰 거듭제곱이 항상 $M/\mathfrak{a}M$을 annihilate하는 것을 알고, 이와 [보조정리 3](#lem3)을 종합하면
    
    $$\mathfrak{m}\subseteq \sqrt{\ann(M/\mathfrak{a}M)}=\sqrt{\mathfrak{a}+\ann(M)}$$

    이므로, 충분히 큰 $n$에 대하여 $\mathfrak{m}^n\in(\mathfrak{a}+\ann(M))$이 성립해야 하는 것을 안다.  
    이제 둘째 조건을 가정하자. 그럼 ring $A'=A/\ann(M)$에서 $\mathfrak{m}+\ann(M)$은 유일한 maximal ideal이고, 가정으로부터 충분히 큰 $n$에 대하여 $(\mathfrak{m}+\ann(M))^n$이 $\mathfrak{a}+\ann(M)$에 속해야 하는 것을 알고 있으므로 $\mathfrak{a}+\ann(M)$은 $A/\ann(M)$의 (ring으로서의) parameter ideal이며, $A/\ann(M)$을 $A$-module로 보면 원하는 결과를 얻는다.  
    마지막 동치의 경우, 다음 포함관계

    $$\mathfrak{m}\subseteq \sqrt{\mathfrak{a}+\ann(M)}=\sqrt{\ann(M/\mathfrak{a}M)}$$

    로부터 자명하다. 
2. $\mathfrak{a}$가 $M$의 parameter ideal이라 하자. 그럼 [보조정리 4](#lem4)에 의하여 $\ann(M)\subseteq \ann(M')\cap \ann(M'')$이므로 $\mathfrak{a}$가 이들의 parameter ideal인 것이 자명하다. 거꾸로 $A/\mathfrak{a}\otimes-$를 취해 얻어지는 다음의 exact sequence
    
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

정의에 의하여, $\dim M/aM=d$라는 것은 ring $A/\ann(M/aM)$의 차원이 $d$라는 것이다. 그럼 [따름정리 1](#cor1)에 의하여 $A/\ann(M/aM)$은 $d$개의 원소로 생성되는 parameter ideal $\mathfrak{a}=(a_1,\ldots, a_d)$를 가지며, [명제 5](#prop5)의 첫째 결과에 의하여 이는 $M/aM$의 parameter ideal이기도 하다. 그럼 

$$\frac{M/aM}{\mathfrak{a}(M/aM)}\cong \frac{M}{((a)+\mathfrak{a})M}=\frac{M}{(a,a_1,\ldots, a_d)M}$$

이 유한한 길이를 가지므로, $(a,a_1,\ldots, a_d)$는 $M$의 parameter ideal이 된다. 따라서 [명제 5](#prop5)의 셋째 조건에 의하여 $\dim M\leq 1+d$이다. 

</details>

## 평탄사상과 차원

차원의 정의에 의하여, ring homomorphism $\phi: A \rightarrow B$을 통해 $A$와 $B$의 차원을 비교하기 위해서는 [§정수적 확장과 아이디얼, ⁋명제 1](/ko/math/commutative_algebra/lying_over_and_going_up#prop1)이 필수적이다. 다음 보조정리 또한 이와 비슷한 용도이지만, prime ideal을 만들어내는 방향이 반대이다. 

<div class="proposition" markdown="1">

<ins id="lem7">**보조정리 7 (Going down for flat extensions)**</ins> Noetherian ring들 사이의 ring homomorphism $\phi: A \rightarrow B$가 주어졌다 하고, 이를 통해 $B$가 flat $A$-module 구조를 갖는다 하자. 그럼 prime ideal들 $\mathfrak{p}\_2\subseteq\mathfrak{p}\_1\subseteq A$와, $\phi^{-1}\mathfrak{q}\_1=\mathfrak{p}\_1$을 만족하는 $B$의 prime ideal $\mathfrak{q}\_1$에 대하여, 적당한 $B$의 prime ideal $\mathfrak{q}\_2$가 존재하여 $\phi^{-1}\mathfrak{q}\_2=\mathfrak{p}\_2$이도록 할 수 있다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $\phi: A \rightarrow B$에 $A/\mathfrak{p}\_2\otimes_A-$를 취하면 다음의 ring homomorphism

$$\phi\otimes_A\id_{A/\mathfrak{p}_2}: A/\mathfrak{p}_2\cong A\otimes_A A/\mathfrak{p}_2 \rightarrow B\otimes_A A/\mathfrak{p}_2\cong B/\mathfrak{p}_2B$$

를 얻으며, $\phi$가 flat이라는 가정으로부터 이 또한 flat인 것을 안다. 따라서 $\mathfrak{p}\_2=0$이고 $A$가 integral domain이라 가정해도 충분하다. 그럼 [§평탄성, ⁋따름정리 3](/ko/math/commutative_algebra/flatness#cor3)에 의하여 $\phi$는 $A$의 non-zerodivisor를 $B$의 non-zerodivisor로 옮겨야 한다. 

한편, [\[집합론\] §선택공리, ⁋정리 4](/ko/math/set_theory/axiom_of_choice#thm4)에 의하여 우리는 $\mathfrak{q}\_1$에 포함되는 minimal prime ideal $\mathfrak{q}\_2$가 존재함을 안다. 그런데 $B$를 자기 자신 위에 정의된 module로 본다면 $\ann B=0$이므로 [§동반소아이디얼, ⁋정리 7](/ko/math/commutative_algebra/associated_primes#thm7)의 첫째 결과에 의하여 $\mathfrak{q}\_2\in \Ass B$이고, 다시 해당 정리의 둘째 결과에 의하여 $\mathfrak{q}\_2$는 zero-divisor로만 이루어져 있어야 한다. 따라서 위에서 살펴본 $\phi$의 성질에 의하여 $\phi^{-1}(\mathfrak{q}\_2)=0$이어야 함을 안다. 

</details>

위의 증명에서 $B/\mathfrak{p}\_2B$를 그대로 살려주면, $\mathfrak{q}\_2$를 택할 때, $\mathfrak{q}\_1$에 속하고 $\mathfrak{p}\_2 B$를 포함하는 prime ideal들 중 minimal한 것으로 택하면 된다는 것을 안다. 

그럼 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="thm8">**정리 8**</ins> Noetherian local ring 사이의 map $(A,\mathfrak{m}) \rightarrow (B, \mathfrak{n})$이 존재한다면

$$\dim B\leq \dim A +\dim A/\mathfrak{m}$$

이 성립하며, 만일 $\phi:A \rightarrow B$가 flat일 경우 등호가 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

편의상 $\dim A=d$, $e=\dim B/\mathfrak{m}B$로 표기하자. 우선 [따름정리 1](#cor1)에 의해 $a_1,\ldots, a_d$이 존재하여, 충분히 큰 $s$에 대하여는 항상 $\mathfrak{m}^s\subseteq (a_1,\ldots, a_d)$이도록 할 수 있고, 비슷하게 $b_1,\ldots, b_e\in B$가 존재하여, 충분히 큰 $t$에 대하여는 항상 $\mathfrak{n}^t\subseteq \phi(\mathfrak{m})B+(b_1,\ldots, b_e)$이도록 할 수 있다. 그럼 이제

$$\mathfrak{n}^{st}=(\mathfrak{n}^t)^s\subseteq (\phi(\mathfrak{m})B+(b_1,\ldots, b_e))^s\subseteq \phi(\mathfrak{m}^s)B+(b_1,\ldots, b_e)\subseteq (\phi(a_1),\ldots, \phi(a_d), b_1,\ldots, b_e)$$

이므로, [§차원, ⁋정리 7](/ko/math/commutative_algebra/Krull_dimension#thm7)에 의해 $\dim B\leq d+e$가 성립한다. 

이제 $\phi:A \rightarrow B$가 $B$를 flat $A$-module로 만든다 가정하고 반대방향 부등호를 보이자. 우선 이를 위해 $B/\phi(\mathfrak{m})B$의 차원을 주는 prime ideal들의 chain을 생각하면, $B$의 적당한 prime ideal $\mathfrak{q}$가 존재하여 $\dim \mathfrak{q}=\dim B/\phi(\mathfrak{m})B$이도록 할 수 있으며, 특히 $\mathfrak{q}$는 $\phi(\mathfrak{m})B$를 포함하는 prime ideal 중 minimal한 것이다. 그럼 이제 다음의 부등식

$$\dim B\geq\dim \mathfrak{q}+\codim \mathfrak{q}=\dim B/\phi(\mathfrak{m})B+\codim \mathfrak{q}$$

으로부터, 우리가 보여야 하는 것은 $\codim \mathfrak{q}\geq\dim A$임을 안다. 그런데 정의에 의하여 $\phi^{-1}(\mathfrak{q})=\mathfrak{m}$이므로, [보조정리 7](#lem7)에 의해 우리는 $\mathfrak{m}$으로 시작하는 $A$의 prime ideal들의 chain

$$\mathfrak{m}\supseteq \mathfrak{p}_1\supseteq \mathfrak{p}_2\supseteq\cdots$$

이 주어질 때마다 $\mathfrak{q}$로부터 시작하는 $B$의 prime ideal들의 chain

$$\mathfrak{q}\supseteq \mathfrak{q}_1\supseteq \mathfrak{q}_2\supseteq\cdots$$

이 존재함을 알고, 이로부터 원하는 부등식을 얻는다. 

</details>

다음 따름정리들은 위의 정리로부터 어렵지 않게 얻어진다. 

<div class="proposition" markdown="1">

<ins id="cor9">**따름정리 9**</ins> Noetherian local ring $(A, \mathfrak{m})$과, $\mathfrak{m}$에서의 $A$의 completion $\widehat{A}$에 대하여, $\dim A=\dim \widehat{A}$가 성립한다.

</div>

<div class="proposition" markdown="1">

<ins id="cor10">**따름정리 10**</ins> 다음이 성립한다.

1. Field $\mathbb{k}$에 대하여, $\dim \mathbb{k}[\x_1,\ldots, \x_r]=r$이다. 
2. 임의의 ring $A$에 대하여, $\dim A[\x]=1+\dim A$가 성립한다.
3. $A$의 임의의 prime ideal $\mathfrak{p}$에 대하여, $\mathfrak{q}\cap A=\mathfrak{p}$를 만족하는 $A[\x]$의 prime ideal $\mathfrak{q}$가 존재하며, 이 성질을 만족하는 것들 중 maximal한 $\mathfrak{q}$에 대하여 식 $\dim A[\x]\_\mathfrak{q}=1+\dim A\_\mathfrak{p}$이 성립한다. 

</div>

## 정칙국소환

한편 [§차원, ⁋정의 9](/ko/math/commutative_algebra/Krull_dimension#def9)을 생각하면, regular local ring $(A, \mathfrak{m})$에서 $\mathfrak{m}$을 생성하는 $d=\dim A$개의 원소들 $a_1,\ldots, a_d$는 $A$의 system of parameters가 되는 것이 자명하다. 이를 *regular system of parameters*라 부른다. 

<div class="proposition" markdown="1">

<ins id="cor11">**따름정리 11**</ins> Regular local ring은 integral domain이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$(A, \mathfrak{m})$의 차원에 대한 귀납법으로 증명한다. $d=0$인 경우는 $A$가 field이므로 증명할 것이 없다. $\dim A=d$인 경우까지 주어진 주장이 성립한다 가정하고 $\dim A=d+1$인 경우를 보이자. 그럼 특히 $\mathfrak{m}\neq 0$이므로 [§정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)로부터 $\mathfrak{m}\neq \mathfrak{m}^2$임을 안다. 한편, [§동반소아이디얼, ⁋정리 7](/ko/math/commutative_algebra/associated_primes#thm7)로부터 $A$의 minimal prime ideal들은 유한하다는 것을 안다. 이들을 $\mathfrak{p}\_1,\ldots, \mathfrak{p}\_k$라 하자. 만일

$$\mathfrak{m}\subseteq \mathfrak{m}^2\cup \mathfrak{p}_1\cup\cdots\cup \mathfrak{p}_k$$

라면 [§동반소아이디얼, ⁋보조정리 2](/ko/math/commutative_algebra/associated_primes#lem2)과 위의 계산 $\mathfrak{m}\neq \mathfrak{m}^2$에 의해 $\mathfrak{m}=\mathfrak{p}\_i$여야 하고, 이는

$$d+1=\dim A=\codim \mathfrak{m}=\codim \mathfrak{p}_i=0$$

이 되어 모순이므로 우리는 반드시 적당한 $a\in \mathfrak{m}$이 존재하여 $a\not\in \mathfrak{m}^2\cup \mathfrak{p}\_1\cup\cdots\cup \mathfrak{p}\_k$여야 함을 안다. 

이제 $A'=A/(a)$라 하고, $A'$의 maximal ideal $\mathfrak{m}'=\mathfrak{m}A'$를 생각하자. 그럼 $a$의 선택에 의하여, $A'$의 prime ideal들 중에는 $\mathfrak{p}\_i$에 대응되는 것이 없으므로 반드시 $\dim A'<\dim A$가 성립하며, 이를 [따름정리 6](#cor6)과 종합하면 $\dim A'=d-1$인 것을 안다. 따라서 다음 식

$$\mathfrak{m}'/(\mathfrak{m}')^2=\mathfrak{m}/(\mathfrak{m}^2+(a))$$

과 [§정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)로부터 $\mathfrak{m}'$이 $(d-1)$개의 원소로 생성되는 것을 알고, 따라서 귀납적 가정에 의해 $A'$는 integral domain이다. 즉, $(a)$는 prime ideal이며, 따라서 어떤 $i$에 대해 $\mathfrak{p}\_i\subsetneq (a)$가 성립한다. 

이제 임의의 $x\in \mathfrak{p}\_i$에 대하여, $x=\alpha a$이도록 하는 $\alpha\in A$를 택하자. 그럼 $a\not\in \mathfrak{p}\_i$이므로 $\alpha\in \mathfrak{p}\_i$이고, 따라서 $\mathfrak{p}\_i=a \mathfrak{p}\_i$이며 이로부터 $\mathfrak{p}\_i=\mathfrak{m}\mathfrak{p}\_i$이다. 다시 [§정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)를 적용하면 $\mathfrak{p}\_i=0$이므로 $A$는 integral domain이다. 

</details>

---

**참고문헌**

**[Eis]** David Eisenbud. *Commutative Algebra: with a view toward algebraic geometry*. Springer, 1995. 

---