---

title: "특성류"
excerpt: ""

categories: [Math / Algebraic Topology]
permalink: /ko/math/algebraic_topology/characteristic_classes
header:
    overlay_image: /assets/images/Math/Algebraic_Topology/Characteristic_classes.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_topology-ko"

date: 2025-10-07
last_modified_at: 2025-10-07
weight: 10

---

이전 글에서 중요한 역할을 했던 $p:\Spe(\or_M^A)\rightarrow M$은 covering space로, 이들은 다음과 같은 성질을 가지고 있었다. 

1. 임의의 $x\in M$에 대하여, $p^{-1}(x)\cong \\{x\\}\times A^\times$이다. 
2. 뿐만 아니라, 임의의 $x\in M$에 대하여, 적당한 열린집합 $U$가 존재하여 $p^{-1}(U)\cong U\times A^\times$이다.

이제 우리는 이를 더 일반화하여 $p^{-1}(x)$ 위에 (discrete set이 아닌) 추가적인 구조가 있는 경우를 살펴본다. 가장 일반적인 정의는 다음과 같다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 위상공간 사이의 contiuous surjection $p:E \rightarrow B$, 그리고 위상공간 $F$에 대하여 *fiber bundle<sub>올다발</sub>*이라는 것은 각각의 $x\in B$마다 열린집합 $U$가 존재하여, 다음의 diagram

![fiber_bundle](/assets/images/Math/Algebraic_Topology/Characteristic_classes-1.png){:style="width:10em" class="invert" .align-center}

을 commute하게 하는 homeomorphism $\phi:U\times F\rightarrow p^{-1}(U)$가 존재하는 것이다. 

</div>

이 때, $B$는 이 bundle의 *base space*, $E$는 *total space*, $F$는 *fiber*라 칭하며, 만일 $U=B$로 택할 수 있으면 이 fiber bundle을 *trivial bundle*이라 부른다. 가령 앞선 예시에서 $M$이 base space, $\Spe(\or_M^A)$는 total space이며 discrete topology가 주어진 $A^\times$가 fiber가 된다. 더 일반적으로 임의의 covering space는 그 fiber가 discrete topology가 부여된 fiber bundle이라 할 수 있다.

특별히 우리가 관심을 가지는 경우는 fiber $F$가 벡터공간일 경우와, topological group일 경우의 두 가지이다. 편의상 앞으로 $B$는 connected인 것으로 가정한다. 

## 벡터다발

우선 우리는 $F$가 벡터공간일 경우를 생각한다. Fiber $F$가 topological group일 경우, $F$는 이미 위상구조가 부여되어 있으므로 [정의 1](#def1)에서 product space $U\times F$의 위상구조가 명확하지만 벡터공간일 경우는 다소 애매하다. 가장 일반적인 세팅으로는 topological ring $\mathbb{K}$이 작용하는 topological vector space $V$념을 사용하면 되지만, 우리는 편의를 위해 당장은 $F$의 base field가 $\mathbb{R}$이고, $F$는 canonical inner product로부터 오는 metric topology가 부여된 공간인 경우만 생각하기로 한다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Fiber bundle $p:E \rightarrow B$에 대하여, fiber space $F$가 위와 같이 위상구조가 주어진 $\mathbb{R}$-벡터공간이고, 추가로 임의의 $x\in B$와, [정의 1](#def1)의 homeomorphism $\phi:U\times  F\rightarrow p^{-1}(U)$에 대하여 다음의 함수

$$\phi(x,-):F \rightarrow p^{-1}(x);\qquad v\mapsto \phi(x,v)$$

가 벡터공간 사이의 isomorphism인 것이다. 

</div>

이를 통해 각각의 fiber $p^{-1}(x)$에는 $F$로부터 물려받는 vector space 구조가 정의된다. 일반적으로 두 vector bundle $p_1:E_1 \rightarrow B_1$과 $p_2:E_2\rightarrow B_2$가 주어졌을 때, 이들 사이의 *morphism*은 연속함수들의 commutatuve diagram

![morphism_of_bundles](/assets/images/Math/Algebraic_Topology/Characteristic_classes-2.png){:style="width:7em" class="invert" .align-center}

을 의미한다. 단, 여기에서 $g$를 각각의 $x\in B_1$에 대하여 $p^{-1}(x)\rightarrow p_2^{-1}(f(x)))$로 제한하였을 때 이 함수가 벡터공간들 사이의 linear map이 되어야 한다.  Vector bundle들 사이의 isomorphism을 어떻게 정의해야 하는지는 자명하다. 

