---

title: "사슬 호모토피"
excerpt: "기본정의"

categories: [Math / Homological Algebra]
permalink: /ko/math/homological_algebra/chain_homotopy
header:
    overlay_image: /assets/images/Homological_algebra/a.png
    overlay_filter: 0.5
sidebar: 
    nav: "homological_algebra-ko"

date: 2022-09-11
last_modified_at: 2022-09-11
weight: 4

---

## Isomorphic chain complexes

수학에서 <em_ko>같다</em_ko>는 개념은 꽤 유연해서, 종종 엄밀하게는 같지 않은 대상을 같게 보기도 한다. 예를 들어 임의의 두 $F$-벡터공간이 주어졌을 때, 이들 두 공간이 서로 다른 원소들로 구성되어 있더라도 이들의 차원이 같으면 이 두 벡터공간을 같은 것으로 생각할 수 있다. 

지금까지 살펴본 chain complex들 사이의 isomorphism을 어떻게 정의해야 하는지는 명확하다.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 두 chain complex $C_\bullet$, $D_\bullet$이 주어졌다 하자. 그럼 $C_\bullet$과 $D_\bullet$이 *isomorphic*하다는 것은 임의의 두 chain map $f:C_\bullet\rightarrow D_\bullet$, $g:D_\bullet\rightarrow C_\bullet$이 존재하여 $fg=\operatorname{id}\_D$이고 $gf=\operatorname{id}\_C$인 것이다. 이 때, $f,g$를 두 chain complex 사이의 *isomorphism*이라 부른다.

</div>

이는 곧, 각각의 $f_n$들이 모두 isomorphism인 chain map $(f\_n)\_{n\in\mathbb{Z}}$이 존재한다는 것과 동치이다. 그럼 $H_n$이 $\mathbf{Ch}(\mathcal{C})$에서 $\mathcal{C}$로의 functor라는 것으로부터 isomorphic한 두 chain complex $C,D$의 $n$-th homology group $H_n(C)$와 $H_n(D)$ 또한 isomorphic하다는 것을 알 수 있다. 

<div class="definition" markdown="1">

<ins id="df2">**정의 2**</ins> 두 chain complex $C_\bullet$, $D_\bullet$이 *quasi-isomorphic*하다는 것은 모든 $n$에 대하여 $H_n(C)\cong H_n(D)$인 것이다. 만일 어떤 chain map $f:C\rightarrow D$과 모든 $n$에 대해 $H_n(f)$가 isomorphism이 된다면, $f$를 *quasi-isomorphism*이라 부른다.

</div>

따라서 isomorphic한 두 chain complex들은 quasi-isomorphic하기도 하다. 그러나 그 역은 성립하지 않는다. 모든 성분이 0인 sequence

$$\cdots\rightarrow 0\rightarrow 0\rightarrow 0\rightarrow\cdots$$

와 isomorphic한 chain complex는 자기자신 뿐이지만, 임의의 exact sequence는 항상 모든 homology module이 0이 된다.

## 사슬 호모토피

임의의 두 complex $C_\bullet$, $D_\bullet$이 주어졌다 하고, 두 chain map $f,g:C_\bullet,D_\bullet$이 주어졌다 하자. 우리가 chain complex를 분석하는 도구는 homology group이기 때문에, 서로 다른 $f,g$가 homology group들에서 동일한 함수를 유도한다면 이들 두 chain map이 거의 동일한 것으로 생각할 수 있다. 이를 위해 다음을 정의하자.

<div class="definition" markdown="1">

<ins id="df3">**정의 3**</ins> 두 chain complex $C,D$와 chain map $f,g:C\rightarrow D$가 주어졌다 하자. 그럼 $f$와 $g$ 사이의 *chain homotopy<sub>사슬 호모토피</sub>*은 다음 diagram

![chain_homotopy](/assets/images/Homological_algebra/Chain_homotopy-1.png){:width="612px" class="invert" .align-center}

에서, $f_n-g_n=d_{n+1}^Dh_n+h_{n-1}d_n^C$가 성립하도록 하는 $h_n:C_n\rightarrow D_{n+1}$의 모임이다. 만일 $f,g$ 사이의 chain homotopy가 존재한다면, $f$와 $g$가 *homotopic*한 chain map이라 부른다. 

</div>

