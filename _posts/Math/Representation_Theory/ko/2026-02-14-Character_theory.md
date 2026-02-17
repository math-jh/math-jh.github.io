---

title: "표현의 지표"
excerpt: ""

categories: [Math / Representation Theory]
permalink: /ko/math/representation_theory/character_theory
header:
    overlay_image: /assets/images/Math/Representation_Theory/Character_theory.png
    overlay_filter: 0.5
sidebar: 
    nav: "representation_theory-ko"

date: 2026-02-14
last_modified_at: 2026-02-14
weight: 2

---

이번 글에서 우리는 character function을 정의하고 이들의 성질에 대해 살펴본다. 이들은 representation을 분류하는 우리의 목표에 큰 도움을 줄 것이다. 

## 군 표현의 지표

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $G$의 representation $\rho:G\rightarrow\Aut(V)$에 대응하는 *character<sub>지표</sub>* $\rchi_\rho:G\rightarrow\mathbb{C}$를

$$\rchi_\rho(g)=\tr(\rho(g))$$

으로 정의한다. 

</div>

즉, 각각의 $g\in G$를 받아서 이것이 정의하는 linear map $\rho(g):V\rightarrow V$의 trace를 내 주는 것이 이 함수가 하는 일이다. 앞으로 살펴보겠지만, 이 함수는 $G$의 representation을 설명하는데 큰 역할을 한다. 가령, 당장 볼 수 있는 것은 이 함수가 $V$의 차원을 담고 있는 것이다. 

$$\rchi_\rho(e)=\tr(\rho(e))=\tr(\id_V)=\dim V.$$

비슷하게 우리는 두 linear map 

$$L_V:V\rightarrow V,\qquad L_W:W\rightarrow W$$

이 주어졌을 때 이들의 direct sum $L_V\oplus L_W: V\oplus W\rightarrow V\oplus W$, 이들의 tensor product $L_V\otimes L_W: V\otimes W \rightarrow V\otimes W$ 등이 어떻게 정의되는지 알고 있고, 이들의 trace가 어떻게 되는지 또한 (가령 행렬로 두고 계산하면) 알고 있다. 이로부터 다음의 명제를 얻는다. 

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> Representation $V, W$에 대해 다음이 성립한다. 

1. $\rchi_{V\oplus W}=\rchi_V\oplus \rchi_W$
2. $\rchi_{V\otimes W}=\rchi_V\rchi_W$
3. $\rchi_{V^\ast}=\overline{\rchi}_V$

</div>

특히 첫 번째 식에 의하여, 임의의 representation은 irreducible decomposition

$$V\cong V_1^{\oplus a_1}\oplus\cdots\oplus V_r^{\oplus a_r}$$

을 가지므로 임의의 representation의 character는

$$\rchi_V=a_1\rchi_{V_1}+\cdots+a_r\rchi_{V_r}$$

로 표현할 수 있음을 안다. 

한편 정의에 의하여

$$\rchi_\rho(hgh^{-1})=\tr(\rho(h)\rho(g)\rho(h)^{-1})=\tr(\rho(g))=\rchi_\rho(g)$$

