---
title: "Kazhdan–Lusztig polynomial"
description: "Kazhdan-Lusztig polynomial은 Hecke algebra 위에서 정의되며, Schubert variety의 교차 코호몰로지 차원을 조합적으로 인코딩하는 다항식이다. 이 글에서는 이 다항식의 정의, 기본 성질, 그리고 Schubert variety와의 관계를 정리한다."
excerpt: "Hecke algebra의 KL basis를 통해 정의되는 polynomial로, Schubert variety의 특이점과 깊이 관련된다."

categories: [Math / Lie Theory]
permalink: /ko/math/lie_theory/kazhdan_lusztig
sidebar:
    nav: "Lie_theory-ko"

date: 2025-01-07
weight: 8
published: false
---

Schubert variety $$X_w \subseteq G/B$$는 일반적으로 특이점을 갖는 사영다양체이며, 그 특이점의 양상은 단순한 차원 정보만으로는 포착되지 않는다. 1979년 Kazhdan과 Lusztig는 [§Bruhat decomposition](/ko/math/lie_theory/bruhat_decomposition)의 조합적 구조 위에 정의되는 일군의 정수계수 다항식을 도입하여, $$X_w$$의 local intersection cohomology의 점별 차원이 이 다항식들로 완전히 인코딩됨을 보였다. 이 *Kazhdan-Lusztig polynomial*은 한편으로는 Hecke algebra의 한 특별한 basis로부터 순수히 조합적으로 정의되며, 다른 한편으로는 Schubert variety의 특이점과 infinite-dimensional Lie algebra의 표현론에 대한 직접적인 cohomological 정보를 담는다. 본 글에서는 이 다항식의 정의와 기본 성질을 정리하고, Schubert variety와의 관계를 statement 수준에서 정리한다.

## Coxeter group과 Bruhat order 복습

