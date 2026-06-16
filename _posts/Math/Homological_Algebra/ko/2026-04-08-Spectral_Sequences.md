---
title: "스펙트럼 열"
description: "filtration이 주어진 복합체의 코호몰로지를 page별로 근사하는 스펙트럼 열의 공식적 정의를 소개하고, 감소 여과와 여과 복합체의 개념을 다룬다."
excerpt: "Filtered complex의 cohomology를 page 단위로 근사하는 spectral sequence"

categories: [Math / Homological Algebra]
permalink: /ko/math/homological_algebra/spectral_sequences
sidebar:
    nav: "homological_algebra-ko"

date: 2026-04-08
weight: 7

---

우리는 앞선 글에서 $$\Ext$$와 $$\Tor$$의 balancing을 증명하며, filtration과 이를 이용한 귀납법을 유용하게 사용하였다. 이는 이번 글에서 다룰 spectral sequence의 원시적인 형태라 생각할 수 있다. Spectral sequence는 filtration이 주어진 cochain complex의 cohomology를, 단계적으로 page를 거쳐 근사하는 체계적인 방법이다. 이러한 데이터를 공식적으로 정의하자.

## 스펙트럼 열

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> *Spectral sequence<sub>스펙트럼 열</sub>*는 다음과 같은 데이터의 모임이다.

1. Bigraded object $$E_r=(E_r^{p,q})_{p,q}$$,
2. $$E_r$$ 위의 bidegree $$(r,1-r)$$ differential $$d_r:E_r^{p,q}\rightarrow E_r^{p+r, q-r+1}$$ (즉, $$d_r^2=0$$)

각 $$r$$에 대하여, bigraded complex $$(E_r^{p,q}, d_r)$$을 *$$r$$번째 page*라고 부른다. 이 때 이들 두 데이터는 다음의 식

$$E_{r+1}^{p,q}\cong \frac{\ker(d_r^{p,q}: E_r^{p,q}\rightarrow E_r^{p+r,q-r+1})}{\im(d_r^{p-r,q+r-1}: E_r^{p-r, q+r-1}\rightarrow E_r^{p,q})}$$

을 통해 연결된다.

</div>

$$E_r$$ page의 원소들을 평면 상의 점 $$(p,q)$$로 시각화한다면, $$d_r^{p,q}$$는 점 $$(p,q)$$에서 $$(p+r, q-r+1)$$로 가는 것이며 이러한 점들이 cochain complex를 구성한다. 특히 $$E_{r+1}^{p,q}$$는 이러한 관점에서 $$(p,q)$$를 지나는 cochain complex의 $$(p,q)$$ 점에서의 cohomology로 생각할 수 있다.

우리의 경험을 바탕으로 spectral sequence를 어떠한 double complex의 total complex라 본다면, 이들 각각의 page들의 differential은 total complex에서의 differential, 즉

$$d^n:\bigoplus_{p+q=n}C^{p,q}\rightarrow \bigoplus_{p+q=n+1}C^{p+q}$$

