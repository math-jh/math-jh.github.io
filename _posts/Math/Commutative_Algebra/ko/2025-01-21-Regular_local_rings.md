---

title: "정칙국소환"
excerpt: ""

categories: [Math / Commutative Algebra]
permalink: /ko/math/commutative_algebra/regular_local_rings
header:
    overlay_image: /assets/images/Math/Commutative_Algebra/Regular_local_rings.png
    overlay_filter: 0.5
sidebar: 
    nav: "commutative_algebra-ko"

date: 2025-01-21
last_modified_at: 2025-01-21
weight: 18

---

## 정칙국소환

한편 [§차원, ⁋정의 9](/ko/math/commutative_algebra/Krull_dimension#def9)을 생각하면, regular local ring $(A, \mathfrak{m})$에서 $\mathfrak{m}$을 생성하는 $d=\dim A$개의 원소들 $a_1,\ldots, a_d$는 $A$의 system of parameters가 되는 것이 자명하다. 이를 *regular system of parameters*라 부른다. 

<div class="proposition" markdown="1">

<ins id="cor1">**따름정리 1**</ins> Regular local ring은 integral domain이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$(A, \mathfrak{m})$의 차원에 대한 귀납법으로 증명한다. $d=0$인 경우는 $A$가 field이므로 증명할 것이 없다. $\dim A=d$인 경우까지 주어진 주장이 성립한다 가정하고 $\dim A=d+1$인 경우를 보이자. 그럼 특히 $\mathfrak{m}\neq 0$이므로 [§정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)로부터 $\mathfrak{m}\neq \mathfrak{m}^2$임을 안다. 한편, [§동반소아이디얼, ⁋정리 7](/ko/math/commutative_algebra/associated_primes#thm7)로부터 $A$의 minimal prime ideal들은 유한하다는 것을 안다. 이들을 $\mathfrak{p}\_1,\ldots, \mathfrak{p}\_k$라 하자. 만일

$$\mathfrak{m}\subseteq \mathfrak{m}^2\cup \mathfrak{p}_1\cup\cdots\cup \mathfrak{p}_k$$

라면 [§동반소아이디얼, ⁋보조정리 2](/ko/math/commutative_algebra/associated_primes#lem2)과 위의 계산 $\mathfrak{m}\neq \mathfrak{m}^2$에 의해 $\mathfrak{m}=\mathfrak{p}\_i$여야 하고, 이는

$$d+1=\dim A=\codim \mathfrak{m}=\codim \mathfrak{p}_i=0$$

이 되어 모순이므로 우리는 반드시 적당한 $a\in \mathfrak{m}$이 존재하여 $a\not\in \mathfrak{m}^2\cup \mathfrak{p}\_1\cup\cdots\cup \mathfrak{p}\_k$여야 함을 안다. 

이제 $A'=A/(a)$라 하고, $A'$의 maximal ideal $\mathfrak{m}'=\mathfrak{m}A'$를 생각하자. 그럼 $a$의 선택에 의하여, $A'$의 prime ideal들 중에는 $\mathfrak{p}\_i$에 대응되는 것이 없으므로 반드시 $\dim A'<\dim A$가 성립하며, 이를 [§매개계, ⁋따름정리 6](/ko/math/commutative_algebra/system_of_parameters#cor6)과 종합하면 $\dim A'=d-1$인 것을 안다. 따라서 다음 식

$$\mathfrak{m}'/(\mathfrak{m}')^2=\mathfrak{m}/(\mathfrak{m}^2+(a))$$

과 [§정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)로부터 $\mathfrak{m}'$이 $(d-1)$개의 원소로 생성되는 것을 알고, 따라서 귀납적 가정에 의해 $A'$는 integral domain이다. 즉, $(a)$는 prime ideal이며, 따라서 어떤 $i$에 대해 $\mathfrak{p}\_i\subsetneq (a)$가 성립한다. 

이제 임의의 $x\in \mathfrak{p}\_i$에 대하여, $x=\alpha a$이도록 하는 $\alpha\in A$를 택하자. 그럼 $a\not\in \mathfrak{p}\_i$이므로 $\alpha\in \mathfrak{p}\_i$이고, 따라서 $\mathfrak{p}\_i=a \mathfrak{p}\_i$이며 이로부터 $\mathfrak{p}\_i=\mathfrak{m}\mathfrak{p}\_i$이다. 다시 [§정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)를 적용하면 $\mathfrak{p}\_i=0$이므로 $A$는 integral domain이다. 

</details>

이 따름정리는 앞으로도 자주 사용하게 되므로, 다음과 같이 새로운 정의를 내린다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Ring $A$의 원소들 $a_1,\ldots, a_d$가 *$R$-regular sequence* 혹은 간단히 *$R$-sequence*라는 것은 $(a_1,\ldots, a_d)$가 proper이고, 각각의 $i$에 대하여 $a_{i+1}$의 image가 $A/(a_1,\ldots, a_i)$에서 non-zerodivisor인 것이다. 

</div>

<div class="proposition" markdown="1">

<ins id="cor3">**따름정리 3**</ins> Regular local noetherian ring의 regular system of parameters는 $R$-sequence를 이룬다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

각각의 $i$에 대하여 $A/(a_1,\ldots, a_i)$도 regular local ring이고, [따름정리 1](#cor1)에 의해 이는 integral domain이며 $x_{i+1}$은 이 ring의 $0$이 아닌 원소가 된다.

</details>

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> Complete regular local noethereian ring $(A, \mathfrak{m})$의 차원이 $d$이고, residue field $\kappa=A/\mathfrak{m}$라 하자. 만일 $R$이 어떠한 field를 포함한다면 $A\cong \kappa[[\x_1,\ldots, \x_d]]$이며, 이 isomorphism은 각각의 변수 $\x_i$들과 $A$의 regular system of parameters를 대응시킨다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[§완비화의 성질들, ⁋정리 8](/ko/math/commutative_algebra/properties_of_completion#thm8)에 의하여, 주어진 가정으로부터 $A$가 $\kappa$를 포함해야 한다는 것을 안다. 이제 [§완비화의 성질들, ⁋정리 5](/ko/math/commutative_algebra/properties_of_completion#thm5)의 첫째 결과에 의하여 $\kappa$-algebra homomorphism $\phi:\kappa[[\x_1,\ldots, \x_d]]\rightarrow A$를 얻으며, 둘째 결과에 의하여 $\phi$는 surjective이다. 한편 $\kappa[[\x_1,\ldots, \x_d]]$는 [따름정리 1](#cor1)에 의하여 $d$차원이므로 

$$d=\dim A=\dim \im(\phi)=\dim \kappa[[\x_1,\ldots,\x_d]]/\ker\phi\leq \dim \kappa[[\x_1,\ldots, \x_d]]-\codim \ker\phi=d-\codim\ker\phi$$

이고, 이것이 참이기 위해서는 반드시 $\codim\ker\phi=0$이어야 한다. 그런데 $\kappa[[\x_1,\ldots, \x_d]]$는 [§매개계, ⁋따름정리 10](/ko/math/commutative_algebra/system_of_parameters#cor10)에 의하여 integral domain이므로, 이는 곧 $\ker\phi=0$이라는 뜻이다. 

</details>

## 이산값매김환

이제 우리는 $1$차원의 regular local ring $(A,\mathfrak{m})$에 대해 살펴본다. 그럼 정의에 의해 $\mathfrak{m}$은 하나의 원소 $m$으로 생성되어야 하며, 우리는 이를 $A$의 *regular parameter* 혹은 *uniformizing parameter*라 부른다. 

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> 1차원의 regular local ring $(A, \mathfrak{m})$이 주어졌다 하고, $m$이 $A$의 regular parameter라 하자. 그럼 $\Frac(A)$의 임의의 원소 $x$는 

$$x=u m^k\qquad \text{$k\in \mathbb{Z}$, $u$ a unit of $A$}$$

의 꼴로 유일하게 적을 수 있다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $A$는 [따름정리 1](#cor1)으로부터 integral domain이다. 이제 [§부풀림 대수, ⁋따름정리 8](/ko/math/commutative_algebra/blowup_algebra#cor8)에 의하여 $\bigcap \mathfrak{m}^i=0$이므로, $0$이 아닌 임의의 $a\in A$에 대하여 $a\in \mathfrak{m}^i$를 성립하도록 하는 index $i$는 유한히 많다. 이들 중 가장 큰 것을 $k$라 하면, $a\in \mathfrak{m}^k=(m^k)$인 것으로부터 $a=vm^k$이도록 하는 $v\in A$가 존재한다. 그럼 $k$의 maximality에 의하여 $v$는 $A$의 unit이다. 

이제 $\Frac(A)$의 임의의 원소 $x$가 주어졌다 하자. $x=a_1/a_2$라 하면, 위의 논증에 의하여 

$$x=\frac{a_1}{a_2}=\frac{v_1m^{k_1}}{v_2m^{k_2}}=v_1v_2^{-1}m^{k_1-k_2}=um^k$$

로 적을 수 있다. 이 때 $u=v_1v_2^{-1}$이 unit이며, 이 표기의 유일성은 거의 자명하다. 

</details>

그럼 위에서 증명한 표기의 유일성으로부터, multiplicative group $\Frac(A)^\times$에서 $\mathbb{Z}$로의 group homomorphism 

$$\nu:\Frac(A)^\times \rightarrow \mathbb{Z};\qquad um^k\mapsto k$$

를 정의할 수 있다. 더 일반적으로 다음을 정의한다. 

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> Integral domain $A$와 totally ordered abelian group $G$에 대하여, group homomorphism $\nu:\Frac(A)^\times \rightarrow G$가 다음 부등식

$$\nu(x+y)\geq \min(\nu(x), \nu(y))$$

를 만족한다면 $\nu$를 *valuation<sub>값매김</sub>*이라 부른다. Valuation $\nu$에 대하여, 다음의 ring

$$S=\nu^{-1}\left(\{g\in G: g\geq 0\}\right)$$

을 $\nu$의 *valuation ring<sub>값매김환</sub>*이라 부른다. 

특히 만일 $G=\mathbb{Z}$일 경우에는 이를 *discrete valuation<sub>이산값매김</sub>*이라 부르고, $\nu$의 valuation ring을 *discrete valuation ring<sub>이산값매김환</sub>*이라 부른다. 

</div>

그럼 위에서 정의한 $\nu:\Frac(A)^\times \rightarrow \mathbb{Z}$가 discrete valuation이 된다는 것은 다음의 식

$$um^k+vm^l=(um^{k-\min(k,l)}+vm^{l-\min(k,l)})m^{\min(k,l)}$$

에 의해 자명하다. 그럼 [명제 4](#prop4)에 의하여, 두 complete discrete valuation ring이 각각 field를 포함하고, isomorphic한 residue field를 갖는다면 이들은 서로 isomorphic하다는 것을 안다. 그러나 일반적으로 complete하지 않은 discrete valuation ring들 사이에는 이러한 종류의 classification이 존재하지 않는다.

## 정규화

이제 우리는 normalization과 regular local ring 사이의 관계를 살펴본다. 우선 편의를 위해, ring $A$의 non-zerodivisor $u$에 대하여, $A/(u)$의 associated prime ideal $\mathfrak{p}$를 *associated to a non-zerodivisor $u$*라 부르기로 하자. 이는 [§동반소아이디얼, ⁋정의 1](/ko/math/commutative_algebra/associated_primes#def1)에서와 마찬가지 예외이다. 


<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> Reduced noetherian ring $A$와 $A$의 total ring of fractions $K$가 주어졌다 하자. 그럼 원소 $x\in K$가 $A$에 속하는 것은 임의의 prime ideal $\mathfrak{p}$ associated to a non-zerodivisor에 대하여 $x$의 $K_\mathfrak{p}$에서의 image가 $A\_\mathfrak{p}$에 속하는 것과 동치이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

정의에 의해 $K$의 원소는 임의의 $a\in A$와 non-zerodivisor $u\in A$에 대하여 $a/u$의 꼴이다. 이제

$$\frac{a}{u}\in A\iff a\in (u)\iff a=0\mod{(u)}\iff \epsilon_\mathfrak{p}(a)= 0\text{ in $(A/(u))_\mathfrak{p}=A_\mathfrak{p}/(u)A_\mathfrak{p}$ for all $\mathfrak{p}$ associated prime of $A/(u)$}$$

가 성립한다. 여기서 $\epsilon_\mathfrak{p}: A \rightarrow A_\mathfrak{p}$는 canonical morphism이고, 마지막 동치는 [§동반소아이디얼, ⁋따름정리 4](/ko/math/commutative_algebra/associated_primes#cor4)에 의한 것이다. 그럼 임의의 prime ideal $\mathfrak{p}$ associated to a non-zerodivisor에 대하여, 

$$\epsilon_\mathfrak{p}(a)\in(u)A_\mathfrak{p}$$

이다. 한편, $A$가 reduced이므로 $K$는 field들의 유한한 direct product이고 ([§동반소아이디얼, ⁋따름정리 8](/ko/math/commutative_algebra/associated_primes#cor8)), localization은 유한한 direct product와 commute하므로 $A\_\mathfrak{p}$의 total ring of fractions와 $K_\mathfrak{p}$를 identify할 수 있다. 이 identification을 통해 위의 포함관계를 다시 살펴보면 원하는 결과를 얻는다. 

</details>

이를 통해 다음을 보일 수 있다.

<div class="proposition" markdown="1">

<ins id="thm8">**정리 8**</ins> Noetherian integral domain $A$가 normal domain인 것은 다음 조건과 동치이다. 

($\ast$) 임의의 prime ideal $\mathfrak{p}$ associated to a principal ideal에 대하여, $\mathfrak{p}A\_\mathfrak{p}$는 $A\_\mathfrak{p}$의 principal ideal이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 ($\ast$)를 가정하고 $A$가 normal domain임을 보인다. 그런데 공통의 quotient field를 갖는 normal domain들이 주어졌다 하면, 이들의 교집합 또한 normal domain이 되는 것이 자명하다. 따라서 다음 식

$$A=\bigcap\text{\scriptsize$\mathfrak{p}$ associated to a principal ideal}A_\mathfrak{p}$$

을 보이면 충분하며, 여기서 $A\_\mathfrak{p}$는 $A$의 quotient field $K$의 부분집합으로 본 것이다. 이제 보이고자 하는 주장은 [명제 7](#prop7)에서 더 일반적인 경우에 다루었다. 

거꾸로 $A$가 normal domain이라 하고, $\mathfrak{p}$가 principal ideal $\mathfrak{a}=(a)$의 associated prime이라 하자. 즉

$$\mathfrak{p}=\ann(b+\mathfrak{a})$$

이며, 우리는 $\mathfrak{p}A\_\mathfrak{p}$가 $A\_\mathfrak{p}$의 principal ideal인 것을 보여야 한다. 이는 어차피 localization에 대한 것이므로, $(A,\mathfrak{p})$가 local ring이었다고 가정해도 상관 없으며, 이 때 $K$를 $A$의 field of fraction이라 하고 집합 $\mathfrak{p}^{-1}$을

$$\mathfrak{p}^{-1}=\{x\in K: x \mathfrak{p}\subseteq A\}$$

으로 정의하면 $\mathfrak{p}^{-1}\mathfrak{p}$는 $\mathfrak{p}$와 $A$ 사이의 ideal이라는 것을 보일 수 있다. 이제 $\mathfrak{p}$의 maximality로부터 $\mathfrak{p}^{-1}\mathfrak{p}=\mathfrak{p}$이거나 $\mathfrak{p}^{-1}\mathfrak{p}=A$가 성립해야 한다. 그런데 만일 $\mathfrak{p}^{-1}\mathfrak{p}=\mathfrak{p}$라면 [§정수적 확장, ⁋보조정리 5](/ko/math/commutative_algebra/integral_extension#lem5)에 의하여 $\mathfrak{p}^{-1}$의 임의의 원소는 integral이고, 따라서 $\mathfrak{p}^{-1}\in R$이다. 그런데 $\mathfrak{p}b\subseteq (a)$이므로, $b/a\in \mathfrak{p}^{-1}$이고 이로부터 $b\in (a)$가 되어 모순이다. 

따라서 $\mathfrak{p}\mathfrak{p}^{-1}=A$여야 한다. 또, $(A, \mathfrak{p})$가 local이므로, 이 두 조건을 종합하면 적당한 $x\in \mathfrak{p}^{-1}$에 대하여 $x \mathfrak{p}=A$여야 함을 안다. 따라서 $\mathfrak{p}=A x^{-1}$은 principal이다. 


</details>

정리 8 증명 다듬기

fractional ideal 먼저 하는게 순서상 맞아보임

내일 가급적이면 11 다



---