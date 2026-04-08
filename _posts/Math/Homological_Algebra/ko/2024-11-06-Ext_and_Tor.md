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
last_modified_at: 2024-11-06
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

한편, [정의 1](#def1) 대신 우리는 고정된 $$N$$에 대하여 $$\Hom_\lMod{A}(-,N):\lMod{A} \rightarrow \Ab$$를 생각한 후 이 left exact functor의 right derived functor로서 $$\Ext$$를 정의할 수도 있었을 것이다. 이 두 정의가 같다는 것은 아래 명제 3에서 확인할 수 있다.

## Tor 함자의 정의

임의의 $$N\in\rMod{A}$$에 대하여, $$-\otimes_A N$$은 $$\lMod{A}$$에서 $$\Ab$$로의 right exact functor이므로, left derived functor를 생각할 수 있다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Right exact functor $$-\otimes_A N:\lMod{A} \rightarrow \Ab$$의 left derived functor를

$$\Tor_i^A(M,N)=L_i(-\otimes_A N)(M)$$

으로 정의하고, 이들을 *$$\Tor$$ group*들이라 부른다.

</div>

$$\Tor$$를 계산하기 위해서는 $$M$$의 projective resolution을 사용해야 한다. 따라서, 앞선 문단에서의 계산과 마찬가지로 $$M$$이 projective $$A$$-module이었다면 $$0 \rightarrow M \rightarrow M \rightarrow 0$$이 $$M$$의 projective resolution이 되고, 이로부터 $$\Tor_1^A(M,N)=0$$이 모든 $$N$$에 대해 성립했을 것이다. 즉, 임의의 projective $$A$$-module은 flat $$A$$-module임을 다시 한 번 확인할 수 있다. 

## Balancing

[정의 1](#def1)에서 우리는 고정된 $$M$$에 대해 $$\Hom_\lMod{A}(M,-)$$를 derive하여 $$\Ext$$를 정의하였고, 이후 $$\Hom_\lMod{A}(-,N)$$를 derive하는 방식도 언급하였다. 이 두 정의가 실제로 일치한다는 사실, 그리고 [정의 2](#def2)에서 $$N$$의 projective resolution을 사용하여 $$\Tor$$를 정의하였으나 $$M$$의 projective resolution을 사용해도 동일한 결과를 얻는다는 사실을 확립한다. 핵심 도구는 double complex의 total complex에 대한 두 가지 분석 방법이다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> $$M \in \lMod{A}$$, $$N \in \lMod{A}$$에 대해, 다음이 성립한다.

$$
H^n(\Hom_\lMod{A}(M, I^\bullet)) \cong H^n(\Hom_\lMod{A}(P_\bullet, N))
$$

여기서 $$P_\bullet \to M$$은 $$M$$의 projective resolution이고, $$N \to I^\bullet$$은 $$N$$의 injective resolution이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Double complex ([§호몰로지, ⁋정의 5](/ko/math/homological_algebra/homology#def5))

$$
K^{p,q} = \Hom_\lMod{A}(P_{-q}, I^p)
$$

을 정의한다. 여기서 $$P_\bullet$$은 degree $$-q$$에 $$P_q$$를 갖는 chain complex로 생각하고, $$I^\bullet$$은 cochain complex이므로 $$K^{p,q}$$는 first quadrant double complex가 된다. Horizontal differential은 $$d_h \colon K^{p,q} \to K^{p+1,q}$$이며 이는 $$I^\bullet$$의 differential에 의해 유도된 $$\Hom_\lMod{A}(P_{-q}, I^p) \to \Hom_\lMod{A}(P_{-q}, I^{p+1})$$이다. Vertical differential은 $$d_v \colon K^{p,q} \to K^{p,q+1}$$이며 이는 $$P_\bullet$$의 differential $$P_{-q} \to P_{-(q+1)}$$에 의해 유도된 $$\Hom_\lMod{A}(P_{-(q+1)}, I^p) \to \Hom_\lMod{A}(P_{-q}, I^p)$$ (방향에 주의)이다. Total complex $$\mathrm{Tot}(K)^n = \bigoplus_{p+q=n} K^{p,q}$$의 differential은 $$d = d_h + (-1)^p d_v$$로 주어진다.

Total complex의 cohomology를 두 가지 방법으로 계산한다.

**첫 번째 방법 (열 단위 분석).** $$P_{-q}$$가 projective이므로, cochain complex $$K^{\bullet, q} = \Hom_\lMod{A}(P_{-q}, I^\bullet)$$의 cohomology는

$$
H^p(K^{\bullet, q}) = \Ext_A^p(P_{-q}, N) = \begin{cases} \Hom_\lMod{A}(P_{-q}, N) & p = 0 \\ 0 & p > 0. \end{cases}
$$

즉, 각 열의 cohomology는 $$p = 0$$에서만 nonzero이다. $$\mathrm{Tot}(K)^\bullet$$에서 $$p > 0$$인 성분만 모은 subcomplex $$A^\bullet$$을 정의하자. 즉 $$A^k = \bigoplus_{p > 0, \, p+q=k} K^{p,q}$$이다. Filtration $$F^p A^k = \bigoplus_{j \geq p, \, j+q=k} K^{j,q}$$을 주자. 그러면 exact sequence

$$0 \to F^{p+1} A^\bullet \to F^p A^\bullet \to K^{\bullet, k-p} \to 0$$

이 얻어지며, 여기서 오른쪽의 $$K^{\bullet, q}$$는 $$p$$에 대해 $$p > 0$$인 성분만을 가진다. $$K^{\bullet,q}$$의 cohomology는 $$p > 0$$에서 모두 $$0$$이므로, $$F^0 A^\bullet = A^\bullet$$에 대해 귀납적으로 $$H^k(A^\bullet) = 0$$임이 따른다. 따라서 $$\mathrm{Tot}(K)^\bullet$$의 cocycle $$x$$는 항상 $$p > 0$$인 성분에서 coboundary이며, 오직 $$p = 0$$인 성분 $$x^{0,n} \in \Hom_\lMod{A}(P_{-n}, N)$$만이 cohomology class를 결정한다.

Quotient complex $$\mathrm{Tot}(K)^\bullet / A^\bullet$$은 $$p = 0$$인 열만으로 이루어진 $$\bigoplus_q K^{0,q} = \bigoplus_q \Hom_\lMod{A}(P_{-q}, N)$$와 동치이며, 여기서의 differential은 $$d_v$$, 즉 $$P_\bullet$$의 differential에 의해 유도된 사상이다. 따라서

$$
H^n(\mathrm{Tot}(K)^\bullet) \cong H^n(\mathrm{Tot}(K)^\bullet / A^\bullet) = H^n(\Hom_\lMod{A}(P_\bullet, N)).
$$

**두 번째 방법 (행 단위 분석).** 각 행 $$K^{p, \bullet} = \Hom_\lMod{A}(P_\bullet, I^p)$$의 homology를 계산한다. $$I^p$$가 injective이므로 $$\Hom_\lMod{A}(-, I^p)$$은 exact이고, $$P_\bullet \to M$$이 resolution이므로

$$
H^{-q}(K^{p, \bullet}) = \begin{cases} \Hom_\lMod{A}(M, I^p) & q = 0 \\ 0 & q > 0. \end{cases}
$$

즉, 각 행의 homology는 $$q = 0$$에서만 nonzero이다. $$q > 0$$인 성분만 모은 subcomplex $$B^\bullet$$에 대해, 위와 동일한 논의로 $$H^k(B^\bullet) = 0$$이 성립한다. Quotient $$\mathrm{Tot}(K)^\bullet / B^\bullet$$은 $$q = 0$$인 행만으로 이루어진 $$\bigoplus_p K^{p,0} = \bigoplus_p \Hom_\lMod{A}(M, I^p)$$와 동치이며, 여기서의 differential은 $$d_h$$, 즉 $$I^\bullet$$의 differential에 의해 유도된 사상이다. 따라서

$$
H^n(\mathrm{Tot}(K)^\bullet) \cong H^n(\mathrm{Tot}(K)^\bullet / B^\bullet) = H^n(\Hom_\lMod{A}(M, I^\bullet)).
$$

두 방법에서 같은 $$H^n(\mathrm{Tot}(K)^\bullet)$$을 얻으므로

$$
H^n(\Hom_\lMod{A}(M, I^\bullet)) \cong H^n(\Hom_\lMod{A}(P_\bullet, N)).
$$

</details>

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $$M \in \lMod{A}$$, $$N \in \rMod{A}$$에 대해, 다음이 성립한다.

$$
H_n(P_\bullet \otimes_A N) \cong H_n(M \otimes_A P'_\bullet)
$$

여기서 $$P_\bullet \to M$$은 $$M$$의 projective resolution이고, $$P'_\bullet \to N$$은 $$N$$의 projective resolution이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Double complex ([§호몰로지, ⁋정의 5](/ko/math/homological_algebra/homology#def5))

$$
K_{p,q} = P_p \otimes_A P'_q
$$

을 정의한다. Horizontal differential은 $$d_h \colon K_{p,q} \to K_{p-1,q}$$이며 $$P_\bullet$$의 differential에 의해 유도되고, vertical differential은 $$d_v \colon K_{p,q} \to K_{p,q-1}$$이며 $$P'_\bullet$$의 differential에 의해 유도된다. Total complex는 $$\mathrm{Tot}(K)_n = \bigoplus_{p+q=n} K_{p,q}$$이고 differential은 $$d = d_h + (-1)^p d_v$$이다.

**첫 번째 방법 (열 단위 분석).** 각 열 $$K_{\bullet, q} = P_\bullet \otimes_A P'_q$$의 homology를 계산한다. $$P'_q$$가 projective이므로 flat이고, 따라서 $$P_\bullet \otimes_A P'_q$$의 homology는

$$
H_p(K_{\bullet, q}) = \begin{cases} M \otimes_A P'_q & p = 0 \\ 0 & p > 0. \end{cases}
$$

$$p > 0$$인 성분만 모은 subcomplex $$A_\bullet$$에 대해 $$H_k(A_\bullet) = 0$$이 성립하며, quotient $$\mathrm{Tot}(K)_\bullet / A_\bullet$$은 $$p = 0$$인 열만으로 이루어진 $$\bigoplus_q M \otimes_A P'_q = M \otimes_A P'_\bullet$$와 동치이다. 따라서

$$
H_n(\mathrm{Tot}(K)_\bullet) \cong H_n(M \otimes_A P'_\bullet).
$$

**두 번째 방법 (행 단위 분석).** 각 행 $$K_{p, \bullet} = P_p \otimes_A P'_\bullet$$의 homology를 계산한다. $$P_p$$가 projective이므로 flat이고, $$P'_\bullet \to N$$이 resolution이므로

$$
H_q(K_{p, \bullet}) = \begin{cases} P_p \otimes_A N & q = 0 \\ 0 & q > 0. \end{cases}
$$

$$q > 0$$인 성분만 모은 subcomplex $$B_\bullet$$에 대해 동일한 논의로 $$H_k(B_\bullet) = 0$$이 성립하며, quotient $$\mathrm{Tot}(K)_\bullet / B_\bullet$$은 $$q = 0$$인 행만으로 이루어진 $$\bigoplus_p P_p \otimes_A N = P_\bullet \otimes_A N$$와 동치이다. 여기서의 differential은 $$d_h$$, 즉 $$P_\bullet$$의 differential에 의해 유도된 사상이다. 따라서 $$H_n(\mathrm{Tot}(K)_\bullet) \cong H_n(P_\bullet \otimes_A N)$$을 얻는다. 두 방법에서 같은 total homology를 얻으므로 결과가 따른다.

</details>

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

이 kernel은 $$m \mid na$$를 만족하는 $$a \pmod{m}$$의 집합이며, 이는 $$\gcd(n,m) \Z \subset \Z$$에 의해 생성되는 $$\Z/m\Z$$의 subgroup $$\gcd(n,m)\Z/m\Z \cong \Z/(m/\gcd(n,m))\Z$$와 같다. 한편 kernel의 순서는 공식 $$\lvert\ker f\rvert \cdot \lvert\operatorname{im} f\rvert = \lvert\Z/m\Z\rvert = m$$에 의해 $$m / \lvert\operatorname{im}(\cdot n)\rvert = m / (m/\gcd(n,m)) = \gcd(n,m)$$이다. 그런데 $$\gcd(n,m)\Z/m\Z \cong \Z/(m/\gcd(n,m))\Z$$의 순서는 $$m/\gcd(n,m)$$이므로, 더 정확히는

$$\ker(\cdot n \colon \Z/m\Z \to \Z/m\Z) \cong \Z/\gcd(n,m)\Z.$$

마지막 동형은 다음과 같이 확인할 수 있다. $$d = \gcd(n,m)$$, $$n = d n'$$, $$m = d m'$$이라 하자. 그러면 $$n'a \equiv 0 \pmod{m'}$$이 되고, $$\gcd(n', m') = 1$$이므로 $$a \equiv 0 \pmod{m'}$$이다. 따라서 kernel은 $$m'\Z/m\Z \subset \Z/m\Z$$이며, 이는 $$\Z/m\Z$$에서 $$d$$배를 취하면 얻어지는 부분군이다. Chinese remainder theorem에 의해 직접 계산하면, 이 부분군은 순서 $$d$$를 가지며 $$\Z/d\Z$$와 동형인다.

</details>

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

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> 체 $$\mathbb{K}$$와 다항식 환 $$A = \mathbb{K}[\x_1, \ldots, \x_n]$$에 대해, 다음이 성립한다.

$$
\Tor_i^A(\mathbb{K}, \mathbb{K}) \cong \bigwedge\nolimits^i_{\mathbb{K}}(\mathbb{K}^n).
$$

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$A = \mathbb{K}[\x_1, \ldots, \x_n]$$ 위에서 $$\mathbb{K} = A/(\x_1, \ldots, \x_n)$$의 projective resolution로서 *Koszul complex*를 사용한다.

Koszul complex $$K_\bullet = K(\x_1, \ldots, \x_n)$$는 다음과 같이 정의된다. 각 $$i = 0, 1, \ldots, n$$에 대해

$$K_i = \bigwedge\nolimits^i A^n$$

이며, 이는 $$A$$-module로서 자유 module이고, $$\e_{j_1} \wedge \cdots \wedge \e_{j_i}$$ ($$1 \leq j_1 < \cdots < j_i \leq n$$)들이 basis를 이룬다. $$K_i$$의 차원은 $$\binom{n}{i}$$이다. Differential $$d_i \colon K_i \to K_{i-1}$$은

$$d(\e_{j_1} \wedge \cdots \wedge \e_{j_i}) = \sum_{k=1}^{i} (-1)^{k+1} \x_{j_k} \e_{j_1} \wedge \cdots \wedge \widehat{\e_{j_k}} \wedge \cdots \wedge \e_{j_i}$$

로 주어진다. 이때 $$\widehat{\phantom{e}}$$는 해당 항이 생략됨을 나타낸다.

$$K_\bullet$$이 $$\mathbb{K}$$의 projective resolution임을 확인한다. $$K_0 = A$$이고, $$K_\bullet \to \mathbb{K}$$로의 사상은 $$\epsilon \colon K_0 = A \to \mathbb{K}$$, $$a \mapsto \overline{a}$$ (각 $$\x_i$$를 $$0$$으로 보내는 몫사상)으로 주어진다. $$d_1 \colon K_1 = A^n \to K_0 = A$$는 $$(a_1, \ldots, a_n) \mapsto \sum a_i \x_i$$이므로 $$\operatorname{im} d_1 = (\x_1, \ldots, \x_n) = \ker \epsilon$$이다. 따라서 $$0 \to K_n \to \cdots \to K_1 \xrightarrow{d_1} A \xrightarrow{\epsilon} \mathbb{K} \to 0$$이 exact함을 보이면 된다.

이 exactness는 $$n$$에 대한 귀납법으로 증명한다.

* $$n = 0$$: $$K_\bullet$$는 $$A \xrightarrow{\epsilon} \mathbb{K} \to 0$$이므로 자명하게 exact하다.

* 귀납 단계: $$n-1$$개의 변수에 대해 $$K(\x_1, \ldots, \x_{n-1})$$가 exact함을 가정한다. $$K(\x_1, \ldots, \x_n)$$를 filtering으로 분해한다. $$A' = \mathbb{K}[\x_1, \ldots, \x_{n-1}]$$ 위에서 Koszul complex $$K'\bullet = K(\x_1, \ldots, \x_{n-1})$$를 생각하자. 그러면

$$K(\x_1, \ldots, \x_n)_i \cong K'_i \oplus K'_{i-1} \cdot \e_n$$

이며, $$d_i$$는 다음 형태를 갖는다:

$$d_i(\alpha + \beta \wedge \e_n) = d'_i(\alpha) + (-1)^i \x_n \alpha + d'_{i-1}(\beta) \wedge \e_n.$$

이를 행렬로 나타내면

$$d_i = \begin{pmatrix} d'_i & (-1)^i \x_n \\ 0 & d'_{i-1} \end{pmatrix}$$

이 된다. 이 행렬 형태에서 $$\ker d_i$$와 $$\operatorname{im} d_{i+1}$$를 계산한다. 귀납 가정에 의해 $$K'\bullet$$은 exact하므로

$$\ker d_i = \ker d'_i \oplus (\ker d'_{i-1} \cap \x_n^{-1}(\operatorname{im} d'_i + (-1)^{i+1} \ker d'_i)) \cdot \e_n$$

가 되고, $$\x_n$$이 $$A$$에서 nonzerodivisor임을 사용하면 $$\ker d_i = \operatorname{im} d_{i+1}$$임을 얻는다. 구체적으로, $$(\alpha, \beta) \in \ker d_i$$라 하면 $$d'_{i-1}(\beta) = 0$$이고 $$d'_i(\alpha) = (-1)^{i+1} \x_n \beta$$이다. 귀납 가정에 의해 $$\beta \in \operatorname{im} d'_{i}$$, 즉 $$\beta = d'_i(\gamma)$$가 존재한다. 그러면 $$d'_i(\alpha + (-1)^{i+1} \x_n \gamma) = 0$$이므로, 다시 귀납 가정에 의해 $$\alpha + (-1)^{i+1} \x_n \gamma \in \operatorname{im} d'_{i+1}$$이다. 따라서 $$\ker d_i \subseteq \operatorname{im} d_{i+1}$$이고, 반대 포함은 자명하다. 따라서 $$K(\x_1, \ldots, \x_n)$$은 exact하다.

이제 이 resolution에 $$- \otimes_A \mathbb{K}$$를 적용한다. 각 $$K_i$$는 자유 $$A$$-module이므로

$$K_i \otimes_A \mathbb{K} \cong \bigwedge\nolimits^i A^n \otimes_A \mathbb{K} \cong \bigwedge\nolimits^i (A^n \otimes_A \mathbb{K}) \cong \bigwedge\nolimits^i \mathbb{K}^n.$$

한편, $$d_i \otimes 1 \colon K_i \otimes_A \mathbb{K} \to K_{i-1} \otimes_A \mathbb{K}$$는 $$\x_j$$를 $$0$$으로 보내므로 영사상이다. 따라서

$$\Tor_i^A(\mathbb{K}, \mathbb{K}) = H_i(K_\bullet \otimes_A \mathbb{K}) = K_i \otimes_A \mathbb{K} \cong \bigwedge\nolimits^i_{\mathbb{K}}(\mathbb{K}^n).$$

</details>
