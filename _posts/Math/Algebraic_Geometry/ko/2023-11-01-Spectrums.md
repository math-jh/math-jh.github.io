---

title: "스펙트럼"
excerpt: "환의 스펙트럼"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/spectrums
header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Spectrums.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_geometry-ko"

date: 2023-11-01
last_modified_at: 2023-11-01
weight: 1

---

대수기하학은 대수적인 대상에 기하적인 의미를 부여하여 대수적인 대상들을 더 잘 이해하게 해 주며, 반대로 기하적인 대상들을 다루는 대수적인 방법을 제공해주기도 한다. 이를 가능하게 하는 것은 스킴의 개념이며, 우리는 대수기하학 카테고리의 처음 몇 개의 글들에서 이를 정의할 것이다. 

대략적인 흐름은 다음과 같다. 미분다양체가 국소적으로는 유클리드 공간을 이어붙여 얻어지듯이, scheme은 국소적으로는 affine scheme을 이어붙여 얻어진다. 여기서 affine scheme이란 적당한 ring $A$의 *spectrum<sub>스펙트럼</sub>* $\Spec A$와 같은 것으로 취급할 수 있는 대상이며, 집합으로서 $\Spec A$는 $A$의 prime ideal들의 모임이며, 여기에 추가적으로 위상구조와 structure sheaf $\mathscr{O}_{\Spec A}$가 주어진다. 

이번 글에서 우리는 $\Spec A$에 적당한 종류의 위상구조와 structure sheaf를 정의한 후, 몇 가지 쉬운 ring에 대해 이들이 어떻게 생겼는지를 살펴본다. 앞으로 이 카테고리의 모든 글들에서 *ring*이라 하면 commutative ring (with unity)를 의미한다.

## $\Spec$ 함자

우선 위상공간으로서 $\Spec A$가 무엇인지를 정의해야 한다. Ring $A$의 prime ideal들의 집합을 $\Spec A$로 적고, 임의의 ideal $\mathfrak{a}\leq A$에 대하여, $V(\mathfrak{a})$를 $\mathfrak{a}$를 포함하는 prime ideal들의 모임이라 하자. 

<div class="proposition" markdown="1">

<ins id="lem1">**보조정리 1**</ins> 다음이 성립한다.

1. $A$의 임의의 ideal $\mathfrak{a},\mathfrak{b}$에 대하여, $V(\mathfrak{ab})=V(\mathfrak{a})\cup V(\mathfrak{b})$가 성립한다.
2. $A$의 ideal들의 모임 $\\{\mathfrak{a}\_i\\}$에 대하여, $V(\sum \mathfrak{a}\_i)=\bigcap V(\mathfrak{a}\_i)$가 성립한다.
3. $A$의 임의의 ideal $\mathfrak{a},\mathfrak{b}$에 대하여, $V(\mathfrak{a})\subseteq V(\mathfrak{b})\iff \sqrt{\mathfrak{a}}\supseteq \sqrt{\mathfrak{b}}$이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

1. $\mathfrak{a}$ 혹은 $\mathfrak{b}$를 포함하는 prime ideal $\mathfrak{p}$는 그보다 작은 ideal $\mathfrak{ab}$ 또한 포함하는 것이 자명하므로, 반대방향 포함관계만 보이면 충분하다. $\mathfrak{p}\supset \mathfrak{ab}$라 가정하자. 만일 $\mathfrak{p}\not\supseteq \mathfrak{b}$라 하면, $b\not\in \mathfrak{p}$인 $\mathfrak{b}$의 원소 $b$를 찾을 수 있다. 한편, 임의의 $a\in \mathfrak{a}$에 대하여, $ab\in \mathfrak{ab}\subseteq \mathfrak{p}$이고, 앞선 가정에 의해 $b\not\in \mathfrak{p}$이므로 반드시 $a\in \mathfrak{p}$이고 따라서 $a\subseteq \mathfrak{p}$가 성립한다.
2. 이는 $\sum \mathfrak{a}_i$가 ideal들 $\mathfrak{a}_i$ 각각을 모두 포함하는 ideal 중 가장 작은 것으로 정의되므로 자명하다.
3. Ideal $\mathfrak{a}$의 radical $\sqrt{\mathfrak{a}}$는 $\mathfrak{a}$를 포함하는 prime ideal들을 모두 교집합하여 얻어지므로 자명하다.

