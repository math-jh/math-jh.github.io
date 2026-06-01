---
title: "Givental J-function과 Mirror Theorem"
description: "기본 정의에서 출발해 양자미분방정식의 기본해로서의 성질을 증명하고, 토릭 파노 다양체의 명시적 hypergeometric 함수와 거울 정리의 관계까지 다룬다."
excerpt: "Quantum differential equation의 fundamental solution과 I=J 정리"

categories: [Math / Mirror Symmetry]
permalink: /ko/math/mirror_symmetry/givental_j_function
sidebar: 
    nav: "mirror_symmetry-ko"

header:
    overlay_image: /assets/images/Math/Mirror_Symmetry/Givental_J_Function.png
    overlay_filter: 0.5

date: 2026-05-28
last_modified_at: 2026-05-28
weight: 6

published: false
---

[§두브로빈 접속, §§D-module](/ko/math/mirror_symmetry/dubrovin_connection#d-module)에서 우리는 quantum cohomology 측의 quantum differential equation (QDE)이 해 공간으로 $$\dim_\mathbb{C} H^\ast(X)$$ 차원의 flat section을 가짐을 보였고, 그 fundamental solution을 명시적으로 적은 것이 *Givental의 $$J$$-function*이라 예고했었다. 한편 [§가우스-마닌 접속, ⁋명제 7](/ko/math/mirror_symmetry/gauss-manin_connection#prop7)에서는 B-side에서 period matrix $$\mathcal{I}^a_p$$가 B-model connection $$\nabla^z_B$$의 fundamental solution matrix를 이루는 것을 살펴보았다. 우리가 예고했던 mirror theorem은 결국 A-side의 $$J$$-function과 B-side의 period matrix가 동일한 $$D$$-module의 fundamental solution이라는 statement로 구체화될 것이며, 이번 글이 그 주장에서 비어있는 A-side 자리를 채울 것이다.

## Descendant Gromov-Witten invariant

$$J$$-function의 정의를 시작하기 전에, 본 글 전반에서 사용할 *descendant* invariant ([\[사교기하학\] §Gromov-Witten 불변량, ⁋정의 2](/ko/math/symplectic_geometry/gromov_witten#def2))를 본 글의 표기에 맞춰 짧게 정리해 두자. Genus $$0$$, $$(n+1)$$-marked, class $$\beta$$의 stable map의 moduli space 

$$\overline{\mathcal{M}}_{0, n+1}(X, \beta)$$

위에는 각 marked point $$i$$에서의 evaluation map $$\ev_i: \overline{\mathcal{M}}_{0, n+1}(X, \beta) \to X$$와 universal cotangent line bundle $$\mathbb{L}_i$$가 정의된다. 직관적으로 $$\mathbb{L}_i$$는 $$i$$번째 marked point들에서의 cotangent line을 moduli space 위에서 붙여준 것이며, 이 때 이 universal cotangent line bundle의 first Chern class

$$\psi_i := c_1(\mathbb{L}_i) \in H^2(\overline{\mathcal{M}}_{0, n+1}(X, \beta))$$

를 *$$\psi$$-class*라 부른다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1 (Descendant Gromov-Witten invariant)**</ins> 임의의 cohomology class $$\gamma_i \in H^\ast(X)$$와 $$k_i \geq 0$$에 대해 *descendant Gromov-Witten invariant*는

$$\left\langle \tau_{k_1}(\gamma_1), \ldots, \tau_{k_{n+1}}(\gamma_{n+1})\right\rangle_{0, n+1, \beta} := \int_{[\overline{\mathcal{M}}_{0, n+1}(X, \beta)]^{\mathrm{vir}}} \prod_{i=1}^{n+1} \psi_i^{k_i} \smile \ev_i^\ast \gamma_i$$

로 정의된다. $$k_i = 0$$인 경우 *primary* invariant, 적어도 하나의 $$k_i \geq 1$$이면 *gravitational descendant*라 부른다.

</div>

Moduli space를 다루며 언어에 약간의 업그레이드가 있기는 하지만, 본질적으로 stack의 Chern class도 직관적인 의미는 일반적인 line bundle의 Chern class와 같다. 즉, $$\mathbb{L}_i$$가 moduli space 위에서 얼마나 꼬여있는지를 측정한 양이다. 더 구체적으로, moduli base의 $$2$$-cycle $$\Sigma$$가 주어졌다 하면 $$\psi_i$$가 이 cycle과 pairing을 통해 주는 양

$$\int_\Sigma \psi_i\in \mathbb{Z}$$

은 $$\Sigma$$를 따라 $$\mathbb{L}_i$$를 한 바퀴 돌리면 이것이 얼마만큼 꼬여서 원래의 fiber와 붙는지, 즉 monodromy action을 보는 것과 같다. 가장 단순한 경우 이 값이 $$1$$인 것은 $$\Sigma$$ 위로 restrict한 $$\mathbb{L}_i$$의 degree가 $$1$$이라는 의미이며, 더 직관적으로 우리는 $$\Sigma$$ 위의 가상의 한 점을 지날 때마다 phase factor, 즉 monodromy가 그 한 점에 응축된 것으로 해석할 수 있다. 물론 이 한 점을 택하는 것은 자유도가 있지만, 이는 정확히 $$\psi_i$$의 cohomology class의 representative를 택하는 것에서 나오는 것이며 따라서 더 일반적으로 $$\int_\Sigma\psi_i$$가 $$n$$이라는 것은 이러한 $$n$$개의 점을 배치해두는 것과 같다. 

잘 알려진 사실은 이들 $$n$$개의 점이 사실은 moduli space의 boundary divisor, 즉 source curve의 degeneration이 일어나는 곳들과 $$\Sigma$$의 intersection이 일어나는 곳으로 생각할 수 있다는 것이며, 이로써 $$\psi_i$$는 source curve의 degeneration에 대한 정보를 담고 있는 것으로 생각할 수 있다.

그럼 [정의 1](#def1)의 $$\psi_i^{k_i}$$ 성분들이 source curve의 degeneration을, $$\ev_i^\ast\gamma_i$$가 target의 incidence condition을 각각 결정한다는 것은 자명하다. 특히 나중 조건은 $$i$$번째 marked point $$p_i$$의 image가 $$\gamma_i$$를 지난다는 조건이다. 그러나 첫째 조건은 다소 덜 직관적이므로 이 의미를 풀어 살펴보자. 

우리는 앞서 $$\psi_i$$가 본질적으로는 source curve의 degeneration들의 합으로 나타날 수 있음을 보았다. 더 구체적으로, source curve가 marked point $$1,\ldots, n$$을 두 개의 component $$S$$, $$S^c$$로 쪼개며 degenerate한다 하고, 이에 대응되는 boundary divisor를 $$D_S$$라 하자. 여기서 우리는 $$i\in S$$인 것으로 두며, $$i$$가 속한 component를 *tail*이라 부른다. 이 때, $$\mathbb{P}^1$$을 stable하게 만들기 위해서는 세 점이 필요하므로 $$S$$와 $$S^c$$ 모두 두 점 이상이어야 한다. 

직관적으로 $$\psi_i$$는 이러한 방식으로 생기는 boundary divisor들의 합 $$\sum_{i\in S} D_S$$처럼 생각할 수 있지만, 이대로 두면 같은 cohomology class가 여러 번 세게 되므로 redundancy를 제거하는 reference choice가 필요하다. 즉, $$j,k$$를 고정하고, $$S^c$$에 해당하는 component를 $$j,k$$와 nodal point로 이쪽 $$\mathbb{P}^1$$의 automorphism을 죽여주어야 한다. 

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2 (Genus 0 Topological Recursion Relation)**</ins> $$\{1, \ldots, n\}$$ ($$n\geq 4$$)의 고정된 세 index $$i,j,k$$에 대하여, $$\psi$$-class $$\psi_i$$는 다음 boundary divisor들의 합

$$\psi_i=\sum_{\substack{S \subset \{1, \ldots, n\} \\ i \in S, j, k \notin S, \lvert S\rvert \geq 2}} D_S \in H^2(\overline{\mathcal{M}}_{0, n})$$

으로 나타난다.

</div>

그럼 target $$X$$가 주어진 stable map의 moduli space $$\overline{\mathcal{M}}_{0, n}(X, \beta)$$에서도 forgetful morphism $$\overline{\mathcal{M}}_{0, n}(X, \beta) \to \overline{\mathcal{M}}_{0, n}$$의 pullback을 통해 위의 공식을 옮겨줄 수 있다. 

이제 $$\psi_i^{k_i}$$를 더 명확하게 이해할 수 있다. 위의 관점에 따르면, $$\psi_i^{k_i}$$는 단지 marked point $$p_i$$에 해당하는 부분이 $$k_i$$번 degenerate해서 tail에 속하는 degenerate cycle을 의미하는 것으로, 이를 종합하면 descendant GW invariant는 *target incidence*와, *source의 depth-$$k_i$$ tail degeneration*의 두 조건을 동시에 만족하는 stable map의 virtual counting으로 생각할 수 있다. 

이제 이러한 gravitational invariant들을 한 번에 고려하기 위해 우리는 formal한 geometric series

$$\frac{1}{z - \psi} = \frac{1}{z}\cdot\frac{1}{1 - \psi/z} = \sum_{k \geq 0} z^{-k-1}\psi^k$$

를 생각한다. 가령, $$\psi$$ class를 마지막 factor에만 끼워넣으면

$$\begin{aligned}\left\langle \gamma_1, \ldots, \gamma_n, \frac{\gamma_{n+1}}{z - \psi}\right\rangle_{0, n+1, \beta}&=\left\langle \gamma_1, \ldots, \gamma_n, \sum_{k \geq 0} z^{-k-1}\psi^k\gamma_{n+1}\right\rangle_{0, n+1, \beta}=\sum_{k\geq 0}z^{-k-1}\left\langle \gamma_1, \ldots, \gamma_n, \psi^k\gamma_{n+1}\right\rangle_{0, n+1, \beta}\\&=\sum_{k \geq 0} z^{-k-1} \left\langle \gamma_1, \ldots, \gamma_n, \tau_k(\gamma_{n+1})\right\rangle_{0, n+1, \beta}\end{aligned}$$

으로, 각 depth $$k$$의 descendant invariant가 $$z^{-k-1}$$ coefficient로 분리되어 한 번에 잡힌다. 일차적으로 이는 우변의 무한합을 담는 것이지만, 다음 절에서 $$J$$-function을 도입하면 우변의 $$z$$까지도 특정한 의미를 담게 되는 것을 확인할 수 있다. 

## $$J$$-function의 도입

이제 앞서 살펴본 gravitational invariant들을 사용하여 $$J$$-function을 도입한다. Smooth projective variety $$X$$, $$H^\ast(X, \mathbb{C})$$의 homogeneous basis $$\{ T_a \}_{a=0,\ldots,s}$$ ($$T_0 = 1$$), 그리고 이들이 주는 Poincaré dual basis $$\{ T^a \}$$를 생각하자. 이 중 $$H^2$$ 성분을 차지하는 부분을 (notation 단순화를 위해) $$\{ T_a \}_{a=1,\ldots,r}$$로 잡으면, [§두브로빈 접속, §§D-module](/ko/math/mirror_symmetry/dubrovin_connection#d-module)에서 도입한 flat coordinate $$t^a$$와 Novikov variable $$q_a := e^{t^a}$$ ($$a = 1, \ldots, r$$)가 정의된다. 편의상 

$$t_{(2)} := \sum_{b=1}^r t^b T_b$$

라 두면 $$q^\beta = e^{t_{(2)} \cdot \beta}$$이다. 한편 Dubrovin connection은 다음의 식

$$\nabla^z = \partial + z^{-1}\mathcal{C}$$

으로 정의되었는데, 이번 글에서 우리는 oscillating integral 쪽과 부호를 맞추기 위해 그 *dual Dubrovin connection*

$$\nabla^{z, \vee} := -\nabla^{-z} = \partial - z^{-1}\mathcal{C}$$

과 이 connection의 horizontal section equation

$$z q_a\partial_{q_a} s = T_a \qtimes s \qquad (a = 1, \ldots, r)\tag{$\ast$}$$

을 고려하기로 한다. 

이 방정식의 해를 구하기 위해 우선 $$z\rightarrow \infty$$인 상황을 보자. 그럼 $$z\rightarrow\infty$$일 때 $$z^{-1}\mathcal{C}$$ 항이 사라지면서 standard differential $$\partial$$로 degenerate하며, 따라서 ($$\ast$$)의 leading-order horizontal section은 $$\partial$$의 horizontal section, 즉 $$q$$에 무관한 constant section이 된다. 더 일반적으로, $$z\rightarrow \infty$$인 limit에서 사라지는 solution은

$$s=s_0+\frac{s_1}{z}+\frac{s_2}{z^2}+\cdots$$

의 꼴일 것이며, 위의 계산에서 $$0$$차항 $$s_0$$은 constant section으로 두면 된다는 것을 보았으므로 다음 꼴

$$s=1+\frac{s_1}{z}+\frac{s_2}{z^2}+\cdots$$

을 ($$\ast$$)에 직접 대입하면 recursive하게 $$s_i$$들을 구할 수 있다. 구체적으로, ($$\ast$$)의 양변을 $$z$$의 거듭제곱별로 정리하면, 좌변은 $$s_0$$이 상수이므로

$$z \cdot \sum_k z^{-k} q_a\partial_{q_a} s_k = \sum_k z^{-k} q_a\partial_{q_a} s_{k+1}$$

이고, 우변은 $$\sum_k z^{-k} T_a\qtimes s_k$$이므로 각각의 $$z^{-k}$$ 계수를 비교하여 일반적인 recursion

$$q_a\partial_{q_a} s_{k+1} = T_a \qtimes s_k \qquad (a = 1, \ldots, r, k \geq 0)$$

을 얻는다. 

Recursion의 첫 단계에 해당하는 $$k = 0$$에서는 $$T_a \qtimes 1 = T_a$$이므로, 별다른 quantum correction 없이 $$q_a\partial_{q_a} s_1 = T_a$$이 성립한다. 이제 양변을 $$q_a$$에 대해 적분하면

$$s_1=t_{(2)} + C_1,\qquad C_1\in H^\ast(X)$$

가 된다. 흥미로운 부분은 quantum correction이 처음 등장하는 $$k=1$$인데, recursion formula

$$q_a\partial_{q_a} s_2 = T_a \qtimes t_{(2)}=T_a\qtimes \left(\sum_{b=1}^r t^b T_b\right)$$

를 생각하면 이제 우변은 classical cup product $$T_a\smile t_{(2)}$$에 추가적으로 quantum correction

$$\sum_{\beta \neq 0} q^\beta \sum_c \left(\sum_{b=1}^r t^b \langle T_a, T_b, T^c\rangle_{0, 3, \beta}\right) T_c$$

부분을 갖는다. 한편 $$T_b \in H^2$$이므로 [\[사교기하학\] §Gromov-Witten 불변량, ⁋명제 4](/ko/math/symplectic_geometry/gromov_witten#prop4)의 결과

$$\langle T_a, T_b, T^c\rangle_{0, 3, \beta} = (T_b \cdot \beta)\langle T_a, T^c\rangle_{0, 2, \beta}$$

을 적용하면 다음의 식

$$T_a \qtimes t_{(2)} = T_a \smile t_{(2)} + \sum_{\beta \neq 0} q^\beta (t_{(2)} \cdot \beta) \sum_c \langle T_a, T^c\rangle_{0, 2, \beta} T_c$$

을 얻는다. 이제 이를 $$q_a$$에 대해 적분하자. Classical 부분 $$T_a \smile t_{(2)}$$의 antiderivative는 $$(t_{(2)})^2/2$$인데, 이는 $$q_a\partial_{q_a} = \partial_{t^a}$$임을 이용하여

$$\partial_{t^a}\bigl((t_{(2)})^2/2\bigr) = \partial_{t^a}\!\left(\frac{1}{2}\sum_{b, c} t^b t^c T_b \smile T_c\right) = \sum_c t^c T_a \smile T_c = T_a \smile t_{(2)}$$

로 직접 확인된다. Quantum 부분의 antiderivative는 $$q^\beta = e^{t_{(2)}\cdot \beta}$$로부터 오는 관계 $$q_a\partial_{q_a} q^\beta = (T_a \cdot \beta) q^\beta$$을 이용해 $$\beta$$별로 풀어내면, 각 $$\beta$$에 대해 $$q^\beta$$ 인자와 *primary* GW invariant ($$\psi$$-class 삽입 없는 descendant invariant) $$\langle T_a, T^c\rangle_{0, 2, \beta}$$로 결정되는 $$H^\ast(X)$$-valued correction으로 정리되며, 따라서 $$s_2$$는 classical $$(t_{(2)})^2/2$$와 이 quantum correction의 합이 된다. 더 높은 $$z^{-k}$$ ($$k \geq 2$$) 차수에서는 같은 recursion을 따라 $$\tau_{k-1}(T_a)$$ 형태의 *gravitational descendant*가 차례로 누적되며, $$J$$-function은 결국 이렇게 강제되는 fundamental solution을 한 줄로 명시적으로 적은 것이다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> $$X$$의 (small) *Givental $$J$$-function<sub>Givental J-함수</sub>* $$J_X: (\mathbb{C}^\ast)^r \times \mathbb{C}^\ast \to H^\ast(X)$$는 다음으로 정의된다.

$$J_X(q, z) := e^{t_{(2)}/z}\left( 1 + \sum_{\substack{\beta \in H_2(X, \mathbb{Z})_{\mathrm{eff}} \\ \beta \neq 0}} \sum_{a=0}^s q^\beta \left\langle \frac{T_a}{z(z - \psi)} \right\rangle_{0, 1, \beta} T^a \right)$$

</div>

여기서 $$H_2(X, \mathbb{Z})_{\mathrm{eff}}$$는 effective curve class들의 집합 ([\[사교기하학\] §양자 코호몰로지, §§Novikov ring](/ko/math/symplectic_geometry/quantum_cohomology#novikov-ring)에서 정의)으로, $$\beta$$가 이 위를 달리며 각 $$\beta \neq 0$$이 차수 $$q^\beta$$의 instanton 보정에 기여한다.

앞서 우리는 다음의 식

$$\left\langle \gamma_1, \ldots, \gamma_n, \frac{\gamma_{n+1}}{z - \psi}\right\rangle_{0, n+1, \beta}=\sum_{k \geq 0} z^{-k-1} \left\langle \gamma_1, \ldots, \gamma_n, \tau_k(\gamma_{n+1})\right\rangle_{0, n+1, \beta}$$

을 이미 검증했으므로, 위의 $$J$$-function은 다음의 꼴

$$J_X(q, z) = e^{t_{(2)}/z}\left(\mathbf{1} + \sum_{\substack{\beta \in H_2(X, \mathbb{Z})_{\mathrm{eff}} \\ \beta \neq 0}}\sum_{a = 0}^s \sum_{k \geq 0} q^\beta z^{-k-2} \langle\tau_k(T_a)\rangle_{0, 1, \beta} T^a\right)$$

로 풀어 적을 수 있다. 따라서, 이 함수는 본질적으로 single marked point descendant invariant

$$\bigl\{\langle\tau_k(T_a)\rangle_{0, 1, \beta}\bigr\}_{\beta \in H_2(X, \mathbb{Z})_{\mathrm{eff}} \setminus \{0\}, a = 0, \ldots, s, k \geq 0}$$

들을 Novikov parameter $$q^\beta$$, spectral parameter $$z^{-k-2}$$와 cohomology의 basis element들 $$T^a$$에 붙여서 만든 generating function으로 생각할 수 있다. 

일반적으로 우리가 위에서 정의한 descendant invariant들은 multi-marked point

$$\left\langle \tau_{k_1}(\gamma_1), \ldots, \tau_{k_{n+1}}(\gamma_{n+1})\right\rangle_{0, n+1, \beta}$$

의 형태이지만, 위에서 우리는 single marked point들만 식에 넣었음을 유의하자. 이것이 가능한 이유는 $$\beta\neq 0$$이므로 source의 stability와 관계없이 target이 충분히 크므로 stability가 보장되기 때문이며, 이들만 보는 것으로 충분한 이유는 본질적으로 우리가 $$H^2$$ 방향 deformation, 즉 small quantum cohomology를 우선적으로 생각하기 때문이다. 

더 구체적으로, 우리는 이미 [\[사교기하학\] §Gromov-Witten 불변량, ⁋명제 4](/ko/math/symplectic_geometry/gromov_witten#prop4)로부터 Gromov-Witten invariant에 divisor $$D\in H^2(X)$$를 insert하는 것이 $$D\cdot \beta$$를 곱하는 효과로 나타남을 보았고, 이를 power series로 전개하면 결국 $$H^2$$ 방향을 보는 것은 $$e^{t_{(2)}\cdot \beta}$$를 앞에 곱하는 것, 즉 Novikov variable을 $$q^\beta \mapsto e^{t_{(2)}\cdot \beta}q^\beta$$로 재매개화하는 것에 지나지 않는다는 것을 살펴보았다. [정의 3](#def3)에서 우리는 여기에 더해 $$T_a/(z-\psi)$$ 항에 $$z^{-1}$$을 한 번 더 곱해주었으므로,[^1] 이 $$z$$-shift까지 반영하면 $$J$$-function 앞에 전체적으로 붙는 factor는 $$e^{t_{(2)}/z}$$가 된다. 이렇게 $$H^2$$ 방향의 의존성을 전부 $$e^{t_{(2)}/z}$$와 Novikov variable에 넣고 나면 Gromov-Witten 정보는 남은 하나의 marked point에 응축되므로, single marked point invariant만 보아도 충분하다. 

한편 $$J$$-function을 도입한 우리의 동기는 QDE ($$\ast$$)의 fundamental solution을 구하기 위함이었다는 것을 기억하자. [§두브로빈 접속, §§D-module](/ko/math/mirror_symmetry/dubrovin_connection#d-module)에서 우리는 A-model $$D$$-module이 base $$M_A = (\mathbb{C}^\ast)^r \times \mathbb{C}^\ast_z$$의 각 점 $$(q, z)$$마다 fiber로 $$H^\ast(X)$$를 얹은 bundle이고, 그 위의 connection 1-form $$\mathcal{C}_a = T_a \qtimes -$$ 또한 이 fiber 위의 endomorphism이었음을 보았으며, 이것의 해가 곧 ($$\ast$$)의 horizontal section이었다. 이들 해들은 $$\dim_\mathbb{C}H^\ast(X)$$차원이며, 만일 우리가 $$T_a$$들을 초기값으로 주고 이 방정식을 풀면 정확히 해들 전부가 나온다. 이 과정을 통해 우리는 다음의 fundamental solution matrix를 얻는다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4 (A-side fundamental solution matrix)**</ins> Endomorphism $$S(q, z) \in \End(H^\ast(X))$$를 다음의 matrix element

$$\eta\bigl(S(q,z)T_a, T_b\bigr) := \eta(T_a, T_b) + \sum_{\beta \neq 0} q^\beta \left\langle \frac{T_a}{z - \psi}, T_b \right\rangle_{0, 2, \beta}$$

으로 정의하자. 여기서 $$\eta$$는 Poincaré pairing이다. 그럼 $$S$$는 다음을 만족한다. 

1. *(Flat section property)* $$S(q, z)$$의 각 column $$S(q, z) T_b$$는 dual small Dubrovin connection $$\nabla^{z, \vee}$$의 horizontal section이다. 즉
   
   $$z q_a\partial_{q_a} \bigl(S(q,z)T_b\bigr) = T_a \qtimes \bigl(S(q,z)T_b\bigr)\qquad (a = 1, \ldots, r)$$

   이다.
2. *($$J$$ = $$T_0$$ column)* $$J_X(q, z) = e^{t_{(2)}/z} S(q, z) T_0$$가 성립한다. 특히 $$J$$ 자체도 ($$\ast$$)의 horizontal section이고,
   
   $$z q_a\partial_{q_a} J_X = T_a \qtimes J_X \qquad (a = 1, \ldots, r)$$

   이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

우선, $$S$$의 정의식에서 둘째 자리에 $$T_b = T_0 = 1$$을 대입하면 $$J = T_0$$ column이 나오는 것을 보이자. 본 글에서는 일관되게 $$1/(z - \psi) = \sum_{k \geq 0} z^{-k-1}\psi^k$$의 convention을 따르며, 이에 맞추어 divisor equation의 보정항도 $$+$$ 부호로 둔다 (문헌에 따라 $$1/(z + \psi)$$를 쓰며 부호가 반대인 경우도 있다). 이제 정의에 들어 있는 2-point descendant는 $$T_0 = 1$$이 끼인 형태이고, 이를 geometric series로 풀면

$$\left\langle \frac{T_a}{z - \psi}, 1\right\rangle_{0, 2, \beta} = \sum_{k \geq 0} z^{-k-1}\langle \tau_k(T_a), 1\rangle_{0, 2, \beta}$$

이다. 이 때, 각 항에 [\[사교기하학\] §Gromov-Witten 불변량, ⁋명제 3](/ko/math/symplectic_geometry/gromov_witten#prop3)을 적용하면 

$$\langle \tau_k(T_a), 1\rangle_{0, 2, \beta} = \langle \tau_{k-1}(T_a)\rangle_{0, 1, \beta}$$

이 모든 $$k\geq 1$$에 대해 성립한다. $$k = 0$$인 항은 string equation 우변에서 내릴 $$\psi$$가 없어 빈 합이 되므로, $$\langle T_a, 1\rangle_{0, 2, \beta} = 0$$ ($$\beta \neq 0$$)으로 사라진다 (이는 fundamental class를 evaluate하는 marked point가 $$\beta \neq 0$$에서 기여하지 않는다는 사실에 다름 아니다). 따라서 멱급수의 차수가 한 칸씩 내려가서 다음의 식

$$\sum_{k \geq 1} z^{-k-1}\langle \tau_{k-1}(T_a)\rangle_{0, 1, \beta} = \sum_{m \geq 0} z^{-m-2}\langle \tau_m(T_a)\rangle_{0, 1, \beta} = \left\langle \frac{T_a}{z(z - \psi)}\right\rangle_{0, 1, \beta}$$

이 된다. 이것이 정확히 [정의 3](#def3)의 small $$J$$ 식 안에 들어 있는 항이며, 여기에 prefactor $$e^{t_{(2)}/z}$$를 곱한 것이 $$J_X = e^{t_{(2)}/z} S(q, z) T_0$$이다. 이것이 [정의 3](#def3)에서 다소 어색하게 보일 수 있었던 추가적인 $$z^{-1}$$의 기원이다. 

이제 $$S$$의 각 열 $$S(q,z)T_b$$가 horizontal section임을 보이자. 이를 위해서는  $$z q_a\partial_{q_a}$$를 $$S(q, z) T_b$$에 직접 작용시켜보면 된다. 우선 $$S(q, z) T_b$$는 $$\beta$$마다 $$q^\beta$$를 인자로 갖는 항들의 합으로 나타나는데, $$J$$-function을 도입하기 전 살펴본 recursion relation과 [\[사교기하학\] §Gromov-Witten 불변량, ⁋명제 4](/ko/math/symplectic_geometry/gromov_witten#prop4)을 사용하면 $$z q_a\partial_{q_a}$$는 결국 $$T_a$$를 한 점으로 삽입하면서, 곱해진 $$z$$로 distinguished marked point의 $$1/(z - \psi)$$에서 $$\psi$$를 한 차수 내리는 효과를 준다.

이제 이렇게 차수를 내린 $$\psi$$를 [명제 2](#prop2)로 (정확히는 [명제 2](#prop2)에서 target을 살린 버전으로) boundary divisor들의 합 $$\sum_S D_S$$로 분해할 수 있다. 이 때, 각 $$D_S$$ 위에서 source curve는 effective class가 $$\beta = \beta_1 + \beta_2$$로 쪼개진 두 component로 갈라지고, 그 사이의 node에서는 diagonal class $$\sum_c T_c \otimes T^c$$가 끼어든다. 새로 삽입한 $$T_a$$가 모이는 component는 3-point invariant $$\langle T_a, T_c, T_d\rangle_{0, 3, \beta_1}$$, 곧 quantum product $$T_a \qtimes$$를 basis로 표현한 structure constant를 주고, 나머지 component는 $$T^c$$를 node로 갖는 $$S(q, z) T_b$$의 (더 낮은 차수인) $$\beta_2$$에 해당하는 부분을 복원한다. 따라서 모든 $$c$$와 분해 $$\beta = \beta_1 + \beta_2$$에 대해 합하면 $$T_a \qtimes$$를 벡터 $$S(q, z) T_b$$에 적용한 것, 곧 우변 $$T_a \qtimes \bigl(S(q, z) T_b\bigr)$$가 정확히 복원된다.

</details>

따라서 $$q\rightarrow 0$$일 때 모든 $$q^\beta$$항이 사라지므로, $$S$$의 classical limit은 $$\id$$이다. 이는 A-side에서는 quantum cup product의 classical limit이 ordinary cup product라는 것의 결과로 생각할 수 있다. 

[명제 4](#prop4)는 $$J$$-function이 단순한 enumerative 데이터의 묶음을 넘어, A-model 측 fundamental solution matrix $$S$$의 한 열 (구체적으로 normalization element $$T_0 = 1$$에 해당하는 열)을 이룸을 보여준다. 이는 [§가우스-마닌 접속, ⁋명제 7](/ko/math/mirror_symmetry/gauss-manin_connection#prop7)의 period matrix $$\mathcal{I}$$가 frame $$\{e_a\}$$로 trivialize한 $$\nabla^z_B$$의 fundamental solution matrix를 이루었던 것과 정확히 대응되는 것이다. 

특히 $$H^\ast(X)$$가 $$H^2(X)$$로 생성되는 경우, 가령 $$X = \mathbb{P}^n$$이나 대부분의 toric Fano variety인 경우 이 한 열 $$J$$가 사실상 $$S$$ 전체를 결정한다. 실제로 [명제 4](#prop4)의 flat section equation $$z q_a\partial_{q_a} J = T_a \qtimes J$$를 반복 적용하면 $$H^2$$ class들의 quantum product $$T_{a_1} \qtimes \cdots \qtimes T_{a_k} \qtimes J$$가 차례로 생성되는데, $$H^\ast(X)$$가 $$H^2$$로 생성되면 이 quantum product들이 모든 $$T_b$$를 cohomology의 basis로 훑으므로 나머지 열 $$S(q, z) T_b$$도 전부 $$J$$의 미분으로 복원되기 때문이다. 이는 [주장 5](#conj5)에서 우리의 "Mirror theorem"이 오직 첫 열에 대한 주장만 하는 것에 대한 정당성을 부여한다.

한편 이 계산은 앞서 ($$\ast$$)에서부터 계산하여 적분을 반복하며 얻어진 적분상수의 처리와도 관련되어 있는데, 바로 [명제 4](#prop4)의 $$S$$는 이 적분상수를 모든 차수에서 $$0$$으로 버린 해라는 것이다. 즉, $$t_{(2)}$$에서 나오는 성분들을 prefactor $$e^{t_{(2)}/z}$$로 따로 떼어내고 나면 남는 모든 보정이 $$\beta \neq 0$$의 instanton 차수 $$q^\beta$$만을 갖도록, 따라서 위와 같이 $$q \to 0$$일 때 classical limit이 나오도록 한 fundamental solution이다. 

## Mirror theorem

우리는 앞서 A-side의 fundamental solution matrix $$S$$ ([명제 4](#prop4))와 B-side의 period matrix $$\mathcal{I}$$ ([§가우스-마닌 접속, ⁋명제 7](/ko/math/mirror_symmetry/gauss-manin_connection#prop7))를 각각 독립적으로 구성하였다. 두 행렬이 실제로 일치한다는 것이 바로 mirror theorem의 통찰 중 하나이다.

<div class="proposition" markdown="1">

<ins id="conj5">**주장 5 (Mirror theorem, $$J$$-function form)**</ins> Mirror pair $$(X, \check{X})$$에 대하여, $$X$$의 $$J$$-function은 $$T_0 = 1$$ normalization에 대응하는 특정 Lefschetz thimble $$\Gamma_0$$ (large radius limit 근방에서 결정되는 *distinguished* thimble)에 대한 oscillating integral의 cohomology basis $$\{T^a\}$$ 성분들로 적힌다. 즉

$$J_X(q, z) = \sum_a J^a(q, z) T^a,\qquad J^a(q, z) \;\propto\; \mathcal{I}^a_{\Gamma_0}(q, z) = \int_{\Gamma_0} T_a\, e^{W_q/z}\,\omega$$

가 up to normalization으로 성립한다. 여기서 우변은 [§가우스-마닌 접속, ⁋명제 7](/ko/math/mirror_symmetry/gauss-manin_connection#prop7)에서 도입한 period matrix $$\mathcal{I}^a_p$$의 $$p = \Gamma_0$$ 열이다. 

</div>

위의 [주장 5](#conj5)는 mirror symmetry의 가장 강한 표현 중 하나로, A-side의 descendant Gromov-Witten invariant 전체가 B-side에서 period integral으로 복원된다는 것이다. 그럼 특히 classical한 버전의 ring-level mirror symmetry $$QH^\ast(X) \cong \Jac(W_q)$$은 $$z\rightarrow 0$$일 때의 leading order로 복원된다. 구체적으로 $$z \to 0$$ stationary phase asymptotic ([§가우스-마닌 접속, ⁋명제 3](/ko/math/mirror_symmetry/gauss-manin_connection#prop3))은 $$W_q$$의 critical point들에 의한 합으로 풀어지며, 그 leading order의 critical value들 $$\{W_q(p)\}$$가 quantum cohomology의 canonical coordinate들을 복원한다.

이 주장은 단순히 [§두브로빈 접속, ⁋주장 4](/ko/math/mirror_symmetry/dubrovin_connection#conj4)를 반복한 것이 아니다. 이를 보이기 위해 우리는 우선 $$J$$-function이 만족하는 QDE ([명제 4](#prop4))와 period matrix가 만족하는 Gauss-Manin system ([§가우스-마닌 접속, ⁋명제 7](/ko/math/mirror_symmetry/gauss-manin_connection#prop7))이 동일한 $$D$$-module을 정의함을 보여야 하며, 이것이 [§두브로빈 접속, ⁋주장 4](/ko/math/mirror_symmetry/dubrovin_connection#conj4)의 내용이다. 그 후에 우리는 $$J$$-function, 즉 행렬 $$S$$의 첫 열이 [§두브로빈 접속, ⁋주장 4](/ko/math/mirror_symmetry/dubrovin_connection#conj4)의 isomorphism 아래 thimble period들의 임의의 선형결합이 아니라 하필 distinguished thimble $$\Gamma_0$$ 위의 oscillating integral 하나로 옮겨짐을 확인해야 한다. 이를 위해서는 추가적인 양 변의 *integral structure*가 일치한다는 주장이 필요하며, A-side에서는 $$K$$-theory와 $$\hat{\Gamma}$$-class가 정의하는 lattice, 그리고 B-side에서는 Lefschetz thimble들이 생성하는 lattice들이 이 역할을 한다. 

Calabi-Yau hypersurface in toric variety의 경우 Givental과 Lian-Liu-Yau가 이를 증명하였으며, 우리의 주된 관심 대상인 toric Fano variety의 경우 다음 절의 *$$I = J$$* 정리가 이 주장의 explicit하고 계산 가능한 형태를 제공한다.

## Givental's Mirror Theorem

Toric Fano variety의 경우 B-side의 oscillating integral이 명시적인 *hypergeometric* 형태로 계산된다. 이를 통해 정의되는 객체가 *$$I$$-function*이며, $$J$$-function의 toric mirror counterpart로 작동한다.

<div class="definition" markdown="1">

<ins id="def6">**정의 6 (Givental의 $$I$$-function)**</ins> $$X$$를 smooth projective toric Fano variety, $$D_1, \ldots, D_N$$을 toric divisor, $$\beta \in H_2(X, \mathbb{Z})$$를 effective curve class라 하자. $$X$$의 *$$I$$-function*은 다음으로 정의된다.

$$I_X(q, z) := e^{t_{(2)}/z} \sum_{\beta \in H_2(X, \mathbb{Z})_{\mathrm{eff}}} q^\beta \prod_{i=1}^N \frac{\prod_{k=-\infty}^{0} (D_i + kz)}{\prod_{k=-\infty}^{D_i \cdot \beta}(D_i + kz)}$$

</div>

여기서 형식상 등장하는 $$-\infty$$로의 무한곱은 분자와 분모에서 정확히 상쇄되어 실제로는 $$D_i \cdot \beta$$의 부호에 따라 유한곱 (혹은 그 역수)으로 환원되므로, $$I_X$$는 정해진 charge 데이터로부터 *손으로* 적어 내려갈 수 있는 명시적 hypergeometric 함수이다. 이 식의 기원은 $$X$$의 Hori-Vafa mirror $$\check{X}$$ 위의 oscillating integral로, 좀 더 정확히는 그 적분을 [주장 5](#conj5)의 distinguished thimble $$\Gamma_0$$에 대해 charge 데이터로 전개한 것이 정확히 $$I_X$$이다. 즉 $$I_X$$는 [§가우스-마닌 접속, ⁋명제 7](/ko/math/mirror_symmetry/gauss-manin_connection#prop7)의 period matrix $$\mathcal{I}$$의 distinguished 열을 명시적으로 적은 것에 다름 아니다. 자세한 전개는 [예시 8](#ex8)로 미루고, 우선 이를 $$J$$-function에 대한 주장으로 번역하자.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7 (Givental's mirror theorem)**</ins> $$X$$가 smooth projective toric Fano variety일 때, $$X$$의 $$I$$-function과 $$J$$-function은 다음 관계를 만족한다.

$$J_X(\tau(q), z) = I_X(q, z)$$

여기서 $$\tau(q)$$는 $$I$$-function의 asymptotic expansion

$$I_X(q, z) = 1 + \tau(q)/z + O(z^{-2})$$

으로부터 정의되는 **mirror map**이다. $$X$$가 **semi-positive** (즉, $$-K_X \cdot \beta \geq 0$$이 모든 effective curve class $$\beta$$에 대해 성립)이면 $$I_X$$와 $$J_X$$는 이 (일반적으로 비자명한) mirror map을 통한 좌표변환으로 일치한다. 나아가 $$I_X = 1 + O(z^{-1})$$, 즉 $$z^0$$ 차수에 leading $$1$$ 외의 보정항이 없으면 mirror map은 trivial하여 $$J_X(q, z) = I_X(q, z)$$가 성립하는데, 이는 특히 Fano index가 $$2$$ 이상인 경우에 해당한다.

</div>

<details class="proof" markdown="1">
<summary>증명 개요</summary>

[정의 6](#def6) 직후 보았듯 $$I_X$$는 B-side period matrix $$\mathcal{I}$$의 distinguished 열 ($$\Gamma_0$$ 위의 oscillating integral) 을 명시적으로 적은 것이므로, [명제 7](#prop7)은 본질적으로 [주장 5](#conj5)를 그 distinguished 열로 제한하여 toric Fano case에서 명시화한 것이다. 따라서 보여야 할 핵심은 이 명시적 hypergeometric 함수 $$I_X$$가 $$J$$-function과 동일한 flat section, 즉 [명제 4](#prop4)의 QDE의 해라는 점이다. 실제로 $$I_X$$의 hypergeometric 곱이 만족하는 미분방정식은 small QDE ($$\ast$$)와 일치하며, 이 일치를 $$\mathbb{P}^n$$에 대해 ODE ($$\dagger$$)의 형태로 직접 계산하는 것이 [예시 8](#ex8)이다. 두 해가 모두 $$z \to \infty$$에서 $$1 + O(z^{-1})$$의 점근을 가지므로 $$z^{-1}$$ 계수로 정의되는 mirror map $$\tau(q)$$를 통한 좌표변환 후 일치하며, 일반 toric Fano에 대한 완전한 증명은 [CK, §11], [MS, Chapter 29] 참조.

</details>

이로써 [명제 7](#prop7)은 mirror symmetry를 *계산 가능한* tool로 바꾼다. $$J$$-function의 추상적인 Gromov-Witten 정의로부터는 직접 계산이 어렵지만, $$I$$-function의 hypergeometric 형태는 charge matrix로부터 손으로 적을 수 있어, 다음 절에서 보듯 $$\mathbb{P}^n$$과 같은 구체적인 경우에 양변을 직접 맞대어 볼 수 있기 때문이다.

## 예시: $$\mathbb{P}^n$$

<div class="example" markdown="1">

<ins id="ex8">**예시 8** ($$X = \mathbb{P}^n$$)</ins> $$\mathbb{P}^n$$의 fan은 [\[토릭 기하학\] §토릭 다양체의 정의, ⁋예시 10](/ko/math/toric_geometry/toric_varieties#ex10)에서 본 standard simplex의 normal fan으로, $$n+1$$개의 ray $$v_i = e_i$$ ($$i = 1, \ldots, n$$)와 $$v_0 = -e_1 - \cdots - e_n$$을 갖는다. Cohomology ring은 $$H^\ast(\mathbb{P}^n) = \mathbb{C}[H]/(H^{n+1})$$로, hyperplane class $$H \in H^2(\mathbb{P}^n)$$ 하나가 ring 전체를 생성하며, 특히 $$H$$는 $$H^2(\mathbb{P}^n) \cong \mathbb{Z}$$ (곧 $$\Pic(\mathbb{P}^n) = \mathbb{Z} H$$) 를 생성한다. Effective curve class는 그 dual인 line class $$H^\vee$$의 음이 아닌 배수 $$d H^\vee$$ ($$d \geq 0$$)로 매개되며, 각 toric divisor에 대해 $$D_i \cdot d H^\vee = d$$이므로 $$I$$-function 공식은

$$I_{\mathbb{P}^n}(q, z) = e^{H \ln q /z} \sum_{d \geq 0} \frac{q^d}{\prod_{j=1}^d (H + jz)^{n+1}}$$

이 된다. $$H^{n+1} = 0$$이므로 분모의 $$(H + jz)^{-(n+1)}$$를 $$z^{-1}$$의 멱으로 전개하면 첫 몇 차수가 명시적으로 풀린다.

$$I_{\mathbb{P}^n}(q, z) = 1 + \frac{H \ln q}{z} + \frac{(H \ln q)^2}{2 z^2} + \cdots + q \frac{1}{(H+z)^{n+1}} + \cdots$$

$$\mathbb{P}^n$$은 $$-K_{\mathbb{P}^n} = (n+1) H$$이므로 Fano index가 $$n+1 \geq 2$$이고, 따라서 [명제 7](#prop7)에 의해 $$I_{\mathbb{P}^n} = 1 + O(z^{-1})$$이 되어 mirror map은 trivial하고

$$J_{\mathbb{P}^n}(q, z) = I_{\mathbb{P}^n}(q, z)$$

이다.

B-side와의 직접 짝맞춤은 [§가우스-마닌 접속, ⁋예시 8](/ko/math/mirror_symmetry/gauss-manin_connection#ex8)에서 이미 절반이 끝나있다. 그 예시에서 우리는 period matrix의 첫 column $$\mathcal{I}^0_p$$가 만족하는 ODE

$$(z\partial_q)(qz\partial_q)^n\mathcal{I}^0_p = \mathcal{I}^0_p \tag{$\dagger$}$$

를 도출했다. [주장 5](#conj5)의 mirror theorem이 옳다면 $$I_{\mathbb{P}^n}$$의 $$H^0$$-coefficient

$$\Phi_0(q, z) := \sum_{d \geq 0} \frac{q^d}{(d!)^{n+1}z^{(n+1)d}}$$

(위의 hypergeometric 곱 식에서 $$H = 0$$으로 specialize한 것) 또한 ($$\dagger$$)를 만족해야 한다. 직접 계산하면 $$qz\partial_q$$의 작용은 항별로 $$d$$를 끌어내고 $$z^{-1}$$ 인자를 붙이므로

$$(qz\partial_q)^n\Phi_0 = \sum_{d\geq 0}\frac{d^n q^d}{(d!)^{n+1}z^{(n+1)d - n}},$$

이고 다시 $$z\partial_q$$를 작용시키면 $$d$$를 한번 더 끌어내고 $$d$$를 $$d - 1$$로 shift시켜

$$(z\partial_q)(qz\partial_q)^n\Phi_0 = \sum_{d \geq 1}\frac{d^{n+1}q^{d-1}}{(d!)^{n+1}z^{(n+1)d - n - 1}} = \sum_{d' \geq 0}\frac{(d'+1)^{n+1}q^{d'}}{((d'+1)!)^{n+1}z^{(n+1)d'}} = \Phi_0$$

가 정확히 성립한다. 따라서 $$I_{\mathbb{P}^n}$$이 만족하는 hypergeometric ODE와 B-side의 Gauss-Manin ODE가 동일하며, 두 fundamental solution이 $$z \to \infty$$에서 같은 normalization $$1 + O(z^{-1})$$을 가지므로 $$J_{\mathbb{P}^n} = I_{\mathbb{P}^n}$$이 곧 [§가우스-마닌 접속, ⁋예시 8](/ko/math/mirror_symmetry/gauss-manin_connection#ex8)의 oscillating integral과 일치한다는 의미가 된다. 

[주장 5](#conj5)의 stationary phase 측면 또한 [§가우스-마닌 접속, ⁋예시 8](/ko/math/mirror_symmetry/gauss-manin_connection#ex8)에서 이미 계산해 두었다. 즉 $$W_q$$의 $$n+1$$개 critical point $$x_\zeta = \zeta q^{1/(n+1)}$$에서의 critical value $$(n+1)\zeta q^{1/(n+1)}$$과 Hessian determinant $$(n+1)(\zeta q^{1/(n+1)})^{-n}$$이 [§가우스-마닌 접속, ⁋명제 3](/ko/math/mirror_symmetry/gauss-manin_connection#prop3)의 stationary phase formula에 대입되어 oscillating integral의 $$z\to 0^+$$ asymptotic을 주며, 이것이 $$I_{\mathbb{P}^n}(q, z)$$의 $$z \to 0$$ asymptotic과도 일치한다 ([CK, §11.2]).

</div>

이 예시는 mirror symmetry가 추상적인 동형이 아니라 *구체적인 hypergeometric 함수의 일치*로 실현됨을 보여준다. 일반적인 toric Fano variety의 경우 비슷한 명시적 계산이 charge matrix로부터 진행되며, 그 모든 사례에서 [명제 7](#prop7)의 $$I = J$$ 정리가 mirror symmetry의 실용적인 검증을 제공한다.

## Big quantum cohomology로의 확장

지금까지 다룬 small $$J$$-function은 [§두브로빈 접속, §§D-module](/ko/math/mirror_symmetry/dubrovin_connection#d-module)의 $$H^2$$ 방향만의 deformation을 base로 한 small quantum $$D$$-module에 대한 fundamental solution이었다. 같은 글의 앞부분에서 본 것처럼 Dubrovin connection 자체는 사실 $$H^\ast(X)$$ 전체 deformation을 base로 한 big quantum cohomology 위에서 정의되었으며, $$H^2$$ 방향만 본 small 버전은 이를 specialize한 것이었다. 같은 격상이 $$J$$-function에 대해서도 가능하며, 그것이 *big $$J$$-function*이다. 

Big 버전의 setup으로 가려면 $$H^\ast(X)$$의 일반적인 deformation parameter $$t = \sum_{a=0}^s t^a T_a$$를 도입해야 한다. 임의의 $$t \in H^\ast(X)$$에 대한 big quantum product $$\star_t$$는 [§두브로빈 접속, §§D-module](/ko/math/mirror_symmetry/dubrovin_connection#d-module)에서 본 대로 $$\mathcal{C}_\alpha = T_\alpha \star_t -$$로 Dubrovin connection의 connection $$1$$-form을 결정한다. 그 dual horizontal section equation은

$$z\partial_a s = T_a \star_t s\qquad (a = 0, 1, \ldots, s)$$

이며, 이것이 small case의 ($$\ast$$)를 $$H^\ast$$ 전체 방향으로 확장한 *big QDE*이다. 

<div class="definition" markdown="1">

<ins id="def9">**정의 9** (Big $$J$$-function)</ins> $$X$$의 *big Givental $$J$$-function* $$J_X^{\mathrm{big}}: H^\ast(X) \times \mathbb{C}^\ast \to H^\ast(X)$$는 다음으로 정의된다.

$$J_X^{\mathrm{big}}(t, z) := e^{t_{(2)}/z}\left( 1 + \sum_{\substack{\beta \in H_2(X, \mathbb{Z})_{\mathrm{eff}}, n \geq 0 \\ (\beta, n) \neq (0, 0)}} \sum_{a=0}^s \frac{q^\beta}{n!} \left\langle \frac{T_a}{z - \psi}, t, \ldots, t \right\rangle_{0, n+1, \beta} T^a \right)$$

여기서 첫 marked point에 $$T_a/(z-\psi)$$가 (즉 $$T_a$$의 pullback에 모든 차수의 $$\psi^k$$가 generating function 형태로) 끼이고, 나머지 $$n$$개 marked point에 모두 $$t \in H^\ast(X)$$가 삽입되어 총 $$n+1$$개 marked point를 이룬다.

</div>

Big J가 big QDE의 horizontal section을 이룬다는 사실은 [명제 4](#prop4)의 small 버전과 같은 논증 — $$\partial_a$$를 marked point 추가, $$\psi$$-class를 topological recursion relation으로 분해 — 을 모든 $$a = 0, \ldots, s$$에 대해 적용하면 그대로 따른다. 그리고 small J는 big J의 $$t = t_{(2)} \in H^2(X)$$ specialization으로 복원되는데, $$H^2$$ 삽입에 (descendant 보정항이 붙은) divisor equation을 $$n$$번 적용하면 $$t_{(2)}$$ 삽입들이 $$(t_{(2)} \cdot \beta)^n$$ 인자와 $$\psi$$-shift 보정으로 빠져나오고, 이들이 $$\sum_n (t_{(2)}\cdot \beta)^n/n! = q^\beta$$로 합산되며 $$\psi$$-shift 보정이 추가 $$z^{-1}$$ 인자를 만들어내어, 결과적으로 marked point가 $$1$$개로 줄어든 [정의 3](#def3)의 small J 형태가 그대로 복원된다. 

Big J-function이 담고 있는 추가 정보는 임의의 cohomology class들로 정해지는 모든 descendant invariant들이다. 이를 토대로 mirror theorem ([주장 5](#conj5))도 big 버전으로 격상되어 *전체* $$S$$-matrix와 *전체* period matrix의 일치를 주장하는 더 강한 statement가 되며, $$I = J$$ ([명제 7](#prop7))도 mirror map $$\tau(q)$$가 일반적으로 자명하지 않은 big version에서 더 풍부한 내용을 갖는다 (예시: Calabi-Yau hypersurface). 한편 우리의 주된 응용 대상인 toric Fano variety (특히 Fano index $$\geq 2$$) 와 partial flag variety 의 경우 mirror map이 trivial하거나 small 정보로 충분하여, 본 글의 main thread는 small case로 일관되게 진행하였다.

---

**참고문헌**

**[CK]** D. A. Cox, S. Katz, *Mirror Symmetry and Algebraic Geometry*, Mathematical Surveys and Monographs **68**, AMS, 1999.

**[MS]** K. Hori, S. Katz, A. Klemm, R. Pandharipande, R. Thomas, C. Vafa, R. Vakil, E. Zaslow, *Mirror Symmetry*, Clay Mathematics Monographs **1**, AMS, 2003.

---

[^1]: 그 기원은 [명제 4](#prop4)의 증명에서 살펴본다. 