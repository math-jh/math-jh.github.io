---

title: "분수아이디얼"
excerpt: ""

categories: [Math / Commutative Algebra]
permalink: /ko/math/commutative_algebra/fractional_ideals
header:
    overlay_image: /assets/images/Math/Commutative_Algebra/Fractional_ideals.png
    overlay_filter: 0.5
sidebar: 
    nav: "commutative_algebra-ko"

date: 2025-01-21
last_modified_at: 2025-01-24
weight: 19

---

다음 글에서 우리는 regular local ring ([§차원, ⁋정의 9](/ko/math/commutative_algebra/Krull_dimension#def9))에 대해 살펴본다. 그 전에 몇가지 개념들을 정의해야 한다. 

## 가역가군

우선 다음을 정의한다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Ring $A$에 대하여, $A$-module $M$이 *invertible<sub>가역</sub>*이라는 것은 $M$이 finitely generated이고, $A$의 임의의 prime ideal $\mathfrak{p}$에 대하여 $M_\mathfrak{p}\cong A_\mathfrak{p}$가 성립하는 것이다. 

</div>

Prime ideal $\mathfrak{p}$와 $\mathfrak{p}$를 포함하는 maximal ideal $\mathfrak{m}$에 대하여, 만일 $A\_\mathfrak{m}\cong M\_\mathfrak{m}$라면 $A\_\mathfrak{p}\cong M\_\mathfrak{p}$일 것이므로 위의 조건은 임의의 maximal idlal에 대해서만 확인해봐도 충분하다. 

이제 $M^\ast=\Hom_A(M,A)$으로 정의하면, $A$가 commutative라는 사실로부터 $\Hom_A(M, A)$도 $A$-module임을 알고, 더 나아가 trace map $M^\ast\otimes M \rightarrow A$ 또한 존재한다. ([\[다중선형대수학\] §Hom과 텐서곱, ⁋정의 6](/ko/math/multilinear_algebra/hom_and_tensor#def6))

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Ring $A$와, $A$의 total ring of fractions $K$를 생각하자. 그럼 $K$의 $A$-submodule $\mathfrak{A}$가 $A$의 *fractional ideal<sub>분수아이디얼</sub>*이라는 것은 $0$이 아닌 적당한 $a\in A$가 존재하여 $a \mathfrak{A}\subseteq A$인 것이다. 

</div>

위의 정의에서 얻어지는 $a \mathfrak{A}$가 $A$의 ideal이 된다는 것은 자명하다. 직관적으로 $\mathfrak{A}$가 finitely generated라면, $a \mathfrak{A}\subseteq A$라는 조건은 $\mathfrak{A}$의 generator들의 공통분모를 곱하여 이를 $A$의 subset으로 보는 것과 같은 것이다. 특히 $K$의 임의의 finitely generated $A$-submodule

$$\left(\frac{a_1}{s_1},\ldots, \frac{a_n}{s_n}\right)A$$

은 원소 $s_1\cdots s_n\in A$에 의해 항상 fractional ideal이 되고, $A$가 noetherian이라면 그 역 또한 성립한다. 일반적인 ideal과 같이, fractional ideal들의 곱 또한

$$\mathfrak{A}\mathfrak{B}=\left\{\sum_{i=1}^n a_ib_i: a_i\in \mathfrak{A}, b_i\in \mathfrak{B}\right\}$$

으로 정의한다. 

다음 정리에서, $K$의 임의의 부분집합 $X$에 대하여, 

$$X^{-1}=(A:_KX)=\{y\in K: yX\subseteq A\}$$

이며, 위의 직관에 따르면 이는 대략적으로 $X$의 분모들의 모임 정도로 생각할 수 있다. 

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3**</ins> Noetherian ring $A$에 대하여 다음이 성립한다.

1. $A$-module $M$이 invertible인 것과, trace map $M^\ast\otimes_A M \rightarrow A$가 isomorphism인 것이 동치이다. 
2. 임의의 invertible module은 $A$의 어떤 fractional ideal과 isomorphic하고, 따라서 $K$의 임의의 invertible $A$-submodule은 $A$의 fractional ideal이다. 이런 식으로 얻어지는 임의의 invertible fractional ideal은 $A$의 non-zerodivisor를 포함한다.
3. $K$의 두 invertible $A$-submodule $M,N$에 대하여, 다음 두 식
    
    $$M\otimes N \rightarrow MN;\quad s\otimes t\mapsto st,\qquad M^{-1}N \rightarrow \Hom_A(M,N);\quad t\mapsto u_t(-)=t-$$

    으로 정의되는 morphism들은 isomorphism들이다. 특히 $M^{-1}\cong M^\ast$이 성립한다.
4. 임의의 $A$-submodule $M\subseteq K$에 대하여, $M$이 invertible인 것과 $M^{-1}M=A$인 것이 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

1. 우선 한쪽 방향은 [§국소화의 성질들, ⁋명제 4](/ko/math/commutative_algebra/properties_of_localization#prop4)에 의해 자명하다.  
    거꾸로 trace map $\tr:M^\ast\otimes_A M \rightarrow A$가 isomorphism이라 하고, $M\_\mathfrak{p}\cong A\_\mathfrak{p}$임을 보여야 한다. 이 때, $\tr$이 isomorphism이므로
    
    $$\tr\left(\sum_{i=1}^n\xi_i\otimes x_i\right)=1$$

    이도록 하는 $M^\ast\otimes M$의 원소가 존재하며, 우리는 $M\_\mathfrak{p}$가 $a_i$로 생성된다는 것을 보인다. 그럼 $M$은 [§국소화의 성질들, ⁋명제 4](/ko/math/commutative_algebra/properties_of_localization#prop4)에 의해 이들 $x_1,\ldots, x_n$들로 생성되어야 한다. 

    다시 이 명제를 통해, 우리는 주어진 가정으로부터 임의의 prime ideal $\mathfrak{p}$에 대해 $\tr_\mathfrak{p}$가 isomorphism이 다음의 isomorphism
    
    $$\tr_\mathfrak{p}: (M^\ast\otimes_AM)_\mathfrak{p}\cong M^\ast_\mathfrak{p}\otimes_{A_\mathfrak{p}}M_\mathfrak{p} \rightarrow A_\mathfrak{p}$$
    
    을 얻는다. 비슷하게 $\xi_i:M \rightarrow A$를 localize하여 $(\xi\_i)\_\mathfrak{p}: M\_\mathfrak{p}\rightarrow A\_\mathfrak{p}$를 정의할 수 있으며, 이들이 원하는 isomorphism이 될 것이다.  
    한편 고정된 $\mathfrak{p}$에 대하여, $1\not\in \mathfrak{p}$이므로 위에서 택한 $\xi_i\otimes x_i$ 중 어느 하나는 $\tr(\xi_i\otimes x_i)=\xi_i(x_i)\not\in \mathfrak{p}$를 만족해야 한다. 그럼 $A\_\mathfrak{p}$에서 이 원소의 역원 $\xi_i(x_i)^{-1}$이 존재하며, 이를 편의상 $a_i$라 쓰기로 하면 다음 식

    $$(\xi_i)_\mathfrak{p}(a_i x_i)=1$$

    을 통해 $(\xi_i)\_{\mathfrak{p}}: M\_\mathfrak{p} \rightarrow A\_\mathfrak{p}$가 $a_i x_i$를 $A\_\mathfrak{p}$로 옮기는 것을 안다. 이제 $A\_\mathfrak{p} \rightarrow M\_\mathfrak{p}$를 $1\mapsto a_ix_i$로 정의하면, 이는 $(\xi_i)\_\mathfrak{p}$의 section이며 따라서 다음의 short exact sequence

    $$0 \longrightarrow \ker (\xi_i)_\mathfrak{p}\longrightarrow M_\mathfrak{p}\overset{(\xi_i)_\mathfrak{p}}{\longrightarrow}A_\mathfrak{p}\longrightarrow 0$$

    가 split한다. 이로부터 $M_\mathfrak{p}\cong A\_\mathfrak{p}x_i\oplus\ker(\xi\_i)\_\mathfrak{p}$인 것을 안다. 비슷하게 $M\_\mathfrak{p}\hookrightarrow M^{\ast\ast}\_\mathfrak{p}$를 통해 $x_i$를 $M^\ast\_\mathfrak{p} \rightarrow A\_\mathfrak{p}$로 보면 $M\_\mathfrak{p}^\ast\cong A\_\mathfrak{p}\xi_i\oplus \ker(x_i)$를 얻으며, 이제

    $$M^\ast_\mathfrak{p}\otimes M_\mathfrak{p}\cong (A_\mathfrak{p}\xi_i\otimes A_\mathfrak{p}x_i)\oplus ( A_\mathfrak{p}\xi_i\otimes\ker (\xi_i)_\mathfrak{p})\oplus(\ker(x_i)_\mathfrak{p}\otimes A_\mathfrak{p}x_i)\oplus (\ker(x_i)_\mathfrak{p}\otimes \ker(\xi_i)_\mathfrak{p})$$

    이다. 그런데 우변의 첫 번째 항이 정확히 $A\_\mathfrak{p}$의 원소를 전부 복원해내므로, $\tr_\mathfrak{p}$로 옮겼을 때 나머지 항들은 $0$으로 가야만 하고, 특히 둘째 항이 $0$으로 가는 것으로부터 $(\ker\xi_i)\_\mathfrak{p}=\ker(\xi_i)_\mathfrak{p}=0$임을 안다. 즉, $\xi\_i$는 위의 주장대로 $M\_\mathfrak{p}$에서 $A\_\mathfrak{p}$로의 isomorphism이고, 이를 통해 $M\_\mathfrak{p}$를 $x_i$로 생성되는 free $A\_\mathfrak{p}$-moule로 생각할 수 있다. 
2. 이제 $M$이 invertible module이라 하자. 이를 $A$의 fractional ideal과 비교하기 위해서는 우선 $M$을 $K$에 넣어주어야 한다. 그런데 우선 $A$의 total ring of fractions $K$의 maximal ideal들은 정확히 $A$의 maximal한 associated prime ideal들에 대응됨을 확인할 수 있고, $\Ass A$는 유한하므로 $K$는 semilocal ring이 된다. 따라서 [§정수적 확장, ⁋명제 13](/ko/math/commutative_algebra/integral_extension#prop13)과 다음 isomorphism들
    
    $$M\otimes K_{\mathfrak{m}K}=M_\mathfrak{m}\cong A_\mathfrak{m}\cong K_{\mathfrak{m}K}$$

    으로부터 $M\otimes K\cong K$를 얻는다. 이제 이를 localization map $\epsilon: M \rightarrow S^{-1}M=K\otimes M$과 합성하면 원하는 embedding을 얻으며, 이 때 $\epsilon$이 injective이라는 사실 또한 $A$의 임의의 maximal ideal $\mathfrak{m}$에 [§국소화의 성질들, ⁋명제 4](/ko/math/commutative_algebra/properties_of_localization#prop4)를 적용하여 다음의 map

    $$\epsilon_\mathfrak{m}: M_\mathfrak{m}\cong A_\mathfrak{m} \rightarrow K\otimes_{A_\mathfrak{m}} A_\mathfrak{m}=S^{-1}A_\mathfrak{m}$$

    을 얻고, 이 때 $S$의 원소들 (즉 $A$의 non-zerodivisor들)이 $A_\mathfrak{m}$의 non-zerodivisor이기 때문에 얻어진다.  
    이제 fractional ideal $\mathfrak{A}$가 주어졌다 하고, $\mathfrak{A}\cap A$가 zerodivisor로만 이루어졌다 하자. 그럼 $\mathfrak{a}$가 (finitely generated) fractional ideal이라는 것으로부터, 공통분모 $a$를 찾아 $a \mathfrak{A}\subseteq A$를 $A$의 ideal이 되도록 할 수 있으며, 이제 [§동반소아이디얼, ⁋정리 7](/ko/math/commutative_algebra/associated_primes#thm7)을 적용하면 $a\mathfrak{A}$는 오로지 non-zerodivisor로만 이루어진 $A$의 ideal이므로, 이는 associated prime ideal들의 합집합에 속하고 다시 여기에 [§동반소아이디얼, ⁋보조정리 2](/ko/math/commutative_algebra/associated_primes#lem2)를 적용하면 $a\mathfrak{A}$가 실제로 어떤 $b\in A$를 annihilate하는 것을 안다. 즉, $ab$는 $\mathfrak{A}$를 annihilate하고 따라서 $\ann(ab)$를 포함하는 prime ideal $\mathfrak{p}$에서 localize를 하면 $M\_\mathfrak{p}\not\cong A\_\mathfrak{p}$임을 안다. 
3. 두 invertible module $M,N$이 주어졌다 하자. 그럼 둘째 결과에 의해 이들을 $K$ 안에 들어있는 fractional ideal로 생각할 수 있으며, 주장에서 주어진 map 또한 이렇게 정의된 것이다. 그럼 어차피 주어진 morphism들이 isomorphism이라는 것은 [§국소화의 성질들, ⁋명제 4](/ko/math/commutative_algebra/properties_of_localization#prop4)을 통해 보일 것이므로, 처음부터 $A$가 local임을 가정해도 되고, 그럼 둘째 결과에서의 논증과 invertible module의 정의에 의해 $M,N$은 모두 $A$와 isomorphic하다. 이제 $M,N$을 생성하는 $K$의 non-zerodivisor를 각각 $s,t$라 하면, 첫 번째 morphism은 원래부터 epimorphism이고, 추가로 $M\otimes_A N$을 $A\cong As\otimes_AAt$로 본다면 $M\otimes N \rightarrow MN$은 $1\otimes1$을 $st$로 보내는 것으로 이해할 수 있으므로 $st$가 non-zerodivisor라는 것으로부터 이것이 monomorphism이기도 하다는 것을 안다.
  두 번째 morphism의 경우, 우선 우리는 두 번째 결과에 의하여 적당한 non-zerodivisor $a\in A\cap M$을 택할 수 있다. 그럼 $0$이 아닌 임의의 $t\in M^{-1}N$에 대해 $ta\neq 0$이므로 $u_t$는 zero morphism이 아니고, 따라서 주장의 morphism은 monomorphism이다. 이것이 epimorphism이라는 것은 임의의 $u\in \Hom_A(M,N)$에 대하여, $u(x)=y$라 하면 $u=u_{y/x}$가 되어 성립한다. 특히 $N=A$로 두면 마지막 주장을 얻는다.
4. 우선 $M$이 invertible이라면 3번 결과에 의해 $M^{-1}\otimes M \rightarrow M^{-1}M$과 trace map $M^\ast\otimes M \rightarrow A$를 같은 것으로 볼 수 있다. 거꾸로 $K$의 임의의 $A$-submodule $M$이 $M^{-1}M=A$를 만족한다면, 위와 마찬가지로 localization을 통해 $(A,\mathfrak{m})$이 local ring이라 가정하고 $M\cong A$임을 보여도 된다. 그런데 조건 $M^{-1}M=A$에 의하여, 적당한 $y\in M^{-1}$에 대해 $yM\not\subseteq \mathfrak{m}$이도록 할 수 있고 그럼 $\mathfrak{m}$의 maximality에 의하여 $yM=A$여야 하고, 이로부터 $M$과 $A$ 사이의 isomorphism $y-$를 얻는다. 

</details>

Ring $A$ 위에 정의된 invertible module들의 isomorphism class들의 모임을 생각하자. 그럼 $\otimes$는 이 isomorphism class를 보존하므로 이 위에 이항연산을 정의하며, $\otimes$가 결합법칙과 교환법칙을 만족하고, 항등원 $A$를 갖는다. 뿐만 아니라, [정리 3](#thm3)의 첫째 결과에 의해 임의의 invertible module은 $\otimes$에 대한 역원 $M^\ast$를 가진다. 이로부터 이 모임이 abelian group이 되는 것을 안다.

비슷하게, $K$의 invertible $A$-submodule들 (즉 $A$의 invertible fractional ideal들) 또한 ideal product를 통해 group의 구조를 가지며, 이 때 [정리 3](#thm3)의 넷째 조건은 $M$의 역원이 $M^{-1}$임을 보여준다. 이들에 다음과 같이 이름을 붙인다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Ring $A$에 대하여 다음을 정의한다. 

1. $A$의 *Picard group<sub>피카르드 군</sub>* $\Pic(A)$는 $\otimes$로 연산이 주어진 invertible $A$-module들의 isomorphism class들의 group이다.
2. $A$의 *Cartier divisor<sub>카르티에 인자</sub>*들의 group $\CaDiv(A)$는 $K$의 invertible $A$-submodule들, 즉 $A$의 fractional ideal들의 group이다.

</div>

그럼 [정리 3](#thm3)로부터 다음이 자명하다.

<div class="proposition" markdown="1">

<ins id="cor5">**따름정리 5**</ins> Noetherian ring $A$에 대하여 다음이 성립한다.

1. $K$의 임의의 invertible $A$-submodule을 받아, 그 isomorphism class를 내놓는 함수 $\CaDiv(A) \rightarrow \Pic(A)$는 surjective이며, 그 kernel은 $K$의 unit들의 group $K^\times$와 isomorphic하다.
2. $\CaDiv(A)$는 $A$의 invertible ideal들에 의해 생성되는 free abelian group이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

1. 주어진 함수가 surjective인 것은 [정리 3](#thm3)의 둘째 결과이며, $K$의 임의의 unit $x$에 대하여 $Ax\subseteq K$는 이 함수에 의해 $A$로 옮겨지는 invertible module이다. 따라서 임의의 invertible submodule $M,N$이 isomorphic하여, 적당한 $x\in K^\times$에 대해 $I=xJ$라 할 수 있으므로 kernel에 대한 주장도 보일 수 있다.
2. 임의의 invertible fractional ideal $\mathfrak{A}$에 대하여, [정리 3](#thm3)의 둘째, 넷째 결과에 의해 $\mathfrak{A}^{-1}$도 invertible fractional ideal이고, 그럼 다시 [정리 3](#thm3)의 둘째 결과에 의해 $\mathfrak{A}^{-1}$은 $A$의 non-zerodivisor를 포함한다. 이를 $a$라 하면, $a \mathfrak{A}\subseteq A$이므로 $\mathfrak{A}=a \mathfrak{A}\cdot (a)^{-1}$이다. 

</details>

---

**참고문헌**

**[Eis]** David Eisenbud. *Commutative Algebra: with a view toward algebraic geometry*. Springer, 1995. 

---