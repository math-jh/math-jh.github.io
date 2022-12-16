---

title: "데데킨트 환에서의 인수분해"
excerpt: "Dedekind ring에서의 ideal factorization"

categories: [Math / Algebraic Number Theory]
permalink: /ko/math/algebraic_number_theory/unique_factorization
header:
    overlay_image: /assets/images/Algebraic_number_theory/Unique_factorization.png
    overlay_filter: 0.5
sidebar: 
    nav: "further_topics"

date: 2021-10-03
last_modified_at: 
weight: 2

published: false

---

<div class="notice--warning" markdown="1">

이 글은 현재 수정중입니다.

이 글은 예전에 쓴 글로, 서술 방향이 마음에 들지 않거나 표기법이 마음에 들지 않아 전체적으로 수정이 진행중입니다. 읽으실 때 참고해주세요.

</div>


## Discrete valuation rings and Dedekind rings

우리는 앞선 글에서, UFD가 아닌 domain, 예를 들어 $\mathbb{Z}[\sqrt{-5}]$ 상에서 ideal factorization의 개념을 도입하면 어떻게 unique factorization이 보장되는지를 살펴보았다. 물론 이 또한 모든 ring에서 되는 것은 아니고, 우리가 앞으로 정의할 *Dedekind domain*의 성질이다. 

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> Ring $R$이 *discrete valuation ring*이라는 것은, $R$이 PID인 동시에 local ring인 것이다.

</div>

*Discrete valuation*이라는 이름은 나중에 그 의미를 알게 된다. 이 이름을 다 불러주기에는 너무 길기 때문에, PID나 UFD 등과 마찬가지로, 이를 *DVR*로 간단히 줄여 말한다. 

$R$이 DVR이라 하자. $R$은 local ring이므로, 유일한 maximal ideal $\mathfrak{m}$이 존재한다. 그런데 $R$은 정의에 의해 PID이기도 하므로, $\mathfrak{m}$을 generate하는 $R$의 원소 $\pi$가 존재한다. 즉, $\mathfrak{m}=R\pi$이다. 이러한 $\pi$를 *uniformizer*라 부른다. 정의에 의해, 모든 field는 DVR이다. (이 경우, $\pi=0$이 된다.) 그러나 많은 경우에 그렇듯, field는 너무 좋은 성질을 많이 갖고 있기 때문에, 우리는 field보다는 조금 덜 trivial한 example들을 살펴볼 것이다. 

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> $R$이 DVR이고, $\pi$가 $R$의 uniformizer라 하자. 

1. $R$은 noetherian이다.
2. $R$이 field가 아니라면, 임의의 nonzero $x\in R$은 unit $u$와, 적당한 integer $k$에 대해 $u\pi^k$의 꼴로 나타난다.
3. $R$이 field가 아니라면, 임의의 nonzero ideal은 $R\pi^k$의 꼴로 나타난다.
4. $R$은 integrally closed이다.
5. $R$이 field가 아니라면 $\mathfrak{m}$이 $R$의 유일한 nonzero prime ideal이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

