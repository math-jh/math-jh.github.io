---

title: "리만 계량"
excerpt: ""

categories: [Math / Differential Geometry]
permalink: /ko/math/differential_geometry/Riemannian_metric
header:
    overlay_image: /assets/images/Math/Differential_Geometry/Riemannian_metric.png
    overlay_filter: 0.5
sidebar: 
    nav: "manifold-ko"

date: 2022-12-16
last_modified_at: 2022-12-16
weight: 1

---

## 리만 계량

우리는 [\[미분다양체\] §미분형식](/ko/math/manifold/differential_forms)에서 exterior algebra를 활용해 exterior algebra bundle

$$\bigwedge\nolimits(T^\ast M)\cong\bigoplus_{k=0}^n\bigwedge\nolimits^k(T^\ast M)$$

을 정의하고, 이 bundle의 smooth section을 differential form으로 정의했다. 비슷한 일을 symmetric algebra를 사용해서도 할 수 있으며, exterior algebra와는 다르게 $k=2$인 경우가 관심의 대상이 된다. 이는 $k=2$인 경우 생기는 $\mathcal{S}^2(T^\ast M)$의 원소들이 $TM$ 위에 symmetric bilinear form을 정의하기 때문이다. 

점 $p\in M$을 고정하자. 그럼 $g_p$는 $\mathcal{S}^2(T^\ast_pM)$의 원소이다. 이제 [\[미분다양체\] §미분형식, ⁋정의 1](/ko/math/manifold/differential_forms#def1) 이후에 확인한 것과 마찬가지 논증을 거쳐 $\mathcal{S}^2(T^\ast_pM)\cong(\mathcal{S}^2(T_pM))^\ast$임을 알 수 있고, [\[다중선형대수\] §대칭대수와 외대수, ⁋정리 13](/ko/math/multilinear_algebra/symmetric_and_exterior_algebras#thm13)에 의해 $g_p$를 $T_pM\times T_pM$에서 $\mathbb{R}$로의 symmetric multilinear map으로 생각할 수 있다. 따라서 $g_p$에 적절한 non-degenerate 조건만 준다면 이를 $T_pM$ 위에 정의된 내적으로 생각할 수 있다. ([\[기초 선형대수학\] §내적공간, ⁋정의 1](/ko/math/basic_linear_algebra/inner_product_space))

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Manifold $M$ 위에 주어진 *Riemannian metric<sub>리만 계량</sub>*은 다음과 같은 센스에서 positive-definite인 smooth section $g\in\Gamma(\mathcal{S}^2(T^\ast M))$을 의미한다.

> (Positive-definiteness) 임의의 $p\in M$에 대하여, $g_p(v,v)>0$이 영이 아닌 모든 $v\in T_pM$에 대하여 성립한다.

</div>

위에서 살펴본 것과 같이, $g$가 Riemannian metric이라면 임의의 한 점 $p$에서 $g_p(-,-)$는 $T_pM$ 위의 내적을 정의하므로, 이를 간단히 $\langle -,-\rangle_g$와 같이 표기한다. 

특별히 점 $p$ 근방의 coordinate system $(U,(x^i))$를 잡는다 하면, $g$를

$$g=\sum_{i,j=1}^ng_{ij}dx^i\otimes dx^j$$

의 형태로 나타낼 수 있고 이 때 $g$가 Riemannian metric인 것과 $n\times n$ 행렬 $(g_{ij})$가 symmetric, positive-definite인 행렬인 것이 동치이다.

벡터공간 $V$ 위의 두 내적 $g$와 $g'$가 주어졌다 하자. 그럼 다음의 식

$$(g+g')(v,w)=g(v,w)+g'(v,w)$$

으로 정의된 $g+g'$ 또한 내적이 된다. 또, $g$가 내적이라면 여기에 영이 아닌 상수 $\alpha$를 곱한 $\alpha g$ 또한 내적이 된다. 이제 유클리드 공간에는 내적이 존재하므로, 임의의 manifold $M$ 위의 coordinate chart $(U,\varphi)$마다 내적을 잘 정의할 수 있으며, partition of unity를 통해 이들을 모두 더해 $M$ 위에서의 함수를 만들 수 있다. 앞선 관찰에 의하여 이 함수는 Riemannian metric이 된다. 즉, 임의의 manifold는 항상 Riemannian metric을 줄 수 있다.

## Musical isomorphism

대수적으로 보았을 때, non-degenerate pairing이 주는 가장 좋은 결과들 중 하나는 이 pairing이 $V$와 그 dual space $V^\ast$ 사이의 isomorphism을 유도한다는 것이다. ([\[기초 선형대수학\] §쌍선형형식, §§비퇴화 쌍선형형식](/ko/math/basic_linear_algebra/bilinear_form#비퇴화-쌍선형형식)) 마찬가지로 Riemannian metric $g$가 주어졌다면, $g$는 다음의 식

$$\tilde{g}:T_pM\rightarrow T_p^\ast M;\qquad(p,v)\mapsto (p,\langle v,-\rangle)\tag{1}$$

을 통하여 두 bundle $TM$과 $T^\ast M$ 사이의 isomorphism을 유도한다. 이를 통해 임의의 벡터장 $X$가 주어졌을 때, $T^\ast M$의 smooth section $\tilde{g}(X)$를 얻는다.

이를 더 자세히 살펴보기 위해, coordinate chart $(x^i)$를 고정하자. 그럼 임의의 두 벡터장

$$X=\sum_{i=1}^n X^i\frac{\partial}{\partial x^i},\quad Y=\sum_{i=1}^n Y^i\frac{\partial}{\partial x^i}$$

에 대하여

$$\tilde{g}(X)(Y)=\sum_{i,j=1}^ng_{ij}dx^i(X)\otimes dx^j(Y)=\sum_{i,j=1}^ng_{ij}X^iY^j$$

이 성립한다. 이제 $Y$에 $\partial/\partial x^j$들을 대입해보면 $\tilde{g}(X)$는 다음의 식

$$\tilde{g}(X)=\sum_{i,j=1}^n g_{ij}X^idx^j$$

으로 주어진다는 것을 알 수 있다. 종종 $\sum_{i=1}^ng_{ij}X^i$를 $X_j$로 줄여쓰기도 하는데, 그럼 위 식은 $\tilde{g}(X)=\sum_{j=1}^nX_j dx^j$가 되므로, $X^i$의 index가 밑으로 내려간 것처럼 보인다. 이 때문에 표기법에 약간의 장난을 쳐서 covector field $\tilde{g}(X)$를 $X^\flat$으로 표기한다. 

물론 (1)은 isomorphism이므로 임의의 covector field $\omega$가 주어졌다면 이에 대응되는 vector field를 얻을 수도 있다. 이러한 vector field는 (당연히) $\omega^\sharp$으로 표기하고, 이들 둘을 묶어서 *musical isomorphism*이라 부른다. 물론 이 둘은 서로의 역함수가 된다.

## 곡선의 길이

한편 Riemannian metric은 드디어 manifold 위에서 거리를 재고, 각도를 재는 등의 기하를 할 수 있게 해 준다. 임의의 벡터공간 $V$ 위에 내적이 정의되면 $\lVert v\rVert:=\sqrt{\langle v,v\rangle}$을 통해 $V$에 거리를 줄 수 있었다는 것을 기억하자.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Riemannian manifold $(M,g)$와, 이 위에 정의된 곡선 $\gamma:[a,b]\rightarrow M$이 있다 하자. 그럼 $\gamma$의 *길이<sub>length</sub>* $\length(\gamma)$는 다음의 식

$$\length(\gamma)=\int_a^b\lVert\dot{\gamma}(t)\rVert_g\mathop{dt}$$

으로 정의된다.

</div>

이렇게 정의한 곡선의 길이는 parametrization에 의존하지 않는다. 한편, 위의 정의를 통해 $M$을 거리공간으로 만들 수 있다. 이를 위해서는

$$d_g(p,q)=\inf_{\gamma\text{ connecting }p,q}\length(\gamma)$$

으로 정의하면 된다.

## Normal bundle

마지막으로 우리는 *normal bundle*이라는 개념을 정의할 수 있다. 임의의 Riemannian manifold $M$이 주어졌다 하고, submanifold $S$를 생각하자. 그럼 $g$를 $S$로 제한하여 $S$ 위에서의 Riemannian metric $\iota^\ast g$를 얻는다. $\iota$에 의해 유도되는

$$d\iota(T_pS)\subseteq T_pM$$

에 의하여 $T_pS$은 $T_pM$의 부분공간으로 볼 수 있고 따라서 $T_pS$는 $T_pM$의 direct summand이다. 일반적으로 $T_pS$의 complementary subspace를 주는 표준적인 방법은 존재하지 않지만, 지금처럼 $T_pM$이 내적공간이라면 이를 $(T_pS)^\perp$으로 정의할 수 있다. 각 점 $p$마다 이러한 bundle $(T_pS)^\perp$이 붙어있는 $\iota(S)$ 위의 vector bundle을 우리는 $S$의 *normal bundle*이라 부르고 $NS$로 적는다.

---

**참고문헌**

**[Lee]** John M. Lee. *Introduction to Riemannian Manifolds*, Graduate texts in mathematics, Springer, 2019  

---