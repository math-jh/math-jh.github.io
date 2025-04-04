---

title: "군의 확장"
excerpt: ""

categories: [Math / Group Theory]
permalink: /ko/math/group_theory/extensions
header:
    overlay_image: /assets/images/Math/Group_Theory/Extensions.png
    overlay_filter: 0.5
sidebar: 
    nav: "group_theory-ko"

date: 2025-03-29
last_modified_at: 2025-03-29
weight: 2

---

이번 글에서 우리는 group의 extension에 대해 다룬다. 

## 군의 확장

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 두 group $G, F$에 대하여, $G$의 $F$에 의한 *extension<sub>확장</sub>* $\mathcal{E}$는 조건 $\ker p=\im i$를 만족하는 다음의 pair

$$\mathcal{E}: F\overset{i}{\hookrightarrow}E\overset{p}{\twoheadrightarrow}G$$

을 의미한다. 

</div>

이에 대한 직관은 다음의 pair

$$\mathcal{E}_0: F \rightarrow F\oplus G \rightarrow G$$

이며, 우리는 이를 *trivial extension*이라 부른다. 그러나 일반적으로 위의 상황에서 first isomorphism theorem에 의하여 다음의 식

$$G\cong E/\ker p=E/\im i$$

이 성립하지만, 그렇다고 하여

$$E\cong (E/i(F))\oplus i(F)$$

가 성립하는 것은 아니므로 주의할 필요가 있다. 어쨌든 이 계산으로부터 $E$가 $G$의 $F$에 의한 extension이기 위해서는 $E$의 적당한 normal subgroup $F'$가 존재하여, $F'$가 $F$와 isomorphic하고 $E/F'$는 $G$와 isomorphic한 것이 동치임을 안다. 

그럼 고정된 $G$와 $F$에 대하여, $G$의 $F$에 의한 extension들을 모두 모아둔 것은 category를 이룬다. 여기에서의 morphism은 다음과 같이 주어진다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 두 extension $\mathcal{E}_1: F \rightarrow E_1 \rightarrow G$과 $\mathcal{E}_2:F \rightarrow E_2 \rightarrow G$에 대하여, $\mathcal{E}_1$에서 $\mathcal{E}_2$로의 *morphism*은 다음의 diagram

![morphism_of_extensions](/assets/images/Math/Group_Theory/Extensions-1.png){:style="width:10.5em" class="invert" .align-center}

을 commute하도록 하는 $u:E_1 \rightarrow E_2$를 의미한다.  

</div>

