---
title: "군의 확장"
description: "군의 확장은 주어진 두 군 사이의 확장 구조를 분류하고, trivial extension의 동치 조건 및 확장들 사이의 morphism을 다룬다."
excerpt: "Short exact sequence로서의 group extension과 semidirect product"

categories: [Math / Group Theory]
permalink: /ko/math/group_theory/extensions
sidebar: 
    nav: "group_theory-ko"

date: 2025-03-29
weight: 2
published: false
revising: true
drift_needed: true

---

이번 글에서 우리는 group의 extension에 대해 다룬다. 

## 군의 확장

::: 정의 1
두 group $G, F$에 대하여, $G$의 $F$에 의한 *extension<sub>확장</sub>* $\mathcal{E}$는 조건 $\ker p=\im i$를 만족하는 다음의 pair

$$\mathcal{E}: F\overset{i}{\hookrightarrow}E\overset{p}{\twoheadrightarrow}G$$

을 의미한다. 
:::

이에 대한 직관은 다음의 pair

$$\mathcal{E}_0: F \rightarrow F\times G \rightarrow G$$

이며, 우리는 이를 *trivial extension*이라 부른다. 그러나 일반적으로 위의 상황에서 first isomorphism theorem에 의하여 다음의 식

$$G\cong E/\ker p=E/\im i$$

이 성립하지만, 그렇다고 하여

$$E\cong (E/i(F))\times i(F)$$

가 성립하는 것은 아니므로 주의할 필요가 있다. 어쨌든 이 계산으로부터 $E$가 $G$의 $F$에 의한 extension이기 위해서는 $E$의 적당한 normal subgroup $F'$가 존재하여, $F'$가 $F$와 isomorphic하고 $E/F'$는 $G$와 isomorphic한 것이 동치임을 안다. 

그럼 고정된 $G$와 $F$에 대하여, $G$의 $F$에 의한 extension들을 모두 모아둔 것은 category를 이룬다. 여기에서의 morphism은 다음과 같이 주어진다. 

::: 정의 2
두 extension $\mathcal{E}_1: F \rightarrow E_1 \rightarrow G$과 $\mathcal{E}_2:F \rightarrow E_2 \rightarrow G$에 대하여, $\mathcal{E}_1$에서 $\mathcal{E}_2$로의 *morphism*은 다음의 diagram

{% diagram Math/Group_Theory/Extensions-1.svg width="10.17em" alt="morphism_of_extensions" %}

을 commute하도록 하는 $u:E_1 \rightarrow E_2$를 의미한다.  
:::

