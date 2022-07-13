---

title: "리 군과 리 대수"
excerpt: "Differential form"

lang: ko

categories: [Math / Manifold]
permalink: /ko/math/manifold/Lie_groups_and_Lie_algebras
header:
    overlay_image: /assets/images/Manifold/Subgroups_of_Lie_groups.png
    overlay_filter: 0.5
sidebar: 
    nav: "manifold-ko"

date: 2022-06-26
last_modified_at: 2022-06-26
weight: 16

---

이번 글에서 우리는 리 군과 리 대수 간에 아주 밀접한 관련이 있다는 것을 보인다.

## Lie group과 distribution

두 Lie group $G,H$와 Lie group homomorphism $F:G\rightarrow H$가 주어졌다 하자. 만일 $\omega\in\Omega^\ast_\text{inv}(H)$라면 $F^\ast\omega\in\Omega^\ast_\text{inv}(G)$가 성립한다. 이는

$$L_g^\ast(F^\ast\omega)=(F\circ L_g)^\ast\omega=(L_{F(g)}\circ F)^\ast\omega=F^\ast(L_{F(g)}\omega)=F^\ast\omega$$

이므로 자명하다. 한편, 우리는 left-invariant 1-form들의 모임 $\Omega\_\text{inv}^1(G)$를 $\mathfrak{g}^\ast$와 동일하게 볼 수 있는데, 이 때 $dF:\mathfrak{g}\rightarrow\mathfrak{h}$라 하면 임의의 $X$에 대해 

$$(F^\ast\omega)=\omega(dF(X))$$

이므로 $F^\ast$는 정확히 $dF$의 dual map이 된다. 이제 $\Omega\_\text{inv}^1(H)$의 basis를 $\omega_1,\ldots,\omega_n$이라 하면 적당한 상수 $c_{ijk}$들에 대해

$$d\omega_k=\sum_{i < j} c_{ijk} \omega_j\wedge\omega_i$$

가 성립하고, 이를 $F^\ast$를 통해 보내면

$$F^\ast(d\omega_k)=F^\ast\left(\sum_{i < j} c_{ijk} \omega_j\wedge\omega_i\right)=\sum_{i < j} c_{ijk} F^\ast(\omega_j)\wedge F^\ast(\omega_i)$$

을 얻는다. 또, $F^\ast$와 $d$가 commute하므로 좌변은 $F^\ast(d\omega_k)=d(F^\ast\omega_k)$를 만족한다. 이제 다음의 $G\times H$의 각각의 성분으로의 projection을 $\pi_1,\pi_2$라 하고, 다음의 1-form들

$$\pi_1^\ast(F^\ast\omega_i)-\pi_2^\ast(\omega_i)$$

을 생각하면 이들은 independent이다. 뿐만 아니라 이들에 의해 생성되는 ideal $\mathscr{I}$는 differential ideal이 되는데, 이는

$$d(\pi_1^\ast(F^\ast\omega_k)-\pi_2^\ast(\omega_k))=\sum_{i < j}c_{ijk}\left(\pi_1^\ast F^\ast \omega_j\wedge\pi_1^\ast F^\ast\omega_i-\pi_2^\ast\omega_j\wedge\pi_2^\ast\omega_i\right)$$

을 적당히 조작하면[^1] $\mathscr{I}$에 속하기 때문이다. 또, 위에서 정의한 1-form들은 그 자체로 left-invariant임을 알 수 있다.

이제 [§Distribution, 정리 11](/ko/math/manifold/distribution#thm11)을 이용할 준비가 끝났지만, 위의 논증을 주의깊게 살펴보면 $F:G\rightarrow H$ 자체는 아무런 역할을 하지 않았다는 것을 알 수 있다. 즉 $dF$가 Lie group homomorphism $F:G\rightarrow H$로부터 얻어진 것이 아니라, 단순히 Lie algebra homomorphism $\bar{F}:\mathfrak{g}\rightarrow\mathfrak{h}$였고 $\bar{F}^\ast$는 그 dual map이었다고 하더라도 위의 계산을 하는 데에는 아무런 문제가 없었을 것이다. 

<div class="proposition" markdown="1">

<ins id="pp1">**명제 1**</ins> $G$가 connected Lie group이라 하고, $F,F':G\rightarrow H$가 $dF=dF'$를 만족한다 하자. 그럼 $F=F'$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

위의 construction과 [§Distribution, 정리 11](/ko/math/manifold/distribution#thm11)의 유일성에 의해 자명하다.

</details>

## 리 군의 부분군

<div class="definition" markdown="1">

<ins id="df2">**정의 2**</ins> Lie group $G$의 *Lie subgroup<sub>리 부분군</sub>*은 submanifold $F:H\rightarrow G$에 대하여, $H$가 Lie group이고, $F$가 Lie group homomorphism도 되는 상황을 나타낸다.

</div>



---

**참고문헌**

**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013  
**[Lee]** John M. Lee. *Introduction to Smooth Manifolds*, Graduate texts in mathematics, Springer, 2012  

---

[^1]: $\pi_2^\ast\omega_j\wedge\pi_1^\ast F^\ast\omega_i$를 뺐다가 더하면 된다.