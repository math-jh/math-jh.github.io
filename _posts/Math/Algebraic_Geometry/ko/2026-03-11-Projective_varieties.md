---
title: "사영다양체"
excerpt: "Projective varieties and homogeneous coordinates"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/projective_varieties
sidebar: 
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Projective_Zarieties.png
    overlay_filter: 0.5

date: 2026-03-11
last_modified_at: 2026-03-12
weight: 2

---

## 사영공간의 정의

이제 우리는 대수다양체의 다른 중요한 클래스인 사영다양체를 정의한다. 우선 다음부터 시작한다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Field $$\mathbb{K}$$ 위의 *projective $$n$$-space<sub>$$n$$차원 사영공간</sub>* $$\mathbb{P}^n_{\mathbb{K}}$$를 다음과 같이 정의한다. 집합으로서

$$\mathbb{P}^n = (\mathbb{K}^{n+1} \setminus \{0\}) / \sim$$

이며, 여기서 동치관계 $$\sim$$은

$$(x_0, \ldots, x_n) \sim (y_0, \ldots, y_n) \iff \text{$x_i = \lambda y_i$ for some $\lambda \in \mathbb{K}^\ast$, for all $i$}$$

으로 주어진다. 혼동의 여지가 없을 때는 $$\mathbb{P}^n$$으로 적는다.

</div>

Equivalence class $$[(x_0, \ldots, x_n)]$$은 보통 $$[x_0 : \cdots : x_n]$$으로 표기하며, 이를 *homogeneous coordinates<sub>동차좌표</sub>*라 부른다. $$x_0, \ldots, x_n$$을 *좌표*라 하고, 이들 중 적어도 하나는 $$0$$이 아니어야 한다. Homogeneous coordinates의 핵심은 좌표들이 *비율*만을 결정한다는 것이다. 즉, 모든 $$\lambda\in \mathbb{K}^\ast$$에 대하여 $$[x_0 : \cdots : x_n] = [\lambda x_0 : \cdots : \lambda x_n]$$이 성립한다. 

## 동차다항식과 사영공간

이제 우리는 affine case에서와 마찬가지로 $$\mathbb{P}^n$$에 위상구조를 주어야 한다. Projective space에서도 마찬가지로 우리는 다항식들의 zero set으로 닫힌집합을 정의할 것인데, 주의할 점은 $$\mathbb{P}^n$$은 quotient set으로 정의되었으므로 일반적으로는 다항식이 $$\mathbb{P}^N$$ 위에 정의된 함수를 정의하지 않는다는 것이다. 즉 임의의 $$F \in \mathbb{K}[x_0, \ldots, x_n]$$에 대하여, $$[x_0 : \cdots : x_n] = [\lambda x_0 : \cdots : \lambda x_n]$$이지만 일반적으로

$$F(x_0, \ldots, x_n)\neq F(\lambda x_0, \ldots, \lambda x_n)$$

이며, 이 계산이 $$\mathbb{P}^n$$의 모든 점에서 evaluation이 임의의 representative에 대해 잘 정의되도록 하는 유일한 다항식은 상수다항식 뿐이다. 그러나 만일 다항식이 정의하는 zero set에만 관심을 둔다면 이 문제가 해결된다. Homogeneous polynomial $$F$$ of degree $$d$$에 대해서는

$$F(\lambda x_0, \ldots, \lambda x_n) = \lambda^d F(x_0, \ldots, x_n)$$

이므로,

$$F(\lambda x_0, \ldots, \lambda x_n) = 0 \iff F(x_0, \ldots, x_n) = 0$$

이다. 따라서 homogeneous polynomial의 zero set은 projective space에서 잘 정의된다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 다항식 $$F \in \mathbb{K}[\x_0, \ldots, \x_n]$$이 *homogeneous of degree $$d$$<sub>$d$차 동차다항식</sub>*라는 것은 모든 $$\lambda \in \mathbb{K}$$에 대해

$$F(\lambda \x_0, \ldots, \lambda \x_n) = \lambda^d F(\x_0, \ldots, \x_n)$$