그럼 만일 $u:E_1 \rightarrow E_2$가 group homomorphism으로서 isomorphism이라면, $u$의 inverse $u^{-1}: E_2 \rightarrow E_1$ 또한 [정의 2](#def2)의 조건을 만족하고 따라서 $u$는 extension들 사이의 morphism으로서 isomorphism이라는 것을 확인할 수 있다. 

앞선 정의를 확장하여, 다음을 정의한다. 

::: 정의 3
$G$의 $F$에 의한 extension $\mathcal{E}:F \rightarrow E \rightarrow G$이 extension

$$\mathcal{E}_0:F \rightarrow F\times G \rightarrow G$$

과 isomorphic하다면, 이를 *trivial extension<sub>자명한 확장</sub>*이라고 부른다. 
:::

그럼 다음이 성립한다. 

::: 명제 4
Extension $\mathcal{E}:F \rightarrow E \rightarrow G$에 대하여, 다음이 모두 동치이다.

1. $\mathcal{E}$가 trivial extension이다.
2. Retraction $r: E \rightarrow F$가 존재한다. 
3. Section $s: G \rightarrow E$가 존재하여 $s(G)$가 $i(F)$의 centralizer에 포함되도록 할 수 있다. 
:::

물론 여기에서 retraction과 section은 단순한 함수가 아니라 group homomorphism을 의미한다. ([\[집합론\] §Retraction과 section, ⁋정의 2](/ko/math/set_theory/retraction_and_section#def2))

::: 증명 (명제 4)
우선 첫째 조건을 가정하고 다음의 diagram

{% diagram Math/Group_Theory/Extensions-2.svg width="11.92em" alt="retraction_and_section" %}

를 생각하자. 그럼 이로부터 retraction $r:E \rightarrow F$를 $\pr_1\circ u$로, $s:G \rightarrow E$를 $u^{-1}\circ\iota_2$로 정의하면 된다. 여기에서 $\pr_1:F\times G \rightarrow F$와 $\iota_2:G \rightarrow F\times G$는 각각 첫째 성분으로의 projection과 둘째 성분에서의 inclusion이며, 위의 diagram이 commute하므로 $r\circ i=\pr_1\circ\iota_1=\id_F$와 $p\circ s=\pr_2\circ\iota_2=\id_G$가 성립한다. 또 $F\times\{e_G\}$의 원소와 $\{e_F\}\times G$의 원소는 서로 commute하고 $u$가 isomorphism이므로, $i(F)=u^{-1}(F\times\{e_G\})$의 원소와 $s(G)=u^{-1}(\{e_F\}\times G)$의 원소 또한 서로 commute하고 따라서 $s(G)$는 $i(F)$의 centralizer에 포함된다.

거꾸로 둘째 조건이 성립한다 가정하자. 그럼 $(r,p): E \rightarrow F\times G$가 주어진 extension과 $F \rightarrow F\times G \rightarrow G$ 사이의 isomorphism이 된다. 실제로 $(r,p)(x)$가 항등원이라면 $x\in\ker p=\im i$이므로 $x=i(f)$인 $f\in F$가 존재하고, $r\circ i=\id_F$로부터 $f=r(x)=e_F$를 얻어 $x$가 항등원이다. 또 임의의 $(f,g)\in F\times G$에 대하여 $p$가 전사이므로 $p(y)=g$인 $y\in E$를 택할 수 있고, $x=i(fr(y)^{-1})y$로 두면 $r(x)=fr(y)^{-1}r(y)=f$이고 $p(x)=g$이므로 $(r,p)$는 전사이다. 이것이 [정의 2](#def2)의 diagram을 commute하게 하는 것은 $(r,p)\circ i=\iota_1$과 $\pr_2\circ(r,p)=p$로부터 얻어진다.

마지막으로 셋째 조건을 가정하자. $F$와 $G$ 둘만의 weak direct product는 $F\times G$와 같고 $i(F)$의 원소와 $s(G)$의 원소가 서로 commute하므로, [\[대수적 구조\] §제한합, ⁋정리 2](/ko/math/algebraic_structures/restricted_sums#thm2)에 의하여 $\varphi\circ\iota_1=i$와 $\varphi\circ\iota_2=s$를 만족하는 homomorphism $\varphi:F\times G \rightarrow E$가 유일하게 유도되며, 이는 $\varphi(f,g)=i(f)s(g)$로 주어진다. 만일 $i(f)s(g)$가 항등원이라면 여기에 $p$를 취하여 $g=e_G$를 얻고 따라서 $i(f)$가 항등원, 즉 $f=e_F$이므로 $\varphi$는 단사이며, 임의의 $x\in E$에 대해 $xs(p(x))^{-1}$이 $\ker p=\im i$에 속하여 $x$가 $i(f)s(p(x))$의 꼴로 적히므로 $\varphi$는 전사이다. 여기에 $\varphi\circ\iota_1=i$와 $p\circ\varphi=\pr_2$를 함께 생각하면 $\varphi$는 extension들 사이의 isomorphism이고 따라서 $\mathcal{E}$는 trivial extension이다. 
:::

만일 $i(F)$가 $E$의 center $Z(E)$에 포함되었다면, 세 번째 조건에서 $s(G)$와 $i(F)$의 관계는 무시하여도 좋을 것이다. ([\[대수적 구조\] §군의 작용, ⁋정의 12](/ko/math/algebraic_structures/group_actions#def12))

::: 정의 5
Extension $\mathcal{E}:F \rightarrow E \rightarrow G$가 *central extension<sub>중심확장</sub>*이라는 것은 $F$의 $E$에서의 image가 $E$의 center에 포함되는 것이다. 
:::

## 군의 반직접곱

한편, trivial extension이 아닌 extension이 존재하는 이유는, 위에서 보았듯 group $G$의 임의의 normal subgroup $N$에 대하여, 다음 식

$$G\cong (G/N)\times N$$

이 항상 성립하지는 <em-ko>않기</em-ko> 때문이다. 그러나 거꾸로 위의 식이 성립한다 하여도, 그것은 abstract group으로서의 isomorphism일 뿐 extension $N \rightarrow G \rightarrow G/N$이 trivial extension이라는 뜻은 아니다. 

::: 정의 6
두 group $N,H$와 group homomorphism $\tau:H \rightarrow \Aut(N)$이 주어졌다 하자. 그럼 $N$과 $H$의 $\tau$에 대한 *semi-direct product<sub>반직접곱</sub>* $N\rtimes_\tau H$는 집합 $N\times H$ 위에 다음의 연산

$$(x_1,y_1)(x_2,y_2)=(x_1\tau(y_1)(x_2), y_1y_2)$$

이 주어진 group이다. 
:::

그럼 $N\rtimes_\tau H$가 위의 연산에 대하여 group의 구조를 가진다는 것을 보일 수 있으며, 이 때 $N\rtimes_\tau H$의 항등원은 $(e_N, e_H)$이며 $(x,y)$의 역원은 $(\tau(y^{-1})(x^{-1}), y^{-1})$이다. 뿐만 아니라 다음이 성립한다.

::: 명제 7
두 함수 $i: N \rightarrow N\rtimes_\tau H$와 $p: N\rtimes_\tau H\rightarrow H$를 다음의 식

$$i(x)=(x, e_H),\qquad p(x,y)=y$$

으로 정의하자. 그럼 이 함수들은 group homomorphism이며, 이들로부터 얻어지는

$$\mathcal{E}_\tau: N \overset{i}{\rightarrow} N\rtimes_\tau H\overset{p}{\rightarrow} H$$

는 $H$의 $N$에 의한 extension이다. 뿐만 아니라, 함수 $s: H \rightarrow N\rtimes_\tau H$를 다음의 식

$$s(y)=(e_N, y)$$

으로 정의하면 $s$는 $p$의 section이다. 다만 $s(H)$가 $i(N)$의 centralizer에 포함되는 것은 $\tau$가 trivial homomorphism인 경우에 한하며, 이 경우 [명제 4](#prop4)에 의하여 $\mathcal{E}_\tau$는 trivial extension이 된다.
:::

$i$가 group homomorphism인 것은 $i(x_1)i(x_2)=(x_1\tau(e_H)(x_2), e_H)=(x_1x_2,e_H)$로부터, $p$가 group homomorphism인 것은 두 원소의 곱의 둘째 성분이 $y_1y_2$인 것으로부터 얻어진다. 또 $p(x,y)$가 항등원인 것은 $y=e_H$인 것과 동치이므로 $\ker p=i(N)=\im i$이고, $i$는 단사이고 $p$는 전사이므로 $\mathcal{E}_\tau$는 $H$의 $N$에 의한 extension이다. 마찬가지로 $s$ 또한 group homomorphism이며 $p\circ s=\id_H$이므로 $s$는 $p$의 section이다. 한편 [정의 6](#def6)의 연산으로부터 다음의 두 식

$$(e_N,y)(x,e_H)=(\tau(y)(x), y),\qquad (x,e_H)(e_N,y)=(x,y)$$

이 성립하므로 $s(y)$가 $i(x)$와 commute하는 것은 $\tau(y)(x)=x$인 것과 동치이고, 따라서 $s(H)$가 $i(N)$의 centralizer에 포함되는 것은 임의의 $y\in H$에 대해 $\tau(y)=\id_N$인 경우, 즉 $\tau$가 trivial homomorphism인 경우뿐이다. 

이번에는 위에서 살펴본 $N,H$가 특정한 group $G$의 subgroup이었다 하자. 만일 $N$이 $G$의 *normal* subgroup이었다면 각각의 $h\in H$가 정의하는 inner automorphism $\rho_h$는 $N$의 automorphism이며 따라서 $\rho: H \rightarrow \Aut(N)$이 정의된다. ([\[대수적 구조\] §군의 작용, ⁋정의 10](/ko/math/algebraic_structures/group_actions#def10)) 그럼 위의 명제로부터 다음을 얻는다.

::: 따름정리 8
Group $G$와 $G$의 normal subgroup $N$, $G$의 subgroup $H$가 주어졌다 하자. 만일 $N\cap H=\{e_G\}$이고 $NH=G$가 성립한다면, 다음의 식

$$N\rtimes_\rho H \rightarrow G;\qquad (x,y)\mapsto xy$$

으로 정의된 group homomorphism은 isomorphism이다. 
:::
::: 증명
우선 주어진 함수가 group homomorphism인 것은 $N$이 $G$의 *normal* subgroup이라는 가정에서 나온다. 실제로 $\rho_{y_1}(x_2)=y_1x_2y_1^{-1}$이므로 다음의 식

$$\bigl(x_1\rho_{y_1}(x_2)\bigr)(y_1y_2)=x_1y_1x_2y_1^{-1}y_1y_2=(x_1y_1)(x_2y_2)$$

이 성립하고, 이는 $(x_1,y_1)(x_2,y_2)$의 image가 $(x_1,y_1)$의 image와 $(x_2,y_2)$의 image의 곱과 같다는 것이다.

이제 역함수를 만들어주면 충분하다. 여기에서 $NH$는 부분집합의 곱 $\{xy\mid x\in N, y\in H\}$를 의미하므로, 가정 $NH=G$는 $G$의 임의의 원소 $g$가 $x\in N$과 $y\in H$에 대해 $g=xy$의 꼴로 적힌다는 것을 곧바로 준다. 또 이렇게 얻어지는 $x$와 $y$는 유일하게 결정되는데, $x_1y_1=x_2y_2$라면 $x_2^{-1}x_1=y_2y_1^{-1}$이 $N\cap H=\{e_G\}$에 속하기 때문이다. 따라서 $g\mapsto (x,y)$가 잘 정의되고, 이것이 위 homomorphism의 역함수이다.
:::

이 경우 $G$가 $N$과 $H$의 (internal) semi-direct product라고 말한다. External semi-direct product와 internal semi-direct product의 차이는 단순히 처음 시작을 어디서 했느냐일 뿐이며 중요한 것은 아니다. 

---

**참고문헌**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  

---