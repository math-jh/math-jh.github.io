---

title: "Bruhat decomposition과 parabolic subgroup"
excerpt: "Bruhat decomposition을 중심으로 한 homogeneous space의 cell decomposition, parabolic subgroup, 그리고 Grassmannian에서의 Schubert variety"

categories: [Math / Lie Theory]
permalink: /ko/math/lie_theory/bruhat_decomposition
sidebar: 
    nav: "Lie_theory-ko"

header:
    overlay_image: /assets/images/Math/Lie_Theory/Bruhat_Decomposition.png
    overlay_filter: 0.5

date: 2025-01-04
last_modified_at: 2025-01-04
weight: 5
published: false

---

Connected reductive algebraic group $$G$$와 그 Borel subgroup $$B$$가 주어졌을 때, $$G$$의 구조를 파악하는 가장 기본적인 도구가 Bruhat decomposition

$$G=\bigsqcup_{w\in W}BwB$$

이다. 이 분해는 $$G$$의 $$B\times B$$-orbit을 Weyl group $$W$$의 원소들로 색인화하며, 이로부터 자연스럽게 flag variety $$G/B$$의 cell decomposition이 얻어진다. 본 글에서는 우선 Bruhat decomposition 자체를 정확히 이해한 뒤, 이를 parabolic subgroup $$P\supseteq B$$로 확장하여 partial flag variety $$G/P$$의 cell decomposition을 얻는 과정을 살펴 본다. 특히 Grassmannian $$Gr_{n-k}(\mathbb{C}^n)$$을 $$GL_n/P_k$$로 실현하는 구체적인 대응과, 이 위에서 정의되는 Schubert cell 및 Schubert variety를 소개한다.

## Reductive group과 Weyl group

우리는 이 글에서 기본적으로 algebraically closed field 위에서 정의된 connected reductive algebraic group $$G$$를 다룬다. [\[리 이론\] §리 군](/ko/math/lie_theory/Lie_groups)에서 Lie group의 개념을, [\[리 이론\] §근계](/ko/math/lie_theory/root_systems)에서 그 Lie algebra의 구조를 살펴 보았으며, [\[리 이론\] §Borel subgroup과 flag variety](/ko/math/lie_theory/borel_subgroup)에서는 이로부터 자연스럽게 얻어지는 Borel subgroup과 flag variety를 소개하였다. 이 절에서는 이들 개념을 algebraic group의 맥락에서 간략히 복습한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Algebraic group $$G$$가 *reductive*라는 것은 $$G$$의 unipotent radical이 trivial한 것이다. 즉, $$G$$는 torus와 semisimple group의 extension으로 주어진다.

</div>

Reductive group $$G$$를 고정하고, $$G$$의 *Borel subgroup* $$B$$와 $$B$$에 포함된 *maximal torus* $$T$$를 고정하자. Borel subgroup은 $$G$$의 maximal connected solvable subgroup이며, 모든 Borel subgroup은 서로 conjugate하다. Maximal torus $$T$$는 $$B$$의 maximal connected diagonalizable subgroup으로, 마찬가지로 모든 maximal torus는 conjugate하다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Maximal torus $$T$$의 normalizer를 $$N_G(T)$$라 할 때, *Weyl group* $$W$$는 다음의 quotient group으로 정의된다.

$$W=N_G(T)/T$$

</div>