가 성립하므로 ([\[선형대수학\] §특성다항식, ⁋정리 5](/ko/math/linear_algebra/characteristic_polynomial#cor5)), 우리는 이로부터 $\rchi_\rho$가 $G$의 *conjugacy class*들 위에서 상수임을 안다. 이러한 함수들에도 이름이 있다. 

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 함수 $\rchi:G\rightarrow\mathbb{C}$가 *class function<sub>유함수</sub>*이라는 것은 $\rchi(hgh^{-1})=f(g)$가 모든 $g,h\in G$에 대해 성립하는 것이다. $G$ 위에 정의된 모든 class function들의 모임을 $\mathbb{C}_\class(G)$으로 적는다. 

</div>

정의에 의해 class function들은 각 conjugacy class들 위에서의 함수값에 의해 결정되며, 따라서 벡터공간으로서 $\mathbb{C}\_\class(G)$는 $G$의 conjugacy class의 개수만큼의 차원을 갖는다. 한편 앞선 글에서 우리가 중요하게 생각했던 아이디어는 어떠한 값이 주어졌을 때, 이를 $G$ 전체에 대하여 평균내주어 $G$-invariant한 값을 얻어낼 수 있다는 것이었는데, 이를 이용하면 $\mathbb{C}\_\class(G)$ 위에 다음과 같은 정의를 해줄 수 있다. 

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> 임의의 class function들 $\rchi_1,\rchi_2: G\rightarrow \mathbb{C}$에 대하여, 

$$\langle \rchi_1,\rchi_2\rangle=\frac{1}{\lvert G\rvert}\sum_{g\in G} \rchi_1(g)\overline{\rchi_2(g)}$$

으로 정의한다. 

</div>

이는 단순히 target space $\mathbb{C}$에 정의된 standard Hermitian product를 $\mathbb{C}\_\class(G)$ 위에 옮겨준 것에 불과하다. 한편, 어떠한 representation $\rho$의 character $\rchi_\rho$에 대해서는, 임의의 $g\in G$에 대하여

$$\rchi_\rho(g^{-1})=\tr(\rho(g^{-1}))=\tr(\rho(g)^{-1})=\tr(\rho(g)^\dagger)=\overline{\tr(\rho(g))}=\overline{\rchi_\rho(g)}$$

이 성립하므로, 두 character $\rchi_1,\rchi_2$에 대해서는 다음 식

$$\langle \rchi_1,\rchi_2\rangle=\frac{1}{\lvert G\rvert}\sum_{g\in G}\rchi_1(g)\overline{\rchi_2(g)}=\frac{1}{\lvert G\rvert}\sum_{g\in G}\rchi_1(g^{-1})\overline{\rchi_2(g^{-1})}=\frac{1}{\lvert G\rvert}\sum_{g\in G}\overline{\rchi_1(g)}\rchi_2(g)=\langle \rchi_2,\rchi_1\rangle$$

이 성립하는 것을 안다. 즉 character들로 제한했을 때 이 inner product는 실수값을 가진다. 

## 지표의 직교성

앞선 글에서 살펴봤듯, 임의의 representation $U$에 대하여, 다음의 fixed point들의 subspace

$$U^G=\{u\in U\mid g\cdot u=u\text{ for all $g\in G$}\}$$

가 존재하며, 이 때

$$p:U\rightarrow U^G;\qquad u\mapsto \frac{1}{\lvert G\rvert}\sum_{g\in G}g\cdot u$$

이 $U$에서 $U$로의 $G$-invariant projection을 정의하고, 그 image는 $U^G$이다. 그 정의에 의하여, $U^G$ 위에 정의된 subrepresentation은 정확히 trivial representation

$$G\rightarrow \Aut(U^G);\quad g\mapsto \id_{U_G}$$

이므로, 우리는 이로부터 representation $U$를 trivial representation $U^G$와 그렇지 않은 부분 $W$로 분해하여

$$U=U^G\oplus W$$

를 얻을 수 있다.

뿐만 아니라, 우리는 $U^G$의 차원 또한 계산할 수 있다. 위의 decomposition에서 $U^G$와 $W$의 적절한 basis를 사용하여 이를 block matrix

$$\begin{pmatrix}\id_{U^G}&0\\0&0\end{pmatrix}$$

의 꼴로 나타낼 수 있으므로 $\varphi: U\rightarrow U$의 trace는 $\dim U^G$와 같다. 이제 정의에 의하여,

$$\dim U^G=\tr(\varphi)=\tr\left(\frac{1}{\lvert G\rvert}\sum_{g\in G}\rho(g)\right)=\frac{1}{\lvert G\rvert}\sum_{g\in G}\tr(\rho(g))=\frac{1}{\lvert G\rvert}\sum_{g\in G}\rchi(g)\tag{1}$$

이다. 

더 일반적으로, 우리는 [§유한군의 표현론, ⁋정의 3](/ko/math/representation_theory/representations_of_finite_groups#def3)에서 임의의 $G$-representation $V,W$에 대하여, 이들의 (underlying $\mathbb{C}$-벡터공간으로서의) $\Hom$-set $\Hom_\mathbb{C}(V,W)$에 $G$-action

$$(g\cdot f)(v)=g\cdot f(g^{-1}\cdot v)\qquad\text{for all $v\in V$}$$

을 정의하였다. 그럼 다음의 식

$$\Hom_\mathbb{C}(V,W)^G=\Hom_G(V,W)$$

이 성립하며, 따라서 식 (1)을 $U=\Hom(V,W)$와 그에 대응되는 trace map $\varphi$에 적용하면

$$\dim \Hom_G(V,W)=\tr(\varphi)=\frac{1}{\lvert G\rvert}\sum_{g\in G}\rchi_{\Hom(V,W)}(g)$$

임을 안다. 한편 $\Hom_G(V,W)=V^\ast\otimes W$임을 활용하면 우변의 character는 다음의 식

$$\rchi_{\Hom_G(V,W)}(g)=\overline{\rchi_V(g)}\rchi_W(g)$$

을 통해 얻어지므로, 위의 식을 다시

$$\dim\Hom_G(V,W)=\frac{1}{\lvert G\rvert}\sum_{g\in G}\overline{\rchi_V(g)}\rchi_W(g)=\langle \rchi_W, \rchi_V\rangle$$

으로 쓸 수 있다. 한편, 마지막으로 $V,W$가 irreducible representation들이라 가정하면 $\Hom_G(V,W)$는 [§유한군의 표현론, ⁋보조정리 8](/ko/math/representation_theory/representations_of_finite_groups#lem8)으로부터 $V\cong W$라면 $1$차원, 그렇지 않다면 $0$차원이므로

$$\dim \Hom_\mathbb{C}(V,W)^G=\dim \Hom_G(V,W)=\begin{cases}1&\text{if $V\cong W$,}\\0&\text{otherwise}\end{cases}$$

이고 이로부터 다음의 식

$$\langle \rchi_W,\rchi_V\rangle=\delta_{VW}$$

을 얻는다. 즉 [정의 4](#def4)의 inner product에 대하여 irreducible character들은 orthonormal set이다. 우리는 $\mathbb{C}\_\class(G)$가 $G$의 conjugacy class들의 개수만큼의 차원을 가지고 있는 것을 알고 있으므로, 이로부터 irreducible representation들은 $G$의 conjugacy class의 개수보다 많을 수 없다는 것을 안다. 뿐만 아니라, 이 inner product를 사용하면 우리는 임의의 representation $V$의 character $\rchi\_V$와, 고정된 irreducible representation $V_i$의 character $\rchi_{V_i}$을 내적하여 $V$ 안에서 $V_i$의 multiplicity를 계산할 수 있다. 

## Regular representation

우리는 categorical equivalence

$$\Rep_\mathbb{C}(G)\cong \lMod{\mathbb{C}[G]}$$

로부터 임의의 $G$-representation이 $\mathbb{C}[G]$-module임을 보았다. 이러한 관점에서 우리는 $\mathbb{C}[G]$-module $\mathbb{C}[G]$에도 관심을 가질 수 있는데, $G$에는 canonical $G$-action (즉 translation map)이 존재하므로 이를 통해 $\mathbb{C}[G]$를 $G$의 representation으로 생각할 수 있다. 더 구체적으로 우리는 임의의 $\phi\in \mathbb{C}[G]$에 대하여, 이를 $\sum \phi_xx$와 같이 표현한다면 다음의 action

$$g\cdot \left(\sum \phi_xx\right)=\sum \phi_x gx$$

으로 정의한다. 혹은 $\phi\in \mathbb{C}[G]$를 받아 $\phi\circ L_{g^{-1}}$을 주는 것으로 생각하여도 된다. 그럼 임의의 representation $V$와 임의의 $v\in V$에 대하여 $V$ 위에 정의된 $G$-action이 정확히 $\mathbb{C}[G]$와 같다는 것이 [§유한군의 표현론, ⁋명제 4](/ko/math/representation_theory/representations_of_finite_groups#prop4)의 결과였다. 따라서 이와 같은 $G$-action이 주어진 $\mathbb{C}[G]$를 살펴보는 것이 중요하게 된다. 

앞선 도구를 사용하여 이 계산을 실행해보면, 우리는 $\mathbb{C}[G]$가 각각의 $G$에 해당하는 basis $g$들 (정확히는 $\delta_g$들)을 가지고 있는 것을 알고 위에서 설명한 action은 정확히 이들 basis들 위에 작용하는 것을 안다. 이제 이 basis를 통해 각각의 $\rho(g)\in\Aut(\mathbb{C}[G])$를 행렬로 표현해보면, translation map $L_{g^{-1}}$이 faithful인 것으로부터 $\rho(g)$를 행렬로 나타내었을 때 이 행렬은 오직 $g=e$일 때만 항등행렬이고, 나머지 경우에는 trace가 $0$이 되는 것을 안다. 즉,

$$\rchi_{\mathbb{C}[G]}(g)=\begin{cases}\lvert G\rvert&\text{if $g=e$}\\0&\text{otherwise}\end{cases}$$

이다. 이제 만일 $V_i$가 $\mathbb{C}[G]$의 irreducible subrepresentation이라면,

$$\langle\rchi_{\mathbb{C}[G]}, \rchi_{V_i}\rangle=\frac{1}{\lvert G\rvert}\sum_{g\in G}\rchi_{\mathbb{C}[G]}(g)\rchi_{V_i}(g)=\frac{1}{\lvert G\rvert} \rchi_{\mathbb{C}[G]}(e)\rchi_{V_i}(e)=\dim V_i$$

이 성립한다. 즉, 우리는 다음의 decomposition

$$\mathbb{C}[G]\cong \bigoplus_{i=1}^r V_i^{\dim V_i}$$

을 얻고, 이로부터

$$\lvert G\rvert=\sum_{i=1}^r (\dim V_i)^2$$

임을 안다. 뿐만 아니라, 이 decomposition이 $\mathbb{C}[G]$ 위에 어떻게 act하는지를 보면 이것이 정확하게 Artin-Wedderburn theorem이 주는 decomposition

$$\mathbb{C}[G]\cong \bigoplus_{i=1}^r\Mat_{d_i}(\mathbb{C})$$

과 같다는 것을 확인할 수 있다. 

## Projection formula

앞서 우리는 $\mathbb{C}\_\class(G)$ 안에서 irreducible representation들의 character가 orthonormal set을 이룬다는 것을 보았다. 이제 우리는 이들이 $\mathbb{C}\_\class(G)$의 orthonormal basis가 된다는 것을 보인다. 

<div class="proposition" markdown="1">

<ins id="lem5">**보조정리 5**</ins> 임의의 함수 $\phi:G\rightarrow \mathbb{C}$와 임의의 representation $\rho:G\rightarrow\Aut(V)$이 주어졌다 하자. 

$$\rho_\phi=\sum_{g\in G} \phi(g)\rho(g): V\rightarrow V$$

으로 정의하면, $\rho_\phi$가 $G$-map인 것과 $\phi$가 class function인 것이 동치이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$\rho_\phi$가 $G$-map이기 위해서는 임의의 $h\in G$와 임의의 $v\in V$에 대하여 다음 식

$$\rho_\phi(h\cdot v)=h\cdot\rho_\phi(v)$$

이 성립해야 한다. 좌변을 직접 계산해보면

$$\rho_\phi(h\cdot v)=\sum_{g\in G}\phi(g)\rho(g)(h\cdot v)$$

이며, 이 합을 $hgh^{-1}$에 대하여 취해도 같은 합이므로

$$\rho_\phi(hv)=\sum_{g\in G}\phi(hgh^{-1})\rho(hgh^{-1})(h\cdot v)=\sum_{g\in G}\phi(hgh^{-1})\rho(h)\rho(g)(v)=\rho(h)\left(\sum_{g\in G}\phi(hgh^{-1})\rho(g)v\right)$$

로 쓸 수 있다. 이제 이것이

$$h\cdot\rho_\phi(v)=\rho(h)\rho_\phi(v)=\rho(h)\left(\sum_{g\in G}\phi(g)\rho(g)(v))$$

와 같기 위해서는 정확히 $\phi(g)=\phi(hgh^{-1})$, 곧 $\phi$가 class function이어야 한다. 

</details>

이제 우리는 이를 사용하여 모든 class function이 irreducible character들의 일차결합으로 나타난다는 것을 보인다. 즉 만일 class function $\phi$에 대하여, $\langle \phi,\rchi_V\rangle=0$이 모든 irreducible character $\rchi_V$에 대해 성립한다면 $\phi=0$이라는 것을 보여야 한다. 

이를 위해 위의 보조정리를 class function $\phi$와 irreducible representation $\rho:G\rightarrow\Aut(V)$에 사용하자. $\phi$가 class function이므로 $\overline{\phi}$도 그러하고, 따라서 $\rho_{\overline{\phi}}$는 $G$-map이며 따라서 [§유한군의 표현론, ⁋보조정리 8](/ko/math/representation_theory/representations_of_finite_groups#lem8)에 의하여 $\rho_{\overline{\phi}}$는 $\lambda\id_V$의 꼴이다. 이제 여기에 trace를 취하면

$$(\dim V)\lambda=\tr(\rho_{\overline{\phi}})=\tr\left(\sum_{g\in G}\overline{\phi(g)}\rho(g)\right)=\sum_{g\in G}\overline{\phi(g)}\rchi_V(g)=\lvert G\rvert\langle \rchi_V,\phi\rangle=0$$

임을 안다. 이제 $\mathbb{C}[G]$ 위에 $\overline{\phi}$가 regular representation으로 작용하는 경우를 생각하자. 그럼 


으로부터 얻어진다. 

## 예시: $S_3$

우리는 이전 글부터 세운 이론을 살펴보는 예시로 이 글을 마무리한다. 우선 임의의 *abelian* group $G$에 대해서는 
