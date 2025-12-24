---

title: "근계"
excerpt: ""

categories: [Math / Lie Theory]
permalink: /ko/math/Lie_theory/root_systems
header:
    overlay_image: /assets/images/Math/Lie_Theory/Root_systems.png
    overlay_filter: 0.5
sidebar: 
    nav: "Lie_theory-ko"

date: 2025-11-12
last_modified_at: 2025-11-12
weight: 2

---

## 원환면의 작용

우리는 [§리 군, ⁋정의 19](/ko/math/Lie_theory/Lie_groups#def19)에서 Lie group $G$의 adjoint representation $G\rightarrow \Aut(\mathfrak{g})$을 정의했다. 이를 통해 우리는 임의의 Lie group을 (basis의 선택을 거친다면) matrix Lie group으로 생각할 수 있다. 많은 경우 $\mathfrak{g}$이 *complex* vector space인 것이 편하므로, 필요한 경우에는 $\mathfrak{g}$의 complexification을 $\mathfrak{g}$로 쓰기도 한다. ([정의 3](#def3))

한편 simply connected, compact Lie group $G$는 항상 torus를 포함한다. 이는 가령, 고정된 방향 $X\in \mathfrak{g}$으로의 exponential map이 정의하는 곡선을 생각하고 $G$가 compact라는 사실을 이용하면 확인할 수 있다. 우리는 우선 다음을 정의한다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Compact connected Lie group $G$에 대하여, $G$의 subgroup $T$가 *maximal torus*라는 것은 $T$가 torus이고, $T\subsetneq T' \subset G$를 만족하는 torus $T'$가 존재하지 않는 것이다.

</div>

한편 우리는 임의의 torus $T$에 대하여, $T$는 abelian이고 따라서 $T$의 임의의 irreducible representation $V$는 $1$차원이라는 것을 안다. 바꾸어 말하자면, 임의의 representation $T\rightarrow\Aut(V)$가 주어졌다 하면, 이를 irreducible subrepresentation으로 분해하여 다음의 식

$$V=\bigoplus_{i}V_i$$

을 얻고, 각각의 $V_i$는 $1$차원이다. 이 때 각각의 $V_i$ 위에서는 $T$의 action이 훨씬 명시적인데, 이는 $V_i$가 $1$차원인 것으로부터 $\Aut(V_i)\cong \mathbb{C}^\times$이므로, torus action은 continuous homomorphism $\chi_{\lambda_i}:T \rightarrow \Aut(V_i)\cong \mathbb{C}^\times$로 주어지기 때문이다. 뿐만 아니라 이것이 irreducible이므로 $\lvert\lambda\rvert=1$이고 따라서 각각의 $V_i$ 위에서 torus action은 

$$t\cdot v=\chi_{\lambda_i}(t)v,\qquad \chi_{\lambda_i}(t)\in S^1\subset\mathbb{C}^\times$$

으로 주어진다. 한편 우리는 다음의 식

$$\chi_{\lambda_i}(\exp(X))=e^{2\pi i \lambda_i(X)}\qquad\text{for all $X\in \mathfrak{t}$}\tag{1}$$

을 통해 $T$의 character $\chi_{\lambda_i}$와 $\mathfrak{t}$ 위에 정의된 linear functional $\lambda_i$ 사이의 일대일 대응이 있는 것을 안다. 

직관적으로 $t\mapsto e^{2\pi i\lambda_i(X)}$를 각속도 $\lambda_i(X)$를 갖는 각운동이라 생각할 수 있고, 이러한 관점을 도입하면 우리는 각각의 $X\in \mathfrak{t}$가 주어졌을 때, 이 방향으로의 각속도 $\lambda_i(X)$가 얼마인지를 통해 이 torus action을 설명할 수 있다는 것을 안다. 이 때 각각의 $\lambda_i$들을 우리는 *weight*라 부른다. 그럼 우리는 각각의 weight $\lambda_i$마다 적당한 $V_i$가 존재하여, 이 위에서는 torus action이 $t\cdot v=\chi_{\lambda_i}(t)v$로 작동하는 것을 안다. 이러한 $V_i$를 *weight space*라 부른다. 

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> 특별한 예시로, 1차원 torus

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

$$\chi_{\lambda_1}(\exp (X))=e^{2\pi i \lambda_1(X)}\qquad\text{for all $X\in \mathfrak{t}$}$$

을 만족하는 linear functional $\lambda_1:\mathfrak{t}\rightarrow \mathbb{C}$으로 주어진다. 이는 당연히 $1\in \mathbb{R}$을 $2$로 보내는 $\lambda_1(t)=2t$에 의해 정의되며 따라서 이 weight space에 해당하는 weight는 (약간의 abuse of notation을 통해) $2$라 할 수 있다. 이 때 $\lambda$가 위의 식을 만족하기 위해서는, $e^{2\pi i}=1$이므로, 반드시 $\lambda(1)\in \mathbb{\mathbb{Z}}$여야 한다. 

더 일반적으로 만일 $r$차원 torus의 action이 주어졌다면 $\mathfrak{t}$는 $\mathbb{R}^r$일 것이며, 이 때 torus $T$를

$$T^r=\left\{(e^{2\pi i t_1}, \ldots e^{2\pi i t_r})\mid t_i\in \mathbb{R}/\mathbb{Z}\right\}$$

으로 쓴다면 그 Lie algebra $\mathfrak{t}\cong \mathbb{R}^r$ 중 weight가 될 수 있는 것은 $\mathbb{Z}^r$에 속하는 원소이며 따라서 weight $\lambda$는 다음의 $r$-tuple

$$\lambda=(n_1, \ldots, n_r)$$

로 주어질 것이다. 명시적으로 이 weight는 임의의 $X=(x_1,\ldots, x_r)\in \mathfrak{t}$가 주어졌을 때 $n_1x_1+\cdots+n_rx_r$을 내놓는 linear functional이다.  

</div>

직관적으로 weight decomposition은 일종의 eigenspace decomposition으로 생각할 수 있으며, 이것이 우리가 real vector space 대신 complex vector space를 생각하는 이유이다. 한편 eigenspace decomposition에서와 마찬가지로, 각각의 weight에 대한 중복도가 $1$일 필요는 없다. 가령 다음의 torus action

$$e^{2\pi i t}\cdot(z_1, z_2)=(e^{4\pi i t}z_1, e^{4\pi i t} z_2)$$

를 생각하면 이번에는 2차원 공간 $\mathbb{C}^2$ 위에서 $T$가 weight $2$를 갖는 것처럼 행동하기 때문이다. 이와 같이 서로 같은 weight $\lambda$들을 갖는 성분들을 한데 모아 이를 $V_\lambda$라 하면, 우리는 *weight space decomposition* $V=\bigoplus V_\lambda$를 얻는다. 지금까지의 논의를 엄밀하게 정의로 적으면 다음과 같다. 

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Torus $T$와 complex $T$-module $V$가 주어졌다 하자. Irreducible character $\chi_\lambda: T \rightarrow S^1$와 그에 해당하는 linear functional $\lambda:\mathfrak{t}\rightarrow\mathbb{C}$에 대하여, $\lambda$가 $V$의 *weight*이라는 것은 다음 집합

$$V_\lambda=\left\{v\in V\mid t\cdot v=\chi_\lambda(t)v\text{ for all $t\in T$}\right\}$$

이 nontrivial인 것이다. 이 때, $V_\lambda$를 $\lambda$의 *weight space*라 하며, decomposition

$$V=\bigoplus_\lambda V_\lambda$$

을 $V$의 *weight decomposition*이라 부른다. 

</div>

특히 이를 위의 상황에 적용하면, 우리는 임의의 simply connected compact Lie group $G$와 $G$의 한 maximal torus $T$에 대하여, adjoint representation $\Ad: G\rightarrow \Aut(\mathfrak{g})$를 $T$로 제한하여 $\mathfrak{g}$를 $T$-module로 볼 수 있다. 그럼 이를 통해 $T$의 representation $\Ad\vert_T: T \rightarrow \Aut(\mathfrak{g})$를 얻고, 따라서 $\mathfrak{g}$의 weight decomposition을 얻게 될 것이다. 

한편 우리는 adjoint action $\Ad$의 명시적인 정의로부터, $T$가 trivial하게 act하는 $\mathfrak{g}$의 subspace를 정확히 알고 있다. 즉 $T$의 Lie algebra $\mathfrak{t}$를 생각하면, $T$가 abelian이라는 사실로부터 $\mathfrak{t}$ 위에서는 이 action이 identity가 되는 것을 안다. 이 때 identity에 해당하는 linear functional은 zero map이므로, 우리는 다음의 decomposition 

$$\mathfrak{g}=\mathfrak{g}_0\oplus\bigoplus_{\alpha\neq 0}\mathfrak{g}_\alpha\tag{2}$$

를 얻는다. 

이제 우리는 앞선 논의를 Lie algebra의 언어로 바꾸어 쓸 것이다. 그 전에 우리의 관심을 다소 제한시킬 필요가 있다. 우선 임의의 Lie algebra $\mathfrak{g}$가 *semisimple*이라는 것은 $\mathfrak{g}$가 simple Lie algebra들의 direct sum이라는 것이며, 여기서 simple Lie algebra는 그 ideal이 $0$과 자기자신 뿐인 non-abelian Lie algebra를 의미한다. 만일 $\mathfrak{g}$가 semisimple Lie algebra라면, 다음의 식

$$( X,Y)=\tr(\ad_X\ad_Y)$$

으로 정의한 $(-,-): \mathfrak{g}\times\mathfrak{g}\rightarrow \mathbb{K}$이 non-degenerate이며 그 역도 성립한다는 것을 보일 수 있다. 그럼 우리는 이 "내적"으로부터 weight들의 기하학에 대해 살펴볼 수 있게 된다. 

따라서 $\mathfrak{g}$가 semisimple Lie algebra라 하자. 그럼 $\mathfrak{g}$의 Lie subalgebra $\mathfrak{h}$가 *Cartan subalgebra*라는 것은 $\mathfrak{h}$가 maximal abelian Lie algebra이며, 각각의 $H\in \mathfrak{h}$에 대하여 $\ad_H$가 diagonalizable인 것이다. 이는 semisimple Lie algebra를 가지는 Lie group $G$로 한정한다면, 정확히 $G$의 maximal torus의 Lie algebra에 해당하는 것이다. 

이를 바탕으로 위의 decomposition (2)를 살펴보면 $\mathfrak{g}\_0$은 정확히 Cartan subalgebra $\mathfrak{h}$에 해당하는 부분이 되며 $\mathfrak{g}\_\alpha$들 위에서는 torus $T$가 act하므로 그 미분 $\ad$를 통해 $\mathfrak{h}$가 act한다. 이제 다음을 정의하자. 

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Semisimple Lie algebra $\mathfrak{g}$와 $\mathfrak{g}$의 Cartan subalgebra $\mathfrak{h}$에 대하여, 

$$\Phi=\left\{\alpha\in \mathfrak{h}^\ast\setminus\{0\}\mid \mathfrak{g}_\alpha\neq 0\right\}$$

의 원소들을 $\mathfrak{g}$의 *root*라 부른다. 이 때 

$$\mathfrak{g}_\alpha=\left\{X\in \mathfrak{g}\mid [H,X]=\alpha(H)X\text{ for all $H\in \mathfrak{h}$}\right\}$$

이다. ([§리 군, ⁋정의 19](/ko/math/Lie_theory/Lie_groups#def19))

</div>

즉, semisimple Lie group $G$와 $G$의 maximal torus $T$, 그리고 $T$의 Lie algebra $\mathfrak{t}$를 생각하면, $T$의 adjoint action의 weight decomposition은 다음의 root space decomposition 

$$\mathfrak{g}=\mathfrak{t}\oplus \bigoplus_{\alpha\in \Phi} \mathfrak{g}_\alpha$$

을 준다. 우리가 이들을 weight 대신 별도로 root라 부르는 이유는 위에서 언급한 것과 같이 $\mathfrak{g}$ 위에 잘 정의된 내적을 통해 이들이 *root system*을 이루기 때문이다. 

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> 유한차원 벡터공간 $E$와 그 위에 정의된 inner product $( -,-)$을 고정하자. $E$의 non-zero vector들의 유한한 집합 $\Phi$가 *root system*이라는 것은 다음의 조건들이 만족되는 것이다. 

1. $\Phi$의 원소들이 $E$를 span한다. 
2. 만일 $\alpha\in \Phi$이고 $c\in \mathbb{R}$이라면 $c\alpha\in \Phi$이기 위해서는 $c=\pm 1$이어야 한다. 
3. 각각의 root $\alpha\in\Phi$에 대하여, $\Phi$는 $\alpha$에 수직인 초평면에 대한 대칭이동 $s_\alpha$에 대해 닫혀있다. 즉, 임의의 $\alpha,\beta\in \Phi$에 대하여
    
    $$s_\alpha(\beta):=\beta-2\frac{(\beta,\alpha)}{(\alpha,\alpha)}\alpha\in \Phi$$

    이다. 
4. 임의의 root $\alpha,\beta\in\Phi$에 대하여, 다음 식
    
    $$\langle \beta,\alpha\rangle:=2\frac{(\alpha,\beta)}{(\alpha,\alpha)}$$

    은 항상 정수이다. 

</div>

## 바일 군

지금까지의 핵심적인 내용을 요약하면 다음과 같다. 

> Compact, connected semisimple Lie group $G$에 대하여, 그 maximal torus $T$를 고정하고 adjoint representation $\Ad:G \rightarrow \Aut(\mathfrak{g})$를 $T$로 제한하여 얻어진 weight decomposition을 생각하자. 그럼 weight들은 $\mathfrak{t}^\ast$의 원소이며, 이 위에 정의된 Killing form $(-,-)$에 대하여, nonzero weight들은 root system을 이룬다.

이제 우리가 남은 글에서 설명할 것은 만일 maximal torus $T$를 다른 maximal torus $T'$로 바꾼다면, 이 root decomposition은 어떻게 바뀔지에 대한 것이다. 큰 흐름은 다음과 같다. 

1. 고정된 root system $\Phi$에 대하여, $\Phi$는 [정의 5](#def5)의 세 번째 조건으로부터 $s_\alpha$들에 대해 닫혀있다. 이러한 원소들로 이루어진 reflection group을 *Weyl group* $W(\Phi)$이라 부른다. 
2. 한편, 임의의 Lie group 위에 정의된 maximal torus $T$에 대하여, $G$의 adjoint action 중 $T$를 보존하는 것들의 모임을 $W(G,T)=N_G(T)/T$으로 적는다. 

우리의 핵심적인 주장은, 위의 상황에서 만들어지는 root system을 $\Phi(G,T)$라 할 경우, $W(\Phi(G,T))\cong W(G,T)$가 성립한다는 것이다. 물론 만일 다른 maximal torus $T'$를 택한다면, 마찬가지로 $W(\Phi(G, T'))\cong W(G, T')$를 얻을 것이다. 그럼 우리의 두 번째 주장은 canonical하게 $W(\Phi(G,T))\cong W(\Phi(G, T'))$ 그리고 $W(G,T)\cong W(G, T')$이며 이 canonical isomorphism 하에서 두 isomorphism $W(\Phi(G,T))\cong W(G,T)$와 $W(\Phi(G, T'))\cong W(G, T')$는 같은 것이라는 것이다. 이에 대한 증명을 모두 하려면 글이 과하게 길어지므로 이 대응들 각각에 대한 설명만 하기로 한다. 

위의 흐름에서 $W(\Phi)$는 그 정의가 자명하므로 $W(G,T)$를 우선 정의하자. 

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> Compact connected Lie group $G$와, $G$의 maximal torus $T$, 그리고 그 normalizer

$$N=N(T)=\{g\in G\mid gTg^{-1}=T\}$$

에 대하여, $W(G,T)=N/T$를 $G$의 *Weyl group*이라 부른다. 

</div>

정의에 의해 Weyl group은 $T$의 선택에 의존하지만, 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="thm7">**정리 7 (Cartan)**</ins> 임의의 compact connected Lie group $G$의 두 maximal torus $T,T'$는 항상 conjugate이며, 임의의 $G$의 원소는 어떤 maximal torus에 포함되어 있다. 

</div>

바꾸어 말하자면, 임의의 $G$의 element는, 고정된 maximal torus $T$에 대하여, 적당한 $t\in T$의 conjugate으로 쓸 수 있다.

이제 $W(G,T)$가 root system $\Phi(G,T)$ 위에 어떻게 작용하는지를 살펴봐야 한다. 이는 다음의 식

$$((nT)\cdot \alpha)(H)=\alpha(\Ad(n^{-1})(H))\qquad\text{for all $H\in \mathfrak{t}$}$$

으로 주어진다. 이는 더 자세하게 쓰면 다음과 같다. 임의의 root $\alpha:\mathfrak{t}\rightarrow \mathbb{C}$를 생각하자. 이 root에 해당하는 weight space는

$$g_{\alpha}=\left\{X\in \mathfrak{g}\mid [H,X]=\alpha(H)X\text{ for all $H\in \mathfrak{h}$}\right\}$$

이다. 이제 임의의 $X\_\alpha\in \mathfrak{g}\_\alpha$와 $n\in N_G(T)$에 대하여, $n$은 $nTn^{-1}=T$를 만족하므로 이를 미분하면 $n$에 의한 adjoint action은 Cartan subalgebra $\mathfrak{t}$ 또한 보존한다. 이제 식

$$\alpha(H)X=[H,X]\text{for all $H\in \mathfrak{t}$}$$

의 양변에 $n$에 의한 conjugation을 취하면, 

$$\alpha(H)(nXn^{-1})=[nHn^{-1}, nXn^{-1}]\text{for all $H\in \mathfrak{t}$}$$

을 얻는다. 한편 $nHn^{-1}\in \mathfrak{t}$이고, 이것이 $\mathfrak{t}$와 $n\mathfrak{t}n^{-1}$ 사이의 bijection을 정의하므로 이는 다음의 식

$$[H, nXn^{-1}]=\alpha(H)\cdot (nXn^{-1})\text{for all $H\in \mathfrak{t}$}$$

으로 쓸 수 있다. 즉, 요약하자면 $\mathfrak{t}$에서 $\mathfrak{t}$로의 conjugation map $c(n): X\mapsto nXn^{-1}$을 생각하면, 식 $w(\alpha)=\alpha\circ c(n^{-1})$으로 정의된 $w(\alpha)$ 또한 root이며 이 때 root space 또한 conjugation action을 통해 옮겨지게 된다. 

이제 이 대응이 $W(G,T)\cong W(\Phi(G,T))$를 준다는 것이 앞서 언급한 핵심적인 주장이 된다. 

한편 [정리 7](#thm7)에 의하여, 우리는 임의의 maximal torus $T, T'$가 주어진다면 $T'=gTg^{-1}$을 만족하는 $g\in G$가 존재하게, 이로부터 만들어지는 Weyl group $W(G, T')$ 또한 

$$W(G, T')=N_G(T')/T'=(gN_G(T)g^{-1})/(gTg^{-1})\cong W(G,T)$$

임을 안다. 이 때 명시적인 isomorphism $W(G,T)\rightarrow W(G, T')$는 당연히 $nT\mapsto gng^{-1}T'$으로 주어진다. 우리의 두 번째 주장은, 이렇게 얻어지는 다음의 diagram

img

이 commutative diagram이라는 것이다. 

## 딘킨 도표

위의 논의에서 우리는 

