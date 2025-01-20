---

title: "차원"
excerpt: ""

categories: [Math / Commutative Algebra]
permalink: /ko/math/commutative_algebra/Krull_dimension
header:
    overlay_image: /assets/images/Math/Commutative_Algebra/Krull_dimension.png
    overlay_filter: 0.5
sidebar: 
    nav: "commutative_algebra-ko"

date: 2025-01-16
last_modified_at: 2025-01-16
weight: 16

---

## 차원의 정의

앞으로의 몇 개의 글에서 우리는 ring의 차원을 정의하고, 그 성질들을 살펴본다. 차원의 정의 자체는 어렵지 않다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Ring $A$의 *Krull dimension<sub>크룰 차원</sub>*은 $A$의 prime ideal들의 descending chain

$$\mathfrak{p}_r\supseteq \mathfrak{p}_{r-1}\supseteq\cdots\supseteq \mathfrak{p}_1\supseteq \mathfrak{p}_0$$

의 length $r$들의 supremum으로 정의하고, 이를 $\dim A$로 적는다. 만일 이러한 $r$이 존재하지 않는다면 $\dim A=\infty$로 정의한다.

</div>

간단히 ring $A$의 Krull dimension을 $A$의 dimension이라 부른다. 예를 들어, field $\mathbb{k}$는 유일한 prime ideal $(0)$을 가지므로 $\mathbb{k}$는 항상 $0$차원이다. 

더 일반적으로 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Ring $A$의 ideal $\mathfrak{a}$에 대하여, $\mathfrak{a}$의 dimension은

$$\dim \mathfrak{a}=\dim A/\mathfrak{a}$$

으로 정의한다. 

$A$의 prime ideal $\mathfrak{p}$에 대하여, $\mathfrak{p}$의 *codimension<sub>여차원</sub>* $\codim \mathfrak{p}$는 $A_\mathfrak{p}$의 차원으로 정의하며, 일반적인 ideal $\mathfrak{a}$의 경우 $\codim \mathfrak{a}$는 $\mathfrak{a}$를 포함하는 prime ideal들의 codimension들의 minimum으로 정의한다. 

마지막으로, 임의의 $A$-module $M$에 대하여 $M$의 dimension과 codimension을 $\ann(M)$의 dimension과 codimension으로 각각 정의한다.

</div>

