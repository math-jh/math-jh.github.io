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

을 얻는다. 이제 $$p< n-1$$에 대해서는 isomorphism ($$\ast\ast$$)을 사용하여 모든 경우가 $$p=n-1$$과 isomorphic함을 알 수 있고 특히

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

마지막으로 Ext와 Tor의 계산을 조금 더 구체적으로 살펴보자. 

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> 두 정수 $$n, m \in \mathbb{Z}$$에 대해, 다음이 성립한다.

$$\Tor_i^\mathbb{Z}(\mathbb{Z}/n\mathbb{Z}, \mathbb{Z}/m\mathbb{Z}) \cong \begin{cases} \mathbb{Z}/(n,m)\mathbb{Z} & i = 0, 1\\ 0 & i \geq 2. \end{cases}$$ 

여기서 $$(m,n)$$은 $$m$$과 $$n$$의 최대공약수이다. 

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$i=0$$인 경우는 표준적인 계산이므로, 다음의 식

$$0 \rightarrow \mathbb{Z}\rightarrow \mathbb{Z}\rightarrow \mathbb{Z}/n\mathbb{Z}\rightarrow 0$$

이 $$\mathbb{Z}/n\mathbb{Z}$$의 projective resolution $$P_\bullet\rightarrow \mathbb{Z}/n\mathbb{Z}\rightarrow 0$$을 구성하는 것을 확인하자. 여기서 첫 번째 함수는 $$\mathbb{Z}$$의 원소를 $$n$$배하여 보내는 함수이다. 이제 $$\Tor$$를 계산하기 위해서는 여기에 $$-\otimes_\mathbb{Z}\mathbb{Z}/m\mathbb{Z}$$를 적용하면 된다. $$\mathbb{Z}\otimes_\mathbb{Z}\mathbb{Z}/m\mathbb{Z}=\mathbb{Z}/m\mathbb{Z}$$이므로, tensor를 취한 후의 projective resolution은

$$0\rightarrow \mathbb{Z}/m\mathbb{Z}\rightarrow \mathbb{Z}/m\mathbb{Z}\rightarrow 0$$

이고, 따라서 첫 번째 homology는

$$H_1(P_\bullet)=\ker(\cdot n)= \{a \in \mathbb{Z}/m\mathbb{Z} \mid na \equiv 0 \pmod{m}\}=\mathbb{Z}/(m,n)\mathbb{Z}$$

이므로 원하는 결과를 얻는다. 

</details>

이 명제는 $$\Tor$$라는 명칭의 기원을 보여주는데,  $$\Tor_1^\mathbb{Z}(\mathbb{Z}/n\mathbb{Z}, \mathbb{Z}/m\mathbb{Z})$$가 nontrivial한 것은 정확히 $$(n,m) > 1$$, 즉 $$\mathbb{Z}/m\mathbb{Z}$$에 $$n$$-torsion 원소가 존재할 때이며, 이 때 최대공약수 $$(n,m)$$이 torsion의 양을 측정하는 것으로 생각할 수 있다.

비슷한 방식으로 $$\Ext$$에 대한 것도 살펴볼 수 있다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> 임의의 abelian group $$A$$와 $$n \in \mathbb{Z}$$에 대해, 다음이 성립한다.

$$\Ext^i_\mathbb{Z}(\mathbb{Z}/n\mathbb{Z}, A) \cong \begin{cases} A[n] & i = 0, \\ A/nA & i = 1, \\ 0 & i \geq 2. \end{cases}$$

여기서 $$A[n] = \{a \in A \mid na = 0\}$$는 $$n$$-torsion subgroup이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