을 만족하는 것이다.

</div>

정의를 복잡하게 해 두긴 했지만, 이는 본질적으로 다항식을 단항식들의 합으로 나타냈을 때, 모든 단항식이 $$d$$차라는 것이다. 그럼 다음을 정의할 수 있다. 

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Homogeneous polynomials $$F_1, \ldots, F_k \in \mathbb{K}[\x_0, \ldots, \x_n]$$에 대하여, *projective algebraic set<sub>사영 대수적 집합</sub>* $$Z(F_1, \ldots, F_k)$$를

$$Z(F_1, \ldots, F_k) = \{[x_0 : \cdots : x_n] \in \mathbb{P}^n \mid F_1(x) = \cdots = F_k(x) = 0\}$$

으로 정의한다. Projective algebraic set들 가운데 그보다 더 작은 projective algebraic set들의 합집합으로 나타나지 않는 것들을 *projective variety<sub>사영다양체</sub>*라 부른다.

</div>

위에서 설명했듯, 각각의 $$F_i$$들이 homogeneous이므로 이것이 잘 정의되는 것을 확인할 수 있다. 

한편 우리는 affine variety를 다룰 때, $$\mathbb{K}[\x_1,\ldots, \x_n]$$의 임의의 부분집합 대신 ideal들만 살펴보면 되었던 것을 기억한다. Projective case에서도 이 철학은 유사하지만, 추가로 homogeneity 가정을 더하여 homogeneous ideal의 개념을 정의할 수 있다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Ideal $$\mathfrak{a} \subseteq \mathbb{K}[\x_0, \ldots, \x_n]$$이 *homogeneous*라는 것은 $$\mathfrak{a}$$가 homogeneous polynomial들로 생성되는 것이다.

</div>

Homogeneous ideal $$\mathfrak{a}$$에 대하여, 그 zero set $$Z(\mathfrak{a})$$를 $$\mathfrak{a}$$의 모든 homogeneous polynomial들이 vanish하는 점들로 정의하면, affine case와 마찬가지로 우리는 Zariski topology를 정의할 수 있다. 이를 위해서는 다음 명제가 필요하다. 

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> 다음이 성립한다.

1. $$Z(0) = \mathbb{P}^n$$, $$Z(1) = \emptyset$$,
2. $$\bigcap_iZ(\mathfrak{a}_i) = Z\left(\sum_i \mathfrak{a}_i\right)$$,
3. $$Z(\mathfrak{a}) \cup Z(\mathfrak{b}) = Z(\mathfrak{a} \cap \mathfrak{b}) = Z(\mathfrak{a}\mathfrak{b})$$.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Affine case와의 유일한 차이점은 여기서 다루는 다항식들이 모두 homogeneous라는 점이지만, 증명 논리 자체는 동일하므로 증명을 생략하기로 한다. 

</details>

Affine case에서와 마찬가지로, 이는 projective space $$\mathbb{P}^n$$ 위에 projective algebraic set들을 닫힌집합으로 갖는 위상구조가 존재한다는 것을 보여주며, 우리는 각각의 projective variety에 이를 이용하여 subspace topology를 줄 수 있다. 마찬가지로 이러한 topology를 *Zariski topology*라 부른다. ([[아핀다양체] §아핀다양체의 정의](/ko/math/algebraic_geometry/affine_varieties)에서 affine case의 Zariski topology를 먼저 살펴보았다.) 

## Projective Nullstellensatz

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> 부분집합 $$X \subseteq \mathbb{P}^n$$의 *homogeneous ideal* $$I(X)$$를

$$I(X) = \{F \in \mathbb{K}[\x_0, \ldots, \x_n] \mid F \text{ is homogeneous and } F(x) = 0 \text{ for all } x \in X\}$$

으로 정의한다.

</div>

<div class="proposition" markdown="1">

<ins id="thm7">**정리 7**</ins> (Projective Nullstellensatz) Field $$\mathbb{K}$$가 대수적으로 닫힌 체이고 $$\mathfrak{a} \subseteq \mathbb{K}[\x_0, \ldots, \x_n]$$이 homogeneous ideal이라 하자. 그럼

