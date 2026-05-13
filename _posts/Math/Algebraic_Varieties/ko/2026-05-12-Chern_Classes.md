---
title: "천 특성류"
excerpt: "벡터다발의 Chern classes와 그 성질들"

categories: [Math / Algebraic Varieties]
permalink: /ko/math/algebraic_varieties/chern_classes
sidebar: 
    nav: "algebraic_varieties-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Chern_classes.png
    overlay_filter: 0.5

date: 2026-05-12
last_modified_at: 2026-05-12
weight: 22
published: false
---

벡터다발은 대수기하학에서 기하적 대상을 다루는 데 핵심적인 도구로, 우리는 이번 글에서 주어진 벡터다발이 얼마나 뒤틀려있는지 측정하는 *Chern class*를 이번 글에서 정의한다. 이는 complex vector bundle에 대해 정의되는 위상적·기하적 불변량으로, 우리는 대수위상에서와 마찬가지로 Chern class를 공리적으로 정의하고, 이를 계산하는 데 필수적인 splitting principle을 소개한 뒤, 여러 구체적인 예시를 통해 그 성질을 살펴볼 것이다. 모든 논의는 적당한 base space $$X$$ 위의 complex vector space에서 이뤄지며, 우리는 $$H^\bullet(X, \mathbb{Z})$$를 사용한다. Cohomology convention에 따라 우리는 $$k$$차원 Chern class는 $$2k$$차원 cohomology에 들어있는 것을 기억하자. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Complex vector bundle $$\mathcal{E} \to X$$에 대해 $$c_i(\mathcal{E}) \in H^{2i}(X, \mathbb{Z})$$가 주어지며, 이들을 *Chern classes<sub>천 특성류</sub>*라고 부른다. 이들은 다음의 공리들을 만족한다.

1. *Naturality* 연속함수 $$f: Y \to X$$에 대하여

   $$c_i(f^{\ast} \mathcal{E}) = f^{\ast} c_i(\mathcal{E})$$

   이 성립한다. 여기서 $$f^{\ast}$$은 cohomology에서의 pullback이다.

2. *Whitney sum formula* 두 vector bundle $$\mathcal{E}, \mathcal{F}$$에 대하여,

   $$c(\mathcal{E} \oplus \mathcal{F}) = c(\mathcal{E}) \smile c(\mathcal{F})$$

   이 성립한다. 여기서 $$c(\mathcal{E}) = \sum_{i \ge 0} c_i(\mathcal{E})$$는 *total Chern class*이며, 우변의 곱은 cup product이다.

3. *Normalization* $$\mathcal{L} \to X$$가 line bundle일 때,

   $$c(\mathcal{L}) = 1 + c_1(\mathcal{L})$$

   이고, 특히 $$X = \mathbb{P}^n$$ 위의 tautological line bundle $$\mathcal{O}(-1)$$에 대해 $$c_1(\mathcal{O}(1))$$은 $$H^2(\mathbb{P}^n, \mathbb{Z})$$의 생성원을 준다.

</div>

그럼 이것이 제대로 된 정의가 되기 위해서는 다음 명제가 필요하다. 

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 위의 공리를 만족하는 Chern class는 유일하게 존재한다.

</div>

이제 이들을 generating function 삼아 다음을 정의한다. 

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Rank $$r$$ vector bundle $$\mathcal{E}$$에 대해, *Chern polynomial* $$c_\t(\mathcal{E})$$를 formal variable $$\t$$에 대한 다항식

$$c_\t(\mathcal{E}) = 1 + c_1(\mathcal{E})\t + c_2(\mathcal{E})\t^2 + \cdots + c_r(\mathcal{E})\t^r$$

으로 정의한다.

</div>

## Chern class의 성질들

이제 우리는 Chern class의 성질들을 추가로 살펴보고, 이를 통해 Chern class의 기하학적 의미를 살펴본다. 우선 line bundle에 대해서는 Chern class를 더 잘 이해할 수 있다. 

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $$X$$가 smooth variety이고, $$\mathcal{L} \to X$$가 line bundle이라 하자. 그럼 Cartier divisor $$\divisor(s)=(\mathcal{L}, s)$$에 대하여,

