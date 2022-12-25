---

title: "Étale Algebras"
excerpt: "Étale Algebras"

categories: [Math / Galois Theory]
permalink: /ko/math/galois_theory/etale_algebra
header:
    overlay_image: /assets/images/Galois_theory/Etale_algebra.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_structures"

date: 2021-09-06
last_modified_at: 
weight: 4

published: false

---
<div class="notice--warning" markdown="1">

이 글은 현재 수정중입니다.

이 글은 예전에 쓴 글로, 서술 방향이 마음에 들지 않거나 표기법이 마음에 들지 않아 전체적으로 수정이 진행중입니다. 읽으실 때 참고해주세요.

</div>

우리는 이제 separable extension을 정의할 것이다. Separable algebraic extension은 minimal polynomial이 separable polynomial, 즉 모든 근들이 서로 다른 polynomial로 나오는 extension을 뜻한다. Separable field extension을 바로 도입하는 대신, 부르바키는 separable algebra라 부를 수 있는 étale algebra를 먼저 정의한다. 

## Linear independence of homomorphisms

우선, $L$이 $K$의 extension field이고, $V$가 $K$-vector space라 하자. 그럼 $L$은 $K$-algebra이므로, $K$-vector space이기도 하고 따라서 $V$에서 $L$로의 모든 $K$-linear mapping들의 집합 $\Hom_K(V, L)$이 잘 정의된다. 이 집합은 다음의 자명한 연산

$$(f+g)(x)=f(x)+g(x),\qquad (\alpha f)(x)=\alpha f(x)\tag{1}$$

을 통해 $L$-vector space structure를 갖는다. 한편, $K$-vector space $V$에 대하여, extension of scalar를 통해 새로운 $L$-vector space $V_{(L)}=L\otimes_K V$를 얻을 수 있다. $V_{(L)}$의 dual $(V_{(L)})^*$은 $\Hom\_L(V\_{(L)}, L)$이고, 그럼

$$\Hom_L(L\otimes_K V,L)\cong\Hom_L(V\otimes_KL, L)\cong\Hom_K(V, \Hom_L(L,L))\cong\Hom_K(V,L)$$

이 성립한다. 특히, 만일 $V$가 finite-dimensional $K$-vector space라면 $\dim_KV=\dim_LV_{(L)}$이고, 따라서 $(V_{(L)})^*$ 또한 finite dimensional $L$-vector space가 된다. 앞선 식에서 $(V_{(L)})^\*\cong\Hom_K(V,L)$이었으므로, 우리는 다음의 식

$$[\Hom_K(V, L):L]=[V:K]$$

를 얻는다. 

<div class="proposition" markdown="1">

**<ins id="pp1">명제 1</ins>** $L$이 $K$의 extension field이고, $A$가 $K$-algebra라 하자. 그럼 $A$에서 $L$로의 $K$-algebra homomorphism들의 집합 $\Hom_{K\text{-alg}}(A, L)$은, $A$에서 $L$로의 $K$-vector space homomorphism들의 집합 $\Hom_K(A,L)$의 linearly independent subset이다.

</div>

약간의 motivation을 위해 $K$-algebra homomorphism과 $K$-vector space homomorphism의 차이를 생각해보자. 임의의 $K$-algebra homomorphism $f:A\rightarrow L$은 (algebra가 $K$-vector space 구조를 가지므로) 당연히 $K$-vector space homomorphism이기도 하다. 반면, $K$-linear map으로써, 식 (1)은 여기에 더하여 임의의 $\alpha\in L$에 대해 $\alpha f:A\rightarrow L$ 또한 $K$-vector space homomorphism이라는 것을 보여준다. 그러나, $\alpha f$는 당연히 $K$-algebra homomorphism이 될 수는 없다. 일반적으로

$$(\alpha f)(xy)=\alpha f(xy)=\alpha f(x)f(y)\neq(\alpha f(x))(\alpha f(y))=(\alpha f)(x)(\alpha f)(y)$$