1. $$Z(\mathfrak{a}) = \emptyset \iff \mathfrak{a} \supseteq (\x_0, \ldots, \x_n)$$,
2. $$I(Z(\mathfrak{a})) = \sqrt{\mathfrak{a}}$$ (if $$Z(\mathfrak{a}) \ne \emptyset$$).

</div>

Affine case와의 차이점은 $$Z(\mathfrak{a}) = \emptyset$$이 $$\mathfrak{a} = (1)$$을 의미하지 않고, $$\mathfrak{a}$$가 *irrelevant ideal* $$(\x_0, \ldots, \x_n)$$을 포함하는 것을 의미한다는 점이다. 이는 $$(\x_0, \ldots, \x_n)$$이 $$\mathbb{K}^{n+1}$$의 원점에 해당하는데, projective space의 정의에서 원점은 제외되었기 때문이다.

## Standard Affine Cover

Projective space $$\mathbb{P}^n$$은 $$n+1$$개의 affine space들로 덮을 수 있다. 이는 projective space를 이해하는 가장 중요한 방법 중 하나이다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> $$i = 0, 1, \ldots, n$$에 대하여, *$$i$$번째 standard open set* $$U_i$$를

$$U_i = \{[x_0 : \cdots : x_n] \in \mathbb{P}^n \mid x_i \ne 0\}$$

으로 정의한다.

</div>

각각의 $$U_i$$에 $$\mathbb{P}^n$$으로부터 오는 subspace topology를 주자. 그럼 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> 각각의 $$U_i$$는 (subspace topology 하에서) affine space $$\mathbb{A}^n$$과 homeomorphic하다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

표기의 편의를 위해 $$i=0$$인 경우를 증명한다. $$U_0$$의 경우, map $$\varphi_0: U_0 \to \mathbb{A}^n$$을

$$\varphi_0([x_0 : x_1 : \cdots : x_n]) = \left(\frac{x_1}{x_0}, \ldots, \frac{x_n}{x_0}\right)$$

으로 정의하자. 역함수 $$\psi_0: \mathbb{A}^n \to U_0$$는

$$\psi_0(a_1, \ldots, a_n) = [1 : a_1 : \cdots : a_n]$$

이다. 이들이 서로 inverse인 것은 정의로부터 자명하다. 이제 $$\varphi_0$$와 $$\psi_0$$가 모두 연속임을 보여야 한다.

우선 $$\varphi_0$$의 연속성을 보이기 위해 $$\mathbb{A}^n$$의 닫힌집합 $$Z(f)$$를 생각하자. 그럼

$$\varphi_0^{-1}(Z(f)) = \left\{[x_0 : \cdots : x_n] \in U_0 \mid f\left(\frac{x_1}{x_0}, \ldots, \frac{x_n}{x_0}\right) = 0\right\}$$

이다. 이제 만일 $$f$$가 degree $$d$$인 다항식이라면, 

$$F(x_0,\ldots, \x_n)=\x_0^d f(\x_1/\x_0, \ldots, \x_n/\x_0)$$

는 homogeneous polynomial이며 $$\varphi_0^{-1}(Z(f)) = Z(F) \cap U_0$$이다. 이는 $$U_0$$의 subspace topology에서 닫힌집합이다.

이제 그 역함수 $$\psi_0$$의 연속성을 보이자. $$U_0$$의 닫힌집합 $$Z(F) \cap U_0$$를 생각하자. 여기서 $$F$$는 homogeneous polynomial of degree $$d$$이다. 그럼

$$\psi_0^{-1}(Z(F) \cap U_0) = \{(x_1, \ldots, x_n) \in \mathbb{A}^n \mid F(1, x_1, \ldots, x_n) = 0\}$$

이다. $$F(1, \x_1, \ldots, \x_n)$$은 $$\mathbb{K}[\x_1, \ldots, \x_n]$$의 다항식이므로 $$\psi_0^{-1}(Z(F) \cap U_0)$$는 $$\mathbb{A}^n$$에서 닫힌집합이다.