1. PID의 임의의 ideal은 하나의 원소로 generate되므로 Noetherian이다.
2. 임의의 prime element $p$에 대하여, $p$를 포함하는 $R$의 maximal ideal이 존재한다. 만일 $p\not\in\mathfrak{m}$이라면 이는 $\mathfrak{m}$의 유일성에 모순이므로, $p\in\mathfrak{m}$이어야 하고 $p=v\pi^m$이다.[^1] 이제 $R$은 UFD이기도 하므로, 임의의 $x\in R$은 prime factor들로 인수분해되어야 하고 따라서 $x=u\pi^k$의 꼴이다.
3. $R$은 PID이므로, $R$의 임의의 ideal은 적당한 $x\in R$에 대해 $Rx$의 꼴이고, 따라서 2번에 의해 주어진 명제가 성립한다.
4. UFD는 integrally closed.
5. $R$이 field가 아니라면 $\pi\neq0$이고 따라서 $\mathfrak{p}\neq 0$이다. 한편, $R$의 또 다른 prime ideal은 반드시 $Rp$의 꼴인데, $R$의 prime element $p$는 2번과 [각주 1](#fn:1)에 의해 $u\pi$ 뿐이므로 주어진 명제가 성립한다. 

</details>

DVR을 정의하고 나면, 우리가 주로 다룰 domain인 *Dedekind domain*을 다음과 같이 정의할 수 있다.

<div class="definition" markdown="1">

<ins id="df3">**정의 3**</ins> Ring $R$이 *Dedekind domain*이라는 것은 $R$이 noetherian integral domain이고, $R$의 임의의 prime ideal $\mathfrak{p}$에 대하여 $\mathfrak{p}$에서의 localization $R\_\mathfrak{p}$가 모두 DVR인 것이다.

</div>

<div class="proposition" markdown="1">

<ins id="pp4">**명제 4**</ins> $R$이 Dedekind domain이라 하자.

1. $R$의 임의의 nonzero prime ideal은 항상 maximal ideal이다.
2. $R$의 임의의 multiplicative subset $S$에 대하여, localization $R_S$ 또한 Dedekind domain이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

1. 우선, 결론에 반하여 어떤 prime ideal $\mathfrak{p}$를 proper하게 포함하는 maximal ideal $\mathfrak{m}$이 존재한다고 가정하자. 그럼 $\mathfrak{m}$은 prime이고, 따라서 $\mathfrak{m}$에서의 localization $R\_\mathfrak{m}$은 DVR이다. 그런데 [§Introduction, 명제 1](/ko/math/algebraic_number_theory/introduction#pp1)에 의하여, 우리는 $R\_\mathfrak{m}$에서의 prime ideal들의 chain $\mathfrak{p}R\_\mathfrak{m}\subset\mathfrak{m}R\_\mathfrak{m}$을 얻게 된다. 이는 [명제 2](#pp2), 5번에 모순이므로, $\mathfrak{p}\subsetneq\mathfrak{m}$인 $\mathfrak{m}$은 존재하지 않는다.
2. 어렵지 않게 $R\_\mathfrak{p}=(R_S)\_{\mathfrak{p}R_S}$임을 보일 수 있다. 예를 들어, 우변의 집합을 생각해보면 이 집합은 $r_2/s_2\not\in\mathfrak{p}R_S$를 만족하는 $(r_1/s_1)/(r_2/s_2)$들의 집합일 것인데, 이를 적당히 통분해주면 $(r_1s_2)/(r_2s_1)$이 된다. 분모 $r_2s_1$을 보면, $r_2\not\in\mathfrak{p}$이고, $s_2\in S$이므로 $s_2\not\in\mathfrak{p}$이다. $\mathfrak{p}$는 $R$의 prime ideal이므로 이들의 곱 $r_2s_1\not\in\mathfrak{p}$이고, 따라서 이 원소는 $R_\mathfrak{p}$의 원소로 볼 수 있다. 반대는 더더욱 자명하다. 이를 통해 2번은 자명하다. 

</details>

[§Introduction](/ko/math/algebraic_number_theory/introduction)에서 소개한 것과 같이, Dedekind domain은 UFD일 필요가 없다. 대표적인 예시는 $\mathbb{Z}[\sqrt{-d}]$가 있는데, 우리는 이들이 Dedekind domain이라는 것은 좀 나중에 증명하기로 하고, 그 대신 Dedekind domain의 unique factorization property부터 증명한다.

## Unique factorization of ideals

우리가 사용할 도구는 학부 대수시간에 ring을 정의하며 증명하는 *중국인의 나머지 정리*다. 앞으로 종종 사용할 예정이니, Chinese Remainder Theorem의 머릿글자를 따서 CRT라 부르자. 

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5 (Chinese Remainder Theorem)**</ins> $R$이 ring이고, $R$의 ideal들 $\mathfrak{a}\_1,\ldots, \mathfrak{a}\_n$들이 주어졌다 하자. 만일 $\mathfrak{a}\_i$들이 *comaximal*이라면, 즉, $i\neq j$에 대해 $\mathfrak{a}\_i+\mathfrak{a}\_j=R$이 성립한다면, 다음의 diagonal mapping

$$x\mapsto (x+\mathfrak{a}_1,\ldots, x+\mathfrak{a}_n)$$ 

이 isomorphism

$$R\big/\bigcap\mathfrak{a}_i\cong (R/\mathfrak{a}_1)\oplus\cdots\oplus(R/\mathfrak{a}_n)$$

을 induce한다. 또, 이 때 $\bigcap\mathfrak{a}\_i=\mathfrak{a}\_1\cdots\mathfrak{a}\_n$이 성립한다.

</div>

우리의 목표는 이를 이용해서 Dedekind domain에서의 unique factorization property를 증명하는 것이다. 즉, Dedekind domain $R$과, 그 ideal $\mathfrak{A}$에 대해 $\mathfrak{A}$가 prime ideal들의 product $\mathfrak{p}_1^{a_1}\cdots\mathfrak{p}_k^{a_k}$의 꼴로 나타난다는 것을 보여야 한다. 아마도... 확실하진 않지만... 이 모양은 CRT에서 좌변의 분모 (즉 $R$을 quotient 시키는 부분)에 들어있으니, 어떻게든 

$$R/\mathfrak{A}\cong R/\mathfrak{p}_1^{a_1}\oplus\cdots\oplus R/\mathfrak{p}_k^{a_k}$$

꼴로 만든 다음 해결을 봐야 할 것 같다. 일단 이 논리를 움직이게 하려면, CRT의 전제조건을 우선 보여야 한다. 그런데 $R$은 Dedekind domain이므로, 모든 prime ideal들은 maximal이고, 따라서 CRT의 comaximal 조건은 다음 보조정리로 충분하다.

<div class="proposition" markdown="1">

<ins id="lem6">**보조정리 6**</ins> 임의의 ring $A$와, $A$의 서로 다른 두 maximal ideal $\mathfrak{m}_1$, $\mathfrak{m}_2$에 대하여, $\mathfrak{m}_1^a+\mathfrak{m}_2^b=R$이 임의의 양의 정수 $a,b$에 대해 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

두 개의 maximal ideal들의 sum은 maximality에 의해 $A$ 전체여야 한다. 즉 $\mathfrak{m}_1+\mathfrak{m}_2=A$이다. 이제 induction을 진행하면 된다. 

$$A=A^a=(\mathfrak{m}_1+\mathfrak{m}_2)^a\subset\mathfrak{m}_1^a+\mathfrak{m}_2$$

가 성립하므로 $A=\mathfrak{m}_1^a+\mathfrak{m}_2$이고, 만일 $A=\mathfrak{m}_1^a+\mathfrak{m}_2^k$가 성립한다면

$$\mathfrak{m}_2^k=\mathfrak{m}_2^kR=\mathfrak{m}_2^k(\mathfrak{m}_1^a+\mathfrak{m}_2)\subset\mathfrak{m}_1^a+\mathfrak{m}_2^{k+1}$$

도 성립하므로 induction이 잘 굴러간다.

</details>

하지만, 이게 만족되었다고 해도 아직 $\mathfrak{A}\cong\mathfrak{p}_1^{a_1}\cdots\mathfrak{p}_k^{a_k}$이라고 하는 것은 아슬아슬하다. 또 다른 보조정리가 필요하다.

위에서 $R$ 대신 $A$를 쓴 것을 보면 짐작하겠지만, 사실 우리는 Dedekind domain $R$ 대신, $A=R/\mathfrak{A}$를 넣어서 증명할 것이고, $R/\mathfrak{A}$가 Dedekind domain이라는 보장은 없으므로[^2] 이 ring에 대해 Dedekind domain의 성질을 쓰면 안 된다. 그러나, 대신 fourth isomorphism theorem을 쓰면, <span class="border-highlight">$R/\mathfrak{A}$의 모든 prime ideal은 maximal</span>이라는 사실은 사용해도 된다. 또, $R/\mathfrak{A}$가 Noetherian인 것도 자명하다. 이 가정들 하에서, 다음 보조정리가 성립한다.

<div class="proposition" markdown="1">

<ins id="lem7">**보조정리 7**</ins> 임의의 Noetherian ring $A$의 모든 nonzero prime ideal들이 maximal이기도 하다면, $A$의 임의의 ideal은 nonzero prime ideal들의 product를 포함한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

사실 두 번째 조건은 안 써도 된다. 만일, 임의의 ideal이 모두 nonzero prime ideal들의 product를 포함한다면 더 이상 증명할 것이 없다. 만일 그러한 ideal이 존재한다면, Noetherian property에 의해 그러한 ideal 중 maximal인 $\mathfrak{J}$를 뽑아올 수 있다. 우선, $\mathfrak{J}$는 정의에 의해 prime이 아니다. 즉, 어떤 $x,y\in A$가 존재하여 $xy\in\mathfrak{J}$이지만 $x,y\not\in\mathfrak{J}$이도록 할 수 있다. 이제 $\mathfrak{A}=Ax+\mathfrak{J}$, $\mathfrak{B}=Ax+\mathfrak{J}$라 하자. 그럼 $\mathfrak{A}$, $\mathfrak{B}$는 모두 $J$를 (strictly) 포함하고, 따라서 이들은 $\mathfrak{J}$의 maximality에 의해, prime ideal들의 product를 포함한다. 그런데 $\mathfrak{A}\mathfrak{B}\subset\mathfrak{J}$이므로, $\mathfrak{J}$도 prime ideal들의 product를 포함해야 한다. 이는 모순이므로, 증명 끝.

</details>

한편, 특별히 이 임의의 ideal을 zero ideal으로 둔다면, $(0)$도 nonzero prime ideal들의 product를 포함해야 하므로

$$\mathfrak{P}_1^{a_1}\cdots\mathfrak{P}_n^{a_n}=0\tag{1}$$

이도록 하는 prime ideal들과 양수들이 존재한다. 뿐만 아니라, 그 역도 성립한다.

<div class="proposition" markdown="1">

<ins id="lem8">**보조정리 8**</ins> 위 식 (1)을 만족하는 ideal $\mathfrak{P}_i$들은 모두 prime이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$\mathfrak{P}_i/\mathfrak{P}_i^{a_i}$들이 $A/\mathfrak{P}_i^{a_i}$ 상에서의 유일한 prime ideal이므로, direct sum에서의 ideal의 모양을 생각해보면 자명하다.

</details>

Ring $A$는 모든 prime ideal들이 maximal이기도 한 ring이므로, 이들은 모두 [보조정리 6](#lem6)의 조건을 만족하고 따라서 CRT에 의해

$$A\cong A/\mathfrak{P}_1^{a_1}\oplus\cdots\oplus A/\mathfrak{P}_n^{a_n}$$

이 성립한다. 이제 드디어 원하는 걸 증명할 수 있다.

<div class="proposition" markdown="1">

<ins id="thm9">**정리 9**</ins> Dedekind ring $R$과, $R$의 nonzero ideal $\mathfrak{A}$에 대하여, $\mathfrak{A}$는 유한하게 많은 prime ideal들 $\mathfrak{p}_1,\ldots,\mathfrak{p}_n$에만 속해 있으며, 적당한 양의 정수 $a_i$들이 존재하여 $\mathfrak{A}=\mathfrak{p}_1^{a_1}\cdots\mathfrak{p}_n^{a_n}$이 성립하며, 그 표현은 유일하다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선, $A=R/\mathfrak{A}$로 두면, 미리 이야기했던 것과 마찬가지로 $A$는 Noetherian ring이며, $A$의 모든 nonzero prime ideal들은 maximal이다. 따라서, [보조정리 7](#lem7)을 $A$의 zero ideal에 적용하면, 우리는 $A$에서 식 (1)을 만족하는 prime ideal들을 얻고, 이들은 $\mathfrak{A}$를 포함하는 $R$의 prime ideal들과 하나씩 대응되므로, 유한하게 많은 $R$의 prime ideal들 $\mathfrak{p}_1,\ldots,\mathfrak{p}_n$들이 $\mathfrak{A}$를 포함한다. 이제 $b_i$들을 $\mathfrak{p}_1^{b_1}\cdots\mathfrak{p}_n^{b_n}\subset\mathfrak{A}$를 만족하는 양의 정수들로 골라오자. $A'=R/ \mathfrak{p}_1^{b_1}\cdots\mathfrak{p}_n^{b_n}$이라 하면, 우리는 CRT의 우변에 있는 direct sum의 ideal들의 모양으로부터, $A'$의 ideal들은 모두 $c_i\leq b_i$를 만족하는 정수들에 대해 $\mathfrak{p}_1^{c_1}\cdots\mathfrak{p}_n^{c_n}$의 꼴임을 알 수 있다. 따라서, $\mathfrak{A}$는 $A'$에서 이 product와 동일한 image를 가지고, 둘 다 $ \mathfrak{p}_1^{b_1}\cdots\mathfrak{p}_n^{b_n}$를 포함하므로, 다시 fourth isomorphism theorem으로부터 이들은 같은 ideal임을 알 수 있다. 유일성 또한 거의 자명하다.

</details>

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> $K=\mathbb{Q}(\sqrt{-23})$이라 하고, $R$을 이 field에서의 $\mathbb{Z}$의 integral closure라 하자. $-23\equiv 1\mod 4$이므로, 우리는 

$$R=\mathbb{Z}\left[\frac{1+\sqrt{-23}}{2}\right]$$

임을 알고 있다. 우리는 아직 이 ring이 Dedekind domain이라는 걸 모르긴 하지만, 이건 나중에 증명하기로 하고, 이 ring 사이에서 ideal들을 조금 계산해보자. 우선 $\alpha=(1+\sqrt{-23})/2$의 minimal polynomial은 $f(x)=x^2-x+6$이고, 따라서 $R$은

$$\mathbb{Z}[x]/(x^2-x+6)$$

과 identify할 수 있다. 예를 들어, 우리가 $2R$, $3R$ 등의 principal ideal들을 factorize한다고 해 보자. 우선 $2R$이 prime인지를 확인하기 위해서는, $R/2R$이 integral domain인지를 확인해보면 된다. 위의 식에 의하여,

$$R/2R\cong(\mathbb{Z}/\mathbb{Z})[x]/(x^2-x+6)$$

이고, $x^2-x+6$은 $\mathbb{Z}/2\mathbb{Z}[x]$에서 $x(x-1)$로 인수분해되므로 $2R$은 prime ideal이 아니다. 예를 들어, 두 nonzero element $x$, $x-1$의 곱은 $x^2-x=0$이 될 것이다. 이 관찰은 우리에게 두 ideal들

$$(2, \alpha),\qquad (2,\alpha-1)$$ 

을 가져다 준다. 이들이 prime ideal인 것은, 위와 같이 진행했을 때 quotient ring이 field $\mathbb{Z}/2\mathbb{Z}$가 나오므로 자명하고, 우리는 

$$(2)=(2,\alpha)(2,\alpha-1)$$

만 보이려 한다. 우선, $2=2\alpha-2(\alpha-1)$이므로, $(2)\subset (2,\alpha)(2,\alpha-1)$임은 자명하다. 한편, $(2,\alpha)(2,\alpha-1)$의 임의의 원소는 

$$x=4r_1+(2\alpha)r_2+2(\alpha-1)r_3\tag{2}$$

의 꼴인데 (여기서 $r_i\in R$), 이들은 어차피

$$x=2(2r_1+\alpha r_2+(\alpha-1)r_3)$$

으로 묶이므로, $x\in (2)$는 자명하다. $(3)$도 거의 똑같이 하면 된다. 조금 더 큰 수를 계산해보자. $(13)$에 대해서는, $x^2-x+6$이 $(x-5)(x-9)$으로 인수분해되는 것을 알 수 있다. 따라서, 위와 마찬가지로 두 개의 ideal $(13, \alpha-5)$, $(13, \alpha-9)$를 생각하는 아이디어 자체는 거의 똑같다. 그리고, 이들 ideal의 product $(13, \alpha-5)(13, \alpha-9)$에 속하는 원소들은 어차피 식 (2)와 비슷한 꼴에, 대신 13으로 묶이도록 되어 있으므로 유일한 문제는 $(13, \alpha-5)(13, \alpha-9)\supset(13)$을 보이는 것이다. $p=2$처럼, 숫자가 작을 때야 이게 별 문제가 안 되지만 여기서 직접 찾는 건 미련한 일이다. 대신, 우리는 두 polynomial $x-5$, $x-9$가 $\mathbb{Z}[x]$에서 coprime인 것을 알고 있고, 따라서 Bezout's lemma에 의하여 

$$f(x)(x-5)+g(x)(x-9)=1$$

이도록 하는 정수계수 다항식 $f,g$가 존재한다는 것을 안다. 이제

$$f(x)\cdot13(x-5)+g(x)\cdot13(x-9)=13$$

이 항상 성립하므로, $x=\alpha$를 대입하면 원하는 결과를 얻는다.  

</div>

---
**References**

[Jan] Gerald J. Janusz. *Algebraic Number Fields*, American  Mathematical Soc., 1995

---

[^1]: 더욱이, prime element의 정의에 의해 $k=1$이어야 한다. 
[^2]: 예를 들어, $R/\mathfrak{A}$는 $\mathfrak{A}$가 prime ideal이 아닌 이상 integral domain조차도 안 된다.
