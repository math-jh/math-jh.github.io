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

Spectral sequence의 각 page는 점진적으로 정제되는 근사이다. 이 근사가 최종적으로 어떤 graded object의 filtration에 의한 associated graded와 일치하는지를 규명하는 것이 바로 수렴의 문제이다. 이에 대해서는 뒤에서 자세히 다룬다.

## 여과열

우리의 경험을 바탕으로 spectral sequence를 어떠한 double complex의 total complex라 본다면, 이들 각각의 page들의 differential은 total complex에서의 differential, 즉

$$d^n:\bigoplus_{p+q=n}C^{p,q}\rightarrow \bigoplus_{p+q=n+1}C^{p+q}$$

의 각 성분을 세밀하게 분석하는 것처럼 생각할 수 있다. 우리는 이를 분석하여, 최종적으로는 이 total complex의 homology를 계산하는 것이 주된 목적이었는데, 이를 위해 우리는 앞서 [§Ext와 Tor, ⁋명제 3](/ko/math/homological_algebra/ext_and_tor#prop3)의 증명에서 total complex $$A^\bullet=\Tot(K)^\bullet$$의 horizontal/vertical degree를 이용하여 filtration을 정의했었다. 다음의 [정의 2](#def2)는 이보다 아주 일반화된 버전이라 생각할 수 있지만, 어쨌든 complex를 더 세밀하게 쪼갠다는 철학 자체는 동일한 것으로 보아도 좋다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Cochain complex $$A^\bullet$$ 위의 *decreasing filtration<sub>감소 여과</sub>* $$F$$는 다음 조건

$$\cdots \supset F^{p-1}A^\bullet \supset F^pA^\bullet \supset F^{p+1}A^\bullet \supset \cdots$$

을 만족하는 subcomplex들의 열 $$(F^p A^\bullet)_p$$이다. 이 때, (decreasing) filtration이 주어진 cochain complex를 *filtered complex*라 부르고, $$(A^\bullet, F)$$로 표기한다.

</div>

특히 $$F^p A^\bullet$$이 $$A^\bullet$$의 subcomplex라는 가정으로부터 $$F^pA^\bullet$$은 $$A^\bullet$$으로부터 differential을 잘 물려받고 이에 대한 cohomology 또한 잘 정의된다. 이에 대한 내용은 [정의 3](#def3)에서 다룬다. 

어쨌든 직관적으로 $$p$$가 증가함에 따라 $$F^p A^\bullet$$은 점점 더 작아지며, 각 단계에서 새로운 정보가 추가되는 것으로 이해할 수 있다. 우리는 위의 [§Ext와 Tor, ⁋명제 3](/ko/math/homological_algebra/ext_and_tor#prop3)의 증명에서 귀납법을 적용하기 위해 $$F^{p+1}A^\bullet/F^pA^\bullet$$을 생각하여 이를 원래의 double complex $$K^{p, \bullet-p}$$로 생각하였는데, 일반적인 경우에도 이 정보는 <em-ko>정확히</em-ko> $$p$$번째 filtration을 담는다는 점에서 중요하다. 이렇게 얻어진 cochain complex

$$\mathrm{Gr}^p A^\bullet = F^p A^\bullet / F^{p+1} A^\bullet$$

를 $$F$$에 대한 *associated graded complex*라 부른다. 이 때 이 complex의 differential은 물론 원래의 cochain complex $$A^\bullet$$에서의 differential로부터 오는 것이다. 

Filtration에 대한 가장 중요한 것은 filtered complex $$A^\bullet$$가 주어졌을 때, filtration이 cohomology 레벨에서도 자연스럽게 정의된다는 것이다. 이 filtration을 사용하여 filtered complex로부터 유도된 spectral sequence의 수렴을 정의할 것이다. 

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Filtered complex $$(A^\bullet, F)$$가 주어졌다 하자. 그럼 inclusion $$F^pA^\bullet\rightarrow A^\bullet$$의 cohomology 레벨에서의 image를

$$F^p H^n = \operatorname{im}\bigl(H^n(F^p A^\bullet) \to H^n(A^\bullet)\bigr)$$

로 정의한다. 

</div>

이 filtration은 $$F^p A^\bullet$$에 포함된 cocycle들이 유도하는 cohomology class들로 이루어진다. $$p$$가 증가하면 $$F^p A^\bullet$$이 작아지므로 $$F^p H^n$$도 작아진다.

## 스펙트럼 열의 수렴

Spectral sequence의 각 page $$E_r^{p,q}$$는 $$r$$이 증가함에 따라 점진적으로 정제되는 근사치이다. 이 근사가 최종적으로 수렴하는지, 그리고 그 수렴값이 어떤 graded object를 근사하는지를 엄밀히 정의한다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Spectral sequence $$\{E_r^{p,q}, d_r\}$$가 *regular*하다는 것은, 각 $$(p,q)$$에 대해 충분히 큰 $$r$$에서 $$E_r^{p,q} = E_{r+1}^{p,q}$$이 성립하는 것이다. 이때 안정화된 값을 $$E_\infty^{p,q}$$로 정의한다.

</div>

Regularity는 spectral sequence의 page가 각 bidegree에서 더 이상 변하지 않음을 보장하므로, 수렴을 논하기 위한 기본 전제가 된다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Spectral sequence $$\{E_r^{p,q}, d_r\}$$가 filtered graded object $$(H^n, F)$$에 *수렴*한다는 것은, 각 $$(p,q)$$에 대해

$$E_\infty^{p,q} \cong F^p H^{p+q} / F^{p+1} H^{p+q} = \mathrm{Gr}^p H^{p+q}$$

이 성립하는 것이다. 기호로는 $$E_r^{p,q} \Rightarrow H^{p+q}$$로 쓴다.

수렴에는 다음과 같은 강도의 구분이 있다. Spectral sequence가 $$(H^n, F)$$에 *strongly convergent*하다는 것은, 각 $$n$$에 대해 filtration $$F^p H^n$$이 Hausdorff 조건 $$\bigcap_p F^p H^n = 0$$을 만족하고 $$H^n = \bigcup_p F^p H^n$$이 성립하는 것이다. 이 조건 하에서 filtration은 $$E_\infty$$의 associated graded를 통해 $$H^n$$을 유일하게 결정한다. 반면, *weakly convergent*하다는 것은 $$E_\infty^{p,q} \cong \mathrm{Gr}^p H^{p+q}$$만이 성립하며, 위의 completeness 조건이 반드시 충족되지 않을 수 있는 경우를 말한다.

</div>

Strong convergence에서는 filtration이 $$H^n$$의 구조를 완전히 회복할 수 있지만, weak convergence에서는 associated graded만 알 수 있으므로 extension problem이 남는다. 

한편, unbounded filtration의 경우에는 *conditional convergence*의 개념이 필요하다. Boardman는 spectral sequence가 filtered object에 conditionally convergent하다는 것을, filtration에 대한 completion과 spectral sequence의 $$E_\infty$$ page 사이의 적절한 대응으로 정의하였다. 이 경우 completeness 조건이 성립하지 않을 수 있으므로, 수렴값이 원래의 $$H^n$$이 아닌 그 completion에 해당할 수 있다. 이에 대한 자세한 논의는 Boardman의 원론을 참고한다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> First quadrant spectral sequence, 즉 $$p < 0$$ 또는 $$q < 0$$인 $$(p,q)$$에 대해 $$E_r^{p,q} = 0$$인 spectral sequence는 항상 regular하다. 또한, 이러한 spectral sequence가 $$E_r^{p,q} \Rightarrow H^{p+q}$$로 수렴할 때, 각 $$(p,q)$$에 대해 충분히 큰 $$r$$에서 $$E_r^{p,q} = E_\infty^{p,q}$$이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

First quadrant에서는 각 $$(p,q)$$에 대해 $$d_r$$가 출발하거나 도착하는 $$r$$이 유한개이다. 구체적으로, $$d_r$$가 $$(p,q)$$에서 도착하려면 $$p-r \geq 0$$이어야 하므로 $$r \leq p$$이며, $$(p,q)$$에서 출발하려면 $$q-r+1 \geq 0$$이어야 하므로 $$r \leq q+1$$이다. 따라서 $$r > \max(p, q+1)$$에 대해 $$d_r$$는 $$(p,q)$$에 trivial하게 작용하며 $$E_r^{p,q}$$는 안정화된다. 이로부터 regularity와 $$E_r^{p,q} = E_\infty^{p,q}$$를 얻는다.

</details>

## 여과열과 스펙트럼 열

Filtered complex $$(A^\bullet, F)$$로부터 spectral sequence를 구성하는 구체적인 과정을 설명한다. [정의 2](#def2)의 filtration과 [정의 3](#def3)의 cohomology 위의 filtration을 사용하여, spectral sequence의 각 page를 단계적으로 구성한다.

이제 spectral sequence의 각 page를 구성한다. $$E_0$$ page는 filtration에 의한 associated graded로부터 직접 얻어진다.

$$E_0^{p,q} = \mathrm{Gr}^p A^{p+q} = F^p A^{p+q} / F^{p+1} A^{p+q}$$

여기서 미분 $$d_0$$는 $$A^\bullet$$의 미분 $$d$$가 $$\mathrm{Gr}^p A^\bullet$$에 유도한 것으로, bidegree $$(0,1)$$을 갖는다. $$E_1$$ page는 $$d_0$$에 대한 cohomology이다.

$$E_1^{p,q} = H^{p+q}(\mathrm{Gr}^p A^\bullet, d_0)$$

이것은 [정의 3](#def3)의 cohomology 위의 filtration의 $$p$$번째 단계와 직접적으로 관련된다.

$$d_1:E_1^{p,q}\rightarrow E_1^{p+1,q}$$은 다음과 같이 정의된다. $$E_1^{p,q}$$의 원소 $$[a]$$를 대표하는 cocycle $$a \in F^p A^{p+q}$$를 선택하자. $$d(a) = 0$$이므로 특히 $$d(a) \in F^{p+1} A^{p+q+2}$$이다. 따라서 $$d(a)$$는 $$E_0^{p+1,q}$$에서 $$d_0$$에 대한 cocycle을 정의하며, 이것이 $$d_1([a])$$를 이룬다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> Filtered complex $$(A^\bullet, F)$$로부터 위에서 구성한 $$E_r^{p,q}$$와 $$d_r$$은 [정의 1](#def1)의 spectral sequence 조건을 만족한다. 즉 $$d_r \circ d_r = 0$$이며 $$E_{r+1}^{p,q} \cong H(E_r, d_r)$$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$r \geq 0$$에 대해

$$Z_r^{p,q} = \{a \in F^p A^{p+q} : d(a) \in F^{p+r} A^{p+q+1}\}, \quad B_r^{p,q} = d(F^{p-r} A^{p+q-1}) \cap F^p A^{p+q}$$

를 정의하자. $$E_r^{p,q} = Z_r^{p,q} / (B_r^{p,q} + Z_{r-1}^{p+1,q-1})$$로 정의되며, $$Z_0 = F^p$$, $$B_0 = F^{p+1}$$이므로 $$E_0^{p,q} = \mathrm{Gr}^p A^{p+q}$$와 일치한다.

$$d_r$$을 다음과 같이 정의한다. $$[a] \in E_r^{p,q}$$를 대표하는 $$a \in Z_r^{p,q}$$를 선택하자. $$d(a) \in F^{p+r} A^{p+q+1}$$이므로 $$d(a) \in Z_r^{p+r, q-r+1}$$이다. $$d(a)$$의 $$E_r^{p+r, q-r+1}$$에서의 class를 $$d_r([a])$$로 정의한다.

$$d_r \circ d_r = 0$$은 $$d^2 = 0$$에 의해 자명하다. $$E_r$$에서 $$d_r$$의 kernel은 $$Z_{r+1}^{p,q} / (B_r^{p,q} + Z_{r-1}^{p+1,q-1})$$이다. $$d_r$$의 image를 확인하자. $$[a] \in E_r^{p-r,q+r-1}$$에 대해 $$d_r([a]) = [d(a)]$$이며, $$d(a) \in F^p A^{p+q}$$이고 $$d(a) = d(a') \in d(F^{p-r} A^{p+q-1}) = B_{r+1}^{p,q}$$이므로 image는 $$(B_{r+1}^{p,q} + Z_r^{p+1,q-1}) / (B_r^{p,q} + Z_{r-1}^{p+1,q-1})$$에 해당한다. 따라서 $$E_{r+1}^{p,q} \cong H(E_r, d_r)$$을 얻는다.

</details>

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> $$f \colon (A^\bullet, F) \to (B^\bullet, G)$$가 filtered complex 사이의 chain map, 즉 각 $$p$$에 대해 $$f(F^p A^\bullet) \subset G^p B^\bullet$$을 만족하는 chain map이면, $$f$$는 각 $$r$$에 대해 well-defined된 사상 $$f_r \colon E_r(A) \to E_r(B)$$를 유도한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$f$$가 chain map이므로 cocycle을 cocycle으로, boundary를 boundary로 보낸다. 또한 $$f(F^p) \subset G^p$$이므로 $$f(Z_r^{p,q}(A)) \subset Z_r^{p,q}(B)$$이고 $$f(B_r^{p,q}(A)) \subset B_r^{p,q}(B)$$이다. 따라서 $$f$$는 각 $$r$$에 대해 $$E_r$$ 상에서 well-defined된 사상을 유도한다.

</details>

이제 위에서 구성한 spectral sequence가 실제로 cohomology에 도달하는지를 확인하자.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> Filtered complex $$(A^\bullet, F)$$로부터 [명제 7](#prop7)에 의해 유도된 spectral sequence $$\{E_r^{p,q}\}$$는 cohomology $$H^\bullet(A^\bullet)$$ 위의 filtration $$F^p H^n$$ ([정의 3](#def3))에 수렴한다. 즉 [정의 5](#def5)의 의미에서 $$E_r^{p,q} \Rightarrow H^{p+q}(A^\bullet)$$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 spectral sequence가 regular함을 확인한다. [명제 6](#prop6)에 의해 first quadrant spectral sequence는 항상 regular하며 $$E_\infty^{p,q}$$가 well-defined된다. 일반적인 filtered complex의 경우에도, 각 $$(p,q)$$에 대해 $$d_r$$가 출발하거나 도착하는 $$r$$이 유한하다면 동일하게 regularity를 얻는다.

$$Z_r^{p,q}$$, $$B_r^{p,q}$$는 [명제 7](#prop7)의 증명에서 정의한 것과 같다.

$$Z_\infty^{p,q} = \bigcap_{r} Z_r^{p,q}$$와 $$B_\infty^{p,q} = \bigcup_{r} B_r^{p,q}$$를 정의하자. 충분히 큰 $$r$$에 대해 $$Z_r^{p,q}$$와 $$B_r^{p,q}$$가 안정화된다고 가정하자. $$Z_\infty^{p,q}$$는 $$d(a) = 0$$을 만족하는 $$a \in F^p A^{p+q}$$, 즉 $$F^p A^{p+q}$$에 속하는 cocycle들의 모임이며, $$B_\infty^{p,q}$$는 $$F^p A^{p+q}$$에 속하는 boundary들의 모임이다.

따라서 $$Z_\infty^{p,q} / B_\infty^{p,q}$$는 $$F^p A^{p+q}$$에서의 cocycle을 boundary로 나눈 것으로, $$F^p H^{p+q}(A^\bullet)$$에 의미론적으로 대응된다. 정확히는, 포함 $$F^p A^\bullet \hookrightarrow A^\bullet$$에 의해 유도된 사상

$$Z_\infty^{p,q} / B_\infty^{p,q} \to F^p H^{p+q}(A^\bullet)$$

는 well-defined surjection이다. Surjection임은 임의의 $$[x] \in F^p H^{p+q}$$가 $$x \in F^p A^{p+q}$$의 cocycle class에 의해 대표되기 때문이다.

마찬가지로, 포함 $$F^{p+1} A^\bullet \hookrightarrow A^\bullet$$에 의해

$$Z_\infty^{p+1,q-1} / B_\infty^{p+1,q-1} \to F^{p+1} H^{p+q}(A^\bullet)$$

도 well-defined surjection을 유도한다. $$Z_\infty^{p,q} / B_\infty^{p,q} \to F^p H^{p+q}$$의 kernel은, cocycle $$z \in Z_\infty^{p,q}$$가 $$A^\bullet$$에서 boundary인 경우, 즉 $$z = d(y)$$인 $$y \in A^{p+q-1}$$가 존재하는 경우이다. 이때 $$z \in F^p A^{p+q}$$이므로 $$y \in F^{p-1} A^{p+q-1}$$으로 잡을 수 있고, $$d(y) = z \in F^p A^{p+q}$$에 의해 $$y \in Z_1^{p-1,q}$$이 되어 $$z \in B_1^{p,q}$$이고, 귀납적으로 $$z \in Z_\infty^{p+1,q-1}$$에 의해 대표됨을 확인할 수 있다.

따라서 $$Z_\infty^{p,q} / B_\infty^{p,q} \to F^p H^{p+q}$$와 $$Z_\infty^{p+1,q-1} / B_\infty^{p+1,q-1} \to F^{p+1} H^{p+q}$$는 각각 surjection이며, 전자의 kernel은 $$Z_\infty^{p+1,q-1} / B_\infty^{p+1,q-1}$$에 포함된다. 이로부터

$$E_\infty^{p,q} = \frac{Z_\infty^{p,q}}{B_\infty^{p,q} + Z_\infty^{p+1,q-1}} \cong \frac{F^p H^{p+q}}{F^{p+1} H^{p+q}} = \mathrm{Gr}^p H^{p+q}$$

를 얻는다.

</details>

## 예시: Ext와 Tor의 balancedness

이제 앞서 정의한 도구들을 이용하여, [§Ext와 Tor, ⁋명제 3](/ko/math/homological_algebra/ext_and_tor#prop3)에서 이미 수행했던 계산을 spectral sequence의 언어로 다시 살펴보자.

[§Ext와 Tor, ⁋명제 3](/ko/math/homological_algebra/ext_and_tor#prop3)에서 우리는 $$K^{p,q} = \Hom_A(P_q, I^p)$$로 주어지는 double complex ([§호몰로지, ⁋정의 4](/ko/math/homological_algebra/homology#def4))의 total complex $$\Tot(K)^\bullet$$을 다루었다. 여기서 $$P_\bullet \to M$$은 projective resolution이고 $$N \to I^\bullet$$은 injective resolution이다.

명제 3의 증명에서 우리는 $$\Tot(K)^\bullet$$ 위에

$$F^p \Tot(K)^k = \bigoplus_{i \geq p, \, i+q=k} K^{i,q}$$

라는 filtration을 사용했다. 이것은 [정의 2](#def2)의 decreasing filtration의 구체적인 예시이다: $$p$$가 커질수록 $$F^p$$는 더 적은 성분만을 포함하며, $$F^{p+1} \Tot(K)^\bullet \subset F^p \Tot(K)^\bullet$$이 성립한다.

[정의 1](#def1)에 의해 이 filtration으로부터 spectral sequence가 유도된다. $$E_0$$ page는 associated graded이며, $$E_0^{p,q} = \mathrm{Gr}^p \Tot(K)^{p+q} = K^{p,q}$$이다. $$d_0$$는 double complex의 vertical differential $$d_v$$에 해당하므로

$$E_1^{p,q} = H^q(K^{p,\bullet}, d_v)$$

이다. $$P_\bullet \to M$$이 resolution이므로 $$I^p$$가 injective인 점을 이용하면 $$E_1^{p,0} = \Hom_A(M, I^p)$$이고 $$q \neq 0$$에서는 $$E_1^{p,q} = 0$$임을 얻는다. $$I^p$$가 injective이므로 $$\Hom_A(-, I^p)$$는 exact functor이고, 따라서 $$P_\bullet$$의 exactness로부터 $$q \neq 0$$에서 $$H^q = 0$$임을 얻는다. 즉, **$$E_1$$ page는 이미 vertical 방향으로는 계산이 끝난 상태**다.

이제 $$E_1$$에서 $$E_2$$로의 page 전이를 살펴보자. $$E_1^{p,q} = \Hom_A(M, I^p)$$이며, $$d_1$$은 double complex의 horizontal differential $$d_h$$에 의해 유도된 사상이다. 즉 $$I^p \to I^{p+1}$$로부터 얻어지는 $$\Hom_A(M, I^p) \to \Hom_A(M, I^{p+1})$$이므로, 각 고정된 $$q$$에 대해 $$E_1^{\bullet, q}$$는 $$\Hom_A(M, I^\bullet)$$ 복합체를 이룬다. 따라서

$$E_2^{p,q} = H^q(\Hom_A(M, I^\bullet)) = \Ext^q_A(M, N)$$

이다. 여기서 중요한 점은, [§Ext와 Tor, ⁋명제 3](/ko/math/homological_algebra/ext_and_tor#prop3)의 증명에서 귀납법으로 계산한 것이 바로 이 $$E_1 \to E_2$$ page 전이에 해당한다는 것이다. 이 경우 $$d_1$$ 이후의 미분 $$d_r$$ ($$r \geq 2$$)은 모두 trivial하므로 $$E_2 = E_\infty$$이다.

[정의 5](#def5)에 의해 $$E_\infty^{p,q} = \mathrm{Gr}^p H^{p+q}(\Tot(K)^\bullet)$$이다. 그러나 명제 3의 증명에서 확인했듯, 각 $$n$$에 대해 $$p > n$$이면 $$H^n(F^p) \cong H^n(F^{p+1})$$이고 $$p < 0$$이면 $$F^p H^n = H^n$$이므로, 사실상 filtration은 split된다. 따라서

$$H^n(\Tot(K)^\bullet) \cong \bigoplus_p E_\infty^{p, n-p} = \Ext^n_A(M, N)$$

를 얻는다.

이것은 spectral sequence가 단 한 번의 page 전이($$E_1 \to E_2$$)에서 안정화되는 매우 단순한 예시이다. 더 일반적인 상황에서는 여러 번의 page 전이가 필요하며, 이것이 spectral sequence의 진정한 힘이 발휘되는 곳이다.

---

**참고문헌**

**[GM]** S. I. Gelfand, Y. I. Manin, *Methods of homological algebra*, Springer, 2003.
**[Wei]** C. A. Weibel, *An introduction to homological algebra*, Cambridge University Press, 1994.
**[God]** R. Godement, *Topologie algébrique et théorie des faisceaux*, Hermann, 1958.
**[Boa]** C. B. Boardman, *Conditionally convergent spectral sequences*, University of Rochester, preprint, 1981.