다소 주의할 사항으로, 위의 정의를 따르면 $\mathfrak{a}$는 먼저 정의한 ideal로서의 dimension과, 이를 $A$-module로 봤을 때의 dimension의 두 가지 정의를 갖게 되는데, 이 두 정의가 주는 값이 다를 수 있다. 따라서 $\dim \mathfrak{a}$라는 표기법을 사용할 때에는 [정의 2](#def2)에서 먼저 정의한 것과 같이 $A$의 ideal로서의 dimension만 의미하기로 한다.

그럼 [§국소화, ⁋명제 8](/ko/math/commutative_algebra/localization#prop8)에 의하여 $\codim \mathfrak{p}$는 prime ideal $\mathfrak{p}$로부터 시작하는 decreasing chain

$$\mathfrak{p}=\mathfrak{p}_r\supseteq \mathfrak{p}_{r-1}\supseteq\cdots\supseteq \mathfrak{p}_1\supseteq \mathfrak{p}_0$$

의 길이의 supremum과 같다. 한편 그 이름과 같이, 다음의 식

$$\dim \mathfrak{a}+\codim \mathfrak{a}=\dim A$$

을 기대하는 것이 자연스러울 것이지만, 이는 일반적으로 성립하지 않는다.

## 차원의 계산

일반적으로 차원을 다를 때에는 ring $A$가 noetherian인 경우를 주로 다루게 된다. 가장 큰 이유 중 하나는 [정리 7](#thm7)이 noetherian ring에서만 성립하기 때문이다. 본격적으로 차원을 계산하기 전에, 간단한 예시를 먼저 살펴보자. 

우선 우리는 [§조르단-횔더 정리, ⁋정리 4](/ko/math/commutative_algebra/Jordan-Holder_theorem#thm4)의 첫째 조건과 셋째 조건 사이의 동치를 통해 $0$차원의 noetherian ring들이 어떠한 것인지는 정확히 알고 있다. 

<div class="proposition" markdown="1">

<ins id="cor3">**따름정리 3**</ins> Noetherian ring $A$에 대하여, $\dim A =0$인 것과 $A$가 artinian인 것이 동치이다. 

</div>

한편, 우리는 다음 명제에 의하여, 일반적으로 $\phi:A \rightarrow B$가 integral이면 dimension이 변하지 않는다는 것을 안다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $\phi: A \rightarrow B$가 integral이라 하자. 그럼 $\ker\phi$를 포함하는 $A$의 임의의 prime ideal $\mathfrak{p}$에 대하여, $\mathfrak{p}=\phi^{-1} \mathfrak{q}$이도록 하는 $B$의 prime ideal $\mathfrak{q}$이 존재한다. 뿐만 아니라, $B$의 임의의 ideal $\mathfrak{b}$에 대하여 $\dim \mathfrak{b}=\dim \phi^{-1} \mathfrak{b}$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

첫 번째 결과는 단순히 [§정수적 확장과 아이디얼, ⁋명제 1](/ko/math/commutative_algebra/lying_over_and_going_up#prop1)이다. 두 번째 결과의 경우, $\dim \mathfrak{b}\geq \dim \phi^{-1}\mathfrak{b}$는 [§정수적 확장과 아이디얼, ⁋명제 1](/ko/math/commutative_algebra/lying_over_and_going_up#prop1)의 두 번째 결과에 의해 성립하고, 반대방향 부등식은 [§정수적 확장과 아이디얼, ⁋따름정리 4](/ko/math/commutative_algebra/lying_over_and_going_up#cor4)에 의해 성립한다. 

</details>

이제 우리는 관심을 돌려 1차원에서 일어나는 일들을 살펴본다. 그 전에 다소 기술적인 다음의 정의를 내린다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Prime ideal $\mathfrak{p}\subseteq A$에 대하여, $\mathfrak{p}$의 *$n$th symbolic power* $\mathfrak{p}^{(n)}$을 다음 식

$$\mathfrak{p}^{(n)}=\{a\in A:\text{$ba\in \mathfrak{p}^n$ for some $b\in A\setminus \mathfrak{p}$}\}$$

으로 정의한다. 

</div>

정의에 의해 $\mathfrak{p}^{(n)}$은 localization $A \rightarrow A\_\mathfrak{p}$을 통해 ideal $(\mathfrak{p}A\_\mathfrak{p})^n$을 $A$로 옮겨온 것이다. 그럼 $\mathfrak{p}$ 바깥에 있는 원소들은 modulo $\mathfrak{p}^({n})$으로 non-zerodivisor가 되며, $\mathfrak{p}^{(n)}A\_\mathfrak{p}=(\mathfrak{p}A\_\mathfrak{p})^n$임이 자명하다. 또, symbolic power들의 descending chain

$$A=\mathfrak{p}^{(0)}\supseteq \mathfrak{p}=\mathfrak{p}^{(1)}\supseteq \mathfrak{p}^{(2)}\supseteq \mathfrak{p}^{(3)}\supseteq\cdots$$

이 존재한다. 

이제 다음 정리를 보일 수 있다.

<div class="proposition" markdown="1">

<ins id="thm6">**정리 6 (Codimension one Principal Ideal Theorem)**</ins> Noetherian ring $A$와 임의의 $a\in A$에 대하여, $\mathfrak{p}$가 principal ideal $\mathfrak{a}=(a)$를 포함하는 prime ideal들 중 minimal인 것이라 하자. 그럼 $\codim \mathfrak{p}\leq 1$이다. 

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

임의의 prime ideal $\mathfrak{q}\subsetneq \mathfrak{p}$에 대하여 $\codim \mathfrak{q}=0$임을 보이면 충분하며, 이는 다시 [§국소화, ⁋명제 8](/ko/math/commutative_algebra/localization#prop8)에 의하여 $\dim A_\mathfrak{q}=0$임을 보이면 된다. 

이제 $A\_\mathfrak{p}$에서 $\mathfrak{p}A\_\mathfrak{p}$는 유일한 maximal ideal이므로, $\mathfrak{p}$는 ideal들 $\mathfrak{q}A\_\mathfrak{p}$, $(\mathfrak{q}A\_\mathfrak{p})^{(n)}$, $\mathfrak{a}A_\mathfrak{p}$가 이 maximal ideal에 포함된다. 특히 우리는 다음의 두 chain

$$\mathfrak{a}A_\mathfrak{p}\subseteq (\mathfrak{q}A_\mathfrak{p})^{(n)}+\mathfrak{a}A_\mathfrak{p}\subseteq \mathfrak{p}A_\mathfrak{p},\qquad \mathfrak{q}A_\mathfrak{p}\subseteq \mathfrak{p}A_\mathfrak{p}$$

을 얻는다. 한편 $\mathfrak{p}A_\mathfrak{p}$가 $\mathfrak{a}A_\mathfrak{p}$를 포함하는 prime ideal들 중 minimal하므로, [§조르단-횔더 정리, ⁋따름정리 8](/ko/math/commutative_algebra/Jordan-Holder_theorem#cor8)에 의하여 $A_\mathfrak{p}/\mathfrak{a}A_\mathfrak{p}$는 artinian이다. 이로부터 symbolic power들로 이루어진 descending chain

$$(\mathfrak{q}A_\mathfrak{p})^{(1)}+\mathfrak{a}A_\mathfrak{p}\supseteq (\mathfrak{q}A_\mathfrak{p})^{(2)}+\mathfrak{a}A_\mathfrak{p}\supseteq\cdots $$

이 멈춰야 한다는 것을 안다. 따라서 $(\mathfrak{q}A\_\mathfrak{p})^{(n)}+\mathfrak{a}A\_\mathfrak{p}= (\mathfrak{q}A\_\mathfrak{p})^{(n+1)}+\mathfrak{a}A\_\mathfrak{p}$라 하자. 그럼 

$$(\mathfrak{q}A_\mathfrak{p})^{(n)}\subseteq (\mathfrak{q}A_\mathfrak{p})^{(n)}+\mathfrak{a}A_\mathfrak{p}= (\mathfrak{q}A_\mathfrak{p})^{(n+1)}+\mathfrak{a}A_\mathfrak{p}$$

이므로, 임의의 $f\in (\mathfrak{q}A\_\mathfrak{p})^{(n)}$는 다음의 꼴

$$f=\alpha a+g,\qquad g\in (\mathfrak{q}A_\mathfrak{p})^{(n+1)}=(\mathfrak{q}A_\mathfrak{p})^{(n)}$$

로 적을 수 있고 이로부터 $\alpha a\in (\mathfrak{q}A\_\mathfrak{p})^{(n)}$이어야 한다. 그런데 이 표현에서 $\mathfrak{p}$는 $\mathfrak{a}$를 포함하는 prime들 중 minimal한 것이므로, $a\not\in \mathfrak{q}$이고 따라서 $\alpha\in (\mathfrak{q}A\_\mathfrak{p})^{(n)}$이어야 한다. 즉, 다음의 식

$$(\mathfrak{q}A_\mathfrak{p})^{(n)}=\mathfrak{a}(\mathfrak{q}A_\mathfrak{p})^{(n)}+(\mathfrak{q}A_\mathfrak{p})^{(n+1)}$$

이 성립한다. 이제 이들을 $A\_\mathfrak{p}/(\mathfrak{q}A\_\mathfrak{p})^{(n+1)}$로 보내면 

$$(\mathfrak{q}A_\mathfrak{p})^{(n)}=\mathfrak{a}(\mathfrak{q}A_\mathfrak{p})^{(n)}\pmod{\mathfrak{q}^{(n+1)}}$$

이고, $a\in \mathfrak{p}A\_\mathfrak{p}=J(A\_\mathfrak{p})$이므로 [§정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)에 의하여 $(\mathfrak{q}A\_\mathfrak{p})^{(n)}=0\pmod{(\mathfrak{q}A\_\mathfrak{p})^{(n+1)}}$이다. 즉, $(\mathfrak{q}A\_\mathfrak{p})^{(n)}=(\mathfrak{q}A\_\mathfrak{p})^{(n+1)}$이다. 이제 이 식을 $\mathfrak{q}$에서 localize하면

$$(\mathfrak{q}A_\mathfrak{q})^{n+1}=(\mathfrak{q}A_\mathfrak{q})^{n}$$

이고, $\mathfrak{q}A_\mathfrak{q}=J(A_\mathfrak{q})$이므로 $(\mathfrak{q}A_\mathfrak{q})^{n}=0$이다. 이제 [§조르단-횔더 정리, ⁋따름정리 8](/ko/math/commutative_algebra/Jordan-Holder_theorem#cor8)의 둘째 조건과 셋째 조건의 동치로부터 $A\_\mathfrak{q}=A\_\mathfrak{q}/(0)$가 artinian이고, 따라서 [따름정리 3](#cor3)으로부터 $\dim A\_\mathfra{q}=0$임을 안다. 

</details>

이제 이를 이용해서 귀납적으로 다음을 보일 수 있다.

<div class="proposition" markdown="1">

<ins id="thm7">**정리 7 (Principal Ideal Theorem)**</ins> Noetherian ring $A$와 임의의 $a_1,\ldots, a_c\in A$에 대하여, $\mathfrak{p}$가 $a_1,\ldots, a_c$를 포함하는 prime ideal들 중 minimal인 것이라 하자. 그럼 $\codim \mathfrak{p}\leq c$이다. 

</div>

즉, noetherian ring의 임의의 prime ideal은 descending chain condition을 만족하며, 이 때 $\mathfrak{p}$에서 시작하는 chain의 길이는 $\mathfrak{p}$의 generator의 개수보다 작거나 같다. 그럼에도 불구하고 무한한 차원을 갖는 noetherian ring이 존재한다. (**[Nag, Appendix, Example 1]**)

한편 [정리 7](#thm7)은 다음과 같은 역 또한 존재한다.

<div class="proposition" markdown="1">

<ins id="cor8">**따름정리 8**</ins> Noetherian ring $A$에서, codimension $c$의 prime ideal $\mathfrak{p}$는 $c$개의 원소로 생성되는 어떠한 ideal을 포함하는 prime ideal들 중 minimal한 것이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

주장과 같이 $\mathfrak{p}$가 codimension $c$라 하자. 우리는 ($0$개의 원소로 생성되는) zero ideal $(0)$으로부터 시작하여, 원소들 $x_1,\ldots, x_r$을 귀납적으로 택하여 원하는 ideal을 만들 것이다. 이제 $0\leq r< c$를 만족하는 $r$에 대하여, $x_1,\ldots, x_r$로 생성되는 ideal을 만들었다 하자.  그럼 우리는 ideal $(x_1,\ldots, x_r)$을 포함하는 prime ideal들 중 어느 것에도 속하지 않는 적당한 $x_{r+1}\in \mathfrak{p}$를 택해야 한다. 이제 이는 

</details>

---

**참고문헌**

**[Eis]** David Eisenbud. *Commutative Algebra: with a view toward algebraic geometry*. Springer, 1995.  
**[Nag]** Masayoshi Nagata. *Local Rings*. Interscience publishers, 1962.

---