---

title: "스킴의 대수구조"
excerpt: ""

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/algebra_of_schemes
header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Algebra_of_schemes.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_geometry-ko"

date: 2025-02-05
last_modified_at: 2025-02-11
weight: 6

---

스킴은 기하적인 동시에 대수적인 대상이므로, 이를 잘 알기 위해서는 앞선 글에서 살펴본 스킴의 위상구조 뿐만 아니라 대수적인 구조도 동시에 고려할 필요가 있으며, 우리는 이전 글에서 이러한 철학이 어떻게 반영되는지를 간략하게 살펴보았다. 이번 글에서는 이 철학을 더욱 발전시킨다. 

## 축소스킴과 정역스킴

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Scheme $X$가 *reduced scheme<sub>축소스킴</sub>*인 것은 임의의 열린집합 $U$에 대하여 $\mathscr{O}\_X(U)$가 reduced인 것이다. ([\[대수적 구조\] §분수체, ⁋정의 11](/ko/math/algebraic_structures/field_of_fractions#def11)) 비슷하게, $X$가 *integral<sub>정역스킴</sub>*인 것은 임의의 열린집합 $U$에 대하여 $\mathscr{O}_X(U)$가 integral domain인 것이다. ([\[대수적 구조\] §분수체, ⁋정의 5](/ko/math/algebraic_structures/field_of_fractions#def5))

</div>

그럼 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="lem2">**보조정리 2**</ins> Scheme $X$가 reduced scheme인 것은 임의의 $x\in X$에 대하여 $\mathscr{O}\_{X, x}$가 reduced ring인 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 reduced scheme $X$의 임의의 점 $x\in X$에 대하여, $x$를 포함하는 affine open subscheme $U=\Spec A$를 생각하자. $\Spec A$ 안에서 $x$에 대응되는 prime ideal을 $\mathfrak{p}$라 하면

$$\mathscr{O}_{X,x}=(\mathscr{O}_X\vert_U)_x\cong \mathscr{O}_{\Spec A, \mathfrak{p}}\cong A_\mathfrak{p}$$

이고, 가정에 의해 $\mathscr{O}\_X(U)\cong A$가 reduced이므로 $A\_\mathfrak{p}$ 또한 reduced이다. 

거꾸로 임의의 $x\in X$에 대하여 $\mathscr{O}\_{X,x}$가 reduced라 하면, 임의의 열린집합 $U$에 대하여 다음 inclusion

$$\mathscr{O}_X(U)\hookrightarrow\prod_{x\in U} \mathscr{O}_{X,x}$$

을 생각하면 $\mathscr{O}_X(U)$가 reduced인 것을 확인할 수 있다. 

</details>

이로부터 reducedness는 stalk-local property인 것을 안다. ([§스킴의 위상구조, ⁋명제 16](/ko/math/algebraic_geometry/topology_of_schemes#prop16)) 또, 만일 ring $A$가 reduced라면 그 localization도 reduced임을 쉽게 보일 수 있으므로, reduced ring의 spectrum은 reduced라는 것을 보일 수 있다. 

비슷하게 integral domain의 spectrum은 integral scheme이다. 이는 직접 보이는 것도 어렵지 않지만, [명제 4](#prop4)에서 우리는 scheme $X$가 integral인 것과, scheme $X$가 irreducible, reduced scheme인 것이 동치인 것을 증명한다. 그럼 integral domain $A$의 spectrum $\Spec A$는

1. $A$가 reduced ring이므로 reduced scheme이고,
2. $A$가 유일한 minimal prime ideal $\\{0\\}$을 가지므로 irreducible이다.

즉, 이를 받아들인다면 integral domain의 spectrum이 integral scheme이라는 것을 볼 수 있다. 

[명제 4](#prop4)의 증명을 위해서는 irreducibility를 다음과 같이 대수적인 언어로 풀어쓰는 것이 좋다.

<div class="proposition" markdown="1">

<ins id="lem3">**보조정리 3**</ins> Affine scheme $\Spec A$가 irreducible인 것은 nilradical $\mathfrak{N}(A)$가 prime ideal인 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$\Spec A$가 irreducible인 것은 이 공간의 임의의 두 basis $D(f),D(g)\neq\emptyset$에 대하여 $D(fg)\neq\emptyset$인 것과 동치이다. 그런데 다음 동치관계

$$D(f)\neq\emptyset\iff f\not\in \mathfrak{p}\text{ for some $\mathfrak{p}$}\iff f\not\in \mathfrak{N}(A)$$

로부터, ([\[대수적 구조\] §분수체, ⁋명제 14](/ko/math/algebraic_structures/field_of_fractions#prop14)) 명제 $D(f),D(g)\neq\emptyset\implies D(fg)\not\in\emptyset$은 다음 명제

$$f,g\not\in \mathfrak{N}(A)\implies fg\not\in \mathfrak{N}(A)$$

와 동치임을 안다. 

</details>

이제 다음을 얻는다. 

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $X$가 integral인 것과, $X$가 reduced, irreducible인 것이 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $X$가 integral이라 하자. 임의의 integral domain은 항상 reduced이므로 $X$는 reduced scheme이다. 만일 $X$가 irreducible scheme이 아니라 하면, 서로소이고 공집합이 아닌 두 열린집합 $U_1,U_2\neq\emptyset$가 존재한다. 그럼 열린집합 $U_1\cup U_2$에 대하여

$$\mathscr{O}_X(U_1\cup U_2)=\mathscr{O}_X(U_1)\times \mathscr{O}_X(U_2)$$

이고, 우변은 integral domain이 아니므로 이는 $X$가 integral이라는 가정에 모순이다.

거꾸로 irreducible reduced scheme $X$가 주어졌다 하고, $X$가 integral scheme임을 보이자. 즉, $X$의 임의의 열린집합 $U$가 주어졌을 때, $\mathscr{O}_X(U)$가 integral domain임을 보여야 한다. 우선 다음 주장을 보이자.

**주장** 임의의 affine open subset $\Spec A\cong V\subseteq X$에 대하여, $\mathscr{O}\_X(V)\cong A$는 항상 integral domain이다. 
> $X$가 reduced라는 가정으로부터 $A$가 reduced ring이어야 하는 것을 안다. 한편, $X$는 $X$의 irreducible closed subset이므로 $V$도 irreducible이고 ([\[위상수학\] §차원, ⁋명제 13](/ko/math/topology/dimension#prop14)) 따라서 [보조정리 3](#lem3)으로부터 $\mathfrak{N}(A)=0$는 prime ideal이 되어 $A$가 integral domain이다. 

이제 일반적으로 $X$의 임의의 열린집합 $U$에 대하여 $\mathscr{O}\_X(U)$가 integral domain임을 보인다. 이를 위해 두 원소 $f,g\in \mathscr{O}\_X(U)$가 $fg=0$을 만족한다고 하자. 그럼 $U$의 두 열린집합

$$D_U(f)=\{x\in U\mid f_x\not\in \mathfrak{m}_x\},\qquad D_U(g)=\{x\in U\mid g_x\not\in \mathfrak{m}_x\}$$

와 이들의 여집합 $Z_U(f), Z_U(g)$에 대하여 $U=Z_U(f)\cup Z_U(g)$가 성립한다. 이제 $X$가 irreducible이므로, [\[위상수학\] §차원, ⁋명제 13](/ko/math/topology/dimension#prop14)으로부터 그 열린집합 $U$ 또한 마찬가지라는 것을 알고 따라서 $Z_U(f)=U$이거나 $Z_U(g)=U$여야 한다. 일반성을 잃지 않고 $Z_U(f)=U$라 하자. 그럼 $U$의 임의의 open affine subset $V$에 대하여, $V$에서

$$D_V(f)=\{x\in V\mid f_x\not\in \mathfrak{m}_x\}$$

로 정의하면 $D_V(f)=D_U(f)\cap V=D(f\vert_{U\cap D_U(f)})\subseteq V$이고, 이것이 공집합이기 위해서는 $f\vert_{U\cap D_U(f)}$가 $\mathscr{O}_X(V)$의 nilpotent element이다. 그런데 $\mathscr{O}\_X(V)$는 위의 주장에 의하여 integral domain이므로, 이로부터 $f\vert_{U\cap D_U(f)}=0$이어야 함을 알고, 이것이 $U$의 임의의 open affine subset $V$에 대해 성립하므로 $f=0$이어야 한다. 

</details>

한편 [§스킴의 위상구조, ⁋예시 6](/ko/math/algebraic_geometry/topology_of_schemes#ex6)을 보면, 임의의 scheme $X$의 irreduciblity를 stalk만 보아서는 판단할 수 없다는 것을 안다. 가령 $Z(\x(\x-1))$는 두 개의 component로 쪼개지므로 각 component의 점은 다른 component의 점에 대한 정보를 알지 못한다. 따라서 integrality 또한 stalk만 보아서는 판단하지 못한다. 

그러나 만일 $X$가 *connected* scheme이었다면, irreducible component들은 반드시 어떠한 점에서는 만나야 하고, 이 점에서의 stalk을 보면 irreducibility를 판단할 수도 있을 것이다. 다음 명제는 이 아이디어를 엄밀하게 적은 것이다. 


<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> Noetherian scheme $X$가 integral인 것과, $X$가 nonempty, connected이고 각각의 $\mathscr{O}_{X,x}$가 integral domain인 것이 동치이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $X$가 integral이라면 $X$는 irreducible이므로 connected이고, 또 integral domain의 localization은 integral domain이므로 한쪽 방향은 자명하다.

반대쪽 방향의 경우, scheme $X$가 reduced인 것은 임의의 integral domain이 reduced이고, reducedness가 stalk-local property이기 때문에 자명하다. 따라서 주어진 조건을 사용하여 $X$가 irreducible이라는 것을 보이면 나머지는 [명제 4](#prop4)로부터 자명하다.

우선 $X$가 noetherian scheme이므로 적당한 noetherian ring들 $A_1,\ldots, A_r$이 존재하여 $X=\bigcup \Spec A\_i$라 할 수 있다. 또, $X$는 위상공간으로서 noetherian이고, 따라서 [\[위상수학\] §차원, ⁋명제 12](/ko/math/topology/dimension#prop13)에 의하여 $X$는 유한히 많은 irreducible component를 갖는다. 이제

$$X=\bigcup_{j=1}^s X_j\tag{$\ast$}$$

가 $X$를 irreducible component들로 분해한 것이라 하면, 고정된 $i$에 대하여 다음 집합들

$$X_1\cap \Spec A_i,\quad X_2\cap \Spec A_i,\quad\ldots,\quad X_s\cap \Spec A_i$$

중 공집합이 아닌 것들은 $\Spec A_i$의 irreducible component들이 된다. 이제 [§스펙트럼, ⁋명제 16](/ko/math/algebraic_geometry/spectrums#prop16)에 의하여, 이들 각각은 minimal prime ideal $\mathfrak{q}_j=I(X_j)$를 정의하며 거꾸로 $A_i$의 임의의 minimal prime ideal은 irreducible component $X_j\cap \Spec A_i$를 유일하게 결정한다. 

한편, $X$는 connected이므로, irreducible decomposition ($\ast$)에서 다음의 교집합

$$X_1\cap \bigcup_{j=2}^s X_j$$

를 생각하면 이는 $X$의 공집합이 아닌 두 열린집합들의 교집합이고, $X$가 connected이므로 이들은 반드시 어떠한 점 $x$에서 만나야 한다. 즉, 적당한 $j$가 존재하여 $x\in X_1\cap X_j$이다. 이제 점 $x$를 포함하는 $X$의 affine cover를 $\Spec A_i$라 하고, 이 때 $x$가 prime ideal $\mathfrak{p}$에 대응된다 하자. 즉

$$x\in \Spec A_i\cap X_1\cap X_j=(\Spec A_i\cap X_1)\cap (\Spec A_i\cap X_j)$$

이다. 이제 앞선 논증으로부터 $\Spec A_i\cap X_1$은 generic point $\mathfrak{q}\_1$을, $\Spec A_i\cap X_j$는 generic point $\mathfrak{q}\_j$를 가지며, 이들은 $A_i$의 minimal prime ideal이다. 이제 $x$에서의 stalk $\mathscr{O}_{X,x}\cong (A\_i)\_\mathfrak{p}$를 생각하면, $\mathfrak{q}_1,\mathfrak{q}_2$의 minimality로부터 $\mathfrak{q}\_1,\mathfrak{q}\_2\subseteq \mathfrak{p}$이고 따라서 $\mathfrak{q}\_1 A_i, \mathfrak{q}\_2 A_i$는 각각 $A_i$의 minimal prime ideal이 된다. ([\[가환대수학\] §국소화, ⁋명제 8](/ko/math/commutative_algebra/localization#prop8)) 그런데 integral domain은 유일한 minimal prime ideal $(0)$을 가지므로 이는 $\mathscr{O}\_{X,x}$가 integral domain이라는 가정에 모순이다.

</details>

위의 증명에서 핵심적인 논리는 

1. $X$가 connected이므로, $X$를 irreducible component들로 분해하면 각각의 irreducible component는 다른 irreducible component와 반드시 만나야 하고[^1]
2. 두 irreducible component가 만나는 점을 $x$라 하고 $x$의 임의의 열린집합을 잡으면 이 열린집합은 각각의 irreducible component의 generic point를 포함할 것이며 ([§스펙트럼, ⁋명제 16](/ko/math/algebraic_geometry/spectrums#prop16)),
3. 따라서 이들 generic point들은 $x$에서의 stalk $\mathscr{O}\_{X,x}$에서도 살아있지만, 이것은 $\mathscr{O}\_{X,x}$가 integral domain이므로 불가능하다.

는 것으로 요약할 수 있다. 이 generic point에 대한 성질은 이 글의 마지막에서 살펴본다. 

## 정규스킴

Integral scheme과 비슷하게 다음을 정의할 수 있다.

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> Scheme $X$가 *normal<sub>정규스킴</sub>*인 것은 임의의 $x\in X$에 대하여 $\mathscr{O}\_{X,x}$가 normal domain인 것이다. ([\[가환대수학\] §정수적 확장, ⁋정의 3](/ko/math/commutative_algebra/integral_extension#def3))

</div>

일반적으로 normal domain의 localization은 항상 normal domain이다. ([\[가환대수학\] §정수적 확장, ⁋명제 12](/ko/math/commutative_algebra/integral_extension#prop12)) 이로부터 normal domain $A$의 스펙트럼 $\Spec A$는 normal scheme인 것을 안다. 

임의의 integral domain은 항상 reduced이고, [보조정리 2](#lem2)로부터 reducedness는 stalk에서 확인할 수 있으므로 임의의 normal scheme은 reduced이다. 반면 integral scheme이 되는 것은 stalk-local property가 아니므로 일반적으로 normal scheme이 항상 integral scheme이 되는 것은 아니다. 그러나 만일 $X$가 connected, nonempty Noetherian scheme이라면 [명제 5](#prop5)에 의해 normality가 integrality를 함의하는 것을 안다. 

한편, 우리는 unique factorization domain은 항상 normal domain인 것을 안다. ([\[가환대수학\] §정수적 확장, ⁋명제 9](/ko/math/commutative_algebra/integral_extension#prop9)) 이로부터 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> Scheme $X$가 *factorial*인 것은 임의의 $x\in X$에 대하여 $\mathscr{O}\_{X,x}$가 unique factorization domain인 것이다.

</div>

따라서 임의의 factorial scheme은 normal scheme이다. 또, unique factorization domain의 localization은 unique factorization domain이므로 unique factorization domain $A$의 spectrum $\Spec A$는 factorial이다. 

## 동반소아이디얼

우리는 [§스펙트럼, ⁋따름정리 17](/ko/math/algebraic_geometry/spectrums#cor17)에 의해, scheme $X=\Spec A$의 irreducible component와 ring $A$의 minimal prime ideal 사이의 일대일대응이 존재하는 것을 안다. 이는 위의 [명제 5](#prop5)에서 중요하게 사용되었다.

한편 대수적으로 minimal prime ideal은 항상 associated prime ideal이 된다. 이는 ring $A$를 자기 자신 위의 module로 보면 $\ann A=\\{0\\}$이므로 [\[가환대수학\] §동반소아이디얼, ⁋정리 7](/ko/math/commutative_algebra/associated_primes#thm7)를 적용하면 확인할 수 있다. 따라서 우리는 (locally noetherian) scheme의 associated point를 다음과 같이 정의한다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> Locally noetherian scheme $X$의 한 점 $x$와 $x$의 affine open neighborhood $U\cong \Spec A$에 대하여, $x$가 $X$의 *associated point<sub>동반점</sub>*이라는 것은 $x$에 대응되는 prime ideal $\mathfrak{p}_x\subset A$가 $A$의 associated prime ideal인 것이다. 

</div>

그럼 이 정의는 $U$의 선택에 의존하지 않으며, 뿐만 아니라 stalk-local하게 쓸 수도 있다. 이는 우선 $x$를 포함하는 affine open neighborhood $\Spec A$에 대하여, $X$가 locally noetherian scheme이라는 조건으로부터 $A$가 noetherian ring이라 가정하면 [\[가환대수학\] §동반소아이디얼, ⁋정리 7](/ko/math/commutative_algebra/associated_primes#thm7)의 셋째 조건으로부터 $\mathfrak{p}\_x$에 포함된 $A$의 associated prime ideal들의 모임과 $A\_{\mathfrak{p}\_x}$의 associated prime ideal들 사이의 일대일대응이 존재하는 것을 알고, 이 일대일대응으로부터 [정의 8](#prop8)을

> Locally noetherian scheme $X$의 한 점 $x$에 대하여, $x$가 $X$의 *associated point<sub>동반점</sub>*이라는 것은 $\mathfrak{m}\_x$가 $\mathscr{O}\_{X,x}$의 associated prime ideal인 것이다.

으로 바꾸어 쓸 수 있기 때문이다. 

이제 [\[가환대수학\] §동반소아이디얼, ⁋정리 7](/ko/math/commutative_algebra/associated_primes#thm7)의 첫째 조건은 만일 $X$가 quasicompact locally noetherian scheme일 경우, 즉 $X$가 noetherian scheme일 경우 associated point들의 유한성 또한 보장해준다. 

또, 이 조건에 의하여, 임의의 minimal prime ideal은 associated prime ideal이므로 이 개념은 $\Spec A$에서의 generic point의 개념을 일반화한다. [정의 8](#def8)에 의하여 우리는 우리의 관심사를 noetherian ring의 spectrum $\Spec A$로 한정할 수 있다. 

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> Noetherian ring의 스펙트럼 $\Spec A$의 associated point들 중, $\Spec A$의 irreducible component들의 generic point에 해당하지 않는 것들을 *embedded point*라 부른다. 

</div>

한편, 정의에 의해 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> Noetherian ring의 스펙트럼 $\Spec A$의 associated point들은 적당한 $f\in A$에 대하여, $\supp(f)$의 irreducible component의 generic point이며, 그 역 또한 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 임의의 $g\in A$와 prime ideal $\mathfrak{q}\in \Spec A$에 대하여

$$\mathfrak{q}\in \supp(g)\iff g_\mathfrak{q}\neq 0\text{ in $A_\mathfrak{q}$}\iff \ann(g_\mathfrak{q})\neq A_\mathfrak{q}$$

이 성립한다. 그런데 [\[가환대수학\] §국소화, ⁋명제 5](/ko/math/commutative_algebra/localization#prop5)에 의하여

$$\ann(g_\mathfrak{q})=\ann(g)A_\mathfrak{q}$$

이므로, 마지막 조건은 $\ann(g)\setminus \mathfrak{q}=\emptyset$, 즉 $\mathfrak{q}\in Z(\ann(g))$와 동치이다. 이로부터 임의의 $g\in A$에 대해

$$\supp(g)=Z(\ann(g))$$

이 성립하는 것을 안다. 따라서 $\supp(g)$의 irreducible component와 $\ann(g)$를 포함하는 minimal prime ideal 사이의 일대일 대응이 존재한다. 

이제 $\Spec A$의 임의의 associated point $\mathfrak{p}$가 주어졌다 하면, 정의에 의해 적당한 $f\in A$가 존재하여 $\mathfrak{p}=\ann(f)$이다. 이제

$$\supp(f)=Z(\ann(f))=Z(\mathfrak{p})$$

이고, $\mathfrak{p}$가 $\ann(f)=\mathfrak{p}$의 minimal prime인 것은 자명하므로 $\mathfrak{p}$는 $\supp f$의 generic point이다. 이 논증은 위의 관찰을 바탕으로 반대로도 작동한다. 

</details>

위의 증명에서 사용한 식

$$\supp(f)=Z(\ann(f))$$

를 살펴보면, 만일 $A$가 integral domain이었다면 $\ann(f)$는 오직 $f=0$일 때만 $A$ 전체이고, 그렇지 않은 경우에는 $0$이 된다. 즉, 이 경우 $\supp(f)$는 $f$가 $0$인 경우만 공집합이고, 나머지 경우에는 $\Spec A$ 전체이며, 우리는 [명제 4](#prop4)에서 $\Spec A$가 irreducible임을 알고 있으므로 $\Spec A$의 유일한 associated point는 generic point $(0)$ 뿐임을 안다. 

더 일반적으로, $A$가 integral domain이 아니라면 $\ann(f)$가 $0$도, $A$도 아닌 경우가 존재하므로 embedded point가 존재할 가능성이 있다. 

<div class="example" markdown="1">

<ins id="ex11">**예시 11**</ins> Affine scheme $X=\Spec \mathbb{k}[\x_1,\x_2]/(\x_2^2, \x_1\x_2)$를 생각하자. 그럼 [§스펙트럼, ⁋보조정리 6](/ko/math/algebraic_geometry/spectrums)과 [§스펙트럼, ⁋명제 9](/ko/math/algebraic_geometry/spectrums#prop9)에 의하여, 집합으로서 

$$X= Z(\x_2^2,\x_1\x_2)=Z(\x_2^2)\cap Z(\x_1\x_2)=\{(0,0)\}$$

이다. 

</div>






한편 [\[가환대수학\] §동반소아이디얼, ⁋따름정리 4](/ko/math/commutative_algebra/associated_primes#cor4)의 둘쨰 결과에 의하여 다음의 함수

$$A \rightarrow \prod_\text{\scriptsize $\mathfrak{p}$ associated prime} A_\mathfrak{p}$$

는 ㅑnjective인 것을 안다. 

---
[^1]: 이 과정에서 $X$의 irreducible component들이 유한히 많기 때문에 각각의 component들이 열린집합임을 사용하였다. 