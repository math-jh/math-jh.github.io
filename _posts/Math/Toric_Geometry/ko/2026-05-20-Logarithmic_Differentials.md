---

title: "토릭 다양체 위의 로그 미분형식"
excerpt: "Fan으로부터 유도되는 logarithmic differential forms와 canonical class의 toric 표현"

categories: [Math / Toric Geometry]
permalink: /ko/math/toric_geometry/logarithmic_differentials
sidebar:
    nav: "toric_geometry-ko"

header:
    overlay_image: /assets/images/Math/Toric_Geometry/Logarithmic_Differentials.png
    overlay_filter: 0.5

date: 2026-05-20
last_modified_at: 2026-05-20
weight: 6

published: false

---

우리는 [§토릭 다양체의 정의, ⁋정의 3](/ko/math/toric_geometry/toric_varieties#def3)에서 fan $$\Sigma$$로부터 toric variety $$X_\Sigma$$를 구성하였고, [§토러스 인자와 선다발, ⁋정의 1](/ko/math/toric_geometry/toric_divisors#def1)에서 각 ray $$\rho \in \Sigma(1)$$에 torus-invariant prime divisor $$D_\rho$$를 대응시켰다. 그 합 $$D = \sum_{\rho \in \Sigma(1)} D_\rho$$는 정확히 $$X_\Sigma \setminus T_N$$의 boundary를 이루며, [\[대수다양체\] §표준선다발](/ko/math/algebraic_varieties/canonical_bundle)에서 보았듯 algebraic variety의 differential geometry는 본질적으로 cotangent sheaf $$\Omega^1_X$$가 결정한다.

이번 글에서 우리는 toric variety $$X_\Sigma$$ 위에서 $$\Omega^1_{X_\Sigma}$$ 자체보다는 *boundary $$D$$를 따라 logarithmic pole을 허용한* 변형 $$\Omega^1_{X_\Sigma}(\log D)$$를 다룬다. 이는 일반적인 toric variety에서 $$\Omega^1_{X_\Sigma}$$ 자체는 fan으로부터 깨끗한 묘사를 갖지 않는 반면, $$\Omega^1_{X_\Sigma}(\log D)$$는 character lattice $$M$$의 원소들로 완전히 trivialize된다는 놀라운 사실 때문이며, 이 trivialization으로부터 canonical class의 fan-theoretic 공식과 anticanonical hypersurface 위의 표준 volume form이 함께 얻어진다.

## Algebraic torus 위의 불변 미분형식

먼저 toric variety $$X_\Sigma$$가 open dense subset으로 포함하는 algebraic torus $$T_N = N \otimes_\mathbb{Z} \mathbb{C}^\ast$$ 위에서 자연스럽게 등장하는 differential form들을 살펴본다. ([§아핀 토릭 다양체, ⁋명제 11](/ko/math/toric_geometry/affine_toric_varieties#prop11)) $$T_N \cong (\mathbb{C}^\ast)^n$$이므로 ($$n = \rank N$$), $$N$$의 임의의 $$\mathbb{Z}$$-기저 $$e_1, \ldots, e_n$$을 잡으면 coordinate $$\x_i \in \mathbb{C}^\ast$$들이 $$T_N$$의 좌표가 된다.

$$T_N$$ 위에서는 $$\x_i \neq 0$$이므로 $$d\x_i/\x_i$$가 well-defined holomorphic 1-form이다. 이는 affine 좌표 $$d\x_i$$와 달리 torus 작용에 대해 invariant라는 결정적인 성질을 가진다. 구체적으로 $$t \in T_N$$의 작용 $$\x_i \mapsto t_i \x_i$$ 하에서

$$t^\ast \!\left(\frac{d\x_i}{\x_i}\right) = \frac{d(t_i \x_i)}{t_i \x_i} = \frac{t_i \, d\x_i}{t_i \x_i} = \frac{d\x_i}{\x_i}$$

이므로, 형식적으로 $$d\log \x_i$$로 적을 수 있는 이 1-form은 *multiplicative* 좌표계 $$T_N$$에 가장 자연스럽게 적응한 미분형식이다.

이를 lattice의 언어로 일반화하기 위해, 각 character $$\rchi^m: T_N \to \mathbb{C}^\ast$$ ($$m \in M$$)에 대해 logarithmic differential

$$d\log(\rchi^m) := \frac{d\rchi^m}{\rchi^m}$$

을 생각하자. 여기서 $$\rchi^m$$은 $$T_N$$ 위 어디에서나 영이 아니므로 위 표현은 well-defined holomorphic 1-form을 정의한다. $$\rchi^{m+m'} = \rchi^m \rchi^{m'}$$로부터 자동적으로

$$d\log(\rchi^{m+m'}) = d\log(\rchi^m) + d\log(\rchi^{m'})$$

이 성립하므로 대응 $$m \mapsto d\log(\rchi^m)$$은 $$\mathbb{Z}$$-linear이다. 이를 다음 정의로 정리한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 각 $$m \in M$$에 대해, $$T_N$$ 위의 *logarithmic differential<sub>로그 미분형식</sub>* $$d\log(\rchi^m)$$을

$$d\log(\rchi^m) = \frac{d\rchi^m}{\rchi^m} \in \Omega^1(T_N)$$

로 정의한다.

</div>

이로부터 자연스러운 $$\mathbb{C}$$-linear map

$$\Psi: M_\mathbb{C} = M \otimes_\mathbb{Z} \mathbb{C} \longrightarrow \Omega^1(T_N); \qquad m \otimes 1 \longmapsto d\log(\rchi^m)$$

이 정의된다. 우리의 첫 결과는 이 map이 정확히 $$T_N$$-invariant 1-form의 공간 위로 isomorphism이라는 것이다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> $$\Psi$$는 $$T_N$$-invariant global 1-form의 공간 $$\Omega^1(T_N)^{T_N}$$ 위로의 $$\mathbb{C}$$-vector space isomorphism

$$\Psi: M_\mathbb{C} \xrightarrow{\ \sim\ } \Omega^1(T_N)^{T_N}$$

을 정의한다. 특히 $$\Omega^1(T_N)^{T_N}$$은 $$n$$차원이며, $$N$$의 $$\mathbb{Z}$$-기저 $$e_1, \ldots, e_n$$의 dual $$e_1^\ast, \ldots, e_n^\ast \in M$$에 대해 $$\{d\log \x_i\}_{i=1}^n = \{d\log(\rchi^{e_i^\ast})\}_{i=1}^n$$이 그 기저를 이룬다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$N$$의 기저 $$e_1, \ldots, e_n$$과 dual 기저 $$e_1^\ast, \ldots, e_n^\ast \in M$$을 고정하면, $$\rchi^{e_i^\ast} = \x_i$$가 $$T_N$$의 좌표 함수이다. 위에서 $$d\log \x_i$$가 $$T_N$$-invariant임을 보였으므로 $$\Psi$$의 image는 $$\Omega^1(T_N)^{T_N}$$에 포함된다.

역으로 임의의 1-form $$\omega \in \Omega^1(T_N)$$은 좌표 $$\x_1, \ldots, \x_n$$에 대해

$$\omega = \sum_{i=1}^n f_i(\x) \, d\x_i = \sum_{i=1}^n (\x_i f_i(\x)) \, d\log \x_i$$

의 꼴로 유일하게 표현된다. $$T_N$$-invariance를 strong한 조건으로 풀어쓰면 모든 $$t \in T_N$$에 대해 $$t^\ast \omega = \omega$$이어야 하고, $$t^\ast(d\log \x_i) = d\log \x_i$$이므로 각 계수 $$\x_i f_i(\x)$$가 $$T_N$$-invariant function이어야 한다. 그런데 $$T_N$$ 위의 invariant regular function은 상수뿐이므로 ([§아핀 토릭 다양체, ⁋명제 10](/ko/math/toric_geometry/affine_toric_varieties#prop10)) $$\x_i f_i(\x) = c_i \in \mathbb{C}$$이고, 따라서

$$\omega = \sum_{i=1}^n c_i \, d\log \x_i = \Psi\!\left(\sum_{i=1}^n c_i \, e_i^\ast\right)$$

가 되어 $$\omega$$가 $$\Psi$$의 image에 들어간다. $$\Psi$$의 단사성은 $$\{d\log \x_i\}$$가 $$\mathbb{C}(T_N)$$-module로서의 $$\Omega^1(T_N)$$의 free basis이므로 자명하다.

</details>

위 명제는 단순히 차원만 맞춰주는 것이 아니라, $$T_N$$-invariant 1-form들이 character lattice의 lattice point들과 *공식적으로 같은 것*임을 알려준다. 따라서 $$T_N$$ 위에서 고려할 가장 자연스러운 top form은 임의의 $$\mathbb{Z}$$-기저 $$m_1, \ldots, m_n$$의 $$M$$에 대해

$$\omega_{T_N} := d\log(\rchi^{m_1}) \wedge \cdots \wedge d\log(\rchi^{m_n}) \in \Omega^n(T_N)^{T_N}$$

으로 주어지며, $$M$$의 기저를 바꾸면 $$\omega_{T_N}$$이 $$\GL_n(\mathbb{Z})$$의 determinant인 $$\pm 1$$배만큼만 변하므로 부호 차이를 제외하면 canonical하다.

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> $$T_N = \mathbb{C}^\ast$$ ($$n=1$$)의 경우, $$M = \mathbb{Z}$$이며 $$M$$의 generator $$1 \in M$$에 대해 $$\rchi^1 = \x$$이다. 따라서 $$\omega_{T_N} = d\x/\x$$이며, $$\mathbb{C}^\ast$$의 de Rham cohomology가 $$H^\bullet(\mathbb{C}^\ast) = \mathbb{C} \oplus \mathbb{C}[d\x/\x]$$로 이 한 형식에 의해 생성된다는 사실 또한 이로부터 자연스럽다.

</div>

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> $$T_N = (\mathbb{C}^\ast)^2$$의 경우 standard 기저 $$\{e_1^\ast, e_2^\ast\} \subset M$$에 대해 $$\rchi^{e_1^\ast} = \x$$, $$\rchi^{e_2^\ast} = \y$$이며

$$\omega_{T_N} = \frac{d\x}{\x} \wedge \frac{d\y}{\y}$$

이다. 만일 대신 기저를 $$\{e_1^\ast + e_2^\ast,\ e_2^\ast\}$$로 바꾸면 $$\rchi^{e_1^\ast + e_2^\ast} = \x\y$$이고

$$\frac{d(\x\y)}{\x\y} \wedge \frac{d\y}{\y} = \left(\frac{d\x}{\x} + \frac{d\y}{\y}\right) \wedge \frac{d\y}{\y} = \frac{d\x}{\x} \wedge \frac{d\y}{\y}$$

가 되어 정확히 동일한 top form이 얻어지는 것을 확인할 수 있다. 이러한 기저 무관성이 곧 $$\omega_{T_N}$$의 canonical성이다.

</div>

## Toric 다양체로의 확장과 로그 극

지금까지의 form들은 $$T_N$$ 위에서만 정의되었다. 우리는 이를 toric variety $$X_\Sigma$$ 전체로 확장하고자 하는데, character $$\rchi^m$$은 $$X_\Sigma$$ 위에서 *rational* function일 뿐이므로 ([§토러스 인자와 선다발, ⁋명제 3](/ko/math/toric_geometry/toric_divisors#prop3)) $$d\log \rchi^m = d\rchi^m / \rchi^m$$ 또한 일반적으로는 boundary $$D_\rho$$를 따라 pole을 가지는 rational form이 된다. 다행히 character의 logarithmic differential의 pole은 *가장 약한* 종류, 즉 logarithmic pole에 한정되며, 이러한 form 전체를 모은 sheaf가 fan으로부터 깔끔하게 기술된다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Smooth variety $$X$$ 위의 reduced effective divisor $$D \subset X$$가 *simple normal crossing divisor* (이하 *SNC divisor*)라는 것은, 각 점 $$p \in X$$ 주위에서 적당한 local coordinate $$z_1, \ldots, z_n$$을 잡았을 때 $$D$$의 local equation이 $$z_1 \cdots z_k = 0$$ ($$0 \le k \le n$$; $$k = 0$$인 경우 $$D$$가 $$p$$를 지나지 않음)의 형태로 표현되는 것을 말한다. 직관적으로, $$D$$를 이루는 component들이 각각 smooth이고 좌표평면처럼 transversally 만나는 경우이다.

</div>

먼저 임의의 smooth variety와 SNC divisor에 대해 logarithmic pole만 허용한 form들의 sheaf를 정의한 뒤 (Saito-Deligne의 표준 정의), 이를 toric variety의 toric boundary에 적용한다.

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> Smooth variety $$X$$와 SNC divisor $$D \subset X$$ ([정의 5](#def5))의 쌍 $$(X, D)$$에 대해, *logarithmic cotangent sheaf<sub>로그 코탄젠트 층</sub>* $$\Omega^1_X(\log D)$$는 $$D$$ 바깥에서 holomorphic이며 $$D$$를 따라서는 1차 이하의 극만 갖는 rational 1-form들로 이루어진 $$\mathcal{O}_X$$-module subsheaf이다. 추상적으로 affine open $$U \subset X$$에 대해

$$\Omega^1_X(\log D)(U) = \{\omega \in \Omega^1_{\mathbb{C}(X)/\mathbb{C}}(U) \mid \omega \text{와 } d\omega \text{가 } U \text{ 위에서 } D\text{를 따라 1차 이하의 극을 가짐}\}$$

으로 주어진다. 국소적으로 $$D = \{z_1 \cdots z_k = 0\}$$이면 $$\Omega^1_X(\log D)$$는

$$\frac{dz_1}{z_1}, \ldots, \frac{dz_k}{z_k}, dz_{k+1}, \ldots, dz_n$$

으로 자유롭게 생성되는 free $$\mathcal{O}_X$$-module이다. 더 높은 차수의 logarithmic form sheaf는 외적으로 $$\Omega^p_X(\log D) := \bigwedge^p \Omega^1_X(\log D)$$로 정의한다.

</div>

[§아핀 토릭 다양체, ⁋명제 9](/ko/math/toric_geometry/affine_toric_varieties#prop9)에서 보았듯 smooth toric variety $$X_\Sigma$$의 affine chart $$U_\sigma$$는 적당한 좌표에서 $$\mathbb{C}^k \times (\mathbb{C}^\ast)^{n-k}$$이고 boundary는 좌표 hyperplane $$\{\x_1 = 0\}, \ldots, \{\x_k = 0\}$$의 합이므로, smooth toric variety의 toric boundary는 자동으로 SNC ([정의 5](#def5))이며 [정의 6](#def6)의 logarithmic cotangent sheaf $$\Omega^p_{X_\Sigma}(\log D)$$가 잘 정의된다.

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> Toric variety $$X_\Sigma$$의 *toric boundary<sub>토릭 경계</sub>* $$D \subset X_\Sigma$$를

$$D = X_\Sigma \setminus T_N = \sum_{\rho \in \Sigma(1)} D_\rho$$

로 정의한다 (reduced divisor로 본다).

</div>

$$\Omega^1_{X_\Sigma}$$ 자체는 일반적인 toric variety에 대해 trivial bundle이 *아니지만*, $$\log D$$ twist를 가하면 놀랍게도 항상 trivial이 된다는 것이 다음 결과의 핵심이다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> Smooth toric variety $$X_\Sigma$$에 대해 자연스러운 isomorphism

$$\Omega^1_{X_\Sigma}(\log D) \cong M \otimes_\mathbb{Z} \mathcal{O}_{X_\Sigma}$$

이 존재한다. 더 구체적으로, character lattice $$M$$의 원소 $$m \in M$$을 logarithmic differential $$d\log(\rchi^m) = d\rchi^m / \rchi^m$$에 대응시키는 map이 위 isomorphism을 정의한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

먼저 각 $$m \in M$$에 대해 $$d\log(\rchi^m)$$이 $$X_\Sigma$$ 위의 global section of $$\Omega^1_{X_\Sigma}(\log D)$$임을 보인다. 이는 local에서 확인하면 충분하다. Smooth cone $$\sigma \in \Sigma$$에 대해 [§아핀 토릭 다양체, ⁋명제 9](/ko/math/toric_geometry/affine_toric_varieties#prop9)에 의해 $$U_\sigma \cong \mathbb{C}^k \times (\mathbb{C}^\ast)^{n-k}$$이고, $$\sigma$$의 ray들의 primitive generator $$v_1, \ldots, v_k$$를 $$N$$의 기저의 일부로 잡아 dual 기저 $$\{v_1^\ast, \ldots, v_n^\ast\} \subset M$$을 만들면 $$U_\sigma$$의 좌표가 $$\x_i = \rchi^{v_i^\ast}$$ ($$i=1, \ldots, n$$)로 주어지며 여기서 $$\x_1, \ldots, \x_k$$는 $$\mathbb{C}$$-값 좌표, $$\x_{k+1}, \ldots, \x_n$$는 $$\mathbb{C}^\ast$$-값 좌표이다. Boundary $$D \cap U_\sigma$$는 $$\{\x_1 \x_2 \cdots \x_k = 0\}$$이며 simple normal crossing이다. 임의의 $$m = \sum_i a_i v_i^\ast \in M$$에 대해

$$d\log(\rchi^m) = d\log\!\left(\prod_i \x_i^{a_i}\right) = \sum_{i=1}^n a_i \, \frac{d\x_i}{\x_i}$$

이며 $$d\x_i/\x_i$$는 $$\x_i = 0$$을 따라 정확히 1차 pole을 갖는 logarithmic form이다 ($$i \le k$$인 경우). $$i > k$$인 경우에는 $$\x_i \in \mathcal{O}_{U_\sigma}^\ast$$이므로 $$d\x_i/\x_i$$는 $$U_\sigma$$ 위에서 regular하다. 따라서 $$d\log(\rchi^m) \in \Omega^1(\log D)(U_\sigma)$$.

이로부터 자연스러운 $$\mathcal{O}_{X_\Sigma}$$-module map

$$\Phi: M \otimes_\mathbb{Z} \mathcal{O}_{X_\Sigma} \longrightarrow \Omega^1_{X_\Sigma}(\log D); \qquad m \otimes 1 \longmapsto d\log(\rchi^m)$$

이 얻어진다. 이것이 isomorphism인 것은 각 $$U_\sigma$$ 위에서 확인하면 되는데, 위의 좌표에서 $$U_\sigma$$ 위의 $$\Omega^1(\log D)$$의 $$\mathcal{O}_{U_\sigma}$$-module 기저는 정확히 $$\{d\x_i/\x_i\}_{i=1}^k \cup \{d\x_j\}_{j=k+1}^n$$이며 ($$\x_j$$가 invertible이므로 $$d\x_j$$와 $$d\x_j/\x_j$$는 $$\mathcal{O}_{U_\sigma}^\ast$$ 배만큼 차이가 나며 같은 free module을 span한다), 이는 $$\{d\log \rchi^{v_i^\ast}\}_{i=1}^n$$과 동일하다. 따라서 $$\Phi$$는 각 affine chart 위에서 free $$\mathcal{O}_{U_\sigma}$$-module 사이의 동형이고, 이로부터 global isomorphism이 따라온다.

</details>

이 명제는 두 가지 측면에서 매우 강한 결과이다. 첫째, [정의 6](#def6)의 logarithmic cotangent sheaf $$\Omega^1_X(\log D)$$는 일반적인 SNC pair $$(X, D)$$에 대해서는 결코 trivial bundle이 되지 않는다. Toric variety의 경우에만 boundary $$D$$가 character lattice $$M$$ 전체의 정보를 정확히 흡수해주어 $$\Omega^1(\log D)$$가 rank $$n$$의 trivial bundle이 되는 것이며, 이는 fan의 ray 구조가 $$M$$의 전 정보를 결정한다는 toric duality의 또 다른 표현이라 할 수 있다.

둘째, 비교를 위해 $$\Omega^1_{X_\Sigma}$$ 자체를 보면 가령 $$X_\Sigma = \mathbb{P}^n$$의 경우 Euler sequence

$$0 \to \Omega^1_{\mathbb{P}^n} \to \mathcal{O}_{\mathbb{P}^n}(-1)^{\oplus(n+1)} \to \mathcal{O}_{\mathbb{P}^n} \to 0$$

으로부터 $$\Omega^1_{\mathbb{P}^n}$$이 trivial bundle이 아니라는 것을 안다. ([\[대수다양체\] §표준선다발, ⁋명제 7](/ko/math/algebraic_varieties/canonical_bundle#prop7)) 실제로 $$\Gamma(\mathbb{P}^n, \Omega^1_{\mathbb{P}^n}) = 0$$임이 알려져 있는데도, $$\log D$$ twist를 가한 $$\Omega^1_{\mathbb{P}^n}(\log D)$$는 위 명제에 의해 trivial bundle 즉 $$\mathcal{O}_{\mathbb{P}^n}^{\oplus n}$$이 되어 $$n$$차원의 global section 공간을 가진다. 이러한 극적인 변화가 정확히 boundary $$D = \sum D_\rho$$에 "logarithmic" 정보를 허용한 대가이다.

<div class="example" markdown="1">

<ins id="ex9">**예시 9**</ins> $$X_\Sigma = \mathbb{P}^1$$의 경우, fan은 $$N = \mathbb{Z}$$에서 두 ray $$\rho_+ = \mathbb{R}_{\ge 0} \cdot 1$$과 $$\rho_- = \mathbb{R}_{\ge 0} \cdot (-1)$$로 이루어지며 boundary는 $$D = D_{\rho_+} + D_{\rho_-} = \{0\} + \{\infty\}$$이다. $$M = \mathbb{Z}$$의 generator $$1 \in M$$에 대해 $$\rchi^1 = \x$$가 $$\mathbb{P}^1$$의 standard inhomogeneous 좌표이며

$$d\log \x = \frac{d\x}{\x}$$

는 $$\x = 0$$과 $$\x = \infty$$ 양쪽에서 1차 pole만을 가지는 logarithmic form이다 ($$\x = \infty$$ 근방에서는 $$\y = 1/\x$$로 좌표를 잡으면 $$d\x/\x = -d\y/\y$$이므로 logarithmic pole임이 확인된다). [명제 8](#prop8)이 주장하는 바는 $$\Omega^1_{\mathbb{P}^1}(\log D) \cong \mathcal{O}_{\mathbb{P}^1}$$이 $$d\x/\x$$를 generator로 갖는 trivial bundle이라는 것이며, 이는 $$\Omega^1_{\mathbb{P}^1} \cong \mathcal{O}_{\mathbb{P}^1}(-2)$$가 *not* trivial인 것과 비교된다.

</div>

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> $$X_\Sigma = \mathbb{P}^n$$의 경우 fan은 $$N = \mathbb{Z}^n$$의 standard 기저 $$e_1, \ldots, e_n$$과 $$e_0 = -e_1 - \cdots - e_n$$의 $$n+1$$개 ray로 이루어진다. 각 $$e_i$$에 대응하는 divisor를 $$D_i$$라 하면 boundary는 $$D = D_0 + D_1 + \cdots + D_n$$이고 $$[D_0] = [D_1] = \cdots = [D_n] = H$$이므로 $$D \sim (n+1) H$$이다. $$M$$의 standard 기저 $$e_1^\ast, \ldots, e_n^\ast$$에 대해 $$\rchi^{e_i^\ast} = \x_i$$ ($$1 \le i \le n$$)가 affine 좌표가 되어

$$\Omega^1_{\mathbb{P}^n}(\log D) \cong \mathcal{O}_{\mathbb{P}^n}^{\oplus n};\qquad \text{기저: } \frac{d\x_1}{\x_1}, \ldots, \frac{d\x_n}{\x_n}$$

이 된다. 한편 $$e_0$$에 대응하는 ray의 $$d\log$$인 $$d\log(\rchi^{-e_1^\ast - \cdots - e_n^\ast}) = -\sum_i d\x_i / \x_i$$가 위의 $$n$$개 기저의 음의 합으로 자동적으로 표현되는 것은 fan의 ray가 $$M$$의 rank를 초과해도 $$M$$ 자체가 결국 모든 logarithmic form들을 매개하는 것의 한 단면이다.

</div>

<div class="example" markdown="1">

<ins id="ex11">**예시 11**</ins> $$X_\Sigma = \mathbb{P}^1 \times \mathbb{P}^1$$의 경우 $$N = \mathbb{Z}^2$$이고 fan은 네 개의 ray $$\pm e_1, \pm e_2$$와 네 개의 maximal cone으로 이루어진다. Boundary는 네 boundary divisor의 합이며, $$M = \mathbb{Z}^2$$의 standard 기저에 대해

$$\Omega^1_{\mathbb{P}^1 \times \mathbb{P}^1}(\log D) \cong \mathcal{O}^{\oplus 2};\qquad \text{기저: } \frac{d\x}{\x}, \frac{d\y}{\y}$$

이 된다. Künneth 분해

$$\Omega^1_{\mathbb{P}^1 \times \mathbb{P}^1}(\log D) = \pr_1^\ast \Omega^1_{\mathbb{P}^1}(\log D_{\mathbb{P}^1}) \oplus \pr_2^\ast \Omega^1_{\mathbb{P}^1}(\log D_{\mathbb{P}^1})$$

와 [예시 9](#ex9)과 비교하면 두 인자가 정확히 $$d\x/\x$$, $$d\y/\y$$를 기여함을 알 수 있다.

</div>

<div class="remark" markdown="1">

<ins id="rmk12">**참고 12**</ins> [명제 8](#prop8)은 smooth toric variety를 가정하였다. $$X_\Sigma$$가 simplicial이지만 smooth가 아닌 경우에도 $$\mathbb{Q}$$-Cartier 수준에서 비슷한 진술이 성립하며, 더 일반적인 normal toric variety에 대해서는 *Zariski differentials* $$\widehat{\Omega}^1_{X_\Sigma}(\log D)$$를 사용하면 동일한 fan-theoretic 묘사가 가능하다. 자세한 논의는 Cox-Little-Schenck의 §8.1–8.2 참고.

</div>

## 표준 인자의 fan-이론적 공식

[명제 8](#prop8)의 즉각적인 귀결로, top form $$\omega_\Sigma := \bigwedge_i d\log(\rchi^{m_i})$$가 $$X_\Sigma$$ 위의 $$\Omega^n_{X_\Sigma}(\log D)$$의 nowhere-vanishing global section이 되는 것을 알 수 있다. 이 형식은 정확히 canonical bundle의 정보와 연결되며, 이를 통해 [§파노 다양체, ⁋명제 3](/ko/math/toric_geometry/reflexive_polytope_fano#prop3)에서 이미 진술된 $$K_{X_\Sigma} = -\sum_\rho D_\rho$$를 fan으로부터 직접 유도할 수 있다.

<div class="proposition" markdown="1">

<ins id="prop13">**명제 13**</ins> Smooth toric variety $$X_\Sigma$$에 대해, $$M$$의 임의의 $$\mathbb{Z}$$-기저 $$m_1, \ldots, m_n$$를 잡으면 top form

$$\omega_\Sigma := d\log(\rchi^{m_1}) \wedge \cdots \wedge d\log(\rchi^{m_n}) \in \Omega^n(X_\Sigma)(\log D)$$

는 $$\Omega^n_{X_\Sigma}(\log D)$$의 nowhere-vanishing global section이며, 기저 선택에 대해 부호를 제외하고 canonical하다. 따라서

$$\Omega^n_{X_\Sigma}(\log D) \cong \mathcal{O}_{X_\Sigma};\qquad K_{X_\Sigma} = -\sum_{\rho \in \Sigma(1)} D_\rho$$

가 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[명제 8](#prop8)에서 $$\Omega^1_{X_\Sigma}(\log D) \cong M \otimes \mathcal{O}_{X_\Sigma}$$이므로 $$\Omega^n_{X_\Sigma}(\log D) \cong \bigwedge^n (M \otimes \mathcal{O}) \cong (\bigwedge^n M) \otimes \mathcal{O} \cong \mathcal{O}_{X_\Sigma}$$이며 ($$M$$이 rank $$n$$의 free abelian group이므로 $$\bigwedge^n M \cong \mathbb{Z}$$이다), 그 generator는 정확히 $$\omega_\Sigma$$이다. $$M$$의 기저를 바꾸면 $$\GL_n(\mathbb{Z})$$의 변환에 의해 $$\omega_\Sigma$$가 $$\det \in \{\pm 1\}$$배만 변하므로 canonical하다.

이제 $$K_{X_\Sigma}$$를 계산하기 위해, $$\omega_\Sigma$$를 $$\Omega^n_{X_\Sigma}$$의 rational section으로 봐서 $$\divisor(\omega_\Sigma)$$를 계산한다. Smooth ray $$\rho \in \Sigma(1)$$에 대해 $$\rho$$를 face로 갖는 maximal cone $$\sigma$$를 잡고 (smooth가정에 의해 $$\sigma$$의 ray들이 $$N$$의 기저 $$v_1, \ldots, v_n$$의 일부를 이루며 $$v_\rho = v_1$$이라 할 수 있다), 그 dual 기저 $$\{v_1^\ast, \ldots, v_n^\ast\} \subset M$$를 $$M$$의 기저 $$m_i$$로 잡자. 그럼 $$U_\sigma$$ 위에서 $$\rchi^{v_i^\ast} = \x_i$$이고 $$D_\rho \cap U_\sigma = \{\x_1 = 0\}$$이며

$$\omega_\Sigma\vert_{U_\sigma} = \frac{d\x_1}{\x_1} \wedge \frac{d\x_2}{\x_2} \wedge \cdots \wedge \frac{d\x_n}{\x_n}$$

이다. $$\Omega^n_{X_\Sigma}$$의 local trivialization $$d\x_1 \wedge \cdots \wedge d\x_n$$과 비교하면

$$\omega_\Sigma\vert_{U_\sigma} = \frac{1}{\x_1 \x_2 \cdots \x_n} \cdot d\x_1 \wedge \cdots \wedge d\x_n$$

이므로 $$\omega_\Sigma$$는 $$U_\sigma$$ 위에서 정확히 $$D_\rho$$ (즉 $$\{\x_1 = 0\}$$)를 따라 1차 pole을 갖는다. $$\sigma$$가 face로 갖지 않는 다른 ray $$\rho'$$에 대해서는 $$U_\sigma$$가 $$D_{\rho'}$$와 만나지 않으므로 $$U_\sigma$$ 위의 $$\omega_\Sigma$$의 vanishing order는 0이다. 모든 ray $$\rho \in \Sigma(1)$$에 걸쳐 종합하면

$$\divisor(\omega_\Sigma) = -\sum_{\rho \in \Sigma(1)} D_\rho.$$

$$\Omega^n_{X_\Sigma}$$는 $$\omega_X = \mathcal{O}(K_X)$$이므로 ([\[대수다양체\] §표준선다발, ⁋정의 6](/ko/math/algebraic_varieties/canonical_bundle#def6)) 위 식이 곧 $$K_{X_\Sigma} = -\sum_\rho D_\rho$$이다.

</details>

위 명제는 $$\omega_\Sigma$$의 두 가지 관점을 동시에 보여준다. 첫째, *log* divisor를 허용하면 ($$\Omega^n(\log D)$$에서 보면) $$\omega_\Sigma$$는 nowhere-vanishing이며 따라서 $$\Omega^n_{X_\Sigma}(\log D) = \mathcal{O}_{X_\Sigma}$$이다. 둘째, 원래의 $$\Omega^n_{X_\Sigma}$$로 내려가면 $$\omega_\Sigma$$가 boundary $$D$$를 따라 정확히 1차 pole을 갖는 rational section이며, 이로부터 $$\Omega^n_{X_\Sigma}(D) \cong \mathcal{O}_{X_\Sigma}$$, 즉 $$K_{X_\Sigma} + D \sim 0$$임이 따라온다. 이는 [§파노 다양체, ⁋명제 3](/ko/math/toric_geometry/reflexive_polytope_fano#prop3)에서 이미 진술된 anticanonical 공식의 정밀한 fan-이론적 출처이다.

## Calabi-Yau hypersurface 위의 Poincaré residue

[명제 13](#prop13)의 $$\omega_\Sigma$$가 갖는 또 하나의 핵심적 응용은 anticanonical hypersurface 위의 자연스러운 holomorphic volume form 구성이다. $$X_\Sigma$$가 Gorenstein Fano toric variety라 가정하고, $$f \in H^0(X_\Sigma, \mathcal{O}(-K_{X_\Sigma}))$$를 anticanonical section이라 하자. 그럼 $$Y := \{f = 0\} \subset X_\Sigma$$는 $$-K_{X_\Sigma}$$ linear system 내의 hypersurface이며, [§파노 다양체, ⁋명제 7](/ko/math/toric_geometry/reflexive_polytope_fano#prop7)의 adjunction에 의해 $$Y$$가 smooth이면 $$K_Y = 0$$, 즉 Calabi-Yau hypersurface가 된다.

이 경우 *Poincaré residue* 

$$\Res_Y\!\left(\frac{\omega_\Sigma}{f}\right) \in H^0(Y, \omega_Y)$$

가 정의되며, 이것이 $$Y$$ 위의 nowhere-vanishing canonical volume form을 정의한다. 핵심은 $$\omega_\Sigma$$가 [명제 13](#prop13)에 의해 $$\divisor(\omega_\Sigma) = -D$$를 가지므로, $$f$$가 anticanonical, 즉 $$\divisor(f) \sim D$$인 한 $$\omega_\Sigma / f$$가 $$Y$$를 따라 정확히 1차 pole을 갖는 rational $$n$$-form이라는 점이다. Residue map은 이러한 simple pole form을 hypersurface 위의 holomorphic $$(n-1)$$-form으로 떨어뜨려준다.

즉 logarithmic differential의 toric variety 위에서의 자연스러움이 곧 Calabi-Yau hypersurface의 정준 volume form의 자연스러움으로 직접 변환된다.

---

**참고문헌**

**[CLS]** D. A. Cox, J. B. Little, H. K. Schenck, *Toric Varieties*, Graduate Studies in Mathematics 124, AMS, 2011. (Chapter 8: differential forms on toric varieties; §8.1–8.2에서 $$\Omega^1(\log D)$$의 위 trivialization을 자세히 다룬다.)

**[Oda]** T. Oda, *Convex Bodies and Algebraic Geometry: An Introduction to the Theory of Toric Varieties*, Springer, 1988.