$$c_1(\mathcal{L}) = [\divisor(s)] \in \CH^1(X)$$

이 성립한다. 특히, $$\mathcal{L} = \mathcal{O}_X(D)$$로 표현될 때 $$c_1(\mathcal{L}) = [D]$$이다.

</div>

즉 이 명제의 핵심은 line bundle에 대해서는 $$\mathcal{L}$$의 *아무* section $$s$$를 택하고 그것이 정의하는 divisor를 생각하면, 이것이 $$\CH^1(X)$$의 원소를 정의하며 이는 $$s$$의 선택에 의존하지 않는다는 것이다. 뿐만 아니라, 이를 Weil divisor $$D$$의 꼴로 적으면 $$c_1(\mathcal{L})$$은 정확히 $$D$$에 해당하는 class가 나오게 된다. 

이 명제에 대한 증명은 exponential exact sequence 

$$0 \to \mathbb{Z} \to \mathcal{O}_X \to \mathcal{O}_X^\ast \to 0$$

로부터 유도되는 connecting homomorphism $$H^1(X, \mathcal{O}_X^\ast) \to H^2(X, \mathbb{Z})$$를 통해 이루어진다. Line bundle은 $$\mathcal{O}_X^\ast$$의 cocycle으로 주어지며, 이에 대응하는 cohomology class가 바로 $$c_1(\mathcal{L})$$이다. 동시에 divisor $$D$$는 $$\CH^1(X)$$의 원소로, 이 두 가지 관점이 Poincaré duality를 통해 일치함을 확인할 수 있다.

우리는 Picard group에서 $$\otimes$$와 $$(-)^\vee$$가 어떠한 식으로 연산을 주는지 보았는데, 이 또한 다음과 같이 잘 연결된다. 

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> $$\mathcal{L}, \mathcal{M}$$이 같은 베이스 $$X$$ 위의 line bundle들이라 하자. 그러면 다음이 성립한다.

1. $$c_1(\mathcal{L} \otimes \mathcal{M}) = c_1(\mathcal{L}) + c_1(\mathcal{M})$$,
2. $$c_1(\mathcal{L}^{\vee}) = -c_1(\mathcal{L})$$.

</div>

따라서, line bundle의 경우 우리는 Chern class를 잘 계산할 수 있을 뿐 아니라 이것이 갖는 연산까지도 잘 보존된다는 것을 안다. 우리가 기대할 수 있는 가장 좋은 일은 이것이 모든 vector bundle의 계산을 가능케 하는 것이겠지만, 일반적으로 vector bundle을 항상 line bundle들의 direct sum으로 분해할 수 있는 것은 아니므로 이것이 바로 가능하지는 않다. 그러나 다음의 splitting principle을 이용하면, 임의의 vector bundle에 대한 Chern class의 계산을 line bundle의 경우로 환원할 수 있다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6 (Splitting principle)**</ins> $$\mathcal{E} \to X$$를 rank $$r$$인 vector bundle이라 하자. 그러면 어떤 연속사상 $$f: Y \to X$$가 존재하여 다음 두 조건을 만족한다.

1. $$f^{\ast}: H^{\ast}(X, \mathbb{Z}) \to H^{\ast}(Y, \mathbb{Z})$$는 단사이다.
2. $$f^{\ast} \mathcal{E}$$는 line bundle $$\mathcal{L}_1, \mathcal{L}_2, \ldots, \mathcal{L}_r$$들의 직합 $$\mathcal{L}_1 \oplus \cdots \oplus \mathcal{L}_r$$으로 분해된다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$f: Y = \mathbb{P}(\mathcal{E}) \to X$$를 projectivization으로 정의한다. $$\mathbb{P}(\mathcal{E})$$ 위에는 tautological line bundle $$S \subset \pi^{\ast} \mathcal{E}$$가 존재하며, quotient bundle $$Q = (\pi^{\ast} \mathcal{E})/S$$는 rank $$r-1$$이다. \mathcal{L}eray-Hirsch theorem에 의해 $$\pi^{\ast}: H^{\ast}(X) \to H^{\ast}(\mathbb{P}(\mathcal{E}))$$는 단사이고, $$H^{\ast}(\mathbb{P}(\mathcal{E}))$$는 $$1, \xi, \xi^2, \ldots, \xi^{r-1}$$을 basis로 하는 자유 $$H^{\ast}(X)$$-module이다. 여기서 $$\xi = c_1(\mathcal{O}_\mathcal{E}(1))$$이다. 이제 $$Q$$에 대해 같은 과정을 반복하면, 적당한 $$Y \to X$$를 얻어 $$f^{\ast} \mathcal{E}$$가 line bundle들의 직합으로 분해됨을 확인할 수 있다.

