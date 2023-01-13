---

title: "Distribution"
excerpt: "Distribution의 정의와 Frobenius theorem"

categories: [Math / Manifold]
permalink: /ko/math/manifold/distribution
header:
    overlay_image: /assets/images/Math/Manifold/Distribution.png
    overlay_filter: 0.5
sidebar: 
    nav: "manifold-ko"

date: 2023-01-12
last_modified_at: 2023-01-12
weight: 14

---

앞서 [§벡터장](/ko/math/manifold/vector_fields)에서 우리는 주어진 manifold $M$ 위에 정의된 임의의 $C^\infty$ 벡터장 $X$에 대하여, 충분히 작은 $\epsilon>0$이 존재하여 다음의 식

$$\sigma'(t)=X(\sigma(t)),\qquad \sigma(0)=p\tag{1}$$

을 만족하는 곡선 $\sigma:(-\epsilon,\epsilon)\rightarrow M$이 존재한다는 것을 보았다. 이렇게 정의된 곡선 $\sigma$의 $M$에서의 image $S$는 점 $p$를 포함하는 $M$의 submanifold로 볼 수 있다. 

한편, 위의 식 (1)은 $\sigma$의 image 뿐만 아니라, 이를 매개화하는 방법도 강제한다. 반면 submanifold $S$는 $\sigma$의 매개화와는 무관하게 결정되므로, 이는 벡터 $X_p$가 아니라 $T_pM$의 1차원 부분공간 $\span(X_p)$에 의해서만 결정된다.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> $m$차원 manifold $M$이 주어졌다 하고, $1\leq k\leq m$인 정수 $k$가 주어졌다 하자. 각각의 $p\in M$마다 $T_pM$의 $k$차원 부분공간 $\mathcal{D}$를 대응시키는 함수 $p\rightarrow\mathcal{D}(p)$를 *$k$차원 distribution*이라 부른다. 

$k$차원 distribution $\mathcal{D}$가 $C^\infty$인 것은 각각의 $p\in M$마다 적당한 열린근방 $U$와, 이 위에서 정의된 $C^\infty$ 벡터장들 $X_1,\ldots, X_k$가 존재하여, 각각의 $x\in U$마다 다음의 식

$$\mathcal{D}(x)=\span\{(X_1)_x,\ldots, (X_k)_x\}$$

이 성립하는 것이다.

</div>

벡터장 $X$는 위에서 살펴본 것과 같이 다음의 식 $p\mapsto\span(X_p)\subseteq T_pM$을 통해 1차원 distribution을 정의한다. 그럼 submanifold $S$는 다음의 식

$$T_xS=\mathcal{D}(x)\qquad\text{for all $x$}$$

을 만족하도록 결정된다. 따라서 다음과 같이 정의한다.

<div class="definition" markdown="1">

<ins id="df2">**정의 2**</ins> $M$ 위에 정의된 $k$차원 distribution $\mathcal{D}$에 대하여, 다음의 식

$$T_xS=\mathcal{D}(x)\qquad\text{for all $x$}$$

을 만족하는 manifold $S$를 $\mathcal{D}$의 *integral manifold*라 부른다.

</div>