</details>

그럼 [\[위상수학\] §집합의 내부, 폐포, 경계, ⁋명제 2](/ko/math/topology/other_concepts#prop2)에 의하여, $V(\mathfrak{a})$들을 닫힌집합으로 갖는 유일한 위상 $\mathcal{T}$가 존재하여 $\Spec A$를 위상공간으로 만들어준다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 위와 같이 정의된 $\Spec A$의 위상을 *Zariski topology<sub>자리스키 위상</sub>*이라 부른다.

</div>

임의의 ring homomorphism $\phi:A \rightarrow B$가 주어졌다 하자. 그럼 $B$의 임의의 prime ideal $\mathfrak{q}$에 대하여 $\phi^{-1}(\mathfrak{q})$는 $A$의 prime ideal이다. ([\[대수적 구조\] §분수체, ⁋명제 9](/ko/math/algebraic_structures/field_of_fractions#prop9)) 이로부터 $\phi$는 $\Spec B$에서 $\Spec A$로의 함수 

$$f: \Spec B \rightarrow \Spec A;\qquad \mathfrak{q}\mapsto \phi^{-1}(\mathfrak{q})\tag{1}$$

를 정의한다.

<div class="proposition" markdown="1">

<ins id="lem3">**보조정리 3**</ins> 위의 식 (1)에 의해 정의되는 $f:\Spec B \rightarrow \Spec A$는 연속함수이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

이를 위해서는 $\Spec A$의 임의의 닫힌집합을 가져왔을 때, 이 닫힌집합의 $f$에 의한 preimage도 $\Spec B$에서의 닫힌집합임을 보이면 충분하다. ([\[위상수학\] §집합의 내부, 폐포, 경계, ⁋명제 2](/ko/math/topology/other_concepts#prop2))

한편 $\Spec A$의 임의의 닫힌집합은 모두 $V(\mathfrak{a})$의 꼴이고, $\Spec B$의 닫힌집합은 모두 $V(\mathfrak{b})$의 꼴이므로 이를 보이기 위해서는 임의의 $A$의 ideal $\mathfrak{a}$가 주어질 때마다 다음의 식

$$f^{-1}(V(\mathfrak{a}))=V(\mathfrak{b})$$

을 만족하는 $B$의 ideal $\mathfrak{b}$가 존재함을 보이면 충분하다. 우리의 주장은 다음의 식

$$f^{-1}(V(\mathfrak{a}))=V(\phi(\mathfrak{a}))$$

이 성립한다는 것이다. 그럼 $\phi(\mathfrak{a})$로 생성되는 ideal이 위의 식을 만족하므로 증명이 완료된다. 

우선 $\mathfrak{q}\in\Spec B$가 좌변에 속한다 하자. 즉 $f(\mathfrak{q})=\phi^{-1}(\mathfrak{q})\in V(\mathfrak{a})$가 성립한다. 그럼 $\mathfrak{a}\subseteq \phi^{-1}(\mathfrak{q})$인 것으로부터 $\phi(\mathfrak{a})\subseteq \mathfrak{q}$이므로 $\mathfrak{q}\in V(\phi(\mathfrak{a}))$이 성립한다.

거꾸로 $\mathfrak{q}\in\Spec B$가 우변에 속한다 하자. 그럼 $\phi(\mathfrak{a})\subseteq \mathfrak{q}$인 것으로부터, 다음의 포함관계

$$\mathfrak{a}\subseteq \phi^{-1}(\phi(\mathfrak{a}))\subseteq\phi^{-1}(\mathfrak{q})=f(\mathfrak{q})$$

를 얻고 이것이 곧 $f(\mathfrak{q})\in V(\mathfrak{a})$, 즉 $\mathfrak{q}\in f^{-1}(V(\mathfrak{a}))$임을 증명한다. 

</details>

따라서 $\Spec$은 $\cRing$에서 $\Top$으로의 contravariant functor로 생각할 수 있다. 앞서 언급했듯, $\Spec A$는 단순한 위상공간이 아니라 *structure sheaf*라 불리는 특정한 sheaf가 추가적인 데이터로 주어진 공간인데, 이를 올바르게 정의하고 나면 $\Spec$이 $\cRing$에서 *locally ringed space*들의 category로의 contravariant functor라고 이야기할 수 있다. 

## 자리스키 위상의 부분공간

$\Spec$이 contravariant functor라는 것으로부터, surjective ring homomorphism $\phi: A \rightarrow B$가 주어질 때마다 위상공간 사이의 continuous injection $f:\Spec B \hookrightarrow \Spec A$가 주어진다는 것을 안다. 즉, $f$를 통해 $\Spec B$를 $\Spec A$의 부분공간으로 생각할 수 있다. 

<div class="proposition" markdown="1">

<ins id="cor4">**따름정리 4**</ins> Ring $A$와 임의의 ideal $\mathfrak{a}$에 대하여, $\Spec A/\mathfrak{a}$는 $\Spec A$의 부분공간이다.

</div>

뿐만 아니라, 위의 경우에는 $\Spec A/\mathfrak{a}$가 어떠한 점들로 이루어져 있는지까지 서술할 수 있는데, [\[대수적 구조\] §몫환, 환 동형사상, ⁋정리 3](/ko/math/algebraic_structures/quotient_rings#thm3)의 네 번째 결과와 [\[대수적 구조\] §분수체, ⁋명제 9](/ko/math/algebraic_structures/field_of_fractions#prop9)를 종합하면 $A/\mathfrak{a}$의 prime ideal들의 모임과, $\mathfrak{a}$를 포함하는 $A$의 prime ideal들의 모임 사이의 inclusion-preserving bijection이 존재하기 때문이다. 

한편, 우리는 [\[가환대수학\] §국소화, ⁋명제 7](/ko/math/commutative_algebra/localization#prop7)로부터 $A$의 localization $S^{-1}A$의 prime ideal과 $A$의 prime ideal들 사이에도 위와 비슷한 관계가 있다는 것을 안다. 즉, $S^{-1}A$의 prime ideal들과, $S$와 만나지 않는 $A$의 prime ideal들 사이의 inclusion-preserving bijection이 존재한다. 이로부터 다음을 얻는다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> Ring $A$와 $A$의 multiplicative subset $S$에 대하여, $\Spec S^{-1}A$는 $\Spec A$의 부분공간이다.

</div>

## 자리스키 위상의 예시들

지금까지 살펴본 정의들과 명제들만으로는 명확한 기하학적 의미를 얻는 것이 쉽지 않다. 이를 해소하기 위해 몇 가지 예시를 살펴본다. 주의할 점은 우리가 일반적으로 생각하는 공간과 이들 스펙트럼들이 조금은 다른 점들이 있다는 것인데, 가령 대부분의 위상공간에서 점들은 모두 closed point, 즉 다음 식

$$\cl(\ast)=\{\ast\}$$

을 만족하는 점들이지만 스펙트럼에서는 그렇지 않은 점들이 존재한다.  

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> $A=\mathbb{Z}$인 경우를 생각하면, $A$의 prime ideal은 소수 $p$에 대해 $(p)=p\mathbb{Z}$, 그리고 zero ideal $(0)$ 뿐이다. 그럼 $(p)$를 포함하는 prime ideal은 오직 $(p)$ 자기자신 뿐이고, 따라서 각각의 $(p)$들은 모두 closed point들이다. 

반면, $(0)$은 $\mathbb{Z}$의 임의의 ideal에 포함되어 있으므로 $V((0))=\Spec \mathbb{Z}\neq \\{(0)\\}$이다. 즉 $(0)$은 closed point가 아니다.

</div>

위의 예시로부터 두 가지 관찰을 할 수 있다. 우선 하나는 $A$의 maximal ideal들은 항상 closed point가 된다는 것이다. 다른 하나는 임의의 integral domain $A$에서는 $(0)$이 prime ideal이므로, 항상 위와 같은 일이 일어난다는 것이다. 

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> Field $\mathbb{k}$의 ideal은 $(0)$과 자기자신뿐이며, 따라서 $\Spec \mathbb{k}$는 한 점 $(0)$으로만 이루어진 공간이다. 

</div>

이 예시는 별 의미가 없는 것처럼 보일 수도 있지만, [따름정리 4](#cor4) 및 [명제 5](#prop5)와 결합하면 기하적인 의미를 갖고 있다. 

우리는 ring $A$의 임의의 prime ideal $\mathfrak{p}$에 대하여, 다음의 ring homomorphism

$$A \rightarrow A_\mathfrak{p} \rightarrow A_\mathfrak{p}/\mathfrak{p}A_\mathfrak{p}=\kappa(\mathfrak{p})$$

을 알고 있다. ([\[가환대수학\] §국소화, §§국소화와 아이디얼](/ko/math/commutative_algebra/localization#국소화와-아이디얼)) 여기서 $A\rightarrow \kappa(\mathfrak{p})$에 $\Spec$을 취하면 다음의 함수

$$\Spec\kappa(\mathfrak{p})\rightarrow\Spec A$$

를 얻고, [따름정리 4](#cor4) 와 [명제 5](#prop5)를 통해 $\Spec\kappa(\mathfrak{p})$를 $\Spec A$의 부분공간으로 생각할 수 있다. 그런데 $\kappa(\mathfrak{p})$는 field이므로, 이는 단순히 $\Spec A$의 한 점에 불과하며 이 때 $\Spec\kappa(\mathfrak{p})$의 (유일한) 한 점 $(0)$이 어디로 가는지를 추적해보면 정확히 $\mathfrak{p}\in\Spec A$로 가는 것을 알 수 있다. 

아마도 가장 기하적인 직관에 도움이 되는 예시는 [예시 9](#ex9)일텐데, 그 전에 다음 예시를 먼저 살펴보자.

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> Field $\mathbb{k}$ 위에 정의된 polynomial algebra $\mathbb{k}[\x]$를 생각하자. $\mathbb{k}[\x]$는 PID이므로, 이 ring의 임의의 ideal은 항상 적당한 $p(\x)\in \mathbb{k}[\x]$에 대하여 $(p(\x))$의 꼴로 적을 수 있다. 여기에 더하여, 편의상 $\mathbb{k}$가 algebraically closed field라 가정하면 $p(\x)$를 항상 일차식들의 곱으로 인수분해할 수 있으며 이로부터 $\mathbb{k}[\x]$의 유일한 prime ideal은 오직 일차식들로 만들어지는 ideal들

$$(\x-x),\qquad x\in \mathbb{k}$$

그리고 $(0)$ 뿐임을 알 수 있다. [예시 6](#ex6)와 마찬가지로 각각의 $(\x-x)$들은 모두 closed point이지만 $(0)$을 포함하는 닫힌집합 $V((0))$은 전체집합이 된다. 

</div>

위의 예시에서 알 수 있듯, 임의의 prime ideal $\mathfrak{p}$가 closed point이기 위해서는 $V(\mathfrak{p})=\\{\mathfrak{p}\\}$여야 하고, 이는 곧 $\mathfrak{p}$가 maximal ideal이어야 한다는 뜻이다. 다음 예시를 살펴보자.

<div class="example" markdown="1">

<ins id="ex9">**예시 9**</ins> $A=\mathbb{k}[\x_1,\ldots, \x_n]$인 경우를 생각하자. 그럼 [\[가환대수학\] §영점정리, ⁋보조정리 4](/ko/math/commutative_algebra/nullstellensatz#lem4)에 의하여, $A$의 maximal ideal들은 오직 다음의 꼴

$$(\x_1-x_1,\ldots, \x_n-x_n),\qquad x_i\in \mathbb{k}$$

의 ideal들 뿐임을 안다. 따라서, $A$의 maximal ideal들과 $\mathbb{k}^n$의 점들 사이의 일대일대응

$$(\x_1-x_1,\ldots, \x_n-x_n) \quad \leftrightarrow\quad (x_1,\ldots,x_n)$$

이 존재한다. 즉 $\Spec A$의 closed point들은 정확히 좌표공간의 점들을 의미한다.

한편 $A$는 또 다른 prime ideal들을 가지는데, 예를 들어 irreducible polynomial $f(\x_1,\ldots,\x_n)\in A$에 대하여 $(f)$는 $A$의 prime ideal이 된다. 만일 $(x_1,\ldots,x_n)$이 식

$$f(x_1,\ldots, x_n)=0$$

을 만족한다면, 이는 기하적으로는 점 $(x_1,\ldots,x_n)$이 방정식 $f(\x_1,\ldots, \x_n)=0$이 정의하는 hypersurface에 속한다는 뜻이 된다. 

</div>



---
**참고문헌**

**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/). 

---