따라서 $$\varphi_0$$와 $$\psi_0$$가 서로 inverse이고 모두 연속이므로 $$\varphi_0$$는 homeomorphism이다.

</details>

즉, 직관적으로 우리는 $$U_i$$를 좌표 $$x_i$$가 무한대가 아닌 점들로 생각할 수 있다. 또, $$\mathbb{P}^n = U_0 \cup \cdots \cup U_n$$이고, 위의 명제에 의해 각 $$U_i \cong \mathbb{A}^n$$이다. 위의 명제의 증명 과정에서 핵심적인 것은 다음의 명제였으므로, 이를 따로 분리해두자.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> Projective variety $$X \subseteq \mathbb{P}^n$$과 standard open set $$U_i$$에 대하여, $$X \cap U_i$$는 $$U_i \cong \mathbb{A}^n$$ 위의 affine variety이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$U_0$$의 경우, $$X = Z(F_1, \ldots, F_k)$$이고 각 $$F_j$$가 homogeneous of degree $$d_j$$라 하자. 그럼 $$X \cap U_0$$는 $$\mathbb{A}^n$$에서

$$F_j\left(1, \frac{\x_1}{\x_0}, \ldots, \frac{\x_n}{\x_0}\right) = 0, \quad j = 1, \ldots, k$$

을 만족하는 점들이다. 양변에 $$\x_0^{d_j}$$를 곱하면

$$\x_0^{d_j} F_j\left(1, \frac{\x_1}{\x_0}, \ldots, \frac{\x_n}{\x_0}\right) = F_j(\x_0, \x_1, \ldots, \x_n) = 0$$

이다. 이제 $$f_j(\x_1, \ldots, \x_n) = F_j(1, \x_1, \ldots, \x_n)$$라 두면, $$X \cap U_0 = Z(f_1, \ldots, f_k) \subseteq \mathbb{A}^n$$이다.

</details>

<div class="example" markdown="1">

<ins id="ex11">**예시 11**</ins> 위의 명제를 기하적으로 해석하기 위해 $$\mathbb{K}=\mathbb{R}$$이라 하고, $$\mathbb{P}^2$$에서 conic $$X = Z(\x_0^2 + \x_1^2 - \x_2^2)$$를 생각하자. 

