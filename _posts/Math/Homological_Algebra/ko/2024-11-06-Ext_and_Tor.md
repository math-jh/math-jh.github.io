---

title: "Ext와 Tor"
excerpt: ""

categories: [Math / Homological Algebra]
permalink: /ko/math/homological_algebra/ext_and_tor
header:
    overlay_image: /assets/images/Math/Homological_Algebra/Ext_and_Tor.png
    overlay_filter: 0.5
sidebar:
    nav: "homological_algebra-ko"

date: 2024-11-06
last_modified_at: 2026-04-09
weight: 6

---

앞선 글에서 우리는 일반적인 left/right exact functor에 대한 right/left derived functor를 정의했다. 이번 글에서 우리는 특별히 $$\lMod{A}$$에서 정의된 left exact functor $$\Hom$$, right exact functor $$\otimes$$의 derived functor에 대해 살펴본다.

## Ext 함자의 정의

임의의 $$M\in\lMod{A}$$에 대하여, $$\Hom_\lMod{A}(M,-)$$은 $$\lMod{A}$$에서 $$\Ab$$로의 left exact functor이다. 따라서 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Left exact functor $$\Hom_\lMod{A}(M,-):\lMod{A} \rightarrow \Ab$$의 right derived functor를

$$\Ext_A^i(M,N)=R^i\Hom_\lMod{A}(M,-)(N)$$

으로 정의하고, 이들을 *$$\Ext$$ group*들이라 부른다.

</div>