Weyl group $$W$$는 $$T$$의 conjugation action에 의해 자연스럽게 $$T$$의 character lattice 위에 작용하며, [\[리 이론\] §근계, ⁋명제 20](/ko/math/lie_theory/root_systems#prop20)에서 확인한 것과 같이 이 action은 root system $$\Phi$$의 대칭성을 포착한다. 더욱 중요한 것은 $$W$$가 *Coxeter group*의 구조를 지닌다는 점이다. 구체적으로, $$B$$에 의해 결정되는 positive root system $$\Phi^+$$와 simple root system $$\Delta=\{\alpha_1,\ldots,\alpha_r\}$$를 고정하면, 각 simple root $$\alpha_i$$에 대응하는 reflection $$s_i=s_{\alpha_i}$$가 생성하는 finite group이 바로 $$W$$이다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> Weyl group $$W$$는 simple reflection들 $$S=\{s_1,\ldots,s_r\}$$에 의해 생성되며, 다음의 관계들을 만족한다.

1. $$s_i^2=e$$ for all $$i$$.
2. $$(s_is_j)^{m_{ij}}=e$$ for $$i\neq j$$, where $$m_{ij}\in\{2,3,4,6\}$$.

따라서 $$(W,S)$$는 Coxeter system을 이룬다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$W$$가 reflection들로 생성되는 것은 [\[리 이론\] §근계, ⁋정의 17](/ko/math/lie_theory/root_systems#def17)의 정의이며, finite Coxeter group으로서의 구조는 root system의 기하학적 성질로부터 얻어진다. 구체적으로, 두 simple reflection $$s_i, s_j$$의 곱 $$s_is_j$$는 $$\alpha_i$$와 $$\alpha_j$$가 생성하는 2차원 평면 위에서 rotation을 정의하며, 그 각도는 두 root 사이의 각도에 의해 결정된다. [\[리 이론\] §근계](/ko/math/lie_theory/root_systems)에서 살펴 본 것과 같이 두 simple root가 이루는 각도는 $$90^\circ, 120^\circ, 135^\circ, 150^\circ$$ 중 하나이므로, $$m_{ij}$$는 각각 $$2,3,4,6$$이 된다. 이들 관계만으로 $$W$$가 완전히 결정되는 것은 Coxeter group의 일반론에 따른다.

</details>

Coxeter system $$(W,S)$$ 위에는 *length function* $$\ell:W\rightarrow\mathbb{Z}_{\geq 0}$$가 자연스럽게 정의된다. $$\ell(w)$$는 $$w$$를 simple reflection들의 곱으로 표현할 때 필요한 최소 개수이며, 이는 $$w$$의 *reduced expression*의 길이와 일치한다. Combinatorial하게는 $$\ell(w)=\lvert\Phi^+\cap w^{-1}\Phi^-\rvert$$로도 주어진다. 즉, $$w$$에 의해 positive root에서 negative root로 본지는 root의 개수가 $$\ell(w)$$이다.

## Bruhat decomposition

Bruhat decomposition은 reductive group $$G$$를 Borel subgroup $$B$$의 double coset으로 분해하는 기본적인 정리이다. 이 분해는 flag variety $$G/B$$의 cell decomposition을 제공하며, 이후에 소개할 Schubert variety의 기초가 된다.

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4 (Bruhat decomposition)**</ins> Connected reductive algebraic group $$G$$, Borel subgroup $$B$$, maximal torus $$T\subset B$$, 그리고 Weyl group $$W=N_G(T)/T$$에 대하여, 다음의 분해가 성립한다.

$$G=\bigsqcup_{w\in W}BwB$$

즉, $$G$$는 $$B$$의 double coset $$BwB$$들의 disjoint union으로 표현되며, 이들은 Weyl group $$W$$의 원소 $$w$$에 의해 색인화된다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $$G=\bigcup_{w\in W}BwB$$임을 보이자. $$G$$ 위에 $$B\times B$$가 $$(b_1,b_2)\cdot g=b_1gb_2^{-1}$$로 작용한다고 생각하면, 각 $$BwB$$는 하나의 orbit이 된다. $$G$$가 irreducible variety이고 $$BwB$$들은 locally closed subset이므로, 이들의 closure 중 maximal dimension을 갖는 것이 전체 $$G$$를 덮어야 한다. BN-pair의 공리에 의하면 $$G$$는 $$B$$와 $$N=N_G(T)$$로 생성되며, $$W=N/T$$가 double coset의 complete set of representatives를 이룬다.

Disjointness를 보이기 위해 $$BwB=BvB$$라 가정하자. 그럼 $$w\in BvB$$이므로 $$w=b_1vb_2$$ for some $$b_1,b_2\in B$$. 이로부터 $$wBw^{-1}=b_1v(b_2Bb_2^{-1})v^{-1}b_1^{-1}=b_1vBv^{-1}b_1^{-1}$$이 된다. 특히 $$wBw^{-1}$$와 $$vBv^{-1}$$는 서로 conjugate한 Borel subgroup이다. 한편 $$w\in N_G(T)$$이므로 $$wTw^{-1}=T$$이고, 따라서 $$T\subset wBw^{-1}\cap vBv^{-1}$$. 두 Borel subgroup이 서로를 normalize하고 같은 maximal torus $$T$$를 포함한다면, $$w^{-1}v$$는 $$B$$를 normalize한다. 그런데 $$B$$의 normalizer는 $$B$$ 자신이므로 $$w^{-1}v\in B$$. $$w^{-1}v\in N_G(T)$$이기도 하므로 $$w^{-1}v\in B\cap N_G(T)=T$$. 따라서 $$w=v$$ in $$W=N_G(T)/T$$이다.

</details>

Bruhat decomposition의 각 조각 $$BwB$$는 *Bruhat cell*이라 불리며, 그 구조는 다음과 같이 좀 더 정교하게 묘사할 수 있다. $$B$$의 unipotent radical을 $$U$$라 하고, opposite Borel subgroup $$B^-$$의 unipotent radical을 $$U^-$$라 하자. 각 $$w\in W$$에 대하여

$$U_w=U\cap wU^-w^{-1}$$

으로 정의하면, $$U_w$$는 root subgroup $$U_\gamma$$들의 곱으로 주어지며, 여기서 $$\gamma$$는 $$w^{-1}\gamma\in\Phi^-$$를 만족하는 positive root들이다. 즉

$$U_w=\prod_{\gamma\in\Phi^+\,:\,w^{-1}\gamma\in\Phi^-}U_\gamma$$

이며, 이는 affine space $$\mathbb{A}^{\ell(w)}$$와 isomorphism한다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> 각 $$w\in W$$에 대하여, 곱 map

$$U_w\times B\longrightarrow BwB,\qquad (u,b)\longmapsto u\dot{w}b$$

은 variety의 isomorphism이며, 따라서 $$BwB\cong\mathbb{A}^{\ell(w)}\times B$$이다. 여기서 $$\dot{w}$$는 $$w\in W=N_G(T)/T$$의 $$N_G(T)$$에서의 lift이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$B=U\rtimes T$$이고, $$U$$는 root subgroup들의 곱으로 분해된다. $$U$$를 $$U_w$$와 $$U_w'=U\cap wUw^{-1}$$의 곱으로 분해하면, $$U=U_wU_w'$$이고 $$U_w\cap U_w'=\{e\}$$. $$U_w'$$는 $$w^{-1}$$에 의해 positive root에서 positive root로 본지는 root들에 해당하므로, $$w^{-1}U_w'w\subset U$$. 따라서 $$BwB=UwB=U_w(wU_w'w^{-1})wB=U_wwB$$. 이제 $$u_1w b_1=u_2w b_2$$라 하면 $$w^{-1}u_2^{-1}u_1w=b_2b_1^{-1}\in B$$. $$u_2^{-1}u_1\in U_w$$이므로 $$w^{-1}u_2^{-1}u_1w\in U^-$$, 따라서 $$w^{-1}u_2^{-1}u_1w\in B\cap U^-=\{e\}$$. 이로부터 $$u_1=u_2$$이고 $$b_1=b_2$$이므로 map이 bijective이며, 실제로 variety의 isomorphism이다. $$U_w$$는 $$\ell(w)$$개의 root subgroup의 곱이고 각 root subgroup은 $$\mathbb{G}_a$$와 isomorphic하므로 $$U_w\cong\mathbb{A}^{\ell(w)}$$이다.

</details>

Bruhat decomposition은 flag variety $$\mathcal{F}=G/B$$로 project하면 cell decomposition을 준다. 각 $$w\in W$$에 대하여

$$X_w^\circ=BwB/B\subset G/B$$

은 $$\mathbb{A}^{\ell(w)}$$와 isomorphic한 locally closed subset이며, 이들의 disjoint union이 $$G/B$$를 덮는다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> $$G=GL_n(\mathbb{C})$$인 경우를 생각하자. Borel subgroup $$B$$는 upper triangular matrix들의 모임이고, maximal torus $$T$$는 diagonal matrix들의 모임이다. Weyl group은 $$W\cong S_n$$이며, 각 $$w\in S_n$$은 permutation matrix로 대표될 수 있다. Bruhat decomposition $$GL_n=\bigsqcup_{w\in S_n}BwB$$는 classical Gauss elimination의 일반화로 이해될 수 있다. 임의의 가역행렬 $$g$$는 row와 column의 elementary transformation을 통해 permutation matrix $$w$$를 중심으로 한 ``canonical form''으로 변형될 수 있으며, 이 때의 $$w$$가 바로 $$g$$가 속하는 Bruhat cell을 결정한다.

</div>

Opposite Borel subgroup $$B^-$$에 대해서도 유사한 decomposition이 존재한다. 이를 *Birkhoff decomposition* 또는 *opposite Bruhat decomposition*이라 한다.

<div class="proposition" markdown="1">

<ins id="thm7">**정리 7 (Birkhoff decomposition)**</ins> $$B^-=w_0Bw_0$$를 $$B$$에 대응하는 opposite Borel subgroup이라 하면, 다음이 성립한다.

$$G=\bigsqcup_{w\in W}B^-wB^-$$

더욱 일반적으로, $$B^+$$와 $$B^-$$를 서로 opposite인 두 Borel subgroup이라 할 때

$$G=\bigsqcup_{w\in W}B^+wB^-$$

이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$B^-=w_0Bw_0$$이므로

$$G=w_0Gw_0=w_0\left(\bigsqcup_{w\in W}BwB\right)w_0=\bigsqcup_{w\in W}(w_0Bw_0)(w_0ww_0)(w_0Bw_0)=\bigsqcup_{w\in W}B^-(w_0ww_0)B^-$$

$$w\mapsto w_0ww_0$$는 $$W$$의 automorphism이므로, 이는 $$G$$의 $$B^-$$에 의한 Bruhat decomposition을 준다.

$$B^+wB^-$$ 형태의 decomposition을 보이기 위해서는, $$B^+=B$$와 $$B^-=w_0Bw_0$$를 대입하면

$$BwB^-=Bww_0Bw_0=B(ww_0)Bw_0$$

이므로 $$w\in W$$를 $$ww_0$$로 재색인하면 된다. 따라서 $$G=\bigsqcup_{w\in W}BwB^-$$이 성립한다.

</details>

## Parabolic subgroup과 generalized Bruhat decomposition

Bruhat decomposition은 Borel subgroup에 대한 것이지만, 이를 $$B$$를 포함하는 더 큰 subgroup, 즉 *parabolic subgroup*으로 확장할 수 있다. Parabolic subgroup은 flag variety를 일반화하는 *partial flag variety* $$G/P$$의 isotropy group으로 작용하며, Grassmannian을 비롯한 다양한 homogeneous space를 Lie-theoretic하게 실현하는 데 핵심적인 역할을 한다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> $$G$$의 subgroup $$P$$가 *parabolic subgroup*이라는 것은 $$G/P$$가 projective variety가 되도록 하는 것이다. Equivalently, $$P$$는 어떤 Borel subgroup을 포함하는 connected closed subgroup이다.

</div>

$$B$$를 포함하는 standard parabolic subgroup들은 simple root system $$\Delta$$의 부분집합 $$I\subseteq\Delta$$에 의해 일대일대응된다. 구체적으로, $$I$$에 대응하는 parabolic subgroup $$P_I$$는

$$P_I=BW_IB$$

으로 정의되며, 여기서 $$W_I=\langle s_i\mid\alpha_i\in I\rangle$$은 $$I$$에 속한 simple reflection들로 생성되는 $$W$$의 *parabolic subgroup*이다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> $$P_I=BW_IB=\bigsqcup_{w\in W_I}BwB$$는 $$G$$의 connected closed subgroup이며, 이는 $$B$$의 Lie algebra에 $$I$$에 해당하는 simple root들의 negative root space들을 추가하여 얻어진다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$B=U\rtimes T$$이고 $$W_I\subset W$$이므로, $$P_I$$는 $$B$$와 $$W_I$$의 대표원소들로 생성되는 subgroup이다. $$W_I$$의 각 원소 $$w$$에 대해 $$BwB$$는 locally closed subset이고, 이들의 union $$P_I$$는 closed subset이다. 실제로 $$P_I$$는 Levi decomposition $$P_I=L_I\ltimes U_I$$를 갖는다. 여기서 Levi factor $$L_I$$는 $$T$$와 $$I$$에 해당하는 root space들로 생성되며, unipotent radical $$U_I$$는 $$I$$에 속하지 않은 positive root들의 root space들로 생성된다. 따라서 $$P_I$$는 connected closed subgroup이다.

</details>

Parabolic subgroup $$P=P_I$$가 주어졌을 때, $$G/P$$ 위의 Bruhat decomposition을 얻기 위해서는 Weyl group $$W$$를 parabolic subgroup $$W_I$$로 quotient해야 한다. 이 때 중요한 역할을 하는 것이 *minimal length coset representative*이다.

<div class="definition" markdown="1">

<ins id="def10">**정의 10**</ins> Parabolic subgroup $$W_I\subseteq W$$에 대하여, *minimal length coset representatives* $$W^I$$는 다음과 같이 정의된다.

$$W^I=\{w\in W\mid\ell(ws)>\ell(w)\text{ for all simple reflections }s\in W_I\}$$

Equivalently, $$W^I$$는 각 left coset $$wW_I$$에서 길이가 최소인 유일한 원소들의 모임이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> 각 left coset $$wW_I$$는 정확히 하나의 minimal length element를 포함한다. 따라서 자연스러운 projection $$W^I\rightarrow W/W_I$$는 bijection이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $$w\in W$$에 대하여, coset $$wW_I$$ 내의 길이가 최소인 원소의 존재성은 finite group $$W_I$$의 coset $$wW_I$$가 비어있지 않으므로, 길이가 최소인 원소가 반드시 존재함을 알 수 있다. 유일성을 보이기 위해 $$u,v\in wW_I$$가 둘 다 minimal length를 갖는다고 하자. 그럼 $$u=vw'$$ for some $$w'\in W_I$$. $$u$$와 $$v$$가 모두 minimal length이므로 $$\ell(u)=\ell(v)\leq\ell(vs)$$ for all simple reflection $$s\in W_I$$. 한편 $$\ell(u)=\ell(vw')$$이고, $$w'\in W_I$$는 simple reflection들의 곱으로 표현된다. Coxeter group에서 $$\ell(vw')=\ell(v)+\ell(w')-2\cdot(\text{cancellation})$$이므로, $$\ell(u)=\ell(v)$$이려면 $$\ell(w')=0$$, 즉 $$w'=e$$이어야 한다. 따라서 $$u=v$$이다.

</details>

Minimal length coset representatives를 사용하면, $$G/P_I$$ 위의 cell decomposition을 얻는다.

<div class="proposition" markdown="1">

<ins id="thm12">**정리 12 (Generalized Bruhat decomposition)**</ins> $$P=P_I$$를 standard parabolic subgroup이라 하면, 다음이 성립한다.

$$G=\bigsqcup_{w\in W^I}BwP$$

따라서 partial flag variety $$G/P$$는 다음과 같이 분해된다.

$$G/P=\bigsqcup_{w\in W^I}BwP/P$$

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Bruhat decomposition $$G=\bigsqcup_{w\in W}BwB$$와 $$P=\bigsqcup_{v\in W_I}BvB$$로부터

$$G=\bigcup_{w\in W}BwP$$

$$G=\bigcup_{w\in W}BwP$$은 Bruhat decomposition과 $$P=\bigsqcup_{v\in W_I}BvB$$로부터 직접적으로 얻어진다. 이제 $$w_1,w_2\in W^I$$에 대해 $$Bw_1P=Bw_2P$$라 하자. 그럼 $$w_1\in Bw_2P$$이므로 $$w_1=b_1w_2p$$ for some $$b_1\in B, p\in P$$. $$p\in P$$이므로 $$p=b'vb''$$ for some $$b',b''\in B, v\in W_I$$. 따라서 $$w_1\in Bw_2vB$$이고, Bruhat decomposition의 disjointness로부터 $$w_1=w_2v$$ in $$W$$. 즉 $$w_1$$과 $$w_2$$는 같은 coset $$wW_I$$에 속한다. $$w_1,w_2\in W^I$$이고 각 coset에 유일한 minimal length element가 존재하므로 $$w_1=w_2$$이다.

</details>

각 cell $$BwP/P\subset G/P$$는 $$\mathbb{A}^{\ell(w)}$$와 isomorphic하며, 이들의 closure는 *Schubert variety*를 정의한다. 이는 다음 절에서 좀 더 구체적으로 다룬다.

## Grassmannian

Generalized Bruhat decomposition의 가장 대표적인 예시는 Grassmannian이다. $$G=GL_n(\mathbb{C})$$를 고정하고, Borel subgroup $$B$$는 upper triangular matrix들의 모임, maximal torus $$T$$는 diagonal matrix들의 모임으로 하자. Weyl group은 $$W\cong S_n$$이고, simple reflection은 adjacent transposition $$s_i=(i\;i+1)$$ ($$1\leq i\leq n-1$$)이다.

<div class="definition" markdown="1">

<ins id="def13">**정의 13**</ins> $$1\leq k\leq n-1$$에 대하여, *Grassmannian* $$Gr_k(\mathbb{C}^n)$$은 $$\mathbb{C}^n$$의 $$k$$차원 부분공간들의 moduli space이다.

$$Gr_k(\mathbb{C}^n)=\{V\subseteq\mathbb{C}^n\mid\dim V=k\}$$

</div>

Grassmannian은 projective variety로 실현될 수 있으며, homogeneous space로서의 구조는 다음과 같이 주어진다. Simple root system $$\Delta=\{\alpha_1,\ldots,\alpha_{n-1}\}$$에서 $$\alpha_k$$를 제외한 부분집합 $$I=\Delta\setminus\{\alpha_k\}$$에 대응하는 maximal parabolic subgroup을 $$P_k$$라 하자. $$P_k$$는 block upper triangular matrix들의 모임으로, 구체적으로

$$P_k=\left\{\begin{pmatrix}A&C\\0&D\end{pmatrix}\in GL_n(\mathbb{C})\;\middle|\;A\in GL_k(\mathbb{C}),\;D\in GL_{n-k}(\mathbb{C})\right\}$$

이다. 이 subgroup은 standard $$k$$-plane $$E_k=\operatorname{span}\{e_1,\ldots,e_k\}$$를 고정하므로, $$GL_n(\mathbb{C})$$의 자연스러운 $$Gr_k(\mathbb{C}^n)$$ 위의 작용은 transitive하고, isotropy group이 바로 $$P_k$$이다. 따라서

$$Gr_k(\mathbb{C}^n)\cong GL_n(\mathbb{C})/P_k$$

이다. 한편 $$V\mapsto V^\perp$$ (적절한 내적 하에서) 또는 $$V\mapsto\mathbb{C}^n/V$$에 의해 $$Gr_k(\mathbb{C}^n)$$과 $$Gr_{n-k}(\mathbb{C}^n)$$ 사이에 canonical isomorphism이 존재하므로, 동일한 방식으로

$$Gr_{n-k}(\mathbb{C}^n)\cong GL_n(\mathbb{C})/P_k$$

으로도 볼 수 있다.

<div class="proposition" markdown="1">

<ins id="prop14">**명제 14**</ins> $$GL_n(\mathbb{C})/P_k\cong Gr_k(\mathbb{C}^n)$$인 경우, Weyl group $$W=S_n$$의 parabolic subgroup $$W_{P_k}$$는 $$S_k\times S_{n-k}$$과 isomorphic하며, minimal length coset representatives $$W^{P_k}$$는 다음과 같이 묘사된다.

$$W^{P_k}=\{w\in S_n\mid w(1)<w(2)<\cdots<w(k),\;w(k+1)<\cdots<w(n)\}$$

이들은 *$$(k,n-k)$$-shuffle*이라 불리며, $$\binom{n}{k}$$개의 원소를 가진다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$P_k$$는 simple reflection $$s_1,\ldots,s_{k-1}$$과 $$s_{k+1},\ldots,s_{n-1}$$을 포함한다. 따라서 $$W_{P_k}=\langle s_1,\ldots,s_{k-1},s_{k+1},\ldots,s_{n-1}\rangle$$은 처음 $$k$$개와 나머지 $$n-k$$개의 문자를 각각 내부적으로 치환하는 permutation들의 모임이므로 $$S_k\times S_{n-k}$$와 isomorphic하다.

Minimal length coset representative $$w\in W^{P_k}$$는 $$wW_{P_k}$$에서 길이가 최소인 원소이다. $$w$$의 길이 $$\ell(w)$$는 inversion의 개수이므로, $$\ell(w)$$가 최소가 되기 위해서는 $$w$$가 $$1,\ldots,k$$ 사이의 상대적 순서와 $$k+1,\ldots,n$$ 사이의 상대적 순서를 모두 보존해야 한다. 즉 $$w(1)<\cdots<w(k)$$이고 $$w(k+1)<\cdots<w(n)$$이어야 한다. 이러한 조건을 만족하는 permutation은 $$\{1,\ldots,n\}$$에서 $$k$$개를 선택하여 앞쪽 $$k$$개의 자리에 증가하는 순서로 배치하고, 나머지를 뒤쪽에 증가하는 순서로 배치하는 것이므로 총 $$\binom{n}{k}$$개가 존재한다. 이는 $$W/W_{P_k}$$의 크기와 일치하므로, 이들이 바로 $$W^{P_k}$$를 이룬다.

</details>

<div class="example" markdown="1">

<ins id="ex15">**예시 15**</ins> $$n=4, k=2$$인 경우, $$W=S_4$$이고 $$W_{P_2}=S_2\times S_2$$이다. Minimal length coset representatives는

$$W^{P_2}=\{1234, 1324, 1423, 2314, 2413, 3412\}$$

이다. 여기서 $$w=1324$$는 $$w(1)=1<w(2)=3$$이고 $$w(3)=2<w(4)=4$$를 만족한다. 각 $$w\in W^{P_2}$$에 대응하는 Schubert cell $$X_w^\circ\subset Gr_2(\mathbb{C}^4)$$은 $$\mathbb{A}^{\ell(w)}$$와 isomorphic하며, $$\ell(1234)=0$$, $$\ell(1324)=1$$, $$\ell(1423)=2$$, $$\ell(2314)=2$$, $$\ell(2413)=3$$, $$\ell(3412)=4$$이다.

</div>

## Schubert cell과 Schubert variety

이제 partial flag variety $$X=G/P$$ 위에서의 geometric structure를 정의하자. $$B$$와 opposite Borel subgroup $$B^-$$를 고정하고, $$G/P$$ 위의 cell decomposition을 구성한다.

<div class="definition" markdown="1">

<ins id="def16">**정의 16**</ins> $$w\in W^P$$에 대하여, *Schubert cell* $$X_w^\circ$$와 *opposite Schubert cell* $$X^w_\circ$$는 각각 다음과 같이 정의된다.

$$X_w^\circ=BwP/P\subseteq G/P,\qquad X^w_\circ=B^-wP/P\subseteq G/P$$

여기서 $$B^-$$는 $$B$$에 대응하는 opposite Borel subgroup이다. 이들의 closure

$$X_w=\overline{X_w^\circ},\qquad X^w=\overline{X^w_\circ}$$

를 각각 *Schubert variety*와 *opposite Schubert variety*라 한다.

</div>

정의에 의해 $$X_w^\circ\cong\mathbb{A}^{\ell(w)}$$이고 $$X^w_\circ\cong\mathbb{A}^{\dim(G/P)-\ell(w)}$$이다. 특히 $$X_{w_0^P}^\circ = Bw_0^P P/P$$는 $$B$$-orbit으로서 $$G/P$$ 안에서 open dense cell이며 ($$\ell(w_0^P)=\dim(G/P)$$), $$X_e^\circ = \{eP\}$$는 $$B$$-fixed point이다. 여기서 $$w_0^P$$는 $$W^P$$에서 가장 긴 원소이다. 대칭적으로 opposite cell 쪽을 보면 $$X^e_\circ = B^- P/P$$가 open dense cell이고 $$X^{w_0^P}_\circ = \{w_0^P P\}$$가 $$B^-$$-fixed point가 된다.

Schubert variety들 사이의 inclusion 관계는 Weyl group 위의 *Bruhat order*에 의해 결정된다.

<div class="proposition" markdown="1">

<ins id="prop17">**명제 17**</ins> $$x,w\in W^P$$에 대하여, 다음이 성립한다.

$$X_x\subseteq X_w\iff x\leq w\text{ in Bruhat order}$$

특히 $$X_w=\bigsqcup_{x\leq w,\,x\in W^P}X_x^\circ$$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$X_w=\overline{B^-wP/P}$$이고 $$B^-$$는 connected solvable group이므로, $$B^-$$-orbit의 closure는 더 작은 dimension을 갖는 orbit들의 union으로 주어진다. Bruhat order $$\leq$$는 $$v\leq w$$가 $$\ell(v)<\ell(w)$$이고 $$BvB\subseteq\overline{BwB}$$일 때 정의되는 순서이다. $$G/P$$로 project하면, $$x\leq w$$인 $$x\in W^P$$에 대해서만 $$X_x^\circ\subseteq X_w$$가 성립함을 확인할 수 있다. 이는 $$P$$로 인해 $$W$$의 원소 중 $$W_P$$에 의한 coset 내부의 차이가 무너지기 때문이다.

</details>

<div class="example" markdown="1">

<ins id="ex18">**예시 18**</ins> $$G/P=Gr_2(\mathbb{C}^4)$$인 경우를 다시 생각하자. $$W^{P_2}$$의 원소들 중 Bruhat order는 다음과 같이 주어진다.

$$1234\leq 1324\leq 1423\leq 2413\leq 3412$$
$$1234\leq 1324\leq 2314\leq 2413\leq 3412$$

즉 $$1324$$ 아래에는 $$1234$$만 있고, $$1423$$와 $$2314$$는 비교 불가능하며 둘 다 $$1324$$ 위에 있다. Schubert variety $$X_{2413}$$는 $$X_{1423}^\circ$$, $$X_{2314}^\circ$$, $$X_{1324}^\circ$$, $$X_{1234}^\circ$$를 포함하며, 이들의 disjoint union으로 이루어진다.

</div>

Schubert variety $$X_w\subset G/P$$는 일반적으로 singular하며, 그 singular locus 역시 더 작은 Schubert variety들의 union으로 표현될 수 있다. Schubert variety의 cohomology class $$[X_w]\in H^\ast(G/P)$$는 $$H^\ast(G/P)$$의 additive basis를 이루며, 이로부터 classical Schubert calculus라 불리는 intersection theory가 전개된다. 특히 Grassmannian의 경우, Schubert variety는 Young diagram으로 색인화되며, 이들의 intersection number는 Littlewood-Richardson coefficient로 주어진다.

---

**참고문헌**

**[Ful]** W. Fulton, *Young tableaux*, London Mathematical Society Student Texts **35**, Cambridge University Press, 1997.

**[Hum]** J. E. Humphreys, *Linear algebraic groups*, Graduate Texts in Mathematics **21**, Springer, 1975.

**[Man]** L. Manivel, *Symmetric functions, Schubert polynomials and degeneracy loci*, SMF/AMS Texts and Monographs **6**, 2001.

**[Spr]** T. A. Springer, *Linear algebraic groups*, Progress in Mathematics **9**, Birkhäuser, 1998.
