---
title: "스펙트럼 열"
excerpt: ""

categories: [Math / Homological Algebra]
permalink: /ko/math/homological_algebra/spectral_sequences
header:
    overlay_image: /assets/images/Math/Homological_Algebra/Spectral_Sequences.png
    overlay_filter: 0.5
sidebar: 
    nav: "homological_algebra-ko"

date: 2026-04-08
last_modified_at: 2026-04-12
weight: 7
published: false

---

우리는 앞선 글에서 $$\Ext$$와 $$\Tor$$의 balancing을 증명하며, filtration과 이를 이용한 귀납법을 유용하게 사용하였다. 이는 이번 글에서 다룰 spectral sequence의 원시적인 형태라 생각할 수 있다. Spectral sequence는 filtration이 주어진 cochain complex의 cohomology를, 단계적으로 page를 거쳐 근사하는 체계적인 방법이다. 이러한 데이터를 공식적으로 정의하자.

## Spectral Sequence

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> *Spectral sequence<sub>스펙트럼 열</sub>*는 다음과 같은 데이터의 모임이다. 

1. Bigraded object $$E_r=(E_r^{p,q})_{p,q}$$,
2. $$E_r$$ 위의 bidegree $$(r,1-r)$$ differential $$d_r:E_r^{p,q}\rightarrow E_r^{p+r, q-r+1}$$ (즉, $$d_r^2=0$$)

각 $$r$$에 대하여, bigraded complex $$(E_r^{p,q}, d_r)$$을 *$$r$$번째 page*라고 부른다. 이 때 이들 두 데이터는 다음의 식

$$E_{r+1}^{p,q}\cong \frac{\ker(d_r^{p,q}: E_r^{p,q}\rightarrow E_r^{p+r,q-r+1})}{\im(d_r^{p-r,q+r-1}: E_r^{p-r, q+r-1}\rightarrow E_r^{p,q})}$$

을 통해 연결된다.

</div>

$$E_r$$ page의 원소들을 평면 상의 점 $$(p,q)$$로 시각화한다면, $$d_r^{p,q}$$는 점 $$(p,q)$$에서 $$(p+r, q-r+1)$$로 가는 것이며 이러한 점들이 cochain complex를 구성한다. 특히 $$E_{r+1}^{p,q}$$는 이러한 관점에서 $$(p,q)$$를 지나는 cochain complex의 $$(p,q)$$ 점에서의 cohomology로 생각할 수 있다. 

## Filtered Complex

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Cochain complex $$A^\bullet$$ 위의 *decreasing filtration<sub>감소 여과</sub>* $$F$$는 다음 조건을 만족하는 subcomplex들의 열

$$\cdots \supset F^{p-1}A^\bullet \supset F^pA^\bullet \supset F^{p+1}A^\bullet \supset \cdots$$

이다. 즉 각 $$p$$에 대해 $$F^p A^\bullet$$은 $$A^\bullet$$의 subcomplex이며, $$d(F^p A^i) \subset F^p A^{i+1}$$이다. Filtered complex는 대상 $$(A^\bullet, F)$$로 표기한다.

</div>