이기 때문이다. 즉, 수많은 $\Hom_K(A,L)$의 원소들 중 $K$-algebra homomorphism이 될 수 있는 것은 일종의 normalization을 거친 homomorphism들 뿐이고, 이는 어떻게 보면 $\Hom_K(A,L)$의 (standard한) basis를 찾는 느낌이기도 하다.  
위의 명제는 이들 $\Hom\_{K\text{-alg}}(A,L)$들이 linearly independent하다는 것을 보여준다. 그렇다면 언제 이들이 $\Hom_K(A,L)$을 span하기도 할까? 즉, 언제 $\Hom\_{K\text{-alg}}(A,L)$이 $\Hom_K(A,L)$의 basis가 될까? 이것이 étale algebra의 정의다.

어쨌든, 이 명제를 증명해보자.

<details class="proof--alone" markdown="1">
<summary>명제 1의 증명</summary>

$\Hom_{K\text{-alg}}(A,L)$의 임의의 유한집합이 linearly independent인 것을 보여야 한다. 이 유한집합의 cardinality에 대한 induction으로 진행한다. $n=0$인 경우는 자명하므로, $n\geq 1$이라 하고, $\Hom\_{K\text{-alg}}(A,L)$의 $n$개의 원소들 $u_1,\ldots, u_n$과 $L$의 원소들 $\alpha_1,\ldots, \alpha_n$에 대하여

$$\alpha_1u_1+\cdots+\alpha_nu_n=0\tag{2}$$

이라 가정하자. 임의의 $x,y\in A$에 대하여

$$\begin{aligned}\sum_{i=1}^{n-1}\alpha_i[u_i(x)-u_n(x)]u_i(y)&=\sum_{i=1}^{n-1}\alpha_i u_i(xy)-u_n(x)\sum_{i=1}^{n-1}\alpha_iu_i(y)\\
&=\sum_{i=1}^n\alpha_iu_i(xy)-u_n(x)\sum_{i=1}^n\alpha_iu_i(y)=0\end{aligned}$$

이 성립하므로, $\sum_{i=1}^{n-1}\alpha_i[u_i(x)-u_n(x)]u_i=0$이 성립한다. 그런데, inductive hypothesis에 의해 $u_1,\ldots,u_{n-1}$은 linearly independent하므로, 이 말은 $\alpha_i[u_i(x)-u_n(x)]=0$이 임의의 $i=1,\ldots, n-1$과 $x\in A$에 대해 성립한다는 뜻이다. $u_i$들은 $x$의 값을 조절해 $0$이 아니도록 할 수 있으므로, 그럼 $\alpha_i=0$이 $i=1,\ldots, n$에 대해 성립한다는 뜻이고, 따라서 위의 식 (2)은 $\alpha_nu_n=0$이 된다. 특히, $\alpha_n=\alpha_nu_n(1)=0$이므로 $\alpha_i=0$ for all $i$이고, 따라서 원하는 결론을 얻는다.
</details>

