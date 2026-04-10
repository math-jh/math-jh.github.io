---
title: "스펙트럴 열"
excerpt: ""

categories: [Math / Homological Algebra]
permalink: /ko/math/homological_algebra/spectral_sequences
header:
    overlay_image: /assets/images/Math/Homological_Algebra/Spectral_Sequences.png
    overlay_filter: 0.5
sidebar: 
    nav: "homological_algebra-ko"

date: 2026-04-08
last_modified_at: 2026-04-08
weight: 7
published: false

---

## 동기

([§유도함자, ⁋정의 4](/ko/math/homological_algebra/derived_functors#def4))에서 우리는 exact하지 않은 functor에 대해 derived functor를 정의하고, short exact sequence로부터 long exact sequence를 유도하는 방법을 살펴보았다. Long exact sequence는 cohomology group 사이의 관계를 밝혀주는 강력한 도구이지만, 정보의 양에 본질적인 한계가 있다. Long exact sequence 하나에서 얻을 수 있는 정보는 본질적으로 "한 차원"에서 다음 차원으로의 연결뿐이며, 여러 차원에 걸쳐 동시에 전개되는 구조를 파악하기에는 부족하다.

예를 들어, double complex $$K^{p,q}$$에서 total complex $$\mathrm{Tot}(K)^n = \bigoplus_{p+q=n} K^{p,q}$$의 cohomology를 계산하고 싶은 상황을 생각하자. Double complex에는 두 개의 미분 $$d_h \colon K^{p,q} \to K^{p+1,q}$$과 $$d_v \colon K^{p,q} \to K^{p,q+1}$$이 존재하며, 이들은 서로 anti-commute한다. 이러한 상황에서 total complex의 cohomology는 행(row)과 열(column) 각각의 cohomology를 통해 근사할 수 있지만, long exact sequence 하나로는 이 근사를 정확하게 수행할 수 없다. 실제로 ([§Ext와 Tor, ⁋명제 3](/ko/math/homological_algebra/ext_and_tor#prop3))에서 이미 filtration을 사용하여 double complex의 cohomology를 계산한 바 있으며, 이는 spectral sequence의 원시적 형태에 해당한다.

Spectral sequence는 본질적으로 **여러 단계에 걸쳐 차례로 cohomology를 취하는 과정**이다. 각 단계에서 이전 단계의 cohomology를 계산하고, 새로운 미분을 도입하여 다음 단계로 넘어간다. 이 과정이 안정화되면, 최종적으로 우리가 원하는 cohomology group에 대한 정보를 얻는다.

## Filtered Complex

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Cochain complex $$A^\bullet$$ 위의 *decreasing filtration<sub>감소 여과</sub>* $$F$$는 다음 조건을 만족하는 subcomplex들의 열

$$\cdots \supset F^{p-1}A^\bullet \supset F^pA^\bullet \supset F^{p+1}A^\bullet \supset \cdots$$

이다. 즉 각 $$p$$에 대해 $$F^p A^\bullet$$은 $$A^\bullet$$의 subcomplex이며, $$d(F^p A^i) \subset F^p A^{i+1}$$이다. Filtered complex는 대상 $$(A^\bullet, F)$$로 표기한다.

</div>

Filtration은 complex를 점진적으로 세밀하게 쪼개는 구조를 제공한다. $$p$$가 증가함에 따라 $$F^p A^\bullet$$은 점점 더 작아지며, 각 단계에서 새로운 정보가 추가된다. 각 $$p$$에 대해 *associated graded*

$$\mathrm{Gr}^p A^\bullet = F^p A^\bullet / F^{p+1} A^\bullet$$

를 정의할 수 있다. $$\mathrm{Gr}^p A^\bullet$$은 $$F^p$$에서 "순수하게 $$p$$번째 단계에 해당하는" 부분을 추출한 것으로 이해할 수 있다. $$A^\bullet$$의 미분 $$d$$는 $$F^p A^\bullet$$을 $$F^p A^\bullet$$ 안으로 보내므로, quotient에서 미분

$$\bar{d}^p \colon \mathrm{Gr}^p A^i \to \mathrm{Gr}^p A^{i+1}$$

가 유도된다. 이 미분은 $$F^{p+1} A^\bullet$$로 보내는 성분을 무시한 것이며, $$\bar{d}^p \circ \bar{d}^p = 0$$이 성립하므로 $$\mathrm{Gr}^p A^\bullet$$은 자체적으로 cochain complex를 이룬다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> *Spectral sequence*는 각 $$r \geq 1$$에 대해 abelian group $$E_r^{p,q}$$와, bidegree $$(r, 1-r)$$를 갖는 사상

$$d_r \colon E_r^{p,q} \to E_r^{p+r, q-r+1}$$

로 이루어진다. 각 $$r$$에 대해 $$(E_r^{p,q}, d_r)$$을 *$$r$$번째 page*라고 부른다. 여기서 $$d_r \circ d_r = 0$$이며, 다음 단계는 $$E_{r+1}^{p,q} = H^{p+q}(E_r^{p-r,q+r-1} \overset{d_r}{\to} E_r^{p,q} \overset{d_r}{\to} E_r^{p+r,q-r+1})$$로 정의된다. Filtered complex $$(A^\bullet, F)$$로부터 유도된 spectral sequence가 cohomology $$H^\bullet(A^\bullet)$$에 *수렴한다*는 것은, 각 $$(p,q)$$에 대해 충분히 큰 $$r$$에 대해 $$E_r^{p,q}$$가 안정화되어 $$E_\infty^{p,q}$$에 도달하며, 이것이 $$H^{p+q}(A^\bullet)$$의 filtration에 의한 associated graded와 일치하는 것을 의미한다.

</div>

$$E_r$$ page의 원소들을 평면 상의 점 $$(p,q)$$로 시각화할 수 있다. $$d_r$$는 점 $$(p,q)$$에서 $$(p+r, q-r+1)$$로, 그리고 $$(-r, r-1)$$ 방향으로 향하는 미분이다. $$r$$이 커질수록 미분의 "거리"가 길어지며, 결국 충분히 먼 $$r$$에서는 더 이상 새로운 차이가 발생하지 않아 안정화된다.

## Double Complex와 Total Complex

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Abelian category $$\mathcal{A}$$ 위의 *double complex<sub>이중 복합체</sub>* $$K^{p,q}$$는 각 $$(p,q) \in \mathbb{Z}^2$$에 대상 $$K^{p,q}$$가 주어지고, 두 종류의 미분

$$d_h \colon K^{p,q} \to K^{p+1,q}, \qquad d_v \colon K^{p,q} \to K^{p,q+1}$$

이 존재하여 $$d_h^2 = 0$$, $$d_v^2 = 0$$, $$d_h d_v + d_v d_h = 0$$을 만족하는 것이다. *Total complex<sub>전체 복합체</sub>* $$\mathrm{Tot}(K)^\bullet$$은

$$\mathrm{Tot}(K)^n = \bigoplus_{p+q=n} K^{p,q}$$

로 정의되며, 미분 $$D = d_h + d_v$$를 갖는다. $$d_h d_v + d_v d_h = 0$$에 의해 $$D^2 = 0$$이다.

</div>

Double complex에서 total complex를 구성하는 것은, 두 방향의 정보를 하나의 복합체로 통합하는 표준적인 방법이다. 그러나 $$\mathrm{Tot}(K)^\bullet$$의 cohomology를 직접 계산하는 것은 일반적으로 어려우므로, filtration을 도입하여 점진적으로 근사한다.

Double complex $$K^{p,q}$$에서 두 가지 자연스러운 filtration을 정의할 수 있다. 첫째, *행 filtration*은

$$F^p_{\mathrm{row}} \mathrm{Tot}(K)^n = \bigoplus_{i \geq p, \, i+j=n} K^{i,j}$$

로 정의된다. 즉 $$p$$번째 열(column) 이후의 항들만 포함한다. 둘째, *열 filtration*은

$$F^p_{\mathrm{col}} \mathrm{Tot}(K)^n = \bigoplus_{j \geq p, \, i+j=n} K^{i,j}$$

로 정의된다. 이 두 filtration 각각에 대해 spectral sequence를 구성할 수 있으며, 두 spectral sequence는 모두 $$H^\bullet(\mathrm{Tot}(K)^\bullet)$$에 수렴한다. 행 filtration에 의한 spectral sequence는 먼저 각 열(column)의 cohomology를 계산한 뒤 행 방향으로 진행하고, 열 filtration에 의한 spectral sequence는 먼저 각 행(row)의 cohomology를 계산한 뒤 열 방향으로 진행한다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> Double complex $$K^{p,q}$$에서 행 filtration과 열 filtration에 의해 얻어지는 두 spectral sequence는 모두 $$H^\bullet(\mathrm{Tot}(K)^\bullet)$$에 수렴한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

행 filtration $$F_{\mathrm{row}}$$에 대해, associated graded는

$$\mathrm{Gr}^p_{\mathrm{row}} \mathrm{Tot}(K)^n = F^p_{\mathrm{row}} \mathrm{Tot}(K)^n / F^{p+1}_{\mathrm{row}} \mathrm{Tot}(K)^n \cong K^{p,n-p}$$

이다. 이에 유도되는 미분은 $$\bar{d} = d_v$$이므로, $$E_1$$ page에서

$$E_1^{p,q} = H^q(K^{p,\bullet}, d_v)$$

를 얻는다. 여기서 $$K^{p,\bullet}$$은 $$p$$번째 열의 cochain complex이다. $$d_1$$ 미분은 $$d_h$$에 의해 유도된다. 즉 $$d_h$$가 각 열의 cohomology class 사이에서 well-defined 사상을 유도함을 확인해야 한다. $$d_h d_v + d_v d_h = 0$$이므로, $$d_v$$-cocycle $$x \in K^{p,q}$$에 대해 $$d_h(x)$$는 $$d_v(d_h(x)) = -d_h(d_v(x)) = 0$$이므로 $$d_h$$-cocycle이다. 또한 $$x = d_v(y)$$이면 $$d_h(x) = d_h d_v(y) = -d_v d_h(y)$$이므로 $$d_v$$-boundary이다. 따라서 $$d_h$$는 cohomology 사이의 well-defined 사상을 유도한다. 뒤의 명제 9에서 증명할 것이지만, filtered complex로부터 유도된 spectral sequence는 cohomology에 수렴하며, 이에 의해 이 spectral sequence는 $$H^\bullet(\mathrm{Tot}(K)^\bullet)$$에 수렴한다. 열 filtration에 대해서도 대칭적인 논의가 적용된다.

</details>

## Filtered Complex의 Spectral Sequence

Filtered complex $$(A^\bullet, F)$$로부터 spectral sequence를 구성하는 구체적인 과정을 설명한다. 이것은 spectral sequence의 가장 기본적인 출발점이다.

먼저, filtration $$F$$에 의해 $$A^\bullet$$의 cohomology $$H^n(A^\bullet)$$에도 자연스러운 filtration이 유도된다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Filtered complex $$(A^\bullet, F)$$에 대해, $$H^n(A^\bullet)$$ 위의 filtration을

$$F^p H^n = \operatorname{im}\bigl(H^n(F^p A^\bullet) \to H^n(A^\bullet)\bigr)$$

로 정의한다. 여기서 사상은 포함 $$F^p A^\bullet \hookrightarrow A^\bullet$$에 의해 유도된다.

</div>

이 filtration은 $$F^p A^\bullet$$에 포함된 cocycle들이 유도하는 cohomology class들로 이루어진다. $$p$$가 증가하면 $$F^p A^\bullet$$이 작아지므로 $$F^p H^n$$도 작아진다.

이제 spectral sequence의 각 page를 구성한다. $$E_0$$ page는 associated graded로부터 직접 얻어진다.

$$E_0^{p,q} = \mathrm{Gr}^p A^{p+q} = F^p A^{p+q} / F^{p+1} A^{p+q}$$

여기서 미분 $$d_0$$는 $$A^\bullet$$의 미분 $$d$$가 $$\mathrm{Gr}^p A^\bullet$$에 유도한 것으로, bidegree $$(0,1)$$을 갖는다. $$E_1$$ page는 $$d_0$$에 대한 cohomology이다.

$$E_1^{p,q} = H^{p+q}(\mathrm{Gr}^p A^\bullet, d_0)$$

$$d_1 \colon E_1^{p,q} \to E_1^{p+1,q}$$은 다음과 같이 정의된다. $$E_1^{p,q}$$의 원소 $$[a]$$를 대표하는 cocycle $$a \in F^p A^{p+q}$$를 선택하자. $$d(a) = 0$$이므로 특히 $$d(a) \in F^{p+1} A^{p+q+2}$$이다. 따라서 $$d(a)$$는 $$E_0^{p+1,q}$$에서 $$d_0$$에 대한 cocycle을 정의하며, 이것이 $$d_1([a])$$를 이룬다.

더 일반적으로, $$E_r$$ page를 구성하기 위해 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> $$r \geq 0$$에 대해, $$Z_r^{p,q}$$와 $$B_r^{p,q}$$를

$$Z_r^{p,q} = \{a \in F^p A^{p+q} : d(a) \in F^{p+r} A^{p+q+1}\},$$

$$B_r^{p,q} = d(F^{p-r} A^{p+q-1}) \cap F^p A^{p+q}$$

로 정의한다. 그리고

$$E_r^{p,q} = Z_r^{p,q} / \bigl(B_r^{p,q} + Z_{r-1}^{p+1,q-1}\bigr)$$

를 $$r \geq 1$$에 대해 정의한다. 여기서 $$Z_0^{p,q} = F^p A^{p+q}$$이고 $$B_0^{p,q} = F^{p+1} A^{p+q}$$이므로 $$E_0^{p,q} = \mathrm{Gr}^p A^{p+q}$$이다.

</div>

$$Z_r^{p,q}$$는 "$$d$$에 의해 적어도 $$r$$칸 앞으로 보내지는" 원소들의 모임이며, $$B_r^{p,q}$$는 "$$r$$칸 뒤에서 온" boundary들의 모임이다. $$r$$이 커질수록 $$Z_r$$은 작아지고 $$B_r$$은 커지며, $$E_r^{p,q}$$는 점점 더 정제된 cohomology 정보를 담게 된다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> $$d_r \circ d_r = 0$$이며, $$E_{r+1}^{p,q} \cong H(\cdots \xrightarrow{d_r} E_r^{p-r,q+r-1} \xrightarrow{d_r} E_r^{p,q} \xrightarrow{d_r} E_r^{p+r,q-r+1} \xrightarrow{d_r} \cdots)$$이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$d_r$$를 구성한다. $$[a] \in E_r^{p,q}$$를 대표하는 $$a \in Z_r^{p,q}$$를 선택하자. $$d(a) \in F^{p+r} A^{p+q+1}$$이므로 $$d(a) \in Z_r^{p+r, q-r+1}$$이다. $$d(a)$$의 $$E_r^{p+r,q-r+1}$$에서의 class를 $$d_r([a])$$로 정의한다. 이것이 well-defined임을 확인하자.

$$a' = a + b + z$$ (여기서 $$b \in B_r^{p,q}$$, $$z \in Z_{r-1}^{p+1,q-1}$$)라 하자. $$d(a') = d(a) + d(b) + d(z)$$이다. $$b \in d(F^{p-r} A^{p+q-1})$$이므로 $$c \in F^{p-r} A^{p+q-1}$$가 존재하여 $$b = d(c)$$이고, $$d(b) = 0$$이다. 또한 $$z \in Z_{r-1}^{p+1,q-1}$$이므로 $$d(z) \in F^{p+r} A^{p+q+1}$$이며, $$d(a')$$와 $$d(a)$$의 차이는 $$d(z) \in Z_{r-1}^{p+r,q-r+1}$$에 있으므로 $$E_r^{p+r,q-r+1}$$에서 동일한 class를 정의한다.

$$d_r \circ d_r = 0$$은 $$d^2 = 0$$에 의해 자명하다. $$E_{r+1}^{p,q}$$의 정의를 확인하면,

$$Z_{r+1}^{p,q} = \{a \in Z_r^{p,q} : d(a) \in B_r^{p+r,q-r+1} + Z_{r-1}^{p+r+1,q-r}\}$$

이며, 이것은 $$E_r$$ page에서 $$d_r$$의 kernel과 일치한다. 마찬가지로 $$E_{r+1}^{p,q}$$에서 quotient하는 것은 $$d_r$$의 image와 일치한다. 따라서 $$E_{r+1}^{p,q} \cong H(E_r, d_r)$$이다.

</details>

## 수렴

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> Spectral sequence $$\{E_r^{p,q}, d_r\}$$가 *regular*라는 것은 각 $$(p,q)$$에 대해 충분히 큰 $$r$$에 대해 $$E_r^{p,q} = E_{r+1}^{p,q}$$이 성립하는 것이다. 이때 충분히 큰 $$r$$에 대해 안정화된 값 $$E_r^{p,q} = E_{r+1}^{p,q}$$를 $$E_\infty^{p,q}$$로 정의한다. Spectral sequence가 *first quadrant*에 있다는 것은 $$E_r^{p,q} = 0$$ for $$p < 0$$ or $$q < 0$$인 것이다.

</div>

First quadrant spectral sequence에서는 각 $$(p,q)$$에 대해 $$d_r$$가 $$E_r^{p,q}$$에서 출발하거나 도착하는 것은 유한 개의 $$r$$뿐이므로 반드시 regular하다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> First quadrant spectral sequence $$E_r^{p,q} \Rightarrow H^{p+q}(A^\bullet)$$에 대해, 충분히 큰 $$r$$에 대해

$$E_\infty^{p,q} \cong F^p H^{p+q} / F^{p+1} H^{p+q} = \mathrm{Gr}^p H^{p+q}(A^\bullet)$$

이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

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