그럼 만일 $u:E_1 \rightarrow E_2$가 group homomorphism으로서 isomorphism이라면, $u$의 inverse $u^{-1}: E_2 \rightarrow E_1$ 또한 [정의 2](#def2)의 조건을 만족하고 따라서 $u$는 extension들 사이의 morphism으로서 isomorphism이라는 것을 확인할 수 있다. 

앞선 정의를 확장하여, 다음을 정의한다. 

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> $G$의 $F$에 의한 extension $\mathcal{E}:F \rightarrow E \rightarrow G$이 extension

$$\mathcal{E}_0:F \rightarrow F\oplus G \rightarrow G$$

과 isomorphic하다면, 이를 *trivial extension*이라고 부른다. 

</div>

그럼 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> Extension $\mathcal{E}:F \rightarrow E \rightarrow G$에 대하여, 다음이 모두 동치이다.

1. $\mathcal{E}$가 trivial extension이다.
2. Retraction $r: E \rightarrow F$가 존재한다. 
3. Section $s: G \rightarrow E$가 존재하여 $s(G)$가 $i(F)$의 centralizer에 포함되도록 할 수 있다. 

</div>

물론 여기에서 retraction과 section은 단순한 함수가 아니라 group homomorphism을 의미한다. ([\[집합론\] §Retraction과 section, ⁋정의 2](/ko/math/set_theory/retraction_and_section#def2))

<details class="proof--alone" markdown="1">
<summary>명제 4의 증명</summary>

우선 첫째 조건을 가정하고 다음의 diagram

![retraction_and_section](/assets/images/Math/Group_Theory/Extensions-2.png){:style="width:12em" class="invert" .align-center}

를 생각하자. 그럼 이로부터 retraction $r:E \rightarrow F$를 $\pr_1\circ u$로, $s:G \rightarrow E$를 $u^{-1}\circ\iota_2$로 정의하면 된다.

거꾸로 둘째 조건이 성립한다 가정하자. 그럼 $(r,p): E \rightarrow F\oplus G$가 주어진 extension과 $F \rightarrow F\oplus G \rightarrow G$ 사이의 isomorphism이 된다. 비슷하게 셋째 조건을 가정하자. 그럼 $s(G)$가 $i(F)$의 centralizer에 포함되므로 $F\oplus G$에서 $F$와 $G$의 weak direct product를 거친 후 $E$로 가는 morphism을 만들 수 있다. 

</details>

만일 $i(F)$가 $E$의 center $C(E)$에 포함되었다면, 세 번째 조건에서 $s(G)$와 $i(F)$의 관계는 무시하여도 좋을 것이다. ([\[대수적 구조\] §군의 작용, ⁋정의 12](/ko/math/algebraic_structures/group_actions#def12))

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Extension $\mathcal{E}:F \rightarrow E \rightarrow G$가 *central extension*이라는 것은 $F$의 $E$에서의 image가 $E$의 center에 포함되는 것이다. 

</div>

## 군의 반직접곱

한편, trivial extension이 아닌 extension이 존재하는 이유는, 위에서 보았듯 group $G$의 임의의 normal subgroup $N$에 대하여, 다음 식

$$G\cong (G/N)\oplus N$$

이 항상 성립하지는 <em_ko>않기</em_ko> 떄문이다. 그러나 그 역이 항상 성립하는 것은 아니다. 

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> 두 group $N,H$와 group homomorphism $\tau:H \rightarrow \Aut(N)$이 주어졌다 하자. 그럼 $N$과 $H$의 $\tau$에 대한 *semi-direct product<sub>반직접곱</sub>* $N\rtimes_\tau H$는 집합 $N\times H$ 위에 다음의 연산

$$(x_1,y_1)(x_2,y_2)=(x_1\tau(y_1)(x_1), y_1y_2)$$

이 주어진 group이다. 

</div>

그럼 $N\rtimes_\tau H$가 위의 연산에 대하여 group의 구조를 가진다는 것을 보일 수 있으며, 이 때 $N\rtimes_\tau H$의 항등원은 $(e_N, e_H)$이며 $(x,y)$의 역원은 $\tau(y^{-1})(x^{-1}), y^{-1})$이다. 뿐만 아니라 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> 두 함수 $i: N \rightarrow N\rtimes_\tau H$와 $p: N\rtimes_\tau H\rightarrow H$를 다음의 식

$$i(x)=(x, e_H),\qquad p(x,y)=y$$

으로 정의하자. 그럼 이 함수들은 group homomorphims이며, 이들로부터 얻어지는

$$\mathcal{E}_\tau: N \overset{i}{\rightarrow} N\rtimes_\tau H\overset{p}{\rightarrow} H$$

는 $H$의 $N$에 의한 extension이다. 뿐만 아니라, 함수 $s: H \rightarrow N\rtimes_\tau H$를 다음의 식

$$s(y)=(e_N, y)$$

으로 정의하면 $s$는 $p$의 section이며, 따라서 [명제 4](#prop4)에 의하여 $\mathcal{E}_\tau$는 trivial extension이다.

</div>

이에 대한 증명은 단순한 계산이다. 

이번에는 위에서 살펴본 $N,H$가 특정한 group $G$의 subgroup이었다 하자. 만일 $N$이 $G$의 *normal* subgroup이었다면 각각의 $h\in H$가 정의하는 inner automorphism $\rho_h$는 $N$의 automorphism이며 따라서 $\rho: H \rightarrow \Aut(N)$이 정의된다. ([\[대수적 구조\] §군의 작용, ⁋정의 10](/ko/math/algebraic_structures/group_actions#def10)) 그럼 위의 명제로부터 다음을 얻는다.

<div class="proposition" markdown="1">

<ins id="cor8">**따름정리 8**</ins> Group $G$와 $G$의 normal subgroup $N$, $G$의 subgroup $H$가 주어졌다 하자. 만일 $N\cap H=\\{e_G\\}$이고 $NH=G$가 성립한다면, 다음의 식

$$N\rtimes_\rho H \rightarrow G;\qquad (x,y)\mapsto xy$$

으로 정의된 group homomorphism은 isomorphism이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

역함수를 만들어주면 충분하다. 이를 위해서는 조건 $NH=G$를 이용하여 $G$의 임의의 원소 $g$에 대해 $g=xy$를 만족하는 적당한 $x\in N$, $y\in H$를 찾아야 하는데, 이는 일반적으로는 불가능하지만 $N$이 $G$의 *normal* subgroup이므로 가능하다. 나머지는 단순한 계산이다.

</details>

이 경우 $G$가 $N$과 $H$의 (internal) semi-direct product라고 말한다. External semi-direct product와 internal semi-direct product의 차이는 단순히 처음 시작을 어디서 했느냐일 뿐이며 중요한 것은 아니다. 

---

**참고문헌**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  

---


FTFGAG
Sylow
solvable S_5