$$\Hom_\lMod{A}(-,N)$$가 exact functor인 것이 $$N$$가 injective object인 것과 동치이다. ([\[다중선형대수학\] §사영가군, 단사가군, 평탄가군, ⁋정의 3](/ko/math/multilinear_algebra/various_modules#def3)) 이를 derived functor를 사용해서 보면, 만일 $$N$$이 injective module이었다면 $$0 \rightarrow N \rightarrow N \rightarrow 0$$이 injective resolution이 되고, 따라서 $$\Ext_A^1(M,N)=0$$이 모든 $$M$$에 대해 성립하는 것을 안다. 그럼 임의의 short exact sequence

$$0 \rightarrow M_1 \rightarrow M_2 \rightarrow M_3 \rightarrow 0$$

에 $$\Hom_\lMod{A}(-,N)$$을 취하고, 그 derived functor를 생각하여 얻어지는 다음의 long exact sequence

$$\begin{aligned}0 &\rightarrow \Hom_\lMod{A}(M_3, N) \rightarrow \Hom_\lMod{A}(M_2, N) \rightarrow \Hom_\lMod{A}(M_1, N)\\
&\rightarrow\Ext_A^1(M_3,N) \rightarrow\Ext_A^1(M_2,N) \rightarrow\cdots\end{aligned}$$

에서, $$\Ext_A^1(M_3,N)=0$$이 성립하므로 $$\Hom_\lMod{A}(-,N)$$이 exact라는 것을 알 수 있다.

한편, [정의 1](#def1) 대신 우리는 고정된 $$N$$에 대하여 $$\Hom_\lMod{A}(-,N):\lMod{A} \rightarrow \Ab$$를 생각한 후 이 left exact functor의 right derived functor로서 $$\Ext$$를 정의할 수도 있었을 것이다. 이 두 정의가 같다는 것은 아래 [명제 3](#prop3)에서 확인할 수 있다.

## Tor 함자의 정의

임의의 $$N\in\rMod{A}$$에 대하여, $$-\otimes_A N$$은 $$\lMod{A}$$에서 $$\Ab$$로의 right exact functor이므로, left derived functor를 생각할 수 있다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Right exact functor $$-\otimes_A N:\lMod{A} \rightarrow \Ab$$의 left derived functor를

$$\Tor_i^A(M,N)=L_i(-\otimes_A N)(M)$$

으로 정의하고, 이들을 *$$\Tor$$ group*들이라 부른다.

</div>

$$\Tor$$를 계산하기 위해서는 $$M$$의 projective resolution을 사용해야 한다. 따라서, 앞선 문단에서의 계산과 마찬가지로 $$M$$이 projective $$A$$-module이었다면 $$0 \rightarrow M \rightarrow M \rightarrow 0$$이 $$M$$의 projective resolution이 되고, 이로부터 $$\Tor_1^A(M,N)=0$$이 모든 $$N$$에 대해 성립했을 것이다. 즉, 임의의 projective $$A$$-module은 flat $$A$$-module임을 다시 한 번 확인할 수 있다.

## Balancing

본질적으로 $$\Hom$$과 $$\otimes$$는 두 개의 대상을 받는 bifunctor이다. 따라서 두 input 중 어느 것을 injective resolution 혹은 projective resolution으로 대체하는지에 따라 다른 결과가 나올 수도 있을 것이며, 이는 그렇게 바람직한 일이 아닐 것이다. 예를 들어 $$\Ext_A^i(M,N)$$을 계산한다 하였을 때, $$M$$의 projective resolution $$P_\bullet\rightarrow M\rightarrow 0$$을 사용하여

$$0\rightarrow \Hom_{\lMod{A}}(M, N)\rightarrow \Hom_{\lMod{A}}(P_0,N)\rightarrow \Hom_{\lMod{A}}(P_1, N)\rightarrow\cdots$$

의 $$i$$번째 cohomology를 생각할 수도 있고, $$N$$의 injective resolution $$0\rightarrow N\rightarrow I^\bullet$$을 사용하여

$$0\rightarrow \Hom_{\lMod{A}}(M, N)\rightarrow \Hom_{\lMod{A}}(M, I^0)\rightarrow \Hom_{\lMod{A}}(M, I^1)\rightarrow\cdots$$

을 생각할 수도 있을 것인데, 이들 두 결과가 같아야 비로소 $$\Ext$$를 "잘" 정의했다고 할 수 있을 것이다. 마찬가지로 $$\Tor$$도 다음의 두 chain complex

$$\cdots\rightarrow P_1\otimes_AN \rightarrow P_0\otimes_AN \rightarrow M\otimes_AN\rightarrow0$$

와

$$\cdots \rightarrow M\otimes_AN_1\rightarrow M\otimes_AN_0\rightarrow M\otimes_A N\rightarrow0$$

중 어느 것을 택하는지에 따라 $$\Tor^A_i(M,N)$$의 값이 달라져서는 안될 것이다.

우리는 따라서 이들이 주는 cohomology를 비교해야 한다. 이를 위한 증명 전략은 $$(p,q)$$ 성분이 $$\Hom_{\lMod{A}}(P_q, I^p)$$인 (혹은 텐서의 경우, $$P_p\otimes P'_q$$인) double complex를 생각하는 것이다. ([§호몰로지, ⁋정의 4](/ko/math/homological_algebra/homology#def4))

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> 두 $$A$$-module $$M \in \lMod{A}$$, $$N \in \lMod{A}$$, 그리고 이들의 projective resolution $$P_\bullet\rightarrow M\rightarrow 0$$과 injective resolution $$0\rightarrow N\rightarrow I^\bullet$$에 대하여, 다음의 isomorphism

$$H^n(\Hom_\lMod{A}(M, I^\bullet)) \cong H^n(\Hom_\lMod{A}(P_\bullet, N))$$

이 성립한다. 여기서 $$P_\bullet \to M$$은 $$M$$의 projective resolution이고, $$N \to I^\bullet$$은 $$N$$의 injective resolution이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

다음의 double complex

$$K^{p,q}=\Hom_\lMod{A}(P_q, I^p)$$

를 생각하자. Horizontal differential $$d_h:K^{p,q} \rightarrow K^{p+1,q}$$은 $$I^p\rightarrow I^{p+1}$$에 $$\Hom_\lMod{A}(P_q,-)$$를 취하여 얻고, 비슷하게 vertical differential $$d_v: K^{p,q}\rightarrow K^{p,q+1}$$은 $$P_{q+1}\rightarrow P_q$$에 $$\Hom_\lMod{A}(-,I^p)$$를 취하여 얻는다. 이제 이 double complex의 total complex $$\Tot(K)^\bullet$$을 생각하자. ([§호몰로지, ⁋정의 5](/ko/math/homological_algebra/homology#def5)) 그럼 주어진 isomorphism은 $$\Tot(K)^\bullet$$의 $$n$$번째 cohomology를 다른 방법으로 계산한 것이다.

이를 확인하기 위해, 우선 cochain complex의 row $$K^{\bullet, q}$$와 column $$K^{p,\bullet}$$의 cohomology는 다음의 식

$$H^q(K^{p, \bullet}) = \begin{cases} \Hom_\lMod{A}(M, I^p) & q = 0 \\ 0 & q > 0, \end{cases}\qquad H^p(K^{\bullet, q}) = \begin{cases} \Hom_\lMod{A}(P_q, N) & p = 0 \\ 0 & p > 0. \end{cases}\tag{$\ast$}$$

으로 계산된다는 것을 확인하자. 여기서 cohomology가 사라지는 것들은 projective module과 injective module의 정의에 따른 것이다. ([\[다중선형대수학\] §사영가군, 단사가군, 평탄가군, ⁋정의 3](/ko/math/multilinear_algebra/various_modules#def3))

[§호몰로지, ⁋정의 5](/ko/math/homological_algebra/homology#def5) 직후에 수행한 계산과 마찬가지로, total complex의 cohomology를 계산하려면 differential들이 각 항을 섞어놓기 때문에 다소 주의해야 한다. 이를 위해 우리는 *filtration*을 사용한다. 

우선 $$\Tot(K)^\bullet$$에 filtration

$$F^p \Tot(K)^k = \bigoplus_{\substack{i \geq p \\ i+q=k}} K^{i,q}$$

을 생각하자. 이는 total complex의 degree $$k$$에서 horizontal 성분이 $$p$$ 이상인 것만 뽑아오는 것이며, 정의에 의해 $$F^0\Tot(K)^\bullet=\Tot(K)^\bullet$$이고, $$p>k$$인 $$p$$에 대해서는 $$F^p\Tot(K)^k=0$$임이 자명하다. 

이제 inclusion으로부터 induce되는 다음의 short exact sequence

$$0 \rightarrow F^{p+1} \Tot(K)^k \rightarrow F^{p} \Tot(K)^k \rightarrow K^{p, k-p} \rightarrow 0$$

가 존재하며, 이를 complex로 승격시키면

$$0 \rightarrow F^{p+1}\Tot(K)^\bullet \rightarrow F^p \Tot(K)^\bullet \rightarrow K^{p, \bullet-p} \rightarrow 0$$

을 얻는다. 즉, 중요한 것은 $$\Tot(K)^\bullet$$의 cohomology는 계산하기 까다롭지만, filtration을 걸면 이를 column의 cohomology 계산과 연관지을 수 있고 따라서 위의 계산 ($$\ast$$)을 활용할 수 있다는 것이다. 

이제 고정된 $$n$$에 대하여 $$H^n(F^p\Tot(K)^\bullet)$$들을 계산하고, 이로부터 $$H^n(F^0\Tot(K)^\bullet)=H^n(\Tot(K)^\bullet)$$을 구해내자. 위의 short exact sequence로부터 다음의 cohomology long exact sequence

$$\cdots\rightarrow H^{n-1}(K^{p, \bullet-p})\rightarrow H^n(F^{p+1}\Tot(K)^\bullet)\rightarrow H^n(F^p\Tot(K)^\bullet)\rightarrow H^n(K^{p, \bullet-p})\rightarrow \cdots$$

을 생각하면, ($$\ast$$)로부터 $$H^{n-1}(K^{p,\bullet-p})$$와 $$H^n(K^{p,\bullet-p})$$이 nontrivial한 부분, 즉 $$p=n,n-1$$인 경우를 제외한 모든 부분에서는 

$$H^n(F^p\Tot(K)^\bullet)\cong H^n(F^{p+1}\Tot(K)^\bullet)\tag{$\ast\ast$}$$

이 성립하는 것을 안다. 이제 $$p=n$$인 경우를 생각하면, long exact sequence는

$$0=H^n(F^{n+1}\Tot(K)^\bullet)\rightarrow H^n(F^n\Tot(K)^\bullet)\rightarrow \Hom_\lMod{A}(M, I^n)\rightarrow H^{n+1}(F^{n+1}\Tot(K)^\bullet)\rightarrow \cdots$$

이며 이를 통해 $$H^n(F^n\Tot(K)^\bullet)$$은 connecting homomorphism

$$\delta_n:\Hom_\lMod{A}(M, I^n)\rightarrow H^{n+1}(F^{n+1}\Tot(K)^\bullet)$$

의 kernel임을 안다. 마찬가지 논리로 $$H^{n+1}(F^{n+1}\Tot(K)^\bullet)$$은 $$\Hom_\lMod{A}(M, I^{n+1})$$로 들어갈 것이며, 실제로 계산을 해 보면 $$\delta_n$$이 정확히 $$\Hom_\lMod{A}(M, I^n)\rightarrow \Hom_\lMod{A}(M, I^{n+1})$$로부터 오는 것을 안다. 즉,

$$H^n(F^n\Tot(K)^\bullet)=\ker\left(\Hom_\lMod{A}(M, I^n)\rightarrow \Hom_\lMod{A}(M, I^{n+1})\right)$$

이다. 이제 이를 바탕으로 $$p=n-1$$인 경우의 cohomology long exact sequence를 분석하면

$$\cdots \longrightarrow \Hom_\lMod{A}(M, I^{n-1}) \overset{\delta_{n-1}}{\longrightarrow} H^n(F^n\Tot(K)^\bullet) \longrightarrow H^n(F^{n-1}\Tot(K)^\bullet) \longrightarrow 0$$

에서, $$H^n(F^{n-1}\Tot(K)^\bullet)$$은 connecting homomorphism $$\delta_{n-1}$$의 cokernel이라는 것을 안다. 이 때, $$H^n(F^n\Tot(K)^\bullet)$$은 이미 $$p=n$$인 경우에 구했으며, connecting homomorphism $$\delta_{n-1}$$은 다시 $$\Hom_\lMod{A}(M, I^{n-1})\rightarrow \Hom_\lMod{A}(M, I^{n})$$으로부터 오는 것이므로

$$H^n(F^{n-1}\Tot(K)^\bullet)=\frac{\ker(\Hom_\lMod{A}(M, I^n) \to \Hom_\lMod{A}(M, I^{n+1}))}{\im(\Hom_\lMod{A}(M, I^{n-1}) \to \Hom_\lMod{A}(M, I^n))}$$

을 얻는다. 이제 $$p<n-1$$에 대해서는 isomorphism ($$\ast\ast$$)을 사용하여 모든 경우가 $$p=n-1$$과 isomorphic함을 알 수 있고 특히

$$H^n(\Tot(K)^\bullet) = H^n(F^0\Tot(K)^\bullet) = H^n(F^1\Tot(K)^\bullet) = \cdots = H^n(F^{n-1}\Tot(K)^\bullet) = H^n(\Hom_\lMod{A}(M, I^\bullet))$$

이다. 이제 비슷한 방식으로, $$\Tot(K)^\bullet$$에 다음의 filtration

$$G^q \Tot(K)^k = \bigoplus_{\substack{j \geq q \\ p+j=k}} K^{p,j}$$

을 걸고 계산하면 $$H^n(\Tot(K)^\bullet) = H^n(\Hom_\lMod{A}(P_\bullet, N))$$를 얻고, 이로부터 원하는 결과를 얻는다.

</details>

비슷한 방식으로 $$\Tor$$에 대해서도 balancing을 증명할 수 있다. 증명 구조는 동일하며, 차이는 projective module들이 flat module이므로 ([\[다중선형대수학\] §사영가군, 단사가군, 평탄가군, ⁋정의 7](/ko/math/multilinear_algebra/various_modules#def7)) 이를 사용하여 계산을 처리해주면 된다는 것이다. 자세한 증명은 생략하기로 한다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> 두 $$A$$-module $$M \in \lMod{A}$$, $$N \in \lMod{A}$$, 그리고 이들의 projective resolution $$P_\bullet\rightarrow M\rightarrow 0$$, $$P_\bullet'\rightarrow N\rightarrow 0$$에 대하여

$$H_n(P_\bullet \otimes_A N) \cong H_n(M \otimes_A P'_\bullet)$$

이 성립한다. 

</div>

## 예시

앞서 정의한 Ext와 Tor 함자를 구체적으로 계산해본다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> $$n, m \in \Z$$에 대해, 다음이 성립한다.

$$
\Tor_1^\Z(\Z/n\Z, \Z/m\Z) \cong \Z/\gcd(n,m)\Z.
$$

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\Z/n\Z$$의 projective resolution을 구성한다. 사상 $$\cdot n \colon \Z \to \Z$$의 image는 $$n\Z$$이므로

$$0 \to \Z \xrightarrow{\cdot n} \Z \to \Z/n\Z \to 0$$

은 exact하며, $$\Z$$는 projective $$\Z$$-module이므로 이것이 $$\Z/n\Z$$의 projective resolution이다.

이 resolution에 $$- \otimes_\Z \Z/m\Z$$를 적용한 chain complex는

$$\cdots \to 0 \to \Z \otimes_\Z \Z/m\Z \xrightarrow{\cdot n \otimes 1} \Z \otimes_\Z \Z/m\Z \to 0 \to \cdots$$

이다. $$\Z \otimes_\Z \Z/m\Z \cong \Z/m\Z$$이므로

$$0 \to \Z/m\Z \xrightarrow{\cdot n} \Z/m\Z \to 0$$

이 되고, 여기서 $$\cdot n$$은 $$\Z/m\Z$$에서 원소 $$a \mapsto na$$로의 사상이다. 따라서

$$\Tor_1^\Z(\Z/n\Z, \Z/m\Z) \cong \ker(\cdot n \colon \Z/m\Z \to \Z/m\Z) = \{a \in \Z/m\Z : na \equiv 0 \pmod{m}\}.$$

이 kernel은 $$m \mid na$$를 만족하는 $$a \pmod{m}$$의 집합이다. $$d = \gcd(n,m)$$, $$n = dn'$$, $$m = dm'$$이라 하자. 그러면 $$m' \mid n'a$$이고, $$\gcd(n', m') = 1$$이므로 $$m' \mid a$$이다. 따라서 kernel은 $$m'\Z/m\Z \subset \Z/m\Z$$, 즉 $$\Z/m\Z$$에서 $$d$$배를 취하면 얻어지는 부분군이다. Chinese remainder theorem에 의해 이 부분군은 순서 $$d$$를 가지며 $$\Z/d\Z$$와 동형이므로

$$\ker(\cdot n \colon \Z/m\Z \to \Z/m\Z) \cong \Z/\gcd(n,m)\Z.$$

</details>

$$\Tor$$라는 이름은 *torsion*에서 유래한다. 명제 5의 결과는 이를 잘 보여준다: $$\Tor_1^\Z(\Z/n\Z, \Z/m\Z)$$가 nontrivial한 것은 정확히 $$\gcd(n,m) > 1$$, 즉 $$\Z/m\Z$$의 원소 중 $$n$$-torsion을 갖는 것이 존재할 때이며, 그 크기 $$\gcd(n,m)$$는 이 torsion의 "양"을 측정한다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> 임의의 abelian group $$A$$와 $$n \in \Z$$에 대해, 다음이 성립한다.

$$
\Ext^1_\Z(\Z/n\Z, A) \cong A/nA.
$$

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\Z/n\Z$$의 projective resolution

$$0 \to \Z \xrightarrow{\cdot n} \Z \to \Z/n\Z \to 0$$

에 $$\Hom_\Z(-, A)$$를 적용한 cochain complex는

$$0 \to \Hom_\Z(\Z, A) \xrightarrow{\cdot n^\ast} \Hom_\Z(\Z, A) \to 0$$

이다. $$\Hom_\Z(\Z, A) \cong A$$이며 (사상은 $$1 \mapsto a$$로 결정됨), 유도된 사상 $$\cdot n^\ast$$은 $$a \mapsto na$$이다. 따라서

$$\Ext^1_\Z(\Z/n\Z, A) \cong \coker(\cdot n \colon A \to A) = A/nA.$$

</details>

$$\Ext$$라는 이름은 *extension*에서 유래한다. 일반적으로 $$\Ext^1(M,N)$$는 $$0 \to N \to E \to M \to 0$$ 형태의 short exact sequence, 즉 $$N$$에 의한 $$M$$의 extension들의 동치류 집합과 자연스럽게 대응된다. 이 대응을 Yoneda의 construction이라 부른다. 명제 6의 결과는 이 관점에서 $$A$$를 coefficient로 하는 $$\Z/n\Z$$-extension이 $$A/nA$$에 의해 분류됨을 보여준다. ([Ext functor - Wikipedia](https://en.wikipedia.org/wiki/Ext_functor))

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> 가환환 $$A$$와 원소 $$\x_1, \ldots, \x_n \in A$$에 대해, *Koszul complex* $$K_\bullet = K(\x_1, \ldots, \x_n)$$를 다음과 같이 정의한다. 각 $$i = 0, 1, \ldots, n$$에 대해

$$K_i = \bigwedge\nolimits^i A^n$$

이며, 이는 $$A$$-module로서 자유 module이고, $$e_{j_1} \wedge \cdots \wedge e_{j_i}$$ ($$1 \leq j_1 < \cdots < j_i \leq n$$)들이 basis를 이룬다. $$K_i$$의 차원은 $$\binom{n}{i}$$이다. Differential $$d_i \colon K_i \to K_{i-1}$$은

$$d(e_{j_1} \wedge \cdots \wedge e_{j_i}) = \sum_{k=1}^{i} (-1)^{k+1} \x_{j_k} e_{j_1} \wedge \cdots \wedge \widehat{e_{j_k}} \wedge \cdots \wedge e_{j_i}$$

로 주어진다. 이때 $$\widehat{\phantom{e}}$$는 해당 항이 생략됨을 나타낸다.

</div>

Koszul complex $$K(\x_1, \ldots, \x_n)$$는 $$\mathbb{K} = A/(\x_1, \ldots, \x_n)$$의 projective resolution이 된다. $$K_0 = A$$이고, $$d_1 \colon K_1 = A^n \to K_0 = A$$는 $$(a_1, \ldots, a_n) \mapsto \sum a_i \x_i$$이므로 *augmentation map* $$\epsilon \colon A \to \mathbb{K}$$에 대해 $$\im d_1 = (\x_1, \ldots, \x_n) = \ker \epsilon$$이다. 따라서 $$0 \to K_n \to \cdots \to K_1 \xrightarrow{d_1} A \xrightarrow{\epsilon} \mathbb{K} \to 0$$이 exact함을 보이면 된다.

이 exactness는 $$n$$에 대한 귀납법으로 증명한다. $$n = 0$$인 경우 자명하다. 이제 $$n-1$$개의 변수에 대해 $$K(\x_1, \ldots, \x_{n-1})$$가 exact함을 가정하고, $$A' = \mathbb{K}[\x_1, \ldots, \x_{n-1}]$$ 위에서 $$K'\bullet = K(\x_1, \ldots, \x_{n-1})$$를 생각하자. 그러면

$$K(\x_1, \ldots, \x_n)_i \cong K'_i \oplus K'_{i-1} \cdot e_n$$

이며, $$d_i$$는 행렬

$$d_i = \begin{pmatrix} d'_i & (-1)^i \x_n \\ 0 & d'_{i-1} \end{pmatrix}$$

의 형태를 갖는다. $$(\alpha, \beta) \in \ker d_i$$라 하면 $$d'_{i-1}(\beta) = 0$$이므로 귀납 가정에 의해 $$\beta = d'_i(\gamma)$$가 존재한다. 또한 $$d'_i(\alpha) = (-1)^{i+1} \x_n \beta$$이므로 $$d'_i(\alpha + (-1)^{i+1} \x_n \gamma) = 0$$이고, 다시 귀납 가정에 의해 $$\alpha + (-1)^{i+1} \x_n \gamma \in \im d'_{i+1}$$이다. 따라서 $$\ker d_i \subseteq \im d_{i+1}$$이고, 반대 포함은 자명하다.

이제 이 resolution에 $$- \otimes_A \mathbb{K}$$를 적용하자. 각 $$K_i$$는 자유 $$A$$-module이므로 $$K_i \otimes_A \mathbb{K} \cong \bigwedge^i \mathbb{K}^n$$이며, $$d_i \otimes 1$$은 $$\x_j$$를 $$0$$으로 보내므로 영사상이다. 따라서

$$\Tor_i^A(\mathbb{K}, \mathbb{K}) = H_i(K_\bullet \otimes_A \mathbb{K}) = K_i \otimes_A \mathbb{K} \cong \bigwedge\nolimits^i_{\mathbb{K}}(\mathbb{K}^n).$$

따라서 다음을 얻는다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> 체 $$\mathbb{K}$$와 다항식 환 $$A = \mathbb{K}[\x_1, \ldots, \x_n]$$에 대해, 다음이 성립한다.

$$
\Tor_i^A(\mathbb{K}, \mathbb{K}) \cong \bigwedge\nolimits^i_{\mathbb{K}}(\mathbb{K}^n).
$$

</div>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            