예를 들어 [§Ext와 Tor, ⁋명제 3](/ko/math/homological_algebra/ext_and_tor#prop3)의 증명에서 우리는 total complex $$A^\bullet=\Tot(K)^\bullet$$의 horizontal/vertical degree를 이용하여 filtration을 정의했었다. 위의 [정의 2](#def2)는 이보다 아주 일반화된 버전이라 생각할 수 있지만, 어쨌든 complex를 더 세밀하게 쪼갠다는 철학 자체는 동일하다. 즉, $$p$$가 증가함에 따라 $$F^p A^\bullet$$은 점점 더 작아지며, 각 단계에서 새로운 정보가 추가된다. 또 우리는 위의 [§Ext와 Tor, ⁋명제 3](/ko/math/homological_algebra/ext_and_tor#prop3)의 증명에서 귀납법을 적용하기 위해 $$F^{p+1}A^\bullet/F^pA^\bullet$$을 생각하여 이를 원래의 double complex $$K^{p, \bullet-p}$$로 생각하였는데, 일반적인 경우에도 이 정보는 <em-ko>정확히</em-ko> $$p$$번째 filtration을 담는다는 점에서 중요하다. 이렇게 얻어진 cochain complex

$$\mathrm{Gr}^p A^\bullet = F^p A^\bullet / F^{p+1} A^\bullet$$

를 $$F$$에 대한 *associated graded complex*라 부른다. 이 때 이 complex의 differential은 물론 원래의 cochain complex $$A^\bullet$$에서의 differential로부터 오는 것이다. 

Double complex와 total complex는 ([§사슬호몰로지, ⁋정의 4](/ko/math/homological_algebra/homology#def4))에서 정의되었으며, ([§Ext와 Tor, ⁋명제 3](/ko/math/homological_algebra/ext_and_tor#prop3))에서 구체적인 계산을 수행하였다.

## 예시: Ext와 Tor의 balancedness

이제 앞서 정의한 도구들을 이용하여, [§Ext와 Tor, ⁋명제 3](/ko/math/homological_algebra/ext_and_tor#prop3)에서 이미 수행했던 계산을 spectral sequence의 언어로 다시 살펴보자.

[§Ext와 Tor, ⁋명제 3](/ko/math/homological_algebra/ext_and_tor#prop3)에서 우리는 $$K^{p,q} = \Hom_A(P_q, I^p)$$로 주어지는 double complex ([§호몰로지, ⁋정의 4](/ko/math/homological_algebra/homology#def4))의 total complex $$\Tot(K)^\bullet$$을 다루었다. 여기서 $$P_\bullet \to M$$은 projective resolution이고 $$N \to I^\bullet$$은 injective resolution이다.

명제 3의 증명에서 우리는 $$\Tot(K)^\bullet$$ 위에

$$F^p \Tot(K)^k = \bigoplus_{i \geq p, \, i+q=k} K^{i,q}$$

라는 filtration을 사용했다. 이것은 [정의 2](#def2)의 decreasing filtration의 구체적인 예시이다: $$p$$가 커질수록 $$F^p$$는 더 적은 성분만을 포함하며, $$F^{p+1} \Tot(K)^\bullet \subset F^p \Tot(K)^\bullet$$이 성립한다.

[정의 1](#def1)에 의해 이 filtration으로부터 spectral sequence가 유도된다. $$E_0$$ page는 associated graded이며, $$E_0^{p,q} = \mathrm{Gr}^p \Tot(K)^{p+q} = K^{p,q}$$이다. $$d_0$$는 double complex의 vertical differential $$d_v$$에 해당하므로

$$E_1^{p,q} = H^q(K^{p,\bullet}, d_v)$$

이다. $$P_\bullet \to M$$이 resolution이므로 $$E_1^{p,q} = \Hom_A(M, I^p)$$를 얻는다. 즉, **$$E_1$$ page는 이미 vertical 방향으로는 계산이 끝난 상태**다.

이제 $$E_1$$에서 $$E_2$$로의 page 전이를 살펴보자. $$E_1^{p,q} = \Hom_A(M, I^p)$$이며, $$d_1$$은 double complex의 horizontal differential $$d_h$$에 의해 유도된 사상이다. 즉 $$I^p \to I^{p+1}$$로부터 얻어지는 $$\Hom_A(M, I^p) \to \Hom_A(M, I^{p+1})$$이므로, 각 고정된 $$q$$에 대해 $$E_1^{\bullet, q}$$는 $$\Hom_A(M, I^\bullet)$$ 복합체를 이룬다. 따라서

$$E_2^{p,q} = H^q(\Hom_A(M, I^\bullet)) = \Ext^q_A(M, N)$$

이다. 여기서 중요한 점은, [§Ext와 Tor, ⁋명제 3](/ko/math/homological_algebra/ext_and_tor#prop3)의 증명에서 귀납법으로 계산한 것이 바로 이 $$E_1 \to E_2$$ page 전이에 해당한다는 것이다. 이 경우 $$d_1$$ 이후의 미분 $$d_r$$ ($$r \geq 2$$)은 모두 trivial하므로 $$E_2 = E_\infty$$이다.

[정의 4](#def4)에 의해 $$E_\infty^{p,q} = \mathrm{Gr}^p H^{p+q}(\Tot(K)^\bullet)$$이다. 그러나 명제 3의 증명에서 확인했듯, 각 $$n$$에 대해 $$p > n$$이면 $$H^n(F^p) \cong H^n(F^{p+1})$$이고 $$p < 0$$이면 $$F^p H^n = H^n$$이므로, 사실상 filtration은 split된다. 따라서

$$H^n(\Tot(K)^\bullet) \cong \bigoplus_p E_\infty^{p, n-p} = \Ext^n_A(M, N)$$

를 얻는다.

이것은 spectral sequence가 단 한 번의 page 전이($$E_1 \to E_2$$)에서 안정화되는 매우 단순한 예시이다. 더 일반적인 상황에서는 여러 번의 page 전이가 필요하며, 이것이 spectral sequence의 진정한 힘이 발휘되는 곳이다.

## Filtered Complex의 Spectral Sequence

Filtered complex $$(A^\bullet, F)$$로부터 spectral sequence를 구성하는 구체적인 과정을 설명한다. 이것은 spectral sequence의 가장 기본적인 출발점이다.

먼저, filtration $$F$$에 의해 $$A^\bullet$$의 cohomology $$H^n(A^\bullet)$$에도 자연스러운 filtration이 유도된다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Filtered complex $$(A^\bullet, F)$$에 대해, $$H^n(A^\bullet)$$ 위의 filtration을

$$F^p H^n = \operatorname{im}\bigl(H^n(F^p A^\bullet) \to H^n(A^\bullet)\bigr)$$

로 정의한다. 여기서 사상은 포함 $$F^p A^\bullet \hookrightarrow A^\bullet$$에 의해 유도된다.

</div>

이 filtration은 $$F^p A^\bullet$$에 포함된 cocycle들이 유도하는 cohomology class들로 이루어진다. $$p$$가 증가하면 $$F^p A^\bullet$$이 작아지므로 $$F^p H^n$$도 작아진다.

이제 spectral sequence의 각 page를 구성한다. $$E_0$$ page는 filtration에 의한 associated graded로부터 직접 얻어진다.

$$E_0^{p,q} = \mathrm{Gr}^p A^{p+q} = F^p A^{p+q} / F^{p+1} A^{p+q}$$

여기서 미분 $$d_0$$는 $$A^\bullet$$의 미분 $$d$$가 $$\mathrm{Gr}^p A^\bullet$$에 유도한 것으로, bidegree $$(0,1)$$을 갖는다. $$E_1$$ page는 $$d_0$$에 대한 cohomology이다.

$$E_1^{p,q} = H^{p+q}(\mathrm{Gr}^p A^\bullet, d_0)$$

$$d_1:E_1^{p,q}\rightarrow E_1^{p+1,q}$$은 다음과 같이 정의된다. $$E_1^{p,q}$$의 원소 $$[a]$$를 대표하는 cocycle $$a \in F^p A^{p+q}$$를 선택하자. $$d(a) = 0$$이므로 특히 $$d(a) \in F^{p+1} A^{p+q+2}$$이다. 따라서 $$d(a)$$는 $$E_0^{p+1,q}$$에서 $$d_0$$에 대한 cocycle을 정의하며, 이것이 $$d_1([a])$$를 이룬다.

$$r \geq 2$$에 대해서도, 각 page에서 $$E_r$$은 이전 page의 cohomology로 정의되며([정의 1](#def1)), 미분 $$d_r$$의 bidegree는 $$(r, 1-r)$$이다. 이것이 filtered complex로부터 유도되는 spectral sequence의 전체 구성이다.

## 수렴

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Filtered complex $$(A^\bullet, F)$$로부터 유도된 spectral sequence $$\{E_r^{p,q}, d_r\}$$가 cohomology $$H^\bullet(A^\bullet)$$에 *수렴*한다는 것은, 각 $$(p,q)$$에 대해 충분히 큰 $$r$$에서 $$E_r^{p,q}$$가 안정화되어 $$E_\infty^{p,q}$$에 도달하며,

$$E_\infty^{p,q} \cong F^p H^{p+q} / F^{p+1} H^{p+q} = \mathrm{Gr}^p H^{p+q}(A^\bullet)$$

이 성립하는 것이다. 여기서 $$F^p H^n$$은 [정의 3](#def3)에서 정의된다. 기호로는 $$E_r^{p,q} \Rightarrow H^{p+q}(A^\bullet)$$로 쓴다.

</div>

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> First quadrant spectral sequence $$E_r^{p,q} \Rightarrow H^{p+q}(A^\bullet)$$에 대해, 충분히 큰 $$r$$에 대해

$$E_\infty^{p,q} \cong F^p H^{p+q} / F^{p+1} H^{p+q} = \mathrm{Gr}^p H^{p+q}(A^\bullet)$$

이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

First quadrant에서는 각 $$(p,q)$$에 대해 $$d_r$$가 출발/도착하는 $$r$$이 유한개이므로 $$E_r^{p,q}$$는 반드시 안정화된다.

$$r \geq 0$$에 대해

$$Z_r^{p,q} = \{a \in F^p A^{p+q} : d(a) \in F^{p+r} A^{p+q+1}\}, \quad B_r^{p,q} = d(F^{p-r} A^{p+q-1}) \cap F^p A^{p+q}$$

를 정의하자. $$Z_r^{p,q}$$는 "$$d$$에 의해 적어도 $$r$$칸 앞으로 보내지는" 원소들의 모임이며, $$B_r^{p,q}$$는 "$$r$$칸 뒤에서 온" boundary들의 모임이다. $$E_r^{p,q} = Z_r^{p,q} / (B_r^{p,q} + Z_{r-1}^{p+1,q-1})$$로 정의되며, $$Z_0^{p,q} = F^p A^{p+q}$$, $$B_0^{p,q} = F^{p+1} A^{p+q}$$이므로 $$E_0^{p,q} = \mathrm{Gr}^p A^{p+q}$$와 일치한다.

$$Z_\infty^{p,q} = \bigcap_{r} Z_r^{p,q}$$와 $$B_\infty^{p,q} = \bigcup_{r} B_r^{p,q}$$를 정의하자. First quadrant이므로, 충분히 큰 $$r$$에 대해 $$Z_r^{p,q}$$와 $$B_r^{p,q}$$가 안정화된다. $$Z_\infty^{p,q}$$는 $$d(a) = 0$$을 만족하는 $$a \in F^p A^{p+q}$$, 즉 $$F^p A^{p+q}$$에 속하는 cocycle들의 모임이며, $$B_\infty^{p,q}$$는 $$F^p A^{p+q}$$에 속하는 boundary들의 모임이다.

따라서 $$Z_\infty^{p,q} / B_\infty^{p,q}$$는 $$F^p A^{p+q}$$에서의 cocycle을 boundary로 나눈 것으로, $$F^p H^{p+q}(A^\bullet)$$에 의미론적으로 대응된다. 정확히는, 포함 $$F^p A^\bullet \hookrightarrow A^\bullet$$에 의해 유도된 사상

$$Z_\infty^{p,q} / B_\infty^{p,q} \to F^p H^{p+q}(A^\bullet)$$

는 well-defined surjection이다. Surjection임은 임의의 $$[x] \in F^p H^{p+q}$$가 $$x \in F^p A^{p+q}$$의 cocycle class에 의해 대표되기 때문이다.

Kernel을 확인하자. $$[z] \in Z_\infty^{p,q} / B_\infty^{p,q}$$가 $$F^p H^{p+q}$$에서 $$0$$으로 간다면, 어떤 $$y \in A^{p+q-1}$$에 대해 $$z = d(y)$$이다. $$z \in F^p A^{p+q}$$이므로, $$y$$를 선택할 때 $$y \in F^{p-1} A^{p+q-1}$$이라고 할 수 있다. $$d(y) = z \in F^p A^{p+q}$$이므로 $$y \in Z_1^{p-1,q}$$이고, 따라서 $$z \in B_1^{p,q} \subset B_\infty^{p,q}$$이다. 따라서

$$E_\infty^{p,q} = Z_\infty^{p,q} / B_\infty^{p,q} \cong F^p H^{p+q}(A^\bullet)$$

이다. 그러나 $$E_r^{p,q}$$의 정의에서 $$Z_{r-1}^{p+1,q-1}$$도 quotient에 포함되어 있으므로, 실제로는

$$E_\infty^{p,q} \cong F^p H^{p+q} / F^{p+1} H^{p+q} = \mathrm{Gr}^p H^{p+q}$$

을 얻는다. 구체적으로, $$E_r^{p,q}$$의 정의에 의해 $$E_\infty^{p,q} = Z_\infty^{p,q} / (B_\infty^{p,q} + Z_\infty^{p+1,q-1})$$이며, $$Z_\infty^{p+1,q-1}$$는 $$F^{p+1} H^{p+q}$$에 대응된다. $$Z_\infty^{p,q} / B_\infty^{p,q} \cong F^p H^{p+q}$$이므로, 추가로 $$Z_\infty^{p+1,q-1}$$에 의한 quotient를 취하면 $$F^p H^{p+q} / F^{p+1} H^{p+q} = \mathrm{Gr}^p H^{p+q}$$를 얻는다.

</details>

이 정리의 의미는 다음과 같다. Spectral sequence는 cohomology $$H^n(A^\bullet)$$ 자체를 직접 계산하는 것이 아니라, 그 filtration에 의한 associated graded를 계산한다. $$H^n(A^\bullet)$$이 filtration $$F^p H^n$$을 갖고 있을 때, $$\mathrm{Gr}^p H^n = F^p H^n / F^{p+1} H^n$$은 filtration의 각 단계에서 "새로 추가되는" 정보를 나타낸다. 만약 filtration이 trivial하다면, 즉 $$F^0 H^n = H^n$$이고 $$F^1 H^n = 0$$이면, $$E_\infty^{0,n} = H^n$$이고 나머지는 모두 $$0$$이므로 cohomology를 직접 얻는다. 일반적으로는 $$H^n \cong \bigoplus_p \mathrm{Gr}^p H^n$$이 성립하지 않을 수 있으므로, filtration의 구조를 추가로 분석해야 한다. 그러나 많은 응용에서 filtration이 enough projective나 similar condition에 의해 split되어 $$H^n \cong \bigoplus_p E_\infty^{p,n-p}$$를 얻는다.

---

**참고문헌**

**[GM]** S. I. Gelfand, Y. I. Manin, *Methods of homological algebra*, Springer, 2003.
**[Wei]** C. A. Weibel, *An introduction to homological algebra*, Cambridge University Press, 1994.
**[God]** R. Godement, *Topologie algébrique et théorie des faisceaux*, Hermann, 1958.