[명제 5](#prop5)에서와 마찬가지의 projective resolution 

$$0 \rightarrow \mathbb{Z}\rightarrow \mathbb{Z}\rightarrow \mathbb{Z}/n\mathbb{Z}\rightarrow 0$$

을 생각하고 $$\Hom_\mathbb{Z}(-,A)$$를 취하자. 그럼 $$\Hom_\mathbb{Z}(\mathbb{Z},A)$$는 $$1$$의 image에 의해 결정되므로, $$\Hom_\mathbb{Z}(\mathbb{Z}, A)\cong A$$이고 이로부터 다음의 complex

$$0 \to A \xrightarrow{\cdot n} A \to 0$$

를 얻는다. 이 때, 첫 번째 함수는 $$a \mapsto na$$이며, 따라서 첫 번째 호몰로지는

$$\Ext^1_\mathbb{Z}(\mathbb{Z}/n\mathbb{Z}, A) \cong \coker(\cdot n ) = A/nA$$

이다. $$\Hom_\mathbb{Z}(\mathbb{Z}/n\mathbb{Z}, A)=A[n]$$인 것은 단순 계산이다.

</details>

더 일반적으로, $$\Ext^1(M,N)$$는 $$0 \to N \to E \to M \to 0$$ 형태의 short exact sequence, 즉 $$N$$에 의한 $$M$$의 extension의 equivalence class와 연결되며, 이는 Yoneda Ext를 통해 확인할 수 있다. ([Wikipedia](https://en.wikipedia.org/wiki/Ext_functor)) [명제 5](#prop5)보다는 덜 직관적이지만, [명제 6](#prop6) 또한 이러한 의미에서 $$\Ext$$라는 명칭의 기원을 보여준다 할 수 있다. 

마지막으로 우리는 다음을 정의한다. 

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> Commutative ring $$A$$와 rank $$n$$ free $$A$$-module $$F$$, 그리고 $$A$$-linear map $$\varphi : F \to A$$가 주어졌다 하자. 그럼 *Koszul complex* $$K(\varphi)_\bullet$$은 exterior algebra $$K=\bigwedge F$$에 다음과 같이 chain complex 구조를 부여한 것이다. 

1. 각각의 $$i$$에 대하여, $$K_i = \bigwedge\nolimits^i F$$이다.
2. 각각의 $$i$$에 대하여, $$d_i: K_i \to K_{i-1}$$는 degree $$-1$$의 graded derivation으로, 식 $$d(f) = \varphi(f)$$와 Leibniz rule
    
    $$d(\xi \wedge \eta) = d(\xi) \wedge \eta + (-1)^{\degree(\xi)} \, \xi \wedge d(\eta)$$

    에 의해 유일하게 결정된다.

</div>

Augmentation map $$\epsilon: K_0=A\to A/\im\varphi$$를 canonical projection으로 정의하면, $$K(\varphi)_\bullet$$을 $$A/\im\varphi$$의 resolution으로 생각할 수 있다. 편의상 $$F$$의 basis $$e_1, \ldots, e_n$$을 고정하고 $$\x_i = \varphi(e_i)$$라 하면 $$\im\varphi = (\x_1, \ldots, \x_n)$$이므로, 이를 $$K_\bullet(\x_1, \ldots, \x_n)$$이라고도 쓴다.

만일 $$\x_1, \ldots, \x_n$$이 $$A$$에서 regular sequence라면, Koszul complex는 $$A/(\x_1, \ldots, \x_n)$$의 *free resolution*이 된다. ([\[가환대수학\] §정칙국소환, ⁋정의 2](/ko/math/commutative_algebra/regular_local_rings#def2)) 즉

$$0 \to K_n \to \cdots \to K_1 \xrightarrow{d_1} A \xrightarrow{\epsilon} A/(\x_1, \ldots, \x_n) \to 0$$

이 exact하다. 

이를 보이기 위해 $$n$$에 대한 귀납법을 사용한다. $$n = 0$$인 경우는 자명하므로, $$n-1$$개의 원소에 대해 $$K(\x_1, \ldots, \x_{n-1})$$가 exact함을 가정하자.

$$\x_n$$이 regular sequence의 마지막 원소이므로, $$\x_n$$은 $$A/(\x_1, \ldots, \x_{n-1})$$ 위에서 non-zerodivisor이다. 따라서 $$\bar{\x}_i$$를 $$\x_i$$의 $$A/(\x_n)$$에서의 image라 하면, $$\bar{\x}_1, \ldots, \bar{\x}_{n-1}$$은 $$A/(\x_n)$$ 위에서 regular sequence가 되고, 귀납적 가정에 의해 $$K'_\bullet = K(\bar{\x}_1, \ldots, \bar{\x}_{n-1})$$는 $$A/(\x_1, \ldots, \x_n)$$의 free resolution이다.

이제 $$K(\x_1, \ldots, \x_n)_i$$를 관찰하면, 정의에 의해

$$K(\x_1, \ldots, \x_n)_i \cong K'_i \oplus K'_{i-1} \cdot e_n$$

이며, $$d_i$$는 행렬

$$d_i = \begin{pmatrix} d'_i & (-1)^i \x_n \\ 0 & d'_{i-1} \end{pmatrix}$$

의 형태를 갖는다. $$(\alpha, \beta) \in \ker d_i$$라 하면 $$d'_{i-1}(\beta) = 0$$이므로, 귀납적 가정에 의해 $$\beta = d'_i(\gamma)$$인 $$\gamma$$가 존재한다. 또한 $$d'_i(\alpha) = (-1)^{i+1} \x_n \beta$$이므로 $$d'_i(\alpha + (-1)^{i+1} \x_n \gamma) = 0$$이고, 다시 귀납적 가정에 의해 $$\alpha + (-1)^{i+1} \x_n \gamma \in \im d'_{i+1}$$이다. 따라서 $$\ker d_i \subseteq \im d_{i+1}$$이고, 반대방향 포함관계는 자명하다.

이는 특히 field $$\mathbb{K}$$ 위의 polynomial algebra $$A=\mathbb{K}[\x_1,\ldots, \x_n]$$과 regular sequence $$(\x_1,\ldots, \x_n)$$의 경우에 잘 적용된다. 이 때 $$F=\bigoplus_1^nAe_i$$이고 augmentation map은 $$e_i\mapsto \x_i$$로 주어진다. 위의 논의에 의해 Koszul complex는 $$\mathbb{K}$$의 free resolution이 되며, 각각의 $$K_i$$는 free $$A$$-module이므로 $$-\otimes_A\mathbb{K}$$를 적용하면 다음의 complex

$$0 \to \bigwedge\nolimits^n \mathbb{K}^n \to \cdots \to \bigwedge\nolimits^1 \mathbb{K}^n \to \bigwedge\nolimits^0 \mathbb{K}^n \to 0$$

을 얻으며, 이는 $$A/(\x_1,\ldots, \x_n)\cong \mathbb{K}$$의 resolution이다. 한편 $$d_i$$는 $$\varphi$$로부터 유도된 것이므로, $$-\otimes_A \mathbb{K}$$를 적용하면 모든 $$\x_j$$-계수가 $$0$$으로 가므로 $$d_i \otimes 1 = 0$$이다. 따라서

$$\Tor_i^A(\mathbb{K}, \mathbb{K}) = H_i(K_\bullet \otimes_A \mathbb{K}) = K_i \otimes_A \mathbb{K} \cong \bigwedge\nolimits^i_{\mathbb{K}}(\mathbb{K}^n).$$

을 얻는다.

이 계산은 나중에 다항식 환 $$\mathbb{K}[\x_1, \ldots, \x_n]$$의 global dimension이 $$n$$임을 보여주는 데 사용된다. ([##ref##](global-dimension/호몰로지?가환대수?))