이 글에서 우리는 $$(W, S)$$를 finite Coxeter system이라 한다. 즉, $$W$$는 simple reflection들의 집합 $$S = \{s_1, \ldots, s_r\}$$에 의해 생성되며 ([§Bruhat decomposition, ⁋명제 2](/ko/math/lie_theory/bruhat_decomposition#prop2))

$$s_i^2 = e,\qquad (s_i s_j)^{m_{ij}} = e\quad (i\neq j,\; m_{ij} \in \{2, 3, 4, 6, \ldots\})$$

의 관계를 만족한다. 각 $$w \in W$$에 대해 *length function* $$\ell(w)$$는 $$w$$를 $$S$$의 원소들의 곱으로 나타낼 때의 최소 길이로 정의되며, 이로부터 *Bruhat order* $$\le$$가 자연스럽게 결정된다. 구체적으로 $$v \le w$$라는 것은 $$w$$의 어떤 reduced expression $$w = s_{i_1} \cdots s_{i_\ell}$$의 부분수열을 골라 $$v$$의 reduced expression을 얻을 수 있음을 의미하며, 이는 [§Bruhat decomposition](/ko/math/lie_theory/bruhat_decomposition)에서 살펴 본 Schubert variety 사이의 포함 관계와 정확히 대응된다.

본 글의 모든 논의는 이 추상적 Coxeter 데이터만 사용하여 진행되지만, 독자는 항상 $$W = N_G(T)/T$$가 reductive group $$G$$의 Weyl group이고 $$\le$$가 flag variety $$G/B$$ 위의 Schubert variety 포함 관계를 인코딩하는 상황을 염두에 두어도 좋다.

## Hecke algebra

Kazhdan–Lusztig polynomial은 $$W$$ 자체가 아니라 그 *Hecke deformation*인 Hecke algebra 위에서 정의된다. 우리는 매개변수 $$q$$를 도입하여, group algebra $$\mathbb{Z}[W]$$의 $$q$$-deformation을 다음과 같이 정의한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Coxeter system $$(W, S)$$에 대하여, *Iwahori–Hecke algebra* $$H = H_q(W)$$는 $$\mathcal{A} = \mathbb{Z}[q^{1/2}, q^{-1/2}]$$ 위의 associative algebra로서, $$s \in S$$에 대응하는 generator $$T_s$$들에 의해 생성되며 다음 관계를 만족한다.

1. *Quadratic relation*: $$T_s^2 = (q - 1) T_s + q$$ for all $$s \in S$$.
2. *Braid relation*: $$\underbrace{T_s T_t T_s \cdots}_{m_{st} \text{ terms}} = \underbrace{T_t T_s T_t \cdots}_{m_{st} \text{ terms}}$$ for $$s \neq t \in S$$.

</div>

Braid relation 덕분에 임의의 reduced expression $$w = s_{i_1} \cdots s_{i_\ell}$$에 대해 $$T_w := T_{s_{i_1}} \cdots T_{s_{i_\ell}}$$는 reduced expression의 선택에 의존하지 않으므로 well-defined이다. 우리는 이렇게 정의된 $$\{T_w\}_{w \in W}$$를 *standard basis*라 부르며, 실제로 $$H$$는 $$\mathcal{A}$$-module로서 이를 free basis로 갖는다.

Quadratic relation으로부터 $$T_s(T_s - (q-1)) = q$$이 성립하므로 $$T_s$$는 가역이며, 그 역원은 다음의 식

$$T_s^{-1} = q^{-1} T_s + (q^{-1} - 1)$$

으로 명시적으로 주어진다. 보다 일반적으로, 임의의 $$w \in W$$에 대해 $$T_w$$는 가역이고 $$T_w^{-1} = T_{s_{i_\ell}}^{-1} \cdots T_{s_{i_1}}^{-1}$$로 표현된다.

<div class="remark" markdown="1">

<ins id="rmk2">**참고 2**</ins> Quadratic relation $$T_s^2 = (q-1)T_s + q$$는 $$q = 1$$일 때 $$T_s^2 = 1$$로 환원되며, 이 경우 $$H$$는 group algebra $$\mathbb{Z}[W]$$가 된다. 즉 Hecke algebra는 $$\mathbb{Z}[W]$$의 1-parameter 변형으로 이해할 수 있다. 한편 일부 문헌은 $$q^{1/2}$$ 대신 변수 $$v$$를 도입하여 $$q = v^2$$로 두거나, generator를 $$\widetilde{T}_s = q^{-1/2} T_s$$로 재정규화하여 quadratic relation을 $$\widetilde{T}_s^2 = (q^{1/2} - q^{-1/2}) \widetilde{T}_s + 1$$로 대칭화하기도 한다. 이러한 표기의 차이는 본질적인 수학적 내용에 영향을 주지 않는다.

</div>

## Bar involution

Kazhdan–Lusztig basis를 단일화하는 핵심 장치는 $$H$$ 위의 *bar involution*이다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> *Bar involution* $$\overline{\,\cdot\,} : H \to H$$는 $$\mathbb{Z}$$-algebra automorphism으로서, 다음의 식

$$\overline{q^{1/2}} = q^{-1/2},\qquad \overline{T_s} = T_s^{-1}$$

으로 정의된다.

</div>

Bar involution이 well-defined임을 확인하기 위해서는 $$T_s^{-1}$$이 $$T_s$$가 만족하는 모든 관계를 만족함을 보이면 충분하다. 우선 quadratic relation의 경우, $$T_s^{-1} = q^{-1} T_s + (q^{-1} - 1)$$로부터

$$\begin{aligned}
(T_s^{-1})^2 &= (q^{-1} T_s + q^{-1} - 1)^2 \\
&= q^{-2} T_s^2 + 2 q^{-1}(q^{-1} - 1) T_s + (q^{-1} - 1)^2 \\
&= q^{-2}\bigl((q-1) T_s + q\bigr) + 2 q^{-1}(q^{-1} - 1) T_s + (q^{-1} - 1)^2 \\
&= (q^{-1} - 1) T_s + q^{-1}
\end{aligned}$$

가 성립하고, 이는 변수 $$q$$를 $$q^{-1}$$로 치환한 quadratic relation과 정확히 일치한다. Braid relation은 $$T_s^{-1}$$들이 $$T_s$$들과 같은 braid relation을 만족함을 직접 확인할 수 있다. Bar involution은 $$\overline{T_w} = T_{w^{-1}}^{-1}$$로 standard basis 위에서 작용한다.

## Kazhdan–Lusztig basis

이제 Hecke algebra $$H$$ 위에서 bar involution에 의해 고정되는 특별한 basis를 도입한다. 이 basis의 존재성과 유일성이 본 글의 핵심 정리이다.

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4 (Kazhdan–Lusztig 1979)**</ins> 각 $$w \in W$$에 대하여, 다음 두 조건을 만족하는 유일한 원소 $$C_w \in H$$가 존재한다.

1. *Self-duality*: $$\overline{C_w} = C_w$$.
2. *Triangularity*: 어떤 다항식 $$P_{v, w}(q) \in \mathbb{Z}[q]$$가 존재하여

   $$C_w = q^{-\ell(w)/2} \sum_{v \le w} P_{v, w}(q)\, T_v$$

   가 성립하며, $$P_{w, w} = 1$$이고 $$v < w$$에 대해 $$\deg P_{v, w} \le \tfrac{1}{2}(\ell(w) - \ell(v) - 1)$$이다.

이 때 $$P_{v, w}(q)$$를 $$v, w$$에 대한 *Kazhdan–Lusztig polynomial*이라 부른다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

증명은 $$\ell(w)$$에 대한 induction과 명시적인 recursion으로 진행된다.

**기저.** $$w = e$$인 경우 $$C_e = T_e = 1$$로 두면 $$\overline{C_e} = 1 = C_e$$이고, $$P_{e, e} = 1$$로 모든 조건이 자명하게 만족된다.

**귀납 단계.** $$\ell(w) \ge 1$$이라 하고, $$\ell(w') < \ell(w)$$인 모든 $$w'$$에 대해 $$C_{w'}$$와 $$P_{v, w'}$$가 유일하게 결정되었다고 가정하자. $$s \in S$$를 $$sw < w$$가 성립하도록 (즉 $$\ell(sw) = \ell(w) - 1$$가 되도록) 선택한다. 그럼 정리 4 조건 2의 형태로 정규화한 generator

$$C_s := q^{-1/2}(T_s - q) = q^{-1/2} T_s - q^{1/2}$$

를 도입하면, $$\overline{C_s} = q^{1/2} T_s^{-1} - q^{-1/2} = q^{1/2}(q^{-1} T_s + q^{-1} - 1) - q^{-1/2} = q^{-1/2} T_s - q^{1/2} = C_s$$이므로 $$C_s$$는 bar-invariant이며, 실제로 $$C_s$$는 정리 4가 보장하는 $$w = s$$에 대응하는 원소이다.

이제 곱 $$C_s \cdot C_{sw}$$를 생각하면 이는 bar-invariant이며, standard basis의 전개에서 $$T_w$$의 계수가 $$q^{-\ell(w)/2}$$가 되도록 정규화되어 있다. 그러나 일반적으로 이 곱은 정리 4의 조건 2에 명시된 degree bound를 위배할 수 있으므로, 다음의 보정 항을 빼주어야 한다. 구체적으로

$$C_s \cdot C_{sw} = C_w + \sum_{\substack{z < w \\ sz < z}} \mu(z, sw)\, C_z$$

의 꼴이 성립하도록 정수 $$\mu(z, sw) \in \mathbb{Z}$$를 유일하게 결정할 수 있는데, 여기서 $$\mu(z, sw)$$는 $$P_{z, sw}(q)$$의 maximum-degree (즉 $$\tfrac{1}{2}(\ell(sw) - \ell(z) - 1)$$ 차) 계수로 주어진다. 이로부터 $$C_w$$를

$$C_w = C_s \cdot C_{sw} - \sum_{\substack{z < w \\ sz < z}} \mu(z, sw)\, C_z$$

으로 정의하면, bar-invariance는 우변의 각 항이 bar-invariant임으로부터 자동으로 따라오고, triangularity 및 degree bound는 $$\mu$$의 정의에 의해 보장된다.

**유일성.** $$C_w$$와 $$C_w'$$이 모두 정리 4의 조건을 만족한다고 하자. 그럼 $$D = C_w - C_w'$$은 bar-invariant이고, $$T_v$$ 전개에서 $$T_w$$의 계수가 $$0$$이며, 다른 모든 $$v < w$$에 대한 $$T_v$$ 계수는 $$\mathcal{A}$$의 원소로서 $$q^{-1/2}$$의 양의 거듭제곱만으로 표현된다. 그러나 bar-invariance는 이 계수가 $$q^{1/2}$$의 양의 거듭제곱으로도 표현됨을 강제하므로, 모든 계수가 $$0$$이 되어 $$D = 0$$이다.

</details>

위 증명에서 등장한 정수 $$\mu(v, w)$$는 *KL $$\mu$$-coefficient*라 불리며, KL polynomial의 leading-degree 계수로서 그 자체가 풍부한 조합적 정보를 담는다. 또한 $$P_{w, w} = 1$$ 외에도 $$v \le w$$에 대해 $$P_{v, w}(0) = 1$$이 성립한다는 사실은 정의로부터 어렵지 않게 따라온다.

<div class="remark" markdown="1">

<ins id="rmk5">**참고 5**</ins> 정리 4의 정규화는 Kazhdan–Lusztig 1979 원논문의 convention을 따른 것이다. 일부 문헌, 특히 Soergel을 비롯한 현대 categorification 문헌에서는 $$C_w$$ 대신 $$\underline{H}_w$$ 또는 $$b_w$$로 표기하고, generator 정규화에 따라 KL polynomial의 변수가 $$v = q^{1/2}$$ 또는 $$v^2 = q$$로 등장하기도 한다. 두 convention 사이의 변환은 단순한 변수 치환이므로 본질적 내용은 동일하다.

</div>

## R-polynomial과 inversion formula

KL polynomial과 짝을 이루는 또 하나의 중요한 다항식 family는 *R-polynomial*이다. 이는 bar involution이 standard basis 위에서 어떻게 작용하는지를 기술한다.

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> $$v, w \in W$$에 대하여, *R-polynomial* $$R_{v, w}(q) \in \mathbb{Z}[q]$$는 다음의 전개

$$\overline{T_{w^{-1}}^{-1}} = q^{-\ell(w)} \sum_{v \le w} R_{v, w}(q)\, T_v$$

에서 유일하게 결정되는 다항식으로 정의된다. 즉, $$R_{v, w}(q)$$는 standard basis 위에서 bar involution을 standard basis로 다시 전개할 때 등장하는 계수이다.

</div>

R-polynomial은 다음의 recursion으로 효율적으로 계산된다: $$sw < w$$인 $$s \in S$$를 고를 때,

$$R_{v, w}(q) = \begin{cases} R_{sv, sw}(q), & \text{if } sv < v, \\ (q - 1) R_{v, sw}(q) + q\, R_{sv, sw}(q), & \text{if } sv > v. \end{cases}$$

또한 $$R_{w, w} = 1$$이며, $$v \not\le w$$이면 $$R_{v, w} = 0$$이다.

KL polynomial과 R-polynomial은 다음의 *inversion formula*를 통해 서로를 결정한다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> 임의의 $$v \le w$$에 대하여,

$$q^{\ell(w) - \ell(v)} \overline{P_{v, w}(q)} - P_{v, w}(q) = \sum_{v < z \le w} (-1)^{\ell(z) - \ell(v)} R_{v, z}(q)\, P_{z, w}(q)$$

가 성립한다. 여기서 $$\overline{P_{v, w}(q)} = P_{v, w}(q^{-1})$$이며, 이 식의 좌변은 KL polynomial의 명시적인 항등식을 통해 R-polynomial들의 합으로 표현된다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

KL basis의 self-duality $$\overline{C_w} = C_w$$를 정의 [정리 4](#thm4) 조건 2의 standard basis 표현에 대입하면

$$q^{-\ell(w)/2} \sum_{v \le w} P_{v, w}(q)\, T_v = \overline{q^{-\ell(w)/2} \sum_{v \le w} P_{v, w}(q)\, T_v} = q^{\ell(w)/2} \sum_{v \le w} \overline{P_{v, w}(q)} \cdot \overline{T_v}$$

가 성립한다. 이 우변에 $$\overline{T_v} = T_{v^{-1}}^{-1}$$의 inverse-transform과 R-polynomial을 통한 standard basis 재전개를 적용하고, 결과의 양변에서 $$T_v$$의 계수를 비교하면 위의 항등식을 얻는다. 자세한 계산은 [BB, Theorem 5.1.4]를 참조한다.

</details>

이 inversion formula는 작은 Coxeter group에 대해 KL polynomial을 손으로 계산할 때 가장 직접적인 도구가 되며, 또한 [BB, Chapter 5]에서 자세히 다루는 KL polynomial의 여러 항등식의 출발점이 된다.

## Schubert variety의 intersection cohomology

지금까지 정의한 KL polynomial은 순수히 조합적인 대상이지만, 본 글의 motivation에서 언급한 대로 이는 Schubert variety의 특이점에 대한 깊은 기하학적 정보를 담고 있다. 본 절에서는 그 핵심 statement만을 정리한다.

$$G$$를 complex reductive algebraic group, $$B$$를 그 Borel subgroup, $$W$$를 Weyl group이라 하고, [§Bruhat decomposition, ⁋정의 16](/ko/math/lie_theory/bruhat_decomposition#def16)에서와 같이 Schubert variety $$X_w = \overline{BwB/B} \subseteq G/B$$를 생각한다. $$X_w$$ 위의 *intersection cohomology sheaf* $$\operatorname{IC}_{X_w}$$는 $$X_w$$가 매끄러운 경우에는 상수층 (constant sheaf) 의 shift와 일치하지만, 특이점이 있는 경우에는 이를 적절히 보정하여 Poincaré duality를 회복시키는 derived category $$D^b_c(X_w)$$의 perverse sheaf로 정의된다.

<div class="proposition" markdown="1">

<ins id="thm8">**정리 8 (Kazhdan–Lusztig conjecture, 기하학적 형태)**</ins> Schubert variety $$X_w \subseteq G/B$$와 그 안의 점 $$v B/B \in X_v^\circ \subseteq X_w$$ ($$v \le w$$)에 대하여, intersection cohomology sheaf의 stalk cohomology의 Poincaré 다항식은 KL polynomial로 주어진다.

$$\sum_{i \ge 0} \dim \mathcal{H}^i(\operatorname{IC}_{X_w})_{vB/B} \cdot q^{i/2} = P_{v, w}(q)$$

특히 $$P_{v, w}(q) = 1$$인 것은 점 $$vB/B$$에서 $$X_w$$가 매끄러운 것과 동치이다.

</div>

<details class="proof" markdown="1">
<summary>증명 (개략)</summary>

이 statement는 Kazhdan–Lusztig가 1979년 논문에서 conjecture로 제시하였으며, 이후 Beilinson–Bernstein과 Brylinski–Kashiwara가 독립적으로 증명하였다. 증명의 핵심은 다음 세 단계로 요약된다. 먼저 flag variety $$G/B$$ 위의 *holonomic $$D$$-module의 category*와 (Verma module의 category $$\mathcal{O}$$의 적당한 block)이 *Beilinson–Bernstein localization*에 의해 동치임을 보인다. 이 동치 하에서 Schubert cell $$X_v^\circ$$를 따라 정의된 simple highest-weight module은 $$X_w$$의 *intersection cohomology* perverse sheaf $$\operatorname{IC}_{X_w}$$에 대응한다. 두 번째 단계로 *Riemann–Hilbert correspondence*에 의해 holonomic $$D$$-module category와 perverse sheaf category가 동치임을 사용하여 위의 대응을 IC sheaf 수준으로 옮긴다. 마지막으로 Hecke algebra의 KL basis $$C_w$$가 정확히 *Grothendieck group* 수준에서 $$[\operatorname{IC}_{X_w}]$$의 class로 실현됨을 보이면, $$C_w = T_w + \sum_v P_{v,w}(q) T_v$$의 계수 $$P_{v,w}(q)$$가 $$\operatorname{IC}_{X_w}$$의 stalk cohomology의 Poincaré 다항식을 주게 된다. 자세한 내용은 [BB, §6.2] 및 [Hum, Chapter 8]을 참조한다.

</details>

이로부터 다음 매끄러움 판정 기준이 즉시 따른다.

<div class="proposition" markdown="1">

<ins id="cor9">**따름정리 9**</ins> Schubert variety $$X_w$$가 매끄러운 것은 모든 $$v \le w$$에 대해 $$P_{v, w}(q) = 1$$인 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$X_w$$의 매끄러움은 모든 점 $$vB/B \in X_w$$에서 매끄러움을 의미하므로, 이는 모든 $$v \le w$$에 대해 $$\mathcal{H}^i(\operatorname{IC}_{X_w})_{vB/B}$$가 $$i = 0$$에서만 1차원이고 다른 차수에서는 $$0$$임을 뜻한다. 정리 [정리 8](#thm8)에 의해 이는 $$P_{v, w}(q) = 1$$과 동치이다.

</details>

이 따름정리는 일반적으로 매끄러움 판정 문제가 KL polynomial의 계산으로 환원됨을 보여준다. 실제로 type $$A$$에서는 이 조건이 pattern avoidance (Lakshmibai–Sandhya 정리에 의해 permutation $$w$$가 패턴 $$3412$$와 $$4231$$을 피한다는 것) 와 동치이며, 다른 type에 대해서도 유사한 조합적 매끄러움 판정이 알려져 있다.

## 작은 예시

KL polynomial이 어떻게 행동하는지 감을 잡기 위해, 가장 작은 비자명한 예시들을 살펴본다.

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> $$W = S_3$$, 즉 $$A_2$$ type Weyl group을 생각하자. $$S = \{s_1, s_2\}$$이고 $$\lvert W\rvert = 6$$이다. 이 경우 모든 $$v \le w$$에 대해 $$P_{v, w}(q) = 1$$이 성립한다. 따름정리 [따름정리 9](#cor9)에 의해 이는 $$GL_3$$의 모든 Schubert variety $$X_w \subseteq GL_3/B$$가 매끄러움을 의미하며, 이는 실제로 잘 알려진 사실이다.

</div>

<div class="example" markdown="1">

<ins id="ex11">**예시 11**</ins> $$W = S_4$$, 즉 $$A_3$$ type Weyl group을 생각하자. 이 경우에도 거의 모든 $$P_{v, w}$$가 1로 주어지지만, 정확히 다음 한 쌍에서 처음으로 비자명한 KL polynomial이 등장한다. $$w = s_2 s_1 s_3 s_2$$ (one-line notation으로 $$w = 3412$$, $$\ell(w) = 4$$) 와 $$v = e$$ ($$v = 1234$$, $$\ell(v) = 0$$) 를 잡으면

$$P_{e, w}(q) = 1 + q$$

가 성립한다. 정리 [정리 8](#thm8)에 의해 이는 $$X_w = X_{3412}$$가 identity coset $$eB/B$$에서 특이점을 갖는다는 것을 의미하며, 그 stalk intersection cohomology가 0차와 2차에서 각각 1차원임을 알려준다. 한편 동일한 $$S_4$$ 안에서 $$w = s_1 s_3 s_2 s_1 s_3$$ ($$w = 4231$$, $$\ell(w) = 5$$) 와 $$v = e$$에 대해서도 비자명한 KL polynomial $$P_{e, 4231}(q) = 1 + q$$가 등장하며, 이 두 경우 ($$3412$$와 $$4231$$) 가 type $$A_3$$에서 매끄러움이 깨지는 유일한 reduced situation이다. 이는 앞서 언급한 Lakshmibai–Sandhya의 pattern $$3412, 4231$$ avoidance 정리의 가장 작은 사례이다.

</div>

위의 예시 [예시 11](#ex11)에서 처음으로 등장한 다항식 $$1 + q$$는 매우 단순한 형태이지만, 일반적인 Weyl group에서는 KL polynomial이 매우 복잡한 형태를 가질 수 있다. 사실 KL polynomial의 계수가 항상 비음 (non-negative) 이라는 추측 (KL positivity conjecture) 은 [정리 8](#thm8)의 기하학적 해석에서 곧장 따라오지만, 일반 Coxeter group, 특히 finite type을 벗어난 경우에는 매우 어려운 문제이며 Elias–Williamson의 Soergel bimodule 이론을 통해 비로소 일반적으로 증명되었다.

KL polynomial은 본 시리즈의 다른 글들과도 직접적으로 연결된다. [§Richardson variety와 Peterson variety](/ko/math/lie_theory/richardson_peterson_variety)에서 정의한 Richardson variety는 두 Schubert variety의 transversal한 교차로서, 그 stalk intersection cohomology가 KL polynomial의 차이로 기술되는 자연스러운 기하학적 무대이다.

---

**참고문헌**

**[KL79]** D. Kazhdan, G. Lusztig, *Representations of Coxeter groups and Hecke algebras*, Invent. Math. **53** (1979), 165–184.

**[KL80]** D. Kazhdan, G. Lusztig, *Schubert varieties and Poincaré duality*, Geometry of the Laplace operator, Proc. Sympos. Pure Math. **36**, AMS, 1980, 185–203.

**[Hum]** J. E. Humphreys, *Reflection groups and Coxeter groups*, Cambridge Studies in Advanced Mathematics **29**, Cambridge University Press, 1990.

**[BB]** A. Björner, F. Brenti, *Combinatorics of Coxeter groups*, Graduate Texts in Mathematics **231**, Springer, 2005.

**[EW]** B. Elias, G. Williamson, *The Hodge theory of Soergel bimodules*, Ann. of Math. (2) **180** (2014), 1089–1136.
