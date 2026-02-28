---

title: "원환면의 작용"
excerpt: ""

categories: [Math / Lie Theory]
permalink: /ko/math/lie_theory/torus_action
header:
    overlay_image: /assets/images/Math/Lie_Theory/Torus_action.png
    overlay_filter: 0.5
sidebar: 
    nav: "Lie_theory-ko"

date: 2026-02-24
last_modified_at: 2026-02-24
weight: 2

---

임의의 유한군 $G$가 주어졌을 때 이를 잘 살펴보는 방법 중 하나는 그 유한차원 representation 

$$\rho:G\rightarrow \Aut(V)$$

을 보는 것이다. $V$의 basis를 선택하고 나면 $\rho$에 의한 $G$의 image를 다루는 것은 선형대수에 불과하므로 우리는 $G$의 구조를 훨씬 쉽게 알아낼 수 있다. 

Lie group의 경우 이러한 표현론적 관점은 더 도움이 되는데, Lie group은 $\GL(n;\mathbb{R})$이나 $\Diff(M)$과 같이, 본질적으로 다른 대상 위에 작용하는 것이기 때문이다. 

다만 [\[표현론\] §유한군의 표현론, ⁋정의 1](/ko/math/representation_theory/representations_of_finite_groups#def1)에서처럼 $G$의 representation theory를 정의하면 Lie group $G$ 위에 있는 smooth structure는 놓치게 되므로, 다음과 같이 정의해주어야 한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Lie group $G$에 대하여, $G$의 *representation<sub>표현</sub>*은 유한차원 벡터공간 $V$와, smooth map

$$\rho:G\rightarrow \Aut(V)$$

이 주어진 것이다. 

</div>

만일 $G$를 discrete topology와 자명한 smooth structure가 주어진 Lie group으로 본다면 이 정의는 [\[표현론\] §유한군의 표현론, ⁋정의 1](/ko/math/representation_theory/representations_of_finite_groups#def1)의 일반화라 생각할 수도 있다. 비슷하게 [\[표현론\] §유한군의 표현론, §§표현론의 기본 개념들](/ko/math/representation_theory/representations_of_finite_groups#표현론의-기본-개념들)에 있는 모든 정의를 Lie group에 대해서도 할 수 있다. 

이 글에서 중요한 역할을 했던 것은 group $G$가 유한군이라는 사실이었다. 가령 $G$의 모든 원소에 대해 평균을 내는 아이디어는 이러한 사실을 바탕으로 했다. 이를 Lie group으로 일반화하기 위해서는 $G$에 어떠한 종류의 유한성을 강제해야 한다. 

우리는 따라서 $G$가 *compact* Lie group인 경우를 종종 다루게 된다. 이 경우, locally compact Hausdorff space로서 $G$ 위에는 Haar measure가 존재하며 따라서 $G$의 원소들에 대한 합을 $G$ 전체에 대한 적분으로 바꿔 쓸 수 있다. 물론 이를 위해서는 $\delta_x$ 함수를 잘 정의하고, 함수공간을 적당한 공간으로 일반화하는 작업을 거쳐야 하지만 이러한 작업은 우리의 현재 목적이 아니므로 생략하기로 혼다. 중요한 것은 리 군의 표현론 또한 유한군의 표현론과 같은 방법론을 통해 접근할 수 있다는 것이다. 특히 임의의 finite-dimensional representation은 irreducible decomposition들의 direct sum으로 나타낼 수 있다. 

한편, 유한차원 representation $G\rightarrow\Aut(V)$가 주어졌다 할 때, 가장 좋은 점은 이들의 image $\rho(g)$들을 (basis의 선택을 통해) 행렬로 생각할 수 있다는 것이다. 따라서 이를 통해 우리는 행렬과 선형사상에 대한 우리의 도구들을 사용하여 이를 탐구할 수 있다. 

선형대수에서 가장 중요한 도구 중 하나는 대각화이다. 따라서 우리는 주어진 Lie group action $\rho:G \rightarrow \Aut(V)$에 대하여, $V$의 basis를 적당히 택하여 $\rho(g)$의 행렬표현을 대각행렬로 만드는 데에 관심이 있다. 만일 $G$가 유한군이었다면, 각각의 $g$에 대해 이러한 basis를 찾아줄 수 있었겠지만 현재는 $G$가 무한하므로 이러한 일을 하기 힘들다. 따라서 우리는 simultaneously diagonalizable인 원소들에 자연스럽게 관심을 갖게 된다. 그런데 [\[선형대수학\] §고유공간분해, ⁋명제 10](/ko/math/linear_algebra/eigenspace_decomposition#prop10)은 두 diagonalizable matrix가 simultaneously diagonalizable일 필요충분조건은 이들이 commute하는 것임을 알고 있으므로, 다음 정의를 내리는 것이 합당하다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Compact, connected Lie group $G$에 대하여, $G$의 subgroup $T$가 *maximal torus*라는 것은 $T$가 torus이고, 포함관계에 대하여 maximal인 것이다. 

</div>

Lie algebra $\mathfrak{g}$의 임의의 원소 $X$를 택한 후, 이 방향으로의 exponential map이 그리는 one-parameter subgroup의 closure가 torus가 된다. 따라서 maximal torus의 존재성은 [\[집합론\] §선택공리, ⁋정리 4](/ko/math/set_theory/axiom_of_choice#thm4)에 의해 자명하다. 

주의할 것은, 위에서 생각하는 one-parameter group $\exp(tX)$가 1차원 torus를 만들 것이라는 착각을 하기 쉬운데 이것이 항상 그렇지는 않다는 것이다. 가령 2차원 torus

$$T^2\cong \mathbb{R}^2/\mathbb{Z}^2$$

을 생각하면, quotient를 취하기 전 $(1,\sqrt{2})$ 방향으로의 one-parameter subgroup은 $T^2$ 전체를 조밀하게 덮고, 이 image의 closure가 바로 $T^2$ 전체가 된다. 이렇게

$$T=\overline{\langle t\rangle}$$

을 만족하는 $t\in T$를 $T$의 *generator*라 부른다. 

## Weight decomposition

우리의 주장은 $\rho(T)$가 simultaneously diagonalizable이라는 것이다. 이를 위해서는 $\rho(T)$의 각각의 원소들이 diagonalizable인 것을 보이면 충분하다. 이를 위해 임의의 finite-dimensional representation $\rho:G\rightarrow \Aut(V)$을 생각하고 이를 maximal torus $T$로 제한한 representation $\rho\vert_T$을 생각하자. 가장 먼저 확인할 수 있는 것은 $T$가 compact Lie group이라는 사실이다. 따라서 [\[표현론\] §유한군의 표현론, ⁋명제 6](/ko/math/representation_theory/representations_of_finite_groups#prop6)과 [\[표현론\] §유한군의 표현론, ⁋보조정리 8](/ko/math/representation_theory/representations_of_finite_groups#lem8)이 모두 성립한다. 

보다 자세하게 이들을 하나하나 써 보면, 우선 $\rho\vert_T$가 unitary representation이라는 사실로부터 우리는 다음의 irreducible decomposition

$$V=\bigoplus_i V_i$$

을 생각할 수 있다. 여기에서 각각의 $V_\lambda$는 irreducible $T$-representation들이다. 한편, $T$가 abelian이므로 임의의 $t\in T$에 대하여, $\rho(t)$은 $T$-action과 모두 commute하고, 따라서 각각의 $V_i$로 제한하였을 때 $\rho(t)$는 $T$-automorphism이다. 이제 [\[표현론\] §유한군의 표현론, ⁋보조정리 8](/ko/math/representation_theory/representations_of_finite_groups#lem8)의 두 번째 결과에 의하여 $\rho(t)$는 상수배

$$\rho(t)(v)=\lambda_i(t)v\qquad \lambda_i(t)\in \mathbb{C}^\times$$

로 주어진다. 그런데 이제 $V_i$ 위에서 $T$가 상수배들로 작용한다면, $V_i$의 임의의 부분공간은 $T$-invariant일 것이며 따라서 $V_i$가 irreducible이기 위해서는 반드시 $\dim V_i=1$이어야만 한다. 

이제 $\dim V_i=1$이므로 $\Aut(V_i)\cong \mathbb{C}^\times$이고, 우리는 위의 $\lambda_i: T\rightarrow \mathbb{C}^\times$가 정확하게 $\rho$의 character에 해당하고, 따라서 irreducible decomposition이 직접적으로 character $\lambda_i$에 의해 parametrize되는 것으로 생각할 수 있다. 즉 다음의 식

$$V=\bigoplus_\lambda V_\lambda;\qquad V_\lambda=\{t\cdot v=\lambda(t)v\text{ for all $t\in T$}\}$$

을 통해 irreducible decomposition이 주어진 것으로 생각하자. 그럼 각각의 $t\in T$에 대하여, $\rho(t)$는 바로 이 decomposition에 의하여 대각화되고, 각각의 eigenspace $V_\lambda$에 해당하는 고유값은 $\lambda(t)$이다. 이와 다른 $t$의 선택은 위의 decomposition은 그대로 두고, 각각의 eigenspace $V_\lambda$에 해당하는 고유값만 바뀌는 것이다. 

직관적으로 $t\mapsto e^{2\pi i\lambda_i(X)}$를 각속도 $\lambda_i(X)$를 갖는 각운동이라 생각할 수 있고, 이러한 관점을 도입하면 우리는 각각의 $X\in \mathfrak{t}$가 주어졌을 때, 이 방향으로의 각속도 $\lambda_i(X)$가 얼마인지를 통해 이 torus action을 설명할 수 있다는 것을 안다. 이 때 각각의 $\lambda_i$들을 우리는 *weight*라 부른다. 그럼 우리는 각각의 weight $\lambda_i$마다 적당한 $V_i$가 존재하여, 이 위에서는 torus action이 $t\cdot v=\rchi_{\lambda_i}(t)v$로 작동하는 것을 안다. 이러한 $V_i$를 *weight space*라 부른다. 

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> 특별한 예시로, 1차원 torus

$$S^1\cong T \cong \mathbb{R}/\mathbb{Z}$$

을 생각하면, $S^1$은 다음의 집합

$$S^1=\left\{e^{2\pi i t}\mid t\in \mathbb{R}/\mathbb{Z}\right\}$$

으로 생각할 수 있다. 이제 이 집합이 2차원 벡터공간 $\mathbb{C}^2$ 위에 다음의 식

$$e^{2\pi i t}\cdot (z_1,z_2)=(e^{4\pi i t}z_1, e^{-2\pi i t}z_2)$$

으로 act한다고 하자. 이 action은 작위적으로 보이지만, 위에서 살펴본 것과 같이 임의의 torus $T$와 임의의 representation $V$가 주어졌다면 $V$의 irreducible decomposition을 생각하고 각각의 irreducible component의 basis $e_i$들을 택하면 모든 torus action은 (적당한 basis의 선택에 의해) 이러한 꼴로 나타나는 것을 안다. 

이를 행렬로 나타내면, 위의 action은 $\GL(2;\mathbb{C})$의 원소(들의 family)

$$\begin{pmatrix}e^{4\pi i t}&0\\0&e^{-2\pi i t}\end{pmatrix}$$

로 나타낼 수 있다. 이 때 이 행렬의 trace $e^{4\pi i t}+e^{-2\pi i t}$가 바로 이 representation의 character이다. 

이 action의 weight space는 $\span(e_1), \span(e_2)$임이 자명하며, 가령 $\span(e_1)$에 해당하는 weight는 다음의 식

$$\rchi_{\lambda_1}(\exp (X))=e^{2\pi i \lambda_1(X)}\qquad\text{for all $X\in \mathfrak{t}$}$$

을 만족하는 linear functional $\lambda_1:\mathfrak{t}\rightarrow \mathbb{C}$으로 주어진다. 이는 당연히 $1\in \mathbb{R}$을 $2$로 보내는 $\lambda_1(t)=2t$에 의해 정의되며 따라서 이 weight space에 해당하는 weight는 (약간의 abuse of notation을 통해) $2$라 할 수 있다. 이 때 $\lambda$가 위의 식을 만족하기 위해서는, $e^{2\pi i}=1$이므로, 반드시 $\lambda(1)\in \mathbb{\mathbb{Z}}$여야 한다. 

더 일반적으로 만일 $r$차원 torus의 action이 주어졌다면 $\mathfrak{t}$는 $\mathbb{R}^r$일 것이며, 이 때 torus $T$를

$$T^r=\left\{(e^{2\pi i t_1}, \ldots e^{2\pi i t_r})\mid t_i\in \mathbb{R}/\mathbb{Z}\right\}$$

으로 쓴다면 그 Lie algebra $\mathfrak{t}\cong \mathbb{R}^r$ 중 weight가 될 수 있는 것은 $\mathbb{Z}^r$에 속하는 원소이며 따라서 weight $\lambda$는 다음의 $r$-tuple

$$\lambda=(n_1, \ldots, n_r)$$

로 주어질 것이다. 명시적으로 이 weight는 임의의 $X=(x_1,\ldots, x_r)\in \mathfrak{t}$가 주어졌을 때 $n_1x_1+\cdots+n_rx_r$을 내놓는 linear functional이다.  

</div>

선형대수학에서의 eigenspace decomposition에서와 마찬가지로, 각각의 weight에 대한 중복도가 $1$일 필요는 없다. 가령 다음의 torus action

$$e^{2\pi i t}\cdot(z_1, z_2)=(e^{4\pi i t}z_1, e^{4\pi i t} z_2)$$

를 생각하면 이번에는 2차원 공간 $\mathbb{C}^2$ 위에서 $T$가 weight $2$를 갖는 것처럼 행동하기 때문이다. 이와 같이 서로 같은 weight $\lambda$들을 갖는 성분들을 한데 모아 이를 $V_\lambda$라 하면, 우리는 *weight space decomposition* $V=\bigoplus V_\lambda$를 얻는다. 지금까지의 논의를 엄밀하게 정의로 적으면 다음과 같다. 

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Torus $T$와 complex $T$-module $V$가 주어졌다 하자. Irreducible character $\rchi_\lambda: T \rightarrow S^1$와 그에 해당하는 linear functional $\lambda:\mathfrak{t}\rightarrow\mathbb{C}$에 대하여, $\lambda$가 $V$의 *weight*이라는 것은 다음 집합

$$V_\lambda=\left\{v\in V\mid t\cdot v=\rchi_\lambda(t)v\text{ for all $t\in T$}\right\}$$

이 nontrivial인 것이다. 이 때, $V_\lambda$를 $\lambda$의 *weight space*라 하며, decomposition

$$V=\bigoplus_\lambda V_\lambda$$

을 $V$의 *weight decomposition*이라 부른다. 

</div>

## 극대 원환면

우리는 이 섹션에서 compact connected Lie group $G$의 임의의 원소는 항상 어떠한 maximal torus에 포함되어 있고, 또 모든 maximal torus는 서로 conjugate이라는 것을 보인다. 

우리의 주장은 compact connected Lie group $G$와 그 maximal torus $T$에 대하여, 다음의 map

$$q: G/T\times T\rightarrow G; \qquad (g,t)\mapsto gtg^{-1}$$

이 surjective라는 것이다. 그럼 특히 임의의 다른 torus $T'$와 그 generator $t'$에 대하여 $gtg^{-1}=t'$을 만족하는 $t\in T$를 찾을 수 있을 것이고, $T$와 $T'$의 maximality를 각각 사용하면 위에서 언급한 두 주장이 증명될 것이다. 

우리는 이 map이 surjective라는 것 뿐만 아니라, 명시적인 mappuing degree까지 구해줄 수 있다. 이를 위해 다음을 정의하자. 

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Compact, connected Lie group $G$와 maximal torus $T$, 그리고 $T$의 normalizer

$$N=\{g\in G\mid gTg^{-1}=T\}$$

에 대하여, group $W=N/T$를 $G$의 *Weyl group<sub>바일 군</sub>*으로 정의한다. 

</div>

그럼 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> Weyl group $W=N/T$는 항상 유한하다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

정의에 의해 $N$은 $T$ 위에 conjugation action

$$N\rightarrow\Aut(T);\qquad n\mapsto (t\mapsto ntn^{-1})$$

으로 작용한다. 그런데 $\Aut(T)$는 torus $T=\mathbb{R}^k/\mathbb{Z}^k$의 lattice가 어디로 옮겨지는지에 의해 결정되고, 이는 $\GL(k;\mathbb{Z})$에 $\Ad(n)$을 통해 담겨있다. 즉 이 action은 $N$에서 $\GL(k;\mathbb{Z})$로의 연속함수로 생각할 수 있다. 그런데 $\GL(k;\mathbb{Z})$는 discrete이므로 $N$의 identity component $N_0$을 생각하면 $N_0$은 모두 항등행렬로 옮겨져야 한다. 즉, $N_0$은 $T$ 위에 자명하게 작용한다. 

이제 임의의 1-parameter subgroup $\alpha:\mathbb{R}\rightarrow N_0$에 대하여, $\alpha(\mathbb{R})\cdot T=T$가 성립해야 하고, 이로부터 $\alpha(\mathbb{R})\subset T$여야 함을 안다. 그런데 [\[미분다양체\] §벡터장, ⁋정리 6](/ko/math/manifold/vector_fields#thm6)에 의하여 이들은 $N_0$에서 항등원의 어떠한 열린근방을 덮으며, 따라서 $N_0$을 생성한다. 즉 $N_0=T$이다.

따라서 $N/T$는 정확하게 $N$의 connected component의 개수이며, $N$은 compact Lie group $G$의 closed subspace로서 마찬가지로 compact이므로 이것이 무한할 수 없다.

</details>

이제 우리의 주장은 다음과 같다. 

<div class="proposition" markdown="1">

<ins id="lem7">**보조정리 7**</ins> Compact, connected Lie group $G$, maximal torus $T$와 함수

$$q:G/T\times T\rightarrow G;\qquad (gT, s)\mapsto gsg^{-1}$$

에 대하여, $q$의 mapping degree는 $\lvert W\rvert$이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Mapping degree를 계산하기 위해서는 regular value 하나를 선택한 후 그 preimage를 모두 찾고, 각각의 preimage에서의 differential의 sign을 계산하면 된다. 

이를 위해 먼저 $T$의 generator $t$를 하나 택하고 그 preimage $q^{-1}(t)$를 생각하자. 임의의 $(gT,s)\in G/T\times T$에 대하여, $q(gT,s)=t$라는 것은 $gsg^{-1}=t$라는 것이다. 한편 $g^{-1}tg=s\in T$이고, 

$$\overline{\langle s\rangle}=g^{-1}\overline{\langle t\rangle}g=g^{-1}Tg$$

인데, $s\in T$이므로 $g^{-1}Tg\subseteq T$이다. 그런데 conjugation을 취하는 것은 homeomorphism이므로 $g^{-1}Tg$는 $T$와 isomorphic한 torus이고, 이로부터 $g^{-1}Tg=T$이며 $g\in N=N_G(T)$인 것을 안다. 또한 $s=g^{-1}tg=(gT)\cdot t$이므로,

$$q^{-1}(t)=\{(gT, (gT)\cdot t)\mid gT\in W\}$$

이다. 여기서 $W$가 $N/T$로 정의된 Weyl group이며, 우리는 $q^{-1}(t)$가 $W$와 일대일 대응됨을 안다.

따라서 남은 것은 이들이 모두 같은 sign을 가져서 mapping degree가 정확히 $\lvert W\rvert$로 나온다는 것을 보이는 것이다. 이를 위해 $G/T\times T$와 $G$의 tangent space를 모두 $\mathfrak{g}$와 동일시한다. 구체적으로, Lie algebra $\mathfrak{g}$를 $\mathfrak{t}$와 그 orthogonal complement $\mathfrak{f}=\mathfrak{t}^\perp$의 direct sum

$$\mathfrak{g}=\mathfrak{t}\oplus\mathfrak{f}$$

으로 분해하면, 원점 근처에서 $T$의 tangent space는 $\mathfrak{t}$이고 $G/T$의 tangent space는 $\mathfrak{f}$로 주어진다. 따라서 $G/T\times T$의 tangent space는 $\mathfrak{t}\oplus\mathfrak{f}\cong\mathfrak{g}$이다.

한편 임의의 $X\in\mathfrak{t}$와 $Y\in\mathfrak{f}$에 대하여, $q$의 $(eT,t)$에서의 differential은 다음과 같이 계산된다. 방향 $X$에 대하여, 즉 $T$ 방향으로의 변화를 생각하면

$$d q_{(eT,t)}(X,0)=\frac{d}{d\epsilon}\bigg\vert_{\epsilon=0}q(eT, t\exp(\epsilon X))=\frac{d}{d\epsilon}\bigg\vert_{\epsilon=0}t\exp(\epsilon X)=X$$

이다. 여기서 $T$가 abelian이므로 $t$와 $\exp(\epsilon X)$가 commute함을 사용하였다. 다음으로 방향 $Y$에 대하여, 즉 $G/T$ 방향으로의 변화를 생각하면

$$d q_{(eT,t)}(0,Y)=\frac{d}{d\epsilon}\bigg\vert_{\epsilon=0}q(\exp(\epsilon Y)T, t)=\frac{d}{d\epsilon}\bigg\vert_{\epsilon=0}\exp(\epsilon Y)t\exp(-\epsilon Y)$$

이다. 이제 $t=\exp(H)$ ($H\in\mathfrak{t}$)로 쓰면,

$$\exp(\epsilon Y)t\exp(-\epsilon Y)=\exp(\epsilon Y)\exp(H)\exp(-\epsilon Y)=\exp(\Ad_{\exp(\epsilon Y)}(H))=\exp(e^{\epsilon\ad_Y}H)$$

이고, 따라서

$$\frac{d}{d\epsilon}\bigg\vert_{\epsilon=0}\exp(\epsilon Y)t\exp(-\epsilon Y)=\frac{d}{d\epsilon}\bigg\vert_{\epsilon=0}\exp(H+\epsilon[Y,H])=\exp(H)\cdot [Y,H]$$

이다. 여기서 $\mathfrak{t}$가 abelian이므로 $[Y,H]\in\mathfrak{f}$이고, $\exp(H)=t$이므로 이는 $t\cdot(\Ad_t^{-1}(Y)-Y)$로 쓸 수 있다. 정리하면, 적절한 identification 하에서

$$d q_{(eT,t)}=\begin{pmatrix} I & 0 \\ 0 & \Ad_t^{-1}\vert_\mathfrak{f}-I \end{pmatrix}$$

이다. 여기서 첫 번째 block은 $\mathfrak{t}$ 방향, 두 번째 block은 $\mathfrak{f}$ 방향에 해당한다.

이제 $\Ad_t^{-1}\vert_\mathfrak{f}-I$가 가역이며, 모든 preimage에서 sign이 맞아떨어짐을 보인다. 만약 $(\Ad_t^{-1}-I)Y=0$인 $Y\in\mathfrak{f}$가 존재한다면, $\Ad_t(Y)=Y$이다. 그럼 임의의 정수 $m$에 대하여 $\Ad_{t^m}(Y)=Y$이고, $t$가 generator라는 가정으로부터 모든 $s\in T$에 대하여 $\Ad_s(Y)=Y$이다. 이제 임의의 $H\in\mathfrak{t}$에 대하여,

$$[H,Y]=\frac{d}{d\epsilon}\bigg\vert_{\epsilon=0}\Ad_{\exp(\epsilon H)}(Y)=0$$

이므로 $Y$는 $\mathfrak{t}$의 모든 원소와 commute한다. 그런데 $\mathfrak{t}$는 maximal abelian subalgebra이므로 $Y\in\mathfrak{t}$이고, 따라서 $Y\in\mathfrak{f}\cap\mathfrak{t}=\{0\}$이다. 즉 $\Ad_t^{-1}\vert_\mathfrak{f}-I$는 가역이다.

마지막으로, $q^{-1}(t)$의 모든 점에서 $dq$의 determinant가 같은 부호를 갖는지 확인하자. 임의의 $w\in W$를 택하고 이를 $x\in N$이 represent한다 하자. 그럼 $q(xT,x^{-1}tx)=t$이므로 $(xT, x^{-1}tx)\in q^{-1}(t)$이다. 이 점에서의 differential을 계산하기 위해, $q$의 정의로부터

$$q(gT, s)=gsg^{-1}$$

이므로, left translation by $x$와 conjugation by $x$를 고려하면

$$d q_{(xT, x^{-1}tx)}=\Ad_x\circ d q_{(eT, t)}\circ (\text{left translation})$$

이다. 특히 $\Ad_x\vert_\mathfrak{f}$와 $\Ad_x\vert_\mathfrak{t}$는 모두 determinant가 $1$인 linear map이며 (전자는 orthogonal map이므로, 후자는 $x\in N$이므로 $\Ad_x$가 $\mathfrak{t}$를 보존하므로), 따라서 $d q_{(xT, x^{-1}tx)}$의 determinant는 $d q_{(eT,t)}$의 determinant와 같다.

한편 $\det(\Ad_t^{-1}\vert_\mathfrak{f}-I)$는 $w\cdot t$에 대해서도 동일하다. 실제로

$$\Ad_{wt^{-1}w^{-1}}\vert_\mathfrak{f}-I=\Ad_w\circ(\Ad_t^{-1}\vert_\mathfrak{f}-I)\circ\Ad_w^{-1}$$

이므로, 이 두 operator는 similar하고 따라서 같은 determinant를 갖는다.

이상에서 $t$는 $q$의 regular value이고, $q^{-1}(t)$의 원소 개수는 $\lvert W\rvert$이며, 모든 preimage 점에서 $dq$의 determinant는 같은 부호를 갖는다는 것을 확인하였다. 따라서 적절한 orientation 선택 하에서 $\deg q=\lvert W\rvert$이다.

</details>

위에서 언급한 것과 같이, 이 보조정리로부터 이 섹션의 핵심적인 내용이 바로 따라나온다.

<div class="proposition" markdown="1">

<ins id="thm8">**정리 8**</ins> Compact connected Lie group $G$에 대해 다음이 성립한다.

1. $G$의 임의의 원소는 어떠한 maximal torus에 포함되어 있다. 
2. $G$의 두 maximal torus는 항상 conjugate이다. 

</div>

따라서 우리는 임의의 compact connected Lie group $G$와 maximal torus $T$에 대하여, 다음의 decomposition

$$G=\bigcup_{g\in G}gTg^{-1}$$

을 얻는다. 이를 *Cartan decomposition*이라 부른다.

## Weyl group parametrization

Cartan decomposition은 $G$의 각 원소가 어떠한 maximal torus에 속한다는 것을 말해주지만, 이 decomposition을 더 명시적으로 기술할 수 있다. 핵심은 [보조정리 7](#lem7)에서 정의한 map

$$q:G/T\times T\rightarrow G;\qquad (gT,t)\mapsto gtg^{-1}$$

이 $\lvert W\rvert$-to-1 covering이라는 사실이다. 이로부터 $G$의 각 원소는 $\lvert W\rvert$개의 preimage를 가지며, 이들 간의 관계를 Weyl group이 정확히 기술해준다.

구체적으로, $G/T\times T$ 위에 다음의 $W$-action을 정의하자.

$$w\cdot(gT, t)=(gw^{-1}T, wtw^{-1})$$

그럼 

$$q(w\cdot(gT,t))=q(gw^{-1}T, wtw^{-1})=gw^{-1}(wtw^{-1})wg^{-1}=gtg^{-1}=q(gT,t)$$

이므로 $q$는 $W$-invariant이고, 따라서 orbit space $(G/T\times T)/W$에서 $G$로의 함수

$$(G/T\times T)/W\rightarrow G$$

을 유도한다. [보조정리 7](#lem7)은 이 함수가 bijection임을 증명한다.

한편, $G$의 conjugacy class들의 공간을 $\Conj(G)$라 하자. 그럼 각 conjugacy class 

$$[g]=\{hgh^{-1}\mid h\in G\}$$

는 $T$와 $W$를 통해 다음과 같이 기술된다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> Maximal torus $T$의 두 원소가 $G$에서 conjugate인 것과 이들이 Weyl group action의 같은 orbit에 속하는 것이 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$T$의 두 원소 $x,y$가 서로 conjugate이라 하자. 즉 적당한 $g\in G$에 대하여 $gxg^{-1}=y$이다. 이제 $T$와 $gTg^{-1}$을 비교하면 이들은 $y$의 centralizer $Z_G(y)$의 maximal torus이다. 따라서 $T=h(gTg^{-1})h^{-1}$이도록 하는 $h\in Z_G(y)$가 존재하며, 이로부터 $(hg)x(hg)^{-1}=y$이고 $hg\in N_G(T)$이다. 즉 $y=(hgT)\cdot x$이므로 $x$와 $y$는 같은 $W$-orbit에 속한다.

역으로, $x,y$가 같은 $W$-orbit에 속한다면 자명히 $G$에서 conjugate이다.

</details>

이로부터 각 conjugacy class $[g]$에 대하여, $[g]\cap T$는 정확하게 하나의 $W$-orbit임을 안다. 따라서 우리는 다음의 일대일대응을 얻는다.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> $T/W$와 $\Conj(G)$ 사이에는 자연스러운 일대일대응이 존재한다.

</div>

이 일대일대응 하에서, $G$ 위의 conjugation action은 $T/W$ 위에서 자명하게 작용한다. 즉, $G$의 각 원소는 자신이 속한 conjugacy class를 보존한다.

## Conjugation action의 분해

이제 $G$가 자기 자신에게 conjugation으로 작용하는 상황을 살펴보자. 이를 위해 각 $g'\in G$에 대하여, conjugation map

$$c_{h}:G\rightarrow G;\qquad g\mapsto hgh^{-1}$$

을 정의한다. 우리의 목표는 이를 $(G/T\times T)/W$로 옮긴 후 이것이 어떻게 작용하는지를 구체적으로 살펴보는 것이다.

먼저 다음을 관찰하자. 임의의 $(gT, t)\in G/T\times T$와 $h\in G$에 대하여,

$$c_{h}(gtg^{-1})=h(gtg^{-1})h^{-1}=(hg)t(hg)^{-1}=q(hgT, t)$$

이 성립한다. 즉, $(G/T\times T)/W\cong G$를 통해 $c_h$를 $G/T\times T$로 옮겨왔을 때 $c_h$는  $(gT, t)$를 $(hgT, t)$로 보내므로, $G/T\times T$ 위에 다음의 $G$-action이 정의된 것으로 생각할 수 있다.

$$h\cdot(gT,t)=(hgT,t)$$

이제 이 action이 $W$-action과 commute하는 것은 자명하며, 따라서 $G$는 quotient $(G/T\times T)/W$ 위에도 잘 정의된 action을 유도한다. 이 observation으로부터 다음을 얻는다.

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> Identification $(G/T\times T)/W\cong G$ 하에서, conjugation action은 다음과 같이 표현된다.

$$h\cdot[(gT,t)]=[(hgT,t)]$$

즉, $G/T$ 성분에는 left multiplication으로 작용하고, $T$ 성분은 보존한다.

</div>

한편, 우리는 [명제 10](#prop10)에 의하여 $T/W$와 $\Conj(G)$ 사이에 일대일대응이 존재함을 안다. $c_h$는, 정의에 의해, $G$의 conjugacy class를 변화시키지 않으며 이것이 위의 명제에서 $T$ 방향의 변화가 없는 것으로 반영된 것을 확인할 수 있다. 그 대신 conjugation action은 정확하게 $G/T$ 위에 작용하는 것으로 생각할 수 있다.

이제 $G/T$ 위에서의 $G$-action을 더 자세히 이해하기 위해, 우리는 이 공간을 Weyl group을 이용히여 다시 쓸 것이다. 우선 $N=N(T)$에 대하여, 다음의 projection map

$$\pi: G/T\rightarrow G/N;\qquad gT\mapsto gN$$

을 생각하자. 그럼 각각의 coset $gN\in G/N$에 대하여, 그 fiber는

$$\pi^{-1}(gN)=\{hT\mid h\in gN\}=\{gxT\mid x\in N\}$$

이며, $g$가 고정되어 있으므로 이 fiber는 본질적으로 $\\{xT\mid x\in N\\}$, 즉 $N/T$와 같다. 더 나아가 위상적으로 $\pi$는 정확하게 $\lvert W\rvert$-fold covering map이라는 것을 확인할 수 있다. ([\[대수적 위상수학\] §피복공간, ⁋정의 3](/ko/math/algebraic_topology/covering_spaces#def3)) 더 정확히 이는 각 fiber가 $W$인 principal $W$-bundle이다. 

## 예시: $\SU(2)$

지금까지의 논의를 compact connected Lie group

$$\SU(2)=\{A\in\GL(2;\mathbb{C})\mid A^\dagger A=I,\det A=1\}=\left\{\begin{pmatrix}\alpha&-\overline{\beta}\\\beta&\overline{\alpha}\end{pmatrix}\,\middle\vert\;\alpha,\beta\in \mathbb{C},\lvert\alpha\rvert^2+\lvert\beta\rvert^2=1\right\}$$

에서 확인해보자. 우선 $\SU(2)$의 maximal torus를 구해야 한다. 우리의 주장은 다음 집합

$$T=\left\{\begin{pmatrix}e^{i\theta}&0\\0&e^{-i\theta}\end{pmatrix}\,\middle\vert \;\theta\in\mathbb{R}/2\pi\mathbb{Z}\right\}$$

이 $\SU(2)$의 (한) maximal torus라는 것이다. $T$가 $1$차원 torus인 것은 자명하므로, maximalilty만 보이면 충분하다. 이를 위해 $T$를 포함하는 $\SU(2)$의 abelian subgroup $A$가 주어졌다 하면, 임의의 원소

$$\begin{pmatrix}a&b\\c&d\end{pmatrix}\in A$$

가 $T$의 모든 원소와 commute해야 하므로 특히 

$$\begin{pmatrix}i&0\\0&-i\end{pmatrix}$$

와 commute해야 하고, 이를 계산하면

$$\begin{pmatrix}a&b\\c&d\end{pmatrix}\begin{pmatrix}i&0\\0&-i\end{pmatrix}=\begin{pmatrix}ai&-bi\\ci&-di\end{pmatrix},\qquad \begin{pmatrix}i&0\\0&-i\end{pmatrix}\begin{pmatrix}a&b\\c&d\end{pmatrix}=\begin{pmatrix}ai&bi\\-ci&-di\end{pmatrix}$$

이므로 이로부터 $b=c=0$이어야 함을 안다. 이로부터 $A\subset T$임을 안다. 

이제 Weyl group을 계산하기 위해 $T$의 normalizer $N=N_{\SU(2)}(T)$이 다음의 식

$$N=T\cup \begin{pmatrix}0&1\\-1&0\end{pmatrix}T$$

으로 주어진다는 것을 보이자. 우선 임의의 $g\in \SU(2)$에 대하여,

$$g=\begin{pmatrix}\alpha&-\overline{\beta}\\\beta&\overline{\alpha}\end{pmatrix},\qquad \lvert\alpha\rvert^2+\lvert\beta\rvert^2=1$$

라 적으면

$$\begin{pmatrix}\alpha&-\overline{\beta}\\\beta&\overline{\alpha}\end{pmatrix}\begin{pmatrix}e^{i\theta}&0\\0&e^{-i\theta}\end{pmatrix}\begin{pmatrix}\end{pmatrix}$$

한편 $g=\begin{pmatrix}a&b\\-b^*&a^*\end{pmatrix}$ ($|a|^2+|b|^2=1$)로 쓰면, 계산을 통해 $g$가 $T$를 보존하는 것은 $ab=0$인 것과 동치임을 알 수 있다. 즉, $b=0$이면 $g\in T$이고, $a=0$이면 $g=\begin{pmatrix}0&b\\-b^*&0\end{pmatrix}=\begin{pmatrix}0&1\\-1&0\end{pmatrix}\begin{pmatrix}b^*&0\\0&-b\end{pmatrix}\in\begin{pmatrix}0&1\\-1&0\end{pmatrix}T$이다.

Weyl group $W\cong\mathbb{Z}_2$의 nontrivial element는 $\begin{pmatrix}0&1\\-1&0\end{pmatrix}$에 해당한다. 이 원소의 $T$ 위에서의 action을 계산하면

$$\begin{pmatrix}0&1\\-1&0\end{pmatrix}\begin{pmatrix}e^{i\theta}&0\\0&e^{-i\theta}\end{pmatrix}\begin{pmatrix}0&-1\\1&0\end{pmatrix}=\begin{pmatrix}e^{-i\theta}&0\\0&e^{i\theta}\end{pmatrix}$$

이다. 즉, Weyl group action은 $\theta\mapsto -\theta$로, torus $S^1$ 위에서의 reflection에 해당한다.

### Weight decomposition

$SU(2)$의 기본적인 representation을 생각하자. 자연스러운 representation $\rho:SU(2)\rightarrow\GL(2,\mathbb{C})$에서 각 $g\in SU(2)$는 $2\times 2$ 행렬로 작용한다. 이를 $T$로 제한하면

$$\rho\vert_T\left(\begin{pmatrix}e^{i\theta}&0\\0&e^{-i\theta}\end{pmatrix}\right)=\begin{pmatrix}e^{i\theta}&0\\0&e^{-i\theta}\end{pmatrix}$$

이므로, weight decomposition은 자명하게 $V=\mathbb{C}e_1\oplus\mathbb{C}e_2$로 주어진다. 여기서 weight들은 $\lambda_1(\theta)=\theta$, $\lambda_2(\theta)=-\theta$이다.

더 흥미로운 예시로, symmetric power $S^n(\mathbb{C}^2)$를 생각하자. 이는 $(n+1)$차원 representation으로, basis가 $e_1^n, e_1^{n-1}e_2, \ldots, e_2^n$으로 주어진다. $T$의 작용은

$$\begin{pmatrix}e^{i\theta}&0\\0&e^{-i\theta}\end{pmatrix}\cdot e_1^{n-k}e_2^k = e^{i(n-2k)\theta}e_1^{n-k}e_2^k$$

이다. 따라서 weight들은 $n, n-2, n-4, \ldots, -n$이며, 각 weight의 multiplicity는 1이다.

### Weyl group action on weights

Weyl group $W=\mathbb{Z}_2$가 weight들 위에 작용한다. Weight $\lambda(\theta)=n\theta$에 대하여, $w\cdot\lambda(\theta)=\lambda(-\theta)=-n\theta$이다. 즉, weight $n$은 $-n$으로 보내진다.

$S^n(\mathbb{C}^2)$의 경우, weight들이 $n, n-2, \ldots, -n$으로 대칭적으로 배열되어 있음을 알 수 있다. 이는 Weyl group이 weight set을 보존한다는 일반적인 사실의 구체적인 예시이다.

## Regular 원소와 Singular 원소

Maximal torus $T$의 원소를 그 "genericity"에 따라 분류할 수 있다.

<div class="definition" markdown="1">

<ins id="defXX">**정의 XX**</ins> Maximal torus $T$의 원소 $t$가 *regular*라는 것은 $wtw^{-1}=t$를 만족하는 $w\in W$가 오직 $w=e$뿐인 것이다. 반대로, $wtw^{-1}=t$인 $w\neq e$가 존재하면 $t$를 *singular*라 한다.

</div>

즉, regular 원소는 Weyl group action의 stabilizer가 자명한 원소이고, singular 원소는 비자명한 stabilizer를 갖는 원소이다.

<div class="example" markdown="1">

<ins id="exXX">**예시 XX**</ins> $SU(2)$의 경우, $T=\{\text{diag}(e^{i\theta}, e^{-i\theta})\}$이고 $W=\mathbb{Z}_2$가 $\theta\mapsto -\theta$로 작용한다. 따라서:

- **Regular:** $\theta \neq 0, \pi$인 원소들. 이들은 reflection의 fixed point가 아니다.
- **Singular:** $\theta=0$ (항등원)과 $\theta=\pi$ ($\text{diag}(-1,-1)$). 이들은 reflection에 의해 고정된다.

Torus $T\cong S^1$에서 singular 원소는 정확히 두 점이며, regular 원소들은 그 여집합이다.

</div>

일반적으로 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="propXX">**명제 XX**</ins> Compact connected Lie group $G$의 maximal torus $T$에 대하여:

1. Regular 원소들은 $T$에서 dense open subset을 이룬다.
2. Singular 원소들은 $T$에서 codimension $\geq 1$인 closed subset을 이룬다.
3. Singular 원소들의 집합은 유한 개의 subgroup들의 합집합이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

(1)과 (2): 각 $w\in W$, $w\neq e$에 대하여, fixed point set $\{t\in T: wtw^{-1}=t\}$는 $T$의 proper closed subgroup이다. Singular 원소들의 집합은 이들의 유한 합집합이므로 closed이고, 그 여집합(regular 원소들)은 dense open이다.

(3): 각 $w\neq e$에 대한 fixed point set이 $T$의 closed subgroup이고, $W$가 유한이므로 유한 개의 subgroup들의 합집합이다.

</details>

### Geometric interpretation

Singular 원소들이 $T$에서 형성하는 집합은 torus를 여러 조각으로 나눈다. $SU(2)$의 경우, singular 원소 두 점이 $S^1$을 두 개의 arc로 나눈다. 각 arc에서 Weyl group은 자유롭게 작용하며, 두 arc는 Weyl group action에 의해 서로 대응된다.

이 관점에서 보면, $T$의 regular 원소들의 quotient $T_{\text{reg}}/W$는 연결된 공간이며, 이를 *Weyl chamber*의 개념과 연결할 수 있다. $SU(2)$의 경우 $T_{\text{reg}}/W \cong (0,\pi)$는 1차원 interval이고, 이것이 바로 1차원 Weyl chamber에 해당한다.

더 일반적인 Lie group에서는 singular 원소들이 torus를 여러 chamber들로 나누고, 각 chamber는 Weyl group action의 fundamental domain 역할을 한다. 이것이 다음 글에서 다룰 root system과 Weyl chamber의 기하적 토대가 된다.

---

**참고문헌**

**[Bro]** Armand Borel, *Linear Algebraic Groups*, Graduate texts in mathematics, Springer, 1991.  
**[BtD]** Theodor Bröcker, Tammo tom Dieck, *Representations of Compact Lie Groups*, Graduate texts in mathematics, Springer, 1985.