한편 위의 [정의 2](#def2)에서, 우리는 $F$가 $\mathbb{R}$-벡터공간인 경우만 생각하여, $\mathbb{R}^n$ 위에 정의된 inner product 구조와 $\mathbb{R}$의 위상구조를 사용하여 이 위에 위상구조를 정의했다. 하지만 엄밀히 말하자면 여기서 필요한 정보는 오직 vector space $F$의 위상구조 뿐으로, $F$를 inner product space로 보았을 때 이는 *Euclidean bundle*이라 부른다. 어쨌든 우리는 대체로 $\mathbb{R}$-벡터공간만 생각할 것이므로 이러한 차이는 넘어가기로 한다. 

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> Trivial bundle이 아닌 예시로는 뫼비우스 띠의 orientation double cover가 있다. 한편 [§푸앵카레 쌍대성, ⁋예시 3](/ko/math/algebraic_topology/Poincare_duality#ex3)에서 우리는 $S^1$의 non-trivial cover또한 생각했었는데, 이는 다음과 같이 기하학적으로 일반화할 수 있다. 

$n+1$차원 벡터공간 $\mathbb{R}^{n+1}$에 대하여, 원점을 지나는 직선들의 공간을 우리는 *projective $n$-space*라 부르고 $\RP^n$으로 표기한다. 원점을 지나는 직선 위의 점들 중, 원점까지의 거리가 $1$인 두 점은 같은 직선을 지정하므로, 우리는 이를 unit $n$-sphere $S^n$ 위의 antipodal point들을 identify하여 얻어지는 quotient space로 생각할 수 있다. 

이제 이 공간 $\RP^n$을 base space $B$로 두고, 이 위에 정의된 vector bundle $\mathcal{O}(-1)$를 다음과 같이 정의하자. 집합으로서 

$$\mathcal{O}(-1)=\{((x,v)\in \RP^n\times \mathbb{R}^{n+1}\mid x\in \span(x)\}$$

으로 정의되며, projection $\gamma_n^1:\mathcal{O}(-1)\rightarrow \RP^n$는 첫 번째 좌표로의 projection이다. 즉 $\gamma_n^1$는 각 점 $x\in \RP^n$마다, $x$가 원래 $\mathbb{R}^{n+1}$에 있을 때 속해있던 바로 그 직선을 붙여준 것이다.

이는 trivial bundle이 아니다. 만일 이것이 trivial bundle이었다면, non-vanishing continuous section $\RP^n\rightarrow \mathcal{O}(-1)$이 존재했을 것이다. 가령 $B$의 모든 점에 fiber의 $1$을 대응시키는 함수가 그러하다. 그런데 임의의 section $s:\RP^n \rightarrow \mathcal{O}(-1)$이 주어졌다 하고, quotient map $q:S^n \rightarrow \RP^n$을 사용한 다음의 합성

$$S^n \overset{q}{\longrightarrow} \RP^n \overset{s}{\longrightarrow} E\overset{\pr_2}{\longrightarrow} \mathbb{R}^{n+1}$$

을 생각하면 이 함수는 $\mathbf{x}\in S^n\subset\mathbb{R}^{n+1}$을 $\mathbf{x}$의 상수배로 보낸다. 이 상수를 $t(\mathbf{x})$라 하면, $t$는 $S^n$에서 $\mathbb{R}$로의 연속함수이고 quotient map $q$로 인하여

$$t(-\mathbf{x})=-t(\mathbf{x})$$

를 만족한다. 이제 $S^n$은 connected이므로 중간값정리에 의하여 $t(\mathbf{x}_0)=0$을 만족하는 $\mathbf{x}_0\in S^n$이 존재한다. 

</div>

더 일반적으로 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> 위상공간 $B$ 위에 정의된 vector bundle $E$ of rank $n$에 대하여, $E$가 trivial bundle인 것은 everywhere linearly independent인 $n$개의 section들 $s_1,\ldots, s_n$이 존재하는 것과 동치이다. 

</div>

한편 임의의 vector bundle $p:E \rightarrow B$와 임의의 연속함수 $f:B'\rightarrow B$가 주어졌을 때, 우리는 다음의 식

$$f^\ast E=\{(x,v)\in B'\times E\mid f(x)=p(v)\}\subset E$$

로 두어 새로운 vector bundle $f^\ast E \rightarrow B'$를 정의할 수 있다. 우리는 이를 *pullback bundle*이라 부르며, 어렵지 않게 임의의 vector bundle $E' \rightarrow B'$가 위의 조건을 만족한다면 $f^\ast E$를 factor through하는 것을 알 수 있다. 

한편 임의의 두 vector bundle $p_1:E_1\rightarrow B_1$, $p_2:E_2\rightarrow B_2$가 주어진다면 이들의 곱 

$$p_1\times p_2: E_1\times E_2 \rightarrow B_1\times B_2$$

또한 $B_1\times B_2$ 위의 vector bundle임을 안다. 이제 만일 $B_1=B_2=B$일 경우, 언제나와 같이 diagonal map

$$\Delta: B\rightarrow B\times B$$

를 사용하면 pullback bundle $\Delta^\ast(p_1\times p_2)$는 $B$ 위의 bundle이 된다. 이를 두 vector bundle $E_1\rightarrow B$, $E_2\rightarrow B$의 *Whitney sum*이라 부르고 $p_1\oplus p_2:E_1\oplus E_2\rightarrow B$와 같이 표기한다. 그 표기에서 알 수 있듯이 이는 fiberwise하게는 두 vector bundle $E_1,E_2$의 fiber의 direct sum에 해당한다. 

비록 자세한 증명을 하지는 않았지만, 비슷한 방식으로 우리는 각각의 fiber (즉 벡터공간)에 정의되는 연산들을 vector bundle로 옮겨올 수 있다. 가령 두 vector bundle $E_1\rightarrow B$, $E_2 \rightarrow B$에 대하여 이들의 tensor product bundle $E_1\otimes E_2 \rightarrow B$를 만들 수 있으며, $\Hom$이나 $\bigwedge$ 등의 연산을 사용하는 것도 가능하다. 

## 슈티펠-휘트니 특성류

앞서 우리는 [§푸앵카레 쌍대성, ⁋명제 4](/ko/math/algebraic_topology/Poincare_duality#prop4)에서 manifold $M$의 $A$-orientability가 다음의 group homomorphism

$$\pi_1(M,x)\rightarrow A^\times$$

에 의해 정의되는 것을 보았다. 한편 $A$는 commutative ring이므로, 위의 group homomorphism은 다음의 abelian group homomorphism

$$H_1(M)\rightarrow A^\times$$

으로 factor through하고 이는 [§코호몰로지, ⁋명제 3](/ko/math/algebraic_topology/cohomology#prop3)에 의하여 $H^1(M;A)$의 원소이다. 만일 이 원소가 $0$이라면 monodromy action이 trivial action이라는 것과 같고, 이는 곧 $\Spe(\or_M^A)$이 trivial covering space라는 뜻이 되어 $M$이 $A$-orientable manifold가 되었다. 한편 임의의 commutative ring $A$에 대하여, $\cRing$의 initial object가 $\mathbb{Z}$이므로 임의의 manifold $M$에 대하여 $\mathbb{Z}$-orientation $H_1(M)\rightarrow \mathbb{Z}^\times$가 결정되면 이를 $\mathbb{Z}^\times\rightarrow A^\times$와 합성하여 $A$-orientation $H_1(M)\rightarrow A^\times$를 결정할 수 있으므로, $\Spe(\or_M^A)$가 trivial cover인지에 대한 본질적인 정보는 $H_1(M;\mathbb{Z}/2)$에 들어있는 것을 안다.

이제 우리는 이를 일반화하여 *Stiefel-Whitney class*를 정의한다. 우선 이는 임의의 vector bundle $E\rightarrow B$가 주어질 때마다 정의되는 cohomology ring $H^\bullet(B;\mathbb{Z}/2)$의 원소 $w(E)$이며, 위와 마찬가지로 만일 $w(E)=0$이라면 $E$는 trivial bundle이 된다. 즉 만일 $w(E)=0$이라면, [명제 4](#prop4)에 의하여, $n=\rank(E)$개의 everywhere linearly independent continuous section이 존재한다. 뿐만 아니라 $w(E)$를 cohomology ring의 degree에 맞춰 

$$w(E)=w_0(E)+w_1(E)+\cdots$$

으로 분해하면, 각각의 $w_i(E)$들은 $n-i+1$개의 everywhere linearly independentsection들을 고르는 것에 대한 *obstruction class*가 된다. 즉 만일 $w_i(E)\neq 0$이라면 $n-i+1$개의 everywhere linearly independent section이 존재할 수 없다. 특히 $w_n(E)\neq 0$이라면 $1$개의 everywhere linearly independent section조차도 존재할 수 없으므로 임의의 section은 반드시 어딘가에서 $0$이 되어야 한다.

이제 우리는 $w(E)$가 만족하는 공리들을 제시한다. 

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Vector bundle $E \rightarrow B$ of rank $n$에 대하여, 다음의 공리를 만족하는 cohomology class $w_i(E)$를 *Stiefel-Whitney class<sub>슈티펠-휘트니 특성류</sub>*라 부른다. 

1. (Rank) $w_0(E)=1$이며, 만일 $i>n$이라면 $w_i(E)=0$이다. 
2. (Naturality) 임의의 $f:B'\rightarrow B$에 대하여, $w(f^\ast E)=f^\ast w(E)$가 성립한다. 
3. (Whitney product formula) $w(E\oplus F)=w(E)w(F)$가 성립한다. 
4. (Normalization) [예시 3](#ex3)의 tautological line bundle $E \rightarrow \mathbb{RP}^1$에 대하여, 

</div>