이 conic은 $$\mathbb{A}^3$$ 안의 원뿔 $$\x_0^2 + \x_1^2 = \x_2^2$$을 homogeneous coordinates로 표현한 것이다. 그럼 standard open set들에서 $$X$$가 어떻게 보이는지는 [명제 10](#prop10)에서 알 수 있다. 즉 $$U_i$$에서 $$X$$가 어떻게 생겼는지를 보기 위해서는 그냥 $$\x_i$$ 자리에 $$1$$을 넣고, 남은 $$n$$개의 변수가 $$\mathbb{A}^n$$의 좌표인 것으로 생각하면 된다. 그럼 특히 다음의 결과를 얻는다. 

1. $$U_0, U_1$$에서 $$X$$는 쌍곡선 $$1+y^2-z^2=0$$, $$x^2+1-z^2=0$$이다.
2. $$U_2$$에서 $$X$$는 원 $$x^2+y^2=1$$이다. 

이는 $$\mathbb{A}^3$$에서 식 $$\x_0^2 + \x_1^2 = \x_2^2$$이 원뿔이고, 이를 평면 $$\x_0=1, \x_1=1, \x_2=1$$로 자른 흔적이 쌍곡선과 원이 되기 때문에 생기는 일이다. 

한편 이를 $$\mathbb{P}^2$$에서 바로 해석할 수도 있다. 이를 위해 우리는 $$\mathbb{P}^2$$를 다음과 같이 얻어내자. $$\x_2\neq 0$$인 점들에 대해서는 $$\x_2>0$$을 만족하는 상반구로 radial projection하고, $$\x_2=0$$인 점들은 antipodal point들을 identify하여 얻는다. 이를 통해 $$\mathbb{P}^2$$는 "무한대 직선" $$\mathbb{P}^1$$에, 상반구의 표면에 해당하는 평면 $$\mathbb{A}^2$$가 합쳐진 모습으로 생각할 수 있다. 그럼 주어진 원뿔은 우선 첫 번째 radial projection을 통해 상반구에 포함되는 원이 되며, 이로부터 $$X$$는 $$\mathbb{P}^2$$에서 원으로 나타난다는 것을 안다. 

물론 처음에 $$\x_0\neq 0$$을 만족하는 점들을 $$\x_0>0$$인 상반구로 radial projection, $$\x_0=0$$인 점들을 $$\mathbb{P}^1$$으로 갖는 식으로 $$\mathbb{P}^2$$를 만들 수도 있었을 것이다. 그럼 이 과정에서는 상반구에 두 개의 반원이 그려질 것이나, 이 두 반원의 경계점이 $$\x_0=0$$인 점들을 identify하는 과정에서 서로 같은 것으로 취급되어 이 그림에서도 $$X$$는 원이 될 것이다. 

이제 이 관점에서, $$U_i$$에서의 $$X$$를 보는 것은 $$\mathbb{P}^2$$에서 무한대 직선 $$\x_i=0$$을 빼는 것에 해당한다. 만일 $$U_2$$에서 $$X$$를 본다면, 위에서 살펴보았듯 $$X$$는 무한대 직선 $$\x_2=0$$과 만나지 않으므로 이 직선을 빼도 온전한 원으로 남는다. 그러나 가령 무한대 직선 $$\x_1=0$$을 뺀다면, $$X$$는 $$\x_1$$과 두 점에서 만나고 있고, 따라서 원 $$X$$에서 이 두 점을 뺀 후 펼치게 되면 쌍곡선이 나오게 되는 것으로 이해할 수 있다. 

![sketch](/assets/images/Math/Algebraic_Geometry/Projective_varieties-1.png){:style="width:50em" class="invert" .align-center}

</div>

## Affine Cone

앞선 예시는 projective space 위의 곡선을 각각의 affine open chart 안에서 보는 방법을 알려주지만, 여전히 다소 덜 직관적이라 생각할 수 있다. Projective variety를 affine space 안의 기하학적 대상으로 이해하는 또 다른 방법은 *affine cone*을 생각하는 것이다.

<div class="definition" markdown="1">

<ins id="def12">**정의 12**</ins> Projective variety $$X \subseteq \mathbb{P}^n$$의 *affine cone<sub>아핀 뿔</sub>* $$C(X) \subseteq \mathbb{A}^{n+1}$$을 다음과 같이 정의한다:

$$C(X) = \{(x_0, \ldots, x_n) \in \mathbb{A}^{n+1} \setminus \{0\} \mid [x_0 : \cdots : x_n] \in X\} \cup \{0\}$$

즉, $$C(X)$$는 $$X$$의 모든 점을 homogeneous coordinates로 표현했을 때 나타나는 $$\mathbb{A}^{n+1}$$의 점들과 원점을 합한 것이다.

</div>

<div class="example" markdown="1">

<ins id="ex13">**예시 13**</ins> [예시 11](#ex11)의 conic $$X = Z(\x_0^2 + \x_1^2 - \x_2^2) \subseteq \mathbb{P}^2$$의 affine cone $$C(X)$$는 $$\mathbb{A}^3$$에서의 원뿔 $$\x_0^2 + \x_1^2 = \x_2^2$$이다.

</div>

그럼 다음이 성립하며, 그 증명들도 어렵지 않다.

<div class="proposition" markdown="1">

<ins id="prop14">**명제 14**</ins> Projective variety $$X \subseteq \mathbb{P}^n$$의 affine cone $$C(X)$$은 다음 성질들을 만족한다:

1. (Homogeneity) $$C(X)$$는 원점을 지나는 직선들로 구성된다. 즉, $$(x_0, \ldots, x_n) \in C(X)$$이고 $$\lambda \in \mathbb{K}$$이면 $$(\lambda x_0, \ldots, \lambda x_n) \in C(X)$$이다.

2. (Algebraic structure) $$X = Z(F_1, \ldots, F_k)$$이면 $$C(X) = V(F_1, \ldots, F_k) \subseteq \mathbb{A}^{n+1}$$이다. 여기서 $$F_i$$들을 $$\mathbb{A}^{n+1}$$의 다항식으로 본다.

3. (Correspondence) $$X \leftrightarrow C(X)$$ 대응은 projective variety와 원점을 지나는 직선으로 이루어진 affine algebraic set 사이의 일대일 대응을 준다.

</div>

이 명제를 통해 우리는 affine cone $$C(X)$$의 성질을 연구하여 $$X$$의 성질을 간접적으로 파악할 수 있다. 

## 사영다양체 사이의 사상

마지막으로 우리는 projective variety들의 morphism을 정의한다. 앞서 우리는 projective algebraic set을 정의할 때 다항식들의 zero set이 projective space의 집합을 잘 정의하지 않는 것을 확인하였는데, 비슷한 일이 morphism을 정의할 때도 일어나며 그 해결책은 이번에도 homogeneous polynomial이다. 

<div class="definition" markdown="1">

<ins id="def15">**정의 15**</ins> 함수 $$\varphi: X \to Y$$가 projective variety $$X \subseteq \mathbb{P}^n$$과 $$Y \subseteq \mathbb{P}^m$$ 사이의 *morphism<sub>사상</sub>*이라는 것은, 각각의 점 $$x$$마다 적당한 homogeneous polynomials $$F_0, \ldots, F_m$$ of the same degree가 존재하여

$$\varphi(x) = [F_0(x) : \cdots : F_m(x)]$$

이고, 모든 $$x \in X$$에 대해 $$F_i(x)$$들이 동시에 $$0$$이 아닌 것이다.

</div>

만일 $$F_0, \ldots, F_m$$이 모두 같은 차수 $$d$$의 homogeneous polynomial이라면, $$F_i(\lambda x) = \lambda^d F_i(x)$$이므로

$$[F_0(\lambda x) : \cdots : F_m(\lambda x)] = [\lambda^d F_0(x) : \cdots : \lambda^d F_m(x)] = [F_0(x) : \cdots : F_m(x)]$$

가 되어 well-definedness가 보장된다는 것을 확인할 수 있다. 다음 예시들은 대표적인 morphism들이다. 

<div class="example" markdown="1">

<ins id="ex16">**예시 16**</ins> 우선 $$\mathbb{P}^1$$에서 $$\mathbb{P}^2$$로의 *Veronese embedding* (of degree 2)을

$$[x:y]\mapsto [x^2: xy:y^2]$$

으로 정의하면, 이는 projective space들 사이의 morphism이 된다. 또 다른 예시로, $$\mathbb{P}^1\times \mathbb{P}^1$$에서 $$\mathbb{P}^3$$의 *Segre embedding*은 다음 식

$$([x:y], [u:v])\mapsto [xu: xv: yu: yv]$$

으로 주어지는 morphism이다. 

</div>

<div class="example" markdown="1">

<ins id="ex17">**예시 17**</ins> **Twisted cubic in $$\mathbb{P}^3$$**

$$C = \{[1 : t : t^2 : t^3] \mid t \in \mathbb{K}\} \cup \{[0 : 0 : 0 : 1]\}$$

는 세 개의 quadratic polynomials

$$\x_0 \x_2 - \x_1^2, \quad \x_0 \x_3 - \x_1 \x_2, \quad \x_1 \x_3 - \x_2^2$$

의 공통 영점이며, $$\mathbb{P}^1$$과 isomorphic하다. 실은, 위의 [예시 16](#ex16)에서 살펴본 Veronese embedding의 개념을 $$d=3$$으로 확장하면, 

$$[x:y]\mapsto [x^3: x^2y: xy^2: y^3]$$

이 $$\mathbb{P}^1$$에서 $$C$$로의 isomorphism이 된다. 

</div>

---

**참고문헌**

**[Har]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Zarieties in Projective Space*, Springer, 2013.  
**[Ful]** W. Fulton, *Algebraic Curves*, 2008.