</details>

Splitting principle의 핵심은 다음과 같다. 임의의 vector bundle $$\mathcal{E}$$는 일반적으로 line bundle들의 직합으로 분해되지 않는다. 이는 마치 실수 계수를 가진 다항식이 실수 위에서는 인수분해되지 않을 수 있지만, 복소수로 확장하면 항상 근을 갖는 것과 유사하다. Splitting principle은 이러한 "확장"의 기하학적 버전으로, 원래 공간 $$X$$에서는 $$\mathcal{E}$$가 twisted되어 있어 line bundle으로 쪼갤 수 없지만, 더 큰 공간 $$Y$$로 올라가면(적절한 fiber bundle을 취함으로써) twist가 풀리고 $$\mathcal{E}$$가 line bundle들의 직합으로 보인다는 것이다.

핵심은 $$f^\ast: H^\ast(X) \to H^\ast(Y)$$가 단사라는 점이다. 이는 $$Y$$가 $$X$$보다 "더 복잡한" 공간이 아니라, $$X$$의 위상적·기하학적 정보를 잃지 않으면서 단순화시키는 공간임을 의미한다. 

예를 들어 Whitney sum formula $$c(\mathcal{E} \oplus \mathcal{F}) = c(\mathcal{E}) \smile c(\mathcal{F})$$를 보이고자 할 때, splitting principle에 의해 $$\mathcal{E} = \bigoplus \mathcal{L}_i$$, $$\mathcal{F} = \bigoplus \mathcal{M}_j$$로 가정할 수 있다. 이때

$$c(\mathcal{E} \oplus \mathcal{F}) = \prod_{i,j} (1 + x_i)(1 + y_j) = \biggl(\prod_i (1 + x_i)\biggr) \smile \biggl(\prod_j (1 + y_j)\biggr) = c(\mathcal{E}) \smile c(\mathcal{F})$$

이고, $$f^\ast$$가 단사이므로 이 등식은 원래 공간 $$X$$에서도 성립한다.

## 천 근과 천 문자

위에서 언급한 것과 같이, 우리는 splitting principle을 바탕으로 임의의 vector bundle을 마치 line bundle들의 직합인 것처럼 다룰 수 있다. 이제 다음을 정의하자. 

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> Rank $$r$$ vector bundle $$\mathcal{E}$$를 생각하고, 이를 splitting principle에 의해 $$f^{\ast} \mathcal{E} = \mathcal{L}_1 \oplus \cdots \oplus \mathcal{L}_r$$로 분해하자. 그럼 이 때 $$x_i = c_1(\mathcal{L}_i) \in H^2(Y)$$를 $$\mathcal{E}$$의 *Chern root<sub>천 근</sub>*들이라 부르며, 이들을 사용하여 $$\mathcal{E}$$의 *Chern polynomial*을

$$c_\t(\mathcal{E}) = \prod_{i=1}^r (1 + x_i \t)$$

으로 정의한다. 이 전개에서 $$c_k(\mathcal{E})$$는 $$x_1, \ldots, x_r$$의 $$k$$-차 elementary symmetric polynomial이 된다.

</div>

그럼 위의 전개에서 각각의 $$c_k(\mathcal{E})$$는 Chern root들 $$x_1,\ldots, x_r$$의 $$k$$차 elementary symmetric polynomial이 된다. 한편 Chern polynomial의 문제 중 하나는 vector bundle의 direct sum이 Chern polynomial에서는 곱셈으로 나온다는 것이다. 이를 위해 exponential을 사용하여 우리는 *Chern character* $$\chern(\mathcal{E})$$를