위에서 잠깐 언급한 basis의 느낌으로 보자면, 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="crl2">**따름정리 2 (Dedekind's theorem)**</ins> $K$의 두 extension field $E$, $L$에 대하여, $E$에서 $L$로의 $K$-algebra homomorphism들의 집합은 $L$-linearly independent하고, 만일 $\dim_KE$가 유한이라면, 이들의 개수는 많아야 $[E:K]$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

첫 번째 주장은 [명제 1](#pp1) 그 자체다. 나머지 부분만 보자면, $\dim_KE=[E:K]$가 유한이라면 $[\Hom_K(E,L):L]=[E:K]$도 마찬가지다. 따라서 $\Hom_K(E,L)$의 linearly independent subset인 $\Hom\_{K\text{-alg}}(E,L)$은 당연히 $\Hom_K[(E,L):L]=[E:K]$를 넘을 수 없다.  

</details>

## Diagonalizable algebras and étale algebras

이제 앞에서의 motivation을 따라, étale algebra를 정의한다.

<div class="definition" markdown="1">

<ins id="df3">**정의 3**</ins> $K$-algebra $A$가 *diagonalizable*이라는 것은 적당한 자연수 $n\geq 0$이 존재하여, $A\cong K^n$이 성립하는 것이다. 만일 $K$의 어떤 extension field $L$에 대하여, $L$-algebra $A_{(L)}$이 diagonalizable이라면, $A$가 $L$에 의해 *diagonalize*되었다고 하고, 이렇게 어떤 extension field에 의해 diagonalize될 수 있는 $K$-algebra $A$를 *étale algebra*라 부른다.

</div>

즉, $A$가 étale algebra라는 것은 적당한 자연수 $n$에 대하여 다음의 식

$$L\otimes_KA\cong L^n$$

이 성립하는 것이다. $L^n$은 commutative하므로, 임의의 étale algebra는 commutative하다. 또, $\dim_LA_{(L)}=\dim_KA$이므로, étale algebra $A$는 $K$에 대해 finite degree를 갖는다. 

<div class="proposition" markdown="1">

<ins id="pp4">**명제 4**</ins> $A$가 finite-dimensional $K$-algebra라면, 다음이 모두 동치이다.

1. $A$가 diagonalizable algebra이다.
2. $A$의 basis $(e_1,\ldots, e_n)$이 존재하여, $e_i^2=e_i$이고 $e_ie_j=0$이 $i\neq j$에 대하여 항상 성립한다.
3. $A$에서 $K$로의 $K$-algebra homomorphism들의 집합 $\Hom_{K\text{-alg}}(A,K)$가 $K$-vector space $A$의 dual space를 generate한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선, $A$가 diagonalizable이라면 $K^n$들의 basis가 2번의 조건을 만족하고, 거꾸로 2번의 조건을 만족하는 basis가 존재한다면 $K^n$으로의 isomorphism을 construct할 수 있으므로 1번과 2번은 동치이다. 한편, 만약 1번이 성립한다면, $A\cong K^n$에서 $K$로의 projection들이 모두 algebra homomorphism이고, 이들은 linearly independent한 $n=\dim_K A^*$개의 원소이므로, 3번이 성립한다. 거꾸로 만일 3번이 성립한다면, 이들은 $A^\*$의 basis가 될 것이다. 그럼 $a\mapsto (u_i(a))$가 $A$에서 $K^n$으로의 isomorphism을 정의하므로 1, 2, 3이 모두 동치이다.

</details>

그럼 우리는 다음과 같이, étale algebra를 도입할 때 언급했던 motivation을 증명할 수 있다.

<div class="proposition" markdown="1">

<ins id="crl5">**따름정리 5**</ins> $L$이 $K$의 extension field라 하자. 그럼 $\Hom_{K\text{-alg}}(A,L)$의 cardinality는 $[A:K]$보다 클 수 없으며, 등호는 정확히 $A$가 $L$에 의해 diagonalize될 때 성립한다. 이 경우, 위의 집합은 $\Hom_K(A,L)$의 basis가 된다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

첫 번째 명제는 그냥 [따름정리 2](#crl2)다. 따라서 등호 조건만 살펴보면 충분하다. 우선 우리는 $L$-vector space들 간의 isomorphism $\Hom\_K(A,L)\cong A\_{(L)}^\ast$가 존재한다는 것을 알고 있다. 따라서, linearly independent subset $\Hom\_{K\text{-alg}}(A,L)\subset\Hom\_K(A,L)$의 $A\_{(L)}^\ast$에서의 image도 linearly independent subset이 된다. 뿐만 아니라, 이 isomorphism을 잘 살펴보면, 이 isomorphism $\pi$는 $u\in\Hom\_K(A,L)$을 다음의 식

$$(\pi u)(1\otimes x)=u(x)$$

을 통해 정의되는 $L$-algebra homomorphism $\pi u:A\_{(L)}\rightarrow L$로 보내며, 사실 *모든* $L$-algebra homomorphism은 이러한 꼴이라는 것을 알 수 있다. 즉, $\pi$는 $\Hom\_{K\text{-alg}}(A,L)$에서 $\Hom\_{L\text{-alg}}(A\_{(L)},L)$로의 surjective map을 정의한다. 이제 앞선 명제의 $1\iff 3$에서, $A$를 $A\_{(L)}$, $K$를 $L$로 바꾸면, $L$-algebra $A\_{(L)}$이 diagonalizable인 것은 (즉, $L$이 $A$를 diagonalize하는 것은)  $\Hom\_{L\text{-alg}}(A\_{(L)},L)$이 $L$-vector space $A\_{(L)}^\ast$를 generate하는 것과 동치라는 것을 알 수 있고, 따라서 원래의 집합 $\Hom\_{K\text{-alg}}(A,L)$는 $\Hom\_K(A,L)$의 basis가 된다.

</details>


그리고, 다음과 같이 étale algebra에 대한 statement를 얻을 수 있다.

<div class="proposition" markdown="1">

<ins id="pp6">**명제 6**</ins> $A$가 $K$-algebra이고, $\Omega$가 $K$의 algebraically closed extension이라 하자. 다음이 모두 동치이다.

1. $A$가 étale algebra이다.
2. $K$의 적당한 finite-degree의 extension이 $A$를 diagonalize시킨다.
3. $\Omega$가 $A$를 diagonialize한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $A$가 étale이라 하면, $A$는 $K$에 대해 finite degree를 갖는다. 이를 $n$이라 하자. 또, $L$이 $A$를 diagonalize하는 $K$의 extension field라 하자. 그럼 앞선 따름정리에 의하여, $\Hom_{K\text{-alg}}(A,L)$은 $n$개의 원소를 갖는다. 한편, 각각의 $u\in\Hom\_{K\text{-alg}}(A,L)$에 대하여, $[u(A):K]\leq [A:K]=n$이 성립한다. 따라서, $u(A)$들로 generate되는 $L$의 subextension은 $K$에 대해 finite degree를 갖는다. 이 subextension $L'$은 $u(A)$들을 모두 포함하고 있으므로, $A$에서 $L'$로 가는 homomorphism은 여전히 $n$개가 있고, 앞선 동치조건에 의하여 $L'$은 $A$를 diagonalize한다.  
이제, 만약 2번이 성립한다면, finite-degree extension은 algebraic extension이고 따라서 $\Omega$의 subextension이므로 3번이 성립하는 것은 자명하다. 또, 3번에 의해 1번이 성립하는 것은 그냥 정의다.

</details>

<div class="proposition" markdown="1">

<ins id="pp7">**명제 7**</ins> <#content#>

</div>

## Separable degree

처음 시작하며 말했듯, étale algebra를 정의하는 이유는 separable extension을 정의하기 위한 것이다. Separable extension은 다음에 정의하게 되겠지만, 우선 separable degree를 정의할 수 있다. $K$에 대해 finite degree를 갖는 commutative algebra $A$에 대하여, 우리는 이 extension의 separable degree를 $A$에서 $K$의 algebraical closed extension $L$로 가는 $K$-algebra $\Hom_{K\text{-alg}}(A,L)$으로 정의할 것이다. 이 값은 $n$으로 bound되어있으므로 항상 유한하지만, 일반적으로 $K$의 algebraic closed extension은 유일하지 않으므로 이 값이 $L$의 선택에 의존하지 않음을 보여야 한다. 다음 보조정리에서, $\Hom\_{K\text{-alg}}(A,L)$의 값을 $h(L)$로 적자.  

<div class="proposition" markdown="1">

<ins id="lem8">**보조정리 8**</ins> $K$의 algebraic closure $\Omega$에 대하여, $h(L)\leq h(\Omega)$가 임의의 extension $L$에 대해 성립하며, 등호는 $L$이 algebraically closed일 때 성립한다.  

</div>

그러므로 다음이 잘 정의된다.

<div class="definition" markdown="1">

<ins id="df9">**정의 9**</ins> $K$의 algebraically closed extension $L$에 대하여, 위에서 정의한 값 $h(L)$을 $A$의 *separable degree*라 부르고, $[A:K]_s$로 적는다.

</div>

이것이 degree라 불리려면, 우리가 예상하는 몇 가지 성질들, 예컨대 다음의 성질들을 만족해야 한다.

$$\begin{aligned}[A\otimes_KB:K]_s&=[A:K]_s[B:K]_s\\ [A_{(K')}:K']_s&=[A:K]_s\\ [A':K]_s&=[A':K']_s[K':K]_s\end{aligned}$$

우선, 첫 번째 식을 보이기 위해 $\Hom\_{K\text{-alg}}(A, L)$, $\Hom\_{K\text{-alg}}(B, L)$, $\Hom_{K\text{-alg}}(A\otimes_KB, L)$들을 생각하자. 정의에 의해, 이들의 cardinality가 각각 $[A:K]_s$, $[B:K]_s$, $[A\otimes_KB:K]_s$이다. 그런데, tensor product의 universal property에 의해서 $\Hom\_{K\text{-alg}}(A, L)\times\Hom\_{K\text{-alg}}(B, L)$의 원소 $(u,v)$와, $\Hom\_{K\text{-alg}}(A\otimes_KB, L)$의 원소 $u\otimes v$가 일대일로 대응된다.

두 번째 식은 간단히 $\Hom\_\text{K'-alg}(A_{(K')}, L)$와 $\Hom_{K\text{-alg}}(A, L)$ 사이의 일대일 대응이 $\hat{u}(x)\leftrightarrow u(1\otimes x)$으로 주어지므로 자명하다.

마지막 식을 보이기 위해, 두 개의 집합 $\Hom_{K\text{-alg}}(K', L)$, $\Hom\_{K\text{-alg}}(A',L)$을 생각하자. 각각의 $\sigma\in\Hom\_{K\text{-alg}}(K', L)$에 대하여, $\Hom\_{K\text{-alg}}(A',L)$의 부분집합 $S\_\sigma$를 $f(\alpha\cdot 1)=\sigma(\alpha)$를 만족하는 $f$들의 모임으로 정의하자. 그럼 $S\_\sigma$들의 모임은 $\Hom\_{K\text{-alg}}(A',L)$의 partition이 된다. 그런데 각각의 $S\_\sigma$는 정의에 의해 $A'$에서 $L$로의 *$K'$-algebra homomorphism*들로 이루어져 있으므로, 각각의 $S\_\sigma$의 cardinality는 $[A':K']_s$가 되어 증명이 끝난다. 

<div class="proposition" markdown="1">

<ins id="pp10">**명제 10**</ins> Finite degree를 갖는 commutative $K$-algebra $A$에 대하여, $[A:K]_s\leq[A:K]$가 항상 성립하며, 등호는 정확히 $A$가 étale algebra일 때 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선, $[A:K]_s\leq [A:K]$는 [따름정리 2](#crl2)에 의해 성립한다는 것을 증명했었다. 이후 [따름정리 5](#crl5)에서 우리는 등호가 성립할 조건이 $A$가 $L$에 의해 diagonalize될 때라는 것을 살펴봤는데, [명제 6](#pp6)의 세 번째 동치조건에서 이는 $A$가 étale algebra인 것과 동치이다.

</details>

그럼 위의 식에서, $C=A\otimes_KB$가 étale인 것은 $A$와 $B$가 모두 étale인 것과 동치라는 것을 확인할 수 있다. 뿐만 아니라, 나머지 식들을 이용하면 $A$가 étale인 것은 $A_{(K')}$가 etal인 것과 동치이고, 또 $A'$가 étale인 것은 $A'$가 étale $K'$-algebra이고, $K'$가 étale $K$-algebra라는 것을 알 수 있다.

## Differential criterion

앞서 separable extension은 separable polynomial에서 그 motivation을 찾을 수 있다고 했었는데, 사실 separble polynomial을 찾을 때 가장 쉬운 방법은 [§Polynomials, 명제 18](/ko/math/galois_theory/polynomials#pp18)과 같이 미분을 해서 근을 비교하는 것이다. Étale algebra도 어쨌든 separable extension과 모종의 관계가 있다고 했으므로, étale algebra의 Kähler differential module에 관심을 가지는 건 어떻게 보면 당연한 일일 것이다.

<div class="proposition" markdown="1">

<ins id="thm11">**정리 11**</ins> Finite degree를 갖는 commutative $K$-algebra $A$가 étale인 것은, $\Omega_K(A)$가 0인 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

증명이 꽤 많이 길다. 

우선, $K$의 algebraic closure $L$을 생각하자. [명제 6](#pp6)에 의해, $A$가 étale이라는 것은 $A_{(L)}$이 diagonalizable인 것이다. 또, [§Polynomials, 명제 20](/ko/math/galois_theory/polynomials#pp20)에 의하여 $\Omega_K(A)\otimes_AA_{(L)}\cong\Omega_L(A_{(L)})$이 성립하므로 $\Omega_L(A_{(L)})$은 $\Omega_K(A)\otimes_KL$과 isomorphic하다. 이제, $\Omega_K(A)=0$인 것은 $\Omega_L(A_{(L)})=0$인 것과 동치이므로, 이 정리는 $K$가 algebraically closed field인 경우, $A$가 diagonalizable인 것과 $\Omega_K(A)=0$인 것이 동치라는 것만 보이면 된다. 

우선 $A$가 diagonalizable이라 가정하자. 그럼 $A$는 $A$의 idempotent들로 generate되므로, $\Omega_K(A)=0$이기 위해서는 이들의 image $de$들이 모두 0이면 된다. 그런데

$$de=d(e^2)=2e\mathop{de}$$

이고, 따라서 $e\mathop{de}=2e^2\mathop{de}=2e\mathop{de}$이므로 $ede=0$이 되어 $de=2e\mathop{de}=0$가 성립한다.

반대 방향은 $A$의 degree에 대한 induction으로 증명한다. 이를 위해 두 가지 fact를 우선 가정하자.

- Algebraically closed field $K$와, $\Omega_K(A)=0$을 만족하는 $K$의 finite-degree extension $A$에 대해, $A$의 임의의 maximal ideal $\mathfrak{m}$은 $\mathfrak{m}=\mathfrak{m}^2$을 만족한다.
- 임의의 commutative ring $A$와, $\mathfrak{a}=\mathfrak{a}^2$을 만족하는 $A$의 finitely generated ideal $\mathfrak{a}$에 대하여, 적당한 idempotent $e\in A$가 존재하여 $\mathfrak{a}=Ae$가 성립한다.

이들 둘을 가정하면 나머지는 어렵지 않다. 우선, $A$의 maximal ideal $\mathfrak{m}$이 주어졌다고 하자. 그럼 첫 번째 fact에 의해, $\mathfrak{m}=\mathfrak{m}^2$이고, 따라서 두 번째 fact에 의해 $\mathfrak{m}=Ae$인 $e\in A$가 존재한다. 그럼 $A/\mathfrak{m}$은 $K$에 대해 degree가 1이다. 또, $A=(1-e)A\oplus eA$이다. $\mathfrak{a}=(1-e)A$라 하자. 그럼 $A/\mathfrak{m}$이 $K$에 대해 degree가 1이므로, $[\mathfrak{a}:K]=1$이고 따라서 $A\cong K\times A/\mathfrak{a}$가 성립한다. 그런데 $\Omega(A/\mathfrak{a})$는 $\Omega_K(A)$의 quotient와 isomorphic하고, $\Omega_K(A)=0$이었으므로 inductive hypothesis에 의해 $A/\mathfrak{a}$가 diagonalizable하다.

</details>

위에서 쓴 두 가지 fact를 증명해야 한다.

<div class="proposition" markdown="1">

<ins id="lem12">**보조정리 12**</ins> Algebraically closed field $K$와, $\Omega_K(A)=0$을 만족하는 $K$의 finite-degree extension $A$에 대해, $A$의 임의의 maximal ideal $\mathfrak{m}$은 $\mathfrak{m}=\mathfrak{m}^2$을 만족한다.

</div>

<div class="proposition" markdown="1">

<ins id="lem13">**보조정리 13**</ins> 임의의 commutative ring $A$와, $\mathfrak{a}=\mathfrak{a}^2$을 만족하는 $A$의 finitely generated ideal $\mathfrak{a}$에 대하여, 적당한 idempotent $e\in A$가 존재하여 $\mathfrak{a}=Ae$가 성립한다.

</div>

## Reduced algebra and étale algebra

<div class="proposition" markdown="1">

<ins id="pp14">**명제 14**</ins> $A$가 commutative, finite-degree $K$-algebra라고 하자. 그럼 $A$가 reduced ring인 것은 적당한 $K$의 extension field들 $L_1,\ldots, L_n$이 존재하여 $A\cong L_1\times\cdots\times L_n$인 것과 동치이다. 

</div>

<div class="proposition" markdown="1">

<ins id="lem15">**보조정리 15**</ins> Perfect field $P$의 finite-degree reduced extension $B$는 반드시 étale $P$-algebra이다.

</div>

<div class="proposition" markdown="1">

<ins id="thm15">**정리 15**</ins> $A$가 finite-degree를 갖는 commutative $K$-algebra라 하자. 그럼 다음이 모두 동치이다.

1. $A$는 étale이다.
2. $K$의 임의의 extension field $L$에 대하여 $L\otimes_KA$가 reduced이다.
3. $K$의 perfect extension field $P$가 존재하여 $P\otimes_KA$가 reduced이다. 

</div>

---
**Reference**

**[BCH]** N. Bourbaki, P.M. Cohn, and J. Howie. <i>Algebra II: Chapters 4 - 7</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013. 

---