만일 어떤 chain map $f$에 대하여, $f=dh+hd$를 만족하는 $h$가 존재한다면, $h$를 $f$와 $0$ 사이의 chain homotopy로 볼 수 있다. 따라서 이와 같은 $h$가 존재할 경우 $f$를 *null homotopic*하다 부른다. 이제 두 chain map $f,g$가 homotopic한 것은 이들의 차이 $f-g$가 nullhomotopic인 것과 동치로 생각할 수 있다. 

<div class="proposition" markdown="1">

<ins id="pp4">**명제 4**</ins> 두 homotopic chain map $f,g:C\rightarrow D$는 homology들 위에서 같은 함수를 유도한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $[a]\in H_n(C)=\ker(d^C_{n})/\operatorname{im}(d^C_{n+1})$을 택하고, $a\in\ker(d_{n}^C)$가 representative라 하자. 우리는 

$$f_n(a)-g_n(b)\in\operatorname{im}(d_{n+1}^D)$$

을 보여야 한다. 그런데 다음의 식

$$(d_{n+1}^D\circ h_n)(a)+(h_{n-1}\circ d_n^C)(a)=f_n(a)-g_n(a)$$

으로부터, $a\in \ker(d_n^C)$이므로 

$$f_n(a)-g_n(a)=d_{n+1}^D)(h_n(a))\in\operatorname{im}(d_{n+1}^D)$$

을 얻는다.

</details>

만일 어떤 chain map $f:C\rightarrow D$에 대하여, 적당한 chain map $g:D\rightarrow C$가 존재하여 $gf$가 $\operatorname{id}\_C$와 homotopic하고, $fg$가 $\operatorname{id}\_D$와 homotopic하다면 $f$를 *chain homotopy equivalence*라 부른다. 

## Homotopy category

[명제 4](#pp4)에 힘입어, 우리는 *homotopy category* $\mathbf{K}(\mathcal{C})$를 다음 과정을 통해 정의할 수 있다. 우선 다음의 첫 번째 보조정리는 자명하다.

<div class="proposition" markdown="1">

<ins id="lem5">**보조정리 5**</ins> 두 chain map 사이의 homotopy relation은 동치관계다.

</div>

이를 통해 $\operatorname{Hom}\_{\mathbf{Ch}(\mathcal{C})}(C\_\bullet,D\_\bullet)$ 위에 동치관계를 정의할 수 있다. 이 동치관계에 의해 생긴 quotient set을 $\operatorname{Hom}\_{\mathbf{K}(\mathcal{C})}(C\_\bullet,D\_\bullet)$으로 정의하자. 

$\mathbf{K}(\mathcal{C})$는 $\mathbf{Ch}(\mathcal{C})$와 동일한 object를 갖고, 이들 사이의 morphism들의 집합은 위와 같이 정의된 $\operatorname{Hom}\_{\mathbf{K}(\mathcal{C})}$와 같고, 이 집합이 abelian group의 구조를 갖는다는 것을 확인할 수 있다. 

두 homotopic chain map $f,g:C\rightarrow D$가 주어졌다 하자. 임의의 $u:B\rightarrow C$, $v:D\rightarrow E$에 대하여 두 map $vfu$와 $vgu$를 생각하자. 다음 diagram

![composition_in_homotopy_category](/assets/images/Homological_algebra/Chain_homotopy-2.png){:width="612px" class="invert" .align-center}

을 생각하면,

$$\begin{aligned}v_nf_nu_n-v_ng_nu_n&=v_n(f_n-g_n)u_n\\&=v_n(d_{n+1}h_n+h_{n-1}d_n)u_n\\&=d_{n+1}v_{n+1}h_nu_n+v_nh_{n-1}u_{n-1}d_n\end{aligned}$$

이 되어, $vfu$와 $vgu$ 사이에 chain homotopy

$$(h'_n=v_{n+1}h_nu_n)_{n\in\mathbb{Z}}$$

이 존재한다는 것을 안다. 즉 위에서 정의한 동치관계는 $\mathbf{Ch}(\mathcal{C})$의 합성과도 잘 맞아 떨어진다. 

비슷한 논리로 $\mathbf{K}(\mathcal{C})$가 additive category라는 것을 보일 수 있으며, 자명한 functor $\mathbf{Ch}(\mathcal{C})\rightarrow\mathbf{K}(\mathcal{C})$가 additive functor가 된다. 

그러나 일반적으로 $\mathbf{K}(\mathcal{C})$는 abelian category가 되지는 않는다. 

---

**참고문헌**

**[Wei]** C.A. Weibel. *An Introduction to Homological Algebra*. Cambridge Studies in Advanced Mathematics. Cambridge University Press, 1995.