$$\chern(\mathcal{E}) = \sum_{i=1}^r e^{x_i} = r + c_1(\mathcal{E}) + \frac{c_1(\mathcal{E})^2 - 2c_2(\mathcal{E})}{2} + \cdots\in H^\bullet(X, \mathbb{Q})$$

로 정의한다. 여기서 이차 이상의 항은 elementary symmetric polynomial로부터 계산해야 함을 기억하자. 어쨌든 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> Chern character는 다음의 성질을 만족한다.

1. $$\chern(\mathcal{E} \oplus \mathcal{F}) = \chern(\mathcal{E}) + \chern(\mathcal{F})$$,
2. $$\chern(\mathcal{E} \otimes \mathcal{F}) = \chern(\mathcal{E}) \cup \chern(\mathcal{F})$$.

즉, Chern character는 vector bundle들의 direct sum을 cohomology의 덧셈으로, tensor product를 cup product로 본다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Splitting principle에 의해 $$\mathcal{E} = \bigoplus \mathcal{L}_i$$, $$\mathcal{F} = \bigoplus \mathcal{M}_j$$로 가정할 수 있다. 이때

$$\chern(\mathcal{E} \oplus \mathcal{F}) = \sum_i e^{x_i} + \sum_j e^{y_j} = \chern(\mathcal{E}) + \chern(\mathcal{F})$$

이고,

$$\chern(\mathcal{E} \otimes \mathcal{F}) = ch\bigg(\bigoplus_{i,j} \mathcal{L}_i \otimes \mathcal{M}_j\bigg) = \sum_{i,j} e^{x_i + y_j} = \bigg(\sum_i e^{x_i}\bigg)\bigg(\sum_j e^{y_j}\bigg) = \chern(\mathcal{E}) \cup \chern(\mathcal{F})$$

이므로 성립한다.

</details>

한편 우리는 exceptional divisor를 계산할 때 projectivized bundle을 사용했었는데, 이와 같이 projectivized bundle을 계산할 때를 위해 다음의 명제를 사용하자. 

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> (Projective bundle formula) $$\pi: \mathbb{P}(\mathcal{E}) \to X$$를 rank $$r$$ vector bundle $$\mathcal{E}$$의 projectivization이라 하고, $$\xi = c_1(\mathcal{O}_\mathcal{E}(1)) \in H^2(\mathbb{P}(\mathcal{E}))$$라 하자. 그러면 $$H^{\ast}(X)$$-algebra isomorphism

$$H^{\ast}(\mathbb{P}(\mathcal{E})) \cong H^{\ast}(X)[\xi] / (\xi^r + \pi^{\ast}c_1(\mathcal{E})\xi^{r-1} + \cdots + \pi^{\ast}c_r(\mathcal{E}))$$

이 존재한다. 특히 $$H^{\ast}(\mathbb{P}(\mathcal{E}))$$는 $$H^{\ast}(X)$$-module로서 $$\{1, \xi, \xi^2, \ldots, \xi^{r-1}\}$$을 basis로 갖는다.

</div>

이 명제로부터 Chern class를 projective bundle의 cohomology ring의 관계식으로 정의할 수도 있다. 위의 식에서 $$\xi$$에 대한 $$r$$-차 관계식의 계수가 바로 $$c_i(\mathcal{E})$$가 된다.

## 접다발의 천 클래스와 오일러 지표

Chern class의 가장 중요한 응용 중 하나는 compact complex manifold의 topological Euler characteristic을 계산하는 것으로, 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> (Poincaré-Hopf) $$X$$를 $$n$$-차원 compact complex manifold라 하자. 그러면

$$\rchi_{\mathrm{top}}(X) = \int_X c_n(T_X)$$

이 성립한다. 여기서 $$\rchi_{\mathrm{top}}(X) = \sum_{i=0}^{2n} (-1)^i \dim H^i(X, \mathbb{Q})$$는 topological Euler characteristic이다.

</div>

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic geometry*, Springer, 1977.  
**[Ful]** W. Fulton, *Intersection theory*, Springer, 1998.  
**[BT]** R. Bott and L. Tu, *Differential forms in algebraic topology*, Springer, 1982.