의 각 성분을 세밀하게 분석하는 것처럼 생각할 수 있다. 우리는 이를 분석하여, 최종적으로는 이 total complex의 homology를 계산하는 것이 주된 목적이었는데, 이를 위해 우리는 앞서 [§Ext와 Tor, ⁋명제 3](/ko/math/homological_algebra/ext_and_tor#prop3)의 증명에서 total complex $$A^\bullet=\Tot(K)^\bullet$$의 horizontal/vertical degree를 이용하여 filtration을 정의했었다. 따라서 우리는 더 일반적으로 *filtered complex*의 개념을 도입해야 한다.

## 여과열

위에서 언급한 것과 같이, 다음의 [정의 2](#def2)는 이보다 아주 일반화된 버전이라 생각할 수 있지만, 어쨌든 complex를 더 세밀하게 쪼갠다는 철학 자체는 동일한 것으로 보아도 좋다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Cochain complex $$A^\bullet$$ 위의 *decreasing filtration<sub>감소 여과</sub>* $$F$$는 다음 조건

$$\cdots \supset F^{p-1}A^\bullet \supset F^pA^\bullet \supset F^{p+1}A^\bullet \supset \cdots$$

을 만족하는 subcomplex들의 열 $$(F^p A^\bullet)_p$$이다. 이 때, (decreasing) filtration이 주어진 cochain complex를 *filtered complex*라 부르고, $$(A^\bullet, F)$$로 표기한다.

</div>

특히 $$F^p A^\bullet$$이 $$A^\bullet$$의 subcomplex라는 가정으로부터 $$F^pA^\bullet$$은 $$A^\bullet$$으로부터 differential을 잘 물려받고 이에 대한 cohomology 또한 잘 정의된다. 어쨌든 직관적으로 $$p$$가 증가함에 따라 $$F^p A^\bullet$$은 점점 더 작아지며, 각 단계에서 새로운 정보가 추가되는 것으로 이해할 수 있다. 우리는 위의 [§Ext와 Tor, ⁋명제 3](/ko/math/homological_algebra/ext_and_tor#prop3)의 증명에서 귀납법을 적용하기 위해 $$F^{p+1}A^\bullet/F^pA^\bullet$$을 생각하여 이를 원래의 double complex $$K^{p, \bullet-p}$$로 생각하였는데, 일반적인 경우에도 이 정보는 <em-ko>정확히</em-ko> $$p$$번째 filtration을 담는다는 점에서 중요하다. 이렇게 얻어진 cochain complex

$$\gr^p A^\bullet = F^p A^\bullet / F^{p+1} A^\bullet$$

를 $$F$$에 대한 *associated graded complex*라 부른다. 이 때 이 complex의 differential은 물론 원래의 cochain complex $$A^\bullet$$에서의 differential로부터 오는 것이다.

Filtration에 대한 가장 중요한 것은 filtered complex $$A^\bullet$$가 주어졌을 때, filtration이 cohomology 레벨에서도 자연스럽게 정의된다는 것이다. 이 filtration을 사용하여 filtered complex로부터 유도된 spectral sequence의 수렴을 정의할 것이다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Filtered complex $$(A^\bullet, F)$$가 주어졌다 하자. 그럼 inclusion $$F^pA^\bullet\rightarrow A^\bullet$$의 cohomology 레벨에서의 image를

$$F^p H^n = \operatorname{im}\bigl(H^n(F^p A^\bullet) \to H^n(A^\bullet)\bigr)$$

로 정의한다.

</div>

이 filtration은 $$F^p A^\bullet$$에 포함된 cocycle들이 유도하는 cohomology class들로 이루어진다. $$p$$가 증가하면 $$F^p A^\bullet$$이 작아지므로 $$F^p H^n$$도 작아진다.

## 스펙트럼 열의 수렴

이제 우리는 spectral sequence의 convergence에 대해 설명한다. 직관적으로 spectral sequence의 각 page $$E_r^{p,q}$$는 $$r$$이 증가함에 따라 점진적으로 정제되는 대상이므로, 우리는 이 근사가 최종적으로 어떠한 것에 수렴하는지를 살펴보아야 한다. 따라서 우선 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Spectral sequence $$\{E_r^{p,q}, d_r\}$$가 *regular*하다는 것은, 각 $$(p,q)$$에 대해 충분히 큰 $$r$$에서 $$E_r^{p,q} = E_{r+1}^{p,q}$$이 성립하는 것이다. 이때 안정화된 값을 $$E_\infty^{p,q}$$로 정의한다.

</div>

Regularity는 spectral sequence의 page가 각 bidegree에서 더 이상 변하지 않는다는 의미이므로, 다음의 정의를 가능하게 해 준다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Spectral sequence $$\{E_r^{p,q}, d_r\}$$가 filtered graded object $$(H^n, F)$$에 *수렴*한다는 것은, 각 $$(p,q)$$에 대해

$$E_\infty^{p,q} \cong F^p H^{p+q} / F^{p+1} H^{p+q} = \gr^p H^{p+q}$$

이 성립하는 것이다. 기호로는 $$E_r^{p,q} \Rightarrow H^{p+q}$$로 쓴다.

</div>

역시 우리가 알고 있는 예시인 double complex의 total complex를 생각하면, 이는 double complex에서 수평방향 filtration을 걸어서 $$p$$를 $$0$$으로 보냈을 때, total complex의 homology가 나오던 것을 일반화한 것이라 생각할 수 있다.

만일 각 $$n$$에 대해 $$\bigcap_p F^p H^n = 0$$ (Hausdorff 조건), $$\bigcup_p F^p H^n = H^n$$ (exhaustive 조건), 그리고 spectral sequence가 regular하다면 각 $$\gr^p H^{p+q}$$의 정보를 모아서 $$H^n$$을 유일하게 재구성할 수 있다. 이 세 조건을 갖춘 경우 spectral sequence가 $$(H^n, F)$$에 *strongly converge*한다고 한다. 반면, 이 세 조건 중 하나라도 충족되지 않으면 *weakly converge*한다고 하며, 이 때에는 $$E_\infty^{p,q}$$만으로는 $$H^n$$을 유일하게 결정할 수 없다.

일반적으로 spectral sequence의 regularity는 항상 성립하는 것은 아니다. 그러나 만일 모든 $$r$$에 대하여, $$E_r^{p,q}$$들이 1사분면에만 존재한다면, 즉 오직 $$p,q\geq 0$$일 때만 $$E_r^{p,q}\neq 0$$일 수 있다면 $$d_r$$을 충분히 취했을 때 점이 2사분면 혹은 4사분면 방향으로 나가버려 $$0$$으로 가게 되므로 항상 regular하게 된다. 즉 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> First quadrant spectral sequence, 즉 $$p < 0$$ 또는 $$q < 0$$인 $$(p,q)$$에 대해 $$E_r^{p,q} = 0$$인 spectral sequence는 항상 regular하다. 또한, 이러한 spectral sequence가 $$E_r^{p,q} \Rightarrow H^{p+q}$$로 수렴할 때, 각 $$(p,q)$$에 대해 충분히 큰 $$r$$에서 $$E_r^{p,q} = E_\infty^{p,q}$$이 성립한다.

</div>

## 여과열과 스펙트럼 열

지금까지 우리는 double complex의 total complex를 생각하고, 여기에 연동된 spectral sequence를 생각하는 식으로 우리의 직관을 만족시켰지만 아직은 이 total complex가 정의하는 spectral sequence가 무엇인지 모른다는 점에서 그 연결고리가 다소 불명확하다. 이번 섹션에서 우리는 임의의 filtered complex로부터 spectral sequence를 구성하는 구체적인 방법을 설명한다. 특히 [§Ext와 Tor, ⁋명제 3](/ko/math/homological_algebra/ext_and_tor#prop3)에서, 양 변의 대상들은 각각 vertical 방향, horizontal 방향으로 걸어둔 filtration이 주는 spectral sequence에 해당하는 것이며, 이것이 같은 대상에 수렴한다는 것이 해당 증명의 기본적인 아이디어이다.

Filtered complex $$(A^\bullet, F)$$가 주어졌다 하자. 그럼 우리는 다음의 식

$$E_0^{p,q} = \gr^p A^{p+q} = F^p A^{p+q} / F^{p+1} A^{p+q}$$

을 통해 직접 $$E_0$$ page를 구성할 수 있다. 이제 이 위의 미분을 정확하게 정의하자. 우선 filtration이 differential을 보존하므로, 이로부터

$$F^p A^{p+q}\rightarrow F^p A^{p+q+1}$$

이 정의된다. 이를 편의상 $$F^p d$$라 적자. 그럼 원하는 미분은 $$F^p d$$에 quotient

$$F^pA^{p+q+1}\rightarrow F^pA^{p+q+1}/F^{p+1}A^{p+q+1}$$

를 합성한 후, first isomorphism theorem을 사용하여 이를

$$F^p A^{p+q}/F^{p+1}A^{p+q}\rightarrow F^pA^{p+q+1}/F^{p+1}A^{p+q+1}$$

로 factor through하여 얻어진다. 이 때, first isomorphism theorem이 잘 적용된다: $$a \in F^{p+1}A^{p+q}$$이면 $$d(a) \in F^{p+1}A^{p+q+1}$$이므로 공역 몫 $$F^p A^{p+q+1}/F^{p+1}A^{p+q+1}$$에서 $$0$$으로 간다.

더 일반적으로, $$E_r$$페이지에서의 미분 $$d_r$$ 또한 비슷한 방식으로 정의된다. 본질적으로 $$E_r^{p,q}$$는 $$F^pC^{p+q}$$에 여러 단계의 quotient를 취하여 만들어지는 것이므로, $$E_r^{p,q}$$의 원소는 어떠한 원소 $$x\in F^pC^{p+q}$$의 적당한 equivalence class $$[x]$$로 생각할 수 있다. 이제 $$d_r^{p,q}: E_r^{p,q}\rightarrow E_r^{p+r, q-r+1}$$은 다음의 식

$$d_r^{p,q}([x])=[dx]\in E_r^{p+r, q-r+1}\tag{$\ast$}$$

로 주어진다. 물론 이 대응이 잘 정의되며 differential을 정의하는 것은 다소 복잡한 계산을 통해 보여야 하지만 ([링크](https://stacks.math.columbia.edu/tag/012K)) 중요한 것은 $$E_r^{p,q}$$의 원소는 다음의 두 조건

- $$dx\in F^{p+r}C^{p+q+1}$$이며,
- 만일 $$x,y\in F^{p+r}C^{p+q}$$들이 $$r-1$$번째 단계의 boundary만큼만 차이난다면, $$x,y$$는 같은 것으로 취급한다.

에 의해 정의될 수 있다는 것이다. 특히 ($$\ast$$)가 알려주는 것은 $$d_r$$들이 모두 본질적으로는 $$d$$와 같은 것이며, 그 index $$r$$은 filtration을 건너뛰는 정도를 측정해주는 데에만 쓰인다는 것이다. 즉 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> Filtered complex $$(A^\bullet, F)$$로부터 위에서 구성한 $$E_r^{p,q}$$와 $$d_r$$은 [정의 1](#def1)의 spectral sequence 조건을 만족한다. 즉 

$$d_r \circ d_r = 0$$

이 성립하며, $$E_{r+1}^{p,q} \cong H(E_r, d_r)$$이다.

</div>

뿐만 아니라, 이렇게 정의된 spectral sequence는 일종의 functoriality 또한 갖는다. 

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> $$f : (A^\bullet, F) \to (B^\bullet, G)$$가 filtered complex 사이의 chain map이라 하자. 즉, 각 $$p$$에 대해 

$$f(F^p A^\bullet) \subset G^p B^\bullet$$

이 성립한다. 그럼 $$f$$는 각 $$r$$에 대해 well-defined된 사상 $$f_r : E_r(A) \to E_r(B)$$를 유도한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$f$$가 chain map이므로 cocycle을 cocycle으로, boundary를 boundary로 보낸다. 또한 $$f(F^p) \subset G^p$$이므로 $$f(Z_r^{p,q}(A)) \subset Z_r^{p,q}(B)$$이고 $$f(B_r^{p,q}(A)) \subset B_r^{p,q}(B)$$이다. 따라서 $$f$$는 각 $$r$$에 대해 $$E_r$$ 상에서 well-defined map을 유도한다.

</details>

그럼 우리의 핵심적인 결과는 이러한 spectral sequence가 실제로 원래의 complex의 cohomology에 도달한다는 것이다. 우선 다음을 정의하자.

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> Filtered complex $$(A^\bullet, F)$$이 *bounded*라는 것은 각각의 $$n$$마다 $$F^pA^n=0$$을 만족하는 충분히 큰 $$p$$와, $$F^pA^n=A^n$$을 만족하는 충분히 작은 $$p$$가 존재하는 것이다. 

</div>

즉 [정의 2](#def2)를 degree $$n$$으로 고정해두고 여기서의 filtration 

$$\cdots\supset F^{p-1}A^n\supset \cdots F^p A^n \supset \cdots F^{p+1}A^n\supset\cdots$$

을 시작했을 때, 이 filtration이 bounded되는 것을 의미한다. 그럼 각각의 $$(p,q)$$마다 $$F^nA^{p+q}=A^{p+q}$$이고 $$F^mA^{p+q}=0$$이도록 하는 $$(m, n)$$이 존재하므로, 고정된 $$(p,q)$$에 대하여, differential $$d_r$$이 이 구간을 나가버릴 정도로 $$r$$을 크게 잡으면 bounded filtered complex는 regular라는 것을 확인할 수 있다.

뿐만 아니라, 우리는 위에서 설명한 $$E_r^{p,q}$$의 원소들에 대한 설명으로부터

$$E_\infty^{p,q}\cong F^p H^{p+q}(A^\bullet)/F^{p+1}H^{p+q}(A^\bullet)$$

임을 보일 수 있고, 이로부터 다음의 결과를 얻는다. 

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> Bounded filtered complex $$(A^\bullet, F)$$가 주어졌다 하고, 이것이 정의하는 spectral sequence $$(E_r^{p,q})$$가 주어졌다 하자. 그럼 $$(E_r^{p,q})$$는 [정의 3](#def3)의 filtered graded object $$(H^\bullet, F)$$에 수렴한다. 즉 $$E_r^{p,q}\Rightarrow H^{p+q}(A^\bullet)$$이다. 

</div>

## 이중열의 스펙트럼 열

우리는 지금까지 $$\Ext$$와 $$\Tor$$의 balancing을 증명했던 [§Ext와 Tor, ⁋명제 3](/ko/math/homological_algebra/ext_and_tor#prop3)을 우리 이론의 motivation으로 삼았다. 우리는 이 글의 마지막을 double sequence로부터 정의되는 spectral sequence를 살펴보며 마무리한다. 

<div class="example" markdown="1">
    
<ins id="ex11">**예시 11**</ins> 임의의 double complex $$K^{p,q}$$의 total complex $$\Tot(K)^\bullet$$을 생각하자. 이 total complex에 두 가지 방식으로 filtration을 걸 수 있다. 

먼저 *vertical filtration*을

$$F^p_v \Tot(K)^n = \bigoplus_{j \geq p} K^{n-j, j}$$

로 정의하자. 이 filtration에 대한 associated graded object는 $$\mathrm{gr}^p_v \Tot(K)^{p+q} = K^{p,q}$$이므로, $$E_0$$ page는

$$E_0^{p,q} = K^{p,q}$$

이며, $$d_0$$은 degree $$(0,1)$$의 derivation이며 vertical differential $$d_v$$에 의해 주어진다. 따라서 $$E_1$$ page는

$$E_1^{p,q} = H^q_v(K^{p,\bullet})$$

이며, $$E_1$$ page의 $$d_1$$은 degree $$(1,0)$$의 derivation이며 horizontal differential $$d_h$$에 의해 유도된다. 한편, 이번에는 *horizontal filtration*을

$$F^p_h \Tot(K)^n = \bigoplus_{i \geq p} K^{i, n-i}$$

로 정의하면, 마찬가지로 $$E_0$$ page는

$$E_0^{p,q} = K^{p,q}$$

이며, $$d_0$$은 horizontal differential $$d_h$$에 의해 주어진다. 따라서 $$E_1$$ page는

$$E_1^{p,q} = H^p_h(K^{\bullet, q})$$

이며, $$d_1$$은 vertical differential $$d_v$$에 의해 유도된다. 

</div>

특별히 $$K^{p,q}$$가 first quadrant double complex라 하자. 그럼 두 filtration이 모두 bounded filtered complex를 정의하므로, [명제 10](#prop10)에 의해 각각의 spectral sequence는 $$H^\bullet(\Tot(K))$$에 수렴한다. 이로부터 우리는 [§Ext와 Tor, ⁋명제 3](/ko/math/homological_algebra/ext_and_tor#prop3)의 증명을 더 fancy한 언어로 다시 복원해낼 수 있다. 

---

**참고문헌**

**[GM]** S. I. Gelfand, Y. I. Manin, *Methods of homological algebra*, Springer, 2003.
**[Wei]** C. A. Weibel, *An introduction to homological algebra*, Cambridge University Press, 1994.
**[God]** R. Godement, *Topologie algébrique et théorie des faisceaux*, Hermann, 1958.