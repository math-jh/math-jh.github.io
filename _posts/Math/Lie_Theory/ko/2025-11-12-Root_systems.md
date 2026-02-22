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

## 리 군의 표현론

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

우리는 따라서 $G$가 *compact* Lie group인 경우를 종종 다루게 된다. 이 경우, locally compact Hausdorff space로서 $G$ 위에는 Haar measure가 존재하며 따라서 $G$의 원소들에 대한 합을 $G$ 전체에 대한 적분으로 바꿔 쓸 수 있다. 물론 이를 위해서는 $\delta_x$ 함수를 잘 정의하고, 함수공간을 적당한 공간으로 일반화하는 작업을 거쳐야 하지만 이러한 작업은 우리의 현재 목적이 아니므로 생략하기로 혼다. 중요한 것은 리 군의 표현론 또한 유한군의 표현론과 같은 방법론을 통해 접근할 수 있다는 것이다. 

## Adjoint representation

Lie group에는 자연스러운 (finite-dimensional) representation $\Ad: G \rightarrow \Aut(\mathfrak{g})$이 존재한다. [§리 군, ⁋정의 19](/ko/math/Lie_theory/Lie_groups#def19) 이는 각각의 $g\in G$가 정의하는 conjugation $h\mapsto ghg^{-1}$의 $h=e$에서의 미분이며, 만일 $G$와 $\Aut(\mathfrak{g})$를 모두 Lie group으로 보아 이를 미분한다면 우리는 $\mathfrak{g}$의 representation

$$\ad: \mathfrak{g}\rightarrow \Lie(\Aut(\mathfrak{g}))$$

을 얻을 수 있으며 [§리 군, ⁋정리 15](/ko/math/Lie_theory/Lie_groups#thm15)을 생각하면 본질적으로 $\Ad$가 알고있는 정보는 여기에 다 담겨있다고 생각해도 된다. 어차피 벡터공간의 Lie algebra를 생각하는 것은 자기자신을 생각하는 것과 같으므로 우리는 $\mathfrak{g}$를 reresentation space $\mathfrak{g}$를 이용하여 표현한다 생각할 수 있고, 이 때 $\ad$는 명시적으로 

$$\ad(X)Y=[X,Y]$$

을 통해 계산해줄 수 있다. 

표현론의 결과들을 사용하는 데에 중요한 것은 임의의 finite-dimensional representation은 항상 unitary라는 것이었다. 이 결과를 증명할 때 사용하는 논리는 $V$ 위에 $G$-invariant inner product를 택할 수 있다는 것인데, 엄밀히 말하자면 우리는 orthogonal complement에 관심이 있으므로 non-degenerate symmetric form만 있어도 충분하다. 그런데 Lie algebra 위에는 자연스러운 bilinear form이 하나 존재한다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Lie algebra $\mathfrak{g}$ 위에 다음의 식

$$K(X,Y)=\tr(\ad(X)\ad(Y))$$

으로 정의된 symmetric bilinear form을 *Killing form*이라 부른다. 

</div>

Killing form이 symmetric이고, $\mathbb{C}$-bilnear인 것은 정의에 의해 자명하다. 심지어 이 Killing form은 별도의 조작을 거치지 않아도 이미 $G$에 의한 adjoint action에 대해 invariant하기도 하다. 즉 다음 식

$$K(\Ad_g(X), \Ad_g(Y))=K(X,Y)$$

이 성립하며, 이를 $g=e$에서 $Z$ 방향으로 미분하면 다음의 $\ad$-invariance

$$0=\frac{d}{dt}\bigg\vert_{t=0}K(\Ad_{\exp(tZ)}X, \Ad_{\exp(tZ)},Y)=K([Z,X],Y)+K(X,[Z,Y])$$

을 얻는다. 남아있는 것은 이것이 non-degenerate인 조건이다. 

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Lie algebra $\mathfrak{g}$이 *simple<sub>단순</sub>*이라는 것은 $\mathfrak{g}$가 non-abelian Lie algebra이고 $\mathfrak{g}$의 ideal이 $0$과 자기자신 뿐인 것이다. Simple Lie algebra들의 direct sum으로 쓸 수 있는 Lie algebra를 *semisimple*이라 부른다. 

</div>

그럼 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> 유한차원 Lie algebra $\mathfrak{g}$에 대하여, 다음이 모두 동치이다. 

1. $\mathfrak{g}$가 semisimple이다.
2. Killing form이 non-degenerate이다.
3. $\mathfrak{g}$가 nonzero abelian ideal을 갖지 않는다. 
4. $\mathfrak{g}$가 nonzero solvable ideal을 갖지 않는다. 
5. $\mathfrak{g}$의 radical이 $0$이다. 

</div>

이에 대한 증명이 당장 중요한 것은 아니므로 넘어가기로 한다. 

## 카르탕 부분대수

선형대수학에서 아주 강력한 도구 중 하나는 대각화이다. 따라서 우리는 주어진 Lie group action $\rho:G \rightarrow \Aut(V)$에 대하여, $V$의 basis를 적당히 택하여 $\rho(g)$의 행렬표현을 대각행렬로 만드는 데에 관심이 있다. 만일 $G$가 유한군이었다면, 각각의 $g$에 대해 이러한 basis를 찾아줄 수 있었겠지만 현재는 $G$가 무한하므로 이러한 일을 하기 힘들다. 따라서 우리는 simultaneously diagonalizable인 원소들에 자연스럽게 관심을 갖게 된다. 

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Semisimple Lie algebra $\mathfrak{g}$에 대하여, $\mathfrak{g}$의 *Cartan subalgebra<sub>카르탕 부분대수</sub>*는 $\ad(H)$가 모든 $H\in \mathfrak{h}$에 대하여 diagonalizable이도록 하는 abelian subalgebra $\mathfrak{h}$ 중 maximal인 것이다. 

</div>

두 diagonalizable operator $A,B$가 simultaneously diagonalizable인 것은 이들 두 operator가 commute하는 것과 동치이므로, 정의에 의하여 $\mathfrak{h}$의 모든 원소들은 simultaneously diagonalizable이다. 

이제 simultaneously diagonalizable operator들의 family $\\{H\in \mathfrak{h}\\}$를 사용하여 $\mathfrak{g}$를 분해하자. 만일 simultaneously diagonalizable operator들의 <em_ko>유한한</em_ko> family $A\_1,\ldots, A\_n$이 주어졌다면, simultaneous eigenspace로 공간을 분해하는 것은 

$$V=\bigoplus V_\alpha,\qquad \text{$A_i v_\alpha=\lambda_i v_\alpha$ for all $v_\alpha\in V$ for all $i$}$$

와 같은 형태이지만, 현재 우리 상황에서는 $\mathfrak{h}$가 벡터공간이므로 linear functional $\mathfrak{\alpha}: \mathfrak{h}\rightarrow \mathbb{C}$를 택하여 $\alpha(H)$가 각각의 $H$의 고유값 역할을 해주도록 하는 것이 낫다. 따라서 다음과 같이 정의한다. 

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> Semisimple Lie algebra $\mathfrak{g}$와 $\mathfrak{g}$의 Cartan subalgebra $\mathfrak{h}$에 대하여, 

$$\Phi=\left\{\alpha\in \mathfrak{h}^\ast\setminus\{0\}\mid \mathfrak{g}_\alpha\neq 0\right\}$$

의 원소들을 $\mathfrak{g}$의 *root*라 부른다. 이 때 

$$\mathfrak{g}_\alpha=\left\{X\in \mathfrak{g}\mid [H,X]=\alpha(H)X\text{ for all $H\in \mathfrak{h}$}\right\}$$

이다. ([§리 군, ⁋정의 19](/ko/math/Lie_theory/Lie_groups#def19))

</div>

정의에 의하여 $\mathfrak{h}$는 자기 자신 위에는 $0$으로 작용한다. 즉 $\mathfrak{h}$는 $\mathfrak{g}$를 simultaneous eigenspace로 분해했을 때 eigenvalue $0$에 해당하는 부분이며 이로부터 우리는 다음의 decomposition

$$\mathfrak{g}=\mathfrak{h}\oplus\bigoplus_{\alpha\in \Phi}\mathfrak{g}_\alpha$$

을 얻는다. 이들이 다음 명제를 만족하는 것은 자명하다. 

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> Seimisimple Lie algebra $\mathfrak{g}$, Cartan subalgebra $\mathfrak{h}$와 그 root decomposition 

$$\mathfrak{g}=\mathfrak{h}\oplus\bigoplus_{\alpha\in\Phi}\mathfrak{g}_\alpha$$

을 생각하고, $K(-,-)$이 $\mathfrak{g}$ 위의 Killing form이라 하자. 다음이 성립한다.

1. 임의의 $\alpha,\beta\in \Phi$에 대하여 $[\mathfrak{g}\_\alpha,\mathfrak{g}\_\beta]\subseteq \mathfrak{g}\_{\alpha+\beta}$가 성립한다. 
2. 만일 $\alpha+\beta\neq 0$이라면 $\mathfrak{g}\_\alpha$와 $\mathfrak{g}\_\beta$는 $K$에 대해 orthogonal이다. 
3. Killing form을 $\mathfrak{g}\_\alpha\otimes \mathfrak{g}\_{-\alpha}$로 제한하면 nondegenerate pairing이 된다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

1. 임의의 $X\in \mathfrak{g}\_\alpha, Y\in \mathfrak{g}\_\beta$, $H\in \mathfrak{h}$에 대하여, 
    
    $$[H,[X,Y]]=[[H,X],Y]+[X,[H,Y]]=[\alpha(H)X,Y]+[X,\beta(H)Y]=(\alpha+\beta)(H)[X,Y]$$

    이 성립한다. 
2. 임의의 $X\in \mathfrak{g}\_\alpha, Y\in \mathfrak{g}\_\beta$, $H\in \mathfrak{h}$에 대하여, $K$의 $\ad$-invariance로부터
    
    $$0=K([H,X],Y)+K(X,[H,Y])=K(\alpha(H),X)+K(X,\beta(H)Y)=(\alpha+\beta)(H)K(X,Y)$$

    을 얻는다. 만일 $\alpha+\beta\neq 0$이라면 이 식이 항상 성립하기 위해서는 $K(X,Y)=0$이 항상 성립해야 한다.
3. Killing form은 $\mathfrak{g}$에서는 non-degenerate이므로, 임의의 $X\in \mathfrak{g}\_\alpha$가 주어졌을 때마다 $K(X,Z)\neq 0$이도록 하는 $Z\in \mathfrak{g}$가 존재한다. 보여야 할 것은 $Z\in \mathfrak{g}\_{-\alpha}$이도록 할 수 있다는 것이다. 이는 $Z$를 root decompose한 후 둘째 결과에 의해 $-\alpha$가 아닌 나머지 부분에 해당하는 성분들은 어차피 $X$와 pairing해봤자 $0$이 되기 때문에 자명하다.

</details>

## 원환면의 작용

우리는 남은 글에서, 위에서 정의한 root $\Phi$들이 갖는 성질을 이용하여 simple Lie algebra의 classification을 진행할 것이다. 그 전에 위의 decomposition이 기하학적으로는 어떠한 꼴인지 살펴보는 것이 이해에 도움이 된다. 

우리는 임의의 torus $T$에 대하여, $T$는 abelian이고 따라서 $T$의 임의의 irreducible representation $V$는 $1$차원이라는 것을 안다. 바꾸어 말하자면, 임의의 representation $T\rightarrow\Aut(V)$가 주어졌다 하면, 이를 irreducible subrepresentation으로 분해하여 다음의 식

$$V=\bigoplus_{i}V_i$$

을 얻고, 각각의 $V_i$는 $1$차원이다. 이 때 각각의 $V_i$ 위에서는 $T$의 action이 훨씬 명시적인데, 이는 $V_i$가 $1$차원인 것으로부터 $\Aut(V_i)\cong \mathbb{C}^\times$이므로, torus action은 continuous homomorphism $\rchi_{\lambda_i}:T \rightarrow \Aut(V_i)\cong \mathbb{C}^\times$로 주어지기 때문이다. 뿐만 아니라 이것이 irreducible이므로 $\lvert\lambda\rvert=1$이고 따라서 각각의 $V_i$ 위에서 torus action은 

$$t\cdot v=\rchi_{\lambda_i}(t)v,\qquad \rchi_{\lambda_i}(t)\in S^1\subset\mathbb{C}^\times$$

으로 주어진다. 한편 우리는 다음의 식

$$\rchi_{\lambda_i}(\exp(X))=e^{2\pi i \lambda_i(X)}\qquad\text{for all $X\in \mathfrak{t}$}\tag{1}$$

을 통해 $T$의 character $\rchi_{\lambda_i}$와 $\mathfrak{t}$ 위에 정의된 linear functional $\lambda_i$ 사이의 일대일 대응이 있는 것을 안다. 


직관적으로 $t\mapsto e^{2\pi i\lambda_i(X)}$를 각속도 $\lambda_i(X)$를 갖는 각운동이라 생각할 수 있고, 이러한 관점을 도입하면 우리는 각각의 $X\in \mathfrak{t}$가 주어졌을 때, 이 방향으로의 각속도 $\lambda_i(X)$가 얼마인지를 통해 이 torus action을 설명할 수 있다는 것을 안다. 이 때 각각의 $\lambda_i$들을 우리는 *weight*라 부른다. 그럼 우리는 각각의 weight $\lambda_i$마다 적당한 $V_i$가 존재하여, 이 위에서는 torus action이 $t\cdot v=\rchi_{\lambda_i}(t)v$로 작동하는 것을 안다. 이러한 $V_i$를 *weight space*라 부른다. 

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> 특별한 예시로, 1차원 torus

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

직관적으로 weight decomposition은 일종의 eigenspace decomposition으로 생각할 수 있으며, 이것이 우리가 real vector space 대신 complex vector space를 생각하는 이유이다. 한편 eigenspace decomposition에서와 마찬가지로, 각각의 weight에 대한 중복도가 $1$일 필요는 없다. 가령 다음의 torus action

$$e^{2\pi i t}\cdot(z_1, z_2)=(e^{4\pi i t}z_1, e^{4\pi i t} z_2)$$

를 생각하면 이번에는 2차원 공간 $\mathbb{C}^2$ 위에서 $T$가 weight $2$를 갖는 것처럼 행동하기 때문이다. 이와 같이 서로 같은 weight $\lambda$들을 갖는 성분들을 한데 모아 이를 $V_\lambda$라 하면, 우리는 *weight space decomposition* $V=\bigoplus V_\lambda$를 얻는다. 지금까지의 논의를 엄밀하게 정의로 적으면 다음과 같다. 

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> Torus $T$와 complex $T$-module $V$가 주어졌다 하자. Irreducible character $\rchi_\lambda: T \rightarrow S^1$와 그에 해당하는 linear functional $\lambda:\mathfrak{t}\rightarrow\mathbb{C}$에 대하여, $\lambda$가 $V$의 *weight*이라는 것은 다음 집합

$$V_\lambda=\left\{v\in V\mid t\cdot v=\rchi_\lambda(t)v\text{ for all $t\in T$}\right\}$$

이 nontrivial인 것이다. 이 때, $V_\lambda$를 $\lambda$의 *weight space*라 하며, decomposition

$$V=\bigoplus_\lambda V_\lambda$$

을 $V$의 *weight decomposition*이라 부른다. 

</div>

이제 adjoint representation $\Ad: G\rightarrow \Aut(\mathfrak{g})$를 통해 $\mathfrak{g}$를 $G$-module로 보고, $G$의 maximal torus $T$로 이를 제한하면 정확히 $T$에 해당하는 $G$의 Lie subalgebra가 Cartan subalgebra $\mathfrak{h}$의 역할을 하고, 따라서 이 경우에 weight decomposition이 곧 위에서 살펴본 root space decomposition이 된다는 것을 안다. 

## 예시: $\sl(2;\mathbb{C})$

우리는 [§리 군, ⁋명제 12](/ko/math/Lie_theory/Lie_groups#prop12)를 통해 $\sl(n;\mathbb{C})$는 $n\times n$ *traceless* 행렬들의 모임임을 안다. 따라서 $\sl(2;\mathbb{C})$는 다음의 세 원소를 basis로 갖는다. 

$$H=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad E=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad F=\begin{pmatrix}0&0\\1&0\end{pmatrix}$$

따라서 $\sl(2;\mathbb{C})$의 곱셈구조는 다음의 commutation relation들

$$[H,E]=2E,\quad [H,F]=-2F,\quad [E,F]=H$$

을 통해 얻어진다. 

우리는 임의의 $\sl(2;\mathbb{C})$-representation이 irreducible representation들의 direct sum으로 나타난다는 것을 보인다. 이는 compact Lie group에 대해서는 자명한 결과이지만 $\SL(w,\mathbb{C})$와 같은 non-compact group에 대해서는 Haar measure의 존재성이 보장되지 않고 따라서 적분을 통해 내적을 평균내는 등의 아이디어를 사용할 수 없다는 것을 기억하자. 

임의의 finite-dimensional $\sl_2$-representation $V$가 주어졌다 하고, 각각의 $\lambda\in \mathbb{C}$에 대하여 weight space

$$V_\lambda=\{v\in V\mid H\cdot v=\lambda v\}$$

으로 정의하자. 그럼 앞서 살펴본 commutation relation에 의하여 

$$E\cdot V_\lambda\subset V_{\lambda+2},\qquad F\cdot V_\lambda\subset V_{\lambda-2}$$

이 성립한다. 우리는 이러한 이유로 $E,F$를 각각 *raising operator*, *lowering operator*라 부르기도 한다. 한편 $V$는 유한차원이므로 weight decomposition

$$V=\bigoplus_{\lambda} V_\lambda$$

를 생각하면, $V_\mu\neq 0$이지만 $V_{\mu+2}=0$이 성립하는 $\mu$가 존재한다. 이러한 $\mu$를 *heighest weight*이라 부르고, $V_\mu$의 원소를 *highest weight vector*라 부른다. 그럼 highest weight vector $v$에 대하여 우리는 다음의 두 식

$$H\cdot v=\mu v,\qquad E\cdot v=0$$

이 성립하는 것을 안다.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> 임의의 highest weight $v_0\in V_\mu$에 대하여, 

$$v_j=\frac{1}{j!}F^j v_0$$

으로 정의하면 다음이 성립한다.

$$H\cdot v_j=(\mu-2j)v_j,\quad F\cdot v_j=(j+1)v_{j+1},\quad E\cdot v_j=(\mu-j+1)v_{j-1}.$$

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

처음 두 식은 자명하므로, $E$에 대한 식만 보이면 충분하다. 귀납법으로 진행한다. $j=0$인 경우는 자명하며, 만일 주어진 식이 $j$에 대해 성립한다면

$$E\cdot v_{j+1}=\frac{1}{j+1}EF\cdot v_j=\frac{1}{j+1}(FE+H)\cdot v_j$$

이고, 귀납적 가정에 의해

$$E\cdot v_j=(\mu-j+1)v_{j-1}$$

이고 $H$에 대한 식으로부터 $H\cdot v_j=(\mu-2j)v_j$이므로 이들을 대입하면 원하는 결과를 얻는다. 

</details>

한편 $V$가 유한차원이므로, $v_{m+1}=0$을 만족하는 가장 작은 정수 $m$이 존재한다. 그럼 이러한 $m$에 대하여, 

$$0=E\cdot v_{m+1}=(\mu-m)v_m$$

과 $m$의 최소성으로부터 $\mu=m$이어야 한다는 것을 안다. 즉 highest weight는 반드시 양의 정수이다. 

<div class="definition" markdown="1">

<ins id="def11">**정의 11**</ins> 고정된 정수 $m\geq 0$에 대하여, $\sl_2$의 representation $V(m)$을 $m+1$개의 vector들 $v_0,\ldots, v_m$과, [명제 10](#prop10)의 action 

$$H\cdot v_j=(m-2j)v_j,\quad F\cdot v_j=(j+1)v_{j+1},\quad E\cdot v_j=(m-j+1)v_{j-1}$$

을 주어 정의한다. $v_{-1}=v_{m+1}=0$이다. 

</div>

어렵지 않게 $V(m)$은 irrducible인 것을 보일 수 있다. 이제 임의의 $\sl_2$-representation $V$에 대하여, 우리는 $V$의 highest weight을 찾은 후 highest weight vector에 대하여 [명제 10](#prop10)을 적용하고, 남아있는 highest weight vector가 있다면 다시 이를 반복하는 식으로 $V$를 irreducible $\sl_2$-representation으로 분해할 수 있다. 

## 근계

위의 $\sl_2$-representation의 예시는 앞으로 해나갈 이야기에 큰 역할을 한다. 우선 다음을 정의하자. 

<div class="definition" markdown="1">

<ins id="def12">**정의 12**</ins> 유한차원 벡터공간 $V$와 그 위에 정의된 inner product $( -,-)$을 고정하자. $V$의 non-zero vector들의 유한한 집합 $\Phi$가 *root system*이라는 것은 다음의 조건들이 만족되는 것이다. 

1. $\Phi$의 원소들이 $V$를 span한다. 
2. 만일 $\alpha\in \Phi$이고 $c\in \mathbb{R}$이라면 $c\alpha\in \Phi$이기 위해서는 $c=\pm 1$이어야 한다. 
3. 각각의 root $\alpha\in\Phi$에 대하여, $\Phi$는 $\alpha$에 수직인 초평면에 대한 대칭이동 $s_\alpha$에 대해 닫혀있다. 즉, 임의의 $\alpha,\beta\in \Phi$에 대하여
    
    $$s_\alpha(\beta):=\beta-2\frac{(\beta,\alpha)}{(\alpha,\alpha)}\alpha\in \Phi$$

    이다. 
4. 임의의 root $\alpha,\beta\in\Phi$에 대하여, 다음 식
    
    $$\langle \beta,\alpha\rangle:=2\frac{(\beta,\alpha)}{(\alpha,\alpha)}$$

    은 항상 정수이다. 

</div>

이제 semisimple complex Lie algebra $\mathfrak{g}$의 Cartan subalgebra $\mathfrak{h}$를 고정하자. 그럼 우선 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="lem13">**보조정리 13**</ins> Semisimple Lie algebra $\mathfrak{g}$, Cartan subalgebra $\mathfrak{h}$, 그리고 root decomposition

$$\mathfrak{g}=\mathfrak{h}\oplus\bigoplus_{\alpha\in \Phi} \mathfrak{g}_\alpha$$

에 대하여 다음이 성립한다. 

1. 임의의 $\alpha,\beta\in \Phi$에 대하여 $[\mathfrak{g}\_\alpha,\mathfrak{g}\_\beta]\subseteq \mathfrak{g}\_{\alpha+\beta}$가 성립한다.
2. 만일 $\alpha+\beta\neq 0$이라면 $\mathfrak{g}\_\alpha$와 $\mathfrak{g}\_\beta$가 orthogonal이다. 
3. $\mathfrak{g}$ 위에 정의된 Killing form을 $\mathfrak{h}$로 제한한 것은 non-degenerate이다. 
4. $\mathfrak{g}$ 위에 정의된 Killing form은 $\mathfrak{g}\_\alpha\times \mathfrak{g}\_{-\alpha} \rightarrow \mathbb{C}$로 제한했을 때 non-degenerate이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

처음 주장은 자명하다. 둘째 주장의 경우, 임의의 $X\_\alpha\in \mathfrak{g}\_\alpha,X\_\beta\in \mathfrak{g}\_\beta$ 그리고 임의의 $H\in \mathfrak{h}$에 대하여, $K$의 $\ad$-invariance로부터 다음의 식

$$0=K([H,X_\alpha],X_\beta)+K(X_\alpha, [H,X_\beta])=K(\alpha(H)X_\alpha, X_\beta)+K(X_\alpha,\beta(H)X_\beta)=(\alpha+\beta)(H)K(X_\alpha,X_\beta)$$

을 얻는다. 따라서 $\alpha+\beta\neq 0$이라면 $\mathfrak{g}\_\alpha$와 $\mathfrak{g}_\beta$는 $K$에 대해 orthogonal이다. 

이제 셋째 주장을 보이기 위해 임의의 $H\in \mathfrak{h}$에 대하여 $X\in \mathfrak{g}$가 존재하여 $K(H,X)\neq 0$이도록 할 수 있다는 것을 기억하자. 새롭게 보여야 할 것은 $X$를 $\mathfrak{h}$에서 뽑을 수 있다는 것이다. 이를 위해 $X$를 root decomposition $\sum X_\alpha$의 꼴로 쓰면, 우리는 위의 결과에 의하여 $K(H,-)$를 취했을 때 $X_0\in \mathfrak{h}$를 제외한 모든 $X_\alpha$가 $0$을 준다는 것을 안다. 따라서 $K(H,H_0)\neq 0$이다. 

넷째 주장은 셋째 주장과 정확히 동일하게 증명하면 된다.

</details>

이제 $\mathfrak{g}$ 위에 정의된 Killing form이 $\mathfrak{h}$위에서도 non-degenerate이므로 이로부터 유도되는 다음의 isomorphism

$$\mathfrak{h}\rightarrow \mathfrak{h}^\ast;\qquad H\mapsto K(H, -)$$

이 존재한다. 그럼 $\Phi\subseteq \mathfrak{h}^\ast$는 $\mathfrak{h}^\ast$의 spanning set이다. $\Phi$의 원소들의 일차결합으로 나타나지 않는 $\mathfrak{h}^\ast$의 원소가 있다 하면, 이에 해당하는 $\mathfrak{h}$의 원소는 모든 $\alpha\in H$에 대하여 $\alpha(H)$를 만족하여야 한다. 이제 임의의 root space $\mathfrak{g}_\alpha$에 대하여, $H$는

$$[H,X]=\alpha(H)X=0\qquad\text{for all $X\in \mathfrak{g}_\alpha$}$$

으로 작용하고, $\mathfrak{h}$는 abelian이므로 이 위에는 $0$으로 작용한다. 즉 $\mathfrak{g}$의 root decomposition을 생각하면 $H$는 $\mathfrak{g}$ 위의 모든 원소에 대하여 $0$으로 작용하고, 이로부터 $H$는 $\mathfrak{g}$의 모든 원소와 Lie bracket에 대해 commute함을 안다. 그런데 [명제 4](#prop4)에 의하여 $\mathfrak{g}$는 nonzero abelian ideal을 가질 수 없고, 특히 $Z(\mathfrak{g})=0$이 성립해야 하므로 $H=0$이어야 한다. 

이로부터 $\Phi$는 $\mathfrak{h}^\ast$을 span하는 것을 안다. 그러나 $\mathfrak{h}^\ast$는 complex vector space이고, 이 위에 정의된 Killing form 또한 positive definite라는 보장이 없으므로 inner product가 아니다. 이를 해소하기 위해 우리는 $\Phi$의 dual element들의 real span을 생각하고 여기로 Killing form을 제한했을 때 positive-definite가 된다는 것을 보인다. 이를 위해서는 root decomposition에 대한 조금 더 자세한 분석이 필요하다. 

각각의 root들 $\alpha\in\Phi$에 대하여, Killing form의 non-degeneracy로부터 다음의 식

$$\alpha(X)=K(H_\alpha,X)\qquad\text{for all $X\in \mathfrak{h}$}$$

을 만족하는 $H_\alpha\in \mathfrak{h}$이 존재한다. 우리의 첫 번째 관찰은 다음의 보조정리이다. 

<div class="proposition" markdown="1">

<ins id="lem14">**보조정리 14**</ins> 임의의 $E\in \mathfrak{g}\_\alpha$와 $F\in \mathfrak{g}\_{-\alpha}$에 대하여, $[E,F]=K(E,F)H\_\alpha$이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$K$의 $\ad$-invariance에 의하여

$$K([E,F],H)=K(F,[H,E])$$

이 모든 $H\in \mathfrak{h}$에 대해 성립한다. 한편 $E\in \mathfrak{g}_\alpha$이므로

$$[H,E]=\alpha(H)E=K(H_\alpha,H)E$$

이고 이를 위의 식에 대입하면

$$K([E,F],H)=K(F,[H,E])=K(F, K(H_\alpha,H)E)=K(H_\alpha,H)K(F,E)=K(K(F,E)H_\alpha,H)$$

이 모든 $H$에 대해 성립하므로 원하는 결과를 얻는다. 

</details>

한편 우리는 [보조정리 13](#lem13)으로부터 $E\in \mathfrak{g}\_\alpha$, $F\in \mathfrak{g}\_{-\alpha}$를 택하여 $K(E,F)\neq 0$이도록 할 수 있다. 그럼 위의 결과로부터 이들은 다음의 relation

$$[E,F]=K(E,F)H_\alpha,\quad [H_\alpha,E]=\alpha(H_\alpha)E=K(\alpha,\alpha)E,\quad [H_\alpha,F]=-\alpha(H_\alpha)F=-K(\alpha,\alpha)F$$

를 만족한다는 것을 안다. 이는 위에서 살펴본 $\sl_2$-representation의 commutation relation과 유사한 꼴이며, 실제로 어렵지 않게 $(\alpha,\alpha)\neq 0$임을 보일 수 있다. 따라서

$$h_\alpha=\frac{2}{K(\alpha,\alpha)}H_\alpha$$

으로 정의하고, 비슷하게 $E$와 $F$ 대신 적절한 scaling을 통해

$$(e_\alpha,f_\alpha)(\alpha,\alpha)=2$$

을 만족하는 $e\_\alpha\in \mathfrak{g}\_\alpha$, $f\_\alpha\in \mathfrak{g}\_{-\alpha}$을 택할 수 있으며 이들은 다음 commutation relation

$$[e_\alpha,f_\alpha]=h_\alpha,\quad [h_\alpha,e_\alpha]=2e_\alpha,\quad [h_\alpha,f_\alpha]=-2f_\alpha$$

을 만족한다. 즉 이들은 $\mathfrak{g}$ 안에서 $\sl_2$과 isomorphic한 subalgebra를 준다. 이를 $\sl_{2,\alpha}$라 하자. 그럼 adjoint action을 통해 $\mathfrak{g}$를 $\sl_{2,\alpha}$-representation으로 볼 수 있다. 

특히 $h_\alpha$가 $\mathfrak{g}$의 원소들에 어떻게 작용하는지를 살펴보자. 우선 \mathfrak{g}$의 root space $\mathfrak{g}_\beta$에 $h_\alpha$의 adjoint action이 어떻게 작용하는지를 보면

$$[h_\alpha, x]=\beta(h_\alpha)x\qquad\text{for all $x\in \mathfrak{g}_\beta$}$$

이므로 $\mathfrak{g}\_\beta$는 이 action에 대한 weight $\beta(h\_\alpha)$의 weight space이다. 그런데 앞서 살펴봤듯 $\sl\_2$-representation의 weight은 항상 정수이므로, 이 값 $\beta(h\_\alpha)=\frac{2K(\alpha,\beta)}{K(\alpha,\alpha)}$은 반드시 정수여야 함을 안다. 또 $\sl_2$ representation의 임의의 weight subspace는 $1$차원이므로 각각의 $\mathfrak{g}_\beta$들도 $1$차원이다. 

한편, 앞서 우리는 $\mathfrak{h}$이 $H_\alpha$들에 의해 생성되는 것을 보았으므로, 그 상수배인 $h_\alpha$들도 $\mathfrak{h}$를 생성한다. 앞서 말했듯 우리는 여기에 root system 구조를 주기 위해 $h_\alpha$들로 생성되는 *real* vector space

$$\mathfrak{h}_\mathbb{R}=\span_\mathbb{R}\{h_\alpha\mid \alpha\in\Phi\}$$

을 생각할 것이다. 그럼 이 위에서 두 basis $h_\alpha,h_\beta$에 대하여

$$K(h_\alpha,h_\beta)=\tr_\mathfrak{g}(\ad h_\alpha\ad h_\beta)=\sum_{\gamma\in\Phi}\gamma(h_\alpha)\gamma(h_\beta)$$

가 성립한다. 우리는 앞서 이들 $\gamma(h_\alpha),\gamma(h_\beta)$들이 정수임을 증명하였으며 따라서 $K(h_\alpha,h_\beta)$도 그러하다. 즉, $\mathfrak{h}_\mathbb{R}$로 제한했을 때 $K$는 real-valued이며, 이제 임의의 $h\in \mathfrak{h}_\mathbb{R}$에 대하여

$$K(h,h)=\tr(\ad_h\ad_h)=\sum_{\gamma\in\Phi}\gamma(h)^2\geq 0$$

을 주므로 우리는 $K$가 $\mathfrak{h}_\mathbb{R}$ 위에서 positive definite인 것을 안다. 특히 이를 다시 $\mathfrak{h}^\ast$로 옮겨주면 $\mathfrak{h}^\ast$에서 $\Phi$의 real span이 Euclidean space를 이룬다는 것을 확인할 수 있고, 이를 보이는 과정에서 우리는 이들 root들이 [정의 12](#def12)의 네 번째 조건을 만족하는 것도 보였다. 이제 우리가 보여야 할 것은 나머지 조건들이다. 

우선 reflection operator를 적용한

$$s_\alpha(\beta)=\beta-\frac{2K(\alpha,\beta)}{K(\alpha,\alpha)}\alpha$$

가 다시 root가 된다는 것을 보여야 하는데, 이는 $\ad f_\alpha$를 $\lvert \beta(h_\alpha)\rvert$번 작용하면 $\mathfrak{g}\_\beta$와 $\mathfrak{g}\_{s_\alpha(\beta)}$ 사이의 isomorphism이 얻어지기 때문에 자명하다. 

둘째 조건의 경우, 만일 $\beta=c\alpha$라 한다면

$$\frac{2K(\alpha,\beta)}{K(\alpha,\alpha)}=2c,\quad \frac{2K(\alpha,\beta)}{K(\beta,\beta)}=\frac{2}{c}$$

가 모두 정수이기 위해서는 $c$는 $\pm 1$, $\pm 2$, $\pm 1/2$ 중 하나여야 하고, 다시 이를 $\sl_2$-representation theory로 옮긴 후 integrality를 적용하면 원하는 결과를 얻는다. 즉 우리는 다음을 증명하였다. 

<div class="proposition" markdown="1">

<ins id="prop15">**명제 15**</ins> [정의 4](#def4)에서 정의한 root들의 모임 $\Phi$는 $\mathfrak{h}^\ast$의 root system이다. 

</div>

## 예시들

이제 다음의 예시들을 살펴보자. 

<div class="example" markdown="1">

<ins id="ex16">**예시 16**</ins> 우선 standard Euclidean space $\mathbb{R}^{n+1}$을 생각하고, $\mathbb{R}^{n+1}$의 subspace

$$V_n=\left\{(x_1,\ldots, x_{n+1}\mid x_1+\cdots+x_{n+1}=0\right\}$$

을 생각하자. 우리는 이 벡터공간의 부분집합

$$\Phi(A_n)=\left\{e_i-e_j\mid 1\leq i\neq j\leq n+1\right\}$$

을 생각한다. 그럼 이 집합이 [정의 5](#def5)의 조건을 모두 만족하는 것을 안다. 첫째 조건인 $\Phi(A_n)$이 $V_n$을 span하는 것과, 둘째 조건이 성립하는 것은 자명하다. 셋째 조건의 경우, 임의의 벡터 $\mathbf{x}=(x_1,\ldots, x_{n+1})$와 임의의 $\mathbf{e}_{ij}=e_i-e_j$에 대하여 다음 식

$$s_{ij}(\mathbf{x})=\mathbf{x}-\langle \mathbf{x}, \mathbf{e}_{ij}\rangle\mathbf{e}_{ij}=(x_1,\ldots, x_{n+1})-(x_i-x_j)\mathbf{e}_{ij}$$

이고 이는 $\mathbf{x}$의 $i$번째와 $j$번째의 성분을 바꾼 것으로 주어진다. 따라서 이로부터 [정의 5](#def5)의 셋째 조건이 성립하는 것을 알고 넷째 조건은 자명하다. 또, 위의 계산으로부터 $W(\Phi(A_n))$은 $\Phi(A_n)$의 각각의 성분을 교환하는 것으로 주어지는 것을 안다. 즉 $W(\Phi(A_n))\cong S_{n+1}$이다. 

</div>

비슷하게 다음의 예시를 생각할 수 있다. 

<div class="example" markdown="1">

<ins id="ex17">**예시 17**</ins> 이번에는 standard Euclidean space $\mathbb{R}^n$을 생각하자. 이번에는 다음 집합

$$\Phi(D_n)=\left\{\pm e_i\pm e_j\mid 1\leq i \neq j\leq n\right\}$$

을 생각한다. 이들 벡터들이 $\mathbb{R}^n$을 span하는 것은 자명하다. 이번에는 임의의 $\mathbf{e}_{ij}^\pm =e_i\pm e_j$들이 어떠한 reflection을 정의하는지를 살펴보아야 한다. 우리는 $e_i-e_j$들이 벡터 $\mathbf{x}$의 $i$번째와 $j$번째 성분을 바꿔주는 것을 알고 있으며 따라서 $e_i+e_j$가 어떠한 reflection을 정의하는지를 알뗜 충분하다. 즉 다음의 계산

$$s_{ij}^+(\mathbf{x})=\mathbf{x}-\langle\mathbf{x}, \mathbf{e}_{ij}^+\rangle\mathbf{e}_{ij}^+=(x_1,\ldots, x_n)-(x_i+x_j)\mathbf{e}_{ij}$$

을 생각하면, $s_{ij}^+$는 주어진 벡터의 $i$번째 성분과 $j$번째 성분을 바꾼 후 부호까지 반대로 바꾸어주는 것이다. 즉 Weyl group은 semidirect product

$$(\mathbb{Z}/2\mathbb{Z})^{n-1}\rtimes S_n$$

이 된다. 

</div>

위의 예시들에서 살펴볼 수 있듯이 root system을 묘사하기 위해 모든 root들이 필요한 것은 아니다. 가령 $\Phi(A_n)$의 경우, 

$$e_i-e_k=(e_i-e_j)+(e_j-e_k)$$

이 성립하며 이로부터 $\Phi(A_n)$을 묘사하기 위해서는 $e_i-e_{i+1}$ 꼴의 원소들만 필요함을 안다. 이와 비슷한 방식으로 우리는 다음을 정의한다. 

<div class="definition" markdown="1">

<ins id="def18">**정의 18**</ins> Root system $\Phi$에 대하여, 우리는 $\Phi$의 부분집합 $\Phi^+$가 *positive root*들의 부분집합이라는 것은 각각의 root $\alpha\in \Phi$에 대하여, $\alpha$와 $-\alpha$ 중 정확하게 하나만이 $\Phi$에 속하며, 임의의 두 $\alpha,\beta\in \Phi^+$가 주어질 때마다 $\alpha+\beta\in \Phi^+$ 또한 성립하는 것이다. Simple root들의 모임 $\Phi^+$을 고정하였을 때, $\Phi^+$의 원소 $\alpha$가 *simple root*라는 것은 $\alpha$를 $\Phi^+$의 두 원소들의 합으로 나타낼 수 없는 것이다. 

</div>

따라서 simple root들 사이의 정수값들 

$$\langle\alpha_i,\alpha_j\rangle=2\frac{(\alpha_i,\alpha_j)}{(\alpha_j,\alpha_j)}$$

들이 어떻게 정의되었는지만 안다면, 임의의 root $\alpha_j$에 대한 reflection $s_j$가 다른 root $\alpha_i$을 어떻게 옮기는지를 알 수 있고 따라서 이들이 Weyl group에 대한 정보를 모두 갖고 있다. 

이제 root system $\Phi$와 simple root들의 모임 $\Delta=\left\\{\alpha_1,\ldots, \alpha_l\right\\}$이 고정되었다고 하자. 그럼 *Cartan matrix*는 다음과 같이 정의된다. 

<div class="definition" markdown="1">

<ins id="def19">**정의 19**</ins> 위와 같은 세팅에서, 다음의 행렬

$$A=(a_{ij})_{1\leq i,j\leq l},\qquad a_{ij}=\langle \alpha_i,\alpha_j\rangle$$

을 *Cartan matrix*라 부른다. 

</div>

Root system의 정의에 의하여 각각의 성분 $a_{ij}$는 정수이다. 또 각각의 $i$에 대하여 $a_{ii}=2$인 것 또한 자명하다. 

한편, 우리는 다음의 식

$$\langle\alpha,\beta\rangle \langle\beta,\alpha\rangle=4\frac{(\alpha,\beta)^2}{\lvert\alpha\rvert^2\lvert\beta\rvert^2}=4(\cos\theta)^2$$

과, 좌변이 정수라는 사실로부터 임의의 두 root $\alpha,\beta$에 대해 $\langle\alpha,\beta\rangle$이 취할 수 있는 값은 $0, \pm 1, \pm 2$ 뿐인 것을 안다. 여기서 $\cos\theta$는 두 root $\alpha,\beta$가 이루는 사잇각이며 이것이 취할 수 있는 값은

$$0, \pm \frac{1}{2}, \pm \frac{\sqrt{2}}{2}, \pm \frac{\sqrt{3}}{2}, \pm 1$$

이 된다. 여기서 $\pm 1$의 경우는 [정의 5](#def5)의 둘째 조건에 의해 배제되므로 root들은 각각 $30$도 (혹은 $150$도), $45$도 (혹은 $135$도), $60$도 (혹은 $120$도)의 각도만 이룰 수 있다. 

예시를 위해 만일 두 root $\alpha,\beta$가 이루는 각이 $30$도이거나 $150$도라 하자. 그럼

$$\langle\alpha,\beta\rangle\langle\beta,\alpha\rangle=3$$

으로부터 $\langle\alpha,\beta\rangle$은 $\pm 1$이거나 $\pm 3$이어야 한다. 이제 다음 식

$$\langle \alpha,\beta\rangle =2\frac{(\alpha,\beta)}{(\beta,\beta)}=\frac{2\lvert\alpha\rvert\lvert\beta\rvert\cos\theta}{\lvert\beta\rvert^2}=\frac{\pm \sqrt{3}\lvert\alpha\rvert}{\lvert\beta\rvert}$$

의 값이 $\pm 1$ 혹은 $\pm 3$이라는 것으로부터 우리는 $\alpha$와 $\beta$의 길이비가 $\sqrt{3}$이어야 함을 안다. 비슷하게 두 root $\alpha,\beta$가 이루는 각이 $45$도 혹은 $135$도라면, 이들 두 root의 길이비는 $\sqrt{2}$여야 하고 $60$도 혹은 $120$도의 경우에는 길이비가 $1$이어야 함을 안다.
