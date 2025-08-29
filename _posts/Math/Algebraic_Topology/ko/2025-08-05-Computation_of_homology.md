---

title: "호몰로지의 계산"
excerpt: ""

categories: [Math / Algebraic Topology]
permalink: /ko/math/algebraic_topology/computation_of_homology
header:
    overlay_image: /assets/images/Math/Algebraic_Topology/Computation_of_homology.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_topology-ko"

date: 2025-08-05
last_modified_at: 2025-08-05
weight: 5

---

우리는 이제 호몰로지를 실질적으로 계산할 수 있는 도구들을 살펴본다. 임의의 공간에 대해 이 공간의 호몰로지를 정의로부터 직접 계산하는 것은 거의 불가능한 일이므로, 우리는 큰 공간들을 작은 공간으로 쪼개고 이들의 호몰로지들로부터 큰 공간의 호몰로지를 계산하는 도구를 개발해야 한다. 가장 직관적인 상황은 Seifert-van Kampen 정리([§피복공간, ⁋정리 13](/ko/math/algebraic_topology/covering_spaces#thm13))의 상황일 것이며, 이 경우 우리는 functor $\pi_1:\Top \rightarrow \Grp$이 colimit을 보존하는 것을 살펴보았다. 그런데 abelianization functor $\ab:\Grp \rightarrow \Ab$는 forgetful functor $U:\Ab \rightarrow \Grp$의 left adjoint functor이고 ([\[대수적 구조\] §가환군, ⁋명제 7](/ko/math/algebraic_structures/abelian_groups#prop7)), left adjoint functor는 colimit을 보존하며 ([\[범주론\] §수반함자, ⁋정리 9](/ko/math/category_theory/adjoints#thm9)) first homology functor $H_1:\Top \rightarrow \Ab$는 이들의 합성이므로 ([§피복공간, ⁋정리 15](/ko/math/algebraic_topology/covering_spaces#thm15)) 또한 colimit을 보존해야 한다. 특별히 [§피복공간, ⁋따름정리 14](/ko/math/algebraic_topology/covering_spaces#cor14)와 같이 위상공간 $X$가 두 connected open subset $U,V$의 합집합으로 나타난다 하자. 그럼 category $\Ab$에서, 두 abelian group의 pushout은 이들의 direct sum의 coequalizer로 주어지므로 다음의 isomorphism 

$$H_1(X)=H_1(U\cup V)\cong \frac{H_1(U)\oplus H_1(V)}{\left\langle (f(x),-g(x))\mid x\in H_1(U\cap V)\right\rangle}$$

이 성립해야 한다. 이번 글에서 우리는 이를 더 일반적인 방식으로 다루게 된다. 

## Relative homology

이를 위해서는 우선 호몰로지를 일반화할 필요가 있다. 공간 $X$와 임의의 부분공간 $A$에 대하여, $k$번째 relative chain group $C_k(X,A)$를 다음의 quotient

$$C_k(X,A):=C_k(X)/C_k(A)$$

으로 정의하자. 그럼 어렵지 않게 boundary map $\partial_k:C_k(X) \rightarrow C_{k-1}(X)$이 quotient group들 사이의 map $C_k(X,A) \rightarrow C_{k-1}(X,A)$를 유도하는 것을 안다. 이로부터 다음의 chain complex

$$\cdots \longrightarrow C_k(X,A)\overset{\partial}{\longrightarrow} C_{k-1}(X,A)\longrightarrow$$

를 만들 수 있다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 위의 chain complex의 $k$번째 호몰로지 $H_k(X,A)$를 *relative homology*라 부른다. 

</div>

이제 category $\Ch(\Ab)$에서의 short exact sequence

$$0 \rightarrow C_\bullet(A) \rightarrow C_\bullet(X) \rightarrow C_\bullet(X,A) \rightarrow 0$$ 

을 생각하자. 그럼 [\[호몰로지 대수학\] §긴 완전열, ⁋정리 1](/ko/math/homological_algebra/long_exact_sequence#thm1)에 의하여 다음의 long exact sequence

$$\cdots \rightarrow H_k(A) \rightarrow H_k(X) \rightarrow H_k(X,A)\rightarrow H_{k-1}(A) \rightarrow \cdots$$

이 존재한다. 이 때 connecting map $H_k(X,A) \rightarrow H_{k-1}(A)$는 $H_k(X,A)$의 임의의 cycle(의 임의의 representative)에 boundary map을 취한 것에 불과하다. 뿐만 아니라, 만일 continuous map $f:X \rightarrow Y$가 $f(A)\subseteq B$를 만족한다면 $f$가 기존의 chain map $C_\bullet(X)\rightarrow C_\bullet(Y)$ 외에도 $C_\bullet(A) \rightarrow C_\bullet(B)$를 유도하고, 다음 diagram 

![relative_homology](/assets/images/Math/Algebraic_Topology/Computation_of_homology-1.png){:style="width:12em" class="invert" .align-center}

이 commute한다는 것으로부터 chain map $C_\bullet(X,A) \rightarrow C_\bullet(Y,B)$ 또한 유도된다. 즉, 이러한 조건을 만족하는 $f:(X,A) \rightarrow (Y,B)$는 homology에서의 map $H_k(f):H_k(X,A) \rightarrow H_k(Y,B)$ 또한 유도한다. 그럼 [§호모토피, ⁋명제 6](/ko/math/algebraic_topology/homotopy#prop6)을 $X$와 $A$ 각각에 적용하고 [\[호몰로지 대수학\] §Digram chasing, ⁋따름정리 2](/ko/math/homological_algebra/diagram_chasing#cor2)를 사용하면 이 조건을 만족하는 homotopic한 연속함수들 $f,g$가 호몰로지에서 같은 함수를 유도하는 것을 안다. 

## Excision theorem

직관적으로 $(X,A)$에 대한 realtive homology $H_\bullet(X,A)$는 inclusion $C_\bullet(A)\hookrightarrow C_\bullet(X)$의 cokernel에 해당하는 chain complex $C_\bullet(X,A)$의 호몰로지이다. 직관적으로 이 과정에서 $C_\bullet(A)$에 대한 정보는 quotient를 취하며 사라지게 되므로, $A$ 안에 들어있는 부분집합을 전체에서 뺀다고 해서 relative homology가 변하지 않을 것이라는 것은 직관적으로는 그럴듯해보인다. 이는 다음의 약한 조건 하에서는 참이다. 

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2 (Excision theorem)**</ins> 공간 $X$의 부분공간 $A$와, $A$의 부분공간 $Z$가 $\cl Z\subseteq \interior A$를 만족한다고 하자. 그럼 inclusion

$$(X\setminus Z, A\setminus Z)\hookrightarrow (X,A)$$

에 의해 유도되는 

$$H_k(X\setminus Z, A\setminus Z)\rightarrow H_k(X,A)$$

는 isomorphism이다. 

</div>

그러나 이 정리가 직관적으로 자명한 것에 비해, 그 증명은 다소 기술적인 부분이 있어 여기에서는 그 증명을 생략하기로 한다. 

한편 우리는 기하적인 상황에서 이와 같이 $A$에 들어있는 정보를 무시하는 방법을 알고 있다. 즉, $A$를 하나의 점으로 줄이는 quotient space $X/A$이다. 그럼 homology $H_k(X/A)$와 relative homology $H_k(X,A)$ 사이의 관계가 있다는 것이 합리적인 추측이다. 물론 위의 정리와 마찬가지로 이는 $A$가 아주 이상한 공간은 아니어야 가능하다. 

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 공간 $X$와 부분공간 $A$에 대하여, 이들 $(X,A)$가 *good pair*라는 것은 $A$가 닫힌집합이고, $X$의 적당한 열린집합 $U$가 존재하여 $A\subset U$이고 $A$가 $U$의 strong deformation retract인 것이다. 

</div>

Good pair $(X,A)$가 주어졌다 하고, $U$가 [정의 3](#def3)의 가정을 만족하는 열린집합이라 하자. 그럼 다음의 diagram

![3*3_diagram](/assets/images/Math/Algebraic_Topology/Computation_of_homology-2.png){:style="width:26em" class="invert" .align-center}

에서, 각 행은 모두 exact이며 처음 두 열도 exact이므로 [\[호몰로지 대수학\] §Diagram chasing, ⁋따름정리 7](/ko/math/homological_algebra/diagram_chasing#cor7)에 의하여 chain complex들의 short exact sequence

$$0\rightarrow C_\bullet(U,A)\rightarrow C_\bullet(X,A)\rightarrow C_\bullet(X,U)\rightarrow 0$$

그리고 이로부터 얻어지는 long exact sequence

$$\cdots \rightarrow H_k(U,A) \rightarrow H_k(X,A)\rightarrow H_k(X,U)\rightarrow H_{k-1}(U,A)\rightarrow \cdots$$

를 얻는다. 그런데 $A$가 $U$의 strong deformation retract라는 가정으로부터 $H_k(U,A)=0$이 모든 $k$에 대해 성립하고 따라서 isomorphism $H_k(X,A)\cong H_k(X,U)$이 모든 $k$에 대해 성립한다. 

한편 임의의 closed subspace $A$에 대하여, $A$를 한 점으로 줄여서 만드는 quotient space $X/A$가 잘 정의되며, 이 때 projection $X \rightarrow X/A$는 $A$를 한 점 $[A]$으로 보내고, $A$ 바깥에서는 homeomorphism인 함수이다. 이 때, 포함관계 

$$\{[A]\}\subseteq U/A\subseteq X/A$$

에 위와 마찬가지 논증을 적용하면 $U/A$가 한 점 $[A]$로 strong deformation retract하므로 $H_k(U/A,[A])=0$으로부터 다음의 isomorphism

$$H_k(X/A, [A])\cong H_k(X/A, U/A)$$

을 얻으며 이들은 quotient map에 의해 유도되는 다음의 diagram

![excision-1](/assets/images/Math/Algebraic_Topology/Computation_of_homology-3.png){:style="width:16em" class="invert" .align-center}

에 넣을 수 있다. 이제 $(X,A)$가 good pair라는 가정으로부터, $A\subset U\subset X$는 [정리 2](#thm2)의 조건 $\cl A\subseteq \interior U$를 만족하고 따라서 inclusion 

$$(X\setminus A, U\setminus A)\hookrightarrow (X,U)$$

에 의해 유도되는 $H_k(X\setminus A, U\setminus A)\rightarrow H_k(X,U)$는 isomorphism이며, 마찬가지로 포함관계 $\\{[A]\\}\subseteq U/A\subseteq X/A$에 [정리 2](#thm2)을 적용하면 다음의 map

$$H_k((X/A)\setminus [A], (U/A)\setminus [A])$$

이 isomorphism이라는 것을 안다. 이들은 마찬가지로 quotient map에 의해 유도되는 다음의 diagram

![excision-2](/assets/images/Math/Algebraic_Topology/Computation_of_homology-4.png){:style="width:24em" class="invert" .align-center}

에 들어가는데, 이 때 왼쪽 수직방향의 $H_k(X\setminus A, U\setminus A)\rightarrow H_k((X/A)\setminus [A], (U/A)\setminus [A])$는 quotient map $p:X\rightarrow X/A$가 $A$ 바깥에서는 homeomorphism이라는 가정으로부터 isomorphism이 된다. 이 결과들을 종합하면 다음의 isomorphism

$$H_k(X,A)\cong H_k(X/A,[A])\tag{1}$$

을 얻는다. 

한편, [§호몰로지, ⁋명제 11](/ko/math/algebraic_topology/homology#prop11)와 [\[호몰로지 대수학\] §Digram chasing, ⁋따름정리 2](/ko/math/homological_algebra/diagram_chasing#cor2)에 의해, 임의의 공간 $X$와 한 점 $x\in X$에 대하여 다음의 long exact sequence

$$\begin{aligned}\cdots &\rightarrow H_k(x)\rightarrow H_k(X)\rightarrow H_k(X,x) \rightarrow H_{k-1}(x)\rightarrow\cdots \\\cdots&\rightarrow H_1(x)\rightarrow H_1(X) \rightarrow H_1(X,x) \rightarrow H_0(x) \rightarrow H_0(X)\rightarrow H_0(X,x)\rightarrow 0\end{aligned}$$

는 모든 $k>1$에 대하여 isomorphism $H_k(X)\cong H_k(X,x)$을 준다. 뿐만 아니라, $k=1$인 경우의 long exact sequence를 보면 

$$0 \rightarrow H_1(X) \rightarrow H_1(X, x) \overset{\partial}{\longrightarrow} H_{0}(x) \overset{\iota_\ast}{\longrightarrow} H_{0}(X)$$

인데, 이 때 $\iota_\ast$는 $H_0(x)$의 generator를 $x$를 포함하는 $X$의 path component로 보내므로 injective이고, 따라서 $\partial$은 zero map이며 이로부터 마찬가지의 isomorphism $H_1(X)\cong H_1(X,x)$을 얻는다. 

한편 $\iota_\ast$가 injective라는 사실로부터 우리는 다음의 long exact sequence

$$0 \rightarrow H_0(x)\rightarrow H_0(X) \rightarrow H_0(X,x)\rightarrow 0$$

를 얻고, 이로부터 isomorphism $H_0(X,x)\cong H_0(X)/\mathbb{Z}$를 얻는다. 기하학적으로 이는 $H_0(X)$의 path component 중 $x$를 포함하는 path component를 없애는 것과 같다. 표기의 깔끔함을 위해 *reduced homology* $\widetilde{H}_k(X)$를 고정된 $x\in X$에 대하여 

$$\widetilde{H}_k(X)=H_k(X,x)$$

으로 정의하면, 위의 isomorphism (1)의 우변을 $\widetilde{H}_k(X/A)$로 바꾸어 다음과 같이 쓸 수 있다. 

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> Good pair $(X,A)$에 대하여, quotient map $X \rightarrow X/A$는 모든 $k$에 대해 다음의 isomorphism

$$H_k(X,A)\cong \widetilde{H}_k(X/A)$$

을 유도한다. 

</div>

## 심플렉스 호몰로지와 특이 호몰로지

한편 relative homology는 정의한 방식은 $\Ch(\Ab)$에서의 monomorphism $C_\bullet(A)\rightarrow C_\bullet(X)$에 cokernel을 취한 것이었으므로, 이 과정은 $C^\Delta_\bullet(A) \rightarrow C^\Delta_\bullet(X)$에 대해 반복해도 된다. 그럼 그 결과로 우리는 simplicial homology 버전의 realtive homology $H_n^\Delta(X,A)$를 얻게 된다. 이제 simplicial homology는 "singular하지 않은" chain들이므로, inclusion 

$$C_\bullet^\Delta(X) \rightarrow C_\bullet(X)$$

에 의해 유도되는 canonical homomorphism 

$$H_\bullet^\Delta(X)\rightarrow H_\bullet(X)\tag{2}$$

이 존재하며, 비슷하게 다음의 canonical homomorphism들

$$H_\bullet^\Delta(A)\rightarrow H_\bullet^\Delta(A),\qquad H_\bullet^\Delta(X,A)\rightarrow H_\bullet(X,A)$$

이 존재한다. 그럼 이들은 [\[호몰로지 대수학\] §긴 완전열, ⁋명제 2](/ko/math/homological_algebra/long_exact_sequence#prop2)에 의하여 다음의 commutative diagram

img

을 정의한다. 이를 사용하면 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5**</ins> 임의의 $\Delta$-complex $X$에 대하여, (2)의 homomorphism은 isomorphism이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

대략적인 흐름을 소개한다. 위의 commutative diagram에 의하여, $X$의 $\Delta$-complex 구조가 정의하는 filtration

$$X_0\subset X_1\subset\cdots\subset X_n=X$$

을 생각한 후 [\[호몰로지 대수학\] §Diagram chasing, ⁋따름정리 2](/ko/math/homological_algebra/diagram_chasing#cor2)를 다음 diagram

img

에 적용하여 귀납법을 돌리자. 이를 위해서는 임의의 $n$과 임의의 $k$에 대하여 relative homology들 사이의 homomorphism

$$H_n^\Delta(X^k, X^{k-1})\rightarrow H_n(X^k, X^{k-1})$$

이 isomorphism임을 보이면 된다. 

우선 정의에 의하여, $C_\bullet^\Delta(X^k, X^{k-1})$은 오직 $n=k$일 때만 nontrivial하며, 따라서 $H_n^\Delta(X^k, X^{k-1})$은 오직 $n=k$일 때만 ($n$-simplex들로 생성되는) nontrivial free abelian group이고, 다른 경우는 모두 trivial하다. 비슷하게 singular homology에 대해서도 $H_n(X^k,X^{k-1})$은 오직 $n=k$일 때만 nontrivial free abelian group이므로 우리는 오직 $H_k^\Delta(X^k, X^{k-1})\rightarrow H_k(X^k, X^{k-1})$이 isomorphism인 것만 보이면 충분하고, 이 함수는 inclusion map $C_k^\Delta(X^k, X^{k-1})\rightarrow C_k(X^k, X^{k-1})$이므로 결국 이 문제는 이 inclusion map의 surjectivity를 보이는 것으로 귀결된다.

임의의 $\sigma\in H_k(X^k, X^{k-1})$이 주어졌다 하자. 만일 $\sigma:\Delta^k \rightarrow X^k$가 $H_k(X^k, X^{k-1})$에서 nonzero라면, 적어도 하나의 $x\in \Delta^k$가 존재하여 $\sigma(x)$가 $X^k\setminus X^{k-1}$에 포함되어야 하고, 따라서 이 점 $\sigma(x)$를 interior로 포함하는 $X^k$의 $k$-simplex가 존재한다. 뿐만 아니라 $\Delta^n$은 connected이므로, 이러한 조건을 만족하는 $k$-simplex는 유일하게 결정되며 이 $k$-simplex가 정확히 $\sigma$의 $H_k^\Delta(X^k, X^{k-1})\rightarrow H_k(X^k, X^{k-1})$에 의한 preimage가 된다. 

</details>

## Eilenberg-Steenrod axiom

Excision은 예를 들어 앞선 증명에서 $k-1$보다 작은 simlpex들 무시할 때도 씀

너무 중요해서 axiom에도 넣음

definition - axiom

이것 만족하면 다 같으나 흥미로운 것들은 이들 중 일부를 만족하지 않음

참고로 이거 보면 A-module로 올리기 가능

## Mayer-Vietoris sequence

마참내 MV Seq. 